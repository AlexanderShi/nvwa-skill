# 01 · Publications landscape and signature-work anatomy — Charles Audet

Research date: 2026-09-27. Method: web-search snippets (~25 searches before the session's shared search budget ran out) plus a primary, group-maintained BibTeX file fetched from GitHub. No full texts were read (arXiv, Springer, SIAM, ACM, GERAD, dblp and OpenAlex hosts were blocked by the egress proxy).

Verification legend: **[S]** confirmed by a search result (title + authors + year, usually venue). **[B]** confirmed by the bbopt group bibliography (`bibliography.bib`, primary, with DOI). **[S+B]** both. Items marked ⚠️ are leads only.

Full hand-built list (151 entries with "Audet" in the author field): `../sources/publications/audet-publications-bbopt-bib.md`.
Source of that list: https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib (primary, group-maintained; may be incomplete).

---

## 1. Landscape

### 1.1 Identity (secondary, profile pages)
- Full professor, Department of Mathematics and Industrial Engineering, Polytechnique Montréal; member of GERAD. PhD in applied mathematics from École Polytechnique de Montréal; post-doc at Rice University (Houston). Research interests stated as "blackbox nonsmooth optimization" and "structured global optimization": pattern search (GPS, MADS) plus exact global methods for bilevel, quadratic, bilinear and integer programming. [S] https://www.gerad.ca/en/people/charles-audet ; https://www.polymtl.ca/expertises/en/audet-charles (secondary, institutional profile)
- PhD year and PhD advisor: ⚠️ not verified. The earliest bib entries (1997–2001) are all with P. Hansen, B. Jaumard, G. Savard, which suggests a GERAD global-optimization training (inference, not verified).

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

### SW1 · Mesh adaptive direct search algorithms for constrained optimization (SIAM J. Optim. 2006, 10.1137/040603371)

| Dimension | Content |
|---|---|
| Origin | GPS analysis (P2) had shown that the strength of optimality conditions depends on "the directions it uses" and on local smoothness; the tightness paper (P3) built small examples where GPS stops at non-stationary points because of its finite direction set. MADS is the answer: keep the mesh, but let poll directions become asymptotically dense. (Link between P2/P3 and MADS: inference from the abstracts, not an oral account.) |
| Why then | GPS theory was mature (Torczon, Lewis–Torczon; Audet–Dennis 2003) and the Clarke nonsmooth calculus gave a language for "stationary without derivatives". Engineering users (Boeing surrogate work, AIAA 2000 [B]) needed general nonsmooth constraints. |
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
