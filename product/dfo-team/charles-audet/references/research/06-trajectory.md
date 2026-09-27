# 06 · Research trajectory

Sources: group bibliography (primary, [B]) — https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib ; search snippets ([S]); NOMAD user guide (primary). Dates are publication years. "Trigger" columns are **inferences** unless a source is given.

---

## 1. Timeline

| Period | Direction | Representative work | Trigger / context |
|---|---|---|---|
| 1997–2002 | Exact global optimization: linear bilevel ↔ mixed 0–1 (JOTA 1997), disjoint bilinear programming (Math. Prog. 1999), branch-and-cut for nonconvex QCQP (Math. Prog. 2000), enumeration of all extreme equilibria of bimatrix games (SISC 2001) | with Hansen, Jaumard, Savard at GERAD [B] | GERAD global-optimization school. PhD at École Polytechnique de Montréal [S, GERAD profile] |
| ~2000–2001 | Move to derivative-free: mixed-variable pattern search (SIAM J. Optim. 2001), surrogate-based constrained optimization (AIAA 2000), thermal-insulation application (Optim. Eng. 2001) | with Dennis (Rice), Booker, Frank, Kokkolaras [B] | Post-doc at Rice University [S, GERAD profile]. Engineering-design needs (surrogates, categorical choices) |
| 2003–2009 | **Theory-building era**: GPS analysis (2003), tightness counterexamples (2004), filter GPS (2004), GPS with derivative info (2004), MADS (2006), second-order MADS (2006), algorithm-parameter tuning with Orban (2006), erratum (2008), PSD-MADS (2008), BiMADS (2008), OrthoMADS (2009), progressive barrier (2009) | mostly SIAM J. Optim. [S+B] | Clarke-calculus analysis of pattern search. NOMAD 1–2 then NOMAD 3 (2008) funded by AFOSR and ExxonMobil (user guide) |
| 2002–2013 (parallel line) | Extremal problems for small polygons (largest small octagon, JCTA 2002; Vincze's wife's octagon is suboptimal, JCTA 2004; perimeter/width/diameter problems, DCG 2009, 2013) | with Hansen, Messine, Ninin [B] | Exact global optimization with a clean, provable answer. A continuing taste for crisp mathematics |
| 2010–2016 | **Applications and engineering the method**: snow water, alloys, metamaterials, bioinformatics, hydropower; OPAL; trade-off studies (2012); fewer evaluations via quadratic models (2014); survey of direct search with applications (2014); linear equalities (2015); dynamic scaling (2016); editorial (2016) | with Le Digabel, Tribes, Alarie, Gheribi, Côté [B] | NOMAD 3 in use by industry; GERAD industrial partners |
| 2017–2022 | **Consolidation**: textbook with Hare (2017); surrogates ensembles, mesh-based Nelder–Mead, PB trust-region with Conn (2018); granular variables (2019); hidden/binary constraints, monotonic grey box (2020); StoMADS, adaptive precision, two decades of applications, performance indicators (2021); NOMAD 4, discontinuities, hierarchical constraints, COCO/GECCO (2022) | [S+B] | NOMAD 4 funded by Huawei Canada, Rio Tinto, Hydro-Québec, NSERC, InnovÉÉ, IVADO (user guide). ML hyperparameter demand (HyperNOMAD) |
| 2023–2026 | **Mixed variables, benchmarks, rethinking the mesh**: meta/categorical framework (2023) → distance (2025) → Cat-Suite and CatMADS (2025/26); counterexample note (2024); covering step (2025); SOLAR (2024/25); Inter-DS multi-fidelity (2025); ADS (2025) and ADS-PB (2026); Mads-PIP (2026); bilevel DFO benchmarking (2026); partitioned structure-aware framework (JOTA 2026); Micro-PRIAD (2026); textbook 2nd ed. (2026) | with Diouane, Hallé-Hannan, Bouchet, Bourdin, Lebeuf, Diago [S+B] | Hydro-Québec energy-systems grant (SOLAR); categorical/ML use cases; Diouane joins as a frequent co-author |

## 2. Pivots and their (inferred) causes

1. **Global/bilevel → blackbox direct search (c. 2000).** Coincides with the Rice post-doc with Dennis and the AIAA 2000 surrogate paper (co-authors Booker, Frank, Moore; affiliation ⚠️ unverified). Inference: exposure to engineering simulation problems where structure (bilinear/bilevel) is unavailable.
2. **Theory → applications + software (c. 2008–2010).** Coincides with Le Digabel's PhD (2008) and the NOMAD 3 release (2008). The team gained software capacity, and industrial users followed.
3. **Default mesh → questioning the mesh (2025–2026).** ADS replaces the mesh with a "punctured space". The flagship concept is being reconsidered by its own authors.
4. **Back to bilevel (2026).** *Benchmarking bilevel derivative-free optimization algorithms* (with Dijon, Diouane; arXiv 2605.30531) returns to the PhD-era problem class, now in the blackbox setting. (Inference: full circle. The paper was not read.)

## 3. Latest 12 months (approx. Sept 2025 – Sept 2026)

