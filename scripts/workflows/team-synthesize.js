export const meta = {
  name: 'team-synthesize',
  description: "T3.6 synthesis: per team member, mine all paper cards into 07/08, conservatively update SKILL.md within a word budget while writing 09-evidence-ledger.md and the technique catalog, then adversarial review and fix until the gates pass",
  whenToUse: 'After team-read: every member batch carded, verify_card_quotes.py all exact, mark_read_from_cards.py run (research-team playbook, stage T3.6).',
  phases: [
    { title: 'Mine', detail: 'quote gate, then aggregate all cards into 07-paper-cards.md and 08-deep-reading-synthesis.md' },
    { title: 'Edit', detail: 'conservative SKILL.md update within the word budget + 09 ledger + technique catalog' },
    { title: 'Verify', detail: 'three read-only skeptics: fidelity, rules, usefulness' },
    { title: 'Fix', detail: 'apply confirmed findings; rerun gates; one more fix round if a gate still fails' },
  ],
}

/*
 * team-synthesize.js · research-team kit, stage T3.6 (cards → skill).
 * Launch:  Workflow({ scriptPath: '<repo>/scripts/workflows/team-synthesize.js', args: { ... } })
 *
 * Args shared by all team workflows:
 *   args.repo     absolute path of the nuwa repo (has scripts/, references/)
 *   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
 *   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
 *   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
 *   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
 *                 dblp, orcid, homepage, chase_hints, student_mode); each member runs through pipeline()
 *                 independently (no barrier between members)
 *
 * Args specific to team-synthesize:
 *   args.wordBudget  target SKILL.md length in words (default 11500; the kit's lesson: ~11-12k, with the exhaustive
 *                    evidence in references/research/09-evidence-ledger.md written in the same pass)
 *   args.maxWords    hard gate for wc -w SKILL.md (default wordBudget + 1500)
 *   args.notes       optional {slug: "member-specific notes for the synthesis"} (e.g. known name collisions)
 *
 * Writes (per member): references/research/07-paper-cards.md, 08-deep-reading-synthesis.md, 09-evidence-ledger.md,
 *   references/technique-catalog.md, SKILL.md, 01-publications.md, 06-trajectory.md, sources/RESOURCES.md
 *   (+ proof-playbook.md / open-problems.md / reading-path.md for a student_mode member).
 *   Backup of SKILL.md before editing: <scratch>/<slug>-SKILL.before-synth-<date>.md.
 * A member whose card quotes are not all exact is blocked at Mine (nothing is edited) and reported.
 * Next: commit per member; team-tighten.js only if SKILL.md is still over budget; then team-integrate.js.
 * Cost baseline (worked example product/dfo-team/): ~6 agents and ~2.4M tokens per member.
 */

const a = (typeof args === 'string' ? JSON.parse(args) : args) || {}
function need(keys) {
  const miss = keys.filter(k => a[k] === undefined || a[k] === null || a[k] === '')
  if (miss.length) throw new Error(`team-synthesize: missing args: ${miss.join(', ')} (see the header comment)`)
}
need(['repo', 'team', 'scratch', 'date', 'members'])
if (!Array.isArray(a.members) || !a.members.length) throw new Error('team-synthesize: args.members must be a non-empty array of team.json member objects')
if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error('team-synthesize: args.date must be "YYYY-MM-DD"')
a.members.forEach((m, i) => { if (!m || !/^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') || !m.name) throw new Error(`team-synthesize: members[${i}] needs a kebab-case slug and a name`) })
if (!String(a.repo).startsWith('/') || !String(a.scratch).startsWith('/')) throw new Error('team-synthesize: args.repo and args.scratch must be absolute paths')
if (String(a.team).startsWith('/')) throw new Error('team-synthesize: args.team must be relative to args.repo, e.g. "product/<team>"')
// args keys this workflow reads; anything else is logged (the kit mixes snake_case and camelCase option names)
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'wordBudget', 'maxWords', 'notes']
const unknownArgs = Object.keys(a).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-synthesize.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)

const REPO = String(a.repo).replace(/\/+$/, '')
const TEAM_REL = String(a.team).replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCR = String(a.scratch).replace(/\/+$/, '')
const DATE = a.date
const BUDGET = Number(a.wordBudget || 11500)
const MAXW = Number(a.maxWords || BUDGET + 1500)
const MEMBERS = a.members

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A() needs opts.phase and opts.label')
  return agent(prompt, opts)
}
function skillDir(m) { return `${TEAM}/${m.slug}` }
function backup(m) { return `${SCR}/${m.slug}-SKILL.before-synth-${DATE}.md` }

