# Frank E. Curtis: stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Frank E. Curtis (Lehigh University ISE; PhD Northwestern 2007 under Jorge Nocedal; Courant postdoc 2007-09; at Lehigh since 2009) |
| Dimension | 02: stated methodology (what he says research and algorithm design should be) |
| Research date | 2026-09-28 |
| Sources consulted | 53 (48 primary: his own web pages, CV, course syllabi, 24 talk-slide decks, 6 papers or preprints, software pages; 5 secondary: Lehigh news and magazine pieces, Crossref metadata) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`; `private/` was not opened |
| Language | English (per team.json) |

**What was read and how.** Curtis has not published a "how I do research" essay, a blog, or a methodology interview that I could find. His stated method comes from four kinds of source: (a) opinion slides inside his talks, where he regularly puts "take-home message" and "raising awareness" slides (I extracted the text of 24 public slide PDFs from his talks page with pypdf, so figures and spoken asides are missing); (b) the prose on his homepage (research overview, reviewing policy, errata policy, software page); (c) course syllabi, especially ISE 403 *Research Methods*; (d) the introductions of papers written to make a methodological point (the regional-complexity paper, the relative-minimization-profile paper, the SIAM Review survey), plus a few press quotes. Slide citations give the slide number printed on the slide ("slide 15/45"). Items from co-authored papers or joint talks are marked **(co-authored)**, because the stance may belong to the co-authors as much as to Curtis.

**Tags.** [stated] = he said or wrote it; [practice] = what he did (papers, code, tables), recorded here only where it anchors a stated claim (agent 03 checks practice); [observed] = what others wrote about him; [inferred] = my inference, and it must not be quoted as his view. Each item is also marked primary or secondary.

---

## 0. Beliefs he repeats (3 or more independent occasions)

| # | Belief (short form) | Occasions (date: source) | Count |
|---|---|---|---|
| R1 | Worst-case complexity theory for nonconvex optimization misrepresents practice; judge methods by practical efficiency | 2017-10-26 Oaxaca talk; 2018-05-04 Courant talk and 2018-07-03 ISMP talk (the same deck was given at JHU, Rutgers and 2018-08-15 MOPTA); 2018-02 regional-complexity preprint; 2019-08-08 ICCOPT semi-plenary; 2021-04-02 ECOM public lecture; 2025-12 NeurIPS workshop plenary and 2026-04-02 Virginia Tech talk (same slide) | 6+ |
| R2 | Infeasibility (and degeneracy) is an overlooked failure mode. A solver should move to minimizing constraint violation automatically and quickly, inside one algorithm | 2008-03 IOS talk (co-authored); 2011-05-16 SIOPT talk; 2012-03 Copper Mountain talk; 2015-03 SIAM CSE and 2015-07 ExxonMobil talks; 2018-07 ISMP talk; homepage research page (undated) | 6 |
| R3 | No two-phase or switching designs ("don't search for feasibility, then optimize"); build a single algorithm with adaptive transitions | 2008-03 IOS talk (co-authored); 2011-05 SIOPT; 2015-03 CSE; 2022-12 NeurIPS plenary; 2023-09 EUCCO plenary | 5 |
| R4 | Design the outer (nonlinear) solver and the inner (subproblem or linear) solver together, and exploit inexact inner solves | homepage research page; 2015-03 CSE and 2015-07 ExxonMobil talks; 2019-08 ICCOPT; 2021-10 and 2025-10 INFORMS NonOpt talks | 5 |
| R5 | Algorithm comparisons are biased (by test sets, tuning, solver selection, single runs); fair comparison must count tuning effort | 2016/2017 relative-minimization-profile paper (co-authored); 2017-10 Oaxaca; 2021-04 ECOM public lecture | 3 |
| R6 | "SG is not a descent method" (so do not call it SGD) | 2016-11 Google talk; 2021-04 ECOM keynote; 2022-12 NeurIPS plenary; 2023-09 EUCCO plenary; homepage research page | 5 |
| R7 | Do not settle for SG; "we should want more", and advocate adaptive or second-order stochastic methods | 2016-11 Google talk; 2018 SIAM Review (co-authored); 2021-04 ECOM keynote; 2021-04 ECOM public lecture | 4 |
| R8 | Adaptivity (adaptive parameters, steps, sample sizes) is what makes methods practical | 2012 PIPAL paper (conclusion); 2015 CSE/ExxonMobil talks; 2018 regional-complexity paper; 2021 ECOM public lecture; 2023 talk titles ("...with Adaptive Parameters") | 5 |

Claims made only once or twice appear in the layers below and are marked as single statements.

---

## 1. Research taste: what is worth doing, what a good result is

**1.1 Continuous optimization has become too theoretical** [stated, primary] (R1)
- "Continuous optimization has become too theoretical in recent years!" His sub-bullets: "too much emphasis on theoretical performance guarantees; not enough emphasis on practical performance; typical analyses and numerical experiments are biasing optimizers toward certain algorithms, and we should snap out of it", followed by the attributed quote "“gone down a bit of a rathole here” — S.J.W." (presumably Stephen J. Wright, who is also on this team; the attribution is only by initials on the slide) (ECOM public lecture "Nonconvex Optimization: Opportunities and Challenges", 2021-04-02, slide 15/45; repeated in the summary, slide 45/45).
- Earlier and milder: "For nonconvex optimization. . . complexity bounds should be taken with a grain of salt (for now)." and "Parting words: There are other, better motivations for second-order methods." (Oaxaca "Beyond Convexity" workshop, 2017-10-26, slide 4/33).
- 2018, framed as a campaign: "Issues that I believe nonlinear optimizers need to address: [...] Our worst-case analysis for nonconvex optimization is faulty. We should characterize complexity in a different way. Purpose of this talk is to convince you. (Otherwise, e.g., we may turn people off from second-order methods.)" (ISMP 2018, 2018-07-03, slide 4/31; the MOPTA 2018 deck has the same lines).
- 2019, as a self-description: slide title "Practical efficiency, not worst-case complexity", with "I have also worked on worst-case complexity for nonconvex optimization. Achieving good/optimal complexity for practical algorithms." (ICCOPT semi-plenary, 2019-08-08, slide 7/55).
- 2025-26, applied to exact-penalty theory: "It is a mistake to overemphasize the relevance of this theory for practical use." His reasons: exact penalization "only applies for minimizers", "requires a parameter that cannot be known in advance", "In practice, subject to a computational budget, a minimizer is not reached", and "the use of stochastic algorithms makes the theory even less relevant" (NeurIPS 2025 workshop plenary, slide 13/33; Virginia Tech INFORMS student chapter, 2026-04-02, slide 14/37).
- Era note: the shift from pure SQP/IPM design toward critiquing complexity began after the post-2010 wave of nonconvex complexity results (Cartis-Gould-Toint, Carmon-Duchi-Hinder-Sidford, both cited on his 2021 slides 29-30) and after his own optimal-complexity trust-region work (TRACE, 2017). He was then a tenured associate professor. [inferred]

**1.2 A convergence or complexity measure is a choice, and a biased one** [stated, primary] (single statement)
- "Aside: Who's to say these are appropriate? Neither offers a guarantee for suboptimality or distance to a solution. We are choosing the condition to benefit our algorithms!" (about ‖∇f‖ ≤ ε and second-order ε-stationarity; ECOM 2021, slide 21/45).
- "Nonconvex functions, even pth order smooth ones, are too diverse. Better to consider subclasses of problems, or analyze performance regionally" (ECOM 2021, slide 31/45).
- "“Better complexity” has yet to mean “better performance” for nonconvex! They say: “Newton's method is as slow as gradient descent.” This essentially ignores reality." (ECOM 2021, slide 32/45).
- Paper version (co-authored with D. P. Robinson): contemporary analyses give "conservative characterizations based on anomalous objectives rather than on ones that are typically encountered in practice" (abstract); the Cartis-Gould-Toint tightness examples use "objective functions that one can argue are not representative of those encountered in regular practice" (§1, p. 3). Static methods come out worst-case optimal "despite the fact that adaptive algorithms often perform better in practice" (§1.1, p. 4). Source: Curtis & Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", arXiv:1802.01062 (v2, 2018-08-24); *Mathematical Programming* 187 (2021) 579-615, DOI 10.1007/s10107-020-01492-3.

**1.3 Nonconvexity is acceptable and local search is worthwhile** [stated, primary] (R-level: 3 occasions)
- "Even 10 years ago, common sentiment among many continuous optimizers: If your (continuous) problem is nonconvex, then it's a bad formulation. [...] On the contrary, there are worthwhile problems that are nonconvex, and algorithms that do not find global minimizers are worthwhile." (ECOM 2021, slide 11/45). "Two messages, in my opinion: (1) Nonconvexity cannot always be avoided. And that's OK! (2) Local search methods are useful, despite no global solution guarantee." (slide 15/45).
- Talk scoping: "local search, not global optimization" (ISMP 2018, slide 5/31) and "not going to do global optimization" (Courant 2018-05-04, slide 4/42).
- Software statement: NonOpt "is not guaranteed to find a global minimizer of the objective function. Rather, it employs local-search techniques based on (generalized) derivative computations in order to improve as best as it can upon an initial solution estimate." (NonOpt homepage, frankecurtis.github.io/NonOpt, undated, read 2026-09-28).

**1.4 What an algorithm should deliver: two audiences** [stated, primary]
- "What do we want from optimization algorithms? Practitioners: reliable, fast, easy-to-use/write software. Algorithm designers and theorists: convergence guarantees, convergence rate guarantees, “simplicity”" (ECOM 2021, slide 5/45).
- Design targets for large-scale NLP, in his words: "scalable step computation (for solving large-scale problems); effective handling of negative curvature (for handling nonconvexity); superlinear convergence in the primal-dual space (for high solution accuracy); asymptotic monotonicity in a merit function (for consistent improvement); effective active-set detection (for warm-starting)". The last two are "especially important in latency-limited environments—i.e., real-time optimization—when one requires a good approximate solution quickly." (homepage Research page, undated; its grant list runs to 2025).
- The stated core challenge: "to design numerical methods that can solve such problems while maintaining the global and fast local convergence guarantees offered by classical methods (that are only efficient when solving smaller-scale problems)" (Research page).

**1.5 Terminology must be exact: SG is not a descent method** [stated, primary] (R6)
- "(The method is sometimes referred to as “SGD”, where the “D” stands for “descent”, but I have strong feelings against this terminology since it is NOT a descent method!)" (Research page, undated).
- On slides: "Not a descent method! . . . but can guarantee eventual descent in expectation" (Google Research NYC, 2016-11, slide 8/42); "Not a descent method!" (ECOM keynote 2021-04, slide 18/59); "Not a descent method! . . . but eventual descent in expectation" (NeurIPS 2022 plenary, slide 15/42; EUCCO 2023, slide 15/44).
- See Contradiction C5: the same slides carry the title "Stochastic gradient descent".

**1.6 Robustness failures of NLP codes are underrated** [stated, primary]
- "State-of-the-art nonlinear optimization codes fail too often. Reasons are “high” nonlinearity, degeneracy, and infeasibility. People have disputed this, but I have results! (We'll never know the number of users that we've lost.)" (ISMP 2018, slide 4/31). The slide admits an unnamed opposing view (see C7).

**1.7 Pragmatic choice of which theorems to prove** [stated, primary, co-authored with Bottou and Nocedal]
- The SIAM Review survey focuses on strongly convex and in-expectation results "for a few reasons. First, it leads to a focus on results that are relevant to actual machine learning practice [...]". On almost-sure convergence via martingale techniques: "For our purposes, we omit these complications since, in our view, they do not provide significant additional insights into the forces driving convergence of the method." (Inset 4.2 "Perspectives on SG Analyses", arXiv:1606.04838 v3 p. 25; *SIAM Review* 60(2) (2018) 223-311, DOI 10.1137/16M1080173). Compare Contradiction C2.

---

## 2. Problem choice: where problems come from, why now

**2.1 Work on what the community overlooks, especially infeasible instances** [stated, primary] (R2)
- "A major challenge often overlooked in research on nonlinear optimization is the fact that contemporary techniques often perform poorly when all of the problem constraints cannot be satisfied simultaneously." He adds: "Is the problem, as posed, feasible? highly nonlinear? degenerate? some or all of the above?" and "This idea of minimizing an objective function subject to controlled violations in the constraints is surprisingly not widely explored in the nonlinear optimization research community" (Research page, undated; the section calls this "on-going work").
- 2008 (joint with Byrd and Nocedal, during his postdoc): guarantees for infeasible problems are "often treated as an afterthought and the rate at which the method converges can be exceedingly slow" (IOS 2008 talk "Infeasibility Detection in Nonlinear Programming", PDF p. 3; this deck has no printed slide numbers).
- 2011-2012: "Is this how we should formulate optimization problems?" (SIOPT 2011-05-16, slides 4/35 and 30/35; Copper Mountain 2012, slide 4/41). His list of causes of infeasibility: "modeling errors; data inconsistency; branch-and-bound for mixed-integer optimization" (Copper Mountain 2012, slide 5/41). "We should solve min f(x) s.t. x ∈ X [the set of violation minimizers]. (Even better would be a single problem or set of conditions for solving (UP).)" (SIOPT 2011, slide 31/35).
- 2015: "We are interested in algorithms such that if (NLP) is infeasible, then there will be an automatic transition to solving the feasibility problem" (SIAM CSE 2015-03, slide 4/25; ExxonMobil 2015-07, slide 4/40).

**2.2 Consolidate a crowded, fragmented area** [stated, primary quotes in a secondary article]
- On the SIAM Review survey: "We saw the need to take all the different approaches people were proposing, solidify them, and share some perspective on what these algorithms could accomplish [...] Doing so would not only help researchers better understand what others are doing but also characterize these approaches in a way that would help reveal new possibilities and new directions that people should explore." Also: "When you have all these people working in the same area, the wheel tends to get reinvented many times [...] people can look at the landscape of possibilities and identify where their work fits in and what gaps they can fill in our understanding." and "We analyzed that algorithm concisely, generalizing the known theory for it in useful ways, so that someone could take some other algorithms that are modified versions and use the same analysis—citing our work instead of redoing things from scratch." (Lehigh *Resolve* magazine, "Frank Curtis: A deep dive into deep learning", vol. 1, 2020).

**2.3 Foundations over applications, carried to wherever applications appear** [stated in a secondary article]
- The writer's paraphrase: "Curtis' own work revolves around building foundational knowledge, rather than focusing on specific applications—a direction he, as a mathematician, finds particularly satisfying." His quote: "The optimization problems I'm working on might involve energy systems or something else, but to me, it's great that I can take the same expertise and apply it wherever algorithms are used." (*Resolve* 2020).
- Applications appear on the homepage as testbeds: PDE-constrained server-room airflow in Ipopt, multi-plant controller design for nonsmooth methods, supervised learning (Research page). [stated]

**2.4 Follow the new source of problems: data and "informed learning"** [stated, primary]
- "However, in many settings today, data reigns supreme! [...] An important question that arises is: How should information/knowledge be incorporated?" (ISMP 2024 semi-plenary, slide 6/50).
- "Motivated by informed learning when model design + regularization is insufficient [...] physics-informed machine learning; fair (supervised) machine learning; . . . but algorithms are general-purpose, e.g., also for simulation optimization" and "My point: It is worthwhile to explore the use of constrained optimization for informed learning. Penalization is not often the best route; there are other/better algorithms to consider." (Virginia Tech 2026-04-02, slides 9/37 and 14/37).
- "Some of the most exciting applications of nonlinear optimization algorithms in the past few years have been on solving problems arising in machine learning applications" (Research page).
- Era note: the ML turn (2016 onward) came with co-authors from industry and ML (Bottou at Facebook AI Research), the NSF TRIPODS institute (2018-2023) and ONR stochastic-constrained grants (2021-2027) (Research page grant list). [stated grant list; inferred causal link]

**2.5 State the desiderata before designing the algorithm** [stated, primary] (2 occasions)
- "What kind of algorithm do we want? Need to establish what we want/expect from an algorithm." His answers: "Feasible methods are not tractable [...] “Two-phase” methods are not effective . . . so should not search for feasibility, then optimize. Only enforce convergence in expectation. Finally, want to use techniques that can generalize to diverse settings." (NeurIPS 2022 plenary, slide 11/42; EUCCO 2023 plenary, slide 13/44).

**2.6 Formulating research topics is a skill to be taught** [stated, primary]
- ISE 403 *Research Methods*, required for all ISE PhD students, has among its objectives: "Explore how to formulate research topics that are worthy of in-depth investigation and the preparation of articles and other written products for publication." The course project is to write a "research proposal". (ISE 403 syllabus, Fall 2023, 2024 and 2025; wording unchanged). The lecture notes are on a login-only course site and were **not read**.

---

## 3. Idea generation

**3.1 The outer solver must know what the inner solver can deliver: inexactness as the lever** [stated, primary] (R4)
- "One of the key ideas in all of this work is that, in order to have a scalable method capable of solving large-scale problems, one needs to design an algorithm in which the demands of the “outer” nonlinear solver are understood by the “inner” subproblem (typically a quadratic optimization problem or linear system) solver. By observing these demands, one can employ iterative optimization or linear algebra techniques and exploit inexact solves—as opposed to treating the subproblem solver as a “black-box” and/or employing direct factorization methods" (Research page).
- 2015 diagnostic list (the most directly usable statement for solver improvement): "The traditional NLP algorithm classes, i.e., augmented Lagrangian (AL) methods, sequential quadratic optimization (SQP) methods, interior-point (IP) methods may fail or be inefficient when exact subproblem solves are expensive . . . or inexact solves are not computed intelligently; algorithmic parameters are initialized poorly . . . or are updated too slowly or inappropriately; a globalization mechanism inhibits productive early steps . . . or blocks superlinear local convergence. This is especially important when your subproblems are NLPs!" (SIAM CSE 2015, slide 5/25; ExxonMobil 2015, slide 7/40, which also shows a stacked "NLP solver / subproblem solver / linear solver" diagram on slides 5-6/40).
- 2019: "Much of my work: exploiting inexactness for scalable constrained optimization." (ICCOPT 2019, slide 6/55).
- 2021 and 2025: "IMPORTANT: Specialized QP solvers, gradient aggregation, and inexact subproblem solutions mean that added per-iteration cost can be negligible compared to “simple” algorithms." (INFORMS 2021 NonOpt talk, slide 8/25; INFORMS 2025 NonOpt talk, slide 9/30).

**3.2 One adaptive algorithm instead of switching between two** [stated, primary] (R3)
- "Our goal is to design a single optimization algorithm designed for the fast solution of (OPT), or the fast solution of (FEAS) when (OPT) is infeasible, that does not switch between two separate techniques (e.g., no feasibility restoration as in Fletcher and Leyffer, 1997)" (IOS 2008 talk, joint with Byrd and Nocedal, PDF p. 5).
- About existing codes: "Many algorithms/codes do this already, by either switching from solving one problem to the other; transitioning from solving one problem to the other. But are they doing it efficiently?" (SIOPT 2011, slide 5/35).
- "The key idea in this work is to carefully monitor progress toward constraint satisfaction, and to rapidly transition to minimizing constraint violation when consistent progress is not being made. The challenge, of course, is to accomplish this without being too conservative" (Research page).
- 2022-23 form: "“Two-phase” methods are not effective . . . so should not search for feasibility, then optimize." (see 2.5).

**3.3 Carry smooth-optimization machinery into nonsmooth and stochastic settings, with safeguards** [stated, primary]
- "The approaches that my collaborators and I have taken involve adapting a popular technique employed when solving smooth problems and merging it with randomized algorithms for capturing information about the nonsmoothness of the problem functions." BFGS/L-BFGS "have demonstrated beneficial behavior when employed to solve nonsmooth problems" (Research page).
- "Central tenets of NonOpt: Quasi-Newton methods are surprisingly effective for “non” optimization. [...] However, they must be guided with cutting planes and/or gradient sampling. Point sets are critical for nonsmooth optimization." (INFORMS 2021, slide 8/25). The motivating challenge: "Do we need complicated “non” optimization software? Many problems are nonlinear, nonsmooth, and nonconvex, . . . but people say these can be solved with simple algorithms." (slide 5/25).
- For stochastic constrained problems: "Same challenges and questions as for unconstrained [...] New challenges for handling constraints as constraints: (i.e., avoid penalty methods, augmented Lagrangian, etc.); balancing the objective and constraints; degeneracy and infeasibility" (ISMP 2024, NeurIPS 2025 slide 7/33, Virginia Tech 2026 slide 9/37).

**3.4 Adaptivity as a design principle** [stated, primary] (R8)
- "I advocate for adaptive (second-order) algorithms for stochastic optimization." (ECOM 2021, slide 43/45).
- "RC analysis can be used to guide the design of new algorithms. For example, [...] an adaptive algorithm that computes different types of steps depending on properties of derivative values at a given iterate can achieve better RC analysis results than an algorithm that is not adaptive." (arXiv:1802.01062, §1.1, p. 4, co-authored).
- The 2012 PIPAL paper closes by crediting "adaptive updates of ρ promoting fast convergence to the feasible region" (*Math. Prog. Comput.* 4(2) (2012) 181-209, DOI 10.1007/s12532-012-0041-4, p. 204). [stated in a paper]

**3.5 When theory and practice disagree, question the yardstick** [stated, primary]
- "Contemporary complexity theory for nonconvex optimization. . . might not be showing a deficiency of certain methods (e.g., 2nd-order TR); might be showing a deficiency of the characterization strategy." (ISMP 2018, slide 10/31). This is how the regional-complexity paper came about: the analysis was changed, not the algorithm. [stated + inferred link]

**3.6 Efficiency means passing information compactly** [stated, primary] (single statement)
- "This talk is about efficient passing of information. [...] [conveying information in a compact form]" (ICCOPT 2019, slide 8/55, on displacement aggregation in L-BFGS).

**3.7 Wanting more than the current workhorse** [stated, primary] (R7)
- "SG is great! Let's keep proving how great it is! [...] No, we should want more. . . SG requires a lot of tuning; Sublinear convergence is not satisfactory; . . . “linearly” convergent method eventually wins [...] Also, any “gradient”-based method is not scale invariant." (Google 2016, slide 15/42; the ECOM 2021 keynote slide 26/59 has the same text with "“hyperparameter” tuning").
- Co-authored: "The theoretical arguments in the previous section, together with extensive computational experience, have led many in the machine learning community to view SG as the ideal optimization approach for large-scale applications. We argue, however, that this is far from settled." (SIAM Review 2018; arXiv:1606.04838 v3 §5, p. 40).

---

## 4. Experiments and execution

**4.1 Fair comparisons must count tuning** [stated, primary] (R5)
- 2017: "Fairly comparing algorithms: How should we compare optimization algorithms for machine learning? Fair comparison would . . . not ignore time spent tuning parameters . . . demonstrate speed and reliability . . . involve many problems (test sets?) . . . involve many runs of each algorithm. What about testing accuracy?" (Oaxaca 2017, slide 33/33).
- 2021: "My goal is not to advocate for one approach for comparisons. Take-home message: The only way for algorithm comparisons to be fair would be for them to include all computational time spent tuning each algorithm." (ECOM 2021, slide 42/45, citing the Asi-Duchi estimate of 750,000 CPU days for one network).

**4.2 Test-set bias and the tuned incumbent** [stated, primary]
- Performance profiles are "A positive development in algorithm comparisons; Dolan and Moré (2002)", but the drawbacks are that "selection of solvers can skew results; even a large test set might not be enough; do solvers (e.g., default parameters) become biased?" (ECOM 2021, slides 34-35/45).
- "Hard to beat a highly tuned state-of-the-art solver! Curtis (2012). I've seen many papers rejected for this reason." Then: "But if you change the test set, it's a different picture! Curtis (2012). We should not let one test set (or a few) bias all research." (slides 37-38/45). For deep learning: "Only using the same handful of problems, all research is biased toward them." (slide 41/45).
- Anchor in his own practice [practice, primary]: in the 2012 PIPAL paper, Ipopt is more efficient on the CUTEr set, but on degenerate Hock-Schittkowski variants (a constraint −c_i(x)² ≤ 0 added for each constraint) "IPOPT is not only less efficient than both PIPAL-c and PIPAL-a, but it also lags slightly in terms of robustness" (DOI 10.1007/s12532-012-0041-4, pp. 205-206). The paper also adopts Ipopt's bound-relaxation and initial-point rules in PIPAL "to have a fairer comparison with IPOPT" (p. 201). This is the "Curtis (2012)" behind the 2021 slides.

**4.3 Benchmarks should not define success for the reader** [stated, primary, co-authored with T. Mitchell and M. L. Overton]
- "[A]n informative and fair benchmark should allow for different interpretations of success/failure, depending on the priorities of the reader, and evaluators should aim not to define success but present as much relevant benchmark data as possible in a concise and intuitive manner." Also: "Even in the event that one algorithm consistently finds better (lower) minimizers and/or stationary points across a test set of nonconvex problems, there is often little to no grounds for attributing such a success to the properties and design of the algorithm." (Curtis, Mitchell & Overton, "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", *Optim. Methods Softw.* 32(1) (2017) 148-181, DOI 10.1080/10556788.2016.1208749, pp. 16-17 of the author PDF). The same paper admits that they "rely upon our new benchmarking tool to justify our algorithm's performance and utility in the absence of convergence results" (p. 3).

**4.4 Stochastic experiments need repetitions and broader test beds** [stated, primary]
- "There needs to be more work along these lines for stochastic optimization. [...] running a solver on a problem once (or a few times) is not enough; algorithm variations even more plentiful" (ECOM 2021, slide 40/45). On a typical deep-learning plot: "Ok, but what about: other objectives? other networks? other datasets? other # of epochs? other hyperparameter settings? other algorithms?" (slide 41/45).

**4.5 Stress-test with tiny pathological models** [stated request + practice, primary]
- Tables of 2-3-variable infeasible problems across Ipopt, Knitro and Filter, with "(We want your infeasible test problems!)" (SIOPT 2011, slide 6/35). Trivially infeasible AMPL models ("s.t. c: 1 <= 0;", "s.t. c: y^2 + 1 <= 0;", with the AMPL presolver turned off) run through ten solvers, recording whether each declared infeasibility (slides 32-33/35).
- Degenerate and infeasible variants are built mechanically from Hock-Schittkowski models (−c_i² ≤ 0 and c_i² ≤ −1) (PIPAL 2012, pp. 205-206). [practice]

**4.6 Theorem assumptions often cannot be checked, so build a checkable safeguard** [stated, primary]
- "Reality: The conditions in this theorem cannot be verified in practice. They require knowing ∇f(w_k). [...] Stabilized variant (SC-s): Loop over (stochastic) gradient computation until [computable surrogate conditions] hold." (Google 2016, slide 37/42).

**4.7 Defaults tuned for a good answer fast; accuracy is the user's choice** [stated, primary]
- "NonOpt's default parameters have been chosen as those that often allow the software to find a good solution estimate relatively quickly. A user can adjust these parameters through options in the software in order to push the solver to try to find solutions of higher accuracy." (NonOpt homepage, undated).

**4.8 Tooling and release habits** [stated, primary]
- ISE 403 teaches "Computing Skills (Linux, LaTeX, git, make)" and "on-campus (high performance) computing resources" (Teaching page; syllabi 2023-2025).
- Research code is released as clearly labelled prototypes: "Note that this is only a prototype implementation. Please e-mail me if you use the code or with any bug reports, comments, or suggestions" (Software page, for SLQP-GS, StochasticSQP, SCBFGS, TRACE). NonOpt "is designed to be extensible. Ideas borrowed from Ipopt." (INFORMS 2021, slide 7/25).
- Resource context: 2006-2012 prototypes were in Matlab (PIPAL ran on Matlab 7.11 R2010b, PIPAL 2012 p. 202) with large-scale runs in Ipopt with Pardiso (Research page; Curtis, Schenk & Wächter, *SIAM J. Sci. Comput.* 32(6) (2010) 3447-3475, DOI 10.1137/090747634). From 2019 onward he writes C++ (NonOpt). [practice]

---

## 5. Judging results

**5.1 A theory result is judged by whether it represents practice** [stated, primary] (R1; see 1.1-1.2)
- "Ideally, we would weigh worst-case analyses differently depending on the category of method. Some methods actually behave like their worst-case; others don't. [...] focus on worst-case analysis can be a self-fulfilling prophecy" (ISMP 2018, slide 11/31); "Let's emphasize worst-case performance less when actual behavior is better!" (slide 31/31).

**5.2 Say what your own approach does not cover** [stated, primary]
- "We're admitting: Our approach does not always give the complete picture. But the contemporary approach can give a misleading picture." (ISMP 2018, slide 10/31). "For some functions, there are holes, but for others the characterization is complete." (slide 30/31).
- Self-critique slide titled "Playing devil's advocate": "“How much does all of this cost?” O(m²n) + O(m⁴) (LBFGS = O(4mn)) Hence, only reasonable for small m. More expensive than BFGS for m = n!" and "“When does s_{k−m} = S_{k−m+1:k} τ ever hold?” Rarely holds exactly. However, one finds it's often close!" (ICCOPT 2019, slide 27/55; repeated at the Goldfarb workshop 2024-11-08). "Implementation is not trivial." (ICCOPT 2019, slide 33/55).

**5.3 Errors: correct publicly, and escalate by impact** [stated, primary] (failures recorded)
- "If any such error were to have a major impact on a main conclusion of one of our published articles, then we would contact the journal of the article in question to make sure that the conclusion is corrected in some manner. On the other hand, some errors—that do not have a major impact on a main conclusion—are worthwhile to mention somewhere, but do not rise to the level that it is necessary to contact the journal." (Errata page, undated; epigraph "Half my life is an act of revision", John Irving).
- Errors he lists: Corollary 3.14 in Berahas, Curtis, Robinson & Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", *SIAM J. Optim.* 31(2) (2021) 1352-1379, DOI 10.1137/20M1354556; Lemma 3.19 in Curtis, Robinson & Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{-3/2}) for nonconvex optimization", *Math. Program.* 162 (2017) 1-32, DOI 10.1007/s10107-016-1026-2; Lemma 4.9 in Burke, Curtis & Wang, "A Sequential Quadratic Optimization Algorithm with Rapid Infeasibility Detection", *SIAM J. Optim.* 24(2) (2014) 839-872, DOI 10.1137/120880045. The errata texts themselves were **not read** (not on the page as fetched). [practice, recorded here because the policy is stated]

**5.4 Report where the competitor wins** [practice, primary]
- The 2011 slides report his own SQuID method beside Filter on the same 8 infeasible problems, and Filter uses fewer iterations on 5 of them (SIOPT 2011, slide 16/35). The 2012 paper says plainly that "PIPAL-a and especially IPOPT have an edge in terms of efficiency" on the CUTEr set (PIPAL 2012, p. 204). No stated rule was found; this is practice evidence for agent 03.

**5.5 Wall-clock per-iteration speedup with a scaling expectation** [stated, primary] (single statement)
- On the inexact interior-point method in Ipopt: "Each iteration of the algorithm required under 9 minutes, a speed-up of over 75% compared to the default Ipopt algorithm, which required approximately 40 minutes per iteration. It is expected that the speed-up would be even more profound for larger problem sizes" (Research page). The scaling claim is stated as an expectation, not a measurement.

---

## 6. Writing and talks

**6.1 Talks are built around explicit take-home messages and aim to persuade** [stated + practice, primary]
- Recurrent slide types: "Main message of this talk" (Oaxaca 2017), "Raising awareness" and "Purpose of this talk is to convince you" (ISMP 2018), "Take-home message #1/#2" (ISMP 2018, ECOM 2021), "My point:" (NeurIPS 2025, Virginia Tech 2026), "Playing devil's advocate" (2019, 2024). [practice: slide structure, 2017-2026]

**6.2 Technical writing, literature review, data visualization and ethics are core PhD skills** [stated, primary]
- ISE 403 objectives include: "Learn fundamental skills for technical reading, technical writing, and literature reviewing skills"; "Practice how to present data visually in an effective manner"; "Develop a firm understanding and appreciation for ethics in research". Its topics are "Presentation Skills, Time Management, Technical Writing, Research Ethics" (syllabi 2023-2025; Teaching page).
- LaTeX is mandatory: "Once LaTeX is covered in the course, all subsequent work must be submitted as documents produced with LaTeX. There are no exceptions to this requirement." (ISE 403 syllabus 2025).
- He helped set up a technical-writing course: Engr498 *Technical Writing for Scientists and Engineers* "was initially created due to the efforts of a former Lehigh student [...], the former Director of ESL [...], and myself" (CV, last revised 2026-04-07, p. 23).

**6.3 Book-writing style: intuition first, proofs deferred** [secondary]
- The press release for *Practical Nonconvex Nonsmooth Optimization* (Curtis & Robinson, SIAM MOS-SIAM Series, 2025, DOI 10.1137/1.9781611978599) says: "A conversational writing style is used throughout, with detailed proofs placed at the end of each chapter to allow readers to first grasp the core ideas before engaging with technical details." It also describes the book as written "with both students and practitioners in mind" and emphasizing "methods that are both efficient and implementable in practice" (Lehigh Rossin College news, undated, read 2026-09-28). The preface was **not read** (see Gaps).

**6.4 A survey should map the landscape so others can place their work** [stated; see 2.2]

**6.5 Naming** [practice, inferred]
- Paper titles from about 2012 use "Sequential Quadratic Optimization" (for example SIAM J. Optim. 2014, 2021), while his 2006-2010 talks and some 2020-21 talk titles say "SQP". No stated rationale was found. [inferred, low confidence]

---

## 7. Research organisation

**7.1 Reviewing reciprocity, with a fixed monthly quota** [stated, primary]
- "I feel strongly that everyone who submits articles regularly to peer-reviewed publications should contribute proportionally to the reviewing process. On average, I submit no more than 6 peer-reviewed articles per year. (These are almost exclusively “journal papers” that are typically ~25-30 pages full of mathematical proofs.) [...] I contribute sufficiently to the overall system by reviewing 12 articles (of the kind that I submit) per year, i.e., one per month." Mechanism: "I maintain a queue of new articles to review, each of which is assigned to an upcoming month in the calendar when I accept the review invitation. [...] If obtaining the review by the end of that month is acceptable for the editor/journal, then I accept the invitation; otherwise, I decline." (Editorship/Reviewership page, undated). The policy was borrowed: "Borrowing an idea from a colleague".
- Output profile implied by this: at most about 6 long, proof-heavy journal papers a year, not conference-paper volume. [stated]

**7.2 Students as the point of the funding** [stated, primary quote in secondary article]
- "Beyond the scientific contributions that they will enable, what is most meaningful to me is that these projects will support incredibly talented doctoral students who inspire me every day." (Lehigh news on the NSF and AFOSR awards, 2025 or 2026, undated page).

**7.3 Structured PhD onboarding** [stated, primary]
- The purpose of ISE 403: to help students "Develop a firm understanding and appreciation for the expectations of a doctoral student in engineering and how they differ from those of an undergraduate or master's student." (syllabi 2023-2025). He is also ISE PhD Program Director (2016-present) and Director of FACET (Future Academic Career Experiential Training, 2021-present), and sat on the INFORMS 2021 "Academic Job Search Panel" (CV). **What he says inside these roles was not found.**

**7.4 Long collaborations and a scale of team** [practice, primary]
- The Collaborators page (read 2026-09-28) lists 9 former PhD advisees, 4 current PhD students, and 4 former postdocs, plus repeated co-authors (Robinson, Nocedal, Byrd, Wächter, Overton, Burke, Lewis, Gould, Toint, S. J. Wright and others). The long partnership with D. P. Robinson now runs to a joint "Sufficient Descent Labs" site for the book and NonOpt (sufficientdescent.github.io, undated).

**7.5 Software as a first-class research output** [stated, primary]
- The Software page separates "prototype software written by me for various research projects" from software "written by others (in some cases with contributions from me)". The NonOpt paper (with L. Zebiane) stresses that "it has been written to be extensible, allowing a user to include other search-direction computation schemes, globalization mechanisms, or (quasi-)Newton-based strategies" (arXiv:2503.22826, 2025, p. 3).

---

## Contradictions (kept, not reconciled)

- **C1. He criticizes complexity theory while continuing to produce it.** 2017-2021 slides: complexity bounds "should be taken with a grain of salt", "Continuous optimization has become too theoretical". Yet his own output includes optimal-complexity methods (TRACE, *Math. Program.* 162 (2017), DOI 10.1007/s10107-016-1026-2; trust funnel, *SIAM J. Optim.* 28(2) (2018) 1533-1563, DOI 10.1137/16M1108650), and his 2026 summary slide lists "worst-case complexity guarantees" among the achievements of his stochastic SQP line (Virginia Tech 2026, slide 36/37). His own 2019 reconciliation: "Achieving good/optimal complexity for practical algorithms" (ICCOPT 2019, slide 7/55). Both positions are on record.
- **C2. Almost-sure convergence: "no significant additional insights" (2016-2018, co-authored) vs. a headline result (2023-2026).** SIAM Review Inset 4.2 (Bottou, Curtis, Nocedal) leaves out martingale almost-sure results because "they do not provide significant additional insights". Later solo talks carry titles such as "On the Almost-Sure Convergence of the Primal Iterates and Lagrange Multipliers in a Stochastic Sequential Quadratic Optimization Method" (MOPTA 2023) and "Almost-Sure Convergence and Active-Set Identification by Stochastic Algorithms for Constrained Optimization" (UCSD 2025), and the 2026 summary lists "stronger convergence guarantees (almost-sure convergence)". The settings differ (unconstrained SG versus constrained SQP with multipliers) and the early statement is co-authored; recorded as a shift, not resolved.
- **C3. Penalty methods: advocated (2008-2012), then "avoid penalty methods" (2024-2026).** Early talk titles: "A New Penalty-SQP Method" (INFORMS 2008), "Penalty Techniques in SQP and Interior-Point Algorithms" (INFORMS 2009), "A Penalty-Interior-Point Algorithm for Nonlinear Optimization" (ICCOPT 2010), and the PIPAL paper (2012). Later: "handling constraints as constraints: (i.e., avoid penalty methods, augmented Lagrangian, etc.)" (ISMP 2024; NeurIPS 2025 slide 7/33; Virginia Tech 2026 slide 9/37) and "Penalization is not often the best route" (2026 slide 14/37). His stochastic SQP methods still use a merit function with an adaptively updated penalty (merit) parameter (the 2024 ISMP slides discuss the "true" merit-parameter update), so the later slogan may refer only to fixed-weight reformulations. That reading is [inferred]; the literal statements conflict.
- **C4. "No feasibility restoration / single algorithm" (2008) vs. his own data (2011-12).** The 2008 goal names Fletcher-Leyffer restoration as what to avoid. On his own 2011 and 2012 slides, the code labelled "Filter" is the most efficient on several small infeasible problems, and faster than his SQuID on 5 of 8 (SIOPT 2011, slides 6 and 16/35). That "Filter" is filterSQP with a restoration phase is [inferred]; the slides give only the label.
- **C5. SGD terminology.** He states "strong feelings against this terminology" (Research page), yet his Google 2016 (slide 8/42) and ECOM 2021 (slide 18/59) slides are titled "Stochastic gradient descent", immediately followed by "Not a descent method!". This could be a rhetorical device; the usage is recorded as found.
- **C6. Record inconsistency (minor).** The CV lists ISE 403 as taught "S-'23, S-'24, S-'25" (spring), but the linked syllabi are dated Fall 2023, Fall 2024 and Fall 2025. The CV's citation details for two 2024 papers on his 2026 slides (MOR 49(4) pages; IJOO 6(3-4) pages) also differ from Crossref (MOR 49(4) 2212-2248, DOI 10.1287/moor.2021.0154; IJOO 6(3-4) 173-195, DOI 10.1287/ijoo.2022.0008). This does not bear on method; it is noted so no one copies the slide citations.
- **C7. An open dispute he acknowledges.** "State-of-the-art nonlinear optimization codes fail too often. [...] People have disputed this, but I have results!" (ISMP 2018, slide 4/31). Who disputed it, and on what data, was **not found**.

## Gaps

- **No methodology essay, blog, or long-form interview found.** The only press quotes are from *Resolve* 2020 and grant news items. Prize citations and any acceptance remarks (2021 SIAM/MOS Lagrange Prize, 2018 INFORMS Computing Society Prize) were not searched for, because of the 2-call WebSearch budget.
- **No video transcripts.** The ECOM 2021 public lecture and keynote are on GMU Kaltura (Cloudflare anti-bot 403), the One World Optimization Seminar talks are on YouTube (yt-dlp hit a bot check), and the ICML 2021 workshop plenary is on SlidesLive (unsupported URL). Nothing was circumvented, so spoken asides such as "I've seen many papers rejected for this reason" survive only as slide text. No transcripts were saved under `references/sources/talks/`.
- **Book preface not read.** *Practical Nonconvex Nonsmooth Optimization* (SIAM 2025, DOI 10.1137/1.9781611978599): SIAM epubs returned 403 to curl and WebFetch, Waterstones showed a captcha, and no public preface was found. The writing philosophy in 6.3 rests on a press release (secondary).
- **ISE 403 lecture content not read** (login-only course site). Only the syllabi are public, so what he actually teaches about choosing topics, writing, time management and ethics is unknown.
- **Advice to PhD students** (FACET program, 2021 job-search panel, 2014 SIOPT "Forward Looking Panel Discussion"): no record found.
- **Slide coverage.** 24 of about 135 listed talk decks were downloaded and text-searched, chosen for tutorial, plenary, opinion or infeasibility content. The other decks, including 2006-2007 .ppt decks and most departmental seminars, were not read.
- **Undated homepage prose.** The Research, Errata and Reviewing pages carry no dates, so whether a statement is early or late cannot be established from the page.
- **Failures and abandoned directions (stated).** Beyond the errata list, he states no abandoned project. The AggQN "Ideas for m ≪ n" slide appears unchanged, still marked "Preliminary results", in 2019 and 2024, which may mean a stalled line [inferred; for agent 03 to check].
- **Scholar profile not queried** (task scope; agent 01 covers publications).

## Sources

Primary unless marked. All read or fetched 2026-09-28. Slide PDFs are at `https://coral.ise.lehigh.edu/frankecurtis/files/talks/<file>.pdf` (listed at https://coral.ise.lehigh.edu/frankecurtis/talks/).

