# 01 · Publications: landscape and signature-work anatomy

> **Researcher**: Andreas Wächter (also written Waechter / Wachter; DBLP pid 62/4235; Google Scholar id `Y1EdzIwAAAAJ` taken from the link on his own publications page)
> **Dimension**: research agent 01 of 06, signature works and the publication landscape (nuwa research-craft Phase 1)
> **Research date**: 2026-09-28
> **Sources consulted**: 34 listed under "Sources": 20 primary, 13 secondary, and 1 that could not be accessed (Google Scholar). WebSearch calls used: 2 of 2.
> **Method**: DBLP SPARQL (`scripts/dblp_works.py`), OpenAlex (`scripts/fetch_publications.py` with API key, then raw OpenAlex queries for three candidate author profiles), the Semantic Scholar author API, arXiv search HTML and abstract/HTML pages, Crossref and doi.org lookups, his Northwestern homepage (all subpages) and the CV PDF linked there, his **PhD thesis** (CMU 2002, PDF on his homepage, read: front matter, Ch. 1, §3.3.3–3.4.1, §4.1.3, Ch. 6, bibliography), the **IBM Research Report RC 23149 preprint** of the IPOPT paper (Optimization Online, read in full), Optimization Online entries, the COIN-OR Ipopt documentation, and Gurobi pages. Google Scholar returned a captcha redirect (not read). No user-supplied material existed in `references/sources/` (only `.gitkeep` files).
> **Tags**: [stated] = what Wächter said or wrote about his own work · [practice] = what the record shows he did (papers, code, CV entries, author lists) · [observed] = what others wrote · [inferred] = my reading, no primary source for it. Each item also says primary or secondary.
> **Quoting**: quotations are verbatim. PDF text extraction split words with spurious spaces (TeX kerning) and turned ligatures into single glyphs; I rejoined the words and wrote "fi"/"ff" as letters. Nothing else was changed.

---

## 0. Identity and data hygiene (read this before reusing any count)

Several people publish under this name, and every automated source mixes them up:

- **OpenAlex** profile `A5112274231` (the one `fetch_publications.py` picked: 90 works, 14,192 citations, h-index 24) mixes in a 1975 forestry paper, a 1991 VLSI thesis, a 2003 astrophysics abstract, a 2008 Delft ram-air-wing dissertation, Austrian teacher-education papers, cardiology papers (Bahlke et al., *Pacing Clin. Electrophysiol.*), MR relaxometry (*Cancers* 2025), a forestry-crane robotics paper (ICRA 2025) and TU Darmstadt machine-tool energy papers. A second OpenAlex profile `A5067291755` ("Andreas Wäechter", 22 works) holds genuine papers of his (IBM lithography, Keskar arXiv preprints, the DC-OPF chance-constraint paper, the 2025 noisy-IPM preprint) plus a Swedish agronomy report that is not his. [practice, secondary]
- **DBLP 62/4235** (50 records, 2000–2026) is clean except one record: "Energieeffizientes Kaltstartverhalten spanender Werkzeugmaschinen" (GI-Jahrestagung 2021, DOI 10.18420/INFORMATIK2021-098), whose co-authors (Walz, Tomov, Heimbach, Weigold) belong to the TU Darmstadt namesake. I dropped it: 49 clean DBLP records. [practice, secondary]
- **Semantic Scholar** author `1745824` (72 papers, 14,147 citations, h-index 28) also absorbs the TU Darmstadt namesake (Procedia CIRP 2023/2026, ZWF 2021/2025, wt Werkstattstechnik 2022). A second profile `31008035` holds his IBM lithography papers and the Xie–Wächter BFGS preprint. [practice, secondary]
- **arXiv** author search returns four papers by a KIT biomedical-engineering "Andreas Wachter" (2109.15063, 2201.03288, 2204.09346, 2310.10199). Excluded. [practice, primary]
- **ORCID** 0000-0002-3278-5637 (given by OpenAlex) is registered to "Andreas Waechter" but has no public employment or works, so I cannot tie it to him. ⚠️ Treat it as unconfirmed.

Every aggregate count below (citations, h-index, papers per period) is **approximate** for this reason. The cleanest bibliography is **his own CV** (c. 2020: 36 journal papers, 1 book chapter, 13 proceedings papers, 2 technical reports, 2 newsletter pieces, 2 US patents) plus DBLP and arXiv for 2020–2026.

---

## 1. Publication landscape

### 1.1 Career and resource context (the frame for every practice below)

| Period | Position | Resources and context | Evidence |
|---|---|---|---|
| 1992–1997 | Diplom-Mathematiker, University of Cologne | — | CV [stated, primary] |
| 1997–2002 | PhD in **Chemical Engineering**, Carnegie Mellon (advisor Lorenz T. Biegler; committee Grossmann, Sholl, Tütüncü) | Process-systems-engineering group. Single Linux workstations; Fortran 77, Harwell MA27, AMPL, ADOL-C; KNITRO and LOQO obtained directly from their authors for comparisons | CV; thesis title page and acknowledgments [stated, primary] |
| Feb 2002 – 2011 | IBM T. J. Watson Research Center, Mathematical Sciences: postdoc (Feb–Oct 2002), then Research Staff Member | Industrial research lab. Project work for IBM customers (circuit tuning, lithography source-mask optimization, reservoir history matching); IBM funded an open-source C++ rewrite of Ipopt, with Carl Laird as summer intern in 2004 and 2005 | CV; Ipopt docs "History of Ipopt" [stated, primary] |
| 2011–2019 | Associate Professor, Northwestern IEMS | Single-PI NSF DMS grants (2012–2015 "Novel Algorithms for Nonlinear Optimization"; 2015–2019 "Algorithms for Nonlinear Nonconvex Optimization under Uncertainty"); NSF CMMI collaborative grant with Pang and Mitchell (2013–2016); PhD students, several co-advised | CV [stated, primary] |
| 2018–2020 | ARPA-E Grid Optimization competition team (with Curtis, Molzahn, Wei, Wong), 2nd place ($400,000) in 2020; Ulam Distinguished Scholar, CNLS, Los Alamos (2019–2020) | Moves into power systems | CV [stated, primary] |
| 2019 – (2025/26?) | Professor, Northwestern IEMS; NSF grant DMS-2012410 acknowledged on 2024–2025 preprints | — | CV; arXiv 2502.11302 footnote [stated, primary] |
| by 2026 | "I moved to Gurobi Optimization. This webpage is no longer maintained." (homepage banner). Gurobi lists him as the presenter of the webinar "Local Nonlinear Optimization in Gurobi 13.0" (18 Feb 2026) | Move date not found; see Contradictions | homepage [stated, primary]; gurobi.com [observed, secondary] |

### 1.2 Topics by five-year period

Each line lists examples whose identifier I checked with a tool in this run. Venue, volume and pages come from DBLP/Crossref unless a note says otherwise.

