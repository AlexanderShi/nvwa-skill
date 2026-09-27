export const meta = {
  name: 'team-integrate',
  description: "T3.8 integrate: refresh a research team's README, DEEP-READING.md and roundtable (fault lines backed by card evidence from both sides) from the members' finished deep reading, then review with two read-only lenses and fix until the gates pass",
  whenToUse: 'After team-synthesize (and team-tighten, if run) for the members, and after every team-increment (research-team playbook, stage T3.8).',
  phases: [
    { title: 'Status', detail: 'team_status.py: exact coverage table and each member stage' },
    { title: 'Integrate', detail: 'docs agent (README + DEEP-READING) and roundtable agent, on disjoint files' },
    { title: 'Verify', detail: 'two read-only skeptics: numbers/links/commands and evidence/attribution' },
    { title: 'Fix', detail: 'apply confirmed findings; rerun gates; one more fix round if a gate still fails' },
  ],
}

/*
 * team-integrate.js · research-team kit, stage T3.8 (team layer after the deep reading).
 * Launch:  Workflow({ scriptPath: '<repo>/scripts/workflows/team-integrate.js', args: { ... } })
 *
 * Args shared by all team workflows:
 *   args.repo     absolute path of the nuwa repo (has scripts/, references/)
 *   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
 *   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
 *   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
 *   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
 *                 dblp, orcid, homepage, chase_hints, student_mode). This step is team-level: it needs all
 *                 members together, so it runs once for the team (no per-member pipeline); pass every member.
 *
 * Args specific to team-integrate:
 *   args.rootReadme  default false: also refresh this team's one row/line in <repo>/README.md (nothing else there)
 *   args.newFaultLines  maximum number of new documented disagreements the roundtable agent may add (default 2)
 *
 * Writes: <team>/README.md, <team>/DEEP-READING.md, <team>/<roundtable>/SKILL.md (+ one row of <repo>/README.md
 *   with rootReadme). Backups: <scratch>/<team-folder>-{README,DEEP-READING,roundtable-SKILL}.before-integrate-<date>.md.
 * Gates: coverage in the docs == python3 scripts/team_status.py <team> --coverage; scripts/check_links.py <team> → 0 broken;
 *   every fault line cites existing card ids on both sides.
 * Next: commit the team docs.
 * Cost baseline (worked example product/dfo-team/, 5 members): ~6 agents and ~1M tokens per run.
 */

const a = (typeof args === 'string' ? JSON.parse(args) : args) || {}
function need(keys) {
  const miss = keys.filter(k => a[k] === undefined || a[k] === null || a[k] === '')
  if (miss.length) throw new Error(`team-integrate: missing args: ${miss.join(', ')} (see the header comment)`)
}
need(['repo', 'team', 'scratch', 'date', 'members'])
if (!Array.isArray(a.members) || !a.members.length) throw new Error('team-integrate: args.members must be a non-empty array of team.json member objects')
if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error('team-integrate: args.date must be "YYYY-MM-DD"')
a.members.forEach((m, i) => { if (!m || !/^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') || !m.name) throw new Error(`team-integrate: members[${i}] needs a kebab-case slug and a name`) })
if (!String(a.repo).startsWith('/') || !String(a.scratch).startsWith('/')) throw new Error('team-integrate: args.repo and args.scratch must be absolute paths')
if (String(a.team).startsWith('/')) throw new Error('team-integrate: args.team must be relative to args.repo, e.g. "product/<team>"')
// args keys this workflow reads; anything else is logged (the kit mixes snake_case and camelCase option names)
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'rootReadme', 'newFaultLines']
const unknownArgs = Object.keys(a).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-integrate.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)

const REPO = String(a.repo).replace(/\/+$/, '')
const TEAM_REL = String(a.team).replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const TEAM_NAME = TEAM_REL.split('/').pop()
const SCR = String(a.scratch).replace(/\/+$/, '')
const DATE = a.date
const ROOT_README = a.rootReadme === true
const NEW_FAULTS = a.newFaultLines === undefined ? 2 : Number(a.newFaultLines)
const MEMBERS = a.members

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A() needs opts.phase and opts.label')
  return agent(prompt, opts)
}
function bk(name) { return `${SCR}/${TEAM_NAME}-${name}.before-integrate-${DATE}.md` }
const memberLine = MEMBERS.map(m => `${m.name} (${m.slug}${m.student_mode ? ', student_mode' : ''})`).join('; ')

