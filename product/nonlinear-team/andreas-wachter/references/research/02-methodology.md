# 02 · Stated methodology (what Wächter SAID research and solver work should be)

- **Researcher:** Andreas Wächter (also written Waechter / Wachter). Northwestern University IEMS from 2011 (Professor from 2019). Earlier IBM T. J. Watson Research Center (2002–2011) and a PhD in Chemical Engineering at Carnegie Mellon (1997–2002, advised by L. T. Biegler). His homepage now reads "I moved to Gurobi Optimization", and in Feb 2026 Gurobi lists him as "Senior Developer".
- **Dimension:** Agent 02, stated methodology: what he *claims* about how to do the work. Whether he practises it is left to 03.
- **Research date:** 2026-09-28
- **Sources consulted:** 19. Of these, 14 are primary: his own or co-authored text, read in full or in the relevant sections. 2 are secondary or institutional (the DBLP record and the Gurobi webinar page). 2 could not be read (a 403 and a 404 response). The text layer of 1 more could not be decoded (see Sources). WebSearch was used twice. Every other source was reached with curl or WebFetch on known URLs. No user-supplied material existed: `references/sources/papers|talks|essays|software` were empty, and `private/` was not opened.

**What the evidence base is, and what it is not.** Wächter has no public essay, interview, blog or "how I do research" lecture that could be found. No video talk with subtitles turned up either (one WebSearch was spent on this and found none). His stated methodology therefore has to be read from six kinds of source:

1. the framing chapters of his PhD thesis (2002): introduction, the caveats of the numerical chapter, and conclusions and future work;
2. the "discussion" passages of the Ipopt implementation paper (preprint 2004, *Math. Program.* 2006);
3. two expository community pieces, both co-authored (SIAG/OPT Views-and-News 2003; Optima 2007);
4. two single-authored tutorials (Dagstuhl 2009; Los Alamos CNLS lecture series 2020), plus the 2026 Gurobi webinar slides (co-authored);
5. the Ipopt "HintsAndTricks" wiki (2007);
6. **681 of his own posts to the public Ipopt mailing list (2002–2021).**

Most of this is advice about *building and using a nonlinear solver*. It says very little about choosing research problems, writing papers or supervising students. The file records what was said and marks the empty layers as empty.

**Tags.**
- **[stated]**: he said or wrote it.
- **[stated-joint]**: it appears in a text he co-authored, so the individual author is unknown.
- **[observed]**: others said it about him.
- **[inferred]**: this agent's reading.
- **P / S**: primary / secondary.

**Page references.** They use the printed page of the document. For the thesis, the PDF page is the printed page + 12. The thesis PDF uses a bitmap font, so its text layer was decoded and word spacing restored. The letters of every thesis quote below were checked against the decoded layer, ignoring whitespace; line-break hyphens are removed.

---

## A. Source corpus and its era / resource context

| # | Source | Date | Author voice | Era / resource context |
|---|---|---|---|---|
| S1 | PhD thesis, *An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering*, Carnegie Mellon University | 29 Jan 2002 | single [stated] P | PhD student in chemical engineering, Biegler group. Fortran 77. Tests on 1 GHz dual Pentium III PCs with 1 GB RAM, 3-hour CPU limit. Applications: process engineering / DAE optimization. |
| S2 | Wächter & Biegler, "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming", preprint 12/19 Mar 2004; *Math. Program.* 106(1):25–57 (2006), DOI 10.1007/s10107-004-0559-y | 2004/2006 | joint (first author) [stated-joint] P | Written at IBM Research. 1.66 GHz Pentium IV. 954 CUTEr problems. |
| S3 | Biegler & Wächter, "DAE-Constrained Optimization", *SIAG/OPT Views-and-News* 14(1):10–15 | Apr 2003 | joint [stated-joint] P | Written at IBM, shortly after the PhD. Survey plus an "Open Problems" list. |
| S4 | Bonami, Forrest, Lee & Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", *Optima* 75, pp. 1–4 | Dec 2007 | joint, 4 authors [stated-joint] P | IBM–CMU Open Collaborative Research on MINLP (Bonmin). |
| S5 | Wächter, "Short Tutorial: Getting Started With Ipopt in 90 Minutes", Dagstuhl Seminar Proceedings 09061, DOI 10.4230/DagSemProc.09061.16 | 2009 | single [stated] P | Written at IBM. Hands-on tutorial for users. |
| S6 | Ipopt Trac wiki page "HintsAndTricks" (Wayback capture of 2012-06-10; page last modified 2007-09-07) | 2007 | Wächter wrote the scaling section: in a list post of 13 Mar 2007 he says "I have writting a little bit about scaling at https://projects.coin-or.org/Ipopt/wiki/HintsAndTricks". The rest of the page has no named author. | [stated] P for the scaling paragraph |
| S7 | Ipopt mailing list (public pipermail archive), 681 messages whose From line is Wächter. Parsed locally, with quoted text (">") stripped so that only his own words count. | 2002–2021 (peak 2005–2010) | single [stated] P | Answers to users while he was project leader. Counts below come from regex matching (method stated with each count) and are approximate. |
| S8 | "Numerical Nonlinear Optimization", 4-part lecture series (slides), Center for Nonlinear Studies, Los Alamos National Laboratory | 22 Jun, 29 Jun, 6 Jul, 13 Jul 2020 | single [stated] P | Ulam Scholar at LANL (2019–2020), full professor. Aimed at a broad, non-specialist audience. |
| S9 | Wächter & Bowly, "Local Nonlinear Optimization in Gurobi 13.0" (Quarto slides, gurobi.github.io); webinar 18 Feb 2026 | 2026 | joint [stated-joint] P | At Gurobi, a commercial solver company. The NL barrier ships as a "Preview Feature". |
| S10 | Homepage research overview, CV page and CV PDF (users.iems.northwestern.edu/~andreasw) | CV c. 2020; page frozen after the move to Gurobi | single [stated] P | Self-description of his research programme. |
| S11 | Author-written abstracts: arXiv:2502.11302 (Curtis, Dezfulian, Waechter, 2025); arXiv:1909.08104 (Tasseff, Coffrin, Wächter, Laird, 2019) | 2019, 2025 | joint [stated-joint] P | Northwestern period. |
| S12 | Ipopt documentation, FAQ and AUTHORS pages (coin-or.github.io/Ipopt, v3.14.20) | current | collective ("we") [stated-joint] P | AUTHORS names "Andreas Waechter, project leader (IBM)". |

