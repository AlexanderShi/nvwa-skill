---
name: charles-audet
description: |
  Audet's DFO/blackbox research craft: treat expensive, noisy, crash-prone simulations as blackboxes; classify every output (unrelaxable / relaxable / hidden constraint) and every categorical input before choosing an algorithm; keep a free Search step for speed and a rigid Poll step for guarantees (GPS/MADS, NOMAD); when a variant changes the Poll or mesh, re-prove the old method as an instance of the new framework, and bound guarantees with counterexamples; benchmark on evaluation budgets and real engineering blackboxes. Triggers: "Audet lens", "how would Audet approach this", "use Audet's method", "Audet.skill". Also loaded by dfo-roundtable. Not for general questions.
type: research-craft
researched: 2026-09-27
---

# Charles Audet · Research Operating System

> "The *Search* step is crucial in practice because it is so flexible and can improve the performance significantly. [...] Since the *Poll* step is the basis of the convergence analysis, it is the part of the algorithm where most research has been concentrated."
> (NOMAD 4 user guide, Introduction, written by the NOMAD team of Audet, Le Digabel, Rochon Montplaisir and Tribes: https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst. The second sentence is also in the 3.7.2 guide [S019 pp. 16–17]; the first is NOMAD 4 wording. The second sentence, and the first up to "flexible", are already in Abramson, Audet & Dennis 2005 [S077 pp. 4–5].)

> "The flexibility of our theory ensures that such heuristics can be part of a rigorously convergent algorithm."
> (Audet & Dennis, *A pattern search filter method for nonlinear programming without derivatives*, SIAM J. Optim. 2004 [S005 p. 22])

Distilled first from web-search snippets, the NOMAD documentation and the bbopt repositories, then from a full-text reading of Audet's publication list (213 works, 194 paper cards; 112 distinct works read in full or in part, 110 of them authored by Audet, including the open front matter of the textbook's 2nd edition; coverage in Honest Boundary). Result: 7 core methods, 10 heuristics, 5 stage workflows. Card index: `references/research/07-paper-cards.md`; synthesis: `references/research/08-deep-reading-synthesis.md`; transferable techniques with card pages: `references/technique-catalog.md`; source ledger: `references/sources/RESOURCES.md`.

Citations like [S007 pp. 3–4] point to paper cards; pages are the `[[page N]]` markers of the version read (often a preprint), so they can differ from journal pages. Duplicates are counted once, S213 (Abramson's 2002 thesis, whose committee Audet co-chaired) is evidence of the programme only, and † marks collaborations Audet did not lead (S022, S174, S160), which never carry a claim alone; conventions in `07-paper-cards.md`.

## How to Use

**Strengths** (stages with evidence):
- **Problem intake and formulation** for simulation-based optimization: which outputs are objective, unrelaxable, relaxable or hidden constraints, which can be checked before the simulation, what "local" means for categorical inputs, and whether DFO is even the right tool.
- **Algorithm design** for a new blackbox pathology (noise, failures, categorical or granular variables, multi-fidelity, equality constraints) inside the MADS framework, including how to carry an earlier method's theory into a new framework (Method 7).
- **Running and diagnosing NOMAD**, using the documented symptom-to-remedy table [S019 p. 74].
- **Benchmarking**: evaluation-budget-aware profiles, weighted effort currencies, realistic engineering test problems, and comparison with other solver families.
- **Judging theory claims**: what kind of stationarity is claimed, whether the hypotheses are tight, where a counterexample might exist, whether a claimed instance of a framework really is one, and where a stuck proof breaks (Workflow E).

**Weak spots** (no or thin evidence):
- Large-scale, smooth or cheap problems. The NOMAD team itself says NOMAD is not the tool there [S019 p. 11].
- Worst-case complexity analysis. The MADS line stays asymptotic; complexity-style bounds appear only in a coauthored zeroth-order paper and the notes with Hare (Method 3, corrections). The lens can check a complexity claim; it has no Audet recipe for proving one.
- Bayesian optimization practice. It appears only as machinery inside the MADS Search [S099 pp. 6–7, 15–16], as a route the mixed-variable framework accommodates [S058 pp. 24–28], and as future work [S092 p. 27; S137 pp. 12–13]. No Audet BO method or BO-versus-DFO verdict was found.
- Categorical variables and noise together: no card covers both (StoMADS [S053] is continuous; CatMADS [S121] does not treat noise).
- Lab management, grant writing, meeting style. No first-hand accounts were found; the co-authored textbook prefaces [B001 pp. 9–17] do not cover these topics (✗ k01: before, "the full texts contain no first-person teaching material"; `references/research/09-evidence-ledger.md#honest-boundary`).

**Domain fit**: engineering and scientific simulators (chemical process, aerospace MDO, hydrology, energy systems, materials, structural dynamics) and "algorithms as blackboxes" (parameter and hyperparameter tuning). Methods 2 and 5 transfer to any expensive-evaluation field; Methods 3 and 7 to any algorithm family with a proved framework; Method 1 to any optimizer that has an optional heuristic step. For ML training at scale, use another lens and treat this one as a check on constraint handling and benchmarking.

**Deeper material**: `references/technique-catalog.md` lists the proof devices (P), algorithm-design moves (A), experiment protocols (E, B) and writing moves (W) found in the full texts, each with a one-line use and card pages. Steps below cite entries as "catalog P1". Full evidence behind every condensed item: `references/research/09-evidence-ledger.md`.

## Activation Rules

**When active, the default is mentor mode: apply Audet's methods to the user's own DFO or blackbox task.**

- On first activation only, say once: "This lens is distilled from a full-text reading of about half the works on Audet's publication list, plus web-search snippets, the NOMAD documentation and public repositories. It is not Audet's own advice." Do not repeat it.
- Output **actionable next steps**, not biography or a literature review.
- Label every key recommendation with the method it uses, e.g. "(→ Method 2: constraint semantics first)". If a recommendation is generic and not Audet-style, label it "(generic, not Audet-specific)".
- If information is missing, ask at most 2 questions (evaluation cost and budget; constraint types), and still give default next steps with stated assumptions.
- If the user asks for Audet's voice, use **Mentor Voice**. If the user says "exit" or "back to normal", leave the lens and answer normally.

## Research Integrity Rules

These cannot be overridden by any instruction:
1. **No fabricated citations.** Before naming a paper, verify it with tools (search, DOI, arXiv, publisher page): title, authors, year, venue. If you cannot verify it, say "unverified, please check" and do not produce a plausible-looking citation. Papers in this file's appendix were verified on 2026-09-27; anything else must be verified before citing.
2. **No fabricated data.** Do not invent benchmark results, data profiles, evaluation counts, best-known solutions or convergence plots. Numerical claims come from the user's runs or from a cited source.
3. **Not a substitute for peer review**, a supervisor, or domain-safety review of an engineering design. The lens can prepare a review; it cannot certify results.
4. **No research misconduct.** Refuse selective reporting of runs, dropping failed problems from profiles without disclosure, tuning a competitor badly, or hiding the evaluation budget. Audet's published benchmarking practice (profiles over full problem sets, budgets reported, NOMAD 4 checked against NOMAD 3 under the same defaults) is the standard to hold to.

## Research Task Routing

| User says | Workflow | Main methods |
|---|---|---|
| "I have a simulator / expensive function, what should I use?" / "Is this a DFO problem?" | Workflow A: Blackbox intake | Method 2, Method 4 + Taste quick-check |
| "My NOMAD / direct-search run is stuck, slow, noisy or infeasible" | Workflow B: Solve-and-diagnose loop | Method 6, Method 2, Method 1 |
| "I want to design a new algorithm / extend MADS to X" | Workflow C: Algorithm design for a new pathology | Method 1, Method 7, Method 3 |
| "I changed the poll / mesh / acceptance rule. Do I need a new convergence proof?" / "My convergence proof is stuck" | Workflow C, steps 3–7; Workflow E, steps 6–7 | Method 7, Method 3 |
| "How do I compare my method with others?" / "Which test problems?" | Workflow D: Benchmark design | Method 5, Method 4 |
| "How do I release my simulator as a benchmark?" | Method 4 steps; Workflow D, step 3 | Method 4, Method 2 |
| "Is this convergence result right / strong enough?" | Workflow E: Theory audit | Method 3, Method 7 |
| "Review my DFO paper draft" | Workflow E, then Workflow D checklist | Method 3, Method 5 |
| "What should my research agenda / thesis topic be?" | Research Heuristic 10 (status grid) plus Workflow A applied to candidate problems | Method 4, Method 1, Method 7 |
| Stages without evidence (grant strategy, lab management, talk design) | Say: "Audet has no distillable public method for this stage", then give a generic answer labeled "not Audet-style" | — |

## Agentic Protocol

### Step 1: Classify the question

| Type | Signal | Action |
|---|---|---|
| Needs facts | names a solver, paper, benchmark, or asks "does X exist?" | Step 2 before answering |
| Pure method | formulation, constraint treatment, experiment design, theory audit | go to the workflow (Step 3) |
| Mixed | the user's concrete problem plus a method question | do Step 2 on the specific points, then the workflow |

### Step 2: Audet-style fact finding (use tools, never memory)

Check, in this order (full list before tightening: `references/research/09-evidence-ledger.md#agentic-protocol`):
1. **The blackbox itself.** Cost per evaluation, budget, failure rate and regions, noise (same x, same output? reducible by more samples?), fidelity levels, a cheap surrogate, variable types (continuous, integer, granular, categorical, meta/dimension-changing, periodic), n.
2. **Constraint inventory.** Per output: quantifiable when violated? Unrelaxable? Hidden (known only through crashes)? Checkable before the simulation, at what cost or fidelity [S123 pp. 2–3]? Use the Le Digabel–Wild taxonomy (verified: Optim. Eng. 25(2), 2024, 10.1007/s11081-023-09839-3), as SOLAR does [S071 pp. 18–23].
3. **Existing tooling.** In the current NOMAD 4 user guide (GitHub: `bbopt/nomad/doc/user_guide`), is the needed variant (Mads-PIP, ADS, CatMADS, PSD-MADS, DMultiMads, StoMADS) in the current release, only in NOMAD 3, or a Python/MATLAB prototype [S021 pp. 4, 8, 18; S129 p. 19]?
4. **Literature for this pathology.** This skill's cards and technique catalog first, then "mesh adaptive direct search" + the pathology, GERAD cahiers (gerad.ca/en/papers), arXiv math.OC, SIAM J. Optim. / COAP / Optim. Eng.: does a MADS variant exist, and what stationarity does it prove?
5. **Benchmarks.** bbopt repos (STYRENE, SOLAR, AIRCRAFT_RANGE, SIMPLIFIED_WING, Cat-Suite, Micro-PRIAD, RUNGEKUTTA), COCO/BBOB, other groups' sets; say which paper version you cite (Method 5).

Keep this search internal. The user sees conclusions and next steps.

### Step 3: Answer

Conclusion first → numbered next steps, each labeled with a method → 🔴 checkpoints (when to stop, switch tools, or re-classify constraints) → limits of this lens for the user's situation.

## Research Taste

Full evidence per mark and warning sign: `references/research/09-evidence-ledger.md#taste-marks` and `#taste-warnings`.

### Marks of good research

1. **It starts from a real blackbox and names its pathologies** (cost, noise, failures, hidden constraints) instead of assuming smoothness [S019 p. 11; S023 p. 7; S071 p. 2].
2. **Guarantees are stated relative to smoothness and to the directions used, and the hypotheses are shown to be necessary** [S002 pp. 9–12; S025 TR pp. 3–12; S138 pp. 2–9].
3. **Practical freedom never costs the theory**: heuristics and models go into the Search or only order points, the Poll keeps convergence, Poll changes inherit theory (Method 7). "Regardless, this freedom must be retained." [S002 p. 3; S006 pp. 1, 14]. ⚠ Scope: Audet-led papers; an application-led filter-MADS run had no published proof [S039 pp. 11, 18].
4. **Constraint semantics are respected**: unrelaxable vs relaxable vs hidden, each treated differently [S007 pp. 2–4; S019 p. 53; S072 pp. 5, 7].
5. **Results are reusable**: the method ships in NOMAD, the problem as a public benchmark [S019 pp. 103–107; S071 pp. 13–14, 20–21]. ⚠ Most partner problems were not released (Method 4).
6. **Repeatability is valued**: deterministic where possible, seeds exposed where not [S021 pp. 14–16; S071 pp. 20–21]. ⚠ OrthoMADS directions are seeded since NOMAD 3.7.1 [S202 p. 104].
7. **Losses and reversals are reported next to wins**: "four examples are not conclusive evidence" [S001 pp. 19, 25]; the losing case explained [S032 pp. 27–28]; a test set admitted to favour a competitor [S129 pp. 21–22].

### Warning signs of bad research

1. **The algorithm assumes every evaluation succeeds** and every constraint is computable everywhere; simulations "may fail to give a result even for feasible points" [S019 pp. 15, 53; S072 pp. 5, 7].
2. **A theorem whose hypotheses were never tested for necessity**, or a vague stationarity notion for nonsmooth f [S025 TR; S138 pp. 2–9; D001 pp. 1–2].
3. **Solver comparisons that ignore evaluation budgets, or parameters tuned and reported on the same problems** [S128 pp. 4–16; S084 pp. 19–20; S057 p. 18].
4. **Only analytic test functions, or benchmarks and instruments nobody audited**: CUTEr-type problems "do not possess the same kind of difficulties" [S023 p. 19]; inherited instances that collapse to an LP [S015 pp. 7–9]; "A referee does not certify the admissibility of a point" [S156 p. 11]. ⚠ A missing cross-family solver is a weaker sign here (Method 5).
5. **DFO used where gradients or convexity are available**, or at large n: "If the optimization problem is convex, or if the functions are smooth and easy to evaluate, or if the number of variables is large, then NOMAD is not the solution that you should use." [S019 p. 11]
6. **A pure heuristic sold as an optimizer, with no convergence backbone** (the corpus wraps heuristics in MADS [S133 pp. 1, 3]; the stochastic-approximation line uses an ODE argument [S150 pp. 14–17]; the textbook: GA and Nelder–Mead "do not meet our definition of a DFO method", though "popular and effective" [B001 p. 15]).
7. **A surrogate chosen by fit error when it only needs to rank or filter points**: the classical metric can pick a model with the wrong minimizer [S046 pp. 13–15; S068 pp. 12–13].

### Taste quick-check

- [ ] Is each evaluation expensive enough (or opaque enough) that derivatives and finite differences are unreasonable?
- [ ] Have you listed what happens when the blackbox fails, and for which inputs?
- [ ] Is every output classified as objective, unrelaxable, relaxable/quantifiable, or hidden, and do you know which can be checked before the simulation?
- [ ] Can you state which stationarity your method guarantees (e.g., Clarke-type) and under which local smoothness?
- [ ] Does the new idea live in a step that does not break the convergence proof (Search, evaluation order, wrapper), and is any surrogate judged by how well it orders points? If it changes the Poll, is the new method an instance of a framework whose theorems already exist? (Methods 1, 7; Heuristic 3)
- [ ] Will you compare on evaluation budgets, first inside one code base, then with at least one realistic blackbox and one derivative-free solver from another family, with tuned parameters tested on problems they were not tuned on?
- [ ] Could the problem instance be released (executable, x0 feasible and infeasible, constraint types, best-known value) so others can test on it?
- [ ] Is n small enough, or can it be reduced by fixing, decomposing or partitioning variables?

## Core Research Methods

Full evidence per method (the text before tightening): `references/research/09-evidence-ledger.md` (`#method-1` … `#method-7`); counts and variants: `references/research/08-deep-reading-synthesis.md` §2–§4.

### Method 1: Free Search, rigid Poll

**One line**: Put every performance idea (surrogates, models, heuristics, global exploration) in an optional Search step, and keep a minimal Poll whose properties carry the convergence proof. Models may also order trial points, or shape the Poll if the guarantees are shown to survive (Method 7). Two more slots the proof cannot see: the evaluation order and a wrapper around the blackbox.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-1):
- Stated: "the search step contributes nothing to the convergence theory" [S031 pp. 4–5]; 2005, with Abramson and Dennis: the Search is crucial in practice "because it is so flexible, but it is a difficulty for the theory for the same reason" [S077 p. 4].
- Practice: a surrogate orders but never prunes the poll [S016 pp. 6, 10]; surrogate ensembles as Search [S046 pp. 7–8]; one pollster carries the PSD-MADS proof [S027 pp. 14–16]; mesh-free Search in ADS [S129 pp. 4, 9, 14].
- Say–do: ✅ stated + practiced, 1998–2026, six five-year periods (39 distinct works, 32 read in full); one exception, S150.
- ✗ **CatMADS is Poll-side**: its extended poll is "labeled as a poll, since it affects the convergence guarantees" [S121 p. 6].
- ⚠ **Model-informed Poll**: the default ORTHO N+1 QUAD picks the (n+1)th direction with a quadratic model [S019 pp. 55, 83]; ✗ the 2014 paper reduces the poll to n+1 points, not a Search [S038 abstract].
- ⚠ **Other theory-free slots**: evaluation order [S072 p. 6]; a wrapper around the blackbox [S112 p. 14].
- ⚠ **No direct search** in two coauthored doctoral-line papers [S150 pp. 14–17; S140 pp. 7–8].

