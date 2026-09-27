# 02 · Stated methodology (what Conn and co-authors SAID about method)

Research date: 2026-09-27. Source basis: search-result snippets only. **Important gap:** no methodology essay, interview transcript, talk recording or "how I do research" piece by Conn turned up. The stated evidence therefore comes from:
(a) Conn's own account in a 2015 career profile (quoted in the third person by the snippet),
(b) co-authored abstracts, book descriptions and prefaces, which state intent and motivation,
(c) descriptions by colleagues in obituaries and prize citations. These are labelled "others' description", not Conn's own statement.

Quotes are used only where a snippet showed the wording in quotation marks or identically across several results. Everything else is marked "(paraphrase)".

## Taste

| # | Statement | Source | Type / credibility |
|---|---|---|---|
| T1 | Conn's research was "typically motivated by algorithms, and included convergence analysis, theory, applications and software" (wording identical across several snippets). | Univ. of Waterloo C&O obituary, 2019 — https://uwaterloo.ca/combinatorics-and-optimization/news/andrew-conn-1946-2019 | Others' description (secondary, written by former colleagues) |
| T2 | Predominantly continuous nonlinear optimization, with "an ongoing interest in applications that involved linear and discrete problems" (paraphrase). Great interest in applying optimization to complex problems, "especially those involving simulation" (paraphrase). | Waterloo obituary; IBM researcher page — https://researcher.watson.ibm.com/researcher/view_person_subpage.php?id=3372 | Secondary |
| T3 | DFO methods matter because practitioners demand them. The 1997 survey discusses the motivation and "why they are in high demand by practitioners" (paraphrase). | CST 1997, Math. Programming 79:397–414, DOI 10.1007/BF02614326 | Co-authored abstract (primary, stated) |
| T4 | DFO methods should "efficiently and rigorously" solve problems. The absence of derivatives, often combined with noise or lack of smoothness, is the challenge (paraphrase of the publisher description). | *Introduction to Derivative-Free Optimization* (SIAM 2009) description — http://www.mat.uc.pt/~lnv/idfo/ ; https://books.google.com/books/about/Introduction_to_Derivative_Free_Optimiza.html?id=tGbUshriSyYC | Co-authored book description (primary, stated) |
| T5 | A reference work should serve practice as well as theory: *Trust-Region Methods* has "several practical comments and an entire chapter devoted to software and implementation issues" and a commented bibliography of 972 references (paraphrase). | CGT 2000, DOI 10.1137/1.9780898719857 — https://researchportal.unamur.be/en/publications/trust-region-methods/ | Book description (primary, stated) |

## Problem choice

| # | Statement | Source | Type |
|---|---|---|---|
| P1 | Problems find you through small acts of help. Conn's origin story for circuit tuning: an IBM EE colleague asked for minimax advice. Because of that exchange Conn was later suggested as "a relatively approachable mathematician" and invited to an internal circuit-tuning workshop (paraphrase; the snippet wording may not be verbatim). | "Profile: Andrew R. Conn", Mathematics Awareness Month 2015 (ASA) — https://ww2.amstat.org/mam/2015/highlighted/MAM2015profile_Conn.pdf | Conn's own account as reported in a profile (primary-ish) |
| P2 | He valued working "in an area rich in problems", with access to "extremely knowledgeable people both inside and outside IBM" (paraphrase). | Same MAM 2015 profile | Primary-ish |
| P3 | The industrial problem was stated in the user's terms: traditional circuit tuning was "slow, tedious, manual, and error-prone" (paraphrase). The aim was a tool that automates tuning and scales to far larger circuits. | MAM 2015 profile | Primary-ish |

## Idea generation / algorithm design

| # | Statement | Source | Type |
|---|---|---|---|
| I1 | Newer DFO algorithms are characterised by techniques that ensure suitable "geometric quality" of the models within a trust-region framework (paraphrase of abstract). | CST 1997, DOI 10.1007/BF02614326 | Co-authored abstract (stated) |
| I2 | The goal is a *general framework* for global convergence of a broad class of DFO trust-region methods (paraphrase of abstract). | CST 1997 in *Tributes to M. J. D. Powell* (CUP) — https://researchportal.unamur.be/en/publications/on-the-convergence-of-derivative-free-methods-for-unconstrained-o/ | Stated |
| I3 | Design for the evaluation budget and for noise: the 1996 algorithm "is constructed to require few evaluations of the objective function and is designed to be relatively insensitive to noise" (paraphrase of abstract). | Conn & Toint 1996, DOI 10.1007/978-1-4899-0289-4_3 | Stated |
| I4 | Exploit structure: the least-squares DFO framework is designed "to take advantage of the problem structure" by building a model for each residual (paraphrase). | Zhang, Conn, Scheinberg 2010, SIAM J. Optim. 20:3555–3576 | Stated |
| I5 | Cross the direct-search / model-based line: "exploits the flexibility of directional direct search methods to integrate quadratic models" (paraphrase). | Conn & Le Digabel 2013, DOI 10.1080/10556788.2011.623162 | Stated |
| I6 | Robust optimization of simulation-based functions is a bilevel DFO problem (paraphrase). | Conn & Vicente 2012, DOI 10.1080/10556788.2010.547579 | Stated |

## Experiments and judging results

| # | Statement | Source | Type |
|---|---|---|---|
| E1 | The purpose of a large test collection is to evaluate nonlinear optimization algorithms. Conn "originated the CUTE … methodology + test problem library" (paraphrase; others' description). | IBM researcher page / Waterloo obituary | Secondary |
| E2 | Software papers should compare the "relative merits of the options" through "intensive numerical tests" (paraphrase). | CGT 1996, DOI 10.1007/BF02592099 | Stated |
| E3 | "Using models improves the performance of the mesh-adaptive direct search algorithm significantly", shown by intensive numerical tests (paraphrase). | Conn & Le Digabel 2013 | Stated |

## Writing and organisation

| # | Statement | Source | Type |
|---|---|---|---|
| W1 | Books should be accessible to readers with a modest background in computational mathematics and also useful to researchers (paraphrase of the IDFO description). | SIAM/ACM DL record — https://dl.acm.org/doi/10.5555/1508119 | Stated |
| W2 | Long collaborations were a deliberate organisational mode: more than 20 papers by the CGT trio alone (others' description). | SIAM News obituary (M. L. Overton, 2019) | Secondary |

## Claims repeated three or more times (candidates for "true methodology")

- **Rigorous and practical together** (T1, T4, T5, I2, E2).
- **Practitioner demand drives the agenda** (T2, T3, P1–P3).
- **Model quality or geometry is the lever** (I1, I2, and the titles of CSV 2008 ×2 and CSV 2009).

## Missing (declared)

- No Conn-authored advice on PhD supervision, choosing topics, or writing style was found.
- No statement by Conn about what he considered *bad* research was found. Negative taste in the SKILL is **inferred from practice** and labelled as such.