---

## B. Findings by the seven layers (framework §一)

### Layer 1: Research taste (what is worth doing, what counts as good)

**T1. Good algorithms are general-purpose, robust and flexible enough to be tailored to the application's structure.** [stated] P. Repeated ≥5 times, 2002–c.2020.
- "Many existing NLP solvers are currently not able to cope with these problem sizes, nor do they offer the flexibility to be tailored to specific applications." S1, p. 6 (2002).
- "The comparison of those different options on two different applications … indicate that the best choice depends on the particular problem characteristics. This emphasizes the importance of flexibility of an optimization algorithm." S1, p. 158.
- "Finally, since Ipopt has been designed with the intention to make it possible to tailor it to different engineering applications, it would be worthwhile exploring its potential in fields like PDE-constrained optimization and circuit tuning." S1, p. 163.
- [stated-joint] The Ipopt FAQ says the move to C++ was made "In an effort to make Ipopt more flexible for new algorithm development". S12.
- The homepage research overview (S10) lists three "broad themes": "Development and implementation of general purpose algorithms." / "Specialized algorithms that exploit specific problem structures." / "Introducing techniques and concepts for nonlinear optimization into settings where they have not yet been exploited."

**T2. Research means design, analysis, implementation and application together, not theory alone.** [stated] P. Repeated 3× across 2002–c.2020.
- "The objective of this dissertation is the design, analysis, implementation, and evaluation of a new NLP algorithm that is able to overcome the current bottlenecks, particularly in the area of process engineering." S1, abstract p. i.
- "Its theoretical convergence properties are to be explored and its performance is to be verified on many test cases." S1, p. 6.
- "I'm interested in the development of practical numerical algorithms for computational optimization. This includes the design and theoretical analysis of new methods, as well as their software implementation and practical application." S10, research page (undated, frozen). The CV biosketch repeats "design, analysis, implementation and application".

**T3. Avoid the combinatorics of active-set identification; this is the reason to prefer interior-point methods.** [stated] P. Repeated in 6 documents over 24 years, the most stable stated rationale found.
- Thesis abstract: the method "follows an interior point approach, thereby avoiding the combinatorial complexity of identifying the active constraints." S1, p. i. See also p. 3 (active-bound identification called "an NP-hard combinatorial problem"), p. 6 and p. 157.
- [stated-joint] IP methods "avoid the combinatorial bottleneck of identifying the active inequality constraints". S3, p. 13 (2003).
- "Avoids combinatorial complexity of identifying active set." S8, Part IV slide 31 (2020).
- [stated-joint] "This avoids combinatorial complexity of identifying binding constraints". S9 (2026).

**T4. Convergence assumptions should concern the problem, not the algorithm's own iterates. A method whose limit points "seem arbitrary" is a defect even if a theorem exists.** [stated] P. Main statement is from 2002; related statements on constraint qualifications recur (see J3).
- About published global-convergence proofs that his counterexample defeats: "Thus, this assumption, like the "Regularity Assumption" in [33], pertains to the behavior of the algorithm rather than to the problem statement itself." S1, p. 81.
- Some methods "can be shown not to produce such limit points, which seem arbitrary and do not provide any useful insight to the user." S1, p. 79.
- He criticises a competitor's filter heuristics: "Their approach is different from the one proposed here in many aspects, and no global convergence analysis is given." S1, p. 54. A near-identical sentence is in S2, p. 1. Read together, these imply a standard that heuristics should come with an analysis [inferred].

**T5. Newton directions with exact second derivatives are usually good; safeguards should not get in their way.** [stated] P. Repeated in 3 documents (2002, 2004, 2020).
- "numerical evidence presented in Section 5.1.2 suggests that Newton directions are usually "good" directions (in particular if exact second derivative information is used)". Hence the filter "has the potential to be more efficient than algorithms based on merit functions, as it generally accepts larger steps." S1, pp. 51–52.
- [stated-joint] "this might indicate that in many cases Newton's method does not require a safeguarding scheme (note that second derivatives are used in the computation of the search directions), or alternatively, that many problems in the test set are not very difficult." S2, p. 23. Both readings are left open.
- On inertia regularization: "No regularization required close to 2nd-order sufficient minimum." / "At the end we have unmodified fast Newton steps." S8, Part IV slide 8.

**T6. The algorithm should not converge to non-minimizers; say plainly that the solver only finds local, first-order points.** [stated] P. Repeated in ≥5 documents plus 17 list posts (2004–2011).
- "Incentive: Avoid convergence to non-minimizers of (NLP)." S8, Part IV slide 8.
- "It is important to keep in mind that the algorithm is only trying to find a local minimizer of the problem; if the problem is nonconvex, many stationary points with different objective function values might exist, and it depends on the starting point and algorithmic choices which particular one the method converges to." S5, p. 2 (2009).
- "We cannot guarantee that Ipopt converges really to a minimizer of the problem - we only can garantee that it converges to a stationary point (this is when the termination tests are satisfied)." S7, 19 Oct 2009, "[Ipopt] empty ipopt.out + objective's decrease".
- [stated-joint] "Local optima are often sufficient in practice" / "Much faster to compute than global optima" / "Not suitable for problems with combinatorial aspects". S9 (2026).

### Layer 2: Problem choice (where problems come from, why now)

