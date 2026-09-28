# Jorge Nocedal · 03 Process evidence (what he and his group actually do)

| Field | Value |
|---|---|
| Researcher | Jorge Nocedal (Walter P. Murphy Professor, IEMS, Northwestern University; living) |
| Dimension | Research-craft Phase 1, agent 03 of 06: **process evidence**. Behaviour visible in code, experiment sections, appendices, review threads, preprint versions and errata (framework §一 layers 4–7, §二 row 3) |
| Research date | 2026-09-28 |
| Sources consulted | 44 (listed under "Sources"): 38 primary, 6 secondary. Primary means Nocedal's own papers, preprints, code archives, web pages, errata and CVs, his group's repositories, his talk transcripts and the archived review thread. Secondary means vendor documentation, bibliographic APIs, one critique and one web search |
| WebSearch calls | 1 of 2 allowed. Everything else came from curl, git clone or WebFetch on known URLs |
| User-supplied material | None. `references/sources/{papers,essays,software}` hold only `.gitkeep`. `talks/` holds 8 transcripts that research agent 02 saved **during this run**. They are not user-supplied; I used three of them (UCLA 2021, Purdue 2017, Simons 2017). `private/` was not opened |
| Scratch | Code archives, clones and extracted texts are in `/tmp/nonlinear-team-scratch/base-skills/jorge-nocedal/a03/`. Nothing was written to the skill folder except this file |

**Labels.**
- **[practice]**: what papers, code or records show was done.
- **[stated]**: what he or the co-authors wrote or said about it.
- **[observed]**: what others recorded (reviewers, vendors, commenters).
- **[inferred]**: my reading, with its basis given.

Every item is also marked **primary** or **secondary**.

**Authorship caveat (read first).**
- Almost every artefact here is co-authored, and most of the code was written by students or postdocs. So "[practice]" usually means **team practice** in a Nocedal-led project. His personal share cannot be separated out.
- In the three student repositories, every commit is by a student. The OpenReview replies are signed by the first author (Keskar). Only one of the 22 arXiv preprints found was submitted by Nocedal himself (arXiv:2110.04355).
- This is itself process evidence; see §7.

**How quotes were taken.**
- PDF text was extracted with pypdf. Ligatures (ﬁ, ﬀ) were normalised to letters, and words split by extraction were re-joined. Nothing else was changed.
- "p." means the page of the PDF file named: the arXiv version given, or the author preprint on his homepage.
- Quotes from code are copied from the files in the named archive. Quotes from talks are YouTube captions, marked "caption-derived", and were not checked against the audio.

---

## 1. Headline findings (behaviour, not statements)

1. **The baseline is the incumbent that the rival community itself ranks best, and the paper says why.**
   - The 2021 finite-difference study justifies NEWUOA from the Moré–Wild and Rios–Sahinidis benchmark literature.
   - When a weaker baseline is used, the paper says so. In 2018 DFOtr was chosen because it is "simple enough to allow us to evaluate all its algorithmic components".
   - The baseline is later upgraded: DFOtr in 2018, then NEWUOA, DFO-LS and COBYLA in 2021 (§2.1).
2. **Fairness engineering that handicaps his own side.** [practice, primary]
   - In 2021 the finite-difference KNITRO run used L-BFGS memory 1 and a simple SQP instead of the interior-point algorithms.
   - In 2003 the team modified *KNITRO's* stopping test to match SNOPT's.
   - In the ML papers, competitors' step lengths were tuned over grids while the team's own method ran untuned.
   - In 2021 an appendix investigates non-default NEWUOA settings (§2.2).
3. **First show the classical method failing on a small, easy, chosen problem, with internal diagnostics. Then run a broad test set.** [practice, primary]
   - The BFGS condition number on ARWHEAD (2020/22).
   - "Failure of the Classical Trust Region Algorithm" (2022).
   - A three-arm design: noiseless original, noisy original, noisy modified (2024).
   - Smooth problems before noisy ones (2018) (§2.4).
4. **Instrument the inside of the algorithm, not only the outcome.** [practice, primary] This runs from 1989 to 2024:
   - time spent in each phase of the algorithm (1989);
   - skipped BFGS updates and phase timings printed by L-BFGS-B;
   - % full steps and CG counts in NITRO (1999);
   - condition number of the interpolation matrix (2009);
   - four-panel plots of ρ_k, radius, gradient and step (2022–2024) (§2.5).
5. **Ablate one component at a time.** [practice, primary] Examples (§2.6):
   - the geometry phase removed entirely (2009);
   - the recovery procedure switched on and off (2018/19);
   - update-skipping against lengthening (2020/22);
   - line search against fixed step, and finite differences against analytic gradients (2024/25).
6. **Losses and inconvenient results are printed.** [practice, primary] Examples (§3):
   - L-BFGS-B abnormal exits in a raw 1997 table;
   - "SVRG is superior on problems such as rcv1";
   - progressive-batching L-BFGS "requires more gradient evaluations" than SG/Adam;
   - update-skipping beats their own lengthening on easy problems;
   - model-based DFO is "more robust in the presence of noise than we expected".
7. **Revision behaviour: concede technical errors fast, and trim failures and anecdotes out of the final version.** [practice, primary]
   - The scale-invariance claim was withdrawn within days of the reviewer's question.
   - Failed remedies were moved to an appendix.
   - A failed "preliminary approach" section and an origin anecdote (the 2015 BBComp win) were deleted from journal-track versions.
   - Headline claims were softened or made more precise between versions (§4).
8. **Code is released and maintained as a numbered artefact, with change markers and conservative engineering choices.** [practice, primary]
   - L-BFGS-B keeps 2.1 and 3.0 downloadable, and the 2011 correction is marked line by line (`c-jlm-jn`).
   - The codes use reverse communication.
   - They reuse proven MINPACK components: Moré–Thuente line search, Moré–Sorensen trust-region solver.
   - Recommended parameter ranges are given as numbers (§2.7).
9. **Research questions become solver options, and later research becomes product features.**
   - [stated] In 2006, KNITRO exposed several barrier-update rules because "it is not known at present which one is the most effective in practice".
   - [observed] The KNITRO 16.0 manual still lists seven `bar_murule` settings. It also has noise-estimation options for finite differences (`findiff_estnoise`, `findiff_terminate`) that match the 2018–2022 research.
   - [inferred] That the research caused these options (§2.8).
10. **In the 2020s the lab prototypes inside the commercial solver.**
    - [practice] In 2024 an Artelys engineer modified KNITRO's Byrd–Omojokun code to add the noise-aware ratio.
    - [practice] KNITRO also serves as the comparator in constrained DFO.
    - [inferred] This gives consistent implementations, and also a conflict-of-interest risk that the papers do not discuss (§2.8, Contradictions C3).

---

## 2. Layer 4: experiments and execution

### 2.1 How baselines are chosen (paper by paper)

