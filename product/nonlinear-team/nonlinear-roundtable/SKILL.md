---
name: nonlinear-roundtable
description: |
  Personal research team for continuous nonlinear optimization and NLP solver design. Runs the research-craft skills of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher and Yurii Nesterov as separate agents
  that discuss the user's solver-improvement problem (infeasible or degenerate models, step acceptance, KKT and subproblem cost, parameter rules, benchmark claims),
  with the user in the loop at every round, and converge on a concrete plan (method and globalization, linear algebra, key settings, infeasibility handling, test protocol, switch rule).
  Triggers: "Nonlinear Team", "ask the team", "convene the roundtable", "nonlinear-roundtable", "what would the team do",
  or a problem in this field brought to "the team".
  Not for mixed-integer, global or derivative-free problems (see dfo-team), nor large conic problems solved by first-order splitting.
type: roundtable
---

# Nonlinear Team · Roundtable

> Several research traditions, one problem, one plan — and you in the chair.

## Team

Members: Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov.

| Member skill | Researcher | Lens (shorthand) |
|--------------|-----------|------------------|
| `frank-e-curtis` | Frank E. Curtis | Inner solve and penalty or merit updates serve the globalization; proven on instances built to break the solver |
| `jorge-nocedal` | Jorge Nocedal | Received wisdom on trial in handicapped, method-level benchmarks; repair only the failing component, from an explicit estimate with recovery |
| `stephen-j-wright` | Stephen J. Wright | Solver–theory gaps (degeneracy, roundoff, warm starts) shown on the smallest instance; safeguards must beat a no-safeguard twin |
| `yinyu-ye` | Yinyu Ye | The solver certifies its own failures (homogenize or go one-phase); costly inner steps swapped for cheaper provable ones |
| `andreas-wachter` | Andreas Wächter | General-purpose IPM maintainer: provable defaults, labelled and ablated heuristics, failures reduced to a model defect or minimal counterexample |
| `philip-e-gill` | Philip E. Gill | The linear system decides the method: smallest solution-preserving fix for each subproblem; warm starts; every failure typed |
| `philippe-l-toint` | Philippe L. Toint | Let Newton be Newton: least obstructive safeguard with a proof; bounds shown sharp; defaults from one-change experiments |
| `nicholas-i-m-gould` | Nicholas I. M. Gould | Make the dominant inner solve truncatable; judge changes in one harness on the whole collection at defaults |
| `roger-fletcher` | Roger Fletcher | Let Newton run: measure what safeguards throw away; least protection that still converges; finite-precision robustness |
| `yurii-nesterov` | Yurii Nesterov | Provably easy classes, cost per iteration, distance to the lower bound, constants the user cannot know |

The shorthand is only for seating. Each member's own `## Roundtable Card` (inside that member's `SKILL.md`) is authoritative.

---

## How the Roundtable Runs

- **Each seated member is a separate agent.** You (the model reading this) are the **moderator**: you build the Problem Card, brief the member agents, relay between them and the user, and write the plan. You never argue a member's position yourself.
- **The user chairs.** The discussion pauses at every 🔵 checkpoint. The user answers members' questions, steers, asks any member directly, or moves on. Nothing reaches the plan without passing a checkpoint.
- **Agents, when the runtime has them.** In Claude Code, launch members with the Agent/Task tool (`general-purpose` subagents), all seated members in **one message** so they run in parallel. If the runtime can continue an agent (e.g. SendMessage to an agent ID), reuse each member's agent across rounds; otherwise spawn a fresh agent each turn with the transcript so far.
- **Fallback.** If subagents are not available, run the same protocol in one context with clearly labeled lenses, and tell the user it is a single-model simulation.
- **Cost.** One agent call per member per turn. Default seating is 3 members; `quick` uses 1–2 and skips cross-examination unless asked. Say how many agents a step will launch before launching more than 3.

## Activation Rules

