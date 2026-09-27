# 01 · Publications: Landscape and Signature-Work Anatomy (Vicente)

> Research date: 2026-09-27. Built from web-search result snippets (Springer/SIAM/T&F landing pages, arXiv/Optimization Online listings, author PDFs on mat.uc.pt, Semantic Scholar, ResearchGate). **No full texts were read**: WebFetch was blocked for every host tried (coral.ise.lehigh.edu, mat.uc.pt, wikipedia, mathgenealogy, optimization-online, springer, lehigh.edu, pitt.edu), and `scripts/fetch_publications.py` (OpenAlex) cannot run here. Only papers whose title + authors + year (+ venue) appeared in a search result are listed as ✅. Credibility: journal landing pages and author-hosted PDFs = primary; search-engine summaries of them = primary content relayed second-hand.

> **Update 2026-09-27 (full-text pass).** The note above describes the first pass only. The complete publication list has since been harvested from the Google Scholar profile and cross-checked against DBLP, Crossref, arXiv and the author's paper pages (`../sources/publications/scholar.md`, `works.json`), and every work has a paper card (`07-paper-cards.md`; synthesis in `08-deep-reading-synthesis.md`). §0 below gives the coverage; §1–§2 are kept as written in the first pass, with corrections marked **[full text]**. Method numbers in §2 follow an early draft in which "Method 4" and "Method 5" were swapped relative to SKILL.md (SKILL.md: Method 4 = generalize the acceptance test, Method 5 = ship and profile); SKILL.md's numbering is authoritative.

## 0. Coverage from the Google Scholar list (full-text pass)

Source list: Google Scholar profile https://scholar.google.com/citations?user=TLkN5_AAAAAJ, harvested and audited 2026-09-27 (`../sources/publications/scholar.md`). Ids: S### = Scholar row (by citations), D### = DBLP-only, H### = author homepage only.

| Item | Count |
|---|---|
| Scholar rows | 122 (7 duplicates merged → 115 distinct works) |
| DBLP-only / homepage-only works | 1 (D001) / 8 (H001–H008) |
| Distinct works | 124: 88 journal articles, 9 preprints, 7 conference papers, 5 chapters, 3 reports, 2 books, 1 thesis, 9 other |
| With DOI / with arXiv id | 96 / 24 |
| Open full text found (`../sources/papers/INDEX.md`) | 108 (`txt`); 16 `no-oa` |
| Read levels (`07-paper-cards.md`) | 92 full, 16 partial, 11 abstract-level, 5 metadata-only, 0 skipped |

Read levels by period (08 §1):

| Period | full | partial | abstract | metadata | total |
|---|---|---|---|---|---|
| 1991–1995 | 4 | 0 | 7 | 1 | 12 |
| 1996–2000 | 12 | 1 | 1 | 2 | 16 |
| 2001–2005 | 9 | 4 | 0 | 0 | 13 |
| 2006–2010 | 14 | 1 | 2 | 0 | 17 |
| 2011–2015 | 18 | 2 | 0 | 2 | 22 |
| 2016–2020 | 10 | 7 | 0 | 0 | 17 |
| 2021–2026 | 24 | 1 | 1 | 0 | 26 |
| undated (S120) | 1 | 0 | 0 | 0 | 1 |

Most-cited works on the profile: the 2009 DFO book [S001] (2876; abstract-level only, no open text), the bilevel bibliography [S002] (930), DMS [S003] (540), descent approaches for quadratic bilevel programming [S004] (483; abstract only), PSwarm [S005] (460), DFO trust-region convergence [S006] (321), the primal-dual interior-point filter method [S007] (313), SID-PSM ordering [S008] (240), discrete linear bilevel programming [S009] (225; abstract only), geometry of interpolation sets [S010] (210).

