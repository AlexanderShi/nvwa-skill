# 03 · Process evidence: what Yinyu Ye and his group actually DO

> **Researcher:** Yinyu Ye (叶荫宇), K. T. Li Professor of Engineering (Emeritus), Stanford MS&E / ICME. Recent papers also list SJTU Antai College (arXiv 2511.00680v3, July 2026).
> **Dimension:** research agent 03 of 06, process evidence. This note covers behaviour: code, experiment sections, version histories, errata and dropped claims. What he *says* is in `02-methodology.md`. This note checks those claims against practice and cites them by their 02 labels (R1–R11, C1–C7).
> **Research date:** 2026-09-28.
> **Sources consulted:** 47 (list at the end): 5 public code repositories cloned and read (full git histories), 6 of Ye's own code or manual files from his homepage, 14 arXiv full texts across 9 papers (early and final versions compared), 16 arXiv abstract or version-history pages, 1 talk deck, 2 errata lists, and Crossref, ML Anthology and MOSEK-documentation records. **No user-supplied material existed**: `references/sources/{papers,talks,essays,software}` held only `.gitkeep`. `private/` was not opened. WebSearch calls used: 1 of 2. No transcripts were saved to `sources/talks/`.
> **Tags:** [practice] means he or his group did it, as shown by code, paper text, tables or version history. [stated] means the text says it; co-authored paper text counts as the group's voice and is not necessarily Ye's own. [observed] means a third party reports it. [inferred] means my reading. Every item is marked primary (P) or secondary (S).
> **Main limit on this evidence:** Ye has **no commit under his name** in any of the five repositories (§4.1). For 2017–2026 every piece of code evidence is his group's practice, usually a PhD student's or postdoc's, under his senior authorship. Only the 1989 SOLNP and 1993 HSD Matlab codes on his homepage show his own hands-on coding. I keep the two apart throughout.
> **Text extraction:** quotes come from PDF text that I extracted myself. Where the extraction dropped the fi/ff ligatures, I restored them. Where it dropped mathematical symbols, I paraphrase instead of quoting.

---

## 0. Summary: recurring behaviours (each seen in 3 or more independent artefacts)

