# Philippe L. Toint — Stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Philippe L. Toint (University of Namur, naXys; emeritus), living |
| Dimension | Stated methodology: what he SAYS research should be (framework §二, agent 2) |
| Research date | 2026-09-28 |
| Sources consulted | 40 documents read in full or in part: 37 primary (8 essays/papers/obituaries, 27 slide decks, 1 interview, homepage + publication list) and 3 secondary/context. 6 more were identified with checked identifiers but not read; see "Sources" and "Gaps" |
| WebSearch calls used | 1 (of 2 allowed) |
| Language | English (team.json) |

**How to read this file.**

- Tags: **[stated]** = he said or wrote it; **[practice]** = something he did (only noted here as context; agent 03 owns practice); **[observed]** = what others said about him, or what he said about someone else; **[inferred]** = my reading, not his words. Each item also says **primary** or **secondary**.
- **No user-supplied material existed** in `references/sources/{papers,talks,essays,software}` (only `.gitkeep` files). Everything below comes from public web sources.
- **Where the quotes come from.** (a) His own talk slides on `perso.unamur.be/~phtoint/talks.html`, with the text pulled out by a tool (pypdf; for the 2003 PostScript deck, strings taken from the dvips output with word breaks put back). (b) Author-hosted preprints of his essays. PostScript preprints had kerning splits that I rejoined, and every quoted string was checked against the de-spaced text. (c) SIAG/OPT *Views and News* PDFs. (d) An automatic speech-recognition (ASR) transcript of a 2026 podcast interview, saved at `../sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt`. The full pass used faster-whisper `small.en`; 13 key passages were re-run with `medium.en` (beam 5), and the quotes below use the medium wording. Podcast quotes carry timestamps and **may still contain recognition errors**: names are often misheard, e.g. "Thoine", "Lancelot", "Poe".
- **Co-authorship caveat.** Many "stated" items come from co-authored texts: with Gould ("How Mature…"), Cartis and Gould (complexity talks), Fletcher and Leyffer (filter history), and Buhmann, Fletcher and Iserles (Powell memoir). They are marked "co-authored": Toint signed them, but the wording is not certainly his alone.
- **Repetition counts.** Many of his talks reuse the same slide. When a phrase recurs across decks, the count shows that he keeps choosing to present that framing over the years. It does **not** show independent re-statements. Counts give the number of distinct decks or documents and their years.

---

## 0. Real beliefs: claims repeated at least 3 times

| # | Belief (short) | Repetitions (distinct documents, years) | Layer |
|---|---|---|---|
| B1 | Convergence theory is necessary but not sufficient; theory and practice must be balanced, and an algorithm must also be tried and implemented | ICIAM slides 2003; Gould & Toint essay 2003/2004 (3 separate passages); Francqui course 2009 ("Meaningful numerical evaluation still needed"); V&N 2006 ("combine both the more abstract aspects … with the very practical"); "does this work well in practice?" on 9 decks 2009–2018; "Can this be (more) practical?" 2017, 2018; podcast 2026 ("the theory, the experiments and the software") | 1, 5 |
| B2 | Testing and benchmarking are a crucial research activity, not a mundane chore; shared test sets (CUTE family) and performance profiles | CUTE report 1993 / TOMS 1995; ICIAM slides 2003; CUTEr report 2002 / TOMS 2003; "How Mature" 2003/2004; performance profiles on 2004, 2009, 2016 decks; podcast 2026 | 4, 5 |
| B3 | Globalization safeguards should interfere as little as possible with Newton's method ("the Newton Liberation Front"); non-monotonicity helps | Slides 2004 Florida, 2006 Lausanne, 2009 Francqui, 2016 Beijing; filter history 2006/2007 (co-authored); "non-monotonicity definitely helpful" 2004, 2009, 2016 | 3 |
| B4 | Exploit problem structure (sparsity, partial separability, multilevel, infinite-dimensional origin) | Slides 2006 CERFACS; V&N 2006 essay; Francqui 2009 lesson 5 and p. 126; "How Mature" 2003/2004 (specialization to problem subclasses); podcast 2026 ("Structure is what allows us to solve large problems") | 2, 3 |
| B5 | Worst-case complexity: "Algorithm design profits from complexity analysis", but bounds must be shown sharp by explicit examples, are "typically very pessimistic", and hide the cost of the subproblem | "Algorithm design profits…" on 4 decks (2009, 2010, 2012 ×2); "sharp? YES!!!" on 11 decks 2009–2021; "Caveat: cost of solving the subproblem!" on 9 decks 2009–2016; "typically very pessimistic" 2011; "(in the weeds of irrelevant asymptotics?)" 2016 | 3, 5 |
| B6 | A new idea is followed by the same three "obvious questions": remove the strong assumption, allow an inexact subproblem solve, check whether it works in practice | 9 decks: Francqui 2009, Toulouse 2009, Paris 2012, Chania 2012, Cracow 2013, Florianópolis 2014, Cambridge 2015, Florence 2017, Rio (ICM) 2018 | 3 |
| B7 | Applications are the field's lifeblood and a source of method; the field is "no longer interested in 'toys'" | ICIAM slides 2003; essay 2003/2004; London 2008 ("source of … methodological inspiration"); V&N 2006 ("remarkably high demand from practitioners"); outreach decks 2009, 2010, 2013, 2015 | 2 |
| B8 | Open acknowledgement of bias, open questions and unexplained behaviour | "biased by our own experience" 2003/2004; "(biased) review" 2008; "(biased) survey" 2009; "my biased and partial view" 2016; "Newton's behaviour unexplained" 2004, 2009, 2016; "Many open questions … but very interesting" 2009, 2010, 2012 | 5, 6 |
| B9 | Standing on the shoulders of giants (a sense of history, and credit to predecessors) | Bernard de Chartres quotation on 4 decks (2009, 2010, 2013, 2015); Powell obituary 2015 ("giants whose shoulders help us all to see further") | 1 |
| B10 | Mathematics as a language: "astonishingly flexible, adaptable, elegant and efficient" | Outreach decks 2010 (FR), 2013 (FR), 2015 (EN) | 1 |
| B11 | Curiosity and friendship-based collaboration as the motor of a research life | "personnal curiosity" 2007 slides; podcast 2026 twice ([0:59:32], [1:09:16]); friendship as the condition for long collaboration (Conn memoir 2019; podcast [0:39:30–0:39:50]). 3 curiosity statements in 2 documents, so borderline | 2, 7 |

