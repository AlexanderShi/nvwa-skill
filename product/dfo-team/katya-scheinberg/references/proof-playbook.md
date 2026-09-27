# Proof playbook: Scheinberg-style complexity analysis templates

> Research date: 2026-09-27. For a student who needs to prove convergence or complexity for a new stochastic, noisy or derivative-free algorithm in the style of Scheinberg's group.
>
> **Read this first.**
> - **Evidence level.** Every paper below was verified by web search (title, authors, year, venue; see `sources/RESOURCES.md`). Only abstracts and search-result summaries were read, not full texts. Anything described as an *assumption form*, a *lemma pattern* or a *bound form* is labelled **(template, inference)** when it is reconstructed from the abstract plus the standard shape of this literature. Check it against the paper before relying on it. Wording marked "(abstract)" is paraphrased from the abstract as it appeared in search results.
> - **The real supervisor wins.** If Scheinberg, or your own reading of the paper, contradicts anything here, this file is wrong.
> - Never cite a constant or rate from this file in a paper. Cite the paper itself, after reading the theorem.

## 0. The shared skeleton (template, inference)

Across the 2014–2026 papers the same five moves appear. The 2022–2023 talk abstract "Overview of Adaptive Stochastic Optimization Methods" (MIT ORC; MICDE seminar video) summarises the programme: adaptive methods let the step-size parameter set the accuracy required of the stochastic approximations, so those requirements are adaptive and may be biased or even inconsistent. The step-size parameter is not bounded away from zero, which is the obstacle, and viewing the algorithm as a stochastic process with martingale behaviour gives expected complexity bounds that also hold with high probability (paraphrase of the abstract).

| Move | What you write down | Typical object |
|---|---|---|
| M1. Oracle contract | For iteration k, conditioned on the past (filtration F_{k−1}): the event I_k = "gradient/model accurate enough" has P(I_k = 1 \| F_{k−1}) ≥ p. The event J_k = "function estimates accurate enough" has its own probability. Accuracy is **relative to the step parameter**, e.g. ‖g_k − ∇f(x_k)‖ ≤ κ·α_k‖g_k‖ (step search) or a fully linear model on B(x_k, Δ_k) (trust region) | indicator variables I_k, J_k; constants κ, p |
| M2. Deterministic lemma on good iterations | If I_k J_k = 1 and α_k (or Δ_k) ≤ ᾱ(ε), then the iteration is successful and gives decrease ≥ h(α_k, ε) | threshold ᾱ(ε) ∝ ε/L-type quantity (template) |
| M3. Potential | Φ_k = ν(f(x_k) − f_low) + (1 − ν)·(step-parameter term), e.g. α_k‖∇f(x_k)‖² or Δ_k². Show that Φ drops in expectation, or on counted iterations, so that damage from bad iterations is paid for | supermartingale-type inequality |
| M4. Step parameter as a random walk | log_γ α_k moves up on successful good iterations and down otherwise. With p above the threshold (1/2-type), it drifts upward whenever α_k is below ᾱ, so it does not collapse | biased random walk |
| M5. Stopping time | T_ε = first k with ‖∇f(x_k)‖ ≤ ε (or a function-value gap). Bound E[T_ε] (renewal-reward / Wald-type argument) or P(T_ε > t) (martingale concentration on Σ(I_k − p)) | E[T_ε] ≤ C·p/(2p−1)·Φ_0/h(ᾱ_ε) (recalled form of the Blanchet et al. 2019 result, verify) ; P(T_ε > t) ≤ exp(−c·t) for t ≥ C′·Φ_0/h (template) |

**What the constants depend on (template):** L (gradient Lipschitz), Φ_0 (initial gap), γ (step-parameter factor), θ (Armijo / acceptance constant), κ's in the oracle contract, the probability gap p − 1/2 (the 1/(2p−1) blow-up), and for DFO the dimension n through the model-error (poisedness / fully linear) constants. Irreducible noise or bias (ε_f, ε_g) does **not** change the ε-order. It sets the smallest ε you can reach. The oracle tutorial abstracts (2021–2024) describe this as bias affecting the neighbourhood of convergence rather than the rate (paraphrase of a search summary of the abstract).

---

## T1. Probabilistically fully linear models, exact function values

