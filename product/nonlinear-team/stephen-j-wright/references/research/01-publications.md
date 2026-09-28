# 01 · Publications: Landscape and Signature-Work Anatomy (Stephen J. Wright)

> **Researcher:** Stephen J. Wright (UW-Madison Computer Sciences; Argonne MCS 1990–2001), living.
> **Dimension:** research agent 01 of 06, signature works and the publication landscape (nuwa research-craft Phase 1).
> **Research date:** 2026-09-28. **Sources consulted:** 34 (22 primary). **WebSearch calls:** 2.
> **Local corpus:** `references/sources/{papers,talks,essays,software}` held only `.gitkeep` files. There was no user-supplied material, so nothing below is marked "from user-supplied material".
> **How items were checked:** every paper below carries a DOI, an arXiv id, or venue + year + full title that I checked this run against DBLP (SPARQL, pid `w/StephenJWright`), Crossref, OpenAlex (API key set; author `A5046109083`), arXiv listing/abstract pages, or Wright's own papers page. Quotations come from full texts or slides I downloaded and read this run (page = PDF page of the file named in Sources), or from the UW-Madison oral-history transcript (locator = speaker-turn timestamp).
> **Tags:** [stated] = Wright said it; [practice] = what his papers, code and records show he did; [observed] = what others (prize committees, institutions) said; [inferred] = my inference, not in any source. Every item is also labelled primary (P) or secondary (S).

---

## 0. Data coverage and caveats

| Source | What it gave | Caveat |
|---|---|---|
| DBLP pid `w/StephenJWright` (SPARQL) | 227 records, 1987–2026: 104 articles, 59 in proceedings, 60 CoRR preprints, 3 books, 1 chapter | Under-covers work before 1990 (2 records) and the control, stochastic-programming and statistics papers. A **second DBLP profile, `75/2677` "Stephen Wright"**, mixes some of his papers (1997 SIMAX augmented-system paper; 2022–2024 bilevel, squentropy, operator-inference and behavior-cloning papers) with other people's work (Event-B, epistemology, optical fibre). [practice, S] |
| OpenAlex author `A5046109083` (`../sources/publications/publications.md`) | 341 works, 27,184 citations, h = 62 | **Contaminated and incomplete.** It lists "current institution: Ames Research Center" and assigns to him a 2026 Mars-helicopter airfoil paper, a 1982 outfall-diffuser paper and a 1977 *Amer. Math. Monthly* note, all by other people. It leaves out *Numerical Optimization* (1999 ed. 9,520 cites; 2006 ed. 9,050 cites under DOIs 10.1007/b98874 and 10.1007/978-0-387-40065-5), so its "Top 25" misses his most-cited work. Counts below are OpenAlex values from 2026-09-28 and are useful only for comparing works with each other. [practice, S] |
| Google Scholar (`VFQRIOwAAAAJ`) | **not read** | WebFetch was redirected to the Google "sorry" captcha page on both attempts. No Scholar counts are used anywhere in this note. |
| Wright's papers page `pages.cs.wisc.edu/~swright/papers/` | His own annotated list for 1992–2011, with preprint numbers (ANL/MCS-P###), talks and books | Flagged "(needs updating!)" on his homepage. It stops around 2011. [practice, P] |
| Homepages (old UW page; `wrightstephen.github.io/sw_proj/`) | Bio, awards, his own choice of "Past Research Projects", books and software | The GitHub page is the current one (© 2025, teaching Spring 2026). [stated, P] |

---

## 1. Publication landscape

### 1.1 Topics by five-year period

Representative works only. Each one was checked this run.

