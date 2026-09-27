#!/usr/bin/env bash
# team_commit.sh — commit a research-team path safely (research-team playbook, every checkpoint).
#
#   bash scripts/team_commit.sh <path> "<message>"
#
# Stages <path> (git add), then checks the WHOLE staging area: any PDF, PostScript, DjVu or EPUB file in any folder,
# any extracted txt/ file, or any file under a private/ folder other than private/README.md stops the commit
# (exit 3; nothing is committed and the offending files are listed). Copyrighted full texts and the user's private
# material never go into git, whatever .gitignore says (it misses slides and teams outside product/).
# Nothing staged → exit 0 with a note. Otherwise it commits with <message> and prints the commit line.
#
# Long stages (acquisition T3.2, reading T3.5, synthesis T3.6) run for hours in a container that can be recycled:
# commit a checkpoint every 30–60 minutes, e.g.
#   bash scripts/team_commit.sh product/<team> "wip(<team>): T3.5 checkpoint"
# Cards of finished batches are safe to commit mid-round; the round's Gate agent fixes the rest.
set -u
if [ $# -ne 2 ] || [ -z "$1" ] || [ -z "$2" ]; then
  echo "usage: bash scripts/team_commit.sh <path> \"<commit message>\"" >&2
  exit 2
fi
path=$1 msg=$2
if [ ! -e "$path" ]; then echo "❌ $path does not exist" >&2; exit 2; fi
git add -- "$path" || exit 1
bad=$(git diff --cached --name-only | grep -Ei '\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/' | grep -v '/private/README\.md$')
if [ -n "$bad" ]; then
  echo "STOP: these staged files must not be committed (copyrighted full texts or private material):" >&2
  echo "$bad" | sed 's/^/  /' >&2
  echo "Unstage them (git restore --staged <file>), add their pattern to .gitignore (or move them out of the repo), and rerun." >&2
  exit 3
fi
if git diff --cached --quiet; then
  echo "= nothing to commit under $path"
  exit 0
fi
git commit -q -m "$msg" && git log -1 --format='✅ committed %h %s'
