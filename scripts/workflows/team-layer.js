export const meta = {
  name: 'team-layer',
  description: 'T2: team layer for a nuwa research team: Roundtable Cards checked, roundtable SKILL.md and team README filled from the templates and the members\' cards (fault lines need evidence from both sides), per-member RESOURCES.md reconciled, then two read-only verifiers and a fixer',
  whenToUse: 'After team-base-skills.js (T1) has built every member skill (quality_check 12/12). Pass ALL members: the roundtable needs every card.',
  phases: [
    { title: 'Cards', detail: 'per member: check or write the Roundtable Card in SKILL.md; digest for the roundtable author' },
    { title: 'Resources', detail: 'per member: reconcile references/sources/RESOURCES.md with SKILL.md; private/README.md present' },
    { title: 'Roundtable', detail: 'roundtable SKILL.md from references/team-templates/roundtable-SKILL.md and the cards' },
    { title: 'README', detail: 'team README.md from references/team-templates/team-README.md' },
    { title: 'Verify', detail: 'two read-only verifiers: structure/consistency and evidence' },
    { title: 'Fix', detail: 'apply confirmed findings; links, placeholders and 12/12 gates again' },
  ],
}

// ---------------------------------------------------------------------------------------------
// Args (shared by all team workflows in scripts/workflows/):
//   args.repo     absolute path of the nuwa repo (has scripts/, references/)
//   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
//   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
//   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
//   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
//                 dblp, orcid, homepage, chase_hints, student_mode). Per-member steps run through pipeline();
//                 the roundtable waits for every member's card (a genuine barrier). Pass ALL members.
// Workflow-specific keys:
//   args.roundtable     optional roundtable slug (default: team.json "roundtable", read by the agents)
//   args.deep_tier      default true: deep reading (T3) is planned, so the TODO items the templates reserve for
//                       team-integrate.js (T3.8) stay in place; false: delete those deep-tier-only parts
//   args.example_team   optional team folder (relative to repo) of a finished team to imitate for shape only,
//                       e.g. "product/dfo-team"
// Outputs: <team>/README.md, <team>/<roundtable>/SKILL.md, each member's Roundtable Card (only if missing or
//   incomplete) and references/sources/RESOURCES.md, private/README.md where missing.
// Gates run by the agents: scripts/check_links.py (0 broken), no "{{" left, TODOs only where a template reserves
//   them for a later step, scripts/quality_check.py 12/12 per member, scripts/team_status.py.
// Next: commit; then the deep tier (team-harvest.js ...) or deliver the base tier.
// Launch: Workflow({scriptPath: "<repo>/scripts/workflows/team-layer.js", args: {...}}).
// Cost: 2 agents per member + 5 (roundtable, README, 2 verifiers, fixer).
// ---------------------------------------------------------------------------------------------