---

## 1. Research taste (layer 1): what counts as good research

**T1. Theory is a necessary, not a sufficient, condition for a good algorithm.** [stated, co-authored with Gould] primary. 2003 draft, published 2004.
> "We continue today to hold the view that such a theory is a necessary, while by no means sufficient, condition for a successful algorithm."

Same essay: "It is to us very noticeable that the role of theory itself has evolved to occupy a place which we believe is well balanced with practice." The ICIAM talk slide (June 2003) has the same idea in short form: "theory viewed as a necessary condition for good algorithms".
Source: Gould & Toint, "How Mature is Nonlinear Optimization?", RAL/Namur report TR03-04 (April 2003), published in *Applied Mathematics Entering the 21st Century: Invited Talks from the ICIAM 2003 Congress*, SIAM 2004, pp. 141–161; slides `sydney03.ps`. Part of B1.

**T2. Proofs for algorithms that are never implemented are a sign of decline.** [stated, co-authored with Gould] primary. 2003/2004. This footnote sits on the page that discusses "self-centered contributions":
> "There are, in our view, too many papers presenting convergence proofs for algorithms that have never been and will probably never be properly implemented, or even tried on simple examples..."

The same essay defines senility as "a more self-centered discourse or the repetition of older ideas instead of the creation of new ones." ("How Mature…", section "Is senility lurking?".)

**T3. Honesty about exceptions to one's own principle.** [stated, co-authored] primary. 2003/2004. Right after claiming that the best algorithms are backed by theory:
> "Honesty forces us to acknowledge a few remarkable exceptions to this rule, like the BFGS variable-metric algorithm for nonconvex unconstrained minimization … or the MINOS algorithm"

**T4. Admired model: a researcher who refuses the split between theory and practice (Powell).** [stated, co-authored] primary. 2018.
> "In a subject that roughly divides into practical designers of algorithms and theoreticians who seek to underpin algorithms with solid mathematical foundations, Mike Powell refused to follow this dichotomy. His achievements span the entire range from difficult and intricate convergence proofs to the design of algorithms and production of software."

Source: Buhmann, Fletcher, Iserles & Toint, *Biogr. Mems Fell. R. Soc.* 64 (2018), doi:10.1098/rsbm.2017.0023. This praises his own PhD advisor. It also shows Toint's value (my inference, [inferred]): the whole range from proof to software.

**T5. Counterexamples count as contributions: "a deconstructor" as well as a constructor of proofs.** [stated, co-authored with Cartis] primary. April 2015.
> "Mike is well known not only as a constructor of proofs but also as a deconstructor, when he thought a proof could not be given. His keen counterexample-building skills have greatly improved our understanding"

Source: Cartis & Toint, "In Memoriam: Michael J. D. Powell (1936–2015)", *SIAG/OPT Views and News* 23(1), 2015, pp. 10–11. The 2018 memoir says the same: "Mike's remarkable talent for producing intriguing counter-examples to sometimes widely held beliefs". It links to B5, where Toint's own talks centre on explicit "slow" examples.

**T6. Rigor: vague ideas are not allowed to "hang around".** [stated / observed about Powell] primary. 2026, podcast ASR [0:26:21–0:27:01]:
> "He was quite direct and to the point, and so he was in a way rightly inquisitive about concepts. He didn't let vagueness hang around. If you had a vague idea, that didn't fit with his view of things. The ideas had to be precise and the result had to be verified and there was no room for approximations. … it was no room for approximating concepts, for sure. And for young students, that is sometimes difficult, but I guess that's how you learn."

This describes Powell. Toint presents it as the standard he learned ("that's how you learn").

**T7. Real-size problems, not "toys".** [stated] primary. ICIAM slides, June 2003 (with Gould): a field "no longer in infancy" is "conscious of the world – applications – software" and "no longer interested in 'toys'". The essay adds a nuance: "This is not to say that all small problems are uninteresting or easy, but the increasing size of the problems that can realistically be solved is, in our view, indicative of the field's evolution." Part of B7.

**T8. Beauty and power of the mathematical language.** [stated] primary. Outreach lectures 2010 (FR, Namur academic-year opening), 2013 (FR, Collège Belgique) and 2015 (EN, Oxford):
> "The mathematical language is astonishingly flexible, adaptable, elegant and efficient."

In 2010 and 2015 he adds: "A regret : not being able to share (yet) the fulgurence of the theory. . ." ("Un regret : ne pas avoir pu vous partager la fulgurance de la théorie. . ."). This is B10. It tells us what he finds beautiful, and it came up in outreach settings, not in technical talks.

**T9. Sense of lineage.** [stated] primary. He quotes Bernard de Chartres ("We are like dwarves standing on the shoulders of giants …") on the history slide of four decks (2009 Francqui, 2010, 2013, 2015). The slides that follow show portraits (Euclid … Cauchy, Dantzig; in 2009 also Powell and Fletcher). This is B9.

**T10. What a good test-problem format needs, in his own terms: to exist and to be free.** [stated, co-authored] primary. 2003/2004, on SIF: the format was "ambitiously (and, with hindsight, perhaps rather arogantly) called the Standard Input Format" [sic]. It "had and continues to have the advantages of merely existing and of coming with free decoding programs." On AMPL/GAMS: "their generalization remains, in our view, somewhat hampered by their non-trivial cost." ("How Mature…")

---

## 2. Problem choice (layer 2)

**P1. Demand from practitioners is a valid reason to take up a topic.** [stated] primary. 2006:
> "The main motivation for studying algorithms for solving this problem is the remarkably high demand from practitioners for such tools."

Source: Toint, "Using Problem Structure in Derivative-Free Optimization", *SIAG/OPT Views-and-News* 17(1), 2006, pp. 11–18. The same essay ends:
> "Developments in these directions combine both the more abstract aspects of algorithm design and theory with the very practical nature of a subject in high industrial demand. There is no doubt that they therefore constitute valuable research challenges."

So his stated test for a good problem is theory-rich AND practically demanded (B1 + B7).

**P2. Large-scale and structured problems as a lifelong direction.** [stated] primary. 2010, external-expert talk for the ADTAO project (Toulouse, in French). His self-description: "intérêt scientifique de longue date pour les problèmes de grande taille" (long-standing scientific interest in large problems). His framing of the challenge: "fournir des outils algorithmiques fiables pour la résolution de ces sous-problèmes" (provide reliable algorithmic tools for solving these subproblems). Slides `2010_toulouse.pdf`.

