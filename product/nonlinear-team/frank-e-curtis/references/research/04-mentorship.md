# Frank E. Curtis: students, postdocs and collaborators (research agent 04)

| Field | Value |
|---|---|
| Researcher | Frank E. Curtis (Lehigh University ISE since Aug 2009; PhD Northwestern 2007 under Jorge Nocedal; Courant postdoc 2007-09) |
| Dimension | 04: mentorship. Supervision style, group habits, lab culture and tacit knowledge, as seen by students, postdocs and collaborators, checked against the record |
| Research date | 2026-09-28 |
| Sources consulted | 38 (18 primary: his CV, web pages, syllabi, his own PhD thesis, group web pages he co-runs, the NonOpt project page and git history, and bibliographic records; 20 secondary: six doctoral theses by his advisees or collaborators, two theses on which he was a committee member, students' and postdocs' own web pages and CV, and Lehigh news and program pages) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only `.gitkeep`. No `private/` folder was opened |
| Language | English (per team.json) |

**What was read and how.** There is no student blog, interview, memorial piece, Festschrift or lab guide about Curtis that I could find. He is mid-career and living, so none of these would be expected yet. The best first-hand student evidence is the **acknowledgements and approval pages of his advisees' dissertations**. Lehigh Preserve now puts item pages behind a bot check (HTTP 429, "Verifying connection"). I did not try to get around it. Instead I found the older theses through the Internet Archive's public copy of the former Preserve (bepress) site: the ISE dissertation listing captured 2020-11-11, then the archived PDFs. Four advisee dissertations were read in their front matter and in selected passages: Hao Wang 2015, Zheng Han 2015, Xiaocun Que (degree Fall 2015, record year 2016) and Wei Guo 2017. Samadi's 2018 thesis survives only as a truncated 1 MiB copy, from which I read the biography and appendix only. The other theses were not read (see Gaps). I also read Curtis's own 2007 PhD thesis (acknowledgements and contents) and the NYU thesis of Tim Mitchell, a collaborator whose code Curtis co-advised. Text was extracted with pypdf. "PDF p." gives the PDF page and "p. iv" the printed page. Ligatures are normalised (ﬁ → fi). Spelling is otherwise left as in the source.

**Division of labour with the other notes.** Note 01 (§1.3) already lists advisees with their thesis lines and discusses author order. Note 03 (PE21, PE22, PE26, PE35) already analyses the git histories: student prototypes that the PI consolidates, NonOpt component credits, corrigenda, and the 2026 AI-agent code pass. I do not repeat that evidence here. Where it bears on mentorship I refer to it by its label and add what the mentorship sources say.

**Tags.** [stated] = Curtis's own words. [practice] = what the record shows he or his group did. [observed] = what students or collaborators say. [inferred] = my reading, not evidence. (P) = primary and (S) = secondary relative to Curtis. A student's account of Curtis is first-hand for the student but **secondary** for Curtis, and is marked (S).

---

## 1. Where his supervision style comes from (lineage)

**L1. How he was supervised himself: Nocedal as advisor, Byrd as working partner, and access to production-solver source code.** [stated] (P)
- Curtis's thesis acknowledgements (2007, PDF p. 5): "I would like to thank first, and above all, Jorge Nocedal. Far be it from me to try and capture, in only a few short lines, the level of guidance and support that he has provided for me over the past few years." He adds that he "would like nothing more than for us to maintain a close professional and personal relationship for many years to come."
- On Byrd (same page): "Any scientific accomplishments contained in these pages would not have been possible without the knowledge and expertise of Richard Byrd."
- On production code: he thanks committee member Richard Waltz "and Todd Plantenga for access to, and technical support for, KNITRO source code". His thesis ends with "numerical results for the KNITRO software package" (abstract, PDF p. 4).
- On other models: he thanks Eldad Haber "for having confidence in me and taking the time to explain concepts", Nick Gould "for enlightening e-mail correspondence and much appreciated encouragement", and Andreas Wächter and Sven Leyffer "for exhibiting to me the levels of creativity and intelligence in a researcher that I can only hope to achieve."
- Committee (CV p. 1): Fourer, Mehrotra and Dr. Richard A. Waltz, the last a KNITRO developer.
- Era: Northwestern IEMS, 2003-07, plus a summer internship at Intel Corporate Technology Group in 2005 (CV p. 1).

**L2. He carries the lineage forward: Nocedal and Nocedal's students recur in his group.** [practice] (P/S)
- Nocedal sits on Curtis advisees' committees: Zheng Han 2015 (approval page, PDF p. 4) and Baoyu Zhou 2022 (Zhou CV p. 1: "Doctoral Committee: Albert S. Berahas, Jorge Nocedal, Daniel Robinson, Luis Nunes Vicente").
- His first postdoc, Albert S. Berahas (2018-20), "completed his thesis ... at Northwestern University, where he was advised by J. Nocedal" (OptML news, 2018-09-01).
- Zhou was a "Visiting Research Assistant, Northwestern University ... Department of Industrial Engineering and Management Sciences, June 2017 – Aug. 2017" while he was Curtis's master's student (Zhou CV p. 1). The CV does not name a host.
- [inferred] The acknowledgement template is inherited. Wei Guo's opens "I would like to thank first, and above all, my academic advisor, Professor Frank E. Curtis" (PDF p. 5). That is almost word for word Curtis's own opening to Nocedal. It suggests students read, and imitate, their advisor's thesis.

