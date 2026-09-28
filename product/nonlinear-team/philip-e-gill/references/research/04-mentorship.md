# Philip E. Gill: students and collaborators (research agent 04)

- **Researcher**: Philip E. Gill. University of California San Diego (UCSD), Department of Mathematics, and co-director of the UCSD Center for Computational Mathematics (CCoM). Earlier at the National Physical Laboratory (NPL), UK, and the Stanford Systems Optimization Laboratory (SOL).
- **Dimension**: students and collaborators: supervision style, group habits, lab culture, tacit knowledge. Framework layer 7 (research organisation), plus the parts of layers 4–6 (experiment, judgement, writing) that show up in how students work.
- **Research date**: 2026-09-28
- **Sources consulted**: 31 (list at the end). 21 are primary: Gill's own pages, reports and papers, and one student thesis read for the student's own practice. 10 are secondary: the collaborator interview, the genealogy database, third-party pages and bios, Crossref, Wikipedia, and search results. WebSearch calls used: 2.
- **Local corpus**: `references/sources/papers/`, `essays/` and `software/` are empty, so there was no user-supplied material. `talks/` holds one auto-caption transcript (Margaret H. Wright, INFORMS 2019). Research agent 01 fetched it earlier in this run; it is not user-supplied. I used it and cite it by line number in that file. `private/` was not opened.
- **Language**: English (team.json).

## Read this first: what the evidence can and cannot carry

For Gill this pass found **no** student memoir, blog post, lab guide, onboarding document, Festschrift, collaborator tribute focused on him, or oral history. Gill is living, so there is no obituary. The only thesis acknowledgements obtained come from one thesis, Kungurtsev 2013, and it has **no acknowledgements section**. What remains:

1. **One first-hand collaborator account**: Margaret H. Wright's 2019 INFORMS History & Traditions interview. It covers the NPL → SOL period, the "Gang of Four", authorship and book decisions. It is YouTube auto-captions, not human-checked. Everything in it is Wright's account, so it is [observed], secondary, for Gill.
2. **One essay in the collective voice**: "George B. Dantzig and systems optimization" (2008). Gill is the first of five authors. It describes how SOL was organised and what its members valued. It is [stated] (collective), primary.
3. **Practice records**: Gill's lists of students and postdocs; his reports page; the acknowledgements, reference lists and experiment sections of reports co-written with students; author order; the UCSD optimizers site; one thesis (Kungurtsev 2013); grant lists. These are [practice], primary.
4. **The Mathematics Genealogy Project (MGP)**: [practice], secondary.

**Consequence**: the supervision style below is **reconstructed from what the records show**, not reported by students. Every tacit-knowledge item in §7 is **[inferred]**, and each one names the evidence it rests on. Nothing here says how Gill runs meetings, edits drafts or assigns topics. No source was found for any of that (see Gaps).

### Tag legend

- **[stated]**: said by Gill, or by a group that includes Gill, in first-person or collective voice.
- **[practice]**: what the records show was done (papers, reports, code, theses, author order, lists).
- **[observed]**: what someone else (a collaborator or third party) reports about Gill or his group.
- **[inferred]**: my synthesis. Treat it as a hypothesis.
- **P / S**: primary / secondary.

Each item that rests on a collaborator's or third party's account starts "according to ⟨who⟩, ⟨source⟩" and is marked S.

---

## 1. Who: lineage and the collaboration network

### 1.1 Upward lineage and "academic siblings"

- **Advisors**: MGP lists Gill's Imperial College PhD (1974, "Numerical Methods for Large-Scale Linearly Constrained Optimization") with "Advisor 1: Walter Murray", "Advisor 2: David Quinn Mayne" [practice, S (MGP id 6811)]. Research agent 01 records Murray–Gill co-authorship from 1972 to 2021. The advisor and student stayed peer collaborators for about 50 years [practice, P bibliographic; see 01-publications §1.4].
- **Many of Gill's closest collaborators are Murray's other students.** MGP lists 40 students for Murray (id 39149). Among them are Margaret H. Wright (Stanford 1976), Nicholas Gould (Oxford 1982), Stephen Nash (Stanford 1982), Francisco Prieto (Stanford 1989), Dulce Ponceleón (Stanford 1991) and Anders Forsgren (KTH 1990, advisor 1 P. O. Lindberg, advisor 2 Murray). Several of them co-author with Gill:
  - Ponceleón: SOL reports 91-3 and 91-7 (Gill homepage, Reports R34–R35) [practice, P].
  - Forsgren is a regular third author on papers with Gill's students:
    - Forsgren, Gill & Shinnerl, "Stability of Symmetric Ill-Conditioned Systems Arising in Interior Methods for Constrained Optimization", SIMAX 17 (1996) 187–211, DOI 10.1137/S0895479894270658.
    - Forsgren, Gill & Griffin, "Iterative Solution of Augmented Systems Arising in Interior Methods", SIOPT 18 (2007) 666–690, DOI 10.1137/060650210.
    - Forsgren, Gill & Wong, "Primal and dual active-set methods for convex quadratic programming", Math. Prog. 159 (2016) 469–508, DOI 10.1007/s10107-015-0966-2.

  [practice, P]
- **Intellectual influences named by the group**: "in addition to GBD, Martin Beale (Imperial College), Gene Golub (Stanford), and Jim Wilkinson (National Physical Laboratory) influenced the early SOL work on numerical software by the present authors" (Gill, Murray, Saunders, Tomlin & Wright 2008, p. 153, DOI 10.1016/j.disopt.2007.01.002) [stated, P].

### 1.2 Doctoral students (the downward lineage)

Gill's homepage lists 25 PhD students (1981–2024) [practice, P]. MGP lists 22 under Gill, including Renke Kuhlmann (Universität Bremen 2018, advisor 1 Christof Büskens, advisor 2 Gill), who is **not** on the homepage [practice, S]. The table joins the two lists with the first joint publication I could verify (Crossref, this run). The "lag" column is the years from the thesis to the first verified journal or book version of work with that student.

