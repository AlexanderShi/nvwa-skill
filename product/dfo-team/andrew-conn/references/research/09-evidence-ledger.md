# Andrew R. Conn · Evidence ledger

> Date: 2026-09-27. The full evidence behind `SKILL.md`. When SKILL.md was tightened on 2026-09-27 (16455 words before, 11000 after), every long evidence list, per-paper case list, say–do tally, variant or contradiction explanation, long anatomy row and condensed step was moved here **verbatim**. SKILL.md keeps, per item, the strongest statement and cards, a one-line say–do count, at most four variant/correction bullets, and a link to the matching section below. Nothing here is new: each section reproduces the SKILL.md item as it stood before tightening, including its cross-references (method, heuristic, workflow and catalog ids are unchanged).

**How to read.** `[S019 pp. 11–12]` is paper card S019 in `07-paper-cards.md`, at the page of the text version read (often a FUNDP/Namur or IBM report or preprint); look up the journal page before citing it in a paper. Same-work pairs count once (S032 = S123, S093 = S108, S111 = S026, S126 ~ S054, S102 ~ S120). Middle-author and role-unidentifiable papers (S032/S123, S057, S003, S060, S136) carry no weight. Say–do counts are cards linked to the method, with weighted papers in brackets. `08 §N` is `08-deep-reading-synthesis.md`; technique ids (P, A, E, W, N) are in `../technique-catalog.md`; ✅ evidence, ⚠ variant, ✗ contradiction or correction.

**Scope.** Sections exist for every SKILL.md item that was condensed. Items not listed (frontmatter, How to Use, Activation Rules, Research Integrity Rules, the rest of the Research Task Routing and Agentic Protocol, the Taste quick-check, the Research Trajectory table, the Mentor Voice questions, the Roundtable Card, the Honest Boundary and the Appendix) were not condensed and remain complete in SKILL.md.

## Contents

