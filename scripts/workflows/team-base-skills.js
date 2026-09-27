export const meta = {
  name: 'team-base-skills',
  description: 'T1: build each member\'s research-craft skill with the nuwa Phase 1-5 pipeline (six research agents, review, four-way-validated synthesis, SKILL.md from the research template, quality gate and blind tests, dual-agent refine)',
  whenToUse: 'After scripts/new_team.py has scaffolded a team from team.json. One pipeline per member; on small machines launch one workflow per member in parallel. Use args.from / args.to to stop at a checkpoint and resume after the user has looked.',
  phases: [
    { title: 'Research', detail: 'Phase 1: six parallel research agents per member write references/research/01-06 (quick tier: 01-03)' },
    { title: 'Review', detail: 'Phase 1.5: merge_research.py summary table, contradictions, one top-up search for thin dimensions' },
    { title: 'Synthesis', detail: 'Phase 2: four-way validation of methods, taste, signature works, workflows, boundary, Roundtable Card draft' },
    { title: 'Build', detail: 'Phase 3: SKILL.md from references/research-skill-template.md in team.json language + RESOURCES.md rows; quality_check.py 12/12' },
    { title: 'Test', detail: 'Phase 4: exam set from the notes, blind answers from SKILL.md alone, grading + citation check, fix (at most 2 rounds)' },
    { title: 'Refine', detail: 'Phase 5: optimizer lens + skill-creator lens (read-only), then apply non-conflicting changes; 12/12 again' },
  ],
}

// ---------------------------------------------------------------------------------------------
// Args (shared by all team workflows in scripts/workflows/):
//   args.repo     absolute path of the nuwa repo (has scripts/, references/)
//   args.team     team folder relative to repo, e.g. "product/bandit-team" (holds team.json)
//   args.scratch  absolute scratch dir for batch/chunk JSON files and backups (agents may write there)
//   args.date     "YYYY-MM-DD" (scripts cannot call Date.now())
//   args.members  array of member objects copied from team.json (slug, name, surname, living, hint, scholar,
//                 dblp, orcid, homepage, chase_hints, student_mode); each member runs independently through
//                 pipeline() (no barrier between members)
// Workflow-specific keys:
//   args.from, args.to   first / last step to run, each one of: research, review, synthesis, build, test, refine
//                        (default research .. refine). The root SKILL.md has user checkpoints after review (1.5),
//                        synthesis (2.5), test (4) and refine (5): to honour them, run with to: "review", show the
//                        returned table, then rerun with from: "synthesis", and so on. Steps read their inputs from
//                        files (research notes; the Phase 2 record in <scratch>/base-skills/<slug>/), so a later run
//                        in the same session can resume. from > research needs the earlier steps' files.
//   args.tier            "standard" (default: six research agents) or "quick" (agents 01-03 only, per the root SKILL.md)
//   args.dims            optional explicit list of research agents to run, e.g. ["02", "06"] (update runs); overrides tier
//   args.user_context    optional: the user's own field and career stage, for the domain-adaptation notes (Phase 0A)
//   args.word_budget     target maximum words for each SKILL.md (default 8000; the DFO base skills were 7.5k-8.7k)
//   args.example_team    optional team folder (relative to repo) of a finished team to imitate for shape only,
//                        e.g. "product/dfo-team"
// Outputs per member (<repo>/<team>/<slug>/): references/research/01-06-*.md, SKILL.md (type: research-craft, with a
//   Roundtable Card), references/sources/RESOURCES.md rows, and for student_mode members a Student Mode section plus
//   references/proof-playbook.md, open-problems.md, reading-path.md. Scratch: <scratch>/base-skills/<slug>/.
// Gates run by the agents: scripts/merge_research.py (Phase 1.5), scripts/quality_check.py 12/12 (Phases 3-5),
//   scripts/check_links.py (member folder). Next: team-layer.js (T2).
// Launch: Workflow({scriptPath: "<repo>/scripts/workflows/team-base-skills.js", args: {...}}).
// Cost: about 17-20 agents per member at the standard tier (6 research + review + synthesis + 2 build + 3-7 test + 3 refine).
// ---------------------------------------------------------------------------------------------