**Steps**:
1. Write the Poll first: directions whose asymptotic properties (dense, or orthogonal and deterministic) give the stationarity you want; Poll-changing ideas go to Method 7.
2. Implement each practical idea as a Search proposing finitely many mesh points; a mesh-leaving trick can often be a one-point Search [S001 p. 17].
3. An untrusted model only orders trial points, never prunes the Poll, and is chosen by order agreement (leave-one-out order error, rank correlation), not fit error [S046 pp. 12–15] (catalog A3).
4. Check the proof when the Search always fails; if it breaks, move that part into the Poll or get it by membership (Method 7).
5. Measure the Search's value by switching it off in the same code (→ Method 5).
6. If the Search becomes the main driver, keep the Poll as safety net; one pollster point per iteration can suffice [S027 pp. 14–16].

**Applies to stage**: idea generation; algorithm design; software design.

**Different from standard practice**: model-based DFO lets the model drive every step, and metaheuristics often have no guarantee; here models mostly propose or order points, and a model inside the Poll keeps the guarantees [S121 pp. 6, 12–15].

**Limitations**: the Poll costs n+1 to 2n evaluations per failed iteration; asymptotic guarantees say little about finite budgets; the mesh restricts trial points [S129 pp. 4, 9, 14].

### Method 2: Constraint semantics first

**One line**: Before choosing an algorithm, classify every blackbox output (objective; unrelaxable constraint; relaxable and quantifiable constraint; hidden constraint shown only as failure), because each class gets a different treatment: extreme barrier, progressive barrier, or failure tagging. The same discipline applies to inputs: the user defines what "local" means for categorical variables.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-2):
- Stated: NOMAD guide: EB constraints "need to be always satisfied (unrelaxable constraints)"; PB constraints "need to be satisfied only at the solution"; for hidden constraints "the evaluation simply fails" [S019 p. 53]. In 2005: "yes/no" constraints at every trial point, open constraints only at the solution, failed runs as +∞ [S077 pp. 2–3].
- Practice: PB grew from STYRENE's 4 closed and 7 open constraints [S007 pp. 2–4, 31]; binary constraints relaxable but unquantifiable [S072 pp. 5, 7]; a priori constraints [S071 pp. 18–23]; categorical neighbourhoods [S121 pp. 6–7, 20].
- Say–do: ✅ stated + practiced, six five-year periods (41 distinct works, 35 read in full); no contradiction.
- ⚠ **When and at what cost** a constraint is computable is a second axis [S123 pp. 2–3; S173 pp. 1, 5].
- ⚠ **The algorithm can override the default**: interrupted evaluations put relaxable constraints under EB [S123 pp. 3, 6].
- ⚠ **Semantics for inputs**: the neighbour set fixes "local"; stronger optimality has a stated price [S011 pp. 8, 22].

**Steps**:
1. List every output; write each constraint as c_j(x) ≤ 0, two-sided bounds as two outputs [S019 p. 39].
2. Per constraint: computable when violated? Meaningful amount? Must hold at every evaluated point? Computable before the run [S123 pp. 2–3]?
3. Unrelaxable or unquantifiable → EB; relaxable and quantifiable → PB (`CSTR` if unsure); equalities → EQPB with Mads-PIP, or reformulate linear ones [S064 pp. 4–10]; interrupted or low-fidelity evaluations → EB.
4. Make crashes explicit (separate executable, non-zero exit), never a large finite penalty [S019 pp. 39, 48].
5. Check a priori constraints in the wrapper (not counted); stop once a point cannot become the incumbent [S071 pp. 18–23] (Heuristic 2).
6. For categorical or meta variables, have the user define (or learn once) the neighbourhood; report evaluations to find vs to certify [S121 pp. 7, 20].
7. Provide feasible and infeasible starts; PB can start infeasible.
8. After the first run, re-check the classification; if PB points stay infeasible too long, tighten bounds or reformulate before changing algorithms.

