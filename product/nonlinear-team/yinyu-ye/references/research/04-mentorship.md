# 04 · Students and collaborators (how Yinyu Ye supervised, and what his group knew)

- **Researcher:** Yinyu Ye (叶荫宇). PhD Stanford 1988 (Engineering-Economic Systems). University of Iowa 1988–2002. Stanford MS&E (K. T. Li Professor, now Emeritus), 2002–2024. Since 2024 he has also held posts at SJTU Antai and fractional visiting posts at SIMIS, CUHK-Shenzhen and HKUST [S1].
- **Dimension:** Agent 04: students and collaborators. Covers supervision style, group habits, lab culture and tacit knowledge.
- **Research date:** 2026-09-28
- **Sources consulted:** 34 documents (S1–S34 below). They fall into these groups:
  - **Seven PhD theses whose front matter and acknowledgements I read** [S4–S10]: Anthony So 2007, Holly Jin 2005, Nicole Taheri 2012, Santiago Akle Serrano 2015, Ding Ma 2018, Ron Estrin 2019 and Oliver Hinder 2019. For Hinder I also read the abstract, the chapter bylines and the conclusion of chapter 8.
  - **One genealogy record** (MGP, with 16 student sub-pages).
  - **Seven student or postdoc homepages** (Hinder, So, X. Li, C. Sun, Chuwen Zhang, Wenzhi Gao, Ruoyu Sun).
  - **The programme of the 2024 retirement celebration.**
  - **Ye's own texts:** CV, 2009 prize speech, 2020 first-person profile, 1996 book preface, 2023 slides and three course pages.
  - **Five Chinese-language reports or transcripts.**
  - **One code repository** (DRSOM.jl: README and git log).
  - **Bibliographic checks:** four arXiv abstract pages, Ye's DBLP record (330 records, fetched 2026-09-28 through the DBLP SPARQL endpoint) and about 30 Crossref DOI lookups.
  - **Search budget:** 2 WebSearch calls. Everything else came from curl or WebFetch on known URLs.
- **User-supplied material:** none. `references/sources/{papers,talks,essays,software}` hold only `.gitkeep`, and `private/` was not opened.

**What kind of evidence this is.** I found no student blog post about Ye as a supervisor, and no lab guide, onboarding document, group web page, Festschrift volume or memoir. Guessed group-page URLs on his site return 404, and the talks at the 2024 retirement celebration survive only as titles and abstracts. The evidence therefore comes from four places:

1. **Dissertation acknowledgements.** They are formal, public and written at graduation, and the genre praises by default. What carries information is **what differs between students**: which traits each one singles out, which co-advisor gets credit for what, and what they admit went wrong.
2. **Signature pages, MGP and the CV.** Together they show who formally advised whom and how often the supervision was shared.
3. **Students' own homepages and the 2024 celebration programme.** These show where students went, how they describe their tie to Ye, and which lines of work they still carry on.
4. **Co-authorship and code** (DBLP, DRSOM.jl). These show whether alumni keep working with him and who actually writes the code.

**Tags.**
- **[stated]**: Ye said or wrote it (primary).
- **[practice]**: what the record shows was done (papers, signature pages, code, course rules).
- **[observed]**: what a student or colleague says about him (first-hand for the student, but **secondary** as evidence about Ye).
- **[inferred]**: my reading, to be checked.

PDF text extraction lost word spacing in three places (Hinder thesis p. v, *Interior Point Algorithms* preface p. xiv, Taheri thesis p. vi). In those quotes I restored the spaces and ligatures only; the words are unchanged. Chinese is quoted in the original, followed by an English translation marked **[tr.]**.

---

## A. Who his students were (verified roster)

### A.1 Three advisee records compared