| Year · work | Baselines actually run | Reason given / how chosen | Label |
|---|---|---|---|
| 1989 · Liu & Nocedal, *Math. Program.* 45:503–528, doi:10.1007/BF01589116 | Buckley–LeNir CG-QN, partitioned quasi-Newton, CONMIN, CG | Competitors run **in their authors' own implementations**: "the combined CG-QN method of Buckley and LeNir (1983) as implemented in Buckley and LeNir (1985) … and the partitioned quasi-Newton method, as implemented by Toint (1983b)" (preprint p. 3); PQN via "the Harwell routine VE08 written by Toint" | [practice + stated, primary] |
| 1997 · "Testing MINOS and L-BFGS-B" web page (May 18, 1997; L-BFGS-B 2.1) | MINOS 5.5 | The MINOS spec file is printed in full (Hessian dimension 100, Superbasics limit 16000, Optimality tolerance 1.0D-5, Iterations 100000). L-BFGS-B was "run using m=12, and no printing (iprint=0); it has no other parameters to be adjusted." Limit 9999 f-evaluations | [practice, primary] |
| 1999 · Byrd, Hribar & Nocedal, *SIOPT* 9:877–900, doi:10.1137/S1052623497325107 | LANCELOT "using second derivatives and all its default settings" | Termination criteria set to 10⁻⁷ for both, so "the termination criteria for these two methods are therefore very similar" (preprint pp. 20–21) | [practice, primary] |
| 2003 · Morales, Nocedal, Waltz, Liu & Goux, LNCSE 30:167–183, doi:10.1007/978-3-642-55508-4_10 | LOQO, KNITRO vs SNOPT, filterSQP | The two interior codes were those available "through the NEOS system". The SQP pair was "the state-of-the-art sequential quadratic programming codes". SNOPT's quasi-Newton Hessian is called "an undesirable disparity" and then used as an experiment: "We will nevertheless take advantage of this difference to assess the effectiveness of quasi-Newton approximations" (p. 7) | [practice + stated, primary] |
| 2008 · Hei, Nocedal & Waltz, *Modeling, Simulation and Optimization of Complex Processes* (Springer) 273–292, doi:10.1007/978-3-540-79409-7_18 | SNOPT, KNITRO-Active (SLQP), TRON, L-BFGS-B; KNITRO-Direct, KNITRO-CG | "four active-set methods that are representative of the best methods currently available" (p. 2). The two interior methods were both taken from KNITRO "to minimize the effect of implementation details" (p. 3). SNOPT and L-BFGS-B were held back to a quasi-Newton section "because this algorithm works more effectively with quasi-Newton Hessian approximations" (p. 3). So methods are compared **like with like on Hessian information** | [practice + stated, primary] |
| 2009 · Fasano, Morales & Nocedal, *OMS* 24:145–154, doi:10.1080/10556780802409296 | newuoa, dfo (both with a geometry phase) | The own method is deliberately stripped down: "to study the effect of omitting the geometry phase, we choose to work with the simplest possible algorithm" (p. 4) | [practice + stated, primary] |
| 2014 → 2015 · Byrd, Hansen, Nocedal & Singer, arXiv:1401.7020 v1 → v2; *SIOPT* 26:1008–1031, doi:10.1137/140954362 | v1: SGD only. v2 adds oLBFGS | v2 §4.6: "We also compared our algorithm to the oLBFGS method [24], which is the best known stochastic quasi-Newton method in the literature" (v2 p. 26). The strongest direct competitor was added in revision; that a referee asked for it is [inferred] | [practice, primary] |
| 2017 → 2019 · Berahas, Bollapragada & Nocedal, arXiv:1705.06211; *OMS* 35:661–680 (2020), doi:10.1080/10556788.2020.1725751 | SVRG | For every method, the paper "independently tested all possible combinations of the tuning parameters" across nine per-iteration budgets (v4 p. 8). The chosen settings are printed in the figure legends (e.g. "SVRG: mSVRG=15000 (2.5n), α=4e-03") | [practice, primary] |
| 2018 · Bollapragada, Mudigere, Nocedal, Shi & Tang, arXiv:1802.05374 (ICML 2018) | Logistic regression: SG (batch 1) and SVRG, steplength tuned over α = 2^j, j ∈ {−10,…,10}. DNNs: SG and Adam with a validation-based "dev-decay" schedule | Own method: "none of the parameters in our PBQN method were tuned for each individual dataset" (v2 p. 6). θ "was tuned lightly by chosing among the 3 values" (p. 7). Batch normalisation and dropout were removed from **all** methods because they are "not conducive to the PBQN approach" (p. 7) | [practice + stated, primary] |
| 2018 → 2019 · Berahas, Byrd & Nocedal, arXiv:1803.10173 v1 → v2; *SIOPT* 29:965–993, doi:10.1137/18M1177718 | v1: DFOtr (Conn–Scheinberg–Vicente) only. v2 adds NOMAD | v1: "We chose the method and software described in [9] because it embodies the state-of-the-art of MB methods and yet is simple enough to allow us to evaluate all its algorithmic components" (v1 p. 4). v2: NOMAD run "with default parameters" (v2 p. 19), then dropped: "Since we observe from the previous results that NOMAD is the slowest of the methods, we do not report for it in the sequel" (v2 p. 20) | [practice + stated, primary] |
| 2021 → 2023 · Shi, Xuan, Oztoprak & Nocedal, arXiv:2102.09762; *OMS* 38:289–311, doi:10.1080/10556788.2022.2121832 | NEWUOA, DFO-LS, COBYLA against FD-L-BFGS, FD-LMDER, FD-KNITRO | The choice follows the literature: "Based on these studies, we regard the model-based approach of Powell as a leading method for derivative-free optimization (DFO)" (p. 4); "We chose newuoa because, as mentioned above, it is regarded as one of the leading codes" (p. 8). NOMAD was excluded because in published tests "cobyla outperforms nomad" (p. 27). Mixed equality–inequality problems were skipped because "we were not able to find an established DFO code of such generality that was sufficiently robust in our experiments" (p. 5) | [practice + stated, primary] |
| 2020 → 2022 · Shi, Xie, Byrd & Nocedal, arXiv:2010.04352; *SIOPT* 32:29–55, doi:10.1137/20M1373190 | Classical BFGS and L-BFGS, plus "BFGS (Skips)" and "L-BFGS (Skips)" | The team built a **cheaper rival of its own method** (skipping updates using the same noise-control test) and ran it as a baseline (v3 pp. 16–17) | [practice, primary] |
| 2024 → 2026 · Xuan & Nocedal, arXiv:2402.11920; *Oper. Res. Lett.* 65:107398, doi:10.1016/j.orl.2025.107398 | KNITRO 12.4 with forward-difference objective gradients | "There is no established constrained DFO solver that naturally lends itself for comparisons in our study. COBYLA or COBYQA treat constraints as black boxes … putting them at a disadvantage" (v1 p. 6) | [practice + stated, primary] |
| 2024 · Sun & Nocedal, arXiv:2411.02665 (journal version not found) | Unmodified KNITRO-CG (Byrd–Omojokun) | Same code, same "default stopping criteria of knitro … ensuring consistency across all tests" (v1 p. 29) | [practice + stated, primary] |

**Pattern** [inferred from the table]:
- For mature fields the baseline is the community's top code, justified from a published benchmark.
- For immature fields (constrained DFO, noisy constrained optimization) the baseline is the team's own production solver, used with and without the new component.
- When a baseline is dropped, the paper states the reason; NOMAD and the mixed-constraint class are both examples.

### 2.2 Fairness controls: what they actually did to make comparisons fair

- **Handicap the proposed side.** [practice, primary: arXiv:2102.09762 p. 27]
  - KNITRO was run "with alg=4 (an SQP algorithm), gradopt=2 (forward differencing), and hessopt=6 (L-BFGS)", and "In order to make the algorithm as close as possible to cobyla, we set the memory size of L-BFGS updating to its minimum value, t = 1 (lmsize=1)."
  - They also did not use KNITRO's interior-point methods "because they may put cobyla at an algorithmic disadvantage", and not SNOPT "because it implements a sophisticated SQP method". The rationale: "In short, we selected a simple nonlinear optimization method to more easily identify the strengths and weaknesses of the finite difference approach."
  - The same act, described in a talk [stated, primary, caption-derived, UCLA 2021 [0:39:31–0:40:02]]: "because we wanted to be super honest the memory in bfgs was set to one which we never use … so let's try to force our algorithm to be as dumb as possible". **Stated and practised match.**
- **Change your own code to match the competitor's stopping rule.** [practice + stated, primary: 2003 p. 6] Stopping tests "cannot be changed by the user. Nevertheless, we tried to make them as similar as possible, and in fact we modified KNITRO's stopping test to be almost identical to that of SNOPT." ("modified" restored from the extraction "modied".)
- **Align termination and budget across codes.**
  - 1999: 10⁻⁷ for both NITRO and LANCELOT.
  - 2003: 10⁻⁶ on all solvers, 30 CPU minutes and 1000 major iterations; hitting a limit counts as failure (p. 7).
  - 2021: KNITRO's optimality test was disabled ("opttol=1e-16, and findiff terminate=0") "For consistency with cobyla" (p. 27).
  - 2024: the same was done against DFOtr (arXiv:2402.11920 p. 7).
  - [practice, primary]
- **Give the competitor the tuning advantage.**
  - SG and SVRG steplengths were tuned over 21 values while PBQN stayed untuned (2018).
  - Every SVRG parameter pair was tried (2017/2019).
  - An appendix asks whether NEWUOA's defaults, "optimized for the noiseless setting", hurt it under noise, and reruns it with p = n+2 and larger interpolation sets (arXiv:2102.09762 App. B, p. 42).
  - [practice, primary]
- **Control implementation effects by staying inside one code base.** Three KNITRO algorithms share "the same type of stop tests and scalings" (2008 p. 3). In 2024 one KNITRO binary is run with and without the modification. [practice + stated, primary]
- **Declared limits of fairness.**
  - "As in most benchmarking studies, the standard disclaimer is in order: codes were tested with default options and overall performance may vary with other settings."
  - Only one code per problem class: "We found it essential to work with a small number of codes to allow us to understand them well enough and ensure fairness of the tests."
  - Both are from arXiv:2102.09762 p. 7. [stated, primary]
- **Ask the rival community before designing the experiment.** [practice, primary: arXiv:2102.09762 acknowledgements, p. 32] "We also thank Philip Gill, Tammy Kolda, Arnold Neumaier, Michael Saunders, Katya Scheinberg, Luis Vicente and Stefan Wild for their correspondences that led to the design of the experiments in this work." Scheinberg, Vicente and Wild are authors in the model-based DFO line whose methods the paper challenges.

### 2.3 Test problems, noise models and protocol