const ARGS = typeof args === 'string' ? JSON.parse(args) : args
function need(ok, msg) { if (!ok) throw new Error(`team-layer args: ${msg}`) }
need(ARGS && typeof ARGS === 'object', 'pass args as a JSON object')
need(typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'), 'args.repo must be an absolute path')
need(typeof ARGS.team === 'string' && ARGS.team.length > 0 && !ARGS.team.startsWith('/'), 'args.team must be relative to args.repo, e.g. "product/<team>"')
need(typeof ARGS.scratch === 'string' && ARGS.scratch.startsWith('/'), 'args.scratch must be an absolute path')
need(/^\d{4}-\d{2}-\d{2}$/.test(ARGS.date || ''), 'args.date must be "YYYY-MM-DD"')
need(Array.isArray(ARGS.members) && ARGS.members.length > 0, 'args.members must be a non-empty array copied from team.json')
ARGS.members.forEach((m, i) => need(m && /^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') && m.name, `args.members[${i}] needs a kebab-case slug and a name`))
need(ARGS.roundtable === undefined || /^[a-z0-9][a-z0-9-]*$/.test(ARGS.roundtable), 'args.roundtable must be a kebab-case slug')

const REPO = ARGS.repo.replace(/\/+$/, '')
const TEAM_REL = ARGS.team.replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCRATCH = ARGS.scratch.replace(/\/+$/, '')
const DATE = ARGS.date
const MEMBERS = ARGS.members
const DEEP = ARGS.deep_tier !== false
const RT_DIR = ARGS.roundtable ? `${TEAM}/${ARGS.roundtable}` : `${TEAM}/<roundtable slug from team.json>`
const TPL = `${REPO}/references/team-templates`
const EXAMPLE = typeof ARGS.example_team === 'string' && ARGS.example_team.trim()
  ? `Worked example of a finished team (read for shape and level of detail only; never copy its field, researchers or content): ${REPO}/${ARGS.example_team.replace(/^\.\//, '').replace(/\/+$/, '')}/.`
  : ''
const LATER = 'team-harvest.js, team-read.js, team-synthesize.js, team-tighten.js, team-increment.js, team-integrate.js, T3, T3.1, T3.8, T4'

const HOUSE = `House rules for every agent in this workflow (nuwa research-team kit):
- Read ${TEAM}/team.json first: "team" (slug), "title", "field", "language" (of every member skill; the team layer follows it too), "roundtable" (the roundtable skill's folder slug${ARGS.roundtable ? `, here ${ARGS.roundtable}` : ''}) and the member entries (name, surname — used for lens labels such as [Surname lens] and @Surname —, living, hint, student_mode).
- Templates live in ${TPL}/ (team-README.md, roundtable-SKILL.md, member-RESOURCES.md, private-README.md). scripts/new_team.py fills their {{PLACEHOLDERS}} and leaves [TODO: …] items, each naming the step that resolves it. This workflow (team-layer.js, T2) resolves the items marked team-layer.js / T2 (and T1 items that are still open); items reserved for later steps (${LATER}) stay as they are${DEEP ? '' : ' unless this prompt says to delete deep-tier-only parts'}.
- Evidence: every paper, tool or link you name carries a DOI, arXiv id or URL that you checked with a tool in this run; never cite from memory. What you say about a member must come from that member's own SKILL.md or research notes (references/research/), never from general knowledge of the researcher. Quotes verbatim with their source. If you did not check something, say so; never guess.
- Sources: public and legitimate only; never shadow libraries or paywall circumvention.
- Privacy: never open, read, quote or copy anything under a references/sources/private/ folder except its README.md. Never send the user's email address or any other personal identifier to an external service.
- Scope: edit only the files this step names as its outputs (scratch files and backups go under ${SCRATCH}/team-layer/). Do not touch the repo's root SKILL.md, references/ or scripts/, and do not git commit or push: the session that launched this workflow commits after the stage.`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A(): opts.phase and opts.label are required')
  return agent(`${HOUSE}\n\n${prompt}`, opts)
}
const P = m => {
  const MD = `${TEAM}/${m.slug}`
  return { MD, SKILL: `${MD}/SKILL.md`, SRC: `${MD}/references/sources`, RES: `${MD}/references/research` }
}

// ---------- schemas ----------
const FINDINGS = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'problem', 'fix'] } },
  },
  required: ['lens', 'findings'],
}
const CARD = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    skill_exists: { type: 'boolean' },
    had_complete_card: { type: 'boolean' },
    edited: { type: 'boolean' },
    lens: { type: 'string' },
    known_for: { type: 'string' },
    leads_when: { type: 'string' },
    first_questions: { type: 'array', items: { type: 'string' } },
    default_recommendation: { type: 'string' },
    pushes_back_on: { type: 'string' },
    likely_disagreements: { type: 'array', items: { type: 'object', properties: { with: { type: 'string' }, point: { type: 'string' }, papers: { type: 'string' } }, required: ['with', 'point'] } },
    blind_spots: { type: 'string' },
    methods: { type: 'array', items: { type: 'string' } },
    workflows: { type: 'array', items: { type: 'string' } },
    taste: { type: 'array', items: { type: 'string' } },
    key_papers: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, id: { type: 'string' }, position: { type: 'string' }, where: { type: 'string' } }, required: ['title', 'id', 'position', 'where'] } },
    deep_tier_done: { type: 'boolean' },
    student_mode: { type: 'boolean' },
    quality_check: { type: 'string' },
  },
  required: ['slug', 'skill_exists', 'had_complete_card', 'edited', 'lens', 'leads_when', 'first_questions', 'likely_disagreements', 'blind_spots', 'methods', 'key_papers', 'deep_tier_done', 'student_mode', 'quality_check'],
}
const RES_OUT = {
  type: 'object',
  properties: {
    rows: { type: 'number' },
    added: { type: 'number' },
    verified: { type: 'number' },
    leads: { type: 'number' },
    rechecked: { type: 'number' },
    failed_recheck: { type: 'number' },
    unverifiable_cited: { type: 'array', items: { type: 'string' } },
    private_readme: { type: 'string', enum: ['existed', 'created', 'missing'] },
    summary: { type: 'string' },
  },
  required: ['rows', 'added', 'verified', 'leads', 'unverifiable_cited', 'private_readme', 'summary'],
}
const RT_OUT = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    words: { type: 'number' },
    description_chars: { type: 'number' },
    seated: { type: 'array', items: { type: 'string' } },
    fault_lines: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, sides: { type: 'string' }, kind: { type: 'string', enum: ['exchange in print', 'contrast of published methods'] }, evidence: { type: 'string' } }, required: ['title', 'sides', 'kind', 'evidence'] } },
    dropped_contrasts: { type: 'array', items: { type: 'string' } },
    seating_rows: { type: 'number' },
    shared_references: { type: 'number' },
    todos_left: { type: 'array', items: { type: 'string' } },
    links: { type: 'string' },
    card_problems: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['file', 'words', 'description_chars', 'seated', 'fault_lines', 'dropped_contrasts', 'seating_rows', 'todos_left', 'links', 'card_problems', 'summary'],
}
const README_OUT = {
  type: 'object',
  properties: { file: { type: 'string' }, words: { type: 'number' }, todos_left: { type: 'array', items: { type: 'string' } }, links: { type: 'string' }, team_status: { type: 'string' }, summary: { type: 'string' } },
  required: ['file', 'todos_left', 'links', 'team_status', 'summary'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    files_changed: { type: 'array', items: { type: 'string' } },
    check_links: { type: 'string' },
    placeholders_left: { type: 'number' },
    quality_checks: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'files_changed', 'check_links', 'placeholders_left', 'quality_checks', 'summary'],
}

