# 06 · Research Trajectory

> Timeline from search snippets (Wikipedia via search = secondary; Lehigh/Coimbra news pages = primary institutional; papers = primary). Dates marked ⚠️ are partially confirmed.
>
> **Update 2026-09-27 (full-text pass).** The complete publication list (124 works, 108 read in full text; `07-paper-cards.md`) changes the picture in three places: a 1991–1995 period of bilevel programming and test-problem generators was missing; direct search enters in 2001 through an application, not in 2007; derivative-based NLP continues to 2008. Rows added or corrected from the cards are marked **[full text]**; the section "Trajectory as seen in the full texts" at the end summarizes `08-deep-reading-synthesis.md` §8–§9.

## Timeline

| Year(s) | Event / direction | Trigger or context (evidence / inference) | Source |
|---|---|---|---|
| 1967 | Born in Coimbra, Portugal | — | Wikipedia via search (secondary) |
| 1990 | B.S. Mathematics & Operations Research, Univ. Coimbra | — | Wikipedia via search (secondary) |
| 1991–1995 **[full text]** | Bilevel programming, complementarity and test-problem generators with known minima (Coimbra, Waterloo, GERAD), mostly with P. Calamai and J. Júdice; earliest listed paper is a 1991 vehicle-routing note in Portuguese | Early OR/global-QP work; generators offered as the field's common testbed | [S002 p. 6; S053; S026; D001; S004; S069; H008] |
| 1996 | Ph.D. Applied Mathematics, Rice University (Fulbright), advisor John Dennis. Thesis: "Trust-Region Interior-Point Algorithms for a Class of Nonlinear Programming Problems". Ralph Budd Thesis Award. One of three finalists, A. W. Tucker Prize (1994–96 cycle) | Derivative-based NLP roots: trust regions and interior points | https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs (primary); https://en.wikipedia.org/wiki/Luis_Nunes_Vicente (secondary) |
| 1996–2018 | Professor of Mathematics, Univ. Coimbra | — | Lehigh news (primary) |
| 2001–2004 **[full text]** | Direct search enters through an application: pattern search for user-provided points (molecular geometry); space mapping and surrogates; a 2004 surrogate-optimization special issue co-edited with Audet and Dennis. Derivative-based NLP continues (inexact SQP 2002, interior-point filter 2004, to 2008) | Application contact; the user's own point generator placed in the search step | [S106 pp. 1–3; S025 pp. 5–6, 9–10; S062; S044; H001; S013; S007; S077; S085] |
| 2007 | SID-PSM (with Custódio); PSwarm (with Vaz). Pivot into DFO, specifically direct search (**[full text]** correction: direct search starts in 2001 [S106]; 2007 is when it becomes the main line) | *Inference*: a Dennis student moving from trust-region NLP into the Rice direct-search tradition, now with a first PhD student of Vicente's own | SIOPT 18 (2007); JOGO 39 (2007) |
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

1. **NLP (trust-region interior-point) → direct search (~2000s)**. Trigger undocumented. *Inference*: the Rice/Dennis direct-search environment plus a first PhD student (Custódio) working on simplex derivatives. **[full text]**: the documented entry is an application in 2001–2004, where a user routine proposes points in the search step of pattern search; the stated paradigm is that the user and the algorithm together, not the algorithm alone, generate new points (paraphrase) [S106 p. 1; S025 p. 1].
2. **Convergence → complexity (2013)**. *Inference*: field-wide complexity turn. Vicente's contribution was to make direct search countable via sufficient decrease.
3. **Deterministic → probabilistic (2014–2015)**. Stated trigger: numerical evidence that random polling without positive spanning did better (GRVZ 2015 abstract).
4. **DFO → ML-flavoured stochastic multi-objective/bilevel (2019 → )**. Coincides with the Lehigh move. Motive stated only generically (02, S1, S6).
5. **Back to stochastic DFO sampling (2022 → 2026)**. A convergence of pivots 3 and 4: noise-aware acceptance tests.

## Entry/exit timing (inference)

- Enters directions **after** a numerical or modelling signal (random directions, multiobjective engineering needs, fairness trade-offs) and **when** an analysis tool is available (sufficient-decrease counting; martingale arguments from the TR 2014 work).
- No documented exit; lines are handed to students, who continue them (Custódio co-authored DMS; Royer carried probabilistic DS through 2019).


## Trajectory as seen in the full texts (2026-09-27)

Source: `08-deep-reading-synthesis.md` §8–§9, built from the 124 paper cards. Card ids point to `07-paper-cards.md`.

### Periods and turns