**P1. Problems come from application bottlenecks: existing codes "reach their practical limits" as models grow.** [stated] P, 2002 (repeated across the thesis's abstract, introduction and conclusions).
- "existing optimization algorithms and their software implementations keep reaching their practical limits, and new methods have to be devised that try to overcome the bottlenecks of the existing ones." S1, p. 2.
- The thesis derives an explicit list of "challenges" from the applications (problem size up to millions of variables; up to 10,000 degrees of freedom; the active-set bottleneck; flexibility about second derivatives and access to Cᵀ; interfaces to simulators) before designing the algorithm. S1, p. 6. The conclusions then map each design decision back to a challenge (S1, p. 157: "The challenges mentioned in Section 1.3 … have motivated its design in the following ways").

**P2. Using the software generates the research questions.** [stated] P, 2002. The same attitude appears in list posts (see E3).
- "Also, continued usage is expected to reveal bottlenecks, either in the implementation or in the underlying mathematical algorithm, and might raise interesting research questions." S1, p. 161.

**P3. The NLP solver is the "heart" of application methods: improve the solver and the applications improve.** [stated-joint] P, 2003.
- "Since the heart of the simultaneous approach is a robust and efficient large-scale NLP solver, improvement in the NLP algorithm will immediately lead to advances in the DAE optimization method." S3, p. 13.

**P4. Standing open problems he named for interior-point NLP (research agenda as stated).** [stated-joint] P, 2003. [stated] P, 2020.
- "Warm starts are needed for nonlinear model predictive control (NMPC) and other applications where DAE optimization must be performed repeatedly with only slightly perturbed data. Whereas this is naturally handled in active set SQP methods, better warm start strategies need to be developed for IP algorithms." S3, p. 13. The same paragraph also names preconditioners for reduced-space CG and handling of nonpositive curvature.
- Seventeen years later: interior-point methods are "Difficult to warm-start" and "Needs a good number of iterations even when starting point is optimal", while "SQP methods can be warm-started well." S8, Part IV slides 31 and 22 (2020).
- CV talk titles (titles only, content not read): "Towards Hot-Started NLP Solvers" (ISMP Berlin, Aug 2012; INFORMS, Oct 2012; UIUC, Sep 2012); "Hot-Starting NLP Solvers" (MIP Workshop, Jul 2014). S10 (CV PDF).
- Repetition count for "IPMs need warm-start strategies": 2003, 2012 (×3 titles), 2014 (title), 2020. That is ≥4, so a real belief. [inferred] He later published a warm-startable SQP-type method for SOCP (SIOPT 2024, DOI 10.1137/22M1507681); whether stated agenda and practice match is for 03.

**P5. Bring nonlinear-optimization techniques into areas that have not used them.** [stated] P, homepage (S10), quoted under T1. No further statement on *how* he picks such areas was found.

**P6. Some problem classes need specialized methods, and a general-purpose NLP solver should say so.** [stated] P, 2006 and 2014 (2×; below threshold).
- "Having said all this, Ipopt will probably not compete 100% with specialized solvers (depends on the solver of course :), which might be able to handle certain degeneracies etc, and also might avoid some overhead." S7, 26 Dec 2006, "Question on quadratic programming".
- For second-order cone constraints, LICQ fails at the apex and Ipopt "will probably fail, or at least perform poorly. This is why there are specialized methods for these second-order cone constraints." S7, 12 May 2014, "[Ipopt] Ipopt for Convex Problems".

### Layer 3: Idea generation

**I1. Ideas come from building a counterexample in which one's own code fails on a "simple, well-posed" problem, then asking which property causes the failure.** [stated] P, 2002.
- "a simple, well-posed example has been presented, on which an unmodified version of Ipopt failed in an unexpected way." S1, p. 72.
- "What property of problem (4.3) could be responsible for the convergence problem?" S1, p. 79. He answers by comparison with SQP: "This situation is a well-known difficulty for another class of optimization methods." S1, p. 79.
- The filter line search is then introduced as the fix (S1, pp. 51–52). [inferred] The stated route is: failure of own code → minimal counterexample → diagnosis by analogy with another method class → remedy with a proof. Only the thesis states it; whether it recurs is for 03.

**I2. Borrow a globalization idea from another framework and change the one piece that blocks the desired property.** [stated] P, 2002.
- The line-search filter "is motivated by the trust region SQP method proposed and analyzed by Fletcher et. al. [35]. An important difference, however, lies in the condition that determines when to switch between certain sufficient decrease criteria; this allows us to show fast local convergence of the proposed line search filter method." S1, p. 52.

**I3. Match the method to the problem structure: the ratio of states to controls, the cost of derivatives, and whether the model is a simulator.** [stated-joint] P, 2003. [stated] P, 2002.
- Sequential DAE approaches: "Because of this cost, second derivatives are rarely available and dense quasi-Newton SQP methods (such as [20]) are best suited for this approach." S3, p. 12. The same article maps multiple shooting to reduced-space SQP, and full discretization to full-space SQP/IP or reduced-space methods, by the state/control ratio (pp. 12–13).
- The thesis lists "different levels of "openness" of the simulation program" (whether systems with the transposed Jacobian can be solved) as something the algorithm must adapt to. S1, pp. 157–158.

No statement was found about where individual ideas came from (no origin story in his own words). Gap.

### Layer 4: Experiments and execution (algorithm engineering, testing, debugging)

**E1. Get the derivatives right before anything else. Use the derivative checker and start from a small instance.** [stated] P. Explicit advice in 13 list posts (2007–2021) plus the 2009 tutorial. The broader keyword count ("derivative checker/test") is 28 posts, 2005–2021. This is the most repeated single piece of execution advice.
- "The first thing to do is always to check that the derivatives are correct (using the derivative checker)." S7, 15 Feb 2012, "[Ipopt] convergence problem".
- "Finally, I would always use the derivative checker to make sure the derivatives are indeed correct." S7, 22 Mar 2012.
- "…you definitely should run the derivative checker to make sure you didn't make a mistake assembling the first derivatives (it is so easy to have a typo here…" S7, 8 Jan 2008.
- "I would run Ipopt''s derivative checker to make sure there are no errors in the first derivatives." S7, 9 Jun 2021 (his last technical answer on the list).
- Tutorial workflow (S5, pp. 14–15), summarised: work out derivatives incl. sparsity; first run with finite-difference Jacobian and L-BFGS on a small instance (n = 5); then add the exact Jacobian and check it with the first-order test; then add the Hessian and check it with the second-order test. "it will be easier to start debugging and checking the results with a small instance." "Also, until the derivatives are correct, there is no point in running Ipopt for many iterations". The exercise ships a "2-mistake" version with "mistakes … purposely included".

**E2. Supply exact second derivatives. Quasi-Newton is a fallback: less robust, and it scales worse with the number of degrees of freedom.** [stated] P. Present in S1 (2002), S3 (2003), S4 (2007), S5 (2009); explicit advice in 13 list posts (2002–2009). That makes ≥17 statements.
- "When process models are implemented from scratch using new modeling tools, automatic differentiation can provide second derivatives of the model equations, which should be exploited by the optimization method for fast convergence." S1, p. 5.
- "By the way, if possible, you should implement second derivatives, it makes quite a difference in terms of efficiency and robustness of the code." S7, 13 Dec 2004.
- "If the second derivatives are not available, you need to use the quasi-Newton option, and this is a) to some degree a heuristic and not as robust as the version using second derivatives, and b) usually not scaling well as the size of the problem increases." S7, 4 Feb 2008.
- On the quasi-Newton option: "the larger the number of degrees of freedom is for your problem …, the more iterations are usually required (as a rule of thumb), whereas the iteration count usually grows only slowly with the dimensionality of a problem when exact Hessian information is used." S7, 1 Aug 2005.
- "This option makes the code usually less robust than if exact second derivatives are used." S5, p. 12.
- Stated exception: "(In general, I would always recommend to use second derivative information if available, and if the Hessian matrix is not dense.)" S7, 27 Dec 2004.

**E3. Scale the problem yourself. The target is gradient entries of about 0.01–100, because a nonlinear solver cannot find good scaling automatically.** [stated] P. Present in S5 (2009) and S6 (2007); explicit scaling advice in 26 list posts (2004–2012).
- "I usually suggest to people that they try to scale the problem so that the non-zero elements in the gradients for the objective and constraint functions are on the order of, say, 0.01 to 100." S7, 13 Mar 2007.
- "For good performance, an optimization problem should be scaled well. … In contrast to linear programming where all derivative information is known at the start of the optimization and does not change, it is difficult for a nonlinear optimization algorithm to automatically determine good scaling factors, and the modeler should try to avoid formulations where some non-zero entries in the gradients are typically very small or very large." S5, p. 12.
- S6 (wiki): the same 0.01–100 target, plus the warning that with Ipopt's default gradient-based scaling "if some of the gradient elements are huge and some are very small, the variables corresponding to the small entries are almost ignored."

**E4. The problem must be smooth. Non-differentiability in the first derivatives is fatal; in the second derivatives it is less harmful.** [stated] P. Present in S1, S5 and S9; 9 list posts (2005–2011).
- "Ipopt is written to solve problems where the functions are a least twice differentiable." S7, 22 Apr 2005 [sic "a least"].
- "the algorithm is much less sensitive to non-smoothness in the second derivatives than in the first derivatives." S7, 24 Nov 2010.
- A three-cause diagnostic he repeats when runs fail: "This can happen, if - your functions are not smooth (i.e., twice differentiable), - the problem is very badly scaled, - the problem fails to satisfy a "constraint qualification"". S7, 27 Dec 2007.

**E5. Reformulate the model to make the solver's job easier (linear before nonlinear, convex before nonconvex, sparse before dense, keep evaluations defined).** [stated] P, 2005–2009. The 2026 advice points the other way; see Contradictions.
- "Linear problems are easier to solve than nonlinear problems, and convex problems are easier to solve than non-convex ones. Therefore, it makes sense to explore different, equivalent formulations to make it easier for the optimization method to find a solution. In some cases it is worth introducing extra variables and constraints if that leads to "fewer nonlinearities" or sparser derivative matrices." S5, p. 13.
- On undefined function values (e.g. log of a non-positive number): "But it is better to avoid such points in the model". He suggests "log(y)" with a new bounded variable y ≥ ε and the constraint h(x) − y = 0. S5, p. 13.
- "I usually suggest to users to use AMPL to experiment with the model formulation for their application, and see how Ipopt (or other solvers) perform." S7, 21 Dec 2007.
- [stated-joint] Modeling burden: "In effect, one shifts some of the burden from the modeler to the solution software. Still, just as we know from MILP and NLP, there are always significant issues that cannot be ignored by a modeler who seeks to solve difficult instances." S4, p. 2 (2007).

**E6. Numerical robustness details matter as much as the algorithm: iterative refinement, pivot tolerances, bound relaxation.** [stated-joint] P, 2004/2006. [stated] 2007 wiki; 2020 slides.
- "In our experience it is very important to use iterative refinement in order to improve robustness of the implementation and to be able to obtain highly accurate solutions." S2, p. 19.
- On relaxing bounds by 10⁻⁸: "Since this perturbation is of the order of the termination tolerance, we believe that this does not constitute an unwanted modification of the problem statement." S2, p. 17. In 2020 the same heuristic is justified by constraint qualifications: "Relaxed solution more likely to satisfy constraint qualification." S8, Part III slide 11.
- "Ill-conditioning is benign for direct symmetric linear solvers." S8, Part IV slide 29. "Computationally, NEVER compute the inverse!" S8, Part I slide 28.
- [stated-joint] The performance and reliability of Ipopt "is dependent on the properties of the selected linear solver", and the paper sets out to test "does the best linear solver vary across NLP problem classes". S11, arXiv:1909.08104 abstract (2019). His list posts discuss linear-solver choice often (keyword count 110 posts, 2002–2012; mostly installation and choice of MA27/MA57/MUMPS/Pardiso).

**E7. Defaults should be robust. When a run fails or speed matters, experiment with the options.** [stated] P, 2009.
- "An effort has been made to choose robust and efficient default values for all options, but if the algorithm fails to converge or speed is important, it is worthwhile to experiment with different choices." S5, p. 11.
- "If it is easy for you to try, I would suggest to just go ahead and see how Ipopt does (I would be interested to know)." S7, 13 Mar 2007.

**E8. Read the iteration log as the primary diagnostic.** [stated] P, 2009; the list repeatedly asks users for output files (keyword count 44 posts, 2002–2012).
- "In a typical optimization run, you would want to see that the objective function is going to the optimal value, and the constraint violation and the dual infeasibility, as well as the size of the primal search direction are going to zero in the end." … "If you see nonzero values even at the very end of the optimization, it might indicate that the algorithm terminated at a critical point that is not a minimizer". S5, p. 10.

### Layer 5: Judging results (benchmarking, when to believe a result)

**J1. A solver comparison measures software at a stage of development, not algorithms. A fair comparison needs an independent party, matched termination criteria, and a per-problem analysis of failures.** [stated] P, 2002. [stated-joint] P, 2004/2006. That is 5 statements in 2 documents; the claim did not reach 3 independent sources.
- "As a consequence, the presented results give only limited information on performance comparisons of the mathematical algorithms, measured for example in iteration count. In particular, implemented heuristics for special cases and ill-conditioning have a large impact on robustness. Therefore, the present results mainly compare the practical performance of software packages at a certain stage of development." S1, p. 131.
- "Such a direct comparison should be performed by an independent party and would have to ensure that the conditions for each method (such as convergence criteria) are as similar as possible. Furthermore, one would have to examine in detail the individual reasons for failure of the solvers on the individual problems." S1, p. 138.
- "The comparison presented here is not meant to be a rigorous assessment of the performance of these three algorithms, as this would require very careful handling of subtle details such as comparable termination criteria etc, and would be outside the scope of this paper. In addition, all three software packages are continuously being improved, so that a comparison might quickly be out of date." S2, p. 24.
- Timing: "Despite this precaution we still observed deviations in some cases of up to 15% and therefore recommend to use the reported CPU times with caution." S1, p. 124.

**J2. Controls built into the benchmark: exclude problems where solvers reached different local optima; include an unguarded "full step" run as a difficulty gauge; include a no-scaling variant when competitors do not scale.** [stated] P, 2002. [stated-joint] 2004/2006.
- Different local solutions: problems are discarded when final objective values differ by more than a relative 10⁻³; "Eq. (5.3) is of course only a simple heuristic." S1, pp. 124–125.
- Full step: "The performance of this option might give an idea of the quality of the search directions and the "degree of nonlinearity" of the considered problems." S1, p. 125.
- "We include a run for IPOPT, for which the automatic problem scaling procedure described in Section 3.8 has been disabled, since the other codes do not perform any scaling of the problem statement." S2, p. 25.
- Test-set hygiene: the AMPL presolve was disabled for CUTE "since some of the problems in the CUTE collection have purposely been formulated in a way that might make them difficult for NLP solvers (e.g. degeneracy)". S1, p. 123.
- Transparency: "Tables with detailed results for every test problem and each solver can be downloaded from the first author's home page". S2, p. 24. The homepage still links these tables (S10). In a list post of 31 May 2016 he pointed a user to them.

**J3. When a run fails, suspect (in order) the user's derivatives, smoothness, scaling and constraint qualifications, then numerical difficulty, and only then a bug.** [stated] P. Repeated across 2007–2014 in the list, and in 2020 in the slides.
- "The reason range from the problem not satisfying certain assumptions to numerical difficulties to possible bugs in imperfect code." S7, 21 May 2010 [sic].
- "If no multipliers exist, algorithms that seek KKT points might have difficulties or fail!" S8, Part III slide 11 (2020).
- Degeneracy / constraint-qualification explanations: 22 list posts (2004–2014).

**J4. Keep the evidence that cuts against your method, and give both readings.** [stated] P, 2002; [stated-joint] 2004.
- After showing the filter is best overall: "Interestingly, exact2 is the winner, if one only considers the 335 problems solved by all options … This might indicate, that there is a number of instances where it pays to be more cautious." S1, p. 129.
- "On the other hand, for the weeds problem, the willingness to take risks pays off in a significantly smaller value of the objective function." S1, p. 128.
- "When facing a relatively high failure rate of 11% we should keep in mind that the CUTE test set is a fairly colorful selection of problems". S1, p. 126.
- On a heuristic: "Even though these heuristics are not frequently activated and the watchdog heuristic might in some cases increase the number of iterations, they appear to have an overall positive effect." S2, p. 12.

**J5. Infeasibility is a result that must be reported quickly and meaningfully. The restoration phase carries the hardest cases, so it must be the most robust part.** [stated] P, 2002; [stated-joint] 2004/2006; restoration or infeasibility discussed in 32 list posts (2002–2010).
- "…the restoration phase is the only step where the filter line search method can fail, and therefore inherits all the difficult cases." S1, p. 160.
- "In summary, the feasibility restoration phase is very important in the sense that it is invoked whenever the progress to the solution becomes difficult, and hence it needs to be very robust." S2, p. 12.
- "Infeasible problems arise, for example due to modeling errors, and a user should be notified quickly of a badly-posed problem." S2, p. 12.
- [stated-joint] 2026: "Some starting points may lead to local infeasibility even when the problem is feasible". S9.

### Layer 6: Writing, talks and teaching

**W1. Teach intuition first; allow some "cheating".** [stated] P, 2020 (1 source).
- "Accessible to broad audience." / "Concentrate on intuition of algorithmic ideas." / "No complicated proofs." / "Some "cheating" (ignoring some subtleties)." S8, Part I slide 2.

**W2. Tutorials should be hands-on and staged, with deliberately broken code to debug.** [stated] P, 2009 (1 source). See E1 (the 1-skeleton / 2-mistake / 3-solution structure, S5 pp. 14–15). The tutorial also states its own scope: "The main goal is to convey enough information to explain the output of the software and some of the algorithmic options available to a user. Rigorous mathematical details can be found in the publications cited in the Introduction." S5, p. 7.

**W3. Structure of his implementation paper as stated in it.** [stated-joint] P. The 2006 paper describes itself as providing "a comprehensive description of the algorithm, including the feasibility restoration phase for the filter method, second-order corrections, and inertia correction of the KKT matrix. Heuristics are also considered that allow faster performance." S2, abstract. [inferred] The stated norm is that implementation papers should publish the heuristics as well as the provable core.

**Observed:** He received INFORMS Graduate Teaching Awards in IEMS for 2011–12 and 2014–15, and was on the 2012–13 Faculty Honor Roll of Northwestern's Associated Student Government. S10 (CV). [observed] P (self-listed record of others' recognition).

