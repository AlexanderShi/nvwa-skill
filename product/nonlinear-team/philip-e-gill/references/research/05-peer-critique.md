# Philip E. Gill · 05 Peer critique: counterexamples, rival benchmarks, rival schools, and how the group answered

- **Researcher**: Philip E. Gill, Department of Mathematics, UC San Diego (at UCSD since 1988; earlier NPL and Stanford SOL). Living; distilled from public academic output only.
- **Dimension**: research agent 05 of 06 (peer critique: blind spots, limits of applicability, judgements shown to be wrong, and the replies), nuwa research-craft mode.
- **Research date**: 2026-09-28
- **Sources consulted**: 44 (listed under "Sources"; 36 primary, 8 secondary or bibliographic). WebSearch calls used: 2. The first found the Izmailov–Uskov and Izmailov–Solodov–Uskov leads (their texts were then not accessible). The second found the OpenSQP benchmark (arXiv 2512.05392), which was then read. No finding below rests on a search-result snippet.
- **Local corpus**: `references/sources/{papers,essays,software}` held only `.gitkeep`. `talks/` held the auto-caption transcript of the 2019 INFORMS interview with Margaret H. Wright, which agent 01 saved from YouTube. It is a web source, not user-supplied. No user-supplied material existed, so nothing below is "from user-supplied material". `private/` was not opened.
- **What was actually read**:
  - Critics' texts read in full or in the stated parts: Hall & McKinnon (arXiv v1, all 21 pp.); Dolan & Moré (arXiv v1, pp. 6–10); Benson, Shanno & Vanderbei (ORFE-01-04 rev. 2002, pp. 1–2, 9, 12–22); Morales, Nocedal, Waltz, Liu & Goux (preprint, pp. 1–15, from a damaged text layer, see the caveat below); Byrd, Nocedal & Waltz, KNITRO (preprint, pp. 1–2 and 12); Izmailov & Solodov 2011 (author copy, pp. 1–2 and 24–25); Joshy & Hwang, OpenSQP (arXiv, pp. 1–2, 10, 12–13); the Mittelmann AMPL-NLP benchmark page (9 Sep 2026).
  - Critics read only as abstracts: Schnabel & Eskow 1990 and 1999, Cheng & Higham 1998, Izmailov & Solodov 2015, Zhurbenko, Izmailov & Uskov 2019.
  - Gill-group replies read in the stated parts: GSW15 pp. 3, 13 and 26; the SNOPT 7.5 guide pp. 1, 4, 9, 72 and 81; the SQOPT 7.5 guide p. 11; Gill & Wong CCoM 13-1 p. 27; Gill & Wong NA-10-03 pp. 2–3 and 16; Forsgren–Gill–Wright 2002 journal pp. 588–590; GKR CCoM 13-04 pp. 1–3; PDB 2020 PDF p. 23.
  - Everything else was checked at the level of metadata (Crossref, zbMATH, OpenAlex, Semantic Scholar). It is marked "not read".
- **Text-layer caveat (Morales et al. preprint)**: the PDF uses Type-3 fonts. The extracted text keeps the words but drops punctuation, the ligatures "fi"/"ff" and all digits. Quotations from it below reproduce the words exactly. They restore the ligatures and the hyphens inside compound words (e.g. "quasi-Newton", "active-set", "limited-memory"), and add no other punctuation. Numbers that were lost are written as "[digits lost]".
- **Tag legend**:
  - [stated]: words of Gill or his co-authors.
  - [practice]: what the Gill group's papers, manuals, software or records show was done.
  - [observed]: what others (critics, benchmarkers, reviewers) report.
  - [inferred]: my inference, with its basis.
  - Each item also says primary (P) or secondary (S). A critic's own publication counts as primary evidence *of the critique*.
- **Attribution caveat**: Gill's papers list authors alphabetically and are all co-authored (01 §0). A critique "of Gill" is therefore always a critique of a group's product (SNOPT, EXPAND, the GMW modified Cholesky, the stabilized-SQP line). None of the critics found addresses Gill personally.

---

## 0. Summary of the strongest findings

1. **One published counterexample to a Gill-group claim, answered by citing it as reassurance.** Hall & McKinnon (Math. Program. 2004) built LP examples on which the EXPAND "anti-cycling" procedure cycles indefinitely, including inside MINOS 5.4. They concluded that EXPAND "cannot be relied upon to prevent cycling". Twelve years later the SQOPT 7.5 guide and the Gill–Wong QP report cite the same paper for the statement that the probability of cycling "is very small". The critic's conclusion and the defender's reading of it are both recorded (Contradictions 1). §1.1
2. **The recurrent external verdict on SNOPT is a limit of applicability, not an error.** Four independent benchmark groups found the same boundary across 25 years: Dolan & Moré (2001/02), Benson, Shanno & Vanderbei (2001/02), Morales, Nocedal, Waltz, Liu & Goux (2003) and Mittelmann (2026). SNOPT is robust when the number of degrees of freedom is small. It slows down, or reaches its time limit, when the number of degrees of freedom is large, and it has only first derivatives while its competitors get second derivatives. The group had written this limit into its own abstract ("say, up to 2000"). It answered with a *fairness* argument about test protocols (GSW15: give both codes the same derivatives, stratify by degrees of freedom) and with an agenda (SQIC, convexification, SNOPT9). SNOPT9 is still "Currently in development" on the UCSD site in September 2026, eleven years after the 2015 paper announced it as "forthcoming". §3, §7
3. **The rival schools' critique of SQP was conceded, not rebutted.** The KNITRO authors wrote that the cost of general QP subproblems "imposes a limitation on the size of problems" and that second derivatives in SQP had "proved to be difficult". Gill & Wong (2010) and Gill & Robinson (2013) say the same in their own words ("a major impediment"), and the whole post-2010 programme is built on that concession. §4
4. **A rival group's finding became the group's own problem.** Izmailov & Solodov (Math. Program. 2011) showed on degenerate problems that SNOPT (and MINOS) is typically attracted to critical Lagrange multipliers, and that "as a consequence, convergence is slow". The Gill–Robinson–Kungurtsev stabilized-SQP papers cite this work as motivation. The same rival group then argued that every globalization of stabilized SQP "inevitably" faces "principal difficulties". Gill–Kungurtsev–Robinson answer with a counter-critique: the rivals' analyses "require a global solution" of a nonconvex QP. §5
5. **Silence is also a reply pattern.** No published reply was found to the modified-Cholesky critiques (Schnabel & Eskow 1990/1999, Cheng & Higham 1998). None was found to the Morales et al. remark that SNOPT's convergence theory is "difficult to establish", or to the Benson–Shanno–Vanderbei verdict by name. GSW15 cites none of these benchmark studies. It rebuts the "conventional wisdom" as a whole. §2, §3.6

---

## 1. Counterexamples to published claims (framework layer 5: result judgement)

### 1.1 EXPAND does not prevent cycling (Hall & McKinnon)