**L3. Postdoc with Overton: co-advising someone else's student through code.** [stated] + [observed]
- Curtis's CV (p. 8) on GRANSO: "I co-advised, with Michael Overton, the writing of the code by Tim Mitchell". [stated] (P)
- Mitchell's NYU thesis (2014, p. iv): "Our mutual collaborators, Frank Curtis, Nicola Guglielmi, and Mert Gürbüzbalaban, have each provided me with interesting problems and insightful feedback and broadened my pool of knowledge." [observed] (S)
- Mitchell's chapter 7 says: "This chapter is joint work with Frank E. Curtis and Michael L. Overton" (PDF p. 146). It became Curtis–Mitchell–Overton, OMS 32(1) 2017, DOI 10.1080/10556788.2016.1208749.
- Curtis also sat on Mitchell's doctoral committee (CV, committee list: "Tim Mitchell, Department of Computer Science, New York University 2014").

---

## 2. Layer 7: supervision structure

**S1. Roster and timeline.** [practice] (P). Sources: CV pp. 24-25 and 29, rev. 2026-04-07; Collaborators page, read 2026-09-28; approval pages of the theses.

| Advisee (role) | Years | Committee (from approval page or CV) | Where next (Collaborators page / OptML "first after OptML") |
|---|---|---|---|
| Hao Wang (PhD) | 2009-15 | Curtis (advisor); Terlaky; J. V. Burke (Washington); Scheinberg | ShanghaiTech (faculty) |
| Xiaocun Que (PhD) | 2009-15 | Curtis (chair); M. L. Overton (NYU); Scheinberg; Ralphs | IBM |
| Jiaxin Liu (PhD, co-advised with Terlaky) | 2010-13 | none: "left program prior to completing proposal" (CV p. 25) | — |
| Zheng Han (PhD) | 2010-15 | Curtis (chair); J. Nocedal (Northwestern); D. P. Robinson (then JHU); Terlaky; Zuluaga | American Express, then Morgan Stanley |
| Wei Guo (PhD) | 2011-17 | Curtis (chair); Yu-Hong Dai; Robinson; Scheinberg; Takáč | J.P. Morgan, then Meta |
| Mohammadreza Samadi (PhD) | 2013-18 | not read | SAS, then J.P. Morgan Chase |
| Rui Shi (PhD) | 2015-20 | not read | SAS |
| Baoyu Zhou (MS 2016-18, then PhD 2018-22) | 2016-22 | Berahas; Nocedal; Robinson; Vicente (Zhou CV) | Chicago Booth, then Michigan postdoc, then ASU assistant professor from July 2024 (Zhou CV) |
| Minhan Li (PhD) | 2019-21 | not read | Amazon, then Meta |
| Qi Wang (PhD) | 2020-25 | not read | Michigan postdoc with U. V. Shanbhag (Qi Wang site) |
| Current: Zebiane, L. Guo, Khatti (co-advised with Robinson), Y. Zhu (co-advised with A. Khajavirad) | 2023- | — | — |
| Postdocs: Berahas 2018-20; O'Neill 2020-22 (co-supervised with Robinson); Dinç Yalçın 2021-22; X. Jiang 2022-24 | | | Michigan; UNC Chapel Hill; Eskisehir Technical U.; U. of Houston (Xin Jiang site) |

- Masters and undergraduate thesis advisees (CV p. 29):
  - Wenda Zhang: "A Subproblem Algorithm for an Adaptive Augmented Lagrangian Method" (2013-14);
  - Jingxuan Liu: a time-series topic (2015);
  - Baoyu Zhou: "Quadratic Optimization for Nonsmooth Optimization Algorithms: Theory and Numerical Experiments" (2017-18);
  - Mandy Liu: "Numerical Optimizaton [sic] Methods in Machine Learning" (2010-12).
- Scale: 50 doctoral committees for other advisors' students (CV list). 13 of them are outside Lehigh: Northwestern, NYU, JHU, Columbia, Oxford, KTH, Toulouse, RPI and Michigan.
- [inferred] Each of the five committees I could read (Wang, Que, Han, Guo, Zhou) pairs Curtis with one outside authority on the thesis's exact topic:
  - Burke for infeasibility-detection SQP;
  - Overton for gradient sampling;
  - Nocedal for active-set and stochastic SQP;
  - Yu-Hong Dai for Barzilai–Borwein and limited-memory steepest-descent methods.

  Dai's pioneering explorations are acknowledged by Guo (PDF p. 5).

**S2. What his students say he gave them.** [observed] (S). All from dissertation acknowledgements.
- According to **Wei Guo** (2017, p. iv / PDF p. 5): "His extraodinary [sic] expertise, vision, and patience have guided me during my PhD study, especially his knowledgable [sic] insights on how to conduct meaningful and influential research, how to overcome various difficulties and challenges along the way, as well as how to work more efficiently and make good use of time. Besides his professional knowledge and thoughts, I have also received valuable suggestions on how to improve my technical writing skills and polish my communication and presentation skills".
- According to **Hao Wang** (2015, p. iv / PDF p. 5): "His expertise and vision have guided me through my research, and played the roles of fuel and lighthouse in my exploratory journey of research. I also want to thank him for providing me with the opportunities to connect with great researchers through conferences and internship programs. Apart from research, I also received much sincere advice from him in many other aspects such as English writing skills and communication skills."
- According to **Zheng Han** (2015, p. iv / PDF p. 5): "He has always been thoughtful in advising, generous (both financially and spiritually) in investing, and patient in mentoring. He also gives me much freedom and encouragement to pursue projects that best suit my ability and interest. I am fortunate to benefit tremendously not only from his thorough professional knowledge but also from his adherence to highest standard and meticulousness to research."
- According to **Xiaocun Que** (degree 2015, p. iv / PDF p. 5), the thanks are short and give no detail: "I would like to thank my advisor Prof. Frank E. Curtis for his excellent guidance during my Ph.D. years."
- Recurring themes. I count a theme only when it appears in two or more independent acknowledgements:
  - (a) **writing and communication coaching**: Guo, Wang;
  - (b) **patience**: Guo, Han;
  - (c) **"vision"/"expertise" guiding the research direction**: Guo, Wang;
  - outside that rule, one single-source theme: **meticulous standards** (Han only). It matches the errata page (§6).
  
  Only Wang mentions networking through conferences and internships. Only Han mentions freedom to choose projects.
