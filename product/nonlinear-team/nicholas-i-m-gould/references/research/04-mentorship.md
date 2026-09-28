# 04 · Mentorship: students, collaborators and group culture (Nicholas I. M. Gould)

- **Researcher**: Nicholas Ian Mark Gould (Nick Gould), STFC Rutherford Appleton Laboratory (RAL), Visiting Professor at Oxford and Edinburgh. Living.
- **Dimension**: research agent 04 of 06, students and collaborators: supervision style, group habits, lab culture, tacit knowledge (nuwa research-craft Phase 1, framework §一 layer 7 and §二 agent 4).
- **Research date**: 2026-09-28.
- **Sources consulted**: 52 (listed under Sources, M01–M52). 46 were read in whole or in the parts cited. 6 were checked only as metadata (M11, M13, M21, M22) or were blocked or returned nothing (M51, M52); each is marked so. WebSearch calls used: 2 of 2. Neither returned anything on Gould's mentoring (the second hit a different Nick Gould, a social-work professor at Bath; the name collision is recorded under Gaps).
- **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` hold only `.gitkeep`, so there was **no user-supplied material**. `private/` was not opened.
- **Method**: I started from his CV [M01], which lists every supervision and examining role, and then looked for the other side of each relation: the student's thesis (acknowledgements), the joint papers (author order, affiliations, funding footnotes, acknowledgements), the student's or colleague's own CV or web page, and the shared code (GALAHAD and CUTEst git histories and GitHub pull requests). I also read the RAL group's own development guidelines, the Fletcher memoir Gould co-wrote, a 2026 podcast interview with Toint (saved by the Toint agent), and the scratch full texts other agents in this workflow had downloaded from public sources (Curtis's 2007 thesis, the Ipopt mailing-list archive). Every DOI below was resolved with Crossref or DataCite in this run.

**Tags.** [stated] = Gould's own words (alone or with co-authors). [practice] = what the record shows he did (papers, author order, code, commits, CV entries). [observed] = what someone else said about him. [inferred] = my reading, with no source saying it. Each item is also marked **primary** (Gould's own text or record) or **secondary** (someone else's account). Everything a student or collaborator says about Gould is secondary by definition. "p." gives the PDF page of the full text I read.

---

## 0. Read this first: what kind of mentor is Gould?

The evidence base for this dimension is **thin, and it is thin for a structural reason**:

- Gould has spent his career (Harwell 1985–90, RAL 1990 to now) in a **national-laboratory numerical analysis group, not a university department**. His only university post was Assistant Professor at Waterloo (1982–85) and Professor of Numerical Optimisation at Oxford (2006–08) [M01, primary, practice].
- He had **one formal doctoral student**: Jaroslav (Jari) Fowkes, Oxford, co-supervised with Chris Farmer [M01][M04][M05][M06]. The Mathematics Genealogy Project lists only Fowkes [M03, secondary].
- His other doctoral links are as **"External Ph.d advisor"** (seven students, 1991–2009) and **external examiner** (at least 15 theses, 1987–2018) [M01, primary]. He supervised 3 M.Sc. students at Waterloo (1982–85) and 4 Oxford MSc students in 2007 [M01].
- He says so himself, in the preface of his course booklet: "Currently we do not provide exercises. This is partially as we are not based in a university and thus lack the experience and imperative to evaluate all the time" [M02 p.vi, stated, primary].
- His travel has been limited: "(My conference talks have been somewhat limited over the past 15 years for health reasons. I have unfortunately turned down many invitations on these grounds.)" [M01 p.21, stated, primary].

So "mentorship" for Gould mostly means **three other things**: co-advising students whose main supervisor sits elsewhere; working with post-PhD collaborators and junior RAL staff; and maintaining shared software (LANCELOT, CUTE → CUTEst, GALAHAD) that other people's students build on. No student blog, memorial piece, Festschrift, lab guide written by him, interview about his supervising, or supervision advice in his own words was found (see Gaps). **Layer 7 of the skill should stay modest.**

---

## 1. The record: who worked under or beside him, and what came out

| Person | Relation (source) | Years | Joint output (checked identifier) | What the record shows |
|---|---|---|---|---|
| **Jaroslav Fowkes** | D.Phil student, Oxford, "supervised by Nick Gould and Chris Farmer" (RAL page [M05]); ORA lists both as Supervisor [M06]; EPSRC Industrial CASE studentship with Schlumberger [M07 p.7][M08] | CV: "2008 D.Phil advisor" [M01]; thesis dated Hilary Term 2011 [M07]; ORA/DataCite 2011; MGP 2012 | Thesis *Bayesian numerical analysis: global optimization and other applications* (10.5287/ora-8r80452qe); Farmer, Fowkes & Gould, "Optimal Well Placement", ECMOR XII 2010 (10.3997/2214-4609.20144994); **Fowkes**, Gould & Farmer, *J. Global Optim.* 2013 (10.1007/s10898-012-9937-9); Cartis, Fowkes & Gould, *J. Global Optim.* 2015 (10.1007/s10898-014-0199-6); Fowkes & Gould, GALAHAD 4.0, *JOSS* 2023 (10.21105/joss.04882); Fowkes, Gould & Scott, *Numer. Algorithms* 2023 (10.1007/s11075-023-01681-z) | After the D.Phil, postdoc with Coralia Cartis (EPSRC 2011–13; Emirates funding 2017–20) [M27], then RAL; now "acting Continuous Optimization group leader" [M05]. **The only student who became a long-term co-developer** [practice, primary + secondary] |
| Jean-Yves L'Excellent | External PhD advisor 1993 [M01]; thesis INPT Toulouse 1995, directed by Joseph Noailles [M17] | 1993–97 | Daydé, **L'Excellent**, Gould, "Element-by-Element Preconditioners for Large Partially Separable Optimization Problems", *SISC* 18 (1997) (10.1137/S1064827594274796) | Thesis topic: element-by-element preconditioners exploiting partial separability, the structure LANCELOT was built on [M17]. Author order breaks the alphabet (D, L, G) [practice] |
| Jérôme Décamps | External PhD advisor 1996 [M01]; thesis INPT 1997, directed by Noailles [M18] | 1996–99 | Daydé, Décamps & Gould, "Subspace-by-subspace preconditioners for structured linear systems", *Numer. Linear Algebra Appl.* 6 (1999) 213–234 (10.1002/(SICI)1099-1506(199904/05)6:3<213::AID-NLA161>3.0.CO;2-V) | Thesis on block iterative methods for partially separable structure [M18]. The 1997 SISC paper's footnote: "Travel was funded in part by the ALLIANCE program from the British Council" [M15 p.1] [practice] |
| Carsten Keller | External PhD advisor 1997 (Oxford) [M01] | 1997–2000 | **Keller**, Gould & Wathen, "Constraint Preconditioning for Indefinite Linear Systems", *SIMAX* 21 (2000) (10.1137/S0895479899351805) | One of Gould's signature KKT-preconditioning papers came out of an external-advisee thesis. Student first, out of alphabetical order. Acknowledgement thanks Gene Golub "for his insightful comments during the process of the work" [M14 p.17]. Keller's thesis: **not read** |
| Philip A. Browne | External PhD advisor 2009 (Bath) [M01] | 2009–12 | **Browne**, Budd, Gould, Kim & Scott, *IJNME* 2012 (10.1002/nme.4367) | Funded by "EPSRC ... contract grant no. EP/E053351/1 and CASE award MCA 09 - 2008/2009" [M19 p.17]; EP/E053351/1 is a grant on which Gould was CoI [M01]. Topology-optimization application. Thesis: **not read** |
| Marli Hernandez (Hatfield), Sybille Schuler (Oxford), Rob Gate (Dundee) | External PhD advisor 1991, 1991, 2000 [M01] | — | none found | Nothing beyond the CV line [practice, primary] |
| Daniel P. Robinson | Postdoc at Oxford (Lehigh bio [M24]); Oxford Mathematical Institute address on the 2010 SIOPT papers [M20 p.1] | c. 2008–10 | Gould & Robinson, *SIOPT* 20 (2010), 10.1137/080744542 and 10.1137/080744554; Gould, Robinson & Thorne, *Math. Program. Comput.* 2010 (10.1007/s12532-010-0011-7); Gould, Orban & Robinson, *MPC* 2013 (10.1007/s12532-012-0050-3); Gould, Loh & Robinson, *SIOPT* 24 (2014) (10.1137/130920599) | 2010 papers "supported by the EPSRC grants EP/E053351/1 and EP/F005369/1" [M20 p.1]; Gould was PI of EP/F005369/1, "Algorithms for Large-Scale Nonlinearly Constrained Optimization" (2007–10, £336k) [M01]. That the postdoc was on Gould's grant is [inferred]. The collaboration continued after Robinson moved to Johns Hopkins, with his student Yueling Loh [M23 p.1] |
| H. Sue Dollar (later Thorne) | Co-author; junior RAL staff member by 2006 (she co-assembled the HSL check lists [M38 p.21]) | 2006–10 | Dollar, Gould, Schilders & Wathen, *SIMAX* 2006 (10.1137/05063427X); Gould, Robinson & Thorne 2010 (above); RAL-TR-2010-013 (below) | Her Oxford D.Phil thesis and its supervisors: **not read / not verified** |
| Coralia Cartis | **Staff colleague, not a postdoc of Gould**: "Research Scientist in Numerical Analysis (permanent post), Numerical Analysis Group, Rutherford Appleton Laboratory 2006–2007"; before that EPSRC postdoc at Oxford with R. Hauser (2004–06) [M27, secondary] | 2006– | The Cartis–Gould–Toint complexity program (see note 01) | Gould was external examiner of her Cambridge PhD (2005) [M01]. See §4 |
| Marius Lange | MSc student of Cartis (Oxford MMSC list [M27]) | 2019 | Cartis, Gould & Lange, *BIT* 60 (2020) 583–589 (10.1007/s10543-019-00791-2) | A 7-page result from an MSc-level collaborator, published with both senior authors [practice] |
| Margherita Porcelli | Junior co-author | 2011–12 | Gould, Porcelli & Toint, *COAP* 2012 (10.1007/s10589-011-9446-7) | Her acknowledgement thanks her Florence colleagues Bellavia and Morini "for several helpful discussions and for their continued encouragement and support" [M25 p.21]; it says nothing about Gould |
| Tyrone Rees | Gould examined his Oxford D.Phil (2010) [M01]; later RAL colleague and, since 2019, group leader [M34][M40] | 2010– | Gould, Orban & Rees, *SIMAX* 35 (2014) (10.1137/130916394); Gould, Rees & Scott, *COAP* 2019 (10.1007/s10589-019-00064-2) | Examinee → colleague → group leader. His thesis acknowledgements do not mention Gould [M33 p.5] |
| Hussam Al Daas | RAL colleague (PhD Inria/Sorbonne 2018) [M32] | 2020s | Al Daas & Gould, arXiv:2511.11135 (v3 2 Mar 2026; the RAL page lists it as "Accepted at SIOPT 2026" [M32]) | The newest method paper (TREK/NREK) is with a young colleague. Its acknowledgement thanks only the reviewers [M31 p.16] |
| Alexis Montoison, Dominique Orban | GitHub co-developers of GALAHAD and CUTEst [M41][M46] | 2022– | Build system, CI, Julia and Python interfaces | See §3.4 |

Readings of the table [inferred]:
- **Examined, then recruited.** Cartis (examined 2005), Rees (2010) and Martin Stoll (2009) all became co-authors (for Stoll: Dollar, Gould, Stoll & Wathen, "Preconditioning Saddle-Point Systems with Applications in Optimization", *SIAM J. Sci. Comput.* 2010, 10.1137/080727129), and Rees became his group leader. Examining was one of the ways Gould found collaborators.
- **Student in first position.** When the student is the driver, Gould's papers break alphabetical order to put the student first: **Keller** 2000, **Fowkes** 2013, and L'Excellent in second place ahead of Gould in 1997. Note 01 found that 88 of 94 multi-author DBLP records are alphabetical; the exceptions are almost all student papers. This is a crediting habit visible only in practice [practice, primary; interpretation inferred].
- **Co-advising, not owning.** Every doctoral link except Fowkes has another institution's supervisor as principal (Noailles at INPT, Wathen at Oxford, Budd at Bath), and Fowkes himself was co-supervised with an industry-linked second supervisor. [practice, primary]

---

## 2. Supervision style (layer 7): what the evidence supports

**S1. Pair the student with someone who owns an application.** [practice, primary]
- Fowkes: EPSRC Industrial CASE studentship "in conjunction with Schlumberger" [M08 acknowledgement]; the thesis thanks Schlumberger for "access to their reservoir simulation software for the industrial application example" [M07 p.7]; the ECMOR paper thanks Schlumberger and "Mohammad Farshi for his advice on interfacing our code with the reservoir simulator" [M09]. The thesis problem is optimal well placement in oil-reservoir simulation [M05].
- Browne: a Bath PhD on topology optimization of structures with buckling constraints, with a CASE award [M19].
- L'Excellent and Décamps: CERFACS/ENSEEIHT theses on preconditioners for the structured linear systems inside LANCELOT-type methods [M17][M18].
- [inferred] The pattern is: a real application or a real solver bottleneck supplies the problem; Gould supplies optimization and linear-algebra machinery; a second supervisor or partner supplies the application.

**S2. The student's thesis can sit well outside Gould's core.** [practice, primary]
- Fowkes's thesis abstract: "a unifying framework for the global optimization of functions which are expensive to evaluate ... based on a Bayesian interpretation of radial basis function interpolation" [M07 p.5]. Bayesian global optimization is not a topic Gould published on before or after. The connection to his own program is the use of Lipschitz bounds: "by making use of Lipschitz continuity of the surrogate approximation, we develop an entirely new algorithm based on overlapping balls" [M07 p.5], and the 2013 JOGO paper's branch-and-bound for "Hessian Lipschitz continuous functions" (10.1007/s10898-012-9937-9) [practice]. [inferred] He let the application choose the field and brought his own tools (Lipschitz-model bounds, as in cubic regularization) to it.

**S3. What his one D.Phil student said.** [observed, secondary; the student's own words]
- "First of all, I would like to thank my supervisors Nick Gould and Chris Farmer for introducing me to this fascinating field and for their continuing support and advice over the years. Researching this thesis has been an inspiring and thoroughly enjoyable experience which would not have been possible without their valuable input." Fowkes, D.Phil thesis, Oxford, Hilary Term 2011, p.7 [M07].
- This is a conventional acknowledgement. It gives no detail on meeting frequency, feedback style or independence. **No other student account was found.**

**S4. Student → postdoc elsewhere → back as co-maintainer.** [practice, primary + secondary]
- Fowkes went from Gould's D.Phil to Edinburgh and to Cartis's Oxford group as a postdoc [M05][M27], then to RAL. By 2022 the two jointly announced GALAHAD 4.0 ("Jari Fowkes and Nick Gould, STFC-Rutherford Appleton Laboratory", NA Digest, 4 May 2022 [M49]) and co-authored the JOSS paper (10.21105/joss.04882). Fowkes also built PyCUTEst with Lindon Roberts and Árpád Bűrmen (*JOSS* 2022, 10.21105/joss.04377), a Python layer on Gould's CUTEst.
- [inferred] The long-run outcome of his one supervision is a successor for the software, not only a paper trail.

**S5. Encouragement at a distance to other people's students.** [observed, secondary]
- Frank E. Curtis (Nocedal's student) in his 2007 Northwestern thesis: "... and to Nick Gould for enlightening e-mail correspondence and much appreciated encouragement." Curtis, *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, PhD thesis, Northwestern, 2007, p.5 (DOI 10.21985/n2r99v). Gould and Curtis later co-authored two papers (see note 01).
- James Diffenderfer, a CUTEst user, on the Ipopt mailing list, 19 May 2020: "I asked about this issue on the CUTEst github page and Nick Gould mentioned that I should check with the ipopt mailing list to see if anyone has encountered a similar issue. It it worth noting that Nick was able to successfully solve the problem without encountering a segmentation fault." [M48] [observed, secondary]. So Gould reproduces a stranger's bug report himself before he redirects it.

**S6. Juniors as critics of his teaching material.** [stated, primary]
- Booklet preface: "A special mention to Sven Leyffer who was involved in writing an earlier incarnation, to Coralia Cartis, Jari Fowkes, Raphael Hauser, Christoph Ortner, and Daniel Robinson who jointly stimulated, dissected and corrected parts of this material" [M02 p.vi]. Three of the five (Cartis, Fowkes, Robinson) are on the table above.
- The same preface directs students to his annotated bibliography, "a corpus of seminal work in the area, which should be read by any student interested in furthering their understanding of the field" [M02 p.vi], and invites them to weaken his assumptions, with some irony: "well-motivated students might if they wish, try to weaken them; we can assure readers that academic journals are full of just such noble endevours" [M02 p.vi, verbatim including the spelling].

**S7. Gould as mentee: whom he credits.** [stated, primary]
- "... to Ken McKinnon, Jorge Nocedal, Jennifer Scott and Nick Trefethen who believed in me when it mattered. And of course to Philippe Toint, without whom my journey through optimization would have been much the poorer, and whose words and deeds have truly been an inspiration." [M02 p.vi]
- His own D.Phil advisor was Walter Murray (MGP [M03]); visiting scholar at Stanford OR in 1981–82 [M01]. No text by Gould about his own supervision was found.

**S8. What he chose to praise in someone else's supervision.** [stated, primary, co-authored with J. A. J. Hall; about Fletcher, not about Gould]
- In the Royal Society memoir of Roger Fletcher: "Roger rarely had more than one PhD student at a time, allowing him to build supportive working relationships with them and, when interests combined, engage with them socially. Many went hillwalking with him, and Womersley recalls their weekly games of squash." Gould & Hall, *Biogr. Mems Fell. R. Soc.* 78 (2025) 127–146, p.12 of the PDF (10.1098/rsbm.2024.0037) [M36].
- The memoir's Figure 3 is "Nick Gould, Roger Fletcher and Sven Leyffer in the Scottish Highlands, 2007" [M36 p.16]. Gould's CV lists "Flat and hill walking" first among his interests [M01 p.28].
- [inferred] A small-group, one-student-at-a-time model with a social side is the model he praises, and it matches his own record (one D.Phil student, a few long collaborations). This is inference from what he chose to write about another person; the text is co-authored, so no sentence can be assigned to Gould alone.

**Not found**: any advice to PhD students in Gould's own words, any description of how he runs meetings, how he gives feedback on drafts, or how he decides when a student's result is good enough.

---

## 3. Group habits and lab culture (RAL Numerical Analysis Group / Computational Mathematics)

Gould's "lab" is the RAL group he joined at Harwell in 1985 and moved with to RAL in 1990 [M01]. It is now the Computational Mathematics Theme, led by Tyrone Rees; the contact page lists "Nick Gould ... (GALAHAD Library)" [M40].

**3.1 The group writes its norms down.** [practice, group level; the 2006 document is **not** by Gould]
- Reid & Scott, *Guidelines for the development of HSL software*, RAL-TR-2006-031 (revised Sept. 2007) [M38]:
  - Independent testing: "We highly recommend that the developer of an HSL package involves someone who has not themselves been closely involved in the design and development of the code in the testing. This may be another Group member who has an interest in the package or, ideally, a potential user from outside the Group. In our experience, feedback from an independent user is invaluable" (p.18).
  - Test sets: "The test set should be as large and varied as possible", with CUTEr named as the optimization collection "developed by the Group and collaborators" (p.18).
  - Several compilers: "We often find that different compilers will unearth errors that others failed to detect" (p.18).
  - Senior sign-off: "the specification document and the main source code must be signed off by a senior member of the Group (currently Duff, Reid and Scott may approve a package)" (p.21).
  - Junior staff built the process: "We are grateful to Coralia Cartis and Sue Dollar for commenting on a draft and for putting together the check lists" (p.21).
- [inferred] This is the professional culture Gould worked inside for four decades: tested, signed-off library code, with the testing done by someone other than the author. Gould is not named among the approvers of HSL packages in 2006/07.

**3.2 A guideline Gould co-authored.** [stated + practice, primary, co-authored]
- Arioli, Duff, Gould, Hogg & Thorne, *Guidelines for development of Matlab interfaces for HSL packages*, RAL-TR-2010-013 (19 April 2010) [M37]. It covers "HSL or GALAHAD Fortran codes"; its co-authors include two junior staff (J. D. Hogg and H. S. Thorne).
  - Tone: "These guidelines are a simple indication of a safe and consistent approach ... Although developers can maintain reasonable freedom, we strongly encourage them to follow these guidelines" (p.5).
  - One source of truth: "any changes required to the main HSL Fortran package must be reflected in and tested with the Matlab interface and vice-versa" (p.5).
  - Exhaustive interface tests: "an automated exhaustive testing of the interface should be performed by the script <packagename> full test.m" (p.11).
  - Recorded pitfalls, and a request to extend them: "we highlight some of the problems we have already encountered and request that you report any other issues to us so that we can expand this section accordingly" (p.12).
- The 2011 revision (RAL-TR-2011-026) lists Arioli, Duff, Hogg and Thorne; Gould is no longer an author [M39, practice].

**3.3 Credit to junior people inside the code.** [practice, primary]
- The unreleased filter-SQP package in GALAHAD opens with: "Principal authors: Nick Gould, Yueling Loh and Daniel P. Robinson" and "originally written in Matlab by Yueling Loh and Daniel P. Robinson / initial Fortran translation, GALAHAD Version 2.6, November 23th 2014" (`src/forthcoming/fisqp/fisqp.F90`, header, HEAD afa13a5 [M41]). Loh was then Robinson's PhD student at Johns Hopkins [M23 p.1].
- Tally of the first "Principal author(s)" line in the 297 top-level module files `src/<package>/<file>.F90` that carry one (HEAD afa13a5; `src/forthcoming` is not included) [M41, practice, primary]:

  | Credit line | Files |
  |---|---|
  | Nick Gould alone | 213 |
  | Nick Gould and Dominique Orban | 58 |
  | With Daniel Robinson (Gould first 3, Robinson first 3, Robinson alone 1) | 7 |
  | With Philippe Toint (Toint alone 4, jointly 4) | 8 |
  | Nick Gould and Margherita Porcelli | 2 |
  | Hussam Al Daas and Nick Gould (junior colleague named first) | 2 |
  | Jaroslav Fowkes and/& Nick Gould (former student named first) | 2 |
  | Alexis Montoison alone | 1 |
  | Nick Gould, John Reid and Jonathan Hogg | 1 |
  | Third-party code shipped in the library (Davis/Amestoy/Duff…; Lin & Moré; Burkardt) | 3 |

  [inferred] The library is overwhelmingly Gould's own code. Where a junior person wrote the method (Robinson, Al Daas, Fowkes), the header can list them **first**, which mirrors the author-order habit in §1.

**3.4 The open-development group since 2022 (GitHub).** [practice, primary]
- **Who commits.** GALAHAD history in the clone (2018-02-03 to 2026-09-26, 1,993 commits): Gould 1,136 (as "Nick Gould" and "nimgould"), Alexis Montoison 798, Jaroslav Fowkes 45, Dominique Orban 13 [M41]. Gould's commits per year: 38 (2018), 6, 30, 131, 238 (2022), 242, 239, 205 (2025), then **7 in 2026** (last on 2026-08-13). Montoison's: 12 (2022), 277, 255, 220, 34 (2026) [M41]. CUTEst (2018–2026-09-27): Gould 173, Montoison 80, Orban 14, Fowkes 7, plus outside contributors (an Octave bridge by user "jezekr" in 2023; Stefan M. Wild, 3 commits) [M46].
- **Division of labour.** Gould writes the Fortran algorithms; Orban started the GitHub Actions and Meson builds (PRs #10 and #26, both opened by `dpo`); Montoison opened the Python, Julia, CI and GALAHAD 5 restructuring PRs (#85, #87, #272, #308, #358, #390); Fowkes opened the METIS interface PR (#382). GitHub lists 139 PRs in ralna/GALAHAD with comments by `nimgould` [M42]. So a senior author in his late sixties writes much of the core code himself and hands the modern tooling to younger collaborators [practice; "late sixties" from the birth date in M01].
- **Tone in the PR threads.** The quotes below are as returned by WebFetch from the public pages. github.com refused curl (403) and the MCP GitHub tool is not enabled for this repository, so **the exact wording could not be checked against the raw page**, and the first thread shows "119 hidden items".
  - Admitting what he does not know: "I really don't understand how macos shared libraries work, do you?" (PR #10, 21 Nov 2022) [M43].
  - Reducing a problem before asking others: "Presumably it would be trivial to build a pair of 5 line modern fortran modules, one of which uses the other, to see this failure in it simplest form, and then to ask the question to the mac community?" (PR #10, 21 Nov 2022) [M43].
  - Frank verdicts on colleagues' code, with priorities stated: "I am afraid that ssids in double precision is as leaky as a paper bag in a storm" and "Thank you @jfowkes, but not high priority I fear" (PR #10, 18 Nov 2022) [M43]. SSIDS comes from RAL colleagues' SPRAL library [inferred from the name; not checked].
  - Credit to a junior collaborator: "Thank you so much, you are my hero of the hour, perhaps day" (PR #272, 5 Jun 2024) [M44].
  - Admitting his own bugs, and changing a habit: "I recently 'improved' trb, so that this is definitely a not improvement!!" (PR #518, 24 Nov 2025); "I shall henceforth add local Julia testing before I push, even if it does mean that I will forget how to do it next time." (PR #518, 27 Nov 2025); "very wise not to trust me, I wouldn't" (PR #518, 27 Nov 2025) [M45].
  - Also in the git log (read directly): merge commits titled "git told me to merge, it knows all, I am but a pawn" (2023-07-01) and "bossy git demands I merge" (2023-07-02) [M41, primary].
- **User support.** CUTEst interfaces to other groups' new solvers keep being added by Gould himself, e.g. "Interface to the Uno package now provided" (2026-05-20) and "add highs as a supported package" (2026-09-27) [M46]. See also S5 (Diffenderfer).

**3.5 Informal and social side of the long collaborations.** [observed, secondary; ASR transcript]
- Toint, on how LANCELOT got its name: "So we designed the name, which has something to do with augmented Lagrangian. In an evening with some wine and some beer around and after some joyous moments, we stumbled on this acronym which stayed with us" (podcast *Subject to*, 27 July 2026, [0:43:41]–[0:44:00]) [M47]. The transcript is **automatic speech recognition, not checked against the audio**; treat the wording as approximate.
- The same interview on the licensing ethos of LANCELOT (Conn–Gould–Toint): "We thought we were all paid by the public funds and so we wanted to make our research public. We made some restriction on its use. We didn't want it to be used for the design of weapons" ([0:44:57]–[0:45:15], ASR) [M47].

---

## 4. How the peer collaborations work (CGT and Cartis–Gould–Toint)

**C1. Origin of Conn–Gould–Toint, as Toint tells it.** [observed, secondary; ASR]
- "I met two people I ended up working with many, many years at that conference, Nick Gould and Andy Cone [Conn]. The conference was in Montreal and Andy was working in Waterloo ... And I went to Waterloo and met Nick who was working there at the time. And so we went along very well, discussed the main thing, the needs to work on large scale problems and the need to write software to do it. And we didn't do anything for a while." ([0:38:32]–[0:39:12]) Then "Andy went for a sabbatical in France in Grenoble. And that was an opportunity for Nick and me to meet. And we started working on trust regions at that time and it has resulted in a long, long story of collaboration and friendship with these two people. I think we wrote more than 50 papers together." ([0:39:20]–[0:39:43], second ASR pass) [M47]. On the dates, see Contradictions.
- [inferred] The collaboration began with an agreed **agenda** ("large scale problems" plus "software to do it"), not with a single paper; the first joint work came years later.

**C2. Books grew from teaching notes and over-ran.** [observed, secondary; ASR]
- *Trust-Region Methods* "started as a course I thought [taught] in my university ... And since I had those notes, I suggested to other guys that what about, you know, elaborating on this. And unfortunately, maybe we could not stop." Writing took "About three years, if I remember well"; asked whether each author wrote 300 pages, Toint answered "More complicated story than that, but nevermind." ([0:47:56]–[0:49:13]) [M47].
- On the 2022 complexity book with Cartis and Gould: "it's very hard to stop once you are going on" ([1:02:47]–[1:02:50]) [M47]. The ASR word just before this ("too weak for my taste") is probably misrecognised; its meaning is not used here.
- How the writing was divided among the three authors: **not documented** anywhere I found.

**C3. Equal contribution, alphabetical order.** [observed, secondary; Cartis's own CV]
- "The papers with Gould and Toint are a long term collaboration, with equal contributions. Authors names on papers typically appear alphabetically as it is common in mathematics." Cartis CV 2025, p.1 [M27].
- A 2023 paper of Gould's with Fowkes and Scott states: "Author Contributions All authors contributed equally to this study" (*Numer. Algorithms* 2023, 10.1007/s11075-023-01681-z) [M12, practice].

**C4. Cartis was a peer, not a protégée.** [practice, secondary; from M27]
- The evaluation-complexity program (ARC 2011 onward) started when Cartis was a permanent RAL research scientist (2006–07) and continued after she moved to Edinburgh (2007) and Oxford (2013), with visiting status at RAL 2007–12 [M27]. It is a **three-peer collaboration**. Gould examined her PhD in 2005 [M01]. Any skill wording that presents Cartis as "Gould's postdoc" would be wrong.

---

## 5. Tacit knowledge: what collaborators pick up that the papers do not say

All items are [inferred] from [practice] records (commits, PR threads, code headers, author order). None comes from a student describing it. Mark them "partly distillable" (framework §八). Confidence: medium at best.

| # | Habit | Evidence |
|---|---|---|
| K1 | **Reduce a platform bug to the smallest failing example, then take it to the community that owns the platform.** | PR #10: the "5 line modern fortran modules" proposal [M43] |
| K2 | **Hunt memory leaks over the whole library, and swap in a known-robust component to isolate the culprit.** | PR #10: "once we switch to a robust solver (such as dsytrf/s), the rest of GALAHAD is now leak free ... That's where my two weeks have gone! On to mumps next." (18 Nov 2022, WebFetch caveat) [M43] |
| K3 | **Keep test levels separate**: stand-alone comprehensive tests versus SIF/CUTEst tests. | PR #10: "'test' just performs the comprehensive stand-alone tests while 'tests' does this + the sif/cutest tests" (11 Nov 2022, WebFetch caveat) [M43]; the same comprehensive-test idea appears in the HSL guidelines [M38] |
| K4 | **Test every language interface locally before pushing**, a rule adopted after a public failure. | PR #518 [M45] |
| K5 | **Leave unfinished methods visible, and ask users to vote with interest.** | `src/forthcoming/README.forthcoming`: "A collection of packages that *may* appear in GALAHAD. Often, this is simply that a given package needs a bit of loving care to move it from an "idea" to something that is reliable and useful to all. If you would like to see any of these moved up the priority chain, let us know. Nick Gould (for the GALAHAD team) October 2016" [M41, stated, primary] |
| K6 | **Credit juniors where it shows**: first place in the author list when the student drove the work; named as principal authors in the code header. | §1 readings; FiSQP header [M41] |
| K7 | **Examine, then collaborate.** | Cartis, Rees, Stoll (§1) |
| K8 | **Pair a methodological student with an industrial problem owner and a second supervisor.** | Fowkes, Browne (S1) |

---

## 6. Failures, abandoned directions, things that did not work (in this dimension)

| # | What | Evidence | Tag |
|---|---|---|---|
| X1 | **Joint filter-SQP with Loh and Robinson never released.** Matlab original by Loh and Robinson; Fortran translation 23 Nov 2014; the file header was last touched for GALAHAD 5.3 (2025-06-16), and the package still sits in `src/forthcoming`. Their SIOPT papers were published (2014, 10.1137/130920599; 2015, 10.1137/140996677, see note 01) | [M41][M23] | [practice, primary] |
| X2 | **Few formal students.** One D.Phil in a 40-year career. The structural reason is stated (not university-based), plus health-limited travel. Collaborators came through examining, co-advising and software instead | [M01][M02] | [stated + practice, primary] |
| X3 | **A self-inflicted regression found by collaborators' CI.** "I recently 'improved' trb, so that this is definitely a not improvement!!" (Nov 2025) | [M45] | [stated, primary; WebFetch caveat] |
| X4 | **A known defect left in place by priority.** SSIDS leaks: "not high priority I fear" (Nov 2022) | [M43] | [stated, primary; WebFetch caveat] |
| X5 | **Sharp drop in Gould's own GALAHAD commits in 2026** (7, against 205–242 a year in 2022–25), while Montoison and Fowkes continue and Fowkes is "acting" group leader. Reason unknown: handover, part-time status or health are all possible. **Do not assume** | [M41][M05] | [practice, primary; any reason is inferred] |
| X6 | **No trace of Gould in an examinee's acknowledgements** (Rees 2010). Weak evidence either way, since examiners are often not thanked | [M33] | [practice, secondary] |

---

## 7. Era and resource context

| Period | Setting | Mentoring and collaboration mode | Resources that made it possible |
|---|---|---|---|
| 1982–85 | Waterloo C&O, Assistant Professor | 3 M.Sc. students; thesis examiner for 3 PhDs; meets Conn (and Toint's visits, per Toint) [M01][M47] | NSERC grant 1983–85 [M01] |
| 1985–1999 | Harwell, then RAL NA group (Duff, Reid, Scott; HSL) | External advisor to Hatfield, Oxford and INPT/CERFACS students; CGT with Conn and Toint | NATO travel grant 1990–95; British Council ALLIANCE travel [M01][M15 p.1]; CERFACS sabbatical 1993 [M01] |
| 1999–2011 | RAL fellow; Oxford professor 2006–08; SIOPT Editor-in-Chief 2004–10 | The one D.Phil (Fowkes, 2008–11); Robinson postdoc; junior RAL staff (Cartis, Dollar, Hogg); MSc supervision | EPSRC grants: GR/S42170/01 (£433k, CoI), EP/E053351/1 (£1,604k, CoI), EP/F005369/1 (£336k, PI) [M01]; Industrial CASE (Schlumberger) [M07] |
| 2011–2020 | STFC Senior Fellow; part time from 2017 | Colleagues rather than students: Rees, Scott, Cartis (Oxford), Fowkes back from postdocs | EP/I013067/1 (£1,489k, CoI), EP/M025179/1 "Least Squares: Fit for the Future" (£970k, CoI) [M01] |
| 2022–2026 | Part-time senior fellow; open GitHub development | Remote, asynchronous collaboration through PRs with Montoison, Orban, Fowkes; interfaces to other groups' solvers | GitHub Actions CI, Meson, Julia and Python ecosystems; EP/X032485/1 [M12] |

[inferred] A reader who copies "how Gould mentors" should note that his model depends on **a permanent lab post with long-lived software and EPSRC grant income**, not on a stream of PhD students. The 2020s version also depends on younger collaborators willing to do the tooling.

---

## Contradictions (kept, not reconciled)

1. **When Toint met Gould at Waterloo.** Toint (ASR): he met Conn and Gould at "that conference", the one in Montreal that the host calls the 1979 ISMP, then "went to Waterloo and met Nick who was working there at the time"; the first CGT trust-region work began when Conn was on sabbatical in Grenoble, "I think it was in 1981" [M47]. Gould's CV: B.A. Oxford 1979, D.Phil Oxford 1982, visiting scholar Stanford 1981–82, **Assistant Professor at Waterloo only from 1982** [M01]. The first CGT papers are 1988 (note 01). The two accounts cannot both be exact on dates; the ASR may also have misheard.
2. **Fowkes's thesis year.** Title page "Hilary Term, 2011"; ORA and DataCite 2011 [M06][M07]; MGP 2012 [M04]; RAL publication list "DPhil Thesis ... 2012" [M05]. The CV places "D.Phil advisor for Jaroslav Fowkes" under 2008 [M01], which is presumably the start year.
3. **Sole or joint supervisor.** The CV lists Gould as "D.Phil advisor" [M01]; ORA, the RAL page and the thesis name **two** supervisors, Gould and Chris Farmer [M05][M06][M07]; MGP lists only Gould as "Advisor 1" [M04].
4. **"Not based in a university."** The booklet says "we are not based in a university and thus lack the experience and imperative to evaluate all the time" [M02 p.vi]. The CV records undergraduate and MSc courses at Oxford and Edinburgh (2001–07), Oxford undergraduate tutorials at Exeter College (2006–07), a professorship (2006–08) and visiting professorships since 1998 and 2008 [M01]. Both are true in their own sense (his employer is a laboratory); the self-description understates his teaching record.
5. **Crediting habit.** Students are placed first in some papers (Keller 2000, Fowkes 2013) but not in others with junior co-authors (Browne et al. 2012, Cartis–Fowkes–Gould 2015 and Cartis–Gould–Lange 2020 are alphabetical). Cartis states that the Gould–Toint papers are alphabetical by convention [M27]. So "student first" is a tendency, not a rule.
6. **Tone.** The formal documents are measured ("we strongly encourage them to follow these guidelines" [M37]). The PR threads are blunt and jokey ("as leaky as a paper bag in a storm"; "very wise not to trust me, I wouldn't" [M43][M45]). Both registers belong to the same person, in different venues.

---

## Gaps (what could not be found or read)

- **No student recollection beyond one acknowledgement paragraph** (Fowkes). No blog posts, memorial or Festschrift pieces, birthday-workshop proceedings, interviews with collaborators about Gould, or onboarding guides of his own were found. One WebSearch for a 60th-birthday event (he turned 60 in 2017) found none; a second, for thesis acknowledgements ("thank Nick Gould" thesis), hit only other people named Nick Gould (a University of Bath social-work professor and others). **Name collision** is a real hazard for later agents.
- **Theses not read**: Carsten Keller (Oxford, c. 1997–2000), H. Sue Dollar (Oxford), Philip Browne (Bath), L'Excellent (INPT 1995) and Décamps (INPT 1997). The last two are marked "accessible: non" on theses.fr [M17][M18]. The rest were not located online in the time allowed (Oxford ORA search returned 403; eprints.maths.ox.ac.uk was unreachable; OpenAlex and Semantic Scholar searches were rate-limited; CORE returned 403). Hernandez, Schuler and Gate: nothing beyond the CV line.
- **Coralia Cartis's PhD thesis** (Cambridge 2005; Gould examiner) and **Daniel Robinson's** account of his Oxford postdoc: not found.
- **Oxford MSc projects supervised by Gould in 2007** (4 students [M01]): names and topics not found.
- **SIAM News obituary of Andrew Conn**: 403, not read [M51]. The Waterloo obituary has nothing on the collaboration's working style [M50].
- **GitHub PR threads**: read only via WebFetch summaries (quotes not checked against the raw HTML), and PR #272 shows 119 hidden items. The MCP GitHub tool refused this repository, and adding it would need the user's consent. A later run with repository access should re-pull the exact comments (`issues/{n}/comments`) for PRs #10, #272 and #518.
- **Supervision advice in his own words** (how to choose a thesis problem, how to review a student draft): none found, in this note or in note 02.
- **The Toint podcast** is an unchecked ASR transcript; quotes need re-checking against the audio before the skill uses them verbatim.
- **Why Gould's GALAHAD commits dropped in 2026**: unknown.

---

## Sources

One line each. P = primary (Gould's own text or record), S = secondary. "Read" = full text or cited parts read in this run.

- M01 · "Curriculum Vitae, Nicholas Ian Mark Gould", N. I. M. Gould, 2023, https://www.numerical.rl.ac.uk/media/nick-gould/nimg.cv.pdf · P (read: personal data, positions, grants, activities, teaching, interests)
- M02 · *An introduction to algorithms for continuous optimization* (course booklet, © 2000, 2021), N. I. M. Gould, https://www.numerical.rl.ac.uk/media/people/nick-gould/cobook.pdf · P (preface pp. v–vi read)
- M03 · Mathematics Genealogy Project, Nicholas Ian Mark Gould (id 89384), https://www.mathgenealogy.org/id.php?id=89384 · S
- M04 · Mathematics Genealogy Project, Jaroslav M. Fowkes (id 294956), https://www.mathgenealogy.org/id.php?id=294956 · S
- M05 · "Jaroslav Fowkes", STFC RAL Computational Mathematics people page, accessed 2026-09-28, https://www.numerical.rl.ac.uk/people/jaroslav-fowkes · S (institutional bio)
- M06 · ORA record, J. Fowkes, *Bayesian numerical analysis: global optimization and other applications*, DPhil, Oxford, 2011, https://ora.ox.ac.uk/objects/uuid:ab268fe7-f757-459e-b1fe-a4a9083c1cba; DataCite 10.5287/ora-8r80452qe · S (bibliographic; supervisors listed)
- M07 · J. M. Fowkes, *Bayesian Numerical Analysis: Global Optimization and Other Applications*, DPhil thesis, Exeter College, Oxford, Hilary Term 2011, DOI 10.5287/ora-8r80452qe · S about Gould (the student's words; acknowledgements p.7 and abstract p.5 read)
- M08 · J. M. Fowkes, N. I. M. Gould & C. L. Farmer, "A branch and bound algorithm for the global optimization of Hessian Lipschitz continuous functions", *J. Global Optim.* 56(4) (2013) 1791–1815, DOI 10.1007/s10898-012-9937-9 · P (acknowledgements read)
- M09 · C. L. Farmer, J. M. Fowkes & N. I. M. Gould, "Optimal Well Placement", *ECMOR XII*, 2010, DOI 10.3997/2214-4609.20144994 · P (acknowledgements read)
- M10 · C. Cartis, J. M. Fowkes & N. I. M. Gould, "Branching and bounding improvements for global optimization algorithms with Lipschitz continuity properties", *J. Global Optim.* 61 (2015) 429–457, DOI 10.1007/s10898-014-0199-6 · P (acknowledgements read)
- M11 · J. M. Fowkes & N. I. M. Gould, "GALAHAD 4.0: an open source library of Fortran packages with C and Matlab interfaces for continuous optimization", *JOSS* 8(87) (2023) 4882, DOI 10.21105/joss.04882 · P (metadata checked here; text read by agent 01)
- M12 · J. M. Fowkes, N. I. M. Gould & J. A. Scott, "Approximating sparse Hessian matrices using large-scale linear least squares", *Numer. Algorithms* (2023), DOI 10.1007/s11075-023-01681-z · P (declarations read)
- M13 · J. Fowkes, L. Roberts & Á. Bűrmen, "PyCUTEst: an open source Python package of optimization test problems", *JOSS* (2022), DOI 10.21105/joss.04377 · S (metadata only)
- M14 · C. Keller, N. I. M. Gould & A. J. Wathen, "Constraint Preconditioning for Indefinite Linear Systems", *SIAM J. Matrix Anal. Appl.* 21 (2000) 1300–1317, DOI 10.1137/S0895479899351805 · P (acknowledgements read)
- M15 · M. J. Daydé, J.-Y. L'Excellent & N. I. M. Gould, "Element-by-Element Preconditioners for Large Partially Separable Optimization Problems", *SIAM J. Sci. Comput.* 18(6) (1997), DOI 10.1137/S1064827594274796 · P (p.1 footnotes and acknowledgements read)
- M16 · M. J. Daydé, J. P. Décamps & N. I. M. Gould, "Subspace-by-subspace preconditioners for structured linear systems", *Numer. Linear Algebra Appl.* 6 (1999) 213–234, DOI 10.1002/(SICI)1099-1506(199904/05)6:3<213::AID-NLA161>3.0.CO;2-V · P (p.1 and acknowledgements read)
- M17 · theses.fr record 1995INPT091H, J.-Y. L'Excellent, *Utilisation de préconditionneurs élément-par-élément pour la résolution de problèmes d'optimisation de grande taille*, INPT Toulouse, 1995, dir. J. Noailles, https://theses.fr/1995INPT091H · S (record and abstract; full text not accessible)
- M18 · theses.fr record 1997INPT092H, J. Décamps, *Méthodes itératives par blocs pour la résolution de problèmes linéaires et non linéaires à structures partiellement séparables*, INPT Toulouse, 1997, dir. J. Noailles, https://theses.fr/1997INPT092H · S (record and abstract; full text not accessible)
- M19 · P. A. Browne, C. Budd, N. I. M. Gould, H. A. Kim & J. A. Scott, "A fast method for binary programming using first-order derivatives, with application to topology optimization with buckling constraints", *Int. J. Numer. Meth. Engng* (2012), DOI 10.1002/nme.4367 · P (affiliations and acknowledgements read)
- M20 · N. I. M. Gould & D. P. Robinson, "A Second Derivative SQP Method: Global Convergence", *SIAM J. Optim.* 20(4) (2010), DOI 10.1137/080744542 (and Part II, "Local Convergence and Practical Issues", DOI 10.1137/080744554) · P (p.1 footnotes read, Part I)
- M21 · N. I. M. Gould, D. P. Robinson & H. S. Thorne, "On solving trust-region and other regularised subproblems in optimization", *Math. Program. Comput.* (2010), DOI 10.1007/s12532-010-0011-7 · P (metadata only)
- M22 · N. I. M. Gould, D. Orban & D. P. Robinson, "Trajectory-following methods for large-scale degenerate convex quadratic programming", *Math. Program. Comput.* (2013), DOI 10.1007/s12532-012-0050-3 · P (metadata only)
- M23 · N. I. M. Gould, Y. Loh & D. P. Robinson, "A Filter Method with Unified Step Computation for Nonlinear Optimization", *SIAM J. Optim.* 24(1) (2014), DOI 10.1137/130920599 · P (p.1 footnotes read)
- M24 · "Daniel P. Robinson", Lehigh University Engineering faculty page, accessed 2026-09-28, https://engineering.lehigh.edu/faculty/daniel-p-robinson · S
- M25 · N. I. M. Gould, M. Porcelli & Ph. L. Toint, "Updating the regularization parameter in the adaptive cubic regularization algorithm", *Comput. Optim. Appl.* (2012; online 2011), DOI 10.1007/s10589-011-9446-7 · P (acknowledgements read)
- M26 · C. Cartis, N. I. M. Gould & M. Lange, "On monotonic estimates of the norm of the minimizers of regularized quadratic functions in Krylov spaces", *BIT Numer. Math.* 60 (2020) 583–589, DOI 10.1007/s10543-019-00791-2 · P (p.1 read)
- M27 · Coralia Cartis, Curriculum Vitae (2025), https://www.maths.ox.ac.uk/system/files/users/cv/Cartis_CV_2025_0.pdf · S about Gould (positions, statement on the collaboration, supervision lists read)
- M28 · H. S. Dollar, N. I. M. Gould, W. H. A. Schilders & A. J. Wathen, "Implicit-Factorization Preconditioning and Iterative Solvers for Regularized Saddle-Point Systems", *SIAM J. Matrix Anal. Appl.* (2006), DOI 10.1137/05063427X · P (p.1 footnotes and acknowledgement read)
- M29 · N. Gould, D. Orban & T. Rees, "Projected Krylov Methods for Saddle-Point Systems", *SIAM J. Matrix Anal. Appl.* 35(4) (2014) 1329–1343, DOI 10.1137/130916394 · P (p.1 read)
- M30 · N. I. M. Gould, T. Rees & J. A. Scott, "Convergence and evaluation-complexity analysis of a regularized tensor-Newton method for solving nonlinear least-squares problems", *Comput. Optim. Appl.* (2019), DOI 10.1007/s10589-019-00064-2 · P (p.1 and acknowledgements read)
- M31 · H. Al Daas & N. I. M. Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems", arXiv:2511.11135v3 (2 Mar 2026) · P (acknowledgement read)
- M32 · "Hussam Al Daas", STFC RAL people page, accessed 2026-09-28, https://www.numerical.rl.ac.uk/people/hussam-al-daas · S
- M33 · T. Rees, *Preconditioning Iterative Methods for PDE Constrained Optimization*, DPhil thesis, Oxford, 2010, https://www.numerical.rl.ac.uk/media/people/tyrone-rees/pdf/TRThesis.pdf · S (acknowledgements read; Gould not mentioned)
- M34 · "Tyrone Rees", STFC RAL people page, accessed 2026-09-28, https://www.numerical.rl.ac.uk/people/tyrone-rees · S
- M35 · F. E. Curtis, *Inexact Sequential Quadratic Programming Methods for Large-Scale Nonlinear Optimization*, PhD thesis, Northwestern University, June 2007, DOI 10.21985/n2r99v (full text from the Northwestern repository as saved in this workflow's scratch) · S (acknowledgements p.5 read)
- M36 · N. I. M. Gould & J. A. J. Hall, "Roger Fletcher. 29 January 1939—15 July 2016", *Biogr. Mems Fell. R. Soc.* 78 (2025) 127–146, DOI 10.1098/rsbm.2024.0037 (royalsocietypublishing.org PDF as saved in this workflow's scratch) · P (co-authored; supervision passage, Figure 3 caption and acknowledgements read)
- M37 · M. Arioli, I. S. Duff, N. I. M. Gould, J. D. Hogg & H. S. Thorne, *Guidelines for development of Matlab interfaces for HSL packages*, RAL-TR-2010-013, 19 April 2010, https://epubs.stfc.ac.uk/manifestation/6610/adghtRAL2010013.pdf · P (read in full)
- M38 · J. K. Reid & J. A. Scott, *Guidelines for the development of HSL software*, RAL-TR-2006-031 (Dec 2006, revised Sept 2007), https://www.numerical.rl.ac.uk/media/reports/rsRAL2006031.pdf · S (group standard not written by Gould; §§5.3, 6.1, 8 read)
- M39 · STFC RAL Computational Mathematics, Technical Reports list, accessed 2026-09-28, https://www.numerical.rl.ac.uk/technical-reports/ · S (bibliographic)
- M40 · STFC RAL Computational Mathematics, "Contact us" and home pages, accessed 2026-09-28, https://www.numerical.rl.ac.uk/contact-us/ · S (institutional)
- M41 · GALAHAD git repository ralna/GALAHAD, HEAD afa13a5 (2026-09-26): commit log and authors, `src/forthcoming/README.forthcoming` (Oct 2016), header of `src/forthcoming/fisqp/fisqp.F90`, https://github.com/ralna/GALAHAD · P (practice)
- M42 · GitHub search, pull requests in ralna/GALAHAD with `commenter:nimgould` (139 results; top 15 by comments listed), 2026-09-28 · P (practice, metadata)
- M43 · GALAHAD PR #10 "GH Action to build and test" (opened by D. Orban, Oct 2022), https://github.com/ralna/GALAHAD/pull/10 · P (practice; read via WebFetch, wording unverified)
- M44 · GALAHAD PR #272 "Evolution to GALAHAD 5" (opened by A. Montoison, Apr 2024), https://github.com/ralna/GALAHAD/pull/272 · P (practice; WebFetch, 119 items hidden)
- M45 · GALAHAD PR #518 "New packages trek and nrek, plus updates to some of the older chaps" (opened by N. Gould, Nov 2025), https://github.com/ralna/GALAHAD/pull/518 · P (practice; WebFetch, wording unverified)
- M46 · CUTEst git repository ralna/CUTEst, HEAD 733acc7 (2026-09-27): commit log and authors, https://github.com/ralna/CUTEst · P (practice)
- M47 · "Subject to: Philippe Toint", podcast hosted by Anand Subramanian, 27 July 2026; automatic transcript saved at `product/nonlinear-team/philippe-l-toint/references/sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt`; episode https://podcasters.spotify.com/pod/show/subject-to/episodes/Subject-to-Philippe-Toint-e3mjb27 · S (collaborator's account; ASR, unchecked)
- M48 · J. Diffenderfer, "Segfault using Ipopt with CUTEst: Use of uninitialised value of size 8", Ipopt mailing list, 19 May 2020, https://list.coin-or.org/pipermail/ipopt/2020-May.txt · S
- M49 · J. Fowkes & N. Gould, "GALAHAD 4.0, nonlinear optimization", NA Digest V.22 #15, 4 May 2022, https://na-digest.coecis.cornell.edu/na-digest-html/22/v22n15.html · P
- M50 · "Andrew Conn (1946–2019)", University of Waterloo Combinatorics & Optimization news, 18 March 2019, https://uwaterloo.ca/combinatorics-and-optimization/news/andrew-conn-1946-2019 · S (read via WebFetch; nothing on working style)
- M51 · "Obituary: Andrew R. Conn", SIAM News, https://www.siam.org/publications/siam-news/articles/obituary-andrew-r-conn · S, **not read** (403)
- M52 · WebSearch, 2 queries (60th-birthday workshop; "thank Nick Gould" thesis), 2026-09-28 · no relevant results. Also blocked or rate-limited: ORA search (403), eprints.maths.ox.ac.uk (unreachable), OpenAlex and Semantic Scholar search (rate-limited), CORE (403) · **not read**