Topic tags by period (a work can carry two; BIL = bilevel/complementarity/global QP, TPG = test-problem generators, NLP = derivative-based NLP, DS = direct search, MB = model-based DFO and surrogates, WCC = worst-case complexity, PROB = probabilistic/stochastic DFO, MOO = multiobjective, SML = stochastic gradient methods for ML, APP = application, SUR = survey/book/service; 08 §8):

| Period | BIL | TPG | NLP | DS | MB | WCC | PROB | MOO | SML | APP | SUR | works |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1991–1995 | 9 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 12 |
| 1996–2000 | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 16 |
| 2001–2005 | 1 | 0 | 6 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 3 | 13 |
| 2006–2010 | 1 | 0 | 2 | 7 | 5 | 0 | 0 | 1 | 0 | 2 | 3 | 17 |
| 2011–2015 | 1 | 0 | 2 | 6 | 5 | 3 | 2 | 2 | 0 | 4 | 2 | 22 |
| 2016–2020 | 0 | 0 | 2 | 3 | 2 | 8 | 3 | 2 | 0 | 4 | 2 | 17 |
| 2021–2026 | 3 | 0 | 2 | 3 | 3 | 0 | 3 | 9 | 12 | 4 | 2 | 26 |

Direction map additions from the full list (not in §1a):
- **1991–1995: bilevel programming and test-problem generators** (Coimbra, Waterloo, GERAD; Calamai, Júdice): bibliography [S002], generators with known minima [S053; S026; D001; S033; S063], descent methods and NP-hardness results [S004; S069] (abstract level), optimality conditions [S052].
- **Derivative-based NLP runs 1996–2008**, not only the PhD: TRIP SQP [S011; S037; S031], inexact SQP [S013], interior-point and filter methods [S007; S077; S085], local analyses [S084; S054; S095; S098].
- **Direct search enters in 2001 through an application** (pattern search for user-provided points, molecular geometry) [S106; S025], before SID-PSM and PSwarm (2007).
- **Model geometry with Conn and Scheinberg, 2008–2009** [S010; S020; S006], contemporary with the book [S001].
- **Applications throughout**: circuits [S039], molecules [S106; S025], finance [S028; S087; S061], astrophysics [S075; S082], geophysics [S068], medicine [S035], manufacturing [S036; S078], transport [S080], sports analytics [S086; S092; S120].
- **Authorship**: 13 single-authored research works, 11 of them in 1991–2005 and the last in 2013 [S023]; junior coauthors (students, postdocs) appear in every period, and long pairings of 5–15 years carry each line of work (08 §9).

Attribution notes: S029 is joint with Bandeira and Scheinberg; S056 counts only for Vicente's §2.1 (PDF pp. 7–9); S121/S122 are SIAG/OPT Views and News issues of which only the Chair's Columns are his; S113 is a talk deck presented by his student Suyun Liu; S040 is his 1996 PhD thesis.

## 1. Publication landscape (hand-built, verified items only)

### 1a. Direction map

