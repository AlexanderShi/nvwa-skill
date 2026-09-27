# M. J. D. Powell · Deep-reading synthesis

> Date: 2026-09-27. Input: every card in `cards/` (16 batch files, 187 card entries; index in `07-paper-cards.md`). Rules applied: `references/paper-reading-card.md` §3 (conservative update: append only; existing methods get evidence first; a new method needs ≥3 distinct papers plus the four checks; reject updates without explanatory power; every claim traceable to a card) and `references/research-extraction-framework.md` §3 (four-way validation) and §11 (quality checklist). This note proposes changes; it does not edit `SKILL.md`.
>
> Citation form: `[S025 p. 11]` = card S025, page as recorded on the card (for most papers after 1997 these are DAMTP report pages, not journal pages). Counting rules: S186 is the same text as S165 and is filed under S165; S175 and S048 are one work at two stages, filed under S175; S165 repackages S148's timing table, so that table counts once as experimental evidence and S148/S165 count as one project for cross-project recurrence. R007 is the Royal Society memoir by Buhmann, Fletcher, Iserles and Toint (secondary, not Powell's words). X001 (SIAM oral history, 2005) and X002 (CIM Bulletin interview, 2003) are Powell's first-person statements and carry the *say* side of say–do. Metadata-only cards are never used as method evidence, and abstract-level links are listed separately and not used for decisions. Some cards record a reader's note about a single paper (a typo, a table that differs between two reports, the wording of an abstract relative to its proofs). These notes are not findings about the researcher. They are not used here, and the two method links that rest on them are excluded from all counts.

---

## 1. Coverage

| Item | Count | Source |
|---|---|---|
| Google Scholar rows (+ DBLP-only) | 211 (+2) = 213 records; 29 duplicates or junk | `07-paper-cards.md`, Coverage |
| Distinct works on the Scholar list | 184 (182 Scholar + D001, D002 from DBLP) | same |
| Card entries | 187 = 184 works + R007, X001, X002 | same |
| **Full text read** | **35 Scholar-list works** (30 full + 5 partial: S057, S074, S078, S121, S170) **+ 3 other documents** (R007, X001, X002) | read-level column of `07-paper-cards.md` |
| Abstract-level | 73 entries (72 works: S175 = S048) | a2-01 … a2-05 |
| Metadata-only | 75 (11 non-research items, 4 books or edited volumes) | a2-01 … a2-05 |
| Skipped | 0 (no work without a card) | INDEX.md |
| Candidate entries / distinct pattern strings | 180 / 123, clustered by meaning into 32 clusters + 17 singletons | `new_pattern_candidates` of all digests |
| Proof-device / transferable-technique entries | 232 / 246 (223 / 198 in full or partial cards) | `proof_devices`, `transferable` |

Full-text reads by five-year period (full + partial / carded research works with a year; editorial items and duplicates excluded): 1960–64 1/7; 1965–69 1/24; 1970–74 0/23; 1975–79 0/17; 1980–84 1/25; 1985–89 2/19; 1990–94 3/20; 1995–99 7/15; 2000–04 8/9; 2005–09 7/7; 2010–15 5/5. The derivative-free period after 1997 is read almost completely. For the rest, the full texts are a handful of classics: DFP 1963 [S001], the Harwell hybrid-method report of 1968 [S019], the ICM rate paper of 1983 [S139], the RQP paper of 1986 [S050], the Karmarkar report of 1989 [S115], the equality-constrained trust region paper of 1990/91 [S030], and the RBF reports of 1989–92 [S090, S089]. No full text exists for 1969–1982. COBYLA [S008], TOLMIN [S040, S071], the 1970 dogleg and trust-region papers [S011, S015], the 1978 SQP papers [S003, S013, S016] and the 1969 augmented Lagrangian [S004] are known only from abstracts or metadata, from Powell's own surveys [S014, S029, S137] and from the memoir [R007]. No method evidence below rests on those cards.

---

## 2. Evidence per existing method

Counts are distinct full or partial works (duplicates merged) whose cards link to the method. A work can give both evidence and a variant.

| Method | Evidence ✅ | Variant ⚠ | Contradiction ✗ | Distinct works touching it | Includes stated / secondary sources | Abstract-level links (not used) |
|---|---|---|---|---|---|---|
| M1 Relax one limitation per solver | 23 | 5 | 0 | 27 | X002; R007 | 3 ✅, 6 ⚠ |
| M2 Two-radius discipline (RHO vs DELTA) | 11 | 10 | 1 (partial) [S025] | 18 | R007 | 2 ✅, 1 ⚠ |
| M3 Fewer evaluations than model parameters | 14 | 8 | 0 | 20 | R007 | 1 ✅, 3 ⚠ |
| M4 Cost and rounding error as part of the algorithm | 31 | 2 | 0 | 31 | X002; R007 | 17 ✅ |
| M5 Experiment-first validation with honest scope | 22 | 14 | 1 [S030] | 34 | X001, X002; R007 | 12 ✅, 4 ⚠ |
| M6 Ship free, self-checking code | 14 | 3 | 0 | 17 | X001, X002; R007 | 4 ✅, 1 ⚠ |

All six methods survive the full texts, and each now rests on Powell's own papers rather than on release notes alone. The ✗ links do not overturn a method: S025's corrects a Limitations line of M2, and S030's limits the scope of M5 (§3, rows 1 and 12).

### M1 · Relax one limitation per solver

- **Strongest practice**:
  - One framework with four model spaces, each judged by its limitation, after which §5 removes the one that remains [S047 pp. 3–12, 17–21].
  - UOBYQA's outer loop is kept and only the tests that relied on an exact model are rewritten [S072 pp. 7–9].
  - One numbered flowchart is shared with UOBYQA [S018 pp. 3, 5].
  - BOBYQA copies NEWUOA and changes only what bounds require [S036 p. 7; S007 pp. 3, 27–29, 32].
  - One change (θ) is made inside otherwise unchanged BOBYQA machinery [S108 p. 4].
  - LINCOA adds active sets and reuses TOLMIN's near-active device [S067 pp. 4, 9, 16].
  - The three stages UOBYQA → 2003 prototype → NEWUOA each remove one measured problem [S124 pp. 22–24].
- **Before DFO**:
  - Davidon's method simplified at two named points [S001 pp. 1, 3].
  - Newton kept, its singular-Jacobian failure removed [S019 pp. 5–7].
  - Only the second-derivative dependence of Fletcher's penalty removed [S050 pp. 1–3].
  - Only the globalization changed, from line search to trust region [S030 pp. 2–5].
  - The augmented Lagrangian and SQP as one-lever changes [R007 pp. 7, 14].
- **Interface continuity** is older than the SKILL says. NS01A(N, X, F, AJINV, DSTEP, DMAX, ACC, MAXFUN, IPRINT, W) with a user routine CALFUN already had the 1992–2013 calling pattern in 1968 [S019 pp. 10, 12].
- **Stated**:
  - The history of the field is written as a chain in which each method removes a named disadvantage of its predecessor [S137 pp. 4, 9, 11, 14, 16].
  - The DFO lineage is explained limitation by limitation [S029 pp. 3–10].
  - A paper closes by naming its binding limit (n > 50) and the next step [S025 p. 30].
- **Say–do update**: ✅ stated + practised, now from full texts spanning 1963–2015. Variants in §3, rows 8 and 19–20.

### M2 · Two-radius trust-region discipline

- **Strongest practice**:
  - First written record: ρ is a lower bound on Δ that is never increased, Δ ≥ ρ, and nine priority rules decide between step types. The idea is credited to research student Evan Jones [S014 pp. 26–28, 34–35].
  - The published description, with the 0.1/0.7 bands, the 1.5ρ reset and the 16/250 schedule [S025 pp. 3, 11–14].
  - The source of the SKILL.md numbers: the Box 14 test with ⅛ρ²·CRVMIN [S018 pp. 4, 7, 27–29].
  - Short steps are postponed because they magnify errors in the model, and an explicit ρ-exit test is needed because successful models can make every step shorter than ½ρ [S007 pp. 8, 27–31].
  - F is not evaluated for steps shorter than ½ρ [S047 p. 5; S072 p. 8].
  - The error-bound test decides when ρ may be reduced [S068 pp. 10–12].
  - BOBYQA refuses to reduce ρ until at least three new F values have been computed at it, which rules out superlinear convergence: the discipline gives up asymptotic speed for stability [S108 p. 17].
  - "one should try to avoid small values of the radius" far from a minimum [S165 p. 18].
- **Stated**:
  - ρ is never increased because each increase would force more decreases later [S025 p. 3].
  - ρ's purpose is to keep enough distance between the interpolation points when F has errors [S018 p. 4; S029 p. 6].
- **Say–do update**: ✅, now from the papers rather than code comments alone. The scope and the Limitations line need changes (§3, rows 1–4).

### M3 · Spend fewer evaluations than the model has parameters

- **Strongest practice**:
  - First statement of 2n+1 conditions with least-Frobenius change, by analogy with symmetric Broyden [S047 pp. 17–21].
  - The formal (m+n+1) system, its O((m+n)²) stable update, and n = 160 solved in 9688 evaluations against 13041 parameters [S045 pp. 4–17; S045 p. 5].
  - The first #F-versus-n table, "at most about 60n" [S072 pp. 13–15].
  - #F below the number of degrees of freedom of a quadratic [S018 pp. 33–34].
  - #F grows no faster than linearly up to n = 320 [S029 pp. 10–11].
  - With the same geometry machinery, symmetric-Broyden quadratics beat linear models, reducing #F and the final error "usually by more than a factor of five" [S093 p. 29].
  - Powell tested the obvious alternative norm himself and kept θ = 0 [S108 pp. 1, 9, 11–13].
  - A mechanism-level argument for O(n) points [S067 pp. 29–30].
- **Stated**:
  - Preference for m ≈ 2n+1 with one point changed per iteration [S137 p. 17].
  - "high accuracy in the solution of an optimization problem may not require high accuracy in any of the quadratic models" [S045 p. 5].
- **Precursors**: Broyden's update never increases the Frobenius norm of the Jacobian error (1968) [S019 pp. 24–25]. DFP builds G⁻¹ from gradient differences [S001 pp. 2–3]. RBF interpolation is the minimum-semi-norm interpolant [S055 pp. 9–12; S075 p. 2].
- **Say–do update**: ✅. The rationale and two Limitations lines need changes (§3, rows 5–7).

### M4 · Engineer cost and rounding error as part of the algorithm