const RULES = `House rules (non-negotiable):
- Evidence: every number comes from a script run (team_status.py), every claim about a member's research points to that member's card ids with pages (e.g. [<slug> card S072 p. 5]); quotes stay verbatim; never guess — write "not recorded" or "in progress" instead.
- Attribution: nothing written by a coauthor, a reviewer, an interviewer or a newsletter/column author is attributed to a member; reviews are the reviewer's voice.
- Privacy: never open, read or quote anything under a references/sources/private/ folder; only say that such folders are git-ignored and never read.
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCR}/. Do not git commit, push, stash, reset or checkout (the operator commits after the stage).`

function ctx(status) {
  return `Team: ${TEAM}/. Read ${TEAM}/team.json first ("field", "language", "roundtable" folder, "members"). The team was built with the nuwa kit in ${REPO} (templates in ${REPO}/references/team-templates/, playbook ${REPO}/references/research-team-playbook.md, tools in ${REPO}/scripts/ and ${REPO}/scripts/workflows/). Today is ${DATE}.
Members in this run: ${memberLine}.
Each member folder that finished the deep reading has: references/sources/publications/works.json + scholar.md; references/sources/papers/INDEX.md (full-text status, role, read level; PDFs and txt/ git-ignored); references/research/cards/*.md + *.digest.json (D1–D8 paper cards); 07-paper-cards.md (card index); 08-deep-reading-synthesis.md (patterns, promotions, corrections, open gaps); 09-evidence-ledger.md (evidence moved out of SKILL.md); references/technique-catalog.md; an updated SKILL.md. Student-mode members also have proof-playbook.md, open-problems.md, reading-path.md.
${status ? `Status from python3 ${REPO}/scripts/team_status.py ${TEAM} (run ${DATE}):
Members ready (08 exists): ${status.ready.join(', ') || 'none'}. Not ready: ${status.not_ready.map(r => `${r.slug} (${r.stage})`).join(', ') || 'none'}.
Exact coverage table (python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage):
${status.coverage_md}` : ''}

${RULES}`
}

function statusPrompt() {
  return `${ctx(null)}

Your job (STATUS, read-only): run python3 ${REPO}/scripts/team_status.py ${TEAM} --json and python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage. Return coverage_md = the --coverage output verbatim; for each member of team.json its slug, inferred stage and whether references/research/08-deep-reading-synthesis.md exists; and problems (e.g. a member in args but not in team.json or the reverse, a script error). Do not edit any file.`
}

function docsPrompt(status) {
  return `${ctx(status)}

Your job (DOCS): update these files and no others: ${TEAM}/DEEP-READING.md and ${TEAM}/README.md${ROOT_README ? `, plus the single row/line for ${TEAM_REL} in ${REPO}/README.md` : ''}. First save copies: mkdir -p ${SCR}; cp ${TEAM}/DEEP-READING.md ${bk('DEEP-READING')}; cp ${TEAM}/README.md ${bk('README')} (skip a file that does not exist yet). Read each file fully before editing, and write in the language each file already uses (team.json "language" for new text).
1. ${TEAM}/DEEP-READING.md: the record of the deep reading. Keep the section structure of ${REPO}/references/team-templates/DEEP-READING.md if that template exists (otherwise keep the file's own sections): status and date (${DATE}); the pipeline actually used, from evidence only (works.json "source_note"/"sources", INDEX.md Source-column counts, the card files, the scripts and workflows in ${REPO}/scripts/ and ${REPO}/scripts/workflows/) — write "not recorded" rather than guess; the commands per member (python3 scripts/acquire_fulltexts.py ${TEAM_REL}/<slug>; python3 scripts/plan_reading_batches.py ${TEAM_REL}/<slug> [--round N --exclude …]; python3 scripts/verify_card_quotes.py ${TEAM_REL}/<slug>; python3 scripts/mark_read_from_cards.py ${TEAM_REL}/<slug>; python3 scripts/team_status.py ${TEAM_REL}; the workflows team-read / team-synthesize / team-tighten / team-increment / team-integrate); the coverage table exactly as above; the reading-batch brief as used (at most 15 lines, summarised from ${REPO}/scripts/workflows/team-read.js); what is still missing per member (works without an open text, books whose bodies were not read — the biggest gaps from each 08's "Open gaps"); how to extend (drop a PDF named like INDEX.md's ID into papers/, rerun acquire_fulltexts.py, plan a new round with --round N --exclude, or run team-increment.js); the privacy and integrity notes (private/ never read; PDFs and txt/ git-ignored).
2. ${TEAM}/README.md: Honest Boundary: replace any "without full-text reading" wording with the true coverage (one line per member or a short table, pointing to DEEP-READING.md). Resources tree: show publications/works.json + scholar.md, papers/INDEX.md (+ git-ignored PDFs/txt), research/cards/, 07-paper-cards.md, 08-deep-reading-synthesis.md, 09-evidence-ledger.md, technique-catalog.md (only files that exist). Under Use, mention each member's technique catalog. In the team table, update a member's lens/status only where the member's methods or stage changed. Members not ready are shown "in progress" with their stage, never with invented numbers.${ROOT_README ? `
3. ${REPO}/README.md: only the row/line for ${TEAM_REL}: a short note that the skills were deepened by full-text reading, linking ${TEAM_REL}/DEEP-READING.md. Change nothing else.` : ''}
Then run python3 ${REPO}/scripts/check_links.py ${TEAM} (0 broken) and return files changed and a summary.`
}

function roundtablePrompt(status) {
  return `${ctx(status)}

Your job (ROUNDTABLE): update ${TEAM}/<roundtable>/SKILL.md only (the folder named by team.json "roundtable"). First save a copy to ${bk('roundtable-SKILL')} (mkdir -p ${SCR} first).
1. Read it fully, then read each ready member's SKILL.md (Roundtable Card, core research method headings, Honest Boundary) and 08-deep-reading-synthesis.md (Promotions, Variants and contradictions, Technique inventory).
2. Team table / member descriptions: update only where a member's methods changed (new or renamed core methods).
3. Documented disagreements (fault lines) and shared references: check every disagreement against the members' cards. Keep a disagreement only if the cards support BOTH sides; add page-referenced card ids for each side (e.g. "[<slug> card S072 p. 5]"). Add at most ${NEW_FAULTS} new documented disagreement(s), and only ones the full texts clearly show, each with card evidence from both sides. A disagreement you cannot back with cards is reworded as an open question or removed (say which in the summary).
4. Member agent brief: tell each member agent to consult its references/technique-catalog.md and references/research/08-deep-reading-synthesis.md when proposing designs, experiments or proofs, and to cite card ids; for student_mode members also proof-playbook.md, open-problems.md and reading-path.md.
5. Honest Boundary: replace any "no full-text reading" statement with one line pointing to ../DEEP-READING.md for coverage.
Keep the roundtable protocol, checkpoints and controls unchanged, and keep it concise. Members not ready keep their current text. Then run python3 ${REPO}/scripts/check_links.py ${TEAM} and return files changed and a summary.`
}