| Cluster | Period | Verified representative items | Co-author pattern |
|---|---|---|---|
| Derivative-based NLP (PhD roots) | 1990–1996 | PhD thesis "Trust-Region Interior-Point Algorithms for a Class of Nonlinear Programming Problems", Rice 1996, advisor John Dennis (Wikipedia via search, secondary) | advisor |
| Direct search made efficient: reuse of samples, models in the search step | 2007–2010 | Custódio & Vicente, SIAM J. Optim. 18 (2007) 537–555; Custódio, Rocha & Vicente, COAP 46 (2010) 265–278, DOI 10.1007/s10589-009-9283-0; Vaz & Vicente, J. Glob. Optim. 39 (2007) 197–219, DOI 10.1007/s10898-007-9133-5 | PhD student (Custódio), Coimbra/Minho colleagues (Vaz, Rocha) |
| Synthesis / textbook | 2009, 2017 | Conn, Scheinberg & Vicente, *Introduction to Derivative-Free Optimization*, MPS-SIAM Series on Optimization, SIAM 2009 (DOI 10.1137/1.9780898718768); Custódio, Scheinberg & Vicente, "Methodologies and software for derivative-free optimization", Ch. 37 in *Advances and Trends in Optimization with Engineering Applications*, SIAM 2017, pp. 495–506 | senior peers |
| Multiobjective direct search | 2011 → | Custódio, Madeira, Vaz & Vicente, "Direct multisearch for multiobjective optimization", SIAM J. Optim. 21(3) (2011) 1109–1140, DOI 10.1137/10079731X | former student + engineering colleagues |
| Nonsmooth / discontinuous / constrained direct search | 2012–2014 | Vicente & Custódio, Math. Program. 133 (2012) 299–325, DOI 10.1007/s10107-010-0429-8; Garmanjani & Vicente, IMA J. Numer. Anal. 33 (2013) 1008–1028; Gratton & Vicente, "A merit function approach for direct search", SIAM J. Optim. 24(4) (2014) 1980–1998 | students + Gratton (Toulouse) |
| Worst-case complexity of direct search | 2013–2016 | Vicente, EURO J. Comput. Optim. 1 (2013) 143–153, DOI 10.1007/s13675-012-0003-7; Dodangeh & Vicente, Math. Program. 155 (2016) 307–332, DOI 10.1007/s10107-014-0847-0; Dodangeh, Vicente & Zhang, Optim. Lett. 10 (2016) 699–708, DOI 10.1007/s11590-015-0908-1 | single-author opener, then students |
| Model-based DFO with sparsity | 2012 | Bandeira, Scheinberg & Vicente, Math. Program. 134 (2012) 223–257, DOI 10.1007/s10107-012-0578-z (arXiv:1306.5729) | young co-author + Scheinberg |
| Probabilistic / randomized methods | 2014–2019 | Bandeira, Scheinberg & Vicente, SIAM J. Optim. 24(3) (2014) 1238–1264; Gratton, Royer, Vicente & Zhang, SIAM J. Optim. 25(3) (2015) 1515–1541; same four, IMA J. Numer. Anal. 38(3) (2018) 1579–1597, DOI 10.1093/imanum/drx043; same four, COAP 72 (2019) 525–559, DOI 10.1007/s10589-019-00062-4 | Toulouse co-advised PhD (Royer) + Gratton + Zhang |
| Evolution strategies made globally convergent | 2015 | Diouane, Gratton & Vicente, Math. Program. 152 (2015) 467–490, DOI 10.1007/s10107-014-0793-x; constrained version COAP 2015, DOI 10.1007/s10589-015-9747-3 | Toulouse co-advised PhD (Diouane) |
| Lehigh era: stochastic multi-objective & ML | 2019 → | Liu & Vicente, Ann. Oper. Res. 2021, DOI 10.1007/s10479-021-04033-z (arXiv:1907.04472); Liu & Vicente, Comput. Manag. Sci. 19(3) (2022) 513–537, DOI 10.1007/s10287-022-00425-z (arXiv:2008.01132) | Lehigh PhD student (Liu) |
| Lehigh era: bilevel | 2021 → | Giovannelli, Kent & Vicente, J. Glob. Optim. 2025, DOI 10.1007/s10898-025-01502-8 (arXiv:2110.00604); Giovannelli, Kent & Vicente, Optim. Methods Softw. 39(4) (2024) 756–778, DOI 10.1080/10556788.2024.2318707 (arXiv:2302.05540) | postdoc/student team |
| Lehigh era: DFO with noise and full/low evaluation | 2021 → | Berahas, Sohab & Vicente, "Full-low evaluation methods for derivative-free optimization", Optim. Methods Softw. 38(2) (2023) 386–411, DOI 10.1080/10556788.2022.2142582 (arXiv:2107.11908); Rinaldi, Vicente & Zeffiro, SIAM J. Optim. 34 (2024) 2067–2092, DOI 10.1137/22M1543446 (arXiv:2202.11074); Ding, Rinaldi & Vicente, arXiv:2509.14505 (2025); Ding, Tran & Vicente, arXiv:2609.11567 (2026) | Lehigh students/postdocs + Rinaldi (Padova) |
| Lehigh era: Pareto analysis | 2025 → | Giovannelli, Raimundo & Vicente, "Pareto sensitivity, most-changing sub-fronts, and knee solutions", arXiv:2501.16993 (v1 Jan 2025, v3 Mar 2026); Tran & Vicente, arXiv:2605.12432 (May 2026) | postdocs |

