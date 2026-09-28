# 02 · Stated methodology: what Nicholas I. M. Gould SAYS research should be

- **Researcher:** Nicholas Ian Mark Gould (STFC Rutherford Appleton Laboratory; visiting professor, Oxford and Edinburgh). Living.
- **Dimension:** stated methodology (research agent 02 of 06, nuwa research-craft Phase 1).
- **Research date:** 2026-09-28.
- **Sources consulted:** 31. Items 28, 29 and 31 in Sources are book descriptions or metadata only; all others were read in full or in substantial part. 28 are primary, meaning written or co-written by Gould, and 3 are secondary. WebSearch calls used: 2.
- **How the evidence was obtained.** Almost every text below is an author-posted PDF from Gould's public RAL page (https://www.numerical.rl.ac.uk/people/nick-gould). The text was extracted locally with pypdf. Identifiers were checked against the Crossref API, the ORCID public API (0000-0002-1031-1588) and his 2023 CV. No user-supplied material existed: `references/sources/papers|talks|essays|software` held only `.gitkeep`. `private/` was not opened.
- **How quotes were checked.** Quotes are verbatim, except that PDF-extraction kerning spaces and line-break hyphens were removed. Typos in the originals are kept and marked [sic]. Page numbers are journal pages when the author-posted PDF is the published version. They are "preprint p." when it is not.

## Read this first: whose voice?

Gould almost never writes alone. Most of the "stated" material below is co-authored:

| Period | Co-authors |
|---|---|
| 1990s | Conn and Toint |
| 2000s | Toint and Orban; Leyffer |
| 2010s | Cartis and Toint |
| 2004–2017 benchmarking papers | J. A. Scott |

Every item is labelled **(sole)** or **(co-authored)**. The texts in his own first-person voice are:

- the 2003 SIAG/OPT *Views-and-News* essay;
- the 2008 and 2012 "How good are projection methods…" papers;
- the preface of his course booklet, which says "I";
- his RAL homepage and CV.

A claim is treated as Gould's belief only when it recurs across co-author groups or appears in the sole-authored texts. The repetition table below does this bookkeeping.

## Era and resource context

These numbers matter when transferring his stated habits to a modern solver team.

| Date | Context | Source (tag) |
|---|---|---|
| 1990s | LANCELOT era. Three-person trans-Atlantic team (IBM Yorktown, RAL, Namur) funded by a NATO travel grant. The LANCELOT A study took "8 months of nearly uninterrupted computation" on a workstation network. One structural-optimization run took "117 hours on an IBM RISC/6000 320". | CGT 1996, p.106; CGT 1994 survey, preprint p.15 [stated, primary] |
| 2003 | GALAHAD 1.0 was built in Fortran 90 on top of the group's own HSL sparse linear algebra. | GOT 2003, p.354 [stated, primary] |
| 2016–17 | Benchmarking on a single 8-core i7-4790 desktop with gfortran 4.7. | Gould & Scott 2017, 36:3 [stated, primary] |
| Career | Lab-based rather than university-based. D.Phil. Oxford 1982; Waterloo 1982–85; Harwell/RAL from 1985; Oxford professor 2006–08. Editor-in-Chief of SIAM J. Optim. 2004/5–2010. | RAL homepage; CV 2023 [stated, primary] |
| Since 2017 | Half time. | RAL homepage [stated, primary] |
| Talks | "My conference talks have been somewhat limited over the past 15 years for health reasons. I have unfortunately turned down many invitations on these grounds." | CV 2023, p.21 [stated, primary, sole] |

The last row explains why no plenary transcripts or interviews exist (see Gaps).

---

## Layer 1: Taste (what is worth doing, what is a good result, what is junk)

**T1. Theory is necessary but not sufficient, and it must be theory of algorithms that are actually implemented.** [stated, primary, co-authored]
- "We continue today to hold the view that such a theory is a *necessary*, while by no means sufficient, condition for a successful algorithm."
- Footnote: "Honesty forces us to acknowledge a few remarkable exceptions to this rule, like the BFGS variable-metric algorithm for nonconvex unconstrained minimization […] or the MINOS algorithm (Murtagh and Saunders, 1978)."
- Source: Gould & Toint, "How mature is nonlinear optimization?", ICIAM 2003 invited talks, SIAM 2004, preprint p.3.

**T2. Negative taste: convergence proofs for algorithms nobody implements.** [stated, primary, co-authored]
- "There are, in our view, too many papers presenting convergence proofs for algorithms that have never been and will probably never be properly implemented, or even tried on simple examples..."
- Source: Gould & Toint 2004, preprint p.11, footnote (2).
- The same attitude reappears ironically, in Gould's own booklet voice, 2021 version: results are stated "under assumptions that are stronger than absolutely necessary—well-motivated students might if they wish, try to weaken them; we can assure readers that academic journals are full of just such noble endevours [sic]." Source: *An introduction to algorithms for continuous optimization*, booklet © 2000, 2021, p.vi [stated, primary, sole].
- See also the fuller booklet quote under W1.

**T3. Theory and algorithms belong together.** [stated, primary]
- "We make no apologies for mixing theory in with algorithms, since (most) good algorithms have good theoretical underpinnings."
- Source: Gould & Leyffer 2003, p.110 (co-authored). The same sentence is repeated verbatim in the 2021 booklet, p.vi (sole).

**T4. Generic software needs guarantees across whole problem classes and parameter ranges.** [stated, primary, co-authored]
- "Due to this wide range of applicability of generic software, it is essential to provide rigorous guarantees of convergence of the implemented algorithms for large classes of problems under a wide variety of possible algorithm parameters."
- Source: Cartis, Gould & Toint, Optima 88 (2012), p.2.

**T5. The size of solvable problems measures progress; large scale is the arena.** [stated, primary, co-authored]
- "the increasing size of the problems that can realistically be solved is, in our view, indicative of the field's evolution." Gould & Toint 2004, preprint p.3.
- 1997 plea, repeated in P2: a method not applicable to large problems may not be worth investigating.

**T6. Nonlinear models are worth the trouble.** [stated, primary, co-authored]
- "At the risk of stating the obvious, the world is not linear […] In our opinion, the frequent use of linear models is not an indication that nonlinear problems do not abound. Rather, it is a statement of the desire to use an algorithm (the simplex method) that is readily understood and is well-known to be suitable for large problems."
- Source: Conn, Gould & Toint, "Large-scale nonlinear constrained optimization: a current survey" (1994), author retypeset, preprint p.2.

