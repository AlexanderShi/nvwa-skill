# Deep reading plan · all five DFO team skills

Goal: deepen `michael-powell`, `andrew-conn`, `katya-scheinberg`, `luis-nunes-vicente` and `charles-audet` by reading each researcher's articles in full text, not search snippets.

## Status (2026-09-27)

**Ready to run.** The environment now allows `api.openalex.org` and `arxiv.org`, and both scripts were tested against the live services. Google Scholar is not usable: it offers no API and blocks automated access. The publication list therefore comes from OpenAlex, and the full texts come from arXiv.

What the environment needs (claude.ai/code → cloud icon above the message box → gear next to the environment):

1. **Network access**: `api.openalex.org` and `arxiv.org`. `export.arxiv.org` is no longer needed: its API refuses cloud IPs (HTTP 406), so the scripts use arxiv.org's web search instead. Optional: `www.damtp.cam.ac.uk` (Powell's technical reports).
2. **Environment variables**: `OPENALEX_API_KEY=<key>`. Without a key, OpenAlex allows $0.10 of requests per day per IP, and the shared cloud IP runs out almost at once (HTTP 429).
3. **Setup script**: `pip install pypdfium2` (PDF text extraction).

Then start a **new session** on the branch that carries this file and say: *"Run the DFO deep reading in product/dfo-team/DEEP-READING.md."*

Papers that are not on arXiv (most of Conn's and Powell's pre-2005 work) will show `no-oa` in each researcher's index. Their PDFs have to come from you: drop them into `<researcher>/references/sources/papers/` (git-ignored) and re-run step 2.

## Steps, per researcher

Order: Scheinberg → Vicente → Audet → Conn → Powell (open-access coverage falls in that order).

```bash
R=katya-scheinberg; NAME="Katya Scheinberg"
# 1. Complete publication list (check the candidate table; rerun with --author-id if the wrong profile was picked)
python3 scripts/fetch_publications.py "$NAME" --json --out product/dfo-team/$R/references/sources/publications
# 2. arXiv full texts + index (PDFs and text are git-ignored; INDEX.md is committed)
python3 scripts/fetch_fulltexts.py product/dfo-team/$R --core 20
```

3. **Read in batches.** One agent per batch of about 10 papers, using the brief below. Core papers get full cards; supplement papers get short cards (abstract, introduction, contribution and conclusion only).
4. **Synthesise.** One agent per researcher applies the conservative-update rules in `references/paper-reading-card.md` §3 to `SKILL.md`, then runs `python3 scripts/quality_check.py product/dfo-team/$R/SKILL.md` and updates `RESOURCES.md` and the Roundtable Card.
5. **Commit** the cards, `INDEX.md`, the updated `SKILL.md` and `RESOURCES.md`. Never commit PDFs or extracted text.

## Scale and cost

Paper counts are only known after step 1. Assume roughly 100–250 works per researcher, several hundred in total. Reading every paper in full would cost tens of millions of tokens. The plan is therefore tiered:

| Tier | Which papers | Reading | Rough cost per paper |
|------|-------------|---------|----------------------|
| core | Top 20 by citations per researcher, plus signature works and the last 3 years | Full text, full card | ~30–50k tokens |
| supplement | Everything else with full text | Abstract, introduction, contributions, conclusion; short card | ~5–10k tokens |
| no-oa | No open full text | Metadata and abstract only until you supply PDFs | — |

Raise `--core` to read more papers in full.

## Reading-batch brief (fill in and send to each agent)

```
You are deepening the research-craft skill at product/dfo-team/{R}/ by reading full texts.
Read first: references/paper-reading-card.md (card format, roles, rules) and {R}/SKILL.md (Core Research Methods).
Batch intent: {one line, e.g. "how Scheinberg turns a deterministic method into a stochastic-oracle method"}
Focus dimensions: {e.g. D1, D2, D4, D8}
Papers (from references/sources/papers/INDEX.md): {rows with role}; texts are in references/sources/papers/txt/.
For each paper: write a card (full for core, short for supplement) and append it to references/research/07-paper-cards.md;
set its Read column in INDEX.md to carded or skimmed.
Rules: page or section numbers on every claim; quote only verbatim text; write "not read" rather than guess;
link each card to a Method N (evidence / variant / new-pattern candidate). Do not edit SKILL.md — synthesis is a separate step.
Report: cards written, method links found, new-pattern candidates, papers you could not read.
```

## What this does not change

- Private materials stay in `katya-scheinberg/references/sources/private/` and are never read into public files.
- The integrity rules in each skill still apply: no claim without a page reference, no invented quotes.