**1997–2001: PhD. Interior-point NLP for process engineering, then a convergence failure and its repair**
- A. M. Cervantes, A. Wächter, R. H. Tütüncü, L. T. Biegler, "A reduced space interior point strategy for optimization of differential algebraic systems", *Comput. Chem. Eng.* 24(1):39–51, 2000. DOI 10.1016/S0098-1354(00)00302-1 [practice, primary]
- R. A. Bartlett, A. Wächter, L. T. Biegler, "Active set vs. interior point strategies for model predictive control", ACC 2000. DOI 10.1109/ACC.2000.877018 [practice]
- A. Wächter, L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", *Math. Program.* 88(3):565–574, 2000. DOI 10.1007/PL00011386. **Signature work 1** [practice]
- L. T. Biegler, A. M. Cervantes, A. Wächter, "Advances in simultaneous strategies for dynamic process optimization", *Chem. Eng. Sci.* 57(4):575–593, 2002. DOI 10.1016/S0009-2509(01)00376-1 [practice]
- R. Fletcher, N. I. M. Gould, S. Leyffer, Ph. L. Toint, A. Wächter, "Global Convergence of a Trust-Region SQP-Filter Algorithm for General Nonlinear Programming", *SIAM J. Optim.* 13(3):635–659, 2002. DOI 10.1137/S1052623499357258. Cited in his thesis as Namur Technical Report 99/03, i.e. written during the PhD. [practice]
- Unpublished: A. Wächter, L. T. Biegler, "Global and Local Convergence of a Reduced Space Quasi-Newton Barrier Algorithm for Large-Scale Nonlinear Programming", CAPD Technical Report B-00-06, CMU, 2000 (PDF on his homepage; text extraction failed, **not read**). It never appeared as a journal paper (not in the CV's journal list). [practice, primary]
- PhD thesis: "An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering", CMU, January 29, 2002 (homepage PDF, **read in part**). [stated/practice, primary]

**2002–2006: IBM I. Filter line search theory and the IPOPT implementation paper, first industrial applications**
- A. Wächter, L. T. Biegler, "Line Search Filter Methods for Nonlinear Programming: Motivation and Global Convergence", *SIAM J. Optim.* 16(1):1–31, 2005, DOI 10.1137/S1052623403426556; and "…: Local Convergence", 16(1):32–48, 2005, DOI 10.1137/S1052623403426544. **Signature work 2** [practice]
- A. Wächter, L. T. Biegler, "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming", *Math. Program.* 106(1):25–57, 2006 (online 28 Apr 2005). DOI 10.1007/s10107-004-0559-y. Preprint: IBM Research Report RC 23149, 12 March 2004, Optimization Online 2004/03/836. **Signature work 3** [practice]
- A. L. Tits, A. Wächter, S. Bakhtiari, T. J. Urban, C. T. Lawrence, "A Primal-Dual Interior-Point Method for Nonlinear Programming with Strong Global and Local Convergence Properties", *SIAM J. Optim.* 14(1):173–199, 2003. DOI 10.1137/S1052623401392123 [practice]
- T. Jockenhövel, L. T. Biegler, A. Wächter, "Dynamic optimization of the Tennessee Eastman process using the OptControlCentre", *Comput. Chem. Eng.* 27(11):1513–1531, 2003. DOI 10.1016/S0098-1354(03)00113-3 [practice]
- L. T. Biegler, A. Wächter, "SQP SAND strategies that link to existing modeling systems", Lecture Notes in Computational Science and Engineering (First CSRI Workshop on PDE-based Optimization), 2003. DOI 10.1007/978-3-642-55508-4_12 [practice]
- A. Wächter, C. Visweswariah, A. R. Conn, "Large-scale nonlinear optimization in circuit tuning", *Future Gener. Comput. Syst.* 21(8):1251–1262, 2005. DOI 10.1016/j.future.2005.04.002. The IBM application; the CV lists 2002–2007 talks on circuit tuning. [practice]
- J. R. P. Rodrigues, A. Wächter, A. R. Conn et al., "Combining Adjoint Calculations and Quasi-Newton Methods for Automatic History Matching", SPE Europec/EAGE 2006, SPE 99996. DOI 10.2118/99996-MS [practice]

**2007–2011: IBM II. Linear algebra inside the IPM, adaptive barrier, matrix-free/inexact steps, MINLP, lithography**
- O. Schenk, A. Wächter, M. Hagemann, "Matching-based preprocessing algorithms to the solution of saddle-point problems in large-scale nonconvex interior-point optimization", *Comput. Optim. Appl.* 36(2–3):321–341, 2007. DOI 10.1007/s10589-006-9003-y [practice]
- O. Schenk, A. Wächter, M. Weiser, "Inertia-Revealing Preconditioning For Large-Scale Nonconvex Constrained Optimization", *SIAM J. Sci. Comput.* 31(2):939–960, 2008. DOI 10.1137/070707233 [practice]
- J. Nocedal, A. Wächter, R. A. Waltz, "Adaptive Barrier Update Strategies for Nonlinear Interior Methods", *SIAM J. Optim.* 19(4):1674–1693, 2009. DOI 10.1137/060649513. Tested in both IPOPT and KNITRO (abstract). [practice]
- F. E. Curtis, J. Nocedal, A. Wächter, "A Matrix-Free Algorithm for Equality Constrained Optimization Problems with Rank-Deficient Jacobians", *SIAM J. Optim.* 20(3):1224–1249, 2009. DOI 10.1137/08072471X (Optimization Online 2008/05/1984) [practice]
- F. E. Curtis, O. Schenk, A. Wächter, "An Interior-Point Algorithm for Large-Scale Nonlinear Optimization with Inexact Step Computations", *SIAM J. Sci. Comput.* 32(6):3447–3475, 2010. DOI 10.1137/090747634 (Optimization Online 2009/02/2227). **Signature work 4** [practice]
- MINLP with the CMU–IBM team: P. Bonami, L. T. Biegler, A. R. Conn, G. Cornuéjols, I. E. Grossmann, C. D. Laird, J. Lee, A. Lodi, F. Margot, N. Sawaya, A. Wächter, "An algorithmic framework for convex mixed integer nonlinear programs" (Bonmin), *Discrete Optim.* 5(2):186–204, 2008, DOI 10.1016/j.disopt.2006.10.011; P. Belotti, J. Lee, L. Liberti, F. Margot, A. Wächter, "Branching and bounds tightening techniques for non-convex MINLP" (Couenne), *Optim. Methods Softw.* 24(4–5):597–634, 2009, DOI 10.1080/10556780903087124; C. D'Ambrosio, J. Lee, A. Wächter, ESA 2009, DOI 10.1007/978-3-642-04128-0_10; G. Nannicini et al., CPAIOR 2011, DOI 10.1007/978-3-642-21311-3_15; P. Bonami, J. Lee, S. Leyffer, A. Wächter, "On branching rules for convex mixed-integer nonlinear optimization", *ACM J. Exp. Algorithmics* 18, 2013, DOI 10.1145/2532568. [practice]
- IBM computational lithography: A. E. Rosenbluth et al., "Intensive optimization of masks and sources for 22nm lithography", Proc. SPIE 7274, 2009, DOI 10.1117/12.814844; D. O. S. Melville et al., Proc. SPIE 7640, 2010, DOI 10.1117/12.846716; D. O. S. Melville, A. E. Rosenbluth, A. Wächter et al., "Computational lithography: Exhausting the resolution limits of 193-nm projection lithography systems", *J. Vac. Sci. Technol. B* 29(6), 2011, DOI 10.1116/1.3662090; two US patents (8266554B2, 8719735B2, listed on the CV, not independently checked ⚠️). [practice]
- A. Wächter, "Short Tutorial: Getting Started With Ipopt in 90 Minutes", Dagstuhl Seminar Proceedings 09061, 2009. DOI 10.4230/DagSemProc.09061.16 (checked through DataCite) [practice]

**2012–2016: Northwestern I. Inexact SQP and hot starts, nonsmooth and ℓ1, structured quasi-Newton SQP**
- F. E. Curtis, J. Huber, O. Schenk, A. Wächter, "A note on the implementation of an interior-point algorithm for nonlinear optimization with inexact step computations", *Math. Program.* 136(1):209–227, 2012. DOI 10.1007/s10107-012-0557-4. The implementation "is included in the IPOPT software package paired with an iterative linear system solver and preconditioner provided in PARDISO" (Optimization Online 2011/04/2992 abstract). [practice, primary]
- F. E. Curtis, T. C. Johnson, D. P. Robinson, A. Wächter, "An Inexact Sequential Quadratic Optimization Algorithm for Nonlinear Optimization", *SIAM J. Optim.* 24(3):1041–1074, 2014. DOI 10.1137/130918320 [practice]
- T. C. Johnson, C. Kirches, A. Wächter, "An Active-Set Method for Quadratic Programming Based On Sequential Hot-Starts", *SIAM J. Optim.* 25(2):967–994, 2015. DOI 10.1137/130940384 [practice]
- M. Feng, A. Wächter, J. Staum, "Practical algorithms for value-at-risk portfolio optimization problems", *Quant. Finance Lett.* 3(1):1–9, 2015. DOI 10.1080/21649502.2014.995214 [practice]
- N. S. Keskar, J. Nocedal, F. Öztoprak, A. Wächter, "A second-order method for convex ℓ1-regularized optimization with active-set prediction", *Optim. Methods Softw.* 31(3):605–621, 2016. DOI 10.1080/10556788.2016.1138222; arXiv:1505.04315. Charles Broyden Prize 2016 (CV). [practice]
- D. Janka, C. Kirches, S. Sager, A. Wächter, "An SR1/BFGS SQP algorithm for nonconvex nonlinear programs with block-diagonal Hessian matrix", *Math. Program. Comput.* 8(4):435–459, 2016. DOI 10.1007/s12532-016-0101-2 [practice]

**2017–2021: Northwestern II. Uncertainty, noise, nonsmoothness, complementarity, simulation optimization, entry into power systems**
- A. Maggiar, A. Wächter, I. S. Dolinskaya, J. Staum, derivative-free trust-region method with Gaussian smoothing and adaptive multiple importance sampling, *SIAM J. Optim.* 28(2):1478–1507, 2018. DOI 10.1137/15M1031679 [practice]
- F. E. Curtis, A. Wächter, V. M. Zavala, "A Sequential Algorithm for Solving Nonlinear Optimization Problems with Chance Constraints", *SIAM J. Optim.* 28(1):930–958, 2018. DOI 10.1137/16M109003X [practice]
- F. Jara-Moroni, J.-S. Pang, A. Wächter, "A study of the difference-of-convex approach for solving linear programs with complementarity constraints", *Math. Program.* 169(1):221–254, 2018. DOI 10.1007/s10107-017-1208-6; follow-up with J. E. Mitchell, *J. Glob. Optim.* 77:687–714, 2020, DOI 10.1007/s10898-020-00905-z [practice]
- N. S. Keskar, A. Wächter, "A limited-memory quasi-Newton algorithm for bound-constrained non-smooth optimization", *Optim. Methods Softw.* 34(1):150–171, 2019. DOI 10.1080/10556788.2017.1378652; arXiv:1612.07350. Y. Xie, A. Waechter, "On the convergence of BFGS on a class of piecewise linear non-smooth functions", arXiv:1712.08571 (no journal version found). [practice]
- A. Peña-Ordieres, J. R. Luedtke, A. Wächter, "Solving Chance-Constrained Problems via a Smooth Sample-Based Nonlinear Approximation", *SIAM J. Optim.* 30(3):2221–2250, 2020. DOI 10.1137/19M1261985; arXiv:1905.07377 [practice]
- A. Peña-Ordieres, D. K. Molzahn, L. A. Roald, A. Wächter, "DC Optimal Power Flow With Joint Chance Constraints", *IEEE Trans. Power Syst.* 36(1):147–158, 2021. DOI 10.1109/TPWRS.2020.3004023; arXiv:1911.12439 [practice]
- S. Tu, A. Wächter, E. Wei, "A Two-Stage Decomposition Approach for AC Optimal Power Flow", *IEEE Trans. Power Syst.* 36(1):303–312, 2021 (online 2020). DOI 10.1109/TPWRS.2020.3002189; arXiv:2002.08003. **Signature work 5** [practice]
- M. Semelhago, B. L. Nelson, E. Song, A. Wächter, "Rapid Discrete Optimization via Simulation with Gaussian Markov Random Fields", *INFORMS J. Comput.* 33, 2021. DOI 10.1287/ijoc.2020.0971 (plus WSC 2017, DOI 10.1109/WSC.2017.8247941) [practice]
- B. Tasseff, C. Coffrin, A. Wächter, C. Laird, "Exploring Benefits of Linear Solver Parallelism on Modern Nonlinear Optimization Applications", arXiv:1909.08104 (2019) [practice]
- A. Wächter, "Nonlinear Optimization Algorithms", Ch. 17 in *Advances and Trends in Optimization with Engineering Applications*, SIAM, 2017, pp. 221–235. DOI 10.1137/1.9781611974683.ch17 [practice]

**2022–2026: Northwestern III, then Gurobi. Decomposition for grids, noisy IPMs, conic SQP with warm starts**
- F. E. Curtis, D. K. Molzahn, S. Tu, A. Wächter, E. Wei, E. Wong, "A Decomposition Algorithm with Fast Identification of Critical Contingencies for Large-Scale Security-Constrained AC-OPF", *Oper. Res.* 71, 2023. DOI 10.1287/opre.2023.2453; arXiv:2110.01737 [practice]
- I. Aravena et al. (incl. Curtis, Tu, Wächter, Wei, Wong), "Recent Developments in Security-Constrained AC Optimal Power Flow: Overview of Challenge 1 in the ARPA-E Grid Optimization Competition", *Oper. Res.* 71, 2023. DOI 10.1287/opre.2022.0315; arXiv:2206.07843 [practice]
- J. Ospina, D. M. Fobes, R. Bent, A. Wächter, "Modeling and Rapid Prototyping of Integrated Transmission-Distribution OPF Formulations With PowerModelsITD.jl", *IEEE Trans. Power Syst.*, 2023. DOI 10.1109/TPWRS.2023.3234725; arXiv:2210.16378 [practice]
- X. Luo, A. Wächter, "A Quadratically Convergent Sequential Programming Method for Second-Order Cone Programs Capable of Warm Starts", *SIAM J. Optim.* 34(3):2943–2972, 2024. DOI 10.1137/22M1507681; arXiv:2207.03082 [practice]
- F. E. Curtis, S. Dezfulian, A. Wächter, "Derivative-free bound-constrained optimization for solving structured problems with surrogate models", *Optim. Methods Softw.* 39, 2024. DOI 10.1080/10556788.2024.2329588; arXiv:2202.12961 [practice]
- S. Dezfulian, A. Wächter, "On the Convergence of Interior-Point Methods for Bound-Constrained Nonlinear Optimization Problems with Noise", *SIAM J. Optim.* 36(3):1356–1386, 2026. DOI 10.1137/24M1666537; arXiv:2405.11400 [practice]
- F. E. Curtis, S. Dezfulian, A. Waechter, "An Interior-Point Algorithm for Continuous Nonlinearly Constrained Optimization with Noisy Function and Derivative Evaluations", arXiv:2502.11302 (Feb 2025; Lehigh ISE Technical Report 25T-002) [practice]
- Y. Lou, X. Luo, A. Wächter, E. Wei, "A Decomposition Framework for Nonlinear Nonconvex Two-Stage Optimization", *SIAM J. Optim.* 36(3):1211–1238, 2026. DOI 10.1137/25M1728661; arXiv:2501.11700 (v1 Jan 2025, v3 Feb 2026) [practice]
- J. Ospina, M. Garcia, X. Luo, A. Wächter, D. M. Fobes, R. Bent, "Smoothed Two-Stage Decomposition Algorithm for Solving Large-Scale Transmission and Distribution AC-OPF Problems", arXiv:2607.16430 (17 Jul 2026) [practice]
- Simulation optimization with Nelson and Song: H. Avci, B. L. Nelson, E. Song, A. Wächter, "Using Cache or Credit for Parallel Ranking and Selection", *ACM TOMACS* 33, 2023, DOI 10.1145/3618299; "Dice and slice simulation optimization for high-dimensional discrete problems", *Eur. J. Oper. Res.* 330, 2026, DOI 10.1016/j.ejor.2026.01.005; H. Avci, B. L. Nelson, A. Wächter, arXiv:2302.02254 [practice]
- Applications with other Northwestern groups (identity plausible, not confirmed by his homepage): I. Horenko et al., "On cheap entropy-sparsified regression learning", *PNAS*, 2022/2023, DOI 10.1073/pnas.2214972120 (co-author O. Schenk); E. Vecchi et al., *J. Comput. Sci.* 76, 2024, DOI 10.1016/j.jocs.2024.102208; N. Izadinia et al., "A versatile optimization framework for sustainable post-disaster building reconstruction", *Optim. Eng.*, 2022, DOI 10.1007/s11081-022-09766-9 (Izadinia is listed as his former student, which supports the identity) [practice]

**Reading the periods** [inferred, from the lists above]. There is one continuous spine, the constrained-NLP solver and its globalization and linear algebra, running from 2000 (failure example) through 2005–2006 (filter plus IPOPT), 2007–2012 (factorization, inertia, barrier update, inexact steps) and 2024–2026 (noisy IPM, warm-startable conic SQP). Around it sit waves of new problem classes, each tied to where he worked and whom he worked with: process engineering (CMU), circuits, lithography and MINLP (IBM), uncertainty, nonsmoothness, complementarity and simulation optimization (NSF and co-advised students at Northwestern), power grids (ARPA-E, LANL, Wei). The homepage names this as the third research theme: "Introducing techniques and concepts for nonlinear optimization into settings where they have not yet been exploited." [stated, primary]

### 1.3 Author order: the first-to-last shift is not informative here

`fetch_publications.py` reports 4 first-authored papers in 2000–2004 and 2005–2009, then **0 first-authored and almost only last-authored papers from 2010**. That looks like a move from doing to supervising. Two reasons it cannot be read that way [inferred, checked on the author lists]:
1. Most of his multi-author papers list authors **alphabetically**, and "Wächter" sorts near the end: Fletcher–Gould–Leyffer–Toint–Wächter; Belotti–Lee–Liberti–Margot–Wächter; Curtis–Nocedal–Wächter; Curtis–Schenk–Wächter; Keskar–Nocedal–Öztoprak–Wächter; Jara-Moroni–Pang–Wächter; Tu–Wächter–Wei; Lou–Luo–Wächter–Wei. So "last author" mostly means "alphabetical".
2. The non-alphabetical orders are more informative: student first, then senior co-authors. Examples are Keskar–Wächter (2019), Luo–Wächter (2024), Dezfulian–Wächter (2026), Peña-Ordieres–Luedtke–Wächter (2020) and Semelhago–Nelson–Song–Wächter (2021).
- The real change is that **sole-student two-author papers appear from about 2016**, alongside a stable set of senior peers. Before 2011 his first-author papers are all with his advisor (Wächter–Biegler ×4) or IBM applications (Wächter–Visweswariah–Conn). [practice, secondary: DBLP author lists]

### 1.4 Collaboration network and students

**Most frequent co-authors, clean DBLP set of 49 records** [practice, secondary]: Frank E. Curtis (9 papers, 2009–2025), Lorenz T. Biegler (7, 2000–2008), Olaf Schenk (5, 2007–2024), Jon Lee (5, 2008–2013), Barry L. Nelson (5, 2017–2026), Eunhye Song (5, 2017–2026), Ermin Wei (4, 2020–2026), François Margot (3), Jorge Nocedal (3, 2009–2016). Clusters: (a) the CMU process-systems group (Biegler, Cervantes, Bartlett, Laird); (b) the Northwestern/Lehigh nonlinear-optimization axis (Nocedal, Curtis, Waltz, Robinson); (c) the Basel/Lugano HPC linear algebra group (Schenk, Hagemann, Huber); (d) the IBM/CMU MINLP team (Lee, Bonami, Margot, Belotti, Cornuéjols, Grossmann, Leyffer); (e) Heidelberg/Magdeburg SQP (Kirches, Sager, Janka); (f) Northwestern simulation optimization (Nelson, Song, Staum); (g) power systems (Wei, Molzahn, Wong, and the LANL PowerModels group: Coffrin, Bent, Fobes, Ospina).

**Mentors, from the thesis acknowledgments** [stated, primary]:
- Biegler, "who gave me the optimal balance of guidance and freedom".
- Nocedal, "who introduced me into the math programming crowd", and whose "contagious optimism together with his amazing ability to always find new important questions from unexpected viewpoints had a significant and inspiring influence on this work".
- Reha Tütüncü, "for taking the effort of teaching me the basics of interior point methods in a reading course".
- He also thanks Richard Byrd and Marcelo Marazzi "for inspiring conversations regarding convergence failures and filter methods", Anders Forsgren and Göran Sporre "for interesting discussions about counter examples during a memorable visit to Stockholm", and Caroline Sainvitu and Philippe Toint "for their valuable feedback on the convergence proofs of the filter method".

**PhD students** (homepage "Students" page and CV "Doctoral Student Advisees") [stated, primary]:

| Student | Graduated | Co-advisor | Papers with him (verified above) |
|---|---|---|---|
| Travis C. Johnson | 2013 | — | inexact SQP (SIOPT 2014), hot-start QP (SIOPT 2015) |
| Mingbin (Ben) Feng | 2016 | Jeremy Staum | VaR portfolio (QFL 2015), WSC 2018 |
| Nitish S. Keskar | 2017 | Jorge Nocedal | ℓ1 active-set (OMS 2016), L-BFGS nonsmooth (OMS 2019) |
| Francisco Jara-Moroni | 2018 | — | LPCC via DC (MP 2018), logical Benders (JOGO 2020) |
| Alejandra Peña-Ordieres | 2020 | — | chance constraints (SIOPT 2020, TPWRS 2021) |
| Mark Semelhago | 2020 | Barry Nelson (homepage adds Eunhye Song) | GMRF simulation optimization (WSC 2017, IJOC 2021) |
| Shenyinying (Ruby) Tu | expected 2021 (CV) | Ermin Wei | two-stage AC-OPF (TPWRS 2021), SC-AC-OPF (OR 2023) |
| Niloufar Izadinia | former (homepage; not on CV) | — | post-disaster reconstruction (Optim. Eng. 2022) |
| Xinyi Luo | expected 2023 (CV) | — | SOCP SQP (SIOPT 2024), two-stage (SIOPT 2026) |
| Shima Dezfulian | expected 2024 (CV) | — | DFO surrogate (OMS 2024), noisy IPM (SIOPT 2026; arXiv 2502.11302) |
| Yuchen Lou | current (homepage) | Ermin Wei | two-stage (SIOPT 2026) |

About half of the students were co-advised across groups: with Nocedal (optimization), Staum and Nelson (simulation/finance) and Wei (EE). Student topics follow the co-advisor's field, which is how the problem-class waves in §1.2 entered his record. [inferred]
Not on either list but co-authors on student-type papers: Alvaro Maggiar (SIOPT 2018), Yuchen Xie (arXiv 1712.08571), Harun Avci (TOMACS 2023, EJOR 2026). Their advisors were not checked. [practice]

### 1.5 Usual venues

From the clean DBLP set: *SIAM J. Optim.* (14), *Math. Program.* (4), *Optim. Methods Softw.* (4), arXiv/CoRR (4 in DBLP; about 18 genuine arXiv ids overall), Winter Simulation Conference (3), *Comput. Chem. Eng.* (2), *SIAM J. Sci. Comput.* (2), *Oper. Res.* (2). Outside DBLP, from the CV and OpenAlex: *IEEE Trans. Power Syst.* (3), SPIE (3), *Chem. Eng. Sci.*, SPE. Algorithm papers go to SIOPT and Math. Program.; linear-algebra-heavy papers to SISC and COA; application papers to the application field's own journal. [practice, secondary]

### 1.6 Most-cited works

OpenAlex counts are from the contaminated profile; S2 = Semantic Scholar (influential citations in brackets). Both fetched 2026-09-28. Google Scholar counts: **not read** (captcha). [practice, secondary]

| # | Work | OpenAlex | S2 |
|---|---|---|---|
| 1 | Wächter & Biegler, IPOPT implementation, *Math. Program.* 2006 | 9,727 | 10,205 (952) |
| 2 | Bonami et al., Bonmin, *Discrete Optim.* 2008 | 908 | 383 (40) |
| 3 | Belotti et al., Couenne, *OMS* 2009 | 607 | 707 (76) |
| 4 | Biegler, Cervantes, Wächter, simultaneous dynamic optimization, *Chem. Eng. Sci.* 2002 | 430 | 449 (19) |
| 5 | Wächter & Biegler, line-search filter I, *SIOPT* 2005 | 412 | 444 (50) |
| 6 | Fletcher, Gould, Leyffer, Toint, Wächter, TR-SQP-filter, *SIOPT* 2002 | 280 | 304 (21) |
| 7 | Wächter & Biegler, line-search filter II, *SIOPT* 2005 | 201 | 219 (18) |
| 8 | Schenk, Wächter, Hagemann, *COA* 2007 | 173 | 184 (6) |
| 9 | Nocedal, Wächter, Waltz, adaptive barrier, *SIOPT* 2009 | 121 | 136 (12) |
| 10 | Wächter & Biegler, failure of global convergence, *Math. Program.* 2000 | 100 | 119 (24) |

The IPOPT paper has more than 20 times the citations of anything else he wrote. Most of those come from **users of the software** [inferred]: the Ipopt documentation asks users of the code to cite this paper (§2.3). His citation profile is that of a software author, not of a theorem author.

### 1.7 Most recent work (last 24 months)

- 2026-07-17: arXiv:2607.16430 (StsDOpt, T&D AC-OPF, with LANL). Affiliation shown: Northwestern.
- 2026-07: two *SIAM J. Optim.* 36(3) papers, the two-stage decomposition (Lou, Luo, Wächter, Wei) and the noisy bound-constrained IPM (Dezfulian, Wächter).
- 2026: *Eur. J. Oper. Res.* 330 (simulation optimization, with Avci, Nelson, Song).
- 2025-02: arXiv:2502.11302 (noisy constrained IPM, with Curtis and Dezfulian).
- 2026-02-18: Gurobi webinar "Local Nonlinear Optimization in Gurobi 13.0"; Gurobi's page names "Dr. Andreas Waechter" as speaker and describes the feature as "The ability to quickly find locally optimal solutions to nonlinear problems". [observed, secondary]
[practice, primary unless marked]

### 1.8 Software as publication

- **Ipopt**. The homepage says: "Starting with my PhD thesis advised by Larry Biegler, I developed Ipopt, a general purpose open-source optimization solver for large-scale nonlinear optimization. Ipopt was first released as FORTRAN code in 2000, and then reimplemend in C++ in 2005-2006 at IBM by Carl Laird and myself. Ipopt has been widely used in numerous application and has been integrated in various commercial software." (typos as in the original) [stated, primary]
  - The Ipopt AUTHORS page lists "Main authors: Andreas Waechter, project leader (IBM) Carl Laird (IBM, Carnegie Mellon University)". The documentation is "maintained by Stefan Vigerske (GAMS Software GmbH) and Andreas Wächter". The current documentation version is 3.14.20. [practice, primary]
- **Bonmin and Couenne**. His software page says Bonmin "resulted from a collaboration between Carnegie Mellon University and IBM". His exact role in the Bonmin and Couenne code is **not documented** in anything I read. [stated, primary]
- **Prizes tied to the software**: 2011 J. H. Wilkinson Prize for Numerical Software (with Carl Laird) "for IPOPT, a software library for solving nonlinear, nonconvex, large-scale continuous optimization problems" (COIN-OR announcement, 7 Apr 2011) [observed, secondary]; 2009 INFORMS Computing Society Prize (with Biegler) for the IPOPT paper (INFORMS page lists names only; the CV names the paper) [stated + observed].

---

## 2. Signature works, dissected (framework §五)

Selection rule: the most cited (SW3), what he himself puts first (the homepage research page opens with Ipopt and lists the filter papers first; the CV award list names SW2 and SW3), and the turning points: SW1 is the origin, SW4 moves from factorization to iterative solvers, SW5 is the late move to decomposition and grids.

### SW1. "Failure of global convergence for a class of interior point methods for nonlinear programming" (Wächter & Biegler, *Math. Program.* 88(3):565–574, 2000; DOI 10.1007/PL00011386)

*Read via the thesis version (§3.3.3 and §4.1); the published article itself was **not read**.*

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary: thesis §3.3.3] "During the development and analysis of the merit function based line search options just described, we found a simple example problem, where Ipopt failed in an unexpected way." The failure surfaced in **his own code**, while he was comparing several globalization options in one implementation. |
| **Why then** | [inferred] Line-search primal-dual IPMs for nonconvex NLP had just gained published global-convergence theorems (the thesis examines El-Bakry et al. 1996, Yamashita 1998, Ulbrich–Ulbrich–Vicente's filter IPM report, and an early LOQO). Implementing several merit functions side by side in one research code created the conditions to see a failure common to all of them. |
| **Key insight** | Methods whose steps are fractions of directions that satisfy the linearized equality constraints, kept interior by the fraction-to-the-boundary rule, can be trapped in a region where the linearized equalities and the linearized bounds are inconsistent. They then converge to arbitrary infeasible points on a **well-posed** problem. His diagnosis of the published theorems [stated, primary, thesis §4.1.3]: the violated assumption "pertains to the behavior of the algorithm rather than to the problem statement itself". |
| **Minimum evidence** | A 3-variable problem, min x₁ s.t. x₁² − x₂ − 1 = 0, x₁ − x₃ − 0.5 = 0, x₂, x₃ ≥ 0, started from (−2, 3, 1). A table of 9 iterates in which step sizes collapse, and "all other choices for the Hessian approximation lead to similar failures". The thesis stresses "the disconcerting observation is that the example problem (3.26) is well posed". The analysis is then generalized to a class ("Algorithm GIP", Theorem 4.1), and the thesis reports numerical confirmation on IPOPT's exact-penalty option and an earlier LOQO version. [stated/practice, primary] |
| **Abandoned paths** | The merit-function line searches he had implemented: an exact penalty function (with a watchdog option) and the Biegler–Cuthrell augmented Lagrangian, which by his own account had no convergence proof yet "seems to work well in practice". They were demoted to comparison options, and the filter became the remedy (SW2). [practice, primary: thesis §3.3] |
| **Reception** | [stated, thesis p. 51] "the above example has been cited and discussed by other researchers", citing Benson–Shanno–Vanderbei (jamming), Marazzi–Nocedal (feasibility control) and Tits et al. [observed, primary] The Tits et al. abstract claims their method "does not suffer a common pitfall recently pointed out by Waechter and Biegler" (Optimization Online 2002/07/509). Wächter is a co-author of the final paper (SIOPT 14(1), 2003) but not of the earlier report version cited in his thesis (TR 2001-3 R2: Tits, Urban, Bakhtiari, Lawrence). [practice] So the critique turned into a collaboration. Liu & Sun (2002 preprint) used "the examples provided by Wachter and Biegler" as hard test cases [observed, primary]. He presented it at ISMP 2000 as "Global Convergence of a Class of Interior-Point Methods for Nonconvex Nonlinear Programming: Failure and Some Remedies" (CV). About 100–119 citations, 24 of them "influential" (S2). |
| **Method it shows** | **Counterexample-driven algorithm design**: take a failure of your own code, reduce it to the smallest well-posed instance, generalize it to a class of methods, check which assumption of each published convergence proof it violates, and design a remedy that provably excludes it. [inferred; the steps themselves are documented in the thesis] |

### SW2. "Line Search Filter Methods for Nonlinear Programming: Motivation and Global Convergence" and "…: Local Convergence" (Wächter & Biegler, *SIAM J. Optim.* 16(1):1–31 and 32–48, 2005; DOIs 10.1137/S1052623403426556, 10.1137/S1052623403426544)

*Read via thesis §3.4 (introduction) and the published abstracts; the SIOPT texts were **not read**.*

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary: thesis §3.3.3–3.4.1] The direct remedy for SW1: "In the remainder of this chapter we will present a different line search technique for Ipopt that does not suffer the described convergence problem." It adapts the Fletcher–Leyffer filter and is "motivated by the trust region SQP method proposed and analyzed by Fletcher et. al.", a paper he co-authored as a PhD student (Namur TR 99/03 → SIOPT 2002). |
| **Why then** | [inferred, with partial evidence] Filter methods were new: Fletcher–Leyffer "to appear" in *Math. Program.* 2002 per the thesis bibliography, and the Namur trust-region filter convergence reports date from 1998–2000. No line-search version with convergence theory existed. He had direct access to the Namur group (co-authorship; acknowledged feedback from Sainvitu and Toint on the proofs; a seminar at Namur in Aug 2002 per the CV). |
| **Key insight** | [stated, primary: thesis pp. 51–52] Two arguments. On efficiency: "numerical evidence presented in Section 5.1.2 suggests that Newton directions are usually good directions (in particular if exact second derivative information is used), and that a filter approach has the potential to be more efficient than algorithms based on merit functions, as it generally accepts larger steps." On robustness: when the step becomes too small, the filter falls back to a feasibility-restoration phase, so the SW1 failure cannot occur. His technical novelty is a **different switching condition**, which lets second-order corrections prevent the Maratos effect. That gives the first local convergence result for a filter method (thesis §6.1). The same framework covers barrier IPMs and active-set SQP. |
| **Minimum evidence** | Proofs (thesis Ch. 4): every limit point feasible, at least one limit point stationary; fast local convergence with second-order corrections. A numerical comparison of line-search options inside the same code (thesis §5.1.2). [practice, primary] |
| **Abandoned paths** | (a) He did not base trial-step acceptance on the norm of the optimality conditions, as Ulbrich–Ulbrich–Vicente do, because keeping μ fixed for several iterations "enables us to base the acceptance of trial steps directly on the barrier function", so the method "is less likely to converge to saddle points or maxima" [stated, thesis p. 53]. (b) A Lagrangian-based filter variant is proposed and only "briefly discussed" (SIOPT I abstract). Whether it was ever pursued further: **not found**. |
| **Reception** | SIAM Student Paper Prize 2002 for "Global and Local Convergence of Line Search Filter Methods for Nonlinear Programming" (CV). 412–444 citations (I) and 201–219 (II). Ipopt's documentation lists these papers as the mathematical basis of the code. [stated/observed] |
| **Method it shows** | **Prove the safeguard you ship**: the theory is written for the globalization mechanism actually in the code, and both global and local behaviour get their own companion paper. [inferred] |

