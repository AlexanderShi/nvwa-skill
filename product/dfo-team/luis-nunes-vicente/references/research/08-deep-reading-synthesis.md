# Deep-reading synthesis · Luís Nunes Vicente

> What this is: the aggregation of all paper cards (`07-paper-cards.md`, `cards/*.md`, `cards/*.digest.json`) into decisions for SKILL.md. It applies the conservative-update rules of `references/paper-reading-card.md` §3 and the four-way validation of `references/research-extraction-framework.md` §3 (cross-project recurrence, say–do consistency, executable steps that differ from standard practice, exclusivity). SKILL.md itself is **not** edited here; §3, §4, §5 and §10 list what should change and what should not. A three-reviewer check of the resulting SKILL.md (2026-09-27) changed some decisions; each is marked "Review outcome" where it applies (§3.1 row 7, §3.2 rows 8 and 16, §3.3, §4.1, §5, §9).
>
> Date: 2026-09-27. Counts come from a script over the 128 card entries (124 works) in the 26 digest files: one card per work; where a work was carded twice, the fuller card counts. Every statement points to card ids, e.g. [S019 p. 20]. Page numbers are those of the text versions read (mostly preprints; see §11).
>
> Reading lesson (general, not about any paper): cards occasionally record small inconsistencies between tables, captions, text and theorem parameters. Before reusing a number or a parameter from any paper, check that the table, the caption and the text agree and that the experiment's parameters satisfy the theorem being cited.

---

## 1. Coverage

| Item | Count |
|---|---|
| Rows on the Google Scholar profile | 122 (115 distinct works; 7 duplicate rows merged) |
| Distinct works (Scholar + 1 DBLP-only + 8 homepage-only) | 124 |
| Full text read, full card | 92 |
| Full text read in part | 16 (S029, S031, S032, S043, S045, S054, S056, S058, S060, S068, S077, S078, S090, S095, S098, S108) |
| Abstract-level card | 11 (S001, S004, S009, S021, S033, S052, S063, S066, S069, S100, S112) |
| Metadata-only card | 5 (H005, H006, H008, S116, S117) |
| Skipped | 0 distinct works |
| Card entries / batch files | 128 entries in 26 batch files (S108, S113, S121, S122 carded twice) |

Read levels by period (all 124 works):

| Period | full | partial | abstract | metadata | total |
|---|---|---|---|---|---|
| 1991–1995 | 4 | 0 | 7 | 1 | 12 |
| 1996–2000 | 12 | 1 | 1 | 2 | 16 |
| 2001–2005 | 9 | 4 | 0 | 0 | 13 |
| 2006–2010 | 14 | 1 | 2 | 0 | 17 |
| 2011–2015 | 18 | 2 | 0 | 2 | 22 |
| 2016–2020 | 10 | 7 | 0 | 0 | 17 |
| 2021–2026 | 24 | 1 | 1 | 0 | 26 |
| undated (S120) | 1 | 0 | 0 | 0 | 1 |

