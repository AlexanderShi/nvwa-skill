# 02 · Stated methodology (what Scheinberg SAID about method)

> Research date: 2026-09-27. Evidence base: search-result snippets only. No transcript, interview text, or full article body could be read (WebFetch blocked for siam.org, cornell.edu, lehigh.edu, gatech.edu, mathopt.org, wikipedia.org).
> **Big caveat:** the stated-methodology layer for Scheinberg is thin in what could be retrieved. Most "stated" evidence below is (a) titles and one-line descriptions of Scheinberg's own essays, talks and tutorials, (b) the framing sentences of author-written abstracts, and (c) institutional bios (usually author-approved). None is a long-form "how I do research" text. This file records only what was said; whether it was done is checked in 03-process-evidence.md.

## A. Scheinberg's own essays, talks, tutorials (primary, but title/summary level)

| # | Item | What it states (paraphrase unless quoted) | Layer | URL | Cred. |
|---|---|---|---|---|---|
| A1 | SIAM News essay "Knowing What to Know in Stochastic Optimization", by Katya Scheinberg, SIAM News vol. 52 issue 02, March 2019 | Title frames the central question as *what an algorithm needs to know* (which accuracy, from which oracle) rather than how to reduce variance everywhere. Search summary: the article "describes novel continuous optimization algorithms, which lie at the core of most foundational data science topics" (summary wording, paraphrase). | Taste / idea generation | https://www.siam.org/publications/siam-news/articles/knowing-what-to-know-in-stochastic-optimization/ | primary (title + summary only) |
| A2 | Lehigh lecture "Stochastic Oracles and Where to Find Them" | Title again puts the **oracle** (what information is available, how reliable) at the centre of the method. | Taste / problem framing | https://engineering.lehigh.edu/node/172051 | primary (title only) |
| A3 | Tutorial video "Introduction to derivative-free and zeroth order optimization II" (YouTube) | Pairs classical DFO with ML's "zeroth-order optimization" under one heading — treats them as the same field. | Framing / bridging | https://www.youtube.com/watch?v=5j8LvlbzsJQ | primary (title only) |
| A4 | Distinguished Tutte Lecture, University of Waterloo C&O | Invited distinguished lecture (content not retrieved). | — | https://uwaterloo.ca/combinatorics-and-optimization/distinguished-tutte-lecture-katya-scheinberg | primary (existence only) |
| A5 | Lehigh ISE Spencer C. Schantz Technical Talk (as Georgia Tech faculty) | Content not retrieved. | — | https://engineering.lehigh.edu/news/article/lehigh-ise-spencer-c-schantz-technical-talk-katya-scheinberg-georgia-institute | primary (existence only) |

## B. Author-written framing in abstracts (primary; these are claims Scheinberg and co-authors chose to foreground)

