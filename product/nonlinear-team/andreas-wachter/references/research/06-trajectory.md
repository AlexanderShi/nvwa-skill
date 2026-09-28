# 06 · Research trajectory: timeline, lineage, turns and their triggers

> **Researcher**: Andreas Wächter (also written Waechter / Wachter; DBLP pid 62/4235; Mathematics Genealogy Project id 248784)
> **Dimension**: research agent 06 of 06, research trajectory (nuwa research-craft Phase 1)
> **Research date**: 2026-09-28
> **Sources consulted**: 24 listed under "Sources": 12 primary and 12 secondary. Identifiers checked with a tool in this run: 49 DOIs (47 through Crossref, 2 through DataCite), 15 arXiv ids (12 through their abstract pages, 3 through the arXiv author listing), and 5 Optimization Online entries. WebSearch calls used: 2 of 2.
> **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` held only `.gitkeep` files. There was no user-supplied material, so nothing below is marked "from user-supplied material". `private/` was not opened. No talk transcript was found, so none was saved under `sources/talks/`.
> **Method**: his homepage (all pages) and his CV PDF (c. 2020, including the full dated talk list, which serves as a time series of topics); the PhD thesis (front matter, acknowledgments, Ch. 1, Ch. 6.2); **Wayback Machine snapshots** of his homepage, the Northwestern IEMS faculty list and Gurobi's "Our Team" page, used to date the move to Gurobi; the Mathematics Genealogy Project (MGP); the co-examined dissertation of M. Schmidt (Hannover 2013); the COIN-OR Ipopt git history and the documentation source; arXiv listings and version histories; Crossref, DataCite and Optimization Online records; the Gurobi 13.0 deck and webinar slides.
> **Tags**: [stated] = he said or wrote it (co-authored text is marked [stated-joint]) · [practice] = what the record shows he did (papers, code, CV entries, dates) · [observed] = what others wrote or recorded · [inferred] = my reading, which no source states. Each item also carries **P** (primary) or **S** (secondary).
> **Quoting**: quotations are verbatim. The thesis text layer splits words with kerning spaces, so I rejoined split words and changed nothing else. In the Ipopt documentation source I dropped Doxygen's `%` escape before "Ipopt".
> **Relation to 01–05**: 01 dissects the signature works and lists papers by period, 03 covers code and revision behaviour, and 04 covers students. I re-checked every identifier and quote used below myself. This file adds the dated timeline, the lineage, the triggers behind each turn, entry and exit timing, the dating of the Gurobi move, and the last 12 months.

---

## 0. Identity hygiene for the timeline

- The OpenAlex profile in `../sources/publications/publications.md` lists 2025 items that belong to namesakes: a forestry-crane robotics paper (ICRA 2025), MR relaxometry (*Cancers* 2025), machine-tool energy papers (TU Darmstadt), and 1975 and 1991 items. None of them belongs in his trajectory. 01 §0 has the full audit. [practice, S]
- arXiv author search (all three spellings, 22 results) contains 4 papers by a KIT biomedical-engineering namesake (2109.15063, 2201.03288, 2204.09346, 2310.10199). His own arXiv record **starts in 2015** (1505.04315). Earlier preprints went to Optimization Online or institutional report series (IBM RC, CMU CAPD, Namur). [practice, P]

---

## 1. Dated timeline

| When | Event | Evidence | Tag |
|---|---|---|---|
| 1992–1997 | Diplom-Mathematiker, University of Cologne | CV ("Diplom-Mathematiker (German Master's degree equivalent in Mathematics)") | [stated, P] |
| 1997–2002 | PhD in **Chemical Engineering**, Carnegie Mellon; advisor Lorenz T. Biegler; committee Grossmann, Sholl, Tütüncü | CV; thesis title page and acknowledgments; MGP 248784 | [stated, P] |
| Oct 1999 | First recorded talk: "A Quasi-Newton Interior Point Method for Large-Scale Nonlinear Programming with Modifications to Handle Constraint Inconsistencies", 1st Workshop on Nonlinear Optimization: Interior-Point and Filter Methods, Coimbra | CV talk #53 | [practice, P] |
| 2000 | "Failure of global convergence for a class of interior point methods for nonlinear programming", *Math. Program.* 88(3):565–574 (DOI 10.1007/PL00011386). ISMP talk Aug 2000: "…Failure and Some Remedies". Fortran Ipopt first released (homepage) | Crossref; CV #51; homepage research page | [practice, P] |
| 2000 | Reduced-space quasi-Newton barrier method: CAPD TR B-00-06 (CMU). **Never published in a journal** (absent from the CV journal list) | CV technical reports | [practice, P] |
| Jan 2002 | Thesis "An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering" (dated January 29, 2002). **Circuit-tuning talk at IMA in the same month**, before the IBM start | thesis; CV #48 | [practice, P] |
| 2002 | TR-SQP-filter convergence with Fletcher, Gould, Leyffer, Toint, *SIAM J. Optim.* 13(3):635–659 (DOI 10.1137/S1052623499357258). SIAM Student Paper Prize for the line-search filter work | Crossref; CV awards | [practice, P] |
| Feb 2002 | IBM T. J. Watson, Mathematical Sciences: postdoc (Feb–Oct 2002), then Research Staff Member (Oct 2002–2011) | CV | [stated, P] |
| 2002 → | Ipopt "actively developed under COIN-OR since 2002" | Ipopt docs source (`doc/main.dox`) | [stated-joint, P] |
| 2004 | ICCOPT-I Young Researcher honourable mention. IBM–CMU joint MINLP study begins | CV; Optima 75 | [stated, P] |
| 2004–2005 | C++ rewrite of Ipopt with Carl Laird (IBM summer intern 2004 and 2005). The homepage dates it "2005-2006" (see Contradictions) | Ipopt docs; homepage | [stated, P] |
| 2005–2006 | Line-search filter I/II, *SIOPT* 16(1), 2005 (DOIs 10.1137/S1052623403426556, 10.1137/S1052623403426544). IPOPT implementation paper, *Math. Program.* 106(1):25–57, 2006 (DOI 10.1007/s10107-004-0559-y). Circuit tuning, *FGCS* 21(8), 2005 (DOI 10.1016/j.future.2005.04.002) | Crossref | [practice, P] |
| 2007–2009 | MINLP plenaries (Czech-French-German 2007, SIAM OP 2008). Bonmin, *Discrete Optim.* 5(2), 2008 (DOI 10.1016/j.disopt.2006.10.011). Couenne, *OMS* 24(4–5), 2009 (DOI 10.1080/10556780903087124) | CV #30–33; Crossref | [practice, P] |
| 2007–2010 | Linear algebra inside the IPM with Schenk (COA 2007, DOI 10.1007/s10589-006-9003-y; SISC 31(2), DOI 10.1137/070707233). Adaptive barrier with Nocedal and Waltz (*SIOPT* 19(4), DOI 10.1137/060649513). Inexact / matrix-free steps with Curtis (*SIOPT* 20(3), DOI 10.1137/08072471X; *SISC* 32(6), DOI 10.1137/090747634) | Crossref | [practice, P] |
| 2009 | INFORMS Computing Society Prize (with Biegler) for the IPOPT paper. Dagstuhl tutorial "Getting Started With Ipopt in 90 Minutes" (DOI 10.4230/DagSemProc.09061.16) | INFORMS page; DataCite | [observed, S]; [practice, P] |
| 2009–2011 | IBM computational lithography (SPIE 2009/2010/2011; *J. Vac. Sci. Technol. B* 29(6), 2011, DOI 10.1116/1.3662090). Two US patents (CV only, not checked ⚠️) | Crossref; CV | [practice, P] |
| 2011 | J. H. Wilkinson Prize for Numerical Software (with C. D. Laird). **Moves to Northwestern IEMS as Associate Professor.** Last year with a substantial number of Ipopt commits (51) | CV; git log | [stated/practice, P] |
| 2012–2015 | NSF DMS single-PI grant "Novel Algorithms for Nonlinear Optimization" (Aug 2012–Jul 2015). "Towards Hot-Started NLP Solvers" talks (ISMP 2012, INFORMS 2012, MIP 2014). Inexact SQP, *SIOPT* 24(3), 2014 (DOI 10.1137/130918320). Hot-start QP, *SIOPT* 25(2), 2015 (DOI 10.1137/130940384). First PhD graduate (T. Johnson, 2013). Co-referee of M. Schmidt's Hannover dissertation (defended 23 Jan 2013) | CV; Crossref; Schmidt thesis | [practice, P] |
| 2013–2016 | NSF CMMI collaborative grant with J.-S. Pang and J. E. Mitchell (complementarity). "Complementarity Formulations of l0-norm Optimization Problems" (Optimization Online 2013/09/4053 → *Pacific J. Optim.* 14(2), 2018 per CV) | CV; Optimization Online | [practice, P] |
| 2015–2019 | NSF DMS single-PI grant "Algorithms for Nonlinear Nonconvex Optimization under Uncertainty" (Sep 2015–Sep 2019). First arXiv preprint (1505.04315, with Keskar, Nocedal, Öztoprak), which won the Charles Broyden Prize 2016. Chance constraints (*SIOPT* 28(1), 2018, DOI 10.1137/16M109003X). Noisy DFO (*SIOPT* 28(2), 2018, DOI 10.1137/15M1031679). Nonsmooth L-BFGS (*OMS* 34(1), 2019, DOI 10.1080/10556788.2017.1378652). Courses "Optimization Methods in Data Science" (2017, 2018) | CV; arXiv; Crossref | [practice, P] |
| Nov 2018 – Nov 2019 | ARPA-E grant "Hybrid Interior-Point/Active-Set SCOPF Algorithms Exploiting Power Systems Characteristics" (with Curtis, Molzahn, Wei, Wong) | CV | [stated, P] |
| 2019 | Promoted to Professor. Stanislaw M. Ulam Distinguished Scholar, CNLS, Los Alamos (2019–2020) | CV | [stated, P] |
| 2020 | 2nd place in the ARPA-E Grid Optimization Competition ($400,000). LANL CNLS lecture series "Numerical Nonlinear Optimization" (22 Jun 2020). **Last Ipopt commit (30 Jun 2020)** | CV; tutorial slides; git log | [practice, P] |
| 2021–2024 | Power-grid decomposition (TPWRS 36(1), 2021, DOI 10.1109/TPWRS.2020.3002189; *Oper. Res.* 71(6), 2023, DOI 10.1287/opre.2023.2453). PowerModelsITD (TPWRS 39(1), 2024, DOI 10.1109/TPWRS.2023.3234725). Conic SQP with warm starts (*SIOPT* 34(3), 2024, DOI 10.1137/22M1507681) | Crossref | [practice, P] |
| **between 8 Oct and 1 Nov 2024** | First appears on Gurobi's "Our Team" page as "Senior Software Developer": "He is a professor of Industrial Engineering at Northwestern University and is excited to join Gurobi's development team during his academic leave." | Wayback snapshots of gurobi.com/company/our-team/ | [observed, S] (a company page, probably approved by him; authorship not known) |
| Jan–Feb 2025 | arXiv 2501.11700 (two-stage decomposition, v1 20 Jan 2025) and 2502.11302 (noisy constrained IPM, 16 Feb 2025) | arXiv | [practice, P] |
| **by 15 May 2025 → by 22 Jan 2026** | Listed on the Northwestern IEMS core-faculty page on 23 Apr and 15 May 2025; absent on 22 Jan 2026 and on 28 Sep 2026 (live). His McCormick profile URL returns 404 | Wayback; live page | [observed, S] |
| **between 23 Sep and 12 Nov 2025** | The Gurobi bio changes to the past tense: "Before joining Gurobi, he spent 10 years at IBM Research and was a professor of Industrial Engineering at Northwestern University." Title now "Senior Developer" | Wayback | [observed, S] |
| 25 Nov 2025 | "What's New in Gurobi 13.0" deck: section "Nonlinear Barrier in Gurobi / Dr. Andreas Wächter" | PDF metadata and pp. 28–33 | [observed, S] |
| **between 19 Aug 2025 and 2 Feb 2026** | Homepage banner appears: "I moved to Gurobi Optimization. This webpage is no longer maintained." | Wayback snapshots of his homepage | [stated, P] |
| 18 Feb 2026 | Gurobi webinar "Local Nonlinear Optimization in Gurobi 13.0" (with S. Bowly) | Gurobi page; slides | [stated-joint, P] |
| Jul 2026 | Two *SIOPT* 36(3) papers online (3 and 8 Jul 2026). arXiv 2607.16430 (17 Jul 2026, LANL-led), which still gives him a northwestern.edu address | Crossref; arXiv HTML | [practice, P] |

---

## 2. Periods and their resource context

| Period | Seniority / setting | Resources and constraints | What the period produced | Evidence |
|---|---|---|---|---|
| 1992–1997, Cologne | Mathematics student | — | Diplom. **Thesis topic and advisor not found** | CV [stated, P] |
| 1997–2002, CMU ChemE | PhD student in a process-systems-engineering group | Single Linux workstations; Fortran 77; Harwell MA27; AMPL; ADOL-C; KNITRO and LOQO obtained from their authors (thesis acknowledgments thank Waltz, Benson and Vanderbei, Moré for TRON, Walther and Vogel for ADOL-C). Biegler is called "a true Doktorvater", who "gave me the optimal balance of guidance and freedom" | Fortran Ipopt, the failure example, filter line search, a TR-SQP-filter co-authorship with the Dundee–Namur–RAL group | thesis [stated, P] |
| 2002–2011, IBM Research | Postdoc, then Research Staff Member | The role combined research with customer projects: "participate in and lead projects for external and internal IBM customers; write efficient state-of-the-art optimization software" (CV). IBM paid for the C++ rewrite: "IBM Research decided to invest in an open source re-write of Ipopt in C++" (Ipopt docs). Industrial problem owners (circuits, lithography, reservoirs) | IPOPT 3.x, filter theory papers, MINLP solvers (Bonmin, Couenne), linear-algebra and inexact-step IPM papers, lithography | CV, docs [stated, P] |
| 2011–2024, Northwestern | Associate Professor, then Professor (2019); 1–3 own students plus co-advised ones | Single-PI NSF DMS grants; NSF CMMI (with Pang, Mitchell); ARPA-E; LANL; DOE OE AGM funding and NSF DMS-2012410 (footnotes of arXiv 2501.11700 v3). Ipopt maintenance passes to Stefan Vigerske: distinct commits per year in this run, Wächter 2010: 120 → 2011: 51 → 2012: 8; Vigerske 2011: 51 → 2012: 73 → 2013: 225 | Problem-class waves (uncertainty, noise, nonsmoothness, complementarity, simulation optimization, power grids) around a solver core | CV; git log [practice, P] |
| Oct/Nov 2024 – 2025, Gurobi on academic leave | Senior Software Developer | Commercial solver company with an existing NL barrier component (the 13.0 deck lists "Introduced in 9.5 in NLPheur heuristic" before "13.0 … Directly callable") | NL barrier as a directly callable local NLP solver ("Preview Feature" in 13.0) | Gurobi pages [observed, S]; slides [stated-joint, P] |
| late 2025 –, Gurobi | Senior Developer | Proprietary code; only public talks and slides are visible | Webinar Feb 2026. Academic papers keep appearing with students and co-authors (Jul 2026) | as above |

[inferred] The trajectory has **two industrial-lab bookends**, IBM (2002–2011) and Gurobi (2024/25–), around a 13-year academic period. In both industrial periods the output is a general-purpose solver. In the academic period it is mostly problem-class papers with students.

---

## 3. Lineage

### 3.1 Upstream

- **Richard R. Hughes → Lorenz T. Biegler** (PhD Wisconsin–Madison 1981, "Optimization Methods for Sequential Modular Simulators") **→ Andreas Wächter** (PhD CMU 2002). Hughes's own advisor is "Unknown" in MGP. The line runs through chemical-engineering process optimization, not mathematics departments. [observed, S: MGP 112809, 102705, 248784]
- **Informal mentors named in the thesis** [stated, P]:
  - R. Tütüncü, "for taking the effort of teaching me the basics of interior point methods in a reading course";
  - J. Nocedal, "who became a very encouraging mentor to me, and who introduced me into the math programming crowd", thanked for "his warm hospitality during my visits at Northwestern". Nocedal later became his departmental colleague (Northwestern IEMS from 2011), co-author (2009, 2009, 2016) and co-advisor (Keskar).
- **Academic siblings who became collaborators** (MGP lists Biegler's students) [observed, S; linking them is practice from author lists]:
  - Carl Laird (PhD 2006): Ipopt C++ co-author and co-recipient of the 2011 Wilkinson Prize. Later a co-author of the 2019 linear-solver study (arXiv 1909.08104).
  - Victor Zavala (2008): chance constraints, *SIOPT* 2018.
  - Arturo Cervantes (2000): 2000 and 2002 papers.
  - Arvind Raghunathan (2004): thanked in the thesis for "joint projects that contributed to this dissertation".

### 3.2 Downstream

Three records disagree, so all three are kept (see Contradictions):

| Record | Students listed |
|---|---|
| MGP 248784 [observed, S] | Ben Feng (2016), Nitish Keskar (2017), Mark Semelhago (2020), Shenyinying Tu (2021), and **Martin Schmidt (Leibniz Universität Hannover, 2013) as "Advisor 3"**. "5 students and 10 descendants" |
| Homepage (frozen) [stated, P] | Current: Yuchen Lou (co-advised with Ermin Wei). Former: Dezfulian, Luo, Izadinia, Tu, Peña-Ordieres, Semelhago, Jara-Moroni, Keskar, Feng, Johnson |
| CV c. 2020 [stated, P] | Dezfulian (exp. 2024), Luo (exp. 2023), Tu (exp. 2021), Semelhago (2020), Peña-Ordieres (2020), Jara-Moroni (2018), Keskar (2017), Feng (2016), Johnson (2013) |

- **Martin Schmidt (new in this run).** His dissertation "A generic interior-point framework for nonsmooth and complementarity constrained nonlinear optimization" (Leibniz Universität Hannover, 2013, DOI 10.15488/8161) names Wächter as the third referee: "Korreferent: Prof. Dr. Andreas Wächter, Northwestern University". The supervisor is Marc Steinbach. The thesis thanks "Andreas Wächter for his valuable comments on an earlier version of the interior-point method for nonsmooth constrained problems". It says its base method "is strongly oriented towards the interior-point code Ipopt of Andreas Wächter", and that "some aspects of the presented strategy are influenced by discussions with Andreas Wächter". [observed, S]
  - The Hannover link predates this: his CV lists talks at the University of Hannover's Institute of Applied Mathematics in Mar 2007 and Feb 2008. [practice, P]
  - No joint paper with Schmidt was found in DBLP. [practice, S]
- **Grand-students (MGP)**: through Feng, Ou Dang (Waterloo 2021); through Schmidt, Yasmine Beck (Trier 2024), Andreas Schmitt (TU Darmstadt 2022), Jeroen Stolwijk (TU Berlin 2018) and Lukas Winkel (Trier 2023). [observed, S]
- **Pattern** [inferred]: the downstream line is short and applied. Most students went into problem classes set by a co-advisor or funding partner (04 §C). The strongest methodological descendant visible here is not a formal student: Schmidt built his framework on Ipopt's design. Ipopt users form a much larger informal "lineage", but no source measures it.

---

## 4. Turns and what triggered them

Trigger types used below: **own-code failure** · **application pull** (a problem owner or employer) · **collaborator / co-advisor** · **funding or competition** · **move** · **return** (an old item from his own future-work list).

| # | Turn (dates) | Trigger type | Evidence for the trigger | Stated reason? |
|---|---|---|---|---|
| T1 | Mathematics (Cologne) → PhD in **Chemical Engineering** (1997) | not known | — | **Not found.** No statement explains why a mathematician chose a ChemE PhD at CMU. |
| T2 | Reduced-space quasi-Newton IPM with merit functions (1999–2000) → full-space **filter** line-search IPM (2000–2002) | **own-code failure** | The 1999 Coimbra talk is already about "Modifications to Handle Constraint Inconsistencies" (CV #53). The failure example appeared in his own implementation (thesis §3.3.3, quoted in 01 SW1). The filter came in from the co-authorship with Fletcher, Gould, Leyffer and Toint (Namur TR 99/03 → *SIOPT* 2002). The Fletcher–Leyffer filter paper itself appeared in 2002: *Math. Program.* 91(2):239–269, DOI 10.1007/s101070100244 | Yes. Stated in the thesis (see 01 SW1–SW2). [stated, P] |
| T3 | Process engineering → **circuit tuning** at IBM (2002–2006) | **application pull, which came before the move** | The thesis (Jan 2002) already lists circuit tuning as future work: "it would be worthwhile exploring its potential in fields like PDE-constrained optimization and circuit tuning". His IMA talk "Application of an Interior Point Method for Large-Scale Nonlinear Programming to Circuit Tuning" is dated **Jan 2002, before the Feb 2002 IBM start** (CV #48) | Only the future-work sentence [stated, P]. That the collaboration led to the job is [inferred]. |
| T4 | Fortran 77 Ipopt 2.x → C++ Ipopt 3.x (2004–2006) | **employer investment** plus **return** | The thesis says "an even larger degree of flexibility could be obtained by a re-implementation in C++, employing object-oriented concepts". The docs say "To continue natural extension of the code and allow easy addition of new features, IBM Research decided to invest in an open source re-write" | Yes (docs) [stated-joint, P] |
| T5 | Entry into **MINLP** (2004–2013) | **employer–university programme** | "In 2004, IBM and Carnegie Mellon University initiated a joint study aimed at Mixed Integer Nonlinear Programming (MINLP), with the goal of releasing the resulting software under the CPL on COIN-OR." And "Our original goal was to use existing software components of COIN-OR to produce a simple NLP-based branch-and-bound code aimed at MINLP problems that have convex relaxations. As we progressed, we expanded our goal" (Optima 75, 2007) | Yes, a joint statement [stated-joint, P]. **Exit** after 2013 (last MINLP paper: ACM JEA 18, 2013, DOI 10.1145/2532568). Reason for leaving MINLP: **not found**. |
| T6 | Factorization-based steps → **iterative linear algebra, inexact / matrix-free steps** (2007–2012) | **collaborators** (Schenk in Basel; Curtis and Nocedal) plus **return** | The thesis future-work list names "the choice of the linear solver used for the factorization of the KKT matrix" and PDE-constrained optimization. First talk: Basel, Feb 2009 (CV). The line was shipped back into Ipopt (*Math. Program.* 136(1), 2012, DOI 10.1007/s10107-012-0557-4) | Only as future work [stated, P]. The collaborator trigger is [inferred]. |
| T7 | Adaptive barrier updates (talks 2004–2005 → *SIOPT* 2009) | **return** | Thesis: "To follow such an approach in nonlinear and nonconvex cases, the mechanisms for global convergence have to be adapted." | yes (future work) [stated, P] |
| T8 | **Computational lithography** (2008–2011) | **employer project** | IBM author teams of 10–30 people (SPIE 2009/2010; JVST B 2011) | [practice, P]. Stops with the move to Northwestern. |
| T9 | IBM → **Northwestern** (2011) | **move** | Nocedal was a mentor since the PhD (thesis acknowledgments; the CV lists an Optimization Technology Center talk at Northwestern in Dec 2002) | **Reason not found.** |
| T10 | After 2011: a fan-out into **problem classes** set by grants and co-advisors: hot-start SQP (2012–2015), complementarity with Pang and Mitchell (2013–2020), ML-flavoured nonsmooth and ℓ1 work with Nocedal and Keskar (2015–2019), noisy DFO (2014–2018), chance constraints (2016–2021), simulation optimization with Nelson and Song (2017–2026), power grids with Wei, Curtis and LANL (2018–2026) | **funding / collaborators / co-advised students** | Grant titles and dates in the CV. His self-description names the programme: "Introducing techniques and concepts for nonlinear optimization into settings where they have not yet been exploited." (homepage research page) | Only the general theme is stated [stated, P]. That each class came through a co-advisor is [inferred] (04). |
| T11 | Entry into **power systems** (2018–) | **competition + funding + lab visit** | ARPA-E grant Nov 2018; GO competition 2nd place 2020; Ulam scholarship LANL 2019–20; "Grid Science Winter School" talk Jan 2019 (CV #2). Open-source IPMs were already the standard OPF tool by then [observed]: Kardos et al., arXiv 1807.03964, write that "Recent advances in open source interior-point optimization methods and power system related software have provided researchers and educators with the necessary platform for simulating and optimizing power networks with unprecedented convenience." | No stated reason. The research page lists "Description of our GO-SNIP team algorithm for the ARPA-E Grip Optimization Competition" [stated, P]. |
| T12 | **Two-stage decomposition** (2020 → 2026) | **return**, with a new application | Thesis 2002: "In the implementation of the elemental decomposition it is currently not possible to impose additional constraints, that couple the entire system. Here, a two-stage decomposition strategy might provide the answer." That came 18 years before TPWRS 2021 and 24 years before *SIOPT* 2026 | The 2002 sentence is [stated, P]; the causal link is [inferred]. |
| T13 | **Noise** in IPMs (2006 idea → 2024–2026 papers) | **return**, after others had built the tools | Talk "Smoothing Noisy Black-Box Functions For Nonlinear Optimization", ISMP Aug 2006 (CV #35); DFO-with-noise talks 2014–2015; *SIOPT* 2018. The 2025 IPM abstract says it builds on "a previously proposed interior-point algorithm that allows inexact subproblem solutions and recently proposed algorithms for solving bound- and equality-constrained optimization problems with only noisy function and derivative values" (arXiv 2502.11302) | stated-joint for the building blocks [P] |
| T14 | **Hot starts → warm-startable conic SQP** (2012 → 2022–2024) | **return** | "Towards Hot-Started NLP Solvers" (ISMP 2012, INFORMS 2012) → QP only (2015) → "A Quadratically Convergent Sequential Programming Method for Second-Order Cone Programs Capable of Warm Starts" (arXiv 2207.03082 v1 7 Jul 2022; *SIOPT* 2024) | [inferred] continuity |
| T15 | Academia → **Gurobi** (leave from Oct/Nov 2024; permanent by late 2025) | **move**, back to building a general-purpose NLP solver | Gurobi bio (Jan 2025): "excited to join Gurobi's development team during his academic leave". The 13.0 deck lists Ipopt-lineage ingredients: "Relies on indefinite factorization of KKT system", "Line search, Feasibility restoration, …", "Regularization for non-convex problem", "Iterative refinement". It also lists a departure: "Simple line search (without filter)" | Only the Gurobi bio wording [observed, S]. **No statement by him on why he moved.** |

### 4.1 What the turns share [inferred]

1. **His own future-work list keeps coming back.** The thesis future-work list (Jan 2002) names the C++ rewrite, the barrier update, linear-solver choice, PDE-constrained optimization, circuit tuning and two-stage decomposition. Every one of these became later work: T3, T4, T6, T7 and T12. The thesis also frames the programme: "Also, continued usage is expected to reveal bottlenecks, either in the implementation or in the underlying mathematical algorithm, and might raise interesting research questions." [stated, P]
2. **Applications arrive through institutions, not literature.** Circuits and lithography came through IBM, MINLP through the IBM–CMU study, uncertainty and complementarity through NSF grants and co-PIs, grids through ARPA-E and LANL, simulation optimization through Nelson and Song.
3. **The core stays fixed.** Every wave is solved by an interior-point or SQP NLP method, usually by turning the new problem into a smooth NLP that existing solvers can handle. The 2026 two-stage paper puts it this way: "As a consequence, efficient off-the-shelf optimization packages can be utilized." (arXiv 2501.11700, abstract) [stated-joint, P]
4. **Long incubation.**
   - Noise: 2006 talk → 2018 paper → 2024–2026 IPM papers.
   - Two-stage decomposition: 2002 → 2021/2026.
   - Hot starts: 2012 → 2024.
   - Chance constraints: talk titled "Kernel-VaR Estimator" (2017) → published as a quantile approximation in 2020.
   - Adaptive barrier: talks 2004 → 2009.
   - ℓ0 complementarity: Optimization Online Sept 2013 → *PJO* 2018.
   - LPCC via DC: received 13 Feb 2016, accepted 2 Nov 2017 (Crossref, DOI 10.1007/s10107-017-1208-6).

### 4.2 How his self-description changed [stated, P]

| Source (date) | Wording |
|---|---|
| CV page biosketch (c. 2020) | "His research interests include the design, analysis, implementation and application of numerical algorithms for nonlinear continuous and mixed-integer optimization." |
| Homepage index (frozen after the move; the same text was on the 19 Aug 2025 Wayback snapshot) | "My research interests include the design, analysis, implementation and application of numerical algorithms for nonlinear continuous and mixed-integer optimization, scientific computing, power systems, and sustainability." |
| CNLS lecture, 22 Jun 2020, example applications | "Optimal operation of electricity or gas networks." / "Optimal control of a chemical plant." / "Transistor sizing in digital circuits." / "Inverse problems (fit coefficients in PDEs)." |
| Gurobi bio (Nov 2025 →) | "an expert in the development of optimization algorithms for nonlinear optimization" |

[inferred] The four example applications in the 2020 lecture line up with his career stages: grids (LANL/ARPA-E), chemical plants (CMU), circuits (IBM) and PDEs (the Basel/IBM inexact line). He chooses examples from problems he has solved himself.

---

## 5. Entry and exit relative to the field

All placements in this section are [inferred] from the dated evidence cited. No source states them.

| Topic | Entry | Relative to the field | Exit / status |
|---|---|---|---|
| Filter globalization | Co-author of the TR-SQP-filter convergence report (Namur TR 99/03, i.e. 1999), before the Fletcher–Leyffer paper appeared in print (*Math. Program.* 2002). Line-search filter theory 2005 | **Early**: he helped build the theory while filters were new. He had the first line-search filter with global and local convergence theory (the INFORMS 2009 citation: "the first to combine a barrier nonlinear programming method with a line search filter method, with a fundamental convergence theory for this approach") | Still the Ipopt default. At Gurobi the 13.0 NL barrier uses "Simple line search (without filter)" (deck p. 33) |
| Convergence critique of IPMs | 2000 failure example | **Early**: the critique came while line-search IPMs for nonconvex NLP were new (see 01 SW1) | Resolved by his own filter |
| Open-source MINLP | 2004 IBM–CMU study; Bonmin 2008, Couenne 2009 | **Early-to-concurrent**: "the subject of MINLP has received a lot of recent attention" (Optima 75, 2007) | **Left** after 2013, at a time when the area had its own dedicated groups. Reason not known |
| Inexact / matrix-free IPM | 2009–2012 | Concurrent with the Curtis–Nocedal inexact-SQP line (a collaboration, not a follow-on) | No new papers after 2014 except the 2025 noisy IPM, which reuses it |
| Chance constraints | 2016 talks, 2018/2020 papers | **Late entrant** to an old field, bringing an NLP angle (smooth quantile reformulation) | Carried into DC-OPF (2021) |
| Power grids | 2018 grant; 2020 competition | **Late entrant** to OPF, where open-source IPMs (his own Ipopt among them) were already standard tools (Kardos et al. 2018). He entered as a solver expert through a competition | Still active in 2026 (arXiv 2607.16430) |
| Noisy optimization | Idea 2006; noisy IPM papers 2024–2026 | **Idea early, papers late**: the 2025 abstract builds on "recently proposed" noisy-optimization algorithms by others | Active in 2025–2026 |
| Machine learning | ℓ1 active-set 2015/16, nonsmooth L-BFGS 2016/19, data-science course 2017–18 | Concurrent, through Nocedal and Keskar | **Left** after about 2019 (the 2017 BFGS arXiv 1712.08571 has no journal version found in Crossref) |

---

## 6. Failures, abandoned directions and unfinished items

[practice unless marked; reasons **not known** unless quoted]

1. **Reduced-space quasi-Newton barrier method** (CAPD TR B-00-06, 2000): central in the thesis, never published in a journal. The full-space filter version won out.
2. **Merit-function line searches**: failed on his own counterexample (2000) and were demoted to options (01 SW1).
3. **Hot-started NLP solvers** (talks 2012–2014): produced only the QP paper (2015). The NLP-level goal came back in conic form in 2022–2024 (T14).
4. **Parallel Ipopt**: ISMP 2009 talk "Solving Nonlinear Optimization Problems on Large-Scale Parallel Computers" (CV #27). The `parallel` branch of Ipopt was never merged (03). The topic returned only as a 2019 linear-solver study (arXiv 1909.08104, a technical report, no journal version in the CV).
5. **MINLP** stops in 2013; **lithography** stops in 2011; **ML-flavoured work** stops about 2019.
6. **Preprints without a journal version found** (Crossref search): Xie & Waechter, arXiv 1712.08571 (2017); Avci, Nelson & Wächter, arXiv 2302.02254 (2023). Having no journal version is not evidence of rejection. No rejection or retraction record was found.
7. **Ipopt stewardship handed over**: his commits fall from 120 (2010) to 8 (2012). There is one commit each in 2013, 2018 and 2020, the last on 30 Jun 2020. Vigerske released 3.14.20 on 27 Aug 2026. [practice, P: git log]

---

## 7. The last 12 months (28 Sep 2025 → 28 Sep 2026)

| Date | Item | Tag |
|---|---|---|
| between 23 Sep and 12 Nov 2025 | Gurobi bio switches from "during his academic leave" to "was a professor … at Northwestern University" | [observed, S] |
| 7 Nov 2025 | arXiv 2501.11700 v2 (two-stage decomposition) | [practice, P] |
| 25 Nov 2025 | "What's New in Gurobi 13.0" deck, section "Nonlinear Barrier in Gurobi / Dr. Andreas Wächter". Its ingredients include "Feasibility Relaxation (feas relax)", "Simple line search (without filter)", "Iterative refinement", "Algorithmic differentiation" and "Handling numerical difficulties to achieve more accurate solutions". Which slides he wrote is **not known** | [observed, S] |
| Jan 2026 | Avci, Nelson, Song, Wächter, "Dice and slice simulation optimization for high-dimensional discrete problems", *Eur. J. Oper. Res.* 330(3):850–863 (DOI 10.1016/j.ejor.2026.01.005; Crossref record created 10 Jan 2026, issue May 2026) | [practice, P] |
| by 22 Jan 2026 | No longer on the Northwestern IEMS core-faculty page | [observed, S] |
| by 2 Feb 2026 | Homepage banner "I moved to Gurobi Optimization. This webpage is no longer maintained." | [stated, P] |
| 18 Feb 2026 | Webinar with S. Bowly, "Local Nonlinear Optimization in Gurobi 13.0". The slides' "Summing Up" includes "Local optima are often sufficient in practice", "Often, starting points help performance", "Not suitable for problems with combinatorial aspects", "Try both for your application" and "Preview feature in Gurobi 13.0!" | [stated-joint, P] |
| 26 Feb 2026 | arXiv 2501.11700 v3 (northwestern.edu address; NSF DMS-2012410 and DOE OE AGM acknowledged) | [practice, P] |
| 1 Jun 2026 | Cederberg, Zhang, Nobel & Boyd, "Disciplined Nonlinear Programming" (arXiv 2606.02896). They cite the IPOPT paper for "the popularity of general-purpose NLP solvers such as Ipopt [93]" and cite the Wächter–Bowly slides [94] for Gurobi's NLP interior-point solver | [observed, S] |
| 3 and 8 Jul 2026 | Lou, Luo, Wächter, Wei, *SIOPT* 36(3):1211–1238 (DOI 10.1137/25M1728661), and Dezfulian, Wächter, *SIOPT* 36(3):1356–1386 (DOI 10.1137/24M1666537), published online | [practice, P] |
| 17 Jul 2026 | Ospina, Garcia, Luo, Wächter, Fobes, Bent, "Smoothed Two-Stage Decomposition Algorithm for Solving Large-Scale Transmission and Distribution AC-OPF Problems" (arXiv 2607.16430). LANL-led; "Integrated into the PowerModelsITD framework"; lists "X. Luo and A. Wächter are with the Northwestern University" | [practice, P] |
| 27 Aug 2026 | Ipopt 3.14.20 released by S. Vigerske. No Wächter commit | [practice, P] |

**Reading of the window** [inferred]: in public, the year shows (a) product work on a local NLP barrier at Gurobi, presented in company channels, and (b) academic papers finishing with former students and the LANL group. No new single-direction research line that is visibly his appears in the window. Every 2026 paper had its first preprint in 2022–2025. **Talks at ICCOPT, INFORMS or SIAM conferences in the window were not searched** (see Gaps).

---

## 8. Candidate trajectory heuristics for the skill (all [inferred] from §§1–7)

- **H1. Keep a future-work list and work through it for 20 years.** Most turns are returns to items written down in 2002 (§4.1).
- **H2. Let institutions bring the problems; keep the method.** Every new application came through an employer, grant, competition or co-advisor. The response is always the same NLP core, adapted.
- **H3. Enter early on algorithmic foundations, late on applications.** He entered filters and the IPM critique early, and MINLP concurrently. He entered chance constraints, grids and noise late, bringing an NLP-solver angle to fields that already had their tools.
- **H4. Leave when the problem class no longer needs a general NLP solver expert** (MINLP after 2013, ML after 2019). The exit reasons are not stated; this is a pattern only.
- **H5. Oscillate between building a solver (industry) and generalizing it (academia).** He built at IBM, generalized at Northwestern, and is building again at Gurobi.

---

## Contradictions (kept, not reconciled)

1. **Date of the Gurobi move.**
   - The Gurobi page lists him from Oct/Nov 2024, "during his academic leave".
   - The Northwestern faculty page still lists him in May 2025.
   - The Gurobi bio is in the past tense by 12 Nov 2025, and his homepage banner appears between Aug 2025 and Feb 2026.
   - Yet arXiv 2607.16430 (Jul 2026) and 2501.11700 v3 (Feb 2026) give his affiliation and email as Northwestern.
   - The frozen homepage index still opens "I'm a Professor in the Department of Industrial Engineering and Management Sciences at Northwestern University" directly under "I moved to Gurobi Optimization".
2. **Ipopt rewrite dates.** The homepage says "reimplemend in C++ in 2005-2006 at IBM by Carl Laird and myself". The Ipopt docs place Laird's internships in "2004 and 2005". The Fortran release year (2000, homepage) also sits beside "actively developed under COIN-OR since 2002" (docs).
3. **Years at IBM.** Gurobi bio: "he spent 10 years at IBM Research". CV: Feb 2002 – 2011.
4. **Martin Schmidt's advisor status.** MGP lists Wächter as "Advisor 3". The dissertation title page lists him as "Korreferent" (third referee), with Steinbach as supervisor.
5. **Student rosters.** MGP (5, including Schmidt), homepage (11 including Lou) and CV (9) disagree. 04 has further disagreements for Feng, Keskar, Avci and Johnson.
6. **Publication years, CV vs Crossref print dates.**
   - Schenk–Wächter–Weiser SISC 31(2): CV 2008, Crossref print Jan 2009.
   - Curtis–Nocedal–Wächter SIOPT 20(3): CV 2009, Crossref print Jan 2010.
   - PowerModelsITD: TPWRS 39(1), print Jan 2024, while 01 lists it as 2023 (online date).
   - The CV gives the failure paper as *Math. Program.* 88(2); Crossref says 88(3).
7. **Signature globalization.** Filter line search is the core of his theory and of Ipopt. The Gurobi 13.0 NL barrier he presented lists "Simple line search (without filter)" as a 13.0 improvement (also noted in 03).
8. **Role title at Gurobi**: "Senior Software Developer" (Oct 2024 – spring 2025), then "Senior Developer" (from the 1 Jun 2025 snapshot). This may just be a site-wide rename; I did not check other staff.

## Gaps

- **Cologne Diplom (1992–1997)**: thesis title, advisor and topic were not found. The CV's Cologne talk (Institute for Computer Science, Jan 2006) hints at a link there, but nothing confirms it.
- **Why ChemE at CMU (1997), why IBM (2002), why Northwestern (2011), why Gurobi (2024/25)**: no stated reason for any move except the Gurobi page's "academic leave" wording. No interview, oral history or retrospective was found (both WebSearch calls spent; one on the Gurobi period and talks, one on post-2020 honours).
- **Post-2020 honours and service**: the CV dates from about 2020. One WebSearch and the INFORMS recipient page found no honour after 2020. SIAM and MOS prize and fellow pages could not be read (SIAM returned 403; mathopt.org is a script-rendered app). **Not verified either way.**
- **Talks in the last 12 months** beyond the Gurobi webinar: conference programmes (INFORMS 2025, SIAM OP26, ICCOPT) were not searched. No recording or transcript was found.
- **Exact start date at Gurobi and exact end date at Northwestern**: bracketed by Wayback snapshots only. LinkedIn was not opened (login wall); theorg.com gives only the title ("No bio yet").
- **Status of the remaining student** (Yuchen Lou, co-advised with Wei): not found.
- **The Gurobi NL barrier's history before him** (the deck says it was "Introduced in 9.5 in NLPheur heuristic"): who built it, and what he changed, is not documented publicly.
- **Google Scholar**: not read (captcha in earlier runs; not retried).
- **Reasons for exiting MINLP (2013) and ML (about 2019)**: not found.

## Sources

Primary = his own writing, code history or bibliographic records of his own papers. Secondary = third parties, aggregators or institutional pages.

1. A. Wächter, homepage: index, research, students, software, links and CV pages (frozen, "I moved to Gurobi Optimization"), fetched 2026-09-28. https://users.iems.northwestern.edu/~andreasw/ (primary)
2. A. Wächter, "Curriculum Vitae: Andreas Wächter, Ph.D." (PDF, c. 2020; appointments, awards, grants, 53 conference talks, 30 seminars, advisees). https://users.iems.northwestern.edu/~andreasw/pubs/CV.pdf (primary)
3. A. Wächter, "An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering", PhD thesis, Carnegie Mellon University, 29 Jan 2002 (front matter, acknowledgments, Ch. 1, §6.2 read). https://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf (primary)
4. Wayback Machine snapshots of the homepage, 2025-08-19 (no banner) and 2026-02-02 (banner), with the CDX listing 2024–2026. https://web.archive.org/web/20260202140356/https://users.iems.northwestern.edu/~andreasw/ (primary, archived)
5. COIN-OR Ipopt git repository: commit log by author and year, release tags to releases/3.14.20 (2026-08-27), and `doc/main.dox` "History of Ipopt". https://github.com/coin-or/Ipopt (primary)
6. P. Bonami, J. J. Forrest, J. Lee, A. Wächter, "Rapid Development of an Open-source MINLP Solver with COIN-OR", *Optima* 75, Dec 2007. https://web.archive.org/web/2015/http://www.mathopt.org/Optima-Issues/optima75.pdf (primary, joint)
7. A. Wächter, "Numerical Nonlinear Optimization, Part I", CNLS lecture slides, Los Alamos, 22 Jun 2020. https://users.iems.northwestern.edu/~andreasw/pubs/CNLStutorial_1.pdf (primary)
8. A. Waechter, S. Bowly, "Local Nonlinear Optimization in Gurobi 13.0", webinar slides, 18 Feb 2026. https://gurobi.github.io/slides/local-nonlinear-v13.html (primary, joint)
9. arXiv abstract pages and version histories: 2607.16430, 2501.11700, 2502.11302, 2207.03082, 2405.11400, 2202.12961, 1905.07377, 2002.08003, 1612.07350 and 1909.08104, fetched 2026-09-28; 1712.08571, 1505.04315 and 2302.02254 checked through the author listing (item 11) only. https://arxiv.org/abs/2607.16430 etc. (primary records)
10. arXiv HTML full-text front matter for 2607.16430v1, 2501.11700v2 and 2501.11700v3 (affiliations, grant footnotes). https://arxiv.org/html/2607.16430v1 (primary)
11. arXiv author search for "Wächter, Andreas", "Waechter, Andreas" and "Wachter, Andreas" (22 results, 4 namesake items excluded). https://arxiv.org/search/?query=Waechter%2C+Andreas&searchtype=author (primary records)
12. Optimization Online entries 2004/03/836, 2008/05/1984, 2009/02/2227, 2011/04/2992 and 2013/09/4053. https://optimization-online.org/2013/09/4053/ etc. (primary records)
13. Crossref records for 47 DOIs cited above (including Fletcher & Leyffer, DOI 10.1007/s101070100244) (bibliographic data; article history for 10.1007/s10107-017-1208-6), fetched 2026-09-28. https://api.crossref.org/works/ (secondary)
14. DataCite records: DOI 10.4230/DagSemProc.09061.16 (Dagstuhl 2009) and DOI 10.15488/8161 (Schmidt 2013). https://api.datacite.org/dois (secondary)
15. Mathematics Genealogy Project records: Andreas Wächter (248784), Lorenz T. Biegler (102705), Richard R. Hughes (112809), Martin Schmidt (241560), Ben Mingbin Feng (273006). https://www.mathgenealogy.org/id.php?id=248784 (secondary)
16. M. Schmidt, "A generic interior-point framework for nonsmooth and complementarity constrained nonlinear optimization", Dr. rer. nat. dissertation, Leibniz Universität Hannover, 2013 (title page, acknowledgments, Ch. 4 passages read via the repository text layer). DOI 10.15488/8161 (secondary; observed)
17. Northwestern IEMS "Faculty" page, live 2026-09-28 and Wayback snapshots 2025-04-23, 2025-05-15 and 2026-01-22; McCormick profile URL (404). https://www.mccormick.northwestern.edu/industrial/people/faculty/ (secondary)
18. Gurobi "Our Team" page: live old-site copy and Wayback snapshots 2024-06-02, 2024-09-08, 2024-09-09, 2024-10-04, 2024-10-08, 2024-11-01, 2024-12-02, 2025-01-15, 2025-03-07, 2025-04-19, 2025-06-01, 2025-07-20, 2025-08-05, 2025-09-23 and 2025-11-12. https://www.gurobi.com/company/our-team/ ; https://www-old.gurobi.com/company/our-team/ (secondary)
19. Gurobi webinar page "Local Nonlinear Optimization in Gurobi 13.0" (speaker bios). https://www.gurobi.com/resources/webinar-events/local-nonlinear-optimization-in-gurobi-13-0 (secondary)
20. Gurobi, "What's New in Gurobi 13.0" slide deck (PDF created 2025-11-25; pp. 26–34 read). https://cdn.gurobi.com/wp-content/uploads/2025-11-25_Whats-New-in-V13.pdf (secondary)
21. INFORMS, "Andreas Wachter" award-recipient page (2009 INFORMS Computing Society Prize citation). https://www.informs.org/Recognizing-Excellence/Award-Recipients/Andreas-Wachter (secondary)
22. D. Cederberg, W. Zhang, P. Nobel, S. Boyd, "Disciplined Nonlinear Programming", arXiv 2606.02896 (1 Jun 2026), and J. Kardos, D. Kourounis, O. Schenk, R. Zimmerman, "Complete results for a numerical evaluation of interior point solvers for large-scale optimal power flow problems", arXiv 1807.03964 (2018) (secondary; observed reception and field context)
23. theorg.com profile "Andreas Waechter – Senior Software Developer at Gurobi Optimization" (title only, "No bio yet"). https://theorg.com/org/gurobi-optimization/org-chart/andreas-waechter (secondary)
24. WebSearch result lists, 2 queries (Gurobi-period talks; post-2020 honours), 2026-09-28, used only to locate items 19, 21 and 22 (secondary)