1. Curtis, F. E. Homepage, Home and bio. https://coral.ise.lehigh.edu/frankecurtis/ (undated). Primary.
2. Curtis, F. E. "Research" page. https://coral.ise.lehigh.edu/frankecurtis/research/ (undated; grants to 2025). Primary.
3. Curtis, F. E. "Editorship/Reviewership" page (reviewing policy). https://coral.ise.lehigh.edu/frankecurtis/editorshipreviewship/ (undated). Primary.
4. Curtis, F. E. "Errata" page. https://coral.ise.lehigh.edu/frankecurtis/errata/ (undated). Primary.
5. Curtis, F. E. "Software" page. https://coral.ise.lehigh.edu/frankecurtis/software/ (undated). Primary.
6. Curtis, F. E. "Teaching" page. https://coral.ise.lehigh.edu/frankecurtis/teaching/ (undated). Primary.
7. Curtis, F. E. "Collaborators/Students/Postdocs" page. https://coral.ise.lehigh.edu/frankecurtis/collaborators/ (undated). Primary.
8. Curtis, F. E. "Talks" and "Talks (Video)" pages. https://coral.ise.lehigh.edu/frankecurtis/talks/ and /talks/talks-video/ (undated). Primary.
9. Curtis, F. E. "Publications" page. https://coral.ise.lehigh.edu/frankecurtis/publications/ (undated). Primary (used for PDF links only).
10. Curtis, F. E. Curriculum Vitae, last revised 2026-04-07. https://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf. Primary.
11. Curtis, F. E. ISE 403 Research Methods syllabi, Fall 2023 / Fall 2024 / Fall 2025. https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2023FallISE403.pdf (and 2024FallISE403.pdf, 2025FallISE403.pdf). Primary.
12. Curtis, F. E. ISE 417 Nonlinear Optimization syllabus, Spring 2019. https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2019SpringISE417.pdf. Primary.
13. Curtis, F. E. (with R. H. Byrd, J. Nocedal). "Infeasibility Detection in Nonlinear Programming", INFORMS Optimization Society Conference, 2008-03. infopt_08.pdf. Primary (joint).
14. Curtis, F. E. and H. Wang. "Infeasibility Detection in Nonlinear Optimization", SIAM Conference on Optimization, 2011-05-16. siopt_11.pdf. Primary.
15. Curtis, F. E. "Infeasibility Detection in Nonlinear Optimization", Copper Mountain Conference on Iterative Methods, 2012-03. copper_12.pdf. Primary.
16. Curtis, F. E. "Adaptive Methods for Large-Scale Nonlinear Optimization", SIAM CSE, 2015-03. cse_15.pdf. Primary.
17. Curtis, F. E. "Recent Adaptive Methods for Nonlinear Optimization", ExxonMobil Research, 2015-07. exxon_15.pdf. Primary.
18. Bottou, L., F. E. Curtis, J. Nocedal. "Stochastic Gradient Methods for Large-Scale Machine Learning" (tutorial), ICML, 2016-06. icml_tutorial_all_16.pdf. Primary (joint).
19. Curtis, F. E. "Stochastic Optimization Algorithms Beyond SG", Google Research NYC, 2016-11. google_16.pdf. Primary.
20. Curtis, F. E. "Worst-Case Complexity Guarantees and Nonconvex Smooth Optimization", CMO Oaxaca "Beyond Convexity" workshop, 2017-10-26. oaxaca_17.pdf. Primary.
21. Scheinberg, K. and F. E. Curtis. "Optimization Methods for Supervised Machine Learning" (tutorial), INFORMS Annual Meeting, 2017-10-23. informs_tutorial_17.pdf. Primary (joint; Part I by Scheinberg).
22. Curtis, F. E. "Algorithms for Nonsmooth Optimization" (tutorial), Northwestern, 2018-03-02. nu_tutorial_18.pdf. Primary.
23. Curtis, F. E. (with D. P. Robinson). "Characterizing the Worst-Case Performance of Algorithms for Nonconvex Optimization", Courant Institute, 2018-05-04. courant_18.pdf. Primary.
24. Curtis, F. E. (with D. P. Robinson). "Characterizing Worst-Case Complexity of Algorithms for Nonconvex Optimization", ISMP Bordeaux, 2018-07-03. ismp_18.pdf. Primary.
25. Curtis, F. E. "Regional Complexity Analysis of Algorithms for Nonconvex Smooth Optimization", DIMACS/TRIPODS/MOPTA, 2018-08-15. mopta_18.pdf. Primary.
26. Curtis, F. E. "New Quasi-Newton Ideas for (Non)smooth Optimization" (semi-plenary), ICCOPT Berlin, 2019-08-08. iccopt_semi_19.pdf. Primary.
27. Curtis, F. E. "Nonconvex Optimization: Opportunities and Challenges" (public lecture), East Coast Optimization Meeting, 2021-04-02. 2021_ecom_public.pdf. Primary.
28. Curtis, F. E. "Optimization Methods for Large-Scale Machine Learning" (keynote), East Coast Optimization Meeting, 2021-04. 2021_ecom.pdf. Primary.
29. Curtis, F. E. "NonOpt: Non(-linear/-smooth/-convex) Optimizer", INFORMS Annual Meeting, 2021-10. 2021_informs.pdf. Primary.
30. Curtis, F. E. "Deterministically Constrained Stochastic Optimization" (plenary), NeurIPS 2022 workshop "Order up!", 2022-12. 2022_neurips.pdf. Primary.
31. Curtis, F. E. "Stochastic Algorithms for Continuous Optimization with Nonlinear Constraints" (plenary), EUCCO Heidelberg, 2023-09. 2023_eucco.pdf. Primary.
32. Curtis, F. E. "Stochastic Algorithms for Nonconvex Constrained Optimization" (semi-plenary), ISMP Montreal, 2024-07. 2024_ismp.pdf. Primary.
33. Curtis, F. E. "Aggregated bfGs", Donald Goldfarb Celebration Workshop, Columbia, 2024-11-08. 2024_don.pdf. Primary.
34. Curtis, F. E. "Nonopt: Nonconvex, Nonsmooth Optimizer", INFORMS Annual Meeting, 2025-10. 2025_informs.pdf. Primary.
35. Curtis, F. E. "Stochastic Algorithms for Nonlinearly Constrained Optimization" (plenary), NeurIPS 2025 workshop on Constrained Optimization for ML, 2025-12. 2025_neurips.pdf. Primary.
36. Curtis, F. E. "Constrained Optimization for Informed Supervised Learning", Virginia Tech INFORMS Student Chapter, 2026-04-02. 2026_vtech.pdf. Primary.
37. Bottou, L., F. E. Curtis, J. Nocedal. "Optimization Methods for Large-Scale Machine Learning", *SIAM Review* 60(2):223-311, 2018. DOI 10.1137/16M1080173; arXiv:1606.04838. Primary (co-authored; full text read at the cited passages).
38. Curtis, F. E. and D. P. Robinson. "Regional complexity analysis of algorithms for nonconvex smooth optimization", *Mathematical Programming* 187:579-615, 2021 (online 2020). DOI 10.1007/s10107-020-01492-3; arXiv:1802.01062. Primary (intro read).
39. Curtis, F. E. and K. Scheinberg. "Optimization Methods for Supervised Machine Learning: From Linear Models to Deep Learning", INFORMS TutORials in OR, 2017, pp. 89-113. DOI 10.1287/educ.2017.0168; arXiv:1706.10207. Primary (abstract only read).
40. Curtis, F. E., T. Mitchell, M. L. Overton. "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", *Optimization Methods and Software* 32(1):148-181, 2017. DOI 10.1080/10556788.2016.1208749 (author PDF CurtMitcOver17.pdf). Primary (§1 and §5 read).
41. Curtis, F. E. "A penalty-interior-point algorithm for nonlinear constrained optimization", *Mathematical Programming Computation* 4(2):181-209, 2012. DOI 10.1007/s12532-012-0041-4 (author PDF Curt12.pdf). Primary (§4 read).
42. Curtis, F. E. and L. Zebiane. "NonOpt: Nonconvex, Nonsmooth Optimizer", arXiv:2503.22826, 2025. Primary (§1 read).
43. Curtis, F. E. and D. P. Robinson. *Practical Nonconvex Nonsmooth Optimization*, SIAM (MOS-SIAM Series on Optimization), 2025. DOI 10.1137/1.9781611978599 (Crossref record only; text not read). Primary (metadata).
44. NonOpt homepage. https://frankecurtis.github.io/NonOpt/ (undated). Primary.
45. Sufficient Descent Labs (Curtis and Robinson). https://sufficientdescent.github.io/ and /practicalnonconvexnonsmooth (undated). Primary.
46. Lehigh Rossin College. "Frank Curtis: A deep dive into deep learning", *Resolve* vol. 1, 2020. https://engineering.lehigh.edu/research/resolve/volume-1-2020/frank-curtis-deep-dive-deep-learning. Secondary (contains direct quotes).
47. Lehigh Rossin College news. "Lehigh ISE faculty publish new book on practical optimization methods" (undated, 2025 or later). https://engineering.lehigh.edu/news/article/lehigh-ise-faculty-publish-new-book-practical-optimization-methods. Secondary.
48. Lehigh Rossin College news. "Frank E. Curtis awarded two federal grants to advance optimization research" (undated, 2025 or 2026). https://engineering.lehigh.edu/news/article/frank-e-curtis-awarded-two-federal-grants-advance-optimization-research. Secondary (contains a direct quote).
49. Lehigh Rossin College news. "Office of Naval Research awards more than $1M to Lehigh ISE" (undated, 2024). https://engineering.lehigh.edu/news/article/office-naval-research-awards-more-1m-lehigh-ise. Secondary.
50. Crossref metadata (api.crossref.org) used to verify: DOIs 10.1007/s10107-016-1026-2, 10.1137/16M1108650, 10.1137/120880045, 10.1137/20M1354556, 10.1137/090747634, 10.1287/moor.2021.0154, 10.1287/ijoo.2022.0008. Secondary (bibliographic).