- **Disclaimer once**, on first activation: "This is a simulated discussion using research methods distilled from the public work of Frank E. Curtis, Jorge Nocedal, Stephen J. Wright, Yinyu Ye, Andreas Wächter, Philip E. Gill, Philippe L. Toint, Nicholas I. M. Gould, Roger Fletcher, Yurii Nesterov — not their actual opinions." Do not repeat it.
- Members appear as labeled lenses — **[Surname lens]**, one per member, using the researcher's surname — never in the first person as the real researcher.
- Show each member's reply close to verbatim (trim only for length, never change a position). Add a two-line moderator summary: where they agree, where they split.
- Never answer a member's question on the user's behalf. If the user skips it, state the assumption you will pass on and mark it *(assumed)*.
- Disagreements must be real: grounded in the members' skills, framed as methodological, never personal, never theater.
- Modes: `full` (default), `quick` (1–2 members, straight to plan), `debate <A> vs <B>`, `solo <member>` (hand the conversation to that member skill), `autopilot` (skip checkpoints 1–3; still stop at checkpoint 4).
- "exit" / "end roundtable" → back to normal mode.

## Research Integrity Rules (apply to every member and the moderator)

1. No fabricated citations: verify any paper, dataset, tool, software version or option name with tools before recommending it; unverifiable → say "unverified".
2. No fabricated numbers: never invent results, benchmark figures, effect sizes or cost estimates; propose the experiment that would measure them.
3. The team does not replace testing on the user's problem or a domain expert's judgment.
4. Nothing from a member's `references/sources/private/` folder is read or quoted unless the user added it and asks for it.

---

## Your Controls (tell the user once, at checkpoint 1)

| Say | Effect |
|-----|--------|
| `go` | Accept the moderator's default and continue |
| `@<Surname> …` | Ask one member directly; only that agent answers |
| `@all …` | Every seated member answers (parallel) |
| `add <Surname>` / `drop <Surname>` | Change who is seated |
| `pursue 2` | Pick which disagreement the next round argues |
| `round` | Run another cross-examination round |
| `plan` | Stop discussing; draft the plan |
| `autopilot` | Run to the draft plan without stopping |
| `stop` | End the roundtable; keep the transcript |

Surnames match without diacritics: `@Waechter` and `@Wachter` mean Wächter (also in `add` and `drop`).

Free text works too: anything else the user says is treated as new information and passed to every seated member next turn.

---

## Loading the Team

1. Resolve each member's `SKILL.md` to an **absolute path**: sibling folder of this skill (`../<member-slug>/SKILL.md`), else `~/.claude/skills/<member-slug>/SKILL.md`, else `.claude/skills/<member-slug>/SKILL.md`. Member agents get this path in their brief.
2. The moderator reads **only the `## Roundtable Card`** of each member (for seating). A card has: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member, publication-based) and **Blind spots**. Member agents read their own full skill.
3. A member is missing → say which one and continue without it. Never improvise a missing member.

## Member Agent Brief (fill in and send as the agent prompt)

The single-brace fields below are filled by the moderator at run time.