**T7. Wariness of fashions, including ones he helped create.** [stated, primary, sole voice]
- The 2021 booklet deliberately excludes "the current obsession with stochastic gradient methods". Of the ideas it covers it says: "Many of the methods we mention will work for such problems, but they are unlikely to be anything close to competitive with the best for these classes." (p.v)
- In its annotated bibliography: "The current obsession with cubic-regularization methods goes back to Yu. Nesterov and B. Polyak […] (2006)." (p.128)
- This is striking, because adaptive cubic regularization (ARC) and its complexity theory are among his own main 2009–2022 topics. See Contradiction C6.

**T8. Praise goes to practical texts and to ideas that survived testing.** [stated, primary]
- Recommended books are "Those we find most useful and which emphasize practical methods": Dennis–Schnabel, Fletcher's *Practical Methods*, Gill–Murray–Wright's *Practical Optimization*, and Nocedal–Wright. Gould & Leyffer 2003, p.167–168 (co-authored); repeated in the booklet, p.125 (sole).
- "The aptly-named BFGS method has stood the test of time well". Gould & Leyffer 2003, p.169.
- "Almost all you need to know about solving small-scale trust-region subproblems is contained in the paper J. Moré and D. Sorensen". Booklet, p.127.
- On his own work: "I would hate to claim “seminal” status for one of my own papers!" Booklet, p.127, footnote (sole). Leyffer's 2003 version says "our own papers".

**T9. The filter is the kind of simple, powerful idea he values.** [stated, primary, co-authored]
- "This simple yet powerful idea may be, in our view, the most significant progress in the past five years". Gould & Toint 2004, preprint p.13.
- The stated reason, in Gould & Leyffer 2003, p.165: "The main objection to merit functions is that they depend, to a large degree, on arbitrary or a priori unknown parameters. A secondary objection is that they tend to be overly conservative in accepting promising potential iterates."

**T10. Worst-case complexity is valued as reassurance, not as a predictor of practice.** [stated, primary, co-authored]
- "Despite its pessimistic outlook, the worst-case perspective is nonetheless reassuring as it allows us to know what to expect in the worst-case from methods we might use. Clearly, the view of the optimization world we most commonly encounter involves the typical-case performance of methods, which is usually far better than the bounds and behaviour discussed here."
- "No significant conclusions can be drawn on the shape of the typical-case landscape beforehand."
- Source: Cartis, Gould & Toint, Optima 88 (2012), p.9.
- The 2022 book's publisher blurb frames evaluation counting the same way: "In many cases, this is often the dominating computational cost." Google Books description of Cartis, Gould & Toint 2022 [stated via publisher text, secondary].

## Layer 2: Problem choice (where problems come from, why now, when to quit)

**P1. Users' needs are the compass.** [stated, primary, co-authored]
- "In our experience a considerable number of users want to solve large problems, while perfectly adequate methods are now available for small problems so long as derivatives are available." CGT, "Methods for nonlinear constraints in optimization calculations" (OUP 1997), preprint p.20.
- The same text hopes for "a narrowing of the gap between the needs of the user community and the provisions of researchers". Preprint p.20.
- Benchmark papers are also framed for users. Gould & Scott 2004, p.301: "Since a potential user may be bewildered by such choice, our intention in this article is to compare the alternatives […] and, as far as is possible, to make recommendations".
- Gould & Scott 2016, 15:3: "a user may not have access to the best solver and so may want to know which is second (or perhaps third) best".

**P2. Screen problems by scalability.** [stated, primary, co-authored]
- "So we end with a plea to the optimization research community: if the “new” method you are considering is not applicable to large problems, consider seriously whether it really is worth investigating." CGT 1997, preprint p.20.

**P3. Agendas come from understudied gaps named explicitly.** [stated, primary, co-authored]
- CGT 1997, preprint p.20, names them:
  - "The global effect of strong nonlinearity on algorithms has not been considered in any depth".
  - "Little is really known about how modern algorithms compare, especially on large or highly nonlinear problems."
  - "Another area which deserves more attention is the effects of noise on minimization algorithms, particularly as so many industrial problems involve noisy functions."
  - "we tend to rely heavily on matrix factorization as a tool, but there are many classes of large problems for which this impossible [sic]."
- The 2003 SIAG essay (sole, p.5) lists "outstanding issues": constraint scaling, preconditioning the conjugate-gradient solve for the barrier Newton system, and extrapolation along the central path.

**P4. Diagnose the bottleneck that explains a historical anomaly, then attack it.** [stated, primary, co-authored]
- "In our opinion, this curious divergence between what logically should have happened in the 1980s, and what actually came to pass may be attributed almost entirely to a single factor: quadratic programming (QP) methods (and their underlying sparse matrix technology) were not then capable of solving large problems."
- Source: Gould & Toint, "SQP methods for large-scale nonlinear programming" (2000), p.150.
- The stated consequence, GOT 2003, p.354: "we decided that our next goal should be to produce high-quality QP codes for eventual incorporation in our own SQP algorithm(s)."

**P5. A problem hierarchy, where solving one level supplies the subproblem solver for the next.** [stated, primary, co-authored]
- "There is also a natural hierarchy of problems, and the ability to solve one is useful if it occurs as a subproblem in a harder one—solving linear systems (sometimes approximately) is vital in linear or quadratic programming, quadratic programs are used within nonlinear programming methods, and local optimization is often a vital component of global optimization."
- Source: Fowkes & Gould, GALAHAD 4.0, JOSS 2023, p.1.

**P6. Real applications motivate teaching and research.** [stated, primary, sole]
- His course opens with the British Gas (Transco) national transmission network: about 58,000 variables for a 24-hour, 10-minute discretization, with the "Challenge: Solve this in real time".
- The slide "TYPICAL PROBLEM" lists: simple bounds, linear and nonlinear constraints, structure, "global solution “required”", integer variables, discretization.
- Source: course slides "Part 0: A gentle introduction", RAL course page.

**P7. When to quit: stop when competitors' evidence says the approach has peaked.** [stated, primary, co-authored]
- This is best documented as his own record of abandonments; see F1–F3 below.
- On augmented Lagrangian methods, GOT 2003, p.354: "the limit of what might be achieved by augmented Lagrangian methods such as LANCELOT A had probably been reached."

## Layer 3: Idea generation

**I1. Borrow from numerical linear algebra and read methods through a linear-algebra lens.** [stated, primary]
- Research interests are stated as "the theory and practice of optimization methods, on numerical linear algebra, on large-scale scientific computation, and on the links between these fields." RAL homepage (sole).
- In the 2008 paper (sole, p.10): "since for linear systems Kaczmarz's method is essentially the Gauss-Seidel iteration, while Cimmino's may be viewed as Jacobi's method for the normal equations, it is perhaps not surprising that these simple projection methods do not perform particularly well".
- On slack variables: "From a linear-algebraic perspective there is little difference". SIAG 2003, p.5 (sole).
- CGT 1997 (preprint p.18) notes "the increasing cross-fertilization between nonlinear optimization and other branches of numerical analysis and applied mathematics" (co-authored).

**I2. Transfer lessons from the unconstrained case, especially inexactness.** [stated, primary, sole]
- "if there is one lesson we should have learned from large-scale unconstrained minimization, it is to aim to solve the subproblem as inaccurately as possible consistent with overall convergence—the truncated Newton approach […] is one of the key ideas to have evolved in the unconstrained case during the 20th century."
- Source: SIAG 2003, p.4.
- Earlier (CGT 1997, preprint p.20): "We must concern ourselves more in the future on methods for which approximate solutions to model problems are sought."

**I3. Revisit "discarded" ideas.** [stated, primary]
- On barrier methods: "We were warned as children that barrier-function methods are beastly because of the effects the barrier has close to the boundary. It later turned out that these fears were almost groundless". SIAG 2003, p.4 (sole).
- Gould & Leyffer 2003, p.173: Karmarkar's "radical “new” approach was actually something that nonlinear programmers had tried (but, most unfortunately, discarded) in the past".
- The same text says the ill-conditioning "defect" of barrier Hessians "is far from fatal" (p.172).

**I4. Use simple, concrete counter-examples to generate insight.** [stated, primary]
- The barrier boundary example: minimize −x on [0,1] from x0 ≈ 10⁻¹². Gould's conclusion: "The lesson here is, I believe, to stay away from the boundary unless there are good reasons to get close […] I strongly believe that it pays to stay close to “the” central path". SIAG 2003, p.4–5 (sole).
- Worst-case constructions by Hermite interpolation show that Newton's method can be as slow as steepest descent. Optima 2012, p.2–4 (co-authored) [stated, primary; the construction itself is practice].

**I5. Exploit structure.** [stated, primary, co-authored]
- "Many large-scale nonlinear problems arise from the modeling of very complicated systems that may be subdivided into loosely connected subsystems. This structure […] exploiting it is often crucial". CGT 1994, preprint p.2.
- "we are now capable of solving far larger problems than before, primarily because of our better exploitation of problem structure." CGT 1997, preprint p.20.
- "For large problems, it is vital to be able to exploit commonly occurring sub-structure". GOT 2005, Acta Numerica, p.324.

**I6. Use second derivatives when they are available.** [stated, primary, co-authored and sole]
- "We strongly recommend the use of exact second derivatives whenever they are available." CGT 1996, p.85.
- "the wider availability of second (and higher order) derivatives must result in a reappraisal of our current “favourite” approaches." CGT 1997, preprint p.20.
- "to obtain fast ultimate convergence, it is usually vitally important to use some 2nd derivative information/approximation". SIAG 2003, p.3 (sole).

## Layer 4: Experiments and execution

**E1. Test on many problems.** [stated, primary, co-authored]
- "Our first decision was to test and report on a large number of test cases. In our experience, this is essential for a true assessment of reliability and performance, as smaller test sets are more likely to introduce unwanted bias." CGT 1996, p.86.

**E2. Compare against the best competitors on the same non-trivial problems.** [stated, primary, co-authored]
- "Unfortunately one soon discovers that one should do a great deal of testing, including experience with the best competitive algorithms on the same non-trivial problems." CGT 1994, preprint p.15.
- A fair cross-package comparison is itself research: "a fair and informative comparison is, in itself, a major research effort." CGT 1996, p.74.

**E3. Test data must be public and large enough to matter.** [stated, primary, co-authored]
- Gould & Scott 2004, p.307, imposed two conditions on the test set: "The matrix must be of order greater than 10,000. — The data must be available to other users." The second was "to ensure that our tests could be repeated by other users and, furthermore, it enables other software developers to test their codes on the same set of examples".
- Gould & Scott 2017 (36:2) criticize studies "limited to a small set of problems, generally arising from a specific application. Moreover, they may use prototype codes that are not available for others to test and they may only be run using MATLAB."
- They also leave out methods for which "implementations that allow timings that are suitable for making fair comparisons with our software are not currently available". Gould & Scott 2017, 36:25.

**E4. Use defaults and do not tune per problem.** [stated, primary, co-authored]
- "Unless otherwise stated, we use these defaults in each case, even if different codes sometimes choose a different value for essentially the same parameter." Gould & Scott 2004, p.309.
- "we normally use the default or otherwise recommended settings; no attempt is made to tune the parameters for a particular problem (this would not be realistic given the size of the test set and number of solvers)." Gould & Scott 2017, 36:5–6.

**E5. Parameters matter enormously, so measure their effect systematically.** [stated, primary, co-authored]
- "relatively innocuous seeming changes, like changing the initial trust region size from one to two, may change the solution time by several orders of magnitude." CGT 1994, preprint p.15.
- The 4OR 2005 study ran "nearly 4000 values of the trust-region parameters" (p.239).
- Its abstract: "the numerical efficiency of these algorithms can easily be improved by choosing appropriate parameters".

**E6. Treat software testing as research, not chores.** [stated, primary, co-authored]
- "At first sight, software testing and comparision [sic] may seem a rather mundane and unchallenging part of the algorithmic development process, but fortunately this view has now been widely replaced with the realization of its crucial nature." Gould & Toint 2004, preprint p.4.
- CUTE's origin (GOT 2003, CUTEr paper, p.374): "originated from the need to perform extensive and documented testing on the LANCELOT package".

**E7. Report timing noise and repeatability limits.** [stated, primary, co-authored]
- "timings can vary if the experiments are repeated. In our experience, this variation is small (typically less than 5%), although for large problems for which memory becomes an issue, the variation can be more significant." Gould & Scott 2017, 36:3.

**E8. Engineering discipline in software.** [stated, primary, co-authored]
- Every GALAHAD package ships with documentation and a test program that "attempts to execute as much of the package as realistically possible". Some code handles "pathological behaviour that cannot be ruled out in theory but nevertheless seems never to occur in practice". GOT 2003, GALAHAD, p.355.
- Robustness habit: "we believe that, at the very least, residuals should always be computed. If large residuals cannot be cured simply through refinement, remedial action should be taken". Gould & Scott 2004, p.322.
- Anti-degeneracy: "by far the easiest in our experience is to randomly perturb the right-hand-sides of the constraints, and only restore (and refine) the solution when optimal for the perturbed version". Gould & Toint 2002, p.156.

## Layer 5: Judging results

**J1. Folklore should not be trusted; test it.** [stated, primary, co-authored]
- "We have many preconceptions but, as the resurrection of barrier methods shows, folklore should not necessarily be trusted." CGT 1997, preprint p.20.
- On parameter conventions: "The commonly used “standard” values for these parameters appear not to be the best choice". 4OR 2005, p.239.

**J2. Random or small-scale evidence is not real-life evidence.** [stated, primary, sole]
- "When we started this study, we were under the impression that projection methods would be generally applicable techniques for solving real-life problems. […] This is contrary to our numerical experience, and simply suggests to us that there is a significant difference between random and real-life problems". Gould 2008, p.9–10.
- "random examples may not reflect practical experience in many cases." Gould 2012, p.1094.
- On SQP with inequality-constrained QP subproblems (SIQP), the popularity rests partly on "favourable empirical evidence accumulated on small-scale problems (Hock and Schittkowski 1981)". GOT 2005, p.334 (co-authored).

**J3. A large theoretical literature is not evidence of practical value.** [stated, primary, sole]
- "despite the large number of theoretical papers devoted to generalizations and convergence issues, there appears to have been little effort to investigate how they really perform in practice." Gould 2008, p.2.
- "they should not be considered as the method of choice for a given application without further strong empirical evidence to support such a claim." Gould 2008, p.10.
- Abstract: "Unfortunately, particularly given the large literature which might make one think otherwise, numerical tests indicate that in general none of the variants considered are especially effective or competitive with more sophisticated alternatives." Gould 2008, p.1.

**J4. Test in the setting most favourable to the method you doubt.** [stated, primary, sole]
- "we attempt to do so in perhaps the most favourable circumstances". Gould 2008, p.2.
- "this is the setting which we had anticipated would put the methods in the best light". Gould 2008, p.10.

**J5. Under challenge, rerun the critics' recommended variants, concede what they show, and keep the conclusion if it survives.** [stated, primary, sole]
- "Recently Censor et al. [2] have challenged these conclusions. […] While these new experiments support the view in [2] that the recommended methods are generally better than those reported on in [7], we do not find that the experiments substantively alter our overall conclusions with respect to the test-set considered." Gould 2012, p.1090.
- He also reproduced their random experiments "as best we could—we didn't have their pseudo-random number generator, but used that from GALAHAD instead". Gould 2012, p.1093.
- He closes constructively: "We would welcome the development of generally applicable software to implement such ideas." Gould 2012, p.1094.

**J6. Read performance profiles carefully.** [stated, primary, co-authored]
- 2004 view: "We believe that such profiles provide a very effective means of comparing the relative merits of different algorithms." Gould & Toint 2004, preprint p.5.
- 2016 view: "caution should be exercised when trying to interpret performance profiles to assess the relative performance of the solvers" (15:1). With more than two solvers "we cannot necessarily assess the performance of one solver relative to another that is not the best" (15:3).
- The proposed remedy: "produce a series of performance profiles, excluding the best solver over the range from successive profiles until only two remain." Gould & Scott 2016, 15:4.
- 1996 predecessor: averages plus five-class rankings, with the caveat that "there is little agreement within the optimization community on alternative aggregate measures." CGT 1996, p.87.
- See Contradiction C4.

**J7. Conclusions stay tentative and test-set dependent.** [stated, primary, co-authored]
- "While the conclusions drawn here therefore remain tentative and dependent on a particular set of test problems, the authors believe that they may be of interest for algorithm developers." 4OR 2005, p.239.
- "direct experience remains of course the best source of inspiration". 4OR 2005, p.239.
- "Of course, only continued experience with LANCELOT will really show its strengths and weaknesses." CGT 1996, p.106.

**J8. Where difficulty comes from.** [stated, primary, co-authored]
- "The difficulty of solving a problem is more often linked to its degree of nonlinearity than to its size." CGT 1996, p.105.

**J9. Admit when no one yet knows.** [stated, primary, sole and co-authored]
- On treating equality constraints: "At this stage I do not think we know which of this [sic] approaches is best, but it is likely that actually there is very little difference." SIAG 2003, p.5 (sole).
- On slacks: "there seem to be ardent devotees of both schools of thought […], so I do not really believe we have exhausted or settled this question." SIAG 2003, p.5 (sole).
- On bound-constrained solvers: "we feel that none of these makes a compelling case as to the best approach(es) for the large-scale case." GOT 2005, p.316 (co-authored).

**J10. Search direction and merit function must cohere.** [stated, primary, sole]
- "it is vital that there is some coherence between the search direction employed and the merit function used to ensure their ultimate satisfaction. Several cautionary examples […] attest to the pitfalls that may befall the unwary." SIAG 2003, p.5.
- GOT 2005, p.333, same idea: "it is vital that all constraints are represented in whatever merit function or filter is used." (co-authored)

## Layer 6: Writing and talks

**W1. Short entry texts for newcomers.** [stated, primary, sole]
- "Another book on optimization? Why? […] Where was the succinct one-hundred-or-so-page introduction that might act as my base camp before I embarked on my assault towards the summit of Mount Optimization? […] I needed the broad picture then, and I still feel that it is necessary now, particularly for non-experts or visitors from other fields who wish to pick up the rudiments."
- Source: booklet preface, p.v.

**W2. Teach the simplest setting first, one constraint type at a time.** [stated, primary]
- Unconstrained problems are taught first because "the underlying linesearch and trust-region ideas are so important that it is best to understand them first in their simplest setting".
- "We purposely consider inequality constraints (alone) in one and equality constraints (alone) in the other, since then the key ideas may be developed without the complication of treating both kinds of constraints at once."
- Source: Gould & Leyffer 2003, p.110 (co-authored); repeated in the booklet, p.v (sole).

**W3. Annotated, opinionated bibliographies.** [stated, primary]
- References are kept out of the main text and moved to "an annotated bibliography of what we consider to be essential references […] which should be read by any student interested in pursuing a career in optimization." Gould & Leyffer 2003, p.110.
- Appendix A is "a personal view of the most significant papers in the area" (p.167).
- *Trust-Region Methods* (2000) is described as featuring "an extensive commented bibliography, which contains 972 references by 745 authors" and "an entire chapter devoted to software and implementation issues". University of Namur research portal abstract [stated via book description, secondary; the book itself not read].
- A running "Quadratic Programming Bibliography" (with Toint, RAL internal report 2000-1, version 28 March 2012) says: "We would be delighted to receive any corrections or updates to this list."

**W4. Frank, self-critical reporting in print.** [stated, primary]
- This is a writing habit visible across co-author groups. The instances are listed in F1–F6 below.
- Characteristic phrases:
  - "frankly rather depressing reading for us" (GOT 2003, p.354);
  - "it hurts us to say, LANCELOT" (Gould & Toint 2000, p.172);
  - "not particularly encouraging!" (CGT 1994, preprint p.15);
  - "we are certainly disappointed" (Gould & Toint 2002, p.169);
  - SIF was "ambitiously (and, with hindsight, perhaps rather arogantly [sic]) called the Standard Input Format" (Gould & Toint 2004, preprint p.4).

**W5. Declare bias and limits of coverage.** [stated, primary, co-authored]
- "Of course, these arguments are biased by our own experience and work". Gould & Toint 2004, preprint p.14.
- "We are aware that, despite our best efforts, the picture remains incomplete and biased by our experience." GOT 2005, p.347.
- "The authors of course realize that this scheme is not the only one that can be defended." CGT 1996, p.87.

**W6. Essays for the community in a conversational, opinionated register.** [stated, primary, sole]
- Opening of the 2003 SIAG essay (p.2): "This is an exciting time to be working in constrained nonlinear optimization. New ideas abound. Collaborations and alliances are forged, rivalry is intense, competition fierce."
- It uses "I believe" and "I strongly believe" repeatedly (p.3–5).
- The 2012 Optima essay opens with an Aesop epigraph about the tortoise and the hare (p.1).
- No talk slides or transcripts were found; see Gaps.

## Layer 7: Research organisation

**O1. Long-term small-team collaboration.** [stated, primary, sole]
- The booklet thanks "Philippe Toint, without whom my journey through optimization would have been much the poorer, and whose words and deeds have truly been an inspiration". It also thanks "Ken McKinnon, Jorge Nocedal, Jennifer Scott and Nick Trefethen who believed in me when it mattered." Booklet, p.vi.
- The collaborations visible in the texts read here are Conn and Toint (LANCELOT, CUTE, *Trust-Region Methods*), Orban (GALAHAD, CUTEr/CUTEst), Cartis (complexity), Scott (benchmarks) and Robinson (SQP). [practice, primary; inferred as a pattern from co-authorship]

**O2. Build reusable infrastructure: a library of independent but interrelated packages.** [stated, primary, co-authored]
- "since we realized that far from producing a single package, we are now in effect building a library of independent but interrelated packages, we have chosen to release an (evolving) large-scale nonlinear optimization library, GALAHAD." GOT 2003, p.354.
- Components are released before the flagship solver is ready: "Since we believe that there might be considerable interest from others in such codes, we have decided to release these before we have finalized our SQP solver(s)." GOT 2003, p.354.

**O3. Maintain infrastructure for decades and listen to users' complaints.** [stated, primary, co-authored]
- On CUTEr's static array dimensions: "Many CUTEr users have learned to detest this inflexibility, and it is certainly the main source of complaint we receive." GOT 2015, CUTEst, p.546.
- The rewrite had been deferred because of scale: "CUTEr (and its dependent SifDec) number roughly 50,000 lines of code. Now, we have done so." GOT 2015, p.546.
- "Such widespread use has inevitably led to a clearer awareness of the deficiencies of the original design". GOT 2003, CUTEr, p.374.

**O4. Pragmatic technology choices: stay in the ecosystem, then bridge outward.** [stated, primary, co-authored]
- 2003: "We had chosen to stay with Fortran rather than C […] partially because many of the package's key (external) components, most especially the HSL […] sparse matrix codes produced by our colleagues, are all Fortran based, and also because we believed (and still believe) Fortran 90 capable of providing all of the facilities we needed." GOT 2003, p.354.
- 2023: "the principal motivation for the new release is to raise the profile of the library by increasing its potential userbase. While modern Fortran is an extremely flexible programming language, it is perceived as old fashioned in many circles." The response was C, Python and Julia interfaces. Fowkes & Gould 2023, p.2.
- 2003 honesty about expertise: the restriction to UNIX "merely reflects our current expertise." GOT 2003, CUTEr, p.375.

**O5. Colleagues as internal reviewers.** [stated, primary, co-authored]
- "Many thanks to our colleagues in the Numerical Analysis Group at the Rutherford Appleton Laboratory for discussions on our findings and commenting on a draft of this note." Gould & Scott 2016, 15:5.

**O6. Lab-based teaching philosophy.** [stated, primary, sole]
- "Currently we do not provide exercises. This is partially as we are not based in a university and thus lack the experience and imperative to evaluate all the time". Booklet, p.vi.
- Course materials are shared openly: "the LaTeX is freely available for one and all to modify according to their needs, so long as basic courtesies are observed." Booklet, p.v–vi.

**O7. Supervision.** No stated advice to PhD students was found. The CV lists one D.Phil. advisee (J. Fowkes, Oxford, 2008), several external-advisor and examiner roles, and MSc supervision [stated, primary]. This is agent 04's territory; see Gaps.

---

## Failures, abandoned directions and corrections (all stated by Gould and co-authors)

| # | What | Words and source | Tag |
|---|---|---|---|
| F1 | LANCELOT B release abandoned (late 1990s) after competitors' comparisons | "the results made frankly rather depressing reading for us […], LANCELOT often, but far from always, being significantly outperformed. […] Reluctantly, we abandoned any plans to release LANCELOT B at that time, and turned our attention instead to SQP methods." Also: "we doubt seriously whether LANCELOT B is a state-of-the-art solver for general nonlinear programming problems." GOT 2003, p.354 | [stated, primary, co-authored] |
| F2 | Large-scale SQP for GALAHAD suspended (2003) | "We have currently suspended development of the large-scale SQP method that we had intended including in GALAHAD […] despite having produced both effective active-set and interior-point QP solvers. Our experience has been that without QP truncation, the cost of the QP solution so dominates that other non-SQP approaches (such as IPOPT […], KNITRO […] and LOQO […]), in which truncation is possible, have made significant progress even before our QP code had solved its first subproblem!" SIAG 2003, p.4 | [stated, primary, sole] |
| F3 | Warm-started active-set QP hope disappointed (2002) | "we are certainly disappointed as we had hoped that the active-set method would be the obvious choice for “warm-started” applications like ”asymptotic” iterations in SQP methods." Gould & Toint 2002, p.169 | [stated, primary, co-authored] |
| F4 | A 117-hour LANCELOT run with default parameters (early 1990s) | "The run we made with the LANCELOT default parameters took 117 hours on an IBM RISC/6000 320 — not particularly encouraging! This provided one motivating factor for us to consider handling inequalities directly via barrier functions." CGT 1994, preprint p.15 | [stated, primary, co-authored] |
| F5 | Prior belief in projection methods overturned (2008) | "When we started this study, we were under the impression that projection methods would be generally applicable techniques for solving real-life problems." Gould 2008, p.9 | [stated, primary, sole] |
| F6 | Erratum (2011): trust-funnel convergence proof | "an error was unfortunately discovered during work with D. Robinson. The problem is in the proof of Lemma 3.10 […] Handling the case where this ratio is unbounded above turned out to be surprisingly complex." Gould & Toint, Erratum, Math. Program. 131 (2012) 403–404, DOI 10.1007/s10107-011-0491-x | [stated, primary, co-authored] |
| F7 | Corrigendum (2016/17): complexity lemma false | "Unfortunately, the proof of Lemma 3.5 in that paper uses a result from an earlier paper in an incorrect way, and indeed the result of the lemma is false. […] the claimed generalization to inequality constraints […] fails to account for complementary slackness, and is thus incomplete." The bound is restored only "for a different, scaled measure of first-order criticality". Cartis, Gould & Toint, Math. Program. 161 (2017) 611–626, DOI 10.1007/s10107-016-1016-4 | [stated, primary, co-authored] |
| F8 | A QP book announced but, as far as found, never published | The 2000 bibliography (version 2012) refers to "our evolving book on the subject". His 2023 CV lists only three books: LANCELOT 1992, *Trust-Region Methods* 2000, *Evaluation Complexity* 2022. | [stated + inferred, primary] |