No writing advice (how to structure papers, figures, reviews or rebuttals) could be found in his own words. Gap.

### Layer 7: Research organisation (software, collaboration, supervision)

**O1. Open source is the research infrastructure: re-use components, contribute changes back, collect test cases from users.** [stated] / [stated-joint] P. Present in S1 (2002), S4 (2007) and S7 (contribution or patch keywords in 61 posts, 2002–2021).
- [stated-joint] "COIN-OR has become the platform that facilitates the collaboration of optimization researchers to start entirely new projects, exploring and developing new algorithmic ideas, by providing both a sound software basis that can be re-used, as well as the technical forum to coordinate the effort." S4, p. 1.
- [stated-joint] "The success of the project is facilitated by the fact that all essential components were available as open-source code, so that they could be changed (and changes could be contributed back to the project maintainers), and by the object-oriented design of the codes." S4, p. 3.
- "If you want you can send me a (preferably small) instance of your problem where you think the performances could be improved." S7, 4 Mar 2005. Requests for instances, test cases or reproduction recipes appear in 32 posts (2002–2012).
- "This chance already fixes the issue that Ali Baharev reported for the two test cases he put online (Thanks, Ali, for making the test cases available)." S7, 5 Oct 2009 [sic "chance"].

**O2. Design software for extension (object-oriented, single interface point), so that new algorithms and applications can be plugged in.** [stated] P, 2002; [stated-joint] 2007; FAQ.
- "In the implementation of Ipopt, all operations with the constraints are requested through one single subroutine, in order to make it easy to tailor decomposition techniques etc. to particular applications. However, an even larger degree of flexibility could be obtained by a re-implementation in C++, employing object-oriented concepts." S1, p. 162.

