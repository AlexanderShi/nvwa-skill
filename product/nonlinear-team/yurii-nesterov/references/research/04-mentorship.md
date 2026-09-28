# 04 · Students and collaborators: how Yurii Nesterov supervises and works with others

| | |
|---|---|
| Researcher | Yurii Nesterov (CORE / INMA, UCLouvain, emeritus; b. 1956) |
| Dimension | Agent 04 of 06: students and collaborators. Covers supervision style, group habits, lab culture and tacit knowledge, following `references/research-extraction-framework.md` §二 (agent 4) and §八 |
| Research date | 2026-09-28 |
| Sources consulted | 33. 26 were read in full or in part and are used here. 7 are metadata-only or were read and turned out to hold nothing on mentorship. All are listed under "Sources". About 12 more were identified but could not be reached (see Gaps) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}` held only placeholders. Nothing under `private/` was opened |

**Tags.**
- [stated]: Nesterov's own words about students, teaching or collaboration.
- [practice]: what records show. These are thesis title pages, institutional thesis lists, CVs, funding lines, co-author data and code locations.
- [observed]: what students, postdocs or colleagues say about him.
- [inferred]: my reading, not anyone's words.

**Source type.** **P** marks a primary record or his own words. **S** marks a secondary source. Everything a student or colleague says *about* Nesterov is marked secondary (S), even when it comes from that person's own thesis or homepage.

**Quotes.** Quotes are verbatim from files I opened with a tool in this run. Line breaks and hyphenation from the PDF extraction are removed, and PDF ligature glyphs (ﬁ, ﬂ) are written as plain letters. Anything outside quotation marks is a paraphrase.

**Overlap.** Notes 01 to 03 are already in this folder.
- 01 (publications) handed the student list to this note (01 §2.2, "to be verified by agent 04").
- 03 (process evidence) already covers who wrote the code and ran the experiments in the joint papers (03 §1.2). Here I only point to it.

**Shape of the evidence.** No student has written a blog post, memoir, "working with Yurii" piece or lab guide that I could find. There is no Festschrift essay with personal recollections either: the 2026 special issue has a two-page editorial only. The first-hand student voice comes from two thesis acknowledgements: Traag 2013, co-supervised with Van Dooren, and Doikov 2021, sole supervisor. It is supported by three kinds of record:
- the UCLouvain CORE list of defended theses;
- homepages and CVs of former students and postdocs;
- funding lines, acknowledgements and co-author data in the joint papers.

The acknowledgements of Rodomanov (2022) and Devolder (2013/2015) would add most to this note. Neither was readable: the UCLouvain DIAL repository reset every connection (see Gaps). What students all know but papers never say therefore rests on very little evidence. Section 5 marks each such item with its source and a confidence level.

---

## 1. The supervision record: who, when, with whom

### 1.1 Doctoral students

| Student | Defence | Thesis (as listed) | Supervisors | First position after PhD (as listed) | Evidence | Tag |
|---|---|---|---|---|---|---|
| Yvan Hachez | 19 May 2003 | "Convex optimization over non-negative polynomials: structured algorithms and applications" | "Yurii Nesterov and Paul Van Dooren" | "ENGIE, Brussels, Belgium" | [M3] CORE thesis list | [practice] P |
| Ruslan Sadykov | 26 June 2006 | "Integer programming-based decomposition approaches for solving machine scheduling problem" | "Yurii Nesterov and Laurence Wolsey" | "Institut de Mathématique de Bordeaux, France" | [M3] | [practice] P |
| Michel Baes | 22 Sept 2006 | "Specral [sic] functions and smoothing techniques on Jordan algebras" | "Yurii Nesterov and Paul Van Dooren" | "Universität Zürich, Austria" [sic] | [M3] | [practice] P |
| Vania Dos Santos Eleuterio | 2009, ETH Zürich | not found | not found | not found | [M4] Math Genealogy only. The thesis was **not read** and could not be located | [observed] S |
| Olivier Devolder | 2013 per [M4]; "August 31, 2015" per [M3] (see Contradictions) | "Exactness, inexactness and stochasticity in first-order method [sic] large-scale convex optimizaiton [sic]" | "François Glineur and Yurii Nesterov" | "Head of Energy Group, N-Side, Louvain-la-Neuve, Belgium" | [M3], [M4] | [practice] P |
| Vincent A. Traag | 2 Sept (2013), UCLouvain, "Docteur en Sciences appliquées" | "Algorithms and Dynamical Models for Communities and Reputation in Social Networks" | "my advisors Paul Van Dooren and Yurii Nesterov" | not stated in the sources read | [M2] thesis title page and acknowledgements; [M4] | [practice] P |
| Nikita Doikov | 20 Sept 2021 | "New second-order and tensor methods in Convex Optimization" | "Yurii Nesterov" (sole) | postdoc with Nesterov, UCLouvain, 09.2021–08.2022; then EPFL (Jaggi) 09.2022–12.2025; Cornell ORIE assistant professor from 01.2026 | [M1] title page; [M3]; [M5] homepage; [M6] CV | [practice] P |
| Anton Rodomanov | 23 Aug 2022 | "Quasi-Newton Methods with Provable Efficiency Guarantees" | "Yurii Nesterov" (sole) | postdoc, ICTEAM UCLouvain, 01/09/2022–31/08/2023; then CISPA (Stich) from 01/09/2023 | [M3]; [M8] homepage; [M9] CV ("Doctoral Candidate … 23/01/2019 – 31/08/2022") | [practice] P |

Counting the table gives 8 distinct doctoral students found. His own Academia Europaea CV (July 2021, read by agent 02) says "Five Ph.D.-students (5 defended)". See Contradictions.

**Pattern A: two eras of supervision.** [practice] P for the record; the reading of it is [inferred]
- **2003–2015: co-supervision.**
  - Every student in this period had a second supervisor: Van Dooren three times, Wolsey once, Glineur once.
  - Some topics lie in neighbouring fields: integer-programming decomposition for scheduling (Sadykov), community detection and social balance (Traag). Others are close to his own program: structured convex optimization over non-negative polynomials (Hachez), smoothing on Jordan algebras (Baes), inexact first-order methods (Devolder).
  - Joint papers are three- to five-author papers with the co-supervisor [M28]:

    | Student | Joint papers with Nesterov |
    |---|---|
    | Hachez | 2 |
    | Baes | 1 |
    | Devolder | 2 (both with Glineur) |
    | Traag | 3 (all with Van Dooren) |
    | Sadykov | 0 in DBLP |

  - First jobs are split between industry (ENGIE, N-Side) and academia (Bordeaux, Zürich).
- **2019–2022: sole supervision inside his own funded program.**
  - Doikov and Rodomanov work squarely on his current line: second-order, tensor and quasi-Newton complexity.
  - They write two-author papers with him. All 6 papers of Doikov's thesis are "Nikita Doikov and Yurii Nesterov" [M1]. All 5 DBLP records of Rodomanov with Nesterov are two-author [M28].
  - Both stay a year as his postdoc, then move to machine-learning-optimization groups: Jaggi at EPFL, Stich at CISPA. Stich was himself Nesterov's postdoc in 2014–2016 [M10].

### 1.2 Postdocs, hosted researchers and team members (as far as verified)

| Person | Relation, as the source states it | Source | Joint papers with Nesterov [M28] | Tag |
|---|---|---|---|---|
| Peter Richtárik | "Postdoctoral Fellow, CORE , Louvain-la-Neuve, Belgium, 2007–2009, host: Yurii Nesterov" | [M11] | 1 in 2010 (4 authors), 1 in 2020 (4 authors) | [practice] P |
| Sebastian U. Stich | "2014–2016 SNSF Postdoctoral Fellow, UCLouvain Hosts: Yurii Nesterov and François Glineur." | [M10] | 1, two-author ("Nesterov, Stich", SIAM J. Optim. 27 (2017) 110–123, DOI 10.1137/16M1060182) | [practice] P |
| Nikita Doikov | "Postdoctoral Researcher at UCLouvain, Belgium ICTEAM / CORE, hosted by Yurii Nesterov 09.2021 – 08.2022" | [M6] | 12 DBLP records 2020–2024, 8 of them two-author; arXiv 2511.07341 (2025, two-author) | [practice] P |
| Anton Rodomanov | "Postdoctoral Researcher ICTEAM Institute at UCLouvain. 01/09/2022 – 31/08/2023" and "working with Yurii Nesterov" | [M8], [M9] | 5, all two-author; plus the preprint "Y. Nesterov and A. Rodomanov", 2023, listed in [M9] | [practice] P |
| Geovani Grapiglia, Mihai Florea, Evgeniya Vorontsova, Masoud Ahookhosh, Valentin Leplat | Named by Doikov as "my colleagues from UCLouvain" during his PhD. Their formal roles are **not verified** | [M1] acknowledgements | Grapiglia 6 (all two-author, 2017–2023); Florea 2 (two-author, 2022, 2025); Ahookhosh 1 paper plus its correction (2024); Leplat 1 (4 authors, 2023); Vorontsova 0 | [observed] S for the relation, [practice] P for the counts |
| Filip Hanzely (visitor) | "Filip Hanzely is visiting Yurii Nesterov and his team at the Center for Operations Research and Econometrics , UCLouvain" (11 Nov 2019) | [M12] | "Stochastic Subspace Cubic Newton Method", ICML 2020 / arXiv 2002.09526 (Hanzely, Doikov, Richtárik, Nesterov) | [observed] S |

**Pattern B: small pairs, not a lab.** [practice] P / [inferred]
- The joint work of the 2017–2025 period is overwhelmingly two-author, "junior person + Nesterov": Grapiglia 6/6, Rodomanov 5/5, Shikhman 4/5, Doikov 8/12, Florea 2/2, Stich 1/1 [M28]. DBLP counts include a few duplicate arXiv/proceedings entries, for example SSCN and the super-universal paper twice each.
- Larger author lists arise when the junior person brings in their own network. Examples: the SSCN paper grew out of Doikov's KAUST visit (see 3.3); Doikov, Mishchenko and Nesterov (SIAM J. Optim. 34 (2024) 27–56, DOI 10.1137/22M1519444).
- This fits his stated view that a paper "normally" has "two or three authors" (see §4) [inferred].
- The 2026 editorial speaks of "more than 80 different coauthors" [M14]. So the pairs are many, but each is small.

---

## 2. Supervision style: what students and hosts report

| # | Finding | Evidence (verbatim) | Source | Tag |
|---|---|---|---|---|
| S1 | **In the sole-supervision era the supervisor sets the problem, sized so that it can be won.** | "He formulated a very interesting research question that I was able to work on with a visible hope to succeed and excited by the challenge." | Doikov, thesis acknowledgements, p. iii [M1], 2021 | [observed] S (according to Doikov) |
| S2 | **Hands-on help throughout.** | "His generous and thorough help at all stages of the work has been both very educational and kind to me." | [M1] p. iii | [observed] S (according to Doikov) |
| S3 | **Teaching by example: students learn by watching him do research.** | "It has been extreme luck and great honor to be supervised by Yurii Nesterov, who gave me a unique opportunity to observe an excellent example of how a high level research must be performed." | [M1] p. iii | [observed] S (according to Doikov) |
| S4 | **In the co-supervision era, leeway to follow one's own interest.** | "The leeway they allowed me to pursue my own interest is much appreciated." ("they" = Van Dooren and Nesterov) | Traag, thesis acknowledgements [M2], 2013 | [observed] S (according to Traag). This covers both advisors, so it cannot be attributed to Nesterov alone |
| S5 | **Speed in mathematics that students notice.** | "I have learned a lot from them, and both are impressively (if not intimidatingly) fast when doing mathematics." | [M2] | [observed] S (according to Traag; again said of both advisors) |
| S6 | **Willing to take an unconventional candidate.** | "Having only a Masters in sociology in my pocket I arrived there to apply for a position as a PhD candidate (although, if memory serves me well, that was not entirely clear for everyone). … Fortunately, my advisors Paul Van Dooren and Yurii Nesterov were happy to take me on board." | [M2] | [observed] S (according to Traag) |
| S7 | **A host remembered warmly by a former postdoc.** | "I've spent two nice years as a postdoc there during right after my PhD" [sic]. Also: "The workshop is dedicated to the 60th birthday of Yurii Nesterov - my former postdoc advisor." | Richtárik, news entries of 11 Nov 2019 and 7 Feb 2016 [M12] | [observed] S (according to Richtárik) |
| S8 | **"His team" as seen from outside, 2019.** | "Filip Hanzely is visiting Yurii Nesterov and his team at the Center for Operations Research and Econometrics , UCLouvain, Louvain-la-Neuve" | [M12], 11 Nov 2019 | [observed] S |

**What is missing.** No source describes meeting frequency, group seminars, how drafts are passed back and forth, how he corrects a student's proof, or how disagreements are settled. These are gaps, not evidence of absence.

---

## 3. Group habits and working patterns seen in the record

### 3.1 The thesis is a set of joint papers along one line [practice] P
- Doikov: "Our thesis is based on new results published in six papers in the leading peer-reviewed journals of Mathematical Optimization and Machine Learning." [M1, p. 9]
- All six are "Nikita Doikov and Yurii Nesterov":
  - JOTA 2021;
  - Math. Program. 2021/22 (DOI 10.1007/s10107-020-01606-x);
  - NeurIPS 2020 ("Convex optimization based on global lower second-order models");
  - CORE DP 2020/29, later Math. Program. 2023 (DOI 10.1007/s10107-021-01761-9);
  - SIAM J. Optim. 30 (2020) 3146–3169 (DOI 10.1137/19M130769X);
  - ICML 2020 ("Inexact Tensor Methods with Dynamic Accuracies").
- The 4-author SSCN paper is cited in the thesis ([68]) but is not one of the six base papers [M1].
- Traag's thesis is different: 8 papers are listed, and only 3 have Nesterov as co-author. The others are with Bruggeman, Lupu, Krings, Van Dooren and De Leenheer [M2 §1.1]. [practice] P

### 3.2 Division of labour on numerics [practice] P
The public code for the Doikov–Nesterov papers sits in the student's GitHub account:
- `github.com/doikov/contracting-newton` (NeurIPS 2020)
- `dynamic-accuracies` (ICML 2020)
- `logsumexp-simplex` (Math. Program. 2023)
- `super-newton` (SIAM J. Optim. 2024)

Source: [M5], links on the paper list. Agent 03 cloned two of these and found every commit by Doikov (03 §1.2). No code by Nesterov himself was found (03 §1.2).

[inferred] In his group, the student carries the implementation and experiments. Doikov's thesis ends each technical chapter with an "Experiments" section and closes with: "Numerical experiments demonstrated that the new methods are competitive with the contemporary first-order algorithms in terms of the total computational time." [M1, p. 220]. Confidence: medium. The division of labour is not stated anywhere (03 notes the same).

### 3.3 Students travel during the PhD, and the visits produce papers [practice] P / [observed] S
- "Nikita Doikov (Higher School of Economics, Moscow) is visiting me at KAUST. He will stay until late November. Nikita is a PhD student working under the supervision of Yurii Nesterov ." (Richtárik, 9 Oct 2017 [M12]). The later 4-author paper with Hanzely and Richtárik is arXiv 2002.09526 (Feb 2020), ICML 2020.
- Doikov's acknowledgements name outside people "who played a role in forming my research directions" [M1]: Vorontsov, Kropotov, Vetrov, Maximov, Gasnikov, Dvurechensky, Richtárik, Hanzely, Grishchenko, Malick and Stich.
- [inferred] He does not keep students inside the group. Outside visits are allowed, and the resulting papers go into the thesis bibliography.

### 3.4 Recruitment: Moscow computer-science and machine-learning training, then complexity theory [practice] P
- Doikov: "BSc in Computational Mathematics, Lomonosov Moscow State University 2015", "MSc in Computer Science, Higher School of Economics 2017", "Software Engineer at Yandex, Russia 2015", Google internships 2016 and 2018 [M6].
- Rodomanov: BSc Moscow State University 2015 and MSc Higher School of Economics 2017, "both under the supervision of Dmitry Vetrov" [M8]. His MSc thesis was "A Superlinearly-Convergent Proximal Newton-Type Method for the Optimization of Finite Sums" [M9]. His PhD was on superlinear rates of quasi-Newton methods.
- [inferred] The PhD question continues the student's prior expertise. Rodomanov went from a superlinear Newton-type method in his MSc to explicit superlinear rates of classical quasi-Newton methods in his PhD. This matches S1: a question "with a visible hope to succeed". Confidence: low to medium; there are two cases only.

### 3.5 Funding frames the team [practice] P
- The ERC Advanced Grant 788368 "ACCOPT – ACelerated COnvex OPTimization" (ERC-2017-ADG) ran 1 Sept 2018 to 31 Aug 2024 with EUR 2,090,038 [M16].
- It is acknowledged in Doikov's thesis [M1, p. iv] and in the Rodomanov–Nesterov papers ("The research results of this paper were obtained with support of ERC Advanced Grant 788368.") [M17, M18]. His solo "Quartic Regularity" (2022) also acknowledges it [M19].
- The project text sets the lines the students then worked on: "The second line of research will be related to applying acceleration techniques to the second-order methods minimizing functions with sparse Hessians." Its closing aim: "the theoretically most efficient methods will definitely outperform any homebred heuristics." [M16]. The text is probably his own but is not signed, so it is [stated?].
- After the grant, a 2025 solo paper is "supported by the National Research, Development and Innovation Office (NKFIH) under grant number 2024-1.2.3-HU-RIZONT-2024-00030" [M20] (Hungary).
- The co-supervised students of 2009–2013 were funded through Belgian network programs. Traag: "the Actions de recherche concertées, Large Graphs and Networks of the Communauté Française de Belgique and the Belgian Network DYSCO (Dynamical Systems, Control, and Optimization), funded by the Interuniversity Attraction Poles Programme" [M2].

### 3.6 Former students and old peers stay in the loop [practice] P
- Solo 2025: "The author is thankful to Ion Necoara and Nikita Doikov for the interesting and motivating discussions related to the topic of this paper." [M21]. Doikov was a former student and by then a peer. Necoara is a long-time co-author (DBLP 2017, 2019).
- Solo 2026: "The author would like to thank Arkadi Nemirovski for very useful remarks and discussions of the results." [M22]. Agent 01 records that the 1983 fast-gradient paper also thanks Nemirovski for stimulating conversations (01 §4A; not re-read by me). That makes Nemirovski his sounding board from 1983 to 2026 [inferred from the two acknowledgements].
- He still co-authors with Doikov after Doikov's PhD: arXiv 2511.07341 (Nov 2025), and "Gradient regularization of Newton method with Bregman distances", Math. Program. 204 (2024), DOI 10.1007/s10107-023-01943-7 [M28, M30].
- Minor practice detail: the 2026 draft header reads "[ version 4.0, file: FeasIPM\InfeasIPM4.tex ]" [M22]. Even a solo 20-page paper went through numbered versions. [practice] P, low weight.

### 3.7 Author order [practice] P
- With students the order is mostly alphabetical: Doikov, Grapiglia and Rodomanov before Nesterov; Nesterov before Shikhman and Stich.
- There are exceptions: "Nesterov, Florea" (Optim. Methods Softw. 37 (2022) 936–953, DOI 10.1080/10556788.2020.1858831) and the preprint "Y. Nesterov and A. Rodomanov" (2023) [M9, M28]. See also 01 §2.1.
- So author order does not reveal who did what.

### 3.8 Community rituals around him [practice] P / [observed] S
Birthday and anniversary meetings recur every few years:
- 2016: "Optimization without Borders", Les Houches, for his 60th birthday [M12, 7 Feb 2016].
- 2021: "Optimization Without Borders" (Nesterov 65), hybrid, Sirius University, Sochi [M12, 12 July 2021]. Speakers included Nemirovski, Polyak, Stich, Shikhman, Dvurechensky and Gasnikov.
- 2024: ALGOPT2024 at UCLouvain, "a celebration of Yurii Nesterov's 50 years anniversary of doing research in optimization" [M12, 26 Aug 2024]; also [M13].
- 2026: a 70th-birthday special issue of *J. Nonlinear Var. Anal.* 10(2)–(3) [M14, M15], and a "Colloquium in honour of Yurii Nesterov, UCLouvain, Belgium" in Oct 2026, listed among Stich's talks [M10].

The editorial says many contributors "have shared with Yurii an intense scientific and personal collaboration" [M14] [observed] S. It carries no personal recollections.

---

## 4. What he says about students, teaching and collaboration [stated] P

Agent 02 (§7, R1–R8) covers these statements in full. Only the parts that bear on supervision are repeated here, re-read in this run.

| # | Statement (verbatim) | Source | Bearing on mentorship [inferred] |
|---|---|---|---|
| Q1 | "If you're using them properly, they help, but we should explain to students that you shouldn't trust computers blindly," … "You need a critical mind. You need to check your answers using alternative methods." | NCCR Automation interview, 15 Aug 2023 [M23] | Teach verification. A numerical result is checked by an independent route |
| Q2 | "Students often don't even try to think, they try to search. They go to Google. Maybe this is good, maybe not; we will see from future results. Clearly, the possibilities for independent problem solving are going down, but with the substantial help from computers maybe the final results will still improve. We don't know yet." | [M23] | Values independent problem solving. He is openly unsure about the new habits and does not simply condemn them |
| Q3 | "We need a special program where students have more time to study such things than they have in standard universities." | [M23] | Training needs time. The field is "too much" for standard curricula |
| Q4 | "The impact of one paper should be divided by the number of authors," … "Even in our field, where usually a paper has normally two or three authors, now there may be 50 or 60. It is meaningless." | [M23] | Consistent with his two-author practice with students (Pattern B) |
| Q5 | "We must be careful. Basic mathematics is actually very simple and logical—but continuous learning is crucial. If students miss key steps early on, it becomes confusing later." | University of Debrecen interview, 20 Nov 2025 [M24] | Foundations first, without gaps |
| Q6 | "Mathematical thinking means supporting your decisions with logical justification — and being able to accept others' reasoning when it's well-supported." | [M24] | The norm for discussion: argument, and yielding to a good argument |
| Q7 | "A model must not only describe reality — it must also be solvable." … "You must balance accuracy with solvability." | [M24] | What he asks of students' models |

No statement on how he chooses students or questions for them, how often he meets them, or how he writes with them was found. **Gap.**

---

## 5. Tacit knowledge: what his students seem to carry (secondary; low to medium confidence)

Each item says who reports it. None is stated by Nesterov as a rule.

| # | Candidate tacit practice | Basis | Confidence |
|---|---|---|---|
| K1 | **Design the method from the analysis, not from an analogy.** Doikov's own 2026 course, "inspired by and largely based on" Nesterov's 2018 book and Nemirovski's notes, opens the fast-gradient chapter with: "Before, we analyzed methods built on some “physical” or “geometrical” intuition. Such methods are easy to describe by analogy to some known phenomena. However it is difficult to analyze them, after the method is already rigidly fixed. Now, we try a different approach. We will immediately start to look into the essence of what we want to achieve, and that would lead us to the development of a method." | Doikov, ORIE 6365 lecture notes, 30 May 2026, preface and §3.5 [M7]. [observed] S. The link to Nesterov is my inference | medium |
| K2 | **Pick a question you can win, then push along one line.** A research question with "a visible hope to succeed" (S1). The thesis then extends one framework (contracting-point and tensor methods) over six two-author papers | [M1] | medium |
| K3 | **"Implementable" is part of the result.** The thesis aim is "studying implementable algorithms with explicitly stated convergence rates, aiming to have both theoretical and practical justification of the methods" (abstract, p. i). The experiments are judged by total computational time against first-order methods (p. 220) | [M1]. [practice] P | medium |
| K4 | **End with open problems.** Doikov's chapters and conclusion list explicit open questions, for example: "Then, it remains to be an open problem — how to implement the Tensor Method when p ≥ 4, by possibly taking into account the structure of convex polynomials." and "Filling the gaps in this picture, especially related to the optimal methods, is an important direction for research." (pp. 221–222) | [M1]. [practice] P. Whether this is his habit or the student's is **not known** | low |
| K5 | **Theory by the pair, code by the student.** See 3.2 and 03 §1.2 | [M5], 03 | medium |
| K6 | **Check by an independent route.** Q1 is his own advice to students. No student confirms that he enforces it | [M23]. [stated] P | low as a supervision practice |
| K7 | **Speed is part of the model students see.** "impressively (if not intimidatingly) fast when doing mathematics" (S5) | [M2]. [observed] S | low (one witness, two advisors) |

---

## 6. Lineage and network

- **His own training.**
  - PhD 1984, Institute of Control Sciences, advisor Boris T. Polyak [M4]. The 2026 editorial calls Polyak "a great world leader in optimization" [M14]. [observed] S
  - His only joint research paper with Polyak in DBLP is the cubic regularization paper (Math. Program. 108 (2006), DOI 10.1007/s10107-006-0706-8, per 01).
  - With Mordukhovich he co-edited the 2017 special issue for Polyak's 80th birthday. With Mordukhovich and Nemirovski he co-edited the 2025 memorial issue. The records are: JOTA 172 (2017) 349–350, DOI 10.1007/s10957-016-1054-3; JOTA 208, DOI 10.1007/s10957-025-02814-1 [M29]. [practice] P
  - **Both prefaces were not read** (Springer bot check). They are the likeliest place for his own account of how he was supervised.
- **Peer collaboration.** Nemirovski is the constant, from 1985 to 2026, and 7 of 10 DBLP records together are two-author [M28]. Todd (1997–2002) and Vial (1999–2012) were the senior peers of the CORE years [M28].
- **Descendants and their groups.**
  - The Stich line: Stich was his postdoc 2014–2016 [M10]. Rodomanov is now a postdoc in Stich's group [M8].
  - The Jaggi line: Doikov was a postdoc 2022–2025 in Jaggi's EPFL lab [M6].
  - The Richtárik line: his postdoc 2007–2009 [M11], later host of Doikov (KAUST 2017) and of Hanzely's visit to Louvain (2019) [M12].
  - [inferred] A lineage that runs from complexity theory into large-scale machine-learning optimization.
- **Textbooks as teaching at a distance.** "This book has become a major reference in the field and has helped to shape the optimization background and taste of generations of researchers." (IMU Gauss Prize citation on the 2004 book [M25]) [observed] S. The 2009 von Neumann citation: the 2004 text "develops state-of-the-art theory at a level appropriate for introductory graduate courses" [M27]. A former student builds his own graduate course on the 2018 book [M7].

---

## 7. Failures, dead ends, corrections

- **Corrections.** "Correction: High-order methods beyond the classical complexity bounds: inexact high-order proximal-point methods", Ahookhosh & Nesterov, Math. Program. 208 (2024) 409–410, DOI 10.1007/s10107-024-02067-2 [M28]. **Content not read.** What was corrected, and who found it, is unknown.
- **Co-supervised students with little joint output.** Sadykov (2006) has no joint paper with Nesterov in DBLP. Baes has one, in 2012, six years after his defence [M28].
  - [inferred] At least some co-supervisions were light, with the main work done with the co-supervisor. It is also possible that DBLP misses Russian-language or CORE-DP-only items. Not resolved.
- **Rejected papers, abandoned student projects, students who left without a degree:** none found. **Gap.**
- **Review friction** in a student-led paper: agent 03 read the NeurIPS 2020 reviews and author feedback (03 §2). I did not re-read them.

---

## 8. Era and resource context

| Period | Setting | Supervision practice (evidence) | Resources |
|---|---|---|---|
| 1977–1992, Moscow (CEMI) | Researcher, Soviet Academy of Sciences system; Polyak as advisor, Nemirovski as senior peer | **No evidence of any students** in this period | Letters "once a month" (his own words, 2023, agent 02 R8); no funding records seen |
| 1993–2009, CORE, Louvain | Professor at CORE; co-director 1999–2003 per 01 | Co-supervised PhDs with Van Dooren and Wolsey (Hachez 2003, Sadykov 2006, Baes 2006); Eleuterio (ETH 2009, per [M4]); hosted Richtárik 2007–2009 | Belgian programs (not itemised for these students); CORE DP series as preprint outlet |
| 2009–2016 | CORE / INMA | Co-supervised Traag (with Van Dooren) and Devolder (with Glineur); hosted Stich 2014–2016 (SNSF) | ARC "Large Graphs and Networks"; DYSCO IAP network [M2]; SNSF fellowship [M10] |
| 2017/2018–2024 | CORE / ICTEAM, ERC AdG | Sole supervisor (Doikov, Rodomanov). Two-author papers, code in student repos, one postdoc year after the PhD. Team of about 6 junior people named by Doikov | ERC AdG 788368, EUR 2.09 M, 2018–2024 [M16]; MIAI Grenoble also acknowledged in 2022 [M19] |
| 2024–2026 | Emeritus UCLouvain; part-time CUHK-Shenzhen; Hungarian grant | Solo papers that thank former students; joint work with ex-students (Doikov) and a Budapest IPM group (per 01); Festschrift events | NKFIH 2024-1.2.3-HU-RIZONT-2024-00030 [M20] |

[inferred] The two-author, question-set-by-supervisor mode belongs to a senior PI with a large personal grant and a small team of strong, computationally trained students. It is not a model for a junior researcher's first students (framework §七).

---

## 9. Where this evidence lands in the seven layers

- **Layer 2 (problem choice).** In the ERC-era group the supervisor chooses the question: S1, K2 and the ERC work plan in 3.5.
- **Layer 4 (execution).** The student implements and runs the experiments; wall-clock comparisons against first-order baselines: 3.2, K3 and K5.
- **Layer 5 (judging results).** Check by alternative methods: Q1 and K6. Only a stated norm, not an observed routine.
- **Layer 6 (expression).** The thesis is a sequence of joint papers and ends with open problems: 3.1 and K4.
- **Layer 7 (organisation).** Two supervision eras (Pattern A), small pairs (Pattern B), outside visits (3.3), a funding frame (3.5), long-lived ties (3.6) and community rituals (3.8).
- **Layer 1 (taste), as it is passed on.** Design from the analysis (K1); textbooks shaping "taste of generations" (§6).
- **Layer 3 (idea generation).** No mentorship evidence. Empty here.

## 10. Leads for the skill (Phase 2; all [inferred], to be checked against 02 and 03)

1. When "Nesterov" proposes work on a solver, frame it as he frames a student's question. It should be one well-posed question with a clear complexity or rate target and "a visible hope to succeed" (S1). It should not be a list of heuristics.
2. Pair each theoretical idea with an implementable variant. Plan a wall-clock comparison against a strong first-order or classical baseline, run by whoever owns the code (K3, K5).
3. Close every proposal with explicit open problems, the way his students close theirs (K4).
4. Keep the team small, one idea-owner plus one implementer, and grow a line of results along one framework (Patterns A and B, 3.1).
5. Do not present these as Nesterov's stated rules. Only Q1–Q7 are his words.

---

## Contradictions (kept, not reconciled)

1. **How many PhD students?**
   - "Five Ph.D.-students (5 defended)": his Academia Europaea CV, page revision of July 2021 (read by agents 01 and 02).
   - "According to our current on-line database, Yurii Nesterov has 3 students and 3 descendants.": Math Genealogy [M4].
   - Six named theses on the CORE list alone [M3]; eight distinct names in total in §1.1.
   - "Professor Yurii Nesterov has produced dozens of master and Ph.D. students and postdoctoral fellows, most of them are now active experienced researchers in the community of applied mathematics and engineering.": 2026 editorial [M14]. The editorial copies other wording nearly verbatim from the 2009 INFORMS citation [M27], so its independent weight is limited [inferred].
2. **Devolder's defence year.** Math Genealogy gives 2013 [M4]. The CORE list gives "August 31, 2015" [M3], the same date as the entry just above it (Aly), which may be a copying error. The next entry below it is dated 4 October 2011. Not resolved.
3. **Who chooses the question?**
   - "He formulated a very interesting research question" (Doikov 2021, sole supervision) [M1].
   - "The leeway they allowed me to pursue my own interest" (Traag 2013, co-supervision, said of both advisors) [M2].
   - These may be two eras or two supervision set-ups, or the difference may be the co-advisor's. Kept as a contradiction.
4. **Where was Doikov a PhD student in 2017?** Richtárik (Oct 2017) says "Nikita Doikov (Higher School of Economics, Moscow) … is a PhD student working under the supervision of Yurii Nesterov" [M12]. Doikov's CV gives "MSc in Computer Science, Higher School of Economics 2017" and a UCLouvain PhD in 2021, with no start date [M6]. Rodomanov's UCLouvain doctoral contract starts 23/01/2019 [M9]. The start of Doikov's PhD and its first host institution are unresolved.
5. **Alphabetical order, with exceptions.** Mostly alphabetical with students, but "Nesterov, Florea" (2022) and "Y. Nesterov and A. Rodomanov" (2023 preprint) are not [M9, M28].
6. **Stated ideal vs record on authorship.** He says citation indices should reward "the amount of personal valuable research" (2023; agent 02 R3). Yet none of his 7 DBLP records for 2025–26 is solo (01 §1). Against this, he posted at least three solo arXiv papers in 2025–26 (2503.10155, 2509.20902, 2603.21500), which are not in that DBLP count. The tension may be a database artefact. Kept as recorded, not resolved.
7. **ALGOPT2024 dates.** "August 27-30, 2024" (Richtárik [M12]) vs "27-29 of August" (Dvurechensky [M13]).
8. **Citation figure.** "These publications have received more than 13000 citations" (Scopus, per [M14]). Agent 01 records thousands of citations for single works (for example the 2004 book). This is a scope difference between databases; noted, not resolved.

## Gaps

- **Rodomanov's thesis acknowledgements.** Not read. The PDF is on DIAL (`dial.uclouvain.be/pr/boreal/object/boreal:266105`), and both curl ("Recv failure: Connection reset by peer", repeated) and WebFetch (HTTP 503) failed. This is the second sole-supervision testimony and would test S1–S3.
- **Other theses not read** (all DIAL-hosted or unlocated):
  - Devolder (2013/2015);
  - Hachez (2003);
  - Baes (2006);
  - Sadykov (2006);
  - Dos Santos Eleuterio (ETH 2009): the ETH Research Collection returned "429 Too Many Requests", and Crossref and DataCite had no record.
- **Traag's Springer Theses edition** (DOI 10.1007/978-3-319-06391-1). Springer Theses volumes often carry a supervisor's foreword. **Not read**: Springer answered with a bot check and a login redirect, which I did not follow.
- **Polyak prefaces** (JOTA 2017 and 2025/26). Not read (Springer bot check). They would show his own account of being supervised.
- **Book prefaces.** The acknowledgements in the 2004 and 2018 books were not read (see 02 Gaps). The copy on a university course server was deliberately not used.
- **Glineur's homepage** (probable student list with co-supervisors) and the UCLouvain people pages: connection reset.
- **No first-hand account of the daily routine.** Nothing on meetings, seminars, how drafts are revised, how proofs are checked, or how collaborations start and end. No student blog, interview or memorial piece was found in either WebSearch call.
- **Moscow period (1977–1992).** No evidence of any supervision.
- **Roles of Grapiglia, Florea, Vorontsova, Ahookhosh, Leplat and Shikhman** (postdoc, visitor, or colleague). Not verified from their own pages. Grapiglia's arXiv author page returned 404.
- **Nemirovski's view of the collaboration.** Not found.
- **Festschrift materials.** Programs, laudations or recordings of Optimization without Borders 2016/2021, ALGOPT2024 and the Oct 2026 colloquium: not read.
- **The 2024 correction** (Ahookhosh & Nesterov): content not read.
- **Services unavailable in this run.** The OpenAlex search API was "temporarily unavailable" and the Semantic Scholar API returned 429. Thesis metadata were checked through the CORE list and Crossref instead.
- **Sub-questions dropped at the time box:** Eleuterio thesis, Devolder thesis, and Rodomanov thesis via any mirror.

## Sources

Tool checks in this run: all DOIs cited above were resolved through the Crossref API, and the arXiv ids through arxiv.org abstract pages. DBLP data comes from this run's SPARQL export in the scratch folder.

**Student and postdoc records and testimonies**
- [M1] Nikita Doikov, *New second-order and tensor methods in Convex Optimization*, PhD thesis, UCLouvain, September 2021, https://doikov.com/thesis.pdf. Read: title page, abstract, acknowledgements (p. iii), funding note (p. iv), §1.1, ch. 5. Primary as a record; secondary about Nesterov.
- [M2] V. A. Traag, *Algorithms and Dynamical Models for Communities and Reputation in Social Networks*, PhD thesis, UCLouvain, 2013 (hdl.handle.net/2078.1/134615), https://www.traag.net/wp/wp-content/papercite-data/pdf/traag_algorithms_2013.pdf. Read: title page, acknowledgements, §1.1. Primary as a record; secondary about Nesterov. The Springer Theses edition (2014, DOI 10.1007/978-3-319-06391-1) was not read.
- [M3] UCLouvain LIDAM/CORE, "Doctoral Dissertations", https://uclouvain.be/en/research-institutes/lidam/core/doctoral-theses, accessed 2026-09-28. Primary (institutional record).
- [M4] Mathematics Genealogy Project, "Yurii Evgenievich Nesterov" (MGP id 102203), https://www.mathgenealogy.org/id.php?id=102203, accessed 2026-09-28. Secondary.
- [M5] Nikita Doikov, homepage, https://doikov.com/, accessed 2026-09-28. Primary (student).
- [M6] Nikita Doikov, Curriculum Vitae, https://doikov.com/CV.pdf, accessed 2026-09-28. Primary (student).
- [M7] Nikita Doikov, *Lecture Notes on Continuous Optimization: Algorithms and Complexity* (Cornell ORIE 6365), 30 May 2026, https://doikov.com/Doikov_Optimization_2026.pdf. Read: preface and opening of §3.5. Primary (student's teaching); secondary about Nesterov.
- [M8] Anton Rodomanov, homepage, https://arodomanov.github.io/, accessed 2026-09-28. Primary (student).
- [M9] Anton Rodomanov, Curriculum Vitae (last updated 5 Jul 2026), https://arodomanov.github.io/files/cv.pdf. Primary (student).
- [M10] Sebastian U. Stich, homepage (CV and talks), https://www.sstich.ch/, accessed 2026-09-28. Primary (postdoc record).
- [M11] Peter Richtárik, "Bio", https://richtarik.org/i_bio.html, accessed 2026-09-28. Primary (postdoc record).
- [M12] Peter Richtárik, "Old News" (entries 14 May 2013; 21 May 2014; 7 Feb 2016; 9 Oct 2017; 11 Nov 2019; 12 Jul 2021; 26 Aug 2024), https://richtarik.org/i_oldnews.html. Secondary (observations by a former postdoc).
- [M13] Pavel Dvurechensky, WIAS homepage (news and publication list), https://www.wias-berlin.de/people/dvureche/, accessed 2026-09-28. Secondary.

**Festschrift, prizes and profiles**
- [M14] B. S. Mordukhovich, X. Qin, J.-C. Yao, "Editorial: Special issue dedicated to the 70th birthday of Professor Yurii Nesterov", *J. Nonlinear Var. Anal.* 10(2) (2026) 199–200, DOI 10.23952/jnva.10.2026.2.01 (PDF http://jnva.biemdas.com/issues/JNVA2026-2-1.pdf). Read in full. Secondary.
- [M15] Crossref listing of the *J. Nonlinear Var. Anal.* 10(2) and 10(3) (2026) special-issue contents. Metadata only.
- [M25] IMU / DMV, "Gauss Prize 2026: Yurii Nesterov", citation, July 2026, https://www.mathunion.org/fileadmin/documents/2026-07/Gauss_Yurii_Nesterov_2026_Citation.pdf. Secondary.
- [M26] Allyn Jackson, "2026 Gauss Prize: Yurii Nesterov", IMU, July 2026, https://www.mathunion.org/fileadmin/documents/2026-07/article-gauss-final.pdf. Read in full; nothing on students. Secondary.
- [M27] INFORMS, "Yurii Nesterov" award-recipient page (2009 von Neumann Theory Prize and 2022 Lanchester Prize citations), https://www.informs.org/Recognizing-Excellence/Award-Recipients/Yurii-Nesterov. Secondary.
- [M32] UCLouvain ICTEAM, "Yurii Nesterov receives the 2026 Carl Friedrich Gauss Prize", 24 July 2026, https://www.uclouvain.be/en/research-institutes/icteam/news/yurii-nesterov-receives-the-2026-carl-friedrich-gauss-prize. Read; nothing on students. Secondary.
- [M33] CUHK-Shenzhen School of Data Science, "NESTEROV, Yurii" profile, https://sds.cuhk.edu.cn/en/teacher/1634. Read; nothing on students. Secondary.

**His own texts and joint papers (funding lines, acknowledgements, headers)**
- [M16] CORDIS, ERC Advanced Grant 788368 "ACCOPT – ACelerated COnvex OPTimization" (ERC-2017-ADG, 2018-09-01 to 2024-08-31), https://cordis.europa.eu/project/id/788368. Primary (grant record; unsigned objective text).
- [M17] A. Rodomanov, Yu. Nesterov, "Greedy Quasi-Newton Methods with Explicit Superlinear Convergence", *SIAM J. Optim.* 31 (2021) 785–811, DOI 10.1137/20M1320651, arXiv 2002.00657. Funding line and acknowledgements read. Primary.
- [M18] A. Rodomanov, Yu. Nesterov, "Rates of superlinear convergence for classical quasi-Newton methods", *Math. Program.* 194 (2022) 159–190, DOI 10.1007/s10107-021-01622-5, arXiv 2003.09174. Funding line and acknowledgements read. Primary.
- [M19] Yu. Nesterov, "Quartic Regularity", arXiv 2201.04852 (CORE DP 2022/01), Jan 2022. Funding line read. Primary.
- [M20] Yu. Nesterov, "Asymmetric Long-Step Primal-Dual Interior-Point Methods with Dual Centering", arXiv 2503.10155, Mar 2025. Affiliation and funding read. Primary.
- [M21] Yu. Nesterov, "Universal Complexity Bounds for Universal Gradient Methods in Nonlinear Optimization", arXiv 2509.20902, Sep 2025. Acknowledgement read. Primary.
- [M22] Yu. Nesterov, "Theorem of Alternative for Extended Homogeneous Linear System and its Application in Conic Optimization", arXiv 2603.21500, Mar 2026. Header and acknowledgement read. Primary.

**Interviews**
- [M23] Robynn Weldon, "'This is an unprecedented overflow': Why the progress of his field alarms Yurii Nesterov", NCCR Automation, 15 Aug 2023, https://nccr-automation.ch/news/2023/unprecedented-overflow-why-progress-his-field-alarms-yurii-nesterov. Primary quotes in a secondary article.
- [M24] "'Mathematical Thinking Is the Key to Understanding AI' — Interview with Yurii Nesterov", University of Debrecen, Faculty of Engineering, 20 Nov 2025, https://eng.unideb.hu/en/news/mathematical-thinking-key-understanding-ai-interview-yurii-nesterov. Primary (Q&A; editing process unknown).

**Records and metadata**
- [M28] DBLP, "Yurii E. Nesterov" (pid 00/343), 122 records, SPARQL export fetched 2026-09-28 (scratch copy used for the co-author counts). Primary record.
- [M29] Crossref records for (a) B. S. Mordukhovich, Yu. Nesterov, "Preface to the Special Issue 'Optimization, Control and Applications' in Honor of Boris T. Polyak's 80th Birthday", *JOTA* 172 (2017) 349–350, DOI 10.1007/s10957-016-1054-3; (b) B. Mordukhovich, A. Nemirovski, Yu. Nesterov, "Special Issue in memory of Boris Polyak", *JOTA* 208, DOI 10.1007/s10957-025-02814-1. Metadata only; texts **not read**.
- [M30] arXiv abstract pages: 2511.07341 (N. Doikov, Yu. Nesterov, "Universal Reduced-Operator Method and High-Order Global Curvature Bounds", 10 Nov 2025) and 2002.09526 (F. Hanzely, N. Doikov, P. Richtárik, Yu. Nesterov, "Stochastic Subspace Cubic Newton Method", 21 Feb 2020). Metadata.

**Consulted, nothing used**
- [M31] A. V. Gasnikov, *Universal gradient descent* (in Russian), arXiv 1711.00394. Preface read; no mentorship content.

**Cross-references inside this skill folder (not counted as sources)**
- `01-publications.md` §2.1, §2.2, §4A: author order, the collaborator table, the 1983 acknowledgement of Nemirovski.
- `02-methodology.md` §7: fuller interview quotes; Academia Europaea CV.
- `03-process-evidence.md` §1.2, §2: code and experiments in the student-led papers; NeurIPS 2020 reviews.