- [inferred] Two of the four (Guo, Wang) single out English or technical writing and presentation. Que says nothing specific, and Han names other things. Writing and presentation coaching therefore seems to be a standing part of how he supervises. This fits his co-founding of an engineering technical-writing course with Lehigh's ESL director (CV p. 22; see 02 §6.2).

**S3. The department's formal model, which he directs.** [stated, institutional] (P, but not signed)
- Curtis is ISE PhD Program Director (2016-present) and FACET Program Director (2021-present) (CV pp. 29-30).
- The FACET page (engineering.lehigh.edu/ise/facet, read 2026-09-28) states the first-year model: "All Lehigh ISE Ph.D. students are matched with a research advisor in their first year in the program. Students are expected to meet regularly with their research advisors to discuss open questions, attempt to make preliminary progress on a project, and, most importantly, demonstrate their potential for performing research."
- Its goals include: "Providing students opportunities to teach and mentor other students" and "Engaging students in outreach efforts". It also runs "Preparation for an Academic Career (PAC)" meetings "every 3-4 weeks".
- The page is institutional and unsigned. That it is his wording is **not established**. What his own one-to-one meetings look like (how often, what format) was **not found** in any source.

**S4. Co-advising and a supervising pair.** [practice] (P/S)
- Robinson moved from JHU to Lehigh in July 2019 (OptML news, 2019-07-01). Before that he sat on Curtis advisees' committees (Han 2015, Guo 2017).
- From 2020, the Curtis–Robinson pair co-supervises:
  - postdoc O'Neill: "He is supervised by OptML faculty members Frank E. Curtis and Daniel P. Robinson" (OptML news, Sept 2020);
  - student Khatti: "Advisors: Prof. Frank E. Curtis, Prof. Daniel P. Robinson" (Khatti site).
- Robinson is a co-author on most advisee papers from 2020 on: Zhou; Qi Wang (SIOPT 2025, DOI 10.1137/23M1569460); Zebiane (arXiv 2509.00888); L. Guo (arXiv 2510.00417); Khatti (arXiv 2505.15788).
- Zhu is co-advised with Aida Khajavirad (Zhu site).
- [inferred] From 2020 the group looks more like a two-PI lab (the joint "Sufficient Descent Labs" site, the book, NonOpt) than a single-PI group. Note 01 §1.3 finds Robinson the dominant co-author: 49 OpenAlex co-authored works.
- [inferred, unverified] Minhan Li appears as an OptML student presenting on 2018-11-07 (seminar archive). Yet the CV counts him as a Curtis advisee only from 2019. The start coincides with the news, dated 2019-07-01, that Katya Scheinberg had accepted a position at Cornell (OptML news). An advisor handover is possible, but no source says so.

**S5. Postdocs come from peer groups and leave for faculty jobs; PhD students mostly go to industry.** [practice] (P/S)
- Postdoc origins: Berahas (Nocedal, Northwestern); O'Neill (S. J. Wright, UW-Madison, "recipient of a prestigious NSF-funded Computing Innovation (CI) Fellowship", OptML news, Sept 2020); Xin Jiang (Vandenberghe, UCLA).
- All four postdocs now hold faculty posts (Collaborators page; Xin Jiang site).
- Of nine PhD graduates, the Collaborators and OptML People pages give first destinations of:
  - industry for six (IBM, American Express, J.P. Morgan, SAS twice, Amazon);
  - academia for two (Hao Wang at ShanghaiTech; Baoyu Zhou at Chicago Booth, then ASU);
  - a postdoc for one (Qi Wang, Michigan).
- Industry internships during the PhD are common and credited:
  - Han at NEC Laboratories America (Han, PDF p. 5);
  - Zhou at Facebook AI Research (2021) and as an Argonne "Givens Associate" (2020) (Zhou CV p. 1);
  - Samadi's "Operations Research Summer Fellowship, SAS Institute, 2018" (Samadi thesis biography, truncated copy);
  - Wang's "internship programs" (Wang, PDF p. 5).

**S6. Each student carries one of his lines. Freedom within a line is the students' account.** [practice] + [observed]
- Note 01 §1.3 matches each thesis to a Curtis publication line. The chapter lists confirm the thesis form:

| Thesis | Chapters |
|---|---|
| Wang 2015 | Introduction; Background; three algorithm chapters (SQO infeasibility detection; matrix-free solvers for exact-penalty subproblems; dynamic penalty-parameter updating); Conclusion |
| Han 2015 | Introduction; Background and related algorithms; three chapters (globalization of PDAS; PDAS with inexact subproblem solves; PDAS for machine learning); Conclusion; appendix on the `pypdas` package |
| Que 2016 | Introduction; two chapters (adaptive gradient sampling; BFGS gradient sampling); algorithmic extensions; Conclusion |
| Guo 2017 | Introduction; a 30-page Background and literature review (convexity, Lanczos, QR and Cholesky, BB methods); three chapters (R-linear convergence of LMSD; nonpositive curvature in LMSD; limited-memory stochastic gradient); Conclusion |

- Each thesis thus takes the same form as Curtis's own 2007 thesis: introduction and background, then paper-sized chapters (four in his case), then a conclusion.
- The paper-chapters match co-authored journal papers:
  - Burke–Curtis–Wang, SIOPT 2014, DOI 10.1137/120880045;
  - Curtis–Que, MPC 2015, DOI 10.1007/s12532-015-0086-2;
  - Curtis–Han, SIOPT 2016, DOI 10.1137/140993314;
  - Curtis–Guo, IMA JNA 2016, DOI 10.1093/imanum/drv034, and 2017, DOI 10.1093/imanum/drx016.
