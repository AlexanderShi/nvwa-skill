# Frank E. Curtis: Signature Works and the Publication Landscape

| Field | Value |
|---|---|
| Researcher | Frank E. Curtis (Lehigh University, ISE; PhD Northwestern 2007, advisor Jorge Nocedal) |
| Dimension | Research agent 01 of 06: signature works and the publication landscape (nuwa research-craft, Phase 1) |
| Research date | 2026-09-28 |
| Sources consulted | 43 (35 primary, 8 secondary). Listed under "Sources"; a 44th, Google Scholar, was attempted but blocked |
| WebSearch calls | 2 |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` held only `.gitkeep` |
| Raw landscape files | `references/sources/publications/publications.md` and `abstracts.md` (OpenAlex, written by `scripts/fetch_publications.py` in this run) |

**Evidence tags.** [stated] means Curtis said or wrote it about his own work (CV, homepage, slides, the prose of a paper). [practice] means what the papers, code and records show he did. [observed] means a third party reported it (prize committees, bibliographic databases). [inferred] means my reading, with the basis given. (P) marks a primary source and (S) a secondary one.

**Reading depth.** I read these full texts in part (introduction, numerics, conclusion, acknowledgments): Byrd–Curtis–Nocedal 2008 and 2010, Curtis 2012 (PIPAL), Curtis–Overton 2012, Curtis–Mitchell–Overton 2017, Curtis–Robinson–Samadi 2017, Bottou–Curtis–Nocedal 2018 (introduction only), and Berahas–Curtis–Robinson–Zhou arXiv v1 (2020). For every other paper I read only the arXiv abstract or the bibliographic record. I did not read any proofs.

---

## 0. A caveat on authorship order that changes how this file reads

- [stated] (P) The CV (rev. 7 Apr 2026, footnote 1) says: "Standard practice in my research field is to list authors alphabetically, as is done for most of the articles in this section."
- [practice] (P) Of the 76 DBLP records, all but about a dozen list authors alphabetically. "Curtis" sorts early, so OpenAlex's automatic count of 81 "first-author" works (see `publications.md`) is an artifact of the alphabet. It does not show that he led those papers. **The framework's "first-author → last-author shift" test therefore does not apply as written.**
- [practice] (P) The useful signal is the non-alphabetical papers. They come in two kinds:
  - *Student or postdoc first, Curtis last or middle, in ML-, OR- or engineering-convention venues:* Han & Curtis 2015 (arXiv 1508.02452); Gao, Goldfarb & Curtis 2020 (OMS, 10.1080/10556788.2019.1683553); Tsang, Shehadeh & Curtis 2023 (ORL, 10.1016/j.orl.2022.12.002); Dai, Wang, Curtis & Robinson (AISTATS 2023, arXiv 2302.06790); Dinç Yalçın & Curtis 2024 (OMS, 10.1080/10556788.2023.2296432); Khatti, Robinson & Curtis (arXiv 2505.15788); Wang, Piermarini, Zhu & Curtis (arXiv 2601.11795); Zhu, Guo, Khatti, Qu, Wu, Zebiane & Curtis (arXiv 2605.06945).
  - *Large multi-institution or applied teams:* the ARPA-E grid papers (Operations Research 2023, 10.1287/opre.2022.0315) and the wave-energy paper (Renewable Energy 2021, 10.1016/j.renene.2021.02.134).
- [inferred] Student-first, Curtis-last ordering clusters after 2022 in ML and fairness work, which suggests he adopts the host community's authorship convention when he writes for ML audiences. That is a change of audience, not evidence that he stopped doing the work himself. The core optimization papers (SIOPT, MP) stay alphabetical through 2026.

---

## 1. Publication landscape

### 1.1 Size and sources (numbers disagree; kept as they are)

| Source | Count | Notes |
|---|---|---|
| CV rev. 7 Apr 2026 (P) | 63 published journal articles ([8]–[70]), 7 journal articles under review, 3 conference papers, 4 review articles or chapters, 1 authored book, 1 edited book, 1 tech report, PhD and BS theses | Authoritative self-listing |
| DBLP pid 61/7604 (S), SPARQL, 2026-09-28 | 76 records, 2004–2026 (57 Article, 17 Informal, 2 Inproceedings); 67 with DOI, 17 with arXiv id | Contains none of his IMA J. Numer. Anal. papers (e.g. 10.1093/imanum/drn003, 10.1093/imanum/drv034, 10.1093/imanum/dry022), which the CV and OpenAlex list |
| OpenAlex A5005028153 (S) | 127 works (132 fetched including preprint duplicates); total citations 5,240; h = 26; i10 = 45 | Contains at least one misattribution: "Collection systems for royalties in wheat an international study" (2013) is on neither the CV nor DBLP |
| Crossref (S) | per-DOI counts only | Example: SIAM Review 2018 has 2,272 Crossref citations against 3,255 in OpenAlex |
| Google Scholar Zfd6irsAAAAJ | **not read** | WebFetch was redirected to Google's CAPTCHA page (`/sorry/`) |
| Semantic Scholar | **not read** | API returned HTTP 429 |

- [practice] (P) arXiv use starts in 2014. The earliest Curtis entry in the arXiv author search is 1402.1917 (Feb 2014). No paper from 2006–2013 appears there, so that era circulated through journals and his homepage PDFs (the homepage still hosts every paper as `files/papers/<Key>.pdf`). Since about 2020 almost every paper is on arXiv first, often tagged with a Lehigh ISE report number (e.g. 2007.10525 = "Lehigh ISE Technical Report 20T-012"; 2503.22826 = "25T-005").

### 1.2 Topics by five-year period

Journal-article counts come from the CV. Themes are my hand classification of the verified titles in DBLP, OpenAlex and the CV [inferred grouping; titles are practice].

| Period (career stage) | Journal articles (CV) | Dominant themes, with representative verified works | Resource context |
|---|---|---|---|
| 2003–2009 (BS at William & Mary; PhD with Nocedal at Northwestern 2003–07; Courant postdoc with Overton 2007–09) | 6 | Undergraduate combinatorics/matrix work (JCTA 2004, 10.1016/j.jcta.2003.10.001; AJMMS 2006, 10.1080/01966324.2006.10737660). **Inexact/matrix-free SQP**: Byrd–Curtis–Nocedal SIOPT 2008 (10.1137/060674004); Curtis–Nocedal–Wächter SIOPT 2009, rank-deficient Jacobians (10.1137/08072471X). **Penalty design**: Curtis–Nocedal "Flexible penalty functions" IMA JNA 2008 (10.1093/imanum/drn003); steplength in IPM for QP, AML 2007 (10.1016/j.aml.2006.05.020) | Student in the Nocedal–Byrd group; Intel internship 2005 (CV); the 2008 paper acknowledges an Intel grant and DOE DE-FG02-87ER25047; Matlab prototypes with GMRES |
| 2010–2014 (Assistant Professor, Lehigh, from Aug 2009) | 9 | **Inexact IPM inside IPOPT**: Curtis–Schenk–Wächter SISC 2010 (10.1137/090747634); + Huber MP-B 2012 (10.1007/s10107-012-0557-4). **Infeasibility detection**: Byrd–Curtis–Nocedal SIOPT 2010 (10.1137/080738222); Burke–Curtis–Wang SIOPT 2014 (10.1137/120880045); PIPAL, MPC 2012 (sole author, 10.1007/s12532-012-0041-4). **Nonsmooth**: Curtis–Overton SIOPT 2012 SQP-GS (10.1137/090780201); Curtis–Que adaptive GS, OMS 2013 (10.1080/10556788.2012.714781). Inexact SQO with Johnson, Robinson and Wächter, SIOPT 2014 (10.1137/130918320) | NSF DMS-1016291 single PI 2010–13 ($110,001); DOE Early Career 2013–18 ($750,000, single PI); first PhD students (Hao Wang, Xiaocun Que from 2009) |
| 2015–2019 (Associate Professor from Jul 2015) | 20 | **Worst-case complexity**: TRACE MP 2017 (10.1007/s10107-016-1026-2); inexact regularized Newton IMA JNA 2019 (arXiv 1708.00475); trust-funnel complexity SIOPT 2018 (10.1137/16M1108650); concise TR analyses Optim. Lett. 2018 (10.1007/s11590-018-1286-2). **ML and stochastic**: SC-BFGS (ICML 2016, sole author); SIAM Review 2018 (10.1137/16M1080173); stochastic TR IJOO 2019 (10.1287/ijoo.2018.0010); negative curvature MP-B 2019 (10.1007/s10107-018-1335-8). **Nonsmooth**: BFGS-SQP OMS 2017 (10.1080/10556788.2016.1208749); quasi-Newton GS MPC 2015 (10.1007/s12532-015-0086-2). **Subproblem solvers and sparsity**: primal-dual active-set (COAP 2015, 10.1007/s10589-014-9681-9; SIOPT 2016, 10.1137/140993314); FaRSA ℓ1 (SIOPT 2017, 10.1137/16M1062259). **Augmented Lagrangian**: MP 2015 (10.1007/s10107-014-0784-y); with Gould, OMS 2016 (10.1080/10556788.2015.1071813). **IPM trust-funnel** with Gould, Robinson, Toint, MP 2017 (10.1007/s10107-016-1003-9). Chance constraints with Wächter and Zavala, SIOPT 2018 (10.1137/16M109003X) | OptML group co-founded 2015 with Scheinberg and Takáč (CV); NSF DMS-1319356 "Randomized Models for Nonlinear Optimization" with Scheinberg, 2013–16; NSF CCF-1618717, 2016–19; TRIPODS 2018–20; visiting Columbia/NYU 2017–18 and Northwestern 2018 |
| 2020–2024 (Professor from May 2021) | 24 | **Stochastic SQP for deterministic constraints**: Berahas–Curtis–Robinson–Zhou SIOPT 2021 (10.1137/20M1354556); rank-deficient MOR 2024 (arXiv 2106.13015); stochastic inexact SQO IJOO 2024 (arXiv 2107.03512); complexity MP 2024 (10.1007/s10107-023-01981-1); inequality + equality SIOPT 2024 (10.1137/23M1556149). **Complexity cont.**: regional complexity MP 2021 (10.1007/s10107-020-01492-3); TR Newton-CG with Royer and S. J. Wright, SIOPT 2021 (10.1137/19M130563X); TRACE inexact, SIOPT 2023 (10.1137/22M1492428). **Quasi-Newton**: L-BFGS displacement aggregation MP 2022 (10.1007/s10107-021-01621-6). **Applications**: ARPA-E SCOPF (OR 2023, 10.1287/opre.2023.2453, and overview 10.1287/opre.2022.0315); healthcare scheduling with Shehadeh (ORL 2023; OR 2025, 10.1287/opre.2022.0258); fairness (Optim. Lett. 2024, 10.1007/s11590-023-02024-6) | ARPA-E grant 2018–22 (5-institution team, 2nd place in the 2020 Grid Optimization Competition); ONR 2021–24 with Berahas; postdocs Berahas, O'Neill, Dinç Yalçın, Jiang |
| 2025–2026 (to date) | 4 published + 7 under review (CV) | **Stochastic/noisy IPM**: SIOPT 2025 (10.1137/23M1569460); MP-B 2026 (10.1007/s10107-025-02320-2); noisy IPM with Dezfulian and Wächter (arXiv 2502.11302). **Active-set identification under noise** (arXiv 2509.00888); **progressive sampling** (arXiv 2510.00417, 2608.12665); **proximal gradient with general constraints** (arXiv 2512.23166). **Nonsmooth, noisy**: GS for noisy problems (arXiv 2604.00278); **NonOpt** C++ solver MPC 2026 (10.1007/s12532-026-00322-5). **Book**: Curtis & Robinson, *Practical Nonconvex Nonsmooth Optimization*, MOS-SIAM Series 2025 (10.1137/1.9781611978599). **ML optimizers**: Hessian-imitation Adam alternative (arXiv 2605.06945) | AFOSR 2025–28 "Lagrange Multiplier and Hessian Estimation in Stochastic Algorithms"; NSF DMS 2025–28 "Gradient Sampling Methods for Noisy Nonconvex Nonsmooth Optimization"; ONR 2024–27 with Robinson (CV) |

[inferred] Across 20 years the problem class stays the same: continuous, mostly nonconvex, often constrained. What changes is the **information model** the algorithm is allowed to use: exact and factorable (2004) → exact but only by iterative solves, i.e. inexact steps (2006–14) → nonsmooth, only gradients almost everywhere (2009–) → worst-case accounting (2014–23) → stochastic objective with deterministic constraints (2016/2020–) → noisy objective **and** constraints (2025–).

### 1.3 Collaboration network and students

[practice] (S) OpenAlex co-authorship counts: Daniel P. Robinson 49 (2014–2026; by far the dominant partner); Andreas Wächter 10 (2009–2024); Baoyu Zhou 10; James V. Burke 8; Jorge Nocedal 7 (2006–2018); Katya Scheinberg 7 (2017–2020); Albert S. Berahas 7 (2019–2026); Mohammadreza Samadi 6; Hao Wang 5; Jiashan Wang 5; Karmel Shehadeh 5; Molzahn, Wei and Wong 5 each (ARPA-E); Michael L. Overton 4 (2012–2020). DBLP agrees on the top three (Robinson 31, Wächter 9, Nocedal 7 among its 76 records). Team members also on this Nonlinear Team: Nocedal, Wächter, Gould and Toint (MP 2017, 10.1007/s10107-016-1003-9; OMS 2016), and S. J. Wright (SIOPT 2021, 10.1137/19M130563X).

[stated] (P) Advisees (CV and collaborators page) and the thesis line each one carried:

| Advisee | Period | Thesis topic (CV) | Matching publication line [practice] |
|---|---|---|---|
| Hao Wang | 2009–15 | "Practical Enhancements in Sequential Quadratic Optimization: Infeasibility Detection, Subproblem Solvers, and Penalty Parameter Updates" | Burke–Curtis–Wang 2014, 2015, 2020 |
| Xiaocun Que | 2009–15 | "Randomized Algorithms for Nonconvex Nonsmooth Optimization" | Curtis–Que 2013, 2015 |
| Zheng Han | 2010–15 | "Primal-Dual Active-Set Methods in Nonlinear Optimization" | COAP 2015, SIOPT 2016, arXiv 1508.02452 |
| Wei Guo | 2011–17 | "Limited Memory Steepest Descent Methods" | IMA JNA 2016 (10.1093/imanum/drv034), 2018 (10.1093/imanum/drx016) |
| Mohammadreza Samadi | 2013–18 | "Efficient Trust Region Methods for Nonconvex Optimization" | TRACE 2017; IMA JNA 2019; SIOPT 2018 |
| Rui Shi | 2015–20 | "Stochastic Trust Region Algorithms" | IJOO 2019; OMS 2022 (10.1080/10556788.2020.1852403) |
| Baoyu Zhou | 2018–22 | stochastic equality-constrained optimization | SIOPT 2021, IJOO 2024, SIOPT 2024, MP 2022 |
| Minhan Li | 2019–21 | "Topics on Data Science and Optimization" | IJOO 2022 (10.1287/ijoo.2022.0073) |
| Qi Wang | 2020–25 | "Inexact and Stochastic Large-Scale Nonlinear Optimization" | TRACE-inexact 2023; stochastic IPM 2025/2026; JOTA 2025 |
| Current: Zebiane, Guo, Khatti, Zhu | 2023– | — | NonOpt; noisy GS; progressive sampling; fairness; momentum |
| Postdocs: Berahas (2018–20), O'Neill (2020–22), Dinç Yalçın (2021–22), X. Jiang (2022–24) | | | stochastic SQP; complexity; incremental quasi-Newton; single-loop IPM |

[inferred] Each student owns one algorithmic line from start to end, and the line usually continues after the student leaves: TRACE (Samadi, 2014) is picked up by Qi Wang (2022); stochastic SQP (Zhou, 2020) is picked up by Jiang and Wang (2023–26).

### 1.4 Venues

[practice] (S) OpenAlex: SIAM J. Optim. 18, Mathematical Programming 10, Optimization Methods & Software 9, IMA J. Numer. Anal. 5, INFORMS J. Optim. 4, Math. Prog. Computation 3, Operations Research 3. In ML venues he publishes rarely: ICML 2016 (sole author) and AISTATS 2023 (student-led), plus workshop plenaries at NeurIPS 2022 and 2025 and ICML 2021 (CV [86], [90], [92]). [inferred] His home audience is the mathematical-programming community. Where the algorithm is the contribution (PIPAL, BFGS-SQP, NonOpt, SQP-GS code), he chooses software-and-numerics venues (MPC, OMS).

### 1.5 Most-cited works (OpenAlex, 2026-09-28; relative only)

| Rank | Work | Id | OpenAlex / Crossref citations |
|---|---|---|---|
| 1 | Bottou, Curtis, Nocedal, "Optimization Methods for Large-Scale Machine Learning", SIAM Review 60(2) 2018 | 10.1137/16M1080173; arXiv 1606.04838 | 3,255 / 2,272 |
| 2 | Curtis, Robinson, Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization", MP 162 (2017) | 10.1007/s10107-016-1026-2 | 167 / 96 |
| 3 | Curtis, Overton, "A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization", SIOPT 22(2) 2012 | 10.1137/090780201 | 132 / 107 |
| 4 | Curtis, Mitchell, Overton, "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", OMS 32(1) 2017 | 10.1080/10556788.2016.1208749 | 105 / 81 |
| 5 | Curtis, Que, "A quasi-Newton algorithm for nonconvex, nonsmooth optimization with global convergence guarantees", MPC 7(4) 2015 | 10.1007/s12532-015-0086-2 | 86 / — |
| 6 | Byrd, Curtis, Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", SIOPT 20(5) 2010 | 10.1137/080738222 | 84 / 67 |
| 7 | Byrd, Curtis, Nocedal, "An Inexact SQP Method for Equality Constrained Optimization", SIOPT 19(1) 2008 | 10.1137/060674004 | 83 / 63 |
| 8 | Burke, Curtis, Lewis, Overton, Simões, "Gradient Sampling Methods for Nonsmooth Optimization", in *Numerical Nonsmooth Optimization* (Springer 2020), ch. 6 | 10.1007/978-3-030-34910-3_6; arXiv 1804.11003 | 68 / 57 |

[inferred] One review paper holds about 60% of all OpenAlex citations. Citations therefore overstate the machine-learning review relative to his algorithmic core. The prize record (1.6) gives a second, independent view.

### 1.6 Prizes (external reception)

- [observed] (S) 2021 SIAM/MOS **Lagrange Prize in Continuous Optimization** for the SIAM Review paper, with Bottou and Nocedal. The citation (Lehigh news, 31 Mar 2021) reads: "Their work provides a foundational and insightful review of optimization methods for large-scale machine learning, including a new perspective for the simultaneous consideration of noise reduction and ill-conditioning and the foundations and analysis of second-order stochastic optimization methods for machine-learning." The committee was Leyffer (chair), X. Chen, de Klerk and Gill.
- [observed] (S) 2018 **INFORMS Computing Society Prize**, with Burke, Lewis and Overton (INFORMS prize page). [stated] (P) In the co-authored highlights article "The Gradient Sampling Methodology" (14 Jan 2019): "The prize was awarded for the articles [BLO05, CMO17, CO12, CQ13, CQ15, BCL+19], which involved co-authorship by Tim Mitchell, Xiaocun Que and Lucas E. A. Simões." The committee was chaired by Andreas Wächter.
- [stated] (P) Nemhauser Doctoral Dissertation Award (Northwestern, 2008), for the thesis *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization* (2007, DOI 10.21985/n2r99v, checked via DataCite). Optimization Letters Best Paper of the Year 2018 (CV); the CV does not name the paper, but his only 2018 Optim. Lett. paper is "Concise complexity analyses for trust region methods" [inferred match].

### 1.7 Recent works (last ~12 months, verified on arXiv or DOI)

- Curtis, Robinson, Zebiane, "Active-Set Identification in Noisy and Stochastic Optimization", arXiv 2509.00888 (Aug 2025)
- Curtis, Guo, Robinson, "Progressively Sampled Equality-Constrained Optimization", arXiv 2510.00417 (v1 Oct 2025, v2 May 2026)
- Curtis, Qu, Robinson, "A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints", arXiv 2512.23166 (Dec 2025)
- Wang, Piermarini, Zhu, Curtis, "Projected Stochastic Momentum Methods for Nonlinear Equality-Constrained Optimization for Machine Learning", arXiv 2601.11795 (Jan 2026)
- Curtis, Jiang, Wang, "A single-loop stochastic feasible interior-point algorithm for nonlinear inequality-constrained optimization", Math. Prog. B 2026, 10.1007/s10107-025-02320-2
- Wu, Curtis, Robinson, "A Bilevel Optimization Approach for Computing Synthetic Data to Mitigate Unfairness in Collaborative Machine Learning", IJOO 2026, 10.1287/ijoo.2025.0091
- Berahas, Curtis, Zebiane, "A Gradient Sampling Algorithm for Noisy Nonsmooth Nonconvex Optimization", arXiv 2604.00278 (v1 Mar 2026, v2 Aug 2026)
- Zhu, Guo, Khatti, Qu, Wu, Zebiane, Curtis, "Low-Order Explicit Hessian Imitation Method for Large-Scale Supervised Machine Learning", arXiv 2605.06945 (May 2026)
- Wu, Curtis, Robinson, "Robust Server Defense Against Unreliable Clients in One-Shot Fair Collaborative Machine Learning", arXiv 2605.08616 (May 2026; DBLP)
- Curtis, Zebiane, "NonOpt: Nonconvex, Nonsmooth Optimizer", MPC 2026, 10.1007/s12532-026-00322-5 (arXiv 2503.22826)
- Curtis, Guo, Robinson, "A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization", arXiv 2608.12665 (Aug 2026). The abstract says it extends the "Gradient-Eigenstep Algorithm by Goyens et al." (Fletcher's augmented Lagrangian) and uses it as a subproblem solver inside progressive sampling.

[inferred] The current agenda moves noise from the objective into the constraints and the multipliers. The recent titles, the AFOSR grant title ("Lagrange Multiplier and Hessian Estimation in Stochastic Algorithms", 2025–28) and the June 2025 talk title "Lagrange-Multiplier and Active-Set Estimation with Noisy and Stochastic Algorithms" (CV [100]) all point this way.

### 1.8 Software as a publication channel

[stated] (P) The CV lists: NonOpt (C++, author); Matlab prototypes StochasticSQP, SCBFGS, TRACE, AggQN, PIPAL and SLQP-GS, each marked "Code written by me"; GRANSO, where "I co-advised, with Michael Overton, the writing of the code by Tim Mitchell"; IPOPT, where he contributed the inexact-step interior-point algorithm; and filterSD (Fletcher's Fortran 77 code), which he manages in COIN-OR. The software page labels most of these "prototype" code and asks users to e-mail bug reports.

[practice] (P) The pattern is one paper, one prototype, and the prototype is written by Curtis himself even when students co-author the paper (SLQP-GS "contributed to by Tim Mitchell"; TRACE "with contributions from Mohammadreza Samadi"; StochasticSQP "with contributions from Baoyu Zhou"). NonOpt took roughly 6 years from its first talk to its paper: "NonOpt: Non(-linear/-smooth/-convex) Optimizer" at ICCOPT Aug 2019 (talks page), arXiv 2503.22826 in Mar 2025, MPC in 2026. [observed name change; inferred scope narrowing] The 2019 talk title included "Non-linear", while the 2025 abstract describes a package "for minimizing locally Lipschitz objective functions" and does not mention constraints.

---

## 2. Signature works (dissected per framework §5)

I chose five works to cover (a) the most cited, (b) the works the prize committees singled out, (c) what Curtis himself names as "Much of my work: exploiting inexactness for scalable constrained optimization." (ICCOPT 2019 slides), and (d) the turning points in 1.2.

### SW1. Byrd, Curtis, Nocedal, "An Inexact SQP Method for Equality Constrained Optimization", SIOPT 19(1):351–369, 2008. DOI 10.1137/060674004
Companions: Curtis–Nocedal–Wächter SIOPT 2009 (10.1137/08072471X); Byrd–Curtis–Nocedal MP 2010 (10.1007/s10107-008-0248-3); Curtis–Schenk–Wächter SISC 2010 (10.1137/090747634); Curtis–Huber–Schenk–Wächter MP-B 2012 (10.1007/s10107-012-0557-4).

- **Origin.** [stated] (P) The introduction targets "very large problems … for which the exact computation of steps in contemporary methods can be prohibitively expensive", with PDE-constrained problems as the named driver. The paper states its purpose: "The main purpose of this paper is to determine the accuracy with which the SQP subproblems must be solved in order to ensure global convergence in the context of a practical algorithm for problem (1.1)." It is his PhD topic (thesis title above). **Who proposed the problem is not documented**; the Nocedal–Byrd group context is [inferred].
- **Why then.** [practice] The paper was received 2 Nov 2006, during the PhD. Funding came from DOE and an Intel grant, and Curtis had interned at Intel in 2005 (CV). [inferred] Krylov solvers were mature and PDE-constrained optimization was pressing on SQP and IPM codes that assume factorization. Contemporaries cited in the paper (Biros–Ghattas; Haber–Ascher; Heinkenschloss–Vicente) had inexact methods without global-convergence conditions for full-space line-search SQP.
- **Key insight.** [practice] (P) Do not control the inexact solve by the norm of the whole primal-dual residual, as classical inexact Newton does. Instead, give the iterative solver termination tests (the paper's "SMART tests") that treat primal and dual residual components separately and require decrease in a local model of the exact-penalty **merit function**. This is the solver-demand principle he states on his research page (see §3 M1).
- **Minimum evidence.** [practice] (P) The Matlab implementation uses unpreconditioned GMRES on 44 CUTEr/COPS equality-constrained problems (fewer than 10,000 variables). The baseline, "ires", differs in exactly one component: it stops GMRES on a relative residual test. With κ = 2^-1 … 2^-10, ires solved 45% to 86% of problems; the proposed method solved 100% (Table 5.2). Stopping tests were deliberately crude: "we implement naïve failure tests in Algorithm B to aggressively challenge the robustness of our approach." The 2010 IPOPT implementation then gave the scale evidence. [stated] (P) On a PDE-constrained server-room airflow problem with hundreds of thousands of variables, "Each iteration of the algorithm required under 9 minutes, a speed-up of over 75% compared to the default Ipopt algorithm, which required approximately 40 minutes per iteration" (research page).
- **Abandoned paths.** [stated] (P) The final remarks defer multiplier boundedness (a safeguard is sketched), fast local rates (via forcing sequences and second-order corrections), and a preconditioner ("preconditioning is an essential part of any implementation for many large-scale problems"; not implemented). The follow-ups show how the deferred items were handled [practice]: rank-deficient Jacobians (2009), nonconvexity (2010), inequalities via IPM (2010), and an IPOPT implementation with PARDISO's iterative solver (2010, 2012). Explicitly abandoned paths are **not documented**.
- **Reception.** [practice] Received Nov 2006, accepted Sep 2007. 83 OpenAlex / 63 Crossref citations. The thesis won the Nemhauser Dissertation Award (2008). The algorithm reached users as an IPOPT option (software page: "Please use the Ipopt option inexact_algorithm yes").
- **Method shown.** M1 (inner solver serves outer solver), M3 (single-component baseline ablation), M6 (build the ladder of cases).

### SW2. The infeasibility line: Byrd, Curtis, Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", SIOPT 20(5):2281–2299, 2010 (DOI 10.1137/080738222), and Curtis, "A penalty-interior-point algorithm for nonlinear constrained optimization", MPC 4(2):181–209, 2012 (DOI 10.1007/s12532-012-0041-4)
Companions: Burke–Curtis–Wang SIOPT 2014 (10.1137/120880045); Burke–Curtis–Wang–Wang SIOPT 2015 (10.1137/130950239) and 2020 (10.1137/18M1176488); Curtis–Nocedal IMA JNA 2008 "Flexible penalty functions" (10.1093/imanum/drn003).

- **Origin.** [stated] (P) The 2010 abstract says: "This paper addresses the need for nonlinear programming algorithms that provide fast local convergence guarantees regardless of whether a problem is feasible or infeasible." The introduction names the drivers as mixed-integer NLP branch-and-bound (many infeasible subproblems) and parametric studies. On the research page: "A major challenge often overlooked in research on nonlinear optimization is the fact that contemporary techniques often perform poorly when all of the problem constraints cannot be satisfied simultaneously."
- **Why then.** [inferred] MINLP codes built on NLP solvers (the 2012 conclusion cites branch-and-bound) needed fast "infeasible" verdicts. Filter/switching approaches (Fletcher–Leyffer, cited) had the weakness that the switching criterion was hard to design.
- **Key insight.** [stated] (P) Use one exact-penalty SQP iteration and treat the **penalty-parameter update rule** as the design object, so that the same method converges superlinearly to an optimum or to an infeasible stationary point. From the research page: "The key idea in this work is to carefully monitor progress toward constraint satisfaction, and to rapidly transition to minimizing constraint violation when consistent progress is not being made." PIPAL carries this into a penalty-interior-point subproblem whose novelty, per its abstract, is "not only on the formulation of the penalty-interior-point subproblem itself, but on the design of updates for the penalty and interior-point parameters."
- **Minimum evidence.** 2010: [practice] (P) a "prototype MATLAB implementation" on illustrative examples (numerics not read in detail). 2012: [practice] (P) the evidence design is the notable part:
  - Head-to-head with IPOPT 3.9 (MA27) on 438 CUTEr AMPL models, with AMPL presolve off "so as to test the algorithms on difficult constraint sets".
  - IPOPT features (bound relaxation, initial-point modification) adopted "for the purpose of providing a fairer comparison".
  - Honest result on the standard set: "all three algorithms are robust, though PIPAL-a and especially IPOPT have an edge in terms of efficiency".
  - The claim is then tested on **constructed variants of Hock–Schittkowski**: degenerate (add −c_i(x)² ≤ 0, 120 problems) and infeasible (add c_i(x)² ≤ −1, 105 problems). On these IPOPT "fails for many of the remaining problems". In Curtis's words: "We admit that creating instances in this manner only produces a certain type of degeneracy, but these models are sufficient for illustrating the robustness of our software on certain rank-deficient problems."
  - Resource limits: Matlab R2010b on an 8-core Opteron; problems whose initial Newton matrix had 20,000 or more nonzeros were removed "due to memory limitations in Matlab".
- **Abandoned or open paths.**
  - [stated] (P) The conclusion hopes that "with a more sophisticated implementation, our algorithm has the potential to be a successful general-purpose solver". [practice] PIPAL stayed a Matlab prototype (PIPAL 1.0 and 1.1 on the software page; GitHub); I found no later PIPAL paper. [inferred] The general-solver ambition was not pursued.
  - [stated] (P) The research page describes "on-going work" on minimizing f subject to v(x) ≤ ε (controlled constraint violation) and calls it "surprisingly not widely explored". [practice] No paper with this formulation is in the CV, DBLP or OpenAlex lists as of 2026 [not found; may be unpublished or dropped].
  - Failure record: [stated] (P) a corrigendum on his errata page gives "A corrected proof of Lemma 4.9" of Burke–Curtis–Wang 2014 (boundedness of search directions).
- **Reception.** [practice] 2010: 84 OpenAlex citations; 2012: 35. [stated] (P) In 2021 he reused the PIPAL comparison as a cautionary example about benchmarking. Slides "Nonconvex Optimization: Opportunities and Challenges", public lecture, ECOM, 2 Apr 2021: "Hard to beat a highly tuned state-of-the-art solver! Curtis (2012)"; "I’ve seen many papers rejected for this reason."; "But if you change the test set, it’s a different picture! Curtis (2012)"; "We should not let one test set (or a few) bias all research."
- **Method shown.** M2 (make the parameter-update rule the contribution), M4 (construct test variants that isolate the claimed feature), M5 (report where the incumbent wins).

### SW3. The nonsmooth line: Curtis & Overton, "A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization", SIOPT 22(2):474–500, 2012 (DOI 10.1137/090780201) → Curtis, Mitchell & Overton, "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", OMS 32(1):148–181, 2017 (DOI 10.1080/10556788.2016.1208749)
Companions: Curtis–Que OMS 2013 and MPC 2015; Burke et al. survey arXiv 1804.11003; Curtis–Robinson–Zhou IMA JNA 2020 self-correcting framework (arXiv 1708.02552); Curtis–Li IJOO 2022; NonOpt MPC 2026; Curtis–Robinson book 2025.

- **Origin.** [practice] (P) He was a postdoc at NYU Courant with Overton, 2007–09 (CV). SQP-GS was received 15 Dec 2009, after he moved to Lehigh. Its NSF acknowledgment (DMS 0602235) is the grant under which, per the 2010 paper's author note, he was supported "while at the Courant Institute". [inferred] The idea is a transfer: his SQP and exact-penalty machinery from the Nocedal group combined with Overton, Burke and Lewis's gradient sampling. The introduction frames it that way: the successes for smooth constrained problems and for nonsmooth unconstrained problems "have laid the groundwork for nonsmooth constrained optimization algorithms."
- **Why then.** [inferred from the paper] GS had just gained convergence theory (Burke–Lewis–Overton 2005; Kiwiel 2007, both cited), and controller-design applications (pseudospectral radius) supplied hard constrained test problems.
- **Key insight (SW3a).** [practice] (P) Put gradient sampling inside an ℓ1-penalty SQP subproblem, sampling gradients of **each** constraint as well as of the objective, which yields convergence with probability one for locally Lipschitz problems.
- **Key insight (SW3b), a reversal.** [stated] (P) The 2017 aim is "to eschew a costly gradient sampling approach entirely". The method keeps BFGS with steering of the penalty parameter and gives up theory: "While our method has no convergence guarantees, we have found it to perform very well in practice on challenging test problems in controller design". Because existing benchmarking tools did not capture the objective / feasibility / budget trade-off, the paper also invents **relative minimization profiles** (RMPs).
- **Minimum evidence.** 2012: [stated] (P) "Preliminary numerical experiments illustrate that the algorithm is effective". 2017: [practice] (P) a new test set of 200 controller-design problems, split into locally Lipschitz (pseudospectral radius) and non-Lipschitz (spectral radius) subsets, against SQP-GS, SNOPT and SFPP. Result: BFGS-SQP "provides no theoretical guarantees yet still manages to provide better overall performance while simultaneously being 14.4 times faster" on the Lipschitz set. On the non-Lipschitz set SQP-GS wins only when it is allowed 10–26.6 times longer.
- **Abandoned paths.**
  - [stated] (P) The 2012 conclusion reports SLP-GS as implemented but inferior: "although the computation time per iteration will generally be less for SLP-GS, the rate of convergence is typically much slower when compared to SQP-GS", and its convergence details were left unworked.
  - [practice] In 2017 the guarantee-carrying SQP-GS was demoted to a comparator of his own new method.
  - [stated] (P) The 2012 acknowledgments credit Kiwiel for comments that "helped to improve the convergence analysis". [inferred] The analysis was repaired during review, which fits the long review (received Dec 2009, accepted Feb 2012, about 26 months).
- **Reception.** [observed] (S)/(P) Both papers are among the six works cited for the 2018 INFORMS Computing Society Prize (1.6). SQP-GS has 132 and BFGS-SQP 105 OpenAlex citations. GRANSO (Mitchell's code) is the released implementation. [practice] The line continues for 14 years: quasi-Newton GS with guarantees (2015), a self-correcting variable-metric framework (2020), inexact subproblems and aggregation (2022), NonOpt (2026), a book (2025), and noisy GS (2026). [stated] (P) At ICCOPT 2019 ("New Quasi-Newton Ideas for (Non)smooth Optimization") he framed his contribution against prior work on a slide titled "What could I say that is new?": earlier methods "Use a bundle method (or other) as the pillar, with BFGS on top" or "Use pure BFGS, but with limited theory"; his stance is to "Use pure BFGS as the pillar" and add damping, cutting planes or gradient sampling only "as needed". "Distinction may seem subtle, but in practice can be significant."
- **Method shown.** M4 (build a domain test set), M5, M7 (invent the evaluation tool when existing ones hide the trade-off), M8 (theory-bearing method first, then a practical variant that may drop theory).

### SW4. Curtis, Robinson, Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization" (TRACE), Math. Prog. 162(1):1–32, 2017. DOI 10.1007/s10107-016-1026-2
Companions: IMA JNA 2019 (arXiv 1708.00475); SIOPT 2018 trust funnel (10.1137/16M1108650); Optim. Lett. 2018 (10.1007/s11590-018-1286-2); MP 2021 regional complexity (10.1007/s10107-020-01492-3); SIOPT 2021 Newton-CG with Royer and Wright (10.1137/19M130563X); SIOPT 2023 TRACE-inexact with Qi Wang (10.1137/22M1492428).

- **Origin.** [stated] (P) The acknowledgments thank "Coralia Cartis, Nicholas I. M. Gould, and Philippe L. Toint for enlightening discussions about the arc algorithm and its theoretical properties that were inspirational for the algorithm proposed in this paper." The introduction states the gap: "Worst-case complexity bounds, on the other hand, have typically been overlooked when analyzing nonconvex optimization algorithms."
- **Why then.** [inferred from the paper] ARC (Cartis–Gould–Toint 2011) had established O(ε^-3/2) and its optimality, which left classical trust-region methods at O(ε^-2). A PhD student (Samadi, 2013–18) and DOE Early Career funding (2013–18, acknowledged) supplied the capacity. Received 21 Oct 2014.
- **Key insight.** [stated] (P) Keep the trust-region framework and its global and fast local guarantees, but change the step-acceptance criteria and the radius update ("contractions and expansions") so that the worst-case bound matches ARC.
- **Minimum evidence.** [practice] (P) Theory only. The MP paper has no numerical section. It assumes exact derivatives and globally solved subproblems ("For simplicity in revealing the salient features"). The Matlab TRACE code was released separately (software page).
- **Abandoned or open paths.**
  - [stated] (P) Inexact subproblem solves: "A complete investigation of these ideas is the subject of current research." [practice] This was closed seven years later by Curtis & Wang, SIOPT 2023.
  - [stated] (P) Sharpness: "We expect that this is also the case for our algorithm, but this has not yet been confirmed." I found no follow-up confirming sharpness [not found].
  - Failure record: [stated] (P) the errata page posts a corrected Lemma 3.19. His note says: "This means that the inequality in the published paper is correct, but not as tight as it could have been."
- **Reception.** [practice] Second most-cited work (167 OpenAlex). About 19 months in review (Oct 2014 to May 2016). It spawned his complexity line of about 10 papers from 2017 to 2024.
- **Self-critique (a later turn).** [stated] (P)
  - 2018 talk "How to Characterize the Worst-Case Performance of Algorithms for Nonconvex Optimization" (with Robinson): "However, there remains a large gap between theory and practice!"; "We’re admitting: Our approach does not give the complete picture." This led to regional complexity analysis (MP 2021).
  - 2021 public lecture, citing TRACE itself: "“Better complexity” has yet to mean “better performance” for nonconvex!" and "Continuous optimization has become too theoretical in recent years!"
  - ICCOPT 2019 slides separate the two lines of his work: "Practical efficiency, not worst-case complexity" for the inexact line, and "Achieving good/optimal complexity for practical algorithms." for the complexity line.
- **Method shown.** M6 (take a known-optimal theory and retrofit it into a practitioner's framework without losing classical guarantees), M9 (question your own evaluation yardstick).

### SW5. Bottou, Curtis, Nocedal, "Optimization Methods for Large-Scale Machine Learning", SIAM Review 60(2):223–311, 2018 (DOI 10.1137/16M1080173; arXiv 1606.04838) → Berahas, Curtis, Robinson, Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", SIOPT 31(2):1352–1379, 2021 (DOI 10.1137/20M1354556; arXiv 2007.10525)

- **Origin.** [practice] (P) Three facts line up in June 2016. The ICML 2016 tutorial "Stochastic Gradient Methods for Large-Scale Machine Learning" (Bottou, Curtis, Nocedal; New York; CV [97]); arXiv v1 of the review on 15 Jun 2016; SIAM Review "Received by the editors June 16, 2016". [inferred] The tutorial and the review were one project. The **turn toward stochastic** predates it: NSF DMS-1319356 "Randomized Models for Nonlinear Optimization" with Scheinberg (2013–16), the sole-author ICML 2016 SC-BFGS paper, and the OptML group (2015).
- **Why then.** [stated] (P) The review's thesis is: "A major theme of this work is that large-scale machine learning represents a distinctive setting in which traditional nonlinear optimization techniques typically falter, and so should be considered secondary to alternative classes of approaches that respect the statistical nature of the underlying problem of interest." [inferred] Deep learning's growth (2012–16) made SG the dominant method, and it had no organizing theory from the nonlinear-programming side.
- **Key insight.** [observed] (S) The prize committee singled out "a new perspective for the simultaneous consideration of noise reduction and ill-conditioning". [stated] (P) The review deliberately avoids numerical horse-races: "Rather than contrast SG and other methods based on the results of numerical experiments—which might bias our review toward a limited test set and implementation details—we focus our attention on fundamental computational trade-offs and theoretical properties of optimization methods."
- **Bridge to his home turf (2020).** [stated] (P) The stochastic-SQP paper transplants the deterministic line-search SQP he had worked on since 2006. From its abstract: "As a starting point for this stochastic setting, an algorithm is proposed for the deterministic setting that is modeled after a state-of-the-art line-search SQP algorithm, but uses a stepsize selection scheme based on Lipschitz constants (or adaptively estimated Lipschitz constants) in place of the line search." It names the new failure mode: "An additional challenge for constrained stochastic optimization is potentially poor behavior of an adaptive merit function parameter that balances emphasis between minimizing constraint violation and reducing the objective function." It then classifies merit-parameter behaviour into events and bounds the bad ones.
- **Minimum evidence (2020).** [practice] (P) The deterministic variant was checked against line-search SQP on CUTE equality-constrained problems ("as reliable … although … sometimes less efficient"). The stochastic variant was run on the same problems with artificial gradient noise at levels ε_N ∈ {1e-8, 1e-4, 1e-2, 1e-1}, 10 runs each, against a stochastic subgradient method on the exact penalty function.
- **Abandoned paths.** Not documented. [stated] (P) Failure record: the errata page posts a corrected statement of "Corollary 3.14 in 'Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization.'"
- **Reception.** [observed] (S) 2021 Lagrange Prize. OpenAlex gives 3,255 citations (Crossref 2,272). Review time: received June 2016, accepted April 2017, published May 2018. arXiv v1→v3 sizes 581→585 KB [inferred: only light revision]. [practice] The 2020 paper opened his largest current line (about 12 papers from 2021 to 2026; §1.2). It also became his plenary topic: NeurIPS workshop 2022 and 2025, ICML workshop 2021, IMA NLA&O 2022, EUCCO 2023, ISMP 2024 semi-plenary (CV).
- **Method shown.** M6 (ladder), M10 (deterministic twin first), M1.

---

## 3. Cross-cutting research moves visible in the publication record (candidates for Phase 2)

These are **practice-level** patterns drawn from the works above. Whether Curtis states them as method is agent 02's question.

| # | Move | Evidence | Tag |
|---|---|---|---|
| M1 | **Make the inner solver serve the outer solver.** Design the subproblem or linear-solver termination from what the globalization (merit function, penalty) needs, not from residual size | Research page: "one needs to design an algorithm in which the demands of the “outer” nonlinear solver are understood by the “inner” subproblem … solver"; SW1; Burke–Curtis–Wang 2020 "Penalty Parameter Updates within the QP Solver"; TRACE-inexact 2023 | [stated]+[practice] (P) |
| M2 | **Treat parameter-update rules (penalty, barrier, merit, radius) as the main design object** | SW2 (PIPAL abstract), flexible penalty 2008, adaptive AL 2015, stochastic-SQP merit-parameter events 2021, TRACE radius update | [practice] (P) |
| M3 | **Baseline that differs in one component** | SW1: ires versus isqp differ only in the GMRES stopping test | [practice] (P) |
| M4 | **Construct test instances that isolate the claimed advantage**, and say how narrow they are | SW2: degenerate and infeasible HS variants; SW3: a 200-problem controller-design set | [practice]+[stated] (P) |
| M5 | **Report where the incumbent wins** | PIPAL on standard CUTEr: "PIPAL-a and especially IPOPT have an edge in terms of efficiency"; the conclusion concedes the difficulty of beating an IPM "performing at its best" | [practice] (P) |
| M6 | **Climb the same ladder in each new information model**: equality → rank-deficient Jacobian → nonconvex → inequality (IPM) → complexity → implementation | Deterministic inexact 2008–2012 (SW1) versus stochastic 2021–2026 (SW5) have parallel title sequences | [practice] (P); deliberate design [inferred] |
| M7 | **Invent the benchmarking lens when existing ones mislead** | RMPs (SW3); 2021 slides on performance-profile and tuning bias | [practice]+[stated] (P) |
| M8 | **A guaranteed method first, then a fast variant that may drop guarantees, compared honestly** | SQP-GS → BFGS-SQP; GS → quasi-Newton GS with guarantees again (2015, 2020) | [practice] (P) |
| M9 | **Audit your own yardstick** | TRACE → "Better complexity has yet to mean better performance" → regional complexity | [stated]+[practice] (P) |
| M10 | **Deterministic twin first**: before randomizing, rebuild the deterministic method without the component that cannot survive noise (e.g. the line search) and show it stays competitive | SW5 abstract | [stated] (P) |
| M11 | **One student, one line; the PI writes the prototype** | §1.3 advisee table; CV "Code written by me" | [stated]+[practice] (P) |

---

## 4. Failures, corrections, abandoned and unfinished directions

| Item | What happened | Source | Tag |
|---|---|---|---|
| Errata policy | "My collaborators and I spend countless hours trying to ensure that all details in our published articles involve no mathematical errors." A journal is contacted only if an error changes "a main conclusion"; smaller errors go on the errata page | Errata page | [stated] (P) |
| Corrigendum 1 | Burke–Curtis–Wang SIOPT 2014: corrected **proof** of Lemma 4.9 | `BurkCurtWang14_corrigendum.pdf` | [practice] (P) |
| Corrigendum 2 | TRACE MP 2017: Lemma 3.19 restated with ½H_Lip; the published inequality is "correct, but not as tight as it could have been" | `CurtRobiSama17_corrigendum.pdf` | [practice] (P) |
| Corrigendum 3 | Berahas–Curtis–Robinson–Zhou SIOPT 2021: corrected **statement** of Corollary 3.14(a) | `BeraCurtRobiZhou21_corrigendum.pdf` | [practice] (P) |
| Retractions | none found | CV, errata page, DBLP | [practice] |
| Rejected papers | none documented for his own work; the 2021 slides say "I’ve seen many papers rejected for this reason" (not beating tuned state-of-the-art solvers) about papers in general | ECOM 2021 slides | [stated] (P); own rejections are a gap |
| SLP-GS | implemented as an option, slower convergence, convergence proof not worked out → SQP-GS preferred | Curtis–Overton 2012 §6 | [stated] (P) |
| SQP-GS's theory-first route | superseded in practice by BFGS-SQP, which has no guarantees | Curtis–Mitchell–Overton 2017 | [practice] (P) |
| PIPAL as general-purpose solver | hoped for in 2012; no further PIPAL paper found | MPC 2012 conclusion; CV | [stated]; abandonment [inferred] |
| "min f s.t. v(x) ≤ ε" for infeasible models | described as ongoing on the research page; no matching publication found | research page; CV | [stated]; status unknown |
| TRACE sharpness | expected, "not yet … confirmed"; no follow-up found | MP 2017 conclusion | [stated] (P) |
| AggQN for SR1 / Broyden class | "For SR1 and Broyden class, not so easy." No paper found | ICCOPT 2019 slides | [stated] (P); not pursued [inferred] |
| NonOpt scope | 2019 title "Non(-linear/-smooth/-convex) Optimizer" → 2025 unconstrained locally-Lipschitz minimizer | talks page; arXiv 2503.22826 | [observed]; narrowing [inferred] |
| Student line not completed | one co-advised PhD student (second-order cone sensitivity analysis, with Terlaky) "left program prior to completing proposal" | CV | [stated] (P) |
| Long reviews | SQP-GS about 26 months (Dec 2009 → Feb 2012); TRACE about 19 months (Oct 2014 → May 2016); infeasibility SQP about 17 months (Oct 2008 → Mar 2010) | received/accepted lines on the papers | [practice] (P) |

---

## Contradictions (kept, not reconciled)

1. **"Too theoretical" versus his own complexity output.** In 2021 he says "Continuous optimization has become too theoretical in recent years!" and "“Better complexity” has yet to mean “better performance” for nonconvex!", citing his own TRACE. Yet from 2017 to 2024 he published about 10 complexity papers, including TRACE, which has no numerical section. In 2019 he framed the complexity line as "Achieving good/optimal complexity for practical algorithms." Both positions are primary and time-stamped: TRACE submitted 2014; slides 2018, 2019, 2021.
2. **Numerics as evidence versus numerics as bias.** His algorithm papers rest on head-to-head numerics (PIPAL versus IPOPT; BFGS-SQP versus SQP-GS/SNOPT). The SIAM Review declines numerical comparison because it "might bias our review toward a limited test set", and the 2021 slides say comparisons are fair only if they "include all computational time spent tuning each algorithm". His own papers do not report tuning time [inferred from the parts read].
3. **Guarantees.** BFGS-SQP (2017) was published with "no convergence guarantees" and praised for it. The 2015 and 2020 nonsmooth quasi-Newton papers exist to restore guarantees ("with global convergence guarantees" is in the 2015 title).
4. **Citation counts disagree by source.** SIAM Review: OpenAlex 3,255, Crossref 2,272. TRACE: 167 against 96. Google Scholar was not read.
5. **Bibliographic sources disagree on the corpus.** OpenAlex includes a wheat-royalties report that is not his; DBLP omits all of his IMA JNA papers, which the CV lists (e.g. "Handling nonpositive curvature in a limited memory steepest descent method", IMA JNA 2016, 10.1093/imanum/drv034). The CV is taken as authoritative.
6. **Authorship-position statistics.** The OpenAlex script's period table sums to 81 "first" positions. The CV footnote says ordering is alphabetical. The raw statistic is kept in `publications.md` but should not be read as leadership.

## Gaps

- Google Scholar profile not read (CAPTCHA); Semantic Scholar not read (HTTP 429). No independent citation count beyond OpenAlex and Crossref.
- **Origin stories in his own voice**, e.g. why he joined Overton, who proposed inexact SQP, how the SIAM Review was commissioned: none found in this pass. Agent 02 should check interviews and the video talks page (`/talks/talks-video/`, not opened).
- The dissertation text was not read (only its DataCite record).
- Numerical sections were read only for Byrd–Curtis–Nocedal 2008, PIPAL 2012, BFGS-SQP 2017 and stochastic SQP 2020 (partly). The infeasibility 2010 numerics, the SIAM Review body, the IMA JNA 2019 v1→v4 changes (44 KB → 108 KB) and the ICML 2016 paper were not read.
- No record of rejected submissions, referee reports or rebuttals.
- Pre-2014 technical-report circulation (Optimization Online, Northwestern OTC reports) not checked.
- The 2018 Optimization Letters best-paper award is not tied to a named paper in the CV (match inferred).
- Semi-plenary and plenary slides from 2022–2025 (stochastic constrained line) were not read. Only 4 slide decks (2018, 2019, 2021 ×2) were read.
- Nothing saved to `references/sources/talks/`: no transcripts were made in this pass, and slide PDFs stay in scratch (copyright).

## Sources

One line each: title, author(s), date, URL or DOI, primary/secondary.

1. DBLP person record pid 61/7604 via SPARQL (`scripts/dblp_works.py`), DBLP, fetched 2026-09-28, https://dblp.org/pid/61/7604.html (secondary)
2. OpenAlex author A5005028153 works (`scripts/fetch_publications.py --orcid 0000-0001-7214-9187`), fetched 2026-09-28, output in `references/sources/publications/publications.md` (secondary)
3. Frank E. Curtis homepage, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/ (primary)
4. Research page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/research/ (primary)
5. Publications (chronological, with BibTeX), Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/publications/publications-chronological/ (primary)
6. Software page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/software/ (primary)
7. Collaborators/Students/Postdocs page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/collaborators/ (primary)
8. Errata page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/errata/ (primary)
9. Talks page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/talks/ (primary)
10. Curriculum Vitae (last revised 7 Apr 2026), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf (primary)
11. Faculty profile "Frank E. Curtis", Lehigh P.C. Rossin College, accessed 2026-09-28, https://engineering.lehigh.edu/faculty/frank-e-curtis (secondary)
12. arXiv author search "Curtis, Frank E", arXiv, accessed 2026-09-28, https://arxiv.org/search/?query=Curtis%2C+Frank+E&searchtype=author (secondary)
13. Bottou, Curtis, Nocedal, Optimization Methods for Large-Scale Machine Learning, arXiv abs (v1 2016-06-15 … v3 2018-02-08), arXiv:1606.04838 (primary)
14. Berahas, Curtis, Robinson, Zhou, Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization, arXiv abs + v1 PDF 2020-07-20, arXiv:2007.10525 (primary)
15. Burke, Curtis, Lewis, Overton, Simões, Gradient Sampling Methods for Nonsmooth Optimization, arXiv abs 2018-04-29, arXiv:1804.11003 (primary)
16. Zhu et al., Low-Order Explicit Hessian Imitation Method for Large-Scale Supervised Machine Learning, 2026-05-07, arXiv:2605.06945 (primary)
17. Curtis, Zebiane, NonOpt: Nonconvex, Nonsmooth Optimizer, 2025-03-28, arXiv:2503.22826 (primary)
18. Curtis, Robinson, Samadi, An Inexact Regularized Newton Framework … O(ε^-3/2), arXiv abs v1–v4 2017–2018, arXiv:1708.00475 (primary)
19. Curtis, Guo, Robinson, A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization, 2026-08-12, arXiv:2608.12665 (primary)
20. Curtis, Guo, Robinson, Progressively Sampled Equality-Constrained Optimization, 2025-10-01, arXiv:2510.00417 (primary)
21. Curtis, Robinson, Zebiane, Active-Set Identification in Noisy and Stochastic Optimization, 2025-08-31, arXiv:2509.00888 (primary)
22. Curtis, Qu, Robinson, A Proximal-Gradient Method for Solving Regularized Optimization Problems with General Constraints, 2025-12-29, arXiv:2512.23166 (primary)
23. Berahas, Curtis, Zebiane, A Gradient Sampling Algorithm for Noisy Nonsmooth Nonconvex Optimization, 2026-03-31, arXiv:2604.00278 (primary)
24. Curtis, Jiang, Wang, Single-Loop Deterministic and Stochastic Interior-Point Algorithms for Nonlinearly Constrained Optimization, 2024-08-29, arXiv:2408.16186 (primary)
25. Crossref REST API checks of 18 DOIs (titles, venues, years, counts), Crossref, 2026-09-28, https://api.crossref.org/works/ (secondary)
26. DataCite record for the PhD thesis "Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization", Curtis, 2007, DOI 10.21985/n2r99v (secondary record of a primary work)
27. Byrd, Curtis, Nocedal, An Inexact SQP Method for Equality Constrained Optimization, SIAM J. Optim. 19(1) 2008, DOI 10.1137/060674004, PDF from homepage (primary)
28. Byrd, Curtis, Nocedal, Infeasibility Detection and SQP Methods for Nonlinear Optimization, SIAM J. Optim. 20(5) 2010, DOI 10.1137/080738222, PDF from homepage (primary)
29. Curtis, A penalty-interior-point algorithm for nonlinear constrained optimization, Math. Prog. Comp. 4(2) 2012, DOI 10.1007/s12532-012-0041-4, PDF from homepage (primary)
30. Curtis, Overton, A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization, SIAM J. Optim. 22(2) 2012, DOI 10.1137/090780201, PDF from homepage (primary)
31. Curtis, Mitchell, Overton, A BFGS-SQP method … relative minimization profiles, Optim. Methods Softw. 32(1) 2017, DOI 10.1080/10556788.2016.1208749, PDF from homepage (primary)
32. Curtis, Robinson, Samadi, A trust region algorithm with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization, Math. Prog. 162(1) 2017, DOI 10.1007/s10107-016-1026-2, PDF from homepage (primary)
33. Bottou, Curtis, Nocedal, Optimization Methods for Large-Scale Machine Learning, SIAM Review 60(2) 2018, DOI 10.1137/16M1080173, PDF from homepage (introduction read) (primary)
34. Corrigendum, Lemma 4.9 of Burke–Curtis–Wang 2014, Curtis (errata page), http://coral.ise.lehigh.edu/frankecurtis/files/errata/BurkCurtWang14_corrigendum.pdf (primary)
35. Corrigendum, Lemma 3.19 of Curtis–Robinson–Samadi 2017, http://coral.ise.lehigh.edu/frankecurtis/files/errata/CurtRobiSama17_corrigendum.pdf (primary)
36. Corrigendum, Corollary 3.14 of Berahas–Curtis–Robinson–Zhou 2021, http://coral.ise.lehigh.edu/frankecurtis/files/errata/BeraCurtRobiZhou21_corrigendum.pdf (primary)
37. Slides "Nonconvex Optimization: Opportunities and Challenges" (public lecture, ECOM, 2 Apr 2021), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/talks/2021_ecom_public.pdf (primary)
38. Slides "Optimization Methods for Large-Scale Machine Learning" (keynote, ECOM, 2 Apr 2021), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/talks/2021_ecom.pdf (primary)
39. Slides "New Quasi-Newton Ideas for (Non)smooth Optimization" (ICCOPT semi-plenary, Aug 2019), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/talks/iccopt_semi_19.pdf (primary)
40. Slides "How to Characterize the Worst-Case Performance of Algorithms for Nonconvex Optimization" (US-Mexico Workshop 2018), Curtis & Robinson, http://coral.ise.lehigh.edu/frankecurtis/files/talks/us-mex_18.pdf (primary)
41. Burke, Curtis, Lewis, Overton, "The Gradient Sampling Methodology" (prize highlights article), 14 Jan 2019, https://cs.nyu.edu/~overton/papers/pdffiles/gs_highlights.pdf (primary)
42. "Frank E. Curtis was co-awarded the 2021 Lagrange Prize in Continuous Optimization", Lehigh Rossin College news, 31 Mar 2021, https://engineering.lehigh.edu/news/article/frank-e-curtis-was-co-awarded-2021-lagrange-prize-continuous-optimization (secondary)
43. INFORMS Computing Society Prize winners list (2018: Burke, Curtis, Lewis, Overton), INFORMS, accessed 2026-09-28, https://www.informs.org/Recognizing-Excellence/Community-Prizes/INFORMS-Computing-Society/INFORMS-Computing-Society-Prize (secondary)
44. Google Scholar profile Zfd6irsAAAAJ: attempted, blocked by CAPTCHA, **not read** (listed for completeness; not counted as consulted content)