- **The claim criticised** [practice, P via S]: Gill, Murray, Saunders & Wright, "A practical anti-cycling procedure for linearly constrained optimization", Math. Program. 45 (1989) 437–474, DOI 10.1007/BF01589114. **Full text not read.** The public zbMATH review (Zbl 0688.90038, reviewer X.-S. Zhang) reports the paper's claim that "“stalling” cannot occur with exact arithmetic" and its verdict: "The paper reports the authors’ computational results and the method appears to be reliable." [observed · S]
- **The critique** [observed · P]: J. A. J. Hall & K. I. M. McKinnon, "The simplest examples where the simplex method cycles and conditions where EXPAND fails to prevent cycling", Math. Program. 100(1, Ser. B) (2004) 133–150, DOI 10.1007/s10107-003-0488-1; arXiv math/0012242 (v1, 22 Dec 2000; read in full).
  - Scope of the original claim, as the critics read it: "In addition it is claimed that stalling cannot occur with expand with exact arithmetic." (p. 2) They also credit the method: "The performance of minos was significantly improved by the incorporation of expand." (p. 3)
  - The logical gap they identify: "The analysis given by Gill et al [7] of their expand procedure proves that the objective function can never return to a value it had at a previous iteration. The expand procedure however relaxes the constraints at each iteration, so the fact that the objective function continually improves does not prove that the method will not return to a previous basic solution." (p. 11)
  - Conclusion: "The 2/6-cycle examples are therefore just points in a full dimensional set of counter-examples, so there is a positive probability of encountering cycling in randomly generated degenerate examples. In practice therefore the expand procedure cannot be relied upon to prevent cycling." (p. 19) Also: "The cycling behaviour is independent of the expand tolerance parameters." (p. 19)
  - Tested on the group's own code: "The examples have been tested on our own implementation of expand and using minos 5.4, which was written by the authors of expand. In both cases if no preprocessing is done the examples cycle indefinitely." MINOS's periodic reset "returns the problem to its initial state so cycling is still indefinite." (p. 20)
  - The rival school's code survives: "However the bqpd code of Fletcher [4] detects degeneracy at the start of the first iteration, changes to the dual, does one pivot, then finds that the dual is infeasible." (p. 20) bqpd belongs to Fletcher's primal-dual alternation family, of which Hall & McKinnon write: "Some of these methods guarantee to terminate in exact arithmetic and also exhibit good behaviour with inexact arithmetic." (p. 2)
  - Hedge the critics themselves make about cycling in general: "though such examples do seem to be very rare in practice" (p. 1).
- **Reply** [practice + stated · P]: there was no retraction, no erratum and no new procedure. The critique is cited, and the guarantee is restated in weaker form:
  - SQOPT 7.5 user's guide (Gill, Murray, Saunders, Wong; February 8, 2016), p. 11: "The EXPAND procedure of Gill et al. [9] takes advantage of δ to reduce the chance of cycling at a point where the active constraints are nearly linearly dependent. Although there is no guarantee of preventing cycling, the probability is very small (see Hall and McKinnon [11])."
  - Gill & Wong, "Methods for Convex and General Quadratic Programming", CCoM 13-1 (version of June 30, 2014), p. 27 (SQIC): "Although the EXPAND procedure provides no guarantee that cycling will not occur, the probability is very small (see Hall and McKinnon [43])." Journal version: Math. Program. Comput. 7 (2015) 71–112, DOI 10.1007/s12532-014-0075-x (journal page not checked).
  - The SNOPT 7.5 guide (p. 72) still names the option "part of the EXPAND anti-cycling procedure [13] designed to make progress even on highly degenerate problems", with the reset default "Expand frequency 10000" (the same 10,000-iteration reset that Hall & McKinnon show does not break the cycle).
- **Reading** [inferred]: the 1989 guarantee was about the objective (no stalling in exact arithmetic), and the procedure's name promised more than that proof covered. The group kept the heuristic, which is cheap and works on its test sets. It downgraded the claim from a guarantee to a probability, and it cited the counterexample paper as the source of that probability. The critics' own words support "rare" only for cycling in general (p. 1). For EXPAND on degenerate examples they conclude a "positive probability" and "cannot be relied upon" (p. 19). See Contradictions 1.
- **Era / resources**: EXPAND dates from the late-1980s Stanford SOL, where it was built for MINOS/LSSOL-era LP and QP solvers in Fortran 77. The critique came from Edinburgh LP specialists (EPSRC-funded), who tested it on MINOS 5.4, OSL 2.0, CPLEX 4.0.7 and XPRESS-MP 7.14 (p. 20).

### 1.2 The Wächter–Biegler non-convergence example (a counterexample the group reported against its own class of methods)

- **The critique** [observed · P, metadata only]: A. Wächter & L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", Math. Program. 88 (2000) 565–574, DOI 10.1007/PL00011386. **Not read** (the abstract is not deposited and Springer redirects to a login).
- **How the Gill side handled it** [practice · P]: Forsgren, Gill & Wright, "Interior Methods for Nonlinear Optimization", SIAM Rev. 44 (2002) 525–597, DOI 10.1137/S0036144502414942, journal pp. 588–590. They present the example in their own survey, citing [106]: "a class of one-dimensional examples was recently defined for which certain line-search barrier-SQP methods (section 6.2.2) fail to find a feasible point and, much more seriously, do not even converge to a meaningful point." (p. 588) They extend it with a failure of the penalty-barrier function, the device their own later work uses. As µ decreases, "one of these trajectories suddenly disappears at the point where the Hessian of the augmented penalty-barrier function of (6.25) becomes indefinite" (p. 589). They close: "Although these particular difficulties can be avoided, it is interesting to see what can go wrong in such a small and seemingly innocuous problem." (p. 589) The section opens: "interior methods successfully and efficiently solve large nonconvex nonlinear programming problems every day, but the possibility of strange or even pathological behavior should not be ignored." (p. 588)
- **Later practice** [practice · P]: the shifted primal-dual penalty-barrier code (PDB, SIOPT 30 (2020), DOI 10.1137/19M1247425; PDF p. 23 of pdb.pdf) borrows the rival group's device for its COPS runs: "the Hessian was modified using the method of Wächter and Biegler [38, Algorithm IC, p. 36], which factors the KKT matrix with δIn added to H."
- **Open question** [inferred]: whether the Forsgren–Gill (1998) primal-dual method itself falls into the class of the 2000 paper was not established. The paper was not read, and the survey does not say.

### 1.3 SNOPT converges to critical multipliers on degenerate problems (Izmailov & Solodov)

- **The critique** [observed · P]: A. F. Izmailov & M. V. Solodov, "On attraction of linearly constrained Lagrangian methods and of stabilized and quasi-Newton SQP methods to critical multipliers", Math. Program. 126 (2011) 231–257, DOI 10.1007/s10107-009-0279-4 (author copy read, journal pp. 231–232, 254–255).
  - Abstract: "The question remained whether the attraction phenomenon still persists for relevant modifications, as well as in professional implementations. In this paper, we answer this question in the affirmative by presenting numerical results for the well known MINOS and SNOPT software packages applied to a collection of degenerate problems." (pp. 231–232)
  - Result: "Table 1 puts in evidence that attraction of MINOS and SNOPT to critical multipliers is typical and, as a consequence, convergence is slow. Results for sSQP are more mixed." (p. 254) The attraction matters because critical multipliers "violate the second-order sufficient optimality conditions, and this was shown to be the reason for slow convergence typically observed for problems with degenerate constraints" (abstract, p. 231).
  - Nuances they report: "SNOPT does not demonstrate any tendency of convergence to 0 for this problem: major iterates converge superlinearly to nonzero solutions" (Test 2.2, p. 254). "for SNOPT there are some rare cases of slow convergence to a critical multiplier" (Test 3.5, p. 255). "Regarding SNOPT for this problem, there are multiple cases of superlinear convergence to noncritical multipliers." (Example 2, p. 255)
  - Setup (era/resources): "we use the default versions of MINOS and SNOPT that come with AMPL [20] student edition; default values of parameters are used" (p. 253). The problems are small academic degenerate examples.
  - Follow-up survey [observed · P, abstract via RePEc]: Izmailov & Solodov, "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23 (2015) 1–26, DOI 10.1007/s11750-015-0372-1. The abstract says the attraction "shows up not only for the basic Newton method, but also for other related techniques (for example, quasi-Newton, and the linearly constrained augmented Lagrangian method)."
- **Reply** [practice · P]: the critique was absorbed as motivation, not contested. Gill, Kungurtsev & Robinson, "A Stabilized SQP Method: Global Convergence", CCoM-13-4 (October 31, 2013, revised June 23, 2015), p. 2: "Stabilized SQP methods are designed to resolve some of the numerical and theoretical difficulties associated with SQP methods when they are applied to ill-posed or degenerate nonlinear problems (see, e.g., … Fernández and Solodov [15], Izmailov and Solodov [23])." In 03 §1.7, the 2013 stabilized SQP paper tests on degenerate sets that the rival groups had used, among them the DEGEN subset used by Izmailov and Solodov. [practice · P via 03]

