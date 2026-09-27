# Technique catalog: transferable moves from Scheinberg's papers

> Date: 2026-09-27. Built from the full-text paper cards (`research/cards/`, index `research/07-paper-cards.md`) and the technique inventory of `research/08-deep-reading-synthesis.md` §7. Every row names the card and the page of the full text where the technique is used. Card ids resolve in `research/07-paper-cards.md` (and in the card key at the end of `SKILL.md`); S043 and D001 are one paper and are cited as D001.
>
> **How to use this file.** Find the row for the job you have (a lemma to prove, a safeguard to design, an experiment to run, a section to write), read the one-line "how to use it", then open the cited paper at the cited page before relying on it. The one-liners are summaries, not theorem statements: never copy a constant from here into a paper.
>
> **Scope.** Techniques only; reading notes that the cards record about typos or small inconsistencies inside papers are deliberately left out. Student-mode proof templates that combine several of these devices are in `proof-playbook.md`.
>
> **Card key (ids used in this file; full entries in `research/07-paper-cards.md`).** B001–B006 the open material of the 2009 IDFO book (Conn–Scheinberg–Vicente; batch `k01`): B001 table of contents, B002–B003 errata for the first and second printings (2015), B004 quadratic-regression addendum (2011), B005 review by J. L. Nazareth, B006 review by D. Orban (B001–B004 co-authored, B005–B006 the reviewers' voice); D001 Jin–Scheinberg–Xie 2024, high-probability step search (SIOPT; = S043, NeurIPS 2021); D003 Berahas–Cao–Choromanski–Scheinberg 2019, linear interpolation vs Gaussian smoothing; S002 SARAH 2017; S003 Fine–Scheinberg 2001, low-rank SVM training; S004 Conn–Scheinberg–Toint 1997, DFO survey; S005 Goldfarb–Ma–Scheinberg 2013, alternating linearization; S006 Berahas et al. 2022, gradient approximations (FoCM); S007 Conn–Scheinberg–Vicente 2009, fully linear TR framework; S008 Conn–Scheinberg–Toint 1997, DFO convergence (Powell volume); S009 SGD/Hogwild! 2018; S010 Scheinberg–Ma–Goldfarb 2010, sparse inverse covariance; S011 Qin–Scheinberg–Goldfarb 2013, group-lasso BCD; S012 Chen–Menickelly–Scheinberg 2018, STORM; S013 Blanchet–Cartis–Menickelly–Scheinberg 2019, STORM rates via supermartingales; S014 Cartis–Scheinberg 2018, probabilistic models rates; S015 Paquette–Scheinberg 2020, stochastic line search; S016 Conn–Scheinberg–Vicente 2008, interpolation geometry; S018 Bandeira–Scheinberg–Vicente 2014, probabilistic-model TR (BSV); S019 Conn–Scheinberg–Toint 1998, DFO in practice; S022 Scheinberg 2006, active-set SVM (sole author); S023 Zhang–Conn–Scheinberg 2010, DFLS; S024 SARAH nonconvex 2017; S025 Conn–Scheinberg–Vicente 2008, regression and underdetermined geometry; S026 Berahas–Cao–Scheinberg 2021, line search with noise; S028 Scheinberg–Goldfarb–Bai 2014, FISTA with backtracking; S029 Scheinberg–Tang 2016, inexact proximal quasi-Newton; S030 Scheinberg–Toint 2010, self-correcting geometry; S031 Curtis–Scheinberg 2017, ML optimization tutorial; S032 SG convergence aspects 2019; S033 Bandeira–Scheinberg–Vicente 2012, sparse interpolation; S035 Wen–Goldfarb–Scheinberg 2012, BCD for SDP; S036 Curtis–Scheinberg–Shi 2019, TR with step normalization; S037 inexact SARAH 2021; S041 Cao–Berahas–Scheinberg 2024, noisy TR high probability; S043 = D001; S047 Curtis–Scheinberg 2020, adaptive stochastic optimization overview; S048 Wen et al. 2009, row-by-row SDP; S049 Scheinberg–Rish 2009, SINCO; S050 Goldfarb–Scheinberg 2004, product-form Cholesky (LP); S052 Ghanbari–Scheinberg 2017, black-box ML tuning with DFO-TR; S054 Ghanbari–Scheinberg 2018, proximal quasi-Newton rates; S055 Tran–Scheinberg–Nguyen 2022, accelerated shuffling; S057 Jin–Scheinberg–Xie 2025, sample complexity; S058 Goldfarb–Scheinberg 2005, product-form Cholesky (SOCP); S061 Scheinberg–Xie 2023, SARC (WSC); S063 Nguyen et al. 2018, "When does stochastic gradient algorithm work well?"; S068 Nguyen–Scheinberg–Tran 2025, stochastic ISTA/FISTA; S072 Conn–Scheinberg–Vicente 2003, interpolation error and poisedness; S073 Tran–Nguyen–Scheinberg 2022, queueing policies; S083 Scheinberg–Xie 2025, unreliable inputs; S084 Tang–Scheinberg 2013, quasi-Newton proximal (NIPS); S087 Scheinberg–Xiong 2026, comparison oracles; S088 Chaudhry–Scheinberg 2025, complexity of model-based DFO; S089 Ghanbari–Li–Scheinberg 2019, zero-one loss; S093 Scheinberg–Xie 2026, SARC (INFORMS J. Optim.); S098 Baraldi–Javeed–Kouri–Scheinberg 2025, ProxSTORM; S100 Tang–Scheinberg 2013, second-order information for ℓ1; S104 Chaudhry–Scheinberg–Sun 2026, Powell-style DFO with complexity; S133 DFO v1.2 manual 2000 (v2.0 substitute); S137 Jin–Scheinberg–Xie 2021, step-size lower bound (OPT workshop); S143 Scheinberg 2009, Optima 79 essay.

---

## 1. Proof devices

### 1.1 Model quality and interpolation geometry (deterministic DFO)

| # | Device | How to use it | Where |
|---|---|---|---|
| P1 | Interpolation error bound by Taylor subtraction | Subtract the interpolation equations from Taylor expansions, cancel the unknown function error through the centre point, and invert a scaled matrix that does not depend on x. | [cards S072, p. 8; S016, pp. 12–17] |
| P2 | Function-error to gradient-error transfer | Get a gradient-error bound from a function-value bound with a Taylor step h = δ(∇f − g)/‖∇f − g‖. | [card S008, pp. 12–13] |
| P3 | Norm equivalence on the unit ball | Scale the sample set to the unit ball, prove max_{B(1)}\|vᵀφ(x)\| ≥ σ‖v‖, and compute the constants by restricting to one or two variables; this lets you measure poisedness with a condition number. | [cards S016, pp. 8–10; S025, pp. 11–13; S072, pp. 17–18] |
| P4 | Greedy construction of a well-poised set | Build or repair a set by argmax or threshold pivoting on Lagrange/Newton polynomials, with a lemma that a replacement point always exists. | [cards S008, pp. 10–11; S016, pp. 19–23; S072, pp. 28–29] |
| P5 | Small ball to larger ball | Show that accuracy on a small ball implies accuracy on a larger ball with the same constants (integral mean value), so the model class is stable under radius changes. | [card S007, pp. 9–10] |
| P6 | Potential for counting geometry swaps | Find a bounded quantity each swap multiplies by a factor > 1 (simplex volume / \|ℓ_j\|), or count a growing orthogonal set (≤ 3n calls), or a Hadamard volume ratio (O(p log p)), or −log\|det Y\| contracting by (1 − 1/n) (Cramer's rule + AM–GM). | [cards S030, p. 6; S088, pp. 8, 12–13; S104, pp. 13–14] |
| P7 | Self-correction lemma | Read the error bound backwards: a failed step means a large model error; with Σℓ_j = 1 this forces a point with \|ℓ_j(x⁺)\| > Λ, so the rejected trial point is an improving swap at no extra evaluation. | [cards S030, pp. 14–15; S143, p. 4] |
| P32 | trace(A) + trace(A⁻¹) bound | Bound ‖A‖ through tr(A) + tr(A⁻¹) ≤ n(Λ² + 1) and λ + 1/λ ≥ 2 instead of multiplying by n; with Λ = 1 + O(1/n) the gradient-error factor is O(√n). Track every constant's n-dependence. | [cards S088, pp. 9–10; S104, pp. 7–10] |
| P36 | Least-squares model error by pseudo-inverse and scaling | Write the coefficient error of a regression model as M† × (Taylor residual); factor the radius out with the diagonal scaling M† = diag(1, (1/Δ)I, (1/Δ²)I) M̂†, so the geometry enters only as ‖M̂†‖ of the scaled set; bound each block, then move from the centre to the ball with one mean-value step. Gives Hessian, gradient and value errors of order Δ, Δ², Δ³ with the factors n^{1/2} and p̄^{1/2} kept explicit (co-authored book addendum; the linear case is the re-proved Theorem 2.13). | [cards B004, pp. 1–2; B002, pp. 1–2] |
| P33 | Hand-checkable 2-D counterexample | Show a safeguard is necessary with a 2-D run whose iterates can be computed by hand, check non-stationarity at the limit by differentiation, and argue that the outcome does not depend on any replacement rule. | [cards S143, pp. 4–5; S030, pp. 8–11] |

### 1.2 Trust-region and step-search skeletons

| # | Device | How to use it | Where |
|---|---|---|---|
| P8 | Trust-region skeleton | Criticality loop is finite; radius bounded below away from criticality; key lemma \|ρ − 1\| ≤ model error / predicted decrease, so success once Δ ≤ c‖g‖; count successful steps by decrease, unsuccessful ones by successful ones plus a log term. | [cards S008, pp. 16–19; S007, pp. 15–18; S023, pp. 13–15; S088, pp. 3–4; S104, pp. 5–6] |
| P9 | Acceptance test replacing the criticality step | Accept (and enlarge Δ) only if ρ_k ≥ η₁ and ‖g_k‖ ≥ η₂Δ_k; the radius then controls both step length and model accuracy, and no iteration needs a certified model. | [cards S018, p. 8; S013, pp. 10, 12; S088, pp. 2–3; S104, p. 4] |
| P17 | Noise slack and damage budget | Relax the sufficient-decrease test by r = 2ε_f; put all noise damage in one function r(ε_f) and require r/h(ᾱ) ≤ γ < 1, which fixes the reachable neighbourhood for each function class. | [cards S026, pp. 7, 15–17; D003, pp. 3–4; S041, p. 11] |
| P20 | One inequality, three function classes | Choose the progress measure per class (f(x₀) − f(x_k); 1/(f − f*); log(1/(f − f*)), or stopped transforms with Jensen) so that one nonconvex decrease inequality gives nonconvex, convex and strongly convex rates. | [cards S014, p. 7; S015, pp. 19–22; S026, p. 7; D001, pp. 6, 19–20] |

### 1.3 Stochastic process: almost-sure and expected complexity

| # | Device | How to use it | Where |
|---|---|---|---|
| P10 | Realization-wise safety + probabilistic progress | Prove the safety property (Δ_k → 0) on every sample path without probability, then show log Δ_k dominates a ±1 submartingale walk counting good iterations; together they contradict a gradient bounded away from zero. | [cards S018, pp. 8–11; S012, pp. 21–22; S098, pp. 17–19] |
| P11 | Joint potential with a case grid | Φ_k = νf + (1 − ν)Δ^q with q the order of the per-step decrease (2 first order, 3 second order); split on ‖∇f‖ ≥ ζδ_k × (I_k, J_k); choose ν near 1 so every case but "both bad" is no worse than an unsuccessful step; offset the worst case with the best case of weight αβ. | [cards S012, pp. 14–20; S013, pp. 14–18; S015, p. 11; S047, pp. 4–6, 10; S098, pp. 13–15] |
| P12 | Renewal-reward stopping time | Check three assumptions (step parameter capped; below Δ_ε it moves like min(Δe^{λW}, Δ_ε) with P(W = +1) ≥ p > 1/2; E[ΔΦ] ≤ −Θh(Δ_k)) and read off E[T] ≤ p/(2p − 1)·Φ₀/(Θh(Δ_ε)) + 1; Wald's identity for nonnegative increments avoids proving T < ∞ first. | [cards S013, pp. 5–9; S047, p. 8; S098, pp. 19–20] |
| P13 | Counting lemmas with a predictable-weight bound | Split iterations into true/false × successful/unsuccessful × step above/below a threshold C; use E[Σ W_k I_k] ≥ p·E[Σ W_k] for W_k fixed by the past; get E[N_ε] ≤ 2p/(2p − 1)²·(2F_ε/h(C) + log_γ(C/α₀)). | [cards S014, pp. 8–13; S026, pp. 8–13; S068, pp. 7–9] |
| P18 | Hölder for rare unbounded errors | Bound the bad-event contribution by E[1_bad·\|err\|] ≤ P(bad)^{1/2}·(second-moment bound)^{1/2}, so it is small when P(bad) is small even though the error is unbounded. | [card S015, p. 6] |
| P19 | Order-mismatch diagnosis | If a bad case can raise f by O(δ²) while a good step only guarantees O(δ³), a probability-only contract cannot work; add an expectation bound of the matching order on estimate errors. | [card S013, p. 28] |
| P23 | Half-step filtration and difference-based estimates | Condition the model and the computed reduction on separate σ-algebras (F_{k−1}, F_{k−1/2}) so their probabilities multiply; with common random numbers, Taylor + Markov give N = O(Δ^{-2}) samples for the reduction difference. | [card S098, pp. 5–7, 21–23] |

### 1.4 High probability and sample complexity

| # | Device | How to use it | Where |
|---|---|---|---|
| P14 | High-probability template | (1) Azuma–Hoeffding on the submartingale Σ I_k − pt; (2) a deterministic lemma: not stopped and enough true iterations ⇒ enough good iterations; (3) a concentration bound on the summed damage (Bernstein via conditional MGFs; Fuk–Nagaev for q-th moments; Chebyshev; Hoeffding for bounded corruption); intersect and invert through a monotone function of ε. No joint potential needed. | [cards D001, pp. 7–13; S041, pp. 16–23; S083, pp. 11–17] |
| P14b | Random threshold from the horizon | When the step threshold depends on the unknown minimum gradient norm, define it as a random variable over the horizon instead of fixing ε in advance. | [card S041, p. 16] |
| P15 | Hypothesis-checklist theorem | Prove realization-wise lemmas for the new method, then state one theorem whose items are exactly the published framework's hypotheses (one-line gloss each) and import its tail bound unchanged. | [cards S093, p. 10; S061, p. 10; S015, pp. 7–8] |
| P16 | Step-parameter lower bound | Map log_{1/γ}(ᾱ/α_k) to an integer walk, dominate it by a one-sided reflected walk (coupling), bound the walk's maximum over n steps from its explicit spectrum with level ℓ ≍ log n; then total cost ≤ n·oc(α*(n)), and a layer-cake sum gives the expected cost. | [cards S137, pp. 4–5, 8–9; S057, pp. 9–13; S093, pp. 17–18] |
| P31 | Random subspaces well aligned with probability > 1/2 | Use the Beta(q/2, (n − q)/2) law of the Haar projection and Paley–Zygmund to show P(well aligned) ≥ 243/443 > 1/2, then plug into a θ > 1/2 process argument. | [cards S088, pp. 16–18; S104, p. 20] |

### 1.5 Gradient estimators and sampling

| # | Device | How to use it | Where |
|---|---|---|---|
| P21 | Sampling radius from a bias–noise trade-off | Write the estimator error as aσ + b/σ, pick σ at the minimizer (independent of the unknown ‖∇φ‖); the existence condition of the inequality is the gradient-norm floor. | [cards D003, p. 7; S006, pp. 6–7; D001, p. 25] |
| P22 | Estimator variance and necessity | Bound the variance with Gaussian moment identities and Chebyshev (or matrix Bernstein when summands are bounded, giving log(1/δ)); for necessity apply a second-moment tail lower bound to a linear test function, then simulate to see how loose it is. | [cards S006, pp. 11–21; D003, pp. 9–10] |
| P22b | Error-budget split | Split a relative error budget λ/(1 − λ) between deterministic bias and sampling error, and tune λ (e.g. 1/(3√n)) so the sample count keeps the right order in n. | [card S006, p. 14] |

### 1.6 First-order, composite and inexact methods

| # | Device | How to use it | Where |
|---|---|---|---|
| P24 | Three-point inequality with skipping steps | Telescope a three-point inequality while counting only the non-skipping steps; use a mode-dependent potential when the method alternates. | [cards S010, pp. 10–11; S005, pp. 8–14] |
| P25 | FISTA potential with a varying prox parameter | Keep FISTA's key inequality while the prox parameter changes (θ_k bookkeeping), and prove μ_k t_k² ≥ (Σ√μ_i/2)² by induction; use a potential that is constant on unsuccessful steps. | [cards S028, pp. 6–10; S054, pp. 19–21; S068, pp. 15–17] |
| P26 | Inexact subproblem solves | Use an error-dominated vs progress dichotomy, a last-good-solve geometric weighting, or error accumulation ρ^k Σ ε_i/ρ^i to carry a rate through inexact inner solves. | [cards S029, pp. 13–19; S054, p. 11; S068, pp. 10, 19–20] |
| P28 | Convergence by embedding | Map each new step into an existing convergent framework with an explicit parameter correspondence (e.g. block steps into Tseng–Yun BCGD; a safeguard read as a barrier parameter). | [cards S011, pp. 9–10; S048, pp. 7–8] |
| P29 | Second-moment bound from per-sample smoothness | Derive E‖∇f(x; ξ)‖² bounds from per-sample smoothness instead of assuming bounded gradients, which fail for strongly convex f. | [cards S009, pp. 4, 10; S032, pp. 21–22; S063, p. 13] |
| P30 | Recursive-estimator MSE telescoping | Telescope the mean squared error of a recursive gradient estimator through the conditional unbiasedness of its increments. | [cards S002, pp. 5, 11; S037, p. 10; S024, pp. 12–13] |
| P34 | Perturbation sandwich for approximate QPs | Bound the optimal-value change of a QP with an approximated matrix on the same feasible set by a sandwich, independent of how the approximation was built. | [card S003, pp. 14–15] |
| P35 | Prox-gradient map is Lipschitz | Prove from nonexpansiveness that h(x) is (2/r + L)-Lipschitz, so the smooth liminf-to-lim argument carries over to composite problems. | [card S098, pp. 29–30] |

### 1.7 Numerical linear algebra inside interior-point methods

| # | Device | How to use it | Where |
|---|---|---|---|
| P27 | Smallest-bad-index contradiction | Prove uniform boundedness of factors as the duality gap → 0 by contradiction on the smallest index where boundedness fails along a subsequence. | [cards S050, pp. 11–14; S058, pp. 19–20] |

---

## 2. Algorithm-design moves

### 2.1 Model-based DFO and geometry

| # | Move | How to use it | Where |
|---|---|---|---|
| A1 | Gate radius decrease on a certificate | Do not shrink the radius after a failed step until the model's geometry is certified adequate. | [cards S008, pp. 14, 17; S007, pp. 13–14; S023, p. 9] |
| A2 | Recycle rejected trial points | Use an unsuccessful trial point to replace a far point or a point with \|ℓ_j(x⁺)\| > Λ before shrinking the radius. | [cards S030, p. 12; S143, pp. 4–5; S104, pp. 10, 12] |
| A3 | Certified core plus reuse pool | Certify n points (Y) with linear Lagrange polynomials; fit the other evaluated points (Z) by least squares with a bounded Hessian. | [card S104, pp. 10–12] |
| A4 | Per-residual models on one sample set | For least squares, model each residual on a shared sample set; switch the model Hessian between Gauss–Newton, Levenberg–Marquardt and full second order by regime. | [card S023, pp. 2, 5, 16–17] |
| A5 | Constraint classes by information and cost | Keep cheap constraints exact in the subproblem; treat hidden constraints through a failure flag, not a large function value. | [cards S019, pp. 3, 6–8; S133, p. 1 (v2.0 manual)] |
| A19 | Powell-style methods in random subspaces | Run the model-based method in Haar-random q-dimensional subspaces; redraw only on radius-changing iterations; impose Δ_min with noise. | [cards S088, pp. 13–19; S104, pp. 17–22] |
| A20 | Hedge model switching | Switch between minimum-Frobenius-norm and minimum-change models by an exponentially weighted average of relative prediction error at the trial point; give the component to every solver in the comparison. | [card S104, pp. 25–27] |

### 2.2 Noisy and stochastic oracles

| # | Move | How to use it | Where |
|---|---|---|---|
| A6 | Relaxed acceptance + cautious radius | Add r = 2ε_f to the numerator of ρ_k (or to the Armijo test); grow the radius only if ‖g_k‖ ≥ η₂Δ_k. | [cards S041, p. 11; S026, pp. 4–5; S083, p. 8] |
| A7 | A second control for estimate accuracy | When ‖∇f‖ is unknown, add a control δ_k with its own "reliable step" update that sets the variance of the function estimates. | [cards S015, pp. 3–4; S047, p. 11] |
| A8 | Fresh estimates, no averaging under biased failures | Draw new estimates at the current and trial points every iteration, independent of the model data; do not average when failures are biased. | [card S012, pp. 7, 26, 28] |
| A9 | Floor-plus-cap oracle | Ask the first-order oracle for max{ε_g, min{τ, κα}‖g‖}: the floor models the sampling limit, the cap removes the need for a step-size bound. | [card D001, pp. 1–3] |
| A10 | Asymmetric step-size update | Make γ_inc > γ_dec so that p·ln γ_inc + (1 − p)·ln γ_dec > 0 holds for a conservative p, which tolerates p < 1/2. | [card S083, pp. 15, 22] |
| A10b | Gate step increases on small gradients | Block step-size increases when ‖g_k‖ < ε_rej (tied to the oracle bias), so noise-driven steps are not rewarded. | [card S083, pp. 8–9] |
| A18 | Sample sizes in knowable quantities | Set sample sizes from α_k, ‖g_k‖, Δ_k and variance bounds, with a guess-and-increase loop when ‖g_k‖ is needed. | [cards S015, p. 7; S047, p. 9; S013, pp. 19–20] |
| A21 | Accuracy inputs scaled to the adaptive parameter by derivative order | In cubic regularization ask for gradient accuracy ∝ μ/σ_k and Hessian accuracy ∝ √(μ/σ_k), matching what the Taylor model needs. | [card S093, pp. 4–5, 11] |

### 2.3 Composite, first-order and second-order methods

| # | Move | How to use it | Where |
|---|---|---|---|
| A11 | Keep the known part exact | For f + φ, keep φ exact in the subproblem and in ared/pred; sample only f. | [cards S098, pp. 2, 4, 7; S068, pp. 1, 4] |
| A12 | Full backtracking that lets the prox parameter grow | Use θ_k bookkeeping (FISTA-BKTR) so the step may increase; the stochastic version needs this. | [cards S028, pp. 8–9; S068, pp. 5, 14–15] |
| A13 | Replace a rate-less line search by an analysable update | Swap a practical line search for a trust-region-like prox-parameter update with a sufficient-decrease test, and keep the line search as an ablation. | [cards S029, pp. 5–6, 24–25; S084, pp. 3–4] |
| A14 | Cheap test, provable fallback | Use a cheap practical test and fall back to the analysable step only when it fails (skipping step; threshold pivoting with argmax as last resort). | [cards S010, p. 4; S005, pp. 7–8; S008, p. 11] |
| A15 | Compact L-BFGS with cached products | Keep a compact L-BFGS representation with cached Q̂d so each coordinate step costs O(m). | [cards S084, p. 3; S100, p. 8] |
| A16 | Block subproblem as a trust-region subproblem | Solve each block exactly by the secular equation with Newton's method and a cached eigendecomposition. | [card S011, pp. 3–4] |
| A17 | PSD block via Schur complement | In block coordinate descent for SDP, write the PSD block as a second-order cone constraint via the Schur complement; exploit closed-form rank-two determinants. | [cards S048, pp. 3–4; S049, pp. 7–8] |

---

## 3. Experiment protocols

### 3.1 DFO benchmarking (the group's published protocol)

| # | Protocol | How to use it | Where |
|---|---|---|---|
| E1 | Moré–Wild set with data profiles | 53 problems, data profiles with budgets in simplex gradients (evaluations/(n+1)), τ = 10⁻¹…10⁻⁷, deterministic noise, solver tolerances matched to the noise. | [cards S023, pp. 17–19; S041, pp. 33–36; S006, pp. 30–31] |
| E2 | Powell-family baseline and rotations | Function-evaluation performance/data profiles against NEWUOA (via PRIMA) or another Powell code; the same generic component for all solvers; average over random rotations of the initial set; let the budget end every run; report failures. | [cards S033, pp. 25–26; S104, pp. 26–30; S012, pp. 27–29] |
| E14 | Restarts and failed evaluations | Use restarts that differ only in one random initial sample, and count failed evaluations in the budget. | [card S019, pp. 10–11] |

### 3.2 Estimators and equal-work comparisons

| # | Protocol | How to use it | Where |
|---|---|---|---|
| E3 | Equal-accuracy stop in the dominant unit | Stop every method at the same accuracy against a common reference and count the dominant unit of work (matrix-vector products, inner products, network passes). | [cards S011, pp. 13–15; S028, p. 17; D001, p. 27; S100, pp. 10–11] |
| E4 | Estimator accuracy at trajectory points | Evaluate estimators at points harvested from optimization trajectories and report the fraction meeting the theorem's threshold (θ < 1/2), not just the mean error. | [cards S006, pp. 29–30; D003, pp. 10–11] |
| E6 | Estimator-agnostic outer method as harness | Put every estimator inside one outer method that is robust to the estimator, at equal per-iteration sample budgets. | [card S073, pp. 6–7, 11] |
| E7 | Baseline at its best | Run the baseline at its best configuration, at its own and at your tolerance, with memory matched; repeat the largest runs independently. | [cards S003, pp. 15–17; S022, pp. 10–13, 16] |
| E11 | Random search at twice the budget | Include random search at 2× the evaluation budget as a sanity baseline; report optimizer overhead separately from evaluation cost. | [card S052, pp. 6–7] |

### 3.3 Theory-versus-practice probes

| # | Protocol | How to use it | Where |
|---|---|---|---|
| E5 | Threshold sweep, adversarial oracle, extremal simulation | Sweep the success probability across the theoretical threshold on a toy problem; build a worst-case oracle inside the contract with Bernoulli(p) flags and compare the plateau with the noise floor; simulate the extremal instance when the lower bound is weak. | [cards S012, pp. 30–32; S041, pp. 30–33; S006, pp. 16–18] |
| E8 | One-violation baseline; assumption-violating competitor | Build a baseline variant that removes one violation of your assumptions, and include a competitor that violates your assumption to show what it buys. | [cards S012, p. 28; S137, p. 6] |
| E9 | Noise slack estimated online, with zero ablation | Estimate the noise slack from repeated oracle calls (e.g. 1/5 of the standard deviation of 30 calls, re-estimated each epoch) and include the zero-slack run. | [card D001, p. 26] |
| E10 | Seeded realizations with histograms | Run 100 seeded realizations and plot histograms against a same-seed, work-adjusted baseline; say where the baseline wins. | [card S098, p. 24] |
| E12 | Measure the new assumption on data | When a paper introduces an assumption (e.g. a growth condition), measure it directly on standard data sets. | [cards S063, pp. 8–11; S089, pp. 8–9] |
| E13 | Report how often each safeguard fired | Log and report the frequency of every safeguard or fallback branch. | [cards S005, p. 19; S036, pp. 19–23] |
| E15 | Sweep multiples of a theory-prescribed parameter | Run the practical code at {0, 1, 2, 4, 8}× the theoretical value and compare the best multiple with the theory. | [card S041, pp. 33–36] |

---

## 4. Writing moves

### 4.1 Framing and positioning

| # | Move | How to use it | Where |
|---|---|---|---|
| W1 | Necessity and minimal sufficiency in one sentence | Write the contribution as "X is necessary for G; however, X is not needed unless Y". | [cards S143, p. 4; S030, pp. 3–4] |
| W2 | History along one design axis | Tell the field's history along one axis so each earlier method is both a success and a failure on it; write related work as a ledger of deficits; list practitioners' alternatives with their failure modes. | [cards S143, pp. 1–2; S010, p. 2; S004, pp. 3–4] |
| W3 | Credit, then test | Credit a competitor's encouraging results before showing, by a counterexample, where its method can fail (the 2009 essay: a geometry-free method that can converge to a non-stationary point); concede a concurrent paper's advantage and say why you do not compare. | [cards S143, p. 4; S012, pp. 5–6] |
| W4 | Objective stated as understanding | When there are no experiments, say the objective is understanding rather than a new practical scheme. | [card S030, p. 4] |
| W8 | Glossary across communities | Add a table mapping the terms of two communities (ML and OR, approximation theory and optimization). | [cards S031, p. 2; S003, pp. 3–4] |
| W15 | Open with a toy or two-regime example | Show the phenomenon on a toy or two-regime example before the theory. | [cards S063, pp. 2–3; S055, p. 4; S002, p. 4] |
| W16 | One oracle language for all prior work | Restate every prior paper, including your own, as a choice in one oracle definition (e.g. a set on the accuracy–probability plane), and write one contribution bullet per closest competitor, saying where your assumption is stronger. | [cards S041, pp. 2–7; D001, pp. 2–3] |

### 4.2 Presenting results

| # | Move | How to use it | Where |
|---|---|---|---|
| W5 | "Choosing constants" before the proof | Explain which parameter trades against which before the heavy proof; give a table of constants with one remark per constant. | [cards S013, p. 14; S098, pp. 15–16] |
| W6 | Zero-parameter remark | After each theorem, set the noise and probability parameters to zero and show the deterministic bound returns; compare constants with the classical method. | [cards S026, pp. 13, 20, 22–23; S005, pp. 11, 16] |
| W7 | Complexity table with an assumption column | Compare methods in one table with a common complexity measure and an "additional assumptions" column; put the full comparison table in the introduction. | [cards S031, p. 13; S037, p. 4; S055, p. 3; S006, p. 5] |
| W9 | Gloss each axiom | Follow each item of an abstract process assumption with a one-line plain-language gloss. | [cards D001, p. 7; S093, p. 10] |
| W11 | Requirement-to-theorem map | Add a remark mapping each algorithmic requirement to the theorem that uses it. | [card S007, p. 21] |
| W12 | Intuition around the key lemma | Put a plain-language paragraph after the key lemma, and design remarks between a theorem's statement and its proof. | [cards S030, p. 15; S008, pp. 17, 19; S057, pp. 8–9] |
| W17 | Split a messy bound into parts | After a complicated tail bound, rewrite it as the optimal-order term, the initial-adjustment term and the noise floor, one sentence each. | [card S041, p. 21] |

### 4.3 Honesty and scope

| # | Move | How to use it | Where |
|---|---|---|---|
| W10 | Fence the scope | List the impractical members of your abstraction, the methods it does not cover and why, and where the method should not be used. | [cards S007, p. 8; S057, p. 2; S035, p. 2] |
| W13 | Numbered findings, negatives included | State numbered findings, negative ones included, before the plots; give 2–3 falsifiable experiment aims. | [cards S104, pp. 26–27; S029, pp. 23–24] |
| W14 | Open problems with the exact blocker | State each open problem with the inequality or technical obstacle that blocks it. | [cards S047, p. 12; S018, pp. 20–21] |
| W18 | Deviation list | List every place the implementation departs from the theory's assumptions, each with its reason. | [cards S098, p. 24; S104, p. 27; D001, p. 26] |
| W19 | Discuss a strong extra assumption by name | After a result that needs a strong assumption, add a named paragraph computing the sample cost it implies and saying plainly whether optimality is known. | [card S068, p. 13] |

### 4.4 Book-level organisation and public correction (the 2009 IDFO book; co-authored)

From the book's table of contents (title level; the chapters were not read), its errata and addendum, and one reviewer's reading. Co-authored with Conn and Vicente, so none of these is credited to Scheinberg alone.

| # | Move | How to use it | Where |
|---|---|---|---|
| W20 | Itemised, dated errata that say when the original statement holds | Keep one dated errata list per printing: page and line, old text, corrected text; for a theorem, give the new proof sketch and constants and state the condition under which the printed statement is still valid; replace "it is then obvious" with a pointer to the argument; fix a wrong number at its source instead of adding a sentence that reconciles it; repeat an item if a later printing still carries it; credit the readers who found errors; publish an omitted derivation as a short dated note next to the errata. | [cards B002, pp. 1–3; B003, p. 1; B004, p. 1] |
| W21 | Toolkit first | Collect the analytical machinery every method needs (sample-set geometry, model-error bounds) in one part, and present each algorithm family as a user of it. | [card B001, pp. 1–2] |
| W22 | Framework and its conditions before the instances | State the algorithmic framework and the conditions its models must satisfy first, then the concrete methods that satisfy them. | [card B001, p. 3] |
| W23 | One section skeleton for parallel variants | Give parallel variants (e.g. interpolation and regression models) the same sequence of sections, so the reader sees exactly what changes. | [card B001, p. 1] |
| W24 | Limitations and the classical comparison, stated early | Put a section on the limitations of the whole approach in the introduction, and state the similarities and differences with the classical method the new one adapts (a reviewer valued the stated limitations of both method families and the stated similarities and differences with classical trust region; the section on limitations is table-of-contents evidence). | [cards B001, p. 1; B006, pp. 1–2] |

Two criticisms shared by both reviewers are cheap to avoid in a thesis or monograph: exercises that only extend the theory, and too few worked numerical examples or bare-bones implementations [cards B005, pp. 2–3; B006, p. 2].

---

## 5. Single-paper devices worth knowing

These appear in one paper only, so they are not promoted to heuristics in `SKILL.md`; they are still useful tools.

| Device | How to use it | Where |
|---|---|---|
| Oracle-side fix for an algorithm-side safeguard | If a stronger theorem seems to need an algorithmic cap, check whether a mild extra oracle condition (a finite τ) removes it. | [card D001, p. 3] |
| Randomness-free safeguard iterations | Keep geometry-fixing iterations free of new random draws so they can be counted deterministically. | [card S088, p. 18] |
| Avoid verify-until-pass loops | Under probabilistic conditions, deterministic inexactness loops amplify the chance of an erroneous exit; design stochastic tests differently. | [card S098, p. 28] |
| Budget-exhaustion certificate | Give an adaptive inner loop a budget equal to its high-probability cost in the good regime; exhausting it certifies, with probability 1 − δ, that you are near-stationary. | [card S087, pp. 35, 40] |
| Invariance test before choosing a measure | List the transformations the oracle cannot see and discard optimality measures that are not invariant under them. | [card S087, pp. 2–3, 10–11] |
| Analysis-only trade-off knob | Keep a parameter that is not algorithmic but trades the allowed failure probability against the neighbourhood size. | [card S026, pp. 8, 13] |
| Method-agnostic guarantee for an approximation step | State the approximation guarantee so it holds regardless of how the approximation is computed. | [card S003, p. 1] |
| Counterexamples separating result types | When your result type (expected hitting time) differs from the literature's (expected gap), show by toy examples that neither implies the other. | [card S068, pp. 25–26] |
