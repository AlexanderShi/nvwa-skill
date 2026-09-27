# 03 · Process evidence — what Audet actually DOES

Evidence types: software (NOMAD source docs, GitHub repos of the bbopt organisation), paper metadata and abstracts (search snippets), and the group bibliography (primary). Full paper texts were not read, so paper-internal structure (appendices, ablations) is inferred only from abstracts.

Credibility: all items below are **primary** (artifacts produced by Audet or teams including Audet) unless marked otherwise. Repos in bbopt are team artifacts; Audet is not necessarily the committer.

---

## A. NOMAD as the research instrument

| Observation | Evidence | URL |
|---|---|---|
| A solver line maintained for 25 years across 4 major versions and 3 developer generations: NOMAD 1–2 (Abramson, Audet, Couture, Dennis), NOMAD 3 (Audet, Le Digabel, Tribes, Rochon Montplaisir), NOMAD 4 (complete redesign). | User guide "Authors and fundings" | https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst |
| New papers become NOMAD components: DMultiMads (Salomon PhD), Mads-PIP (with Brilli, Diouane), ADS (with Diouane, Denorme), CatMADS (Python NomadBBO), sgtelib surrogates (Talgorn), PSD-MADS, VNS search, LH search, quadratic model search. | User guide Introduction + TricksOfTheTrade + ReleaseNotes | same folder |
| Redesign checked against the predecessor before new claims: "The performance of NOMAD 4 and 3 are similar when the default parameters of NOMAD 3 are used". | ReleaseNotes.rst | https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/ReleaseNotes.rst |
| Practitioner diagnosis encoded as a **symptom → remedy table** (difficult constraint → PB instead of EB; no x0 → LH search; different magnitudes → scaling / per-variable Δ0 / tighter bounds; many variables → fix some / PSD-MADS; unsatisfactory solution → change directions, x0, VNS, Mads-PIP/ADS, disable quadratic models, seeds; time consuming → parallel evaluations). | TricksOfTheTrade.rst | https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/TricksOfTheTrade.rst |
| Crash isolation designed in: batch mode runs the blackbox as a separate executable, so "if your blackbox program crashes, it will not affect NOMAD: The point that caused this crash will simply be tagged as a blackbox failure." The example blackbox writes `1e20` on read failure; non-zero exit status means a failed evaluation. | HowToUseNomad.rst, GettingStarted.rst | https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/HowToUseNomad.rst |
| Constraint semantics are part of the interface: `BB_OUTPUT_TYPE` = OBJ / EB / PB / CSTR / F / EQPB / CNT_EVAL / NOTHING. The user must decide, for each output, whether it is unrelaxable, relaxable or merely logged. | HowToUseNomad.rst | same |
| Many entry points for engineers: C++ library, batch mode, C, MATLAB, Python (PyNomad), Java, Julia (NOMAD.jl), Oríon plug-in. | nomad README; bbopt repo list | https://raw.githubusercontent.com/bbopt/nomad/master/README.md |
| Industry and defense funding across versions: AFOSR + ExxonMobil (NOMAD 1–3); Huawei Canada, Rio Tinto, Hydro-Québec, NSERC, InnovÉÉ, IVADO (NOMAD 4). | Introduction.rst | same |

## B. Turning real problems into public benchmark artifacts

