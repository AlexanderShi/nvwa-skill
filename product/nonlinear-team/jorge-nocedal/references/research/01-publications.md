# Jorge Nocedal · 01 Signature works and the publication landscape

- **Researcher**: Jorge Nocedal (Walter P. Murphy Professor, IEMS, Northwestern University; PhD Rice 1978, adviser Richard A. Tapia)
- **Dimension**: research-craft Phase 1, agent 01 of 06: publication landscape plus dissection of signature works (framework §二 row 1, §五)
- **Research date**: 2026-09-28
- **Sources consulted**: 53 (listed under "Sources"): 37 primary (Nocedal's own papers, preprints, CV, homepage, software pages, speech, four talk and interview transcripts), 16 secondary (bibliographic databases, prize and news pages, third-party documentation, one peer critique, two WebSearch calls). Two of the secondary sources (Google Scholar, the MOS Dantzig page) could not be read.
- **Local corpus**: `references/sources/{papers,talks,essays,software}` held only `.gitkeep` files at the start of this run, so nothing here is "from user-supplied material". `private/` was not opened.
- **WebSearch calls used**: 2 of 2.

**Labels.** [stated] = Nocedal said or wrote it about himself or his work; [practice] = what the papers, code or records show he did; [observed] = what others (committees, press, users, critics) reported; [inferred] = my inference, with its basis. Every item is also marked primary or secondary.

**Talk and interview transcripts.** Four transcripts were saved to `../sources/talks/` during this same run by research agent 02; they are not user-supplied. The most important is a 1 h 48 min interview on the YouTube channel "Subject to", uploaded 2026-03-18 (https://www.youtube.com/watch?v=CfR-llfmb6E), transcript file `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt`. Its captions are automatic speech recognition (ASR), not human-checked. Quotes from these files are verbatim *captions* with the [h:mm:ss] block timestamp, marked "caption-derived". ASR errors (e.g. "Richard Bird" for Richard Byrd, "quasin Newton" for quasi-Newton) are left as they appear, with the intended word in square brackets where needed.

**How quotes were taken.** Quotes from pre-2000 papers come from the author-posted PostScript-to-PDF preprints on his homepage. The text extraction breaks up words ("No cedal"), and I restored only the spacing, never the wording. Page numbers are the PDF page of that preprint file, not the journal page. Quotes from arXiv abstracts, press releases and the speech are copied as they appear.

---

## 0. Data sources and coverage caveats (read before using any count)

| Source | What it gave | Caveat |
|---|---|---|
| DBLP (SPARQL, pid `n/JorgeNocedal`) | 83 records 1979–2026 (66 articles, 8 inproceedings, 8 CoRR, 1 book), 73 DOIs | Misses most pre-1990 work (e.g. the 1980 *Math. Comp.* L-BFGS paper, the 1985/1987 *SINUM* papers) and the book chapters. Not usable for 1978–1989 counts. |
| OpenAlex (author `A5081856145`, ORCID-matched, `fetch_publications.py`) | 174 works (179 pulled), 61,051 citations, h = 58 | Contains duplicates (the book appears as 3 records) and at least one misattribution (see §4.6). Its topic labels are noise ("Ecology", "Nature and Landscape Conservation", "Architecture"). Its first/last-author statistics are largely an alphabetical-order artefact (see §2.2). Raw output: `../sources/publications/publications.md`. |
| CV on homepage (`CV/cv_nocedal.pdf`, c. 2018) | 97 numbered publications 1978–2018, software, students, grants, invited talks | Primary but not always up to date (see Contradictions). A second, shorter CV version (`Bio/bio-brief.pdf`, c. 2021) adds honours only. |
| Homepage publication page | ~70 items with author-posted PDFs, c. 1989–2021 | Says "Check Google Scholar for more up to date publications". |
| arXiv author search | 21 preprints, 2013-09 → 2024-11 | Last arXiv submission found: 2411.02665 (Nov 2024). |
| Google Scholar (`gGNxMZ0AAAAJ`) | **not read**: WebFetch was redirected to Google's "sorry" (bot-check) page | Scholar citation counts are absent from this file. |
| Semantic Scholar API | citation counts for 7 papers | The author search returned HTTP 429, so author-level statistics were not read. |
| Crossref | metadata checks for ~50 DOIs | Used to verify every DOI cited below. |

---

## 1. Headline findings

1. **Two-person engine.** Richard H. Byrd (Colorado) is the co-author on 28 of 77 de-duplicated DBLP records and ~39 OpenAlex works, spanning 1987–2023. Nocedal calls this collaboration the most crucial interaction of his career [stated, primary: 2017 speech]. Most signature works are Byrd–Nocedal plus a student.
2. **Signature pattern: an algorithm, then its analysis, then code that is given away or sold.** L-BFGS (1980 paper, 1989 study, Harwell VA15 code, L-BFGS-B TOMS 1997, repaired 2011) and the interior/trust-region line (1999–2000 papers leading to KNITRO 2001–2006) each end in released software [practice, primary].
3. **Three field entries, each triggered from outside the field** [inferred from dates, grants and co-authors]:
   - large-scale unconstrained optimization, driven by storage limits (1980s);
   - large-scale constrained NLP and interior methods, driven by applications and industry (1990s–2000s, Ziena);
   - machine learning, driven by Google, IBM and Intel collaborations and grants (2010–2019).
   A fourth, **optimization with noise** (2018 onward), grew out of the ML stochastic work and engineering design.
4. **Author order is alphabetical for most of his career.** It switches abruptly around 2020 to student first, Nocedal last. Nocedal is last in 9 of 9 DBLP records in 2020–2024 and 2 of 2 in 2025–26; the list is non-alphabetical in 8 of 9 and 2 of 2. So the OpenAlex "first → last author" signal must not be read as a seniority shift before 2020 [practice, primary: computed from DBLP].
5. **Recurring move: re-examine a dismissed tool with careful numerical experiments.** Examples:
   - dropping the geometry phase in model-based DFO (2009, Broyden Prize);
   - finite differences for noisy DFO, "largely dismissed … such views should be re-examined" (2021/2023);
   - L-BFGS for machine learning, "not considered an algorithm of choice" (2018).
   [practice, primary: the abstracts and final remarks quoted in §3–§4]
6. **"I tried everything else."** He describes two signature methods as the survivor of exhausted alternatives. His PhD thesis on scaling quasi-Newton methods was, in his words, "a impressive collection of failed ideas", and L-BFGS came from rejecting that whole approach in his first month back in Mexico in 1978. The 2017 noisy-DFO talk says: "after trying everything else, I see that the only way I know how to do that is going back to Quasi-Newton methods" [stated, primary, caption-derived; §3 SW1, SW5].
7. **He records his own failures and fixes.** Examples:
   - a published correction of the L-BFGS-B code 14 years after release (2011 Remark);
   - errata pages for both book editions and for the SIAM Review paper;
   - a whole paper on Newton iterations that converge to non-stationary points (2004);
   - candid statements of limitations inside papers (KNITRO cannot tell infeasibility from an infeasible stationary point; NITRO deliberately slow-converging).
   [practice, primary]
8. **What he values most is not what is cited most, and he names his own misses.** In a March 2026 interview [stated, primary, caption-derived]:
   - he rates the ECMWF weather-forecasting work (Gauss–Newton, not L-BFGS) his "most important contribution", although it left one lightly cited paper (SW6);
   - he regrets not seeing early enough the "balance between the statistical aspect of the problem and the geometry of the problem" in ML (SW4);
   - he is "taking a pause from writing research papers" to finish the third edition of *Numerical Optimization* (§2.6).

---

## 2. Publication landscape

### 2.1 Topics by five-year period

Representative items only. Each has a DOI or arXiv id checked with Crossref, DBLP or arXiv in this run, or (marked CV) venue + year + title checked against the primary CV. Counts are DBLP (which undercounts before 1990) and OpenAlex.

| Period (position, place) | Main topics (evidence) | Representative verified items |
|---|---|---|
| **1978–1984** (PhD Rice 1978; asst. prof. UNAM, Mexico 1978–81; research associate, Courant/NYU 1981–83) | Conjugate gradients (thesis); line search; **limited-storage quasi-Newton**; variable-storage CG; nonlinear systems in mechanics; inverse eigenvalue problems (with M. Overton) | Thesis "On the Method of Conjugate Gradients for Function Minimization", Rice 1978 (CV; Math Genealogy). Bjørstad & Nocedal, *Computing* 1979, doi:10.1007/BF02246561. **Nocedal, "Updating quasi-Newton matrices with limited storage", *Math. Comp.* 35 (1980) 773–782, doi:10.1090/S0025-5718-1980-0572855-7** (solo). Nazareth & Nocedal, *Math. Program.* 1982, doi:10.1007/BF01583797. Nocedal & Overton, LNM 1005 (1983), doi:10.1007/bfb0112536. |
| **1985–1989** (asst./assoc. prof., Northwestern EECS from 1983) | Conic methods; projected-Hessian SQP updating; **global convergence theory of quasi-Newton methods (with Byrd, Yuan)**; inverse eigenvalue problems; the **L-BFGS numerical study** | Gourgeon & Nocedal, *SISSC* 1985, doi:10.1137/0906019. Nocedal & Overton, *SINUM* 1985, doi:10.1137/0722050. Davidon & Nocedal, *ACM TOMS* 1985, doi:10.1145/3147.3164. **Byrd, Nocedal & Yuan, *SINUM* 24 (1987), doi:10.1137/0724077**. Friedland, Nocedal & Overton, *SINUM* 1987, doi:10.1137/0724043. **Byrd & Nocedal, *SINUM* 26 (1989), doi:10.1137/0726042**. Liu & Nocedal, *SISSC* 1989, doi:10.1137/0910001. **Liu & Nocedal, *Math. Program.* 45 (1989) 503–528, doi:10.1007/BF01589116**. |
| **1990–1994** (prof. from 1992) | Reduced-Hessian SQP analysis; CG convergence; Broyden class; self-scaling QN; column scaling; **compact representations of QN matrices**; the Acta Numerica survey | Byrd & Nocedal, *Math. Program.* 1991, doi:10.1007/BF01588794. Nash & Nocedal, *SIOPT* 1991, doi:10.1137/0801023. Gilbert & Nocedal, *SIOPT* 1992, doi:10.1137/0802003. Byrd, Liu & Nocedal, *SIOPT* 1992, doi:10.1137/0802026. **Nocedal, "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1 (1992) 199–242, doi:10.1017/S0962492900002270**. Nocedal & Yuan, *Math. Program.* 1993, doi:10.1007/BF01582136. Byrd, Nocedal & Schnabel, *Math. Program.* 63 (1994), doi:10.1007/BF01582063. |
| **1995–1999** | **L-BFGS-B**; reduced-Hessian methods for large constrained problems (with Biegler); large-scale equality-constrained trust region; **interior-point trust-region NLP (NITRO)**; the textbook; ICM 1998 invited talk | **Byrd, Lu, Nocedal & Zhu, *SISC* 16 (1995), doi:10.1137/0916069**. Biegler, Nocedal & Schmid, *SIOPT* 1995, doi:10.1137/0805017. **Zhu, Byrd, Lu & Nocedal, Algorithm 778, *ACM TOMS* 23 (1997), doi:10.1145/279232.279236**. Lalee, Nocedal & Plantenga, *SIOPT* 1998, doi:10.1137/S1052623493262993. **Byrd, Hribar & Nocedal, *SIOPT* 9 (1999) 877–900, doi:10.1137/S1052623497325107**. **Nocedal & Wright, *Numerical Optimization*, Springer 1999, doi:10.1007/b98874**. |
| **2000–2004** (co-founds Ziena Optimization 2001, CV) | Interior-point theory; feasible interior methods; **SLQP active-set method**; EQP solution; preconditioning (PREQN); wedge trust-region DFO; failure analysis of Newton's method; PDE-constrained assessment | **Byrd, Gilbert & Nocedal, *Math. Program.* 89 (2000), doi:10.1007/PL00011391**. Morales & Nocedal, *SIOPT* 2000, doi:10.1137/S1052623497327854. Gould, Hribar & Nocedal, *SISC* 2001, doi:10.1137/S1064827598345667. Marazzi & Nocedal, *Math. Program.* 2002, doi:10.1007/S101070100264. Byrd, Nocedal & Waltz, *COAP* 2003, doi:10.1023/A:1025136421370. Morales et al., LNCSE 30 (2003), doi:10.1007/978-3-642-55508-4_10. Byrd, Gould, Nocedal & Waltz, *Math. Program.* 100 (2004), doi:10.1007/S10107-003-0485-4. Byrd, Marazzi & Nocedal, *Math. Program.* 99 (2004), doi:10.1007/S10107-003-0376-8. |
| **2005–2009** | **KNITRO package paper**; 2nd edition of the book; MPCCs; penalty steering; **inexact SQP / matrix-free Newton (with F. E. Curtis)**; adaptive barrier updates (with Wächter, Waltz); LCPs (options pricing, rigid bodies); DFO geometry; data assimilation | **Byrd, Nocedal & Waltz, "Knitro: An Integrated Package for Nonlinear Optimization", in *Large-Scale Nonlinear Optimization* (Di Pillo, Roma eds.), Springer 2006, pp. 35–59, doi:10.1007/0-387-30065-1_4**. Waltz, Morales, Nocedal & Orban, *Math. Program.* 107 (2006), doi:10.1007/s10107-004-0560-5. Nocedal & Wright 2nd ed. 2006, doi:10.1007/978-0-387-40065-5. Leyffer, López-Calva & Nocedal, *SIOPT* 2006, doi:10.1137/040621065. Byrd, Curtis & Nocedal, *SIOPT* 19 (2008), doi:10.1137/060674004. Byrd, Nocedal & Waltz, *OMS* 2008, doi:10.1080/10556780701394169. Curtis & Nocedal, *IMA JNA* 2008, doi:10.1093/imanum/drn003. Nocedal, Wächter & Waltz, *SIOPT* 2009, doi:10.1137/060649513. Fasano, Morales & Nocedal, *OMS* 2009, doi:10.1080/10556780802409296. Fisher, Nocedal, Trémolet & Wright, *Optim. Eng.* 2009, doi:10.1007/s11081-008-9051-5. |
| **2010–2014** (director, Optimization Center; Google consulting 2012–14, CV) | Infeasibility detection (SQP, IPM); **turn to machine learning**: stochastic Hessian information, sample-size selection, ℓ1-regularized second-order methods, sparse inverse covariance, **stochastic quasi-Newton** | Byrd, Curtis & Nocedal, *Math. Program.* 122 (2010), doi:10.1007/S10107-008-0248-3. Byrd, Curtis & Nocedal, *SIOPT* 20 (2010), doi:10.1137/080738222. **Byrd, Chin, Neveitt & Nocedal, *SIOPT* 21 (2011) 977–995, doi:10.1137/10079923X**. Morales & Nocedal, *ACM TOMS* 38 (2011), doi:10.1145/2049662.2049669. Byrd, Chin, Nocedal & Wu, *Math. Program.* 134 (2012), doi:10.1007/s10107-012-0572-5. Olsen, Öztoprak, Nocedal & Rennie, "Newton-Like Methods for Sparse Inverse Covariance Estimation", NIPS 2012 (DBLP; no DOI). Byrd, Nocedal, Waltz & Wu, *Math. Program.* 2013, doi:10.1007/S10107-011-0492-9. Nocedal, Öztoprak & Waltz, *OMS* 2014, doi:10.1080/10556788.2013.858156. Byrd, Hansen, Nocedal & Singer, arXiv:1401.7020 → *SIOPT* 26 (2016), doi:10.1137/140954362. |
| **2015–2019** (chair, IEMS 2013–17) | **SIAM Review survey**; multi-batch and progressive-batching L-BFGS; **large-batch training and sharp minima**; subsampled Newton, Newton-sketch; adaptive sampling; **first noisy-DFO paper**; BFGS with errors | **Bottou, Curtis & Nocedal, arXiv:1606.04838 → *SIAM Rev.* 60 (2018) 223–311, doi:10.1137/16M1080173**. Berahas, Nocedal & Takáč, NIPS 2016, arXiv:1605.06049. **Keskar, Mudigere, Nocedal, Smelyanskiy & Tang, arXiv:1609.04836 (ICLR 2017)**. Bollapragada, Byrd & Nocedal, arXiv:1609.08502 → *IMA JNA* 39 (2019), doi:10.1093/imanum/dry009. Bollapragada, Byrd & Nocedal, arXiv:1710.11258 → *SIOPT* 28 (2018), doi:10.1137/17M1154679. Bollapragada et al., arXiv:1802.05374 (ICML 2018). **Berahas, Byrd & Nocedal, arXiv:1803.10173 → *SIOPT* 29 (2019) 965–993, doi:10.1137/18M1177718**. Xie, Byrd & Nocedal, arXiv:1901.09063 → *SIOPT* 30 (2020), doi:10.1137/19M1240794. |
| **2020–2026** (NAE 2020; Lagrange Prize 2021) | **Noise-tolerant optimization**: noise-tolerant (L-)BFGS, finite-difference DFO benchmarking, adaptive FD intervals, noisy trust region, constrained problems with noise, noisy equality-constrained Byrd–Omojokun, robust-design guidelines, feasible constrained DFO; adaptive sampling for constrained and composite problems; one DOE power-grid (SCOPF) report | **Shi, Xie, Byrd & Nocedal, arXiv:2010.04352 → *SIOPT* 32 (2022), doi:10.1137/20M1373190**. **Shi, Xuan, Öztoprak & Nocedal, arXiv:2102.09762 → *OMS* 38 (2023), doi:10.1080/10556788.2022.2121832**. Shi, Xie, Xuan & Nocedal, arXiv:2110.06380 → *SISC* 44 (2022), doi:10.1137/21M1452470. Öztoprak, Byrd & Nocedal, arXiv:2110.04355 → *SIOPT* 33 (2023), doi:10.1137/21M1450999. Xie, Bollapragada, Byrd & Nocedal, arXiv:2012.15411 → *IMA JNA* 44 (2024), doi:10.1093/imanum/drad020. Sun & Nocedal, arXiv:2201.00973 ("A Trust Region Method for the Optimization of Noisy Functions") → *Math. Program.* 202 (2023), doi:10.1007/s10107-023-01941-9 (retitled "A trust region method for noisy unconstrained optimization"; the match between the two is inferred from authors and topic). Sun & Nocedal, arXiv:2411.02665 (preprint). **Lou, Sun & Nocedal, arXiv:2401.15007 → *SISC* 47 (2025), doi:10.1137/24M1632279**. Xuan & Nocedal, arXiv:2402.11920 → *Oper. Res. Lett.* 65 (2026) 107398, doi:10.1016/j.orl.2025.107398. OSTI report DOE-Northwestern-1077, doi:10.2172/2404586. |

**Constant through all periods** [practice, primary]: quasi-Newton and limited-memory updating.
- 1980 L-BFGS
- 1987–1994 QN theory and compact forms
- 1995–97 L-BFGS-B
- 2000 L-BFGS preconditioning
- 2014–2018 stochastic, multi-batch and progressive-batching L-BFGS
- 2019–2022 noisy and erroneous BFGS

This is the one line that never breaks. Everything else arrives as a stint of roughly 3–10 years.

**What the research statements say** [stated, primary]:
- Homepage (c. 2011–2016): "There is a need for solving ever larger optimization problems, and throughout the years, I have developed algorithms that scale well with the number of variables, make judicious use of second-order information, and parallelize well." (http://users.iems.northwestern.edu/~nocedal/)
- CV (c. 2018), research interests: "Nonlinear optimization, stochastic optimization, scientific computing, software; applications of optimization in machine learning, computer-aided design, and in models defined by differential equations."

### 2.2 Authorship order: alphabetical convention, then a switch around 2020

Computed from the 77 de-duplicated DBLP records [practice, primary]. The 4 records from 1979–1989 are all alphabetical and are omitted from the table; DBLP undercounts that decade.

| Period | Records | Author list alphabetical | Nocedal last | Nocedal first |
|---|---|---|---|---|
| 1990–1994 | 7 | 7 | 5 | 1 |
| 1995–1999 | 6 | 5 | 2 | 1 |
| 2000–2004 | 13 | 13 | 7 | 1 |
| 2005–2009 | 12 | 11 | 4 | 1 |
| 2010–2014 | 13 | 11 | 7 | 1 |
| 2015–2019 | 11 | 10 | 3 | 0 |
| 2020–2024 | 9 | **1** | **9** | 0 |
| 2025–2026 | 2 | **0** | **2** | 0 |

- Before 2020, "Nocedal last" mostly means his surname sorts after Byrd, Curtis, Gould, Liu, Morales and similar names. OpenAlex's "last-author share rising" story does not apply before 2020.
- The five pre-2020 non-alphabetical lists all put a student, postdoc or industry lead first:
  - Zhu, Byrd, Lu, Nocedal (TOMS 1997);
  - Waltz, Morales, Nocedal, Orban (*Math. Program.* 2006; his homepage lists the same paper alphabetically);
  - Olsen, Öztoprak, Nocedal, Rennie (NIPS 2012);
  - Robinson, Feng, Nocedal, Pang (*SIOPT* 2013);
  - Solntsev, Nocedal, Byrd (2015).
- From 2020 the convention is student first, Nocedal last: Xie, Byrd, Nocedal; Shi, Xie, Byrd, Nocedal; Sun, Nocedal; Lou, Sun, Nocedal; Xuan, Nocedal.
- Why he switched is **not stated anywhere I found**. Possible reasons are the ML/CS conventions of the co-authors, or giving credit to students on the job market. This is [inferred] and unverified.
- One reliable seniority signal: from about 2016 onward almost every paper has a current PhD student as the lead contributor (see §2.3). The recent noise papers are two- or three-author papers with a student.

### 2.3 Collaboration network and students

**Core collaborators** (DBLP co-author counts, de-duplicated; OpenAlex counts in parentheses where larger) [practice, primary]:

| Collaborator | Papers | Years | Role (source) |
|---|---|---|---|
| Richard H. Byrd (Univ. Colorado Boulder) | 28 (≈39+12 under "Richard Byrd") | 1987–2023 | Lifelong co-author; they met as graduate students at Rice (2026 interview [0:41:33], caption-derived). Called "my constant friend and colleague" whose "brilliant insights and world-class mathematical skills" he credits [stated, primary: 2017 speech]. |
| Richard A. Waltz | 9 (13) | 2002–2014 | PhD student (2002, CV), then KNITRO co-developer (CV: "KNITRO, A Package for Nonlinear Optimization, Manual, May 2002, with R. Waltz") |
| José Luis Morales (ITAM, Mexico) | 8 (14) | 1999–2020 | Research scientist / postdoc "1999–2007+" (students page); co-author of L-BFGS-B v3.0 and PREQN |
| Figen Öztoprak | 7 (14) | 2012–2023 | Frequent co-author on ℓ1 methods, IPM infeasibility and noisy constrained problems. Position not verified. |
| Frank E. Curtis | 6 (7) | 2006–2018 | PhD student (2007), later co-author of the SIAM Review paper (also a member of this team) |
| Nicholas I. M. Gould (RAL) | 3 (6) | 1998–2005 | EQP, SLQP convergence (also a team member) |
| Andreas Wächter (Northwestern) | 3 | 2009–2016 | Adaptive barrier, matrix-free rank-deficient SQP, ℓ1 active-set prediction (also a team member) |
| Stephen J. Wright | book + 1 paper | 1999, 2006, 2009 | *Numerical Optimization* (both editions); data-assimilation paper (also a team member) |
| Ya-xiang Yuan | 3 | 1987–1998 | QN convergence 1987; self-scaling QN 1993; TR + line search 1998; listed as postdoc/visitor 1998 |
| Michael L. Overton | 4 (CV) | 1983–1987 | Inverse eigenvalue problems, projected-Hessian SQP (Courant period) |
| Jean Charles Gilbert | 3 | 1992–2000 | CG convergence 1992; L-BFGS and AD 1993; IP trust region 2000 |

**Industry co-authors in the ML period** [practice, primary]:
- Will Neveitt: "Google Research" per the NSF bio.
- Mikhail Smelyanskiy: "INTEL" per the NSF bio.
- Yoram Singer; Peder Olsen and Steven Rennie; Dheevatsa Mudigere and Ping Tak Peter Tang: affiliations **not verified** here. The Intel link of the large-batch paper is [inferred] from the CV grant "INTEL, Optimization Methods for Large Scale Machine Learning, Feb 2016–Dec 2018".
- Léon Bottou: Facebook AI Research per the arXiv v1 footnote of 1606.04838.

**PhD students.** Source: CV student list (primary), homepage students page (primary), Math Genealogy (secondary, 19 students).
- 1986–1999: Dong C. Liu (1987), Marucha Lalee (1992), Peihuang Lu (1992), Todd Plantenga (1994), Mary Beth Hribar (1995/96), Guanghui Liu (1999).
- 2000–2010: Marcelo Marazzi (2001), Richard Waltz (2002), Gabriel López-Calva (2005/06), Frank Curtis (2007), Long Hei (2007), Yuchen Wu (2010).
- 2011–2019: Gillian Chin (2013), Samantha Hansen (2014), Stefan Solntsev (2015/16), Nitish Keskar (2017), Albert Berahas (2018), Raghu Bollapragada (2019).
- Listed as "(exp) 2020" in the CV: Hao-Jun Michael Shi, Yuchen Xie.
- Shigeng Sun (2024, Math Genealogy).
- **Likely students** [inferred from first authorship on 2021–2026 papers with Nocedal as last author; not verified]: Melody Qiming Xuan, Yuchen Lou.

Nearly every signature work carries a student as a co-author:
- Liu (L-BFGS);
- Lu and Zhu (L-BFGS-B; Zhu is listed as a postdoc);
- Hribar (NITRO);
- Waltz (KNITRO);
- Curtis (inexact SQP);
- Chin and Hansen (ML);
- Berahas, Shi and Xie (noise).
[practice, primary]

**Postdocs / research scientists** (homepage students page): Daniel Robinson (2010–11), Dominique Orban (2002–03), José Luis Morales (1999–2007+), Xavier Jonsson (2002–03), Jean-Pierre Goux (1998–2001), Ciyou Zhu, Ya-xiang Yuan (1998), Dong C. Liu (1990–91), Albert Berahas (2018).

### 2.4 Venues

| Source | Venues |
|---|---|
| DBLP | *SIAM J. Optim.* 22, *Math. Program.* 17, *Optim. Methods Softw.* 8, CoRR 8, *ACM TOMS* 4, *SIAM J. Sci. Comput.* 4, *Comput. Optim. Appl.* 4 |
| OpenAlex (adds pre-1990 venues) | *SIAM J. Numer. Anal.* 4, *IMA J. Numer. Anal.* 4, *Math. Comp.* 3 |
| ML venues (practice, 2012–2018 only) | NIPS 2012, NIPS 2016, ICLR 2017, ICML 2018, ICASSP 2012, *IEEE TASLP* 2013. After 2018 he returns to *SIOPT*, *SISC*, *Math. Program.*, *OMS*, *IMA JNA*, *ORL*. |

**Software as a publication channel** [practice, primary: CV "Published software"]:
- VA15 in the Harwell library (1990);
- Algorithm 778 L-BFGS-B (TOMS 1997);
- PREQN (TOMS 2001);
- KNITRO manual (2002);
- homepage codes CG+ and Wedge (free, BSD-style).

### 2.5 Most-cited works

Citation counts from four databases disagree and are only for relative comparison. Crossref and Semantic Scholar were queried 2026-09-28; OpenAlex counts come from `fetch_publications.py`.

| # | Work | Verified id | OpenAlex | Crossref | Sem. Scholar |
|---|---|---|---|---|---|
| 1 | Nocedal & Wright, *Numerical Optimization* (1st ed. 1999; 2nd ed. 2006) | doi:10.1007/b98874; doi:10.1007/978-0-387-40065-5 | 9,520 + 9,050 + 1,119 (3 records) | 6,564 + 1,007 | not read |
| 2 | Liu & Nocedal 1989, L-BFGS | doi:10.1007/BF01589116 | 8,818 | 6,927 | 9,075 (702 "influential") |
| 3 | Byrd, Lu, Nocedal & Zhu 1995, L-BFGS-B | doi:10.1137/0916069 | 6,420 | 5,235 | 6,883 |
| 4 | Zhu, Byrd, Lu & Nocedal 1997, Algorithm 778 | doi:10.1145/279232.279236 | 3,565 | 2,907 | not read |
| 5 | Bottou, Curtis & Nocedal 2018, SIAM Review | doi:10.1137/16M1080173 | 3,255 | 2,272 | 4,050 |
| 6 | Nocedal 1980, limited storage | doi:10.1090/S0025-5718-1980-0572855-7 | 2,760 (+561 JSTOR duplicate) | 2,623 | 2,978 |
| 7 | Byrd, Hribar & Nocedal 1999, IPM for large NLP | doi:10.1137/S1052623497325107 | 1,764 | 1,430 | 1,854 |
| 8 | Byrd, Gilbert & Nocedal 2000, IP trust region | doi:10.1007/PL00011391 | 1,672 | 1,331 | not read |
| 9 | Gilbert & Nocedal 1992, CG convergence | doi:10.1137/0802003 | 1,072 | 825 | not read |
| 10 | Waltz, Morales, Nocedal & Orban 2006 | doi:10.1007/s10107-004-0560-5 | 1,067 | 878 | not read |
| 11 | Byrd, Nocedal & Waltz 2006, Knitro | doi:10.1007/0-387-30065-1_4 | 995 | 621 | 1,201 |
| 12 | Byrd, Nocedal & Schnabel 1994, compact representations | doi:10.1007/BF01582063 | 759 | 560 | not read |
| 13 | Keskar et al. 2017, large-batch / sharp minima | arXiv:1609.04836 | 565 (arXiv record) | not read | not read |

All top 13 are either L-BFGS family, interior/KNITRO family, textbook, or the ML survey. [practice, primary + secondary counts]

### 2.6 Recent works (last ~3 years, 2023-09 → 2026-09)

Found via arXiv, OpenAlex and DBLP; all topics are noise or DFO [practice, primary]:
- Lou, Sun & Nocedal, *SISC* 47 (2025) A1335–A1357, doi:10.1137/24M1632279 (arXiv:2401.15007). DBLP's CoRR record for this arXiv id, presumably indexing v1, has the title "Noise-Tolerant Optimization Methods for the Solution of a Robust Design Problem"; the current arXiv version (v2, Oct 2024) and the journal use "Design Guidelines for Noise-Tolerant Optimization with Applications in Robust Design".
- Xuan & Nocedal, "A feasible method for constrained derivative-free optimization", *Oper. Res. Lett.* 65 (2026) 107398, doi:10.1016/j.orl.2025.107398 (arXiv:2402.11920).
- Sun & Nocedal, "A Trust-Region Algorithm for Noisy Equality Constrained Optimization", arXiv:2411.02665 (Nov 2024; no journal version found).
- Nocedal, "An Iterative Approach for Solving the SCOPF Problem Applying LP, SOCP, and NLP Subproblems", DOE technical report DOE-Northwestern-1077 (OSTI 2024), doi:10.2172/2404586. Proposal-style abstract: contingency filtering by LP, SOCP relaxations, then "a non-convex, nonlinear interior-point solver, Artelys Knitro".
- **No arXiv preprint after Nov 2024 was found.** He gives the reason himself in the March 2026 interview: "Right now, I'm just working on the third edition of my book with Steve Wright. I'm taking a pause from writing research papers. I'm very interested in generative AI but I will see if I can have something to contribute there." [1:45:19] [stated, primary, caption-derived]
- **Stated publication rate** (same interview): "Two to three papers a year, less than three per year because I would not publish papers that I thought were not complete uh were not satisfactory or so on." [1:39:37–1:40:12]. This is consistent with the record: 97 CV items over 1978–2018 (about 2.4 a year) and 77 DBLP records over 47 years.

### 2.7 Works Nocedal himself singled out (stated importance)

| Where | What he picked | Label |
|---|---|---|
| NSF biosketch (homepage `CV/nsf-bio.pdf`, c. 2011), "Five Relevant Publications" | stochastic Hessian 2011 (doi:10.1137/10079923X); infeasibility-detection SQP 2010 (doi:10.1137/080738222); geometry phase in DFO 2009 (doi:10.1080/10556780802409296, "Awarded the Charles Broyden Prize"); inexact Newton, nonconvex equality constrained 2010 (doi:10.1007/S10107-008-0248-3); piecewise linear models 2013 (doi:10.1007/S10107-011-0492-9) | [stated, primary]. Constrained by the NSF format ("relevant" to a proposal, recent). Not a lifetime ranking. |
| 2017 von Neumann acceptance speech | "some theoretical results on quasi-Newton methods" presented as a SIAM plenary that "proved to be decisive as it connected me with Mike Powell" | [stated, primary]. See `../sources/talks/2017-von-neumann-prize-acceptance-speech.md` |
| Homepage front page (c. 2016–) | "New: SIAM Review Article (Optimization Methods for Large-Scale Machine Learning)" | [practice, primary] |
| McCormick 2017 press quote | software, and seeing it "impact new application areas, such as machine learning" | [stated, secondary: press release] |
| 2026 interview, on the QN convergence theory with Byrd [0:58:26] | "We worked probably two years on developing this these tools and out of this comes a real understanding of how things are. So I'm really proud of of of of that work." | [stated, primary, caption-derived] |
| 2026 interview, on ECMWF variational data assimilation (1990s) [1:14:00–1:14:34] | "I always felt that it was my most important contribution because if you see the effect of good weather forecast over people's lives and the economy and so on it must be much bigger than the effect that our codes have within airplanes and cars" | [stated, primary, caption-derived]. Barely visible in the citation record: see SW6 and Contradictions. |

---

## 3. Signature works dissected (framework §五)

Selection: **most cited** (SW1, SW3, SW4), **self-identified as career-decisive** (SW2), and **turning points** (SW4 into ML; SW5 into noise). The textbook is the single most-cited item but is **not dissected**: it was not read (only its homepage description and errata pages exist here).

### SW1. The limited-memory BFGS method (1980 → 1989 → L-BFGS-B 1995/1997 → Remark 2011)

Papers:
- Nocedal, *Math. Comp.* 35 (1980) 773–782, doi:10.1090/S0025-5718-1980-0572855-7 (solo; body **not read**: AMS served a Cloudflare challenge; abstract read via OpenAlex).
- Liu & Nocedal, *Math. Program.* 45 (1989) 503–528, doi:10.1007/BF01589116 (author preprint read in full).
- Byrd, Lu, Nocedal & Zhu, *SISC* 16 (1995), doi:10.1137/0916069 (preprint front matter read).
- Zhu, Byrd, Lu & Nocedal, *ACM TOMS* 23 (1997), doi:10.1145/279232.279236.
- Morales & Nocedal, *ACM TOMS* 38 (2011), doi:10.1145/2049662.2049669 (abstract only).

**Origin**
- 1980 abstract: "We study how to use the BFGS quasi-Newton matrices to precondition minimization methods for problems where the storage is critical." Also: "The quasi-Newton matrix is updated at every iteration by dropping the oldest information and replacing it by the newest information." [stated, primary: abstract as indexed by OpenAlex]
- The thesis (1978) was on conjugate gradients (CV, Math Genealogy) [practice, primary]. That L-BFGS grew out of trying to give CG more memory is **[inferred]** from:
  - the thesis topic;
  - the 1982 Nazareth–Nocedal "Conjugate direction methods with variable storage";
  - the 1989 paper's framing that limited-memory methods "can be seen as extensions of the conjugate gradient method, in which additional storage is used to accelerate convergence" (preprint p. 3).
- **First-person origin story** (2026 interview) [stated, primary, caption-derived, `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt`]:
  - Thesis: he wanted "to develop quasant [quasi-Newton] methods that scaled up into millions of variables" and spent "two full years" on it. "if you read them there all of them are a failure. None of them are elegant. None of them are great. … It was a impressive collection of failed ideas." [0:46:37–0:47:11]
  - The switch: "So when I went back to Mexico in 78, the first month that I was there, I remember I went to the board and I realized I did the wrong thing in my thesis. All these methods are too complicated. This is not the way to do that. I was trying to extend the conjugate gradient method. Transform quasin Newton into conjugate gradients. There was the wrong way to do that." [0:49:26–0:50:00]
  - Speed of idea vs. validation: "But in one day, I had this method there and I thought this looks good. And then I spent some months there coding it, testing it, make sure that it really was better. And the more I tested it, the more I realized this is it." [0:50:00]
  - This confirms the CG link inferred above. In his own framing the thesis tried to "Transform quasin Newton into conjugate gradients", which he calls "the wrong way". L-BFGS instead keeps the quasi-Newton update and limits its storage; that second half is my reading [inferred], not his words.

**Why then** [inferred]
- Storage was the binding constraint in 1980 ("problems where the storage is critical").
- By 1989 the test machines were a SUN 3/60 and, for n = 5,000–10,000, the Alliant FX/8 at Argonne (preprint pp. 14–15). Memory, not flops, was scarce.
- Competing large-scale options (partitioned QN, truncated Newton) needed structure or Hessian products. L-BFGS needed only f and ∇f.

**Key insight** (the 1989 paper's own summary): L-BFGS is attractive because it uses "only function and gradient values" and because of its simplicity. "Their simplicity is one of their main appeals: they do not require knowledge of the sparsity structure of the Hessian, or knowledge of the separability of the objective function, and as we will see in this paper, they can be very simple to program." (preprint p. 3) [stated, primary]

**Minimum evidence**
- 1980: the abstract reports that "The resulting algorithms are tested numerically and compared with several well-known methods" [practice, primary: abstract via OpenAlex]. The interview describes months of coding and testing before submission (see Origin) [stated, caption-derived]. The 1980 test set and results were not read.
- 1989 [practice, primary: 1989 preprint]. The paper is mostly a **controlled numerical comparison**:
  - L-BFGS vs Buckley–LeNir;
  - four scaling strategies M1–M4, ranked per problem and tallied (Tables 12–13);
  - L-BFGS vs CONMIN and CG, counting CPU time;
  - L-BFGS vs the partitioned quasi-Newton method of Griewank–Toint.
- A global convergence proof is given for uniformly convex problems only (§7).
- It reports where L-BFGS **loses**: "Our tests have convinced us that the partitioned quasi-Newton method of Griewank and Toint is an excellent method for large scale optimization" (p. 24). And "for large problems with inexpensive functions, CG is competitive with L-BFGS" (p. 25).

**Abandoned paths** [practice, primary: 1989 preprint p. 15]:
- The Gill–Murray diagonal scaling: "In our tests this formula performed well sometimes, but was very inefficient in many problems. Its behavior seemed erratic, even if one included the safeguards suggested by Gill and Murray, and therefore we do not report these results."
- The more elaborate diagonal scaling M4 (suggested by Byrd, per the acknowledgements): "these two scalings are comparable in efficiency, and therefore M3 should be preferred since it is less expensive to implement." The cheaper option wins when performance ties.
- The paper names better dynamic scaling as open: "perhaps this is one of the most important topics of future research in large scale optimization."
- Earlier and larger abandoned path [stated, primary, caption-derived]: the whole thesis programme of CG-like extensions of quasi-Newton methods (see Origin). He calls it the "stepping stone": "what I really learned is that my PhD dissertation was not a failure but had been the stepping stone of that" [0:51:38–0:52:12]. The dissertation title (CV, Math Genealogy): "On the Method of Conjugate Gradients for Function Minimization" (Rice, 1978).

**Reception** [observed + practice]
- 1980 paper, refereeing [stated, primary, caption-derived]: "the reviews were not so good but the editor of the paper was Horge Mor [Jorge Moré] from Argon [Argonne]. he liked it and he made sure that it got published" [0:50:32]. Moré's editorial role is **not verified** from any other source.
- 1980 paper, early reception [stated, primary, caption-derived]: "it didn't register very much. There were a few a couple of people really like the paper. It it did not make much of an effect. It started becoming popular among engineers." [0:51:38]. On M. J. D. Powell: "he didn't like it for reasons that are a little bit technical" [0:52:48]. On Yann LeCun, met in Toronto in 1987: "he immediately coded it to train neural networks and uh he said no it didn't work well and that the stoastic grain [stochastic gradient] method is what worked then" [1:04:28].
- His conviction despite this: "I knew that it was right because I tried everything else." To students: "failures like this and building up knowledge are difficult to distinguish sometimes and you just have to live with that fog of uncertainty for a while" [0:52:12–0:52:48].
- 1989 paper: encouragement came before publication. "We are grateful to Jorge Moré who encouraged us to pursue this investigation" (p. 25).
- Gilbert and Lemaréchal ran similar experiments independently. The paper reports that their differences "are less pronounced than the ones reported in this paper" (p. 4), so a replication with a smaller effect is noted inside the paper.
- Code released as Harwell VA15 ("Our L-BFGS code will be made available through the Harwell library under the name VA15", p. 4).
- Today it is the most-cited journal paper in his record (§2.5).
- The bound-constrained code lives on in SciPy: "SciPy uses a C-translated and modified version of the Fortran code, L-BFGS-B v3.0 (released April 25, 2011, BSD-3 licensed)" [observed, secondary: SciPy docs].

**Follow-through and correction** [practice, primary]
- The 1994 compact representation (Byrd–Nocedal–Schnabel, doi:10.1007/BF01582063) is what made L-BFGS-B cost O(n) per iteration: "by making use of the compact representations of limited memory matrices described by Byrd, Nocedal and Schnabel [6], the computational cost of one iteration of the algorithm can be kept to be of order n" (L-BFGS-B preprint p. 3).
- In 2011 the team published a Remark: "an improvement and a correction to Algorithm 778 … The correction concerns an error caused by the use of routine dpmeps to estimate machine precision" (abstract via OpenAlex). Versions 2.1 and 3.0 are both kept downloadable (L-BFGS-B page).

**Method it shows** (cross-index, [inferred]):
1. Pick the method a user can run with the least problem information, and make it cheap per iteration.
2. Establish it by broad, honest head-to-head numerical tables, including where it loses.
3. Prove what can be proved (convex case).
4. Ship code and maintain it for decades.

### SW2. Convergence theory of quasi-Newton methods under practical line searches (1987, 1989) and the Acta Numerica survey (1992)

Papers:
- Byrd, Nocedal & Yuan, "Global Convergence of a Cass [sic, Crossref title] of Quasi-Newton Methods on Convex Problems", *SINUM* 24 (1987) 1171–1190, doi:10.1137/0724077 (**not read**; metadata only).
- Byrd & Nocedal, "A Tool for the Analysis of Quasi-Newton Methods with Application to Unconstrained Minimization", *SINUM* 26 (1989) 727–739, doi:10.1137/0726042 (**not read**; metadata only).
- Nocedal, "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1 (1992) 199–242, doi:10.1017/S0962492900002270 (author preprint read: introduction, §2, CG and variable-metric sections).

**Origin** [stated, primary: 2017 speech]
- Nocedal names this line as career-decisive: "Don gave me the opportunity to present some theoretical results on quasi-Newton methods, in the form of a plenary lecture, at a SIAM Meeting. … that experience proved to be decisive as it connected me with Mike Powell, whose vision of nonlinear optimization guides my research to this day."
- The CV lists "April 1989, Boston, Plenary talk at the SIAM Meeting on Optimization, Practical Convergence Results for Nonlinear Programming Algorithms". Identifying this as the plenary in the speech is [inferred].
- The CV also lists earlier talks titled "Analysis of Quasi-Newton Methods with Practical Line Searches" (Penn State, Oct 1985) and "Practical Convergence Results in Optimization" (Courant, Apr 1986) [practice, primary].

- 2026 interview [stated, primary, caption-derived]: "Mike Powell the great professor at Cambridge had written a paper after like 10-year effort he was able to prove convergence of the BFGS method the famous quasin Newton method on convex problems it's a beautiful paper and so I decided to work on Richard Bird [Byrd] on exploring this more because there were there's not only just one quasin Newton method there are many others" [0:57:15].

**Why then**: the 2026 account above confirms what was otherwise [inferred]. Powell's convex BFGS proof had just appeared, and DFP was "already observed to be not as good as the BFGS method" [0:57:15–0:57:49]; the open question was why.

**Key insight** (as he frames the whole enterprise in 1992) [stated, primary: Acta preprint]:
- The test for theory is the practitioner's question: "from the point of view of a user of nonlinear optimization routines, how interesting and practical is the body of theoretical analysis developed in this field?" He restricts attention to methods "that deserve to be in a subroutine library", asking "what do we know about the behavior of this method, as implemented in practice?" (p. 1).
- On what QN theory has achieved: "Ironically, our many theoretical studies of variable metric methods have not resulted in the discovery of new methods, but have mainly served to explain phenomena observed in practice." (p. 16)
- Also: "Variable metric methods, aside from being highly effective in practice, are intricate mathematical objects, and one could spend a lifetime discovering new properties of theirs" (p. 16).

**Minimum evidence**: the 1987/1989 papers were not read. His summary of the result [stated, primary, caption-derived]: "what the proof showed is that these quasin Newton methods were all good within the family of methods that goes between BFGS and DFP but excluding DFP. By the time you got a DFP, some self-correcting property was not there." [0:57:49]. Reception he reports: Powell "would send notes like I just read your paper with Richard Bird. This is the best paper I read all year." [1:02:50]

**Abandoned paths / set-asides** [practice, primary: Acta preprint p. 2]:
- The 1992 survey explicitly excludes noise: complete theory "should also take into account the effect of rounding errors, or noise in the function (Hamming 1971). However, we will not consider these aspects here, for this would require a much more extensive survey."
- He returned to exactly this topic 27 years later (SW5). The 2019 noisy-DFO paper uses "noise estimation techniques of Hamming (2012) and Moré and Wild (2011)" (arXiv:1803.10173 abstract).
- The link between the two is [inferred] but the citation continuity to Hamming is documented.

**Reception / prediction record**
- The 1992 prediction "I view the development of a comprehensive theory of conjugate gradient methods as one of the outstanding challenges in theoretical optimization, and I believe that it will come to fruition in the near future" (p. 10) [stated, primary].
- Whether it came true is **not assessed here** (handed to agent 05).

**Method it shows** [inferred]:
1. Theory is judged by whether it explains the behaviour of codes people actually use.
2. Analyse the practical version (inexact line searches, as implemented), not an idealized one.
3. Present results where the community gathers (plenaries, surveys).

### SW3. Interior-point / trust-region NLP → KNITRO (1999, 2000, 2006)

Papers:
- Byrd, Hribar & Nocedal, *SIOPT* 9 (1999) 877–900, doi:10.1137/S1052623497325107 (author preprint read: introduction, final remarks).
- Byrd, Gilbert & Nocedal, *Math. Program.* 89 (2000) 149–185, doi:10.1007/PL00011391 (**not read**).
- Waltz, Morales, Nocedal & Orban, *Math. Program.* 107 (2006) 391–408, doi:10.1007/s10107-004-0560-5 (**not read**).
- Byrd, Nocedal & Waltz, "Knitro: An Integrated Package for Nonlinear Optimization" (2006), doi:10.1007/0-387-30065-1_4 (author preprint dated July 6, 2005, read: introduction, §3.3, §6–7).

**Origin**
- The 1999 algorithm "is based on the framework proposed by Byrd, Gilbert and Nocedal [8]" and adapts "the trust region method of Byrd and Omojokun" for equality-constrained subproblems (preprint p. 2) [stated, primary].
- CV grants in 1996–2001 point to large constrained applications: DOE "Large Scale Optimization and its Application to Weather Forecasting" 1995–98; EDF "Interior Point Methods for Power Generation Schedules" 1998; Synopsys consulting 1998–2002. That these applications motivated the design is [inferred].
- 2026 interview [stated, primary, caption-derived]. He expected the extension to be routine and found it was not: "I thought well this is going to be straightforward the same people will apply them to nonlinear optimization and we're done well it turns out it's not so easy the ideas really extend directly to the convex case but in the non-convex case it doesn't work" [1:17:16].
- Order of work, as he tells it: "we started by developing a theory and that tells exactly how to scale everything. It was a trust region type of algorithm and so the theory was guiding at the side of the algorithm", with student Mary Beth Hribar coding in parallel [1:17:49]. "running the theory took two years and then Mike Powell spent almost a year reviewing the paper because he told us he wanted to find something wrong in it but he couldn't" [1:18:21]. Which paper Powell refereed is not named; the Byrd–Gilbert–Nocedal theory paper is the likely one [inferred].
- A competing effort ran in parallel: Vanderbei's LOQO (ASR "logo"/"loco") extended quadratic-programming ideas "with minimal changes" while "we were designing the elements from scratch using ideas from sequential quadratic programming … Vunder by [Vanderbei] finished first" [1:18:21–1:18:55].

**Why then** [inferred]: interior methods had just transformed LP. The 1999 introduction notes that recent nonconvex line-search IP methods were "quite recent, it is difficult to assess at this point whether they will lead to robust general-purpose codes" (p. 3). The gap was a robust *nonconvex* large-scale IP code.

**Key insight** [stated, primary: 1999 preprint p. 23]: "Rather than trying to mimic primal-dual interior point methods for linear programming, we have taken the approach of developing a fairly standard SQP trust region method, and introduced in it some of the key features of primal-dual iterations."

**Minimum evidence / design priority** [stated, primary]:
- Robustness first, speed later: "No attempt was made to obtain a rapidly convergent method: the barrier parameter was decreased at a linear rate, forcing the iterates of the algorithm to converge linearly" (p. 23).
- Benchmark: Hock–Schittkowski test problems (HS2, HS3, … in the preprint's tables) plus large problems, compared against LANCELOT ("competitive on large problems with a production code such as LANCELOT", p. 23).

**Abandoned or deferred paths** [stated, primary: 1999 preprint p. 23]:
- Superlinear barrier updates were deferred ("We are currently developing [7] various mechanisms to accelerate the iteration").
- The linear-system refinement was flagged as "very conservative (in that it demands very tight accuracy) and leads to high execution times on some problems".
- The primal variant lost to the primal-dual variant: "the primal-dual version of the algorithm is superior to the primal version" (p. 2).

**From algorithm to product** [practice + stated, primary]:
- CV: "2001 Co-founder and President, Ziena Optimization Inc.; 2001 Co-Developer, KNITRO software package; 2002–present Chief Scientist".
- The 2006 paper's design thesis: "These packages are, however, constrained by the underlying algorithm, and as is well known, no single approach is uniformly successful in nonlinear optimization" (p. 1).
- KNITRO therefore integrates two interior methods and an SLQP active-set method with crossover. The analogy is explicit: "The impressive success of an integrated approach of this sort for linear and integer programming, particularly over the past decade [21, 23], argues for a similar approach to be taken in nonlinear optimization" (p. 2).
- On the merit function: "Our numerical experience has shown that the choice of the merit parameter ν plays a crucial role in the efficiency of the algorithm" (p. 11).
- 2026 interview on the code and the company [stated, primary, caption-derived]:
  - Waltz "inherited the code and he told me this code is complete spaghetti now. [laughter] … Can I just write it from scratch? So he did" [1:18:55–1:19:29].
  - Why commercial: "to continue to make it into a good code it had to become commercial. It couldn't stay in academia because we couldn't know who to fund it" [1:19:29].
  - "eventually the the code was sold to a French company called Artillis [Artelys]", with "applications primarily in power systems first" [1:20:00].
  - The name: NITRO stood for "nonlinear interior trust region optimizer"; the K was added at commercialization because "nitro is a terrible name" [1:20:36].

**Stated limitation → later research** [stated, primary + inferred link]:
- The 2006 paper admits: "infeasibility detection is a very difficult problem for nonlinear constraints, and the algorithms in Knitro cannot distinguish between infeasible problems and convergence to an (infeasible) stationary point for a measure of feasibility" (p. 20).
- Follow-ups: Byrd, Curtis & Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization" (*SIOPT* 2010, doi:10.1137/080738222), and Nocedal, Öztoprak & Waltz, "An interior point method for nonlinear programming with infeasibility detection capabilities" (*OMS* 2014, doi:10.1080/10556788.2013.858156).
- That the software gap *caused* these papers is [inferred] from timing and topic.

**Reception** [observed, secondary]
- McCormick 2017: KNITRO "is used in the energy, computer, and financial industries to optimize everything from the design of computer chips to the production and delivery of electricity".
- CV/bio: consulting for Artelys from 2012 or 2014 (two CV versions disagree).
- The 2024 DOE SCOPF report names "Artelys Knitro" as the NLP engine (doi:10.2172/2404586).

**Method it shows** [inferred]:
1. Build from a globally convergent framework you already analysed (Byrd–Gilbert–Nocedal), and prefer robustness over asymptotic speed in a first code.
2. Borrow architecture from a field where it already worked (LP/MIP integration → NLP integration).
3. Write down the code's known failure modes and turn them into the next papers.

### SW4. The machine-learning turn (2010–2018): stochastic Hessian information → SIAM Review survey

Papers:
- Byrd, Chin, Neveitt & Nocedal, *SIOPT* 21 (2011) 977–995, doi:10.1137/10079923X (**not read**; self-selected in the NSF bio).
- Byrd, Chin, Nocedal & Wu, *Math. Program.* 134 (2012), doi:10.1007/s10107-012-0572-5 (**not read**).
- Byrd, Hansen, Nocedal & Singer, arXiv:1401.7020 / *SIOPT* 26 (2016), doi:10.1137/140954362 (abstract read).
- Bottou, Curtis & Nocedal, arXiv:1606.04838 / *SIAM Rev.* 60 (2018), doi:10.1137/16M1080173 (arXiv v1 read: abstract, contents, §4.5, §8).
- Keskar et al., arXiv:1609.04836 (ICLR 2017) (abstract read).

**Origin** [practice, primary: CV]:
- Google grants "Large-Scale Optimization Methods for Machine Learning" (Jan–Dec 2010, $70,000) and "New Optimization Solvers for Machine Learning Applications" (2011–12, $40,000).
- Talks: "A Sub-sampled Hessian Newton Method for Large-Scale Statistical Training, Google" (Nov 2010) and "A Semi-Stochastic Method for Machine Learning", ICCOPT plenary (Aug 2010).
- Consulting: Google 2012–2014.
- Co-author Will Neveitt "(Google Research)" (NSF bio).
- 2026 interview [stated, primary, caption-derived]:
  - "I was contacted by Google around 2008 … for the same reasons as the weather forecasting. There was a group that was doing speech recognition before neural networks and um they were using an optimizer and they contacted me because I knew about LBFGS. How can we use LBFGS here? And my first thing is don't use LBFGS here and so I started getting quite interested in the problem." [1:21:43–1:22:16]
  - He nearly joined Google around 2009 ("one of the VPs asked me to join"), then consulted instead [1:22:50].
  - This confirms the Google origin that the CV records only suggest.

**Why then** [inferred]: large-scale logistic regression and speech/vision models at Google and IBM made batch vs. stochastic a live design question. Second-order and quasi-Newton methods, his home ground, were the non-SG alternative.

**Key insight**
- 2014 stochastic QN abstract: "The direct application of classical quasi- Newton updating techniques for deterministic optimization leads to noisy curvature estimates that have harmful effects on the robustness of the iteration." The fix: curvature collected "pointwise, and at regular intervals, through (sub-sampled) Hessian-vector products" (arXiv:1401.7020) [stated, primary].
- The 2018 survey argues that ML "represents a distinctive setting in which the stochastic gradient (SG) method has traditionally played a central role while conventional gradient-based nonlinear optimization techniques typically falter" (abstract) [stated, primary].
- But: "it would be premature to conclude that SG is a perfect solution for large-scale machine learning problems. There is, in fact, a large gap between asymptotical behavior and practical realities" (arXiv v1 p. 36, §4.5) [stated, primary].

**Minimum evidence** [practice, primary]: the survey is built around two case studies (text classification via convex optimization; deep neural networks) before any theory (contents, §2).

**Abandoned or reframed paths** [practice, primary]:
- The progressive-batching paper states the prior consensus against his home method: "L-BFGS is currently not considered an algorithm of choice for large-scale machine learning applications. One need not, however, choose between the two extremes represented by the full batch or highly stochastic regimes" (arXiv:1802.05374 abstract). He reframes rather than concedes.
- Several ML-era lines stop after 1–3 papers: ℓ1 second-order methods 2012–2016; sparse inverse covariance 2012–2013; Newton-sketch 2017/2020. Whether they were deliberately dropped is [inferred] from the record.

**Reception** [observed, secondary]:
- 2021 Lagrange Prize in Continuous Optimization (MOS–SIAM) for the SIAM Review paper. The committee (Leyffer chair; Chen, de Klerk, Gill) cited "a foundational and insightful review of optimization methods for large-scale machine learning, including a new perspective for the simultaneous consideration of noise reduction and ill-conditioning and the foundations and analysis of second-order stochastic optimization methods for machine-learning" (Lehigh ISE news, 2021; the McCormick news item of 6 Apr 2021 confirms the award and paper but does not carry this wording).
- The survey took 20 months from arXiv v1 (June 2016) to v3 (Feb 2018). A public errata page existed by June 2016 (two equation-reference corrections) [practice, primary].
- The large-batch paper (Keskar et al.) was **contested**. Dinh, Pascanu, Bengio & Bengio, "Sharp Minima Can Generalize For Deep Nets", arXiv:1703.04933, name Keskar et al. (2017) as an instance of the flatness hypothesis and argue "that most notions of flatness are problematic for deep models and can not be directly applied to explain generalization" [observed, secondary]. No written response by Nocedal or his co-authors was found. In a 2024 talk he still stands by the result, with a qualifier: "Well, here's an example that we produced um in 2017 and it's still valid today to some extent", and "it is known now after many years in the area of machine learning is that if you can encourage your optimization algorithms to go to flat minimizers, you are in fact going to get better generalization." [0:25:05–0:25:39, `../sources/talks/2024-10-25_nitmb-seminar-train-dnns_XrX7MEMbdYw.txt`] [stated, primary, caption-derived]

**Retrospective self-critique** (2026 interview) [stated, primary, caption-derived]:
- "a regret that I have is that in all these collaborations where eventually I was able to write a couple of papers that were influential in the field but other than that I wrote a number of papers I never understood that there had to be a balance between the statistical aspect of the problem and the geometry of the problem." [1:26:13]
- "machine learning people developed methods like Adam and so on that dealt with the statistical aspect of it but they're not satisfactory." [1:27:20]
- On architecture vs. algorithm: "That took me also too long to understand that if you say I'm going to improve the training process, you can do it by different two different things. One of them is change the architecture so it's easier to optimize and the other one is just find a better optimization algorithm." [1:43:00]
- This is the clearest stated *failure* in his record: a deterministic optimizer's instinct ("learn the geometry") was, by his own account, insufficient for ML.

**Method it shows** [inferred]:
1. Enter a new field through its practitioners' problems (industry grants and co-authors).
2. Write the field's map (survey with case studies) and your own method's place on it.
3. Adapt the classical deterministic machinery (QN updating, sampling control, line search) rather than invent from scratch.

### SW5. The noise program (2018 → 2025): noisy DFO, noise-tolerant BFGS, finite differences re-examined, design guidelines

Papers (abstracts read on arXiv; bodies **not read**):
- Berahas, Byrd & Nocedal, *SIOPT* 29 (2019), doi:10.1137/18M1177718 (arXiv:1803.10173).
- Xie, Byrd & Nocedal, *SIOPT* 30 (2020), doi:10.1137/19M1240794.
- Shi, Xie, Byrd & Nocedal, *SIOPT* 32 (2022), doi:10.1137/20M1373190 (arXiv:2010.04352).
- Shi, Xuan, Öztoprak & Nocedal, *OMS* 38 (2023), doi:10.1080/10556788.2022.2121832 (arXiv:2102.09762).
- Sun & Nocedal, *Math. Program.* 202 (2023), doi:10.1007/s10107-023-01941-9.
- Lou, Sun & Nocedal, *SISC* 47 (2025), doi:10.1137/24M1632279 (arXiv:2401.15007).

**Origin** [stated, primary: arXiv abstracts]:
- 2020 noise-tolerant QN: "motivated by applications that contain computational noise, employ low-precision arithmetic, or are subject to statistical noise. The classical BFGS and L-BFGS methods can fail in such circumstances because the updating procedure can be corrupted and the line search can behave erratically."
- The CV lists "September 2017, Zero-Order Methods for Nonlinear Optimization, Simons Institute, Berkeley" [practice, primary], which places the DFO turn by 2017.
- In that Simons talk (uploader-provided subtitles) he frames the approach as the one left standing, and as a risk: "And after trying everything else, I see that the only way I know how to do that is going back to Quasi-Newton methods. So, we're gonna go and do Quasi-Newton methods with finite differences in the noisy case, something that people have considered to be a very risky thing to do." [0:02:18, `../sources/talks/2017_simons-zero-order-dynamic-sampling_OfVZ9gArXiY.txt`] [stated, primary, caption-derived]
- UCLA seminar 2021 (ASR), on why finite differences were neglected: "it was dismissed by the optimization community by saying that it's too expensive to do n-function evaluations and finite differences just to get a gradient and that would be unreliable" [0:16:37–0:17:10, `../sources/talks/2021-04-08_ucla-cs201-seminar_4a12aV77CAI.txt`] [stated, primary, caption-derived]

**Why then** [inferred]: the stochastic ML work (SW4) had just forced him to make QN updating robust to noisy curvature. Low-precision hardware and simulation-based engineering design (the robust-design application) supplied deterministic-noise versions of the same problem.

**Key insight** [stated, primary]:
- Keep the classical method, add noise awareness. The 2024/2025 paper "advocates for strategies to create noise-tolerant nonlinear optimization algorithms by adapting classical deterministic methods. These adaptations follow certain design guidelines described here, which make use of estimates of the noise level in the problem" (arXiv:2401.15007).
- Concretely:
  - a "lengthening procedure that spaces out the points at which gradient differences are collected" (arXiv:2010.04352);
  - a noise-aware trust-region acceptance test (arXiv:2411.02665);
  - FD intervals set from a noise estimate (arXiv:1803.10173, 2110.06380).

**Minimum evidence** [practice, primary]: the 2021/2023 FD study is an 82-page benchmarking paper ("82 pages, 38 tables, 29 figures", arXiv comment). It compares "NEWUOA, DFO-LS and COBYLA against the finite-difference approach on three classes of problems" (abstract).

**Contrarian claim** [stated, primary]: "The use of finite differences has been largely dismissed in the derivative-free optimization literature as too expensive in terms of function evaluations and/or as impractical when the objective function contains noise. The test results presented in this paper suggest that such views should be re-examined and that the finite-difference approach has much to be recommended." (arXiv:2102.09762)

**Abandoned or reframed paths** [practice, primary]:
- The robust-design paper's earlier title "Noise-Tolerant Optimization Methods for the Solution of a Robust Design Problem" (DBLP CoRR record, presumably v1; not checked against the arXiv v1 PDF) became, by v2 (Oct 2024) and in *SISC*, "Design Guidelines for Noise-Tolerant Optimization with Applications in Robust Design". The contribution was reframed from one application to general guidelines.
- 2019 admission: the noise estimate and choice of h "are inexpensive but not always accurate, and to prevent failures the algorithm incorporates a recovery mechanism" (arXiv:1803.10173 abstract).

**Reception** [observed, secondary: Semantic Scholar counts on 2026-09-28]: 105 citations for the 2019 paper and 38 for the 2022 paper. Modest compared with SW1–SW4, and early. Peer response from the model-based DFO community to the FD claim is **not found here** (agent 05; cf. the team's dfo-team).

**Method it shows** [inferred]:
1. When a new regime breaks your classical method, locate exactly which component fails (update, line search, differencing interval).
2. Make that component noise-aware using an explicit noise estimate.
3. Prove convergence to a noise-determined neighbourhood.
4. Defend the result with large head-to-head benchmarks against the incumbent methods.

### SW6 (short). Variational data assimilation for weather forecasting (1990s–2009): his self-rated most important practical contribution

Included because he calls it his most important contribution, although citation-based selection would miss it. Evidence is thin; this is not a full dissection.

- **Record** [practice, primary]:
  - CV grants: DOE "Optimization and Eigenvalue Computations with Application to Meteorology and Oceanography" (1992–95); DOE "Large Scale Optimization and its Application to Weather Forecasting" (1995–98); NSF "Improved Minimization Techniques in Meteorological Data Assimilation" (2001–03).
  - CV talk: 1993 plenary "Optimization Calculations with Applications to Meteorology and Oceanography".
  - Paper: Fisher, Nocedal, Trémolet & Wright, "Data assimilation in weather forecasting: a case study in PDE-constrained optimization", *Optim. Eng.* 10 (2009) 409–426, doi:10.1007/s11081-008-9051-5 (Crossref 61 citations; **not read**).
- **Stated account** (2026 interview, caption-derived) [1:12:21–1:16:44]:
  - The ECMWF effort replaced Kalman filtering with variational assimilation, "a nonlinear le squares problem" with "almost a million" variables in the 1990s.
  - He worked on site: "for a number of years I was going to France and England several times a year working in person with the engineers there and eventually we developed a multi-level Gaus Newton method with a spectral preconditioner".
- **Key judgement: exploit problem structure, even against your own method.** He was approached because of L-BFGS but steered them to Gauss–Newton: "when you have a nonlinearly squares problem it has a very special hessen [Hessian] and so you want to the gaus Newton matrix is is the right way of exploiting the hessen not a quasin approximation". "when the problem has a structure like a nonlinearly square structure, you have to exploit it." "the best way to convince them is by getting better numbers with something else, right?" [1:15:39–1:16:44]
- **His view of how breakthroughs happen**, stated here. The caption reads: "People sometimes say you know the big discoveries in science are done by a multid-disciplinary group of people with complimentary expertises. I don't believe that the big discoveries in science are usually done by one or two people quietly in a corner nobody paying attention and then when the big ideas come there's a team that goes and develop this" [1:14:34–1:15:07].
  - Because the ASR drops sentence boundaries, the likely reading is: he does *not* believe the multidisciplinary-team claim; big discoveries come from one or two people working quietly, and teams then develop them. This reading is [inferred] from the context (he goes on: "Hinton and Leon [LeCun] were doing the quiet revolutionary work"). Check the audio before quoting.
- **Method it shows** [inferred]: when the client asks for your famous method, benchmark it against the structure-exploiting alternative and let the numbers decide.

---

## 4. Failures, corrections, abandoned directions, contested claims

### 4.1 Published corrections and errata [practice, primary]
- **L-BFGS-B Remark (2011)**: "an improvement and a correction to Algorithm 778 … The correction concerns an error caused by the use of routine dpmeps to estimate machine precision" (doi:10.1145/2049662.2049669; abstract via OpenAlex). Released 14 years after Algorithm 778. The L-BFGS-B page keeps v2.1 and v3.0 side by side.
- **Book errata**: homepage book page links "Errata2 (Second edition, August 2006)" and "Errata1 (First edition, January 2000)" (contents not read).
- **SIAM Review errata** (June 30, 2016): two equation-reference fixes in Chapter 5 (`PDFfiles/opt_ml_errata.pdf`, read).

### 4.2 Papers about failure [practice, primary]
- Byrd, Marazzi & Nocedal, "On the convergence of Newton iterations to non-stationary points", *Math. Program.* 99 (2004), doi:10.1007/S10107-003-0376-8 (preprint intro read): "Our view is that, when methods fail in practice, there is often apparent convergence to a spurious solution, or at least, negligible progress toward the solution" (preprint p. 2).
- The CV lists a related talk titled "The Dark Secrets of Newton's Method" (INRIA, Nov 2000).
- Nocedal, Sartenaer & Zhu, "On the Behavior of the Gradient Norm in the Steepest Descent Method", *COAP* 2002, doi:10.1023/A:1014897230089 (not read).

### 4.3 Directions entered and left

Based on the publication record. Reasons for leaving are **not stated** in any source found, so each is [inferred].

| Direction | Active | Evidence | Last item |
|---|---|---|---|
| PhD thesis programme: CG-like limited-storage extensions of quasi-Newton methods | 1976–1978 | Thesis (CV); 2026 interview [0:46:37–0:47:11]: "a impressive collection of failed ideas" [stated] | Abandoned in 1978 for L-BFGS (SW1) |
| Reduced-Hessian / projected-Hessian SQP (with Overton at Courant; later Byrd, Biegler) | 1983–2000 | doi:10.1137/0722050; doi:10.1007/BF01588794; doi:10.1137/0805017; 2026 interview [0:55:01–0:55:34]: "the algorithms that we proposed with Michael Overton are not the best thing now they're not considered the best thing those type of reduced methods" [stated] | 2000 (doi:10.1023/A:1008723031056) |
| Inverse eigenvalue problems (with Overton, Friedland) | 1982–1987 | CV items 82, 85, 91; doi:10.1137/0724043 | 1987 |
| Conic methods / conic termination | 1983–1989 | doi:10.1137/0906019 (Crossref 19 citations); doi:10.1137/0910001 (15 citations) | 1989. Low uptake; not revisited. |
| Nonlinear equations via LP (with Duff, Reid) | 1987 | CV item 84 | 1987 |
| Metacomputing / NEOS / iNEOS | 1997–2002 | CV grant "Metacomputing Environments for Optimization" ($1.8M, NSF 1997–2000); iNEOS paper 2002 (CV); DBLP "Solving Optimization Problems Using Parallel and Grid Computing", ENC 2003, doi:10.1109/ENC.2003.1232866 | 2003 |
| Model-based DFO with geometry control (Wedge, geometry phase) | 2002–2009 | doi:10.1007/S101070100264; doi:10.1080/10556780802409296 | 2009, **then reversed** toward finite-difference DFO in 2019+ (SW5), with model-based returning in 2024 (feasible constrained DFO, arXiv:2402.11920) |
| LCPs: American options, rigid bodies | 2007–2013 | doi:10.1007/S00211-008-0183-5; doi:10.1080/10556788.2010.514341; doi:10.1137/110845094 | 2013 |
| PDE-constrained / data assimilation | 1993–2009 | DOE and NSF grants; doi:10.1007/s11081-008-9051-5 | 2009 |
| ℓ1-regularized second-order methods | 2012–2016 | doi:10.1007/S10107-015-0965-3; doi:10.1080/10556788.2016.1138222 | 2016 |

### 4.4 Stated limitations inside signature papers [stated, primary]
- NITRO 1999: deliberately linear convergence; conservative, slow linear-system refinement (p. 23).
- KNITRO 2006: cannot distinguish infeasibility from convergence to an infeasible stationary point (p. 20).
- L-BFGS 1989: loses to partitioned QN on problems with small element functions; CG competitive when functions are cheap (pp. 24–25).
- Geometry 2009: the evidence is for "smooth unconstrained optimization problems with dimensions ranging between 2 and 15" (abstract), and it is unclear whether it transfers to NEWUOA's 2n+1 points: "It remains to be seen whether the observations made in this paper apply also in that context" (p. 9).

### 4.5 Contested or unverified claims
- **Large-batch / sharp minima (2017)**: contested by Dinh et al. 2017 (arXiv:1703.04933) [observed, secondary]. No response by Nocedal found.
- **1992 CG-theory prediction** ("will come to fruition in the near future"): outcome not assessed.
- **Geometry phase (2009)**: the paper suggests the geometry phase "should be re-examined. Perhaps it may be preferable to employ it only as a method of last resort; not as an integral part of the algorithm" (p. 9). It won the Broyden Prize (CV, NSF bio). How the DFO community received the *claim* was not checked.
- **Rejected papers**: none found in any public record (see Gaps).

### 4.6 Bibliographic hygiene (for later harvest steps)
- OpenAlex attributes to him "Small sample composite fault diagnosis of hydraulic bearings based on improved VME algorithm and mRVM" (*Journal of applied artificial intelligence*, 2024, doi:10.59782/aai.v1i2.296). Co-authors: "Matthew B. Baker, Elizabeth King, Joshua Perez"; no institution.
- The topic is far from all his work and it appears in no primary list. **Treat as misattribution; excluded.** The attribution was checked through the OpenAlex API; whether the paper itself is genuine was not investigated.
- The OSTI SCOPF report (doi:10.2172/2404586), by contrast, is institution-matched (Northwestern, DOE-sponsored, names Artelys Knitro) and is kept.

---

## 5. Era and resource context of the practices

| Era | Compute / tools | Team and seniority | Funding and partners (CV) |
|---|---|---|---|
| 1978–1983 | Storage-limited mainframes. 1980 abstract: "problems where the storage is critical". | Early career: solo or one co-author; UNAM, then Courant | NSF–CONACyT cooperative program 1980–81 |
| 1983–1995 | SUN 3/60 workstation; Alliant FX/8 at Argonne for n ≤ 10⁴ (1989 preprint pp. 14–15). Distribution through the Harwell library (VA15); CUTE-type test sets. Consulting for Harwell/UKAEA (1983, 1988). | Assistant → full professor; 1–2 PhD students per paper; Byrd as constant co-author | DOE grant DE-FG02-87ER25047 renewed repeatedly from 1987 (CV suffixes A001–A008; still cited in the 2016 SIAM Review footnote); NSF |
| 1995–2012 | NEOS server; Optimization Technology Center (Argonne–Northwestern joint venture, per the L-BFGS page); Fortran → C packages; commercial code (KNITRO 2001–) | Senior; startup (Ziena) co-founder and chief scientist; postdocs (Morales, Orban, Zhu, Goux) | NSF, DOE, Sandia, EDF, Intel ("Parallel Nonlinear Optimization Algorithms" 2005–08); consulting for Synopsys, Accenture, Chevron-Texaco |
| 2010–2019 | Industrial ML at data-centre scale; GPUs; distributed training (the survey's "Opportunities for Distributed Computing"); NIPS/ICML/ICLR | Department chair 2013–17; larger student cohort (Chin, Hansen, Solntsev, Keskar, Berahas, Bollapragada, Shi, Xie) | Google (2010–12 grants; consulting 2012–14), Intel ($150k 2016–18), ONR ($440k 2015–18; $421.9k 2018–20), NSF, DOE |
| 2020–2026 | Low-precision arithmetic; simulation-based design; power-grid SCOPF with Artelys Knitro | Very senior (NAE 2020); two- to three-author papers with a student first | Not read (CV stops c. 2018). DOE (SCOPF report). |

**Transfer warning** [inferred]: the 1989 L-BFGS practice (scale tests on n ≤ 10⁴, one workstation, ranking tables) and the 2010s ML practice (industry-scale data, company co-authors) both depended on access that a user of this skill may not have. The Byrd collaboration is a person-specific resource no method can copy.

---

## 6. Candidate research-craft patterns for Phase 2 (all [inferred]; to be tested against 02-methodology and 03-process-evidence)

1. **Practitioner-first test of theory**: judge an analysis by whether it explains codes "as implemented in practice". Evidence: Acta 1992 p. 1 and p. 16 [stated]; QN theory on practical line searches (1987, 1989 titles); 2017 speech ("algorithmic innovation comes through numerical experimentation and mathematical analysis").
2. **Honest head-to-head benchmarking, including losses**. Evidence: 1989 L-BFGS vs PQN/CG; 2009 geometry study; 2021/2023 82-page FD study; NITRO vs LANCELOT.
3. **Keep the classical method; repair the component that breaks**. Evidence: stochastic QN (2014) → progressive-batching L-BFGS (2018) → noise-tolerant BFGS (2020/22) → design guidelines (2024/25); noisy Byrd–Omojokun (2024).
4. **Cheapest adequate choice wins ties**. Evidence: M3 over M4 (1989); "only function and gradient values"; KNITRO defaults.
5. **Software as the end product, maintained long-term**. Evidence: VA15, Algorithm 778 plus the 2011 Remark, PREQN, CG+, KNITRO.
6. **Borrow architecture from a neighbouring success**. Evidence: LP/MIP integration → KNITRO (2006 p. 2); SQP inside interior methods (1999 p. 23).
7. **Revisit what the community dismissed, with data**. Evidence: geometry phase (2009); finite differences (2021/2023); L-BFGS in ML (2018).
8. **Exhaust alternatives, then commit, and tolerate the "fog of uncertainty"**. Evidence: thesis → L-BFGS (2026 interview); "after trying everything else … going back to Quasi-Newton methods" (Simons 2017) [stated, caption-derived]; the 1989 paper's reported negative results on scalings.
9. **Exploit structure even against your own method**. Evidence: Gauss–Newton over L-BFGS at ECMWF; "don't use LBFGS here" at Google (2026 interview) [stated, caption-derived]; the 1989 paper recommending partitioned QN when element structure is available [practice].
10. **Enter fields through practitioners' problems**. Evidence: the Google/IBM/Intel ML period; EDF/DOE/Synopsys in the interior period; weather forecasting and data assimilation.

---

## Contradictions (kept, not reconciled)

1. **Authorship of the 1995 L-BFGS-B paper.** Crossref, DBLP and the author preprint (NAM-08, rev. May 1994) list **Byrd, Lu, Nocedal and Zhu**. Nocedal's CV (item 66), his L-BFGS-B software page and the SciPy docs (which copy it) list only "R. H. Byrd, P. Lu and J. Nocedal".
2. **Volume of Waltz–Morales–Nocedal–Orban.** CV and homepage say "*Mathematical Programming* A, Vol. 102, pp. 391–408 (2006)"; Crossref says vol. **107**, pp. 391–408 (2006). Author order also differs: homepage alphabetical (Morales, Nocedal, Orban, Waltz); journal Waltz first.
3. **Years.**
   - "Adaptive Barrier Update Strategies": CV item 27 says 2008, homepage and DBLP say 2009.
   - "A Sequential Quadratic Programming Algorithm with an Additional Equality Constrained Phase": CV and Crossref "issued" say 2011, the print volume 32 is 2012.
   - Morales–Nocedal–Wu is listed under 2011 in the NSF bio.
4. **Titles in the CV vs. the journal.**
   - CV item 41 "An Active-Set Algorithm for Nonlinear Programming Using Linear Programming and Equality Constrained Subproblems" vs. journal "An algorithm for nonlinear optimization using linear programming and equality constrained subproblems".
   - CV item 39 "On the Convergence of Successive Linear Programming Algorithms" vs. journal "…Successive Linear-Quadratic Programming Algorithms".
   - CV item 32 "Steering Penalty Methods" vs. journal "Steering exact penalty methods for nonlinear programming".
5. **Consulting dates for Artelys / Ziena.** CV c. 2018: "2012–present Artelys; 2001–2012 Ziena Optimization LLC". Bio c. 2021: "2014–present Artelys Corp; 2001–2014 Ziena Optimization Inc".
6. **Student record details.**
   - Math Genealogy lists "Chen, Peihuang" (1992) where the CV lists "Peihuang Lu, Ph.D. 1992".
   - Hribar: CV 1995 vs MGP 1996.
   - López-Calva: CV 2006 vs MGP 2005.
   - The CV spells "Todd Plantega", DBLP "Todd D. Plantenga".
7. **Citation counts** for the same paper differ by up to 40% across OpenAlex, Crossref and Semantic Scholar (§2.5). No single number is authoritative.
8. **Self-description vs. prize category.** He accepted a *theory* prize while saying "I am not a pure theoretician … I am just as much a computer scientist who likes to create software" (McCormick 2017). The 1992 survey, by contrast, is pure theory commentary, and the speech credits QN *theory* results as career-decisive. Both self-images are on record.
9. **DFO stance over time.**
   - 2009: model-based DFO "have proved to be effective techniques" (geometry preprint p. 2), citing Moré–Wild's finding that NEWUOA is "overall the most effective method—in many cases by a very wide margin" (p. 9).
   - 2021/2023: finite differences, "largely dismissed", should be re-examined against NEWUOA, DFO-LS and COBYLA.
   - 2024: back to a model-based (interpolation) method for constrained DFO (arXiv:2402.11920).
   Not necessarily inconsistent (different problem regimes), but the emphasis shifts.
10. **What theory should do: 1992 vs. 2026.**
    - 1992 (Acta preprint p. 2): "Global efficiency is an area that requires more attention and where important new results can be expected." Global efficiency includes studying "the worst case global behavior of the methods".
    - 2026 interview (caption-derived): "recently the field has become focusing on complexity results … some of those results actually are even lacking intuition. They're not distinguishing between good methods and bad methods." [1:28:28–1:29:02]
    - The two are compatible if the complaint is about complexity results that fail his 1992 test ("how well can it differentiate between efficient and inefficient methods", Acta p. 2). Still, the call for more complexity-type theory became a critique of it.
11. **Sharp minima (2017).** Dinh et al. (arXiv:1703.04933) argue that flatness notions "can not be directly applied to explain generalization". Nocedal in 2024 (caption-derived): the example "it's still valid today to some extent", and encouraging flat minimizers gives "better generalization". Both positions stand; this file does not adjudicate.
12. **Self-rated importance vs. citation record.** He calls the ECMWF data-assimilation work "my most important contribution" in practical impact (2026 interview). Its only paper found in his record (Fisher et al. 2009) has 61 Crossref citations, against about 7,000 for L-BFGS. Any selection of signature works by citations alone misses what he values most (SW6).
13. **L-BFGS reception.** Now his most-cited paper; by his account (2026 interview) the 1980 version "didn't register very much", had reviews that "were not so good", was disliked by Powell, and failed LeCun's 1987 neural-network test. Both the early indifference and the later dominance are on record.

## Gaps (could not find or did not read)

1. **Google Scholar profile not read**: WebFetch redirected to the Google "sorry" bot-check page. Scholar citation counts and any Scholar-only items are missing.
2. **Semantic Scholar author-level statistics** not read (HTTP 429).
3. **Bodies not read**:
   - the 1980 *Math. Comp.* paper (AMS Cloudflare challenge; abstract only);
   - the 1987 and 1989 *SINUM* QN-theory papers;
   - Byrd–Gilbert–Nocedal 2000;
   - Waltz et al. 2006;
   - the 2011 stochastic-Hessian paper;
   - all noise-program papers (abstracts only);
   - *Numerical Optimization* (either edition, including prefaces).
   Origin, minimum-evidence and abandoned-path claims for these rest on abstracts, CV records or inference, as marked.
4. **Origin stories come from one caption-derived interview.** The WebSearch for an interview found nothing. The origin accounts for L-BFGS, the QN theory, KNITRO, the Google/ML turn and ECMWF all come from the March 2026 interview transcript (`../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt`), which is automatic ASR, not human-checked. They are late retrospective accounts (about 45 years after L-BFGS) and he himself warns "my memory tends to really distort things" [0:46:03]. No contemporaneous account (letters, early talks, referee reports) was found to cross-check them. Moré's role as editor of the 1980 paper is unverified.
5. **Dantzig Prize 2012 citation** not read (mathopt.org pages render empty to curl and WebFetch). The Broyden Prize citation was not read either; the award is known only from the CV.
6. **Rejected papers, referee reports, arXiv v1-vs-final diffs**: none examined beyond submission histories and the robust-design title change. No record of rejected submissions found.
7. **Reasons for leaving directions** (§4.3) are nowhere stated. The reason for the post-2020 switch in author-order convention is not stated.
8. **Affiliations of industry co-authors** other than Neveitt (Google), Smelyanskiy (Intel) and Bottou (Facebook AI Research) are not verified.
9. **Output after Nov 2024**: no arXiv preprints found; the 2025–2026 journal items are both from 2024 preprints. The March 2026 interview explains this as a deliberate pause while he works on the book's third edition (§2.6). Whether he still takes students, and when the third edition appears, is unknown.
11. **Unverified honour.** The interviewer's introduction (2026 interview [0:00:05–0:00:38]; ASR "2024 John Fonoyman prize by Siam") credits him with a 2024 SIAM John von Neumann prize. This is not in either CV version and was not checked with any other source.
12. **Transcripts not read in full.** Only the 2026 interview was read closely (0:37–1:48). The Simons 2017, UCLA 2021 and NITMB 2024 transcripts were searched by keyword. The Purdue 2017, RIIAA 2019 and SIAM AN14 transcripts were not read by this agent; they belong to agent 02's methodology file.
10. **KNITRO corporate history** (Ziena → Artelys) beyond the CV lines is not verified.

## Sources

Retrieval date for all: 2026-09-28. P = primary, S = secondary.

**Profiles, lists and databases**
1. DBLP person record `n/JorgeNocedal`, via SPARQL (`scripts/dblp_works.py`), 83 records — https://dblp.org/pid/n/JorgeNocedal.html — S (bibliographic)
2. OpenAlex author A5081856145 (`scripts/fetch_publications.py`; output in `../sources/publications/publications.md`, `abstracts.md`) — https://openalex.org — S
3. Crossref REST API metadata for ~50 DOIs listed in this file — https://api.crossref.org — S
4. Semantic Scholar Graph API, paper records for 7 DOIs — https://api.semanticscholar.org — S
5. arXiv author search "Nocedal, Jorge" (21 results) and abs pages for 1401.7020, 1605.06049, 1606.04838, 1609.04836, 1609.08502, 1705.06211, 1710.11258, 1802.05374, 1803.10173, 1901.09063, 2010.04352, 2012.15411, 2102.09762, 2110.04355, 2110.06380, 2201.00973, 2401.15007, 2402.11920, 2411.02665 — https://arxiv.org/search/?query=Nocedal%2C+Jorge&searchtype=author — P (author preprints)
6. Google Scholar profile gGNxMZ0AAAAJ — https://scholar.google.com/citations?user=gGNxMZ0AAAAJ — **not read** (bot-check redirect)
7. Mathematics Genealogy Project, id 43740 — https://mathgenealogy.org/id.php?id=43740 — S

**Nocedal's CVs, homepage and software pages**
8. J. Nocedal, Curriculum Vitae (c. 2018) — http://www.ece.northwestern.edu/~nocedal/CV/cv_nocedal.pdf — P
9. J. Nocedal, brief CV (c. 2021; honours to Lagrange Prize 2021) — http://www.ece.northwestern.edu/~nocedal/Bio/bio-brief.pdf — P
10. J. Nocedal, NSF biosketch (c. 2011) — http://www.ece.northwestern.edu/~nocedal/CV/nsf-bio.pdf — P
11. J. Nocedal, homepage (index, research, publications, software, students, misc, book pages) — http://www.ece.northwestern.edu/~nocedal/ and http://users.iems.northwestern.edu/~nocedal/ — P
12. L-BFGS software page — http://users.iems.northwestern.edu/~nocedal/lbfgs.html — P
13. L-BFGS-B software page — http://users.iems.northwestern.edu/~nocedal/lbfgsb.html — P

**Speech, press and prizes**
14. J. Nocedal, Acceptance Speech, 2017 Von Neumann Theory Prize — http://www.ece.northwestern.edu/~nocedal/PDFfiles/VonNeumann_Speech.pdf (notes: `../sources/talks/2017-von-neumann-prize-acceptance-speech.md`) — P
15. A. Morris, "Nocedal Receives John von Neumann Theory Prize", McCormick News, 26 Oct 2017 — https://www.mccormick.northwestern.edu/news/articles/2017/10/nocedal-receives-john-von-neumann-theory-prize.html — S (contains a stated quote)
16. INFORMS, John von Neumann Theory Prize, past awardees — https://www.informs.org/Recognizing-Excellence/INFORMS-Prizes/John-von-Neumann-Theory-Prize — S
17. B. Sandalow, "Jorge Nocedal Selected for Lagrange Prize", McCormick News, 6 Apr 2021 — https://mccormick.northwestern.edu/news/articles/2021/04/jorge-nocedal-selected-for-lagrange-prize.html — S
18. Lehigh ISE, "Frank E. Curtis was co-awarded the 2021 Lagrange Prize in Continuous Optimization", 2021 — https://engineering.lehigh.edu/news/article/frank-e-curtis-was-co-awarded-2021-lagrange-prize-continuous-optimization — S
19. MOS Dantzig Prize 2012 page — http://www.mathopt.org/?nav=dantzig_2012 — **not read** (empty render)

**Papers read (author preprints or arXiv)**
20. J. Nocedal, "Theory of algorithms for unconstrained optimization", Acta Numerica 1 (1992) 199–242, doi:10.1017/S0962492900002270 (author PDF `PDFfiles/acta.pdf`, read in part) — P
21. D. C. Liu & J. Nocedal, "On the limited memory BFGS method for large scale optimization", Math. Program. 45 (1989) 503–528, doi:10.1007/BF01589116 (author PDF `PDFfiles/limited-memory.pdf`, read) — P
22. R. H. Byrd, P. Lu, J. Nocedal & C. Zhu, "A Limited Memory Algorithm for Bound Constrained Optimization", SISC 16 (1995), doi:10.1137/0916069 (tech. rep. NAM-08 rev. 1994, `PDFfiles/limited.pdf`, front matter read) — P
23. R. H. Byrd, M. E. Hribar & J. Nocedal, "An Interior Point Algorithm for Large-Scale Nonlinear Programming", SIOPT 9 (1999), doi:10.1137/S1052623497325107 (preprint 27 Jul 1997, `PDFfiles/nitro.pdf`, intro and final remarks read) — P
24. R. H. Byrd, J. Nocedal & R. A. Waltz, "Knitro: An Integrated Package for Nonlinear Optimization", Springer 2006, doi:10.1007/0-387-30065-1_4 (preprint 6 Jul 2005, `PDFfiles/integrated.pdf`, read in part) — P
25. G. Fasano, J. L. Morales & J. Nocedal, "On the geometry phase in model-based algorithms for derivative-free optimization", OMS 24 (2009), doi:10.1080/10556780802409296 (preprint rev. 12 Aug 2008, `PDFfiles/geometry.pdf`, abstract and final remarks read) — P
26. R. H. Byrd, M. Marazzi & J. Nocedal, "On the convergence of Newton iterations to non-stationary points", Math. Program. 99 (2004), doi:10.1007/S10107-003-0376-8 (preprint OTC 2001/01, `PDFfiles/failofconv.pdf`, abstract and intro read) — P
27. L. Bottou, F. E. Curtis & J. Nocedal, "Optimization Methods for Large-Scale Machine Learning", arXiv:1606.04838 v1 (2016) / SIAM Rev. 60 (2018), doi:10.1137/16M1080173 (read in part) — P
28. Bottou, Curtis & Nocedal, SIAM Review paper errata (30 Jun 2016) — http://www.ece.northwestern.edu/~nocedal/PDFfiles/opt_ml_errata.pdf — P
29. J. Nocedal, "Large Scale Unconstrained Optimization" (1996 preprint; in The State of the Art in Numerical Analysis, OUP 1997; CV item 61) — http://www.ece.northwestern.edu/~nocedal/PDFfiles/york.pdf (skimmed) — P

**Papers known from abstract or metadata only**
30. J. Nocedal, "Updating quasi-Newton matrices with limited storage", Math. Comp. 35 (1980) 773–782, doi:10.1090/S0025-5718-1980-0572855-7 (abstract via OpenAlex; body not read) — P
31. J. L. Morales & J. Nocedal, Remark on Algorithm 778, ACM TOMS 38 (2011), doi:10.1145/2049662.2049669 (abstract via OpenAlex) — P
32. R. H. Byrd, S. L. Hansen, J. Nocedal & Y. Singer, "A Stochastic Quasi-Newton Method for Large-Scale Optimization", arXiv:1401.7020 / SIOPT 26 (2016), doi:10.1137/140954362 (abstract) — P
33. N. S. Keskar et al., "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", arXiv:1609.04836 (ICLR 2017) (abstract) — P
34. R. Bollapragada et al., "A Progressive Batching L-BFGS Method for Machine Learning", arXiv:1802.05374 (ICML 2018) (abstract) — P
35. A. S. Berahas, R. H. Byrd & J. Nocedal, "Derivative-Free Optimization of Noisy Functions via Quasi-Newton Methods", arXiv:1803.10173 / SIOPT 29 (2019), doi:10.1137/18M1177718 (abstract) — P
36. H.-J. M. Shi, Y. Xie, R. Byrd & J. Nocedal, "A Noise-Tolerant Quasi-Newton Algorithm for Unconstrained Optimization", arXiv:2010.04352 / SIOPT 32 (2022), doi:10.1137/20M1373190 (abstract) — P
37. H.-J. M. Shi, M. Q. Xuan, F. Oztoprak & J. Nocedal, "On the Numerical Performance of Derivative-Free Optimization Methods Based on Finite-Difference Approximations", arXiv:2102.09762 / OMS 38 (2023), doi:10.1080/10556788.2022.2121832 (abstract) — P
38. Y. Lou, S. Sun & J. Nocedal, "Design Guidelines for Noise-Tolerant Optimization with Applications in Robust Design", arXiv:2401.15007 / SISC 47 (2025), doi:10.1137/24M1632279 (abstract) — P
39. M. Q. Xuan & J. Nocedal, "A Feasible Method for Constrained Derivative-Free Optimization", arXiv:2402.11920 / ORL 65 (2026), doi:10.1016/j.orl.2025.107398 (abstract) — P
40. S. Sun & J. Nocedal, "A Trust-Region Algorithm for Noisy Equality Constrained Optimization", arXiv:2411.02665 (abstract) — P
41. R. Bollapragada, R. Byrd & J. Nocedal, "Adaptive Sampling Strategies for Stochastic Optimization", arXiv:1710.11258 / SIOPT 28 (2018), doi:10.1137/17M1154679 (abstract) — P
42. R. Bollapragada, R. Byrd & J. Nocedal, "Exact and Inexact Subsampled Newton Methods for Optimization", arXiv:1609.08502 / IMA JNA 39 (2019), doi:10.1093/imanum/dry009 (abstract) — P
43. J. Nocedal, "An Iterative Approach for Solving the SCOPF Problem Applying LP, SOCP, and NLP Subproblems", DOE-Northwestern-1077, OSTI 2024, doi:10.2172/2404586 (OSTI record) — P
44. Remaining DOIs in §2.1, §2.3 and §4: verified by Crossref (titles, venues, volumes, pages, authors) or DBLP; not read — P (metadata)

**Third-party documentation and critique**
45. SciPy documentation, `scipy.optimize.fmin_l_bfgs_b` (v1.18.0), Notes — https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin_l_bfgs_b.html — S
46. L. Dinh, R. Pascanu, S. Bengio & Y. Bengio, "Sharp Minima Can Generalize For Deep Nets", arXiv:1703.04933 (2017) (abstract) — S (peer critique)
47. OpenAlex work record for doi:10.59782/aai.v1i2.296 (suspected misattribution; §4.6) — S

**Talk and interview transcripts** (saved in this run by research agent 02; caption-derived, not human-checked)
48. "Subject to" (YouTube channel), long-form interview with Jorge Nocedal, uploaded 2026-03-18, 1:48:30 — https://www.youtube.com/watch?v=CfR-llfmb6E; transcript `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt` (ASR; read 0:37–1:48 and intro) — P (stated; interviewer's framing is secondary)
49. J. Nocedal, "Zero-order and Dynamic Sampling Methods for Nonlinear Optimization", Simons Institute, 2017 (uploaded 2017-10-03) — https://www.youtube.com/watch?v=OfVZ9gArXiY; transcript `../sources/talks/2017_simons-zero-order-dynamic-sampling_OfVZ9gArXiY.txt` (uploader subtitles; keyword-searched) — P
50. J. Nocedal, UCLA CS201 seminar on DFO of noisy functions, 2021-04-08 — https://www.youtube.com/watch?v=4a12aV77CAI; transcript `../sources/talks/2021-04-08_ucla-cs201-seminar_4a12aV77CAI.txt` (ASR; keyword-searched) — P
51. J. Nocedal, "How is it Possible to Train Deep Neural Networks?", NITMB Seminar, recorded 2024-10-25 — https://www.youtube.com/watch?v=XrX7MEMbdYw; transcript `../sources/talks/2024-10-25_nitmb-seminar-train-dnns_XrX7MEMbdYw.txt` (ASR; keyword-searched) — P

**Searches**
52. WebSearch 1: "Lagrange Prize in Continuous Optimization 2021 Bottou Curtis Nocedal …" (returned sources 17, 18) — S
53. WebSearch 2: "Jorge Nocedal interview origin limited memory BFGS 1980 Courant how the idea came" (no interview found) — S

**Scratch materials** (not committed): `/tmp/nonlinear-team-scratch/base-skills/jorge-nocedal/`, holding `dblp.json`, the extracted CV, bio and preprint texts, and arXiv HTML.