| # | Paper | Stated framing (paraphrase of snippet unless in quotes) | Layer |
|---|---|---|---|
| B1 | Cartis & Scheinberg, Math. Program. 2018 | "the use of probabilistic models only increases the complexity by a constant, which depends on the probability of the models being good" (abstract wording as shown in search result). → Stated standard for a good stochastic result: **same order as the deterministic method, randomness costs only a constant.** | Result judgement |
| B2 | Paquette & Scheinberg, SIOPT 2020 | The expected-iteration bound "matches the complexity bound of deterministic gradient descent up to constants" (snippet; treat as paraphrase-level). Same standard as B1. | Result judgement |
| B3 | Jin, Scheinberg & Xie, SIOPT 2024 | Unlike stochastic gradient methods, the algorithm does not use pre-specified step sizes but adapts them according to estimated progress (paraphrase). → Stated preference: **adaptivity over hand-tuned schedules.** | Taste / method |
| B4 | Chen, Menickelly & Scheinberg, Math. Program. 2018 | Models and estimates must be accurate "with high enough, but fixed, probability" (snippet). → Stated modelling choice: fixed probability, not increasing-to-one. | Method |
| B5 | Cao, Berahas & Scheinberg, Math. Program. 2024 | Oracles "are not assumed to be unbiased or consistent" (paraphrase); relaxed acceptance + cautious radius update. → Stated aim: weaken oracle assumptions as far as possible. | Method |
| B6 | Berahas, Cao, Choromanski & Scheinberg, FoCM 2022 | Title: "A theoretical **and empirical** comparison…" → Stated evaluation standard: compare competing estimators both ways. | Experiment design |
| B7 | Chaudhry & Scheinberg, arXiv:2510.14935 (2025) | Classical model-based trust-region methods "can have the same worst case complexity as any other known DFO method" (snippet). → Stated position: Powell-type model-based DFO is **not** theoretically inferior to direct search / finite-difference methods. | Taste / agenda |
| B8 | Chaudhry, Scheinberg & Sun, arXiv:2609.09441 (2026) | Methods "closest to methods initially proposed and implemented by Powell" made "theoretically competitive"; random subspaces give what they "believe to be nearly tight complexity" (snippet). | Agenda |
| B9 | Scheinberg & Toint, SIOPT 2010 | Geometry-improving steps "cannot be completely eliminated" for global convergence, but can be confined to the final stage (paraphrase). → Stated standard: identify the minimal necessary safeguard. | Method |
| B10 | Scheinberg et al., arXiv:2511.19411 (2025) | A "unified" framework encompassing line search and trust region under corrupted gradients and heavy-tailed function noise (paraphrase). → Stated aim: one analysis template for many adaptive methods. | Method |

## C. Bios and book blurb (primary for self-description; secondary when written by institutions)

| # | Source | Stated content | Cred. |
|---|---|---|---|
| C1 | SIAM News author bio (via search summary) | Research interests "lie in the development of efficient and theoretically sound algorithms for continuous optimization and machine learning" (wording as shown in search summary). | primary-ish (author bio) |
| C2 | IDFO book blurb (SIAM 2009; Amazon/Google Books records) | Book presents DFO methods "designed to efficiently and rigorously solve optimization problems", covering "direct search to model-based approaches"; Scheinberg "authored the open source DFO software" (blurb wording via search summary; paraphrase-level). | primary (co-authored publisher text) |
| C3 | Georgia Tech / KAUST / Wikipedia bios | Service record (MOS Chair from July 2025; co-editor Math. Programming; past EiC Mathematics of Operations Research; past chair SIAG/OPT; EiC SIAM-MOS book series; editor of Optima; ✗ Corrected 2026-09-27: co-editor of Optima (with A. Caprara, under editor A. Lodi, 2009) [card S143, p. 10], not editor.). Signals the community-building layer, not method. | secondary |

## D. Recurring stated themes (≥3 appearances across A–C)

1. **Oracle-first framing** — A1, A2, B4, B5, B10 (5×). What the oracle guarantees, and with what probability, is the problem definition.
2. **Deterministic-parity standard** — B1, B2, B7, B8 (4×). A stochastic or DFO method is "good" when its complexity matches the deterministic/best-known order, with randomness costing constants.
3. **Classical adaptive methods, not schedules** — B3, B4, B5, B10 (4×). Keep line search / trust region; let the step size adapt.
4. **Theory and empirics together** — B6, B8, C1 ("efficient and theoretically sound"), C2 (3–4×).
5. **DFO ≡ zeroth-order optimization** — A3, B6, C1 (3×).

## E. Stated-but-unverified / missing

- No retrieved text where Scheinberg describes *how problems are chosen*, *how papers are written*, or *how mentoring is done*. Those layers have **no stated evidence** here.
- No retrieved quote on reviewing standards or on critiques of other approaches.

---

## Update 2026-09-27 (deepening pass, ~60 additional searches)