- **Canonical paper:** Bandeira, Scheinberg, Vicente. Convergence of trust-region methods based on probabilistic models. *SIAM J. Optim.* 24(3), 1238–1264 (2014). arXiv:1304.2808.
- **Setting:** smooth unconstrained, trust region, random first-order models (e.g., built from random samples), exact f.
- **Assumptions (abstract):** models are sufficiently accurate (fully linear) with probability ≥ 1/2, conditioned on the past. This is contrasted with stochastic-gradient approaches in which the model is only correct in expectation.
- **Lemma pattern (template, inference):** (a) on a good-model iteration with Δ_k small relative to ‖g_k‖, the step is accepted. (b) Exact f means an accepted step never increases f, so f(x_k) is monotone. (c) log Δ_k is a submartingale-type walk when p ≥ 1/2, so Δ_k cannot shrink forever while the gradient stays large.
- **Bound form:** almost-sure first-order convergence, not complexity.
- **What the constants depend on:** fully linear constants κ_ef and κ_eg (poisedness of the sample set × Lipschitz constant), and trust-region update factors.
- **Pitfalls:** "with probability p" must hold **conditionally on the history**. Independence across iterations is not needed, but unconditional probabilities are not enough. With noisy f you are outside T1: go to T2.

## T2. Random models *and* random function estimates (STORM)

- **Canonical paper:** Chen, Menickelly, Scheinberg. Stochastic optimization using a trust-region method and random models. *Math. Program.* 169, 447–487 (2018). https://doi.org/10.1007/s10107-017-1141-8 (arXiv:1504.04231). Origin in R. Chen's Lehigh PhD thesis "Stochastic Derivative-Free Optimization of Noisy Functions" (2015).
- **Assumptions (abstract):** models and estimates are sufficiently accurate "with high enough, but fixed, probability", with accuracy tied to the radius. Constructions are given under biased or unbiased noise.
- **Lemma pattern (template, inference):** the function-estimate accuracy at x_k and x_k + s_k is of order Δ_k². The potential is Φ_k = ν(f(x_k) − f*) + (1 − ν)Δ_k², and a supermartingale inequality E[Φ_{k+1} − Φ_k | F_k] ≤ −σΔ_k² gives ΣΔ_k² < ∞ a.s., hence Δ_k → 0 and a liminf-type stationarity result. Controlling the *damage* from a bad function estimate needs an extra expected-error condition on the estimates (inference, so check the assumption list).
- **Bound form:** almost-sure convergence. The rate came later (T4).
- **Pitfalls:** accuracy ∝ Δ_k² means sample sizes grow like Δ_k^{-4} for sample-mean estimates with fixed variance (template arithmetic). The iteration analysis says nothing about total samples. That gap is closed in T9.

## T3. Counting argument for line search and cubic regularization with probabilistic models

- **Canonical paper:** Cartis, Scheinberg. Global convergence rate analysis of unconstrained optimization methods based on probabilistic models. *Math. Program.* 169, 337–375 (2018). https://doi.org/10.1007/s10107-017-1137-4 (arXiv:1505.06070).
- **Parallel analysis (not Scheinberg):** Gratton, Royer, Vicente, Zhang. Complexity and global rates of trust-region methods based on probabilistic models. *IMA J. Numer. Anal.* 38(3), 1579–1597 (2018). https://doi.org/10.1093/imanum/drx043. It gives high-probability rates for trust region, which makes it a useful contrast in proof technique.
- **Assumptions (abstract):** random first-order models and directions are good only with some probability. Function values are exact. There is also a probabilistic second-order (cubic regularization) variant.
- **Lemma pattern (template, inference):** classify iterations as true/false × successful/unsuccessful × large/small step. Bound each class count by Φ_0/h or by comparison with the true-iteration count, then take expectations.
- **Bound form (abstract):** evaluation complexity the same as the deterministic counterpart, with the probabilistic models increasing it only by a constant that depends on the probability of the models being good. The results improve in the convex and strongly convex cases. The probabilistic cubic-regularization bound has the same (optimal) order in ε as the deterministic case.
- **Pitfalls:** exact function values are what make "successful ⇒ real decrease" true. Once f is noisy, the counting has to charge false successes (T6–T8).

