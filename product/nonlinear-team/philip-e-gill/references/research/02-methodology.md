# Philip E. Gill: stated methodology (research agent 02)

- **Researcher**: Philip E. Gill, University of California San Diego, Department of Mathematics. UCSD Profiles now lists him as Emeritus Professor. Before UCSD: National Physical Laboratory (UK), then the Stanford Systems Optimization Laboratory (SOL) from 1979. He has been at UCSD since 1988.
- **Dimension**: stated methodology, i.e. what he says research should be. Whether he practises it is left to agent 03.
- **Research date**: 2026-09-28
- **Sources consulted**: 22 (17 primary, 5 secondary; list at the end). WebSearch calls used: 2. No user-supplied material existed: `references/sources/{papers,talks,essays,software}` held only `.gitkeep`.
- **Language**: English (team.json).

## Read this first: what "stated" means for Gill

Gill has not written any first-person essay on how to do research, as far as this pass could find. There is also no interview, oral history, blog, award lecture or PhD-advice piece, and no subtitled talk video (see Gaps). His stated methodology has to be reconstructed from four places:

1. **Normative sentences in the introductions, summaries and asides of his papers and surveys.** Almost all of these are co-authored: with W. Murray, M. A. Saunders, M. H. Wright, E. Wong, A. Forsgren, and PhD students or postdocs (J. H. Runnoe, M. Zhang, J. Brust).
2. **One historical essay** ("George B. Dantzig and systems optimization", 2008, five authors). Here the SOL group says in its own voice how optimization research ought to be organised.
3. **Solver user guides** (SNOPT 7.5, NPSOL 5.0). These give advice to modellers about formulation, verification and suspicion of results.
4. **One lecture abstract** (KU Leuven Simon Stevin Lecture, 2014) and his **UCSD course pages** (2021–2023).

Consequences:

- **Voice.** Nearly every statement is a *collective* voice ("we", "in our opinion", "in our view"). Gill's individual view cannot be separated from his co-authors'. Every item below names its co-authors.
- **Authorship of the guide text.** The user-guide advice may partly descend from earlier SOL manuals (e.g. MINOS). This was **not checked**, so that advice is attributed to the four-author SNOPT team, not to Gill alone.

Tags used below:
- **[stated]**: the text asserts it.
- **[practice]**: what the text reports they did. Included only where needed for context; the full analysis is agent 03's job.
- **[observed]**: a third party describes it.
- **[inferred]**: my synthesis.

Each item also says whether the source is primary (P) or secondary (S), and gives its date.

Source keys (full entries under "Sources"):
- **SIGEST05**: SNOPT, SIAM Review 2005
- **GW10/12**: Gill & Wong, "Sequential quadratic programming methods", report NA 10-03 (2010); published 2012
- **GSW15**: Gill, Saunders & Wong, "On the performance of SQP methods", 2015
- **GR22**: Gill & Runnoe, BFGS report, 2022, revised 2023
- **GBD08**: Dantzig essay, 2008
- **FGW02**: Forsgren, Gill & Wright, "Interior methods for nonlinear optimization", SIAM Review 2002
- **SNUG15**: SNOPT 7.5 User's Guide
- **NPUG**: NPSOL 5.0 User's Guide
- **GW15**: Gill & Wong, QP methods, Mathematical Programming Computation 2015
- **BG23**: Brust & Gill, LDLᵀ trust-region method
- **GZ22**: Gill & Zhang, projected-search interior-point method
- **FGWZ23**: Ferry, Gill, Wong & Zhang, projected-search methods
- **GKR20**: Gill, Kungurtsev & Robinson, SIOPT 2020
- **SSL14**: Simon Stevin Lecture abstract
- **UCSD-courses**: UCSD course pages

Page numbers are journal pages where the PDF is the journal version (SIGEST05, FGW02, GBD08). Otherwise they are the page of the preprint or report PDF that was read.

---

## 1. Research taste (what counts as a good method or result)

**T1. Reliability and efficiency are the twin yardsticks, with robustness defined as convergence on many problems.**
[stated], P. Recurs across 2002–2023; see the repetition table.

- "For quasi-Newton methods for unconstrained optimization, it is valuable to develop methods that are robust, i.e., methods that converge on a large number of problems." (BG23, abstract, 2023; with J. Brust)
- "A practical SQP algorithm requires many features to achieve reliability and efficiency." (SIGEST05, p. 115, §6)
- "The results indicate that SQP methods based on maintaining a quasi-Newton approximation to the Hessian of the Lagrangian function are both reliable and efficient for general large-scale optimization problems." (GSW15, abstract, preprint p. 1)

**T2. A method's theory counts only if it survives floating point. Numerical linear algebra is part of the method, not an implementation detail.**
[stated], P.

- "These results server [sic] as a reminder that numerical stability must be taken into account in numerical optimization. A method may have wonderful theoretical properties, but if it fails to deal with numerical issues these properties simply cannot be realized." (GR22, p. 38, 2023 revision; with Runnoe, a PhD student)
- "In the formulation of practical optimization methods, the choice of the numerical linear algebra method used in some inherent calculation can have a fundamental impact on the formulation of the whole optimization algorithm." (SSL14 abstract, 18 Feb 2014; the only single-author statement found)
- "Since linear algebra is a special interest of the authors, we have devoted extra attention to linear algebraic issues associated with interior methods." (FGW02, p. 528)

**T3. The target is "favorable theoretical properties" *and* suitability for large practical problems. Neither alone suffices.**
[stated], P.

