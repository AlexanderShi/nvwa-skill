export const meta = {
  name: 'team-harvest',
  description: 'T3.1: build each member\'s complete publication list (Google Scholar via WebFetch + DBLP SPARQL + Crossref) into works.json + scholar.md, then an independent audit',
  whenToUse: 'Deep tier of a nuwa research team, after T1/T2: before acquire_fulltexts.py. One agent chain per member; run one workflow per member in parallel on small machines.',
  phases: [
    { title: 'Harvest', detail: 'per member: Scholar pages via WebFetch, DBLP via SPARQL, Crossref DOI fill -> works.json + scholar.md, validate_works.py' },
    { title: 'Audit', detail: 'per member: independent year-sorted Scholar pass, DOI/arXiv spot checks, validate_works.py, RESOURCES.md row' },
    { title: 'Acquire', detail: 'optional (args.acquire): run acquire_fulltexts.py and report the full-text index' },
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
//   args.request  optional: the user's request in their own words; opens every agent prompt (set with make_args.mjs --request)
// Workflow-specific keys:
//   args.audit    default true; false skips the independent audit (logged; not recommended)
//   args.acquire  default false; true adds a stage in which an agent runs scripts/acquire_fulltexts.py in the
//                 background and polls it (long: arXiv delay 3 s per work plus downloads and OCR). The proven path is
//                 to leave it false and run acquire_fulltexts.py from the main session (one background process per member).
//   args.search_budget  WebSearch calls this run may use in total (default 2 per member: 1 harvest, 1 audit). Scholar is
//                 read with WebFetch and DBLP/Crossref with curl, which do not count; the session has about 200 WebSearch
//                 calls shared by every agent (playbook §六).
// Outputs per member (<repo>/<team>/<slug>/references/sources/):
//   publications/works.json, publications/scholar.md, row 1 of RESOURCES.md rewritten completely (its template TODO
//   resolved: the list actually used, the counts, the audit date; grep shows no [TODO or {{ left in row 1);
//   with args.acquire also papers/INDEX.md, papers/abstracts.json (+ git-ignored PDFs and txt/)
// Gates run by the agents: scripts/validate_works.py (0 errors); scripts/dblp_works.py for DBLP.
// Next steps (outside this workflow; the return value's "next" lists them): record the Scholar id / DBLP pid the agents
//   found in team.json (new_team.py --set-member), validate_works.py, acquire_fulltexts.py (unless args.acquire), team-chase.js.
// Launch: Workflow({scriptPath: "<repo>/scripts/workflows/team-harvest.js", args: {...}}).
// Cost baseline (DFO worked example, product/dfo-team/): ~3 agents and ~0.4M tokens per member.
// ---------------------------------------------------------------------------------------------

const ARGS = typeof args === 'string' ? JSON.parse(args) : args
function need(ok, msg) { if (!ok) throw new Error(`team-harvest args: ${msg}`) }
need(ARGS && typeof ARGS === 'object', 'pass args as a JSON object')
need(typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'), 'args.repo must be an absolute path')
need(typeof ARGS.team === 'string' && ARGS.team.length > 0 && !ARGS.team.startsWith('/'), 'args.team must be relative to args.repo, e.g. "product/<team>"')
need(typeof ARGS.scratch === 'string' && ARGS.scratch.startsWith('/'), 'args.scratch must be an absolute path')
need(/^\d{4}-\d{2}-\d{2}$/.test(ARGS.date || ''), 'args.date must be "YYYY-MM-DD"')
need(Array.isArray(ARGS.members) && ARGS.members.length > 0, 'args.members must be a non-empty array copied from team.json')
ARGS.members.forEach((m, i) => need(m && /^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') && m.name, `args.members[${i}] needs a kebab-case slug and a name`))
// args keys this workflow reads (all snake_case, like every team workflow); anything else is logged
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'request', 'audit', 'acquire', 'search_budget']
const unknownArgs = Object.keys(ARGS).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-harvest.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)
// args.request (optional): the user's request in their own words. Workflow agents see only their prompt and the
// user's latest message in the launching session; when that message is a side question they may decline the step,
// so A() opens every prompt with the request.
const REQUEST = typeof ARGS.request === 'string' ? ARGS.request.replace(/\s+/g, ' ').trim() : ''
if (ARGS.request !== undefined && ARGS.request !== null && typeof ARGS.request !== 'string') log(`team-harvest.js: args.request must be a string (the user's request in their own words), got ${Array.isArray(ARGS.request) ? 'array' : typeof ARGS.request}; ignored`)
const WHY = REQUEST ? `Why this agent runs: in the session that launched this workflow the user asked: "${REQUEST}". This agent is one step of that work (research-team kit, team-harvest.js, stage T3.1). Do the step below.\n\n` : ''

const REPO = ARGS.repo.replace(/\/+$/, '')
const TEAM_REL = ARGS.team.replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCRATCH = ARGS.scratch.replace(/\/+$/, '')
const DATE = ARGS.date
const MEMBERS = ARGS.members
const DO_AUDIT = ARGS.audit !== false
const DO_ACQUIRE = ARGS.acquire === true
const NOREPLY = 'nuwa-skill@users.noreply.github.com'
const BUDGET = Number.isInteger(ARGS.search_budget) && ARGS.search_budget >= 0 ? ARGS.search_budget : 2 * MEMBERS.length
const SHARE = Math.floor(BUDGET / MEMBERS.length)
const HARVEST_SEARCH = Math.ceil(SHARE / 2)
const AUDIT_SEARCH = SHARE - HARVEST_SEARCH
const SUFFIX = /^(jr|sr|ii|iii|iv)\.?$/i
// family name for author checks and queries: team.json "family_name", else the last word of "name" ("surname" is the
// lens label and may read "N. Higham" when two members share a family name)
function fam(m) { if (m.family_name) return m.family_name; const w = String(m.name).trim().split(/\s+/).filter(x => !SUFFIX.test(x)); return w.length ? w[w.length - 1] : m.name }
function searchLine(n) { return `WebSearch allowance for this task: ${n > 0 ? `at most ${n} call(s)` : 'none (use WebFetch and curl only)'}; report the number in searches_used.` }

const HOUSE = `House rules for every agent in this workflow (nuwa research-team kit):
- Read ${TEAM}/team.json first: it gives the team's field, "language", the field-wide "chase_hints" and each member's entry (name, surname, living, hint, scholar, dblp, orcid, homepage, chase_hints, student_mode). The member entry there is authoritative if it differs from what this prompt repeats.
- Evidence: never write a bibliographic fact from memory. Every DOI, arXiv id, venue and year you record comes from a page or API response you fetched in this run. If you could not check something, leave the field null and say so in your report instead of guessing.
- Sources: public and legitimate only. Never Sci-Hub, LibGen, Z-Library or other shadow libraries, never paywall circumvention, never scraping behind a login.
- Privacy: never open, read, quote or copy anything under a references/sources/private/ folder. Never send the user's email address or any other personal identifier to an external service. Crossref and DBLP requests carry no email at all; where an API insists on one (Unpaywall) use ${NOREPLY}.
- Tools: Google Scholar has no API and blocks curl, so read it only with WebFetch (load it with ToolSearch "select:WebFetch,WebSearch" if it is not loaded). The dblp.org search/pid REST API sits behind a bot wall, so use its SPARQL endpoint. export.arxiv.org rejects cloud IPs (HTTP 406): use the arxiv.org/search HTML pages. OpenAlex rate-limits shared cloud IPs (HTTP 429) unless OPENALEX_API_KEY is set. WebSearch has a per-session budget (about 200 calls): prefer curl or WebFetch against known URLs. Kill background processes by exact PID, never with pkill -f.
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCRATCH}/harvest/<member-slug>/. Do not touch other members' folders, the repo's root SKILL.md, references/ or scripts/, and do not git commit or push: the session that launched this workflow commits after the stage.`

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A(): opts.phase and opts.label are required')
  return agent(`${WHY}${HOUSE}\n\n${prompt}`, opts)
}

function who(m) {
  const bits = []
  if (m.hint) bits.push(`hint: ${m.hint}`)
  bits.push(m.living === false ? 'deceased' : 'living')
  if (m.scholar) bits.push(`Google Scholar user id ${m.scholar}`)
  if (m.dblp) bits.push(`DBLP pid ${m.dblp}`)
  if (m.orcid) bits.push(`ORCID ${m.orcid}`)
  if (m.homepage) bits.push(`homepage ${m.homepage}`)
  return `${m.name} (${bits.join('; ')})`
}
const dirs = m => {
  const MD = `${TEAM}/${m.slug}`
  return { MD, SRC: `${MD}/references/sources`, PUB: `${MD}/references/sources/publications`, PAPERS: `${MD}/references/sources/papers`, SCR: `${SCRATCH}/harvest/${m.slug}` }
}

const SCHOLAR_ROW_PROMPT = 'Return EVERY article row on this page as JSON lines, one per row, in page order, with keys: title, authors, venue, year, cites. Copy text exactly as shown (keep the \'...\' if the author list is truncated). Use null for missing fields. After the rows, on the last line, write TOTAL=<number of rows on this page>. Do not summarise, skip or merge rows.'
const AUDIT_ROW_PROMPT = 'Return EVERY article row on this page as JSON lines, one per row, in page order, with keys: title, year. Copy text exactly as shown. Use null for missing fields. After the rows, on the last line, write TOTAL=<number of rows on this page>. Do not summarise, skip or merge rows.'

const HARVEST = {
  type: 'object',
  properties: {
    researcher: { type: 'string' },
    scholar_user: { type: 'string' },
    identity_confirmed: { type: 'boolean' },
    identity_evidence: { type: 'string' },
    scholar_rows: { type: 'number' },
    pages_fetched: { type: 'number' },
    pages_refetched_at_20: { type: 'number' },
    dblp_pid: { type: 'string' },
    dblp_records: { type: 'number' },
    dblp_only_items: { type: 'number' },
    homepage_only_items: { type: 'number' },
    duplicates_marked: { type: 'number' },
    with_doi: { type: 'number' },
    with_arxiv: { type: 'number' },
    validate_works: { type: 'string' },
    problems: { type: 'array', items: { type: 'string' } },
    output_files: { type: 'array', items: { type: 'string' } },
    searches_used: { type: 'number' },
  },
  required: ['researcher', 'scholar_user', 'identity_confirmed', 'identity_evidence', 'scholar_rows', 'pages_fetched', 'dblp_pid', 'dblp_only_items', 'with_doi', 'with_arxiv', 'validate_works', 'problems', 'output_files'],
}
const AUDIT = {
  type: 'object',
  properties: {
    researcher: { type: 'string' },
    complete: { type: 'boolean' },
    scholar_rows_seen: { type: 'number' },
    missing_found: { type: 'number' },
    fixes_applied: { type: 'array', items: { type: 'string' } },
    dois_checked: { type: 'number' },
    dois_nulled: { type: 'number' },
    arxiv_checked: { type: 'number' },
    arxiv_nulled: { type: 'number' },
    validate_works: { type: 'string' },
    resources_row_updated: { type: 'boolean' },
    remaining_concerns: { type: 'array', items: { type: 'string' } },
    searches_used: { type: 'number' },
  },
  required: ['researcher', 'complete', 'scholar_rows_seen', 'missing_found', 'fixes_applied', 'dois_checked', 'dois_nulled', 'arxiv_checked', 'arxiv_nulled', 'validate_works', 'resources_row_updated', 'remaining_concerns'],
}
const ACQ = {
  type: 'object',
  properties: {
    researcher: { type: 'string' },
    finished: { type: 'boolean' },
    indexed: { type: 'number' },
    txt: { type: 'number' },
    pdf_only: { type: 'number' },
    no_oa: { type: 'number' },
    mismatches: { type: 'number' },
    ocr_used: { type: 'number' },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['researcher', 'finished', 'indexed', 'txt', 'no_oa', 'problems'],
}

function harvestPrompt(m) {
  const { MD, PUB, SCR } = dirs(m)
  const scholarStep = m.scholar
    ? `Scholar profile id: ${m.scholar}.`
    : `team.json has no Scholar id for this member. Find the profile first: WebFetch https://scholar.google.com/citations?view_op=search_authors&mauthors=${encodeURIComponent(m.name)}&hl=en and pick the profile whose affiliation and topics match the hint. Report the id you used in "scholar_user" (the user adds it to team.json; you do not edit team.json). If there is no matching profile, say so, skip to Step 2 and make DBLP (plus the homepage list, and OpenAlex via python3 ${REPO}/scripts/fetch_publications.py "${m.name}" --json --out ${SCR} only when OPENALEX_API_KEY is set; never pass --mailto) the primary list, with ids D### / H###.`
  return `Task (T3.1 harvest): build the COMPLETE publication list of ${who(m)} for the research-craft skill at ${MD}/.
The deep tier reads "all of the researcher's articles on Google Scholar", so the Google Scholar profile is the primary list when there is one; DBLP, Crossref, arXiv and the homepage cross-check it and fill identifiers. Without a Scholar profile, DBLP plus the homepage list is the primary list.
${searchLine(HARVEST_SEARCH)}
Outputs: ${PUB}/works.json and ${PUB}/scholar.md (create the folder if missing). Scratch: ${SCR}/ (save every raw page you fetch there, e.g. scholar-cstart-0.jsonl, so the audit trail survives).

Re-run rule: if ${PUB}/works.json already exists, keep every existing id and record (other files such as papers/INDEX.md and paper cards refer to the ids). Add new rows with new ids after the highest existing number of that letter, fix fields only with evidence, and never renumber.

## Step 1 — Google Scholar (primary)
${scholarStep}
Fetch https://scholar.google.com/citations?user=<id>&hl=en&cstart=N&pagesize=50 for N = 0, 50, 100, … until a page returns no rows (a page with fewer than 50 rows is the last one).
Use this WebFetch prompt, verbatim, for every page:
"${SCHOLAR_ROW_PROMPT}"
If a page's TOTAL is 50, fetch the next page. If a page looks truncated, or the number of JSON lines disagrees with TOTAL, refetch that range with pagesize=20 (cstart=N, N+20, N+40) and use the pagesize=20 rows.
Confirm the profile identity on page 1 (name, affiliation, topics must match the hint: ${m.hint || 'see team.json'}); report the evidence. Scholar sometimes takes a year from a publisher's online-deposit date; do not "fix" years here, the audit does that when two sources agree.

## Step 2 — DBLP (DOIs, arXiv ids, items Scholar misses)
Run python3 ${REPO}/scripts/dblp_works.py --name "${m.name}" to list candidate persons${m.dblp ? ` (team.json already gives pid ${m.dblp}; confirm it)` : ''}; choose the pid whose notes/affiliations match the hint, then python3 ${REPO}/scripts/dblp_works.py --pid <pid> --out ${SCR}/dblp.json.
If the script is missing or fails, query https://sparql.dblp.org/sparql yourself (POST query=<SPARQL>, header Accept: application/sparql-results+json, a normal curl User-Agent). Do not use the dblp.org search or pid REST URLs (bot wall).
Match DBLP records to Scholar rows by normalised title (lowercase, alphanumerics only; Python difflib ratio >= 0.9) and fill doi / arxiv / urls (DBLP "ee" links). A journal version plus its CoRR/arXiv version is ONE item that keeps both ids. DBLP records with no Scholar match become extra items (ids D###, sources ["dblp"]). A researcher without a DBLP entry is normal in some fields: say so and continue.

## Step 3 — Crossref and arXiv fill
For Scholar items still lacking a DOI that look like journal or proceedings papers:
curl -s "https://api.crossref.org/works?query.bibliographic=<url-encoded title>&query.author=${encodeURIComponent(fam(m))}&rows=3&select=DOI,title,container-title,issued" — accept only if the normalised title ratio >= 0.9 and the year is within 1. Sleep 1 s between calls. No email parameter, no mailto header.
arXiv ids: from DBLP CoRR records ("abs/…"), from DataCite (arXiv DOIs look like 10.48550/arXiv.<id>), or from https://arxiv.org/search/?query=<title>&searchtype=title (HTML); accept only on a title ratio >= 0.9 with ${m.name} (family name ${fam(m)}) among the authors.
${m.homepage ? `\n## Step 4 — Homepage\nIf ${m.homepage} (or pages it links to) has a publication list, cross-check it: fill urls (preprint/PDF links are valuable later) and add homepage-only research items as H### (sources ["homepage"]).\n` : ''}
## Output
Write ${PUB}/works.json (UTF-8, json.dump(..., ensure_ascii=False, indent=1)) exactly in this shape:
{"researcher": "${m.name}", "scholar_user": "<id or empty>", "harvested": "${DATE}", "source_note": "<with a Scholar profile: Google Scholar profile + DBLP + Crossref (+ homepage); without one: DBLP + homepage + Crossref (no Google Scholar profile)>",
 "works": [ {"id": "S001", "title": ..., "authors": ..., "venue": ..., "year": <int or null>, "cites": <int or null>,
             "doi": <"10.xxxx/..." or null>, "arxiv": <"2101.01234" or "math/0501001" or null>, "urls": [<landing/PDF urls from DBLP ee, homepage, repositories>],
             "kind": "journal|conference|book|chapter|thesis|report|preprint|patent|talk|other", "dup_of": <id or null>, "sources": ["scholar", "dblp", "crossref", ...] } ... ]}
Ids: S### in Scholar order (citation order as fetched); D### for DBLP-only items; H### for homepage-only items. Never delete a row: mark duplicates (the same paper listed twice on Scholar, a preprint row next to its journal row) and junk rows (a journal or proceedings name, a report number, a scanned title page, a publisher advert) with dup_of = the id of the real work they belong to. A junk row that belongs to no listed work keeps dup_of null, gets kind "other", and is named in your report.
Write ${PUB}/scholar.md: a title line "# <name> — publication list (Google Scholar primary)" (without a Scholar profile: "# <name> — publication list (DBLP and homepage; no Google Scholar profile)"), a header paragraph (harvest date ${DATE}, profile URL, counts: Scholar rows, pages, DBLP-only and homepage-only items, duplicates marked, distinct works listed, how many have a DOI / an arXiv id, the DBLP pid), the profile identity line (affiliation, interests as shown), then a markdown table (#, Year, Title, Venue, Cites, DOI, arXiv, Kind) of all works with dup_of null, sorted by citations (items without citations last). Say "Full records incl. duplicates: works.json".

## Gate
Run python3 ${REPO}/scripts/validate_works.py ${PUB}/works.json and fix every error it reports. Read its warnings too: link near-duplicates with dup_of only when they are the same work in the same form (a conference and a journal version, or a report and its published version, are separate works unless Scholar lists one paper twice). If the script does not exist yet, check by hand: unique ids, required keys, dup_of targets exist, year int or null, DOI starts with "10.", urls is a list; say so in validate_works.
Edit only ${PUB}/works.json and ${PUB}/scholar.md. Report the counts; list every problem honestly (pages that failed, identity doubts, rows you could not parse, DBLP persons you could not disambiguate).`
}

function auditPrompt(m, h) {
  const { MD, SRC, PUB, SCR } = dirs(m)
  return `Task (T3.1 audit): independently audit the publication harvest for ${who(m)} in ${PUB}/works.json and scholar.md (written by another agent; its report: ${JSON.stringify(h)}).
Goal: works.json must contain ALL of the researcher's articles on the Google Scholar profile (or, when the researcher has no Scholar profile, every DBLP record and every research item of the homepage/CV list), with correct identifiers. Assume rows were missed until you have shown otherwise.
${searchLine(AUDIT_SEARCH)}
1. Independently fetch the profile sorted by YEAR (a different order catches rows the citation-order pass dropped): https://scholar.google.com/citations?user=${h && h.scholar_user ? h.scholar_user : (m.scholar || '<id from works.json "scholar_user">')}&hl=en&view_op=list_works&sortby=pubdate&cstart=N&pagesize=50 for N = 0, 50, … with this WebFetch prompt, verbatim:
   "${AUDIT_ROW_PROMPT}"
   Same refetch rule: when a page looks truncated or the line count disagrees with TOTAL, refetch that range with pagesize=20. Save raw pages to ${SCR}/audit-cstart-N.jsonl. (No Scholar profile: audit against DBLP and the homepage list instead and say so.)
2. Compare with works.json by normalised title (Python difflib ratio >= 0.9). Any profile row missing from works.json: append it with the next unused S number (never reuse or renumber ids), same schema, sources ["scholar"]; fill doi/arxiv the same way the harvest did (Crossref without email, DBLP via python3 ${REPO}/scripts/dblp_works.py or sparql.dblp.org). Fix a wrong year or venue only when two independent sources agree (Scholar often shows a publisher's online-deposit year); list each fix.
3. Spot-check identifiers: at least 10 DOIs chosen across the list (curl -s -o /dev/null -w "%{http_code}" https://doi.org/<doi> must be 30x, and the Crossref record's title must match: https://api.crossref.org/works/<doi>) and at least 5 arXiv ids (https://arxiv.org/abs/<id> title must match). Null out wrong ones and look for the right one once. If more than 2 of the sample are wrong, check ALL identifiers of that kind.
4. Regenerate ${PUB}/scholar.md from the fixed works.json (same table format) and add an audit paragraph under the header: "Audited ${DATE}: an independent year-sorted pass over the profile (<n> rows) …", listing what was added and corrected.
5. Run python3 ${REPO}/scripts/validate_works.py ${PUB}/works.json until it reports 0 errors (if the script is missing, check by hand and say so).
6. In ${SRC}/RESOURCES.md, rewrite row 1 (the publication-list row of the team template; add it as row 1 if absent) completely, removing its [TODO: …] note: Status ✅; Link = the list actually used — the Google Scholar profile URL (https://scholar.google.com/citations?user=<id>&hl=en), or, when the member has no Scholar profile, the DBLP person page (https://dblp.org/pid/<pid>.html) and/or the homepage publication list you used, replacing whatever the cell held; Notes = the counts (Scholar rows, distinct works, DBLP-only and homepage-only works) and "publications/works.json + scholar.md, audited ${DATE}". Keep the row's column count. Change nothing else in RESOURCES.md (other TODO items belong to other steps).
   Check: grep -n '^| 1 |' ${SRC}/RESOURCES.md must print one line that contains neither "[TODO" nor "{{"; set resources_row_updated accordingly.
Edit only ${PUB}/works.json, ${PUB}/scholar.md and that one row of ${SRC}/RESOURCES.md. Report what you fixed and what still worries you.`
}

function acquirePrompt(m, a) {
  const { MD, PAPERS, SCR } = dirs(m)
  return `Task (T3.2 acquisition, run as a script): collect the legitimately open full texts for ${m.name}'s works.
The audited list is ${MD}/references/sources/publications/works.json (audit report: ${JSON.stringify(a)}).
1. Check the tools: python3 -c "import pypdfium2" (else pip install pypdfium2 pillow); which tesseract and which ps2pdf (report if missing: scans then stay unreadable, PostScript reports cannot be converted).
2. Run, in the background with output to ${SCR}/acquire.log:
   OMP_THREAD_LIMIT=1 python3 ${REPO}/scripts/acquire_fulltexts.py ${MD}
   (arXiv by id / title / author listing, Unpaywall with a noreply address, URLs from works.json; it checks each PDF is the paper, OCRs scans and garbled text layers, and writes papers/INDEX.md and abstracts.json). OMP_THREAD_LIMIT=1 matters: multi-threaded tesseract makes a small machine crawl.
3. Poll the log every few minutes until the script exits (it sleeps ~3 s between arXiv requests, so a few hundred works take a while). If it is stuck for more than 15 minutes on one work, kill it by its exact PID (not pkill -f), note the work, and rerun with --only for the remaining ids if needed.
4. From ${PAPERS}/INDEX.md count rows by "Full text" (txt / pdf / no-oa) and report mismatches the script rejected and pages that needed OCR.
Do not edit INDEX.md or works.json by hand. Do not download anything outside what the script fetches.`
}

phase('Harvest')
if (!DO_AUDIT) log('args.audit is false: the independent audit is skipped for every member (misses and wrong identifiers will go unchecked)')
if (!DO_ACQUIRE) log('args.acquire is not true: after this workflow run OMP_THREAD_LIMIT=1 python3 scripts/acquire_fulltexts.py <member dir> from the main session, one background process per member (the proven path), then team-chase.js')
const noScholar = MEMBERS.filter(m => !m.scholar).map(m => m.slug)
if (noScholar.length) log(`no Google Scholar id in team.json for: ${noScholar.join(', ')} — their harvest agents search for a profile first and fall back to DBLP/homepage`)

const results = await pipeline(
  MEMBERS,
  // the runtime ends an item's pipeline when a stage returns null, so a dead harvest agent is reported here
  m => A(harvestPrompt(m), { label: `harvest:${m.slug}`, phase: 'Harvest', schema: HARVEST }).then(h => {
    if (!h) log(`${m.slug}: harvest agent returned nothing; audit and acquisition skipped for this member`)
    return h
  }),
  (h, m) => {
    if (!h) return { harvest: null, audit: null } // defensive: already logged in stage 1
    if (!h.identity_confirmed) log(`${m.slug}: profile identity NOT confirmed (${h.identity_evidence}); check before using the list`)
    if (!DO_AUDIT) return { harvest: h, audit: null }
    return A(auditPrompt(m, h), { label: `audit:${m.slug}`, phase: 'Audit', schema: AUDIT }).then(a => {
      if (!a) log(`${m.slug}: audit agent returned nothing`)
      else if (!a.complete) log(`${m.slug}: audit says the list is still incomplete: ${a.remaining_concerns.join('; ')}`)
      if (a && !a.resources_row_updated) log(`${m.slug}: RESOURCES.md row 1 was not rewritten (its template TODO is still open); fix it by hand`)
      return { harvest: h, audit: a }
    })
  },
  (r, m) => {
    if (!DO_ACQUIRE || !r || !r.harvest) return { ...r, acquire: null }
    return A(acquirePrompt(m, r.audit), { label: `acquire:${m.slug}`, phase: 'Acquire', schema: ACQ }).then(q => {
      if (q && !q.finished) log(`${m.slug}: acquisition did not finish: ${q.problems.join('; ')}`)
      return { ...r, acquire: q }
    })
  },
)

const out = MEMBERS.map((m, i) => ({ member: m.slug, ...(results[i] || { harvest: null, audit: null, acquire: null }) }))
const searches = out.reduce((s, r) => s + ((r.harvest && r.harvest.searches_used) || 0) + ((r.audit && r.audit.searches_used) || 0), 0)
log(`WebSearch calls reported: ${searches} (budget ${BUDGET})`)
// ids the agents found that team.json lacks: one new_team.py --set-member command per member
const setIds = MEMBERS.map((m, i) => {
  const h = out[i].harvest
  if (!h) return null
  const kv = []
  if (!m.scholar && h.scholar_user && /^[\w-]{6,}$/.test(h.scholar_user)) kv.push(`scholar=${h.scholar_user}`)
  if (!m.dblp && h.dblp_pid && /^[\w/-]+$/.test(h.dblp_pid)) kv.push(`dblp=${h.dblp_pid}`)
  return kv.length ? `python3 scripts/new_team.py ${TEAM_REL}/team.json --set-member ${m.slug} ${kv.join(' ')}` : null
}).filter(Boolean)
return {
  stage: 'T3.1 harvest',
  date: DATE,
  search_budget: BUDGET,
  searches_used: searches,
  members: out,
  next: [
    ...(setIds.length ? [`Record the ids the harvest found in team.json (check them against the member's hint first): ${setIds.join(' ; ')}`] : []),
    `Gate: python3 scripts/validate_works.py ${TEAM_REL}/<slug> → 0 errors; the S rows match the Scholar total (no Scholar profile: reconcile with python3 scripts/dblp_works.py --pid <pid> and the CV).`,
    `Commit each member: bash scripts/team_commit.sh ${TEAM_REL}/<slug> "sources(<slug>): publication list".`,
    DO_ACQUIRE ? 'Acquisition ran in this workflow: check INDEX.md rows = distinct works (python3 scripts/team_status.py <team>, column Indexed ✓), then team-chase.js.'
      : `T3.2 from the main session, one background process per member: python3 scripts/acquire_fulltexts.py ${TEAM_REL}/<slug> (playbook §三); then team-chase.js per member.`,
  ],
}