> Same evidence rules as above: search results and snippets only, no full text. The new material raises the stated layer from *titles* to *talk abstracts, a newsletter essay, an overview article and a tutorial*. It is still not a long-form "how I do research" text.

### F. Talk and tutorial abstracts (primary: abstracts are normally written by the speaker)

| # | Item | What it states (paraphrase unless quoted) | Layer | URL | Cred. |
|---|---|---|---|---|---|
| F1 | "Stochastic First Order Oracles and Where to Find Them", INFORMS Annual Meeting 2021 (Anaheim) | Continuous optimization is expanding toward methods that do not need exact objective information, and most of them still use approximate first-order information. The talk gives **a general definition of a stochastic oracle** and applies it to sampled stochastic gradients, traditional and randomized finite differences, and robust gradient estimation. It then asks which properties of such oracles the convergence analysis needs. | Problem framing (Method 1) | https://pubsonline.informs.org/do/10.1287/orms.2021.05.48n/full/ | primary (abstract via search summary) |
| F2 | "Stochastic Oracles and Where to Find Them", plenary, NeurIPS 2022 OPT workshop | Same abstract. Opening sentences as shown in search result: "Continuous optimization is a mature field which has recently undergone major expansion and change. One of the key new directions is the development of methods that do not require exact information about the objective function." | Problem framing | https://neurips.cc/virtual/2022/55786 | primary |
| F3 | Same title: Distinguished Tutte Lecture, Waterloo (17 May 2024); Lehigh ISE Spencer C. Schantz Technical Talk (10 Apr 2025) | Same programme, repeated over four years at four venues. One search summary of the tutorial abstract adds three points: variance directly affects the convergence rate; variance trades off against oracle cost across oracles; **bias affects the neighbourhood of convergence but not the rate** (paraphrase; exact wording not confirmed by a second search). | Result judgement (Methods 1, 3) | https://uwaterloo.ca/combinatorics-and-optimization/events/distinguished-tutte-lecture-katya-scheinberg ; https://engineering.lehigh.edu/news/article/lehigh-ise-spencer-c-schantz-technical-talk-katya-scheinberg-georgia-institute | primary |
| F4 | "Overview of Adaptive Stochastic Optimization Methods" (MIT ORC; Princeton; Cornell CAM colloquium 10 Feb 2023; NC State 27 Mar 2023; MICDE Winter 2022 seminar video) | Stochastic variants of adaptive methods (step search, trust region, cubic regularization) let the **step-size parameter dictate the accuracy required** of stochastic approximations. Those requirements are therefore adaptive and may be biased or even inconsistent. The step parameter is not bounded away from zero, which obstructs complexity analysis. **Viewing the algorithms as stochastic processes with martingale behaviour** gives expected-complexity bounds that also hold with high probability. Applications listed: expectation minimization, black-box and simulation optimization, and corrupt samples. | Method statement (Methods 1, 2, 3) | https://orc.mit.edu/events/overview-adaptive-stochastic-optimization-methods ; https://www.youtube.com/watch?v=OVSnPO3FBxY | primary (abstract via search summary) |
| F5 | Aisenstadt Chair lectures, CRM Montréal, 20–30 May 2025: "Introduction to derivative-free and zeroth order optimization I/II"; "A study of stochastic and noisy oracles in unconstrained continuous optimization" | Titles again join DFO and zeroth-order optimization and centre the course on oracles. The word "unconstrained" states the scope explicitly. | Framing; scope | https://www.youtube.com/watch?v=Szz3J0eBCWk ; https://www.youtube.com/watch?v=5j8LvlbzsJQ ; https://www.youtube.com/watch?v=1zS8v_B1JPM ; https://www.crmath.ca/en/prizes-and-honours/aisenstadt-chairs/ | primary (titles) |
| F6 | SIAM Conference on Optimization 2017 (Vancouver) plenary: "Using Second-order Information in Training Large-scale Machine Learning Models" | Title only. States an interest in second-order methods for ML, matched by the practice record (LHAC, Math. Program. 2016; SARC 2023). | Taste | https://archive.siam.org/meetings/op17/invited.php | primary (title via search summary) |

