# Katya Scheinberg · Deep-reading synthesis

> Date: 2026-09-27. Input: every card in `cards/` (21 batch files, 125 card entries; index in `07-paper-cards.md`). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only, existing methods get evidence first, a new method needs ≥3 distinct papers plus the four checks, reject updates without explanatory power, every claim traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`.
>
> Citation form: `[S012 p. 9]` = card S012, page of the extracted text as recorded on the card. `S043/D001` = one paper read under two ids. Counts are **distinct papers** after merging the five same-text pairs (S011 = S123, S089 = S106, S098 = S107, S028 = S067, D001 = S043, filed under the first id of each pair); S143 has an abstract card and a full card and counts once. Cards that record typos or internal inconsistencies of a paper are reading notes and are not used as findings here.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Google Scholar rows | 143 (129 distinct works after 14 duplicate/junk rows) | `07-paper-cards.md`, Coverage |
| Works in `works.json` | 132 (129 Scholar + D001–D003 from DBLP/arXiv) | same |
| Card entries / distinct papers carded | 125 / 119 | same |
| **Full text read** | **78** (64 full, 14 partial) | read-level column of `07-paper-cards.md` |
| Abstract-level | 19 | a2-01, a2-02 |
| Metadata-only | 21 | a2-01, a2-02 |
| Unreadable | 1 (S133; the DFO v2.0 manual was carded as a substitute) [S133 pp. 1–3] | s2-01 |
| Skipped | 8 (3 patents, 4 talks, D002 where Scheinberg is an author only on arXiv v1) | INDEX.md Role = skip |

Full-text reads by period (full + partial / all carded works with a year): 1996–2000 3/13; 2001–2005 5/8; 2006–2010 14/24; 2011–2015 13/17; 2016–2020 25/32; 2021–2026 18/22. The pre-2000 interior-point work is therefore known almost only from abstracts [S027, S040, S045 abstract cards; S039, S034, S091, S134 metadata cards], while the DFO and stochastic-analysis lines are read nearly completely.

Versions actually read, where they differ from the listed venue: S015 is arXiv v1 with the earlier title and no numerical section [S015 p. 1]; S043/D001 is arXiv v5, the SIOPT extension of the NeurIPS paper [S043 contribution; D001 p. 1]; S093 is arXiv v2 [S093 header]; S106 is the 2019 arXiv v1 (same file as S089) [S106 contribution]; S123 is a later revision titled like S011 [S123 contribution]; S021 is the Oct 2013 author preprint [S021 contribution]; S067 is byte-identical to S028 [S067]; S104 is arXiv v1 [S104 header].

---

## 2. Evidence per existing method

Counts below are distinct full/partial/unreadable-substitute papers that the cards link to each method (a paper can give both evidence and a variant). Abstract-level links are listed separately and are not used for decisions.

| Method | Evidence ✅ | Variant ⚠ | Contradiction ✗ | Distinct papers touching it | Abstract-level links |
|---|---|---|---|---|---|
| M1 Oracle contract | 26 | 30 | 0 | 48 | 4 ✅, 1 ⚠ |
| M2 Keep the classical adaptive method | 52 | 11 | 2 | 64 | 4 ✅, 2 ⚠ |
| M3 Stochastic process + deterministic-order complexity | 17 | 23 | 0 | 34 | 3 ✅ |
| M4 Geometry is the price; pay the minimum | 21 | 2 | 0 | 22 | 4 ✅ |
| M5 Compare estimators at equal accuracy | 17 | 29 | 2 | 44 | 1 ✅, 3 ⚠ |
| M6 Exploit structure before going generic | 31 | 8 | 0 | 39 | 2 ✅, 1 ⚠ |

All six methods survive the full texts. The large variant counts for M1, M3 and M5 are mostly deterministic precursors [S004 p. 17; S007 pp. 7–8], out-of-scope lines such as stochastic gradient and applied ML [S002 pp. 3, 5; S009 pp. 11–13; S051 pp. 5–7], and one proof-skeleton correction for M3 [D001 pp. 7–13; S041 pp. 16–21; S083 pp. 11–15], detailed in §3.

### M1 · Oracle contract ("accurate enough, often enough")

- **Strongest practice**: two events I_k, J_k with accuracy ∝ δ_k and δ_k², fixed probabilities conditioned on the past, and failures otherwise unrestricted [S012 pp. 3, 8–9]; separate model and estimate contracts, unbiasedness not assumed [S013 pp. 4, 11–12]; SZO/SFO contracts with bias allowed and oracles built from mini-batches and randomized finite differences [S043/D001 pp. 1–2, 4, 24–25]; irreducible floors ε_g, ε_H with implementability derived for ERM and finite differences, giving the reachable accuracy ε ≥ O(√ε_f) + O(ε_g) [S041 pp. 2, 4–5, 8–9, 21]; the cost of meeting the contract written as an explicit function oc(α) [S057 pp. 4, 11–12, 14, 17]; contracts for corrupted gradients and heavy-tailed values [S083 pp. 2–5, 15].
- **Stated in full texts** (new; SKILL.md relied on talk abstracts): random-model results need sample sizes tied to the step length or radius, with the accuracy hierarchy Hessian < gradient < function value [S031 pp. 21–22]; accuracy scaled to Δ_k or α_k‖g_k‖ with probability 1−δ, and substituting ε for the unknown gradient norm is criticised [S047 pp. 8–9, 12]; probabilistic models fully linear with a probability conditioned on the past [S046 pp. 7–8]; the stated limitation that "it is not necessarily easy to estimate what these probabilities ought to be" [S012 p. 3]. Abstract-level: models accurate only with some high probability [S120 abstract]; oracle failure types enumerated [S111 outcomes report].
- **Deterministic ancestry** (variants, 1997–2015): sufficient sampling combined with geometry for noisy f [S004 p. 17]; radius-scaled accuracy κΔ with a finite repair procedure [S007 pp. 7–8; S143 p. 3]; the error ≤ κΔ shape [S072 pp. 10, 19]; noise damage tied to the radius [S019 pp. 5–6]; the noise floor setting the final radius [S023 p. 19]; fidelity raised when predicted decrease reaches the noise level [S085 p. 2]; fitting tolerance O(Δ²) for SVR models [S121 pp. 5–6]; model quality stated as a probability, with a stochastic trust-region framework named as future work [S033 pp. 5–6].
- **Say–do update**: ✅ stays, now resting on full texts [S031 pp. 21–22; S047 pp. 8–9; S046 pp. 7–8] plus practice in ≥10 papers 2014–2025. The failure-tolerance and threshold statements need correction (§3, rows 2–3).

### M2 · Keep the classical adaptive method; change only what the weaker oracle breaks

- **Strongest practice**: "almost identical to the classical method", only the ‖g_k‖ ≥ η₂δ_k condition added [S018 pp. 1, 8]; the only major change is the relaxed acceptance test, the cautious radius update the second small repair [S041 pp. 11–12]; the Armijo test changed only by 2ε_f, the deterministic method recovered at zero noise [S026 pp. 4–5, 16]; one added control δ_k justified by the false-acceptance failure mode [S015 pp. 1, 3–4]; the failing property of ISTA/FISTA located and repaired with the authors' own deterministic backtracking device [S068 pp. 2, 5, 14–15]; Powell's method kept, criticality step swapped for ‖g‖ ≥ η₂Δ [S104 pp. 4, 18, 24–25; S088 pp. 2–3, 11–12]; STORM recovered exactly when φ = 0 [S098 pp. 1, 5, 27]; "three important aspects" where the standard trust-region proof breaks, and only those re-proved [S008 pp. 17–18].
- **Stated**: "The method itself is not new … Our contribution is to adapt it to the SVM framework" (2006) [S022 p. 3]; line search performs well, SGD is sensitive to parameters [S031 pp. 8, 11, 21]; SG is non-adaptive and tuned per application, the stochastic algorithm shares the deterministic structure [S047 pp. 1–2, 7]; adaptive methods borrow from deterministic optimization [S137 pp. 1, 5]; self-correction is credited to "the trust-region framework" and the new algorithm differs from CSV only in Steps 1, 4b and 5 [S143 pp. 3–5].
- **Say–do update**: ✅, with the stated side dating from 2006 [S022 p. 3], before the stochastic work. Scope must be narrowed (§3, row 4).

### M3 · Analyse the algorithm as a stochastic process and demand deterministic-order complexity

- **Strongest practice**: potential νf + (1−ν)Δ², upward-biased ±1 walk on Δ_k when αβ > 1/2, renewal-reward stopping time with p/(2p−1) [S013 pp. 5–10, 14–15]; hitting-time bound 2p/(2p−1)² by counting [S014 pp. 7–16]; line-search instance [S015 pp. 4, 8, 11, 17–19]; one template for TR, LS and cubic regularization [S047 pp. 7–8, 10]; high-probability tails [S043/D001 pp. 7–13, 17; S041 pp. 16–21, 37; S083 pp. 10–22]; step-parameter lower bound → sample complexity [S137 pp. 4–5; S057 pp. 7–13]; O(ε^{-3/2}) high-probability for stochastic ARC [S061 pp. 9–11; S093 pp. 3, 10–11, 15].
- **Stated**: methods with random estimates "retain their convergence rates" [S031 p. 21]; complexity stated in iterations and in function evaluations with explicit n-dependence [S046 pp. 2, 8]; the framework "can be applied beyond the algorithms discussed in this paper" [S013 p. 33].
- **Say–do update**: ✅. SKILL.md's limitation "steps 1–2 reconstruct the proof pattern from abstract-level descriptions" is now obsolete; the verified skeleton differs from steps 1–3 [D001 pp. 7–13; S041 pp. 16–21; S014 pp. 8–13] (§3, row 1).

### M4 · Geometry is the price of model-based DFO; pay only the minimum

- **Strongest practice**: the radius shrinks only with adequate geometry, certification at unsuccessful and criticality iterations, fully linear suffices [S008 pp. 11, 14–17]; models need be certifiable only within finitely many steps, checked only after a failed ratio test and in the criticality step (the paper source for Method 4 step 2) [S007 pp. 3, 13–14]; geometry necessary (counterexamples) but dedicated geometry evaluations confined to the criticality stage, self-correction elsewhere [S030 pp. 3, 8–15, 18]; random sample sets replace deterministic maintenance [S018 pp. 2, 23–26; S033 pp. 5, 22–23; S014 pp. 28–31]; geometry paid only on unsuccessful iterations with a bounded count (3n, O(p log p)) and randomized via subspaces [S088 pp. 7–8, 12–19]; certificate carried by n points only, Λ = 1000 in practice, benchmarked against NEWUOA [S104 pp. 10–12, 16–23, 27]; practice evidence that full quadratic models are unnecessary (~180 evaluations vs 528 for one full quadratic) [S019 p. 5].
- **Stated in her own words**: "it turns out that it is not necessary to compute extra sample points unless the gradient of the model becomes small" [S143 p. 4]; geometry cannot be totally ignored, but geometry steps are needed only when the model gradient is small [S046 pp. 3–4].
- **Say–do update**: ✅ from Scheinberg's own essay [S143 p. 4] matched point by point by S030 [S030 pp. 12, 14–15]. The attribution and dating in SKILL.md need correction (§3, rows 6–7).

### M5 · Compare estimators head-to-head at equal accuracy (theory + experiment)

- **Strongest practice**: one accuracy target for all estimators, N and σ derived per estimator, quality measured against the theory's θ < 1/2, end-to-end runs in one line search with data profiles in evaluations/(n+1) [S006 pp. 4–5, 25–31]; same target, derived N and σ, equal-N comparison [D003 pp. 7, 10–11]; FD vs REINFORCE at equal per-iteration sample cost inside one estimator-agnostic outer method [S073 pp. 6–7, 11]; equal evaluation budgets, random search at 2× budget, optimizer time separated [S052 pp. 6–8].
- **Group benchmark protocol, now verified** (SKILL.md Honest Boundary lists it as unverified): Moré–Wild 53-problem set, data profiles in simplex gradients, τ = 10⁻¹…10⁻⁷, deterministic noise, tolerances matched to the noise [S023 pp. 17–19]; function-evaluation performance profiles against a Powell-family code with a written tolerance rule [S033 pp. 25–26]; 53 CUTEr sum-of-squares problems with performance profiles [S012 pp. 27–29]; Moré–Wild set, data and performance profiles, fixed evaluation budget [S041 pp. 33–36]; CUTEst/S2MPJ, NEWUOA via PRIMA, profiles averaged over random rotations of the initial set, failures reported [S104 pp. 26–30].
- **Stated**: "In DFO it becomes also important to measure the effort in terms of the number of function evaluations" [S046 p. 8].
- **Say–do update**: ✅ [S046 p. 8; S006 pp. 25–31], scoped to the DFO and estimator line [S082 pp. 4–6; S089/S106 pp. 11, 13–14] (§3, row 17).

### M6 · Exploit structure before going generic

- **Strongest practice**: cheap constraints kept exact in the subproblem, equality constraints reduce the interpolation dimension [S019 pp. 6–7]; low-rank kernel makes the IPM solve O(nk²) [S003 pp. 2, 6–11]; per-residual models with the storage cost named "the essential cost of exploiting the structure" [S023 pp. 2, 5, 17]; closed-form subproblems at gradient cost [S010 pp. 5–6; S005 pp. 1–3, 21]; exact block solves [S011 pp. 3–4, 12]; closed-form rank-two coordinate steps [S049 pp. 5–9]; φ kept exact while only f is sampled [S098 pp. 2, 4, 7; S068 pp. 1, 4]; moments computed once so iterations cost O(d²) regardless of n [S089/S106 pp. 2, 10, 13].
- **Stated** (new; SKILL.md says no statement was found): the 1997 survey names Hessian sparsity, partial separability and element models as the route to larger n, and "thinks of exploiting any structure present in the problem as efficiently as possible" [S004 p. 17]; known derivative sparsity "can be exploited trivially" [S025 p. 18]; interpolation methods "which also exploit the problem structure are recommended" [S023 p. 21]; a scope rule that row-by-row BCD works when the block subproblem is closed-form [S035 pp. 2, 21, 28].
- **Say–do update**: ⚠ → ✅ (co-authored statements 1997, 2008, 2010) [S004 p. 17; S025 p. 18; S023 p. 21].

### Heuristics and taste marks with new full-text practice

- H1 [S018 pp. 1, 6–7]; H2 [S012 pp. 8–9]; H3 [S023 pp. 2, 5, 21]; H4 [S030 pp. 3, 12; S143 pp. 4–5] (wording, §3 row 8); H5 [S006 pp. 5, 25, 32]; H6 [S043/D001 p. 3]; H7 [S041 pp. 11–12]; H8 [S088 pp. 13–19; S104 p. 21]; H9 [S010 pp. 5–6; S003 pp. 6–11]; H10 [S137 p. 3; S057 pp. 7–13; S061 p. 11; S093 pp. 17–18]; H11 [S083 pp. 16–17]; H12 [S026 pp. 4–5, 15–16; D001 pp. 4–5, 26, where ε'_f = 0 performs badly].
- Taste mark 5 (minimal safeguard + negative result): [S143 pp. 4–5; S030 pp. 8–15; S046 pp. 3–4; S021 pp. 10–11; S054 p. 22; S088 Thm 4.6].
- Taste mark 7 (guarantees get stronger): almost sure [S018 pp. 10–11; S012 p. 25] → expected [S014 p. 13; S013 pp. 5–10] → high probability [S043/D001 pp. 7–13; S041 pp. 16–21] → total sample complexity [S057 pp. 12–13] → heavy tails and corrupted inputs [S083 pp. 16–17].
- Warning sign 2 (unbiasedness assumed for biased estimators): biased computation-failure noise makes Monte-Carlo averaging "not a correct approach" [S012 p. 26].
- Signature Work (STORM): origin is stated, not inferred: BSV assumed exact function values [S012 p. 8], assumptions inspired by an early version of Billups–Larson [S012 p. 5]; abandoned paths: the η₂ restriction and the 1/δ⁴ sampling rate are dropped in the implementation (≈1/δ_k chosen after testing) [S012 pp. 21, 28, 30].
- Inner tension "disciplines and vindicates practice": stated [S143 pp. 4–5] and practised within one paper [S030 pp. 4, 18].

---

## 3. Variants and contradictions

The full texts win over search snippets. Rows 1–10 change what SKILL.md says; rows 11–18 add a variant note without changing the claim.

| # | SKILL.md claim | What the full texts show | Cards | Change |
|---|---|---|---|---|
| 1 | M3 steps 1–3: potential Φ_k combining f and the step parameter, supermartingale / stopping time | That is one of three templates. (a) Joint potential + renewal-reward stopping time, expected bounds [S013 pp. 5–10; S015 pp. 8, 11; S047 pp. 4–8; S098 pp. 11–20]. (b) Counting on true/false × successful/unsuccessful × step above/below a threshold, with E[Σ W_k I_k] ≥ p E[Σ W_k], constant 2p/(2p−1)² [S014 pp. 8–13; S026 pp. 8–13; S068 pp. 7–9; S088 Thm 6.13; S104 Thm 5.12]. (c) High-probability: progress measure Z_k alone, deterministic counting lemma, Azuma–Hoeffding on Σ I_k − pt, Bernstein on accumulated damage, no joint potential or supermartingale [D001 pp. 7–13; S041 pp. 16–21; S083 pp. 11–15]. | S013, S015, S047, S098, S014, S026, S068, S088, S104, S043/D001, S041, S083 | Rewrite steps 1–3 as a choice among (a)/(b)/(c); drop the "reconstructed" limitation |
| 2 | M1 "occasional arbitrary failures (probability 1−p) are tolerated" | Holds for model/gradient failures in first-order trust region because an accepted step is bounded by δ_k [S013 p. 17; S012 pp. 8–9]. Second-order TR needs a first-moment bound E\|F − f\| ≤ κ_F δ_k³ (bad cases raise f by O(δ²), good steps gain O(δ³)) [S013 pp. 27–28]; line search needs a variance condition on function estimates [S015 pp. 5–7, 14]; the high-probability step search uses a mean bound plus a subexponential tail for zeroth-order errors [D001 pp. 1–5, 15]; heavy tails need q-th moments [S083 pp. 16–17]. | S012, S013, S015, S043/D001, S083 | Restrict "arbitrary failures" to gradient/model oracles; function-estimate failures need moment bounds |
| 3 | M1 step 5 "p above 1/2-type thresholds"; Signature Work STORM | STORM's almost-sure theorem needs α, β close to 1: with textbook constants (1−α)(1−β) ≤ 1/440; αβ ≥ 1/2 suffices only for the liminf step [S012 pp. 20–22]; experiments succeed at α ≈ 0.27 [S012 p. 31]. The stochastic line search requires p_g ≥ 16/17 and p_f depending on κ_g [S015 pp. 7, 16]. Thresholds can go below 1/2 with an asymmetric step update, p > 1/(m+1) [S083 pp. 15, 22]; the high-probability step search needs p > 1/2 + r/h(ᾱ) [D001 p. 15]. | S012, S015, S083, S043/D001 | State thresholds per paper; add the α,β ≈ 1 caveat to the STORM anatomy |
| 4 | M2 and Taste mark 3 ("classical adaptive methods are analysed, not replaced") as general | The SARAH line introduces a new estimator with a constant, tuned step [S002 pp. 2–3, 7; S024 pp. 3, 8]; the SGD/Hogwild! and "when does SG work" papers analyse practitioner methods unchanged but with prescribed, non-adaptive schedules [S009 pp. 3, 5; S032 pp. 6–8; S063 pp. 2, 5]; LHAC replaces the practical line search with an analysable prox-parameter update, with an ablation showing no loss [S029 pp. 10, 18, 25, 27; S084 pp. 2–4]. | S002, S024, S009, S032, S063, S029, S084 | Scope M2 and Taste 3 to the adaptive / DFO / classical-algorithm line; mention the SG line as a parallel programme outside the lens |
| 5 | M6 say–do ⚠ "explicit statement not found" | Three co-authored statements [S004 p. 17; S025 p. 18; S023 p. 21] | S004, S025, S023 | ⚠ → ✅ |
| 6 | M4 Stated / Taste mark 5: the Optima 79 essay "builds on Moré–Wild" and argues "only minimal quality controls" (search summary) | Both items come from Jorge Nocedal's discussion column in the same issue (p. 6); Moré–Wild is not in her reference list; her own statement is the p. 4 sentence quoted in §2 M4. Title verified: "Geometry in model-based algorithms for derivative-free unconstrained optimization", May 2009. She was co-editor of Optima with Caprara under editor Lodi (p. 10). | S143 (full card, pp. 4, 5–6, 10) | Replace the Stated line; fix the Appendix and Honest Boundary "title not retrieved"; "editor of Optima" → co-editor |
| 7 | M4 "the same position was held for 17 years" | Geometry-as-certificate is present in 1997 [S008 pp. 14–17; S004 pp. 8–9, 17], but in 2008 the stated practical position was to "maintain well-poisedness throughout the algorithm, not just when it is necessary to pass the criterion needed for the convergence proof" [S016 p. 18]. The minimal-safeguard stance dates from 2009–2010 [S143 p. 4; S030 pp. 3, 12]. | S004, S008, S016, S143, S030 | Date the minimal-safeguard position to 2009–2010 |
| 8 | H4 "confine them to the final stage" | S030's own phrase is "the final stage of the algorithm where criticality of a putative stationary point is verified" [S030 p. 3]; the operational rule is "only when the model gradient becomes small" [S143 p. 4; S046 pp. 3–4]. | S030, S143, S046 | Reword H4 and M4 step 3 as "confine them to the criticality step" |
| 9 | Taste mark 4 "A guarantee comes with numbers" as a general mark | Pure-analysis papers have no numerical section: [S014 pp. 1–34], [S015 v1 pp. 1–26], [S026 pp. 3, 28], [S030 p. 4] (objective stated as understanding), [S037 pp. 1–19], [S083 pp. 1–23], [S088 p. 19], [S061 pp. 1–11], [S093 pp. 1–21]. Algorithm and software papers pair theory with numbers [S012 pp. 27–32; S006 pp. 25–31; S033 pp. 25–26; S041 pp. 30–36; S098 pp. 23–28; S104 pp. 26–30]. ML-side papers give numbers without a new guarantee [S022 p. 19; S021 pp. 14, 25–27; S089/S106 pp. 4–7, 15]. | as listed | Rewrite: algorithm/software papers come with numbers; analysis papers are theory-only and leave numerics to companion papers |
| 10 | M3 Stated: "Scheinberg–Xie 2023 (as in the deterministic case, SARC outperforms other stochastic adaptive methods)" | The superiority is a statement about complexity order (O(ε^{-3/2}) vs O(ε^{-2})); S061 and S093 have no numerical section [S061 pp. 1, 3, 9–11; S093 pp. 1, 3]. | S061, S093 | Cite it as a stated parity/order claim, not as empirical evidence |
| 11 | M1 accuracy "relative to the current step or radius" | The FoCM comparison uses the norm condition relative to ‖∇φ‖ and cites the step-scaled form as the alternative [S006 p. 4]; some methods use iteration-indexed schedules instead of a fixed-probability contract [S029 p. 18; S054 pp. 11–14; S068 pp. 4, 11, 13, 20]; the first-order oracle has three regimes (floor ε_g, step-scaled κα‖g‖, cap τ‖g‖) [D001 pp. 1–5]. | S006, S029, S054, S068, S043/D001 | Variant note |
| 12 | M1 (new variant) | Function-estimate contract written on the reduction difference \|ared − cred\| ≤ η·pred_k; with common random numbers O(Δ^{-2}) samples suffice instead of O(Δ^{-4}) [S098 pp. 3, 7, 9, 21–23]; optional difference-moment assumption [S083 p. 3]. | S098, S083 | Variant note (M1 step 4) |
| 13 | M1 (new variant) | Every sample-size rule is stated in quantities the algorithm knows (α_k, ‖g_k‖, Δ_k, variance bounds), and competitors needing ‖∇f(x_k)‖ or ε are criticised [S015 pp. 2, 7; S013 pp. 19–20; S047 p. 9]; the theory uses oracle constants the method never sees, only an upper bound ε'_f enters [S043 p. 4]; unknown constants handled by a parameter that only decreases when a checkable test fails [S014 pp. 29–31]. | S013, S014, S015, S043, S047 | Add to M1 step 2: write the contract in knowable quantities |
| 14 | Taste mark 2 (deterministic parity) | For sample complexity the yardstick becomes the stochastic lower bound and SGD rates [S057 pp. 2, 15–16, 19]; for comparison oracles, matching minimax lower bounds [S087 pp. 23–26, 41–43]; the shuffling method matches GD's O(1/T), not NAG's [S055 pp. 2, 5]. | S057, S087, S055 | Variant note |
| 15 | Warning sign 1 (hand-tuned step schedule) | The group's own SGD analyses use pre-specified schedules computed from known μ and L [S009 pp. 2, 5, 13]. | S009 | Variant note: the warning is about hand tuning where an adaptive method would do |
| 16 | M5 steps 4–5 (same outer method, count evaluations) | The FoCM protocol picks the best of 17 variants per estimator and tunes constant-step variants, and plots RL runs per iteration over 3 seeds [S006 pp. 30, 33, 42; D003 pp. 11–12]; outside DFO the unit is the dominant cost (Aprods, matvecs, inner products, passes, flops, QP solves) [S011 pp. 13–15; S028 p. 17; D001 p. 27; S100 pp. 10–11; S066 p. 25]; some estimator comparisons are by derived complexity only [S088 pp. 6, 11; S087 pp. 17–18]. | S006, D003, S011, S028, S043/D001, S100, S066, S088, S087 | Variant note |
| 17 | M5 as a general practice (the two ✗ cards) | Applied and ML papers follow their field's conventions: naive or persistence baselines on one competition zone [S082 pp. 4–6], stronger baselines in the follow-up [S051 pp. 5–7]; test accuracy and CPU time with per-method tuning [S089/S106 pp. 11, 13–14]. | S082, S051, S089/S106 | Scope M5 to the DFO / estimator line |
| 18 | Roundtable blind spots "nonsmooth", "integer or categorical" | Nonsmooth composite f + φ with known prox is handled [S098 pp. 2–4]; a function-free comparison-oracle framework exists [S087 pp. 2–3, 10–11]; categorical data enter through an exact MILP formulation, not a black box [S017 pp. 3, 7–16]; integer hyperparameters are encoded for a continuous DFO solver without theory [S056 p. 8]. | S098, S087, S017, S056 | Narrow the wording: black-box nonsmooth and integer DFO remain blind spots |

**Authorship fix.** ProxSTORM (arXiv 2510.03187) has Scheinberg as an author [S098 coauthors; S107 same text]. SKILL.md Signature Work (STORM) "Reception" calls it a third-party extension with authors unverified, and `open-problems.md` row 6 lists it as third-party. Both should say it is her paper with Baraldi, Javeed and Kouri (Sandia). Row 6's premise ("the verified analysis … is convex-composite only") is also out of date: ProxSTORM covers nonconvex smooth f plus convex φ with expected O(ε^{-2}) complexity [S098 pp. 11–20]; what remains open there is the high-probability bound and the total sample complexity, which the paper delegates [S098 pp. 9, 17–20, 23].

**Honest Boundary items resolved.** "No full text was read" (78 now read); "experiment conventions unverified" (verified, §2 M5); "Optima 79 title not retrieved" (verified, row 6); "Method 6 practised but not found stated" (row 5).

---

## 4. Promotions

The skill has six core methods, so one promotion fits under the 3–7 cap without replacing a method. One cluster passes all four checks and is not already covered by an existing method.

### Promote → Method 7: Prove it once for an abstract object, then instantiate by checklist

**Cluster** (21 distinct full/partial papers, 1997–2026). Proposed as a new pattern by 15 cards [S004 pp. 8–16; S008 p. 13; S007 pp. 7–13; S011 pp. 9–10; S048 p. 12; S049 p. 9; S035 pp. 19, 23; S014 pp. 3, 8, 13–26; S013 pp. 4, 14–19, 26–33; S015 pp. 7–8, 11; S061 pp. 8, 10–11; S043/D001 pp. 7, 10–23; S057 pp. 7, 13–19; S083 pp. 12, 18–21; S093 p. 10] and used by 6 more [S143 p. 3; S047 pp. 3–8; S098 Thm 21 pp. 19–20; S068 Thm 1 pp. 7–9; S088 Thm 6.13; S104 Thm 5.12]. Abstract-level support: S062, S108, S111, S112.

| Check | Result | Evidence |
|---|---|---|
| 1 Cross-project recurrence | ✅ | DFO model-quality abstraction: undefined "adequate geometry" predicates realised later [S004 pp. 8–16]; "no need to specify exactly how this is done for the purpose of our theory" [S008 p. 13]; fully linear class proved once, interpolation and regression shown to be members [S007 pp. 7–13]. First-order: convergence by embedding new steps into Tseng–Yun BCGD [S011 pp. 9–10], into barrier/AL theory [S048 pp. 7–8, 12]. Stochastic: one process theorem instantiated for steepest descent, convex, strongly convex and ARC [S014 pp. 16–26]; renewal-reward theorem instantiated for first- and second-order STORM [S013 pp. 14–19, 26–32] and imported verbatim by the line search [S015 pp. 7–8, 11]; axioms (i)–(v) proved once and instantiated per function class [D001 pp. 7, 10–23]; one step-parameter assumption instantiated for STORM and SASS [S057 pp. 7, 13–19]; one framework verified for TR and LS [S083 pp. 12, 18–21]. |
| 2 Say–do consistency | ✅ | Stated in text: [S008 p. 13] (quote above); analysis "independent of the sampling techniques" [S007 p. 1]; the framework "can be applied beyond the algorithms discussed in this paper" [S013 p. 33]; "the analysis is structured around a measure in which progress is made in all iterations" [S047 p. 3] in a paper titled as a framework [S047]; "A unified framework for high-probability complexity analysis" (title) [S083]; the framework's scope fenced explicitly [S057 p. 2]. Abstract-level: NSF award titled "A Unified Framework for Analyzing Adaptive Stochastic Optimization Methods Based on Probabilistic Oracles" [S108]; talk "Complexity analysis framework of adaptive optimization methods via martingales" [S112]. |
| 3 Executable, different from standard practice | ✅ | Steps below. Standard practice proves each algorithm separately and re-proves for each variant; here the abstract object is the deliverable, and later papers are written as hypothesis checklists that import the bound [S093 Thm 2–3 p. 10; S061 p. 10; S098 Thm 21 pp. 19–20]. |
| 4 Exclusivity | ✅ | The abstractions are reused as named tools across a decade and across groups: the BCMS19 stopping-time theorem is imported by the Sandia collaboration [S098 pp. 19–20]; the Cartis–Scheinberg 2018 counting lemmas are reused in composite, DFO and Powell-style papers [S068 pp. 7–9; S088 Thm 6.13; S104 Thm 5.12]; JSX24's process is imported by stochastic ARC [S093 p. 10]. In DFO the same move gives a class-level analysis "independent of the sampling techniques" [S007 p. 1], built to cover practical codes that had no convergence theory [S007 p. 2]. |

**Draft for SKILL.md** (for the SKILL.md editor; not applied here):

- **One line**: After the first proof, extract the few properties it actually used, state them as axioms on an abstract model class or iteration process, prove the theorem once, and certify every later algorithm by checking the axioms.
- **Steps**:
  1. Prove one concrete algorithm first. Mark every property of the iteration the proof used (the deterministic DFO theory lists the three places the standard proof breaks [S008 pp. 17–18]; the process axioms list what a true, successful iteration must deliver [S014 p. 8]).
  2. Turn those properties into a short axiom list on an abstract object: a model class (fully linear: error ≤ κΔ on the ball plus a finite certify-or-repair procedure) [S007 pp. 7–8; S143 p. 3], or a process (true and successful ⇒ progress h(α); α ≤ C and true ⇒ successful; progress monotone) [S014 p. 8; D001 p. 7].
  3. Prove the theorem for the abstract object, with all problem dependence carried by a few instantiation quantities (C, h, F_ε; Z_k, h, r) [S014 p. 13; D001 Table 1 p. 6].
  4. Instantiate per algorithm and per function class by computing only those quantities [S014 pp. 16–26; S057 pp. 13–19; S083 pp. 18–21].
  5. For a new algorithm, write a hypothesis-checklist theorem, one line of gloss per axiom, and import the published bound unchanged [S093 p. 10; S061 p. 10; D001 p. 7].
  6. Fence the abstraction: list its impractical members and the neighbouring methods it does not cover [S007 p. 8; S057 p. 2; S047 p. 12].
- **Different from standard practice**: a new variant costs a checklist, not a new proof [S093 p. 10; S098 pp. 19–20], and the abstraction outlives the paper that introduced it [S013 p. 33; S068 pp. 7–9; S104 Thm 5.12].
- **Limitations**: abstractions admit impractical members [S007 p. 8]; constants are worst case and large [S013 p. 16; S012 pp. 20–21]; methods with different step dynamics or measurability fall outside [S057 p. 2; S047 p. 12].
- **Why not merged into M3**: M3 concerns the stochastic-process analysis and the deterministic-order yardstick. This method also covers the deterministic DFO theory of 1997–2009 [S004; S008; S007; S143] and first-order embeddings [S011; S048], and it explains why the papers come in families that import each other's theorems [S015; S061; S093; S098; S068; S088; S104]. It changes what a student does first ("is there a framework whose hypotheses my algorithm satisfies?"), which M3 does not.

With Method 7 the skill is at the 7-method cap. Any later promotion must merge into or replace a method. The closest runner-up, "knowable-quantity accuracy requirements" [S013 pp. 19–20; S015 pp. 2, 7; S047 p. 9], passes all four checks but is folded into M1 (§10, item 3).

---

## 5. New heuristics

Clusters that are executable and pass at least one more check. "Recommend" = add to SKILL.md; "fold" = add as a step of an existing method or workflow instead (no new list item); "hold" = qualifies but adds little to this lens. SKILL.md already has 12 heuristics, above the framework's 5–10, so only four new items are recommended; merging H1 with H2 (two cases of the oracle contract) and H6 with H10 (two cases of strengthening the guarantee) would keep the list short.

| Cluster | Papers | Recurrence | Say–do | Executable & different | Exclusivity | Decision |
|---|---|---|---|---|---|---|
| Measure the theorem, disclose the gap | 12 (H13 below) | ✅ | — | ✅ | ✅ | **Recommend (H13)** |
| Name the blocker when an extension fails | 4 (+ S044 abstract) (H14 below) | ✅ | — | ✅ | ✅ | **Recommend (H14)** |
| Turn the bound's parameter dependence into a design rule | 8 (H15 below) | ✅ | — | ✅ | ✅ | **Recommend (H15)** |
| Pair each upper bound with a tightness construction | 4 (H16 below) | ✅ | — | ✅ | ✅ | **Recommend (H16)** |
| Report what did not work | 13: S022, S011, S089, S035, S005, S036, S098, S104, S017, S078, S074, S024, S066 | ✅ | — | ✅ | partial | Fold into M5 step 5 and Workflow D |
| Counterexample placed before each safeguard | 14: S004, S003, S019, S025, S050, S058, S048, S143, S030, S028, S036, S054, S021, S031 | ✅ | ✅ [S143 p. 4; S046 pp. 3–4] | ✅ | partial | Fold into M2 step 4 (already covers it; add the "smallest instance" detail) |
| Assumption audit before relaxing an assumption | 5: S009 p. 2, S032 p. 3, S036 p. 4, S037 p. 3, S066 p. 8 | ✅ (one group) | — | ✅ | partial | Fold into Workflow E step 1 |
| Compete on constants and assumptions when the order ties | 8: S029 pp. 9–12, S002 p. 6, S024 p. 2, S005 pp. 11, 16, S011 pp. 7–9, S037 p. 4, S055 p. 3, S031 p. 13 | ✅ | — | ✅ | — | Fold into Workflow C step 4 |
| Error-sensitive step only where the estimate is trusted | 3 (partial reads): S036 pp. 4–5, S037 p. 4, S055 pp. 3–4 | ✅ | — | ✅ | — | Hold |
| Smooth true target via its expectation under a data model | 6: S052 pp. 4–5, S078 pp. 4–5, S089 pp. 5–7, S060 p. 5, S051 p. 4, S074 p. 2 | ✅ | — | ✅ | — | Hold (applied ML, outside the DFO lens) |
| Validate against an independent ground truth / known optimum | 4: S094 p. 7, S073 pp. 8–9, S102 pp. 1–2, S049 pp. 12–13 | ✅ | — | ✅ | — | Hold (applied) |
| Spin off the enabling lemma as its own paper | 3: S053 pp. 1, 5, S137 pp. 1, 3, S005 pp. 8, 25–26 | ✅ | — | ✅ | — | Hold (publication tactics) |
| Cheap practical test with fallback to the analysable step | 3 (2 projects): S008 p. 11, S010 p. 4, S005 pp. 7–8 | ✅ | — | ✅ | — | Hold (a device; see §7.2 A14) |
| Open with a toy or two-regime example | 5: S063 pp. 2–3, S055 p. 4, S002 p. 4, S021 pp. 8–9, S009 p. 7 | ✅ | — | ✅ | — | Hold (writing move, §7.4 W15) |

**H13 · If** your theorem has a threshold or constant (minimum success probability, noise floor, sample count), **then** compute it on a toy instance, run experiments across it (including an adversarial oracle that stays inside the contract), and list every place the implementation departs from the assumptions.
Cases: theory-threshold sweep, theory needs (1 − σ) > 0.999 at n = 10 yet 100% success at 0.998 [S012 pp. 30–32]; adversarial oracle with Bernoulli(p) good flags, plateaus compared with the noise floor [S041 pp. 30–33]; weak necessity bound followed by a 10,000-run simulation of the true threshold [S006 pp. 16–18]; the assumption itself measured on standard data [S063 pp. 8–11; S089 pp. 5, 8–9]; a competitor that violates the assumption included to show what it buys [S137 p. 6]; zero-slack ablation [D001 p. 26]; disclosed parameter gaps and deviation lists [S010 pp. 5–7; S005 pp. 18, 23; S033 pp. 6, 21; S098 p. 24; S104 p. 27]; textbook constants plugged in to show their size [S012 Remark 4.13 pp. 20–21].

**H14 · If** a natural extension of your result fails, **then** state it as a conjecture or open problem and name the exact inequality or technical obstacle that breaks.
Cases: lim-type second-order result left as Conjecture 5.1, with Σδ² vs Σδ named as the failing step [S018 pp. 20–21]; stochastic cubic regularization blocked because T_ε defined through x_{k+1} is not a stopping time [S047 p. 12]; order mismatch (O(δ²) damage vs O(δ³) gain) diagnosed and repaired with a moment assumption [S013 p. 28]; certifying Powell-like geometry left as future study [S016 p. 24] and later solved [S104 pp. 1–2, 10–23].

**H15 · If** your bound depends on a parameter you choose, **then** make that dependence the algorithm's default rule.
Cases: raise the step-decrease factor γ when the oracle reliability p is low [S137 pp. 4–5; S057 p. 9]; choose γ_inc > γ_dec so that p < 1/2 is tolerated [S083 pp. 15, 22]; η₂ = √n improves n² to n^{3/2} [S104 pp. 7–8]; the number of inner passes follows from the inner solver's rate [S029 pp. 20–21; S054 pp. 11–12]; the proof's contracting quantity becomes the inner-loop stopping test [S002 pp. 4, 7; S024 p. 7].

**H16 · If** you prove an upper bound, **then** pair it with a construction that attains it or with a lower bound; if the lower bound is weak, simulate the extremal instance.
Cases: Sherman–Morrison family of poised sets showing the poisedness dependence is tight [S088 Thm 4.6]; lower bounds for both the direction estimator and the outer method [S087 pp. 23–26, 41–43]; necessity bound plus simulation [S006 pp. 16–18]; tightness of the step-size lower bound via the q^l term [S137 p. 5].

---

## 6. Candidate pool (not promoted)

| Candidate | Papers (count) | Why it stays in the pool |
|---|---|---|
| Stability as uniform boundedness in the limit (smallest-bad-index contradiction) | S050, S058 (2) + S077 abstract | One project (IPM linear algebra); a proof device, listed in §7.1 P27 |
| Extend own result to a harder class and list what breaks | S058, S008 (2) + S077 abstract | Already M2 step 2 ("mark the first inequality that fails") |
| Organize a survey by the user's problem features | S046 (1) + S090, S001 abstract; S133 substitute p. 1 | One full text |
| Fidelity knob tied to predicted decrease vs noise | S085, S094 (2) | One collaboration; S094 drops the adaptive rule for offline calibration [S094 pp. 4–5] |
| Noise-floor exponent as a comparison axis | S061, S093 (2) | One project (conference + journal) |
| Homotopy / solver path as a selection device | S021, S059, S049 (3) | Fails exclusivity (standard continuation) |
| Deterministic framework first (rewrite the deterministic proof in the stochastic proof's format) | S047, S068, S055, S028 (4) | Folded into M2 step 2 as a variant (§10) |
| Oracle-side fix for an algorithm-side safeguard (τ cap removes α_max) | S043/D001 (1) | Single paper |
| Keep safeguard iterations randomness-free | S088 (1) | Single paper |
| Avoid verify-until-pass loops under probabilistic oracles | S098 (1) | Single paper |
| Relax one oracle at a time | S068 (1) | Single paper; trajectory evidence for Taste mark 7 |
| Import a classical probability result via a probabilist collaborator | S057 (1) | Single paper; collaboration note (§9) |
| Invariance-first formulation; two-case guarantee | S087 (1 each) | Single paper, 2026 |
| Local upper bound plus global SOS lower-bound certificate | S066 (1) | Single paper |
| Least-squares residual reformulation with graceful infeasibility | S021 (1) | Single paper |
| Reparameterize along the path to the optimum | S073 (1) | Single paper |
| Formulation engineering for exact MILP training | S017 (1) | Single paper |
| Analysis-only trade-off knob (γ trades δ against the neighbourhood) | S026 (1) | Single paper |
| Method-agnostic guarantee for an approximation step | S003 (1) | Single paper |
| Constraint taxonomy by information and cost | S019 (1), S133 substitute | M6 evidence, not a separate pattern |
| LP-to-conic transplant | S039, S027, S040 (abstract/metadata only) | Below the read threshold |
| Cross-community synthesis of one object | S081 (abstract) | Abstract only |

---

## 7. Technique inventory

Named devices with the paper and page where they are used, for `proof-playbook.md` and student use.

### 7.1 Proof devices

| # | Device | Where |
|---|---|---|
| P1 | Interpolation error bound: subtract interpolation equations from Taylor expansions, cancel the unknown function error via the centre point, invert an x-independent scaled matrix | S072 p. 8; S016 pp. 12–17 |
| P2 | Function-error to gradient-error transfer by Taylor with h = δ(∇f − g)/‖∇f − g‖ | S008 pp. 12–13 |
| P3 | Norm equivalence max_{B(1)}\|vᵀφ(x)\| ≥ σ‖v‖ after scaling to the unit ball, constants computed by restricting to one or two variables | S016 pp. 8–10; S025 pp. 11–13; S072 pp. 17–18 |
| P4 | Greedy argmax / threshold-pivoting construction of a well-poised set, with a lemma that a replacement point always exists | S008 pp. 10–11; S016 pp. 19–23; S072 pp. 28–29 |
| P5 | Small-ball accuracy implies larger-ball accuracy with the same constants (integral mean value) | S007 pp. 9–10 |
| P6 | Volume / determinant potential for finitely many geometry swaps; orthogonal-set growth (3n); Hadamard volume ratio (O(p log p)); −log\|det Y\| contracts by (1 − 1/n) | S030 p. 6; S088 Thms 3.6, 5.1; S104 pp. 13–14 |
| P7 | Self-correction: failed step + error bound + Σℓ_j = 1 ⇒ an improving swap exists | S030 pp. 14–15; S143 p. 4 |
| P8 | Trust-region skeleton: criticality loop finite; radius bounded below away from criticality; key lemma \|ρ − 1\| ≤ model error / predicted decrease ⇒ success once Δ ≤ c‖g‖ | S008 pp. 16–19; S007 pp. 15–18; S023 pp. 13–15; S088 Lemmas 2.4–2.8; S104 pp. 5–6 |
| P9 | Acceptance test ‖g_k‖ ≥ η₂Δ_k replacing the criticality step | S018 p. 8; S013 pp. 10, 12; S088 pp. 2–3; S104 p. 4 |
| P10 | Realization-wise lemma (Δ_k → 0 on every path) plus a ±1 submartingale bounding log Δ_k from below | S018 pp. 8–11; S012 pp. 21–22; S098 Thm 19 |
| P11 | Potential νf + (1 − ν)Δ^q (q = order of per-step decrease) with a case grid (‖∇f‖ ≥ ζδ_k or not) × (I_k, J_k); worst case offset by the best case of weight αβ | S012 pp. 14–20; S013 pp. 14–18; S015 p. 11; S047 pp. 4–6, 10; S098 pp. 13–15 |
| P12 | Renewal-reward / birth–death stopping time E[T] ≤ p/(2p − 1)·Φ₀/(Θh(Δ_ε)) + 1, Wald's identity without assuming T < ∞ | S013 pp. 5–9; S047 p. 8; S098 pp. 19–20 |
| P13 | Counting lemmas over true/false × successful/unsuccessful × step above/below C, with E[Σ W_k I_k] ≥ p E[Σ W_k] for past-measurable W_k | S014 pp. 8–13; S026 pp. 8–13; S068 pp. 7–9 |
| P14 | High-probability template: deterministic "not stopped + enough true iterations ⇒ enough good iterations" lemma, Azuma–Hoeffding on Σ I_k − pt, Bernstein on summed damage via conditional MGFs; random radius threshold from the minimum gradient norm; Fuk–Nagaev for q-th moments | D001 pp. 7–13; S041 pp. 16–23; S083 pp. 14–17 |
| P15 | Hypothesis-checklist theorem importing a published tail bound | S061 p. 10; S093 p. 10; S015 pp. 7–8 |
| P16 | Step-parameter lower bound: couple log α_k with a reflected random walk, bound its maximum from the explicit spectrum, level l ≈ log n; layer-cake total cost | S137 pp. 8–9; S057 pp. 9–13; S093 pp. 17–18 |
| P17 | Noise slack r = 2ε_f; damage r(ε_f)/h(ᾱ) ≤ γ < 1 fixes the neighbourhood | S026 pp. 7, 15–17; D003 pp. 3–4; S041 p. 11 |
| P18 | Hölder bound E[1_bad\|err\|] ≤ P(bad)^{1/2}·(second moment)^{1/2} for rare unbounded errors | S015 p. 6 |
| P19 | Order-mismatch diagnosis (O(δ²) damage vs O(δ³) gain) ⇒ add a matching moment bound | S013 p. 28 |
| P20 | Progress measures 1/Δ, log ratio, stopped transforms with Jensen: one nonconvex inequality gives convex and strongly convex rates | S014 p. 7; S015 pp. 19–22; S026 p. 7; D001 pp. 6, 19–20 |
| P21 | Sampling radius from a·σ + b/σ; the discriminant gives the gradient-norm floor | D003 p. 7; S006 pp. 6–7; S043 p. 25 |
| P22 | Estimator variance by Gaussian moment identities + Chebyshev or matrix Bernstein; necessity via a second-moment tail lower bound on a linear test function | S006 pp. 11–21, 16–18; D003 pp. 9–10 |
| P23 | Half-step filtration F_{k−1/2}; difference-based estimate under common random numbers, Taylor + Markov ⇒ N = O(Δ^{-2}) | S098 pp. 5–6, 21–23 |
| P24 | Three-point inequality and telescoping with the count of non-skipping steps; mode-dependent potential | S010 pp. 10–11; S005 pp. 8–14 |
| P25 | FISTA potential with a varying prox parameter; μ_k t_k² ≥ (Σ√μ_i/2)² by induction | S028 pp. 6–10; S054 pp. 19–21; S068 pp. 15–17 |
| P26 | Inexact solves: error-dominated vs progress dichotomy; last-good-solve geometric weighting (2 − p)/(1 − p); error accumulation ρ^k Σ ε_i/ρ^i | S029 pp. 13–19; S054 p. 11; S068 pp. 10, 19–20 |
| P27 | Smallest-bad-index contradiction on a subsequence for uniform boundedness of factors | S050 pp. 11–14; S058 pp. 19–20 |
| P28 | Convergence by embedding each step in an existing convergent framework with an explicit parameter mapping; safeguard reinterpreted as a barrier parameter | S011 pp. 9–10; S048 pp. 7–8 |
| P29 | Second-moment bound derived from per-sample smoothness | S009 pp. 4, 10; S032 pp. 21–22; S063 p. 13 |
| P30 | Recursive-estimator MSE telescoping via conditional unbiasedness of increments | S002 pp. 5, 11; S037 p. 10; S024 pp. 12–13 |
| P31 | Random subspaces: Beta law of the Haar projection + Paley–Zygmund ⇒ alignment probability > 1/2, then the θ > 1/2 process | S088 Lemma 6.7; S104 p. 21 |
| P32 | trace(A) + trace(A⁻¹) bound giving √n instead of n; constants tracked in n | S088 Thm 4.3; S104 pp. 7–8 |
| P33 | Hand-checkable 2-D counterexample whose outcome is independent of the replacement rule | S143 pp. 4–5; S030 pp. 8–11 |
| P34 | Perturbation sandwich for an approximate QP on the same feasible set | S003 pp. 14–15 |

### 7.2 Algorithm-design moves

| # | Move | Where |
|---|---|---|
| A1 | Gate radius decrease on a model certificate | S008 p. 14; S007 pp. 13–14; S023 p. 9 |
| A2 | Recycle rejected trial points as geometry repairs before shrinking the radius | S030 p. 12; S143 pp. 4–5 |
| A3 | Certified core of n points plus a least-squares reuse pool (Y/Z split) | S104 pp. 10–12 |
| A4 | Per-residual models on a shared sample set; regime-switching Hessian (Gauss–Newton / LM / full) | S023 pp. 2, 5, 16–17 |
| A5 | Cheap constraints exact in the subproblem; hidden constraints via a failure flag, not a large value | S019 pp. 6–8; S133 p. 1 (v2.0 substitute) |
| A6 | Relaxed acceptance with 2ε_f and a radius increase gated on ‖g_k‖ ≥ η₂Δ_k | S041 p. 11; S026 pp. 4–5; S083 p. 8 |
| A7 | Second control δ_k for function-estimate variance when ‖∇f‖ is unknown | S015 pp. 3–4 |
| A8 | Fresh estimates at current and trial points each iteration; no averaging under biased failures | S012 pp. 7, 26, 28 |
| A9 | Oracle accuracy max{ε_g, min{τ, κα}‖g‖}: floor plus cap removes the step-size bound | D001 pp. 1–3 |
| A10 | Asymmetric step-size update tolerating p < 1/2 | S083 pp. 15, 22 |
| A11 | Composite problems: keep φ exact, sample only f | S098 pp. 2, 4, 7; S068 pp. 1, 4 |
| A12 | Full backtracking with θ_k coupling so the prox parameter may grow | S028 pp. 8–9; S068 pp. 14–15 |
| A13 | Replace a line search without a rate by a TR-like prox-parameter update, keep the line search as an ablation | S029 pp. 5–6, 24–25; S084 pp. 3–4 |
| A14 | Cheap practical test, fall back to the provable step (skipping step; threshold pivoting with argmax as last resort) | S010 p. 4; S005 pp. 7–8; S008 p. 11 |
| A15 | Compact L-BFGS with a cached Q̂d so coordinate steps cost O(m) | S084 p. 3; S100 p. 8 |
| A16 | Block subproblem as a trust-region subproblem (secular-equation Newton, cached eigendecomposition) | S011 pp. 3–4 |
| A17 | PSD block in BCD as a Schur-complement SOC constraint; closed-form rank-two determinant | S048 pp. 3–4; S049 pp. 7–8 |
| A18 | Adaptive sample sizes in knowable quantities with a guess-and-increase loop | S015 p. 7; S047 p. 9 |
| A19 | Powell-style model methods in Haar random subspaces | S088 pp. 13–19; S104 p. 21 |
| A20 | Hedge model switching by EWMA of prediction error | S104 pp. 25–26 |

### 7.3 Experiment protocols

| # | Protocol | Where |
|---|---|---|
| E1 | Moré–Wild set, data profiles in simplex gradients, τ = 10⁻¹…10⁻⁷, deterministic noise, tolerances matched to noise | S023 pp. 17–19; S041 pp. 33–36; S006 pp. 30–31 |
| E2 | Function-evaluation performance profiles against a Powell-family code (NEWUOA/PRIMA), same generic component given to all solvers, rotations of the initial set, failures reported | S033 pp. 25–26; S104 pp. 26–30; S012 pp. 27–29 |
| E3 | Equal-accuracy stop against a common reference, work in the dominant unit | S011 pp. 13–15; S028 p. 17; D001 p. 27; S100 pp. 10–11 |
| E4 | Estimator accuracy at points harvested from optimization trajectories, % meeting the theorem's θ < 1/2 | S006 pp. 29–30; D003 pp. 10–11 |
| E5 | Theory-threshold sweep; adversarial oracle inside the contract; simulation of the extremal instance | S012 pp. 30–32; S041 pp. 30–33; S006 pp. 16–18 |
| E6 | Estimator-agnostic outer method as a harness; equal per-iteration sample budgets | S073 pp. 6–7, 11 |
| E7 | Baseline at its best configuration, at its own and at your tolerance, memory matched, largest runs repeated independently | S003 pp. 15–17; S022 pp. 10–13, 16 |
| E8 | Baseline variant removing one assumption violation; competitor that violates your assumption | S012 p. 28; S137 p. 6 |
| E9 | Noise slack estimated from repeated oracle calls, with a zero-slack ablation | D001 p. 26 |
| E10 | 100 seeded realizations, histograms against a same-seed, work-adjusted baseline, stating where it wins | S098 p. 24 |
| E11 | Random search at 2× the budget; optimizer overhead reported separately | S052 pp. 6–7 |
| E12 | Measure the new assumption directly on standard data | S063 pp. 8–11; S089 pp. 8–9 |
| E13 | Report how often each safeguard or branch fired | S005 p. 19; S036 pp. 19–23 |
| E14 | Restarts differing only in one random initial sample, failed evaluations counted in the budget | S019 pp. 10–11 |
| E15 | Sweep multiples of a theory-prescribed parameter in a practical code | S041 pp. 33–36 |

### 7.4 Writing moves

| # | Move | Where |
|---|---|---|
| W1 | Contribution sentence "X is necessary for G; however, X is not needed unless Y" | S143 p. 4; S030 p. 4 |
| W2 | Field history along one design axis; related work as a deficit ledger; practitioners' alternatives with their failure modes | S143 pp. 1–2; S010 p. 2; S004 pp. 3–4 |
| W3 | Credit a competitor's efficiency before refuting its guarantee; concede a concurrent paper's advantage | S143 p. 4; S012 pp. 5–6 |
| W4 | State the objective as understanding when there are no experiments | S030 p. 4 |
| W5 | "Choosing constants" paragraph before the proof; constants table with one remark per constant | S013 p. 14; S098 pp. 15–16 |
| W6 | After each theorem, zero the noise and probability parameters and show the deterministic bound returns; remark comparing constants with the classical method | S026 pp. 13, 20, 22–23; S005 pp. 11, 16 |
| W7 | Complexity table with a common measure and an additional-assumption column; full comparison table in the introduction | S031 p. 13; S037 p. 4; S055 p. 3; S006 p. 5 |
| W8 | Glossary table mapping two communities' terms | S031 p. 2; S003 pp. 3–4 |
| W9 | One-line gloss after each axiom of an abstract process assumption | D001 p. 7; S093 p. 10 |
| W10 | Fence the scope: impractical members of the abstraction, methods not covered, where the method should not be used | S007 p. 8; S057 p. 2; S035 p. 2 |
| W11 | Remark mapping each algorithmic requirement to the theorem that uses it | S007 p. 21 |
| W12 | Plain-language paragraph after the key lemma; design remarks between statement and proof | S030 p. 15; S008 pp. 17, 19; S057 pp. 8–9 |
| W13 | Numbered findings, negative ones included, before the plots; 2–3 falsifiable experiment aims | S104 pp. 26–27; S029 pp. 23–24 |
| W14 | Open problems stated with the exact technical blocker | S047 p. 12; S018 pp. 20–21 |
| W15 | Open with a toy or two-regime example that shows the phenomenon before the theory | S063 pp. 2–3; S055 p. 4; S002 p. 4 |

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period (carded works with a year; full/partial reads in brackets)

| Period | Works | IPM/conic | SVM training | Model-based DFO | Structured 1st/2nd-order & sparse | SG & variance reduction | Adaptive stochastic (probabilistic oracles) | Gradient estimation / ZO | ML models & applications | DFO applications | Service |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1996–2000 | 13 | 7 [0] | 1 [0] | 5 [3] | | | | | | | |
| 2001–2005 | 8 | 3 [2] | 3 [2] | 1 [1] | | | | | | | 1 [0] |
| 2006–2010 | 24 | 1 [0] | 1 [1] | 7 [6] | 7 [3] | | | | 2 [2] | 3 [1] | 3 [1] |
| 2011–2015 | 17 | | | 3 [3] | 10 [7] | | 2 [1] | | | 2 [2] | |
| 2016–2020 | 32 | | | 2 [1] | 3 [3] | 7 [7] | 9 [5] | 1 [1] | 6 [6] | 3 [2] | 1 [0] |
| 2021–2026 | 22 | | | 2 [2] | | 2 [2] | 11 [10] | 5 [3] | 1 [1] | | 1 [0] |

Topic assignment is by card content (contribution and D1 fields); three undated records (S138, S140, S142) are excluded.

Cards per topic (all carded works; pairs filed under the first id):

- IPM/conic: S027, S034, S039, S040, S045, S050, S058, S069, S077, S091, S134
- SVM training: S003, S022, S059, S071, S097, S140
- Model-based DFO: S001, S004, S007, S008, S016, S019, S023, S025, S030, S033, S046, S053, S062, S065, S072, S088, S104, S121, S133, S143
- Structured 1st/2nd-order & sparse: S005, S010, S011, S021, S028, S029, S035, S042, S048, S049, S054, S064, S066, S079, S084, S090, S096, S100, S101, S124, S142
- SG & variance reduction: S002, S009, S024, S031, S032, S036, S037, S055, S063
- Adaptive stochastic: S012, S013, S014, S015, S018, S026, S041, S043, S047, S057, S061, S068, S083, S093, S098, S108, S111, S112, S113, S119, S120, S137
- Gradient estimation / ZO: D003, S006, S044, S073, S081, S087
- ML models & applications: S017, S020, S051, S060, S074, S078, S082, S086, S089
- DFO applications: S038, S052, S056, S085, S094, S102, S116, S128
- Service: S080, S105, S118, S126, S127, S129, S138

### 8.2 Turns

1. **Deterministic geometry → probabilistic models (2012–2014).** A rigorous theorem for random sample sets sits next to a deterministic practical code, and a stochastic trust-region framework is named as future work [S033 pp. 5–6, 21]; two years later the trust region runs on models that are fully linear only with probability ≥ 1/2 [S018 pp. 1, 6–8]. The certificate became a probability, and the algorithm stayed the same [S018 p. 1].
2. **Almost sure → expected complexity (2014–2020).** a.s. results only [S018 pp. 10–13; S012 p. 25] → hitting-time bounds with exact f [S014 p. 13] → random f and the renewal-reward framework [S013 pp. 4–10] → line search [S015 pp. 17–19] → one template [S047 pp. 7–8].
3. **Expected → high probability and total sample cost (2021–2025).** [S043/D001 pp. 7–13; S041 pp. 16–21; S137 pp. 4–5; S057 pp. 12–13] and then unreliable inputs with heavy tails [S083 pp. 16–17].
4. **Return to Powell-style DFO with complexity (2025–2026).** The open problem of certifying Powell-like geometry [S016 p. 24] and the "closest convergent relative of the practical code" framing [S143 p. 5] come back as complexity results for geometry-correcting methods and random subspaces [S088 pp. 1–3, 12–19; S104 pp. 1–2, 10–23], using the stochastic-analysis devices in the deterministic setting [S088 pp. 2–3].
5. **Parallel lines that ended.** IPM linear algebra (last read paper 2005) [S050; S058]; SVM training at IBM [S003; S059; S022]; structured first-order and sparse learning with Goldfarb, Ma, Qin, Tang, Bai (2009–2016) [S010; S005; S011; S028; S029; S054; S066]; SG/variance reduction with Nguyen and Takáč (2017–2022) [S002; S024; S009; S032; S037; S055]; student-led ML modelling (2017–2019) [S078; S089; S051; S060; S082; S074].

### 8.3 What stayed constant

- The classical trust-region / line-search skeleton, changed in one place per paper [S008 pp. 17–18; S018 p. 1; S041 pp. 11–12; S104 pp. 4, 24–25].
- Radius-scaled accuracy: κΔ on the ball in 1997–2009 [S008 pp. 11–12; S007 pp. 7–8], the same form with probability p from 2014 [S018 pp. 6–7], with irreducible floors from 2021 [S041 pp. 4–5; S083 pp. 2–5].
- Known structure kept exact: cheap constraints in 1998 [S019 pp. 6–7], φ in 2025 [S098 pp. 2, 4, 7].
- Equal-evaluation benchmarking in DFO from the first practice paper [S019 p. 10] to 2026 [S104 pp. 26–30].
- Framework-then-instantiation from the 1997 survey to the 2025 unified framework [S004 pp. 8–16; S083 pp. 12, 18–21] (Method 7).

### 8.4 Reading order the full texts support

All items below were read in full. Stage 1, DFO geometry and trust-region frameworks: S004 → S008 → S016 → S007 → S143 → S030 → S023. Stage 2, probabilistic models: S018 → S012 → S014. Stage 3, expected complexity: S013 → S015 → S047 → S026. Stage 4, high probability and sample complexity: S043/D001 → S041 → S137 → S057 → S061/S093 → S083. Stage 5, estimators: D003 → S006 → S073. Stage 6, composite, nonsmooth and new oracles: S028 → S068 → S098 → S087. Stage 7, Powell-style complexity: S088 → S104. Side reading on structured first-order methods: S005, S010, S011, S029.

### 8.5 Where the stated open problems went

| Open problem as stated | Later |
|---|---|
| Does geometry matter; "it remains to be seen" whether stronger results hold [S143 pp. 4–5]; certify Powell-like algorithms [S016 p. 24] | Complexity for Powell-style methods [S088; S104] |
| Lim-type second-order convergence with probabilistic models [S018 pp. 20–21] | Not resolved in the cards read |
| Rates for stochastic f [S014 p. 33]; tail of the complexity "will follow" [S013 p. 4] | [S013]; [S043/D001; S041] |
| Total gradient-sample complexity vs the literature [S014 p. 28] | [S057 pp. 12–13, 19] |
| Stochastic cubic regularization blocked by measurability; stochastic TRACE [S047 p. 12] | High-probability SARC [S061; S093]; TRACE not in the cards |
| Second order, unbounded Hessians, convex constraints, noisy objectives for self-correcting geometry [S030 p. 18] | Noise and subspaces [S104 pp. 21–22]; constraints not in the cards |
| Acceleration in the block framework [S011 p. 7] | Acceleration does not help proximal quasi-Newton with L-BFGS Hessians [S054 pp. 1, 22, 29] |
| High-probability bound and total sample complexity for ProxSTORM [S098 pp. 9, 23]; high-probability bound for subspace DFO [S088 p. 18; S104 p. 21] | Open |

---

## 9. Collaboration pattern

Research works only (service items, grants and talks excluded); coauthors appearing at least twice in the period.

| Period | Works | Sole-authored | Distinct coauthors | Frequent coauthors (count) |
|---|---|---|---|---|
| 1996–2000 | 13 | 3 | 8 | Conn 4, Toint 4, Goldfarb 3 |
| 2001–2005 | 7 | 0 | 4 | Fine 3, Goldfarb 3 |
| 2006–2010 | 21 | 2 | 38 | Conn 7, Rish 5, Vicente 4, H. Zhang 3, Goldfarb 3, Asadi 3, Ma 2 (plus IBM team papers) |
| 2011–2015 | 16 | 0 | 17 | Goldfarb 5, Bandeira 3, Vicente 3, Ma 2, R. Chen 2, Tang 2, Bai 2, B. Y. Chen 2 |
| 2016–2020 | 27 | 0 | 36 | L. M. Nguyen 5, Takáč 4, Ghanbari 4, Curtis 3, Menickelly 3, Hatalis/Lamadrid/Kishore 3, Cartis 2, Kalagnanam 2 |
| 2021–2026 | 20 | 1 | 20 | M. Xie 6, L. M. Nguyen 4, Berahas 3, Cao 3, Jin 3, Tran 3, Chaudhry 2 |

Overall most frequent: Goldfarb 14 (1998–2014), Conn 12 (1997–2010), Vicente 9 (2003–2017), L. M. Nguyen 9 (2017–2025), M. Xie 6 (2021–2026) [coauthor fields of the cards].

- **One senior partner per era, then a student or postdoc per line.** Conn–Toint for the first DFO code and theory [S004; S008; S019; S030], Conn–Vicente for geometry theory and the book [S072; S016; S025; S007; S001], Goldfarb from interior-point methods to first-order methods [S050; S058; S010; S005; S011; S028]; after 2012 each line is carried by students and postdocs: Tang [S084; S100; S029], Bai [S028; S066; S021], R. Chen and Menickelly [S012], Bandeira [S033; S053; S018], Ghanbari [S052; S054; S078; S089], Cao and Berahas [D003; S026; S006; S041], Jin and Xie [S043/D001; S137; S057; S061; S083; S093], Chaudhry [S088; S104].
- **Specialists brought in for one step.** Applied probability for the stopping-time framework [S013, with Blanchet]; a classical hitting-probability result whose proof is credited to J. A. Fill [S057 pp. 10, 20]; an ML zeroth-order co-author for the estimator comparisons [D003; S006, with Choromanski].
- **Industry and laboratory partners.** IBM (video retrieval, SVM training, seismic inversion, sparse inverse covariance, anomaly localization, optimal decision trees, SGD assumptions) [S020; S086; S003 p. 1; S102 p. 1; S049 p. 21; S074 p. 1; S017 p. 1; S063 header]; Goldman Sachs Asset Management [S021]; Sandia National Laboratories, who reuse the group's STORM analysis for nonsmooth problems [S098 pp. 1–7, 19–20].
- **Sole-authored work is rare and position-like**: the JMLR active-set paper [S022 p. 3], the Optima essay [S143], a position piece on randomized finite differences [S044 abstract], plus the thesis, reports and editorials [S134; S065; S091; S105; S113 metadata cards]. S022 is sole-authored; the Scholar record lists the JMLR issue editors [S022 coauthors].
- **Applied student-led papers** (wind forecasting, anomaly localization, protein alignment) use the host field's data sets and scores, and the optimization content is a smoothing, a penalty or a solver choice [S051 pp. 3–7; S060 pp. 5–9; S082 pp. 3–6; S074 pp. 2–4; S085 p. 2; S094 pp. 3–7].
- **Author order** is alphabetical in several analysis papers and not in others [coauthor fields of S013, S043, S104 vs S041, S002], so it is not evidence of who led.

---

## 10. Rejected updates

1. **"Tool transplant across fields" as a core method** (9 papers: S003, S022, S059, S100, S011, S021, S033, S121, S068). Fails exclusivity; the ML-side instances are already M2 evidence ("the method itself is not new") [S022 p. 3] and M6 evidence. Record as an M2 variant only.
2. **"Counterexample before each safeguard" as a core method** (14 papers). Already M2 step 4 and Taste mark 5; add the smallest-instance detail [S048 pp. 6–7, 10–11; S143 pp. 4–5] to step 4 instead.
3. **"Knowable-quantity accuracy requirements" as a separate method** (6 papers). Passes all four checks [S015 pp. 2, 7; S047 p. 9] but is a constraint on how the M1 contract is written; fold into M1 step 2.
4. **"Recover the known case" as a separate heuristic** (10 papers: S026, S098, S083, S014, D003, S015, S024, S002, S043/D001, S137). Already M3 step 5 and Taste mark 2; add the zero-parameter check [S026 pp. 13, 20, 22–23] to M3 step 5.
5. **"Same harness / implement inside the baseline's code" as a heuristic** (8 papers). Already M5 step 4 and M2 step 5 [S023 pp. 16–17; S073 pp. 6–7].
6. **"Explain the practitioners' anomaly" as a method** (9 papers). Already M4 plus the Inner Tension "disciplines and vindicates practice"; add the full-text sources [S143 pp. 3–5; S030 pp. 4, 18; S104 pp. 1–2].
7. **"Accuracy hierarchy across oracles" as a heuristic** (S031 p. 22; S012 p. 9; S013 p. 14). Fold into M1 step 2.
8. **"Deterministic framework first" as a heuristic** (S047 p. 3; S068 pp. 14–15; S055 pp. 4–5). Fold into M2 step 2 as "rewrite the deterministic proof in the form the stochastic proof needs".
9. **A new method for the SARAH / SGD line.** It does not share the lens (new estimators, tuned or prescribed steps) [S002 pp. 2–3, 7; S009 pp. 3, 5]; record it as scope instead (§3 row 4).
10. **Dropping "integer / nonsmooth" from the blind spots.** The texts show exact MILP training and composite nonsmooth problems with known φ, not black-box integer or nonsmooth DFO [S017 pp. 7–16; S098 pp. 2–4]; narrow the wording only.
11. **Applied-paper evidence standards as a taste claim.** Recorded only as a trajectory and collaboration note (§9) [S051 pp. 3–7; S082 pp. 3–6; S074 pp. 2–4]; it does not describe how Scheinberg's own lens works.
12. **LP-to-conic transplant** (S039, S027, S040). Abstract and metadata only.

---

## 11. Open gaps

- **The book** (S001, no open full text): the organization, the convergence analyses and the software appendix are known from the abstract only [S001 abstract card]. It is the main reference of the DFO line, so claims about its framing stay at abstract level.
- **Her own short statements**: the SIAM News essay "Knowing What to Know in Stochastic Optimization" [S113 metadata], the randomized finite-difference position piece [S044 abstract], the MOR 50th-anniversary editorial [S105 metadata] and the IISE stochastic-gradients perspective [S081 abstract] were not read. The stated side of M1 and M5 therefore rests on the tutorial, the overview and the survey chapter [S031; S047; S046] rather than on these.
- **Interior-point years** (1996–2000): only abstracts and metadata [S027; S040; S045; S034; S091; S039; S134], so the first turn (IPM → DFO) cannot be analysed from texts.
- **Original DFO code documentation**: the v1.2 manual (2000) is unreadable and the v2.0 manual (2003) stands in for it [S133 pp. 1–3]; the 2000 McMaster report is metadata only [S065].
- **Earlier versions**: the 2011 line-search and 2012 "large steps" versions of the backtracking paper are not in the corpus [S067; S101]; the published SIOPT version of the stochastic line search may add experiments that arXiv v1 lacks [S015 p. 1]; the 2025 journal version of the zero-one-loss paper was not read [S106].
- **Applied IBM work** where Scheinberg's role is not identifiable from the text or abstract [S020; S038; S128; S124].
- **Sparse Markov network line with Rish**: only S049 in full; S042, S064, S079, S096, S142 at abstract or metadata level.
- **Figures**: data-profile plots survive only as captions and prose, so the plotted curves were not checked [S023 pp. 18–20; S104 pp. 28–31].
- **Talks and group practice**: talks were skipped [INDEX.md: S092, S109, S110, S135]; no transcript, meeting record or feedback was read (and `references/sources/private/` is out of scope by rule). The Mentor Voice and the tacit-knowledge gap are unchanged.
- **Grant abstracts** describe plans and outcomes, not methods [S108; S111; S119; S120].
