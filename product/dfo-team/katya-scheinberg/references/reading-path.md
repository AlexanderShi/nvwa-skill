# Reading path for a new student in Scheinberg's group

> Research date: 2026-09-27. Every item was verified by web search (title, authors, year, venue; see `sources/RESOURCES.md`). The order and the "what to learn" lines are the skill author's suggestion, reconstructed from how the papers build on each other. They are **not** a reading list Scheinberg has published. If your supervisor gives you a list, use that one instead.
>
> For each item the line says **what method to take from it**, not only what it proves. Read with `proof-playbook.md` open. The template labels (T1–T13) point there.

## Stage 0 · Orientation (1–2 weeks)

| # | Work | What to learn from it (method, not just result) |
|---|---|---|
| 0a | Talk: Scheinberg, "Stochastic Oracles and Where to Find Them", NeurIPS 2022 OPT workshop plenary (https://neurips.cc/virtual/2022/55786). Also given as the Tutte Lecture (2024) and Lehigh Schantz talk (2025); INFORMS 2021 version titled "Stochastic First Order Oracles…" | How Scheinberg frames the whole programme: define the oracle first (sampling, finite differences, randomized FD, robust estimation), then ask what properties the analysis needs. Watch for how bias and variance are separated. |
| 0b | Curtis, Scheinberg. Adaptive stochastic optimization: a framework for analyzing stochastic optimization algorithms. *IEEE Signal Processing Magazine* 37(5), 32–42 (2020). arXiv:2001.06699 | The group's short overview of *why* adaptive methods (line search, trust region) rather than tuned SGD, and how they are analysed. It gives the vocabulary for everything in Stages 2–3. |

## Stage 1 · Foundations: deterministic model-based DFO (3–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 1 | Conn, Scheinberg, Vicente. *Introduction to Derivative-Free Optimization*. SIAM (2009) | The deterministic proof template every later paper modifies: fully linear / fully quadratic models, poisedness, and trust-region convergence with a criticality step. Learn it well enough to rerun the proof with a weaker assumption (Method 2). |
| 2 | Conn, Scheinberg, Vicente. Geometry of interpolation sets in derivative free optimization. *Math. Program.* 111 (2008) | Where the model-error constants come from (Λ-poisedness × Lipschitz × radius). These are the n-dependent constants in every DFO complexity bound (T13). |
| 3 | Scheinberg, Toint. Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization. *SIAM J. Optim.* 20 (2010) | How to use a **negative result** (geometry steps cannot be fully removed) to design the minimal safeguard (Method 4). |
| 4 | Moré, Wild. Benchmarking derivative-free optimization algorithms. *SIAM J. Optim.* 20(1), 172–191 (2009) | The evaluation convention of the field: data profiles, budgets counted in function evaluations, and smooth, noisy and piecewise-smooth test sets. *Not by Scheinberg*, but Scheinberg's Optima 79 (2009) essay discusses these experiments on Powell's method. Whether the group's papers use this benchmark was not verified, so check with your supervisor. |
| 5 | Larson, Menickelly, Wild. Derivative-free optimization methods. *Acta Numerica* 28, 287–404 (2019) | A map of the whole field, including direct search and the ML zeroth-order literature. Co-authored by a Scheinberg PhD graduate (Menickelly, Lehigh 2017). Use it to place your problem, not as a proof source. |

## Stage 2 · Probabilistic models: the pivot (4–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 6 | Bandeira, Scheinberg, Vicente. Convergence of trust-region methods based on probabilistic models. *SIAM J. Optim.* 24(3) (2014). arXiv:1304.2808 | The key move: keep the algorithm and require model quality only with probability ≥ 1/2, *conditioned on the past*. Learn the conditioning and the random-walk argument for Δ_k (T1). |
| 7 | Chen, Menickelly, Scheinberg. Stochastic optimization using a trust-region method and random models (STORM). *Math. Program.* 169 (2018) | How to put *function estimates* under the same contract, with accuracy ∝ Δ_k², and why an extra condition on bad estimates is needed (T2). |
| 8 | Cartis, Scheinberg. Global convergence rate analysis of unconstrained optimization methods based on probabilistic models. *Math. Program.* 169 (2018) | The counting argument (true/false × successful/unsuccessful) and the "deterministic parity" standard: randomness costs only a p-dependent constant (T3). |
| 8b (contrast) | Gratton, Royer, Vicente, Zhang. Complexity and global rates of trust-region methods based on probabilistic models. *IMA J. Numer. Anal.* 38(3) (2018) | A parallel analysis (not Scheinberg's) with high-probability rates. Compare the two proof techniques, which is a good exercise. |

## Stage 3 · Algorithms as stochastic processes (4–6 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 9 | Blanchet, Cartis, Menickelly, Scheinberg. Convergence rate analysis of a stochastic trust-region method via supermartingales. *INFORMS J. Optim.* 1(2) (2019) | **The most reusable tool.** Map any adaptive method to a generic process and read off E[T_ε] (renewal-reward). Learn the assumption list by heart (T4). |
| 10 | Paquette, Scheinberg. A stochastic line search method with expected complexity analysis. *SIAM J. Optim.* 30 (2020) | Transfer of T4 from trust region to backtracking Armijo. Accuracy relative to α_k‖g_k‖. Recovering deterministic GD rates for convex and strongly convex problems (T5). |
| 11 | Berahas, Cao, Scheinberg. Global convergence rate analysis of a generic line search algorithm with noise. *SIAM J. Optim.* 31 (2021) | How to handle bounded, adversarial noise: relax the Armijo test, state the neighbourhood, and give two alternative gradient conditions (T6). |
| 12 | Berahas, Cao, Choromanski, Scheinberg. A theoretical and empirical comparison of gradient approximations in derivative-free optimization. *Found. Comput. Math.* 22 (2022). Companion: arXiv:1905.13043 | How to *meet* a gradient contract: sample counts and radii for FD, interpolation and smoothing estimators, then an equal-accuracy empirical comparison (Method 5). |

## Stage 4 · High probability, noise, sample complexity (6–8 weeks)

| # | Work | What to learn from it |
|---|---|---|
| 13 | Jin, Scheinberg, Xie. High probability complexity bounds for adaptive step search based on stochastic oracles. *SIAM J. Optim.* 34(3) (2024). Conference version NeurIPS 2021 | Upgrading expected bounds to tail bounds via concentration on the count of good iterations, with biased oracles allowed (T7). Also compare the conference and journal versions to see how a result is extended. |
| 14 | Cao, Berahas, Scheinberg. First- and second-order high probability complexity bounds for trust-region methods with noisy oracles. *Math. Program.* 207 (2024) | The minimal-repair pattern: a relaxed acceptance test and a cautious radius update are the *only* changes, with second-order guarantees under noise (T8). |
| 15 | Jin, Scheinberg, Xie. Sample complexity analysis for adaptive optimization algorithms with stochastic oracles. *Math. Program.* 209 (2025) | How to turn iteration bounds into total-sample bounds by lower-bounding the step parameter with high probability (T9). |
| 16 | Scheinberg, Xie. First- and second-order stochastic adaptive regularization with cubics. arXiv:2308.13161 (2023) | The same programme for a second-order method, with zeroth-, first- and second-order oracles each carrying accuracy and reliability requirements (T10). |

## Stage 5 · Current frontier (ongoing)

| # | Work | What to learn from it |
|---|---|---|
| 17 | Scheinberg, Xie. Stochastic adaptive optimization with unreliable inputs. arXiv:2511.19411 (2025) | One framework for line search and trust region under corrupted gradients and heavy-tailed values. Shows how the tail of the bound follows the tail of the oracle (T11). Probably the best entry point for new stochastic work. |
| 18 | Nguyen, Scheinberg, Tran. Stochastic ISTA/FISTA adaptive step search algorithms for convex composite optimization. *J. Optim. Theory Appl.* 205 (2025) | The first step off the smooth-unconstrained core: prox terms and biased gradients (T12). |
| 19 | Chaudhry, Scheinberg. On complexity of model-based derivative-free methods. arXiv:2510.14935 (2025; ICM 2026 proceedings per co-author's page) | Arc 1 algorithms analysed with Arc 2 tools. Counting function evaluations, including geometry steps, gives complexity competitive with other DFO methods (T13). |
| 20 | Chaudhry, Scheinberg, Sun. Powell-style model-based derivative-free optimization with complexity guarantees. arXiv:2609.09441 (2026) | Full Powell geometry handling, random subspaces ("nearly tight", per the authors' belief) and a noisy extension. Read it alongside open-problems.md rows 1–2. |

## Optional context (ML-optimization thread)

- Curtis, Scheinberg. Optimization methods for supervised machine learning: from linear models to deep learning. *INFORMS TutORials in OR* (2017). https://doi.org/10.1287/educ.2017.0168. This is how Scheinberg explains ML optimization to an OR audience, including its open questions.
- Nguyen, Liu, Scheinberg, Takáč. SARAH: a novel method for machine learning problems using stochastic recursive gradient. *ICML* 2017. arXiv:1703.00102. A Lehigh-era variance-reduction paper. It shows the group's ML side is not only adaptive methods.
- Tang, Scheinberg. Practical inexact proximal quasi-Newton method with global complexity analysis. *Math. Program.* 160, 495–529 (2016). arXiv:1311.6547. Complexity analysis for an inexact, randomized subproblem solver (LHAC code).

## How to read (suggested habit, inference from the group's paper pattern)

For every paper in Stages 2–5, write one index card:

1. the oracle contract (accuracy form + probability + conditioning);
2. the classical method and the exact change made;
3. the potential function and the step-parameter argument;
4. the bound (type, order, constants);
5. what the *next* paper in this list relaxes.

After Stage 4 you should be able to predict item 17's assumptions from items 13–16. If you cannot, reread T4 and T7 in the playbook.
