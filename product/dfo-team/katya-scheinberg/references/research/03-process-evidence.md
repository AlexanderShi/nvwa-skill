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
- *Inference (not verified in full text):* benchmark sets likely standard DFO test collections; not confirmed.

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