function teamCtx(m) {
  return `Team: ${TEAM}/. Read ${TEAM}/team.json first: "field" is the research field, "language" the language of the member skills, "roundtable" the roundtable folder, "chase_hints" field-wide open repositories, and "members" the researchers (hint, student_mode, chase_hints). The team was built with the nuwa kit in ${REPO} (rules and templates in ${REPO}/references/, tools in ${REPO}/scripts/). Today is ${DATE}.
Member: ${m.name} (slug ${m.slug}${m.hint ? `; ${m.hint}` : ''}). Skill folder: ${skillDir(m)}/. Where this prompt and the member's entry in team.json differ, team.json wins.`
}

const RULES = `House rules (non-negotiable):
- Evidence: every claim carries card ids with pages (e.g. [S012 p. 9]); quotes are copied verbatim from a card that copied them verbatim from the text; never put a paraphrase inside quotation marks; write "not read" rather than guess.
- Sources: only public, legitimate material. Never Sci-Hub, LibGen, any paywall circumvention, or scraping behind a login.
- Privacy: never open, read or quote anything under a references/sources/private/ folder. Never put the user's e-mail address into a request to an outside service.
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCR}/. Do not git commit, push, stash, reset or checkout (the operator commits after the stage). Stop a process by its exact PID, never with pkill -f <pattern>.`

function ctx(m) {
  const SK = skillDir(m)
  const notes = a.notes && a.notes[m.slug] ? `Member-specific notes from the operator: ${a.notes[m.slug]}\n` : ''
  return `${teamCtx(m)}

Context: ${m.name}'s research-craft skill is ${SK}/SKILL.md, written in team.json "language"; the team's roundtable skill is ${TEAM}/<roundtable>/SKILL.md (folder named in team.json). The skill was first built from web research (references/research/01–06) without full-text reading. The deep reading has since run for this member:
- Publication list: ${SK}/references/sources/publications/works.json and scholar.md.
- Full-text index: ${SK}/references/sources/papers/INDEX.md (Full text, Role, Read columns); texts in papers/txt/ (git-ignored, [[page N]] markers); abstracts in papers/abstracts.json.
- Paper cards: ${SK}/references/research/cards/*.md with matching *.digest.json (batch prefix c = core full cards, s = supplement short cards, b = books read at chapter level, a = abstract-level cards; later rounds look like c2-01; ids starting with B are open book material such as tables of contents, errata, addenda and published reviews).
${notes}Cards sometimes record inconsistencies the reader noticed inside a work (typos, a table that disagrees with the text, results that look carried over between papers). These are reading notes, not findings about the researcher: never surface them in SKILL.md or the reference files as criticism of ${m.name} or coauthors; at most a neutral general lesson without naming the work.
House rules for the update: ${REPO}/references/paper-reading-card.md section 三 (conservative update: only add; mark contradictions instead of deleting; existing methods get evidence, not duplicates; a new core method needs ≥3 distinct works' cards plus the four-way validation; reject updates that add no explanatory power; every new line traceable to card ids) and ${REPO}/references/research-extraction-framework.md section 三 (four-way validation: cross-project recurrence, say–do consistency, executable steps that differ from standard practice, exclusivity) and section 十一 (quality checklist). Those files are in Chinese; their rules apply as written.${m.student_mode ? `
This member has student_mode true: the skill has a Student Mode section and student files references/proof-playbook.md, open-problems.md and reading-path.md (where present). Student Mode rules stay intact.` : ''}

${RULES}`
}

