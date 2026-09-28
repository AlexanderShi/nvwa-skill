# 06 · Research Trajectory (Stephen J. Wright)

> **Researcher:** Stephen J. Wright (UW-Madison Computer Sciences since 2001; Argonne National Laboratory MCS 1990–2001; NC State Mathematics 1986–90; Univ. of Arizona before that; PhD Univ. of Queensland 1984), living.
> **Dimension:** research agent 06 of 06, research trajectory: academic timeline, lineage, direction changes and what triggered them, when he enters and leaves a topic, and the last 12 months (nuwa research-craft Phase 1).
> **Research date:** 2026-09-28. **Sources consulted:** 44, as listed in Sources (17 primary, 23 secondary, 4 services that returned nothing). 5 of the 44 could not be read and are marked as such. **WebSearch calls:** 2 of 2.
> **Local corpus:** `references/sources/papers`, `essays` and `software` are empty. `talks/` holds only the UW-Madison oral-history transcript (2022). Research agent 02 saved it from a public archive, so it is **not** user-supplied, and nothing below is marked "from user-supplied material". I re-read the transcript in full for this dimension. Nothing under `private/` was opened.
> **How items were checked:** every paper named below carries a DOI, an arXiv id, or venue + year + full title that I checked this run against Crossref, OpenAlex (author `A5046109083`, 341 works pulled), DBLP (SPARQL; pids `w/StephenJWright` and `75/2677`), or arXiv abstract and listing pages. Oral-history quotes were string-matched against the transcript file (locator = speaker-turn timestamp, "OH22 [mm:ss]"). PDF quotes carry the page or slide number of the file named in Sources.
> **Tags:** [stated] = Wright said or wrote it · [practice] = what his papers, code, CVs and records show he did · [observed] = what others (institutions, prize committees, colleagues) say · [inferred] = my reading, found in no source. **P** = primary, **S** = secondary.
> **Relation to notes 01–04:** 01 (publications) already has a five-year topic table and the anatomy of five signature works; 03 has an artifact timeline; 04 has the verified student list. This note does not repeat them. It adds the dated career timeline, the lineage, the *triggers* and *timing* of each turn, and the last 12 months. Where I rely on an item that another agent checked this run, I say "(via 01)", "(via 03)" or "(via 04)".

---

## 1. Dated academic timeline

Rows are in date order. "Event" is what happened; "Tag / evidence" names the source.

