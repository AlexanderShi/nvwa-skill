# Yinyu Ye: Research Trajectory

| Field | Value |
|---|---|
| Researcher | Yinyu Ye (叶荫宇). K. T. Li Professor of Engineering (Emeritus), Stanford MS&E and ICME. Since 2024 he has held posts in China and Hong Kong (SJTU, SIMIS, CUHK-Shenzhen, HKUST). The exact titles differ between sources; see Contradictions C6 |
| Dimension | Research agent 06 of 06, research trajectory (nuwa research-craft, Phase 1) |
| Research date | 2026-09-28 |
| Sources consulted | 31 documents and pages (list at the end: 22 primary, 8 secondary, 1 that failed with HTTP 403). Also about 70 Crossref DOI records and 42 arXiv abstract pages, each checked in this run, plus one DBLP SPARQL export (327 records) |
| WebSearch calls | 1 of 2 allowed |
| User-supplied material | None. `references/sources/{papers,talks,essays,software}/` held only `.gitkeep`. `private/` was not opened |
| Transcripts saved | None. No talk had a transcript or subtitles I could download. The slide decks are copyrighted and stay in scratch (`/tmp/nonlinear-team-scratch/base-skills/yinyu-ye/06/`) |

**Tags.** [stated]: Ye said or wrote it about himself (CV, homepage, speeches, interviews, his own slides). [practice]: what the dated record shows he did (papers, arXiv histories, software, grants). [observed]: what third parties reported (journalists, prize and event pages, genealogy databases, other authors). [inferred]: my reading, with the basis given. (P) marks a primary source and (S) a secondary one. [Tn] numbers point to the Sources list.

**Reading depth.** I read the following in full: the CV (23 pp., "Updated October, 2025") [T2]; the homepage, the talks page and the papers page [T1, T4, T5]; the 2009 prize speech in English and Chinese [T7]; the 2020 first-person essay [T9]; the 2017 talk transcript [T12]; the 2025 interview [T13]; the 2026 note [T22]; and the Preface of the 1997 monograph [T10]. I read the text layers of eight slide decks (2021–2026). Of the other papers I read only abstracts and bibliographic records. **I read no proofs and no full paper texts for this dimension.**

**Quotations.** Where a PDF or PostScript text layer had lost the spaces between words, I restored the spacing and changed nothing else. Chinese quotations are given in the original, followed by my translation marked *tr.* and set without quotation marks.

---

## 0. The trajectory in brief

- [inferred] The core stays fixed for 40 years: LP, interior-point methods, and complexity arguments that use duality and potential functions. The applications around it change about once every five to eight years: QP and LCP (late 1980s), SDP relaxation (late 1990s), sensor localization (2004), market equilibrium and MDPs (2005), DRO and online LP (2009), sparse and nonconvex problems (2010), ADMM (2014), GPU first-order solvers (2023), LLM serving and LLM-for-OR (2024–26). Each new application is recast as an LP, a conic problem or a complementarity problem, so the core toolkit can be applied to it. Basis: the timeline in §3. The homepage's own grouping of "Selected-Work" puts every line under LP, algorithm analysis, OR models, complexity or GPU solvers [T1].
- [inferred] He rarely leaves a line for good. He comes back to old lines with new tools: the trust-region QP of 1989 returns as DRSOM/HSODM in 2022; the IPM market equilibrium of 2008 returns as "second-order tâtonnement" in 2025; the MDP strong polynomiality of 2011 returns for games in 2026; sensor localization comes back as a test application in 2024. §5 gives the evidence.
- [stated] He describes one explicit turn in his own words, from proving theorems to turning results into technology: "我原来比较重视理论……但是人到年纪大的时候……我觉得最大的利益还是对一般人生活产生一些影响" *tr. I used to value theory more … but as one gets older … I feel the greatest benefit is still to have some effect on ordinary people's lives* (2017) [T12]. In the dated record the solver-building phase (LEAVES 2017, COPT 2019, GPU solvers from 2023) follows this statement [T21].
- [practice] His output in his emeritus years is the highest of his career: DBLP has 19 records for 2024, 26 for 2025 and 25 for 2026 up to 28 September. Before 2020 the maximum was 14 (2008) [T29].

---

## 1. Academic timeline

| Date | Event | Tag, source |
|---|---|---|
| 1948 | Born in Wuhan | [observed] (S) Wikipedia [T24]. This agrees with the essay's "In 1970, when I was 22" [T9] |
| 1966–1977 | The Cultural Revolution closes the universities. In 1968 his family is sent to a farming village, and from 1970 he works for seven years at a chemical company, hired as a basketball player. "I studied math during the night shift" | [stated] (P) [T9] |
| 1977/78–1982 | University entrance exam 1977 [T9]; enrols in 1978 [T8, slide 2]; B.S. Systems and Control, Huazhong University of Science and Technology, 1982 [T2] | [stated] (P) |
| 1982 | Arrives at Stanford (Engineering-Economic Systems). M.S. 1983 | [stated] (P) [T2][T9] |
| 1982–83 | A near-turn to AI. In the 2017 version he "差点就去搞 AI" *tr. almost went into AI* (expert systems, Lisp) [T12]. In the 2025 version his advisor had students build a Chinese-medicine expert system [T13]. See §4.1 | [stated] (P) |
| 1983–86 | Research assistant, EES. Before 1984 he did "one research project with Prof. David Luenberger" [T10] | [stated] (P) [T2][T10] |
| 1984 | Karmarkar's seminar at Stanford; he decides to do his PhD in mathematical programming | [stated] (P) [T10][T9] |
| 1986–87 | Lecturer, Mathematical Programming and Systems Optimization, EES | [stated] (P) [T2] |
| 1987 | "Visiting Ph.D. Student of Michael Todd", Cornell | [stated] (P) [T2]. The 2020 essay calls this "postdoctoral work"; see C2 |
| 11/1987–08/1988 | Research Scientist, "Optimization Software Development", Integrated Systems Inc., Santa Clara | [stated] (P) [T2] |
| 1988 | PhD, Stanford. Thesis "Interior Algorithms for Linear, Quadratic and Linearly Constrained Convex Programming". Committee: "Sam Chiu, George Dantzig, David Luenberger, Edison Tse (Advisor)" | [stated] (P) [T2]. Advisor attribution is contested; see C1 |
| 09/1988–04/2002 | University of Iowa, Management Sciences. Assistant professor 1988–90, associate 1990–93, professor 1993–98, Henry B. Tippie Research Professor 1998–2002 | [stated] (P) [T2] |
| 1991–2001 | Visiting posts: Rice (1991), Cornell (08–12/1993), NWO Fellowship at Delft (1994–97), Japan ISM (1996), UNSW (1997), MSRI Berkeley (1998), CUHK (2000–01). Adjunct at CAS, Fudan and HUST from 1993 | [stated] (P) [T2] |
| 1991–1993 | Industry: MCI (1991–92, network restoration); AT&T (1992–93), "Linear Programming Solver Development" | [stated] (P) [T2] |
| 11/1/1991 | The Lu Gang shooting at Iowa. He lists it in his academic-life slides as "Another Life Change: We have a faith -- love and kind" | [stated] (P) [T8, slides 10–11]. Recorded because he puts it in his own career narrative. I make no inference about research from it |
| 1997 | *Interior Point Algorithms: Theory and Analysis*, Wiley (DOI 10.1002/9781118032701). Preface signed "Iowa City, 1996" | [practice] (P) [T10][T30] |
| 04/2002 | Moves to Stanford as K. T. Li Chair Professor, MS&E, with a courtesy appointment in EE | [stated] (P) [T2]. On who brought him back, see §4.4 |
| 2006 | INFORMS Optimization Society Farkas Prize (inaugural); INFORMS Fellow; visiting chair at Tsinghua | [stated] (P) [T2][T3] |
| 2008 | *Linear and Nonlinear Programming*, 3rd ed., with Luenberger (DOI 10.1007/978-0-387-74503-9) | [practice] (P) [T30] |
| 2009 | INFORMS John von Neumann Theory Prize, shared with Yurii Nesterov; chair of MOSEK's technical advisory board (2009–) | [stated] (P) [T2][T7] |
| 2012 | ISMP Tseng Lectureship (inaugural), Berlin | [stated] (P) [T2] |
| 2014 | SIAM Optimization Prize, for the MDP simplex and policy-iteration work | [stated] (P) [T2]; [observed] (S) [T11] |
| 2015 | IEEE SPS Signal Processing Magazine Best Paper Award (Luo, Ma, So, Ye, Zhang 2010, DOI 10.1109/msp.2010.936019) | [stated] (P) [T2] |
| 2017 | Chief scientific adviser of Cardinal Operations (杉数科技) [T12]. "2017 Our team released the open-source solver LEAVES" [T21, slide 4] | [observed]/[stated] |
| 2019 | "2019 Our team released the professional solver COPT; subsequently, Alibaba and Huawei established their own solver teams" | [stated] (P) [T21, slide 4] |
| 2021 | *Linear and Nonlinear Programming*, 5th ed. (DOI 10.1007/978-3-030-85450-8) | [practice] (P) [T30] |
| 10/2022 | CUHK-Shenzhen, School of Data Science, Distinguished Visiting Professor (fractional) | [stated] (P) [T2] |
| 04/2024 | SJTU Antai School of Management, Distinguished Professor | [stated] (P) [T2]. Other sources give different titles; see C6 |
| 07/28–29/2024 | "Yinyu Ye Retirement Celebration" at Stanford: talks by students and collaborators, including Todd, Andersen, Anstreicher, Ge, So, Z. Wang and J. Zhang | [observed] (S) [T25] |
| 08/2024 | End of the K. T. Li chair ("2002.4-2024.8"); now "Emeritus" | [stated] (P) [T2][T1] |
| 10/2024, 11/2024 | SIMIS and HKUST, fractional visiting professor | [stated] (P) [T2] |
| 2025 | Constantin Carathéodory Prize, Global Optimization Congress | [stated] (P) [T2][T3]. No external confirmation found |
| 07/02/2026 | Plenary talk, HORIZONS 2026, CEI VinUni (Vietnam), signed "Yinyu Ye (SJTU and Stanford)" | [stated] (P) [T21] |
| 09/23/2026 | Homepage note "Can Pure Offline Data Learning Replace Linear Programming Algorithms?" | [practice] (P) [T22] |

