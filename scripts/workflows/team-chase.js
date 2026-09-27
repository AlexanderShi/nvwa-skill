export const meta = {
  name: 'team-chase',
  description: 'T3.3: find legitimate open-access full texts (and verbatim abstracts) for the works acquire_fulltexts.py could not find, in chunks of ~20 per agent, then merge and re-index',
  whenToUse: 'Deep tier of a nuwa research team, after team-harvest.js and scripts/acquire_fulltexts.py have written papers/INDEX.md. Run one workflow per member in parallel on small machines.',
  phases: [
    { title: 'Plan', detail: 'per member: list no-oa works from INDEX.md + works.json into a chunk file with exact target paths' },
    { title: 'Chase', detail: 'one agent per chunk: member and team chase_hints first, then generic open repositories' },
    { title: 'Merge', detail: 'per member: record found URLs, merge_chase.py (abstracts + re-run acquisition), validate_works.py' },
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
//   args.chunk_size       works per chase agent (default 20)
//   args.max_searches     search attempts per work before moving on (default 4)
//   args.skip_ids         optional {"<member-slug>": ["S012", ...]} works not to chase (not the author's, known closed)
//   args.only_chunks      optional {"<member-slug>": [1, 3]} 1-based chunk numbers to (re)run; the others are skipped and logged
//   args.merge            default true; false leaves papers/abstracts-chase-*.json unmerged (run scripts/merge_chase.py later)
//   args.search_budget    WebSearch calls this run may use in total (default 24 per member); each chunk agent gets an equal
//                         share of its member's part (the session has about 200 shared by every agent; playbook §六)
//   skip_ids and only_chunks are keyed by member slug: a key that is not a member of this run is logged, and for
//   only_chunks it stops the run when a member of the run has no entry (a misspelt slug would re-run every chunk).
// Inputs per member: references/sources/publications/works.json and references/sources/papers/INDEX.md.
// Outputs per member: PDFs at the exact paths scripts/acquire_fulltexts.py expects (git-ignored), then (merge stage)
//   abstracts.json / abstract-sources.json / INDEX.md refreshed by scripts/merge_chase.py, found URLs added to works.json.
// Chunk files: <scratch>/chase/<member-slug>.json (a JSON array of chunks; each work has an exact "target" path), written
//   by scripts/chase_chunks.py in the Plan stage (a low-effort agent runs it and returns its summary).
// Book leads: the chase agents report open parts of books (table of contents, errata, reviews); the merge stage keeps
//   them in papers/book-leads.json ({"<id>": [{"part", "url"}]}), where team-increment.js find: ["book-parts"] starts.
// Abstract files: papers/abstracts-chase-<date>-r<run>-<chunk>.json. The planning agent picks <run> = 1 + the highest run
//   already on disk for that date, so a same-day rerun (e.g. with merge: false, or args.only_chunks) never overwrites an
//   unmerged file; a chase agent that still finds its file present writes <name>-b.json, -c.json … and reports the name.
//   scripts/merge_chase.py merges every abstracts-chase-*.json whatever its suffix.
// Gates run by the agents: scripts/merge_chase.py, scripts/validate_works.py (0 errors).
// Launch: Workflow({scriptPath: "<repo>/scripts/workflows/team-chase.js", args: {...}}).
// Cost baseline (DFO worked example, product/dfo-team/): ~5 agents and ~0.9M tokens per member.
// ---------------------------------------------------------------------------------------------

const ARGS = typeof args === 'string' ? JSON.parse(args) : args
function need(ok, msg) { if (!ok) throw new Error(`team-chase args: ${msg}`) }
need(ARGS && typeof ARGS === 'object', 'pass args as a JSON object')
need(typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'), 'args.repo must be an absolute path')
need(typeof ARGS.team === 'string' && ARGS.team.length > 0 && !ARGS.team.startsWith('/'), 'args.team must be relative to args.repo, e.g. "product/<team>"')
need(typeof ARGS.scratch === 'string' && ARGS.scratch.startsWith('/'), 'args.scratch must be an absolute path')
need(/^\d{4}-\d{2}-\d{2}$/.test(ARGS.date || ''), 'args.date must be "YYYY-MM-DD"')
need(Array.isArray(ARGS.members) && ARGS.members.length > 0, 'args.members must be a non-empty array copied from team.json')
ARGS.members.forEach((m, i) => need(m && /^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') && m.name, `args.members[${i}] needs a kebab-case slug and a name`))
// args keys this workflow reads (all snake_case, like every team workflow); anything else is logged
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'chunk_size', 'max_searches', 'skip_ids', 'only_chunks', 'merge', 'search_budget']
const unknownArgs = Object.keys(ARGS).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-chase.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)

const REPO = ARGS.repo.replace(/\/+$/, '')
const TEAM_REL = ARGS.team.replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCRATCH = ARGS.scratch.replace(/\/+$/, '')
const DATE = ARGS.date
const MEMBERS = ARGS.members
const CHUNK = Number.isInteger(ARGS.chunk_size) && ARGS.chunk_size > 0 ? ARGS.chunk_size : 20
const MAXS = Number.isInteger(ARGS.max_searches) && ARGS.max_searches > 0 ? ARGS.max_searches : 4
const SKIP_IDS = ARGS.skip_ids && typeof ARGS.skip_ids === 'object' ? ARGS.skip_ids : {}
const ONLY = ARGS.only_chunks && typeof ARGS.only_chunks === 'object' ? ARGS.only_chunks : {}
const DO_MERGE = ARGS.merge !== false
const NOREPLY = 'nuwa-skill@users.noreply.github.com'
const RUN_SLUGS = MEMBERS.map(m => m.slug)
for (const [key, strict] of [['only_chunks', true], ['skip_ids', false]]) {
  const v = ARGS[key]
  if (v === undefined || v === null) continue
  need(typeof v === 'object' && !Array.isArray(v), `args.${key} must be an object keyed by member slug, e.g. {"${RUN_SLUGS[0]}": ...}`)
  const unknown = Object.keys(v).filter(k => !RUN_SLUGS.includes(k))
  if (!unknown.length) continue
  const uncovered = RUN_SLUGS.filter(k => !(k in v))
  need(!(strict && uncovered.length), `args.${key} names ${unknown.join(', ')}, not a member of this run (${RUN_SLUGS.join(', ')}); ${uncovered.join(', ')} would then run every chunk. Fix the slug.`)
  log(`team-chase.js: args.${key} has entries for member(s) not in this run, ignored: ${unknown.join(', ')}`)
}
const BUDGET = Number.isInteger(ARGS.search_budget) && ARGS.search_budget >= 0 ? ARGS.search_budget : 24 * MEMBERS.length
const SHARE = Math.floor(BUDGET / MEMBERS.length)
const SUFFIX = /^(jr|sr|ii|iii|iv)\.?$/i
// family name for author checks and queries: team.json "family_name", else the last word of "name" ("surname" is the
// lens label and may read "N. Higham" when two members share a family name)
function fam(m) { if (m.family_name) return m.family_name; const w = String(m.name).trim().split(/\s+/).filter(x => !SUFFIX.test(x)); return w.length ? w[w.length - 1] : m.name }

const HOUSE = `House rules for every agent in this workflow (nuwa research-team kit):
- Read ${TEAM}/team.json first: it gives the team's field, "language", the field-wide "chase_hints" (legitimate open repositories of this field) and each member's entry (name, surname, hint, homepage, member "chase_hints"). The member entry there is authoritative if it differs from what this prompt repeats.
- Evidence: never write a bibliographic fact or an abstract from memory. An abstract you record is copied verbatim from a page you fetched in this run, with its URL. If you did not find something, say "not found"; never guess.
- Sources: public and legitimate only. Forbidden: Sci-Hub, LibGen, Z-Library, Anna's Archive or any other shadow library; any paywall circumvention (no cookie/referrer tricks, no institutional proxies); ResearchGate, Academia.edu or any site behind a login; anything that needs credentials.
- Privacy: never open, read, quote or copy anything under a references/sources/private/ folder. Never send the user's email address or any other personal identifier to an external service; where an API insists on an email parameter (Unpaywall) use ${NOREPLY}.
- Tools: WebSearch has a per-session budget (about 200 calls, shared with every other agent in this session) — go to known repositories with curl or WebFetch first and keep WebSearch for the hard cases. export.arxiv.org rejects cloud IPs (HTTP 406): use arxiv.org/search HTML pages. Some old report servers answer only over http://. PostScript files convert with ps2pdf (ghostscript). Kill background processes by exact PID, never with pkill -f (its pattern matches your own shell).
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCRATCH}/chase/. Do not touch other members' folders, the repo's root SKILL.md, references/ or scripts/, and do not git commit or push: the session that launched this workflow commits after the stage. PDFs and txt/ are git-ignored (copyright) and must stay that way.`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A(): opts.phase and opts.label are required')
  return agent(`${HOUSE}\n\n${prompt}`, opts)
}

const dirs = m => {
  const MD = `${TEAM}/${m.slug}`
  return { MD, PUB: `${MD}/references/sources/publications`, PAPERS: `${MD}/references/sources/papers`, CHUNKFILE: `${SCRATCH}/chase/${m.slug}.json` }
}
const hintList = m => (Array.isArray(m.chase_hints) && m.chase_hints.length ? m.chase_hints.map(h => `"${h}"`).join('; ') : 'none in team.json for this member')

const PLAN = {
  type: 'object',
  properties: {
    chunk_file: { type: 'string' },
    works: { type: 'number' },
    chunks: { type: 'number' },
    books: { type: 'number' },
    next_run: { type: 'number' },
    excluded: { type: 'array', items: { type: 'object', properties: { reason: { type: 'string' }, count: { type: 'number' } }, required: ['reason', 'count'] } },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['chunk_file', 'works', 'chunks', 'books', 'next_run', 'excluded', 'problems'],
}
const CHASE = {
  type: 'object',
  properties: {
    found: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, url: { type: 'string' }, file: { type: 'string' }, version: { type: 'string' } }, required: ['id', 'url', 'file'] } },
    not_found: { type: 'array', items: { type: 'string' } },
    abstracts_added: { type: 'number' },
    abstract_file: { type: 'string' },
    rejected: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, url: { type: 'string' }, reason: { type: 'string' } }, required: ['id', 'reason'] } },
    book_leads: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, part: { type: 'string' }, url: { type: 'string' } }, required: ['id', 'part', 'url'] } },
    searches_used: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['found', 'not_found', 'abstracts_added', 'rejected', 'book_leads', 'searches_used', 'notes'],
}
const MERGE = {
  type: 'object',
  properties: {
    urls_recorded: { type: 'number' },
    abstracts_merged: { type: 'number' },
    new_full_texts: { type: 'array', items: { type: 'string' } },
    still_no_oa: { type: 'number' },
    rejected_by_acquire: { type: 'array', items: { type: 'string' } },
    merge_chase: { type: 'string' },
    validate_works: { type: 'string' },
    book_leads_file: { type: 'string' },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['urls_recorded', 'abstracts_merged', 'new_full_texts', 'still_no_oa', 'merge_chase', 'validate_works', 'problems'],
}

function planPrompt(m) {
  const { MD, CHUNKFILE } = dirs(m)
  const skip = Array.isArray(SKIP_IDS[m.slug]) ? SKIP_IDS[m.slug] : []
  return `Task (T3.3 chase, planning) for ${m.name}: build the list of works to chase. Do not search or download anything in this step.
Run exactly this (it selects the no-oa works from INDEX.md and works.json, computes each work's exact target PDF path, splits them into chunks of ${CHUNK} with books last, writes the chunk file and picks the next abstracts-chase run number for ${DATE}):
  python3 ${REPO}/scripts/chase_chunks.py ${MD} --out ${CHUNKFILE} --date ${DATE} --chunk-size ${CHUNK}${skip.length ? ` --skip-ids ${skip.join(',')}` : ''}
It prints one JSON line {"chunk_file", "works", "chunks", "books", "next_run", "excluded": [{"reason", "count"}], "problems": [...]}; return those fields as they are (exit code 1 means problems, e.g. acquire_fulltexts.py has not run on the current works.json: then chunks is 0). If the script is missing or crashes, say so in problems and return chunks 0. Edit nothing in the repo.`
}

function chasePrompt(m, i, n, run, search) {
  const { PAPERS, CHUNKFILE } = dirs(m)
  const absFile = `${PAPERS}/abstracts-chase-${DATE}-r${run}-${i + 1}.json`
  return `Task (T3.3 chase, chunk ${i + 1} of ${n}): find LEGITIMATE open-access full texts for works by ${m.name} (${m.hint || 'see team.json'}) that the automatic pass (arXiv by id, title and author listing; Unpaywall; URLs already in works.json) could not find. If no full text exists, find at least a genuine abstract.
Your works: python3 -c "import json;[print(json.dumps(w, ensure_ascii=False)) for w in json.load(open('${CHUNKFILE}'))[${i}]]"

Where to look, in this order:
1. This member's leads (team.json member "chase_hints"): ${hintList(m)}. Field-wide leads: the "chase_hints" list at the top of team.json.
2. The researcher's own and coauthors' homepages${m.homepage ? ` (start with ${m.homepage})` : ''} and CV publication pages; university and institutional repositories; department technical-report series; arXiv (arxiv.org/search HTML); HAL; CiteSeerX; OSTI, DTIC and NASA report servers; free conference proceedings; publisher open-access versions (the DOI landing page's own free PDF link); Semantic Scholar and CORE open PDFs; Unpaywall (https://api.unpaywall.org/v2/<doi>?email=${NOREPLY}, OA locations only).
Use curl against those sites first; use WebSearch ("<exact title>" ${fam(m)} pdf) only when the direct routes fail. WebSearch allowance for this whole chunk: ${search > 0 ? `at most ${search} call(s)` : 'none (its share of args.search_budget is 0): curl and WebFetch only'}, and at most ${MAXS} search attempts per work; move on when nothing turns up. Report your WebSearch calls in searches_used.

For each work:
1. Download a candidate to the EXACT target path given for it: curl -sL -A "Mozilla/5.0" --max-time 90 -o <target> "<url>". It must be a PDF (head -c4 <target> prints %PDF). A PostScript file (%!PS): save it under ${SCRATCH}/chase/, convert with ps2pdf, move the PDF to the target. HTML or a login page: delete it.
2. Verify it is THIS paper by THIS author: python3 -c "import pypdfium2 as p; d=p.PdfDocument('<target>'); print(d[0].get_textpage().get_text_range()[:900])" (pip install pypdfium2 pillow if missing) must show the title, or clearly the same work (a technical-report or preprint version with the same title is fine: say which in "version"), AND ${m.name} (family name ${fam(m)}) among the authors on page 1. Report series and repositories hold other people's reports with similar titles, so a title match alone is not enough. A scan with no text layer: check the first page image or the repository metadata, keep it (acquisition will OCR it) and say so. Delete every wrong file and list it under "rejected".
3. No PDF, but a genuine abstract on a legitimate page (publisher landing page, Crossref, DBLP, a repository record): add it to ${absFile} — one JSON object for this chunk, keyed by work id, with the verbatim abstract as the value and "<id>__src" = the page URL (json.dump(obj, f, ensure_ascii=False, indent=1)). The keys are only the "id" values of YOUR chunk list, exactly as written there (never a DOI, a title or an id you made up): scripts/merge_chase.py keeps back a whole file that holds an id missing from works.json / INDEX.md. Create the file when you write your first abstract; if a file of that name already exists before you start (an earlier run), do not overwrite it: use the same name with -b, -c, … before .json. Report the file you wrote in abstract_file. Copy, never paraphrase; skip abstracts that are cut off mid-sentence unless the page shows no more.
4. Books (kind book): the body is rarely open. Never fetch a book body from anywhere except the publisher or the authors offering it openly. List the legitimately open parts you find (table of contents, preface or front matter, errata, addenda, published reviews) under "book_leads" with URLs; a later increment step reads them.

Write nothing else: not works.json, not INDEX.md, not abstracts.json (the merge step records your URLs and runs the scripts). Report found (id, url, file, version), not_found ids, rejected downloads, abstracts added, book leads, and roughly how many searches you used.`
}

function mergePrompt(m, chunks) {
  const { MD, PUB, PAPERS } = dirs(m)
  const found = chunks.flatMap(c => c.found)
  const leads = chunks.flatMap(c => c.book_leads || [])
  const absFiles = chunks.map(c => c.abstract_file).filter(Boolean)
  return `Task (T3.3 chase, merge) for ${m.name}. The chase agents finished (${chunks.length} chunk reports). They found these files: ${JSON.stringify(found)}; they wrote abstracts to ${PAPERS}/abstracts-chase-*.json (${chunks.reduce((s, c) => s + (c.abstracts_added || 0), 0)} reported${absFiles.length ? `; files named: ${absFiles.join(', ')}` : ''}).
1. For each found item: check the file exists at its path and starts with %PDF. Then add its URL to that work's "urls" list in ${PUB}/works.json if it is not there yet (change nothing else; json.dump(..., ensure_ascii=False, indent=1)). The URL tells the index where the copy came from.
2. Run python3 ${REPO}/scripts/validate_works.py ${PUB}/works.json and fix any error you introduced (0 errors).
3. Run python3 ${REPO}/scripts/merge_chase.py ${MD} in the background with OMP_THREAD_LIMIT=1 and output to ${SCRATCH}/chase/${m.slug}-merge.log. It merges the abstracts-chase files into abstracts.json / abstract-sources.json (never overwriting an existing abstract), then re-runs scripts/acquire_fulltexts.py, which indexes the new PDFs, extracts their text and OCRs scans. Poll the log until it exits; if it hangs for more than 15 minutes on one work, kill it by exact PID and report. If merge_chase.py reports a malformed chunk file, fix the JSON syntax (not the content) and run it again. If it keeps a file back because of an id that is not in works.json / INDEX.md, look the work up by its title in works.json: rename the key to the right id when the match is certain, otherwise delete that entry (and its __src) and name it in problems; then run it again.
4. From its output and ${PAPERS}/INDEX.md: the ids that now have "txt"; files acquisition rejected as mismatches (delete those PDFs); how many selected works are still "no-oa".
${leads.length ? `5. Book leads: the chase agents found openly available parts of books: ${JSON.stringify(leads)}. Merge them into ${PAPERS}/book-leads.json, a JSON object {"<work id>": [{"part": "...", "url": "..."}]} (create it if missing; keep existing entries; no duplicate URL per id; json.dump(..., ensure_ascii=False, indent=1)), and report its path in book_leads_file. team-increment.js (find: ["book-parts"]) starts from this file.
` : ''}Edit only works.json ("urls" lists)${leads.length ? ', papers/book-leads.json' : ''} and, when merge_chase.py keeps one back, a papers/abstracts-chase-*.json file (its JSON syntax, or a key as described above; never an abstract's text); the scripts write INDEX.md, abstracts.json and abstract-sources.json.`
}

phase('Plan')
if (!DO_MERGE) log('args.merge is false: abstracts-chase-*.json stay unmerged and new PDFs unindexed until you run python3 scripts/merge_chase.py <member dir>')

const results = await pipeline(
  MEMBERS,
  // the runtime ends an item's pipeline when a stage returns null, so a dead planning agent is reported here
  m => A(planPrompt(m), { label: `chase-plan:${m.slug}`, phase: 'Plan', schema: PLAN, effort: 'low' }).then(plan => {
    if (!plan) log(`${m.slug}: planning agent returned nothing; member skipped`)
    return plan
  }),
  (plan, m) => {
    if (!plan) { log(`${m.slug}: planning agent returned nothing; member skipped`); return null }
    const ex = plan.excluded.filter(e => e.count > 0).map(e => `${e.count} ${e.reason}`).join(', ')
    if (ex) log(`${m.slug}: not chased — ${ex}`)
    if (plan.problems.length) log(`${m.slug}: planning problems — ${plan.problems.join('; ')}`)
    if (!plan.chunks) { log(`${m.slug}: nothing to chase (${plan.works} works)`); return { plan, chunks: [] } }
    const run = Number.isInteger(plan.next_run) && plan.next_run > 0 ? plan.next_run : 1
    if (run !== plan.next_run) log(`${m.slug}: planning agent gave no usable next_run (${plan.next_run}); using r1 (chase agents still never overwrite an existing abstracts file)`)
    else if (run > 1) log(`${m.slug}: abstracts-chase files of earlier runs today exist; this run writes abstracts-chase-${DATE}-r${run}-<chunk>.json`)
    const only = Array.isArray(ONLY[m.slug]) ? ONLY[m.slug].filter(k => Number.isInteger(k) && k >= 1 && k <= plan.chunks) : null
    const idx = Array.from({ length: plan.chunks }, (_, i) => i).filter(i => !only || only.includes(i + 1))
    if (only) log(`${m.slug}: running chunks ${idx.map(i => i + 1).join(', ')} of ${plan.chunks}; the other chunks are skipped (args.only_chunks)`)
    const per = idx.length ? Math.floor(SHARE / idx.length) : 0
    log(`${m.slug}: WebSearch allowance ${per} per chunk agent (${SHARE} for this member; args.search_budget)`)
    return parallel(idx.map(i => () => A(chasePrompt(m, i, plan.chunks, run, per), { label: `chase:${m.slug}:${i + 1}`, phase: 'Chase', schema: CHASE })))
      .then(rs => {
        const failed = idx.filter((_, k) => !rs[k]).map(i => i + 1)
        if (failed.length) log(`${m.slug}: chase chunk(s) ${failed.join(', ')} returned nothing; their works were not chased (rerun with args.only_chunks)`)
        return { plan, chunks: rs.filter(Boolean) }
      })
  },
  (r, m) => {
    if (!r) return null
    const nFound = r.chunks.reduce((s, c) => s + c.found.length, 0)
    const nAbs = r.chunks.reduce((s, c) => s + (c.abstracts_added || 0), 0)
    const nLeads = r.chunks.reduce((s, c) => s + (c.book_leads || []).length, 0)
    log(`${m.slug}: chase found ${nFound} full texts, ${nAbs} abstracts and ${nLeads} book lead(s); ${r.chunks.reduce((s, c) => s + (c.searches_used || 0), 0)} WebSearch call(s)`)
    if (!DO_MERGE || (!nFound && !nAbs && !nLeads)) return { ...r, merge: null }
    return A(mergePrompt(m, r.chunks), { label: `chase-merge:${m.slug}`, phase: 'Merge', schema: MERGE }).then(mg => {
      if (!mg) log(`${m.slug}: merge agent returned nothing; run python3 scripts/merge_chase.py by hand`)
      return { ...r, merge: mg }
    })
  },
)

const out = MEMBERS.map((m, i) => {
  const r = results[i]
  if (!r) return { member: m.slug, error: 'no result (see log)' }
  return {
    member: m.slug,
    planned_works: r.plan.works,
    chunks: r.plan.chunks,
    found: r.chunks.flatMap(c => c.found),
    not_found: r.chunks.flatMap(c => c.not_found),
    rejected: r.chunks.flatMap(c => c.rejected),
    abstracts_added: r.chunks.reduce((s, c) => s + (c.abstracts_added || 0), 0),
    book_leads: r.chunks.flatMap(c => c.book_leads),
    searches_used: r.chunks.reduce((s, c) => s + (c.searches_used || 0), 0),
    merge: r.merge,
  }
})
const searches = out.reduce((s, r) => s + (r.searches_used || 0), 0)
log(`WebSearch calls reported by the chase agents: ${searches} (budget ${BUDGET})`)
const unmerged = out.filter(r => !r.error && !r.merge && (r.found.length || r.abstracts_added)).map(r => r.member)
return {
  stage: 'T3.3 chase',
  date: DATE,
  search_budget: BUDGET,
  searches_used: searches,
  members: out,
  next: [
    unmerged.length ? `Not merged yet (${DO_MERGE ? 'the merge agent returned nothing' : 'args.merge is false'}): python3 scripts/merge_chase.py ${TEAM_REL}/<slug> for ${unmerged.join(', ')}.` : 'Chase output merged (abstracts.json, INDEX.md, works.json urls).',
    `Commit each member: bash scripts/team_commit.sh ${TEAM_REL}/<slug> "chase(<slug>): open copies and abstracts" (PDFs stay out of git; book-leads.json is committed).`,
    `Then plan the first reading round: python3 scripts/plan_reading_batches.py ${TEAM_REL} --out-dir ${SCRATCH} --no-abstract, and run team-read.js per member with round: 1.`,
  ],
}