function minePrompt(m) {
  const SK = skillDir(m), CARDS = `${SK}/references/research/cards`
  return `${ctx(m)}

Your job (MINE): aggregate every card into a synthesis note. Do not edit SKILL.md.
0. Gate first. Run python3 ${REPO}/scripts/verify_card_quotes.py ${SK}. If any quote is NOT FOUND, STOP: write nothing, and return blocked=true with the count in blocked_reason and 0 / [] / "" in the other fields (synthesis waits until every quote is exact; the team-read Gate or a manual fix comes first). Otherwise run python3 ${REPO}/scripts/mark_read_from_cards.py ${SK} so that INDEX.md's Read column is current.
1. Load all ${CARDS}/*.digest.json with python. Compute: cards by read level; per "Method N" the number of distinct cards giving evidence / variant / contradiction; all new_pattern_candidates, clustered by meaning (merge synonyms by reading them, not by string match); proof devices and transferable techniques clustered the same way; coauthor frequencies by period; topics by 5-year period.
2. Open the card .md files behind every candidate cluster with ≥2 cards and every contradiction, and check that the cards really support the claim.
3. Decide, applying the four-way validation strictly:
   - candidate cluster in ≥3 distinct full/partial cards and passes all four checks → PROMOTE to a core method (the skill must stay at 3–7 core methods: if it already has 7, promote only by merging into or replacing the weakest method, and justify it);
   - executable and passes at least one more check → heuristic;
   - otherwise it stays in the candidate pool.
   Also decide which existing methods get new "Practice" evidence, which get a variant note, and whether a claim of the skill is contradicted by the full texts (full texts win over web snippets; record what changes). Reject updates that add no explanatory power (list them).
4. Write ${SK}/references/research/07-paper-cards.md, generated with python from the digests: a header (what the cards are; coverage numbers taken from this member's row of python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage; date ${DATE}; a legend of read levels and batch prefixes), then a table Card (id) | Year | Title | Read level | Batch file (relative link cards/<bid>.md) | Methods linked | One-line contribution, sorted by year. If 07 exists, regenerate it in the same format.
5. Write ${SK}/references/research/08-deep-reading-synthesis.md with sections: Coverage; Evidence per existing method (counts, strongest cards with page refs, say–do update); Variants and contradictions; Promotions (each with the four checks spelled out and ≥3 card ids); New heuristics; Candidate pool (not promoted, with counts); Technique inventory (proof devices, design moves, experiment/evaluation protocols, writing moves, each with card ids); Trajectory as seen in the full texts (periods, turns, what stayed constant); Collaboration pattern; Rejected updates; Open gaps (what the works without an open text leave uncertain). If 08 exists from an earlier round, revise it in place and keep earlier decisions unless new cards overturn them (say so).
Every statement in 08 points to card ids (e.g. [S012 p. 9]).
Edit only 07-paper-cards.md and 08-deep-reading-synthesis.md. Return the structured summary.`
}