| Student | PhD (homepage) | Thesis title (MGP unless noted) | First verified joint paper with Gill (DOI) | Lag | Other senior co-author |
|---|---|---|---|---|---|
| Mary Fenelon | Stanford OR, Nov 1981 | Preconditioned Conjugate-Gradient-Type Methods for Large-Scale Unconstrained Optimization (MGP: advisor **Murray** only) | none found | — | — |
| Aeneas Marxen | Stanford OR, Jul 1986 (MGP: **1989**, advisor **Murray** only) | Primal Barrier Methods for Linear Programming | none found | — | — |
| Jerome Braunstein | UCSD, Jul 1993 | Composite Phase-One Methods for Linear Programming | none found | — | — |
| Joseph Shinnerl | UCSD, Sep 1995 | KKT-Based Interior-Point Methods for Numerical Optimization | SIMAX 1996, 10.1137/S0895479894270658 | ~1 | Forsgren |
| Michael W. Leonard | UCSD, Sep 1995 | Reduced Hessian Quasi-Newton Methods for Optimization | "Reduced-Hessian Quasi-Newton Methods for Unconstrained Optimization", SIOPT 12 (2001) 209–237, 10.1137/S1052623400307950; "Limited-Memory Reduced-Hessian Methods for Large-Scale Unconstrained Optimization", SIOPT 14 (2003) 380–401, 10.1137/S1052623497319973 | 6–8 | — |
| E. Michael Gertz | UCSD, Jan 1999 | Combination Trust-Region Line-Search Methods for Unconstrained Optimization | "A primal-dual trust region algorithm for nonlinear optimization", Math. Prog. 100 (2004), 10.1007/s10107-003-0486-3 | 5 | — |
| Alex Barclay | UCSD, Jul 1999 | SQP Methods For Large-Scale Optimization | "SQP Methods and their Application to Numerical Optimal Control" (Barclay, Gill, Rosen), 1998, 10.1007/978-3-0348-8802-8_21 | before thesis | J. B. Rosen |
| Roummel F. Marcia | UCSD, Mar 2002 | Primal-Dual Interior-Point Methods for Large-Scale Optimization | "Interior Methods For a Class of Elliptic Variational Inequalities" (Bank, Gill, Marcia), LNCSE 2003, 10.1007/978-3-642-55508-4_13 | ~1 | R. E. Bank |
| Julia Kroyan | UCSD, Feb 2004 | Trust-Search Algorithms for Unconstrained Optimization | none found | — | — |
| Joshua D. Griffin | UCSD, Mar 2005 (not in MGP) | "Interior-point methods for large-scale nonconvex optimization" (title as cited in the Erway–Gill–Griffin report) | SIOPT 2007, 10.1137/060650210 | 2 | Forsgren |
| Beate Winkelmann | UCSD, Dec 2005 | Finite Dimensional Optimization Methods and Their Application to Optimal Control with PDE Constraints | none found | — | — |
| Jennifer B. Erway | UCSD, Sep 2006 | Iterative Methods for Large-Scale Unconstrained Optimization | "Iterative Methods for Finding a Trust-region Step", SIOPT 20 (2009) 1110–1131, 10.1137/070708494 (with Griffin); "A Subspace Minimization Method for the Trust-Region Step", SIOPT 20 (2009) 1439–1461, 10.1137/08072440X | 3 | — |
| Daniel P. Robinson | UCSD, Sep 2007 | Primal-Dual Methods for Nonlinear Optimization | "A primal-dual augmented Lagrangian", COAP 51 (2012; online 2010) 1–25, 10.1007/s10589-010-9339-1 | 3 | — |
| Michael W. Ferry | UCSD, May 2011 | Projected-Search Methods for Box-Constrained Optimization | "A class of projected-search methods for bound-constrained optimization" (Ferry, Gill, Wong, Zhang), OMS 39 (2024; online Aug 2023) 459–488, 10.1080/10556788.2023.2241769 | **12** | Wong, M. Zhang |
| Elizabeth Wong | UCSD, Jun 2011 | Active-Set Methods for Quadratic Programming | "Sequential Quadratic Programming Methods" (IMA Vol. 154, online 2011) 147–224, 10.1007/978-1-4614-1927-3_6; "Methods for convex and general quadratic programming", Math. Prog. Comp. 7 (2015; online 2014) 71–112, 10.1007/s12532-014-0075-x | 0–3 | — |
| Joseph (Joey) Reed | UCSD, Nov 2011 | Methods for PDE-Constrained Optimization | none found | — | — |
| Vyacheslav Kungurtsev | UCSD, Jan 2013 | eScholarship PDF: "Second-Derivative Sequential Quadratic Programming Methods for Nonlinear Optimization" (MGP gives a different title; see Contradictions) | "A stabilized SQP method: global convergence", IMA JNA 37 (2017; online 2016) 407–443, 10.1093/imanum/drw004; "… superlinear convergence", Math. Prog. 163 (2017) 369–410, 10.1007/s10107-016-1066-7 | 3–4 | Robinson |
| Patrick Gallagher | Cognitive Science, Nov 2014 (co-advised) | Operator Theory for Analysis of Convex Optimization Methods in Machine Learning (MGP: advisor 1 Virginia de Sa, advisor 2 Gill) | none found | — | — |
| Anna Shustrova | UCSD, Jun 2015 | Primal-Dual Interior Methods for Quadratic Programming | none found | — | — |
| Fangyao Su | UCSD, Jul 2019 | Primal-Dual Path-Following Methods For Nonlinear Programming | none found | — | — |
| Ziyan Zhu | UCSD, Jun 2023 (not in MGP) | not found | none found | — | — |
| Minxin Zhang | UCSD, Jun 2023 | Projected-Search Methods for Constrained Optimization | "A projected-search interior-point method for nonlinearly constrained optimization", COAP 88 (2024) 37–70, 10.1007/s10589-023-00549-1 | ~1 | — |
| Alexander Guldemond | UCSD, Jul 2023 | Large-Scale Trust-Region Methods and Their Application to Primal-Dual Interior-Point Methods | none found | — | — |
| Yesheng Huang | UCSD, Aug 2023 | Primal-Dual Trust-Region Methods For Nonlinear Programming | none found | — | — |
| Jeb Runnoe | UCSD, Jun 2024 | Second-Derivative SQP Methods for Large-Scale Nonconvex Optimization | report only: "On Recent Developments in BFGS Methods for Unconstrained Optimization", CCoM 22-04 (no journal version found by agent 01) | — | — |
| Renke Kuhlmann | Bremen 2018 (MGP only) | A Primal-Dual Augmented Lagrangian Penalty-Interior-Point Algorithm for Nonlinear Programming | none found | — | Büskens (advisor 1) |

"None found" means none in this run's checks (the homepage reports list, Crossref, and agent 01's DBLP/OpenAlex list). It does not mean none exists.

- **Postdocs are former students, every time.** The homepage "Post-Docs" page lists exactly four postdocs, and each is one of his own PhD graduates: E. Michael Gertz (1999–2000), Michael W. Leonard (2002–2003), Jennifer B. Erway (2006–2007) and Elizabeth Wong (2011–2015) [practice, P].
- **Student to maintainer of the group's production code.** Wong is the fourth author, after Gill, Murray and Saunders, of the current SNOPT manual: "User's Guide for SNOPT 7.7: Software for Large-Scale Nonlinear Programming", CCoM 18-1 (2018). It is the reference the UCSD optimizers site gives for SNOPT (ccom.ucsd.edu/~optimizers/solvers/snopt/) [practice, P]. The QP solver SQIC ("Sparse Quadratic programming using Inertia Control") is described as "a particular implementation of the method for standard form QPs described in Section 4" of the Gill–Wong QP paper (genqp report, p. 3). It is distributed on the same site next to SQOPT [practice, P].