**O3. Open-source sustainability and support limits (late statements).** [stated] P, 2021.
- "The Ipopt code has been around for 16 years, but since it is open source we typically do not know what it is used for." The purpose was "to support further funding". S7, 15 Jul 2021.
- "I'm sure you understand that we cannot debug people's code for them." S7, 9 Oct 2021.

**O4. Supervision: what he valued as a student.** [stated] P, 2002 (acknowledgments; 1 source). These are statements about his mentors, not about his own supervision.
- About Biegler: "who gave me the optimal balance of guidance and freedom." S1, p. ii.
- About Nocedal: "his contagious optimism together with his amazing ability to always find new important questions from unexpected viewpoints had a significant and inspiring influence on this work." S1, p. ii.
- No statement about how *he* supervises students was found. The students page (S10) lists co-advised students (with Nocedal, Staum, Nelson/Song and E. Wei), which is practice, not a statement. Gap.

---

## C. Recurring stated claims (≥3 repetitions = real belief)

| # | Claim | Sources (years) | Count | Status |
|---|---|---|---|---|
| R1 | Supply exact second derivatives; quasi-Newton is less robust and scales worse with the number of degrees of freedom | S1 2002, S3 2003, S4 2007, S5 2009, S7 13 explicit posts 2002–2009 | ≥17 | real belief |
| R2 | Check derivatives first (derivative checker, small instance) | S5 2009, S7 13 explicit posts 2007–2021 | ≥14 | real belief |
| R3 | Scale the model (gradients about 0.01–100); a nonlinear solver cannot scale automatically as well as the modeller can | S5 2009, S6 2007, S7 26 posts 2004–2012 | ≥28 | real belief |
| R4 | Avoid combinatorial active-set identification, hence interior-point methods | S1 2002, S3 2003, S8 2020, S9 2026 (+ S1 in 3 places) | 6 | real belief, stable over 24 years |
| R5 | The solver finds local, first-order points only; the starting point matters | S5 2009, S7 17 posts 2004–2011, S8 2020, S9 2026 | ≥20 | real belief |
| R6 | Smoothness (C²) is required; first-derivative kinks are fatal | S1, S5, S7 9 posts, S9 | ≥12 | real belief |
| R7 | Failures often trace to constraint-qualification or degeneracy violations | S1 2002, S2 2004, S7 22 posts 2004–2014, S8 2020 | ≥25 | real belief |
| R8 | Restoration and infeasibility detection must be robust | S1, S2, S7 (32 posts) | ≥34 | real belief |
| R9 | Flexibility / tailoring to application structure | S1 (×4), S3, S10, S12 | ≥7 | real belief (strong in 2002–2007; later statements are homepage-level) |
| R10 | IPMs need warm-start / hot-start strategies; SQP warm-starts well | S3 2003, CV titles 2012 (×3) and 2014, S8 2020 | ≥5 | real belief |
| R11 | User instances and test cases drive improvement; use reveals research questions | S1 2002, S7 32 posts, S4 2007 | ≥30 | real belief |
| R12 | Solver comparisons measure software-at-a-stage and need careful controls | S1 (×4), S2 (×1) | 5 statements, 2 documents | below the 3-source threshold; treat as strong but from one era |

