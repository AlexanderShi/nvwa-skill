# 04 · Students and collaborators (how Wächter supervised, and what his group knew)

- **Researcher:** Andreas Wächter (also written Waechter / Wachter). PhD in Chemical Engineering at Carnegie Mellon (1997–2002, advisor L. T. Biegler). IBM T. J. Watson Research Center (2002–2011). Northwestern University IEMS (2011 on; Professor from 2019). His homepage is now frozen with the note "I moved to Gurobi Optimization. This webpage is no longer maintained."
- **Dimension:** Agent 04: students and collaborators. Covers supervision style, group habits, lab culture and tacit knowledge.
- **Research date:** 2026-09-28
- **Sources consulted:** 33 documents.
  - 4 are primary (his own or co-maintained text): the thesis acknowledgments, the homepage "Students" page, the Ipopt documentation and the Ipopt `AUTHORS` file.
  - 15 are PhD theses by his advisees and colleagues (14 name him in their acknowledgments; Peña-Ordieres's has no acknowledgments section). I read the front matter of each, and in 6 of them also the experimental sections.
  - 5 more theses were checked and do not mention him.
  - 6 are institutional or third-party pages.
  - 3 could not be read (HTTP 403, 403, 401).
  - WebSearch was used 2 times. Everything else came from curl or WebFetch on known URLs, the Northwestern "Arch" repository, the CMU KiltHub/figshare API and the Crossref API.
- **User-supplied material:** none. `references/sources/papers|talks|essays|software` hold only `.gitkeep`, and `private/` was not opened.

**What kind of evidence this is.** No student blog post, lab guide, onboarding document, interview, Festschrift contribution or memoir about Wächter as a supervisor turned up. Two WebSearch calls aimed at such material found none. The evidence therefore comes from three places:

1. **Dissertation acknowledgments.** These are formal, public and written at graduation. Acknowledgments are a genre that praises by default, so their praise carries little information on its own. What carries information is where students **differ** from one another: which traits they single out, and what they say went wrong.
2. **The experimental sections of his advisees' dissertations.** These are the group's working habits as the students actually practised them.
3. **Ipopt's public project files.** These show how he organised collaborators and contributors.

Nothing here is his own statement about how he supervises. See 02-methodology, which records the same gap.

**Tags.**
- **[stated]**: Wächter said or wrote it.
- **[stated-joint]**: a text he co-authored or co-maintains.
- **[practice]**: what was done, as recorded in theses, papers, code or records.
- **[observed]**: what others said about him.
- **[inferred]**: this agent's reading.
- **P / S**: primary / secondary.

Every student recollection below is **secondary** evidence about Wächter, even though it is a first-hand text by the student.

**Page references** are printed page numbers; in every Northwestern thesis cited here the printed page equals the PDF page. Quotes were copied from the PDF text layer (pypdf). Where the text layer lost characters (apostrophes in Keskar 2017; letter spacing in Wächter's 2002 bitmap-font thesis), this is noted at the quote.

---

## A. Who his students and close collaborators were (verified roster)

### A.1 Advisees: three records compared

| Student | Wächter homepage "Students" page [stated, P] | IEMS "PhD Graduates (2000 on)" list [S, institutional] | The student's own thesis (Arch) [observed, S] |
|---|---|---|---|
| Travis Johnson | former | **not listed** | not found in Arch (**not read**) |
| Mingbin (Ben) Feng | co-advised with Jeremy Staum | Fall 2016, advisor **Jeremy Staum** only | Staum is "my advisor"; Wächter is a committee member (p. 5) |
| Nitish S. Keskar | co-advised with Jorge Nocedal | Spring 2017, advisor **Wächter** only | "two excellent advisors", Wächter and Nocedal (p. 6) |
| Francisco Jara-Moroni | former | Summer 2018, Wächter | "my advisor Andreas Wächter" (p. 6) |
| Alejandra Peña-Ordieres | former | Summer 2020, Wächter ("Wäcther", sic) | thesis has **no acknowledgments section** |
| Mark Semelhago | co-advised with Barry Nelson and Eunhye Song | Fall 2020, Nelson, Song, Wächter | "my advising team … Nelson, Andreas Wächter and Eunhye Song" (p. 6) |
| Shenyinying (Ruby) Tu | co-advised with Ermin Wei | Summer 2021, Wächter and Wei; thesis "Two-Stage Decomposition Algorithms and Their Application to Optimal Power Flow Problems" | not found in Arch (**not read**) |
| Xinyi Luo | former | Summer 2023, Wächter | "my supervisor Professor Andreas Wächter" (p. 5) |
| Niloufar Izadinia | former | Fall 2023, Wächter (spelled "Izandinia") | "my advisor Professor Andreas Wächter" (p. 5) |
| Shima Dezfulian | former | Summer 2024, Wächter; thesis "Practical Algorithms for Derivative-Free and Noisy Nonlinear Optimization" | not found in Arch (**not read**) |
| Harun Avci | **not listed** | Summer 2024, advisor **Barry Nelson** only | "my advisors Professors Barry L. Nelson, Andreas Wächter, and Eunhye Song" (p. 5) |
| Yuchen Lou | current (co-advised with Ermin Wei) | not in the list | not applicable. Current status **not found** (the IEMS current-students page loads by script and could not be read) |

The three records disagree for Feng, Keskar, Avci and Johnson. This is kept as a contradiction in §G. Co-advising runs through half the roster: with Nocedal (optimization), Staum and Nelson/Song (simulation), and Wei (electrical engineering, power systems) [practice].

### A.2 Papers with advisees and near-advisees

Identifiers were checked against Crossref or arXiv in this run. I read only the corresponding thesis chapters, not the papers.

| Student | Paper (identifier) | Author order |
|---|---|---|
| Johnson | Curtis, Johnson, Robinson, Wächter, "An Inexact Sequential Quadratic Optimization Algorithm for Nonlinear Optimization", *SIAM J. Optim.* 2014, DOI 10.1137/130918320 | alphabetical |
| Johnson | Johnson, Kirches, Wächter, "An Active-Set Method for Quadratic Programming Based On Sequential Hot-Starts", *SIAM J. Optim.* 2015, DOI 10.1137/130940384 | alphabetical |
| Feng | Feng, Wächter, Staum, "Practical algorithms for value-at-risk portfolio optimization problems", *Quant. Finance Lett.* 2015, DOI 10.1080/21649502.2014.995214 | student first |
| Feng | Feng, Maggiar, Staum, Wachter, "Uniform convergence of sample average approximation with adaptive multiple importance sampling", WSC 2018, DOI 10.1109/WSC.2018.8632370 | student first |
| Keskar | Keskar, Nocedal, Öztoprak, Wächter, "A second-order method for convex ℓ1-regularized optimization with active-set prediction", *Optim. Methods Softw.* 2016, DOI 10.1080/10556788.2016.1138222 | |
| Keskar | Keskar, Wächter, "A limited-memory quasi-Newton algorithm for bound-constrained non-smooth optimization", *Optim. Methods Softw.*, DOI 10.1080/10556788.2017.1378652 (Crossref "issued" 2017) | student + advisor only |
| Jara-Moroni | Jara-Moroni, Pang, Wächter, "A study of the difference-of-convex approach for solving linear programs with complementarity constraints", *Math. Program.*, DOI 10.1007/s10107-017-1208-6 | |
| Jara-Moroni | Jara-Moroni, Mitchell, Pang, Wächter, "An enhanced logical benders approach for linear programs with complementarity constraints", *J. Glob. Optim.* 2020, DOI 10.1007/s10898-020-00905-z | |
| Peña-Ordieres | Peña-Ordieres, Luedtke, Wächter, "Solving Chance-Constrained Problems via a Smooth Sample-Based Nonlinear Approximation", *SIAM J. Optim.* 2020, DOI 10.1137/19M1261985 | |
| Semelhago | Semelhago, Nelson, Wachter, Song, "Computational methods for optimization via simulation using Gaussian Markov Random Fields", WSC 2017, DOI 10.1109/WSC.2017.8247941 | |
| Semelhago | Semelhago, Nelson, Song, Wächter, "Rapid Discrete Optimization via Simulation with Gaussian Markov Random Fields", *INFORMS J. Comput.* 2021, DOI 10.1287/ijoc.2020.0971 | |
| Tu | Tu, Wachter, Wei, "A Two-Stage Decomposition Approach for AC Optimal Power Flow", *IEEE Trans. Power Syst.* 2021, DOI 10.1109/TPWRS.2020.3002189 | |
| Luo | Luo, Wächter, "A Quadratically Convergent Sequential Programming Method for Second-Order Cone Programs Capable of Warm Starts", *SIAM J. Optim.* 2024, DOI 10.1137/22M1507681 | student + advisor only |
| Lou, Luo | Lou, Luo, Wächter, Wei, "A Decomposition Framework for Nonlinear Nonconvex Two-Stage Optimization", *SIAM J. Optim.* 2026, DOI 10.1137/25M1728661 | |
| Izadinia | Izadinia et al. (11 authors, Wächter last), "A versatile optimization framework for sustainable post-disaster building reconstruction", *Optim. Eng.* 2022, DOI 10.1007/s11081-022-09766-9 | |
| Dezfulian | Curtis, Dezfulian, Waechter, "An Interior-Point Algorithm for Continuous Nonlinearly Constrained Optimization with Noisy Function and Derivative Evaluations", arXiv:2502.11302 (16 Feb 2025) | |
| Maggiar (not his advisee) | Maggiar, Wächter, Dolinskaya, Staum, "A Derivative-Free Trust-Region Algorithm for the Optimization of Functions Smoothed via Gaussian Convolution Using Adaptive Multiple Importance Sampling", *SIAM J. Optim.* 2018, DOI 10.1137/15M1031679 | |

- **Maggiar and Avci** [practice, S].
  - The IEMS list gives Alvaro Maggiar's advisor as Irina Dolinskaya (Fall 2014), and Harun Avci's as Barry Nelson.
  - Both published with Wächter.
  - This answers an open question in 01 (§1.4): Wächter worked closely with students whose formal advisor was someone else.

### A.3 Where he served on committees

This is practice: service recorded in the students' acknowledgments.

- **Nocedal's students:** A. S. Berahas (2018), H.-J. M. Shi (2021), Y. Xie (2021), M. Q. Xuan (2023).
- **An ESAM student:** S. Sun (2024; advisor Nocedal).
- **A simulation student:** M. Feng (2016; advisor Staum).
- **His own students' committees** were drawn from the same small circle: Curtis and Wei for Keskar; Wei and Russell Bent (Los Alamos) for Luo; Nocedal, Pang and Mitchell for Jara-Moroni.

[inferred] In practice, the Northwestern nonlinear-optimization "group" was one joint Nocedal–Wächter group with a shared lab room (§B.3). Its outer ring for committees was Curtis, Wei, Byrd, Bayliss and Chopp.

---

## B. Layer 7: research organisation (supervision, collaboration, lab culture)

### B.1 How he himself was mentored (the model he inherited)

All from his PhD thesis acknowledgments, pp. ii–iii, CMU, 29 Jan 2002 [stated, P]. The text layer is a bitmap font, decoded in this run, and word spacing was restored.

- **Biegler**:
  - "who was a true Doktorvater to me. Larry is an excellent and knowledgeable teacher, an inexhaustible fountain of ideas, and an inspiring and open mentor, who gave me the optimal balance of guidance and freedom."
  - "for always having an open ear for my questions and concerns."
- **Nocedal**: "who became a very encouraging mentor to me, and who introduced me into the math programming crowd", with thanks for "his warm hospitality during my visits at Northwestern". His "contagious optimism together with his amazing ability to always find new important questions from unexpected viewpoints had a significant and inspiring influence on this work."
- **Tütüncü**: "for taking the effort of teaching me the basics of interior point methods in a reading course."
- **A distributed support network of senior people.** He thanks:
  - Andrea Walther and Olaf Vogel "for their extensive and fast support with ADOL-C";
  - Richard Waltz "for providing Knitro and discussing aspects of its implementation";
  - Hande Benson and Robert Vanderbei "for their help regarding their Ampl models and Loqo";
  - "Jose Luis Morales for sharing with me his PERL scripts for a convenient analysis of the test runs";
  - Jorge Moré for Tron;
  - Byrd and Marazzi "for inspiring conversations regarding convergence failures and filter methods";
  - Forsgren and Sporre "for interesting discussions about counter examples";
  - Sainvitu and Toint "for their valuable feedback on the convergence proofs of the filter method".

**Reading** [inferred]:
- As a student, he got tools from the people who wrote them: solvers from their authors, test-analysis scripts from a peer, proof checking from the Namur group.
- He then gave the same kind of help. Victor Zavala's 2008 CMU thesis (Biegler group) thanks "Dr. Carl Laird from Texas A&M and Dr. Andreas Wächter from IBM for all their input and help with IPOPT" (p. ii) [observed, S].
- His advisor–mentor pair also split the roles: Biegler provided freedom and an open ear, Nocedal provided optimism and new questions. That split reappears in how his own co-advised student describes him and Nocedal (§B.2, Keskar).

### B.2 Supervision style as students describe it

All [observed, S]. Each item is "according to <student>, <thesis>, page".

- **Specificity and precision, set against Nocedal's breadth.** According to Nitish S. Keskar (PhD 2017, co-advised with Nocedal), *Second-Order Methods for Stochastic and Nonsmooth Optimization*, p. 6. The PDF text layer drops the apostrophes; the quote is given as extracted:
  - "I consider myself lucky to have not just one but two excellent advisors who, in their almost orthogonal approaches, helped me grow as a researcher. With Andreas focus on specificity and precision, and Jorges emphasis on broad, albeit unstructured, ideas, I truly got the best of both worlds."
  - Also: "I dont foresee forgetting the essential skills of research, communication, and learning you taught me."
  - This is the only source that **contrasts** Wächter with another advisor. It is therefore the most informative line in the corpus.
- **High standards, detailed feedback, patience.** According to Xinyi Luo (PhD 2023), *Efficient Second-Order Methods for Second-Order Cone Programs and Continuous Nonlinear Two-Stage Optimization Problems*, p. 5: "Andreas's insightful feedback, patience, and dedication have significantly improved the quality of this work. His high standards and encouragement have constantly motivated me to strive for excellence."
- **Quality as a mission.** According to Niloufar Izadinia (PhD 2023), *Multi-Objective Mixed-Integer Nonlinear and Distributionally Robust Optimization Algorithms and Applications*, p. 5: "His unparalleled knowledge, enthusiasm for research, and his mission to provide high-quality work were constant sources of inspiration throughout my Ph.D."
- **Patience; becoming a friend.** According to Francisco Jara-Moroni (PhD 2018), *Methods for Linear Programs with Complementarity Constraints*, p. 6: "my advisor Andreas Wächter, who within these 5 years has become not only my guide, but also my friend. Andreas, thanks for all your support, patience and help, and for accepting me as your student."
- **Unusual effort from a team of three advisors.**
  - According to Mark Semelhago (PhD 2020), *Computational Aspects of Discrete Optimization via Simulation with Gaussian Markov Random Fields*, p. 6. About Nelson, Wächter and Song jointly: "the amount of effort, care and attention they have shown in helping me develop into a researcher is uncommon and something which I do not take for granted."
  - According to Harun Avci (PhD 2024), p. 5, about the same three: "Their mentorship has prepared me well for the next steps in my career."
- **As a committee member for other advisors' students.**
  - Melody Q. Xuan (2023, p. 6): "I am especially grateful for their feedback and insights into various research topics" (Wächter and Curtis).
  - Yuchen Xie (2021, p. 6): "Thank you, Professor Andreas Wächter and Professor Ermin Wei, for teaching me so much and serving on my dissertation committee."
  - Berahas (2018, p. 6), Shi (2021, p. 9) and Sun (2024, p. 6) give generic thanks.
- **As a peer, seen by a student of Nocedal.** According to Frank E. Curtis (PhD 2007), *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, p. 5, who thanks "Andreas Wächter and Sven Leyffer, for exhibiting to me the levels of creativity and intelligence in a researcher that I can only hope to achieve." Wächter was then at IBM. Curtis became his most frequent co-author (9 papers; see 01) [practice].

**What is *not* said** [inferred]. No student mentions the following, so these stay empty:
- frequency of meetings;
- how problems were assigned;
- how drafts were edited;
- how he handled a student who was stuck;
- anything about writing style.

What the students do single out is consistent across five of them: precision or specificity, high standards or quality, patience. Only Keskar sets him against another advisor.

### B.3 Group habits and lab culture

All [observed, S]. These describe the **shared** Nocedal–Wächter lab, not a Wächter-only group.

- **One room, L375, shared by both groups.**
  - Keskar (2017, pp. 6–7) names the group-mates "Gillian, Travis, Sammy, Stefan, Alvaro, Ben, Francisco, Albert, Vijaya, Samira and Alejandra". That list mixes students of both advisors. He adds: "Im never going to forget times spent in the barbeques, trivia quizzes, side projects, gossiping, group meetings and practical jokes. The years I spent in L375 were some of the best, most productive, and laughter-packed years of my life; Im going to miss them and I hope all the rituals (including pranks) continue." (Apostrophes are lost in the text layer.)
  - Luo (2023, p. 6) thanks "the entire Optimization Lab L375, including the past members Ruby, Yuchen, Alejandra, and Michael, and the current members Shima, Shigeng, Melody, and Xiaochun."
  - Shi (2021, p. 9) lists the "Northwestern Optimization Lab" as students of both advisors (Berahas, Bollapragada, Dezfulian, Jara-Moroni, Keskar, Luo, Peña-Ordieres, Tu, Xuan, Xie and others) and writes: "So much of my Ph.D. research should be credited to them."
- **"Side projects" and "group meetings"** are named. Their format is **not described anywhere** (gap).
- **Internships at a national laboratory as part of training.** Luo (p. 5) thanks the Los Alamos "Advanced Network Science Initiative" for "My summer internship in New Mexico", with LANL staff guiding the internship and co-developing "the two-stage optimization algorithm project". Russell Bent (LANL) sat on her committee. This coincides with Wächter's 2019–20 year at LANL as Ulam Distinguished Scholar (McCormick news, 2 Oct 2019) [practice + observed, S].
- **Shared compute** [inferred from identical specs, S]:
  - Jara-Moroni (p. 55): "a Linux workstation with 3.10GHz Xeon processors using 20 cores (40 cores hyperthreaded) and 256GB RAM".
  - Peña-Ordieres (p. 124): "Ubuntu 16.04 with 256GB RAM and two Intel Xeon processors each with ten 3.10GHz cores".
  - This is probably one group server.

### B.4 How problems reach the students: co-advisors and application partners

[practice + inferred]
- Student topics follow the co-advisor or funding partner: simulation optimization (Nelson and Song; NSF DMS-1854562 funded both Semelhago and Avci), power systems (Wei; LANL), finance (Staum), and bilevel and complementarity problems (Pang, Mitchell).
- Izadinia's thesis lies furthest from solver design. Her chapters cover multi-team performance measurement (NASA award NNX15AK73G), post-disaster building reconstruction (an 11-author interdisciplinary paper) and Wasserstein distributionally robust optimization. Her thanks go to Wächter, "Prof. David Morton and Prof. William M. Miller" (p. 5).
- So "a Wächter student" did not mean "an Ipopt developer". The common core is nonlinear-optimization method applied inside someone else's application.
- This matches his homepage's stated third research theme: introducing nonlinear-optimization techniques "into settings where they have not yet been exploited" (see 01) [stated, P].

### B.5 The Ipopt project as a collaboration and mentoring structure

- **The IBM internship model** [stated-joint, P: Ipopt docs, "History of Ipopt"]: "IBM Research decided to invest in an open source re-write of Ipopt in C++. With the help of Carl Laird, who came to the Mathematical Sciences Department at IBM Research as a summer intern in 2004 and 2005 during his PhD studies, the code was re-implemented from scratch."
  - The `AUTHORS` file lists "Main authors: Andreas Waechter, project leader (IBM) / Carl Laird (IBM, Carnegie Mellon University)".
  - A PhD intern was made co-author of the flagship code. McCormick news (2019) credits the software to both: "With Carl Laird, Professor Wächter created IPOPT" [observed, S].
- **Documentation began as a course project** [stated-joint, P: Ipopt docs, "History of this document"]: "The initial version of this document was created by Yoshiaki Kawajir [sic] … as a course project for 47852 Open Source Software for Optimization, taught by Prof. François Margot at Tepper School of Business, Carnegie Mellon University. After this, Carl Laird … has added significant portions, including the very nice tutorials."
  - Maintenance is now shared: "maintained by Stefan Vigerske (GAMS Software GmbH) and Andreas Wächter".
- **Contributors are credited by file, and unmaintained contributions are removed** [practice, P: `AUTHORS`, stable/3.14].
  - Each contributor is listed next to the files they wrote. Examples: Olaf Schenk and Michael Hagemann (Basel) for PARDISO and MA57; Hans Pirnay and Rodrigo López-Negrete for sIPOPT; Nai-Yuan Chiang and Victor Zavala (Argonne) for the "inertia free curvature test"; Byron Tasseff (LANL) for SPRAL.
  - Some entries carry "[removed from Ipopt source as unmaintained]", for example the Matlab interface by Peter Carbonetto.
  - [inferred] Contributions are accepted, and kept only if someone keeps them working.
- **Day-to-day integration delegated** [observed, S: GitHub PR #428, "single precision", opened 17 Nov 2020, merged 18 Nov 2020].
  - Stefan Vigerske merged it with: "I merged this into branch devel for now, since I might want to do some small changes, probably add a test in travis, add a mention in the docu, etc. But thank you alot for this contribution!"
  - No comment by Wächter appears on that PR. I read one PR only; the GitHub API was not reachable from this session.
- **The citation request as an incentive argument** [stated-joint, P: Ipopt docs, "Availability"]: "Writing high-quality numerical software takes a lot of time and effort, and does usually not translate into a large number of publications, therefore we believe this request is only fair :)."
  - [inferred] He knows that software work is under-rewarded in the publication economy. That matters for students whose theses are largely software (§C.4).

---

## C. Layers 4–6 as practised by his advisees (execution, judgment, reporting)

These are practices recorded in his advisees' dissertations, in chapters that correspond to joint papers with him. They are [practice, S]. Attributing them to **his** supervision is [inferred]: the co-advisor, the student or the field could equally be the source.

### C.1 Benchmarking discipline

- **Give every solver the same oracle.** Keskar (p. 76), for the nonsmooth L-BFGS chapter (the Keskar–Wächter paper): "To make sure each solver obtains the same function and derivative information, we implemented Python wrappers around the Fortran codes written by the respective authors."
- **Test whether the implementation language confounds CPU-time comparisons.** Keskar (p. 37), for the ℓ1 chapter: "the choice of programming language (MATLAB vs. C) has no significant impact on the computation time. In fact, we observed very similar performance of our own MATLAB and C implementations of OBA."
- **Prefer iteration counts when prototype timings are unreliable, and run single-threaded.** Jara-Moroni (p. 110): "For a fair comparison, all experiments were run with a single thread." And: "It is important to point out that CPU time must not be taken too seriously, since it is not clear if hot-starts, in the MATLAB/CPLEX inter-phase, works as efficient as it could. … We consider the number of main iterations as a reflection of the quality of both the pieces selected and the cut generated, so it is our main metric to observe."
- **Say what a prototype is for.** Luo (p. 67), for the SOCP-SQP chapter (the Luo–Wächter SIOPT 2024 paper): "We emphasize that the purpose of our implementation is to assess whether the proposed algorithm exhibits behavior that validates the stated goals: Convergence from any starting point and rapid local convergence to highly accurate solutions. In its current implementation, it requires more computation time than highly sophisticated commercial solvers such as MOSEK or CPLEX, which were developed over decades and have highly specialized linear algebra routines that are tightly integrated into the algorithms."
  - [inferred] This matches his own 2002–2006 view that a comparison measures software at one stage of development (02, R12).
- **Define "good solution" before the experiment, for stochastic NLP.** Peña-Ordieres (p. 124): solutions "are said to be good if they are: (1) consistent over different samples, (2) feasible for the true problem (evaluated with an out-of-sample test), and (3) have low cost."

### C.2 Honest failure accounting

- **Count failures by cause and name the failed instances.** Luo (p. 107), running RestartSQP with the QORE subsolver on CUTE, gives causes and counts: "14 instances encountered failure because the penalty parameter became too large", "14 … QP solver exceeded the maximum number of iterations", "17 … internal QP solver errors", "4 … QORE declaring the QP as unbounded", "3 … declaring them infeasible". The instance names are listed in footnotes.
- **State the limit of your own design.** Luo (p. 111): "the parametric active-set method utilized in the implementation may not be suitable for solving large-scale QP problems. Additionally, the QP solver QORE is still under development and lacks mature error handling compared to well-established solvers like Ipopt."
- **Use a solver failure to motivate a reformulation.**
  - Peña-Ordieres (p. 25, Table 2.1) shows Knitro stopping with "Convergence to an infeasible point. Problem appears to be locally infeasible." on one formulation of a chance constraint, and uses this to argue for her quantile-based formulation.
  - [inferred] This is the same move as Wächter's own 2000 counterexample paper (01, SW1): a well-posed problem on which a method fails, used to motivate a design.
- **The counter-case: baselines dropped without results.**
  - Jara-Moroni (p. 55): "We have considered the knitro nonlinear programming solver … but we do not describe its performance here since it was unable to solve many of the test problems."
  - Keskar (p. 77): "We exclude other methods, including gradient-sampling methods, since we found their performance to be inferior to the methods listed above."
  - In both cases the failing baseline is mentioned but its numbers are not shown. This is kept here as the opposite of the Luo practice.

### C.3 Solver-usage know-how

Tacit: this sits in the experimental sections of the theses, not in the papers' abstracts.

- **An Ipopt warm-start recipe for a sequence of related NLPs.** Peña-Ordieres (p. 124), AC-OPF with joint chance constraints: "The algorithm is implemented in AMPL, using Ipopt 3.12 to solve (4.9). For all iterations of Algorithm 5 after the first, we set Ipopt's parameters to tol = 10−8, mu init = 10−5, bound frac = 10−6, and bound push = 10−6. These changes to the parameters of Ipopt are made to get a better warm-start for the subsequent iterations of the algorithm."
  - The pattern: lower the initial barrier parameter, and keep the push away from bounds small, so the warm start stays near the previous solution.
- **Warm starts by crossover from the interior-point method to SQP.**
  - Luo's RestartSQP (thesis abstract and ch. 3) "supports crossover from interior-point solvers like Ipopt, enabling the solution of subsequent NLPs using the SQP method".
  - Ipopt "performs better as a QP subsolver, just as anticipated. Its robustness contributes to the overall performance of the SQP solver" (p. 111).
- **Supply exact derivatives even for custom nonsmooth-looking functions.** Peña-Ordieres (pp. 125, 129): "For AMPL to compute Qϵ(z), we implemented a function in C that is loaded by AMPL and that performs the root finding process that implicitly defines the smooth quantile Qϵ. This function also computes the gradient and Hessian of Qϵ with respect to each scenario zi."
  - [inferred] This is consistent with his most repeated piece of advice, "supply exact second derivatives" (02, R1).
- **No house-solver dogma.**
  - The Ipopt author's students used whatever fit: Knitro 10.1.2 (Peña-Ordieres ch. 2), Ipopt 3.12 (ch. 4), filter via AMPL and MATLAB+CPLEX (Jara-Moroni), MOSEK via CVX (Luo ch. 2), qpOASES and QORE (Luo ch. 3), and PARDISO from MATLAB (Semelhago).
  - [practice] The only solver-loyalty pattern is PARDISO, the linear solver of his long-time collaborator Olaf Schenk, in Semelhago's code.

### C.4 A software artifact as part of the dissertation

- **Luo**: "RestartSQP, an open-source C++ software package implementing Fletcher's Sℓ1QP method and integrating the parametric active-set methods" (thesis abstract; ch. 3). The thesis gives **no repository URL**.
  - A GitHub repository `chenjianxing1/RestartSQP` exists ("SQPhotstart: A Sequential Quadratic Programming Solver for Constrained Nonlinear Optimization"; C++, CMake, needs Ipopt, bundles qpOASES, optional Gurobi and CPLEX; Travis CI and codecov files; last updated July 2020).
  - Its relation to Luo's package, and its authorship, is **not established** (⚠️ lead only).
- **Semelhago** (p. 84): recasts the algorithms "into an object-oriented programming (OOP) framework. This new implementation is code that practitioners can use and modify". It "can be run using standard MATLAB toolboxes as well as specialized software to reduce linear algebra computational overhead".
  - [inferred] The pluggable-linear-solver design mirrors Ipopt's architecture.
- **Keskar** gives public repositories for both of his methods: `https://github.com/keskarnitish/OBA` (thesis p. 50) and `https://github.com/keskarnitish/NQN` (p. 76). **Not opened.**
- **Peña-Ordieres** (p. 129, future work): "We would like to make this code open-source and readily available". So at graduation it was not yet released.
- [inferred] Building a reusable implementation is a recurring expectation in his group, echoing his own PhD, where the dissertation *was* Ipopt. The degree of release varied.

---

## D. Failures, abandoned directions

- **A joint thesis direction that "did not converge".**
  - According to Mingbin (Ben) Feng, *Green Simulation: Reusing the Output of Repeated Experiments* (PhD 2016, advisor Staum), p. 5: "Thank you Andreas for having me as your first PhD student (well, kind of!). I enjoyed doing research with you, and it is a pity that it did not converge into a thesis." [observed, S]
  - The direction still produced two papers: the VaR portfolio paper (QFL 2015) and the adaptive-multiple-importance-sampling SAA paper (WSC 2018, with Maggiar and Staum) [practice].
  - [inferred] A student's project with him could be publishable without becoming the dissertation. The thesis followed the main advisor.
- **Components that did not reach maturity inside a thesis.** Luo reports the QORE failures and a possible large-scale mismatch of the parametric active-set approach (§C.2). Peña-Ordieres left her code unreleased (§C.4). Jara-Moroni flagged unreliable CPU times at the MATLAB/CPLEX hot-start interface (§C.1).
- **Rejected papers or retracted claims.** **None found.** No public reviews or rebuttals exist for SIOPT or Math. Program. papers.

---

## E. Era and resource context

| Period | Setting | Team and tools | Evidence |
|---|---|---|---|
| 1997–2002 | CMU chemical-engineering PhD, Biegler group; visits to Northwestern (Nocedal), Namur, Stockholm | Solvers and scripts obtained directly from their authors (Knitro, LOQO, TRON, ADOL-C, PERL test-analysis scripts) | thesis acknowledgments [stated, P] |
| 2002–2011 | IBM Research, Mathematical Sciences | Summer intern (Laird, 2004–05) co-writes the C++ Ipopt; CMU–IBM MINLP team (the CMU–IBM project page lists Cornuéjols, Biegler, Grossmann, Margot, Belotti, Bonami, Conn, Lee, Ladanyi, Wächter, Laird, Sawaya) | Ipopt docs [P]; `egon.cheme.cmu.edu/ibm/page.htm` [S] |
| 2011–c. 2024 | Northwestern IEMS; shared lab L375 with the Nocedal group | 1–3 of his own students at a time plus co-advised ones; MATLAB prototypes calling CPLEX or Gurobi; AMPL with Ipopt or Knitro; Python for ML-flavoured work; a 20-core, 256 GB Linux server; NSF DMS funding (e.g. DMS-1854562); CONICYT fellowship (Jara-Moroni); LANL internships | theses [S] |
| 2019–20 | Ulam Distinguished Scholar, CNLS, Los Alamos | power-systems students (Tu, Luo) and LANL co-supervision | McCormick news, 2 Oct 2019 [S]; Luo p. 5 |
| now | Gurobi (homepage note); homepage frozen | supervision presumably ends, but the status of the remaining student (Lou) was **not found** | homepage [stated, P] |

**Transfer caveat** [inferred]:
- The habits in §C come from academic PhD projects with MATLAB or AMPL prototypes and CUTE/CUTEst-scale tests.
- They are not the habits of a production-solver team.
- His current Gurobi practice is **not documented** in anything found.

---

## F. Tacit knowledge: what his students knew that the papers do not say

Each item is labelled with who shows it; all are secondary. Confidence is medium throughout: each item rests on one or two theses.

1. **Warm-starting Ipopt across a sequence of related NLPs.** Lower `mu_init` to about 1e-5, set `bound_frac` and `bound_push` to about 1e-6, and tighten `tol`. According to Peña-Ordieres, thesis p. 124.
2. **When warm starts matter, cross over from the interior-point solution to an active-set SQP.** The IPM gives robustness; the SQP with a parametric QP solver gives reuse of the active set. According to Luo, thesis abstract and ch. 3.
3. **Compare solvers only through identical function and derivative oracles.** Check that the implementation language is not what you are measuring. According to Keskar, pp. 37 and 76.
4. **For MATLAB-level prototypes, treat CPU time as secondary.** Report iterations as the main metric and run single-threaded. According to Jara-Moroni, p. 110.
5. **State what the prototype is meant to validate** (global convergence, fast local convergence, accuracy), and concede the wall-clock race to commercial codes openly. According to Luo, p. 67.
6. **Break failures down by cause, and list failed instances by name.** According to Luo, p. 107.
7. **Write custom model functions as compiled AMPL user functions that return exact gradients and Hessians,** rather than approximating them. According to Peña-Ordieres, p. 125.
8. **Precision first.** The one contrastive recollection (Keskar, p. 6) puts "specificity and precision" at the centre of his supervision, as opposed to Nocedal's "broad, albeit unstructured, ideas".

---

## G. Contradictions (kept, not reconciled)

1. **Who advised Keskar.** The homepage says co-advised with Nocedal. The IEMS graduates list gives only Wächter. Keskar's thesis names both as advisors.
2. **Who advised Feng, and who was the "first" student.**
   - The homepage lists Feng as co-advised with Staum. The IEMS list gives Staum only. Feng calls Staum "my advisor" and Wächter a committee member, and describes himself as Wächter's "first PhD student (well, kind of!)" whose joint research "did not converge into a thesis".
   - Meanwhile the homepage and CV list Travis Johnson as a former student who graduated in 2013, before Feng's 2016.
   - Johnson does not appear in the IEMS graduates list (his department is not confirmed), although Keskar lists a "Travis" among the L375 group-mates.
3. **Avci.** His thesis names Wächter as one of three advisors. The IEMS list names Nelson only. Wächter's frozen homepage does not list him (the homepage may predate Avci's Summer 2024 graduation; not checked).
4. **Open source: stated value versus student practice.**
   - The Ipopt documentation argues for credit to software work, and Luo calls RestartSQP "open-source".
   - But Luo's thesis gives no repository, Peña-Ordieres's code was still unreleased at graduation, and Keskar did publish repositories.
5. **Honest failure reporting versus dropped baselines.** Luo reports every failure by cause. Jara-Moroni and Keskar exclude failing or "inferior" baselines without showing their numbers. Both happen in the same group.
6. **"Ipopt group" versus solver pluralism.** Ipopt's author did not steer students to Ipopt. Several key chapters used Knitro, filter, CPLEX or MOSEK.

---

## H. Gaps (not found or not read)

- **His own statement on how he supervises.** None found (same gap as 02, O4).
- **Theses of Travis Johnson (2013), Ruby Tu (2021) and Shima Dezfulian (2024).** Not in Arch and **not read**; ProQuest copies are behind institutional access and were not used.
- **Carl Laird's CMU thesis** (the IBM-intern period) was not found in KiltHub or the Biegler group page. **Not read.**
- **Alvaro Maggiar's thesis** (2014, advisor Dolinskaya), which could describe the Maggiar–Wächter collaboration from the student side. **Not read.**
- **No student blog, lab guide, onboarding document, Festschrift contribution, interview or talk** about his supervision was found. Two WebSearch calls were spent on this.
- **The USI (Lugano) news item on the ARPA-E Grid Optimization competition** (`usi.ch/en/feeds/20660`, surfaced by WebSearch) returned HTTP 403 to both curl and WebFetch. **Not read.**
- **Biegler's SIAM book front matter** (DOI 10.1137/1.9780898719383), which might acknowledge Wächter: HTTP 403. **Not read.**
- **Linda Pei's thesis** (Nelson group, 2022): HTTP 401. **Not read.**
- **Theses checked that do not mention him:** Wei Wan (CMU 2017; it mentions Ipopt's authorship only), R. López-Negrete (CMU 2011), R. Huang (CMU), S. Seymen (Northwestern 2023), C. Kim (Northwestern 2020).
- **Group meetings and side projects.** Named by Keskar, but their format, frequency and content are not described.
- **IBM-era mentoring beyond Laird** (for example of postdocs in the MINLP project). Not documented.
- **The Gurobi era.** Whether he mentors developers there: not documented.
- **Ipopt code review.** Only one GitHub PR (#428) was read, and it has no Wächter comment. The GitHub API was not reachable from this session.
- **Lead for other agents.** WebSearch surfaced a Google Scholar profile, `scholar.google.com/citations?user=Y1EdzIwAAAAJ`, titled "Andreas Waechter". team.json has no Scholar id. **Not opened**, so the identity is not confirmed.

---

## Sources

Primary (his own or co-maintained):
1. A. Wächter, *An Interior Point Algorithm for Large-Scale Nonlinear Optimization with Applications in Process Engineering*, PhD thesis, CMU, 29 Jan 2002, acknowledgments pp. ii–iii. http://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf (primary; acknowledgments decoded and read)
2. A. Wächter, homepage, "Students" page (frozen; "I moved to Gurobi Optimization"). http://users.iems.northwestern.edu/~andreasw/students.html, accessed 2026-09-28 (primary)
3. Ipopt documentation: Overview, "History of Ipopt", "History of this document", "Availability" (maintained by S. Vigerske and A. Wächter). https://coin-or.github.io/Ipopt/, accessed 2026-09-28 (primary, joint)
4. Ipopt `AUTHORS` file, branch stable/3.14. https://raw.githubusercontent.com/coin-or/Ipopt/stable/3.14/AUTHORS (primary, joint)

Student and colleague dissertations (Northwestern Arch unless noted; front matter read, and the cited experimental pages for items 5–8):
5. X. Luo, *Efficient Second-Order Methods for Second-Order Cone Programs and Continuous Nonlinear Two-Stage Optimization Problems*, Northwestern, 2023. DOI 10.21985/n2-5jy5-nm90 (secondary; pp. 5–6, 67, 107, 111 read)
6. F. I. Jara-Moroni, *Methods for Linear Programs with Complementarity Constraints*, Northwestern, 2018. DOI 10.21985/n2-86kj-yn55 (secondary; pp. 6–8, 55, 110 read)
7. N. S. Keskar, *Second-Order Methods for Stochastic and Nonsmooth Optimization*, Northwestern, 2017. DOI 10.21985/N25X1R (secondary; pp. 6–7, 37, 50, 76–77 read)
8. A. Peña-Ordieres, *Nonlinear Programming Approximations of Chance Constraints*, Northwestern, 2020. DOI 10.21985/n2-84re-9w94 (secondary; front matter, pp. 25, 124–125, 129 read; no acknowledgments section)
9. M. Semelhago, *Computational Aspects of Discrete Optimization via Simulation with Gaussian Markov Random Fields*, Northwestern, 2020. DOI 10.21985/n2-f1rh-h960 (secondary; pp. 4–6, 84 read)
10. N. Izadinia, *Multi-Objective Mixed-Integer Nonlinear and Distributionally Robust Optimization Algorithms and Applications*, Northwestern, 2023. DOI 10.21985/n2-wq9x-kk64 (secondary; p. 5 read)
11. M. Feng, *Green Simulation: Reusing the Output of Repeated Experiments*, Northwestern, 2016. DOI 10.21985/N2HQ25 (secondary; pp. 4–5 read)
12. H. Avci, *Simulation Optimization: Cache and Credit for Parallel Ranking & Selection, and Dice and Slice for High-dimensional Problems*, Northwestern, 2024. DOI 10.21985/n2-tg9m-9034 (secondary; p. 5 read)
13. F. E. Curtis, *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, Northwestern, 2007. DOI 10.21985/N2R99V (secondary; pp. 5–6 read)
14. H.-J. M. Shi, *Methods for Stochastic, Noisy, and Derivative-Free Optimization*, Northwestern, 2021. DOI 10.21985/n2-f1ch-pr51 (secondary; pp. 8–9 read)
15. M. Q. Xuan, *Methods for Derivative-Free Optimization with Applications in Machine Learning*, Northwestern, 2023. DOI 10.21985/n2-0ehk-v526 (secondary; p. 6 read)
16. Y. Xie, *Methods for Nonlinear and Noisy Optimization*, Northwestern, 2021. DOI 10.21985/n2-66e6-2297 (secondary; pp. 6–7 read)
17. S. Sun, *Numerical Methods in Noisy, Stochastic, Nonlinear Optimization*, Northwestern, 2024. DOI 10.21985/n2-km8f-7n29 (secondary; pp. 5–6 read)
18. A. S. Berahas, *Methods for Large Scale Nonlinear and Stochastic Optimization*, Northwestern, 2018. DOI 10.21985/N2M46R (secondary; p. 6 read)
19. V. M. Zavala, *Computational Strategies for the Optimal Operation of Large-Scale Chemical Processes*, CMU, 28 Aug 2008. https://numero.cheme.cmu.edu/content/thesis/thesis_vzavala.pdf (secondary; p. ii read)
20. Checked, no mention of Wächter's mentoring: W. Wan, *Advances in Newton-based Barrier Methods for Nonlinear Programming*, CMU 2017 (KiltHub 6714626); R. López-Negrete, CMU 2011 thesis (numero.cheme.cmu.edu); R. Huang, CMU thesis (numero.cheme.cmu.edu); S. Seymen, Northwestern 2023 (DOI prefix 10.21985, Arch rb68xc46q); C. Kim, Northwestern 2020 (Arch pn89d6834) (secondary)

Institutional and third-party pages:
21. Northwestern IEMS, "PhD Graduates (2000 on)". https://www.mccormick.northwestern.edu/industrial/people/graduate-students/former_students.html, accessed 2026-09-28 (secondary, institutional)
22. McCormick News, "Andreas Wächter Serving as Ulam Distinguished Scholar at Los Alamos National Laboratory", 2 Oct 2019. https://mccormick.northwestern.edu/industrial/news-events/news/articles/2019/waechter-lanl.html (secondary)
23. CMU–IBM Open Source MINLP Project page. https://egon.cheme.cmu.edu/ibm/page.htm (secondary)
24. Biegler group, "Graduated" page. https://numero.cheme.cmu.edu/group/graduated.html (secondary)
25. GitHub, coin-or/Ipopt PR #428 "single precision" (Nov 2020). https://github.com/coin-or/Ipopt/pull/428 (secondary)
26. GitHub, chenjianxing1/RestartSQP (README only). https://github.com/chenjianxing1/RestartSQP (⚠️ lead; relation to Luo's thesis not established)

Not read:
27. USI news feed on the ARPA-E Grid Optimization Competition, https://www.usi.ch/en/feeds/20660 (HTTP 403)
28. L. T. Biegler, *Nonlinear Programming* (SIAM 2010) front matter, DOI 10.1137/1.9780898719383 (HTTP 403)
29. L. Pei, Northwestern 2022 thesis, Arch bv73c083v (HTTP 401)

Papers named in §A.2. Identifiers were checked with Crossref or arXiv in this run; the papers themselves were not read beyond the corresponding thesis chapters:
- DOI 10.1137/130918320
- DOI 10.1137/130940384
- DOI 10.1080/21649502.2014.995214
- DOI 10.1109/WSC.2018.8632370
- DOI 10.1080/10556788.2016.1138222
- DOI 10.1080/10556788.2017.1378652
- DOI 10.1007/s10107-017-1208-6
- DOI 10.1007/s10898-020-00905-z
- DOI 10.1137/19M1261985
- DOI 10.1109/WSC.2017.8247941
- DOI 10.1287/ijoc.2020.0971
- DOI 10.1109/TPWRS.2020.3002189
- DOI 10.1137/22M1507681
- DOI 10.1137/25M1728661
- DOI 10.1007/s11081-022-09766-9
- DOI 10.1137/15M1031679
- arXiv:2502.11302