---

## 2. A competing implementation of a Gill algorithm: the modified Cholesky factorization

- **What was criticised** [practice · P, metadata]: the Gill–Murray modified Cholesky factorization (Gill & Murray, "Newton-type methods for unconstrained and linearly constrained optimization", Math. Program. 7 (1974) 311–350, DOI 10.1007/BF01585529; not read), refined as GMW81 in *Practical Optimization* (not read).
- **Critiques** [observed · P, abstracts]:
  - Schnabel & Eskow, "A New Modified Cholesky Factorization", SIAM J. Sci. Stat. Comput. 11 (1990) 1136–1158, DOI 10.1137/0911064. Abstract: "The modified Cholesky factorization of Gill and Murray plays an important role in optimization algorithms." The new method has the same properties "but for which the theoretical bound on ||E||∞ is substantially smaller", and "In extensive computational tests on indefinite matrices, the new factorization virtually always produces smaller values of ||E||∞ than the existing method, without impairing the conditioning of A + E."
  - Cheng & Higham, "A Modified Cholesky Algorithm Based on a Symmetric Indefinite Factorization", SIMAX 19 (1998) 1097–1110, DOI 10.1137/S0895479896302898. Abstract: they show "that the algorithm is competitive with the existing algorithms of Gill, Murray, and Wright and Schnabel and Eskow."
  - Schnabel & Eskow, "A Revised Modified Cholesky Factorization Algorithm", SIAM J. Optim. 9 (1999) 1135–1148, DOI 10.1137/S105262349833266X. Abstract (Crossref): "Compared with the Gill--Murray--Wright algorithm, the Schnabel--Eskow algorithm has a smaller a priori bound on the perturbation … Users of the Schnabel--Eskow algorithm, however, have reported cases from two different contexts where it makes a far larger modification to the original matrix than is necessary and than is made by the Gill--Murray--Wright method." After the revision: "the modifications to the original matrix made by the new algorithm appear virtually always to be smaller than those made by the Gill--Murray--Wright algorithm, sometimes by significant amounts."
  - Fang & O'Leary, "Modified Cholesky algorithms: a catalog with new approaches", Math. Program. 115 (2008) 319–349, DOI 10.1007/s10107-007-0177-6: **not read** (no abstract deposited; the UMD reprint directory returned 403).
- **Reply**: none found. The closest later Gill paper, Forsgren, Gill & Murray, "Computing Modified Newton Directions Using a Partial Cholesky Factorization", SISC 16 (1995) 139–150, DOI 10.1137/0916009, does not mention the Schnabel–Eskow bound in its abstract (full text not read). [practice · P, abstract only]
- **Reading** [inferred]: the rival's argument was a worst-case bound on the perturbation. The practical record swung back and forth: in some user contexts the older GMW method gave smaller modifications, until the 1999 revision. There is no evidence that the Gill group competed on the bound. Its later nonconvex work moved to other devices (partial Cholesky with negative curvature in 1995; inertia-controlling LDLᵀ factorizations, 03 §2.3), so the rivalry was left to others.

---

## 3. Benchmark studies by other groups: the limits of applicability (layers 4–5)

### 3.1 Dolan & Moré (Argonne), COPS, 2001/2002

- E. D. Dolan & J. J. Moré, "Benchmarking optimization software with performance profiles", Math. Program. 91 (2002) 201–213, DOI 10.1007/s101070100263; arXiv cs/0102001 (read pp. 6–10). [observed · P]
- Setup: LANCELOT, LOQO, MINOS and SNOPT under AMPL, with the superbasics limit raised to 5000 for MINOS and SNOPT and other options at default. The machine was a "SparcULTRA2 running Solaris 7", with a 3,600 s limit per solve (p. 6).
- Scope statement: "MINOS and SNOPT are specifically designed for problems with a modest number of degrees of freedom, while this is not the case for LANCELOT and LOQO." (pp. 6–7)
- Result on the COPS optimal-control and parameter-estimation subset: "SNOPT has a lower number of wins than either LOQO or MINOS, but its performance becomes much more competitive if we extend our τ of interest to 7." and "If we hold to more stringent probabilities of completing a solve successfully, then SNOPT captures our attention with its ability to solve over 90% of this COPS subset" (p. 8).
- On the full COPS set: "we should expect the performance of MINOS and SNOPT to deteriorate on the full COPS set", and a second reason is given: "MINOS and SNOPT use only first-order information, while LOQO uses second-order information." (p. 10)
- Tag: [observed] robust but slow on a problem class with few degrees of freedom; slower where the degrees of freedom are many and the rival has second derivatives.

### 3.2 Benson, Shanno & Vanderbei (Princeton, LOQO's authors), 2001/2002

- H. Y. Benson, D. F. Shanno & R. J. Vanderbei, "A Comparative Study of Large-Scale Nonlinear Optimization Algorithms", ORFE-01-04 (revised July 17, 2002); published in *High Performance Algorithms and Software for Nonlinear Optimization* (2003) 95–127, DOI 10.1007/978-1-4613-0241-4_5. Report read in part. [observed · P]
- Setup: LOQO, KNITRO and SNOPT (the "User's guide for SNOPT 5.3", 1997, is their ref. [9]) on AMPL models of size ≥ 1000. "The only option changed from its default value was increasing the maximum number of superbasic variables allowed for snopt so that it could attempt problems where this value was more than 50." (p. 12) AMPL supplied second derivatives to LOQO and KNITRO; SNOPT used its quasi-Newton default.
- Scope: "Because of its active set approach, snopt works well when the degrees of freedom, that is n − m, is small, generally in the several hundreds." (p. 9)
- Table 1 (p. 12): problems solved and total CPU seconds per category. My sums over the 8 categories: LOQO 177, KNITRO 198 and SNOPT 106 of 238 problems. On unconstrained NLPs SNOPT solved 16 of 56 (LOQO 46, KNITRO 37).
- Cases: cvxbqp1 (10,000 bounded variables): "snopt suffers from the many degrees of freedom in this unconstrained problem. It takes 10000 iterations and 121.86 seconds to solve this problem." (p. 15) Another problem: "snopt struggles, performing 8773 iterations for a problem with 2240 degress [sic] of freedom, and takes 1685.39 seconds." (p. 17) Another: "snopt ran for several hours without making any progress, due to the many degrees of freedom" (p. 18). A counter-case: on a problem with one degree of freedom, "snopt does very well with this problem, solving it in only 0.13 seconds … However, it also ends up at a worse solution than the other two solvers." (p. 15)
- Verdict: "Because it uses only first-order information to estimate the reduced Hessian, by using a limited memory BFGS, the results clearly show that when the degree of freedom is large, a quasi-Newton method is not competitive with a Newton approach." (p. 22)

### 3.3 Morales, Nocedal, Waltz, Liu & Goux (Northwestern / ITAM, KNITRO's group), 2003

