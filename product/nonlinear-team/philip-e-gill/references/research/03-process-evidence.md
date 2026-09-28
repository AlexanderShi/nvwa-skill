# Philip E. Gill · 03 Process evidence: what the papers, reports, manuals and code show he (and his group) actually did

- **Researcher**: Philip E. Gill, Department of Mathematics, UC San Diego (at UCSD since 1988; earlier NPL and Stanford SOL). Living; distilled from public academic output only.
- **Dimension**: research agent 03 of 06 (process evidence: behaviour, not statements), nuwa research-craft mode.
- **Research date**: 2026-09-28
- **Sources consulted**: 41 (listed under "Sources"; 38 primary, 3 secondary or bibliographic aggregators). WebSearch calls used: 2 (both found only material already known or leads; nothing below depends on a search snippet).
- **Local corpus**: `references/sources/{papers,essays,software}` held only `.gitkeep`. `talks/` held the auto-caption transcript of the 2019 INFORMS interview with Margaret H. Wright saved by agent 01 (a web source, not user-supplied). No user-supplied material existed, so nothing below is "from user-supplied material". `private/` was not opened.
- **What was actually read** (full text, or the stated sections): the numerical sections, appendices and front matter of 14 papers and 12 technical reports; four SNOPT user guides (5.3 of 1997, 6.1 of 2002 interface chapter only, 7.5 of 2015, 7.7 of 2018), the NPSOL 5.0 and DNOPT 4 guides; the git history, file trees, READMEs and test scripts of six public repositories of the GitHub organisation `snopt`; the UCSD optimizers website; four arXiv version histories; three Optimization Online preprints compared with their journal versions. Anything not read is marked "not read".
- **Page convention**: "p. N" is the page of the PDF file named in Sources; where the PDF is the typeset journal article, the journal page is given as "journal p. N".
- **Tag legend**: [practice] what the papers, reports, manuals, code or records show was done; [stated] words of the authors (used here only to document a practice, e.g. a protocol sentence); [observed] what a third party reports; [inferred] my inference, with its basis. Each item also says primary (P) or secondary (S).
- **Attribution caveat (read before using any item as "Gill's" habit)**: every work below is co-authored and the author lists are alphabetical (see 01 §0), so the papers cannot tell which co-author did which step. In the public code, Gill has **no commits at all** (§5.2). What this file documents is therefore the practice of *the groups Gill led or belonged to*. Where the evidence narrows the actor (e.g. a student's thesis-era code, an application group's paper), the item says so.

---

## 0. Summary of the strongest process findings