| Date | Item | ID | Status |
|---|---|---|---|
| 2026 (Jan) | *A penalty-interior point method combined with MADS for equality and inequality constrained optimization* (Audet, Brilli, Diouane, Le Digabel, Silva, Tribes). Now Mads-PIP in NOMAD; EQPB constraints "Since version 4.6" | arXiv 2601.20811 | [S+B] |
| 2026 (Jan) | *Multi-fidelity constraints in blackbox optimization* (Alarie, Audet, Diago, Le Digabel, Lebeuf) | arXiv 2601.06321; G-2026-01 | [B] |
| 2026 (Mar) | *Surrogate-based categorical neighborhoods for mixed-variable blackbox optimization* (Audet, Diouane, Hallé-Hannan, Le Digabel, Tribes); repo `bbopt/surrogate_based_neighborhoods` | arXiv 2603.27839; G-2026-16 | [B] |
| 2026 | *CatMADS: MADS for constrained blackbox optimization with categorical variables* (G-2025-42; arXiv 2506.06937) — NomadBBO Python version announced | arXiv 2506.06937 | [B] |
| 2026 (May) | *Benchmarking bilevel derivative-free optimization algorithms* (Audet, Dijon, Diouane) | arXiv 2605.30531; G-2026-26 | [B] |
| 2026 (Jun) | Audet & Hare, *Derivative-Free and Blackbox Optimization*, **2nd edition** (eBook 17 June 2026). Chapters include "Introduction: Tools and Challenges…", "The Beginnings of DFO Algorithms", "Comparing Optimization Methods", "Nelder-Mead", "Assessing Model Quality", "Biobjective Optimization" | 10.1007/978-3-032-00906-7 | [S+B] |
| 2026 (Jul) | *Adaptive direct search algorithms with relaxable and quantifiable constraints* (ADS-PB) | arXiv 2607.05183 | [S+B] |
| 2026 | *A summary of benchmarking constrained, multi-objective and surrogate-assisted optimization methods* (Audet, Hare, Tribes), Optim. Lett. | 10.1007/s11590-026-02302-z | [S+B] |
| 2026 | *A partitioned optimization framework for structure-aware problems* (Audet, Bouchet, Bourdin), JOTA 210(1):9 | 10.1007/s10957-026-03042-x | [B] |
| 2026 (Aug) | Micro-PRIAD v1.0: stochastic power-utility maintenance blackbox collection (Gentile, Lebeuf, Le Digabel, Audet, Diago) | https://github.com/bbopt/Micro-PRIAD | [B] + README |
| 2025 (late) | *Benchmarking DFO solvers for CSP plant design using the SOLAR simulator* (G-2025-70) | GERAD | [B] |
| Related, not Audet | *Parallel versions of the mesh adaptive direct search algorithm* (Le Digabel, Lesage-Landry, Mendoza, Tribes, arXiv 2607.08872, July 2026). Same group, without Audet | arXiv 2607.08872 | [S] |

Direction of travel (inference): (i) constraints richer than inequalities (equalities, relaxable/quantifiable, multi-fidelity); (ii) categorical and structured variables; (iii) benchmark infrastructure and benchmarking papers as first-class outputs; (iv) leaving the mesh behind while keeping directional direct-search theory.

## 4. Lineage (compact)
- Upstream: GERAD global-optimization school (Hansen, Jaumard, Savard); J.E. Dennis Jr. (Rice) for pattern search. Formal PhD advisor ⚠️ not verified.
- Peers and co-leads: Le Digabel, Tribes, Hare, Kokkolaras, Orban, Diouane.
- Downstream (co-authoring students; supervision role not verified): Le Digabel (PhD 2008), Peyrega, Amaioua, Dzahini, Lakhmiri, Salomon (PhDs); Bouchet, Hallé-Hannan, Lebeuf, Ihaddadene, Béchard, Lemyre Garneau (MScs).

## Source IDs (primary unless noted)
- Early global optimization: JOTA 1997 https://doi.org/10.1023/A:1022645805569 ; Math. Program. 1999 https://doi.org/10.1007/s101070050072 ; Math. Program. 2000 https://doi.org/10.1007/s101079900106
- Mixed-variable pattern search (2001): https://doi.org/10.1137/S1052623499352024 ; thermal insulation (2001): https://doi.org/10.1023/A:1011860702585
- GPS analysis (2003): https://doi.org/10.1137/S1052623400378742 ; tightness (2004): https://doi.org/10.1023/B:OPTE.0000033370.66768.a9 ; MADS (2006): https://doi.org/10.1137/040603371 ; PB (2009): https://doi.org/10.1137/070692662 ; OrthoMADS (2009): https://doi.org/10.1137/080716980
- Polygons: DCG 2009 https://doi.org/10.1007/s00454-008-9093-7 ; DCG 2013 https://doi.org/10.1007/s00454-013-9489-x
- Trade-off studies (2012): https://doi.org/10.1080/10556788.2011.571687 ; fewer evaluations (2014): https://doi.org/10.1137/120895056 ; survey (2014): https://doi.org/10.1007/978-1-4939-1124-0_2
- Textbook: https://doi.org/10.1007/978-3-319-68913-5 (2017) ; https://doi.org/10.1007/978-3-032-00906-7 (2026)
- NOMAD 4 (2022): https://doi.org/10.1145/3544489 ; discontinuities (2022): https://doi.org/10.1137/21M1420915 ; hierarchical constraints (2022): https://doi.org/10.1016/j.orl.2022.06.006
- Recent: arXiv:2507.23054 ; arXiv:2607.05183 ; arXiv:2601.20811 ; arXiv:2601.06321 ; arXiv:2603.27839 ; arXiv:2605.30531 ; arXiv:2506.06937 ; https://doi.org/10.1007/s11590-026-02302-z ; https://doi.org/10.1007/s10957-026-03042-x
- GERAD profile (secondary): https://www.gerad.ca/en/people/charles-audet ; NOMAD funding and authorship (primary): https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst
