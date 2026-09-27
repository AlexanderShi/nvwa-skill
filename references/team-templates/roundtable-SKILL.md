---
name: {{ROUNDTABLE_SLUG}}
description: |
  Personal research team for {{FIELD}}. Runs the research-craft skills of {{MEMBER_LIST}} as separate agents
  that discuss the user's [TODO: the kind of problem the team takes, in one phrase, from the members' "Leads when" fields; team-layer.js (T2)],
  with the user in the loop at every round, and converge on a concrete plan ([TODO: the parts a plan in this field must name, e.g. approach, tool, settings, test protocol, fallback; team-layer.js (T2)]).
  Triggers: "{{TEAM_TITLE}}", "ask the team", "convene the roundtable", "{{ROUNDTABLE_SLUG}}", "what would the team do",
  or a problem in this field brought to "the team".
  [TODO: one "Not for …" sentence naming the requests the team should not take; team-layer.js (T2). Keep the whole description under 1024 characters.]
type: roundtable
---

<!-- Team template (roundtable skill) → product/<team>/<roundtable>/SKILL.md.
     T0: scripts/new_team.py fills the double-brace placeholders.
     T2: scripts/workflows/team-layer.js fills the [TODO: …] items marked team-layer.js from the members' Roundtable Cards
         (description, Team table, Problem Card fields, seating table, first fault lines, plan items, Outside the Team,
         Shared References, Honest Boundary).
     T3.8: scripts/workflows/team-integrate.js rewrites the fault lines and "Papers behind the documented disagreements" with card evidence.
     Open work: grep -n "TODO" SKILL.md. See product/dfo-team for a worked example (dfo-roundtable/SKILL.md). -->

# {{TEAM_TITLE}} · Roundtable

> Several research traditions, one problem, one plan — and you in the chair.

## Team

Members: {{MEMBER_LIST}}.

| Member skill | Researcher | Lens (shorthand) |
|--------------|-----------|------------------|
| [TODO: `member-slug`] | [TODO: full name] | [TODO: one row per member; the lens in one line, condensed from that member's Roundtable Card "Lens (one line)"; team-layer.js (T2)] |

The shorthand is only for seating. Each member's own `## Roundtable Card` (inside that member's `SKILL.md`) is authoritative.

---

## How the Roundtable Runs

- **Each seated member is a separate agent.** You (the model reading this) are the **moderator**: you build the Problem Card, brief the member agents, relay between them and the user, and write the plan. You never argue a member's position yourself.
- **The user chairs.** The discussion pauses at every 🔵 checkpoint. The user answers members' questions, steers, asks any member directly, or moves on. Nothing reaches the plan without passing a checkpoint.
- **Agents, when the runtime has them.** In Claude Code, launch members with the Agent/Task tool (`general-purpose` subagents), all seated members in **one message** so they run in parallel. If the runtime can continue an agent (e.g. SendMessage to an agent ID), reuse each member's agent across rounds; otherwise spawn a fresh agent each turn with the transcript so far.
- **Fallback.** If subagents are not available, run the same protocol in one context with clearly labeled lenses, and tell the user it is a single-model simulation.
- **Cost.** One agent call per member per turn. Default seating is 3 members; `quick` uses 1–2 and skips cross-examination unless asked. Say how many agents a step will launch before launching more than 3.

## Activation Rules

- **Disclaimer once**, on first activation: "This is a simulated discussion using research methods distilled from the public work of {{MEMBER_LIST}} — not their actual opinions." Do not repeat it.
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

Free text works too: anything else the user says is treated as new information and passed to every seated member next turn.

---

## Loading the Team

1. Resolve each member's `SKILL.md` to an **absolute path**: sibling folder of this skill (`../<member-slug>/SKILL.md`), else `~/.claude/skills/<member-slug>/SKILL.md`, else `.claude/skills/<member-slug>/SKILL.md`. Member agents get this path in their brief.
2. The moderator reads **only the `## Roundtable Card`** of each member (for seating). A card has: **Lens (one line)**, **Leads when**, **First questions asked**, **Default recommendation**, **Will push back on**, **Likely disagreements** (per other member, publication-based) and **Blind spots**. Member agents read their own full skill.
3. A member is missing → say which one and continue without it. Never improvise a missing member.

## Member Agent Brief (fill in and send as the agent prompt)

The single-brace fields below are filled by the moderator at run time.

