# 03 · Process evidence: what Nicholas I. M. Gould actually does

- **Researcher**: Nicholas Ian Mark Gould (Nick Gould), Senior Fellow, STFC Rutherford Appleton Laboratory (RAL); visiting professor at Oxford and Edinburgh. Living.
- **Dimension**: research agent 03 of 06, process evidence (behaviour, not statements). nuwa research-craft Phase 1.
- **Research date**: 2026-09-28.
- **Sources consulted**: 50 (list at the end).
  - **Primary, 43**: 4 code repositories read through their full git histories and source trees (S01–S04); the JOSS review page and 2 GitHub issue pages, metadata and opening posts only (S05–S07); 31 papers or preprints read in their experimental sections or in full (S10–S39); arXiv abstract pages and the RAL staff page (S46, S48); 2 papers used through note 01 with their DOIs re-checked (S40, S41); and one critique identified but not read (S20a).
  - **Secondary, 7**: metadata-only items (S42, S43, S44), the Crossref checks (S45), the WebSearch result (S47), and notes 01 and 02 of this team (S49, S50), used only for cross-reference.
  - WebSearch calls used: 1 of 2.
- **Local corpus**: `references/sources/papers`, `talks`, `essays` and `software` held only `.gitkeep`, so there was no user-supplied material. `private/` was not opened. No transcript was found, so nothing was saved under `sources/talks/`.
- **Method**:
  - I cloned the full histories of GALAHAD, CUTEst, SIFDecode and the SIF test-problem collection. I read the directory trees, the READMEs, the package headers (each records its release date and principal author), the test programs, the default parameter values and the commit logs.
  - I then read the experiment sections, appendices and conclusions of the papers where a practice shows, and compared arXiv v1 with later versions where two versions exist.
  - Every DOI below was resolved with the Crossref API in this run, or read off the PDF itself. arXiv ids were checked on arxiv.org. Page numbers are journal pages when the author PDF is the published version, and "PDF p." otherwise.

**Tags.**
- **[stated]**: what Gould or his co-authors wrote about their own procedure, inside a paper or code comment.
- **[practice]**: what the record shows was done (code, dates, tables, defaults, commits).
- **[observed]**: what others reported.
- **[inferred]**: my reading, with no direct source.

Each item is also marked **P** (primary) or **S** (secondary).

**Caution on authorship.** Almost every paper is co-authored, with alphabetical author order (see 01 §0). So "practice in paper X" is the practice of that team, not necessarily Gould's own choice. The code record is different: of 1,993 GALAHAD commits, 1,136 are by Gould (git author names "Nick Gould" or "nimgould", [practice, P, S01]). Most package headers name him as principal author. The code is therefore the most individual trace of how he works.

---

## 0. Era and resource context (read before transferring any practice)

