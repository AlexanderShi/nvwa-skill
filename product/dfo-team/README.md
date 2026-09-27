# DFO Team · Personal Derivative-Free Optimization Advisors

Five research-craft skills distilled from leading researchers in derivative-free optimization (DFO), plus a roundtable skill that convenes them on your problem.

This selection follows the mathematical-optimization tradition of DFO; Bayesian optimization and evolutionary methods are not represented.

## The Team

| Skill | Researcher | Known for | Folder |
|-------|-----------|-----------|--------|
| `michael-powell` (Powell.skill) | Michael J. D. Powell | COBYLA, UOBYQA, NEWUOA, BOBYQA, LINCOA; practical model-based DFO | [michael-powell/](michael-powell/) |
| `andrew-conn` (Conn.skill) | Andrew R. Conn | Trust-region methods; model-based DFO theory; *Introduction to Derivative-Free Optimization* | [andrew-conn/](andrew-conn/) |
| `katya-scheinberg` (Scheinberg.skill) | Katya Scheinberg | Model-based and stochastic DFO; probabilistic models | [katya-scheinberg/](katya-scheinberg/) |
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

## Resources

Each researcher has a folder that keeps track of the resources behind that skill:

```
<researcher>/
├── SKILL.md                         # the research skill
└── references/
    ├── research/                    # six research notes (publications, stated method,
    │                                #   process evidence, mentorship, critique, trajectory)
    └── sources/
        ├── RESOURCES.md             # tracker: every source, verified ✅ or lead ⚠️, where it was used
        ├── publications/            # publication landscape
        ├── papers/                  # full texts you download (PDFs are git-ignored)
        ├── talks/                   # transcripts, slides, lecture notes
        ├── essays/                  # methodology writings, surveys
        └── software/                # solver notes and links
```

To add a resource later: add a row to that researcher's `RESOURCES.md`, drop any file into the matching folder, and if it changes a method, update the research note and `SKILL.md`.

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- Research was done through web search results in 2026-09 without full-text reading; each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️.
- Powell (d. 2015) and Conn (d. 2019) are historical lenses; their skills reflect work up to then.
- Treat every recommendation as a hypothesis to test on your problem.
