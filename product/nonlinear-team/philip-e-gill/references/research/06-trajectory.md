# Philip E. Gill: research trajectory (research agent 06)

- **Researcher**: Philip Edward Gill. UC San Diego (UCSD), Department of Mathematics, since 1988. His homepage says "Distinguished Professor of Mathematics". UCSD Profiles now gives "Emeritus Professor, Mathematics". Earlier: National Physical Laboratory (NPL), Teddington, UK, then the Systems Optimization Laboratory (SOL), Stanford, 1979–1988.
- **Dimension**: research trajectory: the academic timeline, lineage, the turns in direction and what triggered them, when he enters and leaves topics, and activity in the last 12 months. Framework layer 2 (problem choice and timing), with evidence for layers 3 and 7.
- **Research date**: 2026-09-28
- **Sources consulted**: 36 (list at the end). 24 are primary: Gill's homepage pages, his papers, reports and slides, the software site, and institutional pages. 12 are secondary: aggregators, the genealogy database, a collaborator interview, and search results. WebSearch calls used: 2.
- **Local corpus**: `references/sources/papers/`, `essays/` and `software/` hold only `.gitkeep`, so **nothing here is from user-supplied material**. `talks/` holds one auto-caption transcript, Margaret H. Wright's 2019 INFORMS interview. Research agent 01 fetched it earlier in this run; it is not user-supplied. I cite it by line number. `private/` was not opened.
- **Sibling notes**: 01-publications, 02-methodology and 04-mentorship already exist. I used them as leads only. Every identifier and quote below was re-checked with a tool in this run (Crossref, DBLP SPARQL, OpenAlex, arXiv, or the text itself). 04-mentorship has the full student table, and this file does not repeat it.

### Tag legend