- "Our aim is to describe a new SQP method that has the favorable theoretical properties of the NPSOL algorithm but is suitable for a broad class of large problems, including those arising in trajectory optimization." (SIGEST05, p. 101)
- "A major goal of this article is thus to show connections between classical and modern ideas and to cover highlights of both theory and practice" (FGW02, p. 528)

**T4. Minimal, equivalence-preserving intervention.** Regularization, convexification and elastic relaxation should change the original problem as little as possible, and ideally leave its solution unchanged.
[stated], P. Repeated three times, 2010–2015.

- "This is done by formulating an alternative problem that is always well posed, yet has (x∗,π∗,z∗) as a solution when (x∗,π∗,z∗) exists." (GW10/12, p. 5, on elastic mode)
- "…the form of the subproblem suggests a “natural” definition of the regularization parameter that is motivated by the need to maintain an approximate equivalence between the regularized and unregularized problem." (SSL14, 2014)
- "…designed so that modifications to the original problem are minimized and applied only when necessary." (GSW15, p. 26, on convexification)

**T5. Unification and connections between method families are prized.**
[stated], P.

- "An especially appealing aspect of the interior-point revolution is its spirit of unification, which has brought together areas of optimization that for many years were treated as firmly disjoint." (FGW02, p. 525)
- "In our view, a central and welcome change has been elimination of the formerly widespread article of faith that linear and nonlinear programming are completely different." (GBD08, p. 155)
- "During this evolution, both the theory and practice of SQP methods have benefited substantially from developments in competing methods." (GW10/12, p. 16)

**T6. Software is a first-class research product and should be publicly available.**
[stated], P, in the collective voice of GBD08.

- The SOL group writes approvingly of Dantzig: "In happy (for us) contrast to some of his colleagues who regarded the design and writing of software as trivial or uninteresting, he dedicated vast amounts of his time and energy to generating support for, nurturing, and protecting software-related activities." (GBD08, p. 153)
- "An essential part of GBD’s perspective was that the fruits of all these activities should be freely available to the wider community." (GBD08, p. 152)
- They also praise NEOS and COIN-OR as "both reflecting GBD’s philosophy of providing publicly available access to the latest and best." (GBD08, p. 156)
- His homepage (current, undated) states his interest as "Design and implementation of algorithms for unconstrained optimization, constrained optimization and nonlinear least squares" and lists him as co-author of NPSOL, LSSOL, QPOPT, SQOPT, SNOPT and SNADIOPT. [stated], P.
- **[inferred] tension.** The SNOPT family was not described as freely available in any source read here. The licensing terms were not checked.

---

## 2. Problem choice

**P1. Problems are pulled by applications and by users' growing models.**
[stated], P.

- "Although NPSOL has solved OTIS examples with as many as two thousand constraints and over a thousand variables, the need to handle increasingly large models has provided strong motivation for the development of new sparse SQP algorithms." (SIGEST05, p. 101; OTIS is an aerospace trajectory system)
- The same paper thanks Boeing engineers "for their constant support and feedback during the development of SNOPT." (SIGEST05, p. 127)
- "Recent developments in methods for mixed-integer nonlinear programming (MINLP) and the minimization of functions subject to differential equation constraints has led to a heightened interest in methods that may be “warm started” from a good approximate solution." (GW10/12, abstract, p. 1)
- Course pages (2021–2022): "If time permits, discussion will include some case studies involving real problems." (UCSD-courses, Math 271A/B/C)

**P2. Take the next problem from the stated weaknesses of your own method class, or from the gap between it and its rival.**
[stated], P. Repeated across 2005, 2010, 2015, 2022 and 2023.

- "(It may be argued that almost all subsequent developments in SQP methods are based on attempts to correct perceived theoretical and practical deficiencies in the Wilson-Han-Powell approach.)" (GW10/12, p. 16)
- 2005 agenda: "Future work must take into account the fact that second derivatives are increasingly available. The QP solver should allow for indefinite QP Hessians, and additional techniques are needed to handle even more degrees of freedom." (SIGEST05, p. 127)
- 2015: "These extensions are motivated by some comparisons of first-derivative SQP methods with second-derivative IP methods." (GSW15, p. 3)
- 2022: interior QP solvers "have had limited success within SQP methods because they are difficult to “warm start” from a near-optimal point". The paper's own method is pitched so that "The shifts on the primal and dual variables allow the method to be safely “warm started”". (GZ22, report p. 5)
- 2023: trust-region methods are regarded as more robust but cost more, so "the most popular quasi-Newton implementations use line-search methods. To fill this gap, we develop a trust-region method…" (BG23, abstract)
- **[inferred]** The 2005 agenda (second derivatives, indefinite QP, more degrees of freedom) is exactly what the 2010–2015 work (GW15 SQIC, GSW15 convexification) says it addresses. The stated agenda was followed for a decade.

**P3. Degeneracy, ill-posedness and infeasibility are treated as normal, not exotic.**
[stated], P.

- "Practical NLP problems with degenerate points are very common and it is crucial that an algorithm be able to handle Ĵ(x) with dependent rows." (GW10/12, p. 5)
- "In this context, regularization is a vital tool for resolving the numerical and theoretical difficulties associated with ill-posed or degenerate optimization problems." (SSL14, 2014)
- For MINLP subproblems: "the rapid and reliable detection of infeasibility is a crucial requirement of an algorithm." (GW10/12, p. 5)
- Contrast, same page: for one-off problems "an infeasible problem is generally the result of a unintended formulation or coding error." So the importance of infeasibility handling is made to depend on the application context.

