# Jorge Nocedal: Students and Collaborators (research agent 04)

- **Researcher**: Jorge Nocedal (Walter P. Murphy Professor, IEMS, Northwestern University; PhD Rice 1978, advisor Richard A. Tapia)
- **Dimension**: mentorship. This covers supervision style, group habits, lab culture, tacit knowledge, the lineage he came from, and how his collaborators work with his students.
- **Research date**: 2026-09-28
- **Sources consulted**: 28 (21 primary, 7 secondary). Details are under Sources. Failed or blocked lookups are under Gaps.
- **Local corpus**: `references/sources/papers/`, `essays/` and `software/` hold only `.gitkeep`. **No user-supplied material exists**, so nothing here is marked "from user-supplied material". The transcripts in `references/sources/talks/` were saved earlier in this run by research agent 02. They are YouTube automatic captions (ASR), not human-checked. I quote them verbatim with the block timestamp `[h:mm:ss]` and mark them "caption-derived". ASR errors stay as they appear, with the intended word in square brackets where needed (e.g. "Richard Bird" [Byrd], "Nitro" [KNITRO]).
- **Tags**:
  - [stated]: what Nocedal says.
  - [practice]: what the record shows he and his group did (papers, theses, CVs, code).
  - [observed]: what students, colleagues or committees say about him.
  - [inferred]: my reading, not confirmed by any source.
  - Every item is also marked primary or secondary.