### G. Essays, overviews, tutorials (primary)

| # | Item | What it states | Layer | URL |
|---|---|---|---|---|
| G1 | Scheinberg, article in *Optima* 79 (Mathematical Programming Society newsletter; ≈2009; exact title not retrieved) | Search summaries of the article: it discusses the Moré–Wild numerical experiments showing Powell's model-based method is very effective despite the low accuracy of its quadratic models. The main point is that one needs to impose **only minimal quality controls** to promote convergence and ensure good performance (paraphrase of search-summary wording). ✗ Corrected 2026-09-27 (full text, card S143, pp. 4, 6): the Moré–Wild framing and the "only minimal quality controls" wording are from Jorge Nocedal's discussion column in the same issue (p. 6), which presents them as a summary of her essay ("As Scheinberg discusses in this issue of Optima, …"); Moré–Wild is not in her reference list. Her own statement is p. 4: "it turns out that it is not necessary to compute extra sample points unless the gradient of the model becomes small." Title: "Geometry in model-based algorithms for derivative-free unconstrained optimization" (May 2009) [card S143, p. 1]. | Method statement (Method 4) | https://www.mathopt.org/Optima-Issues/optima79.pdf |
| G2 | Curtis & Scheinberg, "Adaptive stochastic optimization: a framework for analyzing stochastic optimization algorithms", *IEEE Signal Processing Magazine* 37(5), 32–42 (2020) | Summarises the research on adaptive stochastic methods and contrasts them with non-adaptive SG approaches whose parameters must be tuned for each application. Adaptive methods may offer significant computational savings (paraphrase). | Taste (Method 2) | https://ieeexplore.ieee.org/document/9194022/ ; arXiv:2001.06699 |
| G3 | Curtis & Scheinberg, "Optimization methods for supervised machine learning: from linear models to deep learning", INFORMS *TutORials in OR* (2017) | Introduces "key models, algorithms, and open questions" of optimization for ML to an INFORMS audience that knows optimization but less ML (paraphrase of abstract). Covers first-order, stochastic gradient, variance-reduced and second-order methods. | Framing / teaching | https://doi.org/10.1287/educ.2017.0168 ; arXiv:1706.10207 |

### H. New author-written abstract framing (primary)

| # | Paper | Stated framing | Layer |
|---|---|---|---|
| H1 | Paquette & Scheinberg arXiv v1 (2018, "…with Convergence Rate Analysis") | For deterministic optimization, line search provides stability and improved efficiency. The paper adapts classical backtracking Armijo to the stochastic setting, with accuracy "dynamically adjusted" and holding with a sufficiently large, but fixed, probability (paraphrase). | Method 2 |
| H2 | Berahas, Cao & Scheinberg, SIOPT 31 (2021) | The paper *extends the framework* built for exact function values and random gradients to noisy functions. Noise is bounded in absolute value "without any additional assumptions". Two alternative gradient conditions are given (paraphrase). | Method 1, 3 |
| H3 | Jin, Scheinberg & Xie, Math. Program. 209 (2025) | Step-size parameters in stochastic adaptive methods are not bounded away from zero because of oracle failures, and bounds on them had not been derived before. This states a **gap** and closes it (paraphrase). | Result judgement / agenda |
| H4 | Scheinberg & Xie, arXiv:2308.13161 | SARC outperforms other stochastic adaptive methods, "as in the deterministic case" (paraphrase). The deterministic ordering of methods is the benchmark for the stochastic ordering. | Deterministic parity |
| H5 | Scheinberg & Xie, arXiv:2511.19411 | The first iteration-complexity analysis in this setting with high-probability bounds on the stopping time. The tail decays exponentially or polynomially depending on the zeroth-order oracle assumptions (paraphrase). | Method 3 |
| H6 | Nguyen, Scheinberg & Tran, JOTA 205 (2025) | Stochastic ISTA/FISTA analysed **without assuming an unbiased stochastic gradient**. The inexact fixed-step analysis is extended to backtracking (paraphrase). | Method 1, 2 |
| H7 | Chaudhry & Scheinberg, arXiv:2510.14935 | Theoretical complexity analysis "lags behind practice" for Powell-type model-based methods (paraphrase). The paper sets out to close that gap. | Agenda (Method 4) |