**P4. Choose methods by the resource profile of the problem: derivative cost, degrees of freedom, and whether a sequence of problems or a one-off is being solved.**
[stated], P.

- 2005 design premise: "Second derivatives are assumed to be unavailable or too expensive to calculate." (SIGEST05, p. 99)
- "Hence it is especially effective if the objective or constraint functions (and their gradients) are expensive to evaluate." (SNUG15, p. 1)
- "Unfortunately, there are many practical problems for which even first derivatives are difficult or expensive to compute. Test results from second-derivative methods are unlikely to be representative in this case." (GSW15, p. 3)
- Warm starts and sequences of problems recur: GW10/12 p. 1–3; GW15 p. 2; SIGEST05 §6.1; SNUG15 p. 107; GZ22 p. 5. For example, "if a sequence of related QPs must be solved, then the solution of one problem may be used to “warm start” the next, which can significantly reduce the amount of computation time." (GW15, preprint p. 2)

---

## 3. Idea generation

**I1. Look for formal equivalences between a new method and an old one.**
[stated], P, told as a group story.

- On Karmarkar's 1984 visit: "the SOL researchers, trained in nonlinear optimization in general and barrier methods in particular [23,24], observed the strong similarity between the equations in Karmarkar’s method and those arising in the 1960s logarithmic barrier method of Fiacco and McCormick [12]." (GBD08, p. 154)
- The outcome was Gill, Murray, Saunders, Tomlin & Wright, "On projected Newton barrier methods for linear programming and an equivalence to Karmarkar’s projective method", *Math. Programming* 36 (1986) 183–209, doi:10.1007/BF02592025. [practice]
- The surveys state the same aim: "to show connections between classical and modern ideas" (FGW02, p. 528), and "In this section we review some of the principal developments in SQP methods since 1963 while emphasizing connections to other methods." (GW10/12, p. 16)

**I2. Transfer techniques that work in the unconstrained case into the constrained or projected case.**
[stated], P.

- "…conventional projected-search methods are unable to exploit sophisticated safeguarded polynomial interpolation techniques that have been shown to be effective for the unconstrained case." (FGWZ23, abstract; the motivation for the quasi-Wolfe search)
- "This “convexification” process is related to some well-known methods for unconstrained optimization that modify a subproblem “on-the-fly”." (GSW15, p. 15)

**I3. Combine complementary mechanisms instead of choosing one.**
[stated], P.

- "In nonlinearly constrained optimization, penalty methods provide an effective strategy for handling equality constraints, while barrier methods provide an effective approach for the treatment of inequality constraints." This is the premise for a penalty-barrier hybrid. (GKR20, p. 1067)
- Hybrid QP linear algebra: "This inefficiency may be removed by using a QP solver that maintains an explicit reduced Hessian when the number of degrees of freedom is small, and uses direct factorization when the number of degrees of freedom is large." (GSW15, p. 13)
- GSW15 also proposes an SQP method that "employs both approximate and exact Hessian information" (abstract).

**I4. Let numerical results drive the next idea.**
[stated], P.

- "Before addressing the use of second-derivatives in SQP methods, we present numerical results that have motivated our work." (GSW15, p. 6)
- In GBD08 (p. 155) they praise "GBD’s goal of improving methods by learning from numerical results". The example: early interior-point codes were slow on the netlib problem *israel* because of dense columns, which led to new linear-algebra techniques.

**I5. Start from the linear algebra.** The choice of solver shapes the whole algorithm (SSL14, quoted in T2).
[stated], P.

---

## 4. Experiments and execution

**E1. Test on whole collections, not hand-picked subsets, and say what was excluded and why.**
[stated], P. Four sources.

- "In the interest of complete objectivity, every single unconstrained test problem of dimension n ∈ [2, 5000] available in the CUTEst environment at the time of writing was included and run by each solver." (GR22, p. 25)
- GSW15 runs "almost all the problems from the CUTEst testing environment" (p. 3): 1153 of 1156. The three exclusions are named with a reason (possible floating-point exception), and nonsmooth, unbounded and infeasible problems are kept and listed (pp. 7–8). [stated + practice]
- GW15 gives "Numerical results … for all QPs in the CUTEst test collection" (abstract). SIGEST05 uses "most of the CUTEr and COPS test collections" (abstract).
- Lineage: the SOL group endorses Dantzig's programme that "Software implementing these methods can be written and systematically tested on representative problems" (GBD08, p. 152), and his push for standard LP test sets (netlib, COAL) (p. 155).

**E2. Make comparisons fair by construction.**
[stated], P.

- "The tests are formulated so that the same derivative information is provided to both packages." (GSW15, p. 3)
- SNOPT's optimality tolerance was loosened so that "The larger value of 1.22 × 10−4 was used to match the default optimality tolerance of IPOPT." (GSW15, p. 8) [practice]
- GR22 implements all nine BFGS variants in one MATLAB code base with shared tolerances: "The goal of this report is to implement and test these methods in a uniform, systematic, and consistent way." (p. 1)

**E3. Use performance profiles and explain why averages are biased.**
[stated], P.

- "Averaging also necessitates discarding problems that were not solved. In this case the failed problem can be removed for all solvers or only for those that failed, both of which bias the results against more robust solvers." (GR22, p. 25)
- GSW15 profiles both solve time and function evaluations (pp. 10–11), because the right metric depends on the relative cost of evaluations. GR22 p. 27 makes the same trade-off explicit.