**Funding as a dated record of turns** [stated] (P) [T2, §8], listed by NSF grant topic: linear programming (1990–92); LP interior-point algorithms (1993–95); mathematical programming (1995–98); computational complexity (1997–2000); **SDP and approximation algorithms (1999–2003)**; **MDP and LP (2003–06)**; **complexity of market equilibrium (2006–10)**; GOALI region partitioning (2008–11). Other grants: AFOSR dynamic resource allocation (2009–12); DOE systems-biology optimization software (2009–12); Precourt EV fleet (2012–13); AFOSR quadratic mixed-integer optimization (2012–15); CEPRI power dispatch (2014–). [inferred] Each NSF grant starts at or slightly before the point where the corresponding line appears in the publication record (see §3). The grants therefore date the turns more precisely than prizes do.

---

## 2. Lineage

### 2.1 Advisors and mentors

- [stated] (P) CV: advisor Edison Tse, committee Chiu, Dantzig, Luenberger and Tse [T2].
- [observed] (S) Mathematics Genealogy Project id 12397: "Advisor 1: Edison Tack-Shuen Tse Advisor 2: George Bernard Dantzig" [T23]. Tse: PhD MIT 1970 under Michael Athans, thesis on optimal control with incomplete information. Dantzig: PhD Berkeley 1946 under Jerzy Neyman [T23].
- [stated] (P) He names three mentors in the 2020 essay: "My first mentor was George Dantzig"; "My second important mentor was David Luenberger"; "A third mentor was Michael Todd" [T9]. The 2009 speech says of Dantzig: "He was a great advisor, and a remarkable person as well" [T7].
- [inferred] The lineage runs from control theory (Tse–Athans) and statistics (Dantzig–Neyman) to LP. Ye's systems-and-control B.S. and his control-theory advisor fit the "Engineering-Economic Systems" setting, and the LP specialization came through Dantzig and Todd. Tse's field is not visible in Ye's own research topics.

### 2.2 Students (a sample of the lineage that carries the lines forward)

- [stated] (P) The CV lists 34 PhD advisee entries, 1992–2024 (one name appears twice), and 3 postdocs: Dachuan Xu 2006, Roger Behling 2014, Ruoyu Sun 2017 [T2]. [observed] (S) MGP lists 16 students and 29 descendants [T23]. Agent 04 covers the mentoring side, so here I record only how the students map onto the lines:
  - IPM and solver line: Erling Andersen (1996, "Founder of MOSEK.com") → MOSEK; Steve Benson (1999) → DSDP; Dongdong Ge (2009) and Zizhuo Wang (2012) → COPT (both co-author the "Cardinal Optimizer (COPT) User Guide", arXiv 2208.14314); Oliver Hinder (2019) → nonconvex IPM, then co-author of PDLP (Applegate et al., arXiv 2106.04756) [T2][T31].
  - SDP and sensor localization: Pratik Biswas (2007), Anthony Man-Cho So (2007), Jiawei Zhang (2004, SDP approximation and facility location) [T2].
  - DRO, online LP and markets: Erick Delage (2009), Shipra Agrawal (2011), Zizhuo Wang, Xiaocheng Li (2020), Chunlin Sun (2024) [T2].
  - MDP: Ian Post (2015) [T2].
- [inferred] A former student's work has more than once preceded Ye's own entry into a line. Hinder co-authored PDLP (June 2021) [T31], and Ye's team produced cuPDLP-C in December 2023 (§4.11). Ge leads the SJTU Institute of Intelligent Computing (上海交通大学智能计算研究院院长, [T26]), and Ye took an SJTU post in April 2024 [T2]. These are dated co-occurrences, not stated causes.

---

## 3. Research-direction timeline

Topic counts come from DBLP titles, classified by my own keyword rules [inferred, computed from T29]. The counts show when a line enters and fades; they are not a precise census.

| Line | First verified item | Peak (DBLP title hits by 5-year block) | Fades / returns | Stated or inferred trigger | Timing relative to the field |
|---|---|---|---|---|---|
| A. Karmarkar-type and interior-point LP/QP | Ye & Kojima, "Recovering optimal dual solutions in Karmarkar's polynomial algorithm for linear programming", MP 39, 1987, 10.1007/BF02592079 | 1990–99 (31 of 51 IPM-keyword titles) | "Projective" titles only 1989–91; "potential" 1991–94; "homogeneous" 1994–99, again 2013–15 and 2026 | [stated] Karmarkar's 1984 seminar [T10][T9]. Karmarkar, Combinatorica 1984, 10.1007/BF02579150 | First wave: first paper about three years after Karmarkar [inferred] |
| B. Nonconvex QP / trust region inside IPMs, later second-order methods | Ye, "An Extension of Karmarkar's Algorithm and the Trust Region Method for Quadratic Programming", *Progress in Mathematical Programming*, 1989, 10.1007/978-1-4613-9617-8_3 | 1989–98, then 2022–26 (9 of 10 "second-order/trust-region" titles after 2021) | Ye 1992 (10.1007/BF01580903), Ye 1998 (10.1007/BF01581726); Ye & Zhang 2003 SIOPT (10.1137/S105262340139001X); 2015–19 nonconvex IPMs; returns as DRSOM (arXiv 2208.00208) and HSODM (arXiv 2211.08212) | [stated] In 2022, existing fast nonconvex methods "are hybrid and/or randomized methods and seem difficult to be implemented. Our approach: Reduce dimension in SOM" [T15, slide 9] | The early work (1989–98) came before the nonconvex-complexity literature. The 2022 return came after Nesterov–Polyak, Cartis–Gould–Toint and Curtis–Robinson–Samadi, which his slides cite [T15, slide 7] |
| C. SDP relaxation and approximation | The monograph's §9.5 "Positive semi-definite relaxation" (1997) [T10]; Benson, Ye & Zhang, SIOPT 2000, 10.1137/S1052623497328008 | 2000–09 (34 of 48) | Ye 2001, ".699-approximation algorithm for Max-Bisection", MP, 10.1007/pl00011415; tapering after 2010 | [stated] NSF grant "Semidefinite Programming and Approximation Algorithms, 1999-2003" [T2]. [inferred] Goemans & Williamson, JACM 1995, 10.1145/227683.227684; Halperin & Zwick describe Ye's result as an extension of the Goemans–Williamson Max-Cut method [T30] | Early follower of Goemans–Williamson, about 2–5 years later [inferred] |
| D. Sensor-network localization | Biswas & Ye, IPSN 2004, 10.1145/984622.984630 | 2005–09 (10 of 20) | Exit via "Beyond convex relaxation" (Ji, Sze, Zhou, So & Ye, INFOCOM 2013, 10.1109/INFCOM.2013.6567056); back as a test problem in Tang, Toh, Xiao & Ye, SISC 2024, 10.1137/23M1567229 | [stated] 2004 BASES Innovators' Challenge first place (Biswas & Ye); patent 2005; Polaris Wireless 2006–07 "Mobile Phone Localization" [T2] | [inferred] He brought an SDP tool to an engineering problem the sensor community was then working on. Whether others had used SDP for localization before 2004 was not checked |
| E. Market equilibrium / algorithmic game theory | Ye, "Computing the Arrow-Debreu Competitive Market Equilibrium and Its Extensions", LNCS 2005, 10.1007/11496199_2; Ye, "A path to the Arrow–Debreu competitive market equilibrium", MP 2007/08, 10.1007/s10107-006-0065-5 | 2005–09 (16 of 39 market/equilibrium/game-keyword titles) | Returns 2020–26: Jalota, Pavone, Qi & Ye, GEB 2023 (10.1016/j.geb.2023.06.007); Jalota & Ye, OR 2025 (10.1287/opre.2023.0636); Zhang, He, Jiang & Ye, arXiv 2508.04822 (2025) | [stated] NSF grant 2006–10; WINE co-organizer from 2005 [T2]. [stated, his 2025 retrospective] "Combinatorial (Devanur et al. 2002)" came first, then "IPMs/Weighted LCP: (Ye 2008)" [T20, slide 7] | Follower, about three years after the theoretical-CS start [inferred from his own slide] |
| F. MDPs and RL | Ye, "A New Complexity Result on Solving the Markov Decision Problem", MOR 2005, 10.1287/moor.1050.0149 | 2020–24 by count (7 of 16 MDP/RL-keyword titles) | Ye, MOR 2011, 10.1287/moor.1110.0516; Post & Ye, MOR 2015, 10.1287/moor.2014.0699; Sidford, Wang, Wu, Yang & Ye, arXiv 1806.01492 (NeurIPS 2018); Mei, Sun & Ye, arXiv 2606.29568 (2026) | [stated] NSF grant 2003–06 [T2]. 2015: "There was a significant gap between theoretical research and practical application … It bothered me." [T11] | Against the consensus: he worked on the question after published results suggested simplex and policy iteration could take exponentially many steps [T11]. Entry into RL sample complexity (2018) coincides with the ML wave [inferred] |
| G. Distributionally robust optimization | Delage & Ye, OR 58, 2010, 10.1287/opre.1090.0741. Delage won the 2008 Nicholson prize for it [T2] | Small counts; 2020–24 (5 of 11) | Later OT-based DRO, e.g. OR 2025 (10.1287/opre.2021.0243, via DBLP) | [stated] Boeing 2004–2013, "Stochastic and Robust Decision Making and Optimization" [T2]; the speech thanks "the Boeing Company for picking me as a research partner" [T7]. [stated] 2017: "在测不准的情况下，在决策上是不是可以做点工作" *tr. where things cannot be predicted accurately, can we do some work on the decision side* [T12] | Roughly contemporaneous with Calafiore & El Ghaoui, JOTA 2006, 10.1007/s10957-006-9084-x. The naming claim is contested; see C5 |
| H. Online LP and online allocation | Agrawal, Wang & Ye, arXiv 0911.2974 (v1 2009-11-16); OR 62, 2014, 10.1287/opre.2014.1289 | 2020–26 (32 of 38 online-keyword titles) | Never left. Li & Ye, OR 2022, 10.1287/opre.2021.2164; LLM-serving papers 2025–26 | [inferred] His ISMP 2022 plenary cites "Devanur et al (2009)" immediately before "Agrawal/Wang/Y (2010,14)" and names the "Adwords application" [T16]. Devanur & Hayes, EC 2009 (published 2009-07-06), 10.1145/1566374.1566384 | Close follower: arXiv v1 about four months after Devanur–Hayes [practice, dates from T30/T31] |
| I. Sparse / Lp nonconvex complexity | Chen, Xu & Ye, "Lower Bound Theory of Nonzero Entries in Solutions of ℓ2-ℓp Minimization", SISC 2010, 10.1137/090761471; Ge, Jiang & Ye, MP 2011, 10.1007/s10107-011-0470-2 | 2010–24 | Bian, Chen & Ye, MP 2015, 10.1007/s10107-014-0753-5; Haeser, Liu & Ye, MP 2019, 10.1007/s10107-018-1290-4 | [inferred] The late-2000s sparse-recovery wave; no stated trigger found | Follower [inferred] |
| J. ADMM and coordinate descent | Chen, He, Ye & Yuan, "The direct extension of ADMM for multi-block convex minimization problems is not necessarily convergent", MP 155, 2016, 10.1007/s10107-014-0826-5 | 2015–19 (5 of 10) | Sun, Luo & Ye, MOR 2020, 10.1287/moor.2019.0990; Sun & Ye, MP 2021, 10.1007/s10107-019-01437-5; ADMM-based IPM (IJOC 2025, 10.1287/ijoc.2023.0017) | [inferred] ADMM was popularized by Boyd et al., FnT ML 2011, 10.1561/2200000016. Ye's homepage counts "Convergence of Multi-Block ADMM" among questions "where we settled long-time open questions" [T1] | Entered as a critic after the method was already popular: first a negative result, then a randomized repair |
| K. Solvers and software | COPL codes (COPL_LP "last updated May 21, 98"), DSDP (Benson & Ye, ACM TOMS 2008, 10.1145/1356052.1356057) [T1 Col page][T30] | 2017–26 (LEAVES, COPT; SOLNP+ TOMS 2024, 10.1145/3699956; HDSDP TOMS 2025, 10.1145/3721123) | Continuous since the 1990s, and much larger from 2017 | [stated] 2025: companies came to him after “外部环境的变化” *tr. changes in the external environment* (§4.10) [T13]. [stated] 2017: turning results into technology (§4.10) [T12] | See §4.10 |
| L. GPU first-order LP/QP/SDP/conic | Lu, Yang, Hu, Huangfu, Liu, Liu, Ye, Zhang & Ge, "cuPDLP-C", arXiv 2312.14832 (v1 2023-12-22) | 2024–26 | Han et al., arXiv 2407.15049 (2024); PDHCG, IJOC 2025, 10.1287/ijoc.2024.0983; PDCS, arXiv 2505.00311; D-PDLP, arXiv 2601.07628; arXiv 2608.09159; arXiv 2607.17933 | [stated] "Problem Scales in Real-World Scenarios Are Growing Rapidly, and Exceeding the Limits of CPU-Based Mathematical Programming Solvers" [T21, slide 7] | Follower through collaboration: about one month after Lu & Yang's cuPDLP.jl (arXiv 2311.12180, v1 2023-11-20), whose authors he co-wrote with, and 2.5 years after PDLP (arXiv 2106.04756, v1 2021-06-09) [practice, T31] |
| M. ML optimizers, LLM systems, LLM-for-OR | Adam-mini, arXiv 2406.16793 (2024; ICLR 2025) | 2025–26 (11 of 14 LLM/AI-keyword titles) | arXiv 2508.06133, 2601.17855, 2605.06113, 2606.22327, 2607.03948 (serving); 2510.05186 (training pipeline); 2505.11792 (SIRL, NeurIPS 2025); 2605.28158 (OR-Space) | [stated] LLM inference cost, latency and energy [T19, slide 17]. In 2025: "解决人工智能的耗能、耗时，需要运筹学的方法" *tr. solving AI's energy and time consumption needs OR methods* [T13] | Follower of the LLM wave. He enters through his own online-LP and scheduling tools, not through model design [inferred] |