## T4. Renewal-reward stopping-time analysis (expected complexity)

- **Canonical paper:** Blanchet, Cartis, Menickelly, Scheinberg. Convergence rate analysis of a stochastic trust-region method via supermartingales. *INFORMS J. Optim.* 1(2), 92–119 (2019). https://doi.org/10.1287/ijoo.2019.0016 (arXiv:1609.07428, titled "…via Submartingales").
- **Idea (abstract / search summary):** analyse a *generic* stochastic process and bound the expected stopping time. A renewal-reward process is used, and later work used the same device for stochastic direct-search and line-search analyses.
- **Assumptions (template, inference):** a process {Φ_k, A_k} with Φ_k ≥ 0. A_k is the step parameter updated by factor γ. When A_k is below a threshold, A_k increases with probability ≥ p > 1/2. On such iterations Φ decreases by at least h(A_k).
- **Bound form (recalled form, verify):** E[T_ε] ≤ p/(2p − 1) · Φ_0 / h(Ā_ε) + 1. For STORM this gives O(ε^{-2}) expected iterations in the nonconvex case (order consistent with "deterministic parity").
- **Why it matters for you:** once your algorithm is mapped to the generic process, the rate follows. Your work reduces to checking the assumptions for your oracle and step rule.
- **Pitfalls:** the mapping usually fails at "Φ decreases on good iterations" when function estimates can be wrong. You then need the expected-error condition (T2) or bounded noise (T6).

## T5. Stochastic backtracking Armijo line search (expected complexity)

- **Canonical paper:** Paquette, Scheinberg. A stochastic line search method with expected complexity analysis. *SIAM J. Optim.* 30, 349–376 (2020). https://doi.org/10.1137/18M1216250. arXiv:1807.07994 v1 was titled "…with Convergence Rate Analysis".
- **Assumptions (abstract):** gradient and function values are available up to some dynamically adjusted accuracy that holds with a sufficiently large, but fixed, probability.
- **Lemma pattern (template, inference):** a gradient condition relative to α_k‖g_k‖ and function-estimate errors of order α_k²‖g_k‖². The potential mixes f-gap and α_k‖∇f‖², and T4's machinery applies.
- **Bound form (abstract):** the expected number of iterations to a near-stationary point matches the worst-case efficiency of typical first-order methods. For convex and strongly convex objectives it achieves the rates of deterministic gradient descent in function values.
- **Pitfalls:** accuracy relative to ‖g_k‖ gets harder near stationarity. The theorem is an *iteration* bound, so do not present it as a sample bound.

## T6. Bounded (adversarial) noise in function values

- **Canonical papers:** Berahas, Cao, Scheinberg. Global convergence rate analysis of a generic line search algorithm with noise. *SIAM J. Optim.* 31, 1489–1518 (2021). https://doi.org/10.1137/19M1291832 (arXiv:1910.04055). Companion for the gradient estimator: Berahas, Cao, Choromanski, Scheinberg, *Found. Comput. Math.* 22 (2022), https://doi.org/10.1007/s10208-021-09513-z.
- **Assumptions (abstract):** noise in f bounded in absolute value, with no other assumption. Two alternative conditions on the gradient estimate, each holding with sufficiently large probability, give convergence.
- **Lemma pattern (template, inference):** relax the Armijo test by a noise slack (≈ 2ε_f). Show that on good iterations with ‖∇f‖ above a noise-determined floor, the relaxed test still certifies real decrease.
- **Bound form (abstract):** expected complexity to reach a near-optimal neighbourhood, for convex, strongly convex and nonconvex functions. The neighbourhood size is set by the noise level (form, e.g. ‖∇f‖ ≲ √ε_f-type, is inference).
- **Pitfalls:** a stopping test below the noise floor makes the method run forever or accept noise. Use FoCM 2022's bounds to choose the estimator, the sample count N and the radius σ so that the gradient condition holds.

## T7. High-probability tail bounds for adaptive step search

