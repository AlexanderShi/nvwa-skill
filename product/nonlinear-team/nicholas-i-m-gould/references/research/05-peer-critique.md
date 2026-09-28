# 05 · Peer critique: where others have challenged Nicholas I. M. Gould's work, and how he answered

- **Researcher**: Nicholas Ian Mark Gould (Nick Gould), STFC Rutherford Appleton Laboratory (RAL); visiting professor at Oxford and Edinburgh. Living.
- **Dimension**: research agent 05 of 06, peer critique (nuwa research-craft Phase 1, framework §二 agent 5). The subject is blind spots, limits of applicability and judgements shown to be wrong. For each critique I record the critic, the source, and whether and how it was answered.
- **Research date**: 2026-09-28.
- **Sources consulted**: 54 (C01–C54 under Sources).
  - 17 are primary: Gould's own texts, co-authored texts and code.
  - 37 are secondary: critics, reviewers, benchmarkers, citation-context snippets and this team's notes 01–04.
  - Coverage per source: 31 were read in full or in the passages cited; 12 were read only as an abstract or a Semantic Scholar citation-context snippet; 11 are metadata only, not read, or blocked. The Sources list marks which is which.
  - WebSearch calls used: 2 of 2.
- **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` hold only `.gitkeep`, so there was **no user-supplied material**. `private/` was not opened. No talk transcript was found, so nothing was saved under `sources/talks/`.
- **How the evidence was obtained.**
  - *Quotations*: full texts from arXiv, author-posted PDFs and Gould's public RAL page, extracted locally with pypdf. Page numbers are PDF pages unless a journal page is given.
  - *Citations*: the Semantic Scholar Graph API (citation contexts of ten Gould works), searched for critical wording.
  - *Identifiers*: Crossref (DOIs, abstracts), arXiv abstract pages, and zbMATH Open (public reviews).
  - *Benchmarks*: Hans Mittelmann's public benchmark pages.
  - *Repositories*: the GALAHAD git clone made by agent 03 (HEAD afa13a5e, 2026-09-26), read-only, and GitHub issue pages.
  - Every DOI and arXiv id below was resolved in this run.
- **Citation-context snippets.** Some critiques come only from Semantic Scholar citation-context snippets. Semantic Scholar extracts these automatically from the citing paper's full text, and I did not read that full text. These items are marked **(S2 snippet)**. Their wording is Semantic Scholar's extraction and should be checked against the paper before it is quoted elsewhere.

**Tags.**
- **[stated]**: what Gould (alone or with co-authors) wrote.
- **[practice]**: what the record shows was done (papers, code, dates).
- **[observed]**: what a critic, reviewer or benchmarker said or measured.
- **[inferred]**: my reading, with no direct source.

Each item is also marked **P** (primary: Gould's own text or record) or **S** (secondary: somebody else's).

**Caution on authorship.** Most critiques below target co-authored work: Conn–Gould–Toint (CGT) for LANCELOT, SR1 and trust regions, and Cartis–Gould–Toint for the complexity programme. A critique of "CGT" is therefore not a critique of Gould alone. Only the projection-methods exchange (§1) involves sole-authored papers on his side.

---

## 0. Map of the critiques (era and resource context)

| Years | Target | Critic(s) | Form | Answered? | § |
|---|---|---|---|---|---|
| 1981 (reported 1998) | Modified-factorization trust-region norms | R. Fletcher (NATO ARI discussion) | oral comment, reported by Gould | Yes: accepted as "a possible defect"; the promised fix was not found | 5.4 |
| 1990–1996 | SR1 convergence theory (CGT 1991): the "uniform linear independence" assumption | Khalfan, Byrd, Schnabel | competing analysis + experiments | No reply found | 3.1 |
| 1999–2002 | LANCELOT A performance | Dolan & Moré (COPS), Benson–Shanno–Vanderbei, Chin (Dundee), makers of SNOPT, LOQO, KNITRO, filterSQP | competitor benchmarks | Yes, conceded in print (2003); LANCELOT B shelved | 2.1 |
| 2004 | LANCELOT on complementarity constraints | Fletcher & Leyffer (reporting earlier observations) | remark in a paper | none found | 2.2 |
| 2007–2008 | LANCELOT-type AL convergence theory (LICQ) | Andreani, Birgin, Martínez, Schuverdt | stronger theory under CPLD | none found | 3.2 |
| 2009–2012 | "How good are projection methods…?" (2008) | Censor, Chen, Combettes, Davidi, Herman | published rebuttal paper | **Yes: the only formal comment-and-reply exchange found** | 1 |
| 2011 | Trust-funnel convergence proof | D. P. Robinson (a collaborator) | error found in joint work | Yes: erratum (cross-ref 01 §1.7) | 3.3 |
| 2014–2016 | Constrained-complexity Lemma 3.5 (2014) | not stated; discussed with Birgin, Gardenghi, Martínez, Santos | error | Yes: corrigendum, "the result of the lemma is false" | 3.4 |
| 2014–2021 | Complexity programme: trust region vs ARC, worst-case examples, lower bounds | Curtis–Robinson–Samadi; Curtis–Robinson; Carmon–Duchi–Hinder–Sidford | competing algorithms and analyses | Partly: TRACE implemented in GALAHAD (still `forthcoming`); no printed reply found | 4 |
| 2016–2021 | GLTR: hard case, stopping rules, versus eigenvalue methods | Amaioua–Audet–Conn–Le Digabel; Kolvenbach–Lass–Ulbrich; Zhang–Shen–Li; Zhou–Bai–Li; Jia–Wang | remarks and analyses | Hard case: yes, in 2025–26 (dismissed as contrived). Stopping rules and eigenvalue methods: no reply found | 5 |
| 2018–2026 | GALAHAD CQP and NLP solvers in public benchmarks | H. Mittelmann | benchmark tables | none found; the benchmark still runs "Galahad-3" | 2.3 |
| 2020–2026 | CUTEst: problem sizes, representativeness, fixed sparsity, wrong sparsity patterns | Birgin & Martínez; Liu–Fredriksson–Markidis; Audet et al.; J. Haffner (GitHub) | remarks and a bug report | none found; the 2026 issue is open with no visible reply | 6 |
| 2021–2024 | GALAHAD ARC implementation | Dussault, Migot, Orban (Orban co-maintains GALAHAD and CUTEst) | competing implementation and benchmark | No printed reply; the 2025 TREK paper does not cite it | 4.4 |
| 2000 → 2003 | His own prediction that SQP would win at large scale | Gould himself, then others' benchmarks | self-revision | Revised in 2003 | 7 |

[inferred] **Context.**
- The harshest external evidence against his codes came in 1999–2002. Better-resourced industrial and academic groups were then releasing NLP solvers: KNITRO, LOQO, SNOPT, filterSQP and later IPOPT. The CGT team was three people on two continents, working in Fortran 90 on a national-lab budget (01 §2; 03 §0).
- The complexity critiques (2014–2021) come from inside his collaboration network. Curtis and Robinson are co-authors of Gould, Orban co-maintains his software, and Conn is his long-time co-author. Most "critique" of Gould is therefore friendly competition rather than hostile rebuttal.

---

## 1. The one formal published exchange: projection methods (2008–2012)

### 1.1 The claim criticised

Gould, "How good are projection methods for convex feasibility problems?", *Comput. Optim. Appl.* 40 (2008) 1–12, 10.1007/s10589-007-9073-5 (sole author).

The abstract, as quoted by his critics [C03 arXiv v1 p.2, S, verbatim]: "Unfortunately, particularly given the large literature which might make one think otherwise, numerical tests indicate that in general none of the variants [of projection methods for solving convex feasibility problems] considered are especially effective or competitive with more sophisticated alternatives." [stated, P, quoted via S; the bracketed insertion is the critics'.]

### 1.2 The critique

Censor, Chen, Combettes, Davidi & Herman, "On the effectiveness of projection methods for convex feasibility problems with linear inequality constraints", *Comput. Optim. Appl.* 51 (2012) 1065–1088, 10.1007/s10589-011-9401-7; arXiv 0912.4367 (v1, 22 Dec 2009, read) [C03, observed, S]. Four charges, verbatim from arXiv v1:

1. **Over-generalisation from a narrow test set.** "results based on the geometrically simple 2-set problems of [48] are vastly insufficient to draw general conclusions." (p.2)
2. **Straw-man variants.** "the experiments reported in [48] use suboptimal versions of projection methods, which further questions the justification of the above-quoted general conclusion as to their effectiveness." (p.2)
   - Their own experiment uses extrapolated methods (EAPM, EPPM). "EAPM is clearly the best method: on the average, it is about 60 times faster than PPM, 30 times faster than POCS, and it achieves full convergence in just 7 iterations." (p.5)
   - They conclude that Gould's results "correspond to a suboptimal implementation of projection methods and are not representative of their performance, since drastic improvements can be achieved by appropriate relaxations." (p.6)
3. **Random versus real problems.** Against Gould's claim that random problems are unrepresentative: "Let us observe that random matrices do show up in many real-life problems" (p.5).
4. **Scale.** They exhibit an image-representation problem "over an order of magnitude larger" than Gould's largest Netlib case (p.6). Their conclusion: "correctly implemented projection methods are very efficient for convex feasibility problems with linear inequality constraints, especially for those that are large, sparse, and originate from real-life applications." (p.14)

### 1.3 Gould's answer

Gould, "How good are extrapolated bi-projection methods for linear feasibility problems?", *Comput. Optim. Appl.* 51 (2012) 1089–1095, 10.1007/s10589-011-9414-2 (sole author; read in full) [C02, stated + practice, P]. What he did:

- **Named the charge exactly.** "Recently Censor et al. [2] have challenged these conclusions. Most particularly, the authors objected that [7] use "suboptimal" projection methods in the comparisons made." (p.1090)
- **Reran the critics' methods in his own code, with their best parameter.** "We modified the GALAHAD fortran 2003 package LCF … to include additionally the EAPM and EPPM methods … We used the value ρ = 1.8 that appears to work best in the experiments in [1]" (p.1092).
- **Conceded the specific point in the first finding.** "Figure 1 confirms that the authors of [2] are correct in saying that EAPM and EPPM are better than those discussed in [7]. Indeed since the best bi-projection methods tested in [7] are heuristic, whereas EAPM and EPPM have a convincing convergence theory, this is a satisfactory outcome." (p.1092)
- **Kept the general conclusion on his test set, with numbers.**
  - "there is a significant failure rate (44 cases out 118 problems tested for EAPM and 43 case for EPPM)" (p.1093).
  - "the interior point code was fastest in 71% of the cases." (p.1094)
  - The abstract: "The interior-point method succeeded on all examples, but the best bi-projection method considered here failed to solve 37% of the problems within reasonable CPU time or iteration thresholds."
- **Reproduced the critics' random experiments as far as his tools allowed, and admitted a tool weakness.** "we didn't have their pseudo-random number generator … we had to be content with systems of order 700 by 300 since the factorization code we used was (we discovered) poorly designed for dense problems." (p.1093)
- **Partial concession, partial rebuttal.** "So while we certainly accept that our earlier implemented methods are "suboptimal", the authors' suggestion … that they are not representative of the best methods is, we would argue, debatable, since the differences are relatively minor. Moreover, as the average counts on these random examples are considerably lower than most of the real-life examples from the Netlib set, this suggests that random examples may not reflect practical experience in many cases." (p.1094)
- **Conceded the scope limit and asked for software.** "Of course, other projection methods may well be better than the ones considered here … We would welcome the development of generally applicable software to implement such ideas." (p.1094)
- **Published at an editor's urging.** "The authors is grateful to Bill Hager for encouraging him to publish these follow-up results" [sic] (p.1094).

### 1.4 How a third party read the outcome

Bauschke & Koch, "Projection methods: Swiss army knives for solving feasibility and best approximation problems with halfspaces", arXiv 1301.4506 (v1 read); *Contemporary Mathematics* 636 (2015) 1–40, 10.1090/conm/636/12726 [C04, observed, S].

They cite both sides as settled facts: "Not surprisingly, they are not always competitive with special-purpose solvers [37]; however, when projection methods succeed (see [16] for a compelling set of examples), then they have a variety of very attractive features" (p.13). Here [37] is Gould 2008 and [16] is Censor et al.

[inferred] The field kept both halves. Gould's evidence holds for general-purpose use on diverse LP-derived sets. The critics' evidence holds for large, structured, application-specific problems.

### 1.5 What the exchange shows (limits of applicability)

- [observed, S] **Blind spot named by critics.** A strong general title and abstract ("in general none … competitive") rested on one problem formulation (two sets: an affine space and a box) and one test family (Netlib/CUTEr LPs). The critics attacked the generalisation, not the measurements.
- [practice, P] **His response pattern.** Rerun the critics' methods in the same code; concede the variant point; restate the conclusion with its scope; ask for software. This matches the stated rule J5 in note 02 exactly.
- [inferred] **Unresolved.** Gould never tested on the critics' application class (large sparse imaging and tomography problems), and the critics never tested on Netlib. Each side's conclusion is scoped to its own test set, and neither ran the other's.

---

## 2. Competitors' benchmarks against his solvers

### 2.1 LANCELOT A, 1999–2002: the benchmarks that ended LANCELOT B

**The critics' evidence.** GOT 2003 names the evidence behind the decision [stated, P, C05; GALAHAD paper, *ACM TOMS* 29 (2003) 353–372, 10.1145/962437.962438]: "a number of our colleagues had started to release the results of comparative tests of their new codes — for instance SNOPT [Gill et al. 2002], LOQO [Vanderbei and Shanno 1999], KNITRO [Byrd et al. 1999], and FilterSQP [Fletcher and Leyffer 2002]— against LANCELOT A, and the results made frankly rather depressing reading for us [Dolan and Moré 2000, Benson et al. 2001, and Chin 2001]". The three benchmark sources it cites:

- **Dolan & Moré** [C06, observed, S]. Preprint ANL/MCS-P861-1200, arXiv cs/0102001 (read); published as *Math. Program.* 91 (2002) 201–213, 10.1007/s101070100263.
  - In the COPS case study with LANCELOT, MINOS, SNOPT and LOQO, the text names LOQO as having "the most wins" and says SNOPT "captures our attention with its ability to solve over 90% of this COPS subset" (preprint p.8). It adds: "Even extending τ to 100, we fail to capture the complete performance data for LANCELOT and LOQO." (preprint p.10)
  - On the full COPS set, "LOQO dominates all other solvers" (preprint p.11).
  - The authors add a caveat on their own method: "A performance profile reflects the performance only on the data being used" (preprint p.12).
  - [observed] LANCELOT is never the leader in the text. [inferred] LANCELOT's poor COPS showing is visible only in the figures; the text does not single it out.
- **Dolan & Moré, "Benchmarking optimization software with COPS"**, ANL/MCS-TM-246 (2000; OSTI 10.2172/775270) [C07], and the later **COPS 3.0** report with Munson (2004; OSTI 10.2172/834714) [C08]. **Not read**: OSTI and Argonne returned a bot challenge.
- **Benson, Shanno & Vanderbei**, "A comparative study of large-scale nonlinear optimization algorithms", TR ORFE-01-04 (2001), published in *High Performance Algorithms and Software for Nonlinear Optimization*, Kluwer (2003) 95–127, 10.1007/978-1-4613-0241-4_5 [C09]. **Not read**: no open copy was found.
- **C. M. Chin**, "Numerical results of SLPSQP, filterSQP and LANCELOT on selected CUTE test problems", Numerical Analysis Report NA/203, University of Dundee (2001) [C10]. Known only from the reference list of C05; **not read**.

**The answer** [stated, P] (cross-ref 01 §2.D, 02 F1, 03 §1.2):
- The concession in print: "LANCELOT often, but far from always, being significantly outperformed … the limit of what might be achieved by augmented Lagrangian methods such as LANCELOT A had probably been reached. Reluctantly, we abandoned any plans to release LANCELOT B at that time" (C05, author PDF p.2).
- LANCELOT B was later released inside GALAHAD. It was re-engineered with steering in 2014–16, with steering off by default (03 C5).
- Contradiction C8 in note 03 records that he kept investing in augmented-Lagrangian solvers.

### 2.2 LANCELOT on complementarity constraints

Fletcher & Leyffer, "Solving mathematical programs with complementarity constraints as nonlinear programs", *Optim. Methods Softw.* 19 (2004) 15–40, 10.1080/10556780410001654241 [C11, observed, S, **S2 snippet**]: "[11] and Ferris and Pang [1] attribute certain failures of lancelot for LUBRIF to the fact that the problem contains a complementarity constraint."

- [inferred] This is a limit of applicability: degenerate, MPCC-type constraints, where no constraint qualification holds.
- Reply: none found.

### 2.3 GALAHAD in today's public benchmarks (Mittelmann)

- **Convex QP (CQP).** Mittelmann, "Benchmark of noncommercial QP solvers", 29 Jun 2026, https://plato.asu.edu/ftp/qpbench.html [C48, observed, S]. It runs "Galahad-3: … (QPS input, CQP solver)" on the Maros–Mészáros set against BPMPD, IPOPT, OOQP, CLP, OSQP, HiGHS and cuOpt.
  - Successes, CQP against the leader: 45/46 against BPMPD's 46 (BRUNEL); 76/76, tied with BPMPD, IPOPT and OOQP (CUTE); 14/16 against BPMPD's 16 (MISC).
  - Sample times (s):
    - CQP fails ("f") on BOYD1 and BOYD2;
    - CVXQP3_L takes 246 s, against 10 (BPMPD), 7 (IPOPT), 2 (HiGHS) and 4 (cuOpt);
    - EXDATA takes 39 s, against 1–10 for most others.
  - The same CQP rows appeared in the 12 June 2018 version of the table (ISMP 2018 slides, pp.13–14 [C49]).
  - [inferred] Robustness is near the top among free codes. Speed on some large or dense-Hessian instances is poor. The benchmark still runs GALAHAD **version 3**, while GALAHAD is at 5.x, so current code may do better. That is not tested here.
- **General NLP.** Mittelmann, "AMPL-NLP Benchmark", 9 Sep 2026, https://plato.asu.edu/ftp/ampl-nlp.html [C50, observed, S]. It runs IPOPT, KNITRO, SNOPT, CONOPT, WORHP, FMINCON, COPT, UNO and POUNCE. **No Gould solver (LANCELOT, or any GALAHAD NLP package) is included.**
  - [inferred] Nothing in the page says why. It fits note 03 §1.2: no general-constrained NLP solver after LANCELOT reached GALAHAD's `src/`.
- **Reply**: none found. The 2013 CQP paper's own remark that "insufficient numerical evidence … is a gross oversight" (03 C1) sits beside the fact that the only external CQP comparison found is Mittelmann's.

---

## 3. Theoretical assumptions challenged

### 3.1 SR1: the "uniform linear independence" assumption (CGT 1991)

- **Target.** Conn, Gould & Toint, "Convergence of quasi-Newton matrices generated by the symmetric rank one update", *Math. Program.* 50 (1991) 177–195, 10.1007/BF01594934 [C14, metadata only; the full text is not read].
  - That this paper assumes uniformly linearly independent steps is attested by later citers. Wu, Huang & Wang (arXiv 2306.04111, S2 snippet): "(C5) has been rigorously proved by Conn et al. (1991), assuming that sequence … is uniformly linearly independent". Andrei (2022, S2 snippet) agrees [observed, S].
- **Critique 1.** Khalfan, Byrd & Schnabel, "A theoretical and experimental study of the symmetric rank-one update", *SIAM J. Optim.* 3 (1993) 1–24, 10.1137/0803001 (abstract read via Crossref) [C12, observed, S]: "the sequences of steps produced by the SR1 do not usually seem to have the "uniform linear independence" property that is assumed in recent convergence analysis. This paper presents a new analysis that shows that the SR1 method with a line search is (n+1)-step q-superlinearly convergent without the assumption of linearly independent iterates."
- **Critique 2.** Byrd, Khalfan & Schnabel, "Analysis of a symmetric rank-one trust region method", *SIAM J. Optim.* 6 (1996) 1025–1039, 10.1137/S1052623493252985 (abstract read) [C13, observed, S]: "The analysis makes neither of the assumptions of uniform linear independence of the iterates nor positive definiteness of the Hessian approximations that have been made in other recent analyses of SR1 methods."
- **The critique lives on.** Ramzi et al., "SHINE…", arXiv 2106.00553 (v4 read, p.5) [C15, observed, S]: "While ULI is often used to prove convergence results for qN matrices, e.g. in (Conn et al., 1991; …), it is a strong assumption whose satisfaction in practice is debatable, cf., e.g., (Fayez Khalfan et al., 1993)."
- **Answered?** No reply by Gould or CGT was found. *Trust-Region Methods* (2000), where a reply would most likely appear, was **not read**. Note 01 records that CGT's 1988 experiments recommended SR1 over BFGS inside trust regions [stated, P]. The empirical preference survived; the 1991 theorem's key assumption was judged unrealistic by the Byrd–Schnabel school.

### 3.2 Augmented-Lagrangian convergence under linear independence (CGT 1991, LANCELOT)

- **Target.** Conn, Gould & Toint, "A globally convergent augmented Lagrangian algorithm for optimization with general constraints and simple bounds", *SIAM J. Numer. Anal.* 28 (1991) 545–572, 10.1137/0728030 [C20, metadata].
- **Critique.** Andreani, Birgin, Martínez & Schuverdt, "On augmented Lagrangian methods with general lower-level constraints", *SIAM J. Optim.* 18 (2007) 1286–1309, 10.1137/060654797 [C16, observed, S; Crossref abstract read, passage from **S2 snippet**]: "Global convergence results that use the CPLD constraint qualification are stronger than previous results for more specific problems: In particular, Conn, Gould, and Toint [21] and Conn et al. [20] proved global convergence of augmented Lagrangian methods for equality constraints and linear constraints, assuming linear independence of all the gradients of active constraints at the limit points."
  - The companion paper, *Math. Program.* 111 (2008) 5–32, 10.1007/s10107-006-0077-1 [C17, **S2 snippet**]: "The AS3 condition of [12], when applied only to feasible points, is the classical LICQ assumption".
- **Design critique from the same school.** Birgin & Martínez, "Complexity and performance of an augmented Lagrangian algorithm", *Optim. Methods Softw.* 35 (2020) 885–920, 10.1080/10556788.2020.1746962; arXiv 1907.02401 (v1 read) [C18, observed, S].
  - "Conn, Gould, and Toint [27] produced the celebrated package Lancelot, that solves constrained optimization problems using Augmented Lagrangians in which the constraints are defined by equalities and bounds." (p.1)
  - "Differently from Lancelot, in Algencan … the Augmented Lagrangian is defined not only with respect to equality constraints but also with respect to inequalities." (p.2)
  - [inferred] The rival school's position: slack variables plus bounds (LANCELOT) versus direct treatment of inequalities with safeguarded multipliers (ALGENCAN).
- **Echo in a 2025 QP solver.** Bambade et al., "ProxQP…", *IEEE Trans. Robotics* (2025), 10.1109/tro.2025.3577107 [C19, **S2 snippet**]: "We managed to get rid of most of the strong assumptions required for ensuring global convergence of BCL [27]." Semantic Scholar attributes this context to a citation of CGT 1991.
- **Answered?** No reply found.

### 3.3 Trust funnel (Gould & Toint 2010): an error found by a collaborator, and a structural limit noted by others

- **Error.** Found "during work with D. Robinson", corrected by an erratum (*Math. Program.* 131 (2012) 403–404, 10.1007/s10107-011-0491-x) [C21, stated, P; details in 01 §1.7 and 03 §4.4]. The S2 snippet of the erratum adds: "The convergence proof taking this distinction into account is therefore significantly more involved than the proof of [2], and cannot be presented in the form of a few corrections in the original text."
- **Structural limit.** X. Zhu, "On a globally convergent trust region algorithm with infeasibility control for equality constrained optimization", *J. Appl. Math. Comput.* 50 (2015) 275–298, 10.1007/s12190-015-0870-1 [C22, observed, S, **S2 snippet**]: "a double trust regions strategy similar to Gould and Toint's work [12] is used for step computations and the ratio of normal and tangent trust region radii is out of control in theory though in practice it is not the case."
- **Endorsement from the rival-but-friendly school.** Curtis, Robinson & Samadi, "Complexity analysis of a trust funnel algorithm for equality constrained optimization", *SIAM J. Optim.* 28 (2018) 1533–1563, 10.1137/16M1108650; arXiv 1707.00337 (v1 read, p.27) [C52, observed, S]: "following the current state-of-the-art, we implemented a trust funnel method based on that proposed in [21]". [21] is Gould & Toint 2010.
- **Answered?** The erratum, and the 2017 interior-point trust funnel. The FUNNEL code went to `oblivion` (03 §1.2). No reply to Zhu was found.

### 3.4 Constrained complexity: a false lemma

Cartis, Gould & Toint, "Corrigendum: On the complexity of finding first-order critical points in constrained nonlinear optimization", *Math. Program.* 161 (2017) 611–626, 10.1007/s10107-016-1016-4 (pp.1–2 and acknowledgments read) [C23, stated, P].

- The admission: "the given proof of [4, Lem.3.5] invokes [2, Thm. 3.1] incorrectly, and indeed the result of the lemma is false. Furthermore, the claimed generalization to inequality constraints [4, Sect. 4] fails to account for complementary slackness, and is thus incomplete."
- Who found it is **not stated**. The acknowledgments thank members of the rival São Paulo/Campinas complexity group: "The authors wish to thank Ernesto Birgin, John Gardenghi, Jose-Mario Martinez and [Sandra Santos]".
- How it was answered: the bound was restored for "a different, scaled measure of first-order criticality" (abstract).
- [inferred] The claim was repaired by redefining what is measured, not withdrawn.

---

## 4. The complexity programme (Cartis–Gould–Toint) under critique

### 4.1 "Trust regions are O(ε⁻²), ARC is O(ε⁻³ᐟ²)": a framing overturned

Curtis, Robinson & Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε⁻³ᐟ²) for nonconvex optimization", *Math. Program.* 162 (2017) 1–32, 10.1007/s10107-016-1026-2 (author copy read; PDF pages = journal pages) [C24, observed, S].

- **The framing it takes on.** "the distinguishing feature of arc and other cubic algorithms is that … the stationarity measure tolerance (1.2) is guaranteed to hold after at most O(ϵ−3/2) iterations. This is in contrast to a traditional trust region strategy, for which one can only guarantee that such a tolerance is met after O(ϵ−2) iterations [6]." (p.3)
- **The critique of ARC's design.** "the arc algorithm only achieves its worst-case complexity bounds by imposing a uniform lower bound on the cubic regularization coefficient, which implies that the arc algorithm never computes Newton steps, even in a neighborhood of a strict local minimizer." (p.11). Also: "in contrast to arc in which the cubic regularization strategy is never "off"" (p.3).
- **The tone is collegial.** "The authors are extremely grateful to Coralia Cartis, Nicholas I. M. Gould, and Philippe L. Toint for enlightening discussions about the arc algorithm and its theoretical properties that were inspirational for the algorithm proposed in this paper." (p.30)
- **How Gould answered, in practice** [practice, P, C32]. He implemented TRACE in GALAHAD. The header reads: "TRACE, a trust-region algorithm with contraction and expansion for unconstrained optimization, due to Frank E. Curtis (Leheigh U.) [sic], Daniel P. Robinson (Johns Hopkins U.) and Mohammadreza Samadi (Leheigh U.)", "originally released GALAHAD Version 2.6. October 23rd 2014".
  - It is still in `src/forthcoming/` at HEAD (2026-09-26), 12 years later.
  - [inferred] He treated the rival algorithm as worth coding next to his own. It never reached recommended status.
- **How Gould answered, in print** [stated, P]. Cartis–Gould–Toint's ICM 2018 paper, "Worst-case evaluation complexity and optimality of second-order methods for nonconvex smooth optimization" (*Proc. ICM 2018*, Rio de Janeiro, vol. 3, 3697–3738; header and abstract read, C28), "consider a new general class of inexact second-order algorithms for unconstrained optimization that includes regularization and trust-region variations of Newton method as well as of their linesearch variants" (abstract). [inferred] It absorbed trust-region variants into the optimality framework rather than disputing TRACE. The body was not read in full.

### 4.2 "The worst-case examples are pedagogical"

Curtis & Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", *Math. Program.* 187 (2021) 579–615, 10.1007/s10107-020-01492-3; arXiv 1802.01062 (v1 read) [C25, observed, S].

- "in [4, 7], the authors show that the worst-case complexity guarantees for various well-known methods are tight due to certain objective functions that one might argue are pedogogical [sic] and distinct from those encountered in regular practice." (p.3). Here [4] is CGT 2010 on steepest descent and Newton, and [7] is CGT's "Optimal Newton-type methods".
- The abstract: contemporary worst-case analyses "arguably lead[] to conservative characterizations based on certain objectives rather than on ones that are typically encountered in practice." (S2/arXiv abstract; wording differs slightly between versions.)

**CGT's stated position, which predates this critique** [stated, P, C27]. Cartis, Gould & Toint, "How much patience do you have? A worst-case perspective on smooth nonconvex optimization", *Optima* 88 (2012):

- "Despite being the best-known bound for steepest descent methods and even considering the well-known inefficient practical behaviour of gradient-type methods on ill-conditioned problems, (1) may still seem unnecessarily pessimistic. We illustrate however that this bound is essentially sharp as a function of the accuracy ϵ." (p.3)
- "Despite its pessimistic outlook, the worst-case perspective is nonetheless reassuring as it allows us to know what to expect in the worst-case from methods we might use. Clearly, the view of the optimization world we most commonly encounter involves the typical-case performance of methods, which is usually far better than the bounds and behaviour discussed here." (p.9)

[inferred] The two sides agree on the facts: the bounds are tight, and they are pessimistic for typical problems. They disagree on the value. CGT treat sharp worst-case bounds as reassurance. Curtis and Robinson treat them as a reason to change the measure.

### 4.3 CGT's lower bounds hold only within a class

Carmon, Duchi, Hinder & Sidford, "Lower bounds for finding stationary points I", *Math. Program.* 184 (2020) 71–120, 10.1007/s10107-019-01406-y; arXiv 1710.11606 (v1 read) [C26, observed, S]:

"Cartis et al. [16, 17] show that for important but specific algorithms, namely gradient descent and cubic regularization of Newton's method, the respective performance guarantees are tight in the worst case. They also extend these results to certain structured classes of methods [18, 19]. We provide the first algorithm-independent lower bounds for finding finding [sic] stationary points in the unconstrained setting." (p.2)

[observed] Their abstract also concludes that "cubic-regularized Newton's method … [is] worst-case optimal within [its] natural function class". [inferred] This is a limit on how far CGT's lower bounds reach, and at the same time a confirmation of ARC's optimality.

### 4.4 ARC as software: a collaborator's implementation beats GALAHAD's

Dussault, Migot & Orban, "Scalable adaptive cubic regularization methods", *Math. Program.* 207 (2024) 191–225, 10.1007/s10107-023-02007-6; arXiv 2103.16659 [C31, observed, S].

- **The published abstract** (served by Semantic Scholar): "report numerical experience that confirms that our implementation of ARCqK outperforms a classic Steihaug-Toint trust-region method, and the ARC method of the GALAHAD library. The latter solves the subproblem in nested Krylov subspaces by a Lanczos-based method, which requires the storage of a dense matrix that can be comparable to or larger than the two dense arrays required by our approach if the problem is large or requires many Lanczos iterations."
- **The first version was different.** The arXiv v1 abstract (30 Mar 2021, authors Dussault and Orban only) compares only with "a classic Steihaug-Toint trust region method". The GALAHAD comparison was added in revision. The reason is not known.
- **The critic's position.** D. Orban is co-author of GALAHAD (2003) and CUTEr/CUTEst, and co-maintains them (03 §7).
- **The code at HEAD** [practice, P, C32]. GALAHAD's `arc.F90` still defaults to the iterative subproblem solver: `LOGICAL :: subproblem_direct = .FALSE.`, which uses GLRT. Neither ARC nor TRU references the new TREK/NREK solvers. The TREK paper says they "will be rolled out … in due course" (03 §5).
  - The TREK paper (Al Daas & Gould, arXiv 2511.11135 v3) does not cite Dussault–Migot–Orban.
- **Answered?** Not in print, as far as found. [inferred] TREK (one factorization plus an extended Krylov basis) answers the storage and scalability concern in substance, but not by name.
- **An unmet plan.** Optima 2012 promised: "Work is on-going on the development of sophisticated ARC implementations and the necessary comparison with state of the art trust-regions." (p.9) [stated, P]. No such comparison paper was found in the publication list (01).

### 4.5 A public review of the complexity book

zbMATH review of Cartis, Gould & Toint, *Evaluation Complexity of Algorithms for Nonconvex Optimization* (MOS-SIAM 30, 2022), 10.1137/1.9781611976991, by Julien Ugon (Zbl 1520.90002) [C29, observed, S]:

- Mostly descriptive.
- One evaluative remark: "A significant part of the book is devoted to trust region methods, which isn't surprising given the background of the authors, but the discussion isn't limited to this algorithms and many results are presented for other approaches."

---

## 5. Trust-region subproblem solvers (GLTR and successors)

### 5.1 The hard case

- **Amaioua, Audet, Conn & Le Digabel.** *Eur. J. Oper. Res.* 268 (2018) 13–24, 10.1016/j.ejor.2017.10.058 [C37, observed, S, **S2 snippet**, from the 2016 preprint version]: "However, GLTR could not handle hard cases (see chapter 7 in [17]) of the trust-region subproblems." Conn is a co-author of both GLTR's parent book and this critique.
- **Kolvenbach, Lass & Ulbrich.** *Optim. Eng.* 19 (2018) 697–731, 10.1007/s11081-018-9388-3 [C38, **S2 snippet**]: "Several merely heuristic algorithms exist that do not guarantee (approximate) optimality, for instance the Steihaug–Toint method, the generalized Lanczos trust-region method (GLTR) and the sequential subspace method (SSM)".
- **Zhou, Bai & Li.** "Linear constrained Rayleigh quotient optimization: theory and algorithms", arXiv 1911.02770 (v1 read, p.23); *CSIAM Trans. Appl. Math.* 2 (2021) 195–262, 10.4208/csiam-am.2021.nla.01 [C35, observed, S]: "It is known that the generalized Lanczos method does not work for TRS (2.42) in the hard case [43, Theorem 4.6]. A restarting strategy was proposed to overcome the difficulty, but it was commented that the strategy computationally is very expensive for large scale problems [16, Theorem 5.8]." Here [43] is Zhang–Shen–Li 2017 and [16] is GLTR 1999.
- **Gould's stance, 2025–26** [stated, P, C39]. Al Daas & Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems", arXiv 2511.11135 (v3, p.14): "No Krylov method based on A and b (extended or otherwise) will see the eigenspace E1 in the hard case in exact arithmetic, although rounding errors can gradually introduce it. Since we have never observed the hard case in practice for anything other than contrived examples, our only precaution is to add a tiny (pseudo-random) perturbation to b if requested."
- [inferred] **An explicit, practice-based dismissal of a theory-driven objection.** The earlier direct solver TRS (Gould, Robinson & Thorne, *Math. Program. Comput.* 2 (2010), 10.1007/s12532-010-0011-7; see 03) does treat the hard case algorithmically: its §3.3.6 is "Fast convergence in the hard case", read in agent 03's full text.

### 5.2 Stopping rules

Zhang, Shen & Li, "On the generalized Lanczos trust-region method", *SIAM J. Optim.* 27 (2017) 2110–2142, 10.1137/16M1095056 (abstract read) [C34, observed, S]:

"we integrate the upper bound estimate into the Fortran routine GLTR in the library GALAHAD as new stopping criteria and test the trust-region solver TRU on the problem collection CUTEr. The numerical results show that, with the new stopping criteria in GLTR, the overall performance of TRU can be improved considerably."

- **Adopted?** No commit message in GALAHAD's GLTR history (2018–2026) mentions these criteria or their authors [practice, P, C32; commit messages only; the code itself was not diffed].
- [inferred] An outside, published, drop-in improvement to his own solver was apparently not taken up. **Unverified**: the criteria could have entered under another name.

### 5.3 Eigenvalue-based methods

GLTR 1999 ended by saying that its result "calls into question a number of other recent eigensolution-based proposals for solving the trust-region subproblem" (03 §4, quoting *SIAM J. Optim.* 9 (1999) 504–525, p.522) [stated, P, C33].

Jia & Wang, "A comparison of eigenvalue-based algorithms and the generalized Lanczos trust-region algorithm for solving the trust-region subproblem", arXiv 2102.09693 (abstract read) [C36, observed, S]:

- "For a reasonable comparison of overall efficiency … a vital premise is that the two kinds of algorithms must compute the approximate solutions of TRS with (almost) the same accuracy, but such premise has been ignored in the literature."
- "A number of numerical experiments are reported to illustrate that IRA and IRRA are competitive with GLTR".

**Answered?** No reply found.

### 5.4 Fletcher's 1981 objection to modified-factorization norms, and an unkept promise

Gould & Nocedal, "The modified absolute-value factorization norm for trust-region minimization", in *High Performance Algorithms and Software in Nonlinear Optimization*, Kluwer (1998) 225–241, 10.1007/978-1-4613-3279-4_15 (preprint p.13 read) [C40, stated, P]:

- The objection as he reports it: "In particular Roger Fletcher (Dundee) expressed concern that the distortion induced by (3.5) and (3.9) may be substantial."
- His answer: "We accept that (3.15) may not be as desirable as (3.1), but believe that while (3.1) is out of the question for most large-scale problems, (3.15) is practical, and often useful, for many of them."
- The second objection: "Fletcher also worried that changes in the pivot ordering … may make it difficult to derive effective methods for adjusting the trust-region radius."
- His concession: "we recognize this as a possible defect, and are currently investigating more sophisticated trust-region adjustment strategies both in this and other contexts."

**Kept?** No follow-up paper on trust-region adjustment under changing pivot orders was found. The HSL_VF06 norm is in note 03 §3.1.

---

## 6. Test infrastructure (CUTE / CUTEr / CUTEst, SIF)

- **Problem sizes.** Liu, Fredriksson & Markidis, "A survey of HPC algorithms and frameworks for large-scale gradient-based nonlinear optimization", *J. Supercomput.* 78 (2022) 17513–17542, 10.1007/s11227-022-04555-8 [C41, observed, S, **S2 snippet**]: "many common benchmark problems for optimization, such as the CUTEst library [68], contain mainly relatively small problems, where the authors found that serial solvers like MA27 from HSL performed well."
- **Representativeness.** Audet, Denorme, Diouane, Le Digabel & Tribes, "Adaptive direct search algorithms for constrained optimization", arXiv 2507.23054 (v1 read, p.19) [C42, observed, S]: "a subset of the CUTEst [32] collection of constrained problems, which are also fast to evaluate but still not representative of real-world problems."
- **Fixed sparsity structure biases CPU comparisons.** Birgin & Martínez 2020, arXiv 1907.02401 v1, pp.18–19 [C18, observed, S]:
  - "the current tools available in CUTEst compute the full Jacobian of the constraints … instead of J(x) … respectively. On the one hand, this feature preserves the Jacobian's and the Hessian-of-the-Lagrangian's sparsity structures independently of μ̄k and x, as required by some solvers. On the other hand, it impairs Algorithm 2.1, when applied to problems from the CUTEst collection, of fully exploiting the potential advantage of dealing with inequality constraints without adding slack variables."
  - "Of course, this CUTEst inconvenient influences negatively the comparison of Algencan with other solvers if the CPU time is used as a performance measure."
- **Wrong sparsity patterns (2026, open).** J. Haffner, CUTEst issue #110, 14 Jan 2026, https://github.com/ralna/CUTEst/issues/110 [C43, observed, S; opening post only]: "For a large number of lower-dimensional problems I have tested, the sparsity patterns returned from CUTEst do seem to be incorrect."
  - The first report was on pycutest #105 (9 Jan 2026) [C44], about `isphess` on HS92 returning "36 elements for x0 of size 6, most of which are zero". pycutest's maintainers labelled it "bug" and "upstream".
  - Both issues show no visible reply. The CUTEst issue list shows #110 as **open** (fetched 2026-09-28).
  - [inferred] The reports concern structural, not numerical, nonzeros. The CUTEst paper and SIF design treat sparsity as structural, from group/element structure. That is the same property Birgin & Martínez describe. **Not confirmed by any reply.**
- **Self-critique already in print** (cross-ref 01 §2): SIF "ambitiously (and, with hindsight, perhaps rather arogantly [sic]) called the Standard Input Format"; Fortran 77 inflexibility "certainly the main source of complaint we receive" [stated, P].
- **Counter-view from a co-author (not independent).** Gratton & Toint, "OPM, a collection of Optimization Problems in Matlab", arXiv 2112.05636 [C45, **S2 snippet**]: "CUTEst, which we believe remains an authoritative source of test problems today".
- **Answered?**
  - No printed reply to the size, representativeness or Jacobian-structure critiques was found.
  - A 2023 CUTEst commit "added cisgrp to find sparsity of individual functions" (03 scratch git log) is related but not a declared response [practice, P, C32; relation inferred].
  - The problem collection keeps growing with application and ML-style problems: "New data fitting problems from STFC and Diamond Light Source" (2020), "a few logistic regression problems LR*" (2023) (03 §2). [inferred] This partly answers the "small, academic" charge.

---

## 7. Predictions that did not come true, or were revised

| Year | Prediction or plan (source) | What happened |
|---|---|---|
| 2000 | Gould & Toint, "SQP methods for large-scale nonlinear programming", in *System Modelling and Optimization* (IFIP), Kluwer (2000) 149–178, 10.1007/978-0-387-35514-6_7, pp.171–172 [C46, stated, P]: recent results show SQP methods "are often considerably better than state-of-the-art implementations of other nonlinear programming algorithms (such as MINOS and, it hurts us to say, LANCELOT) … we expect this trend to continue for large ones (say n ∼ 10⁵–10⁶) in the near future, provided that options for solving core linear systems by iterative … methods are incorporated." | **Revised by Gould himself within three years.** SIAG/OPT *Views-and-News* 14(1) (2003), "Some reflections on the current state of active-set and interior-point methods for constrained optimization", p.3 [C47, stated, P]: "We have currently suspended development of the large-scale SQP method … the cost of the QP solution so dominates that other non-SQP approaches (such as IPOPT [33], KNITRO [4] and LOQO [32]), in which truncation is possible, have made significant progress even before our QP code had solved its first subproblem!—see also [23] for further evidence that interior-point methods appear to scale better than SQP ones." Here [23] is Morales, Nocedal, Waltz, Liu & Goux, "Assessing the potential of interior methods for nonlinear optimization" (First Sandia Workshop on Large-Scale PDE-Constrained Optimization, 2003). [observed, S, C50] In Mittelmann's 2026 AMPL-NLP benchmark, SNOPT (SQP) solves 30 of 47 problems, against 45–47 for the interior-point and other codes, and has the worst scaled geometric mean (103, against 1–38). [inferred] This is one medium-size benchmark, not a verdict on SQP at large scale. |
| 2003 | "We are more enthusiastic about an SLP-QP approach we are currently developing [3]" (SIAG 2003, p.3) [stated, P]. [3] is Byrd, Gould, Nocedal & Waltz, RAL-TR-2002-032 | The method was published (*Math. Program.* 2004, 10.1007/s10107-003-0485-4; 01 §1). **No SLP-EQP NLP solver exists in GALAHAD at HEAD**; only the EQP subproblem package `src/eqp` does [practice, P, C32]. Whether the method lives on in KNITRO was **not checked** |
| 2008, 2010, 2012 | Trust-funnel "tests are ongoing"; S2QP large-scale numerics; "sophisticated ARC implementations and the necessary comparison with state of the art trust-regions" | Not delivered in print (03 §5 ledger; §4.4 above) |
| 1998 | "more sophisticated trust-region adjustment strategies" in response to Fletcher | Not found (§5.4) |

---

## 8. Rival schools: where each draws the line against Gould's approaches

| School | Representative critics in this note | What they reject or dispute | Gould's position |
|---|---|---|---|
| Interior-point NLP (IPOPT, KNITRO, LOQO) | Dolan & Moré; Benson–Shanno–Vanderbei; Morales–Nocedal–Waltz et al. (via Gould's own citations) | Augmented-Lagrangian (LANCELOT) and large-scale SQP as general NLP engines | Conceded in 2003 [stated, P]. His own general NLP successors never left `forthcoming`/`oblivion` (03 §1.2) |
| Safeguarded AL (ALGENCAN) | Andreani, Birgin, Martínez, Schuverdt | LICQ-based theory; slacks and bounds for inequalities; CUTEst's fixed sparsity | No reply found |
| Projection / splitting (imaging) | Censor, Combettes, Herman et al. | Judging projection methods on Netlib LPs with simple variants | Conceded the variants, kept the scoped conclusion (§1) |
| Quasi-Newton theory (Byrd–Schnabel) | Khalfan, Byrd, Schnabel | The ULI assumption in SR1 theory | No reply found |
| "Average/regional" complexity; algorithm-independent lower bounds | Curtis–Robinson; Carmon–Duchi–Hinder–Sidford | Worst-case bounds driven by contrived functions; lower bounds only within classes | Worst case is "reassuring" and "essentially sharp" (2012) |
| Eigenvalue-based TRS | Jia & Wang (also Adachi et al., not read) | GLTR 1999's dismissal of eigen-based TRS | No reply found |

---

## 9. Blind spots and limits suggested by the critiques (for the skill)

All [inferred] from the evidence above. Each item names the evidence.

1. **Generalising from his benchmark sets.** Censor et al. objected to the step from Netlib LPs to "in general" (§1). Liu et al. and Audet et al. question how representative CUTEst is (§6). His conclusions are strongest where his test sets are, and are contestable for large structured application classes.
2. **Theory built on assumptions practitioners doubt.** Examples are ULI for SR1 (§3.1) and LICQ for augmented Lagrangians (§3.2). The practical recommendation (SR1; LANCELOT) survived, but the theorem's reach was narrowed by others.
3. **The hard case is dismissed on practice grounds.** It is "never observed … for anything other than contrived examples" (§5.1). Critics who need guarantees (DFO, PDE-constrained robust design) treat GLTR as "merely heuristic".
4. **Outsiders' improvements to his own codes are slow to enter the library, or do not enter it.**
   - TRACE has sat in `forthcoming` since 2014.
   - The Zhang–Shen–Li stopping rules are not visible in GLTR's history.
   - GALAHAD ARC still uses the GLRT default that Dussault–Migot–Orban outperform.
   - Compare 03 §1.1: "the directory tree, not the paper, says what Gould actually trusts."
5. **Weak visibility in third-party benchmarks.** GALAHAD appears only in Mittelmann's QP table, as version 3, and no Gould NLP solver appears in the NLP table (§2.3). His strongest external comparisons are ones he ran himself with J. A. Scott (03 §3.1).
6. **Errors are corrected in public, and critique is answered with experiments.** The 1989 correction, the 2012 erratum, the 2017 corrigendum and the 2012 projection reply follow one pattern: rerun, concede the narrow point, restate the scoped conclusion. The pattern is visible only where a formal critique was published. Critiques in citation contexts and GitHub issues have received no visible reply.

---

## Contradictions (kept, not reconciled)

- **K1. Projection methods.**
  - Gould 2008: "in general none of the variants considered are especially effective or competitive".
  - Censor et al.: "correctly implemented projection methods are very efficient … especially for those that are large, sparse, and originate from real-life applications".
  - Gould 2012 accepts that his variants were "suboptimal", and in the same paragraph calls the claim that they were unrepresentative "debatable" (§1.3).
  - Bauschke & Koch cite both as true (§1.4).
- **K2. Random test problems.**
  - Gould: "random examples may not reflect practical experience in many cases" (2012, p.1094).
  - Censor et al.: "random matrices do show up in many real-life problems" (arXiv v1 p.5).
- **K3. The hard case.**
  - Critics: GLTR "could not handle hard cases"; the Lanczos approach "does not work … in the hard case"; the restart remedy is "very expensive".
  - Gould (2025–26): never observed outside "contrived examples".
  - Yet his own direct solver TRS (2010) devotes a subsection to "Fast convergence in the hard case" (§5.1).
- **K4. Worst-case pessimism.**
  - CGT 2012: the bounds "may still seem unnecessarily pessimistic" but are "essentially sharp", and the perspective is "reassuring".
  - Curtis & Robinson: the tight examples are ones "one might argue are pedogogical and distinct from those encountered in regular practice" (§4.2).
- **K5. ARC against trust regions in practice.**
  - CGT 2012: "Preliminary numerical experiments with ARC variants on small scale problems from CUTEr show superior performance of ARC when compared with a basic trust-region implementation" (Optima p.9).
  - Dussault–Migot–Orban 2024: their ARCqK outperforms both a Steihaug–Toint trust region and GALAHAD's ARC.
  - TRACE: a trust region with ARC's complexity (§4).
- **K6. Eigenvalue-based TRS.**
  - GLTR 1999: its results "call[] into question" eigensolution-based proposals.
  - Jia & Wang 2021: eigenvalue methods are "competitive with GLTR" once accuracy is matched (§5.3).
- **K7. SQP's future.** Gould & Toint 2000 expected SQP's advantage to extend to 10⁵–10⁶ variables. Gould 2003 suspended large-scale SQP because interior-point methods "appear to scale better" (§7). Both statements are his.
- **K8. Critics inside the network.**
  - Conn co-authors a paper saying GLTR "could not handle hard cases".
  - Orban co-authors a paper that outperforms GALAHAD ARC.
  - Curtis and Robinson both overturn the TR-versus-ARC complexity framing and thank CGT for "enlightening discussions".
  - [inferred] Critique of Gould is mostly collegial and often comes from co-authors. That makes "hostile peer critique" nearly absent from the record, not necessarily absent in fact.

---

## Gaps (what could not be found or read)

- **The JOSS review of GALAHAD 4.0** (openjournals/joss-reviews #4882; reviewers F. E. Curtis and J. A. J. Hall) [C51]:
  - WebFetch shows only the opening post;
  - the GitHub API and the GitHub MCP tool refuse this repository in this session.
  - **Not read.** This is the only known formal software review; its content is unknown.
- **Replies to GitHub criticism.** For CUTEst #110 and pycutest #105, only the opening posts are visible. Whether Gould answered is unknown.
- **The 1999–2002 benchmark reports themselves** (COPS ANL/MCS-TM-246 and COPS 3.0; Benson–Shanno–Vanderbei 2001/2003; Chin 2001):
  - **not read**, because of bot challenges at OSTI and Argonne, or because no open copy was found;
  - the exact margins by which LANCELOT A lost are therefore unknown.
- **Full texts of the Byrd–Khalfan–Schnabel SR1 papers** (the DTIC and CU Boulder repositories are blocked) and of Andreani et al. 2007/2008 (Birgin's site reset the connection). Only abstracts and citation snippets were used.
- **Whether CGT ever answered the ULI critique.** *Trust-Region Methods* (2000) was not read, and it is the most likely place for an answer.
- **Rejected papers, referee reports, OpenReview.** None are public; Gould does not publish at ML venues.
- **Hostile critiques, critical essays, blog posts, failed replications.** None found. The search was limited to scholarly APIs, two WebSearch calls and known URLs. Absence here is weak evidence.
- **ARC practical comparisons by others.**
  - The abstracts of Dussault, "ARCq" (*OMS* 33 (2018) 322–335, 10.1080/10556788.2017.1322080), and Bianconcini, Liuzzi, Morini & Sciandrone (*COAP* 60 (2015) 35–57, 10.1007/s10589-014-9672-x) were not available: the publisher elides them, and OpenAlex returned 503.
  - Their verdicts on ARC are **not known**.
- **Critiques of constraint preconditioning and KKT linear algebra** (Keller–Gould–Wathen 2000 and successors). 390 citation contexts were scanned with no substantive critique found, only routine remarks about factorization cost. It is recorded as "none found", not as "none exists".
- **Nesterov–Polyak priority on cubic regularization.** Not examined.
- **Why Mittelmann still runs GALAHAD 3, and why no Gould NLP solver is in the AMPL-NLP benchmark.** Unknown.
- **Whether the Zhang–Shen–Li GLTR stopping criteria entered GALAHAD under another name.** Only commit messages were checked, not a diff of `gltr.F90`.
- **LANCELOT book review in zbMATH.** The contents are "unavailable due to conflicting licenses".

---

## Sources

P = primary (Gould's own text, record or code); S = secondary. "read" = read in full or in the passages cited; "abstract" = abstract only; "S2 snippet" = Semantic Scholar citation context only; "metadata" = identifier checked, text not read.

- C01 · N. I. M. Gould, "How good are projection methods for convex feasibility problems?", *Comput. Optim. Appl.* 40 (2008) 1–12 · 10.1007/s10589-007-9073-5 · P (abstract quoted via C03; full text read by agent 02)
- C02 · N. I. M. Gould, "How good are extrapolated bi-projection methods for linear feasibility problems?", *Comput. Optim. Appl.* 51 (2012) 1089–1095 · 10.1007/s10589-011-9414-2 · P (read in full)
- C03 · Y. Censor, W. Chen, P. L. Combettes, R. Davidi, G. T. Herman, "On the effectiveness of projection methods for convex feasibility problems with linear inequality constraints", *Comput. Optim. Appl.* 51 (2012) 1065–1088 · 10.1007/s10589-011-9401-7 · arXiv 0912.4367 (v1) · S (read pp.1–6, 14)
- C04 · H. H. Bauschke, V. R. Koch, "Projection methods: Swiss army knives for solving feasibility and best approximation problems with halfspaces", *Contemp. Math.* 636 (2015) 1–40 · 10.1090/conm/636/12726 · arXiv 1301.4506 · S (read p.13)
- C05 · N. I. M. Gould, D. Orban, Ph. L. Toint, "GALAHAD, a library of thread-safe Fortran 90 packages for large-scale nonlinear optimization", *ACM TOMS* 29(4) (2003) 353–372 · 10.1145/962437.962438 · P (introduction and references read)
- C06 · E. D. Dolan, J. J. Moré, "Benchmarking optimization software with performance profiles", *Math. Program.* 91 (2002) 201–213 · 10.1007/s101070100263 · arXiv cs/0102001 · S (read §§3–5)
- C07 · E. D. Dolan, J. J. Moré, "Benchmarking optimization software with COPS", ANL/MCS-TM-246 (2000/2001) · 10.2172/775270 · S (metadata; blocked)
- C08 · E. D. Dolan, J. J. Moré, T. S. Munson, "Benchmarking optimization software with COPS 3.0", ANL/MCS-TM-273 (2004) · 10.2172/834714 · S (metadata; blocked)
- C09 · H. Y. Benson, D. F. Shanno, R. J. Vanderbei, "A comparative study of large-scale nonlinear optimization algorithms", in *High Performance Algorithms and Software for Nonlinear Optimization*, Kluwer (2003) 95–127 · 10.1007/978-1-4613-0241-4_5 · S (metadata; not read)
- C10 · C. M. Chin, "Numerical results of SLPSQP, filterSQP and LANCELOT on selected CUTE test problems", Numerical Analysis Report NA/203, University of Dundee (2001) · known from C05's reference list · S (not read)
- C11 · R. Fletcher, S. Leyffer, "Solving mathematical programs with complementarity constraints as nonlinear programs", *Optim. Methods Softw.* 19 (2004) 15–40 · 10.1080/10556780410001654241 · S (S2 snippet)
- C12 · H. Fayez Khalfan, R. H. Byrd, R. B. Schnabel, "A theoretical and experimental study of the symmetric rank-one update", *SIAM J. Optim.* 3 (1993) 1–24 · 10.1137/0803001 · S (abstract)
- C13 · R. H. Byrd, H. Fayez Khalfan, R. B. Schnabel, "Analysis of a symmetric rank-one trust region method", *SIAM J. Optim.* 6 (1996) 1025–1039 · 10.1137/S1052623493252985 · S (abstract)
- C14 · A. R. Conn, N. I. M. Gould, Ph. L. Toint, "Convergence of quasi-Newton matrices generated by the symmetric rank one update", *Math. Program.* 50 (1991) 177–195 · 10.1007/BF01594934 · P (metadata; content attested via C15 and S2 snippets)
- C15 · Z. Ramzi, F. Mannel, S. Bai, J.-L. Starck, P. Ciuciu, T. Moreau, "SHINE: SHaring the INverse Estimate from the forward pass for bi-level optimization and implicit models" (2021–2023) · arXiv 2106.00553 (v4) · S (read p.5)
- C16 · R. Andreani, E. G. Birgin, J. M. Martínez, M. L. Schuverdt, "On augmented Lagrangian methods with general lower-level constraints", *SIAM J. Optim.* 18 (2007) 1286–1309 · 10.1137/060654797 · S (abstract + S2 snippet)
- C17 · R. Andreani, E. G. Birgin, J. M. Martínez, M. L. Schuverdt, "Augmented Lagrangian methods under the constant positive linear dependence constraint qualification", *Math. Program.* 111 (2008) 5–32 · 10.1007/s10107-006-0077-1 · S (S2 snippet)
- C18 · E. G. Birgin, J. M. Martínez, "Complexity and performance of an augmented Lagrangian algorithm", *Optim. Methods Softw.* 35 (2020) 885–920 · 10.1080/10556788.2020.1746962 · arXiv 1907.02401 · S (read pp.1–2, 18–19)
- C19 · A. Bambade, F. Schramm, S. El-Kazdadi, S. Caron, A. Taylor et al., "ProxQP: an efficient and versatile quadratic programming solver for real-time robotics applications and beyond", *IEEE Trans. Robotics* (2025) · 10.1109/tro.2025.3577107 · S (S2 snippet)
- C20 · A. R. Conn, N. I. M. Gould, Ph. L. Toint, "A globally convergent augmented Lagrangian algorithm for optimization with general constraints and simple bounds", *SIAM J. Numer. Anal.* 28 (1991) 545–572 · 10.1137/0728030 · P (metadata)
- C21 · N. I. M. Gould, Ph. L. Toint, "Erratum to: Nonlinear programming without a penalty function or a filter", *Math. Program.* 131 (2012) 403–404 · 10.1007/s10107-011-0491-x · P (S2 snippet; read by agents 01/03)
- C22 · X. Zhu, "On a globally convergent trust region algorithm with infeasibility control for equality constrained optimization", *J. Appl. Math. Comput.* 50 (2015) 275–298 · 10.1007/s12190-015-0870-1 · S (S2 snippet)
- C23 · C. Cartis, N. I. M. Gould, Ph. L. Toint, "Corrigendum: On the complexity of finding first-order critical points in constrained nonlinear optimization", *Math. Program.* 161 (2017) 611–626 · 10.1007/s10107-016-1016-4 · P (read pp.1–2 and acknowledgments)
- C24 · F. E. Curtis, D. P. Robinson, M. Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε⁻³ᐟ²) for nonconvex optimization", *Math. Program.* 162 (2017) 1–32 · 10.1007/s10107-016-1026-2 · S (author copy read pp.3, 11, 29–30)
- C25 · F. E. Curtis, D. P. Robinson, "Regional complexity analysis of algorithms for nonconvex smooth optimization", *Math. Program.* 187 (2021) 579–615 · 10.1007/s10107-020-01492-3 · arXiv 1802.01062 · S (read pp.2–3)
- C26 · Y. Carmon, J. C. Duchi, O. Hinder, A. Sidford, "Lower bounds for finding stationary points I", *Math. Program.* 184 (2020) 71–120 · 10.1007/s10107-019-01406-y · arXiv 1710.11606 · S (read p.2)
- C27 · C. Cartis, N. I. M. Gould, Ph. L. Toint, "How much patience do you have? A worst-case perspective on smooth nonconvex optimization", *Optima* 88 (2012) · https://www.numerical.rl.ac.uk/media/people/nick-gould/CartGoulToin12_optima.pdf · P (read pp.3, 9)
- C28 · C. Cartis, N. I. M. Gould, Ph. L. Toint, "Worst-case evaluation complexity and optimality of second-order methods for nonconvex smooth optimization", *Proc. Int. Cong. Math. 2018*, Rio de Janeiro, vol. 3, 3697–3738 · P (header and abstract read)
- C29 · J. Ugon, zbMATH review Zbl 1520.90002 of C. Cartis, N. I. M. Gould, Ph. L. Toint, *Evaluation Complexity of Algorithms for Nonconvex Optimization*, MOS-SIAM 30 (2022), 10.1137/1.9781611976991 · https://api.zbmath.org · S (read)
- C30 · Y. Cherruault, zbMATH review Zbl 0958.65071 of A. R. Conn, N. I. M. Gould, Ph. L. Toint, *Trust-Region Methods*, MPS-SIAM (2000), 10.1137/1.9780898719857 · S (read). The reviewer's only reservation: "I only regret that global optimization methods are not described in this work."
- C31 · J.-P. Dussault, T. Migot, D. Orban, "Scalable adaptive cubic regularization methods", *Math. Program.* 207 (2024) 191–225 · 10.1007/s10107-023-02007-6 · arXiv 2103.16659 · S (published abstract via Semantic Scholar; arXiv v1 abstract read)
- C32 · GALAHAD git repository (github.com/ralna/GALAHAD), clone at HEAD afa13a5e (2026-09-26): `src/forthcoming/trace/trace.F90` header, `src/arc/arc.F90` defaults, GLTR commit history, tree listing · P (practice; read)
- C33 · N. I. M. Gould, S. Lucidi, M. Roma, Ph. L. Toint, "Solving the trust-region subproblem using the Lanczos method", *SIAM J. Optim.* 9 (1999) 504–525 · 10.1137/S1052623497322735 · P (quoted via note 03, which read §§6–7)
- C34 · L.-H. Zhang, C. Shen, R.-C. Li, "On the generalized Lanczos trust-region method", *SIAM J. Optim.* 27 (2017) 2110–2142 · 10.1137/16M1095056 · S (abstract)
- C35 · Y. Zhou, Z. Bai, R.-C. Li, "Linear constrained Rayleigh quotient optimization: theory and algorithms", *CSIAM Trans. Appl. Math.* 2 (2021) 195–262 · 10.4208/csiam-am.2021.nla.01 · arXiv 1911.02770 · S (read p.23 and references)
- C36 · Z. Jia, F. Wang, "A comparison of eigenvalue-based algorithms and the generalized Lanczos trust-region algorithm for solving the trust-region subproblem" (2021) · arXiv 2102.09693 · S (abstract)
- C37 · N. Amaioua, C. Audet, A. R. Conn, S. Le Digabel, "Efficient solution of quadratically constrained quadratic subproblems within the mesh adaptive direct search algorithm", *Eur. J. Oper. Res.* 268 (2018) 13–24 · 10.1016/j.ejor.2017.10.058 · S (S2 snippet, 2016 preprint)
- C38 · P. Kolvenbach, O. Lass, S. Ulbrich, "An approach for robust PDE-constrained optimization with application to shape optimization of electrical engines and of dynamic elastic structures under uncertainty", *Optim. Eng.* 19 (2018) 697–731 · 10.1007/s11081-018-9388-3 · S (S2 snippet)
- C39 · H. Al Daas, N. I. M. Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems" (2025–26) · arXiv 2511.11135 (v3) · P (read p.14 and references)
- C40 · N. I. M. Gould, J. Nocedal, "The modified absolute-value factorization norm for trust-region minimization", in *High Performance Algorithms and Software in Nonlinear Optimization*, Kluwer (1998) 225–241 · 10.1007/978-1-4613-3279-4_15 · P (read preprint p.13)
- C41 · F. Liu, A. Fredriksson, S. Markidis, "A survey of HPC algorithms and frameworks for large-scale gradient-based nonlinear optimization", *J. Supercomput.* 78 (2022) 17513–17542 · 10.1007/s11227-022-04555-8 · S (S2 snippet)
- C42 · C. Audet, T. Denorme, Y. Diouane, S. Le Digabel, C. Tribes, "Adaptive direct search algorithms for constrained optimization" (2025) · arXiv 2507.23054 · S (read p.19)
- C43 · J. Haffner, "CUTEst returns wrong sparsity patterns for a large number of lower-dimensional problems", CUTEst issue #110, 14 Jan 2026 · https://github.com/ralna/CUTEst/issues/110 · S (opening post only)
- C44 · J. Haffner, pycutest issue #105, 9 Jan 2026 · https://github.com/jfowkes/pycutest/issues/105 · S (opening post only)
- C45 · S. Gratton, Ph. L. Toint, "OPM, a collection of Optimization Problems in Matlab" (2021) · arXiv 2112.05636 · S (S2 snippet; co-author of Gould, not independent)
- C46 · N. I. M. Gould, Ph. L. Toint, "SQP methods for large-scale nonlinear programming", in *System Modelling and Optimization* (IFIP), Kluwer (2000) 149–178 · 10.1007/978-0-387-35514-6_7 · P (read pp.171–172)
- C47 · N. I. M. Gould, "Some reflections on the current state of active-set and interior-point methods for constrained optimization", *SIAG/OPT Views-and-News* 14(1) (2003) · https://www.numerical.rl.ac.uk/media/people/nick-gould/Goul03_siagopt.pdf · P (read p.3 and references)
- C48 · H. D. Mittelmann, "Benchmark of noncommercial QP solvers", 29 Jun 2026 · https://plato.asu.edu/ftp/qpbench.html · S (read)
- C49 · H. D. Mittelmann, "Benchmarks of commercial and noncommercial optimization software", ISMP 2018 slides · https://plato.asu.edu/talks/ismp2018.pdf · S (read pp.9, 13–14)
- C50 · H. D. Mittelmann, "AMPL-NLP Benchmark", 9 Sep 2026 · https://plato.asu.edu/ftp/ampl-nlp.html · S (read)
- C51 · JOSS review thread for GALAHAD 4.0, openjournals/joss-reviews #4882 (opened 26 Oct 2022) · https://github.com/openjournals/joss-reviews/issues/4882 · S (not readable beyond the opening post)
- C52 · F. E. Curtis, D. P. Robinson, M. Samadi, "Complexity analysis of a trust funnel algorithm for equality constrained optimization", *SIAM J. Optim.* 28 (2018) 1533–1563 · 10.1137/16M1108650 · arXiv 1707.00337 · S (read p.27)
- C53 · Semantic Scholar Graph API, citation contexts for ten Gould works (ARC I, CUTEst, CGT 1991 AL, Keller–Gould–Wathen 2000, GLTR, CGT 1991 SR1, Gould–Scott 2016, trust funnel 2010, LANCELOT 1996, Gould 2008/2012), fetched 2026-09-28 · https://api.semanticscholar.org · S (method source)
- C54 · Notes 01–04 of this team for Gould (`references/research/01-publications.md`, `02-methodology.md`, `03-process-evidence.md`, `04-mentorship.md`) · S (cross-reference only)