### SW3. "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming" (Wächter & Biegler, *Math. Program.* 106(1):25–57, 2006; DOI 10.1007/s10107-004-0559-y)

*Read in full as IBM Research Report RC 23149 (12 March 2004, revised 19 March 2004), Optimization Online 2004/03/836. The published version was **not read**; the two may differ.*

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary: RC 23149 abstract] "Local and global convergence properties of this method were analyzed in previous work. Here we provide a comprehensive description of the algorithm, including the feasibility restoration phase for the filter method, second-order corrections, and inertia correction of the KKT matrix. Heuristics are also considered that allow faster performance." [practice, primary] Several items on the thesis's own future-work list (Ch. 6.2) are carried out here. The TRON-based restoration phase is replaced by the IPM filter algorithm applied to a smooth ℓ1-infeasibility reformulation (RC 23149 §3.3.1); the thesis had written that "the restoration phase is the only step where the filter line search method can fail, and therefore inherits all the difficult cases". The inertia-correction heuristic is formalized, and objective-blind restoration gets safeguards. |
| **Why then** | [inferred, with stated resource context] He had just moved to IBM (Feb 2002) and had a stable Fortran 77 code on COIN-OR. A large standard test set (CUTEr "as of Jan 1, 2004") and two competing IPM codes (KNITRO 3.1.1, LOQO 6.06, obtained from their authors) made a large comparison feasible. Hardware: "a PC with a 1.66 GHz Pentium IV microprocessor and 1 GB of memory running RedHat Linux 9.0"; linear solver Harwell MA27 with MC19 scaling. [stated, primary] |
| **Key insight** | The robustness of a general-purpose NLP code sits in its "second-tier" mechanisms, not in the headline method. The mechanisms are: a restoration phase that must "be very robust" because "it is invoked whenever the progress to the solution becomes difficult"; inertia correction; filter reset and watchdog heuristics; slight relaxation of bounds; automatic gradient-based scaling; handling of tiny steps; and iterative refinement on the unreduced system ("In our experience it is very important to use iterative refinement in order to improve robustness of the implementation and to be able to obtain highly accurate solutions."). [stated, primary: RC 23149 §3.3, §3.10] |
| **Minimum evidence** | 954 CUTEr problems, after documented exclusions: 979 candidates → 11 removed as apparently unbounded, 2 with Jacobian evaluation errors, 1 numerical outlier, 11 possibly infeasible. An **ablation of his own safeguards** compared "Filter (default)", "Filter (no heuristics)", "Penalty Function" and "Full Step". A solver comparison with performance profiles for iterations, function evaluations and CPU time, with per-problem tables for IPOPT, KNITRO and LOQO posted on his homepage (the tables are still linked from the publications page). [practice, primary] |
| **What the evidence said, including against him** | "the filter option is indeed more robust than the penalty function method, even when the heuristics are disabled". But on problems both solved, "The filter option seems to be only slightly more efficient for those problems". And "Full Step" alone solved 86.1%: "this might indicate that in many cases Newton's method does not require a safeguarding scheme … or alternatively, that many problems in the test set are not very difficult." On the heuristics: "Even though these heuristics are not frequently activated and the watchdog heuristic might in some cases increase the number of iterations, they appear to have an overall positive effect." [stated, primary] |
| **Abandoned paths** | The penalty-function line search, the TRON restoration phase and the Fortran 77 code base are all superseded. The Ipopt docs say "The development on the Fortran version has ceased", and the C++ rewrite was "re-implemented from scratch". The reduced-space/quasi-Newton variant that is central in the thesis does not appear in this paper, and its CAPD report (B-00-06) was never published in a journal. [practice, primary; reading that as "abandoned" is **inferred**] |
| **Reception** | About 9.7k (OpenAlex) to 10.2k (S2, 952 influential) citations, the most cited work by more than an order of magnitude. INFORMS Computing Society Prize 2009; honorable mention in the ICCOPT-I (2004) Young Researcher Competition (CV); Wilkinson Prize 2011 for the software. The Ipopt docs ask users to cite this paper: "Writing high-quality numerical software takes a lot of time and effort, and does usually not translate into a large number of publications, therefore we believe this request is only fair :)." [stated by the Ipopt documentation, which he co-maintains; primary] |
| **Method it shows** | **Benchmark candidly, and ablate your own safeguards.** He compares against the penalty baseline, the no-heuristics filter and the no-safeguard Full Step, and he reports the result that weakens his case (86.1% with Full Step). He publishes per-problem tables and disclaims the solver comparison: "The comparison presented here is not meant to be a rigorous assessment of the performance of these three algorithms, as this would require very careful handling of subtle details such as comparable termination criteria etc, and would be outside the scope of this paper." [stated, primary] |