| Date | Event | Tag / evidence |
|---|---|---|
| High school, age 16 (year not stated) | Hears the term "numerical math" in a TV interview with the head of the Queensland mathematics department: "I'd never heard this term numerical math and I kind of immediately I was immediately intrigued by it." Wins the Queensland state mathematics competition in his senior year. | [stated, P] OH22 [3:26] |
| 1981 | B.Sc. (Hons), University of Queensland. Honours mathematics plus a computer-science major ("I also did a major in computer science as well"). | [stated, P] old homepage biography (the block is inside an HTML comment in the public page source, so it is not displayed); OH22 [3:26] |
| Received 19 Sep 1983, revised 17 Jan 1984 | Wright & Holt, "An inexact Levenberg-Marquardt method for large sparse nonlinear least squares" (the published title misspells "squres"), *J. Austral. Math. Soc. Ser. B* 26 (1985) 387–403, 10.1017/S0334270000004604. The linear subproblem is solved inexactly with Paige and Saunders' LSQR. The motivating application is earthquake (seismic) inversion. Acknowledgement: "The motivation for this work arose as a result of a period spent by J. N. Holt at the Computer Science Department, Stanford University. We wish to express our thanks to Gene Golub" (p. 402). | [practice, P] full text (Cambridge Core, open archive) |
| 1984 | PhD, University of Queensland: "I did my thesis in 1984 was and was on optimization topics." Thesis title and supervisor: **not found** (see §2.1). Same year: "Mathematical methods for the seismic inversion problem" (OpenAlex W2222248307; Project Euclid collection `pcma`, record 1416337608; **not read**, bot-blocked). | [stated, P] OH22 [3:26]; [practice, S] OpenAlex |
| 1985 | Joins SIAM: "I joined SIAM as soon as I graduated, in 1985". | [stated, P] SIAM profile Q&A reproduced by UW CS, 2024-09-04 |
| c. 1985–86 | Postdoc in the US ("I came to the US, I worked as a postdoc", OH22 [3:26]). Place: University of Arizona Department of Mathematics, which is the affiliation on Wright, "Convergence of Projected Hessian Approximations in Quasi-Newton Methods for the Nonlinear Programming Problem", *IMA J. Numer. Anal.* 6 (1986), 10.1093/imanum/6.4.463. Exact dates **not found**. | [stated, P] + [practice, S] OpenAlex raw affiliation; dates [inferred] |
| 1986 | Wright & Holt, "A new non-linear least squares algorithm for the seismic inversion problem", *Geophys. J. Int.* 87 (1986) 1041–1056, 10.1111/j.1365-246X.1986.tb01982.x. This is the application the 1985 paper promised ("Further testing will include application of the program to the earthquake inversion problem", 1985, p. 402). It is the last paper of the PhD-era line. Wright's address is already NC State. | [practice, P/S] Crossref, OpenAlex affiliation |
| 1986–1990 | Faculty, Mathematics, North Carolina State University: "I started at North Carolina State in 1986 ... I was in a math department was teaching two courses a semester." The SIAM profile gives "North Carolina State University (1986-90)". Papers from 1987 to 1990 carry the NC State address: composite nonsmooth optimization (*Math. Program.* 1987, 10.1007/BF02591697; 1989, 10.1007/BF01587090), "Convergence of SQP-Like Methods for Constrained Optimization" (*SIAM J. Control Optim.* 1989, 10.1137/0327002), "Implementing proximal point methods for linear programming" (*JOTA* 1990, 10.1007/BF00939565), and equality-constrained QP on the Alliant FX/8 vector multiprocessor (*Ann. Oper. Res.* 1988, 10.1007/BF02186482). | [stated, P] OH22 [6:36]; [observed, S] SIAM profile; [practice, S] OpenAlex affiliations |
| Fall 1988 | First invited talk as a PhD, at UW-Madison, hosted by Olvi Mangasarian: "He invited me in the fall of 1988, to come and give a talk." | [stated, P] OH22 [0:51] |
| 1988 | "And then my colleagues at Argonne, I got a phone call in 1988. And they said, "Well, we've got this one year position, and would you be interested in coming?" and I did, I took a leave of absence. And I went and worked there for a year." | [stated, P] OH22 [6:36] |
| 1990 | Permanent position at Argonne MCS, "a senior computer scientist at Argonne National Laboratory (1990-2001)". "the division that I worked in was a combined math and CS division. And so that was my opportunity to sort of crossover more into the computer science side." Argonne-affiliated records appear from 1990 (Pereyra & Wright, "Three-dimensional inversion of travel time data for structurally complex geology", 1990 report on OSTI, no DOI; OpenAlex metadata only) and 1991 (Kelley & Wright, "Sequential quadratic programming for certain parameter identification problems", *Math. Program.* 1991, 10.1007/BF01586941), then an automatic-differentiation case study with Corliss, Bischof, Griewank and Robey (1992, 10.2172/5256454). | [stated, P] current homepage; OH22 [3:26]; [practice, S] OpenAlex |
| 1991 / Aug 1992 | First interior-point papers: "Structured interior point methods for optimal control", Proc. 30th IEEE CDC (1991; month not checked), 10.1109/CDC.1991.261700; "An Interior-Point Algorithm for Linearly Constrained Optimization", *SIAM J. Optim.* 2 (1992), 10.1137/0802023. | [practice, S] Crossref |
| 1993 | Moré & Wright, *Optimization Software Guide* (SIAM), 10.1137/1.9781611970951. "Interior point methods for optimal control of discrete time systems", *JOTA* 1993, 10.1007/BF00940784. | [practice, S] Crossref |
| 1994 | Starts "Interior-Point Methods Online, an older archive of interior-point papers and stuff, which I maintained starting in 1994, in the early days of the Web". | [stated, P] current homepage |
| 1995 | Enters the leadership of the Mathematical Programming Society ("I became involved with that society in 1995"). Starts visiting Madison "about twice a year from about 1995 onwards" for joint projects with Rawlings and Ferris. | [stated, P] OH22 [45:38], [0:51] |
| 1996–97 | PCx betas (May and Oct 1996), 1.0 (Mar 1997): "We released it initially in 1997". Paper: Czyzyk, Mehrotra, Wagner & Wright, *Optim. Methods Softw.* 1999, 10.1080/10556789908805757. | [stated, P] OH22 [9:02]; [practice, P] changelog (via 03) |
| 1997 | *Primal-Dual Interior-Point Methods* (SIAM), 10.1137/1.9781611971453. | [practice, S] Crossref |
| 1997–98 | Two new lines start. (a) Degenerate NLP: stabilized SQP, *Comput. Optim. Appl.* 11 (1998), 10.1023/A:1018665102534 (preprint Feb 1997). (b) Process control with J. B. Rawlings: Rao, Wright & Rawlings, "Application of Interior-Point Methods to Model Predictive Control", *JOTA* 1998, 10.1023/A:1021711402723. OpenAlex's first joint work with Rawlings is dated 1997. | [practice, S] Crossref, OpenAlex |
| 1999 | Nocedal & Wright, *Numerical Optimization* (Springer), 10.1007/b98874. Czyzyk, Wisniewski & Wright, "Optimization Case Studies in the NEOS Guide", *SIAM Review* 1999, 10.1137/S0036144598334874. | [practice, S] Crossref |
| 1999–2003 | metaNEOS grid computing: Linderoth & Wright, "Decomposition Algorithms for Stochastic Programming on a Computational Grid", *COAP* 2003, 10.1023/A:1021858008222. | [practice, S] Crossref; project dates via 03 |
| 2000–2001 | University of Chicago: "a professor of computer science at the University of Chicago (2000-2001)" (homepage), or "a job adjunct position at the University of Chicago in 2000-2001" (OH22). An ML colleague brings him ML optimization problems (§3, T7). | [stated, P] (the two wordings differ; see Contradiction 2) |
| 2000 → 2001 | Interviews at UW-Madison in 2000 and arrives in 2001, as "the first hire into that cluster into computer science" (a campus cluster hire in computational science). He heard of it from Michael Ferris. | [stated, P] OH22 [0:51] |
| 2001–03 | OOQP ("around the time I moved to Wisconsin, we developed another package called OOQP"). Gertz & Wright, *ACM TOMS* 29 (2003), 10.1145/641876.641880. | [stated, P] OH22 [9:02]; [practice, S] Crossref |
| May 2002 | SIAM Optimization plenary, "The Ongoing Impact of Interior-Point Methods": "Research has moved beyond the “frenetic” stage into a phase of consolidation and maturity. Important developments continue to occur." (slide 2). His last papers with "interior" in the title appear in 2002 (Yıldırım & Wright, warm starts, *SIOPT* 12, 2002, 10.1137/S1052623400369235). | [stated, P] slides; [practice, S] OpenAlex title scan |
| 2003–2007 | Editor-in-chief, *Mathematical Programming, Series B*. | [stated, P] homepage |
| 2005 | Earliest statistics-journal paper found: Turlach, Venables & Wright, "Simultaneous Variable Selection", *Technometrics* 2005, 10.1198/004017005000000139. Radiotherapy line 2005–07: Ólafsson & Wright, "Linear programing formulations and algorithms for radiotherapy treatment planning", *OMS* 2005, 10.1080/10556780500134725; Lim, Ferris, Wright, Shepard & Earl, "An Optimization Framework for Conformal Radiation Treatment Planning", *INFORMS J. Comput.* 2007, 10.1287/ijoc.1060.0179. | [practice, S] Crossref, OpenAlex |
| 2005–2014 | SIAM Board of Trustees, the maximum three terms. | [stated, P] OH22 [45:38]; homepage |
| 2006 | *Numerical Optimization*, 2nd ed., 10.1007/978-0-387-40065-5. Oberlin & Wright, "Active Set Identification in Nonlinear Programming", *SIOPT* 17 (2006), 10.1137/050626776: the last degenerate-NLP paper before 2026. | [practice, S] Crossref |
| 2006–07 | Turn to compressed sensing with Rob Nowak (UW ECE). GPSR: Figueiredo, Nowak & Wright, *IEEE JSTSP* 1 (Dec 2007), 10.1109/JSTSP.2007.910281. | [stated, P] OH22 [24:55]; [practice, S] Crossref |
| 2007 | First ML-venue paper in DBLP: Goldberg, Zhu & Wright, "Dissimilarity in Graph-Based Semi-Supervised Classification", AISTATS 2007. Ferris, Mangasarian & Wright, *Linear Programming with MATLAB* (SIAM), 10.1137/1.9780898718775. | [practice, S] DBLP, Crossref |
| 2007–2010 | Chair of the Mathematical (Programming →) Optimization Society (homepage dates; see Contradiction 1). | [stated, P] |
| 2008 | Chabarek, Sommers, Barford, Estan, Tsiang & Wright, "Power Awareness in Network Design and Routing", IEEE INFOCOM 2008, 10.1109/INFOCOM.2008.93 (INFOCOM Test of Time Award, 2019). NIPS workshop talk, Whistler, 12 Dec 2008, "Optimization in Machine Learning". | [practice, S] Crossref; [observed, S] UW CS 2019-03-12; [practice, P] slides |
| 2009 | SpaRSA: Wright, Nowak & Figueiredo, *IEEE TSP* 57 (2009), 10.1109/TSP.2009.2016892. The society is renamed Mathematical Optimization Society after a member vote that "had passed by a margin of 75% to 25%". "I helped organize that meeting in 2009" (ISMP, Chicago). | [practice, S]; [stated, P] OH22 [45:38] |
| 2011 | Hogwild! (arXiv:1106.5730, June 2011; NIPS 2011). Written in the "first months" of the Wisconsin Institute for Discovery's optimization group [observed, S, UW CS 2020-12-08]. SIAM Fellow (class of 2011). | [practice, P]; [observed, S] UW CS 2024-02-14 |
| 2012 | "Accelerated Block-coordinate Relaxation for Regularized Optimization", *SIOPT* 22 (2012), 10.1137/100808563. Leaves MOS leadership: "Finally, I stepped down in 2012." Made a life member. | [practice, S]; [stated, P] OH22 [45:38] |
| 2013 | KDD keynote "Optimization in learning and data analysis", 10.1145/2487575.2492149. | [practice, S] Crossref |
| 2014 | IEEE W. R. G. Baker Award, "for best paper in an IEEE archival publication during 2009-2011". The paper is **not named** in any source read (see Gaps). | [observed, S] SIAM profile 2024 |
| 2014–2019 | Editor-in-chief, *SIAM J. Optim.* | [stated, P] homepage |
| 2015 | "Coordinate descent algorithms", *Math. Program.* 151 (2015), 10.1007/s10107-015-0892-3 (arXiv:1502.04759). Named chairs: Amar and Balinder Sohi Professor (2015–16), George B. Dantzig Professor (2015–). | [practice, S]; [stated, P] homepage |
| 2016 | Sheldon B. Lubar Chair (2016–2026). Postdoc C. W. Royer joins (Nov 2016 – Aug 2019, via 04). | [stated, P] homepage |
| 2017 | UW-Madison IFDS founded under NSF TRIPODS Phase I ("established in Phase I of NSF’s TRIPODS program in 2017 with a $1.5 million grant"). Royer & Wright, arXiv:1706.03131 (June 2017; *SIOPT* 28, 2018, 10.1137/17M1134329): the turn to worst-case complexity. Footnote: "Part of this work was done while the second author was visiting the Simons Institute for the Theory of Computing" (p. 1). | [observed, S] WID 2020-09-01; [practice, P] arXiv v2 |
| 2018 | First papers with Qin Li (UW Mathematics) on multiscale PDEs and sampling (OpenAlex: 21 joint works, 2018–2025). | [practice, S] OpenAlex |
| 2019 | IEEE INFOCOM Test of Time Paper Award (for the 2008 paper). | [observed, S] UW CS 2019-03-12 |
| 2020 | IFDS Phase II: "$12.5 million Phase II grant", of which "$4.6 million is slated for UW–Madison". Wright "directs IFDS at UW–Madison". Fall 2020: "the Deans gave me a semester off teaching" to spin up the institute. INFORMS Optimization Society Khachiyan Prize ("For his vast contributions to continuous optimization, spanning theory, algorithms and software, and the impact of his work on control, signal processing, and machine learning."). NeurIPS Test of Time Award (Hogwild!). | [observed, S] WID 2020-09-01, UW CS 2020-11-11 and 2020-12-08; [stated, P] OH22 [43:05] |
| 2021–22 | Sabbatical ("I was on sabbatical last year"). In Australia from the end of January to early May 2022 for family reasons. | [stated, P] OH22 [43:05], [59:27] |
| 2022 | Hilldale Award, UW-Madison (letter received February 2022). Wright & Recht, *Optimization for Data Analysis* (CUP, Mar 2022), 10.1017/9781009004282. 18 Jul 2022: GitHub repository `wrightstephen/NumericalOptimization3rdEdition` created. It still holds only a README (one commit, 2022-07-18; shallow clone this run). | [stated, P] OH22 [59:27]; [observed, S] UW CS 2024-02-14; [practice, P] git log |
| 4 Oct 2022 | UW-Madison oral-history interview (OH22). | [stated, P] |
| 2023 – Jul 2025 | Chair, Department of Computer Sciences. "fourteen assistant professors were hired during his two years as chair". Paul Barford "In July ... succeeded Steve Wright as chair". | [observed, S] UW CS 2025-09-03, 2025-09-09; [stated, P] homepage |
| Feb 2024 | Elected to the National Academy of Engineering (class of 2024). | [observed, S] UW CS 2024-02-14 |
| 22 Jul 2024 | George B. Dantzig Prize (MOS and SIAM), presented at ISMP 2024, Montreal. | [observed, S] UW CS 2024-07-22 |
| 2024–2026 | Hilldale Professor (homepage). See Contradiction 3. | [stated, P] |
| 21 Apr 2025 | UW Mathematics announces that he will give a plenary lecture at ICM 2026. | [observed, S] UW Math news |
| 3 Sep 2025 | Steps down as chair to "embrace my role as a professor and researcher once more". | [stated, P] quoted in UW CS 2025-09-03 |
| 2025– (homepage) / May 2026 (announced) | Vilas Research Professor. See Contradiction 4. | [stated, P]; [observed, S] UW CS 2026-05-26 |
| 13 Jul 2026 (online) | "Optimization in Theory and Practice", *Proceedings of the International Congress of Mathematicians 2026 – Volume 2: Plenary Lectures*, pp. 363–393, 10.1137/25M1806831 (= arXiv:2510.15734). | [practice, S] Crossref |
| 23–30 Jul 2026 | ICM 2026, Philadelphia. He was scheduled to speak for "control theory and optimization". Whether the lecture was delivered as scheduled was **not verified**: no program or video was read. | [observed, S] UW CS 2026-05-26; ICM site (dates only) |

