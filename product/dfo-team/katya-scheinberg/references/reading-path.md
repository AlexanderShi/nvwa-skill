# Reading path for a new student in Scheinberg's group

> Research date: 2026-09-27 (full-text pass). **Every entry in Stages 0–7 was read in full** for this skill and has a paper card (id in brackets; index in `research/07-paper-cards.md`); the page numbers refer to the version named on the card. The order follows how the papers build on each other in the full texts (`research/08-deep-reading-synthesis.md` §8.4). It is the skill author's suggestion, **not** a reading list Scheinberg has published. If your supervisor gives you a list, use that one instead.
>
> For each item the line says **what method to take from it**, not only what it proves. Read with `proof-playbook.md` open (the template labels T0–T15 point there) and with `technique-catalog.md` for the named devices (P, A, E, W numbers).

## How to read (suggested habit, drawn from the group's paper pattern)

For every paper in Stages 2–7, write one index card:

1. the oracle contract (accuracy form + probability + conditioning);
2. the classical method and the exact change made;
3. the proof template (a joint potential / b counting / c concentration) and the step-parameter argument;
4. the bound (type, order, constants, noise floor);
5. what the *next* paper in this list relaxes, and which earlier theorem it imports.

After Stage 4 you should be able to predict the assumptions of the unreliable-inputs paper [S083] from the ones before it. If you cannot, reread T4 and T7 in the playbook.

## Stage 0 · Orientation (1–2 weeks)

| # | Work | What to learn from it (method, not just result) |
|---|---|---|
| 0a | Curtis, Scheinberg. Adaptive stochastic optimization: a framework for analyzing stochastic optimization algorithms. *IEEE Signal Processing Magazine* 37(5), 32–42 (2020). arXiv:2001.06699 [S047] | The whole programme in one article: the deterministic and stochastic methods in the same algorithm box with two probability knobs (pp. 4, 7); a progress measure that decreases on every iteration (p. 3); potentials by method (pp. 4–6); the expected stopping-time theorem (p. 8); and the open problems stated with their exact blockers (p. 12). |
| 0b | Custódio, Vicente, Scheinberg. Methodologies and software for derivative-free optimization. In *Advances and Trends in Optimization with Engineering Applications*, SIAM (2017), ch. 37. https://doi.org/10.1137/1.9781611974683.ch37 [S046] | How the DFO side of the group maps its field: fully linear models (p. 3), the geometry debate settled: geometry "cannot be totally ignored", and the self-correcting method "resorts to geometry-improving steps only when the model gradient is small" (pp. 3–4), complexity stated in iterations *and* function evaluations with n explicit (p. 8). |
| 0c (optional) | Curtis, Scheinberg. Optimization methods for supervised machine learning: from linear models to deep learning. *INFORMS TutORials in OR* (2017). https://doi.org/10.1287/educ.2017.0168 [S031] | How the two authors explain ML optimization to an OR audience: a glossary across the two communities (p. 2); why SGD wins in theory for large-scale ML ("at least in theory, SGD is a superior algorithm", p. 10) and where its parameter sensitivity hurts in practice (pp. 8–11); an early tutorial statement of the oracle contract: sample sizes chosen large enough relative to the step (p. 21). (The contract itself is stated earlier, in BSV 2014 [S018, pp. 6–7] and STORM [S012, pp. 8–9].) |

