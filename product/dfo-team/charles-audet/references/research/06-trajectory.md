# 06 · Research trajectory

Sources: group bibliography (primary, [B]) — https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib ; search snippets ([S]); NOMAD user guide (primary). Dates are publication years. "Trigger" columns are **inferences** unless a source is given.

**Update 2026-09-27 (full-text reading).** §§1–4 are the first-pass trajectory, kept as written. §5 revises it from the paper cards (`07-paper-cards.md`; aggregation in `08-deep-reading-synthesis.md` §8–9). Where they differ, §5 and `SKILL.md` (Research Trajectory) are current. Card citations are written [S### p. N].

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
- Upstream: GERAD global-optimization school (Hansen, Jaumard, Savard); J.E. Dennis Jr. (Rice) for pattern search. Formal PhD advisor ⚠️ not verified. **Resolved (full text):** B. Jaumard (*directrice de recherche*) and G. Savard (*codirecteur*), thesis of November 1997 [S070 pp. 1–3].
- Peers and co-leads: Le Digabel, Tribes, Hare, Kokkolaras, Orban, Diouane.
- Downstream (co-authoring students; supervision role not verified): Le Digabel (PhD 2008), Peyrega, Amaioua, Dzahini, Lakhmiri, Salomon (PhDs); Bouchet, Hallé-Hannan, Lebeuf, Ihaddadene, Béchard, Lemyre Garneau (MScs). Added from the full texts: M. A. Abramson (Rice PhD 2002), committee co-chaired by Dennis and Audet [S213 pp. 1, 5].

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

## 5. Trajectory from the full texts (2026-09-27)

### 5.1 Corrected timeline

| Period | Direction | Evidence | Change from §1 |
|---|---|---|---|
| 1994–1998 | Exact global optimization: the thesis links structured classes (mixed 0–1, disjoint bilinear, concave QP, QQP, GLCP, linear maxmin, bilevel) by proven reformulations and ports tests across them | Thesis, November 1997, directed by B. Jaumard and G. Savard [S070 pp. 1–3, 33–34, 174] | Start moved to the thesis; advisor resolved |
| 1998–2004 (parallel) | Exact QCQP branch-and-cut, pooling and fractional programming continue after the move to DFO | Rice CRPC report of January 1999 [S010 pp. 1–2]; Ultramar-funded pooling work [S015 p. 15]; [S098] | New row: the exact line did not stop in 2000 |
| November 1998–2002 | Move to derivative-free pattern search: the tightness report probes Torczon's 1997 theorems, then mixed variables and the GPS analysis | CRPC-TR98779, 17 November 1998, at the start of an NSERC postdoc [S025 TR pp. 1–3]; cited by [S002 pp. 3, 14] and [S011 pp. 15, 22] | Start moved from "~2000" to November 1998 |
| 2003–2009 | Theory building: filter, MADS, second order, OrthoMADS, PSD-MADS, BiMADS, progressive barrier | The fixed-direction limitation of GPS is stated as the research problem [D016 p. 4; S005 pp. 1–2; S001 p. 1] | Trigger now stated, not inferred |
| 1997–2022 (parallel) | Extremal small polygons and other exact mathematics (side line), from Graham's octagon in the thesis to certified results in 2022 | [S070 pp. 166–171; S037; S040; S117; S113 pp. 1–2; S142 p. 9; D003 pp. 5–7] | Extended from "2002–2013" |
| 1998–2014 (parallel) | Enumeration and refinement of game equilibria | [S048; S076; D002; S134 pp. 1, 13] | New row |
| about 2010–2016 | Applications with partners and adoption of NOMAD | Hydro-Québec [S204; S074], thermochemistry [S042 abstract; S013], genetics [S066], algorithm tuning [S057; S059] | Partners are named coauthors, not only funders [S123 p. 1; S032; S013 pp. 4–7] |
| 2015–2022 | Consolidation: surrogates managed by order error, noise, hidden constraints and discontinuities, multiobjective indicators, NOMAD 4 | [S046; S068; S114; S053; S084; S072; S090; S138; S004; S021] | Order-error surrogate management added |
| 2025–2026 | Benchmarks as outputs (five benchmark or benchmarking works in two years, plus bilevel benchmarking), the mesh relaxed (ADS), categorical variables, equalities, multi-fidelity, covering and partition theory | [S071; S130; S175; D006; S101/S128; S156]; [S129 p. 1; S172 p. 3]; [S121; S157; S158; S112; S173; S137; S155] | Diouane as co-lead of the algorithm papers [S121; S129; S156; S157; S158; S172] |

### 5.2 Turns

1. **Late 1998: from exact global optimization to pattern search.** The thesis links structured classes by proven reformulations [S070 pp. 33, 174]. Within a year the Rice report probes Torczon's theorems [S025 TR pp. 1–3], while exact QCQP and pooling work continue until 2004 [S010; S015; S098].
2. **2004–2009: finite directions give way to dense directions, and the filter to the progressive barrier.** The GPS limitation is stated [D016 p. 4; S005 pp. 1–2]; MADS decouples mesh and poll [S001 p. 4]; OrthoMADS removes the randomness [S006 p. 1]; PB replaces the filter mechanism while keeping dominance [S007 p. 3].
3. **About 2010: partners and NOMAD.** Hydro-Québec [S204; S074], genetics [S066], algorithm tuning [S057; S059].
4. **2015–2022: consolidation.** Order-error surrogate management [S046; S068; S114], noise [S053; S084], hidden constraints and discontinuities [S072; S090; S138], indicator audits [S004], the NOMAD 4 rewrite [S021].
5. **2025–2026: benchmarks as outputs, and the mesh relaxed.** Five benchmark or benchmarking works in two years [S071; S130; S175; D006; S101/S128] plus bilevel benchmarking [S156]; the group that made the mesh central proposes mesh-free ADS [S129 p. 1; S172 p. 3]; categorical [S121; S157], equalities [S158], multi-fidelity [S112; S173], covering and partition theory [S137; S155].

### 5.3 What stayed constant and what moved

- **Constant**: the Clarke-calculus ladder from 1998 to 2026 [S002 p. 12; S001 pp. 11–13; S007 pp. 24–25; S129 pp. 13–14; S172 pp. 14–15; S158 pp. 16–18]; inheritance as the way new methods get theory (SKILL.md Method 7, 2001–2026); constraint semantics, from the closed/open split [S007 p. 2] to cost-aware assignment [S173 p. 5]; the same testbeds for seventeen years (STYRENE released in 2009 [S007 p. 31], run again in 2026 [S172 p. 18]); a taste for exact or certified answers in the side line [S070 pp. 166–171; S142; D003].
- **Moved**: the counterexample craft, from GPS theory (1998–2009) to algorithm-design toys [S129; S172], measuring instruments [S004] and benchmark referees [S156]; the currency, from CPU time in the exact era [S015; S070] to evaluations [S001; S128] and then to explicitly weighted effort [S155; S156; D006].

### 5.4 Collaboration by era (from `08-deep-reading-synthesis.md` §9)

- The GERAD school (Hansen, Jaumard, Savard) until about 2011, with Hansen continuing in the geometry side line to 2021 [S094]; Rice (Dennis, Abramson) from 1999 to about 2012; geometry (Messine, Perron, Ninin, Bingane) from 2002 to 2025; the NOMAD core (Le Digabel from 2004, Tribes from 2009) throughout the DFO period; Diouane from 2025.
- Sole-authored work is exposition, notes and puzzles (surveys, the French textbook, short notes, puzzles); the 1998 report [S025] is the only sole-authored theory work.
- The late papers are student-led: Hallé-Hannan [S121 p. 1; S157], Brilli [S158 p. 1], Lebeuf [S173 p. 1], Bouchet [S151; S155], Kojtych [S107; S184], Bingane [S113; S142], and the Couderc line [S140; S150].

### 5.5 Pivots of §2 revisited

- Pivot 1 (global/bilevel → blackbox direct search, "c. 2000"): the date moves to November 1998 [S025 TR p. 2]; the inferred cause (exposure to engineering problems without exploitable structure) is not stated in any card, but the AFOSR report shows the engineering-surrogate context from December 2000 [D016 p. 1].
- Pivot 3 (default mesh → questioning the mesh): confirmed and sharpened; ADS proves OrthoMADS an instance of its mesh-free class [S129 pp. 16–19].
- Pivot 4 (back to bilevel, 2026): the bilevel benchmarking paper was read in full [S156]; its link to the thesis-era bilevel work remains an inference.