---

## 2. Lineage

### 2.1 Upstream: training and early influences

- **PhD supervisor: not found.** [practice, S] The Mathematics Genealogy Project record for "Stephen J. Wright" (id 207459) reads "Dissertation: Advisor: Unknown". The UQ eSpace API returned 403, the National Library of Australia catalogue sat behind a bot check (not bypassed), and one WebSearch returned nothing on the thesis.
- **Candidate, not verified.** [inferred] J. N. Holt (Department of Mathematics, University of Queensland) co-wrote both PhD-era papers (1985, 1986). The 1985 paper's motivation came from Holt's stay with Golub's group at Stanford. That makes Holt the most likely supervisor or mentor, but **no source says so**.
- **What the PhD-era papers show about the starting point** [practice, P]:
  - large sparse nonlinear least squares from a real application (seismic inversion);
  - inexact inner solves by an iterative linear solver (LSQR), with a global convergence result and quadratic convergence for zero residuals (1985 abstract);
  - numerical tests on "problems of varying residual size" (1985 abstract).
  - [inferred] "Inexact" is a word he keeps using: inexact LM (1985), "inexact methods" for composite nonsmooth functions (1987, 1989), iSQP (2002), inexact Newton-CG (2022), "inexact evaluations" (2025).
- **Early influences he names** [stated, P]:
  - Olvi Mangasarian, who invited him in 1988 and whom he calls "a pioneer in using optimization to solve machine learning problems" (OH22 [24:55]).
  - Michael Ferris, through whom he learned of the UW job (OH22 [0:51], [1:01:21]).
  - Argonne colleagues. On what he learned from colleagues generally: "I've been very lucky to learn from them by looking at what sort of things they work on about how they go about research and how, how they go about finding research problems." (OH22 [6:36]).
- **Argonne-era senior co-authors** [practice, S]: Victor Pereyra (parallel BVP solver, *SISC* 1990, 10.1137/0911025; the 1990 OSTI report "Three-dimensional inversion of travel time data for structurally complex geology", which continues the seismic thread), C. T. Kelley (1991), Jorge Moré (1993 guide), and the AD group (Corliss, Bischof, Griewank, 1992).

### 2.2 Downstream: students and postdocs over time

The verified list is in 04 §0 and is not repeated. Placed on the trajectory [practice, S unless noted; via 04]:

| Period | Supervision mode | People (status per 04) |
|---|---|---|
| 1990s, Argonne | Lab team: postdocs, summer students, staff on PCx and OOQP | Czyzyk, Wagner, Gertz (roles unverified). "I had several postdocs, and students work on it" [stated, P, OH22 9:02] |
| 1999–2010 | Co-supervision in Chemical Engineering through Rawlings | Tenny (PhD 2002), Venkat (2006), Stewart (2010): verified collaborators, not his advisees |
| 2005–2016 | Own CS PhD students | Sangkyun Lee (PhD 2011, verified); Ji Liu, Christina Oberlin, Arinbjörn Ólafsson (roles unverified) |
| 2014–2026 | Own and co-advised students | Srikrishna Sridhar (2014, third advisor per MGP); Michael O'Neill (verified); Ching-pei Lee (probable); Roger Waleffe (PhD 2024–25, verified); Shuyao Li (co-advised with J. Diakonikolas, PhD 2025–26, verified) |
| 2016– | Postdocs replace the Argonne staff model | Royer (2016–19, verified), Alacaoglu (from 2021, verified); Xie, Ho-Nguyen, Ding (roles unverified) |

- **Genealogy databases are unreliable here** [practice, S]. MGP record 207459 lists one student (Tillmann, TU Darmstadt 2013). Record 102703, a different Stephen Wright (Leeds), wrongly collects a UW student (via 04, K1). **No database gives a usable descendant count.**
- **Recruitment route** [stated, P]: "the students that I've recruited have typically come from graduate classes" (OH22 [35:54]).

---

## 3. Direction changes: what triggered each turn

Each turn gives dates (entry → exit), the trigger type, the evidence, and what carried over. The trigger types are the framework's: new tool, new data or problem, failure, move, colleague, funding.

### T0 · 1983–1986: sparse nonlinear least squares for seismic inversion (PhD era)
- **Trigger: colleague plus application.** [practice, P] Holt's Stanford stay (Golub) and a U.S. Geological Survey contact (Willie Lee is thanked in the 1985 acknowledgement).
- **Carried over** [inferred]: inexact inner solves, sparsity, application-first framing.
- **Exit:** after the 1986 GJI paper he does not return to least squares as a theme. The reason is not stated.