| Artifact | Packaging conventions observed | Origin | URL |
|---|---|---|---|
| STYRENE | C++ executable, `truth.exe x.txt`; 8 variables scaled to [0;100]; 11 constraints `c_j(x) ≤ 0`, split into 4 unrelaxable/nonquantifiable and 7 relaxable/quantifiable using the Le Digabel–Wild taxonomy; truth **and** a static surrogate; feasible and infeasible x0; best-known solution with credit to the students who found it; runs of NOMAD and PSwarm included | chemical-process code "initially developed by Vincent Béchard"; published in JOGO 2008 (Audet, Béchard, Le Digabel) | https://raw.githubusercontent.com/bbopt/styrene/master/README.md |
| SOLAR | multiple instances; mixed variable types; hidden constraints; stochastic instances controlled by seed or replications; fidelity parameter | MSc thesis 2015 (Lemyre Garneau) → Optim. Eng. 2024/25; Hydro-Québec grant | https://raw.githubusercontent.com/bbopt/solar/master/README.md ; 10.1007/s11081-024-09952-x |
| AIRCRAFT_RANGE | MDO problem from NASA BLISS TM; "specifically adapted for benchmarking derivative free optimization algorithms"; two formulations (internal fixed-point MDA vs consistency **equality** constraints); ten initial points; variables scaled to [0,100]; extra output counts discipline analyses | used in PBTR 2018 experiments ("two nonsmooth MDO problems", search snippet); repo 2025 | https://raw.githubusercontent.com/bbopt/aircraft_range/main/README.md |
| SIMPLIFIED_WING | MDO problem (Tribes, Dubé, Trépanier 2005) packaged Jan 2025 | Tribes's earlier MDO work | https://raw.githubusercontent.com/bbopt/simplified_wing/main/README.md |
| RUNGEKUTTA | "The RUNGE-KUTTA blackbox optimization problem" (repo 2025) | Audet, *Tuning Runge-Kutta parameters on a family of ODEs*, IJMMNO 2018 [B] | https://github.com/bbopt/rungekutta |
| Micro-PRIAD | "stochastic blackbox collection of ten problems"; electrical-grid maintenance cost; sub-sampling of Monte Carlo draws within an evaluation (Aug 2026) | GERAD tech report 2026 (Gentile, Lebeuf, Le Digabel, Audet, Diago) [B] | https://raw.githubusercontent.com/bbopt/Micro-PRIAD/main/README.md |
| Cat-Suite | 60 analytical mixed-variable problems (categorical + quantitative), half constrained | GERAD G-2025 (Hallé-Hannan, Audet, Diouane, Le Digabel, Tribes) | https://raw.githubusercontent.com/bbopt/Cat-Suite/main/README.md |

Pattern: application paper or student thesis → C++ (or Julia) executable with a fixed I/O contract → GitHub → used as a benchmark in later algorithm papers. Lags can be long (STYRENE 2008 → repo 2020; SOLAR thesis 2015 → paper 2024).

## C. Benchmarking practice

| Practice | Evidence | Source |
|---|---|---|
| Compare against the strongest solver of a **different** family on its home ground, then on your home ground. | PBTR (Audet, Conn, Le Digabel, Peyrega 2018): "40 smooth constrained problems" → competitive with COBYLA; "two nonsmooth multidisciplinary optimization problems from mechanical engineering" → competitive with NOMAD (search snippet of abstract). | 10.1007/s10589-018-0020-4 |
| Enter other communities' benchmark suites. | NOMAD on the **COCO constrained test suite** (GECCO Companion 2022) [B]; `bbopt/bbob-benchmark` "Blackbox optimization benchmarks using COCO". | 10.1145/3520304.3534019 ; https://github.com/bbopt/bbob-benchmark |
| Take part in multi-team comparisons on shared engineering problems. | Fowler et al. 2008, *Comparison of derivative-free optimization methods for groundwater supply and hydraulic capture community problems*, Adv. Water Resour. 31(5):743–757 — 15 co-authors including Audet, Dennis, Kelley, Kolda [B]. | 10.1016/j.advwatres.2008.01.010 |
| Use other groups' problem sets for noisy optimization. | StoMADS repo runs on "the 40 problems (from the YATSOp repository) considered in the numerical section of the STARS paper", with additive/multiplicative, Gaussian/uniform noise at several levels. | https://raw.githubusercontent.com/bbopt/StoMADS/main/README.md |
| Build shared tooling for profiles. | RunnerPost "produces text data profiles from existing optimization results" from algorithm/problem/output selection files (GERAD G-2025-36). | https://raw.githubusercontent.com/bbopt/RunnerPost/develop/README.md |
| Publish benchmarking as research. | *Performance indicators in multiobjective optimization* (EJOR 2021, 63 indicators classified); *Benchmarking DFO solvers for CSP plant design using the SOLAR simulator* (G-2025-70) [B]; *Benchmarking bilevel derivative-free optimization algorithms* (G-2026-26, arXiv 2605.30531) [B]; *A summary of benchmarking constrained, multi-objective and surrogate-assisted optimization methods* (Optim. Lett. 2026). | see 01 |

## D. Engineering and industrial collaborations (problem sources)

