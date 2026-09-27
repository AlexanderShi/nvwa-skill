#!/usr/bin/env node
// dry_run.mjs — preview and debug a saved team workflow without spending tokens (Node >= 18).
//
//   node scripts/workflows/dry_run.mjs <workflow.js> <args.json | '{...inline json...}'> [options]
//
// The workflow runs in a sandbox that mimics the Workflow runtime: agent() returns a fake result shaped by
// opts.schema instead of spawning an agent; parallel() and pipeline() keep the runtime's semantics (a thunk or item
// that throws becomes null; a pipeline stage gets (prev, item, index), the first stage gets the item, and a stage that
// returns null ends that item's chain); phase() and log() print; Date.now(), Math.random() and new Date() throw as they
// do in the runtime; workflow() is not supported. It prints the meta block, every agent call (label, phase, schema
// keys and the start of its prompt) and the return value, then a summary with warnings.
//
// Fake agent results (from opts.schema): "" strings (the first value for an enum), 0 numbers, [] arrays, and
// booleans true, except names such as blocked/skipped/failed/missing, which get false so the happy path runs.
// Without a schema the fake result is a short string. Change them with:
//   --items N         put N schema-shaped items in every array; strings become "<field>" / "<field-i>" placeholders
//   --bools MODE      happy (default) | true | false  (false exercises the not-ready / not-passed branches)
//   --answers FILE    JSON object {"<regex on the agent label>": value}; the first matching key wins.
//                     value: an object (merged over the fake result, schema-aware: missing fields are filled),
//                     null (the agent "died"), a string (schema-less agents), or an array = one value per
//                     successive matching call (the last one repeats). See examples/*.answers.json.
// Args: string values "$REPO" and "$SCRATCH" are replaced (default: this repo, and <tmpdir>/nuwa-dry-run/<team>).
//   --repo PATH       value for $REPO             --scratch PATH   value for $SCRATCH
//   --team DIR        use <repo>/DIR/team.json: sets args.team and args.members (all, or --member ones)
//   --member a,b      keep only these member slugs (after --team, or from the args file)
// Output:
//   --chars N         prompt characters shown per agent (default 500; a prefix shared with an earlier prompt,
//                     such as the house rules, is collapsed to one line)
//   --full            print every prompt in full           --out DIR   write each prompt to DIR/NNN-<label>.md
//   --quiet           no per-agent prompt text              --forbid RE  warn when a prompt matches RE
//   --strict          exit 2 when there are warnings (exit 1 = the workflow threw or does not parse)
//
// Nothing here touches the repo: the only files written are under --out.

import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import vm from 'node:vm'
import { fileURLToPath } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const DEFAULT_REPO = path.resolve(HERE, '..', '..')
const NEGATIVE_BOOL = /^(blocked|skipped|skip|stopped|failed|fail|missing|error|errors|stuck|dropped|incomplete|truncated|aborted|rejected|timed_out|timeout)$/i
const EFFORTS = new Set(['low', 'medium', 'high', 'xhigh', 'max'])

// ---------------------------------------------------------------- CLI
function usage(code) {
  // the header comment block at the top of this file is the help text
  const lines = fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split('\n').slice(1)
  const end = lines.findIndex(l => !l.startsWith('//'))
  console.log(lines.slice(0, end < 0 ? lines.length : end).map(l => l.replace(/^\/\/ ?/, '')).join('\n'))
  process.exit(code)
}
const argv = process.argv.slice(2)
const opt = { chars: 500, items: 0, bools: 'happy', full: false, quiet: false, strict: false, out: null, answers: null, forbid: null, repo: null, scratch: null, team: null, member: null }
const pos = []
for (let i = 0; i < argv.length; i++) {
  const a = argv[i]
  const val = () => { if (i + 1 >= argv.length) { console.error(`${a} needs a value`); process.exit(1) } return argv[++i] }
  if (a === '-h' || a === '--help') usage(0)
  else if (a === '--full') opt.full = true
  else if (a === '--quiet') opt.quiet = true
  else if (a === '--strict') opt.strict = true
  else if (a === '--out') opt.out = val()
  else if (a === '--chars') opt.chars = Number(val())
  else if (a === '--items') opt.items = Number(val())
  else if (a === '--bools') opt.bools = val()
  else if (a === '--answers') opt.answers = val()
  else if (a === '--forbid') opt.forbid = new RegExp(val())
  else if (a === '--repo') opt.repo = val()
  else if (a === '--scratch') opt.scratch = val()
  else if (a === '--team') opt.team = val()
  else if (a === '--member') opt.member = val().split(',').map(s => s.trim()).filter(Boolean)
  else if (a.startsWith('--')) { console.error(`unknown option ${a}`); usage(1) }
  else pos.push(a)
}
if (pos.length !== 2) usage(1)
if (!['happy', 'true', 'false'].includes(opt.bools)) { console.error('--bools must be happy, true or false'); process.exit(1) }
if (!Number.isInteger(opt.items) || opt.items < 0 || !Number.isInteger(opt.chars) || opt.chars < 0) { console.error('--items and --chars take a non-negative integer'); process.exit(1) }

