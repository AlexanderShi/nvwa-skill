<!-- Team template (member resource tracker) → product/<team>/<member>/references/sources/RESOURCES.md.
     T0: scripts/new_team.py fills the double-brace placeholders.
     T1: scripts/workflows/team-base-skills.js adds one row per source found by research agents 01–06.
     T3: the deep-tier workflows add the rows for the publication list, full-text index, cards, synthesis and technique catalog
         (team-harvest.js, team-read.js, team-synthesize.js) and upgrade ⚠️ leads the full texts confirm.
     T4: scripts/workflows/team-increment.js adds book material and new papers.
     Open work: grep -n "TODO" RESOURCES.md. See product/dfo-team for a worked example (<member>/references/sources/RESOURCES.md). -->

# {{MEMBER_NAME}} · Resource Tracker

Every source behind the `{{MEMBER_SLUG}}` skill, plus anything you add later. One row per resource.

**Status**: ✅ verified (title/authors/venue/year confirmed by search) · ⚠️ unverified (lead only — do not cite) · 📥 saved locally in this folder

Research date: [TODO: date of the first pass, and how the ✅ rows were verified (web-search result snippets, a primary bibliography, the full text); team-base-skills.js (T1)]

| # | Type | Title | Authors | Year | Venue / Where | Link / DOI / arXiv | Status | Used in | Notes |
|---|------|-------|---------|------|---------------|--------------------|--------|---------|-------|
| 1 | profile | Google Scholar publication list of {{MEMBER_NAME}} | — | — | Google Scholar | {{SCHOLAR_URL}} | ⚠️ | — | Seed for the harvest (T3.1). [TODO: when team-harvest.js has built `publications/works.json` and `scholar.md`, set ✅, give the row counts (Scholar rows, distinct works, index-only and homepage-only works) and point to the audit notes] |
| 2 | [TODO: type] | [TODO: one row per source found in the T1 research (notes 01 publications, 02 stated method, 03 process evidence, 04 mentorship, 05 critique, 06 trajectory): papers, books, technical reports, software, talks, interviews, essays, memoirs, student recollections, critiques, profiles. Verify each one with a tool; a source you could not verify stays ⚠️ with the reason in Notes; team-base-skills.js (T1)] | | | | | | | | |
| 3 | [TODO: profile] | [TODO: deep-tier rows, added by T3: the full-text index (`papers/INDEX.md`: counts of txt and no-oa, git-ignored texts); the paper cards (`../research/07-paper-cards.md`: counts per read level, quotes verified); the deep-reading synthesis (`../research/08-deep-reading-synthesis.md`) and the technique catalog (`../technique-catalog.md`). T4 adds one row per book-material item (table of contents, errata, addendum, preface, published review) with its card id.] | | | | | | | | |

**Types**: paper · book · tech-report · software · talk · interview · essay · memoir/obituary · student-recollection · critique · profile (add a type when a source needs one, e.g. book-toc, errata, review)

## Folders

| Folder | What goes there |
|--------|-----------------|
| `publications/` | Publication landscape: `works.json` and `scholar.md` from the harvest (T3.1), the output of `scripts/fetch_publications.py`, or a hand-built list |
| `papers/` | Full texts you download. PDFs are git-ignored — keep copyrighted files local |
| `talks/` | Talk transcripts, slides, lecture notes |
| `essays/` | Methodology writings, surveys, prefaces, advice pieces |
| `software/` | Notes on the researcher's software and code (repo links, versions, docs) |
| `private/` | Git-ignored. Non-public material from your own work with the researcher; only its README is tracked, and nothing in it is read or quoted unless you add it and ask |

## Adding a resource

1. Add a row to the table (keep numbering).
2. If you save a file, put it in the matching folder and mark it 📥.
3. If it changes a method or claim in `SKILL.md`, note which research file (`../research/0X-*.md`) you updated in **Used in**.