1. **Whole-collection testing with a dated snapshot, named exclusions and a size filter** is the constant experimental protocol from 2002 to 2024 (table in §1.1). What changes over time is the *baseline*: none external (SNOPT 2002/2005), one external solver with published option files (SNOPT vs IPOPT, 2015), then mostly in-house predecessors and ablations for MATLAB prototypes (2016–2024).
2. **Numbers are kept out of the paper and put into companion reports.** Per-problem tables live in separate "Supplementary Numerical Results" reports (SQIC 2014, CCoM 20-08, CCoM 22-03) and derivations for every constraint format live in separate "Equations"/"Note on the Formulation" reports (CCoM 19-04 is 109 pages). Journal papers present a simplified problem and point to the reports (§4.1).
3. **Failures are counted, named, re-run and diagnosed**, and the diagnosis becomes the next design (SNOPT's degrees-of-freedom weakness → SQIC's hybrid QP method; missing second derivatives → convexification in DNOPT and the announced SNOPT9) (§2.3).
4. **Theory claims are tested on problem classes chosen to break them** (degenerate CUTEst subsets, competitors' own degenerate test sets, MPECs), with estimated order of convergence tables, and mixed results are reported as mixed (§1.7).
5. **Claims shrink between preprint and journal**: a 2011 preprint's "significantly more efficient than … SNOPT" does not reappear in the 2013 SIOPT paper; a 2018 preprint without numerics becomes a 2020 paper with a new title and an IPOPT comparison (§3.5).
6. **The software is engineered for users over decades**: diagnosis advice in the exit messages kept almost word for word from 1997 to 2015; backward-compatible interfaces; a regression suite that deliberately includes infeasible and memory-failure cases; a deprecation announced one version before removal (§5).
7. **Scoring rules drift and are not reconciled**: the same two CUTEst problems (fletcher, lootsma) are "failures" in 2005 and "successful" in 2015 (Contradictions 1).

---

## 1. Experiment design and execution (framework layer 4)

### 1.1 The test protocol across 22 years (one row per work; every cell read in the source)

| Work (identifier) | Code tested; language; machine | Test set and snapshot | Selection and exclusions | Baseline(s) | Limits | Where the per-problem data are |
|---|---|---|---|---|---|---|
| SNOPT, SIOPT 2002 (DOI 10.1137/S1052623499350013) | SNOPT, Fortran | "The CUTE distribution of 01/May/2001 contains 945 problems" (p. 18); COPS 2.0 (17 problems) | default SIF dimensions | none external | — | in the paper |
| SNOPT, SIAM Rev. 2005 (DOI 10.1137/S0036144504446096) | "SNOPT 7.1 of January 2005" (journal p. 119); g77 `-O`; Linux PC, 2 GB RAM, two 3.06 GHz Xeon, one used per problem | "The CUTEr distribution of December 20, 2004, contains 1020 problems" (journal p. 120); COPS 3.0 (22) | 4 excluded for undefined variables / floating-point exceptions, 5 "too large for the SIF decoder" (journal p. 120); 1007 attempted, split by nZ ≤ 2000 vs > 2000 (Table 3, journal p. 121) | none external | 2000 major iterations | in the paper |
| Erway, Gill, Griffin, SIOPT 2009 (DOI 10.1137/070708494) | Steihaug–Toint and phased-SSM, both in MATLAB | CUTEr unconstrained problems of variable dimension, n = 1000: "The test set was constructed using the CUTEr interactive select tool" (journal p. 1123) | 49 problems | Steihaug–Toint (re-implemented in the same MATLAB environment) | — | in the paper |
| Gill & Robinson, SIOPT 2013 (DOI 10.1137/120882913) | "Numerical results from a simple MATLAB implementation of pdSQP" (journal p. 2005) | 158 CUTEr problems: 111 of the 126 HS problems + 47 equality-constrained problems from an earlier study | 15 HS problems excluded by name with reasons (no general constraints, nonsmooth, …) | none external in the paper | kmax = 600 | "Detailed results … may be found in Gill and Robinson" (report; journal p. 2007) |
| Gill & Wong, MPC 2015 (DOI 10.1007/s12532-014-0075-x) + supplementary report (2014) | SQIC, Fortran 2008; gfortran 4.8.2 `-O`; iMac 3.4 GHz i7, 16 GB | "A total of 253 QPs were identified from the CUTEst" (suppl. p. 1) | "No linear programs were tested because all of the codes under consideration revert to the simplex method when the objective is linear." (suppl. p. 1); small/large split by final number of superbasics | own SQOPT on 145 convex QPs; three linear solvers (LUSOL, MA57, UMFPACK); default vs "forced" block-matrix mode | 5000 s ("In practice, the 5000 second limit is not exact since the time limit is checked every twenty iterations", suppl. p. 1) | supplementary report, Tables 2–13 |
| Gill, Saunders, Wong 2015 (DOI 10.1007/978-3-319-23699-5_5) | SNOPT 7.4 vs IPOPT 3.11.8 with MA57; "Both IPOPT and SNOPT7 were compiled using gfortran 4.6" (p. 6); MacPro 12-core, 64 GB | "The CUTEst distribution of January 14, 2015 (Subversion revision 245) contains 1156 problems" (p. 7) | 3 excluded (floating-point exceptions); nonsmooth, unbounded, infeasible kept and listed | IPOPT, first- and second-derivative modes; both option files printed (Fig. 1, p. 8) | 1800 s | tables and profiles in the paper |
| Forsgren, Gill, Wong, MP 2016 (DOI 10.1007/s10107-015-0966-2; CCoM 15-02 rev.) | PDQP in MATLAB | 143 convex CUTEst QPs with min(m, n) of order 500 or less, plus 16 LPs | 5 infeasible problems kept | own SQOPT: "All SQOPT runs were made using the default parameter options" (p. 25) | — | Table 1 in the report |
| Gill, Kungurtsev, Robinson, MP 2017 (DOI 10.1007/s10107-016-1066-7) | pdSQP, "a preliminary implementation of the method written in MATLAB" (journal p. 404) | degenerate classes (§1.7) | chosen to violate LICQ / strict complementarity | results of other groups' codes on the same sets | kmax = 1000 | in the paper |
| Gill, Kungurtsev, Robinson, SIOPT 2020 (DOI 10.1137/19M1247425) | "simple MATLAB implementation of procedure PDB" (journal p. 1088); KKT factorised with MATLAB `LDL` (MA57) | 124 of 126 HS problems + 16 COPS | "The two excluded problems are hs87, which is nonsmooth, and hs99exp, which is poorly scaled" (journal p. 1088) | IPOPT | 500 iterations | CCoM 19-03, Tables 2–3 |
| Gill & Runnoe, CCoM 22-04 (2022, rev. 2023) | nine BFGS variants; "The code for each solver was written in MATLAB version R2019b" (p. 26); analysis in Python (NumPy, Pandas, Matplotlib, Seaborn); "All computations were carried out on a 2017 MacBook Pro" (p. 26), 8 GB | 275 CUTEst unconstrained problems with n ∈ [2, 5000] | "every single" such problem (p. 25) | the nine variants against each other, including a published method from another group (§3.4) | 3000 iterations | in the report |
| Ferry, Gill, Wong, Zhang, OMS 2023 (DOI 10.1080/10556788.2023.2241769) + CCoM 20-08 | LRHB-qWolfe and LRHB-qArmijo (Fortran package LRHB) | "As of July 1, 2020, the CUTEst test set contains 154 bound-constrained problems" (CCoM 20-08 p. 1), default dimensions | none | L-BFGS-B, "to provide some measure of the efficiency of the projected-search method relative to a state-of-the-art method" (preprint p. 22) | 3600 s, 10⁶ iterations; identical termination rule for all three solvers | CCoM 20-08 |
| Gill & Zhang, COAP 2024 (DOI 10.1007/s10589-023-00549-1) + CCoM 22-03 | pdProj, pdbAll, pdb in MATLAB R2022b; iMac Pro, 128 GB, macOS 12.6.8 | HS 126, BC 139, LC 212, NC 648, QP 141 | "a problem was chosen if the associated KKT system was of the order of 2000 or less" (CCoM 22-03 p. 5); lhaifam omitted for a floating-point exception | in-house only: pdb (the 2020 method) and pdbAll (the new method without projection) | 500 iterations | CCoM 22-03 (100 pages) |
| Brust & Gill, SISC 2024 (DOI 10.1137/23M1623380; arXiv 2312.06884) | LDLtr in MATLAB and Fortran 90 | 252 CUTEst unconstrained problems with n of order 5000 or less | same size rule used to set variable dimensions | bfgsR: "This algorithm is the state-of-the-art line-search BFGS implementation considered by Gill & Runnoe" (preprint p. 12) | 6000 iterations; "near optimal" outcome defined | per-problem table in the preprint |

Tags and reading: [practice · P] for every cell. Era: the machines are single desktops or laptops throughout (2 GB Linux PC in 2005, 8 GB MacBook Pro in 2022, 128 GB iMac Pro in 2023). No cluster runs appear in any numerical section read.

What the table shows [inferred from the rows, each checked above]:
- **The snapshot is always dated or versioned** (distribution date, Subversion revision, "As of July 1, 2020"), and **default SIF dimensions** are the rule. When a size cap is imposed it is stated as a rule on n, on min(m, n) or on the order of the KKT matrix.
- **Exclusions are few and named, with a reason each.** Nonsmooth, unbounded and infeasible problems are usually *kept* and listed rather than removed (GSW15 p. 7; CCoM 22-03 p. 5; SIAM Rev. 2005 journal p. 121).
- **Hardware, compiler, flags and solver versions are reported in almost every numerical section after 2005.**

### 1.2 How baselines are chosen: an arc from "no competitor" to "in-house predecessor"

- **2002/2005: no external solver.** Both SNOPT papers report SNOPT alone on the whole CUTE/CUTEr and COPS sets. The only reference points are the known properties of the problems (feasible or not, bounded or not). [practice · P]
- **2015: one external solver, made comparable by construction.** Printed option files for both codes (GSW15 Fig. 1, p. 8). IPOPT kept at defaults: "With the exception of an 1800-second time-limit, all IPOPT runs were made using the default options." (p. 8). SNOPT's optimality tolerance was loosened to IPOPT's default (quoted in 02, E2). Where the comparison is deliberately asymmetric (first-derivative SNOPT vs second-derivative IPOPT, §3.5 of GSW15), the section title says so. [practice · P]
- **2016–2024: MATLAB prototypes are compared with the group's own earlier codes.** PDQP vs SQOPT at defaults (2016); SQIC vs SQOPT (2015); pdProj vs pdb (the 2020 method) and pdbAll (2024); LDLtr vs bfgsR, the best method of the group's own 2022 BFGS study (2024). External comparisons appear in 2020 (IPOPT) and 2023 (L-BFGS-B). [practice · P]
- **Chained baselines.** The 2024 COAP paper does not compare with IPOPT and instead points back to the 2020 paper: "This reference provides some numerical examples that illustrate the performance of the method compared to the widely-used interior-point method IPOPT." (p. 6). [practice · P] My reading: the external comparison is made once per line of methods, and later methods are compared with the in-house predecessor. [inferred]
- **Borrowed components of the competitor.** FGWZ's quasi-Wolfe search sorts kink steps with a heapsort "adapted from a Fortran implementation by Byrd et al." (p. 22), i.e. from the L-BFGS-B authors, and L-BFGS-B is also the baseline. [practice · P]

### 1.3 Ablation by component

- **pdProj (2024)**: three codes that differ by one feature each, namely pdb (primal shifts only), pdbAll (primal and dual shifts, no projection) and pdProj (both plus projected search). The results report states the finding per component: "The results show that the all-shifted method is more efficient than the method that shifts only the primal variables." (CCoM 22-03 p. 1). [practice · P]
- **SQIC (2015)**: the same QP method with three third-party linear solvers, and with the default mode against a "forced" block-matrix mode. A separate table switches the "phase 3" option on and off (gqp.pdf p. 31). [practice · P]
- **Line searches (2023)**: LRHB-qWolfe vs LRHB-qArmijo, the same code with only the line search changed. [practice · P]
- **BFGS variants (2022)**: all nine variants inside one MATLAB code base with shared constants (Table 1, p. 26). [practice · P]

### 1.4 Prototype in MATLAB, production in Fortran; parameters set on the test collection itself

- New-method papers since 2009 test **MATLAB prototypes** and call them so ("simple MATLAB implementation", "preliminary implementation"). The software papers test **Fortran production code** (SNOPT, SQIC, LRHB). BG23 is the exception: it reports both ("The algorithm is implemented in Matlab and Fortran 90. All software is available in the public domain.", p. 11). Where that software is published was not found (Gaps). [practice · P]
- **Parameter tuning on the evaluation set.** PDB 2020: the control parameters "were chosen based on the empirical performance on the entire collection of problems" (journal p. 1089), and the same 140 problems are then used for the comparison with IPOPT. [practice · P] No held-out set appears in any paper read. [inferred]
- **Starting points**: CUTEst defaults, with x₀ projected onto the bounds (PDB 2020, journal p. 1089; pdSQP 2013). [practice · P]

### 1.5 Instrumentation: count what the algorithm is doing, not only whether it succeeded

- pdSQP 2013 and PDB 2020 report the share of each iteration type (O-, F-, M-, V-iterates) and the percentage of iterations in which the Hessian had to be modified, per problem in the reports and in aggregate in the papers. PDB 2020: in the three COPS failures (glider, robotarm, rocket) "respectively 100%, 99%, and 98% of the iterations required the Hessian to be modified", and 41 of the 124 HS problems needed modification (journal p. 1091). pdSQP 2013 notes that for mss1 "99% of the iterations required some form of convexification" (journal p. 2007). [practice · P]
- The counts are used to support design claims. For M-iterates: "M-iterates generally constitute significantly less than 1% of the total iterations" (pdSQP 2013, journal p. 2007). The IMA JNA 2017 paper reuses this to justify a rule ("Numerical results given by Gill et al. (2014) indicate that M-iterates occur infrequently relative to the total number of iterations", journal p. 418). [practice · P]
- SQIC's tables record the number of factorizations of each matrix (bFac, nFac) next to iterations and time (suppl. p. 1). [practice · P]

### 1.6 Making the test problems well posed for comparison

- **Feasibility problems get an objective**: "In an attempt to create a unique solution for comparison purposes, all the feasibility problems were modified to find the feasible point of least Euclidean length." (CCoM 22-03 p. 5). [practice · P]
- **"Unknown feasibility" is handled explicitly**: problems with no known feasible point are listed by name, some with the perturbation that makes them feasible ("nash is feasible if the constraints are perturbed by 10⁻⁴", CCoM 22-03 p. 5). [practice · P]
- **Warning against family effects**: "Typically, a method will behave in a similar way on all the problems of one type, which can distort any numerical comparison between methods." (CCoM 15-02 rev., p. 26, citing LISWET1–LISWET14). [stated about their own results · P]
- **Test-set representativeness questioned (2009)**: "The unconstrained examples in the CUTEr set are dominated by functions that are relatively inexpensive to evaluate. Many involve taking a prototype low-dimensional problem and extending it to an arbitrary number of dimensions." (Erway–Gill–Griffin, journal p. 1126). [stated · P]

### 1.7 Experiments designed to test a theoretical claim on the class it targets

- MP 2017 (superlinear convergence of stabilized SQP) is tested only on degenerate problems. "In particular, 84 problems were identified for which the active-constraint Jacobian is numerically rank deficient at the computed solution" (journal p. 404), plus 56 with a negligible multiplier on an active bound and 26 failing both conditions. The measure is an estimated order of convergence (EOC) table, split by whether the last step was a "global" or a "local" descent direction (Table 2, journal p. 405). [practice · P]
- **Competitors' test sets are reused**: the 12 degenerate problems of Mostafa, Vicente and Wright (LNCS 2861, 2003, DOI 10.1007/978-3-540-39901-8_10, not read): "Algorithm pdSQP was tested on ten of the twelve problems that could be coded directly or obtained from other sources." Outcome: superlinear on 7, linear on 2, failure on 1, "similar to those obtained by Mostafa, Vicente and Wright" (journal p. 406). Also 86 MPECs obtained from Sven Leyffer (78 solved) and the DEGEN subset used by Izmailov and by Izmailov and Solodov (journal pp. 406–407). [practice · P]
- **A theory-safe variant is tested**: "All the results are from a variant of the method that does not test for a direction of negative curvature until a first-order stationary point is located." (journal p. 402). [practice · P]
- **Mixed results stay mixed** in the conclusion: "Results are more mixed for problems that do not satisfy the property of strict complementarity." (journal p. 408). [practice · P]

### 1.8 Application work: minimal change to the optimizer, a scalable test problem, the solver as a verification tool

- **1998–2000, optimal control with Petzold's group** (NA 98-1; J. Comput. Appl. Math. 120 (2000) 197–213, DOI 10.1016/S0377-0427(00)00310-1). Design constraint: "There is a strong motivation to be able to adapt such an optimization code to our optimal control algorithm with a minimum of changes to the optimizer" (p. 3). "The transformation is cast almost entirely at the user level and requires minimal changes to the optimization software." (abstract, p. 1). The single test problem was chosen because it scales: "This test problem has the property that the size of the optimization problem can be increased by simply using a finer spatial grid." (p. 14). Era: NSF and DOE grants, San Diego Supercomputer Center and NERSC resources (p. 1 footnote). [practice · P]
- **2018, vehicle and fluid-container control with Gerdts' group** (DCDS-S 11 (2018) 1259–1282, DOI 10.3934/dcdss.2018071; Gill second author, so this is an application group's paper). SNOPT is used first for "the model verification process" (p. 2). The group's new structure-exploiting methods are then compared with SNOPT and mostly lose: "Despite the fact that SNOPT does not rely on exact second derivative information, it requires much less computing time than Method (A) in most cases" (p. 22). [practice · P; Gill's personal role not identifiable]