**P3. Specializing to problem subclasses is a fruitful direction.** [stated, co-authored] primary. 2003/2004:
> "we feel that the successful specialization of nonlinear optimization to problem subclasses (like discretized optimal control problem or DAE constrained identification problems) constitutes a fruitful evolution and will in due course become important."

The same conclusion adds: "The quest for methods that can solve problems that are intractable today … is not either anywhere near its end, a very invigourating perpective" [sic].

**P4. Infinite-dimensional origin determines behaviour, so study it.** [stated] primary. 2009, Francqui course, slide "Why consider infinite dimensions?":
> "large-scale finite dimensional problems often result from discretized continuous ones … behaviour on these problems dominated by infinite dimensional properties … Need to investigate infinite dimensions to ensure consistency!"

This is the stated rationale for his multilevel/multigrid trust-region line (2005–2015 talks).

**P5. Motivations he lists for a new method, including curiosity.** [stated] primary. January 2007, the slide "Motivation" for the penalty-free, filter-free ("trust-funnel") method (with Gould):
> "large-scale problems / PDE constrained optimal control applications / backup for a new filter method (in development) / personnal curiosity.. ." [sic]

The deck is titled "(work in progress)". Slides `2007_huatulco.pdf`.

**P6. Application areas as sources of both problems and ideas.** [stated] primary. 2008 (Computational Management Science conference, London), conclusion slide:
> "CMS continues to be the source of interesting applications / methodological inspiration"

The same deck frames algorithm quality as "Issues: reliability, availability, efficiency". Slides `2008_london.pdf`.

**P7. Choosing a PhD topic (retrospective, humorous).** [stated] primary. 2026, podcast ASR [0:15:38–0:16:20]: Powell offered two subjects, "One was SQP and the other one was large-scale non-linear problems. I did the wrong choice. I chose the second. Otherwise, my name would be associated with SQP, but that's too bad." He then describes the thesis: "the rest of my thesis was essentially building on that and working on the theory, the experiments and the software associated with this sort of topic." The first remark is a joke, not a stated regret. [inferred] The second is his own summary of research as a triad (B1).

**P8. Tuning algorithms is itself an optimization problem worth doing.** [stated] primary. 2010 (ORBEL) and 2015 (ISMP) BFO talks. 2010: "Motivation: parameter tuning in algorithm design (Audet-Orban), but many other examples. . ." 2015 poses two separate questions: tuning "on the largest possible class of applications" (designer) against tuning "on a specialized class of applications" (user), and asks "Does achieving the first does help the second?" [sic]. His conclusion: "*** Use BFO to tune your algorithm! ***" and "More user-tunable codes?"

**P9. Pick the gap that the fashionable theory leaves open.** [stated] primary. Podcast ASR [1:02:05–1:02:24], on the 2022 complexity book with Cartis and Gould:
> "But it was a time where complexity began to be a major buzzword in optimization. And a lot of the theory was and still is for the convex case. We thought that doing theory for the non-convex case was important and useful."

**P10. Problems can come from outside the field, including family.** [stated] primary. Podcast ASR [0:56:02–0:57:29]. His transportation career began with a question from his father, an urban planner: "what can you do about all this mathematics for urban planning?" He started on traffic assignment ("a very nice mathematical problem, which has lots of good history"). He says that line later "diverge[d] rather far away" from optimization, and that "the focus on mathematical traffic assignment, essentially disappeared" in favour of choice modelling and surveys. This is a direction he left, in his own words.

**P11. Curiosity as the stated motor.** [stated] primary. Three statements in two documents: "personnal curiosity.. ." [sic] as a motivation for a new method (2007 slides). Then in the 2026 podcast (ASR): "I think curiosity has not ended with my retirement, fortunately, and I'm still going on and doing so with … friends and colleagues" [0:59:32], and "as long as I can continue to be curious and as long as other people are willing to talk to me and possibly work with me, I'm happy to share" [1:09:16].


---

## 3. Idea generation (layer 3)

**I1. The three standard follow-up questions after a promising idea (B6).** [stated, with Cartis & Gould] primary. Nine decks, 2009–2018. After presenting Nesterov–Polyak cubic regularization:
> "Obvious questions: can we avoid the global Lipschitz requirement? / can we approximately minimize m and retain good worst-case function-evaluation complexity? / does this work well in practice?"

From 2013–2014 on, the slide carries answers: "YES! / YES ! / yes". The practice answer stays in lower case. That may be a deliberate hedge; this is [inferred].

**I2. Liberate Newton: design less obstructive safeguards (B3).** [stated] primary. Decks 2004 Florida, 2006 Lausanne, 2009 Francqui and 2016 Beijing (the Fletcher tribute):
> "But classical safeguards limit efficiency! Question: design less obstructive safeguards while ensuring better numerical performance (the Newton Liberation Front !) continuing to guarantee global convergence properties"

The co-authored filter history states the same aim: "Our goal therefore is the development of global optimization safeguards that interfere as little as possible with Newton's method. We believe filter methods achieve this goal." (Fletcher, Leyffer & Toint 2006/2007.)

**I3. Seed ideas from a numerical observation.** [stated, co-authored] primary. 2006/2007:
> "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence."

This observation is given as the motivation for filters: "The success of the unmodified SQP method motivates us to find a way of inducing global convergence, which would allow the full Newton step to be taken much more often." ("A Brief History of Filter Methods", *SIAG/OPT Views-and-News* 18(1), 2007, pp. 2–12; preprint ANL/MCS-P1372-0906.)

**I4. Reframe the question: from "better point" to "worse point".** [stated] primary. ICIAM 2003 and Beijing 2016 slides:
> "Classical question: what is a better point? Rephrase What is a worse point?" (2003; one symbol between "Rephrase" and "What" lost in text extraction)
> "Fletcher and Leyffer replace question: What is a better point? by: What is a worse point?" (2016)

He credits this reframing to Fletcher and Leyffer and says so repeatedly. Podcast [0:51:06–0:51:20]: "the idea was originated with Roger Fletcher and Sven Leifer [Leyffer]. And I work with them to establish the theory, the convergence theory for that method".

**I5. Borrow a structure and extend it by one dimension or one order.** [stated] primary. Two examples:
- Beijing 2016: "(Simple) idea: more dimensions in filter space" (multidimensional filter), then "Again simple idea: use g_i instead of θ_i" (filter for unconstrained problems).
- Florence 2017 / Rio 2018 / SFO 2021, "A (not so) obvious question": "If one uses a model of degree p …, why be satisfied with first- or second-order critical points???" After "A sobering example" the conclusion is "⇒ Need for a completely fresh point of view!"