- Han reports "much freedom" (S2). [inferred] The freedom he describes is freedom *within* the advisor's program. It is not freedom to pick a field. No thesis leaves Curtis's lines.

---

## 3. Layer 7: group habits and lab culture

**G1. The weekly OptML seminar is student-run, and mostly students present papers they have read.** [stated, group site] + [practice] (P)
- The OptML Seminars page (optml.lehigh.edu/seminars, read 2026-09-28) describes the format: "Every week, the OptML group gathers to update each other about their recent work and discuss various problems. In these one hour meetings, one student or faculty member gives a presentation, either to describe what they have learned in the past week or discuss the recent challenges they have been facing. The presentation is interactive with all members of the group participating, asking questions, and offering ideas."
- Archive for Aug 2015 to Apr 2021, which I counted:
  - 139 dated rows (some talks share a date cell): 20 in 2015, 20 in 2016, 22 in 2017, 21 in 2018, 18 in 2019, 27 in 2020 and 11 in spring 2021;
  - 118 speakers labelled "OptML student", 5 postdocs, 5 faculty, 5 guests and 2 visiting students.
- Most student talks link to one or two published papers by others. So the seminar works largely as a **reading group**.
- **Curtis presented 3 times in six years**, each time on a classic tool:
  - 2016-01-28: "Theory of Stochastic Gradient Methods";
  - 2018-10-31: "Theory of BFGS", linked to Byrd & Nocedal, "A Tool for the Analysis of Quasi-Newton Methods with Application to Unconstrained Minimization", SIAM J. Numer. Anal. 1989, DOI 10.1137/0726042;
  - listed under 2019-10-30 (the row shares that date cell with the preceding student talk): "Systematic Insights on the Fisher Matrix and Comments on" Martens, "New insights and perspectives on the natural gradient method", arXiv 1412.1193.
- [inferred] When the advisor presents, he teaches the analysis tools behind a method rather than his own results.
- Record-keeping lapse [practice]: "During this time period [Fall 2021 – Spring 2023], our seminars were listed on Twitter". That period is not archived on the site, and I did not read it.

**G2. The group lives inside COR@L's shared computing and lab infrastructure.** [observed] (S)
- According to Han (PDF p. 5), COR@L lab members provided "strong technical support without which most of the numerical results would not be available".
- According to Que (PDF p. 5), "most of the numerical experiments presented in this thesis were performed using software and hardware in COR@L", with support "in part by NSF grant DMS-1016291".
- Curtis maintained the COR@L website from 2010 to 2018 (CV p. 8).
- [inferred] Resource context: a departmental cluster and lab-maintained software, not national HPC. This matches 03 PE36.

**G3. Service and organising are part of training.** [practice] (P/S)
- Curtis has been "INFORMS Chapter Advisor 2014 – present" (CV p. 30).
- Students take visible roles:
  - Zebiane "served as the President of the Lehigh INFORMS Student Chapter for the 2024-2025 academic year" and received the "RCEAS Graduate Student Leadership and Service Award on April 25, 2025" (Zebiane site);
  - Samadi's biography lists an "INFORMS Magna Cum Laude award for Lehigh University INFORMS Student Chapter, 2015";
  - Khatti "Co-chaired Lehigh ISE's optimization week: GradOpt, MOPTA 2026, and ColOpt" and "Led an OptML group tutorial at Lehigh ISE on LLMs, Transformers, and Hugging Face" (Khatti site, 2026).
- The organising model comes from the PI's own habits: MOPTA website 2010-13, ICCOPT 2022 co-organised with Robinson, and the 2016 US-Mexico workshop (CV pp. 8-9).

**G4. A structured first-year programme and hard formatting rules.** [stated] (P). See 02 §6 and §7.3 for the full text.
- ISE 403 *Research Methods* (required for all ISE PhD students) aims to help students "Develop a firm understanding and appreciation for the expectations of a doctoral student in engineering and how they differ from those of an undergraduate or master's student". Its course project is a "research proposal" (syllabus, Fall 2025).
- ISE 417 *Nonlinear Optimization* (required for first-year PhD students, CV p. 22) states its coding rules in the Spring 2019 syllabus: "All coding must be done in Matlab." "The grade for the project will be based on the quality of your report, the correctness of the code, and the comments/documentation that you provide. When in doubt, comment every line of your code."
- The same syllabus says the final exam is "a cumulative, closed-book, closed-notes, oral exam" and that "Homework solutions and the project report must be submitted as documents produced with LaTeX. There are no exceptions to this requirement."
- [inferred] Students arrive at research with a shared toolchain and a documentation habit that the advisor graded. The oral final exam rehearses defending mathematics aloud.

**G5. Whole-cohort projects (2026).** [practice] (P)
- arXiv 2605.06945, "Low-Order Explicit Hessian Imitation Method for Large-Scale Supervised Machine Learning" (v1 2026-05-07), lists six students and Curtis last: Zhu, L. Guo, Khatti, Qu, Wu, Zebiane, Curtis.
- Four of the authors are his own advisees (Zhu, L. Guo, Khatti, Zebiane). Qu and Wu are OptML PhD students not listed as Curtis advisees. Both co-author with Curtis and Robinson (Curtis, Qu, Robinson, arXiv 2512.23166; Wu, Curtis, Robinson, arXiv 2409.09532).
- This paper does not fit his earlier pattern of one line per student. It appeared three years after a four-student cohort entered together in 2023 (CV p. 24).
- [inferred] It looks like a group project run as a training exercise or a fast exploratory bet in ML-optimizer design. No source says why it was organised this way.

