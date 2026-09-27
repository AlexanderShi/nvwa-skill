# 02 · Stated methodology — what Audet (and the NOMAD team) SAY about how to do DFO/blackbox research

Scope: only statements. Whether they are practiced is checked in 03. No interview, lecture transcript or "how I do research" essay by Audet was found in the search budget available; stated evidence therefore comes from (a) the Audet–Hare textbook (via publisher/review snippets), (b) paper abstracts (via search snippets), (c) the NOMAD user guide (primary source files, collectively authored by the NOMAD team of which Audet is a named developer).

Credibility: **primary** = text written by Audet or a team including Audet; **secondary** = someone else's description. "Verbatim" only where the fetched file or search snippet showed the exact wording; otherwise "(paraphrase)".

---

## Layer 1 · Research taste: what counts as a good problem and a good result

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| T1 | The object of study is the **blackbox**: functions produced by expensive simulations with no exploitable derivatives, possibly noisy, possibly failing even at feasible points. | Verbatim: "Such functions are typically the result of expensive computer simulations which have no exploitable property such as derivatives, may be contaminated by noise, may fail to give a result even for feasible points." | NOMAD 4 user guide, Introduction.rst — https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst | primary (team) |
| T2 | Know when the method is the wrong tool: convex, smooth-and-cheap, or large-n problems should go elsewhere. | Verbatim (commented-out preface kept in source): "If the optimization problem is convex, or if the functions are smooth and easy to evaluate, or if the number of variables is large, then NOMAD is not the solution that you should use. NOMAD is intended for time-consuming blackbox simulation with a small number of variables. NOMAD is often useful when other optimizers fail." | same file | primary (team) |
| T3 | Real problems are unreliable, and methods should be designed for that. | Verbatim: "Launching twice the simulation from the same input may produce different outputs. These unreliable properties are frequently encountered when dealing with real problems." | same file | primary (team) |
| T4 | Theory should say exactly how the strength of the guarantee depends on the directions used and on local smoothness, not just "converges". | Search-snippet wording of the abstract: "a simple convergence analysis that supplies detail about the relation of optimality conditions to objective smoothness properties and to the defining directions for the algorithm." | Audet & Dennis, SIAM J. Optim. 2003, 10.1137/S1052623400378742 | primary |
| T5 | A good convergence result is **tight**: its hypotheses are shown necessary by examples. | (paraphrase) Six small examples show the GPS results cannot be strengthened without additional assumptions; the algorithm's requirements are not artifacts of the proofs. | Audet, Optim. Eng. 2004, 10.1023/B:OPTE.0000033370.66768.a9 | primary |
| T6 | Repeatability matters: deterministic direction choice is preferred when it keeps the guarantees. | (paraphrase) OrthoMADS directions are chosen deterministically, "ensuring that results are repeatable", and its convergence holds deterministically rather than with probability one as for LtMADS. | Abramson, Audet, Dennis, Le Digabel, SIAM J. Optim. 2009, 10.1137/080716980 | primary |
| T7 | The field is a triad: theory, algorithms, applications. | Title wording: "Blackbox and derivative-free optimization: theory, algorithms and applications". | Audet & Kokkolaras editorial, Optim. Eng. 17:1–2, 2016, 10.1007/s11081-016-9307-4 | primary (weak: title only) |

## Layer 2 · Problem choice

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| C1 | DFO/BBO serves practitioners whose real-world problems cannot be approached by gradient-based methods. | (paraphrase) the textbook targets people who want to understand DFO/BBO and practitioners with real-world problems not approachable by gradient methods. | Audet & Hare 2017, Springer, 10.1007/978-3-319-68913-5 (publisher/retailer description via search) | primary (blurb) |
| C2 | Applications are part of the research record: the survey "lists numerous published applications". | (paraphrase) | Audet, survey chapter 2014, 10.1007/978-1-4939-1124-0_2 | primary |
| C3 | Multiobjective blackbox problems arise "when the functions are computed as the result of a computer simulation" and their structure "either cannot be exploited, or is absent". | Search-snippet paraphrase of abstract | Audet, Savard, Zghal, SIAM J. Optim. 2008, 10.1137/060677513 | primary |

