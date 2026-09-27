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

---

## Update 2026-09-27 (deepening pass)

Still **no published critique, comment paper, or public review of Scheinberg's work** was found. The additions are verified parallel and competing lines, which show where others think the framework needs extending, plus Scheinberg's own stated critiques of competing practice.

### 6. Verified parallel / competing lines (authors now confirmed)

| Work | Authors (verified) | Relation to Scheinberg's work |
|---|---|---|
| Complexity and global rates of trust-region methods based on probabilistic models, *IMA J. Numer. Anal.* 38(3), 1579–1597 (2018), https://doi.org/10.1093/imanum/drx043 | S. Gratton, C. W. Royer, L. N. Vicente, Z. Zhang | **Parallel** probabilistic trust-region complexity, with high-probability iteration bounds. It appeared the same year as Cartis–Scheinberg (expected bounds). The probabilistic-model idea from BSV 2014 was developed in two groups at once. Scheinberg's group reached high-probability bounds for *adaptive stochastic* (not only random-model) settings later (2021–2024). |
| Robust Accelerated Adaptive Search: high-probability complexity bounds under bounded-moment stochastic oracles, arXiv:2604.15526 (2026) | S. Zhang, S. Liao, C. Han, T. Guo (UCAS) | **Third-party extension** of the high-probability adaptive-search framework to momentum/acceleration and bounded-moment oracles. Previously listed as possibly related; it is now confirmed **not** Scheinberg's. It fills a gap in the verified corpus (acceleration; open-problems.md row 5). |
| A note on the complexity of random subspace model-based methods for derivative-free optimization, arXiv:2608.17307 (2026) | C. Cartis, L. Roberts | **Parallel/competing** analysis on the question Chaudhry–Scheinberg(–Sun) address: dimension dependence of random-subspace model-based DFO. Compare the bounds before claiming tightness (open-problems.md row 1). |
| Derivative-free optimization methods, *Acta Numerica* 28, 287–404 (2019) | J. Larson, M. Menickelly, S. M. Wild | Survey by a Scheinberg PhD graduate with Argonne co-authors. It positions probabilistic-model methods within the whole DFO field and is the neutral reference for "what else exists". |
| Benchmarking derivative-free optimization algorithms, *SIAM J. Optim.* 20(1), 172–191 (2009) | J. J. Moré, S. M. Wild | The benchmarking standard (data profiles). Scheinberg's Optima 79 essay builds on its findings about Powell's method (search summary). |

### 7. Scheinberg's stated critiques of competing practice (primary)

- **Tuned step schedules in SG methods.** Curtis–Scheinberg, *IEEE SPM* 2020: non-adaptive SG approaches need prescribed parameters tuned for each application. Adaptive methods may save substantial computation (paraphrase).
- **Expectation-only model correctness.** BSV 2014 (via search summary): contrasted with stochastic-gradient approaches in which the model is assumed correct only in expectation.
- **Assuming unbiased gradients.** Nguyen–Scheinberg–Tran, JOTA 2025, analyse stochastic ISTA/FISTA without assuming an unbiased stochastic gradient. Jin–Scheinberg–Xie 2024 allow biased oracles.
- **"Model-based DFO has no competitive worst-case theory."** Chaudhry–Scheinberg 2025 state that complexity analysis lagged behind practice and show that these methods can match any known DFO method in the worst case.
- **Over-engineering model quality.** Optima 79 (≈2009): only minimal quality controls are needed (paraphrase of search summary), citing the Moré–Wild experiments on Powell's method. This is an implicit critique of certifying model quality at every iteration.

### 8. Self-critique through the gaps each paper names (primary)

| Paper | Gap it names in earlier work (abstract-level, paraphrase) |
|---|---|
| Jin–Scheinberg–Xie, Math. Program. 2025 | The step parameter is not bounded away from zero, and bounds on it had not been derived, so earlier iteration bounds did not yield sample complexity. |
| Scheinberg–Xie, arXiv:2511.19411 | Earlier high-probability frameworks did not cover arbitrarily corrupted gradients or heavy-tailed values. This is the first analysis giving high-probability stopping-time bounds in that setting. |
| Chaudhry–Scheinberg–Sun, arXiv:2609.09441 | The 2025 companion analysed a *simplified* version of Powell's methods. The 2026 paper incorporates Powell's full geometry handling. |
| Berahas–Cao–Scheinberg, SIOPT 2021 | The earlier stochastic-process framework assumed exact function values and random gradients. This paper extends it to noisy functions. |

### 9. Updated structural limits

- Limits §4.1–4.2 (smoothness, constraints) are **reconfirmed** by talk titles: the Aisenstadt lectures (2025) are explicitly about *unconstrained* continuous optimization.
- The composite (prox) case is now covered for **convex** problems (JOTA 2025). The nonconvex composite and constrained cases remain outside the verified work.
- Acceleration/momentum: not in the verified Scheinberg corpus. Third parties are extending it (RAAS 2026).
