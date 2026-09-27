# 01 · Publications: landscape and signature-work anatomy

> Researcher: Katya Scheinberg · Research date: 2026-09-27
> Method: web-search snippets only (Semantic Scholar, arXiv, Springer, SIAM, NeurIPS listing pages as surfaced by search). `scripts/fetch_publications.py` could not reach OpenAlex; WebFetch was blocked for every host tried. No full text was read. Every paper below had title + authors + year (+ venue) confirmed in a search result unless marked ⚠️.
> Credibility tags: **primary** = the paper itself / publisher or arXiv record; **secondary** = aggregator or third-party page.

## 1. Publication landscape (hand-built from search results)

### 1.1 Verified papers and books, grouped by research line

| Line | Year | Title | Authors | Venue | ID / URL | Cred. |
|---|---|---|---|---|---|---|
| Early model-based DFO | 1997 | Recent progress in unconstrained nonlinear optimization without derivatives | A. R. Conn, K. Scheinberg, Ph. L. Toint | Mathematical Programming 79, 397–414 | https://doi.org/10.1007/BF02614326 | primary |
| Interpolation geometry | 2008 | Geometry of interpolation sets in derivative free optimization | A. R. Conn, K. Scheinberg, L. N. Vicente | Mathematical Programming 111, 141–172 | https://www.mat.uc.pt/~lnv/papers/csv.pdf | primary |
| Book | 2009 | Introduction to Derivative-Free Optimization | A. R. Conn, K. Scheinberg, L. N. Vicente | SIAM, MPS-SIAM Series on Optimization | http://www.mat.uc.pt/~lnv/idfo/ ; https://books.google.com/books/about/Introduction_to_Derivative_Free_Optimiza.html?id=tGbUshriSyYC | primary |
| Geometry (necessity) | 2010 | Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization | K. Scheinberg, Ph. L. Toint | SIAM J. Optim. 20(6), 3512–3532 | https://doi.org/10.1137/090748536 ; https://optimization-online.org/2009/02/2216/ | primary |
| Structure exploitation (DFO) | 2010 | A derivative-free algorithm for least-squares minimization | H. Zhang, A. R. Conn, K. Scheinberg | SIAM J. Optim. 20(6), 3555–3576 | https://www.math.lsu.edu/~hozhang/papers/GlobalDFLS.pdf | primary |
| ML / structure (IBM era) | 2001 | Efficient SVM training using low-rank kernel representations | S. Fine, K. Scheinberg | J. Mach. Learn. Res. 2, 243–264 | https://www.researchgate.net/publication/2865065_Efficient_SVM_Training_Using_Low-Rank_Kernel_Representations | primary (record) |
| ML / structure | 2010 | Sparse inverse covariance selection via alternating linearization methods | K. Scheinberg, S. Ma, D. Goldfarb | NIPS 23 (2010) | https://papers.nips.cc/paper/4099-sparse-inverse-covariance-selection-via-alternating-linearization-methods ; arXiv:1011.0097 | primary |
| Probabilistic models (pivot) | 2014 | Convergence of trust-region methods based on probabilistic models | A. S. Bandeira, K. Scheinberg, L. N. Vicente | SIAM J. Optim. 24(3), 1238–1264 | arXiv:1304.2808 ; https://arxiv.org/abs/1304.2808 | primary |
| Stochastic TR (STORM) | 2018 | Stochastic optimization using a trust-region method and random models | R. Chen, M. Menickelly, K. Scheinberg | Mathematical Programming 169, 447–487 | https://doi.org/10.1007/s10107-017-1141-8 ; arXiv:1504.04231 | primary |
| Complexity with prob. models | 2018 | Global convergence rate analysis of unconstrained optimization methods based on probabilistic models | C. Cartis, K. Scheinberg | Mathematical Programming 169, 337–375 | https://doi.org/10.1007/s10107-017-1137-4 ; arXiv:1505.06070 | primary |
| Stopping-time analysis | 2019 | Convergence rate analysis of a stochastic trust-region method via supermartingales | J. Blanchet, C. Cartis, M. Menickelly, K. Scheinberg | INFORMS J. on Optimization 1(2), 92–119 | https://ora.ox.ac.uk/objects/uuid:798e9ee8-baa2-4497-b53a-1377c4c2f748 ; arXiv:1609.07428 | primary |
| Stochastic line search | 2020 | A stochastic line search method with expected complexity analysis | C. Paquette, K. Scheinberg | SIAM J. Optim. 30, 349–376 | https://doi.org/10.1137/18M1216250 ; arXiv:1807.07994 | primary |
| Gradient estimators (DFO↔ML) | 2022 | A theoretical and empirical comparison of gradient approximations in derivative-free optimization | A. S. Berahas, L. Cao, K. Choromanski, K. Scheinberg | Found. Comput. Math. 22(2), 507–560 | https://doi.org/10.1007/s10208-021-09513-z ; arXiv:1905.01332 | primary |
| High-probability bounds | 2024 | High probability complexity bounds for adaptive step search based on stochastic oracles | B. Jin, K. Scheinberg, M. Xie | SIAM J. Optim. 34(3), 2411–2439 | https://doi.org/10.1137/22M1512764 ; arXiv:2106.06454 | primary |
| High-probability bounds (TR) | 2024 | First- and second-order high probability complexity bounds for trust-region methods with noisy oracles | L. Cao, A. S. Berahas, K. Scheinberg | Mathematical Programming 207, 55–106 | https://doi.org/10.1007/s10107-023-01999-5 ; arXiv:2205.03667 | primary |
| Complexity of Powell-type DFO | 2025 | On complexity of model-based derivative-free methods | A. Chaudhry, K. Scheinberg | arXiv preprint | arXiv:2510.14935 ; https://arxiv.org/abs/2510.14935 | primary |
| Unreliable oracles | 2025 | Stochastic adaptive optimization with unreliable inputs: a unified framework for high-probability complexity analysis | K. Scheinberg + one co-author (co-author name not confirmed; snippet suggests M. Xie ⚠️) | arXiv preprint | arXiv:2511.19411 ; https://arxiv.org/abs/2511.19411 | primary |
| Powell-style DFO with guarantees | 2026 | Powell-style model-based derivative-free optimization with complexity guarantees | A. Chaudhry, K. Scheinberg, S. Sun | arXiv preprint (submitted 2026-09-08) | arXiv:2609.09441 ; https://arxiv.org/abs/2609.09441 | primary |

