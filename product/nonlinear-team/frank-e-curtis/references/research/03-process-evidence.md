# Frank E. Curtis: Process Evidence (what he actually does)

| Field | Value |
|---|---|
| Researcher | Frank E. Curtis (Lehigh University ISE; PhD Northwestern 2007 under Jorge Nocedal; Courant postdoc 2007–09; Lehigh since Aug 2009) |
| Dimension | Research agent 03 of 06: process evidence (code, experiment sections, early-versus-final versions, corrections, abandoned work) |
| Research date | 2026-09-28 |
| Sources consulted | 44 (38 primary, 6 secondary), listed under "Sources". Two more were attempted and blocked: the OpenReview profile page (bot check) and the OpenReview API (login required) |
| WebSearch calls | 1 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` held only `.gitkeep`; `private/` was not opened |
| Transcripts saved | none (no talk transcripts were produced in this pass) |
| Language | English (per team.json) |

**Tags.** [stated] = Curtis said or wrote it (README, paper prose, commit message, manual). [practice] = what the artifacts show he did (code, git history, file dates, tables, experiment design). [observed] = recorded by a third party (Ipopt maintainers, arXiv/Crossref metadata). [inferred] = my reading; the basis is given, and it must not be quoted as his view. (P) = primary source, (S) = secondary.

**Co-authorship caveat.** Almost every paper is co-authored and alphabetically ordered (see 01 §0). An experiment design in a joint paper is evidence of the *group's* practice. Where a git history shows who did what, I say so. Commits by `frank.e.curtis`, `frankecurtis` or `Frank E. Curtis` are attributed to him. Commits by students are labelled with their names.

**What was read.**
- **Git histories.** I cloned all ten public repositories under github.com/frankecurtis (NonOpt, StochasticSQP, PIPAL, SLQPGS, TRACE, AggQN, SCBFGS, QuasiCuttingPlane, Utilities, StochasticGradientDemo). I read their logs, READMEs, test scripts and selected diffs, plus the eight pull requests the GitHub search API returns for this user.
- **Legacy code releases.** I downloaded the five dated archives from the homepage software page (PIPAL 1.0 and 1.1; SLQP-GS 1.0, 1.1 and 1.2) and read their file dates and READMEs.
- **Paper versions compared.** I compared early and late arXiv versions of nine papers: 1708.00475 v1/v2/v4, 1708.02552 v1/v3/v5, 1712.10277 v1/v3, 1802.09592 v1/v3, 1803.09224 v1/v3, 1903.03471 v1/v3, 2005.07822 v1/v2, 2106.13015 v1/v2 and 1508.02452 v1/v2. For 1508.02452 I compared section headings only.
- **Experiment sections read.** I read these in full:
  - PIPAL (MPC 2012)
  - SQP-GS (SIOPT 2012)
  - Byrd–Curtis–Nocedal SIOPT 2010
  - the stochastic SQP arXiv v1 (2007.10525)
  - inexact TRACE (2204.11322 v1)
  - NonOpt (2503.22826)
- **Other sources.** The Ipopt 3.14 build files and ChangeLog; the errata page and the three corrigenda. I did not read any proofs, and I did not read final journal versions where these differ from the arXiv versions (paywalled).

**Relation to 01 and 02.** 01 dissected five signature works and listed candidate moves M1–M11. 02 collected his stated beliefs R1–R8. This file adds behavioural evidence and cross-checks it against them in §8 ("Stated versus done"). I do not repeat 01's per-paper numerics summaries except where new detail changes the picture.

---

## 0. Artifact timeline (the backbone of the evidence)

Dates are from archive file timestamps, git commits, arXiv submission histories, and the received/accepted lines printed on papers. All are [practice] (P) unless marked.

| Date | Event | Source |
|---|---|---|
| 2009-01-13 | Ipopt 3.5.5 ships an "undocumented version of inexact method" (the inexact interior-point line of SW1) | Ipopt ChangeLog [observed] (S) |
| 2009-10-28 | SLQP-GS 1.0 packaged. Its README cites "A Robust Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization, submitted to SIAM Journal on Optimization, 2009". The code handles inequality constraints only | SLQP-GS_1.0.tgz |
| 2009-12-15 | SQP-GS paper "Received by the editors" (SIOPT) | Curtis–Overton 2012, footnote |
| 2010-06-21 | PIPAL 1.0 README "Last revised: 21 June 2010". It cites Lehigh ISE TR 10T-006, "A Penalty-Interior-Point Method for Large-Scale Nonlinear Optimization … (Article submitted to Mathematical Programming.)". Optimization Online posting of the same date | PIPAL_1.0.tgz; optimization-online.org/2010/06/2661 |
| 2011-02-01 | SLQP-GS 1.1 packaged. The README says the paper is "in second round of review for SIAM Journal on Optimization, February 2011". The code now handles equalities and adds `run_steering_check.m` | SLQP-GS_1.1.tgz |
| 2011-04-26 | PIPAL 1.1 zip, rewritten object-oriented, all files stamped 22:20 that day. The MPC paper was "Received: 26 April 2011" | PIPAL_1.1.zip; Curtis 2012 p. 181 |
| 2011-11-07 | SLQP-GS 1.2, object-oriented rewrite; the README says "in third round of review" | SLQP-GS_1.2.zip |
| 2012-02 / 2012-04 | SQP-GS accepted (SIOPT); PIPAL accepted 11 Apr 2012 (MPC) | papers |
| 2017-08-01 → 2017-09-27 | 1708.00475 v1 has 19 pp. and no numerics. v2 (IMA JNA template, 29 pp.) adds "Algorithm Instance, Implementation, and Numerical Results" on CUTEst | arXiv versions |
| 2017-08-08 → 2018-03-15 | 1708.02552 v1 abstract: "The results of numerical experiments are forthcoming." v3 adds §5 "Numerical Experiments" (C++ implementation) | arXiv versions |
| 2019-06-25 | NonOpt repository created; commit "Added all files from previously used repository." | NonOpt git |
| 2019-07-15 | AggQN repository (arXiv v1 was 8 Mar 2019). A student commit reads "Code gave out good results on August 1st, 2019" (Baoyu Zhou) | AggQN git |
| 2020-01-11 | AggQN commit "Rewrite of files for first MPA submission." arXiv v2 followed on 14 Jan 2020 | AggQN git; arXiv |
| 2020-04-16 → 2020-04-23 | QuasiCuttingPlane: 6 commits in 8 days, then nothing. The README says "A paper is forthcoming." | QuasiCuttingPlane git |
| 2020-07-20 / 2020-07-31 | Stochastic SQP arXiv v1, then the StochasticSQP repository created 11 days later | arXiv; StochasticSQP git |
| 2021-03-25 | Student PR #3, "Add inexact algorithm" (Baoyu Zhou) | StochasticSQP PR #3 |
| 2021-06 → 2021-07 | Curtis's cleanup commits. Then 2106.13015 (24 Jun) and 2107.03512 (7 Jul) go to arXiv | StochasticSQP git; arXiv |
| 2021-07-06 → 2021-07-13 | PIPAL, SLQPGS and SCBFGS moved to GitHub, with the old versions replayed as commits "Version 1.0", "1.1", …. The Utilities repo (created Oct 2020) receives PaperStarter and the shared LaTeX files, mostly committed by D. P. Robinson | git; GitHub API created_at |
| 2022-01-21 | Student PR #4 (Minhan Li's dissertation algorithm for general constraints) merged into a side branch `inequality`, not `master` | StochasticSQP remote refs |
| 2022-04-24 / 2022-05-01 | Inexact-TRACE arXiv 2204.11322, then the TRACE repository a week later ("This software is under development.") | arXiv; TRACE git |
| 2025-03-28 | NonOpt paper on arXiv (tag v2.0 = 2025-04-05) | arXiv; git tags |
| 2025-12-15 / 2026-04-14 | Commits "update for MPC round 1 revision" and "MPC Submission, Revision 2" (tag v2.1) | NonOpt git |
| 2026-07-19 → 2026-07-31 | Code-quality pass driven by a CLAUDE.md "working brief", then v2.2 (CLAUDE.md deleted in the v2.2 commit) | NonOpt git |

---

## 1. Layer 4: experiments and execution (the bulk of the evidence)

### 1.1 Test-set construction

**PE1. Mechanically built pathological variants of a standard set, used to isolate the claimed feature.** [practice] (P)
- PIPAL 2012: degenerate and infeasible Hock–Schittkowski variants (01 SW2).
- Burke–Curtis–Wang–Wang, SIOPT 2020 (10.1137/18M1176488; arXiv 1803.09224): the revised version adds an infeasible set "As in [3], we modified the 126 CUTEr Hock-Schittkowski (hs) problems by adding bound constraints x1≤ 0 and x1≥ 1 to make all hs problems infeasible" (v3 §6.2). The first version (v1, Mar 2018) tested only the feasible HS set.
- Byrd–Curtis–Nocedal 2010 (10.1137/080738222) made `robot` infeasible by adding the constraint c4(x) = c1(x)² + 1 (§5, Example 2), and built two-variable infeasible toys (`unique`, `isolated`).
- Era: 2008–2020, Matlab with CUTEr/AMPL; problems small (HS).

**PE2. Filter the benchmark on the theory's assumptions, and encode the filter in code.** [practice] (P)
- Stochastic SQP v1 (arXiv 2007.10525, §4): of 123 CUTE equality-constrained problems it kept those where "(i) f is not a constant function, (ii) n+m≤ 1000, and (iii) the LICQ held at all iterates in all runs of all algorithms that we ran". That left 49.
- The repository encodes filter (i) as a method, `constantObjective`, which evaluates f at 10 random perturbations of x0 (StochasticSQP `problems/ProblemCUTEst.m`).
- The Utilities repo holds `CUTEst2Matlab/checkConstraintsType.m`, which sorts every CUTEst problem into `list_unconstrained.txt`, `list_equality_constrained.txt` and `list_generally_constrained.txt`.
- [inferred] Condition (iii) conditions the test set on the outcome of the runs. It keeps the theory's assumption true on the evidence set, but it also removes the problems where the method might break.

**PE3. Report every excluded problem, by name and reason.** [practice] (P)
- Inexact regularized Newton (IMA JNA 2019, 10.1093/imanum/dry022, arXiv 1708.00475 v4 §5.2) lists the removals:
  - FLETCBV2 ("terminated at the initial point");
  - five problems "due to a function evaluation error or our memory limitation of 8GB";
  - nine problems where "neither algorithm terminated within our time limit";
  - four where neither succeeded, each with the failure mode of each code.
- PIPAL 2012 removed problems whose Newton matrix had ≥ 20,000 nonzeros "due to memory limitations in Matlab". PIPAL 1.2 hard-codes this as `nnz_max = 2e+04`.
- Era: 2010–2018; Matlab memory and 8 GB caps shaped the test sets.

**PE4. Keep one test set for years, and make it the house set.** [practice] (P)
- The same ten scalable nonsmooth problems (Haarala–Miettinen–Mäkelä: MaxQ, MxHilb, ChainedLQ, ChainedCB3 1/2, ActiveFaces, BrownFunction 2, ChainedMifflin 2, ChainedCrescent 1/2) run through three papers:
  - SVANO (IMA JNA, 10.1093/imanum/drz008; arXiv 1708.02552 v5 §5, n = 50);
  - Curtis–Li (IJOO 2022, 10.1287/ijoo.2022.0073; arXiv 2005.07822, n = 1000, plus ten TEST29 problems);
  - NonOpt (MPC 2026, 10.1007/s12532-026-00322-5, the same 20 problems at n = 1000).
- The NonOpt repository ships these 20 problems as C++ classes (`NonOpt/problems/`).
- Curtis–Li v2 says of the set that it is "a set of 20 test problems for which LMBM has been tuned".
- See Contradiction C3.

**PE5. Build the benchmark from an application domain when the standard sets do not test the claim.** [practice] (P) This is already documented by 01 (the 200-problem controller-design set, BFGS-SQP 2017). The SQP-GS paper adds a design note: "The first problem is somewhat contrived … All the remaining problems are derived from real applications" (Curtis–Overton 2012 §5).

### 1.2 Baselines and fairness devices

**PE6. Implement the competitor yourself, inside the same code base, with shared parts, so that the comparison varies one thing.** [practice] (P)
- iR Newton versus "iARC": "for comparison purposes, one following the ARC algorithm … We refer to … the latter as iARC" (1708.00475 v4 §5). Both use the same Lanczos/GALAHAD RQS machinery and the same parameter table.
- i-TRACE versus TRACE versus ARC: "all of the algorithms were implemented in a single software package in Matlab" and "For a fair comparison, the implementations both involve the auxiliary sequence {∆k}" (2204.11322 v1 §4.1). ARC's inexactness parameter κθ was run at the same three values as i-TRACE's ξ2.
- GS-exact versus GS-inexact versus GS-inexact-agg: GS-exact is the same code with the QP solved to KKT error 10⁻¹⁰, "every aspect of this implementation is the same as that of GS-inexact" (2005.07822 v2 §4).
- Deterministic "SQP Adaptive" versus "SQP Backtracking" (2007.10525 v1 §4.1). The two differ only in the step-size rule.
- Era: 2017–2022, Matlab framework with shared classes (§5, PE24).

**PE7. Ablation by switching one component off.** [practice] (P)
- SQP-GS: the same code with p = 0. "In fact, similarly poor results were obtained for all our remaining test problems when no sampling was performed (i.e., when p = 0), providing strong evidence that the GS procedure is critical for the effectiveness of our approach." (Curtis–Overton 2012 §5, Fig. 5.2)
- AggQN revision: a third algorithm was added that uses the same pair-selection rule but deletes the pair instead of aggregating it. "Consequently, the comparison between the second and third algorithms shows the effect of aggregation itself, rather than only the difference between removing the oldest versus some other historical pair in an L-BFGS scheme." (1903.03471 v3 §4.2; not in v1.)
- Together with the ires/isqp design of 2008 (01, M3), this makes three independent instances over 14 years.

**PE8. Adopt the incumbent's engineering so that the comparison tests the idea, not the plumbing.** [practice]+[stated] (P)
- PIPAL imported IPOPT's bound relaxation, initial-point push, gradient-based scaling (gmax), minimum parameter values and function-evaluation-error handling. In the paper's words, "we have adopted this modification of the initial data to have a fairer comparison with IPOPT" (Curtis 2012 §4.1.5).
- **New code evidence.** Several of these features are absent from PIPAL 1.1, which was packaged on the submission day (26 Apr 2011). They are present in PIPAL 1.2:
  - second-order correction (`Acceptance.secondOrderCorrection`);
  - rejection of trial points after a function-evaluation error (`z.err`);
  - `grad_max` = 1e+02, IPOPT's value (1.1 had 1e+00);
  - the `nnz_max` cap.
  
  All of these are described in the published paper.
- [inferred] They were added during the year of review (Apr 2011 → Apr 2012). Whether referees asked for them is not documented.

**PE9. Be generous to the baseline, and state the handicap in numbers.** [practice] (P)
- Stochastic SQP v1 §4.2: "We tuned the value of τ individually for each problem instance for “Stochastic Subgradient.”" Each baseline run got 10× the iterations, over 11 stepsizes: "Overall, this means that for each problem, “Stochastic Subgradient” was given 110 times the number of iterations that were allowed for “Stochastic SQP.”"
- The proposed method was handicapped too: "we set Hk = I for all k for fairness of comparison with the (first-order) subgradient method".
- Both methods were given identical Lipschitz estimates: "This process was done so that L and Γ were the same for both methods for each problem."

**PE10. Equalize the tuning effort, and make the protocol stricter under revision.** [practice] (P)
- TRish (Curtis–Scheinberg–Shi, IJOO 2019, 10.1287/ijoo.2018.0010).
- v1 (Dec 2017) grid-searched both methods and chose "the parameter settings that lead to be best average testing accuracy over the five runs". As printed, the TRish selection α = 5 lies outside the stated shared grid {1, 10, 100} [practice; a reporting inconsistency].
- v3 (Jun 2018) adds §4.1 "Algorithm Parameter Selection", with 60 settings per method and matched stepsize ranges "so that neither algorithm had an advantage in terms of the range of the stepsizes". It also states: "We took care to make sure that the tuning procedure for TRish did not require more effort than the tuning used for the SG method that we have for comparison purposes."
- In both versions the selection criterion is testing accuracy. I found no separate validation split in the parts read [inferred from the parts read].

**PE11. Time-matched head-to-head against an external state-of-the-art code, rebuilt during revision.** [practice] (P)
- Curtis–Li, v1 (May 2020): LMBM was run with default and with modified termination. The modified run "effectively turned off the stopping conditions based on differences in objective values", because "with its default settings, only one of the 20 test problems (namely, MaxQ) is indicated as “solved” at termination". GS-inexact-agg used dense BFGS and was often an order of magnitude slower in CPU time (Table 6, e.g. MaxQ 1.45 s against 26.01 s).
- Curtis–Li, v2 (Aug 2021, "20T-009-R1"):
  - the modified-termination variant is dropped;
  - GS-inexact-agg switches to L-BFGS with history 50 "so that the algorithm would be more similar to LMBM";
  - GS-inexact-agg gets a CPU limit equal to max{LMBM's average time over 10 runs, 1 s};
  - both codes are averaged over 10 runs.
- The v2 verdict: "one finds that the results are generally comparable. LMBM yields lower values for some problems while GS-inexact-agg yields lower values for a few others."
- A matching NonOpt commit, 2021-08-06, reads "Objective tolerance uses unscaled objective.  IJOO."

**PE12. Stop comparing with other codes once you judge the field empty.** [practice]+[stated] (P)
- NonOpt 2025 §6: "However, since NonOpt performed favorably in these comparisons, LMBM is no longer under active development, and we are not aware of any other open-source software packages under active development for general-purpose locally Lipschitz minimization, our experiments in this paper focus exclusively on experiments with NonOpt only."
- Instead the paper compares internal options: the new IPM QP solver against the dual active-set solver, and "speed" against "accuracy" option profiles.
- See C2 and C3.

### 1.3 Parameters, randomness, repetitions

**PE13. Parameters are tuned on the evaluation set and the paper says so.** [practice]+[stated] (P)
- SQP-GS 2012 §4: "We use values for the static input parameters as indicated in Table 4.1, as we found them to yield the best results for the experiments in section 5." Also: "The remaining values were decided upon during the course of our experiments."
- PIPAL 2012 §4.1.6: "The input parameters for our implementation have been set as those values that we found to yield the best results in our numerical experiments, or, in the cases of ξμ and gmax, have been set as those values used in IPOPT."
- iR Newton 2019: "We chose these values as ones that worked well on our test set for both implemented algorithms."
- The same paper leaves out enhancements to avoid more tuning: "for simplicity and to avoid the need for additional parameter tuning, we did not include such enhancements in our implemented algorithms."
- None of these papers reports the time spent tuning. See C1.

**PE14. Parameters drift between the released code and the paper.** [practice] (P)
- PIPAL's constants changed across versions:
  - `mu_factor` 1e-01 → 5e-01 → 1e-01 (with a new `mu_factor_exp` = 1.5);
  - `rho_trials` 4 → 4 → 8;
  - `mu_trials` 10 → 10 → 4;
  - `shift_max` 1e+04 → 1e+04 → 1e+08;
  - `pivot_thresh` 1e-12 → 5e-01 → 5e-01.
- The paper describes five candidate values each for ρ and μ (the sets Rk and Mk, §4.1.2). Neither released version matches both counts exactly.
- Theory versus practice is flagged in the text: "A sample size of p = n+1 is all that is required in our analysis, but as in [8], we found that the choice p = 2n yielded faster convergence" (SQP-GS §4).

**PE15. Randomized methods: multiple starting points or runs; seeds fixed in code; one lapse.** [practice] (P)
- SQP-GS 2012: "For each problem we ran our implementation with 10 different starting points". The reason given: "since we found that the algorithm behaved consistently even for different starting points, we provide the results for these runs with the idea that they more clearly indicate the robustness of the approach."
- The SLQP-GS 1.1 README (2011) adds a user instruction: "The states of Matlab's built-in rand and randn functions should be set prior to a run to obtain reproducable results."
- SCBFGS calls `rng('default')`. StochasticSQP threads a seed through `ProblemCUTEst` (`rng(P.seed)` before each noisy gradient). Stochastic SQP v1 used 10 runs per problem and noise level. Curtis–Li v2 used 10 runs.
- **The lapse:** SVANO v5 §5, "In each of our experiments, we show the results of a single run for each problem. In each case, we have observed that the results we provide are representative of the algorithm’s average performance in general." This is for a randomized variant (SVANO-GS). See C4.
- NonOpt MPC round-1 revision (Dec 2025) adds `rng(19970830)` to `mpc/addNoiseToImage.m`. [inferred] The image-noise experiment was not seeded before review.

**PE16. Pick the metric that exposes the mechanism, and say which one is "the main measure".** [practice]+[stated] (P)
- iR Newton reports iterations and Hessian-vector products, and points to the latter "as the main measure of improved performance". It explains the mechanism: CG can recover H·s by linear combination (1708.00475 v4 §5.2).
- Curtis–Li counts QP-solver iterations: "a rough proxy for computational effort … we found it to be the best measure for comparison, as opposed to CPU time which can vary" (2005.07822 v2 §4.1).
- Stochastic SQP v1 reports stepsize-choice frequencies: "αk was chosen less than one 40.9% of the time, equal to one 41.8% …".

**PE17. Check empirically that the theory's conditioning event actually happens.** [practice] (P)
- Stochastic SQP v1 §4.2: the event under which the analysis holds occurred "100% of the time in the last 100 iterations", and in 99.10–99.92% of all iterations. The paper concludes: "This provides evidence that the theory offered under the event (25) is relevant in practice."
- TRish v3 reports how often each step case occurred ("case 1 occurred in approximately 27% of the iterations …").
- PIPAL tabulates the final penalty-parameter value over twelve possible values to diagnose update behaviour (Curtis 2012 Table 3; 01).

**PE18. Before a benchmark, show one example at iteration level.** [practice] (P) SQP-GS shows ‖xk − x*‖ curves for 10 runs on a nonsmooth Rosenbrock variant. BFGS-SQP 2017 plots per-iteration objective and violation for all four codes on one random controller-design example before the RMP benchmark. Byrd–Curtis–Nocedal 2010 prints full iteration tables on three toy problems to display the superlinear rate to an infeasible stationary point.

### 1.4 Debugging and code discipline

**PE19. Debug the test problems as well as the solver: build a derivative checker, then make it a standard strategy.** [practice]+[stated] (P)
- NonOpt commits, in order:
  - 2019-10-24 "Initial code for derivative checker.";
  - 2019-11-22 "Fixed derivatives on two test problems.  Made sure that derivative checker uses scaling of objective.";
  - 2021-05-16 "Release candidate 2. Derivative checker now a strategy."
- The manual (revised for MPC round 1, Dec 2025) says of the checker: "it is the best first step for debugging!"
- QuasiCuttingPlane (2020) also has a `checkDerivatives.m` method.

**PE20. Defensive exits that ask the user to report "impossible" states.** [practice]+[stated] (P) The string "This wasn't supposed to happen!" occurs on six lines of NonOpt's `src/*.cpp`, in EXIT messages. The round-1 manual text asks users hitting one to "contact Frank E. Curtis, since that was not supposed to happen!".

**PE21. Students prototype and debug; the PI consolidates.** [practice] (P)
- StochasticSQP PR #3 (Baoyu Zhou, merged 2021-03-25) carries a debugging diary in its squashed commit messages:
  - "Fix some bugs.  TT3 is triggered so many times...";
  - "errors in EQP algorithm found...";
  - "add one more checking termination test as a safeguard...";
  - "add safeguard on L";
  - "change iteration limit from 1000 to 5000";
  - "fix almost all bugs...";
  - "have run this experiment".
- Curtis then commits, in turn:
  - "Cleaned code with inexact subproblem solves." (2021-06-20);
  - "Adding implementation of no-LICQ and inexact versions." (2021-07-09, 103 files changed);
  - "Merged step decomposition and inexact algorithms." (2021-07-23).
  
  He also replaces the bundled MINRES copy with patch instructions ("Removed MINRES code.").
- The same pattern holds in AggQN (student commits in 2019, then "Rewrite of files for first MPA submission.") and in NonOpt ("Merged Minhan's inexact GS branch.", then "Restructured directories in advance of public release.").
- [inferred] This matches 01's M11 ("the PI writes the prototype"). The finer picture: the student writes the first working version, and Curtis rewrites it into the house framework before the paper and the public release.

**PE22. Code-quality pass with an AI coding agent, recorded in a working brief (2026).** [practice] (P)
- In July 2026 NonOpt gained a `CLAUDE.md`: "This file gives Claude Code the context and task list to improve NonOpt. It summarizes a prior review; verify each item against the current source before acting, since line numbers may have shifted."
- It is a prioritized list (HIGH, MEDIUM, LOW, INVESTIGATE) with a verification rule: "Prefer making one change, rebuilding, and testing before moving on."
- The work it drove:
  - a Linux build fix (`std::isnan`);
  - a test-suite exit code that had masked failures;
  - `-O3` builds;
  - reconciling Cholesky tolerance units between two code paths;
  - guarding divisions;
  - hoisting 15 duplicated methods into a base class. This refactor was "Verified via full clean Makefile + CMake rebuilds and byte-for-byte identical `testQPSolver` output (same iteration counts and KKT errors) before/after";
  - CMake and CI;
  - an investigation showing that a QP test failure depended on reference BLAS rather than the platform (see C8).
- Deviations from the review were recorded with reasons ("wanted to avoid a third round of changes to a function already touched twice for correctness"). CLAUDE.md was deleted in the v2.2 commit (2026-07-31).
- Era: senior professor, after acceptance, maintaining a solver.
- [inferred] The review happened after the MPC paper's experiments. The build had been debug-only (`-g`, no `-O`), so the paper's CPU times (NonOpt 2.0) came from an unoptimized build. The paper does not report the build flags [not checked in the paper text].

### 1.5 Reproducibility packaging

**PE23. Ship a reproduction directory with the paper, including raw outputs and runtimes.** [practice] (P)
- NonOpt `mpc/README` maps each paper section to an executable and its option file, states expected runtimes ("around 11000 seconds (around 180 minutes, or 3 hours)"), names the machine ("Macbook Pro … Apple M1 Pro chip and 16GB of memory"), and notes that the LaTeX tables were generated: "The contents of these files were copied and pasted to generate the tables of results that are provided in the paper".
- All 120 per-run output files are committed. "MPC Submission, Revision 2" regenerated all of them, together with the figures and images.
- Earlier practice was thinner. SCBFGS ships one dataset (rcv1) and one driver. PIPAL 1.0 shipped a README with every parameter and every output column documented.
- Era: MPC requires code review; the 2025 packaging is the most complete.

---

## 2. Layer 5: judging results, corrections, and how revision changes a paper

**PE24. Theory first on arXiv, numerics added before or during review.** [practice] (P)
- Pattern across papers (arXiv version sizes and section lists):

| Paper | Early version | Later version | Change |
|---|---|---|---|
| Inexact regularized Newton (IMA JNA 2019, 10.1093/imanum/dry022) | v1 2017-08-01, 19 pp., no numerics | v2 2017-09-27, 29 pp.; v4 2018-03-15, 31 pp. | CUTEst experiments added in v2; ARC/TRACE-as-special-cases section added by v4 (acknowledges "anonymous referees") |
| SVANO (IMA JNA, 10.1093/imanum/drz008) | v1 2017-08-08: "The results of numerical experiments are forthcoming." | v3 2018-03-15 → v5 2019-02-02 | C++ implementation and §5 added |
| ADMM multiaffine (OMS 2020, 10.1080/10556788.2019.1683553; student-led by W. Gao) | v1: "26 pages, 0 figures" | v3: "37 pages, 7 figures" | experiments added (arXiv comment field) |
| Penalty updates within the QP solver (SIOPT 2020, 10.1137/18M1176488) | v1 2018-03: feasible HS only | v2/v3 2020-02 | SQuID comparison and infeasible HS set added |
| L-BFGS aggregation (MP 2022, 10.1007/s10107-021-01621-6) | v1 2019-03: simulated demonstrations | v3 2020-08 | CUTEst adaptive L-BFGS algorithm and single-component ablation added (PE7) |
| TRish (IJOO 2019) | v1 2017-12 | v3 2018-06 | parameter-selection section and equal-effort tuning (PE10) |
| GS inexact (IJOO 2022) | v1 2020-05 | v2 2021-08 "20T-009-R1" | LMBM comparison redesigned (PE11) |
| Rank-deficient stochastic SQP (MOR 2024, 10.1287/moor.2021.0154) | v1 2021-06, 31 pp. | v2 2023-03, 42 pp. "21T-013-R1" | numerics unchanged in structure. v2 adds an Appendix B with "formal results stated and proved" for §4.3 (v1 had only Appendix A) |

- [inferred] Curtis posts the analysis as soon as it is complete. Evidence that a practitioner would accept (CUTEst runs, a comparison with a state-of-the-art code, an ablation) is often added at submission or at referees' request. Revisions are tracked with a Lehigh ISE report number plus "-R1".

**PE25. Credit outside correction openly.** [practice] (P)
- TRish v3 acknowledgments: "The authors would like to thank Chaoxu Zhou of Columbia University for his valuable assistance in correcting errors in an earlier version of this manuscript … In particular, one anonymous referee suggested a proof for Lemma 3.2, which greatly improved the analysis."
- SQP-GS thanks Kiwiel, "whose careful, generous, and insightful comments helped to improve the convergence analysis" (01).

**PE26. Corrigenda: restate the result, give the full corrected proof, say how much it matters, add no narrative.** [practice] (P)
- The three corrigenda (01 §4) each open with a single line ("A corrected proof of Lemma 4.9 from the published paper is provided below."; "A corrected statement of Corollary 3.14(a) …"). Each then gives the full mathematics.
- Only the TRACE note grades the error: "the inequality in the published paper is correct, but not as tight as it could have been".
- None says how or by whom the error was found. The Corollary 3.14 corrigendum heads its restated result "Lemma 3.14" [minor inconsistency in the corrigendum itself].

**PE27. Calibrated claims in results prose.** [practice] (P)
- Stochastic SQP v1 §4.1: "We do not claim that “SQP Adaptive” is as efficient as “SQP Backtracking” since, as has been verified by others in the literature, the line search scheme is very effective across a broad range of problems."
- i-TRACE claims only that it "performs at least as well as arc". In its profiles "(We limit the horizontal axis to τ = 20 so the differences between the graphs can be seen more clearly.)"
- Curtis–Li v1: "(To be fair, there also remain problems for which the solution obtained by GS-inexact-agg is not as good.)"
- Profiles are restricted to commonly solved problems, with success counts reported separately. iR Newton even drops three problems where only *its own* method succeeded: "We feel that this gives a fairer comparison with respect to the problems on which both algorithms were successful."

**PE28. Defer full benchmarking explicitly when the implementation is not ready.** [stated] (P) Byrd–Curtis–Nocedal 2010 §4: "A numerical exploration of the performance of our penalty SQP method on a standard collection of feasible and infeasible problems is outside the scope of this paper as it requires a sophisticated software implementation of the algorithm." The PIPAL paper (2012) supplied a version of that exploration for the penalty-interior-point variant, not for this SQP method [inferred link].

---

## 3. Layer 6: expression (writing and packaging habits)

**PE29. Titles are narrowed during review.** [practice] (P)
- "A Robust Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization" (SLQP-GS 1.0 README, 2009) became "A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization" (SIOPT 2012).
- "A Penalty-Interior-Point Method for Large-Scale Nonlinear Optimization" (PIPAL 1.0 README, TR 10T-006, 2010) became "A penalty-interior-point algorithm for nonlinear constrained optimization" (MPC 2012).
- In both cases the adjective the evidence could not fully carry ("Robust"; "Large-Scale" for a Matlab code that dropped problems at 20,000 nonzeros) disappeared. [inferred reason; the reason is not documented]

**PE30. Scope in the code runs ahead of the paper's exposition.** [practice] (P) SLQP-GS handled equality constraints from 1.1 (Feb 2011). The published paper keeps "only inequality constraints in (1.1)" "For ease of exposition" (Curtis–Overton 2012 §1).

**PE31. Standardized paper scaffolding shared with the main collaborator.** [practice] (P)
- `Utilities/PaperStarter` (July 2021, with D. P. Robinson) generates a paper skeleton. It holds journal class files for SIOPT, MP, IMA JNA, COAP and Optimization Letters, plus a Lehigh ISE technical-report format.
- `LaTeX/dpr_fec.bib` holds 1,821 shared bibliography entries, and `dpr_fec.sty` holds shared macros.
- The Utilities README says: "The code is open source, but time has not been spent on documenting it.  Use at your own risk."
- [inferred] Every paper exists as a Lehigh technical report and a journal version from one source.

**PE32. Release labelling is candid.** [practice] (P)
- READMEs say "It has only moderately been tested" (PIPAL 1.2, SCBFGS 1.0, SLQPGS 1.2) and "This software is under development.  Please check back later." (StochasticSQP, TRACE).
- The software page calls these codes "prototype" and invites bug reports (01, 02).
- The candour extends to unfinished promises (§4).

---

## 4. Failures, abandoned, redirected and unfinished work (behavioural record)

| Item | What the artifacts show | Source | Tag |
|---|---|---|---|
| PIPAL's first venue | June 2010 README: "(Article submitted to Mathematical Programming.)". Published in MPC, received 26 Apr 2011, with fully rewritten code packaged that day | PIPAL_1.0.tgz; Curtis 2012 | [practice] (P). The MP outcome (rejection or withdrawal) is **not documented**; a redirect is [inferred] |
| SQP-GS review | At least three review rounds (README 1.1 "second round", 1.2 "third round"); about 26 months from receipt to acceptance | SLQP-GS archives | [practice] (P) |
| PDAS for isotonic regression and trend filtering (Curtis & Han, arXiv 1508.02452) | v1 Aug 2015, v2 Apr 2016. Still listed only under "Technical Reports" in the 2026 CV; no DOI in Crossref | arXiv; CV; Crossref | [practice]; abandoned or unpublished [inferred] |
| QuasiCuttingPlane | A one-week Matlab probe (Apr 2020): subgradient baseline against a learned quasi-cutting-plane solver (`runExperiment` plots `fsub` against `fqcp`). The README says "A paper is forthcoming."; no such paper in the CV, DBLP or arXiv lists by 2026 | QuasiCuttingPlane git | [practice]; dropped [inferred] |
| AggQN C++ | The README says "(An implementation in C++ is forthcoming.)". The C++ folder holds only Options/Reporter/Vector infrastructure, untouched since Aug 2020 | AggQN git | [practice]. Matches 02's "Preliminary results" slide seen in 2019 and 2024 |
| StochasticSQP inequality support | README: "*Functionality for solving problems with inequality constraints is under development.*" (since 2020). The student's dissertation implementation (PR #4, Jan 2022) sits on branch `inequality`; `master` is unchanged since 2021-07-23. The inequality paper was published anyway (SIOPT 2024, 10.1137/23M1556149) | StochasticSQP refs | [practice] (P) |
| TRACE public code | The 2017 MP paper had no numerics. The GitHub TRACE code is a 2022 rewrite (copyright Curtis, Robinson, Wang), still "under development". Its AUTHORS file reads "The main author of StochasticSQP is:", which shows it was copied from the StochasticSQP template | TRACE git | [practice] (P) |
| Inexact IPM in Ipopt | Shipped in 2009 as an "undocumented version of inexact method". In Ipopt 3.14 it remains behind `--enable-inexact-solver`, "EXPERIMENTAL! (default: no)", and requires Pardiso from pardiso-project.org. The implementation files are authored by A. Wächter (IBM, 2008). The homepage still says "Please use the Ipopt option inexact_algorithm yes" | Ipopt source and ChangeLog; software page | [observed] (S) + [stated] (P) |
| Unseeded experiment | The image-denoising noise was seeded only in the round-1 MPC revision | NonOpt commit ca51558 | [practice] (P) |
| Masked test failures | Until July 2026 the NonOpt test driver returned 0 regardless of results, and the build had no optimization flags | CLAUDE.md tasks 2–3; commit 298a0c3 | [practice] (P) |

---

## 5. Layer 7: research organisation visible in the artifacts

**PE33. One house architecture, carried across 15 years and two languages.** [practice] (P)
- 2011: the object-oriented rewrites of PIPAL and SLQP-GS use the same classes: `Input`, `Iterate`, `Direction`, `Acceptance`, `Parameter`, `Output`, `Counter`.
- 2019–2022: the Matlab frameworks (StochasticSQP, TRACE) use `Problem`, `Point`, `Options`, `Reporter`, `Quantities`, `Strategies`/`Strategy`, with one abstract class plus concrete subclasses per algorithmic choice. Examples: `DirectionComputationEQP`, `DirectionComputationSubgradient`, `StepsizeComputationAdaptive`, `StepsizeComputationConservative`, `LipschitzEstimationFiniteDifference`.
- NonOpt (C++) follows the same pattern: `DirectionComputation{CuttingPlane,Gradient,GradientCombination}`, `QPSolver{DualActiveSet,InteriorPoint}`, `LineSearch{Backtracking,WeakWolfe}`, `Termination{Basic,SecondQP}`, `ApproximateHessianUpdate{BFGS,DFP}`, `DerivativeChecker`.
- [inferred] Variants of an algorithm are strategy objects, which is what makes the one-component baselines of PE6 and PE7 cheap. The NonOpt paper states the aim: "written to be extensible" (02 §7.5).

**PE34. Timing of code relative to papers.** [practice] (P)
- 2009–2012: code releases are timed to submission and review rounds (SLQP-GS 1.0 before submission; PIPAL 1.1 on submission day).
- 2019–2022: public repositories are created within days *after* the arXiv posting (StochasticSQP +11 days, TRACE +7 days).
- 2021: a batch migration of legacy code to GitHub, with release histories replayed as commits.

**PE35. Students own implementations, and their work is credited in AUTHORS files by component.** [practice] (P) NonOpt AUTHORS credits Baoyu Zhou (dual active-set QP solver), Minhan Li (inexactness conditions and the TEST29 problems) and Lara Zebiane (interior-point QP solver, Python interface via PR #2). Outside contributions are accepted as well: PIPAL PRs #1 and #2 by an external user ("itsmathtime", Dec 2021) added function-handle problem definitions and were merged.

**PE36. Compute and resource context over time.** [practice] (P)

| Era | Setting |
|---|---|
| 2009–2010 | The 2009–10 archives list file owner `fec028` in group `e90nocedal` [observed in archive metadata; inferred to be a Northwestern-group machine] |
| 2011 | Mac laptop (`.DS_Store` files); Matlab R2010b on an 8-core Opteron for PIPAL |
| 2017–2022 | 8 GB memory and 4-hour or 90-minute wall-clock caps; Lehigh COR@L "polyps" cluster (i-TRACE) |
| 2025 | Apple M1 Pro laptop (NonOpt) |
| 2026 | GitHub Actions CI and an AI coding agent |

Team: in each era, one PI-written framework with 1–3 students contributing modules.

---

## 6. Layers 1–3 (taste, problem choice, idea generation): what process evidence adds

- **Idea generation, fast probe then decide.** [practice] (P) QuasiCuttingPlane shows a one-week prototype against the simplest baseline (a subgradient method), then abandonment. The AggQN history shows a probe by a student ("first paper extension", Aug 2019) ahead of the full paper. [inferred] Ideas are tested cheaply in Matlab before they enter the C++ or framework code.
- **Criticism absorbed into the next design.** [practice] (P) In 2020 Curtis–Li criticized LMBM's objective-difference stopping (PE11). NonOpt 2025 adopts "termination conditions related to improvement in the objective function value over recent iterations" as its default and notes that "Other software packages … also rely heavily on such heuristic termination conditions, including LMBM and Hanso" (2503.22826 §6.2). See C5.
- For layers 1–3 otherwise, see 01 and 02; no further process evidence was found.

---

## 7. Why these practices matter for someone improving a solver (for Phase 2; not his words)

[inferred] The evidence adds up to a checkable routine:
1. Implement the rival inside your own framework.
2. Vary one strategy object at a time (PE6, PE7, PE33).
3. Make the baseline strong or even favoured, and state by how much (PE8–PE11).
4. Build pathological variants that isolate the claim (PE1).
5. Log every excluded problem (PE3).
6. Check that the theory's event actually occurs (PE17).
7. Version the reproduction package (PE23).

The recorded weak points to guard against:
- tuning on the evaluation set without reporting the tuning effort (PE13);
- a single run for a randomized method (PE15);
- a long-lived house test set (PE4);
- an unoptimized build and masked test failures, found only by a late review (PE22).

---

## 8. Stated versus done (cross-check against 02)

| 02 item (stated) | What the artifacts show | Verdict |
|---|---|---|
| R4 / 3.1: outer and inner solvers designed together; exploit inexact inner solves | iR Newton, i-TRACE, GS-inexact, the stochastic SQP inexact variant and the Ipopt inexact IPM all implement inexact inner solves with termination tests tied to the outer method. The student PR log shows the termination tests (TT1–TT3) being debugged | **Consistent** (practice, 2006–2026) |
| R5 / 4.1: fair comparison must count tuning effort (2017, 2021) | TRish v3 (2018) equalizes tuning effort explicitly; stochastic SQP (2020) over-tunes the baseline. PIPAL (2012), SQP-GS (2012) and iR Newton (2019) tune on the test set without reporting the effort | **Partly consistent; improves after about 2018** |
| 4.2: "We should not let one test set (or a few) bias all research" (2021) | The same 20-problem nonsmooth set runs from 2018 to 2025, and NonOpt 2025 compares only against itself | **Tension** (C3) |
| 4.4: "running a solver on a problem once (or a few times) is not enough" (2021) | 10 starting points (2012) and 10 runs (2020, 2021); but single runs for randomized SVANO-GS (2018/19) | **Mostly consistent; one lapse before the statement** (C4) |
| 4.3: benchmarks should not define success for the reader; present much data | 120 raw output files committed for NonOpt; full per-problem tables in appendices (iR Newton App. C) | **Consistent** |
| 5.2 / 5.4: say what your approach does not cover; report where the competitor wins | "We do not claim …" (PE27); LMBM's better values reported (PE11); "PIPAL-a and especially IPOPT have an edge" (01) | **Consistent** |
| 5.3: errors corrected publicly, escalated by impact | Three corrigenda, each a full restatement with proof (PE26) | **Consistent**; the discovery process is not disclosed |
| 4.7: defaults tuned for a good answer fast | NonOpt experiments are run under a "speed" profile (defaults) and an "accuracy" profile | **Consistent** |
| 1.4 / R8: practitioners want reliable, fast, easy-to-use software | Prototype-labelled Matlab codes; NonOpt with manual, Python and AMPL interfaces, CI in 2026. The Ipopt inexact option remains experimental and opt-in at compile time | **Mixed**: usability arrives late and only in NonOpt |
| R3: single algorithm, no two-phase switching | PIPAL-a and the SQuID/DUST designs update penalty parameters inside one iteration; the infeasible test sets are built to show this | **Consistent** |

---

## Contradictions (kept, not reconciled)

- **C1. Tuning cost.** In 2021 he said "The only way for algorithm comparisons to be fair would be for them to include all computational time spent tuning each algorithm" (02 §4.1). Against that:
  - PIPAL 2012, SQP-GS 2012 and iR Newton 2019 state that their parameters were those that worked best on the reported test set, and none reports tuning time (PE13);
  - in 2018 and 2020 his papers did equalize or favour the baseline's tuning (PE9, PE10).
  
  Both are on record, 2012 through 2021.
- **C2. How the LMBM comparison is summarized.**
  - Curtis–Li v2 (2021): "the results are generally comparable. LMBM yields lower values for some problems while GS-inexact-agg yields lower values for a few others."
  - NonOpt (2025): "since NonOpt performed favorably in these comparisons, … our experiments in this paper focus exclusively on experiments with NonOpt only."
  
  The final IJOO text was not read, so the published wording may differ.
- **C3. Test-set monoculture versus "one test set" warning.** The 2021 slides warn against letting one test set bias research. His nonsmooth line reuses the same ten or twenty problems (the ten Haarala et al. problems, plus TEST29 from Curtis–Li on) from 2018 to 2025, and the set is described as one "for which LMBM has been tuned".
- **C4. Single runs versus repetitions.** SVANO v5 (2019) reports a single run per problem for a randomized method, justified by observed representativeness. In 2021 he said a single or few runs is "not enough".
- **C5. Objective-difference termination.** In 2020 LMBM's objective-difference stopping was treated as a weakness to switch off. By 2025 an objective-improvement rule is NonOpt's default and is defended as common practice.
- **C6. Homepage invitation versus availability.** The software page says "Please use the Ipopt option inexact_algorithm yes". Ipopt 3.14 builds that option only when configured with `--enable-inexact-solver` ("EXPERIMENTAL! (default: no)") and only with Pardiso from pardiso-project.org.
- **C7. Paper versus released code.** PIPAL's published trial-set sizes (five values each for ρ and μ) match neither PIPAL 1.1 (4/10) nor 1.2 (8/4). The TRACE repository README says "under development" while the CV says "Code written by me" for the 2017 paper.
- **C8. Two platform accounts of one QP test failure.** The CLAUDE.md brief reported problem #9 failing on Linux/aarch64 with reference BLAS. The recorded finding was that on macOS with reference BLAS the failure reproduces on problem #11, "not #9", with vendor BLAS passing. The brief kept both readings; so do I.

## Gaps

- **Peer review and rebuttals.**
  - The OpenReview profile (~Frank_E._Curtis1) was blocked by a bot check; its API requires login. No ML-venue reviews or rebuttals were read.
  - Journal referee reports are not public.
  - How he answers criticism is visible only indirectly: acknowledgments, the changes between versions, and the redesigned LMBM comparison.
- **Final journal versions** of the 2019–2024 papers were not read (paywalled). For the stochastic SQP SIOPT 2021 paper arXiv has only v1, so the final numerics (and whether they used the repository's noise model `10^(-factor)/sqrt(n)·randn` added by Berahas in Nov 2020, which differs from v1's N(g, ε_N I)) are **not read**.
- **Rejections.** PIPAL's Mathematical Programming submission outcome is not documented. No other rejected, withdrawn or retracted paper was found. The isotonic-regression report's fate is unknown.
- **Dating gaps.** PIPAL 1.2 and SLQP-GS 1.3 have no original dates (they appear only as 2021 GitHub commits). The "previously used repository" behind NonOpt (before June 2019; the SVANO C++ code) is not public.
- **Private workflow.** Group-internal repositories, experiment logs, lab notebooks and group-meeting practice were not found (agent 04's domain). The review that fed NonOpt's CLAUDE.md ("a prior review") is not public.
- **Unread material.** The PhD thesis (2007) and the book *Practical Nonconvex Nonsmooth Optimization* (2025) were not read.
- **Unconfirmed items.**
  - The Ipopt inexact code: Curtis's own contributions to it were not identified; the files name Wächter.
  - The build flags used for NonOpt 2.0 timings are not reported in the paper [not confirmed].

## Sources

One line each: title, author, date, URL or DOI, primary/secondary.

1. NonOpt repository (git history 2019-06-25 → 2026-07-31, tags v2.0–v2.2, `mpc/README`, `NonOpt-Manual/NonOpt.tex` diff of 2025-12-15, `CLAUDE.md` in commits 298a0c3–ab06fed), Curtis et al., https://github.com/frankecurtis/NonOpt (primary)
2. StochasticSQP repository (git history 2020-07-31 → 2021-07-23; branch `inequality`; `problems/ProblemCUTEst.m`; `external/README.md`), Curtis, Berahas, Robinson, Zhou, https://github.com/frankecurtis/StochasticSQP (primary)
3. StochasticSQP pull requests #1–#4 (Berahas 2020; Zhou 2021; M. Li 2022), GitHub, via the GitHub search API (primary)
4. PIPAL repository (versions 1.0–1.2 as commits; PRs #1–#2, Dec 2021), Curtis, https://github.com/frankecurtis/PIPAL (primary)
5. SLQPGS repository (versions 1.0–1.3), Curtis (contributor T. Mitchell), https://github.com/frankecurtis/SLQPGS (primary)
6. TRACE repository (2022-05), Curtis, Robinson, Wang, https://github.com/frankecurtis/TRACE (primary)
7. AggQN repository (2019-07 → 2021-11), Berahas, Curtis, Zhou, https://github.com/frankecurtis/AggQN (primary)
8. SCBFGS repository (2021-07), Curtis, https://github.com/frankecurtis/SCBFGS (primary)
9. QuasiCuttingPlane repository (2020-04), Curtis, https://github.com/frankecurtis/QuasiCuttingPlane (primary)
10. Utilities repository (PaperStarter, LaTeX, CUTEst2Matlab; 2020-10 → 2021-07), Curtis and Robinson, https://github.com/frankecurtis/Utilities (primary)
11. StochasticGradientDemo repository (2025-05; listed only), Curtis, https://github.com/frankecurtis/StochasticGradientDemo (primary)
12. PIPAL 1.0 archive (files dated 2010-06-21/22; README "Last revised : 21 June 2010"), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/software/PIPAL_1.0.tgz (primary)
13. PIPAL 1.1 archive (files dated 2011-04-26), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/software/PIPAL_1.1.zip (primary)
14. SLQP-GS 1.0 archive (2009-10-28), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/software/SLQP-GS_1.0.tgz (primary)
15. SLQP-GS 1.1 archive (2011-02-01), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/software/SLQP-GS_1.1.tgz (primary)
16. SLQP-GS 1.2 archive (2011-11-07), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/software/SLQP-GS_1.2.zip (primary)
17. Software page, Curtis, accessed 2026-09-28, https://coral.ise.lehigh.edu/frankecurtis/software/ (primary)
18. "A Penalty-Interior-Point Algorithm for Nonlinear Constrained Optimization", Optimization Online entry, Curtis, published 2010-06-21, updated 2013-01-04, https://optimization-online.org/2010/06/2661/ (primary)
19. Curtis, "A penalty-interior-point algorithm for nonlinear constrained optimization", Math. Prog. Comput. 4(2):181–209, 2012, DOI 10.1007/s12532-012-0041-4 (§4 read) (primary)
20. Curtis & Overton, "A Sequential Quadratic Programming Algorithm for Nonconvex, Nonsmooth Constrained Optimization", SIAM J. Optim. 22(2):474–500, 2012, DOI 10.1137/090780201 (§§1, 4, 5, 6 read) (primary)
21. Byrd, Curtis & Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", SIAM J. Optim. 20(5):2281–2299, 2010, DOI 10.1137/080738222 (§§4–5 read) (primary)
22. Curtis, Mitchell & Overton, "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", Optim. Methods Softw. 32(1), 2017, DOI 10.1080/10556788.2016.1208749 (searched for protocol terms only) (primary)
23. Berahas, Curtis, Robinson & Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", arXiv:2007.10525 v1 (2020-07-20); SIAM J. Optim. 31(2), 2021, DOI 10.1137/20M1354556 (v1 §4 read) (primary)
24. Curtis, Robinson & Samadi, "An inexact regularized Newton framework with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", arXiv:1708.00475 v1, v2, v4; IMA J. Numer. Anal. 2019, DOI 10.1093/imanum/dry022 (primary)
25. Curtis, Robinson & Zhou, "A self-correcting variable-metric algorithm framework for nonsmooth optimization", arXiv:1708.02552 v1, v3, v5; IMA J. Numer. Anal., DOI 10.1093/imanum/drz008 (primary)
26. Curtis, Scheinberg & Shi, "A Stochastic Trust Region Algorithm Based on Careful Step Normalization", arXiv:1712.10277 v1, v3; INFORMS J. Optim. 2019, DOI 10.1287/ijoo.2018.0010 (primary)
27. Gao, Goldfarb & Curtis, "ADMM for multiaffine constrained optimization", arXiv:1802.09592 v1, v3; Optim. Methods Softw. 2020, DOI 10.1080/10556788.2019.1683553 (version comparison only) (primary)
28. Burke, Curtis, Wang & Wang, "Inexact Sequential Quadratic Optimization with Penalty Parameter Updates within the QP Solver", arXiv:1803.09224 v1, v3; SIAM J. Optim. 2020, DOI 10.1137/18M1176488 (primary)
29. Berahas, Curtis & Zhou, "Limited-memory BFGS with displacement aggregation", arXiv:1903.03471 v1, v3; Math. Program. 2022, DOI 10.1007/s10107-021-01621-6 (primary)
30. Curtis & Li, "Gradient Sampling Methods with Inexact Subproblem Solutions and Gradient Aggregation", arXiv:2005.07822 v1, v2; INFORMS J. Optim. 2022, DOI 10.1287/ijoo.2022.0073 (primary)
31. Berahas, Curtis, O'Neill & Robinson, "A Stochastic Sequential Quadratic Optimization Algorithm for Nonlinear-Equality-Constrained Optimization with Rank-Deficient Jacobians", arXiv:2106.13015 v1, v2; Math. Oper. Res. 2024, DOI 10.1287/moor.2021.0154 (version comparison only) (primary)
32. Curtis & Han, "Primal-Dual Active-Set Methods for Isotonic Regression and Trend Filtering", arXiv:1508.02452 v1, v2 (headings only) (primary)
33. Curtis & Wang, "Worst-Case Complexity of TRACE with Inexact Subproblem Solutions for Nonconvex Smooth Optimization", arXiv:2204.11322 v1; SIAM J. Optim. 2023, DOI 10.1137/22M1492428 (§4 read) (primary)
34. Curtis & Zebiane, "NonOpt: Nonconvex, Nonsmooth Optimizer", arXiv:2503.22826 (2025-03-28); Math. Prog. Comput. 2026, DOI 10.1007/s12532-026-00322-5 (§6 read) (primary)
35. Curtis, Robinson & Zhou, "Sequential Quadratic Optimization for Stochastic Optimization with Deterministic Nonlinear Inequality and Equality Constraints", SIAM J. Optim. 2024, DOI 10.1137/23M1556149 (Crossref record only) (primary record)
36. Curtis, "A Self-Correcting Variable-Metric Algorithm for Stochastic Optimization", ICML 2016, PMLR 48, https://proceedings.mlr.press/v48/curtis16.html (title and venue checked) (primary record)
37. Errata page and corrigenda (Lemma 4.9 of Burke–Curtis–Wang 2014, DOI 10.1137/120880045; Lemma 3.19 of Curtis–Robinson–Samadi 2017, DOI 10.1007/s10107-016-1026-2; Corollary 3.14 of Berahas et al. 2021), Curtis, https://coral.ise.lehigh.edu/frankecurtis/errata/ (primary)
38. Curriculum Vitae (last revised 2026-04-07), Curtis, http://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf (primary)
39. arXiv abstract pages and submission histories for 24 Curtis papers, arXiv, fetched 2026-09-28, https://arxiv.org/abs/<id> (secondary)
40. Ipopt ChangeLog (stable/3.14; entry 3.5.5, 2009-01-13), COIN-OR, https://github.com/coin-or/Ipopt/blob/stable/3.14/ChangeLog.md (secondary)
41. Ipopt source (stable/3.14): `configure.ac`, `src/Interfaces/IpIpoptApplication.cpp`, `src/Algorithm/Inexact/IpInexactAlgBuilder.cpp`, `doc/options.dox`, COIN-OR (Wächter et al.), https://github.com/coin-or/Ipopt/tree/stable/3.14 (secondary)
42. Crossref REST API checks of 16 DOIs and one title query, Crossref, 2026-09-28, https://api.crossref.org/works/ (secondary)
43. GitHub search API listing of repositories (user:frankecurtis) and pull requests, GitHub, 2026-09-28 (secondary)
44. OpenReview search result listing a profile page for Frank E. Curtis (profile content not readable: bot check), via WebSearch, 2026-09-28, https://openreview.net/profile?id=~Frank_E._Curtis1 (secondary; content **not read**)