## Layer 3 · Idea generation / algorithm design

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| I1 | Two-step design: a **free Search** step that carries practical performance and a **rigid Poll** step that carries the theory. | Verbatim: "The *Search* step is crucial in practice because it is so flexible and can improve the performance significantly. The *Search* step is constrained by the theory to return points on the underlying mesh [...]" and "Since the *Poll* step is the basis of the convergence analysis, it is the part of the algorithm where most research has been concentrated." | NOMAD user guide, Introduction.rst | primary (team) |
| I2 | Extend GPS so that local exploration uses an asymptotically dense set of directions, to handle nonsmooth objectives and general nonsmooth constraints. | (paraphrase of abstract) | Audet & Dennis, SIAM J. Optim. 2006, 10.1137/040603371 | primary |
| I3 | New algorithm families should "retain the theoretical foundations of directional direct search" while freeing the search (ADS: acceptance rule via a "punctured space" instead of a mesh or sufficient decrease). | (paraphrase of abstract) | Audet, Denorme, Diouane, Le Digabel, Tribes, arXiv 2507.23054 (2025) | primary |
| I4 | Surrogates, models and heuristics are welcome as search-step or subproblem components (e.g., models built around the best feasible and best infeasible points). | (paraphrase of PBTR abstract) | Audet, Conn, Le Digabel, Peyrega, COAP 2018, 10.1007/s10589-018-0020-4 | primary |