### SW4. The inexact-step / iterative-linear-algebra line (Curtis, Nocedal, Wächter, *SIOPT* 20(3), 2009; **Curtis, Schenk, Wächter, *SIAM J. Sci. Comput.* 32(6):3447–3475, 2010, DOI 10.1137/090747634**; Curtis, Huber, Schenk, Wächter, *Math. Program.* 136(1), 2012), with Schenk, Wächter, Weiser, *SISC* 31(2), 2008

*Read: abstracts only (OpenAlex and Optimization Online). Full texts **not read**.*

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary: thesis Ch. 6.2] The thesis flagged the factorization bottleneck twice. On inertia correction: "each trial corresponds to a complete factorization of the KKT matrix". On solver choice: "the choice of the linear solver used for the factorization of the KKT matrix impacts the computational speed and robustness". [inferred] The collaborations supplied the missing pieces. Schenk (PARDISO, Basel) brought multilevel incomplete LBLᵀ preconditioners that also estimate inertia (SISC 2008 abstract). Curtis and Nocedal brought inexact-Newton globalization for equality-constrained problems (SIOPT 2009). The first talk on this line, "An Interior-Point Algorithm For Large-Scale Nonlinear Optimization With Inexact Step Computations", was given at Basel in Feb 2009 (CV). |
| **Why then** | [inferred] Target problems were 3D PDE-constrained control, e.g. hyperthermia treatment planning with 150³ states (SISC 2008 abstract). Direct factorization becomes impractical at that size, while Krylov solvers and multilevel preconditioners had become usable. Era: IBM with academic partners in Basel and Evanston. |
| **Key insight** | Replace "factorize, and check inertia from the factorization" with termination tests for an iterative solver that preserve global convergence. The resulting algorithm is "matrix-free in that it does not require the factorization of derivative matrices" and allows "inexact step computations … to save computational expense during each iteration" (SISC 2010 abstract). [practice, primary] |
| **Minimum evidence** | "Numerical results are presented for nonlinear optimization test set collections and a pair of PDE-constrained model problems" (SISC 2010 abstract). The follow-up note (2012) puts the method **back into IPOPT**, paired with PARDISO's iterative solver. [practice, primary] |
| **Abandoned paths** | Not documented in what I read. The related "hot-starting NLP solvers" programme (talks 2012–2014 per the CV: ISMP 2012, INFORMS 2012, MIP 2014) led to the QP paper (SIOPT 2015), which says it "proves to be fairly reliable, despite the lack of global convergence guarantees". A hot-started full NLP solver paper was **not found**, so that direction may have stopped at the QP stage [inferred]. |
| **Reception** | Modest: 57–80 citations (SISC 2010), 32–46 (SIOPT 2009), 24–25 (MP 2012), 50 (SISC 2008). He gave plenaries on the theme: "Large-Scale Nonlinear Optimization with Inexact Step Computations" at Parametric Optimization X (2010) and "Inexact Methods for Nonlinear Optimization" at MOPTA 2014 (CV). [practice, secondary] |
| **Method it shows** | **Attack your production solver's bottleneck, then ship the fix back into the solver.** Find the minimal conditions under which an expensive exact kernel (here factorization and inertia) can be replaced, prove convergence under those conditions, and merge the result into the production code. [inferred] |