function editPrompt(m, mine) {
  const SK = skillDir(m)
  return `${ctx(m)}

The synthesis note is ${SK}/references/research/08-deep-reading-synthesis.md and the card index is 07-paper-cards.md (mining summary: ${JSON.stringify(mine)}).
Your job (EDIT): update the skill conservatively so it is deeper and more usable, following paper-reading-card.md section 三.
Word budget: SKILL.md is loaded into a model's context on activation, so distil, do not paste. It must end at about ${BUDGET} words or fewer (wc -w; hard limit ${MAXW}). Write the exhaustive evidence into ${SK}/references/research/09-evidence-ledger.md IN THE SAME PASS (not as a later clean-up): one section per SKILL.md item, each preceded by an explicit anchor line such as <a id="method-1"></a> and then a heading "## Method 1: <name>" (likewise heuristic-N, taste-marks, taste-warnings, anatomy-<short-name>, corrections, card-key). In SKILL.md put a pointer after each item, e.g. "(full evidence: references/research/09-evidence-ledger.md#method-1)". If a ledger already exists, extend it under the same anchors.
0. Save a copy first: mkdir -p ${SCR} && cp -n ${SK}/SKILL.md ${backup(m)} (keep an existing copy: it is the pre-synthesis state).
SKILL.md (use the section names the skill already has, in its language):
- Core research methods: for each method keep **One line**; **Evidence**, reduced to Stated (the single strongest statement; verbatim with card and page if it is a quote), Practice (the 3–5 strongest cards with pages, e.g. "[card S012, pp. 9–11]"), Say–do (one line with the counts, e.g. "✅ stated + practiced; full texts: N cards"), Variants/corrections (at most 4 one-line bullets, each with its ✗/⚠ mark and card ref); the ledger pointer; **Steps**; **Applies to stage**; **Different from standard practice**; **Limitations**. Promote only what 08 promotes, in the same house format. Keep 3–7 core methods and the existing numbering. Never delete a method or its evidence: if the full texts contradict it, mark the contradiction and correct the claim, citing the card (the detail goes to the ledger).
- Research heuristics, research taste (marks of good research / warning signs), research anti-patterns: add items 08 supports, each with ≥2 card ids, one or two lines each with at most 3 card refs (more in the ledger).
- Stage workflows: make steps more concrete with techniques from the technique inventory (cite cards); add at most one new workflow, only if 08 clearly supports it.
- Signature work anatomy: rest the anatomies of works read in full on the full text (page refs); add 1–2 anatomies of important works read in full that are missing; at most ~2 lines per table row.
- Research trajectory, inner tensions, Roundtable Card: update where the full-text trajectory changes the picture; the Roundtable Card stays short.
- Activation statement and Honest Boundary: replace any "no full texts were read" wording with the exact coverage numbers (this member's row of python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage) and the remaining gaps (works without an open text, books whose bodies were not read, ...). Keep a short "Corrections from the full texts" list (one line each) near the Honest Boundary so the corrections stay visible.
- Sources appendix: one line pointing to 07, 08, 09, INDEX.md and the technique catalog, not a list of every paper.
- Frontmatter: set "researched:" to ${DATE}; keep the description under ~300 words and far below 1024 characters; no keyword lists.
- Research integrity rules${m.student_mode ? ' and Student Mode' : ''} stay untouched. No invented quotes: every quotation in SKILL.md, the ledger or a reference file is copied from a card that copied it verbatim.
Also:
- Create or update ${SK}/references/technique-catalog.md: the transferable techniques (proof devices, design moves, experiment/evaluation protocols, writing moves), grouped, each with a one-line "how to use it" and card ids with pages; link it from SKILL.md (How to Use or the sources appendix).${m.student_mode ? `
- Student mode: update references/proof-playbook.md (add or correct templates from the full texts; keep "inference" labels where a proof form is still inferred), references/open-problems.md (open problems the works themselves state in their conclusions, with card ids) and references/reading-path.md (re-rank with what the full texts show; every entry verified).` : ''}
- Update ${SK}/references/research/01-publications.md (coverage from works.json and scholar.md) and 06-trajectory.md (from 08), and add rows to ${SK}/references/sources/RESOURCES.md for the publication list, INDEX.md, 07, 08, 09 and the technique catalog (✅ verified).
Gates (rerun until they pass): python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md → 12/12; wc -w ${SK}/SKILL.md ≤ ${MAXW}; python3 ${REPO}/scripts/check_ledger.py ${SK} (every 09-evidence-ledger.md#… anchor in SKILL.md resolves); python3 ${REPO}/scripts/check_links.py ${SK} → 0 broken links.
Edit only: SKILL.md, 01-publications.md, 06-trajectory.md, 09-evidence-ledger.md, technique-catalog.md, RESOURCES.md${m.student_mode ? ', the three student-mode files' : ''} (and 07/08 only to fix a link or a count).
Return the structured summary (methods_before/after = number of method headings).`
}

