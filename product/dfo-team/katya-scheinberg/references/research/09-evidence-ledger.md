# Katya Scheinberg · Evidence ledger

> Date: 2026-09-27. The full evidence behind `SKILL.md`. When SKILL.md was tightened on 2026-09-27 (17136 words before, 11995 after; 12376 after the review fixes, which put the Method 1 thresholds, some Method 3 devices and the Workflow B settings table back in SKILL.md, so those also appear there), every long evidence list, per-paper case list, say–do tally, variant or contradiction explanation and long anatomy row was moved here **verbatim**. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant/correction bullets, and a link to the matching section below. Nothing here is new: each section reproduces the SKILL.md item as it stood before tightening, including its cross-references ("Corrections log" there is the section [Corrections from the full texts](#corrections) here). **Exception (k01):** lines marked **(k01)** and the section [Book material](#book-material) were added on 2026-09-27, when the open material of the 2009 IDFO book (batch `k01`, cards B001–B006) was integrated; they are new evidence, not moved text (SKILL.md 12376 words before that integration, 12759 after).

**How to read.** `[card S012, pp. 20–21]` is paper card S012 in `07-paper-cards.md`, at the PDF page of the version named on the card (usually arXiv); look up the journal page before citing it in a paper. S043 and D001 are one paper and are cited as D001. Heuristic numbers are the 2026-09-27 numbering; the cards use the old numbers (mapping in `08-deep-reading-synthesis.md` §12). Say–do counts are distinct papers read in full or in part (the five same-text pairs counted once); a paper can count as both evidence and variant, so the parts can sum to more than the total. Per-card method links (✅ evidence, ⚠ variant, ✗ contradiction) are in the `Methods linked` column of `07-paper-cards.md`; the synthesis is `08-deep-reading-synthesis.md`; named proof devices, experiment protocols and writing moves are in `../technique-catalog.md`.

**Scope.** Sections exist for the SKILL.md items that were condensed: the two taste lists and the taste quick-check, Methods 1–6, the routing table, the fact-finding step of the agentic protocol, Workflows A–H (Workflow B includes the published starting-settings table), Heuristics 1–10, the three signature-work anatomies, the anti-patterns table, the research-trajectory prose and Latest list, the academic lineage, the inner tensions, the mentor-voice questions, the corrections log and the card key. Items not listed (frontmatter, How to Use, activation rules, student mode, integrity rules, the rest of the agentic protocol, roundtable card, honest boundary apart from its corrections list, source lists) were not condensed and remain complete in SKILL.md.

## Contents

- [Research task routing](#routing)
- [Agentic protocol: Step 2: Scheinberg-style fact finding (use tools, never memory)](#agentic-protocol)
- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Taste quick-check](#taste-quick-check)
- [Core research methods: counting note](#methods-note)
- [Method 1: Oracle contract ("accurate enough, often enough")](#method-1)
- [Method 2: Keep the classical adaptive method; change only what the weaker oracle breaks](#method-2)
- [Method 3: Analyse the algorithm as a stochastic process and demand deterministic-order complexity](#method-3)
- [Method 4: Geometry is the price of model-based DFO; pay only the minimum](#method-4)
- [Method 5: Compare estimators head-to-head at equal accuracy (theory + experiment)](#method-5)
- [Method 6: Exploit structure before going generic](#method-6)
- [Workflow A: Oracle audit & problem framing](#workflow-a)
- [Workflow B: Algorithm design for noisy / stochastic DFO](#workflow-b)
- [Workflow C: Probabilistic complexity analysis](#workflow-c)
- [Workflow D: Estimator & experiment design](#workflow-d)
- [Workflow E: Reviewing a DFO / zeroth-order paper or draft](#workflow-e)
- [Workflow F: Complexity proof scaffold (student mode)](#workflow-f)
- [Workflow G: Pre-meeting self-review (student mode)](#workflow-g)
- [Workflow H: Measuring a theorem (tightness and theory-vs-practice probe)](#workflow-h)
- [Heuristic 1: random models, gradients or function values](#heuristic-1)
- [Heuristic 2: skipping geometry-improving steps](#heuristic-2)
- [Heuristic 3: noisy evaluations and gradient estimates](#heuristic-3)
- [Heuristic 4: from expected to high-probability and sample complexity](#heuristic-4)
- [Heuristic 5: bounded noise, biased or inconsistent oracles](#heuristic-5)
- [Heuristic 6: dimension too large for full interpolation models](#heuristic-6)
- [Heuristic 7: heavy-tailed or corrupted oracles](#heuristic-7)
- [Heuristic 8: check an existing framework before a new proof](#heuristic-8)
- [Heuristic 9: measure every threshold and constant](#heuristic-9)
- [Heuristic 10: a failed extension becomes a named open problem](#heuristic-10)
- [Signature work: anatomies kept elsewhere](#signature-note)
- [Signature work: Stochastic optimization using a trust-region method and random models (Mathematical Program…](#signature-storm)
- [Signature work: Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimi…](#signature-self-correcting-geometry)
- [Signature work: High probability complexity bounds for adaptive step search based on stochastic oracles (SI…](#signature-adaptive-step-search)
- [Research anti-patterns (full sources per row)](#anti-patterns)
- [Research trajectory: full-text view, recognition and latest](#research-trajectory)
- [Academic lineage](#academic-lineage)
- [Inner tensions](#inner-tensions)
- [Mentor voice](#mentor-voice)
- [Book material (IDFO 2009): what was read and what it supports](#book-material)
- [Corrections from the full texts](#corrections)
- [Card key (ids used in SKILL.md before tightening)](#card-key)

<a id="routing"></a>

## Research task routing

| User task | Workflow | Methods |
|---|---|---|
| "Is this problem a DFO problem? What should I even assume?" | Workflow A: Oracle audit & problem framing | Method 1, Method 6 + Taste quick-check |
| "Which algorithm should I use / design for my noisy black box?" | Workflow B: Algorithm design | Method 2, Method 4, Method 1 |
| "How do I prove convergence / complexity?" | Workflow C (Workflow F for the detailed scaffold) | Method 3, Method 1 + Heuristic 8 |
| "Does an existing framework already cover my algorithm?" | Method 3 step 1 + `references/proof-playbook.md` §0 | Heuristic 8 |
| "Which gradient estimator / how many samples / what radius?" | Workflow D: Estimator & experiment design | Method 5, Method 1 |
| "How tight is my bound? Does practice match the theory?" | Workflow H: Measuring a theorem | Method 3, Method 5 + Heuristic 9 |
| "Review my DFO / zeroth-order paper" | Workflow E: Review | All methods + Anti-patterns |
| "My method stalls / is noisy / radius collapses" | Workflow B (steps 4–6) + Heuristics 2, 5 | Method 2, Method 4 |
| "My proof breaks at one inequality" | Workflow F step 2 + `references/proof-playbook.md` §0.2 (symptom → device) | Method 3, Method 2 |
| "Which proof trick / experiment protocol / writing move fits here?" | `references/technique-catalog.md` | — |
| (Student) "Prove complexity for my algorithm" | Workflow F: Complexity proof scaffold + `references/proof-playbook.md` | Method 3, Method 2, Method 1 |
| (Student) "Pick / scope a thesis problem" | `references/open-problems.md` + Taste quick-check, then Workflow A on the chosen row | Method 1, Method 3, Method 4 |
| (Student) "Prepare a draft / result for a supervisor meeting" | Workflow G: Pre-meeting self-review | All methods |
| (Student) "What should I read?" | `references/reading-path.md` (stage by current task) | — |
| Writing style, mentoring, lab organisation, grants | No distillable public Scheinberg method for mentoring, lab organisation or grants. Paper-writing moves from the full texts are in `references/technique-catalog.md`. Otherwise give generic advice labelled "not Scheinberg-style". In student mode, point to the user's own notes in `references/sources/private/` | — |

<a id="agentic-protocol"></a>

## Agentic protocol: Step 2: Scheinberg-style fact finding (use tools, never memory)

Check the local corpus first: `references/research/07-paper-cards.md` indexes 125 cards (78 papers read in full or in part) with page references, and `references/technique-catalog.md` lists the devices by name. Then use WebSearch / arXiv / publisher pages / GitHub to check:
- **Oracle facts**: Is the noise in the black box deterministic (numerical) or stochastic (sampling)? Is it biased (smoothing and finite-difference bias, simulation bias)? Can the user control sample size per evaluation? What does one evaluation cost?
- **Classical baseline**: Which classical adaptive method (trust region, Armijo backtracking, Powell-style interpolation code) already fits? Check that the solver exists and is maintained (e.g., PDFO, Py-BOBYQA, DFO-LS on GitHub).
- **Known guarantees**: Is there a probabilistic-model or high-probability complexity result for this oracle class? Check the verified list in `references/sources/RESOURCES.md` and the card index first, then search.
- **Structure**: Is the objective least-squares, separable or composite, or does it have a known component?
- **Competing estimators**: What do the ML papers in the user's area use (Gaussian smoothing, evolution strategies)? This sets up the head-to-head comparison.

Keep search results internal. The user sees the judgement and the next steps.

<a id="taste-marks"></a>

## Taste: marks of good research

Evidence below is from the full texts. Abstract-level evidence was dropped wherever a full-text line exists (it stays in `references/research/02-methodology.md` and `06-trajectory.md`); corrections are in the Corrections log at the end of the Honest Boundary.

1. **The problem is defined by an oracle contract, not by a noise story.** A good paper says what accuracy each estimate needs, relative to the current step or radius, and with what fixed probability.
   - Evidence: events I_k (model good) and J_k (estimates good) with fixed conditional probabilities [card S012, pp. 3, 8–9]; "The key to the analysis lies in the assumption that the accuracy improves in coordination with the perceived progress of the algorithm." [card S013, p. 11]; one oracle language used to restate all prior work [card S041, pp. 2–7].
2. **Deterministic parity.** A stochastic or derivative-free result counts when its complexity has the same order as the deterministic or best-known method, with randomness costing only constants.
   - Evidence: every rate theorem is followed by a remark reading the ε-order against the deterministic method [card S014, pp. 16, 19, 20, 26]; zero the noise and probability parameters and the deterministic bound returns [card S026, pp. 13, 20, 22–23]. Variant: for sample complexity the yardstick is the stochastic lower bound [card S057, pp. 2, 15–16, 19]; for comparison oracles, matching minimax lower bounds [card S087, pp. 23–26, 41–43].
3. **Classical adaptive methods are analysed, not replaced.** Trust region, Armijo backtracking and Powell-style interpolation are kept, and new theory is built under them.
   - Evidence: "almost identical to the classical method" [card S018, p. 1]; the relaxed acceptance test is "the major difference" [card S041, p. 11]; Powell's method kept with the criticality step swapped for one test [card S104, p. 4]. **Scope**: the adaptive / DFO line; the SARAH and SGD papers (2017–2022) are a parallel programme outside this lens [cards S002, pp. 2–3, 7; S009, pp. 3, 5].
4. **A guarantee comes with numbers, in algorithm and software papers.** Theory is paired with head-to-head numerical comparison where a method or code is proposed [cards S012, pp. 27–32; S041, pp. 30–36; S104, pp. 26–30]. Pure-analysis papers are theory-only and leave numerics to companion papers [cards S083; S088, p. 19; S093, p. 3]; one states its objective as understanding rather than a practical scheme [card S030, p. 4].
   - **(k01)** ⚠ Variant, peer view: both reviewers of the 2009 book note few numerical illustrations or examples and no implementation detail [cards B005, pp. 2–3; B006, p. 2]; the book is a theory monograph, which fits the C1 scope.
5. **Find the minimal safeguard, backed by a negative result.** Show what cannot be dropped, then pay for it as rarely as possible.
   - Evidence: "it turns out that it is not necessary to compute extra sample points unless the gradient of the model becomes small." [card S143, p. 4]; geometry steps cannot be eliminated but can be confined to the criticality step [card S030, pp. 3, 8–15]; the Λ-dependence of the error bound shown tight, so Λ = 1 + O(1/n) is the minimum [card S088, Thm 4.6, pp. 11–12].
6. **DFO and ML zeroth-order optimization are one field.**
   - Evidence: the ML estimator with orthonormal directions rewritten as classical interpolation [card D003, pp. 6–7]; RL benchmarks and an ML co-author [card S006, pp. 2–3, 31]; the tutorial explains ML optimization to an OR audience [card S031, p. 2].
7. **Guarantees get stronger over time**: almost-sure, then expected, then high-probability tail bounds.
   - Evidence: almost sure [card S018, pp. 10–11] → expected [cards S014, p. 13; S013, pp. 5–10] → high probability [cards D001, pp. 7–13; S041, pp. 16–21] → total sample complexity [card S057, pp. 12–13] → heavy tails and corrupted inputs [card S083, pp. 16–17].
   - **(k01)** Dating: the 2009 book is the global-convergence rung for model-based DFO; every guarantee named in its table of contents is global convergence and no title mentions complexity or rates [card B001, pp. 2–3]; complexity for these methods arrives with S088 and S104.
8. **A new variant costs a checklist, not a new proof.** Good work leaves behind an abstract object (a model class, a process with axioms) that later algorithms plug into (→ Heuristic 8).
   - Evidence (all within the group's own papers): the Jin–Scheinberg–Xie process imported by stochastic cubic regularization [card S093, p. 10]; the renewal-reward theorem imported by the line search [card S015, pp. 7–8] and ProxSTORM [card S098, pp. 19–20]; Cartis–Scheinberg counting reused in composite and Powell-style papers [cards S068, pp. 7–9; S104, Thm 5.12].
9. **Prior work is positioned by its assumptions, not attacked.** Earlier papers, including the group's own, are restated in one oracle language and criticised for what they assume; a concurrent paper's advantage is conceded.
   - Evidence: prior assumptions drawn as sets on the accuracy–probability plane [card S041, pp. 2–7]; the group's own earlier papers listed with the assumption each new result removes [card D001, pp. 2–3]; a concurrent method credited, its advantage conceded [card S012, pp. 5–6]; a competitor's encouraging results credited, then a 2-D counterexample shows its method can converge to a non-stationary point [card S143, p. 4].

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

1. **A stochastic method with a hand-tuned step schedule** where an adaptive classical method would do. ADAM's best learning rate shifts across problems [card D001, p. 28]; tuning cost is the entry point of the 2020 overview [card S047, pp. 1–2]. Variant: the group's own SGD analyses use schedules computed from known μ and L [card S009, pp. 2, 5, 13], so the warning is about hand tuning, not about every prescribed schedule.
2. **Assuming unbiased, well-behaved estimates** when the estimator is biased by construction, as finite differences and smoothing are. With biased computation-failure noise, Monte-Carlo averaging is not a correct approach [card S012, p. 26]; randomized finite differences carry a fixed bias set by σ [card D001, p. 25]; the frameworks allow bias [cards D001, pp. 1–2; S041, p. 4].
3. **Comparing gradient estimators without fixing the accuracy target and the sample and radius budget** (FoCM 2022 compares them by derived sample counts and radii [card S006, pp. 4–5, 25]).
4. **Dropping geometry safeguards in model-based DFO without an argument** (Scheinberg–Toint 2010 [card S030, pp. 8–11]).
5. **Only almost-sure or expected results for a method sold as practical**, where a single run matters (the 2019 → 2024 progression to tail bounds).
6. **Complexity claims that hide the dependence on the success probability or the dimension** (Cartis–Scheinberg 2018 make the p-dependence explicit [card S014, p. 13]; the 2025–2026 DFO papers track n [cards S088, pp. 9–11; S104, p. 16]).
   - **(k01)** ✅ weak: the 2011 addendum keeps n^{1/2} and p̄^{1/2} (p̄ = n(n + 1)/2) in every constant of the quadratic-regression bounds [card B004, p. 2], and the second-printing erratum adds the missing definition of p̄ [card B003, p. 1].
7. **Sample-size rules written in quantities the algorithm cannot know** (the true gradient norm, the target ε). The papers state every rule in α_k, ‖g_k‖, Δ_k and variance bounds, and criticise competitors that do not [cards S015, pp. 2, 7; S013, pp. 19–20; S047, p. 9].
8. **An iteration bound presented as if it were a cost bound.** The step parameter is not bounded away from zero, so the sample cost needs its own proof [cards S057, pp. 1–2; S041, p. 3; S137, pp. 1, 3].
9. **Thresholds and constants that were never computed or measured.** The group plugs textbook constants into its conditions and sweeps experiments across the theoretical threshold [cards S012, pp. 20–21, 30–32; S041, pp. 30–33].

<a id="taste-quick-check"></a>

## Taste quick-check

- [ ] Can you write the oracle contract: accuracy required per iteration (tied to the step or radius) and the probability it holds?
- [ ] Is every sample-size rule written in quantities the algorithm knows?
- [ ] Is there a classical adaptive method (trust region, line search, Powell-style interpolation) you can keep instead of inventing a new one?
- [ ] Is there a published framework whose hypotheses your algorithm already satisfies (→ Heuristic 8)?
- [ ] Does the expected result match the deterministic order in ε, with randomness costing only constants?
- [ ] Are bias and irreducible noise handled, with convergence to a stated neighbourhood rather than claimed exactly?
- [ ] Will you compare against competing estimators or solvers at equal accuracy, counting function evaluations?
- [ ] Does any structure (least-squares residuals, low rank, separability, a known prox term) beat treating the objective as a scalar black box?
- [ ] Can the result be pushed from expected to high-probability complexity, and from iterations to samples?

<a id="methods-note"></a>

## Core research methods: counting note

Say–do counts are distinct papers read in full or in part (the five same-text pairs counted once). A paper can count as both evidence and variant, so the parts can sum to more than the total. Variants, deterministic ancestry and per-paper detail are in `references/research/08-deep-reading-synthesis.md` §2–3.

<a id="method-1"></a>

## Method 1: Oracle contract ("accurate enough, often enough")

**One line**: Define the problem by what each estimate (function value, gradient, model) must satisfy, with accuracy scaled to the current step size or trust-region radius, and the fixed probability with which it must hold. Design the algorithm after that, not before.
**Evidence**:
- Stated: random-model results need sample sizes tied to the step length or radius [card S031, pp. 21–22]; accuracy scaled to Δ_k or α_k‖g_k‖ with probability 1 − δ, and substituting ε for the unknown gradient norm criticised as over-conservative [card S047, pp. 8–9, 12]; the limitation that "it is not necessarily easy to estimate what these probabilities ought to be" [card S012, p. 3]. The oracle talk (2021–2025) gives a general definition of a stochastic oracle (abstract level).
- Practice: I_k and J_k with accuracy ∝ δ_k and δ_k², fixed probabilities conditioned on the past [card S012, pp. 3, 8–9]; SZO/SFO contracts with bias allowed, built from mini-batches and randomized finite differences [card D001, pp. 1–2, 4, 24–25]; irreducible floors ε_g, ε_H [card S041, pp. 2, 4–5, 21]; corrupted gradients and heavy-tailed values [card S083, pp. 2–5, 15].
- Say–do consistency: ✅ stated + practiced; 48 papers touch this method (26 evidence, 30 variant, 0 contradiction). No talk transcript was read.
- **(k01)** ⚠ Deterministic precursor: the 2009 book's fully linear and fully quadratic models (§6.1) and its "Conditions on the trust-region models" (§10.2) name the certified class that BSV 2014 requires only with probability p; the 2011 addendum's Hessian, gradient and value errors of order Δ, Δ², Δ³ are that certified accuracy; no title mentions probability [cards B001, pp. 2–3; B004, p. 2].
**Steps**:
1. List the oracles you actually have: f̃(x) (and the cost of one sample), g̃(x) or the ability to build a model from samples, and possibly a Hessian estimate. Expect an accuracy hierarchy: function estimates need tighter accuracy than models (ε_F δ_k² against κ δ_k), and Hessians looser than gradients [cards S012, p. 9; S013, p. 14; S031, p. 22].
2. Write the contract per iteration k. The model or gradient error is ≤ κ·Δ_k (trust region) or ≤ κ·α_k‖g̃‖ (step search), with probability ≥ p. The function-estimate error has a matching bound tied to Δ_k or α_k. Write it in quantities the algorithm knows (α_k, ‖g_k‖, Δ_k, variance bounds), never in the unknown ‖∇f(x_k)‖ or the target ε [cards S015, pp. 2, 7; S013, pp. 19–20; S047, p. 9]; the constants may stay unknown to the method, with only an upper bound ε′_f as an input [card D001, p. 4]. When only differences matter, put the contract on the reduction difference |ared − cred| ≤ η·pred_k [cards S098, pp. 3, 7; S083, p. 3].
3. Separate *controllable* error (reduced by more samples or a smaller sampling radius) from *irreducible* error (numerical noise, bias floor). The irreducible part fixes the neighbourhood you can reach. Say so up front. Published floors: ε ≥ O(√ε_f) + O(ε_g) for first-order trust region [card S041, p. 21]; O(ε_f^{2/3}) for cubic regularization [card S093, p. 9]; ε ≥ Ω(√(n·ε_f)), i.e. √n·√ε_f, for model-based DFO [card S104, pp. 16, 22].
4. Compute what it costs to meet the contract, e.g. samples per iteration as a function of Δ_k and the variance, and check that the total budget is feasible: O(σ_f²/Δ_k⁴) function samples and Õ(σ_g²/Δ_k²) gradient samples for STORM [card S013, pp. 19–20]; O(Δ_k^{-2}) with common random numbers when the contract is on differences [card S098, pp. 22–23].
5. Check that the probability threshold the analysis needs is attainable. If p cannot be certified, plan a stronger-assumption fallback or empirical calibration. Thresholds differ by paper: αβ ≥ 1/2 suffices for STORM's liminf step, while its almost-sure theorem needs α, β close to 1, (1 − α)(1 − β) ≤ 1/440 with textbook constants [card S012, pp. 20–22]; p_g ≥ 16/17 for the stochastic line search [card S015, p. 16]; p > 1/2 + r/h(ᾱ) for high-probability step search [card D001, p. 7 (Assumption 3); Thm 3.6, p. 10]; p > 1/(m + 1) with asymmetric step factors and exact values, plus 4mε_f/h(ε) under noise [card S083, pp. 15, 22]. Where you choose the parameters, turn the threshold into a design rule: make γ_inc > γ_dec so that p·ln γ_inc + (1 − p)·ln γ_dec > 0 for a conservative p [card S083, p. 15]; raise the step-decrease factor when p is low [cards S137, pp. 4–5; S057, p. 9]. Experiments succeed far below the theoretical thresholds (α ≈ 0.27) [card S012, p. 31].
**Applies to stage**: problem framing; algorithm design; analysis setup.
**Different from standard practice**: standard stochastic practice fixes a noise model (unbiased, bounded variance) and designs variance reduction or step schedules. Here the requirement adapts with the step size, bias is allowed, and occasional arbitrary failures (probability 1−p) are tolerated. Scope by method and order: in first-order trust region (STORM, Blanchet et al.) both model and function-estimate failures may be arbitrary, with probability 1 − α and 1 − β, because the true change on a wrongly accepted step is bounded through ‖s_k‖ ≤ δ_k and L-smoothness [cards S012, p. 3; S013, p. 17]. Second-order trust region (E|F − f| ≤ κ_F δ_k³ [card S013, p. 28]), the line search (a variance condition [card S015, pp. 5–7, 14]), high-probability step search (mean plus subexponential tail [card D001, pp. 1–5]) and heavy tails (q-th moments [card S083, pp. 16–17]) add a bound on function-estimate errors.
**Limitations**: p is rarely known in practice, as the papers themselves say [cards S012, p. 3; S083, pp. 15, 22; S098, p. 16]. The contract presumes you can control sample sizes. The verified work assumes smooth objectives. Constants that depend on p can dominate on small budgets.

<a id="method-2"></a>

## Method 2: Keep the classical adaptive method; change only what the weaker oracle breaks

**One line**: Start from the method practitioners already trust (trust region, Armijo backtracking, cubic regularization, Powell-style interpolation). Rerun its proof under the weaker oracle and change only the piece that fails.
**Evidence**:
- Stated, from 2006 on: "The method itself is not new (see Nocedal and Wright, 1999). Our contribution is to adapt it to the SVM framework and provide an efficient implementation." [card S022, p. 3]; SG is non-adaptive and tuned per application, and the stochastic algorithm "has the same structure" as the deterministic one [card S047, pp. 1–2, 7]; "The major difference pertains to the fact that the step acceptance criterion is relaxed." [card S041, p. 11].
- Practice: only the ‖g_k‖ ≥ η₂δ_k condition added [card S018, pp. 1, 8]; the Armijo test changed only by +2ε_f [card S026, pp. 4–5, 16]; Powell's method kept, criticality step swapped for ‖g‖ ≥ η₂Δ [cards S104, pp. 4, 18, 24–25; S088, pp. 2–3]; the "three important aspects" where the standard trust-region proof breaks, and only those re-proved [card S008, pp. 17–18]; the essay's new algorithm differs from the CSV framework only in Steps 1, 4b and 5 (reader's comparison of its Algorithms 3.1 and 5.1) [card S143, pp. 3–5].
- Say–do consistency: ✅ stated + practiced; 64 papers touch this method (52 evidence, 11 variant, 2 contradiction). The contradictions are the SARAH papers (a new estimator with a constant, tuned step) [cards S002, pp. 2–3, 7; S024, pp. 3, 8]; the method is scoped to the adaptive / DFO / classical-algorithm line.
- **(k01)** Peer view and book organisation (co-authored, title level): reviewer D. Orban notes "the clearly stated similarities and differences between trust-region methods for smooth problems and for derivative-free problems" and reads the chapters against Conn–Gould–Toint's *Trust-Region Methods* [card B006, p. 2]; J. L. Nazareth: two trust-region frameworks with global convergence proofs are the basis of the "DFO" approach, Powell's methods and wedge methods [card B005, p. 2]. The table of contents states the framework and its conditions on the models (§§10.1–10.2) before the instances (Ch. 11), and repairs Nelder–Mead into a globally convergent variant (§8.3) rather than replacing it [card B001, pp. 2–3].
**Steps**:
1. Pick the classical method that already works for the deterministic version of the user's problem.
2. Rerun its deterministic convergence proof, substituting the Method 1 contract. Mark the **first inequality that fails**. If the deterministic proof is not in the form the stochastic proof needs, rewrite it first, e.g. around a measure that decreases on every iteration [cards S047, p. 3; S068, pp. 14–15].
3. Design the smallest repair for that inequality. Verified repairs: +2ε_f in the Armijo test or the numerator of ρ_k [cards S026, pp. 4–5; S041, p. 11]; the ‖g_k‖ ≥ η₂δ_k acceptance test [card S018, p. 8]; a second control δ_k for estimate accuracy [card S015, pp. 3–4]; letting FISTA's step grow through a θ_k bookkeeping [card S068, pp. 5, 14–15]; a gate ‖g_k‖ ≥ ε_rej that blocks step increases on small gradients [card S083, pp. 8–9].
4. If a safeguard looks removable, try to prove it is. If you cannot, prove a negative example and then confine the safeguard to where it is needed (the Scheinberg–Toint 2010 pattern). Use the smallest instance that breaks the unguarded method: a hand-checkable 2-D run whose outcome does not depend on the replacement rule [cards S143, pp. 4–5; S030, pp. 8–11], or a 3×3 / 2×2 example [card S048, pp. 6–7, 10–11].
5. Keep the classical defaults (radius-update factors, Armijo constant) in experiments, so the comparison isolates the oracle change. Implementing inside the strongest baseline's code, with its defaults, does the same [card S023, pp. 16–17].
**Applies to stage**: algorithm design; debugging a stalling method.
**Different from standard practice**: the usual reflex is either a bespoke algorithm for each noise setting or SGD with a tuned schedule. This lens keeps the trusted algorithm and moves the novelty into the oracle condition and the analysis.
**Limitations**: the result inherits the classical method's scope (local, smooth, mostly unconstrained). It may leave performance on the table compared with bespoke methods such as momentum or acceleration; the verified work covers FISTA with backtracking in the convex composite case [card S068, pp. 15–21] and finds that acceleration may not help proximal quasi-Newton methods [card S054, pp. 1, 22, 29]. It does not describe the group's variance-reduction papers.

<a id="method-3"></a>

## Method 3: Analyse the algorithm as a stochastic process and demand deterministic-order complexity

**One line**: Model the iterates, step-size parameter and success indicators as a random process. Bound the expected stopping time, strengthen it to a high-probability tail bound, and require the ε-order to match the deterministic method.
**Evidence**:
- Stated: methods with random estimates "retain their convergence rates" [card S031, p. 21]; step-size parameters "are not bounded away from zero due to possible oracle failures" [card S057, p. 1]; "By contrast, in the framework presented here, the analysis is structured around a measure in which progress is made in all iterations." [card S047, p. 3]. The talk "Overview of Adaptive Stochastic Optimization Methods" (2022–2023) makes the same argument (abstract level).
- Practice: (a) potential νf + (1 − ν)Δ², renewal-reward stopping time with p/(2p − 1) [card S013, pp. 5–10, 14–15]; (b) counting with 2p/(2p − 1)² [card S014, pp. 7–16]; (c) high-probability tails by counting and concentration [cards D001, pp. 7–13, 17; S041, pp. 16–21; S083, pp. 10–22]; step-parameter lower bound → sample complexity [cards S137, pp. 4–5; S057, pp. 7–13].
- Say–do consistency: ✅ stated + practiced; 34 papers touch this method (17 evidence, 23 variant, 0 contradiction). Most variants are deterministic precursors or a different proof skeleton.
- **(k01)** ⚠ Dating: in the 2009 book every named guarantee is global convergence (§§7.3, 7.4, 8.3, 9.2, 10.4, 10.6); no title contains complexity, rate or worst case [card B001, pp. 2–3].
**Steps** (✗ steps 1–3 were rewritten from the full texts; the earlier single-potential version is in the Corrections log, C4):
1. First check whether a published framework's hypotheses already cover the algorithm (Heuristic 8). If they do, prove the realization-wise lemmas and write a hypothesis-checklist theorem that glosses each axiom and imports the published bound unchanged [cards S093, p. 10; S015, pp. 7–8]. Otherwise choose the template by the guarantee you need and the oracle class:
   - (a) Expected complexity with random function estimates: a joint potential Φ_k = ν(f − f_low) + (1 − ν)·(a step term shaped like the per-step decrease: Δ², Δ³ or α‖∇f‖²), indicators I_k ("good oracle") and J_k ("accurate function estimate"), a case grid (gradient large or small relative to ζΔ_k) × (I_k, J_k), ν near 1 [cards S013, pp. 14–18; S015, p. 11; S047, pp. 4–6; S098, pp. 13–15].
   - (b) Expected complexity with exact f or bounded noise: counting over true/false × successful/unsuccessful × step above/below a threshold, with E[Σ W_k I_k] ≥ p·E[Σ W_k] for W_k fixed by the past; the constant is 2p/(2p − 1)² [cards S014, pp. 8–13; S026, pp. 8–13; S068, pp. 7–9; S088, Thm 6.13; S104, Thm 5.12].
   - (c) High probability: a progress measure Z_k alone, a deterministic lemma (if the method has not stopped and enough iterations were true, then enough iterations were good), Azuma–Hoeffding on Σ I_k − pt, and a Bernstein-type bound on the accumulated noise damage (Fuk–Nagaev, Chebyshev or Hoeffding for other noise models) [cards D001, pp. 7–13; S041, pp. 16–23; S083, pp. 11–17].
2. Prove the deterministic per-realization lemmas: on good iterations with a small enough step, the step is successful and Φ (or Z) decreases by an amount tied to ε [cards S041, pp. 14–16; S093, pp. 5–8]. Show that the step-size parameter behaves like a random walk biased upward when p exceeds the threshold; in the counting proofs this appears as "the number of small true steps is upper-bounded by the number of small false steps" [card D001, p. 8; also S057, pp. 9–10].
3. Bound the expected number of iterations until ‖∇f‖ ≤ ε with a stopping-time argument (template a: E[T_ε] ≤ p/(2p − 1)·Φ₀/(Θh(Δ_ε)) + 1, proved without first showing T_ε < ∞ [card S013, pp. 5–9]), or by solving the counting inequality for E[N] (template b) [card S026, p. 13]. For template (c), intersect the two concentration events and invert through a monotone function of ε; if the step threshold depends on the unknown minimum gradient norm, make it a random variable over the horizon [card S041, pp. 16–21]. If a step fails, use the symptom → device table (`references/proof-playbook.md` §0.2).
4. Upgrade to a high-probability bound before claiming practicality. Then convert iterations into samples: lower-bound the step parameter with high probability by coupling log α_k with a reflected random walk, and multiply by the oracle cost at that floor [cards S137, pp. 4–5; S057, pp. 7–13].
5. Compare with the deterministic bound. State the order in ε and how the constants depend on p (and on dimension n for DFO). If there is irreducible noise, state the reachable neighbourhood. Zero the noise and probability parameters in a remark after each theorem and check that the deterministic bound comes back [cards S026, pp. 13, 20, 22–23; D001, p. 17].
**Applies to stage**: theory and analysis; judging results.
**Different from standard practice**: stochastic-gradient analyses usually bound expected optimality after a fixed schedule. Here the analysis follows an *adaptive* step parameter as a random walk and treats the complexity as a stopping time.
**Limitations**: steps 1–2 were first reconstructed from abstract-level descriptions; the full texts confirm that version for template (a) only and add templates (b) and (c) [08 §3 row 1], so check which template the closest canonical paper uses before relying on one. Heavy technical overhead. Worst-case constants can be loose (Θ carries a 1/1800 factor in the stochastic trust-region bound [card S013, p. 16]). The results say little about typical-case behaviour on small budgets. A stopping time defined through x_{k+1} is not a stopping time with respect to the past, which blocked one extension [card S047, p. 12].

<a id="method-4"></a>

## Method 4: Geometry is the price of model-based DFO; pay only the minimum

**One line**: The geometry (poisedness) of the interpolation set is what certifies model quality. Establish how much geometry is truly needed, then defer it, let it self-correct, or randomize it (random samples, random subspaces) to pay less.
**Evidence**:
- Stated in her own essay (Optima 79, May 2009): "it turns out that it is not necessary to compute extra sample points unless the gradient of the model becomes small." [card S143, p. 4]. In the Scheinberg–Toint abstract: "such geometry improvements cannot be completely eliminated if one wishes to ensure global convergence" [card S030, p. 3]. The 2017 survey chapter: the self-correcting method "resorts to geometry-improving steps only when the model gradient is small" [card S046, p. 4]. (✗ An earlier version attributed Nocedal's column wording to the essay; Corrections log C7.)
- Practice: the radius shrinks only with adequate geometry [card S008, pp. 11, 14–17]; models need be certifiable only within finitely many steps [card S007, pp. 3, 13–14]; counterexamples, then geometry evaluations confined to the criticality stage with self-correction elsewhere [card S030, pp. 3, 8–15, 18]; random sample sets replace deterministic maintenance [card S018, pp. 2, 23–26]; geometry paid only on unsuccessful iterations and randomized through subspaces [card S088, pp. 7–8, 12–19]; certificate carried by n points only [card S104, pp. 10–12, 16–23, 27].
- Say–do consistency: ✅ stated in Scheinberg's own essay (2009) + practiced (1997–2026); 22 papers touch this method (21 evidence, 2 variant, 0 contradiction). Her p. 4 statement is matched point by point by Scheinberg–Toint 2010 [card S030, pp. 12, 14–15]. Dating (✗ corrected, C8): geometry-as-certificate dates from 1997 [card S008, pp. 14–17], but in 2008 the stated practical position was the opposite: "In practice, it is more efficient to maintain well-poisedness throughout the algorithm, not just when it is necessary to pass the criterion needed for the convergence proof." [card S016, p. 18]. The minimal-safeguard stance dates from 2009–2010 and was proved complexity-competitive in 2025–2026 [cards S088; S104].
- **(k01)** Stated in the co-authored book's organisation (2009, title level): Part I, *Sampling and modeling* (book pp. 13–112, about 100 pages), comes before any optimization framework; its only algorithms are geometry-improvement algorithms (§§6.2–6.4); it ends with a 24-page chapter, "Ensuring well poisedness and suitable derivative-free models", opening with fully linear and fully quadratic models (§6.1); eight section titles contain *poisedness*, and Ch. 3 and Ch. 4 reuse one skeleton (Lagrange polynomials → Λ-poisedness → condition number) [card B001, pp. 1–2]. Model-error bounds in step 2's form, with the constants written out: the re-proved Theorem 2.13 (linear regression, κ_eg = ν(1 + p^{1/2}‖M̂†‖/2)) [card B002, pp. 1–2] and the addendum's quadratic-regression bounds (ν₂ × ‖M̂†‖ × n^{1/2}, p̄^{1/2}) [card B004, pp. 1–2]; 13 of the 18 first-printing corrections fall in this part [card B002, pp. 1–3]. Peers: poisedness is "the key notion" (Nazareth) [card B005, p. 2]; positive spanning sets and poisedness are Part I's two paradigms (Orban) [card B006, p. 2]. Dating, consistent with C8: the titles speak of *ensuring* well poisedness; the 2009–2010 minimal-safeguard stance is not visible at title level. The say–do count above is unchanged (it counts papers).
**Steps**:
1. Choose the model class for the budget: linear with n+1 points (cheap, fully linear), or quadratic / minimum-norm underdetermined (more points, better curvature). A middle route: certify only n points with linear Lagrange polynomials and fit the remaining points by least squares with a bounded Hessian [card S104, pp. 10–12].
2. Write the model-error bound as poisedness constant × radius (fully linear), and decide which iterations actually need the certificate. Typically these are unsuccessful iterations where the radius is about to shrink, and criticality checks [cards S007, pp. 13–14; S008, p. 14]. Take Λ = 1 + O(1/n) in the theory, since the Λ-dependence is tight [card S088, pp. 10–12]; practice uses Λ = 1000 [card S104, p. 27].
3. Spend geometry-improving evaluations only there, or confine them to the criticality step (Scheinberg–Toint 2010's "final stage" is the stage where criticality of a putative stationary point is verified [card S030, p. 3]; the trigger is a small model gradient [cards S143, p. 4; S046, pp. 3–4]). Recycle each rejected trial point as a geometry repair before shrinking the radius [cards S030, p. 12; S104, pp. 10, 12]. Count the geometry steps with a potential (a growing orthogonal set, a volume ratio, −log|det Y|) [cards S088, pp. 8, 12–13; S104, pp. 13–14].
4. For high dimension or cheap randomness, replace deterministic geometry with random directions or **random subspaces** and a probability-p quality guarantee. Haar subspaces are well aligned with probability ≥ 243/443 > 1/2 [card S088, p. 16]; draw a new subspace only on iterations that change the radius, so geometry iterations stay deterministic [card S088, p. 18].
5. With noise, keep the sampling radius above a noise-dependent floor so interpolation does not amplify the noise (link to Method 5). In random subspaces, impose Δ_min explicitly and balance it against the noise floor, Δ_min = Θ(√ε_f) [card S104, pp. 18, 22].
6. Benchmark against Powell-family codes (e.g., PDFO, Py-BOBYQA) on the same problems. The 2026 protocol: NEWUOA via PRIMA, CUTEst via S2MPJ, data profiles averaged over random rotations of the initial set, the budget (not a tolerance) ending every run [card S104, pp. 24–30].
**Applies to stage**: algorithm design; debugging (stalling, degenerate models).
**Different from standard practice**: Powell-style practice manages geometry by careful heuristics. Conn-style theory certifies it at every iteration. This lens proves the necessary minimum and randomizes the rest.
**Limitations**: model building costs O(n) evaluations for linear models and O(n²) for full quadratics, so it is expensive in high dimension without subspaces. The verified work covers smooth objectives with few or no constraints. The complexity theory covers linear Lagrange polynomials; the best practical variant is not covered, and a competitive practical random-subspace method "remains difficult" [card S104, pp. 24–25, 27, 29–30].

<a id="method-5"></a>

## Method 5: Compare estimators head-to-head at equal accuracy (theory + experiment)

**One line**: For every candidate gradient or model estimator, derive the sample count and sampling radius needed to meet the same oracle contract. Then run them inside the same outer algorithm and count function evaluations.
**Evidence**:
- Stated: "In DFO it becomes also important to measure the effort in terms of the number of function evaluations" [card S046, p. 8]; in RL and evolution-strategies papers "the number of these directions seems to be chosen to fit the specific method and this choice is somewhat obscure" [card S006, p. 2]; the FoCM title "A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization".
- Practice: one accuracy target for all estimators, N and σ derived per estimator, estimator quality measured against the theorem's θ < 1/2, end-to-end runs in one line search [card S006, pp. 4–5, 25–31]; equal-N comparison [card D003, pp. 7, 10–11]; FD vs REINFORCE at equal per-iteration sample cost [card S073, pp. 6–7, 11]. The group's published benchmark protocol is step 6 [cards S023, pp. 17–19; S012, pp. 27–29; S041, pp. 33–36; S104, pp. 26–30].
- Say–do consistency: ✅ stated + practiced; 44 papers touch this method (17 evidence, 29 variant, 2 contradiction), scoped to the DFO and estimator line. The contradictions are applied, student-led papers that follow their host field's conventions [cards S082, pp. 4–6; S089, pp. 11, 13–14].
- **(k01)** ⚠ Variant (a textbook's scope, not a contradiction): the 2009 book has no section comparing methods and puts software in a 4-page appendix [card B001, p. 3]; reviewer D. Orban: "This is, however, the only comparison between methods to be found in the book." (the introduction), and he reports that the authors call comparison intricate and not an objective [card B006, p. 1]; J. L. Nazareth: few numerical illustrations [card B005, p. 3]. Evaluation-count comparisons appear before [card S019, p. 10] and after the book [cards S023, pp. 17–19; S006, pp. 25–31].
**Steps**:
1. List the competitors, including the ML default (Gaussian smoothing / evolution strategies) and the optimization default (finite differences, interpolation). Write them all as one parametrized formula first, then fill in a table of parameters per method [card S006, pp. 2–3].
2. Fix the accuracy target from Method 1 (e.g., error ≤ θ‖∇f‖) and the noise model (bounded noise ε_f, or stochastic noise).
3. For each estimator, derive the number of samples N and the radius σ that meet the target with probability ≥ p. Record the evaluation cost per accurate gradient. Choose σ at the minimizer of the aσ + b/σ bound; the existence condition gives the gradient-norm floor [cards S006, pp. 6–7; D003, p. 7]. Measure estimator quality at points harvested from real optimization trajectories, reporting the fraction that meets the theorem's threshold [card S006, pp. 29–30].
4. Plug each estimator into the **same** outer method (line search or fixed step) with the same problems, noise and seeds. Give every competitor any new generic component after showing that it helps each of them [card S104, p. 27].
5. Report function evaluations to reach tolerance (and failure rates), not iterations. Include cases where the estimator's assumptions are violated. Report what did not work: numbered findings before the plots, negative ones included, and split outcomes stated as they are [cards S104, pp. 26–27; D001, p. 27; S098, p. 24].
6. For DFO experiments, start from the group's published protocol unless the supervisor says otherwise: Moré–Wild problems or CUTEst via S2MPJ, data profiles in simplex gradients (evaluations/(n+1)), τ from 10⁻¹ to 10⁻⁷, tolerances matched to the noise, a Powell-family baseline [cards S023, pp. 17–19; S041, pp. 33–36; S104, pp. 26–30].
**Applies to stage**: experiment design; method selection; reviewing.
**Different from standard practice**: many ML papers adopt one estimator by convention and compare iteration counts. This lens compares the cost of meeting an accuracy guarantee.
**Limitations**: conclusions depend on the noise model and smoothness. With tiny budgets, asymptotic sample bounds can mislead. Sufficient sample counts can be loose; the FoCM necessity bound is weak and was probed by simulation [card S006, pp. 16–18].

<a id="method-6"></a>

## Method 6: Exploit structure before going generic

**One line**: Before treating the objective as a scalar black box, look for structure you can model directly: residual vectors, low-rank kernels, closed-form subproblems. Keep a generic convergence framework around the structured model.
**Evidence**:
- Stated (co-authored): the 1997 survey "thinks of exploiting any structure present in the problem as efficiently as possible." [card S004, p. 17]; "This is the essential cost of exploiting the structure." [card S023, pp. 17, 21]; known derivative sparsity can be exploited trivially [card S025, p. 18]; a scope rule: "using a BCD method as a general purpose SDP solver is not a good idea" [card S035, pp. 2, 21, 28].
- Practice: per-residual models on one sample set [card S023, pp. 2, 5, 16–17]; cheap constraints kept exact [card S019, pp. 6–7]; low-rank kernel makes the IPM solve O(nk²) [card S003, pp. 2, 6–11]; closed-form subproblems at gradient cost [cards S010, pp. 5–6; S005, pp. 1–3, 21]; the known nonsmooth part φ kept exact while only f is sampled [cards S098, pp. 2, 4, 7; S068, pp. 1, 4].
- Say–do consistency: ✅ stated (co-authored statements 1997, 2008, 2010) + practiced; 39 papers touch this method (31 evidence, 8 variant, 0 contradiction). (✗ Earlier ⚠ "explicit statement not found", from search results only; C9.)
**Steps**:
1. Ask whether the black box returns a vector (residuals, per-scenario outputs) or only a scalar. If a vector, model the components on one shared sample set inside a trust region (Zhang–Conn–Scheinberg 2010, DFLS); you pay in linear algebra and memory, not in function evaluations [card S023, pp. 2, 5, 16–17, 21]. **With stochastic noise this is new ground**: no read paper combines per-residual models with stochastic noise. DFLS was tested with deterministic noise [card S023, pp. 17–19], and STORM samples the scalar sum of squares even on least-squares test problems [card S012, p. 27]. Squaring averaged residuals gives a biased estimate of f (E‖r̄‖² = ‖r‖² + tr Cov(r̃)/N; the skill's arithmetic, not a paper result), so state the bias in the contract and raise the design with the supervisor.
2. Identify known, cheap parts of the objective (regularizers, constraints, a known model part) and keep them exact in the subproblem. Classify constraints by what the oracle returns and what it costs: cheap with derivatives, expensive black box, hidden pass/fail [card S019, pp. 3, 6–8]; for f + φ with a known prox, keep φ exact in the subproblem and in the reduction ratio [card S098, pp. 2, 4, 7].
3. Look for low-rank or sparse structure that makes subproblems closed-form or cheap, as in low-rank kernels for SVM training and alternating linearization for sparse inverse covariance [cards S003, pp. 6–11; S010, pp. 5–6].
4. Wrap the structured model in the usual globalization (trust region) so the convergence theory still applies.
5. Compare against the generic DFO solver on the same budget to show the gain. DFLS used NEWUOA to show the gain from structure and LMDIF to show the gain from interpolation over finite differences [card S023, p. 16].
**Applies to stage**: problem framing; algorithm design.
**Different from standard practice**: generic DFO tooling treats f as an opaque scalar. This lens first spends effort on modelling structure.
**Limitations**: needs access to component outputs or problem knowledge, so it does not help pure scalar black boxes. Structure-specific code is less reusable. Structured models under stochastic noise are not covered by the verified work (step 1).

<a id="workflow-a"></a>

## Workflow A: Oracle audit & problem framing

**Input**: a problem description: what one evaluation returns, its cost, the noise source, dimension, constraints, and the budget.
**Steps**:
1. Classify the noise: none, deterministic (numerical), or stochastic (sampling). Note known bias (smoothing, finite differences, simulation). Estimate the noise level from repeated calls at fixed points; the SASS experiments set the slack to one fifth of the standard deviation of 30 oracle calls, re-estimated every epoch [card D001, p. 26]. (→ Method 1)
2. Write the oracle contract and separate controllable from irreducible error. State the reachable neighbourhood, using the published floor for the closest method (√ε_f-type for first-order trust region and step search, ε_f^{2/3} for cubic regularization, √(n·ε_f) for model-based DFO) [cards S041, p. 21; S093, p. 9; S104, pp. 16, 22]. (→ Method 1)
3. Look for structure: residual vector, known parts (a prox term, cheap constraints), low rank. Classify constraints as cheap with derivatives, expensive black box, or hidden pass/fail [card S019, pp. 3, 6–8]. If the structure is a residual vector and the noise is stochastic, flag Method 6 step 1's caveat. (→ Method 6)
4. Check smoothness and constraints honestly. If the problem is nonsmooth or has hidden constraints, flag that this lens is weak and point to a direct-search lens (e.g., Audet in the roundtable). Composite f + φ with a cheap, exact prox is inside the lens (ProxSTORM) [card S098, pp. 2–4].
5. Run the Taste quick-check.
**🔴 Checkpoint**: if you cannot state even a heuristic accuracy-vs-cost relation for the estimates (no control over samples, unknown noise), stop designing algorithms. First run a noise-estimation experiment (repeated evaluations at fixed points, differences along a line). If the objective is nonsmooth or discontinuous, hand over to another lens.
**Output**: a one-paragraph problem statement with the oracle contract, the reachable accuracy, detected structure, and a go / hand-over decision.

<a id="workflow-b"></a>

## Workflow B: Algorithm design for noisy / stochastic DFO

**Input**: the Workflow A output.
**Steps**:
1. Pick the classical base method: an interpolation trust region (expensive, low n), adaptive step search with estimated gradients (cheaper evaluations, larger n), or a random-subspace model method (large n). If practitioners run a heuristic code, look for "the closest theoretically convergent algorithm to the practical implementations" [cards S143, p. 5; S104, pp. 1–2]. (→ Method 2, Method 4)
2. Choose the estimator and its sampling radius and sample counts via Method 5 bounds (σ from the aσ + b/σ trade-off; σ = O(√ε_f) for randomized finite differences [card D001, p. 25]).
3. Tie the per-iteration accuracy to Δ_k or α_k and implement adaptive sampling that meets it, in knowable quantities with a guess-and-increase loop when ‖∇f‖ is unknown [cards S015, p. 7; S047, p. 9]. Theory asks for O(Δ_k^{-4}) function samples [card S013, pp. 19–20]; the STORM implementation used about 1/δ_k "after testing various other rates" [card S012, pp. 28, 30], so start there and ablate. If you can fix the seeds at x_k and x_k + s_k, estimate the reduction difference with common random numbers: O(Δ_k^{-2}) samples [card S098, pp. 21–23]. Draw fresh estimates at the current and trial points every iteration, and do not average when failures are biased [card S012, pp. 7, 26]. (→ Method 1)
4. If there is noise, relax the acceptance test by a noise-level slack and make radius or step increases cautious (→ Method 2; Heuristic 5): r = 2ε_f in the numerator of ρ_k, radius increase only if ‖g_k‖ ≥ η₂Δ_k [card S041, p. 11]. If the oracle may be wrong more often than right, make the increase factor larger than the decrease factor (Method 1 step 5).
5. Keep geometry maintenance minimal: only at unsuccessful or criticality iterations, or randomized. Replace a criticality loop by the acceptance test ‖g_k‖ ≥ η₂Δ_k [cards S088, pp. 2–3; S104, p. 4], and reuse rejected trial points for self-correction [card S104, p. 10]. (→ Method 4)
6. Define the stopping rule in terms of the noise floor, not a gradient tolerance the oracle cannot resolve. DFLS set the final radius and the finite-difference step to the noise level [card S023, p. 19].

Published starting settings (from the papers' experiments, not recommendations; cite the paper, and ablate):

| Method (paper) | Settings |
|---|---|
| Powell-style DFO, GC-YZ-LIN/V [card S104, Table 6.1, pp. 27–28] | η₁ = 0.01, η₂ = 5 × 10⁻⁹, γ_inc = 1.3, γ_dec = 0.8, Λ = 1000, Λ_sc = 2 |
| SASS step search [card D001, p. 26] | γ = 0.9, θ = 0.2, α₀ = 1; ε′_f = ⅕ × std of 30 zeroth-order calls, re-estimated each epoch |
| ProxSTORM [card S098, Table 2, p. 24] | η₁ = 0.5, η₂ = 5 × 10⁻⁵, δ₀ = 10, δ_max = 10¹⁰, γ = 5; 100 seeded realizations |
| STORM on 53 CUTEr problems [card S012, pp. 28, 30] | budget 1000(n + 1) evaluations, averaged over 10 runs; samples ∝ 1/δ_k |

**🔴 Checkpoint**: after a pilot run, compare the plateau of f̃ with the floor predicted in Workflow A step 2. If f̃ plateaus at that level, stop: the noise floor has been reached. If it plateaus well above it while the radius keeps shrinking, the oracle contract is not being met: increase samples or raise Δ_min, and check with an adversarial oracle that stays inside the contract (Workflow H step 3) [card S041, pp. 30–33]. Do not add heuristics to hide this. Also report how often each safeguard fired [card S005, p. 19].
**Output**: pseudocode with the oracle contract per step, parameter defaults taken from the classical method (and the published settings above where they apply), and a list of the assumptions the design relies on.

<a id="workflow-c"></a>

## Workflow C: Probabilistic complexity analysis

**Input**: the algorithm and the oracle contract. For the detailed student scaffold, use Workflow F with `references/proof-playbook.md`.
**Steps**:
1. Check whether a published framework's hypotheses cover the algorithm (Method 3 step 1; Heuristic 8). If they do, write the hypothesis-checklist theorem and go to step 4 [card S093, p. 10]. Otherwise rerun the deterministic proof with the contract and mark the first failing inequality. (→ Method 2)
2. Pick template (a), (b) or (c), define Φ_k or Z_k and the success indicators, and show the biased-random-walk behaviour of the step parameter. (→ Method 3)
3. Bound the expected stopping time, then the high-probability tail. When the noise is unbounded, bound the sum of damages rather than each one [card D001, pp. 11–12]; for other failures use the playbook's symptom → device table (§0.2). (→ Method 3)
4. Compare with the deterministic order; make the p- and n-dependence explicit. When the ε-order ties, compete on constants and assumptions in a complexity table with an additional-assumption column [cards S037, p. 4; S104, pp. 2–3]. (→ Method 3)
5. Check that the probability threshold is achievable by the sampling scheme from Workflow B, and convert the iteration bound into a sample bound (Heuristic 4). (→ Method 1)
**🔴 Checkpoint**: if the ε-order is worse than the deterministic order, decide explicitly whether this is intrinsic (lower bound known?) or a proof artefact. Do not publish a weaker order without that diagnosis. If p must tend to 1, the fixed-probability framework is not delivering. Say so. If an extension fails, state it as a conjecture and name the inequality that breaks (Heuristic 10).
**Output**: a theorem statement (order + constants + probability), a proof skeleton, and a list of the lemmas to verify rigorously.

<a id="workflow-d"></a>

## Workflow D: Estimator & experiment design

**Input**: candidate methods and estimators, test problems, noise model, budget.
**Steps**:
1. Fix the accuracy target and the noise model shared by all competitors. (→ Method 5)
2. Derive or look up N and σ for each estimator, and state them in the experiment table. Measure estimator accuracy at trajectory points against the theorem's threshold before running end-to-end [card S006, pp. 29–30]. (→ Method 5)
3. Use the same outer algorithm, problems, seeds and budget. Include Powell-family and standard DFO codes as baselines (verify each exists before naming it). Run each baseline at its best configuration [cards S003, pp. 15–17; S022, pp. 10–13]; add a baseline variant that removes one assumption violation, and a competitor that violates your assumption [cards S012, p. 28; S137, p. 6]. (→ Method 4, Method 5)
4. Report function evaluations to tolerance, success rates, and behaviour near the noise floor. Include failure cases. Outside DFO, count the dominant unit of work and state each method's per-iteration charge [card D001, p. 27].
**🔴 Checkpoint**: if one method wins only after per-problem tuning, or only on iteration counts, the comparison is invalid. Redo it with fixed parameters and evaluation counts.
**Output**: an experiment protocol (problems, noise, budgets, metrics, parameter settings) ready to run.

<a id="workflow-e"></a>

## Workflow E: Reviewing a DFO / zeroth-order paper or draft

**Input**: the manuscript or abstract.
**Steps**:
1. Extract the oracle assumptions. Are they unbiased? bounded? always accurate? Could they be weakened to "accurate with probability p"? Audit each assumption against the function class the paper claims (e.g., bounded gradients are false for strongly convex f) [cards S009, p. 2; S032, p. 3]. (→ Method 1)
2. Check whether the algorithm is classical-plus-minimal-change or a new construction, and whether the novelty is justified. (→ Method 2)
3. Check the guarantee type (almost sure / expected / high probability), its order against the deterministic method, and the hidden constants. Check whether the bound counts iterations, samples or evaluations. (→ Method 3)
4. Check the geometry handling for model-based methods. (→ Method 4)
5. Check comparison fairness: same accuracy target, evaluation counts, standard baselines. (→ Method 5)
**🔴 Checkpoint**: if the main claim depends on an oracle assumption that the paper's own estimator violates (e.g., an unbiasedness assumption paired with a smoothing estimator), mark it as a major issue before anything else.
**Output**: a review with major issues (assumptions, guarantee), minor issues (constants, experiments), and 2–3 concrete fixes, each labelled with its method.

<a id="workflow-f"></a>

## Workflow F: Complexity proof scaffold (student mode)

**Input**: the algorithm (pseudocode), what the oracles return, the target guarantee, and any notes or feedback in `references/sources/private/`.
**Steps**:
1. **Oracle contract.** Write I_k and J_k (good-gradient/model and good-function-estimate events), the accuracy form relative to α_k or Δ_k, the probability p conditioned on the past, and what happens on failure: bounded error, expected-error bound, or arbitrary corruption. (→ Method 1; playbook §0 M1)
2. **Map to the closest classical method and the closest canonical template.** Match on algorithm (Armijo / trust region / ARC / Powell-style interpolation) and on oracle class (exact f → T1/T3; random f → T2/T4/T5; bounded noise → T6; biased/probabilistic → T7/T8; costs → T9; corrupted/heavy-tailed → T11; convex composite with exact f → T12; nonconvex f + convex φ with random estimates → T14; comparison oracles → T15; model-based DFO → T0/T13). If a framework's hypotheses fit, write the checklist theorem (Heuristic 8). Otherwise rerun that paper's deterministic core, mark the first inequality that fails, and look the symptom up in the playbook's symptom → device table (§0.2). (→ Method 2, Method 3)
3. **Stochastic-process argument.** Choose expected (renewal-reward, T4; or counting, T3) or high-probability (deterministic counting + concentration on Σ I_k, T7). If the step parameter can collapse, add the lower-bound lemma (T9). (→ Method 3)
4. **Bound.** State order in ε, guarantee type, complexity measure (iterations / samples / function evaluations), p-dependence, n-dependence (DFO), and the noise-floor neighbourhood.
5. **Sanity check against the canonical paper.** Fill the playbook's sanity-check table. Compare the ε-order with the deterministic counterpart. Check that every probability is conditional. Check that bad function estimates are controlled. Check that the constants have the same form (e.g., a p/(2p−1) or 2p/(2p−1)² blow-up) as the canonical theorem, after reading the theorem, not the playbook. Zero the noise and probability parameters and check that the deterministic bound returns.
**🔴 Checkpoint**: stop and bring it to the supervisor (do not polish further) if (a) the ε-order is worse than the deterministic one and you cannot say whether that is intrinsic, (b) the argument needs p → 1 or unconditional independence, or (c) no canonical template or symptom row matches after step 2, which means you may be on new ground and should confirm the setting first. A proof sketch from this workflow is a draft to verify line by line, never a finished theorem (Integrity rule 3).
**Output**: a one-page proof plan: contract, template used and where it breaks, lemma list with status (done / sketched / open), theorem statement draft, the sanity-check table, and 2–3 questions for the supervisor.

<a id="workflow-g"></a>

## Workflow G: Pre-meeting self-review (student mode)

**Input**: the student's draft, result, plot or proof sketch, the meeting's purpose, and any prior feedback in `references/sources/private/feedback/` (if present; read it first and check whether earlier comments were addressed).
**Steps**:
1. **Oracle contract stated?** Can a reader find, in one place, what each estimate must satisfy, how often, and what happens when it fails? (→ Method 1)
2. **Deterministic analogue?** Is it clear which classical method this is, what was changed, and why only that? (→ Method 2)
3. **Complexity order vs deterministic?** State the ε-order, the guarantee type (a.s. / expected / high-probability), the measure (iterations / samples / evaluations) and the p- and n-dependence. Flag any gap from the deterministic order. (→ Method 3)
4. **Equal-evaluation comparisons?** Are experiments counted in function or oracle evaluations, with the same accuracy target, noise, seeds and budgets for all methods, and standard baselines included (a Powell-family code for DFO)? The published papers use the Moré–Wild set or CUTEst via S2MPJ with data profiles in simplex gradients [cards S023, pp. 17–19; S104, pp. 26–30]. *Check the group's current convention with the supervisor; the papers show past practice only.* (→ Method 5)
5. **Geometry and noise floor.** For model-based work, how is geometry maintained and counted? For noisy work, is the stopping rule above the noise floor? (→ Method 4, Method 1)
6. **Relation to the group's recent papers.** Which reading-path / playbook item is closest? Does a framework already cover it (→ Heuristic 8)? What is new relative to it, in one sentence?
**🔴 Checkpoint**: if items 1 or 3 cannot be answered, make them the *first* agenda item ("I am not sure what my oracle contract is" is a good meeting question). Do not hide the gap behind experiments. If private feedback from an earlier meeting has not been addressed, list it at the top.
**Output**: a one-page brief with a one-sentence claim, the oracle contract, the deterministic analogue and change, the bound (or "not yet"), the experiment protocol summary, open issues ranked, and 3 questions to ask. Footer: *"Prepared with a skill distilled from public work. Scheinberg's feedback overrides it."*

<a id="workflow-h"></a>

## Workflow H: Measuring a theorem (tightness and theory-vs-practice probe)

**Input**: a theorem with thresholds or constants (minimum success probability, noise floor, sample count), and an implementation.
**Steps**:
1. Plug textbook parameter values into every probability condition and constant, and print their size [cards S012, pp. 20–21; S013, p. 16]. (→ Method 3)
2. Compute the theoretical threshold on a toy instance and sweep experiments across it, drawing the threshold on the plot [card S012, pp. 30–32]. If your necessity bound is weak, simulate the extremal instance to find the true threshold [card S006, pp. 16–18].
3. Build an adversarial oracle that stays inside the contract (worst admissible noise, Bernoulli(p) flags on good iterations), and compare the plateau it produces with the theorem's noise floor [card S041, pp. 30–33].
4. Sweep multiples of each theory-prescribed parameter in a practical code (e.g. r ∈ {0, 1, 2, 4, 8}·ε_f), including the zero ablation [cards S041, pp. 33–36; D001, p. 26]. (→ Method 5)
5. Pair the upper bound with a construction that attains it or with a lower bound [cards S088, Thm 4.6; S087, pp. 23–26, 41–43].
6. Write the deviation list: every place the implementation departs from the assumptions, each with its reason [cards S098, p. 24; S104, p. 27; D001, p. 26].
**🔴 Checkpoint**: if the measured behaviour contradicts the theorem itself, not just its constants, stop and diagnose before writing: either the proof has a gap or the experiment violates an assumption. If the theory cannot explain an observed regime, say so in the paper rather than smoothing it over [card S041, p. 33].
**Output**: a table of theoretical against measured thresholds and floors, the deviation list, and one remark for the paper interpreting the gap.

<a id="heuristic-1"></a>

## Heuristic 1: random models, gradients or function values

1. **If** your models, gradients or function values are random, **then** require each to be good with a fixed probability rather than always, with accuracy tied to the step or radius; function estimates need the tighter accuracy (ε_F δ_k² against κ_eg δ_k). Cases: BSV, SIOPT 2014 (models good with probability ≥ 1/2, exact function values; arXiv:1304.2808) [card S018, pp. 1, 6–7]; STORM, Math. Program. 2018 (models and estimates both random; https://doi.org/10.1007/s10107-017-1141-8) [card S012, pp. 8–9].

<a id="heuristic-2"></a>

## Heuristic 2: skipping geometry-improving steps

2. **If** you want to skip geometry-improving steps, **then** confine them to the criticality step instead of eliminating them, because full elimination breaks global convergence; the trigger is a small model gradient. Case: Scheinberg–Toint, SIOPT 2010 (https://doi.org/10.1137/090748536) [cards S030, pp. 3, 12; S143, pp. 4–5].

<a id="heuristic-3"></a>

## Heuristic 3: noisy evaluations and gradient estimates

3. **If** evaluations are noisy and you need gradients, **then** choose the estimator, sample count and radius from derived bounds instead of defaulting to Gaussian smoothing. Case: Berahas et al., FoCM 2022 (https://doi.org/10.1007/s10208-021-09513-z) [card S006, pp. 5, 25, 32].

<a id="heuristic-4"></a>

## Heuristic 4: from expected to high-probability and sample complexity

4. **If** you have an expected-complexity result, **then** push it to a high-probability tail bound, and then lower-bound the step parameter with high probability and convert iterations into total oracle or sample cost. Cases: Blanchet et al. 2019 → Jin–Scheinberg–Xie 2024 (https://doi.org/10.1137/22M1512764) [card D001, p. 3]; Jin–Scheinberg–Xie, Math. Program. 209 (2025) (https://doi.org/10.1007/s10107-024-02078-z) [cards S137, p. 3; S057, pp. 7–13; S093, pp. 17–18].

<a id="heuristic-5"></a>

## Heuristic 5: bounded noise, biased or inconsistent oracles

5. **If** f is only known up to bounded noise, or oracles may be biased or inconsistent, **then** relax the acceptance test by a noise slack, update the radius or step cautiously, and prove convergence to a stated neighbourhood, not to stationarity. Cases: Berahas–Cao–Scheinberg, SIOPT 31 (2021) (https://doi.org/10.1137/19M1291832) [card S026, pp. 4–5, 15–16]; Cao–Berahas–Scheinberg, Math. Program. 2024 (https://doi.org/10.1007/s10107-023-01999-5) [card S041, pp. 11–12]; a zero slack performs badly [card D001, p. 26].

<a id="heuristic-6"></a>

## Heuristic 6: dimension too large for full interpolation models

6. **If** the dimension is too large for full interpolation models, **then** run a Powell-style model method in random subspaces. Cases: Chaudhry–Scheinberg 2025 (arXiv:2510.14935); Chaudhry–Scheinberg–Sun 2026 (arXiv:2609.09441) [cards S088, pp. 13–19; S104, p. 21]; the practical subspace variant is not yet competitive [card S104, pp. 29–30].

<a id="heuristic-7"></a>

## Heuristic 7: heavy-tailed or corrupted oracles

7. **If** function-value noise may be heavy-tailed or gradients occasionally corrupted, **then** expect the tail of the complexity bound to follow the oracle's tail (exponential vs polynomial), and state which one you have. Case: Scheinberg–Xie 2025 (arXiv:2511.19411) [card S083, pp. 16–17].

<a id="heuristic-8"></a>

## Heuristic 8: check an existing framework before a new proof

8. **If** you are about to prove complexity for a new variant, **then** first check whether a published framework's hypotheses already cover it and, if so, write a hypothesis-checklist theorem that imports the bound unchanged; if you have proved one algorithm, extract the properties the proof used as axioms on an abstract model class or process, so later variants cost a checklist. Cases: the fully linear class proved once and instantiated for interpolation and regression [card S007, pp. 7–13]; one process theorem instantiated for four settings [card S014, pp. 8, 13, 16–26]; axioms (i)–(v) glossed one per line and imported by stochastic cubic regularization, with the stopping time shifted by one [cards D001, p. 7; S093, p. 10]. (A heuristic, not a core method: the reuse is inside her own group, so exclusivity is not shown; 08 §4.)
- **(k01)** Weak, title-level support: the 2009 book states the trust-region framework and its conditions on the models (§§10.1–10.2) before the concrete methods that satisfy them (Ch. 11: the "DFO" approach, Powell's methods, wedge methods) [card B001, p. 3]. Co-authored; no promotion.

<a id="heuristic-9"></a>

## Heuristic 9: measure every threshold and constant

9. **If** your theorem has a threshold or constant (minimum success probability, noise floor, sample count), **then** compute it on a toy instance, run experiments across it (including an adversarial oracle that stays inside the contract), list every place the implementation departs from the assumptions, and pair the upper bound with a construction that attains it or with a lower bound. Cases: theory needs (1 − σ) > 0.999 at n = 10, yet 100% of runs succeed at 0.998 [card S012, pp. 30–32]; adversarial oracle plateaus compared with the noise floor [card S041, pp. 30–33]; a weak necessity bound followed by a 10,000-run simulation [card S006, pp. 16–18]; a Sherman–Morrison family shows the poisedness dependence is tight [card S088, Thm 4.6]. (→ Workflow H)
- **(k01)** ⚠ Variant: the 2009 book computes Λ on toy sample sets and prints it in figure captions, which made the numbers checkable; the 2015 errata correct them (294, 5324, 492624) and replace a sentence that reconciled two values by a scaling argument with the corrected number [card B002, pp. 2–3]. Illustrations of Λ-poisedness, not tests of a theorem's threshold.

<a id="heuristic-10"></a>

## Heuristic 10: a failed extension becomes a named open problem

10. **If** a natural extension of your result fails, **then** state it as a conjecture or open problem and name the exact inequality or technical obstacle that breaks. Cases: a lim-type second-order result left as a conjecture, with Σδ² against Σδ named as the failing step [card S018, pp. 20–21]; stochastic cubic regularization blocked because T_ε defined through x_{k+1} is not a stopping time [card S047, p. 12]; certifying Powell-like geometry left open in 2008 [card S016, p. 24] and later solved [card S104, pp. 1–2, 10–23].

<a id="signature-note"></a>

## Signature work: anatomies kept elsewhere

Three anatomies are kept here; BSV 2014, FoCM 2022 and the 2026 Powell-style paper are in `references/research/01-publications.md` (section "Signature work anatomies moved from SKILL.md").

<a id="signature-storm"></a>

## Signature work: Stochastic optimization using a trust-region method and random models (Mathematical Programming 2018, DOI 10.1007/s10107-017-1141-8) [card S012, read in full, arXiv v2]

| Dimension | Content |
|---|---|
| Origin | Stated (replaces the earlier *speculation*): BSV assumed "that the function values at the current iterate and the trial point can be computed exactly" (p. 8), so exact function values were the next assumption to drop; some assumptions "were inspired by an early version" of Billups–Larson (p. 5). Material from R. Chen's Lehigh thesis (ref. [6], p. 35). |
| Why then | Stated: DFO was developed for deterministic functions although noise is where it matters most; SG methods are slow and parameter-dependent; SA methods need tuned sampling and cannot handle biased noise (pp. 1–2). Applied motivations: hyperparameter tuning in which training may fail, and black-box solvers whose failure probability rises with the requested accuracy (pp. 3–4, 25–26). |
| Key insight | Models **and** function estimates need to be accurate "with high enough, but fixed, probability", with accuracy tied to the radius: models κ_eg δ_k / κ_ef δ_k² with probability α, estimates ε_F δ_k² with probability β, both conditioned on the past, failures arbitrary ("if a model or estimate is inaccurate, it can be arbitrarily inaccurate", p. 3) (pp. 8–9). Fresh estimates at the current and trial points every iteration (p. 7). |
| Minimal evidence | Abstract gives constructions of sufficiently accurate random models under biased or unbiased noise; the full text gives them in §5: Chebyshev sample averages at n+1 well-poised points, averaged stochastic gradients, and plain interpolation without averaging for computation failures (pp. 24–26, 30). Almost-sure ΣΔ_k² < ∞ via Φ_k = νf + (1 − ν)Δ_k² and a 2×4 case split (pp. 14–19); liminf needs αβ ≥ 1/2 (pp. 21–22), but the almost-sure theorem needs α and β close to 1: (1 − α)(1 − β) ≤ 1/440 with textbook constants (Remark 4.13, pp. 20–21). Experiments: 53 CUTEr sum-of-squares problems, performance profiles in function evaluations, budget 1000(n+1), 10 repetitions (pp. 27–29); computation failures with a garbage value (p. 30); a theory-threshold sweep with 100% success at α ≈ 0.27 (pp. 30–32); logistic regression against Adagrad (pp. 31–35). |
| Abandoned paths | Stated: the η₂ step restriction is used in the proof but not in the experiments (p. 21); the theoretical 1/δ_k⁴ sampling rate was replaced by about 1/δ_k "after testing various other rates" (pp. 28, 30); rates deferred to future research (p. 25). |
| Reception | Became a named algorithm (STORM). Complexity followed in Blanchet et al. 2019, which also drops the restrictive η₂ ≥ κ_ef [card S013, pp. 12, 19]; total sample complexity O(σ_g² ε^{-4} log(1/ε)) gradient samples [card S057, p. 16]. ProxSTORM (arXiv:2510.03187), Scheinberg's own paper with R. J. Baraldi, A. Javeed and D. P. Kouri (Sandia), extends STORM to f + φ, recovers STORM when φ ≡ 0, and shows that only function differences need estimating, O(Δ^{-2}) samples under common random numbers [card S098, pp. 1–3, 7, 9, 23] (an earlier version called it third-party; Corrections log C11). |
| Methods shown | Method 1, Method 2, Method 3, Method 5 (benchmark protocol) |

<a id="signature-self-correcting-geometry"></a>

## Signature work: Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization (SIAM J. Optim. 20, 2010, DOI 10.1137/090748536) and the Optima 79 essay (May 2009) [cards S030 and S143, both read in full]

| Dimension | Content |
|---|---|
| Origin | Stated: an unexplained anomaly. Fasano, Nocedal and Morales observed that an algorithm ignoring geometry "may in fact perform quite well in practice" [card S030, p. 4]; Nocedal is credited with raising the issue (p. 18). The essay asks it in one sentence: "So do we need to be concerned about the geometry of sample sets or not?" [card S143, p. 4]. |
| Why then | The convergence theory of the CSV framework depended on model-improvement steps, while practical codes (NEWUOA, DFO) also computed them without knowing how necessary they were [card S143, p. 3]. In 2008 the stated practice was still to maintain poisedness throughout [card S016, p. 18]. |
| Key insight | Necessity first: hand-checkable 2-D examples in which ignoring geometry converges to a non-stationary point, with an outcome that does not depend on the replacement rule [cards S030, pp. 8–11; S143, pp. 4–5]. Then self-correction: a failed step, the interpolation error bound and Σℓ_j = 1 together force a point with |ℓ_j(x⁺)| > Λ, so the rejected trial point repairs the set at no extra evaluation (Lemma 5.2, pp. 14–15). Dedicated geometry work only in the criticality step (p. 12). |
| Minimal evidence | liminf ‖∇f(x_k)‖ = 0 (Thm 5.8, pp. 17–18). No numerics; the objective is stated as understanding: "Hence, the main objective of this paper is to advance the understanding of the role of geometry in model based DFO methods, rather than to suggest a new practical optimization scheme." (p. 4). The essay presents the method as "the closest theoretically convergent algorithm to the practical implementations in [19] and [6] that exist so far" [card S143, p. 5]. |
| Abandoned paths | Stated future work: second order, unbounded Hessians, convex constraints, noisy objectives (p. 18); whether stronger results hold "remains to be seen" [card S143, p. 5]. |
| Reception | Its counterexample became the standard citation for "geometry cannot be totally ignored" in the 2017 survey chapter [card S046, pp. 3–4]. Self-correction returned as a step of the 2026 Powell-style method, now with complexity [card S104, pp. 10, 12]. |
| Methods shown | Method 4, Method 2; Heuristic 8 (algorithm written against the fully linear class [card S143, p. 3]) |

<a id="signature-adaptive-step-search"></a>

## Signature work: High probability complexity bounds for adaptive step search based on stochastic oracles (SIAM J. Optim. 34, 2024, DOI 10.1137/22M1512764; NeurIPS 2021 conference version) [card D001, read in full, arXiv v5]

| Dimension | Content |
|---|---|
| Origin | Stated: the limits of the group's own earlier step-search analyses: expected complexity only, a step-size cap, exact or bounded zeroth-order oracles, and a more complicated method with O(L³) dependence (pp. 2–3). The high-probability idea is credited to Gratton–Royer–Vicente–Zhang (p. 3). |
| Why then | Stated: an ML competitor (SGD with Armijo) needs per-sample smoothness and severe step bounds (pp. 3–4); oracles in ML come from mini-batches whose size is capped (p. 2). |
| Key insight | Keep the algorithm of Berahas–Cao–Scheinberg unchanged (p. 4) and move the novelty into the oracles: SFO with accuracy max{ε_g, min{τ, κα}‖g‖} and SZO with a mean bound plus a one-sided subexponential tail (p. 1). A finite cap τ removes the step-size bound (p. 3). The proof is a deterministic counting lemma plus Azuma–Hoeffding plus a Bernstein bound on the summed damage, with no joint potential: "The engine of the analysis is a key lemma showing that if the stopping time has not been reached and a large enough number of iterations are true, then there must be a large number of good iterations." (p. 8). |
| Minimal evidence | Tail bounds for nonconvex, convex and strongly convex (PL) functions (pp. 15–23); O(L) instead of O(L³) (p. 17); oracle constructions for mini-batches and randomized finite differences (pp. 24–25); experiments on 64 PMLB datasets and three networks at equal inner-product or pass budgets, with split outcomes reported as they are (pp. 26–28). |
| Abandoned paths | Stated: the step-size cap and the NeurIPS version's independence assumption on function-estimate errors are removed (pp. 3–4); practical variants with adaptive mini-batches and the choice of γ and ε′_f are left open (p. 26). |
| Reception | Its axioms (i)–(v) are imported unchanged by stochastic cubic regularization [card S093, p. 10]; the trust-region counterpart takes its counting idea [card S041, p. 3]; the unreliable-inputs framework generalises it to p < 1/2 and heavy tails and recovers it as a special case [card S083, p. 22]. |
| Methods shown | Method 1, Method 2, Method 3; Heuristic 8 |

<a id="anti-patterns"></a>

## Research anti-patterns (full sources per row)

| Anti-pattern | Why this lens rejects it (source) | Do instead |
|---|---|---|
| Tuned step-size schedule for a noisy black box | Adaptive step search needs no pre-specified step sizes (Jin–Scheinberg–Xie 2024); ADAM's best learning rate shifts across problems [card D001, p. 28] | Adaptive step search or trust region under an oracle contract (Methods 1–2) |
| Assuming unbiased estimates from a biased estimator | The frameworks explicitly allow biased or inconsistent oracles [cards D001, pp. 1–2; S041, p. 4]; under biased computation failures, averaging repeated evaluations optimizes the wrong function [card S012, pp. 26, 30] | Write the contract with a bias term and a neighbourhood result (Method 1); draw fresh estimates at the current and trial points rather than averaging biased failures |
| Gaussian smoothing "because ML uses it" | Estimators compared at equal accuracy (FoCM 2022) | Derive N and σ per estimator and compare evaluation counts (Method 5) |
| Sample sizes set from the true gradient norm or the target ε | Unknowable at run time; the group's rules use α_k, ‖g_k‖, Δ_k and variance bounds [cards S015, pp. 2, 7; S047, p. 9] | Guess-and-increase sampling in knowable quantities (Method 1 step 2) |
| Dropping geometry safeguards without an argument | Geometry steps cannot be fully eliminated (Scheinberg–Toint 2010) | Confine or randomize them (Method 4) |
| Claiming practicality from almost-sure convergence only | The progression to high-probability bounds (2019 → 2024) | Tail bound on iteration complexity (Method 3) |
| Reporting an iteration bound as the cost of the method | The step parameter is not bounded away from zero, so the per-iteration cost grows [cards S057, p. 1; S041, p. 3] | Lower-bound the step parameter and state sample complexity (Heuristic 4) |
| Scalar black-box modelling of a residual vector | Per-residual models (Zhang–Conn–Scheinberg 2010) | Model the components (Method 6) |
| New algorithm when a reanalysis would do | Classical methods kept across 2014–2026 papers | Rerun the classical proof and repair only the failing step (Method 2) |
| Re-proving every variant from scratch | Published frameworks are imported by checklist [cards S093, p. 10; S015, pp. 7–8; S098, pp. 19–20] | Check the axioms of an existing framework first (Heuristic 8) |
| A threshold or constant that nobody computed or tested | The group plugs in textbook constants and sweeps across thresholds [cards S012, pp. 20–21, 30–32; S041, pp. 30–33] | Workflow H |

<a id="research-trajectory"></a>

## Research trajectory: full-text view, recognition and latest

The full-text view of the trajectory (topics by period, the four turns, lines that ended, what stayed constant, collaboration by period) is in `references/research/06-trajectory.md` §9–13 and `references/research/08-deep-reading-synthesis.md` §8–9. In short: one senior partner per era (Conn–Toint, Conn–Vicente, Goldfarb), then a student or postdoc per line from about 2012; sole-authored work is rare: one algorithm and software paper (S022, JMLR 2006) plus position pieces and essays [cards S143; S044]. Author order is alphabetical in several analysis papers and not in others, so it is not evidence of who led.

Recognition: Lagrange Prize in Continuous Optimization 2015 (with Conn and Vicente, for the IDFO book; the citation notes impact in aerospace engineering, urban transport, adaptive meshing and groundwater remediation); Farkas Prize 2019 (INFORMS Optimization Society); SIAM Fellow, class of 2025 (for foundational contributions to DFO and to optimization applications in data science, and for service, paraphrase); INFORMS Fellow; ICM 2026 section lecturer (Control Theory and Optimization; secondary source); past Editor-in-Chief of *Mathematics of Operations Research*.

### Latest
- **Sept 2026**: "Powell-Style Model-Based Derivative-Free Optimization with Complexity Guarantees" (Chaudhry, Scheinberg, Sun; arXiv:2609.09441) [card S104].
- **Aug 2026 (third party, same question)**: Cartis & Roberts, random subspace model-based DFO complexity (arXiv:2608.17307).
- **2026**: ICM section lecture (Control Theory and Optimization); arXiv:2510.14935 listed as ICM 2026 proceedings on the co-author's homepage.
- **2026**: "Function-free optimization via comparison oracles" (Scheinberg, Xiong; arXiv:2604.26867) [card S087]. Stochastic cubic regularization published in *INFORMS J. Optim.* (Scheinberg, Xie; DOI 10.1287/ijoo.2025.0123) [card S093].
- **Nov 2025**: unreliable inputs, a unified high-probability framework (Scheinberg, Xie; arXiv:2511.19411) [card S083].
- **Oct 2025**: complexity of model-based DFO (Chaudhry, Scheinberg; arXiv:2510.14935) [card S088]; ProxSTORM (Baraldi, Javeed, Kouri, Scheinberg; arXiv:2510.03187) [card S098].
- **2025 journal versions**: sample complexity (Jin–Scheinberg–Xie, Math. Program. 209); stochastic ISTA/FISTA (Nguyen–Scheinberg–Tran, JOTA 205).
- Direction: the 2025–2026 papers apply probabilistic and complexity tools to Powell's classical interpolation methods and widen the oracle model (unreliable inputs, comparisons). Candidate thesis problems that follow from this are in `references/open-problems.md`.

**(k01)** The book's afterlife and reception (not a Latest item; no new edition is in the material read): a two-page addendum deriving Theorem 4.13 (27 Jan 2011) [card B004, p. 1]; errata for the first printing (18 items) and the second printing (3 items), both dated 17 May 2015, so a second printing exists (its date is not stated) [cards B002, p. 1; B003, p. 1]. Reviews: J. L. Nazareth, *Mathematics of Computation* 79(271), July 2010 [card B005, pp. 1–3]; D. Orban, *SIAM Review* 53(2), 2011, Book Reviews pp. 395–396 [card B006, pp. 1–2] (✗ earlier listed as 2010; corrected from the authors' book page, 08 §13.6 item 10). A third review (MAA Reviews, 24 June 2009) is listed on the authors' book page but was not read. Details: [Book material](#book-material).

<a id="academic-lineage"></a>

## Academic lineage

- **Training**: Lomonosov Moscow State University (OR, 1992) → Columbia University (PhD OR, 1997). PhD advisor Donald Goldfarb; dissertation on interior-point methods for linear and semidefinite programming (https://en.wikipedia.org/wiki/Katya_Scheinberg; verified 2026-09-27 via search).
- **Intellectual ancestors (evidenced by papers)**: M. J. D. Powell's interpolation-based trust-region methods (named in the 2026 title); A. R. Conn and Ph. L. Toint (co-authors from 1997; trust-region DFO framework); L. N. Vicente (co-author of the 2008 paper, the 2009 book and the 2014 paper).
  - **(k01)** Peer view: reviewer D. Orban reads the 2009 book's trust-region chapters against Conn–Gould–Toint's *Trust-Region Methods* (same series), which "has one author in common" with it, and notes that the older book treats nonsmooth (locally Lipschitz) functions while the DFO book assumes a Lipschitz gradient or Hessian [card B006, p. 2]. The 2009 table of contents gives Powell's methods their own section next to the "DFO" approach (§§11.2–11.3) [card B001, p. 3].
- **Peer collaborators on theory**: C. Cartis (complexity), J. Blanchet (applied probability), K. Choromanski (ML zeroth-order), D. Goldfarb and S. Ma (first-order ML optimization), F. E. Curtis (adaptive stochastic methods overview and tutorial [cards S047; S031]), R. J. Baraldi, A. Javeed and D. P. Kouri of Sandia National Laboratories (ProxSTORM [card S098]).
- **PhD students (verified from lab pages and thesis records)**: R. Chen (Lehigh 2015, STORM), X. Tang (Lehigh, LHAC), M. Menickelly (Lehigh 2017, random models), L. Cao (Lehigh 2021, model-based DFO and noisy analysis), M. Xie (Cornell 2019–2024, reliable adaptive stochastic optimization). The Lehigh page also lists X. Bai, A. Yektamaram, H. Ghanbari and M. Li. Details: `references/research/04-mentorship.md`.
- **Postdocs (verified)**: C. Paquette (Lehigh 2018), A. S. Berahas (Lehigh 2018–2020, co-supervised with Curtis and Takáč), A. Chaudhry (Georgia Tech Butler fellow, 2024–).
- **Other junior co-authors** (relation not confirmed): H. Zhang, A. S. Bandeira, B. Jin, L. M. Nguyen, T. H. Tran, Z. Xiong, S. Sun. Author order in this group is often alphabetical, so do not read it as a statement of who led.
- **Community**: MOS Chair (from July 2025); co-editor of Mathematical Programming; past EiC of Mathematics of Operations Research and of the SIAM-MOS book series; past chair of SIAG/OPT; co-editor of Optima (with A. Caprara, under editor A. Lodi, in 2009) [card S143, p. 10].

<a id="inner-tensions"></a>

## Inner tensions

- **Tension between guarantee-first and Powell's practice-first tradition.** The lens prizes worst-case and high-probability guarantees (Methods 3–4). Yet its latest work (arXiv:2609.09441) is motivated by Powell-style methods that practitioners trusted *before* such guarantees existed, and shows that their geometry handling is complexity-competitive. The lens both disciplines and vindicates practice; the tension already sits inside one paper, which refutes the geometry-free method's guarantee and explains its practical success on the same page [cards S030, pp. 4, 18; S143, pp. 4–5].
  - **(k01)** Peer view of the co-authored 2009 book: J. L. Nazareth places it in the "theoretical algorithmic science" mode and writes that "its focus is not on the “algorithmic engineering” side of the subject." [card B005, p. 3]. Second-hand, the preface's aims as he quotes them (book pp. xi–xii): the basic theory, to the extent that the reader understands what is needed to ensure convergence, how it affects algorithm design and what success to expect where [card B005, p. 1] (paraphrased here; the book body was not read).
- **Tension between classical conservatism and the ML bridge.** The group works on ML problems (JMLR 2001, NIPS 2010, FoCM 2022) but keeps classical line search and trust region as the algorithmic core (Method 2). ML practice leans on momentum, which the verified work does not adopt; a 2026 momentum variant of high-probability adaptive search (arXiv:2604.15526) is by a different group (UCAS), and acceleration is a gap (open-problems.md row 5). The tension is also internal: in 2017–2022 the group ran a parallel programme on new estimators with tuned or prescribed steps (SARAH, SGD without bounded gradients, Nesterov-accelerated shuffling) [cards S002; S009; S055], while the 2020 overview argues against tuned schedules [card S047, pp. 1–2].
- **Tension between elegant assumptions and checkable assumptions.** Fixed-probability oracle contracts (Method 1) give clean deterministic-order theorems, but p is rarely known, and the assumptions have been weakened step by step (unbiased → biased → corrupted or heavy-tailed, 2018 → 2025). The papers say so themselves [cards S012, p. 3; S098, p. 16], and the 2025 framework turns the threshold into a design parameter (p > 1/(m+1)) and replaces p by a conservative lower bound [card S083, pp. 15, 22].
- **Tension between deterministic safeguards and randomization.** In 2010, geometry steps "cannot be completely eliminated". From 2014 on, randomness (random models, random subspaces) replaces much of the deterministic geometry work. The lens holds both positions, depending on whether the guarantee needed is deterministic or probabilistic; in the 2025 subspace method the geometry iterations are kept free of randomness so they can be counted deterministically [card S088, p. 18].
- **Tension between theory-prescribed and practice-chosen parameters.** The theorems fix parameters from worst-case constants, while the implementations deliberately depart from them and say so: 1/δ_k instead of 1/δ_k⁴ sampling and no η₂ test [card S012, pp. 21, 28]; Λ = 1000, a tiny η₂ and a huge Hessian bound [card S104, p. 27]; a fixed mini-batch whose oracle properties are not checked [card D001, p. 26]. The lens resolves it by disclosure (deviation lists, Heuristic 9), not by closing the gap.

<a id="mentor-voice"></a>

## Mentor voice

Constructed from the framing of Scheinberg's paper abstracts and talk abstracts, and from the full texts of her papers. Recorded talks exist (YouTube: NeurIPS 2022 OPT plenary, MICDE seminar, 2025 Aisenstadt lectures), but **no transcript was read**, so treat this as a style guide, not a quotation. In student mode, the student's own notes of real feedback (`references/sources/private/feedback/`, if present) replace this section.
- Suggested questioning style for this lens (not observed feedback): diagnostic questions first ("what does your oracle actually guarantee?"), then a minimal repair.
- Recurring questions (derived from paper and talk framing, not quoted):
  - "What accuracy does this iteration need, and how often do you get it?"
  - "What is the deterministic complexity, and do you match its order?"
  - "Which classical method are you modifying, and what exactly broke?"
  - "Is that expected, or with high probability?"
  - "Does the bias change your rate, or only the neighbourhood you reach?"
  - "Can your step parameter go to zero? Then what is the sample complexity, not just the iteration count?"
  - "How many function evaluations does one accurate gradient cost with each estimator?"
  - "Is your sample-size rule written in things the algorithm knows?"
  - "Is there already a framework whose hypotheses your method satisfies?"
  - "Where is your assumption stronger than the prior paper's, and did you say so?"
- Avoid: praise with no content, and claims about Scheinberg's personal opinions on specific people or papers.

<a id="book-material"></a>

## Book material (IDFO 2009): what was read and what it supports

**(k01)** Added 2026-09-27. Cards: `07-paper-cards.md` rows B001–B006; batch file `cards/k01.md`; synthesis `08-deep-reading-synthesis.md` §13.

**What was read (all in full).** The table of contents, typeset 2008/11/17 [card B001, pp. 1–3]; the errata for the first printing (18 items) and the second printing (3 items), both dated 17 May 2015 [cards B002, pp. 1–3; B003, p. 1]; a two-page addendum deriving the quadratic-regression error bounds of Theorem 4.13, dated 27 Jan 2011 [card B004, pp. 1–2]; reviews by J. L. Nazareth (*Mathematics of Computation* 79(271), 2010) [card B005, pp. 1–3] and D. Orban (*SIAM Review* 53(2), 2011, Book Reviews pp. 395–396) [card B006, pp. 1–2]. B001–B004 are co-authored by Conn, Scheinberg and Vicente and show no division of labour, so nothing is credited to Scheinberg alone. B005–B006 are the reviewers' voice.

**What was not read.** The book body (S001) has no open full text: the chapters, proofs, examples and the software appendix are known only through their titles, the errata items that cite them, and the reviewers' descriptions. Book sentences quoted by a reviewer are second-hand. A third review listed on the authors' book page (MAA Reviews, 24 June 2009; the link returned 404 on 2026-09-27) was not read.

**Architecture (title level)** [card B001, pp. 1–3]:

| Part | Chapters | Book pages | What the titles show |
|---|---|---|---|
| Front | Ch. 1 | 1–12 | Why DFO; examples; **limitations of DFO** (§1.3); how DFO algorithms should work |
| I Sampling and modeling | Ch. 2–6 | 13–112 | Positive spanning sets, linear models, simplex gradients; interpolation, regression and underdetermined models, each with Lagrange polynomials and Λ-poisedness; Ch. 6 ensuring well poisedness, fully linear / fully quadratic models |
| II Frameworks and algorithms | Ch. 7–11 | 113–226 | Directional and simplicial direct search (incl. MADS, a globally convergent Nelder–Mead); line search on simplex derivatives (noise in §9.3; implicit filtering); trust-region framework with conditions on the models (Ch. 10, 34 pp., the longest); "DFO", Powell's methods, wedge methods (Ch. 11) |
| III Review of other topics | Ch. 12–13 | 227–250 | Surrogates; constrained problems; global and mixed-integer problems in one section (pp. 249–250) |
| Appendix | — | 251–254 | Software |

**What it supports in SKILL.md.** Method 4 (stated at the level of the book's organisation; see [Method 4](#method-4)); Method 2, weakly (framework and model conditions before instances; peer: similarities and differences with classical trust region; see [Method 2](#method-2)); the Honest Boundary domain line (below); the Honest Boundary reading-notes lesson (below); the inner tension guarantee-first vs practice-first (peer; see [Inner tensions](#inner-tensions)); the Roundtable Conn lens (the shared framework is Ch. 10); Academic Lineage (peer; see [Academic lineage](#academic-lineage)). Variants, all dating or scope: Methods 1, 3, 5, Taste marks 4 and 7, Heuristic 9 (notes under each anchor). No contradiction.

**Domain boundary.** The book's own scope matches the lens's: constraints, surrogates, global and mixed-integer problems are compressed into Part III, nonsmoothness appears in one direct-search section (§7.4), noise in one section (§9.3), and no title mentions probability [card B001, pp. 1–3]. Nazareth: problems "reasonably smooth, unconstrained", with up to about a hundred variables, and "The important intersection between derivative-free optimization and non-differentiable optimization is not adequately addressed." [card B005, pp. 1, 3]. Orban: a Lipschitz-continuous gradient or Hessian is assumed, nonsmooth trust-region theory lives in Conn–Gould–Toint, and the listed software is research grade [card B006, p. 2].

**Public self-correction (the authors' practice).** The first-printing errata [card B002, pp. 1–3]: item 3 re-proves Theorem 2.13 (linear regression error bounds) for the free-intercept model and states that the book's statement "would be valid if the regression model is of the form" m(y) = f(y⁰) + (y − y⁰)ᵀg; items 8–10 correct the Λ values in figure captions; items 13–14 replace a sentence that reconciled two Λ values by a factor-4 scaling argument with the corrected value; item 5 replaces "It is then obvious" by a pointer to arguments already seen; four readers are credited by name (Griewank, Hare, Le Digabel, Vaz). The second list [card B003, p. 1] repeats two items the second printing still carried and adds the missing definition of p̄. The addendum [card B004, pp. 1–2] supplies a derivation the book omitted, with constants that match the later erratum for book p. 69 term by term (with ‖Σ̂⁻¹‖ in place of the note's ‖M†‖). These are the authors' published corrections, not reading notes about their work, so they count as evidence of practice for the Honest Boundary lesson "check that tables, text and theorem statements agree before submitting". Candidate pattern (not promoted; one source): public, itemised self-correction that states when the original statement remains valid (08 §13.5).

**Reception (the reviewers' voice).** Orban: "bound to become the de facto authoritative text", teaching direct-search and model-based methods with their limitations, with a Part I / Part II split usable as a course order; shortcomings: theory-extending exercises, few examples, no bare-bones implementations, research-grade software, and the introduction holds "the only comparison between methods" [card B006, pp. 1–2]. Nazareth: "gracefully-written, well-organized, and timely", meeting its stated aims; shortcomings: theory-extending exercises, atypical introductory examples, few numerics, no implementation detail, no one-dimensional theory, and the DFO–non-differentiable intersection [card B005, pp. 2–3]. Full comparison: 08 §13.4; `05-peer-critique.md` §10.

**Transferable techniques recorded.** Proof device P36 (least-squares model error as pseudo-inverse × Taylor residual with diagonal Δ-scaling) [cards B004, pp. 1–2; B002, pp. 1–2] and writing moves W20–W24 in `../technique-catalog.md`; the regression device in `../proof-playbook.md` T0; the book stage of `../reading-path.md`.

<a id="corrections"></a>

## Corrections from the full texts

Each entry quotes the wording that the full texts or the 2026-09-27 review corrected (✗), then the current reading. Details: `references/research/08-deep-reading-synthesis.md` §3, §10, §12.
- **C1** ✗ Taste mark 4, "Theory is paired with head-to-head numerical comparison." → only in algorithm and software papers [card S030, p. 4].
- **C2** ✗ Taste mark 3 and Method 2 read as general → scoped to the adaptive / DFO line [cards S002, pp. 2–3; S009, pp. 3, 5].
- **C3** ✗ Method 1 step 5, "(e.g., p above 1/2-type thresholds in BSV-style analyses)" → thresholds differ by paper. A first correction also said only gradient/model failures may be arbitrary; that was wrong for first-order STORM [cards S012, p. 3; S013, p. 17].
- **C4** ✗ Method 3 steps 1–3, "1. Define a potential Φ_k (e.g., a combination of f(x_k) − f* and the step-size parameter) and indicator variables I_k = 1 for "good oracle" iterations and J_k = 1 for "accurate function estimate" iterations. 2. Show that on good iterations with a small enough step, Φ decreases by an amount tied to ε. Show that the step-size parameter behaves like a random walk biased upward when p exceeds the threshold. 3. Bound the expected number of iterations until ‖∇f‖ ≤ ε with a stopping-time / supermartingale argument." and Limitations, "steps 1–2 reconstruct the proof pattern from abstract-level descriptions and the standard form of these frameworks; check them against the full texts before relying on them." → template (a) only [cards D001, pp. 7–13; S041, pp. 16–21].
- **C5** ✗ Method 3 Stated, "Scheinberg–Xie 2023 (as in the deterministic case, SARC outperforms other stochastic adaptive methods)" → an order claim; no numerical section [cards S061, p. 3; S093, p. 3].
- **C6** ✗ Method 5, "The specific test sets and profiles used in the group's papers were **not** verified" → verified from five papers.
- **C7** ✗ Method 4 Stated and Taste mark 5, "Per search summaries, it builds on the Moré–Wild experiments showing that Powell's model-based method works well despite low-accuracy quadratic models, and argues that only minimal quality controls are needed to promote convergence and good performance (paraphrase; article title not retrieved)." → that wording and the Moré–Wild framing are Jorge Nocedal's discussion column in the same issue (p. 6), which presents the view as a summary of her essay ("As Scheinberg discusses in this issue of Optima, one needs to impose only minimal quality controls…"); Moré–Wild is not in her reference list; her own statement is p. 4 [card S143, pp. 4, 6].
- **C8** ✗ Method 4, "The same position was held for 17 years and then proved in 2025–2026." → the stance dates from 2009–2010 [card S016, p. 18].
- **C9** ✗ Method 6, "⚠️ practiced across four projects and two decades; explicit statement not found." → co-authored statements found [card S004, p. 17].
- **C10** ✗ Heuristic 4 (old numbering), "confine them to the final stage instead of eliminating them" → the criticality step (now Heuristic 2) [card S030, p. 3].
- **C11** ✗ STORM anatomy, "Third-party extensions include a nonsmooth "ProxSTORM" preprint (arXiv:2510.03187; authors unverified ⚠️)." → her own paper [card S098, p. 1].
- **C12** ✗ Lineage, "editor of Optima" → co-editor [card S143, p. 10].
- **C13** ✗ Blind spots, "nonsmooth and discontinuous objectives; … integer or categorical variables" → black-box nonsmooth and integer DFO only [cards S098, pp. 2–4; S017, pp. 7–16].
- **C14** ✗ "Feedback style: diagnostic questions first …"; "Scheinberg wants … / accepts … / Scheinberg's default for noisy problems …"; "Scheinberg is merging the two arcs" → rephrased as statements about the papers; no feedback or statement of intent was read.
- **C15** ✗ Method 7, "Prove it once for an abstract object, then instantiate by checklist" (added in the full-text pass) → Heuristic 8; exclusivity not shown [08 §4].

<a id="card-key"></a>

## Card key (ids used in SKILL.md before tightening)

Full entries (venue, DOI, arXiv, read level) are in `references/research/07-paper-cards.md`.

Ids in bold in the lists above resolve there. Other ids: **S005** Goldfarb–Ma–Scheinberg 2013, alternating linearization (Math. Program.); **S007** Conn–Scheinberg–Vicente 2009, fully linear TR framework (SIAM J. Optim.); **S008** Conn–Scheinberg–Toint 1997, DFO convergence (Powell tribute volume); **S009** Nguyen et al. 2018, SGD and Hogwild! (ICML); **S017** Günlük et al. 2021, optimal decision trees via integer programming (J. Global Optim.); **S019** Conn–Scheinberg–Toint 1998, DFO in practice (AIAA/ISSMO); **S022** Scheinberg 2006, active-set QP for SVMs, sole author (JMLR); **S024** Nguyen–Liu–Scheinberg–Takáč 2017, SARAH nonconvex (arXiv:1705.07261); **S025** Conn–Scheinberg–Vicente 2008, regression and underdetermined geometry (IMA J. Numer. Anal.); **S032** Nguyen et al. 2019, SG convergence aspects (JMLR); **S035** Wen–Goldfarb–Scheinberg 2012, BCD for SDP (handbook chapter); **S037** Nguyen–Scheinberg–Takáč 2021, inexact SARAH (Optim. Methods Softw.); **S044** Scheinberg 2022, "To randomize or not?" (INFORMS J. Comput.; abstract level); **S048** Wen–Goldfarb–Ma–Scheinberg 2009, row-by-row SDP (report); **S054** Ghanbari–Scheinberg 2018, proximal quasi-Newton rates (Comput. Optim. Appl.); **S055** Tran–Scheinberg–Nguyen 2022, accelerated shuffling (ICML); **S061** Scheinberg–Xie 2023, SARC (Winter Simulation Conf.); **S073** Tran–Nguyen–Scheinberg 2022, queueing policies (arXiv:2206.10073); **S082** Hatalis et al. 2017, quantile regression for wind power (AAAI Workshops); **S089** Ghanbari–Li–Scheinberg 2019, zero-one loss (arXiv:1903.00359; = S106); **S137** Jin–Scheinberg–Xie 2021, step-size lower bound (OPT workshop). S043 = D001, S106 = S089, S107 = S098 (same texts). Full entries: `references/research/07-paper-cards.md`.