### 1.3 Grand-students and the alumni loop

- MGP lists 8 students for Marcia at UC Merced (2017–2025), among them **Johannes Brust (UC Merced 2018)**. Kungurtsev has one student (Antonio Bellon, CTU Prague 2024), and Robinson has one (Hassan Mohy-ud-Din, Johns Hopkins 2014) [practice, S (MGP)].
- **The loop closes**: Brust, a grand-student through Marcia, later co-authors with Gill: Brust & Gill, "An LDL^T Trust-Region Quasi-Newton Method", SISC 46 (2024) A3330–A3351, DOI 10.1137/23M1623380 [practice, P].
- **Alumni collaborate with each other on a group theme.** Marcia and Erway, both Gill graduates, are the PIs of the NSF collaborative award "Trust-Search Methods for Inverse Problems in Imaging" (CMMI-1333326 and CMMI-1334042; Marcia's page faculty.ucmerced.edu/rmarcia/NSF_TrustSearch.html) [practice, S (third-party page)]. Output includes:
  - Brust, Erway & Marcia, "On solving L-SR1 trust-region subproblems", COAP 66 (2017; online 2016) 245–266, DOI 10.1007/s10589-016-9868-3.
  - Erway & Marcia, "On solving large-scale limited-memory quasi-Newton equations", LAA 515 (2017) 196–225, DOI 10.1016/j.laa.2016.11.003.

  [practice, P]
  - [inferred] The term "trust-search" appears first in this lineage in Kroyan's 2004 thesis title ("Trust-Search Algorithms for Unconstrained Optimization"). It builds on Gertz's 1999 "Combination Trust-Region Line-Search Methods". So a named group concept travelled from Gill's students of about 1999–2004 into a 2013 grant held by two alumni, and back to Gill through their student in 2023–24. This rests on titles and grant text only. I did not read the theses.

### 1.4 Colleagues and application partners at UCSD

- **Grant co-PIs** (homepage Grants page): R. E. Bank, M. J. Holst and L.-T. Cheng on the PDE-constrained optimization awards (NSF DMS-0208449, 2002–05; DMS-0511766, 2005–08), and J. B. Rosen and L. R. Petzold on an NSF CCR subcontract (1995–99) [practice, P]. Bank and Holst also sit on Kungurtsev's thesis committee (thesis p. ii, eScholarship 6081f5jc) [practice, P].
- **Application partners**: H. D. I. Abarbanel (physics) and T. Q. Nguyen (ECE). Wong appears on an Abarbanel chapter: "Dynamical Parameter and State Estimation in Neuron Models" (The Dynamic Brain, 2011), DOI 10.1093/acprof:oso/9780195393798.003.0008 [practice, P]. There is also a DOE final report, "Parameter Estimation and Model Validation of Nonlinear Dynamical Networks" (2015), DOI 10.2172/1177970, with Abarbanel and Gill named [practice, P].

---

## 2. Collaboration norms (from the Gang of Four onward)

### 2.1 Alphabetical authorship, and why

- **According to Margaret H. Wright, INFORMS interview 2019** (auto-captions, `talks/2019-informs-margaret-wright-interview-autocaptions.txt` lines 205–211) [observed, S]: the SOL group "decided that we would always have all four names on what we did and that they would be an alphabetical order Phillip liked that a lot because it would always be Gil at all and I would sometimes say what if I changed my name to aardvark they don't laugh but I was always last okay but we decided that there was no way we could work closely together and have arguments about you know who gets the credit whose name gets to go first because we all knew of instances of that where it led to very bad feeling" [sic, auto-caption; "Gil at all" = "Gill et al."].
- **The norm carries over to his students** [practice, P]. Every student paper verified above is alphabetical, for example Barclay–Gill–Rosen, Bank–Gill–Marcia, Erway–Gill–Griffin, Ferry–Gill–Wong–Zhang, Gill–Kungurtsev–Robinson, Gill–Zhang, Brust–Gill. Where the student's name sorts after "Gill", the student comes second or later even on thesis work (Gill & Leonard 2001/2003, Gill & Wong 2011/2015, Gill & Zhang 2024). New members are slotted in alphabetically: the SNOPT 7.7 manual reads Gill, Murray, Saunders, Wong.
- **Boundary of the norm** [practice, P]. Papers led by application partners do not always follow it:
  - Chan, Khoshabeh, Gibson, Gill & Nguyen, "An Augmented Lagrangian Method for Total Variation Video Restoration", IEEE TIP 2011, DOI 10.1109/TIP.2011.2158229: not alphabetical.
  - Creveling, Gill & Abarbanel, "State and parameter estimation in nonlinear systems as an optimal tracking problem", Phys. Lett. A 2008, DOI 10.1016/j.physleta.2007.12.051: not alphabetical.
  - The 2011 Abarbanel book chapter above is alphabetical.
- [inferred] **Reading rule for the skill**: in Gill's optimization-methods papers, author order says nothing about who led the work or who wrote the code. Do not use first-author position to identify "the student's paper".

### 2.2 Who co-authors what: book decisions

- **According to Wright** (lines 211–215) [observed, S]: the four "had talked for quite a while about writing a book". Saunders "basically said I don't I don't want to be a co-author … it's going to be kind of away from the research that I want to do … I'll happy happy to look at what you've done but I don't want to be a co-author" [sic]. So "the three of us" (Gill, Murray, Wright) wrote *Practical Optimization*. A member could stay inside the group and still opt out of a project, and this was accepted.
- **According to Wright** (lines 329–333) [observed, S]: *Numerical Linear Algebra and Optimization* was titled "volume one" because she was leaving for Bell Labs. "someone said let's just put volume and then we can finish later well of course we didn't if on to never came out" [sic; "volume two never came out"]. This is an **abandoned project**, and research agent 01 records it as well.

### 2.3 Collective insight, credit at the group level

- **According to Wright** (lines 255–261) [observed, S]: during Karmarkar's Stanford talk, "from that conversation emerge the this looks like the equations in a barrier method". Wright says she was the one who said it. "Walter says yeah but I was your adviser … Michael said no no I knew about it Philip knew about it" [sic].
- **The same event in the group's own collective voice** [stated, P]: "During Karmarkar's Stanford talk, the SOL researchers, trained in nonlinear optimization in general and barrier methods in particular [23,24], observed the strong similarity between the equations in Karmarkar's method and those arising in the 1960s logarithmic barrier method of Fiacco and McCormick" (2008 essay, p. 154). The result was a five-author paper, "the Stanford SOL 'gang of four' … and their former colleague John Tomlin, with help from Irvin Lustig (then a Stanford Ph.D. student working with GBD)" (p. 154): Gill, Murray, Saunders, Tomlin & Wright, "On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method", Math. Prog. 36 (1986) 183–209, DOI 10.1007/BF02592025 [practice, P].
- [inferred] This fits the alphabetical rule: individual priority is joked about but never settled, and credit goes to the group. Note that a PhD student (Lustig) was brought in to help.

### 2.4 Negative results that went unpublished

- **According to Wright** (lines 241–243) [observed, S]: after Khachiyan (1979), "we'd take some linear programs we would run conscience myth [Khachiyan's method] and it was always always in our examples way slower than the simplex method … so we didn't ever write a paper about this in retrospect I wish we had because we had lots of numerical results" [sic]. This is a recorded **failure to publish a negative result**, and the group later regretted it.

---

## 3. Lab culture inherited from the Stanford SOL (collective stated voice)

All items below come from Gill, Murray, Saunders, Tomlin & Wright (2008), "George B. Dantzig and systems optimization", *Discrete Optimization* 5:151–158, DOI 10.1016/j.disopt.2007.01.002 (read in full from ccom.ucsd.edu/~peg/papers/gbd.pdf). They are [stated, P] unless marked. Wherever the essay describes Dantzig's views, it is also the five authors' account of the programme they worked in.

- **The lab's programme** (p. 152, their summary of Dantzig's SOL paper): a "critical mass" is needed so that "3. Software implementing these methods can be written and systematically tested on representative problems; 4. Insights can be obtained into the nature of the problems and the properties of the general methods; 5. Based on these insights, methods can be developed to take advantage of the special structure of the most interesting and important problems." Also: "An essential part of GBD's perspective was that the fruits of all these activities should be freely available to the wider community."
- **"Math it up"** (p. 153): "Ph.D. students with practical inclinations also became involved with SOL activities, although they were warned by George that they needed to 'math it up' to pass muster with the primarily theoretical OR Department." (Agent 02 also records this.)
- **Resource context: funding software by stealth** (p. 153): "United States government agencies were reluctant to fund software development, which was not considered to be fundamental research … he managed to do so by bootstrapping grants in optimization that emphasized mathematical theory without mentioning any of the software-related activities that he planned to include." In 2008 the authors still write: "obtaining sustained government funding for software development remains a challenge" (p. 156).
- **Physical scale** (p. 153): when Tomlin arrived in 1970 the lab room held "only a drafting table, a large cabinet … and an IBM 'golfball' computer terminal". The staff were full-time researchers, not faculty. Arrival order: Saunders 1975, Wright 1976, Gill and Murray 1979 from NPL. **According to Wright** (line 179) [observed, S], she was hired "as a senior research associate not a faculty member".
- **Why Gill and Murray left NPL. According to Wright** (lines 189–191) [observed, S]: NPL "had been a place where you could just do the research you wanted … the bosses changed the view they said no no the people that work here have to make contributions to British industry and they have to you know find business customers". So Gill's move to SOL was, on this account, a move toward research freedom.
- **Test-problem culture** (p. 155–156): SOL contributed early netlib LP problems (25fv47, afiro, pilot, …). "long before the availability of tools for doing so, Irv Lustig analyzed and created graphical representations of the matrix structures in the first 53 netlib problems". The essay also gives an example of learning from failures on a named problem: interior methods were slow on `israel` because of "fill-in from a few dense columns", and "linear algebraic techniques were soon developed to address this situation" (p. 156).
- **Senior colleague as shield for software work** (p. 153): Dantzig "dedicated vast amounts of his time and energy to generating support for, nurturing, and protecting software-related activities", in "happy (for us) contrast to some of his colleagues who regarded the design and writing of software as trivial or uninteresting".