## Claims repeated at least three times (candidate real beliefs)

| Claim | Repetitions (source, year) | Count |
|---|---|---|
| R1. Theory is necessary but not sufficient; it must serve implemented, tested algorithms | Gould & Leyffer 2003; Gould & Toint 2004 (two statements); Gould 2008; Optima 2012; booklet 2021 (two statements) | 7 in 5 texts |
| R2. Test widely on large, diverse, public, application-derived sets against the best competitors, using defaults | CGT 1994; CGT 1996; Gould & Scott 2004; Gould & Toint 2004; Gould 2008; Gould 2012; Gould & Scott 2017 | 7 |
| R3. Small, random or toy evidence misleads | CGT 1996 (small sets bias); Gould & Toint 2000 (small-scale SQP claims); GOT 2005 (SIQP small-scale evidence); Gould 2008; Gould 2012 | 5 |
| R4. Large scale is the arena; a method that does not scale is suspect | CGT 1994; CGT 1997; SIAG 2003; GOT 2005; Gould & Toint 2004; JOSS 2023 | 6 |
| R5. Solve subproblems inexactly and design for truncation; linear-algebra cost dominates | CGT 1997; Gould & Toint 2000; SIAG 2003; GOT 2005; Optima 2012 | 5 |
| R6. Received wisdom and folklore must be re-tested | CGT 1997; SIAG 2003; Gould & Leyffer 2003; 4OR 2005; Gould 2008; Gould & Scott 2016 | 6 |
| R7. Algorithm parameters matter; prefer mechanisms without arbitrary or unknown parameters | CGT 1994; Gould & Leyffer 2003; 4OR 2005; Optima 2012 (adaptive σ "no longer conditioned on […] a (global) Hessian Lipschitz constant", p.4) | 4 |
| R8. Exploit problem structure | CGT 1994; CGT 1996; CGT 1997; GOT 2005 | 4 |
| R9. Second derivatives are worth having | CGT 1996; CGT 1997; SIAG 2003 | 3 |
| R10. User needs are the compass | CGT 1996; CGT 1997; Gould & Scott 2004; Optima 2012 (evaluation count "of most interest to users", p.2); Gould & Scott 2016; JOSS 2023 | 6 |
| R11. Cross-fertilize with numerical linear algebra and analysis | CGT 1997; Gould & Leyffer 2003; SIAG 2003; Gould 2008; RAL homepage | 5 |
| R12. Report negative results and own failures frankly | CGT 1994; Gould & Toint 2000; Gould & Toint 2002; GOT 2003; Gould & Toint 2004; Gould 2008; Erratum 2011; Corrigendum 2017 | 8 |

Items that are **stated fewer than three times, so not yet a "real belief"**:
- "stay close to the central path" (SIAG 2003);
- "difficulty tracks nonlinearity rather than size" (CGT 1996);
- noise as an understudied topic (CGT 1997);
- scepticism of stochastic-gradient fashion (booklet 2021).

---

## Contradictions (kept, not reconciled)

**C1. SQP versus interior point, dated sequence of stated views.**
- 1997, CGT preprint p.1–2: "While we may be optimistic that SQP methods will still be the future methods of choice, the past decade has been a slightly sobering experience".
- 2000, Gould & Toint, p.150: aim "to suggest why it is now reasonable to accept the widely-held view that SQP methods really are best."
- 2003, GOT GALAHAD, p.354: "To our minds, there had never really been much doubt that SQP methods would be more successful in the long term".
- 2003, SIAG, sole: SQP suspended (F2). The interior-point QPB "is almost always vastly superior for large problems" (p.4). On interior-point complexity: "It remains to be seen that, if in the long term as problem sizes grow, the superior complexity bounds for interior-point methods proves decisive, but I believe this will be the case." (p.3)
- 2005, GOT Acta, p.334: "We now believe that this is not a coincidence and most likely an indication of the unsuitability of the SIQP paradigm for large-scale optimization."
- Later practice pulls the other way (not read here, titles only; agent 03 should check): N. I. M. Gould and D. P. Robinson, "A second derivative SQP method: global convergence", SIAM J. Optim. 20(4) (2010) 2023–2048; and Gould, Loh & Robinson filter SQP papers, SIAM J. Optim. 2014 and 2015. Titles verified on the RAL publication list.
- The two 2003 texts appeared in the same year and point in opposite directions.

**C2. Augmented Lagrangian methods.**
- 2003: "the limit of what might be achieved by augmented Lagrangian methods such as LANCELOT A had probably been reached" (GOT 2003, p.354).
- Later practice: Curtis, Gould, Jiang & Robinson, "Adaptive augmented Lagrangian methods: algorithms and practical numerical experience", Optim. Methods Softw. 31(1) (2016) 157–186, DOI 10.1080/10556788.2015.1071813. Not read; title and DOI verified via Crossref.

**C3. Warm-starting.**
- 2000: "our answer is both! […] when the active set is essentially known, a few active-set iterations are often cheaper than applying an interior-point method". "Thus we contend that any new SQP method for large-scale nonlinear programming should have access to both interior-point and active-set non-convex QP algorithms." Gould & Toint 2000, p.171.
- 2002: the cold-started interior-point approach "is preferable" for degenerate or nonconvex problems (F3).
- 2003 SIAG, the same essay, p.4: warm-starting is "one area in which active-set methods have a clear edge", followed a few lines later by "it is still sometimes faster (especially in the degenerate case) to “cold-start” an interior-point QP than “warm start” active set QP code".