// ---------- prompts ----------
function cardPrompt(m) {
  const { MD, SKILL, RES } = P(m)
  return `Task (T2 team layer, step 1: Roundtable Card) for ${m.name} (${MD}/).
Read ${SKILL}. If it does not exist, edit nothing and return skill_exists = false (fill the other fields with empty values).
The card is the "## Roundtable Card" section with seven bullets: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member), **Blind spots**. The roundtable moderator reads only this section, so it must be complete and short (under about 350 words).
- Complete card: edit nothing; return its content.
- Missing or incomplete card: write it from the skill's own sections (Research Taste, Core Research Methods, Stage Workflows, Research Anti-patterns, Honest Boundary, and the research notes in ${RES}/ they cite). Nothing new: every bullet must trace to the same skill. Likely disagreements: one per OTHER member listed in team.json, inferred from the methods on both sides, labelled "inferred", naming the paper(s) with identifiers each side rests on where this member's files give them, and "no dispute documented" unless one is. Put the card just before the Honest Boundary. If Activation Rules lack it, add one line: "When convened by <roundtable slug>, answer from the Roundtable Card first and keep it short." Then run python3 ${REPO}/scripts/quality_check.py ${SKILL}: it must still report 12/12 (report the result line either way).
Also return, for the roundtable author: the core method names (the ### headings under the core-methods section), the stage-workflow names, the top 3 taste criteria, what the skill says the member is known for (signature works, software, books; one line, from the skill), the papers behind the member's most distinctive positions (title, DOI/arXiv id, the position it supports, and where in the skill or notes it is used), whether deep-reading files exist (references/technique-catalog.md or references/research/07-paper-cards.md), and whether the skill has a Student Mode.
Files you may edit: ${SKILL} — the Roundtable Card and that one Activation Rules line only.`
}

