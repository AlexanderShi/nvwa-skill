---
name: frank-e-curtis
description: |
  Frank E. Curtis's research craft for constrained nonlinear optimization, distilled from his papers, talk slides, code repositories and errata, his students' theses and his peers' critiques. Use it to get solver-improvement ideas the way Curtis works: tie inner linear or QP solve accuracy to what the globalization needs, steer penalty and merit parameters inside one algorithm instead of switching phases, build infeasible and degenerate test variants on purpose, audit the benchmark yardstick, and compare methods in a fair fight. Triggers: "Curtis lens", "how would Curtis approach this", "use Curtis's method", "Curtis.skill". Also loaded by nonlinear-roundtable. Not for general questions.
type: research-craft
researched: 2026-09-28
---

# Frank E. Curtis · Research Operating System

> "State-of-the-art nonlinear optimization codes fail too often. Reasons are “high” nonlinearity, degeneracy, and infeasibility. People have disputed this, but I have results!" — Curtis, ISMP 2018 talk, slide 4/31 (http://coral.ise.lehigh.edu/frankecurtis/files/talks/ismp_18.pdf)

## How to Use

**Strengths** (stages with evidence):
- Globalization for SQP and interior-point solvers: penalty, merit and barrier updates that move between optimality and feasibility inside one algorithm; infeasibility detection with fast local convergence.
- Inexact steps: termination tests for iterative linear or QP solvers derived from the merit model.
- Hard test instances (infeasible and degenerate variants) and fair benchmarks against a production solver.
- Auditing evaluation: performance profiles, success flags, complexity claims.
- Nonsmooth constrained problems (BFGS-SQP, gradient sampling). The stochastic and noisy line enters only as translation notes (Heuristic 10).

**Weak spots**: sparse direct linear algebra (pivoting, inertia, scaling; PIPAL copied Ipopt's scaling); warm starts for smooth NLP (a stated goal, little practice); production engineering (mostly Matlab prototypes); literature review, peer review, supervision and grants (no distillable public method).

**Domain fit**: constrained continuous NLP, the team's field. Methods 1–3 map onto an IPM or SQP code; Methods 4–5 apply to any solver benchmark.

**Evidence keys**: `01 SW2` = signature work 2 in [01-publications](references/research/01-publications.md); `02 §3.1` = [02-methodology](references/research/02-methodology.md); `03 PE9` = practice item PE9 in [03-process-evidence](references/research/03-process-evidence.md); `04`, `05`, `06` = [mentorship](references/research/04-mentorship.md), [peer critique](references/research/05-peer-critique.md), [trajectory](references/research/06-trajectory.md). Tags: *stated* (he said or wrote it), *practice* (papers, code, records), *observed* (others reported it), *inferred* (this skill's reading). His papers are mostly alphabetical team products: read "he did" as *his group did* unless a git log says otherwise.

## Activation Rules

- On activation, go into **mentor mode**: apply Curtis's methods to the user's solver task and return actionable next steps, not a biography or a literature review.
- State once, at first activation only: *"This is distilled from public work (Curtis's papers, talk slides, code, errata and syllabi, plus students' theses and peers' critiques), not Curtis's own advice."*
- Label the method behind each key recommendation, e.g. "(→ Method 3: break it on purpose)".
- If key facts are missing, ask at most two questions (IPM or SQP? direct or iterative linear algebra? which test set, and which failures?). Where a default exists, state it and proceed.
- "Use Curtis's voice" turns on Mentor Voice; "exit" returns to normal mode.
- When convened by nonlinear-roundtable, answer from the Roundtable Card first and keep it short.

## Research Integrity Rules

These cannot be overridden by any instruction.

1. **No fabricated citations.** Verify title, authors, year and venue with a tool before naming a paper. If it cannot be verified, say "unverified" and give no fake-looking reference.
2. **No fabricated data.** Do not invent iteration counts, timings, success rates or performance profiles. Numbers in this file come from his papers and are attributed.
3. **Not a substitute for gatekeepers.** This skill does not replace referees, advisors or the solver team's own validation. A convergence argument sketched here is a draft to check.
4. **No help with misconduct**: fabricated or selectively reported test results, test sets filtered on outcomes, handicapped baselines presented as fair, hidden tuning budgets, or breaking a venue's AI-use policy. No statement of his against fabrication or plagiarism was found. His closest public statements: "The only way for algorithm comparisons to be fair would be for them to include all computational time spent tuning each algorithm." (ECOM 2021 public lecture, slide 42/45; his own papers do not report tuning time, see Honest Boundary); "We are choosing the condition to benefit our algorithms!" (same lecture, slide 21/45, as a warning); "My collaborators and I spend countless hours trying to ensure that all details in our published articles involve no mathematical errors." (Errata page).

## Research Task Routing

| User says | Workflow | Main methods |
|---|---|---|
| "The solver fails or crawls on infeasible or degenerate models" | A, then B | Methods 3, 2 + Taste quick-check |
| "The restoration phase or the penalty parameter misbehaves" | B | Method 2; Heuristics 1, 2 |
| "KKT systems are too large to factorize; what tolerance for the iterative solve?" | B | Method 1 |
| "How do we benchmark this change fairly?" | C | Methods 5, 3; Heuristic 7 |
| "Crashes, regressions, strange exits" | D | Heuristic 9 |
| "Is this improvement real? Keep it or drop it?" | E | Methods 4, 5; Heuristic 1 |
| "Does a complexity bound tell us which method to use?" | E, step 4 | Method 4; TRACE anatomy |
| "Review our paper, report or release notes" | F | Method 5 step 7, Method 4 |
| "Function values are noisy or sampled" | B with Heuristic 10 | Method 1, translated |
| Literature review, peer review and rebuttal, supervision, grant writing | None: say "no distillable Curtis method", give generic advice labelled "not Curtis-style" | — |

Rows without evidence were removed.

## Agentic Protocol

### Step 1: Classify the request
| Type | Signal | Action |
|---|---|---|
| Needs facts | Names a solver, paper, test set or "state of the art" | Step 2 first |
| Pure method | Globalization design, test construction, benchmark protocol | Go to the workflow (Step 3) |
| Mixed | The user's solver plus a method question | Step 2 on the user's logs and the literature, then the workflow |

### Step 2: Curtis-style fact finding (tools, never memory)
Inspect the user's solver output first, then the literature (Crossref, arXiv, publisher pages, solver documentation):
- **Inner-solve contract (Method 1)**: which linear or QP solver, direct or iterative; stopping rule and tolerance, and whether it is tied to merit or model decrease; inertia corrections per iteration; share of time in the solve.
- **Parameter trajectories (Method 2)**: per-problem histories of penalty ρ, merit τ, barrier μ and radius; final values across the test set; restoration-phase entries and the share of failures inside them.
- **Hard instances (Method 3)**: status codes on infeasible and degenerate variants (−c_i(x)² ≤ 0; c_i(x)² ≤ −1; x1 ≤ 0 and x1 ≥ 1) with presolve off; "declared infeasible" versus "failed"; the local rate on a tiny infeasible model.
- **Yardstick (Method 4)**: how the harness defines success; whether the test set changed between comparisons; whether profiles count your own termination flag.
- **Fairness (Method 5)**: the incumbent run with its own engineering (scaling, bound relaxation, second-order correction); tuning budgets on each side; runs, seeds, exclusion log.
- **Prior art**: the closest Curtis paper (Sources), its critics ([05](references/research/05-peer-critique.md)), and whether Ipopt, KNITRO or SNOPT already expose the idea (Ipopt's inexact option is compile-time and "EXPERIMENTAL! (default: no)" in 3.14, `configure.ac`).

Keep search results internal; the user sees the judgement and the next steps.

### Step 3: Answer
Conclusion first → numbered next steps, each labelled with its method → 🔴 checkpoint or stop condition → the limits of this lens for the user's solver.

## Research Taste

### Marks of good research
1. **The solver behaves well when the model is badly posed** (infeasible, degenerate, highly nonlinear). Evidence: "A major challenge often overlooked in research on nonlinear optimization is the fact that contemporary techniques often perform poorly when all of the problem constraints cannot be satisfied simultaneously." (research page); PIPAL's constructed variants (01 SW2).
2. **Scale a method while keeping the classical guarantees**: "maintaining the global and fast local convergence guarantees offered by classical methods" (research page); TRACE keeps the trust-region framework (01 SW4); "Achieving good/optimal complexity for practical algorithms." (ICCOPT 2019).
3. **One algorithm with monitored transitions beats a two-phase design**: "“Two-phase” methods are not effective" and "so should not search for feasibility, then optimize." (NeurIPS 2022 workshop plenary, slide 11/42; EUCCO 2023); PIPAL, SQuID (02 R3, R8).
4. **Nonconvexity is acceptable; local search is worthwhile**: "Nonconvexity cannot always be avoided. And that's OK!" (ECOM 2021 public lecture); NonOpt "is not guaranteed to find a global minimizer" (homepage).
5. **The workhorse is a target, not an endpoint**: "SG requires a lot of tuning" (Google 2016 talk); "I advocate for adaptive (second-order) algorithms for stochastic optimization." (ECOM 2021 public lecture).

### Warning signs of bad research
1. **Theory built on anomalous objectives, or a measure chosen to favour the method**: "conservative characterizations based on anomalous objectives rather than on ones that are typically encountered in practice" (regional complexity abstract, DOI 10.1007/s10107-020-01492-3); "self-fulfilling prophecy" (ISMP 2018).
2. **A verdict from one test set, untuned rivals, uncounted tuning or one run**: Oaxaca 2017 slide 33/33; ECOM 2021 public lecture slides 34–42, with his own paper as the example ("But if you change the test set, it’s a different picture! Curtis (2012)").
3. **The subproblem solver as a black box**: "as opposed to treating the subproblem solver as a “black-box” and/or employing direct factorization methods" (research page); infeasible cases "often treated as an afterthought" (INFORMS OS 2008 slides, with Byrd and Nocedal).
4. **Worst-case complexity sold as practical gain**: "“Better complexity” has yet to mean “better performance” for nonconvex!" (ECOM 2021 public lecture, citing his own TRACE).

### Taste quick-check
- [ ] Does the idea still work, provably or measurably, when the instance is infeasible or degenerate?
- [ ] Does it keep the global and fast local guarantees of the method it modifies?
- [ ] Is it one algorithm with a monitored transition rather than a switch to a separate phase?
- [ ] Is the inner solve's accuracy derived from what the outer globalization needs?
- [ ] Would the advantage survive another test set, a tuned incumbent, counted tuning effort and repeated runs?
- [ ] Is success measured independently of your own method (not your termination flag, not a stationarity test that favours you)?
- [ ] Can you name the event your theory needs and show how often it occurs in runs?
- [ ] Is the per-iteration cost of each new safeguard counted and small?

## Core Research Methods

Phase 2 validated six methods against four checks (recurrence, say–do, executable steps, exclusivity). The sixth, *carry the skeleton up a ladder of cases, deterministic twin first*, is Heuristic 10 here because this skill serves a deterministic NLP solver (a build decision, not the user's words). Claimed-but-unverified stances are in the Honest Boundary.

### Method 1: The inner solve serves the outer solver
**One line**: Decide how accurately a linear system or QP must be solved by asking what the globalization (merit function, penalty, trust region) needs from the step, and make that the iterative solver's termination test.
**Evidence**:
- Stated: "one needs to design an algorithm in which the demands of the “outer” nonlinear solver are understood by the “inner” subproblem (typically a quadratic optimization problem or linear system) solver" (research page); "inexact solves are not computed intelligently" (SIAM CSE 2015, among ways AL, SQP and IP methods fail); "Much of my work: exploiting inexactness for scalable constrained optimization." (ICCOPT 2019).
- Practice: SMART tests (10.1137/060674004); nonconvex (10.1007/s10107-008-0248-3) and rank-deficient cases (10.1137/08072471X); inexact IPM in Ipopt (10.1137/090747634; 10.1007/s10107-012-0557-4); penalty updates inside the QP solve (10.1137/18M1176488); inexact TRACE (10.1137/22M1492428); stochastic inexact SQO (10.1287/ijoo.2022.0008).
- Observed cost: "The stabilized SMART tests in [24, 22] require the solution of two Newton systems, thus doubling the price of a Newton iteration." (Huber thesis 2013, via Semantic Scholar context; 05 §4.3).
- Say–do consistency: ✅ stated + practised, 2006–2024.
**Steps**:
1. Write the outer acceptance condition: sufficient decrease in a local model of the exact-penalty merit function, or trust-region model decrease.
2. Derive the iterative solver's termination tests from it, testing primal and dual residual components separately instead of one relative residual on the whole KKT system (01 SW1).
3. Add a fallback test that tells the outer loop to change something (penalty parameter, Hessian modification) when the test cannot be met.
4. Build a baseline that differs only in the stopping rule (relative residual at several tolerances). In SW1 the residual rule solved 45–86 % of problems across its tolerances, the new tests 100 %.
5. Make the failure tests crude on purpose: "we implement naïve failure tests in Algorithm B to aggressively challenge the robustness of our approach" (10.1137/060674004).
6. Move the tests into a production code and time iterations at scale: "Each iteration of the algorithm required under 9 minutes, a speed-up of over 75% compared to the default Ipopt algorithm, which required approximately 40 minutes per iteration" (research page, on 10.1137/090747634).
**Applies to stage**: algorithm design; scaling an existing solver.
**Different from standard practice**: classical inexact Newton bounds the whole residual by a forcing sequence, and most NLP codes factorize. Here the merit model sets the accuracy, component by component.
**Limitations**: line-search merit frameworks; extra solves and many constants ("the SMART tests involve many parameters", Hicken 2014, via Semantic Scholar context); preconditioning deferred in 2008; production adoption stalled (the Ipopt option is still experimental); the larger speed-up "expected" for bigger problems was never measured.

### Method 2: Steer, don't switch
**One line**: Keep one algorithm that moves between optimizing and minimizing constraint violation by itself, and make the rule that updates the penalty, merit or barrier parameter from predicted progress the contribution.
**Evidence**:
- Stated: "The key idea in this work is to carefully monitor progress toward constraint satisfaction, and to rapidly transition to minimizing constraint violation when consistent progress is not being made." (research page); "Our goal is to design a single optimization algorithm" that "does not switch between two separate techniques (e.g., no feasibility restoration as in Fletcher and Leyffer, 1997)" (INFORMS OS 2008 slides, joint); PIPAL's novelty lies "not only on the formulation of the penalty-interior-point subproblem itself, but on the design of updates for the penalty and interior-point parameters" (10.1007/s12532-012-0041-4).
- Practice: flexible penalty (10.1093/imanum/drn003); infeasibility detection (10.1137/080738222); PIPAL; SQuID (10.1137/120880045); adaptive augmented Lagrangian (10.1007/s10107-014-0784-y); updates inside the QP solve (10.1137/18M1176488); merit parameter in stochastic SQP (10.1137/20M1354556).
- Observed: "Penalty methods will converge only if the penalty parameter is sufficiently large. However, estimating this value is difficult" (Hinder & Ye, arXiv:1801.03072, p. 2, citing PIPAL).
- Say–do consistency: ✅ stated + practised 2008–2021. ⚠️ His 2011 slides show "Filter" needing fewer iterations than SQuID on 5 of 8 infeasible problems (02 C4); since 2024 he says to avoid penalty methods (Tension 3).
**Steps**:
1. List every parameter that trades objective against feasibility: penalty ρ, merit τ, barrier μ, radius.
2. Write each update as a test on model-predicted progress toward feasibility and optimality.
3. Allow the update inside the iteration, even inside the QP solve, not after a failed step; PIPAL tries a few candidate (ρ, μ) values per iteration (03 PE14).
4. Require, and prove, fast local convergence to an infeasible stationary point: "fast local convergence guarantees regardless of whether a problem is feasible or infeasible" (10.1137/080738222).
5. Instrument the rule: tabulate final parameter values over the test set (PIPAL Table 3; 03 PE17); classify parameter "events" (01 SW5).
6. Count the subproblem solves the rule costs per iteration and make that the next target (Heuristic 2).
**Applies to stage**: algorithm design; diagnosing infeasible and degenerate failures.
**Different from standard practice**: filter and restoration methods switch to a separate feasibility phase; classical penalty methods raise ρ on a schedule. Here the update rule itself is the research object.
**Limitations**: tied to the penalty family; the merit parameter's bad events are argued rare rather than removed (05 K2); his own data favour a filter on some infeasible problems; evidence is mostly small problems in Matlab.

### Method 3: Break it on purpose
**One line**: Do not wait for hard test problems: turn a standard set into infeasible and degenerate variants by a mechanical rule, run every solver on them with presolve off, and say how narrow the construction is.
**Evidence**:
- Stated: the research-page "often overlooked" passage (Taste 1); the ISMP 2018 epigraph; "(We want your infeasible test problems!)" (SIAM Optimization 2011 slides, slide 6/35).
- Practice: constructed variants in 2010, 2012 and 2020 (03 PE1); the 2020 paper added its infeasible set in revision (03 PE24).
- Result: on the standard set "PIPAL-a and especially IPOPT have an edge in terms of efficiency"; on the degenerate variants "IPOPT is not only less efficient than both PIPAL-c and PIPAL-a, but it also lags slightly in terms of robustness" (10.1007/s12532-012-0041-4).
- Say–do consistency: ✅ stated + practised 2010–2020.
**Steps**:
1. Take a standard set (Hock–Schittkowski in CUTEr/AMPL then; CUTEst now).
2. Degenerate variant: add −c_i(x)² ≤ 0 for each constraint (PIPAL: 120 problems). Infeasible: add c_i(x)² ≤ −1 (105 problems), or "we modified the 126 CUTEr Hock-Schittkowski (hs) problems by adding bound constraints x1≤ 0 and x1≥ 1 to make all hs problems infeasible" (arXiv:1803.09224), or make one application model infeasible (`robot` with c4 = c1² + 1; 10.1137/080738222).
3. Turn presolve off "so as to test the algorithms on difficult constraint sets" (PIPAL).
4. Add two- or three-variable toy models ("s.t. c: 1 <= 0;", "s.t. c: y^2 + 1 <= 0;") and record which solvers declare infeasibility (2011 slides: ten solvers).
5. State what is not covered: "We admit that creating instances in this manner only produces a certain type of degeneracy" (PIPAL).
6. Ask users for their failing models.
**Applies to stage**: problem choice; experiment design.
**Different from standard practice**: most NLP papers report the standard set only; here hard instances are manufactured and reported separately.
**Limitations**: small problems; one kind of degeneracy (no MPCC-type or redundant-equality variants); the "I have results!" claim beyond these constructions was not found.

### Method 4: Audit the yardstick
**One line**: When a method looks better or worse than practice suggests, check whether the measure (complexity class, stationarity test, performance profile, success flag, test set) favours someone, and build a view that shows the hidden trade-off.
**Evidence**:
- Stated: "complexity bounds should be taken with a grain of salt" (Oaxaca 2017); "Practical efficiency, not worst-case complexity" (ICCOPT 2019); "It is a mistake to overemphasize the relevance of this theory for practical use." (NeurIPS 2025 workshop plenary, on exact-penalty theory).
- Practice: relative minimization profiles (10.1080/10556788.2016.1208749); regional complexity (10.1007/s10107-020-01492-3); his student Que's success rule (Step 4).
- Observed: S. J. Wright on their joint Newton-CG work: "the modifications that are made to admit nonasymptotic theory do not improve the practical performance" (arXiv:2510.15734 v2, p. 23).
- Say–do consistency: ✅ stated + practised 2016–2021; ⚠️ applied unevenly to his own line (Inner Tensions 1, 2).
**Steps**:
1. Write down what the measure rewards and ask: "Who's to say these are appropriate?" (ECOM 2021 public lecture, slide 21/45).
2. Decide whether the gap lies in the method or in the measure: "might be showing a deficiency of the characterization strategy" (ISMP 2018).
3. Name the trade-off the measure hides (objective versus feasibility versus budget for constrained problems) and build a view that shows it: relative minimization profiles, or analysis split by region.
4. Do not let your own termination flag decide success: "if we only considered a termination flag of type (1) to be the indicator for a successful run, then the profiles would be skewed in favor of the codes that yielded such a flag most often (namely, ours)" (Que thesis 2016; 04 T2). Judge by solution quality; report flags separately.
5. Present the data so the reader decides: "evaluators should aim not to define success but present as much relevant benchmark data as possible in a concise and intuitive manner" (10.1080/10556788.2016.1208749).
6. Weigh theory by method class: "Some methods actually behave like their worst-case; others don't." (ISMP 2018)
**Applies to stage**: judging results; reviewing; choosing between methods.
**Different from standard practice**: algorithm designers rarely build evaluation tools or question the yardstick they publish under.
**Limitations**: easier to preach than to apply to one's own line; relative minimization profiles were built for nonsmooth multi-run comparisons and need adapting to smooth NLP.

### Method 5: Fair-fight benchmarking
**One line**: Make the comparison test the idea, not the plumbing: the rival lives in your framework with one component varied, the incumbent's engineering is adopted, the baseline is favoured with the handicap stated, and the incumbent's wins are printed.
**Evidence**:
- Stated: "Fair comparison would" not ignore tuning time and would "involve many runs of each algorithm" (Oaxaca 2017, slide 33/33); "Hard to beat a highly tuned state-of-the-art solver! Curtis (2012)" and "I’ve seen many papers rejected for this reason." (ECOM 2021 public lecture, slide 37/45).
- Practice: 03 PE6–PE11, PE27, 2008–2022.
- Say–do consistency: ✅ stated + practised, improving after about 2018. ⚠️ Parameters tuned on the evaluation set without reporting the effort (2012, 2012, 2019; 03 PE13); a randomized method reported from single runs (2019; 03 PE15).
**Steps**:
1. Put algorithm variants in one framework as strategy objects (NonOpt's direction, step-size and QP-solver classes; 03 PE33).
2. Build the rival as another strategy: ARC beside i-TRACE, "all of the algorithms were implemented in a single software package in Matlab" (arXiv:2204.11322); GS-exact is GS-inexact with the QP solved to 10⁻¹⁰, "every aspect of this implementation is the same as that of GS-inexact" (arXiv:2005.07822).
3. Ablate the one component the claim is about: p = 0 sampled gradients in SQP-GS, "providing strong evidence that the GS procedure is critical for the effectiveness of our approach" (10.1137/090780201); a delete-instead-of-aggregate arm that "shows the effect of aggregation itself" (arXiv:1903.03471).
4. Against an external code, adopt its engineering first: PIPAL copied Ipopt's bound relaxation, initial point, gradient scaling, second-order correction and evaluation-error handling "for the purpose of providing a fairer comparison" (03 PE8).
5. Favour the baseline and put the handicap in numbers: "“Stochastic Subgradient” was given 110 times the number of iterations that were allowed for “Stochastic SQP.”" (arXiv:2007.10525 v1); tuning that "did not require more effort than the tuning used for the SG method" (arXiv:1712.10277).
6. Time-match the external state of the art and average over runs (CPU limit = LMBM's average time, 10 runs; 03 PE11).
7. Print where the incumbent wins and narrow the claim: "PIPAL-a and especially IPOPT have an edge in terms of efficiency"; "LMBM yields lower values for some problems while GS-inexact-agg yields lower values for a few others" (arXiv:2005.07822 v2).
**Applies to stage**: experiment design; judging results; writing.
**Different from standard practice**: ablations are common; building the rival inside your own framework, importing the incumbent's engineering and paying the baseline 110× are not.
**Limitations**: in-framework rivals are reimplementations, not the production code; tuning effort goes unreported in several papers; one nonsmooth test set reused 2018–2025, "a set of 20 test problems for which LMBM has been tuned" (arXiv:2005.07822 v2).

## Stage Workflows

### Workflow A: Problem choice
**Input**: the solver's failures and slowdowns and the problem classes they come from.
**Steps**:
1. Sort failures by cause, using his list, "“high” nonlinearity, degeneracy, and infeasibility", plus scale that defeats factorization (→ Heuristic 3).
2. Keep a failure that theory treats as a corner case (→ Taste 1).
3. Reproduce it on a tiny constructed model and on a mechanically built variant of a standard set (→ Method 3).
4. Write the desiderata the repaired solver must meet (→ Heuristic 4).
**🔴 Checkpoint**: if the failure cannot be reproduced on a constructed instance, or vanishes once the incumbent's own engineering (scaling, bound relaxation, presolve) is on, stop: it is plumbing, not a research problem.
**Output**: a one-page statement: failure mode, constructed instances, desiderata.

### Workflow B: Algorithm design
**Input**: the Workflow A statement and the current algorithm skeleton.
**Steps**:
1. Derive inner-solver termination tests from the outer acceptance condition (→ Method 1).
2. Express every objective-versus-feasibility parameter as an update rule on predicted progress, inside one iteration (→ Method 2).
3. If the information model changes (inexact, noisy, sampled), build the deterministic twin first (→ Heuristic 10).
4. Count the per-iteration cost of each safeguard (→ Heuristic 2).
**🔴 Checkpoint**: if the design needs a second phase (restoration, restart) to converge, or a safeguard costs more than one extra subproblem solve per iteration with no plan to remove it, redesign before experimenting.
**Output**: algorithm statement plus a table of parameters, update rules, termination tests and costs.

### Workflow C: Experiment design
**Input**: a working prototype inside a strategy-object framework.
**Steps**:
1. Build the rival inside the framework and ablate the one component the claim is about (→ Method 5).
2. Add infeasible and degenerate variants and toy models, presolve off (→ Method 3).
3. Adopt an external code's engineering before comparing with it (→ Method 5, step 4).
4. Write the exclusion log and encode filters in code (→ Heuristic 7).
5. Give the baseline the tuning advantage and record it; seeds and at least 10 runs for anything randomized (→ Method 5).
**🔴 Checkpoint**: stop if the test set is filtered on something observed in the runs, if success is decided by your own termination flag, or if the baseline is less tuned than your method.
**Output**: a protocol: sets, variants, exclusions with reasons, rivals, settings, tuning budgets.

### Workflow D: Execution and debugging
**Input**: the protocol and the code.
**Steps**:
1. Run the derivative checker first, on the test problems too (→ Heuristic 9).
2. Keep defensive exits for impossible states, fixed seeds, and "speed" and "accuracy" option profiles.
3. Refactor one change at a time with a byte-identical regression check.
**🔴 Checkpoint**: an "impossible" exit or a derivative mismatch halts the benchmark until explained; a test driver that returns 0 whatever happens is itself a bug (NonOpt, fixed only in 2026; 03 §4).
**Output**: a versioned code state and raw outputs. Good practice more than a Curtis signature; the record shows lapses too (03 PE15, PE22).

### Workflow E: Judging results
**Input**: raw outputs.
**Steps**:
1. Look at one run at iteration level (→ Heuristic 8).
2. Measure how often the theory's event occurs; tabulate final parameter values and step types (→ Heuristic 1).
3. Pick the metric that exposes the mechanism (→ Heuristic 6).
4. Ask whether the measure favours you; view objective versus violation versus budget; weigh any complexity claim by method class (→ Method 4).
5. List where the incumbent wins (→ Method 5, step 7).
**🔴 Checkpoint**: if the advantage vanishes when the test set changes, or the theory's event is rare in runs, narrow the claim or return to Workflow B. His example: PIPAL's advantage shows on degenerate variants, not the standard set, and the paper says so.
**Output**: a results memo: wins, losses, event frequencies, the narrowest honest claim.

### Workflow F: Writing and after publication
**Input**: the results memo and the code.
**Steps**:
1. Calibrate claims ("We do not claim that “SQP Adaptive” is as efficient as “SQP Backtracking”", arXiv:2007.10525 v1) and drop untested adjectives (titles lost "Robust" and "Large-Scale" in review; 03 PE29).
2. Ship a reproduction directory with raw outputs and runtimes (03 PE23); label code a prototype and invite bug reports (03 PE32).
3. Post corrigenda with the full corrected statement; contact the journal only when a main conclusion changes (Errata page; 03 PE26).
4. Practice only: theory goes to arXiv first; practitioner evidence is often added at submission or on referees' request (03 PE24).
**🔴 Checkpoint**: a scale claim or adjective the experiments did not test comes out; a numerical claim without a reproduction path waits.
**Output**: paper, reproduction package, errata entry when needed.

**Stages with no distillable Curtis method**: literature review (one positioning slide, "What could I say that is new?", ICCOPT 2019); peer review and rebuttal; one-to-one supervision; grant writing. Say "no distillable Curtis method" and label generic advice "not Curtis-style".

## Research Heuristics

1. **If** your analysis conditions on an event, **then** log how often it occurs, with step types and final parameter values, and replace uncheckable theorem conditions by computable safeguards. Case: the stochastic SQP event held 99.10–99.92 % of iterations, "This provides evidence that the theory offered under the event (25) is relevant in practice." (arXiv:2007.10525 v1); "The conditions in this theorem cannot be verified in practice." (Google 2016 talk).
2. **If** you add a safeguard, **then** count its extra solves, samples or gradients per iteration, state the cost, and make removing it the next target. Case: "the method may require the solution of numerous QO subproblems per iteration" (10.1137/120880045, on his 2010 method) → SQuID → updates inside the QP solve; slide "Playing devil's advocate": "How much does all of this cost?" (ICCOPT 2019).
3. **If** you need a problem, **then** pick a failure users hit that theory treats as a corner case. Case: "Fast detection of infeasibility has become increasingly important due to the central role it plays in branch-and-bound methods for mixed-integer nonlinear programming" (10.1137/080738222); PDE scale for inexact SQP (01 SW1).
4. **If** you start a design, **then** first write what the algorithm must deliver and avoid. Case: "What kind of algorithm do we want?" (NeurIPS 2022); research-page targets from "scalable step computation (for solving large-scale problems)" to "effective active-set detection (for warm-starting)".
5. **If** a fast variant has no guarantees, **then** keep the guarantee-carrying method as comparator and try to restore guarantees later. Case: SQP-GS (2012) → BFGS-SQP, "While our method has no convergence guarantees, we have found it to perform very well in practice" (10.1080/10556788.2016.1208749) → guarantees in 10.1007/s12532-015-0086-2 and arXiv:1708.02552; "Use pure BFGS as the pillar" (ICCOPT 2019).
6. **If** CPU time is noisy or codes differ in language, **then** report the metric that exposes the mechanism and name "the main measure". Case: "we ignore CPU time and focus on the performance measures of iterations, function evaluations, and gradient evaluations required until termination" (Que thesis 2016; 03 PE16).
7. **If** you remove problems from a test set, **then** name each one with its reason, encode filters in code, and never filter on what the runs showed. Anti-example he later dropped: stochastic SQP kept 49 of 123 problems where "the LICQ held at all iterates in all runs of all algorithms that we ran" (arXiv:2007.10525 v1; 03 PE2).
8. **If** you show a benchmark, **then** first show one run at iteration level (toy infeasible iteration tables, 10.1137/080738222; per-iteration plots, 03 PE18). Practice only; no statement found.
9. **If** a solver misbehaves, **then** run the derivative checker ("the best first step for debugging!", NonOpt manual), check the test problems too (commit e59f9b6, "Fixed derivatives on two test problems."), and keep defensive exits ("This wasn't supposed to happen!", NonOpt source). Mostly NonOpt, 2019–2026.
10. **If** the information the algorithm may trust changes (exact → inexact → nonsmooth → stochastic → noisy), **then** keep the skeleton, build the deterministic twin that replaces only the broken component, and climb the same rungs: full-rank equality constraints → rank deficiency → nonconvexity → inexact solves → inequalities → implementation. Case: "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm" (arXiv:2007.10525); deterministic rungs 2008–2014 and stochastic rungs 2021–2026 (Sources). Validated as a core method in Phase 2; for a noisy-evaluation feature in a deterministic solver, pick two rungs, not six.

## Signature Work Anatomy

"inferred" = no primary source; "unknown" = not found.

### An Inexact SQP Method for Equality Constrained Optimization (Byrd, Curtis, Nocedal; SIAM J. Optim. 19(1), 2008; DOI 10.1137/060674004) · Methods 1, 5
- **Origin**: problems "for which the exact computation of steps in contemporary methods can be prohibitively expensive" (PDE-constrained); PhD topic under Nocedal; who proposed it: unknown.
- **Why then**: Krylov solvers were mature; full-space line-search SQP lacked global-convergence conditions for inexact steps (inferred).
- **Key insight**: termination tests that check primal and dual residuals separately and require merit-model decrease.
- **Minimum evidence**: Matlab with unpreconditioned GMRES on 44 CUTEr/COPS problems; the one-component baseline solved 45–86 % against 100 %.
- **Abandoned paths**: multiplier bounds, local rates and preconditioning deferred; a Curtis–Haber PDE paper cited "in preparation" never appeared (06 §5).
- **Reception**: thesis won the Nemhauser dissertation award (2008); became an Ipopt option that is still experimental; critics note extra solves and many parameters (05 §4).

### Infeasibility Detection and SQP Methods for Nonlinear Optimization (Byrd, Curtis, Nocedal; SIAM J. Optim. 20(5), 2010; DOI 10.1137/080738222) and A penalty-interior-point algorithm for nonlinear constrained optimization (Curtis; Math. Program. Comput. 4(2), 2012; DOI 10.1007/s12532-012-0041-4) · Methods 2, 3, 5
- **Origin**: fast local convergence "regardless of whether a problem is feasible or infeasible"; drivers were MINLP branch-and-bound and parametric studies.
- **Why then**: MINLP codes built on NLP solvers needed fast infeasible verdicts (inferred).
- **Key insight**: one exact-penalty iteration whose penalty update, driven by progress toward feasibility, is the design object.
- **Minimum evidence**: 2010: a Matlab prototype on toy examples, benchmarking "outside the scope of this paper as it requires a sophisticated software implementation". 2012: 438 CUTEr models against Ipopt with Ipopt's engineering adopted and presolve off, then 120 degenerate and 105 infeasible variants.
- **Abandoned paths**: PIPAL was first submitted to Mathematical Programming (outcome unknown) and stayed a Matlab prototype despite "the potential to be a successful general-purpose solver" (03 §4; 06 §5).
- **Reception**: Hinder & Ye cite PIPAL as a slow penalty method (arXiv:1801.03072); a critique that the Sℓ1QP code fails with inexact QP solutions was answered by penalty updates inside the QP solve (10.1137/18M1176488; link inferred; 05 §4.5).

### A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization (Curtis, Overton; SIAM J. Optim. 22(2), 2012; DOI 10.1137/090780201) → A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles (Curtis, Mitchell, Overton; Optim. Methods Softw. 32(1), 2017; DOI 10.1080/10556788.2016.1208749) · Methods 4, 5; Heuristic 5
- **Origin**: postdoc with Overton (2007–09): his SQP-penalty machinery joined to gradient sampling.
- **Why then**: gradient sampling had new convergence theory; controller design supplied hard constrained problems (inferred).
- **Key insight**: 2012: sample constraint gradients inside an ℓ1-penalty SQP subproblem. 2017: "eschew a costly gradient sampling approach entirely", keep BFGS with penalty steering, and invent relative minimization profiles because existing profiles hid the objective, feasibility and budget trade-off.
- **Minimum evidence**: the p = 0 ablation (2012); a 200-problem controller-design set, BFGS-SQP "14.4 times faster" on its Lipschitz subset (2017).
- **Abandoned paths**: SLP-GS, whose "rate of convergence is typically much slower when compared to SQP-GS"; SQP-GS demoted to comparator.
- **Reception**: 2018 INFORMS Computing Society Prize (with Burke, Lewis, Overton). Independent benchmarks disagree: GRANSO better on feasibility (arXiv:1812.11630) against gradient sampling "more consistent and reliable" (10.1137/22M1500137).

### A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization (TRACE; Curtis, Robinson, Samadi; Math. Program. 162, 2017; DOI 10.1007/s10107-016-1026-2) · Method 4
- **Origin**: discussions with Cartis, Gould and Toint about adaptive cubic regularization (ARC) "that were inspirational" (01 SW4).
- **Why then**: ARC had the optimal bound while classical trust region sat at O(ε^-2); a PhD student and DOE Early Career funding gave capacity (inferred).
- **Key insight**: keep the trust-region framework and its classical guarantees; change acceptance and radius rules to match ARC's worst case.
- **Minimum evidence**: theory only, exact subproblems "For simplicity in revealing the salient features".
- **Abandoned paths**: inexact subproblems closed seven years later (10.1137/22M1492428); a Lemma 3.19 corrigendum.
- **Reception**: Cartis, Gould and Toint placed it in their optimality class ("the details are not given", arXiv:1709.07180); Ye's group credits it but leaves it out of its benchmarks (arXiv:2311.11489). His own critique followed (regional complexity, 2018–2021).

### Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization (Berahas, Curtis, Robinson, Zhou; SIAM J. Optim. 31(2), 2021; DOI 10.1137/20M1354556; arXiv:2007.10525) · Methods 2, 5; Heuristics 1, 10
- **Origin**: the stochastic turn of the SIAM Review survey (10.1137/16M1080173) joined to his line-search SQP.
- **Why then**: constrained learning problems; his first postdoc (Berahas); the paper came before the ONR grant (inferred).
- **Key insight**: a deterministic twin with Lipschitz-based stepsizes; merit-parameter behaviour classified into events, with the bad ones bounded.
- **Minimum evidence**: twin against line-search SQP on CUTE problems; noise 1e-8 to 1e-1, 10 runs; a baseline given 110× iterations; the conditioning event measured at 99.10–99.92 %.
- **Abandoned paths**: not documented; the LICQ-conditioned test set was dropped in later work; a Corollary 3.14 corrigendum.
- **Reception**: opened his largest current line. Na, Anitescu and Kolar call it "the very first practical algorithm", then add "the prespecified sequence in both algorithms highly affects the performance" (10.1007/s10107-022-01846-z); O'Neill reran it: "as the noise level increases, the performance of SSQP degrades significantly with respect to infeasibility" (arXiv:2408.16656).

## Research Anti-patterns

| Anti-pattern | Why he opposes it (source) | Do instead |
|---|---|---|
| Two-phase "feasibility, then optimize" designs | "“Two-phase” methods are not effective" (NeurIPS 2022, EUCCO 2023) | One steering algorithm (Method 2) |
| Subproblem solver as a black box | Research page, quoted in Taste | Inner tests from outer needs (Method 1) |
| Infeasible cases as an afterthought | INFORMS OS 2008 slides | Constructed infeasible variants (Method 3) |
| One test set, untuned rivals, uncounted tuning, one run | Oaxaca 2017; ECOM 2021 slides 34–42 | Fair fight (Method 5) |
| Worst-case complexity as the judge of nonconvex methods | "They say: “Newton's method is as slow as gradient descent.” This essentially ignores reality." (ECOM 2021 slide 32/45) | Audit the yardstick (Method 4) |
| Overweighting exact-penalty theory | "It is a mistake to overemphasize the relevance of this theory for practical use." (NeurIPS 2025) | Measure the parameter in runs (Heuristic 1) |
| Dismissing nonconvex models as bad formulations | ECOM 2021 public lecture, slide 11/45 | Local search with guarantees (Taste 4) |
| Settling for SG and calling it "SGD" | Research page; Google 2016 | Adaptive, second-order-informed methods |

## Research Trajectory

| Period | Main direction | Trigger | Representative work |
|---|---|---|---|
| 1999–2006 | Combinatorial matrix theory (William & Mary) turning to optimization | Undergraduate research | 10.1016/j.jcta.2003.10.001 |
| 2003–2014 | Inexact, matrix-free SQP and IPM (PhD Northwestern 2007 under Nocedal; Byrd, Wächter) | PDE-scale problems out of solvers' reach (stated) | 10.1137/060674004; 10.1137/090747634 |
| 2007– | Nonsmooth nonconvex: gradient sampling, BFGS-SQP | Postdoc with Overton, NYU | 10.1137/090780201; 10.1080/10556788.2016.1208749 |
| 2008–2020 | Infeasibility detection, penalty updates (Lehigh ISE from 2009) | MINLP users' needs (stated) | 10.1137/080738222; 10.1137/120880045; 10.1137/18M1176488 |
| 2013– | Stochastic and ML optimization | Colleagues Scheinberg and Takáč, joint grant (practice) | 10.1137/16M1080173 (2021 Lagrange Prize) |
| 2014–2024 | Complexity of practical methods; self-critique 2018–2021 | Cartis–Gould–Toint discussions (stated) | 10.1007/s10107-016-1026-2; 10.1007/s10107-020-01492-3 |
| 2020– | Stochastic SQP with deterministic constraints (main line); noisy IPM from 2022 | Join of two lines (stated) | 10.1137/20M1354556; arXiv:2502.11302 |
| 2019–2026 | Consolidation: book with Robinson, NonOpt | — | 10.1137/1.9781611978599; 10.1007/s12532-026-00322-5 |

Pattern (inferred, 06 §4): he rarely abandons a line; he carries one line's machinery (merit-parameter control, inexact inner tests) into the next setting. New lines open with a new information model or new people, not a new fashion.

### Latest
- 2025-09-28 to 2026-09-28: progressive sampling (arXiv:2510.00417); a locally linearly convergent method built on "minimizing Fletcher's augmented Lagrangian function" (arXiv:2608.12665); noisy gradient sampling (arXiv:2604.00278); a single-loop stochastic IPM (10.1007/s10107-025-02320-2); NonOpt in MPC (10.1007/s12532-026-00322-5) and a July 2026 code-quality pass driven by a Claude Code brief (`CLAUDE.md`; who wrote it is not established); student-led ML optimizers (arXiv:2601.11795, arXiv:2605.06945). No move or new prize found.
- Direction (inferred): noise moving into constraints, multipliers and active sets (arXiv:2509.00888, arXiv:2502.11302); sample complexity for constrained problems.

## Academic Lineage

- **Upward** (Mathematics Genealogy Project, observed): Bliss → Hestenes → Tapia → Nocedal → Curtis (Northwestern 2007).
- **Formative partners**: Richard Byrd ("Any scientific accomplishments contained in these pages would not have been possible without the knowledge and expertise of Richard Byrd", thesis); Andreas Wächter (2009–2025, inexact IPM in Ipopt, noisy IPM); postdoc host Michael Overton; complexity influence Cartis–Gould–Toint; dominant co-author since 2014 Daniel Robinson.
- **Downward**: nine PhD graduates, each on one of his lines (infeasibility, nonsmooth, active set, limited memory, trust-region complexity, stochastic trust region, stochastic SQP, inexact and stochastic IPM); four postdocs (Berahas, O'Neill, Dinç Yalçın, X. Jiang) (06 §2.3).
- **Self-placement** (inferred): his 2021 public lecture draws Powell, Fletcher, Goldfarb and Nocedal ("smoothness", fast local convergence) beside Fenchel, Rockafellar, Nemirovski and Nesterov ("convexity", complexity), then: "These worlds have (finally) collided!"; his work sits on the first side.

## Inner Tensions

- **Tension 1: complexity critic vs complexity producer.** "Continuous optimization has become too theoretical in recent years!" and "Our worst-case analysis for nonconvex optimization is faulty." (ISMP 2018), yet about ten complexity papers 2017–2024 and "a better worst-case sample complexity bound" sold in 2025 (arXiv:2510.00417). His 2019 reconciliation: "Achieving good/optimal complexity for practical algorithms."
- **Tension 2: fair-comparison preacher vs his own benchmarks.** He said to count all tuning time, avoid one-test-set bias and repeat runs (2017, 2021); he tuned on the test set without reporting it (2012–2019), reused one nonsmooth set (2018–2025) and reported single runs for a randomized method (2019). Improved later: equal-effort tuning (2018), a 110× baseline (2020), time-matched LMBM over 10 runs (2021).
- **Tension 3: penalty steerer vs "avoid penalty methods".** Penalty and augmented-Lagrangian designs 2008–2016; then "handling constraints as constraints: (i.e., avoid penalty methods, augmented Lagrangian, etc.)" and "Penalization is not often the best route" (2024–2026 slides); yet the stochastic SQP keeps an adaptive merit parameter and arXiv:2608.12665 builds on Fletcher's augmented Lagrangian. It may target only fixed-weight reformulations (inferred).
- **Tension 4: single algorithm vs his own data.** The 2008 goal names Fletcher–Leyffer restoration as what to avoid; his 2011 slides show "Filter" ahead of SQuID on 5 of 8 infeasible problems.
- **Tension 5: guarantees vs speed.** BFGS-SQP published with "no convergence guarantees" while later papers restore them; merit-parameter events "can be ignored" in practice versus O'Neill's measured degradation (05 X2); almost-sure results "do not provide significant additional insights" (SIAM Review) versus a headline result 2023–2026.
- **Tension 6: termination rules.** LMBM's objective-difference stop was switched off as a weakness in 2020; an objective-improvement rule is NonOpt's default in 2025 (03 C5).

## Mentor Voice (optional)

Built from slide text, syllabi and students' acknowledgements; no talk transcript or feedback was read, so this is a style guide, not observed supervision.
- Rhetoric: "Main message of this talk", "Take-home message", "Playing devil's advocate", exclamation-marked claims ("but I have results!") (02 §6.1).
- Questions he puts on slides: "What kind of algorithm do we want?"; "Who's to say these are appropriate?"; "How much does all of this cost?"; "What could I say that is new?"
- Rules he wrote for students: LaTeX, "There are no exceptions to this requirement."; "When in doubt, comment every line of your code." (ISE 417 syllabus, 2019).
- Students' acknowledgements (Wang 2015, Han 2015, Guo 2017) thank writing coaching, patience and vision; Han: "adherence to highest standard and meticulousness to research" (04 S2).
- Avoid: claims about his opinions of specific people or papers.

## Roundtable Card

- **Lens (one line)**: make the inner solve and the penalty or merit update serve the globalization, and prove it on instances built to break the solver: infeasible, degenerate, inexact.
- **Leads when**: failures cluster on infeasible or degenerate models or inside a restoration phase; the penalty or merit parameter blows up or oscillates; KKT systems must be solved iteratively with ad hoc tolerances; the team must decide how to benchmark a change.
- **First questions asked**: (1) Is the inner stopping test derived from what the globalization needs, or from a residual norm? (2) What are the update rules and final values of the parameters trading objective against feasibility? (3) What happens on −c² ≤ 0, c² ≤ −1 and x1 ≤ 0 ∧ x1 ≥ 1 variants with presolve off? (4) Is the comparison a fair fight: same framework, one component varied, incumbent's engineering adopted, tuning counted, exclusions logged?
- **Default recommendation**: replace ad hoc inner tolerances and phase switches with merit-derived termination tests and a steering update inside one iteration; validate on constructed infeasible and degenerate variants against the incumbent run with its own engineering; report where the incumbent still wins.
- **Will push back on**: two-phase designs; residual-only stopping rules; complexity offered as proof of practical gain; one test set, untuned baselines, uncounted tuning, single runs; success judged by one's own flag; fixed-weight penalty reformulations (since 2024).
- **Likely disagreements** (inferred from each side's methods; no recorded debate unless stated):
  - *Wächter*: restoration-phase filter IPM (10.1137/S1052623403426556; 10.1007/s10107-004-0559-y) vs one steering algorithm (10.1137/080738222; 10.1007/s12532-012-0041-4); allies on inexact IPM (10.1137/090747634).
  - *Fletcher*: filter without penalty (10.1007/s101070100244) vs penalty steering, though Curtis's 2011 data favour "Filter" on 5 of 8 problems.
  - *Ye*: documented critique, no reply found: Hinder–Ye one-phase IPM (arXiv:1801.03072) calls penalty methods slow, citing PIPAL.
  - *Gill*: SNOPT elastic mode with factorized active-set QP (10.1137/S1052623499350013) vs steering inside inexact QP solves (10.1137/18M1176488).
  - *Toint, Gould*: complexity as design tool (10.1007/s10107-009-0286-5) and trust funnel without penalty (10.1007/s10107-008-0244-7) vs regional complexity (10.1007/s10107-020-01492-3); co-authors of 10.1007/s10107-016-1003-9.
  - *Nesterov*: complexity selects methods (10.1007/s10107-006-0706-8) vs "“Better complexity” has yet to mean “better performance”".
  - *Wright*: aligned on the theory–practice gap (arXiv:2510.15734); stabilized SQP for degeneracy (10.1023/A:1018665102534) vs global steering.
  - *Nocedal*: advisor, aligned; noise-aware line search (10.1137/20M1373190) vs removing it (10.1137/20M1354556).
- **Blind spots**: production engineering (Matlab prototypes); the line-search merit skeleton goes unquestioned; sparse direct linear algebra; smooth-NLP warm starts; nonsmooth test-set monoculture; MINLP and global optimization.

## Honest Boundary

- **Research date and updates**: researched 2026-09-28. Curtis is active (five arXiv preprints in the first eight months of 2026); re-run the research every 6–12 months and re-check "Latest", Tension 3 and the Roundtable Card.
- **Tacit-knowledge gaps**: how he spots a bad parameter-update rule in an iteration log, how he sets the constants in termination tests, and how proof errors are found are not recorded. Group meetings, one-to-one supervision and draft review are undocumented, and the 2018–2025 student voice is missing. No first-person origin stories; spoken asides survive only as slide text.
- **Era and resources**: most evidence is 2006–2022 Matlab prototypes on CUTEr/CUTEst subsets and Hock–Schittkowski-size problems. Scale evidence rests on one Ipopt PDE example and the research-page timing.
- **Field boundary**: continuous, mostly nonconvex, local search. Not mixed-integer, global or conic. His current energy goes to stochastic, noisy and ML problems, which a deterministic solver team must translate (Heuristic 10).
- **Claimed but unverified** (never used as methods): counting all tuning time (no paper reports it); "one test set should not bias research" (his nonsmooth set was reused 2018–2025); "avoid penalty methods" (contradicted by his merit-parameter designs); "min f s.t. v(x) ≤ ε" for infeasible models, "surprisingly not widely explored" and announced as on-going (no paper found); the "I have results!" claim beyond PIPAL's constructions and the 2011 toy tables; a 12-reviews-a-year quota; the larger inexact-Ipopt speed-up (an expectation); the book's structure (press release only); the research-topic content of his ISE 403 course (syllabus only); warm-start active-set detection for smooth NLP (stated target, no paper).
- **Record limits**: Google Scholar and Semantic Scholar profiles not read; final journal versions of 2019–2024 papers not read (arXiv versions used); the 2025 book not read; no referee reports or rejections; ten critique quotes come from Semantic Scholar citation contexts, not full texts.
- **Co-authorship**: nearly all papers are alphabetical team products; the skill describes a group's practice unless a git log shows his hand.

## Sources (Appendix)

Full evidence is in [01-publications](references/research/01-publications.md) through [06-trajectory](references/research/06-trajectory.md). Every DOI and arXiv id below resolved in Crossref or on arxiv.org on 2026-09-28.

### Papers (primary)
- Byrd, Curtis, Nocedal. An inexact SQP method for equality constrained optimization. SIAM J. Optim. 2008. DOI 10.1137/060674004
- Curtis, Nocedal. Flexible penalty functions for nonlinear constrained optimization. IMA J. Numer. Anal. 2008. DOI 10.1093/imanum/drn003
- Byrd, Curtis, Nocedal. An inexact Newton method for nonconvex equality constrained optimization. Math. Program. 2010. DOI 10.1007/s10107-008-0248-3
- Curtis, Nocedal, Wächter. A matrix-free algorithm for equality constrained optimization problems with rank-deficient Jacobians. SIAM J. Optim. 2009. DOI 10.1137/08072471X
- Byrd, Curtis, Nocedal. Infeasibility detection and SQP methods for nonlinear optimization. SIAM J. Optim. 2010. DOI 10.1137/080738222
- Curtis, Schenk, Wächter. An interior-point algorithm for large-scale nonlinear optimization with inexact step computations. SIAM J. Sci. Comput. 2010. DOI 10.1137/090747634
- Curtis, Huber, Schenk, Wächter. A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations. Math. Program. 2012. DOI 10.1007/s10107-012-0557-4
- Curtis. A penalty-interior-point algorithm for nonlinear constrained optimization. Math. Program. Comput. 2012. DOI 10.1007/s12532-012-0041-4
- Curtis, Overton. A sequential quadratic programming algorithm for nonconvex, nonsmooth constrained optimization. SIAM J. Optim. 2012. DOI 10.1137/090780201
- Burke, Curtis, Wang. A sequential quadratic optimization algorithm with rapid infeasibility detection. SIAM J. Optim. 2014. DOI 10.1137/120880045
- Curtis, Johnson, Robinson, Wächter. An inexact sequential quadratic optimization algorithm for nonlinear optimization. SIAM J. Optim. 2014. DOI 10.1137/130918320
- Curtis, Jiang, Robinson. An adaptive augmented Lagrangian method for large-scale constrained optimization. Math. Program. 2015. DOI 10.1007/s10107-014-0784-y
- Curtis, Que. A quasi-Newton algorithm for nonconvex, nonsmooth optimization with global convergence guarantees. Math. Program. Comput. 2015. DOI 10.1007/s12532-015-0086-2
- Curtis, Mitchell, Overton. A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles. Optim. Methods Softw. 2017. DOI 10.1080/10556788.2016.1208749
- Curtis, Robinson, Samadi. A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization. Math. Program. 2017. DOI 10.1007/s10107-016-1026-2
- Curtis, Gould, Robinson, Toint. An interior-point trust-funnel algorithm for nonlinear optimization. Math. Program. 2017. DOI 10.1007/s10107-016-1003-9
- Curtis, Robinson, Zhou. A self-correcting variable-metric algorithm framework for nonsmooth optimization. arXiv:1708.02552
- Bottou, Curtis, Nocedal. Optimization methods for large-scale machine learning. SIAM Review 2018. DOI 10.1137/16M1080173
- Curtis, Scheinberg, Shi. A stochastic trust region algorithm based on careful step normalization. INFORMS J. Optim. 2019. DOI 10.1287/ijoo.2018.0010 (arXiv:1712.10277)
- Berahas, Curtis, Zhou. Limited-memory BFGS with displacement aggregation. arXiv:1903.03471
- Burke, Curtis, Wang, Wang. Inexact sequential quadratic optimization with penalty parameter updates within the QP solver. SIAM J. Optim. 2020. DOI 10.1137/18M1176488 (arXiv:1803.09224)
- Curtis, Li. Gradient sampling methods with inexact subproblem solutions and gradient aggregation. arXiv:2005.07822
- Curtis, Robinson. Regional complexity analysis of algorithms for nonconvex smooth optimization. Math. Program. 2021. DOI 10.1007/s10107-020-01492-3
- Berahas, Curtis, Robinson, Zhou. Sequential quadratic optimization for nonlinear equality constrained stochastic optimization. SIAM J. Optim. 2021. DOI 10.1137/20M1354556 (arXiv:2007.10525)
- Curtis, Robinson, Royer, Wright. Trust-region Newton-CG with strong second-order complexity guarantees for nonconvex optimization. SIAM J. Optim. 2021. DOI 10.1137/19M130563X
- Curtis, Wang. Worst-case complexity of TRACE with inexact subproblem solutions for nonconvex smooth optimization. SIAM J. Optim. 2023. DOI 10.1137/22M1492428 (arXiv:2204.11322)
- Stochastic SQP rungs: DOI 10.1287/moor.2021.0154; DOI 10.1287/ijoo.2022.0008; DOI 10.1007/s10107-023-01981-1; DOI 10.1137/23M1556149; DOI 10.1007/s10957-024-02568-2; DOI 10.1137/23M1569460; DOI 10.1007/s10107-025-02320-2 (arXiv:2408.16186)
- Curtis, Robinson. Practical Nonconvex Nonsmooth Optimization. SIAM 2025. DOI 10.1137/1.9781611978599 (not read)
- Curtis, Zebiane. NonOpt: Nonconvex, Nonsmooth Optimizer. Math. Program. Comput. 2026. DOI 10.1007/s12532-026-00322-5 (arXiv:2503.22826)
- Recent preprints: arXiv:2502.11302; arXiv:2509.00888; arXiv:2510.00417; arXiv:2601.11795; arXiv:2604.00278; arXiv:2605.06945; arXiv:2608.12665
- Curtis. Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization. PhD thesis, Northwestern 2007. http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf

### Stated methodology (primary)
- Research, Errata, Editorship/Reviewership, Software and Talks pages: https://coral.ise.lehigh.edu/frankecurtis/research/ · https://coral.ise.lehigh.edu/frankecurtis/errata/ · https://coral.ise.lehigh.edu/frankecurtis/editorshipreviewship/ · https://coral.ise.lehigh.edu/frankecurtis/software/ · https://coral.ise.lehigh.edu/frankecurtis/talks/
- Slides, 2008–2026: https://coral.ise.lehigh.edu/frankecurtis/files/talks/infopt_08.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/siopt_11.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/copper_12.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/cse_15.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/google_16.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/oaxaca_17.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/ismp_18.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/mopta_18.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/us-mex_18.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/iccopt_semi_19.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2021_ecom_public.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2022_neurips.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2023_eucco.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2024_ismp.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2025_neurips.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/talks/2026_vtech.pdf
- Syllabi: https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2025FallISE403.pdf · https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2019SpringISE417.pdf
- NonOpt homepage: https://frankecurtis.github.io/NonOpt/

### Process evidence (primary)
- Code: https://github.com/frankecurtis/NonOpt (commit history, manual, source) · https://github.com/frankecurtis/PIPAL · https://github.com/frankecurtis/TRACE · https://github.com/frankecurtis/StochasticSQP
- Ipopt inexact option: https://github.com/coin-or/Ipopt/blob/stable/3.14/configure.ac
- PIPAL preprint, 2010: https://optimization-online.org/2010/06/2661/
- Curriculum vitae (revised 2026-04-07): https://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf

### Students, collaborators and peers (secondary)
- Theses: Que 2016, https://web.archive.org/web/20200319034744/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3774&context=etd · Wang 2015, https://web.archive.org/web/20200318151147/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3862&context=etd · Han 2015, https://web.archive.org/web/20200322073308/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3626&context=etd · Guo 2017, https://web.archive.org/web/20200322040506/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3621&context=etd · Mitchell 2014, https://cs.nyu.edu/media/publications/mitchell_tim.pdf
- Genealogy: https://www.mathgenealogy.org/id.php?id=130450
- Critics and commentators: Hinder, Ye, arXiv:1801.03072 · Na, Anitescu, Kolar, DOI 10.1007/s10107-022-01846-z · O'Neill, arXiv:2408.16656 · Wright, arXiv:2510.15734 · Cartis, Gould, Toint, arXiv:1709.07180 · Jiang et al., arXiv:2311.11489 · Kungurtsev, Mitchell, Vyhlídal, arXiv:1812.11630 · Werner, Overton, Peherstorfer, DOI 10.1137/22M1500137 · Huber thesis, DOI 10.5451/unibas-006145479 · Hicken, DOI 10.1007/s11081-014-9258-6
- Peers' papers named in the Roundtable Card: DOI 10.1137/S1052623403426556 · DOI 10.1007/s10107-004-0559-y · DOI 10.1007/s101070100244 · DOI 10.1137/S1052623499350013 · DOI 10.1007/s10107-009-0286-5 · DOI 10.1007/s10107-008-0244-7 · DOI 10.1007/s10107-006-0706-8 · DOI 10.1023/A:1018665102534 · DOI 10.1137/20M1373190

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