**G6. How he says he regards students.** [stated] (P quote in a secondary article)
- Lehigh news on his NSF and AFOSR awards (undated, 2025 or 2026): "Beyond the scientific contributions that they will enable, what is most meaningful to me is that these projects will support incredibly talented doctoral students who inspire me every day."
- The epigraph he chose for his Collaborators/Students/Postdocs page is from Frank Herbert, *Dune*: "And the first lesson of all was the basic trust that he could learn. It is shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult. Muad'Dib knew that every experience carries its lesson."
- [inferred] The epigraph signals a belief that research skill can be learned. It is a selection, not a statement of method.

---

## 4. Tacit knowledge: what the students' theses show the group assumes

These items come from the students' own theses. They are the working norms a student in the group seems to absorb. Each one is [practice] (S: the student wrote it, under Curtis's supervision) unless marked otherwise.

**T1. When codes are in different languages, do not compare CPU time. Compare iterations and evaluations, and argue that per-iteration costs are equal.**
- Que 2016 (PDF p. 92): "Since the codes are written in various languages and were run in different environments (i.e., compiled C++ code versus Matlab), we ignore CPU time and focus on the performance measures of iterations, function evaluations, and gradient evaluations required until termination."
- The same passage adds the claim that "one should expect success in terms of CPU time if all codes were implemented in the same language".

**T2. Do not let your own termination flag decide who "succeeded" in a profile.**
- Que 2016 (PDF p. 94, printed p. 84): "if we only considered a termination flag of type (1) to be the indicator for a successful run, then the profiles would be skewed in favor of the codes that yielded such a flag most often (namely, ours), even though we often found that other runs also yielded good quality solutions". The thesis therefore counts all runs as successful and reports the flag counts separately (Table 3.3).
- [inferred] This worry about benchmarking bias in nonsmooth methods is the same problem that the later relative-minimization-profile method addresses (Curtis–Mitchell–Overton 2017, DOI 10.1080/10556788.2016.1208749). Note 02 covers that method.

**T3. The language is the student's choice; the fairness rule stays fixed.** [practice]
- Wang 2015 used Python (PDF p. 129: "The algorithms were implemented in Python using the NumPy and SciPy packages; in particular, we used the versions Python 2.7, Numpy 1.6.1, SciPy 0.12.0").
- Han 2015 used Python and released `pypdas` (PDF p. 22: "The package is implemented in Python and available as open-source, which should facilitate other researchers efforts in the study of PDAS methods").
- Que used C++ (BFGS-GS).
- Guo 2017 used Matlab (PDF p. 108: the algorithm "was implemented in Matlab along with two other algorithms for comparison purposes").
- Curtis's own released research codes are Matlab ("Code written by me", CV pp. 7-8), and NonOpt is C++.
- [inferred] In 2009-17 no house language was imposed on PhD research, even though the course required Matlab. Consistency was demanded in how codes were compared, not in what they were written in. Note 03 (PE21, PE33) shows that later students write inside Curtis's house framework, with the PI consolidating.

**T4. Your code may become part of a group solver, and you are credited by component.** [practice] (P)
- The NonOpt project page lists its developers with roles:
  - "Frank E. Curtis — main developer";
  - "Lara Zebiane — interior-point subproblem solver";
  - former developers "Baoyu Zhou — active-set subproblem solver" and "Minhan Li — inexactness and aggregation conditions".
- The NonOpt git log (cloned 2026-09-28) has 90 commits:
  - 78 under Curtis's identities (`frank.e.curtis`, `frankecurtis`, `Frank E. Curtis`);
  - 10 by `mil417` (Minhan Li), 2019-09 to 2020-05, e.g. "added new inexact termination and corresponding Hessian approximation";
  - 2 by Zebiane as pull requests ("Pull Interior Point Method Solver (#1)", 2025-01-31; "Python Interface (#2)", 2026-02-10).
- No commit by Zhou appears. The repository was created 2019-06-25 by importing "all files from previously used repository". Zhou's master's thesis was on the QP subproblem solver (CV p. 29).
- See 03 PE21 and PE35 for the pattern of student prototype, PI consolidation and AUTHORS credit.
- [inferred] A student's thesis component can outlive the student inside the group's solver. The master's thesis to active-set solver to NonOpt path (Zhou) is one example.

**T5. Write the background chapter as a textbook primer.** [practice] Guo's 30-page Background and literature review (PDF pp. 7-8, contents) starts from convexity, Lipschitz continuity, SPD matrices, Krylov subspaces, Lanczos, QR and Cholesky before it reaches BB methods. [inferred] The thesis is written for a reader outside the subfield, much like the "conversational" style of the Curtis–Robinson book (see 02 §6.2). This is a single example. I did not check it across theses.

**T6. The whole OptML faculty mentors, not only the advisor.** [observed] (S)
- According to Guo (PDF p. 5), Takáč "has selflessly shared with me many of his helpful experiences and has given me guidance on research topic selections as well as presentation strategies", and Scheinberg taught optimization and ML "through the courses she taught".
- According to Han, Scheinberg exposed him "to machine learning topics" and Ralphs pushed him "to the world of advanced computing".
- According to Mohammadisiahroudi, a Terlaky student (2024, acknowledgements), Curtis is among "other faculty members" thanked "for their invaluable advice and support throughout my PhD journey".
- Suyun Liu, a Vicente student (2022, acknowledgements), thanks Curtis, Fliege and Xie "for sitting on my committee and bringing insightful comments and suggestions to my research proposal and dissertation".

---

## 5. Layer 6: writing, credit and author order

