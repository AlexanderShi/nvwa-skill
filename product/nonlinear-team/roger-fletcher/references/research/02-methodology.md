# Roger Fletcher: stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Roger Fletcher (1939-2016). BA Cambridge 1960 (Natural Sciences, theoretical physics); PhD Leeds 1963 under Colin Reeves; AERE Harwell 1969-73; University of Dundee from 1973 (professor of optimization, later Baxter Professor). Deceased, so this is a historical lens |
| Dimension | 02: stated methodology (what he said research, algorithm design and numerical work should be) |
| Research date | 2026-09-28 |
| Sources consulted | 12 read, fully or in part: 7 primary (1 interview, 3 single-author or co-authored technical reports and preprints, 1 co-authored journal paper, the filterSD software documentation and source headers, 1 co-authored memoir abstract), 5 secondary (Royal Society fellow page, abstract of the Gould and Hall memoir, 2 of Nick Higham's blog posts, Wikipedia). 8 more were identified and checked with Crossref or Semantic Scholar but **not read** (see Gaps) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software,publications}` held only `.gitkeep`; `private/` was not opened |
| Language | English (per team.json) |

**What was read and how.** Fletcher never wrote a "how to do research" essay or blog post that I could find. No recorded talk turned up in a YouTube search (yt-dlp), and the prefaces of *Practical Methods of Optimization* could not be reached (Wiley 403; the Internet Archive copy is access-restricted). The richest stated source is **an interview by Yu-Hong Dai**, hosted on the Kyoto University optimization lab website (`www-optima.amp.i.kyoto-u.ac.jp/ORB/issue22/flectcher_interview.html`). The page is undated; internal evidence places it around 2005-06, since Dai says Fletcher "very recently" proposed his 2005 BFGS/SR1 hybrid. I cite it by question number (Q1-Q21). The rest of his stated method comes from (a) the motivation, discussion and conclusion sections of his late technical reports, where he writes in the first person ("I feel", "My impression is"); (b) *A Brief History of Filter Methods*, a co-authored review in which he, Leyffer and Toint explain why filters were invented and what went wrong; (c) the user documentation of his last code, filterSD, which contains his advice to users. PDFs were extracted with pypdf. Page numbers are the printed page numbers of the preprint or report I read. Quotes are verbatim, with ligatures normalised and extraction spacing tidied; "[sic]" marks original typos.

**Tags.** [stated] = he said or wrote it. [stated, co-authored] = in a jointly written text, so the view may belong as much to his co-authors. [practice] = what he did, recorded only where it anchors a stated claim (checking practice is agent 03's job). [observed] = what others wrote about him. [inferred] = my inference, never to be quoted as his view. Each item is also marked primary or secondary.

---

## 0. Beliefs he repeats (3 or more independent occasions)

| # | Belief (short form) | Occasions (date: source) | Count |
|---|---|---|---|
| R1 | **Safeguard principle.** Add globalization (line search, filter, monotonicity) only in a way that does not spoil the fast, unmodified method. Global convergence is necessary, but it is not allowed to cost the performance that made the method attractive | 2005: Dai and Fletcher, *Numer. Math.* 100 (abstract, p. 33) (co-authored); 2006: *Brief History of Filter Methods*, p. 2 (co-authored); 2009: LMSD report ERGO 09-014, p. 17 (single author) | 3 (2 co-authored) |
| R2 | **The numbers are the arbiter, and claims must be sized to the evidence.** "watch for what the numbers are telling you"; hedge conclusions ("reasonably encouraging", "cannot yet be taken as definitive", "no conclusive outcome either way") | c.2005-06: interview Q7, Q21; 2005: NA/223 abstract, p. 15, p. 17; 2009: ERGO 09-014, p. 16, p. 17 | 3 sources, 7+ statements |
| R3 | **Accuracy is limited by conditioning and round-off, so do not demand too much of it, and read convergence behaviour as evidence of accuracy** | c.2005-06: interview Q13; 2009: ERGO 09-014, p. 15 (tolerance relaxed); 2010-13: glcpd documentation §9 and the rgtol parameter note (repeated in the qlcpd.f source header) | 3 |
| R4 | **Research is for users. Find "what works best", make it available, and value mathematics for its usefulness** | c.2005-06: interview Q2, Q5, Q16; 2005: NA/223, p. 2 (an application user's problem motivates the work); 2011: filterSD user documentation (advice written for users) | 3 sources, 5 statements |
| R5 | **Research problems come out of building his own solvers.** The needs of a code under construction set the research question | 2005: NA/223, p. 1 ("part of a project to provide effective codes"); 2006: *Brief History*, p. 2 (co-authored); 2009: ERGO 09-014, p. 1 (the null-space solver needed inside an SLP code) | 3 |
| R6 | **Derivatives must be exact and checked. Do not use finite differences, scale the problem, give realistic bounds** | 2010-13: filterSD.pdf §5 and the parameter list; glcpd.pdf §2 and §9; checkd.f and checkg.f headers | 3+ statements, but all in **one** software package from one period, so it is weaker evidence than R1-R5 |

Beliefs below this threshold are recorded once in the layers and marked as single statements (1x) or twice-stated (2x).

---

## 1. Research taste: what is worth doing, what a good result is

**1.1 Usefulness is the test of mathematics** [stated, primary] (R4)
- On his physics degree: "I find this background helps a lot when talking to users of optimization, and has influenced my opinions on what aspects of mathematics are `useful' and what are less so." (interview Q2, c.2005-06)
- Asked about Powell and Davidon, he said what he admires: "I like very much that he is firmly concentrated on the ultimate aim of finding what works best and on making it available to users." (Q5, about Powell)
- [stated, co-authored, primary] The Powell memoir he co-wrote (Buhmann, Fletcher, Iserles, Toint, 2018) opens with a statement of values: "In a subject that roughly divides into practical designers of algorithms and theoreticians who seek to underpin algorithms with solid mathematical foundations, Mike Powell refused to follow this dichotomy. His achievements span the entire range from difficult and intricate convergence proofs to the design of algorithms and production of software." (abstract, DOI 10.1098/rsbm.2017.0023; I read only the abstract, via Crossref). It is praise of Powell written by four authors, so I read it as [inferred] evidence of the taste Fletcher shared. It is not his own statement.

**1.2 Simplicity and low overhead count as merit** [stated, primary] (2x: LMSD and PBB; not yet at the 3x threshold)
- He presents LMSD as "a competitive and more simple alternative to the state of the art l-BFGS limited memory method" (ERGO 09-014 abstract, 2009). The benefit "is achieved with less extra storage and housekeeping cost" (p. 17).
- [co-authored] "Consequently, the new gradient projection methods are easy to code and work well in practice." (Dai and Fletcher 2005, *Numer. Math.* 100, p. 45)

**1.3 Scepticism about fashion and about what one reads** [stated, primary] (single interview, 2 answers)
- "Most of them seemed interesting at the time. Fashions change, and what seems important today may not be so in ten years time." (Q14, when asked to list his most important papers)
- "treat everything you read about with some scepticism, and be prepared to follow your own intuition. But be willing to change your mind when it becomes clear that other ideas have been demonstrated to be superior." (Q21, asked about "the most important spirits for doing scientific researches"; his first answer was the joke "Famous Grouse?!")

**1.4 Judgements on which methods have run their course** [stated, primary] (single statements, c.2005-06)
- On quasi-Newton and CG: "However, I find it very hard to envisage significant new ideas in nonlinear CG and quasi-Newton methods." (Q15)
- On CG for large problems: "I can only envisage using (preconditioned) CG when nothing else is practicable." (Q13) He also said: "Many large problems are solved more effectively using sparse matrix factors. Also CG doesn't fit comfortably with inequality constrained problems." (Q13)
- On FR against quasi-Newton: "It was clear early on that DFP and BFGS were superior to FR on small and medium sized problems." (Q12)
- See Contradictions C1 and C2: his 2009-2011 work partly cuts against these judgements.

**1.5 A good theory result is honest about its assumptions** [stated, co-authored, primary] (2006)
- On filter convergence theory: "These results are as strong as can be expected for general NLPs." Straight after: "One undesirable assumption in [10] is the need for global solution to the QP subproblem (2.1)." (*Brief History*, p. 6)

---

## 2. Problem choice: where problems come from, why now, when to stop

**2.1 His own solver pipeline generates the problems** [stated, primary] (R5)
- "This work arises as part of a project to provide effective codes for finding a local solution x* of a nonlinear programming (NLP) problem" (NA/223, 2005, p. 1).
- "The study has been motivated by some on-going work concerning a Sequential Linear Programming (SLP) algorithm for large scale Nonlinear Programming (NLP), in which a suitable algorithm is required for carrying out unconstrained optimization in the null space. [...] Currently the obvious Conjugate Gradient (CG) methods have been used, but these have not proved to be very suitable." (ERGO 09-014, 2009, p. 1)
- [co-authored] Filters were motivated by an observation made while running SQP: "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence." (*Brief History*, 2006, p. 2)

**2.2 An application user's hard case justifies a whole line of work** [stated, primary] (NA/223, 2005, p. 2)
- He poses the objection against his own project: "In view of the ready availability of second derivatives through the AMPL modelling language, one might question whether there is a need for NLP algorithms that use only first derivatives." His answer rests on a competitor's success (SNOPT) and on a concrete application: "Such an example is the optimal design of a Yagi-Uda antenna, shown to me by Martijn van Beurden". On the 5-wire instance, filterSQP (second derivatives via AMPL) took "about 2 hours" against "about 15 minutes" for SNOPT (p. 2).
- The same passage is a statement about formulation: "An much more effective procedure [sic] is not to use AMPL at all, and to use the complex linear equations to eliminate the complex variables, leaving a much smaller problem in just the design variables." (pp. 2-3)

**2.3 Why now: a new idea from outside reopens an old one** [stated, primary]
- "I have therefore returned to some thoughts that I had some 20 years ago (Fletcher [8]), occasioned by innovative ideas inherent in the Barzilai-Borwein (BB) methods [1]." and "However the idea was not taken any further at the time, and it is a version of that idea that is explored in this paper." (ERGO 09-014, 2009, p. 2)
- In the 1960s the trigger was an unpublished report reaching him by chance: "I was lucky that Colin Reeves somehow got one and passed it on to me." (Q3, on Davidon's 1959 Argonne report)

**2.4 Where he wanted to go next** [stated, primary] (single statement, c.2005-06)
- "Nonlinear Complementarity and MPECs has interested me recently, but currently I'm still working on methods for NLP. I'd like to get back to working more on applications at some time." (Q16)

**2.5 When to stop** [stated, primary]
- For a limit he cannot explain, he accepts that nothing may be possible: the loss of benefit beyond a few back vectors "may be due to numerical loss of rank in the bundle of back vectors, in which case there may be nothing that can usefully be done." (ERGO 09-014, p. 17)
- No general statement about when to abandon a research direction was found (see Gaps).

---

## 3. Idea generation

**3.1 Code it first: computation is his way into an idea** [stated, primary] (1 interview, 3 answers: Q2, Q3, Q10)
- On his PhD with Reeves: "Of course, the ideas were fed to me by Colin Reeves; my input was mainly in getting the programs to work! Certainly this helped my subsequent work in writing optimization codes." (Q2)
- On Davidon's report: "I coded it and realized it was able to solve problems substantially faster than steepest descent." (Q3)
- On Fletcher-Reeves: "Colin Reeves was writing lecture notes on CG for Ax = b and realised that the line search aspect of the DFP method could be used to extend CG to solve nonquadratic optimization problems. Since I had a line search code I was able to follow this idea up for him by making some computations." (Q10)

**3.2 Pool experience, then add theory** [stated, primary] (Q3, on DFP)
- "Davidon's report was presented in a very unusual way, and Mike was able to extract the essential feature that was involved. We pooled our experience and added some more theory, leading to the DFP paper."

**3.3 Symmetry and duality arguments** [stated, primary] (single statement)
- On BFGS: "I found the method from the Sherman-Morrison formula via a symmetry (duality) argument." He contrasts this with the other routes: "Broyden saw that the method was one of a one parameter family of methods. [...] Goldfarb established it by a variational principle." (Q6)

**3.4 Borrow a concept from a neighbouring field** [stated, co-authored, primary] (2006)
- "We borrow the concept of domination from multiobjective optimization" (*Brief History*, p. 2). The same text insists on independence from earlier look-alikes: "Filter methods for NLP were developed independently of earlier similar ideas." (p. 5)

**3.5 Physical and geometric intuition, and its limits** [stated, primary] (Q2, Q5, Q20)
- "Davidon brought the intuition of a theoretical physicist to bear, and his ideas were very innovative." (Q5)
- On hill-walking: "Familiarization with maps, contours, local maxima and saddle points certainly helps in visualizing optimization techniques. But it doesn't help very much in understanding the complexity of high dimensional space." (Q20)

**3.6 Hybridize to keep the best property of each method** [stated, primary] (c.2005)
- "There is some evidence that the SR1 method converges faster than BFGS, especially when line searches are not used (say in a trust region context). However there is the problem of retaining a positive definite Hessian with SR1. My proposal in 2005 enables one to stay closer in a sense to SR1, whilst retaining definiteness." (Q15; the scheme is NA/223, published as DOI 10.1007/0-387-33006-2_25)

---

## 4. Experiments and execution

**4.1 First show that the new idea beats the simplest baseline, on a controlled case** [stated, primary] (2009)
- "Firstly it is important to establish whether or not the sweep method improves on the BB method (m = 1) as the number of back vectors m is increased." The controlled case was a 20-variable quadratic with eigenvalues in geometric progression. (ERGO 09-014, p. 5)

**4.2 Equal-footing comparisons using his own implementations** [stated in paper / practice, primary] (2009)
- "It is compared with (my) implementations of other standard first derivative methods, on some standard non-quadratic test problems." "The lmsd, BFGS and l-BFGS methods all use the same Wolfe-Powell line search [...] All codes use the same termination condition" (ERGO 09-014, p. 13). He also counts storage in "long vectors" for every method, e.g. "For l-BFGS, 2m + 4 long vectors are used in my implementation, as against m + 2 for lmsd." (p. 14)
- Test material named in the same section: his own classic problems (Trigonometric from Fletcher and Powell, Laplace2), Toint's Chained Rosenbrock, Raydan's Convex 2 and CUTEr problems. In NA/223 (2005): small and larger CUTE problems chosen so that "the dimension d of the null space at the solution is a significant proportion of n" (p. 15).

**4.3 Advice to users of his codes (filterSD package, 2010-2013)** [stated, primary] (R6)
- Derivative checking: "It is very easy to make errors when deriving formulae for the first derivatives [...] Such errors will almost certainly cause filterSD to malfunction, probably in an unpredictable way. Therefore the user is strongly advised to use the derivative checking subroutine checkd" (filterSD.pdf, §5).
- "This emphasises the importance of getting the gradients correct." and "users are advised not to use finite difference approximations to the gradients as an alternative to providing exact formulae. The code is not designed to allow this, and the outcome is unpredictable, as well as being inefficient." (glcpd.pdf, §9, pp. 7-8)
- Scaling and bounds: "The best advice here is to take every care in scaling the problem." and "the user is advised to provide realistic bounds on the variables, rather than just using values like 1.D20 when an upper bound is not present." (glcpd.pdf §9, p. 8). "where possible supply realistic bounds on x" also appears in the filterSD.pdf parameter list and in the filterSD.f source header.
- Error hygiene is the user's job: "The user is responsible for ensuring that any failures such as IEEE errors (overflow, NaN's etc.) are trapped and not returned to filterSD" (filterSD.pdf §3).
- Design aims, stated: "There main design aims [sic] of the code have been to avoid the use of second derivatives, and to avoid storing an approximate reduced Hessian matrix by using a new limited memory spectral gradient approach based on Ritz values." (filterSD.pdf §1; filterSD.f is dated 5 October 2011; README.pdf: "Release 2.0, Copyright (C) 2011 Roger Fletcher")

**4.4 Tuning parameters openly** [stated, primary] (2009)
- "I have selected m = 5 as a reasonable compromise as to what can best be achieved with the lmsd approach." (ERGO 09-014, p. 16). The conclusion ties the choice to realistic resources: "Fortunately the suggested choice of m = 5 is a not unreasonable value for the number of extra long vectors that might be available in a large scale application." (p. 17)

---

## 5. Judging results

**5.1 Watch the numbers** [stated, primary] (R2)
- "And in Numerical Analysis, watch for what the numbers are telling you." (Q21)

**5.2 Size claims to the evidence** [stated, primary] (R2; examples across 2005-2009)
- "Practical experience is described on small (and some larger) CUTE test problems, and is reasonably encouraging, although there is some evidence of slow convergence on large problems with large null spaces." (NA/223 abstract, 2005)
- "Thus, although the results cannot yet be taken as definitive, they do give some indication as to what level of performance can be expected from a QN code." (NA/223, p. 15)
- "The results provide no conclusive outcome either way." (ERGO 09-014, p. 16)
- "On the basis of the variety of numerical evidence provided, I feel it is reasonable to conclude that a substantial benefit is available" (ERGO 09-014, p. 17)
- On his own limited evidence: "But my (very limited) experience with formulae outside the convex class indicates that one can possibly improve on BFGS by small amounts, and still retain positive definite Hessians." (Q7)

**5.3 Say when there is no convincing explanation, then give an impression labelled as one** [stated, primary] (2009)
- On lmsd's poor Chained Rosenbrock results: "It is difficult to provide any very convincing reason for this. My impression is that, due to the way the function is constructed, the gradient path to the solution [...] has to follow a succession of steep curved valleys" (ERGO 09-014, p. 14).

**5.4 Accuracy realism** [stated, primary] (R3)
- "Getting even six figures of accuracy in the gradients is usually quite a challenge." He adds that accuracy in the variables "might be much less. Unfortunately there's no easy way to check this out [...] On the other hand, the occurrence of superlinear convergence in a Newton or quasi-Newton method is a good indication of an accurate solution." (Q13)
- "If 1 and 2 can be ruled out, I find that 3 occasionally happens in problems that I have solved." Case 3 is "Too small a tolerance on the gradient asked for (rounding errors in calculating the objective function become dominant)". Then: "Unfortunately round-off does limit the accuracy to which problems can be solved." (glcpd.pdf §9, pp. 7-8)
- "rgtol required accuracy in the reduced gradient L2 norm: it is advisable not to seek too high accuracy" (glcpd.pdf §2, p. 3; same wording in the qlcpd.f header)
- In practice, he relaxed a test criterion when it asked for more than the problem could give: "An accuracy criterion of τ = 10^-6 proved difficult to achieve due to full accuracy in f* already having been obtained with lower accuracy in g. Thus the termination criterion has been relaxed for this example." (ERGO 09-014, p. 15)

**5.5 Global convergence is required, but practice outranks a theory-driven fix that hurts performance** [stated, co-authored and single-author, primary] (R1)
- [co-authored] "We show by many numerical experiments that the performance of the PBB method deteriorates if the GLL line search is used." "With the aim of both ensuring global convergence and preserving the good numerical performance of the unmodified methods, we examine other recent work on nonmonotone line searches" (Dai and Fletcher 2005, abstract, p. 21).
- [co-authored] "Although our practical experience suggests that such behaviour is atypical, it is nonetheless prudent to modify the method by incorporating some sort of line search, so as to ensure global convergence in all cases. However it is important that the line search does not degrade the performance of the unmodified method." (same paper, p. 33)
- [co-authored] "Our goal therefore is the development of global optimization safeguards that interfere as little as possible with Newton's method. We believe filter methods achieve this goal." (*Brief History*, p. 2)
- [single author] "In applications to non-quadratic problems, it is seen to be important to preserve some sort of monotonicity property in order to be assured of global convergence. The indications are that this does not interfere with the underlying effectiveness of the unmodified method for a quadratic function." (ERGO 09-014, p. 17)

**5.6 Penalty parameters that depend on the unknown solution are a defect** [stated, co-authored, primary] (2x: the 2002 title and the 2006 review)
- "Unfortunately, a suitable penalty parameter depends on the solution of (1.1) [...] Worse, if the penalty parameter is too large, then any monotonic method would be forced to follow the nonlinear constraint manifold very closely, resulting in much shortened Newton steps and slow convergence." (*Brief History*, p. 2)
- "We have presented filter methods that promote convergence for constrained optimization algorithms without the need of artificial penalty parameters." (*Brief History*, Conclusions, p. 13)
- The same position is in the title of Fletcher and Leyffer, "Nonlinear programming without a penalty function", *Math. Program.* 91(2):239-269, 2002, DOI 10.1007/s101070100244. I checked only the title and metadata; the paper was not read.

**5.7 Credit practical success without proof, but say the proof is missing** [stated, co-authored, primary] (2006)
- On LOQO's one-entry filter: "We are not sure that this device alone can guarantee convergence. The practical performance of LOQO has been encouraging, however, underlining the computational advantage of filter methods." (*Brief History*, p. 10)

**5.8 Theory worries weighed against practical evidence** [stated, primary] (2005)
- On nonconvex QP subproblems: "Even if the QP solver can handle indefinite matrices, there is usually no guarantee that a global (or even local) solution is found to the QP subproblems. (Although it has to be said that there is little evidence that this is a serious difficulty in practice.)" (NA/223, p. 2). See Contradiction C3.

---

## 6. Writing and talks

Evidence here is thin; most of this layer is a gap.

- **Clear presentation extracts the essential feature** [stated, primary] (single statement). About Davidon's 1959 report: "Davidon's report was presented in a very unusual way, and Mike was able to extract the essential feature that was involved." (Q3). [inferred] He thought the step from an obscure presentation to the essential feature was part of the contribution.
- **Talks as a launch venue** [stated, co-authored, primary]: "NLP filter methods were first proposed by Fletcher in a plenary talk at the SIAM Optimization Conference in Victoria in May 1996; the methods are described in [8]." (*Brief History*, p. 5). No slides or transcript of that plenary were found.
- **First-person, hedged voice in single-author reports** [practice, primary]: "I feel", "My impression is", "I think these results provide some evidence", "(my) implementations" (ERGO 09-014, pp. 13-17). This is how he wrote, not a stated rule about writing. It is left for agent 03 to test across his papers.
- **Documentation as part of the work** [practice, primary]: the filterSD package ships its own user guides (filterSD.pdf, glcpd.pdf, README.pdf) with troubleshooting sections written in the first person (§4.3 and §5.4 above).
- Not found: any statement on how to structure a paper, how to write a book (the *Practical Methods of Optimization* prefaces were not read), how to referee, or how to give a talk.

---

## 7. Research organisation: environment, collaboration, students, long-term agenda

**7.1 Choosing an environment** [stated, primary]
- "I worked at Harwell from 1969 to 1973, in company with Mike Powell and others. But Harwell was becoming commercialised so I took the opportunity to move back into academia, and join the very strong NA group at Dundee. I have been very happy here." (Q17)

**7.2 How collaborations formed** [stated, primary]
- DFP came from a chance meeting and shared computing experience: "Mike presented a seminar at Leeds, and changed his title at the last moment to describe his experiences with Davidon's method. He found that I was also working on the method, hence the subsequent cooperation. I didn't know Mike previous to that." (Q4)
- He kept a clear line between respect and joint work: "I know them all well and respect their work greatly. But I have not done any joint research with them." (Q8, on Broyden, Goldfarb and Shanno)

**7.3 Students** [stated, primary] (single statement; supervision style not described)
- "I don't keep records on this, but here is a list of students with whom I have published joint papers." He then names 15, including Julian Hall and Sven Leyffer (Q18). [inferred] He counted students by joint publications, which suggests joint papers were the normal outcome of supervision. Agent 04 should check this against student accounts.
- [observed, secondary] Gould and Hall's memoir abstract: "Roger Fletcher was an inspiration to his students and collaborators alike." (DOI 10.1098/rsbm.2024.0037; abstract only)

**7.4 Long-running code projects as the research agenda** [stated, primary] (2005)
- NA/223 describes a chain of codes: filterSQP ("shown to be reliable and reasonably efficient", hooked to AMPL and "available for use under NEOS"), then filter2, then the quasi-Newton filterQN. "An experimental code filterQN is currently under development, and indeed has been so for some time. [...] The delay in finalizing the code is mainly due to uncertainty as to how best to implement feasibility restoration when second derivatives are not available." (pp. 2, 15)
- [practice, primary] The later filterSD package (Fortran 77, Eclipse Public License, release 2.0 of 2011) is on COIN-OR (github.com/coin-or/filterSD). The last commit there, dated 12 November 2015, was made by Frank E. Curtis. So the stated aim "to provide effective codes" ended in a public release. Whether filterQN was ever released is unknown.

**7.5 How others summed up his range** [observed, secondary]
- Gould and Hall (2025, abstract): "His extremely creative work covered all facets of the area: clever design, inspired analysis and detailed implementation." (DOI 10.1098/rsbm.2024.0037)

---

## 8. Failures, refuted conjectures and abandoned directions (as he stated them)

| Date | What failed or was dropped | His words (source) | Tag |
|---|---|---|---|
| c.1989 to 2009 | An idea for a limited-memory BB variant was not pursued for about 20 years | "However the idea was not taken any further at the time" (ERGO 09-014, p. 2) | stated, primary |
| 1996 to early 2000s | Parts of the first filter method proved unnecessary | "The initial filter method contained features, such as the NW/SE corner rule and unblocking, that were shown to be redundant in the subsequent convergence analysis." (*Brief History*, p. 5) | stated, co-authored |
| late 1990s | The conjecture that filters avoid the Maratos effect was refuted by a counterexample | "Early on, we conjectured that filter methods may be able to avoided [sic] the Maratos effect. [...] However, the following example shattered the hope that filter methods can avoid the Maratos effect in general [...] This example motivated us to include second-order correction (SOC) steps." (*Brief History*, p. 6) | stated, co-authored |
| 2005 | A published theory-driven fix (the GLL nonmonotone line search) degraded PBB, and the unmodified PBB was shown not to converge globally | "we show not to be the case, by exhibiting a counter example in which the method cycles" (Dai and Fletcher 2005, abstract, p. 21) | stated, co-authored |
| 2005 | filterQN stalled on feasibility restoration without second derivatives | "indeed has been so for some time" (NA/223, p. 15) | stated, primary |
| 2005 | Slow convergence of the new QN scheme on large null spaces | "It may be that this is to some extent caused by the use of an l∞ trust region." (NA/223, p. 17) | stated, primary |
| 2009 | The benefit of more back vectors in LMSD saturates | "It is a little disappointing that there seems to be a limit to the number of back vectors that can be utilised effectively." (ERGO 09-014, p. 17). Also "running out of steam at around m = 7, which is perhaps a little disappointing" (p. 5) | stated, primary |
| 2009 | lmsd did badly on Chained Rosenbrock and he had no convincing explanation | "It is difficult to provide any very convincing reason for this." (p. 14) | stated, primary |
| 2009 | CG as the null-space solver inside his SLP code | "these have not proved to be very suitable" (ERGO 09-014, p. 1) | stated, primary |

---

## 9. Era and resource context

- **1960-63, Leeds.** One of the few early university computer laboratories, "centered around a Ferranti Pegasus computer" (Q2). His PhD project was quantum-chemistry code; optimization came "latterly". The DFP (1963) and FR (1964) work came from one person with a line-search code and access to an unpublished report.
- **1969-73, AERE Harwell.** A government research laboratory, where he worked "in company with Mike Powell and others" (Q17). Dai's own framing of the period (Q17) is that Fletcher was "deeply involved in the production of high-quality software at AERE Harwell". Dai's Q6 places him "at Harwell at that time" for the 1970 BFGS paper.
- **1973-2016, Dundee.** A university NA group with PhD students. Filter methods date from 1996 (SIAM Victoria plenary). By 2005 his codes were reaching users through AMPL and NEOS, with CUTE/CUTEr as the test library (NA/223).
- **2009 compute.** LMSD tests ran "on a COMPAQ Evo N800v laptop (clock speed 1.3 GHz) under Linux, with optimized code from the Intel F90 compiler" (ERGO 09-014, p. 13). The codes were Fortran 77. [inferred] A single senior researcher writing all the codes, including the competitors' implementations, limits how far his comparisons can count as equal-footing ones.
- **Seniority.** Most first-person statements above come from his late career (aged about 66-72, some after retirement in 2005 according to the Who Was Who entry title "1993–2005 ... then Emeritus", checked in Crossref metadata). The early-career method (1960s) survives only in his own recollections in the interview, decades after the fact.

---

## Contradictions (kept, not reconciled)

- **C1 (field maturity).** c.2005-06: "I find it very hard to envisage significant new ideas in nonlinear CG and quasi-Newton methods." (Q15). Against this, 2009: he reopens a 20-year-old idea and reports "a substantial benefit" from a limited-memory gradient method "comparable [...] to what can be obtained from the l-BFGS method" (ERGO 09-014, p. 17). LMSD is a steepest-descent/Krylov method, not CG or quasi-Newton in the strict sense, so this may be a narrowing rather than a reversal. The tension about where new first-order ideas can come from remains.
- **C2 (matrix factors against matrix-free).** c.2005-06: "Many large problems are solved more effectively using sparse matrix factors [...] I can only envisage using (preconditioned) CG when nothing else is practicable." (Q13). Against this, 2011: filterSD's stated design aim is "to avoid storing an approximate reduced Hessian matrix by using a new limited memory spectral gradient approach" (filterSD.pdf §1). The linear algebra for constraints in filterSD still uses sparse factors (schurQR.f, sparseL.f), so the shift concerns only the null-space curvature model. Recorded as a dated evolution.
- **C3 (global QP solutions).** 2005: the lack of a global QP solution guarantee is raised, then dismissed: "there is little evidence that this is a serious difficulty in practice" (NA/223, p. 2). Yet the same report lists as a benefit of his design that the Hessian approximation "is a positive semi-definite matrix, which ensures that global solutions of QP subproblems are calculated" (p. 16). The 2006 review (co-authored) calls the global-QP assumption "undesirable" (*Brief History*, p. 6). The design removes a theoretical worry he said did not matter in practice.
- **C4 (scepticism against deference).** Q21 gives both "be prepared to follow your own intuition" and "be willing to change your mind when it becomes clear that other ideas have been demonstrated to be superior". He states both as a pair, so this is a balance rather than a contradiction, but a skill built on it should not collapse it into only one half.
- **C5 (data, not method): date of death.** The Royal Society fellow page says he "died on 5 June 2016". The Gould and Hall memoir title gives "15 July 2016" (Crossref metadata). A WebSearch result summary (not a page I read) says he was reported missing on 5 June and his body was found later. Left as found.

---

## Gaps (what I could not find or read)

- **Prefaces of *Practical Methods of Optimization*** (Vol. 1 1980, Vol. 2 1981; 2nd ed. 1987; paperback 2000, DOI 10.1002/9781118723203): **not read**. The Wiley front-matter PDF returned 403 and the Internet Archive copies are access-restricted lending items. This is probably his main written statement on "practical" methodology and should be the first thing added from user-supplied material.
- **Gould and Hall, Royal Society Biographical Memoir (2025), DOI 10.1098/rsbm.2024.0037**: gold open access (CC-BY), but royalsocietypublishing.org served a Cloudflare challenge (403). Only the abstract, via Crossref, was read. High priority for agents 04 and 06.
- **Powell memoir (Buhmann, Fletcher, Iserles, Toint 2018), DOI 10.1098/rsbm.2017.0023**: the green OA copy on the Namur research portal is behind a Cloudflare challenge. Only the abstract was read. It probably holds Fletcher's own first-hand account of the DFP and Harwell years.
- **SIAM News obituary** ("Obituary: Roger Fletcher", siam.org): 403, **not read**. A WebSearch result summary suggested that Sven Leyffer describes him as a no-nonsense applied mathematician who believed in simple arguments and proofs. That wording is **unverified** and is not recorded as a finding. Verify it before use.
- **The Courier tributes article** (thecourier.co.uk): 403, not read.
- **Fletcher's own reflective chapters, all identified via Crossref, not read (paywalled)**: "The Sequential Quadratic Programming Method" (Lecture Notes in Mathematics, *Nonlinear Optimization*, 2010, pp. 165-214, DOI 10.1007/978-3-642-11339-0_3); "An Overview of Unconstrained Optimization" (*Algorithms for Continuous Optimization*, 1994, pp. 109-143, DOI 10.1007/978-94-009-0369-2_5); "On the Barzilai-Borwein Method" (*Optimization and Control with Applications*, Applied Optimization series, pp. 235-256, DOI 10.1007/0-387-24255-4_10; Crossref gives no year, Semantic Scholar gives 2005); "A new approach to variable metric algorithms" (*Computer Journal* 13(3):317-322, 1970, DOI 10.1093/comjnl/13.3.317). These are the likeliest places for his personal views on SQP history and on unconstrained methods.
- **The 1996 SIAM Optimization (Victoria) plenary** where filters were first proposed: no slides, abstract or recording found.
- **Recorded talks**: yt-dlp searches of YouTube ("Roger Fletcher optimization lecture", "Roger Fletcher Dundee numerical analysis", related queries) found no talk by him. No transcript was saved.
- **His Dundee homepage** (maths.dundee.ac.uk/~fletcher/, archived by the Wayback Machine in 2019): web.archive.org was unreachable from this environment, so it was **not read**.
- **Optima (MOS newsletter) memorial pieces**: the mathopt.org archive is now a JavaScript app and old PDF paths return 404. Not read.
- **The date and newsletter name for the Dai interview**: the page is undated and the section index returns 403. "c.2005-06" is inferred from its content.
- **Layers with little or no stated evidence**: writing (layer 6), PhD supervision style (layer 7), time allocation, refereeing, and explicit rules for abandoning a direction. Nothing was found in which he states how he supervised students.
- **Optimization Online preprints with unextractable text** (Type-3 fonts): "A bundle filter method for nonsmooth nonlinear optimization" (2000/08/207) and "Numerical experience with solving MPECs as NLPs" (2002/08/522). Not read.

---

## Sources

1. Yu-Hong Dai, "An Interview with Roger Fletcher", undated (c.2005-06), Kyoto University optimization lab website, http://www-optima.amp.i.kyoto-u.ac.jp/ORB/issue22/flectcher_interview.html (fetched 2026-09-28). Primary (his own answers).
2. R. Fletcher, S. Leyffer, Ph. L. Toint, "A Brief History of Filter Methods", Argonne preprint ANL/MCS-P1372-0906, 26 Sep 2006, revised 9 Oct 2006, https://optimization-online.org/2006/10/1489/ (PDF read). Primary, co-authored.
3. R. Fletcher, "A Limited Memory Steepest Descent Method", Edinburgh Research Group in Optimization Technical Report ERGO 09-014, 2 Dec 2009, https://optimization-online.org/2009/12/2487/ (PDF read). Published as *Mathematical Programming* 135:413-436 (online 2011), DOI 10.1007/s10107-011-0479-6. Primary.
4. R. Fletcher, "A New Low Rank Quasi-Newton Update Scheme for Nonlinear Programming", Dundee Numerical Analysis Report NA/223, Aug 2005, https://optimization-online.org/2005/08/1192/ (PDF read). Published in *System Modeling and Optimization* (IFIP), pp. 275-293, DOI 10.1007/0-387-33006-2_25. Primary.
5. Y.-H. Dai, R. Fletcher, "Projected Barzilai-Borwein methods for large-scale box-constrained quadratic programming", *Numerische Mathematik* 100:21-47, 2005, DOI 10.1007/s00211-004-0569-y. Read from the course-handout copy at http://www.cs.wisc.edu/~swright/726/handouts/fletcher-barzilai-borwein.pdf. Primary, co-authored.
6. R. Fletcher, filterSD package: README.pdf ("Release 2.0, Copyright (C) 2011"), filterSD.pdf, glcpd.pdf, and source headers of filterSD.f (5 Oct 2011), glcpd.f (27 Mar 2013), qlcpd.f (18 Apr 2013), checkd.f (20 Jan 2011), checkg.f (11 Jan 2011). COIN-OR repository https://github.com/coin-or/filterSD, HEAD d0da7e78 (12 Nov 2015). Primary.
7. M. D. Buhmann, R. Fletcher, A. Iserles, P. Toint, "Michael J. D. Powell. 29 July 1936—19 April 2015", *Biographical Memoirs of Fellows of the Royal Society* 64:341-366, 2018, DOI 10.1098/rsbm.2017.0023. Abstract only (Crossref). Primary, co-authored.
8. N. I. M. Gould, J. A. J. Hall, "Roger Fletcher. 29 January 1939—15 July 2016", *Biographical Memoirs of Fellows of the Royal Society* 78:127-146, 2025, DOI 10.1098/rsbm.2024.0037. Abstract only (Crossref); full text not read. Secondary.
9. Royal Society, "Professor Roger Fletcher FRS" fellow page, https://royalsociety.org/people/roger-fletcher-11447/ (fetched 2026-09-28). Secondary.
10. N. J. Higham, "Michael J. D. Powell (1936–2015)", 5 May 2015, https://nhigham.com/2015/05/05/michael-j-d-powell-1936-2015/ and "50 Years of the Biennial Conference on Numerical Analysis", 30 Jun 2015, https://nhigham.com/2015/06/30/50-years-of-the-biennial-conference-on-numerical-analysis/ (Fletcher-Powell Lecture context only). Secondary.
11. Wikipedia, "Roger Fletcher (mathematician)", raw wikitext fetched 2026-09-28. Background only. Secondary.
12. Crossref metadata (checked, not read in full): R. Fletcher and S. Leyffer, "Nonlinear programming without a penalty function", *Math. Program.* 91(2):239-269, 2002, DOI 10.1007/s101070100244; R. Fletcher, *Practical Methods of Optimization*, Wiley, DOI 10.1002/9781118723203; "Fletcher, Prof. Roger, (29 Jan. 1939–2016), Baxter Professor of Mathematics, 1993–2005, and Professor of Optimization, 1984–2005, University of Dundee, then Emeritus", *Who Was Who*, DOI 10.1093/ww/9780199540884.013.u44012. Secondary (metadata).