function lenses(m) {
  const SK = skillDir(m), REL = `${TEAM_REL}/${m.slug}`
  return [
    { key: 'fidelity', prompt: `FIDELITY skeptic. Assume the edit introduced unsupported claims until shown otherwise.
1. Diff SKILL.md against the pre-synthesis copy ${backup(m)} (and git -C ${REPO} diff -- ${REL} for the other files).
2. For EVERY quotation (text inside quotation marks) added to SKILL.md, 09-evidence-ledger.md, technique-catalog.md${m.student_mode ? ', proof-playbook.md, open-problems.md, reading-path.md' : ''} and 08-deep-reading-synthesis.md: find it in the texts with python (normalise whitespace, hyphenation, ligatures and quote marks; search ${SK}/references/sources/papers/txt/*.txt and abstracts.json). Report every quote not found verbatim.
3. For a sample of at least 25 new evidence claims citing a card id and page: open the card and the text at that page and check the claim. Report unsupported or misattributed claims.
4. Every card id cited in SKILL.md exists in 07-paper-cards.md; every work cited has a DOI/arXiv id/venue matching works.json.
5. python3 ${REPO}/scripts/verify_card_quotes.py ${SK}: report the failing ids (count + up to 30 examples).` },
    { key: 'rules', prompt: `RULES skeptic. Check the edit against the house rules.
1. Diff SKILL.md against ${backup(m)}: was any existing method, evidence line, integrity rule${m.student_mode ? ', student-mode rule' : ''} or honest-boundary gap deleted rather than corrected? Were contradictions marked as such?
2. Every promoted or new method: ≥3 distinct cards, all four checks genuinely met, steps that differ from standard practice. Count core methods (must be 3–7).
3. New heuristics / taste items / anti-patterns: ≥2 card ids each.
4. Frontmatter description: count characters (must be < 1024; target ≈300 words at most) and check there is no keyword stuffing; "researched:" is ${DATE}.
5. Honest Boundary and activation statement: do the coverage numbers match this member's row of python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage? Are the remaining gaps stated?
6. Word budget: wc -w SKILL.md ≤ ${MAXW} (target ${BUDGET}); the ledger exists; every 09-evidence-ledger.md#anchor in SKILL.md resolves (python3 ${REPO}/scripts/check_ledger.py ${SK}); python3 ${REPO}/scripts/check_links.py ${SK} is clean.
6b. Deletion detector: python3 ${REPO}/scripts/check_ledger.py ${SK} --before ${backup(m)} lists every card id, page reference and ≥20-character quote of the pre-synthesis SKILL.md that is now in neither SKILL.md nor the ledger, and protected sections that changed. Two differences are by design: the frontmatter (researched: date, description) and the coverage numbers in the first-activation disclaimer inside Activation Rules; every other item it reports is a finding.
7. Language: new text in SKILL.md is in team.json "language".
8. python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md is 12/12.` },
    { key: 'usefulness', prompt: `USEFULNESS skeptic. You are a PhD student in this team's field (team.json "field") who will use this skill tomorrow.
1. Read ${SK}/SKILL.md end to end and technique-catalog.md. Is the skill now more actionable than before (diff against ${backup(m)})? Where did the edit add bulk without actionable guidance (lists of titles, repeated evidence, vague summaries)? Point to passages to cut, or to move to the ledger.
2. Is the structure intact and consistent (method numbering, links to reference files that exist, workflow checkpoints, a short Roundtable Card)?
3. Test it: pose one realistic research problem in ${m.name}'s area (from the member hint and the skill's own scope) and check whether the skill gives concrete next steps grounded in the new full-text evidence. Report what is missing.
4. Is anything written as ${m.name}'s own view when it should read "the works show / suggest"?` },
  ]
}

