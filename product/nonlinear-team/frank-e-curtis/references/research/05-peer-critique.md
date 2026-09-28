# Frank E. Curtis: Peer Critique (blind spots, limits, contested judgements)

| Field | Value |
|---|---|
| Researcher | Frank E. Curtis (Lehigh University ISE; PhD Northwestern 2007 under Jorge Nocedal) |
| Dimension | Research agent 05 of 06: peer critique (published objections, counterexamples, rival methods, benchmarks by others, and how he answered) |
| Research date | 2026-09-28 |
| Sources consulted | 49 (34 primary, 15 secondary), listed under "Sources" |
| WebSearch calls | 2 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`; `private/` was not opened |
| Transcripts saved | none |
| Language | English (per team.json) |

**Tags.** [stated] = Curtis (or a paper he co-signed) said it. [practice] = what his papers, code or records show he did. [observed] = a third party wrote it (the critic). [inferred] = my reading; the basis is given, and it must not be quoted as anyone's view. (P) = primary source (the critic's own text, or Curtis's own text), (S) = secondary (an aggregator, or a quotation I could only see through a citation-context index).

**How the critiques were found.** No published "comment and reply" pieces, retractions of his results by others, or failed-replication reports turned up. His field publishes in SIAM/MP-type journals with closed review, so critique lives inside other people's papers: in their related-work and experiments sections. I therefore:
1. pulled the Semantic Scholar citation contexts for 14 of his papers (about 5,000 citing records, 4,050 of them for the SIAM Review survey) and filtered them for critical wording;
2. opened the full text (arXiv or the author's PDF) of every critic I then quote, except where marked "via S2 context; full text not read";
3. read the Curtis-side papers that respond;
4. checked every identifier with Crossref or the arXiv abstract page.

Coverage limits are listed under Gaps. The zbMATH Open reviews of his papers (10 reviews among 75 records) are purely descriptive and contain no criticism.

**Co-authorship caveat (from 01).** His papers are alphabetically ordered team products. A critique of "Berahas, Curtis, Robinson, Zhou" targets a group (mostly Curtis, D. P. Robinson and their students), not Curtis alone. Several critics are former collaborators. Tim Mitchell, M. L. Overton, M. J. O'Neill and L. E. A. Simões all co-authored with him; S. J. Wright co-authored the trust-region Newton-CG paper. I flag these cases because friendly critique from inside the network is a different signal from critique by a rival school.

---

## 0. Summary for Phase 2 (what the critique record says about his craft)

| # | Recurring objection | Who raised it | His answer pattern | Status |
|---|---|---|---|---|
| K1 | Stepsize/radius rules driven by **prespecified sequences and constants** (β_k, Lipschitz constants, γ-sequences) that must be tuned and that "highly affect" performance | Na–Anitescu–Kolar; Fang–Na–Mahoney–Kolar (twice); Hong–Na–Mahoney–Kolar; Bellavia–Morini–Rebegoldi; Gratton–Jerad–Toint; Berahas–Bollapragada–Zhou | Counter-critique: rivals' adaptive line searches need accurate gradients; his methods target "a more stochastic regime" | Open; a disagreement about which regime matters |
| K2 | **Assumptions that do not hold, or are hard to check**: symmetric noise for the merit parameter; LICQ at every iterate; bounded stochastic gradients; the SIAM Review's Assumption 4.3 | Na et al.; Fang et al.; O'Neill; Patel–Zhang–Tian; Nguyen et al.; Li–Milzarek | New papers remove assumptions one at a time (rank-deficient Jacobians; complexity with a random merit parameter; almost-sure convergence). Otherwise he argues the bad events can be "ignored for practical purposes" | Partly answered |
| K3 | **Weaker guarantees than rivals**: expectation-only (not almost-sure) convergence; no local rates for inexact SQP; no rapid-local-convergence proof for GS-plus-quasi-Newton; BFGS-SQP has no guarantee at all | Na et al.; Patel; Hong et al.; Helou–Santos–Simões; Werner–Overton–Peherstorfer | Almost-sure results added in 2023–25; the others were not answered in anything I found | Mixed |
| K4 | **Per-iteration cost** of the safeguard: numerous QPs (BCN 2010); two linear systems (inexact IPM); O(n) gradients (SQP-GS); exact QP solves needed (p-sqp) | Burke–Curtis–Wang (self); Huber; Kungurtsev–Mitchell–Vyhlídal; Johnson–Kirches–Wächter | Strongest pattern of answer: the next method removes the cost (SQuID, penalty updates inside the QP solve, BFGS-SQP) | Largely answered by his own later work |
| K5 | **Complexity results that do not improve practice** | S. J. Wright (co-author, 2025); Curtis himself (2018, 2021) | He agrees and attacks the yardstick ("Our worst-case analysis for nonconvex optimization is faulty") while continuing to publish complexity results | A shared, unresolved tension |
| K6 | **Penalty-based infeasibility handling is slow or complicated** | Hinder–Ye (on PIPAL) | No reply found. His later slogans move away from penalties ("avoid penalty methods") [inferred link] | Unanswered in print |
| K7 | **Tooling and code maturity** limit outside adoption: MATLAB-only GRANSO; "under development" repositories; an experimental Ipopt option | Liang–Mitchell–Sun; outside benchmarks that leave TRACE out [inferred] | NonOpt (C++, 2025) [inferred as answer] | Partly answered |

---

## 1. Stochastic constrained optimization (stochastic SQP line, 2020–2026)

**Era and resource context.** Matlab prototypes. Tests use CUTEst equality-constrained problems with simulated gradient noise, plus LIBSVM logistic regression. The core team is Berahas, Curtis, Robinson and students (Zhou, O'Neill, Wang). A rival group formed at the same time: Sen Na, Mihai Anitescu and Mladen Kolar (Chicago/Argonne), later with Michael Mahoney and Yuchen Fang (Berkeley). Its founding paper calls Berahas–Curtis–Robinson–Zhou (BCRZ, SIOPT 31(2) 2021, DOI 10.1137/20M1354556) "the very first practical algorithm" for the problem class, then critiques it point by point. Critique inside this line is therefore mostly **rival-school critique**, and the Curtis group answers in kind.

### 1.1 Prespecified sequences drive performance (K1)

- [observed] (P) **Na, Anitescu & Kolar** (arXiv:2102.05320 v2; *Math. Program.* 199, 721–791, DOI 10.1007/s10107-022-01846-z), p. 3, on BCRZ: "The sequence {βk}k, which is either constant or decaying with a proper rate, determines the iteration convergence behavior, however, still heavily affects the selection of ¯αk. As shown numerically in [3], the line search procedure is still preferable for most of problems." And p. 10: "This observation suggests that the prespecified sequence in both algorithms highly affects the performance."
- [observed] (P) The same paper, p. 10, footnote 1, on a hidden cost: "The implicit cost for deriving Lipschitz constants sequence in [3] is not counted here, which, however, requires non-negligible evaluations for the objective and constraints."
- [observed] (P) **Fang, Na, Mahoney & Kolar** (arXiv:2409.15734 v2, TR-SQP-STORM), p. 2: "our method does not input any prespecified trust-region radius (or stepsize) sequences that significantly affect algorithm performance (see, e.g., Berahas et al., 2021, 2023a,b,c; Curtis et al., 2024; Fang et al., 2024)."
- [observed] (P) **Hong, Na, Mahoney & Kolar** (arXiv:2305.18379, ICML 2023 per the arXiv comment), p. 3: "The stepsize in most of these methods is controlled by prespecified decaying sequences (i.e., the methods are designed under the stochastic approximation regime), with the only exceptions being Na et al. (2023) and Na et al. (2022a), which adopt line search to make the methods more adaptive."
- [observed] (S; via S2 context, full text not read) **Berahas, Bollapragada & Zhou** (arXiv:2206.00712; both Berahas and Zhou are Curtis co-authors): "If such Lipschitz constants are unknown, as is the case more often than not, one can approximate these constants following the approaches proposed in [5, 23, 9]."
- **How it was answered.** [stated] (P) Berahas, Curtis, O'Neill & Robinson (arXiv:2106.13015; *Math. Oper. Res.* 49(4) 2212–2248, 2024, DOI 10.1287/moor.2021.0154), p. 3, turn the critique around against Na et al.'s line search: "(ii) the algorithm in [15] employs an adaptive line search that may require the algorithm to compute relatively accurate stochastic gradient estimates throughout the optimization process. Our algorithm, on the other hand, does not require the LICQ to hold and is meant for a more stochastic regime". So the answer is a claim about regimes, not a removal of the sequences. [practice] (P, from 03 PE27) BCRZ itself had conceded the numerical point: "We do not claim that “SQP Adaptive” is as efficient as “SQP Backtracking”". **Status: open.** Each side names a regime where its own design is the right one.

### 1.2 The merit parameter and the assumptions needed to control it (K2)

- [observed] (P) Na et al. (arXiv:2102.05320), p. 3: BCRZ "showed (ii) under additional assumptions on the noise distribution (e.g Gaussian). See Proposition 3.16 and Example 3.17 therein." Page 3 also: "Our analysis does not rely on the symmetry of the noise distributions (cf. [3, Example 3.17])."
- [observed] (P) **Fang, Na, Mahoney & Kolar** (arXiv:2211.15943 v2; *SIAM J. Optim.* 34(2) 2007–2037, 2024, DOI 10.1137/22M1537862), pp. 2–3: "Berahas et al. (2021a,b, 2022b); Curtis et al. (2021b) imposed a symmetry condition on the noise distribution. In contrast, deterministic SQP schemes only require the stability of the merit parameter". The 2024 TR-SQP-STORM paper (arXiv:2409.15734, p. 3) repeats this: "This substantially relaxes the conditions of existing SSQP methods that demand not only stabilized but also sufficiently large merit parameters. Extreme merit parameters rely on additional model assumptions. For example, Berahas et al. (2021, 2023a,b); Curtis et al. (2024) imposed symmetric assumptions on the noise distribution."
- [observed] (P) **M. J. O'Neill** (a Curtis co-author; arXiv:2408.16656 v2), p. 6: "We choose to avoid this as previous work relied upon strong assumptions (such as uniformly bounded stochastic gradients [4], sub-Gaussian stochastic gradients [14], or direct assumptions on “good behavior” of the merit parameter [3,15,16], which can be implied by the prior assumptions) in order to prove the existence of a lower bound on a stochastically estimated merit parameter sequence." Here [4] is BCRZ 2021, [14] is Curtis–O'Neill–Robinson 2024, and [3,15,16] are Berahas–Curtis–O'Neill–Robinson and two Curtis–Robinson–Zhou papers.
- [observed] (P) **An experiment against the "ignore it in practice" position.** O'Neill ran BCRZ's GitHub code (Algorithm 3, "SSQP") with its published settings. The result (p. 34): "However, as the noise level increases, the performance of SSQP degrades significantly with respect to infeasibility, while the performance of TSSQP is largely unchanged." He attributes SSQP's low-noise edge to "using an estimate of the merit parameter τ, which is more likely to be well-behaved in a low noise setting". That attribution is his reading, not a proof.
- **How it was answered (three moves, all [practice] (P)).**
  1. *Argue the bad events are rare.* BCRZ (homepage preprint of the SIOPT paper, p. 24): "Our goal in this part of our analysis is to argue that these events, exhibiting what we refer to as poor behavior of the merit parameter sequence, are either impossible or can only occur in extreme circumstances in practice." Curtis, Robinson & Zhou (arXiv:2107.03512; *INFORMS J. Optim.* 6(3–4) 173–195, 2024, DOI 10.1287/ijoo.2022.0008), p. 17: "For our purposes here, we do not consider these latter two events since we contend that, for practical purposes, they can be ignored for the same reasons as are claimed in [3]." The inequality paper says the same (Curtis–Robinson–Zhou, *SIAM J. Optim.* 34 (2024) 3592–3622, DOI 10.1137/23M1556149; arXiv:2302.14790, p. 8): "the event represents likely behavior in practice, which shows that our convergence results about the algorithm are meaningful for real-world situations."
  2. *Confront the random process in a later analysis.* Curtis, O'Neill & Robinson (arXiv:2112.14799; *Math. Program.* 205 (2024) 431–483, DOI 10.1007/s10107-023-01981-1), p. 6: "it is possible—even under Assumption 1—for the merit parameter sequence to vanish or for it to eventually remain constant at a value that is not sufficiently small [...] As a result, we have had to devise new analytical approaches that confront the fact that {τk} is a random process, the ultimate behavior of which is uncertain."
  3. *Trade one assumption for another when a case is added.* Berahas, Curtis, O'Neill & Robinson (arXiv:2106.13015), p. 3: "However, for cases not considered in [1] when the merit parameter sequence may vanish, we require the stronger assumption that the difference between each stochastic gradient estimate and the corresponding true gradient of the objective eventually is bounded deterministically in each iteration."
- **Status: partly answered.** The symmetric-noise objection is not withdrawn in any rival paper I read (Fang et al. repeat it in 2024). O'Neill's two-stepsize method avoids estimating τ altogether: the fix came from a former collaborator, not from the Curtis group.

### 1.3 Expectation-only guarantees and the LICQ-conditioned test set (K2, K3)

- [observed] (P) Na et al. (arXiv:2102.05320), p. 10: their "almost sure" guarantee "differs from [3], which established the convergence in expectation."
- [stated] (P) **Self-acknowledged and answered.** Curtis, Jiang & Wang (arXiv:2308.03687; *J. Optim. Theory Appl.* 204 (2025), DOI 10.1007/s10957-024-02568-2), abstract: "convergence guarantees have been limited to the asymptotic convergence of the expected value of a stationarity measure to zero. This is in contrast to the unconstrained setting in which almost-sure convergence guarantees (of the gradient of the objective to zero) can be proved". The paper then proves almost-sure convergence for "a simplified variant of the algorithm from [3]" (p. 2). [inferred] The answer came about two years after the rival's objection, and it covers a simplified variant only.
- [practice] (P) **The first test set was conditioned on the assumption.** BCRZ selected problems "for which (i) f is not a constant function, (ii) n+m ≤ 1000, and (iii) the LICQ held at all iterates in all runs of all algorithms that we ran. This selection resulted in a total of 49 problems." That is 49 of 123 CUTE equality-constrained problems (homepage preprint, p. 25). The group's own follow-up names the gap: "like for the algorithm in [1], for the algorithm in [15] the LICQ is assumed to hold at all algorithm iterates" (Berahas et al., arXiv:2106.13015, p. 3). That paper removes LICQ at the price in 1.2(3). **Answered by his own group.**

### 1.4 Line-search SQP needs a modified Hessian (K3)

- [observed] (P) Fang et al. (arXiv:2211.15943), p. 2: positive definiteness on the null space "is often achieved by Hessian modification, which excludes promising choices of the Hessian matrices, such as the unperturbed (stochastic) Hessian of the Lagrangian." The 2024 paper (arXiv:2409.15734, p. 3): "most existing SSQP methods are line-search-based, necessitating positive definite Hessian approximations typically obtained with cumbersome computational costs (e.g., matrix factorization)."
- **Answer: none found** in the Curtis stochastic-SQP papers read. [inferred] The objection echoes the one Heinkenschloss and Ridzal raised against his deterministic inexact Newton method in 2008 (see 4.2). The line-search design choice has drawn the same objection twice, 15 years apart.

### 1.5 Stochastic trust-region methods (TRish and its second-order version): tuning burden (K1)

- [observed] (P) **Bellavia, Morini & Rebegoldi** (arXiv:2404.13382; *Optim. Methods Softw.* 39 (2024) 937–966, DOI 10.1080/10556788.2024.2346834), p. 2, on TRish (Curtis, Scheinberg & Shi, *INFORMS J. Optim.* 1 (2019) 200–220, DOI 10.1287/ijoo.2018.0010): "Clearly, the performance of TRish depends on the hyper-parameters choice, and its application requires tuning them for each problem, analogously to SG methods. This tuning process can be computationally onerous, and represents the main limitation of the algorithm." Their experiments (p. 20): "TRish is always sensitive to these parameters for any choice of α". They add (p. 2): "In our experience, after tuning the parameters, TRish compares well with adaptive stochastic trust-region methods".
- [observed] (P) **Gratton, Jerad & Toint** (arXiv:2203.01647 v3; *Optim. Methods Softw.* 41 (2026) 478–508, DOI 10.1080/10556788.2023.2296431), p. 2, on the same TRish paper: "Moreover, the analysis of [21] requires the explicit knowledge of the problem’s Lipschitz constant in the algorithm for obtaining the best complexity estimate."
- [observed] (P) Fang et al. (arXiv:2211.15943), p. 3, on the second-order version (Curtis & Shi, *Optim. Methods Softw.* 37 (2022) 844–877, DOI 10.1080/10556788.2020.1852403): "Our design simplifies the one in Curtis and Shi (2020), where there are three parameter sequences to tune whose conditions are highly coupled (see Curtis and Shi, 2020, Lemma 4.5). In addition, as the authors stated, Curtis and Shi (2020) rescaled the Hessian matrix based on the input {γ1,k}, which is not ideal (because the rescaling step modifies the curvature information of the Hessian)."
- [stated] (S; via S2 context, full text not read) Curtis & Shi concede part of this in the paper itself: "Admittedly, this is done with assumptions that impose stricter requirements on the stepsizes employed in the algorithm, but the results are still non-trivial to obtain".
- **Answer: none found** from Curtis. The adaptive-sampling repair came from Bellavia et al. [observed].

---

## 2. The SIAM Review survey (Bottou, Curtis & Nocedal 2018)

**Era and resource context.** The survey was written 2016–2018 (arXiv:1606.04838 v1 June 2016, v3 Feb 2018; *SIAM Review* 60(2) 223–311, DOI 10.1137/16M1080173). Curtis was a mid-career academic writing with an industry ML researcher (Bottou) and his former advisor. Its theory was built to be general but simple. Critics are mostly ML-theory authors who used its assumptions as the baseline to beat.

### 2.1 Assumption 4.3 (first- and second-moment limits) (K2)

- [observed] (P) **Nguyen, Nguyen, van Dijk, Richtárik, Scheinberg & Takáč** (arXiv:1802.03801; *ICML 2018*, PMLR 80:3747–3755; Scheinberg and Takáč were Lehigh colleagues), p. 2, on the arXiv version of the survey: "This assumption does not contradict strong convexity, however, in general, constants M and N are unknown, while M is used to determine the learning rate ηt (Bottou et al., 2016)." Page 4, Remark 1: under their assumption the admissible initial learning rate improves from η0 ≤ 1/(2Lκ²) to 1/(2Lκ). (Paraphrase of a formula comparison; no quotation marks.)
- [observed] (P) **Patel, Zhang & Tian** (arXiv:2110.01663 v3; *NeurIPS 2022*, 36014–36025, DOI 10.52202/068431-2610) give a **counterexample of applicability**. For Poisson regression, p. 3: "the stochastic gradients violate the bounded variance assumption, its generalization [Bottou et al., 2018, Assumption 4.3c], and, in turn, its generalization, expected smoothness [Khaled and Richtárik, 2020, Assumption 2]." Then: "As these three examples show, global convergence analyses that make use of the aforementioned assumptions do not apply to these canonical examples of machine learning problems." The proof is in their Appendix A.4 (p. 18).
- [observed] (P) **Li & Milzarek** (arXiv:2206.03907 v2), p. 2: the survey "showed limk→∞E[∥∇f(xk)∥] = 0 under the additional assumptions that f is twice continuously differentiable and the multiplication of the Hessian and gradient ∇2f(x)∇f(x) is Lipschitz continuous." Also: "We also remove the stringent assumption used in [6] to show (2) for SGD."
- **Answer: none found.** No revision of the survey or published reply exists. [inferred] Curtis's later work moved to constrained stochastic problems and did not return to these unconstrained assumptions.

### 2.2 Leaving out almost-sure convergence (K3)

- [stated] (P, from 02 §1.7) Survey Inset 4.2 on martingale almost-sure results: "we omit these complications since, in our view, they do not provide significant additional insights into the forces driving convergence of the method."
- [observed] (P) **Patel** (arXiv:2004.00475 v2; *Math. Program.* 195 (2022) 693–734, DOI 10.1007/s10107-021-01710-6), who named the function class after the survey's authors. Page 6: "Thus, stopping criteria are predicated on establishing strong convergence, rendering convergence in probability insufficient." Page 7: "For such nonconvex functions—which we refer to as Bottou-Curtis-Nocedal (BCN) functions, as popularized by [4] and are formally specified in §3.4—even convergence in probability has yet to be established." (The S2 context index holds an earlier wording, "strong convergence has yet to be established"; the v2 full text is quoted here.)
- **Answer:** no reply to Patel found. Curtis's own later work makes almost-sure convergence a headline result for stochastic SQP (see 1.3 and 02 C2). [inferred] This is the clearest case of a judgement in his record that the field, and later he himself, treated as mistaken in practice. The settings differ (unconstrained SG versus constrained SQP), so the reversal is not literal.

### 2.3 Reception without critique

- [observed] (S) The zbMATH Open review (document 6870204, reviewer T. Riismaa) is a neutral summary. No published "comment" on the survey was found.
- The survey's forecast that SG's dominance "is far from settled" (02 §3.7) was **not evaluated** here (see Gaps).

---

## 3. Worst-case complexity (TRACE, the inexact regularized-Newton framework, trust-region Newton-CG)

**Era and resource context.** 2014–2023. This is the Cartis–Gould–Toint (CGT) era of evaluation-complexity theory. TRACE (Curtis, Robinson & Samadi, *Math. Program.* 162 (2017) 1–32, DOI 10.1007/s10107-016-1026-2) was published with no numerical section (03).

### 3.1 CGT: "the details are not given" → answered in a later version

- [observed] (P) **Cartis, Gould & Toint** (arXiv:1709.07180, 21 Sep 2017; *Proc. ICM 2018*, 3711–3750, DOI 10.1142/9789813272880_0198), §5 "The Curtis-Robinson-Samadi class", p. 24: "It is stated in [36] that both ARC [...] and TRACE [37] belong to the class, although the details are not given." They then build a lower-bound example (Theorem 5.1) showing that a sub-class "CRSa" is optimal. This **confirms** the O(ε^-3/2) order and **absorbs** his framework into their taxonomy.
- [stated] (P) arXiv:1708.00475 **v1** (Aug 2017), p. 13: "Showing that trace and arc are members of our general framework is not difficult, but is out of the scope of this document." **v4** (received 16 Mar 2018; *IMA J. Numer. Anal.* 39 (2019) 1296–1327, DOI 10.1093/imanum/dry022), p. 3: "In §4, we show that ARC and TRACE can be viewed as special cases of our framework". v4 thanks "the anonymous referees".
- **Status: answered.** Whether CGT's remark or a referee triggered the new §4 is **not documented** [inferred link].

### 3.2 Complexity modifications do not improve practice (K5): a critique he shares

- [observed] (P) **S. J. Wright** (co-author of the trust-region Newton-CG paper), "Optimization in Theory and Practice" (arXiv:2510.15734 v2), p. 23, on Royer–O'Neill–Wright and Curtis–Robinson–Royer–Wright: "They are based on practical methods, but the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance."
- [stated] (P) Curtis says the same about his own TRACE. ECOM 2021 public lecture, slide 32/45: "“Better complexity” has yet to mean “better performance” for nonconvex!", followed by the TRACE citation.
- [stated] (P) He goes further and **attacks the rival yardstick**. ISMP 2018 (with D. P. Robinson), slide 4/31: "Our worst-case analysis for nonconvex optimization is faulty. ▶ We should characterize complexity in a different way. ▶ Purpose of this talk is to convince you." ECOM 2021 public lecture, slide 32/45: "They say: “Newton’s method is as slow as gradient descent.” This essentially ignores reality." [practice] The written form is the regional-complexity paper (Curtis & Robinson, *Math. Program.*, DOI 10.1007/s10107-020-01492-3, per 02 and the TRACE citation list).
- **Reply from the CGT school to "faulty": not found** (Gaps).

### 3.3 Outside benchmarks leave TRACE out

- [observed] (P) **Jiang, He, Zhang, Ge, Jiang & Ye** (Yinyu Ye's group; arXiv:2311.11489 v4; *J. Sci. Comput.*, DOI 10.1007/s10915-025-03154-y). They credit TRACE as "the first adaptive trust-region method" with Õ(ε^-3/2) complexity for second-order points (p. 2). They credit Hamad and Hinder with improving "the complexity’s dependency over Lipschitz constants" (p. 3). Yet their CUTEst study "focus[es] on comparisons with the classical trust-region method [6] and adaptive cubic regularized Newton method [16]", and [16] is not a Curtis paper. TRACE is not a baseline.
- [inferred] A likely reason is the lack of a mature public TRACE code. 03 records that the GitHub TRACE repository is a 2022 rewrite still marked "under development". That link is not stated by Jiang et al.

---

## 4. Inexact and matrix-free Newton–SQP and interior-point methods (2006–2014)

**Era and resource context.** These were PhD and postdoc years (Northwestern, then Courant), with Byrd and Nocedal, and with Schenk and Wächter on the IPOPT side. The prototypes were in Matlab (GMRES/MINRES). The PDE-scale runs used IPOPT with PARDISO's iterative solver. The critics are PDE-constrained-optimization practitioners who tried to use the methods.

### 4.1 "Not yet tested on large problems" → answered

- [observed] (S; via S2 context, full text not read) **Schenk, Wächter & Weiser** (*SIAM J. Sci. Comput.* 31 (2008) 939–960, DOI 10.1137/070707233), on the inexact Newton method for nonconvex problems (Byrd, Curtis & Nocedal, *Math. Program.* 122 (2010) 273–299, DOI 10.1007/s10107-008-0248-3): "A recent exception to this is [13] which allows the use of iterative linear solvers for nonconvex equality constrained optimization without specific preconditioner requirements, but practical performance has not yet been tested on large problems."
- [stated] (S; via S2 context) Curtis, Nocedal & Wächter (*SIAM J. Optim.* 2009, DOI 10.1137/08072471X) state the gap themselves and point to the answer: "the algorithm in this paper and those in [4, 5] require further experimentation on large-scale applications [...] These issues are addressed in [10]." [practice] (P, 01/03) The answer is Curtis, Schenk & Wächter (*SIAM J. Sci. Comput.* 32 (2010) 3447–3475, DOI 10.1137/090747634), an IPOPT implementation with PDE-scale runs. **Answered.**

### 4.2 Line search requires modifying the Hessian

- [observed] (S; via S2 context, full text not read) **Heinkenschloss & Ridzal**, "An Inexact Trust-Region SQP Method with Applications to PDE-Constrained Optimization" (*Numerical Mathematics and Advanced Applications* (ENUMATH 2007 proceedings), pp. 613–620, DOI 10.1007/978-3-540-69777-0_73), on the same 2010 paper: "Nonconvex problems are addressed in [3]; it is required that the Hessian in the quadratic subproblem is modified to exhibit certain positive definiteness properties." And: "In contrast to [3], our trust-region approach does not require a modification of the Hessian in the quadratic subproblem, even in the presence of nonconvexity."
- **Answer: none found** (see 1.4 for the recurrence).

### 4.3 The SMART tests: many parameters, extra solves

- [observed] (S; via S2 context, truncated, full text not read) **Hicken** (*Optim. Eng.* 15 (2014) 575–608, DOI 10.1007/s11081-014-9258-6): "We experimented with a line search based on the SMART tests of Byrd et al. (2008, 2010), but we found that a homotopy-based continuation (described below) was more efficient for the problems considered here; however, we emphasize that the SMART tests involve many parameters and, with further…" The index cuts the sentence off there; the rest was **not read**.
- [observed] (S; via S2 context, full text not read) **J. Huber**, PhD thesis "Interior-point methods for PDE-constrained optimization" (University of Basel, 2013; co-supervised by O. Schenk; DOI 10.5451/unibas-006145479, which resolves to the edoc.unibas.ch record) on the inexact IPM of Curtis–Schenk–Wächter 2010: "The stabilized SMART tests in [24, 22] require the solution of two Newton systems, thus doubling the price of a Newton iteration." And on the 2010 nonconvex method: "Even though global convergence is not guaranteed for the inexact method in [17] within an IIP framework, in practice it has shown good results." He answers with his own variant: "While the IIP method in [24] needs to solve two sparse large-scale linear systems, the IIP method proposed in Chapter 3 comes along with only a single linear system solution in most optimization steps."
- [observed] (S, from 03) The inexact option still sits behind `--enable-inexact-solver`, "EXPERIMENTAL! (default: no)", in Ipopt 3.14. [inferred] Adoption in the main solver stalled.
- **Answer from Curtis: none found.** The cost critique was answered by the Schenk group, not by him.

### 4.4 Local convergence rates missing (K3)

- [observed] (P) Hong, Na, Mahoney & Kolar (arXiv:2305.18379), p. 2: the local rate of inexact Newton methods "is mostly investigated for unconstrained problems [...], while is largely missing in constrained cases (Byrd et al., 2008; 2010; Curtis et al., 2014b; Gu et al., 2017; Burke et al., 2020)." Page 3: "The methods bound the residuals of the solver by a few fixed tuning parameters".
- [stated] (P, from 01 SW1) Byrd–Curtis–Nocedal 2008 had already deferred fast local rates in its final remarks. **Answer:** a 2026 Curtis–Guo–Robinson arXiv paper (2608.12665, title "A Local-Linearly Convergent Algorithm for Nonconvex Equality-Constrained Optimization", listed in 01) may bear on this. Its content was **not read**, so any link is [inferred].

### 4.5 The Sℓ1QP code fails with inexact QP solutions

- [observed] (S; via S2 context, full text not read) **Johnson, Kirches & Wächter** (*SIAM J. Optim.* 25 (2015) 967–994, DOI 10.1137/130940384). They used Curtis's Matlab code "p-sqp" for the Byrd–Curtis–Nocedal 2010 infeasibility-detecting Sℓ1QP method (*SIAM J. Optim.* 20 (2010) 2281–2299, DOI 10.1137/080738222) and wrote: "This tight tolerance is necessary because the convergence analysis for Sℓ1QP method in [7] assumes the exact solution of (43), and p-sqp frequently fails to converge if less accurate solutions are returned."
- [practice] (P, from 03) **Answered later by his own group.** Burke, Curtis, Wang & Wang update the penalty parameter inside an inexact QP solve (*SIAM J. Optim.* 2020, DOI 10.1137/18M1176488; extended arXiv:1803.09224). The link to this particular complaint is [inferred]. The dates fit: JKW 2015, BCWW arXiv v1 2018.

---

## 5. Infeasibility detection and penalty methods (2008–2014)

### 5.1 Self-critique: too many QPs per iteration → SQuID

- [stated] (P) **Burke, Curtis & Wang** (*SIAM J. Optim.* 24(2) (2014) 839–872, DOI 10.1137/120880045; homepage PDF), p. 841, on his own 2010 method with Byrd and Nocedal: "That method does, however, have certain practical disadvantages. The most significant of these is that, particularly in infeasible cases, the method may require the solution of numerous QO subproblems per iteration. Indeed, near an infeasible stationary point, at least three QO subproblems must be solved."
- [stated] (S; via S2 context of arXiv:1803.09224) The next step critiques SQuID in turn: "Our proposed method outperforms the SQuID algorithm proposed in [3], which is also a penalty-SQP method with automatic infeasibility detection, although it requires two exact QP solves per iteration."
- [inferred] This is his most consistent self-correction loop. Each method's per-iteration subproblem count becomes the next paper's target.

### 5.2 Rival critique of PIPAL (K6)

- [observed] (P) **Hinder & Ye**, "A one-phase interior point method for nonconvex optimization" (arXiv:1801.03072 v2), p. 2, on the penalty-interior-point approach (Curtis, *Math. Program. Comput.* 4(2) (2012) 181–209, DOI 10.1007/s12532-012-0041-4): "Penalty methods will converge only if the penalty parameter is sufficiently large. However, estimating this value is difficult: too small and the algorithm will not find a feasible solution; too big and the algorithm might be slow and suffer from numerical issues. Consequently, penalty methods tend to be slow [8, Algorithm 1] or use complex schemes for dynamically updating the penalty parameter [8, Algorithm 2]."
- [observed] (P) The same page criticizes IPOPT's two-phase design: "It is well known that this approach has drawbacks." Curtis also criticized two-phase design (02 §3.2). On IPOPT the two critiques **agree**; they **disagree** on whether a penalty is the cure.
- [stated] (P, from 02 §5.4) Curtis's own 2012 verdict was already modest: "PIPAL-a and especially IPOPT have an edge in terms of efficiency".
- **Answer: none found.** No further PIPAL paper exists (01). [inferred] His later slogans, "avoid penalty methods" and "Penalization is not often the best route" (2024–2026; 02 C3), move in the direction Hinder and Ye argued, without citing them.

### 5.3 Positive reception (kept for balance)

- [observed] (P, via Crossref-verified record; quote via S2 context) Dai, Liu & Sun (*J. Ind. Manag. Optim.* 16 (2020) 1009–1035, DOI 10.3934/jimo.2018190): "it has been an open problem whether these methods are capable of rapidly converging to an infeasible stationary point before Byrd, Curtis and Nocedal [8] creatively presented a set of conditions to guarantee the superlinear convergence of their SQP algorithm to an infeasible stationary point."
- [observed] (S; via S2 context) Gould, Loh & Robinson (*SIAM J. Optim.* 25 (2015) 1885–1911, DOI 10.1137/140996677; Robinson is his closest collaborator): "We believe, however, that recent advances in feasibility detection [3] could be used within our framework and perhaps reduce, if not entirely mitigate, this disadvantage."

### 5.4 An acknowledged dispute whose other side is missing

- [stated] (P) ISMP 2018, slide 4/31: "State-of-the-art nonlinear optimization codes fail too often. ▶ Reasons are “high” nonlinearity, degeneracy, and infeasibility. ▶ People have disputed this, but I have results!" **Who disputed it, and on what data, was not found** (see Gaps).

---

## 6. Nonsmooth, nonconvex optimization (SQP-GS 2012, adaptive GS 2013/2015, BFGS-SQP/GRANSO 2017)

**Era and resource context.** 2009–2017, co-authored with Overton (NYU), his students (Xiaocun Que) and Tim Mitchell (GRANSO's author). The prototypes are Matlab codes, and the applications are controller design with expensive eigenvalue- or H∞-based functions. Most critics are **users from control engineering** or **gradient-sampling theorists**.

### 6.1 No proof of fast local convergence for gradient sampling plus quasi-Newton (K3)

- [observed] (P) **Helou, Santos & Simões** (arXiv:1708.07473; *Comput. Optim. Appl.* 71 (2018) 673–717, DOI 10.1007/s10589-018-0030-2), p. 2, citing Curtis–Overton 2012 and Curtis–Que 2013 and 2015 as [8, 9, 10]: "In fact, there are recent studies that have introduced GS-like algorithms with quasi-Newton techniques [8, 9, 10], however there are no proofs nor numerical results that corroborate a rapid local convergence."
- **Answer: none found.** [observed] Simões later co-authored the gradient-sampling survey with Burke, Curtis, Lewis and Overton (arXiv:1804.11003, in 01). A critic became a collaborator.

### 6.2 SQP-GS: cost, speed and feasibility in practice (K4)

- [observed] (P) **Kungurtsev, Mitchell & Vyhlídal**, "A Comparison of Nonsmooth, Nonconvex, Constrained Optimization Solvers for the Design of Time-Delay Compensators" (arXiv:1812.11630 v1, 2018), is the only independent **head-to-head benchmark** of his nonsmooth codes found. Mitchell co-authored BFGS-SQP. Points:
  - p. 2: SQP-GS "requires evaluating O(n) gradients [...] at every iteration, which can make SQP-GS a computationally expensive method, especially if the cost to compute these functions is nontrivial."
  - p. 3: "the convergence guarantees do not preclude SQP-GS from converging to an infeasible stationary point. Third, as the authors of [KPV+17, Section 4, p. 13327] noted, SQP-GS was indeed quite slow in practice." (KPV+17 is an earlier engineering user; that paper was not read.)
  - p. 18: "SQP-GS was at least a magnitude of order slower than GRANSO, highlighting that the large computational burden of SQP-GS may simply make it a too impractical choice for many users." And: "SQP-GS was not particularly effective at finding the feasible set at all, regardless of the budget, having a success rate of only about 50%." But also: "Nevertheless, SQP-GS still managed to return the majority of the best feasible solutions, even though GRANSO found the very best solution."
- [observed] (P) **Schwerdtner & Voigt**, "SOBMOR: Structured Optimization-Based Model Order Reduction" (arXiv:2011.07567 v2), p. 13. Citing GS (2005), BFGS-SQP (2017) and SQP-GS (2012): "While there exist some methods that solve nonsmooth optimization problems, e. g., [13, 15, 16, 42], these tend to converge only slowly requiring a high number of H∞ norm evaluations." They built an alternative approach rather than use these solvers directly.
- [observed] (P) **Fattahi & Sojoudi** (arXiv:1812.11466), p. 24, on a theoretical limit: "the most well-known numerical algorithms for non-smooth optimization—such as gradient sampling, sequential quadratic programming, and exact penalty algorithms—can only guarantee the C-stationarity of the obtained solutions ([42, 43, 54])", where [43] is Curtis–Overton 2012.
- **Answer.** [practice] (P, from 01 §4) BFGS-SQP (Curtis, Mitchell & Overton, *Optim. Methods Softw.* 32(1) (2017) 148–181, DOI 10.1080/10556788.2016.1208749) was his own move away from SQP-GS's cost, at the price of convergence guarantees. The C-stationarity limit is not addressed.

### 6.3 BFGS without guarantees: less reliable in one independent test (K3)

- [observed] (P) **Werner, Overton & Peherstorfer** (arXiv:2205.15050; *SIAM J. Sci. Comput.* 45 (2023) A933–A957, DOI 10.1137/22M1500137; Overton co-authored both SQP-GS and BFGS-SQP), p. 19: "As an alternative to the relatively expensive gradient sampling method, we also experimented with using the BFGS method, which has proved very effective in other nonsmooth optimization applications [28,39,50]. However, we found that, particularly for the cylinder example, the behavior of gradient sampling was more consistent and reliable, perhaps reflecting its very satisfactory convergence theory, which is not shared by BFGS." Here [28] is Curtis–Mitchell–Overton 2017.
- This conflicts with 6.2, where GRANSO beat SQP-GS on feasibility (see Contradictions).

### 6.4 Tooling limits of GRANSO (K7)

- [observed] (P) **Liang, Mitchell & Sun**, "NCVX: A General-Purpose Optimization Solver for Constrained Machine and Deep Learning" (arXiv:2210.00973 v2, OPT2022 workshop), p. 2: "However, GRANSO users must derive gradients analytically and then provide code for these computations, a process which is often error-prone in machine learning and impractical for deep learning. Furthermore, as part of the MATLAB software ecosystem, GRANSO is generally not compatible with popular machine/deep learning frameworks". (A footnote marker after "analytically" is omitted.)
- **Answer:** PyGRANSO came from Mitchell and Sun, not from Curtis. [inferred] His own later software, NonOpt (C++, 2025; 03), is extensible but is not a deep-learning-framework port.

### 6.5 Benchmarking tool extended by others

- [observed] (P) Kungurtsev et al. used Curtis–Mitchell–Overton's relative minimization profiles and added "Global-Local Profiles" (arXiv:1812.11630, abstract), which "assess the tradeoffs of distributing the budget over few or many starting points". [inferred] The single-run RMP view leaves out the multi-start budget question that matters to engineering users.

---

## 7. How Curtis handles critique (pattern across the record; for Phase 2)

1. **Cost critiques become his next paper.** [practice]
   - Numerous QPs (2010) → SQuID (2014) → penalty updates inside the QP solve (2018–2020).
   - O(n) gradient samples (2012) → adaptive sampling (2013) → BFGS-SQP (2017).
   - LICQ at every iterate (2021) → rank-deficient Jacobians (2021–2024).
   - Expectation-only guarantees (2021) → almost-sure convergence (2023–2025).
   These are the critiques he answers fastest, often before outsiders publish them (5.1 is self-critique).
2. **Assumption critiques get a probabilistic "unlikely in practice" argument first**, then, sometimes, a harder analysis. [practice] Examples: BCRZ p. 24; CRZ p. 17; COR p. 6.
3. **Rival-school critique is met by redefining the regime**, not by conceding. [practice] BCOR p. 3 on Na et al.'s line search: "meant for a more stochastic regime".
4. **Critiques of the yardstick are shared and turned outward.** [stated] He accepts "better complexity ≠ better performance" and blames the evaluation framework ("faulty"), while continuing to publish complexity bounds (02 C1).
5. **Silence on some critiques.** [practice; absence of evidence, so weak] No reply was found to:
   - Heinkenschloss–Ridzal (Hessian modification);
   - Hinder–Ye (penalty slowness or complexity);
   - Helou–Santos–Simões (no local-rate proof);
   - Bellavia et al. (TRish tuning);
   - Fang et al. (positive-definite Hessians);
   - Werner–Overton–Peherstorfer (BFGS reliability).
   These cluster on **globalization design choices** he kept: line search over trust region, merit/penalty functions, BFGS without guarantees.

---

## Contradictions (kept, not reconciled)

- **X1. GRANSO/BFGS-SQP versus gradient sampling on reliability.** Kungurtsev, Mitchell & Vyhlídal (2018): GRANSO was "particularly adept at finding the feasible set, rarely failing to do so", while SQP-GS succeeded "only about 50%" of the time. Werner, Overton & Peherstorfer (2023): gradient sampling "was more consistent and reliable" than BFGS on their cylinder example. The applications differ (input shapers versus multi-fidelity controller design), and both groups include a Curtis co-author.
- **X2. "Ignore in practice" versus measured degradation.** Curtis–Robinson–Zhou: the bad merit-parameter events "can be ignored" "for practical purposes". O'Neill (2024), running BCRZ's own code: "as the noise level increases, the performance of SSQP degrades significantly with respect to infeasibility". O'Neill's causal attribution to the merit parameter estimate is his own, and his test uses simulated noise on CUTEst.
- **X3. Almost-sure convergence: "no significant additional insights" (survey, 2016–2018) versus "stopping criteria are predicated on establishing strong convergence" (Patel, 2020–2022)**, and versus Curtis's own later almost-sure headline results (2023–2025).
- **X4. Which stochastic regime matters.** Na et al. and Fang et al.: prespecified sequences "highly" or "significantly" affect performance, so adaptive line search or trust-region steps with sampled accuracy are better. Berahas–Curtis–O'Neill–Robinson: such line searches "may require [...] relatively accurate stochastic gradient estimates", which their "more stochastic regime" avoids. Neither side has settled this with a shared benchmark that I found.
- **X5. Complexity framework.** CGT (2017) place his CRS framework inside their optimality theory and prove its bound optimal. Curtis and Robinson (2018) call "our worst-case analysis for nonconvex optimization" "faulty" and propose regional complexity. Both are on record; no exchange between them was found.
- **X6. Reception of the infeasibility line.** It is praised as "creatively presented" and as a result that "could be used within our framework" (Dai–Liu–Sun; Gould–Loh–Robinson). Yet a sibling method (PIPAL) is called slow or complex (Hinder–Ye), and his own group calls the 2010 method practically disadvantaged (BCW 2014).

## Gaps

- **Referee reports and rebuttals**: none are public. His venues use closed review. OpenReview was not reachable for 03, and the one ML-conference paper (ICML 2016) was not checked.
- **Failed replications**: none found. No replication study of his numerical claims exists in the sources searched. The closest items are outside benchmarks (6.2, 6.3) and O'Neill's rerun of BCRZ code (1.2).
- **Who disputed "codes fail too often"** (ISMP 2018): not found.
- **CGT or others' reply to the regional-complexity critique**: not found.
- **Full texts not read** (quotes rest on the Semantic Scholar citation-context index and are marked "via S2 context"):
  - Heinkenschloss–Ridzal 2008;
  - Schenk–Wächter–Weiser 2008;
  - Hicken 2014 (the quoted sentence is truncated in the index);
  - Huber 2013 (the edoc bitstream returned an HTML page, not the PDF);
  - Johnson–Kirches–Wächter 2015;
  - Berahas–Bollapragada–Zhou 2022;
  - Curtis & Shi 2022;
  - Dai–Liu–Sun 2020;
  - Gould–Loh–Robinson 2015;
  - the BCWW arXiv:1803.09224 sentence.
  Heinkenschloss–Ridzal *SIAM J. Optim.* 24(3) 2014 (DOI 10.1137/130921738) was located but not read: the Rice repository handle redirects to a moved site, and the Sandia report SAND2011-9346 that was read does not mention Curtis.
- **Leads without a verifiable venue (not entered as findings).** P. Meng, "A matrix-free algorithm for reduced-space PDE-constrained optimization" (Semantic Scholar CorpusId 52094004, 2018, no venue) says the Byrd et al. methods "make assumptions regarding the structure of the problem that favor full-space formulations, and our experience applying them to reduced-space PDE-constrainted optimization has been disappointing". H. Wang's 2015 dissertation (a Curtis student; CorpusId 125769472) repeats the "numerous QO subproblems" point. Neither venue was confirmed.
- **PIPAL citation contexts** were not harvested: Semantic Scholar returned 404 for DOI 10.1007/s12532-012-0041-4, and a title search was rate-limited. Critique of PIPAL beyond Hinder–Ye may exist.
- **Coverage of the context index**: many citing records carry no context. TRACE has 135 citing records, and only 3 contexts matched critical wording. Papers on SIAM/Springer paywalls without an arXiv version could not be checked for text.
- **Predictions**: the survey's claim that SG's dominance is "far from settled", and the 2021 slide advocating adaptive second-order stochastic methods, were not tested against later practice (for example, optimizer-benchmark competitions). That would need sources not consulted here.
- **MathSciNet reviews**: not read (subscription). The zbMATH Open reviews were read and are descriptive.
- **The NonOpt (2025–26) and stochastic interior-point (2024–26) lines** are too recent for published critique. None was found.

## Sources

One line each: title, author(s), date, URL or DOI, primary/secondary. "Read" means the full text was opened unless marked "context only".

1. Na, Anitescu, Kolar, "An Adaptive Stochastic Sequential Quadratic Programming with Differentiable Exact Augmented Lagrangians", Math. Program. 199 (2023; online 2022), DOI 10.1007/s10107-022-01846-z; arXiv:2102.05320 v2 read (primary)
2. Fang, Na, Mahoney, Kolar, "Fully Stochastic Trust-Region Sequential Quadratic Programming for Equality-Constrained Optimization Problems", SIAM J. Optim. 34 (2024) 2007–2037, DOI 10.1137/22M1537862; arXiv:2211.15943 v2 read (primary)
3. Fang, Na, Mahoney, Kolar, "Trust-Region Sequential Quadratic Programming for Stochastic Optimization with Random Models", 2024, arXiv:2409.15734 v2 read (primary)
4. O'Neill, "A Two Stepsize SQP Method for Nonlinear Equality Constrained Stochastic Optimization", 2024, arXiv:2408.16656 v2 read (primary)
5. Hong, Na, Mahoney, Kolar, "Constrained Optimization via Exact Augmented Lagrangian and Randomized Iterative Sketching", ICML 2023 (arXiv comment), arXiv:2305.18379 read (primary)
6. Berahas, Bollapragada, Zhou, "An Adaptive Sampling Sequential Quadratic Programming Method for Equality Constrained Stochastic Optimization", 2022, arXiv:2206.00712, context only (secondary)
7. Bellavia, Morini, Rebegoldi, "An investigation of stochastic trust-region based algorithms for finite-sum minimization", Optim. Methods Softw. 39 (2024) 937–966, DOI 10.1080/10556788.2024.2346834; arXiv:2404.13382 read (primary)
8. Gratton, Jerad, Toint, "Complexity of a class of first-order objective-function-free optimization algorithms", Optim. Methods Softw. 41 (2026) 478–508, DOI 10.1080/10556788.2023.2296431; arXiv:2203.01647 v3 read (primary)
9. Nguyen, Nguyen, van Dijk, Richtárik, Scheinberg, Takáč, "SGD and Hogwild! Convergence Without the Bounded Gradients Assumption", ICML 2018, PMLR 80:3747–3755; arXiv:1802.03801 read (primary)
10. Patel, Zhang, Tian, "Global Convergence and Stability of Stochastic Gradient Descent", NeurIPS 2022, DOI 10.52202/068431-2610; arXiv:2110.01663 v3 read (primary)
11. Patel, "Stopping criteria for, and strong convergence of, stochastic gradient descent on Bottou-Curtis-Nocedal functions", Math. Program. 195 (2022) 693–734, DOI 10.1007/s10107-021-01710-6; arXiv:2004.00475 v2 read (primary)
12. Li, Milzarek, "A Unified Convergence Theorem for Stochastic Optimization Methods", 2022, arXiv:2206.03907 v2 read (primary)
13. Cartis, Gould, Toint, "Worst-case evaluation complexity and optimality of second-order methods for nonconvex smooth optimization", Proc. ICM 2018, 3711–3750, DOI 10.1142/9789813272880_0198; arXiv:1709.07180 read (primary)
14. Wright, "Optimization in Theory and Practice", 2025, arXiv:2510.15734 v2 read (primary)
15. Jiang, He, Zhang, Ge, Jiang, Ye, "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", J. Sci. Comput. (2025), DOI 10.1007/s10915-025-03154-y; arXiv:2311.11489 v4 read (primary)
16. Jiang, Zhang, Jiang, Ye, "Accelerating Trust-Region Methods: An Attempt to Balance Global and Local Efficiency", 2025, arXiv:2511.00680 v3 read, no critique of Curtis found (primary)
17. Hinder, Ye, "A one-phase interior point method for nonconvex optimization", 2018, arXiv:1801.03072 v2 read (primary)
18. Helou, Santos, Simões, "A fast gradient and function sampling method for finite-max functions", Comput. Optim. Appl. 71 (2018) 673–717, DOI 10.1007/s10589-018-0030-2; arXiv:1708.07473 read (primary)
19. Kungurtsev, Mitchell, Vyhlídal, "A Comparison of Nonsmooth, Nonconvex, Constrained Optimization Solvers for the Design of Time-Delay Compensators", 2018, arXiv:1812.11630 v1 read (primary)
20. Werner, Overton, Peherstorfer, "Multifidelity Robust Controller Design with Gradient Sampling", SIAM J. Sci. Comput. 45 (2023) A933–A957, DOI 10.1137/22M1500137; arXiv:2205.15050 read (primary)
21. Schwerdtner, Voigt, "SOBMOR: Structured Optimization-Based Model Order Reduction", 2020/2022, arXiv:2011.07567 v2 read (primary)
22. Fattahi, Sojoudi, "Exact Guarantees on the Absence of Spurious Local Minima for Non-negative Rank-1 Robust Principal Component Analysis", 2018, arXiv:1812.11466 read (primary)
23. Liang, Mitchell, Sun, "NCVX: A General-Purpose Optimization Solver for Constrained Machine and Deep Learning", OPT2022 workshop, arXiv:2210.00973 v2 read (primary)
24. Heinkenschloss, Ridzal, "An Inexact Trust-Region SQP Method with Applications to PDE-Constrained Optimization", Numerical Mathematics and Advanced Applications (ENUMATH 2007), pp. 613–620, DOI 10.1007/978-3-540-69777-0_73, context only (secondary)
25. Schenk, Wächter, Weiser, "Inertia-Revealing Preconditioning For Large-Scale Nonconvex Constrained Optimization", SIAM J. Sci. Comput. 31 (2008) 939–960, DOI 10.1137/070707233, context only (secondary)
26. Hicken, "Inexact Hessian-vector products in reduced-space differential-equation constrained optimization", Optim. Eng. 15 (2014) 575–608, DOI 10.1007/s11081-014-9258-6, context only (secondary)
27. Huber, "Interior-point methods for PDE-constrained optimization", PhD thesis, University of Basel, 2013, DOI 10.5451/unibas-006145479 (edoc record checked), context only (secondary)
28. Johnson, Kirches, Wächter, "An Active-Set Method for Quadratic Programming Based On Sequential Hot-Starts", SIAM J. Optim. 25 (2015) 967–994, DOI 10.1137/130940384, context only (secondary)
29. Dai, Liu, Sun, "A primal-dual interior-point method capable of rapidly detecting infeasibility for nonlinear programs", J. Ind. Manag. Optim. 16 (2020) 1009–1035, DOI 10.3934/jimo.2018190, context only (secondary)
30. Gould, Loh, Robinson, "A Nonmonotone Filter SQP Method: Local Convergence and Numerical Results", SIAM J. Optim. 25 (2015) 1885–1911, DOI 10.1137/140996677, context only (secondary)
31. Ridzal, Aguiló, Heinkenschloss, "Numerical study of a matrix-free trust-region SQP method for equality constrained optimization", Sandia report SAND2011-9346, Dec 2011, https://www.osti.gov/biblio/1038211, read; no mention of Curtis (primary)
32. Berahas, Curtis, Robinson, Zhou, "Sequential Quadratic Optimization for Nonlinear Equality Constrained Stochastic Optimization", SIAM J. Optim. 31(2) (2021) 1352–1379, DOI 10.1137/20M1354556, homepage preprint read (pp. 24–25) (primary)
33. Berahas, Curtis, O'Neill, Robinson, "A Stochastic Sequential Quadratic Optimization Algorithm for Nonlinear-Equality-Constrained Optimization with Rank-Deficient Jacobians", Math. Oper. Res. 49(4) (2024) 2212–2248, DOI 10.1287/moor.2021.0154; arXiv:2106.13015 read (primary)
34. Curtis, Robinson, Zhou, "A Stochastic Inexact Sequential Quadratic Optimization Algorithm for Nonlinear Equality-Constrained Optimization", INFORMS J. Optim. 6(3–4) (2024) 173–195, DOI 10.1287/ijoo.2022.0008; arXiv:2107.03512 read (primary)
35. Curtis, O'Neill, Robinson, "Worst-case complexity of an SQP method for nonlinear equality constrained stochastic optimization", Math. Program. 205 (2024) 431–483, DOI 10.1007/s10107-023-01981-1; arXiv:2112.14799 read (primary)
36. Curtis, Jiang, Wang, "Almost-Sure Convergence of Iterates and Multipliers in Stochastic Sequential Quadratic Optimization", J. Optim. Theory Appl. 204 (2025), DOI 10.1007/s10957-024-02568-2; arXiv:2308.03687 read (primary)
37. Curtis, Robinson, Zhou, "Sequential Quadratic Optimization for Stochastic Optimization with Deterministic Nonlinear Inequality and Equality Constraints", SIAM J. Optim. 34 (2024) 3592–3622, DOI 10.1137/23M1556149; arXiv:2302.14790 read (p. 8) (primary)
38. Burke, Curtis, Wang, "A Sequential Quadratic Optimization Algorithm with Rapid Infeasibility Detection", SIAM J. Optim. 24(2) (2014) 839–872, DOI 10.1137/120880045, homepage PDF read (p. 841) (primary)
39. Burke, Curtis, Wang, Wang, "Inexact Sequential Quadratic Optimization with Penalty Parameter Updates Within the QP Solve: Extended Version", 2018, arXiv:1803.09224, context only (secondary)
40. Curtis, Robinson, Samadi, "An inexact regularized Newton framework with a worst-case iteration complexity of O(ε^-3/2) for nonconvex optimization", IMA J. Numer. Anal. 39 (2019) 1296–1327, DOI 10.1093/imanum/dry022; arXiv:1708.00475 v1 and v4 read (primary)
41. Curtis, Scheinberg, Shi, "A Stochastic Trust Region Algorithm Based on Careful Step Normalization", INFORMS J. Optim. 1 (2019) 200–220, DOI 10.1287/ijoo.2018.0010, homepage PDF opened (primary)
42. Curtis, Shi, "A fully stochastic second-order trust region method", Optim. Methods Softw. 37 (2022) 844–877, DOI 10.1080/10556788.2020.1852403, context only (secondary)
43. Curtis & Robinson, slides "How to Characterize the Worst-Case Performance of Algorithms for Nonconvex Optimization" (ISMP 2018), http://coral.ise.lehigh.edu/frankecurtis/files/talks/ismp_18.pdf, read (slide 4/31) (primary)
44. Curtis, slides "Nonconvex Optimization: Opportunities and Challenges" (ECOM public lecture, 2 Apr 2021), http://coral.ise.lehigh.edu/frankecurtis/files/talks/2021_ecom_public.pdf, read (slide 32/45) (primary)
45. Semantic Scholar Graph API, citation contexts for 14 Curtis papers (DOIs 10.1137/20m1354556, 10.1007/s10107-016-1026-2, 10.1137/060674004, 10.1137/090780201, 10.1080/10556788.2016.1208749, 10.1007/s12532-015-0086-2, 10.1007/s10107-008-0248-3, 10.1137/080738222, 10.1137/120880045, 10.1007/s10107-014-0784-y, 10.1137/090747634, 10.1287/ijoo.2018.0010, 10.1137/1.9781611978599, 10.1137/16m1080173), fetched 2026-09-28, https://api.semanticscholar.org/graph/v1/ (secondary)
46. zbMATH Open API, documents by "Curtis, Frank E." (75 records, 10 reviews), fetched 2026-09-28, https://api.zbmath.org/v1/document/_search (secondary)
47. Crossref REST API, checks of 33 DOIs, 2026-09-28, https://api.crossref.org/works/ (secondary)
48. arXiv abstract pages (version histories and journal references) for 20 arXiv ids cited above, 2026-09-28, https://arxiv.org/abs/ (secondary)
49. Web search results (2 queries: Heinkenschloss–Ridzal SIOPT 2014 location; TRACE comparisons), 2026-09-28, which led to https://www.osti.gov/biblio/1038211 and arXiv:2311.11489 / 2511.00680 (secondary)