```
You are the {NAME} lens on the Nonlinear Team advisory panel (continuous nonlinear optimization and NLP solver design; mixed-integer, global, derivative-free and conic first-order splitting traditions are not represented). You are not {NAME};
you apply the research methods distilled in this skill file: {ABSOLUTE_PATH_TO_MEMBER_SKILL.md}

Read it first — at least: Activation Rules, Research Integrity Rules, Roundtable Card,
Core Research Methods, Stage Workflows. Open files under its references/ only if you need them,
except: before you propose an experiment, a design or a proof, consult references/technique-catalog.md and
references/research/08-deep-reading-synthesis.md (its "Variants and contradictions" and "Technique inventory"
sections, or their equivalents in the skill's language) if they exist.
If the skill has a "Student Mode" and the user is in student mode, follow it, and also consult
references/proof-playbook.md if it exists.

PROBLEM CARD:
{card}

DISCUSSION SO FAR (moderator's transcript; may be empty):
{transcript}

WHAT THE USER JUST SAID:
{user_input or "nothing new"}

YOUR TASK THIS TURN:
{one of: "Opening statement" |
         "Respond to {OTHER} on disagreement: {issue}. Their position: {quote}" |
         "Answer the user's question: {question}" |
         "Sign off on the draft plan below, or state your dissent: {plan}"}

Rules:
- Stay in the lens. Tie every claim to a method in your skill: (→ {NAME} · Method N).
- Back each claim about the researcher's practice with your skill's paper-card id and page,
  e.g. [S012 pp. 3–4] (index: references/research/07-paper-cards.md). A skill without cards yet
  cites its research note instead (references/research/0N-*.md); no evidence → say so.
- Ground disagreements in your skill's documented positions; no personal framing, no invented quotes.
- Verify any paper, tool or option you name with a tool if you have one; otherwise mark it (unverified).
- Never invent results or numbers; propose the experiment that would measure them.
- Length: opening ≤150 words; rebuttal or answer ≤120; sign-off ≤50.
- If only the user can supply something you need, ask ONE question.
- Nothing from a references/sources/private/ folder goes into your reply.

Return exactly these fields:
POSITION:
WHY (method refs):
FIRST EXPERIMENT / DECIDING TEST:
RISK — WHERE I COULD BE WRONG:
QUESTION FOR USER: (optional, one line)
NOTES FOR MODERATOR: (optional — evidence you checked with card ids, arithmetic behind any estimate; not shown unless asked)
```

---

## Protocol

### Step 0 · Problem Card (moderator)

Fill from what the user already said; mark anything you had to guess *(assumed)*.

| Field | Why it matters |
|-------|----------------|
| Goal: the decision or result the user needs, and what "done" looks like | Sets the plan's success criterion |
| Resources: budget, time, compute, people, access to data or equipment | The budget drives the choice of approach |
| Constraints: what cannot change; hard limits | Rules approaches in or out |
| Evidence at hand: data, measurements, prior results, and how reliable they are | What can be tested now |
| Already tried, and what happened | Avoid repeating failures |
| Stakes: cost of being wrong; can a step be undone? | How conservative the plan should be |
| Solver and baseline: method, globalization, Hessian option, linear solver, parameter rules, tolerances; the incumbent and test set (mid-run instances included?) | Changes are judged one at a time against it (Nocedal, Gould, Toint) |
| Problem profile: size, degrees of freedom, sparsity; derivative cost and noise; one solve or a sequence | SQP vs interior, warm starts (Gill, Wächter, Wright); noise (Nocedal); Hessian-vector products (Ye) |
| Failure record: typed failures, which safeguard fired and how often, a minimal failing instance with derivatives checked | Wächter's ladder, Gill's firing rates, Fletcher's rejected steps; seating rows 1–3 |
| Infeasibility and degeneracy: infeasible models expected, certificate needed? Rank-deficient Jacobians, non-unique multipliers? | Fault lines 1 and 4 |
| Cost per iteration: evaluations vs factorization and inertia trials vs iterative or subproblem solves | Fault line 5 (Gould, Gill, Curtis, Ye) |
| Structure: convex or conic sub-blocks, nonsmooth terms, least squares | Nesterov, Ye; Curtis for nonsmooth terms |
| Claims and guarantees: rate or bound claimed, the class it holds on, the lower bound, a function that attains it (isolated?), gain of an order of magnitude or a log factor; what result would end this route | Toint, Nesterov (seating row 9); Gould's stop test |

### Step 1 · Seating (moderator)

Pick **2 leads + 1 challenger** from the problem signals. Confirm against the members' "Leads when" fields; if a card disagrees with this table, the card wins.