| Era | Test set actually used | Protocol details worth copying | Source |
|---|---|---|---|
| 1989 | 16 problems, n = 49 … 10,000 (Penalty I of Gill–Murray, Moré et al. collection problems) | Reports "both the number of function and gradient evaluations and the time required by the various parts of the algorithms", because in most test problems "the function evaluation is inexpensive" (preprint p. 6) | [practice + stated, primary] |
| 1997 | "All the bound constrained optimization problems in CUTE" ("Since there are more than 20 instances of the PALMER problems we only report here 4 runs") | Raw per-problem table with n, time, f-evaluations and final objective for both codes. Abnormal exits are labelled for both codes (L-BFGS-B "ABNO" on EXPQUAD and QRTQUAD, "STOP" on BQPGAUSS; MINOS "current" on TORSION1, TORSION3, TORSION5, NOBNDTOR) | [practice, primary: testing.html] |
| 2003 | CUTE problems in the Benson–Vanderbei AMPL models, up to 10,000 variables | LP and QP excluded ("can be treated more efficiently by specifically designed methods"), as were feasibility problems and bound-only problems. CPU times reported only for n > 100 because "CPU times can be dominated by set-up costs for small problems" | [practice + stated, primary] |
| 2008 | All CUTEr bound-constrained AMPL models that scale, minus repeats ("we only used torsion1 and torsiona from the group of torsion models") | "Unless otherwise noted, default settings were used for all solvers" (p. 4); log performance profiles | [practice, primary] |
| 2009 | 60 smooth problems, n = 2 … 15 | Scope stated in the abstract. The conclusion is limited to (n+1)(n+2)/2-point models: "It remains to be seen whether the observations made in this paper apply also in that context" | [practice + stated, primary] |
| 2018/19 | 49 Hock–Schittkowski problems. 4 noise types (stochastic/deterministic × additive/multiplicative) × 4 levels | Budget 100·n evaluations and 30 CPU minutes. Tolerance 10⁻⁸ "chosen to display the complete evolution of the runs" (v2 p. 19). Deterministic noise uses the Moré–Wild procedure. 392 problem instances in the profiles | [practice + stated, primary] |
| 2021 | 73 CUTEst unconstrained problems (n ≤ 300), least-squares set, 49 + 3 inequality-constrained problems (n, m ≤ 100; variable-size up to 500) | Called through PyCUTEst and pdfo (Python 3.7). Only additive, uniformly distributed, bounded noise: "Perhaps the most important limitation of this study is that it considers only one model of noise" (p. 7) | [practice + stated, primary] |
| 2020/22 | 41 CUTEst unconstrained problems, uniform noise in f and g | "The optimal value φ∗ for each function was obtained by applying the BFGS method to the original deterministic problem until it could not make further progress" (p. 17). "Results are averaged over 5 runs" (p. 25). Bisection line search instead of interpolation "because it is more robust in the presence of noise" (p. 17) | [practice + stated, primary] |
| 2022/23 | "a small selection of unconstrained optimization problems" | "we did not include a stop test and simply ran it for 200 iterations, which was sufficient to observe its asymptotic behavior" (arXiv:2201.00973 p. 18) | [practice + stated, primary] |
| 2024 | "over 50 equality constraint problems from the CUTEst library"; results for 3 reported | Noise injected into f, c, g and J. Gaussian noise also tried, "with similar results" (arXiv:2411.02665 p. 29) | [practice + stated, primary] |
| 2024/25 | A 2-D acoustic horn design problem (PDE-based sample-average objective) | Motivated as a correction of the field's habit: "The recent literature on noisy nonlinear optimization typically reports numerical tests using either synthetic noise or simple machine learning models, leaving the question of their effectiveness in realistic applications open" (arXiv:2401.15007 v2 p. 2) | [practice + stated, primary] |
| ML 2014–2018 | Synthetic data, RCV1-type text sets, a speech recognition problem (SQN), spam, covertype; CIFAR-10/100, MNIST; nets C1–C4, AlexNet-like, ResNet18 | Large-batch study: networks trained "until we couldn't make anymore progress. So there was no early stopping" (Purdue 2017 [0:33:18], caption-derived). The paper reports only final test accuracy because the aim is "to characterize the nature of the minima", not "state-of-the-art accuracy" (arXiv:1609.04836 v2 p. 4) | [practice + stated, primary] |

**Repeated-run discipline** [practice, primary]:
- The Wedge README (Marazzi, 2001): "We recommend that each problem be run a number of times. The default is to run a problem 5 times, if nRunsOptn = 'Var'."
- The same five-run averaging reappears in 2022 (averages over 5 runs) and in the 2017 large-batch paper (5 trials per network).

### 2.4 Order of work inside a project (what gets done first)

1. **The easy, noise-free case before the hard case.** arXiv:1803.10173 v1 §2: "Before embarking on our investigation of noisy objective functions we consider the case when noise is not present, and compare the performance of a model based trust region (MB) method and a straightforward implementation of the L-BFGS method that uses finite differences to approximate the gradient (FDLM)" (p. 4). The 2021 paper repeats the order: §2.1 noiseless, then §2.2 noisy, in each problem class. [practice, primary]
2. **A failure demonstration on a deliberately easy problem, with an internal diagnostic.**
   - 2020/22, Figure 1: the condition number of the BFGS matrix on ARWHEAD with gradient noise U[−10⁻³, 10⁻³]. "The ARWHEAD problem is chosen because it is easily solved yet clearly illustrates the instability of the BFGS matrix under the presence of noisy updates" (arXiv:2010.04352 v3 p. 2).
   - 2022: §4.1 is titled "Failure of the Classical Trust Region Algorithm". The first example is an 8-variable diagonal quadratic (arXiv:2201.00973 p. 18).
   - [practice, primary]
3. **A three-arm controlled comparison.** arXiv:2411.02665 p. 30: "(i) We first report the performance of BO when noise is not injected into the functions … (ii) Next, we introduce noise into the problem but still used the unmodified knitro code … (iii) Finally, we present the results of knitro with our proposed modification". [practice, primary]
4. **Try the naive adaptation first, and write down that it failed.** arXiv:1401.7020 v1 §2.1 "A Preliminary Approach" averaged iterates and gradients into BFGS pairs: "We found that this method was not successful in practice. We applied it to the learning problems described in section 3 and observed that the iteration (1.6) was neither faster nor more robust than the stochastic gradient descent method" (v1 p. 5). The section is absent from v2 (§4). [practice, primary]
5. **The algorithm is often delivered in two papers: first theory, then a practical algorithm.** The line runs arXiv:1901.09063 (Xie, Byrd & Nocedal, "Analysis of the BFGS Method with Errors", Jan 2019) to arXiv:2010.04352, whose final remarks say it "transforms the theoretical algorithm proposed in [29] into a robust and practical procedure" (v3 p. 25). [practice + stated, primary]

### 2.5 Instrumentation: what gets measured inside the algorithm

- **1989**: time in "the various parts of the algorithms" (preprint p. 6). [practice, primary]
- **L-BFGS-B 3.0 (2011)**: every run prints `Tit`, `Tnf`, `Tnint` ("total number of segments explored during Cauchy searches") and `Skip` ("number of BFGS updates skipped"). It also prints `Nact` and separate times for "Cauchy", "Subspace minimization" and "Line search" (`OUTPUTS/output_77_1`). Reference outputs for every driver ship in `OUTPUTS/` so that users can check their build. [practice, primary: Lbfgsb.3.0.tar.gz]
- **NITRO 1999**: columns for the number of CG iterations and "%full steps", the percentage of steps that did not encounter the trust region (preprint p. 21). [practice, primary]
- **2009**: data on "the evolution of the condition number of the interpolation matrix and the accuracy of the gradient estimate" and the rate of successful iterations (abstract; p. 5). This produced a *conjecture* rather than a claim: "We conjecture that a self-correction mechanism may be at play" (p. 2). [practice + stated, primary]
- **2020/22**: the condition number of the BFGS matrix over the iterations (Fig. 1). [practice, primary]
- **2022–2024**: four-panel run diagnostics:
  - 2022 (arXiv:2201.00973 p. 18): noiseless gradient norm against the injected noise level, trust-region radius, distance to solution, and ratio ρ_k clipped at ±5 "for graphical clarity";
  - 2024 (arXiv:2411.02665 p. 30): objective, feasibility error, optimality error and step length.
  - [practice, primary]
- **Noise-aware termination written into code**: the student release `noise-tolerant-bfgs` returns flags such as "`4`: Reached noise level of the function" and "`5`: Reached noise level of the gradient" (README). [practice, primary (group code)]

### 2.6 Ablations: taking one component out

| Component removed or switched | Result reported | Source |
|---|---|---|
| Geometry phase of model-based DFO | "We find, to our surprise, that omitting the geometry phase does not seem to harm the efficiency and robustness of our algorithm" (p. 2); "This is surprising, as we expected Algorithm I to be often slow (or even fail)" (p. 5) | Fasano, Morales & Nocedal 2009 [practice + stated, primary] |
| Recovery procedure in FD-L-BFGS | "As shown, the performance of the method deteriorates substantially when the Recovery procedure is not used" (v2 p. 21) | arXiv:1803.10173 v2 §5.1 |
| Lengthening against update skipping | Skipping "can be a strong alternative to lengthening if the problem is fairly well-conditioned … However, it can fail to capture the change in curvature that is necessary for more difficult problems" (p. 21) | arXiv:2010.04352 v3 §5.3 |
| Line search against fixed step; FD against analytic gradients | Framed as tests of received wisdom: "It is common practice to avoid line searches when minimizing noisy functions. We investigate whether this practice is still justified" (p. 10); "A common view in optimization is that finite difference gradient approximations should be avoided in the noisy setting. We investigate this perspective" (p. 11). The FD interval h was run at 10⁻¹, 10⁻², 10⁻³ "to compare the outcomes of overestimating and underestimating interval choices" | arXiv:2401.15007 v2 §5.1–5.2 |
| Primal against primal-dual barrier step | "the primal-dual version (pd) outperforms the primal version (p)" (preprint p. 21) | Byrd, Hribar & Nocedal 1999 |
| FD interval rule (theoretical against heuristic Lipschitz estimates) | Appendix A: "Numerical Investigation of Lipschitz Estimation". Finding: existing procedures for estimating the derivative bounds "are not robust" (p. 6) | arXiv:2102.09762 |