1. **1991–1995, bilevel and test problems (Coimbra/Waterloo/GERAD)**: a classified bilevel bibliography [S002], test-problem generators with known minima [S053; S026; D001; S033; S063], descent methods and hardness results [S004; S069], optimality conditions [S052]. Seven of its twelve works are abstract-level and one is metadata-only.
2. **1996–2000, derivative-based NLP at Rice**: trust-region interior-point SQP for optimal control, the thesis and TRICE [S040; S011; S037; S031; H007], the interface paper [S048], local theory [S084; H002; H003], two-step algorithms [S039]. Seven single-authored works in five years.
3. **2001–2005, transition**: derivative-based work continues (inexact SQP [S013], degenerate NLP [S054; S076], multipliers [S095; S098], filter interior point [S007]); direct search enters through an application (molecular geometry) [S106; S025]; surrogates through space mapping [S062; S044] and a surrogate-optimization special issue [H001]; the 2001 overview maps local NLP as components [S056 pp. 7–9].
4. **2006–2010, direct search made efficient + model geometry**: PSwarm [S005; S018], SID-PSM [S008; S030; S059; S012], the Conn–Scheinberg geometry and DFO trust-region papers [S010; S020; S006], the book [S001], bilevel as multicriteria [S022]; interior-point work ends here [S077; S085].
5. **2011–2015, new classes + complexity + probability**: DMS [S003], discontinuous functions [S024], merit functions [S049], ES [S050; S057], bilevel DFO [S047], sparse models [S029; S051], complexity [S023; S034], probabilistic models and descent [S014; S019].
6. **2016–2020, complexity programme and Toulouse collaborations**: [S032; S041; S046; S074; S027; S060; S108]; probabilistic extensions [S043; S045]; multiobjective complexity [S015]; survey [S038]; applications [S035; S036; S068].
7. **2021–2026, Lehigh: stochastic ML-facing methods**: stochastic multiobjective learning [S094; S016; S065; S093; S017; S101; S111], bilevel and trilevel stochastic gradient [S070; S042; S091], stochastic DFO [S067; S102; S110], full-low evaluation [S073; S088], a negative result on neural surrogates [S079], knee solutions [S096], sports analytics [S086; S092; S120]. The recurring framing is "the first stochastic version of a known formalism" (a field-wide trend of the period, recorded here, not as taste) [S042 p. 5; S070 p. 1; S091 pp. 1–2; S101 p. 3; S017 p. 5; S067 p. 4; S110 p. 4].

### What stayed constant

- **Keep the skeleton, change one object**: 1996 [S037 pp. 5–7; S040 p. 103] to 2026 [S110 p. 4].
- **Inexactness tied to progress**: 1996 [S040 p. 136], 2002 [S013 p. 10], 2012 [S047 p. 8], 2024–2025 [S088 pp. 13–14; S042 pp. 13–14].
- **Artefacts**: generators 1993–94 [S053 p. 14; D001], TRICE and the interface 1997–99 [H007 p. 3; S048], PSwarm/SID-PSM 2007–09 [S005 p. 14; S059], DMS collection 2011 [S003 p. 15], GitHub code 2022–25 [S016 p. 5; S042 p. 22; S091 p. 7].
- **Publishing the boundary** (SKILL.md heuristic H10; proposed as a Method 6 and demoted on review, see 08 §4.1): 1998 [H003 pp. 4, 18–19] to 2026 [S110 p. 14].
- **Applications**: circuits [S039 pp. 17–18], molecules [S106; S025], superconductivity [S044 p. 18], finance [S028; S087; S061], astrophysics [S075; S082], data assimilation [S043], geophysics [S068], medicine [S035], manufacturing [S036; S078], transport [S080], fairness [S016; S101], sports [S086; S092]. A 2006 essay ties applications to academics' own research portfolio and contacts [S109 pp. 4–5].

### Collaboration pattern

| Period | Works | Single-authored | Top coauthors |
|---|---|---|---|
| 1991–1995 | 12 | 1 | Calamai 7, Júdice 6 |
| 1996–2000 | 16 | 7 | Dennis 3, Heinkenschloss 2 |
| 2001–2005 | 13 | 4 | Alberto 2, Nogueira 2, Rocha 2, S. J. Wright 2 |
| 2006–2010 | 16 | 2 | Conn 4, Scheinberg 4, Custódio 4, Vaz 2, R. Silva 2 |
| 2011–2015 | 20 | 1 | Vaz 5, Gratton 5, Bandeira 3, Scheinberg 3 |
| 2016–2020 | 17 | 0 | Gratton 8, Z. Zhang 4, Royer 4, Vaz 2, Dodangeh 2 |
| 2021–2026 | 26 | 2 | Giovannelli 10, S. Liu 5, Sohab 3, Kent 3 |

- Long pairings of 5–15 years, one or two per period, each tied to a line of work: Calamai and Júdice (bilevel, generators); Dennis and Heinkenschloss (derivative-based NLP); Conn and Scheinberg (model geometry, probabilistic models); Custódio and Vaz (direct search); Gratton, Royer and Zhang (complexity and probability); Liu and Giovannelli (stochastic ML).
- Solo research work concentrates early (11 of 13 single-authored research works in 1991–2005); none after 2013 [S023].
- Specialist coauthors bring certified tools: PDE control [S044], SDP solvers [S028; S087], DC programming [S064; S097], compressed sensing [S051; S029], discrete geometers acknowledged [S041 pp. 7, 9].
- Service (not research method): SIAG/OPT chair 2023–2025, confirmed by his signed Chair's Columns [S122 pp. 23–24; S121 p. 14].

### Pivots, revisited

1. NLP → direct search: documented entry through an application in 2001 [S106; S025]; direct search becomes the main line with PSwarm and SID-PSM in 2007.
2. Convergence → complexity (2013): single-authored opener [S023], every comparison with 2004–2012 derivative-based complexity results [S023 pp. 2, 8–9].
3. Deterministic → probabilistic (2014–2015): the stated trigger is the random-direction numerics of the merit-function paper [S049 pp. 14–15, 17; S019 p. 2] and the probabilistic-models trust-region paper [S014].
4. DFO → ML-facing stochastic methods (2019 →): no personal explanation found; the only signed sentence is field-level [S121 p. 14].
5. Back to stochastic DFO sampling (2022 → 2026): the tail bound [S067], whose own Remark 5.1 discloses that fewer samples per iteration need not reduce total cost [S067 p. 20]; the sequential-test paper takes up that caveat as its entry point [S102 p. 3]; then non-monotone acceptance [S110].