### 1.2 Observed patterns (analysis, secondary — my reading of the table)

- **Two long arcs, one bridge.** Arc 1 (1997–2010, IBM era) = deterministic model-based DFO: interpolation models, trust regions, geometry of sample sets, a textbook, open-source DFO code. Arc 2 (2013–now, Lehigh → Cornell → Georgia Tech) = *probabilistic* models and stochastic oracles: the same classical algorithms (trust region, Armijo line search, cubic regularization) re-analysed when the model/gradient/function estimate is only good with some probability. The bridge is BSV 2014, which keeps the trust-region framework of Arc 1 and changes only the model-quality assumption.
- **Parallel ML thread from the start.** JMLR 2001 (SVM kernels), NIPS 2010 (sparse inverse covariance), FoCM 2022 (with a Google ML researcher, Choromanski), and adaptive step search framed against SGD (SIOPT 2024). Scheinberg did not "move into ML" at one point; ML problems recur as a source of structure and of oracle models.
- **Return to Powell.** 2025–2026 preprints return to Powell-type interpolation methods and give them worst-case complexity bounds, including random-subspace variants and noisy evaluations — the Arc 1 algorithms analysed with the Arc 2 toolkit.
- **Venue profile.** Core optimization journals (in this verified set: Math. Programming ×5, SIAM J. Optim. ×5, INFORMS J. Optim., FoCM) plus ML venues (JMLR, NIPS). Algorithm papers almost always pair a convergence/complexity theorem with numerical comparison (from abstracts: DFLS 2010 "numerical comparisons … to standard derivative-free software packages"; FoCM 2022 "theoretical and empirical"; 2026 "extensive numerical comparison").
- **Co-author pattern.** Senior peers (Conn, Toint, Vicente, Cartis, Goldfarb, Blanchet) on framework papers; junior co-authors (R. Chen, M. Menickelly, C. Paquette, L. Cao, B. Jin, M. Xie, A. Chaudhry, A. S. Berahas) first-authoring the stochastic-oracle papers. Advisor/student status of the juniors is **not** confirmed by any search result (see 04-mentorship.md).