- **Canonical papers:** Jin, Scheinberg, Xie. High probability complexity bounds for line search based on stochastic oracles. *NeurIPS* 34, 9193–9203 (2021). Extended version: High probability complexity bounds for adaptive step search based on stochastic oracles. *SIAM J. Optim.* 34(3), 2411–2439 (2024). https://doi.org/10.1137/22M1512764 (arXiv:2106.06454). Part of M. Xie's Cornell thesis.
- **Assumptions (abstract):** inexact probabilistic zeroth- and first-order oracles, possibly biased. Step sizes adapt to estimated progress rather than following a pre-specified sequence.
- **Lemma pattern (template, inference):** (i) a deterministic count: true iterations with small α succeed and decrease Φ. (ii) Concentration: Σ_{k<t} I_k ≥ (p − δ)t with probability ≥ 1 − exp(−cδ²t) (Azuma–Hoeffding on I_k − p). (iii) The number of large-step iterations is bounded by the Φ-budget. Combining them gives P(T_ε > t) small once t exceeds a deterministic-order threshold.
- **Bound form (abstract):** high-probability tail bound on iteration complexity for nonconvex, convex and strongly convex (PL) functions. The ε-orders mirror the deterministic ones (inference, consistent with "deterministic parity").
- **Constants:** the gap p − 1/2 (template); the bias levels set the reachable neighbourhood.
- **Pitfalls:** exponential tails need light-tailed function-estimate errors. Heavy tails give polynomial tails (T11).

## T8. Noisy trust region, first- and second-order, high probability

- **Canonical paper:** Cao, Berahas, Scheinberg. First- and second-order high probability complexity bounds for trust-region methods with noisy oracles. *Math. Program.* 207, 55–106 (2024). https://doi.org/10.1007/s10107-023-01999-5 (arXiv:2205.03667). Part of L. Cao's Lehigh thesis (2021).
- **Assumptions (abstract):** value, gradient and Hessian estimates are noisy and are not assumed unbiased or consistent.
- **Algorithm changes (abstract):** a relaxed step-acceptance criterion and a cautious trust-region radius update. These are the only changes to the classical method (Method 2 in SKILL.md).
- **Bound form (abstract):** exponentially decaying tail bounds on iteration complexity for approximate first- and second-order optimality.
- **Pitfalls:** second-order results need the Hessian oracle's accuracy tied to Δ_k. The achievable (ε_g, ε_H) are bounded below by the noise.

## T9. From iteration complexity to oracle/sample complexity

- **Canonical paper:** Jin, Scheinberg, Xie. Sample complexity analysis for adaptive optimization algorithms with stochastic oracles. *Math. Program.* 209, 651–679 (2025). https://doi.org/10.1007/s10107-024-02078-z (arXiv:2303.06838).
- **Problem it solves (abstract):** oracle requirements are adaptive, so per-iteration cost varies. The step parameter is not bounded away from zero because of oracle failures, and bounds on it had not been derived before.
- **Lemma pattern (template, inference):** a high-probability lower bound on the step parameter over the run. Then total cost ≤ (iterations) × (max per-iteration cost given that lower bound).
- **Bound form:** total oracle/sample complexity for adaptive methods (step search, trust region). Take the rates from the paper.
- **Pitfalls:** this is the step that turns T2–T8 into statements practitioners care about. Referees will ask for it.

## T10. Stochastic adaptive regularization with cubics (SARC)

- **Canonical paper:** Scheinberg, Xie. First- and second-order stochastic adaptive regularization with cubics: high probability iteration and sample complexity. arXiv:2308.13161 (2023). The preliminary first-order version appeared at the Winter Simulation Conference 2023 and the NeurIPS 2022 OPT workshop.
- **Assumptions (abstract):** stochastic zeroth-, first- and second-order oracles with stated accuracy and reliability requirements.
- **Bound form (abstract):** the first high-probability iteration and sample complexity bounds for first- and second-order SARC. As in the deterministic case, SARC improves on other stochastic adaptive methods (paraphrase). The ε^{-3/2} first-order order is inference from deterministic ARC. Verify it.

## T11. Unreliable inputs: corrupted gradients, heavy-tailed values