## Stage 1 · Foundations: deterministic model-based DFO (3–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 1 | Conn, Scheinberg, Toint. Recent progress in unconstrained nonlinear optimization without derivatives. *Math. Program.* 79 (1997). https://doi.org/10.1007/BF02614326 [S004] | Geometry as the defining ingredient of model-based DFO (pp. 8–9, 17); the first statement of "sufficient sampling" for noisy f and of exploiting structure (p. 17); how to tell a field's history along one design axis (pp. 3–6). |
| 2 | Conn, Scheinberg, Toint. On the convergence of derivative-free methods for unconstrained optimization (1997; Powell tribute volume) [S008] | The deterministic proof template every later paper modifies (T0): the radius is not reduced before geometry is adequate (p. 14, p. 17), the criticality loop, and the "three important aspects" where the standard trust-region proof breaks (pp. 17–18). Abstract predicates ("no need to specify exactly how this is done", p. 13) are the seed of the prove-once, instantiate-by-checklist habit (SKILL.md Heuristic 8). |
| 3 | Conn, Scheinberg, Vicente. Geometry of interpolation sets in derivative free optimization. *Math. Program.* 111 (2008) [S016] | Where the model-error constants come from (Λ-poisedness × Lipschitz × radius; pp. 12–17) and how to measure poisedness with a condition number (pp. 3, 8–11). Note the 2008 practical position: maintain poisedness throughout (p. 18); it changes a year later. |
| 4 | Conn, Scheinberg, Vicente. Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points. *SIAM J. Optim.* (2009). https://doi.org/10.1137/060673424 [S007] | The fully linear / fully quadratic *class*, proved once and instantiated for interpolation and regression, with an analysis "independent of the sampling techniques" (pp. 1, 7–13); certification only after a failed ratio test and in the criticality step (pp. 13–14). |
| 5 | Scheinberg. Geometry in model-based algorithms for derivative-free unconstrained optimization. *Optima* 79 (May 2009) [S143] | Her own short statement of the minimal-safeguard position (p. 4), the hand-checkable 2-D counterexample (pp. 4–5), and how to credit a competitor's encouraging results before showing by a counterexample that its method can converge to a non-stationary point (p. 4). Read only her article (pp. 1–6); the discussion column that follows is Nocedal's. |
| 6 | Scheinberg, Toint. Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization. *SIAM J. Optim.* 20 (2010) [S030] | How to use a **negative result** (geometry steps cannot be fully removed, pp. 8–11) to design the minimal safeguard (Method 4): the self-correction lemma (pp. 14–15) and the volume potential for finite termination (p. 6). |
| 7 | Zhang, Conn, Scheinberg. A derivative-free algorithm for least-squares minimization. *SIAM J. Optim.* 20 (2010) [S023] | Structure first (Method 6): per-residual models on one sample set (pp. 2, 5, 16–17). Also the group's benchmark protocol in its first full form: Moré–Wild set, data profiles in simplex gradients, noise-matched tolerances (pp. 17–19). |

## Stage 2 · Probabilistic models: the pivot (4–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 8 | Bandeira, Scheinberg, Vicente. Convergence of trust-region methods based on probabilistic models. *SIAM J. Optim.* 24(3) (2014). arXiv:1304.2808 [S018] | The key move: keep the algorithm and require model quality only with probability ≥ 1/2, *conditioned on the past* (pp. 6–7), with one change to the acceptance test (p. 8). Learn the split between a safety lemma on every sample path (pp. 8–9) and the submartingale random walk (pp. 10–11) (T1), and how Conjecture 5.1 names the inequality that fails (pp. 20–21). |
| 9 | Chen, Menickelly, Scheinberg. Stochastic optimization using a trust-region method and random models (STORM). *Math. Program.* 169 (2018) [S012] | How to put *function estimates* under the same contract, with accuracy ∝ Δ_k² (pp. 8–9); the joint potential and its case grid (pp. 14–19); what the probability conditions really require (α, β near 1, pp. 20–21) and how the experiments probe that threshold (pp. 30–32) (T2). |
| 10 | Cartis, Scheinberg. Global convergence rate analysis of unconstrained optimization methods based on probabilistic models. *Math. Program.* 169 (2018) [S014] | Template (b): the three-item process assumption (p. 8), the predictable-weight lemma (pp. 8–9) and the counting argument with 2p/(2p − 1)² (pp. 10–13); one theorem instantiated for four settings by computing C, h and F_ε (pp. 16–26) (T3; Heuristic 8). |

## Stage 3 · Expected complexity with random estimates (4–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 11 | Blanchet, Cartis, Menickelly, Scheinberg. Convergence rate analysis of a stochastic trust-region method via supermartingales. *INFORMS J. Optim.* 1(2) (2019) [S013] | **The most reusable tool for template (a).** The renewal-reward theorem E[T] ≤ p/(2p − 1)·Φ₀/(Θh(Δ_ε)) + 1 (pp. 5–9), Wald without proving T < ∞ first (pp. 8–9), "Choosing constants" before the proof (p. 14), and the order-mismatch diagnosis that forces a moment assumption in second order (p. 28) (T4). |
| 12 | Paquette, Scheinberg. A stochastic line search method with expected complexity analysis. *SIAM J. Optim.* 30 (2020) [S015; arXiv v1 read] | Transfer of T4 to backtracking Armijo by re-proving only the decrease assumption (pp. 7–8, 11); a second control for estimate variance (pp. 3–4); the Hölder trick for rare bad events (p. 6); sample-size rules in knowable quantities (p. 7) (T5). |
| 13 | Berahas, Cao, Scheinberg. Global convergence rate analysis of a generic line search algorithm with noise. *SIAM J. Optim.* 31 (2021) [S026] | Bounded, adversarial noise: the +2ε_f Armijo slack (p. 4), a damage budget r(ε_f)/h(ᾱ) ≤ γ < 1 that fixes the neighbourhood (pp. 7, 17–23), and the habit of zeroing the noise and probability parameters after each theorem (pp. 13, 20–23) (T6). |