## Layer 4 · Experiments and benchmarking

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| E1 | Default parameters are a benchmark-derived **compromise**, and users should tune by symptom. | Verbatim: "These values represent a compromise between robustness and performance obtained by developers on sets of problems used for benchmarking. But you might want to improve NOMAD performance for your problem by tuning the parameters or use advanced functionalities." | NOMAD user guide, TricksOfTheTrade.rst — https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/TricksOfTheTrade.rst | primary (team) |
| E2 | Benchmarking tools must account for evaluation budgets: accuracy profiles can mislead when solvers use very different numbers of evaluations; data profiles are absolute, performance profiles relative. | Reported as a quotation from Audet & Hare (2017) in a citing text seen in a search snippet: "accuracy profiles ignore the number of function evaluations required to achieve the presented results, and thus accuracy profiles can be strongly biased when different algorithms use significantly different numbers of function evaluations". The data/performance distinction is a paraphrase. | Book chapter "Comparing Optimization Methods" (2nd ed. ch. 4: https://link.springer.com/chapter/10.1007/978-3-032-00906-7_4) | primary via secondary quotation (treat wording with caution) |
| E3 | The textbook gives comparison methodology a whole chapter ("Comparing Optimization Methods") before the algorithm chapters (ch. 4 of the 2nd ed., after "The Beginnings of DFO Algorithms"). | Chapter titles seen in search results | Springer 2nd ed. 2026, 10.1007/978-3-032-00906-7 | primary (structure) |
| E4 | A 2026 paper summarises benchmarking of constrained, multiobjective and surrogate-assisted methods. | Title only | Audet, Hare, Tribes, Optim. Lett. 2026, 10.1007/s11590-026-02302-z | primary (content not read) |

## Layer 5 · Judging results

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| J1 | Distinguish constraint semantics before judging feasibility: EB constraints "need to be always satisfied (*unrelaxable constraints*)"; PB/F constraints "need to be satisfied only at the solution, and not necessarily at intermediate points (*relaxable constraints*)"; hidden constraints make "the evaluation simply fail". | Verbatim | NOMAD user guide, HowToUseNomad.rst | primary (team) |
| J2 | When unsure about constraints, default to the progressive barrier: "we suggest using the keyword CSTR, which corresponds by default to PB constraints." | Verbatim | same | primary (team) |
| J3 | Report honestly where a feature is weak: EQPB "is supported in Mads-PB but not very good. [...] With EQPB, Mads-PIP works better than Mads-PB." | Verbatim | same | primary (team) |
| J4 | Published theorems are open to correction, including by counterexample. The note's abstract describes "the main flaw revealed by the counterexample". | (paraphrase) | Audet, Bouchet, Bourdin, Math. Program. 2024, 10.1007/s10107-023-02042-3 | primary |

## Layer 6 · Expression (writing, teaching)

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| X1 | Stated goal of the textbook, as quoted by a reviewer: "providing a clear grasp of the foundational concepts in derivative-free and blackbox optimization". | Verbatim inside a review quotation (search snippet). ✅ Checked 2026-09-27 against the primary first-edition preface, reprinted in the 2nd edition: "Our goal is to provide a clear grasp of the foundational concepts in derivative-free and blackbox optimization, in order to push these areas into the mainstream of nonlinear optimization." (B001 p. 13; joint voice of Audet and Hare) | Kokkolaras review, Optim. Eng. 20 (2019), 10.1007/s11081-019-09422-9 | secondary quoting primary |
| X2 | The book is meant for self-learning or an upper-year university course, and assumes multivariate calculus and linear algebra (paraphrase). | (paraphrase). ✅ Checked 2026-09-27 against the preface: "suitable for self-learning or for teaching an upper-year university course"; expected background multivariate calculus, linear algebra and proof techniques (B001 pp. 14–15) | publisher description via search; preface (B001) | primary |
| X3 | Teaching also happens in French at Polytechnique: course notes (MTH6404 integer programming, 2001; MTH1101 Calcul I, 2011) and the book *Optimisation continue* (Presses internationales Polytechnique, 2021, 305 pp). | Bib entries | bbopt bibliography.bib | primary (bibliographic) |

## Layer 7 · Research organisation

| # | Statement | Wording | Source | Cred. |
|---|---|---|---|---|
| O1 | The software is a living research record: NOMAD "has been in continuous development since 2001, evolving with the integration of new algorithmic features published in scientific publications". | Search-summary wording of the TOMS 2022 abstract (treat as paraphrase). ✗ Checked 2026-09-27 against the abstract, which reads: "In continuous development since 2001, it constantly evolved with the integration of new algorithmic features published in scientific publications." (S021 p. 1) | 10.1145/3544489 | primary |
| O2 | User feedback is part of development: "Bug reports and suggestions are valuable to us!" | Verbatim | NOMAD user guide, Introduction.rst | primary (team) |
| O3 | Prototypes are shared early "for transparency" even when "not intended for direct reuse". | Verbatim (CatMADS_prototype README) | https://raw.githubusercontent.com/bbopt/CatMADS_prototype/main/README.md | primary (group) |
| O4 | Shared infrastructure has strict conventions (group BibTeX: "**NEVER** change a key"). | Verbatim | https://raw.githubusercontent.com/bbopt/bibtex/master/README.md | primary (group) |

---

## Statements repeated ≥3 times (strongest stated methodology)
1. **Blackboxes are unreliable (noise, failures, hidden constraints)** — T1, T3, J1; also the Le Digabel 2011 TOMS abstract ("no function values returned for a significant number of calls attempted", search snippet), SOLAR paper ("including hidden constraints").
2. **Constraint type determines treatment** — J1, J2, PB paper, ADS-PB title ("relaxable and quantifiable constraints"), Binary/unrelaxable/hidden title (2020).
3. **Search for performance, poll for theory** — I1, I2, I3, I4.
4. **Theory must be exact about its conditions** — T4, T5, T6, J4.
5. **Benchmark on budgets and on realistic problems** — E1, E2, E3, E4.

## Not found (gaps)
- No verified interview, plenary transcript, or advice-to-students text. Any claim about how Audet chooses topics "in his own words" is therefore unavailable.
- Book preface text not read (Springer and GERAD hosts blocked); only blurbs and review quotations.