---

## 4. Supervision practice at UCSD (reconstructed from records)

### 4.1 Thesis topics follow the group's current method line and its grants

[practice, P (titles from MGP, S; grants from homepage, P); reading: inferred]

| Period | Student topics | Group context at the time |
|---|---|---|
| 1993–1995 | phase-one LP (Braunstein), KKT interior methods (Shinnerl), reduced-Hessian quasi-Newton (Leonard) | post-Karmarkar interior-method linear algebra; NSF DMI-9424639 "Large-Scale Constrained Optimization" (1995–98) |
| 1999–2005 | combination trust-region/line-search (Gertz), trust-search (Kroyan), SQP for optimal control (Barclay), interior methods (Marcia, Griffin) | SNOPT (SIOPT 2002); NSF ACI-0082100 "Innovative Software for Large-Scale Nonlinear Optimization" (2000–03) |
| 2005–2011 | PDE-constrained optimization (Winkelmann 2005, Reed 2011), trust-region subproblems (Erway 2006), primal-dual augmented Lagrangian (Robinson 2007), projected search (Ferry 2011), QP active-set (Wong 2011) | NSF DMS-0208449 "Optimization with PDE Constraints" (2002–05) and DMS-0511766 "Methods and Applications for PDE-Constrained Optimization" (2005–08), co-PIs Bank, Cheng, Holst |
| 2013–2024 | stabilized/second-derivative SQP (Kungurtsev 2013, Runnoe 2024), interior methods for QP/NLP (Shustrova 2015, Su 2019), trust-region interior (Guldemond, Huang 2023), projected search (M. Zhang 2023) | NSF DMS-0915220, DMS-1318480, DMS-1361421; DOE DE-SC0002349; NSF RTG DMS-1345013 (acknowledged in the Gill–Runnoe report, p. 1) |

- [inferred] Topics are **assigned from inside the advisor's current programme** rather than proposed by students from outside it. The one clear exception is the co-advised Cognitive Science thesis (Gallagher 2014). The PDE-constrained theses coincide exactly with the PDE-constrained grant years.

### 4.2 Devices passed from one student generation to the next

[practice, P]