**C4. Performance profiles.**
- 2004: "a very effective means of comparing the relative merits of different algorithms" (Gould & Toint, preprint p.5).
- 2016: "caution should be exercised" when more than two solvers are compared (Gould & Scott, 15:1–15:3).
- In 1996 averages plus rankings were used instead (CGT 1996, p.87).

**C5. Theory as a "necessary condition" versus honest exceptions and complexity-versus-practice.**
- 2004: theory is "necessary", yet the same footnote grants BFGS and MINOS as successful algorithms that lacked it.
- 2012: the complexity-optimal treatment of constraints is "at variance with practical methods" (Optima, p.9). Subproblem cost can be overlooked "for the purposes of the evaluation complexity analysis; but clearly, not for practical purposes" (Optima, p.9).
- The complexity programme (2010–2022 book) measures what the practice-first stance says is not the whole story.

**C6. Cubic regularization.**
- Co-developer of ARC and co-author of a 2022 complexity monograph built around regularization, yet the 2021 booklet calls it "The current obsession with cubic-regularization methods" (p.128).
- This may be self-irony rather than rejection. Recorded as stated.

**C7. Default parameters.**
- CGT 1996: "The default algorithmic choice in the package appears to be both reliable and acceptably efficient" (p.105).
- 4OR 2005: "The commonly used “standard” values for these parameters appear not to be the best choice" (p.239).
- Different code and decade; tension kept.

**C8. Filter versus neither-filter-nor-penalty.**
- 2004: filter "may be, in our view, the most significant progress in the past five years".
- Later practice: Gould & Toint, "Nonlinear programming without a penalty function or a filter", Math. Program. 122 (2010) 155–196, DOI 10.1007/s10107-008-0244-7 (title and DOI checked; content not read). This moves beyond the filter.
- Not a flat contradiction, but a change of stated favourite.

## Gaps (what could not be found or read)

- **No interview, oral history, podcast, video talk or transcript** was found. The CV explains that talks have been limited for about 15 years for health reasons. Plenary or invited titles are listed in the CV (for example ICCOPT 4 Lisbon 2013, ISMP Berlin 2012, SIAM OP 2011, U. Bath "Landscape lecture" 2013), but no slides were located. The old RAL talks page (numerical.rl.ac.uk/talks/talks.shtml) returns 404. Nothing was saved under `sources/talks/`.
- **Prefaces not read:** *LANCELOT* (Springer 1992, DOI 10.1007/978-3-662-12211-2), *Trust-Region Methods* (SIAM 2000, DOI 10.1137/1.9780898719857) and *Evaluation Complexity of Algorithms for Nonconvex Optimization* (SIAM 2022, DOI 10.1137/1.9781611976991). SIAM returned 403 (Cloudflare) to both curl and WebFetch. Only the Namur portal abstract (TRM) and the Google Books blurb (EC book) were read.
- **Not read (behind login):** Bienstock, Gill & Gould, "A note on 'On fast trust region methods for quadratic models with linear constraints', by Michael J.D. Powell", Math. Program. Comput. 7 (2015) 235, DOI 10.1007/s12532-015-0085-3. It may state editorial values.
- **Not readable:** the LANCELOT-versus-MINOS comparison report (Bongartz, Conn, Gould, Saunders & Toint, RAL report on the RAL list, file bcgstRAL97054.pdf) could not be decoded by pypdf because of its font encoding.
- **Delivery unknown:** the ICIAM 2003 talk behind "How mature is nonlinear optimization?" may have been given by Toint. Its acknowledgements say "The second author is indebted to a number of colleagues who have helped supplying some of the material in this talk". Attribution of the spoken talk is unclear, so the text is treated as a co-authored statement.
- **Not located:** the "UK Landscape document on Numerical Analysis" (with N. Higham and E. Süli, 2003; CV).
- **No PhD-supervision advice** in Gould's own words was found (agent 04).
- **No statement of what he considers "bad research"** beyond T2 and J3 (convergence proofs without implementation; theory-heavy literatures without practical evaluation).
- A Google Scholar profile exists (user id 1M6GG2kAAAAJ, from a search result; not opened). team.json has `scholar: ""`. Flagged for the harvest stage; not edited here.

## Sources

One line each. P = primary, S = secondary. All were fetched in this run except where marked.

