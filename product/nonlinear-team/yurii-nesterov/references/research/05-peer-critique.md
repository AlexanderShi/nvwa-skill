# 05 · Peer critique: where Yurii Nesterov's methods and judgements have been challenged

| Field | Value |
|---|---|
| Researcher | Yurii E. Nesterov (CORE / INMA, UCLouvain, emeritus) |
| Dimension | Research agent 05 of 06: peer critique. Covers published criticism, rival explanations and competing methods, benchmark evidence, public reviews, improvements that overtook his bounds, and his own judgements or predictions that did not hold |
| Research date | 2026-09-28 |
| Sources consulted | 53 listed under "Sources": 11 are Nesterov's own or co-authored texts (P), 41 are texts by others (S), and 1 is a public dataset. Five entries were identified but not read beyond the title or DOI: Ye's 1994 SIAM Review book review (SIAM returned 403), Van Scoy et al. 2018, Curtis–Robinson–Samadi 2017, Nesterov's two inexact proximal-point papers (one entry), and Nesterov–Polyak 2006 (known here only through CGT). Most items were read at abstract level. The passages quoted from full texts were read in full, with page numbers |
| WebSearch calls | 2 of the 2 allowed: (1) critical essays and blogs on acceleration, which found the d'Aspremont–Scieur–Taylor monograph; (2) practical tests of Nesterov's third-order methods, which found Cartis et al. 2024/2026 |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`. `private/` was not opened |
| Transcripts saved | none |
| Language | English (per team.json) |

**Tags.**
- **[stated]**: Nesterov wrote or said it.
- **[practice]**: what his papers, code or records show.
- **[observed]**: a third party (critic, reviewer, rival, colleague) said or showed it. Almost every critique in this file is [observed].
- **[inferred]**: my reading. The basis is given each time. Do not quote it as anyone's view.
- **(P)** marks a text written or co-written by Nesterov. **(S)** marks a text by someone else: first-hand for the critic's own claim, second-hand for Nesterov.

**Reading these critiques fairly.**
- Most "critiques" below are published papers that improve on, reinterpret or bound one of his results. They are not polemics.
- I found no polemical exchange, no failed replication of a proved result, no retraction and no published "comment and reply" pair involving Nesterov.
- Proof-based work cannot fail a replication in the empirical sense. His results get *refined* (better constants, better rates, weaker assumptions), *qualified* (limits of applicability) or *reinterpreted* (rival explanations).
- **Several critics are close colleagues.** Nemirovski is his main co-author; Devolder and Glineur are UCLouvain colleagues; Taylor trained in that group; d'Aspremont wrote in the Optima 78 discussion of his work. Their criticism comes from inside the school.
- **Several critics are members of this team**: Wright; Curtis and Nocedal (with Bottou); Gould and Toint (with Cartis); Ye; Curtis again (TRACE). §8 collects their positions for the roundtable.

---

## 1. Accelerated (fast) gradient method, 1983

### 1.1 "The proof works but explains nothing": the intuition critique

Critic by critic, in date order. Every item is [observed] (S) unless marked otherwise.

- **Allen-Zhu & Orecchia 2014/2017** (arXiv 1407.1537v5, p. 4):
  - Accelerated methods "are often regarded as “analytical tricks” [17] because their convergence analyses are somewhat complicated and lack of intuitions." Their [17] is Juditsky's 2013 lecture notes.
  - Footnote 7, p. 5: "little is known on why this linear combination is needed from his proof, except for being used as an algebraic trick to cancel specific terms."
  - Abstract: linear coupling "gives a cleaner interpretation than Nesterov's original proofs", with extensions "to many other settings that Nesterov's methods cannot apply to".
- **Su, Boyd & Candès 2015/2016** (arXiv 1503.01243v2; JMLR 17(153)). Abstract: "We show that the continuous time ODE allows for a better understanding of Nesterov's scheme."
- **Bubeck, Lee & Singh 2015** (arXiv 1506.08187, pp. 1–2): "the intuition behind Nesterov’s accelerated gradient descent is notoriously difficult to grasp, and this has led to a recent surge of interest in new interpretations of this algorithm". Their geometric method comes with "some numerical evidence that the new method can be superior to Nesterov's accelerated gradient descent" (abstract).
- **Wibisono, Wilson & Jordan 2016** (PNAS significance statement): "However, accelerated methods are not descent methods and remain a conceptual mystery."
- **Bottou, Curtis & Nocedal 2016/2018** (SIAM Review; arXiv 1606.04838v3, §7.2, p. 70): "Unfortunately, no intuitive explanation as to how Nesterov’s method achieves this optimal rate has been widely accepted. Still, one cannot deny the analysis and the practical gains that the technique has offered." **Two team members are among these authors.**
- **d'Aspremont, Scieur & Taylor 2021** (*Acceleration Methods*; arXiv 2101.09545v4, p. 2): "Ever since the original algorithm by Nesterov (1983), the acceleration phenomenon was regarded as somewhat of a mystery. While accelerated gradient methods can be seen as iteratively building a model for the function and using it to guide gradient computations, the argument is essentially algebraic and is simply an effective exploitation of regularity assumptions." On p. 3, after introducing performance estimation: "Using this framework, acceleration is no longer a mystery: it is the main objective in the design of the algorithm."
- **Reception, from the IMU (Jackson 2026)**: the 1983–84 work "went largely unnoticed". Jackson gives the Cold War as one reason, and "A more important reason was that the kinds of problems people were trying to solve back in the 1980s were not amenable to Nesterov’s method."

**Was it answered?**
- In the material read, **Nesterov never responds to the intuition critique directly.**
- His stated standard is that the proof is the explanation. 02, T9 (2023): "What is important is to prove that you are right". He also re-derives his methods in simpler forms (the ICM 2010 "simplified version"; see 01 §4A). [stated] P
- **The rival explanations disagree with each other.** They offer linear coupling, an ODE, geometry, a variational Lagrangian, and PEP/Chebyshev design. Each claims to demystify the method. None is presented as the accepted one, and Bottou–Curtis–Nocedal say none is. [observed]

**Blind spot shown [inferred]:**
- His writing optimizes *verifiability* (a short chain of inequalities, the estimate sequences), not *transferability of the idea*.
- Outsiders rebuilt the idea five different ways before they could extend it. Allen-Zhu & Orecchia and Wibisono et al. both present their reinterpretation as the route to generalization.

### 1.2 Behaviour in practice: non-monotonicity, ripples, unknown µ

- **Non-monotone, oscillating iterates** [observed, S]:
  - O'Donoghue & Candès (arXiv 1204.3982v1, p. 1; *FoCM* 2015): "Unlike gradient descent, accelerated methods are not guaranteed to be monotone in the objective value. A common observation when running an accelerated method is the appearance of ripples or bumps in the trace of the objective value".
  - Su–Boyd–Candès (p. 3): "Oscillations or overshoots along the trajectory of iterates approaching the minimizer are often observed when running Nesterov’s scheme."
- **Sensitivity to the strong-convexity estimate** [observed, S] (O'Donoghue & Candès, p. 3):
  - "Estimating the strong convexity parameter is much more challenging."
  - "slightly over or underestimating the optimal value of q for the function can have a severe detrimental effect on the rate of convergence".
  - On Nesterov's own µ-estimation in the 2007 composite paper (their ref. [16] = CORE DP 2007/76): "His scheme achieves a convergence rate quite a bit slower than Algorithm 1 with a known value of µ."
- **Fixed restart criticized** [observed, S]:
  - The 1983 note already restarts every ⌈4√(L/m)⌉ − 1 iterations. This needs m (see 01 §4A). [practice] P
  - O'Donoghue & Candès (§3.1, p. 6): "The drawbacks in using fixed restarts are that firstly it depends on unknown parameters L and, more importantly, µ, and secondly it is a global parameter that may be inappropriate in better conditioned regions."
  - Their remedy is heuristic adaptive restart (function or gradient test). Su–Boyd–Candès then give a restart with a proved linear rate (abstract).
- **Answer.** [practice, P; inferred]
  - Nesterov's own programme did remove unknown *L* (backtracking in 1983, the universal methods in 2013).
  - In what was read, the µ problem and adaptive restart were solved by others: O'Donoghue–Candès; Su–Boyd–Candès; the restart chapter of d'Aspremont–Scieur–Taylor, which "conclude[s] by discussing restart schemes, a set of simple techniques for reaching nearly optimal convergence rates while adapting to unobserved regularity parameters" (abstract).

### 1.3 Robustness: errors, noise and stochastic gradients

- **From his own group, joint text** [stated, P]. Devolder, Glineur & Nesterov (CORE DP 2011/2; *Math. Program.* 146, 2014), abstract:
  - "It appears that in inexact case, the superiority of the fast gradient methods over the classical ones is not anymore absolute. Contrary to the simple gradient schemes, fast gradient methods necessarily suffer from accumulation of errors. Thus, the choice of the method depends both on desired accuracy and accuracy of the oracle."
  - This is the clearest case of the school qualifying its own flagship.
- **A competing error model** [observed, S]. d'Aspremont (arXiv math/0512344; *SIAM J. Optim.* 19, 2008), abstract: "the optimal complexity of Nesterov's smooth first-order optimization algorithm is preserved when the gradient is only computed up to a small, uniformly bounded error." The two results rest on different error assumptions. Kept as a contradiction, not reconciled.
- **Control-theory analysis** [observed, S]. Lessard, Recht & Packard (arXiv 1408.3595v7; *SIAM J. Optim.* 26, 2016):
  - p. 21: "Unlike the Gradient method, Nesterov’s accelerated method is not robust to having a changing fk."
  - p. 2: they derive "first-order methods that achieve nearly the same rate of convergence as Nesterov’s accelerated method but are more robust to noise."
  - p. 21 also shows that their certified rate for the standard tuning "is strictly better than the rate proved in [23] using estimate sequences". So his own bound was loose.
- **Stochastic gradients** [observed, S]:
  - Kidambi, Netrapalli, Jain & Kakade (arXiv 1803.05591; ITA 2018), abstract: there "exist simple problem instances where these methods cannot outperform SGD despite the best setting of its parameters". HB's and NAG's "practical performance gains are a by-product of mini-batching".
  - Their fix is "based on a relatively less popular variant of Nesterov's Acceleration". So the remedy came from his own toolbox.
  - Bottou–Curtis–Nocedal (p. 70): in stochastic settings "one can only hope that acceleration might improve the constants … the rate itself cannot be improved".
- **Scope** [inferred]: Nesterov's acceleration results are deterministic, exact-oracle results. His group documented the inexact-oracle limit itself (2011/2014). The stochastic limit was documented by others.

### 1.4 "Optimal" only up to a constant: performance estimation

- **Drori & Teboulle** (*Math. Program.* 145, 2014; arXiv 1206.3209) [observed, S]:
  - They turn worst-case analysis into an optimization problem (PEP).
  - They find numerically the step coefficients that give "a first-order black-box method that achieves best performance" (abstract).
- **Kim & Fessler** (*Math. Program.* 159, 2016) [observed, S], abstract: the optimized gradient method (OGM) achieves "a convergence bound that is two times smaller than for Nesterov’s fast gradient methods", with "efficient recursive forms that are remarkably similar to Nesterov's fast gradient methods".
- **Drori** (*J. Complexity* 39, 2017, 1–16), abstract: a new lower bound that "matches the worst-case performance of the recently introduced Optimized Gradient Method, thereby establishing that the bound is tight". Exact optimality for smooth convex minimization therefore belongs to OGM, not to Nesterov's FGM. FGM is optimal up to a constant factor.
- **The strongly convex case**:
  - Taylor & Drori (*Math. Program.* 199, 2023), abstract: a method whose bound "exactly matches the lower bound on the oracle complexity".
  - Van Scoy, Freeman & Lynch (*IEEE L-CSS* 2, 2018) is titled "The Fastest Known Globally Convergent First-Order Method for Minimizing Strongly Convex Functions". **Title only; the paper was not read.**
- **The UCLouvain link** [observed, S]. Taylor, Hendrickx & Glineur (*Math. Program.* 161, 2017) made PEP exact, "dimension-independent". Glineur and Hendrickx are Nesterov's Louvain colleagues.
- **Answered?** No response by Nesterov to PEP was found in the material read.
- **Method lesson** [inferred]. His notion of "optimal" is order-optimal. Constants were left to others, who found them by computer-assisted proof. He does not use this tool himself. That is consistent with his pen-and-paper practice in 03 §1.

---

## 2. Self-concordant barriers and polynomial-time interior-point theory (1988–1994)

- **The theory's worst-case character, from his co-author** [observed, S; insider]. Nemirovski & Todd, *Acta Numerica* 17 (2008), p. 202, on the basic path-following method: "At the same time, from a practical perspective a severe shortcoming of the algorithm is its worst-case-oriented nature: as presented, it will always perform according to its worst-case theoretical complexity bounds. There exist implementations of IPMs that are much more powerful in practice, using more aggressive parameter updating policies that are adjusted during the course of the algorithm."
- **The universal barrier as an existence result** [observed, S]:
  - Nemirovski & Todd, p. 208: "From a practical perspective, the existence theorem just formulated is not of much interest – the universal barrier is usually pretty difficult to compute, and in the rare cases when this is possible, it may be non-optimal in terms of its self-concordance parameter."
  - The self-concordance parameter was later sharpened: Bubeck & Eldan (arXiv 1412.1587), abstract, "improving a seminal result of Nesterov and Nemirovski"; Lee & Yue (*Math. Oper. Res.* 46, 2021), abstract: the bound n is "tight and improves the previous O(n) bound by Nesterov and Nemirovski".
- **Convexity only** [observed, S]:
  - Nemirovski & Todd, p. 193: "The theory of self-concordant barriers is limited to convex optimization."
  - Their §4 (p. 228) on IPMs for nonconvex NLP: "the motivating concerns are very different from those for convex optimization: global convergence (possibly to an infeasible point which is a local minimizer of some measure of infeasibility) replaces complexity analysis; superlinear convergence, and the resulting careful control of the parameter t, is of considerable interest; step-size control usually involves a merit function; and modifications to Newton systems are often employed to avoid convergence to stationary points that are not local minimizers."
  - **For this team, this is the key limit.** The machinery inside Ipopt- or KNITRO-type solvers is not what self-concordance theory analyses.
- **Self-concordance excludes common losses** [observed, S]:
  - Bach (*Electron. J. Statist.* 4, 2010; arXiv 0910.4627v1, p. 4): "The logistic function u ↦ log(1 + e^{−u}) is not self-concordant as the third derivative is bounded by a constant times the second derivative (without the power 3/2)."
  - The price of Bach's fix (p. 5): "the notion and the results are not invariant by affine transform (contrary to self-concordant functions)".
  - Sun & Tran-Dinh (*Math. Program.* 178, 2019; arXiv 1703.04599v3, p. 2) generalize the definition. They say the multivariate properties of the standard case "do not hold for the case ν ≠ 3". They also note that self-concordance "is less well-known in other communities".
- **The book itself** [observed, S]:
  - zbMATH reviewer M. A. Hanson on the 1994 book: "Algorithms are given, but numerical results are omitted."
  - Yinyu Ye reviewed the book in *SIAM Review* 36(4) (1994) 682–683, DOI 10.1137/1036175. **Not read** (SIAM returned 403). Ye is a team member, so his contemporary judgement would be valuable. This is a gap.
- **Answered?**
  - The long-step and primal–dual answer came partly from Nesterov himself [practice, P]: Nesterov–Todd self-scaled cones (1997/98) and "Long-step strategies in interior-point primal-dual methods" (*Math. Program.* 76, 1997), listed in 01.
  - Nemirovski & Todd (p. 222) cite "Algorithms 6.2 and 6.3 in Nesterov and Todd (1998)" as adaptive algorithms that "can give much better results in practice". So the shortcoming was addressed for symmetric cones, and by Nesterov's own later work.
  - For general nonconvex NLP it was not addressed. He did not work on nonconvex NLP IPMs.

---

## 3. Cubic regularization (Nesterov–Polyak 2006) and tensor methods (2018–2021)

### 3.1 Priority, numerics and the global subproblem: the trust-region school's critique

Source: Cartis, Gould & Toint (CGT), ARC Part I (*Math. Program.* 127, 2011, DOI 10.1007/s10107-009-0286-5). Read in the Namur preprint dated 29 Sept 2007, revised 25 Sept 2008. All items [observed, S]; **two authors are team members**.

- **Priority.** The cubic-model step "was, as far as we know, first considered by Griewank (in an unpublished technical report [19])" (1981). Then: "More recently, Nesterov and Polyak [25] considered a similar idea … although from a different perspective" (preprint p. 2). Also listed in 01.
- **No numerics.** "Global convergence to second-order critical points and asymptotically quadratic rate of convergence were also proved for this method, but no numerical results were provided." (p. 2)
- **Assumptions relaxed.** Three changes (p. 2):
  - "we relax the need to compute a global minimizer over IRn";
  - "we do not insist that H(x) be globally, or even locally, Lipschitz";
  - a dynamic σ_k replaces "the scaled Lipschitz constant".
- **Subproblem cost.** Computing the exact global model minimizer "may be in general prohibitively expensive from a computational point of view, and thus, for most (large-scale) practical purposes, (highly) inefficient" (§3.2, p. 13).
- **Complexity does not explain performance.** This bears on Nesterov's taste. On CUTEr tests (§7, pp. 33–34):
  - "Whether this is a consequence of a provably good complexity bound or for other reasons of robustness is not clear."
  - Of their own variants, the one "which is less concerned with provably superior worst-case complexity, appears to be more promising."
- **Nesterov's view of the same subproblem**, in CGT's summary (p. 2): Nesterov–Polyak showed "the model's global minimizer could be computed in a manner acceptable from the complexity point of view". So "acceptable in complexity" and "prohibitive in practice" describe the same subproblem. Kept as a contradiction.
- **Answered?** [practice, P; inferred]
  - Nesterov's 2021 tensor paper cites CGT (refs. [11]–[14]) and GALAHAD (ref. [16]). It adopts an adaptive-constant concern as an open problem. §6: "One of the difficult unsolved problems in our approach is related to dynamic adjustment of the Lipschitz constant for the highest derivative … This question is clearly crucial for the practical efficiency of the high-order schemes."
  - That concedes CGT's practical point for p ≥ 3 without saying so.
  - Griewank's priority is not acknowledged in that paper's reference list. It cites Griewank only for algorithmic differentiation (ref. [19], Griewank & Walther 2008).
- **A rival school's answer on complexity** [observed, S; title only]. Curtis, Robinson & Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{−3/2}) for nonconvex optimization", *Math. Program.* 162 (2017) 1–32. The title claims that a trust-region method matches the cubic-regularization bound. **Abstract and text not read.** A team member is the first author.
- **Nonconvex subproblem** [observed, S]. Carmon & Duchi (*SIAM J. Optim.* 29, 2019), abstract: for the nonconvex cubic model, "gradient descent approximates the global minimum" under mild assumptions. This is a matrix-free answer to the subproblem-cost critique.

### 3.2 Accelerated second-order and tensor methods: overtaken bounds and a failed prediction

- **Beaten rate** [observed, S]. Monteiro & Svaiter (*SIAM J. Optim.* 23, 2013), abstract:
  - Their A-NPE method "has a O(1/k^{7/2}) convergence rate, which improves upon the O(1/k^3) convergence rate bound for another accelerated Newton-type method presented by Nesterov" (the 2008 accelerated cubic Newton, *Math. Program.* 112).
  - And: "while Nesterov's method is based on exact solutions of subproblems with cubic regularization terms, the A-NPE method is based on inexact solutions of subproblems with quadratic regularization terms and hence is potentially more tractable from a computational point of view."
- **His framing of the rival** [stated, P]. Tensor paper §1: "…up to the lower complexity bounds (see [1, 2, 13, 18]) and attempts of constructing the optimal methods [24]". [24] is Monteiro–Svaiter.
  - On his own lower bound (§1): "This result is better than the bound in [1] and coincide with the bound in [2]. However, it seems that our justification is simpler." [2] is Arjevani, Shamir & Shiff (arXiv May 2017; *Math. Program.* 178, 2019). Nesterov's CORE DP 2018/05 came later.
- **His own admission and his prediction** [stated, P], tensor paper §6:
  - "we failed to develop an optimal tensor scheme".
  - Then: "Any additional logarithmic factors in the complexity bound of this “optimal” method will definitely kill its tiny superiority in the convergence rate."
- **What happened next** [observed, S]:
  - Near-optimal methods with log factors came first. Jiang, Wang & Zhang (arXiv 1812.06557) built on "the Accelerated Hybrid Proximal Extragradient (A-HPE) framework proposed in Monteiro and Svaiter (2013), where a bisection procedure is installed".
  - In 2022 two groups removed the log factor. Kovalev & Gasnikov (arXiv 2205.09647): existing methods "require performing a complex binary search procedure, which makes them neither optimal nor practical. We fix this fundamental issue". Carmon, Hausler, Jambulapati, Jin & Sidford (arXiv 2205.15371) improve "by a logarithmic factor, matching a lower bound".
  - Carmon et al. also report a practical result: "On logistic regression our method outperforms previous second-order momentum methods, but under-performs Newton's method; simply iterating our first-order adaptive subproblem solver performs comparably to L-BFGS."
- **Assessment** [inferred]:
  - The 2019/21 premise, that an optimal scheme would carry log factors, was overtaken within three years.
  - His practical scepticism about the extra acceleration is **not refuted**. In the one comparison read, the optimal accelerated method lost to plain Newton.
  - Kept as a contradiction (see "Contradictions" 2).
- **"Implementable and very fast"** (DP 2018/05 and *Math. Program.* 2021 abstract, no experiment; 03 §3.1) [observed, S]. Cartis, Hauser, Liu, Welzel & Zhu (arXiv 2501.00404v3, p. 5; *Math. Program. Comput.* 18(3), 2026):
  - After crediting "Tensor methods for convex optimization problems have been pioneered by Nesterov": "However, all these developments have remained generally theoretical when p ≥ 3, so that the efficient implementation of higher-order methods (for p ≥ 3) remains an active area of investigation in which the community has not yet settled on a consensus."
  - Their benchmark measures evaluations and treats wall-clock time "as secondary" (p. 6). Their abstract says that "AR3 variants can be made to outperform second-order variants in terms of objective evaluations, derivative evaluations, and number of subproblem solves".
  - They work with the **nonconvex** regularized subproblem. Nesterov's design avoids it by regularizing until the model is convex (01 §4D).
- **His collaborators' view differs** [observed, S]. Kamzolov, Gasnikov, Dvurechensky, Agafonov & Takáč (arXiv 2208.13190), abstract: "it was shown that such methods can be implementable since the appropriately regularized Taylor expansion of a convex function is also convex and, thus, can be minimized in polynomial time." Here "implementable" means polynomial-time solvable; for Cartis et al. it means efficient in practice. The two camps use the word differently [inferred].

---

## 4. Randomized coordinate descent (CORE DP 2010/2; *SIAM J. Optim.* 2012)

- **His own caveat first** [stated, P]. CORE DP 2010/2, p. 17: "However, for some applications (e.g. Section 6.3), the complexity of one iteration of the accelerated scheme is rather high since for computing yk it needs to operate with full-dimensional vectors."
- **Lee & Sidford** (FOCS 2013; arXiv 1305.1922v1, p. 3) [observed, S]: "in both Nesterov’s paper [24] and later work [25], this method was considered inefficient as the computational complexity of the naive implementation of each iteration of ACDM requires Θ(n) time". They supply an implementation with no asymptotic overhead (§4.3, p. 12). Credit is explicit: "the bulk of the credit for conceiving of such a method belongs to Nesterov".
- **Richtárik & Takáč** (*Math. Program.* 144, 2014; arXiv 1107.2848), abstract [observed, S]: "in contrast with the aforementioned work in which the author achieves the results by applying the method to a regularized version of the objective function with an unknown scaling factor, we show that this is not necessary, thus achieving true iteration complexity bounds". They also report "improving the complexity by the factor of 4 and removing ε from the logarithmic term".
- **Stephen J. Wright, team member** (*Math. Program.* 151, 2015; arXiv 1502.04759v1, p. 17) [observed, S]: "One fact detracts from the appeal of accelerated CD methods over standard methods: the higher cost of each iteration of Algorithm 4." His abstract adds that "efficient implementations of accelerated coordinate descent algorithms are possible" for a common ML structure.
- **Answered** [practice, P]. Nesterov & Stich (*SIAM J. Optim.* 27, 2017), abstract: "In many important situations, the computational expenses of oracle and method itself at each iteration of our scheme are perfectly balanced (both depend linearly on dimensions of the problem)." This is one of the few visible cases where a peer critique of cost is answered by him, seven years on, with a co-author. No reply to Richtárik–Takáč's "unknown scaling factor" point was found.
- **The context he set** [stated, P]. DP 2010/2, p. 2 reproduces the old criticism of coordinate descent: "it seems that no room is left for supporting the coordinate descent idea". Then: "let us look again at the above criticism. It appears, that there is a small chance for these methods to survive." He answers a field-level critique by changing the problem class (huge-scale, distributed data). That is his pattern (02 I8, 03 §2.2).

---

## 5. Smoothing and the 2005 primal–dual schemes

- **Precision ceiling** [observed, S]. d'Aspremont, Optima 78 (Nov 2008) discussion, p. 10: "First-order methods for semidefinite optimization tradeoff a much lower cost per iteration with a much higher dependency on the target precision. This means that one cannot hope to obtain solutions up to a precision 10−8 that is routinely achieved by interior point algorithms." In the same column (p. 9) d'Aspremont, Peña and Scheinberg call smoothing an "important theoretical advance" and "an inspiration". A supportive voice that names the limit.
- **Fixed smoothing parameter** [observed, S]. Tran-Dinh (*Comput. Optim. Appl.* 66, 2017; arXiv 1509.00106), abstract: "a new homotopy strategy for smoothness parameter" that "allows one to automatically update the smoothness parameter at each iteration" at the same per-iteration cost. The implied limit: in the 2005 scheme μ is fixed in advance from ε.
- **Answered in part, by himself, the same year** [practice, P]. The excessive gap technique (*SIAM J. Optim.* 16, 2005), abstract: "a new primal-dual technique" giving O(1/k) with primal–dual control. Whether it fully removes the fixed-μ issue was **not checked** (abstract only).
- **A concurrent rival** [observed, S]. Nemirovski's prox-method (*SIAM J. Optim.* 15, 2004), abstract: "efficiency estimate O(ε^{−1}) for approximating saddle points of convex-concave C^{1,1} functions", tested on large matrix games. Same rate, different mechanism, published the same year. d'Aspremont (Optima 78) lists it among "alternative algorithms with similar characteristics". No priority dispute was found.

---

## 6. His taste itself: complexity-first and convexity-first

- **Complexity analysis as the selector** [stated, P]. 2008/2010: complexity analysis selects "the promising optimization methods among hundreds of others" (02 T3). In 2013 rate estimates may count for more than preliminary experiments (02 T4).
- **Counter-evidence from three directions** [observed, S]:
  1. CGT (2008 preprint): the variant "less concerned with provably superior worst-case complexity" did better. Whether complexity explains the gains "is not clear" (§3.1).
  2. Nemirovski–Todd (2008): the worst-case-oriented path-following method is a "severe shortcoming" in practice. For nonconvex NLP, "global convergence … replaces complexity analysis" (§2).
  3. Performance estimation: order-optimal is not optimal. The constant factor was left on the table for 30 years (§1.4).
- **Convexity as the mark of a solved problem** [stated, P]. NCCR interview, 15 Aug 2023 (quoted in 02 T7, re-checked here): "If there is no convexity, we can find only the local minimum. … So what's the point? It's very easy to get non-convex problems but for me, this means that we didn't think enough." On neural networks: "People are applying different algorithms for non-convexity – we still don’t understand what happens. There is no convex model in this field. It will be done when this convex model can be found."
- **Rival view** [observed, S; the juxtaposition is inferred]. Sun, Qu & Wright (arXiv 1510.06096; John Wright of Columbia, not the team member), abstract: for smooth nonconvex problems where "all local minimizers are also global" and saddles have negative curvature, "a second-order trust-region algorithm … provably converges to a global minimizer efficiently, without special initializations". Carmon–Duchi (§3.1) likewise solve a nonconvex subproblem globally.
  - Neither paper addresses Nesterov. **I found no published critique of his 2023 statement.**
  - For a solver team the point is practical. Nonconvex NLP is the team's core business, and on it Nesterov's taste is openly one-sided (see also 02, Contradiction 3).

---

## 7. Public reviews, excursions and predictions

- **Conference reviews of co-authored ML papers** [observed, S; the author feedback is co-signed, P]. Local copies saved by agent 03 in this run.
  - *NeurIPS 2020, Doikov & Nesterov.* The weaknesses the reviewers raised:
    - "I do not see a clear answer to the questions “for which problems the proposed approach has practical benefits?”"
    - "The advantage of the proposed method over simple non-affine invariant methods … is not clear. The authors should discuss the overall complexity, since the proposed method is more expensive per iteration."
    - "the main assumption -- bounded D -- is very strong".
    - The paper should "empirically compare proposed algorithms with existing second-order methods with line-search".
  - The meta-review was positive. What the rebuttal promised and what was delivered is in 03 §2.1: the line-search comparison was promised and not delivered.
  - *NIPS 2016, Bogolubsky et al.* (8 authors, Nesterov one of them). Reviewers wrote:
    - "the main optimization points made here are adaptations of those proposed in" Nesterov & Spokoiny;
    - "the authors only compared their work with GBP";
    - "all the meat appears in the appendix";
    - "I have doubts about whether the technical assumptions stated will hold in emprical data".
  - [inferred] The same objections recur: practical benefit, per-iteration cost, strong assumptions, thin baselines. The trust-region school raised these in 2008 too.
- **Book reviews.** zbMATH reviews of the 1994, 2004 and 2018 books (Hanson, Todorov, Anholcer) and of the 2013 composite paper (Thierfelder) are descriptive. The only critical line is Hanson's "numerical results are omitted". [observed, S]
- **A prediction outside optimization: the COVID-19 papers, 2020.** Solo CORE DPs 2020/22 and 2020/25 (arXiv 2007.11429v2, dated 24 July 2020) [stated, P]:
  - Abstract of 2020/25: "Our analysis shows that all tested countries are in a dangerous zone except Sweden."
  - §3.11: "the number of asymptomatic virus holders in Sweden now is on the level of four thousands and it is decreasing".
  - Conclusions: "We have already seen the success stories of Japan, Sweden, and The Netherlands, where the number of asymptomatic virus holders was reduced up to a very small level by quite reasonable restrictions in the social behavior." DP 2020/22 abstract: "our predictions were exact, typically, within the accuracy of 0.5%".
  - **What the data show** [inferred; OWID weekly confirmed cases, downloaded 2026-09-28]:
    - Sweden's weekly cases did fall through July 2020, from 7,455 in the week to 29 June to 1,316 in the week to 27 July. The short-term statement matches.
    - They then rose from 1,200 (week to 31 Aug) to 18,474 (2 Nov) and 46,177 (21 Dec).
    - The "success story" framing did not hold into the autumn.
  - **Caveats**:
    - Confirmed cases depend on testing volume.
    - The paper's claims are about the state in July, and it names the risk itself: "The final failures in some of these countries were related to the wrong choice of the stopping moment."
    - This is my comparison. **No peer critique of these papers was found.** 03 records no journal version and 2 citations.
  - [inferred] This is the one place where his quantitative claims can be checked against the world rather than against a proof. The excursion shows the same confidence style ("exact", "very precise") outside his field. The citation list suggests no epidemiologist engaged with it.

---

## 8. For the roundtable: team members who have criticized or qualified Nesterov's work

| Team member | Where | Position | Tag |
|---|---|---|---|
| Stephen J. Wright | *Math. Program.* 151 (2015), p. 17 | Accelerated CD's per-iteration cost "detracts from the appeal"; efficient implementations exist for some structures | [observed] S |
| Frank E. Curtis, Jorge Nocedal (with Bottou) | *SIAM Review* 60 (2018), p. 70 | No widely accepted intuition for acceleration; in stochastic settings only the constants can improve | [observed] S |
| Nicholas Gould, Philippe Toint (with Cartis) | ARC Part I (2011) | Priority to Griewank; no numerics; global subproblem impractical; complexity may not explain performance | [observed] S |
| Frank E. Curtis (with Robinson, Samadi) | *Math. Program.* 162 (2017) | Trust region matches the O(ε^{−3/2}) cubic-regularization bound (title only; not read) | [observed] S |
| Yinyu Ye | *SIAM Review* 36 (1994) 682–683 | Review of the 1994 IPM book; **not read** | — |

**Where Nesterov and the solver-builders agree** [inferred, from what was read]:
- Unknown constants must be estimated adaptively. Compare his universal methods and his tensor §6 with CGT's σ_k.
- Structure beats black-box generality.

**Where they part** [inferred]:
1. Does worst-case complexity predict practical performance?
2. May a method require a global subproblem solve or a known Lipschitz constant?
3. Is nonconvexity a modelling failure or the normal case?
4. Is "implementable" the same as "efficient"?

---

## 9. Failures, overtaken claims, abandoned directions (summary)

- **Overtaken bounds** (refined by others; no error in his proofs):
  - FGM constant, improved by a factor of 2 by OGM.
  - Accelerated cubic Newton O(1/k³), overtaken by O(1/k^{7/2}) (Monteiro–Svaiter 2013).
  - The optimal tensor scheme he "failed to develop", delivered by others (2022).
  - The universal-barrier constant, sharpened in 2014 and 2021.
  - The coordinate-descent complexity constant and the regularization device (Richtárik–Takáč).
- **A prediction overtaken.** "Any additional logarithmic factors … will definitely kill its tiny superiority." The log factor was removed in 2022. Whether the superiority is "tiny" in practice is still open; the one test read favours Newton.
- **A claim not supported by later peers.** "Third-order methods become implementable and very fast": still "generally theoretical" per Cartis et al. 2024/2026.
- **Self-qualification by his own group.** Fast methods "necessarily suffer from accumulation of errors" (2011/2014).
- **The epidemic excursion.** A confident short-term statement matched July 2020 data. The broader "success story" did not hold, and the line was abandoned after two DPs (03 §4).
- **Not found**: retractions, errata to solo papers (two corrections to joint papers exist, contents not read; 03 §2.4), rejected papers, published comment-and-reply exchanges, failed replications.

---

## 10. Era and resource context of the criticized practices

- **1983 method** (Soviet CEMI, no published numerics, limited contact with the West): criticism of intuition came 30 years later from an ML/TCS community that needed to *extend* the method. The Jackson (IMU) write-up ties its 1980s neglect to both the Cold War and the problems of the time.
- **1988–1994 IPM theory** (two-person Moscow collaboration): its worst-case character was criticized once commercial long-step primal–dual codes existed. Part of the fix was his own work in the 1990s at CORE.
- **2006 cubic regularization** (two senior theorists, no code): CGT, a three-person numerical-analysis group with CUTEr, Matlab and GALAHAD, turned it into ARC within two years. The critique reflects a difference in resources and aims more than an error.
- **2010 coordinate descent** (single PC; see 02 era notes): its cost criticism was answered by theoretical CS (Lee–Sidford) and by his own 2017 joint paper.
- **2018–2021 tensor methods** (solo DP, ERC-funded, no experiments): practical testing took until 2020–2026 (Birgin et al.; Cartis et al., a five-person team with a MATLAB package).
- **2020 COVID papers**: solo, with no epidemiology collaborator. By his own words in DP 2020/25 (03 §4), without "enough information and human resources".

---

## 11. What this means for a solver team (for the skill author) [inferred]

1. **Use him for rate-and-structure ideas, then run the solver-builder's checklist.** Ask: what does the step cost per iteration? Which constants must the user know? What happens with inexact oracles or noisy gradients? Is the subproblem nonconvex? Every critique above is one of these four.
2. **Add a monotone safeguard and adaptive restart to any momentum or acceleration idea.** Ripples, µ sensitivity and error accumulation are documented by his own group and others (§1.2–1.3).
3. **Do not port self-concordance arguments into a nonconvex NLP interior-point code unchanged.** Merit or filter globalization, inertia control and superlinear barrier updates are what that code needs (Nemirovski–Todd p. 228). Self-concordance helps in convex sub-blocks: conic pieces, barrier subproblems, logistic-type losses with Bach's modification.
4. **For higher-order or regularized Newton ideas, measure wall-clock time and linear-algebra cost, not only evaluations.** Even the best 2022–2026 evidence is evaluation-count based or loses to Newton (§3.2).
5. **Tune constants with performance estimation (PEP) where fixed-step first-order components exist** (§1.4). "Optimal" in his sense leaves constant factors on the table.
6. **Expect the persona to discount nonconvex practice** (§6). The roundtable should pair him with a trust-region or SQP member on nonconvex questions.

---

## Contradictions (kept, not reconciled)

1. **Global subproblem: "acceptable" vs "prohibitive."** Nesterov–Polyak (as CGT summarize): the cubic model's global minimizer can be computed acceptably from the complexity viewpoint. CGT: exact global minimization is "prohibitively expensive … (highly) inefficient" for large-scale practice.
2. **Log factors and practical value.** 2019/21: an optimal method with log factors would lose its "tiny superiority". 2022: optimal methods without log factors exist. Yet on logistic regression the optimal method "under-performs Newton's method" (Carmon et al.). The first half of his judgement was overtaken and the second half is supported.
3. **"Implementable."** His 2021 abstract and his collaborators (Kamzolov et al.) say high-order convex methods are implementable (convex subproblem, polynomial time). Cartis et al. (2024/2026) say they "have remained generally theoretical when p ≥ 3".
4. **Inexact gradients.** Devolder–Glineur–Nesterov: fast methods "necessarily suffer from accumulation of errors". d'Aspremont (2005/2008): optimal complexity "is preserved" with small uniformly bounded gradient errors. The error models differ, so both stand.
5. **Explanation of acceleration.** Nesterov treats the proof as the explanation. The critics say the proof explains nothing (the "algebraic trick", "mystery"). Five rival explanations each claim to demystify it. d'Aspremont–Scieur–Taylor declare the mystery solved by PEP; Bottou–Curtis–Nocedal (2018) say no explanation is widely accepted.
6. **Complexity as a guide.** Nesterov: complexity analysis selects the promising methods. CGT: the less complexity-driven variant did better, and the reason is unclear. Nemirovski–Todd, his co-author: the worst-case orientation is a "severe shortcoming" in practice, yet the same theory "explained the nature of existing interior-point methods" (p. 195).
7. **Accelerated coordinate descent cost.** Nesterov (2010): "rather high" per-iteration cost. Lee–Sidford (2013): no asymptotic overhead with a mild oracle assumption. Wright (2015): higher cost "detracts", yet efficient for some structures. Nesterov–Stich (2017): "perfectly balanced" in many situations. Four positions, depending on structure.
8. **Nonconvexity.** In 2023 he calls it an unfinished model ("So what's the point?"). His own cubic-regularization work covers nonconvex functions (02, Contradiction 3). Rivals solve structured nonconvex problems globally.
9. **Sweden, 2020.** July: decreasing, a "success story". Autumn: confirmed weekly cases rose about 38-fold from their late-August low by late December (OWID). The paper itself warns about "the wrong choice of the stopping moment".

## Gaps

- **Ye's 1994 SIAM Review of the IPM book**, DOI 10.1137/1036175: 403 from SIAM. A team member's contemporary judgement, unread.
- **Curtis–Robinson–Samadi TRACE** (*Math. Program.* 162, 2017) and **Van Scoy et al.** (*IEEE L-CSS* 2, 2018): title and DOI only. Semantic Scholar gave no abstract and was then rate-limited.
- **Beck–Teboulle FISTA (2009) versus Nesterov's composite method (2007/2013)**: FISTA became the standard in practice. I found no legitimate open copy to check what Beck and Teboulle say about his scheme. **Not read.**
- **Chambolle–Pock (2011) comparison with Nesterov's smoothing**: the HAL copy returned an HTML page. **Not read.**
- **Nesterov's replies**: I found none to the intuition critique, to PEP, to Richtárik–Takáč's "unknown scaling factor", to Monteiro–Svaiter beyond calling it an "attempt", to Griewank's priority, or to the nonconvex-landscape school. His books' prefaces (2004, 2018) and his talks (YouTube bot check, 02 Gaps) might contain them. **Not read.**
- **Correction notices** for Ahookhosh–Nesterov (2024) and Nesterov–Shikhman (2018): contents unknown (03 §2.4).
- **Critiques in Russian** of the 1983 paper or of the CEMI-era IPM work: not searched (WebSearch budget).
- **OpenReview, blogs, social media**: OpenReview is blocked by a bot check (03). The one blog lead (Bubeck's 2015 "revisiting Nesterov's acceleration") surfaced in search results and was **not read**. Ben Recht's or Moritz Hardt's blog critiques were not found.
- **Citations of the COVID papers**: the Semantic Scholar citations endpoint returned 429 and the OpenAlex lookup failed. Whether anyone published a critique is unknown.
- **Nesterov's later inexact proximal-point papers** (*SIAM J. Optim.* 31, 2021, DOI 10.1137/20M134705X; *Math. Program.* 197, 2023, DOI 10.1007/s10107-021-01727-x): **titles only**. Whether they respond to Monteiro–Svaiter could not be checked.

## Sources

Nesterov's own or co-authored texts (P):
1. Yu. Nesterov, "Implementable tensor methods in unconstrained convex optimization", *Math. Program.* 186 (2021) 157–183, DOI 10.1007/s10107-019-01449-1; PMC7875858 (§1, §6, reference list read). P
2. Yu. Nesterov, "Efficiency of coordinate descent methods on huge-scale optimization problems", CORE DP 2010/2 (pp. 2, 17 read); *SIAM J. Optim.* 22 (2012) 341–362, DOI 10.1137/100802001. P
3. Yu. Nesterov, S. U. Stich, "Efficiency of the accelerated coordinate descent method on structured optimization problems", *SIAM J. Optim.* 27(1) (2017) 110–123, DOI 10.1137/16M1060182 (abstract, Crossref). P
4. O. Devolder, F. Glineur, Yu. Nesterov, "First-order methods of smooth convex optimization with inexact oracle", CORE DP 2011/2 (abstract, https://ideas.repec.org/p/cor/louvco/2011002.html); *Math. Program.* 146 (2014) 37–75, DOI 10.1007/s10107-013-0677-5. P (joint)
5. Yu. Nesterov, "Excessive gap technique in nonsmooth convex minimization", *SIAM J. Optim.* 16(1) (2005) 235–249, DOI 10.1137/S1052623403422285 (abstract). P
6. Yu. Nesterov, "Online analysis of epidemics with variable infection rate", CORE DP 2020/25, arXiv 2007.11429v2 (abstract, §3.11, conclusions read); DP 2020/22 "Online prediction of COVID19 dynamics. Belgian case study" (abstract, https://ideas.repec.org/p/cor/louvco/2020022.html). P
7. N. Doikov, Yu. Nesterov, "Convex optimization based on global lower second-order models", NeurIPS 2020; reviews, meta-review, author feedback: https://proceedings.neurips.cc/paper_files/paper/2020/hash/c0c3a9fb8385d8e03a46adadde9af3bf-Abstract.html (local copies from agent 03, read). Paper and feedback P; reviews S.
8. L. Bogolubsky et al. (incl. Nesterov), "Learning Supervised PageRank with Gradient-Based and Gradient-Free Optimization Methods", NIPS 2016; reviews: https://proceedings.neurips.cc/paper_files/paper/2016/hash/1f34004ebcb05f9acda6016d5cc52d5e-Abstract.html (local copy read). Reviews S.
9. R. Weldon, NCCR Automation interview with Nesterov, 15 Aug 2023, https://nccr-automation.ch/news/2023/unprecedented-overflow-why-progress-his-field-alarms-yurii-nesterov (quotes re-checked). P quotes in an S article.
10. Yu. Nesterov, "Inexact high-order proximal-point methods with auxiliary search procedure", *SIAM J. Optim.* 31 (2021) 2807–2828, DOI 10.1137/20M134705X; and "Inexact accelerated high-order proximal-point methods", *Math. Program.* 197 (2023) 1–26, DOI 10.1007/s10107-021-01727-x. **Titles only.** P
11. Yu. Nesterov, B. Polyak, "Cubic regularization of Newton method and its global performance", *Math. Program.* 108 (2006) 177–205, DOI 10.1007/s10107-006-0706-8. **Not read**; known here through CGT's summary. P

Critiques, rival methods and assessments (S):
12. Z. Allen-Zhu, L. Orecchia, "Linear Coupling: An Ultimate Unification of Gradient and Mirror Descent", arXiv 1407.1537v5 (pp. 4–7 read); ITCS 2017, LIPIcs 67:3, DOI 10.4230/LIPIcs.ITCS.2017.3 (DataCite). S
13. W. Su, S. Boyd, E. J. Candès, "A Differential Equation for Modeling Nesterov's Accelerated Gradient Method: Theory and Insights", arXiv 1503.01243v2 (pp. 1–3 read); *JMLR* 17(153) (2016) 1–43. S
14. S. Bubeck, Y. T. Lee, M. Singh, "A geometric alternative to Nesterov's accelerated gradient descent", arXiv 1506.08187 (pp. 1–2 read). S
15. A. Wibisono, A. C. Wilson, M. I. Jordan, "A variational perspective on accelerated methods in optimization", *PNAS* 113(47) (2016), DOI 10.1073/pnas.1614734113 (significance statement, abstract). S
16. A. d'Aspremont, D. Scieur, A. Taylor, "Acceleration Methods", *Found. Trends Optim.* 5(1–2) (2021) 1–245, DOI 10.1561/2400000036; arXiv 2101.09545v4 (pp. 2–3 read). Found via WebSearch 1. S
17. L. Bottou, F. E. Curtis, J. Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Review* 60(2) (2018) 223–311, DOI 10.1137/16M1080173; arXiv 1606.04838v3 (§7.2, p. 70 read). S
18. B. O'Donoghue, E. Candès, "Adaptive Restart for Accelerated Gradient Schemes", *Found. Comput. Math.* 15(3) (2015) 715–732, DOI 10.1007/s10208-013-9150-3; arXiv 1204.3982v1 (pp. 1–6 read). S
19. L. Lessard, B. Recht, A. Packard, "Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints", *SIAM J. Optim.* 26(1) (2016) 57–95, DOI 10.1137/15M1009597; arXiv 1408.3595v7 (pp. 2, 21 read). S
20. A. d'Aspremont, "Smooth Optimization with Approximate Gradient", *SIAM J. Optim.* 19 (2008) 1171–1183, DOI 10.1137/060676386; arXiv math/0512344 (abstract). S
21. R. Kidambi, P. Netrapalli, P. Jain, S. Kakade, "On the Insufficiency of Existing Momentum Schemes for Stochastic Optimization", ITA 2018, DOI 10.1109/ITA.2018.8503173; arXiv 1803.05591 (abstract). S
22. Y. Drori, M. Teboulle, "Performance of first-order methods for smooth convex minimization: a novel approach", *Math. Program.* 145 (2014) 451–482, DOI 10.1007/s10107-013-0653-0; arXiv 1206.3209 (abstract). S
23. D. Kim, J. A. Fessler, "Optimized first-order methods for smooth convex minimization", *Math. Program.* 159 (2016) 81–107, DOI 10.1007/s10107-015-0949-3; arXiv 1406.5468 (abstract). S
24. Y. Drori, "The exact information-based complexity of smooth convex minimization", *J. Complexity* 39 (2017) 1–16, DOI 10.1016/j.jco.2016.11.001; arXiv 1606.01424 (abstract). S
25. A. B. Taylor, J. M. Hendrickx, F. Glineur, "Smooth strongly convex interpolation and exact worst-case performance of first-order methods", *Math. Program.* 161 (2017) 307–345, DOI 10.1007/s10107-016-1009-3; arXiv 1502.05666 (abstract). S
26. A. Taylor, Y. Drori, "An optimal gradient method for smooth strongly convex minimization", *Math. Program.* 199 (2023) 557–594, DOI 10.1007/s10107-022-01839-y; arXiv 2101.09741 (abstract). S
27. B. Van Scoy, R. A. Freeman, K. M. Lynch, "The Fastest Known Globally Convergent First-Order Method for Minimizing Strongly Convex Functions", *IEEE Control Syst. Lett.* 2(1) (2018) 49–54, DOI 10.1109/LCSYS.2017.2722406. **Title only.** S
28. A. S. Nemirovski, M. J. Todd, "Interior-point methods for optimization", *Acta Numerica* 17 (2008) 191–234, DOI 10.1017/S0962492906370018; author copy https://www2.isye.gatech.edu/~nemirovs/Published.pdf (pp. 191–195, 202, 207–208, 222, 228–230 read). S (co-author insider)
29. F. Bach, "Self-concordant analysis for logistic regression", *Electron. J. Statist.* 4 (2010), DOI 10.1214/09-EJS521; arXiv 0910.4627v1 (pp. 4–5 read). S
30. T. Sun, Q. Tran-Dinh, "Generalized self-concordant functions: a recipe for Newton-type methods", *Math. Program.* 178 (2019) 145–213, DOI 10.1007/s10107-018-1282-4; arXiv 1703.04599v3 (pp. 2–3 read). S
31. S. Bubeck, R. Eldan, "The entropic barrier: a simple and optimal universal self-concordant barrier", arXiv 1412.1587 (abstract). S
32. Y. T. Lee, M.-C. Yue, "Universal Barrier Is n-Self-Concordant", *Math. Oper. Res.* 46 (2021) 1129–1148, DOI 10.1287/moor.2020.1113; arXiv 1809.03011 (abstract). S
33. Y. Ye, review of *Interior-Point Polynomial Algorithms in Convex Programming*, *SIAM Review* 36(4) (1994) 682–683, DOI 10.1137/1036175. **Not read (403).** S
34. C. Cartis, N. I. M. Gould, Ph. L. Toint, "Adaptive cubic regularisation methods for unconstrained optimization. Part I", *Math. Program.* 127 (2011) 245–295, DOI 10.1007/s10107-009-0286-5; preprint https://pure.unamur.be/ws/files/1332672/cgt31RR_I.pdf (pp. 1–3, 13, 33–34 read). S
35. F. E. Curtis, D. P. Robinson, M. Samadi, "A trust region algorithm with a worst-case iteration complexity of O(ε^{−3/2}) for nonconvex optimization", *Math. Program.* 162 (2017) 1–32, DOI 10.1007/s10107-016-1026-2. **Title only.** S
36. Y. Carmon, J. C. Duchi, "Gradient Descent Finds the Cubic-Regularized Nonconvex Newton Step", *SIAM J. Optim.* 29 (2019) 2146–2178, DOI 10.1137/17M1113898; arXiv 1612.00547 (abstract). S
37. R. D. C. Monteiro, B. F. Svaiter, "An Accelerated Hybrid Proximal Extragradient Method for Convex Optimization and Its Implications to Second-Order Methods", *SIAM J. Optim.* 23(2) (2013) 1092–1125, DOI 10.1137/110833786 (abstract via Crossref). S
38. Y. Arjevani, O. Shamir, R. Shiff, "Oracle complexity of second-order methods for smooth convex optimization", *Math. Program.* 178 (2019) 327–360, DOI 10.1007/s10107-018-1293-1; arXiv 1705.07260 (abstract). S
39. B. Jiang, H. Wang, S. Zhang, "An Optimal High-Order Tensor Method for Convex Optimization", arXiv 1812.06557 (abstract). Found via WebSearch 2. S
40. D. Kovalev, A. Gasnikov, "The First Optimal Acceleration of High-Order Methods in Smooth Convex Optimization", arXiv 2205.09647 (abstract). S
41. Y. Carmon, D. Hausler, A. Jambulapati, Y. Jin, A. Sidford, "Optimal and Adaptive Monteiro-Svaiter Acceleration", arXiv 2205.15371 (abstract). S
42. D. Kamzolov, A. Gasnikov, P. Dvurechensky, A. Agafonov, M. Takáč, "Exploiting higher-order derivatives in convex optimization methods", arXiv 2208.13190 (abstract). Found via WebSearch 2. S
43. C. Cartis, R. Hauser, Y. Liu, K. Welzel, W. Zhu, "Efficient Implementation of Third-order Tensor Methods with Adaptive Regularization for Unconstrained Optimization", *Math. Program. Comput.* 18(3) (2026) 877–948, DOI 10.1007/s12532-026-00313-6; arXiv 2501.00404v3 (abstract, pp. 5–6 read). Found via WebSearch 2. S
44. P. Richtárik, M. Takáč, "Iteration complexity of randomized block-coordinate descent methods for minimizing a composite function", *Math. Program.* 144 (2014) 1–38, DOI 10.1007/s10107-012-0614-z; arXiv 1107.2848 (abstract). S
45. Y. T. Lee, A. Sidford, "Efficient Accelerated Coordinate Descent Methods and Faster Algorithms for Solving Linear Systems", FOCS 2013, 147–156, DOI 10.1109/FOCS.2013.24; arXiv 1305.1922v1 (pp. 3, 8, 12 read). S
46. S. J. Wright, "Coordinate descent algorithms", *Math. Program.* 151 (2015) 3–34, DOI 10.1007/s10107-015-0892-3; arXiv 1502.04759v1 (pp. 16–18 read). S
47. Q. Tran-Dinh, "Adaptive smoothing algorithms for nonsmooth composite convex minimization", *Comput. Optim. Appl.* 66 (2017) 425–451, DOI 10.1007/s10589-016-9873-6; arXiv 1509.00106 (abstract). S
48. A. Nemirovski, "Prox-Method with Rate of Convergence O(1/t) …", *SIAM J. Optim.* 15(1) (2004) 229–251, DOI 10.1137/S1052623403425629 (abstract via Crossref). S
49. A. d'Aspremont, J. Peña, K. Scheinberg (discussion column) and d'Aspremont, "Smooth Semidefinite Optimization"; Peña, "Nash equilibria computation via smoothing techniques", *Optima* 78 (Nov 2008) pp. 9–12; archived https://web.archive.org/web/20231203022724/https://www.mathopt.org/Optima-Issues/optima78.pdf (read). S
50. J. Sun, Q. Qu, J. Wright, "When Are Nonconvex Problems Not Scary?", arXiv 1510.06096 (abstract). S
51. zbMATH Open reviews: M. A. Hanson (1994 book), M. I. Todorov (2004 book), M. Anholcer (2018 book), J. Thierfelder (2013 composite paper), from the author profile https://zbmath.org/authors/nesterov.yurii (read). S
52. A. Jackson, "2026 Gauss Prize: Yurii Nesterov", IMU prize write-up (read, local copy from this run). S

Data:
- Our World in Data, "Weekly confirmed COVID-19 cases", https://ourworldindata.org/grapher/weekly-covid-cases.csv (downloaded 2026-09-28; Sweden rows June 2020 – January 2021 read). Data source for an [inferred] comparison.
