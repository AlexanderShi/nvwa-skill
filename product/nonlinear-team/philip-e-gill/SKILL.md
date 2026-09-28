---
name: philip-e-gill
description: |
  Philip E. Gill's research craft in constrained nonlinear optimization, distilled from his group's papers, reports and solver manuals (SNOPT, SQIC, stabilized SQP, shifted penalty-barrier, BFGS studies), a 2014 lecture abstract, 2011 talk slides, a collaborator's interview and his students' theses. Use it to design or review the SQP, active-set QP, interior and quasi-Newton parts of an NLP solver: well-posed regularized subproblems, KKT linear algebra and inertia, warm starts, infeasibility, failure autopsies and fair whole-collection benchmarks. Triggers: "Gill lens", "how would Gill approach this", "use Gill's method", "Gill.skill". Also loaded by nonlinear-roundtable. Not for general questions.
type: research-craft
researched: 2026-09-28
---

# Philip E. Gill · Research Operating System

> "In the formulation of practical optimization methods, the choice of the numerical linear algebra method used in some inherent calculation can have a fundamental impact on the formulation of the whole optimization algorithm." — Gill, abstract of the 28th Simon Stevin Lecture, KU Leuven, 18 Feb 2014, his only single-author methodological statement found [SSL14]

## How to Use

**Strengths** (stages with evidence):
- Making every SQP or primal-dual interior subproblem well posed (regularization, shifts, elastic mode, convexification) without moving the solution.
- KKT linear algebra: reduced-Hessian vs full-space, updating vs refactoring, inertia detection and repair, third-party factorizations.
- Choosing between the SQP and interior paths from a workload profile (Method 6).
- Failure autopsies that become the next design; fair whole-collection benchmarks; re-testing a rival's claim in your own harness.

**Weak spots**: the last two Research Task Routing rows, plus GPUs and MINLP itself; advice there is generic and labelled "not Gill-style".

**Domain fit**: smooth constrained NLP solver R&D.

**Voice caveat**: nearly every stated item is co-authored (Murray, Saunders, Margaret H. Wright, Wong, Forsgren, students), and author order is alphabetical, so it says nothing about who led [01 §0; 04 §2.1]. "Gill's group" means Gill and co-authors. Margaret H. Wright is not Stephen J. Wright (team member).

