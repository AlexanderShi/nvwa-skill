# Jorge Nocedal: stated research methodology (research agent 02)

| Field | Value |
|---|---|
| Researcher | Jorge Nocedal (Northwestern University, IEMS; living) |
| Dimension | 02 Stated methodology: what he *says* research should be (framework §一 seven layers, §二 agent 2) |
| Research date | 2026-09-28 |
| Sources consulted | 23 read (18 primary, 4 secondary with direct quotes, 1 mixed), plus 5 works cited by identifier only (checked on Crossref, not read). See "Sources" |
| WebSearch calls | 2 (of 2 allowed). Everything else came from curl or yt-dlp on known URLs and from the Crossref and arXiv pages |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}` held only `.gitkeep` when this run started. Nothing under `private/` was opened |
| Transcripts saved | 7 files in `../sources/talks/` (names listed under "Sources") |

**How to read this file.**
- Every item is tagged **[stated]**, **[practice]**, **[observed]** or **[inferred]**, and marked primary (his own words) or secondary (a journalist or co-author reporting them).
- This file records only what he *says*. Whether he does it is agent 03's job. A few [practice] or [observed] notes are included only where they date or qualify a statement.
- **Caption-derived quotes.** Quotes from talk and interview videos come from YouTube caption tracks. Most are automatic speech recognition (ASR); the Simons 2017 and Purdue 2017 tracks were supplied by the uploader. They are copied **verbatim from the captions**, including ASR misspellings (marked [sic], with the likely word in brackets). They were not checked against the audio. Timestamps refer to the transcript files in `../sources/talks/`.
- **PDF quotes.** Quotes from his PDFs (1992–2006) were extracted with pypdf. Only the spacing damaged by extraction was normalised. Page numbers are those of the author's PDF on his homepage.
- **Co-authored texts.** Statements from papers written with others (Knitro 2006, the SIAM Review 2018 survey, the 2003 benchmark paper, the 2021/2022 finite-difference paper) are the *co-authors' joint* stated position. They are marked "(co-authored)".

---

## 0. Beliefs repeated at least 3 times (framework: repetition = real belief)

| # | Belief (short form) | Repetitions found, with dates | Layer |
|---|---|---|---|
| R1 | Good optimization research has to combine mathematical analysis, algorithm design and software (plus numerical experiments). Heuristics alone and pure theory alone are both not enough | 2017 speech; 2017 McCormick news quote; 2021 UCLA talk; 2024 SIAM press release; 2026 interview (Powell school, the Knitro story) → **5** | 1, 4 |
| R2 | Judge theory by practice: it should explain methods *as implemented* and tell efficient methods from inefficient ones. Global convergence and worst-case complexity alone often fail to do this | 1992 Acta Numerica (several places); 1996 survey; 2018 SIAM Review (co-authored); 2019 RIIAA keynote; 2021 UCLA talk; 2026 interview → **6 sources** | 1, 5 |
| R3 | You trust a method once you have tried everything else, and the answer is often a return to an old, simple tool (quasi-Newton updating, finite differences) | 2017 Simons talk; 2021 UCLA talk; 2026 interview (L-BFGS story, and the Churchill joke) → **3** | 3, 5 |
| R4 | Re-examine simple baselines that the literature has dismissed. The field often fails to compare against them | 2017 Simons talk; 2021 UCLA talk; 2021 arXiv / 2022 OMS abstract (co-authored); related contrarian stance on SGD in the 2018 SIAM Review (co-authored) and in 2017 (secondary) → **3–5** | 1, 4 |
| R5 | Exploit the structure of the problem instead of applying a generic method, even your own famous one | 1996 survey; 2024 NITMB talk; 2026 interview (weather forecasting; Google speech recognition; structure of neural networks) → **3 sources, 5 statements** | 2, 3 |
| R6 | Ideas come from collaborative brainstorming and debate, clashing intuitions and long discussions | 2017 speech; 2021 McCormick Magazine; 2024 NITMB Q&A; 2026 interview (Byrd; US–Mexico workshops) → **4** | 3, 7 |
| R7 | Scale is the core challenge: algorithms must scale with the number of variables (and, later, with nonlinearity and uncertainty) | homepage statement (undated, around 2016–18); 2014 SIAM clip; 2024 SIAM press release; 2026 interview (thesis goal "millions of variables") → **4** | 2 |
| R8 | Robust algorithms must detect their own mistakes and correct themselves (self-correction, recovery procedures) | 1992 Acta (BFGS self-correction); 2017 Simons talk; 2021 UCLA talk; 2026 interview (the self-correcting property in the Byrd–Nocedal analysis) → **4** | 4, 5 |

Beliefs stated fewer than 3 times (for example the critique of publication metrics, which appears in only one source, 2026) are kept below but not promoted to "real belief".

---

## 1. Research taste: what is worth doing, what counts as a good result

**T1. The Powell (and Fletcher) school: applications → rigorous algorithms → software.** [stated, primary, caption-derived]. 2026 interview [0:39:18]:
> "they have a certain style of going saying my ultimate goal is to do applications in order to do that I have to design algorithms but I'm not going to design algorithms heristically [sic: heuristically] I'm going to have a rigorous analysis to understand how they work so this combination of you do the analysis the algorithm then you write it in software was the Powell school and that's what it really appealed to me"

He rejects the two alternatives by name. The pure-mathematics side of optimization "like Rockefeller [sic: Rockafellar] and Clark [sic: Clarke]" was "different that's pure math in some sense". And:
> "there were empirical optimizers who would design algorithms by doing drawing pictures and that didn't appeal to me either" [0:39:51]

The 2017 speech says the same thing in writing [stated, primary, 2017 acceptance speech]:
> "Mike Powell, whose vision of nonlinear optimization guides my research to this day. Here, algorithmic innovation comes through numerical experimentation and mathematical analysis. The right balance is not for us to decide but is driven by the topic. It has its roots in the numerical analysis school of Wilkinson as much as in the optimization school of Dantzig and his generation."

**T2. Theory, algorithm design and software are "three indispensable components".** [stated, secondary: direct quote in a SIAM press release, 2 Apr 2024]:
> "These advances would not have been made possible if I had not considered theory, algorithmic design, and software development as three indispensable components."

He placed himself the same way in 2017 [stated, secondary: McCormick news, 26 Oct 2017]:
> "I was very surprised to receive this award because I am not a pure theoretician … I am just as much a computer scientist who likes to create software and see it impact new application areas, such as machine learning. It is very gratifying to see that this style of research was recognized by such a prestigious award."

And, pluralistically, in the 2017 speech: "Research can be done in so many ways. I have always admired the theoreticians, the model builders, and the software creators. I hope that this community continues to support them all." → R1.

**T3. Theory is valued for how well it explains and discriminates practical methods.** [stated, primary, Acta Numerica 1992, author's PDF pp. 1–2]. He opens the survey with a user's question:
> "from the point of view of a user of nonlinear optimization routines, how interesting and practical is the body of theoretical analysis developed in this field? … I decided to select the best optimization methods known to date – those methods that deserve to be in a subroutine library – and for each method ask: what do we know about the behavior of this method, as implemented in practice?"

and adds a second criterion:
> "We should also ask how useful is the theory when designing new algorithms, i.e. how well can it differentiate between efficient and inefficient methods."

**T4. Global convergence alone is not the goal.** [stated, primary, Acta 1992, p. 7]:
> "In addition to global convergence we would like the methods to converge rapidly. After all, if all we want to achieve is global convergence we should be satisfied with the steepest descent method."

**T5. Much theory explains practice without creating methods.** [stated, primary].
- Acta 1992, p. 16: "Ironically, our many theoretical studies of variable metric methods have not resulted in the discovery of new methods, but have mainly served to explain phenomena observed in practice."
- Four years later, on the conjugate-gradient convergence literature ("Large scale unconstrained optimization", survey dated 23 June 1996, p. 20): "Even though most of these theoretical results are interesting, and some of the proof techniques are innovative, these studies have not lead [sic] to significant practical advances in nonlinear CG methods. Their main contribution has been a better understanding of the crucial role played by line searches."

(See Contradiction C2 for the opposite claim about Knitro.)

**T6. Skepticism about worst-case complexity as the arbiter of algorithms.** [stated, primary, caption-derived] → R2.
- RIIAA keynote 2019 [0:17:34–0:18:07], on "the Russians the complexity school" and pure random sampling: "their algorithm from the point of view of complexity is very good from a point of view of computation is really bad".
- UCLA 2021 [0:04:28]: "complexity analysis is not very helpful in this case the best algorithms from the point of view of worst case complexity and end up being randomized algorithms it could be very simple like simple random search so we're going to have to base our intuition".
- UCLA 2021 [0:24:59], on random-direction gradient estimates: "they are better for the worst case analysis but it's unlikely to to do better than a finite difference approach in practice".
- 2026 interview [1:29:02]: "recently the field has become focusing on complexity results. So, that's even more difficult to follow because some of those results actually are even lacking intuition. They're not distinguishing between good methods and bad methods." He adds that computation "used to be the core now it's a smaller field … the field has become more theoretical and less accessible".
- Co-authored version (Bottou–Curtis–Nocedal, SIAM Review 2018, Inset 4.2, arXiv p. 25): the authors analyse the strongly convex case because of "a desire to present results that are more relevant to actual practice", and they skip almost-sure convergence because "in our view, they do not provide significant additional insights into the forces driving convergence of the method."

**T7. The ideal result is one nobody can improve on, and beautiful.** [stated, secondary: direct quote in McCormick Magazine, Spring 2021]:
> "My students and I try to find not only the solution, but also the most beautiful solution … We aim to develop something that people can't improve upon—this is the ideal."

**T8. Admires originality and courage above technical polish.** [stated, primary, caption-derived, 2026 interview]
- On Dantzig [0:44:56]: "professor Danik [sic: Dantzig] is not the best mathematician here by far but he is the most courageous … nothing stops him … That was a very good example of how how you develop research."
- On Davidon's quasi-Newton idea [1:36:15]: "totally revolutionary was totally original one of the most original ideas in optimization ever". He ranks his own L-BFGS well below it.
- He left his first PhD advisor because "this professor was kind of all doing the same thing. There was nothing really new" [0:38:12].

**T9. No single method wins everywhere; keep complementary approaches.** [stated, primary, co-authored]
- Knitro paper (Byrd, Nocedal, Waltz 2006, author's PDF p. 1): "as is well known, no single approach is uniformly successful in nonlinear optimization." And p. 3: "We take the view that interior-point and active-set methods will both be needed in the years to come."
- The same stance, earlier and single-authored (Acta 1992, p. 32): line-search and trust-region methods "coexist, and it is difficult to predict if one of these two approaches will become dominant."

---

## 2. Problem choice: where problems come from, why now, when to quit

**P1. "Where you place the ladder" matters more than climbing skill.** [stated, primary, 2017 speech]:
> "Recently I heard a senior faculty tell a junior colleague: 'it is not just how good you are at climbing ladders, it is where you place the ladder'. Richard and I spent – it seems – endless time debating where to place the ladder."

It closes with "Falling down from ladders can happen in so many different ways… You, young people should be prepared. I am eager to see where will you put the ladder." The 2026 interview repeats the choice criterion [1:40:12]: young researchers should ask "What is the most likely way that you'll make an important contribution?"

**P2. Problems come from applications, especially very large ones.** [stated, primary]
- Homepage research statement (undated; the page links the SIAM Review 2018 paper as "New", so around 2016–18): "There is a need for solving ever larger optimization problems, and throughout the years, I have developed algorithms that scale well with the number of variables, make judicious use of second-order information, and parallelize well. The motivation for my current algorithmic and theoretical research stems from applications in image and speech recognition, recommendation systems, and search engines."
- 2024 SIAM release: "A problem with 1,000 decision variables was considered very challenging when I was a student, whereas now we can solve problems with millions of variables … That triple combination of high dimensionality, nonlinearity, and uncertainty seemed insurmountable at some point".
- 2014 SIAM clip: the speech-recognition scale "10 million" parameters and "100 million" training points. → R7.

**P3. Pick a scaling goal and pursue it, even through failure.** [stated, primary, caption-derived, 2026 interview [0:46:37]]:
> "Quasi Newton methods were very new then, but people could only solve small problems with them. And I don't know why I decided what I really wanted to do is to develop quasant [sic: quasi-Newton] methods that scaled up into millions of variables".

(Era: Rice/Stanford around 1975–78, punch cards. See §8.)

**P4. Choose big, consequential problems: impact on people over impact inside codes.** [stated, primary, caption-derived, 2026 interview [1:14:00–1:14:34]]. On the ECMWF 4D-Var weather-forecasting project of the 1990s, which he calls his most important practical contribution: "if you see the effect of good weather forecast over people's lives and the economy and so on it must be much bigger than the effect that our codes have within airplanes and cars", and "at that time I already knew that this was a major problem". Related paper, checked by identifier and not read: Fisher, Nocedal, Trémolet, Wright, "Data assimilation in weather forecasting: a case study in PDE-constrained optimization", *Optimization and Engineering* 10(3):409–426, DOI 10.1007/s11081-008-9051-5.

**P5. Enter a field when it poses problems you have never seen, and when the incumbent answer is not final.** [stated]
- McCormick Magazine 2021 (secondary, direct quote): "I don't think that we have found the best optimization for machine learning—that's my main motivating force … Apart from the impact that new optimization ideas could have, I'm drawn to the fact that machine learning poses problems that I've never seen before."
- 2017 (secondary, McCormick news, 19 May 2017): "Us optimizers can't be satisfied that stochastic gradient descent … is the final solution".
- Co-authored (SIAM Review 2018, p. 39): "The theoretical arguments in the previous section, together with extensive computational experience, have led many in the machine learning community to view SG as the ideal optimization approach for large-scale applications. We argue, however, that this is far from settled."
- NITMB Q&A (24 Oct 2024, primary written answer): "One of the big open questions today is how to train deep neural networks efficiently."

**P6. New fields favour newcomers.** [stated, primary, NITMB Q&A 2024]:
> "there are no experts in this incipient field. A young researcher is as likely to make a discovery as an established math or biology researcher. In fact, since we need a new mindset to develop the intersection of these two fields, young people have the advantage since they do not have an established approach to their research."

**P7. Timing and missing the boat.** [stated, primary, caption-derived, 2026 interview [1:42:53–1:44:47]]. His stated regret is seeing too late that machine learning was "different from the other ones … In machine learning, nobody has established anything. The field is still a mystery. So this is up for grabs". He says he "could have actually developed this and it didn't happen … sometimes you say well I really missed the boat". (The details are in §9.)

**P8. When to quit.** No explicit stated rule was found. The nearest statements are the "fog of uncertainty" remark (J5) and the thesis story (F1). → Gap.

---

## 3. Idea generation

**I1. Brainstorming and debate with trusted colleagues.** [stated, primary] → R6.
- 2017 speech: "For me, it has been a collaborative experience where ideas came through brainstorming. And none of those interactions proved as crucial as my long-time exploration with my constant friend and colleague, Richard Byrd."
- NITMB Q&A 2024: "I like to debate and discuss far-out ideas with some of my colleagues. Brainstorming has been one of my modes of operating. I find it liberating."
- McCormick Magazine 2021 (secondary, direct quote): "Insights clash, intuitions may diverge, and people may get passionate. Then suddenly, out of the fog, you get some clarity … And you feel there was a team of people who did it."
- 2026 interview [0:41:33]: with Byrd, "after school we would discuss math in the bar or in the beach … we did this for years and years."

**I2. Read the classics and read outside the discipline.** [stated, primary, NITMB Q&A 2024]:
> "I have found inspiration by reading classic papers and trying to understand how other researchers came up with innovative ideas. I don't look only at my discipline. I try to read more broadly about fundamental breakthroughs in other areas of science."

**I3. Simplify after failure. The good idea came as a simpler reformulation once complicated attempts had failed.** [stated, primary, caption-derived, 2026 interview [0:50:00]]. The L-BFGS origin, UNAM 1978–79:
> "I went to the board and I realized I did the wrong thing in my thesis. All these methods are too complicated. This is not the way to do that. I was trying to extend the conjugate gradient method. Transform quasin [sic] Newton into conjugate gradients. There was the wrong way to do that."

Paper, identifier checked: Nocedal, "Updating quasi-Newton matrices with limited storage", *Mathematics of Computation* 35(151):773–782, 1980, DOI 10.1090/S0025-5718-1980-0572855-7 (not read in this run).

**I4. Put the effort where it matters: estimate derivatives well and reuse proven model machinery.** [stated, primary, uploader subtitles, Simons 2017 [0:40:30–0:41:04]]:
> "Every time I see interpolation, I see my hands tied … I thought about this for two years. I realized the only way I know how to produce models that I can solve in Otime [sic: O(n) time] is with Quasi-Newton updating … So the motivation over there was put all the effort then in estimating the derivatives. Don't put so much effort on the model. Put the effort on estimating the derivatives. And be ready to fail there and to recover if you have a difficulty there".

**I5. An empirical regularity without a proof is an invitation for theory.** [stated, primary, uploader subtitles, Simons 2017 [0:09:37]]. On BFGS applied to nonsmooth problems: "nobody has observed a failure. So therefore, one should be able to prove a result … One needs a very clever theoretician to work through that theory". The 1992 open questions have the same form (Acta p. 21, before Open Question II): "Even though the numerical experience of many years suggests that the BFGS method always converges to a solution point, this has not been proved."

**I6. Gut instinct for people and directions.** [stated, primary, caption-derived, 2026 interview [1:11:48]], on choosing Stephen Wright as co-author: "well how do you know anything your gut you know your instincts tell you right there's no formula … a lot of what we do is subconscious".

**I7. Structure-first thinking.** [stated] → R5.
- 1996 survey p. 2: "understanding the characteristics of the objective function is crucial in large scale optimization."
- 2026 interview [1:16:12]: "when the problem has a structure like a nonlinearly [sic] square structure, you have to exploit it."
- NITMB 2024 [0:52:35], on Kronecker-product structure in neural-network curvature: "That's a third dimension that is exploiting structure … this is right now actually where the action is."
- 2026 [1:25:40], on why neural-network training works: "it's not just any nonlinear function of a million variables it's a structured function and there are symmetries there".

**I8. Change the problem, not only the algorithm.** [stated, primary, caption-derived, 2026 interview [1:43:00]]. A late lesson, 2026:
> "if you say I'm going to improve the training process, you can do it by different two different things. One of them is change the architecture so it's easier to optimize and the other one is just find a better optimization algorithm."

He cites residual connections as the example and says it "took me also too long to understand".

---

## 4. Experiments and execution

**E1. Code and test until the evidence is overwhelming.** [stated, primary, caption-derived, 2026 [0:50:32]], on L-BFGS: "I spent some months there coding it, testing it, make sure that it really was better. And the more I tested it, the more I realized this is it. This is the way to do it."

**E2. Experiments before "philosophizing" or theory, in a new setting.** [stated, primary, caption-derived, UCLA 2021 [0:24:59]]: "why don't we do some experiments before we do more philosophizing or before we do any theory so how about if we do some experiments". The same talk also says "we cannot proceed sorry heuristically we need a theoretical foundation" [0:42:55]. The order is experiments first, then theory. (See C1.)

**E3. Benchmark methods, not codes, and never publish a ranking.** [stated, primary, co-authored with Morales, Waltz, Liu and Goux, 2003, author's PDF p. 2]:
> "we warn the reader against using our results to rank the codes. Not only is such a ranking dubious given that it is based on a particular set of problems, but even within this testing environment relative performance of the codes can change at any time. Second, our goal is to assess the effectiveness of optimization methods … and not simply to evaluate the performance of specific software implementations."

They separate problems into unconstrained, equality-constrained and general classes "to focus on algorithmic features". Their verdict is two-sided: interior methods "appear to be strong competitors of active-set SQP methods, but all codes show much room for improvement" (abstract). Paper: *Lecture Notes in Computational Science and Engineering* 30:167–183, Springer 2003, DOI 10.1007/978-3-642-55508-4_10.

**E4. Compare against the obvious simple baseline.** [stated] → R4.
- Simons 2017 [0:19:18–0:19:51]: "rarely in the literature of derivative-free optimization do people say, 'Well, let me compare with finite difference Quasi-Newton updating.' It's almost never done, right? So otherwise we would have detected throughout the years how the two things work." He adds that "nothing of this, of what I said here, is new."
- Co-authored abstract (Shi, Xuan, Oztoprak, Nocedal, arXiv:2102.09762, 2021; journal version *Optimization Methods and Software* 38(2):289–311, DOI 10.1080/10556788.2022.2121832): "The use of finite differences has been largely dismissed in the derivative-free optimization literature as too expensive in terms of function evaluations and/or as impractical when the objective function contains noise. The test results presented in this paper suggest that such views should be re-examined".
- UCLA 2021 [0:40:36]: "this state-of-the-art code is not faster than finite difference lbfgf [sic: L-BFGS] when there is no noise … nothing is universal but it was surprising we thought it was going to be a struggle".

**E5. Build in adaptivity and recovery; expect the algorithm to be wrong.** [stated] → R8.
- Simons 2017 [0:02:18]: "we're gonna have to be adaptive. We cannot make definitive decisions of what the noise is or what the finite difference intervals are. The algorithm are gonna have to find out when they make a mistake, go back and correct what they are doing."
- UCLA 2021 [0:27:46]: "a method like this has to have a corrective procedure whenever the line search fails".
- Earlier, as an analytic theme (Acta 1992, p. 16): "the BFGS method has interesting self-correcting properties, which account for its robustness."

**E6. Distrust low-dimensional pictures.** [stated, primary, caption-derived]
- Purdue 2017 [0:39:16], his own picture of sharp versus wide minimizers: "my geometrical interpretation. It's gonna be really good, but probably wrong. … Because everything in 2 and 3D is not what happens in reality."
- NITMB 2024 [0:12:56]: "this is too high dimensional to be seen. Right? So are these pictures just fooling you or not? Well the only thing I can say is that these are pictures". (2 repetitions.)

**E7. Rewrite code from scratch when it becomes unmaintainable, and commercialise when academia cannot sustain it.** [stated, primary, caption-derived, 2026 [1:18:55–1:19:29]]. The account: student Richard Waltz "told me this code is complete spaghetti now … Can I just write it from scratch? So he did", and "to continue to make it into a good code it had to become commercial. It couldn't stay in academia because we couldn't know who to fund it [sic: how to fund it]". Context from the CV: Ziena Optimization co-founded in 2001; later sold to Artelys.

**E8. Test on real engineering or industrial problems and accept "no" to your own method.** [stated, primary, caption-derived, 2026]
- Weather [1:16:12–1:16:44]: he told ECMWF not to use L-BFGS but a multilevel Gauss–Newton method with a spectral preconditioner, and "the best way to convince them is by getting better numbers with something else".
- Google speech recognition, around 2008 [1:22:16]: "How can we use LBFGS here? And my first thing is don't use LBFGS here".

---

## 5. Judging results: when to believe, when to stop, negative results

**J1. Confidence comes from exhausting the alternatives.** [stated] → R3.
- 2026 [0:52:12]: "I was sure that it was right because I tried everything else … I knew that it was right because I tried everything else". He cites Churchill's quip about the United States doing "the right thing after trying all the alternatives".
- Simons 2017 [0:02:18]: "after trying everything else, I see that the only way I know how to do that is going back to Quasi-Newton methods."
- UCLA 2021 [0:31:40–0:32:16]: "we tried to do regression-based quasi-newton algorithms and we worked on that for quite a while and we could never get to develop an algorithm that would scale up … going back to bfgs is the result of having tried everything we could someone maybe more clever and may be able to find a whole family … that is better than what we're doing here".

**J2. Hold your ground against unfavourable reviews and eminent doubters when the evidence is yours.** [stated, primary, caption-derived, 2026 [0:50:32–0:53:21]]. The L-BFGS paper got reviews that "were not so good", and editor Jorge Moré "made sure that it got published". Powell "didn't like it for reasons that are a little bit technical. … It didn't bother me because I told you I've tried everything else."

**J3. An algorithm never observed to fail still needs proof. Open questions stay open.** [stated, primary]. See I5. In 1992 (pp. 21–22) he calls the nonconvex BFGS convergence question "one of the most fundamental questions"; he keeps unresolved questions as numbered "Open Questions" instead of smoothing them over.

**J4. Negative theoretical results as a way to understand.** [stated, primary, Acta 1992, p. 2]: "We will see that the weaknesses of several classical algorithms that have fallen out of grace, such as the Fletcher-Reeves conjugate gradient method and the Davidon-Fletcher-Powell variable metric method, are fairly well understood." The 2026 interview describes the Byrd–Nocedal–Yuan analysis the same way [0:57:49]: the proof showed the Broyden-class methods "were all good … but excluding DFP. By the time you got a DFP, some self-correcting property was not there", and "out of this comes a real understanding of how things are." Paper, identifier checked: Byrd, Nocedal, Yuan, "Global convergence of a class of quasi-Newton methods on convex problems", *SIAM J. Numer. Anal.* 24(5):1171–1190, 1987, DOI 10.1137/0724077. Crossref's title field misspells "Class" as "Cass". The paper was not read.

**J5. Failure and knowledge-building look alike from inside. Tolerate the fog.** [stated, primary, caption-derived, 2026 [0:52:12]]:
> "I used to tell over over the years to my students that failures like this and building up knowledge are difficult to distinguish sometimes and you just have to live with that fog of uncertainty for a while".

The 2021 magazine quote uses the same image: "out of the fog, you get some clarity". It is also in the 2026 interview. [inferred] "Fog" is a recurring metaphor (2 sources).

**J6. Some success in nonlinear interior methods is luck; say so.** [stated, primary, caption-derived, 2026 [1:30:07]]: "there is some luck actually involved nonlinear interior point methods and how you move the barrier parameter. there is no complete theory uh behind it." In the 2006 Knitro paper (co-authored, p. 5) the barrier-update question is left open: "Since it is not known at present which one is the most effective in practice, Knitro allows the user to experiment with the barrier update strategies".

**J7. Contested empirical claims: stated confidence, acknowledged dissent.** [stated, primary, caption-derived]
- Purdue, Feb 2017, before the ICLR presentation of Keskar, Mudigere, Nocedal, Smelyanskiy, Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima" (ICLR 2017, arXiv:1609.04836) [0:31:35]: "I don't know how bad the attacks are gonna be from left and right. I'm sure there are gonna be people saying, I don't believe this."
- NITMB, Oct 2024 [0:58:22]: "the white [sic: wide] minimizing the sharp minimizer that became controversial because in our paper we said if you allow noise a significant amount of noise you're going to get to the white [sic] minimizer and people have not agreed with that". He still holds that "to what degree is noise useful? I think it is … We never got good generalization results by suppressing the noise too much."

(Recorded as a stated position under dispute; agent 05 should collect the critiques.)

**J8. Honest empirical verdicts on others' theoretical fixes.** [stated, primary, 1996 survey, pp. 19–20]. On globally convergent Polak–Ribière variants: "numerical results appear to indicate that only a marginal improvement over the standard implementation of the Polak-Ribière method is obtained", and "Numerical experiments again fail to show a significant improvement in performance".

---

## 6. Writing, teaching and talks

**W1. Book purpose: "what are the algorithms that work", plus foundations.** [stated, primary, caption-derived, 2026 [1:09:33]]:
> "Our book was numerical optimization. The motivation always was what are the algorithms that work? tell people how they how what they do and give some u foundations for them and our book is very popular among engineers … people who are teaching more mathematical courses they don't know how to use our book. It doesn't have enough proofs".

The homepage book page (text from the book's promotional description, 2nd edition 2006; joint with S. J. Wright) says the book focuses "on the methods that are best suited to practical problems" and that "The authors have strived to produce a text that is pleasant to read, informative, and rigorous---one that reveals both the beautiful nature of the discipline and its practical side." Book: Nocedal & Wright, *Numerical Optimization*, Springer, 1st ed. 1999 (DOI 10.1007/b98874), 2nd ed. 2006 (DOI 10.1007/978-0-387-40065-5). The book's own preface was **not read**: Springer's front-matter link returned a client challenge (curl) or a cookie-authorisation redirect (WebFetch).

**W2. Writing a book to learn the subject.** [stated, primary, caption-derived, 2026 [1:07:53]]: "the reason why I wanted to buy [sic: write] a book is just because I wanted to learn the subject well this is true that was the only reason". On the co-writing process [1:10:40]: Wright is "very fast and I'm very slow"; Nocedal would tear drafts apart, and "my plan was always sketchy". The third edition is under way as of March 2026 [1:45:19].

**W3. Teaching: summarise cogently and reorder the story.** [stated, primary, caption-derived, 2026 [1:30:40]]: "it's a very interesting exercise to try to summarize ideas to try to be cogent. This it's it's a difficult exercise. So in the mornings before class trying to change the order in which you're going to say things." And: "I always feel like creating new courses. Don't stay with the same course."

**W4. Survey writing: cite codes, not just algorithms; state open questions.** [stated, primary, Acta 1992, p. 2]: "I include references to particular codes in subroutine libraries instead of simply referring to mathematical algorithms." [practice, same text] The survey lists numbered Open Questions I and II (pp. 17, 21–22).

**W5. Talks to the young are worth it: humility.** [stated, primary, caption-derived, 2026 [1:06:43]]: "if I'm giving a talk 20 people if there's only one who will get influenced by this talk That person may become brilliant … They may be become much more important scientists than you. Right? So this is a lesson in humility". The 2017 speech credits a plenary invitation from Goldfarb, when "I had hardly been invited to give any lectures at all", as "decisive" because it connected him with Powell.

**W6. Publishing: few, complete papers; against the conference model and metric-chasing.** [stated, primary, caption-derived, 2026 only; single source → not a ≥3 belief]
- [1:36:48]: the computer-science conference model is "a totally broken system. It's almost random", and there is "no reason why that mode has to be imitated" in mathematical programming.
- [1:38:30]: "Writing more papers is just going to get in the way of writing innovative work."
- [1:38:30–1:39:03], on Google Scholar: "we all know that things are cannot be mapped into one dimension into one number … it's my opinion that we have to fight it."
- [1:39:37–1:40:12], on his own rate: "Two to three papers a year, less than three per year because I would not publish papers that I thought were not complete uh were not satisfactory … have a little courage. Don't just follow the system."
- He also doubts growing author lists: "more papers and more authors not clear that's a good idea who did exe exactly why."
- [practice, to be checked by agent 01/03] The papers-per-year figure is his and the interviewer's estimate.

**W7. Curriculum should be "living".** [stated, primary, caption-derived, 2026 [1:33:25]]: "our curriculum should be a living curriculum should be changing … some topics have to be relegated". Applied to the simplex method: only "a small number" of people need to know it well, and room must be made for AI and machine learning. (Era: 2026.)

---

## 7. Research organisation: collaboration, mentoring, long-term agenda

**O1. Long-term core partnership.** [stated, primary]. Richard Byrd is "my constant friend and colleague" (2017 speech). In 2026 [0:41:33–0:43:16] he describes Byrd's "mathematical abilities and insight is extraordinary", and says Byrd did not get the credit he deserved partly because "if he's proven a theorem, he doesn't feel any need to write it down". [observed by Nocedal of a collaborator]

**O2. Be physically present: networks create opportunities.** [stated, primary, caption-derived, 2026 [1:46:25]]. His closing advice follows his remark "I find all these speeches that people give not useful":
> "if you're not there it will not happen. So go to places, meet people, go to books, be exposed … You have to create your your opportunities … So be curious and go."

He contrasts this with his own isolation in Mexico (1978–81): "I had been disconnected … I had to reconnect myself" [1:03:23], and "my research was not going very well. It's very difficult. uh the environment is you know the environment sometimes help you sometimes does not" [0:53:54].

**O3. Senior people should back the young.** [stated, primary]. He credits Powell and Goldfarb for opportunities "when it was not easy because I was coming from Mexico" (2026 [1:02:18–1:03:23]). A note from Powell ("This is the best paper I read all year") is described as "very important for a young person". The same point is in the 2017 speech.

**O4. Workshops over congresses for deep, adversarial discussion.** [stated, primary, caption-derived, 2026 [1:41:15–1:42:27]]. The US–Mexico workshops allowed people to "sit down and discuss with someone really taking different positions something in depth". He adds a sharp judgment: people who never attended "went on to do things methods that we were very critical of. If they had attended, we probably could have convinced them not to go this way. And they got lot of citations, but it's was the wrong thing to do." (Unnamed; see Gaps.)

**O5. Big discoveries versus teams.** [stated, primary, caption-derived, 2026 [1:14:34–1:15:39]]. The weather project "was a typical team effort", but:
> "People sometimes say you know the big discoveries in science are done by a multid-disciplinary group of people with complimentary expertises. I don't believe that the big discoveries in science are usually done by one or two people quietly in a corner nobody paying attention and then when the big ideas come there's a team that goes and develop this"

The ASR has no punctuation. The context (Hinton and LeCun "were doing the quiet revolutionary work", followed by company teams) shows the intended reading is "I don't believe that. The big discoveries … are usually done by one or two people quietly in a corner". [inferred reading of ASR punctuation] (See C3.)

**O6. Students and humility.** [stated]. See W5. Also: "I really enjoy teaching students even if they're weak. I have patience" (2026 [1:30:40]). He describes students as co-searchers for "the most beautiful solution" (2021, secondary).

**O7. Institution-building: move departments toward machine learning early.** [observed/secondary paraphrase, McCormick Magazine 2021]: as IEMS chair (2013–16) "he championed the idea that certain models and ways of thinking had run their course, and that industrial engineering had to move forward to embrace data-driven models and machine learning". Direct quote: "We were one of the first industrial engineering departments to foresee that machine learning would become a major direction for industrial engineers". The colleague observation (Zhaoran Wang, same article) is [observed]: "Jorge is open minded about emerging, challenging problems, such as deep learning, when most researchers are hesitating about whether to get into this field".

**O8. Current agenda (2026).** [stated, primary, caption-derived, 2026 [1:45:19]]: "I'm taking a pause from writing research papers", to finish the third edition; interested in generative AI, including its effect on education ("organizing groups to discuss those questions"). In 2024 (NITMB Q&A) he wanted "to continue investigating the solution of very large and very nonlinear optimization problems, this time with applications in biology". In the NITMB 2024 talk [0:02:18; 0:55:24] he gives an access motive for training efficiency: "to open up the field for people who don't have enormous computational resources", and "doing uh neural network for the masses is really important".

---

## 8. Era and resource context of the stated practices

| Period | Context he describes | Source |
|---|---|---|
| ~1970–74 (UNAM, physics) | Taught himself Fortran from a book on a PDP. Punch cards, waits of about half an hour ("forced to socialize"). First exposure to optimization through a telescope-design program from Kodak | 2026 interview [0:32:40–0:34:49] |
| 1974–78 (Rice / Stanford) | Very small department. Thesis done "pretty much on my own". Took Dantzig's courses. Goal: quasi-Newton methods for "millions of variables", then out of reach | 2026 [0:37:38–0:47:44] |
| 1978–81 (UNAM faculty) | Isolated ("disconnected"); L-BFGS written and tested alone; later "my research was not going very well" | 2026 [0:49:37–0:54:28] |
| 1983–2012 (Northwestern EECS) | NSF and DOE grants (acknowledged in the 1992/1996 papers); Harwell subroutine library as the standard of practice; decades-long partnership with Byrd; students write codes (KNITRO: Hribar, then Waltz) | Acta 1992; 1996 survey; 2026 [1:17:49–1:19:29] |
| 1990s (ECMWF weather project) | About 1 million variables, forecasts due every few hours, team of "hundred people or something"; several trips a year to France and England | 2026 [1:12:21–1:15:07] |
| 2001– (Ziena / Artelys) | Commercialisation of KNITRO to fund continued development | CV; 2026 [1:19:29–1:20:00] |
| ~2008–2014 (Google) | Consulting on speech recognition; contact with Hinton's group | CV; 2026 [1:21:43–1:24:31] |
| 2016–2024 (machine learning) | Students and colleagues in tech companies; energy cost of training ("comparable to … Argentina", NITMB 2024 [0:01:43]) | NITMB 2024 talk |

[inferred] His strongest methodological claims (theory judged by practice, test against simple baselines, exhaust alternatives) were formed in a small-group, CPU-bound, numerical-analysis culture. The 2026 regrets (the statistical side of learning, architectures) are about a field where "theory has followed experimentation all the time" (NITMB 2024 [0:06:47]). A skill built from this file should flag the difference.

---

## 9. Failures, abandoned directions, rejections and regrets (as he states them)

- **F1. PhD thesis as a collection of failures** [stated, primary, caption-derived, 2026 [0:46:37–0:47:44]]: "if you read them there all of them are a failure. None of them are elegant … It was a impressive collection of failed ideas." Reframed later [0:51:38]: "my PhD dissertation was not a failure but had been the stepping stone". One of its papers "with the wrong ideas made it into math programming by accident". (Not identified. The title was not found in this run.)
- **F2. L-BFGS initially "didn't register very much"**, got poor reviews and was disliked by Powell at first (2026 [0:50:32–0:53:21]). LeCun, he reports, tried L-BFGS for neural networks in 1987 and found "it didn't work well and that the stoastic [sic] grain [sic: gradient] method is what worked" (2026 [1:04:28]). [stated, reporting another's result]
- **F3. Reduced-Hessian methods with Overton (1981–83)** "are not the best thing now they're not considered the best thing" (2026 [0:55:34]). [stated]
- **F4. Regression-based quasi-Newton for noisy functions**: "we worked on that for quite a while and we could never get to develop an algorithm that would scale up" (UCLA 2021 [0:31:40]). [stated]
- **F5. Machine-learning regret**: "I never understood that there had to be a balance between the statistical aspect of the problem and the geometry of the problem. And as a deterministic optimizer, we always work on how to learn the geometry … I didn't see it early enough. And so machine learning people developed methods like Adam and so on … but they're not satisfactory" (2026 [1:26:13–1:27:20]). [stated]
- **F6. Architecture regret**: see I8 and P7 (2026). [stated]
- **F7. Large-batch / sharp-minima claim disputed by others**, and he acknowledges this (2024). See J7. [stated]
- **F8. Collective failures he reports in the field**: in 1996 (p. 19), "So far all attempts to derive an efficient method of the form (5.5) have been unsuccessful". In 1992, conjugate-gradient methods are "perhaps the least understood methods of optimization" (p. 10). [stated]
- **Not found**: any statement by him about a retracted claim, a withdrawn paper, or a direction he formally abandoned (beyond F3–F4). → Gap.

---

## Contradictions (kept, not reconciled)

- **C1. Theory-first or experiment-first?**
  - Theory side, in 2026 (Powell school: "I'm not going to design algorithms heristically [sic]"; Knitro: "the theory was guiding at the side [sic] of the algorithm") and in UCLA 2021 [0:42:55] ("we cannot proceed … heuristically we need a theoretical foundation").
  - Experiment side, in UCLA 2021 [0:24:59] ("why don't we do some experiments before we do more philosophizing or before we do any theory") and in 2026 on L-BFGS (months of coding and testing gave the confidence, not a proof).
  - The 2017 speech defers: "The right balance is not for us to decide but is driven by the topic."
- **C2. Does theory produce new methods?**
  - 1992: "our many theoretical studies of variable metric methods have not resulted in the discovery of new methods".
  - 1996: conjugate-gradient convergence studies "have not lead [sic] to significant practical advances".
  - 2026, on Knitro: "we started by developing a theory and that tells exactly how to scale everything … the theory was guiding at the side [sic: the design?] of the algorithm" [1:17:49].
  - Also 1992, p. 10: a comprehensive conjugate-gradient theory "could result in the discovery of a superior conjugate gradient method".
- **C3. Teams or lone discoverers?**
  - 2021 (secondary quote): "you feel there was a team of people who did it"; weather "was a typical team effort" (2026).
  - Same 2026 passage: he does not believe the multidisciplinary-team account of big discoveries, which are "usually done by one or two people quietly in a corner" (reading of the ASR punctuation inferred).
- **C4. Complexity and global-efficiency theory: called for early, criticised late.**
  - 1992 (Acta p. 2): "Global efficiency is an area that requires more attention and where important new results can be expected."
  - 2019–2026: worst-case complexity is "not very helpful" (2021), "very good from a point of view of complexity … really bad" computationally (2019), and complexity results are "not distinguishing between good methods and bad methods" (2026).
- **C5. Stochastic gradient: optimizer's skepticism, then admission of a blind spot.**
  - 2017–2018: SGD cannot be "the final solution" (2017, secondary); "We argue, however, that this is far from settled" (2018, co-authored).
  - 2026: he regrets not seeing "the statistical aspect", and says machine-learning methods such as Adam handled it, "but they're not satisfactory".
  - Both positions coexist in 2026.
- **C6. Tone about prizes and advice (minor).**
  - 2024: "I am very excited to receive such a prestigious award."
  - 2026 [1:24:31]: "prices [sic: prizes] are not important … never going to be just right". Also 2026: "I find all these speeches that people give not useful", immediately followed by advice (O2).

---

## Gaps (searched or attempted, not found, or not read)

1. **Preface of *Numerical Optimization* (1999, 2006)**: not read. Springer front matter was blocked by a client challenge (curl) or a cookie-authorisation redirect (WebFetch). Only the homepage book blurb was used.
2. **2024 SIAM John von Neumann Prize Lecture (Spokane, 9 July 2024)**: no recording or text found in one targeted search (WebSearch 1 of 2) or in a YouTube search. The title of the lecture is not known.
3. **2012 Dantzig Prize ceremony video** (YouTube uB7CNa9Qw3k, 5 min, linked from his homepage): no captions; not watched.
4. **IPAM tutorial "Optimization Methods for Machine Learning" (2015, parts 1–3)**: no captions available; not read.
5. **DOE ASCR Discovery "genealogy" article** (linked from his homepage): host not resolvable, and the replacement domain was blocked by the egress proxy. Not read.
6. **EECS "Meet the faculty" lecture video** (linked from homepage): not checked. Spanish-language talks (CIMAT, UAM-I) were not transcribed; they may hold stated views for a Mexican audience.
7. **1998 ICM invited lecture** (listed in CV): text not located; title not verified; not read.
8. **Advice to PhD students, lab guide, stopping rule**: no written document found. The only student advice comes from the 2026 interview (J5, O2, W6).
9. **Writing craft** (paper structure, figures, how to write a result): no stated guidance found beyond the teaching remarks (W3) and the book goals (W1).
10. **Who he meant in O4** ("methods that we were very critical of") and **which thesis paper "made it into math programming by accident"** (F1): not identified. They are left unnamed rather than guessed.
11. **The Knitro theory paper that Powell reviewed "almost a year"** (2026 [1:18:21]): the interview does not name it. Candidates exist in his publication list (Byrd–Hribar–Nocedal 1999; Byrd–Gilbert–Nocedal 2000), but the attribution is **not** made here.
12. All caption-derived quotes are unverified against audio. The ASR errors are visible (for example "Horge", "Danik", "heristically").

---

## Sources

Primary = his own words (texts he wrote or co-wrote, his talks, his written Q&A answers). Secondary = reported by others (news items quoting him, press releases).

1. Nocedal homepage (index, research, software, students, courses, misc, book pages), Northwestern. Undated, footer "Last modified 2008", content to about 2021. http://users.iems.northwestern.edu/~nocedal/ (redirect from http://www.ece.northwestern.edu/~nocedal/). **Primary.**
2. J. Nocedal, "Acceptance Speech, 2017 Von Neumann Theory Prize" (1 p. PDF), Oct 2017. http://users.iems.northwestern.edu/~nocedal/PDFfiles/VonNeumann_Speech.pdf. **Primary.**
3. J. Nocedal, *Curriculum Vitae* (bio-brief.pdf, cv_nocedal.pdf, nsf-bio.pdf), homepage, undated (lists honours to 2021). **Primary (context only).**
4. J. Nocedal, "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1 (1992) 199–242, DOI 10.1017/S0962492900002270 (author's PDF from homepage). **Primary.**
5. J. Nocedal, "Large scale unconstrained optimization", Northwestern report dated 23 June 1996; published in *The State of the Art in Numerical Analysis* (eds. A. Watson, I. Duff), Oxford University Press, 1997, pp. 311–338. Venue checked on the homepage publication list; author's PDF read. **Primary.**
6. J. L. Morales, J. Nocedal, R. A. Waltz, G. Liu, J.-P. Goux, "Assessing the potential of interior methods for nonlinear optimization", *LNCSE* 30 (2003) 167–183, DOI 10.1007/978-3-642-55508-4_10 (author's PDF). **Primary, co-authored.**
7. R. H. Byrd, J. Nocedal, R. A. Waltz, "Knitro: An integrated package for nonlinear optimization", in *Large-Scale Nonlinear Optimization*, Springer 2006, pp. 35–59, DOI 10.1007/0-387-30065-1_4 (author's PDF dated 6 July 2005). **Primary, co-authored.**
8. L. Bottou, F. E. Curtis, J. Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Review* 60(2) (2018) 223–311, DOI 10.1137/16M1080173, arXiv:1606.04838 (PDF from homepage). **Primary, co-authored.**
9. H.-J. M. Shi, M. Q. Xuan, F. Oztoprak, J. Nocedal, "On the numerical performance of finite-difference-based methods for derivative-free optimization", arXiv:2102.09762 (2021); *Optimization Methods and Software* 38(2) (2023) 289–311, DOI 10.1080/10556788.2022.2121832. Abstract read. **Primary, co-authored.**
10. N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. T. P. Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", ICLR 2017, arXiv:1609.04836. Abstract read. **Primary, co-authored.**
11. "Subject to: Jorge Nocedal", long-form interview, YouTube channel *Subject to*, uploaded 18 Mar 2026. https://www.youtube.com/watch?v=CfR-llfmb6E. Transcript: `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt` (ASR). **Primary.**
12. J. Nocedal, "How is it Possible to Train Deep Neural Networks?", NITMB Seminar Series, recorded 25 Oct 2024. https://www.youtube.com/watch?v=XrX7MEMbdYw. Transcript: `../sources/talks/2024-10-25_nitmb-seminar-train-dnns_XrX7MEMbdYw.txt` (ASR). **Primary.**
13. J. Nocedal, UCLA CS201 seminar, 8 Apr 2021. https://www.youtube.com/watch?v=4a12aV77CAI. Transcript: `../sources/talks/2021-04-08_ucla-cs201-seminar_4a12aV77CAI.txt` (ASR). **Primary.**
14. J. Nocedal, RIIAA 2.0 keynote, Mexico City, Aug 2019. https://www.youtube.com/watch?v=3zUD3H71HQ0. Transcript: `../sources/talks/2019-08_riiaa2-keynote_3zUD3H71HQ0.txt` (ASR). **Primary.**
15. J. Nocedal, "Zero-order and Dynamic Sampling Methods for Nonlinear Optimization", Simons Institute, uploaded 3 Oct 2017. https://www.youtube.com/watch?v=OfVZ9gArXiY. Transcript: `../sources/talks/2017_simons-zero-order-dynamic-sampling_OfVZ9gArXiY.txt` (uploader subtitles). **Primary.**
16. J. Nocedal, "Nonlinear Optimization Methods for Machine Learning", Purdue IE Distinguished Seminar, 15 Feb 2017. https://www.youtube.com/watch?v=srg3Rx2HvfQ. Transcript: `../sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt` (uploader subtitles). **Primary.**
17. SIAM clip, "Jorge Nocedal on Machine Learning for Recommendation systems, medical diagnosis, speech recognition" (SIAM Annual Meeting 2014), uploaded 24 Oct 2014. https://www.youtube.com/watch?v=mgiUoSKrgbI. Transcript: `../sources/talks/2014_siam-an14-ml-clip_mgiUoSKrgbI.txt` (ASR; narrator and speaker mixed). **Primary/secondary mix.**
18. NITMB, "Solving complex machine learning optimization problems: A conversation with Jorge Nocedal", 24 Oct 2024. https://www.nitmb.org/post/solving-complex-machine-learning-optimization-problems-a-conversation-with-jorge-nocedal. **Primary (his written answers).**
19. S. Langen, "The Optimizer", *McCormick Magazine*, Spring 2021. https://www.mccormick.northwestern.edu/magazine/spring-2021/pdf/the-optimizer.pdf. **Secondary (direct quotes, plus colleague observation).**
20. A. Morris, "Nocedal Receives John von Neumann Theory Prize", Northwestern Engineering News, 26 Oct 2017. https://www.mccormick.northwestern.edu/news/articles/2017/10/nocedal-receives-john-von-neumann-theory-prize.html. **Secondary (direct quote).**
21. D. P. Smith, "The Future of Artificial Intelligence", Northwestern Engineering News, 19 May 2017. https://mccormick.northwestern.edu/news/articles/2017/05/the-future-of-artificial-intelligence.html. **Secondary (direct quote).**
22. SIAM press release, "Jorge Nocedal is the 2024 SIAM John von Neumann Prize Lecturer", GlobeNewswire, 2 Apr 2024. https://www.globenewswire.com/news-release/2024/04/02/2856361/0/en/Jorge-Nocedal-is-the-2024-SIAM-John-von-Neumann-Prize-Lecturer.html. Text verified on the Yahoo Finance mirror https://finance.yahoo.com/news/jorge-nocedal-2024-siam-john-170000743.html. **Secondary (direct quotes).**
23. J. Nocedal, IEMS 490 "Introduction to Machine Learning" syllabus (homepage, undated, around 2014). http://users.iems.northwestern.edu/~nocedal/syllabusML.pdf. **Primary (teaching context; little methodological content).**

Cited by identifier only (checked on Crossref; **not read** in this run):
- J. Nocedal, "Updating quasi-Newton matrices with limited storage", *Math. Comp.* 35(151) (1980) 773–782, DOI 10.1090/S0025-5718-1980-0572855-7.
- R. H. Byrd, J. Nocedal, Y.-X. Yuan, "Global convergence of a class of quasi-Newton methods on convex problems", *SIAM J. Numer. Anal.* 24(5) (1987) 1171–1190, DOI 10.1137/0724077.
- W. C. Davidon, "Variable metric method for minimization", *SIAM J. Optim.* 1(1) (1991) 1–17, DOI 10.1137/0801001 (the first SIOPT paper, which he mentions in 2026).
- M. Fisher, J. Nocedal, Y. Trémolet, S. J. Wright, "Data assimilation in weather forecasting: a case study in PDE-constrained optimization", *Optim. Eng.* 10(3) (2009) 409–426, DOI 10.1007/s11081-008-9051-5.
- J. Nocedal, S. J. Wright, *Numerical Optimization*, Springer, 1999 (DOI 10.1007/b98874) and 2nd ed. 2006 (DOI 10.1007/978-0-387-40065-5).
