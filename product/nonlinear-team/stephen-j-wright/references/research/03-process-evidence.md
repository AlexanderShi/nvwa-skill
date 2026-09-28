# Stephen J. Wright: Process Evidence (what he actually does)

| Field | Value |
|---|---|
| Researcher | Stephen J. Wright (UW-Madison Computer Sciences since 2001; Argonne MCS 1990–2001; living) |
| Dimension | Research agent 03 of 06: process evidence. Sources are code and changelogs, experiment sections, arXiv early-versus-final versions, errata and corrigenda, public reviews and rebuttals, and abandoned or unpublished work |
| Research date | 2026-09-28 |
| Sources consulted | 58 (47 primary, 11 secondary), listed under "Sources". Blocked attempts: the OpenReview forum (browser challenge), the OpenReview API (login required), github.com HTML and the REST API (403 through the proxy), and the Wayback Machine (egress policy) |
| WebSearch calls | 1 of 2 allowed |
| User-supplied material | None. `references/sources/{papers,essays,software}/` held only `.gitkeep`. `talks/` holds the oral-history transcript that research agent 02 saved from the public UW archive; it is not user-supplied. `private/` was not opened. Nothing below is marked "from user-supplied material" |
| Transcripts saved | None in this pass |
| Language | English (per team.json) |