| Period | Setting of the practice | Evidence |
|---|---|---|
| 1988–1996 | Three-person transatlantic team (Conn, Gould, Toint). Small dense tests first, then an "8 months of nearly uninterrupted computation" LANCELOT campaign on a workstation network | 01 §2.A; 02 era table [S] |
| 1999 | IBM RISC System/6000 3BT workstation, 64 MB RAM, xlf90. A 30-CPU-minute limit per run | GLTR, *SIOPT* 9 (1999) p.517–518 [practice, P, S27] |
| 2005 | One 1.6 GHz Pentium IV PC with 512 MB. A 95,040-run parameter sweep | 4OR 2005 p.232 [practice, P, S23] |
| 2008–2013 | Dell workstations. Single-CPU tests in 2008–2010; "four cores" with OpenMP by 2013. Compilers g95, ifort, gfortran 4.3 | S19 p.8; S10 p.50; S11 p.135 [practice, P] |
| 2014–2017 | Matlab prototypes by co-authors (Robinson's group) next to Fortran GALAHAD code. Cplex used as the subproblem solver inside Matlab | S12 PDF p.11; S13 p.1903 [practice, P] |
| 2018–2026 | GALAHAD and CUTEst on GitHub (moved from CCPForge svn in February 2018). A small software team: Gould, J. Fowkes, A. Montoison, D. Orban. Four cores of an i9-9900 with 32 GB for the 2025 TREK tests. Gould has worked half time since 2017 (homepage, via 01) | S01; S32 v1 p.14 [practice, P] |

---

## 1. The code as a lab notebook (GALAHAD)

### 1.1 A three-tier pipeline: `src/` → `forthcoming/` → `oblivion/`

[practice, P, S01] The GALAHAD source tree keeps three tiers. `src/README.packages` labels each package "ok", "beta" or "alpha" and states the rules in one line each:
- "packages that are far from ready but seem promising are in forthcoming/"
- "expired/unfinished packages have been cast into oblivion/"

Both directory READMEs are signed "Nick Gould (for the GALAHAD team)" and dated October 2016 [stated, P]. Typos are original.
- `forthcoming/README.forthcoming`: "A collection of packages that *may* appear in GALAHAD. Often, this is simply that a given package needs a bit of loving care to move it from an "idea" to something that is reliable and useful to all. If you would like to see any of these moved up the priority chain, let us know."
- `oblivion/README`: "Wecome to Oblivion. This is a repository for protoype GALAHAD packages that, honestly, didn't make the grade, or which we ran out of energy, effort or patience to finish. Most will work to some extent, but we do not believe that they have met their initial promise. We have cast them into oblivion as a warning to others." A May 2021 addendum lists packages "know to be broken" (PQP) and those with "No proper interface" (NLSSRT, spelled so in the README; the directory is `nllsrt`).

What actually moves between the tiers [practice, P, S01, git history]:
- **Promoted from `forthcoming` to `src`**:
  - LPB, a new package on 2018-08-26;
  - TRB, "officially released" on 2021-08-01;
  - UGO, BGO, DGO and LHS, moved together on 2022-03-07;
  - TREK, which went from an "alpha" forthcoming package (2025-05-27) to `src/trek` on 2025-11-17.
- **Still waiting in `forthcoming`**, with the dates in their own headers:
  - BARC, adaptive cubic regularization with bounds, "originally released GALAHAD Version 2.2. February 7th 2008";
  - PDQP, "development started August 21st 2009";
  - TRAL, trust-region augmented Lagrangian, 2012;
  - TRACE, 2014;
  - FiSQP, 2014;
  - COLT, 2023;
  - EPF/EXPO, 2024–25;
  - QPF, 2024.
- **In `oblivion`**: 27 directories. 22 are solvers and 5 are utilities (QPS, QTRANS and SCALING for QP data scaling and shifting; CPU_TIME; a METIS copy). The 22 solvers include:
  - 8 directories of general-NLP solvers, covering 7 designs (§1.2);
  - the nonlinear least-squares code NLLSRT;
  - trust-region and subspace methods: TR1, TR2, TR2A, GSM, ISM, ERMO, TRTN;
  - QP codes: PQP, CQPS, LPQPA, LPQPB;
  - the projection code LCF (§4.1);
  - AGD (§1.3).

Caveat [practice, P]: `README.packages` is partly stale. Its `forthcoming` list still includes LPB and TRB, which now live in `src/`. The "alpha" and "beta" labels quoted in §1.2 come from that file.

[inferred] "Released" in a package header means "put in the repository with a version number", not "recommended". A package can be "released" and sit in `forthcoming` for 18 years (BARC). The directory tree, not the paper, says what Gould actually trusts.

### 1.2 The fate of every general-constrained NLP solver he started (answers the gap left by note 01)

Since LANCELOT (1992), `lancelot` is still the only package in `src/` for general nonlinearly constrained optimization. FILTRANE covers nonlinear least squares and feasibility, not optimization [practice, P, S01 README.packages]. Every successor attempt that the tree records is in `forthcoming` or `oblivion`:

| Package (tier) | What it is (header text) | Dates in header / git | Linked papers | Fate |
|---|---|---|---|---|
| SUPERB (oblivion, "beta") | "SUPERB, the Sequential Unconstrained minimization of an l_p Penalty function treating Equality and inequality Restrictions by Barrier terms"; README.packages: "trust-region interior-point for NLP" | "development started October 21st, 2002"; "originally released GALAHAD Version 2.0. February 16th 2005" | The barrier route announced in SIAG/OPT April 2003 ("we have now turned to … sequential barrier-function minimization", 01 §2.D) | Cast into oblivion. **This is the 2003 barrier NLP solver.** It was built, released in 2005, and then abandoned [practice, P] |
| LPSQP (oblivion, "alpha") | "Use an l_p SQP approach to solve general nonlinear programmimg problems" [sic] | released 2.0, February 16th 2005 | — | Oblivion |
| FASTr (oblivion, "beta") | "FASTr, a Filter Active-Set Trust-region method"; copyright line adds "Leyffer/Munson for Argonne Nationa Laboratory" [sic] | released 2.0, May 25th 2005 | Filter-SQP theory (*SIOPT* 2002) | Oblivion |
| FUNNEL, FUNNEL_EQUALITY (oblivion, "alpha") | "FUNNEL, a trust-funnel method for nonlinear optimization" | "originally released GALAHAD Version 2.1, October 17th 2007 for equalities"; "version for inequalities GALAHAD Version 2.6, July 13th 2013" | Gould & Toint, *Math. Program.* 122 (2010) 155–196, 10.1007/s10107-008-0244-7; erratum 10.1007/s10107-011-0491-x; Curtis–Gould–Robinson–Toint, *Math. Program.* 161 (2017) 73–134, 10.1007/s10107-016-1003-9 | Oblivion |
| S2QP (oblivion, "beta") | "trust-region SQP for NLP"; module header "Author: Daniel Robinson" | present at the 2018 svn import | Gould & Robinson, *SIOPT* 20 (2010) 2023–2048, 10.1137/080744542, and 2049–2079, 10.1137/080744554 | Oblivion. The 2010a paper had promised "(4) provide numerical experiments with our evolving GALAHAD package S2QP" (p.2046–2047) [stated, P, S14] |
| SQP (oblivion, "alpha") | "SQP without any globalization" | present at the 2018 import | — | Oblivion |
| TRIMSQP (oblivion) | "trimSQP: a trust-region SQP method … in which descent is imposed explicitely as an additional constraint" [sic]; "Author: Nick Gould and Daniel Robinson" | — | — | Oblivion |
| TRAL (forthcoming, "alpha") | "TRAL, a trust-region augmented Lagrangian algorithm" | released 2.5, June 25th 2012 | — | Waiting |
| FiSQP (forthcoming, "alpha") | "FiSQP, a Filter SQP method"; "originally written in Matlab by Yueling Loh and Daniel P. Robinson"; "initial Fortran translation … November 23th 2014" [sic] | 2014, header revised 2025 | Gould–Loh–Robinson, *SIOPT* 24 (2014) 175–209, 10.1137/130920599; *SIOPT* 25 (2015) 1885–1911, 10.1137/140996677 | Waiting |
| COLT (forthcoming) | "COLT: Constrained Optimization via Least-squares Targets"; Farmer, Fowkes, Gould | "initial version, GALAHAD Version 4.2, October 13th 2023" | none found | Waiting |
| EPF → EXPO (forthcoming, "beta") | "EXPO, an EXponential Penalty function algorithm" | "originally released as EPF, GALAHAD Version 5.1. May 9th 2024"; "renamed EXPO, GALAHAD Version 5.3. June 15th 2025" | none found | Waiting |
| QPF (forthcoming) | "QPF, a quadratic penalty/augmented Lagrangian function algorithm" | released 5.1, October 28th 2024 | none found | Waiting |

Sources: headers of the `.F90` files at HEAD afa13a5e (2026-09-26), `src/README.packages`, and git history [practice, P, S01].

Readings [inferred]:
- (a) After the 2003 abandonment of LANCELOT B and SQP (01 §1.7), he and his collaborators started **twelve** further general-NLP packages over 21 years. They cover at least ten distinct designs: barrier, l_p-penalty SQP, filter active-set, trust funnel, second-derivative SQP, filter SQP, trust-region augmented Lagrangian, least-squares targets, exponential penalty and quadratic penalty. There is also an unglobalized SQP and a descent-constrained trust-region SQP. None displaced LANCELOT in `src/`.
- (b) Papers were published for several of these (trust funnel, S2QP, filter SQP) while the code stayed below release grade. So **publication was not his threshold for release; robustness on CUTEst was** (compare §1.4).
- (c) Not one of these attempts is described in a paper as abandoned. The abandonments are recorded only by the directory move and the README. The practice is candid in code and silent in print, with the 2003 SIAG essay as the exception.

### 1.3 `oblivion` is also a sandbox and a comparison bench

[practice, P, S01 commit messages, verbatim]
- TR1, 2023-01-29: "started development of tr1, a first-order trust-region method ** Broken ATM".
- TR2, 2023-07-01: "introduced simple trust-region method tr2 into oblivion for comparisons".
- TR2A, 2023-07-02: "added tr2a to oblivion (may be useful, not clear yet!)".
- GSM, 2023-03-03: "Added gsm package (not for public consumption ... yet or maybe never!)".
- AGD, 2025-05-06: "add new "oblivion" package agd (accelerated gradient descent)". It went into `oblivion` on arrival. Its header says: "This is based on Algorithm 4.1 by Naoki Marumo & Akiko Takeda, "Parameter-free accelerated gradient descent for nonconvex minimization", SIAM J. Optimization 34(2) pp 2093-2120 (2024)" (Crossref 10.1137/22m1540934).

[inferred] He writes simple reference methods himself, such as a plain first- and second-order trust region or a recent accelerated-gradient paper by others, so as to have baselines in the same code base with the same linear algebra. This fits the baseline pattern in §3.1. He also parks them where users will not mistake them for recommended code.

**Implementing other people's algorithms in his own library** [practice, P]:
- TRACE, header: "a trust-region algorithm with contraction and expansion for unconstrained optimization, due to Frank E. Curtis (Leheigh U.) [sic], Daniel P. Robinson (Johns Hopkins U.) and Mohammadreza Samadi (Leheigh U.)". Released 2.6, October 23rd 2014; still in `forthcoming` [S01].
- AGD, from Marumo & Takeda (above).
- MINPACK-2 `dgqt`, "slightly modified" to serve as the baseline in the 2010 TRS paper (§3.1).
- A reimplemented BA-GMRES in the 2017 least-squares study (§3.1).

### 1.4 Test and release discipline in the code

- **Every package has the same four artefacts** [practice, P, S01; example `src/trs/`]:
  - the module (`trs.F90`);
  - a specification example (`trss.f90`, with expected output files `trsds.output` and others);
  - a comprehensive test program (`trst.F90`, plus `trsti.F90` for the C interface, `Python/test_trs.py`, `Julia/test_trs.jl`);
  - a CUTEst/SIF driver (`runtrs_sif.F90`, `RUNTRS.meta`).

  Counted in this run: 57 of the `src/` packages ship a `run*_sif.F90` CUTEst driver, and 94 ship at least one Fortran test program. Utility packages have no driver. [inferred] An optimization algorithm is built able to run on the whole CUTEst collection from the start.
- **Test programs exercise the failure paths deliberately.** Of the 120 Fortran test programs (`src/*/*t.F90`), 51 have a labelled error-exit section (the strings "error exit" or "error entries"). 73 exercise error exits or negative `status` values when symbolic `GALAHAD_error_*` checks are counted too. 48 contain a section testing the sparse storage formats [practice, P, S01; counts made in this run].

  Examples: `cqpt.F90` and `arct.F90` open with the section banner "error exit tests". `cqpt.F90` then has "special test for status = - 7" and "basic test of various storage formats". `trst.F90` runs "Error entries", then storage formats, then "Normal entries". The older `gltrt.F90` puts "Normal entries" first and "Error entries" last. This matches the 2003 statement that each test program "attempts to execute as much of the package as realistically possible" (02 E8) [stated vs practice: consistent].
- **Paper examples ship as runnable drivers.** `src/trs/trs_paper.F90` holds the 3×3 example of the 2010 TRS paper: H with entries 1, 2, 3 on the diagonal and 4 in position (3,1); c = (5,0,4), (0,2,0) and (0,2,0.0001) for the "Normal case", "Hard case" and "Almost hard case". The paper (Gould, Robinson & Thorne, *Math. Program. Comput.* 2 (2010), p.47) prints the same data and full iteration traces. `trs_paper_large.F90` builds the arrowhead-plus-middle-row Hessian that the paper's Table 2 describes for the CUTEr problem BOX. `src/rqs/rqs_paper_large.F90` is its RQS twin [practice, P, S01 + S10].
- **Code and preprint are released within days.** TREK arXiv v1: 14 Nov 2025. `src/trek` added: 17 Nov 2025 ("added new package trek"). NREK added: 23 Nov 2025 [practice, P, S01, S32]. The TREK header dates the internal code earlier: "originally released in GALAHAD Version 5.2. February 15th 2025", i.e. nine months before the preprint. The 2024 commit "imajor revision of sha to correspond with new tech report" [sic] shows the same coupling for the Hessian-approximation line (SHA first released April 8th 2013; papers in 2024 and 2025) [practice, P, S01].
- **Package headers record a history.** Examples: "development started …", "originally released …", "renamed as PDQP, GALAHAD Version 3.3, April 14th 2021", "renamed EXPO". Each header also lists principal authors (§7). [inferred] This gives each algorithm a dated provenance, like a lab notebook entry.

### 1.5 How he works day to day: commit behaviour

- **Volume and continuity** [practice, P, S01–S04]:
  - Gould authored 1,136 of 1,993 GALAHAD commits, 173 of 297 CUTEst commits, 91 of 120 SIF-collection commits and 78 of 147 SIFDecode commits.
  - GALAHAD commits by Gould per year: 38 (2018), 6 (2019), 30 (2020), 131 (2021), 214 (2022), 266 (2023), 239 (2024), 205 (2025), and 7 (2026 to 26 September).
  - Era: part-time since 2017.
- **Small, frequent, self-deprecating commits** [practice, P]. His messages include:
  - "blunder" 10 times, "bug" or "bugs" 60, "debug" 19, "oops"/"ooops" 5, "forgot" 3, "premature" 2 (word matches);
  - "repair premature commit of new trb (oops)" (2025-09-12);
  - "bug fixes from premature last commit" (2024-01-15);
  - "meson blunder 3 ... i hate these config files!!" (2024-10-30, CUTEst);
  - "a few corrections, but still on the trail of the ldlt_tpp_factor issue" (2026-08-06).

  [inferred] The candour of the published "depressing reading" and "slightly disappointed" passages carries over to the private-looking but public commit log.
- **Where the effort goes, 2021–2026** [practice, P; keyword counts over Gould's 1,136 messages, overlapping, word matches]: "test"/"tests" 108, "doc"/"docs"/"documentation" 88, "python" 76, "julia" 34, "meson" 33, "matlab" 30. The JOSS paper gives the reason: the aim was "to raise the profile of the library by increasing its potential userbase" (01 §1.6). [inferred] His largest recent investment is in interfaces, builds and documentation, not in new algorithms.
- **Division of labour** [practice, P]:
  - Of the commits to `.github/` (CI, Julia checks), 253 are by A. Montoison, 26 by Gould and 15 by Fowkes.
  - Gould writes the Fortran algorithms and the specification sheets. Others own CI and packaging.

### 1.6 Defaults versus the evidence in his own papers

- **LANCELOT steering: shipped, but off by default.**
  - The 2016 study concludes: "lancelot-steering and lancelot-steering-safe were both more efficient and reliable than lancelot on these tests" (Curtis, Gould, Jiang & Robinson, *OMS* 31 (2016), online PDF p.22). It announces: "The new package will be re-branded as Lancelot in the next official release, Galahad 2.6" (p.21).
  - The code has the option, but `lancelot_types.F90` declares `LOGICAL :: steering = .FALSE.`. The specification-file template lists `steer-towards-feasibility NO` [practice, P, S01, S12].
- **Trust-region parameters: partial adoption.**
  - The 2005 study found that the "standard" choice (η1, η2, α1, α2) = (0.25, 0.75, 0.5, 2) needed on average 20.625 iterations. The best cluster, η1 ∈ [0, 10⁻²], η2 = 0.99, α1 = 0.25, α2 = 3.5, needed 14.750 (4OR 3 (2005) p.234, Table 2 [S23]).
  - The current TRU and ARC defaults are `eta_successful = ten ** ( - 8 )` and `eta_very_successful = point9`. TRU also has `radius_increase = two` and `radius_reduce = half` [practice, P, S01].
  - So the tiny-η1 finding was adopted; the radius-change factors stayed at the "standard" values.

[inferred] New mechanisms and new parameter values enter as options, and defaults move conservatively. The record gives no reason (see Contradictions C5).

---

## 2. Test infrastructure as practice: the SIF collection and CUTEst

### 2.1 Where the test problems come from

- **Collected from users by licence.** CUTE (1995) p.126: "because of the LANCELOT licensing agreement, which requires the submission of typical problems by most users of the package, the new problems are likely to be even more user oriented than the present ones." [stated/practice, P, S26a; Bongartz, Conn, Gould & Toint, *ACM TOMS* 21 (1995) 123–160, 10.1145/200979.201043]. On December 15, 1994 the database held 738 problems (p.125).
- **Hand-encoded by Gould himself.** In the current collection (bitbucket optrove/sif, HEAD 2026-06-01; 1,542 top-level SIF files), the "SIF input:" header line credits Gould in 740 files: alone in 564, with Tyrone Rees in 96, with Irv Lustig in 16 [practice, P, S03; count made in this run]. Ph. Toint appears in 526 or more. [inferred] About half of the collection that the field uses to judge solvers was typed in by Gould.
- **Provenance recorded per problem.** Example: `HS105.SIF` says "Source: problem 105 in W. Hock and K. Schittkowski … SIF input: Nick Gould, August 1991. bug correction (line 351) Ph. Toint, May 2024" [practice, P, S03]. That is a bug found 33 years after encoding, fixed and dated in the file.
- **New problem families appear in step with his own projects** [practice, P, S03 `sif.updates`, with paper dates from the PDFs; the links are inferred]:
  - "20/Jan/09: BOX.SIF". The TRS paper was received 11 February 2009, and its Table 2 scales BOX from 10³ to 10⁷ variables [S10 p.50].
  - "17/Aug/11: DEGDIAG.SIF DEGTRID.SIF DEGTRID2.SIF DEGTRIDL.SIF". The CQP paper was received 4 September 2011, and it uses these "(contrived) large examples … for which the exact solution is available" [S11 p.138].
  - "29/Jan/11: GOULDQP1.SIF"; earlier GOULDQP2 and GOULDQP3 are in the 2013 CQP test table [S11 appendix Table A.1].
  - October 2015 to March 2016: 96 data-fitting problems whose header reads "SIF input: Nick Gould and Tyrone Rees". Of these, 60 give "Source: Problem from the NIST nonlinear regression test set" (BENNETT5, CHWIRUT1, DANWOOD…). 16 give "Source: Data from Aaron Parsons, I14: Hard X-ray Nanoprobe". Others are fits to facility data, for example "a sine using simplified muon data". Most come in pairs, a residual form and an "LS" form [practice, P, S03; count made in this run].
  - These were followed in 2019–2020 by "NE" (nonlinear-equation) variants of least-squares problems. The Gould–Rees–Scott tensor-Newton least-squares paper appeared in *COAP* 73 (2019) 1–35, 10.1007/s10589-019-00064-2.
  - Recent sources named in commits: "New data fitting problems from STFC and Diamond Light Source" (2020-01-08); "Extra least-squares/nonlinear systems problems from the scipy benchmark" (2020-01-19); "added a few logistic regression problems LR*" (2023-01-23).

### 2.2 How errors in shared test data are handled

`sif.updates` (444 lines) is a dated public log. Its section headings are: "Additions", "Corrections to problem statement", "Changes to default sizes", "Corrections to classification", "Corrections to citations or comments", "Cosmetic changes" and "Removals" [practice, P, S03]. What it shows:
- **Old versions are kept under new names, not overwritten silently.** Entries:
  - "25/May/24: HS105BUG.SIF (old, buggy HS105.SIF renamed)";
  - "29/May/24: CHARDIS02.SIF CHARDIS12.SIF SISSER2.SIF SINQUAD2.SIF (buggy CHARDIS0, CHARDIS1, SISSER, SINQUAD.SIF corrected)";
  - "14/Jun/25: … (replacements for buggy LUKVLE2.SIF, etc)";
  - "09/Dec/24: SROSENBR.SIF (added 2nd, correct, starting point)";
  - "23/Aug/22: remove DIXMAANA.SIF and replace by sparsity-accurate DIXMAANA1.SIF".

  The DANWOOD fix added "DANI* variants of the DANWOOD examples to repair an incorrect initial formulation (Bug report and correction due to Abel Siqueira, thank you!)" (commit 2019-02-18). [inferred] Published results obtained on the old problem stay reproducible.
- **Bug reporters are credited in the commit line**:
  - "multiple mods/fixes thanks to Serge Gratton & Philippe Toint" (2024-05-28);
  - "updates to classifications: thanks to Christoph Hansknecht" (2024-05-17);
  - "mistakes identified by Philippe Toint rectified" (2023-11-21) [practice, P].
- **Default sizes are kept in step with hardware.** "17/Mar/2002: Default size of all then-current variable-dimension problems raised to reflect the change in computing power since 1993" [practice, P].
- **Duplicates are pruned**: "remove HIER133B.SIF and HIER133C.SIF duplicates of HIER133A.SIF…" (21/Jun/21) [practice, P].
- **Open criticism** [observed, P]: CUTEst issue #110 (14 January 2026, J. Haffner), "CUTEst returns wrong sparsity patterns for a large number of lower-dimensional problems", is open. Only the opening post was readable; no reply was visible (see Gaps).

### 2.3 CUTEst: interfaces to other people's solvers

- **About 45 solvers are interfaced** [practice, P, S02]. The `src/` directories include algencan, bobyqa, cg_descent, cobyla, filtersd, filtersqp, highs, ipopt, knitro, lbfgsb, loqo, minos, newuoa, nomad, npsol, osqp, snopt, tron, uno and worhp. Additions keep coming: "Interface to the Uno package now provided" (2026-05-20) and "add highs as a supported package" (2026-09-27).
- **A scratch area exists here too.** `src/trial` (2026-01-16): "add trial package for trying out new ideas".
- **Test data built to exercise everything.** The CUTEst `src/test` suite uses purpose-built SIF problems `ALLINITU` and `ALLINITC` in single, double and quadruple precision [practice, P].

[inferred] The test environment is kept neutral, with competitors first-class. This matters for §3.1: when Gould compares only against his own codes in a paper, it is not because others' codes are not callable from his tools.

---

## 3. Layer 4: experiment design and execution

### 3.1 How baselines are chosen: two regimes

**Regime A: evaluation papers.** He compares against external codes, obtains them from their authors and lets the authors see the draft.

| Paper | Baselines | Procedure (verbatim where quoted) |
|---|---|---|
| Gould, Hu & Scott, *ACM TOMS* 33(2) Art. 10 (2007), 10.1145/1236463.1236465 [S21] | All serial sparse symmetric direct solvers available, including RAL's own MA57 | Table I gives "the release date of the version of the code used in our experiments". Scope limits are declared: "this study considers only serial codes … we have excluded solvers that are integrated parts of more general application software" (PDF p.2). Acknowledgments: "We would like to thank the authors of the solvers used in this study who supplied us with copies of their codes and documentation, helped us to use the software, answered our queries, and commented on a draft of this article" (PDF p.30). Effect on the field: MA57 and PARDISO "have been significantly improved since we started work on this study, partly as a result of feedback from us" (PDF p.29) [practice + stated, P] |
| Gould & Scott, *ACM TOMS* 43(4) Art. 36 (2017), 10.1145/3014057 [S22] | Direct solvers, preconditioners and Krylov codes from several groups | When a competitor's research code was unusable at scale, they rebuilt it: the BA-GMRES codes "employ automatic arrays … and they contain "stop" statements … As a result, we implemented a modified version of BA-GMRES. This also allowed us to use the stopping criteria C1 and C2 for consistency" (PDF p.17). When a code had no usable interface, it was tried on single problems and left out of the main comparison with the reason given: SYM-ILDL "offers no procedure to take that data and use it as a preconditioner … we were restricted to running individual problems one at a time" (PDF p.13) [practice, P] |
| Gould 2008 [S19] and Gould 2012 [S20] (sole author) | Four, then six, projection variants against GALAHAD's own interior-point code LSQP | Built a full module (LCF) for the evaluation. Critics' methods were added to the same module in 2012 (§4.5) |

**Regime B: method papers.** He compares the new idea against his own previous generation, or against a baseline modified to be fair. In the 2010s he also used deliberate self-built counterparts.

| Paper | New method | Baseline(s) | External code? |
|---|---|---|---|
| GLTR, *SIOPT* 9 (1999) 504–525, 10.1137/S1052623497322735 [S27] | GLTR (HSL_VF05) | Steihaug–Toint, inside the same trust-region code | no |
| Gould & Nocedal, in *High Performance Algorithms and Software in Nonlinear Optimization*, Applied Optimization, Kluwer (1998) 225–241, 10.1007/978-1-4613-3279-4_15 [S29] | Modified absolute-value norm (HSL_VF06) | ℓ2 norm and modified-Cholesky norm in the same code | no |
| Gould, Robinson & Thorne, *Math. Program. Comput.* 2 (2010) 21–57, 10.1007/s12532-010-0011-7 [S10] | TRS, RQS | MINPACK-2 `dgqt`: "we slightly modified this software to record and print required details, and to allow consistent stopping rules" (p.47) | yes, one, modified for fairness |
| Gould, Orban & Robinson, *Math. Program. Comput.* 5 (2013) 113–142, 10.1007/s12532-012-0050-3 [S11] | CQP | Four internal variants T1, T2, P2, P4. BPMPD, Cplex, HOPDM, Mosek, OOPS, OOQP, PCx and Xpress are named in the introduction (p.117) but not run | no |
| Gould & Robinson, *COAP* 67 (2017) 1–38, 10.1007/s10589-016-9886-1 [S31] | DQP | DQP variants (iterative against direct subproblem solves). A crossover with GALAHAD's CQP was tried and not presented (§4.1) | no |
| Gould, Loh & Robinson, *SIOPT* 25 (2015) 1885–1911, 10.1137/140996677 [S13] | FiSQO (Matlab) | Their own PenSQO. "We comment up front that we do not compare FiSQO to methods that use a feasibility restoration phase" (p.1903). Three reasons follow: formulations differ; restoration phases carry heuristics; and avoiding restoration is the paper's point. Then: "Since we have complete control over both algorithms, we are able to isolate any aspect of interest (e.g., the influence of b-pairs), design and perform revealing numerical tests, and confidently present the numerical results." (p.1903) | no (Cplex only as subproblem solver) |
| Curtis, Gould, Jiang & Robinson, *OMS* 31 (2016) 157–186, 10.1080/10556788.2015.1071813 [S12] | Adaptive AL with steering | Basic AL in the same Matlab code, and LANCELOT with and without steering: "Our only modification to Lancelot was to incorporate a basic form of steering … In this manner, we were also able to isolate the effect that steering had on numerical performance" (online PDF p.11) | no |
| Gould, Leyffer & Toint, *SIOPT* 15 (2004) 17–38, 10.1137/S1052623403422637 [S34]; Gould, Sainvitu & Toint, *SIOPT* 16 (2005) 341–357, 10.1137/040603851 [S35] | Multidimensional filter; filter trust region | LANCELOT B (both papers); NITSOL (2004). Taken from the codes named in the numerical sections, which were not read in detail | NITSOL only |
| Gould, Rees & Scott, *COAP* 73 (2019) 1–35, 10.1007/s10589-019-00064-2 [S36] | Tensor-Newton | Gauss–Newton and Newton "found in our RALFit" library | no |
| Al Daas & Gould, arXiv:2511.11135 (v1 2025, v3 2026) [S32] | TREK | TRS (2010) and GLTR (1999), "from the same library"; same compiler flags and the same MA57 factorization | no |

Readings [inferred]:
- (a) In method papers the baseline is almost always **his own earlier code, run under identical linear algebra, stopping rules and hardware**. The single external baseline (`dgqt`) was edited to match stopping rules. The stated rationale is control and isolation.
- (b) The 2013 CQP paper argues from the literature that "insufficient numerical evidence of the above algorithms is a gross oversight" (p.118), yet it runs none of the commercial QP codes it lists. This sits against the stated rule "experience with the best competitive algorithms on the same non-trivial problems" (02 E2); see Contradictions C1.
- (c) External comparisons do happen, but in dedicated evaluation papers, often with J. A. Scott, where the other codes' authors are brought in.

### 3.2 How test sets are built: explicit, stated filters

[practice, P; each rule is quoted from the paper named]

1. **Take a whole collection, then filter by a stated structural criterion.**
   - "all the unconstrained problems contained in the CUTEr test set; we restrict our attention to those problems involving 2000 or fewer variables, since the dense Cholesky factorization used by dgqt struggles with larger cases, and this leads to 97 examples" (S10 p.49). The filter is chosen to be fair to the baseline.
   - CUTEst problems "that have at least one general constraint and at most 1000 variables and 1000 constraints", then "at most 10,000" for LANCELOT (S12 PDF p.13, p.22).
   - TREK: "the set of 96 unconstrained test problems in the current release (2025-09-09) of the CUTEst … that have 1000 or more variables" (S32 v1 p.14). v3 says 93, with no explanation (Contradictions C7).
2. **Remove near-duplicates.** "multiple instances of very similar nature have been excluded" (S11 p.135; near-identical wording, "multiple instances of similar nature were excluded", in S31 p.29); "removed "duplicates" (that is, similar problems belonging to same group), leaving a single representative" (S22 PDF p.4).
3. **Filter to non-trivial problems with a cheap baseline.** For least squares: of 921 matrices, keep those for which unpreconditioned LSMR did not converge "within 100,000 iterations or required more than 10s (when run on a single processor)", leaving 83 (S22 PDF p.4).
4. **Profile only what at least one method solves, and say so.**
   - "Since there is little point in comparing the variants on problems for which all fail, we restrict ourselves to the 77 out of the 120 problems that were solved by at least one variant" (S19 p.9).
   - The same rule appears in S12 (323 of 383; 364 of 457) and S13.
5. **Exclude with a named reason.**
   - "problem HS87 has been removed from the test set, since the objective function is not continuous" (S15 p.2073).
   - Problems where "the Cplex solver "hung"" (S13 p.1905).
   - Problems with "a failure in the subproblem solver or a value signaling a function evaluation error since they did not necessarily give any useful information about the algorithms" (S13 p.1906).
   - FLOSP2* and SEMICON1 "because their solution appears to require more specific preconditioning", and CHEMRCTA/B "because they seemed to generate numerical overflow with all the tested methods" (S34 footnote, p.24).
   - COPS robot1 for evaluation errors, and four problems that hit the 3600 s limit for every solver (S12 PDF p.16).
6. **For expensive sweeps, pick a small hard subset and justify it.** "We have chosen to test the algorithm on a set of 24 problems from the CUTEr collection … These problems have proved to be reasonably hard in the past and are, in our opinion and despite their fairly uniform dimensions, reasonably representative of the unconstrained part of the collection as a whole. … The number of problems in our test set had to be kept relatively low in order to make the test for a large number of parameter values tractable." (S23 p.231). Footnote: "On easy problems, the influence of the parameters is less prominent."
7. **Use small, dense problems only at the early stage, and say that is the stage.** "The HS test suite is comprised of generally small and dense problems that are very useful during early stages of code development; the small size of the problems allows for relatively careful inspection of each problem." (S15 p.2073). The results are labelled "preliminary". See Contradictions C2: elsewhere the record distrusts HS-based evidence.

### 3.3 How test instances are generated

- **Mid-run subproblems, not start-point ones.** "Our test examples are generated by running Algorithm 6.1 on the CUTE set for 10 iterations and taking the trust-region subproblem at iteration 10 as our example. The idea here is to simulate the kind of subproblems which occur in practice, not those which result at the starting point for the algorithm, as such points frequently have special (favorable) properties." (S27 p.518) [practice + stated, P]
- **Verify the "best" value independently.** In GLTR, "a factorization of H + λM was used to confirm that the matrix was positive semidefinite" (S27 p.518) [practice, P].
- **Start-point data when the solver is the object** [practice, P]:
  - TRS: c = ∇f(x₀) and H = ∇²f(x₀), radius 1, the same initial λ = 0 for both codes (S10 p.49).
  - TREK: the same generation, followed by warm-started re-solves at smaller radii (S32).
- **Hand-made 3×3 cases for the pathological regimes**, easy, hard and "nearly hard", with every iteration printed for both codes (S10 p.47–49), and shipped as `trs_paper.F90` (§1.4) [practice, P].
- **Contrived large problems with known solutions to test accuracy.** "The solutions to most of our test problems are not known exactly, so we illustrate how our methods work on a few (contrived) large examples, DEGDIAG, DEGTRID, DEGTRID2 and DEGTRIDL" (S11 p.138). These were added to the SIF collection by Gould (§2.1) [practice, P].
- **Worst-case constructions checked by plotting.** The 2010 complexity paper builds one- and two-dimensional examples by Hermite interpolation and plots f and its first three derivatives: "this figure confirms the properties inherited from the construction of the function f(x), namely, that it is twice continuously differentiable and has uniformly bounded second derivatives" (Cartis, Gould & Toint, *SIOPT* 20 (2010) 2833–2852, 10.1137/090774100, p.2842) [practice, P, S25].

### 3.4 Controlled ablation

[practice, P]
- **LANCELOT with and without steering.** One mechanism was changed; the multiplier updates were left alone. The same success criteria were used for all three variants: "Importantly, these criteria for deeming a problem to have been solved, were used by all three variants described above" (S12 PDF p.21).
- **FiSQO against PenSQO.** "the only difference between the two methods is in the step acceptance criteria" (S13 p.1903). The paper then measures how often its new mechanism fires ("for (32 + 11)/(301 + 66) ≈ 12% of the problems, b-pairs … were computed", p.1907).
- **S2QP.** Three variants that differ in the accelerator step and the penalty update (S15 p.2073).
- **CQP.** Two residual trajectories × two approximation degrees (S11 p.135).
- **GLTR.** Stopping after the Steihaug–Toint point plus 1, 5 or 10 iterations, against running to the best value (S27 Tables 6.4–6.5).

### 3.5 Parameter studies

[practice, P, S23; Gould, Orban, Sartenaer & Toint, *4OR* 3 (2005) 227–241, 10.1007/s10288-005-0065-y]
- **Two-stage grid.** A coarse uniform grid comes first. Then: "Preliminary experiments using the grids … seemed to indicate that the region … was worth being discretized more finely as it appeared to be where the best efficiency would occur" (p.232). The result was 3,960 parameter tuples × 24 problems = "a grand total of 95,040 test runs" on one PC.
- **One parameter left out, with a reason.** The initial radius follows LANCELOT; "We did not perform a sensitivity analysis on this parameter because this issue has already been considered in Sartenaer (1997)" (p.231).
- **A failure rule that never fired, reported anyway.** "We had intended to declare failure when (8) was not met in the first 1000 iterations of the algorithm, but this situation never happened in our tests." (p.230)
- **Adaptive-parameter follow-up with a visitor.** Gould, Porcelli & Toint, "Updating the regularization parameter in the adaptive cubic regularization algorithm", *COAP* 53 (2012) 1–22, 10.1007/s10589-011-9446-7 [S24; abstract and introduction read]. The ARC package header names "Principal authors: Nick Gould and Margherita Porcelli", "originally released GALAHAD Version 2.5. May 13th 2011" [S01].

### 3.6 How numerical trouble is debugged

- **Instrument the failure, then attack its cause.** Gould, Hribar & Nocedal, *SISC* 23 (2001) 1376–1395, 10.1137/S1064827598345667 [S30]. The paper plots, on CUTE CVXQP3, the null-space residual norm and "the cosine of the angle between the preconditioned residual g and the rows of A. Note that this cosine, which should be zero in exact arithmetic, increases and indicates that the CG iterates leave the constraint manifold Ax = b" (p.1382).

  A candidate remedy that failed is reported as such: "The first is to use fixed-precision iterative refinement … This, however, will generally be unsuccessful … We have performed numerical tests and found no improvement from this strategy." (p.1386) The paper's structure is: failure example (§3), error analysis (§4), iterative refinement (§5), residual update (§6), then numerical results (§7) [practice, P].
- **Dissect the worst case.** The TRS paper prints the full λ trace for its worst problem ("The worst performance is for problem GROWTHLS, and in detail we see the following for TRS", p.49) [practice, P, S10].
- **Test cheaper diagnostics, and admit their limits.** Dependent constraints are removed via an LBLᵀ factorization: "We recognize that this is not as robust as, for example, a singular-value decomposition or a rank-revealing QR factorization, but fortunately has proved remarkably reliable in our tests." (S19 p.8) [practice + stated, P]
- **Leave the trail in the code history.** Commits such as "still on the trail of the ldlt_tpp_factor issue" (2026-08-06), "try to debug bgo actions error" (2025-11-25) and "blunder with qpat fix ... try again" (2024-06-06) [practice, P, S01].

### 3.7 Reproducibility artefacts

[practice, P]
- **Full per-problem tables in online supplements.** Examples: Gould 2008 (Appendix 1: all four variants; Appendix 2: LSQP) [S19]; Gould 2012 (Appendix A) [S20]; CQP 2013 (Appendix A, problem statistics with degeneracy flags R/C/B per problem; B, decoding settings; C, parameter settings) [S11]; FiSQO (the technical report's problem-by-problem tables) [S13]. In TREK, the per-problem table is Appendix C in v1 and Appendix D in v3 [S32].
- **The environment's own limits published as settings.** The CQP appendix B lists the CUTEr static array sizes needed ("PARAMETER ( NMAX = 1000000 )" and so on). This is the same inflexibility CUTEst later removed (01 §2.B) [S11 supplement p.13].
- **Hardware, compiler, flags and linear solver stated every time.** Examples: S10 p.50; S11 p.135; S12 PDF p.22; S32 v1 p.14 ("four cores of a PC with sixteen Intel Core i9-9900 CPU 3.10GHz processors … -Ofast … HSL MA57").
- **Competitor versions dated** (S21 Table I).

---

## 4. Layer 5: judging results

### 4.1 Negative and surprising results are printed, including in signature works

[practice + stated, P]
- **GLTR (1999)**, now one of his most cited papers, closes: "We must admit to being slightly disappointed that the new method did not perform uniformly better than the Steihaug–Toint scheme, and we were genuinely surprised that a more accurate approximation does not appear to significantly reduce the number of function evaluations within a standard trust-region method, at least in the tests we performed. While this may limit the use of the methods developed here, it also calls into question a number of other recent eigensolution-based proposals for solving the trust-region subproblem" (S27 p.522). **The negative result is turned into a test that others' methods must also pass.**
- **Gould & Nocedal (1998).** The results table shows the new norm failing (">1800 secs.") on EIGENALS, MSQRTALS, SPARSINE and SPMSRTLS. The text sorts the test problems into three categories, including one where "These indicate the limitations of our approach" (preprint p.11). The conclusion is bounded: "We do not pretend that (3.15) is uniformly appropriate, but suggest that, at the very least, its use should be considered when a problem is know to be ill-conditioned." [sic] (preprint p.13) [S29].
- **Projection methods (2008).** A negative evaluation built on a production module. That module (LCF) is now in `oblivion` (header: "originally released with GALAHAD Version 2.0.July 20th 2006") [S19, S01].
- **DQP (2017).** An experiment kept out of the paper is still reported in its conclusions: "Although not presented in this paper, we experimented with using DQP as the second stage of a cross-over method … Our tests showed that DQP was not especially effective in this capacity." (S31 p.35)
- **CQP (2013).** "We have experimented with the other residual trajectories … with mixed success. Although each proves to perform well (and sometimes exceptionally so) in some cases, none proves to be as reliable as the simple linear and quadratic ones we have focused on here." (S11 p.138)
- **Design beliefs revised by data.** "while our initial instinct was not to provide special code to cope with gradual active-set changes, we are now convinced that there should be some provision to update factorizations if requested." (S31 p.28)

### 4.2 Claims are scoped to what was tested

[stated, P]
- "It is important to emphasize that we are not claiming that FiSQO is better than a flexible penalty-SQO approach but rather that FiSQO appears to be better than a standard penalty-SQO approach." (S13 p.1906)
- "We should be cautious not to infer too much from these examples, particularly as dgqt was originally designed to terminate fast with a low-accuracy but usable solution." (S10 p.49)
- "We did not expect any of the methods tested to be an overall winner, and indeed this is the case." (S32 v1 p.15, kept in v3); and "Unsurprisingly, the new method is not always the best, but in some cases it is." (v1 p.16, kept in v3)
- On the effect of steering across test sets, the optimal-power-flow results: "Interestingly, these results suggest more benefits for steering in the line search algorithm than in the trust region algorithm, which is the opposite of that suggested by the results in Section 3.1.3" (the COPS results) (S12 PDF p.19). The inconsistency is reported, not resolved.

### 4.3 How claims change between versions

- **TREK, arXiv:2511.11135 v1 (14 Nov 2025) and v2 (21 Jan 2026) against v3 (2 Mar 2026)** [practice, P, S32; the version texts were compared in this run]:
  - Abstract, v1/v2: "the solutions to such subproblems lie on a manifold of approximately very low rank". v3: "the solutions to such subproblems effectively lie in a very-low-dimensional subspace". The claim is restated in more precise terms.
  - Experiments redesigned. v1 used radii Δ = 1 then 0.5, an iteration bound m = 100, and 96 problems. v3 has two regimes (Δ₀ = 10 → 1 → 0.1, and Δ₀ = 1 → 0.1), m = 300 and 93 problems. v3 adds a paragraph checking a theoretical prediction: "Significantly, and as predicted in the motivating justification in Section 3, the left-hand figure in Figure 7.1 seems to indicate that including A⁻ᵏb terms in the approximating subspace is advantageous when Δ is large" (v3 p.15; notation re-typed from the PDF). The v1 text had no such check.
  - v3 adds a re-solve analysis ("in only six of ninety three cases examined were any further extended Krylov iterations necessary", p.10), a section on elliptical norms, and "The authors appreciate the helpful comments from two reviewers of this paper." (p.16)
  - [inferred] The reviewers pushed for a test of the regime the theory singles out. The authors answered with a new experiment, not with argument.
- **ARC.** The preprint title "cubic overestimation" (RAL-TR-2007-007) became "cubic regularisation" in *Math. Program.* 2011. The reason is not stated (01 §2.E) [S].
- **Adaptive AL.** arXiv:1408.4500 v1 (20 August 2014, 46 pages) already contains the LANCELOT-with-steering experiment (§3.2 of v1). The journal version (30 pages) moves the proofs and detailed tables to a technical report ("further information can be found in [17, Appendix 3]", online PDF p.11). The experimental design did not change between preprint and journal [practice, P, S12, S12a].
- **Trust funnel (2010).** The journal paper has no numerical section. The abstract still says "Preliminary numerical experiments on CUTEr problems indicate that the method performs well". The only pointer to numbers is Remark 8, which cites the Namur report 07/2 (not read) for "Preliminary numerical experience" of a Maratos effect (p.194). The conclusion says: "On a more practical level, extensive numerical testing of the ideas presented here is necessary. These tests are ongoing, and preliminary results are encouraging." (S16 p.195) The FUNNEL code dates from 17 October 2007, before the paper's acceptance on 20 June 2008. It ended in `oblivion` (§1.2) [practice, P].

### 4.4 How his own errors are corrected

[practice, P]

| Error | Discovery | Repair | Time |
|---|---|---|---|
| CGT 1988 bound-constrained TR, active-set identification proof | not stated | *SINUM* 26 (1989) 764–767, 10.1137/0726044, new proof (01 §1.7) | about 2 months to submission |
| Trust funnel, Lemma 3.10 | "an error was unfortunately discovered during work with D. Robinson" (Erratum, *Math. Program.* 131 (2012) 403–404, 10.1007/s10107-011-0491-x, p.403) | A separate report with Robinson. The 2017 interior-point trust funnel builds on the method "originally described in [23], and then corrected in [22]" (S18 p.75) | — |
| Constrained complexity, Lemma 3.5 (*Math. Program.* 144 (2014) 93–106, 10.1007/s10107-012-0617-9) | not stated | Corrigendum, *Math. Program.* 161 (2017) 611–626, 10.1007/s10107-016-1016-4: "the result of the lemma is false", and the bound is restored "for a different, scaled measure of first-order criticality" | received 11 November 2014, accepted 31 March 2016. The authors "thank Ernesto Birgin, John Gardenghi, Jose-Mario Martinez and Sandra Santos for discussing the issue with them while this correction was being polished" (p.626) [S26] |
| SIF test problems (HS105, CHARDIS0/1, SISSER, SINQUAD, LUKVLE2/4…) | named colleagues, 2019–2025 | new file names; the old versions are kept or renamed (§2.2) | days |

[inferred] The pattern: correct in public, in the same venue or log, as a separate short item; rebuild a weaker or different result instead of withdrawing; and credit whoever found or discussed the error. That includes a group (Birgin, Martínez et al.) working on the same complexity questions.

### 4.5 How criticism is answered

- **Censor et al. (2012) on his 2008 projection paper.** Gould, "How good are extrapolated bi-projection methods for linear feasibility problems?", *COAP* 51 (2012) 1089–1095, 10.1007/s10589-011-9414-2 [S20, sole author]. What he did [practice, P]:
  1. Put the critics' recommended methods into the same code: "We modified the GALAHAD fortran 2003 package LCF, which we previously used to obtain the results reported in [7], to include additionally the EAPM and EPPM methods" (p.1092).
  2. Used the critics' best parameter and checked robustness to it: "We used the value ρ = 1.8 that appears to work best in the experiments in [1], but note that we observed quantitatively similar results with other ρ including ρ = 1." (p.1092)
  3. Conceded in the first finding: "Figure 1 confirms that the authors of [2] are correct in saying that EAPM and EPPM are better than those discussed in [7]." (p.1092)
  4. Reproduced the critics' random experiments and admitted his own tool's weakness: "we didn't have their pseudo-random number generator, but used that from GALAHAD instead, and we had to be content with systems of order 700 by 300 since the factorization code we used was (we discovered) poorly designed for dense problems." (p.1093)
  5. Kept the conclusion, and ended by asking for software: "We would welcome the development of generally applicable software to implement such ideas." (p.1094)
  6. Published because an editor pressed: "The authors is grateful to Bill Hager for encouraging him to publish these follow-up results" [sic] (p.1094).
- **Pre-empting known objections.** Gould & Nocedal (1998) cite the 1981 NATO discussion of Goldfarb's proposal: "In particular Roger Fletcher (Dundee) expressed concern that the distortion induced by (3.5) and (3.9) may be substantial. We accept that (3.15) may not be as desirable as (3.1), but believe that while (3.1) is out of the question for most large-scale problems, (3.15) is practical, and often useful, for many of them." (preprint p.13) [stated, P, S29]
- **Software review (JOSS 2022–23).** The GALAHAD 4.0 review (openjournals/joss-reviews #4882, opened 26 October 2022; reviewers F. E. Curtis and J. A. J. Hall; archive DOI 10.5281/zenodo.8075232) ended in acceptance. The comment threads were **not readable** (see Gaps). The paper's git diff from the pre-review draft (5 April 2022) to the final (23 June 2023) shows only small textual fixes and additions to the package table (`llsr`, `llst`) [practice, P, S01 `doc/paper_v4/paper.md`, S05].

### 4.6 When the theory runs ahead of the code

[practice, P]
- **The 2017 interior-point trust funnel has no numerical results.** It is 62 pages (S18). Its introduction assesses the second-derivative SQP line, citing refs [19–21], the three Gould–Robinson S2QP papers, and [29], Morales–Nocedal–Wu: "Preliminary results when solving small- to medium-sized problems are promising, but their effectiveness on large problems has not yet been confirmed." (p.74–75) This is Gould and Robinson, among the co-authors, assessing their own S2QP work in print. The manuscript was received in December 2013, about four years after the S2QP papers.
- **S2QP.** A "companion paper" gave "preliminary numerical results on the Hock and Schittkowski test set" (S15 p.2049, abstract). The large-scale S2QP experiments promised in 2010a (§1.2) were not found among the SQP titles in his publication list. The code is in `oblivion`.

[inferred] In the 2008–2017 constrained-optimization work, several papers stop at theory plus preliminary numbers, and the software never reached release. See Contradictions C3 against his stated taste (02 T2).

---

## 5. Ledger: promises, abandonments and what happened

| Year | Promise or plan (source) | What the record shows |
|---|---|---|
| 2003 | "turned to … sequential barrier-function minimization" (SIAG/OPT, 01 §2.D) | SUPERB: development 21 October 2002, released 2005, now in `oblivion` [S01] |
| 2003 | "next-generation SQP solvers we intend to introduce in Version 2 of the library" (GALAHAD 2003, 01 C1) | LPSQP 2005, S2QP, SQP and TRIMSQP in `oblivion`; FiSQP (2014) in `forthcoming` [S01] |
| 2008 | ARC bound-constrained variant | BARC in `forthcoming` since February 7th 2008 [S01] |
| 2008 | "extensive numerical testing … These tests are ongoing" (trust funnel, S16 p.195) | FUNNEL in `oblivion`; the 2017 extension is theory only [S01, S18] |
| 2010 | "provide numerical experiments with our evolving GALAHAD package S2QP" (S14 p.2047) | Small HS tests only (S15). S2QP in `oblivion` |
| 2010 | TRS paper: "We leave a more general comparison between direct and iterative approaches … to follow-up work" and "We plan to update the relevant GALAHAD packages GLTR and GLRT to take account of this" (S10 p.52) | The direct-versus-iterative comparison appears 15 years later as TREK against TRS against GLTR (S32). Whether GLTR/GLRT were updated was not checked |
| 2016 | Steering "re-branded as Lancelot in the next official release, Galahad 2.6" (S12 PDF p.21) | Shipped as an option, off by default [S01] |
| 2016 (README) | `forthcoming`: "let us know" to move packages up | TRB, UGO, BGO, DGO, LHS and TREK were promoted (2021–2025). No record of why these and not others (Gaps) |
| 2025 | TREK/NREK "will be rolled out as optional subproblem solvers in other GALAHAD packages in due course" (S32 v3 p.16) | Not checked (too recent) |

---

## 6. Layer 6: how papers are put together (practice)

- **The experiment section opens with explicit questions.** GLTR (S27 p.517): "First, can we obtain significantly better values of the model by finding better approximations to its solution than the Steihaug–Toint method? And second, do better approximations to the minimizer of the model necessarily translate into fewer iterations of the trust-region method?" The two subsections answer them in order [practice, P].
- **Software and experiments sections name the package and the library version:**
  - "implemented as a pair of thread-safe Fortran 95 packages—respectively, TRS and RQS … as part of version 2.3 of the GALAHAD optimization library" (S10 p.46);
  - "An implementation, CQP, is available as part of GALAHAD" (S11 abstract);
  - "implemented both Algorithms 3.1 and 3.2 as a Fortran 95 module LCF … as part of the upcoming release 2.0" (S19 p.7).

  The code often exists before the paper is submitted (FUNNEL, TREK, ARC) [practice, P].
- **Preliminary numbers are labelled as preliminary.** Examples are S15 ("Preliminary testing") and S16 ("Preliminary numerical experiments") [practice, P].
- **Acknowledgments credit referees for changes to the numerics.** "We are extremely grateful to a referee and associate editor for comments that lead to important clarifications of our numerical results." (S11 Acknowledgments) [practice, P]
- **Ideas are credited to meetings.** The trust funnel: "the ICNAO2006 conference in Beijing, which provided an excellent environment for the derivation of some of the results presented here", and discussions at CERFACS "with S. Gratton, D. Orban and A. Sartenaer" (S16 p.195) [stated, P].

---

## 7. Layer 7: research organisation (practice)

- **Visitors and junior colleagues become co-authors of the code, not only of the paper.** Package headers name them [practice, P, S01]:
  - ARC: "Nick Gould and Margherita Porcelli" (2011);
  - S2QP: "Daniel Robinson";
  - TRIMSQP: Gould and Robinson;
  - FiSQP: "Nick Gould, Yueling Loh and Daniel P. Robinson";
  - SHA: "Jaroslav Fowkes & Nick Gould" (2013);
  - COLT: "Jessica Farmer, Jaroslav Fowkes and Nick Gould" (2023);
  - TREK: "Hussam Al Daas and Nick Gould" (2025).

  [inferred] Collaboration is organised around a package in his library. A Matlab prototype by a collaborator (FiSQO) is translated into Fortran by Gould (FiSQP, 2014).
- **Long-term personal maintenance.** He is the largest committer to all four repositories (§1.5), eight years after the move to GitHub and part time [practice, P].
- **A small software team with divided roles** [practice, P, S01 commit authors and messages]:
  - Montoison: CI, meson and Julia; 342 of his 798 commit messages mention "julia", "meson", "CI" or "workflow".
  - Fowkes: Python wheels and PyPI publishing, including "[CI] Add more workflows to help Nick (#534)".
  - Orban: build and CI fixes.
  - Gould keeps the Fortran algorithms and documentation.
- **Test infrastructure run as a community service with a public log** (§2.2) [practice, P].
- **Student supervision: no process evidence found in code or papers** beyond non-alphabetical author order (01 §0). See Gaps.

---

## 7b. Layers 1–3 (taste, problem choice, idea generation) as they show in practice

This agent's brief is behaviour. The items below are what the code and the papers show about layers 1–3. The stated versions are in note 02.

- **Layer 1, taste: the release bar is robustness on the whole collection, not a publication** [practice, P, S01].
  - Subproblem and QP solvers pass the bar. TRS, RQS, GLTR, GLRT, DPS, CQP, DQP, BQP and TREK are all in `src/`.
  - General-NLP solvers do not pass it (§1.2).
  - Named methods by others are kept in `forthcoming` (TRACE) or `oblivion` (AGD) until they prove themselves in his harness.
- **Layer 2, problem choice: problems come from the library's own needs** [practice, P].
  - TRS and RQS supply the subproblem solvers for ARC and trust-region methods (S10).
  - DQP is pitched as "an attractive option as the subproblem solver in the recently developed inexact SQO method called iSQO" (S31 p.35).
  - TREK "adds a further tool to the arsenal of solvers that trust-region and cubic-regularization methods … rely on" (S32 v3 p.16).
  - Another source is criticism of his own evaluations (§4.5).
- **Why now, as the papers put it** [stated, P]:
  - TRS 2010: "We are encouraged here as the sparse-matrix factorization technology has advanced rapidly of late, and both parallel/multi-core and out-of-core factorizations are now available" (S10 p.52). New hardware and tools in the neighbouring field reopen an old subproblem.
- **Layer 3, idea generation: revisit and unify** [stated/practice, P]:
  - "Our aim has been to revisit the popular Gay-Moré-Sorensen [21,38] algorithm(s) for the direct solution of the trust-region subproblem and to provide flexible modern software" (S10 p.52).
  - CQP: "we combine ideas from Zhang [51], Stoer and Wechs [42,43], Stoer, Wechs, and Mizuno [44], and Sun and Zhao [53] into a single cohesive framework" (S11 p.120).
  - This matches the ARC origin in note 01 §2.E, "unify and extend these contributions". Meetings and visits appear as incubators (§6: ICNAO2006, CERFACS).

## 8. Stated method (note 02) against observed practice

| Stated (02) | Practice found here | Verdict |
|---|---|---|
| E1: test on many problems; small sets bias | Whole-collection subsets of 97–457 problems; the 24-problem subset is justified as a trade-off (§3.2) | consistent |
| E2: compare with "the best competitive algorithms on the same non-trivial problems" | Evaluation papers do this (§3.1 A). Method papers compare against own earlier code or self-built counterparts (§3.1 B). CQP 2013 names 8 commercial or academic QP codes and runs none | **partly contradicted** (C1) |
| E3: public test data | SIF collection public, with a correction log; supplements list every problem | consistent |
| E4: use defaults, no per-problem tuning | "default values for most control parameters" with the exceptions listed (S11 p.135; S12) | consistent |
| E5: parameters matter; measure them | 95,040-run sweep; but defaults change conservatively (§1.6) | consistent in study, partial in adoption (C5) |
| E8: test programs execute as much of the package as possible | 51 of 120 test programs have a labelled error-exit section; 73 exercise error statuses (§1.4) | consistent |
| J2/R3: small and random evidence misleads; SIQP's popularity rests on small HS evidence | S2QP's only numbers are on the HS set (S15), labelled preliminary and justified as early-stage | **tension** (C2) |
| T2: "too many papers presenting convergence proofs for algorithms that have never been and will probably never be properly implemented" | 62-page theory-only interior-point trust funnel (2017); trust-funnel numbers deferred to a report; code for both in `oblivion` | **tension** (C3) |
| J5: rerun the critics' variants and concede what they show | Done exactly, in the same code (§4.5) | consistent |
| R12: report negatives and own failures | Printed in papers (§4.1), logged in code (`oblivion`), corrected in errata (§4.4). But no paper announces the abandonment of SUPERB, FUNNEL or S2QP | consistent, but the abandonments show only in code |
| O2: build a library of interrelated packages | Every method paper since 1999 ships a package; the pipeline tiers (§1.1) | consistent |
| F1–F2: LANCELOT B and SQP abandoned in 2003 | Twelve later general-NLP packages; none released (§1.2) | **the "abandonment" was of a route, not of the goal** (C4) |

---

## Contradictions (kept, not reconciled)

- **C1. Comparison with the best competitors, stated against practised.**
  - Stated in 1994 and 1996, co-authored: test against "the best competitive algorithms on the same non-trivial problems" (02 E2).
  - Practised in 1999–2025 method papers: the baseline is his own earlier package, or a self-built counterpart (§3.1 B).
  - The 2013 CQP paper calls "insufficient numerical evidence … a gross oversight" (p.118) while running only internal variants.
  - The 2015 FiSQO paper states the reasons for not comparing externally (p.1903).
  - Both regimes are real. The evaluation papers (2004, 2007, 2017, with Scott) do compare externally.
- **C2. Small test sets.**
  - GOT 2005 blames SIQP's popularity on "favourable empirical evidence accumulated on small-scale problems (Hock and Schittkowski 1981)" (02 J2).
  - S2QP 2010 reports only HS results, calling them useful "during early stages of code development" (S15 p.2073). No later-stage S2QP experiments were found in his publication list.
- **C3. Theory without implementation.**
  - The stated taste criticises proofs for algorithms "never … properly implemented" (02 T2).
  - The 2017 interior-point trust funnel (62 pp., no numerics) and the 2010 trust funnel (numerics deferred to a report) are theory-led. Code exists for both lines (FUNNEL, with an inequality version in 2013), but it is cast into `oblivion`. Whether that code implements the 2017 algorithm is **not known**.
- **C4. "Abandoned" SQP and barrier routes against a 21-year stream of attempts.** 2003: "we have now all but given up our SQP developments" (01 C1). Afterwards came LPSQP (2005), S2QP, TRIMSQP and FiSQP (2014), plus barrier (SUPERB 2005), funnel, AL and penalty variants up to 2025 (§1.2). None was released.
- **C5. Evidence against defaults.**
  - Steering was "more efficient and reliable" (S12 PDF p.22) but is off by default (`steering = .FALSE.`).
  - Radius-update factors stay at the values the 2005 study called not the best, although η1 did move to 10⁻⁸ (§1.6).
- **C6. Steering results across test sets.** The optimal-power-flow results favour steering more for line search than for trust region, "the opposite of that suggested by the results in Section 3.1.3" (COPS), and the paper leaves it so (S12 PDF p.19).
- **C7. TREK problem counts.** v1 uses "96 unconstrained test problems … that have 1000 or more variables" from the release of 2025-09-09. v3 uses 93 from the same release, with no explanation (S32).
- **C8. Stated abandonment of LANCELOT's approach against current investment.** 2003: "the limit of what might be achieved by augmented Lagrangian methods such as LANCELOT A had probably been reached" (01 D). Since then: LANCELOT re-engineered with steering (2014–16); commits "significant updates to expo, trb and lancelot" (2025-09-12); and TRAL (2012) and QPF (2024), both augmented-Lagrangian, in `forthcoming`.

## Gaps (what could not be found or read)

- **GitHub issue and review discussions.** WebFetch returns only the opening post of GALAHAD and CUTEst issues. The repository-scoped GitHub API is not enabled for this session. So Gould's replies to bug reports (for example CUTEst #110 on sparsity patterns; GALAHAD #341, a Julia user's QPA questions) and the JOSS review comments by Curtis and Hall were **not read**. This is the largest gap for "how he answers criticism" in software.
- **Rejected papers and referee reports**: none public. No OpenReview record exists; he does not publish at ML venues.
- **Why packages were promoted or abandoned.** Only the directory moves, and the 2016 and 2021 READMEs, record the decisions. No note explains why SUPERB, FUNNEL or S2QP failed. `src/changes` turned out to be a code-migration checklist ("Files "really using pointers""), not a decision log. The pre-2018 CCPForge svn history is not public.
- **Numerical reports not read**: the trust-funnel Namur report 07/2 (the numbers behind the 2010 abstract); the FiSQO technical report tables; the COR@L 14T-006 report appendices for the adaptive AL paper; the LANCELOT-versus-MINOS report RAL-TR-97-054 (unextractable fonts, see 01).
- **Early versus final versions** were compared only where two public versions exist: TREK (arXiv v1/v2/v3) and adaptive AL (arXiv v1 against journal). Most of his papers have no arXiv version: technical reports first, arXiv only from 2014 (01 §1.4).
- **GLTR/GLRT updates promised in 2010** were not checked in the code history.
- **Talks, lab notebooks, student recollections of his debugging habits**: none found. Mentorship process is agent 04's dimension.
- **The share of the SIF collection encoded by Gould** is counted from the "SIF input:" header line only. Problems encoded before headers were standardised may be under-attributed.

## Sources

Code repositories (primary, practice)
- S01 · GALAHAD, ralna/GALAHAD, full git history (1,993 commits, 2018-02-03 to HEAD afa13a5e, 2026-09-26): `src/README.packages`, `src/forthcoming/README.forthcoming`, `src/oblivion/README`, headers of all `forthcoming` and `oblivion` packages, `src/trs/trs_paper*.F90`, `src/lancelot/lancelot_types.F90`, `src/tru/tru.F90`, `src/arc/arc.F90`, 120 `*t.F90` test programs, `doc/paper_v4/paper.md` history, `.github/`, https://github.com/ralna/GALAHAD · P
- S02 · CUTEst, ralna/CUTEst, full git history (297 commits, HEAD 733acc7, 2026-09-27): `src/` interfaces, `src/trial`, `src/test`, https://github.com/ralna/CUTEst · P
- S03 · SIF test-problem collection, optrove/sif (120 commits, HEAD 29adac9, 2026-06-01): `sif.updates`, problem headers (1,542 top-level SIF files), https://bitbucket.org/optrove/sif · P
- S04 · SIFDecode, ralna/SIFDecode (147 commits, HEAD 979967c, 2026-07-06), commit authorship only, https://github.com/ralna/SIFDecode · P
- S05 · JOSS review thread for GALAHAD 4.0, openjournals/joss-reviews #4882 (opened 2022-10-26), metadata only, comments **not read**, https://github.com/openjournals/joss-reviews/issues/4882 · P
- S06 · GALAHAD issue list filtered by commenter nimgould (titles only), and issue #341 and #371 opening posts, https://github.com/ralna/GALAHAD/issues · P
- S07 · CUTEst issue list filtered by commenter nimgould (titles only), and issue #110 opening post (J. Haffner, 2026-01-14), https://github.com/ralna/CUTEst/issues/110 · P (observed)

Papers and preprints (primary; experimental sections read unless noted)
- S10 · N. I. M. Gould, D. P. Robinson & H. S. Thorne, "On solving trust-region and other regularised subproblems in optimization", *Math. Program. Comput.* 2 (2010) 21–57, 10.1007/s12532-010-0011-7 · P
- S11 · N. I. M. Gould, D. Orban & D. P. Robinson, "Trajectory-following methods for large-scale degenerate convex quadratic programming", *Math. Program. Comput.* 5 (2013) 113–142, 10.1007/s12532-012-0050-3, with its on-line appendices (dated 8 December 2012) · P
- S12 · F. E. Curtis, N. I. M. Gould, H. Jiang & D. P. Robinson, "Adaptive augmented Lagrangian methods: algorithms and practical numerical experience", *Optim. Methods Softw.* 31 (2016) 157–186, 10.1080/10556788.2015.1071813 (online-first PDF read) · P
- S12a · Same authors and title, arXiv:1408.4500 v1 (20 August 2014) · P
- S13 · N. I. M. Gould, Y. Loh & D. P. Robinson, "A nonmonotone filter SQP method: local convergence and numerical results", *SIAM J. Optim.* 25 (2015) 1885–1911, 10.1137/140996677 · P
- S14 · N. I. M. Gould & D. P. Robinson, "A second derivative SQP method: global convergence", *SIAM J. Optim.* 20 (2010) 2023–2048, 10.1137/080744542 (conclusions read) · P
- S15 · N. I. M. Gould & D. P. Robinson, "A second derivative SQP method: local convergence and practical issues", *SIAM J. Optim.* 20 (2010) 2049–2079, 10.1137/080744554 · P
- S16 · N. I. M. Gould & Ph. L. Toint, "Nonlinear programming without a penalty function or a filter", *Math. Program.* 122 (2010) 155–196, 10.1007/s10107-008-0244-7 · P
- S17 · N. I. M. Gould & Ph. L. Toint, "Erratum to: Nonlinear programming without a penalty function or a filter", *Math. Program.* 131 (2012) 403–404, 10.1007/s10107-011-0491-x · P
- S18 · F. E. Curtis, N. I. M. Gould, D. P. Robinson & Ph. L. Toint, "An interior-point trust-funnel algorithm for nonlinear optimization", *Math. Program.* 161 (2017) 73–134, 10.1007/s10107-016-1003-9 (introduction and conclusion read; the absence of a numerical section checked by search of the full text) · P
- S19 · N. I. M. Gould, "How good are projection methods for convex feasibility problems?", *Comput. Optim. Appl.* 40 (2008) 1–12, 10.1007/s10589-007-9073-5 · P
- S20 · N. I. M. Gould, "How good are extrapolated bi-projection methods for linear feasibility problems?", *Comput. Optim. Appl.* 51 (2012) 1089–1095, 10.1007/s10589-011-9414-2 (read in full) · P
- S20a · Y. Censor, W. Chen, P. L. Combettes, R. Davidi & G. T. Herman, "On the effectiveness of projection methods for convex feasibility problems with linear inequality constraints", *Comput. Optim. Appl.* 51 (2012) 1065–1088, 10.1007/s10589-011-9401-7 (metadata only, **not read**) · P (critique)
- S21 · N. I. M. Gould, J. A. Scott & Y. Hu, "A numerical evaluation of sparse direct solvers for the solution of large sparse symmetric linear systems of equations", *ACM Trans. Math. Softw.* 33(2) Art. 10 (2007), 10.1145/1236463.1236465 · P
- S22 · N. Gould & J. Scott, "The state-of-the-art of preconditioners for sparse linear least-squares problems", *ACM Trans. Math. Softw.* 43(4) Art. 36 (2017), 10.1145/3014057 · P
- S23 · N. I. M. Gould, D. Orban, A. Sartenaer & Ph. L. Toint, "Sensitivity of trust-region algorithms to their parameters", *4OR* 3 (2005) 227–241, 10.1007/s10288-005-0065-y · P
- S24 · N. I. M. Gould, M. Porcelli & Ph. L. Toint, "Updating the regularization parameter in the adaptive cubic regularization algorithm", *Comput. Optim. Appl.* 53 (2012) 1–22, 10.1007/s10589-011-9446-7 (abstract and introduction) · P
- S25 · C. Cartis, N. I. M. Gould & Ph. L. Toint, "On the complexity of steepest descent, Newton's and regularized Newton's methods for nonconvex unconstrained optimization problems", *SIAM J. Optim.* 20 (2010) 2833–2852, 10.1137/090774100 (construction sections) · P
- S26 · C. Cartis, N. I. M. Gould & Ph. L. Toint, "Corrigendum: On the complexity of finding first-order critical points in constrained nonlinear optimization", *Math. Program.* 161 (2017) 611–626, 10.1007/s10107-016-1016-4; original paper *Math. Program.* 144 (2014) 93–106, 10.1007/s10107-012-0617-9 (original not re-read) · P
- S26a · I. Bongartz, A. R. Conn, N. Gould & Ph. L. Toint, "CUTE: constrained and unconstrained testing environment", *ACM Trans. Math. Softw.* 21 (1995) 123–160, 10.1145/200979.201043 (§2.1) · P
- S27 · N. I. M. Gould, S. Lucidi, M. Roma & Ph. L. Toint, "Solving the trust-region subproblem using the Lanczos method", *SIAM J. Optim.* 9 (1999) 504–525, 10.1137/S1052623497322735 (§§6–7) · P
- S29 · N. I. M. Gould & J. Nocedal, "The modified absolute-value factorization norm for trust-region minimization", in *High Performance Algorithms and Software in Nonlinear Optimization*, Applied Optimization, Kluwer (1998) 225–241, 10.1007/978-1-4613-3279-4_15 (author preprint dated 25/01/1998) · P
- S30 · N. I. M. Gould, M. E. Hribar & J. Nocedal, "On the solution of equality constrained quadratic programming problems arising in optimization", *SIAM J. Sci. Comput.* 23 (2001) 1376–1395, 10.1137/S1064827598345667 · P
- S31 · N. I. M. Gould & D. P. Robinson, "A dual gradient-projection method for large-scale strictly convex quadratic problems", *Comput. Optim. Appl.* 67 (2017) 1–38, 10.1007/s10589-016-9886-1 · P
- S32 · H. Al Daas & N. I. M. Gould, "Extended-Krylov-subspace methods for trust-region and norm-regularization subproblems", arXiv:2511.11135, v1 (14 November 2025), v2 (21 January 2026, abstract only), v3 (2 March 2026); v1 and v3 full texts compared · P
- S33 · J. M. Fowkes, N. I. M. Gould & J. A. Scott, "Approximating sparse Hessian matrices using large-scale linear least squares", *Numer. Algorithms* 96 (2024) 1675–1698, 10.1007/s11075-023-01681-z (test-set section only) · P
- S34 · N. I. M. Gould, S. Leyffer & Ph. L. Toint, "A multidimensional filter algorithm for nonlinear equations and nonlinear least-squares", *SIAM J. Optim.* 15 (2004) 17–38, 10.1137/S1052623403422637 (§4 test set) · P
- S35 · N. I. M. Gould, C. Sainvitu & Ph. L. Toint, "A filter-trust-region method for unconstrained optimization", *SIAM J. Optim.* 16 (2005) 341–357, 10.1137/040603851 (baselines only) · P
- S36 · N. I. M. Gould, T. Rees & J. A. Scott, "Convergence and evaluation-complexity analysis of a regularized tensor-Newton method for solving nonlinear least-squares problems", *Comput. Optim. Appl.* 73 (2019) 1–35, 10.1007/s10589-019-00064-2 (baselines only) · P
- S37 · N. I. M. Gould & Ph. L. Toint, "FILTRANE, a Fortran 95 filter-trust-region package for solving nonlinear least-squares and nonlinear feasibility problems", *ACM Trans. Math. Softw.* 33(1) (2007), 10.1145/1206040.1206043 (abstract and baselines only) · P
- S38 · N. I. M. Gould, Y. Loh & D. P. Robinson, "A filter method with unified step computation for nonlinear optimization", *SIAM J. Optim.* 24 (2014) 175–209, 10.1137/130920599 (codes named only) · P
- S39 · N. I. M. Gould & Ph. L. Toint, "Preprocessing for quadratic programming", *Math. Program. Ser. B* 100 (2004) 95–132 (author PDF, numerical section heading only; DOI not checked, so no claim rests on it) · P
- S40 · C. Cartis, N. I. M. Gould & Ph. L. Toint, "Adaptive cubic regularisation methods for unconstrained optimization. Part I", *Math. Program.* 127 (2011) 245–295, 10.1007/s10107-009-0286-5 (via note 01; DOI re-checked) · P
- S41 · J. M. Fowkes & N. I. M. Gould, "GALAHAD 4.0: an open source library of Fortran packages with C and Matlab interfaces for continuous optimization", *J. Open Source Softw.* 8 (2023) 4882, 10.21105/joss.04882 (via note 01; DOI re-checked) · P
- S42 · N. Marumo & A. Takeda, "Parameter-free accelerated gradient descent for nonconvex minimization", *SIAM J. Optim.* 34 (2024) 2093–2120, 10.1137/22m1540934 (metadata only; cited because GALAHAD AGD implements it) · S
- S43 · F. E. Curtis, H. Jiang & D. P. Robinson, "An adaptive augmented Lagrangian method for large-scale constrained optimization", *Math. Program.* 152 (2015) 201–245, 10.1007/s10107-014-0784-y (metadata only) · S
- S44 · Gould & Scott 2004 HSL evaluation, 10.1145/1024074.1024077; Gould & Scott 2016 performance profiles, 10.1145/2950048; GALAHAD 2003, 10.1145/962437.962438; CUTEr 2003, 10.1145/962437.962439; CUTEst 2015, 10.1007/s10589-014-9687-3; CGT correction 1989, 10.1137/0726044; Keller, Gould & Wathen 2000, 10.1137/S0895479899351805: DOIs re-checked in this run; content via notes 01 and 02 · S (bibliographic)

Other
- S45 · Crossref REST API metadata checks for all DOIs above, 2026-09-28, https://api.crossref.org · S (bibliographic)
- S46 · arXiv abstract pages and submission histories for 2511.11135 and 1408.4500, 2026-09-28, https://arxiv.org/abs/2511.11135, https://arxiv.org/abs/1408.4500 · P (bibliographic)
- S47 · WebSearch (1 call) locating arXiv 1408.4500 and the Lehigh COR@L report 14T-006 (report **not read**), https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/pdf/tech-papers/14/14T_006_0.pdf · S
- S48 · N. Gould, RAL staff page (list of author PDFs used to locate the papers above), https://www.numerical.rl.ac.uk/people/nick-gould/ · P
- S49 · Note 01 of this team (`01-publications.md`), cross-reference only · S
- S50 · Note 02 of this team (`02-methodology.md`), cross-reference only (stated method for §8) · S
