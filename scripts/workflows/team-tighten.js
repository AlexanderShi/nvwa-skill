export const meta = {
  name: 'team-tighten',
  description: 'T3.7 tighten: per team member, losslessly move long evidence from an over-long SKILL.md into references/research/09-evidence-ledger.md, verify with scripts (lossless, protected sections unchanged, gates), fix until the gates pass',
  whenToUse: 'After team-synthesize when a member SKILL.md is still over the word target (research-team playbook, stage T3.7). Members already within the target are skipped.',
  phases: [
    { title: 'Tighten', detail: 'backup, then move exhaustive evidence to 09-evidence-ledger.md under explicit anchors' },
    { title: 'Verify', detail: 'read-only skeptic: lossless (check_ledger.py), protected sections byte-identical, gates, still useful' },
    { title: 'Fix', detail: 'apply confirmed findings; one more fix round if a gate still fails' },
  ],
}

/*
 * team-tighten.js · research-team kit, stage T3.7 (lossless distillation of SKILL.md).
 * Launch:  Workflow({ scriptPath: '<repo>/scripts/workflows/team-tighten.js', args: { ... } })
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
 * Args specific to team-tighten:
 *   args.target_words target SKILL.md length in words (default 11500)
 *   args.max_words    hard gate for wc -w after tightening (default target_words + 1500)
 *   args.force        default false: tighten even when SKILL.md is already within target_words
 *   (old names targetWords / maxWords are still accepted, with a log line)
 *
 * Writes (per member): SKILL.md and references/research/09-evidence-ledger.md only.
 *   Backup before tightening: <scratch>/<slug>-SKILL.before-tighten-<date>.md (kept if it already exists).
 * Gates: scripts/check_ledger.py --before <backup>, with NO --allow: tightening changes neither the frontmatter nor
 *   Activation Rules, so any "verbatim" problem is a real one (card ids + quotes before ⊆ after ∪ ledger; anchors resolve),
 *   scripts/quality_check.py 12/12, scripts/check_links.py, wc -w ≤ max_words.
 * Next: commit per member; then team-integrate.js.
 * Cost baseline (worked example product/dfo-team/): ~3 agents and ~0.7M tokens per member.
 */

const a = (typeof args === 'string' ? JSON.parse(args) : args) || {}
function need(keys) {
  const miss = keys.filter(k => a[k] === undefined || a[k] === null || a[k] === '')
  if (miss.length) throw new Error(`team-tighten: missing args: ${miss.join(', ')} (see the header comment)`)
}
need(['repo', 'team', 'scratch', 'date', 'members'])
if (!Array.isArray(a.members) || !a.members.length) throw new Error('team-tighten: args.members must be a non-empty array of team.json member objects')
if (!/^\d{4}-\d{2}-\d{2}$/.test(String(a.date))) throw new Error('team-tighten: args.date must be "YYYY-MM-DD"')
a.members.forEach((m, i) => { if (!m || !/^[a-z0-9][a-z0-9-]*$/.test(m.slug || '') || !m.name) throw new Error(`team-tighten: members[${i}] needs a kebab-case slug and a name`) })
if (!String(a.repo).startsWith('/') || !String(a.scratch).startsWith('/')) throw new Error('team-tighten: args.repo and args.scratch must be absolute paths')
if (String(a.team).startsWith('/')) throw new Error('team-tighten: args.team must be relative to args.repo, e.g. "product/<team>"')
// args keys this workflow reads (all snake_case); anything else is logged. Old camelCase names still work as aliases.
const KNOWN_ARGS = ['repo', 'team', 'scratch', 'date', 'members', 'target_words', 'max_words', 'force']
const RENAMED = { targetWords: 'target_words', maxWords: 'max_words' } // old camelCase name -> current name
const ALIAS_OF = Object.fromEntries(Object.entries(RENAMED).map(([o, k]) => [k, o]))
function arg(key) { return a[key] !== undefined ? a[key] : ALIAS_OF[key] ? a[ALIAS_OF[key]] : undefined }
for (const [old, key] of Object.entries(RENAMED)) {
  if (a[old] === undefined) continue
  log(a[key] === undefined
    ? `team-tighten.js: args.${old} is the old name of args.${key}; using it (rename it to ${key})`
    : `team-tighten.js: args.${old} ignored because args.${key} is also given (${old} is only an alias)`)
}
const unknownArgs = Object.keys(a).filter(k => !KNOWN_ARGS.includes(k) && !(k in RENAMED))
if (unknownArgs.length) log(`team-tighten.js ignores args key(s) it does not know (misspelt?): ${unknownArgs.join(', ')}; it reads ${KNOWN_ARGS.join(', ')}`)

