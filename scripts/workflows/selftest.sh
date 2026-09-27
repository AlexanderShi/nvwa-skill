#!/usr/bin/env bash
# selftest.sh — self-test of the research-team kit (run after changing any workflow or kit script; no tokens spent).
#
#   bash scripts/workflows/selftest.sh [product/<finished team>]      e.g. product/dfo-team, the worked example
#
# Without a team only parts 1 (no --forbid) and 3 (without team_check.py) run; give a finished team for the full test.
# 1. The nine example previews (examples/*.args.json + *.answers.json) with dry_run.mjs --strict, plus the variants that
#    take other branches (base-tier team-layer; team-synthesize / team-increment resumed with from: "review" / "fix").
#    --forbid is built from the finished team's team.json (team and roundtable slugs, member surnames), so nothing of
#    that team may leak into the generic workflows.
# 2. make_args.mjs for every workflow on the finished team, and dry_run.mjs --team <team> (no args file) --strict for
#    every workflow: the args a real launch would get.
# 3. Every kit script compiles and answers --help; team_status.py --coverage runs; team_check.py <team> exits 0
#    (the delivery gate: links, templates, git, roundtable, coverage tables, 12/12, quotes, ledgers, works).
# Read-only against the repo: dry runs write nothing, scratch output goes to a temporary folder that is removed.
# Exit code: the number of failed checks (0 = all passed).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/../.." && pwd)
cd "$REPO" || exit 99
TEAM=${1:-}
TMP=$(mktemp -d "${TMPDIR:-/tmp}/nuwa-selftest.XXXXXX")
trap 'rm -rf "$TMP"' EXIT
fail=0
ok() { printf '  ✓ %s\n' "$1"; }
bad() { printf '  ✗ %s\n' "$1"; fail=$((fail + 1)); }
WF="base-skills layer harvest chase read synthesize tighten increment integrate"

FORBID='$^'   # matches nothing
if [ -n "$TEAM" ]; then
  [ -f "$TEAM/team.json" ] || { echo "❌ $TEAM/team.json not found"; exit 99; }
  FORBID=$(python3 - "$TEAM/team.json" <<'PY'
import json, re, sys
t = json.load(open(sys.argv[1]))
words = {t["team"], t["roundtable"]} | {m.get("surname") or m["name"].split()[-1] for m in t["members"]}
print(r"\b(" + "|".join(sorted(re.escape(w) for w in words if len(w) > 2)) + r")\b")
PY
)
  echo "kit self-test · finished team $TEAM · forbid $FORBID"
else
  echo "kit self-test · no finished team given (parts 2 and team_check.py skipped; e.g. bash $0 product/dfo-team)"
fi

echo "1. example previews (strict)"
dry() {  # label, workflow, args (file or inline JSON), answers file
  local out rc
  out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$2.js" "$3" --answers "$4" --quiet --strict --forbid "$FORBID" 2>&1)
  rc=$?
  if [ $rc -eq 0 ]; then ok "$1 ($(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g'))"; else bad "$1 (exit $rc)"; grep -E '^  - |✗' <<<"$out" | head -5; fi
}
for w in $WF; do
  dry "team-$w" "$w" "scripts/workflows/examples/team-$w.args.json" "scripts/workflows/examples/team-$w.answers.json"
done
dry "team-layer deep_tier false" layer "$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));d["deep_tier"]=False;print(json.dumps(d))' scripts/workflows/examples/team-layer.args.json)" scripts/workflows/examples/team-layer.answers.json
for w in synthesize increment; do
  for f in review fix; do
    a=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));d["from"]=sys.argv[2];[d.pop(k,None) for k in ("find","since","what")];print(json.dumps(d))' "scripts/workflows/examples/team-$w.args.json" "$f")
    dry "team-$w from $f" "$w" "$a" "scripts/workflows/examples/team-$w.answers.json"
  done
done

[ -n "$TEAM" ] && echo "2. make_args.mjs and dry_run.mjs --team on $TEAM"
for w in $WF; do
  [ -n "$TEAM" ] || break
  if node scripts/workflows/make_args.mjs "team-$w" --team "$TEAM" --date 2026-01-01 --scratch "$TMP/scratch" > "$TMP/calls-$w.json" 2>/dev/null \
     && python3 -c 'import json,sys;c=json.load(open(sys.argv[1]));assert c and all(x["args"]["members"] for x in c)' "$TMP/calls-$w.json"; then
    out=$(node scripts/workflows/dry_run.mjs "scripts/workflows/team-$w.js" --team "$TEAM" --scratch "$TMP/scratch" --quiet --strict 2>&1)
    rc=$?
    if [ $rc -eq 0 ]; then ok "team-$w: $(python3 -c 'import json,sys;print(len(json.load(open(sys.argv[1]))))' "$TMP/calls-$w.json") call(s); preview $(grep -m1 '^agents' <<<"$out" | sed 's/  */ /g')"
    else bad "team-$w: dry_run --team exit $rc"; grep -E '^  - |✗' <<<"$out" | head -5; fi
  else bad "team-$w: make_args.mjs failed"; fi
done

echo "3. scripts and the delivery gate"
for f in scripts/*.py; do
  python3 -m py_compile "$f" 2>/dev/null || { bad "py_compile $f"; continue; }
  case $(basename "$f") in
    merge_research.py|mark_read_from_cards.py|srt_to_transcript.py|quality_check.py) continue ;;  # no argparse --help
  esac
  python3 "$f" --help > /dev/null 2>&1 || bad "$f --help"
done
ok "py_compile + --help"
bash -n scripts/team_commit.sh && ok "team_commit.sh parses" || bad "team_commit.sh does not parse"
if [ -n "$TEAM" ]; then
  python3 scripts/team_status.py "$TEAM" --coverage > /dev/null && ok "team_status.py --coverage" || bad "team_status.py --coverage"
  out=$(python3 scripts/team_check.py "$TEAM" 2>&1); rc=$?
  if [ $rc -eq 0 ]; then ok "team_check.py: $(tail -1 <<<"$out")"; else bad "team_check.py exit $rc"; grep '✗' <<<"$out" | head -8; fi
fi

echo "self-test: $([ $fail -eq 0 ] && echo "✅ all passed" || echo "❌ $fail failed")"
exit $fail