function lensPrompts(status, reports) {
  const head = `${ctx(status)}

The team docs and the roundtable were just updated (reports: ${JSON.stringify(reports)}). Pre-edit copies: ${bk('README')}, ${bk('DEEP-READING')}, ${bk('roundtable-SKILL')}. You are a READ-ONLY reviewer: do not edit files (scratch work under ${SCR}/ only). Use git -C ${REPO} diff -- ${TEAM_REL}${ROOT_README ? ' README.md' : ''}.`
  return [
    { key: 'numbers-links', prompt: `${head}
LENS: numbers, links, commands.
1. Every coverage number in the changed files matches python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage (rerun it; compare cell by cell).
2. python3 ${REPO}/scripts/check_links.py ${TEAM}${ROOT_README ? ` ${REPO}/README.md` : ''} → 0 broken; every file path mentioned in the changed files exists.
3. Every command shown runs: run each script with --help (never modify product files).
4. Members not ready are not given numbers they do not have.${ROOT_README ? `
5. ${REPO}/README.md changed only in the one row/line for ${TEAM_REL}.` : ''}` },
    { key: 'evidence', prompt: `${head}
LENS: evidence and attribution.
1. Every roundtable disagreement cites card ids that exist in the members' 07-paper-cards.md, on BOTH sides; open those cards and check they support what the roundtable says.
2. Nothing in the changed files is attributed to a member that is really a coauthor's, a reviewer's, an interviewer's or a column author's.
3. The member agent brief points each member to its technique-catalog.md and 08 (and student-mode files where relevant); the roundtable protocol, checkpoints and controls are unchanged against the pre-edit copy.
4. DEEP-READING.md's pipeline description claims nothing that the evidence (works.json sources, INDEX.md, cards, scripts) does not show.` },
  ]
}

function fixPrompt(status, findings, round) {
  return `${ctx(status)}

${round === 1 ? 'Two read-only reviewers checked the integration edits.' : 'After the first fix round some gates still fail.'} Findings: ${JSON.stringify(findings)}
Your job (FIX${round > 1 ? ', round ' + round : ''}): verify each finding yourself, apply those you confirm (blockers and majors always). Do not modify the pre-edit copies.
Then run every gate and report each in gates (name, command, passed, detail):
- coverage: the coverage numbers in ${TEAM}/DEEP-READING.md and README.md equal python3 ${REPO}/scripts/team_status.py ${TEAM} --coverage
- links: python3 ${REPO}/scripts/check_links.py ${TEAM}${ROOT_README ? ` ${REPO}/README.md` : ''} → 0 broken
- fault-lines: every documented disagreement in the roundtable cites existing card ids on both sides (python: extract the ids, look them up in the members' 07-paper-cards.md)
Edit only ${TEAM}/README.md, ${TEAM}/DEEP-READING.md, the roundtable SKILL.md${ROOT_README ? ` and the one ${TEAM_REL} row of ${REPO}/README.md` : ''}. Report what you changed and declined.`
}

const STATUS = {
  type: 'object',
  properties: {
    coverage_md: { type: 'string' },
    members: { type: 'array', items: { type: 'object', properties: { slug: { type: 'string' }, stage: { type: 'string' }, has_08: { type: 'boolean' } }, required: ['slug', 'stage', 'has_08'] } },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['coverage_md', 'members', 'problems'],
}
const OUT = {
  type: 'object',
  properties: { files_changed: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } },
  required: ['files_changed', 'summary', 'problems'],
}
const FINDINGS = {
  type: 'object',
  properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, file: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'problem', 'fix'] } } },
  required: ['findings'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    gates: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, command: { type: 'string' }, passed: { type: 'boolean' }, detail: { type: 'string' } }, required: ['name', 'command', 'passed', 'detail'] } },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'gates', 'summary'],
}