Attribution rules used in all counts:
- S029 is a joint paper with Bandeira and Scheinberg (also on Scheinberg's list); it counts as Vicente evidence as a coauthor [S029].
- S056 (223-page COCONUT report): only §2.1 (PDF pp. 7–9) is Vicente's. Its Method 1 and Method 5 links, which rest on Neumaier's and others' chapters, are excluded [S056 pp. 67–72, 44–46]. Only the §2.1 links (Method 3 scope marker p. 7, Method 4 p. 8, Taste mark 1 p. 8) are counted.
- S121/S122: only the signed Chair's Columns are his; they are service writing and give no method evidence [S122 pp. 23–24; S121 p. 14].
- S113 is a talk deck presented by his student Suyun Liu (footer on every content slide) [S113 pp. 3–46]; it counts as taught-view evidence only.
- S040 is his 1996 PhD thesis (derivative-based) [S040].
- S092's "not applicable" link to Methods 1–4 is dropped (no algorithm) [S092].

How counts were made: a card "gives evidence / variant / contradiction" for Method N if its method-link entry says so; a card is counted once per relation. New-pattern candidates were clustered by reading the pattern and its evidence, not by string match. Where the card text (D1–D8) supports a cluster member that the card did not list as a candidate, the member was added with the page it rests on (marked "text:" in the script output). Candidate entries that the reader marked as not disclosed by the authors were not counted as disclosures.

---

## 2. Evidence per existing method

### 2.1 Counts

| Method | Evidence | Variant | Contradiction | Distinct cards (any relation) | Say–do after full reading |
|---|---|---|---|---|---|
| M1 Heuristic inside a convergent skeleton | 22 | 33 | 1 | 48 (46 full/partial) | ✅ stated + practiced; stated side now verbatim |
| M2 Count evaluations against the gradient benchmark | 17 | 24 | 5 | 44 (43 full/partial) | ✅ stated + practiced; unit narrows in the 2023–26 papers |
| M3 Relax deterministic requirements to probabilistic ones | 15 | 17 | 3 | 31 (all full/partial) | ✅ stated + practiced; scope = DFO line |
| M4 Generalize the acceptance test, not the algorithm | 46 | 25 | 0 | 68 (all full/partial) | ✅ stated + practiced; the changed object is often not the acceptance test |
| M5 Ship the solver, profile it on a collection | 33 | 55 | 8 | 92 (87 full/partial) | ✅ stated + practiced; genre-dependent |

(A card can carry both an evidence and a variant link for the same method, e.g. S005 for M1 [S005 pp. 6, 8–11].)

### 2.2 Method 1 — Heuristic inside a convergent skeleton

- Strongest practice: particle swarm in the search step, "It is the poll step that guarantees the global convergence" [S005 pp. 6, 8–10]; ES kept intact with a separate step size, sufficient decrease and the reset σ_{k+1} = max{σ_k, σ^ES_k}, plus the raw-ES ablation [S050 pp. 4–6, 11, 14–18]; ES directions stay above 90% of those selected under constraints [S057 pp. 2, 4, 10, 12]; FD-BFGS steps "essentially considered as search steps" of direct search [S073 p. 10], constrained sequel [S088 pp. 5–7, 11–13]; MFN models in the optional search step, where optionality licenses loose geometry [S012 pp. 6–8]; model step in the search of a trust-region method glued by sufficient decrease [S071 pp. 2–4, 9–11].
- Earliest instances: user/physics proposals in the search step, 2001 and 2004 [S106 pp. 1–3; S025 pp. 5–6, 9–10]; a 1994 abstract already pairs a fast unguaranteed step with a guaranteed method in a hybrid [S004 abstract].
- Downstream use of the Method-1 product PSwarm in applications [S075 p. 3; S082 p. 3; S036 pp. 7, 9].
- Stated (author voice, full text): "these strategies (i) require no extra function evaluation and (ii) do not interfere with existing requirements for global convergence" [S008 p. 2]; "how to change Algorithm 2.1, in a minimal way, so that it enjoys some form of convergence properties, while preserving as much as possible the original design and goals" [S050 p. 4]; "The search step is optional and does not interfere in the global convergence properties" [S038 p. 13].
- Say–do update: ✅ holds. The stated side no longer rests on a software page and an abstract paraphrase; it rests on three verbatim sentences [S008 p. 2; S050 p. 4; S038 p. 13]. Variants: §3.3.

### 2.3 Method 2 — Count evaluations against the gradient benchmark

- Strongest practice: the origin, two-counter proof, n² = cm⁻² × poll size, comparison with steepest descent [S023 pp. 5–8]; every step including the convex yardstick and numerics against the randomized rival [S046 pp. 1–23]; n-order question [S041 pp. 2, 4–8]; O(mnε⁻²) next to O(n²ε⁻²) [S019 pp. 12, 16, 22]; price of smoothing named [S034 pp. 5–6, 9–11]; probabilistic trust-region rates with n-dependence [S027 pp. 3, 11, 16]; trust-region counterpart [S032 pp. 3, 11, 15, 20]; second-order direct search [S074 pp. 14–18]; decoupled steps [S060 pp. 2–5, 13, 22]; multiobjective gradient descent matching single-objective rates [S015 pp. 2, 9]; stochastic alternating algorithm [S093 pp. 3, 11, 14, 16–17]; non-monotone direct search matched to monotone DS [S110 pp. 4, 9–10, 13–14, 18].
- Stated: "Such an analysis of worst case complexity contributes to a better understanding of the numerical performance" [S023 p. 2]; "In DFO it becomes also important to measure the effort in terms of the number of function evaluations" [S038 p. 8]; "κ can be interpreted as the price to pay for the absence of gradient information" [S041 p. 4].
- Say–do update: ✅ holds for the 2013–2019 DFO complexity line. In several 2023–2026 papers the unit is iterations (or outer iterations) and total sample or oracle work is left open [S073 pp. 8–9; S088 p. 11; S017 p. 17; S042 pp. 20–21; S091 p. 6; S102 p. 16; S110 p. 14; S111 pp. 6–11]. Variants: §3.3.

### 2.4 Method 3 — Relax deterministic requirements to probabilistic ones

- Strongest practice: all six steps visible, threshold p₀(θ, γ) and the rule for the number of random directions [S019 pp. 5–20]; threshold from the radius factors and rates with overwhelming probability for trust regions [S027 pp. 5, 8–11]; the origin with the model as the random object [S014 pp. 2, 7, 10–13]; constrained version with a direction count r_s [S045 pp. 12–16]; Levenberg–Marquardt with probabilistic gradients and a deterministic-vs-probabilistic run [S043 pp. 5, 9–13, 23–25]; tail bound on the estimated decrease [S067 pp. 5–8, 11]; sequential test on the accept/reject decision [S102 pp. 6, 11, 18]; max-M acceptance with probabilistic descent [S110 pp. 10, 13, 15, 18–19].
- Precursor and origin evidence: random sampling gives fully quadratic models with high probability [S029 pp. 5–6, 22]; numerics polling with n/2 random directions [S049 pp. 14–15, 17]; the optimality result used to argue for randomization [S041 p. 8]; probabilistic direct search as the engine of later methods [S073 p. 13; S078 p. 24].
- Stated: "as long as 'good' models are more likely than 'bad' models" [S014 p. 1]; conditioning on the past "is more reasonable than assuming complete independence" [S014 p. 7]; "The proof technique separates the counting … from the probabilistic properties" [S019 p. 22]; the condition "focuses on the reduction estimate" [S067 p. 3].
- Say–do update: ✅ holds for the DFO line. It does not hold as a contrast with stochastic approximation for the bilevel/trilevel SG papers [S042 pp. 13–14, 18, 21; S091 pp. 5–6]. Variants: §3.3.

### 2.5 Method 4 — Generalize the acceptance test, not the algorithm

- Strongest practice: dominance list, success = list changed, proofs carried over, class-native metrics [S003 pp. 2, 4–5, 13, 17–18, 30–31]; merit-function success with the skeleton unchanged [S049 pp. 1, 3–6]; componentwise sufficient decrease for multiobjective gradient descent, price stated in the abstract [S015 pp. 1, 3–4]; max-M acceptance with poll and step logic fixed, price stated [S110 pp. 4, 6, 10, 14]; one acceptance-test change carried through direct search and trust region [S067 pp. 10–18]; only the acceptance quantity redefined and "Only a very few steps in the convergence analysis change" [S013 pp. 9–14]; smoothing with one new rule [S034 p. 7]; acceptance test replaced by a sequential test [S102 p. 11].
- Pre-DFO and outside-DFO instances: [S037 pp. 5–7; S039 pp. 4, 6–7; S084 pp. 2, 5, 10; S007 pp. 1–4, 10; S077 pp. 2, 14–15, 18–21; S085 pp. 2, 4, 9–10; S090 pp. 4–6; S051 p. 3; S087 pp. 3–7; S047 pp. 3, 12–14; S042 pp. 7–8, 18; S091 pp. 3, 14–16].
- Stated: DMS "does not aggregate any of the objective functions" [S003 p. 1]; "The merit function and the corresponding penalty parameter are only used in the evaluation of an already computed step" [S049 p. 3]; the 2001 overview already writes NLP methods as separable components and presents the filter as a multicriteria acceptance rule [S056 pp. 7–9].
- Say–do update: ✅ holds, with 0 contradictions. The wording is too narrow; see §3.3.

### 2.6 Method 5 — Ship the solver, profile it on a collection

- Strongest practice: solver + public 122-problem collection + profiles + default-setting baselines + hybrid vs components ablation [S005 pp. 14–18, 26–27]; public MOO collection, class-native metrics, MOO profiles, best 3 of 8 solvers [S003 pp. 15–20, 24]; four Moré–Wild classes, strongest model-based baseline, losses reported, code released [S012 pp. 9–10, 15]; the released SID-PSM artefact with every strategy a switchable option [S059 pp. 1–2, 9–15, 20–22]; released code, 40 datasets, class-native metrics [S016 pp. 5–7]; collections in three regimes, components as baselines, GitHub code [S088 pp. 14–24]; negative-result paper with public code [S079 pp. 3, 5, 21]; profiles with unsafeguarded CMA-ES and losses [S050 pp. 12–18; S057 pp. 11–18].
- Artefact habit before DFO: generator code as a citable TOMS paper [D001 pp. 1–4]; generators offered as the common testbed [S002 p. 6; S053 p. 14]; TRICE solver with user's guide and GUI [H007 p. 3]; the interface itself published [S048 pp. 1–4].
- Stated: "Care must be exercised in the testing and benchmarking of algorithms and in the interpretation and dissemination of the corresponding results" [S053 p. 14, 1993]; mastery of scientific-computing tools as part of industrial-mathematics training [S109 p. 5, 2006]; a survey that pairs every method class with released software [S038 pp. 4–13, 15].
- Say–do update: ✅, and stronger than SKILL.md's "single quote" [S053 p. 14; S109 p. 5; S038 pp. 4–13]. Genre-dependent, see §3.3–3.4.

### 2.7 Heuristics, taste marks, workflows (links in the cards)

| Item | Evidence | Variant | Contradiction |
|---|---|---|---|
| H2 numerics before theory | S038 (pp. 3–4, 8); also S049→S019 [S049 p. 17; S019 p. 2], S014 pp. 5, 23–24 | — | — |
| H3 control the estimated decrease | S102 (pp. 5, 10); S067 pp. 5–8; S110 pp. 14–15 | — | — |
| H4 nondominated list, no aggregation | S003, S065, S094, S101, S113 (+ S016 pp. 2, 4, 13; S017 pp. 2–3, 18) | S070 | S080, S093, S111 |
| H5 smoothing | — (S034 p. 7 is its source) | S107 | — |
| H7 reuse paid-for evaluations | S008, S012, S030, S047, S059, S064, S089, S104 | S106 | — |
| H8 formalize an informal notion | S092, S096, S109 (stated background) | S094, S101 | — |
| H9 is the n-order optimal? | — (its source S041 is a Method 2 card; wording overstated, §3.1 row 4) | S091 | — |
| H10 break your own theorem | H001 (weak), S083 | S024 | — |
| T1 rigorous and efficient | S056 (§2.1 p. 8), S091 (p. 2) | — | — |
| T3 minimal modification | S037, S044, S054, S093, S095, S097 | — | — |
| T4 theory explains numerics | S030, S076 (+ S108 p. 98; S019 pp. 20–21) | — | — |
| T5 usable artefact | S086 | — | — |
| T6 anchored in an application | 17 cards: H001, S028, S031, S035, S036, S039, S043, S044, S054, S061, S062, S068, S080, S082, S095, S106, S109 | S086, S120 | — |
| W5 no collection / profiles | S053 (stated, p. 14) | — | — |
| Workflow A | S038 (p. 2) | — | — |
| Workflow E | S094, S111, S113 | S070 | — |

---

## 3. Variants and contradictions

### 3.1 Corrections flagged before synthesis — verified against the cards

| # | Claim in SKILL.md | Verdict | Cards | What changes |
|---|---|---|---|---|
| 1 | Method 1: "sufficient decrease (not a mesh) is the glue" | **Confirmed wrong for 2001–2012** | Integer-lattice mesh + simple decrease: [S106 pp. 1–3; S025 pp. 4–6, 9; S005 pp. 10–11; S008 pp. 3–4 (sufficient decrease only for mesh expansion, p. 14); S059 pp. 6–7; S018 pp. 5, 7, 10 (declines sufficient decrease); S012 p. 6; S064 pp. 7–8]. Both globalizations unified in one proof: [S003 pp. 4, 28–31 (numerics use ρ̄ = 0, p. 20); S024 p. 6]. Certified model + criticality step in DFO trust regions: [S006 pp. 2, 14]. Sufficient decrease as the chosen glue: [S023 p. 4; S049 p. 2; S071 pp. 3–4; S050 pp. 4–6; S057 p. 8; S038 pp. 5–6; S073 pp. 5, 10; S088 p. 6] | Date the claim: "mesh + simple decrease in 2001–2012 (SID-PSM, PSwarm, DMS numerics); both unified 2011–2012; sufficient decrease is the glue from 2013 on". Keep the "sufficient decrease frees point generation" rationale [S049 p. 2; S038 pp. 5–6] |
| 2 | DMS test set "69 bi-, 29 tri-, 2 four-objective" | **Confirmed wrong** | [S003 p. 16, Table 5.1] | 69 bi-, 30 tri-, 1 four-objective (FES3) |
| 3 | Probabilistic trust-region rates | **Confirmed** attribution | S014 proves almost-sure convergence only, with Conjecture 5.1 for second-order lim [S014 pp. 8–13, 20–21]; rates sketched in [S019 pp. 21–22] and proved in [S027 pp. 5, 8–11] | SKILL.md's Method 2 and Method 3 practice lines already cite IMA J. Numer. Anal. 2018 for rates; keep that and never cite S014 for rates |
| 4 | "optimal n² factor" (Taste 2; Method 2 practice and limitations; Heuristic 9) | **Confirmed overstated** | Optimality is over the choice of positive spanning set inside the sufficient-decrease upper-bound template; not an oracle lower bound; "no other positive spanning set will yield a better order of n" [S041 pp. 1, 5, 8]; survey wording "approximately optimal" [S038 p. 8] | Reword in all four places; delete "intrinsic to the deterministic class" |
| 5 | "the Lehigh papers ship GitHub code (MOO_Fairness, BSG_Methods_Con_Unc, snee)" | **Partly supported** | Of 22 full-text papers from 2021–2026 with experiments, 8 state public code: [S016 p. 5 (MOO_Fairness); S042 p. 22 (BSG_Methods_Con_Unc); S065 p. 8; S070 p. 13; S088 p. 14; S091 p. 7; S092 p. 3; S079 p. 3]; code by e-mail [S078 p. 22]; no code statement in the other 13 texts, including [S096 p. 6] (no "snee" link in v3; repository not checked) | "Several Lehigh papers release code on GitHub (e.g. MOO_Fairness, BSG_Methods_Con_Unc)"; drop "snee" unless the repository is verified |
| 6 | Non-monotone direct search listed under Method 1 | **Confirmed misplaced** | No search step, no heuristic; only the acceptance test changes [S110 pp. 4, 6, 10, 14] | Move to Method 4 practice |
| 7 | First-pass attribution: random polling "leads to better complexity bounds as well as to gains in numerical efficiency" (GRVZ 2015 abstract) | **Misattributed** (Review outcome) | The sentence is verbatim from the abstract of the 2019 constrained sequel by the same four authors [S045 p. 1]. The 2015 preprint abstract says "recent numerical results" favoured random polling and calls its rate "matching" the deterministic one; the gain is in evaluations, O(mnε⁻²) vs O(n²ε⁻²), when m ≪ n [S019 pp. 1, 16, 22] | Quote the sentence verbatim with [S045 p. 1] as stated evidence for Method 3; keep S019's own wording with [S019 p. 1] |

### 3.2 Further corrections found in the cards

| # | SKILL.md item | Finding | Cards |
|---|---|---|---|
| 8 | Signature Work Anatomy, SID-PSM row ("use them … to build search-step models"; SID-PSM as the SIAM J. Optim. 2007 paper) | The 2007 paper defers the model search step to "separate research" and does not name SID-PSM; the MFN search step appears in the 2010 COAP paper and in the later v1.3 manual; the manual text read cites COAP 46 (2010) and the 2009 book, so it postdates the listed 2008, and when the name SID-PSM first appeared is not established (Review outcome); "Dec 2014" comes from the software page; glue is the rational-lattice mesh with simple decrease | [S008 pp. 3–4, 13; S012 pp. 6–8; S059 pp. 1–7] |
| 9 | Method 2 stated: "recovering classical convergence rates" dated to 2026 | Earlier instances in 2019 and 2023 | [S015 pp. 2, 9; S093 p. 3; S111 p. 1] |
| 10 | Method 3 "Different from standard practice" (vs stochastic approximation) | Holds for the DFO line only; the bilevel/trilevel SG papers use unbiased oracles, Robbins–Monro steps and bounds in expectation | [S042 pp. 13–14, 18, 21; S091 pp. 5–6]; expectation-type step-tied accuracy in [S017 pp. 11, 17] |
| 11 | Anti-pattern "Using 1 random direction" and Method 3 step 5 | The threshold is joint in the direction-success probability and the step-size factors: one direction per iteration has a complexity guarantee when 3 log γ + 11 log θ > 0; m = 2 suffices for γ = 2, θ = 1/2 | [S102 pp. 11, 14, 16–17; S019 p. 20; S110 pp. 13, 18]. In S067 the threshold is on the acceptance constant θ, and the experiments run below it with the gap disclosed and a conjecture [S067 p. 20] |
| 12 | Workflow D | Add: a known upper bound on ε_q; the θ threshold (3.1); the common-random-numbers route O(Δ^{−ε}); the O(δ^{−2q}) paraphrase holds for q ∈ (1, 2] with i.i.d. averaging | [S067 pp. 5–8, 11] |
| 13 | Research Trajectory | Missing 1991–1996 period (bilevel, complementarity, test-problem generators, Coimbra/Waterloo/GERAD); direct search starts 2001, not 1996; derivative-based NLP continues to 2008 | §8 |
| 14 | Honest Boundary: "Web-search snippets only … No full text … was read" | Obsolete: 108 of 124 works were read in full text | §1 |
| 15 | Honest Boundary: "Method 5's stated evidence is a single quote" | Now three more stated sources | [S053 p. 14; S109 p. 5; S038 pp. 4–13] |
| 16 | Heuristic 10 labelled "lesson from critique, not a rule Vicente stated" | Partly practiced (Review outcome): hypothesis-breaking and rejected-alternative examples appear in his papers; the S083 example was supplied by Audet and printed with the scope narrowed. The clause "aim a second example at the proof steps" has no practiced case: it stays a labelled lesson from the 2024 external critique. The 2012 suite was built one test function per hypothesis | [S083 p. 3; S024 pp. 17–23; S007 pp. 25–26; S108 pp. 77–84] |
| 17 | Mentor Voice register "formal and precise" | Holds for papers; the signed service columns are warm, exclamatory, first-name | [S122 p. 23; S121 p. 14] |
| 18 | Latest · Service | SIAG/OPT chair 2023–2025 and newsletter editor 2003–2008 confirmed from signed columns | [S122 pp. 23–24; S121 p. 14] |
| 19 | Inner Tension "DFO core vs ML pivot" | One signed field-level sentence ranks "scalable stochastic methods" first; no personal explanation; the Lehigh output also reaches empirical sports analytics | [S121 p. 14; S086; S092; S120] |
| 20 | Inner Tension "worst case vs typical" | A method with the worse bound performs much better, reported openly | [S032 p. 22] |

### 3.3 Method-level variant notes

**Method 1**
- Glue dating: see §3.1 row 1.
- Step 2 variant: in the ES papers the ES loop itself is the poll-like mechanism; the search step is future work [S050 pp. 6, 19].
- Step 4 variant: the coupling can be a switch rather than a reset. A fast step is accepted only while β ≥ γρ(α); otherwise the method switches to direct search [S073 pp. 5–6; S088 p. 6]. A complexity-derived ratio can trigger the switch [S104 pp. 4–5].
- Reversed structure: a heuristic outer loop (perturb, run SMG, filter dominated points) around an inner method with per-point guarantees; no guarantee for the whole front [S016 p. 13; S017 pp. 17–19; S078 pp. 5–7].
- Failure mode: inserting a learned surrogate gradient into the FLE skeleton does not beat the unwrapped solver across the collection; a surrogate does not help where the component it replaces (forward differences) is already accurate [S079 pp. 20–23].
- Derivative-based precursors (Newton or a structured step inside a trust-region, filter or merit skeleton): [S040 pp. 103–107; S081 pp. 4–6; S011 pp. 16–17, 36–39; S039 p. 4; S062 pp. 5–6; S044 pp. 6–7; S007 pp. 4, 11–12].
- Contradiction (disclosed): a heuristic variant shipped as "not grounded on theoretical principles", compared openly with DARTS, which has the same status [S042 p. 5].

**Method 2**
- Era: no worst-case evaluation counts before 2013; finished results were lim-inf, second-order or local-rate statements (an empirical growth exponent in n is the closest, [S025 p. 13]) [S040 pp. 114, 125–126; S031 pp. 15, 20–21; S011 pp. 39–40; S013 p. 12; S006 p. 3].
- Wording of step 5 and Heuristic 9: §3.1 row 4.
- Yardstick moves in the later papers to the nearest classical method: SCGD [S107 pp. 10, 16], monotone direct search [S110 pp. 4, 13], the best nonconvex bilevel rate [S091 p. 6], SGD/BCD [S111 pp. 7–9].
- Unit: iterations rather than evaluations or samples in several 2023–2026 papers (§2.3).
- Complexity inequalities used as run-time diagnostics [S104 pp. 2, 4].

**Method 3**
- Deterministic ancestor, 1996–2013: exactness relaxed to accuracy tied to the step size, radius or predicted decrease, checked with quantities available at the iteration — 15 cards: [S040 p. 136; H007 pp. 2–3; S048 p. 11; S013 pp. 8, 10, 16; S084 pp. 6, 10–11; S077 p. 6; S085 pp. 4–5; S006 p. 3; S047 pp. 8–9, 14; S097 p. 8; S108 pp. 72–84; S073 pp. 12–13; S088 pp. 13–14; S017 pp. 11, 17; S042 pp. 13–15]. Also "weakest condition the proof touches" — 8 cards: [S031 p. 4; S054 pp. 4–5; S077 pp. 6, 8; S085 pp. 10, 15; S083 pp. 2–3, 6; S045 p. 8; S019 p. 5; S013 pp. 7–8].
- Step 2 refinement: before randomizing, find the one instance of a uniform requirement that the proof uses (cm(D, −g) instead of the cosine measure over all vectors) [S019 p. 5], and restate the deterministic proof with that property [S045 p. 8].
- Step 4 variant: the guarantee can be a bound on the expected iteration count via renewal–reward rather than almost-sure convergence plus a high-probability bound [S102 p. 16; S110 p. 13].
- Step 5 variant: §3.2 row 11.
- Scope: §3.2 row 10.

**Method 4**
- The changed object: across the 68 cards, the acceptance test (or success notion) is the most frequent single object, in about a third of them — DFO [S003; S049; S058 p. 3; S032 pp. 5–6; S067; S102; S110; S071 pp. 3–4; S057 p. 3; S083 pp. 4–5; S006 pp. 14–15] and derivative-based [S013; S039; S007; S077 pp. 14–15; S015; S113 pp. 28, 32]. Elsewhere the object is the stationarity measure [S024 pp. 4, 6, 11; S023 p. 9; S045 pp. 7–11; S040 p. 103], the model class [S006 pp. 7–9; S020 pp. 8–9, 22], the step or direction map [S011 pp. 14–15; S017 p. 8; S042 pp. 7–8; S108 p. 19; S084 p. 2; S044 pp. 3–5], the objective or problem data [S034 p. 7; S107 p. 7; S101 p. 9; S070 pp. 4–5; S080 pp. 4, 17; S051 p. 3; S087 pp. 3–7; S090 pp. 4–6], or the update schedule [S111 pp. 4–5; S043 pp. 5–6]. Suggested wording: "keep the skeleton, change one object — most often the acceptance test". Review outcome: not adopted; the one-line keeps its original wording (conservative update, rule 2), and the breadth is recorded as a Method 4 variant.
- Two recurring sub-steps (§4.2): prove one bridge inequality that puts the new step into the classical theorem's form [S037 pp. 6–7; S039 pp. 6–7; S046 pp. 7–9; S081 pp. 4–5], and check that the new theory collapses to the old one when the new object is trivial [S003 p. 14; S013 pp. 1–2; S011 p. 2; S111 p. 5]. Review outcome: recorded in SKILL.md as standard sub-steps under Variants, not as numbered steps (they failed exclusivity in §4.2).
- Problem-level variant: reformulate the problem so that an existing solver applies, instead of changing an algorithm [S022 p. 12; S036 p. 6; S061 p. 14; S080 p. 4; S101 p. 9; S096 pp. 8–9].
- Step 5 (price in the abstract): done in [S015 p. 1; S017 p. 1; S107 p. 1; S089 p. 1; S096 p. 1]; stated in the text rather than the abstract in [S110 p. 14]; not stated in [S049 p. 1].
- Limitation: the discontinuous extension assumes lim f(x_k) = f(x*) along the refining subsequence and density in every subsequence, and rebuilds the constrained calculus in an appendix [S024 pp. 11, 15, 23–29]; whether the 2024 counterexample targets these steps was not checked (the counterexample paper was not read).

**Method 5**
- Genre: the full protocol (collection, profiles, strongest baseline, component ablation, code) appears in algorithm papers [S005; S012; S003; S050; S057; S064; S097; S016; S073; S088; S079]. Theory-first papers have no numerics or only illustrations [S006; S010 p. 24; S014 pp. 5–6, 23–26; S015; S020 p. 3; S023; S027; S041]. Application papers use the group's solver without a benchmark [S036 pp. 9–11; S061 pp. 8–14; S068 pp. 16–18; S075; S082 pp. 4–5]. Early short papers report numerics without tables [H003 p. 2; S098 p. 8].
- Profiles appear from 2007 [S005 pp. 16–17]; before that, per-problem tables [S037 pp. 8–10; S039 pp. 16–24; S008 pp. 13–17].
- Step 1/4 refinements: mechanism-isolating control variants and fairness handicaps (§7.3, 20 cards). Review outcome: recorded as variants (standard practice), not added to the steps.
- Code claim: §3.1 row 5.

### 3.4 Contradictions (all 21 contradiction links: 17 at method level, 3 for Heuristic 4, 1 for the DMS anatomy row)

| Target | Cards | Nature |
|---|---|---|
| M1 | S042 [p. 5] | a disclosed heuristic variant without safeguard, shipped beside the theory-covered one |
| M2 | S006 [p. 3]; S058 [p. 25]; S065; S070 [p. 5]; S078 [p. 19] | era (2009), a class where the authors doubt a rate exists with dense directions, and application or formulation papers without rates |
| M3 | S067 [p. 20]; S042 [pp. 13–14, 18, 21]; S091 [pp. 5–6] | tested parameter below the proven acceptance threshold, disclosed with a conjecture; stochastic-approximation modelling in the SG papers |
| M5 | H003 [p. 2]; S098 [p. 8]; S007 [p. 26]; S006; S010 [p. 24]; S020 [p. 3]; S027; S094 [pp. 5–6] | genre: theory-first, early short papers, one-dataset preprint |
| H4 | S080 [pp. 18, 21–22]; S093 [pp. 3–4, 15–16]; S111 [pp. 2, 4, 8, 11] | the ML/OR-facing multiobjective papers scalarize (normalized weights; effort weights; step frequencies) and trace fronts by sweeping |
| Signature Work Anatomy (DMS) | S003 [p. 16] | problem counts, §3.1 row 2 |

What changes: Heuristic 4 is scoped (§5); Method 3's contrast clause is scoped (§3.2 row 10); Method 5 is labelled genre-dependent; Method 2 keeps its claim for the DFO complexity line and records the unit and yardstick variants. No existing method is refuted: every contradiction is scoped to a period, a genre or a line of work.

---

## 4. Promotion candidates (none promoted after review)

### 4.1 Candidate Method 6: Publish the Boundary, Then Attack It (proposed; demoted to heuristic H10 on review)

**Review outcome (2026-09-27).** Checks 2 and 4 below do not hold at core-method grade. (2) The "stated" sentences are the practice instances themselves; the only general sentence [S053 p. 14] is about benchmarking and already backs Method 5. (4) In the same team, Powell Method 5 (report what failed and what is not guaranteed), Audet Method 3 (counterexamples bound the guarantee, applied to one's own results) and Conn Method 7 (named weaknesses become the next agenda) cover most facets, so the name test fails. The facet counts come from manual clustering, and the card template asks every card whether failures are reported and how limits are written (D5, D8), which inflates recurrence. Steps 2 and 5 duplicate Method 5 refinements or common practice. Decision: not a core method; SKILL.md keeps 5 methods. The distinctive facets (a proof boundary localized to an inequality or a removed freedom; labelled code-vs-theory departures; printed hypothesis-breaking examples) are merged into heuristic H10, and Taste mark 7, Warning signs 7–8, Workflow C step 7 and Workflow F step 4 keep the practice. The text below is the proposal as first written.

**One line**: every result ships with its boundary written into the paper — where the method loses (against the strongest baseline, rerun if the first comparison favoured the new method), the exact inequality or case where the proof stops, and every place the code departs from the analysed algorithm — and the named boundary becomes the next paper's entry point.

This merges four candidate clusters, which recur in the same papers (e.g. S014, S023, S050, S098, S108, S110 carry two or more facets):

| Facet (cluster) | Full/partial cards | Span | Card ids |
|---|---|---|---|
| Where the method loses ("state where you lose", own failed designs, omitted experiments, negative-result papers) | 42 (+1 abstract) | 1998–2026 | H002 H003 S003 S005 S007 S012 S013 S014 S015 S016 S017 S019 S022 S023 S024 S025 S030 S038 S039 S042 S044 S045 S048 S050 S057 S061 S068 S073 S076 S077 S079 S085 S088 S089 S091 S095 S098 S104 S108 S110 S111 S120 (abstract: S100) |
| Where the proof breaks | 20 | 1999–2026 | S014 S015 S016 S022 S023 S024 S027 S041 S046 S049 S050 S054 S060 S067 S074 S091 S098 S099 S108 S110 |
| Where the code departs from the theory (disclosed) | 16 | 1999–2026 | S003 S005 S008 S012 S018 S029 S042 S048 S050 S059 S067 S073 S076 S090 S093 S110 |
| The boundary becomes the next entry point | 12 | 2002–2025 | S013 S019 S027 S041 S044 S049 S060 S062 S074 S095 S098 S102 |
| **Union** | **59** (+1 abstract) | 1998–2026 | |

**Four checks**

1. *Cross-project recurrence* — ✅. 59 full/partial cards from 1998 [H003 pp. 4, 18–19] to 2026 [S110 p. 14; S111 p. 13], in every topic line: derivative-based NLP [S098 p. 8; S054 p. 14], direct search [S005 p. 18; S050 pp. 15–18], model-based DFO [S012 pp. 2, 10; S029 p. 21], complexity [S023 p. 9; S015 p. 9], probabilistic DFO [S014 pp. 20–21, 26; S019 p. 20; S067 p. 20], multiobjective [S016 p. 6; S111 p. 13], bilevel SG [S042 pp. 28, 32, 36].
2. *Say–do consistency* — proposed ✅; ⚠ after review (instance-level only; author voice inside the papers, as for Methods 1–4; no stand-alone methodology essay). Said: "Care must be exercised in the testing and benchmarking of algorithms and in the interpretation and dissemination of the corresponding results" [S053 p. 14]; "In this sense, the experiment in Subsection 2.2 is biased in favor of direct search based on probabilistic descent" [S019 p. 20]; "The problem in extending this result to more than two local steps or branches lies on the fact that …" [S024 p. 23]; "The geometric factor is a consequence of the particular feasible correction coefficients used here, not a lower bound for every max-M method; hence, the possibility of sharper coefficients is open" [S110 p. 14]; failed variants "we decided to omit" [S079 p. 23]. Done in the same papers: the biased experiment is rerun with baselines at their best [S019 pp. 20–21]; the theorem is stated for two pieces only [S024 p. 17]; the M factor is left as an open question [S110 p. 14]; omitted variants are listed [S079 p. 23].
3. *Executable, and different from standard practice* — ✅. The steps below produce concrete text and tables. The usual alternative is a generic limitations paragraph and unpublished failed proof attempts; here the boundary is localized to a problem class [S073 pp. 17–22], a single inequality [S014 pp. 20–21; S098 p. 8; S074 pp. 17–18], a removed algorithmic freedom [S049 p. 12] or a line of code [S005 p. 15; S018 pp. 7, 10–11].
4. *Exclusivity* — proposed ✅ on the specific form; contested after review (see above) (not on "report limitations" in general): publishing a conjecture together with the inequality that fails [S014 pp. 20–21], a whole negative-result paper about a tool plugged into one's own solver [S079 pp. 1, 3, 21, 23], a self-audit of a motivating experiment [S019 p. 20], and taking up one's own disclosed cost caveat as the next entry point [S067 p. 20 → S102 p. 3].

**Steps**

1. *Losses*: in the introduction and the results, name the classes, budgets and accuracies where the strongest baseline wins [S012 pp. 2, 10; S050 pp. 15–18; S073 pp. 17–22; S088 pp. 22–24; S016 p. 6; S003 pp. 23–25].
2. *Bias audit*: after the theory, check whether the motivating experiment used settings that favour the new method; rerun with baselines at their best and report the smaller gain [S019 p. 20]; give rivals the oracle constants their theory needs and say so [S046 pp. 21–22].
3. *Proof boundary*: when a proof does not extend, publish the exact failing inequality or case (conjecture or remark) and the algorithmic freedom that had to be removed [S014 pp. 20–21; S049 p. 12; S027 pp. 6, 15; S024 p. 23; S015 p. 9; S098 p. 8; S099 pp. 3–4].
4. *Code boundary*: label every place where the implementation departs from the analysed algorithm, with the reason [S005 p. 15; S018 pp. 7, 10–11; S050 p. 11; S012 p. 8; S003 p. 20; S067 pp. 20–21; S110 pp. 10, 20]; separate "for the theory" from "in practice" already in the abstract [S073 p. 1].
5. *Priority*: credit prior or concurrent results in the introduction and scale the novelty claim [S015 p. 2; S038 p. 12; S023 p. 9; S110 p. 3].
6. *Next entry*: turn the named boundary into the next question — random directions announced [S049 p. 17] → probabilistic descent [S019 p. 2]; an exponent gap traced to one decrease formula [S074 pp. 17–18] → decoupled steps [S060 pp. 3, 5]; per-iteration savings vs total cost, disclosed in [S067 p. 20, Remark 5.1] and taken up in [S102 p. 3]; the kinks of one space-mapping definition [S062 pp. 11–13] → the regularized one [S044 pp. 3–5]; the "road map" of [S019 §6] → [S027 p. 3]; an optimal-order result used as the argument for randomization [S041 p. 8].

**Limitations**: the facets are fullest in the DFO algorithm papers; application and ML-venue papers carry fewer of them (count by genre, not a judgement on any paper). A published boundary is not a lower bound [S110 p. 14]. Publishing one's boundary does not replace adversarial checking by others (the 2012 discontinuous result was later counterexampled, per SKILL.md; see Heuristic 10 in §5).

**Method count** (as proposed): 5 → 6. After review: stays 5 (see Review outcome). The four facets are merged into one method rather than promoted separately, to keep the skill lean and because they share one move (localize the boundary and publish it).

### 4.2 Considered and not promoted

| Cluster | Full/partial cards | 1 recurrence | 2 say–do | 3 executable & differs | 4 exclusive | Decision |
|---|---|---|---|---|---|---|
| Negative example for the rejected alternative / assumption-boundary suites | 18 (S002 S011 S020 S022 S024 S040 S044 S046 S055 S062 S074 S081 S083 S092 S096 S108 S110 S113) | ✅ 1994–2026 | ✅ author voice [S020 p. 20] | ✅ | ✗ counterexamples are standard mathematical practice | Heuristic (rewrites H10), §5 |
| One theorem, many instances (nest known theories; abstract assumptions verified per instance) | 21 (+S052 abstract) | ✅ 1996–2026 | ✅ [S011 p. 2 quote] | ✅ | ✗ common among framework theorists | Method 4 variant (standard sub-step: collapse check) |
| Bridge inequality / proof porting | 18 | ✅ 1996–2026 | ✅ [S013 p. 12; S027 p. 1] | ✅ | ✗ standard in the trust-region school | Method 4 variant (standard sub-step: bridge lemma) + proof-device inventory |
| Inexactness tied to the step + weakest condition the proof touches | 15 + 8 | ✅ 1996–2025 | ✅ [S013 p. 2; S048 p. 11] | ✅ | ~ (inexact-Newton tradition) | Method 3 variant (deterministic ancestor) + H3 rewrite |
| Known-answer testbeds (generators, planted truth) | 9 (+2 abstract) | ✅ 1993–2012 | ✅ [S002 p. 6; S053 p. 14] | ✅ | ✅ moderate | Heuristic + Method 5 variant; not promoted because it is a sub-step of Method 5 and era-bound (generators and planted-truth ladders 1993–2012; later only closed-form test instances, e.g. [S042 p. 26]) |
| Cross-field import via specialist coauthor | 12 | ✅ 1999–2025 | ~ stated motive only [S051 p. 1] | ✅ | ✅ moderate | Heuristic, §5 |
| Mechanism-isolating controls and fairness handicaps | 20 | ✅ 1996–2026 | ~ | ✅ | ~ | Method 5 variants (standard-practice refinements of steps 1 and 4) |

---

## 5. New heuristics (the list stays at 10)

Final list (after review): H1, H2, H3 (generalized), H4 (scoped), H6, H7, H8, H10 (rewritten; absorbs the distinctive facets of the Method 6 candidate, §4.1), H11 (= H-new-A), H12 (= H-new-B). Numbers 5 and 9 are retired, so the H# links in 07 keep their first-pass meaning. H5 folds into Method 4 step 2 (its content is already there, and its one new card is a variant [S107 pp. 4, 8, 11]); H9 folds into Method 2 step 5 with the corrected wording [S041 pp. 1, 5, 8].

- **H10 (rewritten; as first proposed)** — *If you reject a design alternative, or push a theorem to weaker regularity, then build the smallest example on which the alternative (or each hypothesis) fails, print it next to the choice, and aim a second example at the proof steps, not only at the hypotheses.* Cards: rejected alternatives [S011 p. 44; S081 p. 5; S020 pp. 19–20; S022 pp. 9–10; S108 p. 78; S110 p. 5; S096 pp. 16, 23–24; S092 p. 6; S113 pp. 18–19; S040 pp. 133–134]; what a measure cannot do [S074 p. 8]; hypothesis-breaking suites and threshold sweeps [S024 pp. 17–23; S108 pp. 80–84]; counterexample printed up front with the scope narrowed [S083 p. 3; the example was supplied by Audet]; the class's known failure example run and reported [S007 pp. 25–26]; pathological example that shows an assumption is not vacuous [S046 p. 23]; one example with every pathology [S055 pp. 1–2]; reusable 1-D pathology [S062 pp. 11–13; S044 pp. 5–6]. Checks: executable ✅, recurrence ✅, say–do ✅; exclusivity ✗. Review outcome: SKILL.md's H10 states the practiced part (print the smallest example where the alternative or each hypothesis fails) plus the Method 6 candidate's proof and code facets; the proof-step clause has no practiced case and is kept only as a labelled lesson from the 2024 external critique (SKILL.md Inner Tensions).
- **H11 = H-new-A (cross-field import)** — *If a constant, subproblem or test in your method has an equivalent in another field, restate it in that field's language and import that field's certified result or solver, with a specialist coauthor.* Cards: cosine measure as a covering radius with discrete-geometry bounds [S041 pp. 6–7, 9]; compressed-sensing recovery for sparse models [S029 pp. 2, 28; S051 p. 1]; SPRT bounds for the acceptance test [S102 pp. 9–10]; DCA from its developers as subproblem engine [S064 pp. 2, 4; S097 pp. 2–5]; multigrid tools from a PDE-control coauthor [S044 pp. 16–18]; SDP certificates with a solver developer [S087 pp. 7, 21]; export of DFO interpolation to Hessian-free methods [S089 pp. 4, 15]; a trust-region object exported to discriminant analysis [S099 pp. 13–15]; a selection criterion from finance [S094 pp. 3–4]; domain-decomposition steps [S108 p. 5]. Checks: executable ✅, recurrence ✅ (12 cards, 1999–2025), exclusivity ✅ moderate; say–do weak.
- **H12 = H-new-B (known-answer testbeds)** — *If no benchmark with known answers exists, generate one with planted solutions and controlled difficulty, certify the instances against the competitors' assumptions, and release the generator as its own citable artefact; in applications, climb a planted-truth ladder (calibrated case → synthetic with known answer → real data).* Cards: [S053 pp. 1–2, 4–9, 14; S026 pp. 1, 9–10, 15–16; D001 pp. 1–4; S002 pp. 4, 6; S055 p. 2; S028 pp. 14–15; S075 pp. 4–8; S087 pp. 8–17; S082 pp. 4–5]; abstract-level [S033; S063]. Checks: all four pass at heuristic grade; kept as a heuristic (see §4.2).
- **H3 (generalized)** — *If information is inexact or noisy, put the accuracy requirement on the quantity the acceptance test uses, tie it to the step size or predicted decrease, make it checkable with quantities available at the iteration, and let the iteration (or the data) decide the effort.* Deterministic cards §3.3 (Method 3); stochastic [S067 pp. 5–8; S102 pp. 5, 10; S110 pp. 14–15].
- **H4 (scoped)** — keep "nondominated list, no a-priori aggregation" for the derivative-free line [S003 pp. 1–2; S016 pp. 2, 4, 13; S017 pp. 2–3, 18; S065 pp. 4, 9; S101 pp. 15–16, 27; S113 pp. 18–21, 41–42]. Add: in the gradient-based ML line, weights appear only in the analysis or as step frequencies, and fronts are traced by sweeping them; state the implied weighted function [S015 pp. 3, 6–8; S017 pp. 13–16; S093 pp. 3, 17; S065 pp. 4, 8; S111 p. 4]. Contradictions: [S080 pp. 18, 21–22; S093 pp. 3–4, 15–16; S111 pp. 2, 4, 8, 11].

Method step refinements (not new heuristics):
- Method 1 step 4: "reset *or switch*" [S050 pp. 6, 11; S073 pp. 5–6; S088 p. 6].
- Method 2 step 5: "is the n-order optimal among poll-set designs within this proof template?" [S041 pp. 2, 5, 8].
- Method 3 step 2: "find the one instance of the requirement the proof uses" [S019 p. 5; S045 p. 8].
- Method 4 steps 4–5: "prove one bridge inequality; check the collapse to the old theory" [S037 pp. 6–7; S046 pp. 7–9; S003 p. 14; S013 pp. 1–2]. Review outcome: recorded as Variants (standard sub-steps), not numbered steps.
- Method 5 steps 1 and 4: "add one control variant that removes the mechanism you credit, and give baselines their best settings" [S074 pp. 20–21; S060 pp. 13, 15; S045 p. 17; S058 p. 22; S008 p. 14; S046 pp. 21–22; S042 p. 26; S018 p. 13]. Review outcome: recorded as Variants (standard practice), not added to the steps.

---

## 6. Candidate pool (not promoted)

| Cluster | Full/partial | Abstract | Span | Why not promoted | Cards |
|---|---|---|---|---|---|
| Publication architecture: theory paper + application paper; infrastructure as its own citable paper | 9 | 1 | 1994–2026 | common publication practice; fails exclusivity; kept as a writing move | D001 S016 S017 S048 S082 S086 S093 S101 S107 (S112) |
| Design around the user's existing oracle / matrix-free interface | 7 | 0 | 1996–2022 | heuristic-grade but tied to the derivative-based period; covered by Method 2's cost unit | H004 H007 S011 S040 S048 S089 S106 |
| Import a formalism and claim the first stochastic version | 7 | 0 | 2024–2026 | one period; field-wide trend; trajectory note only | S017 S042 S067 S070 S091 S101 S110 |
| Condition on the past, not independence | 6 | 0 | 2014–2026 | already Method 3 step 2 | S014 S019 S043 S067 S102 S110 |
| Project a heuristic's proposal onto the mesh; unified ρ̄; zero-extra-evaluation slots | 6 | 0 | 2001–2012 | Method 1 glue evidence (§3.1 row 1) | S003 S005 S008 S024 S025 S106 |
| Reformulate so an existing solver applies | 6 | 2 | 2006–2026 | Method 4 problem-level variant | S022 S036 S061 S080 S096 S101 (S009 S069) |
| Case split by mode or iteration type | 5 | 0 | 2004–2023 | proof device | S006 S007 S032 S049 S073 |
| Implicit weights (analysis weights, effort, step frequencies) | 5 | 0 | 2019–2026 | H4 scope variant | S015 S017 S065 S093 S111 |
| Supervisor-role authorship on student-led artefacts | 5 | 0 | 2020–2025 | collaboration pattern, not a method | S042 S086 S091 S113 S120 |
| Survey as a problem-feature routing table / component map | 4 | 1 | 2001–2020 | writing move; Workflow A evidence | S038 S055 S056 S113 (S001) |
| Exponent balancing | 4 | 0 | 2013–2025 | Method 2 proof device | S023 S032 S034 S107 |
| Reuse guidance to order the poll; import model geometry into direct search | 4 | 0 | 2001–2008 | H7 evidence/variant | S008 S025 S030 S106 |
| Two-layer proof (realization-wise count + conditional Chernoff) | 3 | 0 | 2015–2019 | Method 3 step 4 device | S019 S027 S045 |
| Certify-and-repair; two-sided equivalence; criticality step | 3 | 0 | 2008–2009 | one collaboration (Conn–Scheinberg); proof device | S006 S010 S020 |
| Exploit the problem's own geometry | 3 | 2 | 1994–2015 | generic; fails executability and exclusivity | S002 S057 S099 (S009 S052) |
| Robustness over definitional choices | 3 | 0 | 2025 | one year | S092 S096 S102 |
| Switch between step types by a monitored inequality | 3 | 0 | 2017–2024 | Method 1 step 4 variant | S073 S088 S104 |
| Nondominance as a design primitive (filter → bilevel → DMS) | 2 | 0 | 2004–2006 | history of Method 4/H4 | S007 S022 |
| Formalize an informal notion | 2 | 0 | 2025 | already H8 | S092 S096 |
| Multistart for non-identifiable inverse problems | 2 | 0 | 2011–2012 | two application papers | S075 S082 |
| Check objective conflict before going multiobjective | 2 | 0 | 2018–2023 | two papers | S036 S080 |
| Service: stewardship record; consult–prune–solicit; prize as long-horizon signal | 2 | 0 | 2023–2025 | non-research | S121 S122 |
| Prove the problem hard beside the algorithm | 0 | 2 | 1994 | abstract-level only | (S004 S069) |
| Singletons (20 patterns on 16 cards) | 16 | — | — | below the ≥3 threshold | S005 (heuristic's own termination), S017 (composite-estimator bias audit; diagnose predecessor's assumption), S016 (reclassify a neighbour's method), S028 (clean inputs with a characterization theorem), S034 (problem-class statement), S046 (deterministic counterpart of an in-expectation result), S054 (forward-compatible acceptance test), S068 (fit variant to parallel architecture; reduce search space), S070 (enumerate readings; companion problem; frozen special case), S074 (lazy escalation), S078 (all local optima for a combinatorial master), S084 (branch freezing), S089 (change the unknown), H003 (sibling-algorithm correspondence), H004 (research notes recycled as teaching), S109 (applications through one's own network) |

---

## 7. Technique inventory

### 7.1 Proof devices

- **Two-counter complexity count** — successes from a step-size floor plus telescoped sufficient decrease; failures from the logarithm of the step-size product: [S023 pp. 5–6; S034 pp. 9–10; S046 pp. 10–11; S074 pp. 14–16; S060 pp. 10–12; S108 pp. 22–23; S032 pp. 7–10; S045 pp. 10–11; S110 pp. 7–9]; per realization in the probabilistic case [S019 pp. 10–12; S027 pp. 6–8]; telescoping over the one step type with provable decrease [S073 p. 8; S088 p. 10; S015 pp. 4–5].
- **Step size → 0 / lim inf** — lattice finiteness [S005 p. 10; S003 p. 30; S083 p. 6]; summability of forcing-function decreases [S049 p. 7; S050 pp. 6–7; S057 p. 5; S073 pp. 10–11; S088 pp. 11–12; S058 p. 5; S014 pp. 8–9; S006 p. 18; S071 pp. 9–10]; packing arguments (disjoint squares, hypercubes) [S007 p. 17; S003 pp. 30–31].
- **Refining-direction Clarke stationarity** — [S003 p. 13; S024 pp. 11–13; S049 pp. 8–11; S050 p. 8; S057 pp. 6–7; S058 pp. 7–8; S067 pp. 12–14; S073 pp. 11–12; S088 pp. 12–13; S030 pp. 5–9].
- **Bridge to a classical theorem** — Powell's Cauchy bound, Nesterov's template, Dennis–Moré, lemma-by-lemma reuse: [S037 pp. 6–7; S081 pp. 4–5; S031 p. 10; S039 pp. 6–7; S062 p. 5; S011 p. 28; S040 pp. 28, 109–110; S084 pp. 7–10; S085 pp. 9–10; S046 pp. 4, 7–9; S077 pp. 18–21; S042 p. 18; S043 p. 10]; role dictionary between companion methods [S027 pp. 6–8]; transplant across families [S071 pp. 2–3, 9–11]; lemma-dependency map [S108 p. 23].
- **Absorbing inexactness** — threshold shift η₁ → η₁ + ξ₀ [S013 p. 14]; inexact computations as exact ones with perturbed operators [S040 pp. 139–141]; inexact KKT point = exact solution of a perturbed problem [S090 p. 22]; inexact values within a fraction of the predicted decrease [S047 pp. 5–6]; Carter-type relative-error conditions [S062 pp. 8–9; S044 p. 7].
- **Probabilistic machinery** — log step size against a ±1 random walk, submartingale [S014 pp. 10–11; S019 pp. 8–9; S043 pp. 9–11; S045 pp. 13–14]; realization-wise count + conditional Chernoff [S019 pp. 11–13, 23–24; S027 pp. 6–9]; potential with expected decrease and capped false-acceptance loss [S067 pp. 11–12; S102 pp. 11–13; S110 pp. 16–18]; renewal–reward stopping time with arbitrary p [S102 pp. 22–25; S110 p. 13]; half-step σ-algebra [S102 pp. 11–14; S110 pp. 15–16]; Borel–Cantelli on summable step sizes [S067 pp. 12–14]; spherical-cap probabilities [S019 pp. 25–26; S050 p. 9].
- **Stochastic-gradient templates with O(α_k) error budgets** — null-term three-way split [S017 pp. 13–14]; every inexactness source at O(α_k) [S042 pp. 13–18]; one Lyapunov term per level plus coefficient-sign analysis [S091 pp. 14–16, 26–30]; drift bounds for alternating schemes [S093 pp. 8–10; S111 pp. 15–16]; µ-change term and schedule coupling [S107 pp. 11–13].
- **Mirror the gradient-method proof** in convex and strongly convex classes — [S046 pp. 3–4, 9, 13–14, 17; S015 pp. 6–8; S017 pp. 13–16; S042 pp. 19–20; S107 pp. 8–10; S111 pp. 8–9; S073 pp. 9–10].
- **Implicit-function sensitivity** — [H004 pp. 4–5; S099 pp. 5–6; S062 pp. 3–4; S095 pp. 8–10; S098 pp. 9–14; H003 pp. 4–5; S042 p. 7; S070 pp. 8, 10; S096 pp. 11–12, 19–20].
- **Geometry and poisedness** — two-sided equivalence and the norm-equivalence trick [S010 pp. 8–10]; max-determinant subset [S020 p. 4]; geometry for free after an unsuccessful poll [S008 pp. 10–11]; poisedness bounded by the cosine measure [S030 p. 10]; cosine measure = covering radius [S041 pp. 6–8]; RIP with a bounded orthonormal basis [S029 pp. 11–15].
- **Exponent balancing** — [S023 p. 7; S034 p. 10; S032 p. 15; S107 pp. 10–11 (as an LP)].
- **Case split by mode or iteration type** — [S049 p. 4; S073 pp. 4, 10–11; S032 pp. 7, 9–10; S006 pp. 15, 17; S007 pp. 21–22; S077 pp. 24–25].
- **Constructions that mark a boundary** — conjecture with the failing inequality [S014 pp. 20–21]; saddle counterexample [S074 p. 8]; sharpness example plus threshold sweep [S108 pp. 77–84]; the natural merit function shown to increase [S110 p. 5]; tightness by reduction to steepest descent in dimension 1 [S023 p. 8]; order relation defined so the characterization is definitional [S022 p. 8]; quantile reflection to get a mirror characterization [S101 pp. 23–24].

### 7.2 Algorithm-design moves

- **Put the efficient component in a proof-free slot** (search, poll order, Full-Eval) — [S008 pp. 3–4; S005 pp. 8–10; S025 pp. 6, 9; S012 p. 8; S064 pp. 7–8; S071 pp. 3–4; S073 pp. 5, 10; S039 p. 4].
- **Decouple the heuristic's own step from the convergence-controlling step; reset or switch** — [S050 pp. 6, 11; S057 p. 4; S073 pp. 5–6; S088 p. 6; S068 p. 13].
- **Tie the model or sampling radius to the step size** — [S008 p. 10; S012 p. 7; S064 p. 8; S089 p. 7; S079 p. 20].
- **Handle constraints by evaluation status** — relaxable via merit + restoration, unrelaxable via extreme barrier [S049 pp. 4–6, 13; S018 p. 5; S057 p. 3; S075 p. 3; S005 pp. 6–7]; tangent-cone generators [S018 p. 11; S057 pp. 9–10; S045 p. 7; S088 p. 5].
- **Lift a single-point method to a list** — [S003 pp. 4–7; S016 p. 13; S017 p. 18; S065 p. 9].
- **Split one step into parts with their own measures** — [S007 pp. 6–7; S011 pp. 10–20; S040 pp. 95, 99; S060 pp. 5–6].
- **Tie inexactness to progress with implementable tests** — [S040 p. 136; S013 pp. 10, 16; S047 pp. 8, 14; S085 pp. 4–5; S090 p. 16; S097 p. 8; S073 pp. 12–13; S088 pp. 13–14; S042 pp. 13, 20–21; S017 pp. 11, 17; S043 p. 7].
- **Put the accuracy requirement on the quantity the acceptance test uses** — [S067 pp. 5–8; S102 pp. 5–7; S110 pp. 14–15; S013 pp. 9–10].
- **Turn a proof threshold into an implementation rule** — number of random directions [S019 p. 20; S045 p. 16]; radius factors [S027 p. 8]; acceptance threshold rule and a patch to a widely used solver [S108 pp. 84–85, 97–98]; test boundaries [S102 p. 18]; schedule exponents [S107 p. 24].
- **Reuse information already paid for** — [S008 pp. 7–9; S012 p. 7; S030 p. 13; S047 p. 9; S059 pp. 3–4; S064 p. 22; S074 pp. 5–6, 10–12; S089 pp. 12–13; S104 pp. 7–8].
- **Encode weights as effort or schedules** — [S065 pp. 4, 8; S093 pp. 3, 15–16; S111 p. 4].
- **Reformulate so an existing solver applies** — [S022 p. 12; S036 p. 6; S061 p. 14; S080 p. 4; S101 p. 9]; DFO as the outer solver of a derived low-dimensional problem [S096 pp. 8–9].

### 7.3 Experiment protocols

- **Function evaluations as the unit; budgets in n+1 or multiples of n** — [S005 p. 16; S012 p. 10; S049 pp. 14–15; S050 pp. 12–13; S073 p. 17; S088 pp. 18–19; S079 p. 21].
- **Profiles fitted to the class** — best/average/worst over runs for stochastic solvers [S005 p. 17; S018 pp. 14–15]; shifted ratio near zero [S005 p. 17; S018 p. 20; S097 pp. 11–13]; purity only pairwise and spread kept out of data profiles [S003 pp. 17–20]; cost per nondominated point and down-sampling of fronts [S016 p. 6; S065 p. 11]; profiles on the true f while solvers see noise, runs counted as problems [S067 p. 19; S102 p. 17].
- **Ablate a hybrid against each component** — [S005 pp. 26–27; S073 pp. 14, 17–22; S088 p. 17; S050 pp. 14–18; S057 pp. 11–18; S064 pp. 9–13; S071 pp. 15–16; S102 pp. 17–18; S079 p. 21].
- **Mechanism-isolating controls and targeted test sets** — [S074 pp. 20–21; S060 pp. 13, 15; S045 p. 17; S058 p. 22; S110 pp. 18–19; S008 p. 18; S035 p. 8; S091 pp. 8–9, 47].
- **Fairness to baselines** — baselines tuned first [S008 p. 14]; oracle constants given to the rival [S046 pp. 21–22]; initial guesses withheld from all solvers [S018 p. 13]; one step-size grid per method [S042 p. 26]; biased experiment rerun [S019 p. 20]; rival results supplied by their authors [S012 pp. 15–16]; written fairness rule for stopping tolerances [S029 p. 25]; accelerating components switched off and said so [S045 p. 22].
- **Known-answer validation** — generators [S053; S026; D001]; planted truth [S028 pp. 14–15; S075 pp. 4–8; S087 pp. 8–17; S082 pp. 4–5]; closed-form lower level so the true objective can be plotted [S042 p. 26].
- **Assumption-boundary suites and threshold sweeps** — [S024 pp. 17–23; S108 pp. 80–84; S083 p. 7].
- **Robustness over definitions and parameters** — [S092 pp. 7–9; S096 pp. 16–19; S102 p. 18; S073 p. 22; S016 p. 5].

### 7.4 Writing moves

- **Contribution map; old theories as special cases in the abstract** — [S040 pp. 19–20; S011 p. 2; S013 pp. 1–2; S111 p. 5; S003 p. 14].
- **Algorithm box that marks the diff against the base method** — [S008 p. 7; S018 p. 6; S059 pp. 4–5; S050 pp. 3–6; S107 p. 7].
- **Phenomenon or worked example before the theory; design rationale before the algorithm** — [S003 pp. 7–9; S017 pp. 9–10; S014 pp. 5–6; S110 pp. 4–6].
- **Price or restriction in the abstract** — [S015 p. 1; S017 p. 1; S096 p. 1; S089 p. 1; S107 p. 1; S073 p. 1].
- **Close with specific open problems or a mechanistic reason** — [S024 p. 23; S041 p. 8; S083 p. 8; S091 p. 6; S110 pp. 14, 22].
- **Credit priority and rivals precisely** — [S015 p. 2; S038 p. 12; S041 p. 2; S110 p. 3].
- **Survey by problem feature or by component** — [S055 pp. 2–3; S056 pp. 7–9; S038 p. 2; S113 p. 41].
- **Tables of constants and notation** — [S006 p. 4; S014 p. 3; S086 pp. 3–4].
- **Paper architecture** — method + software paper in the same issue [S026 p. 1; D001 p. 1]; theory + application pairs [S017 p. 19 → S016 p. 4; S107 → S101 pp. 15, 25–26; S093 pp. 3, 15]; interface as a paper [S048 pp. 1–4]; dataset paper [S086 p. 1].

---

## 8. Trajectory as seen in the full texts

Topic tags by period (a work can carry two tags; BIL = bilevel/complementarity/global QP, TPG = test-problem generators, NLP = derivative-based nonlinear programming, DS = direct search, MB = model-based DFO and surrogates, WCC = worst-case complexity, PROB = probabilistic/stochastic DFO, MOO = multiobjective, SML = stochastic gradient methods for ML, APP = application, SUR = survey/book/service):

| Period | BIL | TPG | NLP | DS | MB | WCC | PROB | MOO | SML | APP | SUR | works |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1991–1995 | 9 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 12 |
| 1996–2000 | 1 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 16 |
| 2001–2005 | 1 | 0 | 6 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 3 | 13 |
| 2006–2010 | 1 | 0 | 2 | 7 | 5 | 0 | 0 | 1 | 0 | 2 | 3 | 17 |
| 2011–2015 | 1 | 0 | 2 | 6 | 5 | 3 | 2 | 2 | 0 | 4 | 2 | 22 |
| 2016–2020 | 0 | 0 | 2 | 3 | 2 | 8 | 3 | 2 | 0 | 4 | 2 | 17 |
| 2021–2026 | 3 | 0 | 2 | 3 | 3 | 0 | 3 | 9 | 12 | 4 | 2 | 26 |

Periods and turns:
1. **1991–1995, bilevel and test problems (Coimbra/Waterloo/GERAD)** — a classified bilevel bibliography [S002], test-problem generators with known minima [S053; S026; D001; S033; S063], descent methods and hardness results [S004; S069], optimality conditions [S052]. Seven of its twelve works are abstract-level and one is metadata-only (§11). This period is missing from SKILL.md's trajectory.
2. **1996–2000, derivative-based NLP at Rice** — trust-region interior-point SQP for optimal control, the thesis and TRICE [S040; S011; S037; S031; H007], the interface paper [S048], local theory [S084; H002; H003], IBM two-step algorithms [S039]. Seven single-authored works in five years (§9).
3. **2001–2005, transition** — derivative-based work continues (inexact SQP [S013], degenerate NLP [S054; S076], multipliers [S095; S098], filter interior point [S007]); direct search enters through an application (molecular geometry) [S106; S025]; surrogates through space mapping [S062; S044] and a surrogate-optimization special issue [H001]; the 2001 overview maps local NLP as components [S056 pp. 7–9].
4. **2006–2010, direct search made efficient + model geometry** — PSwarm [S005; S018], SID-PSM [S008; S030; S059; S012], the Conn–Scheinberg geometry and DFO trust-region trilogy [S010; S020; S006], the book [S001], bilevel as multicriteria [S022]; interior-point work ends here [S077; S085].
5. **2011–2015, new classes + complexity + probability** — DMS [S003], discontinuous functions [S024], merit functions [S049], ES [S050; S057], bilevel DFO [S047], sparse models [S029; S051], complexity [S023; S034], probabilistic models and descent [S014; S019].
6. **2016–2020, complexity programme and Toulouse collaborations** — [S032; S041; S046; S074; S027; S060; S108]; probabilistic extensions [S043; S045]; multiobjective complexity [S015]; survey [S038]; applications [S035; S036; S068].
7. **2021–2026, Lehigh: stochastic ML-facing methods** — stochastic multiobjective learning [S094; S016; S065; S093; S017; S101; S111], bilevel and trilevel SG [S070; S042; S091], stochastic DFO [S067; S102; S110], full-low evaluation [S073; S088], a negative result on neural surrogates [S079], knee solutions [S096], sports analytics [S086; S092; S120]. The dominant move is "the first stochastic version of a known formalism" [S042 p. 5; S070 p. 1; S091 pp. 1–2; S101 p. 3; S017 p. 5; S067 p. 4; S110 p. 4].

What stayed constant:
- **Keep the skeleton, change one object** — 1996 [S037 pp. 5–7; S040 p. 103] to 2026 [S110 p. 4].
- **Inexactness tied to progress** — 1996 [S040 p. 136], 2002 [S013 p. 10], 2012 [S047 p. 8], 2024–2025 [S088 pp. 13–14; S042 pp. 13–14].
- **Artefacts** — generators 1993–94 [S053 p. 14; D001], TRICE and the interface 1997–99 [H007 p. 3; S048], PSwarm/SID-PSM 2007–09 [S005 p. 14; S059], DMS collection 2011 [S003 p. 15], GitHub code 2022–25 [S016 p. 5; S042 p. 22; S091 p. 7].
- **Publishing the boundary** (H10; the Method 6 candidate, §4.1) — 1998 [H003 pp. 4, 18–19] to 2026 [S110 p. 14].
- **Applications** — circuits [S039 pp. 17–18], molecules [S106; S025], superconductivity [S044 p. 18], finance [S028; S087; S061], astrophysics [S075; S082], data assimilation [S043], geophysics [S068], medicine [S035], manufacturing [S036; S078], transport [S080], fairness [S016; S101], sports [S086; S092]; stated rationale: applications grow from one's own research portfolio and contacts [S109 pp. 4–5].

---

## 9. Collaboration pattern

Most frequent coauthors by period (works per coauthor; S056 counted as single-authored §2.1; S121/S122 as signed columns; S066, S116, S117 excluded):

| Period | Works | Single-authored | Top coauthors |
|---|---|---|---|
| 1991–1995 | 12 | 1 | Calamai 7, Júdice 6 |
| 1996–2000 | 16 | 7 | Dennis 3, Heinkenschloss 2 |
| 2001–2005 | 13 | 4 | Alberto 2, Nogueira 2, Rocha 2, S. J. Wright 2 |
| 2006–2010 | 16 | 2 | Conn 4, Scheinberg 4, Custódio 4, Vaz 2, R. Silva 2 |
| 2011–2015 | 20 | 1 | Vaz 5, Gratton 5, Bandeira 3, Scheinberg 3 |
| 2016–2020 | 17 | 0 | Gratton 8, Z. Zhang 4, Royer 4, Vaz 2, Dodangeh 2 |
| 2021–2026 | 26 | 2 | Giovannelli 10, S. Liu 5, Sohab 3, Kent 3 |

Overall: Gratton 14 (2014–2022), Vaz 10 (2007–2022), Giovannelli 10 (2023–2026), Scheinberg 8 (2008–2017), Calamai 7 (1992–1995), Júdice 7 (1992–1996), Custódio 7 (2007–2017), Conn 6 (1999–2012), Z. Zhang 6, S. Liu 6, Royer 6, Dennis 5 (1996–2008).

Patterns:
- **Long pairings of 5–15 years**, one or two per period, each tied to a line of work: bilevel/generators with Calamai and Júdice [S002; S053; S026]; derivative-based NLP with Dennis and Heinkenschloss [S037; S031; S011; S013; S048]; model geometry with Conn and Scheinberg [S010; S020; S006; S014]; direct search with Custódio and Vaz [S008; S005; S018; S003; S024]; complexity and probability with Gratton, Royer and Zhang [S019; S027; S045; S074; S060; S108]; stochastic ML with Liu and Giovannelli [S016; S017; S070; S042; S091; S096; S101; S107].
- **Solo work concentrates early**: 13 single-authored research works, 11 of them in 1991–2005 [H008; S040; S081; H007; H003; H004; H002; S084; S055; S095; S062], then [S083 (2009); S023 (2013)]. Besides these: the 2006 essay [S109], his COCONUT section [S056 §2.1] and the signed service columns [S121; S122]. No single-authored research work after 2013.
- **Junior coauthors in every period** (status as signalled in the texts; the advising relation itself is not stated in them — Review outcome): Custódio (PhD thesis record, advisor Vicente); Garmanjani (FCT SFRH/BD doctoral scholarship; "the forthcoming PhD thesis of the first author") [S034 pp. 1, 18]; Dodangeh (FCT SFRH/BD doctoral scholarship) [S046 p. 1; S041 p. 1]; Diouane (CERFACS) [S050 p. 1]; Royer (Toulouse doctoral grant) [S019 p. 1; S027 p. 1]; Song ("a future PhD thesis of the first author") [S089 p. 15]; Liu (Lehigh PhD thesis record); Kent (Lehigh PhD thesis cited as in preparation) [S091 p. 6, ref. 26]; Giovannelli (status not stated in the texts read); Tran (Lehigh postdoc) [S110 p. 1]; further Lehigh coauthors Sohab [S073; S088; S079], Ding [S102; S110] and Tan [S107; S101].
- **Specialist coauthors bring certified tools** (H11): PDE control [S044], SDP solvers [S028; S087], DC programming [S064; S097], compressed sensing [S051; S029], discrete geometers acknowledged [S041 pp. 7, 9], a statistician [S099].
- **Supervisor-role signals in student-led artefacts**: CRediT lists conceptualization, review, supervision and funding only [S086 p. 5]; code in the student's repository and proofs deferred to the student's thesis [S042 p. 22; S091 pp. 6–7, 41]; slides presented by the student [S113]; undergraduates as first authors [S120 p. 1].
- **Governance style** (service, not research): consult, list options, drop the unpopular one, request structured proposals, survey only if needed [S122 p. 24]; count before adjectives in reports [S121 p. 14].

---

## 10. Rejected updates

1. Adding "condition on the past" as a method or heuristic — already Method 3 step 2 [S014 p. 7; S019 p. 7].
2. Adding the two-layer probabilistic proof, exponent balancing, case splits or certify-and-repair as methods — proof devices only (§7.1).
3. Adding "nondominance as a design primitive" separately — history of Method 4 / H4 [S007 pp. 1–3; S022 pp. 2, 8].
4. Adding "theory paper / application paper split" or "infrastructure as a publication" as methods — common practice; writing moves only (§7.4).
5. Adding supervisor-role authorship, service stewardship, "consult–prune–solicit" or "prize as long-horizon signal" to research methods — non-research [S086; S121; S122].
6. Adding "exploit the problem's own geometry" — generic, not executable [S002; S057; S099].
7. Adding "first stochastic version of a formalism" as taste — a field-wide trend in one period; trajectory note only (§8).
8. Promoting negative examples, nesting, bridge lemmas, inexactness tied to the step, known-answer testbeds or controls to separate core methods — absorbed as steps, variants or heuristics (§4.2, §5).
9. Adding quantum computing to the trajectory — service-level mention only [S121 p. 14].
10. Changing Mentor Voice's register for technical feedback — the warm register is from service columns only [S122 p. 23].
11. Claiming an own-words explanation of the ML pivot — only a field-level sentence exists [S121 p. 14].
12. Attributing any COCONUT content beyond §2.1 to Vicente [S056]; using S113 as Vicente-written content beyond a co-presented review; using S120 or S086 as method evidence [S120; S086].
13. Surfacing any reading-note inconsistency (typos, table–text mismatches, parameter mismatches) as a finding about a paper — excluded by rule; only the general lesson in the header is kept.
14. Replacing Method 5's profile norm by "collections are optional" because of the genre variants — the variants are scoped, the norm holds for algorithm papers (§3.3).

---

## 11. Open gaps

- **The book is unread in full text.** S001 (2,876 citations) is at abstract level only; its stated methodology (why models and direct search, what "modified" Nelder–Mead or implicit filtering means) would strengthen or change the stated side of Methods 1, 4 and 5 [S001].
- **1991–1995 is mostly abstracts.** Seven of the twelve works of 1991–1995 are abstract-level [S004; S021; S033; S052; S063; S069; S100] and one is metadata-only [H008]; the 1996 discrete bilevel paper is also abstract-level [S009]. Whether the 1994 hybrid descent method already shows Method 1's "fast step + guarantee" shape rests on one abstract [S004]; whether early computational comparisons already had collection-style protocols rests on one abstract [S021].
- **Metadata only**: H005, H006 (1998 telecom notes), H008 (1991 vehicle routing), S116 (apparently a 2012 thesis title page; Vicente's role not verified), S117 (a special-issue preface).
- **Partial reads (16)**: claims for S029, S031, S032, S043, S045, S054, S056, S058, S060, S068, S077, S078, S090, S095, S098 and S108 rest on the sections read.
- **Versions**: nearly all texts are preprints or arXiv versions; page numbers and abstract wordings may differ from the published papers (e.g. the "matching" wording of [S019 p. 1]).
- **Code and errata not inspected**: SID-PSM, DMS, PSwarm, FLE and the GitHub repositories named in the cards were not opened; only the S112 package header was inspected [S112]. The "snee" repository (a first-pass link, RESOURCES row 28; the S096 text gives none [S096 p. 6]) was not checked.
- **External papers not read**: the 2024 counterexample to [S024] and the 2026 non-convergence analysis of probabilistic direct search; how they bear on [S024 pp. 11, 15] and [S102 p. 16; S110 pp. 13, 18] is open.
- **Tacit layer still thin**: the only primary evidence of how he runs a collective decision is a SIAG board column [S122 p. 24]; theses of his students (Custódio, Diouane, Royer, Liu, Kent) were not read.
- **Recent output**: works after 2026-09-27 are not covered.
