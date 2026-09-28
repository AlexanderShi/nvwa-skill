# Roger Fletcher: students, collaborators and group culture (research agent 04)

| Field | Value |
|---|---|
| Researcher | Roger Fletcher (1939-2016). PhD Leeds 1963 under Colin Reeves; lecturer Leeds to 1969; AERE Harwell 1969-73; University of Dundee from 1973 (professor of optimization and Baxter Professor from 1984, emeritus after 2005). Deceased, so this is a historical lens: everything below comes from what he said in public, what he and his students published, and what others wrote about him |
| Dimension | 04: students and collaborators (supervision style, group habits, group culture, tacit knowledge) |
| Research date | 2026-09-28 |
| Sources consulted | 18 read, fully or in the relevant part: 5 primary (the 2015 Leyffer interview, the Dai interview, two archived versions of his Dundee homepage, Leyffer's 1993 PhD thesis, Grothey's 2001 PhD thesis), 11 secondary (the Gould and Hall Royal Society memoir in full, Leyffer's SIAM News obituary, Nocedal's Optima obituary, Toint's and Curtis's Optima commentaries, the Griffiths and Watson NA Digest notice, the Courier news report, the Mathematics Genealogy Project entry, the EUROPT 2017 memorial-session page, the Optima 73 prize citation, Higham's 2015 blog post), 2 bibliographic (Crossref metadata for 33 papers; the mathopt.org Optima issue index). Several more were tried and could not be reached (see Gaps) |
| WebSearch calls used | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,essays,software}` hold only `.gitkeep`. `sources/talks/` holds a notes file on the Optima 99 interview written by another research agent in this run, not by the user. `private/` was not opened |
| Language | English (per team.json) |

**What was read and how.** Fletcher left no lab guide, blog or advice essay for students, and none of his PhD students has published a first-person memoir of being supervised by him that I could find. The evidence for this dimension is therefore:

1. The Royal Society memoir by N. I. M. Gould and J. A. J. Hall (2025; Hall was his PhD student, Gould a long-time collaborator), read in full from the Wayback Machine copy of the open-access PDF (snapshot of 2 August 2025; the publisher site returns a Cloudflare challenge). It is CC-BY 4.0. It is the richest source on his students. It says itself that it drew on the Dai and Leyffer interviews and that Leyffer commented on a draft (p. 143), so on supervision it is **not independent of Leyffer**.
2. Sven Leyffer's writing about him. Leyffer was his PhD student (thesis dated December 1993), then his research fellow, then his main collaborator. That covers the interview he conducted (*Optima* 99, December 2015), in which Leyffer also recalls Dundee, and his obituary in *SIAM News* 49(10), December 2016, p. 2. I read the obituary from the Wayback copy of the print-issue PDF; siam.org returns 403.
3. Pieces by peers who were not his students: Philippe Toint and Frank E. Curtis (*Optima* 99), Jorge Nocedal (*Optima* 102, April 2017), and the Dundee colleagues David Griffiths and Alistair Watson (NA Digest, July 2016).
4. His own words: the Yu-Hong Dai interview (published in *Pac. J. Optim.* 2 (2006) 1-10 according to the memoir's reference list; I read the copy on the Kyoto University optimization lab website, cited by question number) and his Dundee homepage (Wayback snapshots of 28 April 2001 and 11 March 2017; the 2017 copy carries text written c.2005).
5. Behaviour recorded in students' theses: Leyffer's PhD thesis (Dundee, December 1993; the copy on his Argonne homepage) and Andreas Grothey's (Edinburgh, 2001; Edinburgh Research Archive).

PDFs were extracted with pypdf. Quotes are verbatim. I repaired only PDF-extraction damage: split words ("Y ou" to "You"), line-break hyphens ("numeri-cal" to "numerical"), ligatures, and stray spaces before reference numbers. Original typos are kept and marked [sic]. Page numbers are the printed page numbers of the item named.

**Tags.** [stated] = Fletcher said or wrote it. [practice] = what he or his group did, shown by papers, codes, theses or records. [observed] = what someone else reports about him. [inferred] = my own inference, never to be quoted as anyone's view. Each item is also marked **primary** (his own words or his group's own documents) or **secondary** (someone else's account). Every observation by a student or collaborator is secondary, as the task requires.

---

## 0. Themes reported by three or more independent observers

"Independent" here means different people. The memoir is counted separately from Leyffer only where it gives its own detail (for example the squash games), since it drew on his accounts.

| # | Theme | Who reports it (source) | Count |
|---|---|---|---|
| M1 | **Hospitality to juniors and visitors, often in the hills.** Home invitations, hill walks, conference hosting | Toint 1975 recollection (Optima 99, p. 6); Curtis (Optima 99, p. 7); Leyffer ("a happy environment for his many Ph.D. students and visitors", SIAM News 2016); Gould and Hall (memoir, pp. 133, 138, 141); Fletcher himself about Powell and Davidon (Dai interview Q5) | 5 |
| M2 | **Humility and generosity with credit**, to the point of understating his own role | Nocedal ("charming humility", Optima 102, p. 6); Toint ("far too modest ... and quite typical of him", Optima 99, p. 6); Curtis ("the utmost humility and respect for colleagues", Optima 99, p. 6); Leyffer ("humble and approachable", SIAM News); F. Davidson ("a kind and humble man", Courier 2016); memoir ("extremely modest", p. 142) | 6 |
| M3 | **Code and numbers first, as the value he passed on.** Students and colleagues remember the programmer and "look at examples" as much as the theorems | Leyffer ("one of the things you always told us was to look at examples", Optima 99, p. 4; "software validates theory", SIAM News); Nocedal ("the programmer who knew how to get the numerics right", Optima 102); Toint ("his real interest was in algorithm design", Optima 99, p. 6); memoir ("robust to floating-point computation", p. 137); his own advice "be a good programmer" (Optima 99, p. 4) | 4 observers + his own statement |
| M4 | **Willing to be told he was wrong** by juniors, referees' targets and critics of his codes | Leyffer (Dai referee story, SIAM News); Curtis (criticised one of his codes in a talk Fletcher attended, Optima 99, p. 7); memoir ("initially cynical ... gradually changed his mind", p. 140); his own account (Optima 99, p. 4) | 3 observers + his own statement |
| M5 | **Students' projects were pieces of his own solver stack** (LU updates, sparse LP linear algebra, MINLP on top of bqpd, SLP-filter) | Memoir (Matthews, Hall, Leyffer, Sainz de la Maza, pp. 137-139); Leyffer's thesis (bqpd underlies it, pp. 22, 76-79); homepage (Chin, research fellow Leyffer, c.2001-05); Leyffer on the bqpd "class" design (SIAM News) | 4 (mostly practice) |

---

## 1. Who his students and junior collaborators were

**1.1 His own list** [stated, primary] (Dai interview Q18, c.2005-06)
- Asked for "a full list of your PhD students", he answered: "I don't keep records on this, but here is a list of students with whom I have published joint papers." The list: "Bill Bradbury (MSc), Tony McCann (MSc), Mike Hebden, Shirley Lill, Mike Jackson, Jim Sinclair, Rob Womersley, Paul Matthews, Mehi Al-Baali, Chenxian Xu, Eduardo Sainz de la Maza, Julian Hall, Sven Leyffer, Suliman Al-Homidan, Eric Chin." He added nationalities for four of them (Syrian, Chinese, Saudi, Malaysian).
- [inferred] He defined "student" by joint publication, not by formal supervision. Joint papers seem to have been the normal outcome of working with him. The Mathematics Genealogy Project (id 52148, secondary) lists only five Dundee PhDs: Womersley 1981, Al-Baali 1984, Xu 1987, Hall 1992, Leyffer 1994. See Contradiction C1.

**1.2 Roster with the joint paper that marks each relationship** [practice, primary; papers checked in Crossref in this run]

| Person (status as given by the source) | Period, place | Joint work (checked identifier) | What the memoir says the student contributed |
|---|---|---|---|
| W. W. (Bill) Bradbury, "his first MSc student" (memoir p. 141) | Leeds, 1960s | Bradbury & Fletcher, "New iterative methods for solution of the eigenproblem", *Numer. Math.* 9:259-267, 1966, DOI 10.1007/bf02162089 (the memoir's item 4 prints the pages as "59–267") | eigenproblem methods |
| A. P. (Tony) McCann, "Leeds MSc student" (memoir p. 134 footnote) | Leeds, 1968 | "Acceleration techniques for nonlinear programming", in *Optimization: Proc. Symp. Inst. Math. Appl., University of Keele, 1968* (ed. R. Fletcher), Academic Press 1969, pp. 203-215 (memoir bibliography item 6; a Crossref search found no record, so this rests on the memoir alone) | extrapolation methods for constrained optimization |
| S. A. (Shirley) Lill, his "first PhD student", later a co-founder of NAG Ltd (memoir p. 132) | Leeds from 1967; he left for Harwell before she graduated | "A Class of Methods for Nonlinear Programming II Computational Experience", *Nonlinear Programming* (Academic Press), 1970, pp. 67-92, DOI 10.1016/b978-0-12-597050-1.50007-5 | computational side of his exact-penalty ideas |
| Mike Hebden, "former Leeds student ... who had followed Roger to Harwell" (memoir p. 136) | Leeds, then Harwell | Fletcher, Grant, Hebden, "The continuity and differentiability of the parameters of best linear L approximations", *J. Approx. Theory* 10, 1974, DOI 10.1016/0021-9045(74)90097-5; also "Linear Minimax Approximation as the Limit of Best Lp-Approximation", *SIAM J. Numer. Anal.* 11, 1974, DOI 10.1137/0711013 | lp approximation |
| Mike Jackson, "from Oxford" (memoir p. 136); in Fletcher's own student list (Q18) | Harwell, 1973 | "Minimization of a Quadratic Function of Many Variables Subject only to Lower and Upper Bounds", *IMA J. Appl. Math.* 14, 1974, DOI 10.1093/imamat/14.2.159 | bound-constrained QP code VE04 |
| R. S. (Rob) Womersley, "his first notable PhD student", arrived 1977 (memoir p. 138) | Dundee, PhD 1981 (MGP) | Womersley & Fletcher, "An algorithm for composite nonsmooth optimization problems", *JOTA* 48, 1986, DOI 10.1007/bf00940574 | "numerical methods for structured problems in non-smooth optimization" |
| J. W. (Jim) Sinclair, PhD (memoir p. 138) | Dundee, c.1980 | "Degenerate values for Broyden methods", *JOTA* 33, 1981, DOI 10.1007/bf00935247 | quasi-Newton methods |
| S. P. J. (Paul) Matthews, PhD (memoir p. 138) | Dundee, early 1980s | "Stable modification of explicit LU factors for simplex updates", *Math. Program.* 30, 1984, DOI 10.1007/bf02591933; "A Stable Algorithm for Updating Triangular Factors Under a Rank One Change", *Math. Comp.* 45, 1985, DOI 10.2307/2008137 | stable LU update, "the foundation of Roger's computational work for a while" |
| Mehiddin (Mehi) Al-Baali, PhD (MGP 1984) | Dundee | Al-Baali & Fletcher, "An efficient line search for nonlinear least squares", *JOTA* 48, 1986, DOI 10.1007/bf00940566 | nonlinear least squares; CG convergence observations |
| Chengxian Xu, PhD (MGP 1987) | Dundee | Fletcher & Xu, "Hybrid Methods for Nonlinear Least Squares", *IMA J. Numer. Anal.* 7, 1987, DOI 10.1093/imanum/7.3.371 | nonlinear least squares |
| Eduardo Sainz de la Maza, PhD student (memoir p. 137; Fletcher, Optima 99 p. 4) | Dundee, 1980s | "Nonlinear programming and nonsmooth optimization by successive linear programming", *Math. Program.* 43, 1989, DOI 10.1007/bf01582292 | "a practical variant" of his Sl1QP idea (SLP-EQP) |
| J. A. J. (Julian) Hall, PhD (MGP 1992), first ECOSSE-funded researcher (memoir p. 139) | Dundee | Fletcher, Hall & Johns, "Flexible retrofit design of multiproduct batch plants", *Comput. Chem. Eng.* 15, 1991, DOI 10.1016/0098-1354(91)80029-u; Fletcher & Hall, "Ordering algorithms for irreducible sparse linear systems", *Ann. Oper. Res.* 43, 1993, DOI 10.1007/bf02025533 | convex MINLP solver for a batch-plant model; sparse linear algebra for the LP solver blpd |
| Sven Leyffer, PhD (thesis dated December 1993; MGP gives 1994), then research fellow, then long-term collaborator | Dundee, then Argonne | "Solving mixed integer nonlinear programs by outer approximation", *Math. Program.* 66, 1994, DOI 10.1007/bf01581153; "Numerical Experience with Lower Bounds for MIQP Branch-And-Bound", *SIAM J. Optim.* 8, 1998, DOI 10.1137/s1052623494268455; filter papers 2002 (below) | MINLP outer approximation; then filterSQP |
| Suliman Al-Homidan, PhD student (memoir p. 141) | Dundee, early 1990s | Al-Homidan & Fletcher, "Hybrid Methods for Finding the Nearest Euclidean Distance Matrix", in *Recent Advances in Nonsmooth Optimization*, World Scientific 1995, pp. 1-17, DOI 10.1142/9789812812827_0001 | semidefinite / distance-matrix problems |
| Christine Zoppke-Donaldson, ECOSSE-funded student (memoir p. 139) | Dundee, c.1990 | none: her work on "tolerance tubes" is described as "unpublished" | a precursor of the filter idea, according to the memoir |
| Frank Plab (1989), Andreas Grothey (1994): "more German students" who "further enhanced Roger's research team" (memoir p. 139) | Dundee / Edinburgh | Fletcher, Grothey & Leyffer, "Computing Sparse Hessian and Jacobian Approximations with Optimal Hereditary Properties", IMA Volumes, Springer 1997, pp. 37-52, DOI 10.1007/978-1-4612-1960-6_3 | sparse secant updates. Grothey's PhD was at Edinburgh under Ken McKinnon (see C4) |
| Choong Ming Chin ("Eric Chin" in the Q18 list, [inferred] the same person) | Dundee, PhD completed c.2001 (homepage) | Chin & Fletcher, "On the global convergence of an SLP-filter algorithm that takes EQP steps", *Math. Program.* 96, 2003, DOI 10.1007/s10107-003-0378-6 | SLP-filter with EQP steps |
| Chungen Shen (visitor, not a student per the sources I read) | 2010s | Shen, Leyffer & Fletcher, "A nonmonotone filter method for nonlinear optimization", *Comput. Optim. Appl.* 52, 2012, DOI 10.1007/s10589-011-9430-2 | nonmonotone filter |

Sources for the right-hand column: memoir pp. 132-141 [observed, secondary]. The Crossref checks confirm title, venue, year and co-authors, not the student's role.

**1.3 Peer collaborators who shaped his practice** [practice, primary for the papers; observed for the roles]
- M. J. D. Powell: DFP (1963). Leyffer calls them "a lifelong competitive friendship" (SIAM News).
- G. A. Watson (Dundee colleague): composite nondifferentiable optimization. Fletcher: "which I did with Alistair Watson" (Optima 99, p. 3) [stated].
- Philippe Toint and Nick Gould: filter convergence theory. Fletcher, Leyffer & Toint, "On the Global Convergence of a Filter--SQP Algorithm", *SIAM J. Optim.* 13, 2002, DOI 10.1137/s105262340038081x. Fletcher, Gould, Leyffer, Toint & Wächter, "Global Convergence of a Trust-Region SQP-Filter Algorithm for General Nonlinear Programming", *SIAM J. Optim.* 13, 2002, DOI 10.1137/s1052623499357258. Crossref lists four authors (Fletcher, Gould, Leyffer, Toint) for the second paper, while the memoir's bibliography item 51 adds Wächter. I did not check which is right.
- Danny Ralph and Stefan Scholtes: "Local Convergence of SQP Methods for Mathematical Programs with Equilibrium Constraints", *SIAM J. Optim.* 17, 2006, DOI 10.1137/s1052623402407382.
- Yu-Hong Dai (visitor from Beijing): "On the asymptotic behaviour of some new gradient methods", *Math. Program.* 103, 2005, DOI 10.1007/s10107-004-0516-9; "Projected Barzilai-Borwein methods ...", *Numer. Math.* 100, 2005, DOI 10.1007/s00211-004-0569-y; "New algorithms for singly linearly constrained quadratic programs subject to lower and upper bounds", *Math. Program.* 106, 2006, DOI 10.1007/s10107-005-0595-2.
- Chemical engineers at Edinburgh (ECOSSE): W. R. Johns (1991 paper above); Bill Morton, "Initialising distillation column models", *Comput. Chem. Eng.* 23, 2000 (Crossref date; memoir gives 1999), DOI 10.1016/s0098-1354(00)00295-7.
- **Author order** [practice, primary; inferred reading]: in the student papers above, the order is alphabetical in most cases (Al-Baali-Fletcher, Chin-Fletcher, Fletcher-Hall, Fletcher-Leyffer, Fletcher-Xu). The exceptions are Womersley & Fletcher (1986) and Shen, Leyffer & Fletcher (2012), where the junior author comes first. Agent 01 reached the same conclusion (01-publications.md §1). So author order says nothing reliable about who led a student paper.

---

## 2. Supervision style

**2.1 The template he inherited: the supervisor supplies the idea, the student makes it compute** [stated, primary; observed, secondary]
- His own supervision: "my supervisor got a copy of Bill Davidon's Argonne National Laboratory report [7], and he said, "Try that for your problem."" (Optima 99, p. 2). And "Of course, the ideas were fed to me by Colin Reeves; my input was mainly in getting the programs to work!" (Dai interview Q2). On Fletcher-Reeves: "Since I had a line search code I was able to follow this idea up for him by making some computations." (Q10)
- The memoir repeats the pattern: "By chance, Colin Reeves obtained a copy, and passed this on to his student, Roger, for him to explore." (p. 132). Reeves's lasting influence is attributed to "his insistence that numerical optimization was an upcoming subject of utmost importance (unpublished, 2003)" (p. 131). The source is an unpublished 2003 text, presumably by Fletcher; I have not read it.
- His PhD years as the model environment: "That was probably the happiest period of my life, doing the Ph.D. at Leeds – there were a lot of clever people there!" (Optima 99, p. 1) [stated]. Leyffer ties this to Dundee: "Many years later, while a professor at Dundee, he would create a similarly happy atmosphere for his students and visitors." (SIAM News 2016) [observed, secondary].
- Leyffer on what he passed on: "Roger selflessly provided guidance to his students, passing on to a new generation of researchers the luck and good ideas he felt he was given." (SIAM News 2016) [observed, secondary].
- [inferred] He supervised the way he was supervised. He handed a student an idea or a problem, expected the student to make it compute, and wrote the joint paper. His remark about PhD students (2.3) shows he gave students ideas to try. Nothing I read shows students choosing their own topics.

**2.2 One student at a time, close and social** [observed, secondary] (memoir, era 1977 onward)
- "Roger rarely had more than one PhD student at a time, allowing him to build supportive working relationships with them and, when interests combined, engage with them socially. Many went hillwalking with him, and Womersley recalls their weekly games of squash." (memoir p. 138)
- Era and resources: a university NA group in a small city, with one senior supervisor and no large team. Funding came from the ECOSSE project from 1988 and EPSRC grants in the 1990s (§3.3).

**2.3 Programming skill as the precondition for supervising** [stated, primary] (Optima 99, p. 4, 2015, aged about 76)
- Asked about the role of software, he said: "Yeah, be a good programmer. Now if you give an idea to a Ph.D. student and it doesn't work, you have no idea why he thinks it doesn't work." Then: "Whether it was a poor idea or maybe it was a good idea but his program has a bug in it. Maybe he's not a very good Fortran programmer."
- [inferred] A negative result from a student is not evidence until the advisor can reproduce it in his own code. That fits his habit of implementing competitors' methods himself (see 02-methodology.md §4.2).

**2.4 The MSc-project episode: a supervision failure he told against himself** [stated, primary] (Optima 99, p. 2; the event is early 1980s, going by the 1981 and 1985 SDP-type papers in the memoir, items 20 and 25)
- "In those days we used to have three-month M.Sc. projects, and I had two or three of them, I can't remember whether it was 2 or 3. And I got the student to solve these educational testing problems, which are SDPs, which have matrix constraints, matrix variables, and to solve them by BFGS or SQP or something, It always converged slowly, and I'd just give them to another guy to do. I just though [sic] they weren't very good students. But it was only after the third one that I realized that it was something to do with nondifferentiability of eigenvalue constraints, and then you suddenly start to realize what's going on."
- [inferred] This is the negative case behind 2.3. He blamed students' slow convergence on the students for two or three projects before recognising a structural cause in the problem (nonsmooth eigenvalues). The same problem class turned into his early papers "A Nonlinear Programming Problem in Statistics (Educational Testing)", *SIAM J. Sci. Stat. Comput.* 2:257-267, 1981, DOI 10.1137/0902021, and "Semi-Definite Matrix Constraints in Optimization", *SIAM J. Control Optim.* 23:493-513, 1985, DOI 10.1137/0323032. [inferred] That the MSc projects fed these papers is my reading of the timing; Fletcher does not say so. Short MSc projects worked as cheap, repeated probes of a hard problem.

**2.5 Students worked on components of his own codes** [practice; observed, secondary]
- Paul Matthews: the stable LU update "was the foundation of Roger's computational work for a while" (memoir p. 138).
- Julian Hall: to solve a batch-plant model, "Julian wrote a solver for convex MINLP problems", which "motivated more work on Roger's LP solver blpd (34), with Julian improving its computational efficiency by developing its sparse numerical linear algebra routines" (memoir p. 139).
- Sven Leyffer's thesis runs on Fletcher's QP code. "The LP and QP solver that underlies this thesis is an implementation of a primal ASM with the additional feature of handling degeneracy." (Leyffer thesis, p. 22) [practice, primary]. Its test chapter names the solver: "The individual LP/QP problem is solved using bqpd [18] which resolves degeneracy and has a guaranteed termination even in the presence of round-off errors." (p. 76)
- Choong Ming Chin: joint NA reports NA/199 and NA/202 (2001) and a single-author report, "Chin C.M., Numerical results of SLPSQP, filterSQP and LANCELOT on selected CUTE test problems, Dundee Numerical Analysis Report NA/203, 2001" (homepage report list; report **not read**) [practice, primary record]. [inferred] The student's solo item is a benchmarking report comparing the group's codes with LANCELOT.
- Leyffer on the design of bqpd, which made this kind of plug-in work possible: "The QP solver relies on a matrix algebra "class" that implements the factorization of the basis matrix. Roger provided both dense and sparse instantiations of this "class" and opened the possibility for other classes – for example, for people wishing to exploit the structure of their problem." (SIAM News 2016) [observed, secondary]
- [inferred] A student entered the group by owning one layer of a shared Fortran stack (factorization updates, sparse ordering, the QP inside a MINLP loop, an SLP variant). The student's thesis then reported on that layer honestly (§6.3).

**2.6 From student to research fellow to peer: the Leyffer track** [practice, primary; observed, secondary]
- The homepage (text of 2001, kept in the 2017 copy) says: "Much of my recent work has been in conjunction with a research fellow Sven Leyffer." [stated, primary]
- The filter idea came "in a collaboration with, his now postdoc, Sven Leyffer" [sic commas] (memoir p. 139). Theory followed with a third party: "A variant of this was then subjected to a formal proof of convergence in a collaboration with Philippe Toint (50)." (p. 139)
- The collaboration continued after Leyffer left for Argonne, through MPECs (2004, 2006) and the nonmonotone filter (2012). Leyffer interviewed him in 2015, wrote the SIAM News obituary in 2016, chaired the EUROPT 2017 memorial session and commented on the memoir draft.
- [inferred] The PhD was the start of a working relationship that lasted about 22 years, not a handover. Leyffer took over the public voice, the photos and the stories. That is also a caution: much of what is "known" about Fletcher's supervision comes from one student.

**2.7 How he counted and credited students** [stated, primary; observed, secondary]
- The Q18 answer (1.1) counts students by joint papers.
- He named students when describing results: "And that was Fletcher and Sainz de la Maza (he'was [sic] a PhD student)" (Optima 99, p. 4). On the BB cycling example: "Yuhong Dai answered it, I checked the results." (p. 4)
- One loss he mentions: "And I had a student working on it then, and the student never published anything on it, went in industry and never wrote it up, so I never got a paper out of that." (p. 3, on early SQP)

---

## 3. Group habits and group culture

**3.1 Dundee: an MSc that fed the PhD pipeline** [observed, secondary] (memoir p. 138; era 1970s-80s)
- "The Dundee numerical analysis and programming MSc attracted graduate students eager to learn from the stars of the department such as Roger, who taught courses on numerical linear algebra and optimization. This programme attracted many of Roger's graduate students, and when his first notable PhD student, Robert Womersley, arrived in 1977, studying its courses was almost compulsory."
- [inferred] The group's shared foundation was taught linear algebra and optimization, not an apprenticeship in a particular theory. That matches the linear-algebra-heavy student topics (LU updates, sparse orderings, factorizations).

**3.2 The Dundee conference and the house on Errol Road** [observed, secondary]
- "Both Mary and Roger were extremely gracious hosts, and a long sequence of who's who in numerical analysis made the short trip from West Park Hall conference centre to their house in Errol Road at conference time." (memoir p. 133)
- Toint, as a PhD student at the June 1975 Dundee conference: "the warm welcome in the optimizer's community of the time was a determining factor in my option to continue research in this area." He names Fletcher as "the "optimization host" of the conference". Then: "Roger immediately struck me by his openness, honesty, and unassuming attitude towards young lads like me. I remember in particular watching the Wimbledon finals at his home where he and his wife Mary had very kindly invited me." (Optima 99, p. 6)
- Context [observed, secondary]: Higham (blog, 30 June 2015) says the conference stayed at Dundee until 2007 and moved to Strathclyde in 2009, and that the 2015 meeting introduced a "Fletcher-Powell Lecture". I read only that blog excerpt, not Watson's history of the conference (see Gaps).

**3.3 Funding and the Edinburgh link** [stated, primary; observed, secondary]
- Homepage (c.2001): "The optimization group at Dundee has been associated with researchers in Mathematics and Chemical Engineering at Edinburgh University as part of the ECOSSE project since about 1989. To follow up this work, the EPSRC has funded (from 1996-99) a reseach [sic] project jointly with myself and researchers Ken McKinnon (Maths) and Bill Morton (Chem. Eng.) at Edinburgh." He also mentions an EPSRC grant for the MPEC work and "informal collaborations with John Mackenzie and others at Strathclyde".
- Memoir: "ECOSSE also brought healthy funding for Roger's doctoral and postdoctoral researchers, and Julian Hall was the first to benefit." (p. 139). It dates ECOSSE's inception to 1988 (p. 138); the homepage says "since about 1989".
- The only other student acknowledgement I found shows the link at work. Grothey's Edinburgh thesis (2001): "I would like to thank my supervisor Ken McKinnon for all the support he gave me during the research done on this thesis and for his many helpful comments while writing this thesis. I also would like to thank Sven Leyffer, Roger Fletcher and Bill Morton for many helpful discussions" (p. IV) [primary, practice of the group; secondary as evidence about Fletcher].
- Leyffer: "Roger later worked closely with the School of Chemical Engineering at the University of Edinburgh." (SIAM News 2016)
- [inferred] From 1988 the group's problems came from a funded engineering partner. Students were paid from that partnership and worked on its models (batch plants, flowsheets, distillation columns). This is the period of MINLP, then filters.

**3.4 Report series and code licensing as group infrastructure** [practice, primary]
- The homepage (2017 copy) lists 23 Dundee NA Reports (NA/149 to NA/223, 1993-2005), including ones co-authored with students and fellows (Leyffer, Grothey, Chin, Dai). Leyffer's thesis cites its own joint report as "Numerical Analysis Report NA/141 (to appear in Mathematical Programming) (1992)" (thesis bibliography, item 19). Results circulated as group reports before journal publication.
- Codes were licensed out: "Licences to use any or all of these codes are available at very modest cost, particularly for academic and non-commercial users." (homepage) [stated, primary]. [inferred] Students' code contributions (for example Hall's sparse routines in blpd) went into products the group distributed.

**3.5 The earlier Harwell culture (1969-73), which he joined as a young researcher** [observed, secondary]
- "Such was the competitive culture, there were significant additions to the library in almost every month in 1972, alternating between Mike and Roger, like a good game of tennis. By all accounts, work was taken to the Harwell canteen every day for friendly but provocative discussions over lunch that frequently ended up as published papers." (memoir pp. 133-134)
- The memoir also says: "It is notable, in passing, that Roger did not publish much with his immediate colleagues during his time at Harwell." And: "But Roger's software output via the Harwell Subroutine Library was prolific." (p. 135). See Contradiction C5.
- Era and resources: a government laboratory with a shared subroutine library (HSL) and an internal user base. The "product" was library software rather than students.

**3.6 Hills as the informal seminar room** [observed, secondary; stated, primary]
- "He was always delighted to have visitors, particularly those he could entice into the hills. Each new Munro turned equally into a mathematical journey: Roger delighted in telling his companions interesting facts about the number of the hill they were ever so slowly ascending." (memoir p. 141)
- Toint: "a climb of the Lochnagar peak along with him, Michael Powell and a Thai fellow student, as well as climbing another Munro in the mist with Nick Gould and him" (Optima 99, p. 6).
- Leyffer's Powell story: "So Mike cleverly asked, "Roger, tell me about the proof of the conjugate gradient method" – and deftly managed to catch up with an out-of-breath Roger." (SIAM News 2016)
- Fletcher on Powell and Davidon: "I enjoyed the company of both of them, and remember many happy outings on the hills in Scotland." (Dai interview Q5) [stated, primary]
- Photos: Fletcher and Leyffer on Meall Glas (Optima 99, p. 3); "Nick Gould, Roger Fletcher and Sven Leyffer in the Scottish Highlands, 2007" (memoir p. 142).
- [inferred] Long walks were where junior people got extended time with him. The sources do not show research problems actually being settled on the hills.

---

## 4. Collaboration patterns (how work was shared)

**4.1 Pool experience, then theory; implementer plus extractor** [stated, primary]
- DFP: "Mike was able to extract the essential feature that was involved. We pooled our experience and added some more theory, leading to the DFP paper." (Dai Q3). The collaboration started by accident: "He found that I was also working on the method, hence the subsequent cooperation. I didn't know Mike previous to that." (Q4). Leyffer's version: "When Mike gave his seminar, he found that Roger already knew about Davidon's then-new method and even had a working code." (SIAM News)

**4.2 Algorithm and code first, a theory partner for the proof** [observed, secondary]
- Toint: "Although I had the pleasure to co-author a couple of papers with Roger on convergence theory for filters, I always felt that his real interest was in algorithm design, making sure a particular problem could be solved efficiently and reliably." (Optima 99, p. 6)
- See 01-publications.md for the sequence: filterSQP code and report first, then the proofs with Toint and with Gould, Toint and Wächter.

**4.3 Division of labour with a visitor: the visitor proves, he checks** [stated, primary]
- On the projected-BB cycling question: "Nobody knew whether it cycled or not or whether you had to have a line search, And we answered in the affirmative, or I should say, Yuhong Dai answered it, I checked the results." (Optima 99, p. 4)
- The memoir calls Dai's visit "a vital catalyst" (p. 140).

**4.4 Colleagues nudging him to publish, or implementing his ideas without publishing** [stated, primary]
- Wolfe's degeneracy method: "except Margaret Wright used to tell me she thought it was a great idea and I should publish it; and I published it just recently [41, 42]. I eventually wrote it up. It's in our BQPD solver." (Optima 99, p. 4). The paper: "On Wolfe's Method for Resolving Degeneracy in Linearly Constrained Optimization", *SIAM J. Optim.* 24, 2014, DOI 10.1137/130930522.
- Leyffer tells him that Steve Wright had implemented Sl1QP with slacks and had "very good results with it. I don't think that work was published . . ." (Optima 99, p. 3; Leyffer speaking).
- Michele Benzi at CERFACS gave him references on implicit LU factors: "he gave me lots of references to it in the past, none of which has caught on. Mine has added to it as another one that has not caught on." (p. 4)
- [inferred] His "publish" signal often came from outside. Techniques lived in the code (bqpd) for years before he wrote them up. For a student this meant the group knowledge sat in the Fortran, not in the papers.

**4.5 Borrowing ideas from people and saying so** [stated, primary]
- "So I had two huge good ideas given to me by people, so I got this undeserved reputation for being intelligent." (Optima 99, p. 2; also in the talks notes file)
- "Mike Powell introduced me to it a long time ago, I've never discovered any of these things myself." (p. 4, on Wolfe's method)
- Against this, see Contradiction C3 (Nocedal: "He tried to derive things himself rather than relying on the literature").

---

## 5. Tacit knowledge: what his students and colleagues knew that the papers do not say

Each item gives who reports it. All are secondary unless marked.

| # | Tacit rule | According to (source) | Tag | Era |
|---|---|---|---|---|
| T1 | **Look at examples.** A small example is the first test of any claim | According to Leyffer: "So, I know when I was in Dundee, one of the things you always told us was to look at examples" (Optima 99, p. 4). Fletcher: "Part of it, yeah." Leyffer again (SIAM News): he "valued simple examples to expose a method's limitations", citing the 2005 BB counterexample with Dai | observed (student), confirmed by Fletcher [stated] | Dundee, c.1990-94 (Leyffer's PhD years) |
| T2 | **Single precision as an instability detector.** Keep a single-precision build, because trouble shows there first | According to Leyffer (SIAM News): the solvers "supported both single- and double-precision arithmetic, because numerical difficulties manifested themselves first in the single-precision version." According to the memoir, he used single precision "also as a signal of inherent instability when developing methods (Leyffer 2015)" (p. 138). **Fletcher himself later disowned it** (see C6) | observed | 1990s (bqpd, released 1995 per the homepage) |
| T3 | **Build linear algebra as a swappable "class" inside Fortran 77** (dense and sparse versions of the same interface), so users and students can plug in structure | According to Leyffer (SIAM News) | observed | 1990s |
| T4 | **Software is the check on theory.** He "believed that software validates theory and is simultaneously a guide to good methods" | According to Leyffer (SIAM News); Nocedal: "the programmer who knew how to get the numerics right" (Optima 102) | observed | whole career |
| T5 | **Robustness to floating point comes before sparsity and speed** | According to the memoir: "Of paramount importance was his insistence that the methods he proposed should be robust to floating-point computation. Of lesser importance initially to Roger was the issue of methods being computationally efficient for sparse problems." (p. 137) | observed (written by his student Hall and collaborator Gould) | 1970s-90s |
| T6 | **Distrust textbooks, and your own opinion too** | According to Leyffer (SIAM News): "Throughout his career, Roger distrusted textbooks." And: "However, Roger was just as suspicious of his own opinion, and not above changing his own mind." Fletcher's own version: "So after that I developed a great suspicion of what people were writing in books." (Optima 99, p. 2) [stated] | observed + stated | from his PhD (1960-63) on |
| T7 | **Simple arguments and short proofs** | According to Leyffer: "Roger was what Americans would call a no-nonsense applied mathematician who believed in simple arguments and proofs." (SIAM News). Fletcher's advice to PhD starters: "don't write convergence proofs that are 30 pages long. Make it so that I can understand it. What works for me is to keep the notation as simple as possible." (Optima 99, p. 5) [stated] | observed + stated | late career statement |
| T8 | **Spend time on notation early.** "If I am working through something, I think there is better notation that would serve, I would spend time changing the notation to make the rest of the project easier." | Fletcher (Optima 99, p. 5) [stated, primary]. No student report of this habit was found | stated only | 2015 |
| T9 | **Few references; derive it yourself** | According to Nocedal: his papers "contained very few references (to the consternation of some). He tried to derive things himself rather than relying on the literature, and this gave his famous textbook a unique flavor." (Optima 102, p. 6) | observed (peer, not student) | whole career |
| T10 | **Real problems from engineers outrank test libraries** | Fletcher: "I'd much rather get my problems from the people who have problems to solve, rather than taking them from a library of test problems." (Optima 99, p. 5) [stated]. Leyffer (SIAM News): "He believed that the problems people want to solve should ultimately drive applied mathematics research". Toint (Optima 99, p. 6) supports it but adds that CUTE(st) "remain absolutely crucial for tuning, comparison and standardization" | stated + observed | 1988 onward (ECOSSE) |
| T11 | **Degeneracy: make near-degeneracy exactly degenerate and resolve it (Wolfe's method), do not perturb** | Fletcher (Optima 99, p. 4) [stated]. He reports that users such as Leyffer tell him it works in MINLP codes. No student account of learning this was found | stated | bqpd era, written up 2014 |
| T12 | **Report failures of the group's own code in the thesis** | Leyffer's thesis records bqpd's failures (see 6.3) [practice, primary] | practice | 1993 |

---

## 6. How he treated juniors and critics, and what students did with their own results

**6.1 Critics of his code** [observed, secondary]
- Curtis: "For one of my first visits to a university overseas, Roger came down from Dundee to Edinburgh to attend my talk and, as it turned out, to chat with me on the side for a few minutes during the reception after the seminar. Especially after I spoke critically in my talk about the performance of one of his codes on a certain class of problems, one might think that the experience could have been quite intimidating for me! But with Roger the experience was nothing but a pleasure, and I can say without hyperbole that it will remain one of the most memorable conversations of my career." (Optima 99, p. 7). Date not given; Curtis's PhD was at Northwestern (team.json), so [inferred] mid-to-late 2000s.

**6.2 A junior who pushed back as referee's target** [stated, primary; observed, secondary]
- Fletcher: "Yuhong Dai [50] wrote a paper about Barzilai-Borwein and I was the referee, and I said this paper was of no interest – something along those lines. And then he wrote back and said, "Have you seen the paper of Marcos Raydan [51], where he is solving problems with 10^6 variables with this method." The original paper solves a two-variable problem, you see. So that's a case where I changed my mind." (Optima 99, p. 4)
- Leyffer: "When he refereed a paper by the young Dai on the Barzilai-Borwein method, he initially rejected the idea as useless. Luckily, Dai persisted; eventually Roger not only changed his mind but also coauthored a number of papers with him [1-3]." (SIAM News)
- Homepage (c.2001-05) [stated, primary]: "Most recently I have become interested (again!) in the Barziliai-Borwein [sic] method, having been impressed by the recent numerical work of Marcos Raydan and others, and having benefitted from discussions with Yu-Hong Dai."
- [inferred] What changed his mind was numerical evidence at scale (Raydan's large problems), not a better argument about the two-variable case. That is consistent with T1 and T4. The junior won by pointing to numbers.

**6.3 What a student's thesis looked like: honest about the advisor's solver** [practice, primary] (Leyffer thesis, December 1993)
- "There are no results for the quadratic outer-approximation code for the problems BATCH, GTD and GTD chain(3). This is due to severe growth of round-off error in the reduced Hessian matrix that can affect the QP solver bqpd. The solve for BATCH was aborted after more than an hour without obtaining a solution and the solves for the GTD problems were so inefficient that it was felt that they would otherwise distort the results. It is anticipated that this problem will be remedied in a future release of bqpd." (p. 78)
- Comparisons adjusted for solver reliability: "While bqpd resolves degeneracy, the QP solver of the NAG library that underlies the NLP solver has no facility to detect or handle degeneracy and is consequently cheaper than bqpd. On one very large example, the NLP solver fails to find a feasible point of the linear constraints, due to degeneracy, while bqpd has no difficulty to locate a feasible point. The different degrees of reliability of the solvers should be kept in mind when comparing the results of the experiment and it is preferred to compare the routines by looking at the number of LPs and QPs solved." (p. 79)
- Worst-case example as a driver of the next method (T1 in practice): "A worst case example has been presented for which outer approximation visits all feasible integer assignments in turn before finding the solution. This behaviour has been explained by the failure of outer approximation to take curvature information into account and has motivated the introduction of second order term into the master program" (Ch. 9 Conclusions).
- The student's own voice on how a topic grew: "The introduction of MIQP master programs in Chapter 5 caused me to become interested in MIQP problems" (Synopsis, pp. 14-15).
- [inferred] The thesis shows three group habits in a student's hands: counting work in solver-independent units (LPs and QPs solved), not CPU time, when solvers differ in reliability; printing the failures of the home code; and using a constructed worst case to motivate the next algorithm. I cannot tell from this one thesis whether Fletcher required these habits or Leyffer brought them.

**6.4 Juniors at conferences** [observed, secondary]
- Toint's 1975 account (3.2). Curtis's account (6.1). Curtis on the interview's lesson for juniors: "(4) be critical of your own work, and reexamine it even after it's done. If you look over Fletcher's career, then you can see that this isn't just idle talk, but advice that he has followed himself." (Optima 99, p. 7)
- Curtis also resists Fletcher's self-deprecation: "He may claim that some of these accomplishments were about being in the right place with the right collaborators at the right time, but shame on us if we believe that such a thing can happen merely by chance so often within a single career." (p. 7)

**6.5 His own account of reaching industry partners, which he says he was bad at** [stated, primary] (Optima 99, p. 5)
- "I think you perhaps look around and you see something that you think might benefit from optimization, and you go and bug somebody or go and read some papers in that area and see if there is anything you think you could contribute. And then if you've got the enthusiasm and the personality, you go and try and sell yourself to them. Things I am not very good at."
- [inferred] In practice the ECOSSE partnership (Ponton, Johns, Morton, McKinnon), not self-promotion, supplied the industrial problems for his students.

---

## 7. Failures, lost work and abandoned directions in the mentoring record

| Date | What was lost or went wrong | Evidence | Tag |
|---|---|---|---|
| 1967-69 | His first PhD student's supervision was interrupted by his move to Harwell | "although he left Leeds for Harwell before she had graduated" (memoir p. 132) | observed, secondary |
| 1970s | A student's early-SQP work was never written up | "the student never published anything on it, went in industry and never wrote it up, so I never got a paper out of that." (Optima 99, p. 3) | stated, primary |
| early 1980s | Two or three MSc projects on SDP-type problems "failed" and he blamed the students before seeing the cause (nonsmooth eigenvalues) | Optima 99, p. 2 (§2.4) | stated, primary |
| c.1990 | Zoppke-Donaldson's "tolerance tubes" work, described as a precursor of filters, was never published | memoir p. 139 | observed, secondary |
| 1993 | bqpd failed on BATCH and GTD in Leyffer's quadratic-OA experiments (round-off growth in the reduced Hessian); the fix was deferred to "a future release" | Leyffer thesis, p. 78 | practice, primary |
| 1990s-2014 | The Wolfe degeneracy technique lived in bqpd for years and was published only after Margaret Wright's urging | Optima 99, p. 4; SIAM J. Optim. 24, 2014, DOI 10.1137/130930522 | stated, primary |
| 1990s | A colleague's Sl1QP implementation with good results went unpublished (reported by Leyffer, attributed to Steve Wright) | Optima 99, p. 3 | observed (Leyffer, reporting Wright) |
| c.2000 | His first reaction as referee to Dai's BB paper was to reject it; he reversed later | Optima 99, p. 4; SIAM News | stated + observed |
| 2015 | He disowned the single-precision practice his students remember (T2) | Optima 99, p. 5 | stated, primary |

---

## 8. Era and resource context of the practices above

- **Leeds, 1960-69.** An early computing laboratory (Ferranti Pegasus, paper tape). A supervisor-plus-student pair. Ideas came from the supervisor and chance reports; the student wrote the code (Dai Q2-Q3; Optima 99, pp. 1-2). His first MSc and PhD students came from this setting: Bradbury, McCann, Lill, Hebden.
- **Harwell, 1969-73.** A government lab with the Harwell Subroutine Library as its output, a daily lunch-discussion culture and a competitive exchange with Powell (memoir pp. 133-135). He had few co-authored papers there and a lot of library software. Hebden followed him from Leeds. Jackson (Oxford) collaborated on a code.
- **Dundee, 1973-2005.** A strong small NA group and a taught MSc feeding PhDs. Usually one PhD student at a time. From 1988, ECOSSE and EPSRC money paid doctoral and postdoctoral researchers and brought chemical-engineering problems. Results went out as NA reports and licensed Fortran codes (bqpd 1995, then filterSQP and the MINLP code). Hospitality around the biennial conference.
- **Retirement, 2005-16.** Emeritus. Work with visitors and former students (Dai, Leyffer, Shen) and single-author papers. Invited surveys "as an elder statesman" (memoir p. 141). The 2009 LMSD preprint went out through Edinburgh's ERGO series (02-methodology.md). The 2015 interview and the 2017 memorial session (EUROPT, Montréal, chaired by Leyffer, with a talk by Dai on "A Penalty-Free Method with Superlinear Convergence for Equality Constrained Optimization") show the network in his last years and after his death.
- [inferred] **Limits on transfer to a modern solver team.** One senior person, one student at a time, all code in Fortran 77 written or reviewed by him. Much of the tacit knowledge (T2, T3, T11) lived in the code rather than in documents. A present-day group with many students, version control and continuous benchmarking would need to write down what his group transmitted by proximity.

---

## Contradictions (kept, not reconciled)

- **C1 (how many students).** Fletcher: "I don't keep records on this" and a 15-name list of students "with whom I have published joint papers", including two MSc students (Dai Q18). Mathematics Genealogy Project: five PhDs. Memoir: "Roger rarely had more than one PhD student at a time" (p. 138). Leyffer: "his many Ph.D. students" (SIAM News). Griffiths and Watson: he "supervised many students and research fellows who went on to make their own major contributions" (NA Digest 2016). These are compatible over about 40 years, but the sources count different things.
- **C2 (Mike Jackson's status).** Fletcher lists "Mike Jackson" among his students (Q18). The memoir describes "a collaboration with Mike Jackson from Oxford" (p. 136). Left open.
- **C3 (where his ideas came from).** Fletcher: "I had two huge good ideas given to me by people" (Optima 99, p. 2) and "I've never discovered any of these things myself" (p. 4). Nocedal: "He tried to derive things himself rather than relying on the literature" (Optima 102). Curtis: "shame on us if we believe that such a thing can happen merely by chance so often" (Optima 99, p. 7). Toint calls his downplaying "far too modest" (p. 6). Kept as the subject's view against his peers' view.
- **C4 (Grothey's place).** Memoir: Grothey's arrival in 1994 "further enhanced Roger's research team" (p. 139). Grothey's Edinburgh thesis names Ken McKinnon as supervisor and thanks Fletcher, with Leyffer and Morton, "for many helpful discussions" (p. IV). A member of the wider ECOSSE team rather than his PhD student, going by the thesis.
- **C5 (Harwell collaboration).** The memoir says lunch discussions at Harwell "frequently ended up as published papers" (p. 134), then that "Roger did not publish much with his immediate colleagues during his time at Harwell" (p. 135). Both come from the same text.
- **C6 (single precision).** Leyffer (2015, 2016) and the memoir present single-precision builds as a deliberate instability detector (T2). Fletcher in 2015: "It was a sort of misapprehension on my part that I thought it might be a good idea. I don't believe it anymore; I wouldn't write in single precision now. In fact I would rather go the other way." (Optima 99, p. 5). His reasons there are LP failures and hardware speed ("I think architectures are optimized to double precision"). The detector rationale his student remembers is not the rationale he gave. Kept as a student-memory against self-account contradiction.
- **C7 (dates in the record).** Lagrange Prize: 2006 per the Optima 73 citation (January 2007), Leyffer's SIAM News obituary and the NA Digest notice; 2012 per the memoir (p. 139). RSE Royal Medal: 2008 per the memoir (p. 140) and the Courier; 2011 per the NA Digest notice. Leyffer's PhD: the thesis title page reads "December 1993", the Mathematics Genealogy Project gives 1994 and the memoir says the work "yielded Sven's PhD in 1994". ECOSSE start: 1988 (memoir) against "since about 1989" (homepage). Morton paper: 1999 (memoir) against 2000 (Crossref). Date of death: 15 July 2016 in the memoir title; the memoir text says he set off on 5 June and a police-dog team found his body on 15 July (p. 142); the Courier (16 July 2016) says he was reported missing on 5 June and his body was found "on Friday afternoon".
- **C8 (co-author lists).** Memoir bibliography item 51 lists Wächter as a co-author of the trust-region SQP-filter paper. Crossref metadata for DOI 10.1137/s1052623499357258 lists Fletcher, Gould, Leyffer and Toint. Not resolved here.
- **C9 (name spellings).** "Chenxian Xu" (Dai Q18) against "Chengxian Xu" (MGP, memoir). "Eric Chin" (Q18) against "Choong Ming Chin" (homepage 2017 copy) and "Choong Minh Chin" (homepage 2001 copy). I infer one person in each case but did not verify it.

---

## Gaps (what I could not find or read)

- **No first-person recollection by any student except Leyffer**, and Hall only as co-author of the memoir. Nothing found from Womersley (the memoir cites his memory of squash games but gives no source), Al-Baali, Xu, Sainz de la Maza, Al-Homidan, Chin, Lill/Carter, Sinclair or Matthews. The memoir's claims about supervision partly rest on Leyffer (its acknowledgements, p. 143).
- **Thesis acknowledgements of his own PhD students: none read.** The web copy of Leyffer's thesis has no acknowledgements page. Womersley (1981), Al-Baali (1984), Xu (1987), Hall (1992) and Chin (c.2001) theses were not located online. The Dundee Discovery portal returned a Cloudflare challenge, and I did not try the British Library's EThOS. Only Grothey's Edinburgh thesis, where Fletcher is not the supervisor, was read.
- **Group meetings, how he gave feedback on drafts, how topics were assigned, how long students took**: no evidence found. Layer 7 detail below "one student at a time" and "socialised on the hills" is missing.
- **Alistair Watson's 2006 history of the Dundee conference** (linked from Higham's blog at maths.dundee.ac.uk/~gawatson): the Dundee host is blocked by the egress policy and no Wayback copy was found. **Not read.**
- **The unpublished 2003 text cited by the memoir** for Reeves's influence (p. 131): not identified, not read.
- **Christine Zoppke-Donaldson's "tolerance tubes"** and **Frank Plab**: nothing beyond the memoir's sentence.
- **EUROPT 2017 memorial session**: only the schedule and abstracts were read. None of the three talks is about Fletcher himself, and no slides or recording were found.
- **The memoir's full bibliography** (electronic supplementary material, DOI 10.6084/m9.figshare.c.7754595): **not read**. It might settle C8 and list more student papers.
- **Chin's report NA/203** (2001) and the joint Chin reports NA/199 and NA/202: titles only (homepage), **not read**.
- **The SIAM News web page** (siam.org, 403) and the NAO-IV proceedings front matter (Springer, JavaScript challenge): not reached. The SIAM News text was read from the Wayback copy of the December 2016 print PDF instead.
- **Yu-Hong Dai's own reminiscence**, if one exists (for example in Chinese-language society newsletters): not searched, for lack of WebSearch budget.
- **Where the Optima 99 interview was recorded.** Leyffer says "somebody at this meeting" and "what you talked about at the conference" (p. 4), and reference [52] of the issue links to Hall's EUROPT 2015 page. [inferred] EUROPT 2015 in Edinburgh, not confirmed.

**Notes for other research files (not edits):**
1. 02-methodology.md lists as unverified a SIAM News wording about a "no-nonsense applied mathematician who believed in simple arguments and proofs". That wording is now verified from the December 2016 print PDF (T7).
2. The Dai interview is cited by the memoir as *Pac. J. Optim.* 2 (2006) 1-10, which dates the Kyoto web copy.
3. The Gould and Hall memoir full text can be reached through the Wayback snapshot of the open-access PDF (2 August 2025).

---

## Sources

1. N. I. M. Gould, J. A. J. Hall, "Roger Fletcher. 29 January 1939—15 July 2016", *Biographical Memoirs of Fellows of the Royal Society* 78:127-146, 2025, DOI 10.1098/rsbm.2024.0037, CC-BY 4.0. Full text read from http://web.archive.org/web/20250802143012/https://royalsocietypublishing.org/doi/pdf/10.1098/rsbm.2024.0037. Secondary (student and collaborator account; relies partly on Leyffer and Dai).
2. S. Leyffer, "Obituaries" (Roger Fletcher), *SIAM News* 49(10), December 2016, p. 2. Read from the Wayback copy of https://sinews.siam.org/Portals/Sinews2/Issue%20Pdfs/sn_December2016.pdf (snapshot 13 May 2024). Web version: https://www.siam.org/publications/siam-news/articles/obituary-roger-fletcher/ (403, not read). Secondary (former student).
3. S. Leyffer (interviewer), "It's to Solve Problems – An Interview with Roger Fletcher", *Optima* 99, December 2015, pp. 1-5, https://www.mathopt.org/optima/99/optima_99.pdf. Primary (Fletcher's words); Leyffer's own recollections in it are secondary.
4. Ph. L. Toint, "Impressions of Roger's Interview", *Optima* 99, December 2015, p. 6 (same PDF). Secondary.
5. F. E. Curtis, "Young Researchers Would Be Wise to Read this Interview!", *Optima* 99, December 2015, pp. 6-7 (same PDF). Secondary.
6. J. Nocedal, "Roger Fletcher (1939–2016)", *Optima* 102, April 2017, p. 6, https://www.mathopt.org/optima/102/optima_102.pdf (the mathopt.org issue index lists it as "Obituary for Roger Fletcher"). Secondary.
7. Y.-H. Dai, "An Interview with Roger Fletcher", *Pac. J. Optim.* 2 (2006) 1-10 (citation as given in the memoir's reference list); read at http://www-optima.amp.i.kyoto-u.ac.jp/ORB/issue22/flectcher_interview.html. Primary.
8. D. Griffiths and A. Watson, "Roger Fletcher (1939-2016)", NA Digest 16(27), 18 July 2016 (message dated 17 July 2016), https://na-digest.coecis.cornell.edu/na-digest-html/16/v16n27.html. Secondary (Dundee colleagues).
9. M. Mackay, "Tributes paid to Professor Roger Fletcher", *The Courier*, 16 July 2016, https://www.thecourier.co.uk/fp/education/higher-education/223875/tributes-paid-professor-roger-fletcher/ (read from the Wayback snapshot of 21 February 2026). Secondary (press; quotes F. Davidson).
10. R. Fletcher, Dundee staff homepage, Wayback snapshots of 28 April 2001 (http://www.maths.dundee.ac.uk:80/~fletcher/) and 11 March 2017 (http://www.maths.dundee.ac.uk:80/~fletcher/index.shtml; content c.2005). Primary.
11. S. Leyffer, *Deterministic Methods for Mixed Integer Nonlinear Programming*, PhD thesis, Department of Mathematics & Computer Science, University of Dundee, December 1993, https://www.mcs.anl.gov/~leyffer/papers/thesis.pdf. Primary (student's practice).
12. A. Grothey, *Decomposition Methods for Nonlinear Nonconvex Optimization Problems*, PhD thesis, University of Edinburgh, 2001, https://era.ed.ac.uk/handle/1842/12065 (text bitstream read). Primary for the acknowledgements.
13. Mathematics Genealogy Project, "Roger Fletcher", id 52148, https://www.mathgenealogy.org/id.php?id=52148 (page saved by another agent in this run and read by me). Secondary record.
14. EUROPT 2017 (15th EUROPT Workshop, Montréal, 12-14 July 2017), session "In Memory of Roger Fletcher: Nonlinear Optimization and Control", 13 July 2017, https://symposia.gerad.ca/europt2017/en/schedule?slot_id=1115 (read from the Wayback snapshot of 17 December 2025; the live page returns 404). Secondary record.
15. "The Lagrange Prize", *Optima* 73, January 2007, p. 2 (prize citation for Fletcher, Leyffer and Toint). Read from the copy saved by another agent in this run. Secondary (used for the prize date).
16. N. J. Higham, "50 Years of the Biennial Conference on Numerical Analysis", 30 June 2015, https://nhigham.com/2015/06/30/50-years-of-the-biennial-conference-on-numerical-analysis/ (excerpt on the Fletcher-Powell Lecture and Watson's history). Secondary.
17. Crossref metadata checked in this run for 33 DOIs, most of them cited in §1, §2.4 and §4; the last two (Fletcher & Johnson, SIAM J. Matrix Anal. Appl. 1997; Fletcher, SIAM J. Optim. 2012) were checked for the ECOSSE-era and retirement-era context only (10.1007/bf02162089, 10.1137/0902021, 10.1137/0323032, 10.1007/bf00940574, 10.1007/bf02591933, 10.1007/bf00940566, 10.1093/imanum/7.3.371, 10.1007/bf01582292, 10.1016/0098-1354(91)80029-u, 10.1007/bf02025533, 10.1007/bf01581153, 10.1137/s1052623494268455, 10.1007/s10107-003-0378-6, 10.1007/bf00935247, 10.1007/978-1-4612-1960-6_3, 10.1007/s10589-011-9430-2, 10.1142/9789812812827_0001, 10.1093/imamat/14.2.159, 10.1016/b978-0-12-597050-1.50007-5, 10.1016/0021-9045(74)90097-5, 10.1137/0711013, 10.2307/2008137, 10.1137/130930522, 10.1137/s105262340038081x, 10.1137/s1052623499357258, 10.1137/s1052623402407382, 10.1080/10556780410001654241, 10.1007/s10107-004-0516-9, 10.1007/s00211-004-0569-y, 10.1007/s10107-005-0595-2, 10.1016/s0098-1354(00)00295-7, 10.1137/s0895479896297732, 10.1137/110844362). Bibliographic.
18. Mathematical Optimization Society, Optima issue index (https://www.mathopt.org/api/Optima/..., saved by another agent in this run), for the article titles and authors of Optima 99 and 102. Bibliographic.