### SW5. Barrier smoothing for two-stage decomposition (Tu, Wächter, Wei, *IEEE Trans. Power Syst.* 36(1):303–312, 2021, DOI 10.1109/TPWRS.2020.3002189, arXiv:2002.08003 → **Lou, Luo, Wächter, Wei, *SIAM J. Optim.* 36(3):1211–1238, 2026, DOI 10.1137/25M1728661, arXiv:2501.11700**)

*Read: abstracts only. Full texts **not read**.*

| Dimension | Content |
|---|---|
| **Origin** | [stated, primary: thesis Ch. 6.2, 2002] "In the implementation of the elemental decomposition it is currently not possible to impose additional constraints, that couple the entire system. Here, a two-stage decomposition strategy might provide the answer." [stated, primary: CV] The application trigger came 16–18 years later: the ARPA-E GO competition grant "Hybrid Interior-Point/Active-Set SCOPF Algorithms Exploiting Power Systems Characteristics" (Nov 2018 – Nov 2019), the Ulam scholarship at Los Alamos (2019–20), and co-advising with Ermin Wei (EE). Linking the 2002 sentence to the 2020 paper as cause and effect is **inferred**. |
| **Why then** | [inferred] Grid problems with millions of buses, a DOE competition that rewards wall-clock performance, parallel hardware, and a LANL partner with a modeling stack (PowerModels / PowerModelsITD). |
| **Key insight** | "a smoothing technique that renders the response of a subnetwork differentiable with respect to the input from the master problem, utilizing properties of the barrier problem formulation that naturally arises when subproblems are solved by a primal-dual interior-point algorithm. Consequently, existing efficient nonlinear programming solvers can be used for both the master problem and the subproblems." (TPWRS abstract) [practice, primary] The same move appears in the chance-constraint line: the quantile reformulation "can be directly used by standard nonlinear optimization solvers" (SIOPT 2020 abstract). |
| **Minimum evidence** | TPWRS 2021: "able to solve instances with more than 11 million buses". SIOPT 2026: local differentiability of nonconvex second-stage solutions, so "existing proofs can be applied", plus "fast local convergence of the algorithm as the barrier parameter is driven to zero". [practice, primary] |
| **Abandoned paths** | None documented; **not known**. |
| **Reception** | 33–36 citations for TPWRS 2021. The LANL group extended it to T&D AC-OPF (arXiv:2607.16430, 2026). The SIOPT paper went through three arXiv versions (Jan 2025 → Nov 2025 → Feb 2026) before publication. [practice] |
| **Method it shows** | **Use the solver's own machinery as a modeling device**: turn a nonsmooth or nested structure into a smooth NLP so that existing robust NLP codes, not new bespoke solvers, do the work. The thesis's view is "This emphasizes the importance of flexibility of an optimization algorithm." [inferred, with the stated thesis quote] |

