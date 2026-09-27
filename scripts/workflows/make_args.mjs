#!/usr/bin/env node
// make_args.mjs — build ready-to-launch Workflow calls for a team workflow from the team's team.json (Node >= 18).
//
//   node scripts/workflows/make_args.mjs <workflow> --team product/<team> [options]
//
// <workflow> is a name (team-read) or a path (scripts/workflows/team-read.js). It prints a JSON array of
// {"scriptPath", "args"} objects, ready to pass to the Workflow tool one by one (send them in ONE message so they run
// in parallel): one object per member for the per-member workflows (T1, T3.1–T3.7, T4), one object with ALL members
// for the team-level ones (team-layer.js, team-integrate.js). The member objects are copied from team.json verbatim.
//
// Options:
//   --team DIR        team folder relative to the repo (holds team.json); required
//   --date D          "YYYY-MM-DD" (default: today). Workflows cannot read the clock, so the date is passed in.
//   --member a,b      only these members (per-member workflows; team-level ones always take everyone)
//   --scratch DIR     scratch folder (default ${TMPDIR:-/tmp}/<team-folder>-scratch, created if missing). Use the SAME
//                     scratch for every stage of a team: team-read's default batch files, the chase chunks and the
//                     SKILL.md backups of T3.6/T3.7/T4 live there, and a stage looking in another folder skips the member.
//   --repo PATH       repo root (default: this repo)
//   --request "TEXT"  the user's request in their own words (quote it); set as args.request on every call, and every
//                     agent prompt opens with it. Recommended: workflow agents see only their prompt and the user's LATEST
//                     message in the session; when that is a side question they may decline their step as not asked for.
//                     Without --request a one-line note goes to stderr.
//   --set KEY=JSON    a workflow-specific arg, e.g. --set round=2 --set 'only={"ada-example":["c01"]}' --set to=review
//                     (the value is parsed as JSON, else taken as a string). The key must be one the workflow reads
//                     (its KNOWN_ARGS). A per-member map (only, only_chunks, skip_ids, batch_files, batches, notes, what)
//                     must be keyed by member slugs of this team; each per-member call gets only its own entry.
//   --together        per-member workflows: one call with all selected members instead of one call each
//   --args-only       print only the args object (needs exactly one call); handy for dry_run.mjs:
//                       node scripts/workflows/dry_run.mjs scripts/workflows/team-read.js "$(node scripts/workflows/make_args.mjs team-read --team product/<team> --member <slug> --args-only)"
//   --out DIR         also write DIR/<workflow>.<slug or team>.args.json for each call
//
// Exit code 1 on any error (unknown workflow, member, key or map slug).

import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
export const DEFAULT_REPO = path.resolve(HERE, '..', '..')
export const TEAM_LEVEL = new Set(['team-layer', 'team-integrate'])
// args keyed by member slug in the workflows (the old camelCase alias batchFiles included)
export const MAP_ARGS = ['only', 'only_chunks', 'skip_ids', 'batch_files', 'batchFiles', 'batches', 'notes', 'what']
// values in the examples/ args files that describe the fictional example team, not yours
export const EXAMPLE_ONLY = ['request', 'user_context', 'notes', 'what', 'skip_ids', 'batch_files', 'batchFiles', 'batches', 'only', 'only_chunks', 'since', 'label', 'roundtable']