- **Canonical paper:** Scheinberg, Xie. Stochastic adaptive optimization with unreliable inputs: a unified framework for high-probability complexity analysis. arXiv:2511.19411 (2025).
- **Assumptions (abstract):** gradient estimates may be arbitrarily corrupted with some probability (the abstract states the threshold relative to 1/2; read the exact condition in the paper), and function estimates may be heavy-tailed.
- **Bound form (abstract):** high-probability bounds on the stopping time in one framework covering line search and trust region. The tail decays exponentially or polynomially depending on the assumptions on the zeroth-order oracle.
- **Lesson:** the *tail shape* of your complexity bound is inherited from the tail of the function-value oracle. State it explicitly.

## T12. Composite convex problems with adaptive step search

- **Canonical paper:** Nguyen, Scheinberg, Tran. Stochastic ISTA/FISTA adaptive step search algorithms for convex composite optimization. *J. Optim. Theory Appl.* 205, article 10 (2025). https://doi.org/10.1007/s10957-025-02621-8 (arXiv:2402.15646).
- **Assumptions (abstract):** stochastic gradient not assumed unbiased. The analysis extends inexact fixed-step ISTA/FISTA to stochastic gradients with a backtracking step parameter.
- **Use:** the template for adding a prox term, which is the first step off the smooth-unconstrained core.

## T13. Worst-case complexity of model-based (Powell-style) DFO, including random subspaces and noise

- **Canonical papers:** Chaudhry, Scheinberg. On complexity of model-based derivative-free methods. arXiv:2510.14935 (2025; listed on the co-author's homepage as ICM 2026 proceedings). Chaudhry, Scheinberg, Sun. Powell-style model-based derivative-free optimization with complexity guarantees. arXiv:2609.09441 (2026).
- **Parallel work (not Scheinberg):** Cartis, Roberts. A note on the complexity of random subspace model-based methods for derivative-free optimization. arXiv:2608.17307 (2026).
- **Claims (abstract):** complexity bounds are derived systematically for classical model-based trust-region methods and modern variants. They are shown, for the first time, to have the same worst-case complexity as any other known DFO method. Powell's geometry handling is fully incorporated. Random subspaces give what the authors believe to be nearly tight complexity, and the analysis extends to noisy evaluations.
- **Lemma pattern (template, inference):** a deterministic fully linear / poisedness bound gives a model error ≤ κ(n)·Δ. The complexity is counted in **function evaluations**: iterations × evaluations per iteration, including geometry-improving steps. In random subspaces, the "subspace captures enough of ∇f" event plays the role of I_k with a probability that depends on the subspace dimension, so T1/T4-type machinery applies.
- **Pitfalls:** report the dimension dependence explicitly. Count geometry steps. "Nearly tight" is a belief stated in the abstract, not a proven lower bound (see open-problems.md).

---

## Common pitfalls checklist (use before showing a proof to your supervisor)

1. Is every probability **conditional on the past** (F_{k−1}), and is the required p stated with its threshold (1/2-type) and the resulting 1/(2p − 1)-type constant?
2. Is the accuracy requirement tied to the **step parameter** (α_k, Δ_k), not to the target ε? A fixed-accuracy analysis is a different, weaker result.
3. Do bad function estimates have a controlled effect (an expected-error condition, bounded noise, or a tail assumption)? Otherwise one catastrophic estimate breaks the potential argument.
4. Did you separate **iteration**, **oracle/sample** and (for DFO) **function-evaluation** complexity? Which one does your theorem bound?
5. Did you state the **neighbourhood** set by irreducible noise or bias, and a stopping rule that respects it?
6. Does the ε-order match the deterministic counterpart? If not, is the gap intrinsic (lower bound?) or a proof artefact?
7. Is the result almost sure, expected, or high probability? Did you try to upgrade to a tail bound?
8. Did you reuse a canonical template (T4 generic process; T7 concentration; T11 unified framework) instead of re-deriving it? If you re-derived it, why?

## Sanity-check table (fill in for your theorem)

| Item | Your result | Closest canonical result (paper, theorem no. after reading) | Match? |
|---|---|---|---|
| Oracle contract (accuracy form, probability, conditioning) | | | |
| Algorithm change vs classical method | | | |
| Guarantee type (a.s. / expected / high-prob) | | | |
| ε-order | | | |
| p-dependence of constants | | | |
| n-dependence (DFO) | | | |
| Noise floor / neighbourhood | | | |
| Complexity measure (iterations / samples / evaluations) | | | |
