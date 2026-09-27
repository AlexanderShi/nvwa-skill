# 05 · Peer Critique, Limits, Competing Approaches

> Rule: only methodological differences evidenced by publications. No personal conflict is implied or should be inferred.

## C1 · Counterexample to the discontinuous-functions theorem (direct critique)

- **What**: Audet, Bouchet & Bourdin, "Counterexample and an additional revealing poll step for a result of 'analysis of direct searches for discontinuous functions'", Math. Program. 208 (2024) 411–424, DOI 10.1007/s10107-023-02042-3. The arXiv v1 was titled "Erratum, counterexample and an additional revealing poll step…" (arXiv:2211.09947).
- **Content (search summary)**: a function satisfying all assumptions of the theorem announced in the last part of Vicente & Custódio (Math. Program. 133 (2012) 299–325) contradicts some of its conclusions. The flaw: a directional direct search can converge to a point where f is discontinuous and lower semicontinuous, with f there strictly below lim f(x_k), while generating trial points in only one continuity set. The fix is an additional "revealing" poll step.
- **Lesson for the skill**: the push to extend direct-search theory to ever-weaker smoothness classes has a real failure mode. Claims at the edge of the theory (discontinuity) need adversarial counterexample checking.
- Source: https://link.springer.com/article/10.1007/s10107-023-02042-3 ; https://arxiv.org/pdf/2211.09947 (primary; secondary with respect to Vicente)

## C2 · Sharpness check on probabilistic descent (critique that confirms)

- **What**: Huang & Zhang, "Non-convergence Analysis of Probabilistic Direct Search", arXiv:2606.01320 (May 2026). Zhang co-authored the original 2015 paper.
- **Content**: asks whether the submartingale-like assumption in the existing theory "is essential or merely an artifact". For convex objectives, when polling directions satisfy a probabilistic *ascent* condition, non-convergence has positive probability. For uniform random directions on the sphere, fewer directions than the theory's threshold means the method is **not** globally convergent. So the assumption is essential.
- **Implication**: the GRVZ threshold is sharp, which validates the theory. It is also a hard limit: "use 1 random direction to save evaluations" is unsafe; the direction count must meet the probabilistic-descent threshold.
- Source: https://arxiv.org/abs/2606.01320 (secondary, peer)

## C3 · Competing globalization school: mesh / integer lattice (Audet–Dennis MADS line)

- **Evidence**: Audet, Dennis & Le Digabel, "Globalization strategies for Mesh Adaptive Direct Search", COAP 46 (2010) 193–215, DOI 10.1007/s10589-009-9266-1. The search summary says the convergence theory "does not enforce a notion of sufficient decrease" because iterates lie on a scaled, translated integer lattice.
- **Contrast with Vicente**: Vicente's line relies on sufficient decrease (a forcing function ρ(α)) and needs no mesh. That choice is what makes iteration counting possible (Vicente 2013 abstract: "based on imposing sufficient decrease"). The MADS line keeps simple decrease and mesh structure, which is natural for discrete or granular variables and for the progressive-barrier constraint handling of that school.
- **Where they collide**: multiobjective (DMS 2011 vs DMulti-MADS, COAP 2021, which reports Δ-spread profiles comparing BiMADS, DMS, DMulti-MADS, MOIF, NSGA-II per search summary), constraints (merit function + extreme barrier in Gratton & Vicente 2014 vs progressive barrier in MADS), and discontinuous analysis (C1).
- Sources: https://link.springer.com/article/10.1007/s10589-009-9266-1 ; https://link.springer.com/article/10.1007/s10589-021-00272-9 (primary for the other school)

## C4 · Intrinsic limits stated in Vicente's own work

| Limit | Source |
|---|---|
| Worst-case evaluation complexity of directional DS is O(n²ε⁻²), and the n² factor is **optimal** for this class, so direct search is intrinsically dimension-hungry | Dodangeh, Vicente & Zhang 2016, https://link.springer.com/article/10.1007/s11590-015-0908-1 |
| Nonsmooth via smoothing costs "roughly one order of magnitude" in complexity | Garmanjani & Vicente 2013 |
| Pareto-sensitivity knees need scalarization and 1st/2nd derivatives | arXiv:2501.16993 |
| Non-monotone acceptance makes analysis "significantly more challenging" | arXiv:2609.11567 |
| SMG multi-gradient direction is **biased** even with unbiased per-objective gradients | Liu & Vicente 2021, arXiv:1907.04472 |

## C5 · Competing approach: model-based trust-region DFO (Powell / Conn–Scheinberg lineage)

- The 2009 book itself treats model-based methods (interpolation, geometry control) as the second main framework alongside direct search (book description). Vicente works on both. Vicente's *own* direct-search papers import models only into the **search step** (SID-PSM 2007, MFN 2010), where the poll step carries convergence. The model-based school makes model quality and geometry management the core of the algorithm.
- Vicente's probabilistic-model TR work (2014, 2018) relaxes the deterministic "fully linear every iteration" requirement of the classical model-based theory to a probabilistic one. That is a methodological departure from deterministic geometry control.
- Contradictory evidence about neural or learned surrogates in DFO exists (Bian & Xie, arXiv:2608.24963, 2026, not about Vicente). It is relevant because Vicente's rule of keeping the true function as the acceptance judge ("a surrogate that proposes candidates the true objective must still approve helps", Bian & Xie's finding) is consistent with the search/poll separation. This is an inference linking two sources.

## C6 · Gaps in the critique record

- No published rebuttal or response by Vicente to C1 was found.
- No public review reports or OpenReview threads (the optimization journals Vicente publishes in do not have open review).
- No critique found of the DMS benchmarking metrics or of the Lehigh-era fairness formulation. Absence of evidence, not evidence of absence.