function resourcesPrompt(m) {
  const { MD, SKILL, SRC, RES } = P(m)
  return `Task (T2 team layer: resource tracker) for ${m.name}. File: ${SRC}/RESOURCES.md.
team-base-skills.js (T1) filled it from the research notes; SKILL.md may cite sources the tracker lacks.
1. If the file is missing, create it from ${TPL}/member-RESOURCES.md (replace {{MEMBER_NAME}}, {{MEMBER_SLUG}}, {{SCHOLAR_URL}}). If T1 items are still TODO, fill them as the template says: one row per source in ${RES}/01-06, each verified.
2. Every paper, book, software, talk or page cited in ${SKILL} (and in references/proof-playbook.md, open-problems.md, reading-path.md, technique-catalog.md if they exist) has a row. Add the missing ones, verified with a tool in this run: DOI -> curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> gives 30x and the Crossref title matches; arXiv -> the abs page title matches; other -> the page exists and says what the row says. Add "SKILL" (with the section) to "Used in" where SKILL.md cites the source.
3. Re-check 10 ✅ rows chosen across the table (all if fewer); a failing row becomes ⚠️ with the reason in Notes; if more than 2 fail, re-check every ✅ row.
4. A source SKILL.md cites that you cannot verify: mark it ⚠️ and list it in unverifiable_cited (the fixer decides whether the skill may keep citing it).
5. Leave TODO items reserved for later steps (the Google Scholar row for team-harvest.js; the deep-tier rows for T3/T4) exactly as they are. No "{{" may remain.
6. Make sure ${SRC}/private/README.md exists; if missing, create it from ${TPL}/private-README.md (replace {{MEMBER_NAME}} and {{MEMBER_SLUG}}). Never open anything else in private/.
Edit only ${SRC}/RESOURCES.md and (create only) ${SRC}/private/README.md. Return the counts.`
}

function roundtablePrompt(cards, missing) {
  return `Task (T2 team layer: the roundtable skill). Output: ${RT_DIR}/SKILL.md.
Start from that file if scripts/new_team.py created it (${TPL}/roundtable-SKILL.md with the {{…}} placeholders filled and [TODO: …] items open). If it does not exist, copy the template and replace every placeholder yourself — {{ROUNDTABLE_SLUG}}, {{TEAM_TITLE}}, {{FIELD}}, {{MEMBER_LIST}} (comma-separated member names), {{DATE}} = ${DATE} — so that no "{{" remains. ${EXAMPLE}
Seated members (each has a SKILL.md with a Roundtable Card); digests from their cards: ${JSON.stringify(cards)}
${missing.length ? `Members listed but without a skill yet (leave them out of every table; say so in the Honest Boundary): ${missing.join(', ')}.\n` : ''}Read each seated member's Roundtable Card, Core Research Methods and Research Taste yourself (${TEAM}/<slug>/SKILL.md) before writing; the digests are a map, not the evidence.

Keep every part of the template: it is what makes the roundtable work.
 (a) "How the Roundtable Runs": each seated member runs as its own agent (Agent/Task tool, all seated members launched in one message, agents reused across rounds when the runtime can continue them); the model reading the skill is the moderator and never argues a member's position; the user chairs and the discussion pauses at every 🔵 checkpoint; the single-model fallback is announced; the cost line.
 (b) Activation Rules, Research Integrity Rules (with the private/ rule), Your Controls, Loading the Team (absolute paths; the moderator reads only the Roundtable Cards; a missing member is named, never improvised).
 (c) The Member Agent Brief block (its single-brace fields stay for the moderator to fill at run time).
 (d) Protocol Steps 0-5 with the four 🔵 checkpoints; Checkpoint 4 is never skipped, even in autopilot; Step 5 verifies every name, paper and link and offers to save the transcript only if the user says yes.
 (e) Output Template, Outside the Team, Shared References, Papers behind the documented disagreements, Honest Boundary, the attribution footer.

Resolve the TODO items marked team-layer.js (T2):
1. Frontmatter description: the kind of problem the team takes (from the members' "Leads when"), the parts a plan in this field must name (from their "Default recommendation"), one "Not for …" sentence; the whole description under 1024 characters (count them).
2. Team table: one row per seated member — the slug in backticks, full name, the lens in one line condensed from its card.
3. Problem Card: keep the six generic fields; add 3-6 field-specific fields merged from the members' "First questions asked" (deduplicated), each with "why it matters" naming the lens or seating choice it feeds.
4. Seating table: 8-14 rows "problem signal -> 2 leads -> 1 challenger" built from the members' "Leads when" and "Blind spots"; every seated member leads at least one row; a row where no other lens has evidence gets "— (outside the other lenses' evidence)".
5. Documented fault lines (3-6) — the heart of this step:
   - Candidates: the members' "Likely disagreements", plus contrasts you see between their core methods and taste.
   - Keep a fault line only with evidence from BOTH sides: for each side, a passage in that member's SKILL.md or research notes (references/research/01-06; paper cards and 07-09 if they exist) that rests on a verifiable paper (DOI or arXiv id; page or section when a full text was read). Open those files and check the passage says it. Cite as [<member-slug> <file> §<section>; <DOI or arXiv id>] — or, once paper cards exist, [<member-slug> card <id> p. N].
   - Say whether it is an exchange in print between members (only when you found papers on both sides answering each other) or a contrast of published methods (the usual case). Never invent a debate or a quote.
   - Name what is still contested and the observation or experiment that would settle it.
   - While the members have no paper cards, end each fault line with "(card evidence pending)"; team-integrate.js (T3.8) rewrites them from the cards later.
   - One-sided or unsupported contrasts are not fault lines: drop them and list them in dropped_contrasts with the missing side.
6. Draft-plan items: the settings a plan in this field must always state, 2-3 switch signals, and the field's standard comparison protocol (verified, with its reference in Shared References).
7. Outside the Team: 2-4 bullets "problem signal -> the neighbouring tradition, method or tool that fits better", from team.json "field" and the members' blind spots; say whether any member partly covers it; every tool or paper named verified.
8. Shared References (verified <month year>): 3-8 field-wide references (the standard for comparing methods, a taxonomy of problem types, a survey, key open-source software), each a full reference with DOI or URL checked in this run, ending with one line on why it is here.
9. Papers behind the documented disagreements: while there are no paper cards, write "Pending the deep reading (T3)."; otherwise follow the template.
10. Honest Boundary: the variants for this stage — members rest on web research only (notes 01-06) unless deep-reading files exist; fault lines drawn from the members' cards and notes and not yet checked against full texts; historical-lens bullets for members with "living": false; the traditions outside the team (matching Outside the Team); research date ${DATE}.
Do not edit any other file (not the members' SKILL.md: report a wrong or thin card in card_problems instead).
Keep it concise (about 4,000 words at most).
Gates: python3 ${REPO}/scripts/check_links.py ${RT_DIR} (0 broken); grep -n "{{" (none); grep -n "TODO" (only items reserved for ${LATER}). Return the structured summary.`
}