| Period (role, place) | Main lines [practice, P unless marked] | Representative works (identifiers) |
|---|---|---|
| **1984–1989** (PhD 1984 Univ. of Queensland; U. Arizona; NC State math 1986–90) | Composite nonsmooth optimization; SQP-like and projected-Hessian quasi-Newton convergence for NLP; inexact Levenberg–Marquardt; QP on the Alliant FX/8 vector multiprocessor | Wright & Holt, J. Austral. Math. Soc. B 1985, 10.1017/S0334270000004604; IMA J. Numer. Anal. 1986, 10.1093/imanum/6.4.463; Math. Program. 1987, 10.1007/BF02591697; Ann. Oper. Res. 1988, 10.1007/BF02186482; Math. Program. 1989, 10.1007/BF01587090; SIAM J. Control Optim. 1989 "Convergence of SQP-Like Methods for Constrained Optimization", 10.1137/0327002 |
| **1990–1994** (Argonne MCS from 1990) | Parallel algorithms for boundary-value ODEs and banded systems; discrete-time optimal control (partitioned DP, IPMs for control); first interior-point work; infeasible-IPMs for LCP; identifiable surfaces; software surveying | Wright & Pereyra SISC 1990, 10.1137/0911025; SIOPT 1991 "Partitioned Dynamic Programming for Optimal Control", 10.1137/0801037; Kelley & Wright MP 1991, 10.1007/BF01586941; SIOPT 1992 "An Interior-Point Algorithm for Linearly Constrained Optimization", 10.1137/0802023; SISC 1993 "A Collection of Problems for Which Gaussian Elimination with Partial Pivoting is Unstable", 10.1137/0914013; JOTA 1993 "Interior point methods for optimal control of discrete time systems", 10.1007/BF00940784; SICON 1993 "Identifiable Surfaces in Constrained Optimization", 10.1137/0331048; Moré & Wright *Optimization Software Guide*, SIAM 1993, 10.1137/1.9781611970951; MP 1994 infeasible-IPM for LCP, 10.1007/BF01582211 |
| **1995–1999** | Superlinear and superquadratic IPMs under degeneracy (with Monteiro, Ralph, Zhang); numerical stability of IPM linear algebra; the monograph; PCx; stabilized SQP; IPMs for model predictive control; *Numerical Optimization* 1st ed.; NEOS Guide | Monteiro & Wright COAP 1994, 10.1007/BF01300971; SIMAX 1995, 10.1137/S0895479893260498; Wright & Ralph MOR 1996, 10.1287/moor.21.4.815; Wright & Zhang MP 1996, 10.1007/BF02592215; SIMAX 1997 "Stability of Augmented System Factorizations in Interior-Point Methods", 10.1137/S0895479894271093; *Primal-Dual Interior-Point Methods*, SIAM 1997, 10.1137/1.9781611971453; COAP 1998 stabilized SQP, 10.1023/A:1018665102534; Rao, Wright & Rawlings JOTA 1998, 10.1023/A:1021711402723; SIOPT 1999 modified Cholesky, 10.1137/S1052623496304712; Czyzyk, Mehrotra, Wagner & Wright "PCx: an interior-point code for linear programming", OMS 1999, 10.1080/10556789908805757; Nocedal & Wright *Numerical Optimization*, Springer 1999, 10.1007/b98874; Czyzyk, Wisniewski & Wright SIAM Rev. 1999, 10.1137/S0036144598334874 |
| **2000–2004** (UChicago adjunct 2000–01; UW-Madison from 2001) | Degenerate NLP (SQP and barrier); finite-precision behavior of IPMs; warm-starting IPMs; OOQP; grid computing for stochastic programming; nonlinear MPC via feasible SQP; MPECs | Potra & Wright JCAM 2000, 10.1016/S0377-0427(00)00433-7; Ralph & Wright MOR 2000, 10.1287/moor.25.2.179.12227; SIOPT 2001 finite precision, 10.1137/S1052623498347438 (arXiv math/0103102); MP 2001 Newton/log-barrier, 10.1007/PL00011421; SIOPT 2002 "Modifying SQP for Degenerate Problems", 10.1137/S1052623498333731; Wright & Orban MOR 2002, 10.1287/moor.27.3.585.312; Vicente & Wright COAP 2002, 10.1023/A:1019798502851; Yıldırım & Wright SIOPT 2002, 10.1137/S1052623400369235; MP 2003 constraint identification, 10.1007/s10107-002-0344-8 (arXiv math/0012209); Gertz & Wright ACM TOMS 2003 (OOQP), 10.1145/641876.641880; Linderoth & Wright COAP 2003, 10.1023/A:1021858008222; Wright & Tenny SIOPT 2004, 10.1137/S1052623402413227; Tenny, Wright & Rawlings COAP 2004, 10.1023/B:COAP.0000018880.63497.EB; Ralph & Wright OMS 2004, 10.1080/10556780410001709439 |
| **2005–2009** | End of the degenerate-NLP line; distributed MPC (with Rawlings's group); stochastic programming sampling; radiotherapy; **turn to sparse optimization and compressed sensing**; statistics/ML collaborations; *Numerical Optimization* 2nd ed.; *Linear Programming with MATLAB* | SIOPT 2005 degenerate NLP, 10.1137/030601235; Oberlin & Wright SIOPT 2006, 10.1137/050626776; Linderoth, Shapiro & Wright Ann. OR 2006, 10.1007/s10479-006-6169-8; Nocedal & Wright 2nd ed. 2006, 10.1007/978-0-387-40065-5; Anitescu, Tseng & Wright MP 2007, 10.1007/s10107-006-0005-4; Ferris, Mangasarian & Wright SIAM 2007, 10.1137/1.9780898718775; Figueiredo, Nowak & Wright JSTSP 2007 (GPSR), 10.1109/JSTSP.2007.910281; Venkat, Hiskens, Rawlings & Wright TCST 2008, 10.1109/TCST.2008.919414; Oberlin & Wright MP 2009, 10.1007/s10107-007-0173-x; Wright, Nowak & Figueiredo TSP 2009 (SpaRSA), 10.1109/TSP.2009.2016892 |
| **2010–2014** | Sparse and regularized optimization; identification of active manifolds (Lewis); **Hogwild!** and asynchronous parallel methods with UW systems colleagues; block/stochastic coordinate descent; subspace tracking; LP rounding at scale | Tropp & Wright Proc. IEEE 2010, 10.1109/JPROC.2010.2044010; Zhu, Wright & Chan COAP 2010, 10.1007/s10589-008-9225-2; Lewis & Wright SIOPT 2011 "Identifying Activity", 10.1137/090747117; Niu, Recht, Ré & Wright arXiv:1106.5730 (NIPS 2011 pp. 693–701); SIOPT 2012 "Accelerated Block-coordinate Relaxation for Regularized Optimization", 10.1137/100808563; Lee & Wright JMLR 2012 "Manifold Identification in Dual Averaging for Regularized Stochastic Online Learning" (13:1705–1744); Uhler & Wright SIAM Rev. 2013, 10.1137/120872309; Liu & Wright ACHA 2014 "Robust dequantized compressive sensing", 10.1016/j.acha.2013.12.006 |
| **2015–2019** | Coordinate-descent theory (survey, async, random permutations); **second-order complexity for nonconvex smooth problems**; accelerated methods near saddles; control-theoretic (IQC/SDP) analysis of first-order methods; multiscale PDE sampling (with Qin Li, Jianfeng Lu) | "Coordinate descent algorithms" MP 2015, 10.1007/s10107-015-0892-3 (arXiv:1502.04759); Liu & Wright SIOPT 2015, 10.1137/140961134; Liu, Wright, Ré, Bittorf & Sridhar JMLR 2015 (16:285–322); Lewis & Wright MP 2016, 10.1007/s10107-015-0943-9; Liu & Wright Math. Comp. 2016, 10.1090/mcom/2971; Royer & Wright SIOPT 2018, 10.1137/17M1134329 (arXiv:1706.03131); Hu, Wright & Lessard ICML 2018 (arXiv:1806.03677); O'Neill & Wright MP 2019, 10.1007/s10107-018-1340-y; Lee & Wright ICML 2019 "First-Order Algorithms Converge Faster than O(1/k) on Convex Problems" (arXiv:1812.08485) |
| **2020–2024** (IFDS site director; Khachiyan Prize 2020; NAE and Dantzig Prize 2024; CS chair 2023–25) | Newton-CG complexity extended to trust regions, bounds, equality constraints and inexact Hessians; squared-variable reformulations; single-loop stochastic NLP; min-max; differential privacy; Langevin MC and mean-field NN analysis; bilevel; the data-analysis textbook | Royer, O'Neill & Wright MP 2020, 10.1007/s10107-019-01362-7 (arXiv:1803.02924); O'Neill & Wright IMA JNA 2020, 10.1093/imanum/drz074 (arXiv:1904.03563); Wright & Lee Math. Comp. 2020, 10.1090/mcom/3530; Gürbüzbalaban, Ozdaglar, Vanli & Wright MP 2020, 10.1007/s10107-019-01438-4; Curtis, Robinson, Royer & Wright SIOPT 2021, 10.1137/19M130563X (arXiv:1912.04365); Xie & Wright J. Sci. Comput. 2021, 10.1007/s10915-021-01409-y (arXiv:1908.00131); Ding, Li, Lu & Wright COLT 2021 (arXiv:2010.01405); Yao, Xu, Roosta, Wright & Mahoney IMA JNA 2022, 10.1093/imanum/drac043 (arXiv:2109.14016); Wright & Recht *Optimization for Data Analysis*, CUP 2022, 10.1017/9781009004282; Kwon, Kwon, Wright & Nowak ICML 2023 (arXiv:2301.10945); Xie & Wright MP 2024, 10.1007/s10107-023-02000-z (arXiv:2103.15989); Alacaoglu & Wright AISTATS 2024 (arXiv:2311.00678); Lowy, Ullman & Wright ICML 2024 (arXiv:2402.11173) |
| **2025–2026** (Vilas Research Professor 2025–; ICM plenary 2026 listed on homepage) | Theory-versus-practice essay; a return to **degenerate superlinear convergence** (proximal Newton); squared variables for nonlinear SDP; Hessian-aware gradient scaling; weaker variance assumptions; diffusion models; offline RL with MPC | Wright arXiv:2510.15734 "Optimization in Theory and Practice"; Ding & Wright SIOPT 2025, 10.1137/23M1608343 (arXiv:2310.01784); Ding & Wright arXiv:2502.02099; Li & Wright JOTA 2025, 10.1007/s10957-025-02817-y (arXiv:2310.18841); Smee, Roosta & Wright arXiv:2502.03701; Alacaoglu, Malitsky & Wright arXiv:2504.09951; Lee & Wright arXiv:2602.10470; Zhou, Zhang & Wright arXiv:2601.19285 (CVPR 2026 per DBLP); Deb, Wright & Banerjee arXiv:2603.22430 |

**Reading of the table** [inferred]:
- The **nonlinear-programming core** (SQP, barrier and IPM, degeneracy, active-set identification) runs unbroken from 1986 to 2006.
- It comes back after 2017 as **worst-case complexity** of Newton-type methods, and in 2026 as a **degenerate superlinear-convergence** paper again (arXiv:2602.10470).
- Around this core, the application partner changes about once a decade: process control (1990s–2011), compressed sensing and signal processing (2006–2015), ML and parallel systems (2011–), scientific computing and PDEs (2019–).

### 1.2 Authorship position: solo theorist → PI of a group

DBLP, author-role records only (pid `w/StephenJWright`):

| Period | Records | Solo | First (multi-author) | Last | Middle | CoRR preprints |
|---|---|---|---|---|---|---|
| 1985–89 | 2 | 2 | 0 | 0 | 0 | 0 |
| 1990–94 | 10 | 7 | 1 | 2 | 0 | 0 |
| 1995–99 | 13 | 5 | 3 | 5 | 0 | 0 |
| 2000–04 | 22 | 6 | 2 | 12 | 2 | 0 |
| 2005–09 | 27 | 1 | 2 | 19 | 5 | 0 |
| 2010–14 | 39 | 4 | 1 | 20 | 14 | 10 |
| 2015–19 | 43 | 1 | 0 | 27 | 15 | 14 |
| 2020–24 | 60 | 0 | 1 | 48 | 11 | 30 |
| 2025–26 | 11 | 1 | 0 | 9 | 1 | 6 |

- **Solo work dominates to about 2004** [practice, P]. Almost all the degenerate-NLP and IPM-stability papers are single-authored. After 2005 the solo items are a survey (*Coordinate descent algorithms*, 2015), one algorithm paper (SIOPT 2012) and the 2025 essay. His research voice moves from single-author proofs to surveys, books and group papers.
- **Caveat: "last author" is a weak signal here** [inferred from practice]. Optimization often orders authors alphabetically, and "Wright" sorts near the end. In DBLP, 22 of 42 multi-author papers in the 2000s, 39 of 77 in the 2010s and 40 of 70 in the 2020s are in alphabetical order. The informative cases are:
  - **non-alphabetical last positions**: 9 in the 2000s, 8 in the 2010s, 17 in the 2020s. Examples are O'Neill & Wright, Lee & Wright, Xie & Wright, Li & Wright, and Deb, Wright & Banerjee. These mark a senior or advisor role.
  - **non-alphabetical first positions**: Wright & Pereyra 1990, Wright & Ralph 1996, Wright & Zhang 1996, Wright & Jarre 1999, Wright & Orban 2002, Wright & Tenny 2004, Wright–Nowak–Figueiredo 2008/2009, and Wright & Lee 2020. These mark papers he drove.
- **Preprint culture changes** [practice, P]:
  - Argonne preprint series ANL/MCS-P### in the 1990s (P643, P699, P865, …), all listed on his papers page with revision dates.
  - UW Optimization Technical Reports (e.g. uwopt-0101, uwopt-0201).
  - arXiv from 2000 (math/0012209, math/0103102), then routinely from about 2011. 60 of 227 DBLP records are CoRR.

### 1.3 Collaboration network and likely students

Co-author counts from DBLP (`w/StephenJWright`), with OpenAlex where DBLP under-covers.

| Cluster | Main co-authors (DBLP count; OpenAlex count in brackets) | Years | Nature [inferred unless noted] |
|---|---|---|---|
| IPM and complementarity theory | Renato D. C. Monteiro (3), Daniel Ralph (3), Yin Zhang, Florian Jarre, Florian Potra, Dominique Orban, Luís N. Vicente, E. Alper Yıldırım | 1994–2003 | Peer theorists. Visitors and postdocs of the Argonne era. |
| Argonne / OTC software and NEOS | Joseph Czyzyk, Sanjay Mehrotra, Michael Wagner, Jorge J. Moré, E. Michael Gertz, Jorge Nocedal (book; [9] in OpenAlex, 2006–08) | 1993–2009 | Lab software team. Oral history: "I had several postdocs, and students work on it [PCx]" [stated, P] |
| Process control (UW Chem. & Biol. Eng., TWCCC) | James B. Rawlings (12; [24] 1997–2021), Gabriele Pannocchia (5), Aswin N. Venkat (5), Matthew J. Tenny, C. V. Rao, Brett T. Stewart | 1997–2021 | Long applied partnership. Oral history: joint projects with Rawlings from Argonne days, visiting Madison "about twice a year from about 1995 onwards" [stated, P] |
| UW optimization colleagues | Michael C. Ferris (5), Jeff T. Linderoth (3), Stephen M. Robinson (3), Olvi Mangasarian (book), James Luedtke | 2001–2021 | Departmental peers |
| Sparse / signal processing | Robert D. Nowak (8), Mário A. T. Figueiredo (3), Joel A. Tropp, Laura Balzano (7), Nikhil Rao (4), Parikshit Shah (4), Rebecca Willett (5) | 2007–2024 | Entered through a UW ECE colleague (Nowak) [stated, P, oral history 24:55] |
| ML and parallel systems | Benjamin Recht [11 OpenAlex], Christopher Ré (6), Feng Niu, Victor Bittorf (4), Ji Liu (8), Srikrishna Sridhar (6), Xiaojin Zhu (3), Grace Wahba [7 OpenAlex], Dimitris Papailiopoulos | 2005–2019 | UW CS/Stats peers plus students |
| Nonconvex and NLP complexity | Clément W. Royer, Michael O'Neill, Frank E. Curtis, Daniel P. Robinson, Yue Xie, Fred Roosta, Michael W. Mahoney, Shuyao Li, Ahmet Alacaoglu (6), Jelena Diakonikolas (8) | 2017–2026 | Postdocs and students plus Lehigh peers |
| Applied math / multiscale PDE / sampling | Qin Li (23), Jianfeng Lu (11), Shi Chen (11), Zhiyan Ding (9), Ke Chen (7), Karen Willcox | 2018–2025 | Peer collaboration (Li at UW Math) plus their students |
| Variational analysis | Adrian S. Lewis | 2008–2016 | Peer |

**Overlap with the Nonlinear Team** [practice, P]: Jorge Nocedal (the textbook, 1999 and 2006; Fisher, Nocedal, Trémolet & Wright, Optim. Eng. 2009 "Data assimilation in weather forecasting: a case study in PDE-constrained optimization", 10.1007/s11081-008-9051-5); Frank E. Curtis (SIOPT 2021, above). No co-authored record with Ye, Wächter, Gill, Toint, Gould, Fletcher or Nesterov was found in DBLP (either pid) or in the 341 OpenAlex works. As a 2002 talk reports, Wright follows IPOPT, KNITRO, LOQO and the Wächter–Biegler example closely (§2.1).

**Likely students and postdocs** [inferred from author order, affiliation lines in papers read, and years; Agents 04 and 06 must verify]:
- **Students or advisees**: Christina Oberlin (2006, 2009), Arinbjörn Ólafsson (2005–06), Sangkyun Lee (2009–12), Ji Liu (2012–16), Srikrishna Sridhar (2012–14), Taedong Kim (2015–18), Cong Han Lim (2014–21), Ching-pei Lee (2017–2026), Michael O'Neill (2019–23; UW CS e-mail on arXiv:1803.02924), Changyu Gao (2023–24), Shuyao Li (2023–25).
- **Co-supervised with Rawlings**: Matthew J. Tenny, Aswin N. Venkat.
- **Postdocs**: Clément W. Royer (Wisconsin Institute for Discovery affiliation on arXiv:1706.03131, p. 1), Yue Xie, Ahmet Alacaoglu, Nam Ho-Nguyen.
- Recruitment route [stated, P]: "So the students that I've recruited have typically come from graduate classes" (oral history, turn at 35:54).

### 1.4 Usual venues and dissemination

- **Core optimization journals** [practice, P]: Math. Program. (20 DBLP), SIAM J. Optim. (16), Comput. Optim. Appl. (7), JOTA, MOR, OMS, IMA J. Numer. Anal., SIMAX/SISC. The early 1990s also include SIAM J. Sci. Comput. and Parallel Computing (parallel ODE/linear algebra).
- **ML venues from about 2007** [practice, P]: ICML (12), AISTATS (7), NIPS/NeurIPS (7), JMLR (5), KDD, COLT, UAI, AAAI, CVPR (2026).
- **Application venues follow the partner** [practice, P]: IEEE TSP/JSTSP/ICASSP/Proc. IEEE (signal processing); IEEE TAC, Automatica, TCST, Syst. Control Lett., J. Process Control, AIChE J. (control); Phys. Med. Biol. (radiotherapy); Bioinformatics, PNAS, JAMIA (bio/health).
- **Books, software and web services** [practice, P]:
  - Five books: 1993, 1997, 1999/2006, 2007, 2022.
  - Public software: PCx (LP), OOQP (convex QP), GPSR and SpaRSA (sparse reconstruction), GPU SpaRSA, TV denoising, LPS (regularized logistic regression). All are listed on his homepage.
  - "Interior-Point Methods Online, an older archive of interior-point papers and stuff, which I maintained starting in 1994, in the early days of the Web" [stated, P, GitHub homepage].
  - NEOS Guide case studies (SIAM Rev. 1999).
  - Typo and correction lists kept for every book (homepage).

### 1.5 Most-cited works

OpenAlex, 2026-09-28. Scholar counts were not read.

| Work | OpenAlex cites | Note |
|---|---|---|
| Nocedal & Wright, *Numerical Optimization* (1999, 10.1007/b98874; 2006, 10.1007/978-0-387-40065-5) | 9,520 + 9,050 | Not linked to his OpenAlex author id |
| Figueiredo, Nowak & Wright, GPSR, JSTSP 2007 | 3,572 | |
| *Primal-Dual Interior-Point Methods*, SIAM 1997 | 2,415 | His most-cited solo work |
| Wright, Nowak & Figueiredo, SpaRSA, TSP 2009 | 1,925 | |
| "Coordinate descent algorithms", MP 2015 | 1,499 | Solo survey |
| Hogwild!, arXiv:1106.5730 / NIPS 2011 | 1,206 + 1,090 | Split record. NeurIPS Test of Time Award 2020 [stated, P, homepage] |
| Tropp & Wright, Proc. IEEE 2010 | 1,058 | |
| Venkat et al., distributed MPC, TCST 2008 | 822 | |
| Potra & Wright, "Interior-point methods", JCAM 2000 | 740 | |
| Rao, Wright & Rawlings, JOTA 1998 | 542 | |
| Gertz & Wright, OOQP, ACM TOMS 2003 | 258 | |
| Yıldırım & Wright, warm-start IPM, SIOPT 2002 | 160 | |
| Stabilized SQP, COAP 1998 / Modifying SQP, SIOPT 2002 / degenerate NLP, SIOPT 2005 | 123 / 76 / 60 | The NLP-degeneracy line is cited far less than the rest |
| Royer & Wright SIOPT 2018 / Royer, O'Neill & Wright MP 2020 | 85 / 76 | Curtis et al. SIOPT 2021 shows 2 (plus 30 on the arXiv record): a split record |

**Pattern** [inferred]:
- Citation mass sits in **books, surveys and short, free software-backed algorithms** (GPSR, SpaRSA, Hogwild!).
- The deepest NLP theory (degeneracy, stability) is **low-citation**, even though it is the part most relevant to NLP solver design.

### 1.6 Recent work (about the last 12 months) and live threads

| Date | Work | Thread [inferred] |
|---|---|---|
| 2025-08 | Li & Wright, JOTA 2025, 10.1007/s10957-025-02817-y | Complexity with inexact function, gradient and Hessian evaluations |
| 2025-10 | Ding & Wright, SIOPT 2025, 10.1137/23M1608343 | Reformulation: squared slacks turn inequalities into equalities, with second-order correspondence and complexity |
| 2025-10 / v2 2025-12 | Wright, arXiv:2510.15734 | Solo essay on theory vs practice (LP and smooth unconstrained) |
| 2025-10 | Hellmuth, Jin, Li & Wright, arXiv:2510.01567 | Randomized linear algebra and data selection for PDE inverse problems |
| 2026-01 | Zhou, Zhang & Wright, arXiv:2601.19285 (CVPR 2026) | Optimization lens on diffusion-model generalization |
| 2026-02 | Lee & Wright, arXiv:2602.10470 "Revisiting Superlinear Convergence of Proximal Newton-Like Methods to Degenerate Solutions" | **Return to the 1998–2006 degeneracy theme.** Hölderian error bound, a Jacobian that is only uniformly continuous, a globalization that "avoids the Maratos effect" (abstract) |
| 2026-03 | Deb, Wright & Banerjee, arXiv:2603.22430 | MPC ideas used in offline RL. The DBLP title is "Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning"; the current arXiv title is "Inference Time Policy Optimization for Offline RL with Differentiable World Models" |
| 2026-07 (rev.) | Alacaoglu, Malitsky & Wright, arXiv:2504.09951 | Weaker variance assumptions for SGD-type methods |

### 1.7 What Wright himself puts forward

- **Homepage** [stated, P]: "I am the author or coauthor of widely used text/reference books in optimization, including 'Primal Dual Interior-Point Methods' (SIAM, 1997) and 'Numerical Optimization' (2nd Edition, Springer, 2006, with J. Nocedal). I have published widely on optimization theory, algorithms, software and applications. I am also the coauthor of widely used software for linear and quadratic programming and compressed sensing." (wrightstephen.github.io/sw_proj/, "About").
  - "Some Past Research Projects" on the old UW homepage lists only software: PCx, OOQP, GPSR, SpaRSA, GPU codes, TV denoising, LPS.
- **Oral history (UW-Madison Oral History Program, interview of 2022-10-04)** [stated, P]. Asked about his projects, he chose PCx, OOQP and GPSR/SpaRSA and said of the last two papers: "those papers, the two papers that we wrote in those areas are very highly cited, and they won some major awards." (turn at 12:25). He names three routes to impact:
  - influence on other researchers, "particularly if you, if you do something that someone hasn't really done before, that hasn't really been appreciated before. And people recognize it as being an important direction." (turn at 21:25);
  - software;
  - books, where "I really enjoy this process of sort of distilling knowledge in a particular area, and sort of digesting it, and figuring out how to present it to people who are just coming into the area" (same turn).
  - Students are a fourth.
- **2025 essay** [stated, P]. When he needs his own examples, it cites *Primal-Dual Interior-Point Methods* [107], *Numerical Optimization* [80], SpaRSA [108], Hogwild! [79], *Optimization for Data Analysis* [109], the Newton-CG complexity papers [89, 24], Hu–Wright–Lessard [49], Lee & Wright [63] and O'Neill & Wright [81] (arXiv:2510.15734v2, reference list).

---

## 2. Signature works: anatomy

Selection logic:
- **S1** and **S3** are the most-cited works he authored (the textbook with Nocedal is more cited, but its preface was not read, so it is not dissected).
- **S1, S3 and S4** are also the works he himself foregrounds (§1.7).
- **S2** is the core of his NLP-solver theory and is relevant to this team.
- **S3, S4 and S5** are turning points: to sparse optimization (2007), to ML and parallel methods (2011), and back to Newton-type NLP through complexity (2017).

### S1 · *Primal-Dual Interior-Point Methods* (SIAM 1997, 10.1137/1.9781611971453) and PCx (Czyzyk, Mehrotra, Wagner & Wright, OMS 1999, 10.1080/10556789908805757)

| Dimension | Finding |
|---|---|
| **Origin** | [stated, P] PCx "grew out of my research and interior point methods". Interior-point methods "are relatively, they're simpler than simplex methods are easier to write software for. And so we sat down and wrote our own package in the mid 90s, and released it in 1997 as PCX." (oral history, turn at 9:02). [practice, P] The book was preceded by a run of solo and joint infeasible-IPM papers: OMS 1993 (10.1080/10556789308805537), MP 1994, MOR 1996, MP 1996, COAP 1994, SIMAX 1995. [observed, S] UW CS news (2024-07-22): "His key contributions to interior-point methods culminated in an influential SIAM monograph on the subject in 1997." A search-engine summary of the 2024 Dantzig Prize citation says he "pioneered infeasible interior point methods". The full citation page (mathopt.org, JavaScript) was **not read verbatim**. The preface of the book was **not read** (SIAM returned 403). |
| **Why then** | [stated, P] He had time because the Argonne post had no teaching: "I sort of had time because I wasn't teaching I had time to do things like write books, you know, that, that university people have a lot of trouble finding time for." (oral history, turn at 6:36). [stated, P] In 2002 he described the field as having "moved beyond the 'frenetic' stage into a phase of consolidation and maturity" (talk "The Ongoing Impact of Interior-Point Methods", slide 2). In 2025 he dated the end of the "classical" IPM period to the mid-1990s (arXiv:2510.15734v2, p. 10). [inferred] The book appeared right at the point of consolidation, after Mehrotra's predictor-corrector had become the practical standard and before IPMs moved on to NLP. |
| **Key insight** | [stated, P, 2025 retrospective] Treat LP optimality as a mildly nonlinear system and apply modified Newton steps along the central path. The long-step path-following bound "requires only elementary mathematics and can be proved from scratch in a single lecture of a graduate-level optimization course (see [107, pp. 96–100])" (arXiv:2510.15734v2, p. 10; [107] = the book). |
| **Minimum evidence** | [practice, P] Complexity results for infeasible and superlinear variants in the 1993–1996 papers, together with an implementation that could be tested on netlib (PCx). The PCx paper itself was **not read**. |
| **Abandoned paths** | [stated, P, 2025] The theory-optimal variants lost in practice: "the most successful practical primal-dual approach is closest to the methods with O(n²log ϵ) complexity; methods with the slightly better O(n^1/2 log ϵ) bound are somewhat slower in practice." (arXiv:2510.15734v2, p. 9). [stated, P] PCx's licensing model did not work: for commercial use "you had to apply to Argonne for a license. And turned out very few people did that" (oral history, turn at 9:02). He also recounts, as hearsay he heard in 2016, that Google's founders used PCx early on. This is **unverified**. |
| **Reception** | [practice, S] 2,415 OpenAlex citations. He keeps a "somewhat dated list of corrections" (homepage). [observed, S] The 2024 Dantzig Prize news items single out the monograph. |
| **Method it shows** [inferred] | Consolidate a maturing method class into (i) a proof you can teach in a lecture, (ii) a public code, and (iii) a book. The theory is judged by whether it tracks the heuristics that actually win (Mehrotra), not by the best bound. |

### S2 · Degeneracy-robust local convergence for SQP and IPMs (1998–2006, revisited 2026)

Core papers:
- "Superlinear Convergence of a Stabilized SQP Method to a Degenerate Solution", COAP 1998, 10.1023/A:1018665102534;
- "Modifying SQP for Degenerate Problems", SIOPT 2002, 10.1137/S1052623498333731;
- "Constraint identification and algorithm stabilization for degenerate nonlinear programs", MP 2003, 10.1007/s10107-002-0344-8;
- "An Algorithm for Degenerate Nonlinear Programming with Rapid Local Convergence", SIOPT 2005, 10.1137/030601235;
- Oberlin & Wright, "Active Set Identification in Nonlinear Programming", SIOPT 2006, 10.1137/050626776;
- companions: Wright & Orban MOR 2002; Vicente & Wright COAP 2002; Mostafa, Vicente & Wright COCOS 2003 (10.1007/978-3-540-39901-8_10); SIOPT 2001 (finite precision); Lee & Wright arXiv:2602.10470 (2026).

| Dimension | Finding |
|---|---|
| **Origin** | [stated, P] "We showed in [18] that even when strict complementarity, second-order sufficient conditions, and a constraint qualification hold, nonuniqueness of the optimal multiplier can produce nonsuperlinear behavior of SQP. Motivated by this observation and by the fact that primal-dual interior-point algorithms for related problems converge superlinearly under the conditions just described [20, 16], we proposed a stabilized SQP (sSQP) method [18]" (P699 preprint of SIOPT 2002, p. 1). Also: "Motivation for the sSQP approach came from work on primal-dual interior-point algorithms described in [20,13]." (P865 preprint of MP 2003, p. 2). The idea came **across from his own degenerate-LCP interior-point results** (Monteiro–Wright, Ralph–Wright) into SQP. |
| **Why then** | [practice, P] He had just proved IPM superlinear convergence despite dependent constraints (Ralph & Wright, MOR 2000; preprint 1996) and for degenerate LCP (1994–96). [inferred] Degenerate problems such as MPECs were becoming central in the late 1990s. His own MPEC papers followed (Ralph & Wright OMS 2004; Anitescu, Tseng & Wright MP 2007). |
| **Key insight** | [stated, P] "a slight modification of the well-known sequential quadratic programming method for nonlinear programming that attains superlinear convergence to a primal-dual solution even when the Jacobian of the active constraints is rank deficient at the solution. We show that rapid convergence occurs even in the presence of the roundoff errors" (COAP 1998 preprint P643, abstract, p. 1). In 2003 the key step was separating **weakly from strongly active constraints** with a sequence of LP subproblems (P865, p. 2). |
| **Minimum evidence** | [practice, P] "a simple example" showing that plain SQP loses superlinear convergence (P643, p. 1). This came first; the local analysis, including a floating-point analysis, followed. The same pattern appears in 2001 (finite-precision IPMs for NLP) and in the 2002 talk (numerical stability "until µ≈√u", slide 55). |
| **Abandoned paths / admitted limits** | [stated, P] 1998: the result needed an identification-adjustment step and a start "sufficiently interior": "Still, it would be more satisfactory to know that the algorithm exhibited the desired behavior without this identification adjustment step." (P643, p. 18). The 2003 paper says it drops "the assumption of strict complementarity and a 'sufficiently interior' starting point made in [18]" (P865, p. 2). 2002: exact Hessians only. For quasi-Newton, "Extension of the analysis to this case would, however, not be trivial ... so we leave this issue for possible future work" (P699, p. 2). [inferred] I found no later quasi-Newton degenerate-SQP paper by him in DBLP or OpenAlex, so this looks abandoned. 2002 also sets globalization aside: "we focus on the local properties of the SQP approach and ignore the various algorithmic devices used to ensure global convergence" (P699, p. 2). |
| **Practice → theory** | [stated, P] "Implementations of SQP (for example, SNOPT [10]) often continue to exhibit good local convergence behavior even on degenerate problems ... The iSQP framework proves to be useful in providing some theoretical support for this good practical performance. We find that the strategy of using the active (or working) set from the QP subproblem at the previous iteration as the initial active set for the current iteration is important in explaining the good behavior, as is the fact that the solver of the QP subproblem is allowed to return a slightly infeasible answer." (P699, pp. 1–2). |
| **Reception** | [practice, S] Modest citations (123 / 76 / 39 / 60 / 41 in OpenAlex). [observed, P] Hager's variant and Fischer's alternative appear inside his own papers. He treats these as parallel lines and says his local superlinear result was "later enhanced by Hager [11]" (P699, p. 1; the PDF breaks "en-hanced" across a line). [practice, P] The theme comes back 28 years later in Lee & Wright arXiv:2602.10470: degenerate solutions, Hölderian error bounds, no Maratos effect. |
| **Method it shows** [inferred] | Find a gap between what solvers do and what theory covers (degeneracy, finite precision). Build the smallest counterexample. Transplant a mechanism from a neighbouring class (IPM → SQP). Remove assumptions one paper at a time and state the remaining ones openly. |

### S3 · GPSR (Figueiredo, Nowak & Wright, IEEE JSTSP 2007, 10.1109/JSTSP.2007.910281) and SpaRSA (Wright, Nowak & Figueiredo, IEEE TSP 2009, 10.1109/TSP.2009.2016892)

| Dimension | Finding |
|---|---|
| **Origin** | [stated, P] "the compressed sensing work, which started around 2006 or so that's also tied to machine learning. And so I became a part of that I started collaborating with Professor Rob Nowak here at UW Madison." (oral history, turn at 24:55). "And then GPSR that grew out of my work with, with Rob Nowak, and Mario Fiegueredo, in about 2007, to 2010. And that was during this era, when people came up with this new problem called compressed sensing" (turn at 9:02; the transcript spells the name "Fiegueredo"). |
| **Why then** | [stated, P] Compressed sensing had just turned sparse recovery into large optimization problems. The 2008 NIPS workshop talk frames the change: "Traditionally, research on algorithmic optimization assumes exact data available and precise solutions needed. However, in many optimization applications we prefer simple, approximate solutions to more complicated exact solutions. ... These new 'ground rules' may change the algorithmic approach altogther. For example, an approximate first-order method applied to a nonsmooth formulation may be preferred to a second-order method applied to a smooth formulation." (sjw-nips.pdf, slide 4; the typo "altogther" is in the original). |
| **Key insight** | [practice, P] GPSR: split x into positive and negative parts, recast ℓ2–ℓ1 as a bound-constrained QP, and apply gradient projection with Barzilai–Borwein steps, continuation and debiasing (JSTSP 2007, pp. 586–588). SpaRSA generalizes this: each step solves "an optimization subproblem involving a quadratic term with diagonal Hessian (i.e., separable in the unknowns) plus the original sparsity-inducing regularizer" (TSP 2009, abstract, p. 2479). |
| **Minimum evidence** | [practice, P] Wall-clock comparisons on compressed-sensing, deconvolution and similar problems against IST and the interior-point code l1_ls: "often being significantly faster (in terms of computation time) than competing methods" (JSTSP 2007, abstract, p. 586). |
| **Abandoned paths** | [stated, P] The author of the IPM monograph set IPMs aside for this class. They cannot warm-start along a regularization path: "IP methods ... have been less successful in making effective use of warm-start information ... To benefit from a warm start, IP methods require the initial point to be not only close to the solution but also sufficiently interior to the feasible set and close to a 'central path,' which is difficult to satisfy in practice." (JSTSP 2007, p. 588). His own warm-start IPM work (Yıldırım & Wright 2002) is among the cited attempts. [stated, P] A known weakness was admitted in the abstract: "the performance of GP methods tends to degrade as the regularization term is de-emphasized"; continuation is the fix (p. 586). |
| **Reception** | [practice, S] 3,572 and 1,925 OpenAlex citations. [stated, P] "they won some major awards" (oral history, 12:25). His homepage lists the IEEE W. R. G. Baker Award, 2014, but **which paper won it was not verified**. [stated, P] The codes were given away: "we just made them freely available, because they were pretty short codes, you know, there's no point in trying to copyright them or anything." (9:02). Compare the PCx licensing experience (S1). |
| **Method it shows** [inferred] | Enter a new application area through a local domain partner. Reformulate the problem into a structure where a simple, old method (gradient projection, BB steps) is fast. Measure in wall-clock time against that field's standard codes. Release short free code. |

### S4 · Hogwild! (Niu, Recht, Ré & Wright, arXiv:1106.5730; NIPS 2011 pp. 693–701) and "Coordinate descent algorithms" (Math. Program. 151, 2015, 10.1007/s10107-015-0892-3; arXiv:1502.04759)

| Dimension | Finding |
|---|---|
| **Origin** | [stated, P] First contact with ML problems: during the 2000–01 UChicago adjunct year, an ML colleague brought him optimization problems, "and so that's where I sort of started becoming more interested 2000-2001." (oral history, 24:55). [stated, P] He admits the optimization community's blind spot on SGD: "optimizers knew about it, but didn't pay much attention to it. Because it's very slow, we thought it's very slow. But machine learning people found this was exactly the tool they needed" (24:55). Hogwild! is a UW collaboration with database and systems colleagues (Ré) and Recht [practice, P]. |
| **Why then** | [stated, P, paper] "the recent emergence of inexpensive multicore processors and mammoth, web-scale data sets has motivated researchers to develop several clever parallelization schemes for SGD" (Hogwild TR, p. 1). A single multicore workstation made locking the bottleneck (p. 2). [stated, P, CD survey] "The situation has changed in recent years. Various applications (including several in computational statistics and machine learning) have yielded problems for which CD approaches are competitive in performance with more reputable alternatives." (arXiv:1502.04759v1, p. 2). |
| **Key insight** | [stated, P] "when the data access is sparse, meaning that individual SGD steps only modify a small part of the decision variable, we show that memory overwrites are rare and that they introduce barely any error into the computation when they do occur." (Hogwild TR, p. 2). |
| **Minimum evidence** | [stated, P] "Hogwild! outperforms alternative schemes that use locking by an order of magnitude" (TR abstract, p. 1), backed by a near-optimal rate proof under sparsity. |
| **Abandoned paths** | Not documented (**not read**: no drafts or rejected versions found). [inferred] Locking and MapReduce designs are the foil the paper rejects (TR pp. 1–2). |
| **Reception** | [stated, P] NeurIPS Test of Time Award 2020 (homepage). [practice, S] About 2,300 OpenAlex citations across the split records. The CD survey has 1,499. |
| **Method it shows** [inferred] | Rehabilitate a method the community dismissed as unsophisticated once the application's "ground rules" and hardware change (cheap partial gradients, modest accuracy, sparsity, multicore), then supply the theory. His own framing of CD: "Paradoxically, the apparent lack of sophistication may also account for its unpopularity as a subject for investigation by optimization researchers, who have usually been quick to suggest alternative approaches in any given situation." (arXiv:1502.04759v1, p. 2) [stated, P]. The same move recurs in squared-variable formulations (2023–25): "algorithms built on these formulations are surprisingly competitive with standard methods" (arXiv:2310.01784 abstract). |

### S5 · Newton-CG with worst-case complexity guarantees (2017–2024)

Papers:
- Royer & Wright SIOPT 2018, 10.1137/17M1134329 (arXiv:1706.03131);
- Royer, O'Neill & Wright MP 2020, 10.1007/s10107-019-01362-7 (arXiv:1803.02924);
- Curtis, Robinson, Royer & Wright SIOPT 2021, 10.1137/19M130563X (arXiv:1912.04365);
- extensions: O'Neill & Wright IMA JNA 2020 (bounds, log-barrier); Xie & Wright J. Sci. Comput. 2021 (equality constraints, proximal AL); Yao et al. IMA JNA 2022 (inexact Hessians); Xie & Wright MP 2024 (projected Newton-CG); Ding & Wright SIOPT 2025 (squared variables reduce inequalities to equalities for complexity).

| Dimension | Finding |
|---|---|
| **Origin** | [stated, P] "with the recent upsurge of interest in complexity, several new algorithms have been proposed that have good global complexity guarantees. ... In most cases, these new methods depart significantly from those seen in the traditional optimization literature, and there are questions surrounding their practical appeal. Our aim in this paper is to develop a method that hews closely to the Newton-CG approach, but which comes equipped with certain safeguards and enhancements that allow worst-case complexity results to be proved." (arXiv:1803.02924v4, p. 2). |
| **Why then** | [stated, P] "There has been much recent interest in finding unconstrained local minima of smooth functions, due in part of the prevalence of such problems in machine learning and robust statistics." (arXiv:1706.03131v2, p. 1). [practice, P] Resource context: "Part of this work was done while the second author was visiting the Simons Institute for the Theory of Computing" (same, p. 1). Later papers acknowledge funding from the DARPA Lagrange program and Argonne subcontracts. |
| **Key insight** | [stated, P] 2018: "it is based on line searches only ... Second, its analysis is rather straightforward, relying for the most part on the standard technique for demonstrating sufficient decrease in the objective from backtracking." (arXiv:1706.03131v2, abstract). 2020: solve "a slightly damped version of the Newton equations" by CG while "monitoring the CG iterations for evidence of indefiniteness" (arXiv:1803.02924v4, p. 2). 2021 (with Curtis): "by making fairly minor modifications to such an algorithm, we can equip it with strong theoretical complexity properties without significantly degrading important performance measures" (arXiv:1912.04365v3, p. 2). |
| **Minimum evidence** | [practice, P] Complexity bounds that match the best known second-order rates. In 2021, "numerical comparisons on a standard benchmark test set" (arXiv:1912.04365v3, abstract). |
| **Abandoned paths / self-assessment** | [stated, P, 2025] Looking back on these same papers ([89] = Royer, O'Neill & Wright; [24] = Curtis et al.): "They are based on practical methods, but the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance." (arXiv:2510.15734v2, p. 23). |
| **Reception** | [practice, S] 85 and 76 OpenAlex citations. The 2021 paper's count is split between records. [practice, P] The program spread to bound, equality and inexact settings within 4 years, which shows a sustained agenda rather than a one-off. |
| **Method it shows** [inferred] | Take the method practitioners actually use (Newton-CG, trust-region Newton-CG) and add the smallest safeguards that make the fashionable guarantee provable. Check that practical behavior is not degraded. Later, say openly that the guarantee did not improve practice. |

### Candidate works not dissected (and why)

- **Nocedal & Wright, *Numerical Optimization*** (1999 and 2006): most cited. The prefaces were **not read**, because Springer answered with a cookie/authorization redirect. [stated, P, oral history 23:47]: it is "a textbook, but it's also a reference book. And it's used a lot by people in other areas."
- **Wright & Recht, *Optimization for Data Analysis*** (CUP 2022, 10.1017/9781009004282): the front matter did not load (Cambridge 503 / connection reset). **Not read.**
- **Rao, Wright & Rawlings (JOTA 1998)** and the control line: important for the IPM-for-MPC structure idea (JOTA 1993 onward). It belongs to the trajectory note (Agent 06).

---

## 3. Failures, abandoned directions, slow or missing publications

All items below are [practice, P] unless marked.

1. **Unpublished submission.** Lee & Wright, "Sparse nonlinear support vector machines via stochastic approximation", listed as "submitted, February 2010". The entry is now **commented out** in the HTML of his papers page, and I found no published record in DBLP or OpenAlex. The same page's link for "ASSET" points to a file named `sncss_tpami.pdf`. [inferred] The work was reworked as ASSET: arXiv:1111.0432, ICPRAM 2012, 10.5220/0003786202230228, a minor venue.
2. **Long road to print.** Lewis & Wright, "A proximal method for composite minimization": a technical report dated December 2008 on his papers page, published in *Math. Program.* 158 (2016), 10.1007/s10107-015-0943-9, about 7 years later. The reason is not documented.
3. **arXiv-only items** (no journal or conference version found in DBLP or OpenAlex): "Using Neural Networks to Detect Line Outages from PMU Data" (arXiv:1710.05916); "Convergence and Margin of Adversarial Training on Separable Data" (arXiv:1905.09209).
4. **Explicitly deferred extensions that did not follow.** Quasi-Newton degenerate SQP ("we leave this issue for possible future work", P699, p. 2). "Semi-local" convergence along a twisted central path: the 2002 talk asks "Can we get 'semi-local' convergence results that yield fast convergence beyond the final leg?" (slide 40). The talk bases this on his own runs of MOSEK and PCx on a twisted-path LP with presolve, scaling and crossover turned off (slides 36–39). I found no follow-up paper [inferred].
5. **Correction to a published proof.** Wright & Jarre, MP 1999 (10.1007/s101070050026): his papers page links a "Correction which fixes some typos and completes the proof of Theorem 2 in the published paper." [stated, P]
6. **Licensing failure.** PCx: commercial licences were almost never requested (S1). He later released GPSR/SpaRSA free (S3). [stated, P]
7. **Self-assessed limit of a research program.** The complexity-motivated Newton-CG modifications "do not improve the practical performance" (S5). [stated, P]
8. **Community blind spot he shared.** SGD dismissed as slow (S4). [stated, P]
9. **Rejections.** No public record found. Math-programming venues have no open review, so the absence of evidence says nothing.

---

## 4. Era and resource context

| Period | Context [tag] |
|---|---|
| 1984–1990 | Queensland PhD (1984, optimization); NC State math department teaching "two courses a semester" [stated, P, oral history 6:36]. Vector multiprocessors (Alliant FX/8, 1988) shaped the parallel-algorithm papers [practice, P]. |
| 1988–2001 | Argonne MCS (a one-year visit from 1988, permanent 1990–2001): a combined math and CS division, DOE-funded, no teaching, "good resources" [stated, P, 6:36]. Postdocs and students on PCx [stated, P, 9:02]. NEOS / Optimization Technology Center, and early-web distribution (IPM Online from 1994) [stated, P]. |
| 2001– | UW-Madison "cluster hire in computational science" [stated, P, 0:51]. Joint work across departments: ChemE (TWCCC consortium), ECE, Stats, DB/systems. From 2020, IFDS with "about 34-35 faculty members ... eight postdocs right now" (2022) [stated, P, 18:26]. Multicore workstations (Hogwild), GPUs (SpaRSA GPU, 2008 TR) [practice, P]. Grants from NSF, DOE, AFOSR, ONR and DARPA Lagrange, plus Argonne subcontracts (paper acknowledgments) [practice, P]. |
| Seniority | Editor-in-chief of SIAM J. Optim. (2014–2019) and Math. Program. Ser. B (2003–2007); MOS chair (2007–2010); CS department chair (2023–2025) [stated, P, GitHub homepage]. [inferred] From about 2005 most of the hands-on computing in his papers is done by students and postdocs. |

---

## 5. Cross-cutting patterns for Phase 2 (candidates, all [inferred] from §1–§3)

Each pattern cites the evidence it rests on. None has been through the four-way test yet.

1. **Theory must explain what good solvers already do.**
   - P699 explains SNOPT's local behavior through working-set warm starts and inexact QP solves.
   - The 2025 essay organizes the whole field around theory–practice gaps: "Are the loose bounds provided by the theory due to rare worst-case instances? Can we quantify the rarity of these instances?" (arXiv:2510.15734v2, p. 2).
   - The oral history repeats this: "Is it possible to give it a really bad problem that will confuse it and cause it to take a long time? And if that's the case, are these bad problems rare? Or are they common?" (turn at 40:30).
   - Evidence spans 2002, 2022 and 2025, in papers and speech.
2. **Carry a mechanism from one method class to another.** IPM degenerate-LCP results → stabilized SQP (S2). Squared variables ↔ primal-dual IPMs for LP (arXiv:2310.01784 abstract).
3. **Counterexample first, then relax assumptions paper by paper.** S2: 1998 → 2002 → 2003 → 2005 → 2006.
4. **Take finite precision and linear algebra seriously.** SIMAX 1995 and 1997, SIOPT 1999 and 2001, the 1998 sSQP roundoff analysis, and the 2002 talk: "robust, efficient linear algebra essential to practical effectiveness" (slide 52).
5. **Rehabilitate "unsophisticated" methods when the ground rules change.** Coordinate descent, SGD, gradient projection with BB steps, squared slacks (S3, S4, 2023–25).
6. **Keep the practical algorithm and add minimal safeguards for guarantees; then report honestly whether practice improved.** S5, including the 2025 self-assessment.
7. **Deliver results as code and books as well as papers.** PCx, OOQP, GPSR and SpaRSA, and five books. He names software and books among his measures of success (oral history, 21:25).
8. **Follow the application wave, about once a decade.** "In the in the 90s it was interior point methods in the 2000s or late 2000s, it was data science, where suddenly optimization, you know, had a paradigm shift." (oral history, turn at 57:24). On anticipating the next one: "you just want to kind of have an early warning system, keep your antennae out there and see, if something's interesting, something that tickles your interest happens, it might blow up into a major research topic." (turn at 58:55) [stated, P].

---

## Contradictions (kept, not reconciled)

1. **OpenAlex vs reality.** OpenAlex gives his institution as "Ames Research Center" and assigns him three other people's papers (1977, 1982, 2026). Its author profile also omits *Numerical Optimization*, his most-cited work. [practice, S]
2. **DBLP split.** Some of his papers sit under pid `75/2677` "Stephen Wright", mixed with other people's work. The 1997 SIMAX paper and the ICML 2023, NeurIPS 2022 and ICLR 2024 papers are missing from his main pid. [practice, S]
3. **Hogwild! author order.** The arXiv abstract and the UW technical report list Niu, Recht, Ré, Wright. The DBLP NIPS 2011 record lists Recht, Ré, Wright, Niu. The printed NIPS proceedings were not checked. [practice, S]
4. **Title drift.** arXiv:2603.22430 is titled "Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning" in DBLP but "Inference Time Policy Optimization for Offline RL with Differentiable World Models" on arXiv (latest version, May 2026). [practice, P/S]
5. **Practical cost of complexity safeguards.** In 2021 (Curtis et al.) the modifications come "without significantly degrading" performance and the method "retains the attractive practical behavior". In 2025 he writes they "do not improve the practical performance" and a "large gap" remains. These are not strictly inconsistent: no degradation is not the same as improvement. The emphasis, though, moves from confidence to reservation. [stated, P]
6. **View of SGD.** The 2011 Hogwild! paper praises SGD's "rapid learning rates" (TR, p. 1). In 2022 he recalls that optimizers had thought "it's very slow" (oral history, 24:55). This records a change of view over time, from the pre-2006 community view to the 2011 practice. [stated, P]
7. **Transcript accuracy.** The oral-history transcript misspells names ("Michael Farris" for Ferris, "Jim Rowlings" for Rawlings, "Mario Fiegueredo", "SPASA" for SpaRSA). Quotes above keep the transcript's words. Proper names were checked against DBLP. [practice, P]
8. **Career timeline wording.** The old homepage says he held positions at Arizona and NC State "before becoming a computer scientist at Argonne National Laboratory in 1990". The oral history adds a one-year Argonne position from a 1988 phone call. This is not a contradiction, but the two accounts differ in detail. [stated, P]

## Gaps

- **Google Scholar**: blocked (captcha) on both WebFetch attempts. No Scholar citation counts or ordering, and the complete harvest is left to the later T3.1 step.
- **Prefaces not read**: *Primal-Dual Interior-Point Methods* (SIAM 403), *Numerical Optimization* (Springer auth redirect), *Optimization for Data Analysis* (Cambridge 503 / reset). The origin stories of the books therefore rest on the oral history and inference.
- **Prize citations**: the full MOS/SIAM 2024 Dantzig citation (mathopt.org is JavaScript-only; SIAM returned 403) and the Khachiyan Prize 2020 citation text (INFORMS page lists winners only) were not read verbatim. Which paper won the IEEE W. R. G. Baker Award (2014) was not verified.
- **Genealogy**: the Math Genealogy query returned no parsable results. PhD advisor, thesis title and the full student list are **not verified** (for Agents 04 and 06). The "likely students" in §1.3 are inference only.
- **Software papers**: the PCx (OMS 1999) and OOQP (ACM TOMS 2003) papers were not read. There is no process evidence on the codes (for Agent 03). The GitHub API for user `wrightstephen` was not reachable from this session.
- **ICM 2026**: the homepage lists an "ICM Plenary Lecture, 2026". It was not confirmed whether arXiv:2510.15734 is the proceedings paper for it. The PDF footer carries a SIAM copyright template.
- **Rejections and reviews**: no public records exist for math-programming venues. §3 relies on indirect signals.
- **Semantic Scholar**: the author profiles are fragmented across at least 5 ids and were not used for counts.
- **Early work (1984–1989)**: only titles and identifiers. No full texts were read.

## Sources

1. Wright, S. J. Homepage (old), UW-Madison CS. https://pages.cs.wisc.edu/~swright/ (fetched 2026-09-28). Primary.
2. Wright, S. J. "Publications" (papers, talks, books), 1992–c.2011. https://pages.cs.wisc.edu/~swright/papers/ Primary.
3. Wright, S. J. Homepage (current). https://wrightstephen.github.io/sw_proj/ (© 2025). Primary.
4. DBLP, person `w/StephenJWright`, via `scripts/dblp_works.py` (sparql.dblp.org), 227 records. https://dblp.org/pid/w/StephenJWright.html Secondary.
5. DBLP, person `75/2677` "Stephen Wright" (mixed profile). https://dblp.org/pid/75/2677.html Secondary.
6. OpenAlex author A5046109083, via `scripts/fetch_publications.py` and the API (`../sources/publications/publications.md`). https://openalex.org/A5046109083 Secondary.
7. Crossref REST API, DOI metadata checks (books, PCx, early papers). https://api.crossref.org Secondary.
8. arXiv listing, search and abstract pages for Wright's arXiv ids (1106.5730, 1502.04759, 1706.03131, 1803.02924, 1904.03563, 1912.04365, 2109.14016, 2310.01784, 2311.00678, 2502.02099, 2502.03701, 2504.09951, 2510.15734, 2602.10470, 2603.22430, 2601.19285). https://arxiv.org Primary (metadata).
9. Semantic Scholar author search API (fragmented; not used for counts). https://api.semanticscholar.org Secondary.
10. Google Scholar profile VFQRIOwAAAAJ. https://scholar.google.com/citations?user=VFQRIOwAAAAJ **Not read (captcha).**
11. Wright, S. J. "Optimization in Theory and Practice", arXiv:2510.15734v2 (2 Dec 2025), 31 pp. Primary.
12. Wright, S. J. "Superlinear convergence of a stabilized SQP method to a degenerate solution", Preprint ANL/MCS-P643-0297 (1997); COAP 11 (1998), 10.1023/A:1018665102534. https://pages.cs.wisc.edu/~swright/papers/P643.pdf Primary.
13. Wright, S. J. "Modifying SQP for degenerate problems", Preprint ANL/MCS-P699-1097 (last modified 2002); SIOPT 13 (2002), 10.1137/S1052623498333731. https://pages.cs.wisc.edu/~swright/papers/P699_3.pdf Primary.
14. Wright, S. J. "Constraint identification and algorithm stabilization for degenerate nonlinear programs", preprint P865; MP 95 (2003), 10.1007/s10107-002-0344-8. https://pages.cs.wisc.edu/~swright/papers/P865_2.pdf Primary.
15. Figueiredo, Nowak & Wright, "Gradient Projection for Sparse Reconstruction ...", IEEE JSTSP 1 (2007), 10.1109/JSTSP.2007.910281. https://pages.cs.wisc.edu/~swright/papers/FigNW07a.pdf Primary.
16. Wright, Nowak & Figueiredo, "Sparse Reconstruction by Separable Approximation", IEEE TSP 57 (2009), 10.1109/TSP.2009.2016892. https://pages.cs.wisc.edu/~swright/papers/WriNF08.pdf Primary.
17. Niu, Recht, Ré & Wright, "Hogwild!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent", TR June 2011 / arXiv:1106.5730. https://pages.cs.wisc.edu/~swright/papers/hogwildTR.pdf Primary.
18. Wright, S. J. "Coordinate Descent Algorithms", arXiv:1502.04759v1 (2015); MP 151 (2015), 10.1007/s10107-015-0892-3. Primary.
19. Royer & Wright, "Complexity analysis of second-order line-search algorithms ...", arXiv:1706.03131v2 (2017); SIOPT 28 (2018), 10.1137/17M1134329. Primary.
20. Royer, O'Neill & Wright, "A Newton-CG Algorithm with Complexity Guarantees ...", arXiv:1803.02924v4 (2018); MP 180 (2020), 10.1007/s10107-019-01362-7. Primary.
21. Curtis, Robinson, Royer & Wright, "Trust-Region Newton-CG with Strong Second-Order Complexity Guarantees ...", arXiv:1912.04365v3 (2020); SIOPT 31 (2021), 10.1137/19M130563X. Primary.
22. Wright, S. J. "The Ongoing Impact of Interior-Point Methods", talk slides, SIAM Conference on Optimization, Toronto, 20 May 2002 (expanded 27 May 2002). https://pages.cs.wisc.edu/~swright/talks/siopt_talk_may02.pdf Primary.
23. Wright, S. J. "Optimization in Machine Learning: Recent Developments and Current Challenges", slides, NIPS Workshop, Whistler, 12 Dec 2008. https://pages.cs.wisc.edu/~swright/talks/sjw-nips.pdf Primary.
24. Wright, S. J. "Recent developments in interior-point methods", Preprint ANL/MCS-P783-0999 (1999); in *System Modelling and Optimization* (2000), 10.1007/978-0-387-35514-6_14. https://pages.cs.wisc.edu/~swright/papers/P783.pdf Primary.
25. Potra & Wright, "Interior-point methods", preprint Nov. 1999; JCAM 124 (2000), 10.1016/S0377-0427(00)00433-7. https://pages.cs.wisc.edu/~swright/papers/potra-wright.pdf Primary.
26. UW-Madison Oral History Program, "Oral History Interview, Stephen Wright (2179)", interviewed by Francisco Hernandez-Moleres, 2022-10-04; transcript `Wright.S.2179_transcript.docx`. https://minds.wisc.edu/handle/1793/83811 Primary. (I extracted the text myself into scratch. Research agent 02 has since saved a plain-text copy at `../sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt`, and the quotes here match that file's wording.)
27. UW-Madison Computer Sciences, "Computer Sciences Professor Steve Wright awarded prestigious George B. Dantzig Prize", 2024-07-22. https://www.cs.wisc.edu/2024/07/22/steve-wright-awarded-dantzig-prize/ Secondary (contains primary quotes).
28. UW-Madison Data Science Institute, "Steve Wright Awarded Prestigious George B. Dantzig Prize", 2024-07-22. https://dsi.wisc.edu/2024/07/22/steve-wright-awarded-prestigious-george-b-dantzig-prize/ Secondary.
29. MOS, "2024 Dantzig Prize Citation". https://www.mathopt.org/?nav=dantzig_2024. Seen only as a WebSearch summary (JavaScript page, not read verbatim). Secondary.
30. INFORMS Optimization Society, Khachiyan Prize winners list (2020: Stephen Wright, James Orlin). https://connect.informs.org/optimizationsociety/prizes/khachiyan-prize Secondary.
31. arXiv abstracts: Lee & Wright arXiv:2602.10470 (2026); Ding & Wright arXiv:2310.01784 and arXiv:2502.02099; Smee, Roosta & Wright arXiv:2502.03701; Alacaoglu & Wright arXiv:2311.00678. Primary.
32. OpenAlex title searches for the publication status of arXiv-only items (Liu & Wright ACHA 2014, 10.1016/j.acha.2013.12.006; ASSET, 10.5220/0003786202230228). Secondary.
33. WebSearch results (2 calls): "Stephen J. Wright 2024 George B. Dantzig Prize citation"; "'Stephen Wright' optimization interview career Argonne interior-point Wisconsin machine learning" (led to source 26). Secondary.
34. Wright's papers-page note on Wright & Jarre MP 1999 (10.1007/s101070050026) linking a published-proof correction. https://pages.cs.wisc.edu/~swright/papers/ Primary.