### 1.3 Unverified leads (not cited as fact; see RESOURCES.md ⚠️)

- "Linear interpolation gives better gradients than Gaussian smoothing in derivative-free optimization" (arXiv:1905.13043) — title/ID seen, author list not confirmed.
- "Black-Box Optimization in Machine Learning with Trust Region Based Derivative Free Algorithm" (arXiv:1703.06925) — title/ID seen, authors not confirmed.
- "Computation of sparse low degree interpolating polynomials and their application to derivative-free optimization" (arXiv:1306.5729) — authors not confirmed.
- "Global Convergence Rate Analysis of a Generic Line Search Algorithm with Noise" (SIAM J. Optim., DOI 10.1137/19M1291832) — authors not confirmed.
- "Sample complexity analysis for adaptive optimization algorithms with stochastic oracles" (Math. Program., DOI 10.1007/s10107-024-02078-z; arXiv:2303.06838) — authors not confirmed.
- "Stochastic ISTA/FISTA Adaptive Step Search Algorithms for Convex Composite Optimization" (arXiv:2402.15646) — authors not confirmed.
- "First- and Second-Order Stochastic Adaptive Regularization with Cubics: High Probability Iteration and Sample Complexity" (arXiv:2308.13161) — authors not confirmed.
- "Practical Inexact Proximal Quasi-Newton Method with Global Complexity Analysis" — seen only as the description of GitHub repo LHAC/LHAC whose README mentions Scheinberg; venue/year not confirmed.
- ICM 2026 proceedings status of arXiv:2510.14935 — stated in one search summary, not independently confirmed.

## 2. Signature-work anatomy (4 works)

Selection: the pivot (BSV 2014), the most-reused algorithm (STORM 2018), the DFO↔ML bridge (FoCM 2022), and the latest turn back to Powell (2026). "Speculation" is marked wherever no first-hand source exists.

### 2.1 Convergence of trust-region methods based on probabilistic models (SIAM J. Optim. 2014, arXiv:1304.2808)