const ARGS = typeof args === 'string' ? JSON.parse(args) : args
function need(ok, msg) { if (!ok) throw new Error(`team-base-skills args: ${msg}`) }
need(ARGS && typeof ARGS === 'object', 'pass args as a JSON object')
need(typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'), 'args.repo must be an absolute path')
need(typeof ARGS.team === 'string' && ARGS.team.length > 0 && !ARGS.team.startsWith('/'), 'args.team must be relative to args.repo, e.g. "product/<team>"')
need(typeof ARGS.scratch === 'string' && ARGS.scratch.startsWith('/'), 'args.scratch must be an absolute path')
need(/^\d{4}-\d{2}-\d{2}$/.test(ARGS.date || ''), 'args.date must be "YYYY-MM-DD"')
need(Array.isArray(ARGS.members) && ARGS.members.length > 0, 'args.members must be a non-empty array copied from team.json')
ARGS.members.forEach((m, i) => need(m && /^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') && m.name, `args.members[${i}] needs a kebab-case slug and a name`))

const STEPS = ['research', 'review', 'synthesis', 'build', 'test', 'refine']
const FROM = STEPS.indexOf(ARGS.from || 'research')
const TO = STEPS.indexOf(ARGS.to || 'refine')
need(FROM >= 0 && TO >= 0 && FROM <= TO, `args.from / args.to must be among ${STEPS.join(', ')} with from <= to`)
// args keys this workflow reads; anything else is logged (the kit mixes snake_case and camelCase option names)
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'from', 'to', 'tier', 'dims', 'user_context', 'word_budget', 'example_team']
const unknownArgs = Object.keys(ARGS).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-base-skills.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)
const on = s => { const i = STEPS.indexOf(s); return i >= FROM && i <= TO }

const REPO = ARGS.repo.replace(/\/+$/, '')
const TEAM_REL = ARGS.team.replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCRATCH = ARGS.scratch.replace(/\/+$/, '')
const DATE = ARGS.date
const MEMBERS = ARGS.members
const WORDS = Number.isInteger(ARGS.word_budget) && ARGS.word_budget > 1000 ? ARGS.word_budget : 8000
const USER_CTX = typeof ARGS.user_context === 'string' && ARGS.user_context.trim() ? ARGS.user_context.trim() : ''
const EXAMPLE = typeof ARGS.example_team === 'string' && ARGS.example_team.trim()
  ? `Worked example of a finished team (read for shape and level of detail only; never copy its field, researchers or content): ${REPO}/${ARGS.example_team.replace(/^\.\//, '').replace(/\/+$/, '')}/.`
  : ''
const NOREPLY = 'nuwa-skill@users.noreply.github.com'

const HOUSE = `House rules for every agent in this workflow (nuwa research-team kit):
- Read ${TEAM}/team.json first: "field", "language" (the language of every member skill and research note you write), "title", "roundtable" (the slug of the team's roundtable skill), and the member entries (name, surname, living, hint, scholar, dblp, orcid, homepage, student_mode). The entry there is authoritative if it differs from this prompt.
- This is the nuwa (女娲) research-craft mode: capture HOW the researcher does research (choosing problems, designing experiments or proofs, judging results, writing, supervising), not WHAT they discovered. The repo's root SKILL.md ("研究Skill" section) and references/research-extraction-framework.md are written in Chinese; their rules apply whatever language you write in.
- Evidence: every paper you name carries a DOI, an arXiv id, or venue + year + full title that you checked with a tool in this run; never cite from memory (invented citations are the commonest failure). Quotes are verbatim with their source (and page when taken from a full text); never put a paraphrase inside quotation marks. If you did not read something, write "not read" instead of guessing. Keep contradictions as contradictions. Label what the researcher SAID (stated), what they DID (practice: papers, code, records) and what OTHERS observed.
- Honesty over polish: a skill that marks its gaps honestly beats one that looks complete but invents. A research stage without evidence stays empty and says so.
- Sources: public and legitimate only. Never Sci-Hub, LibGen, Z-Library or other shadow libraries, never paywall circumvention, never scraping behind a login. Do not use Zhihu, WeChat official accounts or Baidu Baike as sources.
- Privacy: never open, read, quote or copy anything under a references/sources/private/ folder. Never send the user's email address or any other personal identifier to an external service; where an API insists on an email parameter (e.g. Unpaywall) use ${NOREPLY}. A living researcher is distilled from public academic output and public statements only.
- Tools: load WebSearch/WebFetch with ToolSearch ("select:WebSearch,WebFetch") if they are not loaded. Google Scholar blocks curl (use WebFetch). WebSearch has a per-session budget (about 200 calls shared by all agents): prefer curl/WebFetch on known URLs. Kill background processes by exact PID, never with pkill -f.
- Scope: edit only the files this step names as its outputs (scratch files go under ${SCRATCH}/base-skills/<member-slug>/). Do not touch other members' folders, the repo's root SKILL.md, references/ or scripts/, and do not git commit or push: the session that launched this workflow commits after the stage.`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A(): opts.phase and opts.label are required')
  return agent(`${HOUSE}\n\n${prompt}`, opts)
}

function who(m) {
  const bits = []
  if (m.hint) bits.push(`hint: ${m.hint}`)
  bits.push(m.living === false ? 'deceased (historical lens)' : 'living')
  if (m.scholar) bits.push(`Google Scholar user id ${m.scholar}`)
  if (m.dblp) bits.push(`DBLP pid ${m.dblp}`)
  if (m.orcid) bits.push(`ORCID ${m.orcid}`)
  if (m.homepage) bits.push(`homepage ${m.homepage}`)
  if (m.student_mode) bits.push('student_mode: true (the user works with this researcher)')
  return `${m.name} (${bits.join('; ')})`
}
const P = m => {
  const MD = `${TEAM}/${m.slug}`
  const SCR = `${SCRATCH}/base-skills/${m.slug}`
  return { MD, RES: `${MD}/references/research`, SRC: `${MD}/references/sources`, SKILL: `${MD}/SKILL.md`, SCR, SYN: `${SCR}/phase2-synthesis.md`, REVIEW: `${SCR}/phase1-review.md`, EXAM: `${SCR}/phase4-exam.json` }
}
const SUR = m => m.surname || m.name

// ---------- Phase 1: the six research dimensions (references/research-extraction-framework.md §二) ----------
const DIMS = [
  {
    n: '01', file: '01-publications.md', title: 'Signature works and the publication landscape',
    look: m => `the Google Scholar profile via WebFetch${m.scholar ? ` (https://scholar.google.com/citations?user=${m.scholar}&hl=en&pagesize=100, citation order: enough for the landscape; the complete harvest is a later step)` : ''}; DBLP via python3 ${REPO}/scripts/dblp_works.py --name "${m.name}" then --pid <pid> (it uses sparql.dblp.org because the dblp.org REST API sits behind a bot wall); Semantic Scholar; arXiv (arxiv.org/search HTML; export.arxiv.org rejects cloud IPs); OpenAlex through python3 ${REPO}/scripts/fetch_publications.py "${m.name}" --out ${P(m).SRC}/publications only when the environment variable OPENALEX_API_KEY is set (shared cloud IPs get HTTP 429 without it; never pass --mailto with the user's email); the researcher's homepage and CV.`,
    extract: `the publication landscape (topics by five-year period, the first-author to last-author shift, the collaboration network and likely students, usual venues, most-cited works, recent works) and 3-5 signature works (most cited + the ones the researcher calls most important + turning points), each dissected as in framework §五: origin, why then, key insight, minimum evidence, abandoned paths, reception, method it shows. Mark "inferred" wherever no primary source gives the origin or the abandoned paths.`,
  },
  {
    n: '02', file: '02-methodology.md', title: 'Stated methodology (what they say research should be)',
    look: () => `essays, blog posts and lecture notes on how to do research; award and plenary lectures; interviews where they talk about method; advice to PhD students; prefaces of their books; tutorial talks (look for transcripts or slides; for a video talk with subtitles use bash ${REPO}/scripts/download_subtitles.sh <URL> <dir> and python3 ${REPO}/scripts/srt_to_transcript.py <srt> <txt>, saving transcripts under the member's references/sources/talks/).`,
    extract: `what they CLAIM about research, sorted into the seven layers of framework §一 (taste, problem choice, idea generation, experiments/execution, judging results, writing and talks, research organisation). A claim repeated at least 3 times is a real belief: count repetitions. Give the exact words (or a faithful paraphrase marked as such), source, date, primary/secondary. If early and late statements disagree, record both with dates. Only record what they said; whether they practise it is agent 03's job.`,
  },
  {
    n: '03', file: '03-process-evidence.md', title: 'Process evidence (what they actually do)',
    look: () => `the code and software they released (repository structure, test scripts, READMEs, changelogs, release notes), paper appendices and experiment sections (baselines, test problems, ablations, benchmark protocols), published reviews and rebuttals (OpenReview where it exists), errata and corrections, early versus final versions (arXiv v1 versus the journal version), abandoned, rejected or retracted work.`,
    extract: `BEHAVIOUR, not statements: how baselines and test problems are chosen, what gets done first, how they debug, how they answer criticism, what they drop. Open the repositories and the papers themselves, not summaries of them. For each practice, name the paper/repository/section where it shows.`,
  },
  {
    n: '04', file: '04-mentorship.md', title: 'Students and collaborators',
    look: () => `students' blog posts and memorial pieces, PhD thesis acknowledgements, lab or group web pages, onboarding or lab guides, collaborator interviews, Festschrift volumes, obituaries and biographical memoirs.`,
    extract: `supervision style, group habits, lab culture, and TACIT knowledge (what the students all know but the papers never say), each labelled "according to <who>, <source>" and marked secondary.`,
  },
  {
    n: '05', file: '05-peer-critique.md', title: 'Peer critique',
    look: () => `failed replications, published comments and replies, counterexamples to their results, public reviews, critical essays, predictions that did not come true, rival schools and competing methods, benchmark studies that compare their methods with others.`,
    extract: `blind spots, limits of applicability, and judgements shown to be wrong; for each critique, the critic, the source, and whether and how it was answered.`,
  },
  {
    n: '06', file: '06-trajectory.md', title: 'Research trajectory',
    look: m => `the full academic timeline (education, positions, prizes), advisor and student lineage (Mathematics Genealogy Project and similar), direction changes and their stated reasons, ${m.living === false ? 'obituaries and memoirs, and who maintains or extends the work now' : 'the last 12 months (new papers, talks, software, moves)'}.`,
    extract: `what triggered each turn (a new tool? new data? a failure? a move?), when they enter and leave a topic (before or after the consensus), a dated timeline table, and the latest activity with dates.`,
  },
]
const DIM_SEL = Array.isArray(ARGS.dims) && ARGS.dims.length
  ? DIMS.filter(d => ARGS.dims.map(String).includes(d.n))
  : (ARGS.tier === 'quick' ? DIMS.slice(0, 3) : DIMS)
need(DIM_SEL.length > 0, 'args.dims selects no research agent (use "01" .. "06")')

// ---------- schemas ----------
const FINDING = { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, location: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'problem', 'fix'] }
const NOTE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    sources_total: { type: 'number' },
    primary_sources: { type: 'number' },
    verifiable_ids: { type: 'number' },
    key_findings: { type: 'array', items: { type: 'string' } },
    contradictions: { type: 'array', items: { type: 'string' } },
    gaps: { type: 'array', items: { type: 'string' } },
  },
  required: ['file', 'sources_total', 'primary_sources', 'key_findings', 'contradictions', 'gaps'],
}
const REVIEW = {
  type: 'object',
  properties: {
    table: { type: 'string' },
    dimensions: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, sources: { type: 'number' }, verdict: { type: 'string', enum: ['ok', 'thin', 'missing'] }, topped_up: { type: 'boolean' }, note: { type: 'string' } }, required: ['file', 'verdict'] } },
    contradictions: { type: 'array', items: { type: 'string' } },
    thin_left: { type: 'array', items: { type: 'string' } },
    ready: { type: 'boolean' },
    reason: { type: 'string' },
  },
  required: ['table', 'dimensions', 'contradictions', 'thin_left', 'ready', 'reason'],
}
const SYNTH = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    core_methods: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, recurrence: { type: 'boolean' }, say_do: { type: 'boolean' }, executable: { type: 'boolean' }, exclusive: { type: 'boolean' }, evidence: { type: 'string' } }, required: ['name', 'recurrence', 'say_do', 'executable', 'exclusive', 'evidence'] } },
    heuristics: { type: 'number' },
    claimed_unverified: { type: 'array', items: { type: 'string' } },
    taste_criteria: { type: 'number' },
    workflows: { type: 'array', items: { type: 'string' } },
    stages_without_evidence: { type: 'array', items: { type: 'string' } },
    signature_works: { type: 'array', items: { type: 'string' } },
    tensions: { type: 'array', items: { type: 'string' } },
    honest_boundary: { type: 'array', items: { type: 'string' } },
    roundtable_lens: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['file', 'core_methods', 'heuristics', 'claimed_unverified', 'taste_criteria', 'workflows', 'stages_without_evidence', 'signature_works', 'tensions', 'honest_boundary', 'roundtable_lens', 'summary'],
}
const BUILD = {
  type: 'object',
  properties: {
    skill_file: { type: 'string' },
    words: { type: 'number' },
    description_chars: { type: 'number' },
    core_methods: { type: 'number' },
    heuristics: { type: 'number' },
    workflows: { type: 'number' },
    signature_works: { type: 'number' },
    quality_check: { type: 'string' },
    quality_passed: { type: 'boolean' },
    links: { type: 'string' },
    extra_files: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['skill_file', 'words', 'description_chars', 'core_methods', 'quality_check', 'quality_passed', 'links', 'extra_files', 'summary'],
}
const RESOURCES = {
  type: 'object',
  properties: {
    rows: { type: 'number' },
    verified: { type: 'number' },
    leads: { type: 'number' },
    saved_locally: { type: 'number' },
    unverifiable: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['rows', 'verified', 'leads', 'unverifiable', 'summary'],
}
const EXAMSET = {
  type: 'object',
  properties: {
    exam_file: { type: 'string' },
    questions: { type: 'array', items: { type: 'object', properties: { qid: { type: 'string' }, kind: { type: 'string', enum: ['known', 'taste', 'edge', 'executability'] }, question: { type: 'string' } }, required: ['qid', 'kind', 'question'] } },
  },
  required: ['exam_file', 'questions'],
}
const ANSWERS = {
  type: 'object',
  properties: { answers: { type: 'array', items: { type: 'object', properties: { qid: { type: 'string' }, answer: { type: 'string' }, methods_used: { type: 'array', items: { type: 'string' } }, papers_named: { type: 'array', items: { type: 'string' } } }, required: ['qid', 'answer'] } } },
  required: ['answers'],
}
const GRADE = {
  type: 'object',
  properties: {
    passed: { type: 'boolean' },
    items: { type: 'array', items: { type: 'object', properties: { qid: { type: 'string' }, verdict: { type: 'string', enum: ['pass', 'partial', 'fail'] }, problem: { type: 'string' } }, required: ['qid', 'verdict'] } },
    citations_checked: { type: 'number' },
    citations_failed: { type: 'array', items: { type: 'string' } },
    findings: { type: 'array', items: FINDING },
  },
  required: ['passed', 'items', 'citations_checked', 'citations_failed', 'findings'],
}
const FIX = {
  type: 'object',
  properties: { applied: { type: 'number' }, declined: { type: 'array', items: { type: 'string' } }, weak_dimensions_marked: { type: 'array', items: { type: 'string' } }, quality_check: { type: 'string' }, words: { type: 'number' }, summary: { type: 'string' } },
  required: ['applied', 'declined', 'quality_check', 'summary'],
}
const LENS = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    scores: { type: 'array', items: { type: 'object', properties: { dimension: { type: 'string' }, score: { type: 'number' }, note: { type: 'string' } }, required: ['dimension', 'score'] } },
    changes: { type: 'array', items: { type: 'object', properties: { location: { type: 'string' }, problem: { type: 'string' }, rewrite: { type: 'string' } }, required: ['location', 'problem', 'rewrite'] } },
  },
  required: ['lens', 'changes'],
}
const APPLY = {
  type: 'object',
  properties: { applied: { type: 'array', items: { type: 'string' } }, declined: { type: 'array', items: { type: 'string' } }, quality_check: { type: 'string' }, words: { type: 'number' }, summary: { type: 'string' } },
  required: ['applied', 'declined', 'quality_check', 'summary'],
}

