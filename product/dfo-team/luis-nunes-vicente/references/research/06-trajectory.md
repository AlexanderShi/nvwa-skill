# 06 · Research Trajectory

> Timeline from search snippets (Wikipedia via search = secondary; Lehigh/Coimbra news pages = primary institutional; papers = primary). Dates marked ⚠️ are partially confirmed.

## Timeline

| Year(s) | Event / direction | Trigger or context (evidence / inference) | Source |
|---|---|---|---|
| 1967 | Born in Coimbra, Portugal | — | Wikipedia via search (secondary) |
| 1990 | B.S. Mathematics & Operations Research, Univ. Coimbra | — | Wikipedia via search (secondary) |
| 1996 | Ph.D. Applied Mathematics, Rice University (Fulbright), advisor John Dennis. Thesis: "Trust-Region Interior-Point Algorithms for a Class of Nonlinear Programming Problems". Ralph Budd Thesis Award. One of three finalists, A. W. Tucker Prize (1994–96 cycle) | Derivative-based NLP roots: trust regions and interior points | https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs (primary); https://en.wikipedia.org/wiki/Luis_Nunes_Vicente (secondary) |
| 1996–2018 | Professor of Mathematics, Univ. Coimbra | — | Lehigh news (primary) |
| 2007 | SID-PSM (with Custódio); PSwarm (with Vaz). Pivot into DFO, specifically direct search | *Inference*: a Dennis student moving from trust-region NLP into the Rice direct-search tradition, now with a first PhD student of Vicente's own | SIOPT 18 (2007); JOGO 39 (2007) |
| 2009 | *Introduction to Derivative-Free Optimization* (Conn, Scheinberg & Vicente), SIAM | Consolidation: "first contemporary comprehensive treatment" | http://www.mat.uc.pt/~lnv/idfo/ |
| 2009–2017 | Associate editor, SIAM J. Optim.; OMS 2010–2018; EURO J. Comput. Optim. board | Service | Lehigh SIAM-Fellow news via search (primary) |
| 2010–2012 | MFN models in DS (2010); DMS multiobjective (2011); discontinuous functions (2012); sparse interpolation models (2012) | Extending DS to new problem classes | papers |
| 2013 | Worst-case complexity of direct search (EJCO); smoothing complexity (IMAJNA) | Entry into the complexity wave | papers |
| 2013–2018 | Editor-in-Chief, *Portugaliae Mathematica* | Service | Lehigh news via search |
| 2014–2019 | Probabilistic models (TR 2014, 2018), probabilistic descent (2015, 2019), merit function (2014), globally convergent ES (2015), convex/optimal-order complexity (2016). Toulouse co-advised PhDs: Diouane 2014, Royer 2016 | Randomization + complexity together; Gratton collaboration | papers; theses |
| 2015 | **Lagrange Prize in Continuous Optimization** (SIAM–MOS) with Conn and Scheinberg, for the 2009 book | Citation: "A small sampling of the direct impact of their work is seen in aerospace engineering, urban transport systems, adaptive meshing for partial differential equations, and groundwater remediation." (exact, in search result) | https://www.uc.pt/en/fctuc/dmat/noticias/LagrangePrize ; https://www.siam.org/programs-initiatives/prizes-awards/joint-prizes/lagrange-prize-in-continuous-optimization/prize-history/ |
| 2017 | "Methodologies and software for DFO" (Custódio, Scheinberg & Vicente), SIAM volume chapter | Survey/consolidation | ResearchGate record |
| 2018 | ISMP 2018 (Bordeaux) plenary ⚠️ (title only partially visible in search) | — | ⚠️ |
| **Aug 1, 2018** | **Move: Coimbra → Lehigh University**, Timothy J. Wilmott '80 Endowed Faculty Professor and Chair, Dept. of Industrial and Systems Engineering | On-record motive: "theory and algorithms, software development, and industrial applications" (see 02, S1) | https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs (primary) |
| 2019–2022 | Stochastic multi-gradient (Ann. OR 2021); accuracy–fairness Pareto fronts (CMS 2022); Liu PhD 2022 | **Pivot toward ML**: stochastic gradient-based multi-objective methods. Trigger (inference): Lehigh ISE's data-science/ML environment | papers; thesis |
| 2021–2025 | Bilevel stochastic gradient (arXiv 2021 → JOGO 2025); multi-objective lower level (OMS 2024); full-low evaluation (OMS 2023) | ML-driven bilevel formulations; DFO under noise | papers |
| 2022–2024 | Weak tail bound / reduced sample sizing (arXiv 2022 → SIOPT 2024) | Return to DFO core with stochastic sampling focus | paper |
| 2023–2025 | Chair, SIAM Activity Group on Optimization | Service | https://engineering.lehigh.edu/news/article/lehigh-ise-chair-has-been-elected-chair-optimization-siam |
| 2024 | SIAM Fellow: "for ground-breaking contributions to derivative-free and bilevel optimization, and exemplary leadership in editorial and organizational service to the SIAM community" (quoted in search result) | — | https://engineering.lehigh.edu/news/article/lehigh-ise-faculty-luis-nunes-vicente-has-been-selected-fellow-siam |