| Dimension | Content |
|---|---|
| Origin | *Speculation*: follows directly from Conn–Scheinberg–Vicente's deterministic model-quality theory (CSV 2008; book 2009). Randomized sampling of interpolation points could not guarantee "fully linear" models every iteration, so the question became what happens if they are good only sometimes. No first-hand origin account found. |
| Why then | *Inference*: randomized linear algebra / compressed sensing ideas were entering DFO (the co-authors' sparse-interpolation lead arXiv:1306.5729 ⚠️), and random models made deterministic certification the bottleneck. |
| Key insight | Keep the classical trust-region algorithm; require first-order models to be sufficiently accurate only **with probability ≥ 1/2** (per abstract snippet); function values are still exact. Convergence survives. |
| Minimal evidence | The abstract states the method uses random models "of higher quality than those produced by usual stochastic gradient methods" with a fixed probability threshold (search snippet, Semantic Scholar/arXiv). |
| Abandoned paths | Unknown. |
| Reception | Became the anchor for STORM (2018) and for Cartis–Scheinberg (2018); later third-party titles use "random models" and "probabilistic models" framing (e.g., arXiv:2409.15734 "Trust-Region Sequential Quadratic Programming for Stochastic Optimization with Random Models" — authors unverified ⚠️). |
| Methods shown | Method 1 (probabilistic-oracle abstraction), Method 3 (minimal model-quality requirement). |

### 2.2 Stochastic optimization using a trust-region method and random models (Math. Programming 2018, DOI 10.1007/s10107-017-1141-8)

| Dimension | Content |
|---|---|
| Origin | *Speculation*: natural next step after BSV 2014 — drop the exact-function-value assumption too. |
| Why then | *Inference*: ML/simulation workloads where both function and gradient are sampled estimates. |
| Key insight | Models **and** function estimates need to be sufficiently accurate "with high enough, but fixed, probability"; accuracy is tied to the trust-region radius; almost-sure convergence to first-order stationarity follows (abstract snippet). |
| Minimal evidence | Abstract: gives examples of generating sufficiently accurate random models "under biased or unbiased noise assumptions". |
| Abandoned paths | Unknown. |
| Reception | Named algorithm ("STORM"); an Argonne ALCF event was titled "STORM: STochastic Optimization using Random Models" (https://www.alcf.anl.gov/events/storm-stochastic-optimization-using-random-models; speaker not confirmed ⚠️); follow-up by others titled "ProxSTORM — A Stochastic Trust-Region Algorithm for Nonsmooth Optimization" (arXiv:2510.03187; authors unverified ⚠️). Complexity analysis followed in Blanchet et al. 2019. |
| Methods shown | Method 1, Method 2 (analysis followed in a separate stopping-time paper), Method 6 (classical adaptive method for stochastic/ML settings). |

### 2.3 A theoretical and empirical comparison of gradient approximations in derivative-free optimization (Found. Comput. Math. 2022, DOI 10.1007/s10208-021-09513-z)

| Dimension | Content |
|---|---|
| Origin | *Speculation*: ML practice (evolution strategies / Gaussian smoothing for RL policy search, co-author Choromanski at Google) used smoothing-based gradient estimates; the optimization community used finite differences and interpolation. The paper puts them on one scale. |
| Why then | *Inference*: zeroth-order methods for RL and adversarial ML became popular ~2017–2019; arXiv v1 is 2019 (arXiv:1905.01332). |
| Key insight | For each estimator (finite differences, linear interpolation, Gaussian smoothing, smoothing on a sphere) derive the **number of samples and sampling radius** that guarantee the accuracy needed by a line-search or fixed-step method; then compare empirically (abstract snippet). |
| Minimal evidence | Abstract describes the bounds per estimator; companion lead title "Linear interpolation gives better gradients than Gaussian smoothing…" (⚠️ authors unverified) suggests the headline empirical finding. |
| Abandoned paths | Unknown. |
| Reception | Published in FoCM; widely referenced by later zeroth-order work (no citation counts verified). |
| Methods shown | Method 4 (head-to-head estimator comparison), Method 1 (accuracy requirement as the yardstick), Method 6 (ML bridge). |

### 2.4 Powell-style model-based derivative-free optimization with complexity guarantees (arXiv 2026, arXiv:2609.09441)

| Dimension | Content |
|---|---|
| Origin | Stated in abstract (snippet): the variants are "closest to methods initially proposed and implemented by Powell", which "rely on low degree polynomial interpolation and carefully maintain geometry of the interpolation sets". Companion paper arXiv:2510.14935 set up the complexity framework. |
| Why then | *Inference*: random-subspace analysis and high-probability tools (Arc 2) now make it possible to bound Powell-type methods, which had strong practical reputations but weaker worst-case theory. |
| Key insight | Classical Powell-style methods can be made "theoretically competitive to other derivative free methods"; applying them in random subspaces recovers "nearly tight" complexity (abstract snippet). |
| Minimal evidence | Abstract: derives complexity bounds, fully incorporates Powell's geometry-handling approach, runs "extensive numerical comparison", and extends subspace analysis to noisy function evaluations. |
| Abandoned paths | Unknown (preprint only). |
| Reception | Too recent (submitted 2026-09-08). |
| Methods shown | Method 3 (geometry as the minimal necessary ingredient), Method 2 (complexity analysis), Method 4 (numerical comparison). |

## Sources used in this file
All URLs/IDs are listed inline. Aggregator records (Semantic Scholar, ResearchGate) are secondary; publisher/arXiv records are primary.

---

## Update 2026-09-27 (deepening pass): leads resolved and papers added

**Leads from §1.3 now verified** (title + authors + year + venue confirmed by search; RESOURCES.md rows updated):

| Year | Title | Authors | Venue / ID |
|---|---|---|---|
| 2019 | Linear interpolation gives better gradients than Gaussian smoothing in derivative-free optimization | A. S. Berahas, L. Cao, K. Choromanski, K. Scheinberg | arXiv:1905.13043 (Lehigh tech report) |
| 2021 | Global convergence rate analysis of a generic line search algorithm with noise | A. S. Berahas, L. Cao, K. Scheinberg | SIAM J. Optim. 31, 1489–1518; https://doi.org/10.1137/19M1291832 ; arXiv:1910.04055 |
| 2025 | Sample complexity analysis for adaptive optimization algorithms with stochastic oracles | B. Jin, K. Scheinberg, M. Xie | Math. Program. 209, 651–679; https://doi.org/10.1007/s10107-024-02078-z |
| 2025 | Stochastic ISTA/FISTA adaptive step search algorithms for convex composite optimization | L. M. Nguyen, K. Scheinberg, T. H. Tran | J. Optim. Theory Appl. 205, art. 10; https://doi.org/10.1007/s10957-025-02621-8 |
| 2023 | First- and second-order stochastic adaptive regularization with cubics: high probability iteration and sample complexity | K. Scheinberg, M. Xie | arXiv:2308.13161 (preliminary: WSC 2023) |
| 2016 | Practical inexact proximal quasi-Newton method with global complexity analysis | X. Tang, K. Scheinberg | Math. Program. 160, 495–529; arXiv:1311.6547 |
| 2025 | (co-author resolved) Stochastic adaptive optimization with unreliable inputs | K. Scheinberg, **M. Xie** | arXiv:2511.19411 |

**Newly added verified works**: Jin–Scheinberg–Xie, NeurIPS 34 (2021), "High probability complexity bounds for line search based on stochastic oracles"; Nguyen–Liu–Scheinberg–Takáč, ICML 2017, "SARAH"; Curtis–Scheinberg, INFORMS TutORials 2017 and IEEE SPM 37(5) 2020.

**Lead resolved negatively**: arXiv:2604.15526 (RAAS) is by Zhang, Liao, Han, Guo (UCAS), not Scheinberg.

**Still unverified**: arXiv:1703.06925; arXiv:1306.5729 (authors).

The analysis templates behind these papers are in `../proof-playbook.md`; the ordered reading list is in `../reading-path.md`.

---

## Update 2026-09-27 (full-text pass): coverage from the Google Scholar list

The publication list is now complete at the level of the Google Scholar profile, and most papers were read in full. Sources: `../sources/publications/scholar.md` (Google Scholar profile https://scholar.google.com/citations?user=zbqRbOkAAAAJ, plus DBLP and Crossref; machine-readable in `works.json`), the full-text index `../sources/papers/INDEX.md`, the paper cards indexed in `07-paper-cards.md`, and the synthesis `08-deep-reading-synthesis.md`.

### Coverage

| Item | Count | Note |
|---|---|---|
| Google Scholar rows | 143 | 14 are duplicates or junk rows (`dup_of` in `works.json`) |
| Distinct works on the Scholar list | 129 | plus 3 found only in DBLP/arXiv (D001–D003) = **132 works** |
| Works with an open full text | 85 | `txt` in INDEX.md; 47 are `no-oa` (including 3 patents and 4 talks) |
| Card entries / distinct papers carded | 125 / 119 | five same-text pairs count once: S011 = S123, S089 = S106, S098 = S107, S028 = S067, D001 = S043 |
| **Read in full text** | **78** | 64 in full, 14 partially (skipped parts named on each card) |
| Abstract-level | 19 | including the IDFO book (S001), which has no open full text |
| Metadata-only | 21 | claims on these cards are marked *inferred* |
| Unreadable | 1 | S133 (DFO v1.2 manual); the v2.0 manual (2003) was carded as a substitute |
| Skipped | 8 | 3 patents, 4 talks, and D002 (Scheinberg is an author only on arXiv v1) |

Full-text reads by period (full or partial / all carded works with a year): 1996–2000 3/13; 2001–2005 5/8; 2006–2010 14/24; 2011–2015 13/17; 2016–2020 25/32; 2021–2026 18/22 [08 §1]. The interior-point years are therefore known almost only from abstracts, while the DFO and stochastic-analysis lines are read nearly completely.

### Research lines in the full list (cards per line; full or partial reads in brackets, from 08 §8.1)

| Line | Works (read) | Card ids |
|---|---|---|
| Interior-point and conic | 11 (2) | S027, S034, S039, S040, S045, S050, S058, S069, S077, S091, S134 |
| SVM training | 6 (3) | S003, S022, S059, S071, S097, S140 |
| Model-based DFO | 20 (16) | S001, S004, S007, S008, S016, S019, S023, S025, S030, S033, S046, S053, S062, S065, S072, S088, S104, S121, S133, S143 |
| Structured first/second-order and sparse learning | 21 (13) | S005, S010, S011, S021, S028, S029, S035, S042, S048, S049, S054, S064, S066, S079, S084, S090, S096, S100, S101, S124, S142 |
| Stochastic gradient and variance reduction | 9 (9) | S002, S009, S024, S031, S032, S036, S037, S055, S063 |
| Adaptive stochastic methods with probabilistic oracles | 22 (16) | S012, S013, S014, S015, S018, S026, S041, S043/D001, S047, S057, S061, S068, S083, S093, S098, S108, S111, S112, S113, S119, S120, S137 |
| Gradient estimation and new oracles | 6 (4) | D003, S006, S044, S073, S081, S087 |
| ML models and applications (mostly student-led) | 9 (9) | S017, S020, S051, S060, S074, S078, S082, S086, S089 |
| DFO applications | 8 (5) | S038, S052, S056, S085, S094, S102, S116, S128 |
| Service and editorial | 7 (1) | S080, S105, S118, S126, S127, S129, S138 |

(Counts in brackets are cards read in full or in part; S143 counts once although it has an abstract card and a full card. The read level of every card is in `07-paper-cards.md`.)

### Leads from §1.3 and later sections now resolved by the full texts

| Lead | Resolution | Card |
|---|---|---|
| arXiv:1703.06925 (authors unconfirmed) | Ghanbari, Scheinberg (2017), "Black-box optimization in machine learning with trust region based derivative free algorithm"; read in full | S052 |
| arXiv:1306.5729 (authors unconfirmed) | Bandeira, Scheinberg, Vicente, *Math. Program.* (2012), DOI 10.1007/s10107-012-0578-z; read partially | S033 |
| ProxSTORM, arXiv:2510.03187 (listed as third-party, authors unconfirmed) | Baraldi, Javeed, Kouri, **Scheinberg** (Sandia collaboration); read in full; same text as the 2024 Sandia report | S098 = S107 |
| Optima 79 article (title not retrieved) | "Geometry in model-based algorithms for derivative-free unconstrained optimization", Optima 79, May 2009, sole-authored; the Moré–Wild framing and the "minimal quality controls" wording attributed to it in earlier search summaries come from Nocedal's discussion column in the same issue (p. 6); she was co-editor of Optima (p. 10) | S143 |
| arXiv:1905.13043 authors | Berahas, Cao, Choromanski, Scheinberg (confirmed in the text) | D003 |
| arXiv:2609.09441 authors | The text lists three authors (Chaudhry, Scheinberg, Sun); the Scholar row lists two | S104 |
| JMLR 2006 active-set SVM paper | Sole-authored; the Scholar record lists the JMLR issue editors as coauthors | S022 |

### Corrections to §1.2 "Observed patterns"

- **Venue profile claim "algorithm papers almost always pair a theorem with numerical comparison"**: true for algorithm and software papers [cards S012, S006, S033, S041, S098, S104], but the pure-analysis papers have no numerical section [cards S014, S026, S083, S088, S093]. SKILL.md Taste mark 4 is corrected accordingly.
- **Two arcs, one bridge**: confirmed, with two more parallel lines visible only in the full list: structured first-order methods and sparse learning (2009–2016) and stochastic gradient / variance reduction (2017–2022) [08 §8.2]. The latter does not follow the adaptive-method lens (new estimators with tuned or prescribed steps) and is recorded in SKILL.md as a scope limit on Method 2.
- **Co-author pattern**: confirmed and refined in 08 §9 (one senior partner per era, then a student or postdoc per line; specialists brought in for one step).

### Signature-work anatomies

The four anatomies in §2 above were built from abstracts. SKILL.md now carries full-text versions of all four plus two more (Scheinberg–Toint 2010 with the Optima 79 essay; Jin–Scheinberg–Xie 2024), each with page references to the cards. §2 is kept as the abstract-level record.