- **Gertz (thesis 1999) → Erway and Griffin (2007).** From Erway, Gill & Griffin, "Iterative Methods for Finding a Trust-Region Step", report NA 07-2 (Nov 2007), p. 20, published as SIOPT 20 (2009), DOI 10.1137/070708494: the iterate is updated "using a line search based on Gertz's 'biased' Wolfe line search (see Gertz [12])", and "The term 'biased' is used by Gertz to refer to a deliberate bias against reducing the trust-region radius when αj is small."
- **Ferry (thesis 2011) → M. Zhang (2020).** From Ferry, Gill, Wong & Zhang, "A Class of Projected-Search Methods for Bound-Constrained Optimization", CCoM 20-07, p. 22: "The resulting implementations, LRHB-qWolfe, and LRHB-qArmijo are based on the Fortran package LRHB (see Ferry et al. [12])." Reference [12] is "A limited-memory reduced-Hessian method for bound-constrained optimization", CCoM 20-05, 2020, by the same four authors. Ferry's 2011 thesis is cited separately as [11].
- **Kungurtsev and Robinson → M. Zhang (2022).** From Gill & Zhang, "A Projected-Search Interior Method for Nonlinear Optimization", CCoM 22-01, p. 27: "For comparison purposes, results are also given for two primal-dual interior-point methods that do not use projection … The second is Algorithm pdb, which is an extension of the primal-shifted method of Gill, Kungurtsev and Robinson [15]." The predecessor students' method is the baseline for the new student.
- **Theses are cited as technical sources, sometimes decades later.** The reports downloaded in this run cite, as "PhD thesis":
  - Fenelon 1981: cited in the 2007 trust-region reports, i.e. 26 years later.
  - Gertz 1999 (trust reports).
  - Kroyan 2004 (SQP survey).
  - Griffin 2005 and Erway 2006 (trust report).
  - Robinson 2007 (pdmerit, pdsqp, SQP survey).
  - Wong 2011 (QP reports).
  - Ferry 2011 (quasiwolfe).
  - Kungurtsev 2013 (pdsqp).
  - M. Zhang 2023 (pdproj).

  One example of how they are used, from the trust report p. 3: "Subspace minimization methods for general large-scale unconstrained optimization have been considered by Fenelon [10], Gill and Leonard [14, 15], Nazareth [28], and Siegel [36, 37]."

### 4.3 Benchmark discipline visible in a student's thesis

Source: Kungurtsev, *Second-Derivative Sequential Quadratic Programming Methods for Nonlinear Optimization*, PhD thesis, UCSD 2013, chair Gill (eScholarship 6081f5jc; chapter 10 read). This is [practice, P] for Kungurtsev and [practice, S] as evidence of Gill's supervision. Spaces lost in PDF text extraction have been restored in the quotes.

- **Test set and protocol** (p. 159): CUTEr problems. "the number of variables and constraints were chosen to be the largest permissible values less than 500 … The total of 540 problems were selected." The outer-iteration limit was 1000 and the optimality threshold 10^-8.
- **The baseline is the group's own production code plus a commercial one** (pp. 159–160): "pdSQP converged to a point satisfying the optimality conditions for 407 (75%) problems, compared to 452 (84%) for SNOPT, and 319 (59%) for Matlab's fmincon SQP algorithm."
- **A weaker result reported without spin, with its reason stated** (p. 160): "These results are encouraging, as SNOPT and fmincon are sophisticated packages that have been developed over a number of years, whereas pdSQP is a prototype Matlab implementation."
- **Failure reasons coded, not hidden** (p. 161): unsolved problems carry letter codes: "m – the maximum number of iterations was exceeded", "b – the maximum number of backtracks for the line-search was reached", "i – the second order modification of the free Hessian matrix failed", "c – the preconvexification procedure failed", "q – the QP solver failed to produce a solution", "d – the QP solver failed to produce a descent direction for the merit function".
- **Variants tested one feature at a time** (p. 161): pdSQP, pdSQPcc (concurrent and post convexification), pdSQPid0 (active-set identification), pdSQPccnc (negative curvature), on 116 Hock–Schittkowski problems. The simplest variant solved the most equality-constrained problems (56 of 71, against 48, 48 and 40).
- **The same discipline under Gill's co-authorship ten years later** [practice, P]. Gill & Zhang 2022 (CCoM 22-01, p. 27): "All three Matlab implementations were initialized with identical control parameters that were chosen based on the empirical performance on the entire collection of problems." Each has a companion report of full per-problem tables: CCoM 22-03 "Numerical Results for a Projected-Search Interior-Point Method" and CCoM 20-08 "Supplementary Numerical Results for Projected-Search Methods for Bound-Constrained Optimization". There are also separate "equations" reports: CCoM 19-04, 21-04, 22-02.
- **Tooling across eras** [practice, P]:
  - Matlab prototypes: Kungurtsev 2013; the Erway–Gill reports of 2007–08 ("implemented and run in Matlab"); pdProj 2022 ("Matlab version R2022b").
  - Fortran production codes: SQIC in Fortran 2008 (genqp p. 3); LRHB in Fortran; the Brust & Gill method "implemented in Matlab and Fortran 90. All software is available in the public domain" (trustRegionQN report).
  - Test sets: CUTEr, later CUTEst, supplied by Gould. "We would like to thank Nick Gould for providing the latest version of the CUTEst test collection" (Gill, Saunders & Wong 2015, report p. 26; "On the Performance of SQP Methods for Nonlinear Optimization", DOI 10.1007/978-3-319-23699-5_5).

### 4.4 Students placed inside ongoing alumni projects

- Gill & Robinson, "A Globally Convergent Stabilized SQP Method" (report CCoM 13-03, p. 34; SIOPT 23 (2013), DOI 10.1137/120882913), acknowledgements: "We would like to thank Slava Kungurtsev for numerous discussions during the preparation of this paper." [practice, P]. Kungurtsev was then a PhD student, and Robinson had graduated in 2007. From 2013 the work continues as a three-way Gill–Kungurtsev–Robinson series: reports CCoM 13-04, 14-01, 16-01, 19-03, 19-04, 21-04; SIOPT 30 (2020), DOI 10.1137/19M1247425 [practice, P].
- [inferred] **Mode of apprenticeship**: a new student joins an advisor–alumnus pair already working on a line, first thanked in the acknowledgements, then listed as co-author.

### 4.5 An outside senior co-author on a student's first paper

[practice, P; reason inferred]

- Shinnerl and Griffin with Forsgren (KTH); Marcia with Bank (UCSD, PDE); Barclay with J. B. Rosen (UCSD). Wong's first computational-assessment paper is with Saunders (Gill, Saunders & Wong 2015). The Gill–Wong acknowledgements thank "Michael Saunders, Iain Duff and Nick Gould for their assistance during the development of SQIC and the computational tests of Section 7" (genqp report, p. 33), and "Anders Forsgren for numerous discussions on SQP methods during the preparation of this paper" (SQP survey report NA 10-3, p. 37).
- [inferred] A student gets a second senior reader and linear-algebra or testing help from Gill's own network, which is largely his academic siblings.

### 4.6 Long gestation, finished after the student leaves

[practice, P for the dates; inferred for the reading]

- Lags from thesis to first journal version (table in §1.2) run from about 1 to 12 years. Examples: Leonard 1995 → SIOPT 2001/2003; Gertz 1999 → Math. Prog. 2004; Robinson 2007 → COAP 2010/12 and SIOPT 2013; Kungurtsev 2013 → IMA JNA and Math. Prog. 2016/17; Ferry 2011 → OMS 2023/24, with a new student (Zhang) and a former postdoc (Wong) added. Leonard's journal papers appeared during or just before his 2002–03 postdoc.
- [inferred] Student work is treated as the start of a line that the advisor carries on, often through a postdoc year or later co-authorship. It is not a unit to publish at graduation. Papers are held until the theory (global and local convergence) and the numerical testing are both complete. 01-publications and 02-methodology record the same standard for Gill's own work.

