# 06 · Research trajectory

> Research date: 2026-09-27. Biographical facts come from institutional bios and Wikipedia as shown in search snippets (secondary unless noted). Exact start/end years not shown in any snippet are marked "≈" or ⚠️.

## 1. Timeline

| Period | Position / event | Research focus (verified works) | Pivot trigger (evidence / inference) | Source |
|---|---|---|---|---|
| to 1992 | Undergraduate degree in operations research, Lomonosov Moscow State University (born in Moscow) | — | — | https://en.wikipedia.org/wiki/Katya_Scheinberg (secondary) |
| 1992–1997 | PhD in operations research, Columbia University (1997). Advisor D. Goldfarb (verified via Wikipedia, 2026-09-27) | DFO begins: Conn–Scheinberg–Toint, Math. Program. 1997 | *Inference*: collaboration with Conn (IBM) during/after PhD | Wikipedia; IDFO blurb (PhD 1997, Columbia; via search summary) |
| ≈1997–≈2010 | Research staff member, IBM T. J. Watson Research Center ("for over a decade") | Model-based DFO (1997; CSV 2008; book 2009; Scheinberg–Toint 2010; Zhang–Conn–Scheinberg 2010), open-source DFO code; ML optimization (Fine–Scheinberg JMLR 2001; Scheinberg–Ma–Goldfarb NIPS 2010) | Industrial lab: applied black-box problems + ML problems side by side | Wikipedia; IDFO blurb (primary co-authored text) |
| 2009 | *Introduction to Derivative-Free Optimization* (SIAM, with Conn and Vicente) | Consolidates Arc 1 | — | http://www.mat.uc.pt/~lnv/idfo/ |
| ≈2010s–2019 | Harvey E. Wagner Endowed Chair Professor, Industrial and Systems Engineering, Lehigh University (start year ⚠️) | **Pivot to probabilistic models**: BSV 2014; STORM 2018; Cartis–Scheinberg 2018; Blanchet et al. 2019; Paquette–Scheinberg 2020; SIAM News essay (Mar 2019, bio lists Lehigh chair) | *Inference*: randomized sampling in DFO + stochastic ML objectives made deterministic model certification the bottleneck | Wikipedia; SIAM News bio (https://www.siam.org/publications/siam-news/articles/knowing-what-to-know-in-stochastic-optimization/) |
| 2015 | Lagrange Prize in Continuous Optimization (MOS–SIAM), with Conn and Vicente, for the IDFO book | Recognition of Arc 1 | — | Wikipedia / KAUST bio (secondary) |
| 2019–2024 | Professor, School of Operations Research and Information Engineering, Cornell University | Gradient-estimator comparison with ML (FoCM 2022); high-probability bounds (Jin–Scheinberg–Xie, arXiv 2021 → SIOPT 2024; Cao–Berahas–Scheinberg, arXiv 2022 → Math. Program. 2024) | *Inference*: move from expected to tail bounds reflects ML-style "single run" guarantees | https://www.orie.cornell.edu/spotlights/welcome-katya-scheinberg (existence; content unread) |
| July 2024– | Coca-Cola Foundation Chair and Professor, H. Milton Stewart School of ISyE, Georgia Tech | Return to Powell-style model-based DFO with complexity (arXiv 2025, 2026); unreliable/heavy-tailed oracles (arXiv 2025) | *Inference*: Arc 2 tools now strong enough to analyse Arc 1 algorithms | https://www.isye.gatech.edu/users/katya-scheinberg (secondary) |
| July 2025– | Chair, Mathematical Optimization Society; co-editor, Mathematical Programming | Service | — | Georgia Tech / KAUST bios (secondary) |
| undated | INFORMS Fellow; SIAM Fellow; Farkas Prize (INFORMS Optimization Society; year ⚠️); past EiC Mathematics of Operations Research; past chair SIAG/OPT; EiC SIAM-MOS book series; editor of Optima (✗ Corrected 2026-09-27: co-editor of Optima (with A. Caprara, under editor A. Lodi, 2009) [card S143, p. 10], not editor. See §14.) | — | — | https://obd.kaust.edu.sa/speakers/detail/katya-scheinberg (secondary) |

## 2. Pivots and their triggers (summary)

1. **Deterministic → probabilistic models (≈2013–2014).** Evidence: BSV 2014 (arXiv:1304.2808) keeps the Arc 1 trust-region machinery and changes only the model-accuracy assumption. Trigger: *inference* (random sampling/sparse recovery ideas; stochastic ML objectives).
2. **Convergence → complexity → high-probability complexity (2015–2024).** Evidence: arXiv:1505.06070 (2015) → arXiv:1609.07428 (2016) → arXiv:2106.06454 (2021) → arXiv:2205.03667 (2022).
3. **Stochastic oracles → unreliable/heavy-tailed oracles (2025).** Evidence: arXiv:2511.19411.
4. **Return to Powell (2025–2026).** Evidence: arXiv:2510.14935; arXiv:2609.09441.

Entry timing: Scheinberg entered model-based DFO early (1997, before the field had a textbook) and entered stochastic adaptive methods (2014) before high-probability analysis of adaptive methods became standard (*inference*: most third-party titles on the topic found in searches date from 2021 onward).

## 3. Latest 12 months (Sept 2025 – Sept 2026)

- **arXiv:2510.14935** (Oct 2025) — "On Complexity of Model-Based Derivative-Free Methods", Chaudhry & Scheinberg. One search summary describes it as an ICM 2026 proceedings contribution ⚠️ (not independently confirmed).
- **arXiv:2511.19411** (Nov 2025) — "Stochastic Adaptive Optimization with Unreliable Inputs: A Unified Framework for High-Probability Complexity Analysis", Scheinberg + one co-author (name ⚠️).
- **arXiv:2609.09441** (submitted 2026-09-08) — "Powell-Style Model-Based Derivative-Free Optimization with Complexity Guarantees", Chaudhry, Scheinberg & Sun.
- Service: MOS Chair and Math. Programming co-editor since July 2025 (just outside the 12-month window, ongoing).
- Leads not attributable (authors unverified ⚠️): "Robust Accelerated Adaptive Search: High-Probability Complexity Bounds under Bounded-Moment Stochastic Oracles" (arXiv:2604.15526, Apr 2026) — same problem family, may or may not involve Scheinberg.

## 4. Not covered

- Exact years for Lehigh start and IBM departure; Farkas Prize year; PhD advisor; full list of recent talks.

---

## Update 2026-09-27 (deepening pass)

### 5. Corrections and filled gaps

| Item | Previous status | Now | Source |
|---|---|---|---|
| Lehigh start | "≈2010s" ⚠️ | Joined Lehigh ISE in **2010**. Harvey E. Wagner Chair from **2014**. Left for Cornell ORIE in July 2019 | Lehigh ISE newsletter / Cornell welcome page (search summaries): https://engineering.lehigh.edu/news/article/postdocs-lehigh-ise-tradition-excellence ; https://www.engineering.cornell.edu/spotlights/welcome-katya-scheinberg |
| Farkas Prize year | ⚠️ | **2019** (INFORMS Optimization Society; Scheinberg was at Cornell at the time) | https://connect.informs.org/optimizationsociety/prizes/farkas-prize/2019 |
| SIAM Fellow | undated | **Class of 2025**. Cited for foundational contributions to DFO and optimization applications in data science, and for service (paraphrase) | https://www.isye.gatech.edu/news/coca-cola-foundation-chair-katya-scheinberg-selected-2025-class-siam-fellows |
| Co-author of arXiv:2511.19411 | ⚠️ | **Miaolan Xie** (verified) | https://arxiv.org/abs/2511.19411 |
| ICM 2026 | ⚠️ one snippet | Scheinberg is an ICM 2026 **section lecturer (Control Theory and Optimization)** (Georgia Tech news summary). arXiv:2510.14935 is listed as ICM 2026 proceedings on the co-author's homepage | https://math.gatech.edu/news/school-mathematics-professor-john-etnyre-speak-icm-2026 ; https://chaudhrya.github.io/ |
| arXiv:2604.15526 (RAAS) | "may or may not involve Scheinberg" | **Not Scheinberg's** (Zhang, Liao, Han, Guo; UCAS) | https://arxiv.org/abs/2604.15526 |

### 6. Invited-talk timeline (verified titles/dates)

| Date | Venue | Title | Signal |
|---|---|---|---|
| 24 May 2017 | SIAM Conference on Optimization (OP17), Vancouver, plenary | Using Second-order Information in Training Large-scale Machine Learning Models | Lehigh-era ML optimization (LHAC 2016, SARAH 2017) |
| 2017 | INFORMS TutORials (with F. E. Curtis) | Optimization Methods for Supervised Machine Learning: From Linear Models to Deep Learning | Teaching ML optimization to OR |
| 2020 | IEEE Signal Processing Magazine (with Curtis) | Adaptive Stochastic Optimization (overview) | Consolidates the adaptive-methods programme |
| 2021 | INFORMS Annual Meeting, Anaheim | Stochastic First Order Oracles and Where to Find Them | Oracle-first programme becomes the headline talk |
| 2022 | MICDE Winter seminar (video); later MIT ORC, Princeton, Cornell CAM (Feb 2023), NC State (Mar 2023) | Overview of Adaptive Stochastic Optimization Methods | Martingale / stopping-time view stated |
| 2022 | NeurIPS OPT workshop, plenary | Stochastic Oracles and Where to Find Them | ML audience |
| 17 May 2024 | Waterloo, Distinguished Tutte Lecture | Stochastic Oracles and Where to Find Them | — |
| 10 Apr 2025 | Lehigh ISE Spencer C. Schantz Technical Talk | Stochastic Oracles and Where to Find Them | — |
| 20–30 May 2025 | CRM Montréal, Aisenstadt Chair lectures | Introduction to derivative-free and zeroth order optimization I–II; A study of stochastic and noisy oracles in unconstrained continuous optimization | Course-length synthesis of both arcs |
| 2026 | ICM, section lecture | (title not retrieved; companion paper arXiv:2510.14935) | Powell-style complexity presented to the whole mathematics community |

*Reading (inference):* between 2021 and 2025 one talk title was reused at four venues, which marks it as the core message of this period. By 2025–2026 the public emphasis widened from stochastic oracles to bringing model-based DFO (Arc 1) into that framework, as the Aisenstadt course and the ICM paper show.

### 7. Group generations (from 04-mentorship.md, verified records)

| Period | Students / postdocs (verified) | Line |
|---|---|---|
| Lehigh 2010–2019 | R. Chen (PhD 2015), X. Tang, M. Menickelly (PhD 2017), X. Bai, A. Yektamaram, H. Ghanbari, L. Cao (PhD 2021), M. Li; postdocs C. Paquette (2018), A. S. Berahas (2018–2020) | Random models / STORM; proximal quasi-Newton for ML; stochastic line search; estimators and noise |
| Cornell 2019–2024 | M. Xie (PhD 2019–2024) | High-probability and sample complexity; unreliable inputs |
| Georgia Tech 2024– | A. Chaudhry (Butler postdoctoral fellow) | Powell-style model-based DFO complexity |

### 8. Latest 12 months, updated

- **Aug 2026 (third party):** Cartis & Roberts, "A note on the complexity of random subspace model-based methods for DFO" (arXiv:2608.17307), on the same question as Chaudhry–Scheinberg(–Sun).
- **2026:** ICM section lecture; arXiv:2510.14935 in ICM proceedings (co-author's page).
- **May 2025:** Aisenstadt Chair lectures (just outside the window; recorded on YouTube).
- **2025:** JOTA stochastic ISTA/FISTA (Nguyen–Scheinberg–Tran) and Math. Program. sample-complexity paper (Jin–Scheinberg–Xie) published.

---

## Update 2026-09-27 (full-text pass)

Source: `08-deep-reading-synthesis.md` §8–§9, built from the paper cards (`07-paper-cards.md`; 78 papers read in full or in part). Citations like [card S018, pp. 1, 6–8] point to the card and the page of the full text.

### 9. Topics by period (carded works with a year; full or partial reads in brackets)

| Period | Works | IPM/conic | SVM training | Model-based DFO | Structured 1st/2nd-order & sparse | SG & variance reduction | Adaptive stochastic (probabilistic oracles) | Gradient estimation / new oracles | ML models & applications | DFO applications | Service |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1996–2000 | 13 | 7 [0] | 1 [0] | 5 [3] | | | | | | | |
| 2001–2005 | 8 | 3 [2] | 3 [2] | 1 [1] | | | | | | | 1 [0] |
| 2006–2010 | 24 | 1 [0] | 1 [1] | 7 [6] | 7 [3] | | | | 2 [2] | 3 [1] | 3 [1] |
| 2011–2015 | 17 | | | 3 [3] | 10 [7] | | 2 [1] | | | 2 [2] | |
| 2016–2020 | 32 | | | 2 [1] | 3 [3] | 7 [7] | 9 [5] | 1 [1] | 6 [6] | 3 [2] | 1 [0] |
| 2021–2026 | 22 | | | 2 [2] | | 2 [2] | 11 [10] | 5 [3] | 1 [1] | | 1 [0] |

Topic assignment is by card content; three undated records are excluded [08 §8.1].

### 10. Turns, as the full texts show them

1. **Deterministic geometry → probabilistic models (2012–2014).** A rigorous theorem for random sample sets sits next to a deterministic practical code, and a stochastic trust-region framework is named as future work [card S033, pp. 5–6, 21]; two years later the trust region runs on models that are fully linear only with probability ≥ 1/2 [card S018, pp. 1, 6–8]. The certificate became a probability; the algorithm stayed the same. This replaces the *inference* in §2 item 1 with text evidence.
2. **Almost sure → expected complexity (2014–2020).** Almost-sure results only [cards S018, pp. 10–13; S012, p. 25] → hitting-time bounds with exact f [card S014, p. 13] → random f and the renewal-reward framework [card S013, pp. 4–10] → line search [card S015, pp. 17–19] → one template for all adaptive methods [card S047, pp. 7–8].
3. **Expected → high probability and total sample cost (2021–2025)** [cards D001, pp. 7–13; S041, pp. 16–21; S137, pp. 4–5; S057, pp. 12–13], then unreliable inputs with heavy tails and p < 1/2 [card S083, pp. 15–17].
4. **Return to Powell-style DFO with complexity (2025–2026).** The open problem of certifying Powell-like geometry [card S016, p. 24] and the "closest theoretically convergent algorithm" framing of the 2009 essay [card S143, p. 5] come back as complexity results for geometry-correcting methods and random subspaces [cards S088, pp. 1–3, 12–19; S104, pp. 1–2, 10–23], using the stochastic-analysis devices (the η₂ acceptance test from 2014) in the deterministic setting [card S088, pp. 2–3].
5. **New oracles (2026).** Optimization defined by a preference relation alone, with matching lower bounds [card S087, pp. 2–4, 24–26].

### 11. Parallel lines that ended

- Interior-point linear algebra (last read paper 2005) [cards S050; S058].
- SVM training at IBM [cards S003; S059; S022].
- Structured first-order and sparse learning with Goldfarb, Ma, Qin, Tang and Bai (2009–2016) [cards S010; S005; S011; S028; S029; S054; S066].
- Stochastic gradient and variance reduction with L. M. Nguyen and Takáč (2017–2022) [cards S002; S024; S009; S032; S037; S055]. This line does not follow the adaptive-method lens (new estimators with tuned or prescribed steps).
- Student-led ML modelling and applications (2017–2019), which use their host field's data sets and scores [cards S078; S089; S051; S060; S082; S074].

### 12. What stayed constant across 1997–2026

- The classical trust-region / line-search skeleton, changed in one place per paper [cards S008, pp. 17–18; S018, p. 1; S041, pp. 11–12; S104, pp. 4, 24–25].
- Radius-scaled accuracy: κΔ on the ball in 1997–2009 [cards S008, pp. 11–12; S007, pp. 7–8], the same form with probability p from 2014 [card S018, pp. 6–7], with irreducible floors from 2021 [cards S041, pp. 4–5; S083, pp. 2–5].
- Known structure kept exact: cheap constraints in 1998 [card S019, pp. 6–7], the prox term in 2025 [card S098, pp. 2, 4, 7].
- Equal-evaluation benchmarking in DFO from the first practice paper [card S019, p. 10] to 2026 [card S104, pp. 26–30].
- Framework-then-instantiation, from the 1997 survey to the 2025 unified framework [cards S004, pp. 8–16; S083, pp. 12, 18–21] (SKILL.md Heuristic 8; proposed as Method 7 and demoted because exclusivity was not shown, see 08 §4).

### 13. Collaboration pattern by period (research works only; coauthors appearing at least twice in the period)

| Period | Works | Sole-authored | Distinct coauthors | Frequent coauthors (count) |
|---|---|---|---|---|
| 1996–2000 | 13 | 3 | 8 | Conn 4, Toint 4, Goldfarb 3 |
| 2001–2005 | 7 | 0 | 4 | Fine 3, Goldfarb 3 |
| 2006–2010 | 21 | 2 | 38 | Conn 7, Rish 5, Vicente 4, H. Zhang 3, Goldfarb 3, Asadi 3, Ma 2 (plus IBM team papers) |
| 2011–2015 | 16 | 0 | 17 | Goldfarb 5, Bandeira 3, Vicente 3, Ma 2, R. Chen 2, Tang 2, Bai 2, B. Y. Chen 2 |
| 2016–2020 | 27 | 0 | 36 | L. M. Nguyen 5, Takáč 4, Ghanbari 4, Curtis 3, Menickelly 3, Hatalis/Lamadrid/Kishore 3, Cartis 2, Kalagnanam 2 |
| 2021–2026 | 20 | 1 | 20 | M. Xie 6, L. M. Nguyen 4, Berahas 3, Cao 3, Jin 3, Tran 3, Chaudhry 2 |

Overall most frequent: Goldfarb 14 (1998–2014), Conn 12 (1997–2010), Vicente 9 (2003–2017), L. M. Nguyen 9 (2017–2025), M. Xie 6 (2021–2026) [08 §9]. One senior partner per era, then a student or postdoc per line from about 2012; specialists brought in for one step (applied probability for the stopping-time framework [card S013]; a hitting-probability proof credited to J. A. Fill [card S057, p. 20]; an ML co-author for estimator comparisons [cards D003; S006]); industry and laboratory partners (IBM; Goldman Sachs Asset Management [card S021]; Sandia National Laboratories [card S098]). Sole-authored research work is rare: one algorithm and software paper (S022, JMLR 2006: an active-set QP for SVMs, benchmarked against SVMlight and released as SVM-QP) plus position pieces and essays [cards S143; S044]. Author order is alphabetical in some analysis papers and not in others, so it is not evidence of who led.

### 14. Corrections to earlier sections

| Item | Earlier | Now | Source |
|---|---|---|---|
| Optima role (§1 "undated" row) | "editor of Optima" | Co-editor of Optima (with A. Caprara, under editor A. Lodi) in 2009; her article in issue 79 (May 2009) is "Geometry in model-based algorithms for derivative-free unconstrained optimization" | [card S143, pp. 1, 10] |
| Minimal-safeguard stance (implied constant since 1997) | held for 17 years | Geometry-as-certificate dates from 1997 [card S008, pp. 14–17], but in 2008 the stated practice was to maintain poisedness throughout [card S016, p. 18]; the minimal-safeguard stance dates from 2009–2010 | [cards S143, p. 4; S030, pp. 3, 12] |
| ProxSTORM (§3 leads) | third-party, authors unverified | Scheinberg's own paper with Baraldi, Javeed, Kouri (Sandia), arXiv:2510.03187 | [card S098] |
| Pivot trigger 1 (§2) | *inference* | text evidence, see §10 item 1 | [cards S033; S018] |

### 15. Latest (added)

- **2026**: "Function-free optimization via comparison oracles" (Scheinberg, Xiong; arXiv:2604.26867) [card S087]; stochastic cubic regularization in *INFORMS J. Optim.* (DOI 10.1287/ijoo.2025.0123) [card S093].
- **Oct 2025**: ProxSTORM (Baraldi, Javeed, Kouri, Scheinberg; arXiv:2510.03187) [card S098].
- **2026**: MOR 50th-anniversary editor's comments (metadata only) [card S105].