// ---------- prompts ----------
function researchPrompt(m, d) {
  const { MD, RES, SRC } = P(m)
  return `Task (nuwa research-craft Phase 1, research agent ${d.n} of 06): research ${who(m)} — ${d.title}.
Member skill folder: ${MD}/. Output: ${RES}/${d.file} (mkdir -p ${RES} first). If the file already has substantial content (an update run), extend it: keep what is there, add new findings under a dated heading, and mark anything the new evidence contradicts.
Read first: ${REPO}/references/research-extraction-framework.md §一 (seven layers) and §二 (the six research agents and their hard requirements).
Local corpus first: if ${SRC}/papers, talks, essays or software already hold files the user supplied (never private/), read the relevant ones before searching the web: user-supplied primary material outranks every web source. Mark findings from them "from user-supplied material".
Where to look: ${d.look(m)}
What to extract: ${d.extract}
${d.n === '04' && m.student_mode ? `This member has a Student Mode (the user works with the researcher). Also collect PUBLIC material that helps a student: the group's public theses, course pages and public lecture notes, reading lists the group published, and the open problems the papers state in their conclusions. Never ask for or look at private material.\n` : ''}Hard requirements (framework §二):
- Every paper: DOI, arXiv id, or venue + year + full title — checked with a tool. No identifier, no entry.
- Tag each item [stated] / [practice] / [observed] / [inferred], and primary or secondary.
- Record failures, abandoned directions, rejected papers and retracted claims: they carry more information than successes.
- Note the era and resource context of each practice (compute, tools, team size, seniority).
- Keep contradictions; do not reconcile them.
- About 5 minutes without useful results on a sub-question: move on and list it under Gaps.
File structure: a header (researcher, dimension, research date ${DATE}, number of sources consulted), the findings grouped as the framework asks, "Contradictions", "Gaps" (what you could not find), and "Sources" (one line each: title, author, date, URL or DOI, primary/secondary).
Write in team.json "language". Edit only ${RES}/${d.file} (and transcripts you save under ${SRC}/talks/).
Return the structured summary.`
}

function reviewPrompt(m, notes) {
  const { MD, RES, REVIEW: RV } = P(m)
  return `Task (nuwa Phase 1.5, research review checkpoint) for ${m.name} (${MD}/).
The research agents reported: ${JSON.stringify(notes)}
1. Run python3 ${REPO}/scripts/merge_research.py ${MD} --mode research and keep its markdown table.
2. Read every research note in ${RES}/ (01-06). Judge each dimension: enough usable sources? Do 02 (stated) and 03 (process evidence) together support at least a few say-do comparisons, which the four-way validation needs? Is the primary share above half? Any paper without an identifier (remove it or find the identifier)? Contradictions between agents (agent X says A, agent Y says B)?
3. For a dimension that is clearly thin (fewer than about 5 usable sources, or 02/03 unable to support any say-do comparison), run ONE targeted top-up search yourself and append what you find to that note under "Top-up (${DATE})". Do not rewrite the notes otherwise.
4. Rerun merge_research.py and write ${RV}: the table, the contradictions, the thin dimensions left, and your verdict.
This is the Phase 1.5 checkpoint the user sees ("garbage in, garbage out": say plainly whether the research is good enough to synthesise). Edit only the notes you topped up and ${RV}.
Return the table (markdown), per-dimension verdicts, contradictions, what is still thin, and ready (true/false) with the reason.`
}

function synthPrompt(m, rv) {
  const { MD, RES, SYN } = P(m)
  const studentLine = m.student_mode
    ? `\n12. Student Mode material (student_mode is true): the researcher's recurring argument, proof, derivation or experiment templates (each tied to verified papers, or marked "template, inference"); open problems the papers themselves state (stated) versus ones you infer (inferred); a staged reading path of verified works for a new student.`
    : ''
  return `Task (nuwa Phase 2, synthesis) for ${m.name}. Do not write SKILL.md in this step.
Read: every note in ${RES}/ (01-06; a quick-tier run has 01-03 only), the Phase 1.5 review ${rv ? `(summary: ${JSON.stringify({ ready: rv.ready, thin_left: rv.thin_left, contradictions: rv.contradictions })})` : `in ${P(m).REVIEW} if it exists`}, and ${REPO}/references/research-extraction-framework.md §三 to §九 and §十一.
Domain adaptation (Phase 0A): ${USER_CTX ? `the user's own context is "${USER_CTX}"` : `no user context was given; assume the user works in the team's field ("field" in team.json)`}.
Do:
1. Candidates: list every candidate research method found in the notes (usually 15-30).
2. Four-way validation of each (framework §三): (1) cross-project recurrence: in at least 2 different projects, papers or periods; (2) say-do consistency: stated in 02 AND visible in practice (03, or the papers in 01); (3) executable: can be written as numbered steps whose actions differ from standard practice; (4) exclusivity: not what every good researcher does. All four -> core method (keep 3-7, most exclusive first; fewer deep ones beat many shallow ones). Executable + at least one other check -> heuristic (5-10). Stated only, no practice evidence -> "claimed but unverified" (goes to the Honest Boundary, never a core method). Not executable -> drop, however quotable.
3. Research taste (§四): 5-8 criteria for good research and warning signs of bad research, each with at least 2 pieces of evidence; turn them into 5-8 yes/no quick-check questions; list 2-3 real forks in the researcher's career (what they chose, what they dropped, with sources) for the taste-prediction test.
4. Signature-work anatomy (§五) for 2-5 works from 01, each tied to a core method; every core method backed by at least one anatomy; "inferred" / "unknown" wherever there is no primary source.
5. Stage workflows (§六): only stages with evidence (at least 3), each with input, researcher-specific steps labelled with methods, a 🔴 checkpoint / stop rule, output, and one line on how it differs from textbook practice. List the stages without evidence ("no distillable method").
6. Filters (§七) for every method: era, field, resource threshold, seniority; give the adjusted version for a lone researcher or an early-career researcher, and note what needs translating for the user's context.
7. Tacit knowledge and the honest boundary (§八): tacit-knowledge gaps, era/resource differences, field boundary, the claimed-but-unverified list, research date ${DATE}${m.living === false ? ', and that the skill is a historical lens reflecting work up to the researcher\'s death' : ''}.
8. Inner tensions: at least 2, each with evidence on both sides (e.g. depth versus pivot, stated versus practised, simplicity versus generality).
9. Research anti-patterns the researcher opposed (with sources); mentor-voice features (only with sources; otherwise say none are documented); academic lineage.
10. Integrity (§九): anything the researcher said publicly against misconduct, to quote in the Research Integrity Rules.
11. Roundtable Card draft for the team: lens in one line; "leads when" (problem signals in the team's field); first questions this lens asks; default recommendation; what it will push back on; likely disagreements with the OTHER members listed in team.json (inferred from the methods on both sides, labelled as inferred, naming the papers each side rests on if known); blind spots.${studentLine}
Write all of it to ${SYN} (mkdir -p its folder): this is the Phase 2 record, the input of Phase 3 and what the user checks at checkpoint 2.5. Every item points to the note and the source it rests on.
Keep the final skill in mind: SKILL.md should stay at or under about ${WORDS} words, so depth on fewer methods beats breadth.
Edit only ${SYN}. Return the structured summary (the checkpoint 2.5 view).`
}