### I. Prize citations and profiles (secondary; institution-written)

| # | Item | Content | URL |
|---|---|---|---|
| I1 | SIAM Fellow, class of 2025 | Recognised for foundational contributions to derivative-free optimization and optimization applications in data science, and for service to the optimization community (paraphrase of Georgia Tech news summary). | https://www.isye.gatech.edu/news/coca-cola-foundation-chair-katya-scheinberg-selected-2025-class-siam-fellows |
| I2 | Lagrange Prize 2015 (with Conn, Vicente; for the IDFO book) | Citation as shown in search result: "A small sampling of the direct impact of their work is seen in aerospace engineering, urban transport systems, adaptive meshing for partial differential equations, and groundwater remediation." | https://www.uc.pt/en/fctuc/dmat/noticias/LagrangePrize ; https://www.mathopt.org/?nav=lagrange |
| I3 | Farkas Prize 2019 (INFORMS Optimization Society) | Award page exists; citation text **not retrieved**. | https://connect.informs.org/optimizationsociety/prizes/farkas-prize/2019 |
| I4 | ICM 2026 section lecture, Control Theory and Optimization | Invited section lecturer (search summary of a Georgia Tech news page). The companion paper arXiv:2510.14935 is listed as ICM 2026 proceedings on the co-author's homepage. | https://math.gatech.edu/news/school-mathematics-professor-john-etnyre-speak-icm-2026 ; https://chaudhrya.github.io/ |
| I5 | MOS Chair | Took office mid-2025 (July per Georgia Tech bio; an Optima summary says August 2025). **No Chair's column or statement on publication culture was found.** | https://www.mathopt.org/Optima-Issues/optima107.pdf (predecessor's column) |

### J. Revised recurring themes (count includes sections A–I)

1. **Oracle-first framing**: A1, A2, B4, B5, B10, F1–F5, H2, H6 (≥12×, over 2019–2025, at four venues with the same talk). This is now the best-evidenced stated principle.
2. **Algorithms analysed as stochastic processes (martingales / stopping times)**: F4, H5, plus the 2019 title (3× stated). The stated side of Method 3 is no longer abstract framing only.
3. **Deterministic parity**: B1, B2, B7, B8, H4 (5×).
4. **Adaptive methods over tuned schedules**: B3, F4, G2, H1 (4×).
5. **Minimal quality control / minimal safeguard**: G1 (2009 essay), B9 (2010), H7 context (3×). This is now stated in Scheinberg's own words (paraphrase), not only practised. ✗ Corrected: her own words are the p. 4 sentence of the essay, not the "minimal quality controls" paraphrase, which is Nocedal's column [card S143, pp. 4, 6]; the stance dates from 2009–2010, while in 2008 the stated practice was to maintain poisedness throughout [card S016, p. 18].
6. **Bias sets the neighbourhood; variance and cost set the rate**: F3, H2 (2×; the exact wording is unconfirmed).
7. **DFO ≡ zeroth-order**: A3, F5, C1 (3×).

### K. Still missing

- No long-form interview, podcast, oral history or "advice to students" text was found.
- No MOS Chair statement, and no SIAG/OPT Views-and-News article by Scheinberg was found. The Optima 79 article title was not retrieved.
- No talk transcript was read, so the talk abstracts are known only through search summaries.