function fixPrompt(m, findings, round) {
  const SK = skillDir(m)
  return `${ctx(m)}

${round === 1 ? 'Three read-only reviewers checked the updated skill.' : 'After the first fix round some gates still fail.'} Findings: ${JSON.stringify(findings, null, 1)}

Your job (FIX${round > 1 ? ', round ' + round : ''}): verify each finding yourself (reviewers can be wrong), then apply every finding you confirm: blockers and majors always, minors when cheap. Unverifiable quotes: replace with an exact quote from the text or remove the quotation marks and mark it as a paraphrase with its page. Failing quotes inside cards: fix them in both the .md card and the .digest.json. Bulk without guidance: cut it or move it to 09-evidence-ledger.md under the matching anchor. Do not delete evidence outright and do not touch the pre-synthesis copy ${backup(m)}.
Then run every gate and report each in gates (name, command, passed, detail):
- quality_check: python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md → 12/12
- quotes: python3 ${REPO}/scripts/verify_card_quotes.py ${SK} → all exact
- ledger: python3 ${REPO}/scripts/check_ledger.py ${SK} → every SKILL.md → ledger anchor resolves
- links: python3 ${REPO}/scripts/check_links.py ${SK} → 0 broken
- words: wc -w ${SK}/SKILL.md → ≤ ${MAXW}
If a script does not exist in this checkout, do the equivalent check with python and say so in detail.
Edit only the files the synthesis step owns (SKILL.md, 07, 08, 09, technique-catalog.md, 01, 06, RESOURCES.md${m.student_mode ? ', the student-mode files' : ''}) and, for quote fixes, the cards.
Return how many findings you applied, which you declined (with the reason), the gates and the final word count.`
}

const MINE = {
  type: 'object',
  properties: {
    blocked: { type: 'boolean' },
    blocked_reason: { type: 'string' },
    cards_total: { type: 'number' },
    full_cards: { type: 'number' },
    abstract_cards: { type: 'number' },
    method_evidence: { type: 'array', items: { type: 'object', properties: { method: { type: 'string' }, supporting_cards: { type: 'number' }, variants: { type: 'number' }, contradictions: { type: 'number' } }, required: ['method', 'supporting_cards'] } },
    promote: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, cards: { type: 'array', items: { type: 'string' } }, as: { type: 'string' } }, required: ['name', 'cards', 'as'] } },
    rejected_updates: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['blocked', 'blocked_reason', 'cards_total', 'full_cards', 'abstract_cards', 'method_evidence', 'promote', 'rejected_updates', 'notes'],
}
const EDIT = {
  type: 'object',
  properties: {
    files_changed: { type: 'array', items: { type: 'string' } },
    methods_before: { type: 'number' },
    methods_after: { type: 'number' },
    words_before: { type: 'number' },
    words_after: { type: 'number' },
    ledger_sections: { type: 'number' },
    quality_check: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['files_changed', 'methods_before', 'methods_after', 'words_before', 'words_after', 'ledger_sections', 'quality_check', 'summary'],
}
const FINDINGS = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    findings: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
      file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } },
      required: ['severity', 'file', 'problem', 'fix'] } },
  },
  required: ['lens', 'findings'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    gates: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, command: { type: 'string' }, passed: { type: 'boolean' }, detail: { type: 'string' } }, required: ['name', 'command', 'passed', 'detail'] } },
    words_after: { type: 'number' },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'gates', 'words_after', 'summary'],
}

async function mineStage(m) {
  const mine = await A(minePrompt(m), { label: `mine:${m.slug}`, phase: 'Mine', schema: MINE })
  if (!mine) { log(`${m.slug}: mine agent returned nothing; member stopped`); return { slug: m.slug, stopped: 'mine agent failed' } }
  if (mine.blocked) { log(`${m.slug}: blocked at the quote gate (${mine.blocked_reason}); nothing edited`); return { slug: m.slug, stopped: `blocked: ${mine.blocked_reason}`, mine } }
  log(`${m.slug}: ${mine.cards_total} cards (${mine.full_cards} full, ${mine.abstract_cards} abstract); ${mine.promote.length} promotion(s) proposed`)
  return { slug: m.slug, mine }
}

async function editStage(s, m) {
  if (s.stopped) return s
  const edit = await A(editPrompt(m, s.mine), { label: `edit:${m.slug}`, phase: 'Edit', schema: EDIT })
  if (!edit) { log(`${m.slug}: edit agent returned nothing; member stopped before review`); return { ...s, stopped: 'edit agent failed' } }
  log(`${m.slug}: methods ${edit.methods_before} → ${edit.methods_after}; words ${edit.words_before} → ${edit.words_after} (budget ${BUDGET}); quality ${edit.quality_check}`)
  return { ...s, edit }
}