### T1 · 1986–1990: convergence theory of SQP-like, quasi-Newton and composite nonsmooth methods (NC State)
- **Trigger: move.** [stated, P] Math-department post; "I did my thesis in 1984 was and was on optimization topics. And from then on, I sort of worked more and more on optimization." (OH22 [3:26]).
- **Early hardware thread** [practice, S]: the Alliant FX/8 QP paper (1988) and the parallel BVP work with Pereyra (1990). Parallel computing was already present before Argonne.
- **Carried over**: SQP local convergence theory. It returns in 1997–2006 (T5).

### T2 · 1990–1993: parallel algorithms, optimal control, AD, software survey (Argonne arrival)
- **Trigger: move to a lab with "a combined math and CS division"** [stated, P, OH22 3:26]. Resources: "we had good resources. And you know, we had time to do interesting things." (OH22 [6:36]).
- **Evidence** [practice, S]:
  - parallel BVP solvers and banded systems;
  - "Solution of discrete-time optimal control problems on parallel computers" (*Parallel Comput.* 1990, 10.1016/0167-8191(90)90060-M);
  - "Partitioned Dynamic Programming for Optimal Control" (*SIOPT* 1991, 10.1137/0801037);
  - AD case studies (1992);
  - the *Optimization Software Guide* (1993).
- **Exit**: the parallel ODE and banded-system line fades after the early 1990s (DBLP titles with "parallel" cluster in 1990–92). The optimal-control structure moves straight into IPMs (T3) and later MPC (T4).

### T3 · 1991–2002: interior-point methods (the "gold rush")
- **Trigger: a new algorithm class.** [stated, P] "I had great fun participating in the interior-point “gold rush” of the 1990s, writing a book on that subject in 1997 and contributing several software packages." (SIAM Q&A, 2024). "In the in the 90s it was interior point methods" (OH22 [57:24]).
- **Entry relative to the field** [practice, S; inferred]:
  - Karmarkar's paper appeared in Dec 1984 ("A new polynomial-time algorithm for linear programming", *Combinatorica* 4, 10.1007/BF02579150).
  - Wright's first IPM paper appeared about 7 years later (CDC, 1991). He entered mid-wave, not at the start.
  - His entry point was structure: IPMs *for optimal control* (CDC 1991; *JOTA* 1993). General LP/LCP came second (infeasible path-following for LCP, *OMS* 1993, 10.1080/10556789308805537).
- **Synthesis at the crest** [practice, S; stated, P]:
  - the monograph (Jan 1997) and PCx (1997) came out just as, by his own later dating, the "classical" period ended.
  - 2025: "For many years after the “classical” period of interior-point linear programming research ended in the mid-1990s, there was little research on improving the complexity bounds further." (arXiv:2510.15734v2, p. 10).
  - The same essay describes the boom as "an explosion of activity in interior-point methods that reverberated for over a decade" (p. 8).
- **Exit and its stated reading** [stated, P; practice, S]:
  - May 2002: "Research has moved beyond the “frenetic” stage into a phase of consolidation and maturity." (siopt_talk_may02.pdf, slide 2).
  - OpenAlex titles with "interior" stop in 2002. The late IPM papers are about robustness at the margins: finite precision (2001), dependent constraints (Ralph & Wright, *MOR* 2000, 10.1287/moor.25.2.179.12227), warm starts (2002).
  - [inferred] He left the topic when he judged it mature, about 5 years after writing its synthesis. He did not leave because of a failure.
- **Observed vs stated** [observed, S]: the 2024 Dantzig citation, as reproduced by SIAM, says "He pioneered infeasible interior point methods". His own word is "participating" (Contradiction 9).
- **Later returns, as an observer and user**:
  - the 2025 essay reviews the "burst of new activity started in the late 2010s" in IPM complexity (p. 10). DBLP has no new IPM-complexity paper by him [practice, S].
  - PCx was "resuscitated" to presolve Netlib for the squared-variable paper, 2023–25 (via 03).

### T4 · 1991/1997–2021: control and model predictive control (the longest line)
- **Trigger: application partner plus structure.** [stated, P] "I've done work with over many years, since the mid 90s, even the early 90s with process control engineers, and I continue to work with that" (OH22 [18:26]).
- **Evidence** [practice, S]: control-structured IPMs from 1991. The partnership with J. B. Rawlings produced 24 joint works in OpenAlex (1997–2021). Madison visits from about 1995.
- **Exit**: the last joint paper with Rawlings is Kumar, Rawlings & Wright, "Industrial, large-scale model predictive control with structured neural networks", *Comput. Chem. Eng.* 2021, 10.1016/j.compchemeng.2021.107291. After 2011 the output is sparse (2011 ×3, 2013, 2021).
- **The MPC idea returns in 2026**: Deb, Wright & Banerjee, arXiv:2603.22430: "Inspired by model predictive control (MPC), we introduce an inference time adaptation framework" (abstract).
- **Membership**: "Member of Texas-Wisconsin-California Control Consortium" is commented out on the old homepage [practice, P]. [inferred] He has left the consortium.

### T5 · 1997–2006, return 2026: degenerate NLP (stabilized SQP, constraint identification)
- **Trigger: carrying his own IPM results across to SQP** (via 01 S2; [stated, P] in preprints P699 and P865): superlinear IPM convergence on degenerate LCPs motivated stabilized SQP.
- **Entry relative to the field** [inferred]: an early, small line. It had modest citations (via 01 §1.5) and ran alongside the MPEC interest of the late 1990s and early 2000s.
- **Exit**: Oberlin & Wright 2006 is the last paper until 2026. **No stated reason.** [inferred] The exit coincides with the compressed-sensing turn (T7) and with the end of Oberlin's thesis work. 03 §4 records that the loop from theory to a released solver never closed.
- **Return (Feb 2026)**: Lee & Wright, "Revisiting Superlinear Convergence of Proximal Newton-Like Methods to Degenerate Solutions", arXiv:2602.10470. The abstract claims superlinear convergence "under a Hölderian error bound condition" with a Jacobian "merely uniformly continuous", plus a globalization that "avoids the Maratos effect". Theory only (via 03). [inferred] The 2026 return comes through the proximal-Newton and regularized-optimization problems of the ML era, not through classical NLP.

### T6 · 1999–2007: grid-scale stochastic programming, radiotherapy (short application lines at the Argonne–UW seam)
- **Trigger: a new tool plus colleagues.** Condor/MW grid computing (metaNEOS) with Linderoth (via 03). Radiotherapy with Ferris, Jeraj and Ólafsson.
- **Duration** [practice, S]: "stochastic program" titles run 2001–2006; radiotherapy titles 2005–2007.
- **Exit**: no stated reason for either. [inferred] These are project-length engagements that ended with the grant or the student (Ólafsson), not abandoned research programs.