### 4.7 Funding and outside experience for students

[practice, P]

- Acknowledged support in student co-authored reports: the NSF Research Training Grant DMS-1345013 (Gill & Runnoe, p. 1); DOE DE-SC0002349 (Gill & Robinson 2013 and Gill & Wong QP report); Northrop Grumman Space Technology "SNOPT for Real Time Trajectory Generation of Constrained Dynamical Systems" (2005–06) and NASA Goddard "Software for Constrained Optimization" (2002–03) (Grants page).
- Kungurtsev's vita (thesis p. x) lists "2011 Research Intern at Argonne National Lab" and "2007–2013 Graduate Teaching Assistant and Graduate Student Researcher".

### 4.8 Thesis form (single case, do not generalise)

- Kungurtsev's 2013 thesis gives two long background chapters to optimality conditions, constraint qualifications and stability theory (ch. 2 and 4, about 33 pp.) before the method chapters. It has no acknowledgements section (table of contents, pp. iv–vii) [practice, P]. With only one thesis read, this is a single observation, not a group norm.

---

## 5. Gill's own stated statements that bear on supervision

- Math 271B course page, Winter 2022 (ccom.ucsd.edu/~peg/math271b/): "I prefer not to answer technical questions by email ( n emails for me to understand your question, m emails for you to understand my answer), but students are welcome to attend my office hours or see me after class." [stated, P] (Agent 02 also records this.)
- The same page: "Matlab enables the student to concentrate on the fundamental ideas of numerical optimization without becoming distracted by the rigors of mental arithmetic." The SU-grade option requires students to make a "fair attempt" at the homework [stated, P].
- **Nothing else found**: no stated philosophy of PhD supervision, no advice to students, no lab rules. Agent 02 reached the same conclusion.

---

## 6. Where the alumni went (network and outcomes)

[practice, S unless marked]

- **Gill's own reports page links each co-author to a current page**, which shows him keeping track of the alumni network [practice, P]. The links: Erway (wfu.edu/~erwayjb), Robinson (engineering.lehigh.edu), Kungurtsev (cs.felk.cvut.cz / fel.cvut.cz), Marcia (faculty.ucmerced.edu/rmarcia), Griffin (blogs.sas.com), Gertz (ccr.cancer.gov staff directory), Brust (search.asu.edu). The dates of these links are unknown.
- **Industrial solver R&D.** According to his SAS blog author bio: "Josh Griffin received his PhD in Mathematics from the University of California, San Diego in 2005. As a Senior Manager in the Advanced Analytics Department, Josh leads a R&D team in SAS/OR devoted to developing software for general and special purpose nonlinear optimization … Prior to joining SAS, Josh was a senior member of the technical staff at Sandia National Laboratories developing derivative-free software for simulation based optimization" (blogs.sas.com/content/author/joshgriffin/, undated) [observed, S].
- **Academic**: Erway, professor of mathematics at Wake Forest (her homepage). Marcia at UC Merced, where he supervises the 8 students listed on MGP. Robinson at Lehigh; Kungurtsev at CTU Prague (links above).
- [inferred] The group's product is people who build solvers, in industry, national labs or academia, and who keep working on the group's themes: trust-search, quasi-Newton, interior and SQP methods.

---

## 7. Tacit knowledge (what the students would know; all [inferred])

Each item names its evidence. None was confirmed by a student account.

| # | Tacit rule | Evidence | Confidence |
|---|---|---|---|
| T1 | Author order is alphabetical; credit is not negotiated through it. Your name may come second on your own thesis work. | §2.1: Wright's account of the origin; every verified student paper | high (practice is uniform) |
| T2 | Your baseline is the group's own previous method or SNOPT, run with identical control parameters. Beating fmincon is not enough. | §4.2, §4.3: Kungurtsev thesis; Gill & Zhang 2022 | medium-high |
| T3 | Prototype in Matlab on the whole CUTEr/CUTEst subset; the production version goes into Fortran; your code will outlive your PhD (LRHB, SQIC). | §4.3; §4.2 (LRHB reused 9 years later) | medium |
| T4 | Report every failure with a reason code, and publish full per-problem tables, if necessary in a separate "numerical results" report; derivations go in a separate "equations" report. | §4.3 (Kungurtsev codes; CCoM 19-04, 20-08, 21-04, 22-02, 22-03) | medium-high |
| T5 | Your thesis is part of the group's technical record: it will be cited as a source for devices (e.g. "Gertz's biased Wolfe line search"), so name your devices and write them out fully. | §4.2 | medium |
| T6 | Expect the journal version to take years and to be finished with Gill after you graduate, possibly with the next student added. | §4.6 | medium |
| T7 | "Math it up": algorithmic or software work must carry full convergence theory (global and local) to count. | §3 (SOL legacy); §4.6; 02-methodology T3 | medium (the link from SOL to UCSD is inferred) |
| T8 | Numerical stability outranks elegant theory: "A method may have wonderful theoretical properties, but if it fails to deal with numerical issues these properties simply cannot be realized." | Gill & Runnoe report GR22, p. 38, co-written with a PhD student (quoted in 02-methodology) | medium |
| T9 | Take technical questions to the office, not to email. | §5 (course page) | medium (stated for courses; extension to PhD students inferred) |
| T10 | Your first paper will likely have a senior outside reader (Forsgren, Saunders, Bank, Rosen). | §4.5 | low-medium |

---

## 8. Failures, abandoned directions, unresolved outcomes

- **Unpublished negative results on Khachiyan's method** (about 1979–80). According to Wright (line 243) [observed, S], the group regretted not writing them up.
- ***Numerical Linear Algebra and Optimization*, volume 2**: never written. According to Wright (lines 331–333) [observed, S], because she left for Bell Labs.
- **Kungurtsev's pdSQP prototype was less reliable than SNOPT** (75% vs 84% on 540 CUTEr problems), and the thesis says so (§4.3) [practice, P]. The stabilized-SQP theory was published (2016/17, 2020), but no distributed pdSQP code was found (Gaps).
- **Journal fate unknown, per agent 01**: "A Regularized SQP Method with Convergence to Second-Order Optimal Points" (Gill, Kungurtsev, Robinson; Optimization Online 2013); Gill & Runnoe's BFGS report (CCoM 22-04). [inferred] The first matches ch. 9 of Kungurtsev's thesis ("Second-Order Primal-Dual SQP"), which may be a thesis line that never reached a journal.
- **Students with no joint publication found**: 12 of the 25 on the homepage (§1.2), none of whose theses I read. The reasons cannot be known from this evidence. It is only an absence in the checked indexes.

## 9. Era and resource context