**Applies to stage**: problem formulation; experiment design; debugging.

**Different from standard practice**: the usual approach folds all constraints into one penalty; here each constraint type is a user modeling decision with its own mechanism.

**Limitations**: it needs the user to know the constraint physics, and misclassification can stall the search; hidden constraints give no feasibility gradient [S090 pp. 8–10].

### Method 3: Guarantee ladder, bounded by counterexamples

**One line**: State convergence as a ladder of optimality conditions that depends on local smoothness and on the directions used, then build the smallest counterexamples showing which hypotheses cannot be dropped. Apply the same test to published results (including your own), to rival methods and to your measuring instruments.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-3):
- Stated: "We admit that the flexibility in the choice of polling directions is exploited to lead to a weak result, but our point is that it can happen." [S005 p. 24]
- Practice: three counterexamples to Torczon's results [S025 TR pp. 3–12]; hierarchy (i)–(vii) [S002 p. 12]; GPS converging to a saddle [S020 pp. 13–15]; a peer's theorem refuted and repaired [S138 pp. 2–9].
- Say–do: ✅ stated + practiced, 1998–2026, seven five-year periods (39 distinct works, 32 read in full), with the corrections below.
- ✗ **Order**: the counterexamples came first (1998 Rice report [S025 TR pp. 1–3]); the GPS analysis supplements them [S002 pp. 3, 14].
- ✗ **Complexity is not absent**: bounds in a coauthored zeroth-order paper [S140 pp. 21–22] and the notes with Hare [S120 pp. 15–16; S124 pp. 10–11]; the MADS line stays asymptotic.
- ✗ **The erratum was a proof erratum**: "even though the statement of Proposition 4.2 is correct, its proof is not compatible with the final notation" [D001 p. 1].
- ⚠ **Beyond one's own theorems**: rival-failure toys [S129 pp. 5–6]; one counterexample per multiobjective indicator [S004 pp. 7–10].

**Steps**:
1. Write the guarantee as a ladder ("if f is Lipschitz near x̂, then a Clarke generalized-derivative condition holds along refining directions; if f is strictly differentiable, then ∇f(x̂)=0") [S002 p. 12]; summarize it as a numbered hierarchy or a case → theorem → assumptions table (catalog W6).
2. Per hypothesis (Lipschitz, strict differentiability, density of directions, constraint qualification), try a 2D example that breaks the conclusion without it: free choices (Search, pattern, poll order, step parameters) adversarial but legal, f defined only where the iterates go and extended smoothly so level sets stay compact, proof by induction over a periodic block [S025 TR pp. 4–12] (catalog P5).
3. If it will not break, check whether the proof uses it; if not, drop it [S137 pp. 11–12]. Prefer hypotheses checkable a priori [S031 p. 20].
4. Audit the theorem you build on, the rival and your instruments too. If a published theorem fails, number the steps of its proof, certify the valid ones, refute the false implication with the simplest function you can, publish the counterexample with a repair (an extra poll step, a stronger hypothesis), run the counterexample through the repaired algorithm, and say which results survive [S138 pp. 2–9].
5. Prefer deterministic variants [S006 p. 1]; randomness only for non-shrinking probes [S138 pp. 7–9] (catalog A14).
6. For your own errors, re-prove in the final notation and say first whether the statement or only the proof changed [D001 p. 1] (catalog W8).

**Applies to stage**: theory; result judgment; reviewing.

**Different from standard practice**: one theorem under convenient assumptions is common; here the output is a hierarchy plus proofs that the assumptions are needed.

**Limitations**: MADS-line results are asymptotic [S053 pp. 11–20]; counterexample crafting is tacit skill; recent algorithm papers carry fewer necessity examples [S121 pp. 12–15].

### Method 4: Turn real blackboxes into public benchmark artifacts

**One line**: Take problems from engineering partners and student theses, and release them as executables with a fixed input/output contract, constraint classification, a surrogate, starting points and a best-known solution, so every later algorithm is tested on a real pathology.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-4):
- Stated: "In fact, it seems that no work exhibits a realistic application specifically developed for BBO benchmarking." [S071 p. 3]
- Practice: STYRENE [S007 p. 31]; pooling data online in 2004 [S015 pp. 5, 15–16]; SOLAR frozen as a reproducible executable [S071 pp. 3, 13–32]; Micro-PRIAD [D006 pp. 6, 13, 23–31]; Cat-Suite [S130 pp. 3, 5–7]; a textbook appendix of five real blackboxes with software (2026) [B001 pp. 9, 21].
- Say–do: ✅ stated + practiced for the group's own benchmark papers, six five-year periods (35 distinct works, 33 read in full); ⚠ scope below.
- ⚠ **Scope**: no public release is mentioned for the partner blackboxes in S013, S032, S145, S084, S143 and S167; once, a scaled-down public twin [D006 pp. 4, 6, 22].
- ⚠ **Steps 2 and 5 are the STYRENE/MDO pattern**: SOLAR keeps physical units and credits values, not points [S071 pp. 17–18, 23, 28].

**Steps**:
1. Wrap the simulator: `bb.exe x.txt` prints the objective then constraints c_j(x) ≤ 0; non-zero exit status = failure [S019 pp. 39–40].
2. Scale variables (STYRENE and MDO use [0,100]) or keep physical units, and say which.
3. Classify constraints (→ Method 2) in the README, including a priori checks [S071 pp. 18–23].
4. Ship a surrogate or fidelity switch and seeds; freeze and version the release (solarX.1) with a self-check [S071 pp. 13–14, 20–21].
5. Provide feasible and infeasible starts and a credited best-known solution, updated publicly.
6. Certify non-triviality: LHS feasibility census against a solver's rate, output variability, active constraints at the best-known point [S071 pp. 24–32] (catalog B2): "Without them, the solution to many of the problems would be trivial or impractical." [S071 p. 11]
7. Publish with a citable paper; if the simulator cannot leave the partner, release a scaled-down public twin [D006 pp. 4, 6, 22].

**Applies to stage**: problem choice; benchmarking; long-term agenda.

**Different from standard practice**: most DFO papers test on analytic functions (CUTEst, Moré–Wild) only; here the application becomes a durable community asset.

**Limitations**: it needs willing partners and a software engineer; lags are long (nine years for SOLAR [S071 pp. 3, 35]); benchmark and solver share a group [S175 p. 12].

### Method 5: Budget-aware, cross-community benchmarking

**One line**: Compare methods by what they achieve per blackbox evaluation, over whole problem sets, first against controlled variants inside one code base and then against strong solvers from other derivative-free families on their home ground, and publish the benchmarking methodology itself.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-5):
- Stated: the benchmarking summary fixes the currency first, the number of calls to the simulation, because each call is expensive (paraphrase) [S128 p. 4]; "having a test set that is representative of the ultimate goal is crucial." [S128 p. 4]
- Stated (textbook, with Hare): benchmarking is Chapter 4 of Part 1 in 2026, after only the naive algorithms of Ch. 3, in all three sample syllabi (the practical course ends with it), with added sections for constrained, surrogate and biobjective problems [B001 pp. 9, 11, 15, 18–19]; in 2017 it was an appendix [B001 pp. 16–17] (comparison of editions: reader's).
- Practice: PBTR vs COBYLA (smooth) and vs NOMAD (MDO) [S063 pp. 6, 17–23]; same-solver first, then three families [S172 pp. 16–19]; four families with h-profiles [S175 pp. 8, 11]; the benchmarking summary [S128 pp. 4–16].
- Say–do: ✅ for evaluation currency, profiles and fair baselines; ⚠ for "cross-community": 16 full cards compare across families, about as many only inside NOMAD (`08` §2.2).
- ✗ **StoMADS test set is version-dependent**: arXiv v1 uses 66 noisy Moré–Wild CUTEst instances [S053 p. 21], not YATSOp/STARS.
- ⚠ **Bounded by the group's own summary**: no derivative-based competitors, few algorithms at a time [S128 pp. 5, 9, 13–14].
- ⚠ **The currency moved**: CPU time [S015 pp. 10–13], Monte Carlo draws [S084 pp. 19–20], weighted effort [S128 p. 15].
- ⚠ **Partner-led application papers use single runs** [S204 pp. 17–19]; read Method 5 as a rule for algorithm papers.

**Steps**:
1. Fix the currency (evaluations, or time if costs vary) and budget; weight mixed effort (N = N_t + w·N_s) and check two weights [S128 p. 15].
2. Use three layers of problems: the competitor's home ground, realistic blackboxes, your pathology; audit inherited instances (Workflow D, step 3).
3. Compare the mechanism first inside one code base, current default included [S172 pp. 16–17, 20]; then other derivative-free families on their home ground, few at a time [S128 pp. 5, 9].
4. Data and performance profiles with shared f0 and f*; flag and drop instances no solver improves; for infeasible starts plot h until the first feasible point, then f (catalog E4); re-plot without the fastest solver [S128 pp. 9, 13–14]; Pareto-compliant indicators for multiobjective [S004 pp. 19–21].
5. Report seeds and spread; treat differences inside the ±2σ noise band as noise [S060 pp. 8, 11–12].
6. After redesigning your own solver, show parity with the old version first: common features, several seeds [S021 p. 14] (catalog E14).
7. Report where the method loses and why, with mechanism counters beside the profiles [S129 pp. 21–23] (catalog E10, E11).

**Applies to stage**: experiment design; result judgment; writing.

**Different from standard practice**: final values on analytic sets against weak baselines are common; here competitors play at home, and all effort has one currency.

**Limitations**: realistic blackboxes are expensive, so problem sets are small; profile choices and the weight w are judgment calls [S128 p. 15]; the textbook chapter is unread (✗ in 2017 an appendix, not a chapter [B001 pp. 16–17]).

### Method 6: The solver as research instrument

**One line**: Every published algorithmic idea is integrated into one long-lived solver (NOMAD) with benchmark-tuned defaults, several interfaces and a documented symptom-to-remedy table, so research results reach engineers and user problems flow back into research.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-6):
- Stated: "In continuous development since 2001, it constantly evolved with the integration of new algorithmic features published in scientific publications." [S021 p. 1]; 2005, co-authored: the interest in direct search "came directly from users" [S077 p. 2].
- Practice: NOMAD C++ at ExxonMobil and Boeing, 2000–2003 [D016 pp. 3, 5, 16]; the 2014 anisotropic mesh made default [S202 pp. 104, 110]; release notes map versions to papers [S019 pp. 103–107]; version parity [S021 p. 14].
- Say–do: ✅ stated + practiced, six five-year periods (40 distinct works, 34 read in full); no contradiction.
- ✗ The first pass quoted a search-summary wording of this abstract [S021 p. 1].
- ⚠ **Prototypes outside NOMAD**: Python [S129 p. 19], MATLAB [S120 p. 21], a solver-agnostic wrapper [S173 pp. 18, 23].
- ⚠ **Features lag papers**: RobustMADS, StoMADS and categorical variables not yet ported in the NOMAD 4 version read [S021 pp. 4, 8, 14, 18].