function buildPrompt(m, syn) {
  const { MD, RES, SYN, SKILL, SCR } = P(m)
  const student = m.student_mode
    ? `
- Student Mode (student_mode is true): add "## Student Mode" right after Activation Rules. It turns on when the user says they are in ${m.name}'s group or supervised by ${m.name}, or says "student mode"; "exit student mode" turns it off. Rules to write: the real supervisor always overrides the skill (everything here is inferred from public work; write "${SUR(m)}'s published work suggests …", never "${SUR(m)} thinks/wants …"); private materials first: at the start of a student-mode task the skill checks references/sources/private/ (the user's own non-public notes: highest priority, quoted only inside the user's own conversation, never copied into public files, commits or roundtable outputs; if the folder is empty, say so once and continue); default routing (proofs or derivations -> references/proof-playbook.md; choosing or scoping a problem -> references/open-problems.md + the taste quick-check; before a supervisor meeting -> a pre-meeting self-review workflow; "what should I read" -> references/reading-path.md); tone of a senior labmate preparing the student, not a stand-in supervisor; hard limits (no predictions of the supervisor's personal reactions, authorship decisions or evaluations of people; no messages impersonating them; no presenting unverified proofs as finished).
  Write the three files from the Phase 2 record: ${MD}/references/proof-playbook.md (recurring argument/proof/experiment templates, each "(verified: <paper id>)" or "(template, inference)"), ${MD}/references/open-problems.md ("stated" versus "inferred" open problems with sources; difficulty marked as the skill author's guess), ${MD}/references/reading-path.md (staged reading order of verified works; "not a list ${SUR(m)} published"). Each file opens with its research date and a "the real supervisor wins" note. If ${MD}/references/sources/private/README.md is missing, create it from ${REPO}/references/team-templates/private-README.md (replace {{MEMBER_NAME}} and {{MEMBER_SLUG}}); never open anything else in private/.`
    : ''
  return `Task (nuwa Phase 3, build the skill) for ${who(m)}.
Inputs: the Phase 2 record ${SYN}${syn ? ` (summary: ${JSON.stringify(syn)})` : ''}, the notes in ${RES}/, and the template ${REPO}/references/research-skill-template.md (in Chinese). ${EXAMPLE}
If ${SKILL} already exists, copy it to ${SCR}/SKILL.before.md first and update it conservatively (keep what the new evidence does not contradict; mark corrections) instead of starting over.
Write ${SKILL} in team.json "language", section by section from the template:
- Frontmatter: "name: ${m.slug}" (the folder name; the roundtable finds members by it), a "description: |" block of at most about 300 words and well under 1024 characters: one sentence on what is distilled and from what, what to use it for, explicit triggers ("${SUR(m)} lens", "how would ${SUR(m)} approach this", "use ${SUR(m)}'s method", "${SUR(m)}.skill"), "Also loaded by <roundtable slug from team.json>.", and "Not for general questions." — no keyword lists; "type: research-craft"; the research date ${DATE} ("researched: ${DATE}", or "调研时间: ${DATE}" when the language is Chinese).
- Headings: in Chinese, keep the template's headings. In any other language use the English names below (scripts/quality_check.py recognises both): 使用说明 How to Use · 激活规则 Activation Rules · 研究诚信规则 Research Integrity Rules · 研究任务路由 Research Task Routing · 回答工作流（Agentic Protocol） Agentic Protocol (do NOT call it "… Workflow": quality_check.py takes the first "##" heading containing "Workflow" as the stage-workflow section) · 研究品味 Research Taste (### Marks of good research / ### Warning signs of bad research / ### Taste quick-check) · 核心研究方法 Core Research Methods ("### Method N: <name>" with **One line**, **Evidence** (Stated / Practice / Say–do consistency: ✅ stated + practised or ⚠️ stated only), **Steps** (numbered, at least 2), **Applies to stage**, **Different from standard practice**, **Limitations**) · 阶段工作流 Stage Workflows ("### Workflow A: …" with **Input**, **Steps**, **🔴 Checkpoint**, **Output**) · 研究启发式 Research Heuristics · 代表作解剖 Signature Work Anatomy (one "###" per work) · 研究反模式 Research Anti-patterns · 研究轨迹 Research Trajectory (with "### Latest") · 学术谱系 Academic Lineage · 内在张力 Inner Tensions · 导师口吻 Mentor Voice (optional) · 诚实边界 Honest Boundary · 附录：调研来源 Sources (Appendix) (make it the first "##" heading containing "Source" or "Reference"; subsections Papers (primary) / Stated methodology (primary) / Process evidence (primary) / Students, collaborators and peers (secondary); every entry with DOI, arXiv id or URL).
- Content rules: 3-7 core methods exactly as validated in Phase 2 (never promote a claimed-but-unverified method); the Research Integrity Rules complete and unchanged in substance (quote the researcher if they spoke against misconduct); the activation disclaimer once ("distilled from public work, not ${SUR(m)}'s own advice"); the routing table keeps only rows with evidence and says so for the rest; stages without evidence say "no distillable ${SUR(m)} method" and mark generic advice "not ${SUR(m)}-style"; every paper cited with an identifier; the Agentic Protocol's fact-finding step names concrete checks derived from the methods (not "search for related information").
- Team additions (not in the template): in Activation Rules add "When convened by <roundtable slug>, answer from the Roundtable Card first and keep it short."; add "## Roundtable Card" just before the Honest Boundary with exactly these bullets, from the Phase 2 draft: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member; inferred from each side's methods, labelled so; name the papers each side rests on; "no dispute documented" unless one is), **Blind spots**. Keep the card under about 350 words: the roundtable moderator reads only this section.
- ${m.living === false ? 'Historical lens: say in How to Use and the Honest Boundary that the skill reflects work up to the researcher\'s death; later developments are others\' work.' : 'Living researcher: the Honest Boundary gives the research date and recommends periodic updates.'}${student}
- The attribution footer from the template (in English: "> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode").
- Word budget: at most about ${WORDS} words (wc -w). Keep long evidence in the research notes and link to them instead of repeating it.
Gate: run python3 ${REPO}/scripts/quality_check.py ${SKILL}. It must report 12/12 in research mode; fix and rerun until it does (at most 5 reruns; report the last output honestly if it still fails). Then run python3 ${REPO}/scripts/check_links.py ${MD} (0 broken links).
Edit only ${SKILL}${m.student_mode ? ', the three student-mode files and private/README.md (create only)' : ''}. Return the structured summary.`
}

