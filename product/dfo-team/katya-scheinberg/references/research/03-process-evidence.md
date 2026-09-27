# 03 · Process evidence (what Scheinberg actually DID)

> Research date: 2026-09-27. Evidence = paper abstracts/records as shown in search results, plus GitHub repository metadata (repository contents could not be opened: the GitHub tool only allowed search, not file reads, for repos outside this project). No full text, appendix, rebuttal, or code file was read. Every claim below is traceable to an abstract-level snippet or repo metadata; deeper claims about proofs or experiments are marked *inference*.

## P1. Same classical algorithm, weaker oracle (probabilistic-oracle abstraction)

| Paper | What changes vs the deterministic method | What stays classical | Source |
|---|---|---|---|
| Bandeira–Scheinberg–Vicente, SIOPT 2014 | Models fully accurate only with probability ≥ 1/2; function values exact | Trust-region acceptance / radius update | arXiv:1304.2808 (primary) |
| Chen–Menickelly–Scheinberg, Math. Program. 2018 (STORM) | Models **and** function estimates accurate with fixed probability; accuracy tied to radius | Trust-region framework | https://doi.org/10.1007/s10107-017-1141-8 (primary) |
| Cartis–Scheinberg, Math. Program. 2018 | Random first-order models/directions good with some probability; also probabilistic cubic regularization | Line search; cubic regularization | https://doi.org/10.1007/s10107-017-1137-4 (primary) |
| Paquette–Scheinberg, SIOPT 2020 | Gradient and function values accurate to dynamically adjusted level with fixed probability | Backtracking Armijo line search | https://doi.org/10.1137/18M1216250 (primary) |
| Jin–Scheinberg–Xie, SIOPT 2024 | Inexact probabilistic zeroth- and first-order oracles, possibly biased | Step search that adapts step size to estimated progress | https://doi.org/10.1137/22M1512764 (primary) |
| Cao–Berahas–Scheinberg, Math. Program. 2024 | Noisy value/gradient/Hessian oracles, not assumed unbiased or consistent | Trust region, with relaxed acceptance and cautious radius update | https://doi.org/10.1007/s10107-023-01999-5 (primary) |
| Scheinberg et al., arXiv:2511.19411 (2025) | Gradients may be arbitrarily corrupted with some probability; heavy-tailed function noise | Line search and trust region in one framework | https://arxiv.org/abs/2511.19411 (primary) |

**Observed practice (7 papers, 2014–2025):** the algorithmic skeleton is almost never new; the novelty is the oracle condition and the analysis. Modifications to the algorithm are minimal and targeted (relaxed acceptance test, cautious radius update) and appear only when the weaker oracle breaks the old proof.

## P2. Analysis style: algorithm as a stochastic process

