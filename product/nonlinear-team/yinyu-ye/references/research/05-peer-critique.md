# 05 · Peer critique: where others found Yinyu Ye's methods limited, superseded or wrong, and how he answered

> **Researcher:** Yinyu Ye (叶荫宇), K. T. Li Professor of Engineering (Emeritus), Stanford MS&E / ICME; since 2024 also at SJTU Antai and other Chinese institutions (see `01-publications.md`).
> **Dimension:** research agent 05 of 06, peer critique (nuwa research-craft, Phase 1). The note covers failed or improved-upon results, published objections, counterexamples, public reviews and rebuttals, rival schools, competing methods and independent benchmarks. The purpose is to find blind spots, limits of applicability and judgements later shown wrong, and to record for each critique who made it, where, and whether and how it was answered.
> **Research date:** 2026-09-28.
> **Sources consulted:** 74, listed under "Sources" (24 primary, 50 secondary; three of the secondary items, the NeurIPS review pages, also contain the group's own author feedback). Of these, 20 were read in full or searched in full text (including web pages), 30 at abstract level, and 24 were bibliographic records only (marked "not read"). Every identifier below was checked in this run with Crossref, OpenAlex, arXiv abstract pages, Optimization Online or the NeurIPS proceedings site. **WebSearch calls used: 1 of 2.** The one search returned nothing usable.
> **User-supplied material:** none. `references/sources/{papers,talks,essays,software}/` held only `.gitkeep`. `private/` was not opened. No transcripts were saved to `sources/talks/`.
> **Tags:** [stated] = what Ye (or a paper, deck or rebuttal from his group) says. [practice] = what he or his group did, shown by papers, code, versions or records. [observed] = what third parties (critics, reviewers, rival teams, benchmark maintainers) say or show. [inferred] = my reading, with the basis given. (P) = primary, (S) = secondary. [Sn] points to the numbered source list.
> **Authorship caveat, which applies throughout:** after about 2010 Ye is usually last author of team papers (see `01-publications.md` §0). Rebuttals and paper text speak for the group. Nothing here shows which words are Ye's own. Critiques of those papers are critiques of his group's practice under his seniority, not necessarily of his personal choices.
> **Era caveat:** the critiques span 1994 to 2026. The early ones (IPM theory against practice, sensor-network SDP) come from an era of Netlib-sized LPs, Matlab plus SeDuMi and 1–3-author papers. The late ones (NeurIPS reviews, GPU benchmarks) come from a field with ML-venue refereeing, GPU hardware and teams of 5–11 authors. Each item gives its era.

---

## 0. Critique register (summary)

| # | Target (Ye's work or claim) | Critic and source | Kind | Answered? How |
|---|---|---|---|---|
| A1 | Simplex / policy-iteration bound for discounted MDPs (MOR 2011) | Hansen, Miltersen & Zwick, JACM 2013 [S27] | improved bound, wider scope | Yes: Ye cites the improvement on his own slides [S32] |
| A2 | Open question: are these methods polynomial when the discount rate is part of the input? | Hollanders, Delvenne & Jungers, CDC 2012 [S28]; Feinberg & Huang, ORL 2014 [S29] | negative answer for Howard's PI; a negative result for value iteration | Partly: Feinberg–Huang is listed on Ye's 2023 slide; Hollanders et al. do not appear in its extracted text [S32] |
| A3 | Vavasis–Ye layered-step IPM (MP 1996) | Monteiro & Tsuchiya, SIOPT 2003 [S24]; Megiddo, Mizuno & Tsuchiya, MP 1998 [S23]; Dadush, Huiberts, Natura & Végh, STOC 2020 / MP 2023 [S25] | needs a quantity "very hard to compute"; not scale-invariant | Yes: Ye co-presented the scale-invariant fix with one of its authors in 2023 [S33] |
| A4 | .699 approximation for Max-Bisection (MP 2001) | Halperin & Zwick, RSA 2002 [S50]; Feige & Langberg 2006 [S51] (not read) | improved ratio | No reply found. Ye left SDP approximation algorithms soon after |
| A5 | Online LP with dual prices (Agrawal–Wang–Ye, OR 2014) | Kesselheim, Radke, Tönnis & Vöcking, arXiv 2013 / STOC 2014 / SICOMP 2018 [S34] | exponentially weaker capacity-ratio requirement, obtained without dual prices | Indirectly: the Ye school stayed with dual prices and changed what is measured (regret, flops) [S35][S36] |
| A6 | cuPDLP-C: "this breakthrough" and "profound impact" (arXiv 2023) | HiGHS docs [S9]; Gurobi 13.0 docs [S7]; Mittelmann LPfeas benchmark, 2026 [S15]; rivals HPR-LP [S61] and cuPDLPx [S60] | prediction partly borne out, but the specific code was superseded | Group's answer: hybrid first-order + IPM + crossover (see `01` M8) |
| A7 | DRSOM "Good potential to be a standard optimizer for deep learning!" (talk, 2023) | none found | prediction not borne out in the evidence I could check | The claim was dropped from the paper (see `03` K3) |
| A8 | "IPM strikes back" complexity baseline (NeurIPS 2019) | NeurIPS reviewers and meta-reviewer [S37] | baseline derivation "not quite correct" | Accepted on the condition that a derivation be added |
| B1 | HSD as the universal certificate machine (Ye's stated belief R8 in `02`) | Permenter, Friberg & Andersen, SIOPT 2017 [S12]; Mittelmann infeasible-SDP benchmark [S13] | fails on weakly infeasible or ill-posed problems | No reply from Ye found |
| B2 | HSD running time | Freund, MIT OR Center WP 2004 / MP 2006 [S11] | stopping rule depends on solution sizes and initial residuals | No reply found |
| B3 | "implementaed in all Linear Programming Commercial Solvers" (homepage) | Gurobi docs [S7]; SDPT3 [S10]; Gondzio 2012 [S6]; MOSEK docs [S8] | implemented, but not the default in most codes | Not addressed |
| B4 | Potential reduction as the preferred engine | Lustig–Marsten–Shanno 1994 and Todd's commentary [S2][S1]; Gondzio 2012 [S6] | practice went to path-following with Mehrotra-type correctors | Not addressed. Ye's own code behaves path-following (`03` K2) |
| B5 | SDP relaxation for sensor-network localization (2004–2007) | Tseng 2007 [S42]; Kim, Kojima & Waki 2009 [S44]; Krislock & Wolkowicz 2010 [S45]; Gouveia & Pong 2012 [S46] | slow, degenerate, weakest in a hierarchy of relaxations | Yes: further relaxations, regularization, local refinement [S41][S43] |
| B6 | Online-LP assumptions and novelty | Kesselheim et al. [S34]; NeurIPS 2020 reviewers [S36] | large, known capacity ratio; prior art (Neely 2010); weak experiments | Partly in the rebuttal; one reviewer said the main concern was not addressed |
| B7 | HSODM cost in full space | Higuchi, Poirion & Takeda, ICLR 2025 [S55] | memory "explodes to O(n^2)"; beaten by a random-subspace variant | No reply found |
| B8 | First-order LP at high accuracy | Gondzio 2012 [S6]; HiGHS docs [S9]; Mittelmann [S15] | slow at small ε; on CPU not competitive | Ye states the same limit himself in 2026 (`01`; [S64] slide 8) |
| B9 | One-phase IPM against IPOPT (Hinder & Ye 2018) | Wächter & Biegler 2000 [S19] as the rival claim; the group's own measurements [S21] | slower than IPOPT; no journal version | Candidly reported by the group |
| C1–C5 | Experimental practice at ML venues and in benchmarking | NeurIPS 2018/2019/2020 reviewers [S36–S39]; Mittelmann, Gould & Scott [S14][S17] | weak baselines, unfair metrics, unproven claims, typos, profile misuse | Mixed; see §3 and §4 |

---

## 1. Judgements superseded or shown wrong

### A1. The MDP bound was improved within two years, and Ye adopted the improvement (2011–2023)

- [observed] (S) Hansen, Miltersen & Zwick, JACM 60(1) 2013, 10.1145/2432622.2432623 [S27], abstract: "Ye [2011] showed recently that the simplex method with Dantzig's pivoting rule, as well as Howard's policy iteration algorithm, solve discounted Markov decision processes (MDPs), with a constant discount factor, in strongly polynomial time." Then: "We improve Ye's analysis in two respects. First, we improve the bound given by Ye and show that Howard's policy iteration algorithm actually terminates after at most O(m/(1−γ) log(n/(1−γ))) iterations. Second, and more importantly, we show that the same bound applies to the number of iterations performed by the strategy iteration (or strategy improvement) algorithm". (Formula typeset from the abstract's text rendering.) Scherrer, MOR 2016 (10.1287/moor.2015.0753) [S30] improves and generalizes these bounds further (record only, **not read**).
- [stated] (P) How Ye answered. His 2023 Simons workshop deck [S32] states his own bound and, on the same slide, the improved one: "The policy-iteration method actually terminates n/(1−γ)· log(m/(1−γ)), iterations with at most O(m²n) operations per iteration (Hansen/Miltersen/Zwick ACM 12)" (slide 9; fractions linearized from the extracted text). For the deterministic case, after his theorems with Post (MOR 2015, 10.1287/moor.2014.0699 [S31]), he adds "Hansen/Miltersen/Zwick 15 was able to reduce a factor m from the bound." (slide 12).
- [inferred] **Response pattern: credit the improver on your own slides and keep teaching the result as a joint line of work.** No defensive reply exists in print. The notation differs: HMZ use n for states and m for actions, and Ye's slide swaps them. The two statements are consistent once that is taken into account.

### A2. The open question Ye left was closed negatively for Howard's method (2012–2014)

- [stated] (P) The 2011 paper (MOR 36, 10.1287/moor.1110.0516 [S26]) leaves open whether the methods are polynomial when the discount rate is an input (`01` SW4). The 2023 deck still asks: "Is there a strongly polynomial-time algorithm for MDP regardless the discount factor?" [S32, slide 14].
- [observed] (S) Hollanders, Delvenne & Jungers, CDC 2012, 10.1109/cdc.2012.6426485 [S28], abstract: "it was shown that PI runs in strongly polynomial time on discounted-reward MDPs, yet only when the discount factor is fixed beforehand. In this work, we show that PI needs an exponential number of steps to converge on discounted-reward MDPs with a general discount factor." HMZ's abstract [S27] also sums up: "it is strongly polynomial for a fixed discount factor, and exponential otherwise."
- [observed] (S) Feinberg & Huang, "The value iteration algorithm is not strongly polynomial for discounted dynamic programming", ORL 42 (2014) 130–131, 10.1016/j.orl.2013.12.011 [S29] (title and record only; **not read**).
- [stated] (P) Ye's 2023 slide files these under progress: "Renewed exciting research work on the simplex method, e.g., Feinberg/Huang 2013, Lee/Epelman/Romeijn/Smith 2013, Scherrer 2014, Fearnley/Savani 2014, Adler/Papadimitriou/Rubinstein 2014, etc." [S32, slide 14]. A text search of the extracted deck finds no mention of Hollanders or Jungers.
- [inferred] His open question survives because it asks about *any* algorithm. The specific method he analysed is now known to be exponential in that regime. **Limit of applicability: "strongly polynomial" in his MDP work holds only for a fixed discount factor, and that is a real restriction, not a technicality.**

### A3. Vavasis–Ye (1996): an unknowable input, and a lack of scale invariance

- [practice] (P) Target: Vavasis & Ye, MP 74 (1996), 10.1007/BF02592148 [S22].
- [observed] (S) Monteiro & Tsuchiya, SIOPT 13(4) 2003, 10.1137/s1052623401388926 [S24], abstract: "Vavasis and Ye's algorithm requires explicit knowledge of χ̄_A (which is very hard to compute or even estimate) in order to compute the layers for the LLS direction." They also note that Megiddo, Mizuno & Tsuchiya (MP 82, 1998, 10.1007/bf01580074 [S23], **not read**) removed that need, but their "algorithm needs to compute n LLS directions on every iteration".
- [observed] (S) Dadush, Huiberts, Natura & Végh (STOC 2020, 10.1145/3357713.3384326; MP 2023, 10.1007/s10107-023-01956-2; arXiv 1912.06252) [S25], abstract: "Monteiro and Tsuchiya … noting that the central path is invariant under rescalings of the columns of A and c, asked whether there exists an LP algorithm depending instead on the measure χ̄*_A … We resolve this open question affirmatively."
- [stated] (P) How Ye answered. The 2023 Simons bootcamp deck, co-authored and co-presented with Bento Natura (one of the four authors above) and Takashi Tsuchiya (the critic), says of his own algorithm: "The algorithm is not scale-invariant." (slide 9). The next slide is titled "Scale-Invariant Improvements" and states the Dadush–Huiberts–Natura–Végh theorem [S33, slides 9–10]. `02-methodology.md` records the same line.
- [inferred] **Response pattern: concede the limitation in the open and teach the fix together with the people who found it.** This is the most direct acknowledgement of a critique I found.

### A4. Max-Bisection .699 (2001) was improved in the next year

- [observed] (S) Halperin & Zwick, RSA 20 (2002) 382–402, 10.1002/rsa.10035 [S50], abstract: "Our results improve, extend and unify results of Frieze and Jerrum, Feige and Langberg, Ye, and others." The improved ratios are not in the abstract and I did not check them. Feige & Langberg's RPR² paper (J. Algorithms 60, 2006, 10.1016/j.jalgor.2004.11.003 [S51]) is **not read**.
- [practice] (P) Ye's own paper: "A .699-approximation algorithm for Max-Bisection", MP 2001, 10.1007/pl00011415 [S49]. After about 2003 his record shows no further SDP-rounding ratio papers (see `01` §1.2).
- [inferred] No reply. It looks like a field he passed through and left once the tool (SDP rounding) had been shown to work.

### A5. Online LP: a rival showed dual prices were not needed and cut the capacity requirement exponentially

- [practice] (P) Agrawal, Wang & Ye, "A Dynamic Near-Optimal Algorithm for Online Linear Programming", OR 62 (2014), 10.1287/opre.2014.1289 [S57]. The arXiv version is cited by the critics as abs/0911.2974.
- [observed] (S) Kesselheim, Radke, Tönnis & Vöcking, arXiv 1311.2578 v1 (full text read; STOC 2014, 10.1145/2591796.2591810; SICOMP 47 2018, 10.1137/15m1033708) [S34]:
  - p. 1: "Our result improves exponentially on previous work with respect to the capacity ratio. In contrast to existing results on packing LP problems, our algorithm does not use dual prices to guide the allocation of resources over time."
  - p. 4: "Agrawal et al. needed the assumption B = Ω(m log(nK/ε)/ε²) or OPT = Ω(c_max m² log(n/ε)/ε²)." (fractions linearized from the PDF layout)
  - p. 4, the other side: "Additionally, the second paper provided a lower bound on B of B = Ω(log m/ε²) to allow for (1 − ε)-competitive algorithms. This bound is matched by our current result." So Ye's group supplied the lower bound that the rival then matched.
- [stated] (P) How the school answered, eight years later. Li & Ye, OR 2022, 10.1287/opre.2021.2164 [S35], abstract: "Virtually all existing online algorithms were based on learning the dual optimal solutions/prices of the linear programs (LPs)". It then poses "two major open questions" (convergence of the learned dual prices, and LPs with coefficients of either sign) and answers both, under an i.i.d. input model with regret bounds. The NeurIPS 2020 rebuttal (Li, Sun & Ye) [S36] argues on cost: "our algorithm has a strongly polynomial O(nnz(A)) flop complexity (linear in the number of non-zero entries in A), while the previous OLP algorithms all require solving O(log n) or O(n) of LPs … For example, Agrawal et al. (2014) solved O(log n) LPs and Kesselheim et al. (2014) solved O(n) LPs."
- [inferred] **Response pattern: do not contest the rival's bound. Keep the dual-price lens (belief R7 in `02`) and move the comparison to axes where it wins: computation per step, regret, general-sign data.**

### A6. cuPDLP-C's "breakthrough" (2023): the prediction partly came true, but the code was superseded

- [stated] (P) cuPDLP-C, arXiv 2312.14832 v2 (Lu, Yang, Hu, Huangfu, Liu, Liu, Ye, Zhang, Ge) [S59], abstract: "We also discuss the profound impact this breakthrough may have on mathematical programming research and the entire operations research community."
- [observed] (S) Adoption by rival solvers, as of 2026-09-28:
  - HiGHS docs [S9]: "HiGHS includes the cuPDLP-C primal-dual hybrid gradient method for LP (PDLP), and also has a native PDLP solver, HiPDLP." The same page adds a limit: "On a CPU, they are unlikely to be competitive with the HiGHS interior point or simplex solvers."
  - Gurobi 13.0 parameter reference [S7] lists "6=PDHG (Primal-Dual Hybrid Gradient)" among Method options and a `PDHGGPU` parameter ("By default, the PDHG algorithm runs on the CPU"). The docs I read do not name the lineage, so **Gurobi's debt to cuPDLP-C specifically is not established**.
- [observed] (S) Mittelmann's LPfeas benchmark, 16 Sep 2026 [S15] (tolerance 1e-6 for all codes; "COPTG has barrier accuracy (1e-8)"). The "scaled" row of shifted geometric means, with instances solved out of 65:

  | COPT | MOSEK | HiGHS | KNITRO | PDLP (OR-Tools) | XOPT | cuOpt | cuPDLPx | COPTG | HPR-LP-C |
  |---|---|---|---|---|---|---|---|---|---|
  | 1.67 (65) | 5.90 (56) | 16.9 (55) | 23.0 (48) | 27.8 (50) | 9.63 (59) | 1.17 (62) | 2.43 (57) | 1.29 (64) | 1 (63) |

  cuPDLP-C itself is not in the table. The GPU first-order entries are cuPDLPx (Lu, Peng & Yang; arXiv 2507.14051 [S60], without Ye) and HPR-LP-C (Chen, Sun, Yuan, Zhang & Zhao; arXiv 2408.12179 [S61]; its abstract claims "2.39x to 5.70x speedup … over the award-winning solver PDLP"). HPR-LP-C has the best mean. The GPU codes ran on an NVIDIA B200 and the CPU codes on an i7-11700K, so the rows are not like-for-like.
- [inferred] The broad bet (GPU first-order LP becomes a standard option in major solvers) looks right in 2026. The specific artefact was overtaken within about two years, by a co-author's next code and by a rival school (the Sun–Toh splitting line). COPT (the solver Ye led) is the fastest CPU code and COPTG is near the top, which fits his hybrid "first-order then second-order" strategy (`01` M8) better than a pure-PDLP claim does. On the hardware and ranking caveats, see C5 below.

### A7. "Good potential to be a standard optimizer for deep learning!" (DRSOM, 2023)

- [stated] (P) Talk slide, 2023-06-30 (quoted in `03` K3 and `01` SW5).
- [practice] (P) The DRSOM paper's v3 (2023-07-02) dropped the neural-network experiments (`03` §5.1). arXiv 2208.00208 v3 [S58] now lists "L_2 − L_p minimization, CUTEst problems, and sensor network localization".
- [observed] (S, weak) An arXiv abstract search for "DRSOM" on 2026-09-28 returns only 2208.00208 itself. I found no third-party DL paper that adopts it. **This is an abstract-level search only. Full-text mentions and ML-venue usage were not checked.**
- [inferred] As far as I could check, the prediction has not come true, and the group quietly stopped making it in print.

### A8. The complexity baseline in "Interior-Point Methods Strike Back" (NeurIPS 2019) was judged incorrect

- [practice] (P) Ge, Wang, Xiong & Ye, NeurIPS 2019 (proceedings hash 0937fb58…, Paper ID 3743) [S37]. The public Reviews, Meta-Review and Author Feedback were read in full.
- [observed] (S) Reviewer 2 (after the feedback): "I'm not convinced by the author's response to my question on showing the derivation of the previous best run time. They need to use more current algorithms for LP (for example, the one by Cohen, Lee, and Song) in order to compute how fast this problem can be solved."
- [stated] (P) The rebuttal had said: "Thus O(N³m⁴) directly comes from formulating and solving the normal equations in one iteration via direct matrix multiplication and Cholesky decomposition. Possibly O(N³m⁴) can be improved by techniques such as fast matrix multiplication, but not too much."
- [observed] (S) Meta-review: "One condition for us to accept your revision: Please add a clear derivation of the previous best run times for this problem. Also revise in light of the fact that the current method of computing the previous best run time (as they described in the rebuttal) is not quite correct, since it does not use the current fastest LP algorithms for the computations".
- [inferred] **Blind spot: the group's complexity comparisons use the classical-IPM cost model (direct factorization, n³), not the fast-LP-solver literature of theoretical CS.** The paper was accepted, but the referees did not accept its framing of "previous best".

### A9. A published correction exists whose content I could not read

- [practice] (P) Burer & Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", MP 2021, 10.1007/s10107-021-01684-5 [S65], correcting MP 2020 (online 2019), 10.1007/s10107-019-01367-2. The arXiv record 1802.02688 (v2, Nov 2018) predates it and says nothing about the correction. **Content not read** (Springer returned a client challenge). Whether the error came from the authors or from a reader is unknown.

---

## 2. Limits of applicability that others established

### B1. HSD certificates fail on weakly infeasible and ill-posed problems (2017–2025)

- [stated] (P) Belief R8 in `02`: an algorithm should certify infeasibility through a homogeneous, one-phase design.
- [observed] (S) Permenter, Friberg & Andersen, SIOPT 27(3) 2017, 10.1137/15m1049415 [S12], abstract: "we show that the self-dual homogeneous model returns facial reduction certificates when it fails to return a primal-dual optimal solution or a certificate of infeasibility." They then give a facial-reduction algorithm that "in principle, always succeeds", and "numerical experiments illustrating barriers to practical implementation." Andersen was Ye's visiting PhD student and the MOSEK founder (`01` §1.3), so this critique comes from **inside the HSD school**.
- [observed] (S) Mittelmann, "Infeasible SDP Benchmark", 21 Sep 2025 [S13], on the Pataki–Liu instances: "A (Farkas) certificate of infeasibility is provided by only some of the solvers and only for the strongly infeasible instances." COPT-8.0.0 (the solver Ye led) reports infeasibility in 99, 100, 56 and 100 of 100 cases on the four *strongly* infeasible families, and in 0 of 100 on each of the four *weakly* infeasible families. MOSEK scores 86 on one weak family, marked "* reports ill-posed". SDPA reports 100 everywhere.
- [practice] (P) The group's own HDSDP paper admits a related gap for dual methods: they "still suffer from failure to identify primal infeasibility" (`03` §4 / K1).
- [inferred] **Limit: "certify infeasibility" holds for strongly infeasible problems. For weak infeasibility and failures of Slater's condition, homogeneous embedding alone is not enough, and facial reduction is the known remedy.** I found no reply from Ye.

### B2. HSD running time depends on the sizes of the solutions (2004)

- [observed] (S) Freund, "On the Behavior of the Homogeneous Self-Dual Model for Conic Convex Optimization", MIT OR Center WP 372-04 (Optimization Online 2004/10/977, full text searched; MP 106, 2006, 10.1007/s10107-005-0667-3) [S11], abstract: "a standard stopping rule implicitly involves the sum of the sizes of the ε-optimal primal and dual solutions, as well as the size of the initial primal and dual infeasibility residuals. This theory suggests possible criteria for developing starting points for the homogeneous self-dual model that might improve the resulting solution time in practice." His open question (p. 15): what are "the relevant behavioral measures … for an instance of P/D in which one or both problems are infeasible?"
- [inferred] This is friendly critique: it takes Ye–Todd–Mizuno and Xu–Hung–Ye (both cited) as the model and shows where scaling and starting points matter. It links to Ye's own work on warm-starting HSD (Skajaa, Andersen & Ye 2013, `01` SW2). No direct reply found.

### B3. "Implemented in all LP commercial solvers": implemented, but seldom the default

- [stated] (P) Homepage [S63]: "Predictor-Corrector IPM and Homogeneous and Self-Dual Algorithm that are implementaed in all Linear Programming Commercial Solvers" (sic).
- [observed] (S) Rival solvers' documentation, 2026:
  - **MOSEK** (C API 11.2.4, §13.2.2) [S8]: "This is the reason why MOSEK solves the so-called homogeneous model". This is the default design, from Ye's student Andersen (Andersen & Andersen 2000, 10.1007/978-1-4757-3216-0_8 [S70]).
  - **Gurobi** 13.0, `BarHomogeneous` [S7]: "At the default setting (-1), it is only used when barrier solves a node relaxation for a MIP model. … The homogeneous algorithm is useful for recognizing infeasibility or unboundedness. It is a bit slower than the default algorithm."
  - **SDPT3** 4.0 (Toh, Todd & Tütüncü; Todd is Ye's HSD co-author) [S10]: "It employs an infeasible primal-dual predictor-corrector path-following method … The current version also implements algorithms for solving a 3-parameter homogeneous self-dual model".
- [observed] (S) Gondzio, "Interior point methods 25 years later", EJOR 218 (2012), 10.1016/j.ejor.2011.09.017 (ERGO-2011-003, full text searched) [S6]:
  - p. 2: "It is broadly accepted today that an infeasible-primal-dual algorithm is the most efficient interior point method."
  - p. 15 credits practical efficiency to "Mehrotra's predictor-corrector technique".
  - A text search of the 33 pages finds no "homogeneous", "self-dual", "embedding" or "Ye".
- [inferred] The claim holds if "implemented" means available. Where Ye's student built the solver (MOSEK), HSD is the default. Elsewhere the default is infeasible primal-dual path-following, and the predictor–corrector in production codes is Mehrotra's heuristic, not the Mizuno–Todd–Ye scheme the homepage lists first (`01` SW2). See Contradiction K1.

### B4. Potential reduction lost to path-following in practice (1994 onward)

- [observed] (S) Lustig, Marsten & Shanno, ORSA J. Comput. 6(1) 1994, 10.1287/ijoc.6.1.1 [S2], abstract: the survey concentrates "on the many variants that can be derived from logarithmic barrier methods", with "Full implementation details of the primal-dual predictor-corrector code OB1".
- [observed] (S) Todd (Ye's frequent co-author), "Commentary—Theory and Practice for Interior-Point Methods", 10.1287/ijoc.6.1.28 [S1], abstract: the practical experience "raises some questions: why does the primal-dual method allow such long steps (99.95% of the way to the whereas primal or dual affine-scaling methods seem limited to, say, 95%)? … And why does the primal-dual affine-scaling algorithm perform poorly, while even tiny centering components render it highly efficient?" (words appear to be missing after "the" in the abstract as published; quoted as it stands). The rejoinder "The Last Word on Interior Point Methods for Linear Programming—For Now" (10.1287/ijoc.6.1.35 [S3]) is **not read** beyond its one-line abstract. I did not check whether Ye wrote a commentary in that issue; Crossref showed commentaries by Todd and Vanderbei.
- [observed] (S) Todd's survey "Potential-reduction methods in mathematical programming", MP 76 (1997) 3–45, 10.1007/bf02614377 [S4], and Anstreicher's "Potential Reduction Algorithms" (1996), 10.1007/978-1-4613-3449-1_4 [S5]: **not read** (the Cornell eCommons copy sits behind a bot challenge; no abstract in Crossref or OpenAlex).
- [practice] (P) `03` K2: Ye's own `HSDLPsolver.m` is labelled "Primal-Dual Potential-Reduction Algorithm" but takes fixed fraction-to-boundary steps with a centrality switch, which is path-following behaviour.
- [inferred] Ye's 2023 preference for "a single merit-function driven algorithm" (`02` C4) runs against 30 years of practice, and also against how his own code behaves. **Limit: potential reduction is his proof engine, not the field's production engine.** No published reply to the path-following camp was found.

### B5. SDP for sensor-network localization: slow, degenerate, weakest in the hierarchy, fragile under noise (2006–2012)

- [practice] (P) Target: Biswas & Ye, IPSN 2004, 10.1145/984622.984630 [S40], and the So–Ye theory paper [S48].

- [observed] (S) Tseng, SIOPT 18 (2007), 10.1137/050640308 [S42], abstract: "Recently Biswas and Ye proposed a semidefinite programming (SDP) relaxation of this problem which has various nice properties … Here, we study a second‐order cone programming (SOCP) relaxation of this problem, motivated by its simpler structure and its potential to be solved faster than SDP. We show that the SOCP relaxation, though weaker than the SDP relaxation, has nice properties that make it useful as a problem preprocessor."
- [observed] (S) Kim, Kojima & Waki, SIOPT 20 (2009), 10.1137/080713380 [S44], abstract: "the sparse SDP relaxation applied to the QOP is at least as strong as the Biswas–Ye SDP relaxation", and "much faster than the Biswas–Ye SDP relaxation".
- [observed] (S) Krislock & Wolkowicz, SIOPT 20 (2010), 10.1137/090759392 [S45], abstract: "The resulting SDP is solved using primal-dual interior point solvers, yielding an expensive and inexact solution. This relaxation is highly degenerate in the sense that the feasible set is restricted to a low dimensional face of the SDP cone, implying that the Slater constraint qualification fails." Their method uses "No SDP solvers".
- [observed] (S) Gouveia & Pong, COAP 2012, 10.1007/s10589-011-9431-1 (Optimization Online abstract) [S46]: "we show that Biswas and Ye's SDP relaxation is equivalent to the degree one SOS relaxation of Kim et al. We also show that Nie's sparse-SOS relaxation is stronger than the edge-based semidefinite programming (ESDP) relaxation".
- [observed] (S) Javanmard & Montanari, FoCM 2013, 10.1007/s10208-012-9129-5 (arXiv 1103.1417) [S47]. For a random geometric graph with bounded noise they "obtain upper and lower bounds on the reconstruction error that match up to a factor that depends only on the dimension". This is third-party theory for the noisy regime that So–Ye's exactness theory (MP 2007, 10.1007/s10107-006-0040-1 [S48]) did not cover.
- [stated] (P) How Ye's group answered, and in part pre-empted:
  - Wang, Zheng, Ye & Boyd, SIOPT 19 (2008), 10.1137/060669395 [S43]: "the speed of the SDP approach is not satisfactory for practical applications", so they "further relax the SDP relaxation" into small sub-cones.
  - Biswas, Liang, Toh, Ye & Wang, IEEE TASE 3(4) 2006, 10.1109/tase.2006.877401 [S41], on noise: "The SDP solution usually has a rank higher than the underlying physical space which, when projected onto the lower dimensional space, generally results in high estimation error." The remedy was "a regularization term" plus using the SDP points "as the initial iterate for a gradient-descent method".
- [inferred] **Response pattern: the speed and noise critiques were met by the group itself (weaker but faster relaxations; relax, then refine locally), not by rebuttal.** The degeneracy critique (no Slater point) was answered by a rival school's facial reduction, not by Ye. Era: 2004–2010, Matlab plus SeDuMi, a single PhD student per thread.

### B6. Online LP: the assumptions and the novelty were questioned (2013–2020)

- [observed] (S) Kesselheim et al. [S34, p. 4]: "In the existing work it is generally assumed that the capacity ratios are large and that this ratio is known at the beginning."
- [observed] (S) NeurIPS 2020 public reviews of Li, Sun & Ye, "Simple and Fast Algorithm for Binary Integer and Online Linear Programming" [S36]:
  - Reviewer 1: "The setting examined has quite a lot of similarities with algorithms used in stochastic network optimization, see e.g. Neely, M.J., 2010 … Indeed, the regret bounds of Section 3 can be achieved by the following algorithm, which is a direct application of the aforementioned techniques".
  - Reviewer 2: "the standard in the literature on this problem, starting with [Kleinberg '05], is to prefer dependences on B … rather than OPT".
  - Reviewer 4 (after the rebuttal): "Unfortunately, authors did not really address my main concern - the provided experimental evaluation."
  - Meta-review, among the "main weaknesses": "The removal of positivity assumptions from the previous work, pointed out as a novel contribution, might not be technically difficult."
- [stated] (P) Rebuttal [S36]: "As mentioned by the reviewer, our algorithms share similarity with the network control algorithm in Neely, M.J. (2010), but our analysis extends their analysis (in i.i.d. setting) to the random permutation setting." On constraint violation it promised a variant "that is feasible with high probability".
- [inferred] **Blind spot: prior art from a neighbouring community (network control) was missed. The group conceded it and repositioned the contribution as analysis in a new setting.**

### B7. HSODM's full-space cost (2025)

- [practice] (P) Target: Zhang, He, Jiang, Xue, Jiang, Ge & Ye, HSODM, MOR 51 (2026), 10.1287/moor.2023.0132 [S54] (arXiv 2211.08212).

- [observed] (S) Higuchi, Poirion & Takeda, "Improving Convergence Guarantees of Random Subspace Second-order Algorithm for Nonconvex Optimization", arXiv 2406.14337 v2 ("ICLR 2025 Spotlight"; full text read) [S55]:
  - p. 5: "HSODM's space complexity explodes to O(n²) due to the Hessian, whereas the proposed method's space complexity is limited to O(sn)".
  - p. 5: "Notice that in any case (for any value of s < n) the actual execution time of the proposed method outperforms HSODM."
  - p. 3 claims the "total computational complexity, as well as space complexity, are improved over the existing algorithm (Zhang et al., 2022) in full space".
  - p. 10 notes the Ye group "vigorously using the idea of HSODM to develop various variants".
- [observed] (S) Other third-party uptake without critique: HSODM extended to bound constraints through affine scaling (Pei, Lin, Louzeiro & Zhu, arXiv 2603.05022 [S56]) and to minimax problems (Chen, Xu & Zhang, arXiv 2602.14058 [S73]).
- [inferred] The memory point depends on the implementation. Ye's group frames its second-order steps around Hessian–vector products and Lanczos (`01` SW5), where the full Hessian need not be stored. So the claim of "explodes to O(n²)" is contestable. **No reply from the group was found.** The group's own low-dimensional answer, DRSOM (2-D subspace), predates this critique.

### B8. First-order LP at high accuracy (2011–2026)

- [observed] (S) Gondzio 2012 [S6, p. 14], written before Ye's GPU turn: "There has been recently growing interest in gradient methods [84] which can only ensure O(1/ǫ) or O(1/ǫ2) terms in their worst-case complexity results. Although they display fast initial progress to optimality they become slow if a high accuracy of solution (small ǫ) is requested."
- [observed] (S) HiGHS docs [S9] (quoted in A6) and Mittelmann's tolerance note [S15] ("the tolerance level for all codes used is 1e-6; COPTG has barrier accuracy (1e-8)").
- [stated] (P) Ye in 2026: "First-order algorithms suffer from low precision; numerically difficult problems converge slowly and unstably" (quoted in `01`; [S64] slide 8).
- [inferred] Here critic and target agree. His answer is architectural: first order to low accuracy, then IPM, then crossover (`01` M8).

### B9. One-phase IPM for NLP against the Wächter–Biegler lesson and IPOPT (2000–2019)

- [observed] (S) Wächter & Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", MP 88 (2000) 565–574, 10.1007/pl00011386 [S19]: **not read** (no abstract in Crossref or OpenAlex, and no open copy found).
- [stated] (P) Hinder & Ye, arXiv 1801.03072 [S20], abstract: "The work of Wachter and Biegler suggests that infeasible-start interior point methods (IPMs) developed for linear programming cannot be adapted to nonlinear optimization without significant modification". The paper then claims its method "fails on only 9% of the problems compared with 16% for IPOPT".
- [stated] (P) Hinder's PhD thesis (Stanford, June 2019, purl.stanford.edu/tn227rh8389; Ye's student) [S21]:
  - PDF p. 215, the group's critique of the rival design: "The algorithm IPOPT is an example of a two-phase algorithm … It is well known that this approach has drawbacks. The algorithm has difficulties detecting infeasibility [114, Table 15] and will fail if the feasibility restoration phase is called too close to the optimal solution. Some of these issues have been addressed by Nocedal, Öztoprak, and Waltz [168]."
  - PDF p. 238, its own limits: "However, IPOPT is generally significantly faster than our algorithm. It has a median runtime of 0.6 seconds per problem versus 3.3 seconds for our algorithm (including problems where the algorithm fails)."
- [practice] (P) There is no journal version of the one-phase IPM (`01`, `03`, checked 2026-09-28). The related barrier-complexity paper had results cut on reviewers' advice (arXiv 1807.00404 comment [S62]: "These results were removed due to reviewer suggestions to focus the paper on the most significant contributions").
- [inferred] This is the clearest **rival-school exchange relevant to NLP solvers**. The Ye school takes a counterexample from the IPOPT school as a challenge, answers it with an LP-style design (reduce primal infeasibility at the rate of μ), and reports robustness but not speed. **I found no published response by Wächter or Biegler, and no independent replication of the 9% vs 16% failure rates.**

### B10. Market equilibria: the polynomial path stops at linear-type utilities (context, not a critique)

- [practice] (P) Ye, "A path to the Arrow–Debreu competitive market equilibrium", MP 111 (2008; online 2006), 10.1007/s10107-006-0065-5 [S52].
- [observed] (S) Chen, Dai, Du & Teng, FOCS 2009, 10.1109/focs.2009.29 [S53], abstract: "the problem of computing an Arrow-Debreu market equilibrium is PPAD-complete even when all traders use additively separable, piecewise-linear and concave utility functions."
- [inferred] This does not target Ye, but it bounds where his IPM-for-markets approach can be expected to reach (unless PPAD ⊆ P).

---

## 3. Blind spots in experimental practice, as seen by referees and benchmarkers

This evidence comes from the only public review records I could open: the NeurIPS 2018–2020 proceedings, which publish reviews, meta-reviews and author feedback. OpenReview was behind a bot challenge (see Gaps). All four papers are team papers, and Ye's personal role is not visible.

- **C1. Baselines weaker than the strongest available.** [observed] (S)
  - NeurIPS 2019 [S37], Reviewer 1 on Sinkhorn's convolutional form: "This trick is crucial and should have been used when comparing with Sinkhorn."
  - Reviewer 3: "In addition to Gurobi, can the authors compare to CPLEX and Mosek. I have frequently found those to be faster than Gurobi for transport problems."
  - NeurIPS 2020 Conic Descent (Duchi, Hinder, Naber & Ye) [S38], Reviewer 2: "The algorithm compares only to itself in the main paper and only to the conditional gradient method in the appendix." Reviewer 4: "Lack of other baselines."
  - Meta-review [S38]: "provide more evidence of the superiority of the algorithm to other known approaches".
- **C2. The wrong unit of work.** [observed] (S) Conic Descent, Reviewer 2: "the conic descent method performs one more exact search step than the conditional gradient method. Thus, comparing only the iteration counts is not fair." After the rebuttal: "After accounting the 2x matrix-vector operations, the CG would outperform CD." [stated] (P) The rebuttal had argued on matrix multiplications: "the histogram indicates that CD empirically does better. We cannot prove why this occurs". **Unresolved** (Contradiction K4).
- **C3. Claims ahead of their proofs, and presentation.** [observed] (S)
  - Conic Descent, Reviewer 1: "The key claims related to the matrix sketching are NOT proven, or even stated formally." The same reviewer also objected to calling Burer–Monteiro a heuristic "when they do not talk about the 'Conic Descent heuristic'".
  - NeurIPS 2019, Reviewer 3 on a global-optimality reading of the free-support section.
  - NeurIPS 2018 (Sidford, Wang, Wu, Yang & Ye, "Near-Optimal Time and Sample Complexities…") [S39]. Reviewer 3: "there are a lot of typos, hindering the correct understanding of it … I think this paper is not ready to be published until its incorrectness can be corrected and modified." Reviewer 1: "the proof of the second inequality of Lemma C.3 doesn't seem valid". Reviewer 2: it "fills just a small (and in my opinion not that significant) gap in a research direction that I personally do not consider that important." (2018 published no author feedback, so no answer is visible.)
- **C4. How benchmarks are summarized.** [observed] (S) Mittelmann's benchmark index [S14]: "Note also that we do not use performance profiles. See this paper and that one We use instead the shifted geometric mean". The links point to Gould & Scott, ACM TOMS 2016, 10.1145/2950048 [S17] ("caution should be exercised when trying to interpret performance profiles to assess the relative performance of the solvers") and Fleming & Wallace, CACM 1986, 10.1145/5666.5673 [S18]. [practice] (P) Ye's group uses Dolan–Moré profiles as a main exhibit (Hinder thesis PDF p. 238 [S21]; HSODM and DRSOM, `03` B5), usually alongside shifted geometric means. [inferred] Gould & Scott's caution applies when profiles compare more than two solvers, as the HSODM benchmarks do. Nicholas Gould is a member of this team.
- **C5. The field in a benchmark "rank".** [observed] (S) Mittelmann [S14]: "For many years our benchmarking effort had included the solvers CPLEX, Gurobi, and XPRESS. Through an action by Gurobi at the 2018 INFORMS Annual Meeting this has come to an end. IBM and FICO demanded that results for their solvers be removed. … In August 2024 Gurobi decided to withdraw from the benchmarks as well and their results have been removed. On 12/24/2024 MindOpt followed suit." [stated] (P) Ye's July 2026 deck has a slide titled "Optimization Solver Rank: LP Benchmark 2026 (https://plato.asu.edu/bench.html by Hans Mittelmann)" [S64, slide 5]. The table is an image, and its content was not extracted. [inferred] A "rank" on these pages is a rank among the solvers that still participate. This is context, not a charge made by Mittelmann. [observed] (S) On the same site's sparse-SDP page (25 Apr 2026), COPT has the best scaled mean (1, 75 of 75 solved), and cuLoRADS (github.com/COPT-Public; the GPU low-rank line of arXiv 2407.15049, on which Ye is an author) scores 3.01 with 71 of 75 [S16]. Among the solvers present, COPT leads.

---

## 4. How Ye and his group answer critique (the craft signal)

Each pattern is seen at least twice. Tags as marked.

| # | Pattern | Evidence | Tag |
|---|---|---|---|
| R-1 | **Credit the improver and fold the result into your own teaching.** No reply articles | HMZ bounds on Ye's slides (A1); DHNV scale invariance co-presented with Natura (A3); Feinberg–Huang listed as "renewed exciting research" (A2) | [stated] (P) |
| R-2 | **Concede specific errors quickly and in plain words** | "It is a mistake and we'll correct it" (Cuturi citation); "MAAIPM cannot optimally solve the free support case" [S37]; "It is fair to point out that CD is a heuristic"; "We agree that the assumption that f have no nonzero direction of recession in K is cludgy" [S38]; similarity to Neely admitted [S36] | [stated] (P, group rebuttals) |
| R-3 | **Run the requested experiment during the rebuttal and report the number, even when it helps the rival** | "Mosek was tested and is much faster than Gurobi, though it is still roughly 3 times slower than MAAIPM"; on the convolutional Sinkhorn: "it indeed improved the results from Sinkhorn's side!" [S37] | [stated] (P) |
| R-4 | **When out-bounded, change the axis of comparison** | Online LP: flops per step and regret rather than capacity ratio (A5, B6); CD: matrix multiplications rather than iterations (C2); IPM on WB: cost per iteration of the normal equations (A8) | [stated]/[inferred] |
| R-5 | **Answer limits by building the next relaxation or hybrid, not by argument** | SNL: SSDP/ESDP, regularization, local refinement (B5); first-order accuracy: FO → IPM → crossover (B8); DRSOM's Assumption (c) repaired by HSODM (`01` SW5) | [practice] (P) |
| R-6 | **Comply with reviewers' cuts and keep the material elsewhere; narrow claims between versions** | 1807.00404 comment [S62]; DRSOM v1 → v3, UTR v1 → v4 (`03` §5.1) | [practice] (P) |
| R-7 | **Leave some critiques unanswered in print** | Weak infeasibility (B1), Freund's scaling analysis (B2), Halperin–Zwick (A4), Kesselheim's primal method (A5), RSHTR (B7): no direct reply found | [observed absence] |

- [inferred] The dominant style is **absorb and extend, not dispute**. I found no published comment, reply or rejoinder by Ye against a critic. Crossref title searches for comments on or notes about his papers returned only his own papers (Gaps). Where he does criticize, the critique targets *others'* methods, as in the next section.

### Ye as critic (brief, for contrast)

- [practice] (P) His critiques take the form of sharp constructions that settle a question. Examples: the multi-block ADMM counterexample (Chen, He, Ye & Yuan, MP 155 2016, 10.1007/s10107-014-0826-5 [S68]; the homepage says "where we settled long-time open questions" [S63]); the two-variable LP against learning the optimal basis purely from data (2026 note, `01` §1.6); and the one-phase IPM against the "two-phase or penalty" consensus (B9).
- [stated] (P) A dismissal in a talk: rival negative-curvature hybrids "seem difficult to be implemented" (`01` SW5).
- How those targets responded was not researched in this run (Gaps).

---

## 5. Index by the seven layers (framework §一)

| Layer | What peer critique shows | Items |
|---|---|---|
| 1 Taste | Theory-first taste (potential functions, HSD, complexity) is respected by peers, but production practice chose other engines. Novelty claims at ML venues were challenged on prior art | B3, B4, B6 |
| 2 Problem choice | He picks long-open questions and gets there first, but rivals often finish them (tighter bounds, scale invariance, better ratios). Fixed-discount and fixed-condition scoping define where his results hold | A1–A4, A2 |
| 3 Idea generation | "Move an LP-IPM idea into a new domain" (SNL, online LP, NLP, markets) is productive but meets domain-native rivals: facial reduction, primal random-order algorithms, network control, IPOPT-style restoration | B5, A5, B6, B9 |
| 4 Experiments | Recurring referee complaints: missing strongest baselines, the wrong unit of work, short or unreproducible experiments. Benchmarkers caution against performance profiles | C1–C4 |
| 5 Judging results | The group concedes errors and narrows claims readily. It published a correction (content unread). The DL-optimizer prediction and the "breakthrough" framing ran ahead of the evidence | A6–A9, R-2, R-6 |
| 6 Expression | Promotional abstracts and talks against candid paper bodies (`03` K4); a slide titled "Solver Rank" drawn from a benchmark that the top rivals have left | A6, C5 |
| 7 Organisation | Critiques land on student-led team papers. The answers come as new papers by the same team, or as teaching with the improvers | R-1, R-5 |

---

## 6. Solver-relevant checks derived from the critiques (for the Nonlinear Team)

[inferred] These are the questions a well-informed critic would put to a Ye-style solver proposal. Each is traced to a critique above. They are not Ye's own rules.

1. **Infeasibility claims:** test on weakly infeasible and non-Slater instances (for example the Pataki–Liu families on Mittelmann's page), not only on strongly infeasible ones. Say which kind the certificate covers (B1).
2. **Homogeneous or one-phase designs:** report the cost in time, not only robustness, against IPOPT, KNITRO or MOSEK at default settings, and track the scaling and starting-point dependence Freund identified (B2, B3, B9).
3. **Complexity baselines:** derive the "previous best" with the current fastest algorithms, not the classical Cholesky cost model (A8).
4. **Work units:** compare on matrix-vector products, factorizations or wall-clock time, not on iterations, when one method does more work per iteration (C2).
5. **Second-order subspace or eigenvector steps (DRSOM, HSODM):** state the memory model (Hessian-vector products or a stored Hessian) and compare against random-subspace variants (B7).
6. **First-order phases:** report at 1e-8 as well as 1e-6, and name the crossover or IPM handoff (B8).
7. **Summaries:** pair performance profiles with shifted geometric means and per-instance tables, and heed Gould–Scott when more than two solvers are compared (C4).

---

## Contradictions (kept, not reconciled)

- **K1. "All commercial solvers" against rival defaults.** Ye's homepage says HSD and the predictor–corrector IPM "are implementaed in all Linear Programming Commercial Solvers" [S63]. Gurobi's documentation says its homogeneous algorithm is used by default only for MIP node relaxations and "is a bit slower than the default algorithm" [S7]. SDPT3 defaults to infeasible path-following [S10]. Gondzio's survey credits Mehrotra's predictor–corrector and never mentions HSD [S6]. MOSEK does default to the homogeneous model [S8]. Both statements can be literally true ("implemented" is not "default"). The tension is kept. This extends `01` C2.
- **K2. How much faster did Karmarkar claim?** Ye's 1996/97 Preface: the speaker said the new method "would be 40 times faster than the simplex method" (main.ps, Preface) [S69]. Todd's 1994 commentary: Karmarkar "claims that his method solved problems 50 times faster than the simplex method" [S1]. The two recollections of the same era differ, and this may be a different talk or a different claim.
- **K3. Could the old IPM bound be improved much?** Rebuttal: "Possibly O(N³m⁴) can be improved by techniques such as fast matrix multiplication, but not too much." Meta-review: the method of computing the previous best "is not quite correct" [S37].
- **K4. Does Conic Descent beat conditional gradient per unit of work?** Rebuttal: "the histogram indicates that CD empirically does better". Reviewer 2 after the rebuttal: "After accounting the 2x matrix-vector operations, the CG would outperform CD." [S38]
- **K5. A reviewer question the published reviews do not contain.** The 2019 author feedback answers a Reviewer 2 "Q4": "I think it doesn't make much sense to compare an interior point method with first order methods......" [S37]. That sentence does not appear in the published text of Reviewer 2's review. The review may have been edited after the feedback. Recorded, not resolved.
- **K6. Does HSODM need O(n²) memory?** Higuchi et al.: "HSODM's space complexity explodes to O(n²) due to the Hessian" [S55]. Ye's group presents its second-order directions as eigenvector computations by Lanczos with Hessian-vector products (`01` SW5), which need not store the Hessian.
- **K7. Who closed the discount-rate question, as Ye tells it?** His 2023 slide lists five follow-up works as "Renewed exciting research work on the simplex method" [S32]. It does not list Hollanders–Delvenne–Jungers [S28], which settled the case of Howard's PI with a general discount factor negatively. The open question on the slide is phrased for any algorithm, so it remains technically open.

---

## Gaps (searched for and not found, or not read)

- **Full texts not read (paywall or bot wall):**
  - Todd's 1997 survey [S4] (Cornell eCommons: AWS-WAF challenge, HTTP 405 to curl and WebFetch);
  - Anstreicher 1996 [S5];
  - Wächter & Biegler 2000 [S19];
  - Mizuno & Todd, "On two homogeneous self-dual approaches to linear programming and its extensions", MP 89 (2001), 10.1007/pl00011413 [S67];
  - Megiddo–Mizuno–Tsuchiya 1998 [S23];
  - Feinberg & Huang 2014 [S29];
  - Feige & Langberg 2006 [S51];
  - Pong & Tseng, "(Robust) Edge-based semidefinite programming relaxation of sensor network localization", MP 130 (2011; online 2010), 10.1007/s10107-009-0338-x [S71];
  - Mittelmann, "An independent benchmarking of SDP and SOCP solvers", MP 95 (2003), 10.1007/s10107-002-0355-5 [S72];
  - the LMS rejoinder and the other 1994 commentaries [S3].
- **Book reviews of *Interior Point Algorithms* (1997)** exist and were **not read** (paywalled): Yin Zhang, IIE Transactions 31(3) 1999, 275–276, 10.1080/07408179908969827 [S66a]; J. Wilson, JORS 51 (2000), 10.2307/254021 [S66b]. Their verdicts are unknown.
- **OpenReview reviews** of the group's ICLR, ICML and NeurIPS papers from 2021 on (for example DRAG, and "Solving Linear Programs with Fast Online Learning Algorithms"): api2.openreview.net and WebFetch both returned a bot challenge. Not read and not circumvented. NeurIPS proceedings reviews after 2020 were not checked for lack of time.
- **Published comments, replies or rejoinders aimed at a Ye paper:** none found. Crossref title queries ("note on", "comment on", "counterexample") returned only Ye's own papers. This is an absence in the searches I ran, not proof that none exists.
- **Independent replication** of the one-phase IPM's 9% vs 16% failure rates, or of the DRSOM and HSODM CUTEst results: none found.
- **Responses by the critics' targets** to Ye's own critiques (multi-block ADMM, offline learning of LP bases): not researched.
- **Content of the Burer–Ye correction (2021):** not read (Springer client challenge).
- **Critiques of Ye's non-NLP lines** (DRO moment sets, Hodge ranking, MDP sample complexity after 2018): not researched, being outside the Nonlinear Team's scope. One DRO paper checked (Mohajerin Esfahani & Kuhn 2018) makes no explicit contrast with Delage–Ye in its abstract, so it is not used.
- **Who wrote the rebuttals:** the NeurIPS author feedbacks are unsigned group texts. Ye's personal share is unknown.
- **Semantic Scholar** (HTTP 429) was unavailable, so no citation-context ("citances") analysis of critical citations was done.
- **The one WebSearch** (for Todd's survey) returned only publisher and ResearchGate links, with no open full text.
- **About 5 minutes without results:** the Optima 1996 archive (Freund–Mizuno status report; URLs returned 404); SSRN and MIT DSpace copies of Freund (bot challenge; used the Optimization Online copy instead).

---

## Sources

Tags: P = primary (Ye or his group), S = secondary. "Read" levels: full = full text read or searched; abstract = abstract or record page read; record = bibliographic record only (not read).

- [S1] M. J. Todd, "Commentary—Theory and Practice for Interior-Point Methods", ORSA J. Comput. 6(1) 1994, 28–31, 10.1287/ijoc.6.1.28 — S, abstract.
- [S2] I. J. Lustig, R. E. Marsten, D. F. Shanno, "Feature Article—Interior Point Methods for Linear Programming: Computational State of the Art", ORSA J. Comput. 6(1) 1994, 1–14, 10.1287/ijoc.6.1.1 — S, abstract.
- [S3] Lustig, Marsten, Shanno, "Rejoinder—The Last Word on Interior Point Methods for Linear Programming—For Now", ORSA J. Comput. 6(1) 1994, 35–36, 10.1287/ijoc.6.1.35 — S, one-line abstract; not read.
- [S4] M. J. Todd, "Potential-reduction methods in mathematical programming", Math. Program. 76 (1997) 3–45, 10.1007/bf02614377 — S, record; not read.
- [S5] K. M. Anstreicher, "Potential Reduction Algorithms", in *Interior Point Methods of Mathematical Programming* (Applied Optimization, Springer), 1996, 10.1007/978-1-4613-3449-1_4 — S, record; not read.
- [S6] J. Gondzio, "Interior point methods 25 years later", EJOR 218 (2012) 587–601, 10.1016/j.ejor.2011.09.017 (ERGO-2011-003, https://webhomes.maths.ed.ac.uk/~gondzio/reports/ipmXXV.pdf) — S, full (searched).
- [S7] Gurobi Optimizer Reference Manual 13.0, Parameters (BarHomogeneous, Method, PDHG*, Crossover), https://docs.gurobi.com/projects/optimizer/en/current/reference/parameters.html, accessed 2026-09-28 — S, full page.
- [S8] MOSEK Optimizer API for C 11.2.4, §13.2 "Linear Optimization" / §13.2.2 "The Interior-point Optimizer", https://docs.mosek.com/latest/capi/solving-linear.html, accessed 2026-09-28 — S, page.
- [S9] HiGHS documentation, "Solvers", https://ergo-code.github.io/HiGHS/stable/solvers/, accessed 2026-09-28 — S, page.
- [S10] K.-C. Toh, M. J. Todd, R. H. Tütüncü, "On the implementation and usage of SDPT3 — a Matlab software package for semidefinite-quadratic-linear programming, version 4.0", Optimization Online 2010/06/2654 — S, abstract.
- [S11] R. M. Freund, "On the Behavior of the Homogeneous Self-Dual Model for Conic Convex Optimization", MIT ORC WP 372-04 (Optimization Online 2004/10/977); Math. Program. 106 (2006) 527–545, 10.1007/s10107-005-0667-3 — S, full (searched).
- [S12] F. Permenter, H. A. Friberg, E. D. Andersen, "Solving Conic Optimization Problems via Self-Dual Embedding and Facial Reduction: A Unified Approach", SIOPT 27 (2017), 10.1137/15m1049415 — S, abstract.
- [S13] H. Mittelmann, "Infeasible SDP Benchmark", 21 Sep 2025, https://plato.asu.edu/ftp/sdp_inf.html — S, full page.
- [S14] H. Mittelmann, "Benchmarks for Optimization Software" (index), https://plato.asu.edu/bench.html, accessed 2026-09-28 — S, full page.
- [S15] H. Mittelmann, "LPfeas Benchmark (find PD feasible point)", 16 Sep 2026, https://plato.asu.edu/ftp/lpfeas.html — S, full page.
- [S16] H. Mittelmann, "Several SDP-codes on sparse and other SDP problems (also on GPUs)", 25 Apr 2026, https://plato.asu.edu/ftp/sparse_sdp.html — S, full page (COPT 1.00 and 75/75; cuLoRADS 3.01 and 71/75; used as context only).
- [S17] N. Gould, J. Scott, "A Note on Performance Profiles for Benchmarking Software", ACM TOMS 43(2) 2016, 10.1145/2950048 — S, abstract.
- [S18] P. J. Fleming, J. J. Wallace, "How not to lie with statistics: the correct way to summarize benchmark results", CACM 29(3) 1986, 10.1145/5666.5673 — S, abstract.
- [S19] A. Wächter, L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", Math. Program. 88 (2000) 565–574, 10.1007/pl00011386 — S, record; not read.
- [S20] O. Hinder, Y. Ye, "A one-phase interior point method for nonconvex optimization", arXiv 1801.03072 — P, abstract.
- [S21] O. Hinder, *Principled Algorithms for Finding Local Minima*, PhD dissertation, Stanford University, June 2019, http://purl.stanford.edu/tn227rh8389 — P (student of Ye), full (searched).
- [S22] S. A. Vavasis, Y. Ye, "A primal-dual interior point method whose running time depends only on the constraint matrix", Math. Program. 74 (1996), 10.1007/BF02592148 — P, record.
- [S23] N. Megiddo, S. Mizuno, T. Tsuchiya, "A modified layered-step interior-point algorithm for linear programming", Math. Program. 82 (1998) 339–355, 10.1007/bf01580074 — S, record; not read.
- [S24] R. D. C. Monteiro, T. Tsuchiya, "A Variant of the Vavasis–Ye Layered-Step Interior-Point Algorithm for Linear Programming", SIOPT 13 (2003), 10.1137/s1052623401388926 — S, abstract.
- [S25] D. Dadush, S. Huiberts, B. Natura, L. A. Végh, "A scaling-invariant algorithm for linear programming whose running time depends only on the constraint matrix", STOC 2020, 10.1145/3357713.3384326; Math. Program. 2023, 10.1007/s10107-023-01956-2; arXiv 1912.06252 — S, abstract.
- [S26] Y. Ye, "The Simplex and Policy-Iteration Methods Are Strongly Polynomial for the Markov Decision Problem with a Fixed Discount Rate", MOR 36(4) 2011, 10.1287/moor.1110.0516 — P, record (content via `01` SW4).
- [S27] T. D. Hansen, P. B. Miltersen, U. Zwick, "Strategy Iteration Is Strongly Polynomial for 2-Player Turn-Based Stochastic Games with a Constant Discount Factor", JACM 60(1) 2013, 10.1145/2432622.2432623 (arXiv 1008.0530) — S, abstract.
- [S28] R. Hollanders, J.-C. Delvenne, R. M. Jungers, "The complexity of Policy Iteration is exponential for discounted Markov Decision Processes", IEEE CDC 2012, 10.1109/cdc.2012.6426485 — S, abstract.
- [S29] E. A. Feinberg, J. Huang, "The value iteration algorithm is not strongly polynomial for discounted dynamic programming", ORL 42 (2014) 130–131, 10.1016/j.orl.2013.12.011 — S, record; not read.
- [S30] B. Scherrer, "Improved and Generalized Upper Bounds on the Complexity of Policy Iteration", MOR 41 (2016), 10.1287/moor.2015.0753 — S, record; not read.
- [S31] I. Post, Y. Ye, "The Simplex Method is Strongly Polynomial for Deterministic Markov Decision Processes", MOR 40 (2015), 10.1287/moor.2014.0699 — P, record.
- [S32] Y. Ye, "Open Questions on the Markov Decision/Game Process", Simons workshop, 29 Nov 2023, https://web.stanford.edu/~yyye/MDPopenqs.pdf — P, full (text extracted in this run's scratch).
- [S33] B. Natura, T. Tsuchiya, Y. Ye, "Bootcamp: Interior Point Methods II", Simons Institute, 1 Sep 2023, https://web.stanford.edu/~yyye/BootcampIPM2.pdf — P (co-authored), full.
- [S34] T. Kesselheim, K. Radke, A. Tönnis, B. Vöcking, "Primal Beats Dual on Online Packing LPs in the Random-Order Model", arXiv 1311.2578 v1 (2013); STOC 2014, 10.1145/2591796.2591810; SICOMP 47 (2018), 10.1137/15m1033708 — S, full (arXiv v1).
- [S35] X. Li, Y. Ye, "Online Linear Programming: Dual Convergence, New Algorithms, and Regret Bounds", Operations Research 70 (2022), 10.1287/opre.2021.2164 — P, abstract.
- [S36] X. Li, C. Sun, Y. Ye, "Simple and Fast Algorithm for Binary Integer and Online Linear Programming", NeurIPS 2020: Reviews, Meta-Review and Author Feedback, https://proceedings.neurips.cc/paper_files/paper/2020/hash/6abba5d8ab1f4f32243e174beb754661-Abstract.html — S (reviews) / P (feedback), full.
- [S37] D. Ge, H. Wang, Z. Xiong, Y. Ye, "Interior-Point Methods Strike Back: Solving the Wasserstein Barycenter Problem", NeurIPS 2019: Reviews, Meta-Review and Author Feedback, https://proceedings.neurips.cc/paper_files/paper/2019/hash/0937fb5864ed06ffb59ae5f9b5ed67a9-Abstract.html — S / P, full.
- [S38] J. C. Duchi, O. Hinder, A. Naber, Y. Ye, "Conic Descent and its Application to Memory-efficient Optimization over Positive Semidefinite Matrices", NeurIPS 2020: Review, Meta-Review and Author Feedback, https://proceedings.neurips.cc/paper_files/paper/2020/hash/5e5dd00d770ef3e9154a4257edcb80b8-Abstract.html — S / P, full.
- [S39] A. Sidford, M. Wang, X. Wu, L. F. Yang, Y. Ye, "Near-Optimal Time and Sample Complexities for Solving Markov Decision Processes with a Generative Model", NeurIPS 2018: Reviews, https://proceedings.neurips.cc/paper_files/paper/2018/hash/bb03e43ffe34eeb242a2ee4a4f125e56-Abstract.html — S, full.
- [S40] P. Biswas, Y. Ye, "Semidefinite programming for ad hoc wireless sensor network localization", IPSN 2004, 10.1145/984622.984630 — P, record.
- [S41] P. Biswas, T.-C. Liang, K.-C. Toh, Y. Ye, T.-C. Wang, "Semidefinite Programming Approaches for Sensor Network Localization With Noisy Distance Measurements", IEEE TASE 3(4) 2006, 10.1109/tase.2006.877401 — P, abstract.
- [S42] P. Tseng, "Second-Order Cone Programming Relaxation of Sensor Network Localization", SIOPT 18 (2007), 10.1137/050640308 — S, abstract.
- [S43] Z. Wang, S. Zheng, Y. Ye, S. Boyd, "Further Relaxations of the Semidefinite Programming Approach to Sensor Network Localization", SIOPT 19 (2008), 10.1137/060669395 — P, abstract.
- [S44] S. Kim, M. Kojima, H. Waki, "Exploiting Sparsity in SDP Relaxation for Sensor Network Localization", SIOPT 20 (2009), 10.1137/080713380 — S, abstract.
- [S45] N. Krislock, H. Wolkowicz, "Explicit Sensor Network Localization using Semidefinite Representations and Facial Reductions", SIOPT 20 (2010), 10.1137/090759392 — S, abstract.
- [S46] J. Gouveia, T. K. Pong, "Comparing SOS and SDP relaxations of sensor network localization", COAP (2012; online 2011), 10.1007/s10589-011-9431-1 (Optimization Online 2010/10/2759) — S, abstract.
- [S47] A. Javanmard, A. Montanari, "Localization from Incomplete Noisy Distance Measurements", FoCM (2013; online 2012), 10.1007/s10208-012-9129-5 (arXiv 1103.1417) — S, abstract.
- [S48] A. M.-C. So, Y. Ye, "Theory of semidefinite programming for Sensor Network Localization", Math. Program. 109 (2007; online 2006), 10.1007/s10107-006-0040-1 — P, record.
- [S49] Y. Ye, "A .699-approximation algorithm for Max-Bisection", Math. Program. 90 (2001), 10.1007/pl00011415 — P, record.
- [S50] E. Halperin, U. Zwick, "A unified framework for obtaining improved approximation algorithms for maximum graph bisection problems", Random Struct. Alg. 20 (2002) 382–402, 10.1002/rsa.10035 — S, abstract.
- [S51] U. Feige, M. Langberg, "The RPR² rounding technique for semidefinite programs", J. Algorithms 60 (2006) 1–23, 10.1016/j.jalgor.2004.11.003 — S, record; not read.
- [S52] Y. Ye, "A path to the Arrow–Debreu competitive market equilibrium", Math. Program. 111 (2008; online 2006), 10.1007/s10107-006-0065-5 — P, record.
- [S53] X. Chen, D. Dai, Y. Du, S.-H. Teng, "Settling the Complexity of Arrow-Debreu Equilibria in Markets with Additively Separable Utilities", FOCS 2009, 10.1109/focs.2009.29 — S, abstract.
- [S54] C. Zhang, C. He, Y. Jiang, C. Xue, B. Jiang, D. Ge, Y. Ye, "A Homogeneous Second-Order Descent Method for Nonconvex Optimization", MOR 51 (2026), 10.1287/moor.2023.0132 (arXiv 2211.08212) — P, record.
- [S55] R. Higuchi, P.-L. Poirion, A. Takeda, "Improving Convergence Guarantees of Random Subspace Second-order Algorithm for Nonconvex Optimization", arXiv 2406.14337 v2 (ICLR 2025 Spotlight) — S, full (searched).
- [S56] Y. Pei, Y. Lin, M. S. Louzeiro, D. Zhu, "A Second-Order Algorithm Based on Affine Scaling Interior-Point Methods for nonlinear Optimisation with bound constraints", arXiv 2603.05022 — S, abstract.
- [S57] S. Agrawal, Z. Wang, Y. Ye, "A Dynamic Near-Optimal Algorithm for Online Linear Programming", Operations Research 62 (2014), 10.1287/opre.2014.1289 — P, record.
- [S58] C. Zhang, D. Ge, C. He, B. Jiang, Y. Jiang, Y. Ye, "DRSOM: A Dimension Reduced Second-Order Method", arXiv 2208.00208 v3 — P, abstract and version record.
- [S59] H. Lu, J. Yang, H. Hu, Q. Huangfu, J. Liu, T. Liu, Y. Ye, C. Zhang, D. Ge, "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv 2312.14832 v2 — P, abstract.
- [S60] H. Lu, Z. Peng, J. Yang, "cuPDLPx: A Further Enhanced GPU-Based First-Order Solver for Linear Programming", arXiv 2507.14051 v4 — S, abstract.
- [S61] K. Chen, D. Sun, Y. Yuan, G. Zhang, X. Zhao, "HPR-LP: An implementation of an HPR method for solving linear programming", arXiv 2408.12179 v2 — S, abstract.
- [S62] O. Hinder, Y. Ye, "Worst-case iteration bounds for log barrier methods on problems with nonconvex constraints", arXiv 1807.00404 v5 (comment field); MOR 49 (2024), 10.1287/moor.2020.0274 — P, abstract and comment.
- [S63] Y. Ye, homepage, "Research Interests/Selected-Work", https://web.stanford.edu/~yyye/, accessed 2026-09-28 — P, full.
- [S64] Y. Ye, "Mathematical Programming in the Era of AI", HORIZONS 2026, VinUni, 2 Jul 2026, https://web.stanford.edu/~yyye/20260701Solver.pdf — P, text extracted (slide 5 title; slide tables are images).
- [S65] S. Burer, Y. Ye, "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", Math. Program. 2021, 10.1007/s10107-021-01684-5; original 10.1007/s10107-019-01367-2; arXiv 1802.02688 — P, record; not read.
- [S66a] Yin Zhang, review of *Interior Point Algorithms: Theory and Analysis*, IIE Transactions 31(3) 1999, 275–276, 10.1080/07408179908969827 — S, record; not read.
- [S66b] J. Wilson, review of *Interior Point Algorithms: Theory and Analysis*, J. Oper. Res. Soc. 51 (2000), 10.2307/254021 — S, record; not read.
- [S67] S. Mizuno, M. J. Todd, "On two homogeneous self-dual approaches to linear programming and its extensions", Math. Program. 89 (2001) 517–534, 10.1007/pl00011413 — S, record; not read.
- [S68] C. Chen, B. He, Y. Ye, X. Yuan, "The direct extension of ADMM for multi-block convex minimization problems is not necessarily convergent", Math. Program. 155 (2016; online 2014), 10.1007/s10107-014-0826-5 — P, record.
- [S69] Y. Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley 1997, 10.1002/9781118032701; Preface read from the author's main.ps (1996/97) — P, Preface (for K2).
- [S70] E. D. Andersen, K. D. Andersen, "The Mosek Interior Point Optimizer for Linear Programming: An Implementation of the Homogeneous Algorithm", in *High Performance Optimization*, 2000, 10.1007/978-1-4757-3216-0_8 — S, record.
- [S71] T. K. Pong, P. Tseng, "(Robust) Edge-based semidefinite programming relaxation of sensor network localization", Math. Program. 130 (2011; online 2010), 10.1007/s10107-009-0338-x — S, record; not read.
- [S72] H. D. Mittelmann, "An independent benchmarking of SDP and SOCP solvers", Math. Program. 95 (2003) 407–430, 10.1007/s10107-002-0355-5 — S, record; not read (cited on Mittelmann's SDP page as the source of the DIMACS error measures).
- [S73] J.-H. Chen, Z. Xu, H.-L. Zhang, "A Homogeneous Second-Order Descent Ascent Algorithm for Nonconvex-Strongly Concave Minimax Problems", arXiv 2602.14058 — S, abstract.
