# Nonlinear Team · Personal Research Advisors

Research-craft skills distilled from the public work of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov, plus a roundtable skill that convenes them on your problem.

Field: continuous nonlinear optimization and NLP solver design (interior-point, SQP and active-set, trust-region and regularization, quasi-Newton, penalty / augmented-Lagrangian / filter globalization, complexity of first- and second-order methods); mixed-integer, global, derivative-free (see dfo-team) and conic first-order splitting traditions are not represented.

This selection follows the smooth NLP solver tradition (interior-point and SQP / active-set codes, trust-region and regularization methods, quasi-Newton updates, penalty, filter and funnel globalization, with Ye and Nesterov adding interior-point and complexity theory), while mixed-integer NLP, certified global optimization, derivative-free and noisy black-box optimization (the [DFO Team](../dfo-team/README.md)) and first-order splitting for LP, QP or conic problems too large to factorize are not represented; the roundtable's "Outside the Team" section says where to go instead and which members partly cover them.

## The Team

| Member | Lens · known for | Status |
|--------|------------------|--------|
| [Frank E. Curtis](frank-e-curtis/SKILL.md) | **Lens:** make the inner solve and the penalty or merit update serve the globalization, and prove it on instances built to break the solver.<br>**Known for:** [inexact SQP](https://doi.org/10.1137/060674004) and [infeasibility-detecting SQP](https://doi.org/10.1137/080738222) with Byrd and Nocedal; the penalty-interior-point code [PIPAL](https://doi.org/10.1007/s12532-012-0041-4); [SQP-GS](https://doi.org/10.1137/090780201) → [BFGS-SQP with relative minimization profiles](https://doi.org/10.1080/10556788.2016.1208749) (2018 INFORMS Computing Society Prize); the [TRACE](https://doi.org/10.1007/s10107-016-1026-2) trust region; [NonOpt](https://doi.org/10.1007/s12532-026-00322-5); co-author of the [SIAM Review survey on optimization for large-scale machine learning](https://doi.org/10.1137/16M1080173). | T1 base skill · base tier done |
| [Jorge Nocedal](jorge-nocedal/SKILL.md) | **Lens:** put the solver's received wisdom on trial with handicapped, method-level benchmarks; keep the classical engine and repair only the failing component, driven by an explicit estimate and a recovery path.<br>**Known for:** [L-BFGS](https://doi.org/10.1007/BF01589116) and L-BFGS-B ([2011 Remark](https://doi.org/10.1145/2049662.2049669)); [KNITRO](https://doi.org/10.1007/0-387-30065-1_4) with Byrd and Waltz; [*Numerical Optimization*](https://doi.org/10.1007/978-0-387-40065-5) with S. J. Wright; the [*Acta Numerica* 1992 theory survey](https://doi.org/10.1017/S0962492900002270); quasi-Newton methods for noisy functions ([2019](https://doi.org/10.1137/18M1177718)). | T1 base skill · base tier done |
| [Stephen J. Wright](stephen-j-wright/SKILL.md) | **Lens:** find where solver behaviour and theory disagree (degeneracy, finite precision, warm starts), show it on the smallest instance with heuristics off, borrow the fix from a neighbouring method class, and keep only safeguards that beat a no-safeguard twin on a fair benchmark.<br>**Known for:** [*Primal-Dual Interior-Point Methods*](https://doi.org/10.1137/1.9781611971453); *Numerical Optimization* with Nocedal; [stabilized SQP for degenerate solutions](https://doi.org/10.1023/A:1018665102534); [finite-precision analysis of interior-point methods](https://doi.org/10.1137/S1052623498347438); the LP/QP codes [PCx](https://doi.org/10.1080/10556789908805757) and [OOQP](https://doi.org/10.1145/641876.641880); [trust-region Newton-CG with complexity guarantees](https://doi.org/10.1137/19M130563X); [*Optimization for Data Analysis*](https://doi.org/10.1017/9781009004282) with Recht. | T1 base skill · base tier done |
| [Yinyu Ye](yinyu-ye/SKILL.md) | **Lens:** an LP interior-point theorist's lens: make the solver certify its own failures (homogenize or go one-phase), swap the costly inner step for a cheaper provable primitive, settle trusted heuristics by proof or smallest counterexample.<br>**Known for:** the [homogeneous self-dual LP algorithm](https://doi.org/10.1287/moor.19.1.53) with Todd and Mizuno; the books [*Interior Point Algorithms*](https://doi.org/10.1002/9781118032701) and [*Linear and Nonlinear Programming*](https://doi.org/10.1007/978-3-030-85450-8) (with Luenberger); [strongly polynomial simplex and policy iteration for fixed-discount MDPs](https://doi.org/10.1287/moor.1110.0516); the [one-phase nonconvex IPM](https://arxiv.org/abs/1801.03072) with Hinder; the [DRSOM](https://arxiv.org/abs/2208.00208) → [HSODM](https://doi.org/10.1287/moor.2023.0132) second-order line. | T1 base skill · base tier done |
| [Andreas Wächter](andreas-wachter/SKILL.md) | **Lens:** the maintainer-theorist of a general-purpose IPM: defaults provable, heuristics labelled and ablated, failures reduced to a model defect or a minimal counterexample, claims tested against the same code without its safeguards.<br>**Known for:** Ipopt: the [filter line-search method](https://doi.org/10.1137/S1052623403426556) and its [implementation paper](https://doi.org/10.1007/s10107-004-0559-y) with Biegler, and the C++ Ipopt 3.x with Laird (Wilkinson Prize 2011); the [2000 failure-of-global-convergence counterexample](https://doi.org/10.1007/PL00011386); the [inexact-step IPM](https://doi.org/10.1137/090747634) with Curtis and Schenk; [two-stage decomposition for AC optimal power flow](https://doi.org/10.1109/TPWRS.2020.3002189). At [Gurobi](https://www.gurobi.com/) since late 2024. | T1 base skill · base tier done |
| [Philip E. Gill](philip-e-gill/SKILL.md) | **Lens:** the linear system decides the method: well-pose each subproblem by the smallest change that keeps the solution, keep warm starts and infeasibility detection, test on whole collections with every failure typed.<br>**Known for:** [SNOPT](https://doi.org/10.1137/S1052623499350013) with Murray and Saunders ([SIGEST 2005](https://doi.org/10.1137/S0036144504446096)); *Practical Optimization* (1981, with Murray and M. H. Wright; [SIAM reprint](https://doi.org/10.1137/1.9781611975604)); the [1986 projected-Newton-barrier / Karmarkar equivalence](https://doi.org/10.1007/BF02592025); the [interior-methods survey](https://doi.org/10.1137/S0036144502414942); [globalized stabilized SQP](https://doi.org/10.1137/120882913) and the shifted penalty-barrier line; an [LDLᵀ trust-region quasi-Newton method](https://doi.org/10.1137/23M1623380). All co-authored, with alphabetical author order. | T1 base skill · base tier done |
| [Philippe L. Toint](philippe-l-toint/SKILL.md) | **Lens:** let Newton be Newton, then try to break your own bound: the least obstructive safeguard that keeps a proof, a constructed function attaining the bound, and defaults settled by one-change experiments on a validated shared collection.<br>**Known for:** co-author of [LANCELOT](https://doi.org/10.1007/978-3-662-12211-2) (1994 Beale–Orchard-Hays Prize), [CUTE](https://doi.org/10.1145/200979.201043) → [CUTEst](https://doi.org/10.1007/s10589-014-9687-3) and [*Trust-Region Methods*](https://doi.org/10.1137/1.9780898719857); [adaptive cubic regularization (ARC)](https://doi.org/10.1007/s10107-009-0286-5) and the [evaluation-complexity book](https://doi.org/10.1137/1.9781611976991) with Cartis and Gould; [filter-SQP convergence theory](https://doi.org/10.1137/S105262340038081X) (2006 Lagrange Prize with Fletcher and Leyffer); the [trust funnel](https://doi.org/10.1007/s10107-008-0244-7); [S2MPJ](https://doi.org/10.1080/10556788.2025.2490640), most of whose code he writes himself. | T1 base skill · base tier done |
| [Nicholas I. M. Gould](nicholas-i-m-gould/SKILL.md) | **Lens:** find the dominant inner solve (KKT, QP, trust-region subproblem) and make it truncatable. Judge changes in one harness, on the whole collection at defaults, with mid-run instances. Promote only survivors. Drop a route in print when rivals' benchmarks say it has peaked.<br>**Known for:** co-author of LANCELOT, [GALAHAD](https://doi.org/10.1145/962437.962438) and CUTE → CUTEst (with Conn, Toint, Orban) and of the books *Trust-Region Methods* (2000) and *Evaluation Complexity* (2022); the trust-region subproblem solvers [GLTR](https://doi.org/10.1137/S1052623497322735), [TRS/RQS](https://doi.org/10.1007/s12532-010-0011-7) and [TREK](https://arxiv.org/abs/2511.11135); ARC with Cartis and Toint; at Harwell/RAL since 1985. | T1 base skill · base tier done |
| [Roger Fletcher](roger-fletcher/SKILL.md) | **Lens:** let Newton run: measure what safeguards throw away, add the least protection that still guarantees convergence, trust nothing not computed in finite precision in your own code.<br>**Known for:** [DFP](https://doi.org/10.1093/comjnl/6.2.163) (with Powell, 1963), [Fletcher–Reeves](https://doi.org/10.1093/comjnl/7.2.149) (1964) and [BFGS](https://doi.org/10.1093/comjnl/13.3.317) (1970); Sl1QP exact-penalty SQP and [SLP-EQP](https://doi.org/10.1007/BF01582292); the [filter method](https://doi.org/10.1007/s101070100244) with Leyffer (2006 Lagrange Prize); [*Practical Methods of Optimization*](https://doi.org/10.1002/9781118723203); [projected Barzilai–Borwein](https://doi.org/10.1007/s00211-004-0569-y) (with Dai), [limited-memory steepest descent](https://doi.org/10.1007/s10107-011-0479-6) and [SLCP](https://doi.org/10.1137/110844362) with the filterSD code. Historical lens (1939–2016). | T1 base skill · base tier done |
| [Yurii Nesterov](yurii-nesterov/SKILL.md) | **Lens:** structure and complexity: which class is provably easy, what one iteration costs in affordable operations, how far the rate is from the lower bound, which constants the user cannot know.<br>**Known for:** the [1983 fast gradient method](https://www.mathnet.ru/eng/dan46009); [self-concordant polynomial-time interior-point theory](https://doi.org/10.1137/1.9781611970791) with Nemirovskii; [smoothing](https://doi.org/10.1007/s10107-004-0552-5); [cubic regularization of Newton's method](https://doi.org/10.1007/s10107-006-0706-8) with Polyak; [implementable tensor methods](https://doi.org/10.1007/s10107-019-01449-1); [super-universal regularized Newton](https://doi.org/10.1137/22M1519444); [*Lectures on Convex Optimization*](https://doi.org/10.1007/978-3-319-91578-4). A theorist who never released a solver; 2009 von Neumann Prize (shared with Ye), 2026 Gauss Prize. | T1 base skill · base tier done |
| [`nonlinear-roundtable`](nonlinear-roundtable/SKILL.md) | Convenes the members to discuss your problem and produce a plan | roundtable |

Each lens is the "Lens (one line)" of that member's `## Roundtable Card`; "known for" is taken from each `SKILL.md` (its introduction and Signature Work Anatomy) and its research notes, with links checked against Crossref, arXiv or the page itself. Status from `python3 scripts/team_status.py product/nonlinear-team`. No member has a **student mode** (proof playbook, open problems, reading path, pre-meeting review).

## Install (Claude Code)

Copy every skill folder into your skills directory. The roundtable finds its members as sibling folders, so install all of them together.

```bash
# macOS / Linux — global install
for d in product/nonlinear-team/*/; do cp -r "$d" ~/.claude/skills/; done
```
```powershell
# Windows PowerShell
Get-ChildItem product\nonlinear-team -Directory | ForEach-Object { Copy-Item -Recurse $_.FullName "$HOME\.claude\skills\" }
```

Restart Claude Code so it picks up the new skills.

## Use

**Convene the whole team on a problem:**

```
> Nonlinear Team: our interior-point NLP solver (filter line search, LDLᵀ with inertia correction) fails on 30 of our 400
  regression models, mostly in restoration, and calls 2 feasible ones infeasible. Two engineers, six months; defaults must not change.
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
| `@Gould …` / `@all …` | Ask one member, or every seated member |
| `add Toint` / `drop Ye` | Change who is seated |
| `pursue 2` / `round` | Pick the disagreement / run another round |
| `plan` / `autopilot` | Go to the plan now / run to the draft plan without stopping |
| `stop` | End the roundtable |

Surnames match without diacritics (`@Waechter` or `@Wachter` = Wächter). Anything else you type is passed to the seated members as new information. At the end the moderator offers to save the transcript as a markdown file.

Cost: one agent call per member per turn — about 3 per round with default seating. Runtimes without subagents fall back to a single-model simulation, and the moderator says so.

**Other modes:**

```
> Nonlinear Team, quick: …                                            # best-fit 1–2 members, straight to plan
> Nonlinear Team, debate Fletcher vs Nocedal: filter or adaptive penalty for our SQP?   # two lenses argue one decision
> Use the Wächter lens on my failing run's iteration log and our restoration-phase options
> How would Gould handle a KKT factorization that takes most of each iteration?   # a single member directly
```

Say "exit" or "end roundtable" to return to normal mode.

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

The technique catalog, `cards/`, 07–09, `publications/works.json` and `scholar.md`, and `papers/` come from the deep reading. **This team is base tier: no deep reading has been done, so those files are absent** (see [DEEP-READING.md](DEEP-READING.md)). Each skill has `SKILL.md`, the notes 01–06 and `RESOURCES.md`; its `publications/` folder holds the OpenAlex pull the notes started from (`publications.md`, `abstracts.md`): raw material, not an audited publication list. Five members also have saved talk transcripts or interview notes under `talks/` (Nocedal, Wright, Gill, Toint, Fletcher). A member with a student mode would also have `proof-playbook.md`, `open-problems.md` and `reading-path.md` under `references/`; none has one yet. No `private/` folder is ever published.

To add a resource later, add a row to that researcher's `RESOURCES.md` and drop the file into the matching folder. If the resource changes a method, update the research note and `SKILL.md`. To add full texts and paper cards, run the deep tier (stages T3.1–T3.8 of the [research-team playbook](../../references/research-team-playbook.md)); [DEEP-READING.md](DEEP-READING.md) then becomes the record of it.

This team is configured by [team.json](team.json). To build another team like it, or to update this one, use the generic kit in this repository (`scripts/new_team.py`, the saved workflows in `scripts/workflows/`): see the [research-team playbook](../../references/research-team-playbook.md).

## Honest Boundary

- These are simulated lenses built from public work, not the researchers' own views.
- The research was done from web search results in September 2026, without full-text reading of the members' publication lists (single papers, theses, slides and transcripts were opened where the notes needed them); each skill's Honest Boundary lists its gaps and `RESOURCES.md` marks unverified leads ⚠️.
- Fletcher (d. 2016) is a historical lens; the skill reflects work up to then.
- Treat every recommendation as a hypothesis to test on your problem.