## Stage 4 · High probability, noise, sample complexity (6–8 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 14 | Jin, Scheinberg, Xie. High probability complexity bounds for adaptive step search based on stochastic oracles. *SIAM J. Optim.* 34(3) (2024); conference version NeurIPS 2021 [D001 = S043; arXiv v5 read] | Template (c): a deterministic counting lemma plus Azuma–Hoeffding plus a Bernstein bound on the summed damage (pp. 7–13), with oracles whose constants the algorithm never sees (pp. 1–4). Also a model for experiments at equal work with split results reported as they are (pp. 26–28) (T7). |
| 15 | Cao, Berahas, Scheinberg. First- and second-order high probability complexity bounds for trust-region methods with noisy oracles. *Math. Program.* 207 (2024) [S041] | The minimal-repair pattern: a relaxed acceptance test and a cautious radius update (p. 11); a random radius threshold (p. 16); the adversarial oracle that probes how tight the noise floor is (pp. 30–33) (T8, Workflow H). |
| 16 | Jin, Scheinberg, Xie. High probability step size lower bound for adaptive stochastic optimization. OPT 2021 workshop [S137] | The enabling lemma on its own, in ten pages: the reflected-walk coupling (pp. 4–5, 8–9) and the design rule it implies for γ (pp. 4–5). |
| 17 | Jin, Scheinberg, Xie. Sample complexity analysis for adaptive optimization algorithms with stochastic oracles. *Math. Program.* 209 (2025) [S057] | How to turn iteration bounds into total-sample bounds (pp. 7–13) and how to fence a framework's scope (p. 2) (T9). |
| 18 | Scheinberg, Xie. Stochastic adaptive regularization method with cubics (WSC 2023) [S061] and First- and second-order stochastic adaptive regularization with cubics, *INFORMS J. Optim.* (2026), arXiv:2308.13161 [S093; arXiv v2 read] | The hypothesis-checklist import in its purest form (Heuristic 8): realization-wise lemmas, then a theorem whose items are exactly T7's hypotheses (S093 p. 10); the stopping-time shift (p. 10); sample complexity via S057 (pp. 17–18) (T10). |
| 19 | Scheinberg, Xie. Stochastic adaptive optimization with unreliable inputs. arXiv:2511.19411 (2025) [S083] | One framework for line search and trust region under corrupted gradients and heavy-tailed values; p < 1/2 through asymmetric step factors (p. 15); the tail of the bound follows the tail of the oracle (pp. 15–17) (T11). Probably the best entry point for new stochastic work. |

## Stage 5 · Estimators: meeting the contract (2–4 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 20 | Berahas, Cao, Choromanski, Scheinberg. Linear interpolation gives better gradients than Gaussian smoothing in derivative-free optimization. arXiv:1905.13043 (2019) [D003] | The short version of the comparison: one convergence condition, then the cost of each estimator to meet it (pp. 3, 7, 10); σ from the bias–noise trade-off (p. 7). |
| 21 | Berahas, Cao, Choromanski, Scheinberg. A theoretical and empirical comparison of gradient approximations in derivative-free optimization. *Found. Comput. Math.* 22 (2022) [S006] | Method 5 in full: N and σ per estimator (Table 1, p. 5), a necessity bound checked by simulation (pp. 16–18), estimator accuracy at trajectory points against the theorem's threshold (pp. 29–30), end-to-end data profiles (pp. 30–31). |
| 22 | Tran, Nguyen, Scheinberg. Finding optimal policy for queueing models: new parameterization. arXiv:2206.10073 (2022) [S073] | How to run a fair estimator comparison when each estimator usually comes bundled with its own algorithm: one estimator-agnostic outer method at equal per-iteration sample cost (pp. 6–7, 11). |

## Stage 6 · Composite, nonsmooth and new oracles (3–5 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 23 | Scheinberg, Goldfarb, Bai. Fast first-order methods for composite convex optimization with backtracking. *Found. Comput. Math.* (2014) [S028] | The deterministic stepping stone: full backtracking that lets FISTA's prox parameter grow (pp. 6–10), which the stochastic version later needs. |
| 24 | Nguyen, Scheinberg, Tran. Stochastic ISTA/FISTA adaptive step search algorithms for convex composite optimization. *J. Optim. Theory Appl.* 205 (2025) [S068] | Locating the property of an accelerated method that breaks under a stochastic oracle and repairing it with the authors' own deterministic variant (pp. 2, 14–15); a two-level proof: generic counting plus an algorithm-specific bound (pp. 7–20) (T12). |
| 25 | Baraldi, Javeed, Kouri, Scheinberg. ProxSTORM — a stochastic trust-region algorithm for nonsmooth optimization. arXiv:2510.03187 (2025) [S098] | Generalise and recover: STORM extended to f + φ and recovered when φ ≡ 0 (pp. 1–5); the contract on reduction differences and the half-step filtration (pp. 5–7); O(Δ^{-2}) samples under common random numbers (pp. 21–23); a deviation list for the experiments (p. 24) (T14). |
| 26 | Scheinberg, Xiong. Function-free optimization via comparison oracles. arXiv:2604.26867 (2026) [S087] | The newest direction: define the problem by what the oracle can distinguish (pp. 2–3, 10–11) and match every layer with a lower bound (pp. 24–26, 41–43) (T15). |