**I6. Structure first (B4).** [stated] primary. 2006 CERFACS slides (with Kim & Kojima): "Problem structure =⇒ Sparse linearization =⇒ Efficient computation". The V&N 2006 essay: "Examples of this type just abound, especially when the size of the problem grows. It is interesting that their structure can very often be captured by the notion of partial separability". Podcast 2026 [0:43:10–0:43:19]:
> "Well, when you have structure, whatever it is, you should take advantage of it. Structure is what allows us to solve large problems. If they were unstructured, we would be just lost."

**I7. Complexity analysis as a design tool (B5).** [stated, with Cartis & Gould] primary. Conclusion slide on four decks (Toulouse 2009, naXys 2010, Paris 2012, Chania 2012): "Algorithm design profits from complexity analysis".

---

## 4. Experiments and execution (layer 4)

**E1. Test infrastructure is born from one's own software needs, then shared.** [stated, co-authored] primary.
- CUTE, 1993 report / *ACM TOMS* 21(1) 1995: "It is inevitable that, during the process of developing a software package, the designers concern themselves with problems of testing." Also: "All of these situations occurred during our own researches and, indeed, many of the facilities described in this paper were originally produced and tested in conjunction with the software package LANCELOT". The tools "will be useful in their own right and should be available to researchers for their development of optimization software."
- CUTEr, 2002 report / *ACM TOMS* 29(4) 2003: CUTE "originated from the need to perform extensive and documented testing on the LANCELOT package".
- Podcast 2026 [0:45:36–0:46:50] (ASR): "When we worked on Lancelot [LANCELOT], we needed the collection of test problem to test the software on. And at the time, test problems were exchanged by exchanging reports and pieces of paper. And so there was a very high likelihood of reproducing or introducing mistakes in the statements of the functions or the derivatives and so on." Also: "since we had them and we use them for testing Landslot [LANCELOT], we thought we could just give them away as well so that people could use them in the same way." And: "its success was honestly quite unexpected. We expect it to be used for a few years, of course, otherwise you wouldn't have done the work, but the success was beyond our expectation."

**E2. Testing is crucial and rests on two pillars.** [stated, co-authored] primary. 2003/2004:
> "At first sight, software testing and comparision may seem a rather mundane and unchallenging part of the algorithmic development process, but fortunately this view has now been widely replaced with the realization of its crucial nature."
> "Testing nonlinear optimization software rests on two important and complementary topics: test problems and comparison methododogy." [sic]
> "For having talked with package developers, we believe that CUTE has increased the level of testing of software packages significantly, helping to track down coding bugs and providing a better assessment of code reliability."

**E3. Report comparisons with performance profiles.** [stated, co-authored] primary. 2003/2004: "We believe that such profiles provide a very effective means of comparing the relative merits of different algorithms." The ICIAM 2003 slide lists "improved reporting methodology (performance profiles)". His filter and ARC results are shown as Dolan–Moré profiles in decks from 2003, 2004, 2009 and 2016 ([practice] context only).

**E4. Beware of overfitting when tuning.** [stated] primary. 2010 BFO deck, conclusions: "beware of overfitting!" In 2015 he reports that self-tuning BFO on CUTEst gave gains of "30% for continuous problems / 19% for mixed-integer problems compared with "intuitively reasonable values"". He tests two training objectives (average vs robust min-max over ±5% parameter perturbations) and says "robust strategy slightly better".

**E5. Scaling matters in practice.** [stated] primary. 2009 Francqui, interior-point lesson: "In practice, scaling is crucial!"

**E6. Meaningful numerical evaluation is still owed for new theory-driven methods.** [stated] primary. 2009 Francqui, conclusion of the regularization lesson: "Meaningful numerical evaluation still needed for many of these algorithms / Many issues regarding regularizations still unresolved". Compare with B1.

**E7. Software as a public good; restrictions on military use.** [stated] primary. Podcast 2026 [0:44:55–0:45:05] (ASR), on whether LANCELOT went commercial: "Yes and no. We thought we were all paid by the public funds, and so we wanted to make our research public. We made some restrictions on its use. We didn't want it to be used for the design of weapons."

**E8. Large-scale work needs software from the start.** [stated] primary. Podcast 2026 [0:39:02–0:39:09] (ASR), on first meeting Conn and Gould in 1979: "we went along very well, discussed the main thing, the needs to work on large scale problems and the needs to write software to do it."

---

## 5. Judging results (layer 5)

**J1. A worst-case bound needs a sharpness example.** [stated, with Cartis & Gould] primary. 11 decks, 2009–2021: "Is the bound in O(ε^{-3/2}) sharp? YES!!!", followed by an explicit Hermite-interpolation construction; for steepest descent, "Sharp??? YES". In the 2011 introductory talk sharpness counts as a result in its own right: "MOREOVER: the better bound (for cubic regularization) is sharp / optimal for 2nd-order methods / Explicit counter example built by Hermite interpolation".

**J2. Worst-case complexity is pessimistic, technical, and depends on hidden costs.** [stated] primary.
- 2011 (St Hubert, interdisciplinary seminar): the complexity question "strongly depends on the algorithm! … the cost of an iteration / typically very pessimistic / (usually quite tricky and technical. . . )".
- On 9 decks (2009–2016): "Caveat: cost of solving the subproblem!"
- Toronto 2016 subtitle: "(in the weeds of irrelevant asymptotics?)"
- naXys 2010: "A minimization algorithm = a rather complex (discrete) dynamical system moving towards a (possibly very) distant goal".
- He raises the relevance doubt himself, as a question in the title. Yet he keeps working in the area (Contradictions C1).

**J3. Surprises are results.** [stated] primary. 2011: "SURPRISE nr 1: a bound exists! (and is independent of problem dimension)". Then "SURPRISE nr 3: Newton's method may need as many iterations as steepest descent (in its worst case)!!! ⇒ Second-order information useless in the worst case!" The 2013 French lecture says: "Les surprises … La méthode de Newton est aussi lente, dans le pire des cas, que la (très lente) méthode de Cauchy".

**J4. Say what is not understood.** [stated] primary. "Newton's behaviour unexplained" appears in the conclusions of 2004 (Florida), 2009 (Francqui, plus ". . . more research needed?") and 2016 (Beijing). "Many open questions . . . but very interesting" closes 2009, 2010 and 2012 decks. This is B8.

