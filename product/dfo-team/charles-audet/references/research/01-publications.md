# 01 · Publications landscape and signature-work anatomy — Charles Audet

Research date: 2026-09-27. Method (first pass): web-search snippets (~25 searches before the session's shared search budget ran out) plus a primary, group-maintained BibTeX file fetched from GitHub. No full texts were read (arXiv, Springer, SIAM, ACM, GERAD, dblp and OpenAlex hosts were blocked by the egress proxy).

**Update 2026-09-27 (full-text reading).** The publication list is now a census of the Google Scholar profile, not a hand-built sample: the profile (https://scholar.google.com/citations?user=WuHBdIkAAAAJ) plus DBLP, Crossref, the GERAD list and the group BibTeX give 212 distinct works (`../sources/publications/scholar.md`, `works.json`). 110 of them were read in full or in part into paper cards (`07-paper-cards.md`; synthesis in `08-deep-reading-synthesis.md`; transferable techniques in `../technique-catalog.md`). See §4 for the coverage and the corrections box in §3 for what the full texts change in the anatomies below. The anatomies in `SKILL.md` are the current versions; the first-pass text below is kept as written.

Verification legend: **[S]** confirmed by a search result (title + authors + year, usually venue). **[B]** confirmed by the bbopt group bibliography (`bibliography.bib`, primary, with DOI). **[S+B]** both. Items marked ⚠️ are leads only.

Full hand-built list (151 entries with "Audet" in the author field): `../sources/publications/audet-publications-bbopt-bib.md`.
Source of that list: https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib (primary, group-maintained; may be incomplete).

---

## 1. Landscape

### 1.1 Identity (secondary, profile pages)
- Full professor, Department of Mathematics and Industrial Engineering, Polytechnique Montréal; member of GERAD. PhD in applied mathematics from École Polytechnique de Montréal; post-doc at Rice University (Houston). Research interests stated as "blackbox nonsmooth optimization" and "structured global optimization": pattern search (GPS, MADS) plus exact global methods for bilevel, quadratic, bilinear and integer programming. [S] https://www.gerad.ca/en/people/charles-audet ; https://www.polymtl.ca/expertises/en/audet-charles (secondary, institutional profile)
- PhD year and PhD advisor: ⚠️ not verified. The earliest bib entries (1997–2001) are all with P. Hansen, B. Jaumard, G. Savard, which suggests a GERAD global-optimization training (inference, not verified).
  - **Resolved 2026-09-27 (full text):** PhD thesis "Optimisation globale structurée : propriétés, équivalences et résolution", École Polytechnique de Montréal, November 1997; *directrice de recherche* B. Jaumard, *codirecteur* G. Savard; jury chaired by J. Gauvin, with P. Marcotte and J.-P. Vial (card S070, pp. 1–3). The Rice postdoc was an NSERC postdoctoral fellowship starting in 1998 (S025 TR p. 2; S015 p. 15).

### 1.2 Output by period (from the 151 bib entries) [B]

| Period | Entries | Dominant themes | Typical venues |
|---|---|---|---|
| 1997–2002 | 13 | bilevel ↔ mixed 0–1, disjoint bilinear, nonconvex QCQP branch-and-cut, enumeration of bimatrix-game equilibria; first pattern-search papers with Dennis (mixed variables 2001) | JOTA, Math. Programming, SISC, SIOPT |
| 2003–2009 | 41 | GPS analysis, tightness counterexamples, filter, MADS, second-order MADS, OrthoMADS, PSD-MADS, BiMADS, progressive barrier; extremal convex polygons with Hansen & Messine | SIOPT (dominant), OPTE, JOGO, DCG |
| 2010–2016 | 36 | applications (snow water equivalent, alloys, metamaterials, bioinformatics, hydropower), algorithm-parameter tuning (OPAL), trade-off studies, fewer evaluations via quadratic models, linear equalities, dynamic scaling; survey 2014; editorial 2016 | COAP, OPTE, Opt. Letters, PJO, SIOPT |
| 2017–2022 | 34 | textbook (2017), surrogate ensembles, mesh-based Nelder–Mead, PB trust region with Conn, granular variables, hidden/binary constraints, StoMADS, adaptive precision, multiobjective indicators, NOMAD 4, discontinuities | COAP, SIOPT, EJOR, ORL, TOMS |
| 2023–2026 | 27 | mixed/categorical variables (framework, distance, CatMADS, Cat-Suite), counterexample note, covering step, SOLAR benchmark, multi-fidelity, ADS (mesh-free), Mads-PIP, bilevel DFO benchmarking, textbook 2nd ed. (2026) | Math. Prog., Opt. Letters, OPTE, COAP, JOTA, GERAD cahiers + arXiv |

### 1.3 Collaboration network (co-author counts within the 151 entries) [B]
Le Digabel 48 · Hansen 29 · Tribes 18 · Dennis 18 · Savard 14 · Messine 13 · Alarie 12 · Diouane 8 · Jaumard 8 · Kokkolaras 7 · Abramson 7 · Hare 5 · Hallé-Hannan 5 · Diago 5 · Lebeuf 5 · Côté 5 · Bouchet 4 · Gheribi 4 · Zghal 4 · Orban 4.
Reading: two long partnerships define the career: Dennis (Rice, 2000–2012) for the pattern-search/MADS theory, then Le Digabel + Tribes (GERAD, 2008–) for NOMAD, software and applications. Industry-side co-authors (Alarie, Côté, Gheribi, Diago, Lebeuf) recur across application and benchmark papers.

### 1.4 Venue habits [B]
- Theory lands in **SIAM J. Optimization** (GPS 2003, MADS 2006, PB 2009, OrthoMADS 2009, PSD-MADS 2008, BiMADS 2008, granular 2019, discontinuities 2022, adaptive precision 2021).
- Applications and benchmarks land in **Optimization and Engineering** (tight GPS 2004, spent potliner 2008, dynamic scaling 2016, SOLAR 2025) and application journals (Hydrological Sciences J., BMC Bioinformatics, CALPHAD, Thermochimica Acta, IEEE Trans. Power Systems).
- Almost every recent paper appears first as a **Les cahiers du GERAD** report plus arXiv (e.g., G-2016-49 for PBTR; G-2025-42 CatMADS; G-2026-01 multi-fidelity constraints).
- Software lands in **ACM TOMS** (Le Digabel 2011; Audet et al. 2022).

---

## 2. Key verified papers (cited in SKILL.md)

| # | Paper | Status | ID |
|---|---|---|---|
| P1 | Audet, Dennis. *Pattern search algorithms for mixed variable programming*. SIAM J. Optim. 11(3):573–594, 2001 | [B] | 10.1137/S1052623499352024 |
| P2 | Audet, Dennis. *Analysis of generalized pattern searches*. SIAM J. Optim. 13:889–903, 2003 | [S+B] | 10.1137/S1052623400378742 |
| P3 | Audet. *Convergence results for generalized pattern search algorithms are tight*. Optim. Eng. 5:101–122, 2004 | [S+B] | 10.1023/B:OPTE.0000033370.66768.a9 |
| P4 | Audet, Dennis. *A pattern search filter method for nonlinear programming without derivatives*. SIAM J. Optim. 14(4):980–1010, 2004 | [B] | 10.1137/S105262340138983X |
| P5 | Audet, Dennis. *Mesh adaptive direct search algorithms for constrained optimization*. SIAM J. Optim. 17(1):188–217, 2006 | [S+B] | 10.1137/040603371 |
| P6 | Audet, Custódio, Dennis. *Erratum: Mesh adaptive direct search algorithms for constrained optimization*. SIAM J. Optim. 18(4):1501–1503, 2008 | [B] (+ ResearchGate listing seen in search) | 10.1137/060671267 |
| P7 | Audet, Orban. *Finding optimal algorithmic parameters using derivative-free optimization*. SIAM J. Optim. 17(3):642–664, 2006 | [B] | 10.1137/040620886 |
| P8 | Audet, Savard, Zghal. *Multiobjective optimization through a series of single-objective formulations* (BiMADS). SIAM J. Optim. 19(1):188–210, 2008 | [S+B] | 10.1137/060677513 |
| P9 | Audet, Béchard, Le Digabel. *Nonsmooth optimization through Mesh Adaptive Direct Search and Variable Neighborhood Search*. J. Global Optim. 41(2):299–318, 2008 (STYRENE problem) | [S+B] | 10.1007/s10898-007-9234-1 |
| P10 | Audet, Dennis. *A progressive barrier for derivative-free nonlinear programming*. SIAM J. Optim. 20(1):445–472, 2009 | [S+B] | 10.1137/070692662 |
| P11 | Abramson, Audet, Dennis, Le Digabel. *OrthoMADS: A deterministic MADS instance with orthogonal directions*. SIAM J. Optim. 20(2):948–966, 2009 | [S+B] | 10.1137/080716980 |
| P12 | Le Digabel. *Algorithm 909: NOMAD: Nonlinear optimization with the MADS algorithm*. ACM TOMS 37(4):44, 2011 | [S] | 10.1145/1916461.1916468 |
| P13 | Audet, Dennis, Le Digabel. *Trade-off studies in blackbox optimization*. Optim. Methods Softw. 27(4–5):613–624, 2012 | [B] | 10.1080/10556788.2011.571687 |
| P14 | Audet. *A survey on direct search methods for blackbox optimization and their applications*. In Mathematics Without Boundaries, Springer, 2014 | [S+B] | 10.1007/978-1-4939-1124-0_2 |
| P15 | Audet, Kokkolaras. *Blackbox and derivative-free optimization: theory, algorithms and applications* (editorial). Optim. Eng. 17:1–2, 2016 | [S+B] | 10.1007/s11081-016-9307-4 |
| P16 | Audet, Hare. *Derivative-Free and Blackbox Optimization*. Springer ORFE, 2017; 2nd ed. 2026 | [S+B] | 10.1007/978-3-319-68913-5 ; 10.1007/978-3-032-00906-7 |
| P17 | Audet, Conn, Le Digabel, Peyrega. *A progressive barrier derivative-free trust-region algorithm for constrained optimization*. Comput. Optim. Appl. 71:307–329, 2018 | [S+B] | 10.1007/s10589-018-0020-4 |
| P18 | Audet, Caporossi, Jacquet. *Binary, unrelaxable and hidden constraints in blackbox optimization*. Oper. Res. Lett. 48(4):467–471, 2020 | [B] | 10.1016/j.orl.2020.05.011 |
| P19 | Audet, Dzahini, Kokkolaras, Le Digabel. *Stochastic mesh adaptive direct search for blackbox optimization using probabilistic estimates* (StoMADS). Comput. Optim. Appl. 79:1–34, 2021 | [S+B] | 10.1007/s10589-020-00249-0 |
| P20 | Alarie, Audet, Gheribi, Kokkolaras, Le Digabel. *Two decades of blackbox optimization applications*. EURO J. Comput. Optim. 9:100011, 2021 | [B] | 10.1016/j.ejco.2021.100011 |
| P21 | Audet, Bigeon, Cartier, Le Digabel, Salomon. *Performance indicators in multiobjective optimization*. EJOR 292(2):397–422, 2021 | [S+B] | 10.1016/j.ejor.2020.11.016 |
| P22 | Audet, Le Digabel, Rochon Montplaisir, Tribes. *Algorithm 1027: NOMAD version 4*. ACM TOMS 48(3):35, 2022 | [S+B] | 10.1145/3544489 ; arXiv 2104.11627 |
| P23 | Audet, Le Digabel, Salomon, Tribes. *Constrained blackbox optimization with the NOMAD solver on the COCO constrained test suite*. GECCO Companion 2022, 1683–1690 | [B] | 10.1145/3520304.3534019 |
| P24 | Audet, Bouchet, Bourdin. *Counterexample and an additional revealing poll step for a result of "analysis of direct searches for discontinuous functions"*. Math. Program. 208:411–424, 2024 | [S+B] | 10.1007/s10107-023-02042-3 ; arXiv 2211.09947 |
| P25 | Andrés-Thiò, Audet, Diago, Gheribi, Le Digabel, Lebeuf, Lemyre Garneau, Tribes. *solar: A solar thermal power plant simulator for blackbox optimization benchmarking*. Optim. Eng., 2024/2025 | [S+B] | 10.1007/s11081-024-09952-x ; arXiv 2406.00140 |
| P26 | Audet, Denorme, Diouane, Le Digabel, Tribes. *Adaptive direct search algorithms for constrained optimization*. GERAD / arXiv 2025 | [S+B] (see author note) | arXiv 2507.23054 |
| P27 | Audet, Denorme, Diouane, Le Digabel, Tribes. *Adaptive direct search algorithms with relaxable and quantifiable constraints*. GERAD / arXiv 2026 | [S+B] | arXiv 2607.05183 |
| P28 | Audet, Hare, Tribes. *A summary of benchmarking constrained, multi-objective and surrogate-assisted optimization methods*. Optim. Lett., 2026 | [S+B] | 10.1007/s11590-026-02302-z |

Author note on P26: one search-engine summary attributed ADS to "Audet and Bouchet, with Bourdin"; the group bibliography lists Audet, Denorme, Diouane, Le Digabel, Tribes, and the NOMAD user guide says ADS integration was done "in collaboration with Youssef Diouane and Théo Denorme". The bib/guide attribution is used.

---

## 3. Signature-work anatomies

> **Corrections from the full texts (2026-09-27).** These first-pass anatomies are kept as written; the current versions, with page references, are in `SKILL.md` (Signature Work Anatomy). The full-text anatomies of OrthoMADS (S006) and ADS (S129, S172) are kept below as SW6 and SW7, moved out of SKILL.md to keep it at five anatomies. What changed:
> - **SW1 (MADS).** The GPS → MADS origin is stated, not inferred: GPS's finite direction set is "the primary drawback of GPS algorithms in our opinion" (S001 p. 1), and the AFOSR final report names it as the research problem (D016 pp. 4–5). The erratum's content is now known: a correct proposition whose proof did not match the final notation, re-proved (D001 pp. 1–2).
> - **SW2 (progressive barrier).** "NOMAD 3 needed a default" is not in the paper. The paper motivates PB by four user situations (S007 pp. 3–4); the origin is stated as combining the GPS filter with MADS-EB (S007 p. 2); the abandoned path is stated: no filter, but its notion of dominance (S007 p. 3); the minimal evidence is a hierarchy, a counterexample forcing assumption A3, and tests on analytic problems plus STYRENE (S007 pp. 15–32).
> - **SW3 (NOMAD 4).** Read in full as arXiv v2 (S021): the origin is software debt (pp. 2–3), and the parity study is described in the paper itself (p. 14). ✗ The search-summary wording quoted in the Origin row below does not match the abstract, which reads: "In continuous development since 2001, it constantly evolved with the integration of new algorithmic features published in scientific publications." (S021 p. 1)
> - **SW4 (tightness).** The origin row is wrong: the counterexamples date from the Rice report CRPC-TR98779 (November 1998, three examples) and are cited by the GPS analysis, which came after them (S025 TR pp. 1–3; S002 pp. 3, 14). The 2004 article's "six examples" remain unverified.
> - **SW5 (solar).** Read in full as arXiv v1 (S071): the thesis origin and the Hydro-Québec grant are confirmed (pp. 1, 3, 35).

### SW1 · Mesh adaptive direct search algorithms for constrained optimization (SIAM J. Optim. 2006, 10.1137/040603371)

| Dimension | Content |
|---|---|
| Origin | GPS analysis (P2) had shown that the strength of optimality conditions depends on "the directions it uses" and on local smoothness; the tightness paper (P3) built small examples where GPS stops at non-stationary points because of its finite direction set. MADS is the answer: keep the mesh, but let poll directions become asymptotically dense. (Link between P2/P3 and MADS: inference from the abstracts, not an oral account.) |
| Why then | GPS theory was mature (Torczon, Lewis–Torczon; Audet–Dennis 2003) and the Clarke nonsmooth calculus gave a language for "stationary without derivatives". Engineering users (surrogate-based design work with Booker, Frank, Moore, AIAA 2000 [B]; industrial affiliation ⚠️ unverified) needed general nonsmooth constraints. |
| Key insight | Decouple the mesh size from the poll size so poll directions can be asymptotically dense; together with the extreme barrier, this gives Clarke-type stationarity for nonsmooth objectives under general constraints (abstract via search). |
| Minimal evidence | Hierarchical convergence analysis plus a first randomized instance (LtMADS; named in OrthoMADS abstract as "the first MADS instance", with results "with probability one"). |
| Abandoned paths | Finite direction sets of GPS (shown inadequate by P3); the randomness of LtMADS was later replaced by deterministic OrthoMADS (P11) because deterministic directions make "results [...] repeatable". |
| Reception | Erratum published 2008 with A.L. Custódio (P6; content of the correction not verified). Became the core of NOMAD (P12, P22). Very highly cited (GERAD profile reports >11k total citations for Audet; per-paper counts not verified). |
| Methods shown | Method 1 (Search/Poll split), Method 3 (theory ladder + counterexamples), Method 6 (solver as instrument). |

### SW2 · A progressive barrier for derivative-free nonlinear programming (SIAM J. Optim. 2009, 10.1137/070692662)

| Dimension | Content |
|---|---|
| Origin | Earlier constraint handling: extreme barrier in MADS 2006 (reject infeasible) and the filter method of 2004 (P4). Practical blackboxes return constraint values that can be violated during the search but must hold at the solution. (Inference from the sequence of papers.) |
| Why then | Filter-GPS existed; MADS gave dense directions; NOMAD 3 (2008) needed a default way to treat quantifiable relaxable constraints. |
| Key insight | Aggregate violations into a constraint-violation function and progressively lower a threshold on it, keeping both a best feasible and a best infeasible incumbent to poll around (description corroborated by the PBTR abstract, P17). |
| Minimal evidence | Convergence analysis plus numerical tests (details not read). |
| Abandoned paths | The filter (F) is still in NOMAD but is not the default: the user guide maps uncertain constraints to `CSTR` = PB, and F is "not compatible with CSTR or PB". Speculation: PB superseded filter as the default for practical reasons. |
| Reception | PB became the standard idea exported to other method families: a PB trust-region method with Conn (P17), a stochastic PB (Math. Program. 2023, ⚠️ authors not fully verified), ADS-PB in 2026 (P27). |
| Methods shown | Method 2 (constraint semantics first), Method 1. |

### SW3 · Algorithm 1027: NOMAD version 4 (ACM TOMS 2022, 10.1145/3544489)

| Dimension | Content |
|---|---|
| Origin | NOMAD "has been in continuous development since 2001, evolving with the integration of new algorithmic features published in scientific publications" (search summary of the TOMS abstract); NOMAD 3 dated from 2008. |
| Why then | Accumulated features (surrogates, PSD-MADS, multiobjective, noise) had outgrown the NOMAD 3 architecture; new funders (Huawei Canada, Rio Tinto, Hydro-Québec, IVADO) per the user guide. |
| Key insight | A complete redesign "with a new architecture providing more flexible code and added functionalities" (search summary) so that new algorithms (DMultiMads, Mads-PIP, ADS, CatMADS) can be added as components. |
| Minimal evidence | Release notes: "The performance of NOMAD 4 and 3 are similar when the default parameters of NOMAD 3 are used". The redesign was validated against its predecessor on the same defaults before new features were claimed. |
| Abandoned paths | Some NOMAD 3 features (RobustMads, StoMads, bi-objective in core) not yet ported (release notes). |
| Reception | Default citation for the solver; wrappers in Python, MATLAB, Julia (NOMAD.jl), Java; plug-in for Oríon (bbopt repos). |
| Methods shown | Method 6, Method 5. |

### SW4 · Convergence results for generalized pattern search algorithms are tight (Optim. Eng. 2004, 10.1023/B:OPTE.0000033370.66768.a9)

| Dimension | Content |
|---|---|
| Origin | After proving results under mild conditions (P2), Audet asked whether the hypotheses were needed. |
| Key insight | Six small-dimensional examples show that the results "cannot be strengthened without additional assumptions", i.e. the algorithm's requirements are not artifacts of the proofs (search-snippet paraphrase of the abstract). |
| Minimal evidence | Explicit low-dimensional counterexamples. |
| Reception | The same counterexample-driven style reappears 20 years later in P24 (a counterexample to a published theorem by Vicente & Custódio 2012, plus a repair via a "revealing poll step"). |
| Methods shown | Method 3. |

### SW5 · solar: a solar thermal power plant simulator for blackbox optimization benchmarking (Optim. Eng. 2024/25, 10.1007/s11081-024-09952-x)

| Dimension | Content |
|---|---|
| Origin | A 2015 Polytechnique master's thesis by M. Lemyre Garneau titled "Modelling of a solar thermal power plant for benchmarking blackbox optimization solvers" [B, thesis entry] → paper nine years later with Lemyre Garneau as co-author. |
| Why then | NSERC Alliance–Mitacs grant "Optimization of future energy systems" with Hydro-Québec (arXiv HTML title-page note seen in search). |
| Key insight | Release a realistic engineering blackbox with instances that differ in variable types, dimension, constraints (including hidden ones), stochasticity and fidelity, so solvers are compared on "real" pathologies (search summary). |
| Minimal evidence | Open-source C++ package on GitHub (bbopt/solar); follow-up "Benchmarking derivative-free optimization solvers for CSP plant design using the SOLAR simulator" (GERAD G-2025-70) [B]. |
| Methods shown | Method 4, Method 5. |

### SW6 · OrthoMADS: a deterministic MADS instance with orthogonal directions (SIAM J. Optim. 20(2), 2009, 10.1137/080716980; read in full [S006])

Full-text anatomy, moved here from SKILL.md (2026-09-27) to keep SKILL.md at five anatomies; its essentials are folded into the SKILL.md MADS anatomy.

| Dimension | Content |
|---|---|
| Origin | Two drawbacks of the authors' own LTMADS: random directions give convergence only with probability one, and Custódio and Vicente observed undesirably large angles between LTMADS poll directions [S006 p. 2]. Booker suggested quasi-Monte Carlo methods, which led to Halton sequences [S006 p. 22]. |
| Why then | The MADS erratum had just restated the instance conditions a new instance must meet [S006 pp. 14, 22; D001]. Random directions also made experiments costly to report: "Because of the random component of LTMADS, we felt that numerical experiments had to be performed on series of several runs to show the reader the variations in the results." [S006 p. 3] |
| Key insight | Replace the random construction by a deterministic one that is integer, orthogonal and asymptotically dense (Halton vector → scaled and rounded q → Householder matrix ‖q‖²I − 2qqᵀ, poll set [H −H]), with the sequence index tied to the finest poll size; everything else stays as in LTMADS [S006 pp. 3–12]. |
| Minimal evidence | No new convergence theory: "The convergence results for ORTHOMADS follow directly from those already published for MADS, and they hold deterministically, rather than with probability one, as for LTMADS, the first MADS instance." [S006 p. 1; Theorem 2.8, p. 14]. On 45 problems, each scored against 30 LTMADS runs, OrthoMADS matches or beats most of them [S006 pp. 15–21]. |
| Abandoned paths | LTMADS's random directions. From NOMAD 3.7.1, OrthoMADS directions come from a seeded generator and "Halton directions are deprecated" [S202 p. 104]: determinism gave way to seeded repeatability. |
| Reception | NOMAD 3's default direction type is ORTHO N+1 with quadratic models, and ORTHO 2N was the first poll type ported to NOMAD 4 [S021 pp. 4, 14]; ADS later proves OrthoMADS an instance of its own class [S129 pp. 16–19]. |
| Methods shown | Method 7, Method 3, Heuristic 8 |

### SW7 · Adaptive direct search algorithms for constrained optimization (GERAD / arXiv 2507.23054, 2025; read in full [S129]), with its PB sequel (arXiv 2607.05183, 2026 [S172])

Full-text anatomy, moved here from SKILL.md (2026-09-27).

| Dimension | Content |
|---|---|
| Origin | Two rival directional direct-search families, each with a weakness: MADS restricts trial points to a mesh but accepts any decrease; sufficient-decrease direct search places points anywhere but may reject genuine improvements. Two 1-D examples show where each mechanism "can hinder convergence efficiency" [S129 pp. 1–6]. |
| Why then | The 2024 counterexample paper had produced the revealing-poll device that ADS reuses [S129 p. 7]. Mesh projection was a known cost in the group's own work: off-mesh surrogate optimization "is often more efficient" [S046 p. 7], and ADS notes that projection "introduces a displacement that may not decrease as fast as the accuracy of the model" [S129 p. 22]. *(The link across papers is an inference.)* |
| Key insight | "This work introduces a new class of methods, Adaptive Direct Search (ADS), which uses a novel acceptance rule based on the so-called punctured space, avoiding both meshes and sufficient decrease conditions." [S129 p. 1]. Exclusion balls of radius δ around visited points replace the mesh, with δ = min{Δ, Δ²/Δ0} so that δ/Δ → 0 [S129 pp. 7–11]. |
| Minimal evidence | lim δ = 0 by exclusion balls and packing, Clarke–Jahn stationarity, and OrthoMADS and QRMADS proved ADS instances by a parameter map and induction [S129 pp. 12–19]; one Python code base for ADS, MADS and SDDS with mechanism counters, on Moré–Wild, CUTEst, SOLAR10 and Simplified-Wing, with a test-set bias toward a competitor admitted [S129 pp. 19–25]. |
| Abandoned paths | The mesh (MADS survives as an instance), and with it the rational-τ requirement, which S129 credits the 2004 tightness article with showing necessary for mesh-based methods [S129 p. 11]. EB only at first; PB came in the sequel, which opens with a 2-variable toy where the mesh blocks an obviously reachable optimum [S172 pp. 7–8]. |
| Reception | Too recent to judge. NOMAD integration was announced [S129 p. 25] and is credited in the NOMAD user guide (first pass). |
| Methods shown | Method 7, Method 3, Method 1, Method 5 |

## 4. Full-text coverage of the Google Scholar list (2026-09-27)

Source list: `../sources/publications/scholar.md` (Google Scholar profile harvested and re-audited 2026-09-27: 222 Scholar rows, every row matched one-to-one; all 134 DOIs and 28 arXiv ids resolve), plus DBLP, the GERAD publication list, the bbopt BibTeX and Semantic Scholar for works not on the profile. Full records, including duplicate rows (`dup_of`), are in `works.json`. Per-work full-text status: `../sources/papers/INDEX.md` (texts are git-ignored). Card index: `07-paper-cards.md`.

| Item | Count | Note |
|---|---|---|
| Scholar rows harvested | 222 | 26 duplicate or junk rows set aside (`dup_of`) |
| Distinct works | 212 | 196 on Scholar (S###) + 16 found elsewhere (D###); kinds: journal 117, report 33, talk 19, other 14, chapter 8, preprint 8, conference 7, book 4, thesis 2 |
| Paper cards | 193 | 19 works skipped without a card (talks, conference duplicates of journal papers, junk rows) |
| Read in full | 108 | 102 Scholar + 6 non-Scholar |
| Read in part | 6 | S202, S133, S140, S184, S118, D008 |
| Unreadable as named | 2 | S025 (the file is the 1998 precursor report CRPC-TR98779, read via OCR); S067 (the file is D002's text) |
| Abstract-level | 57 | no open full text found (`no-oa`) |
| Metadata-only | 20 | title, venue, year |
| Distinct works read in full or in part | 110 | after merging duplicates; 108 are Audet-authored (the other two are S213, M. A. Abramson's thesis, and D008, an edited proceedings volume) |

Counted once: S101 = S128, D002 = S067, S019 = S202, S112 = S163, S145 ≈ S204, S089 = S215, S207 = S208.

Full-text reads by period (full + partial / cards): 1994–1999 1/8; 2000–2004 12/24; 2005–2009 18/35; 2010–2014 15/36; 2015–2019 19/32; 2020–2024 25/29; 2025–2026 24/27. Work from 2020 on is read almost completely; 1994–1999 is read in full only through the thesis (S070).

Weighting: S022 (Audet 7th of 15 authors), S174 and S160 are collaborations Audet did not lead and never support a claim alone. S213 is used only as evidence of the research programme Audet co-directed, never as his writing.

Key works with no open full text (abstract or metadata cards only): the textbook, both editions (S003, D005); VNS search (S009); poll reduction to n+1 points (S038; first labelled "quadratic-model search", but its abstract describes a Poll-side reduction); mesh-based Nelder–Mead (S043); Robust-MADS (S055); BiMADS and MultiMads (S018, S026); MV-MADS (S017); globalization strategies (S024); granular variables (S033); the COCO study (S141); the AIAA 2000 surrogate paper (S008); the NOMAD project record (S012). The 2004 tightness article was not available; its 1998 precursor was read (S025).

Works first read in this pass that matter for the skill: Audet's 1997 PhD thesis, known only by its title in the first pass (S070); the 1998 Rice report that started the tightness line (S025); the 2000–2003 AFOSR final report with the stated origin of MADS (D016); the pooling paper that already concedes a competitor's home ground and puts instance data online (S015); M. A. Abramson's thesis, co-chaired by Audet (S213); the Micro-PRIAD benchmark report (D006); and the late student-led papers on categorical neighbourhoods, penalty-interior-point MADS and multi-fidelity constraints (S157, S158, S173).