---

## 2. Debugging and diagnosis (layers 4–5)

### 2.1 The diagnosis procedure is encoded in the software's exit messages

- **SNOPT 5.3 (October 1997)** has a flat list of `inform` codes 0–44 (pp. 15–16). **SNOPT 7.5 (December 2015)** has a two-level taxonomy, "SOLVER EXIT e" plus "SOLVER INFO i", grouped by cause: 0 finished, 10 infeasible, 20 unbounded, …, 40 numerical difficulties, 50 errors in user-supplied functions, 60 undefined functions, 70 user termination, 90–140 input/system errors (§8.6, pp. 93–98). [practice · P]
- **The advice is ordered by likelihood and has barely changed in 18 years.** For "the current point cannot be improved" both guides list three causes in the same order and with the same example. First, inaccurate gradients ("This is the most likely cause", 5.3 p. 59; 7.5 p. 96). Second, low precision, e.g. accidental single precision. Third, noisy function values from an iterative process, where the remedy is to set `Function precision` and loosen the optimality tolerance. The 1997 text says "do your utmost to ensure that the subroutines are coded correctly" (p. 59). [practice · P]
- **Derivative checking is a guard**: exits 51/52 compare user gradients with forward differences, and "This exit is a safeguard because SNOPT will usually fail to make progress when the computed gradients are seriously inaccurate." (7.5 p. 97). [practice · P]
- **The NPSOL guide (SOL 86-6, "Revised June 4, 2001")** holds the most concrete debugging craft found: "It is remarkable how often the values x = 0 or x = 1 are used to test function evaluation procedures, and how often the special properties of these numbers make the test meaningless." (p. 40), and "since some compilers do not convert such constants to double precision, half the correct figures may be lost by such a seemingly trivial error." (p. 41). It also warns that gradient checking fails if the objective uses data computed by the constraint routine (p. 41). [practice · P, collective four-author voice; how far this text predates 2001 was not checked]

### 2.2 Re-examining one's own failures before counting them

- **2005**: of 19 problems declared infeasible, the two without known feasible points were re-solved with the `Feasible Point` option: "To gain further assurance that these problems are indeed infeasible, they were re-solved using SNOPT’s Feasible Point option" (journal p. 121). The final violations matched, and the paper says "We conjecture that these problems are infeasible." A declared "optimal" is qualified: "We emphasize that this point may not be a constrained local minimizer for the problem." (journal p. 121; hs13 and optmass are given as examples). [practice · P]
- **2013**: every failure of pdSQP is characterised. Six "terminated at infeasible local minimizers of the merit function". For lukvle8, "This problem can be solved successfully in 771 iterations", and mss1 in 2872 iterations (journal p. 2007). So failures were re-run beyond the iteration limit to find out what kind of failure they were. [practice · P]
- **2015**: SNOPT's 25 "false infeasibility" cases are split into 11 that solve at the default tolerance and 7 with a final sum of infeasibilities of order 10⁻⁵ (GSW15 p. 10). The failures stay in Table 2. [practice · P]
- **2014**: an SQIC failure is fixed by a parameter and reported as such: "problem UBH1 encountered numerical difficulties in block-matrix mode with HSL MA57, but was solved successfully with a setting of 10⁹ for the bound on the Schur-complement matrix." (SQIC suppl. p. 1). [practice · P]
- **2016**: the baseline's errors are named too: SQOPT "declared (incorrectly) that problems RDW2D51U and RDW2D52U are unbounded" (CCoM 15-02 rev., p. 25). So are the new method's accuracy shortfalls (RDW2D52B, RDW2D52F with final objectives given to 8 digits, p. 26). [practice · P]

### 2.3 From diagnosis to the next design (the clearest idea-generation trace; layer 3)