function resourcesPrompt(m) {
  const { MD, RES, SRC } = P(m)
  return `Task (nuwa Phase 3, resource tracker) for ${m.name}. Output: ${SRC}/RESOURCES.md.
Start from the existing file (the team scaffold fills ${REPO}/references/team-templates/member-RESOURCES.md and leaves [TODO: …] items) or, if there is none, from that template (replace {{MEMBER_NAME}}, {{MEMBER_SLUG}} and {{SCHOLAR_URL}}; no "{{" may remain).
Fill the TODO items the template assigns to team-base-skills.js (T1): the research-date line, and one row per source found by the research notes ${RES}/01-06 (papers, books, reports, software, talks, interviews, essays, memoirs, student recollections, critiques, profiles). Verify each row with a tool in this run: DOI resolves (curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> gives 30x) and the Crossref title matches, or the arXiv abs page title matches, or the page exists and says what the row says. Status ✅ verified / ⚠️ lead (unverified: reason in Notes, must not be cited as verified) / 📥 saved locally. "Used in" names the notes (01-06) that use it. Merge duplicates; keep numbering.
Leave TODO items that the template assigns to later steps (the Google Scholar row for team-harvest.js; the deep-tier rows for T3/T4) exactly as they are. Never open private/.
Edit only ${SRC}/RESOURCES.md. Return counts and the sources you could not verify.`
}