**Steps**:
1. Implement each accepted algorithm as a NOMAD component behind a parameter; the theory's contract is the plug-in interface [S019 p. 100] (→ Method 7, step 5).
2. Set defaults after benchmarking, as a compromise [S019 p. 73]; keep an old default behind a named switch [S202 p. 110].
3. Publish symptoms and remedies: "Difficult constraint" → "Try PB instead of EB"; "No initial point" → "Add a LH search" [S019 p. 74].
4. Treat user reports and industrial problems as the next research questions (→ Method 4).
5. When the architecture blocks new ideas, redesign, then check parity first [S021 pp. 2–3, 14] (catalog E14).
6. Share the post-processing instrument so all profiles follow one protocol [S128 p. 16].

**Applies to stage**: dissemination; research organisation; debugging users' runs.

**Different from standard practice**: not a prototype per paper, but one maintained product with 25 years of methods, and the channel to industry.

**Limitations**: it needs a stable team and a research software engineer; features lag papers [S021 p. 18]; one codebase can bias the benchmarks it defines [S175 p. 12].

### Method 7: Generalize, then inherit

**One line**: When a new idea changes the Poll, the mesh or the acceptance rule, get its theory by membership rather than a fresh proof, through three devices: re-prove your own earlier flagship as an instance of the new framework (and the new method as an instance of a proved one); admit adaptive mechanisms only if they stop changing after finitely many iterations; expose the theory's contract as the software's plug-in interface. Writing a framework theorem and checking that new rules collapse to old ones is shared ground with the Conn and Vicente lenses.