---

## 3. Failures, abandoned directions, unpublished and superseded work

Negative space carries information. [practice unless marked]

1. **Merit-function globalization in his own code** (exact penalty with watchdog; augmented Lagrangian à la Biegler–Cuthrell). Implemented, shown to fail on his own counterexample, kept as comparison options, replaced as default by the filter (thesis §3.3; RC 23149 §4.1).
2. **TRON-based restoration phase.** The thesis calls it the weak point ("improvements regarding robustness are necessary"; restored iterates "can lead to extremely bad objective function values") and it is replaced in the 2004/2006 paper.
3. **Reduced-space quasi-Newton IPM** (CAPD TR B-00-06, 2000; thesis Ch. 3.2.2–3.2.5). Central in the thesis (it solved the 2-million-variable air-separation problem "in less than 7 hours on a Linux workstation"), but never published in a journal and absent from the IPOPT paper. [practice; "abandoned" is inferred]
4. **Fortran 77 Ipopt 2.x.** "The development on the Fortran version has ceased" (Ipopt docs), superseded by the C++ rewrite that the thesis had proposed ("an even larger degree of flexibility could be obtained by a re-implementation in C++").
5. **Test-set exclusions reported openly.** In RC 23149, footnote 5: "IPOPT failed to converge and was able to produce iterates with very small constraint violation and at the same time very large negative values of the objective function" on 11 CUTEr problems (listed by name). He also reported that IPOPT flagged 11 likely-infeasible problems where KNITRO and LOQO hit the iteration limit.
6. **Long gestations.** Talk "Smoothing Noisy Black-Box Functions For Nonlinear Optimization" (ISMP 2006, CV) → journal paper on Gaussian-smoothing DFO in 2018 (SIOPT 28(2)). Talk "Solving Chance-Constrained Optimization Problems Using a Kernel-VaR Estimator" (2017, CV) → published as a quantile-based smooth approximation in 2020. Thesis idea of two-stage decomposition (2002) → 2020/2026. [practice; gaps and title changes are on record, reasons **not known**]
7. **Hot-started NLP solvers** (talks 2012–2014) → only the QP paper (2015), which admits "the lack of global convergence guarantees". No NLP-level paper found. [inferred]
8. **MINLP line ends after IBM.** There are no new MINLP papers after 2013 (branching rules, ACM JEA). [practice; reason **not known**]
9. **No retractions, errata or rejection records found** in this pass (not searched beyond DBLP/Crossref/arXiv version histories).