[inferred] The ablation target is almost always a **safeguard or heuristic that the field treats as necessary** (geometry phase, avoiding line searches, avoiding finite differences). The team asks whether it earns its cost.

### 2.7 Software practice (read from the code itself)

**L-BFGS, `lbfgs_um.tar.gz` (header "JORGE NOCEDAL *** July 1990 ***"; archive dated 2000)** [practice, primary]
- Reverse communication: "In order to allow the user complete control over these computations, reverse  communication is used."
- Borrowed line search: "The steplength is determined at each iteration by means of the line search routine MCVSRCH, which is a slight modification of the routine CSRCH written by More' and Thuente."
- Numeric guidance instead of prose: "Values of M less than 3 are not recommended; large values of M will result in excessive computing time. 3<= M <=7 is recommended." GTOL defaults to 0.9. A too-small GTOL is reset to 0.9 and a message printed ("GTOL IS LESS THAN OR EQUAL TO 1.D-04").
- The only example driver (`sdrive.f`) is the extended Rosenbrock function with n = 100, m = 5, and "at most 2000 evaluations of F and G".

**L-BFGS-B 2.1 → 3.0 (`Lbfgsb.2.1.tar.gz`, `Lbfgsb.3.0.tar.gz`)** [practice, primary]
- The README calls 3.0 "the modified/corrected limited memory code". The header of `lbfgsb.f` says: "Minor changes in the updated code appear preceded by a line comment as follows". The marker is `c-jlm-jn` (Morales–Nocedal), which occurs 5 times.
- The major change is described in the header: "It is shown that the performance of the algorithm can be improved significantly by making a relatively simple modication [sic] to the subspace minimization phase. The correction concerns an error caused by the use of routine dpmeps to estimate machine precision."
- In the code, 2.1 calls `epsmch = dpmeps()`; 3.0 uses `epsmch = epsilon(one)`. The rewritten `subsm` carries its own dated note ("January 17, 2011"). The header states the workspace formula for both the new and old versions.
- Both versions stay downloadable. The page says: "L-BFGS-B was upgraded on August 2, 2011 from version Lbfgsb.2.1 to version Lbfgsb.3.0".
- Parameter guidance is numeric: "The range  3 <= m <= 20 is recommended". `factr` = "1.d+12 for low accuracy; 1.d+7 for moderate accuracy; 1.d+1 for extremely high accuracy".
- Onboarding goes through drivers: "We recommend that the user read driver1.f/driver1.f90". driver3 shows "how to terminate a run after some prescribed CPU time has elapsed".
- **Packaging slips.**
  - The README lists `compact.pdf` and `acm-remark.pdf` as included, but the 3.0 archive does not contain them.
  - The `subsm` header cites the Remark as "Remark On Algorithm 788" (should be 778) and dates it "Decemmber 27, 2010".
  - [practice, primary] These slips show a small, human release process, not an automated one [inferred].

**CG+ 1.1 (2000)** [practice, primary]
- The user chooses among three variants, including the weakest: "1 : Fletcher-Reeves 2 : Polak-Ribiere 3 : positive Polak-Ribiere (beta = max{beta,0})". A restart option is included (`IREST`).
- A changelog is kept in the README: "Version 1.1 is identical to version 1.0 except for 2 small bugs which were corrected from version 1.0 and some updated comments."
- [inferred] Shipping all three variants lets users reproduce the Gilbert–Nocedal comparison (*SIOPT* 2:21–42, 1992, doi:10.1137/0802003) rather than only use its winner.

**Wedge (Marazzi, 2001; MATLAB)** [practice, primary]
- The trust-region subproblem uses MINPACK's `gqtpar.f` (Moré–Sorensen) through a mex gateway.
- The problem-definition files are "analogous to the ones supplied by the CUTE test suite".
- The first download attempt in this run failed with a proxy/server error; a retry succeeded.

**Group repositories on GitHub (students' code, cloned 2026-09-28)** [practice, primary (group), not Nocedal's own commits]

| Repository | Commits / dates | What it shows |
|---|---|---|
| `keskarnitish/large-batch-training` | 5 commits, 2016-09-12 → 2017-04-24 | Code only for the parametric plots. The README promises: "The code for computing the _sharpness_ of a minima (Metric 2.1) will be released soon." No such code is in the repository at its last commit. When Keras 2 broke the code, a "preliminary PyTorch implementation" was added instead of a fix |
| `hjmshi/PyTorch-LBFGS` (Shi & Mudigere) | 25 commits, 2018-09-07 → 2020-10-20 (last: "correct computation of gtd") | Even an optimizer written for neural networks is first tested on CUTEst: `examples/Other/lbfgs_tests.py` "Tests L-BFGS implementation on common unconstrained optimization test problems from the CUTEst test problem set." Acknowledgements: "Thanks to Raghu Bollapragada, Jorge Nocedal, and Yuchen Xie for feedback on the details of this implementation". So Nocedal acts as a **reviewer of implementation details**, not as a committer |
| `hjmshi/noise-tolerant-bfgs` (Shi & Xie) | 4 commits, 2020-08-18 → 2021-01-25 | One-file Python release of the SIOPT 2022 method, with noise-level termination flags. Announced in the paper (v3 p. 25) |
| `jnocedal/jnocedal.github.io` | 15 commits by `jnocedal`, 2023-02-13 → 2024-01-16 | His own homepage repository. It still contains unedited template filler ("Lorem ipsum …"). This is the only GitHub repository found with commits by him |

### 2.8 From research to product, and prototyping inside the product

- **Open question becomes a user option.**
  - [stated, primary: Knitro 2006 preprint p. 5] "Since it is not known at present which one is the most effective in practice, Knitro allows the user to experiment with the barrier update strategies just mentioned."
  - [practice, primary] The strategies were tested in two different solvers: they "are tested in the two distinct algorithmic frameworks provided by the ipopt and knitro software packages". Source: the abstract of Nocedal, Wächter & Waltz, *SIOPT* 19:1674–1693 (2009), doi:10.1137/060649513, read via OpenAlex. The same abstract says it "examines convergence failures of the Mehrotra predictor-corrector algorithm".
  - [observed, secondary: Artelys Knitro 16.0 manual, "Knitro options"] `bar_murule` still offers "auto", "monotone", "adaptive", "probing", "dampmpc", "fullmpc" and "quality".
- **Noise research and KNITRO options.** [observed, secondary: same manual]
  - `findiff_estnoise` "can be used to enable an estimate of the noise in the model when using finite-difference gradients … This noise estimate can then be used to set a finite-difference steplength appropriate for the estimated noise level". Its value 2 ("withcurv") estimates "a curvature factor as well as the noise".
  - `findiff_terminate` (default "errest") allows "termination based on estimates of the finite-difference error".
  - This matches the 2018–2022 papers: noise estimate plus a second-derivative bound determines h.
  - [inferred] That these options came from that research: the dates are unknown (no release notes found; see Gaps), and Nocedal consulted for Artelys 2012–2020 (CV c. 2023).
- **The origin anecdote that was cut.** [practice, primary: arXiv:1803.10173 v1 p. 3] v1 said: "(In fact, the motivation for the research reported in this paper stems from the competition established in 2015 to test algorithms for black-box (non-noisy) optimization http://bbcomp.ini.rub.de/. The winner was the finite difference BFGS method for bound constrained optimization implemented in the knitro package [5].)" The sentence is gone in v2 and the SIOPT version. So a product result fed a research question, and the trace was then removed.
- **Prototyping in the production solver.** [practice + stated, primary: arXiv:2411.02665 p. 29] "The original BO algorithm in knitro was modified by Figen Oztoprak from Artelys Corp. to include, as an option, the modified ratio (19) and the ability to input the noise level." Other uses:
  - The 2024 feasible-DFO code uses KNITRO 12.4 (SQP, L-BFGS) to solve the trust-region subproblem, wrapped around DFOtr used "without altering its logic" (arXiv:2402.11920 p. 7).
  - The 2021 study uses KNITRO 12.2.

---

## 3. Layer 5: judging results (what they do with results)

