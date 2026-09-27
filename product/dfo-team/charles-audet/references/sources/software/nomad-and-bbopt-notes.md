# NOMAD and the bbopt GitHub organisation — process-evidence notes

Fetched 2026-09-27 via raw.githubusercontent.com (the GitHub web UI / API and gerad.ca / readthedocs were blocked by the egress proxy).
All quotes below are verbatim from the fetched files. Authorship of the user guide is collective (the NOMAD team: Audet, Le Digabel, Rochon Montplaisir, Tribes); individual sentences cannot be attributed to Audet alone.

## 1. NOMAD 4 user guide (source files in bbopt/nomad)

Files: `doc/user_guide/source/{index,Introduction,TricksOfTheTrade,HowToUseNomad,GettingStarted,ReleaseNotes}.rst`
URL pattern: https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst

Verbatim excerpts (Introduction.rst):

- "NOMAD is a software application for simulation-based optimization. [...] NOMAD is at its best when applied to blackbox functions."
- "Such functions are typically the result of expensive computer simulations which have no exploitable property such as derivatives, may be contaminated by noise, may fail to give a result even for feasible points."
- "The *Search* step is crucial in practice because it is so flexible and can improve the performance significantly."
- "Since the *Poll* step is the basis of the convergence analysis, it is the part of the algorithm where most research has been concentrated."
- Commented-out preface still present in the source: "If the optimization problem is convex, or if the functions are smooth and easy to evaluate, or if the number of variables is large, then NOMAD is not the solution that you should use. NOMAD is intended for time-consuming blackbox simulation with a small number of variables. NOMAD is often useful when other optimizers fail."
- Same preface: "Launching twice the simulation from the same input may produce different outputs. These unreliable properties are frequently encountered when dealing with real problems."
- "The development of NOMAD started in 2001, with three versions preceding NOMAD 4."
- Funding: NOMAD 4 "funded by Huawei Canada, Rio Tinto, Hydro-Québec, NSERC [...], InnovÉÉ [...] and IVADO"; NOMAD 3 and NOMAD 1–2 "funded by AFOSR and Exxon Mobil".
- NOMAD 1 and 2 "created and developed by Mark Abramson, Charles Audet, Gilles Couture, and John E. Dennis Jr."
- NOMAD 3 "created and developed by Charles Audet, Sebastien Le Digabel, Christophe Tribes and Viviane Rochon Montplaisir".
- "Some features of NOMAD have been developed under the impulsion of enthusiastic users/developers/interns: [names]".
- "The integration of the Adaptive Direct Search (ADS) algorithm into NOMAD was conducted in collaboration with Youssef Diouane and Théo Denorme." / "The new MadsPIP algorithm was developed in collaboration with Andrea Brilli and Youssef Diouane."
- "Bug reports and suggestions are valuable to us! We are committed to answer to posted requests as quickly as possible."

TricksOfTheTrade.rst:

- "NOMAD has default values for all algorithmic parameters. These values represent a compromise between robustness and performance obtained by developers on sets of problems used for benchmarking."
- A symptom → suggestion table, e.g. "Difficult constraint — Try PB instead of EB"; "No initial point — Add a LH search"; "Variables of different magnitudes — Change blackbox input scaling / Change Δ0 per variable / Tighten bounds"; "Many variables — Fix some variables / Use PSD-MADS"; "Unsatisfactory solution — Change direction type [...] Change initial point [...] Add a VNS Mads search [...] Try Mads-PIP or ADS algorithms [...] Disable quadratic models"; "Optimization is time consuming — Perform parallel blackbox evaluations"; "Blackbox is not that expensive — Setup maximum wall-clock time".

HowToUseNomad.rst:

- "EB constraints correspond to constraints that need to be always satisfied (*unrelaxable constraints*). The technique used to deal with those is the **Extreme Barrier** approach, consisting in simply rejecting the infeasible points."
- "PB and F constraints correspond to constraints that need to be satisfied only at the solution, and not necessarily at intermediate points (*relaxable constraints*)."
- "There may be another type of constraints, the *hidden constraints*, but these only appear inside the blackbox during an execution [...] (when such a constraint is violated, the evaluation simply fails and the point is not considered)."
- "If the user is not sure about the nature of its constraints, we suggest using the keyword CSTR, which corresponds by default to PB constraints."
- EQPB (equality constraints) "Since version 4.6 [...] It is supported in Mads-PB but not very good. [...] With EQPB, Mads-PIP works better than Mads-PB."
- Batch mode: "if your blackbox program crashes, it will not affect NOMAD: The point that caused this crash will simply be tagged as a blackbox failure."

ReleaseNotes.rst:

- "NOMAD 4 is a complete redesign compared with NOMAD 3 [...]" ; RobustMads and StoMads still to be ported from NOMAD 3; "Categorical variables are handled using the CatMads algorithm [...] in the python version of NOMAD 4 called NomadBBO soon available in PyPI."
- "The performance of NOMAD 4 and 3 are similar when the default parameters of NOMAD 3 are used".

## 2. bbopt organisation repositories (metadata via GitHub repository search; READMEs via raw.githubusercontent.com)

| Repo | What it shows (README) |
|---|---|
| bbopt/nomad | C++ MADS implementation; C, MATLAB, Python (PyNomad), Java interfaces; batch & library modes; LGPL v3 |
| bbopt/styrene | "blackbox optimization problem offered as a benchmark case for the derivative-free optimization community"; 8 vars scaled to [0;100]; 11 constraints split into "4 unrelaxable and nonquantifiable" and "7 relaxable and quantifiable" per the Le Digabel–Wild taxonomy; truth + static surrogate executables; feasible and infeasible x0; best-known solution credited to named students; cite Audet, Béchard, Le Digabel (JOGO 2008) |
| bbopt/solar | "a solar thermal power plant simulator for blackbox optimization benchmarking"; multiple instances; some stochastic (seed / replications); fidelity parameter ("The execution time increases with the fidelity") |
| bbopt/aircraft_range | supersonic business jet MDO from NASA BLISS TM; "specifically adapted for benchmarking derivative free optimization algorithms"; two variants (fixed-point MDA vs consistency equality constraints); ten initial points; variables scaled to [0,100] |
| bbopt/simplified_wing | MDO problem (Tribes, Dubé, Trépanier, Eng. Optim. 2005) packaged for benchmarking (Jan 2025) |
| bbopt/Micro-PRIAD | v1.0 (August 2026) "stochastic blackbox collection of ten problems [...] simulates an electrical grid to evaluate the cost of a given maintenance strategy" |
| bbopt/Cat-Suite | "60 mixed-variable analytical problems with categorical and quantitative variables for benchmarking. Half of the problems are constrained." Cite Hallé-Hannan, Audet, Diouane, Le Digabel, Tribes, GERAD G-2025 |
| bbopt/CatMADS_prototype | "The current code is a proof of concept. While the code is shared for transparency, it is still under development" |
| bbopt/RunnerPost | post-processing tool that "produces text data profiles from existing optimization results"; algo/problem/output selection files; GERAD G-2025-36 |
| bbopt/StoMADS | MATLAB; runs on 40 problems from Argonne's YATSOp collection used in the STARS paper, several noise types and levels |
| bbopt/HyperNOMAD | hyperparameter optimisation of deep networks via NOMAD 3 |
| bbopt/bibtex | shared group bibliography with strict entry pattern; "**NEVER** change a key, even if it is not standard or with the wrong year" |
| bbopt/dfbbo | "Repository for the DF-BBO book of Audet and Hare" |
| Others | sgtelib (surrogate library), DMultiMadsPB/EB, rungekutta, bbob-benchmark ("Blackbox optimization benchmarks using COCO"), Nomad_HPO_Llama-2_With_LoRa, BBPF (Blackbox Power Flow) |