Counting method for S7: regex over his own (non-quoted) text, one count per post. These counts are approximate and include some posts that merely *mention* the topic; the "explicit" counts use stricter advice patterns.

---

## D. Self-reported failures, weaknesses and abandoned directions (stated)

- **His own code failed on a simple problem.** "a simple, well-posed example has been presented, on which an unmodified version of Ipopt failed in an unexpected way." S1, p. 72. This failure became the counterexample paper (*Math. Program.* 88:565–574, 2000, DOI 10.1007/PL00011386) and motivated the filter. [stated] P.
- **Weak points listed openly in the thesis's future work** (S1, pp. 159–162) [stated] P:
  - The restoration phase (TRON) needs robustness improvements, and "it has been observed in some instances that the new iterates delivered from the restoration phase can lead to extremely bad objective function values, so that safeguards in this respect are necessary." (p. 160)
  - Inertia correction sometimes makes "corrections … in a large number of successive iterations, during which only small progress is made". (p. 160)
  - "the current strategy for handling negative curvature within the preconditioned gradient method is not yet sufficiently robust and efficient." (p. 160)
  - "the cheaper preconditioner PCG1 has been observed to impair robustness of the overall algorithm in other applications." (p. 161)
  - The degeneracy heuristic "is a practical heuristic at iterates away from a solution, it will not overcome impoverished local convergence to a solution of the barrier problem" when constraint gradients are dependent. (p. 161)
- **Abandoned direction: the reduced-space quasi-Newton version.** It was a centrepiece of the 2002 thesis, but the Ipopt FAQ says: "There is no reduced-space option in the new C++ version". S12 [stated-joint] P. No statement explaining why was found; the reason was not found.
- **Merit-function line search** was implemented, compared and superseded by the filter as the default. S1, pp. 125–129; S2 §4.1. [stated] P.
- **Performance bottleneck admitted:** Ipopt spends "90% of the computation time within the factorization routine MA27BD" on one problem, and "it might be possible to enhance Ipopt's performance in the future by investigating alternative options for solving the linear system". S1, p. 137 [stated] P. The linear-solver study of 2019 (S11) is the later follow-up [inferred].
- No rejected papers, retractions or published errata by Wächter were found (not searched beyond the sources above). Gap.

---

## E. Era and resource context of the stated methods