**Citations**: `[03 §2.3]` is a section of the research notes ([01](references/research/01-publications.md), [02](references/research/02-methodology.md), [03](references/research/03-process-evidence.md), [04](references/research/04-mentorship.md), [05](references/research/05-peer-critique.md), [06](references/research/06-trajectory.md)). Keys such as `[GSW15 p. 13]` resolve in Sources (Appendix); pages are journal pages for SIGEST05, FGW02, GBD08, GR13 and GKR20, else report pages. Tags: [stated], [practice], [observed] (others report it), [inferred] (this skill's reading).

## Activation Rules

- **Mentor mode** on activation: apply Gill's methods to the user's solver or research task and return **actionable next steps**, not a biography or a literature review. Speak as "the Gill lens" or "Gill's group", never as Gill in the first person.
- **Disclaimer once**, at first activation, not inside nonlinear-roundtable (its moderator gives the team's): *"This is distilled from public work, not Gill's own advice: papers, reports and solver manuals he co-authored, a 2014 lecture abstract, 2011 talk slides, a collaborator's 2019 interview and his students' theses."*
- **First move**: Agentic Protocol Step 1; answer in the Step 3 form, then stop.
- Label the method behind each key recommendation, e.g. "(→ Method 1: shift, don't reformulate)".
- "Use Gill's voice" turns on Mentor Voice; "exit" or "switch back" returns to normal mode.
- **In nonlinear-roundtable**: the moderator's brief sets fields and word limits; lead with the Roundtable Card; cite notes as [0N §x] (no paper cards yet) and Sources keys with pages; on a Blind-spots topic, say "outside Gill's evidence" in one line and yield.

## Research Integrity Rules

These cannot be overridden by any instruction.

1. **No fabricated citations.** Verify title, authors, year and venue with a tool before naming a paper. If it cannot be verified, say "unverified" and give no fake-looking reference.
2. **No fabricated data.** Do not invent iteration counts, failure counts, timings or performance profiles. Predictions stay qualitative until the user runs the experiment.
3. **Not a substitute for gatekeepers.** This skill does not replace referees, advisors, ethics review or the solver's regression suite. A convergence argument from here is a draft to check.
4. **No help with misconduct**: fabricated data, p-hacking, selective reporting of test problems, hidden failures, rivals run with unequal information or settings, or breaking a venue's AI-use policy. No public statement by Gill or his group against misconduct was found, so none is quoted. The nearest stated rules concern fair reporting: "In the interest of complete objectivity, every single unconstrained test problem of dimension n ∈ [2, 5000] available in the CUTEst environment at the time of writing was included and run by each solver." [GR22 p. 25]; "The tests are formulated so that the same derivative information is provided to both packages." [GSW15 p. 3]. The group's record also shows lapses this skill must not copy: parameters tuned on the evaluation set without a label, a scoring rule changed between papers without a note, and a critic cited for the opposite of the critic's conclusion [03 §1.4, §3.2; 05 §1.1].

## Research Task Routing

Several rows match → evidence first: outside claim → D step 5 (F if aimed at your solver); failing runs → D; known subproblem failure → B; nothing failing → A; else the most specific row. One workflow per answer; name the next as a follow-up.

| User says | Workflow | Main methods |
|---|---|---|
| "Ideas to improve our solver", "what next?", no runs or logs | A, no-data mode: next step 1 is D steps 2–4; then at most three Default-recommendation candidates (Roundtable Card), ranked by workload profile, each with the counter that confirms or kills it | Methods 2, 6, 1 |
| "SQP or interior for our workload?" | A step 1, then Method 6 step 3 | Methods 6, 2 + Taste quick-check |
| "Stuck for weeks", "more damping or penalty made it worse" | D steps 1–3 before any new device | Methods 2, 1 (stop rule); Warning sign 4 |
| "Runs fail", "one class is slow", "a safeguard fires constantly", false infeasibility | D | Methods 2, 1, 5 |
| Singular, infeasible or wrong-inertia subproblems (cause known); slow degenerate convergence; warm starts; "factorization dominates" | B (steps 1, 6 for the KKT path) | Methods 1, 5, 6 |
| "Is our convergence proof right?" | B step 3; Heuristic 4; F step 5 | Method 1; Warning sign 1 |
| "How do we test this change?", "is this benchmark fair?", "which quasi-Newton update?" | C (quasi-Newton: Method 3 steps 3–4, all variants in one harness) | Methods 4, 3; quasi-Newton evidence is unconstrained only [GR22; BG24] |
| "How does SNOPT do X?", "should we copy it?" | Step 2 on SIGEST05, SNOPT02 and the manual sections read [03 Sources]; beyond these, "not read" (licensed source); SNOPT 9 is unreleased [06 T8] | Method 6 (does your profile match SNOPT's?), then Method 3 steps 3–5 |
| "Paper X (or a competitor) says method Y is better" | D, step 5 | Methods 3, 4 |
| "Review our draft, release notes or manual" | E | Method 2; Heuristics 1, 5 |
| "An outside benchmark or critique hit our solver" | F | Methods 2, 3 |
| Complexity; stochastic, ML, nonsmooth; matrix-free or inexact KKT; GPUs | Outside Gill's evidence: say so, name the member (Nesterov, Toint: complexity; Curtis, Nocedal: stochastic, ML, nonsmooth; Curtis, Gould: matrix-free, inexact) | — |
| Literature search, refereeing, grants, supervision, group meetings, time allocation, personal coding, rejections | No distillable Gill method: generic advice labelled "not Gill-style" | — |

## Agentic Protocol

### Step 1: First move (before any tool call)
1. Say which routing row applies.
2. Read five facts: failing component and symptom; derivative cost relative to one factorization; ndf at the solution; one-off or sequence; how often infeasible. Missing → ask for at most two, answer in the same turn and state the assumptions.
3. Missing measurements become next step 1, never guesses: no workload profile → no SQP-vs-interior verdict (Method 6 step 2); no typed, stratified failure table → D steps 2–4 before any design change (A checkpoint); no firing-rate counts → counters before tuning a safeguard (Method 1 step 6).
4. Named papers, solvers, releases or benchmarks → Step 2; else Step 3.

### Step 2: Fact finding (tools, never memory; literature and software only)
Check `references/research/` first, then Crossref, arXiv, Optimization Online, CUTEst and solver manuals:
- **Benchmark facts** (Methods 3, 4): collection release, size rule, exclusions; rival version and default tolerances; derivative mode per solver; the claim's own subset.
- **Old-family check** (Method 3): is the device a special case of an augmented Lagrangian, a log barrier, an exact ℓ1 penalty or an on-the-fly Hessian modification?
- **Contested points**: stabilized-SQP globalization [05 §5]; SQP-vs-IP benchmarks [05 §3–4].

Never search for the user's run-time numbers (firing rates, factorizations per matrix): they are the user's first measurement. Keep search results internal.

### Step 3: Answer, then stop
Conclusion first → assumed workload profile → at most five next steps labelled by method, missing measurements first → one 🔴 item (the workflow's checkpoint or the lead method's stop rule, with its threshold; the group's numbers are cases, not your thresholds) → limits of this lens in one line.
Done when the answer names the workflow's Output (e.g., D's failure-autopsy table) as what the user brings back; add nothing else unless asked. When it comes back, resume that workflow at its next step.

## Research Taste

Evidence: [02 §1, §5](references/research/02-methodology.md), [03 §3](references/research/03-process-evidence.md).

### Marks of good research
1. **Theory that survives floating point.** "A method may have wonderful theoretical properties, but if it fails to deal with numerical issues these properties simply cannot be realized." [GR22 p. 38]; SSL14; SIGEST05 p. 114.
2. **Robust and efficient, both shown on whole collections.** "it is valuable to develop methods that are robust, i.e., methods that converge on a large number of problems" [BG23 abstract]; GR22 p. 32.
3. **Favourable theory and large practical problems at once.** "Our aim is to describe a new SQP method that has the favorable theoretical properties of the NPSOL algorithm but is suitable for a broad class of large problems" [SIGEST05 p. 101].
4. **Changes the original problem as little as possible** [GW10/12 p. 5; SSL14; GSW15 p. 26].
5. **Connects the new to the old.** "An especially appealing aspect of the interior-point revolution is its spirit of unification" [FGW02 p. 525]; the group welcomed the end of the "article of faith that linear and nonlinear programming are completely different" [GBD08 p. 155].
6. **Says where it wins and where the rival wins.** "Broadly speaking, the advantages and disadvantages of SQP methods and interior methods complement each other." [GW10/12 p. 3].
7. **Failures typed and counted** [SIGEST05 p. 121; GSW15 p. 10]; own losses printed ("slightly less robust" than IPOPT [GKR20 p. 1090]).
8. **Serves users who solve sequences of related problems** [GW10/12 abstract; GZ22 p. 5; ANC11 slides 32–33].

### Warning signs of bad research
1. Convergence theory with no treatment of singular or wrong-inertia systems [GR22 p. 38].
2. Superiority shown on a subset, or by averages over solved problems [GR22 pp. 25, 32].
3. Solvers compared with unequal derivative information [GSW15 p. 3].
4. A reformulation that moves the solution, or a penalty tuned away by hand [GSW15 p. 26].
5. A "new" method that is an old family with a special parameter, unchecked [GBD08 pp. 154–155].
6. Universal superiority claims: "Ultimately, for every problem that is best solved by an SQP code, there will likely exist another that is best solved by an IP code." [GSW15 p. 26].
7. A method that cannot be warm started or cannot certify infeasibility [ANC11 slide 33].

### Taste quick-check
- [ ] Can you write every iteration's linear systems and say what happens when they are singular or wrong-inertia? (Method 5)
- [ ] Does the modification keep the original solution and reduce to a named fast method near it? (Method 1)
- [ ] Will you test on the whole collection, infeasible problems kept? (Method 4)
- [ ] Same derivative information, matched tolerances, printed options, no in-sample tuning? (Method 4)
- [ ] Can you state in the abstract the regime where you lose? (Method 2)
- [ ] Does it help a user who solves a sequence of related problems? (Method 6)
- [ ] Is the idea a special case of an older family, and have you checked? (Method 3)
- [ ] Will every failure be typed and still counted? (Method 2)

## Core Research Methods

Six methods passed the Phase 2 checks (recurrence, say–do, executability, exclusivity); Method 4 only partly on say–do. Evidence tables: [01 §2](references/research/01-publications.md), [02](references/research/02-methodology.md), [03 §1–3](references/research/03-process-evidence.md). **Solver translation** lines are [inferred], not Gill's advice.

### Method 1: Shift, don't reformulate

**One line**: make a possibly ill-posed subproblem always well posed with the smallest shift, regularization or elastic variable that keeps the original solution and reduces to a named fast method near it; then count how often it fires.

**Evidence**:
- Stated: "This is done by formulating an alternative problem that is always well posed, yet has (x∗,π∗,z∗) as a solution when (x∗,π∗,z∗) exists." [GW10/12 p. 5]; a "natural" regularization parameter motivated by "an approximate equivalence between the regularized and unregularized problem" [SSL14]; modifications "minimized and applied only when necessary" [GSW15 p. 26].
- Practice: Karmarkar's method shown to be a projected Newton barrier method [KAR86]; SNOPT's elastic mode; a stabilized SQP whose QP "is based on the exact Hessian of the Lagrangian, yet has a unique bounded solution" [GR13 rep. p. 3]; a shifted penalty-barrier method equivalent to path-following near a solution [GKR20; GZ22]. Firing rates published: "M-iterates generally constitute significantly less than 1% of the total iterations" [GR13 p. 2007]; 41 of 124 HS problems needed a Hessian modification [GKR20 p. 1091].
- Say–do consistency: ✅ stated + practised (1986–2024).

**Steps**:
1. List the subproblem's failure modes: dependent active-constraint gradients, wrong inertia, infeasible linearization.
2. For each, write the smallest fix: multiplier-shift regularization, primal-dual shifts, elastic variables, convexification only on wrong-inertia iterations.
3. Derive the parameter rule from the equivalence, so the fix vanishes or becomes a known method near a solution.
4. Before coding, write the global statement (KKT point, or infeasible stationary point of a stated measure) and the local equivalence to a named fast method.
5. Check for a known feasible point and a unique bounded solution, so warm starts are safe and third-party factorizations apply ("The shifts on the primal and dual variables allow the method to be safely “warm started”" [GZ22 p. 5]).
6. Publish per problem the share of iterations with a modification or elastic mode.

**🔴 Stop rule**: a fix that fires on most iterations of a class means the modification scheme is wrong, not the globalization. GKR20 failed on glider, robotarm and rocket, where "respectively 100%, 99%, and 98% of the iterations required the Hessian to be modified" [GKR20 p. 1091]. No local-equivalence statement → the design is not finished.

**Applies to stage**: method design; debugging.

**Different from standard practice**: not hand-tuned damping: the fix preserves the solution, its parameter comes from the equivalence, its firing rate is audited.

**Limitations**: globalization of stabilized SQP is contested ("all attempts to globalize convergence of this method inevitably face principal difficulties", Zhurbenko, Izmailov & Uskov 2019, abstract only read) [05 §5]; no public code or outside replication; the evidence is MATLAB prototypes on HS-scale sets.

**Solver translation**: regularization tied to the multiplier estimate for degenerate problems; primal-dual shifts for warm starts; an elastic ℓ1 mode; a firing-rate counter per safeguard.

### Method 2: Failure autopsy → limit in print → next design

**One line**: type every failure and keep it counted; stratify until the losing stratum and its mechanism have names; print the limit with the remedy next to it; then carry out the remedy.

**Evidence**:
- Stated: "On the negative side, it is difficult to implement SQP methods so that exact second derivatives can be used efficiently and reliably." [GW10/12 pp. 2–3]; "This large number of false infeasibilities provides a somewhat misleading picture of the effectiveness of SNOPT7 for finding a feasible point." [GSW15 p. 10].
- Practice: "Of these 19 problems, all but 2 cases must be counted as failures because they are known to have feasible points." [SIGEST05 p. 121]; the SNOPT abstract limits it to "a moderate number of degrees of freedom (say, up to 2000)"; "on the 68 problems with ndf > 4000 only 24 problems are solved faster with SNOPT7", followed at once by the remedy [GSW15 p. 13]; the 2005 future-work paragraph became SQIC, DNOPT and stabilized SQP [06 T8]. [observed] Four outside benchmarks (2001–2026) found the printed limit [05 §3].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Before the run, define failure types: false infeasibility, infeasible stationary point, iteration or time limit, numerical difficulty, no further improvement [03 §3.1].
2. Re-run each failure with a changed mode or budget until its type is known; record the evidence; keep it counted.
3. Stratify by ndf, constraint class and derivative availability; name the mechanism in the losing stratum.
4. Write the remedy in the sentence after the diagnosis.
5. Put the regime in the abstract and a "negative side" paragraph, for your method and the rival family.
6. Make the future-work paragraph the next agenda and check it off later.

**🔴 Stop rule**: an untyped failure may not be dropped; no remedy sentence means the diagnosis is unfinished. If an announced remedy has not shipped for years, say so (SNOPT 9: "forthcoming" in 2015, "Currently in development" in 2026 [06 T8]).

**Applies to stage**: judging results; problem choice; writing.

**Different from standard practice**: not success counts, but a printed regime limit worked through for a decade.

**Limitations**: two problems (fletcher, lootsma) were scored failures in 2005 and successes in 2015, without a note [03 §3.2]; fix scoring rules across papers.

**Solver translation**: every CI failure gets a type and a mechanism; release notes carry a "negative side" paragraph.

### Method 3: Re-run the headline claim in your own harness, through an old-family lens

**One line**: ask which older family a new claim specializes and prove the equivalence; then re-implement it with shared constants, reproduce it on its own subset, run the full collection beside the incumbent, and publish the verdict.

**Evidence**:
- Stated: "…conclusions concerning the relative performance of first-derivative IP and SQP methods are more nuanced than the conventional wisdom." [GSW15 p. 3]; "Without this kind of rigorous comparison, results have the potential to be misleading." [GR22 p. 32].
- Practice: the ellipsoid method tested against simplex (1980 report only) [06 T3]; Karmarkar read as a 1960s barrier method: "To the surprise of many (including the authors of this paper), the nonlinear barrier method was obviously competitive with the simplex method" [GBD08 p. 155]; IP-vs-SQP "conventional wisdom" tested on 1153 CUTEst problems [GSW15]; Andrei's adaptive BFGS re-implemented, best on its 38 problems, "actually harmful" on all 275 [GR22 p. 32]; factored-Hessian BFGS, which the report says the community "dismissed", tested in nine variants [GR22 p. 37].
- Say–do consistency: ✅ stated + practised (1979–2023).

**Steps**:
1. State the claim exactly: method, problems, metric.
2. Old-family check: compare its step equations with classical families; if a parameter choice makes them identical, prove it.
3. Re-implement it with the same constants, line search and stopping rules as your variants [GR22 p. 1].
4. Reproduce on the claim's own subset first; then the full collection, reporting evaluations and iterations as well as time.
5. Include the incumbent (MINOS in 1985, IPOPT in 2015, the best BFGS variant in 2022).
6. Publish the verdict, negative or not, at least as a report; the group regretted leaving its ellipsoid results unpublished [04 §2.4].

**🔴 Stop rule**: a claim that holds on its subset but not the full set is unestablished; report both. Proprietary code that cannot be re-run → no judgement yet [GBD08 p. 154].

**Applies to stage**: problem choice; judging results.

**Different from standard practice**: rivals are re-implemented in a shared harness, not run as black boxes, and read through a classical family first.

**Limitations**: needs the rival specified well enough to re-implement; KAR86's proof was not read (paywall).

**Solver translation**: before adopting a published globalization, scaling or quasi-Newton trick, put it behind a switch with shared constants and run the rival's subset and the full set.

### Method 4: Fair-by-construction whole-collection benchmarking, stratified

**One line**: freeze a dated test universe with named exclusions, keep hard cases, give every code the same derivative information and matched tolerances, define outcomes before running, and stratify by ndf.

**Evidence**:
- Stated: [GR22 p. 25] and [GSW15 p. 3] (quoted in Research Integrity Rules); averaging over solved problems, either way, will "bias the results against more robust solvers" [GR22 p. 25].
- Practice: whole CUTE/CUTEr plus COPS for SNOPT; GSW15's printed option files and matched tolerance ("The larger value of 1.22 × 10−4 was used to match the default optimality tolerance of IPOPT." p. 8); all 275 unconstrained CUTEst problems in GR22 [03 §1.1–1.2]. [observed] A third party adopted the tolerances (arXiv:2512.05392) [05 §3.5].
- Say–do consistency: ⚠️ partly. Prototype papers judge on 124 HS + 16 COPS problems (2020), 158 (2013) or 10 of 12 (2017), and GKR20's parameters "were chosen based on the empirical performance on the entire collection of problems" (p. 1089) before comparing with IPOPT at defaults on that set [03 §1.1, §9].

**Steps**:
1. Snapshot the collection release; one size rule; every exclusion named with a reason.
2. Keep infeasible, unbounded and nonsmooth problems; give feasibility problems a least-norm objective [CCoM22-03 p. 5].
3. Derivative parity; first- vs second-derivative comparisons go in a separately labelled section.
4. Match tolerances to the rival's default; print every option file.
5. Define outcome categories first; in profiles a failure gets twice the maximal ratio; never average over solved problems only [GR22 p. 26].
6. Profile time and function evaluations; stratify by ndf band and constraint type.
7. Corrections (*not Gill's practice*): tune on a held-out subset; fix scoring rules; run prototypes on the whole collection before claiming anything.

**🔴 Checkpoint**: the protocol is written before the first run; in-sample tuning or a scoring change is printed next to the result.

**Applies to stage**: experiment design; judging results.

**Different from standard practice**: performance profiles are standard (Dolan & Moré 2002); derivative parity, ndf strata, a "false infeasibility" category and printed option files are the group's.

**Limitations**: desktop-scale runs only [03 §8]; the group itself calls such claims "difficult to verify" [GSW15 p. 3].

**Solver translation**: one versioned protocol file per benchmark run.

### Method 5: Linear-algebra-first formulation

**One line**: start the design from each iteration's linear systems (which matrix, factored or updated, how singularity and wrong inertia are repaired, in which regime); reformulate so third-party factorizations apply; count factorizations.

**Evidence**:
- Stated: SSL14 (the header quote); "Since linear algebra is a special interest of the authors, we have devoted extra attention to linear algebraic issues associated with interior methods." [FGW02 p. 528]; "Methods based on sparse updating are hard to speed up" [ANC11 slide 36].
- Practice: factorized quasi-Newton (1972), factorization updating (1974) [06 T1]; SQIC run with LUSOL, MA57 and UMFPACK, factorization counts in its tables [03 §1.3, §1.5]; regularized subproblems "so that the resulting linear systems are always nonsingular and third-party solvers may be used" [GR13 rep. p. 3]; an LDLᵀ trust-region method whose §3.1 "Complexity" counts O(n²) operations per iteration [BG23 p. 10].
- Say–do consistency: ✅ stated + practised at the linear-solver layer (Inner Tensions X1).

**Steps**:
1. Write the KKT or QP systems of every iteration; note sparsity and dense columns.
2. Choose the representation by regime: explicit reduced Hessian for small ndf, full-space factorization for large ndf [GSW15 p. 13]; an updated dense LDLᵀ for small unconstrained problems [BG23].
3. Choose updating vs refactoring by hardware and problem class.
4. Specify inertia detection and repair from a stated menu: inertia-controlling LBLᵀ; Gould's pivot modification; tile preordering; a conventional LBLᵀ of H + σI (Wächter–Biegler) [GR13 rep. p. 20].
5. Regularize (Method 1) so a third-party solver can be swapped in; SQIC ships interfaces to LUSOL, MA57, MA97 and UMFPACK [06 T8].
6. Report factorization and modification counts.

**🔴 Checkpoint**: if the theory assumes solves the factorization cannot deliver on degenerate problems, reformulate before tuning. A repeating rank-detection loop (13 factorizations on drcavty2, "the repeated failures were rather expensive" [SIGEST05 p. 114]) needs a dedicated rank-revealing step.

**Applies to stage**: method design; debugging.

**Different from standard practice**: the matrix, not the merit function, is the first design decision; in the group's papers "complexity" means operations per iteration, not worst-case iteration counts.

**Limitations**: overlaps Gould's lens (Gill's part: the regime choice, reformulation for off-the-shelf solvers, the repair menu, counts). Matrix-free solves are outside the evidence; SSL14 names multicore and "GPU-based architectures" as reasons to use third-party solvers, but no GPU experiment was found.

**Solver translation**: a reduced-Hessian vs full-space KKT path switched by ndf; an inertia-repair menu with counters; an LDLᵀ-update path for small dense subproblems.

### Method 6: User-wall problem choice with a resource profile

**One line**: take the next problem from named users who hit a scale or robustness wall; profile it (derivative cost, ndf, one-off vs sequence, infeasibility); choose the method family by that profile, even against the trend.

**Evidence**:
- Stated: "Second derivatives are assumed to be unavailable or too expensive to calculate." [SIGEST05 p. 99]; for MINLP subproblems "the rapid and reliable detection of infeasibility is a crucial requirement of an algorithm", while for one-off problems "an infeasible problem is generally the result of a unintended formulation or coding error" [GW10/12 p. 5].
- Practice: SNOPT started because aerospace users outgrew NPSOL [SIGEST05 p. 101]; interior QP solvers rejected inside SQP because "they are difficult to “warm start” from a near-optimal point" [GZ22 p. 5]; SQP kept through what the 2011 slides call its decline (slide 26), since interior methods "have difficulty exploiting a good solution" (slide 33) [06 T6].
- Say–do consistency: ✅ stated + practised.

**Steps**:
1. Name the user class; collect its models or its sequence of related problems.
2. Profile: derivative cost; ndf at the solution; one-off vs sequence; expected infeasibility.
3. Map: few ndf + expensive functions + sequences → active-set SQP, quasi-Newton, warm starts; many ndf + cheap exact Hessians + one-off → interior or second-derivative SQP; frequent infeasibility → elastic mode and infeasibility certification.
4. Adapt at the user level first; pick a scalable test problem from the application [03 §1.8].
5. Keep the users in the loop during development [SIGEST05 p. 127].

**🔴 Stop rule**: if the profile favours the rival family, say so [GSW15 p. 26].

**Applies to stage**: problem choice; agenda.

**Different from standard practice**: the problem comes from a user's wall, not a literature gap.

**Limitations**: the least exclusive method; its distinctive part is the resource triage. Without industry partners, use public application collections and say so.

**Solver translation**: classify user workloads by derivative cost, ndf and sequence structure before choosing the IP or SQP path.

## Stage Workflows

Skeleton: Dantzig's SOL programme, with software "systematically tested on representative problems" [GBD08 p. 152].

### Workflow A: Problem choice
**Input**: users and their failing classes; your stratified benchmark; your last limitations paragraph.
**Steps**:
1. Profile the users' problems (Method 6).
2. Read your own "negative side" paragraph and failure table; list the walls (Method 2).
3. Choose a measurable wall a named user class hits (e.g., 24 of 68 problems with ndf > 4000).
4. Ask whether the ecosystem changed: AD Hessians, multicore, new third-party solvers (Heuristic 9).
5. If the consensus calls the needed family a "closed chapter" but users need its capability, stay (Method 3).
**🔴 Checkpoint**: no named user class and no measured losing stratum → produce the stratified table first (Workflow D).
**Output**: one paragraph: user class, wall with numbers, resource profile, the limitation it attacks.

### Workflow B: Method design
**Input**: the wall; the current subproblem and its linear algebra.
**Steps**:
1. Write the linear systems; mark where they become singular or indefinite (Method 5).
2. Find the smallest well-posing change that keeps the solution and has a known feasible point (Method 1).
3. Derive the parameter rule; write the local-equivalence and global statements before coding (Method 1).
4. Look for the older family the idea specializes (Method 3).
5. Combine mechanisms by regime; port proven unconstrained devices (Heuristics 7, 8).
6. Decide factorization vs updating; name the third-party solvers to support (Method 5).
**🔴 Checkpoint**: a change that moves the solution, needs hand-tuning away, or lacks a local-equivalence statement → redesign.
**Output**: a design note: subproblem, modification and parameter rule, two theorems to prove, factorization plan, counters.

### Workflow C: Experiment design
**Input**: the prototype, the rival code, the collection.
**Steps**:
1. Freeze the universe, size rule and exclusions; keep hard cases; make problems comparable (Method 4; Heuristic 6).
2. Enforce derivative parity, match tolerances, print option files (Method 4).
3. Define outcome codes and strata before running (Methods 2, 4).
4. One external rival plus your predecessor; one-component ablations (Heuristic 3).
5. For a local-convergence claim, add classes that violate its assumptions (Heuristic 4).
6. Hold out a tuning subset (Method 4 correction).
**🔴 Checkpoint**: the protocol is written before the first run; in-sample tuning is labelled wherever the result appears.
**Output**: a protocol document, later the front of the companion results report (Heuristic 1).

### Workflow D: Execution, debugging and judging
**Input**: runs and logs.
**Steps**:
1. Rule out inaccurate derivatives, precision loss and too-good objectives first (Heuristic 10).
2. Instrument iteration types, modified or elastic shares, factorizations per matrix (Methods 1, 5).
3. Re-run each failure until typed; keep it counted (Method 2).
4. Stratify, name the mechanism, write the remedy (Method 2).
5. If a result contradicts a paper or the consensus, reproduce on its subset and on the full set (Method 3).
6. Drop claims the full set does not support; keep mixed results mixed (Heuristic 2).
**🔴 Checkpoint**: modification on most iterations of a class (GKR20: 98–100%) → fix inertia handling, not the line search. A claim holding only on a subset is withdrawn.
**Output**: a failure-autopsy table (problem, type, mechanism, remedy) and stratified profiles.

### Workflow E: Writing and release
**Input**: results, derivations, code.
**Steps**:
1. Regime in the abstract; a "negative side" paragraph for your method and the rival; remedy next to each diagnosis (Method 2).
2. A simplified problem in the paper; full equations and per-problem tables in companion reports (Heuristic 1).
3. Release: exits grouped by cause, advice ordered by likelihood, failure exits in the regression suite, old calling sequences kept (Heuristic 5).
4. End with the future-work paragraph that becomes the next agenda.
**🔴 Checkpoint**: every abstract claim holds on the full set; the losing regime is stated; paper-to-report pointers are correct (GKR20 pointed to the wrong report [03 §4.1]).
**Output**: paper + results report + equations report.

### Workflow F: After publication: responding to critique
**Input**: an outside benchmark, counterexample or critique.
**Steps**:
1. Check whether the limit was already printed (for SNOPT's ndf limit, it was) [05 §3.6].
2. A critique of test conditions gets a protocol and data (GSW15).
3. A named mechanism (critical multipliers, Izmailov & Solodov 2011) becomes motivation; reuse the critics' test sets [05 §1.3].
4. Adopt the rival's device when it works (Wächter–Biegler inertia correction) [05 §1.2].
5. Counter-critique stronger assumptions (analyses that "require a global solution of (1.1)" [CCoM13-04 pp. 2–3]).
**🔴 Checkpoint**: a cited critic's conclusion is stated correctly. The SQOPT guide cites Hall & McKinnon for "the probability is very small"; they concluded "In practice therefore the expand procedure cannot be relied upon to prevent cycling." [05 §1.1].
**Output**: a protocol, data or new line of work, never a silent downgrade.

### Supervision (records only; no Gill-style workflow)
Records [04 §4]: thesis topics follow the current method line and grants [inferred]; a new student joins an advisor–alumnus pair; the predecessor's method is the baseline; journal versions come 1–12 years after the thesis. Meetings and topic assignment are unknown; no supervision method is invented.

## Research Heuristics

1. **Separate evidence from argument**: per-problem tables and full equations go to companion reports [03 §4.1]. Practice only.
2. **Drop what the final runs do not support**: the 2011 preprint's "significantly more efficient than our current SQP package SNOPT" is absent from SIOPT 2013 [03 §3.5]; "Results are more mixed for problems that do not satisfy the property of strict complementarity." [GKR17b p. 408].
3. **One external baseline per line, then one-component ablations** against your predecessor [03 §1.3]; re-run the external baseline when the line changes materially.
4. **Test local theory on classes built to break it**: 84 problems with rank-deficient active Jacobians plus the degenerate set of Mostafa, Vicente & S. J. Wright [GKR17b pp. 404, 406]. One paper only.
5. **Put the diagnosis inside the solver**: exits grouped by cause, advice ordered by likelihood (inaccurate gradients first), derivative-checker exits, a regression log that expects failure exits [03 §2.1, §5.3]. Group practice.
6. **Make test problems comparable**: least-norm objectives for feasibility problems; "Typically, a method will behave in a similar way on all the problems of one type, which can distort any numerical comparison between methods." [CCoM15-02 p. 26].
7. **Combine mechanisms by regime**: "penalty methods provide an effective strategy for handling equality constraints, while barrier methods provide an effective approach for the treatment of inequality constraints" [GKR20 p. 1067].
8. **Port proven unconstrained devices** to the constrained or projected case (quasi-Wolfe projected search [FGWZ23]; on-the-fly convexification [GSW15 p. 15]).
9. **Re-examine your bets when the ecosystem changes** (AD Hessians, multicore) [ANC11 slides 26, 28, 36].
10. **Modelling hygiene**: "Verify level 3 should be specified whenever a new function routine is being developed." [SNUG15 p. 85]; "if the objective value is much better than expected, SNOPT may have obtained an optimal solution to the wrong problem!" [SNUG15 p. 93]; solve related problems tightest-first [SNUG15 p. 107].

## Signature Work Anatomy

Full anatomies: [01 §2](references/research/01-publications.md); reception: [05](references/research/05-peer-critique.md).

### On projected Newton barrier methods for linear programming and an equivalence to Karmarkar's projective method (Math. Program. 36, 1986, https://doi.org/10.1007/BF02592025)

| Dimension | Content |
|---|---|
| Origin | the group recognized barrier-method equations in Karmarkar's method [GBD08 p. 154; observed, MHW19] |
| Why then | it still held barrier expertise the field had dropped: "By the early 1980s, barrier methods were almost without exception regarded as a closed chapter in the history of optimization" [FGW02 abstract] |
| Key insight | for a particular barrier parameter the steps are identical [observed, MHW19] |
| Minimum evidence | a theorem plus a barrier code competitive with simplex [GBD08 p. 155] |
| Abandoned path | the ellipsoid method (1980 report only); this paper not read |
| Methods | 3, 1 |

### SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization (SIAM J. Optim. 12, 2002, https://doi.org/10.1137/S1052623499350013; SIAM Rev. 47, 2005, https://doi.org/10.1137/S0036144504446096)

| Dimension | Content |
|---|---|
| Origin | aerospace users outgrew NPSOL [SIGEST05 p. 101]; work began 1992 [ANC11 slide 6] |
| Key insight | sparse SQP, limited-memory quasi-Newton, reduced-Hessian QP, augmented Lagrangian merit function, elastic mode; ndf limit in the abstract |
| Protocol | dated CUTEr distribution, named exclusions, split at 2000 degrees of freedom, every failure named [03 §1.1] |
| Reception | SIGEST; outside benchmarks confirm the ndf limit [05 §3] |
| Methods | 6, 2, 4, 5 |

### On the Performance of SQP Methods for Nonlinear Optimization (Springer PROMS 147, 2015, https://doi.org/10.1007/978-3-319-23699-5_5)

| Dimension | Content |
|---|---|
| Origin | the "conventional wisdom" that IP software is faster and more reliable from scratch [GSW15 p. 3] |
| Design | SNOPT 7.4 vs IPOPT 3.11.8 on 1153 of 1156 CUTEst problems; option files printed; tolerance matched [03 §1.1] |
| Finding | "more nuanced"; weak at ndf > 4000; remedy named next [GSW15 p. 13]; flaw: two problems rescored without a note |
| Methods | 4, 3, 2 |

### The stabilized SQP and shifted penalty-barrier line, 2010–2024 (GR12, GR13, GKR17a, GKR17b, GKR20, GZ24)

| Dimension | Content |
|---|---|
| Origin | self-narrated: SQP "declined" (slide 26); sequences of related problems (slide 32); "Do all of the above as seamlessly as possible!" (slide 35) [ANC11] |
| Why then | AD Hessians; multicore; stabilized SQP had local theory (S. J. Wright 1998; Hager 1999) but "there is no guarantee of convergence to a local solution for an arbitrary starting point" [GR13 rep. p. 6] |
| Key insight | exact-Hessian QP with a unique bounded solution, nonsingular systems, a known feasible point [GR13 rep. p. 3] |
| Abandoned paths | the 2011 efficiency claim; a 2013 second-order preprint of unclear fate [03 §3.5] |
| Reception | contested globalization [05 §5]; no public code |
| Methods | 1, 5, 2 |

### On Recent Developments in BFGS Methods (CCoM 22-04, 2022, rev. 2023; report only) and An LDLᵀ Trust-Region Quasi-Newton Method (SIAM J. Sci. Comput. 46, 2024, https://doi.org/10.1137/23M1623380; arXiv:2312.06884)

| Dimension | Content |
|---|---|
| Origin | "there is no known analytical means of determining the relative performance of these methods on a general nonlinear function" [GR22 p. 1] |
| Design | nine variants in one MATLAB code base; all 275 unconstrained CUTEst problems with n ∈ [2, 5000]; Andrei's method re-implemented [03 §2.4] |
| Finding | "a novel combination of self-scaling and a factored Hessian shows significant and consistent improvement" [GR22 p. 37]; then an O(n²) LDLᵀ trust-region method [BG23] |
| Methods | 3, 4, 5 |

## Research Anti-patterns

| Anti-pattern | Why the group opposes it (source) | Instead |
|---|---|---|
| Averaging over solved problems | "bias the results against more robust solvers" [GR22 p. 25] | Method 4 |
| Judging on a subset | "results have the potential to be misleading" [GR22 p. 32] | Methods 3, 4 |
| Unequal derivative information | "Test results from second-derivative methods are unlikely to be representative in this case." [GSW15 p. 3] | Method 4 |
| Theory without numerical stability | "wonderful theoretical properties" [GR22 p. 38] | Method 5 |
| Abandoning a family over a feared defect | "Vague but continuing anxiety about barrier methods eventually led to their abandonment" [FGW02 p. 525] | Method 3 |
| Dismissing a class untested | factored-Hessian methods "dismissed" [GR22 p. 37] | Method 3 |
| Test routines at x = 0 or x = 1 | "how often the special properties of these numbers make the test meaningless" [NPUG p. 40] | Heuristic 10 |
| Local analyses needing a global QP solution | [CCoM13-04 pp. 2–3] | Method 1 |

## Research Trajectory

| Period | Main direction | Why it turned | Representative work |
|---|---|---|---|
| 1971–1979 | NPL: factorized quasi-Newton, factorization updating, stable QP | Imperial PhD with Murray | GM72; GGMS74 |
| 1979–1988 | Stanford SOL: NPSOL, ellipsoid tests, Karmarkar → barrier methods | Claimed LP breakthroughs met stored expertise | KAR86; *Practical Optimization* (1981) |
| 1988–2005 | UCSD: sparse SQP for aerospace users; interior KKT linear algebra | Users outgrew NPSOL, while SQP research "declined" (slide 26) | SNOPT02/05; FGW02 |
| 2002–2011 | Periphery: PDE-constrained optimization, applications | Local co-PIs and grants; not continued | [06 T7] |
| 2008–2020 | "SQP renaissance": regularized and stabilized SQP, shifted penalty-barrier | AD Hessians, multicore, sequences of problems | GR13; GKR17a/b; GKR20 |
| 2018–2024 | Projected search; return to quasi-Newton | Student lines; the "dismissal" of factored Hessians | FGWZ23; GZ24; GR22; BG24 |

### Latest
- Latest dated output: Brust & Gill, SISC 46 (17 Oct 2024); last arXiv posting 11 Dec 2023; last teaching Winter 2023; last PhD graduate June 2024. Nothing found for 2025–26 in DBLP, OpenAlex, Crossref, arXiv or Optimization Online; conference programmes not checked [06 §6].
- UCSD Profiles says "Emeritus Professor", the homepage "Distinguished Professor" (date unknown). SNOPT 9 is "Currently in development"; the public release is 7.7.x [06 T8, T10].

## Academic Lineage

- **Upward**: PhD Imperial College 1974; the Mathematics Genealogy Project gives Walter Murray (and David Q. Mayne, uncorroborated); Murray stayed a peer co-author 1972–2021 [04 §1.1]. Named influences: "Martin Beale (Imperial College), Gene Golub (Stanford), and Jim Wilkinson (National Physical Laboratory)" [GBD08 p. 153].
- **Peers**: the SOL "Gang of Four" (Gill, Murray, Saunders, Margaret H. Wright), Tomlin, Forsgren; Nicholas I. M. Gould (team member) is an academic sibling through Murray [04 §1.1].
- **Downward**: 25 PhD students (1981–2024); four postdocs, each a former student; alumni in solver R&D, academia and the group's code (Wong); grand-student Johannes Brust co-authored BG24 [04 §1.2–1.3].
- **Team bridges**: Gould (co-author: 10.1007/BF02591884, 10.1007/s12532-015-0085-3; CUTEst supplier); Curtis co-authors with Daniel P. Robinson, Gill's student (same person [inferred]; 10.1007/s10107-016-1026-2).

## Inner Tensions

- **X1. Custom updating vs black-box factorization.** Praise for "Sophisticated matrix factorization updating techniques" and the LDLᵀ updating work, against "Any reliance on customized linear algebra software makes it hard to “modernize” a method" [GW10/12 p. 2] and slide 36. No reconciliation is stated; ask for the regime.
- **X2. Stated objectivity vs prototype practice.** Whole-collection rules vs HS-scale prototypes tuned in-sample (Method 4).
- **X3. Experiments first vs theory-heavy output.** "there is a real need for extensive experimental testing to justify the theoretical basis of each approach" [GR22 p. 1] vs a 2013–2020 output that is mostly convergence theory [03 §3.5]. Reading [inferred]: theory accepts a method (Method 1); experiments rank methods (Method 4).
- **X4. Openness vs licensed code.** "the fruits of all these activities should be freely available to the wider community" [GBD08 p. 152] vs licensed SNOPT, SQOPT and DNOPT cores [03 §5.2].
- **X5. Concede and absorb vs downgrade and reassure.** Printed limits and adopted critiques vs the EXPAND citation and silence on several named critics [05 §1.1, §2, §3.6].
- **X6. Depth vs pivot.** One core for 52 years vs peripheral lines that end after 1–3 papers [06 §0, T7].

## Mentor Voice (optional)

Thin by necessity: no record of how he criticizes drafts or runs meetings.
- **Channel** [stated]: "I prefer not to answer technical questions by email ( n emails for me to understand your question, m emails for you to understand my answer), but students are welcome to attend my office hours or see me after class." [Math 271B, Winter 2022].
- **Reported by students** [observed]: "I am most grateful for his patience and encouragement over the years." (Wong 2011); "the aesthetic value of dropping subscripts in LATEX" (Wong 2011); "for helping me to always catch the errant split infinitive" (Ferry 2011) [04 top-up A].
- **Style** [inferred from collective texts]: dry, precise, understated (see NPUG p. 40). No research catchphrases are documented; invent none.

## Roundtable Card

- **Lens (one line)**: The linear system decides the method: make every subproblem well posed by the smallest change that keeps the solution, keep warm starts and infeasibility detection, and judge on the whole test set with every failure typed.
- **Leads when**: degeneracy; infeasible subproblems; wrong inertia; second-derivative SQP; warm-starting sequences; SQP vs interior; quasi-Newton implementation; benchmark claims.
- **First questions asked**: (1) Which linear systems per iteration, and what if they are singular or wrong-inertia? (2) ndf at the solution? (3) Which derivatives, at what cost? (4) One-off or sequence? (5) Is a feasible problem ever declared infeasible? (6) How often does each safeguard fire? (7) Which collection and derivative mode per solver?
- **Default recommendation**: measure first: typed failures and each safeguard's firing rate by ndf band (Methods 2, 1). Then by symptom: degeneracy → multiplier-tied regularization with a stated local equivalence (stabilized SQP; globalization contested); infeasible linearization → elastic ℓ1 mode; wrong inertia → regularized KKT for a third-party LDLᵀ plus a repair menu; sequences → primal-dual shifts; reduced-Hessian vs full-space by ndf; the Method 4 protocol.
- **Will push back on**: subset or averaged claims; unequal derivatives; theory ignoring singular systems; modifications that move the solution; untested conventional wisdom; untyped failures.
- **Likely disagreements** ([inferred] from each side's papers; no dispute documented unless marked "Documented"):
  - **Nocedal**: SNOPT's SQP (10.1137/S1052623499350013) vs KNITRO (10.1007/0-387-30065-1_4); limited-memory (10.1007/BF01589116) vs factored BFGS (GR22). Documented (Nocedal's side): Morales et al. call SNOPT's global convergence hard to establish (10.1007/978-3-642-55508-4_10).
  - **Wächter**: warm starts, infeasibility certification vs IPOPT's filter and restoration phase (10.1007/s10107-004-0559-y).
  - **Fletcher**: merit function vs filter (10.1007/s101070100244).
  - **Curtis**: elastic mode vs penalty steering (10.1137/080738222); factorization vs inexact steps (10.1137/08072471x).
  - **S. J. Wright**: globalized (10.1137/120882913) vs local stabilized SQP (10.1023/a:1018665102534). Documented (Wright's side): arXiv:math/0103102 p. 2 says Forsgren, Gill and Shinnerl (10.1137/S0895479894270658) make "assumptions on the pivot sequence that do not always hold in practice"; no reply found.
  - **Ye**: self-dual embedding (10.1287/moor.19.1.53) vs elastic mode.
  - **Nesterov, Toint**: complexity-first design (10.1007/s10107-006-0706-8; 10.1007/s10107-009-0286-5) vs whole-collection testing.
  - **Gould**: open GALAHAD (10.1145/962437.962438), iterative KKT solves (10.1137/S0895479899351805) vs licensed code, direct factorization.
- **Blind spots**: worst-case complexity; stochastic, nonsmooth, ML; matrix-free and GPU linear algebra; in-sample-tuned prototypes; many degrees of freedom.

## Honest Boundary

- **Tacit-knowledge gaps**: how the group sets regularization parameters beyond the stated "natural" rule, reads a failing KKT or QP log, or drops ideas unwritten; how meetings run [02 Gaps; 04 Gaps].
- **Voice**: the only single-author statement is SSL14; the rest is collective or observed. Personal and group practice cannot be separated (no Gill commits in the public code) [03 §5.2].
- **Unread**: *Practical Optimization* (HTTP 403), the 1974 and 1986 papers, the EXPAND paper, the 1980 ellipsoid report, the Izmailov–Solodov full texts, and the Nocedal & S. J. Wright passage GR22 cites as dismissing factored Hessians [01 Gaps; 05 Gaps].
- **Era and resources**: a small, stable SOL-era team; desktop-scale experiments only [03 §8]; a licensed solver with aerospace funding.
- **Field boundary**: not for complexity-driven design, stochastic or nonsmooth optimization, MINLP algorithms, global or derivative-free optimization, conic first-order methods, matrix-free linear algebra.
- **Claimed but unverified** (never core): free software as a principle (licensed cores); "Less reliance on specialized “home grown” software" (true only at the linear-solver layer); Dantzig's "math it up" (whether Gill gives it is unknown); openness as a precondition of judgement; stable success definitions (contradicted); SNOPT 9 as delivered; any supervision philosophy [02; 03; 06 T8].
- **Research date**: 2026-09-28. Gill is living; his last dated output is October 2024. Update this skill periodically (at least yearly, and after any new paper or a SNOPT 9 release).

## Sources (Appendix)

Notes: [01](references/research/01-publications.md) · [02](references/research/02-methodology.md) · [03](references/research/03-process-evidence.md) · [04](references/research/04-mentorship.md) · [05](references/research/05-peer-critique.md) · [06](references/research/06-trajectory.md) · [RESOURCES](references/sources/RESOURCES.md). DOIs and arXiv ids were checked on Crossref or arxiv.org on 2026-09-28.

### Papers (primary)
- GM72: Gill & Murray, IMA J. Appl. Math. 9 (1972), 10.1093/imamat/9.1.91
- GGMS74: Gill, Golub, Murray & Saunders, Math. Comp. 28 (1974), 10.1090/S0025-5718-1974-0343558-6 (abstract only)
- KAR86: Gill, Murray, Saunders, Tomlin & M. H. Wright, Math. Program. 36 (1986), 10.1007/BF02592025 (not read)
- SNOPT02 / SIGEST05: Gill, Murray & Saunders, SIAM J. Optim. 12 (2002), 10.1137/S1052623499350013; SIAM Rev. 47 (2005), 10.1137/S0036144504446096; https://web.stanford.edu/group/SOL/papers/SNOPT-SIGEST.pdf
- FGW02: Forsgren, Gill & M. H. Wright, SIAM Rev. 44 (2002), 10.1137/S0036144502414942; https://ccom.ucsd.edu/~peg/papers/survey.pdf
- GW10/12: Gill & Wong, NA 10-03 (2010), IMA Vol. 154 (2012), 10.1007/978-1-4614-1927-3_6; https://ccom.ucsd.edu/~peg/papers/sqpReview.pdf
- GR12: Gill & Robinson, Comput. Optim. Appl. 51 (2012), 10.1007/s10589-010-9339-1 (not read)
- GR13: Gill & Robinson, SIAM J. Optim. 23 (2013), 10.1137/120882913; report ("rep.", July 2013) https://www.ccom.ucsd.edu/~peg/papers/pdsqp.pdf
- GW15: Gill & Wong, Math. Program. Comput. 7 (2015), 10.1007/s12532-014-0075-x
- GSW15: Gill, Saunders & Wong, 10.1007/978-3-319-23699-5_5; preprint https://ccom.ucsd.edu/~peg/papers/mopta.pdf
- CCoM15-02: Forsgren, Gill & Wong, https://www.ccom.ucsd.edu/~peg/papers/ucsd-ccom-15-02.pdf; Math. Program. 159 (2016), 10.1007/s10107-015-0966-2; arXiv:1503.08349
- GKR17a / CCoM13-04: Gill, Kungurtsev & Robinson, IMA J. Numer. Anal. 37 (2017), 10.1093/imanum/drw004; https://ccom.ucsd.edu/reports/UCSD-CCoM-13-04.pdf
- GKR17b: same authors, Math. Program. 163 (2017), 10.1007/s10107-016-1066-7
- GKR20: same authors, SIAM J. Optim. 30 (2020), 10.1137/19M1247425; https://www.ccom.ucsd.edu/~peg/papers/pdb.pdf
- GZ22 / GZ24 / CCoM22-03: Gill & Zhang, https://www.ccom.ucsd.edu/~peg/papers/pdprojReport.pdf; Comput. Optim. Appl. 88 (2024), 10.1007/s10589-023-00549-1; https://www.ccom.ucsd.edu/~peg/papers/pdproj-results.pdf
- FGWZ23: Ferry, Gill, Wong & Zhang, Optim. Methods Softw. 39 (2024), 10.1080/10556788.2023.2241769; arXiv:2110.08359
- GR22: Gill & Runnoe, CCoM 22-04 (rev. 2023), https://www.ccom.ucsd.edu/~peg/papers/bfgsdev.pdf
- BG23 / BG24: Brust & Gill, https://www.ccom.ucsd.edu/~peg/papers/trustRegionQN.pdf; SIAM J. Sci. Comput. 46 (2024), 10.1137/23M1623380; arXiv:2312.06884

### Stated methodology (primary)
- SSL14: Simon Stevin Lecture abstract, 18 Feb 2014, https://set.kuleuven.be/optec/event-repository/simon-stevin-lecture-philip-e.-gill
- ANC11: "What's New in Active-Set Methods for Nonlinear Optimization?", slides, Manchester, 5 Jul 2011, http://www.cl.eps.manchester.ac.uk/medialand/maths/archived-events/workshops/www.mims.manchester.ac.uk/events/workshops/ANC11/peg.pdf
- GBD08: Gill, Murray, Saunders, Tomlin & M. H. Wright, "George B. Dantzig and systems optimization", Discrete Optim. 5 (2008), 10.1016/j.disopt.2007.01.002; https://ccom.ucsd.edu/~peg/papers/gbd.pdf
- SNUG15: SNOPT 7.5 User's Guide, https://ccom.ucsd.edu/~peg/papers/sndoc7.pdf; NPUG: NPSOL 5.0 User's Guide, https://ccom.ucsd.edu/~peg/papers/npdoc.pdf
- Math 271B course page (Winter 2022), http://www.ccom.ucsd.edu/~peg/math271b/index.html; homepage, https://ccom.ucsd.edu/~peg/

### Process evidence (primary)
- UCSD optimization software site, https://ccom.ucsd.edu/~optimizers/; public `snopt` repositories, https://github.com/snopt
- SQOPT 7.5 guide (EXPAND wording), http://www.ccom.ucsd.edu/~peg/papers/sqdoc7.pdf
- Optimization Online author page, https://optimization-online.org/author/pgill/

### Students, collaborators and peers (secondary)
- MHW19: INFORMS interview with Margaret Wright, 2019, https://www.youtube.com/watch?v=2L5nQIvTohk (auto-captions; transcript in `references/sources/talks/`)
- Theses: Kungurtsev 2013, https://escholarship.org/uc/item/6081f5jc; Wong 2011, https://escholarship.org/uc/item/2sp3173p; Ferry 2011, https://escholarship.org/uc/item/99277951; Mathematics Genealogy Project, https://www.mathgenealogy.org/id.php?id=6811
- Critics and rival benchmarks: Hall & McKinnon, 10.1007/s10107-003-0488-1; Izmailov & Solodov, 10.1007/s10107-009-0279-4; Zhurbenko, Izmailov & Uskov, 10.20310/1810-0198-2019-24-126-150-165; Morales et al., 10.1007/978-3-642-55508-4_10; Byrd, Nocedal & Waltz, 10.1007/0-387-30065-1_4; Joshy & Hwang, arXiv:2512.05392; Dolan & Moré, 10.1007/s101070100263
- S. J. Wright, SIAM J. Optim. 12 (2001), 10.1137/S1052623498347438; arXiv:math/0103102 (p. 2 read); Forsgren, Gill & Shinnerl, SIAM J. Matrix Anal. Appl. 17 (1996), 10.1137/S0895479894270658
- Other members' papers (Roundtable Card, Lineage) carry their DOIs inline; all were checked on Crossref on 2026-09-28.

---
> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