### 1b. Observations on the landscape (inferences, marked)

- **Venue pattern (practice)**: SIAM J. Optim. is the home venue for framework-defining work (2007, 2011, 2014 ×2, 2015, 2024); Math. Programming for theory extensions (2012, 2015, 2016); COAP / Optim. Methods Softw. for software-flavoured or extension papers; EURO J. Comput. Optim. for the short complexity note (2013).
- **Author position (practice)**: Vicente appears first author on only a few verified items (2012 discontinuous; 2013 single-author complexity). The typical pattern is student/postdoc first, Vicente last. *Inference*: from ~2007 onward the operating mode is supervision-driven research programmes.
- **Mode of expansion (inference)**: each cluster opens with a framework paper, is followed within 1–4 years by constrained / convex / second-order / multiobjective extensions, often by the same team (e.g., probabilistic descent 2015 → IMA 2018 → constrained COAP 2019).
- **Pivot (practice)**: after the 2018 move to Lehigh, gradient-based stochastic multi-objective and bilevel methods for ML appear alongside continued DFO work. The SIAM Fellow citation (2024) names "derivative-free and bilevel optimization" (Lehigh news via search).

## 2. Signature-work anatomy (4 works)

Rule: "Origin" and "Abandoned paths" without a first-hand source are marked **(speculation)**.

### 2.1 "Using sampling and simplex derivatives in pattern search methods" (Custódio & Vicente, SIAM J. Optim. 18 (2007) 537–555) + SID-PSM software