- **2002 (CMU PhD, chemical engineering):** single-CPU Linux PCs; Fortran 77; AMPL/ASL for derivatives; the HSL MA27 linear solver. His statements on benchmarking (J1–J2) were written when he was comparing his own code against others' codes, obtained from their authors. Application pull came from process engineering (DAEs, up to 2M variables).
- **2002–2011 (IBM Research):** C++ re-implementation with C. Laird (2005–2006); open source under COIN-OR; industrial applications (circuit tuning, lithography; S10). The mailing-list advice (R1–R8, R11) comes mostly from this period, when he was the project leader handling user support in person.
- **2011–c.2024 (Northwestern, professor):** list activity drops sharply after 2012 (39 posts in 2012, 1 each in 2014 and 2016, 3 in 2021). Stated material from this period is the homepage, the CV, co-authored abstracts and the 2020 lecture slides. Topics broaden to chance constraints, power systems, simulation optimization and noisy functions (S10).
- **Gurobi (move date not found; Senior Developer by Feb 2026):** the only statement from this period is co-authored product slides (S9) for a commercial solver. The advice (avoid auxiliary variables, starting points help, try both local and global) fits Gurobi's expression-based NL modelling API. Its author mix and context differ from the Ipopt-era advice.

---

## Contradictions (kept, not reconciled)

