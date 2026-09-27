# 05 · Peer critique, limits, later developments

Research date: 2026-09-27. No personal disputes were found or are implied. Everything below is a **methodological difference evidenced by publications**. Several items are not critiques of Conn by name; they are later results that bound where the Conn line of methods applies.

## 1. Is geometry management worth its cost? (the central DFO critique)

| Work | What it shows | Relation to Conn's method | Source | Credibility |
|---|---|---|---|---|
| Fasano, Morales, Nocedal, "On the geometry phase in model-based algorithms for derivative-free optimization", *Optim. Methods Softw.* 24 (2009) 145–154 | Numerical study of a model-based algorithm that **dispenses with the geometry phase altogether**. Tracks the interpolation-matrix condition number and gradient accuracy on smooth problems with n = 2–15. Widely read as evidence that practical performance can survive without explicit geometry steps. | Challenges the *practical necessity* of the poisedness maintenance at the heart of CST 1997 / CSV 2008–2009 | https://www.tandfonline.com/doi/abs/10.1080/10556780802409296 | Primary (critic's own paper) |
| Scheinberg & Toint, "Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization", *SIAM J. Optim.* 20(6) (2010) 3512–3532 | Geometry-improving steps **cannot be completely eliminated** if global convergence is wanted, but they can be confined to the final stage, where criticality is checked. | A partial vindication *and* a refinement from inside Conn's own circle | https://optimization-online.org/2009/02/2216/ | Primary |
| "Avoiding geometry improvement in derivative-free model-based methods via randomization" (arXiv 2305.17336) | Title indicates randomized models remove explicit geometry steps. Authors not confirmed in snippet. | Later direction (unverified details) | https://arxiv.org/pdf/2305.17336 | ⚠️ lead only |

**Takeaway for the skill:** the Conn lens should defend geometry control as *the thing that makes the theorem true*. It should also admit, citing the two works above, that practical codes may do less of it and still work well on smooth problems.

## 2. Benchmarking standards moved beyond the CUTE-style comparison

| Work | Point | Source |
|---|---|---|
| Moré & Wild, "Benchmarking derivative-free optimization algorithms", *SIAM J. Optim.* 20(1) (2009) 172–191 | Introduces **data profiles** for DFO under computational-budget constraints, on smooth, noisy and piecewise-smooth problem sets. The unit of cost is function evaluations, not iterations. | https://www.mcs.anl.gov/~more/dfo/ (primary) |
| Rios & Sahinidis, "Derivative-free optimization: a review of algorithms and comparison of software implementations", *J. Global Optim.* 56(3) (2013) 1247–1293 | 22 implementations on 502 problems. Global/multistart solvers (e.g., TOMLAB/MULTIMIN, TOMLAB/GLCCLUSTER, MCS, TOMLAB/LGO) did best on average for solution quality within 2,500 evaluations (snippet). This shows that local model-based methods are not automatically the best choice when the goal is the best solution in a fixed budget. | https://www.semanticscholar.org/paper/Derivative-free-optimization:-a-review-of-and-of-Rios-Sahinidis/580b166bab3796ccf35abdff6b0677986913a5d6 (primary) |

**Implication:** the IBM promotional comparison (4 vs 351 iterations; 82 vs 23,402 simulations against NOMAD, per https://researcher.watson.ibm.com/researcher/view_group.php?id=3346) should be treated cautiously. The problem, the tolerances, whether gradient information was used, and the NOMAD settings are not stated. A Moré–Wild-style data profile would be the fair test. The Conn lens must *apply its own benchmarking discipline* to such claims.

## 3. Limits evidenced by Conn's own later work

- **Constraints and nonsmoothness.** In 2018 Conn co-authored a trust-region method that *imports* the progressive barrier from the MADS school. It is "competitive with COBYLA" on 40 smooth problems and "can be competitive with NOMAD" on nonsmooth MDO problems (DOI 10.1007/s10589-018-0020-4). Smooth-model methods did not dominate on nonsmooth engineering problems.
- **Direct search plus models.** Conn & Le Digabel (2013) show quadratic models improve MADS "significantly". The best practical recipe was a hybrid, not a pure model-based method.
- **Own software superseded.** LANCELOT was replaced by IPOPT inside IBM's circuit tuner (MAM 2015 profile). The augmented-Lagrangian approach was overtaken by interior-point filter methods for that application.

## 4. Where the field went after Conn (context for roundtable disagreements)

| Development | Source | Status |
|---|---|---|
| Comprehensive review organising DFO by assumptions on the black box (deterministic/noisy/stochastic, smooth/nonsmooth, structured) | Larson, Menickelly, Wild, "Derivative-free optimization methods", *Acta Numerica* 28 (2019) 287–404, DOI 10.1017/S0962492919000060 | ✅ primary |
| "Fully linear / fully quadratic" model theory (from the CSV monograph) became the common language for later model-based DFO analyses, including probabilistic and random-subspace variants | Secondary descriptions in later arXiv papers (e.g., https://arxiv.org/pdf/2605.30845) | ✅ as a description of influence (secondary) |
| Powell's own survey of DFO algorithms | Powell, "A view of algorithms for optimization without derivatives", DAMTP 2007/NA03 | ✅ title/author/year. **Content regarding Conn not read**, so no claim is made about Powell's view of CSV geometry. |

## 5. Critiques NOT found (declared)

- No published critique of LANCELOT/CUTE by name was retrieved.
- No reproduction failures, errata or retractions were found for Conn's papers.
- No direct Conn rebuttal to Fasano–Morales–Nocedal was found.