| Dimension | Content |
|---|---|
| Origin | Custódio's PhD, "Applications of Simplex Derivatives to Direct Search Methods" (Coimbra, 2007, advisor Vicente; search result, secondary). Problem: pattern search wastes the function values it has already computed. |
| Why then | Pattern search had a mature global convergence theory (generalized pattern search). Simplex-gradient ideas existed, but using them to guide polling inside a provably convergent method was open. **(speculation, based on the abstract's framing)** |
| Key insight | Reuse previously evaluated points. When a sample set with good geometry exists, compute a simplex gradient/Hessian and use it to order the poll and to build quadratic models for the search step, while keeping the pattern-search convergence theory intact. |
| Minimal evidence | Numerical comparison of the enhanced pattern search against plain pattern search, packaged as SID-PSM (MATLAB). Paper abstract via search. |
| Abandoned paths | Unknown. |
| Reception | Widely cited (search summary). The SID-PSM software was maintained to v1.3 (Dec 2014) under LGPL (mat.uc.pt/sid-psm, primary). |
| Methods shown | Method 1 (heuristic inside a convergent skeleton), Method 4 (software and profiles) |
| **[full text]** corrections | The paper's entry point is an observed L-shaped f-vs-evaluations curve [S008 p. 1]. The glue is the rational-lattice mesh with simple decrease; sufficient decrease appears only in the mesh-expansion rule [S008 pp. 3–4, 14]. The model-based search step is deferred to "separate research" [S008 p. 13]; the MFN search step and the name SID-PSM come in the 2008 manual and the 2010 paper [S059 pp. 1–7; S012 pp. 6–8]. Evidence: 27 CUTEr problems, aggregate tables, −51% evaluations for simplex-gradient ordering [S008 pp. 14–17]. |

### 2.2 "Direct multisearch for multiobjective optimization" (Custódio, Madeira, Vaz & Vicente, SIAM J. Optim. 2011, DOI 10.1137/10079731X)

| Dimension | Content |
|---|---|
| Origin | Extension of the directional direct-search search/poll paradigm to several objectives without scalarization (abstract). The co-author mix (engineering + optimization) suggests the problem came from engineering applications **(speculation)**. |
| Why then | Single-objective direct-search theory (SID-PSM era) and a reusable collection of test problems were in hand. Many multiobjective DFO methods of the day aggregated objectives **(speculation, framed by the abstract's "does not aggregate")**. |
| Key insight | Replace "the incumbent point" by a list of nondominated points and replace "decrease" by Pareto dominance. The search/poll skeleton and step-size logic carry over. |
| Minimal evidence | Performance profiles based on purity and the spread metrics Γ and Δ over 100 AMPL multiobjective problems (69 with 2 objectives, 29 with 3, 2 with 4) (search summary of the paper PDF). |
| **[full text]** correction | Table 5.1 of the paper gives **69 bi-objective, 30 tri-objective and 1 four-objective problem (FES3)** [S003 p. 16]. The engineering-motivation speculation is not confirmed; the stated motivation is the drawbacks of a-priori aggregation [S003 p. 2]. |
| Abandoned paths | Unknown. An **errata** is posted with the paper on the DMS website (search result), so at least one published detail needed correction. |
| Reception | Many follow-ups by others: DMulti-MADS (mesh-adaptive direct multisearch, COAP 2021), adaptive DMS, polynomial models in the DMS search step (2026 arXiv), first-order DMS (search results). |
| Methods shown | Method 5 (generalize the acceptance test), Method 4 (profiles, new metrics, software) |

### 2.3 "Worst case complexity of direct search" (Vicente, EURO J. Comput. Optim. 1 (2013) 143–153, DOI 10.1007/s13675-012-0003-7)

| Dimension | Content |
|---|---|
| Origin | Complexity bounds had become central for derivative-based methods. This single-author note asks the same question of directional direct search with sufficient decrease (abstract). The trigger is not documented **(speculation: the Cartis–Gould–Toint-era complexity wave)**. |
| Why then | The sufficient-decrease variant of direct search (forcing function) provides a per-iteration decrease that can be counted. Mesh-based variants lack this. |
| Key insight | Direct search with sufficient decrease shares steepest descent's worst-case bound: at most O(ε⁻²) iterations to drive ‖∇f‖ below ε (abstract). |
| Minimal evidence | A short proof; no numerics needed. |
| Abandoned paths | Unknown. |
| Reception | Opened a programme: convex case O(ε⁻¹) (Dodangeh & Vicente 2016), optimality of the n² factor in evaluations (Dodangeh, Vicente & Zhang 2016), nonsmooth via smoothing (Garmanjani & Vicente 2013), and later others' multiobjective complexity papers (search results). |
| Methods shown | Method 2 (count the evaluations against a gradient benchmark) |
| **[full text]** | Two-counter proof, n² = cm⁻² × poll size, ε-order tightness by reduction to steepest descent in dimension 1 [S023 pp. 5–8]. "Optimality of the n² factor" (Dodangeh, Vicente & Zhang 2016) holds only among positive-spanning-set choices within the sufficient-decrease bound, not as an oracle lower bound [S041 pp. 1, 5, 8]. |

### 2.4 "Direct search based on probabilistic descent" (Gratton, Royer, Vicente & Zhang, SIAM J. Optim. 25(3) (2015) 1515–1541)

| Dimension | Content |
|---|---|
| Origin | Abstract (via search): "Recent numerical results indicated that randomly generating the polling directions without imposing the positive spanning property can improve the performance." **The theory followed a numerical anomaly.** Wording is from the search summary and may be close to, but is not guaranteed to be, the abstract's exact wording. |
| **[full text]** | The preprint abstract says the rate is "matching" the deterministic one; the gain is in evaluations, O(mnε⁻²) vs O(n²ε⁻²) [S019 pp. 1, 16, 22]. The "recent numerical results" are those of the merit-function paper [S019 p. 2; S049 pp. 14–15]. The first experiment was rerun after the theory showed it was biased in favour of the new method [S019 pp. 20–21]. |
| Why then | Complexity machinery for direct search (2013) now existed. Probabilistic-model analysis for trust regions (Bandeira, Scheinberg & Vicente 2014) supplied the martingale-style tools. |
| Key insight | Polling directions need only a descent property that holds with sufficient probability conditioned on the past (probabilistic descent), not a deterministic positive spanning set. This yields almost-sure convergence and complexity bounds with overwhelming probability, and fewer evaluations per iteration. |
| Minimal evidence | Complexity results, plus numerics where randomization "compares favorably" and is "clearly superior" in some cases (search summary). |
| Abandoned paths | Unknown. |
| Reception | Constrained extension (COAP 2019). A reduced-space extension appeared in SIAM J. Optim. 2023 (DOI 10.1137/22M1488569; authors not confirmed by search, ⚠️). In 2026 Huang & Zhang (arXiv:2606.01320) proved the submartingale-like condition is **essential**: below the direction-count threshold the method is not globally convergent. That is independent confirmation that the theory's threshold is sharp. |
| Methods shown | Method 3 (probabilistic instead of deterministic guarantees), Method 2 |

### 2.5 (short) "Stochastic trust-region and direct-search methods: A weak tail bound condition and reduced sample sizing" (Rinaldi, Vicente & Zeffiro, SIAM J. Optim. 34 (2024) 2067–2092, DOI 10.1137/22M1543446)

- Key insight: impose a tail-bound condition on the *estimated reduction* rather than on each function estimate, so fewer samples per iteration are needed. Vicente's talk abstract (paraphrase) describes a reduction from O(δ⁻⁴) to O(δ⁻²q) samples when the noise moment of order q/(q−1) is bounded. Source: Pitt IE seminar listing and Rice CMOR colloquium listing (primary talk abstracts relayed via search).
- Follow-on: sequential hypothesis testing for the sufficient-decrease test (Ding, Rinaldi & Vicente, arXiv:2509.14505, 2025).
- Methods shown: Method 3, Method 5.

## 3. Sources for this file
- https://link.springer.com/article/10.1007/s13675-012-0003-7 (primary)
- https://www.mat.uc.pt/~lnv/papers/sid-psm.pdf ; http://www.mat.uc.pt/sid-psm/ (primary)
- https://epubs.siam.org/doi/10.1137/10079731X ; http://www.mat.uc.pt/dms/ ; https://optimization-online.org/wp-content/uploads/2010/06/2642.pdf (primary)
- https://www.zhangzk.net/docs/publications/2015dspd.pdf ; https://www.researchgate.net/publication/281124866_Direct_Search_Based_on_Probabilistic_Descent (primary)
- https://doi.org/10.1137/22M1543446 ; https://arxiv.org/abs/2202.11074 (primary)
- https://calendar.pitt.edu/event/ie-seminar-luis-nunes-vicente-reducing-sample-complexity-in-stochastic-derivative-free-optimization-via-tail-bounds-and-hypothesis-testing-416 (primary talk abstract)
- https://link.springer.com/article/10.1007/s10107-014-0847-0 ; https://link.springer.com/article/10.1007/s11590-015-0908-1 (primary)
- https://www.semanticscholar.org/paper/Analysis-of-direct-searches-for-discontinuous-Vicente-Cust%C3%B3dio/d2677c8761e78bf821e79d2b6465d1298b4b060b (primary)
- https://arxiv.org/abs/2606.01320 (secondary: peer analysis)
- http://www.mat.uc.pt/~lnv/idfo/ (primary: book page)