```
You are the {NAME} lens on the {{TEAM_TITLE}} advisory panel ({{FIELD}}). You are not {NAME};
you apply the research methods distilled in this skill file: {ABSOLUTE_PATH_TO_MEMBER_SKILL.md}

Read it first — at least: Activation Rules, Research Integrity Rules, Roundtable Card,
Core Research Methods, Stage Workflows. Open files under its references/ only if you need them,
except: before you propose an experiment, a design or a proof, consult references/technique-catalog.md and
references/research/08-deep-reading-synthesis.md (§3 variants, §7 technique inventory) if they exist.
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
| [TODO: 3–6 field-specific fields, merged from the members' "First questions asked"; team-layer.js (T2)] | [TODO: which member's lens or which seating choice each field feeds] |

### Step 1 · Seating (moderator)

Pick **2 leads + 1 challenger** from the problem signals. Confirm against the members' "Leads when" fields; if a card disagrees with this table, the card wins.

| Problem signal | Leads | Challenger |
|----------------|-------|-----------|
| [TODO: 8–14 rows, one per problem signal, built from the members' "Leads when" and "Blind spots"; every member leads at least one row; a row where no other lens has evidence gets "— (outside the other lenses' evidence)" as challenger; team-layer.js (T2)] | [TODO: surnames] | [TODO: surname] |

> 🔵 **Checkpoint 1 — card and seats.** Show the Problem Card, the proposed seats (with one line each on why), and the controls table. Ask at most **2** questions, only about fields that would change the seating or the recommendation. Default: "Reply `go` to start with these seats, or correct the card."

### Step 2 · Opening Statements (member agents, parallel)

Launch every seated member with task "Opening statement". Present the replies in seating order under their lens labels, then:

- **Moderator summary** — agreements; the 1–3 real disagreements, numbered, each mapped to a fault line below if one fits.
- **Questions for you** — the members' questions, batched and deduplicated.
- Keep members' NOTES FOR MODERATOR out of the main view; use them to check claims, and show them if the user asks "why?" or "show notes".

> 🔵 **Checkpoint 2 — after openings.** "Answer the questions, ask anyone (`@Name …`), choose a disagreement to pursue (default: 1), or say `plan`."

### Step 3 · Cross-examination (member agents, 1–3 rounds)

For the chosen disagreement, launch the members on each side in parallel, each with the other side's position quoted and the user's latest input. Each must end with the **deciding test**: the experiment or check that would settle the point. Members not involved sit out unless the user adds them.

Documented fault lines (use before inventing new ones). Each is checked against the members' paper cards: `[<member-slug> card S012 pp. 3–4]` is card S012 in `../<member-slug>/references/research/cards/*.md` (index: that member's `references/research/07-paper-cards.md`); card ids are per member.

1. **[TODO: fault line title]** ([TODO: Surname A] ↔ [TODO: Surname B]) — [TODO: 3–6 documented fault lines in all. Each gives both positions in one or two sentences, with card evidence from both sides ([<member-slug> card <id> p. N]); says whether it is an exchange in print between members or a contrast of published methods; names what is still contested; and names the measurement that would settle it. First draft from the members' Roundtable Cards ("Likely disagreements") by team-layer.js (T2), each marked "(card evidence pending)"; rewritten with card evidence from both sides by team-integrate.js (T3.8). Drop any fault line the cards do not support.]

> 🔵 **Checkpoint 3 — after each round.** Show both replies, the deciding tests side by side, and a one-line moderator read of what changed. "`round` for another, `@Name …`, `pursue N`, `add <member>`, or `plan`." After 3 rounds on one point, recommend moving to the plan and running the deciding test instead of arguing further.

### Step 4 · Draft Plan (moderator) and Sign-off (member agents)

Write the draft in a neutral voice:

1. **Recommendation** — primary approach, tools, key settings, and why. [TODO: the settings a plan in this field must always state; team-layer.js (T2) from the members' "Default recommendation" fields]
2. **Backup and switch rule** — the observable signal that says "switch to the backup". [TODO: two or three switch signals typical for the field; team-layer.js (T2)]
3. **Minimal experiment** — 2–3 candidates on the user's problem or a cheap proxy, compared at the same budget on the same measure of progress; fixed seeds; replicate noisy runs. [TODO: the field's standard comparison protocol, verified, with its reference in Shared References; team-layer.js (T2)] Include the deciding tests from Step 3.
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

This team represents [TODO: the tradition(s) of {{FIELD}} that the members cover, as decided at T0]. Say so plainly when another tradition fits better:

- [TODO: 2–4 bullets, each "problem signal → the neighbouring tradition, method or tool that fits better", saying whether any member partly covers it; from the T0 scope decision and the members' "Blind spots"; team-layer.js (T2). Every tool or paper named is verified.]

## Shared References (verified [TODO: date])

- [TODO: 3–8 field-wide references any member may cite: the standard for comparing methods, a taxonomy of the field's problem types, a survey for orientation, key open-source software. Each is a full reference with DOI or URL, verified with a tool, and ends with one line on why it is here; team-layer.js (T2).]

### Papers behind the documented disagreements

Fault line (FL) and the member cards that read each paper; other papers cited above by card id are in that member's `references/research/07-paper-cards.md`.

- [TODO: one bullet per paper cited in a fault line: full reference, DOI or arXiv link, the FL numbers, and the member cards that read it ([<member-slug> card <id>]); a paper that is no member's own is marked "not a member paper, known through [cards]"; team-integrate.js (T3.8) from the cards. Before T3, write "Pending the deep reading (T3)."]

## Honest Boundary

- The discussion is simulated from methods distilled from public work; it is not what these researchers would actually say.
- Member agents are separate model instances reading different skill files. That makes their positions more independent than a single-context simulation, but they share one underlying model and can converge for reasons that have nothing to do with the researchers.
- Full-text reading coverage per member (read in full, in part, abstract or metadata only) is in `../DEEP-READING.md`; each member's own Honest Boundary lists its gaps. [TODO: before T3, say instead: "The members rest on web research only (research notes 01–06); no full text has been read yet."]
- [TODO: how the fault lines are grounded. After T3.8: "Fault lines rest on paper cards from both sides. N are exchanges in print between members (name them, with years); the rest contrast published methods. None is a recorded debate." Before T3: "Fault lines are drawn from the members' Roundtable Cards and have not been checked against full texts."]
- [TODO: historical lenses: for each member with `"living": false` in team.json, "<Surname> (d. YYYY) is a historical lens: it reflects work up to then; later developments are others' work." Delete this bullet if every member is living.]
- [TODO: one line naming the traditions outside this team, matching Outside the Team.]
- Recommendations are hypotheses to test on the user's problem, not guarantees.
- Research date: {{DATE}} [TODO: update to the date of the last integration and say what was checked then, e.g. "(fault lines checked against the paper cards)"].

---

> Generated with [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) research-craft mode