**J5. Conjectures can fail; record the counterexample.** [stated, co-authored] primary. Filter history 2006/2007:
> "Early on, we conjectured that filter methods may be able to avoided [sic] the Maratos effect. … However, the following example shattered the hope that filter methods can avoid the Maratos effect in general … This example motivated us to include second-order correction (SOC) steps."

The same text: "The initial filter method contained features, such as the NW/SE corner rule and unblocking, that were shown to be redundant in the subsequent convergence analysis." Theory is used here to prune features.

**J6. Encouragement from numerical results is stated cautiously.** [stated] primary. "Encouraging so far!" (2007, method still "work in progress": "theory to be completed / current code consolidation necessary. .. / many pending implementation issues"). ". . . but this is a first encouraging step!" (2006). On FILTRANE's profiles: "This kind of numerical results is really encouraging and stimulating" (2003/2004, co-authored).

**J7. Judging a whole field: maturity vs senility criteria.** [stated, co-authored] primary. 2003/2004. Maturity signs: adequate theory, better software testing, a world of applications. Senility signs: "a more self-centered discourse or the repetition of older ideas instead of the creation of new ones". Verdict: "a mature but not yet senile domain of research". Hedge: "Of course, these arguments are biased by our own experience and work, but we believe they are shared by a number of actors in the field."

---

## 6. Writing and talks (layer 6)

**W1. Write about "concepts and research practice", not only technique.** [stated, co-authored] primary. Abstract of "How Mature…" (2003): "The discussion does not explore the technical intricacies of nonlinear optimization techniques, but instead focusses on concepts and research practice."

**W2. Talks: a fixed skeleton reused and extended over years.** [practice, noted as context] primary. His complexity decks keep the same core: problem → "useful observation" (Taylor + Lipschitz) → algorithm box → bound → proof in 5 slides → sharpness example → "Obvious questions" → conclusions + references. They grow from 2009 to 2021. Headings are short and there are many "?" and "!!!". Whether this is a stated principle: not found (Gaps).

**W3. Declare bias in reviews.** [stated] primary. "Our purpose: present a (biased) review of some of these ideas" (2008 Provence). "(and subsequent days for a (biased) survey of new optimization methods)" (2009 Francqui). "Some of his ideas (my biased and partial view)" (2016).

**W4. Outreach aim.** [stated] primary. 2010 / 2013 (FR) and 2015 (EN): "Show (by examples) that optimization is a language in which a large number of complex and interesting problems can be solved. / Share my enthousiasm and amazement at the variety and scope of its applications." The 2013 French talk closes with: "Il reste énormément à comprendre et découvrir !" (A great deal remains to be understood and discovered!)

**W5. Books grow from course notes and then keep growing; in hindsight he doubts their size.** [stated] primary. Podcast 2026 (ASR, medium model) [0:47:56–0:48:33], on *Trust-Region Methods*:
> "Well, this book started as a course, I thought [taught], in my university … and I started writing notes about the basics. And since I had those notes, I suggested to other guys that what about, you know, elaborating on this? And unfortunately, maybe we could not stop. There was always something else to say and something else to add. And so the book grew to 900 pages. In retrospect, I'm not so sure this is such a great idea to have such a massive book, but it turned out to be quite useful."

Same pattern for the 2022 complexity book [1:02:45–1:02:53]: "and again, the book is too weak [ASR; both models; probably 'too big'] for my taste, but it's very hard to stop once you're going on." He also says the 2022 book is illustrated partly with his own metal engravings [1:01:18–1:01:35] ([practice] context). The 2019 Conn memoir says the opposite about *Trust-Region Methods* (Contradictions C3). The book page on his site advertises "an entire chapter devoted to software and implementation issues" (Chapter 17, "Practicalities"). I did not read the book's preface or Afterword (Gaps).

**W6. You are responsible for what you write, including with AI.** [stated] primary. Podcast 2026 (ASR, medium model) [1:05:48–1:06:25], on teaching and research with AI:
> "I think we should encourage them to use it, but encourage them to use it in a responsible way and in a transparent way. I mean, in a sense, I keep finding that when you write something, would it be a paper or an essay or an exam or anything, you're responsible for what you write, not a machine is responsible, you are responsible. And so you better check what you say is correct and meaningful."

Right before this [1:03:43–1:04:07] he names open questions for publishing: "what is a referee, what is an author of a paper, and to some extent, what is knowledge". He adds: "I don't claim I have a final assessment about this."

---

## 7. Research organisation (layer 7)

**O1. Long collaborations rest on friendship and sustained time together.** [stated] primary. 2019:
> "But of course, such a long collaboration is only possible when based on true friendship. And our true friendship was built by sharing interests beyond the sphere of mathematical work."

Same text: collaboration with Conn "got truly going only in 1986, when Andy, on sabbatical in Grenoble, invited Nick … and me for a working week. … intense discussions and good food, the real birth of the LANCELOT project." It continued "from letters and email to (many) visits and meetings at conferences". "Altogether, Andy and I have published 44 joint papers, 39 of which with Nick … not to mention a few unpublished crazy ideas."
Source: Toint (postscript by Gould), "In memory of Andy Conn", *SIAG/OPT Views and News* 27(2), 2019, pp. 9–10.

**O2. Long research stays in partner labs.** [stated] primary. 2010 ADTAO talk (FR). The expert model he describes: "séjour de longue durée (plusieurs mois) / association à un laboratoire toulousain". The practical costs he lists: "obtenir de pouvoir quitter mon université pour plusieurs mois … collaborer avec des experts toulousains bien occupés". The outputs he lists: "nouvelles méthodes numériques, boîte à outil algorithmique pour les modélisateurs, 2 articles scientifiques, présentations à 3 conférences internationales, une nouvelle thèse et un post-doctorat en cours". The 2015–2016 decks thank Leverhulme/Balliol (Oxford) and Florence ([practice] context).

**O3. Learning from an advisor: frequent contact and high standards.** [stated] primary. Podcast 2026 (ASR, medium model) [0:22:05–0:22:19]: with Powell "We spent for instance lunchtime together in the Gratz [grad] Center having lunch every day and discussing my progress or my lack of progress. That was quite challenging for me, and I learned a lot from that." At [0:24:52–0:25:01]: "I learned enormously from him and he was a very person with very high standards for everybody, including himself, but also for his students." The 2018 memoir (co-authored) says: "His interactions with that student were constant". Powell also suggested the topic: "led him to suggest this research topic to a young PhD student, Philippe Toint".