**Evidence** (full evidence: references/research/09-evidence-ledger.md#method-7):
- Stated: "The convergence results for ORTHOMADS follow directly from those already published for MADS, and they hold deterministically, rather than with probability one, as for LTMADS, the first MADS instance." [S006 p. 1]
- Practice: GPS as the Δᵖ = Δᵐ case of MADS [S001 p. 4]; OrthoMADS and QRMADS as ADS instances [S129 pp. 16–19]; PSD-MADS as an "apparent pollster" instance [S027 pp. 14–16]; eventually-static adaptation [S074 pp. 12, 14].
- Say–do: ✅ stated + practiced, 2001–2026: 22 distinct cards carry an instance, collapse or finite-change proof (listed in the ledger).
- ⚠ **Exclusivity**: ✅ for the three devices; moderate for the shared steps (Conn and Vicente lenses; Torczon's GPS framework [S002 pp. 1, 11]).
- ⚠ **Where inheritance fails, the papers say what is lost**: PSD-MADS loses the zeroth-order result [S027 p. 17]; StoMADS rehosts a supermartingale argument [S053 pp. 12–19].

**Steps**:
1. List the instance obligations first. For MADS: poll directions are nonnegative integer combinations of D; poll points lie within Δᵖ of the poll center; limits of normalized poll sets are positive spanning; normalized directions over failed iterations are dense in the unit sphere [S006 p. 14].
2. Name the collapse parameter that gives back the old method (Δᵖ = Δᵐ → GPS [S001 p. 4]; h^max_0 = 0 → MADS-EB [S007 p. 12]).
3. Prove membership both ways (new method in a proved framework, your old flagship in the new one) by a parameter map and induction [S129 pp. 16–19] (catalog P9).
4. Let adaptive mechanisms change only finitely often, then reuse the old analysis [S074 pp. 12, 14] (catalog P8); otherwise build the 1-D example and prove the weaker property [S144 pp. 10–12].
5. Expose the proof's contract (finitely many trial points, on the mesh, within budget) as the plug-in interface [S021 pp. 6–7, 11].
6. Where inheritance fails, say which rung is lost [S027 p. 17]; separate classes with one example [S020 pp. 13–15].

**Applies to stage**: algorithm design; theory; software design.

**Different from standard practice**: framework theorems are common; re-hosting one's own flagship in each successor, and admitting adaptive heuristics only with finitely many changes, are not.

**Limitations**: only asymptotic, Clarke-type results are inherited [S023 p. 7]; stochastic variants and wrappers do not inherit automatically [S112 p. 14]; instance proofs must use the final notation [D001 p. 1]. (Method 1: Search ideas; Method 7: Poll/mesh changes; Method 3 audits the guarantee Method 7 builds.)

## Stage Workflows

Full step text and card lists: `references/research/09-evidence-ledger.md#workflow-a` … `#workflow-e`.

### Workflow A: Blackbox intake (is this a DFO problem, and how should it be formulated?)

**Input**: the simulator's cost per run, budget, n, variable types, outputs, known failures, noise, surrogates or fidelities.

**Steps**:
1. Run the Taste quick-check; for convex, cheap-smooth or large-n problems recommend another method (→ Warning sign 5). Sequential MADS is recommended for n ≤ 50 [S021 p. 11]; beyond that, fix variables or use PSD-MADS.
2. Classify each output (objective, EB, PB, EQPB, hidden) and note which is computable before the simulation, at what cost [S123 pp. 2–3] (→ Method 2).
3. Inventory inputs (continuous, integer, granular, categorical, meta); get or learn the categorical neighbourhoods [S121 pp. 6–7, 20].
4. Define the I/O contract (executable, `x.txt`, output order, non-zero exit on failure, scaling, bounds) with a priori checks in the wrapper [S071 pp. 18–23] (→ Method 4).
5. Look for a reformulation that provably transfers optima (linear equalities [S064 pp. 4–10]; only the "singular" variables to DFO [S151 pp. 3–8]) (→ Heuristic 9; catalog P13, A11).
6. Route cheap information (surrogate, lower fidelity, grey-box structure) to the Search or to ordering; judge a surrogate by rank correlation [S167 p. 8].
7. Stochastic outputs: run a noise census (replicate one point, keep the ±2σ band) [S060 pp. 8, 11–12]; whether more samples reduce the noise decides the algorithm (Workflow B, step 7).
8. Pick feasible and infeasible starts; if none, plan an LH search counted in the budget [S159 p. 16].

**🔴 Checkpoint**: if more than about 30% of trial evaluations fail, or the user cannot say which constraints are relaxable, stop and fix the formulation (bounds, reparameterization, classification) before running any optimizer. A rough heuristic threshold, not Audet's number.

**Output**: a one-page formulation: variables, bounds, input and output tables, failure handling, noise census, budget, starts, NOMAD settings.

### Workflow B: Solve-and-diagnose loop (NOMAD or any direct search)

**Input**: the formulation from Workflow A, a first run's history or statistics file, the symptoms.

**Steps**:
1. Run NOMAD 4 with defaults, typed constraints (EB/PB/CSTR) and `MAX_BB_EVAL` = budget; save history and cache (→ Method 6).
2. Map the symptom to a documented remedy, one change at a time [S019 p. 74]: difficult constraint → PB instead of EB; no initial point → LH search; badly scaled variables → scaling or Δ0 per variable; many variables → fix some, or PSD-MADS; unsatisfactory solution → other directions, start or seeds, a VNS or LH search, models off, or (NOMAD 4) "Try Mads-PIP or ADS algorithms" (Mads-PIP for equalities, ADS when the mesh blocks progress [S129 p. 22]); slow → parallel evaluations or a surrogate. Rescale constraints of very different magnitudes [S144 pp. 9–10].
3. Compare each change with the previous run at equal evaluation counts (→ Method 5).
4. Mine the cache first: mesh sizes from good points, sensitivities, re-scoring after a merit change [S073 pp. 22–23] (→ Heuristic 2).
5. If starts end in different local minima, run a global heuristic, then hand over to MADS with the shared cache [S073 pp. 22–24] (catalog A17).
6. If failures cluster, bound them out or add an unrelaxable constraint; at a discontinuity, distance to the region can become a PB constraint [S090 pp. 8–10].
7. If noise is present, choose by what controls it (→ Method 1; catalog A5):
   - controllable by sample size → adaptive precision (MpMads, DpMads), profiles priced in draws [S084 pp. 3, 5–9, 19–20];
   - uncontrollable → StoMADS (NOMAD 3 / MATLAB repo) or replications; "MADS is not appropriate for stochastic blackbox optimization" [S053 p. 28];
   - below decision precision → round the objective [S166 p. 8];
   - categorical variables plus noise: no card covers both, so advice there is generic, not Audet-style.

**🔴 Checkpoint**: stop tuning once three successive single-parameter changes give no improvement at equal budget (a rough threshold, not Audet's number; on a noisy blackbox, judge improvement against the ±2σ band from the noise census). Go back to Workflow A: the formulation, not the solver, is the likely problem.

**Output**: the final parameter file, a before/after plot at equal budgets (the user's own runs), the settings with reasons, remaining risks.

### Workflow C: Algorithm design for a new blackbox pathology

**Input**: a pathology not handled well (categorical variables, multi-fidelity or equality constraints, discontinuities) and a target application.

**Steps**:
1. Check whether a MADS variant exists (Agentic Protocol, Step 2) and what it proves.
2. Draw the failure first: a 1-D or 2-D toy where the existing method, yours included, cannot reach an obvious point [S129 pp. 5–6] (→ Method 3; catalog W4).
3. Decide what the Poll must guarantee; if the idea changes the Poll, mesh or acceptance rule, list the instance obligations [S006 p. 14] (→ Method 7).
4. Put the pathology-specific intelligence in the Search, the evaluation order or a wrapper [S072 p. 6; S112 p. 14] (→ Method 1).
5. Make every adaptive mechanism change only finitely often (→ Method 7, step 4).
6. When importing a mechanism from another family, re-prove it, retune donor-specific parameters, and tie vanishing parameters to the step size [S063 pp. 13, 20–22] (catalog A5, A12).
7. Prove the ladder and attempt counterexamples (→ Method 3); if stuck, Workflow E, step 7; say which rung is lost where inheritance fails [S027 p. 17].
8. Prototype in NOMAD or a shared repo; benchmark same-solver first (→ Methods 5, 6).
9. Release a benchmark instance with the pathology (→ Method 4).

**🔴 Checkpoint**: if the convergence proof needs the Search to succeed, redesign. If a 2D counterexample breaks your main theorem, stop and fix the theory before running more experiments. If an adaptive rule can change infinitely often, the inherited theorem does not apply: freeze it eventually or prove the weaker property [S144 pp. 10–12].

**Output**: algorithm sketch (Search/Poll split, or parent framework and collapse parameter), target theorem with hypotheses, counterexamples to attempt, benchmark plan.

### Workflow D: Benchmark design

**Input**: the method, the competitors, candidate problems, the budget.

**Steps**:
1. Fix the evaluation currency, budget and effort weights (→ Method 5, step 1).
2. Assemble three layers: the competitor's home ground, realistic blackboxes (bbopt, COCO constrained), your pathology (→ Method 5, step 2).
3. Audit instances: re-evaluate published solutions, report inherited instances that collapse to easy cases [S015 pp. 7–9], run an LHS feasibility census on new ones [S175 p. 9] (catalog E9, B2).
4. Plan comparisons and profiles (→ Method 5, steps 3–5).
5. If a heuristic seeds an exact method, run it cold and warm; report evaluations to find vs to certify [S015 p. 9] (catalog E8).
6. Tune on one subset of problems, report on held-out ones, fixing gameable parameters (stopping tolerances) first [S057 p. 18] (→ Heuristic 7; catalog E7).
7. Plan the redesign-parity check and the loss report (→ Method 5, steps 6–7).

**🔴 Checkpoint**: if your method wins only on problems you designed, or only under accuracy profiles, the result is not publishable as a general claim. Narrow the claim or add problems.

**Output**: a benchmark protocol table (problems, n, constraint types, budgets, competitors, settings, seeds, profiles, effort weights). No fabricated results.

### Workflow E: Theory audit (paper, draft, claim, or your own stuck proof)

**Input**: the theorem statement, assumptions and algorithm.

**Steps**:
1. Rewrite the result as a guarantee ladder: which stationarity, under which local smoothness, along which directions? (→ Method 3, step 1)
2. For each assumption, attempt a low-dimensional counterexample (discontinuous f, non-Lipschitz f, finite direction set, CQ failure), using the algorithm's free choices adversarially but legally; one per hypothesis or failing converse [S120 pp. 5–11] (→ Method 3; catalog P7).
3. Could "with probability one" results be deterministic, and does it matter [S138 pp. 7–9]?
4. Are constraints assumed computable everywhere? (→ Method 2)
5. If a flaw is suspected, follow the refute-and-repair protocol (→ Method 3, step 4).
6. Check inheritance claims: parameter map, instance obligations, finitely many adaptive changes, final notation [S129 pp. 16–18; D001 p. 1] (→ Method 7).
7. **Proof-debugging checklist** (your own direct-search proof is stuck). Go down the list; the first item that fails is the lemma to work on:
   1. Does liminf Δ → 0 still hold: integer lattice with rational τ (catalog P2), or exclusion balls and packing without a mesh (catalog P3)?
   2. Is there a refining subsequence (failed iterations with step sizes going to zero)?
   3. Does the failed-poll inequality give one difference quotient of the Clarke derivative (catalog P1)?
   4. Are the normalized refining directions dense, and does each transformation you apply (scaling, rounding, reflection, completion by a model-chosen direction) preserve density (catalog P4; the four MADS instance properties [S006 p. 14])?
   5. Do the adaptive rules change only finitely often (catalog P8)?
   6. Can membership in a proved framework be shown by a parameter map and induction instead (catalog P9)?
8. Audit the instruments the evidence rests on (indicators, surrogate scores, benchmark referees) [S004 pp. 7–10; S156 p. 11].

**🔴 Checkpoint**: do not assert a theorem is wrong without an explicit, checked counterexample. Otherwise say "suspicious, unverified".

**Output**: an audit note: ladder, necessary hypotheses, suspected gaps with counterexample sketches, first failing checklist item, repairs.

## Research Heuristics

Full case lists: `references/research/09-evidence-ledger.md#heuristic-1` … `#heuristic-10`.

1. **If a constraint must hold for the simulation to be meaningful, use the extreme barrier; if its violation is measurable, the progressive barrier; if unsure, CSTR (PB). Run a crashing simulator as a separate executable so crashes count as failed evaluations.** Case: [S007 pp. 2–4, 31; S019 pp. 48, 53; S123 pp. 3, 6].
2. **If some outputs are cheaper or earlier in the pipeline, evaluate them first, stop once the point cannot become the incumbent, flag a-priori rejections as not counted, and mine the cache before a new evaluation.** Case: [S001 p. 4; S123 p. 3; S073 pp. 22–23].
3. **If you want a faster direct search, add the idea as a Search step and leave the Poll untouched; an untrusted model only orders candidates and is judged by order error, not fit error; a Poll-shaping model needs Method 7.** Case: [S046 pp. 12–15; S016 pp. 6, 10; S019 pp. 55, 83].
4. **If you have proved a convergence theorem, try to break each hypothesis with a small example before publishing, using the algorithm's free parameters adversarially but legally; test the rival and your instruments too.** Case: [S025 TR pp. 4–12; S138 pp. 2–9; S004 pp. 7–10].
5. **If an application produced a hard, realistic problem, release it as a benchmark (truth model, surrogate, starting points, best-known solution), certified non-trivial and frozen.** Case: [S007 p. 31; S071 pp. 11, 13–14, 20–32; S130 pp. 5–7].
6. **If you compare solvers, count blackbox evaluations (weighted when effort differs in kind), compare mechanisms first inside one code base, then add a strong derivative-free competitor from another family on its home ground.** Case: [S063 pp. 6, 17–23; S172 pp. 16–20; S128 p. 15].
7. **If an algorithm has tunable parameters, tune it as a blackbox with direct search on one subset of problems, report on held-out problems, and fix first the parameters the objective could game (stopping tolerances).** Case: [S016 pp. 5–6, 15–18; S057 pp. 17–18; S095 p. 9] (catalog E7).
8. **If randomness is not needed for the guarantee, make the method deterministic or seeded; add randomness only where a guarantee needs dense, non-shrinking probes.** Case: [S006 pp. 1, 3; S202 p. 104; S138 pp. 7–9].
9. **If the "blackbox" exposes structure (monotonicity, linear equalities, hierarchy, fidelities), exploit it while keeping a convergence backbone; put cost-saving ideas in a wrapper, pay one true evaluation before a cheap verdict changes the incumbent, and give DFO only the pathological variables.** Case: [S064 pp. 4–10; S112 pp. 7–8, 14; S151 pp. 3–8].
10. **If you are choosing a thesis or agenda topic, map the problem family as a status grid (trivial, solved, open), pick one pathology from the open cells, and plan algorithm, theory, NOMAD integration and benchmark together.** Case: thesis-to-paper pipeline (inferred from bibliography); [S092 pp. 7, 10; S156 p. 10; S121 p. 1] (catalog W10).

## Signature Work Anatomy

Two further full-text anatomies (OrthoMADS, summarized in the MADS table below, and ADS with its PB sequel) are in `references/research/01-publications.md` §3. Full rows: `references/research/09-evidence-ledger.md#signature-work-1` … `#signature-work-5`.

### Mesh adaptive direct search algorithms for constrained optimization (SIAM J. Optim. 2006, 10.1137/040603371; read in full [S001], with the erratum [D001], the AFOSR report [D016] and OrthoMADS [S006])

| Dimension | Content |
|---|---|
| Origin | GPS's finite direction set, "the primary drawback of GPS algorithms in our opinion" [S001 p. 1]; MADS "allows us to show the convergence results that we always wished for in GPS, but knew did not hold." [D016 pp. 4–5] |
| Why then | GPS hierarchy, tightness examples and filter GPS in place [S001 pp. 1–2, 26]; AFOSR, Boeing and ExxonMobil funding [S001 p. 1]; NOMAD C++ already in their projects [D016 pp. 3, 5, 16]. |
| Key insight | Mesh size Δᵐ ≤ poll size Δᵖ, both → 0, so finer lattices allow ever more directions; GPS is the equal case [S001 pp. 4–6]. |
| Minimal evidence | Clarke-to-KKT hierarchy [S001 pp. 11–13]; LTMADS density with probability one [S001 pp. 14–19]; four test problems, one violating the hypotheses [S001 pp. 19–25]. |
| Abandoned paths | GPS's finite direction sets; LTMADS's randomness, replaced by OrthoMADS (2009) [S006 pp. 1–14], seeded since NOMAD 3.7.1 [S202 p. 104]. |
| Reception | A proof erratum (2008) [D001 pp. 1–2]; core of NOMAD 3/4 [S021 pp. 4, 14]; OrthoMADS proved an ADS instance [S129 pp. 16–19]; adopted in-house by an industrial group for its reliability, per Dennis's textbook foreword (a co-author, not independent) [B001 p. 7]; 1952 citations at harvest. |
| Methods shown | Method 1, Method 3, Method 6, Method 7 |

### A progressive barrier for derivative-free nonlinear programming (SIAM J. Optim. 2009, 10.1137/070692662; read in full [S007])

| Dimension | Content |
|---|---|
| Origin | Stated: the authors' GPS filter combined with MADS under the extreme barrier, which needs a feasible start [S007 p. 2]. |
| Why then | Four user situations: no feasible start, constraint-sensitivity information, failing or Boolean industrial codes, evaluations saved by violations [S007 pp. 3–4]. ✗ The first pass inferred a NOMAD 3 need for a default; the paper does not say this. |
| Key insight | "A progressive barrier algorithm places a threshold on the constraint violation it allows, and progressively tightens this threshold as the algorithm progresses." [S007 p. 3]; it polls a best feasible and a best undominated infeasible incumbent; h^max_0 = 0 with a feasible start recovers MADS-EB [S007 pp. 2–13] (catalog A4). |
| Minimal evidence | Hierarchy (i)–(x) with a counterexample forcing A3 [S007 pp. 15–25]; STYRENE, five seeds, both starts [S007 pp. 25–32]; "We need more tests, but we tentatively conclude [...]" [S007 p. 33]. |
| Abandoned paths | "We do not use a filter, but we do use the notion of dominance fundamental to filters" [S007 p. 3]. |
| Reception | Exported to a trust region with Conn [S063 p. 23], discontinuity escape [S090 pp. 8–10] and ADS-PB [S172]; PB is the `CSTR` default [S019 p. 53]. |
| Methods shown | Method 2, Method 1, Method 3, Method 7 |

### Algorithm 1027: NOMAD version 4: Nonlinear optimization with the MADS algorithm (ACM TOMS 48(3):35, 2022, 10.1145/3544489; arXiv v2 read in full [S021])

| Dimension | Content |
|---|---|
| Origin | "In continuous development since 2001" [S021 p. 1]; NOMAD 3's minor-release growth and unanticipated algorithm interactions led to a full redesign [S021 pp. 2–3]. |
| Why then | Features had outgrown NOMAD 3; NSERC grants with Hydro-Québec, Rio Tinto and Huawei-Canada [S021 p. 18]. |
| Key insight | Nested Start/Run/End components so new algorithms plug in; the Search's theory contract as plug-in interface; a shared evaluation queue [S021 pp. 5–11]. |
| Minimal evidence | "Comparing the performance of the two versions is crucial to validate that algorithms have been correctly coded." [S021 p. 14]; parity on 53 smooth and 18 constrained problems, 10 seeds; up to 3.3× on 8 cores [S021 pp. 14–17]. |
| Abandoned paths | Not yet ported in the version read: VNS, BiObjective, ORTHO N+1, RobustMADS, StoMADS, categorical variables [S021 pp. 4, 8, 14, 18]. |
| Reception | The standard NOMAD citation; outside uses [S021 p. 2]; later algorithms built on it [S121 p. 19]. |
| Methods shown | Method 6, Method 5, Method 1, Method 7 |

### solar: A solar thermal power plant simulator for blackbox optimization benchmarking (Optimization and Engineering 2024/25, 10.1007/s11081-024-09952-x; arXiv 2406.00140 v1 read in full [S071])

| Dimension | Content |
|---|---|
| Origin | A 2015 MSc model [S071 pp. 3, 35] released into a gap: "In fact, it seems that no work exhibits a realistic application specifically developed for BBO benchmarking." [S071 p. 3] |
| Why then | NSERC Alliance–Mitacs grant with Hydro-Québec [S071 p. 1]. |
| Key insight | One physics simulator with switches (instance, seed, replication, fidelity) and non-trivializing constraint models, frozen as release 1.0 with a self-check [S071 pp. 3, 11–27]. |
| Minimal evidence | LHS vs NOMAD feasibility; data profiles from 30 starts for NOMAD 3, NOMAD 4 and CMA-ES, none systematically reaching the best known value [S071 pp. 24–30]. |
| Abandoned paths | Simplifications stated with their bias; only best values published [S071 pp. 8, 13, 28]; "Some bugs may still be present in the code, as is often the case in real blackbox problems." [S071 p. 23] |
| Reception | Four solver families benchmarked on it [S175 pp. 7–11]; reused in the group's algorithm papers [S129 pp. 24–25]; outside uptake not verified. |
| Methods shown | Method 4, Method 5, Method 2 |

### Convergence results for generalized pattern search algorithms are tight (Optimization and Engineering 5:101–122, 2004, 10.1023/B:OPTE.0000033370.66768.a9; read via its precursor, Rice CRPC-TR98779, 1998 [S025])

| Dimension | Content |
|---|---|
| Origin | ✗ Corrected (first pass: "follows the 2003 GPS analysis"): the 1998 Rice report probes Torczon's 1997 results [S025 TR pp. 1–3]; the GPS analysis supplements it [S002 pp. 3, 14]. |
| Why then | Torczon's GPS theory was new; Audet had just started his NSERC postdoc at Rice [S025 TR pp. 2–3]. |
| Key insight | Turn the algorithm's legal freedoms against it on the smallest C¹ function defined only where the iterates go: convergence to a maximizer, a nonzero-gradient accumulation point, infinitely many accumulation points [S025 TR pp. 4–12]. |
| Minimal evidence | Closed-form iterates per cycle proved by induction [S025 TR pp. 6–12]; the journal's six examples unread; ADS credits it with showing a rational τ is necessary [S129 p. 11]. |
| Abandoned paths | No repair in the report; repairs came later [S002 pp. 9–12; S011 p. 15]. |
| Reception | The device recurs in [S020 pp. 13–15; S007 pp. 19–21; S138 p. 4]. |
| Methods shown | Method 3 |

## Research Anti-patterns

| Anti-pattern | Record against it (full rows: ledger `#anti-patterns`) | Do instead |
|---|---|---|
| A crashing simulator wrapped in a large finite penalty for a smooth or model-based solver | Failures are tagged, not penalized [S019 pp. 48, 53]; ⚠ a high value is fine when the algorithm reads the jump [S090 p. 22] | Tag failures; bound out failure regions; EB for must-hold constraints |
| Treating all constraints alike | [S007 pp. 2–4; S072 pp. 5, 7] | Classify outputs first (Method 2) |
| Putting a heuristic in charge with no convergence backbone | [S133 pp. 1, 3; S027 pp. 14–16] | Heuristic as Search, poll as safety net (Method 1) |
| Convergence claims with unstated stationarity or hypotheses | [S002 p. 12; S025 TR; S138] | Guarantee ladder plus counterexamples (Method 3) |
| Accuracy-only or final-value comparisons with unequal budgets | [S128 pp. 4–16; S175 p. 11] | Profiles at equal evaluation budgets (Method 5) |
| Using DFO for convex, smooth-cheap or large-n problems | "NOMAD is not the solution that you should use" [S019 p. 11] | Derivative-based or structure-exploiting methods |
| Tuning many solver parameters at once | [S019 p. 74; S125 pp. 14–17] | One change at a time, at equal budget (Workflow B) |
| Application problem kept private after the paper | [S007 p. 31; S071]; ⚠ most partner problems were not released (Method 4) | Release an executable, a surrogate, or a scaled-down public twin [D006 pp. 4, 6, 22] |
| A fresh convergence proof for every variant | [S006 pp. 1, 14; S129 pp. 16–19] | Prove instance membership (Method 7) |
| A ranking surrogate chosen by fit error | [S046 pp. 13–15] | Judge it by order error (Heuristic 3) |
| Cross-code comparisons before a controlled one, or all effort counted as one "evaluation" | [S172 pp. 16–20; S128 p. 15] | Method 5, steps 1 and 3 |
| Tuning and reporting on the same problems | [S057 p. 18; S095 p. 9] | Held-out split (Heuristic 7) |
| Unchecked inherited benchmark instances | [S015 pp. 7–9; S028 p. 14] | Audit instances (Workflow D, step 3) |

## Research Trajectory

| Period | Main direction | Trigger (inferred unless sourced) | Representative work |
|---|---|---|---|
| 1994–1998 (✗ first pass: 1997–2002) | Exact global optimization: a thesis linking structured classes (mixed 0–1, disjoint bilinear, concave QP, bilevel, linear maxmin) by proven reformulations; enumeration of game equilibria | GERAD school; PhD at Polytechnique Montréal, November 1997, directed by B. Jaumard and G. Savard [S070 pp. 1–3, 33, 174] | Thesis [S070]; JOTA 1997 (10.1023/A:1022645805569); Math. Prog. 1999 [S041] |
| 1998–2004 (parallel) | Exact QCQP, pooling and fractional programming continue after the move to DFO | Rice CRPC reports; industry funding (Ultramar Canada) [S010 pp. 1–2; S015 p. 15] | Math. Prog. 2000 [S010]; Management Sci. 2004 [S015]; [S098] |
| Nov 1998–2002 (✗ first pass: ~2000–2002) | Move to derivative-free pattern search: tightness report, mixed variables, GPS analysis | NSERC postdoctoral fellowship at Rice with Dennis [S025 TR p. 2]; AFOSR/Boeing/ExxonMobil surrogate project [D016 pp. 1–5]; aerospace surrogate work (AIAA 2000) | Rice TR 1998 [S025]; SIAM J. Optim. 2001 [S011]; SIAM J. Optim. 2002/2003 [S002]; AIAA 2000 |
| 2003–2009 | Theory building: filter, MADS, second order, OrthoMADS, PSD-MADS, BiMADS, progressive barrier | The fixed-direction limitation of GPS, stated [D016 p. 4; S005 pp. 1–2; S001 p. 1]; NOMAD 1–3 with AFOSR/ExxonMobil funding | SIAM J. Optim. 2004, 2006, 2009 [S005; S001; S020; S006; S027; S007] |
| 1997–2022 (parallel; ✗ first pass: 2002–2013) | Extremal small polygons and other exact mathematics, a side line: from Graham's octagon in the thesis to certified results in 2022 | Taste for exact, certified answers | [S070 pp. 166–171]; JCTA 2002 [S037]; DCG 2009, 2013; [S113; S142; D003] |
| 1998–2014 (parallel) | Enumeration and refinement of game equilibria | GERAD school with Hansen | [S048; S076; D002; S134] |
| 2010–2016 | Applications and practical MADS (scaling, poll reduction to n+1 points, equalities, parallelism, tuning) | NOMAD 3 adoption; industrial partners (Hydro-Québec, Rio Tinto), who are named coauthors, not only funders [S074; S204; S032] | OMS 2012; SIAM J. Optim. 2014 [S038]; survey 2014 [S023]; [S064; S061; S057; S059; S066] |
| 2017–2022 | Consolidation: textbook, noise, surrogates judged by order error, hidden constraints and discontinuities, multiobjective indicators, NOMAD 4 | New funders (Huawei, Rio Tinto, Hydro-Québec, IVADO); ML demand | Springer 2017; [S046; S068; S114; S053; S084; S072; S090; S138; S004; S021] |
| 2023–2026 | Mixed/categorical variables, benchmarks as outputs (five benchmark or benchmarking works in two years), multi-fidelity, equalities, mesh-free ADS, covering and partition theory, bilevel DFO | Energy-systems grants; new co-lead Diouane [S121; S129; S156; S157; S158; S172] | ORF 2023; Optim. Eng. 2024/25 [S071]; [S130; S175; D006; S128; S156; S121; S157; S158; S112; S173; S129; S172; S137; S155] |

**What stayed constant**: the Clarke-calculus ladder, 1998–2026 [S002 p. 12; S158 pp. 16–18]; theory by membership (Method 7); constraint semantics [S007 p. 2; S173 p. 5]; STYRENE, released 2009 and run again in 2026 [S172 p. 18].

**What moved**: the counterexample craft, from GPS theory to toys, instruments and referees [S129; S004; S156]; the currency, from CPU time to evaluations to weighted effort [S015; S128; S155].

### Latest

Twelve months to 2026-09-27, verified via bibliography and/or search; card ids mark works read in full (full entries: `references/research/09-evidence-ledger.md#trajectory`):
- Audet & Hare, *Derivative-Free and Blackbox Optimization*, **2nd edition** (Springer, June 2026, 10.1007/978-3-032-00906-7), front matter read [B001] (k01; before, abstract-level only [D005]): benchmarking promoted from a 2017 appendix to Chapter 4, five real test problems with software, class-tested in 2025 [B001 pp. 9, 12, 16–17, 19–21]; chapters unread.
- **ADS-PB** (arXiv 2607.05183) [S172], after ADS (arXiv 2507.23054) [S129]; **Mads-PIP** (arXiv 2601.20811) [S158], with EQPB in NOMAD "Since version 4.6".
- Multi-fidelity constraints (arXiv 2601.06321) [S173]; surrogate-based categorical neighborhoods (arXiv 2603.27839) [S157]; CatMADS (arXiv 2506.06937) [S121].
- Bilevel DFO benchmarking (arXiv 2605.30531) [S156]; benchmarking summary (Opt. Lett. 2026, 10.1007/s11590-026-02302-z) [S128]; partitioned optimization (JOTA 2026, 10.1007/s10957-026-03042-x) [S155].
- Micro-PRIAD v1.0 (Aug 2026), a stochastic power-utility maintenance benchmark (https://github.com/bbopt/Micro-PRIAD) [D006].

## Academic Lineage

Joint-work counts are distinct non-talk entries of `works.json` (186 entries); full entries: `references/research/09-evidence-ledger.md#lineage`.
- **Upstream**: the GERAD global-optimization school; PhD, Polytechnique Montréal, November 1997, directed by B. Jaumard and G. Savard [S070 pp. 1–3]. J.E. Dennis Jr. at Rice: NSERC postdoc from 1998 [S025 TR p. 2], AFOSR co-PI 2000–2003 [D016]; 21 joint works, 1999–2012.
- **Peers and co-leads**: S. Le Digabel (54 joint works; NOMAD co-lead), C. Tribes (NOMAD research software engineer; 19), V. Rochon Montplaisir, W. Hare (textbook; [S128]), M. Kokkolaras, D. Orban, F. Messine, Y. Diouane (2024– [S092]).
- **Cross-lens collaborations**: A.R. Conn (PBTR, 2018 [S063]); A.L. Custódio (2008 erratum [D001]; feedback on the 2nd edition's biobjective chapter [B001 p. 12]); L.N. Vicente (2004 special-issue co-editor [D012, metadata]).
- **Downstream** (supervision not verified unless cited): M. A. Abramson (Rice PhD 2002, committee co-chaired by Audet [S213 pp. 1, 5]); PhDs Le Digabel, Peyrega, Amaioua, Dzahini, Lakhmiri, Salomon; student-led late papers [S121 p. 1; S158 p. 1; S173 p. 1].

## Inner Tensions

Full text of each tension: `references/research/09-evidence-ledger.md#tensions`.
- **Tension: theoretical purity vs pragmatic tuning.** Proofs are audited with counterexamples, yet NOMAD's defaults are a "compromise" tuned on benchmarks [S019 pp. 73–74]. Theory lives in the Poll, pragmatism in the Search and parameters; say which layer a recommendation comes from.
- **Tension: blackbox doctrine vs structure exploitation.** The group increasingly exploits structure: linear equalities [S064], grey boxes [S143], multi-fidelity [S173], nested splits [S151 pp. 3–5].
- **Tension: the mesh as foundation vs the mesh as limitation.** ADS replaces the MADS mesh with a "punctured space" [S129 p. 1] and proves OrthoMADS an instance of it [S129 pp. 16–19]. In 2005 the MADS authors called using the mesh or not "a matter of taste", untried without it on real problems [S077 p. 4].
- **Tension: small-n niche vs pressure to scale.** NOMAD is for "a small number of variables" [S019 p. 11]; PSD-MADS and partitioned reformulations [S155 pp. 19–20] push beyond.
- **Tension: auditing others vs being audited.** A counterexample for a peer's theorem [S138]; a proof erratum for the group's own flagship [D001 p. 1]. Audit this lens the same way.
- **Tension: public benchmarks vs partner problems.** Most partner blackboxes read were not released [S013 pp. 2–10; S084 pp. 24–26].
- **Tension: "cross-community" stated vs same-solver comparisons practiced.** Most algorithm papers compare inside NOMAD [S128 pp. 5, 9].

## Mentor Voice (optional)

Use only when the user asks. No recordings or interviews were found, so this voice is **constructed from documented practice, not quotes**. First-person teaching and advice appear only in co-authored texts (e.g., the textbook prefaces with Hare [B001 pp. 9–17]; advice to researchers with Abramson and Dennis [S077 pp. 2, 12]); a student's acknowledgment [S213 p. 5] is not Audet's voice either (✗ k01: before, "no first-person teaching or feedback material"; `references/research/09-evidence-ledger.md#mentor-voice`).
- Style (constructed): concrete; starts from the problem, not the method. Asks about failures before asking about gradients.
- Typical questions (constructed): "What does one evaluation cost, and how many can you afford?" "What happens when the simulation fails?" "Which of these constraints can be violated during the search?" "Which step of your algorithm carries the proof?" "Can you break this hypothesis in two dimensions?" "At equal numbers of evaluations, who wins?"
- Avoid: grand claims about "global optimality" for blackboxes; dismissing heuristics or models outright (the record absorbs them instead).

## Roundtable Card

- **Lens (one line)**: Expensive, unreliable simulators are blackboxes. Classify constraints first, let heuristics and models propose (or order) points in a free Search step, let a dense-direction Poll carry the guarantee, and judge everything at equal evaluation budgets on real engineering problems.
- **Leads when**: evaluations are expensive (seconds to days); outputs are nonsmooth, noisy or discontinuous; the simulator crashes (hidden constraints); constraints mix unrelaxable and relaxable types; variables are integer, granular or categorical; n is small to moderate; an off-the-shelf solver is needed.
- **First questions asked**: (1) Cost per evaluation and total budget? (2) Where does the simulation fail, and does the same input give the same output? (3) Per output: objective, unrelaxable, relaxable, or equality, and which can be checked before the simulation? (4) Variable types, bounds, n; for categorical variables, what counts as a neighbour? (5) A cheaper surrogate or fidelity, and a feasible starting point?
- **Default recommendation**: **NOMAD 4** (MADS; https://github.com/bbopt/nomad, ACM TOMS 2022), outputs typed `OBJ`/`EB`/`PB` (`CSTR` if unsure), `EQPB` with **Mads-PIP** for equalities; default quadratic models; an LH search if there is no feasible x0; **PSD-MADS** or fixed variables for larger n; **DMultiMads** for multiobjective problems. Noise: adaptive precision if more samples reduce it [S084], otherwise **StoMADS** (NOMAD 3 / MATLAB) or replications. Why: guarantees for nonsmooth constrained blackboxes plus explicit handling of failures and constraint types.
- **Will push back on**: finite-difference gradients through a noisy or crashing simulator; one penalty for every constraint; heuristics with no convergence backbone; convergence claims with unspecified stationarity or untested hypotheses; surrogates chosen by fit error; comparisons without equal evaluation budgets or with only analytic test functions; DFO on convex, cheap-smooth or large-n problems. Shared with the Conn lens: prefer membership in a proved framework to a fresh proof.
- **Likely disagreements** (methodological, publication-based):
  - vs **Powell**: Powell lets interpolation models drive every step. In the MADS line, models mostly propose or order points; when they enter the Poll (the default (n+1)th direction [S019 pp. 55, 83]; CatMADS neighbourhoods [S121 p. 6]), the papers show that the guarantees are kept. The PBTR authors (with Conn) write: "Given a very badly behaved function we would use a direct-search method. If the function can be adequately approximated by a smooth function we would prefer a model-based approach [...]" [S063 p. 2]. The textbook states the same split: direct search even for nonsmooth functions, model-based methods when the objective is expected to be smooth [B001 pp. 15–16]. The disagreement centres on nonsmooth, failing and noisy blackboxes.
  - vs **Conn**: shared ground (joint 2018 papers; framework proofs). The difference is where model quality sits: the engine of a trust-region step (Conn), or a proposal generator with the Poll as the guarantee (Audet). The PB was transplanted into a trust-region framework with retuned parameters [S063 pp. 10–14, 20–22].
  - vs **Scheinberg**: shared ground, verified: StoMADS imports that line's probabilistic-estimate devices, attributed per definition and lemma [S053 pp. 2–4, 12]. *(Inference; no direct exchange found)*: StoMADS keeps dense directions and asymptotic, probability-one Clarke stationarity, where a complexity-oriented lens would ask for expected iteration bounds.
  - vs **Vicente**: globalization. The 2025 ADS paper contrasts mesh plus simple decrease (MADS), sufficient decrease (SDDS) and punctured space (ADS), with a 1-D example exposing each rival family's weakness [S129 pp. 5–6]; a 2024 counterexample to a Vicente–Custódio (2012) theorem located the false step and gave a repair [S138 pp. 2–9]. Relations are collaborative.
- **Blind spots**: high-dimensional or cheap smooth problems; worst-case complexity; Bayesian optimization (only as Search machinery [S099]); categorical variables with noise; misclassified constraints; reliance on a large software team.

## Honest Boundary

This skill was built from public information and has these limits (clauses marked k01 changed with the book-material batch; earlier wording: `references/research/09-evidence-ledger.md#honest-boundary`):
- **Coverage.** First pass: web-search snippets, the group BibTeX file and the NOMAD user-guide sources on GitHub (publisher, arXiv, SIAM, ACM, GERAD, dblp and OpenAlex hosts were blocked then). Full-text pass (2026-09-27): of 213 listed works (196 Scholar + 17 others), 109 were read in full, 7 in part (including the textbook's front matter [B001]; B001 is the front matter of D005, and the book appears in both rows) and 2 were unreadable as named (S025, read via its 1998 precursor report; S067); 56 are known only from abstracts and 20 from metadata; 19 talks, duplicates and junk rows were skipped (`references/research/07-paper-cards.md`). Guide sentences are collectively authored and cannot be attributed to Audet alone; the two Search/Poll sentences have a 2005 named-author source, co-authored with Abramson and Dennis [S077 pp. 4–5].
- **Key works still unread (no open full text).** (⚠ k01: narrowed from the whole textbook.) The textbook bodies, first and second editions [S003; D005]: only the 2nd edition's front matter (foreword, both prefaces, table of contents; 22 pages) was read [B001], so chapter content is known from titles only and the accuracy-profile warning still comes from a secondary quotation; VNS search [S009], poll reduction to n+1 points [S038], mesh-based Nelder–Mead [S043], Robust-MADS [S055], BiMADS and MultiMads [S018; S026], MV-MADS [S017], globalization strategies [S024], granular variables [S033], the COCO study [S141], the AIAA 2000 surrogate paper [S008] and the NOMAD project record [S012]. The 2004 tightness article was read only through its 1998 precursor report [S025], so "six counterexamples" is unverified. Claims about these works rest on abstracts.
- **Version dependence.** Many texts read are preprints or reports (StoMADS arXiv v1 [S053], NOMAD 4 arXiv v2 [S021], the 2012 GERAD survey [S023], the 3.7.2 guide [S019], arXiv versions of most 2022–2026 papers). Test sets, pages and details may differ in the published versions (e.g., StoMADS's test problems [S053 p. 21]).
- **Thin early period.** 1994–1999 is read in full only through the thesis [S070] and, via OCR, the 1998 Rice report [S025]; six of its eight cards are abstract-level, so reformulation-era claims rest mainly on S070 and S050.
- **Tacit-knowledge gap.** No interview, lecture transcript or student recollection was found. (✗ k01: before, "the full texts contain no first-person teaching material".) First-person teaching material exists only co-authored (e.g., textbook prefaces with Hare [B001 pp. 9–17]; advice to researchers with Abramson and Dennis [S077 pp. 2, 12]); acknowledgments add little [S213 p. 5]. How Audet chooses topics, gives feedback, crafts counterexamples, or splits supervision with Le Digabel cannot be distilled. Mentorship patterns are inferred from co-authorship, except Abramson's co-chaired thesis [S213 p. 1]; Audet's own advisors are verified [S070 p. 3].
- **Era and resource limits.** Methods 4 and 6 rely on a 25-year software line, a research software engineer, and industrial and defense funding. An individual researcher should adopt NOMAD and the bbopt benchmarks rather than replicate that infrastructure.
- **Stated-but-thinly-verified items.** The accuracy-profile warning comes via a citing author's quotation (✗ k01: the textbook's stated goal, once known only from a reviewer's quotation, is now read in its preface [B001 p. 13]). Several NOMAD 4 documentation quotes are not in the 3.7.2 guide read [S019] and rest on the GitHub guide sources (`references/sources/software/nomad-and-bbopt-notes.md`): the epigraph's first sentence; the Search "constrained by the theory to return points on the underlying mesh"; CSTR "corresponds"; EQPB "not very good" in Mads-PB and "Since version 4.6"; "Try Mads-PIP or ADS algorithms"; the release-notes parity sentence (the Search, CSTR, EQPB-in-Mads-PB and parity quotes, and the accuracy-profile warning, are now quoted only in `references/research/09-evidence-ledger.md` #method-1, #method-2, #method-5, #signature-work-3). The MADS erratum, the 2026 benchmarking summary and *Two decades of blackbox optimization applications*, unread in the first pass, are now read [D001; S128; S013].
- **Method 7's exclusivity is moderate.** It passes the exclusivity check only through three devices (re-hosting one's own flagship in the successor framework, eventually-static adaptation, the plug-in contract); its framework-proof and collapse-check steps are shared with the Conn and Vicente lenses.
- **Roundtable disagreement with Scheinberg is still partly inferred.** The shared probabilistic-estimate ground is verified [S053 pp. 2–4, 12]; the disagreement over expected-iteration bounds is inferred from problem framing, and no direct exchange of papers was found.
- **Weighting.** Collaborations Audet did not lead (S022†, S174†, S160†) and Abramson's thesis (S213) never carry a claim alone. S140 was read only in part, so the complexity statement rests on its theorem statements.
- **Unverified facts.** The affiliations of some industry co-authors; the authorship of the stochastic progressive-barrier Math. Program. paper (not on Audet's Scholar list); formal supervision roles other than Abramson's. See ⚠️ rows in `references/sources/RESOURCES.md`.
- **Research date: 2026-09-27.** Later papers, NOMAD releases and the full content of the 2nd edition are not covered.

## Corrections from the full texts

First-pass errors fixed by the full-text reading; every original line, verbatim: `references/research/09-evidence-ledger.md#corrections`. Most are marked ✗ inline (Methods 1, 3, 5, 6; the PB and GPS-tightness anatomies; the trajectory table). The rest:
- ✗ Method 1, step 4 was inverted (first pass: "the idea belongs in the Search, not the Poll").
- ✗ Heuristic 9: "a convergence backbone", not "the direct-search backbone" [S150; S140].
- ✗ Tensions: audits in 1998, 2002, 2024 (not 2003, 2004, 2024); Audet co-authored MADS, not "the founder of the mesh idea".
- ✗ Lineage: first joint work with Diouane 2024, not 2023 [S092]; counts from `works.json` (Dennis 21, Le Digabel 54; BibTeX gave 18, 48); advisors verified [S070 pp. 1–3].

## Sources (appendix)

Research files: `references/research/01-publications.md` … `06-trajectory.md`; resource table: `references/sources/RESOURCES.md` (54 rows); publication extract: `references/sources/publications/audet-publications-bbopt-bib.md`.

Deep reading (2026-09-27): publication list `references/sources/publications/scholar.md` (+ `works.json`; Google Scholar profile https://scholar.google.com/citations?user=WuHBdIkAAAAJ); full-text index `references/sources/papers/INDEX.md` (texts git-ignored); paper-card index `references/research/07-paper-cards.md` (194 cards in `references/research/cards/`); synthesis `references/research/08-deep-reading-synthesis.md`; techniques `references/technique-catalog.md`. Evidence ledger (full evidence per SKILL.md item, and the text of every condensed item before tightening): `references/research/09-evidence-ledger.md`.

### Papers (primary)
- Audet, Dennis. Analysis of generalized pattern searches. SIAM J. Optim. 13, 2003. https://doi.org/10.1137/S1052623400378742
- Audet. Convergence results for generalized pattern search algorithms are tight. Optim. Eng. 5, 2004. https://doi.org/10.1023/B:OPTE.0000033370.66768.a9
- Audet, Dennis. Mesh adaptive direct search algorithms for constrained optimization. SIAM J. Optim. 17(1), 2006. https://doi.org/10.1137/040603371
- Audet, Dennis. A progressive barrier for derivative-free nonlinear programming. SIAM J. Optim. 20(1), 2009. https://doi.org/10.1137/070692662
- Abramson, Audet, Dennis, Le Digabel. OrthoMADS. SIAM J. Optim. 20(2), 2009. https://doi.org/10.1137/080716980
- Audet, Orban. Finding optimal algorithmic parameters using derivative-free optimization. SIAM J. Optim. 17(3), 2006. https://doi.org/10.1137/040620886
- Audet, Conn, Le Digabel, Peyrega. A progressive barrier derivative-free trust-region algorithm. COAP 71, 2018. https://doi.org/10.1007/s10589-018-0020-4
- Audet, Dzahini, Kokkolaras, Le Digabel. StoMADS. COAP 79, 2021. https://doi.org/10.1007/s10589-020-00249-0
- Audet, Le Digabel, Rochon Montplaisir, Tribes. Algorithm 1027: NOMAD version 4. ACM TOMS 48(3), 2022. https://doi.org/10.1145/3544489
- Audet, Bouchet, Bourdin. Counterexample and an additional revealing poll step… Math. Program. 208, 2024. https://doi.org/10.1007/s10107-023-02042-3
- Abramson, Audet, Dennis. Nonlinear programming by mesh adaptive direct searches. 2005 report. https://doi.org/10.21236/ada444692 [S077]
- Andrés-Thiò, Audet, et al. solar: a solar thermal power plant simulator for blackbox optimization benchmarking. Optim. Eng., 2024/25. https://doi.org/10.1007/s11081-024-09952-x
- Audet, Denorme, Diouane, Le Digabel, Tribes. Adaptive direct search algorithms for constrained optimization (2025), arXiv:2507.23054; …with relaxable and quantifiable constraints (2026), arXiv:2607.05183

### Stated methodology (primary)
- Audet, Hare. Derivative-Free and Blackbox Optimization. Springer 2017 (https://doi.org/10.1007/978-3-319-68913-5); 2nd ed. 2026 (https://doi.org/10.1007/978-3-032-00906-7); front matter of the 2nd ed. read (https://www.gerad.ca/Charles.Audet/PUB/FrontMatter.pdf) [B001]
- Audet. A survey on direct search methods for blackbox optimization and their applications. Springer 2014. https://doi.org/10.1007/978-1-4939-1124-0_2
- Audet, Kokkolaras. Blackbox and derivative-free optimization: theory, algorithms and applications (editorial). Optim. Eng. 17, 2016. https://doi.org/10.1007/s11081-016-9307-4
- NOMAD 4 user guide sources (Introduction, TricksOfTheTrade, HowToUseNomad, ReleaseNotes). https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst

### Process evidence (primary)
- bbopt GitHub organisation (NOMAD, STYRENE, SOLAR, AIRCRAFT_RANGE, Cat-Suite, RunnerPost, StoMADS, Micro-PRIAD). https://github.com/bbopt
- Group bibliography bibliography.bib (151 Audet entries). https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib
- Audet, Le Digabel, Salomon, Tribes. NOMAD on the COCO constrained test suite. GECCO Companion 2022. https://doi.org/10.1145/3520304.3534019
- Alarie, Audet, Gheribi, Kokkolaras, Le Digabel. Two decades of blackbox optimization applications. EURO J. Comput. Optim. 9, 2021. https://doi.org/10.1016/j.ejco.2021.100011

### Others (secondary)
- GERAD profile of Charles Audet. https://www.gerad.ca/en/people/charles-audet
- Kokkolaras, review of Audet & Hare, Optim. Eng. 20, 2019 (co-author, not independent). https://doi.org/10.1007/s11081-019-09422-9
- Le Digabel, Wild. A taxonomy of constraints in black-box simulation-based optimization. Optim. Eng. 25(2), 2024. https://doi.org/10.1007/s11081-023-09839-3
- Dzahini, Rinaldi, Royer, Zeffiro. Direct-search methods in the year 2025: theoretical guarantees and algorithmic paradigms. arXiv:2403.05322
- Le Digabel. Algorithm 909: NOMAD. ACM TOMS 37(4), 2011. https://doi.org/10.1145/1916461.1916468

---
> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