**W1. Author order: alphabetical by default, student-first in ML-convention venues.** [stated] + [practice] (P)
- CV footnote 1 (p. 2): "Standard practice in my research field is to list authors alphabetically, as is done for most of the articles in this section."
- DBLP (76 records, from note 01): 62 of 74 multi-author records are alphabetical. The student- or postdoc-first exceptions checked on arXiv this run are:
  - Han & Curtis, arXiv 1508.02452;
  - Wu, Curtis & Robinson, arXiv 2409.09532;
  - Khatti, Robinson & Curtis, arXiv 2505.15788;
  - Wang, Piermarini, Zhu & Curtis, arXiv 2601.11795;
  - Zhu, Guo, Khatti, Qu, Wu, Zebiane & Curtis, arXiv 2605.06945;
  - Dinç Yalçın & Curtis, OMS 2024, DOI 10.1080/10556788.2023.2296432 (Crossref).
- Advisee papers in optimization journals stay alphabetical even when the student leads:
  - Curtis & Wang, SIOPT 2023, DOI 10.1137/22M1492428;
  - Curtis, Robinson & Zebiane, arXiv 2509.00888;
  - Curtis, Guo & Robinson, arXiv 2510.00417;
  - Berahas, Curtis & Zebiane, arXiv 2604.00278.
- The convention passes to students. Baoyu Zhou's CV (rev. 2026-07-14, p. 2) says: "All publications with '∗' sign on my name indicates the author list is arranged in alphabetical order." It also underlines his own students, so author order no longer carries the credit.
- [inferred] What a student learns: in this group, author position does not tell who did the work. Credit is carried elsewhere: in who gives the talk, who is thesis owner, and component credits in software (T4).

**W2. Writing and presentation coaching is personal and repeated.** [observed] (S) Guo and Wang (S2) both name writing and communication advice. Curtis's stated position (LaTeX mandatory, and technical writing as a core PhD skill) is in 02 §6.2. [inferred] The coaching is part of individual supervision, not only of the course.

---

## 6. Failures, corrections and abandoned work (mentorship-relevant)

- **Attrition.** Jiaxin Liu, co-advised with Terlaky (2010-13), "left program prior to completing proposal" (CV p. 25). [practice] (P) The CV records it openly and does not delete it. No reason is given.
- **Public errata on three student-coauthored papers.** The Errata page (read 2026-09-28) corrects:
  - Corollary 3.14 in Berahas–Curtis–Robinson–Zhou, SIOPT 2021, DOI 10.1137/20M1354556;
  - Lemma 3.19 in Curtis–Robinson–Samadi, MP 2017, DOI 10.1007/s10107-016-1026-2;
  - Lemma 4.9 in Burke–Curtis–Wang, SIOPT 2014, DOI 10.1137/120880045.

  Its preamble: "My collaborators and I spend countless hours trying to ensure that all details in our published articles involve no mathematical errors. These articles are also put through multiple rounds of revision before they are published. However, it is inevitable that some errors can still fall through the cracks." [stated + practice] (P)
  - All three listed errata concern papers from a student's thesis line. **No source says who made or found the errors.** Nothing here should be read as blaming students.
  - Note 03 PE26 describes the format of the corrigenda.
  - [inferred] The group's standard, as a student would meet it: errors in theses-derived papers are corrected publicly by the PI, with the result restated and the full proof redone.
- **Student work parked, not merged.** Minhan Li's dissertation algorithm for general constraints was merged into a side branch `inequality` of StochasticSQP, not `master` (03, artifact timeline, 2022-01-21). [practice] (P) No paper from that branch appears in DBLP or the CV (checked this run).
- **Archival gaps in the group record.** OptML news and seminars for Fall 2020 to Spring 2023 exist only on Twitter. The Collaborators page affiliations are out of date (see Contradictions). [practice] (P)

---

## 7. Era and resource context

| Period | Supervision setting | Evidence |
|---|---|---|
| 2003-07 (as a student) | Nocedal–Byrd group at Northwestern; KNITRO source access; Intel internship | own thesis (PDF p. 5); CV p. 1 |
| 2007-09 (postdoc) | Courant, with Overton; co-advises Tim Mitchell's code | CV p. 8; Mitchell thesis p. iv |
| 2009-15 | New assistant professor, 27-28 years old (born 1981, About page). Takes two PhD students in his first semester (Wang, Que). Single-PI NSF DMS-1016291 (Que acknowledgements). COR@L computing | CV; theses |
| 2015-19 | OptML founded with Scheinberg and Takáč (2015). Weekly student seminar. ML turn. Sabbatical 2017-18 at Columbia (Goldfarb), NYU (Overton), JHU (Robinson) and Northwestern (Nocedal, Wächter). First postdoc (Berahas, 2018) | OptML news 2017-08-28, 2018-09-01 |
| 2019-24 | Robinson at Lehigh; co-supervision. Postdocs O'Neill, Dinç Yalçın, Jiang. COVID-era Zoom (ISE 403 syllabus Zoom rules). ICCOPT 2022 hosted | OptML news; CV |
| 2023- | Four-student cohort (2023). NonOpt as a group solver with PR-based student contributions. Whole-cohort ML paper (2026). AI-agent code pass on NonOpt (2026, see 03 PE22) | CV; NonOpt git; arXiv 2605.06945 |

---

## Contradictions (kept, not reconciled)