---

## 4. Cross-cutting patterns (candidate research methods for Phase 2; all [inferred] from the evidence above)

- **P1. The solver is the laboratory.** Research questions come from the behaviour of his own code on test sets and applications. The thesis says so: "continued usage is expected to reveal bottlenecks, either in the implementation or in the underlying mathematical algorithm, and might raise interesting research questions" [stated, primary]. Evidence: SW1, SW3, SW4.
- **P2. Future-work lists that he actually works through.** At least six items from thesis Ch. 6.2 reappear as later publications or code: the restoration phase, inertia handling, adaptive barrier updates (NWW 2009), linear-solver choice (Schenk 2007/2008; Tasseff et al. 2019), the C++ rewrite, circuit tuning (FGCS 2005), PDE-constrained optimization (SISC 2008/2010) and two-stage decomposition (2020/2026).
- **P3. Counterexample → class → assumption audit → remedy with proof** (SW1 → SW2).
- **P4. Theory for the shipped algorithm, then an implementation paper with ablations and honest disclaimers** (SW2 → SW3).
- **P5. Structure exploitation through a flexible solver interface, not a bespoke solver.** Reduced-space options (thesis), inexact linear algebra (SW4), barrier smoothing so that off-the-shelf NLP solvers can be used (SW5, chance constraints 2020).
- **P6. New problem classes arrive through collaborators and co-advised students**: IBM customers, the CMU MINLP team, Nelson/Staum, Wei, LANL (§1.4).
- **P7. Heuristics are admitted as heuristics.** They are named, justified by observed failure modes ("We also noticed that in some cases the full step … is rejected in successive iterations"), measured in ablations, and never passed off as theory.

---

## Contradictions (kept, not reconciled)

1. **Ipopt dates.** The homepage says Ipopt "was first released as FORTRAN code in 2000" and "reimplemend in C++ in 2005-2006 at IBM by Carl Laird and myself". The Ipopt docs say it has "been actively developed under COIN-OR since 2002", and that Laird "came to the Mathematical Sciences Department at IBM Research as a summer intern in 2004 and 2005" when "the code was re-implemented from scratch". So the rewrite is dated 2004–2005 in one source and 2005–2006 in the other.
2. **Year of the IPOPT paper**: 2005 (OpenAlex; Crossref online date 28 Apr 2005) vs 2006 (print issue 106(1), March 2006; DBLP; CV). Its title also differs: in the CV's award list it is "On the implementation of a primal-dual interior point filter line search algorithm…", which is not the published title.
3. **Issue number of the SW1 paper**: the CV says *Math. Program.* 88(2):565–574; Crossref says 88(3).
4. **Title of the adaptive-barrier paper**: CV "Adaptive barrier strategies for nonlinear interior methods" vs published "Adaptive Barrier Update Strategies for Nonlinear Interior Methods".
5. **Current affiliation.** The homepage banner says "I moved to Gurobi Optimization", and Gurobi introduced him as its speaker in Feb 2026. Yet arXiv v3 of 2501.11700 (26 Feb 2026) and arXiv 2607.16430 (17 Jul 2026) still give his affiliation as Northwestern, with a northwestern.edu address. Move date unknown.
6. **Filter vs merit function, strength of the claim.** The 2002 thesis abstract says "the new filter approach seems superior to those based on merit functions". The 2004 IPOPT preprint finds a clear robustness gain but that on problems both options solve "The filter option seems to be only slightly more efficient", and a Full-Step variant solved 86.1% of problems.
7. **Citation counts disagree across aggregators**: Bonmin 908 (OpenAlex) vs 383 (S2); Couenne 607 vs 707; IPOPT 9,727 vs 10,205. Profile contamination affects both aggregators (§0).
8. **Namesake contamination** in DBLP (one TU Darmstadt record) and in OpenAlex, S2 and arXiv (§0). The OpenAlex "first/last author" statistics also contradict what the author lists actually show, because of alphabetical ordering (§1.3).

## Gaps

