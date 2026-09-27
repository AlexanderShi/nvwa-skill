export const meta = {
  name: 'team-read',
  description: 'T3.5 deep reading: per team member, read each planned batch of open full texts or abstracts into D1-D8 paper cards, then gate the round (cards complete, quotes verbatim, Read column filled)',
  whenToUse: 'After plan_reading_batches.py has written a batch file for each member (research-team playbook, stage T3.5). For throughput launch one workflow per member in parallel.',
  phases: [
    { title: 'Plan', detail: 'list the batches in each member batch file; skip batches already carded' },
    { title: 'Read', detail: 'one agent per batch writes cards/<bid>.md + <bid>.digest.json; one retry per failed batch' },
    { title: 'Gate', detail: 'per member: cards complete, merge_chase, verify_card_quotes all exact, mark_read_from_cards, team_status' },
  ],
}

/*
 * team-read.js · research-team kit, stage T3.5 (deep reading into paper cards).
 * Launch:  Workflow({ scriptPath: '<repo>/scripts/workflows/team-read.js', args: { ... } })
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
 * Args specific to team-read:
 *   args.round       reading round number (default 1); only used to build the default batch-file path
 *   args.batchFiles  optional {slug: absolute path}: the batch JSON of each member, written by
 *                      python3 scripts/plan_reading_batches.py <team>/<slug> --round N [--exclude a.json,b.json] > FILE
 *                    default: <scratch>/batches-<slug>-r<round>.json
 *   args.batches     optional {slug: [{bid, mode}]}: skip the Plan agent for that member (then no already-carded check)
 *   args.only        optional {slug: [bid, ...]}: run only these batches of that member (the others are logged as skipped)
 *   args.overwrite   default false: batches whose cards/<bid>.md and <bid>.digest.json already exist are skipped (resume)
 *   args.retry       default true: re-run a batch once when its agent died or wrote no cards
 *
 * Writes (per member): <team>/<slug>/references/research/cards/<bid>.md + <bid>.digest.json;
 *   abstract batches may add papers/abstracts-chase-<bid>.json and open PDFs they found; the Gate merges the
 *   abstracts (scripts/merge_chase.py), fixes failing quotes and fills INDEX.md's Read column.
 * Next: commit the member's references/ (PDFs and txt/ are git-ignored); new open texts → acquire_fulltexts.py and a
 *   further round (plan_reading_batches.py --round N+1 --exclude <this round's batch file>); then team-synthesize.js.
 * Concurrency is min(16, CPUs-2) agents per workflow, so one workflow per member in parallel is faster than one big run.
 * Batch sizing that worked (plan_reading_batches.py defaults): core ≤110 pp and ≤5 works, supplement ≤220 pp and ≤8, a book
 *   (>150 pp) alone, abstract batches of 30; a later round must --exclude the batch files of rounds still in flight.
 * Cost baseline (worked example product/dfo-team/, 5 members, 795 cards): ~22 agents and ~5.8M tokens per member.
 */