---

## 4. Turns and their triggers

### 4.1 Into OR and LP (1982–1984): three stated versions

- [stated] (P, 2017) "1982 年刚到美国读书的时候 AI 非常热……那时候要搞所谓的专家系统 AI 空间，学的语言是学 Lisp，没有很多的数据，人家有些就总结不出来，AI 就慢慢的冷下去了。我比较喜欢数学，就从事了运筹学。" *tr. When I arrived in the US in 1982 AI was very hot … it was so-called expert systems, the language was Lisp, there was not much data, people could not summarize [the rules], and AI slowly cooled down. I liked mathematics better, so I went into operations research.* [T12]
- [stated] (P, 2025) "当时我的导师给我们布置任务，构建一个中医的专家系统……所以在当时的条件下，构造这样一个系统，数据是不够的。但恰恰是遇到了这些问题，使我对“量化”产生了兴趣，从而投身运筹学的研究。" *tr. My advisor gave us the task of building an expert system for traditional Chinese medicine … under the conditions of the time there was not enough data to build such a system. But it was exactly these problems that made me interested in quantification, and so I devoted myself to OR research.* [T13]
- [stated] (P, 1996) "On a sunny afternoon in 1984, one of my officemates told me that there would be a seminar given by N. Karmarkar … At the time, my knowledge of linear programming was limited to one optimization course and one research project with Prof. David Luenberger … I was not particular enthusiastic about the statement from the speaker that a new interior-point method would be 40 times faster than the simplex method, but I was amazed by the richness and applicability of linear programming as a whole. That was how and when I determined to devote my Ph.D. study to mathematical programming." [T10, Preface p. xiii]
- [stated] (P, 2020) "I remember the day I became fascinated by linear programing. It was a sunny day in 1984 … I quickly decided to devote my PhD to this branch of mathematics." [T9]
- **Trigger type** [inferred]: a failure in one field (AI with too little data) followed by a new tool (Karmarkar's method) seen in person. The decision point is a seminar, not a problem he met in practice. The three accounts differ in emphasis; see C3.

### 4.2 From projective to potential-reduction and primal-dual IPMs (1987–1994)

- [practice] (P) The sequence: dual recovery in Karmarkar's method (1987); extension to convex QP (Ye & Tse 1989, 10.1007/BF01587086); projective transformations (Ye, SIAM J. Comput. 1990, 10.1137/0219030; Todd & Ye, MOR 1990, 10.1287/moor.15.3.508); potential reduction (Ye 1991, MP 50, 10.1007/BF01594937; column generation, SIOPT 1992, 10.1137/0802002); predictor-corrector (Mizuno, Todd & Ye, MOR 1993, 10.1287/moor.18.4.964); quadratic convergence (Ye, Güler, Tapia & Zhang, MP 1993, 10.1007/BF01581242); homogeneous self-dual (Ye, Todd & Mizuno, MOR 1994, 10.1287/moor.19.1.53) [T30].
- [practice] (P) "Projective" appears in DBLP titles only in 1989–1991, and the "build-up" scheme (with Dantzig) appears only in 1990 [T29]. **Abandoned path**: the projective framework. No statement explaining why was found.
- [stated] (P) The environment he credits: "a group of fabulous colleagues who worked on Interior-Point Algorithms for LP and SDP: Todd, Anstreicher, Nemirovskii, Vavasis, (… long name list). I felt so lucky, at the beginning of my career, to associate with such a wonderful, unselfish, and supporting group in a very competitive research environment. Everyone was cheering for everyone else; it was like a family." [T7]
- [inferred] What drove the turn: working inside the community (Cornell visits in 1987 and 1993, Rice in 1991) and the race to get the best iteration bound. The co-author lists track the visits: Todd and Mizuno (Cornell), Güler, Tapia and Zhang (Rice) [T2][T30].
- **Era and resources** [stated] (P): an assistant professor at Iowa, mostly solo or 2–3 authors, NSF grants for LP (1990–92, 1993–95) and College of Business summer grants [T2]. AT&T LP-solver consulting 1992–93 [T2]. Software in C and Fortran for DOS, HP and Linux, with MPS input and options "to return an optimal basic solution and to detect infeasibility or unboundedness" (COPL_LP, "last updated May 21, 98") [T1 Col page].

### 4.3 From LP-IPM to SDP relaxation and approximation (about 1995–2003)

- [practice] (P) The monograph (1996/97) already has §9.5 "Approximating Quadratic Programming: Positive semi-definite relaxation" [T10, table of contents]. It is followed by Benson, Ye & Zhang (SIOPT 2000, the dual-scaling DSDP line), Ye 2001 (Max-Bisection, 10.1007/pl00011415), Ye & Zhang 2003 (10.1137/S105262340139001X) and Nesterov, Todd & Ye 1999 (10.1007/s10107980009a) [T30].
- [stated] (P) NSF "Semidefinite Programming and Approximation Algorithms, 1999-2003"; "Principal Organizer (1 of 2), Semidefinite Programming and Large-Scale Discrete Optimization Workshop, DIMACS and Princeton University, 1999" [T2].
- [inferred] Trigger: a new tool (IPMs extend to SDP) meeting a new question (Goemans–Williamson 1995 showed that SDP relaxations give approximation guarantees). The step from his IPM work was short.
- [observed] (S) Anstreicher, 2024: "In their 2003 paper “New results on quadratic minimization”, Ye and Zhang introduced fundamental theory for SDP relaxations applied to extended trust-region subproblems. This paper stimulated a long line of research that continues to this day" [T25].

### 4.4 The move from Iowa to Stanford (2002) and the change of topics that followed

- [stated] (P) "I am so grateful to Dick Cottle, Pete Veinott, Peter Glynn, Michael Saunders, Ben van Roy, and Stephen Boyd, who brought me back to Stanford, where I learnt many new things and have had many talented students. Especially, Pete has been a mentor for me." [T7]
- [practice] (P) After 2002 the topics widen fast. Sensor localization begins in 2004, market equilibrium and MDPs in 2005, DCP/CVX with Boyd in 2006 (Grant, Boyd & Ye, 10.1007/0-387-30528-9_7), DRO around 2008–10, online LP in 2009 [T30][T31]. The largest student cohort in his CV graduates in 2007–2014 [T2]. Industry partners multiply: Boeing 2004–13, American Express 2005–08, Huawei 2005–10, Polaris Wireless 2006–07, AtRoad 2006–07 [T2].
- [inferred] Trigger: the move itself. At Stanford he had a courtesy EE appointment and Boyd and Saunders as colleagues, with larger student cohorts and Bay Area industry partners. Several new lines are the problems of specific partners, formulated as convex or LP models: localization (Polaris), robust decisions (Boeing), network economics. The moves also broadened his venues: WINE, SODA, INFOCOM, IPSN and ACM TOSN appear in this period [T29].

### 4.5 MDPs: a decade-long line started against negative results (2003–2026)

- [stated] (S with direct quotes, 2015) "There was a significant gap between theoretical research and practical application," said Professor Ye. "It bothered me." The report adds that he "listed recent work by academics that seemed to disprove the efficiency of the methods" [T11].
- [practice] (P) NSF "Markov Decision Problem and Linear Programming, 2003-2006" [T2] → Ye 2005 MOR (an IPM-based strongly polynomial bound) → Ye 2011 MOR (simplex with Dantzig's rule and policy iteration are strongly polynomial for a fixed discount) → Post & Ye 2015 MOR (deterministic MDPs) → Sidford et al. 2018 (sample complexity with a generative model) → constrained MDPs (arXiv 2402.16324, 2024) → Jiang, Ye & Zong, ORL (10.1016/j.orl.2026.107529, online 2026) → Mei, Sun & Ye, arXiv 2606.29568 (v1 2026-06-28), "The Simple Strategy-Iteration Method is Strongly Polynomial for the Turn-Based Deterministic Forward Game" [T30][T31].
- [inferred] Trigger: a gap between theory and practice that he himself names, answered with the tools of line A. The line shows his typical time scale: the IPM bound came first (2005), the stronger simplex result six years later (2011), extensions another 4 to 15 years later.

### 4.6 DRO and online LP (2008–2014): application partners, then theory

- [stated] (P) Homepage: DRO "where we created the name DRO first time", and Online LP "as a general model for dynamic resource allocations, both are populary applied in business and industries" (sic) [T1].
- [practice] (P) Delage & Ye, OR 2010, and Agrawal, Wang & Ye, arXiv v1 2009-11-16 (published OR 2014, revised v2 2013 and v3 2014) [T30][T31]. At the time Boeing funded "Dynamic Resource Allocation" (2004–13) and AFOSR funded "Optimization Algorithms and Equilibrium Analysis for Dynamic Resource Allocation" (2009–12) [T2].
- [inferred] Trigger: industry questions (Boeing, advertising) plus a recent CS result (Devanur–Hayes 2009) that he recast as LP duality with learned prices. The online-LP line is the longest-running of his post-2002 lines and is the one he now applies to LLM serving (§4.12).

### 4.7 Nonconvex and sparse problems, ADMM (2010–2019): critic, then repair

- [practice] (P) The Lp-minimization complexity papers (2010–2015), then the multi-block ADMM counterexample (MP 2016) and its randomized fix (MOR 2020) [T30].
- [stated] (P) The homepage frames the ADMM and simplex/policy-iteration work as cases "where we settled long-time open questions" [T1].
- [inferred] Trigger: popular methods whose convergence nobody had checked (ADMM after Boyd et al. 2011). He enters once a method is widely used and asks whether it actually converges. The same stance underlies the MDP line (§4.5) and the 2026 note on learning (§4.13).

### 4.8 The second-order / trust-region return (2015–2026)

- [practice] (P) Nonconvex IPMs with Hinder (arXiv 1801.03072, v1 2018-01-09; MOR 2024, 10.1287/moor.2020.0274) → DRSOM (arXiv 2208.00208, v1 2022-07-30) → HSODM (arXiv 2211.08212; MOR 2026, 10.1287/moor.2023.0132) → HSODF (MP 2026, 10.1007/s10107-025-02230-3) → universal trust region (arXiv 2311.11489; JSC 2026, 10.1007/s10915-025-03154-y) → accelerated trust region (arXiv 2511.00680) → first-order IP trust region for linear constraints (arXiv 2604.24488, v1 2026-04-27) [T30][T31].
- [stated] (P, 2022 slides) He places the line in his own history: "For the ball-constrained nonconvex QP (trust-region subproblem): O(loglog(𝜖-1)); see Y (1989,93), Vavasis&Zippel (1990)" and "For nonconvex QP with a polyhedral constraint: O(𝜖-1); see Y (1998)" [T15, slide 4]. He also claims early priority: "Trust-region with the fixed-radius strategy, 𝑂(𝜖−3/2), see the lecture notes by Ye† since 2005" [T15, slide 7]. Those lecture notes were **not read**, so the claim is unchecked; see C9.
- [stated] (P) Motivation: FOM-with-negative-curvature methods "are hybrid and/or randomized methods and seem difficult to be implemented. Our approach: Reduce dimension in SOM" [T15, slide 9].
- [inferred] Trigger: implementability, a practitioner's objection to the existing complexity-optimal methods. The team is new (Shanghai: Chuwen Zhang, Bo Jiang, Chang He, Yuntian Jiang, with Ge; see 04-mentorship), and the tool (a 2-D trust-region subproblem) goes back to his 1989 trust-region QP. [stated] (P) The 2022 talk was billed at HKUST as "DRSOM: A Dimension-Reduced Second-Order Method for Machine and Deep Learning" [T4], so ML was part of the target audience.
- **Relevance for a solver team** [inferred]: he came back to nonlinear programming through unconstrained and simply constrained second-order steps. That is where his recent ideas are densest. Classical SQP or filter/penalty globalization of general NLP is not among his recent topics.

### 4.9 Solvers as the unifying goal (2017–2026)

- [stated] (P, 2017) "以前我认为我就要搞出个万能的算法，解所有的线性规划都要解得快，但是我后来反观看AI是非常定制的，我可以对某一类方法用的好就用那个方法，不是追求某一个统一的算法" *tr. I used to think I had to create a universal algorithm that solves every LP fast, but looking back at AI, it is highly customized: if one method works well for one class, use that method, rather than pursuing a single unified algorithm* [T12].
- [stated] (P, 2017) "我原来比较重视理论，很多问题都是写文章，证明一些东西，也小有成就，但是人到年纪大的时候维护自己工作利益所在。我觉得最大的利益还是对一般人生活产生一些影响" *tr. I used to value theory more, writing papers and proving things, with some success; but as one gets older [one asks] where the value of one's work lies. I feel the greatest benefit is still to have some effect on ordinary people's lives* [T12]. And: "这就是到一定年龄的时候，就追求鼓励这些年轻人……把自己的学术成果转化成技术" *tr. at a certain age one seeks to encourage young people … to turn their academic results into technology* [T12].
- [stated] (P, 2021) "The innovation of efficient optimization methods/algorithms should be driven by scientific/theoretical research, besides software engineering and coding" and "The development of mathematical programming solvers is best done by a small dedicated team whose members have passion and love in optimization" [T14, slide 61].

### 4.10 COPT and the move of his center of gravity to China (2017–2024)

- [stated] (P, 2025) "近年来，由于外部环境的变化，导致一些国内企业难以再继续使用西方的求解器产品，必须转向“自力更生”。一些企业找到了我和我的学生们，希望我们能够迎着前所未有的困难“顶上去”，开发出中国自己的求解器。我们也的确做到了。" *tr. In recent years, because the external environment changed, some domestic companies could no longer use Western solver products and had to turn to self-reliance. Some companies came to me and my students, hoping we would push through unprecedented difficulties and develop China's own solver. And we did.* [T13]
- [stated] (P) Dated milestones from his 2026 slides: "2017 Our team released the open-source solver LEAVES"; "2019 Our team released the professional solver COPT" [T21, slide 4]. [observed] (S) Ge's 2024 abstract: COPT's "journey from inception to becoming the second best software globally in its field" [T25].
- [practice] (P) CUHK-SZ 2022.10, SJTU 2024.4, SIMIS 2024.10, HKUST 2024.11; Stanford chair ends 2024.8 [T2]. [observed] (S) In April 2024 Ge is 上海交通大学智能计算研究院院长 *tr. dean of the SJTU Institute of Intelligent Computing* [T26].
- [inferred] Trigger: outside demand, since companies needed a domestic solver. The group had been built at Stanford (students who went back and founded Cardinal Operations; see 04-mentorship) and was later placed in institutions led by former students. **No statement from him on why he took the SJTU post was found** (Gaps).

### 4.11 GPU first-order solvers (2023–2026)

- [stated] (P, 2026 slides) "In November 2023, in collaboration with the University of Chicago/MIT, the COPT team released cuPDLP-C, the world's first linear programming algorithm under a CPU+GPU heterogeneous computing architecture" [T21, slide 11]. The same slide credits the algorithm: "PDLP: Incorporating multiple acceleration techniques into PDHG (Applegate et al. 2021)".
- [practice] (P) Dates: PDLP arXiv v1 2021-06-09 (Applegate, Díaz, Hinder, Lu, Lubin, O'Donoghue, Schudy); cuPDLP.jl v1 2023-11-20 (Lu, Yang); cuPDLP-C v1 2023-12-22 (Lu, Yang, …, Ye, Zhang, Ge) [T31]. [stated] (P) Why GPUs are hard for classical methods: "First-order algorithms suffer from low precision; numerically difficult problems converge slowly and unstably" and "Second-order algorithms involve matrix inversion/factorization, for which parallel acceleration on GPU yields limited improvement" [T21, slide 8].
- [practice] (P) Then comes a rapid series. Low-rank SDP on GPU (arXiv 2407.15049, 2024); PDHCG for QP (IJOC 2025); PDCS for conic programs (arXiv 2505.00311); multi-GPU D-PDLP (arXiv 2601.07628, v1 2026-01-12); GPU conic QP with local linear convergence (arXiv 2608.09159, v1 2026-08-10); a distributed rank-adaptive ALM for SDP (arXiv 2607.17933, v1 2026-07-20) [T31]. There is also GPU work on the interior-point side. The 2026 slides show COPT GPU-barrier results on NVIDIA and Chinese GPUs ("BW1000", "X201") [T21, slides 15–16].
- [stated] (P) He reports impact: "NVIDIA cuOpt is partly inspired by the 2023 cuPDLP-C work of Ye, Ge, and Lu, with its early codebase and design influenced by cuPDLP-C." [T21, slide 41]. This is his claim about another company's product; I did not check it against NVIDIA.
- [inferred] Trigger: new hardware together with a first-order method that became competitive on it (PDLP). He entered as a fast follower by joining the authors of cuPDLP.jl. Then he did what he did with IPMs in the 1990s: widened the problem class (LP → QP → SDP → conic) and scaled up (single → multi-GPU).
- **Era and resources** [stated] (P): NVIDIA A6000 and H100, "8 H100s", and Chinese "Muxi" GPUs; the deck claims "Excluding hardware improvement, LP (COPT and others) speed becomes 3.5x faster on average in the past 4 years" [T21, slide 14]. The deck's PDF author metadata is "Dongdong Ge" [T21], so the wording may be the team's.

### 4.12 LLMs: as a workload, as a modelling assistant, as an optimizer target (2024–2026)

- [practice] (P) Three strands, each with arXiv ids checked:
  - Optimizers for LLM training: Adam-mini (arXiv 2406.16793; ICLR 2025, with his former postdoc Ruoyu Sun); OSDN (arXiv 2605.13473).
  - LLM systems as online LP and scheduling problems: arXiv 2508.06133, 2508.14544, 2510.05186, 2601.17855, 2605.06113, 2606.22327, 2607.03948.
  - LLMs that write optimization models: SIRL (arXiv 2505.11792, NeurIPS 2025) and the OR-Space benchmark (arXiv 2605.28158) [T31][T29].
- [stated] (P) The 2025 plenary motivates the systems strand: "Traditional schedulers like FCFS fail to scale with LLM workloads - we need better approaches!" [T19, slide 17]. The 2026 plenary uses "Huawei's Real LLM Serving Trace" [T21, slide 44].
- [observed] (S) In the April 2024 SJTU lecture he demonstrated "其研究团队在研的数学规划对话建模软件" *tr. the conversational math-programming modelling software his team is developing* after showing ChatGPT 3.5's modelling weaknesses [T26].
- [inferred] Trigger: a new workload with money attached (inference cost and GPU idle time). He enters through the tool he already owns (online LP with learned dual prices), not by designing models.

### 4.13 Where he stands now on learning versus algorithms (September 2026)

- [stated] (P) In the note dated September 23, 2026, he constructs LP instances where a basis that is optimal at two nearby data points is not optimal between them. He concludes: "Therefore, the pure offline learning from data, basic on data similarity, is unlikely to accurately predict its optimal basis or optimal solutions for linear programming." and "Therefore, Data learning may be more helpful to Integer Programming due to its solution-Immutability." [T22]
- [stated] (P) In July 2026 he closes the HORIZONS deck with "ML-Based or LLM-Based Hyperparameter Tuning", "ML/DL/LLM-Assisted Cutting Plane Generation" and "AI-Guided Branching and Search Path Evolving" as the "New Paradigm" [T21, slide 48]. He also asks "How to “prove” a math theorem using (inexact) numerical Algorithms?" after cuLoRADS results on the quantum ordered-search SDP [T21, slide 37].
- [inferred] His current stance: AI serves as a helper around the solver (presolve, tuning, branching, modelling) and as a new source of large instances. It does not replace the continuous algorithm. The note supplies a small counterexample in support. His ADMM and MDP work took the same shape: test a popular belief with a counterexample.

---

## 5. Cross-cutting patterns of entry and exit

1. **Early entry when the tool is new, as a follower when the application is new.** [inferred from §3] He was early on IPMs (about three years after Karmarkar), and his SDP relaxation work began about 2–5 years after Goemans–Williamson. He followed within about four months on online LP, about three years on market equilibria and about a month on GPU PDLP (via collaboration). He entered LLM systems during the boom. What he adds is mostly an LP, IPM or duality reformulation with a complexity or regret bound. [stated] His 2023 "Research Tips" slide lists paired terms without saying which side he prefers: "Theory vs Practice", "Model vs Methodology", "Focus vs Broadness", "Quality vs Quantity", "Individual vs Group", "In mind vs On paper" [T8, slide 15].
2. **Few clean exits; returns with new tools.** [practice] The DBLP keyword years show every major line recurring after its peak: homogeneous (1994–99, 2013–15, 2026), sensor/localization (2004–13, 2016, 2023–26), market/equilibrium (2005–16, 2020–25), second-order/trust-region (1994, 2022–26) [T29]. [inferred] He treats an old application as a test bed for a new method. Sensor-network localization, for instance, reappears as the application of the Riemannian DRSOM (SISC 2024).
3. **A negative result before a positive one.** [practice] ADMM divergence, then randomized ADMM. Exponential simplex examples, then strong polynomiality for fixed discount. "Beyond convex relaxation" after the SDP localization work. The 2026 LP-sensitivity counterexample before recommending learning for IP. The accelerated trust-region paper reports its own trade-off in the abstract: "quadratic local convergence is preserved under moderate global acceleration, but it breaks down when pursuing extreme global efficiency" [T31, arXiv 2511.00680].
4. **Turns are dated by money and partners before papers.** [inferred] NSF topic grants (SDP 1999, MDP 2003, markets 2006) and industry partners (AT&T 1992, Boeing 2004, Polaris 2006, Cardinal Operations 2017, Huawei traces in 2026) either precede or coincide with the first papers of each line [T2][T21].
5. **Team structure changes with the turn.** [practice] DBLP shows 1–3 authors per paper in the 1990s and 5–9 in 2025–26 (e.g. arXiv 2605.06113 has nine authors) [T29][T31]. Details are in 01-publications §0 and 04-mentorship.

---

## 6. Failures, abandoned directions, corrections

- [stated] (P) **AI in 1982–83, abandoned** because of too little data (§4.1) [T12][T13].
- [stated] (P) **Max-Bisection 0.7, failed**: "had a provable approximation rate of 0.699 … She said this number looked like a “supermarket number” … and asked me to make it to 0.7. I tried very hard but could not prove it. Later, somebody did use a stronger SDP relaxation to make the bound 0.701, which still stands as the best today." [T7]. [observed] (P, other authors) Halperin & Zwick, *Random Structures & Algorithms* 20 (2002), "A unified framework for obtaining improved approximation algorithms for maximum graph bisection problems", 10.1002/rsa.10035: "Our results improve, extend and unify results of Frieze and Jerrum, Feige and Langberg, Ye, and others." Their ratio is not in the abstract, and the paper was **not read**. Whether 0.701 still "stands as the best" after 2009 was **not checked**.
- [practice] (P) **Karmarkar's projective framework, abandoned** after 1991 (§4.2); no stated reason.
- [stated] (P) **A universal LP algorithm, abandoned as a goal** in favour of customized methods (2017, §4.9) [T12]. See C8 for the tension with COPT.
- [practice] (P) **Convex relaxation for sensor localization, partly abandoned**: "Beyond convex relaxation: A polynomial-time non-convex optimization approach to network localization" (INFOCOM 2013) [T30].
- [practice] (P) **DRSOM has no journal version.** The CV lists it only as "NeurIPS Workshop: Order up! The Benefits of Higher-Order Optimization in Machine Learning, Spotlight Presentation, 2022" (C80) [T2]. arXiv v3 (2023-07-02) says "Considerable changes in the main text" [T31]. The later HSODM and HSODF papers did reach MOR and MP in 2026 [T30]. Whether DRSOM was rejected, withdrawn or never submitted is unknown.
- [practice] (P) **Retitled papers**: DBLP records arXiv 2508.04822 as "The Implicit Barrier of Utility Maximization: An Interior-Point Approach for Market Equilibria", while its current arXiv title is "The Second-Order Tâtonnement: Decentralized Interior-Point Methods for Market Equilibrium" (v3 2025-09-27, "improve organization") [T29][T31]. DBLP likewise keeps DRSOM's first title, "… and Preliminary Analyses" [T29]. [inferred] Both changes reframe the paper for a different audience: an IPM framing becomes an economics framing.
- [practice] (P) **Published corrections** (contents **not read**): Burer & Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", MP 2021, 10.1007/s10107-021-01684-5; Dang & Ye, "Erratum/Correction to 'On the complexity of an expanded Tarski's fixed point problem under the componentwise ordering'", TCS 2020, 10.1016/j.tcs.2019.03.014 [T30]. [practice] Arxiv 1801.03072 v2, two days after v1: "fixed typo in sign of dual multiplier in KKT system" [T31].
- **No retracted claim or documented rejection was found.**

---

## 7. Era and resource context by phase

| Phase | Position and seniority | Team | Compute and tools | Money and partners | Source |
|---|---|---|---|---|---|
| 1983–1988 | PhD student, lecturer, software job at Integrated Systems | Solo or with advisor or Todd; "I published three papers while I was working on my PhD" [T9] | Not documented | Fellowships, RA and TA posts [T9] | [T2][T9] |
| 1988–2002 | Iowa, assistant professor to named chair | Mostly solo or 2–3 authors; a few PhD students (Kaliski, Huang, Benson); Andersen as a visiting student | C and Fortran codes (COPL_LP, QP, LC, GP; DSDP), MPS input, DOS/HP/Linux [T1 Col page] | NSF topic grants; AT&T, MCI; foreign fellowships (NWO, ARC, Japan) | [T2] |
| 2002–2016 | Stanford K. T. Li chair, courtesy EE | Large PhD cohorts (graduations 2007–2014), co-advising | DSDP5 (Matlab and C); CVX with Boyd | NSF, AFOSR, DOE, EPRI; Boeing, Huawei, American Express and others | [T2][T7] |
| 2017–2024 | Stanford plus Cardinal Operations (chief scientific adviser) and CUHK-SZ | Company and university teams in Shanghai and Shenzhen; students working as solver engineers (see 04) | COPT; Julia and C; GPUs from 2023 (A6000, H100) | Chinese industry demand for a domestic solver [T13] | [T12][T13][T21] |
| 2024–2026 | Emeritus; SJTU, SIMIS, CUHK-SZ, HKUST | 5–9 authors per paper; teams led by former students (Ge) | Multi-GPU (8×H100), Chinese GPUs | Industry traces (Huawei), grid operators ("CSG Market Clearing") [T21] | [T2][T21][T26] |

---

## 8. The last 12 months (October 2025 to September 2026)

All identifiers were checked in this run on arXiv abstract pages [T31], Crossref [T30] or the DBLP export [T29]. Dates are arXiv v1 dates or publication dates.

| Date | Item | Line | Tag |
|---|---|---|---|
| 2025-10-06 | OptPipe: pipeline parallelism for LLM training, arXiv 2510.05186 | M | [practice] (P) |
| 2025-10 | CV updated ("Updated October, 2025") [T2] | — | [practice] (P) |
| 2025-11-01 | "Accelerating Trust-Region Methods: An Attempt to Balance Global and Local Efficiency", arXiv 2511.00680 (v3 2026-07-07) | B | [practice] (P) |
| 2025-11-20 | PDHCG published, IJOC, 10.1287/ijoc.2024.0983; smart crossover also appears in IJOC in 2025 (10.1287/ijoc.2022.0291) | L, K | [practice] (P) |
| 2025-12-04 | Talk "Second-Order Tâtonnement for Market Equilibria: Methods, Complexity, and Extensions", Kyoto University [T4][T20] | E | [practice] (P) |
| 2026-01 | Universal trust region, JSC (10.1007/s10915-025-03154-y); HSODF, MP (10.1007/s10107-025-02230-3) | B | [practice] (P) |
| 2026-01-12 | D-PDLP, multi-GPU PDLP, arXiv 2601.07628 | L | [practice] (P) |
| 2026-01-25 | "A Universal Load Balancing Principle and Its Application to Large Language Model Serving", arXiv 2601.17855 | M | [practice] (P) |
| 2026-03-15 | Nonstationary online LP with polylog regret, arXiv 2603.14673 (with Glynn and Jaillet) | H | [practice] (P) |
| 2026-04 | Tarski fixed points and supermodular games, TCS, 10.1016/j.tcs.2026.115823 | E | [practice] (P) |
| 2026-04-27 | "Scalable First-Order Interior Point Trust Region Algorithms for Linearly Constrained Optimization", arXiv 2604.24488 | B | [practice] (P) |
| 2026-05 | HSODM published, MOR 51(2), 10.1287/moor.2023.0132 | B | [practice] (P) |
| 2026-05-07, 05-13, 05-27 | LLM-serving load balancing (arXiv 2605.06113); OSDN linear attention (2605.13473); OR-Space benchmark for optimization agents (2605.28158) | M | [practice] (P) |
| 2026-06-21, 06-28 | Geometry-aware LLM scheduling (arXiv 2606.22327); strategy iteration strongly polynomial for turn-based deterministic forward games (2606.29568) | M, F | [practice] (P) |
| 2026-07-02 | Plenary "Mathematical Programming in the Era of AI", HORIZONS 2026, Vietnam [T21] | L, M | [practice] (P) |
| 2026-07-04, 07-20 | Online LP for multi-objective LLM routing (arXiv 2607.03948); distributed rank-adaptive ALM for large SDPs (2607.17933) | H, L | [practice] (P) |
| 2026-08-10, 08-12, 08-27 | GPU conic QP (arXiv 2608.09159); Sinkhorn–Knopp local convergence (2608.11760); token-level advertising (2608.27382) | L, H | [practice] (P) |
| 2026-09 | Adaptive resolving methods for MDPs with function approximation, ORL (10.1016/j.orl.2026.107529; volume dated 2027-01) | F | [practice] (P) |
| 2026-09-14 | "SL(n) Representation Learning …", arXiv 2609.15083, with Mukuta and Harada (Tokyo). arXiv lists "Ye, Yinyu", but **identity not verified** | ? | [observed] (bibliographic) |
| 2026-09-23 | Note "Can Pure Offline Data Learning Replace Linear Programming Algorithms?" [T22] | A | [stated] (P) |

- [observed] (S) OpenAlex also attributes to "Yinyu Ye" medical-imaging papers in 2025–26: npj Digital Medicine 2026 (10.1038/s41746-026-02389-9), J. Am. Coll. Radiol. 2026 (10.1016/j.jacr.2026.07.009), Medical Image Analysis 2025 (10.1016/j.media.2025.103548). Crossref gives no affiliation for these [T30]. The CV lists one earlier medical-imaging paper with the same Shenzhen group (C82, MICCAI 2022, last author Dong Ni) [T2], so the attribution is plausible. **Not resolved.**
- [inferred] What is new in the last 12 months: (i) multi-GPU and distributed versions of every first-order solver; (ii) interior-point and trust-region ideas pushed onto first-order hardware (arXiv 2604.24488); (iii) LLM serving as the main new application of online LP; (iv) return to his strongly-polynomial MDP/game line; (v) a public position that offline learning cannot replace LP algorithms.

---

## 9. Implications for the skill

[inferred] These notes are for a skill that proposes ideas to improve a nonlinear solver. From the trajectory:

- Ideas "in Ye's manner" are likely to be reformulations: cast a solver sub-task as an LP, conic, complementarity or online-learning problem that has a complexity or regret guarantee. Examples in his record are the homogeneous self-dual embedding for infeasibility, crossover as a basis-identification problem, diagonal preconditioning as an SDP, step-size selection as online learning (arXiv 2505.23081 and 2509.11007), and a 2-D trust-region subproblem in place of a full Newton step.
- His recent nonlinear work covers unconstrained or linearly constrained second-order steps (DRSOM, HSODM, universal and accelerated trust region, first-order IP trust region), derivative-free constrained NLP (SOLNP+, TOMS 2024), and GPU first-order conic and QP methods. **General SQP, filter or merit globalization and KKT linear algebra for large sparse NLP are absent from his last-decade record.** The skill should say so rather than invent his views there.
- His typical first move on a popular method is to look for a counterexample or a missing convergence proof (ADMM 2014–16, the 2026 LP-learning note). A "Ye review" of a solver heuristic should start there.

---

## Contradictions

- **C1. Who was his PhD advisor?** CV: "Edison Tse (Advisor)", with Dantzig on the committee [T2]. MGP: Tse Advisor 1, Dantzig Advisor 2 [T23]. Wikipedia: PhD "under the supervision of George B. Dantzig" [T24]. His own speech and essay: Dantzig "was a great advisor" [T7] and "My first mentor was George Dantzig" [T9]. Kept as is.
- **C2. What was his time with Todd?** CV: "1987: Visiting Ph.D. Student of Michael Todd" and a 1993 visiting-scientist post at Cornell, with no postdoc listed [T2]. The 2020 essay: Todd "invited me to do postdoctoral work at Cornell" [T9]. The 1996 preface: "I also went to Cornell to work under the guidance of Prof. Michael Todd" [T10].
- **C3. Why he chose OR/LP: three stated versions.** 2017: AI cooled, "我比较喜欢数学" *tr. I liked mathematics better* [T12]. 2025: the Chinese-medicine expert system made him interested in quantification [T13]. 1996/2020: Karmarkar's 1984 seminar decided it [T10][T9]. The 1996 preface also mentions a prior research project with Luenberger. The 2025 interview says "我的导师" *tr. my advisor* assigned the expert-system task, without naming the advisor.
- **C4. His first reaction to Karmarkar.** 1996: "I was not particular enthusiastic about the statement from the speaker that a new interior-point method would be 40 times faster than the simplex method" [T10]. The 2020 essay omits the scepticism ("I became fascinated by linear programing") [T9]. His 2021–26 decks lead with multiplicative speed-up claims, e.g. "3.5x faster on average in the past 4 years" [T21].
- **C5. Who named DRO?** Homepage: "where we created the name DRO first time" [T1]. The title "On Distributionally Robust Chance-Constrained Linear Programs" (Calafiore & El Ghaoui, JOTA, published 2006-12-11, 10.1007/s10957-006-9084-x) predates Delage & Ye (OR 2010; the CV's Nicholson prize for it is 2008) [T30][T2]. Not reconciled. Earlier working-paper dates of Delage–Ye were not checked.
- **C6. His current titles.** CV: "2024.4-present: Distinguished Professor of the Antai School of Management, Shanghai Jiao Tong University" [T2]. CUHK-SZ profile: "a Fractional Professor at the Institute of Intelligent Computing of Shanghai Jiao Tong University" [T28]. 2025 bio: "now the Visiting Professor of Shanghai Jiao Tong University" [T3]. 2025 interview headline: "斯坦福大学终身教授" *tr. Stanford tenured professor*, while the homepage says "Emeritus" [T13][T1].
- **C7. Student records.** CV versus MGP: Benson 1999 vs 1998; Bosch 1994 vs 1993; "Pi-Fang Huang 1995" vs "Hung, Pi-Fang 1994"; Ding 2013 vs 2012; "Tiago Akle 2014*" vs "Serrano, Santiago 2015". MGP lists Zhaonan Qu (2024), and the CV does not. The CV lists "Zhishu Zhu 2010" and "Zhisu Zhu 2017" [T2][T23].
- **C8. Universal versus customized algorithms.** In 2017 he gives up the "万能的算法" *tr. universal algorithm* for customized methods [T12]. Since 2019 he leads a general-purpose solver (COPT) [T1][T21]. In 2026 he argues that general LP algorithms cannot be replaced by learning from similar instances [T22].
- **C9. Priority on nonconvex second-order complexity.** 2022 slide: "Trust-region with the fixed-radius strategy, O(ε^−3/2), see the lecture notes by Ye† since 2005" [T15]. The published record has no Ye paper with that result before DRSOM. The same slide cites Nesterov–Polyak (2006) and Cartis–Gould–Toint (2011) for O(ε^−3/2). The lecture notes were not found.
- **C10. Where COPT was built.** NJU 2024 report: "他的团队在斯坦福自主研发的COPT求解器" *tr. the COPT solver his team developed independently at Stanford* [T27]. The 2025 interview has Chinese companies approaching him and his students because of external restrictions [T13]. The 2026 slide places LEAVES (2017) and COPT (2019) under "Our team" alongside Cardinal Operations, Huawei, CAS and Alibaba [T21].
- **C11. How big the output is.** 2020 essay: "more than 170 peer-reviewed papers" [T9]. CV 2025: J1–J207 and C1–C95, with some duplicates [T2]. DBLP: 327 records [T29]. OpenAlex: 504 works, probably including namesakes [T32].
- **C12. Press framing versus the theorem.** The 2015 MS&E news says he "proved that two algorithms … are, indeed, the fastest and most accurate ways to solve specific types of complicated optimization problems" [T11]. The paper's title claims strong polynomiality "for the Markov Decision Problem with a Fixed Discount Rate" (MOR 2011) [T30]. The press version is broader than the theorem.

---

## Gaps

- **His stated reason for taking the SJTU post (2024) and for leaving the Stanford chair in 2024** was not found. The SIMIS profile page returned HTTP 403 to WebFetch and gave an empty shell to curl [T33].
- **Stated reasons for entering sensor localization (2004), market equilibria (2005), DRO (2008) and ADMM (2014)** were not found in his own words. The triggers in §3 for these lines are dated co-occurrences (grants, partners, prior papers), not his statements.
- **Talk recordings not watched or transcribed**: the Stanford Zoom recording of "Recent Computational Progress on LP Solvers" (2024-02-14) linked from [T4], and the SJTU 大师讲坛 video mentioned in [T26]. Neither offered downloadable subtitles, so nothing was saved to `sources/talks/`.
- **The celebration talks** (Todd, "Yinyu Ye's Research on Interior-point Methods"; Ge, "The Development History of COPT"; Z. Wang) survive only as abstracts [T25]. These are the most likely third-party accounts of his turns, and I did not find their slides.
- **The "lecture notes by Ye since 2005"** on fixed-radius trust region (C9): not located.
- **Identity of "Yinyu Ye"** on the 2025–26 medical-imaging papers and on arXiv 2609.15083: not resolved.
- **External confirmation** of the 2025 Carathéodory Prize and of the NVIDIA cuOpt lineage claim: not found. Both rest on his own CV and slides.
- **Wikipedia's "co-founder of minMax Optimization Inc."** [T24] does not appear in the CV. Not verified.
- **Referee reports and rejections**: none public. Whether DRSOM was ever submitted to a journal is unknown.
- **Google Scholar**: not tried in this run. Agent 01 reports a CAPTCHA redirect, and DBLP's HTML/XML endpoints now show a bot check, so only SPARQL worked [T29].
- **Full texts**: I read no proof or full paper for this dimension. In particular, whether Halperin–Zwick's ratio is 0.701, and whether it was later improved, is not checked.

---

## Sources

Primary (Ye's own material and dated records)

- T1. Yinyu Ye, homepage, https://web.stanford.edu/~yyye/ (accessed 2026-09-28), with sub-pages family.html, other.html and Col.html (Computational Optimization Laboratory software). (P)
- T2. Yinyu Ye, Curriculum Vitae, "Updated October, 2025", https://web.stanford.edu/~yyye/cvYYYE25.pdf. (P)
- T3. Yinyu Ye, very short bio 2025 (English and Chinese), https://web.stanford.edu/~yyye/VeryShortbio2025.pdf. (P)
- T4. Yinyu Ye, talks index, https://web.stanford.edu/~yyye/talks.html (accessed 2026-09-28). (P)
- T5. Yinyu Ye, recent papers page, https://web.stanford.edu/~yyye/newpapers.html (accessed 2026-09-28). (P)
- T7. Yinyu Ye, speech on receiving the John von Neumann Theory Prize, 2009-10-11, https://web.stanford.edu/~yyye/Yinyu-accept-speech.pdf, and the Chinese version, https://web.stanford.edu/~yyye/yinyu-speech-Chinese.pdf. (P)
- T8. Yinyu Ye, "My Academic, Sport, and Life as a Whole", slides, 2023 (PDF created 2023-07-06), https://web.stanford.edu/~yyye/MyacademicSportlife.pdf. (P)
- T9. Stanford Engineering, "Yinyu Ye: Sports led me from the rice fields to Stanford", first-person essay, 2020-12-08, https://engineering.stanford.edu/news/yinyu-ye-sports-led-me-rice-fields-stanford. (P, institution-edited)
- T10. Yinyu Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley, 1997, DOI 10.1002/9781118032701. Preface ("Iowa City, 1996") and table of contents, read from https://web.stanford.edu/~yyye/main.ps. (P)
- T12. 雷锋网 (Leiphone), "运筹学教授叶荫宇：作为 AI 基石，优化算法如何在实际中应用？", 2017-06-27, edited transcript of Ye's talk at the 2017 AI 大师论坛, https://www.leiphone.com/category/industrynews/DwILBnyYJPMfv7WX.html. (P, edited transcript)
- T13. 中新社 (China News Service), "东西问丨叶荫宇：AI与OR，共促人类未来", 2025-03-06, https://www.chinanews.com/gn/2025/03-06/10378972.shtml. (P, edited interview)
- T14. Yinyu Ye, "From 0.618 to Mathematical Optimization", slides (PDF created 2021-06-15), https://web.stanford.edu/~yyye/618Slides.pdf. (P)
- T15. Yinyu Ye, "DRSOM: A Dimension-Reduced Second-Order Method for Nonconvex Optimization", slides, HK PolyU, 2022-09-19 (PDF created 2022-09-23, author "Yinyu Ye"), https://web.stanford.edu/~yyye/DRSOM-220916-v3.pdf. (P)
- T16. Yinyu Ye, "Online Linear Programming: Applications and Extensions", ISMP 2022 plenary slides (PDF created 2022-08-15), https://web.stanford.edu/~yyye/ISMP2022.pdf. (P)
- T17. Yinyu Ye, "Open Questions on the Markov Decision/Game Process", Simons Institute, 2023-11-29, https://web.stanford.edu/~yyye/MDPopenqs.pdf. (P; used only for the date and scope of the MDP line)
- T19. Yinyu Ye, "Mathematical Optimization in the Era of AI", INFORMS International 2025, Singapore (PDF created 2025-07-20, author metadata "xcy27"), https://web.stanford.edu/~yyye/MPinEraofAI20250720.pdf. (P, team-prepared)
- T20. Yinyu Ye with C. Zhang, C. He and B. Jiang, "Second-Order Tâtonnement for Market Equilibria: Methods, Complexity, and Extensions", Kyoto University, 2025-12-04, https://web.stanford.edu/~yyye/KyotoIMU2025.pdf. (P)
- T21. Yinyu Ye, "Mathematical Programming in the Era of AI", HORIZONS 2026, CEI VinUni, 2026-07-02 (PDF author metadata "Dongdong Ge"), https://web.stanford.edu/~yyye/20260701Solver.pdf. (P, team-prepared)
- T22. Yinyu Ye, "Can Pure Offline Data Learning Replace Linear Programming Algorithms?", note dated 2026-09-23, https://web.stanford.edu/~yyye/LPsolutionsensitivity.pdf. (P)
- T29. DBLP SPARQL export for pid 42/1372-1 (327 records, including the 2025–26 records with DOIs), https://sparql.dblp.org/sparql, queried 2026-09-28. (P, bibliographic)
- T30. Crossref REST API records (api.crossref.org), checked 2026-09-28 for every DOI named in this file. (P, bibliographic)
- T31. arXiv abstract pages (arxiv.org/abs/…), checked 2026-09-28 for every arXiv id named in this file, including version histories and comments. (P, bibliographic)

Secondary

- T11. Stanford MS&E News, "Professor Yinyu Ye Awarded Optimization Prize: Proves Efficiency of Popular Markov Decision Process Algorithms", 2015-01-29, https://msande.stanford.edu/news/professor-yinyu-ye-awarded-optimization-prize-proves-efficiency-popular-markov-decision. (S, with direct quotes)
- T23. Mathematics Genealogy Project: Yinyu Ye id 12397, Edison Tse id 54272, George Dantzig id 32292, https://www.mathgenealogy.org/id.php?id=12397 (accessed 2026-09-28). (S)
- T24. Wikipedia, "Yinyu Ye" (raw wikitext), https://en.wikipedia.org/wiki/Yinyu_Ye (accessed 2026-09-28). (S)
- T25. "Yinyu Ye Retirement Celebration, July 28-29, 2024, Stanford", programme and abstracts, https://quyanlin.github.io/ye/event.html. (S)
- T26. 上海交通大学研究生院, "斯坦福大学李国鼎讲席教授叶荫宇做客第218期大师讲坛", 2024-04-28, https://www.gs.sjtu.edu.cn/post/detail/Z3MyMDMz. (S)
- T27. 南京大学工程管理学院, "《我的学术、体育以及人生发展》——叶荫宇教授赴仙林校区与我院本科生开展交流", 2024-04-18, https://sme.nju.edu.cn/5f/15/c2039a679701/pagem.htm. (S)
- T28. CUHK-Shenzhen School of Data Science, faculty profile "YE, Yinyu, Professor (Fractional)", https://sds.cuhk.edu.cn/en/teacher/1750 (accessed 2026-09-28). (S)
- T32. OpenAlex author A5041526408, via `references/sources/publications/publications.md` (generated 2026-09-28). (S)
- T33. SIMIS profile, https://www.simis.cn/yinyu-ye/: HTTP 403 via WebFetch, empty shell via curl. Found through the one WebSearch call. (failed)

Papers named in this file (identifier checked in T30 or T31; Ye's own unless marked)

- Karmarkar, "A new polynomial-time algorithm for linear programming", Combinatorica, 1984, 10.1007/BF02579150 (not Ye's)
- Ye & Kojima, "Recovering optimal dual solutions in Karmarkar's polynomial algorithm for linear programming", MP, 1987, 10.1007/BF02592079
- Ye, "An Extension of Karmarkar's Algorithm and the Trust Region Method for Quadratic Programming", Progress in Mathematical Programming, 1989, 10.1007/978-1-4613-9617-8_3
- Ye & Tse, "An extension of Karmarkar's projective algorithm for convex quadratic programming", MP, 1989, 10.1007/BF01587086
- Ye, "A Class of Projective Transformations for Linear Programming", SIAM J. Comput., 1990, 10.1137/0219030
- Todd & Ye, "A Centered Projective Algorithm for Linear Programming", MOR, 1990, 10.1287/moor.15.3.508
- Ye, "An O(n³L) potential reduction algorithm for linear programming", MP, 1991, 10.1007/BF01594937
- Ye, "A Potential Reduction Algorithm Allowing Column Generation", SIOPT, 1992, 10.1137/0802002
- Ye, "On affine scaling algorithms for nonconvex quadratic programming", MP, 1992, 10.1007/BF01580903
- Mizuno, Todd & Ye, "On Adaptive-Step Primal-Dual Interior-Point Algorithms for Linear Programming", MOR, 1993, 10.1287/moor.18.4.964
- Ye, Güler, Tapia & Zhang, "A quadratically convergent O(√n L)-iteration algorithm for linear programming", MP, 1993, 10.1007/BF01581242
- Ye, Todd & Mizuno, "An O(√nL)-Iteration Homogeneous and Self-Dual Linear Programming Algorithm", MOR, 1994, 10.1287/moor.19.1.53
- Goemans & Williamson, "Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming", JACM, 1995, 10.1145/227683.227684 (not Ye's)
- Ye, "On the complexity of approximating a KKT point of quadratic programming", MP, 1998, 10.1007/BF01581726
- Nesterov, Todd & Ye, "Infeasible-start primal-dual methods and infeasibility detectors for nonlinear programming problems", MP, 1999, 10.1007/s10107980009a
- Benson, Ye & Zhang, "Solving Large-Scale Sparse Semidefinite Programs for Combinatorial Optimization", SIOPT, 2000, 10.1137/S1052623497328008
- Ye, "A .699-approximation algorithm for Max-Bisection", MP, 2001, 10.1007/pl00011415
- Halperin & Zwick, "A unified framework for obtaining improved approximation algorithms for maximum graph bisection problems", Random Structures & Algorithms, 2002, 10.1002/rsa.10035 (not Ye's)
- Ye & Zhang, "New Results on Quadratic Minimization", SIOPT, 2003, 10.1137/S105262340139001X
- Biswas & Ye, "Semidefinite programming for ad hoc wireless sensor network localization", IPSN, 2004, 10.1145/984622.984630
- Ye, "A New Complexity Result on Solving the Markov Decision Problem", MOR, 2005, 10.1287/moor.1050.0149
- Ye, "Computing the Arrow-Debreu Competitive Market Equilibrium and Its Extensions", LNCS, 2005, 10.1007/11496199_2
- Grant, Boyd & Ye, "Disciplined Convex Programming", Nonconvex Optimization and Its Applications, 2006, 10.1007/0-387-30528-9_7
- Calafiore & El Ghaoui, "On Distributionally Robust Chance-Constrained Linear Programs", JOTA, 2006, 10.1007/s10957-006-9084-x (not Ye's)
- So & Ye, "Theory of semidefinite programming for Sensor Network Localization", MP, 2007, 10.1007/s10107-006-0040-1
- Ye, "A path to the Arrow–Debreu competitive market equilibrium", MP, 2007/2008, 10.1007/s10107-006-0065-5
- Benson & Ye, "Algorithm 875: DSDP5", ACM TOMS, 2008, 10.1145/1356052.1356057
- Devanur & Hayes, "The adwords problem", ACM EC, 2009, 10.1145/1566374.1566384 (not Ye's)
- Agrawal, Wang & Ye, "A Dynamic Near-Optimal Algorithm for Online Linear Programming", arXiv 0911.2974 (2009); OR, 2014, 10.1287/opre.2014.1289
- Delage & Ye, "Distributionally Robust Optimization Under Moment Uncertainty with Application to Data-Driven Problems", OR, 2010, 10.1287/opre.1090.0741
- Luo, Ma, So, Ye & Zhang, "Semidefinite Relaxation of Quadratic Optimization Problems", IEEE SPM, 2010, 10.1109/msp.2010.936019
- Boyd, Parikh, Chu, Peleato & Eckstein, "Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers", FnT ML, 2011, 10.1561/2200000016 (not Ye's)
- Ye, "The Simplex and Policy-Iteration Methods Are Strongly Polynomial for the Markov Decision Problem with a Fixed Discount Rate", MOR, 2011, 10.1287/moor.1110.0516
- Chen, Xu & Ye, "Lower Bound Theory of Nonzero Entries in Solutions of ℓ2-ℓp Minimization", SISC, 2010, 10.1137/090761471
- Ge, Jiang & Ye, "A note on the complexity of Lp minimization", MP, 2011, 10.1007/s10107-011-0470-2
- Ji, Sze, Zhou, So & Ye, "Beyond convex relaxation: A polynomial-time non-convex optimization approach to network localization", IEEE INFOCOM, 2013, 10.1109/INFCOM.2013.6567056
- Bian, Chen & Ye, "Complexity analysis of interior point algorithms for non-Lipschitz and nonconvex minimization", MP, 2015, 10.1007/s10107-014-0753-5
- Post & Ye, "The Simplex Method is Strongly Polynomial for Deterministic Markov Decision Processes", MOR, 2015, 10.1287/moor.2014.0699
- Chen, He, Ye & Yuan, "The direct extension of ADMM for multi-block convex minimization problems is not necessarily convergent", MP, 2016, 10.1007/s10107-014-0826-5
- Hinder & Ye, "A one-phase interior point method for nonconvex optimization", arXiv 1801.03072 (2018)
- Sidford, Wang, Wu, Yang & Ye, "Near-Optimal Time and Sample Complexities for Solving Discounted Markov Decision Process with a Generative Model", arXiv 1806.01492 (NeurIPS 2018)
- Haeser, Liu & Ye, "Optimality condition and complexity analysis for linearly-constrained optimization without differentiability on the boundary", MP, 2019, 10.1007/s10107-018-1290-4
- Sun, Luo & Ye, "On the Efficiency of Random Permutation for ADMM and Coordinate Descent", MOR, 2020, 10.1287/moor.2019.0990
- Sun & Ye, "Worst-case complexity of cyclic coordinate descent: O(n²) gap with randomized version", MP, 2021, 10.1007/s10107-019-01437-5
- Applegate et al., "Practical Large-Scale Linear Programming using Primal-Dual Hybrid Gradient", arXiv 2106.04756 (2021) (not Ye's; Hinder is a co-author)
- Li & Ye, "Online Linear Programming: Dual Convergence, New Algorithms, and Regret Bounds", OR, 2022, 10.1287/opre.2021.2164
- Zhang, Ge, He, Jiang, Jiang & Ye, "DRSOM: A Dimension Reduced Second-Order Method", arXiv 2208.00208 (2022)
- Ge, Huangfu, Wang, Wu & Ye, "Cardinal Optimizer (COPT) User Guide", arXiv 2208.14314 (2022)
- Zhang et al., "A homogeneous second-order descent method for nonconvex optimization", arXiv 2211.08212; MOR, 2026, 10.1287/moor.2023.0132
- Jalota, Pavone, Qi & Ye, "Fisher markets with linear constraints: Equilibrium properties and efficient distributed algorithms", GEB, 2023, 10.1016/j.geb.2023.06.007
- Jiang, He, Zhang, Ge, Jiang & Ye, "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", arXiv 2311.11489; JSC, 2026, 10.1007/s10915-025-03154-y
- Lu & Yang, "cuPDLP.jl: A GPU Implementation of Restarted Primal-Dual Hybrid Gradient for Linear Programming in Julia", arXiv 2311.12180 (2023) (not Ye's)
- Lu et al., "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv 2312.14832 (2023)
- Jiang & Ye, "Achieving Instance-dependent Sample Complexity for Constrained Markov Decision Process", arXiv 2402.16324 (2024)
- Tang, Toh, Xiao & Ye, "A Riemannian Dimension-Reduced Second-Order Method with Application in Sensor Network Localization", SISC, 2024, 10.1137/23M1567229
- Zhang et al., "Adam-mini: Use Fewer Learning Rates To Gain More", arXiv 2406.16793 (2024; ICLR 2025)
- Han et al., "Accelerating Low-Rank Factorization-Based Semidefinite Programming Algorithms on GPU", arXiv 2407.15049 (2024)
- Hinder & Ye, "Worst-Case Iteration Bounds for Log Barrier Methods on Problems with Nonconvex Constraints", MOR, 2024, 10.1287/moor.2020.0274
- Ge, Liu, Liu, Tan & Ye, "Algorithm 1053: SOLNP+", ACM TOMS, 2024, 10.1145/3699956
- Gao, Ge & Ye, "Algorithm 1055: HDSDP", ACM TOMS, 2025, 10.1145/3721123
- Deng et al., "An Enhanced ADMM-Based Interior Point Method for Linear and Conic Optimization", IJOC, 2025, 10.1287/ijoc.2023.0017
- Ge, Wang, Xiong & Ye, "From an Interior Point to a Corner Point: Smart Crossover", IJOC, 2025, 10.1287/ijoc.2022.0291
- Jalota & Ye, "Stochastic Online Fisher Markets: Static Pricing Limits and Adaptive Enhancements", OR, 2025, 10.1287/opre.2023.0636
- Nguyen et al., "Robustifying Conditional Portfolio Decisions via Optimal Transport", OR, 2025, 10.1287/opre.2021.0243 (via DBLP)
- Huang, Zhang, Li, Ge, Liu & Ye, "A Restarted Primal-Dual Hybrid Conjugate Gradient Method for Large-Scale Quadratic Programming", IJOC, 2025, 10.1287/ijoc.2024.0983
- Lin, Xiong, Ge & Ye, "A Practical GPU-Enhanced Matrix-Free Primal-Dual Method for Large-Scale Conic Programs" (PDCS), arXiv 2505.00311 (2025)
- Chen, Xia, Shao, Ge & Ye, "Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling", arXiv 2505.11792 (NeurIPS 2025)
- Gao, Chu, Ye & Udell, "Gradient Methods with Online Scaling Part I. Theoretical Foundations", arXiv 2505.23081 (2025); Chu, Gao, Ye & Udell, "… Part II. Practical Aspects", arXiv 2509.11007 (2025)
- Zhang, He, Jiang & Ye, "The Second-Order Tâtonnement: Decentralized Interior-Point Methods for Market Equilibrium", arXiv 2508.04822 (2025)
- Wang, Ye & Zhou, "LLM Serving Optimization with Variable Prefill and Decode Lengths", arXiv 2508.06133 (2025); Chen, Ye & Zhou, "Adaptively Robust LLM Inference Optimization under Prediction Uncertainty", arXiv 2508.14544 (2025)
- Li, Zhang, Liu, Ge & Ye, "OptPipe: Memory- and Scheduling-Optimized Pipeline Parallelism for LLM Training", arXiv 2510.05186 (2025)
- Jiang, Zhang, Jiang & Ye, "Accelerating Trust-Region Methods: An Attempt to Balance Global and Local Efficiency", arXiv 2511.00680 (2025)
- He, Jiang, Zhang, Ge, Jiang & Ye, "Homogeneous second-order descent framework: a fast alternative to Newton-type methods", MP, 2026, 10.1007/s10107-025-02230-3
- Li, Huang, Liu, Ge & Ye, "D-PDLP: Scaling PDLP to Distributed Multi-GPU Systems", arXiv 2601.07628 (2026)
- Chen, Bu, Song, Lu, Ye & Zhou, "A Universal Load Balancing Principle and Its Application to Large Language Model Serving", arXiv 2601.17855 (2026)
- Xu, Shen, Glynn, Ye & Jaillet, "A Single-Sample Polylogarithmic Regret Bound for Nonstationary Online Linear Programming", arXiv 2603.14673 (2026)
- Dang, Qi & Ye, "Computations and complexities of Tarski's fixed points and supermodular games", TCS, 2026, 10.1016/j.tcs.2026.115823
- Su, Zhang, Huang, Li & Ye, "Scalable First-Order Interior Point Trust Region Algorithms for Linearly Constrained Optimization", arXiv 2604.24488 (2026)
- Bu et al., "Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale", arXiv 2605.06113 (2026); Zhou et al., "OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention", arXiv 2605.13473 (2026); Zhou, Lu, Zhao, Lin, Ge & Ye, "OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents", arXiv 2605.28158 (2026)
- Kong, Qi, Ye & Zhou, "Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice", arXiv 2606.22327 (2026); Mei, Sun & Ye, "The Simple Strategy-Iteration Method is Strongly Polynomial for the Turn-Based Deterministic Forward Game", arXiv 2606.29568 (2026)
- Chen, Ye & Zhou, "Online Linear Programming for Multi-Objective Routing in LLM Serving", arXiv 2607.03948 (2026); Li, Liu, Ge & Ye, "A Curvature-Aware Rank-Adaptive Distributed Augmented-Lagrangian Solver for Large-Scale SDPs", arXiv 2607.17933 (2026)
- Li, Huang, Liu, Ge & Ye, "GPU-Accelerated Conic Quadratic Programming with Local Linear Convergence under Strict Complementarity", arXiv 2608.09159 (2026); Gao, Qu, Ye & Udell, "Tight Nonasymptotic Local Convergence of Sinkhorn-Knopp", arXiv 2608.11760 (2026); Liu, Zhang, Yu, Ye & Qi, "Token-Level Advertising", arXiv 2608.27382 (2026)
- Jiang, Ye & Zong, "Adaptive resolving methods for Markov decision processes with function approximations", ORL, 2026 (vol. dated 2027), 10.1016/j.orl.2026.107529
- Corrections: Burer & Ye, MP, 2021, 10.1007/s10107-021-01684-5; Dang & Ye, TCS, 2020, 10.1016/j.tcs.2019.03.014
- Identity unverified: Li, Mukuta, Yang, Ye & Harada, "SL(n) Representation Learning …", arXiv 2609.15083 (2026); medical-imaging papers 10.1038/s41746-026-02389-9, 10.1016/j.jacr.2026.07.009, 10.1016/j.media.2025.103548