- **Google Scholar profile** (`Y1EdzIwAAAAJ`): captcha redirect on both WebFetch attempts. No Scholar citation counts and no Scholar-based publication list.
- **Published versions not read** (paywalled): SW1 (read via the thesis), SW2 (thesis chapters and abstracts), SW3 (preprint only), SW4 and SW5 (abstracts only). The CAPD report B-00-06 PDF could not be text-extracted (**not read**).
- **Bonmin and Couenne**: his specific contribution is not documented in anything read. Not dissected for that reason, although they are his 2nd and 3rd most-cited papers.
- **Self-assessment of his most important work**: no interview, essay or retrospective found within the 2-search budget. The only stated evidence is the ordering on his homepage research page and the CV award list.
- **Rejections, referee reports, errata**: none found; not systematically searched.
- **Gurobi period**: move date, role (a WebSearch snippet mentioned a "Senior Developer" LinkedIn title; LinkedIn not opened, so it stays unverified ⚠️) and any public output on Gurobi 13.0's NLP algorithm are **not found**.
- **CV vintage**: the CV PDF dates from about 2020 (items "to appear 2020"), so talks, grants and service after 2020 are missing.
- **Students' theses and student recollections**: not read here (agent 04's task).
- **LANL CNLS tutorial slides** (June 22, 2020, 4 parts, homepage): part 1 downloaded and skimmed only for date and scope; content **not read** (agent 02's task).
- Semantic Scholar batch endpoint returned HTTP 429; per-paper abstracts came from OpenAlex instead.
- The patents (US 8266554B2, 8719735B2) are listed from the CV only and were not checked against a patent database.

## Sources

Primary = his own writing, code documentation, or bibliographic records of his own papers; secondary = aggregators or third parties.

1. Andreas Wächter, homepage index, research, students, publications, software and CV pages, users.iems.northwestern.edu/~andreasw/ (fetched 2026-09-28): https://users.iems.northwestern.edu/~andreasw/ (primary)
2. Andreas Wächter, "Curriculum Vitae: Andreas Wächter, Ph.D." (PDF, c. 2020): https://users.iems.northwestern.edu/~andreasw/pubs/CV.pdf (primary)
3. A. Wächter, "An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering", PhD thesis, Carnegie Mellon University, 29 Jan 2002: https://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf (primary)
4. A. Wächter, L. T. Biegler, CAPD Technical Report B-00-06, CMU, 2000: https://users.iems.northwestern.edu/~andreasw/pubs/CAPD_B0006_QN-IP.pdf (primary; not read, extraction failed)
5. A. Wächter, L. T. Biegler, "On the Implementation of an Interior-Point Filter Line-Search Algorithm for Large-Scale Nonlinear Programming", IBM Research Report RC 23149, 12 Mar 2004: https://optimization-online.org/2004/03/836/ (primary; read in full)
6. Published version: *Math. Program.* 106(1):25–57, 2006, DOI 10.1007/s10107-004-0559-y (primary; record checked via Crossref, text not read)
7. A. Wächter, L. T. Biegler, *Math. Program.* 88(3):565–574, 2000, DOI 10.1007/PL00011386 (primary; record checked via Crossref)
8. A. Wächter, L. T. Biegler, *SIAM J. Optim.* 16(1):1–31 and 32–48, 2005, DOIs 10.1137/S1052623403426556, 10.1137/S1052623403426544 (primary; abstracts via OpenAlex)
9. F. E. Curtis, O. Schenk, A. Wächter, *SIAM J. Sci. Comput.* 32(6), 2010, DOI 10.1137/090747634; Optimization Online 2009/02/2227 (primary; abstract)
10. F. E. Curtis, J. Huber, O. Schenk, A. Wächter, *Math. Program.* 136(1), 2012, DOI 10.1007/s10107-012-0557-4; Optimization Online 2011/04/2992 (primary; abstract)
11. F. E. Curtis, J. Nocedal, A. Wächter, *SIAM J. Optim.* 20(3), 2009, DOI 10.1137/08072471X; Optimization Online 2008/05/1984 (primary; abstract)
12. S. Tu, A. Wächter, E. Wei, *IEEE TPWRS* 36(1), 2021, DOI 10.1109/TPWRS.2020.3002189, arXiv:2002.08003 (primary; abstract)
13. Y. Lou, X. Luo, A. Wächter, E. Wei, *SIAM J. Optim.* 36(3), 2026, DOI 10.1137/25M1728661, arXiv:2501.11700 (primary; abstract and arXiv HTML affiliations)
14. arXiv abstract/HTML pages for 2607.16430, 2502.11302, 2405.11400 and 2501.11700, fetched 2026-09-28: https://arxiv.org/abs/2607.16430 etc. (primary)
15. arXiv author search "Wächter, Andreas" / "Waechter, Andreas": https://arxiv.org/search/?query=W%C3%A4chter%2C+Andreas&searchtype=author (primary records; 4 namesake items excluded)
16. OpenAlex abstracts and bibliographic records for 22 key DOIs (batch query, 2026-09-28): https://api.openalex.org/works (secondary)
17. Crossref records for DOIs 10.1007/PL00011386, 10.1007/s10107-004-0559-y, 10.1137/S1052623403426556, 10.1016/j.disopt.2006.10.011, 10.1137/1.9781611974683.ch17, 10.1007/s12532-016-0101-2: https://api.crossref.org/works/ (secondary)
18. DataCite record via doi.org for A. Wächter, "Short Tutorial: Getting Started With Ipopt in 90 Minutes", 2009, DOI 10.4230/DagSemProc.09061.16 (primary record)
19. DBLP SPARQL, person 62/4235, 50 records, fetched 2026-09-28 by scripts/dblp_works.py: https://dblp.org/pid/62/4235.html (secondary)
20. OpenAlex author profiles A5112274231, A5067291755, A5144432222, fetched 2026-09-28; summary in ../sources/publications/publications.md (secondary; contaminated, see §0)
21. Semantic Scholar author profiles 1745824 and 31008035, fetched 2026-09-28: https://api.semanticscholar.org/graph/v1/author/1745824/papers (secondary; contaminated)
22. COIN-OR Ipopt documentation, index ("History of Ipopt", citation request), v3.14.20: https://coin-or.github.io/Ipopt/ (primary)
23. COIN-OR Ipopt documentation, "Authors and Contributors": https://coin-or.github.io/Ipopt/AUTHORS.html (primary)
24. A. L. Tits, A. Wächter, S. Bakhtiari, T. J. Urban, C. T. Lawrence, Optimization Online 2002/07/509 entry (UMD ISR TR 2002-29), published *SIAM J. Optim.* 14(1), 2003, DOI 10.1137/S1052623401392123: https://optimization-online.org/2002/07/509/ (primary for the Tits et al. statement; observed)
25. X. Liu, J. Sun, "A Robust Primal-Dual Interior-Point Algorithm for Nonlinear Programs", NUS manuscript, Jan 2002: https://optimization-online.org/2002/01/436/ (secondary; observed reception)
26. Optimization Online search results for "Wächter" and "inexact step computations", 2026-09-28: https://optimization-online.org/?s=W%C3%A4chter (secondary)
27. COIN-OR, "IPOPT Wins the Wilkinson Prize for Numerical Software", 7 Apr 2011: https://www.coin-or.org/2011/04/07/ipopt-wins-the-wilkinson-prize-for-numerical-software/ (secondary)
28. INFORMS, "INFORMS Computing Society Prize" winners page (2009 entry): https://www.informs.org/Recognizing-Excellence/Community-Prizes/INFORMS-Computing-Society/INFORMS-Computing-Society-Prize (secondary)
29. Gurobi, "Local Nonlinear Optimization in Gurobi 13.0" webinar page (event 18 Feb 2026): https://www.gurobi.com/resources/webinar-events/local-nonlinear-optimization-in-gurobi-13-0 (secondary)
30. Gurobi, "Our Team" (old site), bio of Andreas Waechter: https://www-old.gurobi.com/company/our-team/ (secondary)
31. ORCID public record 0000-0002-3278-5637 ("Andreas Waechter", no public works): https://orcid.org/0000-0002-3278-5637 (secondary; not tied to him ⚠️)
32. A. Wächter, "Numerical Nonlinear Optimization, Part I", CNLS tutorial slides, Los Alamos, 22 Jun 2020: https://users.iems.northwestern.edu/~andreasw/pubs/CNLStutorial_1.pdf (primary; skimmed for date and scope only)
33. Google Scholar profile Y1EdzIwAAAAJ: https://scholar.google.com/citations?user=Y1EdzIwAAAAJ (not read; captcha)
34. WebSearch result lists (2 queries: Gurobi move; Wilkinson Prize 2011), 2026-09-28, used only to locate items 27, 29 and 30 (secondary)