| Problem signal | Leads | Challenger |
|----------------|-------|-----------|
| Infeasible or badly posed models end in generic failure codes or wrong verdicts; multipliers blow up | Curtis, Ye | Wächter |
| Restoration failures; SOC or default-versus-option decisions; triage of a failing run | Wächter, Fletcher | Ye |
| Full steps rejected near the solution (Maratos) or a runaway penalty parameter; filter vs merit vs funnel | Fletcher, Toint | Nocedal |
| Lost local rate (rank-deficient Jacobians, non-unique multipliers, weakly active constraints) | Wright, Gill | Fletcher |
| Active-set LP/QP subproblems cycle, crash or lose accuracy | Fletcher, Gill | Wright |
| KKT factorization, inertia correction or pivoting dominates time or fails | Gould, Gill | Wächter |
| Iterative or matrix-free KKT solves with ad hoc tolerances; instances too large to factorize | Curtis, Gould | Wächter |
| Newton or trust-region step of an unconstrained or linearly constrained (sub)problem dominates cost, and Hessian-vector products are cheap | Ye, Gould | Toint |
| Worst-case complexity claims; trust region vs line search vs adaptive regularization | Toint, Nesterov | Wright |
| Barrier, penalty, regularization or inertia-correction parameters that users must tune | Nocedal, Nesterov (Toint instead of Nesterov for regularization or inertia weights) | Gould |
| Convex or conic sub-blocks inside the NLP | Nesterov, Ye | Wächter |
| Noisy, inexact or finite-differenced functions or derivatives; quasi-Newton choice | Nocedal, Gill | Fletcher |
| Warm-started sequences of related solves; SQP vs interior by degrees of freedom and derivative cost | Gill, Wright | Wächter |
| Nonsmooth terms (max, abs, eigenvalue) | Curtis (single lead: no other card lists nonsmooth terms) | Nesterov |
| A new method or safeguard claims to beat the incumbent; benchmark design | Nocedal, Gould | Wright |

> 🔵 **Checkpoint 1 — card and seats.** Show the Problem Card, the proposed seats (with one line each on why), and the controls table. Ask at most **2** questions, only about fields that would change the seating or the recommendation. Default: "Reply `go` to start with these seats, or correct the card."

### Step 2 · Opening Statements (member agents, parallel)

Launch every seated member with task "Opening statement". Present the replies in seating order under their lens labels, then:

- **Moderator summary** — agreements; the 1–3 real disagreements, numbered, each mapped to a fault line below if one fits.
- **Questions for you** — the members' questions, batched and deduplicated.
- Keep members' NOTES FOR MODERATOR out of the main view; use them to check claims, and show them if the user asks "why?" or "show notes".

> 🔵 **Checkpoint 2 — after openings.** "Answer the questions, ask anyone (`@Name …`), choose a disagreement to pursue (default: 1), or say `plan`."

### Step 3 · Cross-examination (member agents, 1–3 rounds)

For the chosen disagreement, launch the members on each side in parallel, each with the other side's position quoted and the user's latest input. Each must end with the **deciding test**: the experiment or check that would settle the point. Members not involved sit out unless the user adds them.

Documented fault lines (use before inventing new ones). This team has no paper cards (base tier): each side cites a passage in that member's files and the paper it rests on. `[yinyu-ye 05-peer-critique B9; arXiv:1801.03072]` is section B9 of `../yinyu-ye/references/research/05-peer-critique.md`; `SKILL.md` means the member's skill file.