| Era | Setting | Team | Compute and tools | Seniority |
|---|---|---|---|---|
| 1970–79 | NPL, Teddington: government lab, research freedom until policy changed (Wright, lines 189–191) | Gill and Murray (Murray also his advisor); Wright visiting for her thesis for 6 months (Wright, lines 159–165) | Fortran (per 01-publications); computing setup not documented in these sources | early career, peers |
| 1979–87 | Stanford SOL (OR Dept), funded through theory grants (essay p. 153) | "Gang of Four" research staff plus Tomlin, Stanford PhD students (Fenelon, Marxen; MGP lists Murray as advisor) and Lustig as helper | in the 1970s SOL, "a few decks of IBM cards" (Wright, line 185) and a terminal link to SLAC (lines 201–205); TeX for *Practical Optimization* (1981; lines 215–223) | mid-career research staff, not faculty |
| 1988–2000s | UCSD Mathematics / CCoM | Gill as the only PI in his group, with 1–3 PhD students at a time [inferred from the dates in §1.2]; Murray and Saunders at Stanford for the software | workstations; Matlab prototypes; Fortran solvers; CUTE/CUTEr | senior faculty; Distinguished Professor, SIAM Fellow, SDSC Senior Fellow (homepage "In Person") |
| 2010–24 | UCSD; last PhD cohort 2023–24 | Gill plus Wong (postdoc then co-author), alumni Robinson, Kungurtsev and Brust as remote co-authors | Matlab R2022b; CUTEst; Fortran 2008 (SQIC) | senior or emeritus (agent 02: UCSD Profiles lists Emeritus) |

---

## Contradictions (kept, not reconciled)

1. **Fenelon and Marxen.** Gill's homepage lists both as his graduate students (Stanford OR, 1981 and **July 1986**). MGP lists **Walter Murray alone** as advisor for both and dates Marxen's PhD to **1989**. [practice, P vs S] Co-supervision at SOL would explain both lists, but no source confirms it.
2. **Kungurtsev thesis title and month.** MGP: "SQP Methods for Nonlinearly Constrained Optimization". The eScholarship PDF and Gill's own citation (pdsqp report ref. [37]): "Second-Derivative Sequential Quadratic Programming Methods for Nonlinear Optimization". The homepage dates it January 2013; Gill's citation says February 2013.
3. **Student counts.** The homepage lists 25 students, including Griffin and Z. Zhu, neither of whom is in MGP. MGP counts 22 plus Kuhlmann (Bremen 2018), who is not on the homepage. Agent 01 records the same.
4. **Who saw the Karmarkar–barrier link.** Wright's account has Wright, Murray ("I was your adviser") and Saunders ("Philip knew about it") each claiming or sharing it (lines 257–259). The 2008 essay credits "the SOL researchers" collectively (p. 154).
5. **Scope of the alphabetical rule.** It is uniform in the optimization-methods papers but not in two application papers (Chan et al. 2011; Creveling, Gill & Abarbanel 2008). A third application paper (Abarbanel et al. 2011) is alphabetical. This is recorded as a boundary, not resolved.

## Gaps (what I could not find)

- **No first-hand student account**: no memoir, blog post, interview, lab guide or onboarding document by any of the 25 students or 4 postdocs. Nothing on group meetings, how often he meets students, how topics are assigned, how drafts are edited or how theses are examined.
- **Thesis acknowledgements**: eScholarship refused curl (CloudFront 403), and its search page came back empty through WebFetch. OpenAlex and Semantic Scholar searches were rate-limited in this run. Only Kungurtsev's PDF could be fetched by known item id, and it has no acknowledgements. Su 2019 (item 9wv1z3qw) is over WebFetch's 10 MB limit. The theses of Erway, Robinson, Wong, Ferry, M. Zhang, Runnoe, Guldemond, Huang and Z. Zhu, where acknowledgements would describe supervision, were **not read**. This is the best next lead.
- **No Festschrift, birthday workshop or tribute for Gill** turned up in one WebSearch. Gill spoke at the 2004 Stanford conference for the 60th birthdays of George, Saunders and Varah ("On unconstrained optimization and other Blasts from the Past...", program page). No slides were found.
- **SIAM oral histories** (history.siam.org): 403 to both curl and WebFetch. Any interview there with Wright, Murray, Saunders or Golub remains unread.
- **SOL article about Michael Saunders** (web.stanford.edu/group/SOL/saunders.html): 404.
- **The SNOPT GitHub organisation** (github.com/snopt): not accessible in this session, so contributor habits were not checked.
- **Stanford-era supervision** (Fenelon, Marxen): theses not read.
- **Ziyan Zhu (UCSD 2023)**: thesis not found. OpenAlex returned a 2022 Harvard thesis by a "Ziyan Zhu" on 2D materials, probably a different person. Unresolved.
- **A Google Scholar profile** for Gill (user id izPDLNYAAAAJ) surfaced in a WebSearch result. team.json has no Scholar id. The profile was not opened.
- **Walter Murray's current status** and any memorial writing: not checked.

## Sources