**O4. Credit and priority handled with generosity.** [stated] primary. Podcast 2026 [0:27:46–0:28:27] (ASR): a letter Powell wrote to John Dennis after Toint "managed to get the result first" on sparse quasi-Newton updates, ahead of a Dennis student. Toint: "I was quite pleased to meet the other guy in the conference a year after that." The lesson is only implicit ([inferred]). His own supervision advice to students: not found (Gaps).

**O5. Support young people.** [stated] primary. 2019, what he values in Conn: "continued supportive interest in young people, hospitality and generosity". This is praise of a colleague, so [observed about Conn] and [stated value].

**O6. Community decisions by consultation; his own organisational misjudgement stated.** [stated] primary. Podcast 2026 [0:51:54–0:53:03] (ASR). As MOS chair (with predecessor Steve Wright) he renamed the Mathematical Programming Society to the Mathematical Optimization Society after "we ran a consultation of all the members to see whether the ID [idea] would actually make enough consensus". On keeping the journal name *Mathematical Programming* (to avoid messing up "citations and bibliographical databases"), he said: "Maybe that was a mistake and we should have done it as well."

**O7. Modest about credit for institution-building.** [stated] primary. Podcast 2026 [1:06:42–1:07:40] (ASR). He tells how he suggested to Gene Golub, at the Namur Saturday market, that "there was room in my view for a SIAM Journal on Optimization proper". Then: "maybe this conversation had a role in the creation of SIOP[T]. But I certainly would not claim being the originator of the journal."

**O8. Research as the default use of freedom; long-running partner groups.** [stated] primary. Podcast 2026 [0:58:28–1:00:36] (ASR). Retirement meant "No longer meetings, no faculty meetings … no boards of director, essentially a lot of freedom for doing what I like, which is very often research". He continues with Serge Gratton (Toulouse; met in the mid-1990s, first on data assimilation, now "method[s] for deep learning and network training") and with the Florence group (Morini, Bellavia, Porcelli), "Good people who I'm still working with on a regular basis."

---

## 8. Failures, abandoned directions, self-criticism (as he states them)

| # | What he says went wrong or was dropped | Source |
|---|---|---|
| F1 | Filter methods do not avoid the Maratos effect in general: the early conjecture was "shattered", so SOC steps were added | Fletcher, Leyffer & Toint 2006/2007 (co-authored) |
| F2 | The first filter method had redundant features (NW/SE corner rule, unblocking), removed after analysis | same |
| F3 | SIF was named "perhaps rather arogantly" [sic]. It lacks features of modelling languages (e.g. sets) | Gould & Toint 2003/2004 (co-authored) |
| F4 | CUTE's original design had deficiencies, revealed by widespread use (no multi-platform support; cumbersome with several compilers) | CUTEr report 2002 / TOMS 2003 (co-authored) |
| F5 | Newton's (and the filter's) good behaviour remains "unexplained" (2004, 2009, 2016) | slides |
| F6 | Trust-funnel 2007: "theory to be completed", "many pending implementation issues" (openly work-in-progress) | slides 2007 |
| F7 | In hindsight, unsure a 900-page book "is such a great idea" | podcast 2026 (ASR) |
| F8 | He got a poor mark in his only optimization course ("He claimed that I did not understand anything about the KKT conditions") and turned to science "mostly by accident" | podcast 2026 [0:09:49–0:13:23] (ASR). Biographical, but tells us he does not claim early talent |
| F9 | Not renaming the journal *Mathematical Programming* along with the society: "Maybe that was a mistake" | podcast 2026 [0:53:00] (ASR) |
| F10 | His transportation line drifted away from optimization: "the focus on mathematical traffic assignment, essentially disappeared" | podcast 2026 [0:56:56–0:57:29] (ASR) |
| F11 | The 2022 complexity book is also bigger than he would like: "very hard to stop once you're going on" | podcast 2026 [1:02:45–1:02:53] (ASR) |
| — | Rejected papers, retracted claims, abandoned projects in his own words: **not found** | Gaps |

---

## 9. Era and resource context

- **1977–1978 PhD (Namur, research in Cambridge with Powell, Royal Society funding).** "Large" meant about 50 variables (podcast [0:33:23–0:33:38]). Test problems were exchanged on paper. The PhD topic was suggested by the advisor (2018 memoir).
- **1980s–1990s: LANCELOT/CUTE era.** Three-person transatlantic team (Conn at Waterloo, then IBM; Gould at Waterloo, then RAL/CERFACS; Toint at Namur). They worked by letters, email, visits, and one decisive working week in Grenoble. Fortran and anonymous ftp. Software released free, with a non-weapons restriction (podcast).
- **2000s: filter and multilevel era.** The Fletcher–Leyffer–Toint and Gould–Leyffer–Toint collaborations. FILTRANE was built inside GALAHAD and tested on CUTEr with performance profiles.
- **2008–present: complexity era with Cartis and Gould** (Oxford/RAL, Leverhulme/Balliol visits). Later work with Florence (Bellavia, Morini) and Toulouse (Gratton): inexact, stochastic, and objective-function-free methods. During 2012–2015 he was also vice-rector for research and IT (Imperial 2015 seminar bio). That seniority and administrative load is context for claims made in those years.
- A parallel career in transportation modelling (director of the Transportation Research Group) supplies many "application" examples (discrete choice, synthetic population) in his outreach decks.

---

## 10. Contradictions (kept, not reconciled)