1. **CV author order versus arXiv.** The CV lists [82] as "Frank E. Curtis Zahra Khatti, Daniel P. Robinson" (p. 7). arXiv 2505.15788 lists Khatti, Robinson, Curtis, and Khatti's site calls it "first-author work". The CV lists [83] as "Frank E. Curtis and Zheng Han". arXiv 1508.02452 lists Han, Curtis. Yet CV entries [72] (Wang, Piermarini, Zhu, Curtis) and [81] (Wu, Curtis, Robinson) keep the student-first order. The CV is inconsistent about student-first papers.
2. **Stated academic-career goal versus PhD outcomes.** The FACET page aims to "Motivate students to pursue careers in academia". Six of nine Curtis PhD graduates went first to industry (S5), while all four postdocs went to faculty posts. Caveat: FACET dates from 2021, after most of these students graduated.
3. **"Freedom to pursue projects" versus one-line-per-student.** Han reports "much freedom and encouragement to pursue projects that best suit my ability and interest". The thesis record shows every thesis on a Curtis research line (S6; 01 §1.3). Both can be true (freedom within a line). I leave them as stated.
4. **Stale or inconsistent records.**
   - Collaborators page affiliations are out of date: Baoyu Zhou at "University of Chicago, Booth School of Business", but his own CV shows ASU assistant professor since July 2024; Xin Jiang at "Cornell University", but his site shows University of Houston.
   - Que: CV "Graduated Fall 2015", Preserve record year 2016.
   - Samadi: CV "Graduated Fall 2018", his thesis biography "Sep 2013–Jan 2019".
   - Minhan Li: an OptML student from 2018 at the latest (seminar archive), a Curtis advisee "2019 – 2021" (CV).

   These do not bear on method. They are recorded so no one copies them as facts.

## Gaps (what I could not find)

- **Dissertations not read.** Samadi 2018: only the biography and appendix survive in the truncated 1 MiB archive copy, so the acknowledgements were not read. Rui Shi 2020: the archived PDF returns 404. Minhan Li 2021, Baoyu Zhou 2022 and Qi Wang 2025: on the new Lehigh Preserve behind a bot check, with no archive copy found. OpenAlex and Semantic Scholar searches returned HTTP 429/503 throughout this run. Their acknowledgements would be the best evidence on the 2018-25 supervision style, which is the co-advising era.
- **Master's and undergraduate theses** (W. Zhang, J. Liu, B. Zhou MS, M. Liu): not found online, not read.
- **Postdoc accounts.** Berahas's site returned 403 and O'Neill's page 404. None of the four postdocs has a public account of working with Curtis that I found.
- **Meeting practice.** How often he meets students one-to-one, whether he runs a separate group meeting besides OptML, how topics are assigned, and how drafts are reviewed: none of these was found in any source. FACET's "meet regularly" is institutional boilerplate.
- **What students say informally.** No blogs, interviews, memorial pieces, lab or onboarding guides, or Festschrift were found. LinkedIn profiles were not used (login wall). Twitter/X seminar listings for 2021-23 were not read.
- **Reasons behind the whole-cohort 2026 paper** (G5) and behind the parked `inequality` branch (§6): not stated anywhere I found.
- **Funding per student** (RA versus TA, grant mapping): only Que's NSF acknowledgement and Han's "generous (both financially ...)" were found.
- **ISE 403 lecture content**: behind a login, not read (as in 02).

## Sources