- **[stated]**: said by Gill, or by a group writing in a voice that includes him (slides, abstracts, papers, the 2008 essay).
- **[practice]**: what the records show he did (papers, reports, software, grants, dates).
- **[observed]**: what another person reports about him (here almost always M. H. Wright's interview).
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary source.

---

## 0. The trajectory in one paragraph (all [inferred], built from the sections below)

Gill's 55-year arc has **one constant core and several peripheral excursions**. The core is the numerical linear algebra *inside* an optimization method: factorizations, their updates, and how the choice of solver shapes the whole algorithm. That core ran from the 1972 factorized quasi-Newton paper, through the SOL codes and SNOPT, to the 2024 LDLᵀ trust-region method. Three kinds of trigger turned him:

1. **External shocks that met stored expertise**. Khachiyan (1979): tested, then dropped. Karmarkar (1984): entered interior methods **before the consensus**.
2. **Users hitting a scale or robustness wall**. Aerospace trajectory users outgrew NPSOL, and SNOPT followed from 1992. He built it **while**, by his own account, SQP research was in decline.
3. **Changes in hardware and the software ecosystem**. Modelling languages began supplying second derivatives, and multicore machines arrived. These drove his self-named 2008 "SQP renaissance": regularized and stabilized SQP, with the emphasis moved from matrix updating to factorization.

He **returns to old topics after decades**, by name. Quasi-Newton factored-Hessian methods came back in 2022–24, 50 years after his 1972 paper. "Shifted" barrier ideas appear in 1987 and again in 2020. A student's thesis often seeds a line that the group picks up again 10 or more years later. **The last dated output is October 2024. Nothing new was found for the 12 months to 2026-09-28.**

---

## 1. Dated timeline

| Date | Event | Tag | Source |
|---|---|---|---|
| 1971 | "Diploma of Imperial College, 1971" | [practice] P | homepage *In Person* |
| 1972 | First refereed optimization paper, with Murray: "Quasi-Newton Methods for Unconstrained Optimization", *IMA J. Appl. Math.* 9 (1972) 91–108, DOI 10.1093/imamat/9.1.91. Also that year, an NPL-era numerical-analysis paper with G. F. Miller: "An Algorithm for the Integration of Unequally Spaced Data", *Comput. J.* 15 (1972), DOI 10.1093/comjnl/15.1.80 | [practice] P | Crossref |
| c. 1973 | Visits Stanford. According to Wright, "Philip Gill who worked at the National Physical Laboratory in England had come to Stanford as a visitor I think in 73" [sic, auto-caption] | [observed] S | Wright interview, lines 145–147 |
| 1974 | PhD, Imperial College London. MGP gives the dissertation "Numerical Methods for Large-Scale Linearly Constrained Optimization", "Advisor 1: Walter Murray", "Advisor 2: David Quinn Mayne" | [practice] S (MGP); year also on homepage (P) | MGP id 6811; homepage |
| 1974 | "Methods for modifying matrix factorizations" (Gill, Golub, Murray, Saunders), *Math. Comp.* 28 (1974) 505–535, DOI 10.1090/S0025-5718-1974-0343558-6. Reprinted in the 2007 collection *Milestones in Matrix Computation* (DBLP incollection record) | [practice] P | Crossref; DBLP |
| 1974 | *Numerical Methods for Constrained Optimization* (Academic Press, 1974), Gill and Murray. Whether they were editors or authors was not checked. OpenAlex W1483815626 attributes the second name to "William Allan Murray", probably a misattribution | [practice] S | OpenAlex |
| 1974–79 | NPL papers with Murray: Newton-type methods (*Math. Prog.* 7 (1974), DOI 10.1007/BF01585529), stable QP (*Math. Prog.* 14 (1978), DOI 10.1007/BF01588976), nonlinear least squares (*SINUM* 15 (1978), DOI 10.1137/0715063), and "The Design and Structure of a Fortran Program Library for Optimization" (with Picken and Wright; *ACM TOMS* 5 (1979) 259–283, DOI 10.1145/355841.355844) | [practice] P | Crossref |
| 1979 | "Philip Gill and Walter Murray joined SOL in 1979 from the National Physical Laboratory in Teddington, England" | [stated, collective] P | Gill et al. 2008 essay, p. 153 |
| 1980 | "A Numerical Investigation of Ellipsoid Algorithms for Large-Scale Linear Programming" (Gill, Murray, Saunders, Wright), DTIC report ADA093617, 1980. No journal paper followed (see §3, T3) | [practice] S (OpenAlex W1500330311) | OpenAlex |
| 1981 | *Practical Optimization* (Gill, Murray, Wright), Academic Press 1981. SIAM Classics reissue 2019, DOI 10.1137/1.9781611975604 | [practice] P/S | DBLP; Open Library; Crossref |
| 1982–86 | NPSOL. Gill's own 2011 timeline gives "1982 NPSOL, G, Murray, Saunders & Wright (and Sven!)". The user's guide for version 4.0 appeared in 1986 (DOI 10.21236/ADA169115) | [stated] P; [practice] P | 2011 slides, slide 6; Crossref |
| 1984–86 | Karmarkar episode → "On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method" (with Tomlin), *Math. Prog.* 36 (1986) 183–209, DOI 10.1007/BF02592025 | [practice] P | Crossref; essay pp. 154–155 |
| 1987 | SOL 87-9 "Shifted Barrier Methods for Linear Programming" and SOL 87-12 "A Schur-Complement Method for Sparse Quadratic Programming" (homepage R37 and R36). No journal version of 87-9 was found | [practice] P | homepage *Technical Reports* |
| 1988 | "At UCSD since 1988" | [practice] P | homepage *In Person* |
| 1991 | *Numerical Linear Algebra and Optimization*, vol. 1 (Gill, Murray, Wright), Addison-Wesley 1991. SIAM reissue 2021, DOI 10.1137/1.9781611976571. Volume 2 was never written (§5) | [practice] S (Open Library) / P (Crossref) | Open Library; Crossref |
| 1991 | "Inertia-Controlling Methods for General Quadratic Programming", *SIAM Rev.* 33 (1991) 1–36, DOI 10.1137/1033001. SOL reports 91-3 and 91-7 still appear three years after the move | [practice] P | Crossref; homepage R34–R35 |
| 1992 | Start of SNOPT: "1992– SNOPT, G, Murray & Saunders '97" (slide 6). Same year: AIAA paper with McDonnell Douglas engineers, "The application of nonlinear programming and collocation to optimal aeroassisted orbital transfers" (Gill, Murray, Shi, Nelson, Young, Saunders), 30th Aerospace Sciences Meeting, DOI 10.2514/6.1992-734 | [stated] P; [practice] P | slides; Crossref |
| 1992 | "Preconditioners for Indefinite Systems Arising in Optimization", *SIMAX* 13 (1992) 292–311, DOI 10.1137/0613022 (interior-method KKT linear algebra) | [practice] P | Crossref |
| 1993 | First UCSD PhD graduate (Braunstein, July 1993). The two earlier students on his list are Stanford OR students (1981, 1986) | [practice] P | homepage *Graduate Students* |
| 1994 | "Large-scale SQP Methods and their Application in Trajectory Optimization", in *Computational Optimal Control* (1994) 29–42, DOI 10.1007/978-3-0348-8497-6_3 | [practice] P | Crossref |
| 1995 | "Primal–dual methods for linear programming", *Math. Prog.* 70 (1995) 251–277, DOI 10.1007/BF01585940. NSF DMI-9424639 "Large-Scale Constrained Optimization" (1995–98) | [practice] P | Crossref; homepage *Grants* |
| 1995–99 | UCSD subcontract on NSF CCR-9527151 (PI L. R. Petzold): "optimization and control of chemical and biological processes". Leads to the DASOPT and optimal-control SQP papers, e.g. *J. Comput. Appl. Math.* 120 (2000) 197–213, DOI 10.1016/S0377-0427(00)00310-1 | [practice] P | homepage *Grants*; Crossref |
| 1997 | SNOPT 5.3 and SQOPT 5.3 user's guides (NA 97-5, NA 97-4) | [practice] P | homepage R31–R32 |
| 1998 | Forsgren & Gill, "Primal-Dual Interior Methods for Nonconvex Nonlinear Programming", *SIOPT* 8 (1998) 1132–1152, DOI 10.1137/S1052623496305560 | [practice] P | Crossref |
| 2000–03 | NSF ACI-0082100 "Innovative Software for Large-Scale Nonlinear Optimization" | [practice] P | homepage *Grants* |
| 2001 | SnadiOpt, a package that adds automatic differentiation to SNOPT: arXiv cs/0106051 | [practice] P | arXiv; DBLP |
| 2002 | SNOPT journal paper, *SIOPT* 12 (2002) 979–1006, DOI 10.1137/S1052623499350013. Survey "Interior Methods for Nonlinear Optimization" (with Forsgren and M. H. Wright), *SIAM Rev.* 44 (2002) 525–597, DOI 10.1137/S0036144502414942 | [practice] P | Crossref |
| 2002–08 | PDE-constrained optimization grants: NSF DMS-0208449 (2002–05) and DMS-0511766 (2005–08), co-PIs Bank, Cheng, Holst. NASA Goddard NAG5-12312 (2002–03). Northrop Grumman "SNOPT for Real Time Trajectory Generation of Constrained Dynamical Systems" (2005–06) | [practice] P | homepage *Grants* |
| 2003 | IOTR 1.0, "a C++ Interior-Point Package for Large-Scale Nonlinear Programming" (NA 03-1, with Gertz and Griffin) | [practice] P | homepage R25 |
| Jan 2004 | Talk at the SVG60 meeting, Stanford, 9–10 Jan 2004: "On unconstrained optimization and other Blasts from the Past..." | [practice] S | SVG60 program page |
| 2005 | SNOPT SIGEST, *SIAM Rev.* 47 (2005) 99–131, DOI 10.1137/S0036144504446096 | [practice] P | Crossref |
| 2005–11 | Applied collaborations: tensegrity (*IJSS* 42 (2005), DOI 10.1016/j.ijsolstr.2005.01.014; 43 (2006), DOI 10.1016/j.ijsolstr.2005.07.046), state estimation in physics (*Phys. Lett. A* 372 (2008), DOI 10.1016/j.physleta.2007.12.051), video restoration (*IEEE TIP* 20 (2011) 3097–3111, DOI 10.1109/TIP.2011.2158229) | [practice] P | Crossref |
| 2008 | Gill et al., "George B. Dantzig and systems optimization", *Discrete Optim.* 5 (2008) 151–158, DOI 10.1016/j.disopt.2007.01.002 (retrospective) | [stated, collective] P | Crossref; full text |
| 2008– | "the SQP renaissance" (his own label, slide 6). Reports: NA 08-2 "A Primal-Dual Augmented Lagrangian" → *COAP* 51 (2012; online 2010) 1–25, DOI 10.1007/s10589-010-9339-1 | [stated] P; [practice] P | slides; homepage R20; Crossref |
| Aug 2010 | Gill & Wong, "Sequential Quadratic Programming Methods" (NA 10-03) → IMA Vol. 154, DOI 10.1007/978-1-4614-1927-3_6 (online 2011) | [practice] P | report; Crossref |
| 5 Jul 2011 | Talk "What's New in Active-Set Methods for Nonlinear Optimization?", Manchester, workshop in honour of Sven Hammarling. Gill narrates the SQP decline and renaissance there | [stated] P | slides (54 pp.) |
| 2013 | Gill & Robinson, "A Globally Convergent Stabilized SQP Method", *SIOPT* 23 (2013) 1983–2010, DOI 10.1137/120882913 | [practice] P | Crossref |
| 18 Feb 2014 | 28th Simon Stevin Lecture on Optimization in Engineering, KU Leuven: "Numerical Linear Algebra and Optimization" | [stated] P (abstract) | KU Leuven OPTEC page |
| 2014–15 | Gill & Wong, "Methods for convex and general quadratic programming", *Math. Prog. Comp.* 7 (2015; online Aug 2014) 71–112, DOI 10.1007/s12532-014-0075-x (the basis of SQIC). Gill, Saunders & Wong, "On the Performance of SQP Methods for Nonlinear Optimization", Springer PROMS 147 (2015) 95–123, DOI 10.1007/978-3-319-23699-5_5, which announces "the forthcoming SNOPT9" (preprint p. 26) | [practice] P; [stated] P | Crossref; preprint |
| 2015 | Bienstock, Gill & Gould, "A note on 'On fast trust region methods for quadratic models with linear constraints', by Michael J.D. Powell", *Math. Prog. Comp.* 7 (2015) 235, DOI 10.1007/s12532-015-0085-3 | [practice] P | Crossref |
| 2016–17 | Stabilized SQP with Kungurtsev and Robinson: *IMA JNA* 37 (2017) 407–443, DOI 10.1093/imanum/drw004; *Math. Prog.* 163 (2017) 369–410, DOI 10.1007/s10107-016-1066-7. Forsgren, Gill & Wong, *Math. Prog.* 159 (2016) 469–508, DOI 10.1007/s10107-015-0966-2 (arXiv 1503.08349) | [practice] P | Crossref; arXiv |
| 2017–18 | DNOPT user's guide (CCoM 17-3). SNOPT 7.7 user's guide (CCoM 18-1, with Murray, Saunders, Wong) | [practice] P | UCSD optimizers site |
| 2018–21 | Applied co-authorships: optimal control with hyperbolic PDEs (*DCDS-S* 11 (2018) 1259–1282, DOI 10.3934/dcdss.2018071), seismic design (*CMES* 120 (2019) 517–543, DOI 10.32604/cmes.2019.06269), path planning (AIAA SciTech 2020, DOI 10.2514/6.2020-0987) | [practice] P | Crossref |
| 2019, 2021 | SIAM Classics reissues of both books (DOIs above) | [practice] P | Crossref |
| 2020 | Gill, Kungurtsev & Robinson, "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", *SIOPT* 30 (2020) 1067–1093, DOI 10.1137/19M1247425 | [practice] P | Crossref |
| 2021–23 | Graduate teaching: Math 277A (Spring 2021), 271A/B/C (2021–22), 202A (Fall 2022), 171A (Winter 2023). **Winter 2023 is the last quarter listed** | [practice] P | homepage *Teaching* |
| Jul 2022 – Oct 2023 | Gill & Runnoe, "On Recent Developments in BFGS Methods for Unconstrained Optimization", CCoM 22-04, "July 1, 2022, Revised October 17, 2023" (report only) | [practice] P | report p. 1 |
| Oct 2022 | Last Optimization Online posting: "A Projected-Search Interior Method for Nonlinear Optimization" | [practice] P | Optimization Online author page |
| 2023–24 | Projected search: Ferry, Gill, Wong & Zhang, *OMS* 39 (2024; online 18 Aug 2023) 459–488, DOI 10.1080/10556788.2023.2241769 (arXiv 2110.08359). Gill & Zhang, *COAP* 88 (2024; online 21 Feb 2024) 37–70, DOI 10.1007/s10589-023-00549-1 | [practice] P | Crossref; arXiv |
| Jun–Aug 2023 | Four PhD graduates in one summer: Z. Zhu (June), M. Zhang (June), Guldemond (July), Huang (August) | [practice] P | homepage *Graduate Students* |
| 11 Dec 2023 | Last arXiv submission: Brust & Gill, "An LDLᵀ Trust-Region Quasi-Newton Method", arXiv 2312.06884 | [practice] P | arXiv search |
| Jun 2024 | Last PhD graduate listed: Jeb Runnoe | [practice] P | homepage |
| 17 Oct 2024 | **Latest dated publication found**: Brust & Gill, *SISC* 46 (2024) A3330–A3351, DOI 10.1137/23M1623380 | [practice] P | Crossref; DBLP; S2 |
| undated (as of 2026-09-28) | Title "Emeritus Professor, Mathematics" on UCSD Profiles. The homepage still says "Distinguished Professor of Mathematics" | [practice] S / P | UCSD Profiles; homepage |
| undated | Honours on the UCSD Mathematics profile: "Fellow of the Society for Industrial and Applied Mathematics", "NSF SCREMS Award", "Member of the Stanford University Inventor Hall of Fame". Also on the homepage: "Senior Fellow, San Diego Supercomputer Center". SIAM Fellow year: a WebSearch summary says 2014, **not confirmed by a primary source** (see Contradictions and Gaps) | [practice] P (institutional pages) | UCSD Math profile; homepage |
| undated (as of 2026-09-28) | SNOPT site: latest listed release **SNOPT 7.7.4**. "SNOPT 9: Currently in development. Simplified user interface. Can use exact second derivative information. Updated QP subproblem solver SQIC. Written in Fortran 2003" | [stated] P | ccom.ucsd.edu/~optimizers (SNOPT page and Reference Guide) |
| undated (as of 2026-09-28) | Still listed as SOL personnel: "Philip Gill (University of California, San Diego)" | [practice] P | Stanford SOL personnel page |

---

## 2. Lineage

Summary only. 04-mentorship §1 has the full, DOI-checked table.

- **Upward**: advisors Walter Murray and David Q. Mayne (MGP) [practice, S]. Murray stayed his closest co-author from 1972 to 2021; 01-publications gives 96 joint OpenAlex records. So the advisor did not become a senior patron; he became a lifelong peer [practice, P bibliographic].
- **Intellectual influences named by the group**: "in addition to GBD, Martin Beale (Imperial College), Gene Golub (Stanford), and Jim Wilkinson (National Physical Laboratory) influenced the early SOL work on numerical software by the present authors" (2008 essay, p. 153) [stated, collective, P]. The Golub link is also in print: Golub is a co-author of the 1974 factorization-updating paper (Crossref).
- **Downward** (the thesis titles used in the table below were checked on MGP student pages in this run): the homepage lists 25 PhD students (Nov 1981 to Jun 2024) and 4 postdocs, each of them a former student of his: Gertz 1999–2000, Leonard 2002–03, Erway 2006–07, Wong 2011–15 [practice, P]. MGP lists 22 students, including Kuhlmann (Bremen 2018, co-advised), who is not on the homepage [practice, S].
- **Student output by period** [practice, P; the reading is inferred]:

  | Period | Students | Topics |
  |---|---|---|
  | 1993–99 | 5 | phase-one LP, KKT interior methods, reduced-Hessian quasi-Newton, trust-region/line-search, SQP for control |
  | 2002–07 | 6 | interior methods, trust-search, PDE-constrained optimization, trust-region subproblems, primal-dual augmented Lagrangian |
  | 2011–15 | 6 | projected search, QP active-set, PDE, stabilized SQP, cognitive-science co-advising, interior QP |
  | 2019–24 | 6 | path-following, projected search, trust-region interior methods, second-derivative SQP |

  Four students finished in summer 2023 and one in 2024. That looks like a cohort finished out before emeritus status [inferred; the emeritus date was not found].
- **Grand-students coming back into the line**: Johannes J. Brust (PhD UC Merced 2018, under Gill's graduate Roummel Marcia, per MGP) is Gill's co-author on the 2023–24 LDLᵀ paper [practice; P for the paper, S for the lineage].

---

## 3. Turns in direction: triggers, timing, resource context

Each turn gives: what changed, what triggered it (with its tag), when he entered or left relative to the field's consensus, and the era and resources at the time.

### T1. NPL, 1970s: optimization built on stable factorization updates

- **What**: quasi-Newton methods that "recur" a factorization of the Hessian approximation. The 1972 abstract: the method "is based on recurring the factorization of an approximation to the Hessian matrix. Knowledge of this factorization allows greater flexibility when choosing the direction of search while minimizing the adverse effects of rounding error" (*IMA J. Appl. Math.* 1972, abstract via OpenAlex) [stated, P]. The same idea was then generalized in "Methods for modifying matrix factorizations" (1974) and carried into QP (1978) and nonlinear least squares (1978) [practice, P].
- **Trigger**: [inferred] the NPL numerical-analysis culture of Wilkinson's laboratory. The group names Wilkinson as an influence (essay p. 153 [stated]). This is the trigger for the *style* of the work, not for any one paper; no first-hand account of how the topic was chosen was found.
- **Timing**: [inferred] contemporary with the quasi-Newton mainstream (DFP/BFGS, 1963–70). His distinctive contribution was the numerically stable *implementation*, not the update formula.
- **Resources**: a government laboratory where, according to Wright, "you could just do the research you wanted … it didn't have to make a product it didn't have to make money" [sic] (interview lines 189–191) [observed, S]. Team: Gill and Murray, with Picken, and Wright visiting. The library-design paper of 1979 targets "a Fortran program library for optimization" (its title) [practice, P]. The link from that paper to the NAG Library comes from 01-publications and was not re-checked here.

### T2. The 1979 move to Stanford SOL

- **What**: Gill and Murray moved from NPL to Dantzig's SOL. With Saunders (back in 1979) and Wright (at SOL since 1976), they formed what the essay calls the Stanford SOL "gang of four" (arrival dates p. 153, the name p. 154) [stated, collective, P].
- **Trigger, push**: according to Wright, "Philip and Walter had become increasingly unhappy with the NPL … the bosses changed the view they said no no the people that work here have to make contributions to British industry and they have to you know find business customers … they said we don't like it we don't want to be here" [sic] (lines 187–193) [observed, S].
- **Trigger, pull**: "George had already expressed a strong interest in having a bigger group" (Wright, line 193) [observed, S]. The essay's account of Dantzig's programme is that a "critical mass" was needed so that "Software implementing these methods can be written and systematically tested on representative problems" (p. 152) [stated, collective, P].
- **Resource context**: Wright says she was hired "as a senior research associate not a faculty member" (line 179) [observed]. **Gill's own SOL rank is not stated** in any source I read. Software was funded by stealth: Dantzig "managed to do so by bootstrapping grants in optimization that emphasized mathematical theory without mentioning any of the software-related activities" (essay p. 153) [stated, collective, P].
- [inferred] **Pattern**: the move was toward freedom to do curiosity-driven method-and-software research, away from pressure to serve industry customers. Later his group took industrial *users* seriously (Boeing, Northrop Grumman), but as sources of hard problems, not as customers directing the work.

### T3. Khachiyan (1979–80): entered at once, left at once, did not publish the negative result as a paper

- **Trigger**: an external theoretical shock (Khachiyan's 1979 polynomial-time result).
- **Practice**: "Stanford SOL researchers were among the earliest to investigate the performance of the ellipsoid algorithm applied to linear programs, and (as is now well-known) the method turned out to be extremely slow in practice" (essay p. 154) [stated, collective, P]. There is a 1980 DTIC report, "A Numerical Investigation of Ellipsoid Algorithms for Large-Scale Linear Programming" (ADA093617) [practice, S (OpenAlex); not read].
- **Exit**: Wright: "it was always always in our examples way slower than the simplex method … it was not even a contender so we didn't ever write a paper about this in retrospect I wish we had because we had lots of numerical results" [sic] (lines 241–243) [observed, S].
- **Timing**: [inferred] entered with the crowd, left **before or with** the consensus. The group's own benchmark verdict came early.
- See Contradictions, item 2: Wright says there was no paper, but a DTIC report exists.

### T4. Karmarkar (1984) → barrier and interior methods: entered **before** the consensus

- **Trigger**: an external shock (Karmarkar's announcement) meeting expertise the group held but the field had dropped. The group's co-authored survey states the field's view of the time: "By the early 1980s, barrier methods were almost without exception regarded as a closed chapter in the history of optimization" (Forsgren, Gill & Wright 2002, abstract via Crossref) [stated, P]. The essay: "the SOL researchers, trained in nonlinear optimization in general and barrier methods in particular [23,24], observed the strong similarity between the equations in Karmarkar's method and those arising in the 1960s logarithmic barrier method of Fiacco and McCormick" (p. 154) [stated, collective, P].
- **Why then, and why them**: Wright: "if karma curse thing had happened a few years later I'm not sure there would have been anybody who really knew about barrier methods" [sic; "Karmarkar's thing"] (line 259) [observed, S].
- **Practice**: "By the summer of 1985 … [they] had proved that there was a formal mathematical connection between Karmarkar's method and the log barrier method. In addition, a 'projected Newton barrier' code had been written and compared with the simplex method (as implemented in MINOS) on a suite of representative LPs … To the surprise of many (including the authors of this paper), the nonlinear barrier method was obviously competitive with the simplex method, providing the first confirmation outside AT&T of the promise of barrier-based methods for LP" (essay pp. 154–155) [stated, collective, P]. Published as *Math. Prog.* 36 (1986), DOI 10.1007/BF02592025 [practice, P].
- **Follow-on and exit pattern**: he stayed in interior methods from the linear-algebra side:
  - SOL 87-9 shifted barrier;
  - KKT preconditioners (1992);
  - primal–dual LP (1995);
  - quasidefinite and ill-conditioned systems (1996);
  - nonconvex primal–dual interior methods (1998);
  - the 2002 survey;
  - IOTR (2003);
  - the 2020 shifted penalty-barrier method.

  [practice, P] He never left interior methods. His production solver stayed SQP, though; IOTR is not on the current software site [practice, P (site checked 2026-09-28)].
- **Resources**: a four-person staff team plus Tomlin, and a PhD student (Lustig) helping (essay p. 154). MINOS already existed in the group and served as the baseline [stated, P].

### T5. The 1988 move to UCSD Mathematics

- **What**: "At UCSD since 1988" (homepage) [practice, P]. SOL technical reports continue to 1991 (SOL 91-3, 91-7; homepage R34–R35), and the earliest UCSD report on his *selected* reports list is NA 95-1 (QPOPT, 1995) [practice, P]. SOL still lists him as personnel today [practice, P].
- **Trigger**: **not found**. No statement by Gill was found.
  - Context [observed, S]: Wright left SOL "around 1988" for Bell Labs because "in the o.r department there was no possibility that I would ever get to be a research faculty member … in 20 years am I still going to be here as a research associate" [sic] (lines 305–313).
  - [inferred, weak] If Gill held a similar non-faculty post at SOL (his rank there is **not stated** in any source I read), a move to a faculty chair may have had a similar motive. This is **not** evidenced for Gill.
- **Effect on the research** [inferred from dates]: the move turned Gill from a staff member of a four-person team into a faculty PI with PhD students (first UCSD graduate 1993). In DBLP the last Gill–Murray–Saunders–Wright research paper is the 1991 *SIAM Review* QP paper. After that the four appear together only on the NPSOL 5.0 guide (NA 98-2, 1998) and the 2008 essay; Gill, Murray and Wright together on the book reissues (2019, 2021). The three-way Gill–Murray–Saunders software line (SNOPT, SQOPT, QPOPT) continued across Stanford and San Diego.

### T6. The 1990s: building a sparse SQP code while, by his own account, SQP research declined

- **Stated trend**: "In the late 1980s/early 1990's, research on SQP methods declined. Three reasons (but interconnected): The rise of interior-point methods / The rise of automatic differentiation packages … Computer architecture evolved" (2011 slides, slide 26) [stated, P].
- **What he did**: started SNOPT in 1992 (slide 6) [stated, P].
- **Trigger**: users hitting a scale wall. "Although NPSOL has solved OTIS examples with as many as two thousand constraints and over a thousand variables, the need to handle increasingly large models has provided strong motivation for the development of new sparse SQP algorithms" (SIGEST 2005, p. 101) [stated, P]. The SIGEST thanks "Dan Young and Rocky Nelson of the Boeing Company (formerly McDonnell Douglas Space Systems …) for their constant support and feedback during the development of SNOPT" (p. 127) [stated, P]. Both names are co-authors of the 1992 AIAA paper (Crossref) [practice, P].
- **Timing**: [inferred] **against the trend**. He kept to SQP through its decline because a concrete user class (aerospace trajectory optimization) needed features that interior methods lacked: warm starts, few function evaluations, and infeasibility handling. The 2011 slides list the "not-so-nice features of IP methods": they "have difficulty exploiting a good solution" and "have difficulty certifying infeasible constraints" (slide 33) [stated, P].
- **Resources**: a UCSD PI with 1–3 students at a time, plus Stanford co-developers. Funding: NSF DMI (1995–98), an NSF CCR subcontract (1995–99), and later aerospace contracts [practice, P].

### T7. The 2000s: consolidation plus a wide periphery

- **Core**:
  - the SNOPT papers (2002 *SIOPT*, 2005 *SIAM Rev.* SIGEST);
  - the interior-methods survey (2002);
  - trust-region work with students (Gertz 2004; Erway & Griffin 2009 ×2) [practice, P].
- **Periphery, each tied to a grant or a local partner**:
  - PDE-constrained optimization (NSF DMS 2002–08, co-PIs Bank, Cheng, Holst);
  - tensegrity (with Skelton, 2005–06);
  - physics and neuroscience state estimation (with Abarbanel, 2008–11);
  - video restoration (with Nguyen, 2011).

  [practice, P] [inferred] The periphery follows **local UCSD collaborators and grants** rather than a planned research agenda. Apart from the PDE-constrained line, none of these became a line of methods papers.
- **Side software that did not last**: SnadiOpt (2001, AD for SNOPT; arXiv cs/0106051) and IOTR 1.0 (2003, a C++ interior package). Neither is distributed on the current UCSD optimizers site, which offers SNOPT, DNOPT, NPSOL, SQOPT and SQIC [practice, P]. "Discontinued" is [inferred].
- [inferred] SnadiOpt is an early practical answer to the AD trend that his 2011 slide 26 later names as one cause of the SQP decline: he tried to bring the new tool into SNOPT, not to leave SQP.

### T8. 2008–: the self-named "SQP renaissance" (second derivatives, regularization, stabilization)

This is the best-documented turn, because Gill narrated it himself.

- **Stated triggers** [stated, P]:
  - **New applications**: "Many important applications require the solution of a sequence of related optimization problems / ODE and PDE-based optimization with mesh refinement / Mixed-integer nonlinear programming / infeasible constraints are likely to occur. The common feature is that we would like to benefit from good approximate solutions" (slide 32). The same trigger is in the NA 10-03 abstract (Aug 2010): "Recent developments in methods for mixed-integer nonlinear programming (MINLP) and the minimization of functions subject to differential equation constraints has led to a heightened interest in methods that may be 'warm started' from a good approximate solution" (p. 1).
  - **New derivatives**: "modeling languages such as AMPL and GAMS started to provide second derivatives automatically" (slide 26). The timeline has "1997– AMPL, GAMS introduce automatic differentiation" (slide 6).
  - **New hardware**: "Methods based on sparse updating are hard to speed up / Reformulate methods to shift the emphasis from sparse matrix updating to sparse matrix factorization / Thereby exploit state-of-the-art linear algebra software / Less reliance on specialized 'home grown' software" (slide 36). Slide 28: "Moore's Law has been 'updated': 'the number of cores (cpus) on a processor will double every 18 months'".
- **Self-set agenda, with a lag**: the SIGEST (2005) already ends with "Future work must take into account the fact that second derivatives are increasingly available. The QP solver should allow for indefinite QP Hessians, and additional techniques are needed to handle even more degrees of freedom" (p. 127) [stated, P]. [inferred] The 2008– programme carries out that paragraph:
  - QP methods for indefinite Hessians and SQIC (Gill & Wong 2014/15);
  - regularized and stabilized SQP (2010–2017);
  - DNOPT (2017).
- **Aims** (slide 35): "to define an SQP method that exploits second derivatives. to provide a globally convergent method that is provably effective for degenerate problems[,] perform stabilized SQP near a solution[,] allow the use of modern sparse matrix packages[,] 'black-box' linear equation solvers" [stated, P].
- **Timing**: [inferred] he entered stabilized SQP about a decade after its local theory (Wright, Hager and others, late 1990s), and his contribution was the *global* method. That is late for the theory, and early among the builders of practical global versions. The dating of the predecessors is from general knowledge of the field and was **not checked in this run**; treat it as a lead.
- **Reversal of a lifelong bet** [inferred]: slide 36 moves the emphasis *away from* the factorization **updating** that defined his work from 1972 (T1) through SNOPT's reduced-Hessian QP solver (slide 24: "The KKT equations are solved by updating factors of AF and the reduced Hessian"). This is a self-revision driven by hardware, not by any theoretical failure.
- **Stated plan vs practice**: the stated move toward "less reliance on … 'home grown' software" (2011) sits next to a practice of still building the group's own QP solver, SQIC. SQIC, however, is "capable of using third-party linear solvers -- interfaces to LUSOL, HSL_MA57, HSL_MA97, UMFPACK are included" (SQIC page) [practice, P]. In 2022 the pdProj prototype factors each KKT matrix "using the Matlab built-in command LDL, which uses the routine MA57". When the inertia is wrong, "the Hessian of the Lagrangian H was modified using the method of Wächter and Biegler [27, Algorithm IC, p. 36]" (Gill & Zhang CCoM 22-01, p. 28) [practice, P]. [inferred] The shift did happen at the linear-solver layer: he now borrows the IPOPT inertia-correction device.
- **An unfulfilled forecast**: 2015: "the forthcoming SNOPT9" (Gill, Saunders & Wong, preprint p. 26) [stated, P]. 2026: "SNOPT 9 Currently in development" (SNOPT page, checked 2026-09-28) [stated, P]. The public release is still SNOPT 7.7.x. That is **at least 11 years** from "forthcoming" with no public release found [practice, P; the reasons were not found].

### T9. 2018–2024: interior–SQP hybrids, projected search, and a return to quasi-Newton

- **Shifted penalty-barrier** (*SIOPT* 2020). The Optimization Online preprint of Jan 2018 was titled "A Shifted Primal-Dual Interior Method for Nonlinear Optimization"; the 2020 journal title says "Penalty-Barrier" [practice, P]. [inferred] The word "shifted" links this to SOL 87-9 "Shifted Barrier Methods for Linear Programming" (1987). **Neither text was read** to confirm it is the same device, so the 33-year link rests on the titles only.
- **Projected search** (2020–2024). The seed is Ferry's 2011 thesis ("Projected-Search Methods for Box-Constrained Optimization", MGP id 154960, checked). It was taken up again from 2020, with M. Zhang and Wong, in the *OMS* 2024 and *COAP* 2024 papers [practice, P]. A roughly 10-year gap from thesis to programme.
- **Return to quasi-Newton after 50 years**:
  - Gill & Runnoe (CCoM 22-04, 2022/2023) run a systematic comparison and conclude: "some newer modifications show little or no improvement, while a novel combination of self-scaling and a factored Hessian shows significant and consistent improvement. (Surprisingly, most authors in the optimization community have dismissed factored Hessian methods; see, e.g., Grandinetti [12,13] Nocedal and Wright [16, p. 201].)" (p. 37) [stated, P].
  - Brust & Gill (2024) cite "Gill & Murray [25]", the 1972 paper, as the origin of the LDLᵀ approach, and note that such factorizations "have been used extensively in the implementation of line-search quasi-Newton methods … but they are seldom used in trust-region quasi-Newton methods" (CCoM 23-01, p. 3) [stated, P].
  - [inferred] This is a deliberate return to his first topic, framed as a correction of the community's neglect. It is also a return to the "updating" style that slide 36 had moved away from, but for dense, small-to-medium unconstrained problems, where the multicore argument matters less.
- **Tooling in this era** [practice, P]:
  - the BFGS report's solvers were "written in MATLAB version R2019b", and its analysis "in Python using Numpy, Pandas, Matplotlib and Seaborn" on "a 2017 MacBook Pro" (CCoM 22-04, section 5.2);
  - pdProj ran on "Matlab version R2022b on an iMac Pro" (CCoM 22-01, p. 29);
  - the 2015 SNOPT vs IPOPT study ran on "a MacPro configured with a 2.7GHz 12-core Intel Xeon E5 processor and 64GB of RAM" (preprint p. 6).

  This is desktop-scale experimentation throughout, with Matlab prototypes and Fortran production codes.

### T10. Wind-down (2023–)

- **Evidence** [practice, P unless marked]:
  - last teaching quarter listed: Winter 2023;
  - last PhD graduate: June 2024;
  - last arXiv submission: 11 Dec 2023;
  - last Optimization Online post: Oct 2022;
  - latest publication: 17 Oct 2024;
  - title now "Emeritus Professor" on UCSD Profiles [S].
- [inferred] A gradual close: a cohort of students is finished out (5 graduates, 2023–24), then no new papers. **Whether he is retired, emeritus but still researching, or working unpublicly on SNOPT 9 cannot be told from the public record.**

---

## 4. Entering and leaving topics, relative to the consensus

| Topic | Entered | Left or current | Relative to the consensus | Basis |
|---|---|---|---|---|
| Factorized quasi-Newton / Newton | 1972 | returned 2022–24 | with the mainstream on the formulas; he led on stable implementation. The 2022 return is explicitly **against** the community's dismissal | [practice]; GR22 p. 37 [stated] |
| Stable QP / active-set | 1978 | ongoing to 2016 (SQIC, primal/dual active-set) | stayed in active-set QP after interior QP became popular | [practice] |
| General-purpose SQP (NPSOL) | 1982 | ongoing | entered in the "salad days" (his slide 6: "1975–84 the SQP 'salad days'"); **stayed through the decline** | [stated] + [practice] |
| Ellipsoid method | 1979–80 | 1980 | tested with the crowd, left early on benchmark evidence | [stated, collective]; [observed] |
| Barrier / interior methods | 1984–85 | ongoing (2020–24 hybrids) | **before the consensus**, from expertise the field had abandoned | [stated, collective] |
| Sparse large-scale SQP (SNOPT) | 1992 | ongoing (SNOPT 9 in development) | **against the trend** he himself describes | [stated] |
| Trust-region subproblems | ~1999 (Gertz) | 2009; returned 2023–24 | followed the established trust-region school; returned with LDLᵀ | [practice] |
| PDE-constrained optimization | 2002 | ~2011 (last related thesis, Reed 2011); applied items 2018, 2021 | entered when the area grew, tied to local co-PIs and grants; not continued as a methods line | [practice]; the reason for leaving was not found |
| Regularized / stabilized SQP | 2008 | 2020 | after the local theory, early among global practical methods | [stated] + [inferred] |
| Projected search | 2011 (thesis) | 2024 | revived a classical (Bertsekas-type) device for new settings. The history claim was not checked | [practice] |

---

## 5. Failures, abandoned directions, unfulfilled plans

| Item | What happened | Tag / source |
|---|---|---|
| Ellipsoid method (1979–80) | Tested, "way slower than the simplex method". No journal paper, a report only (DTIC ADA093617, 1980). Wright regrets not publishing | [observed] Wright lines 241–243; [stated, collective] essay p. 154; [practice] OpenAlex |
| *Numerical Linear Algebra and Optimization*, vol. 2 | Never written. Wright: "someone said let's just put volume and then we can finish later well of course we didn't if on to never came out" [sic; "volume two never came out"] (lines 331–333) | [observed] S |
| Shifted barrier LP (SOL 87-9, 1987) | No journal version found | [practice] P (homepage R37; DBLP) |
| SnadiOpt (2001), IOTR (2003) | Manuals published; the codes are not on the current distribution site | [practice] P; "abandoned" [inferred] |
| SNOPT 9 | "forthcoming" in 2015; "Currently in development" in 2026 | [stated] P, both dates |
| Optimization Online 2013/10 "A Regularized SQP Method with Convergence to Second-Order Optimal Points" | No journal version located by 01-publications or in DBLP (checked here) | [practice] P |
| Gill & Runnoe BFGS report (CCoM 22-04, rev. Oct 2023) | Report only. No journal version in Crossref, DBLP or S2 as of 2026-09-28 | [practice] P |
| Peripheral application lines (tensegrity, neuroscience, video) | Each produced 1–3 papers and ended | [practice] P; "ended" means no later item found |

---

## 6. Latest activity (window 2025-09-28 to 2026-09-28)

**Nothing new was found for the last 12 months.** The checks, all run on 2026-09-28:

| Source | Latest item | Result for the window |
|---|---|---|
| DBLP pid 04/4552 (SPARQL; 43 records) | 2024: *SISC* 46, *COAP* 88, *OMS* 39 | none |
| OpenAlex author A5003732991, `counts_by_year` | 2024: 3 works | none for 2025 or 2026 |
| OpenAlex works filter from 2024-06-01 | 1 work (SISC, 2024-10-17) | none |
| Semantic Scholar author 1744288 (147 papers) | 2024-10-17 | none |
| Crossref author searches (Gill plus each of Brust, Wong, Zhang, Kungurtsev, Robinson, Saunders, Murray, Forsgren; from 2024-10-01) | 2024-10-17 | none |
| arXiv author search "Gill, Philip E" | 2312.06884 (11 Dec 2023) | none |
| Optimization Online author page | Oct 2022 | none |
| Homepage refereed articles / reports | A1 = Brust & Gill 2024; R1 = CCoM 23-01 | none |
| Homepage teaching | Winter 2023 | none |
| UCSD optimizers site | SNOPT 7.7.4 (undated); SNOPT 9 "Currently in development" | undated, so it cannot be placed in the window |
| CCoM news | newest item Dec 2019 (2020 RTG winter workshop) | none |
| WebSearch (1 of 2) for 2025–26 talks, emeritus or awards | profile pages only | none |

The **latest dated activity** is the SISC publication of 17 Oct 2024. The latest dated *preprint* activity is the 17 Oct 2023 revision of CCoM 22-04 and the 11 Dec 2023 arXiv posting. Conference programmes for 2025–26 (e.g. ICCOPT 2025, SIAM OP26) were **not checked**. See Gaps.

---

## 7. Era and resource context (per phase)

| Era | Setting | Team | Compute and tools | Seniority |
|---|---|---|---|---|
| 1970–79 | NPL, a government lab, free research until a policy change (Wright) | Gill, Murray; Picken; Wright visiting | Fortran library design (TOMS 1979). No hardware details found | from PhD to peer of his advisor |
| 1979–88 | Stanford SOL, software funded through theory grants (essay p. 153) | Gang of Four plus Tomlin; Stanford OR PhD students | Wright's early-1970s Stanford computing: "a few decks of IBM cards" and a terminal link to SLAC (lines 185, 201–205); MINOS as the in-house baseline; the netlib LP set that SOL helped seed (essay p. 155) | mid-career; Gill's SOL rank not stated (Wright was a "senior research associate") |
| 1988–2007 | UCSD Mathematics / CCoM; NSF and aerospace contracts; SDSC Senior Fellow | faculty PI with 1–3 PhD students; Murray and Saunders remote | Fortran production codes; CUTE/CUTEr, COPS; AMPL/GAMS interfaces (01) | senior faculty |
| 2008–2024 | UCSD; NSF DMS-0915220, DMS-1318480, RTG DMS-1345013 (GR22 p. 1) | Gill plus postdoc/co-author Wong; alumni Robinson, Kungurtsev, Brust | Matlab R2019b/R2022b prototypes; Python analysis (2022); 12-core MacPro (2015); CUTEst; third-party MA57 via Matlab LDL | Distinguished Professor, then emeritus |

---

## 8. Recurring trajectory patterns (candidates for the skill; all [inferred])

1. **Keep unfashionable expertise; strike when a shock arrives.** Barrier methods were a "closed chapter" (2002 survey), and the group still held the expertise in 1984. Basis: T4.
2. **Let a real user's scale wall pick the next system, even against the trend.** Basis: OTIS/NPSOL → SNOPT (T6).
3. **Re-examine the method when the hardware or software ecosystem changes, including your own past bets.** Updating → factorization; second derivatives from AD. Basis: T8, slides 26, 28, 36.
4. **Write your own agenda at the end of the flagship paper, then carry it out over 10 years.** Basis: SIGEST p. 127 → 2008–2017 (T8).
5. **Return to your first topic with modern testing and argue with the consensus.** Basis: 1972 → GR22/BG24 (T9).
6. **A student's thesis is a seed that may lie dormant for about 10 years.** Basis: Ferry 2011 → 2020–24 (T9; 04 §4.6).
7. **The periphery follows local partners and grants; the core does not move.** Basis: T7.
8. **Announced software can slip for a long time.** SNOPT 9, 2015 → 2026. A caution the skill should carry about his group's software timelines, not a method to copy.

---

## Contradictions (kept, not reconciled)

1. **Title today.** The homepage *In Person* page says "Distinguished Professor of Mathematics". UCSD Profiles says "Emeritus Professor, Mathematics". The UCSD Mathematics profile gives neither title. The dates are unknown, and "Distinguished Professor Emeritus" would fit both, but no source says so.
2. **Khachiyan results.** Wright (lines 241–243): "we didn't ever write a paper about this". A 1980 DTIC report on ellipsoid algorithms for large-scale LP by the same four authors exists (OpenAlex W1500330311). Possibly "paper" meant a journal paper. Not read.
3. **SIAM Fellow year.** A WebSearch result summary says he was elected SIAM Fellow in 2014, citing contributions to optimization, linear algebra and software. The primary pages (homepage, UCSD Math profile) give no year. The SIAM pages returned HTTP 403 and the Wayback Machine returned 403. Unconfirmed.
4. **Homepage bibliography vs Crossref**:
   - "A globally convergent stabilized SQP method", homepage "23 (2013), 1083-2010" vs Crossref 1983–2010;
   - "A primal-dual augmented Lagrangian", homepage "47 (2010)" vs Crossref vol. 51 (2012; online Aug 2010);
   - Forsgren–Gill–Wong, homepage "159 (2016), 460-508" vs Crossref 469–508;
   - Webert et al., homepage "6 (2018)" vs Crossref vol. 11.

   I used Crossref for all identifiers.
5. **Stated move away from home-grown software (2011, slide 36) vs practice.** The group went on to build its own QP solver (SQIC) and SNOPT 9. SQIC does accept third-party linear solvers. Kept as a tension: the stated shift applies to the linear-algebra layer, not to the optimization code.
6. **The 2011 move away from "sparse matrix updating" vs the 2022–24 return to factorization *updating*** (factored-Hessian BFGS; LDLᵀ updates). They may be reconciled by problem class (large sparse constrained vs dense unconstrained), but Gill states no such reconciliation in what I read.
7. **Who saw the Karmarkar–barrier link.** Wright claims it; she reports Murray ("I was your adviser") and Saunders ("I knew about it Philip knew about it") (lines 257–259). The 2008 essay credits "the SOL researchers" collectively (p. 154).
8. **Student counts.** The homepage lists 25 PhD students; MGP lists 22, including Kuhlmann, who is not on the homepage (details in 04).
9. **DNOPT guide year.** The DNOPT page's BibTeX gives CCoM 17-3 with `YEAR = {2017}`; a (commented-out) BibTeX block on the downloads page gives `YEAR = {2016}` for the same guide. Minor, unresolved.

## Gaps (what I could not find)

- **Why he moved from Stanford to UCSD in 1988**: no statement by Gill or anyone else. The only context is Wright's reason for her own departure.
- **When he became emeritus**: not found. The UCSD emeriti list loads dynamically and returned no names to curl or WebFetch.
- **Honours with dates and citations**: the SIAM Fellow year (SIAM site 403; Wayback 403). The Stanford University Inventor Hall of Fame (year, the invention cited, presumably SNOPT or NPSOL, is unconfirmed). Stanford OTL guessed URLs gave 404. No other prizes turned up in two WebSearch calls. **I did not search** individually for named prizes (e.g. the Beale–Orchard-Hays or Dantzig prizes), so "none found" is not "none".
- **Early life, undergraduate training, and when he started at NPL**: only "Diploma of Imperial College, 1971" and "Ph.D. … 1974" were found. Whether the PhD was done while employed at NPL is not stated anywhere I read.
- **Talks from 2024 to 2026**: conference programmes (ICCOPT 2025, SIAM OP26, ISMP 2024) were not checked. Google Scholar returned a CAPTCHA; the github.com/snopt organisation returned 403, so no commit dates for SNOPT 9 are available.
- **SNOPT release dates**: the 7.7.x "What's New" list is undated.
- **Why the PDE-constrained line and the application lines ended**: no source.
- **The 1987 and 2020 "shifted" methods**: not read, so whether they share a device is unverified.
- **Stabilized-SQP predecessors' dates** (used in the T8 timing claim): not checked in this run.
- **The status of Walter Murray**, his lifelong collaborator: not checked.
- **The 1974 Academic Press book**: whether Gill and Murray were editors or authors was not checked.

## Sources

1. P. E. Gill, homepage, *In Person* (Personal.html), https://ccom.ucsd.edu/~peg/Personal.html, fetched 2026-09-28. Primary.
2. P. E. Gill, homepage, *Selected published and accepted papers* (Papers.html), https://ccom.ucsd.edu/~peg/Papers.html, fetched 2026-09-28. Primary.
3. P. E. Gill, homepage, *Selected Technical Reports* (Reports.html), https://ccom.ucsd.edu/~peg/Reports.html, fetched 2026-09-28. Primary.
4. P. E. Gill, homepage, *Graduate Students* (Students.html), fetched 2026-09-28. Primary.
5. P. E. Gill, homepage, *Post-Docs* (Postdocs.html), fetched 2026-09-28. Primary.
6. P. E. Gill, homepage, *Research Grants* (Grants.html), fetched 2026-09-28. Primary.
7. P. E. Gill, homepage, *Teaching* (Teaching.html), fetched 2026-09-28. Primary.
8. P. E. Gill, homepage, *Research Interests* (Interest.html), fetched 2026-09-28. Primary.
9. Mathematics Genealogy Project, "Philip Edward Gill" (id 6811), https://www.mathgenealogy.org/id.php?id=6811, plus student pages 154960 (Ferry), 208003 (Reed), 343635 (Runnoe), 343633 (Guldemond), 343637 (Huang), 343634 (Su), 208002 (Shustrova), 101643 (Winkelmann), 79325 (Kroyan) and 60147 (Marcia, for Brust), fetched 2026-09-28. Secondary.
10. DBLP, person 04/4552 "Philip E. Gill", via SPARQL (`scripts/dblp_works.py`), 43 records, https://dblp.org/pid/04/4552.html, fetched 2026-09-28. Primary (bibliographic).
11. OpenAlex, author A5003732991 (`counts_by_year`) and a works filter from 2024-06-01, plus works W1500330311 and W1483815626, https://api.openalex.org, queried 2026-09-28. Secondary.
12. Semantic Scholar Graph API, author 1744288 (147 papers), queried 2026-09-28. Secondary.
13. Crossref REST API: metadata for every DOI cited above (43 checked, see the scratch log) plus author searches from 2024-10-01, https://api.crossref.org, queried 2026-09-28. Secondary (bibliographic).
14. arXiv, author search "Gill, Philip E" (4 results: 2312.06884, 2110.08359, 1503.08349, cs/0106051), https://arxiv.org/search/?query=Gill%2C+Philip+E&searchtype=author, fetched 2026-09-28. Primary (bibliographic).
15. Optimization Online, author page "pgill", https://optimization-online.org/author/pgill/, fetched 2026-09-28. Primary.
16. UCSD Optimization Software site: home, SNOPT, DNOPT, SQIC and downloads pages, and the SNOPT7 Reference Guide introduction ("What's New in SNOPT"), https://ccom.ucsd.edu/~optimizers/, fetched 2026-09-28. Primary.
17. UCSD Department of Mathematics, profile "Philip Gill" (honours list), https://www.math.ucsd.edu/people/profiles/philip-gill, fetched 2026-09-28. Primary (institutional).
18. UCSD Profiles, "Philip Gill" ("Emeritus Professor, Mathematics"), https://profiles.ucsd.edu/philip.gill, fetched 2026-09-28. Secondary (institutional aggregator).
19. Stanford SOL, Personnel page, https://web.stanford.edu/group/SOL/home_personnel.html, fetched 2026-09-28. Primary (institutional).
20. Stanford SOL, "The SVG Meeting: A Celebration", 9–10 Jan 2004, home and program pages, https://web.stanford.edu/group/SOL/svg60/, fetched 2026-09-28. Secondary.
21. KU Leuven OPTEC, "28th Simon Stevin Lecture … 'Numerical Linear Algebra and Optimization', Philip E. Gill", 18 Feb 2014, https://set.kuleuven.be/optec/event-repository/simon-stevin-lecture-philip-e.-gill, fetched 2026-09-28. Primary (abstract) / secondary (host's bio).
22. P. E. Gill, "What's New in Active-Set Methods for Nonlinear Optimization?", slides, Advances in Numerical Computation (in honour of Sven Hammarling), Manchester, 5 Jul 2011, http://www.cl.eps.manchester.ac.uk/medialand/maths/archived-events/workshops/www.mims.manchester.ac.uk/events/workshops/ANC11/peg.pdf, read in full 2026-09-28. Primary.
23. P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, M. H. Wright, "George B. Dantzig and systems optimization", *Discrete Optimization* 5 (2008) 151–158, DOI 10.1016/j.disopt.2007.01.002, read at https://ccom.ucsd.edu/~peg/papers/gbd.pdf. Primary (collective).
24. P. E. Gill, W. Murray, M. A. Saunders, "SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization", *SIAM Review* 47 (2005) 99–131, DOI 10.1137/S0036144504446096. PDF https://web.stanford.edu/group/SOL/papers/SNOPT-SIGEST.pdf; pp. 101 and 127 read. Primary.
25. P. E. Gill, M. A. Saunders, E. Wong, "On the Performance of SQP Methods for Nonlinear Optimization", CCoM 15-01 / Springer PROMS 147 (2015) 95–123, DOI 10.1007/978-3-319-23699-5_5. Preprint http://www.ccom.ucsd.edu/~peg/papers/mopta.pdf; pp. 6 and 26 read. Primary.
26. P. E. Gill, E. Wong, "Sequential Quadratic Programming Methods", NA 10-03, Aug 2010 (IMA Vol. 154, DOI 10.1007/978-1-4614-1927-3_6), http://www.ccom.ucsd.edu/~peg/papers/sqpReview.pdf; pp. 1–3 read. Primary.
27. P. E. Gill, J. H. Runnoe, "On Recent Developments in BFGS Methods for Unconstrained Optimization", CCoM 22-04 (1 Jul 2022, rev. 17 Oct 2023), http://www.ccom.ucsd.edu/~peg/papers/bfgsdev.pdf; p. 1, §5.2 and p. 37 read. Primary.
28. J. J. Brust, P. E. Gill, "An LDLᵀ Quasi-Newton Trust-Region Method", CCoM 23-01 (Nov 2023; arXiv 2312.06884; SISC 46 (2024), DOI 10.1137/23M1623380), http://www.ccom.ucsd.edu/~peg/papers/trustRegionQN.pdf; pp. 1–3 read. Primary.
29. P. E. Gill, M. Zhang, "A Projected-Search Interior Method for Nonlinear Optimization", CCoM 22-01 (COAP 88 (2024), DOI 10.1007/s10589-023-00549-1), http://www.ccom.ucsd.edu/~peg/papers/pdprojReport.pdf; pp. 28–29 read. Primary.
30. A. Forsgren, P. E. Gill, M. H. Wright, "Interior Methods for Nonlinear Optimization", *SIAM Review* 44 (2002) 525–597, DOI 10.1137/S0036144502414942. Abstract read via Crossref. Primary.
31. M. H. Wright, INFORMS History & Traditions interview, uploaded 2019-11-18, https://www.youtube.com/watch?v=2L5nQIvTohk. Local auto-caption transcript `../sources/talks/2019-informs-margaret-wright-interview-autocaptions.txt` (fetched by research agent 01 in this run; not user-supplied), lines 145–147, 179, 187–195, 205–215, 241–243, 253–259, 305–313, 327–333. Secondary for Gill (first-hand collaborator account, auto-captions).
32. Open Library search API: *Practical Optimization* (Academic Press 1981; SIAM 2019) and *Numerical Linear Algebra and Optimization* (Addison-Wesley 1991; SIAM 2021), https://openlibrary.org/search.json, queried 2026-09-28. Secondary.
33. UCSD CCoM News and Announcements page, https://ccom.ucsd.edu (news list; newest item Dec 2019), fetched in this run. Secondary.
34. `references/sources/publications/publications.md` (OpenAlex harvest, generated 2026-09-28 by `scripts/fetch_publications.py`). Secondary (aggregator); used for the per-period counts only.
35. WebSearch, query 1: "Philip E. Gill" … 2025 OR 2026 talk OR emeritus OR award, 2026-09-28. It led to the UCSD Mathematics profile. Secondary.
36. WebSearch, query 2: "Philip E. Gill" SIAM Fellow class citation, 2026-09-28. Its result summary gives the 2014 SIAM Fellow claim, unconfirmed. Secondary.