### T7 · 2000–2001 (first contact) → 2005–2015: statistics, sparse optimization, compressed sensing, ML
- **Trigger 1: a colleague walked in** [stated, P]: "he came into my office one day and said, I believe you do optimization, and he said, I think I've got these optimization problems coming from machine learning. Can you help me with these, and so that's where I sort of started becoming more interested 2000-2001." (OH22 [24:55]; the colleague's name is "[unclear]" in the transcript.)
  - **Lag** [practice, S]: the earliest statistics-journal paper found is from 2005 (Technometrics) and the first ML-venue paper in DBLP is from 2007 (AISTATS). About 5 years passed between first contact and first publication.
- **Trigger 2: a new problem class plus a local partner** [stated, P]: "the compressed sensing work, which started around 2006 or so that's also tied to machine learning. And so I became a part of that I started collaborating with Professor Rob Nowak here at UW Madison. And since then, it's just it's my involvement in that area has just grown and grown." (OH22 [24:55]).
- **Entry relative to the field** [practice, S; inferred]:
  - the founding papers are Candès, Romberg & Tao, *IEEE TIT* 52 (Feb 2006), 10.1109/TIT.2005.862083, and Donoho, "Compressed sensing", *IEEE TIT* 52 (Apr 2006), 10.1109/TIT.2006.871582.
  - GPSR appeared in Dec 2007, 1–2 years after them. He entered early in the wave and supplied the solvers the theory needed.
- **Stated rationale for the algorithmic change** [stated, P]: "Traditionally, research on algorithmic optimization assumes exact data available and precise solutions needed. However, in many optimization applications we prefer simple, approximate solutions to more complicated exact solutions. ... These new “ground rules” may change the algorithmic approach altogther." (NIPS workshop, 12 Dec 2008, slide 4; the typo is in the original).
- **Exit** [practice, S]: joint work with Nowak runs 2007–2013 in OpenAlex (one more in 2019). DBLP titles with "sparse/compress" thin out after 2015. No stated exit; the problems were absorbed into ML optimization.

### T8 · 2010–2023: coordinate descent, asynchronous parallel SGD (Hogwild!)
- **Trigger: new hardware plus new data scale** [stated, P, paper]: "the recent emergence of inexpensive multicore processors and mammoth, web-scale data sets has motivated researchers to develop several clever parallelization schemes for SGD" (Hogwild! TR, June 2011, p. 1). The work was a collaboration with UW systems colleagues (Ré) and Recht.
- **Trigger for coordinate descent: applications changed the ground rules** [stated, P]: "The situation has changed in recent years. Various applications (including several in computational statistics and machine learning) have yielded problems for which CD approaches are competitive in performance with more reputable alternatives." (arXiv:1502.04759v1, p. 2).
- **Entry relative to the field** [practice, S; inferred]: his *SIOPT* 22 (2012) block-coordinate paper (10.1137/100808563; [inferred] the "10" in the SIAM manuscript number suggests a 2010 submission) appeared in the same journal year as Nesterov's "Efficiency of Coordinate Descent Methods on Huge-Scale Optimization Problems", *SIOPT* 22 (2012), 10.1137/100802001. He entered at about the same time, not after. The solo survey (2015) is again a **synthesis at the crest**, as with the 1997 monograph.
- **Admitted community blind spot** [stated, P]: on SGD before about 2008, "optimizers knew about it, but didn't pay much attention to it. Because it's very slow, we thought it's very slow." (OH22 [24:55]).
- **Exit**: coordinate-descent titles run to 2023 (DBLP). No stated exit.

### T9 · 2017–2025: worst-case complexity of Newton-type methods for nonconvex problems
- **Trigger: fashion from ML plus an institutional visit** [stated, P]: "There has been much recent interest in finding unconstrained local minima of smooth functions, due in part of the prevalence of such problems in machine learning and robust statistics." (arXiv:1706.03131v2, abstract). The Simons Institute visit footnote is on p. 1.
- **Entry relative to the field: a late entrant** [practice, S; inferred]. Earlier work:
  - Nesterov & Polyak, "Cubic regularization of Newton method and its global performance", *Math. Program.* 108 (2006), 10.1007/s10107-006-0706-8;
  - Cartis, Gould & Toint, "Adaptive cubic regularisation methods for unconstrained optimization. Part I", *Math. Program.* (online 2009), 10.1007/s10107-009-0286-5;
  - Carmon, Duchi, Hinder & Sidford, "Accelerated Methods for NonConvex Optimization", *SIOPT* 28 (2018), 10.1137/17M1114296.
  - Wright entered 8–11 years after the first two. His paper positions itself against these "recent proposals" by keeping line searches and a "rather straightforward" analysis (abstract). [inferred] For the first time in his career he joins a wave late, and he offers the practitioner's method (Newton-CG), not a new algorithm class.
- **Self-verdict** [stated, P, 2025]: "the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance." (arXiv:2510.15734v2, p. 23).
- **Status**: still active in 2025. Li & Wright, *JOTA* 2025, 10.1007/s10957-025-02817-y. Ding & Wright, "On Squared-Variable Formulations", *SIOPT* 2025, 10.1137/23M1608343.

### T10 · 2018–2026: data-science foundations (PDEs and sampling, privacy, robustness, min-max, diffusion, RL)
- **Trigger: funding and institution plus colleagues** [practice, S; stated, P]. IFDS (TRIPODS 2017, 2020) under his direction. "in recent years, I worked a lot with people in data science. And that's probably my main, interdisciplinary engagement in the last 10 years." (OH22 [18:26]).
- **Lines** [practice, S]:
  - multiscale PDEs, Langevin sampling and randomized linear algebra with Qin Li (2018–2025);
  - differential privacy and robust stochastic optimization with Changyu Gao and Andrew Lowy (arXiv:2302.04972, 2402.11173, 2412.11003);
  - min-max fixed-point methods with Alacaoglu (arXiv:2402.05071);
  - bilevel optimization with Nowak's group (2022–24, under DBLP pid 75/2677);
  - diffusion models (arXiv:2601.19285, CVPR 2026);
  - offline RL (arXiv:2603.22430).
- [inferred] The pattern changes: many short, co-author-led excursions, with Wright in the senior (last-author) position (via 01 §1.2).

### T11 · 2023–2026: administrative detour and return
- 2022: "I haven't done administrative work in the department, except for this institute that I that I head up" (OH22 [45:38]). One year later he became department chair, 2023–25.
- Old homepage, still online on 2026-09-28: "Current Research: Being Department Chair." Teaching: "Current: Not these days, baby!" [stated, P] (both visible in the page, not in comments).
- 2025: steps down to "embrace my role as a professor and researcher once more" [stated, P].
- **What followed** [practice, P]:
  - the ICM plenary essay on theory and practice (Oct 2025, published Jul 2026);
  - a return to degenerate superlinear convergence (Feb 2026);
  - teaching CS730 Nonlinear Optimization II in Spring 2026 (current homepage).

---

## 4. Entry and exit timing (summary)

Field reference points are the dated papers named in §3. "Lag" = his first paper minus the reference point.

| Topic | Field reference point | His entry | Lag | His exit | Exit reason | Timing type [inferred] |
|---|---|---|---|---|---|---|
| Interior-point methods | Karmarkar, Dec 1984 | CDC 1991 | ~7 yr | 2002 | [stated] field in "consolidation and maturity" (2002) | Mid-wave entry, synthesis at the crest (1997), exit after maturity |
| Degenerate NLP / stabilized SQP | (his own degenerate-LCP IPM results, 1994–96) | 1997 preprint | 0–1 yr after his own results | 2006; return 2026 | not stated | Early and self-seeded; low-citation; left unfinished |
| Compressed sensing / sparse | Candès–Romberg–Tao, Donoho, 2006 | GPSR 2007 | 1–2 yr | ~2014–15 | not stated | Early; supplied algorithms to a theory-led field |
| Coordinate descent | Nesterov, SIOPT 2012 | SIOPT 2012 (2010 ms.) | ~0 | ~2023 | not stated | Simultaneous; survey (2015) at the crest |
| Asynchronous SGD | (SGD dismissed by optimizers until ~2006–08, [stated]) | Hogwild!, 2011 | — | fed into CD work | — | Early (Test of Time 2020) |
| Nonconvex complexity | Nesterov–Polyak 2006; Cartis–Gould–Toint 2009 | 2017 | 8–11 yr | active in 2025 | — | **Late**; brought the practitioner's method; 2025 self-critique |
| Data-science foundations | (institutional: TRIPODS 2017) | 2018 | — | active | — | Institution-driven portfolio |

[inferred] Three regularities:
1. He writes the synthesis (a book or solo survey) when a wave crests: 1997 IPM, 2015 CD, 2022 data-analysis textbook, 2025/26 ICM essay.
2. He leaves a topic by judging it mature, without announcing a move. The only explicit exit statement found is the 2002 IPM slide.
3. His application partner changes about once a decade (01 §1.1 has the same reading). He says the same of the field: "about every decade has been a big thing that's happened" (OH22 [57:24]).

---

## 5. The last 12 months (2025-09-28 → 2026-09-28)

All [practice, P] from the arXiv abstract pages (version dates as shown there) unless tagged otherwise.

| Date | Item |
|---|---|
| (boundary) Jul / 3 Sep 2025 | Chair term ends; Barford succeeds in July. Quote of 3 Sep 2025 [stated, P, via UW CS news]. |
| 2 Oct 2025 (v1); 14 Jan 2026 (v2) | Hellmuth, Jin, Li & Wright, "Data selection: at the interface of PDE-based inverse problem and randomized linear algebra", arXiv:2510.01567, a review. |
| Oct 2025 | Ding & Wright, "On Squared-Variable Formulations", *SIOPT* (Crossref issued 2025-10), 10.1137/23M1608343. |
| 17 Oct 2025 (v1); 2 Dec 2025 (v2) | Wright, "Optimization in Theory and Practice", arXiv:2510.15734. It is the ICM 2026 plenary paper: *Proc. ICM 2026*, Vol. 2, pp. 363–393, 10.1137/25M1806831, online 13 Jul 2026 [practice, S, Crossref]. The acknowledgement reads: "Thanks to Ben Recht for suggesting the topic of this review and to Haihao Lu for his guidance on first-order methods for linear programming." (v2, p. 25). |
| 21 Oct 2025 | Talk, University of Minnesota CSE Data Science Initiative ML seminar, "Optimization in Data Science" [practice, P, event page]. |
| 24 Oct 2025 | Talk, University of Minnesota ISyE Distinguished Seminar, "Inexact Fixed-Point Iterations for Min-Max Problems" (the Alacaoglu–Kim–Wright line, arXiv:2402.05071) [practice, P, event page]. |
| 27 Jan 2026 (v1); 30 Mar (v2); 10 Sep 2026 (v3) | Zhou, Zhang & Wright, "Smoothing the Score Function to Enhance Generalization in Diffusion Models", arXiv:2601.19285; "Accepted by CVPR2026" (arXiv comment); DBLP lists CVPR 2026. |
| 11 Feb 2026 | Lee & Wright, "Revisiting Superlinear Convergence of Proximal Newton-Like Methods to Degenerate Solutions", arXiv:2602.10470. |
| Spring 2026 | Teaches CS730 Nonlinear Optimization II [stated, P, current homepage, last modified 21 Mar 2026]. |
| 23 Mar 2026 (v1); 20 May 2026 (v2) | Deb, Wright & Banerjee, arXiv:2603.22430. v1 (per DBLP): "Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning". The current arXiv title is "Inference Time Policy Optimization for Offline RL with Differentiable World Models". |
| 5 / 26 May 2026 | Vilas Research Professorship announced, together with the ICM plenary [observed, S, UW CS]. |
| 5 Jun 2026 | Shuyao Li's PhD (co-advised with J. Diakonikolas) [observed, S, via 04]. |
| 19 Jun 2026 | Quoted on Michael Ferris's retirement: Ferris is "one of the leading researchers in the world in connecting optimization to real-world problems in an enormous variety of areas." [stated, P, in UW CS news]. |
| 1 Jul 2026 | Alacaoglu, Malitsky & Wright, arXiv:2504.09951 v2, "Towards Weaker Variance Assumptions for Stochastic Optimization". |
| 23–30 Jul 2026 | ICM 2026, Philadelphia (plenary scheduled; delivery **not verified**). His stated plan: "In my talk, I plan to discuss the complementary roles of mathematical theory and computational practice in optimization, showing how each of these two aspects of the field has driven developments in the other." [stated, P, UW CS 2026-05-26]. |

**Not his** (name collisions found in this window) [practice, S]: arXiv:2510.15649 is by "Stephen Michael Wright". arXiv:2511.12705 is by "Stephen Wright, Colin Paterson" and sits in the mixed DBLP profile 75/2677. Neither is by Stephen J. Wright.

**Reading of the last 12 months** [inferred]:
- Two strands run side by side:
  - a senior-author portfolio of ML and data-science papers led by students and co-authors (diffusion, offline RL, PDE data selection, variance assumptions);
  - a personal return to **classical NLP themes**: degenerate superlinear convergence, and the theory–practice essay.
- For an NLP-solver team, the second strand is the live one. The 2026 degeneracy paper is theory only; it runs no experiments.

---

## 6. Era and resource context of each phase

| Phase | Compute and tools | Team and seniority | Funding and institution | Tag |
|---|---|---|---|---|
| 1983–86 PhD, Queensland | LSQR on a sparse Jacobian | PhD student with a faculty co-author | University | [practice, P] |
| 1986–90 NC State | Alliant FX/8 vector multiprocessor (1988 paper) | Junior faculty, solo papers, "two courses a semester" | Math department | [practice, S]; [stated, P] |
| 1990–2001 Argonne | Parallel machines, Unix workstations; netlib; early web (IPM Online 1994); grid (Condor/MW) | Staff scientist with postdocs and summer students; no teaching | DOE lab; "more of a soft money environment" later ([stated, P], OH22 6:36); "I had time to do things like write books" | [stated, P]; [practice] via 03 |
| 2001–2010 UW, early | MATLAB, C with CPLEX; GPUs (NVIDIA partnership, via 03) | Cluster hire; cross-department co-supervision (ChemE, ECE, Stats) | NSF, industrial consortium (TWCCC) | [stated, P]; [practice, S] |
| 2010–2016 | Multicore servers (Hogwild!), WID optimization group | Named chairs from 2015; EiC of SIOPT | NSF, ONR, AFOSR, DOE/Argonne subcontracts (CD survey footnote, p. 1) | [practice, P] |
| 2017–2022 | Laptops, CUTEst, GitHub; Simons Institute visit | Postdocs run experiments; IFDS site director ("about 34-35 faculty members ... eight postdocs", OH22 18:26) | NSF TRIPODS ($1.5M, then $4.6M of $12.5M) | [stated, P]; [observed, S] |
| 2023–2025 | — | Department chair; research output continues through co-authors | — | [observed, S] |
| 2025–2026 | — | Vilas Research Professor; ICM plenary | — | [observed, S] |

[inferred] The IPM monograph and *Numerical Optimization* (1997, 1999) came from the no-teaching Argonne setting. He says so himself (OH22 [6:36]). The later books came with co-authors (2007 with Ferris and Mangasarian, 2022 with Recht). The one book project announced since 2022, a third edition of *Numerical Optimization*, has no public output after 4 years.

---

## 7. Failures, abandoned directions and unfinished items (trajectory level)

| Item | Evidence [tag] | Status |
|---|---|---|
| Degenerate-NLP techniques never reached a released solver | 1997–2006 papers defer practical testing; no code; 2026 return is theory only [practice, P via 01/03; inferred "abandoned"] | Unfinished for 20 years |
| PCx licensing model | "turned out very few people did that, because you know, what way pay when you can get it for free" (OH22 [9:02]); later codes released freely [stated, P] | Model dropped after ~2001 |
| Missed recognition of PCx's use | "I wish I'd known about that 20 years earlier" (OH22 [9:02]) [stated, P] | Regret, not a research failure |
| *Numerical Optimization*, 3rd ed. | Repository created 2022-07-18 with a README only; no later commit (clone this run) [practice, P] | Announced, no public output |
| SGD dismissed by optimizers, himself included ("we thought it's very slow") | OH22 [24:55] [stated, P] | Acknowledged misjudgment |
| Complexity-driven Newton-CG | "do not improve the practical performance" (2025, p. 23) [stated, P] | Self-assessed limit of a 2017–2024 program |
| Short application lines ended without stated reason | Radiotherapy (2005–07, OpenAlex titles), grid stochastic programming (2001–06, OpenAlex titles), power systems (2014–18: arXiv:1409.3832 and arXiv:1503.02360 in the arXiv listing, DBLP titles to 2018) [practice, S] | Reasons not documented |
| Rejected papers | No public record (closed review in math programming) | Unknown |

---

## 8. Candidate patterns for Phase 2 (all [inferred]; each cites its evidence)

1. **Enter through structure or a partner, not through fashion alone.**
   - IPMs came in through optimal-control structure (1991).
   - Sparse optimization came in through Nowak (2006).
   - Data science came in through IFDS and Qin Li (2017–18).
   - The exception is nonconvex complexity (2017), where he entered late and on the ML wave.
2. **Write the synthesis at the crest.** The 1997 monograph, the 2015 CD survey, the 2022 textbook and the 2025/26 ICM essay. Each came while he was still active in the topic, and each consolidated it for newcomers. He states this motive: "I really enjoy this process of sort of distilling knowledge in a particular area" (OH22 [21:25]).
3. **Leave by maturity, not by failure; return decades later through a new door.**
   - IPM: exit in 2002, when "consolidation and maturity" set in.
   - Degenerate SQP: exit in 2006, return in 2026 through proximal Newton.
   - MPC: from the 1990s control work to 2026 offline RL.
4. **Luck and openness are his own explanation for the turns** [stated, P]: "luck plays such a big role, you know, just being in the right place at the right time, talking to the right people having a chance encounter with someone." (OH22 [1:01:21]). His advice for the next turn: "keep your antennae out there" (OH22 [58:55]).
5. **Seniority changes the unit of work** (01 §1.2 author-position data). Solo proofs dominate to about 2004. After that he works as senior author on student and postdoc papers, while solo writing moves to surveys, books and essays.

For a solver team, patterns 2 and 3 matter most. His NLP ideas that are "left unfinished" (T5; 03 §4) and his theory–practice gap agenda (2025 essay) are the parts of the trajectory still open.

---

## Contradictions (kept, not reconciled)

1. **MOS chair dates.** The homepage and bios give "Past Chair of the Mathematical Optimization Society, 2007-2010". The oral-history transcript says "I was elected Chair of the society in 2000, in 2000. In 2006, I became the Chair." and "Finally, I stepped down in 2012." (OH22 [45:38]). The transcript may be garbled; agent 02 records the same conflict (C4). [stated, P vs stated, P]
2. **University of Chicago role, 2000–2001.** The current homepage says "a professor of computer science at the University of Chicago (2000-2001)". The oral history says "a job adjunct position at the University of Chicago in 2000-2001" (OH22 [24:55]). [stated, P vs stated, P]
3. **Hilldale.** UW CS news (2024-02-14): "received the Hilldale Award from UW–Madison in 2022". The oral history places the award letter in February 2022. The current homepage lists "Hilldale Professor, UW-Madison, 2024-2026", and the SIAM 2024 profile says he "holds ... the Hilldale Professorship". An award in 2022 and a professorship in 2024–2026 may be two stages of one honour; no source says so. [observed, S vs stated, P]
4. **Vilas date.** The current homepage (last modified 21 Mar 2026) says "Vilas Research Professor, UW-Madison, 2025-". UW CS announced the professorship on 5 May 2026 (go.wisc.edu/wrightvilas) and 26 May 2026 ("has been named"). [stated, P vs observed, S]
5. **Homepage self-description.** The current homepage lists "Professor, Department of Computer Sciences at UW-Madison (2023-2025)", as if the professorship had ended. UW CS news of May 2026 calls him "Professor of Computer Sciences". The old homepage still says "Chair" and "Current Research: Being Department Chair." more than a year after he stepped down. [stated, P vs observed, S]
6. **Administrative work.** 2022: "I haven't done administrative work in the department, except for this institute" (OH22 [45:38]). 2023–25: department chair. This is a change over time, not a misstatement. (Same as 02 C5.)
7. **When his ML interest started.** Stated: 2000–2001 (OH22 [24:55]). Practice: first statistics paper 2005, first ML-venue paper 2007. Interest and publication are 5 years apart.
8. **NC State tenure.** "1986-90" (SIAM profile; UMN bio) versus a one-year Argonne leave after a 1988 phone call (OH22 [6:36]). The 1990 papers still carry NC State addresses. (Also 01 C8.)
9. **"Pioneered" vs "participating".** SIAM's 2024 profile: "He pioneered infeasible interior point methods which culminated in his 1997 SIAM monograph". Wright, same document: "I had great fun participating in the interior-point “gold rush” of the 1990s". His first IPM paper appeared 7 years after Karmarkar. [observed, S vs stated, P]
10. **SIAM membership length.** "I joined SIAM as soon as I graduated, in 1985" versus the profile's "an active member of SIAM for 38 years" (2024 − 38 = 1986). [stated, P vs observed, S]
11. **Record contamination.** OpenAlex gives his institution as "Ames Research Center" and assigns him other people's papers (1977, 1982, 2026; see 01). arXiv and DBLP pid 75/2677 mix in other Stephen Wrights (§5). No single database is a safe base for his trajectory. [practice, S]

## Gaps

- **PhD thesis title and supervisor: not found.** MGP says "Advisor: Unknown". The UQ eSpace API returned 403; the NLA catalogue is bot-walled (not bypassed); one WebSearch returned nothing. J. N. Holt is a candidate by inference only.
- **University of Arizona**: exact dates and the host were not found. Only the 1986 affiliation and "I worked as a postdoc" are known.
- **Names not recovered**: who phoned from Argonne in 1988, and the UChicago ML colleague ("[unclear]" in the transcript). I did not guess.
- **Stated reasons for leaving topics**: only the 2002 IPM "maturity" slide was found. For degenerate NLP (2006), radiotherapy (2007), grid stochastic programming (2006), compressed sensing (~2014) and power systems (2018), no stated reason exists in the sources read.
- **ICM 2026 delivery**: the proceedings paper is confirmed (Crossref), but no program, video or report of the lecture was read.
- **IEEE W. R. G. Baker Award (2014)**: the paper was not identified. The award window was 2009–2011. SpaRSA (*TSP* 2009) and Tropp & Wright (*Proc. IEEE* 2010) both fall in it. The oral history says the GPSR and SpaRSA papers "won some major awards" (OH22 [12:25]). Not settled.
- **Talks in the last 12 months**: only the two UMN talks (Oct 2025) and the ICM plenary were found (1 WebSearch). The YouTube and Videolectures lists on his homepage were not opened.
- **Google Scholar**: not attempted this run (01 found it captcha-blocked). Semantic Scholar was not used.
- **Rejected papers and failed grant proposals**: no public record.
- **Why the Lubar Chair and Hilldale Professorship end in 2026** (homepage dates): not stated. [inferred] They may be superseded by the Vilas professorship; not verified.
- **The 1984 Project Euclid paper** ("Mathematical methods for the seismic inversion problem"): the venue page was bot-blocked (Incapsula). **Not read.**

## Sources

Primary (P) and secondary (S). "Not read" marks sources I tried and could not open.

1. UW-Madison Oral History Program, "Oral History Interview, Stephen Wright (2179)", interviewer F. Hernandez-Moleres, 2022-10-04, https://minds.wisc.edu/handle/1793/83811; local transcript `../sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt` (read in full; quotes string-matched). P
2. S. J. Wright, current homepage, https://wrightstephen.github.io/sw_proj/ (fetched 2026-09-28; Last-Modified 21 Mar 2026). P
3. S. J. Wright, old UW homepage, https://pages.cs.wisc.edu/~swright/ (fetched 2026-09-28, including the page source's commented-out biography). P
4. S. J. Wright & J. N. Holt, "An inexact Levenberg-Marquardt method for large sparse nonlinear least squres", *J. Austral. Math. Soc. Ser. B* 26 (1985) 387–403, 10.1017/S0334270000004604 (full text, Cambridge Core). P
5. S. J. Wright & J. N. Holt, "A new non-linear least squares algorithm for the seismic inversion problem", *Geophys. J. Int.* 87 (1986), 10.1111/j.1365-246X.1986.tb01982.x (Crossref and OpenAlex metadata only). S
6. S. J. Wright, "Mathematical methods for the seismic inversion problem", 1984, OpenAlex W2222248307, https://projecteuclid.org/euclid.pcma/1416337608. **Not read** (bot-blocked). S
7. S. J. Wright, "The Ongoing Impact of Interior-Point Methods", slides, SIAM Conference on Optimization, Toronto, 20 May 2002 (expanded 27 May 2002), https://pages.cs.wisc.edu/~swright/talks/siopt_talk_may02.pdf (slides 1–2, 54, 59 read). P
8. S. J. Wright, "Optimization in Machine Learning", NIPS Workshop, Whistler, 12 Dec 2008, https://pages.cs.wisc.edu/~swright/talks/sjw-nips.pdf (slides 2–5 read). P
9. F. Niu, B. Recht, C. Ré & S. J. Wright, "Hogwild!", technical report, June 2011, https://pages.cs.wisc.edu/~swright/papers/hogwildTR.pdf; arXiv:1106.5730 (p. 1 read). P
10. S. J. Wright, "Coordinate Descent Algorithms", arXiv:1502.04759v1 (2015), pp. 1–2; *Math. Program.* 151 (2015), 10.1007/s10107-015-0892-3. P
11. C. W. Royer & S. J. Wright, "Complexity analysis of second-order line-search algorithms for smooth nonconvex optimization", arXiv:1706.03131v2 (2017), pp. 1–2; *SIOPT* 28 (2018), 10.1137/17M1134329. P
12. S. J. Wright, "Optimization in Theory and Practice", arXiv:2510.15734v2 (2 Dec 2025), full text; *Proc. ICM 2026*, Vol. 2, pp. 363–393, 10.1137/25M1806831. P
13. arXiv abstract pages (with submission histories) for 2510.01567, 2510.15734, 2601.19285, 2602.10470, 2603.22430, 2504.09951, read 2026-09-28. P
14. arXiv author search listings for "Wright, Stephen J", "Wright, Stephen" and "Wright, S J", https://arxiv.org/search/ (read 2026-09-28). S
15. UW CS news, "CS Professor Steve Wright to be plenary speaker at International Congress of Mathematicians 2026 and named Vilas Research Professor by UW–Madison", K. Barrett-Wilt, 2026-05-26, https://www.cs.wisc.edu/2026/05/26/steve-wright-plenary-speaker-at-icm-2026-and-vilas-research-professor/. S (contains P quotes)
16. UW CS news, "Professor Steve Wright steps down as Computer Sciences Department Chair", K. Barrett-Wilt, 2025-09-03, https://www.cs.wisc.edu/2025/09/03/professor-steve-wright-steps-down-as-cs-department-chair/. S (contains P quotes)
17. UW CS news, "Paul Barford assumes new role as chair of Computer Sciences", R. Robey, 2025-09-09, https://www.cs.wisc.edu/2025/09/09/paul-barford-new-computer-sciences-chair/. S
18. UW CS news, "CS Professor Steve Wright spotlighted by SIAM" (SIAM profile and Q&A reproduced), 2024-09-04, https://www.cs.wisc.edu/2024/09/04/cs-professor-steve-wright-spotlighted-by-siam/. P (Wright's answers) / S (profile)
19. UW CS news, "Computer Sciences Professor Steve Wright awarded prestigious George B. Dantzig Prize", 2024-07-22, https://www.cs.wisc.edu/2024/07/22/steve-wright-awarded-dantzig-prize/. S
20. UW CS news, "Steve Wright elected to prestigious National Academy of Engineering", 2024-02-14, https://www.cs.wisc.edu/2024/02/14/steve-wright-elected-to-prestigious-national-academy-of-engineering/. S
21. UW CS news, "Stephen Wright wins 2020 INFORMS Optimization Society Khachiyan Prize", 2020-11-11, https://www.cs.wisc.edu/2020/11/11/steve-wright-wins-2020-informs-optimization-society-khachiyan-prize/. S
22. UW CS news, "Professor Stephen Wright Announced Winner of the Test of Time Award at 2020 NeurIPS Conference", S. Pavlic, 2020-12-08, https://www.cs.wisc.edu/2020/12/08/professor-stephen-wright-announced-winner-of-the-test-of-time-award-at-2020-neurips-conference/. S (contains P quotes)
23. UW CS news, "Paul Barford and Stephen Wright awarded 2019 IEEE INFOCOM Test of Time Paper Award", 2019-03-12, https://www.cs.wisc.edu/2019/03/12/paul-barford-and-stephen-wright-awarded-2019-ieee-infocom-test-of-time-paper-award/. S
24. UW CS news, "Professor Michael Ferris Retires After 38 Years at UW–Madison", 2026-06-19, https://www.cs.wisc.edu/2026/06/19/professor-michael-ferris-retires-after-38-years-at-uw-madison/. S (contains P quotes)
25. UW CS news listing via the site's WordPress API (post titles and dates mentioning Wright, 2018–2026), https://www.cs.wisc.edu/wp-json/wp/v2/posts?search=Wright. S
26. Wisconsin Institute for Discovery, "UW–Madison to continue fundamental data science research with Phase II award from NSF", 2020-09-01, https://wid.wisc.edu/uw-madison-to-continue-fundamental-data-science-research-with-phase-ii-award-from-nsf/. S (contains P quotes)
27. UW-Madison Mathematics news, "Affiliate Prof. Steve Wright to be plenary speaker at ICM 2026", 2025-04-21, https://www.math.wisc.edu/2025/04/21/affliate-prof-steven-wright-invited-as-speaker-to-2026-icm/. S
28. University of Minnesota CSE DSI, "CSE DSI Machine Learning Seminar with Stephen Wright (CS, UW Madison)", 21 Oct 2025, https://cse.umn.edu/dsi/events/cse-dsi-machine-learning-seminar-stephen-wright-cs-uw-madison. P (abstract and bio)
29. University of Minnesota ISyE, "ISyE Distinguished Seminar: Stephen Wright", 24 Oct 2025, https://cse.umn.edu/isye/events/isye-distinguished-seminar-stephen-wright. P (abstract)
30. ICM 2026 website (dates and venue only; no speaker list found), https://www.icm2026.org/; IMU pages https://www.mathunion.org/icm/icm-2026 and https://www.mathunion.org/icm-plenary-and-invited-speakers. S
31. Crossref REST API: metadata for 10.1137/25M1806831 and the ICM 2026 Vol. 2 record 10.1137/1.9781611978636, plus DOI checks for every paper named above (Wright's papers and the field reference points 10.1007/BF02579150, 10.1109/TIT.2005.862083, 10.1109/TIT.2006.871582, 10.1007/s10107-006-0706-8, 10.1007/s10107-009-0286-5, 10.1137/17M1114296, 10.1137/100802001). S
32. OpenAlex, author A5046109083, 341 works with authorships and raw affiliations (pulled 2026-09-28), https://openalex.org/A5046109083. S
33. DBLP via SPARQL (`scripts/dblp_works.py`), pid `w/StephenJWright` (227 records) and pid `75/2677` (24 records, mixed), https://dblp.org/pid/w/StephenJWright.html. S
34. Mathematics Genealogy Project, record 207459 ("Stephen J. Wright", advisor unknown), https://www.mathgenealogy.org/id.php?id=207459. S
35. GitHub repository `wrightstephen/NumericalOptimization3rdEdition` (shallow clone, one commit dated 2022-07-18, README only), https://github.com/wrightstephen/NumericalOptimization3rdEdition. P
36. Lee & Wright, arXiv:2602.10470 (2026), abstract. P (also in 13)
37. Deb, Wright & Banerjee, arXiv:2603.22430 (2026), abstract. P (also in 13)
38. UQ eSpace API, https://api.library.uq.edu.au/v1/records/search. **Not read** (HTTP 403).
39. National Library of Australia catalogue, https://catalogue.nla.gov.au/. **Not read** (bot check; not bypassed).
40. SIAM ePubs page for the ICM 2026 proceedings, https://epubs.siam.org/doi/book/10.1137/1.ICM26. **Not read** (403); Crossref used instead.
41. WebSearch 1: "Stephen J. Wright" OR "Stephen John Wright" PhD thesis University of Queensland 1984 supervisor optimization. No thesis record found. S
42. WebSearch 2: "Stephen Wright" Wisconsin optimization 2026 plenary OR keynote OR seminar OR colloquium talk. This led to sources 27–29. S
43. Research notes of this run (secondary compilations, all tool-checked by their agents): `01-publications.md`, `02-methodology.md`, `03-process-evidence.md`, `04-mentorship.md` in this folder. S
44. arXiv API (export.arxiv.org). **Not read** (HTTP 406); the HTML search listing (14) was used instead.