**E4. Define success and failure precisely and conservatively.**
[stated], P.

- "A run was considered to have “failed” if a final point of local infeasibility was declared for a problem that is known to be feasible." (GSW15, pp. 9–10)
- "As this study does not recognize a qualitative distinction between a local and global solution, the outcomes for fletcher and lootsma are listed as successful." (GSW15, p. 10)

**E5. Stratify results by problem characteristics.** Degrees of freedom, constraint type and derivative availability are used instead of a single aggregate.
[stated] (GSW15, pp. 13, 26), P.

**E6. Modelling hygiene: verify derivatives, bound away from singularities, give good starts, order related problems.**
[stated], P, solver-guide voice. Repeated in two guides roughly 14 years apart.

- "Verify level 3 should be specified whenever a new function routine is being developed." (SNUG15, p. 85)
- "For maximum reliability, it is preferable for the user to provide all partial derivatives (see Chapter 8 of Gill, Murray and Wright [GMW81], for a detailed discussion)." (NPUG, p. 19; guide revised 2001)
- "…the Verify parameter (see §8.1) should be used to check the calculation of any known gradients." (NPUG, pp. 11, 19)
- "(The log singularity is more serious. In general, keep x as far away from singularities as possible.)" (SNUG15, p. 78)
- "Whenever practical, a series of related problems should be ordered so that the most tightly constrained cases are solved first." (SNUG15, p. 107)
- The pointer to *Practical Optimization* Chapter 8 shows that the book holds the long form of this advice. That chapter was **not read**.

---

## 5. Judging results

**J1. Theory alone cannot rank methods; claims need systematic testing.**
[stated], P. Four statements, three of them in one 2022/23 report.

- "Unfortunately, there is no known analytical means of determining the relative performance of these methods on a general nonlinear function, and there is a real need for extensive experimental testing to justify the theoretical basis of each approach." (GR22, p. 1)
- "The difficulty of judging the impact of the many theoretical developments of quasi-Newton methods emphasizes the importance of practical testing to support claims of improved reliability or convergence." (GR22, p. 4)
- "…the reason for this practical superiority is not fully understood." (GR22, p. 4, on BFGS)
- See also T2 (GR22, p. 38).

**J2. Small or shared-subset comparisons mislead.**
[stated], P.

- "It is important to emphasize the need for uniform analysis and systemic numerical testing in order to draw meaningful conclusions about these algorithms’ relative performance. Without this kind of rigorous comparison, results have the potential to be misleading." (GR22, p. 32)
- The example given: a published adaptive-scaling method looks superior on the 38 problems shared with its source paper, but "if the test set is expanded to the full 275 problems and the more relevant metrics are measured then it is clear from Figure 11 that the suggested method is actually harmful to the methods performance." (GR22, p. 32)

**J3. Distrust results that are too good, and always ask whether a local optimum is the one wanted.**
[stated], P, solver-guide voice.

- "For example, if the objective value is much better than expected, SNOPT may have obtained an optimal solution to the wrong problem! … Verifying that the problem has been defined correctly is one of the more difficult tasks for a model builder." (SNUG15, pp. 93–94)
- "If nonlinearities exist, one must always ask the question: could there be more than one local optimum?" (SNUG15, p. 94)
- "Our advice is always to specify a starting point that is as good an estimate as possible, and to include reasonable upper and lower bounds on all variables… We expect modelers to know something about their problem, and to make use of that knowledge as they themselves know best." (SNUG15, p. 94)

**J4. Test "conventional wisdom" and community consensus against data.**
[stated], P. Four sources, 2002–2023.

- "The conventional wisdom is that when solving a general nonlinear problem “from scratch” … software based on an IP method is generally faster and more reliable than software based on an SQP method." Then: "This claim is difficult to verify, however…". And: "…conclusions concerning the relative performance of first-derivative IP and SQP methods are more nuanced than the conventional wisdom." (GSW15, p. 3)
- "(Surprisingly, most authors in the optimization community have dismissed factored Hessian methods; see, e.g., Grandinetti [12,13] Nocedal and Wright [16, p. 201].)" (GR22, p. 37)
- On barrier methods: "Vague but continuing anxiety about barrier methods eventually led to their abandonment…" (FGW02, p. 525). And: "…by a strange twist of fate, ill-conditioning, their longtime bugbear, has recently been shown not to be harmful under circumstances that almost always hold in practice." (p. 528) And: "Despite recent complete analyses of the ill-conditioning associated with interior methods, its effects remain widely misunderstood." (p. 565)
- "To the surprise of many (including the authors of this paper), the nonlinear barrier method was obviously competitive with the simplex method…" (GBD08, p. 155). They admit their own prior expectation was wrong.

**J5. No universal winner; say where each method is best.**
[stated], P. Four sources, 2005–2015.

- "Ultimately, for every problem that is best solved by an SQP code, there will likely exist another that is best solved by an IP code." (GSW15, p. 26)
- "Broadly speaking, the advantages and disadvantages of SQP methods and interior methods complement each other." (GW10/12, p. 3)
- On LANCELOT: "It complements SNOPT and the other methods discussed above." (SIGEST05, p. 102)
- SNOPT "is best suited for problems with a moderate number of degrees of freedom (say, up to 2000)" (SIGEST05, abstract). SNUG15 p. 1 says the same.

**J6. Report your own solver's failures and interpret them.**
[stated, with practice], P.