1. M. H. Wright, INFORMS History & Traditions interview, uploaded 2019-11-18, https://www.youtube.com/watch?v=2L5nQIvTohk. Local auto-caption transcript `../sources/talks/2019-informs-margaret-wright-interview-autocaptions.txt`, cited by line. Secondary for Gill: first-hand collaborator account, auto-captions.
2. P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, M. H. Wright, "George B. Dantzig and systems optimization", *Discrete Optimization* 5 (2008) 151–158, DOI 10.1016/j.disopt.2007.01.002, read at https://ccom.ucsd.edu/~peg/papers/gbd.pdf. Primary (collective).
3. P. E. Gill homepage, "In Person" (Personal.html), https://ccom.ucsd.edu/~peg/, fetched 2026-09-28. Primary.
4. P. E. Gill homepage, "Graduate Students" (Students.html), fetched 2026-09-28. Primary.
5. P. E. Gill homepage, "Post-Docs" (Postdocs.html), fetched 2026-09-28. Primary.
6. P. E. Gill homepage, "Selected Technical Reports" (Reports.html), fetched 2026-09-28. Primary.
7. P. E. Gill homepage, "Research Grants" (Grants.html), fetched 2026-09-28. Primary.
8. P. E. Gill, Math 271B course page (Winter 2022), http://www.ccom.ucsd.edu/~peg/math271b/index.html, fetched 2026-09-28. Primary.
9. UCSD Optimization Software site: home, SNOPT page (SNOPT 7.7 manual citation, CCoM 18-1), contact page, https://ccom.ucsd.edu/~optimizers/, fetched 2026-09-28. Primary.
10. Mathematics Genealogy Project: Philip Gill (id 6811), Walter Murray (39149), Roummel Marcia (60147), Renke Kuhlmann (248251), Kungurtsev (208004), Robinson (112624), Fenelon (89370), Marxen (89374), Forsgren (89385), Ponceleón (39233), Nash (89371), Prieto (89375), and the pages of the other 18 Gill students, https://www.mathgenealogy.org/, fetched 2026-09-28. Secondary.
11. V. Kungurtsev, *Second-Derivative Sequential Quadratic Programming Methods for Nonlinear Optimization*, PhD thesis, UCSD, 2013 (chair P. E. Gill), https://escholarship.org/uc/item/6081f5jc. Front matter and ch. 10 read. Primary (student practice).
12. P. E. Gill, D. P. Robinson, "A Globally Convergent Stabilized SQP Method", CCoM 13-03 (SIOPT 23 (2013) 1983–2010, DOI 10.1137/120882913), http://www.ccom.ucsd.edu/~peg/papers/pdsqp.pdf. Acknowledgements and references read. Primary.
13. J. B. Erway, P. E. Gill, J. D. Griffin, "Iterative Methods for Finding a Trust-Region Step", NA 07-2 (SIOPT 20 (2009) 1110–1131, DOI 10.1137/070708494), http://www.ccom.ucsd.edu/~peg/papers/trust.pdf. pp. 3 and 20 and the references read. Primary.
14. J. B. Erway, P. E. Gill, "An Interior-Point Subspace Minimization Method for the Trust-Region Step", NA 08-1, http://www.ccom.ucsd.edu/~peg/papers/trustBarrier.pdf. Funding and references read. Primary.
15. M. W. Ferry, P. E. Gill, E. Wong, M. Zhang, "A Class of Projected-Search Methods for Bound-Constrained Optimization", CCoM 20-07 (OMS 39 (2024) 459–488, DOI 10.1080/10556788.2023.2241769), http://www.ccom.ucsd.edu/~peg/papers/quasiwolfe.pdf. p. 22 and the references read. Primary.
16. M. W. Ferry, P. E. Gill, E. Wong, M. Zhang, "Supplementary Numerical Results for Projected-Search Methods for Bound-Constrained Optimization", CCoM 20-08, http://www.ccom.ucsd.edu/~peg/papers/quasi-results.pdf. Test description read. Primary.
17. P. E. Gill, M. Zhang, "A Projected-Search Interior Method for Nonlinear Optimization", CCoM 22-01 (COAP 88 (2024) 37–70, DOI 10.1007/s10589-023-00549-1), http://www.ccom.ucsd.edu/~peg/papers/pdprojReport.pdf. p. 27 read. Primary.
18. P. E. Gill, M. Zhang, "Numerical Results for a Projected-Search Interior-Point Method", CCoM 22-03 (June 2022, rev. Sept 2023), http://www.ccom.ucsd.edu/~peg/papers/pdproj-results.pdf. Introduction read. Primary.
19. P. E. Gill, J. H. Runnoe, "On Recent Developments in BFGS Methods for Unconstrained Optimization", CCoM 22-04, http://www.ccom.ucsd.edu/~peg/papers/bfgsdev.pdf. p. 1 funding line read. Primary.
20. P. E. Gill, E. Wong, "Sequential Quadratic Programming Methods", NA 10-3 (IMA Vol. 154, DOI 10.1007/978-1-4614-1927-3_6), http://www.ccom.ucsd.edu/~peg/papers/sqpReview.pdf. Acknowledgements (p. 37) and references read. Primary.
21. P. E. Gill, E. Wong, "Methods for Convex and General Quadratic Programming" (report version 13 July 2014; Math. Prog. Comp. 7 (2015) 71–112, DOI 10.1007/s12532-014-0075-x), http://www.ccom.ucsd.edu/~peg/papers/genqp.pdf. pp. 3 and 33 read. Primary.
22. P. E. Gill, M. A. Saunders, E. Wong, "On the Performance of SQP Methods for Nonlinear Optimization", CCoM 15-01 (Springer PROMS 2015, DOI 10.1007/978-3-319-23699-5_5), http://www.ccom.ucsd.edu/~peg/papers/mopta.pdf. Acknowledgements (p. 26) read. Primary.
23. J. J. Brust, P. E. Gill, "An LDL^T Quasi-Newton Trust-Region Method", CCoM 23-01 (SISC 46 (2024) A3330–A3351, DOI 10.1137/23M1623380), http://www.ccom.ucsd.edu/~peg/papers/trustRegionQN.pdf. Software-availability sentence read. Primary.
24. Stanford SOL website: Personnel page and 2004 conference pages (program and honorees), https://web.stanford.edu/group/SOL/home_personnel.html and https://web.stanford.edu/group/SOL/svg60/, fetched 2026-09-28. The honorees text, "30 years of collaboration with Philip Gill and Walter Murray -- most recently on SNOPT. (One of those decades included Margaret Wright as part of the famous Gang of Four at SOL.)", was written by the organizers. Secondary.
25. J. B. Erway, homepage and publications page, https://users.wfu.edu/erwayjb/, fetched 2026-09-28. Secondary.
26. R. F. Marcia, "Collaborative Research: Trust-Search Methods for Inverse Problems in Imaging" page, http://faculty.ucmerced.edu/rmarcia/NSF_TrustSearch.html, fetched 2026-09-28. Secondary.
27. J. Griffin, SAS Blogs author page (bio), https://blogs.sas.com/content/author/joshgriffin/, fetched 2026-09-28. Secondary.
28. UCSD CCoM site (directors listed: Bank, Gill, Holst), https://ccom.ucsd.edu/people/alumni.php, fetched 2026-09-28. Secondary.
29. Crossref metadata records used to verify every DOI above, plus DOIs 10.1137/S0895479894270658, 10.1137/060650210, 10.1007/s10107-015-0966-2, 10.1137/S1052623400307950, 10.1137/S1052623497319973, 10.1007/s10107-003-0486-3, 10.1007/978-3-0348-8802-8_21, 10.1007/978-3-642-55508-4_13, 10.1137/08072440X, 10.1093/imanum/drw004, 10.1007/s10107-016-1066-7, 10.1137/19M1247425, 10.1007/BF02592025, 10.1007/s10589-010-9339-1, 10.1007/s10589-016-9868-3, 10.1016/j.laa.2016.11.003, 10.1109/TIP.2011.2158229, 10.1016/j.physleta.2007.12.051, 10.1093/acprof:oso/9780195393798.003.0008, 10.2172/1177970; https://api.crossref.org, queried 2026-09-28. Secondary (bibliographic).
30. Wikipedia, "Michael Saunders (academic)", raw wikitext, fetched 2026-09-28. Secondary; background only, not cited for any claim above.
31. WebSearch results (2 queries: thesis acknowledgements; Gill tribute or birthday workshop), 2026-09-28. Secondary; led to Gill's Google Scholar profile id, no tribute found.