- J. L. Morales, J. Nocedal, R. A. Waltz, G. Liu & J.-P. Goux, "Assessing the Potential of Interior Methods for Nonlinear Optimization", in *Large-Scale PDE-Constrained Optimization*, LNCSE 30 (2003) 167–183, DOI 10.1007/978-3-642-55508-4_10. The preprint (Nocedal's homepage) was read; see the text-layer caveat in the header. [observed · P]
- Their own caveat, which they state before the results: "even SNOPT which follows a well established active-set SQP approach is still being modified in significant ways Therefore we warn the reader against using our results to rank the codes" (p. 2). Also: "Our numerical tests were conducted in the fall of [digits lost] at that time a second derivative version of SNOPT was not available" (p. 7, footnote).
- On design choices: "But it is not a traditional unconstrained quasi-Newton method and no special consideration has been given to make the code efficient for unconstrained problems SNOPT maintains two approximate Hessians the limited-memory BFGS approximation of the full Hessian and a dense reduced Hessian Therefore for large problems it will be inefficient to keep both a sparse and a dense version of essentially the same [n × n, symbol lost] matrix" (p. 7).
- On theory: "Global convergence results are difficult to establish for SNOPT mainly because the merit function [symbol lost] is treated as a function of x s y and is therefore not minimized by a solution point" (p. 5). See Contradictions 2.
- On results:
  - "SNOPT required consistently more function evaluations than the other codes as is expected from a quasi-Newton method Computing times would improve if the dense quasi-Newton approximation were to be replaced by a limited-memory approximation" (pp. 9–10, unconstrained).
  - "We observe that SNOPT performs quite well compared to the other three codes despite using only first derivatives This is remarkable and contrasts with our observations for unconstrained and equality constrained problems" (p. 13, general constraints). On scaled-up versions: "We compared KNITRO and SNOPT but were not able to discern any clear trend" (p. 14).
  - On reporting: "SNOPTs performance in terms of function evaluations must be interpreted with caution because the code does not report them in the same manner as the other codes it may undercount them when the objective function is linear" (p. 14).
- Final remark: "The two rather different interior algorithms implemented in LOQO and KNITRO appear to be competitive in terms of robustness and efficiency with the active-set SQP algorithms implemented in SNOPT and filterSQP" (p. 15). From the abstract: "Overall interior methods appear to be strong competitors of active-set SQP methods but all codes show much room for improvement" (p. 1).

### 3.4 Mittelmann, AMPL-NLP benchmark (Arizona State), page dated 9 Sep 2026

- H. D. Mittelmann, "AMPL-NLP Benchmark", https://plato.asu.edu/ftp/ampl-nlp.html (fetched 2026-09-28). [observed · P for the data]
- Setup: "The codes were run in default mode and with a time limit of 2hrs on an AMD Ryzen 9 5900X (12 cores, 128GB)." SNOPT-7.7 was run against IPOPT-3.14.5, KNITRO-16.0, CONOPT-4.38.1, WORHP-1.16, FMINCON-2024a, COPT-8.0.0, UNO-2.9.0 and POUNCE-0.10.0 on 47 "medium size" instances, mostly with tens of thousands of variables.
- Result: SNOPT solved 30 of 47. Its scaled shifted geometric mean time was 103, the largest of the nine codes (COPT 1, KNITRO 1.17, POUNCE 5.82, UNO 11.1, IPOPT 11.6, WORHP 11.8, MATLAB 37.0, CONOPT 38.4). The failures are marked "t" (time limit) or "f", for example on the cont5_* control problems (90,600 variables) and on bearing_400 (160,000 variables, no constraints).
- Reading [inferred]: this is the 2002 boundary seen again 24 years later. Nothing on the page says whether second derivatives were given to the codes that accept them, and SNOPT 7.7 cannot use them, so the fairness objection of GSW15 (§3.6) applies here too.

### 3.5 Joshy & Hwang, OpenSQP (UC San Diego, MAE), Dec 2025

- A. J. Joshy & J. T. Hwang, "OpenSQP: A Reconfigurable Open-Source SQP Algorithm in Python for Nonlinear Optimization", arXiv 2512.05392 (read pp. 1–2, 10, 12–13). [observed · P]
- The result favours SNOPT on small problems: on 575 CUTEst problems with m, n ≤ 100, "OpenSQP and SNOPT achieve the highest success rate of 83.30%, resolving 479 out of 575 problems" (pp. 12–13), ahead of IPOPT's 475 (all codes on quasi-Newton Hessians). "Only SNOPT and OpenSQP, through their mechanisms for addressing infeasible subproblems, could manage such cases" (overdetermined problems, p. 13).
- The Gill protocol has been adopted: "For SNOPT and IPOPT, we adopted tolerances from the benchmarking study by Gill et al. [28]" (p. 12, where [28] is GSW15). The GSW15 argument is repeated almost word for word: "Although IP methods are generally considered more reliable … numerical studies suggest otherwise [28]." (p. 2)
- Critiques:
  - Scaling: "their efficiency deteriorates as the problem size increases, primarily due to the challenges associated with identifying the set of active constraints at the solution" (p. 1).
  - Transparency: "While numerous open-source and commercial SQP algorithms are available, their implementations lack the transparency and modularity necessary to adapt and fine-tune them for specific applications or to swap out different modules to create a new optimizer." (abstract, p. 1). SNOPT is described as "a leading commercial SQP optimizer" (p. 11).
  - An edge-case design choice: "This contrasts with SNOPT, which terminates immediately if function evaluations fail at the computed proximal point." (p. 10)
- A third-party claim that I did not check: quasi-Newton interior methods "frequently outperform their SQP counterparts when solving trajectory optimization problems starting from poor initial guesses", citing Kaneko & Martins, AIAA J. 63 (2025) 420–438, DOI 10.2514/1.J063976 (DOI verified; **not read**).

### 3.6 How the Gill group answered the benchmark verdicts

- **The limit was already written into the group's own abstract** [stated · P]: SNOPT is "best suited for problems with a moderate number of degrees of freedom (say, up to 2000)" (SIAM Rev. 2005 abstract; 01 §2.4). The SNOPT 7.5 guide (p. 1) says: "On large problems, SNOPT is most efficient if only some of the variables enter nonlinearly, or there are relatively few degrees of freedom at a solution (i.e., many constraints are active)." On p. 4 it adds: "However, unlike previous versions of SNOPT, there is no limit on the number of degrees of freedom." The guide recommends the CG QP solver "for problems with large numbers of degrees of freedom (say, more than 2000 superbasics)" (p. 81).
- **A fairness argument, not a rebuttal of named critics** [stated · P]: GSW15 (Gill, Saunders, Wong, "On the Performance of SQP Methods for Nonlinear Optimization", 2015, DOI 10.1007/978-3-319-23699-5_5; preprint p. 3):
  - "The conventional wisdom is that when solving a general nonlinear problem “from scratch” … software based on an IP method is generally faster and more reliable than software based on an SQP method." Then: "Providing a fair comparison of SQP and IP methods is also complicated by the fact that very few SQP software packages are able to exploit the second derivatives of a problem." And: "Test results from second-derivative methods are unlikely to be representative in this case."
  - The protocol: "The tests are formulated so that the same derivative information is provided to both packages."
  - The limit was measured and conceded (p. 13): "on the 68 problems with ndf > 4000 only 24 problems are solved faster with SNOPT7."
  - The fix was named in the next sentence: "This inefficiency may be removed by using a QP solver that maintains an explicit reduced Hessian when the number of degrees of freedom is small, and uses direct factorization when the number of degrees of freedom is large." (SQIC)
  - Summary (p. 26): "Ultimately, for every problem that is best solved by an SQP code, there will likely exist another that is best solved by an IP code."
- **No named reply** [practice · P]: GSW15's bibliography (as extracted) cites Dolan & Moré only for performance profiles (and the COPS memorandum). It does not cite Benson–Shanno–Vanderbei or Morales et al. The reply is addressed to the "conventional wisdom", not to named critics. [inferred]
- **Reception of the reply** [observed · P]: at least one later group adopted the GSW15 protocol and argument (OpenSQP, §3.5). Its own benchmark reproduces the GSW15 picture on small problems, where SNOPT is the most robust.

---

## 4. Rival schools' critique of the SQP programme itself (layer 1: taste)

- **KNITRO's authors (SLQP school)** [observed · P]: Byrd, Nocedal & Waltz, "Knitro: An Integrated Package for Nonlinear Optimization", in *Large-Scale Nonlinear Optimization* (2006) 35–59, DOI 10.1007/0-387-30065-1_4; preprint of July 6, 2005, p. 12: "The active-set method implemented in Knitro does not follow an SQP approach because, in our view, the cost of solving generally constrained quadratic programming subproblems imposes a limitation on the size of problems that can be solved in practice. In addition, the incorporation of second derivative information in SQP methods has proved to be difficult." They describe SNOPT neutrally (p. 2): "Snopt uses a line search approach, and in its default setting, employs quasi-Newton approximations to the Hessian."
- **Gill's side concedes both points** [stated · P]:
  - Gill & Wong, "Sequential Quadratic Programming Methods", UCSD NA-10-03 (August 2010), pp. 2–3; published in *Mixed Integer Nonlinear Programming*, IMA Vol. 154 (2012) 147–224, DOI 10.1007/978-1-4614-1927-3_6. They write: "On the negative side, it is difficult to implement SQP methods so that exact second derivatives can be used efficiently and reliably." And: "The complexity of the QP subproblem has been a major impediment to the formulation of second-derivative SQP methods". Also: "Over the years, algorithm developers have avoided this difficulty by eschewing second derivatives and by solving a convex QP subproblem defined with a positive semidefinite quasi-Newton approximate Hessian". And: "Any reliance on customized linear algebra software makes it hard to “modernize” a method to reflect new developments in software technology". And on the rival: "Broadly speaking, the advantages and disadvantages of SQP methods and interior methods complement each other."
  - The 2011 Manchester slides give the same diagnosis for why SQP research "declined" in the late 1980s and early 1990s (01 §2.5).
- **Filter school (Fletcher & Leyffer)**: "Nonlinear programming without a penalty function", Math. Program. 91 (2002) 239–269, DOI 10.1007/s101070100244. Not read, so whether it names SNOPT's merit function was not checked. Gill & Wong (NA-10-03, p. 16) list filter methods among the four developments "that, in our opinion, were influential in shaping developments in the area". [stated · P] That is recognition, not rebuttal.
- **Reading** [inferred]: in the SQP-versus-IP debate the Gill side does not defend the old design. It agrees with the rivals' diagnosis and argues about the *test conditions* (§3.6). It then spends 15 years on the conceded weaknesses: convexification, regularized QP with third-party factorizations, and SNOPT9 "Can use exact second derivative information" (UCSD page, 2026).

---

## 5. Critiques of the late programme: stabilized SQP and its globalization

- **The general critique** [observed · P, abstracts]:
  - Zhurbenko, Izmailov & Uskov, "Hybrid globalization of convergence of subspace-stabilized sequential quadratic programming method", Tambov University Reports, Ser. Natural and Technical Sciences 24 (126) (2019) 150–165, DOI 10.20310/1810-0198-2019-24-126-150-165. Abstract: "However, all attempts to globalize convergence of this method inevitably face principal difficulties related to the behavior of this method when the iterates are still relatively far from solutions. Specifically, the stabilized sequential quadratic programming method has a tendency to generate long sequences of short steps before its superlinear convergence shows up."
  - Izmailov & Solodov, TOP 2015 (DOI 10.1007/s11750-015-0372-1), abstract on stabilized SQP and the augmented Lagrangian: "However, when the starting point is far, even those algorithms do not appear to provide fully satisfactory remedies."
  - These abstracts do not name Gill. That they include the Gill–Robinson / Gill–Kungurtsev–Robinson approach is [inferred]. The basis: Zhurbenko et al. say "all attempts", and the Gill papers are the main line-search globalizations of stabilized SQP in the literature they cite (their reference lists were not read).
  - Not read (texts behind a Springer login; abstracts not deposited): Izmailov & Uskov, "Subspace-stabilized sequential quadratic programming", COAP 67 (2017) 129–154, DOI 10.1007/s10589-016-9890-5; Izmailov, Solodov & Uskov, "Combining stabilized SQP with the augmented Lagrangian algorithm", COAP 62 (2015) 405–429, DOI 10.1007/s10589-015-9744-6; and "Globalizing Stabilized Sequential Quadratic Programming Method by Smooth Primal-Dual Exact Penalty Function", JOTA 169 (2016) 148–178, DOI 10.1007/s10957-016-0889-y. Also Fernández & Solodov, "Stabilized sequential quadratic programming: a survey", Pesquisa Operacional 34 (2014) 463–479, DOI 10.1590/0101-7438.2014.034.03.0463. It is open access, but SciELO served a bot challenge (HTTP 403) and the CONICET repository copy failed. **Not read.**
- **The Gill side's counter-critique** [stated · P]: Gill, Kungurtsev & Robinson, CCoM-13-4 (rev. June 23, 2015), pp. 2–3; journal version IMA J. Numer. Anal. 37 (2017) 407–443, DOI 10.1093/imanum/drw004.
  - They grant the rivals' premise: "The first is that stabilized SQP methods have no global convergence theory." And, as a consequence: "This strategy may require several switches between a conventional and a stabilized SQP method before the neighborhood of a solution is identified correctly."
  - They criticise the rivals' assumptions: "When establishing the local convergence rate of stabilized SQP methods, the potential nonconvexity of the QP subproblem implies that assumptions must be made regarding which solution of (1.1) is found. For example, some analyses require a global solution of (1.1) (see, e.g., [24,25]), or require that the “same” local solution is found at each step." Here [24] and [25] are the two Izmailov–Solodov–Uskov papers above.
  - They state their own claim: "It is not necessary to solve a nonconvex QP subproblem, and no assumptions are necessary about the quality of each subproblem solution." and "while being able to transition seamlessly to stabilized SQP with fast local convergence in the neighborhood of a solution."
- **Self-pruned claim in the same line** [practice · P, via 03 §3.5]: the 2011 preprint (Gill & Robinson, "Regularized Sequential Quadratic Programming", UCSD NA-11-02) said that "Preliminary numerical experiments on a subset of problems from the CUTEr test collection indicate that the proposed SQP method is significantly more efficient than our current SQP package SNOPT." The 2013 SIOPT version (DOI 10.1137/120882913) claims only robustness. No reason is given (03 Gaps). This is the only dropped performance claim found in the Gill record.
- **Reception** [practice · P, 01 §2.5]: the six core papers of the line have modest citation counts in OpenAlex (94, 50, 52, 29, 14 and 3). I found no published replication of the Gill–Robinson / Gill–Kungurtsev–Robinson methods by another group. None of the external benchmarks found in §3 includes their MATLAB codes.

---

## 6. Reception of the 1985–86 Karmarkar equivalence (a result that met resistance)

- **The oral reception** [observed · P for Wright's first-hand account; auto-captions, so wording approximate]: the 2019 INFORMS interview with Margaret Wright, transcript lines 283–287. After her 1985 ISMP talk presenting the equivalence theorem and numbers: "this pretty well-known person who's a friend of mine came up to me and said this is terrible this is terrible … he said this can't be right this can't be right and I said it's a theorem you saw the proof". Her explanation: "people who had thought this was a fundamental breakthrough never seen before on the planet were upset because if you say this is a barrier method from the late sixties look at the fiat code [Fiacco and] McCormick book it kind of shatters that idea".
- **The written reception** [observed · S]: zbMATH review Zbl 0624.90062 (reviewer B. Strazicky) of Gill, Murray, Saunders, Tomlin & Wright, Math. Program. 36 (1986) 183–209, DOI 10.1007/BF02592025. It is descriptive: "It turns out that if both of these methods are applied to the same problem using the same initial point, then by using special parameter values in the barrier method one can achieve that the iterates are identical. … Conclusions pro and contra the barrier method are also discussed." The paper itself was not read.
- **Reading** [inferred]: the resistance was to what the result meant, not to its correctness ("it's a theorem"). No published technical rebuttal of the equivalence was found. The critic is unnamed in the interview, and I did not try to identify him.

---

## 7. Predictions and self-announcements that did not come true (layer 5)

| Announcement | Source | What happened | Tag |
|---|---|---|---|
| SNOPT9, "the forthcoming SNOPT9" with second derivatives | GSW15, preprint p. 26 (2015) | UCSD SNOPT page, fetched 2026-09-28: "SNOPT 9 Currently in development Simplified user interface Can use exact second derivative information Updated QP subproblem solver SQIC Written in Fortran 2003". Public downloads offer SNOPT7 only (01 §2.5). | practice · P |
| EXPAND as an "anti-cycling procedure" | 1989 title; SNOPT 7.5 guide p. 72 | Counterexamples (§1.1). The claim was restated as "no guarantee … the probability is very small" (2014, 2016). | practice · P + observed · P |
| Regularized SQP "significantly more efficient than … SNOPT" | NA-11-02 (2011), via 03 §3.5 | Dropped in the 2013 journal version. | practice · P |
| Moderate degrees of freedom "(say, up to 2000)" as a design limit | SIOPT 2002 / SIAM Rev. 2005 abstracts | Limit removed in the 7.5 guide ("no limit on the number of degrees of freedom"). External benchmarks up to 2026 still show slowdowns on problems with many degrees of freedom (§3). | practice · P + observed · P |
| A Gill–Wright book "Computational Optimization: Nonlinear Programming (to be published in 2025)" | OpenSQP reference 30 (a third party citing it) | Not found in Crossref on 2026-09-28. The source is only a citation by others, so this is a lead, not a missed prediction (Gaps). | observed · S |

---

## 8. Public reviews (layers 1 and 6)

- **Book reviews found (metadata verified; texts not read: JSTOR, Wiley, SIAM and T&F require access)**:
  - *Practical Optimization* (1981): Engineering Optimization 6(2) (1982) 113–114, DOI 10.1080/03052158208928041 (unsigned). The Mathematical Gazette 66(437) (1982) 252–253, DOI 10.2307/3616583 (Cobb). Int. J. Numer. Methods Eng. 18(6) (1982) 954, DOI 10.1002/nme.1620180612 (Ricketts). SIAM Review 25(2) (1983) 283–284, DOI 10.1137/1025065 (J. S. Kowalik).
  - *Numerical Linear Algebra and Optimization, Vol. 1* (1991): SIAM Review 35(1) (1993) 155–158, DOI 10.1137/1035028 (Kowalik & Zikan). Networks 24(2) (1994) 128–129, DOI 10.1002/net.3230240218 (Fang & Puthenpura).
  - What these reviews criticise is **not known** (not read).
- **zbMATH reviews** (public, read) [observed · S]: SNOPT SIOPT 2002 (Zbl 1027.90111), reviewed by K. Schittkowski, author of the rival SQP code NLPQL. The review restates the abstract ("designed for problems with many thousands of constraints and variables but a moderate number of degrees of freedom (say, up to 2000)") and contains no criticism. EXPAND 1989 (Zbl 0688.90038) and the Karmarkar equivalence (Zbl 0624.90062) are covered in §1.1 and §6. Schnabel & Eskow 1990 (Zbl 0716.65023, N. Vulchanov) restates the smaller-bound claim.
- **Referee reports, rebuttal letters**: none public. The only visible trace of refereeing is an acknowledgement (PDB 2020: "three referees for constructive comments that significantly improved the presentation", 03 §3.5), and the almost three-year review of the SNOPT paper (01 §2.4).

---

## 9. Patterns in how the group meets critique (candidate items for Phase 2; all [inferred], each from ≥ 2 items above)

1. **Concede the limit in print before the critics do, then turn it into the agenda.**
   - Evidence: the "(say, up to 2000)" limit in the 2002/2005 abstracts, then SQIC and the CG QP solver.
   - The "major impediment" of second derivatives (2010), then convexification and SNOPT9.
   - The stabilized-SQP "no global convergence theory" (2013/2015), then the primal-dual augmented Lagrangian globalization.
2. **Contest the test protocol rather than the verdict.** Evidence: GSW15's "same derivative information" and the ndf-stratified analysis. The conventional wisdom is called "more nuanced", not wrong. External benchmarks give second derivatives to the interior codes (§3.2–3.4).
3. **Absorb a rival's diagnosis as motivation.** Evidence: Izmailov & Solodov's critical-multiplier result is cited as the reason for stabilized SQP, and the rivals' degenerate test sets are reused (§1.3). Wächter & Biegler's counterexample is presented in the group's own survey and their inertia-correction algorithm is adopted in PDB (§1.2).
4. **Downgrade a guarantee instead of retracting it, and cite the critic.** Evidence: EXPAND (§1.1). No erratum or retraction exists anywhere in the record (01 §3).
5. **Counter-critique the rival's assumptions.** Evidence: GKR on "a global solution of (1.1)" (§5). Also GSW15 on second-derivative test environments being "unlikely to be representative" (§3.6).
6. **Leave some critiques unanswered.** Evidence: the modified-Cholesky bound (§2). Also Morales et al. on convergence theory (§3.3), and Benson–Shanno–Vanderbei by name.

---

## 10. Era and resource context of the critiques

| Critique | When / setting | Resource context that limits how far it transfers |
|---|---|---|
| Schnabel & Eskow; Cheng & Higham | 1990–1999, dense matrices | Worst-case bounds and dense tests; not tied to SNOPT's sparse setting |
| Hall & McKinnon | 1996–2004, LP simplex codes | Exact-degeneracy LP examples; MINOS 5.4 without preprocessing; modern presolve changes the practical risk (not tested) |
| Dolan & Moré; Benson–Shanno–Vanderbei; Morales et al. | 2000–2003, Sun workstations, AMPL | SNOPT 5.3/6.x with a superbasics limit that had to be raised; rivals given AMPL second derivatives; SNOPT had no second-derivative option then |
| Izmailov & Solodov | 2008–2011 | AMPL student-edition SNOPT at defaults; small degenerate academic problems |
| Wächter & Biegler | 2000 | One-dimensional analytic example; applies to a class of barrier-SQP methods |
| Mittelmann | 2026, 12-core Ryzen, 2 h limit | SNOPT 7.7 (first derivatives only) against codes that can use second derivatives; "medium size" = up to about 260,000 variables |
| OpenSQP | 2025, MacBook Pro i5 (p. 11) | CUTEst problems with m, n ≤ 100, 250-iteration cap; memory raised to mimic full BFGS |

---

## Contradictions (kept, not reconciled)

1. **What Hall & McKinnon showed about EXPAND.**
   - Critics: "there is a positive probability of encountering cycling in randomly generated degenerate examples. In practice therefore the expand procedure cannot be relied upon to prevent cycling." (arXiv p. 19)
   - Gill group, citing the same paper: "Although there is no guarantee of preventing cycling, the probability is very small (see Hall and McKinnon [11])." (SQOPT 7.5 guide p. 11; the same sentence in CCoM 13-1 p. 27)
   - The critics call cycling examples in general "very rare in practice" (p. 1). They do not say this of EXPAND on degenerate problems.
2. **SNOPT's convergence theory.**
   - Morales et al.: "Global convergence results are difficult to establish for SNOPT" (p. 5).
   - Gill, Murray, Saunders & Wright, SOL 86-6R (abstract, read by agent 01): "Global convergence is proved for an SQP algorithm that uses this merit function." That proof covers a simplified NPSQP ("use of a single penalty parameter, and strengthened assumptions", §1).
   - The SNOPT paper claims the "favorable theoretical properties of the NPSOL algorithm" (SIAM Rev. 2005, p. 101).
3. **Is SNOPT competitive?** The verdicts depend on the test set and the derivatives given, and they point in different directions:
   - "a quasi-Newton method is not competitive with a Newton approach" when the degrees of freedom are many (Benson et al. p. 22).
   - "SNOPT performs quite well … This is remarkable" on general constraints (Morales et al. p. 13).
   - "over 90% of this COPS subset" (Dolan & Moré p. 8).
   - 30 of 47 and the slowest geometric mean (Mittelmann 2026).
   - Joint-highest success rate on small CUTEst (OpenSQP 2025).
   - "in some situations, quasi-Newton SQP methods are more efficient than interior methods that utilize the exact Hessian" (GSW15 abstract).
4. **Degrees of freedom, in the same manual.** The SNOPT 7.5 guide says "no limit on the number of degrees of freedom" (p. 4). It also says SNOPT is "most efficient if … there are relatively few degrees of freedom" (pp. 1, 4) and reserves the CG solver for "more than 2000 superbasics" (p. 81).
5. **Modified Cholesky.** Schnabel & Eskow 1990 say their method "virtually always produces smaller values" of the perturbation than the Gill–Murray method. Schnabel & Eskow 1999 report user cases where their 1990 method "makes a far larger modification … than is made by the Gill--Murray--Wright method".
6. **Stabilized-SQP globalization.** Zhurbenko–Izmailov–Uskov (2019): "all attempts to globalize convergence of this method inevitably face principal difficulties". Gill–Kungurtsev–Robinson (2015 revision): the method is able "to transition seamlessly to stabilized SQP". Each side says the other's analysis needs assumptions (global QP solutions, or a switch from conventional SQP).

## Gaps (searched or looked for, not found or not accessible)

- **Stabilized-SQP critiques in full**:
  - Fernández & Solodov 2014 survey: SciELO returned a bot challenge (403), and the CONICET handle failed.
  - Izmailov–Uskov 2017 and Izmailov–Solodov–Uskov 2015/2016: Springer redirects to a login, no abstract is deposited, and no author copy was found.
  - Whether these texts name the Gill–Robinson / Gill–Kungurtsev–Robinson methods is unknown.
- **Wächter & Biegler 2000**: not read. Whether Forsgren–Gill 1998 is in the failing class was not determined.
- **Filter school's critique of merit and penalty functions** (Fletcher & Leyffer 2002): not read. The abstract is not deposited.
- **Modified Cholesky**: Fang & O'Leary 2008 not read (UMD 403). The Cheng & Higham full text was not read (Manchester 503). GMW81 itself (in *Practical Optimization*) was not read.
- **The EXPAND paper (1989) and the Karmarkar-equivalence paper (1986)**: not read (Springer paywall), so the original claims are known only from the critics and reviewers.
- **Six book reviews** (§8): content not read.
- **Trajectory-optimization community** (Betts; Kaneko & Martins 2025): the abstracts are not deposited, and the Kaneko & Martins claim reported by OpenSQP is unverified. Agamawi & Rao (arXiv 1905.12745) was checked and mentions SNOPT only descriptively.
- **Direct replies**: I found no paper, note or talk in which the Gill group names Benson–Shanno–Vanderbei or Morales et al. and answers them. There is no public correspondence with Hall & McKinnon beyond the two citations.
- **Mittelmann archives**: earlier versions of the NLP benchmark with SNOPT (for a time series) were not checked.
- **Critiques of LUSOL / factorization updating, and of the NPSOL/SNOPT merit-function parameter choices**: not searched (time).
- **Gill–Wright forthcoming book** ("to be published in 2025", cited by OpenSQP): not found in Crossref. Status unknown.
- **Systematic citation scan**: done only for Gill & Robinson 2013 (OpenAlex "cites" filter, 50 citing works; abstracts screened). OpenAlex rate-limited (HTTP 429) repeated calls, and the arXiv API returned HTTP 406, so there was no systematic scan for comments or replies on the other key papers.
- **Rejected papers, referee reports, rebuttals**: none public.

## Sources

1. J. A. J. Hall, K. I. M. McKinnon, "The simplest examples where the simplex method cycles and conditions where EXPAND fails to prevent cycling", Math. Program. 100(1) (2004) 133–150, DOI 10.1007/s10107-003-0488-1; arXiv math/0012242 v1 (2000-12-22), read in full — primary (critic)
2. P. E. Gill, W. Murray, M. A. Saunders, M. H. Wright, "A practical anti-cycling procedure for linearly constrained optimization", Math. Program. 45 (1989) 437–474, DOI 10.1007/BF01589114 — primary metadata (not read)
3. zbMATH Open reviews: Zbl 0688.90038 (X.-S. Zhang), Zbl 0624.90062 (B. Strazicky), Zbl 1027.90111 (K. Schittkowski), Zbl 0716.65023 (N. Vulchanov), fetched 2026-09-28, https://zbmath.org/ — secondary (public reviews)
4. P. E. Gill, W. Murray, M. A. Saunders, E. Wong, "User's Guide for SQOPT Version 7.5", CCoM, February 8, 2016, http://www.ccom.ucsd.edu/~peg/papers/sqdoc7.pdf (p. 11) — primary
5. P. E. Gill, E. Wong, "Methods for Convex and General Quadratic Programming", CCoM 13-1 (June 30, 2014), http://www.ccom.ucsd.edu/~peg/papers/gqp.pdf (p. 27); journal Math. Program. Comput. 7 (2015) 71–112, DOI 10.1007/s12532-014-0075-x — primary
6. P. E. Gill, W. Murray, M. A. Saunders, E. Wong, "User's Guide for SNOPT Version 7.5", http://www.ccom.ucsd.edu/~peg/papers/sndoc7.pdf (pp. 1, 4, 9, 72, 81) — primary
7. R. B. Schnabel, E. Eskow, "A New Modified Cholesky Factorization", SIAM J. Sci. Stat. Comput. 11 (1990) 1136–1158, DOI 10.1137/0911064 (abstract via OpenAlex) — primary (critic, abstract only)
8. R. B. Schnabel, E. Eskow, "A Revised Modified Cholesky Factorization Algorithm", SIAM J. Optim. 9 (1999) 1135–1148, DOI 10.1137/S105262349833266X (abstract via Crossref) — primary (critic, abstract only)
9. S. H. Cheng, N. J. Higham, "A Modified Cholesky Algorithm Based on a Symmetric Indefinite Factorization", SIAM J. Matrix Anal. Appl. 19 (1998) 1097–1110, DOI 10.1137/S0895479896302898 (abstract via OpenAlex) — primary (abstract only)
10. H.-r. Fang, D. P. O'Leary, "Modified Cholesky algorithms: a catalog with new approaches", Math. Program. 115 (2008) 319–349, DOI 10.1007/s10107-007-0177-6 — metadata only (not read)
11. A. Forsgren, P. E. Gill, W. Murray, "Computing Modified Newton Directions Using a Partial Cholesky Factorization", SIAM J. Sci. Comput. 16 (1995) 139–150, DOI 10.1137/0916009 (abstract via OpenAlex) — primary (abstract only)
12. E. D. Dolan, J. J. Moré, "Benchmarking optimization software with performance profiles", Math. Program. 91 (2002) 201–213, DOI 10.1007/s101070100263; arXiv cs/0102001 (pp. 6–10 read) — primary (third-party benchmark)
13. H. Y. Benson, D. F. Shanno, R. J. Vanderbei, "A Comparative Study of Large-Scale Nonlinear Optimization Algorithms", ORFE-01-04 rev. July 17, 2002, https://vanderbei.princeton.edu/tex/loqo5/loqo5_5.pdf; in *High Performance Algorithms and Software for Nonlinear Optimization* (2003) 95–127, DOI 10.1007/978-1-4613-0241-4_5 — primary (rival benchmark)
14. J. L. Morales, J. Nocedal, R. A. Waltz, G. Liu, J.-P. Goux, "Assessing the Potential of Interior Methods for Nonlinear Optimization", LNCSE 30 (2003) 167–183, DOI 10.1007/978-3-642-55508-4_10; preprint http://users.iems.northwestern.edu/~nocedal/PDFfiles/assessment.pdf (damaged text layer) — primary (rival benchmark)
15. R. H. Byrd, J. Nocedal, R. A. Waltz, "Knitro: An Integrated Package for Nonlinear Optimization", in *Large-Scale Nonlinear Optimization* (2006) 35–59, DOI 10.1007/0-387-30065-1_4; preprint July 6, 2005, http://users.iems.northwestern.edu/~nocedal/PDFfiles/integrated.pdf (pp. 1–2, 12) — primary (rival school)
16. H. D. Mittelmann, "AMPL-NLP Benchmark", page dated 9 Sep 2026, https://plato.asu.edu/ftp/ampl-nlp.html, fetched 2026-09-28 — primary (third-party benchmark data)
17. A. J. Joshy, J. T. Hwang, "OpenSQP: A Reconfigurable Open-Source SQP Algorithm in Python for Nonlinear Optimization", arXiv 2512.05392 (Dec 2025), pp. 1–2, 10–13 read — primary (third-party benchmark)
18. S. Kaneko, J. R. R. A. Martins, "Simultaneous Design and Trajectory Optimization Strategies for Computationally Expensive Models", AIAA J. 63 (2025) 420–438, DOI 10.2514/1.J063976 — metadata only (not read; cited by 17)
19. Y. M. Agamawi, A. V. Rao, "Comparison of Derivative Estimation Methods in Solving Optimal Control Problems Using Direct Collocation", arXiv 1905.12745; journal version "Comparison of Derivative Estimation Methods in Optimal Control Using Direct Collocation", AIAA J. 58 (2020) 341–354, DOI 10.2514/1.J058514 (Crossref-verified) — checked; no critique of SNOPT found (secondary for this file)
20. P. E. Gill, M. A. Saunders, E. Wong, "On the Performance of SQP Methods for Nonlinear Optimization", in *Modeling and Optimization: Theory and Applications* (2015) 95–123, DOI 10.1007/978-3-319-23699-5_5; preprint http://www.ccom.ucsd.edu/~peg/papers/mopta.pdf (pp. 1, 3, 13, 26) — primary
21. P. E. Gill, E. Wong, "Sequential Quadratic Programming Methods", UCSD NA-10-03 (August 2010), http://www.ccom.ucsd.edu/~peg/papers/sqpReview.pdf (pp. 2–3, 16); in *Mixed Integer Nonlinear Programming* (2012) 147–224, DOI 10.1007/978-1-4614-1927-3_6 — primary
22. A. Forsgren, P. E. Gill, M. H. Wright, "Interior Methods for Nonlinear Optimization", SIAM Rev. 44 (2002) 525–597, DOI 10.1137/S0036144502414942 (journal pp. 588–590 read) — primary
23. A. Wächter, L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", Math. Program. 88 (2000) 565–574, DOI 10.1007/PL00011386 — metadata only (not read)
24. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization", SIOPT 30 (2020) 1067–1093, DOI 10.1137/19M1247425; http://www.ccom.ucsd.edu/~peg/papers/pdb.pdf (PDF p. 23) — primary
25. A. F. Izmailov, M. V. Solodov, "On attraction of linearly constrained Lagrangian methods and of stabilized and quasi-Newton SQP methods to critical multipliers", Math. Program. 126 (2011) 231–257, DOI 10.1007/s10107-009-0279-4; author copy http://www.cs.wisc.edu/~solodov/izmsol08iSQP.pdf — primary (critic)
26. A. F. Izmailov, M. V. Solodov, "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23 (2015) 1–26, DOI 10.1007/s11750-015-0372-1; abstract via https://ideas.repec.org/a/spr/topjnl/v23y2015i1p1-26.html — primary (abstract only)
27. N. G. Zhurbenko, A. F. Izmailov, E. I. Uskov, "Hybrid globalization of convergence of subspace-stabilized sequential quadratic programming method", Tambov University Reports 24 (126) (2019) 150–165, DOI 10.20310/1810-0198-2019-24-126-150-165 (abstract via OpenAlex) — primary (abstract only)
28. A. F. Izmailov, E. I. Uskov, "Subspace-stabilized sequential quadratic programming", COAP 67 (2017) 129–154, DOI 10.1007/s10589-016-9890-5 — metadata only (not read)
29. A. F. Izmailov, M. V. Solodov, E. I. Uskov, "Combining stabilized SQP with the augmented Lagrangian algorithm", COAP 62 (2015) 405–429, DOI 10.1007/s10589-015-9744-6 — metadata only (not read)
30. A. F. Izmailov, M. V. Solodov, E. I. Uskov, "Globalizing Stabilized Sequential Quadratic Programming Method by Smooth Primal-Dual Exact Penalty Function", JOTA 169 (2016) 148–178, DOI 10.1007/s10957-016-0889-y — metadata only (not read)
31. D. Fernández, M. V. Solodov, "Stabilized sequential quadratic programming: a survey", Pesquisa Operacional 34 (2014) 463–479, DOI 10.1590/0101-7438.2014.034.03.0463 — metadata only (open access, but access blocked; not read)
32. P. E. Gill, V. Kungurtsev, D. P. Robinson, "A Stabilized SQP Method: Global Convergence", CCoM-13-4 (Oct 31, 2013, rev. June 23, 2015), https://ccom.ucsd.edu/reports/UCSD-CCoM-13-04.pdf (pp. 1–3); IMA J. Numer. Anal. 37 (2017) 407–443, DOI 10.1093/imanum/drw004 — primary
33. P. E. Gill, D. P. Robinson, "A Globally Convergent Stabilized SQP Method", SIOPT 23 (2013) 1983–2010, DOI 10.1137/120882913, and its 2011 preprint UCSD NA-11-02 — primary (used via 03 §3.5)
34. P. E. Gill, W. Murray, M. A. Saunders, M. H. Wright, "Some Theoretical Properties of an Augmented Lagrangian Merit Function", SOL 86-6R (1986), https://ccom.ucsd.edu/~peg/papers/merit.pdf (abstract and §1) — primary
35. P. E. Gill, W. Murray, M. A. Saunders, "SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization", SIOPT 12 (2002) 979–1006, DOI 10.1137/S1052623499350013, and SIAM Rev. 47 (2005) 99–131, DOI 10.1137/S0036144504446096 — primary (via 01 §2.4)
36. P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, M. H. Wright, "On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method", Math. Program. 36 (1986) 183–209, DOI 10.1007/BF02592025 — metadata only (not read)
37. UCSD Optimization Software, SNOPT page, https://ccom.ucsd.edu/~optimizers/solvers/snopt/, fetched 2026-09-28 — primary
38. INFORMS History & Traditions Interview with Margaret Wright, 2019-11-18, https://www.youtube.com/watch?v=2L5nQIvTohk; auto-caption transcript at `references/sources/talks/2019-informs-margaret-wright-interview-autocaptions.txt` (lines 283–287) — primary for Wright's account, [observed] for Gill
39. Book reviews of *Practical Optimization*: Engineering Optimization 6(2) (1982) 113–114, DOI 10.1080/03052158208928041; Math. Gazette 66 (1982) 252–253, DOI 10.2307/3616583; IJNME 18 (1982) 954, DOI 10.1002/nme.1620180612; SIAM Rev. 25 (1983) 283–284, DOI 10.1137/1025065 — metadata only (not read)
40. Book reviews of *Numerical Linear Algebra and Optimization, Vol. 1*: SIAM Rev. 35 (1993) 155–158, DOI 10.1137/1035028; Networks 24 (1994) 128–129, DOI 10.1002/net.3230240218 — metadata only (not read)
41. Crossref REST API (DOI metadata and deposited abstracts), queried 2026-09-28, https://api.crossref.org/ — secondary (bibliographic)
42. OpenAlex API (abstracts; the citing-works scan of W2027507632), queried 2026-09-28, https://api.openalex.org/ — secondary (aggregator)
43. Semantic Scholar Graph API (open-access locations), queried 2026-09-28 — secondary (aggregator)
44. Research notes 01-publications.md and 03-process-evidence.md in this folder (for the 2011 dropped claim, the reception counts and the SNOPT limits) — secondary (internal)
