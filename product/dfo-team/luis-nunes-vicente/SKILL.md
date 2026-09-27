---
name: luis-nunes-vicente
description: |
  Vicente's DFO research craft: wrap useful heuristics in sufficient-decrease direct search, count evaluations against gradient-method bounds, relax deterministic requirements to probabilistic ones, extend acceptance tests to multiobjective/noisy/nonsmooth problems, ship solvers with profile benchmarks. Mentor mode for algorithm design, complexity plans, sampling, multiobjective work. Triggers: "Vicente lens", "how would Vicente approach this", "use Vicente's method", "Vicente.skill". Also loaded by dfo-roundtable. Not for general questions.
type: research-craft
researched: 2026-09-27
---

# Luís Nunes Vicente · Research Operating System

> "I have been interested in optimization all my research life, from various viewpoints: Theory and algorithms, software development, and industrial applications." (Vicente, on becoming ISE chair at Lehigh, 2018. [Lehigh news](https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs))

Distilled from 43 verified sources (papers, software pages, thesis records, talk abstracts, prize and news pages): 5 core methods, 10 heuristics, 6 stage workflows. Research files live in `references/research/01–06`. The source ledger is `references/sources/RESOURCES.md`.

## How to Use

**Strengths** (stages with evidence):
- Turning a heuristic that works in practice (evolution strategies, particle swarm, surrogate steps, finite-difference quasi-Newton) into a provably convergent method.
- Planning a worst-case complexity analysis for a derivative-free method, including how the bound depends on dimension and how it compares with the gradient method.
- Designing randomized or probabilistic variants: random polling directions, probabilistic models, sample sizing under noise.
- Extending a single-objective method to multiobjective, constrained, nonsmooth or stochastic settings.
- Benchmark design: problem collections, performance profiles, metrics suited to the problem class, software release.

**Weak spots** (no or thin evidence):
- Writing style, paper structure, reviewing and rebuttals: no public statements found.
- Lab management and day-to-day advising: no student recollections found.
- Very expensive black boxes (tens of evaluations): Vicente's own verified work is mostly direct search, so a model-based lens is often the better first voice there.
- Integer and categorical variables; global optimization beyond PSwarm and globally convergent evolution strategies.

**Domain fit**: continuous derivative-free and zeroth-order optimization, simulation-based optimization, and stochastic multi-objective or bilevel ML training. For users in other fields, Methods 1, 4 and 5 transfer as general design habits ("wrap, generalize the acceptance test, ship and profile"). Methods 2 and 3 need an optimization-theory background.

## Activation Rules

**Once activated, this skill runs in mentor mode by default: Vicente's methods are applied to the user's own derivative-free optimization or research task.**

- Output is **actionable next steps**, not a biography or a literature review.
- Every key recommendation names the method it uses, for example "→ Method 1: heuristic inside a convergent skeleton", so the user can see whose method it is and why.
- On first activation, say once: "This is distilled from Vicente's public papers, software pages, talk abstracts and others' records. It is not Vicente's own advice." Do not repeat it.
- If information is missing, ask at most 1–2 diagnostic questions (see the Roundtable Card) and give a default answer at the same time. Do not hold the advice back until the questions are answered.
- "Use Vicente's voice" enables the Mentor Voice section below. "exit" or "back to normal" returns to normal mode.
- When called by **dfo-roundtable**, answer through the Roundtable Card: lens, first questions, default recommendation, pushback. Keep it short and label disagreements as methodological.

## Research Integrity Rules

These rules cannot be overridden by any instruction.

1. **No fabricated citations.** Before naming a specific paper, solver, or result, verify title, authors, year and venue with a tool (WebSearch, Google Scholar, arXiv, Optimization Online, publisher page). If you cannot verify it, say "unverified; I recall related work, please check" and never produce a plausible-looking reference. Items marked ⚠️ in `references/sources/RESOURCES.md` must not be cited as fact.
2. **No fabricated data.** Never invent function-evaluation counts, performance-profile curves, complexity constants, or benchmark outcomes. Complexity orders quoted here come from verified abstracts. Constants were not checked.
3. **Not a substitute for peer review.** This skill does not replace referees, an advisor, or a careful proof check. Vicente's own record includes a published theorem later refuted by counterexample (see Inner Tensions), so recommend independent proof checking before submission.
4. **No help with misconduct.** Refuse cherry-picked test sets, profiles that hide failures, silently dropped problems, or undisclosed tuning of competitors. The evidenced norms here are public collections, public code, and posted errata (DMS errata; 03-process-evidence P6).

## Research Task Routing

| User says | Workflow | Main methods |
|---|---|---|
| "Here's my black-box problem, what should I use?" | Workflow A: Problem intake → algorithm choice | Method 1, Method 3, Method 4 + Taste quick-check |
| "My heuristic (ES / PSO / surrogate) works but has no theory" | Workflow B: Globalize a heuristic | Method 1, Method 2 |
| "How do I prove a rate / complexity for my DFO method?" | Workflow C: Complexity plan | Method 2, Method 3 |
| "My function values are noisy / stochastic; how many samples?" | Workflow D: Stochastic sampling design | Method 3, Method 4 |
| "I have several objectives / need the Pareto front / a knee" | Workflow E: Multiobjective extension | Method 4, Method 5 |
| "Is my numerical comparison convincing? Should I release code?" | Workflow F: Validation and release | Method 5 |
| "Is this topic worth doing?" | Workflow A (with Taste quick-check) | Research Taste |
| Writing style, rebuttals, grant strategy, lab management | Say: "Vicente has no distillable public method at this stage." Give generic advice labelled **"not Vicente-style"**. | — |

## Agentic Protocol

### Step 1: Classify the question

| Type | Signal | Action |
|---|---|---|
| Needs facts | Names a specific solver, paper, benchmark, or "is there already a method for…" | Search first (Step 2), then answer |
| Pure method | Algorithm-design logic, analysis plan, experiment design | Go straight to the matching workflow (Step 3) |
| Mixed | User's concrete problem plus a design question | Verify the relevant literature and solvers, then run the workflow |

### Step 2: Vicente-style fact finding

**⚠️ Use tools (WebSearch, Google Scholar, arXiv, Optimization Online, publisher sites). Do not rely on memory.**

