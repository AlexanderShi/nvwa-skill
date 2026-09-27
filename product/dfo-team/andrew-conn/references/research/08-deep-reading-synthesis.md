# Andrew R. Conn · Deep-reading synthesis

> Date: 2026-09-27. Input: every card in `cards/` (20 batch files, 140 card entries for 138 in-scope works; index in `07-paper-cards.md`). §12 adds the book-material batch `k01` (6 cards, B001–B006) and is kept apart from the counts of §1–§11. Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence first, a new method needs ≥3 distinct papers plus the four checks, reject updates without explanatory power, every claim traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`.
>
> Citation form: `[S012 p. 9]` = card S012, page of the extracted text as recorded on the card; `abstract` = abstract-level card. Counts are **distinct papers** after merging same-work pairs: S032 = S123, S093 = S108, S111 = S026 (report version), S126 ~ S054 (same primal-dual line), S102 ~ S120 (analysis and complete-results companion); where noted, also D002 = S039 (journal version) and S166 ~ S099 (conference abstract of the journal paper). S236 and S049 each have two cards (metadata/unreadable superseded by full cards `c3-01` and `s4-01`) and count once.
>
> Weighting: IBM team papers where Conn is a middle author (S032/S123, S057) and papers where his personal role is not identifiable (S003, S060) are carded but carry no weight as evidence for or against his practice. Cards that record typos or internal inconsistencies noticed inside a paper are reading notes and are not used as findings here.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Google Scholar rows | 237 (+ 2 DBLP-only items D001, D002); 56 duplicate rows set aside | `scholar.md` |
| Distinct works on the list | 155 | `scholar.md`, `works.json` |
| Full-text index rows | 183 = the 155 works + 28 rows that are not Conn works (11 unresolved title-page fragments, 17 referee lists, report sections or misattributed rows); 183 − 45 = 155 − 17 = 138 in scope | `../sources/papers/INDEX.md` |
| Skipped, excluded from every denominator | **45**: 17 rows that are not Conn publications (referee and acknowledgement lists, progress-report sections, a misattributed row, an organisers' message), 11 unresolved title-page fragments, 13 patents, 2 talks (S148, S187), S153 (authorship doubtful), S156 (P. F. O'Neill's thesis) | INDEX.md Role = skip; `scholar.md` |
| In-scope works / card entries | 138 / 140 | `07-paper-cards.md` |
| Distinct papers | 133 (131 with D002 and S166 also merged) | same |
| **Full text read** | **71** (53 full, 18 partial) | read-level column |
| Abstract-level | 50 | a2-01, a2-02, a2-03 |
| Metadata-only | 16 | a2-01, a2-02, a2-03 |
| Unreadable | 1 (S093; the same Cornell TR text is read as S108) [S093] | s2-02 |

Full-text reads by period (full + partial / carded): 1972–1979 1/11; 1980–1989 12/26; 1990–1995 17/27; 1996–2000 22/32; 2001–2005 2/7; 2006–2010 6/11; 2011–2015 4/15; 2016–2023 7/9. The CGT, LANCELOT and early DFO years (1985–2000) are read almost completely; the 1970s penalty and minimax papers, the books and the 2006–2015 energy work are known mostly from abstracts [S024, S038, S014, S015 abstract; S001, S002, S006 abstract; S098, S100, S083, S105, S132, S084, S076, S147, S142 abstract].

Eight scanned papers were read from page images and their cards carry page references but no quotes: S018, S021, S030, S046, S048, S108, S130, S164. OCR text now exists for spot checks.

Versions actually read, where they differ from the listed venue: S049 is FUNDP Report 88/4 (revised January 1989), not the 1994 chapter [S049 header]; S126's file is FUNDP Report 96/9, the bounds-and-linear-equalities member of the S054 line [S126 contribution]; S003 is the 31 October 2005 preprint [S003 header]; S075 is the 28 June 2016 preprint [S075 header]; S089 is Report 92/18 revised November 1993 [S089 header]; S031 is Report 90/4 revised 1995 [S031 M1 link]; S057 is arXiv v1 [S057 header]; S093 and S108 are the same 1990 Cornell TR [S093]; S236 is the whole newsletter issue, of which only the essay on pp. 1–7 is Conn's [S236 header].

---

## 2. Evidence per existing method

Counts are distinct full/partial cards linking to the method (a card can give both evidence and a variant); "weighted" merges same-work pairs and drops the four unweighted papers. Abstract- and metadata-level links are listed separately and are not used for decisions.

| Method | Evidence ✅ | Variant ⚠ | Contradiction ✗ | Distinct full/partial cards | Weighted papers | Abstract/metadata cards |
|---|---|---|---|---|---|---|
| M1 Theory–code–test triad | 33 | 33 | 2 (both target a factual line, not the method: S021 → warning sign 2, S236 → say–do line) | 63 | 58 | 15 |
| M2 Test bed as infrastructure | 28 | 20 | 2 (S057 set aside, middle author; S066 reclassified as variant, §3 row 17) | 41 | 36 | 9 |
| M3 Certify the model | 11 | 16 | 0 | 24 | 24 | 1 |
| M4 Enter through the user's door | 16 | 4 | 0 | 20 | 16 | 24 |
| M5 Derivatives and structure first | 49 | 2 | 0 | 50 | 46 | 23 |
| M6 Transplant and hybridize | 49 | 0 | 0 | 49 | 42 | 24 |

All six methods survive the full texts; none is contradicted at its core. The high variant counts for M1 and M3 come from the order and packaging of the triad (§3 rows 4, 14–15) and from pre-DFO forms of the certified-interface idea (§3 row 19).

### M1 · The theory–code–test triad

- **Strongest practice**: the 1988 twin, theory and testing submitted six months apart and cross-cited [S008 pp. 1–2, 28; S011 pp. 2–3], with the testing paper checking its deviations against the theory and repairing a failure within what the theory allows [S011 pp. 5, 19–20]; theory [S005] → book [S006 abstract] → 21-variant study on 943 CUTE instances citing the theory at each step [S040 pp. 7, 10, 12, 15–16] → complete data [S103 pp. 1–2]; the analysed algorithm shipped as HSL VE12, "exactly the algorithm we analysed" [S026 p. 30]; theorem, code and data profiles in one paper plus a local-convergence companion [S025 pp. 3, 16–21; S065 pp. 1, 20–26]; theorem + code + two-tier numbers [S075 pp. 17–23]. Waterloo form: algorithm paper and refereed Fortran code as twins in one journal issue [S042, S109 metadata/abstract]; theory + implementation + numbers with the rate in a twin report [S030 pp. 4, 15–16, 26–27].
- **Stated in full texts** (new; SKILL.md relied on obituaries): "final implementations and the studied algorithms should differ as little as possible", theory necessary but not sufficient, backed by intensive testing [S046 p. 11]; "the construction of appropriate software is by no means trivial and we wish to make a thorough job of it" [S005 p. 4]; software is the main purpose of algorithm design, and "Frankly, we were surprised when researching this paper quite how few papers contained numerical results" [S080 p. 16]; "nobody should be publishing papers whose main purpose is to describe an algorithm that is intended to be practically useful, unless they also provide evidence that the algorithm is competitive on significant problems" [S061 p. 27]; much of the joint effort went into software, input and testing [S086 pp. 2–3]; the methods' potential "will only be fully realized when associated high quality software will become available to users" [S009 p. 17]. First person, for industrial work: the triad he names is state-of-the-art optimization, domain experts and familiar interfaces, and convergence theory is not mentioned [S236 p. 4].
- **Say–do update**: ✅ stays; the stated side now rests on co-authored primary texts (1989–1997) and one first-person essay, not on obituaries. Qualify "together": the triad is a property of a line of papers, often assembled in either order (§3 rows 4, 14).

### M2 · Build the test bed as research infrastructure

- **Strongest practice**: CUTE as a published, classified, solver-agnostic product with interfaces to rival codes (COBYLA, NPSOL, VF13) [S004 pp. 4–25]; the LANCELOT options study with coded failures and a same-answer filter [S040 pp. 27–39]; LANCELOT vs MINOS on 913 problems in evaluations and CPU, stratified by class, failures by cause [S102 pp. 7–13; S120 pp. 2–3, 27]; a bias-controlled open benchmark protocol [S188 pp. 3–9]; two tiers (CUTE/HS + Boeing helicopter) in evaluations with CPU explicitly excluded [S020 pp. 8–10]; noisy variants at two levels [S019 pp. 15–18]; Moré–Wild data profiles with deterministic noise [S025 pp. 17–19]; two tiers with baselines from both schools [S075 pp. 17–23].
- **Stated in full texts**: "We believe that the important figures in such a comparison are the number of function and gradient calls" [S011 p. 22]; "We do not list the CPU time, since it is not relevant in our context" [S020 p. 10]; large test sets are "essential for a valid assessment", smaller ones "more likely to introduce unwanted bias" [S102 p. 7]; personal intervention "and thus of bias" kept to a minimum [S188 p. 3]; format differences "could be a major obstacle to valid comparisons" [S137 p. 2]; both practical and academic problems required [S046 pp. 11–12]; first person: an open-source MINLP package released with test problems as early as possible, and a two-tier benchmark against commercial tools [S236 pp. 5–6].
- **Say–do update**: ✅, now with a primary stated side (1988–2007). Variants on the cost unit and the noise tier in §3 row 16.

### M3 · Certify the model

- **Strongest practice**: all of steps 1–4 in the first DFO convergence paper (error bounds, "adequate" geometry, finite improvement plus small-gradient certification, proof using adequacy only) [S013 pp. 11–17]; geometry as an explicit, measurable condition with an attainability theorem and restoration [S009 pp. 3, 9–16]; basis-independent Λ-poisedness with a repair algorithm [S124 pp. 2, 6–10, 27–29]; equivalence Λ ↔ ‖M⁻¹‖ and one-point repairs [S016 pp. 3, 7, 13, 16, 19–23]; regression and underdetermined models [S028 pp. 9–10, 16, 22–24]; the model-improvement algorithm made part of the definition of a model class [S012 pp. 1, 7–9, 13]; the radius not cut before the model is fully linear, in the practical code [S020 pp. 4–5].
- **Reused by Conn's own later papers (the payoff of step 4)**: only the structure-specific lemma proved, the rest cited from the framework [S025 p. 12]; "there is no need to add further analysis to the convergence theory of derivative-free trust-region methods" [S066 p. 3]; certification carries the local rate [S065 p. 10]; the framework cited as the building block of the progressive-barrier method [S075 p. 25].
- **Stated**: "The main task of such a derivative free algorithm is to maintain an interpolation sampling set so that this constant remains small, and at least uniformly bounded" [S016 p. 1]; "In practical situations only the geometry of the interpolation set is controllable" [S124 p. 32]; "The abstraction highlights, in our opinion, the fundamental requirements for obtaining the appropriate convergence results" [S012 p. 13].
- **Say–do update**: ✅. Step 5 ("measure how often improvement steps fire") has no measured frequencies in the cards: CSV 2009 says only qualitatively that replacing points because of bad pivots is rarely necessary [S012 p. 12], and the 2018 paper names the measurement as future work [S075 p. 23] (§3 row 19).

### M4 · Enter through the user's door

- **Strongest practice**: the first JiffyTune paper, with user pain in the designers' terms, interfaces inside their design systems and adoption reported as 41 designers on 168 circuits [S036 pp. 1, 5–6]; EinsTuner co-written with IBM's EDA group, tested on real microprocessor designs, wired in by back-annotation, published at DAC [S027 pp. 1, 4, 6, 8]; noise constraints delivered inside the designers' tool [S039 pp. 1, 6, 8]; Boeing helicopter and nozzle problems at an AIAA MDO symposium [S020 pp. 1–3]; shale-gas scheduling via the NTNU/IO centre [S060 pp. 1, 27] (unweighted: Conn's role not identifiable); air-traffic models driven by controllers' practice [S099 pp. 7, 14, 19; S141 pp. 10–12].
- **Stated, first person** (new): the minimax question, the invitation as an approachable mathematician and "I said it was very interesting but it was too bad that they were using 1960s algorithms in the 1990s and so I was asked to tell them about 1990 algorithms" [S236 p. 3]; manual tuning slow, tedious, manual and error-prone, the tool a standard IBM tool for all custom circuits [S236 p. 4]; "Without which, algorithms twice as good would not have succeeded" (software in the users' environment) [S236 p. 4]; an area rich in problems with access to extremely knowledgeable people [S236 p. 7]; intimate collaboration with domain experts, and applying optimization "almost a duty" [S236 p. 5]. Co-authored: "The designers' focus shifts from solving the optimization problem to specifying it correctly and completely" [S036 p. 1].
- **Say–do update**: ✅, now primary and first person. The limitation "it depended on IBM's in-house access" is confirmed in his words: the project would not have happened in an academic environment [S236 p. 4, p. 5].

### M5 · Exploit derivatives and structure before going black-box

- **Strongest practice**: the derivative audit before DFO, one reason per route (finite differences, AD, source) [S019 p. 3; S009 pp. 3–4]; the flagship tool gradient-based via adjoint time-domain sensitivities [S027 pp. 1, 4–5; S036 pp. 1–3]; one adjoint for all merit-function gradients [S039 pp. 3–4]; cheap constraints exact in the subproblem, equalities shrinking the interpolation space [S020 pp. 6–7]; bounds outside the penalty [S005 pp. 1–2, 4; S007 pp. 3, 7–8]; linear constraints outside the augmented Lagrangian [S022 pp. 2–3, 29; S113 pp. 4, 25]; one radius per element [S047 pp. 3, 5–6]; slack structure eliminated in closed form [S089 pp. 4–7]; per-residual models [S025 pp. 2, 5, 16]; nested structure saving lower-level evaluations [S066 pp. 1, 8–9, 16–19].
- **Stated**: "The fact that we are able to solve large problems at all is because they are structured" [S086 p. 5]; exploiting structure is the only reasonable way for large problems [S046 pp. 3, 8–9]; growth in solvable size "primarily because of our better exploitation of problem structure" [S080 p. 16]; "We strongly recommend the use of exact second derivatives whenever they are available" [S040 p. 24]; "Without a fast, accurate and reliable time-domain sensitivity engine, it would not have been possible to create a tool such as EinsTuner" [S027 p. 4]; "the polynomial interpolation-based methods which also exploit the problem structure are recommended" [S025 p. 21]; first person: derivatives were the decisive technical argument for the in-house simulator [S236 p. 3].
- **Say–do update**: ✅, stated from 1989 on. Variants in §3 row 20.

### M6 · Transplant proven machinery and hybridize across schools

- **Strongest practice**: trust-region machinery carried into DFO with the non-triviality stressed [S012 pp. 2–3; S013 pp. 7, 9, 18]; the augmented-Lagrangian shift carried from penalties to barriers [S007 pp. 5–6, 26–27]; linear Chebyshev theory carried to nonlinear minimax [S130 pp. 11–18; S164 pp. 3–7; S108 pp. 4–5]; LP primal-dual machinery carried to nonconvex NLP [S054 p. 2; S026 pp. 2, 6–9] and to the sum of norms [S017 pp. 8–10]; the progressive barrier moved from MADS into a trust region [S075 pp. 3, 10, 13, 20]; a hybrid family with the rival MINLP methods as its extremes [S003 pp. 1–3, 9–10]; trust-region ratio logic stabilising a cutting-plane dual [S060 pp. 13–20]; the 1970s penalty machinery carried into logical constraints fifty years on [S141 pp. 3–5, 13].
- **Stated**: the authors find it "rather strange" that the shift device was never applied to barriers [S007 p. 5]; the rule for choosing between schools, "Given a very badly behaved function we would use a direct-search method. If the function can be adequately approximated by a smooth function we would prefer a model-based approach" [S075 p. 2]; first person, 1990s algorithms carried into 1960s practice [S236 p. 3].
- **Say–do update**: ✅. Variant in §3 row 21.

### Heuristics, taste marks and signature works with new full-text practice

- H1 [S036 pp. 1–3; S027 p. 4; S039 pp. 3–4; S040 p. 24; S236 p. 3]; nuance: modelling f can beat estimated derivatives per evaluation, "it may not be optimal to use function values to compute explicit derivative approximations" [S009 p. 4]. H2 [S025 pp. 2, 5, 16, 21; S065 pp. 2, 26]. H3 [S066 pp. 1, 8–9, 16–19]. H4: NOMAD uses the Conn–Le Digabel quadratic models by default [S075 p. 19; S023 abstract]. H5, with the device retuned to the host's evaluation economics [S075 pp. 3, 9, 11, 13, 20]. H6 [S008 + S011; S040 + S103; S030 pp. 4, 27; S113 + S107; S025 + S065]. H7 [S004 pp. 2–4; S149 pp. 4, 68; S236 p. 5]. H8, first person, "age is often a negative attribute" of LANCELOT against IPOPT [S236 pp. 4–5], plus the same move on his own methods [S108 pp. 17, 21; S017 p. 2; S016 p. 19]. H9, first person [S236 p. 3].
- Taste mark 2 (class-level theory) [S008 pp. 4, 6–7, 27; S010 pp. 6–7; S021 pp. 7, 10; S030 p. 10; S031 p. 10; S012 p. 3]. Mark 3 (a real user): wanted problems whose answers people were extremely interested in [S236 p. 2]; "clearly meets a strong and explicit need in several application areas" [S019 p. 20]. Mark 4 (budget and noise as inputs): noise-aware predicted-reduction test [S019 p. 12]; radius and tolerances in physical units [S036 p. 5]; noise understudied "particularly as so many industrial problems involve noisy functions" [S080 p. 17]; noisy f in a convergence theorem [S031 pp. 57–58]. Mark 5 (infrastructure) [S004; S149; S137; S188; S046]. Mark 6 (model quality) as in M3.
- Warning sign 6 (claim calibration): "competitive", "preferable" only where the curves support it [S075 pp. 1, 22–23]; "complement each other", own weakness on LPs stated plainly [S102 pp. 12, 17]; "appears … preferable" backed by per-iteration cost [S108 pp. 18–19]; declines to claim superiority, names the counterexample to its own method [S048 p. 21]; "qualitatively similar" to commercial software [S236 p. 6].
- Signature Work anatomies: see §3 rows 8–10 and the terminology note in row 24.

---

## 3. Variants and contradictions

The full texts win over search snippets. Rows 1–13 change what SKILL.md says; rows 14–26 add a variant note without changing the claim.

| # | SKILL.md claim | What the full texts show | Cards | Change |
|---|---|---|---|---|
| 1 | M1 say–do line, Honest Boundary, Mentor Voice, JiffyTune anatomy: no first-person essay or first-hand account was found | Conn's single-author essay *My Experiences as an Industrial Research Mathematician*, SIAG/OPT Views-and-News 18(2), October 2007, pp. 1–7, covering how problems reached him, what made the circuit project succeed, lab versus university, and career facts. It partly recovers how he dealt with IBM engineers and management (18-month survival fight, advocacy through the engineers) [S236 pp. 1–7]. | S236 | Cite S236 as the primary stated source; keep "no student memoirs or recordings" |
| 2 | M4 Stated, Step 2, Step 5, H8, H9, JiffyTune origin: cited as MAM 2015 paraphrases | The same items appear first person in 2007: minimax question → workshop and the 1960s-algorithms remark [S236 p. 3]; slow, tedious, manual, error-prone tuning, standard tool for all custom circuits, LANCELOT then IPOPT [S236 p. 4]; "age is often a negative attribute" [S236 p. 5]; an area rich in problems with extremely knowledgeable people [S236 p. 7]. Two verbatim quotes are on the card [S236 pp. 3, 4]. Whether MAM 2015 reuses this text was not checked [S236 card]. | S236 | Replace the paraphrases with S236 citations and the two quotes |
| 3 | Warning-signs preamble: "No explicit critique by Conn was found" | Co-authored explicit critiques: few papers contain "numerical results which justified their author's optimistic analytic assessments, or indeed any numerical results at all" [S080 p. 16]; "nobody should be publishing papers …" without evidence of competitiveness [S061 p. 27]; "in our opinion, the contortions" needed for positive-definite SQP secant updates [S080 p. 4]; SA, GA and Nelder–Mead rarely best, citing McKinnon's counterexample (16-author white paper, section authorship unknown) [S136 pp. 13–14]. | S080, S061, S136 | Warning signs 1–3 get stated sources; say "co-authored" |
| 4 | Warning sign 2: "A theorem with no runnable code and no numbers. This never occurs in the confirmed record"; Taste mark 1 "Proof, code and numbers arrive together" | Theory-only papers are common: "Nor have we provided any detailed numerical evidence that the approach taken here is effective on general problems" [S007 p. 27], although the same paragraph reports anecdotally that a rudimentary implementation solved over ninety percent of about a thousand problems [S007 p. 27]; practical performance declared unknown, left to future work [S021 p. 26]; no code or numbers [S013 p. 22; S012 pp. 11–13; S124 pp. 27–32; S130 p. 32; S018 pp. 4, 15]; code and numbers deferred [S005 pp. 4, 27; S107 p. 4; S031 pp. 2, 13, 28]. In almost every line the other legs follow in companion papers (S005 → S006 → S040; S019, code first → S013 → S020; S012 → S025, S075; S018 → S030's twin report); S021's announced numerical follow-up is not among the cards. | S007, S021, S013, S012, S124, S130, S018, S005, S107, S031 | Rewrite: the warning is "a theorem whose algorithm never gets code or numbers anywhere in the line"; mark 1 becomes "arrive within a line of work, rarely in one paper" |
| 5 | Research Trajectory table | Missing periods and projects: IBM–CMU MINLP project he initiated and chose, BONMIN released in little more than a year (own contribution called minimal) [S236 pp. 4–5; S003 pp. 1–2]; seismic matching and history matching as IBM first-of-a-kind projects [S236 p. 6; S161, S171, S098, S100, S076, S142 abstract]; maintenance scheduling as simulation-based DFO [S236 pp. 6–7; S101 abstract]; a three-year DARPA grant of $917,809 within a year of joining IBM [S236 p. 2; S017 p. 1]; three years teaching a course at Yale until its OR department closed [S236 p. 2]; electricity-grid white paper [S136 p. 1]; air-traffic line with ENAC from 2015 [S063 abstract; S166; S099; S141]. | S236, S003, S101, S136, S099, S141 | Add rows for mid-2000s–2008 MINLP (start year not dated in the sources), 2006–2015 petroleum/maintenance, 2015–2023 air traffic |
| 6 | Latest: "The last confirmed papers are the two 2018 works … No activity since then" | Posthumous publications: AutoML (AAAI 2020, middle author) [S032]; derivative-free exact penalty (2022) [S135 abstract]; aircraft conflict MINLP (EJOR 2023) and the quadrant penalty (OJMO 2023), both dedicated "In memory of our dearest friend Andy Conn" [S099 p. 2; S141 p. 2]. S141 is framed as an answer to Conn's 1981 question whether penalty functions can contribute to discrete or global optimization [S141 pp. 4, 13]. | S032, S135, S099, S141 | "Last papers during his lifetime: 2018; posthumous co-authored papers 2020–2023"; still a historical lens |
| 7 | How to Use weak spots: integer or categorical variables "outside Conn's documented work" | Mixed-integer work exists in applied collaborations: the MINLP project he initiated [S236 pp. 4–5]; MILP decomposition for shale gas [S060, role not identifiable]; aircraft-conflict MINLP and logical constraints as penalties [S099 pp. 6–10, 19–20; S141 pp. 4–11]. No Conn-led method for integer DFO. | S236, S099, S141, S060 | Narrow the wording: integer DFO remains a blind spot; mixed-integer formulations appear in team application work |
| 8 | Signature Work CST 1997 survey: Origin "speculation"; Abandoned paths "unknown" | Origin is stated: applications "presented to the authors" with expensive simulations and unavailable source code [S009 p. 3], geophysical measurement and helicopter rotors [S019 pp. 2–3]. Abandoned paths: the CST full-replacement geometry step, later called "very expensive" and replaced by one-point repairs [S016 p. 19]; the CST O(Δ) gradient bound, later called "clearly inferior" [S124 pp. 26–27]. Minimal evidence confirmed: 20 small CUTE problems, n = 2–4, noiseless and at two noise levels [S019 pp. 15–18]. | S009, S019, S016, S124 | Replace "speculation" and "unknown" |
| 9 | Signature Work LANCELOT: Abandoned paths "presumably not made defaults (speculation)" | The authors say the ℓ₂ trust region, diagonal rescaling and DFP "could probably be removed from future releases", and automatic scaling and accurate BQP solves should not be defaults [S040 p. 50]; LANCELOT A's major defect is its handling of linear constraints [S061 p. 21]. | S040, S061 | Replace the speculation |
| 10 | Signature Work JiffyTune: Minimal evidence "Unknown" | The 1996 ICCAD paper reports use by 41 designers on 168 circuits and a benchmark matrix re-evaluated by a reference simulator [S036 pp. 2, 6]. | S036 | Fill in |
| 11 | M2 Practice: "40 smooth problems (vs COBYLA) plus nonsmooth MDO problems (vs NOMAD)" | Both baselines (NOMAD 3.7.2, COBYLA) run on both tiers; tier 2 is two MDO problems (AIRCRAFT RANGE, SIMPLIFIED WING); on the smooth set the new code is comparable to COBYLA and both model-based codes beat NOMAD [S075 pp. 17–23]. | S075 | Reword |
| 12 | Honest Boundary: "Web-snippet research only … full texts were blocked or unread" | 71 full texts read, 8 from page images; 50 abstracts; no code inspected (§1, §11). | all | Rewrite the boundary |
| 13 | M1, M2, M5 Stated lines resting on obituaries and abstracts | Co-authored primary statements quoted in §2 [S046 p. 11; S005 p. 4; S080 p. 16; S061 p. 27; S011 p. 22; S102 p. 7; S086 p. 5; S040 p. 24]. | as listed | Replace or add |
| 14 | M1 order ("theorem, code, numbers") | The triad is assembled across papers in either order: theory first, code deferred [S005 pp. 4, 27; S022; S007]; code and tests first, theory later [S019 pp. 15–20 → S013]; test → theory, with the theorem's constant checked against new runs [S011 p. 20 → S010 pp. 5–6, 15–19]; code → observation → theorem → next release [S074 pp. 3, 25]; split over report clusters [S108 pp. 4, 22; S164 pp. 2, 22; S130 p. 32]. | as listed | Variant note |
| 15 | M1 (new variant): theory aimed at the code actually run | Relax the analysed algorithm towards what codes do: "we are trying to bridge the gap by describing an algorithmic framework in the spirit of the first category of methods, while retaining all the same global convergence properties of the second category" [S012 p. 2]; theory for Powell's practical Lagrange-maximization rule and for minimum-norm models already used in codes [S016 pp. 18–19; S028 p. 2]; abstract stopping rules built to contain the native tests of named packages, with native-implies-abstract lemmas [S022 pp. 5–6, 26–29; S113 p. 18; S107 p. 25]; deviations of the tested code checked against the theory [S011 p. 5]; theory as a constraint on engineering changes [S036 pp. 4–5]. | S012, S016, S028, S022, S113, S107, S011, S036 | Add to M1 step 2 and to Workflow B's checkpoint as the positive rule |
| 16 | M2 step 1 (evaluations as the unit) and the noisy tier | The unit is what the user pays: CPU and linear-algebra counts when evaluations are cheap [S058 p. 3; S049 pp. 10–11; S061 p. 21]; two units can rank packages in opposite directions [S120 pp. 28–50]. The LANCELOT-era test beds have no noisy tier [S004 pp. 6–8; S040 pp. 30–31]; noise enters with DFO [S019 pp. 17–18; S025 pp. 17–19; S065 pp. 23–24]. | as listed | Variant note |
| 17 | M2 as a universal standard (card S066 ✗) | The first paper in a new problem class tests small hand-built examples and says why: "there are no comparisons with competing methods — this is because such methods appear not to exist" [S066 p. 19]. | S066 | Reclassify ✗ → ⚠: disclose the absence of baselines rather than invent one |
| 18 | M2 (new variant): a tier before the public set | Validate the formulation on an analytic prototype with exact gradients [S027 p. 5]; drive the component with synthetic sequences before real trajectories [S010 pp. 14–19]; test a general method first on the prototype subclass where baselines exist [S026 p. 30; S054 p. 27]; a synthetic model realistic enough to expose the difficulties but small enough to iterate, then a real case reported where it did worse [S236 p. 6]; re-evaluate final designs with a higher-fidelity simulator [S036 pp. 2, 6]. | as listed | Add "Tier 0" to M2 and Workflow C |
| 19 | M3 as a DFO-era invention; M3 step 5; Tension 1 | Pre-DFO certified interfaces carry theorems: a fraction of the generalized Cauchy decrease [S008 pp. 4, 7, 11]; inner-solve accuracy [S005 pp. 7, 13; S007 pp. 14, 27; S022 pp. 5, 26–28; S113 pp. 5, 14–19]; gradient error ≤ κΔ [S031 pp. 6–7; S047 pp. 5, 16–17]; step geometry σ_min(S) assumed [S010 pp. 7–8]. Step 5 never done [S016 p. 24; S075 p. 23]. The tension appears inside Conn's own papers: new algorithms may not outperform Powell's rule [S016 p. 23]; bad-pivot replacements rarely needed in practice [S012 p. 12]; an implemented bilevel method without explicit model-improvement iterations [S066 pp. 6–10]; certification enforced but unused in the 2018 theorems [S075 pp. 8, 12, 15–16]. | as listed | Variant note; add the in-house evidence to Tension 1 |
| 20 | M5 step 4 and step 3 | Step 4 generalises to "split by type, give each block its natural treatment" across 12 papers and all periods (§5 table; §7.2 A4). The structure exploited can be the structure of the *solution* (levelled reference sets) rather than of the objective [S164 pp. 8, 21; S108 p. 4; S130 pp. 4–5]. DFO was chosen for a stochastic simulation objective (maintenance under random failures), no results reported [S236 p. 7]. | S164, S108, S130, S236 | Variant notes |
| 21 | M6 step 4 ("keeps the stronger convergence theory") | The 2018 hybrid's theorem gives only that one radius sequence tends to zero [S075 pp. 15–16]; the imported device had to be retuned to the host's evaluations per iteration [S075 pp. 13, 20]. | S075 | Variant note |
| 22 | M4 entry route | Other routes: a management call pointed at the user's next structural change (discrete variables entering tuning) [S236 p. 4]; low-stake first-of-a-kind pilots with a customer [S236 p. 6]; problems harvested through a software licence [S004 p. 4]; a funder's RFI [S136 p. 1] (unweighted: 16-author team paper, Conn's role not identifiable; not used in SKILL.md). After the prototype, an 18-month fight for survival won with his immediate management's support and through the engineers who argued its case [S236 pp. 3–4]. | S236, S004, S136 | Variant note |
| 23 | Inner Tensions (new) | Craftsmanship versus good enough: the pressure to finish adequate-but-improvable work is "one of the largest 'lowlights'" [S236 p. 2], yet he values applications where even suboptimal solutions help greatly [S236 pp. 4, 6]. | S236 | Add a tension (later dropped from SKILL.md: the two sides are not in conflict) |
| 24 | Signature Work CSV 2009 and Academic Lineage: "fully linear / fully quadratic" described as later literature's language | The paper defines the terms itself [S012 p. 2, Defs. 3.1, 3.3 pp. 7–9], and the practical DFO paper already says the radius should not be decreased "until the interpolation becomes fully linear" [S020 pp. 4–5]. | S012, S020 | Reword |
| 25 | Academic Lineage formation | Waterloo from 1968 as a PhD student, 1971 postdoc at the Hebrew University, two French sabbaticals, recruited by Ellis Johnson at Oberwolfach and accepting within a year [S236 pp. 1–2]. Thesis title and advisor: the coauthors' posthumous paper gives the thesis as "A gradient type method of locating constrained minima" (Waterloo, 1971) and names Pietrzykowski as "Conn's PhD advisor" [S141 pp. 3, 13] (secondary, not Conn's own words); the title also appears in the Scholar record [S134 metadata]. | S236, S141, S134 | Add details |
| 26 | Research Integrity rule 4 ("no public statement found") | Co-authored statements against bias and for evidence [S061 p. 27; S188 p. 3; S102 p. 7]; public errata crediting the finders [D001 p. 1; S059 p. 4]; own-code expertise bias declared in a comparison [S061 p. 25]. | S061, S188, S102, D001, S059 | Add as positive models |

---

## 4. Promotions

The skill has six core methods, so one promotion fits under the 3–7 cap without replacing a method. One cluster passes all four checks and is not covered by an existing method.

### Promote → Method 7: Audit your own released solver; its named weaknesses are the next agenda

**Cluster** (15 distinct full/partial papers in five lines, 1989–2009, plus the 2007 essay; 16 cards, since S054 and S126 are one line and count as one paper). Proposed as a new pattern by 11 full/partial cards [S016 p. 19; S017 p. 2; S040 pp. 49–50; S054 p. 2 (= S126 pp. 2–3); S058 p. 3; S061 p. 15; S074 p. 3; S089 pp. 4, 8–9; S124 pp. 26–27; S164 p. 21] and used by 5 more [S022 p. 2; S026 p. 33; S108 pp. 17, 21; S012 p. 2; S236 pp. 4–5]; the S040 weak points lead to S089 and S007 [S040 p. 49]. Abstract-level: a 1978 concession reopened in 1989 [S051, S072 abstract].

| Check | Result | Evidence |
|---|---|---|
| 1 Cross-project recurrence | ✅ (full mechanism in LANCELOT, 9 papers, and minimax, 2; step 5 alone in location, DFO and circuits) | LANCELOT (1992–2000): named weak points → S089, S007 [S040 p. 49]; a 117-hour default run → the barrier line [S061 p. 15]; a shortcut in the released code → S022 [S022 p. 2]; named LANCELOT drawbacks → S054 [S054 p. 2], whose nonconvex failure → S026 [S026 p. 33]; LANCELOT's own linear-algebra cost → S058 [S058 p. 3]; an observed regularity of the LANCELOT B prototype → S074 [S074 p. 3]. Minimax (1978–1990): the failure mode of Conn's 1978 method → the Conn–Li method [S164 p. 21], which beats his own 1979 code [S108 pp. 17, 21]. Location: the Calamai–Conn methods named inefficient and replaced [S017 p. 2]. DFO (1997–2009): CST 1997's step and bound replaced [S016 p. 19; S124 pp. 26–27]; the authors' own book and CST 1997 placed in the "impractical" category [S012 p. 2]. Circuits: LANCELOT swapped for IPOPT [S236 pp. 4–5]. |
| 2 Say–do consistency | ✅ | Stated: a list of weak points seen only in the detailed runs, each paired with a planned fix, and options that "could probably be removed from future releases" [S040 pp. 49–50]; LANCELOT A's major defect named as its handling of linear constraints, and a declared expertise bias [S061 pp. 21, 25]; own step "very expensive" [S016 p. 19]; own bound "clearly inferior" [S124 pp. 26–27]; "our previous linesearch algorithm" named as the cause of the old failure [S026 p. 33]; first person, "age is often a negative attribute" [S236 p. 5]. Done: the follow-up papers exist [S089; S007; S022; S054; S026; S058; S074; S016; S124; S108; S017]. |
| 3 Executable, different from standard practice | ✅ | Steps below. Standard practice motivates new work from others' weaknesses and defends one's own released code; here the own code is the first object of critique, the list is printed in the testing paper, and earlier own methods are named as superseded [S040 p. 49; S108 p. 21; S016 p. 19]. |
| 4 Exclusivity | ⚠ plausible, indirect evidence (revised after review) | The evidence is indirect: the group complains that few papers report numbers at all [S080 p. 16] and demands evidence of competitiveness [S061 p. 27], which does not show that other groups avoid auditing their own released code. The move is shared with Gould and Toint, so it is a CGT-group trait, and within the DFO team it is close to the Powell lens (each new solver removes a measured limitation of its predecessor) and the Vicente lens (publish the boundary, then attack it). What is Conn-specific is the numbered weak-points list printed inside the testing paper [S040 pp. 49–50] and the sizing of fixes into note, theory paper or new method; Conn carried it into the DFO line with Scheinberg and Vicente [S016 p. 19; S124 pp. 26–27; S012 p. 2] and into IBM tooling [S236 pp. 4–5]. In the DFO team it is what ties this lens's agenda to released code. |

**Draft for SKILL.md** (for the SKILL.md editor; not applied here):

- **One line**: After each release, run your own code on the shared test set and on the hardest real case, print its weak points with a planned fix each, make each fix the next paper, and say in print when a newer method, yours or someone else's, supersedes your old one.
- **Steps**:
  1. Run the released code with defaults on the whole public collection and on the worst real case you have; record failures with numbers (problem, size, hours) [S061 p. 15; S040 pp. 34–39].
  2. In the testing paper, add a numbered weak-points list, each item with a planned fix, and name the options the data do not support [S040 pp. 49–50].
  3. Size each fix: an algebraic inefficiency → a short note tied to the released code [S089 pp. 4, 8–9]; a design shortcut → a theory paper that removes it [S022 p. 2]; a structural failure → a new method, then its successor if it fails in turn [S054 p. 2 → S026 p. 33].
  4. When the code shows a good behaviour the theory does not explain, make it the next theorem and aim it at the next release [S074 pp. 3, 25] (→ H10).
  5. When a new method replaces your earlier one, benchmark against the earlier one and say so [S108 pp. 17, 21; S017 p. 2; S016 p. 19; S124 pp. 26–27]; inside a user's tool, swap in the better solver even if the old one is yours [S236 pp. 4–5] (absorbs H8).
  6. Publish the agenda: close surveys with the group's own next projects [S009 p. 17; S061 pp. 15–22; S086 pp. 15–16; S080 pp. 16–17].
- **Applies to stage**: research agenda, problem choice after a release, writing (testing papers, surveys).
- **Different from standard practice**: the multi-year agenda comes from public self-critique of released software, not from gaps in others' papers; the SKILL.md routing row "Multi-year research agenda … Evidence is thin" gains a documented mechanism.
- **Limitations**: needs a released code with users and a shared test set (team-scale; an individual researcher can apply it to one published code and one benchmark). It can lock a group into incremental repairs of one package: much of the CGT group's 1992–2000 output repairs or extends LANCELOT [S089; S007; S022; S054; S058; S074; S082; S085] (proportions in §8.1). Shared with Gould and Toint, and close to moves in the Powell lens (solver lineage) and the Vicente lens (publish the boundary, then attack it), so it cannot be attributed to Conn alone. The DFO line did not complete the matching measurement step (how often geometry steps fire) [S075 p. 23].
- **Why not merged into M1 or H8**: M1 is the triad inside one project, and its step 5 ("when tests fail, go back to step 1") stays within that project. This method is between projects: it explains why one triad produces the next and why the trajectory has the shape it has (§8.4). H8 covers only the swap of a solver inside a tool and becomes step 5.

With Method 7 the skill is at the 7-method cap. Any later promotion must merge into or replace a method.

**Runners-up (not promoted)**:
- *Theory aimed at the code actually run* (10 papers: S010, S011, S012, S016, S022, S028, S049, S074, S107, S113; §3 row 15). Passes recurrence, say–do [S012 p. 2; S107 p. 25; S046 p. 11] and executability, but it is the direction of M1 and the positive form of M1's anti-pattern "theorem about an idealised algorithm, code that does something else". Folded into M1 (higher explanatory power there; no eighth slot).
- *Split by type, give each block its natural treatment* (12 weighted papers). Passes recurrence and executability, stated in [S080 p. 12; S022 p. 2], but it is M5 step 4 generalised. Folded into M5 (§3 row 20).

---

## 5. New heuristics

Clusters that are executable and pass at least one more check. "Recommend" = add to SKILL.md; "fold" = add as a step or case of an existing method or heuristic instead. SKILL.md has 9 heuristics; the framework asks for 5–10. Recommended arithmetic: H6 and H7 restate M1 step 4 and M2 (fold them into those methods as cases), H8 becomes M7 step 5, leaving H1–H5 and H9 plus the four new items below = 10.

| Cluster | Papers (full/partial) | Recurrence | Say–do | Executable & different | Exclusivity | Decision |
|---|---|---|---|---|---|---|
| Anomaly harvested as a conjecture, then proved | 4: S011, S010, S074, S049 | ✅ (1988–1997, three lines) | ✅ [S010 p. 5; S074 p. 3] | ✅ | partial | **Recommend (H10)** |
| Extend a theory by re-proving only the changed lemmas | 7: S007, S022, S025, S031, S066, S113, S155 (+ S047, S065, S011, S008) | ✅ | ✅ [S007 p. 8; S066 p. 3] | ✅ | partial | **Recommend (H11)** |
| Use every evaluation twice | 5: S013, S019, S026, S056, S058 (+ S009, S020, S025, S066) | ✅ | ✅ [S019 p. 4; S013 p. 17; S058 p. 4] | ✅ | ✗ (standard in model-based DFO codes; Powell's codes too [S028 p. 2]) | **Recommend (H12)** |
| Failed evaluation shrinks the region and retries | 2: S020, S027 (+ S026 p. 8; S033 abstract) | ✅ (two projects) | ✅ [S027 p. 5] | ✅ | partial | **Recommend (H13)** |
| One adjoint for the merit function | 1: S039 (+ S036 p. 3; S077, S033, D002 abstract) | ✅ (1997–2000) | — | ✅ | ✅ | Fold into H1 |
| Tier 0: prototype, synthetic, right-sized model | 4: S027, S026/S054, S036, S236 (+ S010) | ✅ | ✅ [S236 p. 6] | ✅ | ✗ | Fold into M2 (§3 row 18) |
| Attribute the rival's advantage before claiming | 4: S025, S061, S102/S120 (+ S027, S017, S040; S072, S176 abstract; S003 unweighted) | ✅ | ✅ [S061 p. 25] | ✅ | partial | Fold into M2 step 4 |
| Report where the method loses | 4: S020, S049, S056, S066 (+ S011, S040, S048, S102, S236) | ✅ | ✅ [S049 p. 19; S236 p. 6] | ✅ | partial | Fold into M2 step 5 and warning sign 6 |
| Characterisation-driven design for kinked objectives | 5: S233, S030, S108, S130, S164 (+ abstracts S014, S015, S024, S029, S044, S052, S062, S097) | ✅ (1978–1992) | ✅ in-paper [S233 p. 1] | ✅ | ✅ | Fold into M5 as the nonsmooth-era variant; §7.2 A5 |
| Survey as a research agenda | 4: S009, S061, S080, S086 (+ S001 abstract) | ✅ | — | ✅ | ✗ | Fold into M7 step 6 |
| Promise-then-deliver sequels | 3: S018 → S021, S113 → S107, S005 → S022 | ✅ | — | ✅ | ✗ | Hold (writing move, §7.4 W9) |

**H10 · If** your own tests show a result you cannot explain, **then** publish it as an explicit conjecture with the reason it is hard, make its explanation the next paper, and print the theorem's predicted quantity next to the observed one.
Cases: SR1's unexplained win in a trust region written up as a conjecture [S011 p. 20] and proved three years later, "Somewhat surprisingly, the traditional supremacy of the BFGS update is questioned by these numerical experiments" [S010 p. 5], with the computable bound printed beside the observed Hessian errors [S010 pp. 12, 15–19]; one inner iteration per outer iteration "often apparent" in the LANCELOT B prototype turned into a theorem, with what is proved and what is only observed kept apart [S074 p. 3]; the SR1 advantage failing under partial separability, with a conjectured mechanism [S049 p. 19].

**H11 · If** you extend a published convergence theory (yours or a framework's), **then** list which lemma uses which assumption, re-prove only those, map every other result by number to its predecessor, and check that each new rule reduces to the old one in the one-component case.
Cases: "We have intentionally kept our development as close as possible to that of Conn et al. [11]" [S007 p. 8]; results mapped by number to S005 with the one new difficulty marked [S022 pp. 13–15, 20–22]; only the counterpart of one lemma is new [S113 pp. 9, 14, 17]; noisy f handled by patching the one inequality that uses exact values [S031 pp. 36, 57–58]; discontinuous case changes only step 4 of the algorithm [S155 pp. 27, 32, 35]; each per-element rule stated with its one-element reduction [S047 pp. 10, 14]; plug-in on the CSV framework [S025 p. 12; S066 p. 3].

**H12 · If** each evaluation is expensive, **then** use every evaluated point twice: in the model and its geometry, to validate a long step before paying for a new evaluation, and as a candidate iterate even when it was sampled for geometry; reject trial points by cheap tests before evaluating them, and keep cheap constraints inside the subproblem so no evaluation is spent on an infeasible point.
Cases: "we will however insist on the ability of our algorithm to take long steps and also to progress as early as possible with every available function evaluation" [S019 p. 4], with models from fewer than p points and a history ratio test [S019 pp. 6–10]; geometry points may become iterates and any computed value is to "be exploited if at all possible" [S013 pp. 15, 17]; quality checks from construction byproducts cost no evaluations [S009 pp. 14–15]; analytic constraints in the subproblem [S020 p. 6]; a safety step without evaluation [S025 pp. 7–9]; an interiority test before evaluating an undefined barrier [S026 pp. 8–9]; evaluations reused across nested solves within O(Δ³) [S066 pp. 9, 14]; the cheap-computation analogue, reusing inner-solver byproducts because discarding them is "quite wasteful" [S058 pp. 4, 8, 10], and crediting a cheap bonus step in the ratio test [S056 pp. 4–7].

**H13 · If** the simulator can fail at a trial point, **then** give it a failure return code, let the optimizer skip the iteration and cut the trust region, count failed evaluations in the budget, report the failure rate, and draw the case where the heuristic stops wrongly.
Cases: virtual (pass/fail) constraints handled by a temporary radius cut and re-solve, 15–20% failed evaluations counted in the totals, and the heuristic's failure case drawn [S020 pp. 7–8, 10]; "In our opinion, failure recovery is a necessary ingredient of efficient circuit tuning" with a simulator failure code [S027 p. 5]; recovery from nonworking circuits [S033 abstract].

H1 fold (wording for the editor): "… and if the optimizer needs only the gradient of a scalar merit function, weight the adjoint excitations by the multipliers and run one adjoint analysis; choose direct or adjoint sensitivities by the ratio of parameters to functions" [S039 p. 4; S036 p. 3; S077 abstract; D002 abstract].

---

## 6. Candidate pool (not promoted)

Counts are cards proposing the pattern (full/partial weighted papers in brackets); support from other card fields is named where it matters.

| Candidate | Cards | Why it stays in the pool |
|---|---|---|
| Counterexample as a design and proof tool (necessity of an assumption, against a rival, against a published theorem) | 9 [7]: S003, S005, S007, S018, S022, S028, S052, S107, S126 | Generic mathematical practice (fails exclusivity); listed as proof device P8 |
| Kink-manifold projection; ε-active sets with tolerance halving; factorisation-first design | 11 [4], 3 [3], 4 [4]: S014, S015, S030, S043, S044, S062, S067, S097, S130, S155, S233; S030, S130, S233; S030, S048, S096, S233 | One technical family of 1978–1992; §7.2 A5–A6 and the M5 variant |
| Modular proof reuse as a core method | 7 [7] | M1 step 1 and M3 step 4 already predict it; kept as H11 |
| Staged validation (Tier 0) | 5 [4]: S026, S027, S036, S054, S236 | Folded into M2 (§3 row 18) |
| Fair-to-the-rival benchmarking | 8 [4]: S003, S025, S061, S072, S102, S120, S176, S188 | Folded into M2 step 4; §7.3 E9 |
| Survey as a research agenda | 5 [4]: S001, S009, S061, S080, S086 | Folded into M7 step 6 |
| Report where the method loses | 4 [4]: S020, S049, S056, S066 | Folded into M2 step 5 |
| Checkable certificate as the theorem's interface (pre-DFO) | 3 [3]: S008, S031, S113 | M3 variant (§3 row 19) |
| Geometry calculus (abstract measure ↔ computable matrix) | 3 [3]: S016, S028, S124 | One project; M3 evidence and P6 |
| Reduce to the classical case (global-to-local, TR inactive, one-component check) | 3 [3]: S018, S047, S065 | Proof device P19 |
| Promise-then-deliver sequels | 3 [3]: S018, S021, S107 | Writing move W9 |
| One-factor or factorial variants before external comparison | 3 [3]: S040, S049, S075 | Already M2 step 5; E2 |
| New standard as a superset of the incumbent (SIF ⊃ MPS) | 3 [3]: S046, S137, S149 | One project (SIF) |
| Answer an old question from one's own early work | 3 [3]: S233, S130, S141 | Two questions only (1978 → 1989; 1981 → 2023, posthumous, framed by coauthors) |
| Public erratum crediting the finder | 2 [2]: D001, S059 | Integrity positive model (§3 row 26); three works with the book errata, still not promoted (§12.2) |
| Insurance assumption over all combinatorial branches | 2 [2]: S005, S022 | One project; proof device P9 |
| Recover a forgotten lesson | 2 [2]: S007, S009 | Writing move W10 |
| Rate first, convergence second | 2 [2]: S018, S021 | One project; P11 |
| Complete-results companion reports; failure accounting | 2 [2] each: S103, S120; S040, S102 | M2 evidence; E3–E4 |
| Reformulate before solving | 8 [1]: D002, S015, S027, S043, S053, S055, S067, S116 | M5 step 3 evidence; support from S036, S039, S066, S099, S141 in other fields (A11) |
| Write for both audiences | 5 [1]: S083, S149, S154, S176, S181 | Abstract-level |
| Hybrid family with rival methods as extremes | 2 [1]: S003 (unweighted), S082 | M6 evidence |
| Fix discrete decisions from a cheap solve, then repair | 2 [1]: S060 (unweighted), S099 | One weighted paper |
| Flow-equivalence screening | 2 [0]: S076, S142 | Abstract only |
| From the essay only: interface outranks a factor-two algorithm; topic choice by written criteria; advocacy is part of the project; move on after adoption; low-stake pilots | 1 each: S236 pp. 4, 4 and 6, 3–4, 5, 6 | Single source; M4 step 4 quote, M4 variant notes (§3 row 22), trajectory note (§8.2) |
| Other singletons | 1 each: S008 (graded assumption ladder), S010 (assumption calibrated on own run data; experiments aimed at the predicted constant), S011 (controlled test-variant generation), S012 (delimit an abstraction by its trivial members), S013 (representation chosen for the proof), S017 (physical interpretation as correctness check), S021 (two-layer rate analysis), S036 (make tacit requirements explicit), S065 (budget-regime split across companion papers), S066 (error-budget propagation), S075 (retune an imported device), S085 (structure as a design variable), S111 (report-to-journal revision), S136 (better-than-known as success), S141 (impossibility-first design) | Single paper; several appear in §7 |

---

## 7. Technique inventory

Named devices with the paper and page where they are used.

### 7.1 Proof devices

| # | Device | Where |
|---|---|---|
| P1 | Generalized Cauchy point as a step certificate: any step with a fixed fraction of its decrease is admissible; variants with negative-curvature decrease and a bonus step | S008 pp. 3–4, 7, 11; S031 pp. 17–18; S026 pp. 8–9; S012 pp. 5–6; S056 pp. 6–7 |
| P2 | Radius bounded below by taking the first violating iteration (minimal counterexample) | S008 pp. 14–15; S031 pp. 19–20; S047 pp. 17–20; S013 pp. 18–19; S025 pp. 13–14 |
| P3 | Counting over successful iterations (split k ≤ pS(k); Σ1/b_k finite contradicts the Hessian-growth assumption) | S008 pp. 15–16; S031 p. 21; S047 pp. 20–21; S022 p. 13 |
| P4 | liminf → lim by interleaved subsequences with path length bounded by function decrease | S013 pp. 21–22; S012 pp. 19–21; S031 pp. 22–24 |
| P5 | Criticality coupling Δ ≤ μ‖g‖ transfers model-gradient convergence to the true gradient; Δ → 0 as stopping test | S013 pp. 16–17, 20; S012 pp. 18–19; S025 pp. 14–15; S065 p. 10; S075 pp. 6–7 |
| P6 | Interpolation-geometry calculus: Λ-poisedness ↔ ‖M⁻¹‖, cancel the value error by subtracting one interpolation equation, prove on the unit ball then rescale, pivot-threshold bounds, greedy existence, poisedness kept under exchange | S016 pp. 6–13, 15–23; S028 pp. 4, 9–13, 24; S124 pp. 8–10, 17; S013 pp. 10–13; S019 pp. 13–14 |
| P7 | Parameter bounded away from zero: assume the reduction step fires infinitely often, show the acceptance test eventually always holds | S005 pp. 17–19; S007 pp. 44–47; S022 pp. 20–23; S107 pp. 19–23; S054 p. 15; S126 pp. 15–16 |
| P8 | Necessity by a constructed admissible iterate cycle or a small counterexample; the same against a rival or a published theorem | S005 pp. 21–25; S007 pp. 20, 47–51; S126 p. 8; S031 pp. 54–55; reused S022 p. 24, S107 p. 24; S018 pp. 14–15; S003 pp. 4–5; S028 pp. 19–20; S009 pp. 7–8 |
| P9 | Finitely many active or dominant index sets: fix one along a subsequence; an "insurance" assumption over every subset | S005 pp. 13–14; S022 pp. 8–9, 15; S107 p. 14; S026 pp. 26–27 |
| P10 | Active-set identification: dominated/floating split, strongly vs weakly active, Moreau decomposition, strict-complementarity pairing | S005 pp. 5–6; S007 pp. 10–11; S008 pp. 20–22; S022 pp. 14–15; S107 p. 12; S113 p. 19; S074 p. 15; S031 p. 8 |
| P11 | Range/null error split with a 2-step contraction; rate proved first, local convergence after | S018 pp. 8–13; S021 pp. 10–12, 20–26; S030 pp. 18–22 |
| P12 | Bounded deterioration in a weighted norm; Banach perturbation lemma inside an induction | S021 pp. 15–17, 24–25; S056 pp. 11–12; S049 p. 7 |
| P13 | Averaged Hessian and the direction-to-matrix lift ‖A‖ ≤ ‖AS‖/σ_min(S); a bound computable from a run | S010 pp. 10–12 |
| P14 | Factorisation certificates: inertia identity, Fredholm alternative, negative curvature from LDLᵀ, exact Schur-complement cancellation | S096 pp. 4–11; S049 pp. 8–9; S089 pp. 7–9; S054 pp. 7–8; S126 pp. 7–8 |
| P15 | Proof by reuse: revisit only the places where the changed assumption is used | S113 pp. 9, 17; S031 pp. 57–58; S022 pp. 13–15; S025 p. 12; S074 pp. 10, 12; S058 p. 6; S155 pp. 27–35 |
| P16 | Inexactness bounded by a fraction of the predicted decrease; noise ratio inserted in the ratio lemma | S066 pp. 5–6; S031 pp. 57–58; S019 p. 12 |
| P17 | Alternatives and duality: Gordan, Fredholm, LP weak duality as a stopping certificate, duality chain | S130 p. 22; S096 p. 6; S031 pp. 50–51; S017 p. 2; S060 pp. 29–30 |
| P18 | Finite termination because sign patterns cannot recur; impossibility results fix the minimal form before construction | S155 p. 26; S141 pp. 4–7 |
| P19 | Reduce to the classical case: global method reduces to a local algorithm; trust region inactive so the classical local proof applies; one-component reduction | S018 pp. 7, 14; S008 pp. 19–22; S065 pp. 13–17; S047 pp. 10, 14 |
| P20 | Descent for max-type functions from cadre multipliers (gradient as a convex combination of differences) | S130 pp. 22–23; S108 pp. 7–9, 11–12; S164 pp. 8, 18–19; S233 pp. 2–3 |

### 7.2 Algorithm-design moves

| # | Move | Where |
|---|---|---|
| A1 | Specify each component only by the checkable property the proof uses (inner stopping test on a criticality measure; model class by error bounds plus a finite improvement procedure) | S005 pp. 7, 27; S007 pp. 14, 27; S013 p. 13; S022 pp. 5–6; S058 pp. 6–7; S012 pp. 7–8; S113 pp. 5, 14–19; S031 pp. 9–11 |
| A2 | Two-regime outer loop: a sure-to-converge fallback and a fast mechanism switched by one test; tolerances as powers of the penalty parameter | S005 pp. 7–8, 18–19; S007 pp. 12–13, 20; S022 p. 6 |
| A3 | Fallback direction from the same factorisation, switched by a slope test | S054 pp. 6–11, 14; S126 pp. 12, 14; S017 p. 10 |
| A4 | Split by type: cheap or linear parts handled exactly, only the hard part penalised or modelled; per-component radii or penalties | S005 pp. 1, 4; S020 pp. 3, 5–8; S022 pp. 2, 6; S047 pp. 5–6, 11–12; S074 p. 2; S080 p. 12; S089 pp. 4–7; S113 pp. 3–4, 20–22; S126 pp. 2–3; S141 p. 4; S108 pp. 15–16 |
| A5 | Horizontal/vertical step for max-type or kinked objectives; ε-active working set with tolerance halving; multiplier signs for multiple dropping | S233 pp. 2–7; S030 pp. 5–10; S108 pp. 5, 9–16; S130 pp. 17–23; S164 pp. 10–13, 19–20; S014, S015, S044 abstract |
| A6 | Factorisation-first: one QR or LDLᵀ gives direction, optimality test and certificate; constant columns first | S233 pp. 4–5, 7; S030 pp. 15–16; S048 pp. 11–17; S096 pp. 5–7 |
| A7 | The radius shrinks only when the model was certified; otherwise repair the geometry and keep the radius | S009 pp. 9–10; S013 p. 14; S020 pp. 4–5; S025 pp. 7–9; S075 pp. 6–7 |
| A8 | Evaluation economy (H12) | S019 pp. 6–10, 12; S013 pp. 15, 17; S020 p. 6; S026 pp. 8–9; S066 pp. 9, 14; S009 pp. 14–15 |
| A9 | Cheap bonus step credited in the acceptance ratio; closed-form updates of variables of known form | S056 pp. 4–7, 13–15; S027 p. 5 |
| A10 | Reuse inner-solver byproducts (CG directions, Rayleigh quotients) | S058 pp. 4, 8–10 |
| A11 | Reformulate before solving: max → epigraph inequalities; semi-infinite → integral equality; robust min-max → bilevel; trigonometry-free velocities; logical constraints → quadrant penalty | S027 p. 2; S036 p. 5; S039 pp. 2–3; S066 pp. 16–17; S099 pp. 6–10; S141 pp. 4, 11 |
| A12 | One adjoint for the merit-function gradient; direct vs adjoint by the parameter/function ratio | S039 p. 4; S036 p. 3; S077, S033, D002 abstract |
| A13 | Failure recovery (H13) | S020 pp. 7–8; S027 p. 5; S026 p. 8 |
| A14 | A parametrised family whose extremes are the rival classical methods | S003 pp. 3, 9–10; S082 pp. 3, 5–6 |
| A15 | Import a device and retune it to the host's evaluation economics | S075 pp. 13, 20 |
| A16 | Trust-region ratio test to stabilise a non-NLP method (cutting-plane dual) | S060 pp. 18–19 (unweighted; listed in the catalog only as an illustration) |
| A17 | Fix discrete decisions from a cheap continuous solve, then repair or prove globally | S060 pp. 19–20; S099 pp. 19–20 |
| A18 | Noise level and physical units as algorithm parameters | S019 p. 12; S036 p. 5; S031 pp. 57–58; S025 pp. 17–19 |
| A19 | Warm starts from structure (multipliers 1/n, previous inner solution, linear surrogate of the solution map, alternative first step after a parameter change) | S027 p. 4; S074 pp. 3, 7; S066 pp. 12–13; S082 pp. 5–6 |
| A20 | Treat the user's given structure as a design variable (element merging) | S085 pp. 2, 6–7 |

### 7.3 Experiment protocols

| # | Protocol | Where |
|---|---|---|
| E1 | Testing twin: test exactly the analysed class, check deviations against the theory, fix failures within what the theory allows | S011 pp. 3, 5, 19–20; S040 pp. 7–16 |
| E2 | One-change variants around a printed default, or a full factorial of own options, before any external comparison; best and worst over a parameter box | S011 p. 10; S040 pp. 32–34; S049 p. 10; S058 pp. 12–16; S075 pp. 19–22; S030 p. 26 |
| E3 | Coded failure taxonomy, same-answer filter, symmetric accounting of false failures and false successes | S040 pp. 34, 38; S103; S102 pp. 12–14; S120 p. 27; S019 p. 17; S049 p. 10 |
| E4 | Complete per-run results in a companion report | S103 pp. 1–2; S120 pp. 2, 27; S030 pp. 4, 27 |
| E5 | Cost unit = what the user pays: function and gradient calls; CPU and linear-algebra counts when evaluations are cheap; two units side by side | S011 p. 22; S020 p. 10; S019 pp. 15–18; S058 p. 3; S049 pp. 10–11; S120 pp. 28–50 |
| E6 | Two tiers: public collection plus application instances | S020 pp. 8–10; S056 pp. 16–23; S075 pp. 17–23; S108 pp. 20–22; S017 pp. 11–18; S027 pp. 5–7; S236 p. 6 |
| E7 | Noise protocol: same problems noiseless and at two levels, the method and the baseline given the true level; data profiles with deterministic noise and tolerances at the noise level | S019 pp. 17–18; S025 pp. 17–19; S065 pp. 23–24 |
| E8 | Stress variants: bounds around the unconstrained solution, degenerate variants that break an assumption, a conditioning knob, published generators and seeds | S011 p. 11, appendix pp. 24–25; S010 pp. 13–14, 21; S049 pp. 10, 20–21; S096 pp. 14–16; S048 pp. 18–20 |
| E9 | Fair to the rival: rival's author as coauthor; own-code expertise bias declared; rival re-implemented on the same simulator; rerun on the earlier study's machine and instances; baselines as ablations; one-component swap to explain a gap; targeted diagnostic rerun; fixed problem list and compulsory defaults | S102 p. 2; S061 p. 25; S027 p. 6; S017 p. 14; S025 p. 16; S003 pp. 15–16 (unweighted); S040 pp. 36–37; S188 pp. 5, 7 |
| E10 | Tier 0: analytic prototype with exact gradients; synthetic sequences; prototype subclass with known baselines; right-sized synthetic model; final designs re-evaluated by a reference simulator | S027 p. 5; S010 pp. 14–19; S026 p. 30; S054 p. 27; S236 p. 6; S036 pp. 2, 6 |
| E11 | Stratify results by the structural feature the design says matters | S102 pp. 15–18; S017 p. 13; S096 pp. 14–16 |
| E12 | Report adoption and where time goes (users, sessions, problems, runs; simulation vs optimizer time) | S036 p. 6; S027 p. 6 |
| E13 | Disclose excluded problems and starting-point feasibility; data profiles counting feasible solutions only | S075 pp. 17–19 |
| E14 | A win/lose regime conclusion tied to tables; a dedicated section for the bad cases | S049 p. 19; S056 pp. 19–24; S020 pp. 7–8 |

### 7.4 Writing moves

| # | Move | Where |
|---|---|---|
| W1 | Numbered comments after the algorithm: what practical codes do differently, own weak spots and remedies | S013 pp. 15–16; S019 pp. 13–15; S022 p. 7; S031 (remarks after the algorithm) |
| W2 | Map each result by number to its predecessor; spend prose only on what is new | S022 pp. 13–15; S007 p. 8; S113 p. 9 |
| W3 | Derivative triage in the introduction, one sentence per route | S009 pp. 3–4; S019 p. 3; S020 pp. 2–3 |
| W4 | Gap statement as categories of prior methods, each with the property it lacks | S012 p. 2; S021 pp. 5–6; S017 pp. 2–4; S080 pp. 9–11 |
| W5 | Close a survey with the group's own agenda | S009 p. 17; S061 pp. 15–22; S080 pp. 16–17; S086 pp. 15–16 |
| W6 | Calibrated claims ("competitive", "complement each other", "appears preferable"); package-specific and general conclusions kept apart | S075 pp. 1, 22–23; S102 p. 17; S108 pp. 18–19; S010 p. 20; S048 p. 21; S040 p. 50; S236 p. 6 |
| W7 | Say what is proved and what is only observed | S074 p. 3; S048 p. 21; S011 p. 20 |
| W8 | Public errata that keep the statement and numbering and credit the finders | D001 p. 1; S059 pp. 1, 4 |
| W9 | A future-work paragraph that names the next theorem, delivered in the sequel | S018 p. 15 → S021 p. 6; S005 p. 4 → S022; S113 p. 25 → S107 |
| W10 | Recover a forgotten lesson (1970s barrier ill-conditioning; Winfield's overlooked interpolation trust region) | S007 pp. 4–5; S009 pp. 5–6 |
| W11 | The smallest degenerate example (six points on a circle) | S009 pp. 7–8; S016 p. 6 |
| W12 | Infrastructure papers: numbered design requirements with their costs; user-question order and a session transcript; each manual chapter ends with the problem class now expressible | S046 pp. 11–13; S004 pp. 3, 35–39; S149 pp. 30, 38 |
| W13 | Table of constants with mnemonic subscripts and a roadmap before the analysis | S012 p. 4 |
| W14 | Justify infrastructure by the scientific failure it prevents | S137 p. 2 |
| W15 | Essay voice: highlights and lowlights side by side, aphorisms, concrete figures, footnotes for non-specialists | S236 pp. 2–6 |

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period (carded works; full/partial reads in brackets)

Columns: PEN penalty and nondifferentiable NLP; MMX minimax, ℓ₁/ℓ∞ fitting and piecewise-linear; LOC location and network problems via continuous methods; NLA numerical linear algebra; TR derivative-based trust-region and quasi-Newton theory; AL augmented Lagrangian, barrier and primal-dual; SW software, input formats and testing; SRV surveys, books and editorial; DFO derivative-free optimization; CIR circuit and microwave design; ENE energy, petroleum and industrial systems; MIX MINLP and mixed discrete applications; ML IBM machine-learning and imaging teams.

| Period | Works | PEN | MMX | LOC | NLA | TR | AL | SW | SRV | DFO | CIR | ENE | MIX | ML |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1972–1979 | 11 | 4 [0] | 6 [1] | | | | | | | | 1 [0] | | | |
| 1980–1984 | 15 | 8 [5] | 3 [0] | 2 [0] | 1 [1] | | | | 1 [0] | | | | | |
| 1985–1989 | 11 | 1 [0] | 4 [2] | 1 [0] | | 2 [2] | | 2 [2] | 1 [0] | | | | | |
| 1990–1994 | 25 | | 3 [2] | 3 [0] | | 6 [6] | 3 [3] | 6 [3] | 3 [2] | | | 1 [0] | | |
| 1995–1999 | 28 | | 1 [0] | | | 3 [3] | 5 [5] | 5 [4] | 3 [1] | 4 [4] | 6 [3] | 1 [0] | | |
| 2000–2004 | 12 | | | 1 [1] | | | 2 [2] | 2 [1] | 3 [0] | 1 [1] | 3 [0] | | | |
| 2005–2009 | 10 | | | | | | | | 1 [1] | 4 [3] | 1 [0] | 3 [0] | 1 [1] | |
| 2010–2014 | 15 | | | | | | | | 1 [0] | 4 [3] | | 10 [2] | | |
| 2015–2019 | 7 | | | | | | | | | 2 [1] | | 1 [0] | 2 [1] | 2 [2] |
| 2020–2023 | 4 | | | | | | | | | 1 [0] | | | 2 [2] | 1 [1] |

Topic assignment is by card content (title, contribution and D1 fields). Members: PEN D001, S018, S021, S024, S030, S038, S045, S052, S053, S090, S096, S104, S134; MMX S014, S015, S042, S051, S067, S069, S071, S072, S093, S108, S109, S116, S130, S155, S164, S202, S233; LOC S017, S029, S041, S043, S044, S062, S114; NLA S048; TR S008, S010, S031, S047, S049, S056, S058, S059, S082, S085, S089; AL S005, S007, S022, S026, S054, S074, S107, S111, S113, S126; SW S004, S006, S011, S040, S046, S078, S102, S103, S117, S120, S137, S149, S178, S186, S188; SRV S001, S061, S073, S080, S086, S121, S127, S152, S175, S181, S214, S224, S236; DFO S002, S009, S012, S013, S016, S019, S020, S023, S025, S028, S065, S066, S075, S091, S124, S135; CIR D002, S027, S033, S036, S039, S055, S077, S097, S106, S154, S176; ENE S060, S076, S079, S083, S084, S098, S100, S101, S105, S132, S136, S140, S142, S147, S161, S171; MIX S003, S063, S099, S141, S166; ML S032, S057, S123.

### 8.2 Turns

1. **Penalty and nondifferentiable methods, sole-authored and then with students (1972–1985).** Thesis and the 1973 nondifferentiable penalty [S134 metadata; S024 abstract]; direct minimax methods built on the solution's characterisation [S233 p. 1; S014 abstract]; ℓ₁ fitting with Bartels [S015, S042 abstract]; the exact-penalty programme with Coleman [S018; S030; S021]. The numerical-linear-algebra emphasis is credited to Bartels [S233 p. 9].
2. **Trust regions, bounds and testing with Gould and Toint (1984–1989).** Directions of infinite descent with Gould [S096]; the 1988 theory/testing twin [S008; S011], whose closing programme is the LANCELOT plan [S011 p. 24]; the LANCELOT design statement [S046 pp. 11–13]. Conn–Li minimax work continues in parallel [S130; S164; S108].
3. **LANCELOT as a research engine (1990–2000).** The move to IBM in 1990 [S236 p. 2] does not change this line: SIF [S149; S137], the book [S006 abstract], the options study [S040; S103], CUTE [S004], the MINOS comparison [S102; S120], and the audit-driven follow-ups (§4) [S089; S007; S022; S054; S058; S074; S082; S085; S047; S026].
4. **Two IBM lines start in 1996.** DFO with Toint, from applications "presented to the authors" [S009 p. 3; S013 p. 2], named in the 1996 paper [S019 pp. 2–3]; circuit tuning from an engineer's minimax question [S236 p. 3; S036]. The circuit line is gradient-based [S027 p. 4], and his 1970s minimax expertise returns as a smooth reformulation [S036 p. 5; S027 p. 2].
5. **DFO theory consolidation (2003–2012)** with Scheinberg and Vicente [S124 → S016, S028 → S012; S002 abstract], then structured DFO [S025; S065; S066].
6. **Industrial diversification (2004–2015).** MINLP with CMU [S236 pp. 4–5; S003]; petroleum as first-of-a-kind projects, entered deliberately once circuit tuning was routine ("make a splash in a new area") [S236 pp. 5–6; S098, S161, S171, S100, S076, S142 abstract]; maintenance scheduling [S236 pp. 6–7; S101 abstract]; NTNU operations work [S060; S105, S132, S084, S147 abstract]; the grid white paper [S136]. Known mostly from abstracts.
7. **Hybrids with the MADS school and air traffic with ENAC (2013–2018)** [S023 abstract; S075; S091 abstract; S063 abstract; S166].
8. **Posthumous (2020–2023)** [S032; S135 abstract; S099; S141].

### 8.3 What stayed constant

- The trust region as the default globalisation device: bounds (1988) [S008], convex sets [S031], element radii [S047], DFO [S013; S012], least squares [S025], a cutting-plane dual [S060 pp. 18–19], the progressive barrier [S075].
- Penalty functions from the thesis to the posthumous papers: S134 → S024 → S018/S030 → S045 → S005 (augmented Lagrangian) → S007 (Lagrangian barrier) → S091 (ℓ₁ and AL inside MADS, abstract) → S135 (abstract) → S141, which answers his 1981 question [S141 pp. 4, 13].
- Working on the structure rather than around it: kinks [S233], partial separability [S046; S149], slacks [S089], residuals [S025], nesting [S066] (M5).
- Shared problem sets and evaluation counts: 1988 [S011 p. 22] to 2018 [S075 pp. 17–23] (M2).
- Engineering users: microwave networks in 1975 [S097 abstract; S233 pp. 9–10], circuit designers in the 1978 minimax abstract [S014 abstract], IBM circuits 1996–2005 [S036; S027; S039].

### 8.4 Where the stated agendas went

| Stated as next | Later |
|---|---|
| AL with bound-constrained subproblems [S011 p. 24] | S005 (1991); LANCELOT [S006 abstract] |
| Full quasi-Newton version of the exact-penalty method [S018 p. 15] | S021 (1984) [S021 p. 6] |
| Sequel to the 1991 AL paper [S005 p. 4] | S022 (1996) |
| LANCELOT weak points 1 and 3 [S040 p. 49] | S089 (1994), S007 (1997) |
| Further developments after the 117-hour run [S061 pp. 15–22] | S085, S082, S113/S107, S058 |
| Comparing modern algorithms, noise understudied [S080 p. 17] | S102 (1997); noise in DFO [S019; S025] |
| DFO open problems: geometry vs cost, initial models with fewer points, structure, noise via regression, software [S009 p. 17] | S016 p. 19 (2008); S028 underdetermined and regression models (2008) [S028 pp. 2, 17, 27]; S025 (2010); S020 (1998) and the DFO manual [S178 metadata] |
| Practical performance of the 1984 quasi-Newton method [S021 p. 26] | Not in the cards |
| Prove uniform bounds for Powell-like rules [S016 p. 24] | Not in Conn's cards |
| Measure how often geometry improvement is needed [S075 p. 23] | Open |
| Maintenance scheduling for several dependent facilities [S236 pp. 6–7] | S101 (2010) treats one installation (abstract); the generalisation is not in the cards |
| Whether penalty functions help discrete or global optimization (1981) [S141 p. 4] | S141 (2023), by his coauthors |

---

## 9. Collaboration pattern

Research works only (edited volumes, special issues, forewords and the book review excluded); same-work pairs merged; coauthors appearing at least twice in the period.

| Period | Works | No coauthor | Distinct coauthors | Frequent coauthors (count) |
|---|---|---|---|---|
| 1972–1989 (Waterloo) | 35 | 7 (S024, S053, S071, S090, S104, S134, S233) | 11 | Bartels 8, Gould 6, Coleman 5, Y. Li 4, Toint 4, Charalambous 3, Calamai 3 |
| 1990–1995 (IBM; LANCELOT) | 25 | 1 (S186) | 13 | Toint 18, Gould 17, Sartenaer 3, Bongartz 2 |
| 1996–2005 (DFO, circuits) | 31 | 0 | 26 | Toint 17, Gould 12, Visweswariah 10, Scheinberg 5, Haring 4, Sartenaer 3, Coulman 2, Morrill 2, Wu 2, Vicente 2, Orban 2 |
| 2006–2018 (energy, structured DFO, MADS) | 30 | 2 (S152, S236: essays) | 70 | Scheinberg 7, Vicente 5, H. Zhang 4, Foss 4, Mello 3, Horesh 3, Jimenez 3, van Essen 3, Gunnerud 3, Le Digabel 3, Wächter 2, Knudsen 2, Grossmann 2, Mongeau 2, Audet 2 |
| 2019–2023 (posthumous) | 4 | 0 | 12 | Cafieri 2, Mongeau 2 |

Overall most frequent (all cards): Toint 44 cards (1988–2003), Gould 40 (1984–2003), Scheinberg 12 (1997–2010), Visweswariah 11 (1996–2005), Bartels 8 (1977–1989), Coleman 7 (1980–1984; co-editor 1997), Vicente 7 (1999–2012), Mongeau 6 (1992–2023), Y. Li 6 (1988–1992), Sartenaer 6 (1993–1996) [coauthor fields of the cards].

- **One long trio per era.** CGT: Gould from 1984 [S096] and Toint from 1988 [S008] to 2003 [S137], with Sartenaer [S031; S113; S107; S022; S047; S058], Bongartz [S004; S102] and Orban [S026; S137] as fourth authors; CST, then CSV for DFO [S009; S013; S020; S124; S016; S028; S012]. SKILL.md's "long-lived trios" limitation of M1 is confirmed.
- **Waterloo: a colleague and three students.** Bartels on ℓ₁/ℓ∞ [S015; S042; S072 abstract], students Coleman [S018; S030; S021], Calamai [S041; S062; S044 abstract] and Li [S130; S164; S108]; sole-authored research papers only before 1980 [S024 abstract; S053 abstract; S233].
- **Domain experts as coauthors in the users' venues.** IBM circuit engineers [S036; S027; S039]; NTNU and Statoil-side engineers [S060; S105, S132, S147 abstract]; Shell/IBM history matching [S100, S076, S142 abstract]; ENAC air-traffic researchers [S099; S141]. The essay names them as the reason the circuit project got off the ground [S236 p. 4].
- **The rival school as coauthor.** MINOS's author on the LANCELOT–MINOS comparison [S102 p. 2]; the MADS group on both hybrid directions [S075; S023 abstract]; the combinatorial school for a network penalty method [S114 abstract] and facility location [S043 abstract].
- **Longest collaboration outside the trio**: Mongeau, from discontinuous piecewise-linear optimization at INRIA (1992) [S155] to the posthumous air-traffic papers (2023) [S099; S141].
- **Team papers grow after 2006**: 70 distinct coauthors in 2006–2018, driven by large IBM and industry teams [S136 (16 authors); S003 (11); S076 (8 abstract)]; Conn's personal contribution is often not identifiable [S003 header; S060 header] or explicitly "minimal" [S236 p. 5].

---

## 10. Rejected updates

1. **"Split by type" as a new core method** (12 weighted papers). It is M5 step 4 generalised; a separate method would duplicate M5. Add the cases to M5 (§3 row 20) instead.
2. **"Theory aimed at the code actually run" as a new core method** (10 papers). It is the direction of M1 and the positive form of M1's existing anti-pattern; no eighth slot. Variant note on M1 (§3 row 15).
3. **"Characterisation-driven design / the Waterloo nonsmooth toolkit" as a core method.** Passes the checks, but the full-text evidence is mostly one line with Li [S108; S130; S164] plus S233 and S030, the rest abstract-level, and it is period-bound (1978–1992). M5 variant plus §7.2 A5–A6.
4. **"Counterexample as a design tool" as a heuristic** (9 cards). Generic mathematical practice; it would not identify Conn. Kept as P8.
5. **"Modular proof reuse" as a core method.** It is what M1 step 1 and M3 step 4 predict; kept as H11.
6. **"Survey as a research agenda" as a separate heuristic.** Becomes M7 step 6.
7. **H6 and H7 as separate heuristics.** They restate M1 step 4 and M2; fold them in as cases to keep the list at 10.
8. **Middle-author and role-unidentifiable papers as evidence** [S032/S123; S057; S003; S060]. Excluded, including the M2 ✗ on S057.
9. **Removing integer variables from the weak spots.** Narrow the wording only: no Conn-led integer method, and he calls his MINLP contribution minimal [S236 p. 5].
10. **Essay-only patterns as heuristics** (interface outranks a factor-two algorithm; written topic-choice criteria; advocacy; move on after adoption; low-stake pilots) [S236 pp. 3–6]. One source each; use as M4 quotes and variant notes.
11. **Energy-era practice as new M4 evidence at method level.** Only abstracts and one role-unidentifiable full text [S060]; keep as trajectory.
12. **"Write for both audiences" as a heuristic.** Four of five cards are abstract-level [S083, S154, S176, S181].
13. **Any change to Tension 3 or the IBM promotional numbers.** No card touches them.
14. **Findings from reading notes** (typos, tables that disagree with the text, carried-over results). Not used, per the rules at the top.

---

## 11. Open gaps

- **The books** (S001 *Trust-Region Methods*, S002 *Introduction to DFO*, S006 LANCELOT) have no open full text: their organisation, the software chapter and the convergence analyses are known from publisher descriptions only [S001, S002, S006 abstract]. For *Introduction to DFO* the organisation is now read from the contents, with errata, an addendum and two reviews (§12); the chapters are still unread.
- **1970s work**: only S233 is read in full; the 1973 penalty paper, the 1977 direct penalty method, the minimax and ℓ₁ papers are abstracts [S024; S038; S014; S015; S051 abstract]; the thesis itself is metadata only [S134]; its title and advisor (Pietrzykowski) come from the coauthors' posthumous paper [S141 pp. 3, 13].
- **2001–2015**: 12 of 33 works read; the petroleum, seismic, maintenance and NTNU papers are abstracts [S098; S161; S171; S101; S083; S100; S105; S132; S084; S076; S147; S142], and the one full text is role-unidentifiable [S060]. M4's energy-era practice rests on these abstracts and the essay [S236 pp. 5–7].
- **Key hybrid and circuit papers are abstract-level**: Conn–Le Digabel 2013 [S023], the QCQP subproblems in MADS [S091], JiffyTune TCAD [S033], EinsTuner FGCS [S106], the 2022 derivative-free exact penalty [S135]. H4's "significantly improved" rests on the S023 abstract plus S075 p. 19.
- **The 2011 SIAM News essay** with the same title as S236 was not read [S152 metadata]; it may be a later version.
- **Versions**: the published S049 chapter, the SIOPT version of S093 and the published S003 were not compared with the reports read [S049 header; S093; S003 header].
- **Scans**: eight early papers have page references but no verified quotes; OCR text exists for checks [S018; S021; S030; S046; S048; S108; S130; S164]. Several OCR'd tables are scrambled [S049 header].
- **Patents** (13, 1999–2021, including the SAGD well-control family) were skipped; they may document the late IBM industrial work [INDEX.md Role = skip].
- **Code**: the DFO package, LANCELOT and CUTE sources were not inspected; the DFO v1.2 manual is metadata only [S178].
- **Supervision and group practice**: the essay says nothing about students, supervision or how he wrote papers [S236 D8]; there are no memoirs, recordings or referee reports. The Mentor Voice remains constructed, now with verified first-person aphorisms available [S236 pp. 3–5].
- **Figures**: the LANCELOT study's figures and the 2018 profiles survive only as captions and prose [S040 header; S075 header].


---

## 12. Book material (batch k01, added 2026-09-27)

Input: `cards/k01.md` and `k01.digest.json`, six items around *Introduction to Derivative-Free Optimization* (IDFO; Conn, Scheinberg and Vicente, SIAM 2009), all read in full:
- B001, the table of contents (book pp. vii–ix);
- B002 and B003, the authors' errata lists for the first printing (18 items) and the second printing (3 items), both dated 05/17/2015;
- B004, the authors' two-page addendum of 01/27/2011 deriving the quadratic-regression error bounds (the book's Theorem 4.13);
- B005, J. L. Nazareth's review (*Math. Comp.* 79(271), 2010, pp. 1867–1869; DOI 10.1090/S0025-5718-10-02379-3, verified on Crossref);
- B006, D. Orban's review (*SIAM Review* 53(2), 2011, pp. 395–396).

**Voices and weight.** B001–B004 are the three authors' joint voice; Conn's personal share cannot be separated, so they weigh like the CSV papers. B005 and B006 are external reviewers; they are used only as reception, peer view, blind spots and domain fit, never as evidence of Conn's practice, and book passages they quote are marked *relayed*. The book body (S002) is still unread: claims about chapter content go no further than section titles, the errata's page references and the reviews. These six items are **not** added to the paper counts or say–do tallies of §1–§2; SKILL.md cites them by id.

**Date of B006.** The batch file, INDEX.md and the digest gave 2010. Crossref places the Book Reviews section of *SIAM Review* 53(2) (2011, online 5 May 2011) at pp. 375–405 (DOI 10.1137/SIREAD000053000002000375000001), and its editor's note lists a derivative-free-optimization review. The review is therefore from 2011, which the card had inferred from a same-page review of a 2011 book [B006 p. 1]. Recorded here, in `07-paper-cards.md` and in RESOURCES.md; on review the digest, INDEX.md and `works.json` were also set to 2011 (§12.6); the local text file keeps its 2010 name.

### 12.1 What the book material adds or changes, per SKILL.md item

| SKILL.md item | What the book material shows | Cards (pages) | Change |
|---|---|---|---|
| M1 triad | At book level only the theory leg is present: no chapter or section title announces a numerical study; software is a four-page appendix; the named practical methods come after the theory (Ch. 11). Peers: "few numerical illustrations" and no implementation details; the introduction holds "the only comparison between methods"; the pointed-to software is "research grade". The relayed preface aim ties the theory to "what is needed to ensure convergence, how it affects algorithm design". Consistent with M1's "assembled across a line of papers": the code is the DFO package [S020], the numbers are in the papers [S019; S025; S075]. | B001 p. 3; B005 pp. 1, 3; B006 pp. 1–2 | ⚠ variant bullet "Book level" on M1; ledger `#method-1` |
| M2 test bed | Comparing derivative-free methods "is intricate and is not an objective of the book" (the authors' stance as relayed by Orban); no section title mentions benchmarking. M2 lives in the papers. | B006 p. 1; B001 pp. 1–3 | ⚠ ledger `#method-2` only; SKILL.md unchanged (no new instruction) |
| M3 certify | **Stated by organisation** (contents, title level): Part I (Chs 2–6, about 100 book pages) of model and geometry theory before every optimization framework of Part II (Part I itself holds the pivotal and geometry-improvement algorithms of §§6.3–6.4, and §1.4 already runs Nelder–Mead); a chapter per sample-set regime (Chs 3–5); Ch. 6 "Ensuring well poisedness and suitable derivative-free models"; Ch. 10 states "Conditions on the trust-region models" (10.2) before the methods and their first- and second-order convergence. **Step 1 in full** for quadratic regression: bounds of fully quadratic form whose geometry dependence is one scale-free norm. **Variant**: 13 of the 18 first-printing errata fall in Part I, including the rewritten linear-regression Theorem 2.13 and the replaced quadratic-regression constants; two of the three errors that survived the reprint are regression statements. **Peer view**: the trust-region chapters are "the centerpiece"; Part I's rigor makes Nelder–Mead "almost a simple and didactic illustration of the direct-search framework". | B001 pp. 1–3; B004 pp. 1–2; B002 pp. 1–3; B003 p. 1; B005 p. 2; B006 p. 2 | "Stated (book organisation, 2009)" line and ⚠ "Step 1's constants are error-prone" on M3; ledger `#method-3` |
| M3 limitation "Assumes smoothness"; Roundtable blind spots | Nazareth: the DFO/non-differentiable intersection "not adequately addressed" (a flaw). Orban, on the trust-region model-based chapters: the book assumes a Lipschitz-continuous gradient or Hessian, a different context from the 30 nonsmooth pages of *Trust-Region Methods* (not a flaw). ⚠ Neither places nonsmooth problems wholly outside the book: the contents list §7.4 "Global convergence in the nonsmooth case" (B001 p. 2), and Nazareth reports that Ch. 7 covers "both continuously differentiable and nonsmooth cases" (B005 p. 2). | B005 pp. 2–3; B006 p. 2; B001 p. 2 | Cited in the Roundtable blind spots; ledger `#method-3`, `#book-material` |
| M6 transplant | Both schools in one book, each with framework and convergence sections; rival methods (Powell's methods, wedge methods) beside the authors' "DFO" approach (title level; a survey textbook covers rival methods as a matter of genre, so weak evidence, house rules §3.4). Orban: the "clearly stated similarities and differences" between smooth and derivative-free trust-region methods. | B001 pp. 2–3; B006 p. 2 | Practice item on M6; ledger `#method-6` |
| M7 | Not engaged: no solver is involved. | — | None |
| Taste mark 1 | The caveat "rarely in one paper" holds at book level (see M1). | B005 p. 3 | Ledger only |
| Taste mark 2 | Theory stated for frameworks: section titles 7.2, 9.1, 10.1. | B001 pp. 2–3 | Ledger only |
| Taste mark 6 | Ch. 6 title; model quality as one computable number ‖M̂†‖. | B001 p. 2; B004 pp. 1–2 | Ledger only (the M3 stated line carries it) |
| Taste mark 7 | ⚠ The authors correct their own released book in public; the list credits readers who pointed out errors (four named); whether any correction came from the authors' own checking is not stated. | B002 p. 3; B003 p. 1 | Ledger only |
| Warning sign 7 | (section title only) §1.3 "Limitations of derivative-free optimization" comes before §1.4 "How derivative-free algorithms should work"; Orban praises the account of both families' limitations. | B001 p. 1; B006 p. 1 | Evidence added to sign 7; ledger `#taste-warnings` |
| Workflow B | Ch. 10's order (framework → conditions on models → first-order → second-order → larger balls → subproblem) is the order of steps 1–4, at title level. | B001 p. 3 | Ledger `#workflow-b` only |
| Honest Boundary, integrity positive model "public errata keep the statement and credit the finders [D001; S059]" | The book errata credit four named finders (✅) but change statements: Theorem 2.13's statement and constants, several definitions (⚠); a note says when the printed statement would still hold. | B002 pp. 1–3; B003 p. 1 | Qualified in the "Stated vs practised" line; catalog W8 variant |
| Honest Boundary, books gap | Six open items read in full; the book body still unread. | B001–B006 | Gap sentence extended; coverage bullet notes the six cards sit outside the counts |
| Domain fit (hyperparameter tuning) | Orban: the introduction's first example, parameter tuning, is "a nonsmooth noisy problem"; in his paragraph on the trust-region model-based chapters, the book assumes a Lipschitz-continuous gradient or Hessian. That the example lies outside the class the theory covers is the card's inference. | B006 pp. 1–2 | Added to Domain fit; ledger `#book-material` |
| Roundtable "Leads when … dimension in the tens" | Nazareth sizes the book's problems at "say up to a hundred" variables. | B005 p. 1 | Consistent; not changed (§12.4 item 6) |
| Signature Work 1, Reception | Orban: "bound to become the de facto authoritative text"; Nazareth: the trust-region chapters "the centerpiece", goals met "admirably", nonsmooth overlap "not adequately addressed". | B005 pp. 2–3; B006 pp. 1–2 | Reviewer line in the Reception row; ledger `#signature-work-1` |
| Research Trajectory | The book was maintained: addendum 2011, errata for two printings 2015. No new edition. | B002 p. 1; B003 p. 1; B004 p. 1 | Ledger `#trajectory` only |
| Technique catalog | P6 gains its regression form; new P21 (check the model form a borrowed proof assumes); W8 gains the book-errata variant; new writing moves W16–W19 (limitations before prescriptions; parallel chapter templates; tools apart from algorithms; hedge words corrected as claims). | B001–B004, B006 | `technique-catalog.md` |

### 12.2 Candidate pool

| Candidate | Works (pages) | Decision |
|---|---|---|
| Public erratum crediting the finder | 3 works, three coauthor groups with only Conn in common: D001 p. 1 (1981, Coleman), S059 pp. 1, 4 (1989, Gould and Toint), the IDFO errata B002 p. 3 / B003 p. 1 (2015, Scheinberg and Vicente; one work) | Reaches the count of three but **stays in the pool**. (i) The third work is book material, and §3 of the house rules does not promote from this material alone. (ii) The four-way validation is not done, and exclusivity is weak: errata lists that thank their finders are ordinary practice for textbooks and journals. (iii) The book case varies the pattern: statements change, not only proofs (§12.1). Kept as catalog W8 (with a variant) and as the Honest Boundary's positive model. |
| Check what you called straightforward (new) | S012 p. 3 (the CGT book's claim that second-order DFO analysis follows simply, answered as not trivial); B002 p. 2 (item 5 withdraws "It is then obvious"); B004 p. 1 beside B002 p. 3 (a full derivation of regression bounds whose constants were corrected, on a topic S028 p. 14 had called "straightforward adaptations") | **Pool only.** Two papers and one book-material work (B002 and B004 count as one); no stated side; whether the book's Theorem 4.13 is S028's statement cannot be checked without the book body. Its transferable part is catalog P21. |

### 12.3 Changes made to SKILL.md

Net growth 464 words (11177 → 11641, `wc -w`; 11571 before the review corrections of §12.6). Each line cites B ids; full evidence under the ledger anchors named in §12.1.
1. Intro paragraph: one sentence saying the book's open material was read and the body was not.
2. Domain fit: the book's first motivating example, parameter tuning, is "a nonsmooth noisy problem" while its model-based (trust-region) theory assumes a Lipschitz-continuous gradient or Hessian (reviewer D. Orban; wording corrected on review, §12.6).
3. Warning sign 7: the book's own "Limitations" section, and a reviewer's praise.
4. M1: ⚠ "Book level" bullet (theory leg; reviewers on numbers and software).
5. M3: "Stated (book organisation, 2009)" line, and ⚠ "Step 1's constants are error-prone".
6. M6: practice item "both schools in one textbook, rival methods (Powell's, wedge) beside the authors' 'DFO' approach", labelled title level and weak evidence (§12.6).
7. Signature Work 1, Reception row: one line per reviewer, by name.
8. Roundtable Card blind spots: the reviewers' two points (overlap with non-differentiable optimization "not adequately addressed"; model-based theory assumes a Lipschitz-continuous gradient or Hessian), with a ⚠ that the contents include §7.4, nonsmooth direct-search convergence. ✗ Corrected on review: the first version said both reviewers place nonsmooth problems outside the book (§12.6).
9. Honest Boundary: the six cards sit outside the coverage counts; the books-gap sentence says exactly what was read; the errata variant of the positive model.
10. Appendix: card count, the book page's read items, and the two reviews as secondary sources.

Frontmatter, Activation Rules, Research Integrity Rules, method numbering, heuristics and workflows are unchanged.

### 12.4 Rejected updates (book material)

1. **Promoting "Public erratum crediting the finder"** to a heuristic or method (§12.2).
2. **A new method from the book's architecture** ("tools before algorithms", "limitations before prescriptions", parallel chapter templates). It is M3's and M1 step 1's order in textbook form, and a textbook's order is also a teaching choice; recorded as M3's stated emphasis and as writing moves W16–W18.
3. **Rewriting M3 step 1** to require an independent derivation of the constants. One book's errata show the constants were error-prone, not that a check was part of the practice; kept as a variant bullet and catalog P21.
4. **Counting the reviews as evidence of Conn's practice**, or adding the six items to the say–do tallies. The reviews are peer readings of a joint book; the tallies stay paper counts.
5. **Nazareth's framing** of the book as "emblematic" of algorithmic science & engineering [B005 p. 3]: it rests on his own SIAM News article; not used.
6. **Raising the Roundtable's "dimension in the tens"** to "up to a hundred" [B005 p. 1]: a reviewer's sizing of the book's class, not of Conn's practice; consistent, unchanged.
7. **M7 or Taste mark 7 evidence from the errata**: no solver is involved, and the list credits readers who pointed out errors, without saying whether the authors' own checks found any; a T7 variant in the ledger only.
8. **The card's reading path in SKILL.md**: useful, but not a Conn method; it stays in `cards/k01.md`.
9. **Deleting "keeps the statement"** from W8 and from the Honest Boundary: append-only; both are qualified with the book-errata variant.
10. **A Research Trajectory "Latest" line**: there is no new edition, only errata for a second printing [B003 p. 1]; ledger `#trajectory` only.
11. **Mapping book theorems to papers beyond titles** (e.g. Theorem 4.13 = S028's regression bound; Ch. 10 = S012): cannot be checked without the book body; kept at title level on the card.
12. **A new M2 line in SKILL.md** from Orban's "not an objective of the book": it adds no instruction; ledger `#method-2` only.
13. **Correcting B006's year in INDEX.md and `works.json`**: verified (Crossref, 2011), but those files are harvest outputs; recorded in 07, RESOURCES.md and here, and flagged. *Reversed on review (§12.6)*: the digest is the card's own output, and 07 must agree with it, so the digest, INDEX.md and `works.json` now say 2011.
14. **Reviewer-derived lessons as catalog entries** ("say where the code and the numbers are" [B005 p. 3]; bare-bones implementations in the exercises [B006 p. 2]): they are critiques of the book, not devices it uses; recorded in `05-peer-critique.md` §6.

### 12.5 Open gaps after the book material

- The IDFO chapters themselves (13 chapters and the software appendix) are unread; the reading path in `k01` is built from titles.
- *Trust-Region Methods* [S001] and the LANCELOT book [S006]: no open material was read.
- B004's extracted text writes ‖M†‖ after the scaling and ν for ν2 in the residual bound; extraction loss or a slip of the original is undecided [B004 card].
- When each erratum was found, and by whom, is not stated [B002 card].

### 12.6 Corrections after review (2026-09-27)

A reviewer checked the book-material integration against the texts. Every finding was confirmed against B001–B006 and applied; nothing was promoted or removed, and each overstatement is kept visible as a ✗ or ⚠ line where it had been stated.
1. **Nonsmooth scope (major).** ✗ "Both reviewers place nonsmooth problems outside the book" overstated both reviews. The contents list §7.4 "Global convergence in the nonsmooth case" [B001 p. 2], and Nazareth reports that Ch. 7 treats global convergence "for both continuously differentiable and nonsmooth cases" [B005 p. 2]. His criticism is that the overlap with non-differentiable optimization is "not adequately addressed" [B005 p. 3]. Orban's Lipschitz sentence sits in his paragraph on the trust-region model-based chapters [B006 p. 2]. Corrected in SKILL.md (Domain fit, Roundtable blind spots), §12.1 and §12.3 here, ledger `#method-3` and `#book-material`, `05-peer-critique.md` §6, and the k01 card and digest.
2. **Title-level labels.** The M3 stated line says Part I precedes every *optimization framework* of Part II, not every algorithm (Part I holds the algorithms of §§6.3–6.4, and §1.4 runs Nelder–Mead). The M6 item says rival *methods*, not codes, and is marked weak evidence (survey genre, house rules §3.4). Warning sign 7's "Limitations" citation is marked as a section title only. B001 gains its W7 link (card, digest, 07 row).
3. **M3 constants bullet.** That errata item 11's constants are Theorem 4.13's, as derived in the addendum, is labelled an inference. The imperative "Derive the constants yourself" is removed from SKILL.md, in line with §12.4 item 3; the lesson stays in catalog P21 and the ledger, labelled as the skill's own.
4. **Reader credit.** The claim that the corrections came "not from the authors' own testing" is replaced: the list credits readers who pointed out errors; whether any came from the authors' own checking is not stated [B002 p. 3].
5. **Warning sign 7, errata item 2.** "Sharpen rather than soften" is replaced by a neutral description, consistent with the card's "overstated wording" class and catalog W19.
6. **Numbers and dates.** Software appendix book pp. 251–254, not 251–255 [B001 p. 3]. B006's year is 2011 in the digest, INDEX.md and `works.json` as well (Crossref re-checked: *SIAM Review* 53(2), pp. 375–405, print 2011-01, online 2011-05-05); this reverses §12.4 item 13.
7. **Traceability and wording.** SKILL.md's intro sentence now points to `09-evidence-ledger.md#book-material`. "Le Digabel later co-wrote" becomes "also co-wrote" (the 2013 paper predates the 2015 list).