function readmePrompt(cards, rt) {
  return `Task (T2 team layer: the team README). Output: ${TEAM}/README.md.
Start from the README scripts/new_team.py created (${TPL}/team-README.md with placeholders filled and [TODO: …] items open) or, if there is none, from the template itself: replace every placeholder — {{TEAM_TITLE}}, {{TEAM_SLUG}} (team.json "team"), {{FIELD}}, {{MEMBER_LIST}}, {{ROUNDTABLE_SLUG}}, {{MEMBER_TABLE}} (one row per member: | [Name](<slug>/SKILL.md) | lens · known for | status |) — so that no "{{" remains. ${EXAMPLE}
The roundtable skill was just written: ${rt ? `${rt.file} (seated: ${rt.seated.join(', ')})` : `${RT_DIR}/SKILL.md (its author returned no report; read the file)`}. Member digests: ${JSON.stringify(cards.map(c => ({ slug: c.slug, lens: c.lens, known_for: c.known_for, student_mode: c.student_mode, deep_tier_done: c.deep_tier_done })))}
Resolve the TODO items marked team-layer.js (T2):
- The scope sentence (which tradition of the field this selection follows; which neighbouring traditions are not represented), consistent with the roundtable's "Outside the Team".
- The team table: each member's one-line lens and what it is known for, taken from that member's SKILL.md (not from memory); the status cell from python3 ${REPO}/scripts/team_status.py ${TEAM}; mark student-mode members; then delete the instruction line.
- Use: a realistic two-line problem from the field, with the budget, constraints and failure modes a member would ask about; the single-lens examples with real surnames and typical artefacts of the field. The checkpoint and control tables must match the roundtable skill's (read it).
- Install: the snippets must use the team's real path, ${TEAM_REL} (fix the template's product/<slug> path if the team lives elsewhere).
- Honest Boundary for the base tier: "The research was done from web search results in <month year>, without full-text reading; each skill's Honest Boundary lists its gaps and RESOURCES.md marks unverified leads ⚠️." (unless team_status.py shows deep-reading output), plus a historical-lens bullet for each member with "living": false (with the year of death from its skill).
${DEEP
    ? '- Deep tier planned: leave the TODO items reserved for team-integrate.js (T3.8) — the technique-catalogs paragraph and the coverage table — in place; they are the open-work list for the deep tier.'
    : '- No deep reading is planned (args.deep_tier is false): delete the technique-catalogs paragraph, the coverage table and their TODO lines, and say in the Resources section that the deep-reading files are absent.'}
Keep the Resources tree and its explanation.
Gates: python3 ${REPO}/scripts/check_links.py ${TEAM}/README.md (0 broken); grep -n "{{" (none); grep -n "TODO" (only items reserved for ${LATER}).
Edit only ${TEAM}/README.md. Return the structured summary.`
}