function examPrompt(m, syn) {
  const { MD, RES, SYN, EXAM } = P(m)
  return `Task (nuwa Phase 4, set the exam) for ${m.name}. You write questions and expected answers; a different agent answers them blind from SKILL.md alone, and a third grades.
Read the notes in ${RES}/ and the Phase 2 record ${SYN} (not SKILL.md).
Write 6 questions:
- 3 "known": research situations where ${m.name} gave clear, documented advice or made a documented research decision (primary sources only).
- 1 "taste": a real fork in the career (from the Phase 2 taste-prediction list): present the options as they looked then and ask which direction this lens would take.
- 1 "edge": a research question outside the researcher's field or era${USER_CTX ? ` (set it in the user's context: ${USER_CTX})` : ''}; the right answer is a hedged inference ("based on Methods X and Y, probably … but not certain"), not a confident verdict.
- 1 "executability": a realistic stuck research situation in the team's field (an experiment that fails, a proof that does not close, a reviewer's objection); the right answer is next steps with checkpoints and method labels, not encouragement.
Write ${EXAM}: a JSON list of {qid, kind, question, expected, evidence (source + identifier)}.
Return only qid, kind and question for each (never the expected answers).`
}

function answerPrompt(m, qs) {
  const { SKILL, RES, SCR } = P(m)
  return `Task (nuwa Phase 4, blind answers). You are using a research-craft skill exactly as a user of it would. Read ${SKILL} (and only the files SKILL.md itself tells you to open for these situations, such as a technique catalog or student-mode files). Do NOT open ${RES}/ or anything under ${SCR}/: the test measures what SKILL.md alone carries.
Answer each question below as the skill instructs (follow its Activation Rules, routing and Agentic Protocol; verify any paper you name with a tool, as the skill's integrity rules demand; mark (unverified) otherwise). Label the methods you use.
Questions: ${JSON.stringify(qs)}
Return one answer per qid (150-300 words each), the methods used and the papers you named.`
}

function gradePrompt(m, qs, answers, round) {
  const { SKILL, EXAM } = P(m)
  return `Task (nuwa Phase 4, grading, round ${round}) for ${m.name}'s skill ${SKILL}. You are a strict, independent grader: assume a miss until the answer shows otherwise.
Expected answers and evidence: ${EXAM} (only the qids below are graded this round).
Answers given blind from SKILL.md: ${JSON.stringify(answers)}
Grade each qid: known -> direction consistent with the documented position (pass / partial / fail); taste -> did it predict the direction actually taken, for the right reasons; edge -> hedged, grounded in named methods, no invented certainty; executability -> concrete next steps with 🔴 checkpoints and method labels, different from generic advice (fail if it is encouragement or a literature review).
Citation check: every paper named in the answers, and a sample of at least 10 papers cited in SKILL.md (all of them if fewer), must resolve: DOI -> https://doi.org/<doi> gives 30x and the Crossref title matches; arXiv -> the abs page title matches; otherwise the venue + year + title must be confirmed by a search. List failures.
Also run python3 ${REPO}/scripts/quality_check.py ${SKILL} and report it.
For each miss, say what in SKILL.md caused it (a method weighted wrongly, a missing routing row, a vague step, a missing boundary) and give a concrete fix. Severity: blocker = invented citation or a claim the evidence contradicts; major = failed test item; minor = polish. passed = no fail verdicts and no blockers or majors. Read-only: edit nothing.
Questions graded: ${JSON.stringify(qs)}`
}

function fixPrompt(m, grade, round, final) {
  const { SKILL, SYN, RES, SCR } = P(m)
  return `Task (nuwa Phase 4, fix after test round ${round}) for ${m.name}'s skill ${SKILL}.
Grader's report: ${JSON.stringify(grade)}
Verify each finding yourself (graders can be wrong), then apply what you confirm: blockers and majors always, minors when cheap. Fix causes, not symptoms: if a known-position test failed because a method is weighted wrongly or missing, go back to the evidence (${RES}/, ${SYN}) and correct the method (Phase 2 rules still apply: four-way validation, 3-7 core methods). Replace or remove any citation that failed the check.
${final ? `This is the last round (the root SKILL.md allows two Phase 2-4 iterations). Whatever still fails after your fixes: write it into the Honest Boundary as a named weak dimension instead of polishing further, and list it in weak_dimensions_marked.` : 'A second test round re-asks the failed questions after your fix.'}
Stay within about ${WORDS} words. Rerun python3 ${REPO}/scripts/quality_check.py ${SKILL} until 12/12 and python3 ${REPO}/scripts/check_links.py ${P(m).MD}.
Edit only ${SKILL} (and the student-mode files if a finding concerns them). A copy for comparison: cp it to ${SCR}/SKILL.before-fix-${round}.md before editing. Return what you applied and declined.`
}

function lensPrompt(m, which) {
  const { SKILL, MD } = P(m)
  const a = `Lens A (auto-skill-optimizer). Score the skill 1-5 on eight structural dimensions: workflow clarity, boundary conditions, checkpoint design, instruction specificity, routing coverage, failure prevention, evidence traceability, size discipline (about ${WORDS} words at most). Then dry-run three typical prompts a user of this skill would send in the team's field (one of them a stuck-project request) and note where the skill leaves the model unsure what to do first or when to stop. Output the 2 weakest dimensions as concrete changes: location, problem, and the rewritten text.`
  const b = `Lens B (skill-creator). Review: (1) the frontmatter description — do the triggers cover how people will actually ask (and is it under 1024 characters, count them, without keyword stuffing)?; (2) the Activation Rules — are they operable (question routing, frequency limits such as "disclaimer once", failure prevention, the roundtable line)?; (3) Research Task Routing — does it cover the research situations users of this field really bring (list any missing one only if the skill has evidence for it)?; (4) is the Roundtable Card complete (seven bullets) and short?; (5) missing key information. Output 2-3 concrete changes: location, problem, and the rewritten text.`
  return `Task (nuwa Phase 5, dual-agent refine, read-only review) of ${SKILL} (member ${m.name}; folder ${MD}/).
${which === 'A' ? a : b}
Refinement standard: a change must make the skill act on activation (know what to do first and when to stop), not merely add content. Do not propose changes to the Research Integrity Rules except to restore something missing. Read-only: edit nothing.`
}

function applyPrompt(m, lenses) {
  const { SKILL, SCR, MD } = P(m)
  return `Task (nuwa Phase 5, apply the refinements) to ${SKILL}. Two read-only reviewers proposed changes: ${JSON.stringify(lenses)}
Copy the file to ${SCR}/SKILL.before-refine.md, then apply the non-conflicting changes that make the skill act on activation; where the two conflict, pick one and say why. Decline changes that only add bulk, weaken the integrity rules, or claim more than the evidence supports. Stay within about ${WORDS} words.
Rerun python3 ${REPO}/scripts/quality_check.py ${SKILL} until 12/12 and python3 ${REPO}/scripts/check_links.py ${MD}.
Edit only ${SKILL}. Return the change summary (the checkpoint the user confirms): applied, declined with reasons, quality check line, word count.`
}

// ---------- pipeline ----------
const skipped = STEPS.filter(s => !on(s))
if (skipped.length) log(`steps not run in this invocation (args.from/args.to): ${skipped.join(', ')}`)
if (on('research') && DIM_SEL.length < DIMS.length) log(`research agents not run: ${DIMS.filter(d => !DIM_SEL.includes(d)).map(d => d.file).join(', ')} (${Array.isArray(ARGS.dims) ? 'args.dims' : 'quick tier'})`)

phase('Research')
const results = await pipeline(
  MEMBERS,
  // Phase 1 — six research agents in parallel (a per-member barrier: the review needs all notes)
  (_, m) => {
    const st = { member: m.slug }
    if (!on('research')) return st
    return parallel(DIM_SEL.map(d => () => A(researchPrompt(m, d), { label: `research:${m.slug}:${d.n}`, phase: 'Research', schema: NOTE })))
      .then(ns => {
        const missing = DIM_SEL.filter((d, k) => !ns[k]).map(d => d.file)
        if (missing.length) log(`${m.slug}: research agent(s) returned nothing for ${missing.join(', ')}; the review step checks those notes`)
        return { ...st, notes: ns.filter(Boolean) }
      })
  },
  // Phase 1.5 — review checkpoint
  (st, m) => {
    if (!on('review')) return st
    return A(reviewPrompt(m, st.notes || []), { label: `review:${m.slug}`, phase: 'Review', schema: REVIEW }).then(rv => {
      if (!rv) log(`${m.slug}: review agent returned nothing`)
      else if (!rv.ready) log(`${m.slug}: Phase 1.5 says the research is not ready (${rv.reason}); ${on('synthesis') ? 'continuing — the thin dimensions must show in the Honest Boundary' : 'stopping here as requested'}`)
      return { ...st, review: rv }
    })
  },
  // Phase 2 — synthesis (record in scratch)
  (st, m) => {
    if (!on('synthesis')) return st
    return A(synthPrompt(m, st.review), { label: `synthesis:${m.slug}`, phase: 'Synthesis', schema: SYNTH }).then(sy => {
      if (!sy) throw new Error(`${m.slug}: synthesis agent returned nothing; later steps skipped`)
      const n = sy.core_methods.length
      if (n < 3 || n > 7) log(`${m.slug}: Phase 2 produced ${n} core methods (the rule is 3-7); the build step must resolve it`)
      return { ...st, synthesis: sy }
    })
  },
  // Phase 3 — SKILL.md and RESOURCES.md in parallel (disjoint files)
  (st, m) => {
    if (!on('build')) return st
    return parallel([
      () => A(buildPrompt(m, st.synthesis), { label: `build:${m.slug}`, phase: 'Build', schema: BUILD }),
      () => A(resourcesPrompt(m), { label: `resources:${m.slug}`, phase: 'Build', schema: RESOURCES }),
    ]).then(([b, r]) => {
      if (!b) throw new Error(`${m.slug}: build agent returned nothing; test and refine skipped`)
      if (!b.quality_passed) log(`${m.slug}: quality_check.py not at 12/12 after the build (${b.quality_check})`)
      if (b.words > WORDS * 1.15) log(`${m.slug}: SKILL.md has ${b.words} words (budget ${WORDS})`)
      if (!r) log(`${m.slug}: resources agent returned nothing; RESOURCES.md rows still TODO`)
      else if (r.unverifiable.length) log(`${m.slug}: ${r.unverifiable.length} source(s) left ⚠️ unverified in RESOURCES.md`)
      return { ...st, build: b, resources: r }
    })
  },
  // Phase 4 — exam, blind answers, grading, fix (at most 2 rounds)
  async (st, m) => {
    if (!on('test')) return st
    const exam = await A(examPrompt(m, st.synthesis), { label: `exam:${m.slug}`, phase: 'Test', schema: EXAMSET })
    if (!exam || !exam.questions.length) { log(`${m.slug}: no exam was set; Phase 4 tests skipped`); return { ...st, tests: null } }
    let qs = exam.questions
    const rounds = []
    for (let round = 1; round <= 2; round++) {
      const ans = await A(answerPrompt(m, qs), { label: `answer:${m.slug}:r${round}`, phase: 'Test', schema: ANSWERS })
      if (!ans) { log(`${m.slug}: blind-answer agent returned nothing in round ${round}; tests stop`); break }
      const grade = await A(gradePrompt(m, qs, ans.answers, round), { label: `grade:${m.slug}:r${round}`, phase: 'Test', schema: GRADE })
      if (!grade) { log(`${m.slug}: grader returned nothing in round ${round}; tests stop`); break }
      const serious = grade.findings.filter(f => f.severity !== 'minor').length
      rounds.push({ round, items: grade.items, citations_failed: grade.citations_failed, findings: grade.findings.length, serious })
      if (grade.passed && serious === 0) break
      const fix = await A(fixPrompt(m, grade, round, round === 2), { label: `fix:${m.slug}:r${round}`, phase: 'Test', schema: FIX })
      rounds[rounds.length - 1].fix = fix
      if (!fix) { log(`${m.slug}: fixer returned nothing in round ${round}`); break }
      if (round === 2 && fix.weak_dimensions_marked && fix.weak_dimensions_marked.length) log(`${m.slug}: still weak after 2 rounds, marked in the Honest Boundary: ${fix.weak_dimensions_marked.join('; ')}`)
      const failedIds = grade.items.filter(it => it.verdict !== 'pass').map(it => it.qid)
      qs = exam.questions.filter(q => failedIds.includes(q.qid))
      if (!qs.length) { if (round === 1) log(`${m.slug}: round 1 failed on citations or findings only; the fix handled them and no question needs re-asking`); break }
    }
    return { ...st, tests: rounds }
  },
  // Phase 5 — dual-agent refine
  (st, m) => {
    if (!on('refine')) return st
    return parallel(['A', 'B'].map(w => () => A(lensPrompt(m, w), { label: `refine-${w}:${m.slug}`, phase: 'Refine', schema: LENS })))
      .then(ls => {
        const got = ls.filter(Boolean)
        if (got.length < 2) log(`${m.slug}: ${2 - got.length} refine reviewer(s) returned nothing`)
        if (!got.length) return { ...st, refine: null }
        return A(applyPrompt(m, got), { label: `refine-apply:${m.slug}`, phase: 'Refine', schema: APPLY }).then(ap => ({ ...st, refine: ap }))
      })
  },
)

return MEMBERS.map((m, i) => results[i] || { member: m.slug, error: 'pipeline dropped this member (see log)' })
