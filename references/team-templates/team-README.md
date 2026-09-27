<!-- Team template (team README) → product/<team>/README.md.
     T0: scripts/new_team.py fills the double-brace placeholders and the member rows of The Team.
     T2: scripts/workflows/team-layer.js fills the lens column, the scope line, the Use examples and the base-tier Honest Boundary.
     T3.8: scripts/workflows/team-integrate.js adds the technique-catalog paragraph and the five-column coverage summary,
           pasted unchanged from python3 scripts/team_status.py <team dir> --coverage --short. The script sums it from
           the full --coverage table, which goes unchanged into DEEP-READING.md, so the two always agree.
     No TODO item may remain after T2 (base tier: team-layer.js deletes the deep-tier-only parts) or after T3.8 (deep tier).
     Open work: grep -n "TODO" README.md. See product/dfo-team for a worked example (README.md). -->

# {{TEAM_TITLE}} · Personal Research Advisors

Research-craft skills distilled from the public work of {{MEMBER_LIST}}, plus a roundtable skill that convenes them on your problem.

Field: {{FIELD}}.

[TODO: one sentence on scope: which tradition of the field this selection follows, and which neighbouring traditions are not represented; from the T0 scope decision; team-layer.js (T2)]

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
{{MEMBER_TABLE}}
| `{{ROUNDTABLE_SLUG}}` | Convenes the members to discuss your problem and produce a plan | roundtable |

[TODO: after T1, replace each "lens: …" cell with the member's one-line lens and what they are known for (signature works, software, books), and each status cell with the member's stage from `python3 scripts/team_status.py product/{{TEAM_SLUG}}`; mark any member with a **student mode** (proof playbook, open problems, reading path, pre-meeting review); team-layer.js (T2), refreshed by team-integrate.js (T3.8). Then delete this line.]

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all of them together.

```bash
# macOS / Linux — global install
for d in product/{{TEAM_SLUG}}/*/; do cp -r "$d" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\{{TEAM_SLUG}} -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> {{TEAM_TITLE}}: [TODO: a realistic two-line problem from the field, with the budget, constraints and
  failure modes a member would ask about; team-layer.js (T2)]
```

Each seated member runs as **its own agent** that reads its own skill file; the main session moderates. You chair the discussion — it pauses at four checkpoints:

| Checkpoint | You see | You can |
|-----------|---------|---------|
| 1 · Card and seats | Problem Card, who sits and why | Correct the card, change seats, answer ≤2 questions |
| 2 · After openings | Each member's position, first experiment, risk; agreements and splits | Answer members' questions, ask anyone, pick the disagreement to argue |
| 3 · After each round | Both sides' replies and the test that would settle the point | Another round, bring someone in, or move to the plan |
| 4 · Draft plan | Plan with each member's sign-off or dissent | Approve, change, or reopen a point (never skipped) |

**Controls** (any time):

| Say | Effect |
|-----|--------|
| `go` | Accept the default and continue |
| `@<Surname> …` / `@all …` | Ask one member, or every seated member |
| `add <Surname>` / `drop <Surname>` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> {{TEAM_TITLE}}, quick: …                          # best-fit 1–2 members, straight to plan
> {{TEAM_TITLE}}, debate <Surname> vs <Surname>: …  # two lenses argue one decision
> Use the <Surname> lens on my [TODO: a typical artefact in this field, e.g. draft, design, analysis plan; team-layer.js (T2)]
> How would <Surname> handle [TODO: a typical sub-problem; team-layer.js (T2)]?   # a single member directly
```

Say "exit" or "end roundtable" to return to normal mode.

**Technique catalogs.** [TODO: keep this paragraph only once the deep tier (T3) is done; team-integrate.js (T3.8).] Each skill has a `references/technique-catalog.md`. It lists the transferable devices found by reading that researcher's papers in full ([TODO: the catalog's groups, e.g. proof devices, design moves, experiment protocols, writing moves]). Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. [TODO: which members' `SKILL.md` steps cite catalog entries by id and which point to catalog sections.] You can also ask for the catalog directly:

```
> [TODO: two example requests, each naming a member lens and a catalog group; team-integrate.js (T3.8)]
```

## Resources

Each researcher has a folder that keeps track of the resources behind that skill:

```
<researcher>/
├── SKILL.md                             # the research skill (links into the evidence ledger)
└── references/
    ├── technique-catalog.md             # transferable devices from the papers, each with card pages
    ├── research/
    │   ├── 01- … 06-*.md                # six research notes (publications, stated method, process
    │   │                                #   evidence, mentorship, critique, trajectory)
    │   ├── cards/<batch>.md             # paper cards: D1–D8, method links, verified quotes, page refs
    │   ├── cards/<batch>.digest.json    # the same cards, machine-readable
    │   ├── 07-paper-cards.md            # card index: one row per work, read level, methods linked
    │   ├── 08-deep-reading-synthesis.md # patterns, promotions and corrections drawn from all cards
    │   └── 09-evidence-ledger.md        # full evidence behind each SKILL.md item
    └── sources/
        ├── RESOURCES.md                 # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/
        │   ├── works.json               # complete publication list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        ├── software/                    # notes on the researcher's software and code
        └── private/                     # git-ignored; only its README is tracked
```

The technique catalog, `cards/`, 07–09, `publications/` and `papers/` come from the deep reading (see [DEEP-READING.md](DEEP-READING.md)); a base-tier skill has only `SKILL.md`, the notes 01–06 and `RESOURCES.md`. A member with a student mode also has `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- [TODO: the research basis. Base tier (team-layer.js, T2): "The research was done from web search results in <month year>, without full-text reading; each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️." Deep tier (team-integrate.js, T3.8): "The research started from web search results in <month year>. On <date> it was deepened by reading each researcher's publications in full or in part wherever an open copy exists. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):" followed by the table below.]

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | [TODO: replace this header, its separator and this row with the output of `python3 scripts/team_status.py product/{{TEAM_SLUG}} --coverage --short`, pasted unchanged (the same five columns, one row per member by surname; the script sums Distinct works indexed, Read in full / in part, Abstract only + Metadata only, and Skipped from the full --coverage table). Never type a number. team-integrate.js (T3.8); team-layer.js (T2) deletes the table at the base tier.] | | | | |

  [TODO: after the table: what is not openly available (book bodies, early papers), which openly available parts of books were read (T4 increments), and any special items counted among the full reads (interviews, memoirs). End with: "Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️." team-integrate.js (T3.8); deleted with the table at the base tier.]
- [TODO: historical lenses: for each member with `"living": false` in `team.json`, "<Surname> (d. YYYY) is a historical lens; the skill reflects work up to then." Delete if every member is living; team-layer.js (T2).]
- Treat every recommendation as a hypothesis to test on your problem.