const LENSES = [
  {
    key: 'structure',
    prompt: () => `READ-ONLY verifier: structure and consistency of the team layer in ${TEAM}. Edit nothing.
1. python3 ${REPO}/scripts/check_links.py ${TEAM}: report every broken link.
2. grep -rn "{{" ${TEAM} --include=*.md: every hit is a finding. grep -n "TODO" in README.md, the roundtable SKILL.md and each member's references/sources/RESOURCES.md: every TODO left must be one a template reserves for a later step (${LATER}); any other TODO is a finding. DEEP-READING.md is not part of this step.
3. Every member in team.json appears consistently: the README team table (linking to its folder), the roundtable Team table, the disclaimer's member list, the seating table (leads at least one row); lens labels and @-controls use real surnames. Each member SKILL.md has a complete "## Roundtable Card" (7 bullets) and the Activation Rules line about the roundtable; python3 ${REPO}/scripts/quality_check.py <member>/SKILL.md still reports 12/12.
4. The roundtable keeps: members run as separate agents with the user in the loop ("How the Roundtable Runs"); Activation Rules; Research Integrity Rules incl. the private/ rule; Your Controls; Loading the Team; the Member Agent Brief block; Protocol Steps 0-5 with four checkpoints (Checkpoint 4 never skipped, even in autopilot); Output Template; Outside the Team; Shared References; Honest Boundary; the footer. The README's checkpoint and control tables match the roundtable's.
5. Roundtable frontmatter: name equals team.json "roundtable"; type: roundtable; description under 1024 characters (count them), triggers present, no keyword stuffing.
6. Seating rows agree with the members' "Leads when"; the Problem Card's field-specific fields cover each member's "First questions asked".
7. python3 ${REPO}/scripts/team_status.py ${TEAM} runs; the README status column and Honest Boundary agree with it. Install snippets use the team's real path (${TEAM_REL}).
8. Nothing leaked from another team (for example a worked-example team's field, members or references).
Report findings with severity (blocker = broken protocol, wrong member, false claim; major = missing required part, broken link, inconsistency; minor = polish), file, location, problem and a concrete fix.`,
  },
  {
    key: 'evidence',
    prompt: () => `READ-ONLY verifier: evidence behind the team layer in ${TEAM}. Edit nothing. Assume a claim is unsupported until you have opened its source.
1. For every documented fault line in the roundtable SKILL.md: open the cited evidence on BOTH sides (the member SKILL.md passages, research notes, paper cards if any) and confirm each side's position is what the fault line says; both sides must be present; identifiers must resolve (curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> gives 30x and the Crossref title matches; arXiv abs page title matches). A position attributed to a member that its own skill does not support is a blocker; a fault line with evidence on one side only is major; "exchange in print" needs papers on both sides that answer each other.
2. The Team-table lenses, the README "known for" lines and the seating rationale: each matches the member's own SKILL.md (no facts from memory).
3. Shared References and Outside the Team: every paper or tool resolves and says what the line claims.
4. RESOURCES.md: every paper cited in each member's SKILL.md has a row; spot-check 5 ✅ rows per member with tools.
5. Nothing quotes or paraphrases material from any references/sources/private/ folder (do not open private files other than README.md).
Report findings with severity (blocker/major/minor), file, location, problem and a concrete fix.`,
  },
]

function fixPrompt(findings) {
  return `Task (T2 team layer: fix). Two read-only verifiers checked ${TEAM}. Findings: ${JSON.stringify(findings)}
Verify each finding yourself (verifiers can be wrong), then apply those you confirm: blockers and majors always, minors when cheap.
- A fault line that fails the both-sides test: find the missing evidence in the members' files if it is there; otherwise drop the fault line (or move it to a "contrasts to check" note) and renumber references to it.
- A wrong or incomplete member card: fix only that member's "## Roundtable Card" in its SKILL.md, then rerun python3 ${REPO}/scripts/quality_check.py on it (12/12).
- An unverifiable citation: replace it with a verified one or remove it.
Files you may edit: ${TEAM}/README.md, the roundtable SKILL.md, members' references/sources/RESOURCES.md, members' Roundtable Card sections. Back up each file to ${SCRATCH}/team-layer/ before its first edit.
Then rerun the gates and report them: python3 ${REPO}/scripts/check_links.py ${TEAM} (0 broken); grep -rn "{{" ${TEAM} --include=*.md (count); quality_check.py on every member SKILL.md.
Return applied and declined findings (with reasons) and the gate results.`
}