const REPO = String(a.repo).replace(/\/+$/, '')
const TEAM_REL = String(a.team).replace(/^\.\//, '').replace(/\/+$/, '')
const TEAM = `${REPO}/${TEAM_REL}`
const SCR = String(a.scratch).replace(/\/+$/, '')
const DATE = a.date
const TARGET = Number(arg('target_words') || 11500)
const MAXW = Number(arg('max_words') || TARGET + 1500)
const MEMBERS = a.members

function A(prompt, opts) {
  if (!opts || !opts.phase || !opts.label) throw new Error('A() needs opts.phase and opts.label')
  return agent(prompt, opts)
}
function skillDir(m) { return `${TEAM}/${m.slug}` }
function backup(m) { return `${SCR}/${m.slug}-SKILL.before-tighten-${DATE}.md` }
function ledger(m) { return `${skillDir(m)}/references/research/09-evidence-ledger.md` }

const RULES = `House rules (non-negotiable):
- Lossless: nothing is deleted, only moved; quotes stay verbatim; every card id keeps its page references. Never put a paraphrase inside quotation marks.
- Privacy: never open, read or quote anything under a references/sources/private/ folder.
- Scope: edit only the files this step names as its outputs; scratch files go under ${SCR}/. Do not git commit, push, stash, reset or checkout (the operator commits after the stage). Stop a process by its exact PID, never with pkill -f <pattern>.`

function protectedList(m) {
  return `frontmatter, How to Use (except a pointer to the ledger and technique catalog), Activation Rules, ${m.student_mode ? 'Student Mode, ' : ''}Research Integrity Rules, the method numbering and headings, the Honest Boundary facts and coverage numbers, and the Roundtable Card content (in a skill written in another language, the equivalent sections, e.g. 激活规则, 研究诚信规则, 诚实边界)`
}

function ctx(m) {
  const SK = skillDir(m)
  return `Team: ${TEAM}/ (read ${TEAM}/team.json for the field and the language of the skills). Today is ${DATE}.
${m.name}'s research-craft skill is ${SK}/SKILL.md. It was updated from a full-text reading of the researcher's works (cards in references/research/cards/, index 07-paper-cards.md, synthesis 08-deep-reading-synthesis.md, technique catalog references/technique-catalog.md; possibly a first 09-evidence-ledger.md). A skill is loaded into a model's context on activation and must stay actionable: the user asked to DISTIL the reading into the skill, not to paste it. Target: at most ~${TARGET} words (hard limit ${MAXW}).

${RULES}`
}

function tightenPrompt(m) {
  const SK = skillDir(m)
  return `${ctx(m)}

Your job (TIGHTEN, lossless): bring SKILL.md to at most ~${TARGET} words without losing information or traceability.
0. Measure: wc -w ${SK}/SKILL.md. ${a.force ? 'Tighten even if it is already within the target (args.force).' : `If it is already ≤ ${TARGET} words AND every 09-evidence-ledger.md#… link in SKILL.md resolves, change nothing and return skipped=true.`}
1. Save a copy first: mkdir -p ${SCR} && cp -n ${SK}/SKILL.md ${backup(m)} (keep an existing copy: it is the pre-tighten state).
2. Create or extend ${ledger(m)}: the full evidence behind SKILL.md, one section per SKILL.md item, each preceded by an explicit anchor line (<a id="method-1"></a>, then "## Method 1: <name>"; likewise heuristic-N, taste-marks, taste-warnings, anatomy-<short-name>, corrections, card-key). Move there, verbatim, every long evidence list, every per-work case list beyond the strongest few, long say–do tallies, long variant/contradiction explanations and long anatomy table rows. Start the ledger with a short Contents list of its anchors.
3. In SKILL.md keep, for every core method: One line; Evidence reduced to Stated (the single strongest statement, verbatim with card and page if it is a quote), Practice (the 3–5 strongest cards with pages), Say–do (one line with the counts), Variants/corrections (at most 4 one-line bullets, each keeping its ✗/⚠ mark and card ref); a pointer "(full evidence: references/research/09-evidence-ledger.md#method-N)"; Steps; Applies to stage; Different from standard practice; Limitations. Heuristics and taste items: one or two lines each with at most 3 card refs, plus a ledger pointer. Signature work anatomy: keep the anatomies but at most ~2 lines per row. Research trajectory: keep the table, trim the prose. Keep a short "Corrections from the full texts" list (one line each) near the Honest Boundary so the corrections stay visible.
4. Do NOT change: ${protectedList(m)}. Do not add new claims.
5. Every quotation left in SKILL.md stays verbatim. Every card id in SKILL.md exists in 07-paper-cards.md.
6. Link the ledger from the sources appendix.
7. Gates: python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md → 12/12 (the checker counts method headings, steps, say–do marks, taste items, workflows with checkpoints, anatomies, honest-boundary items, tensions and verifiable ids — keep enough of each); python3 ${REPO}/scripts/check_ledger.py ${SK} --before ${backup(m)} (no --allow: tightening changes neither the frontmatter nor Activation Rules) → lossless (card ids, page references and quotes of the pre-tighten copy all in SKILL.md or the ledger; frontmatter, Activation Rules, Research Integrity Rules${m.student_mode ? ', Student Mode' : ''} byte-identical) and every anchor resolves; python3 ${REPO}/scripts/check_links.py ${SK} → 0 broken. Report words before/after (wc -w).
Edit only SKILL.md and 09-evidence-ledger.md.`
}

function verifyPrompt(m, t) {
  const SK = skillDir(m)
  return `${ctx(m)}

SKILL.md has just been tightened (report: ${JSON.stringify(t)}); the pre-tighten copy is ${backup(m)} and the moved material is in ${ledger(m)}. You are a READ-ONLY reviewer: do not edit files.
Check with scripts, not by eye:
1. Lossless: python3 ${REPO}/scripts/check_ledger.py ${SK} --before ${backup(m)} (no --allow; every "✗" line it prints is a finding, none is excused by judgement): every card id, page reference and quotation in the pre-tighten copy appears in the new SKILL.md or in the ledger, and every SKILL.md → ledger anchor resolves. Every ✗/⚠ correction still appears somewhere, and each method's corrections are at least mentioned in SKILL.md.
2. Frontmatter, Activation Rules, Research Integrity Rules${m.student_mode ? ' and Student Mode' : ''} are byte-identical to the pre-tighten copy (check_ledger.py --before checks this; the equivalent headings in another language count); the method numbering and headings, the Honest Boundary facts and coverage numbers and the Roundtable Card are unchanged in substance, and How to Use changed at most by a pointer (diff them).
3. python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md is 12/12; wc -w ≤ ${MAXW}; python3 ${REPO}/scripts/check_links.py ${SK} is clean; every 09-evidence-ledger.md#anchor linked from SKILL.md exists.
4. Usefulness: read the new SKILL.md end to end. Is each method still executable (steps intact), and is the strongest evidence still visible next to each claim? Is anything important now only in the ledger that should be back in SKILL.md?
Report findings with severity (blocker = information lost or a protected section changed; major = gate failing or a method no longer usable; minor = polish) and a concrete fix each.`
}

function fixPrompt(m, findings, round) {
  const SK = skillDir(m)
  return `${ctx(m)}

SKILL.md was tightened (evidence moved to ${ledger(m)}; pre-tighten copy at ${backup(m)}). ${round === 1 ? 'A read-only reviewer reported:' : 'After the first fix round some gates still fail:'} ${JSON.stringify(findings)}
Your job (FIX${round > 1 ? ', round ' + round : ''}): verify each finding, apply the ones you confirm (blockers and majors always); restore anything lost from the pre-tighten copy (into SKILL.md or the ledger); restore protected sections byte for byte. Do not modify the pre-tighten copy.
Then run every gate and report each in gates (name, command, passed, detail):
- lossless: python3 ${REPO}/scripts/check_ledger.py ${SK} --before ${backup(m)} (no --allow) → no problems
- quality_check: python3 ${REPO}/scripts/quality_check.py ${SK}/SKILL.md → 12/12
- links: python3 ${REPO}/scripts/check_links.py ${SK} → 0 broken
- words: wc -w ${SK}/SKILL.md → ≤ ${MAXW}
If a script does not exist in this checkout, do the equivalent check with python and say so in detail.
Edit only SKILL.md and 09-evidence-ledger.md. Report words before/after, the gates and what you declined.`
}

const TIGHT = {
  type: 'object',
  properties: {
    skipped: { type: 'boolean' },
    words_before: { type: 'number' },
    words_after: { type: 'number' },
    ledger_sections: { type: 'number' },
    quality_check: { type: 'string' },
    summary: { type: 'string' },
  },
  required: ['skipped', 'words_before', 'words_after', 'ledger_sections', 'quality_check', 'summary'],
}
const FINDINGS = {
  type: 'object',
  properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor'] }, problem: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'problem', 'fix'] } } },
  required: ['findings'],
}
const FIX = {
  type: 'object',
  properties: {
    applied: { type: 'number' },
    declined: { type: 'array', items: { type: 'string' } },
    gates: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, command: { type: 'string' }, passed: { type: 'boolean' }, detail: { type: 'string' } }, required: ['name', 'command', 'passed', 'detail'] } },
    words_before: { type: 'number' },
    words_after: { type: 'number' },
    summary: { type: 'string' },
  },
  required: ['applied', 'declined', 'gates', 'words_before', 'words_after', 'summary'],
}

async function tightenStage(m) {
  const t = await A(tightenPrompt(m), { label: `tighten:${m.slug}`, phase: 'Tighten', schema: TIGHT })
  if (!t) { log(`${m.slug}: tighten agent returned nothing; member stopped`); return { slug: m.slug, stopped: 'tighten agent failed' } }
  if (t.skipped) { log(`${m.slug}: already ${t.words_before} words (≤ ${TARGET}); skipped`); return { slug: m.slug, skipped: true, tighten: t } }
  log(`${m.slug}: ${t.words_before} → ${t.words_after} words; ledger sections ${t.ledger_sections}; quality ${t.quality_check}`)
  return { slug: m.slug, tighten: t }
}

async function verifyStage(s, m) {
  if (s.stopped || s.skipped) return s
  const v = await A(verifyPrompt(m, s.tighten), { label: `verify-tighten:${m.slug}`, phase: 'Verify', schema: FINDINGS })
  if (!v) log(`${m.slug}: reviewer returned nothing; the fix agent will still run every gate`)
  const findings = v ? v.findings : []
  log(`${m.slug}: ${findings.length} findings (${findings.filter(f => f.severity === 'blocker').length} blockers)`)
  return { ...s, findings, reviewed: !!v }
}

async function fixStage(s, m) {
  if (s.stopped || s.skipped) return s
  let fix = await A(fixPrompt(m, s.findings, 1), { label: `fix-tighten:${m.slug}`, phase: 'Fix', schema: FIX })
  let failing = fix ? fix.gates.filter(g => !g.passed) : [{ name: 'fix agent', command: '-', passed: false, detail: 'fix agent returned nothing' }]
  let rounds = 1
  if (failing.length) {
    log(`${m.slug}: gate(s) still failing: ${failing.map(g => g.name).join(', ')}; one more fix round`)
    const fix2 = await A(fixPrompt(m, failing.map(g => ({ severity: 'blocker', problem: `${g.name} failed: ${g.detail}`, fix: `make "${g.command}" pass` })), 2), { label: `fix2-tighten:${m.slug}`, phase: 'Fix', schema: FIX })
    rounds = 2
    if (fix2) { fix = fix2; failing = fix2.gates.filter(g => !g.passed) }
    if (failing.length) log(`${m.slug}: STILL failing after two fix rounds: ${failing.map(g => `${g.name} (${g.detail})`).join('; ')}; needs a human look (backup: ${backup(m)})`)
  }
  return { ...s, fix, fix_rounds: rounds, gates_failing: failing.map(g => g.name) }
}

const results = await pipeline(MEMBERS, tightenStage, verifyStage, fixStage)
const members = results.map((r, i) => r || { slug: MEMBERS[i].slug, stopped: 'a stage threw; this member was dropped (see the run transcript)' })
return {
  stage: 'T3.7 tighten',
  date: DATE,
  target_words: TARGET,
  members: members.map(r => ({
    slug: r.slug,
    stopped: r.stopped || null,
    skipped: !!r.skipped,
    backup: r.skipped || r.stopped ? null : `${SCR}/${r.slug}-SKILL.before-tighten-${DATE}.md`,
    tighten: r.tighten || null,
    findings: r.findings ? r.findings.length : null,
    fix: r.fix || null,
    fix_rounds: r.fix_rounds || 0,
    gates_failing: r.gates_failing || null,
  })),
  next: [
    'Commit each tightened member (SKILL.md + references/research/09-evidence-ledger.md).',
    'Then team-integrate.js (team README, DEEP-READING.md, roundtable) once every member is synthesised.',
  ],
}