**3.1 Printing losses and limits of their own method** [practice + stated, primary]
- 1989: partitioned quasi-Newton "is extremely effective, and is superior to the limited memory methods" on many problems (preprint p. 3; details in 01 §SW1).
- 1997: L-BFGS-B's own abnormal exits (ABNO, STOP) sit in the public table next to MINOS's.
- 2003 abstract: "all codes show much room for improvement", and that includes KNITRO.
- 2008 summary: the SLQP method (KNITRO-Active) "is robust, but is not as effective as gradient projection at identifying the optimal active set".
- 2017 (arXiv:1705.06211 v1 p. 7): "Our results show that SVRG is superior on problems such as rcv1 where the benefits of using curvature information do not outweigh the increase in cost."
- 2018 (arXiv:1802.05374 v2 p. 7): "We observe from our results that the PBQN method achieves a similar test accuracy as SG and Adam, but requires more gradient evaluations." Final remarks: "To make the new method competitive with SG and Adam for deep learning, we need to improve several of its components" (p. 8).
- 2021 (arXiv:2102.09762 p. 6): "For noisy functions, we observed that newuoa is more efficient and accurate than the finite-difference l-bfgs method for unconstrained optimization, but not by a wide margin." Also: "One striking observation from our study is that interpolation-based trust-region methods are more robust in the presence of noise than we expected."