1. **Auxiliary variables: add them (2005/2009) vs avoid them (2026).**
   - 2009: "In some cases it is worth introducing extra variables and constraints if that leads to "fewer nonlinearities" or sparser derivative matrices", with the log(h(x)) → log(y), h(x) − y = 0 trick. S5, p. 13.
   - 2005: "maybe it is possible to reformulate your optimization problem (possibly by introducing auxilliary variables) so that it maybe has more variables and constraints, but so that the Jacobian matrix is sparse." S7, 4 Apr 2005.
   - 2026 [stated-joint]: "Preferable to carry complex expressions right through" / "NL barrier often converges better if we avoid auxiliary variables". S9.
   - Context differs (Ipopt with user-coded sparse derivatives vs Gurobi's expression-tree NL barrier, co-authored with S. Bowly). Which author wrote the 2026 line is unknown.
2. **Safeguards: help or hindrance?**
   - Filter is "the most robust and efficient option" (S1, p. 7), and the step-acceptance criteria "interfere with pure Newton's method in the appropriate circumstances" (S1, p. 129).
   - But on the problems all options solved, "it pays to be more cautious" (S1, p. 129). The unguarded full step even beat the filter on the MITT set (S1, p. 137).
   - He leaves both readings open: Newton needs no safeguard, *or* the test set is easy (S2, p. 23).
3. **Second derivatives: "the best choice depends on the particular problem characteristics" (2002) vs near-blanket advice (2004–2009).**
   - 2002: "the best choice depends on the particular problem characteristics" (S1, p. 158); SR1 "seems to provide faster performance" than BFGS in his reduced-space tests (p. 158).
   - 2004–2009 list: "I would always recommend to use second derivative information if available, and if the Hessian matrix is not dense." (S7, 27 Dec 2004).
   - 2005: "Ipopt has quasi-Newton options, with perform Ok" (S7, 1 Aug 2005), against "The quasi-Newton version of Ipopt is definitely less robust than the exact derivative one." (S7, 8 Jan 2008).
4. **Hands-on user support, early vs late.**
   - 2004: "you could send me your source code (assuming that it is easy to compile :), and I could try to have a look at it". S7, 29 Nov 2004.
   - 2021: "I'm sure you understand that we cannot debug people's code for them." S7, 9 Oct 2021.
   - The seniority and resource context changed (IBM project leader vs professor or Gurobi developer, with a volunteer project).
5. **Comparisons: the stated standard vs what the text itself does.**
   - He states that a fair solver comparison "should be performed by an independent party" (S1, p. 138) and that his comparisons are "not meant to be a rigorous assessment" (S2, p. 24).
   - Yet both documents still conclude in Ipopt's favour: it "compares favorably" (S1, abstract p. ii), and the results show "favorable performance of IPOPT" (S2, p. 27).
   - The 2019 co-authored study issues "linear solver recommendations" (S11).
   - These are recorded as stated; whether the practice fits is for 03.

---

## Gaps

- **No long-form methodology text:** no essay, interview, oral history, award-acceptance speech or "how I do research" talk was found. Wilkinson Prize 2011 and INFORMS Computing Society Prize 2009 citations and responses were not searched (budget). Layers 2 (why-now reasoning), 3 (origin of ideas) and 6 (writing) rest on a thin base.
- **No video transcripts:** one WebSearch for recorded lectures returned none, and no transcripts were saved under `sources/talks/`. The Gurobi webinar (18 Feb 2026) has no recording link on its page. Not read: any recording.
- **Not read:**
  - the IMA short course slides "Constrained Nonlinear Optimization Algorithms" (2016): the homepage link returns 404;
  - Curtis–Schenk–Wächter (2010) PDF on Curtis's site: 403;
  - CAPD report B-00-06 (2000): downloaded, but its PDF text layer could not be decoded;
  - the 2017 book chapter "Nonlinear Optimization Algorithms" (*Advances and Trends in Optimization with Engineering Applications*, pp. 221–235): paywalled or not located;
  - talk content for the CV-listed plenaries (MOPTA 2014, ECCO 2013, PORT 2010, SIAM OP 2008, Czech-French-German 2007): titles only.
- **Supervision:** no statement in his own words on how he advises students (layer 7). Only his 2002 thanks to his own mentors.
- **Gurobi period:** move date and role statements beyond the webinar bio were not found. There is no single-authored statement from this period.
- **Ipopt GitHub Discussions (2021–):** his posts there were not harvested (only the mailing list was). This could add late-period statements.
- **Failures:** no rejected papers, errata or retractions were found. The self-reported weaknesses in D come from the thesis only.
- **Authorship of co-authored texts:** for S2, S3, S4, S9, S11 and S12 his individual voice cannot be separated from his co-authors'.

---

## Implications for Phase 2 (for the synthesiser; all [inferred])

- The most distinctive stated method is a **solver-engineer's diagnostic ladder**: derivatives → smoothness → scaling → constraint qualification / degeneracy → numerics (linear solver, iterative refinement, pivots) → only then algorithm or bug. It is stated ≥3 times in each rung and should be checked against practice in 03.
- **Stated taste criteria usable as quick tests:**
  - Does the method avoid combinatorial active-set work?
  - Does it keep fast Newton steps near a solution?
  - Are the convergence assumptions about the problem rather than the iterates?
  - Does it report local infeasibility meaningfully?
  - Can it be tailored to problem structure without rewriting the core?
- **Stated benchmarking controls:** exclude runs that reach different local optima; include an unguarded Newton baseline; include a no-scaling variant; keep CPU-time caveats; publish per-problem tables. These are directly usable for "improve our solver" requests.

---

## Sources

1. A. Wächter, *An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering*, PhD thesis, Carnegie Mellon University, 29 Jan 2002. http://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf (primary; full text read in the sections cited).
2. A. Wächter, L. T. Biegler, "On the Implementation of an Interior-Point Filter Line-Search Algorithm for Large-Scale Nonlinear Programming", preprint 12 Mar 2004 (rev. 19 Mar 2004), https://optimization-online.org/wp-content/uploads/2004/03/836.pdf; published *Math. Program.* 106(1):25–57, 2006, DOI 10.1007/s10107-004-0559-y (primary, joint; preprint read).
3. L. T. Biegler, A. Wächter, "DAE-Constrained Optimization", *SIAG/OPT Views-and-News* 14(1):10–15, Apr 2003. https://siagoptimization.github.io/assets/views/14-1.pdf (primary, joint; read).
4. P. Bonami, J. J. Forrest, J. Lee, A. Wächter, "Rapid Development of an Open-source Minlp Solver with COIN-OR", *Optima* 75, Dec 2007, pp. 1–4. https://web.archive.org/web/2015/http://www.mathopt.org/Optima-Issues/optima75.pdf (primary, joint; read).
5. A. Wächter, "Short Tutorial: Getting Started With Ipopt in 90 Minutes", Dagstuhl Seminar Proceedings 09061 (Combinatorial Scientific Computing), 2009, DOI 10.4230/DagSemProc.09061.16. https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol09061/DagSemProc.09061.16/DagSemProc.09061.16.pdf (primary; read).
6. Ipopt Trac wiki "HintsAndTricks", last modified 2007-09-07, Wayback capture 2012-06-10. https://web.archive.org/web/20120610120203/https://projects.coin-or.org/Ipopt/wiki/HintsAndTricks (primary for the scaling section; read).
7. Ipopt mailing list archive (pipermail), monthly files 2002–2024, 681 messages from A. Wächter, 2002–2021. https://list.coin-or.org/pipermail/ipopt/. The files cited include 2004-December, 2005-March, 2005-April, 2005-August, 2006-December, 2007-March, 2007-December, 2008-January, 2008-February, 2009-October, 2010-May, 2010-November, 2012-February, 2012-March, 2014-May, 2021-June, 2021-July and 2021-October (`.txt.gz`) (primary; parsed and read).
8. A. Wächter, "Numerical Nonlinear Optimization", Parts I–IV, lecture slides, Center for Nonlinear Studies, Los Alamos National Laboratory, 22 Jun – 13 Jul 2020. http://users.iems.northwestern.edu/~andreasw/pubs/CNLStutorial_1.pdf … _4.pdf (primary; read).
9. A. Waechter, S. Bowly, "Local Nonlinear Optimization in Gurobi 13.0", slides for a webinar held 18 Feb 2026. https://gurobi.github.io/slides/local-nonlinear-v13.html (primary, joint; read).
10. Gurobi webinar page "Local Nonlinear Optimization in Gurobi 13.0" (date and speaker bios). https://www.gurobi.com/resources/webinar-events/local-nonlinear-optimization-in-gurobi-13-0 (secondary / institutional; read via WebFetch).
11. A. Wächter, homepage (index, research, publications, software, students, CV pages), http://users.iems.northwestern.edu/~andreasw/, frozen with the note "I moved to Gurobi Optimization"; accessed 2026-09-28 (primary; read).
12. A. Wächter, Curriculum Vitae (PDF, c. 2020). http://users.iems.northwestern.edu/~andreasw/pubs/CV.pdf (primary; read).
13. F. E. Curtis, S. Dezfulian, A. Waechter, "An Interior-Point Algorithm for Continuous Nonlinearly Constrained Optimization with Noisy Function and Derivative Evaluations", arXiv:2502.11302, 16 Feb 2025 (primary, joint; abstract read).
14. B. Tasseff, C. Coffrin, A. Wächter, C. Laird, "Exploring Benefits of Linear Solver Parallelism on Modern Nonlinear Optimization Applications", arXiv:1909.08104, 17 Sep 2019 (primary, joint; abstract read).
15. Ipopt documentation, FAQ and AUTHORS pages, v3.14.20. https://coin-or.github.io/Ipopt/FAQ.html, https://coin-or.github.io/Ipopt/AUTHORS.html (primary, collective; read).
16. DBLP record for pid 62/4235 (SPARQL export, fetched 2026-09-28; used to check the DOIs cited: 10.1007/PL00011386 [*Math. Program.* 2000, "Failure of global convergence for a class of interior point methods for nonlinear programming"], 10.1137/22M1507681 [SIOPT 2024, SOCP warm starts], 10.1007/S10107-004-0559-Y). https://dblp.org/pid/62/4235 (secondary, bibliographic).
17. A. Wächter, "Constrained Nonlinear Optimization Algorithms", IMA short course slides, 2016, http://users.iems.northwestern.edu/~andreasw/pubs/IMA26.pdf. **Not read: 404.**
18. F. E. Curtis, O. Schenk, A. Wächter, "An Interior-Point Algorithm for Large-Scale Nonlinear Optimization with Inexact Step Computations", *SIAM J. Sci. Comput.* 32(6):3447–3475, 2010, DOI 10.1137/090747634. The PDF at coral.ise.lehigh.edu returned 403. **Not read.**
19. A. Wächter, L. T. Biegler, "Global and Local Convergence of a Reduced Space Quasi-Newton Barrier Algorithm for Large-Scale Nonlinear Programming", CAPD Technical Report B-00-06, Carnegie Mellon University, 2000. http://users.iems.northwestern.edu/~andreasw/pubs/CAPD_B0006_QN-IP.pdf. **Downloaded, but the text layer could not be decoded; not read.**