phase('Status')
const st = await A(statusPrompt(), { label: 'status:team', phase: 'Status', schema: STATUS, effort: 'low' })
if (!st) throw new Error('team-integrate: the status agent returned nothing; run python3 scripts/team_status.py <team> --coverage by hand and retry')
const argSlugs = new Set(MEMBERS.map(m => m.slug))
const statusRows = st.members.filter(r => argSlugs.has(r.slug))
const status = {
  coverage_md: st.coverage_md,
  ready: statusRows.filter(r => r.has_08).map(r => r.slug),
  not_ready: statusRows.filter(r => !r.has_08).map(r => ({ slug: r.slug, stage: r.stage })),
}
const unseen = MEMBERS.filter(m => !st.members.some(r => r.slug === m.slug)).map(m => m.slug)
if (unseen.length) log(`members in args but not reported by team_status.py: ${unseen.join(', ')}`)
if (st.problems.length) log(`status problems: ${st.problems.join('; ')}`)
if (status.not_ready.length) log(`not ready (no 08 yet), shown as in progress: ${status.not_ready.map(r => `${r.slug} (${r.stage})`).join(', ')}`)
if (!status.ready.length) {
  log('no member has finished the synthesis; nothing to integrate')
  return { stage: 'T3.8 integrate', date: DATE, status, skipped: 'no member ready', next: ['Run team-synthesize.js first.'] }
}

phase('Integrate')
const [docs, table] = await parallel([
  () => A(docsPrompt(status), { label: 'integrate:docs', phase: 'Integrate', schema: OUT }),
  () => A(roundtablePrompt(status), { label: 'integrate:roundtable', phase: 'Integrate', schema: OUT }),
])
if (!docs) log('docs agent returned nothing; README/DEEP-READING may be unchanged (the reviewers will see)')
if (!table) log('roundtable agent returned nothing; the roundtable may be unchanged (the reviewers will see)')

phase('Verify')
const ls = lensPrompts(status, { docs, roundtable: table })
const reviews = await parallel(ls.map(l => () => A(`${l.prompt}
Report findings with severity (blocker = wrong number, broken link, unsupported or misattributed claim; major = misleading or materially incomplete; minor = polish), the file, and a concrete fix each.`, { label: `verify:${l.key}`, phase: 'Verify', schema: FINDINGS })))
const missing = ls.filter((l, i) => !reviews[i]).map(l => l.key)
if (missing.length) log(`reviewer(s) returned nothing: ${missing.join(', ')}; those lenses were not checked`)
const findings = reviews.flatMap((r, i) => (r ? r.findings.map(f => ({ ...f, lens: ls[i].key })) : []))
log(`${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers, ${findings.filter(f => f.severity === 'major').length} majors)`)

phase('Fix')
let fix = await A(fixPrompt(status, findings, 1), { label: 'fix:integration', phase: 'Fix', schema: FIX })
let failing = fix ? fix.gates.filter(g => !g.passed) : [{ name: 'fix agent', command: '-', passed: false, detail: 'fix agent returned nothing' }]
let rounds = 1
if (failing.length) {
  log(`gate(s) still failing: ${failing.map(g => g.name).join(', ')}; one more fix round`)
  const fix2 = await A(fixPrompt(status, failing.map(g => ({ severity: 'blocker', file: 'gate', problem: `${g.name} failed: ${g.detail}`, fix: `make "${g.command}" pass` })), 2), { label: 'fix2:integration', phase: 'Fix', schema: FIX })
  rounds = 2
  if (fix2) { fix = fix2; failing = fix2.gates.filter(g => !g.passed) }
  if (failing.length) log(`STILL failing after two fix rounds: ${failing.map(g => `${g.name} (${g.detail})`).join('; ')}; needs a human look`)
}

return {
  stage: 'T3.8 integrate',
  date: DATE,
  status,
  docs,
  roundtable: table,
  findings: findings.length,
  blockers: findings.filter(f => f.severity === 'blocker').length,
  lenses_missing: missing,
  fix,
  fix_rounds: rounds,
  gates_failing: failing.map(g => g.name),
  next: [
    `Commit the team docs (${TEAM_REL}/README.md, DEEP-READING.md, the roundtable SKILL.md${ROOT_README ? ', README.md' : ''}).`,
    status.not_ready.length ? `Rerun team-integrate.js after ${status.not_ready.map(r => r.slug).join(', ')} finish(es) the synthesis.` : 'All members are integrated.',
  ],
}