| Record | What it lists | Note |
|---|---|---|
| CV, "Ph.D. Dissertation Advisees" (updated Oct 2025) [S2] | 34 lines: 6 Iowa/visiting and 28 Stanford. "Zhishu Zhu 2010" and "Zhisu Zhu 2017" may be the same person. **Iowa:** Kaliski 1992, Bosch 1994 (Co-DA), Huang 1995, Andersen 1996 (visiting, "U of Denmark", "Founder of MOSEK.com"), Qian 1997 (Co-DA), Benson 1999. **Stanford 2004–2024:** J. Zhang, So, Biswas, Peters, Ge, Carlsson, Delage, Zhu, Agrawal, Z. Wang, Qi Qi, Taheri, Ding (Co-DA), Eberhart (Co-DA), Dalal ("Danal", Co-DA), Akle (Co-DA), Nguyen (Co-DA), Wen, Post, Shamsi, Zhu, Estrin (Co-DA), Hinder, Wu, X. Li, G. Chen (Co-DA), M. Zhu (Co-DA), C. Sun. **Postdocs:** Dachuan Xu 2006, Roger Behling 2014, Ruoyu Sun 2017 | [practice] primary. 10 of the 34 lines are marked "Co-DA"; Andersen is marked "Visiting". "Last known position" is often stale (see G) |
| Mathematics Genealogy Project id 12397 [S3] | "16 students and 29 descendants". It adds two names the CV lacks or spells differently: **Zhaonan Qu** (Stanford 2024, "Topics in Econometrics and Optimization", Advisor 1 Guido Imbens, Advisor 2 Ye) and **Santiago Akle Serrano** (2015, Advisor 1 Michael Saunders, Advisor 2 Ye; this is the CV's "Tiago Akle 2014* (Co-DA)") | [practice] secondary (community-submitted) |
| Thesis signature pages [S4–S10] | So 2007: "(Yinyu Ye) Principal Co-Advisor" with "(Rajeev Motwani) Principal Co-Advisor". Akle 2015: "Michael Saunders, Primary Adviser", "Yinyu Ye, Co-Adviser". Estrin 2019: "Yinyu Ye, Primary Adviser", "Michael Saunders, Co-Adviser". Hinder 2019: "Yinyu Ye, Primary Adviser" (readers Saunders and Sidford) | [practice] primary |

Thesis titles, as given by MGP [S3] (they show the range of topics he supervised):
- *Iowa:* Kaliski 1992, "A Decomposition Variant for Large Scale Linear Programming". Hung 1994, "An Asymptotical O(Sqrt(N)L)-Iteration Path Following Linear Programming Algorithm that Uses Wider Neighborhood and Its Implementation". Benson 1998, "Solving Large-Scale Combinatorial Optimization Problems". Qian 1997, "Efficient Operations Planning and Its Integration with Cost Accounting". Bosch 1993, "Quantile Regression with Smoothing Splines" (Advisor 1 Woodworth).
- *Stanford:* J. Zhang 2004, "Approximation Algorithms for Facility Location Problems". Biswas 2007, "Semidefinite Programming Approaches to Distance Geometry Problems". So 2007, "A Semidefinite Programming Approach to the Graph Realization Problem: Theory, Applications and Extensions". Ge 2009, "Geometric Rounding: Theory and Application". Carlsson 2009, "Map Segmentation Algorithms for Geographic Resource Allocation". Delage 2009, "Distributionally Robust Optimization in context of Data-driven Problems". Z. Wang 2012, "Dynamic Learning Mechanisms in Revenue Management Problems". Ding 2012 (with Zenios), "A Scoring-based Ranking System and Its Application in Cadaver Kidney Allocation". Wen 2014, "Waterflood optimization using streamlines and reservoir management risk analysis with market uncertainty".

Theses not in MGP, from the documents themselves:
- Taheri 2012 (ICME), "Linear Optimization Methods for Vehicle Energy and Communication Networks" [S6].
- Estrin 2019 (ICME), "The Merits of Keeping it Smooth: Iterative Linear Solvers and a Smooth Exact Penalty Function for Constrained Nonlinear Optimization" [S8].
- Hinder 2019 (MS&E), "Principled Algorithms for Finding Local Minima" [S10].

**Recent members who are not in the CV** (this settles an open question in 01-publications §1.3):
- **Chuwen Zhang:** "I received my PhD at Shanghai University of Finance and Economics in 2025, advised by Prof. Yinyu Ye and Dongdong Ge." [S17] [observed, self-description]
- **Wenzhi Gao:** "a fourth-year Ph.D. student in the Institute for Computational and Mathematical Engineering (ICME) at Stanford University advised by Professor Madeleine Udell . I also work closely with Professor Yinyu Ye." [S18] [observed]
- **Xiaocheng Li:** "advised by Prof. Kay Giesecke, Prof. Markus Pelger, and Prof. Yinyu Ye" [S15]. The CV lists him without a Co-DA mark. [observed]
- **Chunlin Sun** (ICME): "very fortunate to be advised by Professor Yinyu Ye" [S16]. [observed]
- **Ruoyu Sun, postdoc:** "Post-doctoral Scholar, Dept. of Management Science and Engineering, Stanford University (host: Yinyu Ye), 2015-2016" [S19]. The CV says 2017. [observed]

### A.2 Who kept working with him after graduating (DBLP, Ye's record, 330 entries) [S31]

[practice] primary (bibliographic). Counts are joint records with Ye in DBLP. "After" means records dated after graduation year + 1.

| Alumnus (grad) | Joint records, span | After graduation | Pattern |
|---|---|---|---|
| Dongdong Ge (2009) | 37, 2011–2026 | 37 | Long-term partner. Co-leads the solver work (COPT, DRSOM line) |
| Jiawei Zhang (2004) | 27, 2002–2013 | 12 | Long partnership (approximation, facility location), then stops |
| Anthony Man-Cho So (2007) | 20, 2005–2016 | 9 | SNL and SDP line, continued as faculty at CUHK |
| Zizhuo Wang (2012) | 17, 2008–2026 | 9 | Online LP, then COPT (co-author of arXiv 2208.14314) |
| Erick Delage (2009) | 7, 2009–2025 | 5 | Occasional |
| Oliver Hinder (2019) | 6, 2018–2025 | 4 | Returns to co-author with the next cohort (Qu, Gao): "Optimal Diagonal Preconditioning", *Operations Research* 73(3) 2025, DOI 10.1287/opre.2022.0592 |
| Ruoyu Sun (postdoc 2015–16) | 5, 2016–2025 | 4 | Occasional |
| Biswas (2007), Taheri (2012), Ding (2013), Post (2015), Kaliski (1992) | 3–4 each | 0 | Co-author only during the PhD |
| Ron Estrin (2018/19), Akle (2014/15), Dalal, Eberhart, Wen | 0 | 0 | Formal or co-advised supervision with no joint paper in DBLP |

- [inferred] The group has two tiers. A handful of alumni become lifelong co-authors and co-leaders of a research line: Ge, J. Zhang, So, Wang. Many others publish with him only while they are students.
- [inferred] The zero-paper co-advisees are cases of formal supervision (see B.3).
- Caveat: DBLP's name disambiguation is imperfect. "Qi Qi" gives 8 records in 2020–2026 that may belong to another person, so that row is left out.

---

## B. Layer 7: research organisation (supervision, collaboration, lab culture)

### B.1 How he himself was mentored (the model he says he copies)

- [stated] primary, 2020 [S20]: "My first mentor was George Dantzig … George was a great advisor. I actively sought out his advice and showed him my research ideas. Thanks in large part to him, I published three papers while I was working on my PhD. I continued to seek George's advice long after I earned my doctorate and even after he retired." The "second important mentor was David Luenberger", and "A third mentor was Michael Todd, at Cornell University … He invited me to do postdoctoral work at Cornell, and we went on to write quite few papers together".
- [stated] primary, 2020 [S20], under the editor's heading "Mentoring as coaching": "One way mentors help the next generation of researchers is by introducing them to other people in the field. Your career isn't just your research. It's a network."
- [stated] primary, 2009 [S21]: the early interior-point community was "a wonderful, unselfish, and supporting group in a very competitive research environment. Everyone was cheering for everyone else; it was like a family." He adds: "Especially, Pete has been a mentor for me. His devotion and love for OR&MS set a role model for me to follow."
- [practice] primary [S2]: in 1987 he was a "Visiting Ph.D. Student of Michael Todd" at Cornell. He later hosted a visiting PhD student himself: Erling Andersen, from Denmark, in 1996.
- [inferred] What he inherited has three parts: a student brings ideas to the advisor, the advisor stays available for decades, and the advisor's main gift is a network. B.3 and A.2 show him repeating each part.

### B.2 Supervision style as he states it and as students describe it

**Stated (Ye, primary):**
- 2020 [S20]: "As a professor, I like students who have a great intellectual curiosity and who are willing to look into open questions that have been studied but not solved. I challenge them to do some research around that topic, and then we hold weekly meetings and continue working together. My proudest moments are when students come into my office and tell me they have found something really eye-opening, that they've conquered a scientific mystery."
- 2020 [S20]: "After all these years, I still advise my students to take an interest in sports. I learned a lot from playing basketball: the importance of training hard, of team-work, of competitive spirit, but also playing by the rules."
- 2023 slides, "Advises to Students" [S22]: "Be Grateful and Hopeful: no envy and nor self-doubt / Be Kind and Tolerant: love others and love yourself too / Have a Specialty: find something deep and interesting / Have a Hobby: find something to relax / Have a Faith: find something to believe". Under "Research Style" the same deck lists "Individual vs Group" and "In mind vs On paper" without saying where he stands.
- 2017, edited transcript [S27]: "我原来比较重视理论，很多问题都是写文章，证明一些东西，也小有成就" **[tr.]** "I used to put the weight on theory, writing papers and proving things, with some small success". Also: "这就是到一定年龄的时候，就追求鼓励这些年轻人，不光是有一定的学术造诣，把自己的学术成果转化成技术，对人的基本生活产生影响，这才是 OR 的本质" **[tr.]** "at a certain age, what I pursue is encouraging these young people not only to reach academic accomplishment but to turn their results into technology that affects people's basic lives; that is the essence of OR".

**Observed (students, first-hand; secondary as evidence about Ye):**

| Student (thesis year) | What they single out | Source |
|---|---|---|
| Anthony So (2007) | "I would like to express my heartfelt thanks to Professor Ye, for his guidance and constant encouragement and support, as well as the many enjoyable discussions we had over the last four years." Other faculty are credited for bringing him into other fields: Koltun and Roughgarden "got me excited about various topics in theoretical computer science"; Guibas introduced "the field of rigidity theory" | [S4] p. vii |
| Holly Jin (Toronto 2005; spent two years at Stanford) | "I would like to thank Prof. Yinyu Ye for inspiring me to the exciting field of sensor network research. I am very fortunate to be able to learn from him and his class. His work with Pratik Biswas was a vital starting point for my thesis." Her two advisors are Carter and Saunders; Saunders gets the credit for "making every sentence concise and correct" | [S5] p. iv |
| Nicole Taheri (2012) | "Yinyu Ye has been a wonderful thesis adviser. His energy and enthusiasm for his work is inspiring, and I hope to one day have a research group like his." Also: "Weekly meetings with Professor Ye's research group were consistently interesting and provided insightful feedback." Saunders is "my reference for LaTeX and proper grammar" | [S6] p. vi |
| Santiago Akle Serrano (2015) | "I thank Michael Saunders for his patience, encouragement and mentorship. Yinyu Ye for his guidance and for introducing me to this area of research." | [S7] p. v |
| Ron Estrin (2019) | Ye appears in the committee list ("This work benefited substantially from their questions and suggestions"), plus: "Yinyu also merits special mention for agreeing to be my official principal supervisor upon Michael Saunders's retirement." The day-to-day mentors named are Saunders, Friedlander and Orban | [S8] p. vi |
| Oliver Hinder (2019) | "I want to start by thanking my advisor Yinyu Ye, when we started working together we had a lot of failed projects but you were really great at helping me pick myself back up. You have been full of much positive encouragement and really taught me how to persevere." | [S10] p. v |

- [observed → inferred] Across the six acknowledgements, the words attached to Ye are **"introducing me to this area"**, **"inspiring me to the … field"**, **"guidance"**, **"encouragement"**, **"energy and enthusiasm"** and **"persevere"**.
  - None of the six credits him with line-by-line writing or technical polishing.
  - In every co-advised case where the thesis says who did what (Jin, Taheri, Akle, Estrin), that polishing is credited to Michael Saunders.
  - Reading: Ye's role is to **open a field and keep morale up**. Close technical and writing work often falls to a co-advisor or to peers.
  - This is a pattern across four or more independent writers, not one student's view.
- [observed] Stated and observed agree on **weekly meetings**. Ye's 2020 statement (weekly meetings) matches Taheri's 2012 account of a weekly group meeting that gave "insightful feedback".
- [observed] Stated and observed agree on **"open questions" before safe ones**. Ye's 2020 statement (open questions that "have been studied but not solved") matches Hinder's account of starting with "a lot of failed projects".
- [inferred] Both matches are consistent with a high-risk problem choice early in the PhD, buffered by encouragement.

### B.3 Shared supervision: how problems and advisors reach the students

- [practice] primary. **Co-advising is common, and the partners often come from outside optimization:**
  - Motwani (CS theory) for So [S4].
  - Zenios for Ding [S3].
  - Saunders (SOL, numerical linear algebra) for Akle and Estrin [S7][S8], and as a committee member for Hinder [S10].
  - Giesecke and Pelger for X. Li [S15].
  - Imbens (econometrics) for Qu [S3].
  - Udell as primary advisor for Gao [S18].
  - Ge at SUFE for Chuwen Zhang [S17].
  - The CV marks 10 of its 34 lines "Co-DA" [S2].
- [practice] primary. **Students may do much of the thesis with other faculty.**
  - Hinder's Part I (chapters 2–5) is "Joint work with Yair Carmon, John Duchi and Aaron Sidford".
  - Only Part II (chapters 6–8, interior-point methods) is joint with Ye (with Haeser in chapter 6) [S10, chapter bylines].
- [practice] primary. **Formal supervision without co-authorship.** Ye became Estrin's "official principal supervisor" when Saunders retired [S8], and DBLP has no Ye–Estrin paper [S31].
- [inferred] This is the "career is a network" statement put into practice. Students are routinely placed with a second advisor who has a complementary skill: CS theory, numerical linear algebra, econometrics, statistics. Ye supplies the problem area and the connections.

### B.4 Group habits and lab culture

- **A shared problem line spans several theses.** [practice] primary, papers verified.
  - The seed: Biswas & Ye, "Semidefinite programming for ad hoc wireless sensor network localization", IPSN 2004, DOI 10.1145/984622.984630.
  - It spawned several theses and papers: Biswas's thesis; So & Ye, *Math. Program.* 2007 (DOI 10.1007/s10107-006-0040-1); Jin's SpaseLoc (Carter, Jin, Saunders & Ye, *SIAM J. Optim.* 17(4) 2006, DOI 10.1137/040621600); Biswas, Liang, Toh, Ye & Wang, *IEEE T-ASE* 2006 (DOI 10.1109/tase.2006.877401); Zhu, So & Ye, *SIAM J. Optim.* 2010 (DOI 10.1137/090772009); Taheri's lateration-graph chapter [S6].
  - How So describes his starting point [S4 abstract, p. v]: "Recently, Biswas and Ye (2004) have proposed a semidefinite programming (SDP) based model for the problem and have reported its superb experimental performance. Our work is motivated by the desire to explain this phenomenon in a rigorous manner."
  - [inferred] Division of labour: one student shows that the method works in experiments, and the next student proves why.
- **Online LP passed down the cohorts.** [practice] primary.
  - Agrawal, Wang & Ye, "A Dynamic Near-Optimal Algorithm for Online Linear Programming", *Operations Research* 2014, DOI 10.1287/opre.2014.1289.
  - Wang's thesis on dynamic learning in revenue management [S3].
  - Taheri's online-LP charging mechanism: Taheri, Entriken & Ye, *IEEE Trans. Smart Grid* 2013, DOI 10.1109/tsg.2012.2233768.
  - Li & Ye, "Online Linear Programming: Dual Convergence, New Algorithms, and Regret Bounds", *Operations Research* 2022, DOI 10.1287/opre.2021.2164.
  - Xiaocheng Li's 2024 celebration talk "Watermarking LLMs with Online Linear Programming" [S11].
- **A negative result becomes a seed for students.** [practice] primary.
  - The group's counterexample: Chen, He, Ye & Yuan, "The direct extension of ADMM for multi-block convex minimization problems is not necessarily convergent", *Math. Program.* 155 (2016), DOI 10.1007/s10107-014-0826-5.
  - It was taken up by the postdoc Ruoyu Sun (with his PhD advisor Luo): arXiv 1503.06387, which the CV credits with a 2015 Nicholson second prize [S2].
  - In 2026 Wenzhi Gao revisits it on his blog: "periodically using a negative dual stepsize also fixes the divergence of multi-block ADMM on classical quadratic counterexamples" [S18b].
  - [inferred] The group's own counterexamples serve as standing test problems for later generations.
- **Weekly group meetings and collaboration among students.** [observed] Taheri [S6]: "I collaborated on research projects with fellow graduate students Santiago Akle, Onkar Dalal, and Davood Shamsi, who taught me about math, research, and cooperation. Weekly meetings with Professor Ye's research group were consistently interesting and provided insightful feedback. I would especially like to thank Zizhuo Wang for a number of helpful discussions." [inferred] Senior students (Wang, then a PhD student) act as informal second mentors.
- **Courses as the entry point, graded by projects.** [practice] primary, course pages 2023–24 [S23]:
  - MS&E 314: "Homework Exercises: 5 homework assignments will not be graded but discussed in Problem Sessions. Computational Project: A team and quarter-long project (up to 3 people) -- 100%". The page also says "it is essential to have a tolerance for mathematical discourse plus an ability to follow - and devise one's own - mathematical proofs" and "various algorithm implementation projects can be substituted for the final exam".
  - MS&E 310: "Midterm exam: November 3-5 take home, 50%; A project (up to two students): report due December 11 50%".
  - Jin credits "him and his class" [S5]. At SJTU in 2024 he "欢迎在场的同学参与其团队的研究" **[tr.]** "welcomed the students present to join his team's research" [S29, secondary report].
  - [inferred] Team computational projects are how students first try his problems.
- **Students read and test his books.** [practice] primary, *Interior Point Algorithms* preface, Iowa City 1996, p. xiv [S24]:
  - "I am specially indebted to Steve Benson and Andrew Prince, who made a careful and thorough reading of the manuscript and provided me numerous comments and suggestions on organizing the materials presented in this book. Special thanks also go to Erling Andersen, for giving me detailed feedback from a course he taught in Odense University using an early version of the manuscript".
  - And: "For their contribution to this effort, I acknowledge the students and other participants in the course 6K287 at the Department of Management Science."
- **Industry partners in the thesis.** [practice] primary:
  - Taheri: "The main project in this thesis was initiated and explored in collaboration with Robert Entriken at the Electric Power Research Institute (EPRI) … EPRI funded three years of this research" [S6]. The CV lists "Recipient of the 2010 and 2011 EPRI … Gift" [S2].
  - Jin thanks "Robert Bosch Corporation's support of my research at Stanford University" [S5].
  - The CV records business-plan wins: "2004 BASES Innovators' Challenge First-Place Winners: Pratik Biswas and Yinyu Ye on sensor network localization" and a 2005 win with Jin, Carter and Saunders. It also lists a patent, "A Semi-Definite Programming Method for AD HOC Network Node Localization, 2005", and an industry project "Polaris Wireless Inc (2006-2007), Mobile Phone Localization" [S2].
- **The alumni network is visible as a community.** [practice] primary, 2024 retirement celebration programme [S11]:
  - The talks were "from Professor Ye's students and collaborators". Sessions were chaired by former students (Ding, Hinder, Z. Wang).
  - The event was "supported financially by donations from Cardinal Operations, MOSEK, the Stanford Department of Management Science and Engineering (MS&E), the Stanford MS&E Operations Research Group, Yichuan Ding, Jiawei Zhang, and Zeyu Zheng".
  - Z. Wang's talk abstract: "I would share some of my experiences and stories learning and working with Prof. Yinyu Ye, who have greatly guided my professional career." (Only the abstract exists; see Gaps.)
  - So: "my journey in tackling this problem, which began with my PhD work under Professor Ye's supervision".

### B.5 Students who became solver builders (the MOSEK → DSDP → COPT pipeline)

- **Iowa era.** [practice] primary.
  - Andersen (visiting PhD, 1996) is listed as "Founder of MOSEK.com, Optimization Software" [S2]. Ye is "Chairman of the technical advisory board of MOSEK (2009-)" [S2].
  - Andersen & Ye, "Combining Interior-Point and Pivoting Algorithms for Linear Programming", *Management Science* 42(12) 1996, DOI 10.1287/mnsc.42.12.1719. His 2024 talk revisits it: "we will review the joint work by Yinyu Ye and the speaker on basis identification" [S11].
  - Benson (Iowa 1999) wrote DSDP: Benson, Ye & Zhang, *SIAM J. Optim.* 2000, DOI 10.1137/s1052623497328008; Benson & Ye, "Algorithm 875: DSDP5", *ACM TOMS* 2008, DOI 10.1145/1356052.1356057.
- **Stanford and Shanghai era.** [stated], 2017 and 2025:
  - 2017 [S27]: "王曦也是我们斯坦福的学生，现在是杉数的产品经理" **[tr.]** "Wang Xi is also one of our Stanford students, now a product manager at Cardinal Operations". Also: "杉数这些年轻人都是从斯坦福回来的学生" **[tr.]** "the young people at Cardinal Operations are all students who came back from Stanford".
  - 2025 [S26]: "一些企业找到了我和我的学生们，希望我们能够迎着前所未有的困难"顶上去"，开发出中国自己的求解器。我们也的确做到了。" **[tr.]** "Some companies came to me and my students hoping we would 'step up' against unprecedented difficulty and develop China's own solver. We did." Also: "我们要做就要做到最好，要做到未来全世界都用我们的产品。" **[tr.]** "If we do it, we do it best, so that in future the whole world uses our product."
- [observed] Ge's 2024 talk abstract [S11]: "the development of the COPT mathematical optimization software under the leadership of Professor Yinyu Ye. We will explore its journey from inception to becoming the second best software globally in its field. Additionally, I will share recent advancements in leveraging GPU architectures to accelerate mathematical optimization, a new progress made under his guidance."
- [observed] Chuwen Zhang [S17]: "I worked as an Operations Research Engineer at [Cardinal Operations] during 2018-2025, building optimization solvers and operations research solutions". In the same years he did his PhD, co-advised by Ye and Ge.
- [practice] primary, DRSOM.jl repository [S25]:
  - The repository sits under the student's own GitHub account (bzhangcw). The README lists "Developer: Chuwen Zhang … Yinyu Ye".
  - The git history is almost entirely one student's: 78 + 28 + 26 commits under "C. Zhang", "cz" and "C Zhang", plus 11 under "brentian" (the documentation host is bzhangcw.io, apparently the same person). There is one commit by "COPT-Public".
  - The README thanks "the COPT team". Co-authors listed there include Ge, Bo Jiang, Yuntian Jiang and Chang He.
- [practice] primary. Paper: Ge, Huangfu, Wang, Wu & Ye, "Cardinal Optimizer (COPT) User Guide", arXiv 2208.14314. Two of the five authors (Ge, Wang) are his former PhD students.
- [inferred] This pattern recurs over 30 years. A student takes an algorithm Ye analysed (homogeneous self-dual IPM, dual-scaling SDP, and later PDHG and second-order methods) and turns it into production software. Ye then stays on as adviser to the resulting company or project. For a solver team this is the most transferable part of his supervision: a **complexity-theory advisor paired with a student-engineer who owns the code**.

---

## C. Layers 4–6 as his students practised them (execution, judgement, reporting)

- **Benchmark against the incumbent solver and report where you lose.** [practice] primary, Hinder thesis [S10].
  - Abstract: "Comparisons with IPOPT on a subset of CUTEst problems indicate less frequent failures and superior performance for detecting infeasibility."
  - Chapter 8 conclusion (p. 230) admits a weakness: "We find that manually tuning the value of µ0 for a specific problem often significantly reduces the number of iterations. This sensitivity to the initialization, especially compared with the homogenous self-dual, is a known issue for Lustig's IPM for linear programming".
  - The same page proposes a next step: "Potentially switching to an LBL factorization … might help resolve this issue."
- **Use LP interior-point design as the template for nonlinear programming.** [practice] primary [S10, abstract]: "we reduce primal feasibility at the same rate as the barrier parameter. This gives an algorithm with more robust convergence properties and closely resembles successful algorithms from linear programming." [inferred] The homogeneous self-dual method is the group's reference point for robustness. Here it is invoked both as the model and as the standard the new method falls short of (initialisation).
- **Cross-lab code and review.** [practice] primary [S10]:
  - Hinder thanks "the many developers of Julia and related packages that made my 'One-Phase IPM' possible: Dominque Orban, Iain Dunning, Miles Lubin".
  - The chapter 8 paper acknowledges "Michael Saunders and Ron Estrin for useful conversations and feedback on the paper".
  - [inferred] Implementation help came from the Saunders/SOL circle and the Julia community, not from inside a Ye software group.
- **Explain an empirical success rigorously.** [practice] primary: So's thesis programme, quoted in B.4 [S4].

---

## D. Failures, abandoned directions, trimmed or unpublished papers

- **Early failed projects are part of the story students tell.** [observed] Hinder: "when we started working together we had a lot of failed projects" [S10, p. v].
- **The Max-Bisection bound he could not improve**, told by Ye in public. [stated] primary, 2009 prize speech [S21]:
  - "One time I worked on an approximation algorithm for the Max-Bisection problem, and had a provable approximation rate of 0.699. … I tried very hard but could not prove it. Later, somebody did use a stronger SDP relaxation to make the bound 0.701, which still stands as the best today."
  - The papers are Ye, "A .699-approximation algorithm for Max-Bisection", *Math. Program.* 2001, DOI 10.1007/pl00011415, and very likely Halperin & Zwick, *Random Structures & Algorithms* 2002, DOI 10.1002/rsa.10035. The speech names no one; the identification is mine and the text was not read.
  - [inferred] He tells students about his own dead ends. This matches "Take a loss" on his 2023 sport slide [S22].
- **A paper trimmed at referees' request, with a long gap between arXiv and journal.** [practice] primary.
  - Hinder & Ye, "Worst-case iteration bounds for log barrier methods on problems with nonconvex constraints": arXiv 1807.00404 (v1 July 2018, v5 3 Nov 2023), published in *Math. Oper. Res.* 49 (2024) 2402–2424, DOI 10.1287/moor.2020.0274.
  - The arXiv comment: "several results were removed from the previous version most notably the results on convex case. These results were removed due to reviewer suggestions to focus the paper on the most significant contributions. These results still appear in the first author's PhD thesis".
  - [inferred] The PhD thesis serves as the archive of results cut from papers.
- **A student solver paper with no journal version found.** [practice]: Hinder & Ye, "A one-phase interior point method for nonconvex optimization", arXiv 1801.03072. The last arXiv version is v2 of 11 Jan 2018, with the comment "fixed typo in sign of dual multiplier in KKT system". Ye's DBLP record (330 entries) has no entry for it. Its status beyond arXiv was **not verified**; do not read it as "rejected".
- **Students who stopped publishing with him at graduation** (Biswas, Taheri, Ding, Post, Kaliski; A.2). This is not a failure as such, but it is the usual outcome for the students outside the core few.

---

## E. Era and resource context

| Period | Group size and setting | Resources and tools | Evidence |
|---|---|---|---|
| 1988–2002, Iowa | Small department (Management Sciences). 5 PhD graduates 1992–1999 (2 co-advised) plus one visiting student (Andersen). Students read the monograph drafts; a course (6K287) served as test audience | NSF grants listed in the preface. Codes in C and Fortran (COPL series). Software distributed from the book's web page | [S2][S24] |
| 2002–2024, Stanford | 28 CV lines for Stanford advisees (2004–2024) in MS&E and ICME, 8 of them marked Co-DA; 3 postdocs. Weekly group meeting. Cross-department co-advisors. Industry-funded theses (EPRI, Bosch). Business-plan competitions and patents | MATLAB codes on SeDuMi and DSDP for sensor-network localization. Julia for Hinder's IPM (2018–19). Taheri notes the ICME computing community | [S2][S5][S6][S10] |
| 2017–2026, Stanford plus Shanghai | Solver company (Cardinal Operations, COPT released 2019 per 01-publications) plus university groups (SUFE/SJTU, ICME). Students work as solver engineers while doing the PhD (Chuwen Zhang, 2018–2025). Teams of 5–7 authors | Julia (DRSOM.jl), GPU work "under his guidance" (Ge abstract). Also, in the wider circle, AI-assisted proofs with Lean: Wenzhi Gao's 2026 blog lists results "developed with AI assistance with accompanying Lean projects" [S18b]. This is context about the student, not evidence about Ye | [S11][S17][S18b][S25] |

---

## F. Tacit knowledge: what his students knew that the papers do not say

Each item names who says it and where. All are secondary as evidence about Ye.

1. **Expect early failure; the advisor's job is morale, not rescue.** According to Hinder, 2019 thesis acknowledgements [S10]: many failed projects at the start, with Ye "really great at helping me pick myself back up". This matches Ye's own "Take a loss" [S22]. Confidence: medium (one student explicitly, plus a stated principle).
2. **Ye opens the field; others help you finish the text.** According to Akle [S7], Jin [S5], Taheri [S6] and Estrin [S8], Ye is credited with introducing or inspiring the area and with guidance and enthusiasm. Saunders is credited with writing, grammar and LaTeX. Confidence: medium-high (four independent writers, same split). A student of Ye's should look for writing and numerical-linear-algebra mentoring elsewhere, and in practice they did.
3. **The weekly group meeting is where feedback happens, and peers teach each other.** According to Taheri [S6]; Ye states the same [S20]. Confidence: medium.
4. **Pick up the group's standing problems and counterexamples.** This is inferred from the SNL, online-LP and multi-block-ADMM lineages (B.4). No student says it in words. Confidence: medium, [inferred].
5. **If your method works in experiments, someone (maybe you) should prove why; if it has a proof, someone should build it.** Inferred from So's thesis statement [S4], the Biswas → So sequence, and the student-built solver line (B.5). Confidence: medium.
6. **Your thesis may have a second home.** Co-advisors in CS, statistics or econometrics, and whole thesis parts done with other faculty, are normal (Hinder Part I, So with Motwani, Qu with Imbens). According to the signature pages and bylines [S3][S4][S10]. Confidence: high as practice.
7. **Industry partners and companies are part of the group, not outside it.** EPRI and Bosch funded thesis projects [S5][S6]. The company Cardinal Operations employs students during the PhD [S17]. Two of his students' companies sponsor his celebration [S11]. Confidence: high as practice.
8. **Alumni come back.** Hinder co-authors with the next cohort (Qu, Gao) [S31]. Ge and Wang co-lead COPT [S12][S11]. Former students chair his celebration sessions [S11]. Confidence: high as practice.

Not recoverable from public material: how the weekly meeting is run (format, who presents, how problems are assigned), how he gives feedback on drafts, how he decides when a student should drop a problem, and how he handles authorship order. The last one changed around 2015, from alphabetical to student-first; see 01-publications. No source explains why.

---

## G. Contradictions (kept, not reconciled)

1. **Who was Ye's doctoral advisor.**
   - CV: "Edison Tse (Advisor)", with Dantzig on the committee [S2].
   - MGP: Advisor 1 Tse, Advisor 2 Dantzig [S3].
   - So's thesis (2007): "Back then I did not know that Professor Dantzig was Professor Ye's doctoral advisor" [S4].
   - Ye himself: Dantzig "was a great advisor" (2009) [S21]; "My first mentor was George Dantzig … George was a great advisor" (2020) [S20].
   - (Same contradiction as 01-publications C1, here in a student's version.)
2. **Advisee counts and dates.**
   - CV: 34 lines, 10 marked Co-DA. MGP: 16 students.
   - Dates differ: Benson 1998 (MGP) vs 1999 (CV); Bosch 1993 vs 1994; Hung 1994 vs "Pi-Fang Huang 1995"; Ding 2012 vs 2013; Akle 2015 (MGP, thesis) vs "Tiago Akle 2014*" (CV).
   - Zhaonan Qu is an advisee in MGP but absent from the CV.
3. **Role labels.**
   - The CV marks Estrin "Co-DA", but his signature page reads "Yinyu Ye, Primary Adviser" [S8]. His acknowledgements explain that this was formal, after Saunders's retirement.
   - The CV lists So without Co-DA, but So's signature page names Ye and Motwani as "Principal Co-Advisor" [S4].
   - The CV lists X. Li without Co-DA, but Li names three advisors [S15].
4. **Postdoc dates.** Ruoyu Sun was a postdoc in "2015-2016" per his homepage [S19] and in "2017" per the CV [S2].
5. **Where COPT was built.**
   - NJU report (secondary, 2024): "他的团队在斯坦福自主研发的COPT求解器" **[tr.]** "the COPT solver his team developed independently at Stanford". It adds that "团队成员联合创立的杉数科技" **[tr.]** "team members co-founded Cardinal Operations" [S30].
   - Ge's abstract describes COPT's development "under the leadership of Professor Yinyu Ye" [S11]. Chuwen Zhang places the solver work at Cardinal Operations [S17]. Ye (2017) speaks of students who "came back from Stanford" to the company [S27].
   - Whether COPT was built "at Stanford" or at the company in China by Stanford alumni is not settled by these sources.
6. **Theory versus practice as the thing he teaches.**
   - 2017: he says he "used to" emphasise theory and now encourages students to turn results into technology [S27].
   - 2020: what he prizes in students is conquering "a scientific mystery" in open questions [S20].
   - 2023: "Theory vs Practice" appears on a slide as a pair with no preference marked [S22].

---

## H. Gaps (not found or not read)

- **Thesis acknowledgements not read**: Biswas, Ge, Delage, Z. Wang, Agrawal, Carlsson, Post, X. Li, C. Sun, Qu, Benson, Andersen, Kaliski, Chuwen Zhang (SUFE).
  - Stanford SearchWorks returned a bot-detection page to both curl and WebFetch.
  - OpenAlex search was paused ("Anonymous search is paused") and Semantic Scholar returned HTTP 429.
  - Stanford purl identifiers for these theses are unknown.
  - Only the theses hosted by SOL, CUHK or Hinder's homepage were read.
- **The 2024 celebration talks**: Z. Wang's "Learning and Working with Prof. Yinyu Ye", Ge's "The Development History of COPT" and Todd's "Yinyu Ye's Research on Interior-point Methods" exist only as abstracts. I found no slides, video or transcript. No transcript was saved to `sources/talks/`.
- **No lab guide, group page, onboarding document or student blog post** about working with him. Guessed URLs on his site (students.html, group.html, people.html) return 404.
- **No Festschrift volume** was found, only the 2024 event programme. No memoir (he is living).
- **Chinese-language interviews with Ge or Z. Wang about Ye** were not found within the budget of 2 WebSearch calls. Cardinal Operations' website renders by JavaScript and had no readable founder story.
- **Unreachable pages**: Erick Delage's HEC page (connection reset; WebFetch 503) and MOSEK's history pages (JavaScript-only).
- **Supervision details**: no source describes meeting format, how problems are assigned, how drafts are reviewed, how authorship is decided, or how rejections are handled with students. The only visible case is the reviewer-driven trimming of Hinder & Ye (D).
- **Iowa-era supervision**: nothing from those students beyond the preface acknowledgements.
- Wenzhi Gao's `people.html` and `bio.html` returned 404.

---

## I. What this means for the skill (inferred; to be tested against 02, 03 and 05)

- **Asked "how would Ye staff a solver-improvement project?"**, the skill should answer with the recorded pattern. Pair a complexity or algorithm question he cares about with a student-engineer who owns the code (Andersen → MOSEK, Benson → DSDP, Chuwen Zhang → DRSOM.jl, Ge and Wang → COPT). Put numerical linear algebra and writing with a co-advisor or peer (the Saunders pattern). Benchmark against the incumbent solver (IPOPT on CUTEst for nonlinear programming), and report the losses as well (the µ0 sensitivity).
- **Asked "what should a student work on?"**: an open problem that has been "studied but not solved" [S20]. Prefer one of the group's standing lines (SDP relaxation, online LP, homogeneous IPMs, counterexamples such as multi-block ADMM), and expect early failures [S10].
- **Evidence strength for the skill**: supervision style rests on six theses plus Ye's statements (medium). The solver pipeline rests on the CV, DBLP, code and abstracts (high as practice). The inner workings of the group are unknown.

---

## Sources

- S1: Yinyu Ye, homepage, https://web.stanford.edu/~yyye/ (accessed 2026-09-28). Primary.
- S2: Yinyu Ye, CV "Updated October, 2025", https://web.stanford.edu/~yyye/cvYYYE25.pdf (sections 1, 4, 6, 7). Primary.
- S3: Mathematics Genealogy Project, Yinyu Ye (id 12397), https://www.mathgenealogy.org/id.php?id=12397, and student pages (ids 130392, 140097, 144618, 147090, 176746, 193474, 219337, 239186, 254196, 333555, 344374, 35496, 60617, 60628, 60629, 60630). Secondary (community-submitted database).
- S4: Anthony Man-Cho So, "A Semidefinite Programming Approach to the Graph Realization Problem: Theory, Applications and Extensions", PhD thesis, Stanford, 2007, https://www1.se.cuhk.edu.hk/~manchoso/papers/thesis.pdf (signature page, abstract, acknowledgements pp. vii–viii). Primary for So; secondary about Ye.
- S5: Holly Hui Jin, "Scalable Sensor Localization Algorithms for Wireless Sensor Networks", PhD thesis, University of Toronto, 2005, https://web.stanford.edu/group/SOL/dissertations/holly-thesis.pdf (abstract, acknowledgements p. iv). Secondary about Ye.
- S6: Nicole Anahita Taheri, "Linear Optimization Methods for Vehicle Energy and Communication Networks", PhD thesis, Stanford ICME, June 2012, https://web.stanford.edu/group/SOL/dissertations/onlinecopy-ntaheri_thesis.pdf (acknowledgements p. vi). Secondary about Ye.
- S7: Santiago Akle Serrano, "Algorithms for Unsymmetric Cone Optimization and an Implementation for Problems with the Exponential Cone", PhD thesis, Stanford ICME, 2015, http://purl.stanford.edu/sn367tt9726 (read via https://web.stanford.edu/group/SOL/dissertations/ThesisAkleAdobe-augmented.pdf; signature page, acknowledgements p. v). Secondary about Ye.
- S8: Ron Estrin, "The Merits of Keeping it Smooth: Iterative Linear Solvers and a Smooth Exact Penalty Function for Constrained Nonlinear Optimization", PhD thesis, Stanford ICME, 2019, http://purl.stanford.edu/dh100nj5076 (read via https://web.stanford.edu/group/SOL/dissertations/thesis-ron-estrin.pdf; signature page, acknowledgements p. vi). Secondary about Ye.
- S9: Ding Ma, "Essays in Marketing, Economics, and Optimization", PhD thesis, Stanford MS&E, 2018, http://purl.stanford.edu/xp256qm9828 (advisers Hartmann and Saunders; Ye is thanked only among MS&E faculty). Secondary; used only as a negative check.
- S10: Oliver Hinder, "Principled Algorithms for Finding Local Minima", PhD thesis, Stanford MS&E, 2019, https://stacks.stanford.edu/file/druid:tn227rh8389/final-thesis-removed-intermediate-augmented.pdf (signature page, abstract, acknowledgements p. v, chapter bylines, ch. 8 conclusion p. 230). Secondary about Ye; primary for the joint chapters.
- S11: "Yinyu Ye Retirement Celebration, July 28-29, 2024, Stanford" (programme and abstracts), https://quyanlin.github.io/ye/event.html. Secondary (organisers' page; abstracts written by the speakers).
- S12: D. Ge, Q. Huangfu, Z. Wang, J. Wu, Y. Ye, "Cardinal Optimizer (COPT) User Guide", arXiv 2208.14314 (2022). Primary (co-authored).
- S13: Stanford Systems Optimization Laboratory, "Publications: dissertations", https://web.stanford.edu/group/SOL/publications_dissertations.html. Primary (lab page; used to locate S5–S9).
- S14: Oliver Hinder, homepage https://www.oliverhinder.com/ and papers page https://www.oliverhinder.com/papers-and-talks. Secondary about Ye.
- S15: Xiaocheng Li, homepage, https://xiaocheng-li.github.io/. Secondary.
- S16: Chunlin Sun, homepage, https://chunlinsun.github.io/ (© 2024). Secondary.
- S17: Chuwen Zhang, homepage, https://bzhangcw.io/. Secondary.
- S18: Wenzhi Gao, homepage https://web.stanford.edu/~gwz/index.html and ICME profile https://icme.stanford.edu/people/wenzhi-gao. S18b: blog, https://web.stanford.edu/~gwz/blog.html (posts dated 2026-03-02 to 2026-09-09). Secondary.
- S19: Ruoyu Sun, homepage, https://ruoyus.github.io/. Secondary.
- S20: Stanford Engineering, "Yinyu Ye: Sports led me from the rice fields to Stanford" (first-person essay, by Edmund L. Andrews), 2020-12-08, https://engineering.stanford.edu/news/yinyu-ye-sports-led-me-rice-fields-stanford. Primary (first person, institution-edited).
- S21: Yinyu Ye, "Yinyu Ye's speech after winning the John von Neumann Theory Prize (10/11/2009)", https://web.stanford.edu/~yyye/Yinyu-accept-speech.pdf. Primary.
- S22: Yinyu Ye, "My Academic, Sport, and Life as a Whole" (slides, 2023), https://web.stanford.edu/~yyye/MyacademicSportlife.pdf (slides 5, 12, 15). Primary.
- S23: Ye's course pages, 2023–24: MS&E 310 https://web.stanford.edu/class/msande310/, MS&E 314 https://web.stanford.edu/class/msande314/, MS&E 111/211 https://web.stanford.edu/class/msande211x/. Primary.
- S24: Yinyu Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley, 1997, DOI 10.1002/9781118032701. Preface pp. xiii–xiv ("Iowa City, 1996"), read from the front-matter PostScript https://web.stanford.edu/~yyye/main.ps. Primary.
- S25: DRSOM.jl repository (README, git log), https://github.com/bzhangcw/DRSOM.jl (hosted under the student's own GitHub account), docs https://drsom.bzhangcw.io/. Primary (practice).
- S26: 中新社 (王宗汉, 裴心语), "东西问丨叶荫宇：AI与OR，共促人类未来", 2025-03-06, https://www.chinanews.com/gn/2025/03-06/10378972.shtml. Primary (edited interview).
- S27: 雷峰网 (王金许), "运筹学教授叶荫宇：作为 AI 基石，优化算法如何在实际中应用？", 2017-06-27, https://www.leiphone.com/category/industrynews/DwILBnyYJPMfv7WX.html. Primary (edited talk transcript).
- S28: 香港中文大学（深圳）数据科学学院, "活动回顾 | 叶荫宇教授做客港中大（深圳）大师讲堂", 2023-04-06, https://sds.cuhk.edu.cn/event/942 (Zizhuo Wang as host). Secondary.
- S29: 上海交通大学研究生院, "斯坦福大学李国鼎讲席教授叶荫宇做客第218期大师讲坛", 2024-04-28, https://www.gs.sjtu.edu.cn/post/detail/Z3MyMDMz. Secondary.
- S30: 南京大学工程管理学院, "《我的学术、体育以及人生发展》——叶荫宇教授赴仙林校区与我院本科生开展交流", 2024-04-18, https://sme.nju.edu.cn/5f/15/c2039a679701/pagem.htm. Secondary.
- S31: DBLP, Yinyu Ye (pid 42/1372-1), 330 records fetched 2026-09-28 via https://sparql.dblp.org/sparql; person page https://dblp.org/pid/42/1372-1. Primary (bibliographic).
- S32: arXiv abstract pages: 1801.03072 (Hinder & Ye), 1807.00404 (Hinder & Ye), 1503.06387 (Sun, Luo & Ye), 2208.14314 (COPT), 2208.00208 (DRSOM). Primary (bibliographic).
- S33: Stanford MS&E, faculty page https://msande.stanford.edu/people/yinyu-ye, checked for student or retirement items; none found. Secondary.
- S34: Anthony Man-Cho So, homepage, https://www1.se.cuhk.edu.hk/~manchoso/ (used to locate S4). Secondary.

**Papers named above.** Each identifier was checked by tool in this run, through Crossref DOI lookup, the arXiv abstract page or the DBLP record:
- Biswas & Ye, IPSN 2004, 10.1145/984622.984630
- So & Ye, *Math. Program.* 2007, 10.1007/s10107-006-0040-1
- Carter, Jin, Saunders & Ye, *SIAM J. Optim.* 2006, 10.1137/040621600
- Biswas, Liang, Toh, Ye & Wang, *IEEE T-ASE* 2006, 10.1109/tase.2006.877401
- Zhu, So & Ye, *SIAM J. Optim.* 2010, 10.1137/090772009
- Taheri, Entriken & Ye, *IEEE Trans. Smart Grid* 2013, 10.1109/tsg.2012.2233768
- Agrawal, Wang & Ye, *Oper. Res.* 2014, 10.1287/opre.2014.1289
- Li & Ye, *Oper. Res.* 2022, 10.1287/opre.2021.2164
- Post & Ye, *Math. Oper. Res.* 2015, 10.1287/moor.2014.0699 (CV: 2013 Nicholson second prize)
- Delage & Ye, *Oper. Res.* 2010, 10.1287/opre.1090.0741 (CV: 2008 Nicholson first prize)
- Chen, He, Ye & Yuan, *Math. Program.* 155 (2016), 10.1007/s10107-014-0826-5
- Sun, Luo & Ye, arXiv 1503.06387
- Haeser, Hinder & Ye, *Math. Program.* 186 (2021), 10.1007/s10107-019-01454-4 (Hinder thesis ch. 6)
- Hinder & Ye, *Math. Oper. Res.* 49 (2024), 10.1287/moor.2020.0274, arXiv 1807.00404
- Hinder & Ye, arXiv 1801.03072
- Qu, Gao, Hinder, Ye & Zhou, *Oper. Res.* 73(3) 2025, 10.1287/opre.2022.0592
- Andersen & Ye, *Management Sci.* 1996, 10.1287/mnsc.42.12.1719
- Benson, Ye & Zhang, *SIAM J. Optim.* 2000, 10.1137/s1052623497328008
- Benson & Ye, *ACM TOMS* 2008, 10.1145/1356052.1356057
- Ye, *Math. Program.* 2001, 10.1007/pl00011415
- Halperin & Zwick, *Random Structures & Algorithms* 2002, 10.1002/rsa.10035 (identification only; not read)
- Ye & Zhang, "New Results on Quadratic Minimization", *SIAM J. Optim.* 2003, 10.1137/s105262340139001x (the subject of Anstreicher's 2024 talk)
- Vavasis & Ye, *Math. Program.* 1996, 10.1007/BF02592148 (the subject of Tsuchiya's 2024 talk, which calls it "so elegant and fascinating" and describes years of work "to make it simple and scaling invariant")
- Zhang, He, Jiang, Xue, Jiang, Ge & Ye, *Math. Oper. Res.* 2026, 10.1287/moor.2023.0132
- Zhang, Ge, He, Jiang, Jiang & Ye, arXiv 2208.00208
- Ge, Huangfu, Wang, Wu & Ye, arXiv 2208.14314
- Ye, *Interior Point Algorithms*, 1997, 10.1002/9781118032701