**Tags.** [stated] means Wright wrote or said it, in paper prose, a README, a changelog, a rebuttal or an interview. [practice] means the artifact itself shows what was done: code, file dates, tables, the design of the tests, or what changed between versions. [observed] means a third party recorded it (reviewers, a student's errata, an editorial board). [inferred] is my reading of the evidence; the basis is always given, and an inferred item must never be quoted as Wright's view. (P) marks a primary source and (S) a secondary one.

**Quoting conventions.**
- Quotes are verbatim.
- Four texts were extracted from dvips PostScript or PDFs built from it: P485 corrigenda, P664 errata, the PCx User Guide and P600. In those I only rejoined letter-spaced words and restored dropped fi/ff ligatures. Such quotes are marked "(spacing normalized)".
- Where a PDF lost a symbol-font word, I restore it in square brackets, for example [l1_ls].
- Page locators are PDF pages of the file named in Sources.

**Scope note.** Agent 01 (`01-publications.md`) already covers the publication landscape and the anatomy of the signature works, and agent 02 (`02-methodology.md`) covers stated method. This file adds behaviour. Where a finding sharpens or contradicts 01/02, it says so.

---

## 0. Artifact timeline (the backbone of the evidence)

All dates come from the artifacts themselves: the papers page, changelogs, arXiv submission histories, file dates inside code archives, and GitHub metadata. All entries are [practice, P] unless marked.

| Date | Artifact | What it shows |
|---|---|---|
| Dec 1994 → rev. May 1998 → MP 84 (1999) → corrigenda 22 Sep 2000 | Wright & Jarre, "The role of linear objective functions in barrier methods", 10.1007/s101070050026 (preprint MCS-P485-1294) | A 4-year revision cycle, then a self-published corrigendum that completes a proof (§2.1) |
| 15 May 1996 → 18 Oct 1996 → 7 Mar 1997 → 2 Nov 1997 | PCx beta-1.0, beta-2.0, 1.0, 1.1 (changelog) | Release first, then add robustness features release by release (§1.4) |
| May 1996 → rev. May 1998 and Dec 1998 → SIOPT 9 (1999) | "Modified Cholesky factorizations in interior-point algorithms for linear programming", 10.1137/S1052623496304712 (P600) | Linear-algebra theory tested in a toy IPM and inserted into PCx (§1.1) |
| Feb 1997 → COAP 11 (1998) | Stabilized SQP, 10.1023/A:1018665102534 (P643) | Counterexample-first (01, S2) |
| Oct 1997 → SIOPT 13 (2002) | "Modifying SQP for degenerate problems", 10.1137/S1052623498333731 (P699) | A theorem written to explain an earlier computational observation (§1.1) |
| 1997 → errata "last updated December 12, 1999" | *Primal-Dual Interior-Point Methods*, 10.1137/1.9781611971453 | 43 corrections, including 3 repaired proofs and one retracted overclaim (§2.1) |
| Jan 1998 → rev. May 2000 → SIOPT 12 (2001); arXiv math/0103102 (Mar 2001) | "Effects of finite-precision arithmetic on interior-point methods for nonlinear programming", 10.1137/S1052623498347438 (P705) | A 2-variable MATLAB example, then a perturbed example chosen to break the favourable case (§1.1) |
| 8 Aug 2000 | JOTA errata by Matthew J. Tenny for Rao, Wright & Rawlings (1998), 10.1023/A:1021711402723 | A student reimplementing the method found the equation errors; Wright posts the errata "courtesy of Matt Tenny" (§2.1) |
| Mar 2000 → rev. May 2001 → SIOPT 12 (2002) | Yıldırım & Wright, warm-start IPMs, 10.1137/S1052623400369235 | Numerical section added at the referees' prompting (§2.2) |
| Dec 2000 → rev. Dec 2001 → MP 95 (2003) | "Constraint identification and algorithm stabilization for degenerate nonlinear programs", 10.1007/s10107-002-0344-8, arXiv math/0012209 | Test protocol borrowed from the competing paper; failures tabulated (§1.2) |
| 1999–2001 (metaNEOS) → COAP 24 (2003) → Best Paper note, COAP 29 (2004) | Linderoth & Wright, "Decomposition algorithms for stochastic programming on a computational grid", 10.1023/A:1021858008222 | A new tool (MW on Condor) driven by a chosen application; folklore tested (§1.3) |
| Oct 2001 user guide → TOMS 29 (2003) → 0.99.27 (2 Oct 2016); GitHub `emgertz/OOQP` since 2012 | OOQP, 10.1145/641876.641880 | Changelog driven by user problems; the co-author maintains the code in later years (§1.4) |
| Jan 2002 → rev. Oct 2002 → Ann. OR 142 (2006) | Linderoth, Shapiro & Wright, "The empirical behavior of sampling methods for stochastic programming", 10.1007/s10479-006-6169-8, with a companion data site | Data released in SMPS format; a promise of more detail was never fulfilled (§1.5) |
| 2004 | Wright & Tenny SIOPT 14, 10.1137/S1052623402413227 (theory) + Tenny, Wright & Rawlings COAP 28, 10.1023/B:COAP.0000018880.63497.EB (application) | Theory and computation split into companion papers (§3) |
| 2005 | "An algorithm for degenerate nonlinear programming with rapid local convergence", SIOPT 15, 10.1137/030601235 | "Simulated roundoff" experiment (§1.1) |
| 2006 | Oberlin & Wright, "Active set identification in nonlinear programming", SIOPT 17, 10.1137/050626776 | The degenerate-NLP line's only large computational study: C + CPLEX 9.0 on a degenerate CUTEr subset (§1.2) |
| Jun 2007 → Jan 2009; SpaRSA 2.0 of 20 Jan 2009 | GPSR (JSTSP 2007, 10.1109/JSTSP.2007.910281) and SpaRSA (TSP 2009, 10.1109/TSP.2009.2016892) codes | Equal-objective benchmarking; an own-paper error corrected in the follow-up paper (§1.2, §2.1) |
| May 2008 → 14 Oct 2008 | TVGP v1 → v2.0 (Zhu, Wright & Chan, COAP 47 (2010), 10.1007/s10589-008-9225-2) | Convergence criteria made consistent across algorithms in a second release (§1.4) |
| Sep 2008 | Lee & Wright GPU technical report | "submitted, 2008"; no publication record found (§4) |
| Dec 2008 arXiv v1 (34 KB) → Apr 2015 v2 (118 KB) → MP 158 (2016) | Lewis & Wright, "A proximal method for composite minimization", 10.1007/s10107-015-0943-9, arXiv:0812.0423 | Computations added in the 6-year revision (§2.2) |
| Feb 2010 | Lee & Wright, "Sparse nonlinear support vector machines via stochastic approximation" | Submitted; the entry is now commented out of the papers page; no publication found (§4) |
| Apr 2010 → Sep 2011 | LPS v1.0 → v2.2, tied to "Accelerated block-coordinate relaxation…", SIOPT 22 (2012), 10.1137/100808563 | Script that reproduces the paper's tables; code released alongside the paper revision (§1.5) |
| Sep 2010 → ICPRAM 2012 | ASSET, drafted in the IEEE TPAMI template; published as 10.5220/0003786202230228 and arXiv:1111.0432 | Ended at a minor venue (§4) |
| Jun 2011 | Hogwild! TR / arXiv:1106.5730 (NIPS 2011) | Fairness device: the competitor was hand-coded and optimized (§1.2) |
| 2013, 2014 | NIPS reviews and author feedback (Sridhar et al. 2013; Lim & Wright 2014) | How criticism was answered (§2.3) |
| Feb 2015 | "Coordinate descent algorithms", arXiv:1502.04759, MP 151, 10.1007/s10107-015-0892-3 | Synthetic test family tuned to the constants in the theory (§1.1) |
| Jul 2016 → Jun 2018 (v5); Jun 2017 → Jan 2020 (v4) | Lee & Wright, IMA JNA 39 (2019), 10.1093/imanum/dry040; Wright & Lee, Math. Comp. 89 (2020), 10.1090/mcom/3530 | Observed "stressed" cases turned into analysis papers (§3) |
| Jun 2017 → Oct 2018 | O'Neill & Wright, MP 176 (2019), 10.1007/s10107-018-1340-y, arXiv:1706.07993 | Claim softened in revision (§2.2) |
| Jul 2019 v1 → Sep 2020 v4 | Xie & Wright, J. Sci. Comput. 86 (2021), 10.1007/s10915-021-01409-y, arXiv:1908.00131 | Numerical section removed and more theory added (§2.2) |
| Dec 2019 → Nov 2020 | Curtis, Robinson, Royer & Wright, SIOPT 31 (2021), 10.1137/19M130563X, arXiv:1912.04365 | CUTEst ablation of the complexity safeguards (§1.2) |
| Mar 2021 v1 → Jun 2023 v3 | Xie & Wright, MP 207 (2024), 10.1007/s10107-023-02000-z, arXiv:2103.15989 | A whole method (scaled two-metric projection) dropped in revision (§2.2) |
| Jun 2022; typos of 31 Jan 2023 | GitHub `wrightstephen/OptimizationForDataAnalysis` (typo list for 10.1017/9781009004282) | Errata kept up for the third book (§2.1) |
| 18 Jul 2022 | GitHub `wrightstephen/NumericalOptimization3rdEdition` | README promises chapter drafts; the repository is empty (§4) |
| Oct 2023 → SIOPT 35 (2025) | Ding & Wright, "On squared-variable formulations", 10.1137/23M1608343, arXiv:2310.01784 | PCx "resuscitated" 26 years on, to presolve Netlib (§1.2) |
| Oct 2025 v1 → Dec 2025 v2 | Wright, "Optimization in theory and practice", arXiv:2510.15734 | Precision and hedging edits (§2.2) |
| Feb 2026 | Lee & Wright, arXiv:2602.10470 | Return to degenerate superlinear convergence; theory only (§4) |

---

## 1. Layer 4: experiments and execution (the bulk of the evidence)

### 1.1 The signature move: a tiny example built to test whether a theorem shows up in floating point

In 1996–2006 almost every NLP or IPM theory paper Wright wrote alone ends with a small, hand-built experiment. The experiment is usually in MATLAB, uses 2 to 12 variables, and is designed to check a specific prediction of the analysis, not to benchmark. [practice, P]

| Paper | Experiment | Verbatim evidence |
|---|---|---|
| Modified Cholesky, SIOPT 1999 (P600, §6) | Toy primal-dual IPM on dense random LPs with m = 6, n = 12 and "controlled degeneracy properties". The monitored quantities are compared with the paper's estimates | "To test that the analysis of this paper was reflected in computations, we coded a simple primal-dual interior-point algorithm and applied it to test problems with controlled degeneracy properties." (spacing normalized). "In PCx [3], we needed to change fewer than 20 lines of the sparse Cholesky code of Ng and Peyton [10]." (spacing normalized) |
| Finite precision, SIOPT 2001 (§7) | 2-variable example (2.8). Run once with the full system, once with the condensed system, then on a modified example that removes a lucky cancellation | "We programmed the method in Matlab, using double-precision arithmetic." "To show that the lack of cancellation effects in Table 7.2 cannot be assumed in general, we modified problem (2.8) slightly" (arXiv math/0103102 / P705 text, §7) |
| Degenerate NLP, SIOPT 2005 (§6) | One step of Framework INEQ from ε-perturbed points, for ε = 2^-3 to 2^-40. Then a "simulated roundoff" run that injects perturbations of size u = 10^-12 | "(The results were obtained from a Matlab implementation.)". "Our example (6.6) is too small and simple to exhibit the errors discussed in the previous paragraph, but we can simulate the effects of such errors by introducing arbitrary perturbations into (4.2) and tracking the effects of these perturbations on the computed step." The expected result is that finite precision interferes "only when η̄ drops below √u" (p. 695) |
| Constraint identification, MP 2003 (P865, §6) | 100 random perturbations per ε on three small problems, two of them modified Hock–Schittkowski problems. Then a 20-trial duel of sSQPa against standard SQP on a 2-variable MFCQ problem | See §1.2 |
| Coordinate descent survey, MP 2015 (§3.8) | Convex quadratics Q := V_{r,η}ΣV_{r,η}^T + ζ11^T, whose parameters (η, ζ, r, cond Σ) are chosen to move the constants that appear in the theory's bounds. Six variants are run: CYCLIC, IID and EPOCHS, each with a fixed and an optimal step | "Nevertheless it is worth asking whether various aspects of the convergence analysis presented above — in particular, the distinction between CD variants — can be observed in practice." It reports that a linear rate "held even for problems in which Q was singular — a significant improvement over the sublinear rates predicted by the theory", and "numerous “stressed” settings in which the CYCLIC variants are much slower than the randomized variants, by factors of 10 or more." (arXiv:1502.04759v1, pp. 22–24) |

- The same move appears in a talk [practice, P]. For the Vavasis–Ye "twisted central path" geometry he built the LP "min x0 subject to x0 ≥ ϵ^i xi, 0 ≤ xi ≤ 1" and ran two production codes on it, MOSEK and his own PCx. He reported "n = 20, ϵ = 0.1. Turn off presolve, scaling, crossover to simplex." and observed "Each iteration resolves a single component." (SIAM OPT talk, 20 May 2002, slides 36–39). The switches were turned off so that the solver's heuristics would not hide the geometry the theory describes.
- Theory is also written to explain computation [practice, P]. P699 Theorem 5.2 is introduced with "(This result explains an observation made while doing computational experiments for an earlier paper [18].)" (P699 preprint, p. 10). The acknowledgments name who ran those experiments: "Thanks also to Michael for for carrying out numerical experiments during his summer at Argonne in 1997." (p. 25; "for for" is in the original; "Michael" is Michael Wagner, named in the preceding sentence).
- [inferred] For solver design this is his most transferable habit. Every asymptotic claim, whether superlinear rate, identification or stability, gets a tiny example in which the predicted quantity is printed iteration by iteration and compared with the bound. Where needed, the example is perturbed so that it has the bad case.

### 1.2 Test sets, baselines and fairness devices

**Where the test problems come from** [practice, P]:
- **Netlib and application LPs** (PCx, 1997). "We solved a large set of test problems, both feasible and infeasible, taken for the most part from the familiar netlib set." The set also includes "some new problems arising from the NEMS project at Argonne" (PCx User Guide, OTC 96/01, §1 and §10; spacing normalized). Infeasible problems are part of the standard run.
- **A borrowed protocol** (P865, 2000). "Our tests of Procedure ID0 are similar to those reported by Facchinei, Fischer, and Kanzow [5, Section 4]." Examples 2 and 3 are "A modification of problem 46 from [10], described in [5, Example 2]" and of problem 43, both from Hock–Schittkowski via the competing paper (pp. 21–22). He tests on his competitor's instances.
- **Degenerate CUTEr problems, with a production code as oracle** (Oberlin & Wright 2006). "The subset contains degenerate problems of small or medium size for which the Interior/Direct algorithm of Knitro 4.x terminates successfully within 3000 iterations (with default parameter values)" (p. 598). The "true" active set is estimated from Knitro's output, and the paper admits that this estimate is itself parameter-sensitive (pp. 598–599, 603).
- **Random problems with dialled-in degeneracy** (same paper). The generator controls "the row rank of J and A and the proportion of weakly active constraints" (p. 595). The paper states why both kinds of problem are used: "While the random problems are well scaled with dense constraint Jacobians, the CUTEr problems may be poorly scaled and typically have sparse constraint Jacobians." (p. 593)
- **CUTEst with a size rule** (Curtis, Robinson, Royer & Wright 2021, co-authored). "If the default size (according to the sizes that come with the distribution, downloaded July 1, 2020) was in the range [100,1000], then we used the default size." This gives 233 problems, and the reported results use the 109 with n ≥ 100 (arXiv:1912.04365v3, p. 21).
- **Netlib again, through his own old presolver** (Ding & Wright 2023). "Since the problem data of Netlib usually have some redundancies and degeneracies, which hurts code performance and makes comparisons unreliable, we use the presolver from PCx [5] on each problem." Acknowledgment: "We thank Ivan Jaen Marquez for his help in resuscitating the PCx linear programming code for use in our experiments." (arXiv:2310.01784, pp. 23, 27)
- **Application test cases**: IEEE 57-bus, IEEE 300-bus and Polish 2383/2746-bus systems for the Sℓ1LP feasibility-restoration algorithm (Kim & Wright, Optim. Eng. 2015, 10.1007/s11081-015-9292-z; arXiv:1405.0322, §6). SMPS stochastic-programming instances (20term, LandS, gbd, SSN, storm) are released on a companion site. Images (Barbara, Cameraman, shape) are shipped inside the TVGP code.

**Baselines and fairness devices** [practice, P unless marked]:
- **Stop at the same objective value** (GPSR 2007, SpaRSA 2009).
  - GPSR: "To perform this comparison, we first run the [l1_ls] algorithm and then each of the other algorithms until each reaches the same value of the objective function reached by [l1_ls]." (JSTSP 2007, p. 593)
  - SpaRSA: "To make the comparison independent of the stopping rule for each approach, we first run FPC to set a benchmark objective value, then run the other algorithms until they each reach this benchmark." (TSP 2009)
  - GPSR reuses the benchmark scenario of the strongest competitor: a CS setup "(similar to the one in [36])", where [36] is the l1_ls paper, and "Parameter [τ] is chosen as suggested in [36]" (p. 592).
- **Tune the competitor** (Hogwild!, 2011, group paper with Niu, Recht and Ré). "To be as fair as possible to prior art, we hand coded RR to be nearly identical to the Hogwild! approach, with the only difference being the schedule for how the gradients are updated." RR's locks were then optimized to spinlocks. "We show results for the largest value of the learning rate γ which converges" (hogwildTR, p. 11). [inferred] Given the co-authors, the systems-side fairness work is probably not Wright's own.
- **Cap the method with the stronger guarantee so it cannot win on accuracy** (Xie & Wright, arXiv:2103.15989). "Although PNCG and LBNCG are able to locate approximate second-order optimal solutions, we stop these algorithms as long as a first-order point is found or time/iteration limit is reached, so that comparison with pgrad is fair." (§5; LBNCG is the group's own earlier log-barrier Newton-CG.) The baselines span general solvers (projected gradient, MATLAB `fmincon` interior point), the group's own earlier method, and NMF-specialized alternating methods.
- **Ablate the safeguard the theory needs** (Curtis et al. 2021).
  - Each complexity-motivated variant is paired with a "(no reg.)" twin: "This variant demonstrates the effect of this regularization term on the practical performance of TR-Newton."
  - The reported outcome goes against the paper's own devices: "The variants with no regularization term in the subproblems outperform the others in this respect; recall that these variants do not possess optimal complexity guarantees." (arXiv:1912.04365v3, pp. 21–22)
  - This is the computational basis of the 2025 self-assessment that 01 and 02 quote (§5.2 in 02).
- **Duel on the failure case** (P865). On a 2-variable problem where "The constraint gradients are linearly dependent, but satisfy MFCQ", sSQPa converged in two iterations in all 20 trials. For standard SQP: "Failure occurred 9 times in the 20 trials, while the other 11 trials required between 13 and 15 iterations each." (pp. 23–24)
- **Report the failures in the tables** (P865). "For ϵ = .1, the correct active set was identified in 82 trials, but in none of these cases was the correct classification into B+ and B0 obtained." Parameter sensitivity is disclosed: "by changing τ̂ from 0.65 to 0.4, we find for ϵ = 0.1 that the proportion of correct classifications jumps from 31% to 64%." (pp. 21–22)
- **Flag the favourable setup yourself** (Oberlin & Wright 2006). "It is unlikely that a nonlinear programming algorithm that uses LP-P or LP-D as its identification technique could in practice choose a value of Δ as nice as the one used in these tests." (p. 593)

**Solver-engineering choices written into experiment sections** [practice, P]:
- *Oberlin & Wright* (pp. 592–594):
  - "We implemented all tests in C, using the CPLEX callable library (version 9.0)".
  - CPLEX cut generation was switched off: "given our usually excellent starting point for the LPEC test, the cost of cut generation is excessive compared to the cost of solving the root relaxation".
  - The feasibility tolerance was tightened from 10^-6 to 10^-9 because LP-P objective values were "too negative" under the defaults.
  - Near-minimal big-M values cut run times "by as much as 50%".
- *Curtis et al. 2021*, on CG's iteration cap: "we use the quantity n̄ := min{n+2, 1.2n} in place of n ... This relaxation can be beneficial in practice since loss of conjugacy due to numerical rounding can result in a zero residual not being attained by CG after n steps." The randomized-Lanczos minimum-eigenvalue check runs with a tight tolerance "since Algorithm 3 is rarely invoked" (p. 20).
- *Ding & Wright 2023*, a debugging note that names a monitored quantity: "In the experiments, we observed that SSV-SQP fails to converge when the complementarity measure ∥rxs∥1 + ∥rrw∥1 is small while the infeasibility measure increases. Convergence tends to occur when these two measures decrease at similar rates." (arXiv:2310.01784, footnote 11)

### 1.3 Testing folklore and building tools around an application

- **Folklore tested and rejected** [stated, P] (Linderoth & Wright, COAP 2003 Best Paper note, COAP 29 (2004), p. 124). "anecdotally their performance was thought to be inferior to methods that used a quadratic regularization term and which therefore required a specialized quadratic programming code for their solution. (We did not find evidence to support this belief.)"
- **Tool-building driven by a chosen application** [stated, P] (same note): "During initial development of MW, Linderoth and Wright sought applications that could be used to test it and drive its evolution. Two-stage stochastic linear programming was a fairly obvious candidate." The PDF breaks "a fairly" as "af airly".
- **Scale and resources** [stated, P]: "Using a computational grid of over 1000 processors spread across the U.S. and Europe, the problem was solved in a little over one day of wall clock time." The instance had 10^7 sampled scenarios and "over 10^10 unknowns" (same note).
- **Warm starts decide the method** [practice, P] (Kim & Wright 2015, arXiv:1405.0322, p. 2). He chose an LP-based Sℓ1LP method, following Fletcher, over IPMs for power-flow restoration because of warm starts, and cited his own earlier negative result: "By contrast, warm-starting strategies for interior-point methods have not proved to be effective in general (Yildirim and Wright 2002), except when the optimal active set does not change between outer iterations."
- [inferred] The same trade-off, warm-startable active-set or first-order methods against IPMs, decided the method class in GPSR (2007) and in Sℓ1LP (2015).

### 1.4 Code: how his solvers evolved (changelogs)

**PCx** (Czyzyk, Mehrotra, Wagner & Wright; OMS 11 (1999), 10.1080/10556789908805757) [practice, P, changelog "updated 1/10/06"]:
- **Release history**:
  - beta-1.0: 15 May 1996.
  - beta-2.0: 18 Oct 1996, which "Includes dense column handling, many memory leak and bug fixes".
  - 1.0: 7 Mar 1997, which "Includes higher-order corrections, scaling, bug fixes".
  - 1.1: 2 Nov 1997, which "Includes hooks to incorporate alternative linear equations solvers, including WSSMP".
- **Maintenance to 2006**: fixes to presolve (row singletons, 2002 and 2003), MPS parsing ("MI" bounds, 2001), a Gondzio-corrector bug on bounded instances (1999), the line-search heuristic (2001), and hash tables for more than 1.3 million rows and columns (2004).
- **Measured claim for a pluggable solver**. For the linear-solver hook, the page reports measured results rather than a claim: "Overall, WSSMP never performs significantly worse, while for some larger problems it outperforms the Ng-Peyton sparse Cholesky solver by as much as an order of magnitude." (PCx WSSMP page)
- **Design intent** [stated, P, User Guide §1, spacing normalized]. It lists "modular structure, which makes it easy for users to modify the code to experiment with variants of the current algorithm", and says "PCx should be viewed as work in progress".
- **Named division of labour**: "Marc Wenzel programmed the dense-column-handling and conjugate gradient refinement features ... Doug Moore ... pointed out and repaired many memory leaks in the beta-1.0 release. Hans Mittelmann prepared the executables for numerous architectures and ran many of the benchmark tests." (PCx page)
- **Current status**: "PCx is no longer supported." (PCx page). Yet it was brought back in 2023 for experiments (§1.2).

**OOQP** (Gertz & Wright; TOMS 2003) [practice, P, changelog and GitHub `emgertz/OOQP`]:
- **Structure-independent core**. The design isolates the IPM from problem structure: "The code that implements the core of the algorithm, including all its sophisticated heuristics, can be reused across the entire space of problem structures and applications." Algorithm choice is justified by experience: Mehrotra and Gondzio correctors "have proved to be the most effective methods for linear programming problems and in our experience are just as effective for QP." (TOMS paper, pp. 60, 64)
- **Changes driven by users' problems**:
  - 0.99.10 (May 2004) added `--scale` because "This work was motivated by some practical problems arising in forestry management, in which the values of some data objects ranged over 25 orders of magnitude."
  - 0.99.25 (2014) "Throws an exception (instead of crashing) if MA27 cannot factor a matrix after several attempts with different parameters."
  - 0.99.24 (2012) states "that the MA27 interface is the best supported and most robust."
- **Who did the later work** [inferred]. After about 2004 the named maintainers are Vanitha Suresh (releases 0.99.10–0.99.21, per the OOQP page), Gertz (repository owner from 2012) and users (Kibaek Kim, John Grove). Wright's hands-on role in the code looks to end with the paper.

**TVGP** (Zhu, Wright & Chan) [practice, P]:
- The second release (14 Oct 2008): "Changed algorithms to give consistent convergence criteria; changed test code to facilitate esier comparison between the algorithms". It adds: "Run data is saved in a mat file to allow regenereration of tabular data and figures as needed" (changelog; the misspellings are in the original).
- The test driver `Test_TVGP.m` has on/off flags for about 20 algorithm variants. It runs all of them to a common relative duality-gap tolerance, swept over 10^-2, 10^-3, 10^-4 and 10^-6.

### 1.5 Reproducibility packaging

- **LPS** (code rewritten for distribution by Wright himself) [practice, P].
  - The page states: "The codes were written initially by W. Shi and S. Wright in 2006-2008 and rewritten for distribution in 2008-2011 by S. Wright."
  - The README lists "TestTables.m: Routine to reproduce the data reported in the tables of [5]", where [5] is the SIOPT 2012 paper.
  - The script header carries his initials and dates ("SJW 4/19/10", "SJW 8/7/10", "SJW 8/24/11").
  - It sweeps gradient-sample and Hessian-sample fractions, with a built-in ablation: "% interpret hessianSampleFrac=0 to mean that we use a first-order % method (no Newton acceleration)." (LPS-v2.2/code/TestTables.m)
  - Version 2.2 was "Issued in conjunction with the revision of [2]", and version 2.1 "modified the approach of [1] in several ways to accommodate a convergence analysis while retaining performance characteristics of the earlier implementation" (LPS page).
  - [inferred] The code was deliberately changed to fit the analysis while practical behaviour was checked. This is the same move as the 2017–2021 Newton-CG program (01, S5), made 7 years earlier.
- **Data release** [practice, P]. The stochastic-programming data are on a companion site in SMPS format, with suggested starting points. The site also carries a promise that was not kept [stated, P]: "Currently the paper contains a fair amount of detail about the experiments. Eventually we'll put additional details here." It was unchanged when read on 2026-09-28.
- **Code by postdocs** [practice, P]. From about 2020 the experiment code sits in postdocs' repositories. Xie & Wright v1 footnote: "Source codes of experiments in this section can be found at: https://github.com/yue-xie/ProjectedNewton" (a MATLAB repository created 2020-12-16, per GitHub metadata). Hardware is reported: "Matlab R2018b on MacBook Air 1.3 GHz Intel Core i5" (2021) and "a 2020 Macbook Pro with an Apple M1 chip and 8GB of memory" (Ding & Wright).

---

## 2. Layer 5: judging results, corrections, and what revision changes

### 2.1 He publishes his own errors, including proof errors

- **Corrigendum to a journal proof** [practice, P] (Wright & Jarre, MP 84, corrigenda dated 22 Sep 2000): "The published paper contains a number of typographical errors and an incomplete proof. We indicate the corrections here." and "The final part of the proof of Theorem 2 is incomplete. We remedy this fault by deleting the material from line 6 on page 368 through the end of the proof, and replacing with the following." (spacing normalized)
- ***Primal-Dual Interior-Point Methods* errata**, 43 items, "last updated December 12, 1999" [practice, P]. Beyond typos they include:
  - item 13, Theorem 6.8: "The use of ϵ(A, b, c) and consequently the definition of C3 in (6.52) is incorrect."
  - item 15, Algorithm PC for LCP: "The predictor and corrector steps are reversed in the specification of the algorithm."
  - item 20, Theorem 9.3: "This proof is inadequate since it assume feasibility of the primal problem." ("assume" is in the original.)
  - item 18, an overclaim about the homogeneous self-dual formulation of Ye, Todd and Mizuno, withdrawn with a counterexample: "Replace “all” by “most of”", adding "(There is an example in the YTM paper [159, page 62] of a problem that is both primal and dual infeasible, for which a solution of the HSD formulation reveals only the primal infeasibility.)"
  - Nine readers are thanked by name, among them Nick Higham and Anders Forsgren.
- **Errata for the other books** [practice, P]:
  - *Numerical Optimization* 2nd ed.: 79 items, "Last updated May 17, 2008". Nocedal's page keeps separate lists for the 1st-edition printings ("updated 2/12/06").
  - *Optimization for Data Analysis*: a typo list dated "31 January 2023", kept in a GitHub repository. Two of its four credited readers are his students and co-authors (Ching-pei Lee, Changyu Gao). The corrections include a sign-of-curvature slip ("“strongly convex in λ” should be “strongly concave in λ”").
- **A student's reimplementation surfaces errors** [observed, P]. The JOTA 1998 errata were written by the student Matthew J. Tenny: "This paper presents the corrected equations used in the JOTA paper [1]." (errata of 8 Aug 2000, spacing normalized). Wright hosts them "courtesy of Matt Tenny" (papers page). [inferred] Errors in the MPC structured-IPM equations surfaced when a student implemented them. They were posted, not buried.
- **Own-paper error corrected in the next paper** [practice, P]. SpaRSA says of GPSR's debiasing stopping rule: "(The same criterion is used in GPSR; the criterion shown in [39, (21)] is erroneous.)" (TSP 2009, §II-I).

### 2.2 What revisions change (arXiv v1 versus final)

Method: I fetched submission histories for all 79 arXiv records under his name plus arXiv:0812.0423. For 56 multi-version records I diffed v1 against the latest abstract, and for four NLP-relevant papers I compared the full texts. [practice, P]

| Paper | v1 → final | Direction |
|---|---|---|
| Xie & Wright, arXiv:2103.15989 (MP 2024) | Title "Complexity of Projected Newton Methods for Bound-constrained Optimization" becomes "Complexity of a Projected Newton-CG Method for Optimization with Bounds". The v1 §3, "Complexity of scaled two-metric (gradient) projection", with an O(ϵ^-2) result, is gone from the final (0 occurrences of "scaled two-metric" against 8 in v1). It is replaced by a section comparing definitions of approximate second-order points | A method was **dropped**. The reason is not stated in the paper, and the referee reports were not read |
| Xie & Wright, arXiv:1908.00131 (J. Sci. Comput. 2021) | v1 had "5 Numerical experiment" on dictionary learning, and its abstract said "Preliminary numerical results support our findings and demonstrate efficiency of this traditional method on dictionary learning". v4 has no experiment section. It adds operation complexity with Newton-CG and "5 Determining ρ". The parameter condition changes from "ρ = O(1/ϵ^η)" to "ρ = Ω(1/ϵ^η)", and the η range is corrected | Experiments **removed**, theory deepened, a bound corrected |
| O'Neill & Wright, arXiv:1706.07993 (MP 2019) | v1: the heavy-ball method "does not converge to critical points that do not satisfy second-order necessary conditions". Final: it "is unlikely to converge to strict saddle points" | Claim **softened** to what the stable-manifold argument gives (almost-sure, not certain) |
| Lewis & Wright, arXiv:0812.0423 (MP 2016) | v1 (Dec 2008, 34 KB) has no computations. v2 (Apr 2015, 118 KB) adds "Preliminary computational results on both convex and nonconvex examples are promising." | Computations **added** during a 6-year revision |
| Yıldırım & Wright (SIOPT 2002) | "We are grateful to the referees for their careful reading of the first version of the paper and their perceptive comments, which prompted the addition of section 6." (the numerical section) | Computations **added** at the referees' prompting |
| Wright & Lee, arXiv:1706.00908 (Math. Comp. 2020) | "A convergence analysis is developed to support the computational observations" becomes "...to explain the empirical observations" | The analysis framed as an **explanation** of what was observed |
| Curtis et al., arXiv:1912.04365 (SIOPT 2021) | Abstract essentially unchanged (ratio 0.98). The CUTEst download is dated 1 July 2020, after v1 of Dec 2019. The acknowledgments credit "the editor and two anonymous referees, whose comments led to significant improvements to the paper" | [inferred] Experiments rerun or rebuilt during revision |
| Wright, arXiv:2510.15734 (v1 17 Oct → v2 2 Dec 2025) | 73 changed sentences, mostly copy edits. The substantive ones: "kth Lanczos subspace" becomes "kth Krylov subspace"; "a nearby instance is easy to solve" becomes "is usually easy to solve"; "global minima of nonconvex objectives are usually found easily" becomes "global minima of certain nonconvex objectives are usually found easily [96], despite global minimization of general nonconvex objectives being intractable"; "more general linear functions" becomes "more general nonlinear functions" | Terminology corrected and claims **hedged** |

- [inferred] No single rule governs whether experiments survive revision. They are added when referees ask (2002) or when the paper matures into a method paper (2015). They are cut when the paper becomes a complexity paper (2021). Complexity papers get tighter statements and fewer, better-scoped claims.
- **Revision time is long** in the Argonne-era record [practice, P, papers page]:
  - P485: Dec 1994 → rev. May 1998 → 1999.
  - P600: May 1996 → rev. May 1998 and Dec 1998 → 1999.
  - P622 (Ralph & Wright, MOR 25, 10.1287/moor.25.2.179.12227): Nov 1996 → rev. Aug 1998 → 2000.
  - P681 ("On the convergence of the Newton/log-barrier method", MP 90, 10.1007/PL00011421): Aug 1997 → rev. Jan 1999 and Apr 2000 → 2001.
  - P705: Jan 1998 → rev. May 2000 → 2001.
  - P772 (Wright & Orban, MOR 27, 10.1287/moor.27.3.585.312): Jul 1999 → rev. May 2001 → 2002.
  - P865: Dec 2000 → rev. Dec 2001 → 2003.
  - Typical: one to two rounds, 2–4 years from preprint to print.

### 2.3 How he answers criticism (public rebuttals)

Only the NIPS proceedings site exposes reviews and author feedback for his papers. OpenReview was blocked (see Gaps). Both rebuttals below are **joint author texts**, so they show the group's practice and cannot be attributed to Wright alone. [practice, P]

**Lim & Wright, NIPS 2014** ("Beyond the Birkhoff Polytope: Convex Relaxations for Vector Permutation Problems", NIPS 27; arXiv:1407.6609):
- **Rerun the experiments with an expanded design, rather than argue**. "We would like to note that we have a full version of this paper that fixes all typos spotted by the referees, and has a revised and expanded experiment section."
- **Change solver when the tool distorts the comparison**. "We were constrained in the submitted version by using CVX to solve all formulations on the Munsingen data set, and CVX was unacceptably slow on the Birkhoff formulation. We have switched to using Frank-Wolfe for all formulations on Munsingen, since timings and efficiency are not of significant interest here." And: "we have dropped timings for this dataset altogether, since for most formulations the times are fast, with the one exception being due more to an infelicity in the CVX solver than to a defect in the formulation."
- **Drop an experiment that lacks a baseline**. "we decided not to pursue results on the graph data that was used in [22], as the case for solving the seriation problem on this graph was weak, and no “baseline” solution was available."
- **Concede errors plainly, even beyond what the reviewer found**. "Thank you for catching these errors in our exposition on R-matrices. We had actually said that for any pre-R matrix there is only one corresponding R-matrix, but even this claim is false".
- **Defend what they believe in**. "We believe the figure is worth including and will try to provide a better explanation in the revision."
- Afterwards the paper grew into a 31-page arXiv version, retitled "Sorting Network Relaxations for Vector Permutation Problems" (v3, Feb 2016).

**Sridhar, Bittorf, Liu, Zhang, Ré & Wright, NIPS 2013** ("An Approximate, Efficient LP Solver for LP Rounding"; arXiv:1311.2661):
- **Run the reviewer's baseline inside the rebuttal**. Reviewer 4 asked: "The simple baseline of increasing the tolerance \epsilon for the Cplex-LP solver is not tested." The authors answered with a table for ε ∈ {10^-1, 10^-3, 10^-5} on frb59-26-1. Reviewer 4 then wrote: "The rebuttal has answered my only (minor) concern".
- **Answer a "why not SGD" question with a complexity comparison**. "we see an iteration complexity of epsilon^{-2} for SCD ... For diminishing-step or constant-step variants of SG, we see complexity of epsilon^{-7}, while for robust SG, we see epsilon^{-10}." [inferred] This paragraph reads like the optimization theorist's contribution.
- **Tone down an overclaim**. "We agree that the paper should tone down its claim that Cplex and Gurobi are unsuited to machine learning applications ... We will make the more limited claim that we identify a class of problems where using approximate LP solutions for LP-rounding is a competitive approach."
- **Classify instances by which solvers can run**. "Our instances to fall in to three categories: (1) All methods could run; (2) Cplex-LP could run, but not Cplex-IP; (3) Only Thetis works." ("to fall in to" is in the original.)

**Reviewers' view of a gap** [observed, P], NIPS 2017 (Lim & Wright, "k-Support and Ordered Weighted Sparsity for Overlapping Groups: Hardness and Algorithms"; reviews only, no rebuttal published). Reviewer 3: "While being mostly a computational paper, strangely, the experiment section only compared the statistical performances of different norms, without conducting any computational comparison."

**Journal referees are adopted and credited** [practice, P]:
- Oberlin & Wright 2006: "Following a suggestion of a referee ... we obtained a new identification technique ... We found that, indeed, this “threshold LP-D” estimate of the active set was more accurate" (p. 603).
- P699: "I am also grateful to two referees for their comments on the first version and their pointers to related literature, which improved this version of the paper considerably."
- P600: "their extremely close and patient reading of both versions led to the elimination of many infelicities and typos" (spacing normalized).

### 2.4 How results are reported: calibrated language

[practice, P]
- **Low-accuracy advantage shown, weakness conceded**. "Overall, although the results for SSV-SQP are considerably worse overall than for MPC, we see reasons to investigate the approach further. First, the difference in performance and robustness of the two approaches is least for low-accuracy solutions ... Second, we believe that tuning we could improve the performance of SSV-SQP, for which (by contrast with MPC) there is no “folklore” concerning heuristics that improve efficiency." Also: "The practical implications of this theoretical advantage are however minimal." (arXiv:2310.01784, §4 and §5.2.2)
- **Speed comparisons flagged as indicative only**. "Of course, these speed comparisons are implementation dependent, and should not be considered as a rigorous test, but rather as an indication of the relative performance of the algorithms for this class of problems." (SpaRSA, TSP 2009)
- **Scope of "competitive" stated**. The method "is competitive with the specialized methods on problems with relatively low dimensions" (Xie & Wright v1, §5).
- **Deferred items listed**. The conclusions of P865 (2000), Oberlin & Wright (2006) and Yıldırım & Wright (2002) end with explicit lists of what was not done (see §4).

---

## 3. Layer 6: expression (how the work is packaged)

- **Theory paper plus companion application paper** [practice, P]. "A companion report of Tenny, Wright, and Rawlings [15] describes application of the algorithm to nonlinear optimization problems arising in model predictive control." (Wright & Tenny, SIOPT 2004, p. 1077). The SIOPT paper has no numerical section. Its implementation remark is a forecast, not a test: "We anticipate, however, that a procedure that works well in practice would be relatively easy to implement, especially under the LICQ and strict complementarity assumptions." (p. 1095)
- **Short conference paper plus long arXiv version** (NIPS 2013 and 2014, ICML) [practice, P]. "An extended version of the ICPRAM 2012 paper" (arXiv:1111.0432 comment); "A short version of this paper appeared in NIPS 2014" (arXiv:1407.6609 comment).
- **"Honest limits" paragraph in conclusions** [practice, P]:
  - P865, 2000: "Nevertheless, the practical usefulness of constraint identification and stabilization techniques remains to be investigated."
  - Oberlin & Wright, 2006: "However, it remains to determine how the schemes above can be used effectively as an element of a practical algorithm for solving nonlinear programs."
- **Simplicity preferred over completeness in exposition** [practice, P] (Curtis et al. 2021, §5). "This “implicitly capped” method is more complicated to describe than the “explicitly capped” version of CG that we consider here, so in this paper we opted for simplicity of description at the expense of a (small) probability of failure in the subsequent call to Algorithm 3."
- **Credit for a proof given to a colleague** [practice, P]. "We thank Yue Xie for providing most of the proof of Theorem 2." (Curtis et al. 2021, acknowledgments)
- **Talks show computation next to theory** [practice, P]. The 2002 talk sets solver output tables (MOSEK and PCx iterates) beside the geometric theory (slides 36–40).

---

## 4. Failures, abandoned, deferred and unfinished work (behavioural record)

| Item | Evidence [tags] | Status |
|---|---|---|
| **Embedding degenerate-NLP techniques (stabilization, constraint identification) in a practical solver** | Deferred in 2000 (P865, §7), 2002 (P699: quasi-Newton case left "for possible future work"; globalization ignored) and 2006 (Oberlin & Wright, §5). No released NLP code and no follow-up paper embedding them was found in DBLP or OpenAlex (see 01). In 2026 the topic returns only as theory (Lee & Wright, arXiv:2602.10470, no experiments), motivated by the practical difficulty that line-search parameters to avoid the Maratos effect "can be difficult in practice" (p. 2) [practice, P; inferred on "abandoned"] | **Unfinished for 20 years**: the loop from theory to solver never closed |
| Computational follow-up of warm-start IPMs | Yıldırım & Wright (2002): "In future work, we plan to extend the techniques to infeasible interior-point methods and perform computational experiments to determine the practical usefulness of these techniques." The implementation paper appeared without Wright: John & Yıldırım, COAP 41 (2008), 10.1007/s10589-007-9096-y [practice, P/S]. Wright later cites the 2002 paper as evidence that IPM warm starts "have not proved to be effective in general" (Kim & Wright, arXiv:1405.0322, p. 2) [practice, P] | Handed off; later used as a negative result |
| "Semi-local" convergence along twisted central paths | Asked on slide 40 of the 2002 talk; no paper found (see 01) [inferred] | Open |
| Sparse nonlinear SVMs via stochastic approximation (Lee & Wright) | ACM-format manuscript, "submitted, February 2010". The entry is **commented out** in the papers-page HTML, and OpenAlex title search returns 0 records [practice, P] | Unpublished |
| ASSET (Lee & Wright) | A draft in the IEEE TPAMI template (`sncss_tpami.pdf`, Sep 2010) was published at ICPRAM 2012 (6 pp., 10.5220/0003786202230228) with an arXiv "extended version" [practice, P]. That it was rejected by TPAMI is **not verified** [inferred] | Downgraded venue |
| GPU implementations of SpaRSA and PDHG (Lee & Wright) | TR of Sep 2008 in the IEEE TSP template, "submitted, 2008". OpenAlex has only the 2008 TR record, with no venue. Code released (Nov 2008) [practice, P] | Code outlived the paper |
| *Numerical Optimization* 3rd edition | GitHub repository created 18 Jul 2022: "Github working directory for Numerical Optimization, 3rd edition. Completed drafts of chapters will be posted here as they become available." It is empty (size 0) and the last push was 18 Jul 2022 [practice, P] | Stated plan with no public output as of 2026-09-28 |
| Companion-site promise (sampling paper) | "Eventually we'll put additional details here." Not updated [stated, P] | Unfulfilled |
| PCx licensing | "PCx is freely available, but is not public domain software. Commercial users should obtain a license." (PCx page). Later codes (GPSR, SpaRSA, LPS, TVGP, GPU) were posted as plain zip or tar downloads [practice, P]. Compare the oral-history regret (01, S1) | Model abandoned after about 2001 |
| Variants tried and dropped | GPSR: "In earlier testing, we experimented with other variants of GP, including the GPCG approach of [43] and the proximal-point approach of [59]. The GPCG approach runs into difficulties because the projection of the Hessian [...] onto most faces of the positive orthant defined by [...] is singular, so the inner CG loop in this algorithm tends to fail." (JSTSP 2007, p. 590). Oberlin & Wright: alternative bound-handling formulations "gave little or no improvement in performance, so we do not report on them further." (p. 598). P600: "since we observed some large linear programs in which the skipped pivots were not confined to the lower right corner, we omit a detailed analysis of this case." (spacing normalized) [practice, P] | Documented drops |
| Rejected journal papers | No public record (math-programming venues have closed review) | Unknown |

---

## 5. Layer 7: research organization visible in the artifacts

- **Division of labour on code** [practice, P]:
  - Argonne era: postdocs and staff (Czyzyk, Wagner, Wenzel, Moore), a summer student running experiments (Michael Wagner, summer 1997), an external benchmarker (Mittelmann), and summer students on OOQP ("Nate Brixius and Bjarni Halldorsson, who contributed to the early stages of this project in the summer of 1999", TOMS 2003).
  - UW 2001–2011: PhD students write the experiment code (Oberlin in C with CPLEX; Tenny for MPC; Zhu for TVGP; S. Lee for GPU). Wright rewrote LPS himself.
  - 2017–: postdocs (Royer, Xie, Alacaoglu, Ding) run MATLAB experiments and host the code.
- **Students as error-finders and errata authors** [practice, P]: Tenny (JOTA errata, 2000); S. Lee ("Thanks to Sangkyun Lee for pointing it out", LPS 2.1 changelog); Ching-pei Lee and Changyu Gao (OFDA typos, 2023).
- **Credit is given in the artifact** [practice, P]. This appears in changelogs ("Thanks to Kibaek Kim", "Thanks to John Grove"), acknowledgments, and "courtesy of Matt Tenny" on the papers page.
- **Rules for shared materials** [stated, P] (TRIPODS-EDUCATION README, 2017): "Material should be posted with the consent of all authors involved - do no upload interesting stuff you find on the web without obtaining consent from the authors." ("do no" is in the original.)
- **Resourcing** [practice, P]. The artifacts name the funders: DOE contract W-31-109-Eng-38 (Argonne), NSF (CDA-9726385, ACI-0082065, CCF-0430504 and others), TWMCC industrial members (Wright & Tenny), and NVIDIA's "Professor Partnership Program" for GPUs.

---

## 6. Era and resource context of the practices

| Period | Setting | Practices tied to it |
|---|---|---|
| 1994–2001, Argonne MCS | No teaching; a DOE lab with software staff and postdocs; Unix workstations (IBM RS6000, SGI IRIX, Argonne's IBM quad); Fortran and C; netlib and MPS; metaNEOS grid (Condor/MW, 1000+ processors) | Solver releases with changelogs (PCx), solo theory papers with toy MATLAB checks, long revision cycles, errata lists, grid-scale computational studies |
| 2001–2010, UW-Madison CS | PhD students; MATLAB for illustrations; C with the CPLEX callable library; Knitro as a reference solver; GPUs donated by NVIDIA | Degenerate-NLP computational study (2006); signal-processing codes released as MATLAB zips; equal-objective benchmarking |
| 2011–2016, ML and parallel era | Multicore servers (for Hogwild!: "a dual Xeon X650 CPUs (6 cores each x 2 hyperthreading) machine with 24GB of RAM"); CVX and Gurobi; NIPS review culture | Tuning the competitor, rebuttals with new tables, short conference versions plus long arXiv versions |
| 2017–2026, complexity and data-science era | Postdocs, laptops (MacBook Air 2018; M1 MacBook Pro 2020), CUTEst, GitHub | Ablations of complexity safeguards, theory-only complexity papers, code in postdocs' repositories, arXiv revision hedging |

[inferred] The toy-example-in-MATLAB habit costs almost nothing in compute. It is still available to anyone improving a solver. The grid-scale studies depended on Argonne and Condor infrastructure that a small team does not have.

---

## 7. Layers 1–3 (taste, problem choice, idea generation): what process evidence adds

- **Observation first, then a paper that explains it** [practice, P]. The chain runs as follows:
  1. The CD survey's "stressed" settings (2015).
  2. Lee & Wright, "Random permutations fix a worst case for cyclic coordinate descent" (2016–2019), whose final abstract adds that RPCD performs "even better than RCD in a certain regime".
  3. Wright & Lee, "to explain the empirical observations" (2017–2020).
  - Ho-Nguyen & Wright (MP 2022, 10.1007/s10107-022-01796-6) is the same move: "Numerical experiments show that, despite the nonconvexity, standard descent methods appear to converge to the global minimizer for this problem. Inspired by this observation, we show that..." (arXiv:2005.13815v1 abstract).
- **Borrowing from teammates' traditions** [practice, P]:
  - Fletcher's Sℓ1LP and the Fletcher–Sainz de la Maza theory are the base of the power-systems algorithm ("Following Fletcher (1987), we refer to this approach as sequential ℓ1-linear programming (Sℓ1LP)", arXiv:1405.0322, p. 6).
  - Vavasis–Ye geometry is tested on MOSEK and PCx (2002).
  - Ye–Todd–Mizuno HSD is discussed and corrected in the PDIPM errata.
  - SNOPT's behaviour is the explanandum of P699.
  - Philip Gill is thanked for discussions in P699.
- **Own old code as a research instrument** [practice, P]. PCx 1.1 (1997) presolves Netlib for a 2023 squared-variables study. [inferred] He keeps infrastructure alive for decades and reuses it to test new formulations on the problems where IPMs were first tuned.

---

## 8. Stated versus done (cross-check against 02)

| Stated (02) | Done (this file) | Verdict [inferred] |
|---|---|---|
| B1: theory and practice drive each other | A tiny floating-point check in nearly every theory paper, 1996–2006 (§1.1); theorems written to explain computations (P699); CUTEst ablation (2021); Netlib (2023). But the degenerate-NLP techniques never reached a released solver, despite deferrals in 2000, 2002 and 2006 (§4) | **Consistent at the level of illustration; inconsistent at the level of solver delivery for the NLP line** |
| 5.1 (2025): "computational experience on similar problems is a more reliable guide" | Standard test sets used throughout: netlib 1997, modified Hock–Schittkowski 2000, CUTEr 2006, CUTEst 2021, Netlib 2023, IEEE bus systems 2015 (§1.2) | Consistent |
| B7: weaker, realistic assumptions | Assumptions removed paper by paper, 1998–2005 (01, S2); degenerate CUTEr problems and dialled-in degeneracy chosen on purpose (§1.2) | Consistent |
| 5.3: honesty about what has not been shown | Favourable Δ flagged; "not ... a rigorous test"; "considerably worse overall"; failures tabulated; public corrigenda and errata (§1.2, §2) | Consistent, with strong evidence |
| 4.3: release software freely | PCx licensed for commercial use; OOQP gated by a request form (live page, updated 2016; GitHub copy since 2012); plain zip downloads for GPSR, SpaRSA, TVGP, LPS and GPU codes from 2007 (§4) | Practice changed over time, and the 2022 statement fits the later codes better than PCx or OOQP |
| B4: re-examine unsophisticated methods | CD stress tests; squared slacks on Netlib; Sℓ1LP chosen for warm starts; BB variants in GPSR (§1, §4) | Consistent |
| 6.2: books as distillation | Errata kept for all three books through 2008/2023; the 3rd-edition repository has been empty since 2022 | Consistent for maintenance; the new-edition plan has no visible output |
| 7.1: learned research style from colleagues | Adopted a competitor's test protocol (FFK 2002), took up referees' suggestions, gave named credit in changelogs | Consistent |

---

## Contradictions (kept, not reconciled)

1. **Stated research priority against follow-through on the NLP line.** Wright states repeatedly (02, B1) that practice and theory must drive each other. His conclusions of 2000 and 2006 say the practical embedding "remains to be investigated" or "remains to determine", yet no solver-level test was ever published. Both claims are documented; they are not reconciled here.
2. **Experiments added versus experiments removed in revision.** Yıldırım & Wright (2002) and Lewis & Wright (2015) gained numerical sections in revision. Xie & Wright (2021) lost its dictionary-learning experiments, and Xie & Wright (2024) lost a whole method. No stated policy explains the difference.
3. **"Free" software, stated and done.**
   - Oral history (2022): OOQP "also was was free" (transcript wording). The live OOQP page (updated 10/2/2016) still says "If you would like a copy of OOQP, go to the OOQP Request Form and fill it out", and it requires MA27 from the HSL Archive for the general sparse solver. A commented-out block adds that "OOQP's authors will be notified" when MA27 has been downloaded. The source has also been on GitHub (`emgertz/OOQP`) since 2012.
   - PCx: "freely available, but is not public domain software".
4. **Same paper, two emphases** (Curtis et al. 2021). The abstract says the method "retains the attractive practical behavior of classical trust-region Newton-CG". The paper's own §6 reports that the no-regularization variants, which lack the guarantee, "outperform the others" in Hessian-vector products. (01 and 02 record the 2021 against 2025 tension; this is the same tension inside one paper.)
5. **Hogwild! wording.** The paper says the RR locking optimization "results in nearly an order of magnitude increase in wall clock time for all problems that we discuss" (hogwildTR, p. 11). Read literally, the optimization made RR slower, which contradicts its stated purpose of fairness to prior art. It is kept verbatim; no erratum was found.
6. **Publication year of Wright & Jarre.** The papers page says "Mathematical Programming, Series A 84 (1998)". Crossref gives 1999 (vol. 84, pp. 357–373, 10.1007/s101070050026).
7. **PCx status.** The page says "PCx is no longer supported." A 2023 paper "resuscitated" it for experiments. This is not a logical conflict, but the two artifacts describe the code's status differently.

## Gaps

- **OpenReview not read.** It covers ICLR 2024 (Kwon, Kwon, Wright & Nowak, forum CvYBvgEUK9) and the NeurIPS 2022, 2023 and 2024 papers. The forum page returned a browser challenge and the API required login, and I did not bypass them. So there is no rebuttal evidence after 2014.
- **GitHub internals not read.** Commit histories, issues (OFDA has 1 open issue; OOQP has 4) and file trees were not visible, because github.com and api.github.com returned 403 through the proxy and the GitHub MCP is restricted to this session's repository. Only raw README and NEWS files and search metadata were read.
- **Source code of PCx and OOQP not opened.** Only changelogs, user guides and READMEs were read, so debugging practice inside the solvers is not documented. The TVGP and LPS archives were opened.
- **Referee reports for journal papers** are not public. The reasons for dropping the two-metric method (2103.15989) and the dictionary-learning experiments (1908.00131) are unknown.
- **Application-side computational papers not read in full.** Tenny, Wright & Rawlings (COAP 2004), Rao, Wright & Rawlings (JOTA 1998), the LSW sampling experiments beyond the setup, and the Kim & Wright results tables.
- **Journal versus preprint** was compared only through arXiv. SIAM and Springer final versions were not diffed against the ANL preprints.
- **No code found** for Royer & Wright (2018) or Royer, O'Neill & Wright (2020). Both papers are theory-only.
- **Talk videos not transcribed** (YouTube playlist; yt-dlp is blocked by YouTube's sign-in check, per 02). The Interior-Point Methods Online archive (Wayback) was blocked by the egress policy.
- **Not read**: the 1st-edition *Numerical Optimization* errata PDFs, and the student theses (Oberlin, Tenny, Lee, Liu, O'Neill), which belong to agent 04.
- **Not examined**, for time: arXiv revisions with large abstract changes in ML papers (2412.11003, 2411.14332, 1807.09146, 2111.01842).

## Sources

Primary unless marked (S). "Read" means the full text or the relevant section was read in this run.

1. Wright, S. J. Publications page, including the HTML comments (commented-out entries, revision dates), c. 1992–2011. https://pages.cs.wisc.edu/~swright/papers/ (P)
2. Wright, S. J. & Jarre, F. "The role of linear objective functions in barrier methods: Corrigenda", 22 Sep 2000. https://pages.cs.wisc.edu/~swright/papers/P485_corrections.ps; paper MP 84 (1999) 357–373, 10.1007/s101070050026 (P)
3. Tenny, M. J. "JOTA paper errata", 8 Aug 2000, for Rao, Wright & Rawlings, JOTA 99 (1998), 10.1023/A:1021711402723. https://pages.cs.wisc.edu/~swright/papers/P664-corrections.ps (P, observed)
4. Wright, S. J. *Primal-Dual Interior-Point Methods*: list of errors and typos, last updated 12 Dec 1999. https://pages.cs.wisc.edu/~swright/IPPD/siampage/typos.pdf; book 10.1137/1.9781611971453 (P)
5. Nocedal & Wright, "Corrections to Numerical Optimization, Second Edition", last updated 17 May 2008. https://pages.cs.wisc.edu/~swright/NumericalOptimization/NumOpt2-typos.pdf; book 10.1007/978-0-387-40065-5 (P)
6. Nocedal, J. "Numerical Optimization: Errata" (1st-edition printings), http://users.iems.northwestern.edu/~nocedal/book/errata.html (P; errata PDFs not read)
7. Wright & Recht, "Optimization for Data Analysis: Typos", 31 Jan 2023. https://raw.githubusercontent.com/wrightstephen/OptimizationForDataAnalysis/main/optml_typos.pdf; book 10.1017/9781009004282 (P)
8. GitHub search metadata for user `wrightstephen` (6 repositories: TRIPODS-EDUCATION, cs524, OptimizationForDataAnalysis, wrightstephen.github.io, ifds-research-expo, NumericalOptimization3rdEdition), via GitHub MCP search, 2026-09-28 (P)
9. README of `wrightstephen/NumericalOptimization3rdEdition`, 18 Jul 2022 (raw.githubusercontent.com) (P)
10. README of `wrightstephen/TRIPODS-EDUCATION`, 2017–2018 (P)
11. PCx home page, changelog (updated 1/10/06) and WSSMP results page. https://pages.cs.wisc.edu/~swright/PCx/ (P)
12. Czyzyk, Mehrotra, Wagner & Wright, *PCx User Guide (Version 1.1)*, OTC Technical Report 96/01, 3 Nov 1997. https://pages.cs.wisc.edu/~swright/PCx/doc/PCx-user.pdf; paper OMS 11 (1999), 10.1080/10556789908805757 (P)
13. OOQP home page and changelog (updated 10/2/2016). https://pages.cs.wisc.edu/~swright/ooqp/ (P)
14. Gertz & Wright, "Object-oriented software for quadratic programming", ACM TOMS 29 (2003) 58–81, 10.1145/641876.641880 (read) (P)
15. `emgertz/OOQP` README and NEWS (raw.githubusercontent.com); repository metadata via GitHub search (P)
16. Lee & Wright, GPU reconstruction page (updated 11/03/2008) and TR "Implementing Algorithms for Signal and Image Reconstruction on Graphical Processing Units", Sep 2008. https://pages.cs.wisc.edu/~swright/GPUreconstruction/ (P)
17. TVGP page, changelog and TVGP.v2.0 code archive (Test_TVGP.m, TV_GPBBsafe.m). https://pages.cs.wisc.edu/~swright/TVdenoising/; paper Zhu, Wright & Chan, COAP 47 (2010), 10.1007/s10589-008-9225-2 (P)
18. LPS page, changelog and LPS-v2.2 archive (README.txt, TestTables.m). https://pages.cs.wisc.edu/~swright/LPS/; papers: Shi, Wahba, Wright et al., Stat. Interface 1 (2008), 10.4310/SII.2008.v1.n1.a12; Wright SIOPT 22 (2012), 10.1137/100808563 (P)
19. "The Empirical Behavior of Sampling Methods for Stochastic Programming" companion site. https://pages.cs.wisc.edu/~swright/stochastic/sampling/ (P)
20. GPSR and SpaRSA pages (Figueiredo's site), http://www.lx.it.pt/~mtf/GPSR/ and http://www.lx.it.pt/~mtf/SpaRSA/ (P)
21. arXiv abstract pages and submission histories for 80 records (79 author-search results plus 0812.0423), and v1 abstract pages for the 56 multi-version records, fetched 2026-09-28 (P, metadata)
22. Wright, "Superlinear convergence of a stabilized SQP method to a degenerate solution", ANL/MCS-P643 (1997); COAP 11 (1998), 10.1023/A:1018665102534 (P)
23. Wright, "Modifying SQP for degenerate problems", ANL/MCS-P699 (rev. 2002); SIOPT 13 (2002), 10.1137/S1052623498333731 (read) (P)
24. Wright, "Constraint identification and algorithm stabilization for degenerate nonlinear programs", ANL/MCS-P865 / arXiv:math/0012209; MP 95 (2003), 10.1007/s10107-002-0344-8 (read, §6–7) (P)
25. Wright, "An algorithm for degenerate nonlinear programming with rapid local convergence", SIOPT 15 (2005) 673–696, 10.1137/030601235 (read, §6) (P)
26. Oberlin & Wright, "Active set identification in nonlinear programming", SIOPT 17 (2006) 577–605, 10.1137/050626776 (read, §4–5) (P)
27. Wright & Tenny, "A feasible trust-region sequential quadratic programming algorithm", SIOPT 14 (2004), 10.1137/S1052623402413227 (P); companion Tenny, Wright & Rawlings, COAP 28 (2004), 10.1023/B:COAP.0000018880.63497.EB (identifier checked, not read)
28. Yıldırım & Wright, "Warm-start strategies in interior-point methods for linear programming", SIOPT 12 (2002), 10.1137/S1052623400369235 (read, §6–7) (P)
29. John & Yıldırım, "Implementation of warm-start strategies in interior-point methods for linear programming in fixed dimension", COAP 41 (2008), 10.1007/s10589-007-9096-y (metadata only) (S)
30. Wright, "Modified Cholesky factorizations in interior-point algorithms for linear programming", ANL/MCS-P600; SIOPT 9 (1999), 10.1137/S1052623496304712 (read, §6) (P)
31. Wright, "Effects of finite-precision arithmetic on interior-point methods for nonlinear programming", arXiv:math/0103102; SIOPT 12 (2001), 10.1137/S1052623498347438 (read, §7) (P)
32. Linderoth & Wright, COAP 24 (2003), 10.1023/A:1021858008222, and "COAP 2003 Best Paper Award" note, COAP 29 (2004) 123–126 (note read) (P)
33. Linderoth, Shapiro & Wright, Optimization Technical Report 02-01 (rev. Sep/Oct 2002); Ann. OR 142 (2006), 10.1007/s10479-006-6169-8 (setup read) (P)
34. Lee & Wright, "Sparse Nonlinear Support Vector Machines via Stochastic Approximation", manuscript, Feb 2010. https://pages.cs.wisc.edu/~swright/papers/sncss.pdf (P)
35. Lee & Wright, ASSET draft (IEEE TPAMI template), Sep 2010, https://pages.cs.wisc.edu/~swright/papers/sncss_tpami.pdf; ICPRAM 2012, 10.5220/0003786202230228; arXiv:1111.0432 (P)
36. Figueiredo, Nowak & Wright, GPSR, IEEE JSTSP 1 (2007), 10.1109/JSTSP.2007.910281 (read, §III–IV) (P)
37. Wright, Nowak & Figueiredo, SpaRSA, IEEE TSP 57 (2009), 10.1109/TSP.2009.2016892 (read, experiments) (P)
38. Niu, Recht, Ré & Wright, Hogwild! TR / arXiv:1106.5730 (NIPS 2011) (read, §6–7) (P)
39. Wright, "Coordinate descent algorithms", arXiv:1502.04759; MP 151 (2015), 10.1007/s10107-015-0892-3 (read, §3.8) (P)
40. Curtis, Robinson, Royer & Wright, arXiv:1912.04365v3; SIOPT 31 (2021), 10.1137/19M130563X (read, §5–7) (P)
41. Royer & Wright, arXiv:1706.03131 / SIOPT 28 (2018), 10.1137/17M1134329; Royer, O'Neill & Wright, arXiv:1803.02924 / MP 180 (2020), 10.1007/s10107-019-01362-7 (checked for experiments; none) (P)
42. Xie & Wright, arXiv:2103.15989 v1 and v3; MP 207 (2024), 10.1007/s10107-023-02000-z (both versions read, structure and §5) (P)
43. Xie & Wright, arXiv:1908.00131 v1 and v4; J. Sci. Comput. 86 (2021), 10.1007/s10915-021-01409-y (structure compared) (P)
44. O'Neill & Wright, arXiv:1706.07993 v1 and v3; MP 176 (2019), 10.1007/s10107-018-1340-y (abstracts compared) (P)
45. Ding & Wright, arXiv:2310.01784; SIOPT 35 (2025), 10.1137/23M1608343 (read, §4–6) (P)
46. Lee & Wright, arXiv:2602.10470 (2026) (scanned for experiments) (P)
47. Wright, "Optimization in Theory and Practice", arXiv:2510.15734 v1 (17 Oct 2025) and v2 (2 Dec 2025) (full-text diff) (P)
48. Kim & Wright, arXiv:1405.0322; Optim. Eng. (2015), 10.1007/s11081-015-9292-z (intro and experiments setup read) (P)
49. Lewis & Wright, arXiv:0812.0423 v1/v2; MP 158 (2016), 10.1007/s10107-015-0943-9 (abstracts compared) (P)
50. NIPS 2014 reviews and author feedback, paper 1143, Lim & Wright, "Beyond the Birkhoff Polytope: Convex Relaxations for Vector Permutation Problems". https://proceedings.neurips.cc/paper_files/paper/2014/file/675731a0bb3936b988f8203106382076-Reviews.html (P for the rebuttal; reviewer text is observed)
51. NIPS 2013 reviews and author feedback, paper 1320, Sridhar et al., "An Approximate, Efficient Solver for LP Rounding". https://proceedings.neurips.cc/paper_files/paper/2013/file/2a50e9c2d6b89b95bcb416d6857f8b45-Reviews.html (P/observed)
52. NIPS 2017 reviews, paper 224, Lim & Wright, "k-Support and Ordered Weighted Sparsity for Overlapping Groups: Hardness and Algorithms". https://proceedings.neurips.cc/paper_files/paper/2017/file/13fe9d84310e77f13a6d184dbf1232f3-Reviews.html (S, observed)
53. Wright, "The Ongoing Impact of Interior-Point Methods", SIAM Conference on Optimization, Toronto, 20 May 2002, slides 34–40. https://pages.cs.wisc.edu/~swright/talks/siopt_talk_may02.pdf (P)
54. UW-Madison Oral History Program, interview 2179 (2022-10-04), transcript at `../sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt` (saved by agent 02; used only for statements about software development) (P)
55. `yue-xie/ProjectedNewton` repository metadata (GitHub search; created 2020-12-16, MATLAB, no README) (P)
56. Crossref REST API: DOI checks for every DOI in this file (S)
57. OpenAlex API (title searches for publication status: the GPU TR, sncss, John & Yıldırım, ASSET, the TV paper, Lewis & Wright, Kim & Wright, Ho-Nguyen & Wright 10.1007/s10107-022-01796-6) (S)
58. WebSearch (1 call): "Stephen J. Wright" erratum/corrigendum; led to source 6 (S)

Attempted and not read: OpenReview forum https://openreview.net/forum?id=CvYBvgEUK9 (browser challenge); OpenReview API (login required); github.com repository pages and api.github.com (403); Wayback copy of Interior-Point Methods Online (egress policy).