// ---------- run ----------
phase('Cards')
if (!DEEP) log('args.deep_tier is false: the README drops its deep-tier-only parts (technique catalogs, coverage table)')

const [resources, team] = await parallel([
  // per-member resource trackers: independent of the cards and the roundtable (disjoint files)
  () => pipeline(MEMBERS, m => A(resourcesPrompt(m), { label: `resources:${m.slug}`, phase: 'Resources', schema: RES_OUT })),
  async () => {
    // barrier by necessity: the roundtable needs every member's card
    const cards = await pipeline(MEMBERS, m => A(cardPrompt(m), { label: `card:${m.slug}`, phase: 'Cards', schema: CARD }))
    const got = cards.map((c, i) => c ? { ...c, slug: MEMBERS[i].slug } : null)
    const failed = MEMBERS.filter((m, i) => !got[i]).map(m => m.slug)
    const noSkill = got.filter(c => c && !c.skill_exists).map(c => c.slug)
    if (failed.length) log(`card agent returned nothing for: ${failed.join(', ')} — they are left out of the roundtable`)
    if (noSkill.length) log(`no SKILL.md yet for: ${noSkill.join(', ')} — run team-base-skills.js first; they are left out of the roundtable`)
    const seated = got.filter(c => c && c.skill_exists)
    const edited = seated.filter(c => c.edited).map(c => c.slug)
    if (edited.length) log(`Roundtable Card written or completed for: ${edited.join(', ')}`)
    if (seated.length < 2) { log('fewer than 2 members have a skill: roundtable and README not written'); return { cards: got, roundtable: null, readme: null } }
    const rt = await A(roundtablePrompt(seated, [...failed, ...noSkill]), { label: 'roundtable', phase: 'Roundtable', schema: RT_OUT })
    if (!rt) log('roundtable agent returned nothing')
    else if (rt.dropped_contrasts.length) log(`roundtable: ${rt.dropped_contrasts.length} one-sided contrast(s) dropped: ${rt.dropped_contrasts.join('; ')}`)
    const rd = await A(readmePrompt(seated, rt), { label: 'readme', phase: 'README', schema: README_OUT })
    if (!rd) log('README agent returned nothing')
    return { cards: got, roundtable: rt, readme: rd }
  },
])

const resList = (resources || []).map((r, i) => r ? { member: MEMBERS[i].slug, ...r } : { member: MEMBERS[i].slug, error: 'no result' })
resList.filter(r => r.error).forEach(r => log(`resources agent returned nothing for ${r.member}`))

phase('Verify')
const wroteTeamFiles = Boolean(team && (team.roundtable || team.readme))
if (!wroteTeamFiles) log('no roundtable or README was written in this run: verification and fix skipped (fix the causes logged above and rerun)')
const reviews = wroteTeamFiles
  ? (await parallel(LENSES.map(l => () => A(l.prompt(), { label: `verify:${l.key}`, phase: 'Verify', schema: FINDINGS })))).filter(Boolean)
  : []
if (wroteTeamFiles && reviews.length < LENSES.length) log(`${LENSES.length - reviews.length} verifier(s) returned nothing`)
const findings = reviews.flatMap(r => r.findings.map(f => ({ ...f, lens: r.lens })))
const serious = findings.filter(f => f.severity !== 'minor').length
if (wroteTeamFiles) log(`verification: ${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers, ${serious} blocker+major)`)

phase('Fix')
let fix = null
if (findings.length) fix = await A(fixPrompt(findings), { label: 'fix:team-layer', phase: 'Fix', schema: FIX })
else if (wroteTeamFiles) log('no findings: fix step skipped')

return {
  team: TEAM_REL,
  cards: team && team.cards ? team.cards.map((c, i) => c ? { member: c.slug, edited: c.edited, skill_exists: c.skill_exists, quality_check: c.quality_check } : { member: MEMBERS[i].slug, error: 'no result' }) : null,
  resources: resList,
  roundtable: team ? team.roundtable : null,
  readme: team ? team.readme : null,
  findings: findings.length,
  serious_findings: serious,
  fix,
}