- On SNOPT's 25 "false infeasibility" results: "This large number of false infeasibilities provides a somewhat misleading picture of the effectiveness of SNOPT7 for finding a feasible point." (GSW15, p. 10) The paper then re-examines each case. **[inferred]** This is both self-criticism and defence. The failures are counted as failures in the table (Table 2) and discussed in the text.

**J7. Openness is a precondition of judgement.** The group notes that Karmarkar's proprietary code blocked independent testing: "because the software implementing his method was proprietary, researchers outside AT&T were unable to perform comparative numerical tests as they had with Khachiyan’s method." (GBD08, p. 154)
[stated], P.

---

## 6. Writing and talks

**W1. Organise surveys historically and by "influential" threads rather than a forced taxonomy. Say that the choice is an opinion.**
[stated], P.

- "The complex interrelationships that exist between optimization methods make it difficult (and controversial) to give a precise taxonomy of the many different SQP approaches. Instead, we will discuss methods under four topics that, in our opinion, were influential in shaping developments in the area." (GW10/12, p. 16)

**W2. Write surveys for non-experts and admit the limits of coverage.**
[stated], P.

- "Because this is a survey intended for nonexperts, we have included a substantial amount of background material on optimality conditions in section 2." (FGW02, p. 529)
- "We apologize in advance to all those whose favorite topics or works have not been mentioned here." (FGW02, p. 529)
- "Our omission of any discussion of software is the most obvious lack." (FGW02, p. 590)

**W3. State the negatives of your own approach in the introduction.**
[stated], P.

- GW10/12 pp. 2–3 has an explicit "On the negative side" paragraph for SQP ("it is difficult to implement SQP methods so that exact second derivatives can be used efficiently and reliably") and a matching one for interior methods.
- SIGEST05 p. 127: "indefinite QP subproblems raise many practical questions, and alternatives are needed when second derivatives are not available."

**W4. A light literary voice is acceptable.**
[stated], P.

- FGW02 opens with an Austen pastiche: "It is a truth universally acknowledged that the field of continuous optimization has undergone a dramatic change since 1984." (p. 525)
- It closes: "But for those of us who enjoy nonlinearity and its difficulties, this is a privilege rather than a burden." (p. 590)

**W5. Teaching statements** (UCSD-courses, 2021–2023). [stated], P.

- The graduate sequence "is intended as an introduction to the design and analysis of algorithms for numerical optimization… for graduate students … who want to develop an understanding of practical methods for optimization."
- "Matlab enables the student to concentrate on the fundamental ideas of numerical optimization without becoming distracted by the rigors of mental arithmetic."
- Math 171B (Spring 2023): "it must be emphasized that mathematical programming has no direct connection with computer programming." The same page says "The aim of the class is for students to understand the basic theory and methods for nonlinear optimization problems, determine whether a problem has a solution or not, and gain practical experience by utilizing state-of-the-art tools." This page's template differs from his other course pages, so its author may be a TA or the department (not checked).

---

## 7. Research organisation (time, team, students, agenda)

**O1. The systems-optimization-laboratory model, endorsed.**
[stated], P, collective voice. Dantzig's five-part programme is summarised with approval (GBD08, p. 152). A "critical mass" of people is needed so that:

1. "Representative problems can be modeled mathematically;"
2. "General-purpose optimization methods can be devised;"
3. "Software implementing these methods can be written and systematically tested on representative problems;"
4. "Insights can be obtained into the nature of the problems and the properties of the general methods;"
5. "Based on these insights, methods can be developed to take advantage of the special structure of the most interesting and important problems."

"In our view, GBD deserves enormous credit … for his pioneering and enduring contributions to modeling and optimizing complex systems." (GBD08, p. 156)

**[inferred]** This five-step loop is the closest thing to a stated research workflow for Gill. It matches what his papers say they do: model, general method, software, systematic test, specialise.

**O2. Lineage in numerical analysis.** "We note for completeness that, in addition to GBD, Martin Beale (Imperial College), Gene Golub (Stanford), and Jim Wilkinson (National Physical Laboratory) influenced the early SOL work on numerical software by the present authors." (GBD08, p. 153)
[stated], P.

**O3. Funding realities for software research.**
[stated], P.

- "…in those days United States government agencies were reluctant to fund software development, which was not considered to be fundamental research." (GBD08, p. 153)
- Dantzig funded SOL "by bootstrapping grants in optimization that emphasized mathematical theory without mentioning any of the software-related activities that he planned to include." (p. 153)
- In 2007/8: "obtaining sustained government funding for software development remains a challenge." (p. 156)

**O4. Students must "math it up".** PhD students with practical inclinations at SOL "were warned by George that they needed to “math it up” to pass muster with the primarily theoretical OR Department." (GBD08, p. 153)
[stated], P. This is Dantzig's advice reported by the group. Whether Gill gives the same advice is **not known**.

**O5. Industrial users as collaborators.** Boeing thanks (SIGEST05, p. 127). SNUG15 p. 107 thanks named users "for their feedback while running SNOPT on numerous examples".
[stated], P.

**O6. Supervision.** No stated philosophy of supervision was found. The only explicit supervisory statement is a teaching preference: "I prefer not to answer technical questions by email ( n emails for me to understand your question, m emails for you to understand my answer), but students are welcome to attend my office hours or see me after class." (UCSD-courses, Math 271B, Winter 2022)
[stated], P. Gill's homepage lists 25 PhD students (1981–2024) and 4 postdocs [practice, P].

---

## Claims repeated three or more times (the real beliefs)

