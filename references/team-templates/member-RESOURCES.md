<!-- Team template (member resource tracker) → product/<team>/<member>/references/sources/RESOURCES.md.
     T0: scripts/new_team.py fills the double-brace placeholders. With no Scholar id in team.json, row 1's Link reads
         "— (no Scholar profile in team.json; list from DBLP/homepage)" ("—" with --base-tier) until the harvest rewrites it.
     T1: scripts/workflows/team-base-skills.js adds one row per source found by research agents 01–06.
     T3: team-harvest.js (T3.1) rewrites row 1 completely; team-synthesize.js (T3.6) replaces the deep-tier placeholder row
         with the real rows (full-text index, cards, synthesis, ledger, technique catalog), or appends them when a
         base-tier file has no placeholder row, and upgrades ⚠️ leads the full texts confirm. After T3 no TODO item may
         remain in this file.
     Base tier (new_team.py --base-tier at T0, or team-layer.js with deep_tier: false at T2; no deep reading planned): row 1 keeps Status ⚠️, its Link cell becomes
         "—" when it still holds a TODO item or the "— (no Scholar profile in team.json; …)" scaffold text (a real profile
         URL stays), and its Notes become "not harvested (base tier)"; the deep-tier placeholder row is deleted. Upgrading
         to the deep tier later: this file keeps its base-tier form until T3.1 rewrites row 1 and T3.6 appends the deep-tier rows.
     T4: scripts/workflows/team-increment.js adds book material and new papers.
     Open work: grep -n "TODO" RESOURCES.md. See product/dfo-team for a worked example (<member>/references/sources/RESOURCES.md). -->

# {{MEMBER_NAME}} · Resource Tracker

Every source behind the `{{MEMBER_SLUG}}` skill, plus anything you add later. One row per resource.

**Status**: ✅ verified (title/authors/venue/year confirmed by search) · ⚠️ unverified (lead only — do not cite) · 📥 saved locally in this folder

Research date: [TODO: date of the first pass, and how the ✅ rows were verified (web-search result snippets, a primary bibliography, the full text); team-base-skills.js (T1)]

| # | Type | Title | Authors | Year | Venue / Where | Link / DOI / arXiv | Status | Used in | Notes |
|---|------|-------|---------|------|---------------|--------------------|--------|---------|-------|
| 1 | profile | Publication list of {{MEMBER_NAME}} (Google Scholar; DBLP and the homepage CV when there is no Scholar profile) | — | — | Google Scholar / DBLP | {{SCHOLAR_URL}} | ⚠️ | — | Seed for the harvest (T3.1). [TODO: team-harvest.js (T3.1) rewrites this whole row, this note included: Status ✅; Link = the list actually used (the Scholar profile URL, or the DBLP person page plus the homepage list when there is no profile); Notes = the counts (Scholar rows, distinct works, DBLP-only and homepage-only works) and "publications/works.json + scholar.md, audited <date>". Base tier: see the comment at the top] |
| 2 | [TODO: type] | [TODO: one row per source found in the T1 research (notes 01 publications, 02 stated method, 03 process evidence, 04 mentorship, 05 critique, 06 trajectory): papers, books, technical reports, software, talks, interviews, essays, memoirs, student recollections, critiques, profiles. Verify each one with a tool; a source you could not verify stays ⚠️ with the reason in Notes; team-base-skills.js (T1)] | | | | | | | | |
| 3 | [TODO: type] | [TODO: placeholder for the deep-tier rows. team-synthesize.js (T3.6) replaces this whole row with real rows: the full-text index (`papers/INDEX.md`: counts of txt and no-oa; the texts stay local); the paper cards (`../research/07-paper-cards.md`: counts per read level, quotes verified); the deep-reading synthesis (`../research/08-deep-reading-synthesis.md`), the evidence ledger (`../research/09-evidence-ledger.md`) and the technique catalog (`../technique-catalog.md`). Row 1 already covers the publication list. T4 later adds one row per book-material item (table of contents, errata, addendum, preface, published review) with its card id. Base tier: delete this row] | | | | | | | | |

**Types**: paper · book · tech-report · software · talk · interview · essay · memoir/obituary · student-recollection · critique · profile (add a type when a source needs one, e.g. book-toc, errata, review)

## Folders

| Folder | What goes there |
|--------|-----------------|
| `publications/` | Publication landscape: `works.json` and `scholar.md` from the harvest (T3.1), the output of `scripts/fetch_publications.py`, or a hand-built list |
| `papers/` | Full texts you download and their extracted `txt/`. They stay local (git-ignored) |
| `talks/` | Talk transcripts, slides, lecture notes. Your own notes and links are committed; slide decks and other copyrighted files stay local |
| `essays/` | Methodology writings, surveys, prefaces, advice pieces. Copyrighted files stay local |
| `software/` | Notes on the researcher's software and code (repo links, versions, docs) |
| `private/` | Git-ignored. Non-public material from your own work with the researcher; only its README is tracked, and nothing in it is read or quoted unless you add it and ask |

## Adding a resource

1. Add a row to the table (keep numbering).
2. If you save a file, put it in the matching folder and mark it 📥. A copyrighted file (PDF, PostScript, DjVu, EPUB, slides) stays local in every folder, not only `papers/`. The repository's `.gitignore` keeps PDF, PostScript, DjVu and EPUB files anywhere under `references/sources/`, and `papers/txt/`, out of git, but not slides (`.ppt`, `.pptx`, `.key`) or other formats, so check `git status` before you commit.
3. If it changes a method or claim in `SKILL.md`, note which research file (`../research/0X-*.md`) you updated in **Used in**.
