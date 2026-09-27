# Charles Audet · Resource Tracker

Every source behind the `charles-audet` skill, plus anything you add later. One row per resource.

**Status**: ✅ verified (title/authors/venue/year confirmed by search) · ⚠️ unverified (lead only — do not cite) · 📥 saved locally in this folder

Verification channel for ✅ rows: **(S)** a web-search result showed title + authors + year (+ venue); **(B)** the group-maintained primary bibliography `bbopt/bibtex/bibliography.bib` (fetched 2026-09-27) lists the entry with DOI or report number; **(S+B)** both. Research date 2026-09-27; about 25 web searches were run before the session's shared search budget ran out (first pass).

Update 2026-09-27 (full-text reading): the Google Scholar list was harvested into `publications/` (212 distinct works) and 110 of them were read in full or in part into paper cards (rows 49–52). PDFs and extracted texts are saved locally in `papers/` but are git-ignored (copyright); only `papers/INDEX.md` is committed. Rows 4, 7, 25, 35 and 48 are updated from the full texts; row 44 is checked against the Scholar list.

| # | Type | Title | Authors | Year | Venue / Where | Link / DOI / arXiv | Status | Used in | Notes |
|---|------|-------|---------|------|---------------|--------------------|--------|---------|-------|
| 1 | profile | Charles Audet — GERAD people page; Polytechnique expert directory | — | 2026 | gerad.ca; polymtl.ca | https://www.gerad.ca/en/people/charles-audet ; https://www.polymtl.ca/expertises/en/audet-charles | ✅ (S) | 01, 06 | Position, PhD (Polytechnique), Rice post-doc, research interests; secondary |
| 2 | paper | Pattern search algorithms for mixed variable programming | C. Audet, J.E. Dennis Jr. | 2001 | SIAM J. Optim. 11(3):573–594 | https://doi.org/10.1137/S1052623499352024 | ✅ (B) | 01, 03, 06 |  |
| 3 | paper | Analysis of generalized pattern searches | C. Audet, J.E. Dennis Jr. | 2003 | SIAM J. Optim. 13:889–903 | https://doi.org/10.1137/S1052623400378742 | ✅ (S+B) | 01, 02, SKILL |  |
| 4 | paper | Convergence results for generalized pattern search algorithms are tight | C. Audet | 2004 | Optimization and Engineering 5:101–122 | https://doi.org/10.1023/B:OPTE.0000033370.66768.a9 | ✅ (S+B) | 01, 02, 05, SKILL | Six small counterexamples (per abstract; journal text not read). Its precursor, Rice CRPC-TR98779 (Nov 1998, three examples), was read via OCR: card S025 |
| 5 | paper | A pattern search filter method for nonlinear programming without derivatives | C. Audet, J.E. Dennis Jr. | 2004 | SIAM J. Optim. 14(4):980–1010 | https://doi.org/10.1137/S105262340138983X | ✅ (B) | 01, 03 |  |
| 6 | paper | Mesh adaptive direct search algorithms for constrained optimization | C. Audet, J.E. Dennis Jr. | 2006 | SIAM J. Optim. 17(1):188–217 | https://doi.org/10.1137/040603371 | ✅ (S+B) | 01, SKILL | Signature work |
| 7 | paper | Erratum: Mesh adaptive direct search algorithms for constrained optimization | C. Audet, A.L. Custódio, J.E. Dennis Jr. | 2008 | SIAM J. Optim. 18(4):1501–1503 | https://doi.org/10.1137/060671267 | ✅ (B) 📥 | 01, 05, SKILL | Read in full (card D001): a proof erratum; the statement of Prop. 4.2 was correct (p. 1) |
| 8 | paper | Finding optimal algorithmic parameters using derivative-free optimization | C. Audet, D. Orban | 2006 | SIAM J. Optim. 17(3):642–664 | https://doi.org/10.1137/040620886 | ✅ (B) | 03, SKILL | Algorithms as blackboxes |
| 9 | paper | Multiobjective optimization through a series of single-objective formulations (BiMADS) | C. Audet, G. Savard, W. Zghal | 2008 | SIAM J. Optim. 19(1):188–210 | https://doi.org/10.1137/060677513 | ✅ (S+B) | 01, 02 |  |
| 10 | paper | Nonsmooth optimization through Mesh Adaptive Direct Search and Variable Neighborhood Search (STYRENE) | C. Audet, V. Béchard, S. Le Digabel | 2008 | J. Global Optim. 41(2):299–318 | https://doi.org/10.1007/s10898-007-9234-1 | ✅ (S+B) | 03, 04 |  |
| 11 | paper | A progressive barrier for derivative-free nonlinear programming | C. Audet, J.E. Dennis Jr. | 2009 | SIAM J. Optim. 20(1):445–472 | https://doi.org/10.1137/070692662 | ✅ (S+B) | 01, SKILL | Signature work |
| 12 | paper | OrthoMADS: A deterministic MADS instance with orthogonal directions | M.A. Abramson, C. Audet, J.E. Dennis Jr., S. Le Digabel | 2009 | SIAM J. Optim. 20(2):948–966 | https://doi.org/10.1137/080716980 | ✅ (S+B) | 01, 02, 05 |  |
| 13 | software paper | Algorithm 909: NOMAD: Nonlinear optimization with the MADS algorithm | S. Le Digabel | 2011 | ACM TOMS 37(4):44 | https://doi.org/10.1145/1916461.1916468 | ✅ (S) | 01, 03 | Not authored by Audet |
| 14 | paper | Trade-off studies in blackbox optimization | C. Audet, J.E. Dennis Jr., S. Le Digabel | 2012 | Optim. Methods Softw. 27(4–5):613–624 | https://doi.org/10.1080/10556788.2011.571687 | ✅ (B) | 01, SKILL |  |
| 15 | paper | Reducing the number of function evaluations in mesh adaptive direct search algorithms | C. Audet, A. Ianni, S. Le Digabel, C. Tribes | 2014 | SIAM J. Optim. 24(2):621–642 | https://doi.org/10.1137/120895056 | ✅ (B) | 05 | Quadratic models in search |
| 16 | essay/survey | A survey on direct search methods for blackbox optimization and their applications | C. Audet | 2014 | Mathematics Without Boundaries (Springer) | https://doi.org/10.1007/978-1-4939-1124-0_2 | ✅ (S+B) | 01, 02 |  |
| 17 | essay | Blackbox and derivative-free optimization: theory, algorithms and applications (editorial) | C. Audet, M. Kokkolaras | 2016 | Optimization and Engineering 17:1–2 | https://doi.org/10.1007/s11081-016-9307-4 | ✅ (S+B) | 02 |  |
| 18 | book | Derivative-Free and Blackbox Optimization | C. Audet, W. Hare | 2017 | Springer ORFE | https://doi.org/10.1007/978-3-319-68913-5 | ✅ (S+B) | 02, 04, SKILL | Preface not read |
| 19 | book | Derivative-Free and Blackbox Optimization, 2nd edition | C. Audet, W. Hare | 2026 | Springer ORFE | https://doi.org/10.1007/978-3-032-00906-7 | ✅ (S+B) | 02, 06, SKILL | eBook 17 June 2026; ch. 4 'Comparing Optimization Methods' |
| 20 | critique/review | Book review of Audet & Hare (Optimization and Engineering) | M. Kokkolaras | 2019 | Optimization and Engineering 20 | https://doi.org/10.1007/s11081-019-09422-9 | ✅ (S) | 02, 04, 05 | Reviewer is a frequent co-author (not independent) |
| 21 | paper | A progressive barrier derivative-free trust-region algorithm for constrained optimization | C. Audet, A.R. Conn, S. Le Digabel, M. Peyrega | 2018 | Comput. Optim. Appl. 71:307–329 | https://doi.org/10.1007/s10589-018-0020-4 | ✅ (S+B) | 03, 05, SKILL | Compared with COBYLA and NOMAD |
| 22 | paper | Efficient solution of quadratically constrained quadratic subproblems within a direct-search algorithm | N. Amaioua, C. Audet, A.R. Conn, S. Le Digabel | 2018 | EJOR | https://doi.org/10.1016/j.ejor.2017.10.058 | ✅ (B) | 04, 05 |  |
| 23 | paper | Binary, unrelaxable and hidden constraints in blackbox optimization | C. Audet, G. Caporossi, S. Jacquet | 2020 | Oper. Res. Lett. 48(4):467–471 | https://doi.org/10.1016/j.orl.2020.05.011 | ✅ (B) | 02, 03, SKILL |  |
| 24 | paper | Stochastic mesh adaptive direct search for blackbox optimization using probabilistic estimates (StoMADS) | C. Audet, K.J. Dzahini, M. Kokkolaras, S. Le Digabel | 2021 | Comput. Optim. Appl. 79:1–34 | https://doi.org/10.1007/s10589-020-00249-0 | ✅ (S+B) | 03, 05, SKILL |  |
| 25 | paper | Two decades of blackbox optimization applications | S. Alarie, C. Audet, A.E. Gheribi, M. Kokkolaras, S. Le Digabel | 2021 | EURO J. Comput. Optim. 9:100011 | https://doi.org/10.1016/j.ejco.2021.100011 | ✅ (B) 📥 | 03, SKILL | Read in full (card S013) |
| 26 | paper | Performance indicators in multiobjective optimization | C. Audet, J. Bigeon, D. Cartier, S. Le Digabel, L. Salomon | 2021 | EJOR 292(2):397–422 | https://doi.org/10.1016/j.ejor.2020.11.016 | ✅ (S+B) | 03, 04 | 63 indicators |
| 27 | software paper | Algorithm 1027: NOMAD version 4: Nonlinear optimization with the MADS algorithm | C. Audet, S. Le Digabel, V. Rochon Montplaisir, C. Tribes | 2022 | ACM TOMS 48(3):35 | https://doi.org/10.1145/3544489 ; arXiv:2104.11627 | ✅ (S+B) | 01, 03, SKILL | Signature work |
| 28 | paper | Constrained blackbox optimization with the NOMAD solver on the COCO constrained test suite | C. Audet, S. Le Digabel, L. Salomon, C. Tribes | 2022 | GECCO Companion, 1683–1690 | https://doi.org/10.1145/3520304.3534019 | ✅ (B) | 03, 05 |  |
| 29 | paper | Counterexample and an additional revealing poll step for a result of 'analysis of direct searches for discontinuous functions' | C. Audet, P.-Y. Bouchet, L. Bourdin | 2024 | Math. Program. 208:411–424 | https://doi.org/10.1007/s10107-023-02042-3 ; arXiv:2211.09947 | ✅ (S+B) | 03, 05, SKILL | Targets Vicente & Custódio 2012 |
| 30 | paper | Convergence towards a local minimum by direct search methods with a covering step | C. Audet, P.-Y. Bouchet, L. Bourdin | 2025 | Optimization Letters | https://doi.org/10.1007/s11590-024-02165-2 ; arXiv:2401.07097 | ✅ (S+B) | 03, 06 |  |
| 31 | paper | solar: A solar thermal power plant simulator for blackbox optimization benchmarking | N. Andrés-Thiò, C. Audet, M. Diago, A.E. Gheribi, S. Le Digabel, X. Lebeuf, M. Lemyre Garneau, C. Tribes | 2024/2025 | Optimization and Engineering | https://doi.org/10.1007/s11081-024-09952-x ; arXiv:2406.00140 | ✅ (S+B) | 01, 03, SKILL | Hydro-Québec grant |
| 32 | tech-report | Adaptive direct search algorithms for constrained optimization (ADS) | C. Audet, T. Denorme, Y. Diouane, S. Le Digabel, C. Tribes | 2025 | GERAD / arXiv | arXiv:2507.23054 | ✅ (S+B) | 02, 05, 06 | One search summary misattributed authors to Bouchet/Bourdin; bib + NOMAD guide used |
| 33 | tech-report | Adaptive direct search algorithms with relaxable and quantifiable constraints (ADS-PB) | C. Audet, T. Denorme, Y. Diouane, S. Le Digabel, C. Tribes | 2026 | GERAD / arXiv | arXiv:2607.05183 | ✅ (S+B) | 06, SKILL |  |
| 34 | tech-report | A penalty-interior point method combined with MADS for equality and inequality constrained optimization | C. Audet, A. Brilli, Y. Diouane, S. Le Digabel, E.J. Silva, C. Tribes | 2026 | arXiv | arXiv:2601.20811 | ✅ (S+B) | 06 |  |
| 35 | paper | A summary of benchmarking constrained, multi-objective and surrogate-assisted optimization methods | C. Audet, W. Hare, C. Tribes | 2026 | Optimization Letters | https://doi.org/10.1007/s11590-026-02302-z | ✅ (S+B) 📥 | 02, 06, SKILL | Read in full as GERAD preprint G-2025-36 (card S128; twin S101) |
| 36 | tech-report | Benchmarking bilevel derivative-free optimization algorithms | C. Audet, V. Dijon, Y. Diouane | 2026 | GERAD G-2026-26 / arXiv | arXiv:2605.30531 | ✅ (B) | 06 |  |
| 37 | paper | Comparison of derivative-free optimization methods for groundwater supply and hydraulic capture community problems | K.R. Fowler, …, C. Audet, …, T.G. Kolda (15 authors) | 2008 | Adv. Water Resour. 31(5):743–757 | https://doi.org/10.1016/j.advwatres.2008.01.010 | ✅ (B) | 03 |  |
| 38 | software | NOMAD 4 user guide (source .rst files) | NOMAD team (Audet, Le Digabel, Rochon Montplaisir, Tribes) | 2026 | GitHub bbopt/nomad | https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst | ✅ 📥 | 02, 03, 05, SKILL | Verbatim excerpts in software/nomad-and-bbopt-notes.md |
| 39 | software | bbopt GitHub organisation (NOMAD, styrene, solar, aircraft_range, Cat-Suite, RunnerPost, StoMADS, Micro-PRIAD, bibtex …) | NOMAD / GERAD team | 2016–2026 | GitHub | https://github.com/bbopt | ✅ 📥 | 03, 04, SKILL | READMEs via raw.githubusercontent.com |
| 40 | publications | Group bibliography bibliography.bib (151 Audet entries extracted) | bbopt group | 2026-09-23 (last update) | GitHub bbopt/bibtex | https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib | ✅ 📥 | 01, 04, 06 | Extract: publications/audet-publications-bbopt-bib.md |
| 41 | paper | A taxonomy of constraints in black-box simulation-based optimization | S. Le Digabel, S.M. Wild | 2024 | Optimization and Engineering 25(2):1125–1143 | https://doi.org/10.1007/s11081-023-09839-3 ; arXiv:1505.07881 | ✅ (S+B) | 03, 05 | NOT an Audet paper; adopted in STYRENE README |
| 42 | paper | Direct-search methods in the year 2025: theoretical guarantees and algorithmic paradigms | K.J. Dzahini, F. Rinaldi, C.W. Royer, D. Zeffiro | 2025 | arXiv / ScienceDirect | arXiv:2403.05322 | ✅ (S) | 04, 05 | Secondary; first author is a former group PhD |
| 43 | paper | Analysis of direct searches for discontinuous functions | L.N. Vicente, A.L. Custódio | 2012 | Math. Program. 133:299–325 | (cited in the 2024 counterexample abstract) | ✅ (S, via citing abstract) | 05 | Target of Audet et al. 2024 |
| 44 | paper | Constrained stochastic blackbox optimization using a progressive barrier and probabilistic estimates | ⚠️ authors not seen | ~2023 | Math. Program. | https://link.springer.com/article/10.1007/s10107-022-01787-7 | ⚠️ | 01 | Likely Dzahini/Kokkolaras/Le Digabel; unverified. Not on Audet's Google Scholar list (212 works), so do not attribute it to Audet |
| 45 | paper | Non-convergence analysis of probabilistic direct search | ⚠️ unknown | 2026 | arXiv | arXiv:2606.01320 | ⚠️ | 05 | Do not cite |
| 46 | paper | Best practices for comparing optimization algorithms | Beiranvand, Hare, … ⚠️ | 2017 | ⚠️ venue unverified | arXiv:1709.08242 | ⚠️ | 05 | Hare, not Audet |
| 47 | interview/talk | Any Audet interview, plenary transcript or advice-to-students text | — | — | — | — | ⚠️ not found | Honest Boundary | Search budget exhausted; gerad.ca talks pages blocked. The 110 full texts read (rows 49–52) contain no first-person teaching material either; 19 talks on the Scholar list have no open text (`papers/INDEX.md`, role `skip`) |
| 48 | fact | Audet's PhD advisor and PhD year | C. Audet (thesis) | 1997 | École Polytechnique de Montréal | Google Scholar list (card S070) | ✅ 📥 | 06, SKILL | Resolved 2026-09-27 from the thesis jury page: directrice B. Jaumard, codirecteur G. Savard, November 1997 (S070 pp. 1–3) |
| 49 | publications | Charles Audet — publication list (Google Scholar profile + DBLP + Crossref + GERAD + bbopt BibTeX + Semantic Scholar): 222 Scholar rows, 196 distinct Scholar works + 16 others = 212 works | harvested for this skill | 2026 | `publications/scholar.md`, `publications/works.json` | https://scholar.google.com/citations?user=WuHBdIkAAAAJ | ✅ 📥 | 01, 07, SKILL | Re-audited 2026-09-27: every Scholar row matched; all 134 DOIs and 28 arXiv ids resolve |
| 50 | profile | Full-text index (per-work source, full-text status, role, read level) | generated by `scripts/acquire_fulltexts.py`, edited by hand | 2026 | `papers/INDEX.md` | — | ✅ 📥 | 07, 08, SKILL | PDFs and texts git-ignored; 19 rows marked `skip` |
| 51 | profile | Paper cards index: 193 cards (108 full, 6 partial, 2 unreadable as named, 57 abstract, 20 metadata) | this skill | 2026 | `../research/07-paper-cards.md`; cards in `../research/cards/` | — | ✅ | SKILL, 08 | Generated from `cards/*.digest.json`; 110 distinct works read in full or in part, 108 Audet-authored |
| 52 | profile | Deep-reading synthesis: evidence per method, corrections, promotion of Method 7, heuristics, technique inventory, trajectory, collaboration pattern | this skill | 2026 | `../research/08-deep-reading-synthesis.md`; techniques in `../technique-catalog.md` | — | ✅ | SKILL, 01, 06, technique-catalog | Every statement cites card ids with pages |

**Types**: paper · book · tech-report · software · talk · interview · essay · memoir/obituary · student-recollection · critique · profile

## Folders

| Folder | What goes there |
|--------|-----------------|
| `publications/` | Publication landscape (output of `scripts/fetch_publications.py`, or a hand-built list) |
| `papers/` | Full texts you download. PDFs are git-ignored — keep copyrighted files local |
| `talks/` | Talk transcripts, slides, lecture notes |
| `essays/` | Methodology writings, surveys, prefaces, advice pieces |
| `software/` | Notes on solvers and code (repo links, versions, docs) |

## Adding a resource

1. Add a row to the table (keep numbering).
2. If you save a file, put it in the matching folder and mark it 📥.
3. If it changes a method or claim in `SKILL.md`, note which research file (`../research/0X-*.md`) you updated in **Used in**.