- Blanchet–Cartis–Menickelly–Scheinberg, INFORMS J. Optim. 2019: a framework "based on analyzing properties of an underlying generic stochastic process and deriving a bound on the expected stopping time" (snippet; primary record https://ora.ox.ac.uk/objects/uuid:798e9ee8-baa2-4497-b53a-1377c4c2f748). The arXiv version was titled "…via Submartingales" (arXiv:1609.07428); the journal title says "Supermartingales" — the naming changed between versions (observable from the two records).
- Progression of result type across papers (observable in titles/abstracts): almost-sure convergence (STORM 2018) → expected complexity (Cartis–Scheinberg 2018; Blanchet et al. 2019; Paquette–Scheinberg 2020) → **high-probability tail bounds** (Jin–Scheinberg–Xie 2024; Cao–Berahas–Scheinberg 2024, "exponentially decaying tail bounds") → unified high-probability framework under corrupted/heavy-tailed inputs (arXiv:2511.19411).
- Result yardstick used repeatedly: complexity "the same as" deterministic counterpart up to a constant depending on the success probability (Cartis–Scheinberg 2018; Paquette–Scheinberg 2020).

## P3. DFO geometry: find the minimal safeguard, then analyse practice

- Conn–Scheinberg–Toint, Math. Program. 1997: trust-region DFO with techniques ensuring the "geometric quality" of models (https://doi.org/10.1007/BF02614326, primary).
- Conn–Scheinberg–Vicente, Math. Program. 2008: poisedness / error bounds for interpolation sets (https://www.mat.uc.pt/~lnv/papers/csv.pdf, primary).
- Scheinberg–Toint, SIOPT 2010: shows geometry-improving steps cannot be completely eliminated for global convergence, and gives an algorithm in which they occur only in the final stage, using a "self-correction mechanism" of trust region + interpolation (https://doi.org/10.1137/090748536, primary). → A negative result used to design the smallest fix.
- Chaudhry–Scheinberg arXiv:2510.14935 (2025) and Chaudhry–Scheinberg–Sun arXiv:2609.09441 (2026): take Powell-style methods as given, "fully incorporate Powell's geometry handling approach", derive complexity, add random subspaces and noise (primary).

## P4. Experiments: head-to-head against standard codes and estimators

- Zhang–Conn–Scheinberg, SIOPT 2010: least-squares DFO algorithm with "numerical comparisons … to standard derivative-free software packages" (snippet; https://www.math.lsu.edu/~hozhang/papers/GlobalDFLS.pdf).
- Berahas–Cao–Choromanski–Scheinberg, FoCM 2022: four gradient estimators (finite differences, linear interpolation, Gaussian smoothing, sphere smoothing) compared by derived sample-count/radius bounds **and** empirically (https://doi.org/10.1007/s10208-021-09513-z).
- Chaudhry–Scheinberg–Sun 2026: "extensive numerical comparison of the model-based trust region methods" (arXiv:2609.09441).
- *Inference (not verified in full text):* benchmark sets likely standard DFO test collections; not confirmed. ✗ Superseded (full text): verified from five papers (Moré–Wild set, CUTEr/CUTEst, data and performance profiles) [cards S023, pp. 17–19; S033, pp. 25–26; S012, pp. 27–29; S041, pp. 33–36; S104, pp. 26–30].

## P5. Structure exploitation before generic methods

- Fine–Scheinberg, JMLR 2001: low-rank kernel representation (incomplete Cholesky with pivoting per snippet) to make SVM training efficient (https://www.researchgate.net/publication/2865065_Efficient_SVM_Training_Using_Low-Rank_Kernel_Representations).
- Scheinberg–Ma–Goldfarb, NIPS 2010: alternating linearization exploiting the sparse-inverse-covariance structure so subproblems have closed-form solutions; O(1/ε) iterations (https://papers.nips.cc/paper/4099-sparse-inverse-covariance-selection-via-alternating-linearization-methods).
- Zhang–Conn–Scheinberg, SIOPT 2010: model each residual of a least-squares objective separately rather than the sum.

## P6. Software trail (metadata only)

| Artifact | Evidence | URL | Cred. |
|---|---|---|---|
| DFO (Fortran, COIN-OR) | IDFO book blurb: Scheinberg "authored the open source DFO software"; unofficial GitHub mirror of COIN-OR DFO exists | https://github.com/jacobwilliams/dfo | primary (blurb) / secondary (mirror) |
| DFO-TR (Python) | Repo "Blackbox derivative-free optimization with DFO-TR algorithm", created 2015 by The Climate Corporation; README mentions Scheinberg (matched by GitHub `in:readme Scheinberg` search) — an industrial user of the method | https://github.com/TheClimateCorporation/dfo-algorithm | secondary |
| DFOTR (MATLAB) | Repo by Liyuan Cao (co-author of FoCM 2022 and Math. Program. 2024), created 2019; README matched `Scheinberg` | https://github.com/LiyuanCao/DFOTR | secondary |
| LHAC (C++) | Repo "Practical Inexact Proximal Quasi-Newton Method with Global Complexity Analysis"; README matched `Scheinberg` (paper venue/year unverified ⚠️) | https://github.com/LHAC/LHAC | secondary |
| DFLS (C) | Repo named DFLS; README matched `Scheinberg` | https://github.com/ikarib/DFLS | secondary |

**Observed practice:** code is released as small research implementations tied to specific papers (MATLAB/Python/C++), not as a maintained solver suite after the original DFO package. *Inference:* compared with the Powell (PDFO) or NAG Py-BOBYQA/DFO-LS ecosystems, Scheinberg's code footprint is research-grade.

## P7. What could not be observed

- Proof drafts, arXiv v1→final changes (beyond the Submartingales→Supermartingales title change), referee reports, rebuttals, failed projects. No evidence of abandoned directions was retrievable.

---

## Update 2026-09-27 (deepening pass)

### P1+ More papers with the same pattern: classical method kept, weaker oracle

| Paper | What changes vs deterministic | What stays classical | Source |
|---|---|---|---|
| Berahas–Cao–Scheinberg, SIOPT 31 (2021) | f computed with bounded noise, and no other assumption. Gradient estimates inexact and possibly random | Line search (modified by a noise slack) | https://doi.org/10.1137/19M1291832 ; arXiv:1910.04055 |
| Jin–Scheinberg–Xie, NeurIPS 34 (2021) | Probabilistic zeroth/first-order oracles, possibly biased | Line search | https://proceedings.neurips.cc/paper/2021/hash/4cb811134b9d39fc3104bd06ce75abad-Abstract.html |
| Scheinberg–Xie, arXiv:2308.13161 (2023; WSC 2023 preliminary) | Stochastic zeroth/first/second-order oracles with accuracy and reliability requirements | Adaptive regularization with cubics | https://arxiv.org/abs/2308.13161 |
| Jin–Scheinberg–Xie, Math. Program. 209 (2025) | Adaptive oracle costs; step parameter not bounded below | Step search / trust region | https://doi.org/10.1007/s10107-024-02078-z |
| Nguyen–Scheinberg–Tran, JOTA 205 (2025) | Stochastic gradient not assumed unbiased | ISTA / FISTA with backtracking | https://doi.org/10.1007/s10957-025-02621-8 |

With the earlier table this makes **12 papers (2014–2026)** following P1. That is enough to treat Method 2 as the group's default design move, not a coincidence.

### P2+ Analysis style: more detail

- Blanchet et al. (2019): the search summary describes the core device as a general **renewal-reward** process and its stopping time. Later work used the same device for stochastic direct-search and line-search analyses (https://doi.org/10.1287/ijoo.2019.0016).
- **Title drift between arXiv v1 and the journal version** (observable): "…via Submartingales" → "…via Supermartingales" (Blanchet et al.); "A Stochastic Line Search Method with Convergence Rate Analysis" (arXiv:1807.07994 v1) → "…with Expected Complexity Analysis" (SIOPT 2020); "…for Line Search Based on Stochastic Oracles" (NeurIPS 2021) → "…for Adaptive Step Search Based on Stochastic Oracles" (SIOPT 2024). *Reading (inference):* results are sharpened in revision toward a precise statement of *which* guarantee (expected complexity) and *which* algorithm class (step search rather than line search).
- **Short version first, long version later** (observable): NeurIPS 2021 → SIOPT 2024; NeurIPS 2022 OPT workshop / WSC 2023 → arXiv:2308.13161 (extended to second order). *Inference:* ML or simulation venues are used to put a result out, and optimization journals carry the full theory.
- **From iteration to sample complexity** (observable): after tail bounds (2021–2024), the 2025 Math. Program. paper bounds the step parameter to obtain total oracle cost. It is the same programme one level closer to practice.

### P4+ Experiments: what could and could not be verified

- FoCM 2022 abstract (via search): numerical results evaluate the quality of the gradient approximations *and* their performance inside a line-search DFO algorithm. Estimators are compared on two levels, accuracy of the estimate and end-to-end performance.
- Optima 79 (≈2009) essay: builds on the Moré–Wild numerical experiments on Powell's method (search summary). ✗ Corrected 2026-09-27 (full text, card S143, pp. 4, 6): the Moré–Wild framing and the "only minimal quality controls" wording are from Jorge Nocedal's discussion column in the same issue (p. 6), which presents them as a summary of her essay ("As Scheinberg discusses in this issue of Optima, …"); Moré–Wild is not in her reference list. Her own statement is p. 4: "it turns out that it is not necessary to compute extra sample points unless the gradient of the model becomes small." Moré & Wild, SIAM J. Optim. 20(1) (2009), introduced **data profiles** for budget-limited DFO benchmarking (https://doi.org/10.1137/080724083).
- Stefan M. Wild (co-author of the benchmark paper) sat on R. Chen's 2015 Lehigh PhD committee (thesis record, https://preserve.lehigh.edu/etd/2548). Menickelly (Scheinberg PhD, 2017) co-authored the 2019 Acta Numerica DFO survey with Larson and Wild.
- *Inference, not verified:* the group's DFO experiments likely use Moré–Wild-style problems and data/performance profiles, with budgets counted in function evaluations. **No search result confirmed the test sets or metrics used in any specific Scheinberg paper.** The pre-meeting workflow in SKILL.md therefore phrases this as a question to check, not a rule. ✗ Superseded (full text): the published conventions are now verified (see the line above and SKILL.md Method 5); the group's *current* convention is still a question for the supervisor.

### P5+ ML-optimization thread (verified)

- Tang & Scheinberg, *Math. Program.* 160, 495–529 (2016), "Practical inexact proximal quasi-Newton method with global complexity analysis" (arXiv:1311.6547; LHAC = Low-rank Hessian Approximation in Active-set Coordinate descent). The first global rate for an algorithm that solves its subproblems inexactly by randomized coordinate descent (per summary of Tang's thesis).
- Nguyen, Liu, Scheinberg, Takáč, *ICML* 2017, "SARAH" (arXiv:1703.00102): a recursive stochastic gradient for finite sums, with a linear rate under strong convexity, including for the inner loop.
- SIAM OP17 plenary title (2017): "Using Second-order Information in Training Large-scale Machine Learning Models".
- *Observed:* at Lehigh (2010–2019) the ML line ran alongside the probabilistic-model line and shared its taste: exploit structure (low-rank Hessians, active sets) and prove a global rate.

### P6+ Software trail update

- LHAC paper venue now verified (Math. Program. 2016), so row 32 in RESOURCES.md is upgraded.

### P9 Say–do cross-check after this pass

| Stated (02-methodology) | Practised (this file) | Verdict |
|---|---|---|
| Define the oracle first (F1–F3, 2021–2025) | Oracle conditions are the main novelty in 12 papers (P1, P1+) | ✅ consistent |
| Analyse algorithms as stochastic processes with martingale behaviour (F4) | Blanchet 2019 renewal-reward; tail bounds 2021–2025 | ✅ consistent |
| Minimal quality control in model-based DFO (Optima 79, ≈2009) | Scheinberg–Toint 2010; Powell-style complexity 2025–2026 | ✅ consistent over 17 years. ⚠ Corrected: not constant. The stance dates from 2009–2010 [cards S143, p. 4; S030, pp. 3, 12]; in 2008 the stated practice was the opposite, "maintain well-poisedness throughout the algorithm" [card S016, p. 18]; the "minimal quality controls" wording is Nocedal's column [card S143, p. 6] |
| Adaptive methods instead of tuned schedules (G2, F4) | Every stochastic paper uses line search, trust region or ARC | ✅ consistent. Large-scale ML evidence for the *savings claim* is not in the verified corpus (see open-problems.md row 10) |
| Bias affects the neighbourhood, not the rate (F3, paraphrase) | Neighbourhood results in BCS 2021 and CBS 2024; biased oracles in JSX 2024 | ✅ consistent (stated side unconfirmed verbatim) |