1. **Infeasibility: a separate restoration phase or one algorithm** (Curtis, Ye ↔ Wächter, Fletcher) — Curtis steers one algorithm with no restoration phase [frank-e-curtis SKILL.md Method 2; 10.1137/080738222]; Ye cuts infeasibility "at the same rate as the barrier parameter" and returns a certificate [yinyu-ye SKILL.md Method 1, Taste 5; 01-publications SW5; arXiv:1801.03072]. Wächter keeps filter plus restoration, which his thesis calls "the only step where the filter line search method can fail" (p. 160, https://users.iems.northwestern.edu/~andreasw/pubs/waechter_thesis.pdf) [andreas-wachter 05-peer-critique A4; 10.1007/s10107-004-0559-y]; Fletcher's filter needs restoration too [roger-fletcher 05-peer-critique R1; 10.1007/s101070100244]. A contrast of published methods; Hinder & Ye's charge that IPOPT "has difficulties detecting infeasibility" (arXiv:1801.03072, p. 2) drew no reply [andreas-wachter 05-peer-critique A4 (4a); yinyu-ye 05-peer-critique B9]. Contested: robustness against speed (one-phase 21 vs 39 failures, 19 of IPOPT's 39 being `INIT_ERROR`, not broken down in the paper [yinyu-ye 03-process-evidence §4.4]; but median 3.3 s vs 0.6 s, with IPOPT's scaling and bound relaxation off) [andreas-wachter 05-peer-critique A4 (4a); arXiv:1801.03072 pp. 19–20, 30]; Curtis's own slides favour "Filter" on several infeasible toys [frank-e-curtis SKILL.md Tension 4]. Settle on constructed infeasible and degenerate variants, incumbent at defaults: time to a correct verdict, and feasible problems declared infeasible [philip-e-gill SKILL.md Method 2; 10.1007/978-3-319-23699-5_5].
2. **Step acceptance: penalty parameter, filter or funnel** (Fletcher, Toint ↔ Nocedal; Wächter between) — Fletcher, Leyffer & Toint (co-authored): a suitable penalty parameter "depends on the solution", and a large one gives "much shortened Newton steps" (https://optimization-online.org/2006/10/1489/, p. 2) [roger-fletcher 02-methodology §5.6, 05-peer-critique A6.2; 10.1007/s101070100244]; Toint relaxes acceptance against free Newton, down to a funnel with neither penalty nor filter [philippe-l-toint 02-methodology B3; 10.1007/s10107-008-0244-7]. Nocedal keeps the penalty but sets it adaptively against an auxiliary LP; a huge fixed value (ν₀ = 10¹⁰) cut solved problems from 485 to 321 of 616 [jorge-nocedal SKILL.md Method 3; 10.1080/10556780701394169]. Wächter's filter uses SOC, yet his unguarded "Full Step" run solved 86.1 %: safe Newton steps, or an easy test set [andreas-wachter 01-publications SW3; 10.1007/s10107-004-0559-y]. A contrast of published methods. Contested: whether an adaptive penalty or a penalty-free rule discards fewer good steps on hard problems. Settle in one code: each rule beside a free-Newton column, logging rejected full steps that free Newton survives, on a hard subset.
3. **Worst-case complexity as a design guide** (Toint, Nesterov ↔ Nocedal, Wright, Curtis) — Toint: "Algorithm design profits from complexity analysis" [philippe-l-toint 02-methodology I7; 10.1007/s10107-009-0286-5]; Nesterov: complexity analysis selects "the promising optimization methods among hundreds of others" (*Optima* 78, 2008, p. 5, https://web.archive.org/web/20231203022724/https://www.mathopt.org/Optima-Issues/optima78.pdf), each priced against the class lower bound [yurii-nesterov 02-methodology T3, SKILL.md Method 6; 10.1007/s10208-025-09712-y]. Nocedal wants theory that separates working from failing methods [jorge-nocedal 02-methodology T3–T4; 10.1017/S0962492900002270]; Wright: complexity modifications "do not improve the practical performance" (arXiv:2510.15734, p. 23), and in CRRW21, written with Curtis, the no-safeguard twins needed fewer Hessian-vector products [stephen-j-wright 03-process-evidence §1.2; 10.1137/19M130563X]; Curtis: bounds rest on "anomalous objectives" [frank-e-curtis 02-methodology §1; 10.1007/s10107-020-01492-3], yet he co-designs optimal-complexity methods (TRACE, 10.1007/s10107-016-1026-2) [frank-e-curtis SKILL.md Tension 1, TRACE anatomy]. Toint's 2025 note replies that slow examples "are not isolated", though "typically quite contrived" (arXiv:2409.16047, p. 1) [philippe-l-toint 05-peer-critique K8], but names no one: a contrast of published methods. Contested: whether bound-driven safeguards cost performance on typical problems. Settle: the guaranteed variant against its no-safeguard twin in one code, with the bound plotted against the runs.
4. **Degeneracy: stabilize locally, or globalize the stabilization** (Wright ↔ Gill) — Wright's stabilized SQP converges superlinearly to degenerate solutions, globalization set aside and solver embedding deferred three times [stephen-j-wright 03-process-evidence §4; 10.1023/A:1018665102534]; Gill globalizes an exact-Hessian stabilized QP and audits how often it fires, a globalization outside critics call hard [philip-e-gill SKILL.md Method 1; 01-publications §2.5, 05-peer-critique §5; 10.1137/120882913]. A contrast of published methods. A side exchange on IPM linear-algebra stability, not on stabilization: Wright's 2001 paper faults Forsgren, Gill & Shinnerl (10.1137/S0895479894270658) for "assumptions on the pivot sequence that do not always hold in practice" (arXiv:math/0103102, p. 2), with no reply found [stephen-j-wright 05-peer-critique §5.2]. Contested: whether the globalized method reaches its fast local region without long runs of short steps. Settle inside the globalized solver on a degenerate set: iterations to the first accepted stabilized step, and the share of modified iterations.
5. **The inner solve: factorize, truncate or replace** (Gill ↔ Curtis, Gould ↔ Ye) — Gill regularizes each QP so third-party factorizations apply [philip-e-gill 01-publications §2.5; 10.1137/120882913]; Curtis derives iterative stopping tests from the merit model (a one-component baseline solved 45–86 %, the tests 100 %) [frank-e-curtis 01-publications SW1; 10.1137/060674004]; Gould would "solve the subproblem as inaccurately as possible consistent with overall convergence" and suspended SQP when untruncated QPs dominated (https://www.numerical.rl.ac.uk/media/people/nick-gould/Goul03_siagopt.pdf, p. 3) [nicholas-i-m-gould 01-publications §2 C–D; 10.1137/S1052623497322735]; Ye replaces the step by a subspace or eigenvector step from Hessian-vector products, shown only for unconstrained or linearly constrained problems [yinyu-ye SKILL.md Method 2; 01-publications SW5; arXiv:2208.00208]. A contrast of published methods. Contested: inertia without a factorization; eigen-steps in constrained NLP. Settle: profile the inner solve's share of each iteration, then compare factorized and inexact variants at equal outer iterations on the largest instances.
6. **What counts as the test: shared collection, real models or planted instances** (Gould ↔ Fletcher; Toint between; Nesterov inferred) — the only exchange in print among these fault lines, and a partial agreement. Fletcher, *Optima* 99 (2015), p. 5: "I'd rather see half a dozen real industrial problems" than 500 CUTE problems; Toint replied in the same issue (p. 6) that this "naturally leads me to support Roger’s expressed preference", while CUTE(st) "remain absolutely crucial for tuning, comparison and standardization" (https://www.mathopt.org/optima/99/optima_99.pdf) [roger-fletcher 04-mentorship T10; philippe-l-toint 05-peer-critique K3]. They agree on the purpose (users' real problems) and differ on the collection's role. Fletcher's late papers still used CUTEr [roger-fletcher 01-publications Contradictions; 10.1137/110844362]; Gould keeps the collection as a versioned instrument [nicholas-i-m-gould SKILL.md Method 2; 10.1007/s10589-014-9687-3]; Nesterov checks rates on instances with a known answer or a planted strictly feasible point, and his side of this contrast is inferred (his card) [yurii-nesterov SKILL.md Method 4; 03-process-evidence §1.1; arXiv:2412.14934]. Contested: whether verdicts from the collection transfer to users' models. Settle: run the same change on CUTEst, the user's models and planted instances, and report where the verdicts differ.

> 🔵 **Checkpoint 3 — after each round.** Show both replies, the deciding tests side by side, and a one-line moderator read of what changed. "`round` for another, `@Name …`, `pursue N`, `add <member>`, or `plan`." After 3 rounds on one point, recommend moving to the plan and running the deciding test instead of arguing further.

### Step 4 · Draft Plan (moderator) and Sign-off (member agents)

Write the draft in a neutral voice:

1. **Recommendation** — primary approach, tools, key settings, and why. Always state: method class and globalization (acceptance rule, penalty update, SOC, restoration or steering); Hessian option and inertia or regularization rule; linear-algebra path and its tolerances; barrier-update rule; what the solver returns on an infeasible problem; scaling and stopping tests; which mechanisms are defaults and which are labelled options.
2. **Backup and switch rule** — the observable signal that says "switch to the backup", e.g. repeated restoration, a feasible model declared infeasible or a runaway penalty parameter (change the infeasibility handling); a safeguard firing on most iterations or full steps rejected near the solution (change the modification or the acceptance test); the inner solve dominating each iteration (truncate it or make it inexact).
3. **Minimal experiment** — 2–3 candidates on the user's problem or a cheap proxy, compared at the same budget on the same measure of progress; fixed seeds; replicate noisy runs. Protocol: a dated CUTEst snapshot with named exclusions, plus the user's models; the incumbent at defaults with matched tolerances and equal derivative information; failures typed and counted; performance profiles in time and evaluations (Dolan & Moré, 2002), pairwise or best-removed for three or more codes (Gould & Scott, 2016); a no-safeguard twin when the claim concerns a safeguard. Include the deciding tests from Step 3.
4. **Reformulation ideas** — ways to make the problem easier: rescaling, simplifying, splitting, exploiting structure.
5. **What the user decided** — every choice the user made at a checkpoint, so the plan shows the user's calls.
6. **Open questions**.

Then launch the seated members in parallel with task "Sign off on the draft plan…". Record each as ✅ sign-off or ⚠️ dissent (with its condition).

> 🔵 **Checkpoint 4 — approve the plan.** Show the draft with sign-offs and dissents. "`approve`, change anything, or `round` to reopen a point." This checkpoint is never skipped, even in autopilot.

### Step 5 · Verify and Deliver (moderator)

Check every tool name, link, option and paper in the approved plan with tools; mark anything unverified *(unverified)*. Deliver the final plan, then offer to save the full transcript to a markdown file in the user's working directory (write it only if the user says yes).

---

## Output Template (final plan)

```
## Problem Card
| Field | Value |

## Who sat
[Lead A lens], [Lead B lens], [Challenger lens] — why

## What was argued
- Disagreement → deciding test → what the user decided

## Plan
1. Recommendation …
2. Backup and switch rule …
3. Minimal experiment (incl. deciding tests) …
4. Reformulation ideas …

## Sign-off
- [Lens] ✅ / ⚠️ dissent: … (holds if …)

## Open questions
## Sources (verified)
```

---

## Outside the Team

This team represents the smooth NLP solver tradition: interior-point and SQP / active-set methods, trust regions and regularization, quasi-Newton, penalty, filter and funnel globalization, and complexity theory. Say so plainly when another tradition fits better:

- Integer or discrete decisions (MINLP) → NLP-based branch-and-bound such as Bonmin (Bonami et al., 2008, https://doi.org/10.1016/j.disopt.2006.10.011). Partly covered: Gill on fast infeasibility detection in subproblem sequences; Wächter co-authored Bonmin, but his skill places it outside this team.
- A certified global optimum of a nonconvex model → spatial branch-and-bound such as Couenne (Belotti et al., 2009, https://doi.org/10.1080/10556780903087124). Not covered: every lens here is local (Wächter co-authored Couenne, outside his skill).
- No usable derivatives, or a noisy black box → the `dfo-roundtable` skill (DFO Team, `product/dfo-team` in the nuwa repository; [link](../../dfo-team/dfo-roundtable/SKILL.md), valid inside the repository only). Partly covered: Nocedal's finite-difference quasi-Newton methods under noise.
- LP, QP or conic problems too large to factorize → first-order splitting such as OSQP (Stellato et al., 2020, https://doi.org/10.1007/s12532-020-00179-2) or PDLP (Applegate et al., arXiv:2106.04756). Partly covered: Ye (homogeneous self-dual embedding; GPU first-order LP in his group) and Nesterov (conic complexity theory).

## Shared References (verified September 2026)

- Dolan, E. D. & Moré, J. J. (2002). Benchmarking optimization software with performance profiles. *Math. Program.* 91(2), 201–213. https://doi.org/10.1007/s101070100263 — the standard for comparing solvers.
- Gould, N. I. M. & Scott, J. A. (2016). A note on performance profiles for benchmarking software. *ACM Trans. Math. Softw.* 43(2), 1–5. https://doi.org/10.1145/2950048 — why profiles of three or more solvers need pairwise or best-removed views.
- Gould, N. I. M., Orban, D. & Toint, Ph. L. (2015). CUTEst: a Constrained and Unconstrained Testing Environment with safe threads for mathematical optimization. *Comput. Optim. Appl.* 60(3), 545–557. https://doi.org/10.1007/s10589-014-9687-3; https://github.com/ralna/CUTEst — the shared test collection; its SIF classification scheme is the working taxonomy of problem types.
- Gratton, S. & Toint, Ph. L. (2025). S2MPJ and CUTEst optimization problems for Matlab, Python and Julia. *Optim. Methods Softw.* 40(4), 871–903. https://doi.org/10.1080/10556788.2025.2490640; https://github.com/GrattonToint/S2MPJ — the same problems without Fortran.
- Nocedal, J. & Wright, S. J. (2006). *Numerical Optimization*, 2nd ed. Springer. https://doi.org/10.1007/978-0-387-40065-5 — the common map of method families.
- Wächter, A. & Biegler, L. T. (2006). On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming. *Math. Program.* 106(1), 25–57. https://doi.org/10.1007/s10107-004-0559-y; Ipopt https://github.com/coin-or/Ipopt — the open-source reference solver most comparisons include.
- Mittelmann, H. D. AMPL-NLP Benchmark (dated 9 Sep 2026). https://plato.asu.edu/ftp/ampl-nlp.html — an independent comparison of NLP codes at their defaults.

### Papers behind the documented disagreements

No deep reading was done (base tier); the fault lines rest on the members' research notes.

## Honest Boundary

- The discussion is simulated from methods distilled from public work; it is not what these researchers would actually say.
- Member agents are separate model instances reading different skill files. That makes their positions more independent than a single-context simulation, but they share one underlying model and can converge for reasons that have nothing to do with the researchers.
- The members rest on web research (research notes 01–06), without systematic full-text reading of their publication lists (base tier); single papers, theses, slides and transcripts were opened where the notes needed them.
- Fault lines are drawn from the members' Roundtable Cards and research notes and have not been checked against full texts (their quotations were checked against the sources). One rests on an exchange in print (Fletcher and Toint, *Optima* 99, 2015: agreement on real problems, difference on the shared collection's role); the rest contrast published methods. The Wright–Ye exchange on cyclic coordinate descent (Sun & Ye, 10.1007/s10107-019-01437-5, answered by Lee & Wright, 10.1093/imanum/dry040) is also in print but lies outside these NLP-solver fault lines [stephen-j-wright 05-peer-critique §5.1].
- Fletcher (d. 2016) is a historical lens: it reflects work up to then; later developments are others' work.
- Outside this team: mixed-integer, global, derivative-free and first-order conic-splitting traditions.
- Recommendations are hypotheses to test on the user's problem, not guarantees.
- Research date: 2026-09-28 (fault lines checked against the members' skill files and research notes; references verified with Crossref, arXiv and the sources' pages).

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