Primary (Curtis's own material, group pages he co-runs, bibliographic records):
1. Curtis, F. E. *Curriculum Vitae*, last revised 2026-04-07. https://coral.ise.lehigh.edu/frankecurtis/files/cv/cv.pdf. Primary.
2. Curtis, F. E. "Collaborators/Students/Postdocs" page (undated, read 2026-09-28). https://coral.ise.lehigh.edu/frankecurtis/collaborators/. Primary.
3. Curtis, F. E. *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, PhD thesis, Northwestern University, June 2007. http://coral.ise.lehigh.edu/frankecurtis/files/dissertations/Curt07.pdf. Primary.
4. Curtis, F. E. "Errata" page (undated, read 2026-09-28). https://coral.ise.lehigh.edu/frankecurtis/errata/. Primary.
5. Curtis, F. E. "About me" page (undated, read 2026-09-28). https://coral.ise.lehigh.edu/frankecurtis/about/. Primary (birth year only).
6. Curtis, F. E. ISE 403 *Research Methods* syllabus, Fall 2025 (also Fall 2023 and 2024). https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2025FallISE403.pdf. Primary.
7. Curtis, F. E. ISE 417 *Nonlinear Optimization* syllabus, Spring 2019. https://coral.ise.lehigh.edu/frankecurtis/files/syllabi/2019SpringISE417.pdf. Primary.
8. OptML @ Lehigh, home and news page (read 2026-09-28). https://optml.lehigh.edu/. Primary (group site co-run by Curtis).
9. OptML @ Lehigh, People page. https://optml.lehigh.edu/people/. Primary (group site).
10. OptML @ Lehigh, Seminars page, archive Aug 2015 to Apr 2021. https://optml.lehigh.edu/seminars/. Primary (group site).
11. NonOpt project page (developers list), undated, read 2026-09-28. https://frankecurtis.github.io/NonOpt/ (linked from Sufficient Descent Labs, https://sufficientdescent.github.io/). Primary.
12. NonOpt git repository, commit log (90 commits, 2019-06-25 to 2026-07-31). https://github.com/frankecurtis/NonOpt. Primary.
13. arXiv abstract records, read 2026-09-28: 1508.02452 (Han, Curtis 2015); 2409.09532 (Wu, Curtis, Robinson 2024); 2505.15788 (Khatti, Robinson, Curtis 2025); 2601.11795 (Wang, Piermarini, Zhu, Curtis 2026); 2604.00278 (Berahas, Curtis, Zebiane 2026); 2503.22826 (Curtis, Zebiane 2025); 2605.06945 (Zhu, Guo, Khatti, Qu, Wu, Zebiane, Curtis 2026); 1412.1193 (Martens). Primary (bibliographic).
14. Crossref metadata for DOIs 10.1137/0726042, 10.1137/120880045, 10.1007/s10107-016-1026-2, 10.1137/20M1354556, 10.1080/10556788.2016.1208749, 10.1007/s12532-015-0086-2, 10.1137/140993314, 10.1287/ijoo.2022.0073, 10.1080/10556788.2023.2296432, 10.1137/22M1492428, 10.1287/ijoo.2018.0010, 10.1093/imanum/dry022, 10.1137/16M1108650, 10.1007/s10107-021-01621-6, 10.1137/1.9781611978599, 10.1093/imanum/drv034, 10.1093/imanum/drx016. Primary (bibliographic).
15. DBLP records for pid 61/7604 (76 records, harvested by research agent 01, reused). https://dblp.org/pid/61/7604. Primary (bibliographic).
16. Byrd, R. H. and J. Nocedal. "A Tool for the Analysis of Quasi-Newton Methods with Application to Unconstrained Minimization", SIAM J. Numer. Anal., 1989. DOI 10.1137/0726042. Primary (record only, not read; cited as the paper Curtis presented).
17. Curtis, F. E., T. Mitchell and M. L. Overton. "A BFGS-SQP method for nonsmooth, nonconvex, constrained optimization and its evaluation using relative minimization profiles", Optim. Methods Softw. 32(1), 2017. DOI 10.1080/10556788.2016.1208749. Primary (record; content in notes 01 to 03).
18. Burke, J. V., F. E. Curtis and H. Wang. "A Sequential Quadratic Optimization Algorithm with Rapid Infeasibility Detection", SIAM J. Optim., 2014. DOI 10.1137/120880045. Primary (record and corrigendum on the Errata page).

Secondary (students', postdocs' and colleagues' accounts; institutional pages):

19. Guo, W. *Limited Memory Steepest Descent Methods for Nonlinear Optimization*, PhD dissertation, Lehigh University, May 2017 (Theses and Dissertations 2621). Archived at https://web.archive.org/web/20200322040506/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3621&context=etd. Secondary.
20. Wang, H. *Practical Enhancements in Sequential Quadratic Optimization: Infeasibility Detection, Subproblem Solvers, and Penalty Parameter Updates*, PhD dissertation, Lehigh University, 2015 (etd 2862). Archived at https://web.archive.org/web/20200318151147/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3862&context=etd. Secondary.
21. Han, Z. *Primal-Dual Active-Set Methods for Convex Quadratic Optimization with Applications*, PhD dissertation, Lehigh University, 2015 (etd 2626). Archived at https://web.archive.org/web/20200322073308/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3626&context=etd. Secondary.
22. Que, X. *Randomized Algorithms for Nonconvex Nonsmooth Optimization*, PhD dissertation, Lehigh University, record year 2016 (etd 2774). Archived at https://web.archive.org/web/20200319034744/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=3774&context=etd. Secondary.
23. Samadi, M. *Efficient Trust Region Methods for Nonconvex Optimization*, PhD dissertation, Lehigh University, 2018/19 (etd 4370). Archived at https://web.archive.org/web/2020/https://preserve.lehigh.edu/cgi/viewcontent.cgi?article=5371&context=etd. The copy is truncated: biography and appendix only. Secondary.
24. Internet Archive capture of the Lehigh Preserve ISE dissertation listing, 2020-11-11. https://web.archive.org/web/20201111152635/https://preserve.lehigh.edu/engr-industrial-dissertation/. Secondary (finding aid).
25. Mitchell, T. *Robust and efficient methods for approximation and optimization of stability measures*, PhD thesis, NYU Computer Science, September 2014. https://cs.nyu.edu/media/publications/mitchell_tim.pdf. Secondary.
26. Liu, S. PhD dissertation, Lehigh University ISE, May 2022 (Curtis as committee member). https://preserve.lehigh.edu/_flysystem/fedora/2023-11/preserve30750.pdf. Secondary.
27. Mohammadisiahroudi, M. *Quantum Computing and Optimization Methods*, PhD dissertation, Lehigh University, August 2024. https://preserve.lehigh.edu/_flysystem/fedora/2025-02/Mohammadisiahroudi_lehigh_0105A_12945.pdf. Secondary.
28. Zhou, B. *Curriculum Vitae*, last revised 2026-07-14, and personal site. https://baoyuzhou18.github.io/cv_BaoyuZhou.pdf. Secondary.
29. Wang, Q. personal site (read 2026-09-28). https://sites.google.com/view/qi-wang. Secondary.
30. Khatti, Z. personal site (read 2026-09-28). https://zahrakhatti.github.io/. Secondary.
31. Zebiane, L. personal site (read 2026-09-28). https://coral.ise.lehigh.edu/laz223/. Secondary.
32. Zhu, Y. personal site (read 2026-09-28). https://www.yunlangzhu.com/. Secondary.
33. Jiang, X. personal site (read 2026-09-28). https://jiangxjames.github.io/. Secondary.
34. Mitchell, T. personal site (home, research and software pages, read 2026-09-28). http://www.timmitchell.com/. Secondary.
35. Lehigh ISE. "Lehigh ISE Future Academic Career Experiential Training Program (FACET)" (undated, read 2026-09-28). https://engineering.lehigh.edu/ise/facet. Secondary (institutional; program directed by Curtis per CV).
36. Lehigh Rossin College news. "Frank E. Curtis awarded two federal grants to advance optimization research" (undated, 2025 or 2026). Page saved by research agent 02 (engineering.lehigh.edu news). Secondary (contains a primary quote).
37. Lehigh Rossin College news. "Highly cited paper co-authored by ISE professor Frank E. Curtis emerges as a go-to resource ..." (undated). https://engineering.lehigh.edu/node/13332. Secondary.
38. Research notes 01-publications.md, 02-methodology.md and 03-process-evidence.md of this skill (same run), cross-referenced for authorship statistics, the syllabus analysis and the git-history analysis. Secondary (internal).
