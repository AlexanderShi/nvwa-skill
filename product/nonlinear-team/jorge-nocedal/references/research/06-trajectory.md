# Jorge Nocedal · 06 Research trajectory

- **Researcher**: Jorge Nocedal. Walter P. Murphy Professor of Industrial Engineering and Management Sciences (IEMS), Northwestern University; Director, Center for Optimization and Statistical Learning (OSL). PhD Rice 1978, advisor Richard A. Tapia.
- **Dimension**: research-craft Phase 1, agent 06 of 06: research trajectory (framework §二 row 6). Covers the dated timeline, advisor and student lineage, each change of direction and what triggered it, when he entered and left each topic relative to the field, and the last 12 months.
- **Research date**: 2026-09-28
- **Sources consulted**: 33 (16 primary, 17 secondary), listed under "Sources". Crossref metadata (60 DOIs queried, 47 cited here) counts there as one secondary source.
- **Local corpus**: `references/sources/papers/`, `essays/` and `software/` hold only `.gitkeep` files, so **no user-supplied material exists** and nothing here is marked "from user-supplied material". Research agent 02 saved the talk and interview transcripts in `../sources/talks/` earlier in this run. They are YouTube captions, mostly automatic speech recognition (ASR) that nobody has checked by hand. Quotes from them are verbatim *captions* with the block timestamp `[h:mm:ss]`, marked "caption-derived". ASR errors stay as they are, with the intended word in square brackets. `private/` was not opened.
- **WebSearch calls used**: 2 of 2 (the 2024 SIAM prize; a third edition of the book).
- **Division of labour**: the publication landscape and signature works are in `01-publications.md`, stated method in `02-methodology.md`, process evidence in `03-process-evidence.md`, and students and supervision in `04-mentorship.md`. This file adds four things: the dated timeline, the causes of each turn and their timing, a topic-by-period matrix built from the CV, and the latest activity. It cross-references the other files rather than repeating them. Where I re-cite a paper, I re-checked its identifier with Crossref, arXiv or zbMATH in this run.

**Labels.** Each item carries one of:
- [stated]: Nocedal said or wrote it;
- [practice]: what the papers, CVs, grants, code or patents show he did;
- [observed]: what others (institutions, press, companies, databases) report;
- [inferred]: my reading, with its basis given.

Each item is also marked primary or secondary.

---

## 0. Headline findings

1. **Five phases, each an overlapping stint of about 8–15 years, joined by one unbroken tool.** The phases are:
   - unconstrained quasi-Newton (QN) and conjugate gradients (CG), 1978–c. 1995;
   - constrained NLP, interior-point methods and KNITRO, c. 1995–2014;
   - machine learning, 2009/10–2019;
   - optimization with noise, 2017/18–2025;
   - a declared pause for the book's third edition, 2025–26.

   Quasi-Newton updating runs through every phase: L-BFGS (1980), L-BFGS-B (1995–97), stochastic, multi-batch and progressive-batching L-BFGS (2014–18), and noise-tolerant BFGS (2020–22). Section 4 has the matrix. [practice, primary]
2. **Most entries into new application areas were pulled in by a user of L-BFGS, not pushed by theory.** Both ECMWF (1990s) and Google (2008/09) approached him because L-BFGS was known. In both cases he says his first advice was *not* to use it. He calls the ECMWF contact "also what led me into machine learning". [stated, primary, caption-derived: 2026 interview [1:15:39], [1:22:16]]
3. **The theoretical turns start from someone else's paper or tool.**
   - The QN convergence theory with Byrd (1987–89) was triggered by Powell's BFGS convergence proof for convex problems [stated, 2026 [0:57:15]].
   - The noise programme (2017→) was built on Moré and Wild's benchmarking (2009) and their noise-estimation tool ECnoise (2011) [stated, UCLA 2021 [0:02:46], [0:33:23]; papers verified].
4. **Failure is the documented trigger of the first turn.** His PhD programme (CG-style extensions of QN methods) was "a impressive collection of failed ideas". L-BFGS came from rejecting that whole approach in his first month back in Mexico in 1978. [stated, primary, caption-derived: [0:47:11], [0:50:00]]
5. **Interior-point methods: he entered with the NLP wave, not ahead of it.** He entered in about 1996–97, some 12 years after Karmarkar's 1984 LP paper, when interior methods were already "the rage" in LP, QP and convex programming (his words). He worked in parallel with Vanderbei–Shanno's LOQO (1999) and before Wächter–Biegler's IPOPT paper (2005/06). What set him apart was designing the method from SQP and trust-region ideas rather than extending QP. [stated + practice; timing comparison inferred]
6. **Machine learning: he entered against the ML consensus, and left with regrets.** Entry was 2009/10, pitching second-order and sampling methods against the view that "you can only use simple methods" (Purdue 2017). ML venues and ML talk titles stop after 2018. In 2026 he names two regrets:
   - not seeing "the balance between the statistical aspect of the problem and the geometry";
   - not moving into architectures.

   [stated + practice]
7. **Leaving a direction is rarely announced; the record just stops.**
   - Topics that end with no stated reason: inverse eigenvalue problems (1987), conic methods (1989), metacomputing/NEOS (2003), linear complementarity problems (LCPs) and finance (2013), ℓ1 methods (2016). Their reasons are nowhere stated.
   - Two exits come with a stated reason: the reduced-Hessian SQP line ("not considered the best thing now") and regression-based QN for noise ("we could never get to develop an algorithm that would scale up").

   [practice; reasons stated only where noted]
8. **Institutional turns track the research turns.** [practice, primary: CVs]
   - Engineering First curriculum and the Harris teaching professorship, 1997–2001;
   - Ziena co-founded 2001 (KNITRO);
   - Accenture consulting (2001–02), leading to a 2008 patent on debt-collection practices;
   - Google grants 2010–12 and consulting 2012–14;
   - move from EECS to IEMS, 2012/13, as department chair 2013–17;
   - noise-era funders: DARPA, NSF zero-order, AFOSR, ONR (2018–24).
9. **Last 12 months (2025-09-28 → 2026-09-28).**
   - One journal paper appeared: *ORL*, online 2025-12-10, from a 2024 preprint.
   - No new arXiv preprint (the last is Nov 2024).
   - One long interview (uploaded 2026-03-18). In it he says he is "taking a pause from writing research papers" to finish the third edition of *Numerical Optimization* with S. J. Wright, expected "in six months". He is also "very interested in generative AI", mainly its effect on education.
   - No third edition was found by 2026-09-28.

   [practice + stated]

---

## 1. Dated timeline

Source codes used in the table:
- CV18: `CV/cv_nocedal.pdf` on the old homepage (c. 2018; P).
- CVgh: the CV linked from `jnocedal.github.io` (c. 2022; P).
- CVmcc: the 2-page "Download CV" on the McCormick profile (current; P).
- BIO21: `Bio/bio-brief.pdf` (c. 2021; P).
- MGP: Mathematics Genealogy Project (S).
- I26: the 2026 "Subject to" interview (P, caption-derived).