| # | Belief (my wording; quotes above) | Count and where | Span |
|---|---|---|---|
| R1 | Reliability/robustness and efficiency are the joint yardsticks (T1) | ≥5: SIGEST05 p. 115 and p. 127; GSW15 abstract; BG23 abstract; FGWZ23 abstract ("substantially more efficient and reliable"); SSL14 ("robustness and the efficiency") | 2005–2023 |
| R2 | Warm starts, good starting points and sequences of related problems matter; this is a core SQP/active-set advantage (P4) | ≥6: GW10/12 pp. 1–3; GW15 p. 2; SIGEST05 §6.1; SNUG15 pp. 94, 107; GZ22 p. 5 | 2005–2022 |
| R3 | Systematic testing on whole collections, with fair and uniform conditions, is needed to judge methods (E1, E2, J1, J2) | ≥5: GR22 pp. 1, 4, 25, 32; GSW15 p. 3; GW15 abstract; SIGEST05 abstract; GBD08 pp. 152, 155 | 1986–2023 |
| R4 | Numerical linear algebra and stability decide whether theory is realised (T2, I5) | ≥4: GR22 p. 38; SSL14; FGW02 p. 528; GW10/12 pp. 2–3 | 2002–2023 |
| R5 | SQP and IP (and other families) are complementary; no universal winner (J5) | ≥4: GW10/12 p. 3; GSW15 p. 26; SIGEST05 p. 102; GZ22 p. 5 | 2005–2022 |
| R6 | Handle degeneracy, infeasibility and ill-posedness by regularization or elastic relaxation that preserves equivalence (T4, P3) | ≥4: GW10/12 p. 5; SSL14; GSW15 p. 26; SIGEST05 §1.1 | 2005–2015 |
| R7 | Connections and unification between old and new methods (T5, I1) | ≥4: FGW02 pp. 525, 528; GBD08 pp. 154–155; GW10/12 p. 16 | 2002–2012 |
| R8 | Conventional wisdom and community dismissals must be tested (J4) | ≥4: GSW15 p. 3; GR22 p. 37; FGW02 pp. 525, 528, 565; GBD08 p. 155 | 2002–2023 |
| R9 | Derivative cost and availability should shape method choice and test design (P4) | ≥4: SIGEST05 p. 99; SNUG15 p. 1; GSW15 p. 3; NPUG p. 19 | 2001–2015 |

