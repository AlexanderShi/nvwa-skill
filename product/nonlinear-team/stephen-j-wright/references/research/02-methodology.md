# Stephen J. Wright: stated research methodology (Phase 1, research agent 02)

- **Researcher**: Stephen J. Wright (University of Wisconsin-Madison, Computer Sciences; Argonne National Laboratory 1990-2001; living)
- **Dimension**: stated methodology, meaning what Wright *says* research, algorithm design, judging results, writing and teaching should be. Whether he practises it is left to agent 03 (`03-process-evidence.md`).
- **Research date**: 2026-09-28
- **Sources consulted**: 26 (21 primary, 5 secondary), listed under "Sources". Another 8 were identified but could not be read (see "Gaps").
- **WebSearch calls used**: 2 of 2. Everything else was fetched with curl or WebFetch from known URLs (homepage, arXiv, Optimization Online, MINDS@UW, Crossref and OpenAlex for identifier checks).
- **Local corpus**: `references/sources/{papers,talks,essays,software}` held only `.gitkeep` files at the start of this run, so there was no user-supplied material. `private/` was not opened.
- **Saved by this run**: `references/sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt`, a plain-text copy of the public UW-Madison oral-history transcript (the archive's own transcript, not checked against the audio).

**Tags**: [stated] = Wright's own words · [practice] = what his papers or code do (noted only where a stated claim needs its context; agent 03 owns this) · [observed] = what others say about him · [inferred] = my reading, not his words. **P** = primary, **S** = secondary.
Quotes are verbatim. In quotes from PDFs I removed only line-break hyphenation and footer text. Oral-history quotes keep the transcript's spoken disfluencies, and the timestamps are the transcript's own. A paraphrase is marked "(paraphrase)" and never appears inside quotation marks.

---

## 0. The core beliefs: claims repeated at least 3 times

| # | Belief (short form) | Count | Dated occurrences (source keys, see §Sources) | Status |
|---|---|---|---|---|
| B1 | **Theory and computational practice must drive each other.** Neither is sufficient alone, and gaps between them are themselves research problems. | 8 | OPT02 (2002), SIAM04 (2004), SQP02 abstract (2002), CD15 (2015), OH22 (2022), OTP25 (2025), UWCS26 (2026), CS730-26 (2026) | real belief, stable for 24 years |
| B2 | **Match the algorithm to the application's structure.** Build methods from a "toolkit" of components (general-purpose software stays important, NIPS10 slide 2). | 6 | FoCM02 (2002), OPT02 (2002), NIPS08 (2008), NIPS10 (2010), CD15 (2015), OTP25 (2025) | real belief |
| B3 | **Applications create the new problem classes and revitalise the field**, and the traffic runs both ways (ML to optimization, optimization to ML). | 7 | SIAM04, NIPS08, NIPS10, KDD13, PCMI16/18, OH22, UMN25 | real belief |
| B4 | **Old or "unsophisticated" methods deserve re-examination.** Optimizers have dismissed useful methods too quickly. | 5 | OPT02, SIAM04, CD15, OH22, OTP25 | real belief |
| B5 | **Formulation is a skill.** The same problem can be written in many ways, and choosing well matters. | 4 | NIPS08, PCMI16/18, OH22, OTP25 | real belief |
| B6 | **Present fundamentals in their simplest form, with complete elementary proofs.** | 4 | NIPS10, CD15, PCMI16/18, OH22 (on books) | real belief (writing) |
| B7 | **Analyse under weaker, realistic assumptions.** Standard assumptions (LICQ, strict complementarity, Lipschitz constants) often fail or are too conservative. | 4 | CI00 (2000), FP01 (2001), SQP02 (2002), OTP25 (2025) | real belief (taste) |
| B8 | **Worst-case complexity bounds are not a guide for choosing an algorithm.** They are a tool for understanding. | 2 (+1 title only) | CRRW21 abstract (co-authored, 2021), OTP25 (2025); talk title "The role of complexity bounds in optimization" (Math4DS, transcript not read) | below threshold. Treat as a strong recent statement, not yet a confirmed repeated belief |

---

## 1. Research taste (what is worth doing, what counts as a good result)

**1.1 Theory and practice as two engines (B1).** [stated] P
- 2025: "There are often gaps between the practical performance of an algorithm and what can be proved about it. These two facets of the field — the theoretical and the practical — interact in fascinating ways, each driving innovation in the other." (*Optimization in Theory and Practice*, arXiv:2510.15734v2, abstract, p. 1)
- 2025, adopting Knuth's dictum: "It contains many enlightening observations about the relationship between theory and practice in that field, summarizing them in the quote “The best theory is inspired by practice and the best practice is inspired by theory.” Optimization has adhered to this dictum throughout its history as both a mathematical and highly practical discipline." (arXiv:2510.15734, p. 2. The Knuth paper is D. E. Knuth, "Theory and practice", *Theoretical Computer Science* 90 (1991) 1-15, doi:10.1016/0304-3975(91)90295-D. I verified the identifier and did not read the paper.)
- 2026: "In my talk, I plan to discuss the complementary roles of mathematical theory and computational practice in optimization, showing how each of these two aspects of the field has driven developments in the other." (Wright quoted in UW-Madison CS news, 2026-05-26, about his ICM 2026 plenary. The quote is P and the article is S.)
- 2004 (slides): "However, the theory isn't the whole story! Explicit manipulation of dual variables λ is key to making these algorithms effective in practice." (SIAM Annual Meeting talk "Continuous Optimization: Recent Developments and Applications", July 2004, slide 21, on interior-point NLP methods.)
- 2002 (slides), research agenda for NLP: "more computation-guided development of algorithms and theory" (SIAM OPT02 talk "The Ongoing Impact of Interior-Point Methods", 20 May 2002, slide 58, "topics for further investigation").
- 2022 (teaching, the same belief transmitted to students): "I'll ask them to go and write a program to implement a particular algorithm computationally and use it to solve problems and to make observations about how it performs in practice. And then I will also ask them to prove things about how that algorithm works, and what kinds of problems it can solve" (UW oral history, 2022-10-04, [40:30]).
- 2026 syllabus: "We will discuss both mathematical properties and practical aspects of these methods." (CS730 Nonlinear Optimization II, Spring 2026 syllabus.)
- Era context: the statement appears in his early-UW talks on interior-point and NLP methods (2002-2004, just after Argonne), the data-science years (2015) and his ICM-level retrospective (2025-26). The framing becomes more explicit and self-conscious over time. The 2025 paper is his most complete statement of it.

**1.2 A good result can be something that has not been done before and takes time to be recognised.** [stated] P
- "I would say that one of the metrics is your impact on other researchers, how your work has influenced other people in your area, and also in applications areas ... And particularly if you, if you do something that someone hasn't really done before, that hasn't really been appreciated before. And people recognize it as being an important direction. And sometimes that happens right away. And sometimes it takes, it takes some time for that to be recognized." (OH22 [21:25])
- In the same answer he lists four channels of impact: influence on researchers, software, books and students (paraphrase). Software: "optimization is a field where you can write software that actually comes up with a computer implementation of these methods that you can use to solve important key problems" (OH22 [21:25]).

**1.3 Optimization is mathematics, and he leans theoretical.** [stated] P
- "There is a lot of sophisticated math that goes on in optimization. And maybe I regret that people in math departments don't maybe recognize that as much as they could. I started out in a math department. So you know, that's kind of my I've always been biased more to the theoretical side, although I really love working on applications and software as well. ... I think there are more areas of math that we could bring in and use to develop optimization." (OH22 [12:59])
- Contrast with how others see him (S, [observed]): "While many researchers in optimization focus on either theory, computational implementation, or practical applications, Wright is active in all three aspects." (UW CS news, 2026-05-26.) The same article says his ICM invitation "stems from his work developing optimization algorithms with mathematically rigorous performance guarantees, not just experimental results."

**1.4 Weaker, realistic assumptions are a mark of a better analysis (B7).** [stated] P
- 2001: "In the interests of generality, we weaken an assumption that is often made in the analysis of algorithms for (1.1), namely, that the gradients of the active constraints are linearly independent at the solution. We replace this linear independence constraint qualification (LICQ) with the weaker Mangasarian-Fromovitz constraint qualification (MFCQ)" (Effects of Finite-Precision Arithmetic on Interior-Point Methods for NLP, arXiv:math/0103102, p. 2; SIAM J. Optim. 12 (2001) 36-78, doi:10.1137/S1052623498347438).
- 2001, criticising related work because its assumption fails in real computation: related work "makes assumptions on the pivot sequence that do not always hold in practice." (same paper, p. 2)
- 2001, arguing that a condition costs nothing in floating-point practice: "The latter condition is hardly restrictive, since the data errors made in storing the problem in a digital computer mean that the solution set is known only to within some multiple of u in any case." (same paper, p. 2)
- 2002: "Most local convergence analyses of the sequential quadratic programming (SQP) algorithm for nonlinear programming make strong assumptions about the solution, namely, that the active constraint gradients are linearly independent and that there are no weakly active constraints. In this paper, we establish a framework for variants of SQP that retain the characteristic superlinear convergence rate even when these assumptions are relaxed" (Modifying SQP for Degenerate Problems, SIAM J. Optim. 13 (2002) 470-497, doi:10.1137/S1052623498333731, abstract via Crossref).
- 2000: "We can drop the assumption of strict complementarity and a “sufficiently interior” starting point made in [18], and we do not need the stronger second-order conditions of [8]." (Constraint Identification and Algorithm Stabilization for Degenerate Nonlinear Programs, arXiv:math/0012209, p. 2; Math. Program. 95 (2003) 137-160, doi:10.1007/s10107-002-0344-8)
- 2025, the same instinct applied to complexity theory: "The algorithm design and analysis is based on assumptions about the problem that are much too conservative for most instances, or are tight on only a small fraction of the search space navigated by the algorithm." (arXiv:2510.15734, p. 5, first of four listed reasons for theory-practice gaps)
- Era context: the 2000-2002 statements come from the Argonne period (DOE-funded, no teaching) and his degenerate-NLP / stabilized-SQP programme.

**1.5 What he calls a poor result.** [stated] P, all from arXiv:2510.15734 (2025)
- A theoretically significant method with no practical effect: of the ellipsoid method, "its impact on practical computations with LP was negligible." (p. 8)
- Analysis on instance distributions unlike real ones: average-case simplex analysis, "while an important contribution, has little relevance to LP instances arising in practice, which are not distributed in the same way as the random instances in these studies." (p. 7)
- Theory that does not reach the code: momentum algorithms "are rarely implemented as written." (p. 21) Multi-step optimal-stepsize theory "does not have immediate practical relevance, though it provides insights" (p. 21).
- His own line of work is judged by the same standard (see §5.2).
- Positive exemplars he names: FISTA works "“out of the box,” matching their solid theoretical design with good practical performance" (p. 21). Restarting is "an area in which theoretical and practical developments appear to have gone hand-in-hand" (p. 21). Cubic regularization is "possibly the first Newton-based method devised specifically to admit nonasymptotic complexity theory, while also having practical relevance" (p. 22).

**1.6 Simplicity is valued.** [stated] P
- 2002, on his feasible trust-region SQP for model predictive control: "simple, yet with good convergence properties" and "particularly well suited to the nonlinear MPC problem" (FoCM '02 talk "Optimization Problems in Model Predictive Control", 6 Aug 2002, slide 3).
- 2015, on coordinate descent: "CD methods are the archetype of an almost universal approach to algorithmic optimization: solving an optimization problem by solving a sequence of simpler optimization problems." (Coordinate Descent Algorithms, arXiv:1502.04759, p. 2; Math. Program. 151 (2015) 3-34, doi:10.1007/s10107-015-0892-3)

---

## 2. Problem choice (where problems come from, why now, when to stop)

**2.1 Applications generate the problem classes (B3).** [stated] P
- 2004: "Applications are becoming more plentiful and diverse, and are driving developments in algorithms and software." Also: "NLP is a broad paradigm encompassing many pathological situations. Difficult to design robust algorithms; Relative performance of algorithms/software varies widely between problems." And: "Continual reevaluation of old ideas." (SIAM04, slide 3, "Nonlinear Programming: Themes")
- 2010: "Optimization is going through a period of growth and revitalization, driven largely by new applications in many areas." (NIPS 2010 tutorial "Optimization Algorithms in Machine Learning", 6 Dec 2010, slide 2)
- 2013: "the rich collection of problems in learning and data analysis is providing fresh perspectives on optimization algorithms and is driving new fundamental research in the area." (KDD 2013 keynote abstract "Optimization in learning and data analysis", doi:10.1145/2487575.2492149. I read the abstract text through OpenAlex's reconstruction of the published abstract.)
- 2025: "In turn, these areas have prompted a ferment of new research activity in optimization by posing challenging new problems and new contexts." (UMN Data Science Initiative seminar abstract "Optimization in Data Science", 21 Oct 2025)
- 2025: "These classes have been refined over the years in response to the demands of application areas. Over the past 15 years, for example, machine learning has been a rich source of optimization problems characterized by many variables, a great deal of data, and certain structures in the objective functions that can be exploited by algorithms." (arXiv:2510.15734, p. 1)
- 2022: "pretty much any optimization researcher, even the very theoretically oriented researchers spend some fraction of their time working with domain scientists in other areas on on interesting applications." (OH22 [18:26]) He names structural biology, process control (since the early 1990s) and data science (his main engagement in the last 10 years).

**2.2 "Why now": a new big thing about once a decade, and you keep your antennae out.** [stated] P
- "about every decade has been a big thing that's happened. In the in the 90s it was interior point methods in the 2000s or late 2000s, it was data science, where suddenly optimization, you know, had a paradigm shift. ... I want to be around when that happens again" (OH22 [57:24])
- "you never know it, they often just come out of left field. And so you just want to kind of have an early warning system, keep your antennae out there and see, if something's interesting, something that tickles your interest happens, it might blow up into a major research topic. You just have to sort of keep your finger on the pulse" (OH22 [58:55])
- How he entered ML (paraphrase of OH22 [24:55]-[30:28]): in 2000-2001 a machine-learning colleague at the University of Chicago came to his office with optimization problems from ML. Compressed-sensing work with Rob Nowak followed around 2006. He treats this as chance plus openness, not a plan.

**2.3 Gaps between theory and practice are a source of problems.** [stated] P (links to B1)
- 2025, a list of research questions to ask when practice beats theory: "Are the loose bounds provided by the theory due to rare worst-case instances? Can we quantify the rarity of these instances? Can we mollify these instances, for example by showing that a nearby instance is usually easy to solve? Gaps may prompt a search for new kinds of algorithms with better theoretical and possibly even better practical properties." (arXiv:2510.15734, p. 2)
- 2025, the three ways to close a gap: "by refining the complexity analysis, refining problem classes to identify subclasses that admit tighter analysis, or discovering algorithmic features or even new algorithms with better theoretical performance" (p. 6)
- 2002, the same move with interior-point geometry: "In theory, superlinear convergence doesn't happen until the final almost-straight leg ... Practical algorithms can step past many corners of C at once, provided they are not too sharp. Can we get “semi-local” convergence results that yield fast convergence beyond the final leg?" (OPT02, slide 40)
- 2004, the same move with MPECs: "Fletcher & Leyffer ('02) showed that ordinary SQP codes performed excellently on MPEC benchmarks (and interior-point codes were also quite good). Why? Can robustness of standard NLP approaches be improved further?" (SIAM04, slide 38)
- 2002: "We discuss the reasons for which implementations of SQP often continue to exhibit good local convergence behavior even when the assumptions commonly made in the analysis are violated." (SQP02 abstract, doi:10.1137/S1052623498333731)

**2.4 Degeneracy is worth studying because of scale and discretization.** [stated] P, 2000
- "We believe that degeneracy is an important issue, given the large size of many modern applications of nonlinear programming and their nature as discretizations of continuous problems. Nevertheless, the practical usefulness of constraint identification and stabilization techniques remains to be investigated." (arXiv:math/0012209, p. 19)

**2.5 When to stop.** No stated criterion was found for abandoning a problem (see Gaps). The nearest statement is about professional service: "I've sort of dialed back a little bit on that now. Because I need to get ... I've got less time to do that stuff. I need to get some work done." (OH22 [52:43])

---

## 3. Idea generation

**3.1 Assemble algorithms from a toolkit of components (B2).** [stated] P
- 2010: "However, there is a growing emphasis on “picking and choosing” algorithmic elements to fit the characteristics of a given application — building up a suitable algorithm from a “toolkit” of components. It's more important than ever to understand the fundamentals of algorithms as well as the demands of the application, so that good choices are made in matching algorithms to applications." (NIPS10, slide 2)
- 2008: "Many interesting adaptations of fundamental algorithms that exploit the structure and fit the requirements of the application." And: "Different applications have very different properties and requirements, that require different algorithmic approaches. Some approaches transfer between applications and can be analyzed at a more abstract level." (NIPS 2008 workshop talk "Optimization in Machine Learning: Recent Developments and Current Challenges", Whistler, 12 Dec 2008, slides 3 and 10)
- 2008, on combining fast-local and cheap-step methods: "Often, there is a choice between (i) methods with fast asymptotic convergence (e.g. interior-point, SQP) with expensive steps and (ii) methods with slow asymptotic convergence and cheap steps, requiring only (approximate) gradient information. The latter are more appealling when we need only an approximate solution. The best algorithms may combine both approaches!" (NIPS08, slide 10; the spelling "appealling" is in the original)
- 2015: "We expect to see further developments and extensions, further customization of the approach to specific problem structures, further adaptation to various computer platforms, and novel combinations with other optimization tools to produce effective “solutions” for key application areas." (CD15, p. 29)
- 2002: "practical algorithms appear to tie together many ideas, new and old (SQP, trust-region, filter, linear algebra of different types,...)" (OPT02, slide 58)
- 2025: "Along with mathematical expertise and imagination, a good deal of intuition and domain knowledge for the key application areas is required for successful algorithm design, adaptation, and application." (arXiv:2510.15734, p. 1)

**3.2 Carry ideas across problem classes.** [stated] P
- 2000: "Motivation for the sSQP approach came from work on primal-dual interior-point algorithms described in [19,12]." (arXiv:math/0012209, p. 2, on the origin of stabilized SQP)
- 2008, analogies between classes: matrix-completion algorithms "can be similar to compressed sensing, but with more complicated linear algebra. (Like the relationship of interior-point SDP solvers to interior-point LP solvers.)" (NIPS08, slide 9)
- 2000: "We believe, however, that ingredients of the approach proposed here can be embedded in practical algorithms, such as SQP algorithms that include modifications (merit functions and filters) to ensure global convergence." (arXiv:math/0012209, pp. 2-3)

**3.3 Revisit old and dismissed methods (B4).** [stated] P
- 2015: "The obviousness of the CD approach and its acceptable performance in many situations probably account for its long-standing appeal among practitioners. Paradoxically, the apparent lack of sophistication may also account for its unpopularity as a subject for investigation by optimization researchers, who have usually been quick to suggest alternative approaches in any given situation." (CD15, p. 2)
- 2022, self-critical about the community on SGD: "this method had been around since the early 1950s. But optimizers knew about it, but didn't pay much attention to it. Because it's very slow, we thought it's very slow. But machine learning people found this was exactly the tool they needed" (OH22 [24:55]). He also names Frank-Wolfe (1950s) and accelerated gradient (early 1980s) as old methods that ML revived.
- 2025, on first-order methods for LP: "Such ideas had been tried in the 1980s without much success on practical problems, but several factors gave rise to renewed interest." (arXiv:2510.15734, p. 11)
- 2004: "Continual reevaluation of old ideas." (SIAM04, slide 3)

**3.4 Observe first, explain second.** [stated] P
- 2025: "In some cases (such as those involving nonconvex formulations of low-rank matrix optimization problems) this phenomenon was observed first in practice: Algorithms that were guaranteed to find only first-order optimal points were consistently finding global solutions. Explanations of why this happens, including rigorous specification of conditions under which it happens, has followed." (arXiv:2510.15734, p. 24)
- 2025: "(Theoreticians strive to justify approaches that have seen practical success; practitioners gain confidence from theoretical underpinnings of innovations that have proved useful in practice.)" (p. 25)

**3.5 Formulation as a design variable (B5).** [stated] P
- 2025: "Any given practical problem can be formulated in many different ways, all “valid” in the sense that their solutions are equivalent and achieve the goals of the application. However, some of these formulations may be much harder to solve than others, due to redundancies or degeneracies (and many other more subtle reasons). Expertise is needed to choose the formulation that can be solved most efficiently with the algorithmic tools at hand. Conversely, designers of algorithms and software try to make their tools as robust as possible to such problematic aspects of formulations." (arXiv:2510.15734, pp. 2-3)
- 2008: "Duality often key to getting a practical formulation." (NIPS08, slide 10)
- 2016/2018: "In many cases, there are a number of different ways to formulate a given application as an optimization problem." (PCMI notes, Optimization Online 2016/12/5748, p. 4)
- 2022: the aim of teaching is that when "someone gives them a problem from an application, hopefully, they'll have the skill to sort of distill it down to an optimization problem that they can solve" (OH22 [35:54])

---

## 4. Experiments and execution

**4.1 Check whether theory's distinctions are visible in computation.** [stated] P, with a [practice] pointer for agent 03
- 2015: "A full computational comparison between variants of CD (and between CD and other methods) is beyond the scope of this paper. Nevertheless it is worth asking whether various aspects of the convergence analysis presented above — in particular, the distinction between CD variants — can be observed in practice." (CD15, pp. 22-23) The experiment used synthetic quadratics with parameters tuned to stress the constants that appear in the theory. It reports: "This linear rate held even for problems in which Q was singular — a significant improvement over the sublinear rates predicted by the theory." (p. 23) [practice: agent 03 should dissect this design]
- 2025: "computational experience on similar problems is a more reliable guide" than complexity bounds when choosing an algorithm (arXiv:2510.15734, p. 6).
- 2008: "Exhaustive tests show that non-intuitive choice of step length works best" (NIPS08, slide 43, on primal-dual image denoising). Empirical tuning is stated openly.
- 2025, on how the LP interior-point field did it: practical methods "were being tested on test problems batteries, which were curated to be representative of real-world problems. (The "netlib" test set (https://www.netlib.org/lp/) was particularly influential.)" (arXiv:2510.15734, p. 9)

**4.2 Software engineering and numerics are part of the job.** [stated] P
- 2025: "Development of software to implement these algorithms requires many other areas of expertise to be brought to bear, involving broader mathematical knowledge and software engineering expertise. The mathematical issues include the vagaries of finite-precision arithmetic, robustness in the face of ill-posed formulations, the interface with numerical linear algebra, and parallel implementation, among many others. Engineering issues (some of which can also be analyzed mathematically) include management of hierarchical memory and data movement." (arXiv:2510.15734, p. 1)
- 2000: "The numerical implications should also be investigated, since implementation of these techniques may require solution of ill-conditioned systems of linear equations" (arXiv:math/0012209, p. 19)
- 2004, on software design trends: object-oriented designs "allow specialization according to problem structure, modular use of linear algebra" (SIAM04, slide 56; he names his own OOQP among the examples).
- 2002 (MPC application): "Our experience shows that there is considerable advantage to retaining feasibility. This leads us to consider a method of the feasible SQP type." (FoCM02, slide 29) This is a design choice he explicitly derives from application experience.

**4.3 Release software freely.** [stated] P
- 2022, on GPSR and SpaRSA (compressed sensing, about 2007-2010): "we just made them freely available, because they were pretty short codes, you know, there's no point in trying to copyright them or anything." (OH22 [9:02])
- On PCx (LP, Argonne, released 1997), paraphrased from OH22 [9:02]: it was free for research, with a licence required for commercial use, and "very few people did that". He says he later learned (in 2016) that the early Google founders had used it: "I wish I'd known about that 20 years earlier." [stated, uncorroborated here; I did not check the Google claim.]
- Era context: PCx and OOQP were built at Argonne with "several postdocs, and students" (OH22 [9:02]), a lab setting with software staff time that a university group usually lacks.

**4.4 Posting preprints openly.** [stated] P
- 2002: "reminder! Send your new tech reports to http://www.optimization-online.org" (FoCM02, slide 2). The current homepage calls Optimization Online "the latest and greatest eprints on optimization (be sure to post your finest work!)" and notes that he maintained "Interior-Point Methods Online ... starting in 1994, in the early days of the Web" (wrightstephen.github.io/sw_proj, read 2026-09-28).

---

## 5. Judging results

**5.1 Four reasons why practice beats worst-case theory: his checklist.** [stated] P, arXiv:2510.15734, pp. 5-6 (verbatim bullet openings)
1. "The algorithm design and analysis is based on assumptions about the problem that are much too conservative for most instances, or are tight on only a small fraction of the search space navigated by the algorithm."
2. "The instances in a problem class that are difficult for an algorithm might be extremely rare."
3. "Algorithms may contain adaptive mechanisms (for example, line searches or trust-region strategies) that allow them to exploit variations in the properties of problems across the parameter space. These gains may be reflected in practice but the variability of properties of the problem may be hard to express in an abstract way that lends itself to theoretical analysis."
4. "The problems of interest in a given class actually belong to a subclass with properties that set them apart from the wider class and make them easier to solve."

Conclusion he draws: "For these and other reasons, practitioners are generally not advised to use complexity bounds as the sole basis for choosing which algorithm to apply to a given problem. Such bounds may be a consideration, but computational experience on similar problems is a more reliable guide. Nevertheless, the process of understanding the gaps and perhaps narrowing or closing them ... deepens our understanding of both the algorithms and problem classes. Sometimes the insights so gained can percolate into wide practical use, as in the interior-point revolution in linear programming." (p. 6)

**5.2 Judging his own complexity-guaranteed methods (self-critique).** [stated] P
- 2025, on the Newton-CG methods of Royer, O'Neill and Wright (Math. Program. 180 (2020) 451-488, doi:10.1007/s10107-019-01362-7; arXiv:1803.02924) and Curtis, Robinson, Royer and Wright (SIAM J. Optim. 31 (2021) 518-544, doi:10.1137/19M130563X; arXiv:1912.04365): "They are based on practical methods, but the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance. This is not surprising since our assumptions on f are so mild, and potentially admit pathological examples." (arXiv:2510.15734, p. 23)
- 2021, the co-authored framing of the same line (stated, but by four authors): "These methods have often been designed primarily with complexity guarantees in mind and, as a result, represent a departure from the algorithms that have proved to be the most effective in practice. ... The resulting trust-region Newton-CG method also retains the attractive practical behavior of classical trust-region Newton-CG, which we demonstrate with numerical comparisons on a standard benchmark test set." (CRRW21 abstract via Crossref) The criterion is that a complexity-motivated method must at least keep the practical behaviour of the method it modifies. See Contradictions C2 for how the 2025 wording differs.

**5.3 Honesty about what has not been shown.** [stated] P
- 2000: "the practical usefulness of constraint identification and stabilization techniques remains to be investigated." (arXiv:math/0012209, p. 19)
- 2002 talk disclaimer: "Disclaimer: Opinions are personal!" (OPT02, slide 2)
- 2004, a hype check against evidence: "The Grid isn't all hype! Optimizers have done serious computations on it." (SIAM04, slide 48). Serious computation is his criterion for whether a trend is real.

**5.4 Skepticism about method labels.** [stated] P
- 2010, on "online BFGS" and diagonal scaling in ML: "Since the gradients are so inexact (based on just one data point), both in update and right-hand side of the step equations, these methods are really stochastic gradient with interesting scaling, rather than quasi-Newton in the conventional sense." (NIPS10, slide 73)

**5.5 Greedy decrease versus longer-horizon steps.** [stated] P
- 2010: "The “greedy” strategy of getting good decrease from the current search direction is appealing, and may lead to better practical results." (NIPS10, slide 6)
- 2025: "Given that even exactly-minimizing choices of α cannot yield better worst-case results than those for the constant 1/L step, we are tempted to conclude that there can be no other schemes using the search direction s_k = −∇f(x_k) that yield better complexities. Remarkably, this is not true!" (arXiv:2510.15734, p. 15) This refers to the nonmonotone "silver stepsize" line, which he says "does not have immediate practical relevance" (p. 21). See C1.

---

## 6. Writing, books and talks

**6.1 Fundamentals, simplest forms, complete elementary proofs (B6).** [stated] P
- 2015: "Our approach throughout is to describe the CD methods in their simplest forms, to illustrate the fundamentals of the applications, implementations, and analysis." (CD15, p. 2)
- 2016/2018: "Our approach throughout is to give a concise description of some of the most important algorithmic tools for smooth nonlinear optimization and regularized optimization, along with the basic convergence theory for each. ... In most cases, the theory is elementary enough to include here in its entirety. In the few remaining cases, we provide citations to works in which complete proofs can be found." (PCMI notes, p. 3; published as "Optimization algorithms for data analysis", IAS/Park City Mathematics Series vol. 25 (2018) 49-97, doi:10.1090/pcms/025/02)
- 2010: "We present a selection of algorithmic fundamentals in this tutorial" (NIPS10, slide 2)
- Publisher description of *Optimization for Data Analysis* (Wright and Recht, CUP 2022, doi:10.1017/9781009004282): "This text covers the fundamentals of optimization algorithms in a compact, self-contained way, focusing on the techniques most relevant to data science." (S: publisher blurb via Crossref; authorship of the blurb unknown. The preface itself was not read.)

**6.2 Books are for distillation and for newcomers and outside users.** [stated] P
- "I really enjoy this process of sort of distilling knowledge in a particular area, and sort of digesting it, and figuring out how to present it to people who are just coming into the area who are keen to learn about the area. ... they can influence people who just take the book, they need to solve a problem in their own domain, and they can take a book and find methods in the book that will help them address their problem." (OH22 [21:25])
- On *Numerical Optimization*: "it's also a reference book. And it's used a lot by people in other areas ... who, as I said, sort of need to use optimization, but they're not quite sure what method to use, or how to go about writing their problem down in the right way." (OH22 [23:47])
- Era and resource context: "I had time because I wasn't teaching I had time to do things like write books, you know, that, that university people have a lot of trouble finding time for." (OH22 [6:36]) This refers to Argonne in the 1990s, where *Primal-Dual Interior-Point Methods* (SIAM 1997, doi:10.1137/1.9781611971453) was written. *Numerical Optimization* (with Nocedal; 1st ed. 1999, 2nd ed. 2006, doi:10.1007/978-0-387-40065-5) spans the Argonne-to-UW move.

**6.3 Talk structure (partly practice).** [practice, from the slide decks; listed here because the slides state it] A "themes" slide comes first and states the thesis (OPT02 slide 2, SIAM04 slide 3, NIPS08 slide 3, FoCM02 slide 3). A closing "topics for further investigation" or "Conclusions" slide lists open questions (OPT02 slide 58, NIPS10 slide 82: "There is much more to be gained from the interaction between the two areas."). Agent 03 should check whether his papers follow the same pattern.

**6.4 Standards imposed on students' written work.** [stated] P (course documents)
- CS524, Fall 2018 page: "Explain your work. This means write in words how you solved the problem, use intuitive variable names, and comment any code you turn in. It is unacceptable to simply turn in undocumented code. Even if your code produces the correct result, undocumented code and ugly code will lose points." (The page lists two TAs. Authorship of this wording is not certain, so it is P for the course and uncertain for Wright personally.)
- CS730, Spring 2026 syllabus: "Written homework must be typeset in LaTex" and "If you use AI in any way to generate a solution, then you must describe fully in your submission how you used it."

---

## 7. Research organisation (colleagues, students, time, community)

**7.1 He learned research style from colleagues.** [stated] P
- "I've been very lucky to learn from them by looking at what sort of things they work on about how they go about research and how, how they go about finding research problems." (OH22 [6:36]) Named influences in the interview are Olvi Mangasarian (his first invited talk as a PhD, Madison 1988), Michael Ferris and Jim Rawlings (joint projects from about 1995). The Argonne and North Carolina State colleagues are not named individually.

**7.2 Students are recruited from graduate courses.** [stated] P
- "the students that I've recruited have typically come from graduate classes, they're not students that are new as undergrads. So they've typically taken the classes and then said, "Well, I'm doing well, in this class, I'm really interested in doing a PhD in this area."" (OH22 [35:54])
- Teaching is about "not just to learn things, but also to learn how to think about things" (OH22 [35:54]). The research questions he teaches students to ask: "How much computer time will it take to find the solution? Is it even possible to find a solution? ... Is it possible to give it a really bad problem that will confuse it and cause it to take a long time? And if that's the case, are these bad problems rare? Or are they common? ... we ask those questions in research. And we also teach students to think about questions like that." (OH22 [40:30]) In 2022 this is the same "rare hard instances" question he writes into the 2025 paper (§2.3).

**7.3 Luck and chance encounters.** [stated] P
- "to be successful, you have to work hard, and you have to be smart, and all that kind of thing. But luck plays such a big role, you know, just being in the right place at the right time, talking to the right people having a chance encounter with someone." (OH22 [1:01:21])

**7.4 The community is collegial, not territorial.** [stated] P
- "it really is a very friendly community. People are supportive of each other. They're not sort of super aggressive about defending their own territory. As I know, other communities are" (OH22 [53:26])

**7.5 Service is institution-building, and was done when time allowed.** [stated] P
- He led the renaming of the Mathematical Programming Society to the Mathematical Optimization Society (2009 vote, "75% to 25%"). He rewrote the constitution and bylaws "to turn them into sort of user guides for how to organize the different meetings of the society" (OH22, service section, around [45:38]-[52:37]).
- "I was lucky that I did a lot of that work during the years I was at Argonne, when I, I had more time to get involved with that." (OH22, same section)
- Roles, from the bios: Editor-in-Chief of SIAM J. Optimization 2014-2019 and of Math. Programming Series B 2003-2007, MOS Chair (2007-2010 per the bios; see C4), SIAM Trustee 2005-2014, NSF IFDS site director. IFDS started up in fall 2020 and, as of the 2022 interview, "engages about 34-35 faculty members", with eight postdocs and "six or seven" research assistants (OH22 [18:26] and [43:05]). He was CS Department Chair 2023-2025 (homepage).

**7.6 Interdisciplinary work is normal.** [stated] P. See §2.1 (OH22 [18:26]). The IFDS framing is "the theoretical fundamental side of data science" (OH22 [57:24]).

---

## 8. Failures, dismissed directions and self-corrections (stated)

- **SGD dismissed as slow.** The optimization community (he says "we") did not take SGD seriously before about 2006-2008 (OH22 [24:55]). By 2025 he writes that SGD "is undoubtedly consuming far more compute cycles than any other optimization algorithm in the world today" (arXiv:2510.15734, p. 25). [stated, a self-inclusive admission]
- **Complexity-first modifications did not pay off in practice** for his own Newton-CG line (§5.2). [stated, 2025]
- **Unverified practical value** of constraint identification and stabilization, flagged by himself in 2000 (§5.3). Whether it was later tested is for agent 03 to check.
- **Lost credit on PCx** ("I wish I'd known about that 20 years earlier", OH22 [9:02]). This is a missed-recognition episode, not a research failure.
- **No rejected papers, retracted claims or abandoned projects** were found in stated material. Two published corrections exist and are listed on his papers page: a "Correction which fixes some typos and completes the proof of Theorem 2" for Wright and Jarre 1998, and a corrections file for P664. Both are [practice], for agent 03, and not read here.

---

## 9. Era and resource context of the stated methods

| Period | Setting (from OH22 and the homepage) | Stated method most tied to it |
|---|---|---|
| 1984-1990 | PhD at Queensland, postdoc, NC State mathematics department (two courses per semester) | "biased ... to the theoretical side" (§1.3) |
| 1990-2001 | Argonne MCS: no teaching, DOE funding, postdocs, a software culture (PCx 1997, OOQP around 2001) | books (§6.2), degenerate NLP and weak assumptions (§1.4), software and numerics (§4.2), service (§7.5) |
| 2001-2015 | UW-Madison CS (computational-science cluster hire); compressed sensing and ML era, multicore | toolkit (§3.1), application-driven (§2.1), free codes (§4.3) |
| 2015-2026 | UW, IFDS (NSF), department chair 2023-2025; ML at scale, LLMs | complexity theory and the theory-practice gap (§5), fundamentals-first teaching (§6.1), AI-use disclosure (§6.4) |

---

## Contradictions (kept, not reconciled)

- **C1. Greedy versus longer-horizon steps (2010 vs 2025).** In 2010 greedy one-step decrease "may lead to better practical results" (NIPS10, slide 6). In 2025 non-greedy stepsize schedules give provably better worst-case complexity ("Remarkably, this is not true!", p. 15), but the theory "does not have immediate practical relevance" (p. 21). This is consistent on practice and changed on theory. The 2010 slide implies that fixed-step analysis is the route to rates, while the 2025 text shows long steps beating it.
- **C2. How to describe complexity-guaranteed Newton-CG (2021 vs 2025).** The 2021 co-authored abstract says the new trust-region Newton-CG "retains the attractive practical behavior of classical trust-region Newton-CG". The 2025 solo text says the modifications "do not improve the practical performance" and that the bounds are "quite pessimistic". These are not logically incompatible (retain ≠ improve), but the emphasis moves from a defence of the method to a self-critique.
- **C3. SGD (before 2008 vs 2022-2025).** In 2022 he recalls that before 2008 optimizers "didn't pay much attention to it. Because ... we thought it's very slow" (OH22 [24:55]). In 2025 it is the single most important optimization algorithm by compute (p. 25), and "It is possibly surprising that an algorithm based on crude (but cheap) approximations to the gradient admits any useful theory at all — but it does." This is an acknowledged change of view.
- **C4. MOS chair dates.** The oral-history transcript reads "In 2006, I became the Chair" and "I stepped down in 2012" (OH22, service section). His homepage and 2025 seminar bios say "Past Chair of the Mathematical Optimization Society, 2007-2010". The transcript may be garbled at this point ("I was elected Chair of the society in 2000, in 2000"). Not resolved.
- **C5. Administrative work.** In 2022: "I haven't done administrative work in the department, except for this institute that I that I head up" (OH22). He was Department Chair 2023-2025 (homepage). This is a later change, recorded because the 2022 statement about how he allocates time no longer holds.
- **C6. Self-description versus others' description.** He says he is "biased more to the theoretical side" (OH22 [12:59]). The UW CS news [observed] says he is "active in all three aspects" (theory, computation, applications). This is a difference of emphasis, not necessarily a conflict.

---

## Gaps (searched for and not found, or not readable)

- **Book prefaces not read.** *Primal-Dual Interior-Point Methods* (1997) front matter: SIAM returned 403 to curl and WebFetch. *Numerical Optimization* prefaces (1999, 2006): Springer front matter returned a JavaScript challenge. *Optimization for Data Analysis* preface (doi:10.1017/9781009004282.001): Cambridge paywall. *Optimization for Machine Learning* (MIT Press 2011) preface and "Introduction: Optimization and Machine Learning" (doi:10.7551/mitpress/8996.003.0002, .0003): MIT Press blocked and the MPG PuRe copy returned 403. Prefaces are the most likely place for further stated method on writing, so this is the largest gap.
- **Video talks not transcribed.** His YouTube playlist (PL5oPwlS-sZr8GGQTiwBjc9crNbRO9hnyy) includes "ICM 2026 Plenary Lecture", "Math4DS Live No. 45: The role of complexity bounds in optimization", "Connections between Optimization, Learning and Control: Past, Present and Future", "Keynote: Optimization in Data Science", MLSS 2013 lectures and an OWOS talk on second-order nonconvex methods. yt-dlp was refused by YouTube's sign-in bot check, and I did not bypass it. arXiv:2510.15734 is very probably the written counterpart of the ICM plenary [inferred from the UW CS news description of the talk. The arXiv record names no venue, and its footer reads "Copyright © 20XX by SIAM"].
- **No essay, blog or advice-to-PhD-students text by Wright** was found. The oral history (OH22) is the only long-form interview found.
- **Proceedings of the IEEE editorial** "Big Data: Theoretical Aspects" (Haykin, Wright, Bengio, 2016, doi:10.1109/JPROC.2015.2507658) was not read (IEEE returned 418).
- Not searched for lack of time and budget: **Optima MOS chair columns** (2007-2010) and **SIAM J. Optimization editorials** (2014-2019).
- **Prize citations** (Dantzig Prize 2024, Khachiyan Prize 2020, NAE 2024) were not read in full. Only the criteria phrases quoted in seminar bios were seen.
- **No stated criterion for abandoning a problem or direction** was found (layer 2 "when to stop" is empty).
- **No stated views on refereeing or rebuttals** were found, despite his five years as SIOPT Editor-in-Chief.
- **Tool limits in this run**: DBLP returned a bot challenge and the arXiv API returned 406. I used the arXiv HTML author search, OpenAlex (ORCID 0000-0001-6815-7379, 341 works) and Crossref for identifier checks instead.

---

## Sources (one line each; P = primary, S = secondary)

1. **OH22**. UW-Madison Oral History Program, "Oral History Interview, Stephen Wright (2179)", interviewer F. Hernandez-Moleres, 2022-10-04. https://minds.wisc.edu/handle/1793/83811. Transcript saved at `../sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt`. P
2. **OTP25**. S. J. Wright, "Optimization in Theory and Practice", arXiv:2510.15734 (v1 2025-10-17, v2 2025-12-02; full text read, 31 pp.). P
3. **CD15**. S. J. Wright, "Coordinate Descent Algorithms", arXiv:1502.04759; Math. Program. 151 (2015) 3-34, doi:10.1007/s10107-015-0892-3 (arXiv v1 full text read). P
4. **PCMI16/18**. S. J. Wright, "Optimization Algorithms for Data Analysis", Optimization Online 2016/12/5748 (https://optimization-online.org/2016/12/5748/, posted 2016-12-01, updated 2019-02-21; PDF read); published in *The Mathematics of Data*, IAS/Park City Math. Series 25 (2018) 49-97, doi:10.1090/pcms/025/02. P
5. **NIPS10**. S. J. Wright, "Optimization Algorithms in Machine Learning", NIPS tutorial slides, 6 Dec 2010, https://pages.cs.wisc.edu/~swright/nips2010/sjw-nips10.pdf (82 slides read). P
6. **NIPS08**. S. J. Wright, "Optimization in Machine Learning: Recent Developments and Current Challenges", NIPS workshop slides, Whistler, 12 Dec 2008, https://pages.cs.wisc.edu/~swright/talks/sjw-nips.pdf. P
7. **OPT02**. S. J. Wright, "The Ongoing Impact of Interior-Point Methods", SIAM Conference on Optimization, Toronto, 20 May 2002 (expanded 27 May 2002), https://pages.cs.wisc.edu/~swright/talks/siopt_talk_may02.pdf. P
8. **SIAM04**. S. J. Wright, "Continuous Optimization: Recent Developments and Applications", SIAM Annual Meeting, Portland, July 2004, https://pages.cs.wisc.edu/~swright/talks/siam-annual-jul04.pdf. P
9. **FoCM02**. S. J. Wright (with Rawlings, Tenny, Pannocchia), "Optimization Problems in Model Predictive Control", FoCM '02, Minneapolis, 6 Aug 2002, https://pages.cs.wisc.edu/~swright/talks/focm-talk.pdf. P
10. **CI00**. S. J. Wright, "Constraint Identification and Algorithm Stabilization for Degenerate Nonlinear Programs", arXiv:math/0012209 (ANL/MCS-P865-1200, Dec 2000); Math. Program. 95 (2003) 137-160, doi:10.1007/s10107-002-0344-8. P
11. **FP01**. S. J. Wright, "Effects of Finite-Precision Arithmetic on Interior-Point Methods for Nonlinear Programming", arXiv:math/0103102; SIAM J. Optim. 12 (2001) 36-78, doi:10.1137/S1052623498347438. P
12. **SQP02**. S. J. Wright, "Modifying SQP for Degenerate Problems", SIAM J. Optim. 13 (2002) 470-497, doi:10.1137/S1052623498333731 (abstract only, via Crossref). P
13. **CRRW21**. F. E. Curtis, D. P. Robinson, C. W. Royer, S. J. Wright, "Trust-Region Newton-CG with Strong Second-Order Complexity Guarantees for Nonconvex Optimization", SIAM J. Optim. 31 (2021) 518-544, doi:10.1137/19M130563X, arXiv:1912.04365 (abstract only). P (co-authored)
14. **KDD13**. S. J. Wright, "Optimization in learning and data analysis", KDD 2013 keynote, doi:10.1145/2487575.2492149 (abstract only, via OpenAlex). P
15. **UMN25**. UMN CSE Data Science Initiative, "Optimization in Data Science" (Wright seminar abstract and bio), 21 Oct 2025, https://cse.umn.edu/dsi/events/optimization-data-science-stephen-wright-cs-uw-madison. P (abstract) / S (bio)
16. **UWCS26**. K. Barrett-Wilt, "CS Professor Steve Wright to be plenary speaker at International Congress of Mathematicians 2026 and named Vilas Research Professor", UW-Madison CS news, 2026-05-26, https://www.cs.wisc.edu/2026/05/26/steve-wright-plenary-speaker-at-icm-2026-and-vilas-research-professor/. S (contains one P quote)
17. **CS730-26**. S. J. Wright, CS/Math 730 Nonlinear Optimization II syllabus, Spring 2026 (public Google Doc linked from the homepage), https://docs.google.com/document/d/1jDKaJTDmco2uQN7zHddhAXqJnvPIThZx4d_PMZgfcwo. P
18. CS524 Introduction to Optimization, Fall 2018 course page, https://pages.cs.wisc.edu/~swright/cs524-f18.html. P (course document; wording possibly shared with TAs)
19. CS726 (Fall 2019) and CS730 (Spring 2020) course pages, https://pages.cs.wisc.edu/~swright/cs726-f19.html and https://pages.cs.wisc.edu/~swright/cs730-s20.html. P (minor)
20. Homepage, https://pages.cs.wisc.edu/~swright/ (read 2026-09-28), and papers and talks list https://pages.cs.wisc.edu/~swright/papers/. P
21. Homepage (new), https://wrightstephen.github.io/sw_proj/ (read 2026-09-28). P
22. C.-P. Lee, S. J. Wright, "First-order algorithms converge faster than O(1/k) on convex problems", arXiv:1812.08485 (ICML 2019) (abstract only). P ([practice] context for §5)
23. Royer, O'Neill, Wright, "A Newton-CG algorithm with complexity guarantees for smooth unconstrained optimization", Math. Program. 180 (2020) 451-488, doi:10.1007/s10107-019-01362-7, arXiv:1803.02924 (identifier checked, not read; cited because OTP25 judges it). P
24. Math department news, "Affiliate Prof. Steve Wright to be plenary speaker at ICM 2026", 2025-04-21, https://www.math.wisc.edu/2025/04/21/affliate-prof-steven-wright-invited-as-speaker-to-2026-icm/. S
25. UMN ISyE Distinguished Seminar page (bio with prize criteria), https://cse.umn.edu/isye/events/isye-distinguished-seminar-stephen-wright. S
26. Publisher description of S. J. Wright and B. Recht, *Optimization for Data Analysis*, Cambridge University Press 2022, doi:10.1017/9781009004282 (Crossref abstract field). S

Identified but **not read**: *Primal-Dual Interior-Point Methods* front matter (doi:10.1137/1.9781611971453); *Numerical Optimization* 2nd ed. front matter (doi:10.1007/978-0-387-40065-5); *Optimization for Data Analysis* preface (doi:10.1017/9781009004282.001); *Optimization for Machine Learning* preface and introduction (doi:10.7551/mitpress/8996.003.0002, doi:10.7551/mitpress/8996.003.0003); Haykin, Wright, Bengio, Proc. IEEE 104 (2016) 8-10 (doi:10.1109/JPROC.2015.2507658); D. E. Knuth, "Theory and practice", TCS 90 (1991) 1-15 (doi:10.1016/0304-3975(91)90295-D); YouTube talks (playlist PL5oPwlS-sZr8GGQTiwBjc9crNbRO9hnyy).
Identifiers of other works named in passing (checked via Crossref or OpenAlex): GPSR, IEEE J. Sel. Top. Signal Process. 1 (2007), doi:10.1109/JSTSP.2007.910281; SpaRSA, IEEE Trans. Signal Process. 57 (2009) 2479-2493, doi:10.1109/TSP.2009.2016892; OOQP, ACM TOMS 29 (2003) 58-81, doi:10.1145/641876.641880; stabilized SQP, Comput. Optim. Appl. 11 (1998) 253-275, doi:10.1023/A:1018665102534; Lee and Wright, IMA J. Numer. Anal. 39 (2019) 1246-1275, doi:10.1093/imanum/dry040.
