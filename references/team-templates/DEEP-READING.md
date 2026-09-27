<!-- Team template (deep-reading record) → product/<team>/DEEP-READING.md.
     T0: scripts/new_team.py creates it with status "Not started".
     T3.1–T3.7: the deep-tier workflows (team-harvest.js, team-chase.js, team-read.js, team-synthesize.js, team-tighten.js)
           and scripts produce what this file records; tick the stage table as each stage is committed.
     T3.8: scripts/workflows/team-integrate.js resolves every TODO item left in this file (Status, the skills table, the
           roundtable line, the ID letters, the chase repositories, Coverage, its notes and What is still missing). After
           T3.8 no TODO item may remain: the delivery gate greps the team for them.
     T4: scripts/workflows/team-increment.js adds book material and new papers.
     Base tier (team-layer.js with deep_tier: false, no deep reading planned): replace this whole file, this comment
           included, with the two paragraphs below, so the links to it keep working and no TODO item is left:
               # Deep reading · {{TEAM_TITLE}}
               No deep reading is planned for this team (base tier): the skills of {{MEMBER_LIST}} rest on web research
               only (research notes 01–06 in each member's references/research/). To add it later, run stages T3.1–T3.8
               of references/research-team-playbook.md in the nuwa repository; this file then becomes the deep-reading record.
     Open work: grep -n "TODO" DEEP-READING.md. See product/dfo-team for a worked example (DEEP-READING.md). -->

# Deep reading · {{TEAM_TITLE}}

This is the record of how the skills of {{MEMBER_LIST}} are deepened. Each researcher's publications are read in full or in part wherever an open copy exists, and not just as search snippets. Cards and syntheses are written in {{LANGUAGE}}.

## Status ({{DATE}})

**Not started.** The members' skills rest on web research only (research notes 01–06). Progress at any time: `python3 scripts/team_status.py product/{{TEAM_SLUG}}`.

| Stage | Workflow / script | Done |
|-------|-------------------|------|
| T3.1 Publication list | `team-harvest.js` → `validate_works.py` | ☐ |
| T3.2 Open full texts | `acquire_fulltexts.py` | ☐ |
| T3.3 Chase open copies and abstracts | `team-chase.js` → `merge_chase.py` | ☐ |
| T3.4 Reading batches | `plan_reading_batches.py` (one run per round) | ☐ |
| T3.5 Cards | `team-read.js` → `verify_card_quotes.py` → `mark_read_from_cards.py` | ☐ |
| T3.6 Synthesis | `team-synthesize.js` → `quality_check.py` | ☐ |
| T3.7 Tighten | `team-tighten.js` → `check_ledger.py` | ☐ |
| T3.8 Integrate | `team-integrate.js` → `team_status.py --coverage` → `check_links.py` | ☐ |
| T4 Increments | `team-increment.js` (open parts of books, new papers) | ☐ |

[TODO: when T3.8 is done, replace "Not started" and the paragraph above with **Complete.** and these facts, each number taken from `team_status.py` or `verify_card_quotes.py`, never typed from memory:
- every work on each researcher's publication list is indexed;
- how many open full texts were read in full or in part, how many turned out unreadable (each card says why) and how many rows were skipped;
- cards written: total cards, items carded, batch files, split into research works and book material;
- verbatim quotes checked against the extracted text, and how many pass;
- the openly available book material that was read and carded (T4), per book;
- the cards were then distilled into each `SKILL.md`.]

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| [TODO: `member-slug`] | [TODO: count] | [TODO: one row per member: new or renamed core methods (**M<N> · name**), or "Unchanged count" plus any proposed method demoted on review; from each member's 08-deep-reading-synthesis.md; team-integrate.js (T3.8)] |

Each skill also gains the following files:

- `references/technique-catalog.md`: transferable devices from the papers, each with card references.
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections.
- `references/research/09-evidence-ledger.md`: the full evidence, moved out of `SKILL.md` when it was tightened. `SKILL.md` links to its anchors.

In `{{ROUNDTABLE_SLUG}}`, [TODO: which fault lines were added, rewritten or dropped on the card evidence; team-integrate.js (T3.8)].

## Pipeline

Run every stage per member (one workflow per member, in parallel: a workflow runs at most min(16, CPUs − 2) agents at once). How to launch each workflow and its arguments: `scripts/workflows/README.md`. Commit after every stage; the session container is ephemeral. Never commit PDFs, extracted text or `private/`.

1. **Publication list (T3.1, `team-harvest.js`).** The researcher's Google Scholar profile is read page by page with a fetch tool (WebFetch), because Scholar has no API and blocks `curl`. The list is cross-checked with DBLP through its SPARQL endpoint (`scripts/dblp_works.py`; the DBLP REST API sits behind a bot wall), Crossref for DOIs, and DataCite/arXiv; an independent audit sorted by date catches missed rows. `scripts/validate_works.py` checks the result.
   - The outputs are `references/sources/publications/works.json` (all records, including duplicates marked `dup_of`) and `scholar.md` (the readable list and audit notes).
   - IDs (the letters `validate_works.py` accepts): `S` = Scholar row · `D` = bibliographic database only (DBLP, Crossref, …) · `H` = author homepage or CV only · `R` = report-series item not matched to a Scholar row · `X` = external document about the researcher (interview, oral history, memoir) · `B` = openly available part of a book (T4). Any other letter must be passed to `validate_works.py --extra-id-letters`. [TODO: the letters this team used beyond `S`, and for which items, counted from each member's works.json; team-integrate.js (T3.8)]
2. **Open full texts (T3.2).** `scripts/acquire_fulltexts.py` tries, in order: arXiv (by ID or by title search on arxiv.org/search), Unpaywall open-access copies, and author or repository links listed in `works.json`. It requires the researcher's surname among an arXiv hit's authors, checks that each download is a PDF whose first pages carry the title, extracts the text with `[[page N]]` markers, and falls back to tesseract OCR for scans and garbled font layers. The results go into `references/sources/papers/INDEX.md` and `abstracts.json`.
3. **Chase (T3.3, `team-chase.js`).** For works still `no-oa`, agents search legitimate open sources for full texts and abstracts, starting from the `chase_hints` in `team.json`: [TODO: the repositories that actually yielded texts, e.g. author homepages, institutional technical-report series, open proceedings, preprint servers, from INDEX.md's Source column and abstract-sources.json; team-integrate.js (T3.8)]. A report series matched by title can hold other authors' reports, so the author is checked on page 1, not just the title words. `scripts/merge_chase.py` merges their output into `abstracts.json` and re-runs the acquisition, which records `Source = manual` for files saved by hand. **Never shadow libraries, never paywall circumvention.**
4. **Reading batches (T3.4).** `scripts/plan_reading_batches.py` sets each row's Role and splits the papers into batches:
   - **core**: full read, at most 5 papers or 110 pages per batch;
   - **supplement**: selective read, at most 8 papers or 220 pages;
   - **book**: over 150 pages, read chapter by chapter, alone in its batch;
   - **abstract**: no full text, so an abstract or metadata card only, 30 per batch.

   It runs in rounds as new full texts turn up; each later round passes the earlier rounds' plan files to `--exclude`, including rounds still being read. The last round emits the abstract batches. Batch IDs are `c01`, `s02`, … in round 1 and `c2-01`, `a2-03`, … in later rounds.
5. **Cards (T3.5, `team-read.js`).** One agent per batch writes `references/research/cards/<batch>.md` and `<batch>.digest.json` using the brief below. `07-paper-cards.md` indexes every card.
6. **Quote check.** `scripts/verify_card_quotes.py` looks up every quoted passage (`quotes[].text` in the digests) in the extracted text or abstract, normalising ligatures, hyphenation, quote marks and whitespace. Every NOT FOUND is fixed before synthesis.
7. **Read column.** `scripts/mark_read_from_cards.py` fills INDEX.md's Read column from each card's `read_level`: `full` → `carded`, `partial` → `skimmed`, `abstract` → `abstract`, `metadata` → `metadata`, `unreadable` → `unreadable`.
8. **Synthesis (T3.6, `team-synthesize.js`).** Per researcher, with the conservative-update rules of `references/paper-reading-card.md` §3:
   1. One agent mines the cards into `08-deep-reading-synthesis.md`.
   2. A conservative edit of `SKILL.md` follows, within a word budget stated up front, writing `09-evidence-ledger.md` at the same time. Existing methods get evidence first. A new core method needs 3 or more distinct papers plus the four checks.
   3. Read-only skeptics review the edit adversarially.
   4. The verified objections are fixed, and `quality_check.py` is re-run.
9. **Tighten (T3.7, `team-tighten.js`, only for skills still over the word budget).** Long evidence moves from `SKILL.md` to `09-evidence-ledger.md` without loss; `scripts/check_ledger.py --before <scratch>/<slug>-SKILL.before-tighten-<date>.md` (the pre-tighten copy) proves every card id, page reference and quote survives, the front matter and rule sections are unchanged, and every ledger anchor resolves. After the synthesis alone, `scripts/check_ledger.py` without `--before` checks the ledger anchors.
10. **Integrate (T3.8, `team-integrate.js`).** The team README, this file and the roundtable's fault lines are refreshed from the members' 08 syntheses; the coverage table comes from `scripts/team_status.py`; `scripts/check_links.py` checks every link.

### Commands, per researcher

Run these from the repository root. Needs network access to arxiv.org, api.unpaywall.org and api.crossref.org, plus `pypdfium2` and Pillow; `tesseract` (OCR) and `ps2pdf` (PostScript reports) are needed for older papers. Set `OMP_THREAD_LIMIT=1` when several OCR runs share the machine.

```bash
T=product/{{TEAM_SLUG}}
R=<member-slug>                      # each member's "slug" in $T/team.json
S=${TMPDIR:-/tmp}/{{TEAM_SLUG}}-scratch; mkdir -p "$S"   # the workflows' scratch: plan JSON and backups stay outside the repo
D=<YYYY-MM-DD>                       # the date passed to the workflow run

python3 scripts/team_status.py $T    # where every member stands

# T3.1 after team-harvest.js: check the publication list
python3 scripts/validate_works.py $T/$R

# T3.2 open full texts + INDEX.md (PDFs and txt/ stay local; INDEX.md and abstracts.json are committed)
python3 scripts/acquire_fulltexts.py $T/$R

# T3.3 after team-chase.js: merge its output and re-run the acquisition
python3 scripts/merge_chase.py $T/$R

# T3.4 roles + reading batches; one round per wave of new full texts (team-read.js reads $S/batches-<slug>-r<round>.json)
python3 scripts/plan_reading_batches.py $T/$R --no-abstract > "$S/batches-$R-r1.json"
python3 scripts/plan_reading_batches.py $T/$R --round 2 --no-abstract --exclude "$S/batches-$R-r1.json" > "$S/batches-$R-r2.json"
#    ... once a round plans no full-text batch, a last round without --no-abstract gives the remaining works abstract/metadata batches

# T3.5 after team-read.js: check every quote, then fill the Read column (no unread rows after the last round)
python3 scripts/verify_card_quotes.py $T/$R
python3 scripts/mark_read_from_cards.py $T/$R

# T3.6 after team-synthesize.js: quality gate and ledger anchors
python3 scripts/quality_check.py $T/$R/SKILL.md
python3 scripts/check_ledger.py $T/$R
# T3.7 after team-tighten.js (it saves the pre-tighten copy itself): prove the move to the ledger lossless
python3 scripts/check_ledger.py $T/$R --before "$S/$R-SKILL.before-tighten-$D.md"
#    scratch lost? every stage is committed: git show <pre-tighten commit>:$T/$R/SKILL.md > "$S/$R-SKILL.before-tighten-$D.md"

# T3.8 team level
python3 scripts/team_status.py $T --coverage     # paste into Coverage below, unchanged
python3 scripts/check_links.py $T
```

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md` by `python3 scripts/team_status.py product/{{TEAM_SLUG}} --coverage`. Paste its output here; never edit a number by hand.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| [TODO: one row per member plus a **Total** row, pasted from team_status.py --coverage; team-integrate.js (T3.8)] | | | | | | | | | | |

Notes:

- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage. A member without a Google Scholar profile has 0 Scholar rows; that member's list comes from DBLP and the homepage. [TODO: special items counted here, such as interviews or memoirs, per member, and any member without a Scholar profile; team-integrate.js (T3.8)]
- *Read in part* means the supplement reading: abstract, introduction, method or algorithm, main result, experimental setup and conclusion. For a multi-author volume it means only the researcher's own section.
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book (table of contents, errata, addendum, preface, published reviews). They are not counted in the research-work columns.
- *Skipped* rows have Role `skip` in INDEX.md and no card. They are rows that are not the researcher's work (referee lists, misattributed rows, unresolved fragments), plus patents, talks and conference duplicates of journal papers. The Coverage section of each skill's `08-deep-reading-synthesis.md` counts them.
- Page references on cards are pages of the text version that was read, often a technical report or preprint. Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

The full brief lives in `scripts/workflows/team-read.js`; this is the record.

```
You are deepening the research-craft skill at product/{{TEAM_SLUG}}/{R}/ by reading full texts.
Read first: references/paper-reading-card.md (card format, roles, rules) and {R}/SKILL.md
(methods, heuristics, taste marks, workflows — you link cards to their numbers).
Batch {bid} ({core | supplement | book | abstract}): {papers from the plan JSON: ID, year, title, venue,
role, pages, txt path}. Texts are in references/sources/papers/txt/, abstracts in abstracts.json.
Write references/research/cards/{bid}.md in {{LANGUAGE}}. Open it with: batch intent (one line), focus dimensions
(D1–D8), material roles, and how file pages map to printed pages. Then one card per paper:
  core → every dimension from the whole text; supplement → abstract, introduction, method, main result,
  experimental setup, conclusion; book → chapter level; abstract → from the abstract, or metadata only — say which.
Write references/research/cards/{bid}.digest.json: one object per card (fields: see paper-reading-card.md §四).
Rules: a page reference ([[page N]] markers) on every claim; at most two quotes per card, verbatim, with page —
they must pass scripts/verify_card_quotes.py; write "not read" rather than guess; say when the researcher's role
is unclear (middle author, team paper); link each card to Method N / heuristic as evidence, variant or contradiction;
note new-pattern candidates. Never read references/sources/private/. Do not edit SKILL.md, INDEX.md or other
batches — synthesis is a separate step.
Report: cards written, method links, new-pattern candidates, papers you could not read and why.
```

## What is still missing

- **Works with no open full text** have abstract or metadata cards only: [TODO: count in scope, total and per member (Abstract only + Metadata only, from the Coverage table); team-integrate.js (T3.8)]. Their evidence carries less weight in the syntheses.
- **Book bodies** are rarely open, so no book chapter is read unless it is: [TODO: per book, what was read (table of contents, errata, addenda, preface, published reviews; T4) and what was refused or not found, logged as a lead; team-integrate.js (T3.8) from the B rows of INDEX.md and each 08's Open gaps].
- **Uneven periods.** [TODO: career periods with poor open coverage, with counts of open vs closed works per period, e.g. a member's early papers; team-integrate.js (T3.8) from INDEX.md]
- **Unreadable files** are listed on their cards: [TODO: member and card id for each, from the digests' read_level "unreadable"; team-integrate.js (T3.8)].

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses.
3. **Put it in `<researcher>/references/sources/papers/`.** This folder is git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** Use `python3 scripts/acquire_fulltexts.py product/{{TEAM_SLUG}}/<researcher> --only <ID>`. It extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. Run it in the checkout that holds the other papers' PDFs and `txt/`: rows without local files keep their committed status, but their quotes cannot be re-verified.
5. **Card and fold it in.** Either run `team-increment.js` (T4; see `scripts/workflows/README.md`), which cards the new material, folds it into the skill, verifies and fixes; or by hand: plan a new round with `plan_reading_batches.py … --round <next> --no-abstract --exclude <earlier plan files, comma-separated>`, read with the brief above, run `verify_card_quotes.py` and `mark_read_from_cards.py`, add the card's row to `07-paper-cards.md` from its digest fields, and apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`.
6. **Refresh the numbers.** Re-run `python3 scripts/team_status.py product/{{TEAM_SLUG}} --coverage`, paste it unchanged into the Coverage table here, and update the five-column summary in the team README from it (or run `team-integrate.js`, which does both).

## Privacy and integrity

- Private materials stay in each member's `references/sources/private/` (git-ignored) and are never read into public files. The deep reading works only from public sources.
- PDFs and extracted text are git-ignored for copyright reasons. Only indexes, abstracts, cards and syntheses are committed.
- Full texts come only from legitimate open copies: arXiv, Unpaywall, author pages, institutional report series and open repositories.
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`.
