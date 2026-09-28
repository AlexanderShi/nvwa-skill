# 06 · Research trajectory: timeline, lineage, turns and the last 12 months (Nicholas I. M. Gould)

- **Researcher**: Nicholas Ian Mark Gould (Nick Gould), born 1957. STFC Senior Fellow, Computational Mathematics, Rutherford Appleton Laboratory (RAL), half time since 2017. Visiting Professor at Oxford and Edinburgh. Living.
- **Dimension**: research agent 06 of 06, research trajectory (nuwa research-craft Phase 1; framework §一 layer 2 "problem choice: why now, when to quit" and §二 agent 6).
- **Research date**: 2026-09-28.
- **Sources consulted**: 34 (T01–T34 under Sources). 30 were read in whole or in the parts cited. 4 were blocked, abstract or metadata only, or returned nothing, and each is marked. 19 are primary: his homepage, CV, Oxford profile, eight of his own texts (abstract only for one), one announcement, and six git repositories and release pages read as a record of practice. WebSearch calls used: **2 of 2**.
- **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` hold only `.gitkeep`, so there was **no user-supplied material**. `private/` was not opened. No transcript was saved to `sources/talks/`, because I found no new talk. The one interview I used (Toint's 2026 podcast) was already saved, as an ASR transcript, in the Toint member folder by another agent.
- **Method**: I rebuilt the timeline from his own CV and homepage [T01][T02]. I dated every turn from the publication record: DBLP via SPARQL [T07], with every DOI below resolved through Crossref in this run [T11], plus arXiv [T08][T09] and Optimization Online [T10]. For the years after 2018 I used the git histories of the four repositories he maintains [T13][T15]–[T18], because since 2020 his output shows up more in code than in papers. Notes 01–04 of this workflow were read for cross-checking. Where I rely on a fact they found, I re-fetched it here (CV, homepage, SIAG/OPT 2003, GALAHAD 2003, JOSS 2023, ARC I, TREK).

**Tags.** [stated] = Gould's own words, alone or with co-authors. [practice] = what the record shows he did (papers, dates, commits, CV entries). [observed] = what someone else said. [inferred] = my reading, with no source saying it. Each item is also marked **primary** (Gould's own text or record) or **secondary** (someone else's account, or a bibliographic database). Page numbers are journal pages unless marked "PDF p.".

---

## 0. Read this first: the shape of the trajectory

1. **One institution, one partner, one theme across 45 years.** He has been in the same numerical-analysis group since 1985 (Harwell, which moved to RAL in 1990). Philippe Toint has been his co-author since 1988 (the first CGT papers, checked in Crossref), with the last joint preprint in 2021 (arXiv 2111.14098). DBLP holds 54 Gould–Toint records, 1991–2020. The theme that never leaves is the linear algebra of the optimization **subproblem**: QP, KKT/saddle-point systems, the trust-region subproblem. It runs from the 1984 Stanford QP paper to the 2025 TREK/NREK paper [practice, primary + DBLP].
2. **The turns are in the globalization and analysis layer, not in the subproblem layer.** He moved from augmented Lagrangian (1988–1997) to SQP (1997–2003), then to barrier/interior point (2003), trust funnel (2007), regularization and complexity (2007–2021), and SQP again (2008–2015). Meanwhile the subproblem work continued without a break [practice].
3. **What triggers a turn** (evidence in §3): other people's benchmarks (1997–2003); a theory result by others plus a new colleague (Nesterov–Polyak 2006 plus Cartis joining RAL in 2006); a grant plus a postdoc (SQP with Robinson, 2008; materials preconditioning, 2013–16; least squares, 2015–20); a new colleague with a linear-algebra tool (Al Daas and extended Krylov, 2025); and the size of the user base (C/Python/Julia interfaces, 2022–23).
4. **How he leaves a topic**: he rarely announces it. He closes a line with a consolidating book (*Trust-Region Methods* 2000; *Evaluation Complexity* 2022) or with a software package. When the reason for leaving is a failure, he says it in print (LANCELOT B and SQP, 2003) [practice + stated].
5. **Since about 2020 the trajectory is mostly software.** No refereed article is dated 2021 or 2022 on his CV. There are no arXiv or Optimization Online postings between December 2021 and November 2025. His GALAHAD commits went from 30 in 2020 to 238–242 a year in 2022–2024 [practice, primary]. The newest research items (TREK/NREK, least squares over simplices) came out as **paper and package together, or as a package only**.
6. **He never entered stochastic or machine-learning optimization, and said why**: his course book leaves out "the current obsession with stochastic gradient methods" (§3, T8) [stated, primary].
7. **The last 12 months (to 2026-09-28)**: one arXiv paper, one STFC application report, two GALAHAD releases with new packages, a CUTEst release with a new solver interface (Uno), and a re-licensing and move of the SIF test-problem collection. His most recent commit is dated 2026-09-27 (§6) [practice, primary].

---

## 1. Dated timeline

| Year | Event | Kind | Evidence | Tag |
|---|---|---|---|---|
| 1957 | Born 25 April, Woking, England | personal | CV p.1 [T02] | practice, primary |
| 1976 | 8 months as Assistant Scientific Officer, Division of Numerical Analysis and Computing, NPL, before university. Co-author of NPL algorithms-library reports with P. E. Gill, W. Murray and S. M. Picken (1977) | position / first software | homepage [T01]; CV pp.2, 20 [T02] | practice, primary |
| 1976–79 | Oxford (Corpus Christi), exhibitioner then scholar; B.A. first class 1979 | education | CV p.1 [T02] | practice, primary |
| 1979–82 | D.Phil. Oxford 1982, "Numerical methods for linear and quadratic programming". Advisor Walter Murray (MGP). SERC grant 1979–82 | education | CV p.1 [T02]; MGP 89384 [T04] | practice, primary + secondary |
| 1981–82 | Visiting scholar, Stanford Operations Research. SOL reports 82-9 and 82-10 with Gill, Murray, Saunders and M. H. Wright → "A weighted gram-schmidt method for convex quadratic programming", *Math. Program.* 30 (1984), 10.1007/BF02591884. Also a USGS earthquake-epicentre report with Murray (1981) | position / first papers | CV pp.2, 20 [T02]; Crossref [T11] | practice, primary |
| 1982–85 | Assistant Professor, Combinatorics & Optimization, Waterloo. Solo CORR reports on generalized steepest edge for LP (83-2, 84-1) and QP stability (83-11). First paper with A. R. Conn: "On the Location of Directions of Infinite Descent for Nonlinear Programming Algorithms", *SINUM* 21 (1984), 10.1137/0721072. NSERC grant 1983–85 | position / new partner | CV pp.2, 20 [T02]; Crossref [T11] | practice, primary |
| 1985–90 | Harwell Laboratory, Numerical Analysis Group (SSO, then PSO 1989). Mostly solo papers: QP existence and uniqueness, *Math. Program.* (1985), 10.1007/BF01585660; "On Growth in Gaussian Elimination with Complete Pivoting", *SIMAX* 12 (published 1991), 10.1137/0612025; LP crash procedures with J. K. Reid, *Math. Program.* (1989), 10.1007/BF01589115. HSL packages | position / linear-algebra culture | CV p.1 [T02]; Crossref [T11] | practice, primary |
| 1986 | Leslie Fox Prize in numerical analysis (September). A secondary list names J. W. Demmel and N. I. M. Gould as the 1986 first prizes. Prize paper: **not found** | prize | CV p.2 [T02]; Wikipedia list [T29] | practice primary; observed secondary |
| 1988 | First Conn–Gould–Toint (CGT) papers: bound-constrained trust region, *SINUM* 25 (1988), 10.1137/0725029, and the testing paper, *Math. Comp.* 50 (1988), 10.1090/S0025-5718-1988-0929544-3. **Correction** in 1989, 10.1137/0726044 | new line: trust region | Crossref [T11] | practice, primary |
| 1989–91 | Proposals for a standard input format for test problems (Waterloo CSS-89-61, 1989; Namur 91/8, 1991); CGT-edited *Math. Program. B* issues on large-scale optimization (1989, 1990) | infrastructure | CV pp.4, 19 [T02] | practice, primary |
| 1990 | "I moved with the Group to the Central Computing Department (as it was then) at RAL in 1990 and have been there almost ever since." NATO travel grant 1990–95 (the CGT trio) | move (institutional) | homepage [T01]; CV p.3 [T02] | stated + practice, primary |
| 1991–92 | Augmented Lagrangian theory, *SINUM* 28 (1991), 10.1137/0728030; SR1 convergence, *Math. Program.* (1991), 10.1007/BF01594934; **LANCELOT** book and code (Springer 1992), 10.1007/978-3-662-12211-2 | software line 1 | Crossref [T11] | practice, primary |
| 1993 | Sabbatical at CERFACS, Toulouse (Parallel Algorithms Team). CERFACS reports with Arioli, Chan, Duff and Reid, and with Conn, Sartenaer and Toint. It led to element-by-element preconditioners with Daydé and L'Excellent, *SISC* 18 (1997), 10.1137/S1064827594274796. He was external PhD advisor to L'Excellent (1993) and Décamps (1996) | sabbatical → linear-algebra branch | homepage [T01]; CV pp.2, 19, 25 [T02]; Crossref [T11] | practice, primary |
| 1994 | Beale–Orchard-Hays Prize (August), shared in the CGT trio | prize | CV p.2 [T02]; homepage [T01] | practice, primary |
| 1995 | CUTE, *ACM TOMS* 21 (1995), 10.1145/200979.201043. Work starts on the Fortran 90 LANCELOT B | infrastructure | Crossref [T11]; GALAHAD 2003 p.354 [T20] | practice + stated, primary |
| 1997 | LANCELOT B prototype working. First interior-point theory: Lagrangian barrier, *Math. Comp.* (1997), 10.1090/S0025-5718-97-00777-1 | turn begins | [T20] p.354; Crossref [T11] | stated + practice, primary |
| 1997–2002 | Other groups' benchmarks show LANCELOT A "often, but far from always" outperformed. LANCELOT B is shelved and the team turns to SQP, building the QP layer first | **turn 1** (§3) | [T20] p.354 | stated, primary |
| 1998– | Visiting Professor, Edinburgh | position | CV p.2 [T02] | practice, primary |
| 1999–2000 | GLTR, *SIOPT* 9 (1999), 10.1137/S1052623497322735; KKT constraint preconditioning with Keller (student) and Wathen, *SIMAX* 21 (2000), 10.1137/S0895479899351805; *Trust-Region Methods* (SIAM 2000), 10.1137/1.9780898719857 | subproblem layer; consolidating book | Crossref [T11] | practice, primary |
| 1999 | Promoted to Band 2 (Individual Merit) fellow | position | CV p.1 [T02] | practice, primary |
| 2001–02 | Superlinear primal–dual IPM, *SIOPT* (2001), 10.1137/S1052623400370515; filter-SQP convergence with Fletcher, Leyffer, Toint and Wächter, *SIOPT* 13 (2002), 10.1137/S1052623499357258 | IPM and filter theory | Crossref [T11] | practice, primary |
| 2003 | GALAHAD 1.0 and CUTEr, *ACM TOMS* 29(4), 10.1145/962437.962438 and 10.1145/962437.962439. **April 2003: the large-scale SQP is suspended** and the team turns to "sequential barrier-function minimization" | **turn 2** (§3) | [T19] p.4; [T20] | stated, primary |
| 2003–04 | SLP-EQP with Byrd, Nocedal and Waltz, *Math. Program.* 100 (2004; online 2003), 10.1007/s10107-003-0485-4. Senior Visiting Scientist, Argonne (2004) | alternative bet | Crossref [T11]; CV p.2 [T02] | practice, primary |
| 2004–10 | Editor-in-Chief, *SIAM J. Optim.* (the CV says 2004–2010, the homepage 2005–2010; see Contradictions) | service peak | CV p.26 [T02]; homepage [T01] | practice, primary |
| 2005 | Acta Numerica survey with Orban and Toint, 10.1017/S0962492904000248 | consolidation | Crossref [T11] | practice, primary |
| 2006–08 | Professor of Numerical Optimisation and Tutorial Fellow of Exeter College, Oxford. "I returned full-time to RAL in 2008." Reason for leaving the chair: **not stated** | move and return | homepage [T01]; CV p.1 [T02] | stated, primary |
| 2006–07 | Coralia Cartis is a Research Scientist in the RAL Numerical Analysis Group (2006–07), then a visiting RAL scientist (2007–12). ARC preprint RAL-TR-2007-007, received by *Math. Program.* 1 Oct 2007; trust funnel (RAL-TR-2007-016) | **turn 3** (§3) | Cartis CV p.1 [T26]; ARC I p.245 [T23] | practice, primary + secondary |
| 2008 | Only formal D.Phil student, Jaroslav Fowkes (the CV lists "D.Phil advisor" under 2008; the MGP dates the degree 2012). SQP comes back with Daniel Robinson (Oxford postdoc) under EPSRC EP/F005369/1 (PI, 2007–10) | **turn 4** (§3) | CV pp.3, 24 [T02]; MGP [T06]; SQP II p.2049 [T24] | practice, primary |
| 2008 | Solo negative evaluation that closes a topic: "How good are projection methods for convex feasibility problems?", *COAP* 40 (2008), 10.1007/s10589-007-9073-5 | exit by evaluation | Crossref [T11] | practice, primary |
| 2009 | Inaugural SIAM Fellow (May) | honour | CV p.2 [T02]; homepage [T01] | practice, primary |
| 2010–14 | The densest refereed period: the complexity program with Cartis and Toint; saddle-point spectra with Simoncini (*SIMAX* 2010, 10.1137/080733413) and projected Krylov with Orban and Rees (*SIMAX* 2014, 10.1137/130916394); CUTEst (*COAP* 2015, online 2014, 10.1007/s10589-014-9687-3) | peak | DBLP [T07]; Crossref [T11] | practice, primary |
| 2011 | STFC Senior Fellow (Band H, Individual Merit) | position | CV p.1 [T02]; homepage [T01] | practice, primary |
| 2013–16 | EPSRC "Preconditioners for Large-Scale Atomistic Simulations" (PI, 2013–15) → dimer saddle search, *Math. Comp.* (2016), 10.1090/mcom/3096; universal preconditioner, *J. Chem. Phys.* 144 (2016), 10.1063/1.4947024. No materials-science paper after 2016 in DBLP or the CV | application excursion, then exit | CV pp.2, 5–6 [T02]; Crossref [T11] | practice, primary |
| 2015–20 | EPSRC "Least Squares: Fit for the Future" (CoI) → least-squares preconditioners (*ACM TOMS* 2017, 10.1145/3014057), tensor-Newton least squares (*COAP* 2019, 10.1007/s10589-019-00064-2); critique of performance profiles (*ACM TOMS* 2017, 10.1145/2950048) | grant-driven line | CV p.2 [T02]; Crossref [T11] | practice, primary |
| 2016 | All associate-editor roles end (SIOPT, *Math. Program.*, TOMS, IMA JNA, Math. Comp., MPC area editor) | service exit | CV p.26 [T02] | practice, primary |
| 2017 | "have worked half time since the summer of 2017" | resource change | homepage [T01] | stated, primary |
| 2018 | GALAHAD moves to GitHub: first commits 3–4 Feb 2018, "Transfer of CCPForge svn revision 706". ICM 2018 proceedings with Cartis and Toint, 10.1142/9789813272880_0198 | tooling change; recognition | GALAHAD git [T13]; Crossref [T11] | practice, primary |
| 2020–21 | Last complexity preprints: arXiv 2001.10802, 2011.00854, 2111.14098. No journal versions found (Crossref queries); the 2022 book has a chapter "Inexact Function Values and Derivatives" (10.1137/1.9781611976991.ch13) | exit from complexity (§3 turn 6) | arXiv [T08]; Optimization Online [T10]; Crossref [T11] | practice, primary + secondary |
| 2022 | Book *Evaluation Complexity of Algorithms for Nonconvex Optimization* (SIAM), 10.1137/1.9781611976991. GALAHAD 4.0, announced 4 May 2022: "A defining feature of this new release are native interfaces to C and Matlab." ICM 2022 proceedings, 10.4171/icm2022/95. STFC course on continuous optimization for scientists | consolidating book; software turn | Crossref [T11]; NA Digest [T22]; CV p.24 [T02] | practice + stated, primary |
| 2022–24 | Alexis Montoison's first GALAHAD commit (2022-11-20); by 2023 he is the top committer. Python/Julia interfaces (4.2, 2023); GALAHAD 5.0.0 (tag 2024-07-05); Meson build; precompiled binaries | team change | GALAHAD git and tags [T13] | practice, primary |
| 2023 | JOSS paper (with Fowkes), 10.21105/joss.04882: "the principal motivation for the new release is to raise the profile of the library by increasing its potential userbase" (p.2) | **turn 7** (§3) | [T21] | stated, primary |
| 2024–25 | Hessian approximation with Fowkes and Scott, *Numer. Algorithms* (2024), 10.1007/s11075-023-01681-z, and *ACM TOMS* (2025), 10.1145/3728460. EPF exponential-penalty prototype (header: May 2024), renamed EXPO 15 June 2025, still in `src/forthcoming` | new lines | Crossref [T11]; GALAHAD git [T13] | practice, primary |
| 2025 | Royal Society memoir of Roger Fletcher with J. A. J. Hall, *Biogr. Mems Fell. R. Soc.* 78 (2025) 127–146, published 14 May 2025, 10.1098/rsbm.2024.0037 (abstract read). GALAHAD 5.3.0 (2025-09-03) absorbs SPRAL's SSIDS | memorial writing; infrastructure | Crossref [T33]; release notes [T14] | practice, primary |
| 2025-11 → 2026-09 | Last 12 months: see §6 | — | — | — |

---

## 2. Lineage

### 2.1 Upward and sideways (who trained him, who trained beside him)

- **Advisor**: Walter Murray (D.Phil. University of London 1970, "Constrained Optimization"; the MGP lists his own advisor as "Unknown") [T05, secondary]. Gould's D.Phil. is Oxford 1982 under Murray [T04, secondary; thesis title confirmed by CV p.1, T02 primary].
- **Academic siblings** (other Murray students in the MGP) include **Philip E. Gill** (Imperial College London 1974), who is a member of this team, and also Anders Forsgren (KTH 1990), Michael Overton, Stephen Nash (Stanford 1982) and Samuel Eldersveld (Stanford 1991) [T05, secondary]. **Gould and Gill are academic brothers.** In DBLP, Gould shares exactly two records with Gill: the 1984 Gill–Gould–Murray–Saunders–Wright QP paper (10.1007/BF02591884), and a 2015 note with Bienstock and Gill, "A note on 'On fast trust region methods for quadratic models with linear constraints'…", *Math. Program. Comput.* (2015), 10.1007/s12532-015-0085-3. He has no record with Murray, Saunders or M. H. Wright after 1984 [T07][T11, practice].
- **Before the D.Phil.**: the 1976 NPL placement and the 1977 NPL library reports with Gill and Murray [T02 pp.2, 20]. [inferred] The NPL placement is where the link to Murray and Gill started, which would explain the choice of advisor and the 1981–82 Stanford year. No source says this.

### 2.2 Downward (students)

- **Formal D.Phil. student**: one, Jaroslav M. Fowkes (Oxford 2012 in MGP; "Bayesian Numerical Analysis: Global Optimization and Other Applications"). Fowkes has one student of his own (Lingyi Yang, Oxford 2022), so the MGP counts **1 student and 2 descendants** for Gould [T04][T06, secondary]. Fowkes later became Gould's RAL colleague and GALAHAD co-maintainer (GALAHAD 4.0 announcement, JOSS paper, 29 + 16 commits under "Jari" and "Jaroslav Fowkes") [T13][T21][T22, primary].
- **External PhD advisor** (CV p.25): Hernandez and Schuler (1991), L'Excellent (1993), Décamps (1996), Keller (1997), Gate (2000), Browne (2009). **External examiner** for, among others, Cartis (Cambridge 2005), Stoll (2009), Rees (2010), Pestana (2011), Turner (2014) and Schork (2018) [T02, primary]. Examinees who became co-authors: Cartis, Rees, Stoll [practice].
- [inferred] His "school" passes on through **software and test problems, not through students**. Note 04 covers this dimension.

### 2.3 Collaboration eras (DBLP pid 55/5344, 98 records; top co-authors per period) [T07, secondary bibliographic, computed here]

| Period | Records | Solo | Top co-authors | Reading [inferred] |
|---|---|---|---|---|
| 1984–89 | 4 | 1 | Gill, Murray, Saunders, M. H. Wright, Conn, Reid (1 each) | apprenticeship network (Stanford SOL), then Harwell |
| 1990–94 | 4 | 0 | Conn 3, Toint 3 | CGT trio forms |
| 1995–99 | 13 | 1 | Toint 8, Conn 6, Daydé 3 | trio at its peak; the CERFACS sabbatical branch |
| 2000–04 | 16 | 0 | Toint 12, Orban 5, Leyffer 3 | GOT (Gould–Orban–Toint) replaces CGT for software |
| 2005–09 | 10 | 1 | Toint 3, Scott 2, Hu 2, Dollar 2, Schilders 2 | a thin period (Oxford chair, SIOPT editorship); linear-algebra benchmarking |
| 2010–14 | 23 | 1 | Toint 14, Cartis 11, Robinson 5 | CGT again, now Cartis–Gould–Toint |
| 2015–19 | 21 | 0 | Toint 12, Cartis 11, Robinson 4, Scott 3, Curtis 2 | complexity program at full length |
| 2020–26 | 7 | 0 | Fowkes 3, Cartis 2, Toint 2, Scott 2, Simoncini 1, Al Daas 1 | RAL colleagues and software |

DBLP's pid 55/5344 has only one book record (*Trust Region Methods*, 2000), no Acta Numerica survey and no QPLIB (checked in this run), and no records for 2021–2022.

---

## 3. The turns: what changed, what triggered it, and when relative to the field

Each turn gives the trigger, his stated reason (when there is one), the timing, and the resources of the moment.

### Turn 0 (1985): from university LP/QP to the Harwell sparse-linear-algebra culture

- **What changed**: after Waterloo he joined the Harwell Numerical Analysis Group. His next five years are mostly solo papers on the linear algebra underneath optimization (QP existence and uniqueness 1985, penalty-function linear algebra, LP crash with Reid 1989, growth in Gaussian elimination 1991) [practice, primary; T02, T11].
- **Trigger**: a move. Why he left Waterloo after three years: **not found** [gap].
- **Resources**: a national-lab group with its own library (HSL). He wrote HSL packages (FD05 … VF05, CV p.21) [practice, primary].

### Turn 1 (1997–2002): leaving augmented Lagrangian for SQP, by way of the QP layer

- **Trigger (stated, external benchmarks)**: "a number of our colleagues had started to release the results of comparative tests of their new codes—for instance SNOPT …, LOQO …, KNITRO …, and FilterSQP …—against LANCELOT A, and the results made frankly rather depressing reading for us … LANCELOT often, but far from always, being significantly outperformed." They concluded that "the limit of what might be achieved by augmented Lagrangian methods such as LANCELOT A had probably been reached." Then: "Reluctantly, we abandoned any plans to release LANCELOT B at that time, and turned our attention instead to SQP methods." (GALAHAD 2003, p.354 [T20]) [stated, primary]
- **Belief carried over**: "To our minds, there had never really been much doubt that SQP methods would be more successful in the long term, but there had been general concerns over how to solve (approximately) their all-important (large-scale) quadratic programming (QP) subproblems." (p.354) [stated, primary]
- **Timing vs the field**: he entered augmented Lagrangian for large scale early (theory 1988–91, a released code in 1992). He left it **after** SNOPT, LOQO, KNITRO and filterSQP had been benchmarked against LANCELOT, and the exit was triggered from outside [practice + stated].
- **Resources**: Fortran 90 compilers. They stayed with Fortran because the HSL components were Fortran and "we believed (and still believe) Fortran 90 capable of providing all of the facilities we needed." (p.354) [stated, primary]

### Turn 2 (April 2003): suspending SQP, turning to interior point / barrier

- **Trigger (stated, own experience against rivals)**: "We have currently suspended development of the large-scale SQP method that we had intended including in GALAHAD … despite having produced both effective active-set and interior-point QP solvers. Our experience has been that without QP truncation, the cost of the QP solution so dominates that other non-SQP approaches (such as IPOPT …, KNITRO … and LOQO …), in which truncation is possible, have made significant progress even before our QP code had solved its first subproblem!" (SIAG/OPT Views-and-News 14(1), 2003, p.4 [T19]) [stated, primary]
- **New direction**: "Since we have now all but given up our SQP developments, we have now turned to what we consider to be the other possibility, namely to solve general constrained optimization problems by sequential barrier-function minimization, using the lessons learned when designing and evaluating QPB." (p.4) [stated, primary]
- **The principle behind it**: "if there is one lesson we should have learned from large-scale unconstrained minimization, it is to aim to solve the subproblem as inaccurately as possible consistent with overall convergence" (p.4) [stated, primary]
- **Timing**: the essay opens with the view of someone who arrives after a revolution: the stimulus was "without doubt in part what has been called the “interior-point” revolution. But also the fight-back from the traditionalists" (p.2) [stated, primary]. [inferred] He moved to interior point after IPOPT, KNITRO and LOQO had shown its scaling. His IPM theory (1997, 2001) came earlier than that.
- **What happened next** [practice, primary, T13]: no general-NLP barrier solver appears among GALAHAD's released packages as of HEAD 2026-09-26 (note 03 traces each attempt). The interior-point line lived on in QP (QPB/CQP; "Trajectory-following methods for large-scale degenerate convex quadratic programming", *Math. Program. Comput.* 5 (2013), 10.1007/s12532-012-0050-3) and in the interior-point trust funnel with Curtis, Robinson and Toint (*Math. Program.* 2017, 10.1007/s10107-016-1003-9).

### Turn 3 (2006–2007): globalization by regularization, and worst-case complexity

- **Trigger (stated in the paper: a new result by others that had no numbers)**: ARC I synthesizes Griewank 1981, Nesterov–Polyak 2006 and Weiser et al. 2007. Of Nesterov–Polyak it says that global convergence and rates were proved "but no numerical results were provided" (p.247). The aim: "to unify and extend these contributions into a coherent and numerically efficient algorithmic framework, for which global and asymptotic convergence results can be proved under weaker assumptions and with simpler proofs, while preserving the good complexity bound shown by Nesterov and Polyak" (p.247) [T23, stated, primary].
- **Trigger (practice: a new colleague)**: Cartis joined the RAL Numerical Analysis Group as a permanent Research Scientist in 2006–07, after an Oxford postdoc 2004–06 [T26, secondary]. The ARC paper lists Cartis and Gould at RAL, and Gould also at the Oxford Computing Laboratory; it was received 1 Oct 2007 and funded by EPSRC GR/S42170 [T23 p.245, primary].
- **Trigger (observed, collaborator's account)**: Toint, in a 2026 podcast, says "it was a time where complexity began to be a major buzzword in optimization. And a lot of the theory was and still is for the convex case. We thought that doing theory for the non-convex case was important and useful." (ASR transcript [1:02:05]–[1:02:22], T28; automatic transcript, not checked against the audio) [observed, secondary].
- **Timing**: early. The first RAL report came about a year after Nesterov–Polyak 2006, and this became the densest research line of his career (2010–2020).
- **Tension recorded at the start**: the paper's own numerics favoured the variant "less concerned with provably superior worst-case complexity" (p.289) [stated, primary].
- **Parallel idea from the same months**: the trust funnel, "Nonlinear programming without a penalty function or a filter" (RAL-TR-2007-016 → *Math. Program.* 2010, 10.1007/s10107-008-0244-7), with an erratum in 2012 (10.1007/s10107-011-0491-x) [practice, primary].

### Turn 4 (2008): SQP comes back, with a postdoc and a grant

- **Trigger (practice)**: Daniel P. Robinson, then at the Oxford Mathematical Institute (affiliation on the 2010 paper), and EPSRC grants EP/E053351/1 and EP/F005369/1, the second with Gould as PI, "Algorithms for Large-Scale Nonlinearly Constrained Optimization", 2007–10 (CV p.3) [T24 p.2049 footnotes; T02, primary].
- **How the 2003 obstacle was handled (stated)**: "One novel difference, however, is that we never require the global minimizer of a general indefinite quadratic program (QP). This is accomplished by computing trial steps as the sum of two well-defined steps." The predictor step "is the unique solution to a strictly convex QP" (SQP Part II, p.2049 [T24]) [stated, primary]. [inferred] This answers the 2003 complaint that the nonconvex QP cost dominates SQP.
- **Outcome**: papers in 2010–2015, first with Robinson, then with Loh and Robinson: "A Filter Method with Unified Step Computation for Nonlinear Optimization", *SIOPT* 24 (2014), 10.1137/130920599, and "A Nonmonotone Filter SQP Method: Local Convergence and Numerical Results", *SIOPT* 25 (2015), 10.1137/140996677. The Fortran filter-SQP (FiSQP, translated 2014) is still in `src/forthcoming` in 2026 [T13, practice]. So SQP returned **as papers but not as a released solver**.

### Turn 5 (2013–2020): grant-led excursions (materials, least squares, applications)

- **Materials simulation** (EPSRC EP/J021377/1, PI, 2013–15, CV p.2): dimer saddle search (10.1090/mcom/3096) and universal preconditioner (10.1063/1.4947024, eight authors including Ortner and Csányi). No follow-up after 2016 [practice, primary]. [inferred] He entered with the grant and left when it ended.
- **Least squares** (EPSRC EP/M025179/1, 2015–20): the least-squares preconditioner survey (10.1145/3014057), tensor-Newton (10.1007/s10589-019-00064-2), then Hessian approximation by least squares (2024–25) and GALAHAD least-squares packages (BLLS 2020, SLLS 2022, CLLS 2022, BLLSB 2023, BNLS 2024; SNLS/SLLSB 2026, from the dates each `src/` directory first appears [T13]). **This is the one grant-led line that did not end with its grant.** [practice, primary]
- **Earlier applications** from supervision links: "Optimal Well Placement" (Farmer, Fowkes and Gould, ECMOR XII, 2010, 10.3997/2214-4609.20144994) and binary programming for topology optimization (Browne, Budd, Gould, Kim and Scott, *IJNME* 2012, 10.1002/nme.4367) [T02][T11].

### Turn 6 (2020–2022): closing the complexity program

- **Evidence of exit [practice]**: the last complexity preprints are arXiv 2001.10802 (Jan 2020), 2011.00854 (Nov 2020, v2 Oct 2021) and 2111.14098 (Nov 2021). Optimization Online shows nothing from him between Dec 2021 and Nov 2025 [T10]. Crossref queries found no journal versions of the three preprints. The book (2022) has a chapter titled "Inexact Function Values and Derivatives" (10.1137/1.9781611976991.ch13) [T11]. [inferred] The preprints were folded into the book, which closed the line. This is his usual exit: a consolidating monograph, as with the trust-region work in 2000.
- **Stated reason for stopping**: **not found**. Toint says the book "is too weak for my taste" (ASR, "weak" probably a mishearing), and calls it "another long project" [T28, observed, secondary].
- **Timing vs the field** [inferred]: he left while nonconvex complexity was still an active research area, and moved his effort into code.

### Turn 7 (2018–2024): from a research code to a multi-language library with a team

- **Stated trigger (user base, rivals' languages)**: "Although GALAHAD 4.0 contains an increased variety of new solvers, the principal motivation for the new release is to raise the profile of the library by increasing its potential userbase. While modern Fortran is an extremely flexible programming language, it is perceived as old fashioned in many circles. Rival open-source solvers such as IPOPT … and commercial ones such as KNITRO … are written predominantly in C/C++" (JOSS 2023, p.2 [T21]) [stated, primary].
- **Contrast with 2003**: then, "we believed (and still believe) Fortran 90 capable of providing all of the facilities we needed" ([T20] p.354). The code language did not change. What changed was the strategy: bridge to users instead of waiting for them [stated + practice].
- **Practice** [T13]: SVN on CCPForge → GitHub (Feb 2018); Gould+`nimgould` commits per year: 38 (2018), 6 (2019), 30 (2020), 131 (2021), 238 (2022), 242 (2023), 239 (2024), 205 (2025), 7 (2026 to date). A second maintainer, Montoison, joined in 2022, and all authors together committed 528 times in 2023. From 2022-03-07 onward his own 2010–15 global-optimization work with Fowkes returns as packages (BGO, DGO, UGO) [practice, primary].
- **Resources**: half time from 2017 [T01]; talks limited, in the CV's words "for health reasons" (CV p.21 [T02]). [inferred] Code, which travels without its author, may have become the main output channel for someone who turned down most invitations. The CV wording is the only evidence.

### Turn 8 (non-entry): stochastic and machine-learning optimization

- **Stated**: "We have chosen not to delve into the extensive but specialised worlds of linear and convex optimization (specifically linear programming, and the current obsession with stochastic gradient methods) except in passing. Many of the methods we mention will work for such problems, but they are unlikely to be anything close to competitive with the best for these classes." (course booklet *An introduction to algorithms for continuous optimization*, © 2000, 2021, preface p.v [T25]) [stated, primary]
- **Practice**: no stochastic or ML paper in DBLP or the CV [T02][T07]. The one data-analysis item is the 2026 STFC report on muon-decay event detection (§6), which is signal processing for a facility rather than ML optimization [practice].
- **Why it matters for the skill** [inferred]: a skill built from him should **not** be used to generate ML-training advice. He has a stated reason for staying out.

### Turn 9 (2025–2026): the subproblem again, with a new colleague's tool

- **Practice**: Hussam Al Daas (RAL since August 2020; background in Krylov methods, domain decomposition and HPC [T27]) and Gould: arXiv 2511.11135, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems" (v1 14 Nov 2025, v2 21 Jan 2026, v3 2 Mar 2026) [T09]. The packages `trek` (first commit 2025-11-17) and `nrek` (2025-11-23) were committed three and nine days after v1, and shipped in GALAHAD 5.4.0 (2025-11-27) [T13][T14].
- **Stated framing of the result**: "We did not expect any of the methods tested to be an overall winner, and indeed this is the case." (arXiv 2511.11135v3, PDF p.15 [T09]) [stated, primary]. The comparison is against his own older solvers TRS and GLTR, on four cores of an Intel i9 PC with HSL MA57 (PDF p.14) [practice].
- [inferred] The same pattern as 2000 (Keller–Wathen) and 2014 (Orban–Rees): a numerical-linear-algebra colleague brings a tool, and Gould aims it at the optimization subproblem.

---

## 4. Entering and leaving topics, relative to the consensus

All rows are [inferred] from the dates in §1 and §3. The dates themselves are [practice, primary].

| Topic | Entered | Relative to the field | Left | How he left |
|---|---|---|---|---|
| Numerical QP/LP linear algebra | 1977–82 (NPL, Stanford) | inside the founding group (Gill–Murray–Saunders–Wright) | never | — |
| Trust regions for constrained problems | 1988 (CGT) | early | never (book 2000, TREK 2025) | — |
| Augmented Lagrangian, large scale | 1988–92 | early, among the first released large-scale NLP codes | 1997–2003 | benchmarks by others; stated in print; the code still ships |
| SQP, large scale | c.1997–2003 | follower (the SQP promise was old) | 2003 suspended; 2008–15 papers; no release | stated suspension; a later quiet return |
| Interior point / barrier for NLP | theory 1997/2001; software plan 2003 | after the IPM-for-NLP codes had shown scaling | no released NLP IPM | never announced |
| Filter methods | 2002 (theory with Fletcher, Leyffer, Toint, Wächter) | early (the idea was Fletcher–Leyffer's) | 2015 (filter SQP with Loh and Robinson) | package left in `forthcoming` |
| Penalty-free, filter-free (trust funnel) | 2007 | his own proposal | 2017 (interior-point trust funnel) | no package |
| Saddle-point / KKT preconditioning | 2000 | early in the constraint-preconditioning literature | 2014 (last SIMAX) | continues as package code |
| Nonconvex evaluation complexity | 2007 | early (a year after Nesterov–Polyak) | 2021–22 | book |
| Projection methods for feasibility | 2008 (one evaluation) | late, as a critic | 2011/12 ("How good are extrapolated bi-projection methods for linear feasibility problems?", *COAP*, 10.1007/s10589-011-9414-2) | negative evaluation |
| Materials-science preconditioning | 2013 | via grant and collaborator | 2016 | grant end |
| Least squares | 2015 (grant) | — | ongoing (2026 packages) | — |
| Stochastic gradient / ML | never | — | — | stated exclusion |

---

## 5. Failures, abandonments and unfinished items along the trajectory

The details and quotes are in notes 01–03. This list only dates them.

| When | Item | Evidence |
|---|---|---|
| 1989 | Correction to the 1988 CGT convergence proof (10.1137/0726044) | Crossref [T11] [practice] |
| 1995–2002 | LANCELOT B shelved "at that time" (then shipped inside GALAHAD 1.0 as "a stop-gap") | [T20] p.354 [stated] |
| 2003 | Large-scale SQP suspended | [T19] p.4 [stated] |
| 2003 | The announced barrier NLP solver was never released | [T13] tree, and note 03 [practice] |
| 2011–12 | Trust-funnel erratum | 10.1007/s10107-011-0491-x [practice] |
| 2014–17 | Complexity corrigendum, received 11 Nov 2014, accepted 31 Mar 2016: "the proof of Lemma 3.5 in that paper uses a result from an earlier paper in an incorrect way, and indeed the result of the lemma is false." 10.1007/s10107-016-1016-4 | author PDF p.1 [T34] [stated, primary] |
| 2008 → 2026 | BARC (2008) and FiSQP (2014) still in `src/forthcoming` | [T13] |
| 2023 CV → 2026 | Two books "in preparation" (a solo optimization-algorithms book, and *Computational quadratic programming* with Toint). Four technical reports "in preparation", including Coulibaly–Gould–Orban (IPMs without strict complementarity), Gould–Kočvara–Robinson–Toint (enriched recursive multilevel) and Gould (linear least squares over polyhedral sets). The last two map onto a small 2009 multilevel grant (EP/G038643/1) and the later CLLS/SLLSB packages. **None found published** by Crossref/arXiv queries in this run | CV p.20 [T02]; [T08][T11] [practice] |
| 2020–21 | Three complexity preprints without journal versions (probably absorbed into the 2022 book, see Turn 6) | [T08][T10][T11] |

No rejected papers or retracted claims were found.

---

## 6. The last 12 months (2025-09-28 → 2026-09-28), dated

All items are [practice, primary] unless marked.

| Date | Item | Source |
|---|---|---|
| 2025-09-28 → 10-11 | GALAHAD: work on TRB, TRS and RQS ("improve trb and related (unfinished)", 2025-09-28; zero and identity Hessians supported in TRS/RQS, 2025-10-05). SIFDecode: better decoding messages and exit codes (2025-09-28 → 10-01) | [T13][T16] |
| 2025-10-01 | ARCHDefs: "remove references to SPRAL (as this is now internal to GALAHAD)", following GALAHAD 5.3.0 (2025-09-03), which folded SPRAL's SSIDS and its MO/MS/MU/RB helpers into GALAHAD (headers: "Forked and extended for GALAHAD, Nick Gould, version 3.1, 2016") | [T17][T13][T14] |
| 2025-11-14 | arXiv 2511.11135 v1, Al Daas & Gould (math.NA; cross-list math.OC). Also posted on Optimization Online | [T09][T10] |
| 2025-11-17 / 11-23 / 11-27 | New GALAHAD packages TREK and NREK (principal authors "Hussam Al Daas and Nick Gould"); GALAHAD **5.4.0** released | [T13][T14] |
| 2026-01-14 / 01-19 | SNLS ("an algorithm for nonlinear least-squares over simplices") and SLLSB: header "originally released" dates. Principal author: Gould | [T13] (file headers) |
| 2026-01-16 | CUTEst: new tool `cutest_cishp`, and a "trial package for trying out new ideas" (`src/trial`) | [T15] |
| 2026-01-21, 03-02 | arXiv 2511.11135 v2 and v3 | [T09] |
| 2026-02-15 | REVERSE (reverse-communication type) package, header date. Principal author: Gould | [T13] |
| 2026 | STFC technical report "Event identification for digitised traces from muon decay detectors" (Shustin, Fowkes, …, Baker, Gould), 10.5286/stfctr.2026017. The abstract claims derivative-based methods "could enable approximately two- to four-fold higher usable count rates" for µSR experiments. Gould is last of 10 authors; his role is **not stated** | DataCite [T12] (abstract read; report not read) |
| 2026-05-15 → 06-04 | CUTEst: interface to the Uno solver (written by C. Vanaret and S. Leyffer, per the README Gould wrote), new tools `cutest_csp` and `cutest_cdimscj`; CUTEst **2.7.1** (2026-06-04) | [T15] |
| 2026-05-30 → 06-07 | SIF test-problem repository: "modify the licence and README", compressed versions of the too-large files (bundle adjustment BA-L…, MNIST…, LRCOVTYPE), master file pointed "at new repo", classification database updated. A second contributor (Pim Heeman) is active | [T18] |
| 2026-06-12 / 06-13 | "New packages for GALAHAD 5.5" (SNLS, SLLSB, REVERSE, committed by Fowkes); GALAHAD **5.5.0** (release note, via WebFetch: "new packages for solving nonlinear least-squares when the variables are constrained to lie between lower and upper bounds, or are constrained to lie within the intersection of non-overlapping unit simplices") | [T13][T14] |
| 2026-08-03 → 08-13 | Montoison replaces the C++ SSIDS code with Fortran and renames it SLBLT, now the default sparse solver. Gould commits fixes to the Fortran SSIDS code (2026-08-06, 08-08, 08-13: "still on the trail of the ldlt_tpp_factor issue") | [T13] |
| 2026-09-11 | GALAHAD **5.5.2**. The README already refers to "at least GALAHAD v5.6.0 and libHSL v2026.8.4"; package headers read "GALAHAD 5.6.0 - 2026-08-08" | [T13] |
| 2026-09-27 | CUTEst: "add highs as a supported package"; SIF: "Correction to attribution for HS113". His latest public activity | [T15][T18] |
| (2025-05-14, just before the window) | Fletcher memoir with J. A. J. Hall published | [T33] |
| (2025-06-17, just before the window) | *ACM TOMS* Hessian secant approximation, 10.1145/3728460 | [T11] |

**Readings of the last 12 months** [inferred]:
- He is active, and his output is in code: 23 GALAHAD commits, 14 CUTEst, 11 SIFDecode (10 as "Nick Gould", 1 as "nimgould"), 6 SIF and 2 ARCHDefs under his name in the window.
- **Commit authorship understates his work.** He has no GALAHAD commit between 2025-11-29 and 2026-06-22, yet three packages naming him principal author carry header dates of January–May 2026 and were committed by Fowkes on 2026-06-12. Anyone reading activity from git logs alone would misdate his work.
- **Current directions**: (a) the TR and regularization subproblem (TREK/NREK); (b) least squares with simplex and bound constraints; (c) owning the sparse direct solver inside GALAHAD instead of depending on SPRAL/HSL; (d) test infrastructure (Uno and HiGHS connections, re-licensing SIF); (e) applied work for the STFC ISIS facility.
- **No talks were found** for the window (one WebSearch; nothing on the RAL site). This fits the CV's note on talks [T02].

---

## 7. Era and resource context by phase

| Phase | Computing and tools | Team | Seniority and funding |
|---|---|---|---|
| 1976–85 | Mainframe Fortran libraries (NPL, Stanford SOL), technical-report culture | student, then a junior member of the Stanford SOL group; Waterloo assistant professor | SERC studentship, NSERC grant |
| 1985–95 | Fortran 77, HSL, anonymous ftp; test problems exchanged "by exchanging reports and pieces of paper" before SIF (Toint's account, ASR [0:45:42] [T28], secondary) | national-lab group; transatlantic trio funded by NATO travel grants | SSO/PSO, then Grade 7 |
| 1995–2006 | Fortran 90; workstation network (he ran the group's SUN/IBM/Compaq/Intel network 1990–2006, CV p.25); NEOS | GOT (Gould–Orban–Toint) plus RAL linear-algebra colleagues | Individual Merit fellow 1999; EPSRC CoI grants (£375k–£433k) |
| 2006–2016 | Matlab for prototypes (ARC I tests in Matlab 7.2, p.289 [T23]), Fortran 2003 for release; CCPForge SVN | Cartis–Gould–Toint; postdocs and junior staff; the one D.Phil. student | Oxford chair 2006–08; PI of EP/F005369/1; SIOPT EiC; STFC Senior Fellow 2011 |
| 2017–2026 | GitHub (2018), CI, Meson, C/Python/Julia/Matlab bindings, PyPI, precompiled binaries | Fowkes, Montoison, Al Daas, Scott; outside contributors | half time; grants listed only to 2020 on the CV; talks limited |

[inferred] Some of his practices depend on the national-lab setting: decades-long code maintenance, and few students with many peers. They will not transfer directly to a university group or a start-up solver team.

---

## 8. Trajectory patterns for Phase 2 (all [inferred], to be tested)

- **P1. Separate the layer you never leave from the layer you turn in.** The subproblem linear algebra is constant. Globalization strategies are tried, benchmarked and abandoned. Suggested skill behaviour: when a user's solver underperforms, ask first whether the subproblem solve (QP, KKT, TR) is the bottleneck, before changing the globalization. This follows Turn 2's "lesson".
- **P2. Let outside benchmarks trigger an exit, and say so in print.** Turns 1 and 2 were triggered by rivals' comparative tests, and the admissions are published.
- **P3. Enter on someone else's theorem that has no numbers.** ARC started from Nesterov–Polyak's result, which had "no numerical results". The move was to unify, weaken the assumptions, and add CUTEr tests.
- **P4. Close a line with a book or a package, not with an announcement.** 2000 and 2022 were books. TREK/NREK and SNLS were packages.
- **P5. New colleague + tool → old subproblem.** Keller/Wathen 2000, Orban/Rees 2014, Al Daas 2025.
- **P6. Grants open short excursions; only the one tied to the core (least squares) survived.**
- **P7. Explicit non-entry.** Stochastic and ML optimization are left out on purpose, with a stated reason (§3 Turn 8).

---

## Contradictions (kept, not reconciled)

1. **How and when CGT began.** Toint (podcast 2026, ASR, unchecked): he met "Nick Gould and Andy Cone [Conn]" at the 1979 ISMP in Montreal, visited Waterloo and "met Nick who was working there at the time", and "I think it was in 1981, Andy went for a sub-article [sabbatical] in France in Gros-en-Oble [Grenoble]. And there was an opportunity for Nick, Andy and me to meet. And we started working on Trust Regions at that time." ([0:38:32]–[0:39:30], T28, observed, secondary). Gould's CV: B.A. Oxford 1979, Stanford 1981–82, Waterloo 1982–85 (CV pp.1–2, T02, primary). The first CGT paper appeared in 1988, and the first Conn–Gould paper in 1984 [T11]. The two accounts do not fit together as stated.
2. **"More than 50 papers together"** (Toint about the trio, [0:39:42], ASR) vs DBLP: 54 Gould–Toint records but 12 with Conn [T07]. It depends on whether he meant the pair or the trio.
3. **SIOPT Editor-in-Chief start year**: 2004 (CV p.26) vs 2005 (homepage) [T01][T02].
4. **SQP**: "all but given up" (April 2003, [T19] p.4) vs the 2008–2015 SQP papers, with no released solver as of 2026 [T13]. The same stated abandonment followed by a return is in note 01.
5. **Package "release" dates in file headers vs git and release notes.** TREK header: "originally released in GALAHAD Version 5.2. February 15th 2025". But `src/trek` first appears in git on 2025-11-17, and the release note says 5.4.0 "adds the new packages TREK … and NREK" [T13][T14]. EXPO header: "originally released as EPF, GALAHAD Version 5.1. May 9th 2024", but tag v5.1.0 is dated 2025-01-12 and EXPO is still in `forthcoming`. [inferred] The header "release" dates seem to be internal start or version dates, not public releases. Not confirmed.
6. **Fortran stance**: 2003, "we believed (and still believe) Fortran 90 capable of providing all of the facilities we needed" [T20] vs 2023, Fortran "is perceived as old fashioned in many circles", so C interfaces for rivals' ecosystems [T21]. The two statements are not logically incompatible, but the stated priority changed.
7. **Activity signal**: git shows no GALAHAD commit by Gould from 2025-11-29 to 2026-06-22, while package headers name him principal author with dates inside that gap [T13].
8. **Toint on the complexity book**: in the ASR transcript he calls it "not so long as the Trasijan [trust-region] book" and faster to write, but also "too weak for my taste" (probably a mishearing) [T28]. The wording needs the audio.

## Gaps

- **Gould's own account of any turn in his career** (an interview, oral history or retrospective) was not found. Every stated trigger above comes from paper introductions or the 2003 essay. The only biographical narrative is Toint's (ASR, secondary).
- **Why he left Waterloo (1985)** and **why he left the Oxford chair (2008)**: not stated anywhere I found.
- **The prize papers**: the 1986 Leslie Fox Prize paper and the 1994 Beale–Orchard-Hays citation text were not found (the citation page is JavaScript or Cloudflare blocked, per note 01).
- **Google Scholar**: the WebSearch surfaced a profile id `1M6GG2kAAAAJ` for "Nick Gould", but WebFetch hit Google's CAPTCHA. **Not read or verified** (T32). Citation-per-year trends are therefore missing.
- **Talks in the last 12 months**: none found. The RAL talks page gives 404 (note 01). The CV lists invited talks only to 2018.
- **Fate of the in-preparation books and reports** (§5): unknown beyond "not found published".
- **Gould's role in the 2026 ISIS muon report**: not stated. The report itself was not read (DataCite abstract only).
- **The Fletcher memoir's full text** was not read in this run (Crossref abstract only). It may hold Harwell-era context for Gould's own path (Fletcher was at AERE Harwell before Dundee, per the abstract).
- **Grant funding after 2020**: the 2023 CV lists grants only to 2020. Current funding is unknown.
- **Pre-2018 code history**: the GALAHAD git history starts with the CCPForge transfer (SVN revision 706), so its earlier record is not visible here.

## Sources

- T01 · "Nick Gould", STFC RAL Computational Mathematics people page (biography, publication list), accessed 2026-09-28, https://www.numerical.rl.ac.uk/people/nick-gould/ · primary
- T02 · N. I. M. Gould, "Curriculum Vitae, Nicholas Ian Mark Gould", 2023, 28 pp., https://www.numerical.rl.ac.uk/media/nick-gould/nimg.cv.pdf · primary
- T03 · "Prof. Nick Gould", Oxford Mathematical Institute profile (status: Visiting Professor; Senior Fellow, STFC-RAL), accessed 2026-09-28, https://www.maths.ox.ac.uk/people/nick.gould · primary (institutional)
- T04 · Mathematics Genealogy Project, Nicholas Ian Mark Gould, id 89384, https://www.mathgenealogy.org/id.php?id=89384 · secondary
- T05 · Mathematics Genealogy Project, Walter Murray, id 39149 (student list), https://www.mathgenealogy.org/id.php?id=39149 · secondary
- T06 · Mathematics Genealogy Project, Jaroslav M. Fowkes, id 294956, https://www.mathgenealogy.org/id.php?id=294956 · secondary
- T07 · DBLP pid 55/5344, 98 records 1984–2025, via `scripts/dblp_works.py` (sparql.dblp.org), 2026-09-28, https://dblp.org/pid/55/5344.html · secondary (bibliographic)
- T08 · arXiv author searches ("Gould, Nicholas I M", "Gould, Nick", "Gould, N I M", "Gould, Nicholas", "Gould, N I"), 2026-09-28, https://arxiv.org/search/ · secondary (bibliographic). The export API returned HTTP 406
- T09 · H. Al Daas & N. I. M. Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems", arXiv:2511.11135 (v1 2025-11-14, v2 2026-01-21, v3 2026-03-02); abstract page and v3 PDF (pp.1, 5, 14–16 read) · primary
- T10 · Optimization Online, author page "Nicholas I. M. Gould" (10 postings, 2017-08 → 2025-11-14), https://optimization-online.org/author/nick-gould/ (via WebFetch) · secondary (bibliographic)
- T11 · Crossref REST API: 49 DOIs resolved (title, venue, year, authors all matched), ORCID-filtered and title queries, 2026-09-28, https://api.crossref.org · secondary (bibliographic)
- T12 · DataCite metadata and abstract, Shustin et al., "Event identification for digitised traces from muon decay detectors", STFC 2026, 10.5286/stfctr.2026017, https://epubs.stfc.ac.uk/work/67428951 · secondary (bibliographic; report not read)
- T13 · GALAHAD git repository ralna/GALAHAD, cloned 2026-09-28, HEAD afa13a5 (2026-09-26): commit log by author and date, tags v3.0.0–v5.5.2, first-commit dates of `src/*`, headers of trek, nrek, ssls, snls, sllsb, reverse, nodend, mo, ms, mu, rb, forthcoming/expo, README.md, `version`, https://github.com/ralna/GALAHAD · primary (practice)
- T14 · GALAHAD GitHub releases page (release notes v5.3.0–v5.5.2), via WebFetch 2026-09-28, https://github.com/ralna/GALAHAD/releases · primary (practice; wording from WebFetch's extraction, raw HTML blocked to curl)
- T15 · CUTEst git repository ralna/CUTEst, HEAD 733acc7 (2026-09-27): log, `src/uno/README.uno`, `src/trial/trial_main.F90` header, https://github.com/ralna/CUTEst · primary (practice)
- T16 · SIFDecode git repository ralna/SIFDecode, HEAD 979967c (2026-07-06), https://github.com/ralna/SIFDecode · primary (practice)
- T17 · ARCHDefs git repository ralna/ARCHDefs, HEAD 871a416 (2025-10-28), https://github.com/ralna/ARCHDefs · primary (practice)
- T18 · SIF git repository ralna/SIF, HEAD 319d16b (2026-09-27): log and README, https://github.com/ralna/SIF · primary (practice)
- T19 · N. I. M. Gould, "Some Reflections on the Current State of Active-Set and Interior-Point Methods for Constrained Optimization", SIAG/Optimization Views-and-News 14(1), April 2003, pp.2–7, https://www.numerical.rl.ac.uk/media/people/nick-gould/Goul03_siagopt.pdf · primary
- T20 · N. I. M. Gould, D. Orban & Ph. L. Toint, "GALAHAD, a library of thread-safe Fortran 90 packages for large-scale nonlinear optimization", ACM TOMS 29(4) (2003) 353–372, 10.1145/962437.962438 (author PDF, pp.353–355 read) · primary
- T21 · J. Fowkes & N. I. M. Gould, "GALAHAD 4.0: an open source library of Fortran packages with C and Matlab interfaces for continuous optimization", JOSS 8(87) 4882 (2023), 10.21105/joss.04882 (full text read) · primary
- T22 · J. Fowkes & N. Gould, "GALAHAD 4.0, nonlinear optimization", NA Digest v.22 n.15, 4 May 2022, https://na-digest.coecis.cornell.edu/na-digest-html/22/v22n15.html · primary
- T23 · C. Cartis, N. I. M. Gould & Ph. L. Toint, "Adaptive cubic regularisation methods for unconstrained optimization. Part I: motivation, convergence and numerical results", Math. Program. 127 (2011) 245–295, 10.1007/s10107-009-0286-5 (pp.245–248, 289 read) · primary
- T24 · N. I. M. Gould & D. P. Robinson, "A Second Derivative SQP Method: Local Convergence and Practical Issues", SIAM J. Optim. 20(4) (2010) 2049–2079, 10.1137/080744554 (p.2049 read) · primary
- T25 · N. I. M. Gould, *An introduction to algorithms for continuous optimization* (course booklet, © 2000, 2021), preface pp.v–vi, https://www.numerical.rl.ac.uk/media/people/nick-gould/cobook.pdf · primary
- T26 · C. Cartis, Curriculum Vitae (2025), positions p.1 and journal list pp.1–3, https://www.maths.ox.ac.uk/system/files/users/cv/Cartis_CV_2025_0.pdf · secondary
- T27 · "Hussam Al Daas", STFC RAL people page (biography), accessed 2026-09-28, https://www.numerical.rl.ac.uk/people/hussam-al-daas/ · secondary
- T28 · "Subject to: Philippe Toint", podcast hosted by Anand Subramanian, 27 July 2026; automatic transcript (not checked against the audio) saved at `product/nonlinear-team/philippe-l-toint/references/sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt`; episode https://podcasters.spotify.com/pod/show/subject-to/episodes/Subject-to-Philippe-Toint-e3mjb27 · secondary (collaborator's account, ASR)
- T29 · "Leslie Fox Prize for Numerical Analysis", Wikipedia (raw wikitext, winners list citing the IMA), accessed 2026-09-28, https://en.wikipedia.org/wiki/Leslie_Fox_Prize_for_Numerical_Analysis · secondary
- T30 · WebSearch 1: "Nick Gould" OR "Nicholas Gould" optimization Rutherford Appleton 2026 talk OR workshop OR seminar, 2026-09-28. No 2026 event found; surfaced T10 and the Scholar id in T32 · secondary (search)
- T31 · WebSearch 2: GALAHAD 5.0 OR 5.5 release announcement …, 2026-09-28. Surfaced the GALAHAD 5.5 documentation (dated 12 June 2026, authors Fowkes, Gould, Montoison, Orban) and the releases page (T14) · secondary (search)
- T32 · Google Scholar profile `1M6GG2kAAAAJ` ("Nick Gould"), https://scholar.google.com/citations?user=1M6GG2kAAAAJ · **not read** (CAPTCHA); identity not verified
- T33 · N. I. M. Gould & J. A. J. Hall, "Roger Fletcher. 29 January 1939—15 July 2016", Biogr. Mems Fell. R. Soc. 78 (2025) 127–146, published 2025-05-14, CC-BY, 10.1098/rsbm.2024.0037 · primary (Crossref metadata and abstract only; full text **not read** in this run)
- T34 · C. Cartis, N. I. M. Gould & Ph. L. Toint, "Corrigendum: On the complexity of finding first-order critical points in constrained nonlinear optimization", Math. Program. 161 (2017) 611–626, 10.1007/s10107-016-1016-4 (author PDF, p.1 read), https://www.numerical.rl.ac.uk/media/people/nick-gould/CartGoulToin16_mp.pdf · primary