| Domain | Paper(s) [B unless noted] | Notes |
|---|---|---|
| Aerospace surrogate design | Audet, Booker, Dennis, Frank, Moore, *A surrogate-model-based method for constrained optimization*, AIAA Paper 2000-4891 | Booker/Frank were Boeing researchers (⚠️ affiliation from memory, not verified here) |
| Thermal insulation (mixed variables) | Kokkolaras, Audet, Dennis, Optim. Eng. 2001 | first application of mixed-variable pattern search |
| Chemical process | Audet, Béchard, Chaouki, *Spent potliner treatment process optimization using a MADS algorithm*, Optim. Eng. 2008; STYRENE (JOGO 2008) | industrial partner ⚠️ not verified |
| Hydrology / snow | *Snow water equivalent estimation using blackbox optimization* (PJO 2013); hydrological model calibration (Hydrol. Sci. J. 2019; Minville et al. 2014) | bib contains dozens of hydrology references added for these papers — domain literature was read |
| Hydropower operations | Séguin, Côté, Audet (IEEE TPWRS 2016; EJOR 2017; J. Water Resour. Plan. Manag. 2017); maintenance of turbine fleets (2014) | Côté co-developed PyNomad (user guide) |
| Materials / alloys | Gheribi, Audet, Le Digabel et al., CALPHAD 2011/2012; Thermochimica Acta 2013 | |
| Metamaterials | Audet, Diest, Le Digabel, Sweatlock, Marthaler, book chapter 2013 | |
| Bioinformatics / pharma | PSEUDOMARKER 2.0 using NOMAD (BMC Bioinformatics 2014); adaptive crossover bioequivalence designs (Pharm. Stat. 2016) | |
| Algorithms as blackboxes | Audet & Orban SIAM J. Optim. 2006; OPAL (2010, 2013, Math. Prog. Comput. 2014); Runge–Kutta tuning 2018; HyperNOMAD; `Nomad_HPO_Llama-2_With_LoRa` repo (2023) | |
| Energy systems | SOLAR (2024/25); Micro-PRIAD (2026); `BBPF` Blackbox Power Flow repo (2023) | Hydro-Québec, Huawei funding lines |
| Retrospective | Alarie, Audet, Gheribi, Kokkolaras, Le Digabel, *Two decades of blackbox optimization applications*, EURO J. Comput. Optim. 2021 | a review written from the group's own application record |

## E. One framework, extended pathology by pathology

Each new difficulty is attacked by a MADS variant that keeps the poll-based guarantee (all [B], most also [S]):
mixed variables (2001) → filter constraints (2004) → dense directions (2006) → second order (2006) → parallel space decomposition PSD-MADS (2008) → biobjective BiMADS (2008) and multiobjective (EJOR 2010) → progressive barrier (2009) → periodic variables (2012) → fewer evaluations with quadratic models (2014) → linear equalities (2015) → dynamic scaling (2016) → noisy/robust (2018) → surrogate ensembles (2018) → granular/discrete (2019) → constraint scaling, hidden/binary constraints (2020) → stochastic StoMADS (2021) and adaptive precision (2021) → discontinuities (2022) → hierarchical constraints (2022) → meta/categorical variables (2023–2026) → multi-fidelity (2025–2026) → penalty-interior point Mads-PIP (2026) → mesh-free ADS and ADS-PB (2025–2026).

## F. Self-correction and counterexamples (result-judgment behaviour)

- 2004: six small counterexamples show GPS results are tight (10.1023/B:OPTE.0000033370.66768.a9).
- 2008: erratum to the MADS paper, co-authored with A.L. Custódio (10.1137/060671267). What was corrected was not verified.
- 2022–2024: arXiv 2211.09947 titled "Erratum, counterexample and an additional revealing poll step for a result of 'Analysis of direct searches for discontinuous functions'"; the journal version in Math. Program. 208 (2024) drops "Erratum" from the title. It gives a counterexample to a theorem in Vicente & Custódio (Math. Program. 133:299–325, 2012) and proposes a repair (a "revealing poll step").
- 2025: covering step (Opt. Lett.) strengthens direct-search guarantees towards local minima rather than stationary points (search snippet: "Convergence towards a local minimum by direct search methods with a covering step").

## G. Structure creep: from pure blackbox to grey box

Linear equalities (2015), monotonic grey box (Opt. Lett. 2020), hierarchically constrained (ORL 2022), multi-fidelity constraints (2026), partitioned framework for structure-aware problems (JOTA 2026). The group exploits known structure whenever a blackbox exposes some, while keeping a direct-search backbone.

## Era / resource notes
- The whole toolchain runs on a workstation. The limiting resource is blackbox evaluations, not compute for the optimizer. Parallelism appears as batch/parallel evaluations (OpenMP in NOMAD 4) and PSD-MADS.
- The research model relies on a **stable team**: a co-developer (Le Digabel) and a research software engineer (Tribes, 18 co-authored entries), plus continuous industry funding. A solo researcher cannot reproduce this scale. The small-resource version is to adopt NOMAD and the bbopt benchmark problems rather than build a solver.