Single-mention items that are **not** yet established beliefs: I2 (transfer from the unconstrained case, 2 mentions), O4 ("math it up", Dantzig's words), W4 (literary voice).

---

## Failures, limitations and abandoned directions, as stated

- **SNOPT's own weaknesses, stated by its authors.**
  - Inefficiency as the degrees of freedom grow: "methods that maintain an explicit reduced Hessian … become less efficient as the number of degrees of freedom increases", and "on the 68 problems with ndf > 4000 only 24 problems are solved faster with SNOPT7" (GSW15, p. 13).
  - 25 false-infeasibility terminations (p. 10).
  - 96 total failures out of 1153 (Table 2).
  - [stated + practice], P.
- **Limits of quasi-Newton SQP.** "indefinite QP subproblems raise many practical questions" (SIGEST05, p. 127). The customised linear algebra is hard to "modernize" (GW10/12, p. 2). [stated], P.
- **A negative result on others' methods.** "some newer modifications show little or no improvement" (GR22, p. 37), and one published scaling is "actually harmful" (p. 32). [stated], P.
- **A direction the whole community abandoned, then revived.** Barrier methods were dropped in the 1970s over ill-conditioning worries that later proved largely unfounded (FGW02, pp. 525, 528). This is the group's own cautionary tale about judging methods by feared defects. [stated], P.
- **Wrong prior expectation, admitted.** They were surprised that the barrier method was competitive with simplex (GBD08, p. 155). [stated], P.
- **Announced but unverified.** GSW15 (p. 26) describes "the forthcoming SNOPT9". Whether it was released was **not checked**.
- No rejected papers, retractions or self-declared abandoned projects of Gill's own were found (see Gaps).

## Era and resource context

- **1970s–1988**: NPL (UK), then Stanford SOL from 1979, as the SOL "gang of four" (Gill, Murray, Saunders, M. H. Wright). A small, stable team with a lineage from Wilkinson, Golub and Beale. Fortran codes. Industrial trajectory-optimization users (McDonnell Douglas, later Boeing). Funding was hard to obtain for software (GBD08).
- **2002–2005 SNOPT experiments**: one Linux PC, 2 GB RAM, g77, SNOPT 7.1 (SIGEST05, p. 119).
- **2015 comparisons**: a 12-core Mac Pro with 64 GB RAM, gfortran, CUTEst revision 245, IPOPT 3.11.8 with MA57 (GSW15, p. 6).
- **2022 BFGS study**: MATLAB R2019b on a 2017 MacBook Pro, with Python used for analysis (GR22, pp. 26–27).
- **People**: since about 2005 most statements are co-authored with UCSD PhD students or postdocs (Wong, Robinson, Kungurtsev, Zhang, Runnoe) or ex-students (Brust at ASU). The GR22 and BG23 statements may carry the students' drafting voice.

## Contradictions and tensions (kept, not reconciled)

1. **Customised factorization updating versus black-box linear algebra.**
   - GW10/12 (p. 2) praises SQP's "Sophisticated matrix factorization updating techniques" that "have the benefit of providing a uniform treatment of ill-conditioning and singularity".
   - The same text, one paragraph later, says "Any reliance on customized linear algebra software makes it hard to “modernize” a method…".
   - SNOPT (SIGEST05) is built on customised LU and basis repair.
   - By 2014 (SSL14) and GW15 p. 3 the stated preference is third-party or black-box solvers plus regularization.
   - Both evaluations stand. The direction of travel from 2005 to 2014 is toward black-box solvers.
2. **Are interior methods the right tool for "one-off" problems?**
   - GW10/12 (p. 3, 2010): "although interior methods are very effective for solving “one-off” problems, they are difficult to adapt…"
   - GSW15 (p. 3, 2015): "it is shown that active-set methods can be efficient for the solution of “one-off” problems", and the conventional wisdom is "more nuanced".
   - GZ22 (p. 5, 2022) repeats the 2010 framing almost verbatim, without the 2015 qualification.
3. **Second derivatives.**
   - 2005: "Second derivatives are assumed to be unavailable or too expensive" (SIGEST05, p. 99), yet the same paper says "Future work must take into account the fact that second derivatives are increasingly available" (p. 127).
   - 2015: "If software is intended to be used in an environment in which second derivatives are available, then it is clear that the method that can best exploit these derivatives should be used" (GSW15, p. 3), but also that second-derivative test results "are unlikely to be representative" of problems where derivatives are expensive (p. 3).
4. **Test collections as arbiter versus test collections as unrepresentative.**
   - GR22 treats all of CUTEst as the basis of "complete objectivity" and praises curated collections (p. 4).
   - GSW15 (p. 3) says claims are "difficult to verify … as most test collections include unrelated problems of varying sizes and difficulty". It also says standard test environments favour second-derivative methods.
5. **Disagreement with a fellow team member's textbook.** GR22 (p. 37) counts Nocedal & Wright's *Numerical Optimization* (p. 201) among those who "dismissed factored Hessian methods", and reports that a self-scaled factored-Hessian BFGS gives "significant and consistent improvement". The Nocedal & Wright passage was **not read**. This is a live disagreement for the roundtable.
6. **[inferred] Stated primacy of testing versus a heavily theoretical output.** GR22 says there is "no known analytical means" to rank methods and asks for extensive testing. Yet a large share of Gill's 2013–2020 output consists of convergence-theory papers (stabilized SQP, penalty-barrier). This is a statement-versus-practice question for agent 03, not a contradiction within the statements.

## Gaps (searched, not found or not accessible)

- **No first-person methodology text**: no essay, interview, oral history, award or plenary lecture transcript, blog, or PhD-student advice. Two WebSearch calls turned up only the Simon Stevin lecture abstract and publication pages.
- **No talk video with subtitles found**, so no transcript was saved under `references/sources/talks/`.
- **Book prefaces not read.** The prefaces of *Practical Optimization* (Academic Press 1981; SIAM Classics 2019, doi:10.1137/1.9781611975604) and *Numerical Linear Algebra and Optimization* (1991; SIAM Classics 2021, doi:10.1137/1.9781611976571) could not be reached: SIAM epubs returns 403 to curl and WebFetch, archive.org is blocked by the egress policy, and the Google Books API quota was exhausted. These are the most likely home of the "practical" philosophy. The NPSOL guide points to Chapter 8 of *Practical Optimization* for practical advice (**not read**).
- **Other methodological texts known only by title and metadata, not read:**
  - Gill, Murray, Saunders & Wright, "Model building and practical aspects of nonlinear programming", in *Computational Mathematical Programming* (1985), pp. 209–247, doi:10.1007/978-3-642-82450-0_7. DTIC copy ADA155720 returned 403.
  - "Considerations of numerical analysis in a sequential quadratic programming method", *Lecture Notes in Mathematics* (1986), pp. 46–62, doi:10.1007/BFb0072670.
  - "Some issues in implementing a sequential quadratic programming algorithm", *ACM SIGNUM Newsletter* 20(2):13–19 (1985), doi:10.1145/1057941.1057944. Crossref abstract read; full text returned 403.
  - "Constrained nonlinear programming", *Handbooks in OR & MS* vol. 1 (1989), pp. 171–210, doi:10.1016/S0927-0507(89)01004-2.
- **Course materials behind the UCSD login** ("Protected/ClassNotes") were not accessed, by rule.
- **Nothing found** on how Gill chooses collaborators, allocates time, runs a group, or handles referee rejections. No stated failures of his own beyond solver limitations.
- **Other checks not made:**
  - Whether the SNOPT/NPSOL guide advice originated in the MINOS manuals.
  - Whether SNOPT9 was released.
  - The terms of SNOPT's licence.
  - When he became emeritus.
- **Downloaded but not analysed for methodology**: "Inertia-controlling methods for general quadratic programming" (SIAM Review 1991, `icqp.pdf`) and the NA 10-1 QP report (`genqp.pdf`, an earlier version of GW15).

## Sources

One line each: title; authors; date; identifier or URL; primary (P) or secondary (S).

1. Philip E. Gill homepage (frames: Personal, Interest, Teaching, Students, Postdocs, Papers, Reports); P. E. Gill; undated, current; https://ccom.ucsd.edu/~peg/ ; P
2. UCSD course pages Math 271A (Fall 2021), 271B (Winter 2022), 271C (Spring 2022), 277A (Spring 2021), 171B (Spring 2023); P. E. Gill (171B authorship not checked); 2021–2023; https://ccom.ucsd.edu/~peg/math271a/index.html (and sibling paths) ; P
3. SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization; Gill, Murray, Saunders; SIAM Review 47(1):99–131, 2005; doi:10.1137/S0036144504446096 (read via https://web.stanford.edu/group/SOL/papers/SNOPT-SIGEST.pdf; originally SIAM J. Optim. 12(4):979–1006, 2002, doi:10.1137/S1052623499350013) ; P
4. Sequential Quadratic Programming Methods; Gill, Wong; UCSD report NA 10-03 (Aug 2010), published in *Mixed Integer Nonlinear Programming*, IMA Vol. 154, pp. 147–224 (2012); doi:10.1007/978-1-4614-1927-3_6 ; read https://ccom.ucsd.edu/~peg/papers/sqpReview.pdf ; P
5. On the Performance of SQP Methods for Nonlinear Optimization; Gill, Saunders, Wong; *Modeling and Optimization: Theory and Applications*, Springer Proc. Math. Stat. 147, pp. 95–123 (2015); doi:10.1007/978-3-319-23699-5_5 ; read preprint https://ccom.ucsd.edu/~peg/papers/mopta.pdf ; P
6. On Recent Developments in BFGS Methods for Unconstrained Optimization; Gill, Runnoe; UCSD CCoM report 22-04, July 2022, revised Oct 2023; https://ccom.ucsd.edu/~peg/papers/bfgsdev.pdf ; P
7. George B. Dantzig and systems optimization; Gill, Murray, Saunders, Tomlin, M. H. Wright; *Discrete Optimization* 5(2):151–158 (2008); doi:10.1016/j.disopt.2007.01.002 ; read https://ccom.ucsd.edu/~peg/papers/gbd.pdf ; P
8. Interior Methods for Nonlinear Optimization; Forsgren, Gill, M. H. Wright; SIAM Review 44(4):525–597 (2002); doi:10.1137/S0036144502414942 ; read https://ccom.ucsd.edu/~peg/papers/survey.pdf ; P
9. User's Guide for SNOPT Version 7.5: Software for Large-Scale Nonlinear Programming; Gill, Wong, Murray, Saunders; Dec 2015; https://ccom.ucsd.edu/~peg/papers/sndoc7.pdf ; P
10. User's Guide for NPSOL 5.0: A Fortran Package for Nonlinear Programming; Gill, Murray, Saunders, M. H. Wright; Report SOL 86-6 / NA 98-2, revised June 2001; https://ccom.ucsd.edu/~peg/papers/npdoc.pdf ; P
11. Methods for convex and general quadratic programming; Gill, Wong; *Math. Program. Comput.* 7(1):71–112 (2015); doi:10.1007/s12532-014-0075-x ; read preprint https://ccom.ucsd.edu/~peg/papers/gqp.pdf ; P
12. An LDLᵀ Trust-Region Quasi-Newton Method; Brust, Gill; SIAM J. Sci. Comput. 46:A3330–A3351 (2024); doi:10.1137/23M1623380 ; read report CCoM 23-01 (Nov 2023) https://ccom.ucsd.edu/~peg/papers/trustRegionQN.pdf ; P
13. A projected-search interior-point method for nonlinearly constrained optimization; Gill, Zhang; *Comput. Optim. Appl.* 88:37–70 (2024); doi:10.1007/s10589-023-00549-1 ; read report CCoM 22-01 (June 2022) https://ccom.ucsd.edu/~peg/papers/pdprojReport.pdf ; P
14. A class of projected-search methods for bound-constrained optimization; Ferry, Gill, Wong, Zhang; *Optim. Methods Softw.* 39:459–488 (2023/2024); doi:10.1080/10556788.2023.2241769 ; read https://ccom.ucsd.edu/~peg/papers/quasiwolfe.pdf ; P
15. A Shifted Primal-Dual Penalty-Barrier Method for Nonlinear Optimization; Gill, Kungurtsev, Robinson; SIAM J. Optim. 30(2):1067–1093 (2020); doi:10.1137/19M1247425 ; read https://ccom.ucsd.edu/~peg/papers/pdb.pdf ; P
16. Simon Stevin Lecture "Numerical Linear Algebra and Optimization" (abstract; bio written by host); P. E. Gill; 18 Feb 2014; https://set.kuleuven.be/optec/event-repository/simon-stevin-lecture-philip-e.-gill ; P (abstract) / S (bio)
17. On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method; Gill, Murray, Saunders, Tomlin, M. H. Wright; *Math. Programming* 36(2):183–209 (1986); doi:10.1007/BF02592025 (metadata checked via Crossref; full text not read) ; P (metadata only)
18. UCSD Mathematics faculty profile, Philip Gill; UCSD; undated; https://www.math.ucsd.edu/people/profiles/philip-gill ; S
19. UCSD Profiles, Philip Gill (title "Emeritus Professor, Mathematics"); UCSD; undated; https://profiles.ucsd.edu/philip.gill ; S
20. Some issues in implementing a sequential quadratic programming algorithm; Gill, Murray, Saunders, M. H. Wright; *ACM SIGNUM Newsletter* 20(2):13–19 (1985); doi:10.1145/1057941.1057944 (Crossref abstract only) ; S (metadata)
21. Crossref / OpenAlex metadata for the not-read items (doi:10.1007/978-3-642-82450-0_7; doi:10.1007/BFb0072670; doi:10.1016/S0927-0507(89)01004-2; doi:10.1137/1.9781611975604; doi:10.1137/1.9781611976571); retrieved 2026-09-28 ; S
22. Stanford SOL website (publications_classics, publications_books pages; checked for Gill essays, none methodological); https://web.stanford.edu/group/SOL/ ; S