**3.2 How many runs are shown: "typical behavior" reporting** [practice + stated, primary]
- 2020/22: "The performance of the methods is best understood by studying the runs on each of the 41 test problems. Since this is impractical due to space limitations, for every experiment, we selected a problem that illustrates typical behavior over the whole test set" (arXiv:2010.04352 v3 pp. 17–18). Profiles over all 41 problems follow in §5.4.
- 2024: "While we conducted experiments on over 50 equality constraint problems from the CUTEst library, we report results for three sets of experiments that exemplify the typical behavior observed in our more comprehensive set of experiments" (arXiv:2411.02665 p. 29). Here no aggregate over the 50 problems is shown [practice, from the section read].
- [inferred] Choosing the illustrative problem is a judgement call that readers cannot audit when there is no aggregate (2024). It can be audited when there is one (2022; 2021's Appendix C "Complete Numerical Results").

**3.3 Theory checked against the run** [practice + stated, primary: arXiv:2201.00973 p. 19] The bound of Theorem 6 is plotted over the observed gradient norms. The paper concludes "that the theoretical prediction given in Theorem 6 is pessimistic when compared to the final achieved accuracy in the gradient, as is to be expected of convergence results that assume that the largest possible error occurs at every iteration". This matches the stated belief R2 in 02 (judge theory by practice).

**3.4 Surprise is recorded, not smoothed over** [practice, primary]
- 2009 "to our surprise";
- 2021 "Surprisingly, the carefully crafted newuoa code is not more efficient, as measured by the number of function evaluations, than a finite-difference l-bfgs method" (p. 6), and "more robust … than we expected";
- UCLA 2021, caption-derived: "it was surprising we thought it was going to be a struggle" [0:40:36].

**3.5 Confidence in a method comes with its failure mode written down** [stated, primary]
- The 2019 abstract: the noise estimate and h "are inexpensive but not always accurate, and to prevent failures the algorithm incorporates a recovery mechanism".
- The Simons 2017 talk describes the diagnosis tree the recovery follows: "There are two possibilities. You estimated the noise wrong. In this case, why don't you re-estimate the noise? The other one, it looks like the estimate of the noise is fine, the finite difference interval is fine, maybe just the line search set you off" [0:28:20, uploader-provided subtitles].

---

## 4. Responding to criticism and revising (reviews, versions, errata)

### 4.1 The one public review thread found: ICLR 2017, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima"

Keskar, Mudigere, Nocedal, Smelyanskiy & Tang. OpenReview id H1oyRlYgg; arXiv:1609.04836. Read from an Internet Archive snapshot (2024-03-21) of the OpenReview API, because the live site served a bot challenge. All replies are signed by the first author, Keskar. [observed + practice, primary]

| Date | Who | Point | Response / outcome |
|---|---|---|---|
| 2016-12-02 | AnonReviewer2 | The sharpness metric with "1+f(x)" in the denominator is not scale invariant | 2016-12-07 reply: "You are right, this metric is not scale invariant, and we will remove that statement from the paper in our next update." A **new check was run in response**: "we experiment with the denominator changed to f(x0) - f(x) … and observed similar order-of-magnitude results, indicating that our numbers reported in the paper are not misleading." Carried out: v1 p. 5 read "invariance of sharpness to problem dimension, sparsity and scale"; v2 reads "problem dimension and sparsity" |
| 2016-12-03 | AnonReviewer3 | True local minima, or minima of 1-D slices? | "Agreed, we cannot guarantee that the solutions obtained by the SB and LB methods are indeed local minima of the problem (as we did not attempt to verify second-order optimality). To be cautious, we will use the terms "LB solution" and "SB solution", as appropriate, in our updated manuscript." **Only partly carried out**: v2 still uses "minimizer" 45 times (v1: 38) and "LB solutions" once, but adds "So far, we have used the term sharp minimizer loosely" (v2 p. 5) and "(In this paper, we only provided some numerical evidence.)" (p. 9) |
| 2016-12-16 | AnonReviewer3 (rating 6) | Try rescaled Gaussian noise in LB gradients | 2016-12-27, a **negative result disclosed in the thread**: "We experimented with additive random Gaussian noise (both in gradients and in iterates), noisy labels and noisy input-data. However, despite significant tuning of the hyperparameters of the random noise, we did not observe any consistent improvements in testing error." And: "LB methods may need to be modified in a more fundamental way to achieve good generalization." No such experiment appears in v2 [practice, from the versions read] |
| 2016-12-16 | AnonReviewer2 (rating 10) | "Little novelty but valuable empirical evidence" | "Thanks for your review" |
| 2016-12-17 | Alex Lamb (public) | Very small batches? Noise injection? | "a batch-size of 8 or 16 led to (statistically) similar values of testing accuracy as a batch size of 256" (preliminary experiments), plus the same noise-injection negative result |
| 2017-02-06 | Program chairs | "Accept (Oral)" | — |
| 2019-10-08 | Amir H. Abdi (public), two comments | "Potential mistake in Appendix C" (performance-model assumption); "Typo in Figure 5" (ε value) | **No reply** in the archived thread (snapshot 2024-03). No arXiv v3 exists. [practice, primary] |

**Other v1 → v2 changes** [practice, primary]:
- The v1 main-text §4 "Attempts to Alleviate the Problem" (data augmentation, conservative training, robust training) moved to Appendix E. The v2 conclusion describes them as "attempts to remedy the problem" whose results are "preliminary".
- New warm-starting ("piggybacked") experiments entered the main text as the positive lead.

### 4.2 What changes between arXiv v1 and the final version (8 papers compared)

| Paper | v1 → final | What changed (behavioural reading) |
|---|---|---|
| arXiv:1401.7020 (SQN) | v1 Jan 2014 → v2 Feb 2015 → *SIOPT* 2016 | Deleted: §2.1 "A Preliminary Approach" with its admission of failure. Added: §3 "Convergence Analysis" and §4.6 "Comparison to the oLBFGS method". **Failure removed, theory and strongest competitor added** [practice, primary] |
| arXiv:1609.04836 (large batch) | v1 Sep 2016 → v2 Feb 2017 (ICLR) | Scale claim removed; "loosely" caveat added; remedies moved to an appendix; code link added (§4.1) |
| arXiv:1705.06211 (Newton-sketch) | v1 May 2017 (conference-style, 25 pp) → v4 May 2019 (36 pp) → *OMS* 2020 | The v1 abstract claim that the methods "are far more efficient than SVRG, a popular first-order method" (v1 p. 1) and the v1 contribution "These observations are in stark contrast with popular belief" (p. 2) are **gone** from v4. v4's abstract frames the work as revealing "relative tradeoffs" and CG vs. SGI "advantages". The rcv1 loss to SVRG is kept (v4 p. 9) [practice, primary]. That v1 was a rejected conference submission is **not verified** (format only; [inferred, weak]) |
| arXiv:1802.05374 (PBQN) | v1 Feb 2018 → v2 May 2018 (ICML) | No substantive change in structure or in the negative DNN result (both versions contain "requires more gradient evaluations") |
| arXiv:1803.10173 (noisy DFO) | v1 Mar 2018 (40 pp) → v2 Jan 2019 (26 pp) → *SIOPT* 2019 | BBComp origin sentence removed. NOMAD added as a second baseline. "Model based (MB)" renamed "function interpolating (FI)". The paper shrank from 40 to 26 pages: v1's pointer "a larger sample can be found in Appendix A" disappeared, and the v2 appendix A is shorter. The Kelley and Barton background paragraphs are in both versions [practice, primary] |
| arXiv:2010.04352 (noise-tolerant BFGS) | v1 Oct 2020, v2 3 days later, v3 Sep 2021 → *SIOPT* 2022 | Only v3 read (v1/v2 not compared) |
| arXiv:2102.09762 (FD study) | v1 Feb 2021 (82 pp, 38 tables, 29 figures) → *OMS* 38:289–311 (23 pp), retitled "On the numerical performance of finite-difference-based methods for derivative-free optimization" | arXiv never updated: the long form stays public as the full record, and the journal form is the compressed claim [practice, primary; journal text not read] |
| arXiv:2401.15007 (robust design) | v1 Jan 2024 "Noise-Tolerant Optimization Methods for the Solution of a Robust Design Problem" → v2 Oct 2024 → *SISC* 2025 "Design Guidelines for Noise-Tolerant Optimization with Applications in Robust Design" | The guarantee was made more precise: v1 "convergence to a neighborhood of the solution", v2 "convergence to a neighborhood of stationarity". "deterministic nonlinear optimization" became "nonlinear optimization" in the first sentence. The acknowledgements thank "the referees for their valuable comments" [practice, primary] |

**Not compared:** arXiv:1606.04838 v1 → v3 (see 01 for the 20-month timeline), 1605.06049, 2110.06380.

### 4.3 Errata and corrections actually published [practice, primary]
- *Numerical Optimization*, 2nd ed. (with S. J. Wright): "Corrections to Numerical Optimization, Second Edition, Published August 2006 (Last updated May 27, 2008)". There are **80 numbered corrections**, from p. 5 to p. 629. They range from typos to substantive fixes, e.g. item 8, "will be able" → "will not be able", and item 12, "Remove the paragraph". First edition: separate sheets for the first and for the "second and third printings (updated 2/12/06)", with instructions for identifying the printing (`book/errata.html`).
- SIAM Review 2018 survey: an errata sheet "(Last updated: June 30, 2016)" with two equation-reference fixes. Its last update is two weeks after arXiv v1 (15 June 2016); the original posting date is unknown.
- L-BFGS-B: the 2011 Remark (Morales & Nocedal, *ACM TOMS* 38(1), doi:10.1145/2049662.2049669; full text **not read**: 403/404 at all three URLs tried). The code-level evidence of the change is in §2.7.
- **No corrigendum** was found on Crossref for a journal article with Nocedal as author ("corrigendum", "erratum", "correction to" queries). **No withdrawn arXiv preprint** was found (22 checked).

---

## 5. Failures, abandoned directions, dropped material (process trail)

| Item | Evidence | Label |
|---|---|---|
| Naive averaged-pair stochastic BFGS | "not successful in practice … neither faster nor more robust than the stochastic gradient descent method" (arXiv:1401.7020 v1 p. 5); deleted in v2 | [practice, primary] |
| Noise injection to rescue large-batch training | Gaussian noise in gradients and in iterates, noisy labels, noisy inputs: "despite significant tuning … we did not observe any consistent improvements" (OpenReview 2016-12-27) | [practice, primary; reported in thread only] |
| Large-batch remedies (augmentation, conservative, adversarial training) | v1 §4 → v2 Appendix E; "do not completely correct the problem" (v1 p. 12) | [practice, primary] |
| Sharpness-metric code | Promised "will be released soon" (README, 2016/17); not in the repository | [practice, primary] |
| Regression-based quasi-Newton for noise | Stated only: "we worked on that for quite a while and we could never get to develop an algorithm that would scale up" (UCLA 2021 [0:31:40], caption-derived). **No paper or code trace found** | [stated, primary] |
| PBQN for deep learning | Reported as not yet competitive; no follow-up PBQN-for-DNN paper found in the arXiv list | [practice, primary; follow-up absence from arXiv list only] |
| L-BFGS-B machine-epsilon error | Lived from 1997 until the 2011 3.0 release (dpmeps → epsilon) | [practice, primary] |
| Wedge (2002) | One paper and one MATLAB code; no follow-up. Model-based DFO resumed in 2024 via DFOtr, not Wedge | [practice, primary + inferred] |
| Newton-sketch "far more efficient than SVRG" | Claim removed between v1 and v4 | [practice, primary] |
| Unanswered 2019 comments on the ICLR paper | No reply; no v3 | [practice, primary] |
| Rejected papers | **None identifiable** from public records (see Gaps) | — |

---

## 6. Layer 6: how the work is written up (structure actually used)

- **Study-type titles.** At least 5 works are empirical studies by title:
  - "A Numerical Study of Active-Set and Interior-Point Methods for Bound Constrained Optimization" (2008);
  - "Assessing the Potential of Interior Methods for Nonlinear Optimization" (2003);
  - "An Investigation of Newton-Sketch and Subsampled Newton Methods" (2017/2020);
  - "On the Numerical Performance of Derivative-Free Optimization Methods Based on Finite-Difference Approximations" (2021);
  - "On the Geometry Phase in Model-Based Algorithms for Derivative-Free Optimization" (2009).
  - [practice, primary]
- **Declared limitations as a section.** arXiv:2102.09762 §1.3 "Limitations of this Work": one code per class, default options, no global or Bayesian methods, no nonsmooth problems, one noise model. arXiv:2401.15007 §1.1 states what the literature's tests leave open. [practice, primary]
- **Complete results kept in appendices.** Examples [practice, primary]:
  - arXiv:2102.09762 App. C "Complete Numerical Results" (the paper is 82 pages);
  - arXiv:1803.10173 App. A (performance and data profiles);
  - arXiv:1609.04836 App. B–E.
- **Figure vocabulary.** [practice, primary]
  - Performance profiles (2003, 2008, 2019).
  - Data profiles (2019, 2021).
  - Log-ratio profiles, called "Morales profiles" in arXiv:2010.04352 v3 Fig. 12, "proposed by Morales [34]" (arXiv:2102.09762 p. 9). Morales, "A numerical study of limited memory BFGS methods", *Appl. Math. Lett.* 15:481–487 (2002), doi:10.1016/S0893-9659(01)00162-8; not read.
  - Four-panel run diagnostics (2022–2024).
- **Tuned settings printed in legends** (Newton-sketch figures), so readers can see what each competitor was given. [practice, primary]
- **Benchmark prose warns against over-reading.** The 2003 paper: "we warn the reader against using our results to rank the codes" (p. 2; quoted in full in 02 E3). The 1997 web table has no such warning [practice, primary]; see C6.

---

## 7. Layer 7: organisation of the work (who does what)

- **Students and postdocs write the code and run the experiments.** [practice, primary]
  - 1997: the page says "Details of the runs are in ~ciyou/Tmns2", i.e. Ciyou Zhu's account.
  - 2011: J. L. Morales co-signed the L-BFGS-B changes.
  - CG+: G. Liu and R. Waltz.
  - 2016–2021: all commits in the three group repositories are by Keskar, Shi or Xie.
  - 2026 interview (in 01): Waltz rewrote KNITRO from scratch.
- **Students submit the preprints.** The arXiv submitter is the first-author student or postdoc for 21 of the 22 preprints found on arXiv (the 21 returned by the arXiv author search, plus arXiv:1401.7020, which that search does not return) (Oztoprak, Hansen, Solntsev, Keskar, Berahas, Curtis, Bollapragada, Shi, Xie, Xuan, Sun, Lou). The exception is arXiv:2110.04355, submitted by Nocedal. [practice, primary: arXiv submission histories]
- **Author order.** 01 §2.2 documents the switch to student-first, Nocedal-last around 2020 (not re-derived here).
- **Industry people inside the loop.** [practice, primary: author lists, affiliations, acknowledgements]
  - Intel: Mudigere, Smelyanskiy, Tang (2017, 2018).
  - Google Research: Singer (SQN 2014/16).
  - Artelys: Oztoprak (2021 paper; KNITRO modification in 2024).
  - CV c. 2023: consulting for Artelys 2012–2020 and Google 2012–2014; Chief Scientist, Ziena, 2002–2015. [practice, primary]
- **Byrd as a standing reader.** Byrd is thanked for "initial feedback" (2021) and for "valuable discussions" (2025) on papers he did not co-author, and is a co-author on 2018/19, 2020/22 and 2021/23. [practice, primary]
- **Consulting the competing school before experiments** (2021 acknowledgement, §2.2). [practice, primary]
- **Funding shape of the 2018–2024 noise and ML programme.** [practice, primary: CV c. 2023]
  - DARPA 2018–19, $250,000.
  - ONR 2018–20, $421,900; ONR 2021–24, $446,000.
  - NSF 2020–23, $200,000 ("Zero-Order and Stochastic Methods for Nonlinear Optimization").
  - AFOSR 2020–23, $380,000.
  - Intel 2016–18, $150,000.

---

## 8. Era and resource context of the practices

| Era | Compute and tools visible in the artefacts | Team / seniority | Transfer caveat [inferred] |
|---|---|---|---|
| 1989–1990 | SUN 3/60; Alliant FX/8 at Argonne for large n (01); Fortran 77; Harwell library distribution (VA15) | Mid-career; one student (D. C. Liu); Byrd suggested one of the scalings tested (01) | Memory-bound era: storage, not flops, was the scarce resource (01), hence O(n) storage and few user parameters |
| 1995–2000 | Fortran 77 codes, anonymous FTP (`eecs.nwu.edu`), CUTE via SIF; MINOS as the reference | Full professor; postdocs (Zhu, Morales); Optimization Technology Center (Argonne–Northwestern) | Raw per-problem tables on a web page stood in for today's supplementary material |
| 2003–2009 | Sun Ultra 5 with 385 MB (2003); NEOS; AMPL models; KNITRO commercial (Ziena) | Company co-founder; students (Waltz, Hei); access to competitors' binaries | Benchmarks included his own commercial code |
| 2014–2018 | Keras/Theano, then PyTorch; GPUs; Intel and Google collaborators | Department chair (2013–17); large student cohort | Industry datasets and hardware (e.g. the Google speech problem) are not reproducible outside |
| 2019–2025 | Python 3.7, PyCUTEst, pdfo; Knitro 12.2–12.4 with vendor-modified builds; a 16-core Xeon workstation with 32 GB (2019) and a 16-core Xeon Silver with 200 GB (2024) | Very senior; 1–2 students per paper; Artelys engineer as co-developer | Prototyping inside KNITRO depends on a vendor relationship that most groups lack |

---

## 9. Stated method against observed practice (cross-check with 02-methodology)

| 02 item (stated) | What the artefacts show | Verdict |
|---|---|---|
| R4/E4: compare with the dismissed simple baseline | FD-L-BFGS against the DFO incumbents (2018, 2021); update-skipping as their own simple rival (2022) | **Practised** |
| E5/R8: build in recovery; expect the algorithm to be wrong | Recovery procedure ablated (2019); lengthening (2022); noise-level termination flags (2020 code); self-calibrated line search (2025) | **Practised** |
| E3: benchmark methods, not codes; never rank | 2003 and 2008 control implementation effects. But the 1997 web page is a code-vs-code table, and every comparison is between specific codes at default settings | **Partly practised**; see C6 |
| E6: distrust 2-D/3-D pictures | The ICLR 2017 paper's core evidence includes 1-D parametric plots, backed by a sensitivity metric that v2 calls "imperfect" | **Tension**; see C7 |
| J1/R3: trust what survives after trying everything | SQN v1's documented failed approach; 2009 ablation. The regression-QN attempt has no written trace | **Partly traceable** |
| R2: judge theory by practice | Theorem 6 bound plotted against observed accuracy and called "pessimistic" (2022) | **Practised** |
| E7: rewrite code from scratch; commercialise | Not checkable in code (KNITRO is closed source). L-BFGS-B was *patched* in 2011, not rewritten | **Not verifiable** for KNITRO |
| E2: experiments before theory | Noise line: theory (arXiv:1901.09063) sits between two algorithm-plus-experiment papers. KNITRO line: theory first (01 SW3) | **Mixed**, as 02 C1 already records |

---

## Contradictions (kept, not reconciled)

- **C1. Baseline strength in the noisy-DFO line.**
  - 2018/19 chose DFOtr for simplicity, not the fastest code, and still concluded that FDLM "is a very competitive method" (v1 p. 6).
  - v1 also conceded: "Conclusive remarks about the relative performance of the MB and FDLM approaches are, however, difficult to make" (p. 6).
  - 2021 used NEWUOA and found it "more efficient and accurate than the finite-difference l-bfgs method" in the noisy unconstrained case.
- **C2. Their verdict on model-based DFO moves.**
  - 2009: the geometry phase may be dispensable.
  - 2018: direct-search and FI methods "do not, however, scale well with the number of variables" (v2 p. 2).
  - 2021: "more robust in the presence of noise than we expected".
  - 2024: they build their own constrained method on DFOtr, which is "robust and efficient, closely trailing in performance the state-of-the-art method, NEWUOA" (arXiv:2402.11920 p. 6).
- **C3. Handicapping themselves vs. using their own product as the yardstick.**
  - The same group handicaps its own method (lmsize = 1; untuned PBQN; KNITRO's stopping test changed to SNOPT's).
  - Yet it also uses its own commercial solver as both the platform and the comparator (2008, 2021, 2024), with no conflict-of-interest statement in the papers read.
- **C4. Promise vs. delivery on the ICLR review.** The reply said "we will use the terms 'LB solution' and 'SB solution'". v2 still says "minimizer" 45 times and adds only a "loosely" caveat.
- **C5. Two origin stories for the finite-difference noise work.**
  - v1 (2018): "stems from the competition established in 2015 … The winner was the finite difference BFGS method … implemented in the knitro package".
  - Talks (Simons 2017, UCLA 2021; in 02): the approach is the survivor "after trying everything else".
  - The journal version keeps neither.
- **C6. "Never rank codes" (2003) vs. the public 1997 table.** The table is titled "TESTING MINOS AND L-BFGS-B" and linked from the software page as "Numerical results comparing L-BFGS, version Lbfgsb.2.1, and MINOS". The 2003 paper, by contrast, warns against ranking.
- **C7. Distrust of low-dimensional pictures (stated, 2017/2024) vs. 1-D parametric plots as core evidence (practice, 2017).** Both come from the same period and the same project.
- **C8. Dates of the Artelys consulting.** The c. 2023 CV on the GitHub homepage says "2012-2020 Artelys". 01 reports older CV versions giving 2012 or 2014 as the start. Recorded, not resolved.

---

## Gaps (searched or attempted, not found, or not read)

1. **Live OpenReview** was blocked by a bot challenge (API and WebFetch). Only the Internet Archive snapshot of 2024-03-21 was read, so any later replies are unknown. A WebSearch for other OpenReview forums with Nocedal as author found none (1 call).
2. **NeurIPS 2016 (multi-batch L-BFGS) and ICML 2018 (PBQN) reviews**: not public or not found. Whether arXiv:1705.06211 v1 was a rejected conference submission is unknown.
3. **Journal referee reports and response letters**: none public. This leaves the SIOPT, *Math. Program.*, OMS and SISC revisions in §4.2 without their prompts.
4. **The 2011 Remark on Algorithm 778**: not read (403 at `~morales`, 404 at two `~nocedal` paths). Only the code header describes it.
5. **KNITRO internals and history**: closed source. The Artelys "what's new" page returned 404, so when `findiff_estnoise`, `findiff_terminate` and the `bar_murule` variants appeared is unknown. The research-to-product link in §2.8 stays [inferred].
6. **PREQN archive**: not downloaded or read (page only).
7. **Not read for experimental design**: arXiv:1606.04838 (v1 → v3 diff), 1605.06049, 1609.08502, 1710.11258, 2110.06380, 2012.15411. Also the 1980 *Math. Comp.* paper and the 1987/1989 theory papers.
8. **Journal versions**: none read. The v1-to-journal comparisons use the last arXiv version as a proxy (the OMS 2023 page count comes from Crossref, 289–311).
9. **Student theses, lab notebooks, group-meeting records, onboarding documents**: none found in public sources. Handed to agent 04.
10. **The regression-based quasi-Newton attempt** (stated at UCLA 2021): no written trace found.
11. ***Numerical Optimization*, 1st → 2nd edition**: changes not examined. The first-edition errata sheets (PS/PDF) were not opened; only their index page was.
12. **Rejected papers or withdrawn claims**: none identifiable. Absence of evidence, not evidence of absence.
13. **Caption-derived quotes** (UCLA 2021, Purdue 2017, Simons 2017) were not checked against the audio.

---

## Sources

Primary unless marked otherwise. "Read" = the relevant sections were opened in this run.

1. J. Nocedal, software page (KNITRO, L-BFGS, PREQN, CG+, Wedge), Northwestern, "Last modified: February 1, 2008" footer. http://users.iems.northwestern.edu/~nocedal/software.html. Primary.
2. L-BFGS page and distribution `lbfgs_um.tar.gz` (lbfgs.f, sdrive.f; code dated July 1990, archive April 2000). http://users.iems.northwestern.edu/~nocedal/lbfgs.html. Primary; code read.
3. L-BFGS-B page and distributions `Lbfgsb.2.1.tar.gz`, `Lbfgsb.3.0.tar.gz` (README, lbfgsb.f, routines.f, drivers, OUTPUTS). http://users.iems.northwestern.edu/~nocedal/lbfgsb.html. Primary; code read.
4. "Testing MINOS and L-BFGS-B", May 18, 1997. http://users.iems.northwestern.edu/~nocedal/testing.html. Primary; read.
5. CG+ page and `CG+.1.1.tar.gz` (Liu, Nocedal, Waltz; April 2000). http://users.iems.northwestern.edu/~nocedal/CG%2B.html. Primary; read.
6. PREQN page (Morales & Nocedal; release 1.1, file dated 01/01/2011). http://users.iems.northwestern.edu/~nocedal/preqn.html. Primary; page only.
7. Wedge page and `WEDGE.tar.gz` (Marazzi, README dated 4-Sep-2001). http://users.iems.northwestern.edu/~nocedal/wedge.html. Primary; README read.
8. *Numerical Optimization* book page, "Corrections … Second Edition (Last updated May 27, 2008)" (`book/errata2.pdf`) and first-edition errata index (`book/errata.html`), Nocedal & Wright. http://users.iems.northwestern.edu/~nocedal/book/. Primary; read.
9. Bottou, Curtis & Nocedal, "SIAM Review paper – Errata (Last updated: June 30, 2016)", `PDFfiles/opt_ml_errata.pdf` (copy downloaded earlier in this run by agent 01). Primary; read.
10. J. Nocedal, homepage https://jnocedal.github.io/, its repository github.com/jnocedal/jnocedal.github.io (commits 2023-02-13 → 2024-01-16) and `cv_nocedal.pdf` (c. 2023). Primary; read.
11. D. C. Liu & J. Nocedal, "On the limited memory BFGS method for large scale optimization", *Math. Program.* 45 (1989) 503–528, doi:10.1007/BF01589116 (author preprint). Primary; sections read.
12. R. H. Byrd, M. E. Hribar & J. Nocedal, "An Interior Point Algorithm for Large-Scale Nonlinear Programming", *SIOPT* 9 (1999) 877–900, doi:10.1137/S1052623497325107 (author preprint). Primary; §4 read.
13. J. L. Morales, J. Nocedal, R. A. Waltz, G. Liu & J.-P. Goux, "Assessing the Potential of Interior Methods for Nonlinear Optimization", LNCSE 30 (2003) 167–183, doi:10.1007/978-3-642-55508-4_10 (author PDF). Primary; §§1–4 read.
14. R. H. Byrd, J. Nocedal & R. A. Waltz, "Knitro: An Integrated Package for Nonlinear Optimization" (2006), doi:10.1007/0-387-30065-1_4 (preprint July 6, 2005). Primary; §3 read.
15. L. Hei, J. Nocedal & R. A. Waltz, "A Numerical Study of Active-Set and Interior-Point Methods for Bound Constrained Optimization", in *Modeling, Simulation and Optimization of Complex Processes* (Springer, 2008) 273–292, doi:10.1007/978-3-540-79409-7_18 (author PDF). Primary; §§1–3 read.
16. G. Fasano, J. L. Morales & J. Nocedal, "On the geometry phase in model-based algorithms for derivative-free optimization", *OMS* 24 (2009) 145–154, doi:10.1080/10556780802409296 (author PDF). Primary; read.
17. J. Nocedal, A. Wächter & R. A. Waltz, "Adaptive Barrier Update Strategies for Nonlinear Interior Methods", *SIOPT* 19 (2009) 1674–1693, doi:10.1137/060649513. Abstract via OpenAlex API. Primary (abstract only).
18. R. H. Byrd, S. L. Hansen, J. Nocedal & Y. Singer, "A Stochastic Quasi-Newton Method for Large-Scale Optimization", arXiv:1401.7020 v1 and v2; *SIOPT* 26 (2016) 1008–1031, doi:10.1137/140954362. Primary; both versions compared.
19. N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy & P. T. P. Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", arXiv:1609.04836 v1 and v2 (ICLR 2017). Primary; both versions compared.
20. OpenReview forum H1oyRlYgg (ICLR 2017 paper76): reviews, comments, decision. Read via the Internet Archive snapshot of `api.openreview.net/notes?forum=H1oyRlYgg` (captured 2024-03-21). Primary (review record).
21. A. S. Berahas, R. Bollapragada & J. Nocedal, "An Investigation of Newton-Sketch and Subsampled Newton Methods", arXiv:1705.06211 v1 and v4; *OMS* 35 (2020) 661–680, doi:10.1080/10556788.2020.1725751. Primary; v1/v4 compared.
22. R. Bollapragada, D. Mudigere, J. Nocedal, H.-J. M. Shi & P. T. P. Tang, "A Progressive Batching L-BFGS Method for Machine Learning", arXiv:1802.05374 v1 and v2 (ICML 2018). Primary; read.
23. A. S. Berahas, R. H. Byrd & J. Nocedal, "Derivative-Free Optimization of Noisy Functions via Quasi-Newton Methods", arXiv:1803.10173 v1 and v2; *SIOPT* 29 (2019) 965–993, doi:10.1137/18M1177718. Primary; both versions compared.
24. H.-J. M. Shi, Y. Xie, R. H. Byrd & J. Nocedal, "A Noise-Tolerant Quasi-Newton Algorithm for Unconstrained Optimization", arXiv:2010.04352 v3; *SIOPT* 32 (2022) 29–55, doi:10.1137/20M1373190. Primary; §§1, 4–6 read.
25. H.-J. M. Shi, M. Q. Xuan, F. Oztoprak & J. Nocedal, "On the Numerical Performance of Derivative-Free Optimization Methods Based on Finite-Difference Approximations", arXiv:2102.09762 v1; journal version *OMS* 38 (2023) 289–311, doi:10.1080/10556788.2022.2121832. Primary; §§1–2, 4–5, App. B read.
26. F. Oztoprak, R. H. Byrd & J. Nocedal, "Constrained Optimization in the Presence of Noise", arXiv:2110.04355 v1; *SIOPT* 33 (2023) 2118–2136, doi:10.1137/21M1450999. Primary; §4 opening read.
27. S. Sun & J. Nocedal, "A Trust Region Method for the Optimization of Noisy Functions", arXiv:2201.00973 v1; *Math. Program.* 202 (2023) 445–472, doi:10.1007/s10107-023-01941-9. Primary; §4 read.
28. Y. Lou, S. Sun & J. Nocedal, arXiv:2401.15007 v1 and v2; *SISC* 47 (2025) A1335–A1357, doi:10.1137/24M1632279. Primary; both versions compared.
29. M. Q. Xuan & J. Nocedal, "A Feasible Method for Constrained Derivative-Free Optimization", arXiv:2402.11920 v1; *Oper. Res. Lett.* 65 (2026) 107398, doi:10.1016/j.orl.2025.107398. Primary; §3 read.
30. S. Sun & J. Nocedal, "A Trust-Region Algorithm for Noisy Equality Constrained Optimization", arXiv:2411.02665 v1 (journal version not found). Primary; §4 read.
31. arXiv abstract pages (submission histories, submitters, comments) for the 22 preprints found under his name (the 21 in the arXiv author search, plus arXiv:1401.7020), retrieved 2026-09-28, e.g. https://arxiv.org/abs/1705.06211. Primary (records).
32. J. Nocedal, UCLA CS201 seminar, 2021-04-08, transcript `../sources/talks/2021-04-08_ucla-cs201-seminar_4a12aV77CAI.txt` (ASR captions; saved by agent 02 this run). Primary, caption-derived.
33. J. Nocedal, Purdue distinguished seminar, 2017-02-15, transcript `../sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt` (uploader subtitles). Primary, caption-derived.
34. J. Nocedal, Simons Institute talk on zero-order methods, 2017, transcript `../sources/talks/2017_simons-zero-order-dynamic-sampling_OfVZ9gArXiY.txt` (uploader subtitles). Primary, caption-derived.
35. N. S. Keskar, `keskarnitish/large-batch-training` (GitHub; 5 commits 2016–2017), cloned 2026-09-28. Primary (group code; not Nocedal's commits).
36. H.-J. M. Shi & D. Mudigere, `hjmshi/PyTorch-LBFGS` (GitHub; 25 commits 2018–2020), cloned 2026-09-28. Primary (group code).
37. H.-J. M. Shi & Y. Xie, `hjmshi/noise-tolerant-bfgs` (GitHub; 4 commits 2020–2021), cloned 2026-09-28. Primary (group code).
38. Artelys, *Knitro 16.0 User's Manual*, "Knitro options" (`bar_murule`, `findiff_estnoise`, `findiff_terminate`), https://www.artelys.com/app/docs/knitro/3_referenceManual/userOptions.html, retrieved 2026-09-28. Secondary (vendor documentation).
39. Crossref REST API metadata checks for every DOI above, plus Zhu, Byrd, Lu & Nocedal, *ACM TOMS* 23 (1997) 550–560, doi:10.1145/279232.279236; Byrd, Lu, Nocedal & Zhu, *SISC* 16 (1995) 1190–1208, doi:10.1137/0916069; Morales & Nocedal, *ACM TOMS* 38 (2011), doi:10.1145/2049662.2049669; Gilbert & Nocedal, *SIOPT* 2 (1992) 21–42, doi:10.1137/0802003; Morales & Nocedal, *SIOPT* 10 (2000) 1079–1096, doi:10.1137/S1052623497327854; Marazzi & Nocedal, *Math. Program.* 91 (2002) 289–305, doi:10.1007/s101070100264; Shi, Xie, Xuan & Nocedal, *SISC* 44 (2022) A2302–A2321, doi:10.1137/21M1452470. Secondary (bibliographic); these papers themselves were not read.
40. J. L. Morales, "A numerical study of limited memory BFGS methods", *Appl. Math. Lett.* 15 (2002) 481–487, doi:10.1016/S0893-9659(01)00162-8. Crossref metadata only. Secondary; not read.
41. Y. Xie, R. H. Byrd & J. Nocedal, "Analysis of the BFGS Method with Errors", arXiv:1901.09063 (abstract page only). Primary; not read beyond the listing.
42. L. Dinh, R. Pascanu, S. Bengio & Y. Bengio, "Sharp Minima Can Generalize For Deep Nets", arXiv:1703.04933 (abstract page; the critique itself is handled in 01/05). Secondary.
43. Internet Archive Wayback Machine availability and CDX APIs (to locate the OpenReview snapshot). Secondary (access route).
44. WebSearch, 2026-09-28, query `openreview.net forum "Jorge Nocedal"` (1 call). It returned no OpenReview forums; it surfaced jnocedal.github.io. Secondary.
