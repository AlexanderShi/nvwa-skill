# 03 · Process Evidence (what Vicente actually DID)

> Behaviour traces: algorithm-design moves visible across papers, analysis templates, released software, benchmarking protocol, corrections. Reconstructed from abstracts, software pages and repository titles relayed by search. **No code or full text was opened** (all fetch hosts blocked; GitHub MCP limited to this repo), so "practice" here means *what the published artefacts show was done*, not how it was done day to day.

## P1 · Design move: put the useful heuristic inside a provably convergent direct-search skeleton

Recurring template: **search step = anything you like (heuristic, model, swarm, ES offspring); poll step and step-size control = where convergence comes from; acceptance by sufficient decrease.**

| Instance | Heuristic kept | Guarantee added | Source (credibility) |
|---|---|---|---|
| SID-PSM (Custódio & Vicente 2007) | quadratic models in the search step; simplex gradients to order the poll | generalized-pattern-search global convergence | http://www.mat.uc.pt/sid-psm/ (primary) |
| PSwarm (Vaz & Vicente, J. Glob. Optim. 39 (2007) 197–219) | particle swarm in the "optional search phase" | coordinate-search convergence "to stationary points from arbitrary starting points" | https://link.springer.com/article/10.1007/s10898-007-9133-5 (primary) |
| MFN models (Custódio, Rocha & Vicente, COAP 2010) | minimum Frobenius norm quadratic models minimized in a trust region → search step | unchanged directional DS structure | https://link.springer.com/article/10.1007/s10589-009-9283-0 (primary) |
| Globally convergent ES (Diouane, Gratton & Vicente, Math. Program. 2015) | CMA-ES-type recombination + random offspring | reduce step size when sufficient decrease fails; otherwise the step may be "reset to the step size maintained by the evolution strategies themselves, as long as this is sufficiently large" | https://link.springer.com/article/10.1007/s10107-014-0793-x (primary) |
| Full-low evaluation (Berahas, Sohab & Vicente, OMS 2023) | Full-Eval: finite-difference gradient + BFGS line search (efficient when smooth, no noise) | Low-Eval: cheap direct-search-type iterations, robust to noise and non-smoothness | https://arxiv.org/pdf/2107.11908 (primary) |
| Non-monotone DS (Ding, Tran & Vicente 2026) | max-M non-monotone acceptance (helps in curved valleys) | new complexity theory despite no monotonic decrease | https://arxiv.org/abs/2609.11567 (primary) |

Cross-project count: ≥6 projects over 2007–2026 → passes the cross-project check.

## P2 · Analysis template: sufficient decrease → count iterations/evaluations → compare with the gradient method → ask whether the order is optimal

| Step | Instance | Source |
|---|---|---|
| Establish the smooth nonconvex bound | O(ε⁻²) iterations, like steepest descent (Vicente 2013) | https://link.springer.com/article/10.1007/s13675-012-0003-7 |
| Specialize to convex | O(ε⁻¹), like the gradient method (Dodangeh & Vicente 2016) | https://link.springer.com/article/10.1007/s10107-014-0847-0 |
| Track dimension and check optimality | O(n²ε⁻²) evaluations, and the n² factor is optimal (Dodangeh, Vicente & Zhang 2016) | https://link.springer.com/article/10.1007/s11590-015-0908-1 |
| Price in nonsmoothness | smoothing DS is "roughly one order of magnitude worse" (Garmanjani & Vicente 2013) | https://optimization-online.org/2012/01/3331/ |
| Price in randomness | probabilistic descent: better bounds with overwhelming probability (GRVZ 2015); trust-region with probabilistic models: global rates (GRVZ 2018) | https://dx.doi.org/10.1093/imanum/drx043 |
| Price in noise | samples per iteration reduced from O(δ⁻⁴) to O(δ⁻²q) (tail bound; talk abstract paraphrase) | https://doi.org/10.1137/22M1543446 |
| Price in non-monotonicity | "comprehensive complexity theory" for max-M acceptance (2026) | https://arxiv.org/abs/2609.11567 |

**Observed discipline**: each new algorithmic freedom (randomness, noise, nonsmoothness, non-monotonicity, multiple objectives) is paid for with an explicit complexity statement, not only with numerics.

## P3 · Probabilistic relaxation of deterministic requirements