## Stage 7 · Powell-style complexity: the two arcs meet (3–4 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 27 | Chaudhry, Scheinberg. On complexity of model-based derivative-free methods. arXiv:2510.14935 (2025; ICM 2026 proceedings per the co-author's page) [S088] | Stage 1 algorithms analysed with Stage 2–4 tools: the criticality step replaced by the η₂ test (pp. 2–3), counting geometry steps (pp. 8, 12–13), an n-explicit error bound with a tightness example (pp. 9–12), random subspaces through a θ > 1/2 process (pp. 16–18) (T13). |
| 28 | Chaudhry, Scheinberg, Sun. Powell-style model-based derivative-free optimization with complexity guarantees. arXiv:2609.09441 (2026) [S104] | The certified-core-plus-reuse design (pp. 10–12), −log\|det Y\| as a potential (pp. 13–14), noisy subspaces with Δ_min (pp. 17–22), and the current benchmark protocol against NEWUOA on CUTEst (pp. 24–30). Read it alongside open-problems.md rows 1–2 and B14–B15. |

## Side reading · structured first-order methods (optional)

All read in full; useful when your problem has structure a first-order method can exploit (Method 6).

- Scheinberg, Ma, Goldfarb. Sparse inverse covariance selection via alternating linearization methods. NIPS 23 (2010). arXiv:1011.0097 [S010]: closed-form subproblems at gradient cost (pp. 5–6) and a skipping-step fallback to the analysable step (p. 4).
- Goldfarb, Ma, Scheinberg. Fast alternating linearization methods for minimizing the sum of two convex functions. *Math. Program.* (2013). arXiv:0912.4571 [S005]: complexity for alternating direction methods and reporting how often a safeguard fired (p. 19).
- Qin, Scheinberg, Goldfarb. Efficient block-coordinate descent algorithms for the group lasso. *Math. Program. Comput.* (2013) [S011]: exact block solves as trust-region subproblems (pp. 3–4) and counting the dominant unit of work (pp. 13–15).
- Scheinberg, Tang. Practical inexact proximal quasi-Newton method with global complexity analysis. *Math. Program.* 160 (2016). arXiv:1311.6547 [S029]: replacing a line search that has no rate by an analysable prox-parameter update, with the line search kept as an ablation (pp. 5–6, 24–27).

## Outside the syllabus (not read in full for this skill)

Useful context, but none of these was read in full here, so the notes are at abstract or title level. Verify before relying on them.

- Conn, Scheinberg, Vicente. *Introduction to Derivative-Free Optimization*. SIAM (2009) [S001; no open full text, abstract-level card]. The textbook treatment of Stage 1; the main reference of the DFO line.
- Talk: Scheinberg, "Stochastic Oracles and Where to Find Them", NeurIPS 2022 OPT workshop plenary (https://neurips.cc/virtual/2022/55786); also the Tutte Lecture (2024) and the Lehigh Schantz talk (2025); INFORMS 2021 version titled "Stochastic First Order Oracles…" (talk abstracts only; no transcript read).
- Moré, Wild. Benchmarking derivative-free optimization algorithms. *SIAM J. Optim.* 20(1), 172–191 (2009). *Not by Scheinberg.* The data-profile convention that the group's DFO papers use [cards S023, pp. 17–19; S041, pp. 33–36]. (Earlier versions of this file said the Optima 79 essay discusses these experiments; that discussion is in Nocedal's column in the same issue, not in her essay [card S143, p. 6].)
- Larson, Menickelly, Wild. Derivative-free optimization methods. *Acta Numerica* 28, 287–404 (2019). A map of the whole field, co-authored by a Scheinberg PhD graduate (Menickelly, Lehigh 2017). Use it to place your problem.
- Gratton, Royer, Vicente, Zhang. Complexity and global rates of trust-region methods based on probabilistic models. *IMA J. Numer. Anal.* 38(3) (2018). A parallel analysis (not Scheinberg's) credited as the source of the high-probability idea [card D001, p. 3]; comparing its technique with Stage 2–4 is a good exercise.
- Nguyen, Liu, Scheinberg, Takáč. SARAH. *ICML* 2017. arXiv:1703.00102 [S002; read in full, but outside the adaptive lens]. Shows that the group's ML side was not only adaptive methods: a new estimator with a constant, tuned step.
