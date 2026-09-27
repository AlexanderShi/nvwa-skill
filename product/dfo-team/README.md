# DFO Team · Personal Derivative-Free Optimization Advisors

Five research-craft skills distilled from leading researchers in derivative-free optimization (DFO), plus a roundtable skill that convenes them on your problem.

This selection follows the mathematical-optimization tradition of DFO; Bayesian optimization and evolutionary methods are not represented.

## The Team

| Skill | Researcher | Known for | Folder |
|-------|-----------|-----------|--------|
| `michael-powell` (Powell.skill) | Michael J. D. Powell | COBYLA, UOBYQA, NEWUOA, BOBYQA, LINCOA; practical model-based DFO | [michael-powell/](michael-powell/) |
| `andrew-conn` (Conn.skill) | Andrew R. Conn | Trust-region methods; model-based DFO theory; *Introduction to Derivative-Free Optimization* | [andrew-conn/](andrew-conn/) |
| `katya-scheinberg` (Scheinberg.skill) | Katya Scheinberg | Model-based and stochastic DFO; probabilistic models. Has a **student mode** (proof playbook, open problems, reading path, pre-meeting review) | [katya-scheinberg/](katya-scheinberg/) |
| `luis-nunes-vicente` (Vicente.skill) | Luís Nunes Vicente | Direct search; convergence and worst-case complexity | [luis-nunes-vicente/](luis-nunes-vicente/) |
| `charles-audet` (Audet.skill) | Charles Audet | MADS, NOMAD; blackbox and constrained optimization | [charles-audet/](charles-audet/) |
| `dfo-roundtable` | — | Convenes the five to discuss your problem and produce a plan | [dfo-roundtable/](dfo-roundtable/) |

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all six together.

```bash
# macOS / Linux — global install
for d in product/dfo-team/*/; do cp -r "$d" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\dfo-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> DFO team: I'm calibrating a groundwater simulator, 12 parameters with bounds,
  each run takes 20 minutes and sometimes crashes. Budget is ~500 runs.
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
| `@Powell …` / `@all …` | Ask one member, or every seated member |
| `add Conn` / `drop Vicente` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> DFO team, quick: …                        # best-fit 1–2 members, straight to plan
> DFO team, debate Powell vs Audet: …       # two lenses argue one decision
> Use the Vicente lens on my convergence proof
> How would Scheinberg handle noise here?   # a single member directly
```

Say "exit" or "end roundtable" to return to normal mode.

**Technique catalogs.** Each skill has a `references/technique-catalog.md`. It lists the proof devices, algorithm-design moves, experiment protocols and writing moves found by reading that researcher's papers in full. Each entry has a one-line "how to use it" and the paper cards, with pages, that it rests on. Powell's, Conn's and Audet's `SKILL.md` steps cite entries by id (e.g. E6, P1); Scheinberg's and Vicente's point to catalog sections. You can also ask for the catalog directly:

```
> Which of Powell's proof devices fit my interpolation-model argument?
> Audet lens: which experiment protocol should I use to benchmark my blackbox solver?
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
        │   ├── works.json               # complete Google Scholar list, cross-checked (DBLP, Crossref, arXiv)
        │   └── scholar.md               # the same list, readable, with audit notes
        ├── papers/
        │   ├── INDEX.md                 # every work: full-text status, role, read level
        │   ├── abstracts.json           # abstracts (arXiv / Crossref)
        │   ├── *.pdf                    # open full texts (git-ignored)
        │   └── txt/                     # extracted text with [[page N]] markers (git-ignored)
        ├── talks/                       # transcripts, slides, lecture notes
        ├── essays/                      # methodology writings, surveys
        └── software/                    # solver notes and links
```

`katya-scheinberg/references/` also holds the student-mode files: `proof-playbook.md`, `open-problems.md` and `reading-path.md`. Her git-ignored `sources/private/` folder is never published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add a paper's full text, follow "How to extend" in [DEEP-READING.md](DEEP-READING.md).

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research started from web search results in 2026-09. On 2026-09-27 it was deepened by reading each researcher's Google Scholar publications in full or in part wherever an open copy exists. Coverage, from each `papers/INDEX.md` (details in [DEEP-READING.md](DEEP-READING.md)):

  | Researcher | Works indexed | Read in full / in part | Abstract or metadata only (incl. unreadable) | Skipped (not the author's, or not research) |
  |---|---|---|---|---|
  | Powell | 187 | 34 / 5 | 148 | 0 |
  | Conn | 183 | 53 / 18 | 67 | 45 |
  | Scheinberg | 132 | 68 / 14 | 42 | 8 |
  | Vicente | 124 | 92 / 16 | 16 | 0 |
  | Audet | 212 | 109 / 6 | 78 | 19 |

  Powell's 34 full reads include his two interviews and the Royal Society memoir of him (by Buhmann, Fletcher, Iserles and Toint). Works without an open full text are known from their abstract or metadata only. These include most of Powell's pre-1994 papers and the bodies of the major books: *Trust-Region Methods*, *LANCELOT*, *Introduction to Derivative-Free Optimization* and Audet–Hare. What is openly available of two of those books was also read. For *Introduction to Derivative-Free Optimization* that is the table of contents, the errata, the 2011 addendum and two published reviews (Nazareth, Orban). For Audet–Hare it is the 2nd-edition preface and contents. Each skill's Honest Boundary lists its gaps, and `RESOURCES.md` marks unverified leads ⚠️.
- Powell (d. 2015) and Conn (d. 2019) are historical lenses; their skills reflect work up to then.
- Treat every recommendation as a hypothesis to test on your problem.