1. N. I. M. Gould, "Some Reflections on the Current State of Active-Set and Interior-Point Methods for Constrained Optimization", SIAG/Optimization Views-and-News 14(1) (April 2003) 2–7 — https://www.numerical.rl.ac.uk/media/people/nick-gould/Goul03_siagopt.pdf — P (sole; read in full)
2. N. I. M. Gould & Ph. L. Toint, "How mature is nonlinear optimization?", in *Applied Mathematics Entering the 21st Century: Invited Talks from the ICIAM 2003 Congress* (Hill & Moore, eds.), SIAM (2004) 141–161; preprint dated 28 April 2003 — https://www.numerical.rl.ac.uk/media/people/nick-gould/GoulToin04.pdf — P (no DOI; venue from author CV and homepage)
3. C. Cartis, N. I. M. Gould & Ph. L. Toint, "How Much Patience Do You Have? A Worst-Case Perspective on Smooth Nonconvex Optimization", Optima 88 (May 2012) 1–10 — https://www.numerical.rl.ac.uk/media/people/nick-gould/CartGoulToin12_optima.pdf — P
4. N. Gould & J. Scott, "A Note on Performance Profiles for Benchmarking Software", ACM TOMS 43(2) (2016) Art. 15 — DOI 10.1145/2950048 — P (read in full)
5. N. Gould & J. Scott, "The State-of-the-Art of Preconditioners for Sparse Linear Least-Squares Problems", ACM TOMS 43(4) (2017) Art. 36 — DOI 10.1145/3014057 — P
6. N. I. M. Gould & J. A. Scott, "A numerical evaluation of HSL packages for the direct solution of large sparse, symmetric linear systems of equations", ACM TOMS 30(3) (2004) 300–325 — DOI 10.1145/1024074.1024077 — P
7. N. I. M. Gould, D. Orban, A. Sartenaer & Ph. L. Toint, "Sensitivity of trust-region algorithms to their parameters", 4OR 3 (2005) 227–241 — DOI 10.1007/s10288-005-0065-y — P
8. N. I. M. Gould, "How good are projection methods for convex feasibility problems?", Comput. Optim. Appl. 40 (2008) 1–12 — DOI 10.1007/s10589-007-9073-5 — P (sole)
9. N. I. M. Gould, "How good are extrapolated bi-projection methods for linear feasibility problems?", Comput. Optim. Appl. 51(3) (2012) 1089–1095 — DOI 10.1007/s10589-011-9414-2 — P (sole; read in full)
10. N. I. M. Gould, D. Orban & Ph. L. Toint, "GALAHAD, a library of thread-safe Fortran 90 packages for large-scale nonlinear optimization", ACM TOMS 29(4) (2003) 353–372 — DOI 10.1145/962437.962438 — P
11. N. I. M. Gould, D. Orban & Ph. L. Toint, "CUTEr and SifDec: a constrained and unconstrained testing environment, revisited", ACM TOMS 29(4) (2003) 373–394 — DOI 10.1145/962437.962439 — P
12. N. I. M. Gould, D. Orban & Ph. L. Toint, "CUTEst: a Constrained and Unconstrained Testing Environment with safe threads for mathematical optimization", Comput. Optim. Appl. 60(3) (2015) 545–557 — DOI 10.1007/s10589-014-9687-3 — P
13. N. Gould, D. Orban & Ph. Toint, "Numerical methods for large-scale nonlinear optimization", Acta Numerica 14 (2005) 299–361 — DOI 10.1017/S0962492904000248 — P
14. N. I. M. Gould & S. Leyffer, "An Introduction to Algorithms for Nonlinear Optimization", in *Frontiers in Numerical Analysis (Durham 2002)*, Springer (2003) 109–197 — DOI 10.1007/978-3-642-55692-0_4 — P
15. A. R. Conn, N. I. M. Gould & Ph. L. Toint, "Large-scale Nonlinear Constrained Optimization: a Current Survey", in *Algorithms for Continuous Optimization* (Spedicato, ed.), Kluwer (1994) 287–332 — DOI 10.1007/978-94-009-0369-2_10 — P (author retypeset PDF read)
16. A. R. Conn, N. I. M. Gould & Ph. L. Toint, "Methods for nonlinear constraints in optimization calculations", in *The State of the Art in Numerical Analysis* (Duff & Watson, eds.), OUP (1997) 363–390 — https://www.numerical.rl.ac.uk/media/people/nick-gould/ConnGoulToin97_sota.pdf — P (no DOI; venue from homepage; preprint read)
17. A. R. Conn, N. Gould & Ph. L. Toint, "Numerical experiments with the LANCELOT package (Release A) for large-scale nonlinear optimization", Math. Program. 73 (1996) 73–110 — DOI 10.1007/BF02592099 — P
18. N. I. M. Gould & Ph. L. Toint, "SQP Methods for Large-Scale Nonlinear Programming", in *System Modelling and Optimization* (Powell & Scholtes, eds.), Kluwer (2000) 149–178 — DOI 10.1007/978-0-387-35514-6_7 — P
19. N. I. M. Gould & Ph. L. Toint, "Numerical Methods for Large-Scale Non-Convex Quadratic Programming", in *Trends in Industrial and Applied Mathematics*, Kluwer (2002) 149–179 — DOI 10.1007/978-1-4613-0263-6_8 — P
20. N. I. M. Gould, *An introduction to algorithms for continuous optimization* (course booklet, © 2000, 2021) — https://www.numerical.rl.ac.uk/media/people/nick-gould/cobook.pdf — P (sole; preface, conclusions and Appendix A read)
21. N. Gould, RAL course page "Continuous Optimization" and slides "Part 0: A gentle introduction" — https://www.numerical.rl.ac.uk/courses/continuous-optimization/ — P
22. N. Gould, RAL staff page (biography, research interests, publication list) — https://www.numerical.rl.ac.uk/people/nick-gould — P
23. N. I. M. Gould, Curriculum Vitae (2023) — https://www.numerical.rl.ac.uk/media/nick-gould/nimg.cv.pdf — P
24. J. M. Fowkes & N. I. M. Gould, "GALAHAD 4.0: an open source library of Fortran packages with C and Matlab interfaces for continuous optimization", JOSS 8(87) (2023) 4882 — DOI 10.21105/joss.04882 — P (read in full)
25. C. Cartis, N. I. M. Gould & Ph. L. Toint, "Corrigendum: On the complexity of finding first-order critical points in constrained nonlinear optimization", Math. Program. 161 (2017) 611–626 — DOI 10.1007/s10107-016-1016-4 — P (abstract and introduction)
26. N. I. M. Gould & Ph. L. Toint, "Erratum to: Nonlinear programming without a penalty function or a filter", Math. Program. 131 (2012) 403–404 — DOI 10.1007/s10107-011-0491-x — P (read in full)
27. N. I. M. Gould & Ph. L. Toint, "A Quadratic Programming Bibliography", RAL Numerical Analysis Group Internal Report 2000-1 (version 28 March 2012) — https://www.numerical.rl.ac.uk/media/people/nick-gould/gtNAGIR001.pdf — P (front page only)
28. University of Namur research portal, abstract of Conn, Gould & Toint, *Trust-Region Methods* (SIAM 2000; DOI 10.1137/1.9780898719857) — https://researchportal.unamur.be/en/publications/trust-region-methods/ — S (book description)
29. Google Books description of Cartis, Gould & Toint, *Evaluation Complexity of Algorithms for Nonconvex Optimization* (SIAM 2022; DOI 10.1137/1.9781611976991) — https://books.google.com/books/about/Evaluation_Complexity_of_Algorithms_for.html?id=wR56EAAAQBAJ — S (publisher blurb)
30. C. Cartis, N. I. M. Gould & Ph. L. Toint, "Worst-case evaluation complexity and optimality of second-order methods for nonconvex smooth optimization", Proc. ICM 2018, Vol. 3 (2019) 3697–3737 — https://www.numerical.rl.ac.uk/media/people/nick-gould/CartGoulToint18_icm.pdf — P (abstract and introduction; no methodology statements found)
31. Y. Censor, W. Chen, P. L. Combettes, R. Davidi & G. T. Herman, "On the effectiveness of projection methods for convex feasibility problems with linear inequality constraints", Comput. Optim. Appl. 51 (2012) 1065–1088 — DOI 10.1007/s10589-011-9401-7 — S (the critique Gould answered in source 9; metadata only, not read)

Other material checked but not cited as evidence:
- ORCID public works list (0000-0002-1031-1588) and the Crossref API, used for identifier checks.
- The Oxford CS legacy page http://www.cs.ox.ac.uk/nick.gould/home.html. It lists the course booklet as "by Nicholas I. M. Gould and friends, 2006", which helps date it.