export function today() {
  const d = new Date()
  const p = n => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`
}

export function workflowPath(w, repo = DEFAULT_REPO) {
  if (w.endsWith('.js') || w.includes('/')) return path.resolve(w)
  return path.join(repo, 'scripts', 'workflows', `${w.startsWith('team-') ? w : `team-${w}`}.js`)
}

export function workflowName(p) { return path.basename(p).replace(/\.js$/, '') }

export function knownArgs(src) {
  // the KNOWN_ARGS literal every team workflow declares, plus its RENAMED aliases
  const m = /const KNOWN_ARGS\s*=\s*\[([^\]]*)\]/.exec(src)
  const keys = m ? [...m[1].matchAll(/'([^']+)'|"([^"]+)"/g)].map(x => x[1] || x[2]) : []
  const r = /const RENAMED\s*=\s*\{([^}]*)\}/.exec(src)
  const aliases = r ? [...r[1].matchAll(/(\w+)\s*:/g)].map(x => x[1]) : []
  return { keys, aliases }
}

export function loadTeam(repo, team) {
  const rel = String(team).replace(/^\.\//, '').replace(/\/+$/, '')
  const file = path.join(repo, rel, 'team.json')
  let tj
  try { tj = JSON.parse(fs.readFileSync(file, 'utf8')) } catch (e) { throw new Error(`cannot read ${file}: ${e.message}`) }
  if (!Array.isArray(tj.members) || !tj.members.length) throw new Error(`${file}: "members" must be a non-empty array`)
  return { rel, tj, name: rel.split('/').pop() }
}

export function defaultScratch(teamName) { return path.join(process.env.TMPDIR || os.tmpdir(), `${teamName}-scratch`) }

// per-member map args whose keys are not slugs of the given members: [{key, unknown: [...]}]
export function mapProblems(args, slugs) {
  const out = []
  for (const k of MAP_ARGS) {
    const v = args && args[k]
    if (!v || typeof v !== 'object' || Array.isArray(v)) continue
    const unknown = Object.keys(v).filter(s => !slugs.includes(s))
    if (unknown.length) out.push({ key: k, unknown })
  }
  return out
}

function parseValue(v) { try { return JSON.parse(v) } catch { return v } }

export function buildCalls(o) {
  const repo = path.resolve(o.repo || DEFAULT_REPO)
  const wf = workflowPath(o.workflow, repo)
  if (!fs.existsSync(wf)) throw new Error(`no workflow ${wf}`)
  const name = workflowName(wf)
  const { keys, aliases } = knownArgs(fs.readFileSync(wf, 'utf8'))
  const { rel, tj, name: teamName } = loadTeam(repo, o.team)
  const all = tj.members
  let members = all
  if (o.member && o.member.length) {
    const unknown = o.member.filter(s => !all.some(m => m.slug === s))
    if (unknown.length) throw new Error(`--member: not in ${rel}/team.json: ${unknown.join(', ')}`)
    if (TEAM_LEVEL.has(name)) throw new Error(`${name} is team-level: it runs with ALL members of team.json (drop --member)`)
    members = all.filter(m => o.member.includes(m.slug))
  }
  const extra = {}
  for (const kv of o.set || []) {
    const i = kv.indexOf('=')
    if (i < 1) throw new Error(`--set ${kv}: use KEY=VALUE`)
    const k = kv.slice(0, i)
    if (['repo', 'team', 'scratch', 'date', 'members', 'request'].includes(k)) throw new Error(`--set ${k}: use --${k === 'members' ? 'member' : k} instead`)
    if (keys.length && !keys.includes(k) && !aliases.includes(k)) throw new Error(`--set ${k}: ${name} does not read this key; it reads ${keys.join(', ')}`)
    extra[k] = parseValue(kv.slice(i + 1))
  }
  const probs = mapProblems(extra, members.map(m => m.slug))
  if (probs.length) throw new Error(probs.map(p => `--set ${p.key}: key(s) ${p.unknown.join(', ')} are not members of this run (${members.map(m => m.slug).join(', ')})`).join('; '))
  const date = o.date || today()
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new Error('--date must be YYYY-MM-DD')
  const scratch = path.resolve(o.scratch || defaultScratch(teamName))
  const request = typeof o.request === 'string' ? o.request.trim() : ''
  const base = { repo, team: rel, scratch, date, ...(request ? { request } : {}) }
  // team-layer names the roundtable folder in its prompts; give it team.json's so the agents see the real path
  if (keys.includes('roundtable') && tj.roundtable && !('roundtable' in extra)) base.roundtable = tj.roundtable
  const groups = TEAM_LEVEL.has(name) || o.together ? [members] : members.map(m => [m])
  const calls = groups.map(ms => {
    const slugs = ms.map(m => m.slug)
    const own = Object.fromEntries(Object.entries(extra).map(([k, v]) => [k,
      MAP_ARGS.includes(k) && v && typeof v === 'object' && !Array.isArray(v)
        ? Object.fromEntries(Object.entries(v).filter(([s]) => slugs.includes(s))) : v])
      .filter(([k, v]) => !(MAP_ARGS.includes(k) && v && typeof v === 'object' && !Array.isArray(v) && !Object.keys(v).length)))
    const { roundtable, ...rest } = base
    return { scriptPath: wf, args: { ...rest, members: ms, ...(roundtable ? { roundtable } : {}), ...own } }
  })
  return { name, calls, scratch, teamLevel: TEAM_LEVEL.has(name) }
}

function usage(code) {
  const lines = fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('\n').slice(1)
  const end = lines.findIndex(l => !l.startsWith('//'))
  console.log(lines.slice(0, end).map(l => l.replace(/^\/\/ ?/, '')).join('\n'))
  process.exit(code)
}

function main() {
  const argv = process.argv.slice(2)
  const o = { set: [] }
  const pos = []
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]
    const val = () => { if (i + 1 >= argv.length) { console.error(`${a} needs a value`); process.exit(1) } return argv[++i] }
    if (a === '-h' || a === '--help') usage(0)
    else if (a === '--team') o.team = val()
    else if (a === '--date') o.date = val()
    else if (a === '--member') o.member = val().split(',').map(s => s.trim()).filter(Boolean)
    else if (a === '--scratch') o.scratch = val()
    else if (a === '--repo') o.repo = val()
    else if (a === '--request') o.request = val()
    else if (a === '--set') o.set.push(val())
    else if (a === '--together') o.together = true
    else if (a === '--args-only') o.argsOnly = true
    else if (a === '--out') o.out = val()
    else if (a.startsWith('--')) { console.error(`unknown option ${a}`); usage(1) }
    else pos.push(a)
  }
  if (pos.length !== 1 || !o.team) usage(1)
  o.workflow = pos[0]
  let r
  try { r = buildCalls(o) } catch (e) { console.error(`make_args: ${e.message}`); process.exit(1) }
  if (o.argsOnly && r.calls.length !== 1) { console.error(`make_args: --args-only needs exactly one call (got ${r.calls.length}); add --member <slug> or --together`); process.exit(1) }
  try { fs.mkdirSync(r.scratch, { recursive: true }) } catch (e) { console.error(`make_args: cannot create scratch ${r.scratch}: ${e.message}`); process.exit(1) }
  if (o.out) {
    fs.mkdirSync(o.out, { recursive: true })
    for (const c of r.calls) {
      const who = r.teamLevel || c.args.members.length > 1 ? 'team' : c.args.members[0].slug
      fs.writeFileSync(path.join(o.out, `${r.name}.${who}.args.json`), JSON.stringify(c.args, null, 1) + '\n')
    }
  }
  console.log(JSON.stringify(o.argsOnly ? r.calls[0].args : r.calls, null, 1))
  if (!(o.request || '').trim()) console.error('make_args: note: no --request; pass the user\'s request in their own words (--request "…") so every agent prompt opens with it (agents otherwise see only the user\'s latest message)')
  if (!o.argsOnly) console.error(`${r.calls.length} ${r.name} call(s)${r.teamLevel ? ' (team-level: all members)' : r.calls.length > 1 ? ', one per member: launch them in one message' : ''}; scratch ${r.scratch}`)
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main()
