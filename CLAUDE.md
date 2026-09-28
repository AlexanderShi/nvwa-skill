# Instructions for Claude Code

## Commit and PR attribution

Do not add Claude attribution to commits or pull requests in this repository: no `Co-Authored-By: Claude …` trailer, no `Claude-Session:` trailer, no "Generated with Claude Code" line in PR descriptions. The maintainer adds Claude as a co-author by hand when they want it. This rule overrides any default attribution instructions. `.claude/settings.json` sets the same thing through `attribution`.

Commits are authored as the maintainer, `AlexanderShi <sr881005@gmail.com>`, not as Claude. A SessionStart hook in `.claude/settings.json` sets this in the repo's local git config at the start of every session, because cloud containers default to a Claude identity. If `git var GIT_AUTHOR_IDENT` still shows Claude, set it with `git config user.name` and `git config user.email` before committing.