| # | Behaviour (practice) | Where it shows | Era |
|---|---|---|---|
| B1 | **Classical outer framework, own subproblem engine.** The group takes an accepted globalisation (augmented Lagrangian, trust region, dual scaling, PDHG) and replaces the inner step with an interior-point, homogeneous, eigenvalue or low-dimensional computation. | SOLNP 1989 (Robinson's augmented Lagrangian + interior LP/QP inner solver); HSD LP code 1993; DRSOM 2022 (TR in a 2-D subspace); HSODM 2022 (TR step as a leftmost eigenvector); HDSDP 2022 (DSDP + embedding); ABIP 2018/2022 (IPM with ADMM inner solves) | 1989–2026 |
| B2 | **Homogenise or embed so that infeasibility needs no special phase.** | HSD code 1993 (τ/κ infeasibility test); one-phase IPM for NLP 2018; HDSDP 2022 (embedding replaces big-M); HSODM 2022 ("homogenized quadratic model"); 2015 teaching note (LP to homogeneous feasibility over a simplex) | 1993–2026 |
| B3 | **Revive their own legacy code and benchmark against it.** | SOLNP (1989) → SOLNP+ (2022, compared with "the last version by MATLAB"); DSDP5.8 → HDSDP (DSDP5.8 is a baseline); cuPDLP.jl → cuPDLP-C (Julia version re-run as a baseline); HSD Matlab code kept alive from 1993 to 2021 | 1989→2026 |
| B4 | **Reuse the group's own problem classes as testbeds for decades.** Sensor-network localisation (SNL) and L2–Lp minimisation appear in paper after paper. | SNL: 2004/2006 SDP papers → DRSOM 2022 (v1 and v3) → HDSDP instances "sensor 500b/1000b" → Riemannian DRSOM 2024. L2–Lp: DRSOM v1/v3, HSODM v1 ("one of our greatest interests") | 2004–2024 |
| B5 | **Benchmarks: a public test set, same-language open baselines at default settings, scaled geometric means, failures charged at the limit.** | DRSOM v3, HSODM v7, HSODF v5, UTR v4 (CUTEst, Julia baselines, SGM with shifts of 1 s and 50 iterations, a failure counted as 20,000); cuPDLP-C (MIPLIB 2017 relaxations + Mittelmann, SGM10); HDSDP (Mittelmann + SDPLIB, DIMACS errors, failure counted as 40,000 s); OnePhase (CUTEst vs IPOPT, Dolan–Moré profiles) | 2018–2026 |
| B6 | **Report where the baseline wins, in the same paper.** | DRSOM v1 Table 1 (SAGA beats DRSOM); DRSOM v3 (CG solves the most instances, LBFGS needs the fewest iterations); HSODM v7 (TR-STCG best on gradient evaluations); OnePhase (IPOPT faster, and fewer iterations when both succeed); cuPDLP-C (COPT 2–4× faster on the standard sets); HDSDP (COPT solves 72 vs 67); ATR (the extreme-acceleration variant loses local quadratic convergence) | 2018–2026 |
| B7 | **Release early and revise heavily.** arXiv v1 soon after the code, then many versions over years; claims are narrowed, dropped or split off into new papers. | DRSOM (3 versions; neural-network claims dropped); HSODM (7 versions, 2022→2026); UTR (4 versions, retitled, "can be accelerated" dropped and later split into ATR); smart crossover (7 versions); Hinder–Ye barrier bounds (5 versions; results cut at reviewers' request) | 2018–2026 |

---

## 1. Research taste in practice: what gets built, kept and highlighted

**1.1 He keeps his own early solvers in circulation for decades.** [practice] (P)
- The homepage still serves `matlab/hsdLPsolver.m`, labelled "updaded 11/9/04" on matlab.html. The code comments date the core to Iowa: "6) cleaned on 11/16/93". Its references are Ye–Todd–Mizuno ("to appear in Math. of OR") and Xu–Hung–Ye 1993 ("manuscript, Department of Management Sciences, The University of Iowa").
- The 5th-edition textbook page (LY5thmatlab.html) serves `HSDLPsolver.m` "updaded 11/7/21". A `diff` shows that **the numerical core is unchanged since 1993.** Only three things changed: the documentation moved to a header, a semicolon was added to `iter = iter + 1` (which had printed the iteration counter on every pass), and the header now reads "Complete Implementation of the Homogenerous and Self-Dual Primal-Dual Potential-Reduction Algorithm for LP" (typo verbatim). `solnp.m` is byte-identical between the matlab/ folder (page dated 2004; manual dated 1989) and the 2021 LY5thmatlab/ folder.
- Era and resources: sole author or two Iowa students; Matlab, probably on a NeXT [inferred: the SOLNP manual's PostScript header reads "Display NeXT manual.dvi"]. The NETLIB LPs afiro, adlittle and agg ship as `.mat` sample files.
- [inferred] For teaching and demos he prefers a short, readable, stable reference code to a tuned one. The 2021 book still ships 1993 numerics.

**1.2 The results he builds on further are those that work as software.** [practice] (P)
- DSDP (Benson–Ye–Zhang, SIOPT 2000, 10.1137/S1052623497328008) reported "the first computational results of interior-point algorithms for approximating maximum cut semidefinite programs with dimension up to 3,000" (Crossref abstract). Twenty-two years later HDSDP (arXiv 2207.13862; ACM TOMS 2025, 10.1145/3721123) "is developed in parallel to DSDP5.8" and "works as one of the candidate SDP methods in the state-of-the-art commercial solver COPT".
- The cuPDLP-C README opens with "cuPDLP is now available in [COPT 7.1]". The repository's first commit is 2023-12-12; the COPT 7.1 release date was not checked.
- SOLNP+ README: "This is C implementation of SOLNP algorithm, which is proposed by Yinyu Ye (1989) and originally implemented in Matlab. Various improvements have been made to increase the robustness and reduce number of function evaluations compared with the original version."
- Era: from 2019 the group sits inside the COPT / Cardinal Operations and SUFE ecosystem. The repositories are under the `COPT-Public` GitHub organisation.
- [observed] (S) MOSEK's current manual says of its LP interior-point optimizer: "This is the reason why MOSEK solves the so-called homogeneous model (13.2)". This is independent evidence that the HSD idea lives in commercial code. It is not a check of his claim about "all" commercial solvers (see 02, S1).

**1.3 A new method goes into an existing solver as an option, not a replacement.** [practice] (P)
- SOLNP+ (C, 2022–) has a `drsom` setting. `solnp_util.c` defaults it to `stgs->drsom = 0`, and `subnp_qp.c` comments "Use DRSOM update". A commit on 2023-06-24 reads "fix a bug of drsom". The group's 2022 method was wired into the revived 1989 solver, switched off by default.

---

## 2. Problem choice in practice

**2.1 Revisit his own old problem classes and algorithms with new tools (B3, B4).** [practice] (P)
- SNL. The 2006 ACM TOSN paper (Biswas, Lian, Wang, Ye; 10.1145/1149283.1149286) says in its abstract: "The SDP solution can then also be used as a starting point for steepest descent based local optimization techniques that can further refine the SDP solution." The same two-stage design is DRSOM's 2022 testbed. `DRSOM.jl/test_snl/src/snl.jl` is described as "Module for modeling Sensor Network Localization problem using SDP relaxation and DRSOM to minimize the second-stage nonlinear least-square problem" and loads `MosekTools` for the SDR stage. DRSOM v3 §4.2 runs SNL "with SDR initialization" and without it.
- L2–Lp. HSODM v1 §5 (arXiv 2211.08212v1): "First, we include a set of nonconvex L2−Lp minimization problems that arise from compressed sensing. This problem has long been one of our greatest interests." The class goes back to Ge–Jiang–Ye 2011 (MP, 10.1007/s10107-011-0470-2) and Chen et al., arXiv 1105.0638.
- Potential reduction. A 2015 teaching note, "On a First-Order Potential Reduction Algorithm for Linear Programming" (homepage PDF, dated July 30, 2015; footnote: "This was a teaching note for course MS&E310, Linear Optimization"), recasts LP as the homogeneous feasibility problem "(Ye et al. [5])" over a simplex and applies a steepest-descent potential reduction. His 1990s tools (HSD, potential function, analytic centre as the start) are here recombined with a first-order method, eight years before the group's GPU first-order LP work (cuPDLP-C 2023). [inferred: the note is an early step towards that work; no text links the two.]
- The 2024 paper "When Does Primal Interior Point Method Beat Primal-dual in Linear Optimization?" (arXiv 2411.16015; Gao, Liu, Ye, Udell) reopens a settled consensus. Its abstract opens: "The primal-dual interior point method (IPM) is widely regarded as the most efficient IPM variant for linear optimization."

**2.2 Ideas start as course notes on the homepage and are not always published.** [practice] (P)
- "A Second-Order Path-Following Algorithm for Unconstrained Convex Optimization" (sole author, May 31, 2017). Its abstract: "We present more details of the minimal-norm path following algorithm for unconstrained smooth convex optimization described in the lecture note of CME307 and MS&E311 [10]."
- The 2015 potential-reduction note (§2.1).
- Crossref lists neither note as a journal article (queries of 2026-09-28). Both are 5–6 pages and sole-authored, and both are linked from `newpapers.html` next to journal papers.
- [inferred] Sole-authored teaching notes are where he keeps an idea when a student project does not take it up. The regularisation-path idea of 2017 resembles the "homotopy HSODM" of HSODF (arXiv 2306.17516). No text states a link.

**2.3 The platform follows the hardware and the product.** [practice] (P)
- Matlab (1989–2004), PC-DOS executables and Fortran/C (the 1997 COPL codes), C for DSDP, Julia on a Mac desktop (2018–2025: OnePhase, DRSOM.jl; both papers name "a desktop of Mac OS with a 3.2 GHz 6-Core Intel Core i7 processor"), then CUDA on an NVIDIA H100 (cuPDLP-C 2023). This matches his stated GPU agenda of 2017 (02 §2.3).
- DRSOM.jl commit of 2022-08-14: "change dependencies, remove mosek, matlab, sedumix". Commercial and Matlab dependencies were removed two weeks after the first release.

---

## 3. Idea generation in practice

**3.1 One move, repeated over 33 years: interior or homogeneous machinery inside a classical frame (B1, B2).** [practice] (P)
- 1989, SOLNP User's Guide (Iowa, August 1989): "The kth major iteration of SOLNP solves a linearly constrained optimization problem with an augmented Lagrangian objective function (Robinson [1])". The linearised equalities are first checked for feasibility, and "If it is not, an interior linear programming (LP) Phase 1 procedure is called to find an interior feasible (or near-feasible) solution." For the QP: "Since there is no need to obtain highly accurate solution of (2), we use the interior QP algorithm to reach an approximate solution, which usually takes few steps." The references are Robinson 1972, MINOS 5.1 and his own 1987 thesis.
- In `subnp.m` the Levenberg-type regularisation is scaled by inverse distances to the bounds (`dx(1:mm,1)=ones(mm,1)./gap`), an affine-scaling device. The regulariser is multiplied by 3 until the step stays inside the bounds (`l=3*l`).
- 1993, the HSD LP code: infeasibility is declared from the τ/κ ratio (`if (tau*kappa0/(tau0*kappa) < toler) & (mu/mu0 < toler/n)`), and there is no Phase I or big-M. The doc block: "The result is a strict complementarity solution, i.e., a solution in the relative interior of the LP optimal face."
- 2018, one-phase IPM for NLP (Hinder & Ye, arXiv 1801.03072). Its abstract names the obstacle it attacks: "The work of Wachter and Biegler suggests that infeasible-start interior point methods (IPMs) developed for linear programming cannot be adapted to nonlinear optimization without significant modification, i.e., using a two-phase or penalty method." Its answer: "we reduce primal feasibility at the same rate as the barrier parameter". The companion paper (Haeser, Hinder, Ye; MP 2019, 10.1007/s10107-019-01454-4) supplies the theory and names the competitor: "we show that IPOPT, an algorithm that does not carefully control primal feasibility has practical issues with the dual multipliers values growing to unnecessarily large values."
- 2022, HDSDP: "HDSDP aims to show how dual-scaling algorithm benefits from the self-dual embedding". The embedding "needs no big-M initialization" (§4).
- 2022, HSODM: "By finding the leftmost eigenvector of a gradient-Hessian integrated matrix at each iteration" (v1 abstract), i.e. the homogenised model is solved as an eigenproblem.
- Era: the move survives every change of team (Iowa students Xu and Hung; Stanford students Benson, Biswas and Hinder; the SUFE/COPT team from 2019).

**3.2 Variants are grown in the codebase before they become papers.** [practice] (P; student-written code)
- DRSOM.jl commit history (156 commits, 2022-07-31 → 2026-06-18). The header of `test/cutest-benchmark/test_cutest_batch.jl` reads "project=> RSOM / created Date=> Tu Mar 2022". The legacy SNL script names outputs `rsom_snl_…`, so the method was called RSOM about four months before the DRSOM arXiv v1 (2022-07-30).
- After v1: "add 3 direction version" (08-03), "a multi-direction mode" (08-13), "add BFGS DRSOM" (08-18), "update Quasi-Newton (Hessian-Learning) mode" (08-16).
- "add homogeneous Krylov directions" (2022-10-17), then "add HSDOM and tests" (2022-11-15), the day HSODM arXiv v1 appeared.
- "add pathfollowing hsdom" (2023-04-25), then HSODF arXiv v1 (2023-06-30).
- "add a new Universal Trust-Region Method" (2023-08-02), then UTR arXiv v1 (2023-11-20).
- "atr v1" (2025-01-03), then ATR arXiv v1 (2025-11-01).
- [inferred] One shared codebase is the group's research notebook, and each paper is a branch of it. The lag from the first related commit to arXiv v1 was about 4 months for RSOM→DRSOM, 1 month for HSODM (the "add HSDOM and tests" commit is dated the day of v1), 3.5 months for UTR and 10 months for ATR.

**3.3 Tools come from the Julia ecosystem, not from scratch.** [practice] (P)
- HSODM v7 §6.1: "we directly use the line-search algorithms from LineSearches.jl [26], and the Lanczos method from KrylovKit.jl [21]." DRSOM v1 §4: baselines "computed via a third-party package Optim.jl". HSODF (arXiv 2306.17516v5 §5): "Most of the subroutines can be found in standard Julia packages". Only the new methods and one competitor are written in-house: "two methods in this paper, Adaptive-HSODM (Algorithm 2), Homotopy-HSODM (Algorithm 4), and the inexact Newton method (iNewton-Grad) are implemented by ourselves."

---

## 4. Experiments and execution

**4.1 Who writes the code.** [practice] (P)
- `git log` author counts: DRSOM.jl: C. Zhang / cz / C Zhang / brentian / Brent Zhang / chuwen (together 145 of 156), "Your Name" (an unconfigured git identity) 10, COPT-Public 1. OnePhase: ohinder, Oliver Hinder, Fadi Hamad (and aliases). cuPDLP-C: Hannes Uppman 27 (external), cz 24, SkyLiu0 18, JinsongLiu6 10, and others. HDSDP: Wenzhi Gao / Gwzwpxz. SOLNP_plus: Tank (Jiyuan Tan), JinsongLiu6, and others. **No commit is by Ye.**
- The DRSOM.jl README nonetheless lists "Developer - Chuwen Zhang … - Yinyu Ye".
- [inferred] From about 2000 his role in software is design, problem choice and senior authorship. Implementation, debugging and benchmarking are the students'. The 1989/1993 Matlab codes are the last code evidence that is clearly his own.

**4.2 Test-set selection is stated, and it is shaped by what the algorithm needs.** [practice] (P)
- OnePhase (2018): "We selected a subset from CUTEst with more than 100 variables and 100 constraints, but the total number of variables and constraints less than 10,000. We further restricted the CUTEst problems to ones that are classified as having first and second derivatives defined everywhere (and available analytically). This gave us a test set with 238 problems."
- **Infeasible test sets are built on purpose.** OnePhase §5.2 shifts CUTEst constraints to make "a test set that was more likely to contain infeasible problems". It also uses the NETLIB infeasible LPs and removes CPLEX2, "an almost feasible problem that was declared feasible by both solvers". The OnePhase `to_do.md` lists "*- create infeasible test set*" and "*- run full netlib test*".
- SOLNP+ (2022) keeps only the Hock–Schittkowski problems whose initial point is interior to the box, because the solver requires one: 74 problems. It also excludes hs54, hs70 and hs85 because "the initial and optimal values … are inconsistent with the information provided by Hock and Schittkowski". The detailed table's problems "are chosen arbitrarily from the 74 problems."
- Unconstrained CUTEst subsets **change from paper to paper** within one codebase:
  - DRSOM v3: from each parametrised problem "choose the first one that has n [≤] 200 variables" (the sign is lost in extraction; the repository filter is `4 <= nlp.meta.nvar <= 200`).
  - HSODM v7: "n ∈ [4, 5000]", "all instances that fit the criterion", 200 instances.
  - HSODF v5: 500 ≤ n ≤ 5000, 81 instances.
  - UTR v4: "dimension n ≤ 5000".
  - `problem_cols.jl` holds a hand-curated list `UNC_PROBLEMS_GOOD` of 176 instances, commented only "# I select a set of unconstrained problems" (2022/11/04). No criterion is written down.
- cuPDLP-C: "We select 383 instances based on the same criteria in [10]", i.e. those of the cuPDLP.jl paper, and solve their LP relaxations. Separately, large instances were added "To highlight the advantages of cuPDLP-C over COPT on extremely large instances" (§3.3).

**4.3 Baselines: the predecessor, the reigning champion, and open same-language codes at default settings.** [practice] (P)
- HDSDP compares HDSDP, DSDP5.8 (the predecessor) and "COPT 6.5 (fastest solver on Mittelmann's benchmark)".
- SOLNP+ compares with COBYLA (through PDFO) and NOMAD 3.9.1, and with "the last version by MATLAB" (abstract).
- OnePhase compares with IPOPT with default MUMPS, which "has been in development for over 15 years".
- The second-order line uses JSO Julia codes (Orban & Siqueira; Dussault) at default settings. HSODM v7: "We use the original implementation in [36] and the default settings therein." UTR v4: "Since both the classical trust-region method (Newton-TR-STCG) and adaptive cubic regularized method (ARC) are well studied, we directly use the implementation in Dussault [36]."
- **The baselines were upgraded during revision.** HSODM v1 (Nov 2022) compared with LBFGS and Newton-TR from Optim.jl and with the group's own DRSOM and DRSOM-H. HSODM v7 compares with Newton-TR-STCG and ARC from JSO, and the L2–Lp section and the DRSOM comparisons are gone. The code shows the same drift: "add TRST (Steihaug-Toint CG)" (2023-08-30), "add Mishchenko's strategy" (2023-09-01).
- A single GALAHAD comparison exists (`test_galahad/test.jl`: GALAHAD ARC on BDQRTIC, N=100). No paper reports GALAHAD, KNITRO or IPOPT for the unconstrained line. [inferred: the second-order line was never benchmarked against Fortran production codes.]
- **Baseline runs are reused across papers.** The ARC row (K=167, t_G=5.32, k_G=185.03, k^f_G=185.03, k^g_G=888.35) and the Newton-TR-STCG row (K=165, 6.14, 170.44, 170.44, 639.64) are identical in HSODM v7 Table 6.1 and UTR v4 Table 3.

**4.4 Protocol details, and fairness adjustments made in revision.** [practice] (P)
- Metrics are scaled geometric means with failures charged at the cap. DRSOM v3: "If an instance is the failed, its iteration number and solving time are set to 20, 000" (verbatim). Shifts are 1 s and 50 iterations. DRSOM v3 counts an instance solved if min{‖g_k‖, ‖g_k‖/‖g_0‖} ≤ 1e−5, where the minimum "accounts for the case where the gradient is too large". The repository's current batch script instead switches to the relative test only when ‖g₀‖ > 1e15 (`this_tol = g₀ > 1e15 ? tol_grad * g₀ : tol_grad`). The script was edited after v3 (commits of 2023-08-24 and 2024-05-12), so the code used for the paper may have differed. [not resolved]
- HDSDP: tolerance 5×10⁻⁶, "the broadly accepted DIMACs error", a failure counted as 40,000 s. On threads: "We set the number of MKL threads to be 12 for DSDP5.8; the Threads parameter of COPT is also set to 12. To enhance reproducibility HDSDP uses 8 threads."
- cuPDLP-C v1 (2023-12-22) → v2 (2024-01-07), "fix typos, update numerical results". v2 adds "For fair comparisons, we exclude the running time needed for different presolving and scaling techniques." The repository shows the timing split was coded before the paper was revised: "add Presolve timing" (2023-12-14), "add presolve/scaling time" (2023-12-16). The same week: "use deterministic SpMV algs" (2023-12-14, three commits).
- Cross-hardware comparison is openly declared: "We run COPT on AMD Ryzen 9 5900X with 512GB RAM, whereas the GPU-based cuPDLP-C is tested on NVIDIA H100 80GB."
- OnePhase measures iterations because the Julia code is slower: "However, IPOPT is generally significantly faster than our algorithm. … For this reason, we compare the algorithms based on iteration counts." It also says what it did not measure: "We do not currently compare the number of function evaluations with IPOPT", and it points to SNOPT as better when function evaluations are expensive.
- A robustness check at a looser tolerance: OnePhase re-runs both solvers at 10⁻² (one-phase fails 10 times, IPOPT 41).
- **Consistency check (mine).** The repository's `benchmark-tables/table_CUTEst_IPOPT.csv` gives 238 rows: optimal 191, INIT_ERROR 19, MAX_TIME 9, ERROR 8, primal_infeasible 8, MAX_IT 3. The failures sum to 39, as the paper says. One-phase: MAX_IT 13 + MAX_DELTA 4 + MAX_TIME 4 = 21, as the paper says. **About half of IPOPT's counted failures (19 of 39) are `INIT_ERROR`.** The paper does not break them down. [inferred: these may be harness or initial-point errors rather than algorithmic failures; not checked.]

**4.5 Candour about cost and weak spots inside the paper.** [practice] (P)
- DRSOM v1 §4.4.2: "In our preliminary experiments, the vanilla DRSOM is five times slower than Adam in running time at the same iteration number; thus, we only run DRSOM in 50 epochs. For Adam, we collect the results in 100 epochs." (The unequal-epoch design is stated openly.)
- HDSDP §7, "When (not) to use DSDP/HDSDP": "If the problem is dense and most constraints are full-rank, dual method has no advantage over the primal-dual solvers". Also: "dual methods still suffer from failure to identify primal infeasibility."
- OnePhase §6: "A disadvantage of using the Cholesky factorization is that we often had difficulty obtaining a sufficiently accurate solution as we approached optimality." It also reports sensitivity to the initial barrier value (manual tuning "often significantly reduces the number of iterations"), and compares that to "Lustig's IPM for linear programming".
- HSODF v5 §5.1: "it seems that the Lanczos method should be modified to adopt better inexactness strategies since the gap-dependent conditioning is missing in the general case (Section 2.1). We leave this improvement for future study."

**4.6 Debugging behaviour (group, not Ye).** [practice] (P; student-authored)
- OnePhase `to_do.md` (Hinder, 2017–2019) is a rare look at the debugging agenda. Items include:
  - "write code that saves all the CUTEst files need for the paper in one go! (i.e., have an experimental script and a paper producing script)"
  - "detect is problem is caused by factorization issues or lack of smoothness of functions (identify function, a direction and a point)"
  - "increase delta when ever there is any sort of failure"
  - "solve MUMPS issues, version"
  - long-term items that carry Ye-school ideas: "(1) find LP solution first, (2) start from analytic centre, (3) re-write so problem is well-conditioned" and "momentum/homogenous style scaling".
- DRSOM.jl: `test_setup.jl` runs a smoke test on one CUTEst problem before every batch ("include a small test to make sure everything works"). It holds about 30 commented-out `filter_optimization_method` lines, so method selection is switched by hand.
- Commit messages are terse (31 of 156 begin with "update"; others read "xs", "ss", "cc", "idd").
- [inferred] The group's engineering is fast and informal. Rigour lives in the papers' protocols more than in the repository hygiene.

**4.7 His own 1993 code: documentation drifted from behaviour, and the drift survives to 2021.** [practice] (P; Ye's own code)
- The doc says the adaptive centring switch fires when min(x.*s)/μ "is bounded from below by constant (1-beta)/10". The code tests `>= (1-beta)` with no /10.
- The doc says `toler` "Default value: 1.0e-6". The code sets `toler = 1.e-8`.
- Optional inputs (`u`, `bindx`, `findx`, `toler`, `beta`) are tested with `exist('…')` inside a function that takes only `(A,b,c)`, so the user cannot pass them and the defaults always apply. When `bindx` is non-empty, `u` would be undefined. [inferred from reading the code; not run]
- All of this is unchanged in the 2021 5th-edition copy.

---

## 5. Judging results: what they keep, cut, correct and split off

**5.1 Claims narrowed or dropped between versions.** [practice] (P)
- **DRSOM, v1 (2022-07-30) → v3 (2023-07-02).**
  - v1 title: "…and Preliminary Analyses". v1 abstract: "For neural networks, our preliminary implementation seems to gain computational advantages in terms of training accuracy and iteration complexity over state-of-the-art first-order methods including SGD and ADAM." v1 experiments: logistic regression (MNIST), L2–Lp, SNL, Fashion-MNIST, CIFAR10/ResNet18.
  - v3 abstract ends: "…including L2−Lp minimization, CUTEst problems, and sensor network localization." The neural-network and logistic-regression sections are gone; a CUTEst benchmark and large SNL instances (up to 10,000 sensors) come in.
  - v2 and v3 add local quadratic convergence and a "corrector step" that removes an assumption. The comment on both: "Considerable changes in the main text".
  - No journal version was found in Crossref (2026-09-28), and the README still cites the arXiv version. [not evidence of rejection]
- **The deep-learning line did not die; it moved.** DRAG, "Dimension-Reduced Adaptive Gradient Method" (Li, Zhou, Ding, Toh, Ye), appeared at the NeurIPS 2022 OPT workshop (ML Anthology record). Its OpenReview forum is Xp-__WzXiBy. Reviews were not read (§Gaps).
- **UTR, v1 (2023-11) → v4 (2026-01).** It was retitled from "A Universal Trust-Region Method for Convex and Nonconvex Optimization" to "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses". The v1 clause "attains an O(ε^{-1/2}) complexity bound for convex optimization and can be accelerated" loses "and can be accelerated" in v4. Acceleration became a separate paper (ATR, arXiv 2511.00680).
- **HSODM, v1 (42 KB) → v7 (692 KB), 2022-11 → 2026-06; MOR 51(2), 10.1287/moor.2023.0132.** v1 had no numerical claim in the abstract. v7 adds "The numerical results demonstrate the advantage of the proposed method over other second-order methods". The baselines were upgraded (§4.3).
- **Hinder & Ye, worst-case barrier bounds (arXiv 1807.00404, 5 versions 2018→2023; MOR 49(4) 2024, 10.1287/moor.2020.0274).** The arXiv comment: "Note that several results were removed from the previous version most notably the results on convex case. These results were removed due to reviewer suggestions to focus the paper on the most significant contributions. These results still appear in the first author's PhD thesis". **This is the only documented reaction to reviewers I found: comply and cut, but keep the material in the student's thesis.**

**5.2 Negative results reported as findings.** [practice] (P)
- ATR (arXiv 2511.00680v3) has "An Attempt" in its title. Abstract: "quadratic local convergence is preserved under moderate global acceleration, but it breaks down when pursuing extreme global efficiency." Text: "While the proposed algorithm attains a near-optimal global oracle complexity rate, it fails to balance the global guarantees and the local efficiency." The experiments section is framed as confirming the trade-off.
- The 2023 talk slide (YE20230630.pdf, slide 29, "App. V: Neural Networks and Deep Learning") has a "Cons" list next to the "Pros": "DRSOM may over-fit the models".

**5.3 Errata and corrections.** [practice] (P)
- *Interior Point Algorithms* (1997), correction.html. The page still shows his Iowa address. Most items are typos, and each reader who found one is thanked by name and institution. Among them:
  - one inequality direction and one theorem constant: "Theorem 3.11 and Exercise 3.8: Change "\eta(x,s)\le 1" to "\eta(x,s)\le 1/\sqrt{2}""
  - a strict inequality in Algorithm 5.2 made non-strict
  - two citation errors, each with an apology: "Reference [52]: Change "D. P. Bertsekas" to "D. Bertsimas". I apologize to Bertsimas for this error."
- *Linear and Nonlinear Programming*, 5th ed. errata (PDF by Yinyu Ye, 2022-03-10). Three items, one of them substantive (a second-order condition): "Page 527, line 7, change "… is positive semidefinite" to "remains positive definite in the null-space of A"".
- Journal corrections found in Crossref (contents **not read**):
  - Burer & Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 190 (2021) 845–848, 10.1007/s10107-021-01684-5 (corrects 10.1007/s10107-019-01367-2);
  - Dang & Ye, "Erratum/Correction to 'On the complexity of an expanded Tarski's fixed point problem under the componentwise ordering'", *TCS* 817 (2020) 80, 10.1016/j.tcs.2019.03.014.
- arXiv revision notes that fix signs or errors: 1801.03072 v2, "fixed typo in sign of dual multiplier in KKT system" (two days after v1); 1208.5083, "Minor typo fixes and improvements over version 1". No retraction found.

**5.4 Mixed results are published with the honest numbers.** [practice] (P)
- HDSDP Table 7, on part of Mittelmann's collection: HDSDP solved 67 with SGM 228.64; DSDP5.8 62 and 276.96; COPT v6.5 72 and 100.53. The paper keeps its claim to a niche ("advantages on SDP instances featuring low-rank structure and sparsity") rather than claiming overall superiority.
- cuPDLP-C: in the body, on the standard sets, "cuPDLP-C performs around 2 to 4 times slower than COPT with different presolvers", and the wins are shown on the handpicked large instances of §3.3. The abstract is pitched higher: "The experiments further highlight its substantial computational advantages and potential for solving large-scale linear programming problems. We also discuss the profound impact this breakthrough may have on mathematical programming research and the entire operations research community." (see K4)

---

## 6. Expression in practice

- **The word "preliminary" is systematic.** [practice] (P) It appears in the DRSOM v1 title ("Preliminary Analyses") and abstract ("our preliminary implementation"), in HSODF ("some preliminary numerical results") and in HSODM v7 ("these preliminary implementations"). [inferred] It hedges the experiments while the theory carries the paper.
- **Software papers carry a "when not to use" section.** HDSDP §7 is the example (see §4.5).
- **Performance profiles plus SGM tables**, with full per-instance tables in appendices (DRSOM v3 Tables A.1–A.2; HDSDP Tables 9–14; OnePhase publishes CSVs under `benchmark-tables/`). [practice] (P)
- **Titles that concede.** "An Attempt to Balance Global and Local Efficiency" (ATR); "When Does Primal Interior Point Method Beat Primal-dual…?" [practice] (P)
- **The 1997 monograph gives implementation 27 pages of about 400.** Chapter 10, "Implementation Issues" (pp. 337–363), covers presolver, normal equations vs augmented system, numerical phase, iterative methods, high-order predictor–corrector, HSD, and optimal-basis identification (TOC read from main.ps; chapter text **not read**). [practice] (P)

---

## 7. Research organisation in practice

- **Papers are written with students, and the student is first author.** In 2020–2024, 87 of 107 OpenAlex-attributed papers have Ye as last author (see `sources/publications/publications.md`, an automated count; secondary). The code evidence (§4.1) agrees. [practice] (P/S)
- **A core team of 5–6 people carries each second-order paper from one codebase.** The authors are Zhang C., He C., Jiang Y., Ge D., Jiang B. and Ye, in rotating first-author order. They wrote DRSOM (2022), HSODM (2022), HSODF (2023), UTR (2023) and ATR (2025); ATR's authors are Jiang Y., Zhang C., Jiang B. and Ye (no Ge, no He). HAR (arXiv 2511.05788) is by the same students without Ye and lives in the same DRSOM.jl repository. [practice] (P) [inferred: the codebase outlives his involvement in each paper]
- **Team size scales with engineering.** The enhanced ABIP (arXiv 2209.01793) has 11 authors and cuPDLP-C has 9; OnePhase (2018) had 2. [practice] (P)
- **Revision timescales are long.** HSODM took 3.5 years from arXiv v1 to its final version, the barrier-bounds paper 6 years (2018 → MOR 2024), and smart crossover 4 years (7 versions, IJOC 2025). [practice] (P)
- **External contributors are welcomed into the public code.** In cuPDLP-C, Hannes Uppman (27 commits, custom CUDA kernels), Oscar Dowson ("Remove reference to Clp in the README") and Søren Fuglede Jørgensen had their PRs merged. [practice] (P)
- **Options are abandoned in the open.** The cuPDLP-C README parameter table shows a struck-out option: "Choose line search: 0-fixed, ~~1-Malitsky~~, 2-Adaptive". Presolve moved from CLP to HiGHS ("replace CLP by HiGHS to load mps and presolve", 2024-01-07). [practice] (P)
- **His 1990s distributions are no longer maintained.** The three COPL download links on book.html point to `http://www.stanford.edu/~yyye/Col`, which returns Stanford's "Page not found" page (checked 2026-09-28). [observed by me] (P)

---

## Contradictions (kept, not reconciled)

- **K1. Infeasibility certificates: stated as essential (R8), but shipped later in practice.** He states (02 R8, S8/S13/S19) that an algorithm should certify infeasibility. The cuPDLP-C repository was public from 2023-12-12 and its arXiv v1 came out 2023-12-22, yet "add infeasibility detection; fix some bug" is dated 2024-01-22 and the v0.4.0 merge "add python interface, add postsolve and infeasible detection" 2024-01-31. HDSDP's own paper says its dual method "still suffer[s] from failure to identify primal infeasibility". In the older HSD line (1993 code; OnePhase 2018), by contrast, infeasibility detection is built in from the start.
- **K2. "Potential reduction" in name, fraction-to-boundary in code (bears on 02 C4).** The 2021 header calls HSDLPsolver.m a "Primal-Dual Potential-Reduction Algorithm". The code evaluates no potential or log-barrier function. It takes a fixed `beta = .995` fraction-to-boundary step and switches the centring weight `gamma` between 1/√(n+nb+1) and 0 by a centrality test, which is path-following / predictor-style behaviour. The 1993 doc of the same code called it "the homogeneous and selfdual interior-point algorithm". So a stated merit-function preference (02 C4) and a potential-reduction label sit on code that behaves otherwise.
- **K3. Deep learning: promoted in talks, dropped from the paper.** Talk of 2023-06-30 (YE20230630.pdf, slide 29): "Good potential to be a standard optimizer for deep learning!" arXiv DRSOM v3, two days later (2023-07-02), drops the neural-network experiments from the abstract and experiments. The DL line continued separately (DRAG, NeurIPS 2022 OPT workshop).
- **K4. Candid paper bodies, promotional abstracts and talks (bears on 02 C6).** In paper bodies, slowness is reported in plain words: DRSOM "five times slower than Adam"; OnePhase "IPOPT is generally significantly faster"; cuPDLP-C "2 to 4 times slower than COPT". The cuPDLP-C abstract speaks of "substantial computational advantages" and "this breakthrough", and the talks (02 §1.4, S18) lead with multiplicative speed-ups. Both come from the same group and period.
- **K5. The ill-conditioning claim vs the observed conditioning limit (bears on 02 C3).** The HSODF abstract: GHM "can be solved by extremal symmetric eigenvalue procedures and thus grant an advantage in ill-conditioned problems". The same paper's experiments note that the Lanczos solver lacks "gap-dependent conditioning … in the general case" and needs better inexactness strategies.
- **K6. "Developer" without commits.** The DRSOM.jl README lists Ye as a developer, but none of its 156 commits is his. This may just be a different sense of "developer" (design vs code). Recorded, not resolved.
- **K7. Documentation vs behaviour in his own code** (§4.7). The documented threshold (1-beta)/10 and tolerance 1e-6 differ from the coded (1-beta) and 1e-8. Unchanged 1993–2021.

---

## Gaps (searched for and not found, or not read)

- **OpenReview reviews and rebuttals: not read.** The API (api.openreview.net and api2) and the web forum both returned a bot-challenge page (HTTP 403 "ChallengeRequiredError"), and WebFetch saw only the verification screen. Forums known to exist: Xp-__WzXiBy (DRAG), AM1UcqDDDv ("Solving Linear Programs with Fast Online Learning Algorithms"), a51bLzOy1u ("Online Linear Programming for Multi-Objective Routing in LLM Serving"). The decisions and reviewer criticisms of Ye's ML-venue submissions are therefore unknown. One WebSearch returned a snippet claiming an ICLR 2023 submission date for DRAG. I could not verify it, so it is not used.
- **DBLP** (Anubis bot wall), **Semantic Scholar** (HTTP 429) and **OpenAlex search** (rate-limited) were unavailable for venue checks. I used Crossref and arXiv instead.
- **Contents of the two journal corrections** (Burer–Ye 2021; Dang–Ye 2020): not read. Springer's page returned a JavaScript client challenge, and I did not try Elsevier.
- **Journal (final) versions** of HSODM (MOR), HSODF (MP), UTR (JSC), HDSDP and SOLNP+ (TOMS): not read. I used the latest arXiv versions, which carry the acceptance notes.
- **Early implementation papers**: Xu–Hung–Ye 1996 (*Ann. Oper. Res.* 62:151–171, 10.1007/BF02206815) and Andersen–Ye 1998 (*COAP* 10:243–269, 10.1023/A:1018369223322) were **not read** (no open copy found; Crossref has no abstracts). The NETLIB-era test protocol of his own group (1993–1998) is therefore undocumented here, beyond the sample files shipped with hsdLPsolver.m.
- ***Interior Point Algorithms*, Ch. 10**: only the TOC was read.
- **DSDP5 source code** (Argonne) and the **1997 COPL codes**: not examined. The COPL links are broken.
- **COPT internals**: closed source, so the group's production-solver practice is unobservable.
- **Status of DRSOM (2022) and of the one-phase IPM (2018)**: no journal version was found in Crossref for either. Whether they were rejected, withdrawn or never submitted is unknown.
- **Ye's own debugging or code-review behaviour after 2000**: no primary evidence. The repositories show only the students'. Agent 04 (mentorship) may find recollections.
- **Rejected papers**: none documented directly. The only visible reviewer interaction is the arXiv comment on 1807.00404.
- **About 5 minutes without results**: a machine-readable arXiv author query (export.arxiv.org returned 301/406). Replaced by the arXiv HTML author search.

---

## Sources

Ye's own homepage artefacts (all primary, accessed 2026-09-28):
1. Homepage, https://web.stanford.edu/~yyye/ (P)
2. "Recent Papers", https://web.stanford.edu/~yyye/newpapers.html (P)
3. Book page for *Interior Point Algorithms* (software links), https://web.stanford.edu/~yyye/book.html (P)
4. "List of Corrections" (IPA 1997 errata), https://web.stanford.edu/~yyye/correction.html (P)
5. LY 5th-edition errata, https://web.stanford.edu/~yyye/LYLNLP5therrata.pdf (PDF metadata author Yinyu Ye, created 2022-03-10) (P)
6. Matlab codes page (2004), https://web.stanford.edu/~yyye/matlab.html; code files hsdLPsolver.m, solnp.m, subnp.m under /matlab/ (P)
7. LY 5th-edition Matlab page, https://web.stanford.edu/~yyye/LYtextbook5thMatlab/LY5thmatlab.html; HSDLPsolver.m and solnp.m (updated 11/7/21) (P)
8. Y. Ye, "SOLNP Users' Guide — A Nonlinear Optimization Program in MATLAB", University of Iowa, August 1989, https://web.stanford.edu/~yyye/matlab/manual.ps (P)
9. Y. Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley 1997, DOI 10.1002/9781118032701; front matter/TOC from https://web.stanford.edu/~yyye/main.ps (P)
10. Y. Ye, "On a First-Order Potential Reduction Algorithm for Linear Programming", note dated July 30, 2015, https://web.stanford.edu/~yyye/FO-potential-reduction.pdf (P)
11. Y. Ye, "A Second-Order Path-Following Algorithm for Unconstrained Convex Optimization", note dated May 31, 2017, https://web.stanford.edu/~yyye/min-norm-path0.pdf (P)
12. Y. Ye, "Mathematical Optimization in Machine Learning/Decision-Making", slides, 2023-06-30 (PDF author metadata "xcy27"), https://web.stanford.edu/~yyye/YE20230630.pdf (P, team-prepared)

Code repositories (primary; cloned with full history on 2026-09-28):
13. DRSOM.jl, https://github.com/bzhangcw/DRSOM.jl (156 commits, 2022-07-31 → 2026-06-18) (P)
14. OnePhase, https://github.com/ohinder/OnePhase (168 commits, 2017-05-05 → 2023-09-18) (P)
15. cuPDLP-C, https://github.com/COPT-Public/cuPDLP-C (95 commits, 2023-12-12 → 2024-12-18) (P)
16. HDSDP, https://github.com/COPT-Public/HDSDP (8 commits, 2022-07-15 → 2025-04-07) (P)
17. SOLNP_plus, https://github.com/COPT-Public/SOLNP_plus (2022-09-02 → 2025-05-13) (P)

Papers (identifiers checked by tool in this run; full text read where marked):
18. C. Zhang, D. Ge, C. He, B. Jiang, Y. Jiang, Y. Ye, "DRSOM: A Dimension Reduced Second-Order Method", arXiv:2208.00208 (v1 2022-07-30 "…and Preliminary Analyses", v2 2023-01-02, v3 2023-07-02); v1 and v3 full text read (P)
19. C. Zhang, C. He, Y. Jiang, C. Xue, B. Jiang, D. Ge, Y. Ye, "A homogeneous second-order descent method for nonconvex optimization", arXiv:2211.08212 (v1, v3, v7 read); *Math. Oper. Res.* 51(2), 2026, DOI 10.1287/moor.2023.0132 (P)
20. C. He, Y. Jiang, C. Zhang, D. Ge, B. Jiang, Y. Ye, "Homogeneous second-order descent framework: a fast alternative to Newton-type methods", arXiv:2306.17516 (v1 abstract, v5 read); *Math. Program.* 2025, DOI 10.1007/s10107-025-02230-3 (P)
21. Y. Jiang, C. He, C. Zhang, D. Ge, B. Jiang, Y. Ye, "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", arXiv:2311.11489 (v1 abstract, v4 read); *J. Sci. Comput.*, DOI 10.1007/s10915-025-03154-y (P)
22. Y. Jiang, C. Zhang, B. Jiang, Y. Ye, "Accelerating Trust-Region Methods: An Attempt to Balance Global and Local Efficiency", arXiv:2511.00680 (v3 read) (P)
23. C. He, B. Jiang, Y. Jiang, C. Zhang, S. Zhang, "History-Aware Adaptive High-Order Tensor Regularization", arXiv:2511.05788 (abstract page only; Ye not an author) (P)
24. H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832 (v1 and v2 read and diffed) (P)
25. W. Gao, D. Ge, Y. Ye, "HDSDP: Software for Semidefinite Programming", arXiv:2207.13862 (v2 read); *ACM TOMS* Algorithm 1055, 2025, DOI 10.1145/3721123 (P)
26. D. Ge, T. Liu, J. Liu, J. Tan, Y. Ye, "SOLNP+: A Derivative-Free Solver for Constrained Nonlinear Optimization", arXiv:2210.07160 (v1 read); *ACM TOMS* Algorithm 1053, 2024, DOI 10.1145/3699956 (P)
27. O. Hinder, Y. Ye, "A one-phase interior point method for nonconvex optimization", arXiv:1801.03072 (v2 read) (P)
28. O. Hinder, Y. Ye, "Worst-Case Iteration Bounds for Log Barrier Methods on Problems with Nonconvex Constraints", arXiv:1807.00404 (abstract page and comment); *Math. Oper. Res.* 49(4) 2402–2424, 2024, DOI 10.1287/moor.2020.0274 (P)
29. G. Haeser, O. Hinder, Y. Ye, "On the behavior of Lagrange multipliers in convex and nonconvex infeasible interior point methods", arXiv:1707.07327 (abstract); *Math. Program.* 2019, DOI 10.1007/s10107-019-01454-4 (P)
30. W. Gao, H. Liu, Y. Ye, M. Udell, "When Does Primal Interior Point Method Beat Primal-dual in Linear Optimization?", arXiv:2411.16015 (abstract) (P)
31. D. Ge, C. Wang, Z. Xiong, Y. Ye, "From an Interior Point to a Corner Point: Smart Crossover", arXiv:2102.09420 (version history; J-ref IJOC 37(6), 2025) (P)
32. T. Lin, S. Ma, Y. Ye, S. Zhang, "An ADMM-Based Interior-Point Method for Large-Scale Linear Programming", arXiv:1805.12344; *Optim. Methods Softw.* 36(2–3):389–424, DOI 10.1080/10556788.2020.1821200 (abstract) (P)
33. Q. Deng et al. (11 authors incl. Y. Ye), "An Enhanced ADMM-based Interior Point Method for Linear and Conic Optimization", arXiv:2209.01793 (abstract) (P)
34. Y.-C. Chu, W. Gao, Y. Ye, M. Udell, "Gradient Methods with Online Scaling Part II. Practical Aspects", arXiv:2509.11007 (abstract) (P)
35. Z. Lin, Z. Xiong, D. Ge, Y. Ye, "A Practical GPU-Enhanced Matrix-Free Primal-Dual Method for Large-Scale Conic Programs", arXiv:2505.00311 (abstract, versions) (P)
36. Y. Su, C. Zhang, P. Huang, T. Li, Y. Ye, "Scalable First-Order Interior Point Trust Region Algorithms for Linearly Constrained Optimization", arXiv:2604.24488 (abstract) (P)
37. S. J. Benson, Y. Ye, X. Zhang, "Solving Large-Scale Sparse Semidefinite Programs for Combinatorial Optimization", *SIAM J. Optim.* 10(2):443–461, 2000, DOI 10.1137/S1052623497328008 (Crossref abstract) (P)
38. P. Biswas, T.-C. Lian, T.-C. Wang, Y. Ye, "Semidefinite programming based algorithms for sensor network localization", *ACM Trans. Sensor Networks*, 2006, DOI 10.1145/1149283.1149286 (Crossref abstract) (P)
39. P. Biswas, Y. Ye, "Semidefinite programming for ad hoc wireless sensor network localization", IPSN 2004, DOI 10.1145/984622.984630 (record only) (P)
40. X. Xu, P.-F. Hung, Y. Ye, "A simplified homogeneous and self-dual linear programming algorithm and its implementation", *Ann. Oper. Res.* 62:151–171, 1996, DOI 10.1007/BF02206815 (record only; not read) (P)
41. E. D. Andersen, Y. Ye, "A Computational Study of the Homogeneous Algorithm for Large-scale Convex Optimization", *Comput. Optim. Appl.* 10(3):243–269, 1998, DOI 10.1023/A:1018369223322 (record only; not read) (P)
42. S. Burer, Y. Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", *Math. Program.* 190:845–848, 2021, DOI 10.1007/s10107-021-01684-5 (record only; not read) (P)
43. C. Dang, Y. Ye, "Erratum/Correction to 'On the complexity of an expanded Tarski's fixed point problem under the componentwise ordering'", *Theor. Comput. Sci.* 817:80, 2020, DOI 10.1016/j.tcs.2019.03.014 (record only; not read) (P)
44. J. Li, P. Zhou, K. Ding, K.-C. Toh, Y. Ye, "Dimension-Reduced Adaptive Gradient Method", NeurIPS 2022 Workshops: OPT, ML Anthology https://mlanthology.org/neuripsw/2022/li2022neuripsw-dimensionreduced/ ; OpenReview forum Xp-__WzXiBy (not readable) (P record / S index)

Listings and third-party (secondary unless noted):
45. arXiv author search for "Yinyu Ye" (139 entries with comments), https://arxiv.org/search/?query=%22Yinyu+Ye%22&searchtype=author, accessed 2026-09-28 (S, index)
46. Crossref REST API records for items 19–43 (S, index)
47. MOSEK Optimization Toolbox manual, §13.2.2 "The Interior-point Optimizer", https://docs.mosek.com/latest/toolbox/solving-linear.html, accessed 2026-09-28 (S, observed)