| Date | Event | Evidence | Tag |
|---|---|---|---|
| 1950 or 1952 | Born, Mexico City | Interviewer: "you were born in Mexico in 1950" [0:00:38], answered "I was born and raised in Mexico City" [0:01:14] without correcting the year. Wikipedia infobox: 1952. See Contradictions. | [observed, secondary] |
| school years | German school in Mexico City, kindergarten to high school. High-school physics teacher gave an after-hours special-relativity course. | I26 [0:03:27], [0:19:43]–[0:20:16] | [stated, primary, caption-derived] |
| c. 1970–72 | During a 6-month delay of university start, joined the industrial-engineering department of a US manufacturer; made department manager "at the age of 19"; trained in Michigan. Worked days while studying for "almost two years". | I26 [0:24:13]–[0:26:26]. The same passage dates the US plant visit to "1977", which conflicts with the CV (see Contradictions). | [stated, primary, caption-derived] |
| 1970–1974 | B.Sc. Physics, UNAM | CV18, CVmcc | [practice, primary] |
| 1970–74 (undated within) | Intern at the UNAM astronomy institute (to get his home-built telescope mirror plated). Ran a Kodak lens-design optimization program on a PDP computer: "it was an optimization problem. It was a nonlinear continuous optimization problem … So it was my first exposure to that and to applied mathematics". Also told at RIIAA 2019 ("I've never stopped looking ahead of sation [ASR; sense: at optimization] since then just because of this telescope"). | I26 [0:32:08]–[0:33:13]; RIIAA 2019 [0:34:29] | [stated, primary, caption-derived] |
| 1974 | To Rice (Mathematical Sciences) on a Mexican fellowship. Recruited by the aeronautics professor "Angelo Mier" [ASR; the name is garbled and unverified]. Had admissions to Berkeley and Wisconsin; Imperial College's acceptance arrived too late. | I26 [0:34:49]–[0:36:32]; CV18 "1974-1978 Rice University, Ph.D." | [stated + practice, primary] |
| 1974 (after 6 months) | Changed advisor to Richard Tapia after the aeronautics advisor dismissed a Powell paper | I26 [0:38:12] (see §3, T1) | [stated, primary, caption-derived] |
| c. 1975–76 (undated) | Followed Tapia to Stanford for Tapia's sabbatical year and stayed on. Took Dantzig's PhD LP course and his reading seminar. | I26 [0:40:58], [0:44:23]–[0:45:29]. The year is not given. | [stated, primary, caption-derived] |
| 1978 | PhD, Rice. Thesis "On the Method of Conjugate Gradients for Function Minimization". | MGP id 43740; CV18 item 97 | [practice, primary + secondary] |
| 1978–1981 | Assistant Professor, UNAM (applied-math institute; CV item 95 is an IIMAS program-library guide, 1980). Wrote L-BFGS (published 1980). Worked on mechanics (with Gil Strang), inverse eigenvalue problems and derivative-free optimization. | CV18; I26 [0:49:26], [0:53:21] | [practice + stated] |
| 1980 | "Updating quasi-Newton matrices with limited storage", *Math. Comp.* 35, doi:10.1090/S0025-5718-1980-0572855-7 (solo) | Crossref | [practice, primary] |
| 1980–81 | NSF–CONACyT grant "Numerical Computations in Nonlinear Mechanics" | CV18 grants | [practice, primary] |
| 1981–1983 | Research Associate, Courant Institute, NYU. First constrained-optimization work (with M. Overton); inverse eigenvalue problems. | CV18; I26 [0:53:54]–[0:55:34]; Nocedal & Overton, *SINUM* 22 (1985), doi:10.1137/0722050 | [practice + stated] |
| 1983 | Joins Northwestern EECS as assistant professor, choosing it over an offer from Toronto CS | CV18; I26 [0:55:34]–[0:56:41] | [practice + stated] |
| June–July 1983 | Talks at Cambridge DAMTP ("Conic Methods for Optimization") and at Harwell; consulting for UKAEA Harwell in 1983 and 1988 | CV18 talks and consulting | [practice, primary] |
| 1987 | First Byrd–Nocedal paper: Byrd, Nocedal & Yuan, *SINUM* 24, doi:10.1137/0724077. DOE grant DE-FG02-87ER25047 begins; it is renewed at least to suffix A008 (2004–08). Visit to Toronto, where he met LeCun (by his account). | Crossref; CV18 grants; I26 [1:04:28] | [practice + stated] |
| 1989 | L-BFGS numerical study, Liu & Nocedal, *Math. Program.* 45, doi:10.1007/BF01589116. Plenary talk at the SIAM Optimization meeting, Boston (April). Associate Editor of *Math. Program.* 1989–2016. | Crossref; CV18 | [practice, primary] |
| 1990 | L-BFGS released as VA15 in the Harwell Library | CV18 "Published software" | [practice, primary] |
| 1991 | *SIAM J. Optim.* founded; he co-founded it (interviewer's framing) and was associate editor 1990–2014 (CVgh, CVmcc). Vol. 1 opens with Davidon's "Variable Metric Method for Minimization", doi:10.1137/0801001. | I26 [1:34:33]–[1:35:40]; Crossref | [practice + stated] |
| 1992 | Full professor (per the 01 note; not re-checked). "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1, doi:10.1017/S0962492900002270. | Crossref | [practice, primary] |
| 1992–1998 | Meteorology and climate grants: DOE "Optimization and Eigenvalue Computations with Application to Meteorology and Oceanography" (1992–95); Argonne "Climate Modeling on Parallel Computers" (1993–97); DOE "Large Scale Optimization and its Application to Weather Forecasting" (1995–98) | CV18 grants | [practice, primary] |
| 1995 / 1997 | L-BFGS-B: *SISC* 16 (1995), doi:10.1137/0916069; Algorithm 778, *ACM TOMS* 23 (1997), doi:10.1145/279232.279236 | Crossref | [practice, primary] |
| 1997 | First interior-point talks: "Interior Point Methods for Nonlinear Optimization", FoCM Rio (Jan 1997); "Interior Points vs Active Set Methods", Dundee (June 1997). NSF "Metacomputing Environments for Optimization", $1.8M, 1997–2000. | CV18 talks and grants | [practice, primary] |
| 1998 | ICM Berlin invited speaker; paper: Byrd & Nocedal, "Active set and interior methods for nonlinear optimization", *Documenta Math.* Extra Vol. ICM III (1998). Harris Professor of Teaching Excellence 1998–2001. | zbMATH record; CV18 | [practice + observed] |
| 1999 | *Numerical Optimization* (with S. J. Wright), Springer, doi:10.1007/b98874. Byrd, Hribar & Nocedal, *SIOPT* 9, doi:10.1137/S1052623497325107. | Crossref | [practice, primary] |
| 2001 | Co-founds Ziena Optimization and co-develops KNITRO; Accenture consulting 2001–02 | CV18; BIO21 | [practice, primary] |
| 2001-11-05 → 2008-07-22 | Patent US 7,403,923 "Debt collection practices" (filed 2001, granted 2008); inventors Elliott, O'Neill, Nocedal, Fourer; assignee Accenture Global Services | Google Patents record; CV18 "PATENT" | [practice, primary + secondary] |
| 2004 | ISI Highly Cited Researcher (Mathematics) | CV18 only | [practice, primary; not externally checked] |
| 2006 | KNITRO package paper, doi:10.1007/0-387-30065-1_4; 2nd edition of the book, doi:10.1007/978-0-387-40065-5 | Crossref | [practice, primary] |
| 2008 or 2009 | First contact from Google's speech group | I26 [1:21:43] "around 2008"; Purdue 2017 [0:03:32] "2009". See Contradictions. | [stated, primary, caption-derived] |
| c. 2009 | Nearly joins Google: "one of the VPs asked me to join … I think my wife said yes for about 12 hours and then changed" | I26 [1:22:50] | [stated, primary, caption-derived] |
| 2010 | SIAM Fellow; Charles Broyden Prize (for the 2009 geometry-phase paper, per the 01 note and the NSF bio). First ML talk: ICCOPT plenary, Aug 2010, "A Semi-Stochastic Method for Machine Learning". Google grant, Jan–Dec 2010. | CV18; BIO21 | [practice, primary] |
| 2010–2014 | Editor-in-Chief, *SIAM J. Optim.* | CV18, BIO21, CVmcc | [practice, primary] |
| 2011 | First ML paper: Byrd, Chin, Neveitt & Nocedal, *SIOPT* 21, doi:10.1137/10079923X | Crossref | [practice, primary] |
| 2012 | George B. Dantzig Prize | CV18; Wikipedia "Dantzig Prize" lists "2012: Jorge Nocedal, Laurence Wolsey" | [practice + observed] |
| 2012–2014 | Consulting for Google | CV18, CVmcc | [practice, primary] |
| 2012 → 2013 | EECS appointment ends in 2012; David and Karen Sachs Professor and Chair, IEMS, 2013–17 | CV18, CVmcc | [practice, primary] |
| 2014 or 2015 | Ziena role ends. Dates disagree: "2002-present Chief Scientist" (CV18); "2001-2014 Ziena" (BIO21); "2002-2015 Chief Scientist" (CVmcc). Artelys acquired Ziena "in 2015" (Wikipedia; no primary source found). | as listed | [practice + observed]; see Contradictions |
| 2016 (June) | "Optimization Methods for Large-Scale Machine Learning" with Bottou and Curtis, arXiv:1606.04838, published in *SIAM Rev.* 60 (2018), doi:10.1137/16M1080173 | arXiv; Crossref | [practice, primary] |
| 2017 | Walter P. Murphy Professor. INFORMS John von Neumann Theory Prize, shared with D. Goldfarb. Simons talk "Zero-Order Methods for Nonlinear Optimization" (Sept). | CV18; Wikipedia "John von Neumann Theory Prize" lists "2017 Donald Goldfarb and Jorge Nocedal" | [practice + observed] |
| 2018 (March) | First noisy derivative-free optimization (DFO) preprint, arXiv:1803.10173, published in *SIOPT* 29 (2019), doi:10.1137/18M1177718. DARPA "Optimization Methods for Stochastic Data-Driven Optimization", 2018–19. | arXiv; Crossref; CVgh | [practice, primary] |
| 2019 | Outstanding Engineering Alumnus Award, Rice | CVgh, CVmcc | [practice, primary] |
| 2020-02-20 | His team NU_Columbia_Artelys (Waltz, Bienstock, Nocedal) placed seventh in Challenge 1 of the ARPA-E Grid Optimization competition, "qualifying for the maximum prize money of $400,000" | Artelys news page | [observed, secondary] |
| 2020 | Elected to the US National Academy of Engineering | BIO21, CVmcc; Wikipedia | [practice + observed] |
| 2020–2024 | Noise-era grants: NSF "Zero-Order and Stochastic Methods for Nonlinear Optimization" (2020–23); AFOSR "Machine Learning and Physics Based Systems …" (2020–23); ONR "Stochastic Constrained Optimization" (2021–24) | CVgh grants | [practice, primary] |
| 2021 | Lagrange Prize in Continuous Optimization | BIO21, CVmcc (the citation was not read) | [practice, primary] |
| 2023 (Jan 9–13) | 12th US–Mexico Workshop on Optimization and its Applications, Huatulco. He is named as an organizer by the interviewer; the OSL page confirms the workshop and OSL sponsorship. | I26 [1:40:45]; OSL "Past Workshops" page | [observed + stated] |
| 2024 | SIAM John von Neumann Prize; lecture on 9 July at the SIAM Annual Meeting | CVmcc "2024 John Von Neumann Prize (SIAM)"; IDEAL Institute news 2024-05-02; Wikipedia "John von Neumann Prize" lists "2024: Jorge Nocedal"; WebSearch hit on the SIAM press release of 2024-04-02 (page not opened) | [practice + observed] |
| 2024 | DOE report "An Iterative Approach for Solving the SCOPF Problem Applying LP, SOCP, and NLP Subproblems", doi:10.2172/2404586 (OSTI) | Crossref | [practice, primary] |
| 2024-11-04 | Last arXiv preprint to date: Sun & Nocedal, "A Trust-Region Algorithm for Noisy Equality Constrained Optimization", arXiv:2411.02665 | arXiv listing, checked 2026-09-28 | [practice, primary] |
| 2025-05-02 | Lou, Sun & Nocedal, *SISC* 47, doi:10.1137/24M1632279 | Crossref; OpenAlex date | [practice, primary] |
| 2025-12-10 | Xuan & Nocedal, "A feasible method for constrained derivative-free optimization", *Oper. Res. Lett.* 65 (2026) 107398, doi:10.1016/j.orl.2025.107398 (preprint arXiv:2402.11920) | Crossref; OpenAlex | [practice, primary] |
| 2026-03-18 | "Subject to" interview uploaded (1:48:30). Book third edition in progress; pause from research papers; GenAI-and-education discussion groups. | I26 [1:45:19]–[1:45:51] | [stated, primary, caption-derived] |
| 2026 (current) | McCormick profile: Walter P. Murphy Professor of IEMS and (by courtesy) ESAM; Director, OSL. Still listed as active, not emeritus. | McCormick profile (© 2026) | [observed, primary institutional record] |

---

## 2. Lineage

### 2.1 Upward: formal and chosen

**Formal line** [practice, secondary: MGP pages read 2026-09-28]:

Gilbert Ames Bliss → Magnus R. Hestenes (Chicago, 1932) → Richard A. Tapia (UCLA, 1967; Advisor 1 Hestenes, Advisor 2 Charles B. Tompkins; thesis "A Generalization of Newton's Method with an Application to the Euler-Lagrange Equation") → Jorge Nocedal (Rice, 1978; thesis "On the Method of Conjugate Gradients for Function Minimization").

- Richard H. Byrd is Tapia's student too (Rice, 1976; MGP id 43741). So Nocedal's lifelong co-author is his academic sibling.
- Tapia has 35 students and 121 descendants in MGP; Hestenes has 36 and 269.
- **Continuity** [inferred]. Hestenes co-authored "Methods of conjugate gradients for solving linear systems" (Hestenes & Stiefel, *J. Res. NBS* 49, 1952, doi:10.6028/jres.049.044). Nocedal's thesis was on conjugate gradients two academic generations later.
  - Nocedal does not mention this link in any source I read.
  - He describes Tapia's supervision as light: "he did read my thesis and signed it but I did it pretty much on my own" (I26 [0:40:58]).
  - So the CG continuity is a genealogical fact, not a documented influence.

**Chosen line** (what he names as formative) [stated, primary]. Full treatment in `04-mentorship.md` §1; the dated anchors are:

| Figure | Role in the trajectory | When | Evidence |
|---|---|---|---|
| M. J. D. Powell | School of choice: "this combination of you do the analysis the algorithm then you write it in software was the Powell school and that's what it really appealed to me" | from 1974 (the Powell paper that ended his first advisorship) | I26 [0:39:18] |
| Richard Byrd | Peer "role model" at Rice; co-author 1987–2023 | from c. 1974 | I26 [0:41:33]; 2017 speech |
| George Dantzig | Model of "how you develop research": "not the best mathematician here by far but he is the most courageous" | Stanford year, c. 1975–76 | I26 [0:44:56] |
| Jorge Moré | As editor, pushed the 1980 L-BFGS paper through poor reviews | 1979–80 | I26 [0:50:32] |
| Don Goldfarb | Promoter. He introduced Nocedal to Powell (interview) and gave him a SIAM plenary slot (speech). | 1980s | I26 [0:52:48], [1:03:23]; 2017 speech |
| Michael Overton | Courant colleague; first constrained-optimization work | 1981–87 | CV18; I26 [0:54:28] |

### 2.2 Downward: students by era

[practice; MGP secondary, CVs and homepage primary]

- **Counts.** MGP lists **19 PhD students and 22 descendants**. The CVs and `jnocedal.github.io` list about 22 PhDs and 7 M.S. students, 1986–2023. Descendants in MGP: Curtis 2, Berahas 1.
- **Current students.** `jnocedal.github.io` lists Shigeng Sun and Yuchen Lou (co-advised). MGP already records Sun's PhD as 2024, so the page is out of date on this point.

The eras of the students' theses match the research eras. Titles are in `04-mentorship.md` §3.1.

| Student cohort | PhD years (MGP / CV) | Research era they carried |
|---|---|---|
| D. C. Liu; M. Lalee; P. Lu (MGP "Chen, Peihuang"); T. Plantenga | 1987–1994 | Limited memory, QN, trust region, large equality-constrained problems |
| M. B. Hribar; G. Liu; M. Marazzi; R. Waltz | 1995/96–2002 | Interior-point NLP (NITRO → KNITRO), DFO (Marazzi) |
| G. López-Calva; F. E. Curtis; L. Hei; Y. Wu | 2005/06–2010 | Penalty steering, inexact SQP, active-set / SLQP |
| G. Chin; S. Hansen; S. Solntsev; N. Keskar; A. Berahas; R. Bollapragada | 2013–2018/19 | Machine learning: sampling, stochastic QN, ℓ1, large batch |
| H.-J. M. Shi; Y. Xie; M. Q. Xuan; S. Sun (Y. Lou current) | 2021/22–2024 | Noise, finite-difference DFO, noisy trust region, constrained DFO |

**Reading** [inferred]:
- The student cohorts lag the research turns by about 3–5 years; the thesis completes after the topic is entered.
- The noise cohort (2021–24) was recruited while he was still in the ML phase (the first noise preprint is from March 2018). New directions are therefore started with the incoming cohort, not handed down to them.

---

## 3. Direction changes and what triggered them

Each turn gives the trigger in his words where one exists, the dated record, and a timing judgment. A turn with no stated trigger says so.

### T0. Physics → applied mathematics / optimization (c. 1972–74)
- **Trigger** [stated, caption-derived]:
  - The telescope internship and the Kodak lens-optimization code (I26 [0:32:40]–[0:33:13]).
  - Opportunity: "I started getting more interested in applied math even though my friends stayed in physics. I realized there were so many opportunities in applied math." (I26 [0:37:05])
  - The applications he made were deliberate: "in all these places I applied to mass [math] type departments at Berkeley and Wisconsin and at rice it was aerostautics [aeronautics]. It was going to be optimization based. So it was a very conscious decision." (I26 [0:37:05])
- **Kind of trigger**: a concrete application plus a hands-on computing experience. [inferred]

### T1. Aeronautics advisor → Tapia (1974)
- **Trigger** [stated, caption-derived, I26 [0:38:12]]: "this professor was kind of all doing the same thing. There was nothing really new. And the the last drop is that I received a paper that Mike Powell had written and I brought it to him and I told him this is really interesting and he told me this is not interesting at all. Right. And then I realized we don't have common common interests."
- **Kind of trigger**: disagreement over taste. He left over a judgment of what is interesting. [inferred]

### T2. Thesis programme → L-BFGS (1978)
- **Trigger** [stated, caption-derived]:
  - The failure of two years of thesis work: "all of them are a failure. None of them are elegant" [0:47:11].
  - A fresh start after a move, in the first month back in Mexico: "I went to the board and I realized I did the wrong thing in my thesis. All these methods are too complicated. This is not the way to do that." [0:50:00]
  - Then "some months there coding it, testing it" [0:50:32].
- **Record** [practice]:
  - Thesis 1978 (MGP).
  - The only 1977–84 *Math. Program.* paper in zbMATH is Nazareth & Nocedal, "Conjugate direction methods with variable storage", *Math. Program.* 23 (1982), doi:10.1007/BF01583797. This is probably the thesis-derived paper that he says "with the wrong ideas made it into math programming by accident" [0:47:44]. The identification is [inferred] from venue, date and topic; I did not read the paper.
  - L-BFGS: *Math. Comp.* 1980.
- **Timing against the field**: ahead of consensus. By his account the paper "didn't register very much", "started becoming popular among engineers", Powell "didn't like it", and LeCun's 1987 neural-network test failed ([0:51:38], [0:52:48], [1:04:28]) [stated]. It became his most-cited line only after the 1989 numerical study and the 1990 Harwell release (Crossref and OpenAlex counts in 01 §2.5) [practice]. The lag from idea to uptake was about 10 years. [inferred]

### T3. UNAM → Courant (1981): first constrained optimization; inverse eigenvalue problems
- **Trigger** [stated, caption-derived, I26 [0:53:54]–[0:54:28]]:
  - An offer from Courant;
  - personal reasons (his future wife lived in New York);
  - "I realized of course at that time that my research was not going very well. It's very difficult. uh the environment is you know the environment sometimes help you sometimes does not".
- **Record**:
  - Nocedal & Overton, *SINUM* 22 (1985), doi:10.1137/0722050 (projected-Hessian SQP);
  - Friedland, Nocedal & Overton, *SINUM* 24 (1987), doi:10.1137/0724043 (inverse eigenvalue problems).

  The inverse eigenvalue problem came from a physicist friend's nuclear-physics problem while he was at UNAM ([0:53:21]) [stated].
- **Exits**:
  - Inverse eigenvalue problems: last paper 1987 [practice]; no reason stated.
  - Reduced/projected-Hessian SQP: continued with Byrd and Biegler to 2000 (doi:10.1137/0805017, 1995; doi:10.1023/A:1008723031056, 2000), then dropped. In 2026 he judges these methods "not considered the best thing now" [0:55:34] [stated].
- **Kind of trigger**: a move of environment, where a new colleague brings a new problem class. [inferred]

### T4. Courant → Northwestern EECS (1983)
- **Trigger** [stated, I26 [0:55:34]–[0:56:41]]: no permanent position at Courant, and his wife's preferences (a big city; her sisters lived near Chicago). He would have preferred Toronto CS "because of professional ambition". Toronto tried to recruit him again in 1987 [1:04:28].
- **Consequence** [inferred]: a CS department (EECS) for 29 years. This matches his self-description as "just as much a computer scientist who likes to create software" (McCormick 2017 press quote, cited in 01).

### T5. Convergence theory of quasi-Newton methods with Byrd (1985–1994)
- **Trigger** [stated, caption-derived, I26 [0:57:15]]: "Mike Powell the great professor at Cambridge had written a paper after like 10-year effort he was able to prove convergence of the BFGS method … on convex problems it's a beautiful paper and so I decided to work on Richard Bird [Byrd] on exploring this more". The Powell paper is not identified in this run.
- **Record** [practice]:
  - talks: Oct 1985 "Analysis of Quasi-Newton Methods with Practical Line Searches"; April 1986 "Practical Convergence Results in Optimization"; April 1989 SIAM plenary "Practical Convergence Results for Nonlinear Programming Algorithms" (CV18);
  - papers: doi:10.1137/0724077 (1987); doi:10.1137/0726042 (1989); doi:10.1137/0802003 (CG, with Gilbert, 1992); *Acta Numerica* 1992.
- **Payoff he names**: "So that work gave us a lot of recognition because people like Powell and Dennis and so on said, "Oh, this is deep. This is deep work."" [0:57:49]–[0:58:26] [stated]. The 2017 speech credits the Goldfarb-arranged plenary with connecting him to Powell.
- **Kind of trigger**: a new result by another researcher (Powell) opens a question that a two-person team can extend. [inferred]

### T6. Weather forecasting and data assimilation (c. 1992–2009)
- **Trigger** [stated, I26 [1:15:39]]: "the reason why they contacted me is because by that time LBFGS was well known … and they said how can we use LBFGS here which by the way in the future this is also what led me into machine learning". His own answer was Gauss–Newton: "when the problem has a structure like a nonlinearly square structure, you have to exploit it" [1:16:12].
- **Record** [practice]:
  - grants 1992–98 (meteorology, climate modeling, weather forecasting) and NSF "Improved Minimization Techniques in Meteorological Data Assimilation" 2001–03 (CV18);
  - May 1993 plenary "Optimization Calculations with Applications to Meteorology and Oceanography" (CV18);
  - the single paper Fisher, Nocedal, Trémolet & Wright, *Optim. Eng.* 10 (2009), doi:10.1007/s11081-008-9051-5.
- **Weight**: he rates it his "most important contribution" [1:14:00] [stated]. See 01 SW6 for the contrast with its citation count.
- **Kind of trigger**: an external user brings a large application because of his software's reputation. [inferred]

### T7. Constrained NLP, interior-point methods and KNITRO (c. 1993–2014)
- **Trigger** [stated, caption-derived, I26 [1:16:44]–[1:17:49]]:
  - A deliberate programme: "I got interested then in developing algorithms for constraint optimization and I started working very um deliberately on different classes of problems, equality constraint problems and inequality and learning how to do them really slowly."
  - A belief about the field: "interior point methods had already been invented and there were the rage in linear programming and there were the rage in quadratic programming and convex programming … I thought well this is going to be straightforward the same people will apply them to nonlinear optimization and we're done well it turns out it's not so easy … in the non-convex case it doesn't work".
- **Record** [practice]:
  - Trust-region equality-constrained work first: Lalee, Nocedal & Plantenga, *SIOPT* 8 (1998), doi:10.1137/S1052623493262993. The DOI stem "93" suggests a 1993 submission [inferred].
  - Interior-point talks from Jan 1997 (CV18).
  - Byrd–Hribar–Nocedal 1999 and Byrd–Gilbert–Nocedal 2000 (doi:10.1007/PL00011391).
  - The Ziena/KNITRO chain 2001–06.
  - Penalty steering and inexact SQP 2005–10.
  - Infeasibility detection, last paper 2014 (CV18 item 20).
- **Timing against the field** [inferred from verified dates]:
  - Karmarkar's LP paper: *Combinatorica* 4 (1984), doi:10.1007/BF02579150.
  - Nocedal's first NLP interior-point talks and papers: 1997–99, about 12 years later. He entered after interior methods were the consensus in LP/QP/convex programming.
  - In NLP he was contemporaneous with Vanderbei & Shanno, *COAP* 13 (1999), doi:10.1023/A:1008677427361, which he says "finished first" ([1:18:21]–[1:18:55]).
  - He was earlier than Wächter & Biegler, *Math. Program.* 106 (issued 2005), doi:10.1007/s10107-004-0559-y.
  - His stated point of difference: "we were designing the elements from scratch using ideas from sequential quadratic programming" ([1:18:55]).
- **Why commercial** [stated, [1:19:29]]: "to continue to make it into a good code it had to become commercial. It couldn't stay in academia because we couldn't know who to fund it." Later "the code was sold to a French company called Artillis [Artelys] that keeps developing and it's thriving" ([1:20:00]).
- **Exit**: the constrained-NLP line thins out after 2010 and ends in 2014 [practice]. No reason is stated. It overlaps the ML entry for 2010–14 (§4).

### T8. Side lines of the 1995–2013 period (entered and left without stated reasons)

| Line | Dates | Evidence | Tag |
|---|---|---|---|
| Metacomputing / NEOS / grid | 1997–2003 | NSF $1.8M 1997–2000; Argonne NEOS grant 1997–98 (CV18); talk "Metacomputing Environments for Optimization", CERFACS 1998; "Solving optimization problems using parallel and grid computing", ENC 2003, doi:10.1109/ENC.2003.1232866 | [practice, primary]; exit reason not stated |
| Undergraduate curriculum (Engineering First) | 1997–2001 | CV item 58 (1997); Harris Professor of Teaching Excellence 1998–2001 | [practice, primary] |
| Industry analytics (Accenture, Synopsys, Chevron-Texaco, Deloitte workshop) | 1998–2007 | CV18 consulting; debt-collection patent (filed 2001); talk "Demand Optimization", Deloitte & Touche workshop, Feb 2007 | [practice, primary] |
| LCPs, options pricing, rigid bodies, games | 2007–2013 | Morales, Nocedal & Smelyanskiy, *Numer. Math.* 111 (2008), doi:10.1007/S00211-008-0183-5; Robinson, Feng, Nocedal & Pang, *SIOPT* 23 (2013), doi:10.1137/110845094; NSF "Market-Based Calibration of Pricing Models for Financial and Energy Option Contracts" 2010–13 | [practice, primary]; exit reason not stated |
| PDE-constrained optimization | 2001–2009 | NSF ITR "Optimization of Systems Governed by PDEs" 2002–05; talk "Inexact Newton Methods for PDE-Constrained Optimization", 2007 | [practice, primary] |
| Model-based DFO with geometry control | 2002–2009 | Wedge (2002); geometry phase, Fasano, Morales & Nocedal, *OMS* 24 (2009), doi:10.1080/10556780802409296 | [practice, primary]; reversed in T10 |

**Reading** [inferred]: in 2004–2013 the CV talk titles spread across many applications (finance, games, power markets at the Fields Institute in 2006, rigid bodies, computational chemistry at Berkeley in 2005). Several lines lasted one grant cycle and a handful of papers. The period looks exploratory. The next lasting turn (ML) came out of it through a practitioner's call, not through any of these lines.

### T9. Machine learning (2009/10–2019)
- **Trigger** [stated]:
  - The practitioner's call: Purdue 2017 [0:03:32] "So 2009, when I first got a call from the person at that time in charge of speech at Google". The 2026 interview dates it "around 2008" [1:21:43].
  - His contrarian first move: "How can we use LBFGS here? And my first thing is don't use LBFGS here" [1:22:16].
  - Long-standing sympathy: "I had followed what Yan Leon [LeCun] had done and the neural networks people and for some reason I always found it more interesting than logic based AI" [1:22:16].
  - The pitch to the field: "There is the idea that if the problem is so large, you can only use simple methods. I'm trying to motivate people to look at methods that are not like that." (Purdue 2017 [0:02:56]; caption-derived)
- **Record** [practice]:
  - First ML talk Aug 2010 (ICCOPT plenary); Nov 2010 talks at Google, IBM Watson and Georgia Tech (CV18).
  - First paper *SIOPT* 2011 (doi:10.1137/10079923X), then doi:10.1007/s10107-012-0572-5 (2012) and arXiv:1401.7020 → doi:10.1137/140954362.
  - ML venues (DBLP inproceedings records): NIPS 2012, ICASSP 2012, NIPS 2016, ICLR 2017 (arXiv:1609.04836), ICML 2018 (arXiv:1802.05374).
  - SIAM Review survey, arXiv:1606.04838.
  - Funding: Google 2010 and 2011–12; DOE "Statistical Learning …" 2011–14; ONR 2015–18; Intel 2016–18.
  - EECS → IEMS chair 2013.
- **Exit** [practice]:
  - The last ML-titled invited talks are Sept 2018 ("Nonlinear Optimization and Neural Networks", UC Davis) and Oct 2018 ("Nonlinear Optimization and Statistical Learning", Georgia Tech) (CVgh).
  - From March 2019 the talk titles are zero-order and noise (CVgh).
  - The last ML-venue paper is ICML 2018 (arXiv:1802.05374). The Newton-sketch study appeared in *OMS* in 2020 (doi:10.1080/10556788.2020.1725751) from a 2017 preprint.
  - He returned to talk about deep networks once, at NITMB in Oct 2024 ("How is it Possible to Train Deep Neural Networks?"; transcript saved by agent 02).
- **His retrospective on the exit** [stated, caption-derived, I26 [1:26:13]]: "a regret that I have is that in all these collaborations where eventually I was able to write a couple of papers that were influential in the field but other than that I wrote a number of papers I never understood that there had to be a balance between the statistical aspect of the problem and the geometry of the problem." Also [1:43:00]: "That took me also too long to understand that if you say I'm going to improve the training process, you can do it by different two different things. One of them is change the architecture so it's easier to optimize and the other one is just find a better optimization algorithm."
- **Timing against the field** [inferred]:
  - He entered after stochastic gradient (SG) methods were established in neural-network practice. By his own account, LeCun had found in 1987 that SG worked where L-BFGS did not.
  - He argued against that consensus (second-order and sampling methods), which puts his entry against the ML consensus rather than with it.
  - He left in 2018–19 while ML optimization was still growing. In 2026 he describes the prevailing adaptive methods ("Adam and so on") as "not satisfactory" [1:27:20]. So he left before the field's questions were settled, not after.
  - I did not measure when the optimization community at large entered ML, so "early" versus "late" relative to his peers is not established.

### T10. Optimization with noise and zero-order methods (2017/18–2025)
- **Triggers** [stated, caption-derived]. The emphasis shifts between talks (see Contradictions):
  - Simons, Sept 2017 [0:40:30]–[0:41:04]: dissatisfaction with interpolation-based DFO: "there are two things that always worried me. One of them is the cost and the concept of doing a model by interpolation. And the other one is whether it really could be done in a parallel way … Every time I see interpolation, I see my hands tied." And "I thought about this for two years. I realized the only way I know how to produce models that I can solve in Otime is with Quasi-Newton updating".
  - RIIAA, Aug 2019 [0:13:35]–[0:14:08]: an application need. For noisy function-value-only problems in the thousands of variables, "such an algorithm would be needed in reinforcement learning such an algorithm does not exist now".
  - UCLA, April 2021 [0:56:58]: "by the way our work is motivated by computational math right people are solving pdes or other simulations and inside those programs there's another simulation inside and that is not done exactly".
- **Enabling tools from others** [stated + practice]:
  - Moré & Wild's benchmarking paper (*SIOPT* 20, 2009, doi:10.1137/080724083): "a very important paper that demystified many methods" (UCLA [0:02:46]).
  - Their noise estimator (Moré & Wild, "Estimating Computational Noise", *SISC* 33, 2011, doi:10.1137/100786125): "in the noise estimation we use a procedure developed by more android [Moré and Wild] called easy noise [ECnoise]" (UCLA [0:33:23]).
  - The trigger here is a new *tool* made by others, plus his own long-running doubt about the interpolation paradigm. [inferred]
- **Abandoned inside the turn** [stated, UCLA [0:31:40]–[0:32:16]]: "we tried to do regression-based quasi-newton algorithms and we worked on that for quite a while and we could never get to develop an algorithm that would scale up and would have a limited memory version of it so we failed … going back to bfgs is the result of having tried everything we could". This repeats the 1978 pattern of exhausting the alternatives and then returning to quasi-Newton updating. [inferred link]
- **Reversal of his own 2009 position**: in 2009 he studied and trimmed model-based DFO (geometry phase). From 2018 he argued for finite differences (FD) against model-based methods (doi:10.1137/18M1177718; FD benchmark *OMS* 2023, doi:10.1080/10556788.2022.2121832). In 2024–25 he returned to a model-based method for the constrained case (doi:10.1016/j.orl.2025.107398). [practice; 01 Contradiction 9]
- **Record** [practice]:
  - BFGS with errors (*SIOPT* 30, 2020, doi:10.1137/19M1240794);
  - noise-tolerant QN (*SIOPT* 32, 2022, doi:10.1137/20M1373190);
  - constrained problems with noise (*SIOPT* 33, 2023, doi:10.1137/21M1450999);
  - noisy trust region (*Math. Program.* 202, 2023, doi:10.1007/s10107-023-01941-9);
  - adaptive sampling for constrained and composite problems (*IMA JNA* 44, doi:10.1093/imanum/drad020);
  - robust design (*SISC* 47, 2025);
  - noisy equality-constrained trust region (arXiv:2411.02665);
  - feasible constrained DFO (*ORL* 2026).
  - Grants DARPA 2018–19, NSF 2020–23, AFOSR 2020–23, ONR 2021–24 (CVgh).
- **Parallel applied thread (power grids)** [practice + observed]:
  - ARPA-E Grid Optimization Challenge 1, seventh place (Artelys news, 2020-02-20);
  - DOE SCOPF report (2024), which names "a non-convex, nonlinear interior-point solver, Artelys Knitro" (per 01).
- **Timing against the field** [inferred]: he entered after the noise-estimation and benchmarking tools existed (2009–2011). He then argued against the prevailing preference for model-based or direct-search DFO, so his entry positioned him as a contrarian to the DFO consensus.

### T11. Pause (2025–2026)
- **Stated** [I26 [1:45:19]–[1:45:51], caption-derived]: "Right now, I'm just working on the third edition of my book with Steve Wright. I'm taking a pause from writing research papers. I'm very interested in generative AI but I will see if I can have something to contribute there. I'm interested in the occasional [educational] aspect of it which at this point seems completely confusing how it's going to disrupt education and what are you going to do about this? So I've been organizing groups to discuss those questions and um in six months when the third edition of the book is finished we've added a lot of material since then I will see if I have something to contribute."
- **Consistent with the record** [practice]: no arXiv preprint after 2024-11-04; the 2025–26 journal items both come from 2024 preprints.
- **Book history as he tells it** [stated, [1:07:53]–[1:09:01]]: he wanted to write a book "just because I wanted to learn the subject well"; "the first edition took six years"; "we did a second edition fairly quickly within five years … And then for 17 years the book stayed and we're now doing the third edition". This matches the dates 1999 → 2006 [practice]. Seventeen years after 2006 is 2023, so work on the third edition apparently began around 2023. That date is my inference.

---

## 4. Topic × period matrix (entry and exit dates)

- **Source** [practice, primary]: the 96 numbered publications parsed from CV18 (1978–2018; one item was lost in text extraction), plus the 10 DBLP journal records from 2019–2026 that are not in the CV. Total 106.
- **Classification** [inferred]: I assigned each item to one topic from its title, keyword-first, and hand-corrected four items: steering penalty → constrained; the Waltz et al. interior algorithm → constrained; conic → QN; the 1994 survey → other.
- **Caveat**: ML-era and noise-era papers that *use* quasi-Newton updating are counted under ML or noise, not under QN.

| Period | QN / CG / unconstrained | Constrained NLP (SQP, IPM, penalty, active set) | Applications (eigenvalue, mechanics, weather, LCP, PDE, curriculum) | ML / stochastic / ℓ1 | Noise / DFO | Other | Total |
|---|---|---|---|---|---|---|---|
| 1975–79 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| 1980–84 | 3 | 0 | 3 | 0 | 0 | 0 | 6 |
| 1985–89 | 9 | 1 | 2 | 0 | 0 | 0 | 12 |
| 1990–94 | 9 | 1 | 0 | 0 | 0 | 1 | 11 |
| 1995–99 | 6 | 5 | 1 | 0 | 0 | 0 | 12 |
| 2000–04 | 5 | 7 | 1 | 0 | 1 | 0 | 14 |
| 2005–09 | 0 | 11 | 2 | 0 | 1 | 0 | 14 |
| 2010–14 | 0 | 6 | 2 | 5 | 0 | 0 | 13 |
| 2015–19 | 0 | 0 | 0 | 11 | 2 | 0 | 13 |
| 2020–24 | 0 | 0 | 0 | 1 | 6 | 0 | 7 |
| 2025–26 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |

**Patterns** [inferred from the matrix]:
- **Overlap-then-clean-exit.**
  - Constrained NLP and ML overlap for 2010–14; ML and noise overlap for 2017–20.
  - After each overlap the old topic stops completely: 0 constrained papers after 2014, 0 ML papers after 2020. He does not keep a residual stream in an old area.
  - Standalone QN/CG papers stop after 2004, but QN returns as the engine inside the ML and noise work.
- **Steady rate.** Output holds at 11–14 items per five years from 1985 to 2019, then halves (7 in 2020–24). That fits his stated "Two to three papers a year" [1:39:37] and the 2025–26 pause.
- **DFO is the longest intermittent line.** It runs as an interest at UNAM in 1978–81 (stated, [0:53:21]; no paper found), then 2002, 2009 and 2018–26. It is the only topic he left and came back to.

---

## 5. Entry and exit timing, compared with the field

All judgments here are [inferred]; the basis for each is in the last column.

| Topic | Entered | Relative to consensus at entry | Left | Relative to the field at exit | Basis |
|---|---|---|---|---|---|
| Limited-memory QN | 1978–80 | **Ahead**: the paper "didn't register"; reviews poor | never (it became a tool) | — | Stated reception [0:51:38]; citation take-off after 1989–90 (01 §2.5) |
| QN convergence theory | 1985–87 | **Following a lead**: extends Powell's proof | 1994 (Acta 1992 as summary) | Left once the tool was built; later criticised complexity theory for "lacking intuition" [1:29:02] | CV talk titles; Crossref dates |
| Reduced-Hessian SQP | 1981–85 | With the field (a current SQP topic) | 2000 | Left as the methods fell out of favour ("not considered the best thing now") | Stated [0:55:34]; last paper 2000 |
| NLP interior point | 1996–97 | **With the NLP wave, after the LP consensus**; parallel to LOQO | c. 2010–14 | Left as KNITRO went commercial and to Artelys | Karmarkar 1984; Vanderbei–Shanno 1999; Wächter–Biegler 2005; CV |
| Machine learning | 2009–10 | **Against the ML consensus** (SG) and in favour of second-order methods | 2018–19 | Left before the questions were settled; states regrets about the statistical and architectural sides | Purdue 2017 [0:02:56]; I26 [1:26:13], [1:43:00]; CVgh talk titles |
| Noise / zero-order | 2017–18 | **After the enabling tools** (Moré–Wild 2009/2011); **against the DFO preference** for interpolation models | 2024–25 (pause) | Paused with the book, not abandoned | Simons 2017; UCLA 2021; arXiv listing |

---

## 6. Era and resource context of each phase

This extends 01 §5 with the trajectory-specific points.

| Phase | Seniority and position | Resources that made the turn possible | Transferability warning [inferred] |
|---|---|---|---|
| 1978–81 (UNAM) | Newly minted PhD in a place he felt was "disconnected" | A blackboard and months of coding. "I had been disconnected and then this is where you realize their networks get get created" [1:03:23]. | L-BFGS was possible with almost no infrastructure; recognition was not. It needed Moré, Goldfarb and Powell. |
| 1981–95 (Courant → NU EECS) | Postdoc → full professor | Byrd as a constant co-author; a DOE grant renewed from 1987; Harwell and UKAEA contacts; workstation-scale testing | The Byrd partnership is person-specific. |
| 1995–2012 (NU EECS, Ziena) | Senior professor, start-up co-founder | NEOS/Argonne, the Optimization Technology Center (per 01), a commercial code base, postdocs (Morales, Orban), industry consulting | A commercial solver as a research platform is rarely available. |
| 2010–19 (NU IEMS, chair) | Chair and prize winner | Google and Intel access to data and compute; industry co-authors; students interning at companies (04 §3.6) | The ML turn depended on industrial access. |
| 2018–26 (NU IEMS, OSL director) | Very senior (NAE 2020; SIAM von Neumann 2024) | Defense and NSF funding for zero-order and stochastic methods; small 2–3-author papers with one student | This phase is the most transferable: laptop-scale experiments on CUTEst-type problems with added noise (see 03). |

---

## 7. Latest activity (last 12 months: 2025-09-28 → 2026-09-28)

| Date | Item | Evidence | Tag |
|---|---|---|---|
| 2025-12-10 (online) | Xuan & Nocedal, "A feasible method for constrained derivative-free optimization", *Oper. Res. Lett.* 65 (2026) 107398, doi:10.1016/j.orl.2025.107398. Preprint arXiv:2402.11920 (Feb 2024). | OpenAlex publication date; Crossref | [practice, primary] |
| 2026-03-18 (upload) | "Subject to: Jorge Nocedal", 1:48:30 interview (https://www.youtube.com/watch?v=CfR-llfmb6E): life history, book, KNITRO, ML regrets, plans | Transcript `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt` | [stated, primary, caption-derived] |
| during 2025 (stated in 2026) | Created a new course: "I always feel like creating new courses. Don't stay with the same course. Even last year a new course." | I26 [1:30:40] | [stated, primary, caption-derived]; the course was not identified |
| 2025–26 (stated) | Organizing discussion groups on generative AI and education | I26 [1:45:51] | [stated, primary, caption-derived]; no external trace found |
| 2025–26 (stated) | Third edition of *Numerical Optimization* in progress, "in six months when the third edition of the book is finished" (said in an interview uploaded 2026-03-18) | I26 [1:45:51]. WebSearch on 2026-09-28 found only the 2nd edition listed. | [stated]; publication **not observed** |
| 2025-10-31, 2026-01-16 | OSL seminars (Y. Cui; X. Yuan). The center he directs remains active; his own role in these events is not stated. | OSL "Seminars and Tutorials" page | [observed, primary institutional record] |
| checked 2026-09-28 | **No arXiv preprint since 2024-11-04**; no DBLP or OpenAlex record dated after 2025-12-10; no YouTube talk uploaded in the window other than the interview (search sorted by upload date) | arXiv author listing; DBLP SPARQL (83 records); OpenAlex; YouTube search | [practice, primary + secondary] |
| current | Homepage `jnocedal.github.io` still lists Shigeng Sun and Yuchen Lou as current students | Homepage | [practice, primary]; Sun's PhD is dated 2024 by MGP |

Just outside the window: *SISC* robust-design paper (2025-05-02); the Midwest Optimization & Statistical Learning workshop hosted by OSL (2025-05-16); upload of the Oct 2024 NITMB talk (2025-07-18).

---

## 8. Failures, abandoned directions and reversals in the trajectory

Consolidated from the turns above, with cross-references to 01 §4, 02 §9 and 03 §5.

| Item | Date | What happened | Tag |
|---|---|---|---|
| Thesis programme (CG-style extensions of QN) | 1976–78 | "a impressive collection of failed ideas" [0:47:11]; replaced by L-BFGS | [stated, primary, caption-derived] |
| L-BFGS reception | 1980–c. 1989 | Poor reviews; saved by the editor (Moré); Powell disliked it; LeCun's 1987 test failed | [stated] |
| UNAM research environment | 1978–81 | "my research was not going very well" → left for Courant | [stated] |
| Reduced-Hessian SQP (with Overton, Byrd, Biegler) | 1983–2000 | Dropped; "not considered the best thing now" | [stated + practice] |
| Nearly left academia for Google | c. 2009 | Declined because of family | [stated] |
| ML programme | 2010–19 | Two regrets stated: the statistics/geometry balance and architectures | [stated] |
| Large-batch / sharp-minima claim | 2016–17 | Contested by Dinh, Pascanu, Bengio & Bengio, arXiv:1703.04933 ("Sharp Minima Can Generalize For Deep Nets") | [observed, secondary]; see 01 §4.5, 03 §4.1 |
| Regression-based QN for noisy problems | c. 2017–20 | "we could never get to develop an algorithm that would scale up" | [stated]; no paper trace (03 §5) |
| Geometry phase (2009) → finite differences (2018+) → model-based again (2024) | 2009–2024 | Reversal and partial return on DFO method choice | [practice] |
| Unmet expectation for the book | 1999 | "we thought, well, maybe this book will be known for five years or so. uh maybe we'll send two sell 2,000 copies" [1:08:27] (ASR; the sense is "sell 2,000 copies") | [stated] |
| Rejected or retracted papers | — | **None found** in any public record | Gap |

---

## Contradictions (kept, not reconciled)

1. **Birth year.** The interviewer says "you were born in Mexico in 1950" (I26 [0:00:38]) and Nocedal does not correct it. Wikipedia's infobox and category say 1952. No primary document with a birth date was found.
2. **Factory year.** In I26 [0:25:51] he describes seeing "a factory in the US in 1977 car manufacturing plant" during his UNAM-era job. The CVs place him at Rice in 1974–78 and at UNAM in 1970–74. This is either an ASR error, a slip of memory (he warns "my memory tends to really distort things" [0:46:03]) or a different visit. Not resolved.
3. **First contact from Google.** "So 2009, when I first got a call from the person at that time in charge of speech at Google" (Purdue 2017 [0:03:32]) versus "I was contacted by Google around 2008, something like that, about 2008" (I26 [1:21:43]). The first Google grant in the CV starts Jan 2010.
4. **How he was connected to Powell.**
   - The 2017 speech: a SIAM plenary lecture arranged by Goldfarb "proved to be decisive as it connected me with Mike Powell".
   - The 2026 interview: "The first time I met Mike Powell, Don Garb [Goldfarb] said, 'Go and introduce him'" [0:52:48], in the L-BFGS context. The close relationship began later with a day in Cambridge after a stay at Harwell [1:02:17].
   - CV18 dates a Cambridge DAMTP talk to June 1983 and the only SIAM optimization plenary listed to April 1989.

   The three accounts do not fix one sequence.
5. **Ziena and Artelys dates.**
   - CV18: "2002-present Chief Scientist, Ziena"; consulting "2012-present Artelys; 2001-2012 Ziena".
   - BIO21: "2014-present Artelys Corp; 2001-2014 Ziena".
   - CVmcc and CVgh: "2002-2015 Chief Scientist"; "2012-2020 Artelys".
   - Wikipedia: Ziena "bought by Artelys in 2015".
6. **Editorial record differs across CV versions.** CV18 lists "1991-1995 Associate Editor, Mathematics of Computation" and no *SIOPT* associate editorship. CVgh and CVmcc list "1990- 2014 Associate Editor, SIAM Journal on Optimization" and drop the *Math. Comp.* line.
7. **Student years differ by source.**
   - Shi and Xie: "(exp) 2020" (CV18), "2021" (CVgh), "2022" (homepage).
   - Bollapragada: 2019 (CV18 "exp", CVgh, MGP) versus 2018 (homepage).
   - Sun: "2024 (exp)" (CVgh), 2024 (MGP), yet "Current Students" on the homepage.
8. **The stated motivation for the noise programme shifts by audience and year.**
   - 2017: the cost and non-parallelism of interpolation models.
   - 2019: reinforcement learning.
   - 2021: inexact inner simulations in computational science.
   - 2024–25: robust engineering design (paper title).
   - Also 2021, from the same talk: "we don't have good applications" [0:56:58], which sits oddly beside the application-led framing of 2019.
9. **When he "entered" constrained optimization.** The interview places it at Courant in 1981–83 ("That was the first time that I actually worked on constraint problems" [0:55:01]). It also presents constrained optimization as a deliberate new programme begun after the 1990s weather work ("I got interested then in developing algorithms for constraint optimization" [1:16:44]). The publication record supports both a 1985 start (SQP) and a mid-1990s re-entry (interior point, trust region).
10. **Self-description of research motivation, old versus new homepage.**
    - The old EECS page (footer "Last modified: February 1, 2008", yet it advertises the 2016 SIAM Review article): research motivated by "image and speech recognition, recommendation systems, and search engines".
    - The new `jnocedal.github.io`: "weather forecasting, engineering design and machine learning", with a new concern to "decrease energy demands" of training.

    Both are current web pages.
11. **Theory versus computation over the career.** In 1992 he called for more work on "global efficiency" (01 Contradiction 10). In 2026 he says the field "has gone really really theoretical" and "the computational side of it … used to be the core now it's a smaller field" [1:29:02]–[1:29:35]. His own trajectory moved from theory-heavy (1985–94) to computation- and software-heavy (1995–2025).

## Gaps

1. **Google Scholar** not attempted: 01 found it bot-blocked in this run. No Scholar-only items or recent Scholar entries were checked.
2. **Prize citations not read.** The SIAM pages (von Neumann, Dantzig, Lagrange) returned HTTP 403 to curl and WebFetch. The 2024 SIAM press release was seen only as a WebSearch hit, and the GlobeNewswire copy failed to load. The NAE 2020 citation was not found. Prize facts rest on Nocedal's CVs (primary) plus Wikipedia prize lists and the IDEAL repost (secondary).
3. **Ziena → Artelys sale date**: no primary source (Artelys "about" and KNITRO pages did not mention Ziena).
4. **Founding date of OSL** and of the earlier "Optimization Center" / Optimization Technology Center: not found.
5. **Why he left EECS for IEMS (2012/13)**: no statement found. The same goes for why each side line of T8 was dropped, and why the constrained-NLP line stopped in 2014.
6. **Undated early events**: the Stanford year (c. 1975–76), the Harwell stay that preceded the Cambridge day with Powell, and the Argonne sabbaticals where he met S. J. Wright (the first edition's six-year writing period implies a start around 1993; inferred).
7. **The Powell BFGS paper** that triggered T5 (he dates it "1975 … eventually published in 76", [0:38:44]) is not identified with an identifier in this run.
8. **The thesis-derived *Math. Program.* paper**: identified only by inference as Nazareth & Nocedal 1982 (doi:10.1007/BF01583797); not read.
9. **Third edition status**: no announcement found (WebSearch, 2026-09-28). Whether it has appeared or slipped is unknown.
10. **Last 12 months**: 2025–26 conference programmes (e.g., INFORMS 2025, ICCOPT/ISMP) were not checked for talks. The GenAI discussion groups and the new 2025 course have no external trace. Whether he is taking new PhD students is unknown.
11. **Rejected papers, withdrawn directions and referee reports**: none found for any period.
12. **The field-wide timing** of the optimization community's entry into ML (to place his 2009/10 entry as early or late relative to peers) was not measured.

## Sources

Retrieval date for all: 2026-09-28. P = primary, S = secondary.

**Nocedal's own documents and pages**
1. J. Nocedal, Curriculum Vitae (c. 2018, 17 pp.) — http://www.ece.northwestern.edu/~nocedal/CV/cv_nocedal.pdf — P
2. J. Nocedal, brief CV/bio (c. 2021) — http://www.ece.northwestern.edu/~nocedal/Bio/bio-brief.pdf — P
3. J. Nocedal, Curriculum Vitae (c. 2022, 17 pp.) linked from the new homepage — https://github.com/jnocedal/jnocedal.github.io/blob/0e7c39c0a226f3ad09a26f53741305da6d6e4e25/cv_nocedal.pdf — P
4. J. Nocedal, 2-page CV ("Download CV" on the McCormick profile; lists the 2024 SIAM prize) — https://ar.mccormick.northwestern.edu/services/profiles/482/curriculum_vitae — P
5. J. Nocedal, homepage (research statement, current and former students) — https://jnocedal.github.io — P
6. J. Nocedal, old EECS homepage — http://www.ece.northwestern.edu/~nocedal/ — P
7. Northwestern Engineering faculty profile "Nocedal, Jorge" (© 2026) — https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/nocedal-jorge.html — P (institutional record)
8. "Subject to: Jorge Nocedal", interview, YouTube, uploaded 2026-03-18 — https://www.youtube.com/watch?v=CfR-llfmb6E — transcript `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt` — P (caption-derived)
9. J. Nocedal, "Nonlinear Optimization Methods for Machine Learning", Purdue IE Distinguished Seminar, 2017-02-15 — https://www.youtube.com/watch?v=srg3Rx2HvfQ — transcript `../sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt` — P (caption-derived)
10. J. Nocedal, "Zero-order and Dynamic Sampling Methods for Nonlinear Optimization", Simons Institute, 2017 — https://www.youtube.com/watch?v=OfVZ9gArXiY — transcript `../sources/talks/2017_simons-zero-order-dynamic-sampling_OfVZ9gArXiY.txt` — P (caption-derived)
11. J. Nocedal, RIIAA 2.0 keynote, Mexico City, Aug 2019 — https://www.youtube.com/watch?v=3zUD3H71HQ0 — transcript `../sources/talks/2019-08_riiaa2-keynote_3zUD3H71HQ0.txt` — P (caption-derived)
12. J. Nocedal, UCLA CS201 seminar, 2021-04-08 — https://www.youtube.com/watch?v=4a12aV77CAI — transcript `../sources/talks/2021-04-08_ucla-cs201-seminar_4a12aV77CAI.txt` — P (caption-derived)
13. J. Nocedal, "How is it Possible to Train Deep Neural Networks?", NITMB seminar, 2024-10-25 — https://www.youtube.com/watch?v=XrX7MEMbdYw — transcript `../sources/talks/2024-10-25_nitmb-seminar-train-dnns_XrX7MEMbdYw.txt` (keyword search only) — P (caption-derived)
14. J. Nocedal, 2017 John von Neumann Theory Prize acceptance speech (notes with verbatim excerpts) — `../sources/talks/2017-von-neumann-prize-acceptance-speech.md`; original http://www.ece.northwestern.edu/~nocedal/PDFfiles/VonNeumann_Speech.pdf — P
15. arXiv author listing "Nocedal, Jorge" (21 preprints, newest 2411.02665) — https://arxiv.org/search/?query=Nocedal%2C+Jorge&searchtype=author — P
16. arXiv abstract pages 1606.04838, 1609.04836, 1803.10173, 2401.15007, 1401.7020 and (third party) 1703.04933 — https://arxiv.org/abs/<id> — P (third-party page S)

**Databases and third-party records**
17. Crossref REST API, metadata for 60 DOIs queried (47 cited in this file) — https://api.crossref.org — S
18. DBLP SPARQL via `scripts/dblp_works.py --pid n/JorgeNocedal` (83 records, 1979–2026) — https://dblp.org/pid/n/JorgeNocedal.html — S
19. OpenAlex, works of author A5081856145 from 2024-09-01 — https://api.openalex.org — S
20. Mathematics Genealogy Project, Jorge Nocedal (id 43740) — https://mathgenealogy.org/id.php?id=43740 — S
21. Mathematics Genealogy Project, Richard Alfred Tapia (id 14920) — https://mathgenealogy.org/id.php?id=14920 — S
22. Mathematics Genealogy Project, Magnus Rudolph Hestenes (id 6174) — https://mathgenealogy.org/id.php?id=6174 — S
23. zbMATH Open API, documents by Nocedal 1977–1984 and 1998 (ICM paper in *Doc. Math.* Extra Vol.) — https://api.zbmath.org — S
24. Google Patents, US 7,403,923 B2 "Debt collection practices" (filed 2001-11-05, granted 2008-07-22) — https://patents.google.com/patent/US7403923B2/en — S
25. Wikipedia, "Jorge Nocedal" (raw wikitext) — https://en.wikipedia.org/wiki/Jorge_Nocedal — S
26. Wikipedia, "Dantzig Prize" — https://en.wikipedia.org/wiki/Dantzig_Prize — S
27. Wikipedia, "John von Neumann Theory Prize" — https://en.wikipedia.org/wiki/John_von_Neumann_Theory_Prize — S
28. Wikipedia, "John von Neumann Prize" (SIAM) — https://en.wikipedia.org/wiki/John_von_Neumann_Prize — S
29. IDEAL Institute, "Jorge Nocedal Awarded John von Neumann Prize by the Society for Industrial and Applied Mathematics", 2024-05-02 — https://www.ideal-institute.org/2024/05/02/jorge-nocedal-awarded-john-von-neumann-prize/ — S
30. WebSearch results for the 2024 SIAM prize, incl. the SIAM/GlobeNewswire release "Jorge Nocedal is the 2024 SIAM John von Neumann Prize Lecturer", 2024-04-02 (page itself not loaded) — https://www.globenewswire.com/news-release/2024/04/02/2856361/0/en/Jorge-Nocedal-is-the-2024-SIAM-John-von-Neumann-Prize-Lecturer.html — S
31. Artelys, news page, item "Artelys amongst the top ten finalists of the ARPA-E Grid Optimization Competition", 2020-02-20 — https://www.artelys.com/news/ — S
32. Northwestern Center for Optimization and Statistical Learning pages (home, news, past workshops, seminars) — https://www.mccormick.northwestern.edu/research/optimization-machine-learning-center/ — S (institutional)
33. YouTube search "Jorge Nocedal" sorted by upload date (20 results; only the 2026 interview is within the window) — https://www.youtube.com/results?search_query=%22Jorge+Nocedal%22&sp=CAI%253D — S. A second WebSearch ("Nocedal Wright Numerical Optimization third edition 2026") returned only 2nd-edition listings; it is counted here with the search results, not as a separate source.

**Papers cited above for dating** (identifier checked with Crossref, arXiv or zbMATH in this run; listed by identifier in the text): doi:10.1007/BF02246561; 10.1090/S0025-5718-1980-0572855-7; 10.1007/BF01583797; 10.1137/0722050; 10.1137/0724077; 10.1137/0724043; 10.1137/0726042; 10.1007/BF01589116; 10.1017/S0962492900002270; 10.1137/0802003; 10.1137/0916069; 10.1145/279232.279236; 10.1137/S1052623493262993; 10.1137/S1052623497325107; 10.1007/b98874; 10.1007/PL00011391; 10.1137/0805017; 10.1023/A:1008723031056; 10.1109/ENC.2003.1232866; 10.1007/0-387-30065-1_4; 10.1007/978-0-387-40065-5; 10.1007/S00211-008-0183-5; 10.1137/110845094; 10.1080/10556780802409296; 10.1007/s11081-008-9051-5; 10.1137/10079923X; 10.1007/s10107-012-0572-5; 10.1137/140954362; 10.1137/16M1080173; 10.1080/10556788.2020.1725751; 10.1137/18M1177718; 10.1137/19M1240794; 10.1137/20M1373190; 10.1080/10556788.2022.2121832; 10.1137/21M1450999; 10.1007/s10107-023-01941-9; 10.1093/imanum/drad020; 10.1137/24M1632279; 10.1016/j.orl.2025.107398; 10.2172/2404586; arXiv:1606.04838; 1609.04836; 1401.7020; 1802.05374; 1803.10173; 2402.11920; 2411.02665; Byrd & Nocedal, "Active set and interior methods for nonlinear optimization", *Documenta Math.* Extra Vol. ICM III (1998) (zbMATH). Third-party works used for timing: Hestenes & Stiefel 1952, doi:10.6028/jres.049.044; Karmarkar 1984, doi:10.1007/BF02579150; Davidon 1991, doi:10.1137/0801001; Vanderbei & Shanno 1999, doi:10.1023/A:1008677427361; Wächter & Biegler 2005/06, doi:10.1007/s10107-004-0559-y; Moré & Wild 2009, doi:10.1137/080724083; Moré & Wild 2011, doi:10.1137/100786125; Dinh et al. 2017, arXiv:1703.04933.
