# Luís Nunes Vicente · Evidence ledger

> Date: 2026-09-27. The full evidence behind `../../SKILL.md`. When SKILL.md was tightened on 2026-09-27 (13254 words before, 10494 after, by `wc -w`), every long evidence list, per-paper case list beyond the strongest few, say–do tally, variant or contradiction explanation, long anatomy row and trajectory paragraph was moved here **verbatim**. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count (the evidence / variant / contradiction link counts of `08-deep-reading-synthesis.md` §2.1), at most four variant or correction bullets, and a link to the matching section below. Nothing here is new: each section reproduces the SKILL.md item as it stood before tightening, including its cross-references ("Taste mark 7", "Warning sign 8", "Inner Tensions", "Workflow A step 6" and so on refer to SKILL.md items whose full text is also in this file). The one exception is the last section, which gathers the corrections of the full-text reading from `08-deep-reading-synthesis.md` into one table.

**How to read.** [S019 p. 20] is paper card S019 in `07-paper-cards.md`, at the page of the text version read (mostly preprints or arXiv versions; check the published version before citing a page). In a Signature work section, bare page numbers refer to the card in its heading. Per-card method links (evidence, variant, contradiction) are in the `Methods linked` column of `07-paper-cards.md`; counts, variants, contradictions and promotion decisions are in `08-deep-reading-synthesis.md` (§2 counts, §3 variants and contradictions, §4 promotion candidates, §5 heuristics); proof devices, algorithm-design moves, experiment protocols and writing moves are in `../technique-catalog.md`. Heuristic numbers are the 2026-09-27 numbering (H5 and H9 retired).

**Scope.** Sections exist for every SKILL.md item that was condensed or reworded: the taste lists and quick-check, Methods 1–5, Workflows A–F, the fact-finding step, the task-routing table, the ten heuristics (H1–H12 without the retired H5 and H9), the six signature-work anatomies, the anti-patterns table, the research trajectory, the academic lineage, the inner tensions and the mentor voice. Items not listed (frontmatter, How to Use apart from a pointer line, Activation Rules, Research Integrity Rules, Step 1 and Step 3 of the agentic protocol, Roundtable Card, Honest Boundary, Appendix apart from the link to this file) were not condensed and remain complete in SKILL.md.

## Contents

- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Taste: quick-check](#taste-quick-check)
- [Method 1: Heuristic Inside a Convergent Skeleton](#method-1)
- [Method 2: Count Evaluations Against the Gradient Benchmark](#method-2)
- [Method 3: Relax Deterministic Requirements to Probabilistic Ones](#method-3)
- [Method 4: Generalize the Acceptance Test, Not the Algorithm](#method-4)
- [Method 5: Ship the Solver, Profile It on a Collection](#method-5)
- [Workflow A: Problem intake → algorithm choice](#workflow-a)
- [Workflow B: Globalize a heuristic](#workflow-b)
- [Workflow C: Complexity plan](#workflow-c)
- [Workflow D: Stochastic sampling design](#workflow-d)
- [Workflow E: Multiobjective extension](#workflow-e)
- [Workflow F: Validation and release](#workflow-f)
- [Agentic protocol: Step 2, Vicente-style fact finding](#fact-finding)
- [Research task routing](#task-routing)
- [Research heuristics: numbering note](#research-heuristics)
- [Heuristic 1: wrap a heuristic rather than replace it](#heuristic-1)
- [Heuristic 2: numerics beat what theory says is needed](#heuristic-2)
- [Heuristic 3: accuracy on the quantity the acceptance test uses](#heuristic-3)
- [Heuristic 4: several objectives without derivatives: a nondominated list](#heuristic-4)
- [Heuristic 6: merit function vs extreme barrier](#heuristic-6)
- [Heuristic 7: reuse evaluations already paid for](#heuristic-7)
- [Heuristic 8: formalize an informal notion](#heuristic-8)
- [Heuristic 10: print the edge next to the result](#heuristic-10)
- [Heuristic 11: import a certified result from another field](#heuristic-11)
- [Heuristic 12: known-answer testbeds](#heuristic-12)
- [Signature work: Using sampling and simplex derivatives in pattern search methods (SIAM J. Optim. 18, 2007) …](#signature-s008)
- [Signature work: Direct multisearch for multiobjective optimization (SIAM J. Optim. 21, 2011, DOI 10.1137/10…](#signature-s003)
- [Signature work: Worst case complexity of direct search (EURO J. Comput. Optim. 1, 2013, DOI 10.1007/s13675-…](#signature-s023)
- [Signature work: Direct search based on probabilistic descent (SIAM J. Optim. 25(3), 2015) [S019]](#signature-s019)
- [Signature work: Globally convergent evolution strategies (Math. Program. 152, 2015, DOI 10.1007/s10107-014-…](#signature-s050)
- [Signature work: Stochastic trust-region and direct-search methods: a weak tail bound condition and reduced …](#signature-s067)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory (table, prose and Latest)](#research-trajectory)
- [Academic lineage](#academic-lineage)
- [Inner tensions](#inner-tensions)
- [Mentor voice](#mentor-voice)
- [Corrections from the full texts](#corrections)

<a id="taste-marks"></a>

## Taste: marks of good research

1. **Rigorous and efficient at the same time.** A method must converge from arbitrary starting points *and* stay numerically competitive.
   - Evidence: SID-PSM combines "global convergence properties with the efficiency of the use of quadratic polynomials to enhance the search step and of the use of simplex gradients for guiding the function evaluations of the poll step" ([SID-PSM page](http://www.mat.uc.pt/sid-psm/); [S059 p. 1]); full-low evaluation is "a new class of rigorous methods for derivative-free optimization with the aim of delivering efficient and robust numerical performance" ([arXiv:2107.11908](https://arxiv.org/abs/2107.11908); [S073 p. 1]).
2. **Countable: cost measured in function evaluations against the gradient-method yardstick.**
   - Evidence: O(ε⁻²) like steepest descent ([DOI 10.1007/s13675-012-0003-7](https://doi.org/10.1007/s13675-012-0003-7)); O(ε⁻¹) under convexity ([DOI 10.1007/s10107-014-0847-0](https://doi.org/10.1007/s10107-014-0847-0)); the n² factor optimal among positive-spanning-set choices within the sufficient-decrease bound, not as an oracle lower bound ([DOI 10.1007/s11590-015-0908-1](https://doi.org/10.1007/s11590-015-0908-1); [S041 pp. 1, 5, 8]). Stated: "In DFO it becomes also important to measure the effort in terms of the number of function evaluations" [S038 p. 8].
3. **Minimal modification of what practitioners already use.**
   - Evidence: for ES, "The modifications consist essentially of the reduction of the size of the steps" on failed sufficient decrease [S050 p. 1]; PSwarm puts particle swarm in the optional search step ([DOI 10.1007/s10898-007-9133-5](https://doi.org/10.1007/s10898-007-9133-5)); SID-PSM's add-ons "(i) require no extra function evaluation and (ii) do not interfere with existing requirements for global convergence" [S008 p. 2].
4. **Theory that explains the numerics.**
   - Evidence: probabilistic descent started from numerics in which random polling did better [S019 pp. 1–2]; the 2019 sequel reports gains "as it is suggested by the respective worst-case complexity bounds" [S045 p. 1]; "Such an analysis of worst case complexity contributes to a better understanding of the numerical performance of this class of derivative-free optimizations methods." [S023 p. 2].
5. **A usable artefact.**
   - Evidence: SID-PSM (MATLAB, LGPL [S059 p. 1]; v1.3, Dec 2014, per the software page); DMS with posted errata and a public AMPL collection [S003 p. 15]; PSwarm with a public 122-problem collection [S005 p. 14]; public code in 8 of 22 Lehigh experimental papers (2021–2026), e.g. [S016 p. 5; S042 p. 22; S088 p. 14]; generator code as its own TOMS paper in 1994 [D001 pp. 1–4].
6. **Anchored in an application.**
   - Evidence: 3D full-waveform inversion [S068]; fairness in credit scoring and criminal justice [S016]; molecular geometry [S106]; astrophysics [S075]. The Lagrange Prize citation lists "aerospace engineering, urban transport systems, adaptive meshing for partial differential equations, and groundwater remediation".
7. **The boundary is part of the result** (H10): where it loses, where the proof stops, where the code departs from the theory.
   - Evidence: a conjecture printed with the inequality that fails [S014 pp. 20–21]; "In this sense, the experiment in Subsection 2.2 is biased in favor of direct search based on probabilistic descent." [S019 p. 20], followed by a rerun [pp. 20–21]; a negative-result paper about neural surrogates in his own solver [S079 pp. 3, 23].

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

1. **Heuristic with no convergence safeguard** (ES or PSO tuned by trial). The ES and PSwarm papers add the guarantee [S050 pp. 4–6; S005 p. 6].
2. **Aggregating objectives before the front is known.** DMS "does not aggregate any of the objective functions" [S003 p. 1]; the fairness work builds the complete front [S016 pp. 2, 4]. Scope: the derivative-free line; the gradient-based ML papers sweep weights or step frequencies to trace a front [S093 pp. 3, 15–17; S111 p. 4].
3. **Fixed worst-case sample sizes per iteration under noise.** "It is finally important to highlight that all the methods mentioned above are fixed-sampling schemes, which always pay the worst-case cost." [S102 p. 3].
4. **Expensive deterministic requirements whose necessity nobody has measured** (positive spanning sets, fully linear models every iteration) [S014 p. 1; S019 p. 5].
5. **Numerical claims without a problem collection and profiles.** DMS used 100 AMPL problems with purity and spread profiles [S003 pp. 15–20]. Stated in 1993: "Care must be exercised in the testing and benchmarking of algorithms and in the interpretation and dissemination of the corresponding results" [S053 p. 14].
6. **Theorems at the edge of regularity with no counterexample search.** *A lesson from the 2024 counterexample to the 2012 discontinuous-functions theorem, i.e. from external critique of Vicente's own work, not a rule Vicente stated.* His papers do print hypothesis-breaking examples (H10).
7. **A motivating experiment that favours the new method and is never rerun.** See Taste mark 7 [S019 pp. 20–21]; tune the baseline first [S008 p. 14].
8. **Code that silently departs from the analysed algorithm.** The papers label each departure and its reason [S005 p. 15; S050 p. 11; S067 p. 20].

<a id="taste-quick-check"></a>

## Taste: quick-check

- [ ] Does the method keep an existing, efficient heuristic and add a guarantee, rather than replacing it?
- [ ] Is there an acceptance test (sufficient decrease or its generalization) that makes progress countable?
- [ ] Can you state the worst-case bound in *function evaluations* with its n-dependence, next to the gradient-method bound?
- [ ] Is any deterministic requirement more expensive than it needs to be, and could a probabilistic version do the job?
- [ ] For multiple objectives: do you avoid a priori aggregation, and do you have class-appropriate metrics?
- [ ] Is there a problem collection, a strongest-available baseline at its best settings, and profiles?
- [ ] Will you release the code, and is there one real application?
- [ ] Have you searched for counterexamples to your boundary-case theorem, and written down where the method loses, where the proof stops and where the code departs from the analysed algorithm?

<a id="method-1"></a>

## Method 1: Heuristic Inside a Convergent Skeleton

**One line**: Keep whatever generates good trial points (models, swarms, ES offspring, finite-difference quasi-Newton, user-supplied moves) in a free "search" role, and let convergence come from a poll / step-size mechanism with an acceptance test the heuristic cannot break: an integer-lattice mesh with simple decrease in the 2001–2012 papers, sufficient decrease from 2013 on [S008 pp. 3–4; S005 pp. 10–11; S023 p. 4].

**Evidence**:
- Stated: "It is the poll step that guarantees the global convergence of the pattern search method." [S005 p. 6]; the question is "how to change Algorithm 2.1, in a minimal way, so that it enjoys some form of convergence properties, while preserving as much as possible the original design and goals." [S050 p. 4]. Practice: the papers cited in the steps, from user-proposed points in the search step (2001) [S106 pp. 1–3] to FD-BFGS steps "essentially considered as search steps" (2023) [S073 p. 10].
- Say–do consistency: ✅ stated + practiced (one disclosed exception: a variant shipped as "not grounded on theoretical principles" [S042 p. 5]).
- Variants that change a step: ⚠ **glue, dated (step 3)**: integer-lattice mesh + simple decrease in 2001–2012 (SID-PSM, PSwarm, the DMS numerics) [S008 pp. 3–4; S059 pp. 6–7; S003 p. 20]; one proof for both in 2011–2012 [S003 pp. 28–31; S024 p. 6]; sufficient decrease from 2013 [S023 p. 4; S050 pp. 4–6], because it frees point generation from the lattice and "in practice, sufficient decrease can be imposed as not to differ much from simple decrease." [S049 p. 2]. **Switch instead of reset (step 4)**: accept the fast step only while β ≥ γρ(α), else switch to direct search [S073 pp. 5–6; S104 pp. 4–5].

**Steps**:
1. Name the heuristic and its own step mechanism (ES step size σ, swarm velocity, model minimizer, BFGS step). Do not change how it proposes points. Rewrite the base method with its proof-free slots named ([search], [order], [mesh]) [S008 pp. 3–4].
2. Put it in the search step (or make it the "Full-Eval" iteration type): one heuristic iteration per search step, poll centred at the heuristic's best point [S005 pp. 8–10]. Define a poll set D (positive spanning, or random per Method 3) and a step size α.
3. Accept a trial point only if f(trial) < f(x) − ρ(α) with a forcing function ρ (e.g., ρ(α)=cα²). If search fails, poll; if poll fails, shrink α. (Mesh variant: project the heuristic's points onto the mesh and accept on simple decrease [S005 pp. 10–11].)
4. Let the heuristic keep its own step when it is larger: reset σ_{k+1} = max{σ_k, σ^ES_k} on success [S050 pp. 6, 11], or switch.
5. Prove lim inf α_k = 0 and stationarity along refining directions (if the test compares values across iterations, chain back to the last success [S050 pp. 9–10]), then move to Method 2 for rates.
6. Compare the raw heuristic with the globalized version, and each component as its own solver, on one collection (Method 5) [S005 pp. 26–27]; if exploration was the selling point, add a multimodal suite with medians over random starts [S050 pp. 16–18]. If efficiency drops, revisit Step 4.

**Applies to stage**: idea generation, algorithm design.

**Different from standard practice**: Heuristic communities tune without guarantees; theory communities design provable algorithms from scratch. Vicente's move is a *thin wrapper* that leaves the heuristic intact. The search/poll wrapper itself is shared with the MADS school (Audet lens, Method 1). What is distinctive: the heuristic keeps its own step mechanism (the reset or the β ≥ γρ(α) switch), and from 2013 sufficient decrease removes the lattice projection a mesh method would need (for ES, discrete sampling) [S050 p. 2; S049 p. 2].

**Limitations**: Guarantees are stationarity, not global optimality; pure CMA-ES was slightly better at global search [S050 pp. 17–18]. Failed polls cost up to |D| evaluations. Sufficient decrease is less natural than a mesh for granular or discrete variables, where the MADS line is stronger. The guarantee covers the analysed algorithm, not necessarily the shipped code (H10).

<a id="method-2"></a>

## Method 2: Count Evaluations Against the Gradient Benchmark

**One line**: For every derivative-free variant, give a worst-case bound on iterations *and* function evaluations (with n-dependence), set it next to the gradient method's bound for the same class, then ask whether the order is optimal among the designs the proof template allows.

**Evidence**:
- Stated: direct search based on imposing sufficient decrease "shares the worst case complexity bound of steepest descent" [S023 p. 1]; "κ can be interpreted as the price to pay for the absence of gradient information." [S041 p. 4]; "recovering classical convergence rates of single-objective methods" [S111 p. 1]. Practice: the papers cited in the steps, plus convex O(ε⁻¹) [S046], O(mnε⁻²) next to O(n²ε⁻²) [S019 p. 16] and probabilistic trust-region rates [S027 pp. 5, 8–11] (the 2014 paper proves almost-sure convergence only [S014 pp. 8–13]).
- Say–do consistency: ✅ stated + practiced for the 2013–2019 DFO complexity line. ⚠ Several 2023–2026 papers count iterations and leave total sample or oracle work open [S073 pp. 8–9; S102 p. 16; S110 p. 14; S111 pp. 6–11].
- Variant that changes a step (step 4): the later papers' yardstick is the nearest classical method (SCGD, monotone direct search, SGD/BCD) [S107 p. 16; S110 p. 13; S111 pp. 7–9].

**Steps**:
1. Fix the function class and the stationarity measure (‖∇f‖, or the step size as a surrogate); state it as Model / Oracle / ε-solution [S023 p. 2].
2. With sufficient decrease, each success decreases f by at least ρ(α); bound unsuccessful iterations by counting α-reductions; add the two [S023 pp. 5–6].
3. Convert iterations to evaluations as (poll size) × cm(D)⁻², so each factor of n has a named source [S023 pp. 7–8; S041 p. 4].
4. Put the result next to the gradient method's bound. If it is worse, name the price (smoothing: "roughly one order of magnitude worse" [S034 p. 1]); say so if a competitor's bound is better [S023 p. 9].
5. Ask the lower-bound question in the form the proof allows: is the n-order optimal among poll-set designs in this template (minimize |D|/cm(D)² [S041 pp. 2, 5, 8])? Is the ε-order tight (reduce to steepest descent in dimension 1 [S023 p. 8])? Do not call either an oracle lower bound.
6. Only then check whether the bound predicts the numerical ranking (Method 5), and report it when it does not [S032 p. 22].

**Applies to stage**: theory, result judgment.

**Different from standard practice**: Many DFO papers stop at lim-inf convergence or at numerics. Vicente treats *evaluations* as the unit of cost and the gradient method as the yardstick; mesh-based analyses without sufficient decrease do not give such counts without extra conditions [S023 p. 9].

**Limitations**: Worst-case bounds are pessimistic (Inner Tensions). The n² factor is optimal only within the positive-spanning-set template [S041 pp. 1, 5, 8]; random directions give O(mnε⁻²) [S019 p. 16]. Requires sufficient decrease. Era effect: counting bounds became a field-wide priority in the 2010s.

<a id="method-3"></a>

## Method 3: Relax Deterministic Requirements to Probabilistic Ones

**One line**: When a deterministic requirement is expensive (positive spanning sets, models that are fully linear at every iteration, accurate function values), require it only with probability p conditioned on the past. Prove almost-sure convergence and high-probability complexity, and take the savings as fewer evaluations or samples.

**Evidence**:
- Stated: "One knows however from the unconstrained case that randomly generating the polling directions leads to better complexity bounds as well as to gains in numerical efficiency" [S045 p. 1, 2019]; the gain is in evaluations, since the 2015 abstract calls its rate "matching" the deterministic one [S019 p. 1] and the bound is O(mnε⁻²) against O(n²ε⁻²) [S019 p. 16]. A standard framework works "as long as “good” models are more likely than “bad” models" [S014 p. 1]. Practice: probabilistic models [S014 pp. 7, 10–13], probabilistic descent [S019 pp. 7–9], trust-region rates [S027 pp. 5, 8–11], the tail bound [S067 pp. 5–8] and the sequential test [S102 pp. 6, 11], each cited in the steps.
- Say–do consistency: ✅ stated + practiced for the DFO line; not as a contrast with stochastic approximation in the bilevel/trilevel SG papers [S042 pp. 13–14, 18; S091 pp. 5–6].
- Variants that change a step: **step 4**, a bound on the *expected* iteration count via renewal–reward [S102 p. 16; S110 p. 13]; **step 5** (disclosed contradiction), the tail-bound paper runs a tuned θ = 0.5 far below its proven threshold (θ > 4 for q = 2, about 9 for q = 1.5) because both algorithms "show bad performance for θ greater than 1", and states the gap with a conjecture [S067 p. 20].

**Steps**:
1. List each deterministic requirement and its cost per iteration (e.g., 2n poll directions; interpolation points; N samples per estimate).
2. Find the one instance of the requirement the proof actually uses (cm(D, −g) instead of the cosine measure over all vectors) [S019 p. 5; S045 p. 8], and replace it with "holds with probability ≥ p given the past". Targets: a descent property of the directions, model accuracy, a tail bound on the *estimated decrease* [S067 pp. 3, 5].
3. Derive the threshold on p from the step-size factors and turn it into a rule: m > log₂[1 − ln θ / ln γ] random directions (m = 2 for γ = 2, θ = 1/2) [S019 p. 20], the sample size [S067 p. 7], or sequential-test boundaries ±σ²/(2eC) [S102 pp. 9, 18].
4. Prove almost-sure convergence (submartingale on log α_k) plus complexity with overwhelming probability (realization-wise count, then conditional Chernoff [S019 pp. 11–13]); or bound E[T_ε] via renewal–reward [S102 pp. 16, 22–25].
5. **Meet the thresholds that are cheap to meet; label the ones you cannot.** Direction-count and step-factor thresholds cost little (m = 2 for γ = 2, θ = 1/2; one direction with 3 log γ + 11 log θ > 0, e.g. θ = 0.95, γ = 1.3 [S102 pp. 16–18]): never go below them to "save more" (Huang & Zhang, arXiv:2606.01320, abstract read, report non-convergence below the threshold). Some thresholds are not practical: run the tuned value, as S067 does with θ = 0.5, label the run as outside the theorem, and optionally add a control with θ above the threshold.
6. Run randomized against deterministic on the same collection; report where randomization is clearly better and where it is not [S019 pp. 20–21; S045 p. 15].

**Applies to stage**: algorithm design, theory, experiments.

**Different from standard practice**: The stochastic-approximation tradition assumes unbiased oracles and diminishing step sizes. In the DFO line, Vicente keeps adaptive-step DFO machinery and asks only for probabilistic accuracy of *components*: directions, models, decrease estimates [S014; S019; S067; S102].

**Limitations**: Guarantees are almost-sure, high-probability or in expectation only. Threshold and noise-moment assumptions must hold, and constants must be supplied (a bound on the noise constant ε_q [S067 p. 6]; the noise variance [S102 pp. 18–19]). The sequential test's sample-size result is approximate and Gaussian [S102 pp. 9–10]. The direction-count threshold caps the savings.

<a id="method-4"></a>

## Method 4: Generalize the Acceptance Test, Not the Algorithm

**One line**: To reach a new problem class (multiple objectives, constraints, noise, nonsmoothness), keep the search/poll/step-size skeleton, redefine only what counts as "success", and re-derive the theory.

**Evidence**:
- Stated: DMS "does not aggregate any of the objective functions" and is "inspired by the search/poll paradigm of direct-search methods of directional type" [S003 p. 1]; stochastic multi-gradient is "seen as an extension of the classical stochastic gradient method" [S017 p. 1]; "The merit function and the corresponding penalty parameter are only used in the evaluation of an already computed step, to decide whether it will be accepted or not." [S049 p. 3]. Practice: the list iterate [S003 pp. 4–5, 30–31], merit-function success [S049 pp. 3–6], componentwise sufficient decrease [S015 pp. 3–4], one acceptance change through direct search and trust region [S067 pp. 10–18], non-monotone max-M acceptance [S110 pp. 4, 6, 10].
- Say–do consistency: ✅ stated + practiced; no card contradicts it.
- Variants that change a step: **step 2**, in about two thirds of the linked cards the changed object is not the acceptance test but the stationarity measure [S024 pp. 4, 6, 11], the model class [S006 pp. 7–9], the direction map [S017 p. 8] or the objective [S034 p. 7]; run the steps on that object. **Step 4** uses two standard sub-steps, not distinctive (08 §4.2): a bridge inequality into the classical theorem [S037 pp. 6–7; S046 pp. 7–9] and a collapse check to the old theorem [S003 p. 14; S013 pp. 1–2].

**Steps**:
1. Write the base algorithm as four parts: search, poll, acceptance test, step update.
2. Identify the smallest object that must change. Multiple objectives: the incumbent becomes a nondominated list. Constraints: f becomes a merit function for relaxable constraints plus an extreme barrier for unrelaxable ones. Nonsmooth f: run direct search on the smoothed f_μ and reduce μ when α is small [S034 p. 7]. Noise: f(x) becomes an estimate controlled by a tail bound. Weaker regularity: the stationarity measure changes.
3. Keep the step-size logic unchanged. Define success in the new sense, and write down what the proof needs from it (for a list: which elements must be kept [S003 pp. 4–7]).
4. Re-derive the limit statement for the new class, with the extra complexity factor.
5. State the price in the abstract: "roughly one order of magnitude worse" [S034 p. 1]; "it is shown that this direction is biased even when all individual gradient estimators are unbiased" [S017 p. 1].
6. Define metrics native to the new class (for Pareto fronts: purity, spread Γ and Δ) and hand off to Method 5.

**Applies to stage**: problem framing, algorithm design.

**Different from standard practice**: Common multiobjective practice scalarizes with weights and reuses single-objective solvers; common constrained DFO uses fixed-parameter penalties. Vicente reuses the *skeleton*, so most of the proof carries over, and changes only the notion of success (or the one object that must change).

**Limitations**: The method inherits the skeleton's dimension limits, and dominance lists can grow large. The Pareto-sensitivity (knee) work goes the other way: it needs scalarization and first- and second-order derivatives [S096 p. 1]. A 2024 paper (Audet, Bouchet & Bourdin; not read here) gives a counterexample to a 2012 result; which step it targets is unknown. The 2012 paper states its extra assumptions explicitly [S024 pp. 11, 15].

<a id="method-5"></a>

## Method 5: Ship the Solver, Profile It on a Collection

**One line**: A method is finished when it exists as a freely available solver and has been compared on a stated problem collection with performance profiles, using metrics suited to the problem class.

**Evidence**:
- Stated: "Theory and algorithms, software development, and industrial applications" (Lehigh news 2018); "Care must be exercised in the testing and benchmarking of algorithms and in the interpretation and dissemination of the corresponding results" [S053 p. 14]; "A fair comparison among different solvers should be based on the number of function evaluations, instead of based on the number of iterations or on the CPU time." [S005 p. 16]. Practice: already complete in 2007 (solver, public 122-problem collection, profiles, hybrid-vs-components ablation) [S005 pp. 14–18, 26–27]; also [S003 pp. 15–20; S050 pp. 12–18; S088 pp. 14–24].
- Say–do consistency: ✅ stated + practiced, genre-dependent: the full protocol is in algorithm papers; theory-first papers have none [S023; S041]; application papers use the group's solver without a benchmark [S036 pp. 9–11]; several papers do not mention a code release [S008; S019; S050; S067].
- Variants that change a step: refinements of steps 1 and 4, standard practice rather than distinctive (08 §4.2): one control that removes the credited mechanism [S074 pp. 20–21]; tune the baseline first [S008 p. 14]; give rivals the oracle constants their theory needs [S046 pp. 21–22]; report where the strongest baseline wins, by class and budget [S050 pp. 15–18; S012 p. 10].

**Steps**:
1. Implement with the theoretical safeguards switchable, so that *heuristic on/off* and *safeguard on/off* become the ablation [S059 pp. 20–22].
2. Assemble or reuse a problem collection and make it available (DMS offered its AMPL set [S003 p. 15]; PSwarm its 122 problems [S005 p. 14]). If no benchmark with known answers exists, generate one (H12).
3. Choose metrics native to the class: evaluations to reach a given accuracy; purity (pairwise only) and spread Γ/Δ for Pareto fronts, spread kept out of data profiles [S003 pp. 17–20]; best/average/worst over runs for stochastic solvers [S005 p. 17]; profiles on the true f while the solver sees noise [S067 p. 19]. Plot performance and data profiles.
4. Compare against the strongest accessible baseline *and* against the unsafeguarded heuristic, with each component alone [S005 pp. 26–27; S073 pp. 17–22].
5. Release the code (LGPL or GitHub) and post errata when you find mistakes.
6. Add one real application (geophysics, aerospace, fairness).

**Applies to stage**: experiments, publication, post-publication.

**Different from standard practice**: Many theory papers ship no code, and many applied papers use no collection or profiles. Vicente's algorithm papers typically bundle a theory paper, a solver and profiles.

**Limitations**: Academic collections may not reflect expensive real black boxes with budgets of tens of evaluations. The earlier solvers are MATLAB- or C/AMPL-era [S059 p. 1; S005 p. 14]. The code, the errata pages and the GitHub repositories were **not inspected** in this research.

<a id="workflow-a"></a>

## Workflow A: Problem intake → algorithm choice

**Input**: f (smooth? noisy? discontinuous?), n, the evaluation budget, constraints (which may be violated during the run?), the number of objectives, and any heuristic already in use.

**Steps**:
1. Classify regularity and noise (→ Method 4 decides which acceptance test is needed); route by problem feature as the 2017 survey does [S038 p. 2]. If outputs change only on an unknown grid ("Many optimization problems are only apparently continuous." [S083 p. 1]), treat the problem as implicitly discrete [S083 pp. 4–5].
2. Budget check: evaluations per iteration (poll size ~ n, or m random directions) against the budget (→ Method 2). If n is large relative to the budget, consider probabilistic descent with m = 2 random directions for γ = 2, θ = 1/2 [S019 p. 20] (→ Method 3).
3. Split constraints into relaxable (merit function + restoration) and unrelaxable (extreme barrier) [S049 pp. 4–6]; tangent-cone generators for linear constraints [S045 p. 7] (→ Method 4).
4. Several objectives: keep a nondominated list (→ Method 4); compute knees later if one compromise is needed.
5. A heuristic in use: keep it in the search step (→ Method 1). If finite differences are accurate, consider a Full-Eval (FD-BFGS) / Low-Eval (direct search) switch [S073 pp. 5–6, 17–22].
6. Name candidate verified solvers (SID-PSM, DMS, PSwarm, FLE, MATLAB `patternsearch`) and verify availability with a tool. For stochastic f, no public code is stated for the tail-bound or sequential-test methods [S067; S102]: implement S067's Algorithm 1 (one random unit direction, two averaged estimates, accept if f_k − f_k^g ≥ θδ_k^q) [S067 p. 10] and benchmark against StoMADS, the baseline used there [S067 pp. 21–22].

**🔴 Checkpoint**: If the budget is below roughly one full poll per iteration for many iterations (e.g., tens of evaluations in moderate n), the direct-search lens is weak. Hand over to a model-based lens (Powell / Conn–Scheinberg style) and say so explicitly.

**Output**: a verdict (algorithm family + why), a first configuration (forcing function, poll type, constraint handling), a benchmark plan, and the main risk.

<a id="workflow-b"></a>

## Workflow B: Globalize a heuristic

**Input**: pseudo-code of the heuristic, how it adapts its own step, typical results.

**Steps**:
1. Isolate the heuristic's step generator and internal step size (→ Method 1); mark the diff against the base method in the algorithm box [S008 p. 7; S050 pp. 3–6].
2. Wrap it: search = heuristic; poll = positive spanning or random directions; accept on sufficient decrease; shrink α on failure. For a population method, put the sufficient decrease on the recombined mean (one extra evaluation; the best variant) [S050 pp. 4, 13].
3. Add the reset rule σ_{k+1} = max{σ_k, σ^ES_k} [S050 pp. 6, 11] or a monitored switch [S073 pp. 5–6].
4. Prove lim inf α_k = 0 and stationarity; justify density of directions by spherical-cap probabilities if needed [S050 p. 9]; then apply Workflow C.
5. Ablation: raw vs wrapped vs wrapped-without-reset vs each component alone, on one collection (→ Method 1 step 6; Method 5 step 4).
6. Label every place the code will depart from the analysed algorithm, with the reason (H10).

**🔴 Checkpoint**: If the wrapped version loses more than modest efficiency on smooth problems, the reset rule or forcing function is too conservative; retune before writing theory. If the heuristic has no identifiable step size, stop: Method 1 does not apply cleanly. If it is a learned surrogate replacing an already accurate component (e.g. forward differences), test that first [S079 pp. 20–23].

**Output**: a modified algorithm box, a convergence-proof outline, and an ablation table template.

<a id="workflow-c"></a>

## Workflow C: Complexity plan

**Input**: the algorithm, the function class, and the measure of stationarity.

**Steps**:
1. Confirm there is a sufficient-decrease test; if not, decide whether to add one (→ Method 2). State the class as Model / Oracle / ε-solution [S023 p. 2].
2. Bound successes with ρ(α) and a step-size floor, failures by the log of the step-size product → iteration bound [S023 pp. 5–6]; choose the forcing exponent by minimizing the ε-power [S023 p. 7].
3. Convert to evaluations (poll size × cm(D)⁻²) → n-dependence [S023 pp. 7–8].
4. Compare with the gradient method in the same class; for convex classes, mirror its proof step for step [S046 pp. 3–4, 9, 13–14].
5. If randomness is involved, add the probabilistic layer (→ Method 3, step 4).
6. Ask whether the order is optimal within the proof template and whether the ε-order is tight (→ Method 2, step 5).
7. Where the proof does not extend, publish the failing inequality or case as a conjecture or remark (H10).

**Stuck on → device** (details in `references/technique-catalog.md` §1):

| Stuck on | Device | Cards |
|---|---|---|
| Success probability below 1/2 (e.g. one random direction), so the submartingale argument fails | Renewal–reward: require p log γ + (1 − p) log θ > 0 and bound E[T_ε] | [S102 pp. 16, 22–25; S110 p. 13] |
| Two sources of randomness (random direction, noisy accept/reject) | Half-step σ-algebra F_{k+1/2}: contains the direction, not the decision | [S102 pp. 11–14; S110 pp. 15–16] |
| Noisy estimates cause false acceptances | Potential Φ_k = f(X_k) − f* + ηΔ_k^q with a capped expected loss per false success | [S067 pp. 11–12; S102 pp. 11–13] |
| The acceptance test compares quantities from different iterations | Chain back to the last success | [S050 pp. 9–10] |
| The failing index (objective, piece, mode) changes with k | Pigeonhole a subsequence on which it is constant | [S003 p. 13] |
| Need to show the ε-order is tight | Reduce the method to steepest descent in dimension 1 | [S023 p. 8] |
| A new object (list, merit function, estimate) breaks the classical theorem | Bridge inequality into the classical proof, then a collapse check | [S037 pp. 6–7; S046 pp. 7–9; S003 p. 14] |
| Mesh and sufficient-decrease variants seem to need two proofs | One box with ρ̄ ∈ {0, forcing function} on the displacement | [S024 p. 6; S003 pp. 28–31] |
| You call your condition "weaker" | Prove each rival condition implies yours | [S067 p. 9; S102 p. 7] |

**🔴 Checkpoint**: If the bound needs assumptions the algorithm cannot check (e.g., the probability threshold is unmet by the actual direction count and step factors), stop and fix the algorithm, not the proof. Put a hypothesis needed only by one pathological branch into that branch's theorem [S049 p. 12]. Before claiming results for weak regularity (discontinuous f), search for counterexamples (H10; see the labelled lesson under Inner Tensions).

**Output**: a lemma chain (3–5 lemmas), the final bound in ε and n, a comparison line with the gradient method, and open questions.

<a id="workflow-d"></a>

## Workflow D: Stochastic sampling design

**Input**: the noise model (moments, heavy tails?), the cost per sample, whether seeds can be fixed, and the current sample-size rule.

**Steps**:
1. Put the accuracy requirement on the *estimated decrease*, not on each function value (→ Method 3) [S067 pp. 3, 5].
2. Choose the sufficient-decrease power q: O(Δ^{−2q}) i.i.d. samples per iteration for q ∈ (1, 2] under a finite r-th moment, r = q/(q − 1) [S067 pp. 6–7]; it needs a known bound on the noise constant ε_q and θ above a threshold [S067 pp. 6, 11]. With common random numbers, O(Δ^{2−2q}) [S067 p. 8].
3. Optionally replace fixed sampling with a sequential test on the sign of a mean, with P(reject | acceptable) ≤ 1/2 and P(accept | unacceptable) ≤ C/µ; in the Gaussian case, boundaries ±σ²/(2eC) with a known variance [S102 pp. 5–10, 18–19]. With one random direction, pick step factors with 3 log γ + 11 log θ > 0 [S102 pp. 16–18].
4. Keep the direct-search or trust-region step logic unchanged; the same acceptance change carries across both [S067 pp. 15–18] (→ Method 4).
5. Benchmark total samples to reach a given accuracy against the fixed-sample baseline, with profiles on the true f and each repeated run counted as a problem [S067 p. 19; S102 p. 17]. The papers give per-iteration counts or iteration bounds; the total is your job [S102 p. 3].

**Defaults and preconditions** (from the preprints read; check the published versions):
- *q trade-off*: lower q means fewer samples per iteration but a higher required moment (q = 1.5 needs a finite third moment) and a higher iteration complexity, O(ε^{−q/(q−1)}) in the smooth case [S067 pp. 7, 20; S102 p. 3].
- *Starting values in the paper* (grid-tuned on its own test set): q = 1.5, p_k = ⌈0.01 δ_k^{−3}⌉, θ = 0.5, τ = 0.001, τ̄ = 1.001, δ₀ = 2; q = 1.5 beat q = 2 and StoMADS [S067 pp. 20–22]. θ = 0.5 is below the proven threshold (Method 3 step 5).
- *Common random numbers* need per-seed output Lipschitz in x, uniformly in the seed, or Gaussian-process noise [S067 p. 8, Props 2.6–2.7]; discrete-event simulators often violate this, so test it first.
- *Known variance*: the sequential test assumes the variance or an upper bound is known; estimation is left to the implementation (pointers to Berahas–Byrd–Nocedal and Moré–Wild) [S102 p. 19].
- *When the sequential test helps*: the worst case stays of order δ⁻⁴; the expected sample size is O(δ^{−2−r}) when the potential decrease is Θ(δ^r), r ∈ (0, 2] [S102 pp. 4, 10]. The evidence is a comparison with its own fixed-sample counterpart on 91 CUTEst instances with Gaussian noise [S102 pp. 17–18].
- *Code*: none stated (Workflow A step 6).
- *Constraints and crashes*: S067, S102 and S110 treat unconstrained problems; the extreme-barrier evidence is deterministic [S049; S057; S005]. No paper read covers stochastic f with unrelaxable or hidden constraints.

**🔴 Checkpoint**: If only a finite r-th moment with 1 < r < 2 holds (infinite variance), S067 still covers it with q = r/(r − 1) > 2, at a higher per-iteration cost, O(Δ^{−q²}) as the exponent reads in the extracted preprint (Thm 2.4 [S067 p. 7]; check the published version). If no moment above 1 can be assumed, or samples are not i.i.d., none of these papers covers the case: say so. Fixed O(Δ⁻⁴) sampling is no fallback there, since it assumes finite variance [S067 p. 4; S102 p. 2]. If ε_q or the variance bound cannot be supplied, the guarantees do not apply as stated.

**Output**: a sampling rule, the assumptions list, and an experiment design comparing total sample counts.

<a id="workflow-e"></a>

## Workflow E: Multiobjective extension

**Input**: the objectives, whether the decision maker wants the full front or a representative point, and derivative availability.

**Steps**:
1. Without derivatives: a DMS-style method, with a nondominated list, success defined by dominance, and the same poll/step logic (→ Method 4). Cheap levers: poll centre with the largest spread gap Γ; a cache [S003 pp. 4–7, 25].
2. With stochastic gradients (ML): stochastic multi-gradient or block/function alternation. Account for the multi-gradient bias (Method 4 step 5 [S017 p. 1]). Alternating schemes encode weights as step counts; state the implied weighted function [S093 pp. 3, 15–17; S111 p. 4].
3. If one point is needed: compute knee solutions after the front via Pareto sensitivity, which needs scalarization and 1st/2nd derivatives [S096 pp. 1, 4–5].
4. Evaluate with purity (pairwise only) and spread Γ/Δ, spread kept out of data profiles [S003 pp. 17–20], plus hypervolume if the literature uses it; report cost per nondominated point [S016 p. 6] (→ Method 5).
5. If a heuristic outer loop generates the front, filter dominated points and report how many were removed: "We found that 70-80% of the final points produced by this process were actually dominated ones, and we removed them for the purpose of analyzing results." [S016 p. 5].

**🔴 Checkpoint**: If the user plans to fix the weights a priori "to keep it simple", challenge this: fixed weights miss nonconvex parts of the front [S003 p. 2]. Without derivatives, Pareto-sensitivity knees are not available as published. Say what the theory covers: for DMS, only a limit point in a stationary form of the front [S003 p. 26].

**Output**: a formulation choice, an algorithm, metrics, and a plan for presenting the front.

<a id="workflow-f"></a>

## Workflow F: Validation and release

**Input**: the method, the implementation status, and the candidate test problems.

**Steps**:
1. Freeze a collection and state it (→ Method 5); if no benchmark with known answers exists, generate one with planted solutions (H12).
2. Pick metrics suited to the class and use performance and data profiles [S050 pp. 12–13].
3. Baselines: the strongest available solver at its best settings, the unsafeguarded heuristic and each component alone [S008 p. 14; S005 pp. 26–27]; one mechanism-isolating control [S074 pp. 20–21].
4. Boundary audit (H10): list where you lose, by class and budget; rerun any motivating experiment whose settings favoured you [S019 pp. 20–21]; label every departure of the code from the analysed algorithm [S005 p. 15; S050 p. 11]; write down where the proof stops.
5. Release the code with the paper and prepare an errata channel.
6. Add one real application.

**🔴 Checkpoint**: If the method wins only on problems you designed, or loses to its own unsafeguarded heuristic across the collection, do not submit yet; revisit Method 1, step 4. If the gain survives only with settings the theory forced on the baselines, report the rerun, not the first run.

**Output**: a benchmark protocol, a figure list, a boundary paragraph, and a release checklist.

<a id="fact-finding"></a>

## Agentic protocol: Step 2, Vicente-style fact finding

**⚠️ Use tools (WebSearch, Google Scholar, arXiv, Optimization Online, publisher sites). Do not rely on memory.**

- **Does a globally convergent version already exist?** Search "globally convergent" + the heuristic's name, and "direct search" + heuristic. Check whether the step-size safeguard is sufficient decrease or a mesh (his own solvers used a mesh with simple decrease in 2001–2012 and sufficient decrease from 2013 [S008 pp. 3–4; S023 p. 4]).
- **What complexity is known for this class?** Search "worst case complexity" + direct search / trust region + the class. Record the order in ε and in n, the unit (iterations, evaluations or samples), and the gradient-method benchmark for the same class.
- **Is there a probabilistic variant?** Search "probabilistic descent", "probabilistic models", "tail bound", "sequential test" + the method. Record the threshold (probability, step-size factors, number of directions) and any non-convergence results (e.g., arXiv:2606.01320).
- **Which solvers can be benchmarked?** Check availability and licence of SID-PSM (MATLAB, LGPL [S059 p. 1]), DMS, PSwarm (C with an AMPL interface in 2007 [S005 p. 14]), FLE (MATLAB, GitHub [S088 p. 14]), MATLAB `patternsearch`, and the user's current solver. The tail-bound and sequential-test papers state no public code [S067; S102]. For multiobjective problems, check the metrics used in the literature (purity, spread Γ/Δ, hypervolume).
- **Known errata or counterexamples?** Search the key paper title + "counterexample" or "erratum" before relying on a theorem at the edge of the theory (discontinuous functions, weak regularity).

Keep the search results internal. The user sees the fact-based judgment and the next steps.

<a id="task-routing"></a>

## Research task routing

| User says | Workflow | Main methods |
|---|---|---|
| "Here's my black-box problem, what should I use?" | Workflow A: Problem intake → algorithm choice | Method 1, Method 3, Method 4 + Taste quick-check |
| "My heuristic (ES / PSO / surrogate) works but has no theory" | Workflow B: Globalize a heuristic | Method 1, Method 2 |
| "How do I prove a rate / complexity for my DFO method?" / "My proof is stuck" | Workflow C: Complexity plan (with the stuck-on table) | Method 2, Method 3 |
| "My function values are noisy / stochastic; how many samples?" | Workflow D: Stochastic sampling design | Method 3, Method 4 |
| "I have several objectives / need the Pareto front / a knee" | Workflow E: Multiobjective extension | Method 4, Method 5 |
| "Is my numerical comparison convincing? Should I release code?" | Workflow F: Validation and release | Method 5 |
| "Where does my method lose? How do I write the limitations?" | Workflow F, step 4 (boundary audit) | H10, Method 5 |
| "Is this topic worth doing?" | Workflow A (with Taste quick-check) | Research Taste |
| Rebuttals, grant strategy, lab management | Say: "Vicente has no distillable public method at this stage." Give generic advice labelled **"not Vicente-style"**. For paper *structure*, the writing moves in `references/technique-catalog.md` §4 are evidenced. | — |

<a id="research-heuristics"></a>

## Research heuristics: numbering note

H5 and H9 are retired numbers (smoothing now sits in Method 4 step 2; "is the n-order optimal?" in Method 2 step 5), so that card links in `07-paper-cards.md` keep their meaning.

<a id="heuristic-1"></a>

## Heuristic 1: wrap a heuristic rather than replace it

- **H1 · If a heuristic works but lacks guarantees, then wrap it rather than replace it.** Case: evolution strategies made globally convergent by step reduction on failed sufficient decrease (Diouane, Gratton & Vicente 2015) [S050 pp. 4–6, 11]; particle swarm in the search step (Vaz & Vicente 2007) [S005 pp. 8–10].

<a id="heuristic-2"></a>

## Heuristic 2: numerics beat what theory says is needed

- **H2 · If numerics beat what theory says is needed, then the theory's requirement is too strict: find the weaker property.** Case: random polling without positive spanning sets → probabilistic descent; the random-direction numerics came first [S049 pp. 14–15, 17] and were reproduced before the theory [S019 pp. 2, 6–7].

<a id="heuristic-3"></a>

## Heuristic 3: accuracy on the quantity the acceptance test uses

- **H3 · If information is inexact or noisy, then put the accuracy requirement on the quantity the acceptance test uses, tie it to the step size or predicted decrease, make it checkable at the iteration, and let the iteration (or the data) decide the effort.** Case: weak tail bound (2024) [S067 pp. 5–8]; sequential test (2025) [S102 pp. 5, 10]; inexact SQP whose "bounds on the inexactness do not rely on Lipschitz constants, derivative bounds, and other quantities that are difficult to obtain in practice" [S013 p. 2].

<a id="heuristic-4"></a>

## Heuristic 4: several objectives without derivatives: a nondominated list

- **H4 · If there are several objectives and no derivatives, then keep a nondominated list; do not aggregate.** Case: DMS [S003 pp. 1–2]; the fairness front [S016 pp. 2, 4, 13]. Scope: in the gradient-based ML line, weights appear in the analysis or as step frequencies and fronts are traced by sweeping them [S015 pp. 3, 6–8; S093 pp. 3, 17; S111 p. 4].

<a id="heuristic-6"></a>

## Heuristic 6: merit function vs extreme barrier

- **H6 · If some constraints may be violated during the run and others may not, then use a merit function (+ restoration) for the former and an extreme barrier for the latter.** Case: Gratton & Vicente 2014 [S049 pp. 1, 4–6]; extreme barrier in the ES and PSwarm papers [S057 p. 3; S005 pp. 6–7].

<a id="heuristic-7"></a>

## Heuristic 7: reuse evaluations already paid for

- **H7 · If you have already paid for evaluations, then reuse them** with simplex gradients to order the poll and minimum-Frobenius-norm models in the search step. Case: simplex-gradient ordering cut evaluations by about half on its test set [S008 pp. 7–9, 17]; MFN search steps [S012 p. 7].

<a id="heuristic-8"></a>

## Heuristic 8: formalize an informal notion

- **H8 · If practitioners use an informal notion ("knee"), then formalize its verbal definition and state the formalization's restrictions up front.** Case: Pareto sensitivity: "a widely accepted (quantitative) definition for such solutions is lacking" [S096 p. 3]; the abstract says the approach is "restricted to scalarized methods" [S096 p. 1].

<a id="heuristic-10"></a>

## Heuristic 10: print the edge next to the result

- **H10 · If a result has an edge (a rejected design alternative, a hypothesis at the edge of regularity, a proof that does not extend, code that departs from the analysed algorithm), then print the edge next to the result**: the smallest example on which the alternative or hypothesis fails; the exact inequality or case where the proof stops, with the algorithmic freedom that had to be removed; each code departure with its reason; where the strongest baseline wins. Cases: one test function per violated hypothesis, rerun at a tighter tolerance [S024 pp. 17–23]; a counterexample to the paper's own definition, supplied by Audet and printed up front with the scope narrowed [S083 p. 3]; a conjecture printed with the failing inequality [S014 pp. 20–21]; search step off and step size never increased so that a theorem goes through [S049 p. 12]; a mechanistic reason for a two-piece limit [S024 p. 23]; code departures labelled (Warning sign 8); a whole negative-result paper [S079 pp. 3, 23]. Grade: practiced from 1998 to 2026 (08 §4.1), but never stated as a general rule and shared with the Powell, Conn and Audet lenses, so it is a heuristic, not a core method.

<a id="heuristic-11"></a>

## Heuristic 11: import a certified result from another field

- **H11 · If a constant, subproblem or test in your method has an equivalent in another field, then restate it in that field's language and import that field's certified result or solver, with a specialist coauthor.** Cases: the cosine measure recast as a sphere-covering radius [S041 pp. 6–8]; compressed-sensing recovery for sparse Hessian models [S029 pp. 2, 28]; Wald's SPRT bounds for the acceptance test [S102 pp. 9–10]; DC programming from its developers [S064 pp. 2, 4].

<a id="heuristic-12"></a>

## Heuristic 12: known-answer testbeds

- **H12 · If no benchmark with known answers exists, then generate one with planted solutions and controlled difficulty, certify the instances against the competitors' assumptions, and release the generator as its own citable artefact; in applications, climb a planted-truth ladder (calibrated case → synthetic with known answer → real data).** Cases: QP and bilevel generators [S053 pp. 1–2, 14; S026 pp. 1, 15–16] with the code as a TOMS paper [D001 pp. 1–4]; planted truth in finance and astrophysics [S028 pp. 14–15; S075 pp. 4–8]. Era-bound (1993–2012); later papers use closed-form test instances [S042 p. 26].

<a id="signature-s008"></a>

## Signature work: Using sampling and simplex derivatives in pattern search methods (SIAM J. Optim. 18, 2007) [S008]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | An observed phenomenon: "The curve representing the objective function value as a function of the number of function evaluations frequently exhibits an L-shape for pattern search runs." [p. 1]. Custódio's PhD (Coimbra 2007, advisor Vicente; thesis record). |
| Why then | Vicente's concurrent sample-set geometry work supplied the simplex-gradient error bounds [pp. 6, 19; S010; S020]. |
| Key insight | A Λ-poised subset of stored points gives a simplex gradient that orders the poll and decides mesh expansion, at no extra evaluation and without touching the convergence requirements [pp. 2, 7–9]; after an unsuccessful poll the geometry comes for free [pp. 10–11]. |
| Minimal evidence | 27 CUTEr problems, 120 versions; simplex-gradient ordering cut evaluations by 51% on average against 11% for dynamic polling [pp. 14–17]. Aggregate tables, not profiles. |
| Abandoned paths | Pruning the poll to one direction lost quality (a test that violated the theory's conditions, and said so) [p. 18]; the model search step was deferred as "the topic of a separate research" [p. 13]. |
| Glue and naming | Rational-lattice mesh with simple decrease; sufficient decrease only in the mesh-expansion rule [pp. 3–4, 14]. The MFN search step appears in the 2010 COAP paper [S012 pp. 6–8] and in the later SID-PSM v1.3 manual [S059 pp. 1–7]; when the name SID-PSM first appeared was not established from the texts read. |
| Reception | Widely cited; the SID-PSM solver packages this paper and the 2010 one (MATLAB, LGPL [S059 p. 1]; v1.3 dated Dec 2014 on the software page). |
| Methods shown | Method 1 (dated glue), H7, Method 5 (tables; no code statement in the paper), H10 |

<a id="signature-s003"></a>

## Signature work: Direct multisearch for multiobjective optimization (SIAM J. Optim. 21, 2011, DOI 10.1137/10079731X) [S003]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | A-priori aggregation needs weights, returns one point and must be rerun when preferences change; varying weights may not spread points on nonconvex fronts [p. 2]. Mostly written during a Courant Institute visit [p. 1]. |
| Why then | The direct-search template was shared with the concurrent discontinuous-functions paper [S024; pp. 27, 33]; the AMPL recoding habit came from PSwarm [S005 p. 14]. |
| Key insight | The incumbent becomes a list of nondominated (x; α) pairs, success means the list changed, and sufficient decrease becomes F(x) ∉ D(L; ρ̄(α)); with one objective DMS is direct search [pp. 2, 4–5]. One proof covers lattice and sufficient-decrease globalizations [pp. 28–31]. |
| Minimal evidence | 100 bound-constrained problems recoded in AMPL and made public: 69 bi-, 30 tri- and 1 four-objective (FES3) [p. 16, Table 5.1]; eight public solvers tested, best three reported; purity only pairwise; spread Γ/Δ [pp. 15–20]. |
| Abandoned paths / boundary | A randomized orthogonal poll was not better [p. 20]. NSGA-II is slightly better on Δ and BIMADS wins on ZDT4 [pp. 23–25]. The theory gives a limit point in a stationary form of the front; the numerics use a non-dense poll with ρ̄ = 0 [pp. 20, 26]. Errata posted on the DMS site (not inspected). |
| Reception | Many follow-ups by others, including a mesh-adaptive direct multisearch (COAP 2021) that benchmarks against DMS. |
| Methods shown | Method 4, H4, Method 5, H10 |

<a id="signature-s023"></a>

## Signature work: Worst case complexity of direct search (EURO J. Comput. Optim. 1, 2013, DOI 10.1007/s13675-012-0003-7) [S023]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | An analogy: steepest descent needs O(ε⁻²) iterations, and direct search with positive spanning sets is "of descent type" [p. 2]. A single-author note written during a Courant Institute visit [p. 1]; every comparison is with 2004–2012 derivative-based complexity results [pp. 2, 8–9]. |
| Why then | "Intuitively speaking, insisting on a sufficient decrease will make the function values decrease by a certain non-negligible amount each time a successful iteration is performed." [p. 4]. |
| Key insight | Two counters (successes via a step-size floor and telescoped decrease; failures via the log of the step-size product): O(ε⁻²) iterations and O(n²ε⁻²) evaluations, n² = cm⁻² × poll size [pp. 5–8]. |
| Minimal evidence | A short proof; ε-order tightness borrowed by reduction to steepest descent in dimension 1 [p. 8]; no numerics. |
| Abandoned paths / boundary | ρ = ctᵖ with p ≠ 2 performed worse in earlier numerics [p. 7]; the lattice route is explicitly not covered [pp. 4, 9]; finite-difference adaptive cubic regularization has a better ε-power [p. 9]. |
| Reception | A programme: convex [S046], n-order optimality within the PSS template [S041], smoothing [S034], probabilistic descent [S019 p. 12], multiobjective rates [S015]. |
| Methods shown | Method 2, H10 |

<a id="signature-s019"></a>

## Signature work: Direct search based on probabilistic descent (SIAM J. Optim. 25(3), 2015) [S019]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | "we were surprised by the numerical experiments reported [18]" [p. 2]: random polling directions, possibly fewer than n + 1, did better; [18] is the merit-function paper [S049 pp. 14–15]. Reproduced in Table 1: m = 2 random directions best on most problems [pp. 6–7]. |
| Why then | Complexity counting (2013) plus conditioning on the past from the probabilistic trust-region paper [p. 8; S014 p. 7]. |
| Key insight | The proof uses cm(D_k, −g_k), not the cosine measure over all vectors [p. 5]; ask for it with probability p given the past. p₀ = ln θ / ln(γ⁻¹θ) [p. 9]; m > log₂[1 − ln θ / ln γ] directions suffice [p. 20]. |
| Minimal evidence | Almost-sure convergence; O(ε⁻²) with overwhelming probability; O(mnε⁻²) evaluations against O(n²ε⁻²) [pp. 9–17]; the abstract calls the rate "matching" [p. 1]. 10 CUTEr problems at n = 40 and 100 [pp. 20–21]. |
| Abandoned paths / boundary | The first experiment was "biased in favor" of the new method and was rerun with the baselines at their best; the gain shrank but remained [pp. 20–21]. The {d, −d} design is left open [pp. 22–23]. |
| Reception | Trust-region rates along §6's road map [S027 p. 3]; constrained extension [S045]; sequential-test and non-monotone successors [S102; S110]. Huang & Zhang (2026, arXiv:2606.01320; abstract read, paper not read) report non-convergence without the threshold condition. |
| Methods shown | Method 3, Method 2, H2, H10 |

<a id="signature-s050"></a>

## Signature work: Globally convergent evolution strategies (Math. Program. 152, 2015, DOI 10.1007/s10107-014-0793-x) [S050]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | No global convergence results existed for (µ/µ_W, λ)-ES in the nonlinear-optimization sense [p. 2]; the two fields "have historically had little connection, in part because of major differences in terminology and notation" [p. 2]. First author Diouane (CERFACS, TOTAL-supported [p. 1]); his Toulouse PhD thesis is in the Appendix. |
| Why then | The sufficient-decrease line did not need a lattice, whereas MADS would have required discrete ES sampling [p. 2]. |
| Key insight | Change the ES "in a minimal way" [p. 4]: a separate step size with sufficient decrease on the mean, contraction on failure, reset σ_{k+1} = max{σ_k, σ^ES_k} on success; sampling, selection, recombination and the CMA updates untouched [pp. 4–6]. |
| Minimal evidence | Clarke stationarity under density of directions [pp. 8–10]; 53 Moré–Wild problems with data profiles (50n budget) and performance profiles; a multimodal suite with medians over 20 starts [pp. 12–18]. |
| Abandoned paths / boundary | An acceptance combination dropped because it was hard to prove [p. 5]. MADS is slightly better at small budgets; pure CMA-ES is more robust on piecewise-smooth problems [pp. 15–18]. A weight condition the theory needs was not enforced in the runs, and the paper says why [p. 11]. |
| Reception | Constrained sequel with an extreme barrier [S057]; a parallel ES for 3D full-waveform inversion [S068]. |
| Methods shown | Method 1 (step 4 reset), Method 5, H1, H10 |

<a id="signature-s067"></a>

## Signature work: Stochastic trust-region and direct-search methods: a weak tail bound condition and reduced sample sizing (SIAM J. Optim. 34, 2024, DOI 10.1137/22M1543446) [S067]

All six were read in full text; bare page numbers refer to the card in the heading.

| Dimension | Content |
|---|---|
| Origin | Stochastic trust-region and direct-search methods need O(Δ_k⁻⁴) samples per iteration under finite variance [p. 4]; model-based stochastic DFO needs gradient estimates not available for nonsmooth f [p. 3]. |
| Why then | The probabilistic-models line [S014] and a nonsmooth DFO trust-region method with Rinaldi and coauthors [p. 15] were in hand. |
| Key insight | One tail bound on the reduction estimate the acceptance test uses [p. 3], scaled with the sufficient-decrease power q (Workflow D); the same change goes through direct search and trust region [pp. 10–18]. |
| Minimal evidence | Almost-sure Clarke stationarity via a potential and Borel–Cantelli [pp. 11–14]; rivals' conditions shown to imply the new one [p. 9]; 96 nonsmooth problems × 10 runs, profiles on the true f, StoMADS as baseline [pp. 19–23]. |
| Abandoned paths / boundary | Remark 5.1: fewer samples per iteration need not mean less total cost, since lower q can raise the iteration complexity. Remark 5.2: the runs use an acceptance constant far below the proven threshold; "Finding weaker versions of (3.1) that still guarantee convergence under reasonable assumptions remains of course an open problem to be studied more in depth in future works." [p. 20]. No rates. |
| Reception | The sequential-test paper takes up Remark 5.1 as its entry point [S102 p. 3]: a disclosed boundary becomes the next paper. |
| Methods shown | Method 3, Method 4, H3, H10 |

<a id="anti-patterns"></a>

## Research anti-patterns

| Anti-pattern | Why Vicente's work argues against it (source) | Do instead |
|---|---|---|
| Publishing a tuned heuristic with no convergence safeguard | ES 2015 and PSwarm 2007 add the safeguard cheaply [S050 pp. 4–6; S005 pp. 8–10] | Method 1 wrapper |
| Scalarizing objectives with fixed weights before seeing the front | DMS "does not aggregate" [S003 p. 1]; the fairness work builds the complete front [S016 pp. 2, 4] (derivative-free line) | Nondominated list; knees afterwards |
| A fixed large sample size every iteration | Tail-bound and sequential-test sampling [S067 pp. 5–8; S102 pp. 3, 10] | Control the estimated decrease adaptively |
| Using 1 random direction "because randomization is cheap" | The guarantee is joint in step factors and direction count [S019 p. 20]; one direction under S102's condition 3 log γ + 11 log θ > 0 [S102 p. 16]; non-convergence reported below the threshold (Huang & Zhang 2026) | Meet the threshold for your (γ, θ, m); print the rule |
| Claiming efficiency from a handful of problems | DMS used 100 problems with class-specific profiles [S003 pp. 15–20]; PSwarm 122 [S005 p. 14] | Collection + profiles + strongest baseline |
| Theorem for discontinuous f with no adversarial check | The 2012 result was counterexampled in 2024 (Inner Tensions) | Search for counterexamples (H10); add a "revealing" poll |
| Treating penalty parameters and barriers uniformly for all constraints | Merit function + extreme barrier split [S049 pp. 4–6] | Classify constraints as relaxable or unrelaxable |
| Reporting only the settings where you win, or keeping a biased motivating experiment | Losses reported by class and budget [S050 pp. 15–18; S003 pp. 23–25]; biased experiment rerun (Taste mark 7) | H10; Workflow F step 4 |
| Shipping code that silently differs from the analysed algorithm | Each departure labelled with its reason (Warning sign 8) | H10 |
| Calling a condition "weaker" without comparing | Rivals' conditions proved to imply the new one [S067 p. 9; S102 p. 7] | Prove the implication before the claim |
| Counting per-iteration savings as total savings | The tail-bound paper warns that fewer samples per iteration need not reduce total cost [S067 p. 20, Remark 5.1], and the sequential-test paper builds on that caveat [S102 p. 3]; the gap persists in [S102 p. 16; S110 p. 14] (Inner Tensions) | Report total evaluations or samples to reach ε |

<a id="research-trajectory"></a>

## Research trajectory (table, prose and Latest)

| Period | Main direction | Trigger (inferred unless cited) | Representative work |
|---|---|---|---|
| 1991–1995 | Bilevel programming, complementarity, test-problem generators (Coimbra, Waterloo, GERAD) | Collaboration with Calamai and Júdice | Bilevel bibliography [S002]; generators [S053; S026; D001] |
| 1996–2000 | Derivative-based NLP: trust-region interior-point SQP for optimal control | PhD at Rice with John Dennis | Thesis 1996 (Tucker Prize finalist) [S040]; TRIP SQP [S011]; TRICE [H007] |
| 2001–2005 | Transition: direct search enters through an application; surrogates via space mapping; derivative-based work continues | An application contact [S106 p. 1]; a special issue co-edited with Audet and Dennis [H001] | User-provided points in pattern search [S106; S025]; inexact SQP [S013]; space mapping [S062] |
| 2006–2010 | Direct search made efficient (reuse, models, swarm) + model geometry; DFO book | Coimbra faculty; first PhD student (Custódio, thesis record); Conn–Scheinberg collaboration | PSwarm [S005]; SID-PSM [S008]; MFN [S012]; geometry papers [S010; S020; S006]; book [S001] |
| 2011–2015 | New problem classes + complexity + probability; ES | Complexity wave; numerical evidence for random polling [S019 p. 2]; Gratton collaboration | DMS [S003]; discontinuous [S024]; WCC [S023]; merit [S049]; probabilistic TR [S014]; probabilistic descent [S019]; ES [S050]; Lagrange Prize 2015 |
| 2016–2020 | Complexity programme and probabilistic extensions; move to Lehigh (ISE chair, 2018) | Toulouse collaborations (Gratton, Royer, Zhang) | Convex and optimal-order WCC [S046; S041]; TR rates [S027]; constrained [S045]; MOO complexity [S015] |
| 2021–2026 | Lehigh: stochastic ML-facing methods (multi-objective, bilevel, trilevel); stochastic DFO sampling; Pareto analysis | The probabilistic line meets the noisy ML setting | SMG [S017]; fairness [S016]; bilevel/trilevel SG [S042; S091]; full-low [S073]; tail bound [S067]; sequential test [S102]; Pareto sensitivity [S096]; non-monotone [S110] |

What stayed constant: keep the skeleton, change one object (1996 [S037 pp. 5–7] to 2026 [S110 p. 4]); inexactness tied to progress (1996 [S040 p. 136] to 2025 [S042 pp. 13–14]); artefacts (generators, TRICE, PSwarm/SID-PSM, the DMS collection, GitHub code); printing the boundary (H10; 1998 [H003 pp. 4, 18–19] to 2026 [S110 p. 14]). *The first stochastic version of a known formalism* (2024–2026) [S042 p. 5; S091 pp. 1–2] is a field-wide trend of that period, recorded here, not as taste.

### Latest

- Sep 2026: Ding, Tran & Vicente, "Non-monotone direct-search methods for deterministic and stochastic derivative-free optimization" (arXiv:2609.11567) [S110].
- May 2026: Tran & Vicente, "Stochastic block coordinate and function alternation for multi-objective optimization and learning" (arXiv:2605.12432) [S111].
- Mar 2026: Pareto sensitivity paper v3 (arXiv:2501.16993) [S096].
- Sep 2025: Ding, Rinaldi & Vicente, "Sequential test sampling for stochastic derivative-free optimization" (arXiv:2509.14505) [S102].
- Service: SIAG/OPT chair 2023–2025 (signed Chair's Columns [S122 pp. 23–24; S121 p. 14]); SIAM Fellow 2024 ("for ground-breaking contributions to derivative-free and bilevel optimization, and exemplary leadership in editorial and organizational service to the SIAM community").

<a id="academic-lineage"></a>

## Academic lineage

John E. Dennis Jr. (Rice; PhD advisor, 1996) → **Vicente** → Ana Luísa Custódio (Coimbra 2007), Youssef Diouane (INP Toulouse 2014, co-advised with Serge Gratton), Clément W. Royer (Toulouse 2016, co-advised with Gratton), Suyun Liu (Lehigh 2022) (thesis records), and others (Math Genealogy lists 14 students; unverified individually). The papers signal doctoral status for some junior coauthors: FCT SFRH/BD doctoral scholarships for Garmanjani and Dodangeh [S034 p. 1; S046 p. 1; S041 p. 1], a Toulouse doctoral grant for Royer [S019 p. 1], and Kent's Lehigh PhD thesis, cited as in preparation [S091 p. 6, ref. 26]; Tran was a Lehigh postdoc [S110 p. 1]. The advising relation itself is not stated in these texts.

Key collaborators: Conn and Scheinberg (book; model geometry; probabilistic models), Gratton (14 joint works, 2014–2022), Vaz, Giovannelli, Custódio, Z. Zhang, Rinaldi, Berahas: one or two long pairings per period, each tied to a line of work; no single-authored research work after 2013 (08 §9). Dennis also co-authored the MADS line with Audet, and Audet, Dennis and Vicente co-edited a 2004 surrogate-optimization special issue [H001].

<a id="inner-tensions"></a>

## Inner tensions

- **Worst-case countability vs typical performance.** The case for a method rests on evaluation-count bounds (Method 2), which are pessimistic, so practical claims rest on profiles (Method 5), and the bound does not always predict the ranking: "Despite the fact of exhibiting a worse WCC bound, the smoothing approach worked much better than the composite one" [S032 p. 22].
- **Generality vs correctness.** Pushing the direct-search analysis to discontinuous functions produced a theorem later counterexampled (Audet, Bouchet & Bourdin 2024; not read here). The 2012 paper stated its hypotheses and a mechanistic reason for its two-piece limit [S024 pp. 11, 15, 23], and its numerical suite was built one test function per hypothesis [S024 pp. 17–23]. *Lesson drawn by this skill from the 2024 counterexample, not documented as Vicente's practice: also aim one example at a proof step, not only at the hypotheses.* DMS needed posted errata.
- **Direct-search skeleton vs borrowing derivatives and models.** SID-PSM and MFN import models, Full-low evaluation uses finite-difference BFGS, Pareto sensitivity *requires* derivatives, and a 2017 paper asks when to switch from derivative-free to derivative-based [S104 p. 2]. In the papers, the skeleton is used to guarantee convergence alongside models and derivatives.
- **DFO core vs the ML pivot.** After 2018 much of the output is gradient-based stochastic multi-objective and bilevel work; the stochastic-DFO papers reconnect the two. No source explains the pivot in his own words; the only signed sentence is a service column listing "scalable stochastic methods" first among major developments [S121 p. 14].
- **Randomization savings vs the probability threshold.** Randomization cuts evaluations only above a threshold (Huang & Zhang 2026, abstract read, report non-convergence below it), and tuned constants can sit below proven thresholds [S067 p. 20].
- **Evaluations as the unit vs what the recent papers count (say vs do).** Method 2's stated unit is the function evaluation [S038 p. 8], but several 2023–2026 papers bound iterations and leave total samples open [S073 pp. 8–9; S102 p. 16; S110 p. 14]. The tail-bound paper itself discloses that fewer samples per iteration need not reduce total cost [S067 p. 20], and the sequential-test paper builds on that caveat [S102 p. 3].
- **Analysed algorithm vs shipped code.** The theory covers an idealized algorithm; the code is tuned. The papers resolve this by disclosure (H10), not by making the two identical.

<a id="mentor-voice"></a>

## Mentor voice

*Reconstructed from written artefacts. **None of these are documented quotes.***

- Feedback style (inferred from the papers): a structural question first ("what is your acceptance test?"), then cost accounting ("how many evaluations per iteration, and how does that scale with n?"), then evidence ("which collection, which profile?"), then the boundary ("where do you lose?").
- Typical questions (paraphrase-style, not quotes): "Where does convergence come from in your method: search or poll?" "Is the decrease sufficient or simple?" "What is the price in complexity of your generalization?" "Which of your constraints can be violated during the run?" "Is the code public?" "Which inequality stops your proof, and have you written it down?" "Did you rerun the first experiment with the baselines at their best?"
- Register: formal and precise in the papers; limitations stated in abstracts (e.g., "restricted to scalarized methods" [S096 p. 1]); hedges local and concrete ("slightly better", "not overwhelming") [S050 p. 17; S003 p. 21]. The signed service columns are warmer, but that is service writing [S122 p. 23].
- Avoid: grand claims of global optimality; promising gains without an evaluation count; limitations stated only in general terms.

<a id="corrections"></a>

## Corrections from the full texts

Every row below is a correction that the full-text reading made to the first-pass (web-snippet) version of SKILL.md. The decisions and card lists come from `08-deep-reading-synthesis.md` §3.1–3.2, §3.4 and §5; the "Corrected wording" column quotes SKILL.md as it stood before tightening (the section it sat in is named in brackets). SKILL.md keeps a one-line version of the main rows under "Corrections from the full texts".

| # | First-pass claim | Corrected wording (SKILL.md before tightening) | Cards | Synthesis row |
|---|---|---|---|---|
| 1 | Method 1: "sufficient decrease (not a mesh) is the glue" | "an integer-lattice mesh with simple decrease in the 2001–2012 papers, sufficient decrease from 2013 on" (Method 1, one line); "one proof for both in 2011–2012" (Method 1, variants) | [S008 pp. 3–4; S059 pp. 6–7; S003 pp. 28–31; S024 p. 6; S023 p. 4; S049 p. 2] | 08 §3.1 row 1 |
| 2 | DMS test set "69 bi-, 29 tri-, 2 four-objective" | "69 bi-, 30 tri- and 1 four-objective (FES3)" (DMS anatomy) | [S003 p. 16, Table 5.1] | 08 §3.1 row 2 |
| 3 | Probabilistic trust-region rates (attribution to the 2014 paper) | "the 2014 paper proves almost-sure convergence only [S014 pp. 8–13]" (Method 2, evidence); rates are cited to [S027 pp. 5, 8–11] | [S014 pp. 8–13, 20–21; S027 pp. 5, 8–11] | 08 §3.1 row 3 |
| 4 | "optimal n² factor" (Taste 2; Method 2 practice and limitations; Heuristic 9) | "the n² factor optimal among positive-spanning-set choices within the sufficient-decrease bound, not as an oracle lower bound" (Taste mark 2); H9 retired into Method 2 step 5 | [S041 pp. 1, 5, 8] | 08 §3.1 row 4 |
| 5 | "the Lehigh papers ship GitHub code (MOO_Fairness, BSG_Methods_Con_Unc, snee)" | "public code in 8 of 22 Lehigh experimental papers (2021–2026)" (Taste mark 5); the "snee" repository listed as not inspected (Honest Boundary) | [S016 p. 5; S042 p. 22; S088 p. 14] | 08 §3.1 row 5 |
| 6 | Non-monotone direct search listed under Method 1 | "non-monotone max-M acceptance [S110 pp. 4, 6, 10]" (Method 4, practice) | [S110 pp. 4, 6, 10, 14] | 08 §3.1 row 6 |
| 7 | Random polling "leads to better complexity bounds as well as to gains in numerical efficiency" attributed to the 2015 abstract | quoted with "[S045 p. 1, 2019]"; "the 2015 abstract calls its rate "matching" the deterministic one [S019 p. 1]" (Method 3, evidence) | [S045 p. 1; S019 pp. 1, 16] | 08 §3.1 row 7 |
| 8 | SID-PSM anatomy: models built in the 2007 paper; SID-PSM = the 2007 paper | "the model search step was deferred as "the topic of a separate research" [p. 13]"; "The MFN search step appears in the 2010 COAP paper [S012 pp. 6–8] … when the name SID-PSM first appeared was not established from the texts read" (SID-PSM anatomy) | [S008 pp. 3–4, 13; S012 pp. 6–8; S059 pp. 1–7] | 08 §3.2 row 8 |
| 9 | Method 2 stated: "recovering classical convergence rates" dated to 2026 | earlier instances in 2019 and 2023; SKILL.md quotes the sentence without a date [S111 p. 1] | [S015 pp. 2, 9; S093 p. 3; S111 p. 1] | 08 §3.2 row 9 |
| 10 | Method 3 "Different from standard practice" (vs stochastic approximation), unscoped | "✅ stated + practiced for the DFO line; not as a contrast with stochastic approximation in the bilevel/trilevel SG papers" (Method 3, say–do) | [S042 pp. 13–14, 18; S091 pp. 5–6] | 08 §3.2 row 10 |
| 11 | Anti-pattern "Using 1 random direction" and Method 3 step 5 | the threshold is joint in step factors and direction count: "one direction with 3 log γ + 11 log θ > 0, e.g. θ = 0.95, γ = 1.3"; "m = 2 for γ = 2, θ = 1/2"; S067's θ = 0.5 runs below its proven threshold, disclosed (Method 3, step 5 and variants) | [S102 pp. 16–18; S019 p. 20; S067 p. 20] | 08 §3.2 row 11 |
| 12 | Workflow D without preconditions | a known bound on ε_q, the θ threshold, the common-random-numbers route and q ∈ (1, 2] added (Workflow D, steps and defaults) | [S067 pp. 5–8, 11] | 08 §3.2 row 12 |
| 13 | Research Trajectory without 1991–1995; direct search from 1996 | 1991–1995 row added; direct search enters in 2001–2005; derivative-based work continues (Research Trajectory) | 08 §8 | 08 §3.2 row 13 |
| 14 | Honest Boundary: "Web-search snippets only … No full text … was read" | 108 of 124 works read in full text (Honest Boundary, coverage) | 08 §1 | 08 §3.2 row 14 |
| 15 | Honest Boundary: "Method 5's stated evidence is a single quote" | stated side of Method 5 rests on [S053 p. 14], a 2006 essay and a 2017 survey (Method 5, evidence; Honest Boundary) | [S053 p. 14; S109 p. 5; S038 pp. 4–13] | 08 §3.2 row 15 |
| 16 | Heuristic 10 labelled "lesson from critique, not a rule Vicente stated" | H10 partly practiced ("Grade: practiced from 1998 to 2026 … never stated as a general rule"); the proof-step clause kept as a labelled lesson under Inner Tensions | [S083 p. 3; S024 pp. 17–23] | 08 §3.2 row 16; §5 |
| 17 | Mentor Voice register "formal and precise" only | "The signed service columns are warmer, but that is service writing [S122 p. 23]" (Mentor Voice) | [S122 p. 23; S121 p. 14] | 08 §3.2 row 17 |
| 18 | Latest · Service unconfirmed | "SIAG/OPT chair 2023–2025 (signed Chair's Columns [S122 pp. 23–24; S121 p. 14])" (Latest) | [S122 pp. 23–24; S121 p. 14] | 08 §3.2 row 18 |
| 19 | Inner Tension "DFO core vs ML pivot" | "the only signed sentence is a service column listing "scalable stochastic methods" first among major developments [S121 p. 14]" (Inner Tensions) | [S121 p. 14] | 08 §3.2 row 19 |
| 20 | Inner Tension "worst case vs typical" | "Despite the fact of exhibiting a worse WCC bound, the smoothing approach worked much better than the composite one" [S032 p. 22] (Inner Tensions) | [S032 p. 22] | 08 §3.2 row 20 |
| 21 | Heuristic 4 unscoped | "Scope: in the gradient-based ML line, weights appear in the analysis or as step frequencies and fronts are traced by sweeping them" (H4) | [S015 pp. 3, 6–8; S093 pp. 3, 17; S111 p. 4] | 08 §3.4; §5 |
| 22 | Heuristics H5 (smoothing) and H9 (is the n-order optimal?) | retired numbers: "smoothing now sits in Method 4 step 2; "is the n-order optimal?" in Method 2 step 5" (Research Heuristics) | [S034 p. 7; S041 pp. 1, 5, 8] | 08 §5 |