- [Taste: marks of good research](#taste-marks)
- [Taste: warning signs of bad research](#taste-warnings)
- [Method 1: The theory–code–test triad](#method-1)
- [Method 2: Build the test bed as research infrastructure](#method-2)
- [Method 3: Certify the model — make "geometry" a condition that carries the theorem](#method-3)
- [Method 4: Enter through the user's door](#method-4)
- [Method 5: Exploit derivatives and structure before going black-box](#method-5)
- [Method 6: Transplant proven machinery and hybridize across schools](#method-6)
- [Method 7: Audit your own released solver; its named weaknesses are the next agenda](#method-7)
- [Workflow A: Problem intake and method choice](#workflow-a)
- [Workflow B: Algorithm design with certified models](#workflow-b)
- [Workflow C: Testing and benchmarking package](#workflow-c)
- [Workflow D: Diagnosing a stalled or crashing DFO solver on a real simulator](#workflow-d)
- [Workflow E: Industrial engagement](#workflow-e)
- [Workflow F: Conn-style review of a DFO paper or draft](#workflow-f)
- [Workflow G: Post-release audit and next agenda (new)](#workflow-g)
- [Heuristic 1: derivatives before DFO](#heuristic-1)
- [Heuristic 2: least squares](#heuristic-2)
- [Heuristic 3: robust as bilevel](#heuristic-3)
- [Heuristic 4: models inside direct search](#heuristic-4)
- [Heuristic 5: progressive barrier](#heuristic-5)
- [Heuristic 9: answer small questions](#heuristic-9)
- [Heuristic 10: unexplained results become conjectures](#heuristic-10)
- [Heuristic 11: extending a convergence theory](#heuristic-11)
- [Heuristic 12: use every evaluation twice](#heuristic-12)
- [Heuristic 13: failed evaluations](#heuristic-13)
- [Signature work: Recent progress in unconstrained nonlinear optimization without derivatives](#signature-work-1)
- [Signature work: Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points](#signature-work-2)
- [Signature work: LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization](#signature-work-3)
- [Signature work: JiffyTune: circuit optimization using time-domain sensitivities](#signature-work-4)
- [Signature work: CUTE: constrained and unconstrained testing environment](#signature-work-5)
- [Research anti-patterns](#anti-patterns)
- [Research trajectory](#trajectory)
- [Academic lineage](#lineage)
- [Inner tensions](#tensions)
- [Mentor voice (evidence note)](#mentor-voice)
- [Agentic Protocol, Step 2 (derivative and structure audits) and routing row](#agentic-protocol)
- [Corrections from the full texts](#corrections)

<a id="taste-marks"></a>

## Taste: marks of good research

*Condensed in:* SKILL.md › Research Taste › Marks of good research (one line per mark, at most three cards).

*Before tightening (verbatim):*

1. **Proof, code and numbers arrive together — within a line of work, rarely in one paper.**
   - Evidence: the 1988 CGT convergence paper and its testing twin, received six months apart and cross-cited [S008 pp. 1–2, 28; S011 pp. 2–3]; the 1991 augmented-Lagrangian theory, then LANCELOT (1992), then the 1996 numerical experiments [S005; S040]; Conn–Toint 1996, then CST 1997, then CST 1998, then the DFO code on COIN-OR [S019; S013; S020]. ⚠ Single papers are often theory-only or code-only; the other legs follow in companions, in either order (warning sign 2; M1 variants).
2. **Theory covers a class, not one code.**
   - Evidence: CGT 1988 treats "a class of trust region algorithms" [S008 p. 1] (title), with the class-level theory at [S008 pp. 4, 6–7, 27]; CST 1997 aims at "a general framework in which reasonable global convergence results can be obtained" [S013 p. 2]; CSV 2009 proves convergence for general derivative-free trust-region algorithms [S012 pp. 3, 7–9]; see also [S010 pp. 6–7; S031 p. 10].
3. **The problem has a real user who pays per evaluation.**
   - Evidence: circuit tuning with IBM designers, the resulting tool deployed as a standard IBM tool [S036 p. 6; S236 p. 4]; DFO motivated by "the high demand from practitioners for such tools" [S009 p. 3] and research that "clearly meets a strong and explicit need in several application areas" [S019 p. 20]; when recruited to IBM he wanted problems whose answers people were extremely interested in [S236 p. 2].
4. **The evaluation budget and noise are design inputs from the start.**
   - Evidence: Conn–Toint 1996 was designed to require few evaluations and to be relatively insensitive to noise, and was tested with and without noise [S019 pp. 2, 15–18], with a noise-aware predicted-reduction test [S019 p. 12]; radius and tolerances in physical units [S036 p. 5]; noise named as understudied, "particularly as so many industrial problems involve noisy functions" [S080 p. 17]; a noisy f inside a convergence theorem [S031 pp. 57–58].
5. **Infrastructure others can use counts as research.**
   - Evidence: CUTE [S004]; the SIF input standard [S149; S137]; a bias-controlled open benchmark protocol [S188]; LANCELOT (1994 Beale–Orchard-Hays Prize); the DFO package on COIN-OR.
6. **The model's quality is an explicit, checkable object.**
   - Evidence: the 1997 survey measures the "geometrical quality" of the model [S009 p. 11], with an attainability theorem and bounded restoration [S009 pp. 9–16]; CSV 2008 on interpolation, regression and underdetermined sets [S016; S028]; the model-improvement algorithm is part of the definition of a model class [S012 Defs 3.1, 3.3, pp. 7–9].
7. **Your own released code is the first object of critique.** (new, full texts)
   - Evidence: three weak points of LANCELOT seen in the detailed runs, two with a stated remedy, and options that "could probably be removed from future releases" [S040 pp. 49–50]; LANCELOT A's major defect named as its handling of linear constraints [S061 p. 21]; the authors' own CST 1997 geometry step called "very expensive" and replaced [S016 p. 19]; his own 1979 minimax code benchmarked and beaten by its successor [S108 pp. 17, 21] (M7).

<a id="taste-warnings"></a>

## Taste: warning signs of bad research

*Condensed in:* SKILL.md › Research Taste › Warning signs of bad research (one line per sign).

*Before tightening (verbatim):*

✗ Corrected: the first pass said no explicit critique by Conn was found. Co-authored critiques exist: the evidence rule quoted in Integrity rule 4 [S061 p. 27] and the authors' surprise at how few papers report numerical results at all [S080 p. 16]. Signs 1–3 now have stated sources; signs 4–7 remain inferred from practice.
1. A DFO heuristic with no convergence story. CSV 2009 sorts the literature into practical codes without theory and provable methods that were impractical, and sets out to close that gap [S012 p. 2]; a practical rule that "seems to work well in practice" is given provable alternatives [S016 pp. 18–19]; the 2009 book teaches convergent Nelder–Mead variants (publisher description).
2. A theorem whose algorithm never gets code or numbers anywhere in its line of work. ✗ Corrected: the first pass said a theorem with no code and no numbers never occurs in the record. Theory-only papers are common: the 1984 quasi-Newton paper declares its practical performance unknown and left to future work [S021 p. 26], and [S013 p. 22; S012 pp. 11–13; S124 pp. 27–32; S130 p. 32] carry no numbers; the 1997 barrier paper has no detailed numerical evidence, only an anecdotal report that a rudimentary implementation solved over ninety percent of about a thousand problems [S007 p. 27]. In most lines the other legs follow in companions (S005 → S040; S019, code first → S013 → S020; S012 → S025, S075); the cards show no numerical follow-up for the 1984 method.
3. Results on a handful of hand-picked problems. Counter-examples in Conn's own work: CUTE, and the 2018 study on 40 smooth problems plus engineering problems [S075 pp. 17–23]. Stated: "Smaller test sets are more likely to introduce unwanted bias and make the statistical results less useful." [S102 p. 7]; personal intervention "and thus of bias" kept to a minimum [S188 p. 3].
4. DFO used where derivatives were obtainable. Counter-example: JiffyTune and EinsTuner used simulator sensitivities and gradient-based NLP [S036 pp. 1–3; S027 p. 4]. "We strongly recommend the use of exact second derivatives whenever they are available." [S040 p. 24].
5. A structured problem treated as a pure black box. Counter-examples: least-squares DFO (2010) and bilevel DFO (2012) [S025 pp. 2, 5, 16; S066 pp. 1, 8–9]. "The fact that we are able to solve large problems at all is because they are structured." [S086 p. 5].
6. Claiming superiority where the data show only competitiveness. The 2018 progressive-barrier paper calibrates by tier: the abstract says "competitive"; the conclusion says competitive with the same-school baseline and "preferable" to the other school's on each tier, each supported by the profiles [S075 pp. 1, 22–23]. Also: "complement each other", with the authors' own weakness on linear programs stated [S102 pp. 12, 17]; where evaluation counts were comparable, a tie broken by a stated per-iteration cost argument and worded as only appearing preferable [S108 pp. 18–22]; industrial results called qualitatively similar to commercial software [S236 p. 6].
7. Results that hide where the method loses. (new, full texts) Conn's papers give the bad cases their own place: a regime where a strategy "seems to be clearly inefficient" [S049 p. 19]; a dedicated section on bad cases [S056 pp. 19–24]; the failure case of a heuristic drawn [S020 pp. 7–8]; LANCELOT's "disappointing reliability" on linear programs [S102 p. 12].

<a id="method-1"></a>

## Method 1: The theory–code–test triad

*Condensed in:* SKILL.md › Core Research Methods › Method 1 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Deliver each algorithm as a package: a class-level convergence theorem, a working code, and a numerical study, often as paired publications. The package is assembled across a line of papers, in either order, and the theory is aimed at the code actually run.
**Evidence**:
- Stated (co-authored): implementations and the analysed algorithms "should differ as little as possible" [S046 p. 11]; the 1994 rule that a practical algorithm needs evidence it competes [S061 p. 27]; the main reason for designing algorithms is to let others solve real problems, and quality software is one of the best ways to do it [S080 p. 16] (paraphrase). First person, for industrial work he names a different triad (optimization, domain experts, familiar interfaces) and does not mention convergence theory [S236 p. 4].
- Practice: the 1988 theory/testing twin [S008; S011]; CGT 1991 → LANCELOT → the 1996 study citing the theory at each step [S005; S040 pp. 7–16]; the analysed primal-dual algorithm shipped as HSL VE12, "exactly the algorithm we analysed" [S026 p. 30]; the DFO line from Conn–Toint 1996 to the COIN-OR code [S019; S013; S020].
- Say–do consistency: ✅ stated + practiced; 63 cards (58 weighted papers). ✗ Corrected: the first pass found no first-person essay; it exists [S236 pp. 1–7], so the stated side no longer rests on obituaries.
- Variants: ⚠ **Either order across a line**: theory first, with the code rudimentary and systematic numbers deferred [S005 p. 4; S007 p. 27]; code first [S019 → S013]; anomaly → theorem (H10). ⚠ **Theory aimed at the code actually run** (10 papers): step 2, also for devices already in use [S028 p. 2; S016 pp. 18–19, 24]. ⚠ **Industrial triad**: convergence inherited from CGT theory [S036 p. 4].
**Steps**:
1. Write the algorithm as a *framework*: list the minimal properties each step and model must satisfy (a fraction of Cauchy decrease, an inner stopping test on a criticality measure, a model class defined by error bounds), not one fixed code [S008 pp. 3–4; S005 pp. 7, 27; S012 pp. 7–8].
2. Prove global convergence for the framework, and turn the assumptions into a checklist the code must enforce. Aim the framework at the code you will run: make its abstract tests contain the native tests of the packages you target, and prove that the native tests imply them [S022 pp. 26–29; S107 p. 25].
3. Build a reference implementation that enforces exactly that checklist and exposes the algorithmic options. Record every deviation from the analysed algorithm and check it against the theory [S011 p. 5; S026 p. 30].
4. Run a numerical study that compares the options on a shared collection. If it is large, publish it as a companion paper, with the complete per-run results in a report [S040; S103]. (Former H6, *finish a convergence theory, then write its testing companion*; cases [S008 + S011; S006 + S040; S113 + S107; S025 + S065].)
5. When tests fail, go back to step 1 and fix the assumptions or the framework. Do not patch the code silently. When tests show a win the theory does not explain, make it the next theorem (H10).
**Applies to stage**: algorithm design, experiments, writing.
**Different from standard practice**: many groups publish either the theorem or the code. Conn's record repeatedly publishes both as twins within a few years, on shared infrastructure, and builds the abstract theory to cover the stopping tests of existing packages.
**Limitations**: slow (CSV 2008 took about 18 months from submission to acceptance), and a line can take several papers and years. It relied on long-lived trios (CGT, CST/CSV) [08 §9]. Smooth convergence theory may say little about nonsmooth or noisy engineering blackboxes. In industrial projects Conn himself names a different triad (optimization, domain experts, interfaces) [S236 p. 4].

<a id="method-2"></a>

## Method 2: Build the test bed as research infrastructure

*Condensed in:* SKILL.md › Core Research Methods › Method 2 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Before claiming anything, make (or adopt) a shared, public problem collection and input format, and test on it together with noisy and engineering cases.
**Evidence**:
- Stated (co-authored): "We believe that the important figures in such a comparison are the number of function and gradient calls required to solve the problem." [S011 p. 22]; "Smaller test sets are more likely to introduce unwanted bias and make the statistical results less useful." [S102 p. 7]; format differences "could be a major obstacle to valid comparisons between competing optimization codes" [S137 p. 2]. First person: the MINLP project's first objective was an open-source package with test problems [S236 p. 5].
- Practice: CUTE (1995) as a classified, solver-agnostic product with interfaces to rival codes [S004 pp. 4–25]; the LANCELOT options study with coded failures [S040 pp. 27–39]; LANCELOT vs MINOS on 913 problems, with MINOS's author as coauthor [S102 pp. 2, 7–13; S120]; a bias-controlled open protocol [S188 pp. 3–9]; noise at two levels [S019 pp. 15–18]; data profiles with deterministic noise [S025 pp. 17–19]; two tiers with baselines from both schools [S075 pp. 17–23].
- Say–do consistency: ✅ stated + practiced; 41 cards (36 weighted papers). ✗ Corrected: in the 2018 study both baselines (COBYLA, NOMAD) ran on both tiers, not one each [S075 pp. 17–23].
- Variants: ⚠ **No noisy tier before DFO** [S004 pp. 6–8; S040 pp. 30–31]. ⚠ **First paper in a new problem class**: "An astute reader will notice that there are no comparisons with competing methods — this is because such methods appear not to exist." [S066 p. 19]. Disclose the missing baseline rather than invent one.
**Steps**:
1. Fix the evaluation unit the user pays for: function evaluations or simulations when evaluations are expensive, not iterations; CPU and linear-algebra counts when they are cheap. If two units disagree, report both [S011 p. 22; S020 p. 10; S120 pp. 28–50].
2. Tier 0: check the formulation and each new component on a prototype with known answers (exact gradients, synthetic sequences, a subclass with known baselines); size a synthetic model to expose the difficulties but keep iteration fast [S027 p. 5; S010 pp. 14–19; S026 p. 30; S236 p. 6].
3. Tier 1: a public collection (CUTE lineage, or the Moré–Wild set), selected by class strings rather than by hand, with noisy variants at two levels and the baseline told the same noise level [S004 pp. 8–10; S019 pp. 17–18; S025 pp. 17–19]. If you release a solver, release the collection and its input format with it (former H7; cases: CUTE with SIF problems for LANCELOT [S004 pp. 2–4; S149 pp. 4, 68]; the MINLP package with test problems [S236 p. 5]).
4. Tier 2: real engineering or application instances. Report the tiers separately, and disclose excluded problems and infeasible starting points [S020 pp. 8–10; S075 pp. 17–19].
5. Pick the baseline from the *competing* school (model-based vs direct search, e.g. COBYLA and NOMAD as in 2018), and be fair to it: invite its author, declare your own-code expertise bias, fix the problem list and the defaults in advance [S102 p. 2; S061 p. 25; S188 pp. 5, 7].
6. Report per-option results (one change from the default at a time), coded failures, and where the method loses; put complete per-run data in a companion report [S040 pp. 32–39; S103 pp. 1–2; S049 p. 19].
**Applies to stage**: experiment design, results judgement.
**Different from standard practice**: the test environment is treated as a publishable, reusable research product, not a private script, and a second tier of noisy and industrial instances is required.
**Limitations**: the 1990s CUTE style predates data profiles. Add Moré–Wild data profiles (2009) for budget-limited DFO, as Conn's own later papers do [S025 pp. 17–19; S075 pp. 17–19]. Building an environment is a large, team-scale effort; individual researchers should adopt one rather than build one.

<a id="method-3"></a>

## Method 3: Certify the model — make "geometry" a condition that carries the theorem

*Condensed in:* SKILL.md › Core Research Methods › Method 3 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Turn the heuristic part of model-based DFO (is my interpolation model any good?) into an explicit, algorithm-independent quality condition. Then prove convergence once for every algorithm that maintains it.
**Evidence**:
- Stated (co-authored): "The main task of such a derivative free algorithm is to maintain an interpolation sampling set so that this constant remains small, and at least uniformly bounded." [S016 p. 1]; "In practical situations only the geometry of the interpolation set is controllable." [S124 p. 32]; "The abstraction highlights, in our opinion, the fundamental requirements for obtaining the appropriate convergence results." [S012 p. 13].
- Practice: steps 1–4 already in CST 1997 [S013 pp. 11–17]; an attainability theorem, and the radius cut only when the model was adequate [S009 pp. 9–16]; Λ-poisedness with a repair algorithm [S124]; one-point repairs [S016 pp. 19–23]; regression and underdetermined models [S028]; the improvement algorithm inside the definition of a model class [S012 pp. 7–9]. Payoff of step 4: later papers prove only the structure-specific lemma [S025 p. 12; S066 p. 3; S075 p. 25].
- Say–do consistency: ✅ stated + practiced; 24 cards (24 weighted papers).
- Variants: ⚠ **Before DFO**, certified interfaces already carried the theorems (a Cauchy-decrease fraction, inner-solve tests, a gradient error ≤ κΔ) [S008 p. 7; S022 pp. 26–28; S031 pp. 6–7]. ⚠ **Step 5 unmeasured**: only a qualitative remark that bad-pivot replacements are rarely necessary [S012 p. 12], and the measurement listed as future work in 2018 [S075 p. 23]. ⚠ **Own devices superseded**: the CST 1997 step "very expensive" [S016 p. 19], its gradient bound "clearly inferior" [S124 pp. 26–27] (M7). "Fully linear" is the papers' own term, not later literature's [S020 pp. 4–5; S012 Defs 3.1, 3.3].
**Steps**:
1. Write the Taylor-like error bounds your model must satisfy within the trust region (value and gradient, plus Hessian for second order).
2. Choose the model type by regime, then identify the geometric property of the sample set that guarantees those bounds for it [S028 pp. 1–2]:
   - expensive evaluations → underdetermined minimum-norm (minimum-Frobenius) models, as in the COIN-OR DFO code and Powell's codes;
   - cheap but noisy evaluations → regression on more points than basis functions; if re-sampling the same point does not reduce the noise, regress on spread, well-poised points instead [S028 p. 27];
   - avoid best-sub-basis selection: it is not robust to small perturbations of the sample set, while the minimum-norm solution is [S028 pp. 19–20].
   Measure the property with quantities the model construction already produces, such as factorisation pivots with a threshold [S009 pp. 14–15; S016 pp. 19–23].
3. Give the algorithm a *model-improvement* step that restores the property in a bounded number of evaluations. Add a *criticality* check that forces the model to be certified before small gradients are trusted (Δ ≤ μ‖g‖) [S012 pp. 13–14, 18–19]. Shrink the radius only if the model was certified when the step was computed; otherwise repair and keep the radius [S009 pp. 9–10; S020 pp. 4–5].
4. Prove convergence using only the certified-model property, so the model builder can be swapped out. State the interface as error bounds plus a finite, uniformly bounded improvement procedure [S012 Def. 3.1, pp. 7–8]. The proof skeleton is in Workflow B step 4.
5. Measure how often the improvement steps fire on real runs. They cost evaluations; report the cost (see Workflow D). Conn's own papers left this as future work [S075 p. 23].
**Applies to stage**: idea generation, algorithm design, debugging.
**Different from standard practice**: many practical codes manage geometry by internal heuristics. This method elevates it to the interface between theory and code.
**Limitations**: Fasano, Morales and Nocedal (2009) showed a code that skips the geometry phase entirely can perform well on smooth problems. Scheinberg and Toint (2010) showed geometry steps can be confined to the criticality stage. Both mean explicit maintenance may cost more evaluations than it saves. Conn's own papers concede this: the new geometry algorithms may not outperform Powell's rule [S016 p. 23]. The noise benefit of regression is argued in the geometry paper (a consistency result), not tested there [S028 p. 17]. The method assumes smoothness and is weak on nonsmooth, discontinuous or strongly noisy blackboxes.

<a id="method-4"></a>

## Method 4: Enter through the user's door

*Condensed in:* SKILL.md › Core Research Methods › Method 4 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Find problems by being the approachable optimizer inside an engineering organisation. Then formulate their task as a well-posed program and deliver a tool they use daily.
**Evidence**:
- Stated (first person, 2007 essay): "I said it was very interesting but it was too bad that they were using 1960s algorithms in the 1990s and so I was asked to tell them about 1990 algorithms." [S236 p. 3]; software in the users' own environment outranks a factor-two gain (top quote) [S236 p. 4]. Co-authored: "The designers’ focus shifts from solving the optimization problem to specifying it correctly and completely." [S036 p. 1]. (The first pass had these as MAM 2015 paraphrases.)
- Practice: JiffyTune → EinsTuner (TCAD 1998; DAC 1999; FGCS 2005), with adoption reported as 41 designers on 168 circuits [S036 pp. 1, 5–6; S027 pp. 1, 8]; Boeing problems at an AIAA MDO symposium [S020 pp. 1–3]; air-traffic models with ENAC [S099; S141]. ✗ No weight: S060, S057 and S136, which the first pass listed.
- Say–do consistency: ✅ stated + practiced; 20 cards (15 weighted papers plus the essay).
- Variants (single source, the essay; catalog N2–N6): the next topic taken from the users' next structural change (the MINLP project) [S236 p. 4]; low-stake pilots [S236 p. 6]; an eighteen-month survival fight, won with his immediate management's support and through the engineers [S236 pp. 3–4]; after adoption he "yearned to make a splash in a new area" [S236 p. 5]. From the papers: problems harvested through a software licence [S004 p. 4].
**Steps**:
1. Answer small optimization questions from engineers generously. Record the ones that recur [S236 p. 3].
2. Sit in the users' own meetings or workshops and write their pain in their words. His circuit users described manual tuning as slow, tedious and error-prone [S236 p. 4]; the 1996 paper says "slow, tedious and iterative" [S036 p. 1]. Compare the vintage of their algorithms with the state of the art; that gap is the entry [S236 p. 3].
3. Formulate the problem mathematically (objective, constraints, bounds, where derivatives come from) and get the users to sign off on it. Make tacit requirements explicit, because the optimizer exploits every aspect left unspecified [S036 pp. 2, 6].
4. Wrap a general-purpose solver in a user-facing tool inside the users' own environment: problem specification from their data, and recovery from failed designs (JiffyTune; H13) [S036 p. 5; S027 p. 5].
5. Define success as adoption and report it (users, sessions, distinct problems, runs) [S036 p. 6]. The essay's circuit-tuning tool became a standard IBM tool used on all custom circuits [S236 p. 4] (the essay does not name it; it is identified with the EinsTuner line via FGCS 2005). Swap the internal solver when a better one appears (LANCELOT → IPOPT [S236 p. 4]). (Single source, 2007 essay; catalog N4: let the domain experts carry the technical case to management [S236 pp. 3–4].)
**Applies to stage**: problem choice, deployment, research agenda.
**Different from standard practice**: the application is not a demo section in a methods paper. It is a multi-year engineering product co-owned with domain experts and published in *their* venues (IEEE TCAD, DAC, AIAA).
**Limitations**: it depended on IBM's in-house access to designers and simulators; in his own words the circuit project would not have happened in an academic environment [S236 p. 4]. An academic user needs a partnership agreement and data access. It is a senior-researcher strategy: early-career researchers should start with one well-scoped partner problem. The 2006–2015 energy practice rests on abstracts and the essay; the two full texts from that period do not identify his role [S060; S136].

<a id="method-5"></a>

## Method 5: Exploit derivatives and structure before going black-box

*Condensed in:* SKILL.md › Core Research Methods › Method 5 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Treat "derivative-free" as a last resort. First extract gradients from the simulator, and exploit problem structure (least squares, bilevel, bounds) in the model.
**Evidence**:
- Stated (co-authored): "The fact that we are able to solve large problems at all is because they are structured." [S086 p. 5]; without a fast time-domain sensitivity engine EinsTuner would not have been possible [S027 p. 4] (paraphrase); structure-exploiting interpolation methods are recommended for least squares [S025 p. 21] (paraphrase). First person: derivatives were the decisive argument for the in-house simulator [S236 p. 3].
- Practice: the flagship circuit tool gradient-based via adjoint sensitivities [S027 pp. 4–5; S036 pp. 1–3]; cheap constraints exact [S020 pp. 6–7]; bounds and linear constraints outside the penalty [S005 pp. 1–2; S022 pp. 2–3]; per-residual models [S025]; nested structure [S066].
- Say–do consistency: ✅ stated + practiced; 50 cards (44 weighted papers plus the essay).
- Variants: ⚠ **Split by type** (step 4 generalised; 12 weighted papers; catalog A4). ⚠ **Structure of the solution** in the Waterloo minimax work (catalog A5–A6) [S233; S130]. ⚠ **Model f rather than estimate derivatives**: "This simple example indicates that it may not be optimal to use function values to compute explicit derivative approximations." [S009 p. 4].
**Steps**:
1. Map which parts of the function are analytic, which come from a simulator, and whether the simulator can produce sensitivities or adjoints. Write the triage in one sentence per route with the reason each fails or works [S009 pp. 3–4; S019 p. 3].
2. If affordable gradients exist, use gradient-based NLP (historically LANCELOT; later IPOPT in the same IBM tool) and stop here. Choose direct or adjoint sensitivities by the ratio of parameters to functions; for a scalar merit function one adjoint analysis gives all gradients [S036 p. 3; S039 p. 4].
3. Otherwise, write the objective in its natural composite form (sum of squares, max, bilevel) and model the *components*, not the scalar (H2). Reformulate first: max → epigraph constraints [S036 p. 5; S027 p. 2]; robust min–max → bilevel [S066 pp. 16–17].
4. Handle cheap constraints (bounds, analytic and linear constraints) exactly, inside the subproblem, so no evaluation is spent on an infeasible point. Model only the expensive ones [S020 pp. 6–7; S022 pp. 2–3].
5. Pure black-box treatment is only for what is left.
**Applies to stage**: problem choice, algorithm design.
**Different from standard practice**: many DFO users reach for a black-box solver first. Conn's record shows the flagship industrial project was *not* derivative-free.
**Limitations**: needs access to simulator internals or problem structure, which proprietary codes may not give. Extracting structure takes engineering time that a small project may not have.

<a id="method-6"></a>

## Method 6: Transplant proven machinery and hybridize across schools

*Condensed in:* SKILL.md › Core Research Methods › Method 6 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: Carry mature tools (trust regions, penalty and augmented-Lagrangian ideas) into new settings, and borrow the rival school's best device instead of competing with it.
**Evidence**:
- Stated (co-authored): the authors find it "rather strange" that the augmented-Lagrangian shift had not been applied to barriers [S007 p. 5]; the 2018 paper with Audet, Le Digabel and Peyrega: "Given a very badly behaved function we would use a direct-search method. If the function can be adequately approximated by a smooth function we would prefer a model-based approach unless it is essential to exploit some parallel architecture." [S075 p. 2].
- Practice: trust regions carried into DFO [S012 pp. 2–3]; the shift from penalties to barriers [S007 pp. 5–6]; Chebyshev theory to nonlinear minimax [S130; S164]; LP primal-dual machinery to nonconvex NLP [S054; S026]; the progressive barrier moved into a trust region [S075 pp. 3, 13, 20]; Conn–Le Digabel models as NOMAD's default [S075 p. 19].
- Say–do consistency: ✅ stated + practiced; 49 cards (42 weighted papers).
- Variant: ⚠ step 4 is not what the 2018 hybrid achieved: its theorem is weaker than either parent's (one radius sequence tends to zero) [S075 pp. 15–16], and the imported device had to be retuned [S075 pp. 13, 20].
**Steps**:
1. List your mature tools, with the assumptions each needs to work.
2. For a new setting, ask which assumption fails (no derivatives, hidden constraints, nonsmoothness) and whether a certified surrogate can restore it (see M3).
3. List the rival school's strongest device, e.g. MADS's progressive barrier or its polling robustness. Apply the rule stated in the 2018 paper with Audet, Le Digabel and Peyrega: badly behaved → direct search; adequately smooth → model-based, unless parallel evaluation is essential → direct search [S075 p. 2].
4. Build the hybrid in whichever direction keeps the stronger convergence theory: models as a *search step* inside MADS, or a barrier inside a trust region. Retune the imported device to the host's evaluation economy [S075 pp. 13, 20], and if the hybrid's theory ends up weaker than either parent's, say so [S075 pp. 15–16].
5. Benchmark the hybrid against both parent methods on two tiers of problems (M2), and report per tier which parent it matches and which it beats, as the 2018 conclusion does [S075 pp. 22–23].
**Applies to stage**: idea generation, research agenda.
**Different from standard practice**: the usual move is to defend one's own school. Conn co-authored with the MADS group and with MINOS's author [S102 p. 2], and reused his own 1970s–90s tools decades later.
**Limitations**: hybrids inherit the weaker parent's assumptions in places. The 2018 hybrid won by tier, not across the board: competitive with the same-school baseline and preferable to the other school's on each tier [S075 pp. 22–23], with a theorem weaker than either parent's [S075 pp. 15–16]. It needs deep fluency in both schools, which is usually a team asset.

<a id="method-7"></a>

## Method 7: Audit your own released solver; its named weaknesses are the next agenda

*Condensed in:* SKILL.md › Core Research Methods › Method 7 (strongest statement, 3–5 practice cards, say–do count, at most four variants or corrections; Steps and Limitations condensed).

*Before tightening (verbatim):*

**One line**: After each release, run your own code on the shared test set and on the hardest real case, print its weak points (with a planned fix where you have one), make each fix the next paper, and say in print when a newer method, yours or someone else's, supersedes your old one.
**Evidence**:
- Stated (co-authored and first person): three LANCELOT A weak points seen only in the detailed runs, two with a stated remedy, and options that "could probably be removed from future releases" [S040 pp. 49–50]; the package's major defect named [S061 p. 21]; own step "very expensive" [S016 p. 19], own bound "clearly inferior" [S124 pp. 26–27]; "our previous linesearch algorithm" named as the cause of an old failure [S026 p. 33]. First person: "age is often a negative attribute" [S236 p. 5].
- Practice (15 papers, 1989–2009, plus the essay): the full mechanism in LANCELOT (9 papers: named weak points, a 117-hour run, a code shortcut and an observed regularity each became a paper [S040 p. 49 → S089, S007; S061 p. 15; S022 p. 2; S054 p. 2 → S026 p. 33; S058 p. 3; S074 p. 3]) and in minimax (2 papers: a failure mode of his 1978 method → the Conn–Li method, which beat his 1979 code [S164 p. 21; S108 pp. 17, 21]). Step 5 alone in location [S017 p. 2], DFO (the stated items above; [S012 p. 2]) and circuits (LANCELOT → IPOPT, essay only [S236 pp. 4–5]).
- Say–do consistency: ✅ stated + practiced; 16 cards (15 papers plus the essay). Four-way validation (08 §4): recurrence, say–do and executability ✅; exclusivity ⚠ plausible, indirect evidence only [S080 p. 16]: the move is shared with Gould and Toint and close to the Powell lens (each solver removes a measured limitation) and the Vicente lens (publish the boundary, then attack it). Conn-specific: the numbered weak-points list inside the testing paper, and the sizing of fixes (step 3).
**Steps**:
1. Run the released code with defaults on the whole public collection and on the worst real case you have; record failures with numbers (problem, size, hours) [S061 p. 15; S040 pp. 34–39].
2. In the testing paper, add a numbered weak-points list. Give a planned fix where you have one, and say where you have none; name the options the data do not support [S040 pp. 49–50].
3. Size each fix: an algebraic inefficiency → a short note tied to the released code [S089 pp. 4, 8–9]; a design shortcut → a theory paper that removes it [S022 p. 2]; a structural failure → a new method, then its successor if it fails in turn [S054 p. 2 → S026 p. 33].
4. When the code shows a good behaviour the theory does not explain, make it the next theorem and aim it at the next release [S074 pp. 3, 25] (H10).
5. When a new method replaces your earlier one, benchmark against the earlier one and say so [S108 pp. 17, 21; S017 p. 2; S016 p. 19; S124 pp. 26–27]. Inside a user's tool, swap in the better solver even if the old one is yours (former H8; case [S236 pp. 4–5]).
6. Publish the agenda: close surveys with the group's own next projects [S009 p. 17; S061 pp. 15–22; S086 pp. 15–16; S080 pp. 16–17].
**Applies to stage**: research agenda, problem choice after a release, writing (testing papers, surveys).
**Different from standard practice**: the multi-year agenda comes from public self-critique of released software, not only from gaps in others' papers. How rare this is elsewhere is not established by the cards; the only related evidence is the group's remark that few papers report numbers at all [S080 p. 16].
**Limitations**: needs a released code with users and a shared test set (team-scale; an individual researcher can apply it to one published code and one benchmark). It can lock a group into incremental repairs of one package: much of the CGT group's 1992–2000 output repairs or extends LANCELOT [S089; S007; S022; S054; S058; S074; S082; S085] (proportions in 08 §8.1). It is shared with Gould and Toint and close to moves in the Powell and Vicente lenses, so it cannot be attributed to Conn alone. The DFO line did not report the matching measurement (how often geometry steps fire) [S075 p. 23].

<a id="workflow-a"></a>

## Workflow A: Problem intake and method choice

*Condensed in:* SKILL.md › Stage Workflows › Workflow A (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: problem description (variables, objective, constraints), the simulator, evaluation cost, noise level, budget, parallel capacity.
**Steps**:
1. Derivative audit (M5), one sentence per route [S009 pp. 3–4; S019 p. 3] (W3). If gradients are affordable, recommend gradient-based NLP and stop. If the simulator gives sensitivities, choose direct or adjoint by the ratio of parameters to functions [S036 p. 3] (A12).
2. Structure audit (M5). Is it least squares (H2), bilevel or robust (H3)? Max-type, which can become an epigraph formulation [S036 p. 5] (A11)? Are bounds and analytic constraints separate from simulated ones?
3. Smoothness and noise check. Re-evaluate a few points, and perturb slightly to catch deterministic noise (the number of points is a rule of thumb, not from the papers). Apply the rule of the 2018 paper co-authored with Audet, Le Digabel and Peyrega: badly behaved → direct search; adequately smooth → model-based, unless it is essential to exploit parallel evaluation → direct search [S075 p. 2]. Use the parallel capacity from the cost audit here. If nonsmooth, noisy or with hidden constraints, consider a hybrid (M6).
4. Fix the budget in evaluations, the success criterion in the user's words (M4), and the smallest meaningful change of each variable in physical units [S036 p. 5] (A18).
5. Pick a primary method and one baseline from the other school (M2).
**🔴 Checkpoint**: if you cannot state the evaluation budget and the success criterion, or the user can supply gradients but prefers "black-box" for convenience, stop and resolve that first.
**Output**: a one-paragraph verdict (DFO yes or no; which family), the structure to exploit, the baseline, the budget, and the main risk.

<a id="workflow-b"></a>

## Workflow B: Algorithm design with certified models

*Condensed in:* SKILL.md › Stage Workflows › Workflow B (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: a new DFO algorithm idea (model type, step computation, constraint handling), or a convergence proof that is stuck.
**Steps**:
1. Write it as a framework: specify each component only by the checkable property the proof uses, e.g. a fraction of Cauchy decrease and a model class defined by error bounds plus a finite improvement procedure [S012 pp. 5–9; S013 p. 13] (M1, M3; A1, P1).
2. Choose the model type by the regime rule of M3 step 2 (expensive → minimum-norm underdetermined; cheap and noisy → regression [S028 pp. 1–2, 27]) and the matching geometry condition (CSV 2008 ×2).
3. Specify the model-improvement and criticality steps, and bound their cost. The radius shrinks only if the model was certified [S009 pp. 9–10; S020 pp. 4–5] (A7); couple Δ ≤ μ‖g‖ at small gradients [S012 pp. 13–14] (P5).
4. Prove global convergence using only the certified-model property, link by link (catalog §1; the CSV 2009 order [S012 pp. 13–21; S013 pp. 16–22]):
   - P1: every step achieves a fixed fraction of the Cauchy decrease of the model;
   - P2: the radius stays bounded below while the gradient is bounded away from zero (argue from the first iteration that violates the bound);
   - P3: count over successful iterations to get liminf ‖g‖ = 0;
   - P5: the criticality coupling Δ ≤ μ‖g_model‖ carries model-gradient convergence to the true gradient;
   - P4: liminf → lim by interleaved subsequences;
   - P16 if f is inexact or noisy: keep the inexactness below a fraction of the predicted decrease.
   When stuck, find the link that fails; it names the missing model or algorithm property, usually A7 (radius cut only when certified) or the criticality step. If you extend an existing theory, re-prove only the lemmas whose assumptions change and map the rest by number (H11; P15) [S025 p. 12; S022 pp. 13–15].
5. Decide which rival-school device, if any, to import (M6), and plan to retune it to your evaluation economy [S075 pp. 13, 20] (A15).
6. Put evaluation economy (H12) and failure handling (H13) into the algorithm box, not into the code afterwards.
7. Plan the numerical companion before proving everything (M1 → Workflow C). After the algorithm, add numbered comments on what practical codes do differently and on your own weak spots [S013 pp. 15–16; S019 pp. 13–15] (W1).
**🔴 Checkpoint**: if the proof needs a property your code cannot check or enforce, redesign. Do not publish a theorem about a different algorithm from the one you run. Positive form: the abstract tests should contain the native tests of the code you run, with a lemma that the native tests imply them [S022 pp. 26–29; S107 p. 25].
**Output**: algorithm framework, list of assumptions, proof skeleton with the failing link named, and the list of code-enforced conditions.

<a id="workflow-c"></a>

## Workflow C: Testing and benchmarking package

*Condensed in:* SKILL.md › Stage Workflows › Workflow C (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: an implemented solver or prototype, and candidate test problems.
**Steps**:
1. Fix the cost unit and the convergence test (M2 step 1) [S011 p. 22; S020 p. 10] (E5).
2. Tier 0: an analytic prototype, synthetic inputs, or a subclass with known baselines (M2 step 2) (E10).
3. Tier 1: a public collection (CUTE lineage or the Moré–Wild set) selected by class, noiseless and at two noise levels, with the baseline told the true noise level [S019 pp. 17–18; S025 pp. 17–19] (E7).
4. Tier 2: two or more engineering or application instances with realistic budgets. Disclose excluded problems and infeasible starting points [S075 pp. 17–19] (E13).
5. Internal study first: one change from the default at a time, or a factorial of your own variants, before any external comparison [S040 pp. 32–34; S075 pp. 19–22] (E2).
6. Baselines: at least one model-based and one direct-search code. Verify their current versions with tools. Apply the fairness protocol of M2 step 5 (E9).
7. Report every option setting, coded failures (stall, infeasible, budget, crash) with a same-answer filter, budget exhaustion, and where the method loses; put complete per-run results in a companion report [S040 pp. 34, 38; S102 pp. 12–14; S103] (E3, E4, E14).
8. Summarise with performance or data profiles (for constrained problems count feasible points only [S075 pp. 17–19]), and state the claim strictly according to the evidence: "competitive", "complement each other", "comparable", and "preferable" only on the tier or measure that supports it [S075 pp. 1, 22–23; S102 p. 17] (W6). Keep package-specific and general conclusions apart [S040 p. 50].
**🔴 Checkpoint**: if the method wins only on hand-picked problems, or only when measured in iterations, stop. Do not claim improvement; return to Workflow B.
**Output**: test plan table (problems × solvers × budgets), reporting template, and the claim wording.

<a id="workflow-d"></a>

## Workflow D: Diagnosing a stalled or crashing DFO solver on a real simulator

*Condensed in:* SKILL.md › Stage Workflows › Workflow D (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: run logs (points, values, trust-region radii, failed evaluations), solver settings, the simulator's behaviour.
**Steps**:
1. Check the noise level at the stall point: re-evaluate the same point (stochastic noise) and evaluate along a short line of tiny perturbations (deterministic computational noise, where re-evaluation returns the identical value; the estimation is generic, not Conn-style). Feed the result to the solver as absolute and relative noise levels; if the predicted reduction is not larger than the noise, improve the model instead of evaluating the step [S019 pp. 11–12] (M2, M3).
2. Check model quality: the conditioning of the interpolation or regression system, how often improvement steps fire, and whether the radius was cut while the model was uncertified [S009 pp. 9–10; S020 pp. 4–5] (M3; A7).
3. Check failed evaluations: does the simulator return a failure code, are failures counted in the budget, and does the solver cut the radius and retry (H13) [S020 pp. 7–8, 10; S027 p. 5]?
4. Check for hidden structure the solver ignores: least squares (switch to per-residual models, H2), bounds hit repeatedly, cheap constraints evaluated through the simulator, points sampled for geometry but never used as iterates (M5, H12).
5. Check scaling and tolerances against the simulator's natural resolution: set the initial trust-region radius, feasibility and bound tolerances and the stopping step length to the smallest meaningful move of each variable, not machine precision [S036 p. 5] (A18).
6. If the function is nonsmooth or has hidden constraints, try a direct-search or hybrid alternative (M6).
**🔴 Checkpoint**: if geometry-improvement steps take most of the evaluations with no decrease (the share is a rule of thumb, not from the papers), or the predicted reduction stays at the noise level [S019 p. 12], stop tuning the current method. Switch the model type by the regime rule of M3 step 2 (regression on spread points when re-sampling does not reduce the noise [S028 p. 27]) or switch the family.
**Output**: ranked diagnosis, each item with a specific test to run and a fallback method.

<a id="workflow-e"></a>

## Workflow E: Industrial engagement

*Condensed in:* SKILL.md › Stage Workflows › Workflow E (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: a partner organisation, its problem, and its tools.
**Steps**:
1. Attend the partner's own working meetings and record the current manual process, its costs, and the vintage of the algorithms in use [S236 p. 3] (M4; N1).
2. Co-write the mathematical formulation and get sign-off. Make tacit requirements (area, power, ratios, regularity) explicit [S036 pp. 2, 6].
3. Prototype with a general-purpose solver behind the partner's own interface, including recovery from failed designs (H13). Validate final designs with a higher-fidelity reference simulator [S036 pp. 2, 6] (E10).
4. Measure adoption (users, sessions, distinct problems, runs) and time saved, not only optimality [S036 p. 6; S027 p. 6] (E12).
5. Publish in the partner's venue as well as in optimization venues.
6. For a new area, start with a low-stake pilot with a small investment from the partner, and a right-sized synthetic model before the real case (single source: 2007 essay [S236 p. 6]; catalog N5, E10).
**🔴 Checkpoint**: if the partner cannot supply a way to run simulations and an acceptance criterion within the first phase, do not start algorithm research. Re-scope first.
**Output**: problem charter (formulation, data access, success metric, solver choice, publication plan).

<a id="workflow-f"></a>

## Workflow F: Conn-style review of a DFO paper or draft

*Condensed in:* SKILL.md › Stage Workflows › Workflow F (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: the manuscript.
**Steps**:
1. Is there a theorem, a code and numbers (M1)? Which is missing, and does the line of work deliver it elsewhere (a theory-only paper is acceptable if a companion supplies code and numbers)?
2. Does the theorem cover the algorithm actually implemented, including its stopping tests [S022 pp. 26–29]? Are the model-quality conditions enforced in the code (M3)?
3. Is the test set public and two-tier, with a cost unit of evaluations, baselines from both schools and a declared fairness protocol (M2)?
4. Could derivatives or structure have been used (M5)?
5. Does the claim wording match the evidence ("competitive" vs "better")? Are proved and merely observed behaviour kept apart [S074 p. 3; S011 p. 20] (W7)? Are failures and losing regimes reported (warning sign 7)?
**🔴 Checkpoint**: if the paper claims superiority on fewer than a public collection's worth of problems, or measures in iterations only, recommend major revision.
**Output**: review memo: summary, three main issues mapped to M1, M2, M3 and M5, and requested experiments.

<a id="workflow-g"></a>

## Workflow G: Post-release audit and next agenda (new)

*Condensed in:* SKILL.md › Stage Workflows › Workflow G (card references moved to the method steps it points to).

*Before tightening (verbatim):*

**Input**: a released solver or tool (or a finished project's code), its test collection, and the hardest real case you have.
**Steps**:
1. Run the defaults on the whole public collection plus the worst real case; code failures by cause and record size and time [S040 pp. 34–39; S061 p. 15] (M7 step 1; E3).
2. Write the numbered weak-points list; give a planned fix where you have one and say where you have none; name the options the data do not support [S040 pp. 49–50].
3. Classify each weak point: algebraic inefficiency → short note; design shortcut → theory paper; structural failure → new method [S089; S022 p. 2; S054 p. 2] (M7 step 3).
4. List behaviour of the code that the theory does not explain; write each as a conjecture with the reason it is hard (H10) [S011 p. 20; S074 p. 3].
5. For every successor, benchmark it against your own earlier method and say plainly which supersedes which [S108 pp. 17, 21; S016 p. 19].
6. Publish the agenda: the weak-points list in the testing paper, or a survey that closes with the group's next projects [S009 p. 17; S080 pp. 16–17] (W5).
**🔴 Checkpoint**: if the weak-points list is empty, the test set is too easy or too small; extend it before planning (M2). If the last few projects were all repairs of the same package (how many is a rule of thumb, not from the papers), check whether the users' problem has moved before starting another (M4; Tension 5).
**Output**: weak-points table (symptom, evidence, planned fix, paper type, priority), a conjecture list, and a one-year agenda.

<a id="heuristic-1"></a>

## Heuristic 1: derivatives before DFO

*Condensed in:* SKILL.md › Research Heuristics › H1 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

H6–H8 were folded into M1 step 4, M2 step 3 and M7 step 5; ids are kept stable.

- **H1 · If affordable gradients can be obtained from the simulator, then use gradient-based NLP, not DFO. If the optimizer needs only the gradient of a scalar merit function, weight the adjoint excitations by the multipliers and run one adjoint analysis; choose direct or adjoint sensitivities by the ratio of parameters to functions.**
  - Case: JiffyTune (IEEE TCAD 1998) and EinsTuner (DAC 1999) used time-domain sensitivities with a general NLP solver [S036 pp. 1–3; S027 p. 4]; one adjoint for all merit-function gradients [S039 pp. 3–4; S077 abstract]; derivatives as the decisive argument for the in-house simulator [S236 p. 3]. Nuance: modelling f can beat estimated derivatives per evaluation [S009 p. 4].

<a id="heuristic-2"></a>

## Heuristic 2: least squares

*Condensed in:* SKILL.md › Research Heuristics › H2 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H2 · If the objective is a sum of squares of simulated residuals, then model each residual separately on one shared sample set, and switch the model Hessian by regime.**
  - Case: Zhang, Conn, Scheinberg, *SIOPT* 20:3555–3576 (2010): all residual models share one sample set of 2n+1 points with minimum-Frobenius updates, so the extra models cost storage but no evaluations [S025 pp. 2, 16–17]; the model Hessian switches from Gauss–Newton to Gauss–Newton + κ‖m‖I to the full model by gradient and residual size, an adaptive Levenberg–Marquardt model [S025 pp. 5–6]; a safety step spends no evaluation when the step is short [S025 pp. 7–8]; the radius shrinks only when a failure cannot be blamed on geometry [S025 p. 9]. One model per residual also gives a local quadratic rate for zero-residual problems [S065 pp. 1–2, 26].

<a id="heuristic-3"></a>

## Heuristic 3: robust as bilevel

*Condensed in:* SKILL.md › Research Heuristics › H3 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H3 · If the problem has uncertain parameters or implementation errors, then formulate the robust counterpart as a bilevel DFO problem.**
  - Case: Conn & Vicente, OMS 27:561–577 (2012) [S066 pp. 1, 8–9, 16–19].

<a id="heuristic-4"></a>

## Heuristic 4: models inside direct search

*Condensed in:* SKILL.md › Research Heuristics › H4 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H4 · If a direct-search code is your robust baseline, then add a quadratic-model search step rather than replacing it.**
  - Case: Conn & Le Digabel, OMS 28:139–158 (2013), whose abstract reports that the models improve MADS's performance significantly (abstract level [S023]); NOMAD uses these models by default [S075 p. 19].

<a id="heuristic-5"></a>

## Heuristic 5: progressive barrier

*Condensed in:* SKILL.md › Research Heuristics › H5 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H5 · If constraints are simulation outputs, then keep both a best-feasible and a best-infeasible incumbent (progressive barrier), even inside a trust-region method.**
  - Case: Audet, Conn, Le Digabel, Peyrega, COAP 71:307–329 (2018), with the device retuned to the host's evaluations per iteration [S075 pp. 3, 9, 11, 13, 20].

<a id="heuristic-9"></a>

## Heuristic 9: answer small questions

*Condensed in:* SKILL.md › Research Heuristics › H9 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H9 · If an engineer asks you a small optimization question, then answer it. That is how problems find you.**
  - Case: a minimax question led to the circuit-tuning workshop (Conn's first-person account [S236 p. 3]).

<a id="heuristic-10"></a>

## Heuristic 10: unexplained results become conjectures

*Condensed in:* SKILL.md › Research Heuristics › H10 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H10 · If your own tests show a result you cannot explain, then publish it as an explicit conjecture with the reason it is hard, make its explanation the next paper, and print the theorem's predicted quantity next to the observed one.** (new, full texts)
  - Case: SR1's unexplained win in a trust region was written up as a conjecture [S011 p. 20] and proved three years later, with the computable bound printed beside the observed Hessian errors [S010 pp. 5, 12, 15–19]; one inner iteration per outer iteration, "often apparent" in the LANCELOT B prototype, turned into a theorem, with proved and observed kept apart [S074 p. 3]; a conjectured mechanism for the SR1 advantage failing under partial separability [S049 p. 19].

<a id="heuristic-11"></a>

## Heuristic 11: extending a convergence theory

*Condensed in:* SKILL.md › Research Heuristics › H11 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H11 · If you extend a published convergence theory (yours or a framework's), then list which lemma uses which assumption, re-prove only those, map every other result by number to its predecessor, and check that each new rule reduces to the old one in the one-component case.** (new)
  - Case: the barrier development kept deliberately close to the 1991 augmented-Lagrangian paper [S007 p. 8]; results mapped by number to the 1991 paper, with the one new difficulty marked [S022 pp. 13–15, 20–22]; noisy f handled by patching the one inequality that uses exact values [S031 pp. 36, 57–58]; each per-element rule stated with its one-element reduction [S047 pp. 10, 14]; plug-in on the CSV 2009 framework [S025 p. 12; S066 p. 3].

<a id="heuristic-12"></a>

## Heuristic 12: use every evaluation twice

*Condensed in:* SKILL.md › Research Heuristics › H12 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H12 · If each evaluation is expensive, then use every evaluated point twice: in the model and its geometry, to validate a long step before paying for a new evaluation, and as a candidate iterate even when it was sampled for geometry. Reject trial points by cheap tests before evaluating them, and keep cheap constraints inside the subproblem so no evaluation is spent on an infeasible point.** (new)
  - Case: "At variance with Powell's proposal, we will however insist on the ability of our algorithm to take long steps and also to progress as early as possible with every available function evaluation." [S019 p. 4], with models from fewer than a full set of points and a ratio test on stored values [S019 pp. 6–10]; any computed value is to "be exploited if at all possible" and geometry points may become iterates [S013 pp. 15, 17; S009 p. 10]; analytic constraints kept in the subproblem [S020 p. 6]; evaluations reused across nested solves [S066 pp. 9, 14]; an interiority test before evaluating an undefined barrier [S026 pp. 8–9].

<a id="heuristic-13"></a>

## Heuristic 13: failed evaluations

*Condensed in:* SKILL.md › Research Heuristics › H13 (rule condensed to one line, at most three cards).

*Before tightening (verbatim):*

- **H13 · If the simulator can fail at a trial point, then give it a failure return code, let the optimizer skip the iteration and cut the trust region, count failed evaluations in the budget, report the failure rate, and draw the case where the heuristic stops wrongly.** (new)
  - Case: pass/fail ("virtual") constraints handled by a temporary radius cut and re-solve, with 15–20% failed evaluations counted in the totals and the heuristic's failure case drawn [S020 pp. 7–8, 10]; "In our opinion, failure recovery is a necessary ingredient of efficient circuit tuning." [S027 p. 5]; recovery from nonworking circuits in JiffyTune (abstract level [S033]).

<a id="signature-work-1"></a>

## Signature work: Recent progress in unconstrained nonlinear optimization without derivatives

*Condensed in:* SKILL.md › Signature Work Anatomy (rows condensed to about two lines). Original heading: Recent progress in unconstrained nonlinear optimization without derivatives (Mathematical Programming 1997, DOI 10.1007/BF02614326)

*Before tightening (verbatim):*

Read in full [S009], with its predecessor Conn–Toint 1996 [S019] and the Powell-festschrift convergence paper [S013].

| Dimension | Content |
|---|---|
| Origin | Stated (the first pass had speculation): "the applications presented to the authors", in which f is very expensive and derivatives are missing because f is a measurement or the output of a large simulation whose source code is effectively unavailable [S009 p. 3]; the 1996 algorithm paper names geophysical layer depth and helicopter-rotor vibration [S019 pp. 2–3]. |
| Why then | Powell's 1994 interpolation proposal preceded Conn–Toint by a year [S019 p. 4]; the Sauer–Xu (1995) interpolation error bound was available for the companion festschrift paper [S013 pp. 2, 9]; Conn had a decade of trust-region convergence theory behind him. The survey also rehabilitates Winfield's overlooked method [S009 pp. 5–6]. |
| Key insight | Put the interpolation model in a trust-region framework and maintain its geometric quality explicitly, so trust-region convergence arguments carry over. Concretely: shrink the radius only if the geometry was adequate when the step was computed, otherwise repair and keep the radius [S009 pp. 9–10]; measure geometry with quantities the model construction already produces (Newton-polynomial pivots) [S009 pp. 14–15]. |
| Minimal evidence | Conn–Toint 1996: 20 small CUTE problems (n = 2–4), noiseless and at two noise levels, against a finite-difference trust-region code built from LANCELOT routines, counted in function evaluations [S019 pp. 15–18]. The survey itself has no numbers [S009 p. 12]. |
| Abandoned paths | Filled in by the full texts (the first pass had "unknown"): the CST full-replacement geometry step, later called "very expensive" and replaced by one-point repairs [S016 p. 19]; the CST O(Δ) gradient bound, later called "clearly inferior" [S124 pp. 26–27]; CST 1997 later placed among provably convergent but impractical methods [S012 p. 2]. |
| Reception | A standard DFO reference, leading to CSV 2008–2009 and the 2009 book (2015 Lagrange Prize). Its closing open problems became the next decade's papers [S009 p. 17 → S016; S028; S025; S020]. |
| Methods shown | M1, M3, M6, M5 (derivative triage [S009 pp. 3–4]), M7 |

<a id="signature-work-2"></a>

## Signature work: Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points

*Condensed in:* SKILL.md › Signature Work Anatomy (rows condensed to about two lines). Original heading: Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points (SIAM J. Optim. 2009, DOI 10.1137/060673424)

*Before tightening (verbatim):*

Read in full [S012].

| Dimension | Content |
|---|---|
| Origin | Stated (the first pass had speculation): the paper sorts the literature into practical trust-region DFO codes without convergence theory (Marazzi–Nocedal, Powell 2003) and provably convergent methods that were impractical, among them the authors' own *Trust-Region Methods* and CST 1997. It aims at the first kind with the guarantees of the second [S012 p. 2]. |
| Why then | The geometry toolkit (Λ-poisedness [S124]; interpolation sets [S016]; regression and underdetermined models [S028]) was in place, so the theorem could be stated once for a general algorithm [S012 pp. 2, 29]. |
| Key insight | Convergence needs only a fraction of Cauchy (and eigenstep) decrease plus models from a *fully linear* (or fully quadratic) class, which the paper itself defines by Taylor-like error bounds *and* the existence of a model-improvement algorithm that certifies in a finite, uniformly bounded number of steps [S012 Defs 3.1, 3.3, pp. 7–9]. Any model builder that certifies this inherits the result. The algorithm is relaxed toward practice: acceptance on simple decrease, one trust region for both step and sampling, and uncertified models allowed to move the iterate [S012 pp. 2–3, 13–14]. (The first pass attributed "fully linear / fully quadratic" to later literature; corrected.) |
| Minimal evidence | The proofs: first- and second-order lim-type results [S012 pp. 15–28]. No numbers; practicality is argued in prose (one-point replacements, bad pivots rarely replaced in practice, O(n⁶) vs O(n⁴) linear algebra) [S012 pp. 11–13]. |
| Abandoned paths | Powell's two trust regions, rejected as more complicated [S012 p. 2]; the authors' own book's claim that second-order DFO analysis follows simply from the derivative-based case, answered in this paper: the adaptation is not as trivial as one might expect [S012 p. 3]. |
| Reception | Widely cited foundation; refined by Scheinberg & Toint 2010 and challenged in practice by Fasano–Morales–Nocedal 2009 (Tension 1); reused as a plug-in by Conn's own later papers [S025 p. 12; S066 p. 3; S075 p. 25]. |
| Methods shown | M3, M1 (theory aimed at the code), M6, M7 |

<a id="signature-work-3"></a>

## Signature work: LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization

*Condensed in:* SKILL.md › Signature Work Anatomy (rows condensed to about two lines). Original heading: LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization (Release A) (Springer Series in Computational Mathematics 17, 1992, DOI 10.1007/978-3-662-12211-2), with its origin in the 1988 CGT theory/testing twin (SIAM J. Numer. Anal. 1988, DOI 10.1137/0725029; Math. Comp. 1988, DOI 10.1090/s0025-5718-1988-0929544-3)

*Before tightening (verbatim):*

The book itself is abstract-level [S006]; this anatomy rests on the 1988 twin [S008; S011], the 1989 design statement [S046], the 1994 survey [S061] and the 1996 numerical-experiments paper [S040], all read in full.

| Dimension | Content |
|---|---|
| Origin | Stated (the first pass had speculation). The first CGT paper gave bound constraints, frequent in practice, a class-level trust-region theory [S008 pp. 1–2]; its testing twin set out to "demonstrate the viability" of those methods [S011 p. 3] and closed with the programme that became the package: an augmented Lagrangian with bound-constrained subproblems [S011 p. 24], analysed in CGT 1991 [S005]. Design requirements stated in 1989: implementations and analysed algorithms "should differ as little as possible", intensive testing on practical and academic problems, and structure exploitation [S046 pp. 3, 11–12]. |
| Why then | Gould and Conn had worked together since 1984 [S096]; large problems needed projected search, truncated conjugate gradients and partially separable updating [S008 p. 27]; an input format (SIF, a superset of MPS; later the format of CUTE) let users pose them [S149 pp. 4, 6; S004 pp. 4–5]. |
| Key insight | Any step with a fixed fraction of the generalized Cauchy decrease is admissible, which gives global convergence for a whole class [S008 pp. 3–4, 22, 27]. Such a class matters when users can pose problems to it and it has been stress-tested on a large common collection; group partial separability is exploited throughout [S040 p. 6]. |
| Minimal evidence | The 1988 twin: ten tables with bounds added around the unconstrained solutions and "degenerate" variants, cost in function and gradient calls, received six months after the theory paper and published in the same month [S011 pp. 11–25; S008 p. 1; S011 p. 2]. Then "Numerical experiments with the LANCELOT package" (*Math. Programming* 73:73–110, 1996): 21 one-change variants × 943 CUTE instances; the default succeeds on 873 of 943 [S040 pp. 27–35]; complete data in a separate report [S103]. |
| Abandoned paths | BFGS, "surprisingly disappointing" relative to SR1 inside a trust region [S011 p. 20]; the ℓ₂ trust region, diagonal rescaling and DFP "could probably be removed from future releases" [S040 p. 50]; LANCELOT A's major defect is its handling of linear constraints [S061 p. 21]. |
| Reception | 1994 Beale–Orchard-Hays Prize. The SR1 anomaly, left as an explicit conjecture, became a theorem three years later [S011 p. 20 → S010 p. 5] (H10). The printed weak points became the next papers [S040 p. 49 → S089; S007]; a 117-hour default run started the barrier line [S061 p. 15]. The generalized Cauchy point recurs in Conn's DFO theory [S012 pp. 5–6]. Later replaced by IPOPT inside IBM's circuit tuner [S236 pp. 4–5]. |
| Methods shown | M1, M2, M3 (a certificate as the theorem's interface), M5, M7, H10 |

<a id="signature-work-4"></a>

## Signature work: JiffyTune: circuit optimization using time-domain sensitivities

*Condensed in:* SKILL.md › Signature Work Anatomy (rows condensed to about two lines). Original heading: JiffyTune: circuit optimization using time-domain sensitivities (IEEE TCAD 1998, IEEE Xplore 736569)

*Before tightening (verbatim):*

The TCAD paper is abstract-level [S033]. This anatomy rests on JiffyTune's first published account, "Optimization of custom MOS circuits by transistor sizing" (ICCAD 1996, DOI 10.1109/iccad.1996.569578), read in full [S036], and on Conn's essay [S236].

| Dimension | Content |
|---|---|
| Origin | Conn's first-person account [S236 p. 3]: an electrical-engineering colleague's minimax question; later he was suggested as a relatively approachable mathematician and invited to an IBM-wide circuit-tuning meeting, where he remarked that the users ran 1960s algorithms in the 1990s and was asked to present 1990s ones. (The first pass had the same story as a MAM 2015 paraphrase.) |
| Why then | The in-house simulator SPECS was on average 70× faster than the SPICE-like AS/X and computed time-domain sensitivities by the direct and the adjoint method [S036 pp. 2–3; S236 p. 3]; LANCELOT existed as the engine [S036 p. 7]. |
| Key insight | Do not treat the circuit as a black box. "Our ability to compute gradients efficiently is crucial to the success of this approach" [S036 p. 1]. Pose minimax, power, and transistor-and-wire tuning as NLP (minimax through an epigraph variable), retune the solver to noise and physical units, and put it inside the designers' own schematic systems [S036 pp. 1, 5]. |
| Minimal evidence | Filled in (the first pass had "unknown"): a gradient benchmark on a 144-transistor circuit; a priority-decoder case study re-measured by the reference simulator; adoption by 41 designers on 168 unique circuits, about 1,200 sessions and over 2,200 runs [S036 pp. 3, 6]. |
| Abandoned paths | Not stated for the design. The 1996 paper treats static-timing and dynamic tuning as complementary stages [S036 p. 1]; the next tool, EinsTuner, took the static-timing route with gradients [S027 pp. 1–2]. Recovery from non-working circuits was still open in 1996 [S036 p. 7]. The engine was later swapped, LANCELOT → IPOPT [S236 pp. 4–5]. |
| Reception | Led to EinsTuner (DAC 1999; FGCS 2005) and an IBM Outstanding Technical Achievement Award. The essay's circuit-tuning tool (unnamed there; identified with this line via FGCS 2005) is deployed as a standard tool within IBM for all custom circuits [S236 p. 4]. Before that came an eighteen-month fight for the project's survival, won with his immediate management's support and through the engineers [S236 pp. 3–4]. |
| Methods shown | M4, M5, M1 (industrial triad) |

<a id="signature-work-5"></a>

## Signature work: CUTE: constrained and unconstrained testing environment

*Condensed in:* SKILL.md › Signature Work Anatomy (rows condensed to about two lines). Original heading: CUTE: constrained and unconstrained testing environment (ACM TOMS 1995, DOI 10.1145/200979.201043) (new)

*Before tightening (verbatim):*

Read in full [S004].

| Dimension | Content |
|---|---|
| Origin | The developers' own testing burden: a package author must obtain, specify and manage a large problem collection and compare approaches; "All of these situations occurred during our own researches" [S004 p. 3]. A spin-off of the LANCELOT project [S004 p. 3]. |
| Why then | SIF already existed as LANCELOT's input format and extends MPS, so linear-programming sets were reachable too [S004 pp. 2–5; S149]. Format differences between solvers blocked valid comparisons [S137 p. 2]. |
| Key insight | Decouple problems from solvers: one input format, a decoder, evaluation tools in each solver's preferred form, class strings for reproducible subset selection, and thin interfaces to rival codes (COBYLA, NPSOL, VF13) [S004 pp. 8–25]. Growth through users: the LANCELOT licence requires most users to submit typical problems [S004 p. 4]. |
| Minimal evidence | 738 problems on 15 December 1994, absorbing the existing collections by name [S004 p. 4]. No solver results in the paper; they were deferred to the LANCELOT reports [S004 p. 5]. "The only way to really judge the effectiveness of the environment is for the reader to use it." [S004 p. 25]. |
| Abandoned paths | Not stated (no first-hand source). |
| Reception | Ancestor of CUTEr and CUTEst (not discussed in the paper); CUTEst problems form tier 1 of Conn's 2018 study [S075 p. 17]; the CUTE interfaces were used to plug MINOS into JiffyTune [S036 p. 2]. |
| Methods shown | M2, M4 (licence route), M7 |

<a id="anti-patterns"></a>

## Research anti-patterns

*Condensed in:* SKILL.md › Research Anti-patterns (source column condensed to card references).

*Before tightening (verbatim):*

| Anti-pattern | Why Conn's record argues against it (source) | Do instead |
|---|---|---|
| Going black-box by default | Flagship industrial work was gradient-based via sensitivities (JiffyTune 1998; DAC 1999) [S036 pp. 1–3; S027 p. 4] | Workflow A derivative audit (M5) |
| Theorem about an idealised algorithm, code that does something else | Framework theory paired with enforcing codes (CGT 1988/1991; CST 1997 → DFO code); abstract tests built to contain packages' native tests [S022 pp. 26–29; S107 p. 25] | M1 steps 2–3 |
| Benchmarking on your own favourite problems | CUTE (1995); two-tier tests in 2018 [S075 pp. 17–23]; small test sets "more likely to introduce unwanted bias" [S102 p. 7] | M2 two-tier public test bed |
| Counting iterations instead of evaluations | Budget and noise designed in from 1996; evaluations are the user's cost [S011 p. 22; S020 p. 10] | M2 step 1; data profiles |
| Ignoring noise until deployment | Conn–Toint 1996 tested with and without noise [S019 pp. 17–18] | Noisy variants in Tier 1 |
| Defending your own solver or school | LANCELOT → IPOPT swap [S236 pp. 4–5]; MADS hybrids (2013, 2018); own methods named as superseded [S016 p. 19; S108 pp. 17, 21] | M6; M7 step 5 |
| Overclaiming | The 2018 paper calibrates by tier: "competitive" with the same-school baseline, "preferable" to the other school's on each tier [S075 pp. 1, 22–23]; "complement each other" [S102 p. 17] | Workflow C claim wording |
| Publishing a practical algorithm with no evidence it competes (new) | [S061 p. 27]; surprise at how few papers report numbers [S080 p. 16] | M1; Workflow F |
| Leaving an unexplained win as a footnote (new) | SR1 conjecture → theorem [S011 p. 20 → S010 p. 5]; observation → theorem [S074 p. 3] | H10 |
| Wasting evaluations: discarding points sampled for geometry, or evaluating points that violate cheap constraints (new) | [S019 p. 4; S013 pp. 15, 17; S020 p. 6] | H12 |
| Treating simulator crashes as fatal, or leaving failed runs out of the counts (new) | [S020 pp. 7–8, 10; S027 p. 5] | H13 |
| Tolerances and initial radius in machine units (new) | Tuning in physical units; a radius far below the smallest meaningful move "may be disastrous" [S036 p. 5; S019 p. 12] | Workflow D step 5 |
| Arranging the comparison in your own favour (new) | Rival's author as coauthor [S102 p. 2]; own expertise bias declared [S061 p. 25]; personal intervention kept minimal [S188 p. 3] | M2 step 5 |

<a id="trajectory"></a>

## Research trajectory

*Condensed in:* SKILL.md › Research Trajectory (table kept verbatim; prose and Latest condensed).

*Before tightening (verbatim):*

| Period | Main direction | Trigger for the shift | Representative work |
|---|---|---|---|
| 1971–1985 (Waterloo) | Penalty and nondifferentiable methods for NLP; direct minimax and ℓ₁ fitting (with Bartels); students on penalty, location and minimax problems | PhD topic (advisor T. Pietrzykowski [S141 p. 3]); supervising students; the numerical-linear-algebra emphasis is credited to Bartels [S233 p. 9] | Conn 1973 *SINUM* (DOI 10.1137/0710063); Conn 1978 minimax [S233]; Coleman & Conn 1982 [S018; S030]; Coleman & Conn 1984 [S021] |
| 1985–1996 (Waterloo → IBM) | Trust regions, augmented Lagrangian, large-scale software and testing | CGT collaboration: Gould from 1984 [S096], Toint from 1988 [S008]; the 1988 testing paper's closing programme is the LANCELOT plan [S011 p. 24] | CGT 1988, 1991; LANCELOT 1992; CUTE 1995 |
| 1990–2000 (IBM) | LANCELOT as a research engine: audit-driven follow-ups (M7); a DARPA grant within a year of joining IBM [S236 p. 2] | The move to IBM does not change this line; the package's printed weak points do [S040 p. 49; S061 p. 15] | S089, S007, S022, S054 → S026, S058, S074; LANCELOT–MINOS comparison [S102] |
| 1990–2005 (IBM) | Industrial circuit tuning | Move to IBM in 1990 (recruited by Ellis Johnson [S236 p. 2]); an engineer's minimax question [S236 p. 3] | JiffyTune 1996/1998 [S036]; DAC 1999 [S027]; FGCS 2005 |
| 1996–2010 | Model-based DFO theory, code, book | Stated: applications "presented to the authors" with expensive simulations and no derivatives [S009 p. 3; S013 p. 2]; named applications [S019 pp. 2–3] | CST 1997; CSV 2008 ×2, 2009; IDFO 2009; ZCS 2010 |
| Mid-2000s–2008 (new; start year not dated in the sources) | IBM–CMU MINLP project (BONMIN), initiated and chosen by Conn; he calls his own contribution minimal | Management call for IBM–CMU projects; discrete variables coming into circuit tuning [S236 pp. 4–5] | Bonami et al. 2008 (role not identifiable) [S003] |
| 2006–2015 (new) | Petroleum (seismic matching, history matching) as IBM first-of-a-kind projects; maintenance scheduling as simulation-based DFO; NTNU operations; electricity-grid white paper | Circuit tuning had become routine; he yearned to make a splash in a new area [S236 p. 5] | Mostly abstracts [S098; S100; S076; S142; S101; S105]; [S060; S136] (roles not identifiable) |
| 2006–2018 | Energy and other applications; robust/bilevel DFO; hybrids with MADS | NTNU/Statoil board seat (2006); Montréal collaboration | Conn & Vicente 2012; Conn & Le Digabel 2013; Audet et al. 2018; Amaioua et al. 2018 |
| 2015–2023 (new) | Air-traffic conflict resolution with ENAC, continued after his death by his coauthors | Toulouse collaboration (Mongeau, from 1992 [S155]) | Peyronne et al. 2015 [S063 abstract]; Cafieri–Conn–Mongeau 2023 [S099; S141] |

During the IBM years the essay also reports three years of teaching a course at Yale (undated in the essay) [S236 p. 2].

**Why the trajectory has this shape** (full texts): M7 explains much of the 1992–2000 output, a large part of which repairs or extends LANCELOT [S040 p. 49; S061 pp. 15–22] (proportions in 08 §8.1). Constants across all periods: the trust region as the default globalisation device, from bounds (1988) [S008] to DFO [S012] and the progressive barrier [S075]; penalty functions from the thesis to the posthumous papers, one of which answers a question he asked in 1981 [S141 pp. 4, 13]; engineering users, from microwave networks in 1975 [S233 pp. 9–10] to IBM circuits [S036; S027]. Of the stated agendas, most were delivered in later papers (08 §8.4); the exceptions are the numerical study announced in 1984 (warning sign 2), a uniform-bound proof for Powell-like rules [S016 p. 24], and measuring how often geometry improvement is needed [S075 p. 23].

### Latest
- Conn died on 14 March 2019. ✗ Corrected: the first pass said there was no activity after the two 2018 works. Those were his last papers during his lifetime (*COAP* 71:307–329; *EJOR* 268:13–24); co-authored papers kept appearing in 2020–2023 [S032, middle author; S135 abstract; S099 p. 2; S141 p. 2], two of them dedicated "In memory of our dearest friend Andy Conn". They are his coauthors' framing, so this is still a **historical lens** (research date 2026-09-27).

<a id="lineage"></a>

## Academic lineage

*Condensed in:* SKILL.md › Academic Lineage (condensed).

*Before tightening (verbatim):*

- **Formation**: B.Sc. Imperial College London (1967) → M.Sc. computer science, Manitoba (1968) → Ph.D., Waterloo Applied Analysis and Computer Science (1971), thesis "A gradient type method of locating constrained minima"; advisor T. Pietrzykowski (per his coauthors' posthumous paper [S141 pp. 3, 13]; secondary, not Conn's own words; the title also appears in the Scholar record [S134 metadata]) → postdoc, Hebrew University of Jerusalem. His essay adds that he was at Waterloo from 1968 as a doctoral student, had two sabbaticals in France, and was recruited to IBM by Ellis Johnson at Oberwolfach, accepting within a year [S236 pp. 1–2].
- **Students** (10 PhD students at Waterloo per the SIAM obituary): Thomas F. Coleman (1979, penalty methods) [S018; S030; S021], Paul H. Calamai (1983, location problems) [S041; S062 abstract], Yuying Li (1988, nonlinear minimax) [S130; S164; S108]. All three became Waterloo professors.
- **Collaborators**: Nicholas Gould and Philippe Toint (CGT trio, more than 20 joint papers; in the cards Toint appears on 44 and Gould on 40, 1984–2003); Katya Scheinberg (IBM, 1997–2009; 12 cards) and Luís Nunes Vicente (DFO trio; 7 cards); Richard Bartels at Waterloo (8 cards); Hongchao Zhang; IBM engineers Chandu Visweswariah (11 cards), Ruud Haring and Andreas Wächter; Marcel Mongeau (1992–2023); Charles Audet and Sébastien Le Digabel (MADS school) [08 §9]. The rival school as coauthor: MINOS's author on the LANCELOT–MINOS comparison [S102 p. 2].
- **Influence**: the "fully linear / fully quadratic" language of model-based DFO analyses. ✗ Corrected: the first pass traced it to the CSV monograph through secondary descriptions. The terms are defined in CSV 2009 itself [S012 Defs 3.1, 3.3, pp. 7–9], and "fully linear" already appears in the 1998 practical paper [S020 pp. 4–5]. The CUTE lineage continues in CUTEr and CUTEst (author lists not verified here).

<a id="tensions"></a>

## Inner tensions

*Condensed in:* SKILL.md › Inner Tensions (condensed).

*Before tightening (verbatim):*

- **Tension 1 — theory vs practice (geometry).** Conn's DFO theory makes geometry maintenance the condition that carries the convergence theorem (CSV 2008–2009). Yet a geometry-free code performed well on smooth problems (Fasano–Morales–Nocedal 2009), and Scheinberg & Toint (2010), from inside Conn's own circle, confined geometry steps to criticality checks. On one side is the rigour the theorem needs; on the other, the evaluations it costs. The tension is already inside his own papers: the new geometry algorithms may not outperform Powell's rule [S016 p. 23]; bad-pivot replacements are rarely needed in practice [S012 p. 12]; the implemented bilevel method runs without explicit model-improvement iterations [S066 pp. 6–10]; the 2018 algorithm enforces certification that its theorems do not use [S075 pp. 8, 12, 15–16].
- **Tension 2 — author vs pragmatist.** Conn co-created LANCELOT, yet IBM's circuit tool swapped it for IPOPT; in his own words, "age is often a negative attribute" [S236 p. 5]. The flagship industrial project was gradient-based even while Conn was founding modern model-based DFO. The record suggests his loyalty went to the user's problem, not to the method.
- **Tension 3 — rival-school rhetoric vs tier-specific calibrated wins.** An IBM page presents a Conn-team model beating NOMAD by orders of magnitude in simulations (promotional, set-up unknown). The peer-reviewed 2018 paper with the NOMAD authors calibrates by tier: the abstract says "competitive"; the conclusion says competitive with the same-school baseline and "preferable" to the other-school baseline on each tier [S075 pp. 1, 22–23]. Promotional rivalry sits alongside collaboration and measured claims.
- **Tension 4 — generality vs structure.** Class-level theory for general black-box algorithms (CSV 2009) sits alongside a strong habit of exploiting structure: least squares (2010), bilevel (2012), and sensitivities in circuits. The two meet in plug-in proofs: the structured papers reuse the general framework and prove only the structure-specific lemma [S025 p. 12; S066 p. 3].
- **Tension 5 — package repair vs moving on** (new). The self-audit loop (M7) kept the CGT group repairing and extending LANCELOT for much of 1992–2000 [S089; S007; S022; S054; S058; S074]. In application work he moved to a new area once a tool was routine (circuit tuning → petroleum) [S236 p. 5].

<a id="mentor-voice"></a>

## Mentor voice (evidence note)

*Condensed in:* SKILL.md › Mentor Voice (note condensed; the five constructed questions are unchanged).

*Before tightening (verbatim):*

The evidence is thin but no longer empty. No recordings, interviews or student memoirs were found. There is one first-person essay (2007) with a candid, self-deprecating voice: highlights and lowlights side by side, concrete figures, and short aphorisms [S236 pp. 2–6]. Colleagues' descriptions (SIAM obituary: "known to everyone as Andy") point the same way. A few verified sentences from the essay can be quoted: the "1960s algorithms in the 1990s" remark [S236 p. 3], the "algorithms twice as good" line at the top of this file [S236 p. 4], and "age is often a negative attribute" [S236 p. 5]. The questions below are **constructed from his methods**. They are not recorded phrases:

<a id="agentic-protocol"></a>

## Agentic Protocol, Step 2 (derivative and structure audits) and routing row

*Condensed in:* SKILL.md › Agentic Protocol › Step 2 (first two bullets condensed) and Research Task Routing (multi-year agenda row reworded).

*Before tightening (verbatim):*

- **Derivative audit.** Can gradients be had at all: simulator sensitivities (as in JiffyTune), adjoints, automatic differentiation, affordable finite differences? Which parts of the function are analytic? Write one sentence per route with the reason it works or fails, as his DFO papers open [S009 pp. 3–4; S019 p. 3].
- **Structure audit.** Is the objective a sum of squares? Max-type, bilevel or robust? Are there bounds, analytic constraints, or constraints that are simulation outputs? Is anything separable?

| "Multi-year research agenda" | Workflow G + Research Trajectory. The mechanism is documented (M7); how he chose new application areas rests on one essay's stated criteria [S236 pp. 4, 6] | M7, M6, M4 |

<a id="corrections"></a>

## Corrections from the full texts

*Condensed in:* SKILL.md › Corrections from the full texts (one line each), and the ✗ bullets inside the methods, taste lists, Academic Lineage and Latest.

The first pass used web-search snippets only. Every line of SKILL.md (before tightening) that records a first-pass error, gap or speculation corrected by the full-text reading, verbatim, with the section it stood in:

- **Warning signs of bad research** (line 120 before tightening):

  ✗ Corrected: the first pass said no explicit critique by Conn was found. Co-authored critiques exist: the evidence rule quoted in Integrity rule 4 [S061 p. 27] and the authors' surprise at how few papers report numerical results at all [S080 p. 16]. Signs 1–3 now have stated sources; signs 4–7 remain inferred from practice.

- **Warning signs of bad research** (line 122 before tightening):

  2. A theorem whose algorithm never gets code or numbers anywhere in its line of work. ✗ Corrected: the first pass said a theorem with no code and no numbers never occurs in the record. Theory-only papers are common: the 1984 quasi-Newton paper declares its practical performance unknown and left to future work [S021 p. 26], and [S013 p. 22; S012 pp. 11–13; S124 pp. 27–32; S130 p. 32] carry no numbers; the 1997 barrier paper has no detailed numerical evidence, only an anecdotal report that a rudimentary implementation solved over ninety percent of about a thousand problems [S007 p. 27]. In most lines the other legs follow in companions (S005 → S040; S019, code first → S013 → S020; S012 → S025, S075); the cards show no numerical follow-up for the 1984 method.

- **Method 1: The theory–code–test triad** (line 148 before tightening):

  - Say–do consistency: ✅ stated + practiced; 63 cards (58 weighted papers). ✗ Corrected: the first pass found no first-person essay; it exists [S236 pp. 1–7], so the stated side no longer rests on obituaries.

- **Method 2: Build the test bed as research infrastructure** (line 165 before tightening):

  - Say–do consistency: ✅ stated + practiced; 41 cards (36 weighted papers). ✗ Corrected: in the 2018 study both baselines (COBYLA, NOMAD) ran on both tiers, not one each [S075 pp. 17–23].

- **Method 3: Certify the model — make "geometry" a condition that carries the theorem** (line 184 before tightening):

  - Variants: ⚠ **Before DFO**, certified interfaces already carried the theorems (a Cauchy-decrease fraction, inner-solve tests, a gradient error ≤ κΔ) [S008 p. 7; S022 pp. 26–28; S031 pp. 6–7]. ⚠ **Step 5 unmeasured**: only a qualitative remark that bad-pivot replacements are rarely necessary [S012 p. 12], and the measurement listed as future work in 2018 [S075 p. 23]. ⚠ **Own devices superseded**: the CST 1997 step "very expensive" [S016 p. 19], its gradient bound "clearly inferior" [S124 pp. 26–27] (M7). "Fully linear" is the papers' own term, not later literature's [S020 pp. 4–5; S012 Defs 3.1, 3.3].

- **Method 4: Enter through the user's door** (line 202 before tightening):

  - Stated (first person, 2007 essay): "I said it was very interesting but it was too bad that they were using 1960s algorithms in the 1990s and so I was asked to tell them about 1990 algorithms." [S236 p. 3]; software in the users' own environment outranks a factor-two gain (top quote) [S236 p. 4]. Co-authored: "The designers’ focus shifts from solving the optimization problem to specifying it correctly and completely." [S036 p. 1]. (The first pass had these as MAM 2015 paraphrases.)

- **Method 4: Enter through the user's door** (line 203 before tightening):

  - Practice: JiffyTune → EinsTuner (TCAD 1998; DAC 1999; FGCS 2005), with adoption reported as 41 designers on 168 circuits [S036 pp. 1, 5–6; S027 pp. 1, 8]; Boeing problems at an AIAA MDO symposium [S020 pp. 1–3]; air-traffic models with ENAC [S099; S141]. ✗ No weight: S060, S057 and S136, which the first pass listed.

- **Recent progress in unconstrained nonlinear optimization without derivatives (Mathematical Programming 1997, DOI 10.1007/BF02614326)** (line 395 before tightening):

  | Origin | Stated (the first pass had speculation): "the applications presented to the authors", in which f is very expensive and derivatives are missing because f is a measurement or the output of a large simulation whose source code is effectively unavailable [S009 p. 3]; the 1996 algorithm paper names geophysical layer depth and helicopter-rotor vibration [S019 pp. 2–3]. |

- **Recent progress in unconstrained nonlinear optimization without derivatives (Mathematical Programming 1997, DOI 10.1007/BF02614326)** (line 399 before tightening):

  | Abandoned paths | Filled in by the full texts (the first pass had "unknown"): the CST full-replacement geometry step, later called "very expensive" and replaced by one-point repairs [S016 p. 19]; the CST O(Δ) gradient bound, later called "clearly inferior" [S124 pp. 26–27]; CST 1997 later placed among provably convergent but impractical methods [S012 p. 2]. |

- **Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points (SIAM J. Optim. 2009, DOI 10.1137/060673424)** (line 408 before tightening):

  | Origin | Stated (the first pass had speculation): the paper sorts the literature into practical trust-region DFO codes without convergence theory (Marazzi–Nocedal, Powell 2003) and provably convergent methods that were impractical, among them the authors' own *Trust-Region Methods* and CST 1997. It aims at the first kind with the guarantees of the second [S012 p. 2]. |

- **Global convergence of general derivative-free trust-region algorithms to first- and second-order critical points (SIAM J. Optim. 2009, DOI 10.1137/060673424)** (line 410 before tightening):

  | Key insight | Convergence needs only a fraction of Cauchy (and eigenstep) decrease plus models from a *fully linear* (or fully quadratic) class, which the paper itself defines by Taylor-like error bounds *and* the existence of a model-improvement algorithm that certifies in a finite, uniformly bounded number of steps [S012 Defs 3.1, 3.3, pp. 7–9]. Any model builder that certifies this inherits the result. The algorithm is relaxed toward practice: acceptance on simple decrease, one trust region for both step and sampling, and uncertified models allowed to move the iterate [S012 pp. 2–3, 13–14]. (The first pass attributed "fully linear / fully quadratic" to later literature; corrected.) |

- **LANCELOT: A Fortran Package for Large-Scale Nonlinear Optimization (Release A) (Springer Series in Computational Mathematics 17, 1992, DOI 10.1007/978-3-662-12211-2), with its origin in the 1988 CGT theory/testing twin (SIAM J. Numer. Anal. 1988, DOI 10.1137/0725029; Math. Comp. 1988, DOI 10.1090/s0025-5718-1988-0929544-3)** (line 421 before tightening):

  | Origin | Stated (the first pass had speculation). The first CGT paper gave bound constraints, frequent in practice, a class-level trust-region theory [S008 pp. 1–2]; its testing twin set out to "demonstrate the viability" of those methods [S011 p. 3] and closed with the programme that became the package: an augmented Lagrangian with bound-constrained subproblems [S011 p. 24], analysed in CGT 1991 [S005]. Design requirements stated in 1989: implementations and analysed algorithms "should differ as little as possible", intensive testing on practical and academic problems, and structure exploitation [S046 pp. 3, 11–12]. |

- **JiffyTune: circuit optimization using time-domain sensitivities (IEEE TCAD 1998, IEEE Xplore 736569)** (line 434 before tightening):

  | Origin | Conn's first-person account [S236 p. 3]: an electrical-engineering colleague's minimax question; later he was suggested as a relatively approachable mathematician and invited to an IBM-wide circuit-tuning meeting, where he remarked that the users ran 1960s algorithms in the 1990s and was asked to present 1990s ones. (The first pass had the same story as a MAM 2015 paraphrase.) |

- **JiffyTune: circuit optimization using time-domain sensitivities (IEEE TCAD 1998, IEEE Xplore 736569)** (line 437 before tightening):

  | Minimal evidence | Filled in (the first pass had "unknown"): a gradient benchmark on a 144-transistor circuit; a priority-decoder case study re-measured by the reference simulator; adoption by 41 designers on 168 unique circuits, about 1,200 sessions and over 2,200 runs [S036 pp. 3, 6]. |

- **Latest** (line 492 before tightening):

  - Conn died on 14 March 2019. ✗ Corrected: the first pass said there was no activity after the two 2018 works. Those were his last papers during his lifetime (*COAP* 71:307–329; *EJOR* 268:13–24); co-authored papers kept appearing in 2020–2023 [S032, middle author; S135 abstract; S099 p. 2; S141 p. 2], two of them dedicated "In memory of our dearest friend Andy Conn". They are his coauthors' framing, so this is still a **historical lens** (research date 2026-09-27).

- **Academic Lineage** (line 499 before tightening):

  - **Influence**: the "fully linear / fully quadratic" language of model-based DFO analyses. ✗ Corrected: the first pass traced it to the CSV monograph through secondary descriptions. The terms are defined in CSV 2009 itself [S012 Defs 3.1, 3.3, pp. 7–9], and "fully linear" already appears in the 1998 practical paper [S020 pp. 4–5]. The CUTE lineage continues in CUTEr and CUTEst (author lists not verified here).

- **Roundtable Card** (line 532 before tightening):

  - *Scheinberg lens*: deterministic certification within a finite, uniformly bounded number of iterations, with uncertified models still allowed to move the iterate (CSV 2009 [S012 p. 3]), versus probabilistic "often enough" guarantees. ✗ Corrected by the full texts: the first pass called Conn's side "always-maintained geometry".

- **Honest Boundary** (line 539 before tightening):

  - **Coverage of the full-text reading.** The full-text index has 183 rows: the 155 distinct works on the Google Scholar list (237 rows plus 2 DBLP-only items; `references/sources/publications/scholar.md`) and 28 rows that are not Conn works (11 unresolved title-page fragments; 17 referee or acknowledgement lists, progress-report sections, misattributed rows or an organisers' message). 45 rows are set aside: those 28, plus 13 patents, 2 talks, S153 (authorship doubtful) and S156 (a student's thesis). That leaves 138 in-scope works, each with a paper card: 71 full texts read (53 in full, 18 in part), 50 abstract-level, 16 metadata-only, 1 unreadable (S093, whose file is identical to S108 and is read there) (`references/research/07-paper-cards.md`). Full-text coverage is 51%; per-period counts are in `references/research/01-publications.md` §3. The first pass used web-search snippets only; the MAM 2015 profile, obituaries and IBM pages are still known only from snippets.