const WF_PATH = path.resolve(pos[0])
const REPO = path.resolve(opt.repo || DEFAULT_REPO)
const warnings = []
const warn = msg => { warnings.push(msg); console.log(`  ⚠ ${msg}`) }
const readJson = (p, what) => {
  try { return JSON.parse(fs.readFileSync(p, 'utf8')) } catch (e) { console.error(`cannot read ${what} ${p}: ${e.message}`); process.exit(1) }
}

// ---------------------------------------------------------------- args
let args
let argsLabel
if (/^\s*[{"[]/.test(pos[1])) {
  // inline JSON; a JSON string ("{\"repo\": ...}") reaches the script as a string, as a stringified Workflow args would
  try { args = JSON.parse(pos[1]) } catch (e) { console.error(`inline args are not valid JSON: ${e.message}`); process.exit(1) }
  argsLabel = typeof args === 'string' ? 'inline JSON, passed to the script as a string' : 'inline JSON'
} else {
  args = readJson(path.resolve(pos[1]), 'args file')
  argsLabel = path.relative(process.cwd(), path.resolve(pos[1])) || pos[1]
}
if ((opt.team || opt.member) && (!args || typeof args !== 'object' || Array.isArray(args))) { console.error('--team / --member need args given as a JSON object'); process.exit(1) }
if (opt.team) {
  const tj = readJson(path.join(REPO, opt.team, 'team.json'), 'team.json')
  args.team = opt.team.replace(/^\.\//, '').replace(/\/+$/, '')
  args.members = tj.members
}
if (opt.member && Array.isArray(args.members)) {
  const unknown = opt.member.filter(s => !args.members.some(m => m && m.slug === s))
  if (unknown.length) { console.error(`--member: not in members: ${unknown.join(', ')}`); process.exit(1) }
  args.members = args.members.filter(m => opt.member.includes(m.slug))
}
const teamName = String(args.team || 'team').split('/').filter(Boolean).pop()
const SCRATCH = path.resolve(opt.scratch || path.join(os.tmpdir(), 'nuwa-dry-run', teamName))
const subst = v => {
  if (typeof v === 'string') return v.split('$REPO').join(REPO).split('$SCRATCH').join(SCRATCH)
  if (Array.isArray(v)) return v.map(subst)
  if (v && typeof v === 'object') return Object.fromEntries(Object.entries(v).map(([k, x]) => [k, subst(x)]))
  return v
}
args = subst(args)

let answers = []
if (opt.answers) {
  const raw = readJson(path.resolve(opt.answers), 'answers file')
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) { console.error('the answers file must hold a JSON object {"<label regex>": value}'); process.exit(1) }
  answers = Object.entries(raw).filter(([k]) => !k.startsWith('_')).map(([k, v]) => {
    let re
    try { re = new RegExp(k) } catch (e) { console.error(`answers file: "${k}" is not a valid regular expression: ${e.message}`); process.exit(1) }
    return { key: k, re, value: subst(v), used: 0 }
  })
}

// ---------------------------------------------------------------- source, meta, static checks
const src = fs.readFileSync(WF_PATH, 'utf8')

function scanLiteral(text, start) {
  // returns the index just past the object literal that opens at text[start] === '{'
  let depth = 0
  for (let i = start; i < text.length; i++) {
    const c = text[i]
    if (c === '"' || c === "'" || c === '`') { i = skipString(text, i); continue }
    if (c === '/' && text[i + 1] === '/') { i = text.indexOf('\n', i); if (i < 0) return -1; continue }
    if (c === '/' && text[i + 1] === '*') { i = text.indexOf('*/', i) + 1; if (i <= 0) return -1; continue }
    if (c === '{' || c === '[') depth++
    if (c === '}' || c === ']') { depth--; if (depth === 0) return i + 1 }
  }
  return -1
}
function skipString(text, i) {
  const q = text[i]
  for (let j = i + 1; j < text.length; j++) {
    if (text[j] === '\\') { j++; continue }
    if (text[j] === q) return j
  }
  return text.length
}
function pureLiteralProblems(lit) {
  // tokens allowed in a pure literal: strings without ${}, numbers, true/false/null, keys, { } [ ] , : and a leading minus
  const probs = []
  const re = /\s+|\/\/[^\n]*|\/\*[\s\S]*?\*\/|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`|-?\d+(?:\.\d+)?(?:e[+-]?\d+)?|\.\.\.|[A-Za-z_$][\w$]*|[{}[\],:]|./gy
  const toks = []
  let m
  while ((m = re.exec(lit)) !== null && m[0].length) {
    const t = m[0]
    if (/^\s+$/.test(t) || t.startsWith('//') || t.startsWith('/*')) continue
    toks.push(t)
  }
  toks.forEach((t, k) => {
    if (t.startsWith('`') && t.includes('${')) probs.push('template interpolation')
    else if (t === '...') probs.push('spread')
    else if (/^[A-Za-z_$]/.test(t) && toks[k + 1] !== ':' && !['true', 'false', 'null'].includes(t)) probs.push(`identifier "${t}"`)
    else if (!/^[{}[\],:]$/.test(t) && !/^["'`]/.test(t) && !/^-?\d/.test(t) && !/^[A-Za-z_$]/.test(t)) probs.push(`token "${t}"`)
  })
  return [...new Set(probs)]
}

console.log(`dry run  ${path.relative(process.cwd(), WF_PATH) || WF_PATH}`)
console.log(`args     ${argsLabel}${opt.team ? ` (members from ${opt.team}/team.json)` : ''}; $REPO=${REPO}; $SCRATCH=${SCRATCH}`)
if (opt.answers) console.log(`answers  ${opt.answers} (${answers.length} rule(s))`)
console.log(`fakes    strings ${opt.items ? 'placeholders' : '""'}, numbers 0, arrays of ${opt.items}, booleans ${opt.bools}`)

const metaMatch = /^export\s+const\s+meta\s*=\s*/m.exec(src)
let meta = null
if (!metaMatch) warn('the script does not begin with "export const meta = {...}"')
else {
  if (src.slice(0, metaMatch.index).replace(/\/\/[^\n]*|\/\*[\s\S]*?\*\/|\s+/g, '') !== '') warn('code before "export const meta" (meta must come first)')
  const s = metaMatch.index + metaMatch[0].length
  const e = src[s] === '{' ? scanLiteral(src, s) : -1
  if (e < 0) warn('meta is not an object literal')
  else {
    const lit = src.slice(s, e)
    const probs = pureLiteralProblems(lit)
    if (probs.length) warn(`meta is not a pure literal: ${probs.join(', ')}`)
    try { meta = vm.runInNewContext(`(${lit})`, {}) } catch (err) { warn(`meta does not evaluate: ${err.message}`) }
  }
}
const metaPhases = meta && Array.isArray(meta.phases) ? meta.phases.map(p => p && p.title) : []
if (meta) {
  if (typeof meta.name !== 'string' || !meta.name) warn('meta.name is missing')
  if (typeof meta.description !== 'string' || !meta.description) warn('meta.description is missing')
  console.log(`meta     ${meta.name} — ${meta.description}`)
  if (meta.whenToUse) console.log(`         when: ${meta.whenToUse}`)
  console.log(`phases   ${metaPhases.join(' · ') || '(none)'}`)
}
function codeOnly(text) {
  // blank out comments and string / template literals (newlines kept) so the line scan sees code only;
  // quote-strings stop at a newline, so a regex literal holding a quote cannot swallow the file
  const out = text.split('')
  const blank = (a, b) => { for (let k = a; k < b; k++) if (out[k] !== '\n') out[k] = ' ' }
  for (let i = 0; i < text.length; i++) {
    const c = text[i]
    if (c === '/' && text[i + 1] === '/') { const e = text.indexOf('\n', i); const end = e < 0 ? text.length : e; blank(i, end); i = end; continue }
    if (c === '/' && text[i + 1] === '*') { const e = text.indexOf('*/', i + 2); const end = e < 0 ? text.length : e + 2; blank(i, end); i = end - 1; continue }
    if (c === '"' || c === "'" || c === '`') {
      let j = i + 1
      while (j < text.length && text[j] !== c && !(c !== '`' && text[j] === '\n')) j += text[j] === '\\' ? 2 : 1
      blank(i + 1, Math.min(j, text.length)); i = j; continue
    }
  }
  return out.join('')
}
codeOnly(src).split('\n').forEach((code, i) => {
  if (/\bDate\.now\s*\(|\bMath\.random\s*\(|\bnew\s+Date\s*\(\s*\)/.test(code)) warn(`line ${i + 1}: Date.now() / Math.random() / new Date() throw in the Workflow runtime`)
  if (/^\s*import\s+(?:[\w*{][^;]*\bfrom\s+)?['"]|\brequire\s*\(|\bprocess\.|\bfs\./.test(code)) warn(`line ${i + 1}: no module, process or filesystem API in workflow scripts`)
})

// ---------------------------------------------------------------- fakes
function placeholder(key, idx) { return `<${key || 'value'}${idx === undefined ? '' : `-${idx + 1}`}>` }
function fake(schema, key, idx) {
  if (!schema || typeof schema !== 'object') return null
  if ('const' in schema) return schema.const
  if (Array.isArray(schema.enum) && schema.enum.length) return schema.enum[0]
  let t = schema.type
  if (Array.isArray(t)) t = t.find(x => x !== 'null') || 'null'
  if (!t) t = schema.properties ? 'object' : schema.items ? 'array' : null
  switch (t) {
    case 'object': return Object.fromEntries(Object.entries(schema.properties || {}).map(([k, s]) => [k, fake(s, k, idx)]))
    case 'array': return Array.from({ length: opt.items }, (_, i) => fake(schema.items || {}, key, i))
    case 'string': return opt.items ? placeholder(key, idx) : ''
    case 'number': case 'integer': return 0
    case 'boolean': return opt.bools === 'true' ? true : opt.bools === 'false' ? false : !NEGATIVE_BOOL.test(key || '')
    default: return null
  }
}
function shaped(schema, over, key) {
  // an answer merged over the schema: objects keep the fields the answer omits, arrays map item by item
  if (over === null || over === undefined || !schema || typeof schema !== 'object') return over
  const isObj = v => v && typeof v === 'object' && !Array.isArray(v)
  if (isObj(over) && (schema.type === 'object' || schema.properties)) {
    const base = fake(schema, key)
    for (const [k, v] of Object.entries(over)) base[k] = shaped(schema.properties && schema.properties[k], v, k)
    return base
  }
  if (Array.isArray(over) && (schema.type === 'array' || schema.items)) return over.map(v => shaped(schema.items, v, key))
  return over
}
function schemaProblems(s, where) {
  if (!s || typeof s !== 'object') return [`${where}: not an object`]
  const out = []
  const t = Array.isArray(s.type) ? s.type : [s.type]
  if (t.includes('object') || s.properties) {
    const props = s.properties || {}
    for (const r of s.required || []) if (!(r in props)) out.push(`${where}: required "${r}" is not in properties`)
    for (const [k, v] of Object.entries(props)) out.push(...schemaProblems(v, `${where}.${k}`))
  }
  if (t.includes('array')) {
    if (!s.items) out.push(`${where}: array without items`)
    else out.push(...schemaProblems(s.items, `${where}[]`))
  }
  return out
}

// ---------------------------------------------------------------- runtime stubs
const calls = []
const logs = []
const phasesSeen = new Set()
let currentPhase = null
let outDir = null
if (opt.out) {
  outDir = path.resolve(opt.out)
  fs.mkdirSync(outDir, { recursive: true })
  for (const f of fs.readdirSync(outDir)) if (/^\d{3,}-.*\.md$/.test(f)) fs.unlinkSync(path.join(outDir, f))
}
const indent = (text, pre) => text.split('\n').map(l => pre + l).join('\n')

function commonPrefix(a, b) {
  const n = Math.min(a.length, b.length)
  let i = 0
  while (i < n && a.charCodeAt(i) === b.charCodeAt(i)) i++
  return i
}
function showPrompt(prompt) {
  if (opt.quiet) return
  if (opt.full) { console.log(indent(prompt, '    │ ')); return }
  let from = 0
  let same = null
  for (const c of calls.slice(0, -1)) {
    const l = commonPrefix(c.prompt, prompt)
    if (l > from) { from = l; same = c }
  }
  if (from >= 200) {
    const nl = prompt.lastIndexOf('\n', from)
    from = nl > 0 ? nl + 1 : from
    console.log(`    │ [first ${from} chars identical to #${same.n} ${same.label}]`)
  } else from = 0
  const shown = prompt.slice(from, from + opt.chars)
  if (shown) console.log(indent(shown, '    │ '))
  const rest = prompt.length - from - shown.length
  if (rest > 0) console.log(`    │ … +${rest} chars (--full, or --out DIR for every prompt)`)
}
function checkPrompt(prompt, label) {
  const bad = [[/\bundefined\b/, 'undefined'], [/\[object Object\]/, '[object Object]'], [/\bNaN\b/, 'NaN']]
  for (const [re, what] of bad) {
    const m = re.exec(prompt)
    if (m) warn(`${label}: prompt contains "${what}" … ${JSON.stringify(prompt.slice(Math.max(0, m.index - 60), m.index + 40))}`)
  }
  if (opt.forbid) {
    const m = opt.forbid.exec(prompt)
    if (m) warn(`${label}: prompt matches --forbid (${JSON.stringify(m[0])}) … ${JSON.stringify(prompt.slice(Math.max(0, m.index - 60), m.index + 40))}`)
  }
}

async function agent(prompt, opts) {
  const o = opts || {}
  const n = calls.length + 1
  const label = o.label || `(no label #${n})`
  const ph = o.phase || currentPhase
  if (typeof prompt !== 'string') throw new TypeError(`agent(): the prompt must be a string (call #${n})`)
  if (!o.label) warn(`agent #${n}: no opts.label`)
  if (!o.phase) warn(`agent #${n} ${label}: no opts.phase (falls back to the global phase "${currentPhase}")`)
  if (ph && meta && !metaPhases.includes(ph)) warn(`agent #${n} ${label}: phase "${ph}" is not in meta.phases`)
  if (o.effort && !EFFORTS.has(o.effort)) warn(`agent #${n} ${label}: effort "${o.effort}" is not one of ${[...EFFORTS].join('/')}`)
  if (o.schema) {
    const probs = schemaProblems(o.schema, 'schema')
    if (o.schema.type !== 'object') probs.unshift('schema: the root must be {type: "object", properties: {...}}')
    if (probs.length) throw new Error(`agent ${label}: unsatisfiable schema: ${probs.join('; ')}`)
  }
  if (ph) phasesSeen.add(ph)
  const call = { n, label, phase: ph || null, schema: o.schema ? Object.keys(o.schema.properties || {}) : null, effort: o.effort || null, model: o.model || null, chars: prompt.length, prompt }
  calls.push(call)
  const extras = [o.effort && `effort=${o.effort}`, o.model && `model=${o.model}`, o.isolation && `isolation=${o.isolation}`, o.agentType && `agentType=${o.agentType}`].filter(Boolean).join(' ')
  console.log(`\n#${n} [${ph || '-'}] ${label}  ${call.schema ? `schema{${call.schema.join(',')}}` : 'text'}${extras ? '  ' + extras : ''}  (${prompt.length} chars)`)
  showPrompt(prompt)
  checkPrompt(prompt, label)
  if (outDir) {
    call.file = `${String(n).padStart(3, '0')}-${label.replace(/[^A-Za-z0-9._-]+/g, '_').slice(0, 80)}.md`
    fs.writeFileSync(path.join(outDir, call.file), `<!-- #${n} label: ${label} · phase: ${ph} · schema: ${call.schema ? call.schema.join(', ') : 'none'}${extras ? ' · ' + extras : ''} -->\n\n${prompt}\n`)
  }
  let result = o.schema ? fake(o.schema) : `(dry-run text result of ${label})`
  const rule = answers.find(r => r.re.test(label))
  if (rule) {
    let v = rule.value
    if (Array.isArray(v)) v = v[Math.min(rule.used, v.length - 1)]
    rule.used++
    result = v === null ? null : o.schema ? shaped(o.schema, v) : v
    console.log(`    → answer "${rule.key}"${Array.isArray(rule.value) ? ` (#${rule.used})` : ''}${result === null ? ': null (agent died)' : ''}`)
  }
  await Promise.resolve()
  return result === null ? null : JSON.parse(JSON.stringify(result))
}

async function parallel(thunks) {
  if (!Array.isArray(thunks)) throw new TypeError('parallel() expects an array of functions')
  if (thunks.length > 4096) throw new RangeError('parallel(): at most 4096 items')
  for (const t of thunks) if (typeof t !== 'function') throw new TypeError('parallel() expects an array of functions, not promises. Wrap each call: () => agent(...)')
  const settled = await Promise.allSettled(thunks.map(t => { try { return Promise.resolve(t()) } catch (e) { return Promise.reject(e) } }))
  return settled.map((r, i) => {
    if (r.status === 'fulfilled') return r.value
    warn(`parallel[${i}] failed: ${r.reason && r.reason.message ? r.reason.message : r.reason}`)
    return null
  })
}

async function pipeline(items, ...stages) {
  if (!Array.isArray(items)) throw new TypeError('pipeline() expects an array as the first argument')
  if (items.length > 4096) throw new RangeError('pipeline(): at most 4096 items')
  for (const s of stages) if (typeof s !== 'function') throw new TypeError('pipeline() stages must be functions: pipeline(items, item => ..., result => ...)')
  const settled = await Promise.allSettled(items.map(async (item, i) => {
    let v = await item
    for (const s of stages) {
      if (v === null) break
      v = await s(v, item, i)
    }
    return v
  }))
  return settled.map((r, i) => {
    if (r.status === 'fulfilled') return r.value
    warn(`pipeline[${i}] failed: ${r.reason && r.reason.message ? r.reason.message : r.reason}`)
    return null
  })
}

function phase(title) {
  currentPhase = String(title)
  phasesSeen.add(currentPhase)
  console.log(`\n== phase: ${currentPhase}`)
  if (meta && !metaPhases.includes(currentPhase)) warn(`phase("${currentPhase}") is not in meta.phases`)
}
function log(message) {
  const m = String(message)
  logs.push(m)
  console.log(`  log: ${m}`)
  if (/\bundefined\b|\[object Object\]|\bNaN\b/.test(m)) warn(`log line contains undefined / [object Object] / NaN: ${m}`)
}
const budget = { total: null, spent: () => 0, remaining: () => Infinity }
async function workflow() { throw new Error('workflow() is not supported in dry run (dry-run the child workflow on its own)') }
const consoleStub = { log: (...a) => { warn('console.log is not part of the workflow API (use log())'); console.log(...a) } }

// ---------------------------------------------------------------- run
// top-level args keys the script reads: a key it never reads is usually a misspelt option (the workflows mix
// snake_case and camelCase names, e.g. word_budget vs wordBudget) and would be ignored silently in a real run
const readKeys = new Set()
const argsSeen = args && typeof args === 'object' && !Array.isArray(args)
  ? new Proxy(args, {
    get(t, p, r) { if (typeof p === 'string') readKeys.add(p); return Reflect.get(t, p, r) },
    has(t, p) { if (typeof p === 'string') readKeys.add(p); return Reflect.has(t, p) },
  })
  : args
const context = vm.createContext({ agent, parallel, pipeline, phase, log, args: argsSeen, budget, workflow, console: consoleStub })
vm.runInContext(`(() => {
  const RealDate = Date
  const no = what => { throw new Error(what + ' is not available in workflow scripts (it would break resume); pass dates in args') }
  globalThis.Date = new Proxy(RealDate, {
    construct(t, a) { if (!a.length) no('new Date()'); return new t(...a) },
    apply() { no('Date()') },
    get(t, p) { return p === 'now' ? () => no('Date.now()') : Reflect.get(t, p) },
  })
  Math.random = () => no('Math.random()')
})()`, context)

const body = src.replace(/^export\s+const\s+meta\s*=/m, 'const meta =')
let script
try {
  script = new vm.Script(`(async () => {\n${body}\n})()`, { filename: WF_PATH, lineOffset: -1 })
} catch (e) {
  console.log(`\n✗ syntax error: ${e.message}`)
  console.log(String(e.stack).split('\n').slice(0, 4).join('\n'))
  process.exit(1)
}

let result
let failed = null
try {
  result = await script.runInContext(context)
} catch (e) {
  failed = e
}

// ---------------------------------------------------------------- report
if (failed) {
  console.log(`\n✗ the workflow threw: ${failed && failed.message ? failed.message : failed}`)
  const frames = String(failed && failed.stack || '').split('\n').filter(l => l.includes(WF_PATH)).slice(0, 5)
  if (frames.length) console.log(frames.join('\n'))
} else {
  console.log('\n== return value')
  console.log(result === undefined ? '(undefined: the script returns nothing)' : JSON.stringify(result, null, 2))
  const txt = JSON.stringify(result === undefined ? null : result)
  if (/\[object Object\]|\bNaN\b/.test(txt || '')) warn('the return value contains [object Object] or NaN')
}

if (argsSeen !== args) {
  const unread = Object.keys(args).filter(k => !readKeys.has(k) && !k.startsWith('_'))
  if (unread.length) warn(`args key(s) never read by the script in this run: ${unread.join(', ')} (misspelt? see the header comment of the workflow for its option names)`)
}
const byPhase = {}
calls.forEach(c => { byPhase[c.phase || '-'] = (byPhase[c.phase || '-'] || 0) + 1 })
const chars = calls.reduce((s, c) => s + c.chars, 0)
const biggest = calls.reduce((b, c) => (!b || c.chars > b.chars ? c : b), null)
const unreached = metaPhases.filter(p => !phasesSeen.has(p))
const unusedAnswers = answers.filter(r => !r.used).map(r => r.key)
console.log('\n== summary')
console.log(`agents   ${calls.length}${calls.length ? ` (${Object.entries(byPhase).map(([p, k]) => `${p} ${k}`).join(', ')})` : ''}`)
if (calls.length) console.log(`prompts  ${chars} chars (~${Math.round(chars / 4 / 1000)}k tokens of input); longest #${biggest.n} ${biggest.label} (${biggest.chars} chars)`)
console.log(`logs     ${logs.length}`)
if (unreached.length) console.log(`not reached with these args/fakes: ${unreached.join(', ')} (see --answers / --items / --bools)`)
if (unusedAnswers.length) console.log(`answers never used: ${unusedAnswers.join(', ')}`)
if (outDir) {
  fs.writeFileSync(path.join(outDir, 'calls.json'), JSON.stringify(calls.map(({ prompt, ...c }) => c), null, 1) + '\n')
  fs.writeFileSync(path.join(outDir, 'return.json'), JSON.stringify(failed ? { error: String(failed.message || failed) } : (result === undefined ? null : result), null, 1) + '\n')
  console.log(`written  ${calls.length} prompt file(s), calls.json and return.json in ${outDir}`)
}
console.log(warnings.length ? `warnings ${warnings.length}:\n${warnings.map(w => '  - ' + w).join('\n')}` : 'warnings none')
console.log(failed ? 'result   ✗ FAILED' : 'result   ✓ ran to the end')
process.exit(failed ? 1 : (opt.strict && warnings.length ? 2 : 0))