- **GSW15 (2015)**: the comparison with IPOPT is stratified by degrees of freedom. The finding: "on the 68 problems with ndf > 4000 only 24 problems are solved faster with SNOPT7" (p. 13). Cause named: the explicit reduced Hessian in the QP solver. Remedy named in the next sentence: "This inefficiency may be removed by using a QP solver that maintains an explicit reduced Hessian when the number of degrees of freedom is small, and uses direct factorization when the number of degrees of freedom is large." (p. 13), which is SQIC. The second weakness is isolated on the 296 unconstrained or bound-constrained problems, where the limited-memory Hessian is the bottleneck. The remedy is second derivatives with convexification (§4 of the paper), "the basis of the second-derivative solvers in the dense SQP package DNOPT … and the forthcoming SNOPT9" (p. 26). [practice · P]
- **SNOPT 2002 → 2005**: the 2002 paper ends with an "Extensions" section (§7, "Where possible, we have defined the SQP algorithm to be independent" of the QP solver, p. 22) listing approximate reduced Hessians, range-space and Schur-complement methods. In 2005, "Approximate Reduced Hessians" (§4.4) and "CG Methods" (§4.5) are part of the method, a new line-search safeguard "Bounding the Constraint Violation" (§2.8) appears, and the remaining ideas move to §8 "Alternative QP Solvers". [practice · P] The self-declared limit "(say, up to 2000)" degrees of freedom (2005 abstract) becomes, in the 7.5 guide: "unlike previous versions of SNOPT, there is no limit on the number of degrees of freedom." (p. 4). [practice · P]
- **PDB 2020**: the failure mechanism (near-singular KKT matrices, Hessian modified in almost every iteration) becomes the paper's closing lesson: "The results illustrate the crucial importance of an effective modification scheme when the KKT matrix does not have the correct inertia." (journal p. 1091). [practice · P]
- Earlier example (read by agent 01, not re-read here): the expensive TPP rank-detection failures on drcavty2 in SNOPT 2005 are the stated reason for SQOPT's "BR factorization" (01 §2.4). [practice · P, via 01]

### 2.4 Reaction to someone else's headline claim: test it on your own problems

- Khachiyan's ellipsoid method (1979): "it was always always in our examples way slower than the simplex method" and "we didn't ever write a paper about this in retrospect I wish we had because we had lots of numerical results about it" (Wright interview, auto-captions, transcript line 243). [observed · P for Wright, auto-caption wording approximate]
- Karmarkar (1984): the group looked for the connection to barrier methods and published an equivalence with numerical tests (Math. Prog. 36 (1986) 183–209, DOI 10.1007/BF02592025; not read). The interviewer summarises the numbers as "sometimes it is better than simplex and sometimes it's not" (transcript line 267, interviewer's words). [observed · P for the interview; the paper's own numbers not read]
- Andrei's adaptive scaled BFGS (Numer. Algorithms 77 (2018) 413–432, DOI 10.1007/s11075-017-0321-1; not read): re-implemented as bfgsN in the common MATLAB code. The group reports that on the 38 problems shared with Andrei's paper it looks best, and on all 275 problems it is "actually harmful to the methods performance" (GR22 p. 32; full quote in 02, J2). [practice · P]

---

## 3. Judging results (layer 5)

### 3.1 Outcome categories are explicit and fine-grained

- GSW15 Tables 2–3 separate "Optimal", "Optimal, but low accuracy", "Unbounded", "Infeasible constraints", "Locally infeasible constraints" (all successes) from "False infeasibility", "Iteration limit", "Time limit", "Numerical problems", "Final point cannot be improved" (failures). IPOPT's own exit categories are kept ("Restoration failed", "Too few degrees of freedom", …) (p. 12). [practice · P]
- SQIC marks "d" (dead point) and "w" (weak minimizer) per problem (suppl. p. 1). GR22 classifies outcomes as "optimal, near optimal but badly scaled, line search failure, or too many iterations" (p. 25). BG23 defines a "near optimal" category with a formula (p. 12). [practice · P]
- In profiles, a failure gets a fixed penalty: "If method s failed for problem p, then rp,s is set to be twice the maximal ratio" (CCoM 22-03 p. 6; same convention in GR22 p. 26). [practice · P]

### 3.2 Scoring rules change over time and the change is not flagged

- fletcher and lootsma (feasible problems whose starting points are infeasible and stationary for the sum of infeasibilities): 2005, "These problems are also listed as failures." (journal p. 122); 2015, "As this study does not recognize a qualitative distinction between a local and global solution, the outcomes for fletcher and lootsma are listed as successful." (GSW15 p. 10). No sentence in 2015 refers to the earlier rule. [practice · P] (Contradictions 1.)

### 3.3 Reporting where the new method loses

- "As expected, Figure 5 shows that SQOPT is the best solver for convex problems with a small number of superbasics." (Gill & Wong 2015, gqp.pdf p. 31). [practice · P]
- "The results indicate that, overall, the simple MATLAB code PDB usually requires fewer function evaluations than IPOPT but is slightly less robust." (PDB 2020, journal p. 1090). [practice · P]
- The method is applied outside its intended use and the results are published anyway: "Algorithm PDQP would not be recommended for solving a linear program" (CCoM 15-02 rev., p. 28), followed by 16 LP results. [practice · P]
- "The reader should exercise some care when interpreting these results." (same report, p. 26), about their own favourable 63% figure. [practice · P]

### 3.4 Judging another group's result: rerun it in the common environment, on the full set