- **Strongest practice**:
  - A whole paper exists because rounding made a correct algorithm inefficient. The fix is a factored Ω whose shape keeps a zero block in floating point [S124 pp. 3, 10–16, 22–25].
  - The error-matrix stability invariant, the M⁴ cancellation analysis, constant-term suppression, implicit Hessian storage, and a 10⁵-iteration stress test [S045 pp. 13–14, 19–24, 29–35].
  - The origin-shift error analysis, working with differences, and time/(n²·#F) roughly constant [S018 pp. 13, 15–17, 29, 37].
  - RESCUE, the eighth-power argument for origin shifts, and safeguard costs reported per row [S007 pp. 20–25, 32, 34].
  - Flops as the design target: O(n³) → O(n^{7/3}) or O(n^{11/5}) [S148 pp. 6–24; S165 pp. 12–20].
  - An O(n²)-per-iteration budget drives LINCOA's step [S067 pp. 2, 9–11].
  - In 1968: O(n³) → O(n²), rounding floors on Δ, and a projection identity that stops rounding errors accumulating [S019 pp. 9, 19, 21–25, 29–30].
- **Stated**:
  - "whenever I try to invent a new method, I assume initially that the computer arithmetic is exact". Stability properties then let matrix details follow [X002 p. 4].
  - "A device of this kind was necessary in order to provide software" [S137 p. 13].
  - An O(n³) average per iteration "would not be practicable" [S067 p. 2].
- **Say–do update**: ✅. Step 3 needs the split in §3, row 9, and step 4 the concrete protocol in row 10.

### M5 · Experiment-first validation with honest scope

- **Strongest practice**:
  - A random family with 5 instances per n, a per-ρ trace, a rounding stress test by adding 10⁴ to F, a published failure on sums of moduli, a scaling law, per-task timings and a baseline from published counts [S025 pp. 22–30].
  - Nine problems, "?" for runs above 500,000 evaluations, and reruns under permuted variables [S018 pp. 30–37].
  - Chaotic and unexplained results printed [S036 pp. 9–19].
  - Perturbed starts and a ρ_end sweep to separate local minima [S007 pp. 33–39].
  - Surprises labelled and then tested [S047 pp. 12–17].
  - An "embarrassing" spread reported [S072 pp. 12–15].
  - Raw outliers and extra runs for one cell [S108 pp. 10–17].
  - Two local minima with their F values [S067 pp. 23–25].
  - In 1968: a no-solution case, a local minimum chosen as "a severer test", a deliberately badly scaled case, and every CALFUN call listed [S019 pp. 35–42, 45].
  - Untuned parameters, and a terminal-number diagnosis of every failure [S050 pp. 9–12].
  - Wrong-minimum runs kept in the main table in 1963 [S001 p. 5].
- **Stated**:
  - "without numerical experience, I would be cut off from my main source of ideas" [X002 p. 3].
  - "I could not tolerate a failure rate of 10%" [X002 p. 4].
  - Multiple starts, and the warning that slow runs are often blamed on local minima when the method is unsuitable [X001 p. 12]. The scope is a few hundred variables [X001 p. 21].
  - "it is important to study what can go wrong" [S014 p. 42].
  - Solve particular problems well "in order not to be misled from efficiency in practice by a desire to prove convergence theorems" [S029 p. 2].
- **Say–do update**: ✅ for algorithm and software papers. Scope, step 1 and two merged clusters are in §3, rows 11–13, and §4.2.

### M6 · Ship the algorithm as free, self-checking code

- **Strongest practice**:
  - The 1968 Harwell report ships listing, driver, CALFUN and printed output, with a parameter section for a reader "who just wishes to make use of the subroutine" [S019 pp. 9–13, 45].
  - Code free by e-mail [S025 p. 30; S018 p. 37; S007 p. 39].
  - Four packages free (TOLMIN, COBYLA, UOBYQA, NEWUOA) [S029 p. 11].
  - BOBYQA sent to about 200 people [S108 p. 10].
  - The RBF programs too [S057 p. 22; S074 p. 29].
  - Reports and software were free "Decades before this has been endorsed by governments and funding agencies" [R007 p. 13]. Code reports appear from 1970 on [R007 pp. 27–30], and his last months went to "finishing touches to software" [R007 p. 24].
- **Stated**:
  - "Whenever the author has discovered techniques of this importance to practical algorithms on previous occasions, he has developed Fortran software that makes the discoveries available for general use." [S124 p. 22]
  - Better techniques should be "just as easy to use" as primitive ones [X001 p. 20].
  - The Harwell duty to produce general Fortran, and HSL started "to reduce duplication" [X002 p. 3; X001 p. 8].
- **Say–do update**: ✅, with the practice dated back to 1968 (§3, row 14).

### Heuristics and taste marks with new full-text practice

- **H1** (rescale before RHOBEG): [S019 pp. 10–11, 40–42].
- **H2** (NPT = 2n+1, also n+6): [S018 pp. 2, 4; S036 pp. 17–19; S007 pp. 34, 37; S108 p. 12; S067 pp. 23–25]. The evidence is mixed: see §3, row 23.
- **H3** (bound interval ≥ 2·RHOBEG): [S036 pp. 6–7; S007 p. 5].
- **H4** (check the model before lowering the resolution): [S025 pp. 11–13; S068 pp. 11–12; S072 p. 9; S018 pp. 28–29; S007 pp. 30–31; S093 pp. 8–9]. Variant: rebuild the model by differences before declaring a stationary point [S019 p. 35].
- **H5** (local minima → several starts): [S001 p. 5; S019 pp. 8–9, 45; S025 p. 23; S007 p. 38; S067 p. 23]. See the refinement in §3, row 24.
- **H6** (model each constraint): [S014 pp. 3, 24, 29–30; S050 pp. 2–3, 12; S030 pp. 3–5, 21]. Also a 1989 statement of the principle: "I still hold this view, and it has been strengthened by the results of this paper." [S115 p. 40]
- **H7** (redesign above O(n³)): [S047 pp. 2–3, 17; S025 pp. 28, 30; S045 p. 3; S067 p. 2]. Variant: redesign by a change of coordinates, not of model [S165 pp. 12–13; S148 p. 21].
- **H8** (equality as two inequalities): [S067 p. 2].
- **H9** (say when published results and current code differ): [S007 p. 33; S072 p. 13; S018 pp. 30–31].
- **Taste mark 5** (theory written to enable code): the memoir sentence is verified, "Mike Powell refused to follow this dichotomy" [R007 p. 3]. Variants: theory written to explain a method's success rather than to improve software [S121 p. 3]; theory for a simplified family that is explicitly slower than the shipped code [S093 p. 2]; theory that exposes a practice–theory gap and proposes an algorithmic change [S139 p. 14].
- **Warning sign 1** (a default recommended without its failure cases): McKinnon's example rebuilt in full [S029 pp. 5–6]; Nelder–Mead [S014 pp. 17–18, 44]; simulated annealing, "a horrible method" [X001 p. 12], "very extravagant in their use of function evaluations" [X002 p. 4; S014 p. 47]; a popular preference for truncated CG [S165 p. 3]; claims about Karmarkar's method [S115 p. 36].
- **Warning sign 3** (lumping constraints): [S115 p. 40; S014 p. 3; S050 p. 12].

---

## 3. Variants and contradictions

The full texts take precedence over search snippets. Rows 1–18 change what SKILL.md says. Rows 19–27 add a variant note without changing the claim.

| # | SKILL.md claim | What the full texts show | Cards | Change |
|---|---|---|---|---|
| 1 | M2 Limitations: "The constants (0.1, 0.7, 1.5, 16, 250) are empirical and their rationale is undocumented (a tacit-knowledge gap)"; Honest Boundary, same | Several constants are argued in print. The three ratio bands are read as "too conservative, adequate or overambitious", the 1.5ρ reset "is helpful occasionally", and the 16/250 formula gives reductions "by about a factor of ten" that end exactly at ρ_end [S025 pp. 11, 14]. The 16/250 formula also follows from ρ_old/ρ_new = ρ_new/ρ_end, the 1.5ρ snap exists "to sharpen the test in Box 10", BIGLAG's radius rests on three stated considerations, and the sixth-power weight rests on σ_t = O(Δ⁴/dist⁴) [S018 pp. 23, 27–28]. The roles of β = 2.1, γ = ¼ and Δ_{k+1} = max[ρ_k, ½‖step‖] are given, and the two-radius idea is credited to Evan Jones [S014 pp. 26–27, 34–35]. The tolerance ε is motivated by the reduction that a step shorter than ½ρ gives up [S068 p. 11]; the card's reconstruction of ⅛ from this is its own inference, and the printed constant cannot be read in the extracted text. Other constants are labelled empirical: the CG truncation [S018 p. 19], and 0.01 and 0.1 in BOBYQA [S007 pp. 23, 32]. The model-error test and the step test changed between the 2003 progress report and the release, from ½ηρ² to ⅛ρ²·CRVMIN [S072 pp. 8–9; S018 pp. 28–29]. | S025, S018, S014, S068, S072, S007 | Rewrite: "Some constants are argued (list); others are labelled empirical in the papers; values were retuned between versions." Narrow the tacit-knowledge gap in the Honest Boundary. |
| 2 | M2 Limitations: a monotone RHO "is ill-suited to strongly noisy or drifting objectives" | Powell designs the ρ floor for mild noise. A large ρ₁ "can alleviate the damage from any random noise" [S014 p. 27]. F is reduced with well-separated points "before closer interpolation points are allowed" [S068 p. 10]. ρ_beg should make values informative when F has "spurious contributions that are larger than rounding errors" [S018 p. 4]. The algorithm is "designed to be robust when the objective function is noisy" [S072 p. 7]. Δ ≥ ρ is "intended to be suitable" for first-derivative discontinuities [S018 p. 33]. The limits are documented too: sums of moduli with n terms fail [S025 pp. 26–27], and rounding sets a floor below which the work is wasted [S025 p. 26; S068 p. 13]. There is no stochastic model anywhere. | S014, S068, S018, S072, S025 | Qualify: large RHOBEG and the ρ floor are Powell's own remedy for mild noise and kinks; strongly noisy or drifting F remains outside the lens. |
| 3 | M2 one-line: RHO is the "resolution" of the search | Also stated: ρ keeps interpolation points apart so that errors in F do limited damage [S018 p. 4; S025 p. 2; S029 p. 6; S047 p. 5], and increases are avoided because each would force more decreases later [S025 p. 3]. | S018, S025, S029, S047 | Add the noise-separation reading next to the resolution reading. |
| 4 | M2 presented as Powell's trust-region method | The two-radius split belongs to the interpolation codes from UOBYQA on. COBYLA used Δ = ρ [S047 p. 5; S014 p. 34]. His general trust-region exposition has one radius [S137 p. 15], as do the theory papers [S129 pp. 3–5; S030 p. 4] and the SAO proposal [S167 p. 16]. The convergence proof uses a single ρ, and Powell plans to restore the two radii for efficiency [S093 pp. 5, 30]. | S047, S014, S137, S129, S030, S167, S093 | Scope note: "specific to the interpolation-model codes (UOBYQA–LINCOA)". |
| 5 | M3 Different from standard practice: Powell "trusts an underdetermined model plus memory of curvature" | ∇²Q does not become accurate. At termination ‖∇²F − ∇²Q‖_F still exceeds ½‖∇²F‖_F [S007 p. 3]. At n = 320, 96.8% of the initial Hessian error remains, and Powell calls BOBYQA possibly "the world's worst procedure for estimating second derivatives" [S108 p. 14]. ‖H_K − ∇²F‖ > 0.9‖H_1 − ∇²F‖ is not unusual [S067 p. 3]. Powell's own explanations: a win/win argument found "with hindsight" [S018 pp. 2–3]; Hessian changes tend to zero, which gives a Broyden–Dennis–Moré-type condition [S072 pp. 4–5; S029 p. 10; S137 p. 18]; sub-level sets of Q exclude neighbourhoods of worse interpolation points [S067 pp. 29–30]. He also says that convergence theory did not explain NEWUOA's success [S007 p. 3], and his account of the mechanism changed between 2007 and 2015 [S029 p. 10; S007 p. 3; S067 pp. 29–30]. | S007, S108, S067, S018, S072, S029, S137 | Rewrite the rationale: "judge the model by the steps it produces, not by its accuracy" (cluster Q10, 9 works). |
| 6 | M3 Limitations: "The choice of norm is itself debatable: later work explores other norms (⚠ unverified)" | The Frobenius norm of the Hessian change is chosen for independence from the shift of origin x₀ and for uniqueness [S045 p. 4]. Powell himself tested a θ-weighted norm with a gradient term, and found it "disappointing" in practice [S108 pp. 1, 11–13]. | S045, S108 | Replace the ⚠ lead with these two cards. |
| 7 | M3 step 4: choose the point to replace by Lagrange function or denominator, "not just its age" | Age is a legitimate secondary criterion: among points with \|ℓ_t\| ≥ ½ max, the oldest is dismissed, because the update erases errors in the replaced row and column [S045 pp. 14, 29]. | S045 | Variant note. |
| 8 | M1 step 5 and Workflow A: "UOBYQA only for small n" / "UOBYQA stayed for small n" | NEWUOA "has superseded UOBYQA" [S029 p. 10], while UOBYQA is still distributed [S029 p. 11]. The full-quadratic regime survives as the user's choice m = ½(n+1)(n+2) inside NEWUOA and BOBYQA [S018 p. 2; S007 p. 34]. UOBYQA's limit is given as three figures: "very promising" for n ≤ 20 [S025 p. 1]; prohibitive beyond about 50 [S025 p. 30; S047 p. 2; S045 p. 3]; about 100 in practice [S029 p. 10]. | S029, S018, S007, S025, S047, S045 | Variant: the predecessor survives as a parameter setting; cite the 20/50/100 figures with their sources. |
| 9 | M4 step 3: "Give numerical repairs their own named routines … triggered by measurable symptoms" | Split in two. Geometry repairs are kept as named routines (BIGLAG, BIGDEN [S018 pp. 20–26]; ALTMOV, RESCUE [S007 pp. 12–13, 20–25]). Arithmetic patches are rejected: "if a need for the modification of parameters is detectable, then substantial errors must have occurred already that require attention" [S124 p. 25]. A code-level precaution is published together with the property it breaks [S045 p. 31]. Stability is designed in instead: an error matrix that the update zeroes in the touched row and column [S045 p. 14; S068 pp. 6–8; S025 pp. 16–17], and a factored representation whose shape forces the invariant [S124 p. 14; S018 p. 13]. The order is stated: exact arithmetic first, then stability properties [X002 p. 4]. | S018, S007, S124, S045, S068, S025, X002 | Rewrite step 3 (merged cluster Q8, §4.2). |
| 10 | M4 step 4: "Test the same problem at different precisions or on different machines" | Powell's protocol works on one machine and uses transformations that change nothing in exact arithmetic. Examples: permute the variables [S018 pp. 32, 36; S036 pp. 14, 18–19]; run a configuration in which the new code must equal the old one [S124 pp. 23–24]; add a large constant to F [S025 p. 26]; rerun in single and double precision [S139 pp. 5–6]; add 10⁻⁶-perturbed starts [S007 p. 36]; rerun with a 100× tighter tolerance [S007 p. 38]; solve the mirrored problem [S170 p. 25]; monitor a sign invariant [S124 p. 24]. | S018, S036, S124, S025, S139, S007, S170 | Rewrite step 4 with this protocol (cluster Q9, 9 works); add it to the Workflow B checkpoint. |
| 11 | M5 step 1: "Pick 1–10 small problems whose solutions or structure you know" | The main instrument is a random family with a planted minimizer: the trigonometric sum of squares, used from 1963 [S001 p. 5] to 2013 [S108 p. 10]. It has 5 instances per n, the same random numbers for every variant, min–max ranges rather than means, and n doubling up to 320 [S025 p. 22; S047 p. 14; S072 pp. 13–14; S029 pp. 10–11; S036 p. 12; S007 pp. 33–34; S093 pp. 28–29]. Hand-built problems with many local minima are added [S036 pp. 9–10; S007 pp. 35–38; S067 p. 23], and so are cases built to break his own method [S019 pp. 39–42; S055 p. 7; S075 p. 9; S085 p. 20; S170 pp. 23–24; S045 p. 33]. | as listed | Rewrite steps 1–2; fold cluster Q13 (adversarial cases, 8 works) into step 1. |
| 12 | M5 as a general practice (the ✗ card) | Theory-only papers exist and say so: "mainly of theoretical interest" and no numerical computation [S030 pp. 5, 21]; no experiments, stated [S167 p. 17]; pure theory [S129; S121 p. 3; S090 pp. 13–14]. The honest-scope half holds in each of them. | S030, S167, S129, S121, S090 | Scope M5 to algorithm and software papers. |
| 13 | M5 step 5: compare with other solvers (labelled generic) | Powell's papers compare only against his own earlier codes [S018 §8, pp. 30–37; S036 p. 11; S047 p. 3; S093 p. 30]. He calls his interest in numerical comparisons "relatively small" [S115 pp. 39–40]. The exception is a comparison with other methods on their own test problems with their published counts [S019 pp. 37–39]. UOBYQA's only baseline is Powell's own 1964 method, using Fletcher's (1965) published Chebyquad counts [S025 pp. 29–30]. | S018, S036, S047, S093, S115, S019, S025 | Keep the "generic modern step" label and add this fact. |
| 14 | M6 Practice: "all five solvers were distributed this way from 1992 to 2013" | The practice dates from Harwell in 1968 [S019 pp. 9–13, 45; R007 pp. 5, 13, 27–30; X002 p. 3]. Variants: a package delivered to a company [S089 pp. 3, 14, 21]; no free-use statement [S078]; no code at all [S030 p. 21]. | S019, R007, X002, S089, S078, S030 | Extend the Practice line. |
| 15 | Academic Lineage: "Doctoral students: not verified … Do not name any" | PhD students named by the memoir: Philippe Toint (from January 1977) [R007 p. 15], Ya-xiang Yuan (1983–88) [R007 pp. 15–16] and Hans Martin Gutmann [R007 p. 21]. Research student and coauthor Ioannis Demetriou [R007 p. 19]. Research student Evan Jones, who proposed the two radii [S014 pp. 34–35]. About 18 research students ("I’ve had about 18 research students"), with published work with "about a third" of them [X001 p. 14]. The interviewer calls Martin D. Buhmann "your student" and Powell does not contradict it [X001 p. 13] (interviewer framing). | R007, S014, X001 | Fill in. Do not name A. C. Faul as his student: the card finds no supervisor named [S075 header]. |
| 16 | Research Trajectory: Harwell "exact dates ⚠️"; Plummer chair "start year ⚠️" | Harwell 1959–76 [R007 p. 5]; Plummer Chair from 1976 [R007 p. 9]; ScD 1979 [R007 p. 12]; retired 2001, two years early, to maximise research time [R007 p. 24]; died 19 April 2015 [R007 p. 3]. | R007 | Fill in. |
| 17 | COBYLA anatomy: Origin "not documented"; Abandoned paths "Unknown" | Origin, in Powell's own later surveys: IMSL had wrapped his gradient codes (TOLMIN) with differences, and he was unhappy about it and about the popularity of simulated annealing and genetic algorithms [S029 p. 2; S014 p. 2]. A four-variable, ten-constraint problem from Westland Helicopters led to the code, which is "very slow, as expected, when there are no constraints" [S029 p. 3; S014 p. 45]. On convergence: "I am unable to give a favourable answer within the usual conventions of convergence theory" [S029 p. 8]. COBYLA had one radius; the two radii came later [S014 p. 34; S047 p. 5]. Abandoned path: RBF models were tried for the local model and "did not bring, in the optimization context, the results he had hoped for" [R007 pp. 17, 21]. The memoir places the RBF attempt first and the polynomial-interpolation codes after it [R007 pp. 17, 21]; Powell's own accounts of COBYLA's origin do not mention it [S029 pp. 2–3; S014 p. 2]. RBF global optimization continued with Gutmann [S055 pp. 8–13; R007 p. 21], and UOBYQA's development began "about ten years" before 2002 [S047 p. 10]. | S029, S014, S047, R007, S055 | Replace "Speculation" with these. The COBYLA paper itself stays abstract-only [S008]. |
| 18 | Inner Tension 1 and Latest: "complexity guarantees … apparently still being added in 2026"; the handoff note that Powell published DFO trust-region convergence papers in 2003 and 2012 | Checked against the cards. S093 (2012) proves lim ‖∇F(x_k)‖ = 0 for a simplified family with one evaluation per iteration, and gives no rate or complexity [S093 pp. 4, 25]. Powell concedes that the family is much less efficient than NEWUOA [S093 p. 2]. S047 (2003) is an empirical comparison of model spaces with no convergence theorem [S047 pp. 3, 11]. The shipped codes have no convergence theory: for COBYLA he cannot give a favourable answer [S029 p. 8], and "NEWUOA and BOBYQA provide a counter-example to the suggestion in Gould and Toint (2004) that theoretical insight is of vital importance" [S007 p. 3]. A gradient-based family theorem covers any-decrease acceptance and the symmetric Broyden update [S129 pp. 2–6]. The memoir says his interest in theory "slowly decreased" in the DFO years [R007 p. 17]. | S093, S047, R007, S029, S007, S129 | Qualify the tension: convergence (not complexity) for a simplified DFO family exists from Powell himself (S093 only); the shipped codes remain without theory. |
| 19 | M1 lineage COBYLA → UOBYQA → NEWUOA → BOBYQA → LINCOA | The lineage also contains intermediates that were tried and dropped: UOBDQA and UOBSQA [S047 pp. 3, 9–16], the 2003 prototype [S072], five alternative-step versions [S036 pp. 11–14], Krylov steps and boundary searches [S067 pp. 12–16, 21–25], and a θ-weighted norm [S108]. | S047, S072, S036, S067, S108 | Variant note (the lineage includes rejected intermediates). |
| 20 | M1 applies to Powell's own solvers | The same move is applied to other people's algorithms (Davidon [S001 p. 1]; Fletcher's penalty [S050 pp. 1–2]; Karmarkar without the standard form, with equivalence proved [S115 pp. 23–31]; SAO with a new acceptance rule [S167 pp. 3, 16]); to theorems (a regular-grid hypothesis removed [S090 pp. 2–3]; a Lipschitz-boundary assumption removed with the rate kept [R007 p. 23]; differentiability replaced by continuity [S167 p. 4]); and within one paper (tridiagonal → band [S148 pp. 4–14]). | S001, S050, S115, S167, S090, R007, S148 | Variant note; this folds cluster Q15. |
| 21 | Research Taste mark 5, and Honest Boundary "Stated but unverified" | The memoir sentence is verbatim [R007 p. 3]. The 2007 essay and the Acta Numerica survey are now read in full [S029; S014]. | R007, S029, S014 | Move from "unverified" to verified. |
| 22 | Mentor Voice: "no recordings or recollections in the evidence"; Weak spots: "no student recollections were readable" | Two first-person interviews [X001; X002] and a memoir partly by a former PhD student [R007 pp. 10–12, 15]. Supervision as reported: he chose neglected topics for students "in order that they can become leading experts" [X002 p. 5]; he was usually not a coauthor of students' papers [X002 p. 5; X001 p. 14]; visitors got contact "maybe once a month" [X001 p. 15]; he read and annotated everything a junior colleague wrote [R007 p. 11]; he encouraged a student onto an idea, then recorded it himself in a survey when the student did not publish [S014 pp. 34–35]. | X001, X002, R007, S014 | Update Mentor Voice (real quotes are now available) and the Weak spots. |
| 23 | H2: start at NPT = 2n+1, also try n+6 | Best m "may depend strongly on F" [S036 p. 19]. n+6 needs fewer evaluations on ARWHEAD [S036 p. 18] and on the points problem, which has many local minima [S007 p. 37]; it gives the shortest run times on CHROSEN despite somewhat more evaluations [S036 pp. 17–18]; it needs about 3× more evaluations on the trigonometric family [S036 p. 17]. 2n+1 beating n+6 is usual but not general [S007 p. 34]. | S036, S007 | Variant note. |
| 24 | H5: final F depends on start or NPT → local minima | Add two tests. Slow runs are often blamed on local minima when "the method they're using simply isn't suitable for the objective function" [X001 p. 12]. Rerun with ρ_end 100× smaller: if each run changes far less than the gaps between runs, the values are distinct minima, not rounding noise [S007 p. 38]. Give each failure the terminal numbers that assign it a cause [S050 pp. 11–12; S019 pp. 13, 42]. | X001, S007, S050, S019 | Rewrite H5 (cluster Q21, 5 works). |
| 25 | NEWUOA and BOBYQA anatomy: "Why then", "Origin: *Speculation*" | Least-Frobenius updating was "not tried by the author until January, 2002", and its results "seemed to deserve publicity as soon as possible" [S072 pp. 7–8]. Eighteen months of rounding trouble followed [S124 p. 22]; the release came in December 2003, after Powell "resisted pressure from the editor and referees" of S072 to describe unstable details [S018 p. 3]. BOBYQA started because NEWUOA's success with 320 variables "encouraged" an extension to bounds [S036 p. 6], and "It was not easy to decide to release" it [S007 p. 39]. | S072, S124, S018, S036, S007 | Replace the speculation. |
| 26 | Workflow E step 4, Heuristic 9 | Every constant labelled with its origin (a proof requirement, a balancing equation, a magnitude estimate, "chosen intuitively", "chosen empirically") [S019 pp. 16–17, 21–23; S025 pp. 11, 14; S018 pp. 19, 23, 27–28; S007 pp. 23, 32; S093 pp. 6–7]; the tuning status of experimental parameters stated [S050 p. 9; S093 p. 27]. | as listed | Add to Workflow E as a check (cluster "label constants", 6 works). |
| 27 | Anti-pattern "Defaulting to Nelder–Mead" | Confirmed in full text [S029 pp. 5–6; S014 pp. 17–18, 44]; simulated annealing added [X001 pp. 12, 20; X002 p. 4; S014 p. 47]. | S029, S014, X001, X002 | Add simulated annealing and genetic algorithms. |

**Contradiction accounting.** The digests contain four ✗ links. S025 is row 1 (a partial contradiction). S030 is row 12 (a matter of scope). R007 covers rows 15–17. The fourth is a reader's note about the wording of one abstract relative to the proofs in the same paper. By the house rule it is not a finding about the researcher and is not used; the general lesson it would give (state in the abstract only what is proved) is already Taste warning sign 2. One ⚠ link that records a difference between two reports' tables is likewise not used.

---

## 4. Promotions

SKILL.md has six core methods, so one promotion fits under the 3–7 cap. Nine clusters have ≥3 distinct full or partial works and pass all four checks. Five of them (Q1–Q5) are one stated loop and are merged into a single Method 7. The other four cannot be separate methods once the cap is reached. They are merged into existing methods (Q6+Q7 into M5, Q8 into M4) or routed to the taste layer (Q16), with the reasons given in §4.2. No existing method is weak enough to replace: the two with the fewest supporting works, M6 (17 distinct works, 14 ✅) and M2 (18 distinct works, 11 ✅, 10 ⚠), are still well supported and specific to Powell.

### 4.1 Promote → Method 7: Settle claims with the smallest decisive case (numerics → conjecture → proof or counterexample, with proofs fitted to the code)

**Cluster** (34 distinct full or partial works: 31 Powell papers plus X001, X002 and R007), merged from five candidate clusters whose cards overlap:

| Sub-cluster | Full/partial works | Abstract-level support |
|---|---|---|
| Q1 Smallest explicit counterexample: against a popular default, per mechanism or model class, per design rule, marking a theorem's boundary | 20 (19 projects): R007, S014, S019, S029, S030, S047, S067, S072, S090, S093, S108, S115, S121, S124, S129, S137, S139, S148/S165, S167 | S020, S026, S049, S142, S144, S150, S155 (✅); S128, S134 (⚠); S145 metadata, not used |
| Q2 Numerics → conjecture → proof or counterexample | 13: X001, X002, R007, S025, S045, S055, S068, S075, S078, S090, S115, S121, S139 | S032, S113, S134 (✅); S031, S051 (⚠) |
| Q3 Explain a surprise with a designed follow-up experiment | 7: X001, X002, S036, S047, S074, S108, S170 | — |
| Q4 Fit the proof to the code (safeguards that let the proof go through, theorems widened to admit the practitioner's choice, proof-only devices dropped) | 10: R007, S019, S030, S047, S050, S067, S072, S085, S093, S129 | S027, S032, S175 (✅); S125, S128, S147 (⚠) |
| Q5 State the price of theory in numbers (implied constants and counts against machine precision; which questions theory does not answer) | 7: S007, S014, S029, S085, S093, S129, S165 | — |

**Why one method.** Powell states the loop as one thing: "Answers to such questions are either proofs or counter-examples, and often I have tried to discover which of these alternatives applies." [X002 p. 2] The sub-clusters also meet in the same papers. S129 has both the sharpness counterexample and the theorem widened to admit practice [S129 pp. 2, 5, 11–13]. S093 has the family proof and the counterexample for the exact-step rule [S093 pp. 5–6, 22]. S030 has the proof-motivated terms and the one-variable example against sufficient decrease [S030 pp. 4, 21]. S115 has the table, then the conjecture, then the exact-arithmetic proof of failure [S115 pp. 36–39].

| Check | Result | Evidence |
|---|---|---|
| 1 Cross-project recurrence | ✅ | Spans 1968–2015 and at least six topics. Nonlinear equations [S019 pp. 5–8]; quasi-Newton rate theory [S139 pp. 3–14; S121 pp. 3, 22–23]; SQP and trust regions [S050 pp. 3, 6; S030 pp. 4, 21]; LP [S115 pp. 32–39]; RBF [S090 pp. 3, 14; S055 pp. 7, 14–15; S075 pp. 5–10; S078 p. 12]; trust-region linear algebra [S165 p. 3; S148 pp. 4–14]; DFO design [S047 pp. 9–16; S072 pp. 6–7; S124 pp. 11–12; S108 pp. 5–9, 12; S067 pp. 11, 14–16]; DFO theory [S093 p. 22; S129 pp. 11–13]; surveys [S014 pp. 4, 14, 17–18, 39–40; S029 pp. 4–9; S137 pp. 3, 8–10, 13]. |
| 2 Say–do consistency | ✅ | Say: the quote above [X002 p. 2]; "If I try an algorithm and it doesn't behave in the way I expect then there's a basis of an idea, and I try to explain it." [X001 p. 17]; "So, I don't delay publication while waiting for proof." [X001 p. 18]; "I also try to explain and to take advantage of the information that is provided by both good and bad features of numerical results" [X002 p. 3]; do not be "misled from efficiency in practice by a desire to prove convergence theorems" [S029 p. 2]; the standard theoretical questions "do not go far enough" [S165 p. 18]; any-decrease acceptance is a "strong preference" [S129 p. 2]; sufficient decrease "was introduced to assist proofs of convergence" [S072 p. 2]. Do: Lemma 3 "was suggested by numerical calculations" [S045 pp. 26, 32]; a table suggests spurious convergence and closed-form formulas prove it [S115 pp. 36–39]; COBYLA's surprise is tested by random diagonal scaling [S047 pp. 15–16]; a counterexample is sought as a nonlinear feasibility problem [S121 pp. 22–23]. Secondary: "Mike's remarkable talent for producing intriguing counter-examples to sometimes widely held beliefs" [R007 p. 16]. |
| 3 Executable, different from standard practice | ✅ | Steps below. Mainstream DFO convergence theory (Conn–Scheinberg–Vicente) secures model accuracy with a model-improvement step that may spend extra F values [S093 pp. 3–4; S108 p. 3]; Powell calls it "a major strategic difference" and instead widens the theorem to cover the one-F-per-iteration code [S129 pp. 2, 5; S093 pp. 4–6]. Design rules he argues for carry a small failing instance, and each surprise is either settled or printed as unexplained. |
| 4 Exclusivity | ✅ | Counterexamples are common in mathematics. What is distinctive is using them systematically as the unit of argument for design rules and against popular defaults, together with fitting theorems to the code. The memoir singles this out [R007 pp. 3, 16]. Powell's DFO theory differs from the mainstream Conn–Scheinberg–Vicente theory in its proof-to-code fit (sub-cluster Q4): one new F value per iteration, no separate model-improvement phase [S093 pp. 3–4]. This supports Q4, not the counterexample core. |

**Draft for SKILL.md** (for the SKILL.md editor; not applied here):

- **One line** (as applied in SKILL.md, narrowed after review): Treat an unexpected run or a disputed design rule as a conjecture. Settle it with the smallest decisive case: a designed experiment that removes the suspected mechanism, an explicit counterexample in two or three variables, or a proof written for the family of methods the code actually belongs to.
- **Steps**:
  1. Keep a log of runs that did not behave as expected. Write each one as an explicit conjecture about mechanism, rate or accuracy [X001 p. 17; X002 p. 2; S047 pp. 3, 13].
  2. Test the suspected mechanism experimentally first. Transform the problem so that the mechanism is removed: random diagonal scaling [S047 pp. 15–16]; bounds at ±10¹⁰ to run the unconstrained case inside the constrained code [S036 p. 11]; ten extra instances for one surprising cell [S108 p. 12]; a spacing constraint to test an explanation [S074 p. 26]. If the surprise survives, publish it as unexplained [S047 p. 13; S074 p. 26; S036 p. 15].
  3. Shrink the question to the smallest setting where it survives (n = 2, d = 1, one variable) and settle it there exactly: a proof [S121 p. 3; S090 pp. 3, 14; R007 p. 9], or a counterexample with exact numbers [S115 pp. 32–39; S139 pp. 9–10]. If a counterexample is hard to find, parametrise the iterate sequence and solve the algorithm's conditions as a feasibility problem [S121 pp. 22–23].
  4. For each rule or safeguard you argue for (not every constant), give the smallest instance on which the method fails without it [S072 pp. 6–7; S124 pp. 11–12; S093 p. 22; S108 pp. 5–9; S129 pp. 11–13; S067 pp. 11, 14–16], and label the other constants by origin; Powell labels several constants empirical [S018 p. 19; S007 pp. 23, 32] and "often" (not always) settles a question this way [X002 p. 2]. Give every popular default you argue against a two-variable counterexample plus a cost argument [S165 p. 3; S148 p. 5; S115 pp. 4, 32–39; S029 pp. 4–9].
  5. When you prove, fit the theorem to the code. Prove it for a family defined by one inequality per decision, so that the practical choices (any-decrease acceptance, growing B_k, any ζ in an interval) are inside it [S129 pp. 2–5; S093 pp. 5–6; S030 pp. 3, 20, 22]. Add a safeguard only if it is inactive near the solution (show r_k → 1 and cite the unsafeguarded rate theorem [S030 pp. 15, 18]) or costs at most one evaluation [S093 pp. 6–8]. If a safeguard is kept only so that a theorem applies, say so and name its cost, as in 1968: x is not moved after a special step so that Powell's 1969 theorem holds, a "rather contentious decision" [S019 p. 16]. Prefer devices that pay for themselves and also enable a proof: the dogleg is motivated in the report by O(n²) cost and the steepest-descent bias of short steps [S019 pp. 18–19], and the memoir adds that it "enabled the construction of a convergence proof" [R007 p. 6]; the stay-or-double penalty rule [S050 pp. 3, 6]; the η₂Δ near-active set [S067 pp. 9–10, 18–19]. Avoid devices that exist only to assist proofs when they cost practice [S072 p. 2; S030 p. 21].
  6. State the price of the theorem in numbers: the implied constant against machine precision [S014 p. 11], the worst-case count, even when it is "monstrous" [S129 p. 15], a finiteness bound against the number of floating-point values [S029 p. 8], and when a bound misrepresents practice [S085 p. 13].
- **Applies to stage**: idea generation, algorithm design, result judgement, theory, writing.
- **Different from standard practice**: see check 3 above (neutral contrast with Conn–Scheinberg–Vicente).
- **Limitations**: small cases can mislead about large n. COBYLA's surprising success on near-isotropic problems disappeared under scaling [S047 pp. 13, 15–16], and Powell suspects that his test functions are "too easy" [S093 p. 30]. The smallest case does not always extend: the n = 2 DFP theorem does not carry over to n = 3, because the path can pass around the limit line there, and months of counterexample search had not succeeded [S121 pp. 22–23]. Proofs for simplified families may not cover the shipped code [S093 p. 2]. Several surprises stayed unexplained [S047 p. 13; S074 p. 26; S036 pp. 15, 18]. Era: single-author work [X002 p. 5; X001 p. 14]; Powell still valued hand calculation [X002 p. 2]; today add computer-algebra checks and automated counterexample search (generic, not Powell-specific).

With Method 7 the skill reaches the 7-method cap. Any later promotion must merge into or replace a method.

### 4.2 Clusters that pass the four checks but are merged or routed (cap reached)

| Cluster | Works | Four checks | Decision and justification |
|---|---|---|---|
| Q6 Publish with explicit status (preliminary labels, publish without waiting for proof, tuning status, public correction of one's own earlier account) | 12: S007, S030, S036, S047, S050, S055, S068, S072, S093, S124, S129, X001 (+S010, S016 abstract) | Recurrence ✅ 1986–2012 [S050 p. 12; S072 pp. 8, 12–15; S047 pp. 19–20; S036 p. 19; S093 p. 27]. Say ✅ "I don't delay publication while waiting for proof" [X001 p. 18]; results "seemed to deserve publicity as soon as possible" [S072 pp. 7–8]. Executable ✅: label each component final, provisional or under development, and state the tuning status of every parameter set. Exclusive ✅: "The reason for jumping the gun in the publication of results …" [S047 pp. 19–20]; published before the release decision [S036 p. 19]. | **Merge into M5** as step 6. M5's function is to tell the reader what is and is not established, and status labels extend that from test scope to design maturity. A separate method would duplicate M5's "honest scope". |
| Q7 Publish the rejected alternative (decision record) | 13: S018, S036, S055, S057, S067, S068, S074, S078, S085, S089, S108, S124, S148 (+S006, S051, S142 abstract) | Recurrence ✅ 1992–2015. Say ✅ "The reason for giving so much attention to failures of the Krylov method is that our findings may be helpful to future research." [S067 p. 30]; "Most of the efforts of those investigations, which have taken about two years, were spent on promising techniques that have not been included in the software." [S067 p. 30]. Executable ✅: what was tried, which counterexample or table ruled it out, when the decision was taken [S067 pp. 4, 16, 25, 30]. Exclusive ✅: negative design results are in the abstract [S108 p. 1; S067 p. 1]. | **Merge into M5** as step 7, together with Q6. The same explanatory role applies to the design history. The keep-it-simple rule it implies (remove a component when measured #F does not justify it [S067 pp. 21, 25; S078 p. 27; S085 p. 22]) goes in the same step. |
| Q8 Stability designed in (self-correcting updates, invariant-preserving storage, invariant kept at the cost of information) | 11: R007, S001, S007, S018, S019, S025, S045, S068, S124, S137, X002 (+S118, S080 abstract) | Recurrence ✅ 1963–2009 [S001 p. 2; S019 p. 25; S068 pp. 6–8; S045 p. 14; S124 pp. 10, 14; S007 pp. 20–25]. Say ✅ [X002 p. 4]. Executable ✅: define the error matrix Ξ = W − H⁻¹ and show that the update zeroes the touched row and column [S045 p. 14]; store Ω = ZSZᵀ with exactly the rank that exact arithmetic implies [S124 p. 14]; test with injected errors [S045 pp. 30–32]. Exclusive ✅: it goes against "the standard advice of many numerical analysts" to factorize rather than update inverses [S124 p. 25; S045 p. 35]. | **Merge into M4** by rewriting step 3 (§3, row 9). It is the positive form of M4 ("rounding error as part of the algorithm"), and it corrects M4's own step 3. |
| Q16 Derive alone on neglected problems, then check the literature and credit | 6: R007, S068, S115, S167, X001, X002 | Recurrence ✅ [S068 p. 10; S115 pp. 3–4, 41; S167 p. 4; R007 pp. 10–12, 23–24]. Say ✅ "It is unusual for me to make progress in research by studying papers that other people have written" [X002 p. 3]; "I'd quite like to crack them myself" [X001 p. 14]; students get "topics that are not receiving much attention" [X002 p. 5]; DFO is "very much neglected" [X001 p. 22]. Executable ✅: derive first, then search and credit [S068 p. 10; S167 p. 4]. Exclusive ✅. | **Route to Research Taste** as a new mark 6 plus quick-check items (draft below). It concerns topic choice and working style, which the framework places in the taste layer, not a research step. Tension recorded from his own words: "I often consider submissions in isolation, although I should relate them to published work" [X002 p. 5]; he viewed the Karmarkar field "through a window that is shamefully narrow" [S115 p. 41]. |

**Draft wording for the merged items** (not applied):

- M5 step 6: "Label the status of each component (final, provisional, under development) and of each parameter set (tuned or not, fixed before the experiments or after). Publish when the results deserve it, and say what is incomplete" [S072 pp. 8, 12–15; S047 pp. 19–20; S050 p. 9; S093 p. 27; X001 p. 18].
- M5 step 7: "Publish the rejected alternatives with the counterexample or table that ruled each out, and remove a component from the code when measured costs do not justify it" [S067 pp. 1, 21, 25, 30; S124 pp. 9, 24; S018 p. 15; S108 pp. 1, 13; S089 pp. 15–16].
- M4 step 3: "Design stability in: choose updates whose error matrix is zeroed where it is touched, and representations whose shape forces the invariants exact arithmetic guarantees; keep named repair routines for geometry (BIGLAG, BIGDEN, ALTMOV, RESCUE), not for arithmetic patches" [S045 p. 14; S124 pp. 14, 25; S018 pp. 13, 20–26; S007 pp. 20–25].
- Research Taste mark 6: "The problem is neglected, and an algorithm you have in mind would extend the range of calculations that can be solved; a new algorithm can create its own applications" [X002 pp. 3, 5; X001 pp. 20–22; S170 p. 26; S029 pp. 1–2].
- New warning sign: "A primitive method is popular because it is easy to use (simulated annealing, Nelder–Mead)" [X001 pp. 12, 20; X002 p. 4; S014 p. 47; S029 pp. 2, 5].
- Taste quick-check: "Is the topic under-studied enough that one person can lead it?" [X002 p. 5]; "Would your method fail on more than a negligible fraction of your test set? (Powell: 10% is intolerable)" [X002 p. 4].

---

## 5. New heuristics

Clusters that are executable and pass at least one more check. "Recommend" = add to SKILL.md. "Fold" = add as a step of an existing method or workflow, with no new list item. SKILL.md already has 10 heuristics, the top of the framework's 5–10, so only two new items are recommended. To stay at 10, H10 could be merged into H9 (both about naming what produced a result) and H7 folded into M4 step 1. *Applied after review*: to respect the 5–10 cap, SKILL.md merges the first-pass H10 (name the implementation) into H9, keeps H1–H9 (the cards cite them), adds H11 below as its Heuristic 10, and folds H12 into Method 3, step 2 and Workflow C, step 3.

| Cluster | Works | Recurrence | Say–do | Executable & different | Exclusivity | Decision |
|---|---|---|---|---|---|---|
| Q11 Quadratic case first | 7: S001, S029, S036, S045, S072, S108, S137 (+S049, S132, S154 abstract) | ✅ 1963–2013 | ✅ [S137 pp. 16–17; S029 p. 2] | ✅ | ✗ (quadratic termination was the era's standard criterion [S001 p. 1]) | **Recommend (H11)** |
| Q12 Invariance picks the free choice | 12: S007, S014, S019, S036, S045, S047, S055, S089, S108, S137, S139, S165 | ✅ 1968–2013 | partial: stated as a criterion in papers [S045 p. 4; S036 p. 19] | ✅ | partial | **Recommend (H12)** |
| Q14 One code base, incumbent as a special case | 5: S036, S047, S093, S108, S124 | ✅ | partial [S047 p. 3] | ✅ | partial | Fold into M1 step 4: "run the predecessor as a special case of the new code (θ = 0, m = m*, bounds ±10¹⁰, switch off) with the same random numbers" [S108 pp. 2, 10; S124 pp. 23–24; S036 p. 11; S047 pp. 3, 11; S093 p. 28] |
| Q9 Rounding probes invariant in exact arithmetic | 9 | ✅ | partial [X002 p. 4] | ✅ | ✅ | Fold into M4 step 4 and the Workflow B checkpoint (§3, row 10) |
| Q21 Failure attribution (local minimum, rounding, or unsuitable method) | 5: S007, S019, S025, S050, X001 | ✅ | ✅ [X001 p. 12] | ✅ | partial | Fold into H5 (§3, row 24) |
| Label every constant with its origin | 6: S007, S018, S019, S025, S050, S093 | ✅ 1968–2012 | — | ✅ | partial | Fold into Workflow E and the M2 Limitations rewrite (§3, rows 1, 26) |
| Q13 Adversarial cases for one's own method | 8: S007, S019, S025, S045, S055, S075, S085, S170 (+S038 abstract) | ✅ | — | ✅ | partial | Fold into M5 step 1 (§3, row 11) |
| Q18 Cost measurement protocols | 10: S001, S007, S018, S025, S047, S067, S074, S089, S148/S165 | ✅ | — | ✅ | partial | Fold into M4 step 1 ("then check the formula by timing: time/(n²·#F) across n") and Workflow D |
| Q15 Enter another's method by re-derivation | 5: R007, S001, S050, S115, S167 (+S107, S125, S132, S150 abstract) | ✅ | ✅ [X001 p. 10; S115 pp. 3–4] | ✅ | partial | Fold into M1 as a variant (§3, row 20) |

**H11 · If** you design or judge an update or a method, **then** first ask what it does when F is quadratic (termination, a monotone error, the rate), and design it so that the quadratic-case property holds without restricting the method to quadratics.
Cases: the question is named as the one "most useful" to his development of unconstrained algorithms [S137 pp. 16–17]; the design creed is to solve contrived, often quadratic, problems well [S029 p. 2]; quadratic termination is used to filter competing methods [S001 p. 1]; the projection identity is proved for quadratic F and used for general F [S072 pp. 4–5; S045 pp. 9–10; S108 p. 3; S036 p. 5].

**H12 · If** a design choice has a free norm, weight or variant, **then** pick it by the invariance you need (shift of origin, scaling of the variables, orthogonal rotation), and reject a variant that loses the invariance even if it is more accurate.
Cases: the Frobenius norm of the Hessian change is chosen because it is shift-invariant [S045 p. 4]; the dependence of θ is fixed by scaling x → σx [S108 pp. 7–8]; a more accurate RBF edge variant is repaired because it loses scaling invariance [S055 pp. 16–17]; rotation insensitivity is a release criterion [S036 p. 19]; a prototype that is not rotation-invariant is kept "only for some preliminary investigations" [S047 p. 20]; slowness on a badly scaled system is shown to be intrinsic by invariance [S019 p. 42]; invariance licenses a simplification [S089 p. 11]; invariance is used to normalize a problem where the proof is easiest (origin at x_k [S007 pp. 19–20]; ∇²F(x*) = I [S139 p. 3]; B diagonal [S165 p. 5]).

---

## 6. Candidate pool (not promoted)

| Candidate | Works (full/partial; abstract) | Why it stays in the pool |
|---|---|---|
| Q17 Surveys as research instruments (one essay per mechanism with its best theorem and cleanest failure; survey as re-proof; recording a student's unpublished work) | 5: R007, S014, S029, S137, S148/S165 (the report rewritten for a conference audience); S037, S166 abstract | A writing move (§7.4 W5). SKILL.md has no survey workflow, so there is no gain |
| Q19 Model-error tests with online constants | 5: S018, S025, S068, S072, S093 | Evidence for M2 step 4 and H4, not a separate pattern |
| Q20 Lagrange-function (determinant-ratio) geometry control | 6: S014, S018, S025, S068, S093, S124; S002 secondary | Already M3 step 4; now practice evidence |
| Q10 Judge a model by its steps | 9 | Absorbed into the rewrite of the M3 rationale (§3, row 5) |
| Q25 Native-norm descent proof | 3 (S074, S075, S085; one RBF project); S046 abstract ⚠ | One research line; proof device §7.1 P16 |
| Q24 Local approximate Lagrange functions plus refinement (RBF) | 1 (S085); S109 abstract; S088, S110 metadata | RBF-specific, below the read threshold |
| Q26 Finite-domain edge effects as the open problem | 0 carded as candidate in full cards (topic of S055 pp. 13–17; X002 p. 6; X001 p. 13); S043, S113, S134 abstract | A research topic, not a method |
| Q23 Test the regime users actually have | 3: S057 p. 6, S067 p. 25, X001 p. 21 | Two practice cards; the note "difficulty does not track n" [X001 p. 21] belongs in the Workflow A checkpoint as a remark |
| Q22 Return the algorithm's by-products for diagnostics | 2: S001 p. 1, S019 p. 12 | Harwell era only; modern traces are covered by M5 and Workflow B |
| Q29 Two-part design: one change for the local rate, another for bad starts | 1: S019 p. 6 (+S137 framing); S002 abstract | Below the threshold |
| Q28 Same benefit as the classical technique, one requirement fewer | 1: S090; S012, S062 abstract | An M1 variant at abstract level |
| Q31 Subproblem devices (exact solve on a cheap restricted set; crude solve with a proven ratio) | 2: S025, S036; S095 abstract | Techniques (§7.2 A9–A10) |
| Q32 Benchmark on the competitor's own problem with their published counts | 1: S019 pp. 37–39 (S025 pp. 29–30 uses Fletcher's published counts for Powell's own 1964 method, so it is not a competitor case) | A note in §3, row 13 |
| Q30 Referee by checking every line | 1: X002 p. 5 (+R007 p. 11) | A stated habit; a Mentor Voice remark only |
| Q27 Recast a task as a small problem for one's own solver | 0; S188 abstract, S082 metadata | Below the read threshold |
| Balance cost monomials; timing sweep for hidden constants; advocacy rewrite | 1 project (S148/S165) | One project counted once; §7.1 P17, §7.3 E7 |
| Singletons, full or partial (4) | S050 (difference approximation justified by a vanishing multiplier, pp. 2, 10); S170 (practical choice exactly optimal for a nearby problem, pp. 7–8); S167 (merit function from the subproblem's own duality theorem, pp. 7, 16); S089 (check the asymptotic design rule against all higher-order terms, pp. 16–21) | Single papers; techniques |
| Singletons, abstract-level (13) | S177, S054, S123, S154, S120, S022, S033, S149, S169, S049, S155, S163, S162 | Abstract only; not used |

---

## 7. Technique inventory

Named devices with the card and page where they are used, for student use and for a possible `proof-playbook.md`.

### 7.1 Proof devices

| # | Device | Where |
|---|---|---|
| P1 | A Lagrange function is the basis-independent determinant ratio for replacing a point. Replacing a column multiplies \|det\| by \|θ_t\|; the update denominator σ = det W⁺/det W | S014 p. 32; S068 p. 5; S025 p. 18; S093 pp. 9–13; S124 pp. 7–8; S018 pp. 21–22 |
| P2 | Self-correction: the update zeroes the touched row and column of the error matrix Ξ = W − H⁻¹ and leaves the rest unchanged, so errors never grow and are erased once every point has moved | S068 pp. 6–8; S025 pp. 16–17; S045 p. 14, pp. 26–28; S124 p. 10; S018 p. 13 |
| P3 | Projection identity against rounding: Broyden's error identity, and J − H⁻¹ projected at each update | S019 pp. 24–25 |
| P4 | Representation forcing an invariant: Ω = ZSZᵀ with exactly n̂ − m̂ columns forces a zero block (proof by cofactors) | S124 p. 14; S018 p. 13; S007 p. 17 |
| P5 | Pythagorean identity for least-change projection, telescoped to vanishing changes and then a Broyden–Dennis–Moré condition, without an accurate model | S072 pp. 4–5; S045 pp. 9–10; S047 pp. 18–19; S029 p. 10; S036 p. 5; S137 pp. 17–18; S108 p. 3 |
| P6 | KKT/saddle system of the least-change problem; Lagrange functions as the columns of W⁻¹; rank-two inverse update with σ = αβ + τ² | S045 pp. 7–17; S072 pp. 10–12; S018 p. 9; S007 pp. 14–17; S047 p. 19 |
| P7 | Closed-form rounding magnitudes on a tunable geometric example (cluster radius η at distance ξ; powers M⁴, M⁶, M⁸) that set practical thresholds | S124 pp. 11–12, 15–16; S045 p. 19; S018 p. 29; S007 p. 32 |
| P8 | A cheap analytic bound replaces an expensive selection quantity | S007 pp. 19–20; S036 p. 13; S025 pp. 7–9, 22 |
| P9 | Counting and potential arguments for repair steps: a shrinking index set (3n+3), the potential Γ_k, determinant recovery, a fixed-factor gain per restart, termination via unbounded volume | S093 pp. 13–19; S067 pp. 18–19; S014 pp. 45–46 |
| P10 | Convergence under weak hypotheses: counting successes (order ℓ/log ℓ), dyadic blocks with a harmonic sum, upgrading lim inf to lim by index pairs, an up-crossing argument, the largest step fraction inside the level set | S129 pp. 7–11; S093 pp. 25–27; S030 pp. 11–12 |
| P11 | Safeguard inactivity: r_k → 1, so the trust region is inactive and the unsafeguarded rate theorem applies; a penalty parameter that stays or at least doubles is eventually constant | S030 pp. 10, 15, 18; S050 pp. 3, 6–7 |
| P12 | Normalization by invariance: affine, orthogonal or origin-shift invariance; subtract what the approximation reproduces exactly | S139 p. 3; S165 p. 5; S014 pp. 12–13; S137 p. 5; S007 pp. 19–20; S068 p. 9; S121 pp. 8–9 |
| P13 | Smallest-case reduction (n = 2 or d = 1, where the algorithm's state collapses) | S121 p. 3; S090 pp. 3, 14; R007 p. 9; S139 pp. 8–14 |
| P14 | Failure proofs in exact arithmetic: a reduction identity with geometric decay, so the total decrease is finite; an objective built from the iterates you want (functional equation); a published counterexample rebuilt as a recurrence with a closed form; number-theoretic non-repetition; counterexample search posed as a feasibility problem | S115 pp. 37–39; S139 pp. 9–10; S029 pp. 5–6; S014 p. 14; S121 pp. 22–23 |
| P15 | Equivalence theorem by induction on coinciding step QPs, so guarantees carry across a reformulation | S115 pp. 28–31 (S150 abstract) |
| P16 | Native-norm descent: each stage is an exact line search in the error semi-norm; monotonicity plus finite dimension give convergence | S075 pp. 5–6; S085 pp. 8–12; S074 pp. 13–18 |
| P17 | Operation-count bounds: rotation sequences normalized by commutation and exchange; matched floor-sum counts; cost monomials balanced by choosing parameters as powers of n | S148 pp. 8–24; S165 pp. 14–20 |
| P18 | Root-finding made robust: reparametrize the secular equation so it is convex, bracket with Newton and false position, and use a failed Cholesky as a Rayleigh-quotient lower bound | S165 pp. 6, 9–10; S186 p. 7 |
| P19 | A theory bound becomes a runtime test by estimating its unknown constant online as the largest observed ratio | S068 p. 4; S025 pp. 10, 13; S093 p. 7 |
| P20 | Induction carrying two invariants (conjugacy and eigenvectors of HG); an update derived from the invariant the proof needs | S001 pp. 2–3 |
| P21 | Range/null-space split for sufficient descent; a trapezoid expansion shows the unit step is accepted | S050 pp. 4–5, 8–9; S030 pp. 7–8 |
| P22 | Duality sign pattern linking a box-bounded dual to an ℓ₁ exact penalty; localization by X ∩ N | S167 pp. 5–8, 12, 17 |
| P23 | Kernel moment identities (Peano); geometric far-centre Vandermonde; stencils from polynomial exactness plus the PDE; all higher-order terms bounded | S090 pp. 7–12; S089 pp. 5–6, 17–21 |
| P24 | Limit set of the piecewise-linear iterate path; compactness over n+1 directions; the quadratic case as polynomial best approximation | S121 pp. 5–8; S139 pp. 7, 10–12 |

### 7.2 Algorithm-design moves

| # | Move | Where |
|---|---|---|
| A1 | Keep the framework and change one component (a shared flowchart, a restricted model space, the incumbent as a special case) | S018 pp. 3, 5; S047 pp. 3, 11; S072 p. 9; S036 p. 7; S108 pp. 2, 4; S050 pp. 2–3; S030 pp. 2–5 |
| A2 | Two radii: ρ is a never-increased lower bound on Δ; no evaluation for ‖d‖ < ½ρ; an explicit ρ-exit test | S014 pp. 26–28; S025 pp. 3, 11–14; S072 pp. 8–9; S018 pp. 4, 7, 27–29; S007 pp. 27–31 |
| A3 | Accept any decrease, so x_k is always the best point | S047 p. 6; S072 p. 2; S129 p. 2; S093 pp. 4–5; S030 p. 21 |
| A4 | Separate the two causes of a failed model step (step too long, or sample set degenerate) and give each its own remedy | S014 p. 25; S018 p. 6; S093 pp. 6–8 |
| A5 | Geometry step maximizes \|ℓ_t\| in a ball; the point to drop is chosen by \|ℓ_t\| or \|σ_t\| times a distance power, or by the largest barycentric coordinate | S014 pp. 29, 32, 34; S025 p. 18; S072 p. 12; S018 pp. 23, 27–28; S007 pp. 12–13; S093 pp. 7–8 |
| A6 | Choose the initial points so that the Lagrange functions and the inverse KKT matrix are in closed, sparse form | S068 pp. 14–15; S025 pp. 14–16; S072 p. 8; S018 pp. 8–11, 37–41; S007 pp. 4–8 |
| A7 | Origin shifts; work with differences; drop the constant term | S025 pp. 2, 14; S045 pp. 19–23; S124 p. 12; S018 pp. 15–16, 29; S007 p. 32 |
| A8 | Implicit Hessian (a base matrix plus stored multipliers on rank-one terms) | S045 p. 13; S018 pp. 16–17; S007 p. 15 |
| A9 | Solve a restricted subproblem exactly (on n+1 or m−1 lines) instead of the full one approximately | S036 pp. 9–13; S007 p. 12 |
| A10 | Guard a cheap heuristic step with an analytic lower bound and fall back to a Cauchy step; a crude solve with a proven ratio plus a logged empirical ratio | S036 p. 13; S007 pp. 12–13; S025 pp. 7–9 |
| A11 | Switch on consecutive flags (three model errors; three flags before replacing Q by Q_int) | S018 pp. 28–29, 31–32; S007 pp. 30–32 |
| A12 | Dogleg: keep Levenberg–Marquardt's bias towards steepest descent at O(n²) | S019 pp. 18–19; R007 p. 6 |
| A13 | Enlarge the radius only after two extrapolation estimates, by at most a factor of two | S019 p. 22 |
| A14 | Keep the steps spanning the space (an orthonormal recency basis with a 30° test; alpha steps) | S019 pp. 25–27; S093 p. 6 |
| A15 | Floors tied to rounding (DSTEP; no model update from shorter displacements) | S019 pp. 21, 33 |
| A16 | Model each constraint separately and use the merit function only to accept steps | S014 pp. 24, 29–30; S050 pp. 2–3, 12; S030 pp. 3–5, 21; S115 p. 40 |
| A17 | Near-active set within η₂Δ; active constraints imposed on step increments | S067 pp. 9–10 |
| A18 | A change of variables that keeps the solver's invariant and makes its linear algebra cheap | S165 pp. 12–16; S148 pp. 14–24 |
| A19 | A shift of origin instead of an unbounded penalty (augmented Lagrangian) | R007 p. 7; S137 pp. 9–10 |
| A20 | Partial or damped updates that keep positive definiteness, stating what information is lost | R007 p. 15; S137 p. 13 |
| A21 | Relax inconsistent linearized constraints to a residual bound between two computable minima | S030 pp. 2–3 |
| A22 | Write a transformed method's step as a QP in the original variables and extend the method through that QP | S115 pp. 19, 25–27 |
| A23 | Fix a free weight by scale invariance; damp the recurrence against self-reinforcement | S108 pp. 7–9 |
| A24 | An approximate solve followed by an exact minimum-norm repair | S108 p. 25 |
| A25 | Randomize the data ordering for cheap coarsening; minimax by feasibility sweeps and bisection | S074 pp. 7–8; S057 p. 17; S170 pp. 4–5 |

### 7.3 Experiment protocols

| # | Protocol | Where |
|---|---|---|
| E1 | A random family with a planted minimizer (trigonometric sum of squares, 1963–2013): 5 instances per n, the same random numbers for every variant, min–max ranges, n doubling to 320 | S001 p. 5; S019 pp. 37–38; S068 p. 12; S025 p. 22; S047 p. 14; S072 pp. 13–14; S029 pp. 10–11; S036 p. 12; S007 pp. 33–34; S093 pp. 28–29; S108 pp. 10–12; S137 p. 18 |
| E2 | Per-resolution trace: #F and the best F at each ρ | S068 p. 13; S025 p. 24 |
| E3 | Rounding probes that change nothing in exact arithmetic (§3, row 10) | S018 pp. 32, 36; S036 pp. 14, 18–19; S124 pp. 23–24; S025 p. 26; S139 pp. 5–6; S007 pp. 36, 38; S170 p. 25 |
| E4 | Fault injection and stress tests of a component: 10⁵ iterations, injected errors, a far origin, shrinking Δ, and the failing phase published | S045 pp. 29–34 |
| E5 | Follow up a surprise by removing its suspected mechanism | S047 pp. 15–16; S036 p. 11; S108 p. 12; S074 p. 26; S170 pp. 25–26 |
| E6 | One code base with the incumbent as a special case | S047 pp. 3, 11; S108 pp. 2, 10; S036 p. 11; S093 p. 28; S124 pp. 23–24 |
| E7 | Cost reporting: #F and seconds side by side; per-task timing shares; time/(n²·#F); histograms of inner work; the first evaluation with F ≤ 1.001·F_final; safeguard costs in each row; timing sweeps for the hidden constant and the crossover n; a size × n timing grid; cost-normalized units | S047 pp. 16–17; S025 p. 28; S018 pp. 34–35, 37; S067 p. 24; S007 p. 34; S148 pp. 21–22; S089 pp. 14–15; S001 pp. 3–4 |
| E8 | Failures in the main table: wrong-minimum runs marked; "?" for runs above 500,000 evaluations; non-converged runs kept; excluded variants explained; raw outliers shown; local minima listed with their F values | S001 p. 5; S025 p. 23; S018 p. 36; S075 p. 9; S036 pp. 15, 17; S108 p. 12; S067 p. 23; S007 p. 38 |
| E9 | Cases built to break one's own method | S019 pp. 39–42, 45; S055 p. 7; S075 p. 9; S085 p. 20; S170 pp. 23–24; S045 p. 33 |
| E10 | Fix the parameters before the experiments and say so | S093 p. 27; S050 p. 9 |
| E11 | Rate experiments at extreme precision (rescaling; mantissa and exponent stored separately) | S139 pp. 5–6; S108 p. 15 |
| E12 | The competitor's own test problem with the competitor's published counts (one project) | S019 pp. 37–39 |
| E13 | Write down the expected results before running the experiments | S047 p. 3; S075 p. 9 |

### 7.4 Writing moves

| # | Move | Where |
|---|---|---|
| W1 | Status labels per component, with dates ("still under development", "crude and provisional", "embarrassing") | S072 pp. 7–8, 12–15; S047 pp. 19–20; S036 p. 19; S030 pp. 5, 21; S050 p. 12 |
| W2 | A decision record: what was tried, what ruled it out, when | S067 pp. 1, 4, 16, 25, 30; S124 pp. 9, 22–24; S018 p. 15; S108 pp. 1, 13 |
| W3 | The negative result in the abstract, or what could not be proved | S108 p. 1; S115 p. 2; S067 p. 1; S139 p. 1 |
| W4 | Every constant labelled with its origin | S019 pp. 16–17, 21–23; S025 pp. 11, 14; S018 pp. 19, 23, 27–28; S007 pp. 23, 32 |
| W5 | A survey with one essay per mechanism (algorithm, best theorem, cleanest failure) and the author's opinion in the first person | S014 pp. 1, 17–18, 42–47; S029 pp. 2–11; S137 pp. 2–19 |
| W6 | First-person candour about surprises ("staggering and unexplained") | S047 p. 13; S072 p. 14; S108 p. 14 |
| W7 | Skippable proofs signposted | S045 p. 26; S093 pp. 13, 16, 20; S121 pp. 4, 10 |
| W8 | Each unusual term of an acceptance test justified by the proof that needs it, right after the algorithm | S030 p. 4 |
| W9 | Precise credit, narrow novelty claims, and a statement of how much literature was read | S115 pp. 3–4, 41; S068 p. 10; S167 p. 4; S014 pp. 34–35 |
| W10 | The scaling limit in the abstract as a number of variables tied to a cost formula | S025 p. 1 |
| W11 | A software report organized for users first; each error message written as a diagnosis | S019 pp. 9, 11, 13 |
| W12 | A numbered flowchart shared with the predecessor | S018 pp. 3, 5 |
| W13 | Open with the concrete episode that made the question urgent | S029 pp. 1–3; S014 p. 2; S089 p. 2 |
| W14 | Say where a lemma came from ("suggested by numerical calculations") | S045 pp. 26, 32; S068 p. 10 |

---

## 8. Trajectory as seen in the full texts

### 8.1 Topics by period

Carded research works by five-year period and topic; full or partial reads are in brackets. Editorial items and duplicates are excluded.

| Period | Physics | Unconstrained opt. | DFO | Constrained opt. | LP / interior point | Approximation | RBF | Nonlinear equations | Numerical linear algebra | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960–64 | 4 (0) | 2 (1) | 1 (0) | — | — | — | — | — | — | 7 (1) |
| 1965–69 | — | 2 (0) | 1 (0) | 1 (0) | — | 15 (0) | — | 1 (1) | 4 (0) | 24 (1) |
| 1970–74 | — | 11 (0) | 1 (0) | 2 (0) | — | 6 (0) | — | 1 (0) | 2 (0) | 23 (0) |
| 1975–79 | — | 6 (0) | 1 (0) | 3 (0) | — | 5 (0) | — | — | 2 (0) | 17 (0) |
| 1980–84 | — | 9 (1) | — | 8 (0) | — | 7 (0) | — | — | 1 (0) | 25 (1) |
| 1985–89 | — | 5 (0) | — | 8 (1) | 1 (1) | 1 (0) | 2 (0) | — | 2 (0) | 19 (2) |
| 1990–94 | — | — | 1 (0) | 2 (1) | 3 (0) | 3 (0) | 11 (2) | — | — | 20 (3) |
| 1995–99 | — | 2 (2) | 1 (1) | — | 1 (0) | 3 (1) | 8 (3) | — | — | 15 (7) |
| 2000–04 | — | 1 (1) | 7 (6) | — | — | — | 1 (1) | — | — | 9 (8) |
| 2005–09 | — | 1 (1) | 4 (4) | — | — | — | 2 (2) | — | — | 7 (7) |
| 2010–15 | — | 1 (1) | 3 (3) | 1 (1) | — | — | — | — | — | 5 (5) |

### 8.2 Periods and turns

| Period | Main direction | Full texts | Turn and its documented trigger |
|---|---|---|---|
| 1959–1962, Harwell | Crystal-field physics calculations [S061, S091, S101 abstract; R007 p. 5] | none | Into optimization: he programmed Davidon's method on a Ferranti Mercury in 1962 [S137 p. 4] |
| 1963–1976, Harwell | Variable metric (DFP) [S001]; derivative-free methods of 1964–65 [S002, S012 abstract]; approximation theory (15 works in 1965–69); nonlinear equations and software [S019]; augmented Lagrangian [R007 p. 7; S137 pp. 9–10]; dogleg and trust region [R007 pp. 6, 15, 19] | S001, S019 | From line searches to a step bound with one function value per iteration, "unlike earlier methods by the author", following Broyden [S019 p. 9]; the programme is stated in the conclusion [S019 p. 43] |
| 1976–1991, Cambridge (Plummer chair) | SQP and exact penalties [S050, S030]; rate theory [S139]; LP and Karmarkar [S115]; TOLMIN [S040, S071 abstract/metadata]; RBF from the mid-1980s [S090] | S139, S050, S115, S030, S090 | Into constrained optimization after 1976 [R007 p. 14]; into RBFs after a conversation with de Boor [R007 p. 21]; into Karmarkar by committing to a talk [S115 pp. 3–4] |
| 1992–2001 | RBF solvers and theory [S089, S055, S075, S085, S057]; COBYLA and the Acta Numerica survey [S014]; trust-region linear algebra [S148, S165]; the Lagrange-function toolkit for UOBYQA [S068]; DFP theory for n = 2 [S121] | 11 | Back to DFO: IMSL wrapped his gradient codes with differences, and a helicopter design problem [S029 pp. 2–3; S014 pp. 2, 45]; from linear to quadratic models because COBYLA was inadequate when second-derivative terms matter [S068 p. 4; S029 p. 9] |
| 2002–2015, retired (from 2001) | UOBYQA [S025]; least-Frobenius updating and NEWUOA [S047, S045, S072, S124, S018]; an RBF interlude [X001 p. 13; S074, S078]; essays [S029, S137]; BOBYQA [S036, S007]; family theorems [S129, S093]; θ-norm [S108]; SAO [S167]; LINCOA's step [S067] | 17 | The measured O(n⁴) cost leads to least-Frobenius updating in January 2002 [S045 p. 3; S072 pp. 7–8]; rounding failures lead to the factored Ω [S124 pp. 3, 22]; NEWUOA's success encourages bounds [S036 p. 6], then linear constraints [S067 pp. 1–2]; nonlinear constraints remain the unfinished aim [S093 pp. 30–31; S137 p. 19] |

### 8.3 What stayed constant

- **One test family for fifty years**: a sum of squares of trigonometric functions with random integer coefficients in [−100, 100] and a perturbed start [S001 p. 5 (1963); S019 pp. 37–38; S068 p. 12; S025 p. 22; S047 p. 14; S072 p. 13; S029 p. 10; S036 p. 6; S007 p. 33; S093 p. 28; S108 p. 10 (2013)].
- **A step bound with one new function value per iteration**, stated as a programme in 1968 [S019 p. 43] and realized from COBYLA to LINCOA [S093 p. 4; S029 pp. 6–10].
- **Least-change updating**, from Broyden's Jacobian update [S019 pp. 24–25] to symmetric Broyden without derivatives [S137 pp. 16–17; S045 pp. 4–5].
- **Free code with reports**, from 1968 [S019] to 2015 [S067 p. 30; S124 p. 22].
- **Evaluations as the unit of cost** [S001 p. 5; S012 abstract; S025 p. 24; S067 p. 24].
- **Counterexamples as arguments** [S019 p. 8; S139; S115; S014; S029; S072; S124; S093; S108; S067].
- **Sole authorship and short, self-weighted reference lists** in the DFO line: 12 references with 5 his own [S025 p. 31]; 10 with 4 [S047 p. 22]; 8 with 4 [S045 p. 36]; 5 with 3 [S124 p. 25; S007 p. 39]; 2 [S036].
- **Candid status**, from "tenuous" and "chosen intuitively" [S019 pp. 17, 21] through "provisional" [S050 p. 12] to "embarrassing" [S072 p. 14] and the two years of rejected work [S067 p. 30].

---

## 9. Collaboration pattern

Coauthored research works by career period (works.json authors; editorial items, multi-author volumes and duplicates excluded).

| Period | Research works | Coauthored | Coauthors (works) |
|---|---|---|---|
| 1960–1976 Harwell | 62 | 20 | A. R. Curtis 5 (S128, S177, S127, S208, S021); R. Fletcher 2 (S001, S052); J. K. Reid 2 (S056, S021); S. Marlow 2 (S161, S136); J. R. Gabriel 2, D. F. Johnston 2 (S063, S061); R. Orbach 2 (S091, S101); I. Barrodale and F. D. K. Roberts 1 (S175 = S048); others 1 each (Swann, Handscomb, Mayers, Brodlie, Madsen, Gaffney, Leask, Wolf) |
| 1977–1991 Cambridge, before DFO | 60 | 19 | Y. Yuan 3 (S149, S050, S030); Ph. L. Toint 2 (S042, S150); R. M. Chamberlain 2 (S027, S153); I. C. Demetriou 2 (S076, S095); others 1 each (Iserles, Martin, Jacobson, Lemaréchal, Pedersen, Sabin, Hopper, Roberts, Cullinan, Ge, Håvie, Cheney, Buhmann) |
| 1992–2001 | 31 | 7 | R. K. Beatson 4 (S043, S134, S088, S087); A. C. Faul 2 (S075, S085); I. C. Demetriou 1 (S142); G. Goodsell 1 (S087) |
| 2002–2015 | 17 | 2 | A. C. Faul, G. Goodsell (S074); R. K. Beatson, A. M. Tan (S078): RBF only |

- **Overall**: 48 of 170 research works are coauthored (28%), in line with Powell's own estimate: "Relatively few of my papers are written with other authors, I would think fewer than fifty percent probably" and "I collaborate far less than other people" [X001 p. 14]. Every DFO paper read is sole-authored [S014, S068, S025, S047, S045, S072, S124, S018, S029, S036, S007, S093, S108, S067]. The late coauthored papers are all RBF papers with Cambridge or Canterbury colleagues [S074, S078].
- **Recurring partners by line**: Curtis (Harwell approximation and sparse Jacobians); Yuan and Toint (PhD students; SQP/trust regions and sparse Hessians) [R007 pp. 15–16]; Demetriou (research student; data smoothing) [R007 p. 19]; Beatson and Faul (RBF solvers) [S075; S085; S074; S078]; Fletcher (DFP) [S001].
- **Stated**:
  - Most papers are single-authored by choice, and he is usually not a coauthor of his students' papers [X002 p. 5].
  - He had "about 18 research students" and published with "about a third" of them [X001 p. 14].
  - He coauthored with Iserles only because Iserles insisted [X001 p. 15].
  - "I'd quite like to crack them myself" [X001 p. 14].
  - Visitors should work on their own project, with contact "maybe once a month" [X001 p. 15].
- **Reported**: a self-declared loner who read and annotated everything junior colleagues wrote [R007 pp. 10–11]; he avoided committees and pruned his scope to "optimization only" [R007 pp. 12, 23].
- **Credit practice**: acknowledgements name the exact contribution of each group member [S055 p. 17; S075 p. 10]. He recorded a student's unpublished idea himself [S014 pp. 34–35]. Disclosure of prior art led him to replace his own proofs by citations [S167 p. 4].

---

## 10. Rejected updates

1. **A separate method for "exact-arithmetic-invariant rounding probes"** (Q9, 9 works). It says the same thing as M4 step 4 with a better protocol; folded (§3, row 10).
2. **A separate method for "judge a model by its steps"** (Q10, 9 works). It is M3's rationale; folded (§3, row 5).
3. **Separate methods for stability-by-design (Q8) and for status and rejected alternatives (Q6, Q7).** They pass the four checks, but a separate method would duplicate M4 and M5 and break the cap; merged (§4.2).
4. **Self-derivation over the literature as a Core Research Method.** It is taste and working style, not a research step; routed to Research Taste (§4.2). Advising students to skip the literature would also transfer poorly; Powell himself names the cost [X002 p. 5; S115 p. 41].
5. **Replacing M2's "resolution" framing by "noise robustness".** Both readings are in the texts [S025 pp. 3, 14; S018 p. 4]; add, do not replace (§3, row 3).
6. **Recording the memoir's framing that Powell published DFO convergence papers in 2003 and 2012.** Only S093 (2012) has a convergence theorem; S047 has none [S047 pp. 3, 11]. Only the S093 qualification is carried forward (§3, row 18).
7. **Naming A. C. Faul or G. Goodsell as Powell's students.** The files read do not say so [S075 header; S055 p. 17].
8. **Heuristics for cost-monomial balancing, timing sweeps and "advocacy rewrite".** They come from one project (S148/S165) and are listed as techniques only.
9. **Heuristics for "return by-products for diagnostics" (Q22) and "benchmark on the competitor's problem" (Q32).** Harwell-era, one or two cards; covered by M5 and Workflow B.
10. **Any RBF-specific pattern** (Q24–Q26) as a SKILL.md item. The lens is DFO; these stay in the inventory.
11. **"Referee by checking every line" as a heuristic.** One stated source [X002 p. 5]; a Mentor Voice remark at most.
12. **Anything derived from the cards' reading notes** (typos, a table that differs between two reports, the wording of an abstract). These are not findings about Powell or his coauthors. The neutral lesson "check that published tables, text and code agree" is already Heuristic 9 and Workflow E step 4.
13. **Abstract-only clusters** (Q27, Q28, the 13 abstract singletons). They are below the read threshold, and no method evidence is built on them.

---

## 11. Open gaps

- **1969–1982 has no full text.** COBYLA (S008, abstract only), TOLMIN (S071 metadata; S040 abstract), the 1970 hybrid and trust-region papers (S011, S015 metadata), the 1978 SQP papers (S003, S013 metadata; S016 abstract), the augmented Lagrangian (S004 metadata), the watchdog technique (S027 abstract), the convergence papers of 1975–84 (S024, S028 metadata; S033 abstract), the 1972 and 1981 books (S199 metadata; S009 abstract) and the 1987 and 1990 RBF reviews (S005 metadata; S010 abstract) are known only from abstracts, from Powell's later surveys [S014; S029; S137] and from the memoir [R007]. The following is therefore uncertain:
  - whether Method 7's loop and the counterexample-per-rule habit worked the same way in the SQP and convergence-theory years (the abstracts suggest so [S020, S026, S049, S051], but no text was read);
  - where the DELTA half of Method 2 originated. The trust region "pioneered in [10]" and the ratio test rest on the memoir [R007 pp. 15, 19]; the 1970 papers were not read;
  - how COBYLA's constants and rules were chosen. The account is secondhand [S014 pp. 24–30, 45; S029 pp. 6–9];
  - Method 6 between 1970 and 1992. The code reports (VF02AD, VMCWD, ZQPCVX, TOLMIN) are titles or abstracts only [S081, S059, S058, S071].
- **LINCOA was never described in a paper**; only its trust-region step was [S067 p. 30]. BOBYQA exists only as a report [S007].
- **The order of the RBF attempt relative to COBYLA**: the memoir places the RBF attempt first and the polynomial-interpolation codes after it [R007 pp. 17, 21]; Powell's own accounts of COBYLA's origin do not mention it (§3, row 17).
- **Partially read works**: pages named on each card were skipped [S057 pp. 14–16; S074 pp. 9–12, 14–17, 19–20; S078 pp. 6–18, 28–30; S121 pp. 12–21; S170 pp. 15–20]. Some figures cannot be read in the extractions [S067 p. 23; S085 p. 20; R007 figures], and some constants cannot be read either [S068 p. 11; S030 p. 4].
- **Supervision** is known from the interviews and the memoir only [X001 pp. 14–15; X002 p. 5; R007 pp. 10–12]. There is no recollection written by a student other than the memoir, two of whose authors are named as his students (Toint [R007 p. 15]; Buhmann, by an interviewer [X001 p. 13]).
- **Reception and benchmarks** (Moré–Wild 2009, PRIMA, PDFO) are outside Powell's texts and stay secondary. Powell's own DFO papers compare only against his own earlier methods (§3, row 13).
- **Talks known only by title**, for example the 2011 lecture "A parsimonious way of constructing quadratic models …" [R007 p. 16 caption], were not read.
