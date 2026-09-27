# 05 · Peer critique, limits and competing approaches

Honest scope: no published critique aimed specifically at Audet's work (such as a failed replication or a rebuttal exchange) was found in the available budget. This file collects: (1) limits the Audet team states itself, (2) corrections and counter-corrections in the record, (3) methodological contrasts with competing schools, documented by publications, and (4) gaps. Items marked ⚠️ are leads only.

---

## 1. Self-declared limits (primary, NOMAD team)
| Limit | Wording | Source |
|---|---|---|
| Wrong tool for convex, smooth-and-cheap, or high-dimensional problems | "If the optimization problem is convex, or if the functions are smooth and easy to evaluate, or if the number of variables is large, then NOMAD is not the solution that you should use." | NOMAD user guide source, Introduction.rst (commented-out preface) — https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst |
| Equality constraints weak in Mads-PB | "It is supported in Mads-PB but not very good." | HowToUseNomad.rst |
| Defaults are a compromise and may be poor on your problem | "These values represent a compromise between robustness and performance obtained by developers on sets of problems used for benchmarking." | TricksOfTheTrade.rst |
| Quadratic models can hurt | Tricks table lists "Disable quadratic models" as a remedy for "Unsatisfactory solution" and "Improvements get negligible"; a warning says "-Inf" outputs declared as constraints make NOMAD build models that "can hinder the overall optimization". | TricksOfTheTrade.rst, HowToUseNomad.rst |
| Mesh restricts the search | The ADS abstract frames MADS as restricting "trial points to a mesh" and SDDS as accepting only "sufficient decrease". ADS is proposed to avoid both, so the mesh is presented as a limitation of the team's own flagship (search-snippet paraphrase). | arXiv 2507.23054 |

## 2. Corrections in the record
| Event | Direction | Source | Cred. |
|---|---|---|---|
| Erratum to MADS (2008), with A.L. Custódio | Audet's own flagship corrected. Content not verified. | 10.1137/060671267 [B]; ResearchGate listing seen in search | primary |
| Counterexample (2022 arXiv; Math. Program. 2024) to a theorem in Vicente & Custódio, Math. Program. 133:299–325 (2012), on direct search for discontinuous functions. The flaw: a directional direct-search method can generate trial points converging to a point where f is discontinuous and lower semicontinuous with f(x*) strictly below lim f(x_k). Repair: an additional "revealing poll step". | Audet's group critiquing a competing direct-search analysis | 10.1007/s10107-023-02042-3 ; arXiv 2211.09947 | primary (abstract via search) |
| GPS "tightness" examples (2004) | Audet delimiting the team's own theory | 10.1023/B:OPTE.0000033370.66768.a9 | primary |

No published response by Vicente or Custódio to the 2024 note was found (search budget exhausted; absence is not evidence).

## 3. Methodological contrasts with competing approaches

### 3.1 Model-based trust-region DFO (Powell and Conn lenses)
- **Evidence of engagement, not rejection.** Audet co-authored two 2018 papers with A.R. Conn: a progressive-barrier **trust-region** method (COAP 71:307–329) and quadratic subproblems inside direct search (EJOR 2018) [S+B]. Audet & Hare wrote *Model-Based Methods in Derivative-Free Nonsmooth Optimization* (book chapter, 2020, 10.1007/978-3-030-34910-3_19) [B]. Quadratic models became a default NOMAD search after *Reducing the number of function evaluations in MADS* (SIAM J. Optim. 2014) [B].
- **Where the lenses differ (inference from abstracts):** in the Audet framework, models live in the **search** step and are never needed for convergence. Poll directions carry the guarantee, so a bad model costs evaluations but not theory. The PBTR abstract reports competitiveness with **COBYLA** on 40 smooth constrained problems and with NOMAD on two nonsmooth MDO problems. This implicitly concedes that model-based methods set the bar on smooth problems, and that the argument for direct search rests on nonsmooth, failing or noisy blackboxes.
- Secondary: reviewers call the textbook balanced between theory and practice (Brezhneva, Math. Reviews 2018). The book covers heuristics (GA, Nelder–Mead), direct search (GPS, MADS) and model-based methods (simplex gradient, trust region) (search snippet).

### 3.2 Sufficient-decrease and probabilistic direct search (Vicente lens)
- The ADS paper (2025) sets MADS (mesh, simple decrease) against SDDS (sufficient decrease, points anywhere) and proposes a third acceptance rule. This is a direct, publication-level methodological disagreement about **how to globalize direct search**.
- OrthoMADS (2009) replaced the randomized LtMADS because deterministic directions give repeatable runs and deterministic (not probability-one) convergence. Randomized direct search is a competing paradigm. A 2025 survey by Dzahini (a former group PhD), Rinaldi, Royer and Zeffiro, *Direct-search methods in the year 2025: theoretical guarantees and algorithmic paradigms* (arXiv 2403.05322), covers these paradigms (content not read; secondary).
- ⚠️ *Non-convergence analysis of probabilistic direct search* (arXiv 2606.01320): authors not verified, do not cite as Audet's.
- In the verified Audet corpus, guarantees are asymptotic: Clarke stationarity, "with probability one" for StoMADS. No worst-case complexity bound appears in any verified Audet title or abstract. This is absence of evidence, not a verified position.

### 3.3 Stochastic / noisy optimization (Scheinberg lens)
- StoMADS (2021) uses "random estimates of function values" that must be "accurate with a sufficiently large but fixed probability and to satisfy a variance condition" (abstract via search). This probabilistic-estimates framing is shared with stochastic trust-region lines. The direct lineage and citation were not verified.
- The StoMADS repo benchmarks on the problem set of the STARS paper (arXiv 2207.06452, *Stochastic trust-region algorithm in random subspaces*; authors not verified here beyond the README link), which shows a willingness to compete on the other side's problems.
- Adaptive precision (SIAM J. Optim. 2021) and robust MADS (2018) are two further noise strategies inside the same framework [B].

### 3.4 Bayesian optimization and ML-style surrogates
- **No verified Audet critique of Bayesian optimization was found.** What the record does show: surrogate ensembles with order-based error (JOGO 2018), uncertainty quantification with ensembles of surrogates (COAP 2022), locally weighted regression surrogates (Optim. Eng. 2018), and the sgtelib library [B]. In every case the surrogate feeds the search step. It never replaces the poll.
- Categorical/mixed-variable benchmarks (Cat-Suite, 60 problems) and SOLAR give a neutral ground for BO-vs-MADS comparisons. No verified head-to-head result was found.

### 3.5 Evolutionary / heuristic methods
- Participation in the evolutionary community's benchmark (NOMAD on COCO constrained suite, GECCO Companion 2022) [B].
- Heuristics are absorbed and given guarantees rather than dismissed: mesh-based Nelder–Mead (COAP 2018), VNS search (JOGO 2008), cross-entropy + MADS (Oper. Res. Forum 2021) [B].

## 4. Limits of this critique file
- Independence problem: the two textbook reviews found are by Brezhneva (independent as far as known) and Kokkolaras (frequent co-author, not independent).
- No citation-context analysis (how others criticize MADS in their related-work sections) was possible without full texts.
- ⚠️ Lead: *Best practices for comparing optimization algorithms* (Beiranvand, Hare, et al.; arXiv 1709.08242) is a benchmarking-methodology paper co-authored by Audet's textbook partner Hare, not by Audet. The full author list and venue were not verified.