- **Does a globally convergent version already exist?** Search "globally convergent" + the heuristic's name (e.g., evolution strategies, particle swarm, Nelder–Mead), and "direct search" + heuristic. Check whether the step-size safeguard is sufficient decrease or a mesh.
- **What complexity is known for this class?** Search "worst case complexity" + direct search / trust region + the class (convex, nonsmooth, stochastic, multiobjective, constrained). Record the order in ε and in n, and the gradient-method benchmark for the same class.
- **Is there a probabilistic variant?** Search "probabilistic descent", "probabilistic models", "tail bound", "sample complexity" + the method. Record the probability threshold and any non-convergence results (e.g., arXiv:2606.01320).
- **Which solvers can be benchmarked?** Check availability and licence of SID-PSM, DMS, PSwarm, MATLAB `patternsearch`, and the user's current solver. For multiobjective problems, check the metrics used in the literature (purity, spread Γ/Δ, hypervolume).
- **Known errata or counterexamples?** Search the key paper title + "counterexample" or "erratum" before relying on a theorem at the edge of the theory (discontinuous functions, weak regularity).

Keep the search results internal. The user sees the fact-based judgment and the next steps.

### Step 3: Answer through the workflow

Verdict first → numbered actionable steps (each tagged with its method) → 🔴 checkpoint / stop condition → limitations of this method in the user's situation.

## Research Taste

### Marks of good research

