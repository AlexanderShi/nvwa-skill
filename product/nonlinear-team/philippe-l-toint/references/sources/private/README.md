<!-- Team template (private folder rule) → product/<team>/<member>/references/sources/private/README.md.
     T0: scripts/new_team.py writes it for every member and fills the double-brace placeholders. No workflow reads or fills this folder.
     .gitignore keeps the rest of the folder out of git: "product/**/references/sources/private/*" plus
     "!product/**/references/sources/private/README.md". Check with: git check-ignore -v <file in private/>.
     See product/dfo-team for a worked example (a student-mode member's private/README.md). -->

# Private materials (git-ignored)

Everything in this folder except this README is ignored by git, so it never reaches the public repository.

Put material here that comes from your own work with Philippe L. Toint and is not public, for example:

- lecture notes and slides from courses or reading groups
- comments on your drafts, proofs, designs or talks
- notes from group or one-on-one meetings
- unpublished drafts you co-authored

Nothing here is read by the research or deep-reading workflows, and the `philippe-l-toint` skill opens this folder only when you have added material and ask it to use it. If the skill has a student mode, it then treats these as its highest-priority sources, and it never quotes them outside your own conversation.

Good practice: this is someone else's unpublished feedback. Keep it private, and consider telling the person it came from that you use it this way.

Suggested layout:

```
private/
├── lectures/
├── feedback/        # one file per draft, e.g. 2026-10-paper1-comments.md
├── meetings/
└── drafts/
```

Philippe L. Toint's actual feedback always overrides anything the skill infers from public work.