## Latest 12 months (Sep 2025 – Sep 2026)

| Date | Item | Source |
|---|---|---|
| Sep 2025 | Ding, Rinaldi & Vicente, "Sequential test sampling for stochastic derivative-free optimization", arXiv:2509.14505. Sufficient decrease posed as a sequential hypothesis test; AFOSR FA9550-23-1-0217 and ONR N000142412656 support | https://arxiv.org/pdf/2509.14505 |
| Feb 2026 | UH ISE seminar "Pareto sensitivity, most-changing sub-fronts, and knee solutions"; a UF ISE seminar with the same topic (date ⚠️) | https://www.ise.uh.edu/research/seminars/202602/pareto-sensitivity-most-changing-sub-fronts-knee-solutions |
| (year ⚠️) | Talks "Reducing Sample Complexity in Stochastic DFO via Tail Bounds and Hypothesis Testing" at Pitt IE (Apr 16) and Rice CMOR (Feb 23) | Pitt / Rice event pages |
| Mar 2026 | Pareto sensitivity paper revised (v3) | https://arxiv.org/abs/2501.16993 |
| May 2026 | Tran & Vicente, "Stochastic block coordinate and function alternation for multi-objective optimization and learning", arXiv:2605.12432 | https://arxiv.org/abs/2605.12432 |
| Sep 2026 | Ding, Tran & Vicente, "Non-monotone direct-search methods for deterministic and stochastic derivative-free optimization", arXiv:2609.11567 | https://arxiv.org/abs/2609.11567 |

## Pivots and their triggers (summary)

1. **NLP (trust-region interior-point) → direct search (~2000s)**. Trigger undocumented. *Inference*: the Rice/Dennis direct-search environment plus a first PhD student (Custódio) working on simplex derivatives.
2. **Convergence → complexity (2013)**. *Inference*: field-wide complexity turn. Vicente's contribution was to make direct search countable via sufficient decrease.
3. **Deterministic → probabilistic (2014–2015)**. Stated trigger: numerical evidence that random polling without positive spanning did better (GRVZ 2015 abstract).
4. **DFO → ML-flavoured stochastic multi-objective/bilevel (2019 → )**. Coincides with the Lehigh move. Motive stated only generically (02, S1, S6).
5. **Back to stochastic DFO sampling (2022 → 2026)**. A convergence of pivots 3 and 4: noise-aware acceptance tests.

## Entry/exit timing (inference)

- Enters directions **after** a numerical or modelling signal (random directions, multiobjective engineering needs, fairness trade-offs) and **when** an analysis tool is available (sufficient-decrease counting; martingale arguments from the TR 2014 work).
- No documented exit; lines are handed to students, who continue them (Custódio co-authored DMS; Royer carried probabilistic DS through 2019).