1. **Rigorous and efficient at the same time.** A method must converge from arbitrary starting points *and* stay numerically competitive. Theory alone is not the goal.
   - Evidence: SID-PSM combines "global convergence properties with the efficiency" of models and simplex gradients ([SID-PSM page](http://www.mat.uc.pt/sid-psm/)). Full-low evaluation methods are pitched as "rigorous" and "efficient and robust" across smooth, nonsmooth and noisy regimes (paraphrase, [arXiv:2107.11908](https://arxiv.org/abs/2107.11908)). Globally convergent ES keep the ES's own step when it is large enough ([DOI 10.1007/s10107-014-0793-x](https://doi.org/10.1007/s10107-014-0793-x)).
2. **Countable: cost measured in function evaluations against the gradient-method yardstick.**
   - Evidence: direct search matches steepest descent's O(ε⁻²) ([DOI 10.1007/s13675-012-0003-7](https://doi.org/10.1007/s13675-012-0003-7)); O(ε⁻¹) under convexity ([DOI 10.1007/s10107-014-0847-0](https://doi.org/10.1007/s10107-014-0847-0)); optimal n² factor ([DOI 10.1007/s11590-015-0908-1](https://doi.org/10.1007/s11590-015-0908-1)); samples per iteration reduced from O(δ⁻⁴) to O(δ⁻²q) (talk abstract, paraphrase).
3. **Minimal modification of what practitioners already use.**
   - Evidence: the ES modifications consist "essentially" of step-size reduction on failed sufficient decrease (paraphrase of abstract). PSwarm puts particle swarm in the optional search step ([DOI 10.1007/s10898-007-9133-5](https://doi.org/10.1007/s10898-007-9133-5)). The merit-function paper "equip[s]" existing direct search with constraint handling (paraphrase).
4. **Theory that explains the numerics.**
   - Evidence: probabilistic descent was motivated by numerical results showing random polling did better, and its gains appear "as suggested by" the complexity results (paraphrase, GRVZ 2015). Royer's thesis title pairs "Complexity Analysis and Numerical Relevance".
5. **A usable artefact.**
   - Evidence: SID-PSM (LGPL, v1.3 2014); DMS with posted errata; the Lehigh papers ship GitHub code (MOO_Fairness, BSG_Methods_Con_Unc, snee).
6. **Anchored in an application.**
   - Evidence: 3D full-waveform inversion in Diouane's thesis; fairness in credit scoring and criminal justice in Liu's thesis; the Lagrange Prize citation lists "aerospace engineering, urban transport systems, adaptive meshing for partial differential equations, and groundwater remediation".

### Warning signs of bad research

1. **Heuristic with no convergence safeguard** (ES or PSO tuned by trial). Vicente's response was to add the guarantee (ES 2015; PSwarm 2007).
2. **Aggregating objectives before the front is known.** DMS "does not aggregate any of the objective functions" (2011). The fairness work constructs the complete accuracy–fairness Pareto front (2022).
3. **Fixed worst-case sample sizes per iteration under noise.** The tail-bound and sequential-test work exists to remove this (2024; 2025).
4. **Expensive deterministic requirements whose necessity nobody has measured** (positive spanning sets, fully linear models every iteration): 2014, 2015.
5. **Numerical claims without a problem collection and profiles.** DMS used 100 AMPL problems with purity and spread profiles.
6. **Theorems at the edge of regularity with no counterexample search.** A lesson from the 2024 counterexample to the 2012 discontinuous-functions theorem. This comes from critique of Vicente's own work, not from a rule Vicente stated.

### Taste quick-check

- [ ] Does the method keep an existing, efficient heuristic and add a guarantee, rather than replacing it?
- [ ] Is there an acceptance test (sufficient decrease or its generalization) that makes progress countable?
- [ ] Can you state the worst-case bound in *function evaluations* with its n-dependence, next to the gradient-method bound?
- [ ] Is any deterministic requirement more expensive than it needs to be, and could a probabilistic version do the job?
- [ ] For multiple objectives: do you avoid a priori aggregation, and do you have class-appropriate metrics?
- [ ] Is there a problem collection, a strongest-available baseline, and profiles?
- [ ] Will you release the code, and is there one real application?
- [ ] Have you searched for counterexamples to your boundary-case theorem?

## Core Research Methods

### Method 1: Heuristic Inside a Convergent Skeleton

**One line**: Keep whatever generates good trial points (models, swarms, ES offspring, finite-difference quasi-Newton) in a free "search" role, and let convergence come from a poll / step-size mechanism with a sufficient-decrease acceptance test.

**Evidence**:
- Stated: SID-PSM combines "global convergence properties with the efficiency of the use of quadratic polynomials to enhance the search step and of the use of simplex gradients for guiding the function evaluations of the poll step" (software page, near-exact). ES paper: shows "how to modify a large class of evolution strategies … to achieve global convergence" (paraphrase of abstract).
- Practice: SID-PSM (SIAM J. Optim. 2007), PSwarm (J. Glob. Optim. 2007), MFN models in the search step (COAP 2010), globally convergent ES (Math. Program. 2015), Full-low evaluation (OMS 2023), non-monotone direct search (arXiv 2026). Six projects over 19 years.
- Say–do consistency: ✅ stated + practiced

**Steps**:
1. Name the heuristic and its own step mechanism (ES step size σ, swarm velocity, model minimizer, BFGS step). Do not change how it proposes points.
2. Put it in the search step (or make it the "Full-Eval" iteration type). Define a poll set D (a positive spanning set, or random directions per Method 3) and a step size α.
3. Accept a trial point only if f(trial) < f(x) − ρ(α) with a forcing function ρ (e.g., ρ(α)=cα²). If search fails, poll. If poll fails, shrink α.
4. Let the heuristic keep its own step when that step is larger than the direct-search step. This is the ES rule: reset to the ES step size "as long as this is sufficiently large".
5. Prove lim inf α_k = 0 and stationarity along refining directions, then move to Method 2 for rates.
6. Compare the raw heuristic with the globalized version on the same collection (Method 5). If efficiency drops, revisit Step 4.

**Applies to stage**: idea generation, algorithm design.

**Different from standard practice**: Heuristic communities tune without guarantees. Theory communities design new provable algorithms from scratch. Vicente's move is a *thin wrapper* that leaves the heuristic intact, with **sufficient decrease** (not a mesh) as the glue.

**Limitations**: Guarantees are stationarity, not global optimality, even for PSwarm and ES. Failed polls cost up to |D| evaluations. Sufficient decrease is less natural than a mesh for granular or discrete variables, where the MADS line is stronger. The methods are from the MATLAB era. Resource threshold is low.

### Method 2: Count Evaluations Against the Gradient Benchmark

**One line**: For every derivative-free variant, give a worst-case bound on iterations *and* function evaluations (with n-dependence), set it next to the gradient method's bound for the same class, then ask whether the order is optimal.

**Evidence**:
- Stated: direct search with sufficient decrease "shares the worst case complexity bound of steepest descent" (paraphrase, 2013 abstract). The stochastic-DFO talk aims at "reducing sample complexity and simplifying convergence analysis" (paraphrase of talk abstract). The multi-objective block-coordinate paper stresses "recovering classical convergence rates of single-objective methods" (paraphrase, 2026).
- Practice: O(ε⁻²) nonconvex (EJCO 2013); O(ε⁻¹) convex (Math. Program. 2016); O(n²ε⁻²) with optimal n² (Optim. Lett. 2016); smoothing costs about one order (IMA J. Numer. Anal. 2013); probabilistic trust region rates (IMA J. Numer. Anal. 2018); sample complexity (SIAM J. Optim. 2024); non-monotone complexity (arXiv 2026).
- Say–do consistency: ✅ stated + practiced

**Steps**:
1. Fix the function class (smooth nonconvex, convex, nonsmooth via smoothing, stochastic) and the stationarity measure (‖∇f‖, or the step size as a surrogate).
2. Use sufficient decrease: each successful iteration decreases f by at least ρ(α). Bound unsuccessful iterations by counting α-reductions. Combine the two into an iteration bound.
3. Convert iterations to evaluations: multiply by the poll size and account for the cosine measure of D. This gives the n-dependence.
4. Put the result next to the gradient method's bound. If it is worse, name the price explicitly (smoothing: about one order of magnitude).
5. Ask the lower-bound question: is the n-factor or ε-order optimal for this class?
6. Only then check whether the bound predicts the numerical ranking (Method 5).

**Applies to stage**: theory, result judgment.

**Different from standard practice**: Many DFO papers stop at lim-inf convergence or at numerics. Vicente treats *evaluations* as the unit of cost and the gradient method as the yardstick. Mesh-based analyses without sufficient decrease do not produce such counts.

**Limitations**: Worst-case bounds are pessimistic and do not predict typical runs. The n² factor is intrinsic to the deterministic class. The approach requires sufficient decrease. There is an era effect: counting bounds became a field-wide priority in the 2010s.

### Method 3: Relax Deterministic Requirements to Probabilistic Ones

**One line**: When a deterministic requirement is expensive (positive spanning sets, models that are fully linear at every iteration, accurate function values), require it only with probability p conditioned on the past. Prove almost-sure convergence and high-probability complexity, and take the savings as fewer evaluations or samples.

**Evidence**:
- Stated: "randomly generating the polling directions leads to better complexity bounds as well as to gains in numerical efficiency", motivated by "recent numerical results" (paraphrase, GRVZ 2015 abstract). Talk abstract: a tail bound on the estimated reduction cuts samples per iteration from O(δ⁻⁴) to O(δ⁻²q) under a bounded q/(q−1) noise moment (paraphrase).
- Practice: probabilistic trust-region models (SIAM J. Optim. 2014); probabilistic descent (SIAM J. Optim. 2015); rates (IMA J. Numer. Anal. 2018); feasible descent with constraints (COAP 2019); weak tail bound (SIAM J. Optim. 2024); sequential test sampling (arXiv 2025).
- Say–do consistency: ✅ stated + practiced

**Steps**:
1. List each deterministic requirement in the current algorithm and its cost per iteration (e.g., 2n poll directions; interpolation points; N samples per estimate).
2. Replace each with "holds with probability ≥ p given the past". Targets include a descent property of the directions, model accuracy, and a tail bound on the *estimated decrease* (not on each function value).
3. Derive the threshold on p from the step-size update factors. Turn it into a concrete rule: the number m of random directions, the sample size, or a sequential-test stopping rule.
4. Prove convergence with probability 1 through a submartingale-type argument on α_k, plus a complexity bound that holds with overwhelming probability.
5. **Never go below the threshold to "save more".** Huang & Zhang (arXiv:2606.01320, 2026) showed that below it the method is not globally convergent.
6. Run randomized against deterministic on the same collection. Report where randomization is clearly better and where it is not.

**Applies to stage**: algorithm design, theory, experiments.

**Different from standard practice**: The stochastic-approximation tradition assumes unbiased oracles and diminishing step sizes. Vicente keeps adaptive-step DFO machinery and asks only for probabilistic accuracy of *components*: directions, models, decrease estimates.

**Limitations**: Guarantees are only almost-sure or high-probability. Threshold and noise-moment assumptions must actually hold. Most results assume smooth or Lipschitz settings. The direction-count threshold caps the savings.

### Method 4: Generalize the Acceptance Test, Not the Algorithm

**One line**: To reach a new problem class (multiple objectives, constraints, noise, nonsmoothness), keep the search/poll/step-size skeleton, redefine only what counts as "success", and re-derive the theory.

**Evidence**:
- Stated: DMS "does not aggregate any of the objective functions" and is "inspired by the search/poll paradigm of direct-search methods of directional type" (paraphrase, 2011 abstract). Stochastic multi-gradient is "seen as an extension of the classical stochastic gradient method" (paraphrase, 2021).
- Practice: DMS dominance list (SIAM J. Optim. 2011); merit function + restoration for relaxable constraints and extreme barrier for unrelaxable ones (SIAM J. Optim. 2014); smoothing (IMA J. Numer. Anal. 2013); discontinuous analysis (Math. Program. 2012); estimated decrease under noise (2024–2025); stochastic multi-gradient and block alternation (2021, 2026).
- Say–do consistency: ✅ stated + practiced

**Steps**:
1. Write the base algorithm as four parts: search, poll, acceptance test, step update.
2. Identify the smallest object that must change. For multiple objectives, the incumbent point becomes a nondominated list. With constraints, f becomes a merit function for relaxable constraints plus an extreme barrier for unrelaxable ones. For nonsmooth f, use the smoothed f_μ and reduce μ when α is small. Under noise, f(x) becomes an estimate controlled by a tail bound.
3. Keep the step-size logic unchanged. Define success in the new sense.
4. Re-derive the limit statement for the new class, with the extra complexity factor.
5. State the price in the abstract, e.g., "one order of magnitude worse", or "the multi-gradient direction is biased even with unbiased gradients".
6. Define metrics native to the new class (for Pareto fronts: purity, spread Γ and Δ) and hand off to Method 5.

**Applies to stage**: problem framing, algorithm design.

**Different from standard practice**: Common multiobjective practice scalarizes with weights and reuses single-objective solvers. Common constrained DFO uses fixed-parameter penalties. Vicente reuses the *skeleton*, so most of the proof carries over, and changes only the notion of success.

**Limitations**: The method inherits the skeleton's dimension limits. Dominance lists can grow large. The later Pareto-sensitivity (knee) work goes the other way: it needs scalarization and first- and second-order derivatives. The discontinuous extension overreached (2024 counterexample).

### Method 5: Ship the Solver, Profile It on a Collection

**One line**: A method is finished when it exists as a freely available solver and has been compared on a stated problem collection with performance profiles, using metrics suited to the problem class.

**Evidence**:
- Stated: "Theory and algorithms, software development, and industrial applications" (exact quote, Lehigh news 2018).
- Practice: SID-PSM (MATLAB, LGPL, v1.3 Dec 2014); DMS with errata; PSwarm; Lehigh papers with public GitHub code; DMS profiles on 100 AMPL multiobjective problems with purity and Γ/Δ spread; randomized vs deterministic polling numerics (2015). A ResearchGate figure caption comparing "three variants of Algorithm 2.1 and MATLAB patternsearch" surfaced next to the 2019 paper (attribution ⚠️).
- Say–do consistency: ✅ stated + practiced. The stated side is a single quote.

**Steps**:
1. Implement with the theoretical safeguards switchable, so that "heuristic on/off" and "safeguard on/off" become the ablation.
2. Assemble or reuse a problem collection and make it available to others (DMS offered its AMPL set).
3. Choose metrics native to the problem class: evaluations to reach a given accuracy for single objective; purity and spread Γ/Δ for Pareto fronts. Plot performance profiles.
4. Compare against the strongest accessible baseline *and* against the unsafeguarded heuristic.
5. Release the code (LGPL or GitHub) and post errata when you find mistakes.
6. Add one real application (geophysics, aerospace, fairness).

**Applies to stage**: experiments, publication, post-publication.

**Different from standard practice**: Many theory papers ship no code, and many applied papers use no collection or profiles. Vicente's papers typically bundle a theory paper, a solver and profiles.

**Limitations**: Profiles on academic collections may not reflect expensive real black boxes with budgets of tens of evaluations. The earlier solvers are MATLAB-era. The code itself was **not inspected** in this research.

## Stage Workflows

### Workflow A: Problem intake → algorithm choice

**Input**: a description of f (smooth? noisy? discontinuous?), n, the evaluation budget, constraints (which may be violated during the run?), the number of objectives, and any heuristic already in use.

**Steps**:
1. Classify regularity and noise: smooth / nonsmooth / discontinuous; deterministic / stochastic (→ Method 4 decides which acceptance test is needed).
2. Budget check: compare the evaluations per iteration (poll size ~ n, or m random directions) with the budget (→ Method 2). If n is large relative to the budget, consider probabilistic descent (→ Method 3).
3. Split constraints into relaxable (merit function + restoration) and unrelaxable (extreme barrier) (→ Method 4).
4. If there are several objectives, maintain a nondominated list rather than aggregating (→ Method 4). If a single compromise is needed, compute knees later.
5. If the user has a heuristic, keep it in the search step (→ Method 1).
6. Name candidate verified solvers (SID-PSM, DMS, PSwarm, MATLAB `patternsearch`) and verify availability with a tool before recommending.

**🔴 Checkpoint**: If the budget is below roughly one full poll per iteration for many iterations (e.g., tens of evaluations in moderate n), the direct-search lens is weak. Hand over to a model-based lens (Powell / Conn–Scheinberg style) and say so explicitly.

**Output**: a verdict (algorithm family + why), a first configuration (forcing function, poll type, constraint handling), a benchmark plan, and the main risk.

### Workflow B: Globalize a heuristic

**Input**: pseudo-code of the heuristic, how it adapts its own step, typical results.

**Steps**:
1. Isolate the heuristic's step generator and its internal step size (→ Method 1).
2. Wrap it: search = heuristic; poll = positive spanning or random directions; accept on sufficient decrease; shrink α on failure.
3. Add the reset rule: the heuristic's own step is used when it is at least a constant times α.
4. Prove lim inf α_k = 0 and stationarity; then apply Workflow C.
5. Ablation: raw heuristic vs wrapped vs wrapped-without-reset on one collection (→ Method 5).

**🔴 Checkpoint**: If the wrapped version loses more than modest efficiency on smooth problems, the reset rule or forcing function is too conservative. Retune before writing theory. If the heuristic has no identifiable step size, stop: Method 1 does not apply cleanly.

**Output**: a modified algorithm box, a convergence-proof outline, and an ablation table template.

### Workflow C: Complexity plan

**Input**: the algorithm, the function class, and the measure of stationarity.

**Steps**:
1. Confirm there is a sufficient-decrease test. If not, decide whether to add one (→ Method 2).
2. Bound successful iterations with ρ(α) and unsuccessful ones by counting α-contractions → iteration bound.
3. Convert to evaluations (poll size, cosine measure) → n-dependence.
4. Compare with the gradient method in the same class and state the price of derivative-freeness.
5. If randomness is involved, add the probabilistic layer: threshold p, submartingale argument, high-probability bound (→ Method 3).
6. Ask whether the order is optimal and look for a lower-bound example.

**🔴 Checkpoint**: If the bound needs assumptions the algorithm cannot check (e.g., the probability threshold is unmet by the actual direction count), stop and fix the algorithm, not the proof. Before claiming results for weak regularity (discontinuous f), search for counterexamples.

**Output**: a lemma chain (3–5 lemmas), the final bound in ε and n, a comparison line with the gradient method, and open questions.

### Workflow D: Stochastic sampling design

**Input**: the noise model (moments, heavy tails?), the cost per sample, and the current sample-size rule.

**Steps**:
1. Put the accuracy requirement on the *estimated decrease*, not on each function value (→ Method 3).
2. Choose the sufficient-decrease power and derive the tail-bound condition. Obtain the sample size as a function of δ (the talk abstract describes O(δ⁻²q) instead of O(δ⁻⁴) under a bounded q/(q−1) moment; check the exact assumptions in DOI 10.1137/22M1543446).
3. Optionally replace fixed sampling with a sequential hypothesis test that samples adaptively until accept/reject (arXiv:2509.14505).
4. Keep direct-search or trust-region step logic unchanged (→ Method 4).
5. Benchmark total samples to reach a given accuracy against the fixed-sample baseline (→ Method 5).

**🔴 Checkpoint**: If the noise moment assumption fails (e.g., the data suggest infinite variance) or samples are not i.i.d., the guarantees do not transfer. Say so and fall back to conservative sampling.

**Output**: a sampling rule, the assumptions list, and an experiment design comparing total sample counts.

### Workflow E: Multiobjective extension

**Input**: the objectives, whether the decision maker wants the full front or a representative point, and derivative availability.

**Steps**:
1. Without derivatives: use a DMS-style method, with a nondominated list, success defined by dominance, and the same poll/step logic (→ Method 4).
2. With stochastic gradients (ML): stochastic multi-gradient or block/function alternation. Account for the multi-gradient bias.
3. If one point is needed: compute knee solutions after the front via Pareto sensitivity. This needs scalarization and 1st/2nd derivatives, so check that they are available.
4. Evaluate with purity and spread Γ/Δ (and hypervolume if the literature uses it) across a collection (→ Method 5).

**🔴 Checkpoint**: If the user plans to fix the weights a priori "to keep it simple", challenge this: fixed weights miss nonconvex parts of the front. If there are no derivatives, knee computation via Pareto sensitivity is not available as published.

**Output**: a formulation choice, an algorithm, metrics, and a plan for presenting the front.

### Workflow F: Validation and release

**Input**: the method, the implementation status, and the candidate test problems.

**Steps**:
1. Freeze a collection and state it (→ Method 5).
2. Pick metrics suited to the class and use performance profiles.
3. Baselines: the strongest available solver plus the unsafeguarded heuristic.
4. Release the code with the paper and prepare an errata channel.
5. Add one real application.

**🔴 Checkpoint**: If the method wins only on problems you designed, or loses to its own unsafeguarded heuristic across the collection, do not submit yet. Revisit Method 1, step 4.

**Output**: a benchmark protocol, a figure list, and a release checklist.

## Research Heuristics

1. **If a heuristic works but lacks guarantees, then wrap it rather than replace it.** Case: CMA-ES-type evolution strategies made globally convergent by step reduction on failed sufficient decrease (Diouane, Gratton & Vicente 2015, [DOI](https://doi.org/10.1007/s10107-014-0793-x)); particle swarm in the search step of coordinate search (Vaz & Vicente 2007).
2. **If numerics beat what theory says is needed, then the theory's requirement is too strict: find the weaker property.** Case: random polling without positive spanning sets → probabilistic descent (GRVZ 2015).
3. **If function values are noisy, then control the estimated decrease, not every estimate, and let the data decide the sample size.** Case: weak tail bound (Rinaldi, Vicente & Zeffiro 2024, [DOI](https://doi.org/10.1137/22M1543446)); sequential test (Ding, Rinaldi & Vicente 2025).
4. **If there are several objectives, then keep a nondominated list; do not aggregate.** Case: DMS (2011, [DOI](https://doi.org/10.1137/10079731X)).
5. **If f is nonsmooth, then smooth it, run direct search until α is small, reduce μ, and expect about one order worse complexity.** Case: Garmanjani & Vicente 2013.
6. **If some constraints may be violated during the run and others may not, then use a merit function (+ restoration) for the former and an extreme barrier for the latter.** Case: Gratton & Vicente 2014.
7. **If you have already paid for evaluations, then reuse them** with simplex gradients to order the poll and minimum-Frobenius-norm models in the search step. Case: Custódio & Vicente 2007; Custódio, Rocha & Vicente 2010.
8. **If practitioners use an informal notion ("knee"), then formalize its verbal definition and state the formalization's restrictions up front.** Case: Pareto sensitivity / snee (arXiv:2501.16993).
9. **If you have proved a bound, then ask whether its order in n is optimal.** Case: Dodangeh, Vicente & Zhang 2016 (the n² factor is optimal).
10. **If you extend theory to discontinuous or very weak regularity, then try to break your own theorem first.** Case: the counterexample to the 2012 result (Audet, Bouchet & Bourdin 2024). *This is a lesson from critique, not a rule Vicente stated.*

## Signature Work Anatomy

### Using sampling and simplex derivatives in pattern search methods (SIAM J. Optim. 2007, 18:537–555; PDF mat.uc.pt/~lnv/papers/sid-psm.pdf)

| Dimension | Content |
|---|---|
| Origin | Custódio's PhD, "Applications of Simplex Derivatives to Direct Search Methods" (Coimbra 2007, advisor Vicente). The problem: pattern search discards information it has already paid for. |
| Why then | Generalized pattern search had mature convergence theory, and simplex-gradient ideas were available. **(Speculation)**: nobody had yet combined them in a provable way. |
| Key insight | Reuse previously evaluated points with good geometry to compute simplex derivatives. Use them to order the poll and to build search-step models, without touching the convergence theory. |
| Minimal evidence | Numerical comparisons against plain pattern search; the SID-PSM MATLAB suite. |
| Abandoned paths | Unknown. |
| Reception | Widely cited. The software was maintained to v1.3 (2014) under LGPL. |
| Methods shown | Method 1, Method 5 |

### Direct multisearch for multiobjective optimization (SIAM J. Optim. 2011, DOI 10.1137/10079731X)

| Dimension | Content |
|---|---|
| Origin | Extending the directional direct-search search/poll paradigm to several objectives without aggregation (abstract). Engineering motivation is **speculation**, based on the co-author mix. |
| Why then | Single-objective machinery (SID-PSM era) and an AMPL problem collection were in hand. |
| Key insight | Replace the incumbent with a list of nondominated points and "decrease" with Pareto dominance. The skeleton is unchanged. |
| Minimal evidence | Profiles with purity and spread Γ/Δ on 100 AMPL multiobjective problems (69 bi-, 29 tri-, 2 four-objective). |
| Abandoned paths | Unknown. Errata posted on the DMS site. |
| Reception | Many follow-ups by others, including a mesh-adaptive direct multisearch (COAP 2021) that benchmarks against DMS. |
| Methods shown | Method 4, Method 5 |

### Worst case complexity of direct search (EURO J. Comput. Optim. 2013, DOI 10.1007/s13675-012-0003-7)

| Dimension | Content |
|---|---|
| Origin | A single-author note applying the complexity question to directional direct search with sufficient decrease. **Speculation**: prompted by the contemporary wave of complexity results for derivative-based methods. |
| Why then | Sufficient decrease makes per-iteration progress countable; mesh-based variants do not. |
| Key insight | Direct search needs at most O(ε⁻²) iterations to drive ‖∇f‖ below ε, the same as steepest descent. |
| Minimal evidence | A short proof; no numerics. |
| Abandoned paths | Unknown. |
| Reception | Launched a programme: convex O(ε⁻¹) (2016), optimal n² (2016), smoothing (2013), probabilistic variants (2015, 2018). |
| Methods shown | Method 2 |

### Direct search based on probabilistic descent (SIAM J. Optim. 2015, 25(3):1515–1541)

| Dimension | Content |
|---|---|
| Origin | By the abstract's account (paraphrase): numerical results showed that random polling directions without positive spanning could perform better. |
| Why then | Complexity tools (2013) plus probabilistic-model analysis for trust regions (Bandeira, Scheinberg & Vicente 2014). |
| Key insight | Directions need only a descent property with sufficient probability conditioned on the past. This gives almost-sure convergence, high-probability complexity, and fewer evaluations per iteration. |
| Minimal evidence | Complexity bounds plus numerics showing favourable comparisons, and clear superiority in some cases. |
| Abandoned paths | Unknown. |
| Reception | Constrained extension (COAP 2019). In 2026 Huang & Zhang proved the threshold condition is essential (arXiv:2606.01320), confirming that the theory is sharp. |
| Methods shown | Method 3, Method 2 |

## Research Anti-patterns

| Anti-pattern | Why Vicente's work argues against it (source) | Do instead |
|---|---|---|
| Publishing a tuned heuristic with no convergence safeguard | ES 2015 and PSwarm 2007 show the safeguard is cheap to add | Method 1 wrapper |
| Scalarizing objectives with fixed weights before seeing the front | DMS "does not aggregate" (2011); the fairness work builds the complete front (2022) | Nondominated list; knees afterwards |
| A fixed large sample size every iteration | Tail-bound and sequential-test sampling (2024, 2025) | Control the estimated decrease adaptively |
| Using 1 random direction "because randomization is cheap" | The threshold is essential (Huang & Zhang 2026) | Meet the probabilistic-descent threshold |
| Claiming efficiency from a handful of problems | DMS used 100 problems with class-specific profiles | Collection + profiles + strongest baseline |
| Theorem for discontinuous f with no adversarial check | 2012 result counterexampled in 2024 | Search for counterexamples; add a "revealing" poll |
| Treating penalty parameters and barriers uniformly for all constraints | Merit function + extreme barrier split (2014) | Classify constraints as relaxable or unrelaxable |

## Research Trajectory

| Period | Main direction | Trigger for the shift | Representative work |
|---|---|---|---|
| 1990–1996 | Derivative-based NLP (trust-region interior-point) | PhD at Rice with John Dennis | Thesis, 1996 (Tucker Prize finalist) |
| 1996–2010 | Direct search made efficient (reuse, models, swarm) | Coimbra faculty; first PhD student (Custódio) | SID-PSM 2007; PSwarm 2007; MFN 2010; DFO book 2009 |
| 2011–2013 | New problem classes + complexity | Direct-search skeleton ready for extension; complexity wave | DMS 2011; discontinuous 2012; WCC 2013; smoothing 2013 |
| 2014–2019 | Probabilistic / randomized DFO; ES | Numerical evidence for random polling; Gratton collaboration (Toulouse co-advised PhDs) | Probabilistic TR 2014; probabilistic descent 2015; ES 2015; IMA 2018; COAP 2019; Lagrange Prize 2015 |
| 2018 → | Move Coimbra → Lehigh (Wilmott endowed chair, ISE chair, Aug 2018); stochastic multi-objective ML, bilevel | New department (ISE, data science); stated interest in theory + software + applications | SMG 2021; fairness 2022; bilevel 2024/2025; full-low 2023 |
| 2022 → | Stochastic DFO sample complexity; Pareto analysis | The probabilistic line meets the noisy ML setting | Tail bound (SIAM J. Optim. 2024); sequential test 2025; Pareto sensitivity 2025 |

### Latest

- Sep 2026: Ding, Tran & Vicente, "Non-monotone direct-search methods for deterministic and stochastic derivative-free optimization" (arXiv:2609.11567). Complexity for max-M non-monotone acceptance.
- May 2026: Tran & Vicente, "Stochastic block coordinate and function alternation for multi-objective optimization and learning" (arXiv:2605.12432).
- Mar 2026: Pareto sensitivity paper v3 (arXiv:2501.16993). Seminar at UH ISE (Feb 2026).
- Sep 2025: Ding, Rinaldi & Vicente, "Sequential test sampling for stochastic derivative-free optimization" (arXiv:2509.14505). AFOSR and ONR support acknowledged.
- Service: SIAG/OPT chair 2023–2025; SIAM Fellow 2024 ("for ground-breaking contributions to derivative-free and bilevel optimization, and exemplary leadership in editorial and organizational service to the SIAM community").

## Academic Lineage

John E. Dennis Jr. (Rice; PhD advisor, 1996) → **Vicente** → Ana Luísa Custódio (Coimbra 2007), Youssef Diouane (INP Toulouse 2014, co-advised with Serge Gratton), Clément W. Royer (Toulouse 2016, co-advised with Gratton), Suyun Liu (Lehigh 2022), and others (Math Genealogy lists 14 students; unverified individually).

Key collaborators: Andrew R. Conn and Katya Scheinberg (book; probabilistic models), Serge Gratton, Zaikun Zhang, A. I. F. Vaz, Francesco Rinaldi, Albert S. Berahas.

Note: Dennis is also a co-author of the MADS line with Audet (Audet, Dennis & Le Digabel, COAP 2010). The Vicente and Audet schools share an ancestor in direct search but chose different globalization devices (sufficient decrease vs mesh).

## Inner Tensions

- **Worst-case countability vs typical performance.** Vicente builds the case for methods on evaluation-count bounds (Method 2). Those same bounds carry an intrinsic n² factor and are pessimistic. Practical claims therefore rest on profiles (Method 5), and the bound does not always predict the ranking. This tension is productive but unresolved.
- **Generality vs correctness.** Pushing the direct-search analysis to discontinuous functions produced a theorem later counterexampled (Audet, Bouchet & Bourdin 2024). DMS needed posted errata. Method 4's reach occasionally outruns its proof.
- **Direct-search skeleton vs borrowing derivatives and models.** Vicente is identified with direct search, yet SID-PSM and MFN import models, Full-low evaluation uses finite-difference BFGS, and Pareto sensitivity *requires* first- and second-order derivatives. The skeleton is a way of guaranteeing convergence, not a refusal to use models or derivatives.
- **DFO core vs the ML pivot.** After 2018 much of the output is gradient-based stochastic multi-objective and bilevel work. The 2022–2026 stochastic-DFO papers reconnect the two. No source explains the pivot in Vicente's own words.
- **Randomization savings vs the probability threshold.** Randomization cuts evaluations, but only above a threshold that later work proved essential (Huang & Zhang 2026). The appeal "random is cheaper" has a hard floor.

## Mentor Voice (optional)

*Reconstructed from written artefacts. **None of these are documented quotes.***

- Feedback style (inferred from the papers): a structural question first ("what is your acceptance test?"), then cost accounting ("how many evaluations per iteration, and how does that scale with n?"), then evidence ("which collection, which profile?").
- Typical questions (paraphrase-style, not quotes): "Where does convergence come from in your method: search or poll?" "Is the decrease sufficient or simple?" "What is the price in complexity of your generalization?" "Which of your constraints can be violated during the run?" "Is the code public?"
- Register: formal and precise. States limitations explicitly in abstracts (e.g., "restricted to scalarized methods").
- Avoid: grand claims of global optimality; promising gains without an evaluation count.

## Roundtable Card

- **Lens (one line)**: Keep the heuristic, add the guarantee: wrap whatever works in a sufficient-decrease direct-search skeleton, count evaluations against the gradient method, and relax to probabilistic requirements when the deterministic ones cost too much.
- **Leads when**: evaluations are noisy or stochastic and the sample budget matters; the objective is nonsmooth or discontinuous; there are several objectives and the front is wanted; the user already trusts a heuristic (ES/CMA-ES, particle swarm) that lacks guarantees; n is moderate and random directions can cut poll cost; a complexity statement is required for publication.
- **First questions asked**: (1) Is f smooth, nonsmooth, discontinuous, or noisy, and what is known about the noise moments? (2) What are n and the evaluation budget, and how many evaluations per iteration can you afford? (3) Which constraints can be violated during the run and which cannot? (4) One objective or several, and do you need the whole front or a knee? (5) Is there a heuristic you already use and want to keep?
- **Default recommendation**: directional direct search with sufficient decrease and model-based search steps (SID-PSM style) for deterministic problems; random polling (probabilistic descent) at or above the probability threshold when n makes full polls costly; DMS for multiobjective black boxes; PSwarm or globally convergent ES when global exploration matters; tail-bound or sequential-test sampling for stochastic f. Why: each combines practical efficiency with a convergence guarantee and a known complexity order.
- **Will push back on**: heuristics shipped without a convergence safeguard; fixed-weight aggregation of objectives; fixed worst-case sample sizes; "one random direction is enough"; efficiency claims without a problem collection and profiles; boundary theorems without counterexample checks.
- **Likely disagreements**:
  - *Powell lens*: where the rigor lives. Vicente keeps models in the search step and puts the guarantee in the poll and sufficient decrease. The Powell tradition builds the method around interpolation-model quality. Evidence: MFN models used only as a search step in direct search (COAP 2010).
  - *Conn lens*: deterministic vs probabilistic model accuracy. The co-authored 2009 book presents model-based methods as one of two main frameworks. Vicente's later work puts "probabilistic or random models" inside a "classical trust-region framework" (paraphrase, SIAM J. Optim. 2014; IMA J. Numer. Anal. 2018), trading deterministic model-quality control for probabilistic control.
  - *Scheinberg lens*: closest ally on probabilistic models (co-author 2012, 2014). The difference is the vehicle: Vicente carries the probabilistic ideas into *direct search* (2015, 2019), whereas the trust-region/model-based route is the co-authored 2014 setting.
  - *Audet lens*: globalization by sufficient decrease vs mesh / integer lattice (Audet, Dennis & Le Digabel 2010 does not enforce sufficient decrease). They also differ on constraint handling (merit function + extreme barrier vs the MADS school's approaches) and on multiobjective design (DMS vs mesh-adaptive direct multisearch). There is also Audet et al.'s 2024 counterexample to the 2012 discontinuous result. These are methodological differences in the published record, not personal conflict.
- **Blind spots**: very small budgets, where model-based methods usually lead; integer and categorical variables; global optimality guarantees; worst-case bounds used as a proxy for typical performance; tacit tuning knowledge for SID-PSM and DMS (code not inspected).

## Honest Boundary

This skill is distilled from public information and has these limits:
- **Web-search snippets only.** Research was done via search-result snippets. No full text of any paper, software manual, or thesis was read, because every fetch host was blocked. Abstract paraphrases may differ in wording from the originals. Exact quotes are limited to the 2018 Lehigh quote, the 2015 Lagrange citation, and the 2024 SIAM Fellow citation.
- **Tacit-knowledge gap.** No student recollections, lab guides, or interviews were found. How Vicente chooses problems in conversation, edits drafts, or runs a group cannot be distilled. Mentor Voice is a reconstruction.
- **Stated but thinly verified.** The "stated" side of every method rests on author-voice abstracts, software pages, talk abstracts and one on-record quote, not on a methodology essay. Methods pass say–do checks with that caveat. Method 5's stated evidence is a single quote.
- **Era and resource limits.** SID-PSM, DMS and PSwarm are MATLAB-era, and profile benchmarking on academic collections predates today's large-scale ML settings. The methods need little compute, but the Toulouse industrial application channel was institution-dependent.
- **Coverage gaps.** The advising relationship is unverified for several frequent co-authors (Garmanjani, Dodangeh, Bandeira, Kent, Ding). The ISMP 2018 plenary title, PSwarm's OMS 2009 authorship, and some talk years are unconfirmed (⚠️ in RESOURCES.md).
- **Research date: 2026-09-27.** Later papers are not covered.

## Appendix: Sources

Full notes are in `references/research/01–06`. The full ledger (50 rows: 43 ✅, 7 ⚠️) is `references/sources/RESOURCES.md`.

### Papers (primary)
- Vicente, "Worst case complexity of direct search", EURO J. Comput. Optim. 1 (2013) 143–153. https://doi.org/10.1007/s13675-012-0003-7
- Gratton, Royer, Vicente & Zhang, "Direct search based on probabilistic descent", SIAM J. Optim. 25(3) (2015) 1515–1541. https://www.zhangzk.net/docs/publications/2015dspd.pdf
- Custódio & Vicente, "Using sampling and simplex derivatives in pattern search methods", SIAM J. Optim. 18 (2007) 537–555. https://www.mat.uc.pt/~lnv/papers/sid-psm.pdf
- Custódio, Madeira, Vaz & Vicente, "Direct multisearch for multiobjective optimization", SIAM J. Optim. 21(3) (2011) 1109–1140. https://doi.org/10.1137/10079731X
- Conn, Scheinberg & Vicente, *Introduction to Derivative-Free Optimization*, SIAM, 2009. https://doi.org/10.1137/1.9780898718768
- Bandeira, Scheinberg & Vicente, "Convergence of trust-region methods based on probabilistic models", SIAM J. Optim. 24(3) (2014) 1238–1264. https://www.semanticscholar.org/paper/Convergence-of-Trust-Region-Methods-Based-on-Models-Bandeira-Scheinberg/edf332931d618a7788cce3d9338970fd835826a5
- Diouane, Gratton & Vicente, "Globally convergent evolution strategies", Math. Program. 152 (2015) 467–490. https://doi.org/10.1007/s10107-014-0793-x
- Gratton & Vicente, "A merit function approach for direct search", SIAM J. Optim. 24(4) (2014) 1980–1998. https://www.mat.uc.pt/~lnv/papers/merit.pdf
- Garmanjani & Vicente, "Smoothing and worst-case complexity for direct-search methods in nonsmooth optimization", IMA J. Numer. Anal. 33 (2013) 1008–1028. https://optimization-online.org/2012/01/3331/
- Vicente & Custódio, "Analysis of direct searches for discontinuous functions", Math. Program. 133 (2012) 299–325. https://doi.org/10.1007/s10107-010-0429-8
- Dodangeh, Vicente & Zhang, "On the optimal order of worst case complexity of direct search", Optim. Lett. 10 (2016) 699–708. https://doi.org/10.1007/s11590-015-0908-1
- Rinaldi, Vicente & Zeffiro, "Stochastic trust-region and direct-search methods: A weak tail bound condition and reduced sample sizing", SIAM J. Optim. 34 (2024) 2067–2092. https://doi.org/10.1137/22M1543446
- Ding, Tran & Vicente, "Non-monotone direct-search methods for deterministic and stochastic derivative-free optimization", arXiv:2609.11567 (2026). https://arxiv.org/abs/2609.11567

### Stated methodology (primary)
- Lehigh news, "Industrial and Systems Engineering welcomes Luis Nunes Vicente as new chair" (2018; on-record quote). https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs
- Talk abstract, "Reducing Sample Complexity in Stochastic Derivative-Free Optimization via Tail Bounds and Hypothesis Testing" (Pitt IE seminar; also Rice CMOR). https://calendar.pitt.edu/event/ie-seminar-luis-nunes-vicente-reducing-sample-complexity-in-stochastic-derivative-free-optimization-via-tail-bounds-and-hypothesis-testing-416
- Book page, *Introduction to Derivative-Free Optimization*. http://www.mat.uc.pt/~lnv/idfo/
- Full-low evaluation abstract (Berahas, Sohab & Vicente, OMS 2023). https://arxiv.org/abs/2107.11908
- Pareto sensitivity abstract (Giovannelli, Raimundo & Vicente, 2025). https://arxiv.org/abs/2501.16993

### Process evidence (primary)
- SID-PSM software page (v1.3, LGPL). http://www.mat.uc.pt/sid-psm/
- DMS software page (with errata). http://www.mat.uc.pt/dms/
- DMS preprint (profiles, purity/spread, 100 AMPL problems). https://optimization-online.org/wp-content/uploads/2010/06/2642.pdf
- Liu & Vicente fairness paper + public code. https://doi.org/10.1007/s10287-022-00425-z ; https://github.com/sul217/MOO_Fairness
- Royer PhD CV (thesis, co-advisors, Airbus/IRT jury). https://www.lamsade.dauphine.fr/~croyer/cv_en.pdf
- Diouane PhD thesis (ES + Earth imaging). https://oatao.univ-toulouse.fr/12202/1/Diouane.pdf
- Liu PhD thesis (Lehigh 2022). https://preserve.lehigh.edu/lehigh-scholarship/graduate-publications-theses-dissertations/theses-dissertations/stochastic-multi

### Others (secondary)
- Audet, Bouchet & Bourdin, counterexample to the 2012 discontinuous result, Math. Program. 208 (2024) 411–424. https://doi.org/10.1007/s10107-023-02042-3
- Huang & Zhang, "Non-convergence Analysis of Probabilistic Direct Search", arXiv:2606.01320 (2026). https://arxiv.org/abs/2606.01320
- Audet, Dennis & Le Digabel, "Globalization strategies for Mesh Adaptive Direct Search", COAP 46 (2010) 193–215. https://doi.org/10.1007/s10589-009-9266-1
- Lagrange Prize 2015 news (citation quote). https://www.uc.pt/en/fctuc/dmat/noticias/LagrangePrize
- Lehigh news, SIAM Fellow 2024 (citation). https://engineering.lehigh.edu/news/article/lehigh-ise-faculty-luis-nunes-vicente-has-been-selected-fellow-siam
- Wikipedia (bio, via search snippet). https://en.wikipedia.org/wiki/Luis_Nunes_Vicente

---
> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