const a = (typeof args === 'string' ? JSON.parse(args) : args) || {}
function need(keys) {
  const miss = keys.filter(k => a[k] === undefined || a[k] === null || a[k] === '')
  if (miss.length) throw new Error(`team-read: missing args: ${miss.join(', ')} (see the header comment)`)
}
need(['repo', 'team', 'scratch', 'date', 'members'])
if (!Array.isArray(a.members) || !a.members.length) throw new Error('team-read: args.members must be a non-empty array of team.json member objects')
if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error('team-read: args.date must be "YYYY-MM-DD"')
a.members.forEach((m, i) => { if (!m || !/^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') || !m.name) throw new Error(`team-read: members[${i}] needs a kebab-case slug and a name`) })
if (!String(a.repo).startsWith('/') || !String(a.scratch).startsWith('/')) throw new Error('team-read: args.repo and args.scratch must be absolute paths')
if (String(a.team).startsWith('/')) throw new Error('team-read: args.team must be relative to args.repo, e.g. "product/<team>"')
// args keys this workflow reads; anything else is logged (the kit mixes snake_case and camelCase option names)
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'round', 'batchFiles', 'batches', 'only', 'overwrite', 'retry']
const unknownArgs = Object.keys(a).filter(k => !KNOWN_ARGS.includes(k))
if (unknownArgs.length) log(`team-read.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)

const REPO = String(a.repo).replace(/\/+$/, '')
const TEAM_REL = String(a.team).replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCR = String(a.scratch).replace(/\/+$/, '')
const DATE = a.date
const ROUND = Number(a.round || 1)
const RETRY = a.retry !== false
const MEMBERS = a.members

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A() needs opts.phase and opts.label')
  return agent(prompt, opts)
}
function list(x) { return Array.isArray(x) && x.length ? x.join('; ') : '' }
function skillDir(m) { return `${TEAM}/${m.slug}` }
function cardsDir(m) { return `${skillDir(m)}/references/research/cards` }
function batchFile(m) { return (a.batchFiles && a.batchFiles[m.slug]) || `${SCR}/batches-${m.slug}-r${ROUND}.json` }

function teamCtx(m) {
  return `Team: ${TEAM}/. Read ${TEAM}/team.json first: "field" is the research field, "language" the language of the member skills, "roundtable" the roundtable folder, "chase_hints" field-wide open repositories, and "members" the researchers (hint, student_mode, chase_hints). The team was built with the nuwa kit in ${REPO} (rules and templates in ${REPO}/references/, tools in ${REPO}/scripts/). Today is ${DATE}.
Member: ${m.name} (slug ${m.slug}${m.hint ? `; ${m.hint}` : ''}). Skill folder: ${skillDir(m)}/. Where this prompt and the member's entry in team.json differ, team.json wins.`
}

const RULES = `House rules (non-negotiable):
- Evidence: every claim carries a page ("p. 7") or section ("§3.2") reference taken from the [[page N]] markers of the extracted text ("abstract" for an abstract). Quotes are copied verbatim, character for character (line breaks collapsed to single spaces), so a script can find them; never put a paraphrase inside quotation marks. If you did not read something, write "not read"; never guess.
- Sources: only public, legitimate material (open access, author-hosted copies, institutional repositories, free proceedings). Never Sci-Hub, LibGen, any paywall circumvention, or scraping behind a login.
- Privacy: never open, read or quote anything under a references/sources/private/ folder. Never put the user's e-mail address (or any personal address) into a request to an outside service; Crossref needs none, and where a service insists on one (Unpaywall) use nuwa-skill@users.noreply.github.com, the address scripts/acquire_fulltexts.py uses.
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCR}/. Do not git commit, push, stash, reset or checkout (the operator commits after the stage). Stop a process by its exact PID, never with pkill -f <pattern> (that can kill your own shell).`

function cardRules(m) {
  return `Card rules (non-negotiable):
- Follow ${REPO}/references/paper-reading-card.md: dimensions D1–D8, material roles, the card-file layout and digest fields of its section 四, and the quote rules. That file is written in Chinese; its rules apply as written.
- Every claim in a card carries a page or section reference from the [[page N]] markers.
- Quotes: at most 2 per card, copied EXACTLY from the text file (or from abstracts.json for an abstract) so that scripts/verify_card_quotes.py finds them; give the page.
- Link each card to the skill: "Method N" of ${m.slug}/SKILL.md (evidence ✅ / variant ⚠ / contradiction ✗) or "new-pattern candidate: <short name>". In the digest, method_links[].method is always written "Method N" (N = the number in the SKILL.md heading, whatever language the skill is written in) so that scripts can count it.
- A "transferable technique" is something a PhD student in this field could copy into their own work tomorrow (a proof device, an algorithm- or study-design move, an experiment or evaluation protocol, a writing move). Leave the line out rather than write a platitude.
- The D1–D8 dimensions were written for mathematical and computational research. Where a dimension is meaningless for a work in this field (for example no proofs), write "n/a" instead of forcing it.
- Card language: write the cards in the language of the texts you read (English texts → English cards) so that notes and verbatim quotes sit side by side; the skill itself follows team.json "language".`
}

const DIGEST_SHAPE = `{"id","year","title","read_level":"full|partial|abstract|metadata|unreadable","contribution":"one sentence","problem_entry":"how the problem was entered (D1, one line)","key_idea":"(D2, one line)","assumptions":"(D3, one line)","proof_devices":["named devices with pages"],"experiments":"(D5, one line or 'none')","positioning":"(D6, one line)","writing":"(D7, one line)","limits_future":"(D8, one line)","method_links":[{"method":"Method 3","relation":"evidence|variant|contradiction","note":"...","pages":"pp. 4-6"}],"new_pattern_candidates":[{"pattern":"short name","evidence":"...","pages":"..."}],"transferable":["..."],"coauthors":"...","quotes":[{"text":"verbatim","page":7}]}`

function specLine(b, bf) {
  return `Your work list (ids, years, titles, venues, roles, pages, DOIs/arXiv ids, authors, notes and the path of each extracted text file) is batch "${b.bid}" in ${bf}. Print it with:
  python3 -c "import json;b=[x for x in json.load(open('${bf}'))['batches'] if x['bid']=='${b.bid}'][0];[print(p) for p in b['papers']]"
Relative "txt" paths in that file are relative to ${REPO}.`
}

function leads(m) {
  const mh = list(m.chase_hints)
  return `Leads, in this order: this member's chase_hints${mh ? ` (${mh})` : ' (none given)'}; the team's "chase_hints" in team.json;${m.homepage ? ` the homepage ${m.homepage};` : ''} then the generic open sources: author and coauthor homepages, institutional repositories, department technical-report series, arXiv (arxiv.org/abs/<id>; export.arxiv.org answers 406 to cloud IPs), HAL, free proceedings, publisher open-access versions, Semantic Scholar / CORE open PDFs.`
}

function modeText(b, m) {
  if (b.mode === 'book') {
    return `- This is a book, monograph, thesis or long report (read at chapter level). Read the preface, the table of contents, the introduction of every chapter, and the chapters that carry the author's method (where the method is stated, analysed, applied and evaluated) and the concluding chapter. Write ONE long card with D1–D8 filled at chapter level, plus a "Chapter map" (one line per chapter: what it teaches, pages). Say which chapters you did not read.`
  }
  if (b.mode === 'supplement') {
    return `- supplement works: read the abstract, introduction and contributions paragraph, the method/algorithm statement, the assumptions and main result statements (with a look at how the key argument is made), the experiment or evaluation setup and the conclusion. Write a SHORT card: D1, D2, D3, D4 (brief), D5 (one line if there are experiments), D8.`
  }
  return `- core works: read the WHOLE work (appendices may be skimmed; say which). Write a FULL card: D1–D8 all filled.${b.mode !== 'core' ? ` (This batch has mode "${b.mode}"; read each item as its "role" and "note" say, and treat items without a note as core.)` : ''}`
}

function readPrompt(m, b, bf, retry) {
  const SK = skillDir(m), CARDS = cardsDir(m)
  return `${teamCtx(m)}

You are deep-reading research works by ${m.name} to deepen the research-craft skill at ${SK}/ (the user asked to read all of ${m.name}'s works on the publication list and distil them into the skill).

Before reading, read:
1. ${REPO}/references/paper-reading-card.md (card format).
2. ${SK}/SKILL.md, at least the core research methods, research heuristics and research taste sections (in a Chinese skill: 核心研究方法, 研究启发式, 研究品味), so that you can link cards to Method N.

Batch ${b.bid} (mode ${b.mode}).
${specLine(b, bf)}

How to read (the text files have [[page N]] markers; page through long files with the Read tool's offset/limit and locate sections with grep -n):
${modeText(b, m)}
- If a work entry carries a non-empty "note", follow it: it says what the item is, whose voice it is and how to read it. A published review is the reviewer's voice, never the authors'; a table of contents is "title only" (never invent chapter content).
- Before reading a text, check its first page: the title AND ${m.surname || m.name} among the authors (report series and title matching can yield other people's work). If it is not the work named, mark it "unreadable" and add "WRONG-TEXT <id>: <what the file really is>" to problems.
- If a text is garbled (mostly non-words, e.g. a broken font layer) or nearly empty (a scan without a text layer), mark it "unreadable" and add "REOCR <id>" to problems.

Output files (mkdir -p ${CARDS} first):
A) ${CARDS}/${b.bid}.md. Start with the three-line batch header from the card spec ("Batch intent / Focus dimensions / Material roles"; state the intent yourself after looking at the titles) and one line on how file pages map to printed pages. Then one card per work, heading "### <ID> · <title> (<venue> <year>, <DOI or arXiv>)" with the work's id from the list (e.g. "### S012 · ..."), and right under it the read level (full / partial / unreadable, with the parts read). After the dimensions add "**Method links**:", "**Transferable techniques**:" (bullets) and "**Quotes**:" (≤2 verbatim, with page).
B) ${CARDS}/${b.bid}.digest.json: a JSON array, one object per work, in this shape:
${DIGEST_SHAPE}
Every work of the batch gets a card and a digest object, including unreadable ones.

${cardRules(m)}

${RULES}
Edit no file other than the two output files.${retry ? '\nA previous attempt at this batch died or wrote no cards; files it left may exist. Overwrite them.' : ''}

Return the structured status (bid "${b.bid}").`
}

function absPrompt(m, b, bf, retry) {
  const SK = skillDir(m), CARDS = cardsDir(m), PAP = `${SK}/references/sources/papers`
  return `${teamCtx(m)}

You are cataloguing works of ${m.name} that have no open full text on disk (or are non-research items) for the research-craft skill at ${SK}/. The user asked to read all of ${m.name}'s works; for these only metadata and, where available, abstracts can be read.

Read first: ${REPO}/references/paper-reading-card.md (card format) and the core research methods section of ${SK}/SKILL.md.
Abstracts: ${PAP}/abstracts.json (keyed by work id). Metadata: ${SK}/references/sources/publications/works.json.

Batch ${b.bid} (mode abstract).
${specLine(b, bf)}

If the WebFetch or WebSearch tools are not loaded, load them with ToolSearch "select:WebFetch,WebSearch".
For a work with no abstract in abstracts.json, try (curl first; the WebSearch tool has a small per-session budget shared by every agent, so use it only when the curl leads are exhausted, at most 2 searches per work):
- Crossref: curl -s "https://api.crossref.org/works/<doi>" (the "abstract" field) — never add an e-mail or mailto parameter;
- the arXiv abstract page https://arxiv.org/abs/<id>; DataCite for arXiv DOIs (10.48550/arXiv.<id>); the Semantic Scholar graph API (https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=abstract,openAccessPdf); the publisher landing page.
${leads(m)}
Forbidden: Sci-Hub, LibGen, paywall circumvention, scraping behind a login.
- An abstract you found: record it verbatim in ${PAP}/abstracts-chase-${b.bid}.json (a JSON object keyed by work id, plus "<id>__src" holding the source URL; json.dump(..., ensure_ascii=False, indent=1)). The Gate merges it into abstracts.json with scripts/merge_chase.py, so your abstract quotes will verify afterwards.
- An OPEN PDF that is clearly the work (first page shows the title and ${m.surname || m.name} among the authors): download it with curl -sL -A "Mozilla/5.0" --max-time 90 to ${PAP}/<slug>.pdf, where <slug> is exactly what acquire_fulltexts.py computes from the works.json row (otherwise the next acquisition run will not see the file): python3 -c "import sys,json;sys.path.insert(0,'${REPO}/scripts');import acquire_fulltexts as q;w=[x for x in json.load(open('${SK}/references/sources/publications/works.json'))['works'] if x['id']=='<id>'][0];print(q.slug(w))". Check it starts with %PDF (head -c4) and add "NEW-PDF <id> <url>" to problems. Do not read it here; the next round will.

Write ${CARDS}/${b.bid}.md: a header line "Abstract-level cards — full text not available; claims rest on the abstract/metadata only", then for each work a compact card "### <id> · <title> (<venue> <year>, <DOI/arXiv>)" with **Read**: abstract | metadata-only, D1 (problem/entry), D2 (key idea), D8 (contribution), each one or two lines citing "abstract" as the location, and **Method links** only where the abstract clearly supports them. For a metadata-only work write one line on what can be inferred from title, venue and coauthors, labelled "inferred from title".
Also write ${CARDS}/${b.bid}.digest.json with the same object shape as full cards:
${DIGEST_SHAPE}
(read_level "abstract" or "metadata"; "" or [] for fields you cannot fill; quotes may be verbatim abstract sentences with "page": "abstract").

${cardRules(m)}

${RULES}
Edit no file other than the card files, abstracts-chase-${b.bid}.json and any open PDF you downloaded.${retry ? '\nA previous attempt at this batch died or wrote no cards; files it left may exist. Overwrite the card files.' : ''}

Return the structured status (bid "${b.bid}"; count works with an abstract as partial_read and metadata-only works as unreadable).`
}

function planPrompt(m, bf) {
  return `${teamCtx(m)}

Your job (PLAN, read-only): list the reading batches of ${m.name} in the batch file ${bf} (JSON written by scripts/plan_reading_batches.py: {"summary", "batches": [{"bid", "mode", "papers": [...]}]}).
With python, for each batch report bid, mode, number of works and total pages, and put in already_carded the bids for which BOTH ${cardsDir(m)}/<bid>.md and <bid>.digest.json already exist.
Also check, for every non-abstract batch, that each work's "txt" file exists (relative paths are relative to ${REPO}); add "MISSING-TXT <bid> <id>" to problems for each one missing (PDFs and txt/ are git-ignored, so a fresh checkout lacks them until scripts/acquire_fulltexts.py is rerun).
If the file does not exist or is not valid JSON, return file_exists false and say why in problems. Do not edit any file.`
}

function gatePrompt(m, rd) {
  const SK = skillDir(m), CARDS = cardsDir(m)
  const reports = rd.todo.map((b, i) => {
    const r = rd.reports[i]
    return r ? { bid: b.bid, mode: b.mode, cards_written: r.cards_written, unreadable: r.unreadable, problems: r.problems } : { bid: b.bid, mode: b.mode, agent: 'died' }
  })
  return `${teamCtx(m)}

Your job (GATE for the reading round just finished). Batch file: ${rd.bf}. Batches run now: ${rd.todo.map(b => b.bid).join(', ')}.
Readers' reports: ${JSON.stringify(reports)}
1. Completeness: for every batch above, ${CARDS}/<bid>.md and <bid>.digest.json exist; the digest parses as a JSON array; its ids equal the batch's work ids (compare with the batch file in python); every object has the digest fields of ${REPO}/references/paper-reading-card.md section 四 and a read_level in full|partial|abstract|metadata|unreadable; every id has a "### <ID> ·" heading in the .md. Repair small format problems yourself (a missing field → "" or [], a heading typo). Do NOT write missing cards: list those batch ids in batches_incomplete and the missing or extra work ids in id_mismatches.
2. Chase output: if any ${SK}/references/sources/papers/abstracts-chase-*.json exists or a reader reported NEW-PDF, run python3 ${REPO}/scripts/merge_chase.py ${SK}. It merges the abstracts into abstracts.json / abstract-sources.json (never overwriting an existing abstract; cleanly merged chunk files are deleted), then reruns acquire_fulltexts.py, which indexes the PDFs the readers saved and lists the ids that now have a full text: put those in new_texts (they are read in the next round, not here). If the acquisition step fails (e.g. no network), rerun with --no-acquire and say so in problems.
3. Quotes: python3 ${REPO}/scripts/verify_card_quotes.py ${SK}. For every NOT FOUND quote, open the text at the cited page and either replace the quote by the exact text or remove the quotation marks and keep it as a paraphrase with the page, in BOTH the .md card and the .digest.json. Rerun until every quote is exact (quotes_not_found must be 0; if one cannot be fixed, say why in problems).
4. python3 ${REPO}/scripts/mark_read_from_cards.py ${SK} (fills INDEX.md's Read column from read_level).
5. python3 ${REPO}/scripts/team_status.py ${TEAM} --no-quality; copy this member's row into status_row.
6. From the readers' problems, collect REOCR ids into reocr, WRONG-TEXT items into wrong_text and NEW-PDF items into new_pdfs (id + url).

${RULES}
Edit only: this round's card files (and quote fixes in earlier cards if the checker flags them), abstracts.json / abstract-sources.json via the merge, and INDEX.md via mark_read_from_cards.py.`
}

const STATUS = {
  type: 'object',
  properties: {
    bid: { type: 'string' },
    cards_written: { type: 'number' },
    full_read: { type: 'array', items: { type: 'string' } },
    partial_read: { type: 'array', items: { type: 'string' } },
    unreadable: { type: 'array', items: { type: 'string' } },
    new_pattern_candidates: { type: 'array', items: { type: 'string' } },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['bid', 'cards_written', 'full_read', 'partial_read', 'unreadable', 'new_pattern_candidates', 'problems'],
}
const PLAN = {
  type: 'object',
  properties: {
    file_exists: { type: 'boolean' },
    batches: { type: 'array', items: { type: 'object', properties: { bid: { type: 'string' }, mode: { type: 'string' }, papers: { type: 'number' }, pages: { type: 'number' } }, required: ['bid', 'mode', 'papers'] } },
    already_carded: { type: 'array', items: { type: 'string' } },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['file_exists', 'batches', 'already_carded', 'problems'],
}
const GATE = {
  type: 'object',
  properties: {
    batches_incomplete: { type: 'array', items: { type: 'string' } },
    id_mismatches: { type: 'array', items: { type: 'string' } },
    merged_chase: { type: 'boolean' },
    new_texts: { type: 'array', items: { type: 'string' } },
    quotes_total: { type: 'number' },
    quotes_fixed: { type: 'number' },
    quotes_not_found: { type: 'number' },
    reocr: { type: 'array', items: { type: 'string' } },
    wrong_text: { type: 'array', items: { type: 'string' } },
    new_pdfs: { type: 'array', items: { type: 'string' } },
    status_row: { type: 'string' },
    problems: { type: 'array', items: { type: 'string' } },
  },
  required: ['batches_incomplete', 'id_mismatches', 'merged_chase', 'new_texts', 'quotes_total', 'quotes_fixed', 'quotes_not_found', 'reocr', 'wrong_text', 'new_pdfs', 'status_row', 'problems'],
}

async function planStage(m) {
  const bf = batchFile(m)
  if (a.batches && Array.isArray(a.batches[m.slug])) {
    return { bf, batches: a.batches[m.slug], already_carded: [], problems: [] }
  }
  const p = await A(planPrompt(m, bf), { label: `plan:${m.slug}`, phase: 'Plan', schema: PLAN, effort: 'low' })
  if (!p) { log(`${m.slug}: plan agent returned nothing; member skipped`); return { bf, skipped: 'plan agent failed' } }
  if (!p.file_exists) { log(`${m.slug}: batch file ${bf} missing or invalid (${list(p.problems)}); member skipped`); return { bf, skipped: 'no batch file', problems: p.problems } }
  if (p.problems.length) log(`${m.slug}: plan found ${p.problems.length} problem(s), e.g. ${p.problems.slice(0, 3).join('; ')} (full list in the result)`)
  return { bf, batches: p.batches, already_carded: p.already_carded, problems: p.problems }
}

async function readStage(pl, m) {
  if (pl.skipped) return pl
  let todo = pl.batches
  const only = a.only && a.only[m.slug]
  if (Array.isArray(only)) {
    const keep = new Set(only)
    const dropped = todo.filter(b => !keep.has(b.bid)).map(b => b.bid)
    const unknown = only.filter(id => !todo.some(b => b.bid === id))
    if (dropped.length) log(`${m.slug}: args.only, not running ${dropped.length} batch(es): ${dropped.join(', ')}`)
    if (unknown.length) log(`${m.slug}: args.only names batches not in ${pl.bf}: ${unknown.join(', ')}`)
    todo = todo.filter(b => keep.has(b.bid))
  }
  const noTxt = new Set(pl.problems.filter(p => /^MISSING-TXT\s/.test(p)).map(p => p.split(/\s+/)[1]))
  const blockedByTxt = todo.filter(b => noTxt.has(b.bid)).map(b => b.bid)
  if (blockedByTxt.length) {
    log(`${m.slug}: skipping ${blockedByTxt.length} batch(es) whose text files are missing (${blockedByTxt.join(', ')}); run python3 scripts/acquire_fulltexts.py ${TEAM_REL}/${m.slug} to restore txt/, then rerun with only: {"${m.slug}": ${JSON.stringify(blockedByTxt)}}`)
    todo = todo.filter(b => !noTxt.has(b.bid))
  }
  if (!a.overwrite && pl.already_carded.length) {
    const done = new Set(pl.already_carded)
    const skipped = todo.filter(b => done.has(b.bid)).map(b => b.bid)
    if (skipped.length) log(`${m.slug}: ${skipped.length} batch(es) already carded, skipped (overwrite: true redoes them): ${skipped.join(', ')}`)
    todo = todo.filter(b => !done.has(b.bid))
  }
  if (!todo.length) { log(`${m.slug}: nothing to read`); return { ...pl, todo: [], reports: [], failed: [], missing_txt: blockedByTxt } }
  const byMode = {}
  todo.forEach(b => { byMode[b.mode] = (byMode[b.mode] || 0) + 1 })
  log(`${m.slug}: reading ${todo.length} batch(es) ${JSON.stringify(byMode)}`)

  const run = (b, retry) => A(b.mode === 'abstract' ? absPrompt(m, b, pl.bf, retry) : readPrompt(m, b, pl.bf, retry),
    { label: `read:${m.slug}:${b.bid}${retry ? ':retry' : ''}`, phase: 'Read', schema: STATUS })
  const reports = await parallel(todo.map(b => () => run(b, false)))
  const bad = () => todo.filter((b, i) => !reports[i] || !(reports[i].cards_written > 0))
  const failed1 = bad()
  if (failed1.length && RETRY) {
    log(`${m.slug}: retrying ${failed1.length} batch(es) once: ${failed1.map(b => b.bid).join(', ')}`)
    const again = await parallel(failed1.map(b => () => run(b, true)))
    failed1.forEach((b, j) => { if (again[j]) reports[todo.indexOf(b)] = again[j] })
  } else if (failed1.length) {
    log(`${m.slug}: ${failed1.length} batch(es) failed and args.retry is false: ${failed1.map(b => b.bid).join(', ')}`)
  }
  const failed = bad().map(b => b.bid)
  if (failed.length) log(`${m.slug}: still no cards for ${failed.join(', ')}; rerun with only: {"${m.slug}": ${JSON.stringify(failed)}}`)
  return { ...pl, todo, reports, failed, missing_txt: blockedByTxt }
}

async function gateStage(rd, m) {
  if (rd.skipped) return { slug: m.slug, skipped: rd.skipped, problems: rd.problems || [] }
  const done = rd.reports.filter(Boolean)
  const summary = {
    slug: m.slug,
    batch_file: rd.bf,
    batches_run: rd.todo.map(b => b.bid),
    batches_failed: rd.failed,
    batches_skipped_missing_txt: rd.missing_txt || [],
    cards_written: done.reduce((s, r) => s + (r.cards_written || 0), 0),
    unreadable: done.flatMap(r => r.unreadable),
    new_pattern_candidates: done.flatMap(r => r.new_pattern_candidates),
    reader_problems: done.flatMap(r => r.problems.map(p => `${r.bid}: ${p}`)),
    plan_problems: rd.problems || [],
  }
  if (!rd.todo.length) return { ...summary, gate: null }
  const g = await A(gatePrompt(m, rd), { label: `gate:${m.slug}`, phase: 'Gate', schema: GATE })
  if (!g) log(`${m.slug}: gate agent returned nothing; run verify_card_quotes.py and mark_read_from_cards.py by hand`)
  else {
    log(`${m.slug}: ${summary.cards_written} cards; quotes ${g.quotes_total} (fixed ${g.quotes_fixed}, not found ${g.quotes_not_found}); incomplete batches ${g.batches_incomplete.length}; new PDFs ${g.new_pdfs.length}; re-OCR ${g.reocr.length}`)
    if (g.quotes_not_found > 0) log(`${m.slug}: ${g.quotes_not_found} quote(s) still NOT FOUND; synthesis must wait until verify_card_quotes.py is all exact`)
  }
  return { ...summary, gate: g }
}

const results = await pipeline(MEMBERS, planStage, readStage, gateStage)
const members = results.map((r, i) => r || { slug: MEMBERS[i].slug, error: 'a stage threw; this member was dropped (see the run transcript)' })
const more = members.filter(r => r.gate && (r.gate.new_pdfs.length || r.gate.new_texts.length || r.gate.reocr.length)).map(r => r.slug)
const incomplete = members.filter(r => (r.batches_failed && r.batches_failed.length) || (r.batches_skipped_missing_txt && r.batches_skipped_missing_txt.length) || (r.gate && r.gate.batches_incomplete.length)).map(r => r.slug)
return {
  stage: 'T3.5 read',
  date: DATE,
  round: ROUND,
  members,
  next: [
    `Commit each member's references/ (cards, INDEX.md, abstracts*.json); PDFs and txt/ are git-ignored.`,
    incomplete.length ? `Incomplete or skipped batches for: ${incomplete.join(', ')}; restore missing texts with acquire_fulltexts.py if listed, then rerun team-read with args.only for those batch ids.` : 'All batches of this round have cards.',
    more.length ? `New open texts or re-OCR candidates for: ${more.join(', ')}; run python3 scripts/acquire_fulltexts.py ${TEAM_REL}/<slug>, then plan_reading_batches.py ${TEAM_REL}/<slug> --round ${ROUND + 1} --exclude <this round's batch file> and run team-read again.` : 'No new open texts reported.',
    'When every member is fully carded and verify_card_quotes.py is all exact: team-synthesize.js.',
  ],
}