See §2.4 (Andrei's method) and 02 J2. The behaviour is re-implementation plus a larger test set plus different metrics (function evaluations and iterations rather than CPU time only). [practice · P]

### 3.5 Claims pruned or added between preprint and journal (early vs final versions)

| Line of work | Early version | Final version | What changed |
|---|---|---|---|
| Regularized / stabilized SQP | Gill & Robinson, "Regularized Sequential Quadratic Programming", UCSD NA-11-02, Optimization Online 2011/10 (27 pp., sections: Introduction, Algorithm, QP subproblem, Convergence, Conclusions) | "A Globally Convergent Stabilized SQP Method", SIOPT 23 (2013), DOI 10.1137/120882913 (received June 29, 2012; accepted July 12, 2013) | The 2011 introduction says: "Preliminary numerical experiments on a subset of problems from the CUTEr test collection indicate that the proposed SQP method is significantly more efficient than our current SQP package SNOPT." (p. 5). The 2011 text has no numerical section. The 2013 paper adds §6 "Numerical results" (158 CUTEr problems, MATLAB) and claims only robustness ("Overall, the results indicate that the algorithm of pdSQP is robust", journal p. 2007). SNOPT appears in the 2013 paper only as a bibliography entry, cited for BFGS Hessians. Title "regularized" → "stabilized". [practice · P] Why the efficiency claim went is not stated (Gaps). |
| Second-order regularized SQP | arXiv 1205.2304 v1 (10 May 2012, 9 pp., submitted by Kungurtsev; PDF title "Direction of negative curvature for regularized SQP", listing title "Negative Curvature and Second-order optimality for regularized SQP"; author spelled "Phillip Gill"): "This note discusses the computation and use of a direction of negative curvature" (p. 1). Then Optimization Online 2013/10, "A Regularized SQP Method with Convergence to Second-Order Optimal Points" (32 pp.) | CCoM 13-04 "A Stabilized SQP Method: Global Convergence" ("June 2013 (Revised April 2024)"), IMA JNA 37 (2017) 407–443, DOI 10.1093/imanum/drw004 | The IMA JNA abstract covers the same ground as the 2013 preprint abstract: negative curvature in a flexible line search, finite termination, safeguarding relevant "only when the iterates are converging to an infeasible stationary point", second-order necessary conditions. [inferred: the second-order preprint was absorbed into the 2017 paper under a new title. This refines the "fate unknown" entry in 01 §3.] |
| Shifted penalty-barrier interior method | "A Shifted Primal-Dual Interior Method for Nonlinear Optimization", CCoM-18-1 (February 1, 2018), 24 pp.: sections 1–5 with "Implementation details" but **no numerical results** | CCoM 19-03 (March 1, 2019) and SIOPT 30 (2020), DOI 10.1137/19M1247425 (received February 28, 2019; accepted December 23, 2019): "A Shifted Primal-Dual **Penalty-Barrier** Method" | Numerical testing (MATLAB PDB vs IPOPT on 140 problems) was added before submission. Title reframed. A 109-page companion note (CCoM 19-04) was released the same day as the report. The journal acknowledges "three referees for constructive comments that significantly improved the presentation" (journal p. 1091). [practice · P] |
| Convex QP active-set methods | CCoM-15-02, "Active-Set Methods for Convex Quadratic Programming" (March 28, 2015); arXiv 1503.08349 v1 (28 Mar 2015, submitted by Forsgren) | arXiv v2 (30 Dec 2015); MP 159 (2016) 469–508, DOI 10.1007/s10107-015-0966-2, "Primal and dual active-set methods for convex quadratic programming" | Title sharpened. The March 2015 report version already has §7 with the MATLAB PDQP vs SQOPT numerics (the arXiv v1 PDF itself was not opened). The March and revised numbers were not diffed (Gaps). [practice · P] |
| Projected search (bound constraints) | arXiv 2110.08359 v1 (15 Oct 2021, submitted by Wong), "Projected-Search Methods for Bound-Constrained Optimization", journal-ref field "CCoM 21-01" | OMS 39 (2024 issue; online 2023-08-18) 459–488, DOI 10.1080/10556788.2023.2241769, "A class of projected-search methods …"; homepage lists it as CCoM 20-07 | Title and report number differ across the three records (Contradictions 7). [practice · P] |

### 3.6 Reports are maintained long after the journal version

CCoM 13-04 and 14-01 carry "(Revised April 2024)" although their journal versions appeared in 2016–2017. CCoM 22-03 is "June 2022, Revised September 2023". CCoM 22-04 is "July 1, 2022, Revised October 17, 2023". [practice · P] [inferred] The report, not the journal article, is treated as the living reference version.

---

## 4. Expression: how the output is packaged (layer 6)

### 4.1 Paper + "Numerical Results" report + "Equations" report

- **Results reports**: "Numerical results for SQIC: Software for large-scale quadratic programming" (July 13, 2014; linked from the solver page as "supplementary material"). CCoM 20-08 opens with "This document provides detailed information of the numerical results used to compile the performance profiles" (p. 1). CCoM 22-03 has 100 pages of per-problem tables. [practice · P]
- **Equations reports**: CCoM 19-04 (109 pp.): "This note derives the shifted primal-dual penalty-barrier merit functions and associated path-following equations for an optimization problem with constraints written in eight different ways" (p. 2). Also CCoM 21-04, "Line-Search and Trust-Region Equations for a Primal-Dual Interior Method for Nonlinear Optimization" (September 1, 2021), and CCoM 22-02, "Equations for a Projected-Search Path-Following Method for Nonlinear Optimization" (June 2022). Only their first pages were read; both state that the approximate Newton equations derived there are "equivalent to a regularized form of the conventional primal-dual path-following equations" under certain conditions (p. 1 of each). [practice · P]
- **The paper shows a simplified problem**: "For brevity, we consider the simplified problem" (CCoM 22-03 p. 2). PDB 2020 derives everything for (NIP) and handles the full CUTEst format by pointing to the note. [practice · P]
- **A pointer error**: the SIOPT 2020 paper sends readers to "[20, Tables 2 and 3] for detailed results for each problem" (journal p. 1090). Its reference [20] is CCoM 19-04, the equations note, which contains no numbered results tables. The tables are in CCoM 19-03, Tables 2–3. [practice · P] (Contradictions 5.)

### 4.2 Publication channels

- **Department report series first.** SOL reports, then UCSD NA and CCoM reports, and Optimization Online for some; arXiv is marginal. All five arXiv records found were **submitted by someone else**: Forsgren (1503.08349), Wong (2110.08359), Brust (2312.06884), Kungurtsev (1205.2304), and an ANL staff member for the SnadiOpt guide (cs/0106051). [practice · P] [inferred] Gill himself does not post to arXiv.
- **The manual is itself a citable report**, and users are told to cite it: the downloads page says "If you are using SNOPT for your own research, please cite the following publications:" and lists the 7.7 manual (CCoM 18-1) and the 2005 SIAM Review paper. [practice · P]

### 4.3 Documentation lineage and reuse

- The DNOPT 4 guide (August 2020) reuses the SNOPT abstract nearly verbatim, including "On large problems, DNOPT is most efficient if only some of the variables enter nonlinearly" (p. 1), for a solver the website describes as "Intended for small- to medium- scale problems". [practice · P] (Contradictions 10.)
- The 5.3 guide is labelled "DRAFT, October 1997" (p. 1). The 7.7 guide's running headers read "SNOPT 7.6 User’s Guide" (e.g. p. 8). The 7.5 guide has no "What's New" section; the 7.7 guide has one with two bullets (§1.8). [practice · P]

---

## 5. Software engineering and maintenance (layers 4 and 7)

### 5.1 Backward compatibility and staged deprecation

- "snOptB is the “basic” user interface with arguments identical to versions of SNOPT up to Version 5.3-4." (7.5 guide p. 31), with `snOpt` kept as an alias. DNOPT ships a `dnNPSOL` interface whose calling sequence mimics NPSOL: "The dnNPSOL interface is designed for the solution of small dense problems." (DNOPT guide p. 36). [practice · P]
- The f2c C translation was **announced for removal one version ahead**, "A f2c translation of SNOPT to the C language is still provided, although this feature will be discontinued in the future" (7.5, December 2015, p. 1), and then removed: "The f2c’d version of SNOPT is no longer included in the distribution." (7.7, March 2018, p. 8). [practice · P]
- A user-reported class of failure is fixed in the interface, not left to users: new `snInitF`/`snSpecF` routines open files by name because with shared libraries "users may get unexpected results with Fortran unit numbers"; "These subroutines will eliminate this issue by handling unit numbers internally." (7.7 p. 8). [practice · P]

### 5.2 Who writes the public code

Git histories of the six repositories of `github.com/snopt`, cloned 2026-09-28 (all history, `git log --all`):

| Repository (created) | Commits | Authors |
|---|---|---|
| snopt-matlab (2014-10-20) | 103 | Elizabeth Wong 102, one external contributor 1 |
| snopt-interface (C/C++ API, 2014-10-03) | 82 | Wong 80, two external contributors 1 each |
| snopt-python (2015-02-10) | 43 | Wong 42, one external contributor 1 |
| snopt7-examples (2018-04-17) | 5 | Wong 5 |
| SNOPT7.jl (2018-09-18) | 16 | Wong 9, Ziang Liu 5, Eric Heiden 2 |
| snctrl (optimal-control interface, 2015-04-28) | 4 | Wong 4 |

- **Gill has zero commits**, and the repositories hold interfaces and examples only; the solver source is licensed and not public. [practice · P] [inferred] Division of labour: Gill (with Murray and Saunders) owns algorithms and manuals; Wong, his former PhD student and long-term co-author, owns interfaces, packaging and user-facing examples. Gill's personal coding practice cannot be observed (Gaps).
- snopt-matlab's commit messages are mostly user-facing fixes and interface redesigns, e.g. "fixed LPs being passed to SQOPT; add explicit lp call" (2018-01-18). Version 3.0 is documented as "Changes from version 2.5: * all-in-one calls to SNOPT (for NLPs) and SQOPT (for LPs and QPs)" (README). The repository also ships an fmincon-style wrapper (`matlab/util/solve_snfmincon.m`, `examples/fmincon/`), lowering the switching cost for MATLAB users. [practice · P]

### 5.3 The regression suite tests the failure paths on purpose

- `snopt7-examples/fortran/check` runs 54 example programs; `check.log0` is the reference output (header "S N O P T  7.6.1    (Apr 2017)", 10,194 lines). Besides the classic MINOS-era models (t1diet … t7etamacro, MPS files adlittle, pilot4, refinery) and optimal-control problems (spring, catmix), it includes **deliberately infeasible variants**: `hs47ModInfa.f` is "hs47Modc with the bounds changed to give an infeasible problem" ("12 October 2014: First version"); also hs76ModInf and hs76QNModInf. It also has memory tests (snmemtesta/b), a hot start (catmixb_hot), a user stop (catmixc_stop), pure feasibility runs (snfeasa/b), and a driver for "the stand-alone derivative checker" (snchka.f, "01 Jun 2006: First version"). [practice · P]
- The reference log therefore expects non-success exits: in `check.log0`, "EXIT 10 -- the problem appears to be infeasible" appears 8 times (SNOPTA 5, SNOPTB 2, SQOPT 1) and "SQOPT EXIT 50 -- error in the user-supplied functions" once, among the successful exits. [practice · P] [inferred] Correct *detection* of failure is part of what "passing" means.

### 5.4 Public infrastructure around the software

- The UCSD optimizers site keeps a filterable CUTEst problem browser (dimensions, nonzeros, classification strings, links to the SIF files "maintained by Nick Gould"). This is a tool for building size- and type-filtered test sets of the kind used in §1.1. [practice · P]
- Its "Benchmarks" page held a heading and no content when fetched on 2026-09-28. [practice · P]
- Trial versions are offered for SNOPT7 and SQOPT7 only; no SNOPT9 appears (see also 01 §3). [practice · P]

---

## 6. Problem choice, collaboration and organisation (layers 2 and 7)

- **Application groups bring the problem; the optimizer is inserted with minimal change** (Petzold 1998–2000; Gerdts 2018; aerospace funding on every recent SNOPT/DNOPT guide: "Partially supported by Northrop Grumman Aerospace Systems", 7.5 and 7.7 p. 1). [practice · P]
- **Two kinds of team** [inferred from the author lists and the code record in §1.1 and §5.2]: (a) theory-plus-MATLAB-prototype papers with PhD students and postdocs (Robinson, Kungurtsev, Erway, Griffin, Zhang, Runnoe, Brust, Ferry); (b) production software with Murray, Saunders and Wong. The student-era papers carry the student's tools; GR22's analysis stack is Python while the solvers are MATLAB (p. 26).
- **Near-term self-criticism feeds long-term agenda**: the SNOPT limits written down in 2002/2005 (indefinite QP Hessians, more degrees of freedom; quoted in 01 §2.4) are exactly what SQIC (2015), DNOPT/convexification (2015–2020) and the stabilized SQP line address. [practice · P for the sequence; [inferred] for intent]

---

## 7. Failures, abandoned directions and dropped claims (new in this file, or refined from 01)

| Item | Evidence | Tag |
|---|---|---|
| 2011 claim of being "significantly more efficient than our current SQP package SNOPT" not carried into the 2013 journal paper | OO 2011/10 p. 5 vs SIOPT 2013 §6 | practice · P (reason not stated) |
| 2012 arXiv note and 2013 second-order preprint never published under their titles; content apparently absorbed into IMA JNA 2017 | arXiv 1205.2304; OO 2013/10 abstract; CCoM 13-04 abstract | practice + inferred |
| 2018 interior-method preprint had no numerics; retitled and numerics added in 2019 | CCoM-18-1 vs CCoM 19-03 / SIOPT 2020 | practice · P |
| SNOPT's false infeasibilities (17 in 2005 for nZ ≤ 2000; 25 in 2015), iteration-limit and time-limit failures | SIAM Rev. 2005 Table 3; GSW15 Tables 2–3 | practice · P |
| PDB 2020 fails on 3 of 16 COPS problems (glider, robotarm, rocket) with near-singular KKT matrices | journal p. 1091 | practice · P |
| pdSQP 2013 fails on 8 of 158; MP 2017 fails on 1 of 10 MVW problems and on 8 of 86 MPECs | journal pp. 2007; 406 | practice · P |
| Structure-exploiting methods of the 2018 application study lose to SNOPT in most cases | DCDS-S 2018 p. 22 | practice · P |
| f2c C version discontinued (announced 2015, removed 2018) | SNOPT 7.5 p. 1; 7.7 p. 8 | practice · P |
| SNOPT9 announced in 2015, no public release found; website benchmarks page empty | GSW15 p. 26; optimizers site 2026-09-28 | practice + inferred |
| Khachiyan experiments never published as a journal paper | Wright interview line 243 (and the 1980 DTIC report listed in 01) | observed |

No retraction, erratum or correction was found: the Crossref query for errata with Gill as author returned only other people named Gill.

---

## 8. Era and resource context of the practices

| Period | Setting (from the sources) | Practices that depend on it |
|---|---|---|
| 1974–1987, NPL then Stanford SOL | Four near-peers (Gill, Murray, Saunders, Wright); Fortran; shared terminal access to SLAC machines in the early 1970s [observed, Wright interview]; LP test problems at hand | Test-the-hype-yourself (Khachiyan, Karmarkar); library-grade Fortran with user guides (NPSOL's debugging advice) |
| 1992–2005, UCSD + SOL, SNOPT era | Aerospace users (McDonnell Douglas/Boeing); CUTE/CUTEr and COPS become available from other groups; g77 on one Linux PC (2005) | Whole-collection runs of one's own solver without an external baseline; failures named in print; paper "Extensions" become next-version features |
| 2009–2024, UCSD faculty group with PhD students and postdocs | NSF DMS grants, Northrop Grumman, NIH (7.5 guide); MATLAB R2019b–R2022b; single desktops or laptops (8–128 GB); CUTEst with Subversion revisions; IPOPT and L-BFGS-B freely available as baselines | MATLAB prototypes; external baseline once per line of methods, then in-house ablations; supplementary-results and equations reports; interfaces on GitHub maintained by Wong |

Transferability note [inferred]: none of the protocols needs more than one workstation. What they need is a large public test set with metadata (CUTEst), a free competitor, and the discipline of writing everything down. All of these exist today.

---

## 9. Cross-check against the stated methodology in 02 (for Phase 2)

| 02 item (stated) | What the practice shows | Verdict |
|---|---|---|
| E1 test on whole collections | Consistent (table §1.1), with explicit size caps (n ≤ 5000; min(m, n) ≲ 500; KKT order ≤ 2000) and a few named exclusions | consistent, with caps |
| E2 fair comparisons by construction | Consistent in GSW15 (option files, matched tolerance, labelled asymmetric section). But PDB 2020 tunes its parameters on the same 140 problems it then uses against IPOPT at defaults | partly consistent |
| E3 performance profiles, not averages | Consistent from 2015 on; failures get 2× max ratio | consistent |
| E4 conservative success/failure definitions | Consistent within each paper, but the rule for fletcher/lootsma flips between 2005 and 2015 | inconsistent over time |
| J2 small or shared-subset comparisons mislead | Used against Andrei's 38-problem comparison. The group's own prototypes are often judged on HS-scale sets (124 HS + 16 COPS in 2020; 158 in 2013; 10 of 12 MVW problems in 2017) | tension (Contradictions 2) |
| J6 report own failures | Strongly consistent (§2.2, §7) | consistent |
| E6 verify derivatives, distrust too-good results | Built into the software (exit 51/52, Verify level) and into the regression suite (infeasible variants) | consistent, and enforced in code |

---

## 10. Candidate process patterns for the skill (each backed by at least two independent items above; all [inferred])

1. **Freeze and cite the test universe**: a dated or versioned CUTEst snapshot, default dimensions, one written size rule, named exclusions with reasons, hard cases kept (§1.1, §1.6).
2. **One external comparison per method line, made fair on paper; then ablate against your own predecessor** (§1.2, §1.3).
3. **Instrument the algorithm**: report iteration-type shares, modification rates and factorization counts, and use them to explain failures (§1.5, §2.3).
4. **Re-run every failure until you can name its type** (true infeasibility, infeasible stationary point, iteration budget, tolerance), then count it anyway (§2.2).
5. **Let the stratified comparison write the next design** (degrees of freedom → hybrid QP solver; problem class → second derivatives) (§2.3).
6. **Test a local-convergence theorem on problems built to violate its assumptions, including the competitors' own test sets, and report EOC by class** (§1.7).
7. **Publish the evidence separately from the argument**: per-problem results and full-format equations in companion reports that are kept revised (§4.1, §3.6).
8. **Encode debugging knowledge in the solver's messages, ordered by likelihood, and test the failure exits in the regression suite** (§2.1, §5.3).
9. **Change interfaces slowly**: keep old calling sequences, announce removals one release ahead (§5.1).
10. **Drop claims the final experiments do not support** (§3.5).

---

## Contradictions (kept, not reconciled)

1. **Scoring of fletcher and lootsma**: "failures" in SIAM Rev. 2005 (journal p. 122) vs "listed as successful" in GSW15 (p. 10), with no note of the change.
2. **Stated vs practised test-set breadth**: GR22 insists on "every single" problem and warns that shared subsets mislead (pp. 25, 32). The same group's MATLAB prototypes are judged on 124 HS + 16 COPS problems (2020), 158 problems (2013) or 10 hand-coded problems (2017), and PDB's parameters were tuned on the evaluation set (journal p. 1089).
3. **Efficiency claim 2011 vs 2013**: "significantly more efficient than our current SQP package SNOPT" (OO 2011/10 p. 5) vs no efficiency claim and no SNOPT comparison in the SIOPT 2013 paper.
4. **Degrees-of-freedom limit**: "best suited for … (say, up to 2000)" (2005 abstract) and "there is no limit on the number of degrees of freedom" (7.5 guide p. 4), against GSW15's data that SNOPT is faster on only 24 of the 68 problems with ndf > 4000 (p. 13). "No limit" is a capacity statement, not an efficiency statement; both are kept.
5. **Pointer to the PDB per-problem tables**: SIOPT 2020 cites [20] = CCoM 19-04 (equations note, no results tables); the tables are in CCoM 19-03.
6. **Report number CCoM 18-1** is used both for "A Shifted Primal-Dual Interior Method for Nonlinear Optimization" (February 2018 preprint, p. 1) and for the SNOPT 7.7 User's Guide (downloads page BibTeX, "NUMBER = {CCoM 18-1}").
7. **Projected-search paper identifiers**: arXiv 2110.08359 says "CCoM 21-01" and "Projected-Search Methods for Bound-Constrained Optimization"; the homepage says CCoM 20-07 and "A Class of Projected-Search Methods …"; the journal uses the latter title.
8. **Fate of the 2013 second-order preprint**: 01 §3 lists it as a gap; this file infers absorption into IMA JNA 2017 from matching abstracts. That is an inference, not a documented statement by the authors.
9. **Who did the Khachiyan tests**: Wright says "we and other groups I'm not positive who did this" (transcript line 241). She says there was no paper, while 01 lists a 1980 DTIC report by the four authors.
10. **DNOPT's self-description**: its guide's abstract speaks of efficiency "On large problems" (p. 1); the website says "Intended for small- to medium- scale problems".

## Gaps (searched or looked for, not found or not accessible)

- **Referee reports, rebuttals, rejected submissions**: none public. The venues (SIAM, Springer, OUP, T&F) do not publish reviews. The only trace is acknowledgments ("three referees", SIOPT 2020). No OpenReview presence.
- **Gill's own code and coding habits**: the SNOPT/SQOPT/NPSOL/DNOPT sources are licensed; public repositories contain interfaces only, all committed by Wong and others. The MATLAB prototypes of the 2009–2024 papers were not found online. BG23 says its software "is available in the public domain" (p. 11), but no location was found.
- **Core-solver changelogs**: none public beyond the two-bullet "What's New" in the 7.7 guide. SNOPT 6.1 guide checked only for the interface history; 7.4 and 7.6 guides not read.
- **Why claims were dropped or titles changed** (2011 → 2013; 2018 → 2019; 2015 v1 → v2): not stated anywhere read. The v1/v2 numbers of arXiv 1503.08349 and the 2022/2023 revisions of CCoM 22-04 were not diffed.
- **1970s–1980s process**: the numerical sections of the Math. Prog. 1986 Karmarkar-equivalence paper, the DTIC ellipsoid report, the NPL reports and the TOMS 1979 library-design paper were not read (paywalled or not located as text). *Practical Optimization* chapter 8 (the long form of the debugging advice) not read.
- **User-support behaviour**: the SNOPT Google Groups forum linked from the optimizers site was not examined (Google Groups pages are script-rendered); GitHub issues could not be listed with the tools available in this session.
- **Student theses** (Wong 2011, Kungurtsev, Zhang, Runnoe, Ferry): not read here; left to agent 04. They would show how prototypes become Fortran code.
- **SNOPT9 status**: no release, preprint or talk found as of 2026-09-28.
- **Gill's 2011 Manchester slides** were read by agent 01 and are cited there; not re-read for process content here.

## Sources

1. P. E. Gill, W. Murray, M. A. Saunders, "SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization", SIAM J. Optim. 12 (2002) 979–1006, DOI 10.1137/S1052623499350013; PDF https://www.ccom.ucsd.edu/~peg/papers/snpaper.pdf — primary (§6–8 read)
2. P. E. Gill, W. Murray, M. A. Saunders, same title, SIAM Review 47 (2005) 99–131, DOI 10.1137/S0036144504446096; PDF https://web.stanford.edu/group/SOL/papers/SNOPT-SIGEST.pdf — primary (§2.8, §4, §7–9 read)
3. P. E. Gill, W. Murray, M. A. Saunders, "User's Guide for SNOPT 5.3", Report NA 97-5, UCSD, draft October 1997, https://www.ccom.ucsd.edu/~peg/papers/sndoc5.pdf — primary (inform codes, exit advice read)
4. P. E. Gill, W. Murray, M. A. Saunders, "User's Guide for SNOPT 6.1", Report NA 02-2, UCSD, 2002, https://www.ccom.ucsd.edu/~peg/papers/sndoc6.pdf — primary (interface-history lines only)
5. P. E. Gill, W. Murray, M. A. Saunders, E. Wong, "User's Guide for SNOPT Version 7.5", December 2015, https://www.ccom.ucsd.edu/~peg/papers/sndoc7.pdf — primary (front matter, §1, §4, §8 read)
6. P. E. Gill, W. Murray, M. A. Saunders, E. Wong, "User's Guide for SNOPT Version 7.7", CCoM 18-1, March 2018, https://ccom.ucsd.edu/~optimizers/static/pdfs/snopt7-7.pdf — primary (front matter, §1.8 read)
7. P. E. Gill, W. Murray, M. A. Saunders, M. H. Wright, "User's Guide for NPSOL 5.0", Technical Report SOL 86-6, revised June 4, 2001, https://www.ccom.ucsd.edu/~peg/papers/npdoc.pdf — primary (§8–10 read)
8. P. E. Gill, E. Wong, M. A. Saunders, "User's Guide for DNOPT Version 4", August 2020, https://ccom.ucsd.edu/~optimizers/static/pdfs/dndoc.pdf — primary (abstract, contents, §5 read)
9. P. E. Gill, E. Wong, "Numerical results for SQIC: Software for large-scale quadratic programming" (supplementary material), July 13, 2014, https://www.ccom.ucsd.edu/~peg/papers/sqic-results.pdf — primary (read)
10. P. E. Gill, E. Wong, "Methods for convex and general quadratic programming", Math. Prog. Comp. 7 (2015) 71–112, DOI 10.1007/s12532-014-0075-x; PDF https://www.ccom.ucsd.edu/~peg/papers/gqp.pdf — primary (§7 read)
11. A. Forsgren, P. E. Gill, E. Wong, "Active-Set Methods for Convex Quadratic Programming", CCoM-15-02, March 28, 2015, https://optimization-online.org/wp-content/uploads/2015/03/4848.pdf, and revised report https://www.ccom.ucsd.edu/~peg/papers/ucsd-ccom-15-02.pdf; published as "Primal and dual active-set methods for convex quadratic programming", Math. Prog. 159 (2016) 469–508, DOI 10.1007/s10107-015-0966-2; arXiv 1503.08349 (v1 2015-03-28, v2 2015-12-30) — primary (§7 of the revised report read; v1 front page read)
12. P. E. Gill, M. A. Saunders, E. Wong, "On the Performance of SQP Methods for Nonlinear Optimization", in Modeling and Optimization: Theory and Applications, Springer PROMS 147 (2015) 95–123, DOI 10.1007/978-3-319-23699-5_5; preprint https://www.ccom.ucsd.edu/~peg/papers/mopta.pdf — primary (§3–5 read)
13. P. E. Gill, D. P. Robinson, "Regularized Sequential Quadratic Programming", UCSD NA-11-02, Optimization Online 2011/10/3222, https://optimization-online.org/2011/10/3222/ — primary (introduction and structure read)
14. P. E. Gill, D. P. Robinson, "A Globally Convergent Stabilized SQP Method", SIAM J. Optim. 23 (2013) 1983–2010, DOI 10.1137/120882913; PDFs https://ccom.ucsd.edu/~peg/papers/siam_88291.pdf (journal) and https://www.ccom.ucsd.edu/~peg/papers/pdsqp.pdf (report, July 6, 2013) — primary (§6 read)
15. P. Gill, V. Kungurtsev, D. Robinson, "Negative Curvature and Second-order optimality for regularized SQP", arXiv 1205.2304 v1 (2012-05-10) — primary (p. 1 and version record read)
16. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Regularized SQP Method with Convergence to Second-Order Optimal Points", Optimization Online 2013/10/4102, https://optimization-online.org/2013/10/4102/ — primary (abstract read)
17. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A stabilized SQP method: global convergence", IMA J. Numer. Anal. 37 (2017) 407–443, DOI 10.1093/imanum/drw004; report CCoM 13-04 (June 2013, revised April 2024), https://www.ccom.ucsd.edu/~peg/papers/pdsqpglobalReport.pdf — primary (abstract and §2 excerpt read)
18. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A stabilized SQP method: superlinear convergence", Math. Prog. 163 (2017) 369–410, DOI 10.1007/s10107-016-1066-7; PDF https://www.ccom.ucsd.edu/~peg/papers/pdSQPlocal.pdf; report CCoM 14-01 (revised April 2024) — primary (§4–5 read)
19. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Shifted Primal-Dual Interior Method for Nonlinear Optimization", CCoM-18-1, February 1, 2018, https://optimization-online.org/2018/01/6444/ — primary (structure and §4 read)
20. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", CCoM 19-03, March 1, 2019, https://www.ccom.ucsd.edu/~peg/papers/pdbReport.pdf — primary (§6 and tables read)
21. P. E. Gill, V. Kungurtsev, D. P. Robinson, "Note on the Formulation of a Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", CCoM 19-04, March 1, 2019, https://www.ccom.ucsd.edu/~peg/papers/pdbFormats.pdf — primary (introduction and structure read)
22. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", SIAM J. Optim. 30 (2020) 1067–1093, DOI 10.1137/19M1247425; PDF https://www.ccom.ucsd.edu/~peg/papers/pdb.pdf — primary (§6–7 read)
23. P. E. Gill, M. Zhang, "A Projected-Search Interior Method for Nonlinear Optimization", CCoM 22-01, June 2022, https://www.CCoM.ucsd.edu/~peg/papers/pdprojReport.pdf, and "A projected-search interior-point method for nonlinearly constrained optimization", Comput. Optim. Appl. 88 (2024) 37–70, DOI 10.1007/s10589-023-00549-1, PDF https://www.CCoM.ucsd.edu/~peg/papers/pdproj.pdf — primary (§2 excerpt and §6 read)
24. P. E. Gill, M. Zhang, "Numerical Results for a Projected-Search Interior-Point Method", CCoM 22-03, June 2022, revised September 2023, https://www.CCoM.ucsd.edu/~peg/papers/pdproj-results.pdf — primary (pp. 1–9 read, tables skimmed)
25. M. W. Ferry, P. E. Gill, E. Wong, M. Zhang, "A class of projected-search methods for bound-constrained optimization", Optim. Methods Softw. 39 (2024) 459–488 (online 2023), DOI 10.1080/10556788.2023.2241769; preprint https://www.CCoM.ucsd.edu/~peg/papers/quasiwolfe.pdf; arXiv 2110.08359 — primary (numerical section read)
26. M. W. Ferry, P. E. Gill, E. Wong, M. Zhang, "Supplementary Numerical Results for Projected-Search Methods for Bound-Constrained Optimization", CCoM 20-08, August 10, 2020, https://www.CCoM.ucsd.edu/~peg/papers/quasi-results.pdf — primary (read)
27. P. E. Gill, J. H. Runnoe, "On Recent Developments in BFGS Methods for Unconstrained Optimization", CCoM 22-04, July 1, 2022, revised October 17, 2023, https://www.CCoM.ucsd.edu/~peg/papers/bfgsdev.pdf — primary (§5–6 read)
28. J. J. Brust, P. E. Gill, "An LDL^T Trust-Region Quasi-Newton Method", SIAM J. Sci. Comput. 46 (2024) A3330–A3351, DOI 10.1137/23M1623380; arXiv 2312.06884; preprint https://www.CCoM.ucsd.edu/~peg/papers/trustRegionQN.pdf — primary (§4 end and §5 read)
29. J. B. Erway, P. E. Gill, J. D. Griffin, "Iterative Methods for Finding a Trust-region Step", SIAM J. Optim. 20 (2009) 1110–1131, DOI 10.1137/070708494; PDF https://www.ccom.ucsd.edu/~peg/papers/siam_70849.pdf — primary (§4 read)
30. P. E. Gill, L. O. Jay, M. W. Leonard, L. R. Petzold, V. Sharma, "An SQP method for the optimal control of large-scale dynamical systems", Report NA 98-1 (https://www.ccom.ucsd.edu/~peg/papers/modjac.pdf); J. Comput. Appl. Math. 120 (2000) 197–213, DOI 10.1016/S0377-0427(00)00310-1 — primary (report read)
31. J.-H. Webert, P. E. Gill, S.-J. Kimmerle, M. Gerdts, "A study of structure-exploiting SQP algorithms for an optimal control problem with coupled hyperbolic and ordinary differential equation constraints", DCDS-S 11 (2018) 1259–1282, DOI 10.3934/dcdss.2018071; PDF https://www.ccom.ucsd.edu/~peg/papers/truckSQP.pdf — primary (introduction and §5 end read)
32. GitHub organisation `snopt`: repositories snopt-matlab, snopt-interface, snopt-python, snopt7-examples, SNOPT7.jl, snctrl (git histories, trees, READMEs, `fortran/check`, `fortran/check.log0`, `fortran/hs47ModInfa.f`), cloned 2026-09-28, https://github.com/snopt — primary (practice)
33. UCSD Optimization Software website (home, downloads, solvers/snopt, solvers/dnopt, solvers/sqic, benchmarks, cutest/problems), fetched 2026-09-28, https://ccom.ucsd.edu/~optimizers/ — primary
34. P. E. Gill, homepage lists "Selected published and accepted papers" and "Selected Technical Reports", fetched 2026-09-28, https://ccom.ucsd.edu/~peg/ — primary
35. INFORMS, "INFORMS History & Traditions Interview with Margaret Wright", YouTube, 2019-11-18, https://www.youtube.com/watch?v=2L5nQIvTohk; auto-caption transcript at `references/sources/talks/2019-informs-margaret-wright-interview-autocaptions.txt` (saved by agent 01) — primary for Wright's account, [observed] for Gill; wording approximate
36. arXiv abstract pages and version histories for 1503.08349, 2110.08359, 2312.06884, 1205.2304, cs/0106051, fetched 2026-09-28, https://arxiv.org/abs/ — primary bibliographic
37. P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, M. H. Wright, "On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method", Math. Prog. 36 (1986) 183–209, DOI 10.1007/BF02592025 — primary (metadata verified; not read)
38. P. E. Gill, D. P. Robinson, "A primal-dual augmented Lagrangian", Comput. Optim. Appl. 51 (2012; online 2010) 1–25, DOI 10.1007/s10589-010-9339-1 — primary (metadata verified; cited only as the source of the "preliminary numerical results" referred to in source 13; not read)
39. N. Andrei, "An adaptive scaled BFGS method for unconstrained optimization", Numer. Algorithms 77 (2018) 413–432, DOI 10.1007/s11075-017-0321-1 — secondary for this file (the method Gill & Runnoe re-tested; metadata verified; not read)
40. E.-S. Mostafa, L. N. Vicente, S. J. Wright, "Numerical Behavior of a Stabilized SQP Method for Degenerate NLP Problems", LNCS 2861 (2003) 123–141, DOI 10.1007/978-3-540-39901-8_10 — secondary for this file (source of a reused test set; metadata verified; not read)
41. Crossref REST API (DOI metadata for all DOIs above; errata query for author "Philip E. Gill"), queried 2026-09-28, https://api.crossref.org/works — bibliographic aggregator (secondary)
