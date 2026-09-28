# 06 · Research trajectory (Philippe L. Toint)

| Field | Value |
|---|---|
| Researcher | Philippe Louis Toint, University of Namur (UNamur, formerly FUNDP), Department of Mathematics and Namur Institute for Complex Systems (naXys); professor emeritus since 2016. Living. |
| Dimension | Research agent 06 of 06: research trajectory. Covers the full timeline, advisor and student lineage, direction changes and their triggers, when he enters and leaves a topic, and the last 12 months. Framework §一 layer 2 (problem choice) and layer 7 (research organisation); §二 agent 6. |
| Research date | 2026-09-28 |
| Sources consulted | 40 (R1–R40 under Sources). 21 are primary. 4 were blocked or returned nothing usable, and each of those is marked. |
| WebSearch calls used | 2 of 2 |
| Language | English (team.json) |
| Local corpus | `references/sources/papers`, `essays` and `software` hold only `.gitkeep`. `talks/` holds the ASR transcript of the July 2026 podcast, saved by research agent 02 in this run. It is **not user-supplied material**, so nothing below is marked "from user-supplied material". I read the whole transcript. `private/` was not opened. |

**How to read this file.**
- **Tags.** [stated] means Toint said or wrote it, alone or as a co-author (co-authored items are marked). [practice] means the record shows he did it: papers, code commits, registries. [observed] means someone else reports it. [inferred] is my own reading, and the basis is given. Each item is also marked **P** (primary: his own words or his own record) or **S** (secondary: someone else, or a registry).
- **Identifiers.** Every paper named here has a DOI, an arXiv id, or a venue + year + title. I checked each one in this run against Crossref (R29, R30), the arXiv listing and abstract pages (R18, R19), or his own publication list (R2). Where two sources give different dates, both are kept (see Contradictions).
- **Podcast quotes.** They come from an automatic speech-recognition transcript that no human has checked (R10). Each carries a timestamp and the model that produced the wording ("medium" = re-run with the larger model; "small" = the first full pass only). Misheard names are corrected in square brackets.
- **Quote normalisation.** PDF ligatures (ﬁ, ﬂ) and line-break hyphens are rejoined. Nothing else is changed. French quotes are verbatim, and my translations are in *italics* outside quotation marks.
- **Cross-references.** Research notes 01, 02 and 04 were written earlier in this run. Wherever I use a fact from them without re-checking it, I say so. Most of their trajectory facts I re-fetched and checked myself (R1–R35).

---

## 0. The trajectory in one screen