- **C1. Relevance of worst-case complexity.** He states "Algorithm design profits from complexity analysis" (4 decks, 2009–2012). He also calls bounds "typically very pessimistic" (2011) and asks "(in the weeds of irrelevant asymptotics?)" (2016). The question is left open in his own titles.
- **C2. "Theory necessary but not sufficient" vs his own complexity-first program.** In 2003/2004 he criticises "too many papers presenting convergence proofs for algorithms that have never been … implemented, or even tried on simple examples". His 2009 course says "Meaningful numerical evaluation still needed for many of these algorithms". In later complexity decks the practice question keeps a lower-case "yes" (2013–2018) and "Can this be (more) practical?" (2017, 2018). Whether his later papers meet his own 2003 standard is for agent 03 to check. The tension is recorded here.
- **C3. The size of *Trust-Region Methods*.** In 2019 he presents the book's "sheer size … and the scope of its table of contents" as evidence of the authors' commitment ("Those possibly doubting the intensity of our common involvement should have a look at the sheer size of this book"). In 2026 he says: "In retrospect, I'm not so sure this is such a great idea to have such a massive book, but it turned out to be quite useful" (ASR, medium model [0:48:27]).
- **C4. Dates and counts in his collaboration story.** 2019 (written): collaboration with Conn and Gould "got truly going only in 1986, when Andy, on sabbatical in Grenoble"; "44 joint papers" with Conn, "39 of which with Nick". 2026 (spoken, ASR medium model [0:39:16–0:39:43]): "a few years later, I think it was in 81, Andy went for a sabbatical in France in Grenoble"; "I think we wrote more than 50 papers together". Both ASR models give "81". This is probably a memory slip, but it is left as recorded.
- **C5. Origin of trust regions vs the filter credit.** No contradiction found. He consistently credits Powell (1970) for trust regions (podcast; 2015 obituary) and Fletcher & Leyffer for filters ("the filter methodology introduced by Fletcher and Leyffer", 2003/2004 essay; 2016 slides; podcast).
- **C6. Humility vs visible pride.** He says "I certainly would not claim being the originator of the journal" (SIOPT) and plays down the SQP choice as a joke. Of the Conn–Gould collaboration he says "a long and very nice story which I'm very proud of" (podcast [0:39:43]). No real tension; recorded for the persona layer.

---

## 11. Gaps (searched for, not found or not readable)

- **No "how to do research" essay, PhD-advice text or lab guide** by Toint was found on his homepage, talk list, publications list, the SIAG/OPT newsletter archive, or through the one web search.
- **Prefaces not read:** *Trust-Region Methods* (SIAM 2000; preface, Chapter 17 "Practicalities", Afterword) and *Evaluation Complexity of Algorithms for Nonconvex Optimization* (SIAM 2022; preface and "Perspectives"). SIAM epubs returned HTTP 403. *LANCELOT* (Springer 1992) preface was also not read.
- **Optima 88 (2012) "How much patience do you have? A worst-case perspective on smooth nonconvex optimization"** (Cartis, Gould & Toint) was not read. The author-hosted PDF returned 404 and old Optima PDFs are not on the new mathopt.org site. Web-archive access is blocked by the egress policy.
- **MOS Chair's columns in *Optima* (2010–2013)** were not read, for the same reason.
- **ISMP 2012 opening address**, "Remembering Andrew Conn" (ICCOPT 2019) and "Remembering Michael Powell and Roger Fletcher" (NAOIV 2017) are listed on his talk page without slides.
- **Acta Numerica 2005 survey** (Gould, Orban & Toint, doi:10.1017/S0962492904000248): the author preprint TR04-08 has font-encoded text that could not be extracted, so it was not read.
- **ICM 2018 proceedings chapter** (doi:10.1142/9789813272880_0198): not read (publisher 403). Only the ICM talk slides were read.
- **CUTEst 2015 paper** (doi:10.1007/s10589-014-9687-3): not open access, not read.
- **"Optimisation", Encyclopédie Philosophique Universelle (1990)**: a philosophical entry by Toint, listed on his publications page, not available online. Not read.
- **Podcast 2026:** the ASR transcript is machine-made. Quotes should be re-checked against the audio before being used as verbatim in the final skill.
- **What he tells his own students** (supervision rules, how he picks student topics, how he writes with students): nothing stated found. Agent 04 may find student recollections.
- **Rejected papers or retracted results in his own words:** none found.

---

## 12. Sources

Primary sources were written or spoken by Toint (alone or as co-author). "Checked" means the identifier or venue/year/title was confirmed with a tool in this run: Crossref API, or his own publication list at perso.unamur.be.

**Essays, papers, obituaries**

1. N. I. M. Gould & Ph. L. Toint, "How Mature is Nonlinear Optimization?", in *Applied Mathematics Entering the 21st Century: Invited Talks from the ICIAM 2003 Congress* (J. H. Hill, R. Moore, eds., as given on his publication list), SIAM, 2004, pp. 141–161. Read as author preprint TR03-04 (April 2003 draft): https://perso.unamur.be/~phtoint/pubs/TR03-04.ps. Venue/year/title checked on his publication list. Primary, co-authored.
2. R. Fletcher, S. Leyffer & Ph. L. Toint, "A Brief History of Filter Methods", *SIAG/OPT Views-and-News* 18(1), 2007, pp. 2–12 (preprint ANL/MCS-P1372-0906). Read at https://perso.unamur.be/~phtoint/pubs/TR06-04.pdf; issue confirmed at https://siagoptimization.github.io/assets/views/18-1.pdf. Primary, co-authored.
3. Ph. L. Toint, "Using Problem Structure in Derivative-Free Optimization", *SIAG/OPT Views-and-News* 17(1), 2006, pp. 11–18. https://siagoptimization.github.io/assets/views/17-1.pdf. Primary.
4. Ph. L. Toint (with postscript by N. Gould), "In memory of Andy Conn / In Memoriam Andrew Conn (1946–2019)", *SIAG/OPT Views and News* 27(2), 2019, pp. 9–10. https://siagoptimization.github.io/assets/views/ViewsAndNews-27-2.pdf. Primary.
5. C. Cartis & Ph. L. Toint, "In Memoriam: Michael J. D. Powell (1936–2015)", *SIAG/OPT Views and News* 23(1), 2015, pp. 10–11. https://siagoptimization.github.io/assets/views/ViewsAndNews-23%281%29.pdf. Primary, co-authored.
6. M. Buhmann, R. Fletcher, A. Iserles & P. Toint, "Michael J. D. Powell. 29 July 1936—19 April 2015", *Biographical Memoirs of Fellows of the Royal Society* 64 (2018) 341–366, doi:10.1098/rsbm.2017.0023 (Crossref checked). Read at https://perso.unamur.be/~phtoint/pubs/Powell.pdf. Primary, co-authored.
7. I. Bongartz, A. R. Conn, N. Gould & Ph. L. Toint, "CUTE: Constrained and Unconstrained Testing Environment", *ACM TOMS* 21(1), 1995, doi:10.1145/200979.201043 (Crossref checked). Read as report TR93-10 (Oct 1993): https://perso.unamur.be/~phtoint/pubs/TR93-10.ps. Primary, co-authored.
8. N. I. M. Gould, D. Orban & Ph. L. Toint, "CUTEr and SifDec: a Constrained and Unconstrained Testing Environment, revisited", *ACM TOMS* 29(4), 2003, doi:10.1145/962437.962439 (Crossref checked). Read as report TR02-07: https://perso.unamur.be/~phtoint/pubs/TR02-07.ps. Primary, co-authored.