- Trust-region models need only be accurate with some probability conditioned on the past, so "random models of higher quality than those produced by the usual stochastic gradient methods" can be used (Bandeira, Scheinberg & Vicente 2014, abstract paraphrase). https://www.semanticscholar.org/paper/Convergence-of-Trust-Region-Methods-Based-on-Models-Bandeira-Scheinberg/edf332931d618a7788cce3d9338970fd835826a5 (primary)
- Polling directions need only probabilistic descent, with no positive spanning set (GRVZ 2015), later extended to bound and linear constraints via random directions in approximate tangent cones (GRVZ 2019). https://link.springer.com/article/10.1007/s10589-019-00062-4 (primary)
- In the stochastic setting the tail bound applies to the *estimated decrease*, and the sufficient-decrease check becomes a *sequential hypothesis test* (Ding, Rinaldi & Vicente 2025). https://arxiv.org/pdf/2509.14505 (primary)
- Sparse interpolation models: with few samples, recover sparse Hessian structure (Bandeira, Scheinberg & Vicente 2012, arXiv:1306.5729). This is a compressed-sensing-style relaxation of the interpolation requirement (inference from abstract). https://arxiv.org/abs/1306.5729 (primary)

## P4 · Generalize the acceptance test to reach a new problem class

| New class | What replaced "f(trial) < f(x) − ρ(α)" | Source |
|---|---|---|
| Multiobjective (DMS 2011) | trial point not dominated by the current list; the list is updated by Pareto dominance | https://epubs.siam.org/doi/10.1137/10079731X |
| Constraints (Gratton & Vicente 2014) | merit function (+ restoration) for relaxable constraints; extreme barrier for unrelaxable ones | https://www.mat.uc.pt/~lnv/papers/merit.pdf |
| Discontinuous f (Vicente & Custódio 2012) | same test; analysis via Rockafellar upper subderivatives along refining directions | https://doi.org/10.1007/s10107-010-0429-8 |
| Stochastic f (2024–2025) | decrease estimated from samples, controlled by tail bound / sequential test | https://arxiv.org/abs/2202.11074 |
| Stochastic multi-objective ML (2021–2026) | multi-gradient via a QP subproblem (biased even with unbiased gradients); block-coordinate + function alternation | https://arxiv.org/abs/1907.04472 ; https://arxiv.org/abs/2605.12432 |

## P5 · Software and benchmarking protocol

- **Released solvers** (primary, software pages via search):
  - SID-PSM, MATLAB, v1.3 (Dec 2014), GNU LGPL, "freely available for research, educational or commercial use", obtained by e-mail. http://www.mat.uc.pt/sid-psm/
  - DMS (Direct MultiSearch), MATLAB site with paper and **errata**. http://www.mat.uc.pt/dms/
  - PSwarm (with Vaz): bound/linear constrained global DFO solver; the ASCL entry lists it as a code (https://ascl.net/2111.003). Authorship of the OMS 2009 solver paper was not confirmed by search (⚠️ in RESOURCES).
  - Lehigh-era papers ship public GitHub code written by the student or postdoc first author: `sul217/MOO_Fairness` (fairness trade-offs, "code and jupyter notebooks corresponding to four sets of trade-off results"), `GdKent/BSG_Methods_Con_Unc` (bilevel SG), `tommaso-giovannelli/snee` (Pareto knees). Repo titles/descriptions came from search; contents not opened.
- **Benchmarking**: DMS used performance profiles (Dolan–Moré style) with metrics suited to the new setting, namely purity and spread Γ and Δ, on a collection of 100 AMPL problems; the problem collection was offered to others (search summary of the DMS paper PDF). GRVZ 2015 compared random versus deterministic polling and reports "clear superiority" of randomization in some cases (abstract paraphrase). A ResearchGate figure caption, "Performance of three variants of Algorithm 2.1 and MATLAB patternsearch", surfaced in the search for GRVZ 2019. Which paper it belongs to is not confirmed (⚠️).
- **Real applications in theses**: 3D full-waveform inversion (Earth imaging, geophysics) in Diouane's thesis; an Airbus – IRT Saint Exupéry member on Royer's jury; credit-scoring and criminal-justice-style fairness data in Liu's thesis (search summaries of thesis pages, secondary).

## P6 · Corrections and failures on record

- **DMS errata** posted on the DMS website (existence confirmed; content not seen).
- **Discontinuous-functions theorem**: the theorem announced in the last part of Vicente & Custódio (2012) has a counterexample (Audet, Bouchet & Bourdin, Math. Program. 208 (2024) 411–424, DOI 10.1007/s10107-023-02042-3; arXiv v1 titled "Erratum, counterexample and an additional revealing poll step…", arXiv:2211.09947). How Vicente responded is not documented in the sources found.
- No record found of rejected papers, abandoned directions, or retractions.

## P7 · Era and resource profile

- Methods run in MATLAB on laptop-scale test sets (AMPL/CUTEr-type collections). None need large compute. The Lehigh ML work uses standard ML datasets (logistic classification, multi-target regression, continual learning). Resource threshold: low, so an individual researcher can execute these methods.
- Toulouse co-supervision (with Serge Gratton) gave access to industrial and geophysics problems. That application channel is institution-dependent (see 04).
