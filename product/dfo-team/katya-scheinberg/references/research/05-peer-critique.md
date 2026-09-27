# 05 · Peer critique, limits, competing approaches

> Research date: 2026-09-27. No published critique *of* Scheinberg's work (comment paper, failed replication, public review) was found in the searches that could be run. This file therefore records (a) limits visible in Scheinberg's own later papers, (b) methodological positions Scheinberg's papers take against competing practice, and (c) third-party follow-ups whose titles indicate where the framework was extended — authors of those follow-ups are **unverified** (⚠️) and they are not cited as fact about who did what.

## 1. Limits made visible by Scheinberg's own later work (primary, self-critique by progression)

| Earlier assumption | Later relaxation | Reading |
|---|---|---|
| Exact function values; only models random (BSV 2014, arXiv:1304.2808) | Function estimates random too (STORM, Math. Program. 2018, https://doi.org/10.1007/s10107-017-1141-8) | The 2014 setting did not cover sampled objectives. |
| Almost-sure convergence (STORM 2018) | Expected complexity (Blanchet et al. 2019) → high-probability tail bounds (Jin–Scheinberg–Xie 2024, https://doi.org/10.1137/22M1512764; Cao–Berahas–Scheinberg 2024, https://doi.org/10.1007/s10107-023-01999-5) | Almost-sure/expected results were judged insufficient for practice where one run matters. |
| Unbiased / well-behaved oracles | Biased oracles (Jin–Scheinberg–Xie 2024); oracles "not assumed to be unbiased or consistent" (Cao–Berahas–Scheinberg 2024); arbitrarily corrupted gradients and heavy-tailed function noise (arXiv:2511.19411, 2025) | Earlier noise models were too optimistic for real stochastic and zeroth-order settings. |
| Geometry steps as used in IDFO-era algorithms | Geometry steps confined to the final stage (Scheinberg–Toint 2010, https://doi.org/10.1137/090748536); random subspaces (arXiv:2510.14935; arXiv:2609.09441) | Cost of geometry maintenance was a recognised practical weakness of model-based DFO. |

## 2. Positions Scheinberg's papers take against competing practice (primary framing, my reading)

- **Against "Gaussian smoothing by default" in ML zeroth-order work.** FoCM 2022 (https://doi.org/10.1007/s10208-021-09513-z) compares smoothing estimators with finite differences and linear interpolation on equal footing (sample counts and radius). A companion preprint title, "Linear interpolation gives better gradients than Gaussian smoothing in derivative-free optimization" (arXiv:1905.13043, authors ⚠️ unverified), states the headline position.
- **Against pre-specified step-size schedules (SGD practice).** Jin–Scheinberg–Xie 2024 foreground that step sizes adapt to estimated progress rather than following a schedule.
- **Against the view that model-based DFO lacks competitive worst-case guarantees.** Chaudhry–Scheinberg 2025 (arXiv:2510.14935) states these methods "can have the same worst case complexity as any other known DFO method" (snippet wording). *Inference:* aimed at the comparison with direct-search and finite-difference methods whose complexity theory matured earlier.
- **Against "geometry-free" model-based practice without guarantees.** Scheinberg–Toint 2010 proves geometry steps cannot be completely eliminated for global convergence.

## 3. Third-party extensions / competing lines (⚠️ authors unverified; title + ID seen in search results)

| Title (as seen) | ID | What it signals |
|---|---|---|
| ProxSTORM — A Stochastic Trust-Region Algorithm for Nonsmooth Optimization | arXiv:2510.03187 | STORM's smoothness assumption is a limit; others extend to nonsmooth. |
| Trust-Region Sequential Quadratic Programming for Stochastic Optimization with Random Models | arXiv:2409.15734 | Random-model TR is unconstrained in Scheinberg's core work; others extend to constraints. |
| Iteration Complexity and Finite-Time Efficiency of Adaptive Sampling Trust-Region Methods for Stochastic Derivative-Free Optimization | arXiv:2305.10650 | Competing design: adaptive sampling to control estimator error, versus fixed-probability accuracy. |
| Complexity of Zeroth- and First-Order Stochastic Trust-Region Algorithms | SIAM J. Optim., DOI 10.1137/24M1664484 | Parallel complexity line for stochastic TR. |
| Avoiding Geometry Improvement in Derivative-Free Model-Based Methods via Randomization | arXiv:2305.17336 | Alternative answer to the geometry question (randomization instead of self-correction). |
| On complexity constants of linear and quadratic models for derivative-free trust-region algorithms | arXiv:2205.11358 | Scrutiny of the constants hidden in model-based DFO complexity (relevant to "same order, worse constant" claims). |
| Trust-region algorithms: probabilistic complexity and intrinsic noise with applications to subsampling techniques | arXiv:2112.06176 | Parallel probabilistic-TR analysis with intrinsic noise. |
| A trust region method for noisy unconstrained optimization | Math. Program., DOI 10.1007/s10107-023-01941-9 | Competing noise-tolerant TR design (bounded noise, deterministic-style analysis). |

## 4. Structural limits of the lens (analysis — secondary)

1. **Smoothness.** All verified core papers assume a smooth objective (Lipschitz gradient implied by "first-order stationary point" analysis). Nonsmooth, discontinuous or hidden-constraint black boxes are outside the verified work.
2. **Constraints.** Verified probabilistic-model papers are unconstrained (titles: "unconstrained optimization", "trust-region methods"); only the IDFO book and early DFO code address constraints (content not verified here).
3. **Checkability of oracle probabilities.** The frameworks assume a probability p (e.g., ≥ 1/2 in BSV 2014) of a "good" model/estimate; in practice p is rarely known. *Inference:* the lens is strongest when the user can control sample sizes to make p provable (e.g., sampling with known variance).
4. **Constants vs orders.** "Same order as deterministic" results hide constants that depend on p and dimension (Cartis–Scheinberg 2018 wording); for small evaluation budgets constants dominate.
5. **Software maturity.** No maintained modern solver distribution from Scheinberg's group was found (see 03, P6); users needing robust production code will go to other ecosystems (e.g., Powell-family codes such as PDFO https://github.com/pdfo/pdfo, or NAG's Py-BOBYQA https://github.com/numericalalgorithmsgroup/pybobyqa and DFO-LS https://github.com/numericalalgorithmsgroup/dfols — existence confirmed by GitHub metadata).

## 5. Methodological contrasts with the other DFO-team lenses (evidence-based, not personal)

- **Powell lens** (practical interpolation methods, geometry handled by engineering judgement): Scheinberg's 2010 and 2025–2026 papers both *engage* Powell-type methods — first showing a safeguard cannot be dropped, later proving Powell-style methods competitive. Contrast = guarantee-first versus performance-first justification.
- **Conn lens** (deterministic trust-region DFO; "fully linear" model certification): shared origin (CST 1997; CSV 2008; book 2009). Scheinberg's 2014+ work replaces "certified every iteration" with "good with probability p".
- **Vicente lens**: co-author on the 2014 pivot; the direct-search side of Vicente's work (not verified in this file) contrasts with Scheinberg's model/gradient-estimate side.
- **Audet lens** (direct search for nonsmooth, constrained black boxes): contrast on smoothness and oracle assumptions (see §4.1–4.2). No direct exchange between the two was found.