async function verifyStage(s, m) {
  if (s.stopped) return s
  const ls = lenses(m)
  const reviews = await parallel(ls.map(l => () => A(`${ctx(m)}

The skill has just been updated from the paper cards (edit summary: ${JSON.stringify(s.edit)}). You are a READ-ONLY reviewer: do not edit any file.
${l.prompt}
Report findings with severity (blocker = false/unsupported claim or broken rule; major = misleading or materially weaker; minor = polish) and a concrete fix each.`, { label: `verify:${l.key}:${m.slug}`, phase: 'Verify', schema: FINDINGS })))
  const missing = ls.filter((l, i) => !reviews[i]).map(l => l.key)
  if (missing.length) log(`${m.slug}: reviewer(s) returned nothing: ${missing.join(', ')}; those lenses were not checked`)
  const findings = reviews.filter(Boolean).flatMap(r => r.findings.map(f => ({ ...f, lens: r.lens })))
  log(`${m.slug}: ${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers, ${findings.filter(f => f.severity === 'major').length} majors)`)
  return { ...s, findings, lenses_missing: missing }
}

async function fixStage(s, m) {
  if (s.stopped) return s
  let fix = await A(fixPrompt(m, s.findings, 1), { label: `fix:${m.slug}`, phase: 'Fix', schema: FIX })
  let failing = fix ? fix.gates.filter(g => !g.passed) : [{ name: 'fix agent', command: '-', passed: false, detail: 'fix agent returned nothing' }]
  let rounds = 1
  if (failing.length) {
    log(`${m.slug}: gate(s) still failing after fix: ${failing.map(g => g.name).join(', ')}; one more fix round`)
    const fix2 = await A(fixPrompt(m, failing.map(g => ({ severity: 'blocker', file: 'gate', problem: `${g.name} failed: ${g.detail}`, fix: `make "${g.command}" pass` })), 2), { label: `fix2:${m.slug}`, phase: 'Fix', schema: FIX })
    rounds = 2
    if (fix2) { fix = fix2; failing = fix2.gates.filter(g => !g.passed) }
    if (failing.length) log(`${m.slug}: STILL failing after two fix rounds: ${failing.map(g => `${g.name} (${g.detail})`).join('; ')}; needs a human look`)
  }
  return { ...s, fix, fix_rounds: rounds, gates_failing: failing.map(g => g.name) }
}

const results = await pipeline(MEMBERS, mineStage, editStage, verifyStage, fixStage)
const members = results.map((r, i) => r || { slug: MEMBERS[i].slug, stopped: 'a stage threw; this member was dropped (see the run transcript)' })
const done = members.filter(r => !r.stopped && r.gates_failing && !r.gates_failing.length).map(r => r.slug)
const over = members.filter(r => r.fix && r.fix.words_after > BUDGET).map(r => `${r.slug} (${r.fix.words_after})`)
return {
  stage: 'T3.6 synthesize',
  date: DATE,
  word_budget: BUDGET,
  members: members.map(r => ({
    slug: r.slug,
    stopped: r.stopped || null,
    mine: r.mine || null,
    edit: r.edit || null,
    findings: r.findings ? r.findings.length : null,
    blockers: r.findings ? r.findings.filter(f => f.severity === 'blocker').length : null,
    lenses_missing: r.lenses_missing || [],
    fix: r.fix || null,
    fix_rounds: r.fix_rounds || 0,
    gates_failing: r.gates_failing || null,
  })),
  next: [
    `Commit each finished member (${done.join(', ') || 'none'}): SKILL.md and references/ (never PDFs, txt/ or private/).`,
    over.length ? `Over the ${BUDGET}-word target: ${over.join(', ')}; run team-tighten.js for them.` : 'Every finished SKILL.md is within the word target.',
    'When every member is synthesised: team-integrate.js (team README, DEEP-READING.md, roundtable).',
  ],
}