1. **Seven research eras over about 50 years (1974–2026).** Each era follows one core question, and there is no gap between them. The eras are:
   - PDE optimal control (master's thesis, 1974);
   - derivative-free conjugate directions, then sparse quasi-Newton (thesis, 1975–78);
   - sparsity and partial separability (1979–86);
   - Conn–Gould–Toint (CGT) globalisation for large-scale problems, with software and test sets (1986–2000);
   - non-monotone and filter acceptance (1994–2007);
   - worst-case evaluation complexity (2007–2023);
   - objective-function-free (OFFO) and adaptive methods for noisy and machine-learning problems (2021–26).

   Two side lines run in parallel: transport modelling (1975–2015) and derivative-free optimization (1994–2022). [practice, P, timeline §1]
2. **What triggered the turns, as he tells it.**
   - An advisor's offer: Powell proposed "SQP" or "large-scale" as thesis topics.
   - A shared need met at a conference: "the needs to work on large scale problems and the needs to write software to do it."
   - A software need: CUTE was built because LANCELOT needed test problems.
   - A new idea by friends, whose theory was missing: filters.
   - A new result by others, whose practical side was missing: Nesterov–Polyak "no numerical results were provided".
   - A gap left by fashion: complexity theory was "for the convex case".
   - A funding call with a partner: the ADTAO data-assimilation project with Gratton.
   - An empirical fact from machine learning: the popularity of Adagrad and Adam under noise.
   - Tool decline: "the use of Fortran has significantly declined since 1995".

   Each trigger is sourced in §3. [stated, P]
3. **When he enters and leaves a topic.** For ideas that are new in NLP he enters early, inside one or two years of the originating result: filter proposed May 1996, SLP-filter proof 1998; Nesterov–Polyak 2006, ARC reports September 2007. For the ML optimizers he arrives late relative to the ML consensus (Adagrad and Adam were already "very popular" when he started in 2022), but early in the NLP complexity community, and he comes with theory and counterexamples rather than benchmarks. He leaves topics quietly. He never announces an exit: transport "diverge[d]"; filters stop after 2007 apart from a 2016 tribute; the CGT line stops producing after the 2022 book. [inferred from §1 and §4]
4. **The institutional arc.** He was hired as a teaching assistant in 1974 and stayed at one university for his whole career. He carried heavy administration while his output was at its highest: head of computer services 1998–2000, department director 2006–09, MOS chair 2010–13, vice-rector around 2015. He retired on 2016-08-31. After retirement his output did not fall: he began posting on arXiv (2017), moved his base of work to Toulouse (CIMI chair 2016–18, then ANITI-funded work), and in 2024–26 writes his own code in Matlab, Python and Julia. [practice, P/S, §1, §6]

---

## 1. Dated timeline (master table)

Kinds: E = education or position, H = honour, R = research event or paper, S = software or infrastructure, T = transport or other side line, L = lineage.

| Date | Kind | Event | Tag | Src |
|---|---|---|---|---|
| 1952 | E | Born in Brussels ("I was born in Brussels, like a lot of Belgians", [0:01:34], small). The Imperial bio also gives "born 1952". | stated / S | R10, R9 |
| 1970 | E | Starts mathematics at Namur and also takes physics for two years before dropping it, because the physics labs took too much time ([0:12:03–0:12:18]). The 1970 date is the host's; Toint does not correct it. | stated (ASR) | R10 |
| 1974 | E | Master in Mathematics, Namur. The master's thesis is "La méthode de Ritz Galerkin en contrôle optimal : convergence et calcul de l'erreur" (1974). He calls PDE-constrained optimal control "more fashionable at the time than nonlinear optimization, for sure" ([0:14:00–0:14:08], small). | practice / stated | R6, R10 |
| 1974-09-15 | E | Hired by Namur as a teaching assistant, "half-time research and half-time teaching" ([0:14:56–0:15:07], small). His PhD starts the same day, per ORCID (education 1974-09-15 → 1978-05). | stated / P | R10, R4 |
| 1975 | R, L | First conference, Dundee. He meets Powell there, and Powell proposes to supervise him: "why don't you work with me?" ([0:17:37–0:17:56], small). His first report on derivative-free methods is with his local advisor Callier ("On Quadratic Function Minimization: The n-step Termination Property Can Imply The Conjugateness of Search Directions", report 75/1, 1975). | stated / practice | R10, R2 |
| 1975 | T | "Namur 0, un modèle de circulation pour l'agglomération namuroise", report 75/8 (Duchâteau & Toint, 1975). This is the start of the transport line, in the same year as his first optimization report. | practice, P | R2 |
| 1977-01 | E | Arrives in Cambridge "on Royal Society's funding in January 1977, after waiting a year during Mike's move from Harwell to Cambridge" (Powell memoir, preprint p. 14). | stated, co-authored, P | R12 |
| 1977 | R | The thesis topic turns from derivative-free conjugate directions (Toint & Callier, *JOTA* 23 (1977), DOI 10.1007/BF00933294 and 10.1007/BF00933295) to sparse quasi-Newton updating ("On sparse and symmetric matrix updating subject to a linear equation", *Math. Comp.* 31 (1977), DOI 10.1090/S0025-5718-1977-0455338-4). See Turn 1 in §3. | practice, P | R29 |
| 1978 | E, L | PhD, Namur. The thesis is "Unconstrained Optimisation : The Analysis of Conjugate Directions Methods without Derivatives and a New Algorithm Using a Sparse Quasi-Newton Update". Advisor 1 is M. J. D. Powell and advisor 2 is F. M. Callier (MGP). Powell chaired the examination committee ([0:34:29], small). ORCID gives the end date as 1978-05. | S / stated | R5, R10, R4 |
| 1979 | E, T | Appointed lecturer at Namur. From 1979 he is co-director of the Numerical Analysis Unit and director of the Transportation Research Group (Edinburgh notice; the Imperial bio says the same). | S | R8, R9 |
| 1979 (summer) | L | At ISMP Montréal, as "a fresh PhD", he meets Conn. He visits Waterloo and meets Gould (V&N 27(2) p. 9; podcast [0:38:32–0:39:12]). | stated, P | R11, R10 |
| 1979 | R | Powell & Toint, "On the Estimation of Sparse Hessian Matrices", *SINUM* 16 (1979), DOI 10.1137/0716078. This paper became "Appendix 7" of his thesis, which he says upset Powell ([0:33:52–0:34:11], small). | practice / stated | R29, R10 |
| 1980, 1983 | S | Harwell Subroutine Library routines: TD03AD, sparse Hessian estimation (1980), and VE08AD, partially separable optimization with bounds (1983). | practice, P | R2 |
| 1982 | R | Griewank & Toint, "Partitioned variable metric updates for large structured optimization problems", *Numer. Math.* 39 (1982), DOI 10.1007/BF01399316. Partial separability begins here. | practice | R29 |
| 1983 | S | "Test problems for partially separable optimization and results for the routine PSPMIN", report 83/4 (1983). This is "Toint's collection", later absorbed into CUTEst (S2MPJ p. 1). | practice / stated | R2, R22 |
| 1984 | L | Second visit to Conn, with Gould: "we started to discuss optimization of large nonlinear problems (a few tens of variables by then)" (V&N 27(2) p. 9). | stated, P | R11 |
| 1986 | R, S | "But collaboration got truly going only in 1986, when Andy, on sabbatical in Grenoble, invited Nick (then back in Europe) and me for a working week" — "the real birth of the LANCELOT project" (V&N 27(2) p. 9). The same year he publishes a solo convergence paper for his own structure idea ("Global convergence of the partitioned BFGS algorithm for convex partially separable optimization", *Math. Prog.* 36 (1986), DOI 10.1007/BF02592063). | stated / practice | R11, R29 |
| 1987 | E, S | Becomes associate professor (R8). Publishes "Call for test problems in large scale nonlinear optimization", *IMANA Newsletter* 12(1) (1987) pp. 48–52 (listed in R2; text not read). | S / practice | R8, R2 |
| 1988 | R | First CGT papers: "Global Convergence of a Class of Trust Region Algorithms for Optimization with Simple Bounds", *SINUM* 25 (1988), DOI 10.1137/0725029, and "Testing a class of methods …", *Math. Comp.* 50 (1988), DOI 10.1090/S0025-5718-1988-0929544-3. Also Lescrenier & Toint on the FPS 164 and Cray X-MP vector processors, *Int. J. Supercomputing Appl.* 2 (1988), DOI 10.1177/109434208800200105. | practice | R29 |
| 1991 | R, S, T | CGT, "A Globally Convergent Augmented Lagrangian Algorithm …", *SINUM* 28 (1991), DOI 10.1137/0728030. Also report 91/8 on the SDIF format and report 91/10 "A comprehensive description of LANCELOT". On the transport side, *Advanced Telematics in Road Transport* (EU DRIVE proceedings, Elsevier, 1991), co-edited. | practice | R29, R2 |
| 1992 | S | *LANCELOT … (Release A)*, Springer 1992, DOI 10.1007/978-3-662-12211-2. | practice | R29 |
| 1993 | E | Full professor (R8). | S | R8 |
| 1994 | H, R | Beale–Orchard-Hays Prize with Conn and Gould (listed on ORCID, the Namur portal and the Edinburgh notice). The Namur portal's "DFO: Derivative free numerical algorithms for optimization" project starts 1994-03-01 with Toint as PI. | S / P | R4, R6, R8 |
| 1995 | S | "CUTE", *ACM TOMS* 21 (1995), DOI 10.1145/200979.201043. | practice | R29 |
| 1996-05 | R | "NLP filter methods were first proposed by Fletcher in a plenary talk at the SIAM Optimization Conference in Victoria in May 1996" (V&N 18(1) p. 5). In the same year Toint publishes a solo non-monotone line-search assessment (*SISC* 17 (1996), DOI 10.1137/S106482759427021X). | stated, co-authored / practice | R13, R29 |
| 1997 | R | Solo paper on non-monotone trust regions, *Math. Prog.* 77 (1997), DOI 10.1007/BF02614518. DFO survey with Conn and Scheinberg, *Math. Prog.* 79 (1997), DOI 10.1007/BF02614326. Transport: Bierlaire, Lotan & Toint, *Transp. Sci.* 31 (1997), DOI 10.1287/trsc.31.4.363. | practice | R29 |
| 1998–2000 | E | In charge of the University Computer Services (R8). | S | R8 |
| 1999 | R | GLTR: Gould, Lucidi, Roma & Toint, *SIOPT* 9 (1999), DOI 10.1137/S1052623497322735. | practice | R29 |
| 2000 | R | Conn, Gould & Toint, *Trust-Region Methods*, SIAM 2000, DOI 10.1137/1.9780898719857. The book "started as a course I thought [taught] in my university" and "grew to 900 pages" ([0:47:56–0:48:27], medium). | practice / stated | R29, R10 |
| 2002 | R | Filter-SQP convergence: Fletcher, Leyffer & Toint, *SIOPT* 13 (2002) 44–59, DOI 10.1137/S105262340038081X. Trust-region SQP-filter with Gould and Wächter, *SIOPT* 13 (2002) 635–659, DOI 10.1137/S1052623499357258. EPSRC fellowship 1 Nov 2002 (Namur portal). | practice / S | R29, R6 |
| 2003 | S, H | GALAHAD and CUTEr papers, *ACM TOMS* 29(4) (2003), DOI 10.1145/962437.962438 and 10.1145/962437.962439. Erskine Fellow at Canterbury, Jan–Apr 2003 (ORCID). EPSRC fellowship May 2003 (portal). | practice / P | R29, R4, R6 |
| 2004 | R | Gould & Toint, "How Mature is Nonlinear Optimization?", in *Applied Mathematics Entering the 21st Century: Invited Talks from the ICIAM 2003 Congress*, SIAM 2004, pp. 141–161 (from his list; the text was read by agent 02, not by me). | stated | R2, R38 |
| 2005 | R | *Acta Numerica* survey, Gould, Orban & Toint, vol. 14 (2005), DOI 10.1017/S0962492904000248. Filter trust region for unconstrained problems, Gould, Sainvitu & Toint, *SIOPT* 16 (2005), DOI 10.1137/040603851. | practice | R29 |
| 2006 | H | **Lagrange Prize in Continuous Optimization** (MPS and SIAM), shared with Fletcher and Leyffer, for Fletcher & Leyffer, "Nonlinear programming without a penalty function", *Math. Prog.* 91 (2002) 239–269, DOI 10.1007/s101070100244, and the Fletcher–Leyffer–Toint *SIOPT* 13 (2002) paper. The committee was Dennis, Gould, Lewis and Todd (chair) (*Optima* 73 p. 5). | S | R14, R15, R4 |
| 2006–2009 | E | Director of the Department of Mathematics (R8). | S | R8 |
| 2007 | R | Fletcher, Leyffer & Toint, "A Brief History of Filter Methods", *SIAG/OPT Views-and-News* 18(1) (March 2007) 2–12. This is his last new filter paper that I found (see §4). The ARC ("ACO") report, Part I, is dated 29 Sep 2007 (TR07-05a). | practice | R13, R23 |
| 2008 | R, L | Gratton, Sartenaer & Toint, "Recursive Trust-Region Methods for Multiscale Nonlinear Optimization", *SIOPT* 19 (2008), DOI 10.1137/050623012. This is the earliest Gratton–Toint journal paper in Crossref. The Namur portal project "Complexity in nonlinear optimization" (Toint, Gould, Cartis) starts 2008-11-01. Gould & Toint, "Nonlinear programming without a penalty function or a filter", *Math. Prog.* 122 (2010; online 2008-09-23), DOI 10.1007/s10107-008-0244-7. | practice | R30, R6, R29 |
| 2009 | H, R | SIAM Fellow, class of 2009 (homepage, ORCID). Francqui Chair, KU Leuven, 2009 (ORCID). EPSRC fellowship Jan 2009 (portal). ARC Part I online 2009-05-19 (*Math. Prog.* 127 (2011), DOI 10.1007/s10107-009-0286-5). | P / practice | R1, R4, R6, R29 |
| c. 2009–2010 | R | A long stay in Toulouse as external expert of the ADTAO data-assimilation project, with Gratton (slides, June 2010; the exact dates of the stay are not given). See Turn 6. | stated, P | R25 |
| 2010 | H, E, R | Honorary Professor, University of Edinburgh (ORCID; Edinburgh notice). naXys: he is a founding member (homepage: "Funding member" [sic]). He gives the talk at the "NAXYS Opening Day, Namur, October 2010" (R27 title page). Cartis, Gould & Toint, "On the Complexity of Steepest Descent, Newton's and Regularized Newton's Methods …", *SIOPT* 20 (2010), DOI 10.1137/090774100. | P / S / practice | R4, R8, R1, R27, R29 |
| 2010–2013 | E | Chairman of the Mathematical Optimization Society (homepage). The renaming from "Mathematical Programming Society" was launched in the handover with Steve Wright ([0:51:37–0:52:28], small). | P / stated | R1, R10 |
| 2012 | R | ISMP 2012 Berlin "Opening address" (talks page). Cartis, Gould & Toint, "How much patience do you have? A worst-case perspective on smooth nonconvex optimization", *Optima* 88 (2012) pp. 1–10 (from his list; not read). | practice | R3, R2 |
| 2013 | R, T | Solo paper, "Nonlinear stepsize control, trust regions and regularizations for unconstrained optimization", *OMS* 28 (2013), DOI 10.1080/10556788.2011.610458. Transport: Barthelemy & Toint, "Synthetic Population Generation Without a Sample", *Transp. Sci.* 47 (2013), DOI 10.1287/trsc.1120.0408. Data assimilation: Gratton, Toint & Tshimanga, *QJRMS* 139 (2013), DOI 10.1002/qj.2050. | practice | R29 |
| 2014 | S, T, L | CUTEst, *COAP* 60 (2015; online 2014-08-24), DOI 10.1007/s10589-014-9687-3. Last transport PhD: Barthélemy (MGP, 2014). His last transport-policy talk on his talks page is "Gouvernance intelligente : un outil intégrateur" (MIPIM 2014, Cannes). | practice | R29, R5, R3 |
| 2015 | E, H, T, L | In February 2015 he "currently serves as Vice-rector for Research and IT" (Imperial seminar bio, 11 Feb 2015). Leverhulme Fellow and Oliver Smithies Fellow at Balliol, Sep–Dec 2015 (ORCID). Last MGP student: Rodrigues Sampaio, 2015. Last transport paper found: Barthelemy & Toint, "A Stochastic and Flexible Activity Based Model for Large Population. Application to Belgium", *JASSS* (2015), DOI 10.18564/jasss.2819. | S / P / practice | R9, R4, R5, R30 |
| 2016-08-31 | E | End of employment at Namur (ORCID). Emeritus from then (homepage). The host dates retirement to 2016 ([0:58:22], small). | P | R4, R1, R10 |
| 2016–2018 | E | "Chaire d'Excellence CIMI", Toulouse INP (ORCID). The talks page lists "Adventures in the jungle of high-degree nonlinear optimization (CIMI, Toulouse, France)" in 2017. | P | R4, R3 |
| 2016 | R, L | Curtis, Gould, Robinson & Toint, "An interior-point trust-funnel algorithm for nonlinear optimization", *Math. Prog.* 161 (2017; online 2016-04-07), DOI 10.1007/s10107-016-1003-9. Tribute talk "Filter methods: a tribute to Roger Fletcher" (ICNAAO Beijing, Aug 2016). | practice | R29, R28 |
| 2017-04 | R | First arXiv posting: Chen, Toint & Wang, arXiv:1704.06919 (23 Apr 2017). All 53 of his arXiv papers date from after his retirement. | practice, P | R18 |
| 2017 | R, S | BFO: Porcelli & Toint, *ACM TOMS* 44 (2018; online 2017), DOI 10.1145/3085592. High-order regularization with the São Paulo group: Birgin, Gardenghi, Martínez, Santos & Toint, *Math. Prog.* 163 (2017; online 2016-08-30), DOI 10.1007/s10107-016-1065-8. | practice | R29 |
| 2018 | H, R | Invited speaker at ICM 2018, Rio (ORCID; talks page). Chapter: Cartis, Gould & Toint, DOI 10.1142/9789813272880_0198 (Crossref pp. 3711–3750; his list gives vol. 4 pp. 3729–3768). Powell memoir, DOI 10.1098/rsbm.2017.0023. Variable-precision note, arXiv:1812.03467 (Dec 2018). | P / practice | R4, R3, R29, R2, R19 |
| 2019 | R | Toint's memoir of Conn, *SIAG/OPT V&N* 27(2) (2019) pp. 9–10. | P | R11 |
| 2020 | R | His list includes Bellavia, Gurioli, Morini & Toint, "A stochastic ARC method with inexact function and random derivatives evaluations", "Proceedings of the International Conference on Machine Learning (ICML), 2020". **I could not find it in the PMLR vol. 119 index**; see Contradictions. | practice, unverified | R2, R34 |
| 2021-12 | S | OPM, a collection of CUTEst problems in Matlab, arXiv:2112.05636 (v1 10 Dec 2021; v2 16 Jan 2025). | practice | R19 |
| 2022 | R | *Evaluation Complexity of Algorithms for Nonconvex Optimization*, Cartis, Gould & Toint, SIAM 2022, DOI 10.1137/1.9781611976991. OFFO turn: arXiv:2203.01647 (v1 3 Mar 2022) and arXiv:2203.09947 (v1 18 Mar 2022; the latter coins "OFFO"). | practice / stated | R29, R19, R20, R21 |
| 2023 | R | Multilevel OFFO for neural-network training: Gratton, Kopaničáková & Toint, *SIOPT* 33 (2023), DOI 10.1137/23m1553455. Solo counterexample, "Divergence of the ADAM algorithm with fixed-stepsize: a (very) simple example", arXiv:2308.00720, later a chapter in *Mathematical Optimization for Machine Learning* (De Gruyter, 2025), DOI 10.1515/9783111376776-013. Last Cartis–Gould–Toint item in Crossref: the ICM 2022 chapter, "The evaluation complexity of finding high-order minimizers of nonconvex optimization", DOI 10.4171/icm2022/95, published 2023-12-15. | practice | R29, R30, R19 |
| 2024-01-19 | L | Defence of S. Jerad (Toulouse; theses.fr gives Gratton as sole director). Jury: Gratton, Bellavia (president), Toint, Bolte, **Frank E. Curtis**, E. Simon; reviewers Krause and Cartis. | S | R35 |
| 2024-05-31 | S | First commit of S2MPJ on GitHub (GrattonToint/S2MPJ). 106 of 134 commits are by Toint (accounts `phtoint` and "Philippe Toint"). | practice, P | R31 |
| 2024 | R | S2MPJ paper, arXiv:2407.07812 (*OMS* 40 (2025), DOI 10.1080/10556788.2025.2490640). Solo paper, "Examples of slow convergence for adaptive regularization optimization methods are not isolated", arXiv:2409.16047 (*Math. Prog.* 2025, DOI 10.1007/s10107-025-02286-1). Preface with Gratton, Gondzio, Nesterov and Yuan, *OMS* 39 (2024), DOI 10.1080/10556788.2024.2406663. | practice | R19, R29 |
| 2025-09 → 2026-09 | — | Last 12 months: see §7. | — | — |

---

## 2. Lineage

### 2.1 Upward: his advisors, and how the topic was chosen

- **Registry** [S, R5]: MGP id 87096 lists advisor 1 as Michael James David Powell and advisor 2 as Frank Maria Callier (Namur, 1978).
- **The local start** [practice, P, R2, R29]: his first reports and papers (1975–78) are with Callier and J.-J. Strodiot on derivative-free conjugate-direction methods and subspace decomposition. Example: Toint & Callier, *JOTA* 23 (1977), DOI 10.1007/BF00933295.
- **The switch to Powell's topic** [stated, P]. The memoir (co-authored) says Powell's interest in large problems "led him to suggest this research topic to a young PhD student, Philippe Toint", and that "The idea was to extend the variable metric ideas to structured problems with structurally sparse Hessian matrices" (R12, preprint p. 14). In Toint's spoken version, Powell offered a choice: "He told me I could choose between two subjects. One was SQP and the other one was large-scale non-linear problems. I did the wrong choice. I chose the second. Otherwise, my name would be associated with SQP, but that's too bad." ([0:15:38–0:15:55], medium, R10). He treats this as a joke, not a regret; agent 02 reads it the same way (R38 P7).
- **What he took from Powell** is in `04-mentorship.md` §5 (R39): daily lunches discussing "my progress or my lack of progress", no vagueness, "hard to convince … your best advocate".

### 2.2 Downward: doctoral students by era

MGP lists 20 students (1985–2015) and 49 descendants (R5). theses.fr adds two Toulouse co-directions (Tröltzsch 2011, Gürol 2013; R35). There is also the informal case of Jerad (2024; R35). `04-mentorship.md` §1 has the full roster with joint-paper DOIs (R39). Here I only map students onto the eras, because the mapping shows how the group followed his turns [practice, S]:

| Era of Toint's programme | Students (MGP year) | Link to the turn |
|---|---|---|
| Sparsity, least squares, geodesy (1979–86) | Manneback 1985, Murigande 1986 | Structured linear algebra and application |
| CGT trust regions, networks, inverse problems (1986–93) | Lescrenier 1989, Sartenaer 1991, Tuyttens 1991, Sebudandi 1992, Burton 1993 | Built alongside LANCELOT |
| Transport (1975–2015) | Bierlaire 1996, Bastin 2004 (with Louveaux), Barthélemy 2014 (with Cornelis) | Transport group |
| GALAHAD/CUTEr, interior points, DFO, bilevel (1995–2005) | Orban 2001, Schulze 2002 (Trier), Colson 2003 (with Savard) | Software era |
| Filter (1998–2007) | Sainvitu 2007 | Filter trust region |
| Multilevel with Gratton (2005–11) | Mouffe 2009, Tomanos 2009, Weber Mendonça 2009, Malmedy 2010, Thekale 2011 (Erlangen); Tröltzsch 2011 (INPT) | Recursive trust region |
| Data assimilation with Gratton | Gürol 2013 (INPT) | ADTAO line |
| Complexity (2007–) | Rodrigues Sampaio 2015 | Complexity + DFO |
| OFFO (2021–) | Jerad 2024 (formally Gratton's; Toint on the jury) | OFFO/Adagrad |

[inferred] Every era after 1985 has at least one thesis attached. Formal supervision stops with his retirement (last MGP student 2015). Afterwards his junior co-authors (Jerad, Kopaničáková, Seraghiti, Sim) appear only on papers with his partners: Gratton (Jerad, Kopaničáková, Sim) and Porcelli (Seraghiti) (R19, R29). I did not check where these juniors work.

### 2.3 Sideways: collaborator generations (who carried each era)

[practice, P/S: R29, R30, R11, R10, R19]

| Period | Main partners | Start trigger (stated or inferred) | How it ended |
|---|---|---|---|
| 1977–81 | Powell (2 joint papers: *SINUM* 1979, DOI 10.1137/0716078; the 1981 Shanno–Toint note in *IMA JNA* 1, from his list) | Thesis supervision [stated] | Thesis finished. "I've co-authored only two papers with Michael Powell" ([0:33:52], small) |
| 1981–84 | Griewank (partial separability, *Numer. Math.* 1982, DOI 10.1007/BF01399316) | Not stated. Griewank was at DAMTP Cambridge in 1981 (the ARC Part I report cites "Technical Report NA/12, 1981, DAMTP"), so a Powell-group contact is [inferred] | Griewank "got interested in automatic differentiation and did most of his career in this sector later on" ([0:40:56–0:41:04], small) [stated] |
| 1986–2007 (Conn); 1986–2023 (Gould) | Conn, Gould (CGT) | Met 1979, talked 1984, working week in Grenoble 1986 (R11) [stated] | Conn: collaboration "for some years" after 2000, then DFO with Scheinberg (R11); Conn died in 2019. Gould: the last joint item in Crossref is the ICM 2022 chapter (published 2023). No stated end |
| 1998–2007 | Fletcher, Leyffer (+ Wächter 2002) | Fletcher's May 1996 filter proposal (R13 p. 5) | "Brief History" (2007), then the 2016 tribute (R28) |
| 2005/08–2026 | Gratton (Toulouse; CERFACS, then INPT/IRIT/ANITI) | "I'm still doing research with somebody I met in the 1990s in the mid-90s, Serge Graton [Gratton], who was a student in CERFAC [CERFACS]" ([0:58:52–0:59:06], small). Earliest joint journal paper in Crossref: 2008 | Ongoing. 11 of his 12 most recent works are with Gratton (`01-publications.md` §1.6, R37; consistent with R18) |
| 2007–2023 | Cartis (+ Gould) | Nesterov–Polyak 2006; ARC reports Sep 2007 (R23) | The 2022 book and the ICM 2022 chapter are the last items in Crossref |
| 2010–2026 | Bellavia, Morini (Florence), Gurioli (2018–23), Porcelli (2011–2025) | The first Bellavia item is a five-author regularized least-squares paper with Cartis and Gould, *SINUM* 2010, DOI 10.1137/080732432 | Ongoing: *JOTA* 2026, DOI 10.1007/s10957-026-03004-3; arXiv:2602.11770; arXiv:2505.06374 |
| 2016–2017 | Birgin, Martínez et al. (São Paulo); Chen (Hong Kong PolyU); Curtis–Robinson | Not stated anywhere I read | One or two papers each: DOI 10.1007/s10107-016-1065-8; 10.1137/18m1166511; 10.1007/s10107-016-1003-9 |

### 2.4 Links to other members of the Nonlinear team (verified only)

- **Gould**: CGT, 1986–2023 (R11, R30).
- **Fletcher**: Lagrange Prize 2006 (R14). Toint co-authored the 2018 Powell memoir with Fletcher and gave the 2016 tribute talk (R12, R28).
- **Wächter**: co-author of the trust-region SQP-filter paper, DOI 10.1137/S1052623499357258 (R29).
- **Curtis**: co-author of the interior-point trust funnel, DOI 10.1007/s10107-016-1003-9. Also a fellow jury member at Jerad's 2024 defence (R35).
- **Nesterov**: ARC is built explicitly on Nesterov–Polyak (R23). Nesterov co-signed the 2024 *OMS* preface with him (DOI 10.1080/10556788.2024.2406663).
- **S. J. Wright**: his predecessor as MOS chair, who launched the renaming with him ([0:51:37–0:52:28], small).
- **Gill**: named, with Murray, M. Wright and Saunders, as having "take[n] the lead in using very good linear algebra techniques in optimization" ([0:19:38–0:19:54], small). Speakers are not labelled in the transcript; the passage reads as Toint's.
- No verified joint work with Nocedal or Ye was found (not searched exhaustively).

---

## 3. The turns: what triggered each, and when he entered and left

Each turn has: what changed, the trigger (stated vs inferred), the entry timing relative to the field, the exit, and the resource context.

### Turn 0 → 1 (1974–77): from PDE optimal control to derivative-free conjugate directions to sparse quasi-Newton

- **What changed.** The master's thesis was on Ritz–Galerkin methods in optimal control (1974, R6). The thesis started on derivative-free conjugate-direction methods with Callier (1975–77, R2). The core became sparse quasi-Newton updating with Powell (1977).
- **Trigger** [stated, P]: meeting Powell at Dundee in 1975. "And then he said, why don't you work with me? And I said, sure." ([0:17:54–0:17:58], small). Then Powell offered the SQP-or-large-scale choice (§2.1). Context he gives about the field at the time: "numerical analysis was dominated by PDEs" ([0:13:42–0:13:46], small).
- **Timing** [stated / observed]: at the frontier, in competition. He "managed to get the result first" ahead of a student of John Dennis on sparse quasi-Newton updates ([0:27:57–0:28:05], small). Powell smoothed the resulting friction with a letter to Dennis (R39 M6).
- **Resource context** [stated, P]: "large at the time meant 50 variables" ([0:33:23–0:33:38], small). A Siemens 4004 at Namur (report 76/4, R2). A Royal Society grant. Test problems exchanged on paper.

### Turn 2 (1979–86): sparsity to partial separability, and software through Harwell

- **What changed.** From sparse matrices to function structure: partially separable functions (Griewank & Toint 1982, DOI 10.1007/BF01399316), with codes released through the Harwell Subroutine Library (TD03AD 1980, VE08AD 1983) and his own test collection (report 83/4) (R2).
- **Trigger.** Not stated as an event. His own later account of why the structure matters: "when you have structure, whatever it is, you should take advantage of it. Structure is what allows us to solve large problems. If they were unstructured, we would be just lost." ([0:43:11–0:43:22], medium) [stated, P]. The partial-separability idea "was not directly in my thesis, but came just immediately after" ([0:33:10–0:33:14], small).
- **Entry timing** [inferred]: early. Partial separability is his and Griewank's own construction; there was no field to enter.
- **Exit.** He never left the structure idea. It returns in LANCELOT's group-partially-separable format, in DFO ("Exploiting Problem Structure in Derivative Free Optimization", *ACM TOMS* 48 (2022), DOI 10.1145/3474054), and in complexity (Chen, Toint & Wang, *SIOPT* 29 (2019), DOI 10.1137/18m1166511). The January 2026 talk title is "Stochastic ADAGRAD with bounds, curvature (and problem structure)" (R6). [practice, P]

### Turn 3 (1986–2000): CGT, i.e. globalization + code + test set + book

- **Trigger** [stated, P], in two versions (see Contradictions C1):
  - written, 2019: "My second visit to Andy followed in 1984, where we started to discuss optimization of large nonlinear problems (a few tens of variables by then) together with a colleague of his named Nick Gould. The discussion were lively and we had marvellous plans on how to develop our new ideas and associated code. But collaboration got truly going only in 1986, when Andy, on sabbatical in Grenoble, invited Nick (then back in Europe) and me for a working week." (R11 p. 9);
  - spoken, 2026: "discussed the main thing, the needs to work on large scale problems and the needs to write software to do it. And we didn't do anything for a while. And then a few years later, I think it was in 81, Andy went for a sabbatical in France in Grenoble." ([0:39:04–0:39:25], medium).
- **The CUTE sub-turn** [stated, P]: "When we worked on Lancelot, we needed the collection of test problem to test the software on. And at the time, test problems were exchanged by exchanging reports and pieces of paper. And so there was a very high likelihood of reproducing or introducing mistakes in the statements of the functions or the derivatives" ([0:45:36–0:45:57], medium). On its reception: "the success was beyond our expectation" ([0:46:50–0:46:53], medium).
- **The book sub-turn** [stated, P]: "this book started as a course, I thought [taught], in my university … And unfortunately, maybe we could not stop." ([0:47:56–0:48:19], medium). He was PI of a funded project for the book, 1997-01 → 2000-03, per the Namur portal as read by agent 01 (R37). I could not re-read that record because the projects sub-page returned 403 (R7).
- **Entry timing** [inferred]: early and constructive. Trust-region theory existed for unconstrained problems (Powell 1970, per his own account, [0:36:45–0:36:57], small), but CGT's first papers (1988) extend it to bounds and, in 1991, to general constraints through an augmented Lagrangian. The software was "one of the first or maybe the first … package for solving large scale non-linear problems" together with MINOS ([0:44:02–0:44:19], small) [stated].
- **Resource context** [practice / stated]: a three-person team across countries (Namur; Waterloo, then IBM; Waterloo, then RAL). Work was done "from letters and email to (many) visits and meetings at conferences" (R11 p. 9). Fortran. Vector machines (Lescrenier & Toint 1988). Free distribution with one restriction: "We didn't want it to be used for the design of weapons" ([0:45:05–0:45:15], medium). Toint was also directing the transport group (R8).

### Turn 4 (1994–2007): non-monotone acceptance, then the filter

- **What changed.** The two solo non-monotone papers (1996 *SISC*, 1997 *Math. Prog.*) came first. Then the joint filter theory from 1998 (report 98/13 per R37; I did not re-check it). Published in 2002 (two *SIOPT* papers), then extended (multidimensional filter, *SIOPT* 15 (2004), DOI 10.1137/S1052623403422637; filter trust region, DOI 10.1137/040603851).
- **Trigger** [stated, co-authored, P]: an observation from test sets, plus a friend's new idea. "Yet we have noticed that the unmodified sequential quadratic programming (SQP) method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence." and "Our goal therefore is the development of global optimization safeguards that interfere as little as possible with Newton's method." (R13 p. 3). In the podcast: "the idea was originated with Roger Fletcher and Sven Leifer [Leyffer]. And I work with them to establish the theory, the convergence theory for that method" ([0:51:06–0:51:20], small).
- **Entry timing** [practice]: early. The idea was proposed in May 1996; the first convergence proof (SLP) came next, "later generalized to SQP methods" (R13 p. 5). The 2006 prize citation credits his paper with "novel techniques to provide a satisfying proof of correctness for the filter approach in its original SQP context" (*Optima* 73 p. 5, R14) [observed, S].
- **Exit** [practice / inferred]: I found no new filter paper after 2007 in Crossref or on his list, apart from the 2016 tribute talk. His 2016 conclusions keep the question open: "non-monotonicity definitely helpful / Newton's behaviour unexplained" (R28 p. 28) [stated]. His 2025–26 constrained algorithms explicitly avoid filters: "without using a merit function or filter" (arXiv:2510.16390 abstract, R19). The 2007 side path already did the same in its title ("Nonlinear programming without a penalty function or a filter", DOI 10.1007/s10107-008-0244-7, which needed an erratum, DOI 10.1007/s10107-011-0491-x). [inferred] He left the filter as a *proof object*, but he kept its design goal (disturb Newton or the base method as little as possible) and carries it into OFFO.

### Turn 5 (2003–2011): multilevel trust regions and the Toulouse link

- **What changed.** Trust-region methods that exploit a hierarchy of discretizations (*SIOPT* 19 (2008), DOI 10.1137/050623012). This was carried by the Namur multilevel cohort (4 theses 2009–10) and co-directed with Gratton (R39).
- **Trigger.** No explicit account found. His 2010 slides say how he came to Toulouse: "une longue collaboration avec le CERFACS dans le secteur de l'optimisation/algèbre linéaire numérique", "dans le comité scientifique" (R25 p. 2) [stated, P]. *A long collaboration with CERFACS in optimization and numerical linear algebra; on the scientific committee.* The multilevel paper also carries his first complexity result: the ARC-era report says "The authors are only aware of the analysis by Gratton, Sartenaer and Toint (2008), (Corollary 4.10) where a bound on the complexity of an inexact variant of the trust-region method is shown to be of the same order as that of steepest descent" (TR09-14 p. 3, R24) [stated, co-authored, P]. [inferred] The complexity turn therefore grew partly out of the multilevel work.

### Turn 6 (c. 2008–2013): data assimilation, taken on through a funding call

- **Trigger** [stated, P], from the slide "Comment j'ai atterri dans le projet ADTAO" (*How I landed in the ADTAO project*): "une longue collaboration avec le CERFACS", "Serge Gratton et l'assimilation de données", "Appel à projet de la Fondation STAE . . . (montage du projet et formulation)" (R25 p. 2). *Serge Gratton and data assimilation; a call for projects from the STAE Foundation (setting up and formulating the project).* The mode was a "séjour de longue durée (plusieurs mois)" (p. 5), *a long stay of several months*. The reported outputs: "nouvelles méthodes numériques, boîte à outil algorithmique pour les modélisateurs, 2 articles scientifiques, présentations à 3 conférences internationales, une nouvelle thèse et un post-doctorat en cours" (p. 6).
- **In his spoken memory** [stated, ASR small]: "The first thing I did with him, he was mostly doing data simulation [assimilation] at the time. And I joined him on a project like that." ([0:59:50–0:59:59]). **This conflicts with the paper record**; see Contradiction C3.
- **Record** [practice]: range-space Krylov methods (*SIMAX* 32 (2011), DOI 10.1137/090780493); *QJRMS* 139 (2013), DOI 10.1002/qj.2050; data-assimilation talks 2011–2015 (R3). Then "we moved to other topics like regularization method" ([1:00:11–1:00:16], small).
- **Entry timing** [inferred]: as an outside expert invited into a domain that was already established, where his contribution was large-scale linear algebra and optimization.

### Turn 7 (2007–2023): worst-case evaluation complexity

- **Trigger** [stated, co-authored, P]. Nesterov and Polyak had proved the better bound, "but no numerical results were provided". The aim: "Our purpose here and in [2] is to unify and extend these contributions into a coherent and numerically efficient algorithmic framework, for which global and asymptotic convergence results can be proved under weaker assumptions and with simpler proofs, while preserving the good complexity bound shown by Nesterov and Polyak [25]." (TR07-05a pp. 1–2, R23). The first evidence offered was numerical: "Numerical experiments with small-scale test problems from the CUTEr set show superior performance of the ACO algorithm when compared to a trust-region implementation." (abstract).
- **Retrospective reason** [stated, P]: "it was a time where complexity began to be a major buzzword in optimization. And a lot of the theory was and still is for the convex case. We thought that doing theory for the non-convex case was important and useful." ([1:02:05–1:02:24], medium).
- **An earlier doubt about the field, which this answered** [stated, P]: the 2008 slide "Unconstrained optimization — a “mature” area?" (R26 p. 6). The same deck's conclusions still ask for "Meaningful numerical evaluation still needed" (p. 36).
- **Entry timing** [practice]: about one year after Nesterov & Polyak, "Cubic regularization of Newton method and its global performance", *Math. Prog.* 108 (2006) 177–205, DOI 10.1007/s10107-006-0706-8 (online 2006-04-25); the ARC report is dated Sep 2007. This was before "complexity" became the "buzzword" he describes. The surprise result came within three years: "A big surprise: Newton's method may require as much as ⌈κC ϵ^-2⌉ function evaluations" (naXys opening day, Oct 2010, R27 p. 21).
- **Resource context** [practice]: EPSRC grant GR/S42170 (acknowledged in TR07-05a). His EPSRC fellowships of 2002, 2003 and 2009 (R6). The Namur project from 2008-11 (R6). Experiments were small CUTEr tests. At the same time he was department director (2006–09), MOS chair (2010–13) and vice-rector (c. 2015).
- **Wind-down** [practice]: consolidated in the 2022 SIAM book. The last CGT item in Crossref is the ICM 2022 chapter (published Dec 2023). He himself now calls the book "too weak [big] for my taste" ([1:02:45–1:02:50]; both models give "weak"; "big" is my reading, as in R38 F11). He keeps producing solo or small-team *sharpness* notes: arXiv:2409.16047 (2024), arXiv:2408.09124 (2024), and the "simple proof" of DCA complexity with an example "indicating that the rate cannot be improved" (arXiv:2601.15970 abstract, 2026).

### Turn 8 (2021–2026): objective-function-free (OFFO), Adagrad-type and ML optimizers

- **Trigger** [stated, co-authored, P]: an empirical regularity reported by others. "a number of these contributions … indicate that, when the (noisy) objective function is evaluated, its accuracy is significantly more critical to ensure convergence than that of the computed (noisy) derivatives. This may be the reason why methods where the objective function is not evaluated, such as Adagrad [10], RMSProp [21], Adam [15] or AMSGrad [20], have become very popular in the context of finite-sum minimization" (arXiv:2203.01647v1 p. 1, R20). And in arXiv:2203.09947v1 p. 1 (R21): "Such methods, coined OFFO for Objective-Function-Free Optimization, have recently been very popular in the context of noisy problems, in particular in deep learning applications" and "it is our point of view that their deterministic (noiseless) counterparts are good stepping stones to understand their behaviour."
- **The question he carries over from Turn 7** [stated, co-authored, P]: "Is such an improvement in complexity also possible for (noiseless) OFFO algorithms? We answer this question positively in what follows." (R21 p. 2).
- **Institutional trigger** [practice, P]: the funding line on these papers is "Partially supported by ANITI" (Toint) and "3IA Artificial and Natural Intelligence Toulouse Institute (ANITI) … ANR-19-PI3A-0004" (Gratton) (R20 p. 1, R21 p. 1, R22 p. 1). The CIMI chair (2016–18, R4) and the February 2026 ANITI visit (R6) place him in Toulouse's AI institute. In his words, with Gratton "we continue to be interested, for instance, in the method for deep learning and network training" ([0:59:17–0:59:27], small).
- **Entry timing** [inferred, with dated basis]: late relative to ML practice. Adagrad, RMSProp and Adam predate 2022 and were already "very popular" by his own account. Early relative to NLP complexity theory: he claims the first O(ε^-3/2) OFFO bound (R21). Muon, a recent ML optimizer, appears in his April 2026 title (arXiv:2604.17423), so he now tracks ML optimizer fashion within months. He enters with theory, counterexamples (the ADAM divergence example, arXiv:2308.00720) and variants that handle noise, bounds, constraints, multilevel structure and asynchrony. He does not compete on large GPU benchmarks. [practice, R19]
- **Return to constraints, 2025–26** [practice, P]: arXiv:2510.16390 (equality constraints), arXiv:2602.11770 (general constraints, with Florence), arXiv:2603.29685 (stochastic objective, deterministic constraints). All are "objective-function-free", use "an adaptive switching strategy between a normal step … and a tangential step" (2602.11770), and avoid "a merit function or filter" (2510.16390). [inferred] These reuse the composite-step / trust-funnel idea of 2007–2017 with Adagrad-type tangential steps.

### Infrastructure turn (2021–26): out of Fortran

- **Trigger** [stated, co-authored, P, R22]: "An interface with Matlab was first produced using the “MEX files” mechanism available in that language, but this proved difficult to maintain for all computer architectures." (p. 2). And: "one must admit that the use of Fortran has significantly declined since 1995, and that reliance on a unique tool written in this language could be problematic, in particular for the continued use of the test problem collection." (p. 2). And: "the basic design of the environment has not fundamentally changed since 1995." (p. 1).
- **Practice** [P, R31]: he writes the code himself. S2MPJ's git history has 134 commits since 2024-05-31, 106 of them by Toint. The latest are 2025-10-08 "Correction to range constraints", 2026-02-08 "coorection [sic] for Python 3.14 + hand-coded HS problems" and 2026-08-24 "adding LICENCE file". In the ralna GitHub repositories of CUTEst, SIFDecode and GALAHAD, **no commit author matches "Toint"** (R32). [inferred, with a caveat] The Fortran line is maintained by others, and his own software work moved to native Matlab, Python and Julia. The caveat: those histories may have been imported without their pre-GitHub authors.

### Side line: transport (1975–2015), entered by a family question and left by drift

- **Trigger** [stated, ASR small]: his father, an urban planner, "asked me one day, what can you do about all this mathematics for urban planning?" ([0:56:17–0:56:22]). The Belgian doctorate also required an "annex thesis, which is a development on another topic" ([0:56:08–0:56:12]).
- **Evolution and exit** [stated, ASR small]: "the focus on mathematical traffic assignment, essentially disappeared. There were all the questions about choice modeling, behavioral studies, surveys" ([0:56:56–0:57:13]). "we all group [our group] run the first survey, the first national Belgian mobility survey" ([0:57:13–0:57:20]). The line was "close to optimization and to diverge rather far away" ([0:57:27–0:57:29], garbled). In his university, "people think of me as being the transportation guy, not at all the optimization guy" ([0:57:55–0:58:02]).
- **Record** [practice]: Namur 0 (1975); EU DRIVE (1991); MEUSE (*Transp. Res. B* 1995, DOI 10.1016/0191-2615(94)00025-u); logit (1997); mobility books (2002, 2003); mixed logit (2006–10); synthetic population (2013); last paper found, *JASSS* 2015 (DOI 10.18564/jasss.2819); last PhD 2014 (R2, R29, R30, R5).
- **[inferred]** The transport line ended at his retirement. No decision to leave is stated anywhere. His homepage still lists transport among his interests (R1).

### Side line: derivative-free optimization (1994–2022)

- **Record** [practice]: DFO project from 1994-03 (R6); survey with Conn and Scheinberg 1997 (DOI 10.1007/BF02614326); Colson (2003) and Tröltzsch (2011) theses; BFO (2017; DOI 10.1145/3085592); algorithm tuning with profiles (DOI 10.1145/3310362); structure in DFO (2022; DOI 10.1145/3474054).
- **Trigger**: not stated in anything I read. The Conn memoir says only "We continued to collaborate after that for some years, in particular with Katya Scheinberg on the topic of derivative-free optimization" (R11 p. 9). This team has a separate dfo-team for that tradition (team.json).

---

## 4. Entry and exit timing, summarised

| Topic | Field-level anchor (dated) | Toint's entry | Lag | Exit | Before or after consensus [inferred] |
|---|---|---|---|---|---|
| Sparse quasi-Newton | Competing Dennis student at the same time (podcast) | 1977 | ~0 | Folded into partial separability (1982) | Frontier; beat a rival to the result |
| Partial separability | His own idea with Griewank | 1982 | — | Never; recurs to 2026 | Created it |
| Bound/AL trust region + LANCELOT | Trust region, Powell 1970 (his account) | 1986 (Grenoble) / 1988 (papers) | ~16 years after the TR idea; first for large-scale bound + general constraints | Book 2000; "for some years" after | Early for large-scale NLP software ("maybe the first", together with MINOS) |
| Test environment | Paper exchange of problems | 1983 (own set), 1987 (call), 1995 (CUTE) | — | Still maintaining (S2MPJ 2026) | Created the consensus benchmark |
| Non-monotone | (not dated in sources read) | 1994–97 solo | — | Filter work | Not determinable |
| Filter | Fletcher, May 1996 | 1998 report, 2002 papers | ~2 years | 2007 (V&N history); 2016 tribute | Early. Theory for a new idea |
| Multilevel TR | — | 2005–08 with Gratton | — | The cohort's last paper is Gratton, Malmedy & Toint, "Quasi-Newton updates with weighted secant equations", *OMS* 30 (2015; online 2014), DOI 10.1080/10556788.2014.971025. The idea reappears as multilevel OFFO (2023) and recursive AdaGrad (2025) | Not determinable |
| Nonconvex complexity | Nesterov–Polyak 2006 | Sep 2007 | ~1 year | 2022 book, 2023 ICM chapter; sharpness notes to 2026 | Before the "buzzword" phase, in his own account |
| OFFO / Adagrad / Adam | Adagrad, Adam "very popular" (his 2022 text) | Mar 2022 | Years behind ML practice | Ongoing | After the ML consensus; early in NLP theory |
| Muon | (Muon's own date not checked in this run) | Apr 2026 title | — | Ongoing | Fast follower |
| Shampoo | — | Apr 2026 (v1 title and abstract) | — | **Dropped by v3, Aug 2026** | Withdrawn inside 4 months; reason not stated |
| Transport | — | 1975 | — | c. 2015 | Local, application-driven |

---

## 5. Failures, abandoned directions and narrowed claims (trajectory view)

These are additions to `01-publications.md` §3 and `02-methodology.md` §8 (R37, R38), which list the corrigenda (the trust funnel 2008 → erratum 2011/12, DOI 10.1007/s10107-011-0491-x; the constrained-complexity corrigendum, DOI 10.1007/s10107-016-1016-4) and the stated self-criticisms.

| Item | Evidence | Trajectory reading |
|---|---|---|
| **Shampoo removed** from arXiv:2604.17423 | v1 (19 Apr 2026) title "…AdaGrad, Shampoo and Muo[n]" and abstract "adaptive variants of Shampoo and Muon". v3 (27 Aug 2026): "an adaptive variant of Muon" (R19). The Namur portal and two 2026 talk titles still carry "Shampoo" (R6). The Optimization Online title has also dropped it (R33) | A claim narrowed four months after posting. The reason is **not stated**. The most recent visible retreat |
| **SQP not chosen** (1977) | "I did the wrong choice" ([0:15:47], medium); "the method I failed to be associated with" ([0:50:19–0:50:22], small) | A self-described road not taken. Said as a joke, twice in one interview |
| **Transport line faded** | §3 side line | Left by drift; the end coincides with retirement |
| **Filter left as proof object** | No new filter paper after 2007 (Crossref and his list); 2025–26 constrained methods avoid filters by design | A quiet exit; the design goal survives |
| **"Nonlinear stepsize control" unification** (solo, 2013) | Asked for in 2008: "Meaningful numerical evaluation still needed" (R26 p. 36). No numerical follow-up found (also R37) | Left open |
| **Unregularised Newton as a complexity-competitive method** | "A big surprise" (R27 p. 21); DOI 10.1137/090774100 | His own group's example closed that path. It reopened in 2023–26 with Newton variants that reach near-optimal complexity (arXiv:2302.10065; arXiv:2505.04807 → *EJCO* 2026, DOI 10.1016/j.ejco.2026.100128) |
| **Fortran infrastructure** | Stated decline of Fortran; no Toint commits in ralna repos | Handed over; he rebuilt the collection in other languages |
| **ICML 2020 listing** | On his list; not found in PMLR vol. 119 (R34) | Unverifiable. Possibly a workshop paper (inferred) |
| **Homepage frozen** | Talks list ends in 2021; journal list ends in 2023; reports end in 2024 (R1–R3) | The public CV lags the activity. Use the Namur portal, arXiv and git for recent work |
| Rejected papers, abandoned projects in his own words | none found | Gap |

---

## 6. Era and resource context by phase

| Phase | Seniority and admin load | Team | Compute, tools and distribution | Funding named in sources |
|---|---|---|---|---|
| 1974–78 | Teaching assistant, "half-time research" | Callier locally; Powell in Cambridge | Siemens 4004; "large" = 50 variables; problems on paper | Royal Society grant (R12) |
| 1979–86 | Lecturer; co-director of the Numerical Analysis Unit; director of the transport group | Griewank; first students | Harwell Subroutine Library routines; Fortran | not stated |
| 1986–2000 | Associate professor (1987), full professor (1993); head of computer services 1998–2000 | CGT, three countries | Vector machines (1988); Fortran; anonymous ftp (CUTE abstract, R37); letters and email | Namur project for the TR book 1997–2000 (R37, not re-read) |
| 2000–2010 | Department director 2006–09 | Fletcher–Leyffer; Namur cohort of about 10 juniors (R39); Gratton | GALAHAD Fortran 90/95; CUTEr; performance profiles | EPSRC fellowships 2002, 2003, 2009; EPSRC GR/S42170; STAE Foundation (ADTAO) |
| 2010–2016 | MOS chair 2010–13; vice-rector (in office Feb 2015) | Cartis–Gould; Florence; Toulouse | Pen-and-paper theory; small CUTEr/CUTEst tests | Leverhulme / Balliol 2015 |
| 2016–2026 | Emeritus: "No longer meetings, no faculty meetings … essentially a lot of freedom for doing what I like, which is very often research" ([0:58:31–0:58:46], small) | Gratton (almost all papers), Florence, Toulouse juniors | arXiv-first from 2017; GitHub (S2MPJ, 2024–); Matlab/Python/Julia; one workstation ("Dell Precision computer with 64 GiB of memory", R22 p. 21) | CIMI chair 2016–18; ANITI (ANR-19-PI3A-0004, via Gratton) |

[inferred] **The research questions follow the tools and the problem sizes of each era.** Fifty variables and paper problems led to sparsity. Vector machines and ftp led to LANCELOT/CUTE. Mature software and test sets made the question "why does unsafeguarded Newton work?" possible, which led to filters. Nesterov–Polyak's theory led to complexity. ML noise, and the funding to work on it, led to OFFO. Any method taken from him should keep the era qualifier.

---

## 7. The last 12 months (2025-09-28 → 2026-09-28), dated

[practice, P unless marked. Sources: arXiv abstract pages and submission histories (R19); Crossref (R29); Namur portal activity entries (R6, titles and dates only, no venues); S2MPJ git history (R31); podcast (R10); Optimization Online (R33)]

| Date | Item |
|---|---|
| 2025-09-29 | Online: Gratton, Jerad & Toint, "Complexity and performance for two classes of noise-tolerant first-order algorithms", *OMS* 40 (2025), DOI 10.1080/10556788.2025.2532736 (arXiv:2203.01757). |
| 2025-10-06 | Online: Toint (solo), "Examples of slow convergence for adaptive regularization optimization methods are not isolated", *Math. Prog.*, DOI 10.1007/s10107-025-02286-1. |
| 2025-10-08, 10-31 | S2MPJ commits: range constraints, infinite ranges, tar files. |
| 2025-10-18 | arXiv:2510.16390, Gratton & Toint, "A Simple First-Order Algorithm for Full-Rank Equality Constrained Optimization" (v2 2026-03-10). First OFFO paper with constraints. |
| 2025-11 | Print: Gratton, Sim & Toint, "Refining asymptotic complexity bounds …", *COAP* 92 (2025), DOI 10.1007/s10589-025-00709-5. |
| 2026-01 | Print: Porcelli, Seraghiti & Toint, "prunAdag: an adaptive pruning-aware gradient method", *COAP* 93 (2026), DOI 10.1007/s10589-025-00723-7. |
| Jan 2026 (→ 9 Jan) | Invited talk "Stochastic ADAGRAD with bounds, curvature (and problem structure)" (Namur portal; venue not shown). |
| 2026-01-22 | arXiv:2601.15970, Gratton & Toint, DCA iteration complexity, "a simple proof". Published in *Optimization Letters* 2026-07-20, DOI 10.1007/s11590-026-02327-4. |
| 2026-02-08 | S2MPJ commit: "coorection [sic] for Python 3.14 + hand-coded HS problems". |
| 2026-02-12 | arXiv:2602.11770, Bellavia, Gratton, Morini & Toint, "An objective-function-free algorithm for general smooth constrained optimization". |
| 2026-02-13 → 02-21 | Visiting researcher at ANITI, Toulouse (Namur portal). |
| 2026-02-17 | arXiv:2505.04807 v2 (fast Newton under local Lipschitz smoothness). Published in *EJCO* 14 (2026), DOI 10.1016/j.ejco.2026.100128. |
| 2026-03 | Print: Gratton, Jerad & Toint, "Complexity of a class of first-order objective-function-free optimization algorithms", *OMS* 41 (2026), DOI 10.1080/10556788.2023.2296431 (online 2024-02-08). |
| 2026-03-31 | arXiv:2603.29685, Gratton & Toint, OFFO for stochastic objectives with deterministic constraints. |
| 2026-04-14 | Invited talk "Deterministic and stochastic optimization without evaluating the objective function" (Namur portal; venue not shown). |
| 2026-04-19 | arXiv:2604.17423 v1: unified theory for adaptive first-order methods, "including AdaNorm, full and diagonal AdaGrad, Shampoo and Muon". v2 2026-05-01. v3 2026-08-27 drops Shampoo (§5). |
| 2026-05 | *JOTA* 209 (2026): Bellavia, Gratton, Morini & Toint, "An Optimally Fast Objective-Function-Free Minimization Algorithm Using Random Subspaces", DOI 10.1007/s10957-026-03004-3. |
| 2026-06-01 | arXiv:2606.01787, Gratton & Toint, "Stochastic convergence of parallel asynchronous adaptive first-order methods": "Numerical experiments suggest that such asynchronous adaptive algorithms are very relevant in heterogeneous large-scale machine learning systems." |
| 2026-06-04; 06-26 → 07-01 | Two invited talks on the unified-theory paper, still under its v1 title with "Shampoo" (Namur portal; venues not shown; WebSearch 2 found none). |
| 2026-06-11 | arXiv:2505.06374 v2 (ADAGB2, stochastic second-order Adagrad with bounds). |
| 2026-07-27 | Podcast interview "Subject to: Philippe Toint" (host Anand Subramanian), 1:11:05. His plans: "as long as I can continue to be curious and as long as other people are willing to talk to me and possibly work with me, I'm happy to share" ([1:09:16], medium). |
| 2026-08-24 | S2MPJ commit "adding LICENCE file". |

**Reading of the last 12 months** [inferred]. The output rate is steady: five new arXiv papers in 2026 up to June, plus revisions. He works on three fronts at once:
- OFFO with constraints (three papers);
- adaptive and ML optimizers (unified theory with Muon; asynchronous methods; Adagrad with bounds);
- sharpness and simplicity notes (DCA "simple proof"; slow examples).

He also maintains S2MPJ himself. Gratton is a co-author of all five 2026 preprints; the Florence group (Bellavia, Morini) of one. No new CGT or Cartis paper appears.

---

## 8. Hypotheses for the synthesis stage (inferred; the "how he turns" craft)

1. **Enter where theory is missing on a new, practical idea, and enter fast.** Filter (1996 → 1998) and cubic regularization (2006 → 2007) were both entered by asking "can this be proved under weaker, practical assumptions, and does it work on CUTEr?" (R13, R23).
2. **Enter where a fashion leaves a gap.** Nonconvex complexity while complexity was a "buzzword … for the convex case" (R10). Deterministic OFFO as a "stepping stone" while ML practice ran ahead of theory (R21).
3. **Build the instrument when the work needs it, then keep it alive when its language dies.** CUTE for LANCELOT (1995), then S2MPJ once Fortran declined (2024) (R10, R22, R31).
4. **Carry the machinery forward.** Each era reuses the previous one: trust region → filter trust region → multilevel trust region → ARC → OFFO-ARC → Adagrad with constraints. Each new setting is entered with the old toolkit, and the old question ("safeguard as little as possible") is re-asked.
5. **Leave quietly and keep the goal.** No exit statements. Topics fade (transport, filter, CGT), while the design aims persist.
6. **Turns come with people and money.** The turns are tied to a meeting (Powell 1975; Conn and Gould 1979/84/86), a partner's funding call (STAE/ADTAO), or an institute (ANITI). A skill that suggests "ideas to improve our solver" in his voice should ask: which partner, which test set, which funding horizon?

---

## Contradictions (kept, not reconciled)

- **C1. When the CGT collaboration started.** Written in 2019: met 1979, second visit 1984, "collaboration got truly going only in 1986, when Andy, on sabbatical in Grenoble" (R11 p. 9). Spoken in 2026: "a few years later, I think it was in 81, Andy went for a sabbatical in France in Grenoble" ([0:39:16–0:39:25]; both ASR models give 81) (R10). The first CGT papers appear in 1988 (R29).
- **C2. LANCELOT's date.** "the publication, in 1991, of the LANCELOT package (and associated theory) and the first CUTE collection" (R11). The Springer book is 1992 (DOI 10.1007/978-3-662-12211-2) and CUTE is in *ACM TOMS* in 1995 (R29). Report 91/10 "A comprehensive description of LANCELOT" is 1991 (R2). This may be release vs publication; not resolved.
- **C3. What came first with Gratton.** Toint (ASR): "The first thing I did with him, he was mostly doing data simulation [assimilation] at the time. And I joined him on a project like that." (R10). In Crossref the earliest joint journal papers are multilevel trust regions (*SIOPT* Jan 2008; *IMA JNA* 2008) and inverse scattering (2009). The data-assimilation papers are later (*SIMAX* 2011; *QJRMS* 2013) (R30). The ADTAO slides (June 2010) describe the data-assimilation project as recent and still running (R25).
- **C4. The length of the Cambridge stay.** Host: "a little over six months" ([0:20:13–0:20:22]). Toint: "I spent a year in Cambridge for my thesis" ([0:14:35–0:14:40], small). Memoir: arrived January 1977 (R12).
- **C5. Employment title.** ORCID: "Full Professor", 1974-09-15 → 2016-08-31 (R4). Edinburgh and Imperial bios: lecturer 1979, associate professor 1987, full professor 1993 (R8, R9). The podcast: hired "as a teaching assistant" on graduation (R10).
- **C6. MOS chair dates.** Homepage: 2010–2013 (R1). Podcast host: "from 2010 to 2012" (intro [0:01:12–0:01:15]) and "between 2010 and 2013" ([0:51:30–0:51:35]) (R10). The Edinburgh and Imperial bios say 2010–2013.
- **C7. The Namur research portal reflects the tool it uses.** It shows an ORCID link on "sandbox.orcid.org" and the headline "8992 Citations / 45 h-index" (Scopus-based) (R6). OpenAlex gives 17,686 citations and h = 57 (R40). Not reconciled; the counts are relative only.
- **C8. The ICM chapters.** ICM 2018: pages 3711–3750 in Crossref vs "vol.4, pp. 3729-3768" on his list. ICM 2022: his list gives "Strong Evaluation Complexity Bounds for Arbitrary-Order Optimization of Nonconvex Nonsmooth Composite Functions … ICM 2022, St Petersburg", while Crossref gives "The evaluation complexity of finding high-order minimizers of nonconvex optimization", DOI 10.4171/icm2022/95 (R2, R29).
- **C9. ICML 2020.** Listed as ICML proceedings on his list (R2). Not present in the PMLR vol. 119 index (R34).
- **C10. The title of the unified-theory paper.** The Namur portal (output and two talk entries) keeps "Shampoo" (R6). arXiv v3 and Optimization Online have dropped it (R19, R33).
- **C11. When the transport career started.** Host: "from 1979 to 2016" ([0:55:50–0:56:01]). Edinburgh: director of the group "since 1979" (R8). Toint: "from the very days of my thesis" ([0:56:02]), and report 75/8 "Namur 0" is dated 1975 (R2).
- **C12. Pride in the book vs its size.** 2019: the book's "sheer size" is evidence of commitment (R11). 2026: "In retrospect, I'm not so sure this is such a great idea to have such a massive book" ([0:48:27], medium) (R10). The same doubt is voiced about the 2022 book ([1:02:45–1:02:53]). (Also recorded by agent 02 as C3/F11.)

---

## Gaps

- **Namur portal sub-pages returned 403** (prizes (12), activities (356), projects (67), supervised work (92)) with both curl and WebFetch (R7). So there is **no complete prize list** (the 12 prizes), **no venues for the 2026 talks**, and no re-check of the 1997–2000 book project (taken from R37).
- **Vice-rector dates**: only "currently serves" in February 2015 (R9) and "Past vice-rector" on the homepage (R1). Start and end years were not found.
- **The origin of the Griewank collaboration**, the São Paulo (Birgin–Martínez) and Hong Kong (X. Chen) collaborations, and the DFO start (1994): no stated trigger found.
- **Why he stopped transport work and why the CGT line stopped after 2022**: no statement found. Both are recorded as drift.
- **Why Shampoo was dropped** (arXiv:2604.17423 v1 → v3): not stated anywhere I read. The v3 PDF was not read. Checking its text or comments would be the next step.
- **The multilevel turn's trigger** (c. 2003–05): no first-hand account found.
- **Texts not read**: *Optima* 88 (2012), "How much patience do you have?", which is the likeliest stated origin story for the complexity turn (R37 reports a 404). The 1987 *IMANA Newsletter* call. The prefaces of the 2000 and 2022 books. The 2023 corrigendum. arXiv:2302.07049v1 was downloaded but not read.
- **Rejected papers, abandoned projects in his own words, referee exchanges**: none found.
- **MOS and SIAM prize pages** are rendered with JavaScript (R36). The Lagrange Prize was verified through *Optima* 73 instead. The Beale–Orchard-Hays 1994 prize rests on ORCID, the Namur portal and Edinburgh (all self-reported or institutional), not on the MOS page.
- **DBLP** was not queried by me (agent 01 did; R37).
- **GitHub**: only S2MPJ was inspected. OPM and BFO repositories were not found or checked. The ralna repositories may not carry pre-GitHub authors.
- **The podcast** is unchecked ASR. Quotes from the small model only (most of the transport and Gratton passages) should be re-checked against the audio before being used verbatim.

---

## Sources

P = primary (Toint's own words or record); S = secondary. "Read" means read in this run by this agent unless marked otherwise.

- R1. Ph. Toint, home page, accessed 2026-09-28, https://perso.unamur.be/~phtoint/toint.html (P; read)
- R2. Ph. Toint, "Publications of Ph. Toint" (books, articles to 2023, reports to 2024), accessed 2026-09-28, https://perso.unamur.be/~phtoint/publications.html (P; read: book, early-article, early-report and recent sections)
- R3. Ph. Toint, "Talks by Ph. Toint" (2000–2021), accessed 2026-09-28, https://perso.unamur.be/~phtoint/talks.html (P; read 2011–2021 part)
- R4. ORCID public record 0000-0002-6166-1860 (educations, employments, distinctions, invited positions), via https://pub.orcid.org/v3.0/0000-0002-6166-1860/activities, 2026-09-28 (P, self-curated; read)
- R5. Mathematics Genealogy Project, "Philippe Louis Toint", id 87096, https://www.mathgenealogy.org/id.php?id=87096 (S; read)
- R6. University of Namur Research Portal, "Philippe Toint" person page (degrees, master's thesis, projects excerpt, prizes excerpt, 2025–26 outputs and activities), https://researchportal.unamur.be/en/persons/phtoint (S, institutional; read)
- R7. Namur portal sub-pages /prizes/, /activities/, /projects/ (HTTP 403 via curl and WebFetch), 2026-09-28 (not read)
- R8. University of Edinburgh staff news, "Honorary Professor: Philippe L Toint" (2010 appointment), https://www.ed.ac.uk/news/staff/appointments-awards/2010/philippe-toint-070510 (S; read)
- R9. Imperial College London event page, seminar "Worst-case complexity of nonlinear optimization: Where do we stand?", 11 Feb 2015, speaker biography, https://www.imperial.ac.uk/events/105173/ (S; the live URL loops on redirects; read from the copy saved by agent 02 in this run at /tmp/nonlinear-team-scratch/base-skills/philippe-l-toint/imp.html)
- R10. "Subject to: Philippe Toint", podcast, host Anand Subramanian, 2026-07-27, https://podcasters.spotify.com/pod/show/subject-to/episodes/Subject-to-Philippe-Toint-e3mjb27; ASR transcript `../sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt` (P, machine transcript; read in full)
- R11. Ph. L. Toint (postscript N. Gould), "In Memoriam Andrew Conn (1946–2019)", *SIAG/OPT Views and News* 27(2), 2019, pp. 9–10, https://siagoptimization.github.io/assets/views/ViewsAndNews-27-2.pdf (P; read)
- R12. M. Buhmann, R. Fletcher, A. Iserles & P. Toint, "Michael J. D. Powell. 29 July 1936—19 April 2015", *Biogr. Mems Fell. R. Soc.* 64 (2018) 341–366, DOI 10.1098/rsbm.2017.0023; preprint https://perso.unamur.be/~phtoint/pubs/Powell.pdf (P, co-authored; p. 14 read)
- R13. R. Fletcher, S. Leyffer & Ph. Toint, "A Brief History of Filter Methods", *SIAG/OPT Views-and-News* 18(1), March 2007, pp. 2–12, https://siagoptimization.github.io/assets/views/18-1.pdf (P, co-authored; pp. 3–5 read)
- R14. *Optima* 73 (Mathematical Programming Society newsletter), January 2007, "The Lagrange Prize" citation, p. 5, https://mathopt.zib.de/Optima-Issues/optima73.pdf (S; read)
- R15. SIAM press release, "SIAM Awards Lagrange Prize to Roger Fletcher, Sven Leyffer and Philippe L. Toint", 18 Jul 2006, https://www.eurekalert.org/news-releases/491180 (S; curl 403; read as a WebFetch summary only, so not quoted verbatim)
- R16. WebSearch 1, "SIAM Lagrange Prize Continuous Optimization 2006 Fletcher Leyffer Toint filter paper citation", 2026-09-28 (search record; led to R14, R15)
- R17. WebSearch 2, "Philippe Toint 2026 invited talk "unified convergence theory" …", 2026-09-28 (search record; no talk venue found)
- R18. arXiv author search "Toint", 53 results, ordered by date, https://arxiv.org/search/?query=Toint&searchtype=author (P records; read)
- R19. arXiv abstract pages and submission histories: 2606.01787, 2604.17423 (v1 and current), 2603.29685, 2602.11770, 2601.15970, 2510.16390, 2507.11513, 2505.06374, 2505.04807, 2502.08308, 2409.16047, 2408.09124, 2407.07812, 2308.00720, 2302.07049, 2203.09947v1, 2203.01647v1, 2112.05636, 1812.03467, https://arxiv.org/abs/<id> (P; read)
- R20. S. Gratton, S. Jerad & Ph. L. Toint, "Parametric complexity analysis for a class of first-order Adagrad-like algorithms", arXiv:2203.01647v1, 3 Mar 2022 (published as DOI 10.1080/10556788.2023.2296431) (P; pp. 1–2 read)
- R21. S. Gratton, S. Jerad & Ph. L. Toint, "Convergence properties of an Objective-Function-Free Optimization regularization algorithm, including an O(ε^-3/2) complexity bound", arXiv:2203.09947v1, 18 Mar 2022 (published as DOI 10.1137/22M1499522) (P; pp. 1–2 read)
- R22. S. Gratton & Ph. L. Toint, "S2MPJ and CUTEst optimization problems for Matlab, Python and Julia", arXiv:2407.07812v1, 10 Jul 2024; *OMS* 40 (2025), DOI 10.1080/10556788.2025.2490640 (P; pp. 1–2 and 20–21 read)
- R23. C. Cartis, N. I. M. Gould & Ph. L. Toint, "Adaptive cubic overestimation methods for unconstrained optimization. Part I", report TR07-05a (29 Sep 2007), https://perso.unamur.be/~phtoint/pubs/TR07-05a.pdf; published as DOI 10.1007/s10107-009-0286-5 (P; pp. 1–4 read)
- R24. C. Cartis, N. I. M. Gould & Ph. L. Toint, "On the complexity of steepest descent, Newton's and regularized Newton's methods …", report 09/14 (15 Oct 2009), https://perso.unamur.be/~phtoint/pubs/TR09-14.pdf; DOI 10.1137/090774100 (P; pp. 1–4 read)
- R25. Ph. Toint, "Le point de vue d'un expert extérieur du projet ADTAO" (slides), Toulouse, June 2010, https://perso.unamur.be/~phtoint/talks/2010_toulouse.pdf (P; all 10 pages read)
- R26. Ph. Toint, "Nonlinear stepsize control, Trust-Region and Regularization Algorithms for Unconstrained Optimization" (slides), Veszprém, Dec 2008, https://perso.unamur.be/~phtoint/talks/2008_veszprem.pdf (P; pp. 1, 6, 36 read)
- R27. Ph. Toint (with C. Cartis and N. Gould), "A (quick) overview of some complexity issues for nonconvex optimization" (slides), NAXYS Opening Day, Namur, Oct 2010, https://perso.unamur.be/~phtoint/talks/2010_naxys.pdf (P; pp. 1, 21 read)
- R28. Ph. Toint, "Filter methods: a tribute to Roger Fletcher" (slides), ICNAAO Beijing, Aug 2016, https://perso.unamur.be/~phtoint/talks/2016_beijing_for_roger.pdf (P; pp. 6, 21, 28 read)
- R29. Crossref REST API metadata for about 85 DOIs cited here, https://api.crossref.org/works/<doi>, 2026-09-28 (S, metadata)
- R30. Crossref author and bibliographic searches (Gratton–Toint, Cartis–Toint, Gould–Toint, Bellavia–Toint, Porcelli–Toint, transport and economics venues, individual titles), 2026-09-28 (S, metadata)
- R31. Git history of S2MPJ (GrattonToint/S2MPJ; blob-less clone, 134 commits, 2024-05-31 → 2026-08-24), https://github.com/GrattonToint/S2MPJ (P, practice)
- R32. Git histories of ralna/CUTEst, ralna/SIFDecode, ralna/GALAHAD (blob-less bare clones; author search for "Toint" returned 0), https://github.com/ralna (S; others' repositories)
- R33. Optimization Online, author page "Philippe L. Toint" (10 most recent postings, 2024-09 → 2026-06, with update dates), https://optimization-online.org/author/philippe-toint/ (P records; read)
- R34. Proceedings of Machine Learning Research, vol. 119 (ICML 2020) index, https://proceedings.mlr.press/v119/ (S; searched for "Toint" and "Bellavia", no hit)
- R35. theses.fr API records 2011INPT0031 (Tröltzsch), 2013INPT0040 (Gürol), 2024TLSEP024 (Jerad; jury and reviewers), https://theses.fr/api/v1/theses/these/<id> (S; JSON saved by agent 04 in this run, read by me)
- R36. Mathematical Optimization Society prize and officer pages, https://www.mathopt.org/?nav=lagrange etc. (JavaScript-rendered, no content; not read)
- R37. Research note `01-publications.md`, research agent 01, 2026-09-28 (repository cross-reference; used for the 1997–2000 book project, report 98/13 and the "11 of 12" co-author count)
- R38. Research note `02-methodology.md`, research agent 02, 2026-09-28 (repository cross-reference; P7, F11, C3)
- R39. Research note `04-mentorship.md`, research agent 04, 2026-09-28 (repository cross-reference; student roster, cohort practices, M6)
- R40. OpenAlex landscape, author A5002913605, `../sources/publications/publications.md`, 2026-09-28 (S; citation and h-index counts)