- **Division of labour with the other notes.** His *stated* research advice is catalogued in `02-methodology.md`; the publication landscape and author-order analysis are in `01-publications.md`. This note cross-references them rather than repeating them. What it adds:
  - what the student/collaborator record shows;
  - what the one student-written text I could read (Curtis's 2007 thesis) says;
  - the lineage he describes for himself.

---

## 0. Bottom line (what a user of this skill should take from this note)

1. **The evidence is thin on the student side.**
   - Only one first-hand student text was found and read: Frank E. Curtis's 2007 PhD thesis (acknowledgements and experimental chapters).
   - No student blog, memorial, lab guide, Festschrift or group-meeting description was found.
   - Most of what follows is therefore (a) Nocedal's own account, and (b) patterns in the publication, thesis and CV record. It is not first-hand student testimony.
2. **The supervision unit is a triad: Byrd, Nocedal and a student.**
   - 15 of the 22 students who co-author with Nocedal in DBLP have at least one paper that also includes Richard H. Byrd (University of Colorado Boulder).
   - Curtis's thesis says its scientific accomplishments "would not have been possible without the knowledge and expertise of Richard Byrd" [practice + observed, primary].
   - After 2022 no student paper includes Byrd.
3. **The group runs on shared code and shared people.**
   - Students write or inherit the group's solver. Mary Beth Hribar coded the first NITRO/KNITRO algorithm; Richard Waltz rewrote it from scratch.
   - Later students test their algorithms inside KNITRO, with source code and technical support from former students (Waltz, Plantenga).
   - Former students sit on later students' committees: Waltz on Curtis's, Curtis on Xuan's.
4. **From about 2010, students work alongside industry.** There are internships at Intel, Facebook and ExxonMobil, and industry co-authors (Google, Intel, IBM). Student funding comes partly from industry grants (Intel) and partly from a single DOE grant renewed since 1987. [practice, primary]
5. **Stated ethos** [stated, primary, mostly caption-derived]:
   - live with the "fog of uncertainty";
   - publish fewer, complete papers;
   - "if you're not there, it won't happen. So be there";
   - patience with weak students;
   - humility toward the young;
   - aim for "the most beautiful solution".
6. **Where he came from.** His own PhD supervision was hands-off: "I did it pretty much on my own". His real models were a fellow student (Byrd), Dantzig's seminar, and Powell and Goldfarb as senior backers. His own record shows the opposite of hands-off: he co-authors essentially every student's papers. This contrast is [inferred]; he never draws it himself.

---

## 1. Lineage: how Nocedal himself was mentored (layer 7; shapes how he supervises)

| # | Item | Evidence | Tag |
|---|------|----------|-----|
| L1 | **Changed advisor after 6 months over taste.** His first advisor at Rice (an aeronautics professor; the ASR garbles the name) dismissed a Powell paper Nocedal brought him. | 2026 interview [0:38:12]: "I received a paper that Mike Powell had written and I brought it to him and I told him this is really interesting and he told me this is not interesting at all. Right. And then I realized we don't have common common interests." | [stated, primary, caption-derived] |
| L2 | **Nominal advisor, self-directed thesis.** Richard Tapia supervised lightly: he took Nocedal along to Stanford for a sabbatical year and signed the thesis. | 2026 [0:40:58]: "he did read my thesis and signed it but I did it pretty much on my own." Also [0:40:25]: "Richard Tapia was very kind person, very charismatic. I really didn't work much with him". | [stated, primary, caption-derived] |
| L3 | **Tapia's one recorded intervention with Byrd.** Tapia made Byrd stop talking to everyone and finish. | 2026 [0:42:09–0:42:43]: "Richard Tapia was his advisor. He told him, "Richard, I prohibit you now from talking to any of the other students. [laughter] Close the door and you're going to finish your thesis."" MGP confirms Byrd as a Tapia student (Rice 1976) [practice, secondary]. | [observed by Nocedal, primary, caption-derived] |
| L4 | **The real mentor was a peer.** Byrd was a fellow graduate student and "role model", and the discussions were informal and went on for years. | 2026 [0:41:33–0:42:09]: "he was a role model … there was this student there Richard Bird [Byrd] that everybody regarded him as the Einstein of the department because he knew everything about everything … after school we would discuss math in the bar or in the beach. We would be discussing about this all the time and we did this for years and years." | [stated, primary, caption-derived] |
| L5 | **Dantzig's reading seminar was a model of "how you develop research".** What mattered was the courage, not the lectures. | 2026 [0:44:56–0:45:29]: "he would talk about what what he did and why he got into certain topics and I realized at that time professor Danik [Dantzig] is not the best mathematician here by far but he is the most courageous." … "That was a very good example of how how you develop research." He also says he stopped attending Dantzig's LP course [0:46:03]. | [stated, primary, caption-derived] |
| L6 | **Senior backers made his career.** Powell gave a whole day and wrote notes on papers; Goldfarb gave him a plenary slot and introductions; Moré as editor got L-BFGS published despite poor reviews. | 2026 [1:02:50–1:03:57]: "we we spent the whole day talking about subjects … He read all my papers … he would send notes like I just read your paper with Richard Bird. This is the best paper I read all year. So those things are very important for a young person, right?" Goldfarb: "started promoting me and introducing me to people" (same block). Moré [0:50:32–0:51:06]: "the reviews were not so good but the editor of the paper was Horge Mor [Jorge Moré] from Argon. he liked it and he made sure that it got published". The paper is Nocedal, *Math. Comp.* 1980, doi:10.1090/s0025-5718-1980-0572855-7. The Goldfarb plenary is also in the 2017 speech. | [stated, primary; interview caption-derived] |
| L7 | **Thanks to the people he "learned so much" from** are to peers, not supervisors. | 2017 von Neumann speech (notes file): "Michael Overton, Steve Wright, Nick Gould, and Jong-Shi Pang from whom I learned so much". | [stated, primary] |

**Reading** [inferred]:
- His formative experiences were peer debate (Byrd), a senior who gave time and wrote notes (Powell), and a sponsor who opened doors (Goldfarb). Formal supervision (Tapia) played little part.
- In the interview he generalises the Powell/Goldfarb experience into a principle: support the young (see 02-methodology O3, W5).
- He never says he reproduces the Byrd-style peer debate with his own students. The triad structure in §3 is the closest evidence.

---

## 2. Supervision style: what he says (layer 7, with cross-links)

Everything below is [stated, primary], caption-derived where marked.

| # | Claim | Verbatim | Source |
|---|-------|----------|--------|
| S1 | Tells students that failure and knowledge-building look alike | "I used to tell over over the years to my students that failures like this and building up knowledge are difficult to distinguish sometimes and you just have to live with that fog of uncertainty for a while, right?" | 2026 interview [0:52:12–0:52:48], caption-derived. Context: his own "impressive collection of failed ideas" thesis [0:47:11]. |
| S2 | Choosing a collaborator is gut feeling, not a formula (answer to students who ask how he knew to write the book with Wright) | "Sometimes students come to me and it says how did you know sometimes young people are very naive right they come and ask you how did you know at that time to choose the right to write this book with you right >> well how do you know anything your gut you know your instincts tell you right there's no formula" | 2026 [1:11:15–1:11:48], caption-derived. The ASR inserts a speaker-change mark (">>") before "well how do you know"; that the reply is Nocedal's is probable from context, not certain. |
| S3 | Patience with weak students; teaching as a way to sharpen ideas; keeps creating new courses | "I always feel like creating new courses. Don't stay with the same course. Even last year a new course. … I really enjoy teaching students even if they're weak. I have patience and it's a very interesting exercise to try to summarize ideas to try to be cogent." | 2026 [1:30:07–1:30:40], caption-derived |
| S4 | Students carry pressures a supervisor may not see | "a young woman come to my office and after a little while she starts crying … they have a lot of pressures they uh they have a lot of difficulties there" | 2026 [1:32:19–1:32:52], caption-derived |
| S5 | Publish fewer, complete papers, and tell the young to take that risk | "Two to three papers a year, less than three per year because I would not publish papers that I thought were not complete uh were not satisfactory or so on. … At least when I argue to young people, I can show that my record I I risked it this way because I had fewer papers than others. … so have a little courage. Don't just follow the system." | 2026 [1:39:37–1:40:45], caption-derived. Also 02-methodology. |
| S6 | Distrust of rising author counts and of conference reviewing by PhD students | "the model used in computer science of publishing in conferences where more and more papers are submitted and they're reviewed by the PhD students, not by the professors. This a totally broken system." / "the number of authors is increasing more papers and more authors not clear that's a good idea who did exe exactly why." | 2026 [1:36:48–1:37:58], caption-derived. **See Contradictions C3.** |
| S7 | Go where the people are | "if you're not there it will not happen. So go to places, meet people, go to books, be exposed. … if you're not there, it won't happen. So be there." | 2026 [1:46:25–1:46:59], caption-derived (his message "for the younger generation") |
| S8 | Workshops over conferences for depth; they steer careers | "because those were workshops and not conferences there was a lot of time to discuss. … sit down and discuss with someone really taking different positions something in depth that I think was very useful for my career and very useful for other people career and young people like Andreas others say that it was also instrumental in their cases." | 2026 [1:41:20–1:42:27], caption-derived (US–Mexico Workshop on Optimization). "Andreas" is probably Andreas Griewank, named just before [inferred]. |
| S9 | Student and advisor aim at the unimprovable solution | "My students and I try to find not only the solution, but also the most beautiful solution. We aim to develop something that people can't improve upon—this is the ideal." | McCormick Magazine, Spring 2021 ("The Optimizer", Sara Langen). A quote inside a university article, so **secondary** transmission of a stated view. |
| S10 | Ideas come out of a clash of views in a group | "Insights clash, intuitions may diverge, and people may get passionate. Then suddenly, out of the fog, you get some clarity. And you feel there was a team of people who did it." | Same 2021 article, secondary transmission |
| S11 | Humility: the one listener may outgrow you | "if I'm giving a talk 20 people if there's only one who will get influenced by this talk That person may become brilliant. … They may be become much more important scientists than you." | 2026 [1:06:43–1:07:18], caption-derived (02-methodology W5) |
| S12 | The young have the advantage in a new field | "there are no experts in this incipient field. A young researcher is as likely to make a discovery as an established math or biology researcher." | NITMB Q&A (2024/25), primary written Q&A |
| S13 | "Where to place the ladder" is the choice he wants the young to face | "Richard and I spent – it seems – endless time debating where to place the ladder." … "You, young people should be prepared. I am eager to see where will you put the ladder." | 2017 von Neumann speech, primary |

---

## 3. Supervision and group habits: what the record shows (practice)

### 3.1 Roster and scale [practice, primary unless marked]

- **Size.** About 22 PhD graduates between 1987 and 2024, plus 7 M.S. students (Dong C. Liu also took an M.S. in 1986 before his PhD). That is roughly one PhD every 1.7 years. The homepage lists 2–3 current students at a time. Sources: CV (c. 2018), the old homepage "Students / People" page, `jnocedal.github.io`, and MGP (19 students, secondary).
- **Postdocs and research scientists** (old homepage): Dong C. Liu (1990–91), Ya-xiang Yuan (1998), Jean-Pierre Goux, Ciyou Zhu, José Luis Morales (1999–2007+), Dominique Orban and Xavier Jonsson (2002–03), Daniel Robinson (2010–11), Albert Berahas (2018).
- **Dissertation titles** (MGP, secondary; Curtis's and Bollapragada's also confirmed from their own CVs, primary). They track his research eras:
  - 1987–1999, quasi-Newton and trust region:
    - Liu 1987 "Optimization Algorithms Based on a Rational Model"
    - Lalee 1992 "Algorithms for nonlinear optimization"
    - Lu (Chen) 1992 "Bound constrained nonlinear optimization and limited memory methods"
    - Plantenga 1994 "Large-scale nonlinear constrained optimization using trust regions"
    - Hribar 1996 "Large-scale constrained optimization"
    - G. Liu 1999 "Design issues in algorithms for large scale nonlinear programming"
  - 2001–2010, constrained NLP / KNITRO:
    - Marazzi 2001 "Nonlinear Optimization with and without Derivatives"
    - Waltz 2002 "Algorithms for Large-Scale Nonlinear Optimization"
    - López-Calva 2005 "Exact-Penalty Methods for Nonlinear Programming"
    - Curtis 2007 "Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization"
    - Hei 2007 "Practical Techniques for Nonlinear Optimization"
    - Wu 2010 "Active Set Algorithms for Large-Scale Nonlinear Programming"
  - 2013–2019, machine learning:
    - Chin 2013 "Nonlinear Optimization Algorithms for Large-Scale Machine Learning"
    - Hansen 2014 "Newton Methods for Large Scale Problems in Machine Learning"
    - Solntsev 2015 "Methods for Nonsmooth and Stochastic Optimization for Machine Learning"
    - Keskar 2017 "Second-Order Methods for Stochastic and Nonsmooth Optimization" (MGP lists **Andreas Wächter as advisor 1 and Nocedal as advisor 2**)
    - Berahas 2018 "Methods for Large Scale Nonlinear and Stochastic Optimization"
    - Bollapragada 2019 "Methods for Deterministic and Stochastic Optimization"
  - 2024, noise:
    - Sun 2024 "Numerical Methods in Noisy, Stochastic, Nonlinear Optimization"
  - Not in MGP: Shi, Xie and Xuan (all noise-era, 2021–2023 by various sources).
- **Co-advising.**
  - Keskar was co-advised with Wächter (MGP).
  - The current student Yuchen Lou is marked "(co-advised)" on `jnocedal.github.io`; the co-advisor is not named (Gaps).

### 3.2 The Byrd–Nocedal–student triad [practice, primary: computed from DBLP, 77 de-duplicated records, a lower bound since OpenAlex lists ~174 works]

- **Coverage.** 22 of Nocedal's students appear as his DBLP co-authors. **15 of the 22 have at least one paper that also includes Richard H. Byrd:**
  - Waltz 5, Curtis 3, Chin 3, Lu 2, Wu 2, Xie 2;
  - one each for Liu, Marazzi, Hribar, Hansen, Solntsev, Berahas, Bollapragada, Shi, López-Calva.
- **Span.** The triads run from Byrd, Liu & Nocedal 1992 (doi:10.1137/0802026) to Shi, Xie, Byrd & Nocedal 2022 (doi:10.1137/20M1373190).
- **Examples:**
  - Byrd, Lu, Nocedal & Zhu 1995, L-BFGS-B (doi:10.1137/0916069);
  - Byrd, Hribar & Nocedal 1999 (doi:10.1137/S1052623497325107);
  - Byrd, Curtis & Nocedal 2008 (doi:10.1137/060674004);
  - Byrd, Chin, Nocedal & Wu 2012 (doi:10.1007/S10107-012-0572-5);
  - Bollapragada, Byrd & Nocedal 2018 (doi:10.1137/17M1154679);
  - Berahas, Byrd & Nocedal 2019 (doi:10.1137/18M1177718);
  - Xie, Byrd & Nocedal 2020 (doi:10.1137/19M1240794).
- **Observed by a student.** Curtis, 2007 thesis, Acknowledgments p. 5 [observed, primary]:
  - "Any scientific accomplishments contained in these pages would not have been possible without the knowledge and expertise of Richard Byrd. I am honored to have had the opportunity to work closely with Richard and would like to thank him for all of the stimulating conversations we have had about this and other work."
- **What Nocedal says about Byrd's role** [stated, primary, caption-derived]:
  - 2026 [1:17:16–1:17:49]: "we started looking at that case again with Richard Bird [Byrd] closely and we immediately identified the obstacles".
  - 2026 [0:43:16]: Byrd, "if he's proven a theorem, he doesn't feel any need to write it down."
- **Reading** [inferred]: Byrd appears to act as a second, theory-heavy supervisor who works at a distance (Colorado). The students do the writing and the coding. How the remote co-supervision was organised (visits, calls, summer stays) is **not documented** (Gaps).
- **Shift after 2022** [practice, primary: DBLP]. None of the 2023–2026 student papers include Byrd:
  - Sun & Nocedal 2023, doi:10.1007/S10107-023-01941-9;
  - Sun & Nocedal 2024, arXiv:2411.02665;
  - Lou, Sun & Nocedal 2025, doi:10.1137/24M1632279 (arXiv:2401.15007);
  - Xuan & Nocedal 2026, doi:10.1016/J.ORL.2025.107398.
  
  Byrd's last DBLP record with Nocedal is Öztoprak, Byrd & Nocedal 2023 ("Constrained Optimization in the Presence of Noise", *SIAM J. Optim.*), which has no student. Why the change happened is not stated anywhere I found.
- **Other second supervisors.**
  - Andreas Wächter (Northwestern colleague): Curtis, Nocedal & Wächter 2009 (doi:10.1137/08072471X); Nocedal, Wächter & Waltz 2009 (doi:10.1137/060649513); Keskar, Nocedal, Öztoprak & Wächter 2016 (doi:10.1080/10556788.2016.1138222).
  - Nick Gould on Hribar's and Waltz's papers: Gould, Hribar & Nocedal 2001 (doi:10.1137/S1064827598345667); Byrd, Gould, Nocedal & Waltz 2004 (doi:10.1007/S10107-003-0485-4).
  - Sven Leyffer on López-Calva's: Leyffer, López-Calva & Nocedal 2006 (doi:10.1137/040621065).
  - [practice, primary]

### 3.3 The code is the lab: students write, inherit and test inside the group's solver [practice + observed, primary]

- **First code by a student, in parallel with the theory.**
  - 2026 [1:17:49]: "the theory was guiding at the side of the algorithm and then at the on the side I had a student Mary Beth Ryber [Hribar] we were coding it there and this is an effort that took a number of years" [stated, caption-derived].
  - The paper is Byrd, Hribar & Nocedal 1999, doi:10.1137/S1052623497325107.
- **A later student rewrites it.**
  - 2026 [1:18:55–1:19:29]: "that led to several PhD dissertations and like the third dissertation or so was done by a former student called Richard Waltz. He inherited the code and he told me this code is complete spaghetti now. [laughter] this is just you know unwieldy. Can I just write it from scratch? So he did and he stayed with this and to this day Richard Waltz is working for Nitro [KNITRO]." [stated, caption-derived]
  - The student's rewrite became the product: Byrd, Nocedal & Waltz, "Knitro: An Integrated Package for Nonlinear Optimization" (2006), doi:10.1007/0-387-30065-1_4. The CV lists Nocedal as co-founder of Ziena Optimization in 2001 [practice].
- **Later students get the source code and support from former students.**
  - Curtis 2007, Acknowledgments p. 5: "Richard has been a good friend and I would like to thank him and Todd Plantenga for access to, and technical support for, KNITRO source code." [observed, primary]
  - Plantenga was himself a Nocedal PhD (1994): Lalee, Nocedal & Plantenga 1998, doi:10.1137/S1052623493262993.
- **Standard experimental path in a thesis: Matlab prototype, then test sets, then an application, then inside KNITRO.** From Curtis 2007 [practice, primary]:
  - p. 50: "We first applied our stand-alone Matlab implementation of Algorithm 4.1 to a set of 44 equality constrained problems from the CUTEr [4, 19] and COPS [10] collections."
  - p. 72: "This section contains numerical results for a particular implementation of Algorithm 5.3 based on the KNITRO-Direct algorithm from the KNITRO 5.0 software package [40]."
  - p. 94: "We tested the code using a set of 85 equality constrained problems from the CUTEr [4, 19] and COPS [10] collections."
  - Chapter 4 also uses PDE-constrained model problems through a Matlab environment "provided by Haber and Hanson [21]" (p. 48).
- **Robustness is stressed on purpose, not hidden.** Curtis 2007, p. 50: "Though there exist techniques for continuing a stagnated run of the algorithm when an ascent direction for the penalty function or a short steplength coefficient is computed, we implement naïve failure tests in Algorithm 4.1 to aggressively challenge the robustness of our approach." [practice, primary]
  - Whether this is a group norm or Curtis's own choice is **not established**. It is consistent with the "detect failure" theme in 02-methodology R8 [inferred].
- **Comparisons against the group's own default.** Curtis 2007, p. 95: "We compare the results of the algorithm using the standard penalty function approach in KNITRO-Direct, call it pi default, with the results using a flexible penalty function." The baseline is the production code the group maintains [practice, primary].

### 3.4 Numerical-study papers as student projects [practice, primary; reading inferred]

Several student papers are comparative numerical investigations rather than new-method papers:
- Hei, Nocedal & Waltz 2008, "A Numerical Study of Active-Set and Interior-Point Methods for Bound Constrained Optimization" (doi:10.1007/978-3-540-79409-7_18);
- Berahas, Bollapragada & Nocedal 2017, "An Investigation of Newton-Sketch and Subsampled Newton Methods" (arXiv:1705.06211);
- Shi, Xuan, Öztoprak & Nocedal 2023, "On the numerical performance of finite-difference-based methods for derivative-free optimization" (doi:10.1080/10556788.2022.2121832).

[inferred] A careful benchmark of existing methods seems to be one way a student (or a new research direction) gets started. This is not stated anywhere.

### 3.5 Cohorts: senior students work with juniors [practice, primary]

- **Chains of co-authorship between students:**
  - Berahas + Bollapragada (arXiv:1705.06211);
  - Bollapragada + Shi (arXiv:1802.05374, ICML 2018);
  - Shi + Xie (doi:10.1137/20M1373190);
  - Shi + Xie + Xuan (doi:10.1137/21M1452470);
  - Shi + Xuan (doi:10.1080/10556788.2022.2121832);
  - Sun + Lou (arXiv:2401.15007; doi:10.1137/24M1632279).
- **Senior students review juniors' drafts.** Progressive-batching L-BFGS paper (arXiv:1802.05374), Acknowledgements: "We thank Albert Berahas for his insightful comments regarding multi-batch L-BFGS and probabilistic line searches, as well as for his useful feedback on earlier versions of the manuscript." Berahas was the previous student on multi-batch L-BFGS (Berahas, Nocedal & Takáč, NIPS 2016).
- **Office-mates as support.** Curtis 2007, p. 5: "especially thank my officemates and good friends, Gabriel López-Calva and Long Hei, for helping me out so much over the past few years" [observed, primary].

### 3.6 Industry embedding of students (c. 2010–2021) [practice, primary]

- **Internship leading to a paper.** Keskar, Mudigere, Nocedal, Smelyanskiy & Tang, arXiv:1609.04836 (ICLR 2017), p. 1, footnote on Keskar: "Work was performed when author was an intern at Intel Corporation". The three co-authors besides Keskar and Nocedal are listed with Intel affiliations.
- **Recurring industry co-authors on student papers:**
  - Mudigere and Tang (Intel) again on Bollapragada, Mudigere, Nocedal, Shi & Tang, arXiv:1802.05374. The affiliations are from the arXiv PDF.
  - Yoram Singer ("Google Research", arXiv PDF footnote) on Byrd, Hansen, Nocedal & Singer, arXiv:1401.7020.
  - Other non-academic co-authors on student papers are Neveitt (Byrd, Chin, Neveitt & Nocedal 2011, doi:10.1137/10079923X) and Olsen and Rennie (Chin, Nocedal, Olsen & Rennie 2013, doi:10.1109/TASL.2013.2263142). **Their affiliations were not checked in this run.**
- **Internships and visits on students' own CVs:**
  - Shi: Facebook research intern 2019 ("Advisor: Dheevatsa Mudigere"), then Meta research scientist from 2021 (Shi CV, primary).
  - Bollapragada: ExxonMobil Upstream Research intern 2016; visiting researcher at INRIA Paris with A. d'Aspremont, April–June 2018 (Bollapragada CV, primary).
- **Industry money funds students.** arXiv:1802.05374, Acknowledgements: "Bollapragada is supported by DOE award DE-FG02-87ER25047. Nocedal is supported by NSF award DMS-1620070. Shi is supported by Intel grant SP0036122." The CV lists INTEL, "Optimization Methods for Large Scale Machine Learning", Feb 2016–Dec 2018, $150,000; Google grants 2010 and 2011–12.
- **Former students as his channel into industry.** NITMB 2024 talk:
  - [0:04:35]: "I have students and colleagues in the tech industry um and have discussions with them".
  - [1:00:39–1:01:12]: "one of my former students is a co-author of GPT4 and he works on that uh gening data selecting data using data and I never get any information from him. … They want to talk to me about optimization and that's it."
  - [stated, primary, caption-derived]. The GPT-4 student is not named, and the claim was not checked.
- **He publicises former students' industry results.** NITMB 2024 [0:05:08–0:05:40]: "a student who graduated two years ago Michael Shei [Shi], he graduated from our department. This year he and his team at Meta won the machine learning training competition which is called the ML Commons. … I I was glad to see that my former student won by a lot and they beat what is called the atom [Adam] method." [stated, primary, caption-derived; the competition result itself was not checked]

### 3.7 Credit-giving in talks [practice, primary, caption-derived]

- Simons Institute 2017 [0:00:01]: "one of my students here has done a lot of the ideas that I wanna present here, so I just want to give credit to these people here."
- UCLA 2021 [0:01:06]: "in the last couple of years we've written a few papers a combination of authors and here they are they of course get a lot of credit for what has been done here". Later [0:42:16]: "the students that i showed you there in the beginning they're cheerful they're all smiling because they're working on this topic".
- RIIAA 2019 [0:13:03]: "my son Albert Barajas did a lot of this work here". This is almost certainly an ASR error for "my student Albert Berahas" [inferred]; the passage is about derivative-free optimization, Berahas's topic (doi:10.1137/18M1177718).
- Author order switches around 2020 to student first, Nocedal last (01-publications §2.2). The pre-2020 exceptions also put a student or junior first, e.g. Solntsev, Nocedal & Byrd 2015 (doi:10.1080/10556788.2015.1028062). Why he switched is not stated.

### 3.8 Committees, awards and placement [practice, primary]

- **Former students on later committees.**
  - Curtis's committee: "Prof. Robert Fourer, Prof. Sanjay Mehrotra, Dr. Richard A. Waltz" (Curtis CV).
  - Curtis sat on Melody Xuan's committee, 2022–2023, "Advisor: Jorge Nocedal" (Curtis CV).
- **Department dissertation prize.** Two students won the Northwestern IEMS Nemhauser Dissertation Award: Curtis (2008, Curtis CV) and Bollapragada (2019, "Best doctoral dissertation, IEMS", Bollapragada CV). Other students' awards were not checked.
- **Placements verified this run:**
  - Curtis: Lehigh (professor);
  - Berahas: University of Michigan (Curtis collaborators page; he was also a postdoc of Curtis's);
  - Bollapragada: UT Austin;
  - Shi: Meta;
  - Waltz: KNITRO developer, per Nocedal (2026 [1:19:29]).

---

## 4. Observed by others (secondary unless the observer wrote it first-hand)

| # | Observation | Who / where | Tag |
|---|-------------|-------------|-----|
| O1 | "I would like to thank first, and above all, Jorge Nocedal. Far be it from me to try and capture, in only a few short lines, the level of guidance and support that he has provided for me over the past few years. Suffice it to say that I have been extremely privileged to have Jorge as an advisor and friend, and I would like nothing more than for us to maintain a close professional and personal relationship for many years to come." | According to Frank E. Curtis, PhD thesis, Northwestern 2007, Acknowledgments p. 5 | [observed, primary (the student's own text)]. Warm but generic: it says nothing about *how* he advised. |
| O2 | "It should also be added that, all throughout his career, Nocedal has been outstanding at mentoring both students and junior colleagues." | According to the INFORMS 2017 John von Neumann Theory Prize citation (INFORMS award page) | [observed, secondary: prize committee, no specifics] |
| O3 | "Jorge is open minded about emerging, challenging problems, such as deep learning, when most researchers are hesitating about whether to get into this field." The article frames Wang as having "the rare opportunity to have such a renowned researcher as a mentor". | According to Zhaoran Wang (junior IEMS colleague), McCormick Magazine, Spring 2021 | [observed, secondary] |
| O4 | Nocedal "thrives on the collaborative energy his students bring to his research". | According to the article's writer (Sara Langen), McCormick Magazine, Spring 2021 | [observed, secondary; journalistic] |
| O5 | Byrd as the scientific backbone of the thesis (quoted in §3.2) | According to Curtis 2007, p. 5 | [observed, primary] |
| O6 | Former students (Waltz, Plantenga) run the code infrastructure for current students | According to Curtis 2007, p. 5 | [observed, primary] |
| O7 | Nocedal's own observation of the book collaboration with Steve Wright: "Steve is very fast and I'm very slow. and he would [clears throat] write a a chapter and I would start tearing it apart … my plan was always sketchy and his attitude is there's nothing here. Contact me when you've actually written it." And "from day one he was an excellent collaborator". | 2026 [1:10:40–1:11:15] | [stated about a collaborator, primary, caption-derived]. Wright's side was **not read** (Gaps). |

---

## 5. Lab culture and tacit knowledge

Each item says who reports it. Anything reconstructed from records rather than reported by a student is marked [inferred].

- **T1. KNITRO source is the testbed; ask Waltz or Plantenga when stuck.** According to Curtis (2007 thesis, p. 5) [observed, primary]. The thesis chapters confirm it in practice (§3.3).
  - For a solver team the transferable habit is to put a new globalisation or step idea inside the production code and compare against its default. Toy code alone is not enough.
- **T2. Theory questions go to Byrd.** According to Curtis 2007 (p. 5) and Nocedal 2026 [1:17:16–1:17:49] [observed + stated, primary]. The triad statistics in §3.2 show this in practice.
- **T3. Prototype in Matlab on CUTEr/COPS, add an application, then embed in KNITRO.** From Curtis 2007, pp. 48–95 [practice, primary]. That this is the *group's* standard path, and not just Curtis's, is [inferred] from one thesis.
- **T4. Stress-test robustness with deliberately naïve failure tests.** From Curtis 2007, p. 50 [practice, primary]. Group-wide status: [inferred].
- **T5. Senior students review juniors' drafts.** From the arXiv:1802.05374 acknowledgements [practice, primary].
- **T6. Internships are research periods that produce papers,** and some industry contacts (e.g. Mudigere, Tang) recur across students. From the arXiv:1609.04836 footnote, arXiv:1802.05374 and the Shi CV [practice, primary]. That this is deliberate placement is [inferred].
- **T7. The US–Mexico optimization workshops are part of students' exposure.** Bollapragada presented "Adaptive Sampling Strategies for Stochastic Optimization" (with Byrd and Nocedal) at the US and Mexico Workshop on Optimization and its Applications, Huatulco, July 2018 (Bollapragada CV) [practice, primary]. Nocedal values these workshops for depth (S8) [stated]. Whether he sends students routinely is [inferred].
- **T8. Learn a new field by teaching it, with a student TA.** When he moved into machine learning he taught IEMS 490 "Introduction to Machine Learning". Stefan Solntsev was the teaching assistant, and the syllabus says the course "follows the general organization of the class taught by Andrew Ng at Stanford" (syllabusML.pdf, undated, c. 2014; also cited in 02-methodology) [practice, primary]. He said the same about the book: "the reason why I wanted to buy a book [write a book] is just because I wanted to learn the subject well" (2026 [1:07:53]) [stated, caption-derived].
- **Not found**: how group meetings run, how often he meets students, how problems are handed out, what a first-year student does, how drafts are edited. No first-hand student account covers any of these.

---

## 6. Failures, abandoned directions and friction (mentorship-relevant)

- **His own thesis as a failure he uses in teaching.** "It was a impressive collection of failed ideas" (2026 [0:47:11]). He turns it into advice to students (S1) [stated, primary, caption-derived]. The breakthrough came afterwards, alone, at UNAM (01-publications §3, SW1).
- **Advisor mismatch.** He left his first Rice advisor after six months (L1) [stated].
- **A student's code judged unmaintainable.** Waltz called the inherited KNITRO code "complete spaghetti" and rewrote it (2026 [1:19:29]). Nocedal tells this as a success of the student's initiative, not a failure of the first code [stated].
- **A student-led paper that was contested.** The large-batch paper (Keskar et al., arXiv:1609.04836), produced during Keskar's Intel internship, was challenged by Dinh, Pascanu, Bengio & Bengio, "Sharp Minima Can Generalize For Deep Nets" (arXiv:1703.04933; title checked this run). No written response by the group was found (see 01-publications).
- **The field moved away from his style of work, which affects what students inherit.** He says complexity-driven theory is "lacking intuition. They're not distinguishing between good methods and bad methods", and that "the computational side of it … used to be the core now it's a smaller field" (2026 [1:29:02–1:29:35]) [stated, caption-derived]. What this means for students' careers is not discussed.
- **Regret he passes on.** He says he saw the statistical and architectural sides of machine learning too late (2026 [1:26:13–1:27:20], [1:43:00–1:44:47]) [stated]. He does not say whether it shaped what he told students.
- **No rejected student papers, dropped student projects or students who left the programme were found.**

---

## 7. Era and resource context

| Era | Group setup | Resources | Evidence |
|-----|-------------|-----------|----------|
| 1983–1999 (EECS; assistant to full professor) | 1–2 PhD students per project. Byrd as remote co-author. Students code Fortran solvers (L-BFGS-B with Lu and Zhu; NITRO with Hribar; trust-region code with Lalee and Plantenga) | DOE DE-FG02-87ER25047 from 1987. NSF. Harwell library distribution | CV; DBLP; 2026 interview; 01-publications §6 |
| 2000–2010 (Ziena from 2001; KNITRO) | Students work inside a commercial code base. Former students maintain it (Waltz, Plantenga). Postdocs Morales, Orban. Co-supervision with Wächter, Gould, Leyffer | DOE, NSF (incl. STTR 2003 for software). KNITRO source | CV; Curtis 2007; DBLP |
| 2010–2019 (turn to ML; chair 2013–17) | Largest cohort (Chin, Hansen, Solntsev, Keskar, Berahas, Bollapragada, Shi, Xie). Industry internships and co-authors. Student cohorts. The ML course as training | Google (2010, 2011–12), Intel ($150k, 2016–18), ONR, NSF, DOE | CV; arXiv PDFs; student CVs |
| 2020–2026 (NAE 2020) | 2–3 author papers with one or two students on noise-tolerant methods. Byrd absent from student papers after 2022. In 2026 he says he is "taking a pause from writing research papers" to write the 3rd edition of the book (2026 [1:45:19]) | Not read (the CV stops c. 2018) | DBLP; 2026 interview |

**Transfer warning** [inferred]:
- Several of these practices depended on resources a user of this skill may not have:
  - a lifelong theory partner (Byrd);
  - a commercial solver owned by the group, with former students as maintainers;
  - a single federal grant renewed for three decades;
  - industry partners hosting interns.
- What transfers to a solver team is the *pattern*: test new ideas inside the production code against its defaults; build robustness tests into the experiments; have seniors review juniors; keep a long-term theory partner in the loop.

---

## 8. Mapping to the seven layers (framework §一)

- **Layer 4 (experiment and execution)**: T1, T3, T4; §3.3–3.4. The evidence is one thesis plus paper titles.
- **Layer 5 (result judgement)**: S1 (fog of uncertainty); the robustness stress tests (T4).
- **Layer 6 (expression)**: credit-giving in talks (§3.7); author-order shift (01-publications).
- **Layer 7 (research organisation)**: most of this note. Covered: the triad, code as lab, cohorts, industry embedding, committees, the lineage (§1), and stated ethos (§2).
- **Layers 1–3 (taste, problem choice, idea generation)**: only indirect evidence here (S9 "most beautiful solution", S13 "ladder", L5 Dantzig's courage). See 02-methodology.

---

## Contradictions (kept, not reconciled)

- **C1. Graduation years and names differ across his own pages, his CV, MGP and students' CVs** [practice, primary vs secondary]:

  | Student | Values found |
  |---------|--------------|
  | Bollapragada | 2018 (`jnocedal.github.io`); 2019 (his CV, MGP; Nocedal CV "2019 (exp)") |
  | Shi | "2020 (exp)" (Nocedal CV); PhD "2016–2021" (Shi CV); "September 2016 – December 2021" (Shi bio page); 2022 (`jnocedal.github.io`). His Meta job started August 2021, before the December 2021 end date. |
  | Solntsev | 2015 (homepage, MGP); 2016 (Nocedal CV) |
  | Hribar | 1995 (homepage, CV); 1996 (MGP) |
  | López-Calva | 2006 (CV); 2005 (MGP); absent from both homepage student lists |
  | Peihuang Lu | "Peihuang Lu" (homepage, CV); "Peihuang Lu Chen" (MGP) |
  | Plantenga | "Todd Plantega" (homepage, CV); "Plantenga" (MGP, DBLP, Curtis thesis) |
  | Shigeng Sun | "Current Students" on `jnocedal.github.io`; PhD 2024 in MGP |

- **C2. Supervised hands-off, supervises hands-on.** He describes his own PhD as done "pretty much on my own" (L2). His record shows him as co-author on essentially every student's papers, and Byrd on most of them as well (§3.2). He never comments on the contrast [inferred tension].
- **C3. Says author counts are inflating; his own peaked in the 2010s.** He questions "more papers and more authors" (S6). DBLP mean authors per paper:
  - 1990s: 2.69;
  - 2000s: 2.8;
  - 2010s: 3.5 (including two 5-author papers with Intel co-authors, 2016 and 2018);
  - 2020s: 3.0.

  His numbers stay small by ML standards, but the rise came in exactly the period he now criticises [practice vs stated].
- **C4. Lone discovery versus team.** In 2026 [1:14:34–1:15:07] he says big discoveries are usually made "by one or two people quietly in a corner nobody paying attention and then when the big ideas come there's a team that goes and develop this". The ASR is garbled around "I don't believe that", so the exact polarity is uncertain. In 2021 he said of group work: "you feel there was a team of people who did it" (S10, secondary). Both are kept.
- **C5. Credit to students versus alphabetical order.** He credits students explicitly in talks (§3.7), yet until about 2020 author lists were mostly alphabetical, which puts him after most student surnames by accident. The 2020 switch to student-first is unexplained (01-publications §2.2).

---

## Gaps

1. **No first-hand student recollection besides Curtis's thesis acknowledgement.** No blog post, memorial piece, interview with a former student, or lab/onboarding guide was found. Searches: one WebSearch for thesis acknowledgements, one for a Festschrift, plus homepage crawling of Curtis, Shi and Bollapragada.
2. **Other theses not read.** Full texts of the dissertations of Waltz (2002), Hribar (1996), Berahas (2018), Keskar (2017), Bollapragada (2019), Shi, Xie, Xuan and Sun were not found openly.
   - Northwestern Arch returned "No entries found" for "Nocedal".
   - OpenAlex indexed none of the titles.
   - The Semantic Scholar API was rate-limited; the arXiv API returned errors.
   - ProQuest was not used (login).
3. **No Festschrift, birthday workshop or special issue in his honour was found** (one WebSearch).
4. **DOE ASCR Discovery "genealogy" article on Nocedal was not read.** It is linked from his homepage "Miscellaneous" page as `ascr-discovery.science.doe.gov/genealogy/nocedal1.shtml`. The host does not resolve, and web.archive.org is blocked from this environment. A Wayback snapshot of `nocedal2.shtml` exists (2013-02-16) but could not be fetched. By its title, this is the most likely public source on his lineage and students.
5. **2012 Dantzig Prize citation not read**: mathopt.org needs JavaScript and the Wayback copy is blocked.
6. **SIAM News 2024 prize article not read** (Cloudflare 403). A GlobeNewswire copy of the SIAM release was read through WebFetch, which returned extracted quotes rather than raw HTML. It has no content on students.
7. **Not documented anywhere I found:**
   - how the Byrd co-supervision works in practice (visits, Colorado stays, calls);
   - how group meetings run;
   - how thesis problems are assigned;
   - why Byrd drops off student papers after 2022;
   - who co-advises Yuchen Lou;
   - which former student co-authored GPT-4.
8. **The collaborators' side is missing.** No account by Byrd, Steve Wright, Waltz or Wächter of working with Nocedal or his students was found. The Springer front matter of *Numerical Optimization* (preface acknowledgements) was blocked by a bot challenge. I did not use unauthorised PDF copies of the book.
9. **Industry co-author affiliations for Neveitt, Olsen and Rennie were not checked.**

---

## Sources

One line each: title, author, date, URL or DOI, primary/secondary.

1. "Subject to: Jorge Nocedal", long-form interview (YouTube, ASR captions), uploaded 2026-03-18. https://www.youtube.com/watch?v=CfR-llfmb6E, local `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt`. **Primary (caption-derived).**
2. J. Nocedal, acceptance speech, INFORMS John von Neumann Theory Prize, Oct 2017. http://www.ece.northwestern.edu/~nocedal/PDFfiles/VonNeumann_Speech.pdf, notes in `../sources/talks/2017-von-neumann-prize-acceptance-speech.md`. **Primary.**
3. J. Nocedal, "Zero-order and Dynamic Sampling Methods for Nonlinear Optimization", Simons Institute, 2017. https://www.youtube.com/watch?v=OfVZ9gArXiY, local transcript. **Primary (caption-derived).**
4. J. Nocedal, UCLA CS201 seminar, 2021-04-08. https://www.youtube.com/watch?v=4a12aV77CAI, local transcript. **Primary (caption-derived).**
5. J. Nocedal, "How is it Possible to Train Deep Neural Networks?", NITMB seminar, 2024-10-25. https://www.youtube.com/watch?v=XrX7MEMbdYw, local transcript. **Primary (caption-derived).**
6. J. Nocedal, RIIAA 2.0 keynote, Mexico City, Aug 2019. https://www.youtube.com/watch?v=3zUD3H71HQ0, local transcript. **Primary (caption-derived).**
7. J. Nocedal, Purdue distinguished seminar, 2017-02-15. https://www.youtube.com/watch?v=srg3Rx2HvfQ, local transcript. **Primary (caption-derived).**
8. J. Nocedal, homepage "Students / People" page (footer 2008, content c. 2018). http://www.ece.northwestern.edu/~nocedal/students.html. **Primary.**
9. J. Nocedal (apparently his own site), jnocedal.github.io. Current and former students list; contains unedited template filler. https://jnocedal.github.io/. **Primary** (authorship not independently confirmed).
10. J. Nocedal, Curriculum Vitae (c. 2018): students supervised, grants. http://www.ece.northwestern.edu/~nocedal/CV/cv_nocedal.pdf. **Primary.**
11. J. Nocedal, IEMS 490 "Introduction to Machine Learning" syllabus (undated, c. 2014). http://users.iems.northwestern.edu/~nocedal/syllabusML.pdf. **Primary.**
12. "Solving complex machine learning optimization problems: A conversation with Jorge Nocedal", NITMB (undated, c. 2024–25). https://www.nitmb.org/post/solving-complex-machine-learning-optimization-problems-a-conversation-with-jorge-nocedal. **Primary (written Q&A).**
13. F. E. Curtis, *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, PhD thesis, Northwestern University, 2007 (Acknowledgments p. 5; pp. 48–95 read). http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf. **Primary.**
14. F. E. Curtis, Curriculum Vitae (last revised 2026-04-07): committee, Nemhauser award, Xuan committee. http://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf. **Primary.**
15. F. E. Curtis, homepage "Collaborators/Students/Postdocs" page (accessed 2026-09-28). https://coral.ise.lehigh.edu/frankecurtis/collaborators/. **Primary.**
16. H.-J. M. Shi, CV and Biography page (bio generated 2023-08-28). https://hjmshi.github.io/CV.pdf, https://hjmshi.github.io/bio.html. **Primary.**
17. R. Bollapragada, Education page and CV (accessed 2026-09-28). https://sites.google.com/view/raghub/education, CV via Google Drive link on that page. **Primary.**
18. Mathematics Genealogy Project: Jorge Nocedal (id 43740), his 19 listed students, and Richard A. Tapia (id 14920). https://www.mathgenealogy.org/id.php?id=43740. **Secondary.**
19. DBLP records for Jorge Nocedal (pid n/JorgeNocedal), fetched via the DBLP SPARQL endpoint 2026-09-28 (cached by this run's harvest). https://dblp.org/pid/n/JorgeNocedal. **Primary (bibliographic record).**
20. N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, P. T. P. Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", ICLR 2017. arXiv:1609.04836 (p. 1 footnote read). **Primary.**
21. R. Bollapragada, D. Mudigere, J. Nocedal, H.-J. M. Shi, P. T. P. Tang, "A Progressive Batching L-BFGS Method for Machine Learning", ICML 2018. arXiv:1802.05374 (affiliations, acknowledgements read). **Primary.**
22. R. H. Byrd, S. L. Hansen, J. Nocedal, Y. Singer, "A Stochastic Quasi-Newton Method for Large-Scale Optimization". arXiv:1401.7020 → *SIAM J. Optim.* 26 (2016), doi:10.1137/140954362 (affiliation footnotes read). **Primary.**
23. S. Langen, "The Optimizer", McCormick Magazine, Spring 2021. https://www.mccormick.northwestern.edu/magazine/spring-2021/the-optimizer. **Secondary.**
24. INFORMS, award recipient page for Jorge Nocedal: 2017 John von Neumann Theory Prize citation. https://www.informs.org/Recognizing-Excellence/Award-Recipients/Jorge-Nocedal. **Secondary.**
25. A. Morris, "Nocedal Receives John von Neumann Theory Prize", Northwestern Engineering news, 2017-10-26. https://www.mccormick.northwestern.edu/news/articles/2017/10/nocedal-receives-john-von-neumann-theory-prize.html. **Secondary.**
26. B. Sandalow, "Jorge Nocedal Selected for Lagrange Prize", Northwestern Engineering news, 2021-04-06. https://mccormick.northwestern.edu/news/articles/2021/04/jorge-nocedal-selected-for-lagrange-prize.html. **Secondary.**
27. "Jorge Nocedal Awarded John von Neumann Prize by the Society for Industrial and Applied Mathematics", Northwestern Engineering news, April 2024. https://www.mccormick.northwestern.edu/news/articles/2024/04/jorge-nocedal-awarded-john-von-neumann-prize-by-the-society-for-industrial-and-applied-mathematics/. **Secondary.**
28. SIAM press release "Jorge Nocedal is the 2024 SIAM John von Neumann Prize Lecturer", GlobeNewswire, 2024-04-02 (read via WebFetch extraction). https://www.globenewswire.com/news-release/2024/04/02/2856361/0/en/jorge-nocedal-is-the-2024-siam-john-von-neumann-prize-lecturer.html. **Secondary.**

**Papers cited as evidence of practice.** Identifiers come from DBLP (source 19) unless noted; all were checked in this run.
- Nocedal 1980, doi:10.1090/s0025-5718-1980-0572855-7 (from the OpenAlex list in `../sources/publications/publications.md`)
- Byrd, Liu & Nocedal 1992, doi:10.1137/0802026
- Byrd, Lu, Nocedal & Zhu 1995, doi:10.1137/0916069
- Lalee, Nocedal & Plantenga 1998, doi:10.1137/S1052623493262993
- Byrd, Hribar & Nocedal 1999, doi:10.1137/S1052623497325107
- Gould, Hribar & Nocedal 2001, doi:10.1137/S1064827598345667
- Byrd, Gould, Nocedal & Waltz 2004, doi:10.1007/S10107-003-0485-4
- Leyffer, López-Calva & Nocedal 2006, doi:10.1137/040621065
- Byrd, Nocedal & Waltz 2006 (Knitro), doi:10.1007/0-387-30065-1_4 (OpenAlex list)
- Hei, Nocedal & Waltz 2008, doi:10.1007/978-3-540-79409-7_18
- Byrd, Curtis & Nocedal 2008, doi:10.1137/060674004
- Curtis, Nocedal & Wächter 2009, doi:10.1137/08072471X
- Nocedal, Wächter & Waltz 2009, doi:10.1137/060649513
- Byrd, Chin, Neveitt & Nocedal 2011, doi:10.1137/10079923X
- Byrd, Chin, Nocedal & Wu 2012, doi:10.1007/S10107-012-0572-5
- Chin, Nocedal, Olsen & Rennie 2013, doi:10.1109/TASL.2013.2263142
- Solntsev, Nocedal & Byrd 2015, doi:10.1080/10556788.2015.1028062
- Keskar, Nocedal, Öztoprak & Wächter 2016, doi:10.1080/10556788.2016.1138222
- Berahas, Nocedal & Takáč, "A Multi-Batch L-BFGS Method for Machine Learning", NIPS 2016 (DBLP record)
- Berahas, Bollapragada & Nocedal 2017, arXiv:1705.06211
- Bollapragada, Byrd & Nocedal 2018, doi:10.1137/17M1154679
- Berahas, Byrd & Nocedal 2019, doi:10.1137/18M1177718
- Xie, Byrd & Nocedal 2020, doi:10.1137/19M1240794
- Shi, Xie, Byrd & Nocedal 2022, doi:10.1137/20M1373190
- Shi, Xie, Xuan & Nocedal 2022, doi:10.1137/21M1452470
- Shi, Xuan, Öztoprak & Nocedal 2023, doi:10.1080/10556788.2022.2121832
- Öztoprak, Byrd & Nocedal 2023, "Constrained Optimization in the Presence of Noise", *SIAM J. Optim.* (DBLP record; DOI not listed here)
- Sun & Nocedal 2023, doi:10.1007/S10107-023-01941-9
- Sun & Nocedal 2024, arXiv:2411.02665
- Lou, Sun & Nocedal 2025, doi:10.1137/24M1632279 (arXiv:2401.15007)
- Xuan & Nocedal 2026, doi:10.1016/J.ORL.2025.107398
- Dinh, Pascanu, Bengio & Bengio, "Sharp Minima Can Generalize For Deep Nets", arXiv:1703.04933 (title checked on arxiv.org)

---

## Top-up (2026-09-28)

Added at the Phase 1.5 review checkpoint by the review agent, not by research agent 04. Target: the one thin part of this dimension, first-hand evidence from the student side (Gap 1). Budget used: 3 WebSearch calls, plus curl on known URLs. Nothing above this heading was changed.

**Result in one line.** No second first-hand student account of *how* Nocedal supervises was found; Curtis's 2007 thesis acknowledgement is still the only one. The top-up adds one student's own records (Shigeng Sun) and a collaborators' acknowledgement from April 2026.

**TU1. Shigeng Sun's own homepage and CV** [practice, primary: student-written records; factual, not testimony about supervision]
- Homepage: "I obtained my PhD in Applied Mathematics under the supervision of National Academy of Engineering member, Prof. Jorge Nocedal in 2024." And: "I graduated in 2024 and joined The D.E.Shaw Group as a Quant Analyst upon graduation."
- CV (quoted as extracted, including its spellings):
  - "Ph.D, Engineering Sciences and Applied Mathematics Sept. 2019 - Sept. 2024" / "Advisor: Dr. Jorge Nocedal";
  - "Prof. Nocedal’s Research Group, Department of IEMS, Northwestern University … Sept. 2020-Present";
  - internships: "Virtu Financial … Quantitive Strategiest (Intern) June. 2023 - Aug. 2023" and "Amazon A WS AI Labs … Applied Scientist (Intern) Sept. 2023 - Dec. 2023";
  - "Center of Optimization and Statistical Learning … Student Administrator Aug. 2021-Present";
  - "The D. E. Shaw Group … Quantitive Analyst Oct. 2024 - Present".
- What this changes in this note:
  - **Contradiction C1 (Sun)**: resolved. He finished in September 2024 (his CV; MGP agrees on 2024). The "Current Students" list on `jnocedal.github.io` is stale.
  - **§3.6 industry embedding**: the internship pattern continues past 2021, into 2023 (finance and AWS AI Labs), and the placement is in quantitative finance.
  - **Supervision across departments**: the degree is in ESAM (Engineering Sciences and Applied Mathematics), not IEMS, and he joined the group one year into the PhD (2019 vs 2020) [practice].
  - **Title history of arXiv:2401.15007**: the CV lists the Lou–Sun–Nocedal paper under a third title, "Nonlinear Optimization in the Presence of Noise: Applications, Noise Models and Problem Structure. Preprint on revision with SIAM Journal Of Scientific Computing (2024)". Matching it to arXiv:2401.15007 / doi:10.1137/24M1632279 is [inferred] from authors, year and venue. It adds a middle step to the retitling recorded in `03-process-evidence.md` §4.2.
  - The CV also lists "S. Sun, J. Nocedal, On the Global Convergence of Byrd-Omojokun SQP Method for Equality Constrained Optimization. Preprint." An arXiv title search and a Crossref query found no record, so it has no identifier and must not be cited as a paper.
- Still missing: neither page says anything about how supervision worked.

**TU2. Collaborators continue the noisy-constrained line during his pause and thank him for comments** [practice, primary]
- F. Oztoprak & R. Byrd, "A Noise Tolerant SQP Algorithm for Inequality Constrained Optimization", arXiv:2604.14368 v1 (submitted 15 Apr 2026). Nocedal is **not** an author.
- Acknowledgments (PDF p. 28): "The authors are grateful to Jorge Nocedal for his helpful comments on an earlier version of this work."
- It extends Oztoprak, Byrd & Nocedal 2023 (doi:10.1137/21M1450999). It cites Sun & Nocedal, arXiv:2411.02665 as still a preprint in April 2026 (reference [20]; mentioned on PDF p. 2).
- Reading [inferred]:
  - During the pause he announced in the 2026 interview, he still reads and comments on his core collaborators' drafts. This reverses the "Byrd as standing reader" role in `03-process-evidence.md` §7.
  - The Byrd–Oztoprak pair carries the constrained-noise line on without him.
  - For `06-trajectory.md` §7: this is an item inside the last-12-months window. It is not a Nocedal paper, so 06's "no Nocedal arXiv preprint since 2024-11-04" still holds.

**TU3. Identifier fix for this note.** "Öztoprak, Byrd & Nocedal 2023 … (DBLP record; DOI not listed here)" is doi:10.1137/21M1450999 (Crossref: *SIAM J. Optim.* 33 (2023) 2118–2136; authors Oztoprak, Byrd, Nocedal).

**TU4. What was tried and failed**
- WebSearch 1, `"Jorge Nocedal" PhD dissertation Northwestern acknowledgments "my advisor" pdf`: returned only profile pages (Wikipedia, Northwestern Scholars, Scholar, ResearchGate, MGP, Shi's bio page already used in §3.6).
- WebSearch 2, `"advisor, Jorge Nocedal" OR "advisor Jorge Nocedal" thesis acknowledgements`: returned only profile pages, plus an unrelated Scribd document (not opened).
- WebSearch 3, `Northwestern dissertation "Jorge Nocedal" "Richard Byrd" "I would like to thank" optimization pdf`:
  - it surfaced arXiv:2604.14368 (TU2);
  - the other hits were copies of *Numerical Optimization* on third-party sites. They were **not opened**, because they are not legitimate sources.
- curl on known URLs:
  - MOS *Optima* back issues, sought for the 2012 Dantzig Prize citation: the index sits behind a Cloudflare Turnstile page, and the old `Optima-Issues/optima89–91.pdf` paths return 404;
  - Berahas's Michigan homepage returned 403, and `keskarnitish.github.io` returned 404;
  - Bollapragada's publications page lists his thesis ("Methods for Deterministic and Stochastic Optimization") but gives no link;
  - `hjmshi.github.io` links only a CV;
  - the OSL publications page lists no theses.
- **Gap 1 therefore stands.** Supervision claims in this note rest on the record, on Nocedal's own statements and on one student's acknowledgement.

**Top-up sources** (retrieved 2026-09-28)
- T1. S. Sun, homepage, https://shigengsun.github.io/. Primary (student's own page).
- T2. S. Sun, CV, https://github.com/shigengsun/shigengsun.github.io/blob/master/Shigeng%20CV.pdf (fetched via raw.githubusercontent.com). Primary (student's own record). Personal contact details in it were not copied.
- T3. F. Oztoprak & R. Byrd, "A Noise Tolerant SQP Algorithm for Inequality Constrained Optimization", arXiv:2604.14368 v1 (PDF read: abstract, §1 related work, acknowledgements, references). Primary (collaborators' practice).
- T4. Crossref REST API record for doi:10.1137/21M1450999. Secondary (bibliographic).
- T5. R. Bollapragada, publications page, https://sites.google.com/view/raghub/publications. Primary (thesis listed, no link).
- T6. WebSearch calls 1–3 above. Secondary.