**Talk slides** (all from https://perso.unamur.be/~phtoint/talks.html; primary)

9. "How mature is Nonlinear Optimization?" (with N. Gould), ICIAM, Sydney, June 2003, `talks/sydney03.ps`.
10. "Trust regions, filter and non-monotonicity…" / "Non-monotonicity and filter methods in nonlinear optimization", 2004 (Gainesville, Florianópolis, Tilburg), `talks/2004_florida.pdf`.
11. "Filters: an efficient tool for nonlinear programming", 2006 (Lausanne and others), `talks/2006_lausanne.pdf`.
12. "Recognizing Underlying Sparsity in Optimization" (Kim, Kojima, Toint), Sparse Days CERFACS, June 2006, `talks/2006_cerfacs.pdf`.
13. "Nonlinear programming without a penalty function or filter" (with N. Gould), Huatulco, Jan 2007, `talks/2007_huatulco.pdf`.
14. "Some new developments in nonlinear programming", GOM08, Aug 2008, `talks/2008_provence.pdf`.
15. "New developments in nonlinear programming with perspectives for management sciences", CMS London, 2008, `talks/2008_london.pdf`.
16. "Advanced Algorithms in Nonlinear Optimization", Belgian Francqui Chair course, Leuven, April 2009 (323 slides), `courses/francqui.pdf`.
17. "Cubic regularization algorithm and complexity issues for nonconvex optimization", Toulouse, Aug 2009, `talks/2009_toulouse.pdf`.
18. "BFO: a simple brute-force optimizer", ORBEL 24, Jan 2010, `talks/2010_orbel.pdf`.
19. "Le point de vue d'un expert extérieur du projet ADTAO", Toulouse, June 2010, `talks/2010_toulouse.pdf`.
20. "A (quick) overview of some complexity issues for nonconvex optimization", naXys opening day, Oct 2010, `talks/2010_naxys.pdf`.
21. "Une promenade informelle dans le monde de l'optimisation mathématique", Namur academic-year opening, Sept 2010, `talks/2010_rentree_academique.pdf`.
22. "An introduction to complexity analysis for nonconvex optimization", St Hubert, Jan 2011, `talks/2011_st_hubert.pdf`.
23. "Evaluation complexity in smooth constrained and unconstrained optimization", Paris 2012, `talks/2012_paris.pdf`.
24. "Complexity Issues for Nonconvex Optimization", OMS Chania 2012, `talks/2012_chania.pdf`.
25. "Complexity in nonlinear optimization", 2013 (La Roche, Florence, Krakow), `talks/2013_cracovie.pdf`.
26. "Une promenade informelle dans le monde de l'optimisation mathématique", Collège Belgique, Namur, Oct 2013, `talks/2013_college_belgique.pdf`.
27. "Evaluation Complexity In Nonlinear Optimization Using Lipschitz-Continuous Hessian", X BRAZOPT, March 2014, `talks/2014_florianopolis.pdf`.
28. "How much patience do you have? Issues in complexity for nonlinear optimization", Cambridge/Edinburgh 2015, `talks/2015_cambridge.pdf`; and Toronto (Fields) June 2016, `talks/2016_toronto.pdf`.
29. "An informal walk in the world of mathematical optimization", Oliver Smithies and Leverhulme Lecture I, Balliol, Oxford, Nov 2015, `talks/2015_balliol_students.pdf`.
30. "Algorithm Tuning Using Optimization", ISMP Pittsburgh, July 2015, `talks/2015_pittsburgh.pdf`.
31. "Filter methods: a tribute to Roger Fletcher", ICNAAO Beijing, Aug 2016, `talks/2016_beijing_for_roger.pdf`.
32. "A path and some adventures in the jungle of high-order optimization", Rome/Florence 2017, `talks/2017_florence.pdf`; and "Worst-case evaluation complexity for nonconvex optimization: adventures in the jungle of high-order nonlinear optimization", ICM 2018 Rio, `talks/2018_rio.pdf`. The related proceedings chapter (Cartis, Gould & Toint, *Proc. ICM 2018*, doi:10.1142/9789813272880_0198, Crossref checked) was not read.
33. "Recent results in worst-case evaluation complexity for smooth and non-smooth, exact and inexact, nonconvex optimization", SFO 2021, `talks/2021_SFO.pdf`.

**Interview**

34. "Subject to: Philippe Toint", podcast hosted by Anand Subramanian, published 27 July 2026, 1:11:05. RSS https://anchor.fm/s/4dbe3348/podcast/rss; episode https://podcasters.spotify.com/pod/show/subject-to/episodes/Subject-to-Philippe-Toint-e3mjb27. Local ASR transcript: `../sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt`. Primary (his spoken words; machine transcript).

**Context and secondary**

35. Toint homepage and publication list, https://perso.unamur.be/~phtoint/toint.html and https://perso.unamur.be/~phtoint/publications.html (accessed 2026-09-28). Primary, for the bibliography.
36. *Trust-Region Methods* book page, https://perso.unamur.be/~phtoint/pubs/trbook.html (SIAM blurb; Conn, Gould & Toint, SIAM 2000, doi:10.1137/1.9780898719857, Crossref checked). Book not read. Secondary (publisher blurb).
37. Imperial College seminar page, "Worst-case complexity of nonlinear optimization: Where do we stand?", 11 Feb 2015 (abstract and bio): https://www.imperial.ac.uk/events/105173/. Secondary (bio text probably supplied by Toint).
- Also checked, not read: *Evaluation Complexity of Algorithms for Nonconvex Optimization: Theory, Computation and Perspectives* (Cartis, Gould & Toint, SIAM 2022, doi:10.1137/1.9781611976991); *LANCELOT* (Conn, Gould & Toint, Springer 1992, doi:10.1007/978-3-662-12211-2); CUTEst (Gould, Orban & Toint, *Comput. Optim. Appl.* 60(3), 2015, doi:10.1007/s10589-014-9687-3). All Crossref checked.
- University of Namur research portal profile, https://researchportal.unamur.be/en/persons/phtoint/ (lists "Press/Media (1)" and "Foreword/postscript 1"; sub-pages returned 403; not read). Secondary.
