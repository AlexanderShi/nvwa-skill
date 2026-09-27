# Deep reading · all five DFO team skills

This is the record of how `michael-powell`, `andrew-conn`, `katya-scheinberg`, `luis-nunes-vicente` and `charles-audet` were deepened. Each researcher's Google Scholar publications were read in full or in part wherever an open copy exists, and not just as search snippets.

## Status (2026-09-27)

**Complete.** The deep reading covered every researcher's publication list:

- Every work on each researcher's Google Scholar profile is indexed.
- 415 of the 421 open full texts were read in full or in part. Five files turned out to be unreadable (each card says why) and one row was skipped.
- Every indexed research work of the researcher has at least one paper card, at full, partial, abstract or metadata level. In total there are 795 cards on 785 items in 116 batch files: 766 research works plus 19 book-material items (10 works have two cards). The 72 skipped rows (patents, talks and rows that are not the researcher's work) have none.
- All 1,139 verbatim quotes on the cards were checked against the extracted text, and all of them pass.
- The openly available book material was read and carded (batch `k01` in each of the four book authors' skills):
  - for *Introduction to Derivative-Free Optimization*: the table of contents, both errata lists (05/17/2015), the 2011 addendum on quadratic-regression bounds, and the reviews by J. L. Nazareth (*Math. Comp.* 2010) and Dominique Orban (*SIAM Review* 2011);
  - for Audet–Hare, *Derivative-Free and Blackbox Optimization*: the 2nd-edition front matter (preface and contents, 22 pp).

  The book bodies are not open and were not read. Each skill's `08-deep-reading-synthesis.md` has a "Book material" section, and each `09-evidence-ledger.md` has a `#book-material` anchor.
- The cards were then distilled into each `SKILL.md`.

What changed in the skills:

| Skill | Core methods | Change from the deep reading |
|---|---|---|
| `michael-powell` | 7 | New **M7 · Settle claims with the smallest decisive case** |
| `andrew-conn` | 7 | New **M7 · Audit your own released solver; its named weaknesses are the next agenda** |
| `katya-scheinberg` | 6 | Unchanged count. A proposed M7 was demoted to Heuristic 8 on review |
| `luis-nunes-vicente` | 5 | Unchanged count. A proposed M6, "publish the boundary", was demoted to H10 |
| `charles-audet` | 7 | New **M7 · Generalize, then inherit** |

Each skill also gained the following files:

- `references/technique-catalog.md`: transferable proof, design, experiment and writing devices, each with card references.
- `references/research/08-deep-reading-synthesis.md`: patterns, promotions and corrections.
- `references/research/09-evidence-ledger.md`: the full evidence, moved out of `SKILL.md` when it was tightened. `SKILL.md` links to its anchors.

In `dfo-roundtable`, fault line 4 (globalization in direct search) now records Vicente's own history from the cards.

## Pipeline actually used

1. **Publication list.** The Google Scholar profiles were read page by page with a fetch tool (WebFetch). Scholar blocks `curl` and has no API, and OpenAlex was rate-limited, so `scripts/fetch_publications.py` was not used.
   - Each list was cross-checked with DBLP through its SPARQL endpoint, because the DBLP REST API was behind a bot wall. Crossref and DataCite/arXiv were also used, plus author homepages, zbMATH, the GERAD Cahiers and Audet's own bibliography where they helped.
   - The outputs are `references/sources/publications/works.json` (all records, including duplicates marked `dup_of`) and `scholar.md` (the readable list and audit notes).
   - IDs: `S` = Scholar row · `D` = DBLP or other index only · `H` = author homepage only · `X` = Powell's two interviews · `R` = the Royal Society biographical memoir of Powell (by Buhmann, Fletcher, Iserles and Toint).
2. **Open full texts.** `scripts/acquire_fulltexts.py` tries the following sources in order:
   1. arXiv, by ID or by title search on arxiv.org/search.
   2. Unpaywall open-access copies.
   3. Author or repository links listed in `works.json`.

   It checks that each download is a PDF and that its first pages carry the title. Otherwise the file is dropped as a mismatch. It extracts the text with `[[page N]]` markers and falls back to tesseract OCR for scans and garbled font layers. The results go into `references/sources/papers/INDEX.md` and `abstracts.json`.
3. **Agent search of open repositories.** For works that were still `no-oa`, agents searched legitimate open sources:
   - author homepages;
   - RAL ePubs;
   - Namur (FUNDP), Waterloo, Cornell, Rice, Columbia and GERAD technical reports;
   - DAMTP NA reports (over http);
   - Optimization Online, HAL, JMLR/NeurIPS/PMLR, OSTI and CORE.

   Files found this way were saved under the index naming scheme and re-indexed by `acquire_fulltexts.py`, which records `Source = manual` (or `DAMTP report`). **Never Sci-Hub, never paywall circumvention.**
4. **Reading batches.** `scripts/plan_reading_batches.py` sets each row's Role and splits the papers into batches:
   - **core**: full read, at most 5 papers or 110 pages per batch;
   - **supplement**: selective read, at most 8 papers or 220 pages;
   - **book**: over 150 pages, read chapter by chapter;
   - **abstract**: no full text, so an abstract or metadata card only, 30 per batch.

   The script ran in several rounds as new full texts turned up. The last round emitted the abstract batches. Batch IDs are `c01`, `s02`, … in round 1 and `c2-01`, `a2-03`, `s4-01`, … in later rounds.
5. **Cards.** One agent per batch wrote `references/research/cards/<batch>.md` and `<batch>.digest.json` using the brief below. `07-paper-cards.md` indexes every card.
6. **Quote check.** `scripts/verify_card_quotes.py` looked up every quoted passage (`quotes[].text` in the digests) in the extracted text or abstract. All 1,139 are exact matches.
7. **Read column.** `scripts/mark_read_from_cards.py` filled INDEX.md's Read column from each card's `read_level`:
   - `full` → `carded`
   - `partial` → `skimmed`
   - `abstract` → `abstract`
   - `metadata` → `metadata`
   - `unreadable` → `unreadable`
8. **Synthesis.** Each researcher went through four steps, with the conservative-update rules of `references/paper-reading-card.md` §3:
   1. One agent mined the cards into `08-deep-reading-synthesis.md`.
   2. A conservative edit of `SKILL.md` followed. Existing methods get evidence first. A new method needs 3 or more distinct papers plus the four checks.
   3. Three read-only skeptics reviewed the edit.
   4. The verified objections were fixed.

   `SKILL.md` was then tightened, with the long evidence moved to `09-evidence-ledger.md`, and `quality_check.py` was re-run.

### Commands, per researcher

Run these from the repository root. Needs network access to arxiv.org, api.unpaywall.org and api.crossref.org, plus `pypdfium2` and Pillow; `tesseract` is needed for OCR.

```bash
R=katya-scheinberg   # also: michael-powell, andrew-conn, luis-nunes-vicente, charles-audet
# (works.json + scholar.md were built by hand from Google Scholar, DBLP SPARQL, Crossref, DataCite/arXiv)

# 1. Open full texts + INDEX.md (PDFs and txt/ are git-ignored; INDEX.md and abstracts.json are committed)
#    Rows whose PDF/txt is not on disk keep their committed txt/pdf status, but re-extraction and the
#    quote check need the original files. An older copy of the script reset those rows to no-oa; if that
#    happens, restore with: git checkout -- product/dfo-team/$R/references/sources/papers/INDEX.md
python3 scripts/acquire_fulltexts.py product/dfo-team/$R

# 2. Roles + reading batches (plan JSON kept outside the repo); one round per wave of new full texts
python3 scripts/plan_reading_batches.py product/dfo-team/$R --no-abstract > /tmp/$R-round1.json
python3 scripts/plan_reading_batches.py product/dfo-team/$R --round 2 --exclude /tmp/$R-round1.json > /tmp/$R-round2.json
#    ... last round without --no-abstract, so the remaining works get abstract/metadata batches

# 3. After the cards are written: check every quote, then fill the Read column
python3 scripts/verify_card_quotes.py product/dfo-team/$R
python3 scripts/mark_read_from_cards.py product/dfo-team/$R

# 4. After synthesis
python3 scripts/quality_check.py product/dfo-team/$R/SKILL.md
```

## Coverage

These counts are exact and were computed from each researcher's `references/sources/papers/INDEX.md`.

| Researcher | Scholar rows | Distinct works indexed | Open full text | Read in full | Read in part | Abstract only | Metadata only (incl. unreadable) | Skipped (not the author's / non-research) | Book material carded | Quotes verified |
|---|---|---|---|---|---|---|---|---|---|---|
| M. J. D. Powell | 211 | 187 | 39 | 34 | 5 | 73 | 75 | 0 | 0 | 193 |
| Andrew R. Conn | 237 | 183 | 72 | 53 | 18 | 50 | 17 | 45 | 6 | 200 |
| Katya Scheinberg | 143 | 132 | 85 | 68 | 14 | 19 | 23 | 8 | 6 | 196 |
| Luís Nunes Vicente | 122 | 124 | 108 | 92 | 16 | 11 | 5 | 0 | 6 | 232 |
| Charles Audet | 222 | 212 | 117 | 109 | 6 | 56 | 22 | 19 | 1 | 318 |
| **Total** | 935 | 838 | 421 | 356 | 59 | 209 | 142 | 72 | 19 | 1139 |

Notes:

- *Distinct works indexed* = Scholar rows minus duplicates, plus items found only in DBLP or on a homepage. For Powell it also includes the two interviews and the Royal Society memoir. Powell's open full texts include those three non-Scholar sources and one duplicate report, and his 34 full reads include the two interviews and the memoir.
- *Read in part* means the supplement reading: abstract, introduction, algorithm, main theorem, experimental setup and conclusion. For a multi-author volume it means only the researcher's own section.
- *Book material carded* counts the `B` rows in INDEX.md: openly available parts of a book (table of contents, errata, addendum, preface, published reviews). They are not counted in the research-work columns. The three IDFO authors share the same six items.
- *Skipped* rows have Role `skip` in INDEX.md and no card. They are rows that are not the researcher's work, such as referee lists, report sections, misattributed rows and unresolved fragments, plus patents, talks and conference duplicates of journal papers. Each skill's `08-deep-reading-synthesis.md` §1 counts them.
- Page references on cards are pages of the text version that was read, often a technical report or preprint. Check the journal page before citing one in a paper.

## Reading-batch brief (as used, shortened)

```
You are deepening the research-craft skill at product/dfo-team/{R}/ by reading full texts.
Read first: references/paper-reading-card.md (card format, roles, rules) and {R}/SKILL.md
(methods, heuristics, taste marks, workflows — you link cards to their numbers).
Batch {bid} ({core | supplement | book | abstract}): {papers from the plan JSON: ID, year, title, venue,
role, pages, txt path}. Texts are in references/sources/papers/txt/, abstracts in abstracts.json.
Write references/research/cards/{bid}.md. Open it with: batch intent (one line), focus dimensions (D1–D8),
material roles, and how file pages map to printed pages. Then one card per paper:
  core → every dimension from the whole text; supplement → abstract, introduction, algorithm, main theorem,
  experimental setup, conclusion; book → chapter level; abstract → from the abstract, or metadata only — say which.
Write references/research/cards/{bid}.digest.json: one object per card (fields: see paper-reading-card.md §四).
Rules: a page reference ([[page N]] markers) on every claim; at most two quotes per card, verbatim, with page —
they must pass scripts/verify_card_quotes.py; write "not read" rather than guess; say when the researcher's role
is unclear (middle author, team paper); link each card to Method N / heuristic as evidence, variant or contradiction;
note new-pattern candidates. Do not edit SKILL.md, INDEX.md or other batches — synthesis is a separate step.
Report: cards written, method links, new-pattern candidates, papers you could not read and why.
```

## What is still missing

- **Works with no open full text** have abstract or metadata cards only. There are 346 in scope: Powell 148, Conn 66, Scheinberg 40, Vicente 16 and Audet 76. Their evidence carries less weight in the syntheses.
- **Book bodies** are not openly available, so no book chapter was read:
  - Conn–Gould–Toint, *Trust-Region Methods* (SIAM 2000) and *LANCELOT* (Springer 1992): abstract or metadata cards only. The SIAM front matter of *Trust-Region Methods* was refused with 403.
  - Conn–Scheinberg–Vicente, *Introduction to Derivative-Free Optimization* (SIAM 2009), which appears on three lists: the table of contents, both errata lists, the 2011 addendum and two published reviews were read (cards `k01`). The chapters themselves were not. A third review (MAA Reviews, 2009) returned 404 and is logged as a lead.
  - Audet–Hare, *Derivative-Free and Blackbox Optimization* (Springer 2017, metadata-level): for the 2nd edition (2026), the front matter (preface and contents) was read (card `k01`). The chapters were not.
  - Powell, *Approximation Theory and Methods* (CUP 1981): metadata only.
- **Powell's pre-1994 papers.** 129 of his 148 no-oa works are from before 1994. They include:
  - the 1964 conjugate-direction method;
  - the 1969 augmented-Lagrangian paper;
  - the 1977 conjugate-gradient restarts paper;
  - the 1978 paper "A fast algorithm for nonlinearly constrained optimization calculations".

  The 1994 COBYLA paper is also closed. His derivative-free period is read far better than his earlier work: 31 of the 49 dated index rows from 1994 on have open text (28 of his 46 works, plus the two interviews and the memoir; one undated society notice, S211, has none), against 8 of 137 before 1994.
- **Five unreadable files** are listed on their cards: Conn S093, Scheinberg S067 and S133, Audet S025 and S067.

### How to extend

1. **Get a legitimate copy.** Sources are a library, publisher access or the author.
2. **Name the file like the index.** Use `<ID>-<year>-<first eight title words, lowercased, hyphenated>.pdf`, the stem `acquire_fulltexts.py` uses. For example, `S025-2002-uobyqa-unconstrained-optimization-by-quadratic-approximation.pdf`.
3. **Put it in `<researcher>/references/sources/papers/`.** This folder is git-ignored. Check by hand that the file is the paper, because the title check only runs on downloads.
4. **Re-run the acquire script.** Use `python3 scripts/acquire_fulltexts.py product/dfo-team/<researcher> --only <ID>`. It extracts the text, OCRs scans, and sets `Full text = txt` and `Source = manual`. Run it in the checkout that holds the other papers' PDFs and `txt/`: rows without local files keep their committed status, but their quotes cannot be re-verified. If an older copy of the script reset those rows to `no-oa`, restore the index with `git checkout -- <researcher>/references/sources/papers/INDEX.md`.
5. **Plan a new round.** Use `python3 scripts/plan_reading_batches.py product/dfo-team/<researcher> --round <next> --no-abstract --exclude /tmp/<researcher>-round1.json,… > /tmp/<researcher>-round<next>.json` (`--exclude` takes the earlier rounds' plan files, comma-separated), keeping the plan JSON outside the repository. Works that have text but only an abstract or metadata card are batched again.
6. **Read with the brief above.** Then run `verify_card_quotes.py` and `mark_read_from_cards.py`, and add the card's row to `07-paper-cards.md` by hand from its digest fields (id, year, title, read_level, batch file, method_links, contribution), in the format of the neighbouring rows (the indexes were first built by one-off scripts; none ships). Then apply the conservative-update rules to `SKILL.md`, `09-evidence-ledger.md` and `technique-catalog.md`.

## Privacy and integrity

- Private materials stay in `katya-scheinberg/references/sources/private/` (git-ignored) and are never read into public files. The deep reading worked only from public sources.
- PDFs and extracted text are git-ignored for copyright reasons. Only indexes, abstracts, cards and syntheses are committed.
- Full texts came only from legitimate open copies: arXiv, Unpaywall, author pages, institutional report series and open repositories.
- The integrity rules in each skill still apply. No claim goes in without a page reference, and no quote is invented: every quote on a card passes `scripts/verify_card_quotes.py`.
