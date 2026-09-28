# 03 · Process evidence: what Yurii Nesterov actually does

| Field | Value |
|---|---|
| Researcher | Yurii E. Nesterov (CORE / INMA, UCLouvain; emeritus. Also Corvinus Budapest and CUHK-Shenzhen according to his 2024–2026 arXiv affiliation lines) |
| Dimension | Research agent 03 of 06: process evidence. Covers experiment sections, test problems and baselines, code, early versus final versions, review timelines, corrections, rebuttals, and abandoned work |
| Research date | 2026-09-28 |
| Sources consulted | 39 (31 primary, 8 secondary), listed under "Sources". 4 more were blocked: OpenReview (bot check, API challenge), the GitHub REST API (not enabled for this session; `git clone` of public repos worked), the Wayback Machine (connection reset), and the old Optima PDF URLs (404; the text was read from this run's scratch copy) |
| WebSearch calls | 1 of the 2 allowed (OpenReview lookup; no useful result) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` hold only `.gitkeep`. `private/` was not opened |
| Transcripts saved | none (no talk transcripts were found or produced in this pass) |
| Language | English (per team.json) |

**Tags.**
- **[stated]**: Nesterov wrote or said it, in a paper's prose, a rebuttal he co-signed, an essay or an interview.
- **[practice]**: what the artifacts show was done: tables, test generators, hardware lines, reference lists, arXiv version histories, Crossref dates, git logs.
- **[observed]**: recorded by a third party: reviewers, colleagues, the IMU write-up.
- **[inferred]**: my reading. The basis is always given. Do not quote it as his view.
- **(P)** marks a primary source and **(S)** a secondary one.

**Co-authorship caveat.**
- A joint paper shows the practice of the group, not of Nesterov alone.
- Author order with students is mostly alphabetical (see 01 §2.1), so it does not identify who did what.
- Where a git history or a README names the person who wrote the code, I say so.
- I did not find a statement of the division of labour in any joint paper.

**What was read in full text.**

*Nesterov's solo papers:*
- Three CORE Discussion Papers: 2010/2 (coordinate descent), 2012/2 (huge-scale subgradient) and 2013/26 (universal gradient methods). Another agent of this run had fetched these to the shared scratch folder.
- The *Math. Program.* 2021 tensor paper (open access, PMC).
- Eight solo arXiv papers from 2020–2026: 2007.11429 (v1 and v2), 2201.04852, 2311.13838, 2311.15154 (v1 and v2), 2412.14934, 2503.10155, 2509.20902 and 2603.21500 (v1 and v2).

*Joint papers:*
- Nesterov & Florea 2105.09241 and Rodomanov & Nesterov 2002.00657v2.
- Doikov, Mishchenko & Nesterov 2208.05888.
- The NeurIPS 2020 Doikov–Nesterov paper, with its supplement, six reviews, the meta-review and the author feedback, plus arXiv 2006.08518v2.
- The NIPS 2016 reviews of the Bogolubsky et al. PageRank paper.
- The Ahookhosh–Nesterov *Math. Program.* 2024 paper (open access, PMC).

*Essays and records:*
- Nesterov's two Optima pieces (2008, 2012).
- The introduction and table of contents of his 2013 Russian dissertation (hosted by dissercat).
- Two student code repositories (git clone) and one Zenodo code package.

*Paywalled:* no journal version of a solo paper other than the tensor paper was readable.

---

## 1. Experiments and execution (framework layer 4). This is the core of the file

### 1.1 Where his solo numerics appear, and what they contain [practice, P]

The table lists every solo optimization paper I read in full, in order. The epidemic model is listed separately in §4.

| Paper (identifier) | Numerics? | Test problems | Baselines actually run | Hardware / software line | Framing word |
|---|---|---|---|---|---|
| "Efficiency of coordinate descent methods on huge-scale optimization problems", CORE DP 2010/2 → *SIAM J. Optim.* 22(2) 2012, DOI 10.1137/100802001 | yes, §6.3 | One self-generated family, the "Google problem": a random graph with average node degree p, n = 65,536 to 1,048,576. Stopping rule ‖Ēx − x‖ ≤ 0.01‖x‖ | **None.** RCDM is the only method run. It is compared with ACDM and the fast gradient method only through a complexity table, (6.9), and an operation count: "For our computer, this amount of computations takes at least 20 minutes." | "The computations were performed on a standard Pentium-4 computer with frequency 1.6GHz." | "preliminary computational results" (§1) |
| "Subgradient methods for huge-scale optimization problems", CORE DP 2012/2 → *Math. Program.* 146 (2014), DOI 10.1007/s10107-013-0686-4 | yes, §7 | The same random Google problem, recast as a nonsmooth max-type problem. N up to 1,048,576, p = 8 to 32 | The same method with a different implementation: sparse updates (SUSM) versus standard sparse matrix-vector products (SM). "Recall that the both schemes implement the same minimization method (4.3). The only difference between them consists in the way of computing/updating the matrix-vector products." Plain subgradient and smoothing are compared by operation counts only. Extrapolation instead of running: "From the table (7.8) we can guess that for the same number of iterations, the usual subgradient method would require almost a year of computations." | "Our experiments were performed on a standard PC with 2.6GHz processor and 4Gb of RAM." He explains a timing anomaly by the platform: "The later effect can be explained by the troubles with keeping massive computations in the fast memory of Windows system." | "promising results of preliminary computational experiments" (abstract) |
| "Universal gradient methods for convex optimization problems", CORE DP 2013/26 → *Math. Program.* 152 (2015), DOI 10.1007/s10107-014-0790-0 | yes, §5 | Three random families: (1) matrix games with entries uniform in [−1, 1], n = 896, m = 128, and 512 × 512; (2) a continuous Steiner problem, n = 256, m = 512, with centres "generated randomly in the box"; (3) the universal method against his own 2005 smoothing | **Only his own methods**: PGM, FGM, entropy versus Euclidean setup, weighted dual averaging (his 2009 paper), smoothing (his 2005 paper). Runs are cut off with "out of time" | none stated | "encouraging numerical experiments" (abstract) |
| "Implementable tensor methods in unconstrained convex optimization", CORE DP 2018/05 → *Math. Program.* 186 (2021) 157–183, DOI 10.1007/s10107-019-01449-1 | **no** | none | none. Practicality is argued by an operation count per iteration: "This is the same order of complexity as that of one iteration in Trust Region Methods [15] and usual Cubic Regularization [27, 31]. However, we can expect that the third-order methods converge much faster." Implementation is delegated: "we just mention that the Galahad Optimization Library [16] has special subroutines for solving the auxiliary problems in the form (5.10)." | none | abstract: "implementable and very fast" |
| "Quartic Regularity", arXiv 2201.04852 → *Vietnam J. Math.* 53 (2025) 553–575, DOI 10.1007/s10013-024-00720-z | no | none | none | none | none |
| "Primal subgradient methods with predefined stepsizes", arXiv 2311.13838 → *JOTA* (2024), DOI 10.1007/s10957-024-02456-9 | no | none | none | none | none |
| "High-Order Reduced-Gradient Methods for Composite Variational Inequalities", arXiv 2311.15154 | no | none | none | none | none |
| "Local and Global Convergence of Greedy Parabolic Target-Following Methods for Linear Programming", arXiv 2412.14934 | yes, §8 | "For our computational experiments, we use a simple random generator proposed in [6]." [6] is the Budapest group's joint paper. The generator builds a strictly feasible primal–dual pair first, then A with entries uniform in (−1, 1), b = Ax̂ and c = ŝ. 32 ≤ m ≤ n/2, 64 ≤ n ≤ 1024. "Our results correspond to the series of random test problems of length one hundred." | His own earlier first-order-prediction schemes, (2.14) and (5.1). Their results are not displayed ("very similar to the results of method (2.14), presented in [6]"). No external LP code is run | none | "In our opinion, these results are very promising." |
| "Asymmetric Long-Step Primal-Dual Interior-Point Methods with Dual Centering", arXiv 2503.10155 | yes, §9 | Random low-rank quadratic-interpolation SDO problems, "several series of one hundred random problems", data uniform in [−1, 2], ε = 10⁻⁸ | **None.** The comparison is handed to others: "It will be interesting to compare our computational results with performance of other efficient optimization schemes (e.g. [6, 27])." He then writes out a reformulation "suitable for solving by the other first- and second-order methods". [6] and [27] are the Li–Sun–Toh and Zhao–Sun–Toh augmented-Lagrangian solvers | "We performed our experiments at the usual notebook. Nevertheless, the largest problem in our test set was solved in less than fifty seconds." Linear algebra: "we used the standard Cholesky factorization." | "preliminary but encouraging numerical results" (abstract) |
| "Universal Complexity Bounds for Universal Gradient Methods in Nonlinear Optimization", arXiv 2509.20902 | no | none | none | none | none |
| "Theorem of Alternative for Extended Homogeneous Linear System and its Application in Conic Optimization", arXiv 2603.21500 | no | none | none | none | none |

**Pattern 1: numerics are optional, and only a minority of solo papers have them.** [practice, P; count from the table]
- 5 of the 11 solo optimization papers read in full have a numerical section.
- 0 of the 11 compare against a method, code or solver written by someone else.
- When a comparison with others' methods matters, he does it on paper: complexity tables (DP 2010/2 (6.9)), operation-count extrapolations ("at least 20 minutes", "almost a year of computations"), or per-iteration cost equivalences (tensor §5).
- This fits the reviews of his earlier flagship works: the 1994 IPM book, with "numerical results are omitted" (zbMATH review, quoted in 01), and the 2006 cubic-regularization paper. Of the latter, Cartis–Gould–Toint wrote: "Global convergence to second-order critical points and asymptotically quadratic rate of convergence were also proved for this method, but no numerical results were provided." (ARC Part I preprint, p. 2) [observed, S].
- His 2013 dissertation lists "Вычислительные эксперименты" (computational experiments) sections in only two chapters: §2.3.6, composite, and §5.1.5, smoothing. The cubic-regularization chapter has "Вычислительные детали" (computational details, §4.1.5) instead [practice, P; table of contents only].

**Pattern 2: the experiment tests the rate, not competitiveness.** [practice, P]
- The universal DP states the purpose: "In our numerical experiments we tried to check the actual level of adaptivity of the above methods to the local topological structure of the objective function." (§5, p. 14).
- The tables list the required accuracy ε = 2⁻⁵ … 2⁻¹³ against iterations. He reads the empirical complexity exponent off the table. FGM on the Steiner problem: "Increase of the accuracy in four times results in doubling the number of iterations. From the complexity point of view, this corresponds to the level O(1/ε^{1/2})". The Euclidean setup "just corresponds to the worst-case theoretical bound".
- Next to each iterate count he reports the method's own accuracy certificate and its current Lipschitz estimate.
- The 2024 LP paper goes one step further. It fits an empirical iteration model, k ≈ ¼(25 + log₂ m · log₂(n/16)) (eq. 8.2), and reports its error: "In our experiments, the standard deviation of this forecast is 0.46 iterations."
- [inferred] For him the experiment checks whether the proven rate, or a better one, shows up on typical instances. It is not a benchmark against the state of the art.

**Pattern 3: random instances with a known answer.** [practice, P]
- **2013 universal DP.** Matrix games with optimal value zero. Footnote 2: "Since in this problem the optimal value is known, we use it in the stopping criterion."
- **2012 subgradient DP.** The Google problem is recast so that g* = 0 and X* is a cone.
- **2021 memory paper** (Nesterov & Florea, *Optim. Methods Softw.* 37 (2022) 936–953, DOI 10.1080/10556788.2020.1858831; arXiv 2105.09241). A log-sum-exp is shifted by its own gradient at 0: "Clearly, in this case we have ∇f(0) = 0, so the unique solution of our test problem (41) is x∗ = 0." (§5, p. 15).
- **2021 greedy quasi-Newton paper** (Rodomanov & Nesterov, *SIAM J. Optim.* 31 (2021) 785–811, DOI 10.1137/20m1320651; arXiv 2002.00657v2 §5.1). The same shifted log-sum-exp construction, "so the unique minimizer of our test function (5.1) is x∗ = 0". Here the starting point is placed on the sphere of radius 1/n around the minimizer, "motivated by (4.27)", so the local theory is what gets tested.
- **2024 LP paper.** The generator plants a strictly feasible primal–dual pair.
- [inferred] The same generator in two papers with two different junior co-authors (2020, 2021) suggests a house test problem that he carries into collaborations. Who wrote the generator code is not documented.

**Pattern 4: hard test functions built from lower-bound constructions.** [observed + practice]
- Gürbüzbalaban & Overton (preprint 24 Jan 2011; *Nonlinear Anal.* 75 (2012), DOI 10.1016/j.na.2011.07.062) [observed, S]:
  - "In 2008, Nesterov [Nes08] introduced the following smooth (differentiable, in fact polynomial) function on Rn:"
  - with the reference "[Nes08] Y. Nesterov, 2008. Private communication."
  - They call it "a challenging test problem for optimization methods" and analyse his two nonsmooth variants as well.
- The smooth variant also received a paper by Jarre ("On Nesterov's smooth Chebyshev–Rosenbrock function", *Optim. Methods Softw.* 2013, DOI 10.1080/10556788.2011.638924). A complexity note by Cartis, Gould & Toint "resolves the apparent contradiction" between Jarre's bound and known worst-case results (*Optim. Methods Softw.* 2013, DOI 10.1080/10556788.2012.722632; Optimization Online 2011/07/3101 abstract) [observed, S].
- So Nesterov handed out hard instances informally and did not publish them himself [practice, as recorded by others].
- In the student-led super-universal paper (Doikov, Mishchenko, Nesterov, *SIAM J. Optim.* 34 (2024) 27–56, DOI 10.1137/22m1519444; arXiv 2208.05888 §7), one experiment is "Worst Instances". Its objective's structure "is very similar to the worst-case function from lower bounds for high-order methods [35]", where [35] is Nesterov's 2021 tensor paper [practice, P].

**Pattern 5: an implementation ablation instead of an external baseline.** [practice, P] In DP 2012/2 the only measured comparison isolates one design choice, sparse updating versus standard matrix-vector products, inside the same algorithm (tables 7.7–7.8). That is a clean ablation: one variable changes.

**Pattern 6: adaptive constants by doubling, with the constant set by hand.** [practice, P]
- 2010 DP §6.1: the random adaptive coordinate method doubles L̂ᵢ while the sign test fails and halves it after the step. The backtracking is designed so that it "should not be based on computation of the function values".
- 2012 DP §4: "we multiply the bounds by η > 1 and restart the method from scratch … For numerical experiments, we usually take η = 2."
- The tensor paper gives a diagnostic rule in place of a theorem: "if we see that this process is too slow, this means that our estimate is too small" (§6) [stated, P].
- 2025 SDO paper: fixed parameters (β = 0.2, A = 2, ε = 10⁻⁸, y₀ = 0) and "the rudimentary Damped Newton Method" as corrector: "Its improvement is an interesting topic for further research."

**Pattern 7: statistics come late.** [practice, P]
- In 2010–2013 each setting is reported for a single generated instance. The texts speak of "a randomly generated graph" and "our problem instance". No repetitions or dispersion are reported.
- In 2024–2025 (the LP and SDO papers, both written while he worked with the Budapest IPM group, whose generator [6] he uses) each cell is a mean over 100 instances with a relative standard deviation.
- [inferred] The later habit may come from the collaborators' testing protocol. The LP paper says: "As in numerical testing of [6], in all our experiments, each predictor step is followed by a single corrector step". This is not otherwise verified.

### 1.2 Joint and student-led papers: what changes when a student is involved [practice, P]

| Paper | Data / test problems | Baselines | Code |
|---|---|---|---|
| Doikov & Nesterov, "Convex optimization based on global lower second-order models", NeurIPS 2020 (proceedings page and DBLP conf/nips/DoikovN20; arXiv 2006.08518) | Public LIBSVM datasets: w8a, covtype, a9a, connect-4, mnist. Logistic regression with an ℓ2-ball constraint | Frank–Wolfe, gradient method and fast gradient method with line search; SGD and SVRG "with constant step-size, tuned for each problem" | "All methods were implemented in C++. The source code can be found at https://github.com/doikov/contracting-newton/". Clock time on "Intel Core i5 CPU, 1.6GHz; 8 GB RAM". Git log: every commit is by "Nikita" / "Nikita Doikov", 20–28 Oct 2020, i.e. after the review. Python drivers, C++ core, vendored Eigen |
| Rodomanov & Nesterov, SIOPT 2021 (above) | Shifted log-sum-exp (known x* = 0) and logistic regression | Gradient method, DFP, BFGS, SR1, plus greedy and randomized variants | no code link in the paper |
| Nesterov & Florea, OMS 2022 (above) | Shifted log-sum-exp (known x* = 0), M = 6n; n = 100, 200, 400 in Tables 3–4 | Gradient method = bundle size 1; a sweep over bundle sizes 1–256 and two replacement rules | none stated |
| Doikov, Mishchenko & Nesterov, SIOPT 2024 (above) | Polytope feasibility, soft maximum, "worst instances" | Gradient method, fast gradient method, cubic Newton with fixed or adaptive constants | github.com/doikov/super-newton. Three Jupyter notebooks plus `methods.py` and `oracles.py`. All commits by Nikita Doikov on 12 Aug 2022, the day after the arXiv posting |
| Bankmann, Mehrmann, Nesterov & Van Dooren, *Vietnam J. Math.* 48 (2020) 633–659, DOI 10.1007/s10013-020-00427-x (arXiv 1904.08202) | Passivity LMIs; publication-example notebooks | none in the scope checked | Zenodo record 2643171, "Code and examples …". Zenodo lists all four authors as creators, but `setup.py` says `author='Daniel Bankmann'` (TU Berlin). Python library, supplemented by a TU Berlin GitLab repo |
| Bogolubsky, Dvurechensky, Gasnikov, Gusev, Nesterov, Raigorodskii, Tikhonov, Zhukovskii, "Learning Supervised PageRank with Gradient-Based and Gradient-Free Optimization Methods", NIPS 2016 (proceedings page; DBLP conf/nips/BogolubskyDGGNR16) | Per the reviewers: "a web graph used in related work"; "The data sets are not publicly available" | Per Reviewer 3: compared "only" with GBP. Reviewer 2: "none of the experiment results are in the main text" | none found |

**What changes** [practice + inferred]:
- With a student in charge of the numerics, the papers use public datasets or shared notebooks, external baselines such as FW, SGD, SVRG and classical quasi-Newton, wall-clock time, and public code.
- None of this appears in his solo papers.
- The division of labour is not stated anywhere, but every code artefact found was written and committed by the junior co-author (Doikov, Bankmann).
- **No repository, code package or software release by Nesterov himself was found.** I checked the arXiv listing (57 entries, only one with a code link, the Bankmann one), student repositories and Zenodo. [practice, P; absence of evidence]

### 1.3 Honest reporting of where the new method loses [practice, P]

- **Rodomanov & Nesterov 2021** (arXiv 2002.00657v2 p. 22): "However, the classical SR1 method always remains the best. Nevertheless, the greedy methods are quite competitive." Their tables show the standard SR1 beating every greedy variant at every accuracy.
- **Universal DP 2013/26** (p. 18): "The results of PGM (2.16) are not so impressive." A diagnosis follows: "It seems that a weak point of this method is the quality of termination criterion." The Euclidean-setup FGM is shown behaving exactly at the worst-case rate.
- **NeurIPS 2020.** Reviewer 2 noted that the older Contracting Trust-Region method "works better than their novel proposal of Aggregating Newton Method". The rebuttal conceded: "We agree that the first algorithm seems to have better performance in practice. From our experience, the aggregating method is more stable though." (line numbers of the PDF removed.)
- **2024 LP paper** (p. 28): the finite-termination test does not keep up at large sizes: "For the biggest dimensions, the method almost always stops before the optimal basis could be detected by our tests."
- **Nesterov & Florea 2021**: they hedge the generality of their own result: "Maybe our preliminary conclusions are problem specific."

---

## 2. Judging results, criticism and corrections (framework layer 5)

### 2.1 How a rebuttal is handled: NeurIPS 2020, the only public review exchange found [practice, P; reviews observed, S]

- **Reviews.** Six reviews and a meta-review. Several reviews list weaknesses, but the meta-review says "all reviewers liked your paper and see a potential for the field". Reviewer 1 on the writing: "The presentation is very scholarly, there are no over-claims."
- **Rebuttal.** One page, co-signed; drafting authorship unknown. It answers each reviewer in order:
  - **Concede.** The R2 point, quoted in §1.3.
  - **Defend the assumption.** R4 had called a bounded domain "very strong". The reply: "We think, that the assumption on the boundness of the problem domain is not very strong." They argue that practical models bound variables through regularization balls or simplices. They also note that the subproblem is simpler than cubic Newton's ("no cubic terms").
  - **Answer with a proof.** R5 doubted a Hölder-type inequality. The reply writes out the Newton–Leibniz integral bound.
  - **Answer with cost accounting.** R3 asked about the advantage over first-order methods. The reply gives the per-step cost, O(n³) plus the Hessian cost O(mn²) against O(mn) for a gradient. It argues that the complexity parameter H_ν "can be much smaller than the max. eigenvalue of the Hessian".
  - **Fix typos.** "There was a typo in (23), this rate should be the same as that one in (13)." Also "A typo in the statement of Theorem 4 … This is fixed".
  - **Promise more.** On a SoftMax (log-sum-exp) application for R1: "We are happy to add our experimental results with this objective into the supplementary part." On second-order methods with line search for R6: "Indeed, it seems to be a reasonable and interesting comparison. We are happy to add more experiments into the supplementary part." On code: "The code with our implementation will be available."
- **What was delivered** [practice, P; checked by text search]:
  - **Delivered.** The code, released on GitHub on 20 Oct 2020. The missing references: Katyusha and SARAH appear in both the camera-ready and arXiv v2.
  - **Not delivered.** No SoftMax / log-sum-exp experiment and no comparison with second-order line-search methods appears in the proceedings supplement or in arXiv 2006.08518v2 (21 Dec 2020). Reviewer 3's request for averages over runs ("Figure 3 seems to display a single run of each method") was also not visibly addressed. A text search of the supplement and of arXiv v2 finds no averaged results.
  - **Later.** A "Soft Maximum" experiment does appear two years later in the super-universal paper (arXiv 2208.05888 §7, and `experiment_soft_maximum.ipynb` in the repo).
  - [inferred] Promised additions migrated to a later paper instead of being added to the accepted one.

### 2.2 Answering a pessimistic predecessor or a peer result with a changed problem class [practice, P]

- **Tensor paper (MP 2021, §1).** He cites the only prior convex analysis, Baes's unpublished preprint, as "concluded by a pessimistic comment on practical applicability of these methods". His answer is structural: re-regularize so that "an appropriately regularized Taylor approximation of convex function is a convex multivariate polynomial". Footnote 1 locates the predecessor's flaw in the parameter choice: "Thus, we cannot guarantee that this polynomial is convex." He answers criticism by changing the construction, not by running experiments.
- **Optima 88 (May 2012) discussion column, "How to Make the Gradients Small".** The column accompanies Cartis–Gould–Toint's main article in that issue (lower bound O(ε^{−3/2}) for nonconvex gradient-norm minimization). In it he did three things:
  1. He compiled the known complexity results for a target whose rate, as he put it, "is addressed very rarely".
  2. He built new regularize-and-restart schemes on the spot, marking the gap: "The lower complexity bounds for these settings are not known."
  3. He proved a resisting-oracle lower bound for a slightly changed problem class: "Let us show that a minor change in the initial conditions dramatically changes our conclusions."

  [practice, P]
- [inferred] The same theme returns later in his co-authored work on approximate stationary points (Grapiglia & Nesterov, arXiv 1907.07053). That this column seeded it is my inference.

### 2.3 Failures and limits stated in print [stated, P]

- Tensor paper, §6: "Simple comparison of the complexity bounds in Sects. 3 and 4 shows that we failed to develop an optimal tensor scheme." In the same place he argues the gap may not matter in practice: "Any additional logarithmic factors in the complexity bound of this “optimal” method will definitely kill its tiny superiority in the convergence rate." He lists "One of the difficult unsolved problems in our approach", the dynamic adjustment of the Lipschitz constant, as "clearly crucial for the practical efficiency of the high-order schemes."
- 2013 dissertation table of contents: in the accelerated-cubic-regularization chapter there is a section titled "4.2.6 Ложное ускорение" (False acceleration). **Content not read** (title only, via dissercat). [inferred] He documents a variant that looks accelerated but is not. Unverified.

### 2.4 Corrections, errata, retractions [practice, P; Crossref search on title words erratum/correction/corrigendum/retraction with author Nesterov]

| Item | Record | Content |
|---|---|---|
| Nesterov & Shikhman, "Correction to: Computation of Fisher–Gale Equilibrium by Auction", *J. Oper. Res. Soc. China* (2018) | DOI 10.1007/s40305-018-0209-3, correcting 10.1007/s40305-018-0195-5 | **not read** (paywalled) |
| Ahookhosh & Nesterov, "Correction: High-order methods beyond the classical complexity bounds: inexact high-order proximal-point methods", *Math. Program.* 208 (2024) 409–410 | DOI 10.1007/s10107-024-02067-2, first online 10 Feb 2024, correcting 10.1007/s10107-023-02041-4. The PMC copy of the corrected article says only "corrected publication 2024" and "A Correction to this paper has been published" | **not read**. The PMC text does not say what changed |

- No retraction was found.
- No erratum to a solo paper was found. The search covers only records whose titles contain those words.
- Both corrections are on co-authored papers.

---

## 3. Order of work, versions and publication behaviour (framework layers 4 and 6)

### 3.1 The discussion paper is effectively final; journal revision is light [practice, P]

| Pair compared | What changed |
|---|---|
| DP 2012/2 (Jan 2012) → *Math. Program.* 2014 (Crossref reference list) | **Identical 10-item reference list, in the same order.** The status line of ref. [5] is carried over unchanged: DP "CORE Discussion Paper 2010/2. Accepted by SIOPT." → MP "CORE iscussion paper 2010/2. Accepted by SIOPT" [sic], although the SIOPT paper had appeared in 2012 |
| DP 2010/2 (Jan 2010) → *SIAM J. Optim.* 2012 (OpenAlex abstract) | The abstract is word-for-word the DP abstract except "Surprisingly enough" → "Surprisingly". It still contains "Our numerical test confirms a high efficiency of this technique on problems of very big size." References: 8 in the DP, 10 in SIOPT (Crossref; the two additions are not identifiable from the blank Crossref entries) |
| DP 2013/26 (Apr 2013) → *Math. Program.* 2015 (Crossref) | 11 → 12 references. Added: Babonneau–Nesterov–Vial on gas networks. Updated: Lan's title, from "Level methods uniformly optimal …" (submitted) to "Bundle-level methods uniformly optimal …" (MP 2013). Body not compared (journal text not read) |
| DP 2018/05 → *Math. Program.* 2021 tensor paper | Received 29 Mar 2018, accepted 4 Nov 2019, about 19 months of review. The abstract is unchanged apart from spelling out the two relative-smoothness citations. It keeps the claim "the third-order methods become implementable and very fast" with no experiment added. Acknowledgement: "The comments of two anonymous referees were extremely useful." |

- [inferred] The idea is finished when the DP goes out. Referees change bibliographic details and, per his own acknowledgement, improve the text, but the claims, framing and numerics stay as first written.
- His 2013 dissertation describes the lag [stated, P; Russian text via dissercat]: "Большинство из них было получено в 2002-2007 годах и опубликовано ближе к концу десятилетия в ведущих оптимизационных журналах." My translation: most of these results were obtained in 2002–2007 and published towards the end of the decade in leading optimization journals.

### 3.2 Review durations (Crossref "received" → "accepted"; Springer and T&F record these from about 2018) [practice, P]

- **Solo papers:**
  - tensor, *Math. Program.*: 19 months (Mar 2018 → Nov 2019);
  - "Superfast second-order methods …", *JOTA* 2021, DOI 10.1007/s10957-021-01930-y: 14 months;
  - "Inexact accelerated high-order proximal-point methods", *Math. Program.* 2023, DOI 10.1007/s10107-021-01727-x: 15 months;
  - "Set-limited functions and polynomial-time interior-point methods", *JOTA* 2024, DOI 10.1007/s10957-023-02163-x: 10 months;
  - "Primal subgradient methods with predefined step sizes", *JOTA* 2024: 6 months;
  - "Inexact basic tensor methods …", *OMS* 2022, DOI 10.1080/10556788.2020.1854252: 5 months.
- **With students:** 5–19 months (e.g. Rodomanov, JOTA 2021: Jul → Dec 2020; Doikov, JOTA 2021: Jul 2019 → Feb 2021). The longest joint case is Ahookhosh & Nesterov at 25 months (Oct 2021 → Nov 2023).
- These dates show long revision cycles but **no rejection**. Rejections leave no trace in Crossref. **Gap.**

### 3.3 Short, self-referential bibliographies in solo papers [practice, P; Crossref reference-count]

- **Solo *Math. Program.* papers 2005–2018:** 7–20 references each:
  - smoothing 2005: 11;
  - cubic 2006, joint with Polyak: 14;
  - dual extrapolation 2007: 7;
  - accelerated cubic 2008: 8;
  - primal-dual subgradient 2009: 17;
  - composite 2013: 20;
  - huge-scale subgradient 2014: 10;
  - universal 2015: 12.
- **Solo papers 2021–2024:** 8–32.
- **Recent co-authored papers (2025–2026):** 27–45 (e.g. Dvurechensky & Nesterov, FoCM 2026: 45; E.-Nagy, Illés, Nesterov & Rigó, MP 2026: 37).
- In the three solo DPs read, a large share of the references are to his own earlier papers (e.g. in DP 2013/26, 7 of 11 references include him as an author, 4 of them solo).
- The three solo DPs (2010/2, 2012/2, 2013/26) carry **no acknowledgements of people**, only grant lines.
- Later solo papers thank individuals:
  - Grapiglia and the referees (tensor, 2019);
  - Ion Necoara and Nikita Doikov (2509.20902);
  - Nemirovski (2603.21500).

### 3.4 arXiv behaviour [practice, P; arXiv author listing, 57 records, parsed 2026-09-28]

- **Solo arXiv postings begin in 2020.** The first is the COVID paper 2007.11429; the optimization papers start from 2022.
- **Solo revisions are quick fixes made days after posting, never updates after review:**
  - 2007.11429 v1 22 Jul → v2 23 Jul 2020: typo fixes, e.g. "Next-Day Low" → "Next-Day Law";
  - 2311.15154 v1 25 Nov → v2 2 Dec 2023: a sentence moved; a new acknowledgement of "excellent working conditions at The Hong Kong Polytechnic University";
  - 2603.21500 v1 22 Mar → v2 25 Mar 2026: mostly English polish ("Our approach can be seen as an unambiguous" → "… as a straightforward"; "on the level of" → "at the level of"; "IPM" → "IPMs") plus one substantive clarification ("If the problem is feasible, then the projective variable goes to infinity too.").
- **Published solo papers are not updated with journal references.** 2201.04852 (Vietnam J. Math. 2025) and 2311.13838 (JOTA 2024) remain v1.
- **Student co-authored papers are updated with journal references in batches.** Doikov, Rodomanov and Grapiglia papers were all revised between 19 May and 3 June 2021.
- **A draft-versioning habit shows once.** 2603.21500 prints its TeX file and version under the title: "[ version 3.0, file: FeasIPM\InfeasIPM3.tex ]" in v1 and "[ version 4.0, file: FeasIPM\InfeasIPM4.tex ]" in v2. The path uses a Windows backslash.
  - [inferred] Numbered TeX files per draft, and a Windows machine. The latter is consistent with the 2012 DP's "Windows system" remark.
  - This is a single instance; no other paper shows the stamp.
- **Caution.** The weekday-and-time headers on arXiv PDFs (e.g. "Friday 20th December, 2024, 01:58") are arXiv's compile time, not his writing time. The recompiled 2007.11429 v1 PDF carries "Monday 16th May, 2022". Do not read working hours from them.

### 3.5 Presentation habits visible across 15 years [practice, P]

- **Tables are numbered like displayed equations.** Examples: (6.9) in 2010, (7.7)–(7.11) in 2012, (5.3)–(5.8) in 2013, (8.1)–(8.3) in 2024, (9.6)–(9.8) in 2025.
- **Numerics sit in the last or second-to-last section.**
- **They are labelled "preliminary" in every solo paper that has them:**
  - 2010: "preliminary computational results";
  - 2012: "preliminary computational experiments";
  - 2013: "preliminary computational results";
  - 2024: "preliminary computational results";
  - 2025: "preliminary but encouraging numerical results".

  The same word appears in the solo 2007/76 abstract (IDEAS) and in the 2020 (Rodomanov) and 2021 (Florea) joint papers.
- **A size taxonomy as a design device.** DP 2012/2 opens with "Table 1. Problem sizes, operations and memory". It lists small (all operations, 10⁰–10²), medium (A⁻¹, 10³–10⁴), large-scale (Ax, 10⁵–10⁷) and huge-scale (x + y, 10⁸–10¹²), with iteration cost and memory for each. [inferred] He picks the admissible operation first and designs the method to fit it.

---

## 4. Problem choice, excursions and abandoned directions (framework layer 2)

- **COVID-19 modelling, 2020: an excursion with no follow-up** [practice, P]:
  - **Record.** Two solo CORE DPs: "Online prediction of COVID19 dynamics. Belgian case study" (DP 2020/22) and "Online analysis of epidemics with variable infection rate" (DP 2020/25 = arXiv 2007.11429, physics.soc-ph, 24 pp., 13 figures).
  - **Method.** An axiomatic discrete-time model ("HIT") fitted to public daily counts: "Our World in Data" and "WORLDOMETER" are refs. [11] and [15]. Political events are dated from news articles (BBC, Bloomberg, Time, Business Insider).
  - **Claims are strong.** DP 2020/22 abstract: "During this time, our predictions were exact, typically, within the accuracy of 0.5%." DP 2020/25: "Our reconstructions are very precise." It also says "all tested countries are in a dangerous zone except Sweden".
  - **A resource limit is admitted.** "However, at this moment we do not have enough information and human resources for investigating this question in details." So one delay, Δ = 10, calibrated on Belgium, is used for all countries.
  - **Afterwards.** No journal version is found in Crossref, and the papers are absent from DBLP. There is no later epidemic paper on arXiv. Semantic Scholar shows 2 citations for 2007.11429.
  - [inferred] A fast, solo entry into a crisis problem using his own modelling style. It stopped after two DPs. Why is not recorded.
- **Preprints with no journal version found** (as of 2026-09-28, Crossref title search) [practice, P]:
  - Ahookhosh & Nesterov Part II (arXiv 2109.12303, Sept 2021). Part I appeared in MP 2024 after 25 months.
  - "Gradient Methods for Stochastic Optimization in Relative Scale" (Nesterov & Rodomanov, arXiv 2301.08352, v2 May 2023).
  - "High-Order Reduced-Gradient Methods for Composite Variational Inequalities" (arXiv 2311.15154).

  Their fate is unknown: rejection, still under review, or dropped. **Not verified.**
- **Title changes on the way to the journal**:
  - "Optimization Methods for Fully Composite Problems" (arXiv 2103.12632) → "High-Order Optimization Methods for Fully Composite Problems" (*SIAM J. Optim.* 2022, DOI 10.1137/21m1410063);
  - "Gradient methods for minimizing composite objective function" (DP 2007/76) → "… composite functions" (MP 2013).
- **Re-entering the interior-point field with a group** [practice, P]. The 2024–2026 IPM papers (2412.14934, 2503.10155, 2603.21500, and the E.-Nagy–Illés–Nesterov–Rigó MP 2026, DOI 10.1007/s10107-025-02260-x) reuse the Budapest group's random generator and ideas. The solo papers do the theory, and the numerics stay small and random.

---

## 5. Research organisation visible in the record (framework layer 7)

- **Peer seminars as a testing ground** [stated, P; 2013 dissertation, "Публикации и апробация результатов" (publications and presentation of results), via dissercat].
  - The venues listed: Nemirovski's optimization seminar at Georgia Tech, "(апрели 2008 - 2012гг.)" (the Aprils of 2008–2012); Polyak's laboratory at IPU RAN (March 2011); Tikhomirov's seminar at MSU (April 2012); Spokoiny's PreMoLab at MIPT (December 2011, April 2012); IFOR, ETH Zurich (March 2008, September 2011).
  - The Optima 78 essay likewise says it was written during a visit to IFOR, ETH Zurich (paraphrase).
  - [inferred] A yearly spring visit to the closest peer's seminar served as his review loop in 2008–2012.
- **The 2013 dissertation is built from solo papers** [stated, P]. It rests on 19 articles, only two of which were "написанных в соавторстве" (written with co-authors). For those two he claims the results listed among the thesis propositions.
- **Student-era division of labour** [practice, P + inferred]:
  - Every code artefact found was written by the junior co-author (Doikov: C++ and Python; Bankmann: Python).
  - Student-led experiments use ML-style datasets and baselines.
  - His solo numerics remain small, hand-run and generator-based.
- **Resource and era context** [practice, P]:
  - **2010:** a Pentium-4 at 1.6 GHz, already old hardware then.
  - **2012:** "a standard PC with 2.6GHz processor and 4Gb of RAM", Windows.
  - **2025:** "the usual notebook". A laptop was enough because the claim is about iteration counts; there are no GPUs, clusters or benchmark suites anywhere.
  - **Students (2020):** a Core i5 at 1.6 GHz, C++. Students (2022): Python notebooks.
  - Funding lines: Belgian ARC and IAP grants (2010–2013); the Russian PreMoLab grant (2012); ERC Advanced Grant 788368 (2018–2023).
  - Team: a single senior author until about 2016, then a stream of students and postdocs.

---

## 6. Stated versus practice (testing agent 02's candidate methods)

| Stated (agent 02) | What the practice shows | Verdict |
|---|---|---|
| Rates first, experiments confirm. 2013 dissertation [stated, P]: "Оценки скорости сходимости стали важным аргументом в пользу новых методов. Может быть даже более важным, чем результаты предварительных численных экспериментов." My translation: rate estimates became an important argument for new methods, perhaps even more important than preliminary numerical experiments. | 6 of 11 solo papers have no numerics. Where numerics exist they test the rate (§1.1, Patterns 1–2). Claims survive review unchanged without experiments (tensor, §3.1). | **Consistent** |
| Remove unknowable parameters at a constant-factor cost (E2, T13) | Doubling-and-restart and backtracking appear in each solo DP with numerics. The universal DP reports the method's Lipschitz estimate next to the iteration count ("the actual level of the Lipschitz constants are much lower than the theoretical prediction"). But in practice the constants are hand-set (η = 2; β = 0.2, A = 2), and the tensor Lipschitz estimate stays an open problem in print. | **Consistent, with an admitted gap** |
| "You need to check your answers using alternative methods." / "you shouldn't trust computers blindly" (NCCR 2023, E4) | His solo experiments are never checked against another solver or code (§1.1, Pattern 1). Instead, correctness is checked by construction: known optimal values, planted solutions (Pattern 3), and method-generated accuracy certificates. | **Partly consistent.** The check is by construction, not by an alternative code |
| Progress means "it took an hour … reduced to one minute" (NCCR 2023; 01 §3) | Wall-clock time appears in solo work only in DP 2012/2, measured against the same method implemented differently, and in the 2025 "less than fifty seconds" remark. There are no timed comparisons against competing methods. | **Tension** (kept in Contradictions) |
| Match the method to size and affordable operations (P5) | DP 2012/2 Table 1 (size classes by admissible operation). The 2010 and 2012 DPs design the method around O(1) or O(log n) updates. | **Consistent** |
| Break a bound by changing the oracle or class, then say which assumption changed (I3, I4, J3) | Optima 88 resisting-oracle construction; tensor paper's convexification of the Baes scheme (§2.2) | **Consistent** |

---

## 7. What this means for a solver team (for the skill author) [inferred]

- To think like Nesterov about a solver change:
  1. Write the per-iteration cost in terms of the admissible operations.
  2. Prove, or at least state, the rate.
  3. Test the rate on random instances with a planted solution by tabulating iterations against ε.
  4. Isolate implementation choices by ablation inside one algorithm.
- Do **not** expect him to supply benchmarking protocol, CUTEst-style test sets, performance profiles or cross-solver comparisons. None was found in his own work. In the student-led work these come from the students.
- Diagnostics he actually uses:
  - the method's own gap or accuracy certificate against the true residual;
  - the empirical exponent read from the table;
  - the Lipschitz estimate the method generates;
  - for convexified subproblems, a slow inner process as a signal that the regularization constant is too small (tensor §6).

---

## Contradictions (kept, not reconciled)

1. **arXiv revisions.**
   - 01 (§2.1) says: "All eight arXiv abstract pages I checked have a single version (v1). He does not post revised versions publicly."
   - The full listing shows three solo papers with a v2 (2007.11429, 2311.15154, 2603.21500), each within days of v1, plus many revised joint papers.
   - Both are partly true. No solo paper is updated after review; quick post-posting fixes do happen.
   - 01 also dates his first solo arXiv posting to 2022 ("Quartic regularity"). The listing shows the solo COVID paper 2007.11429 in July 2020. The first solo *optimization* posting is indeed 2022.
2. **Wall-clock yardstick versus iteration-count practice.**
   - [stated] NCCR 2023: progress is seen when solving "took an hour" and "it's reduced to one minute".
   - [practice] His solo numerics report iterations against accuracy. The only timed comparisons are against his own alternative implementation (2012) or a single statement of absolute time (2025).
3. **"Check your answers using alternative methods" versus no cross-solver checks.**
   - [stated] NCCR 2023.
   - [practice] §1.1, Pattern 1. The SDO paper names Li–Sun–Toh and Zhao–Sun–Toh as the comparison to make and leaves it to others.
4. **Tensor methods' practicality.**
   - The DP and journal abstract: "implementable and very fast". This was kept through 19 months of review with no experiment.
   - Jackson (IMU 2026, p. 3): "Requiring huge computing capacity, tensor methods remain theoretical constructs for now".
   - Nesterov's own §6 lists the Lipschitz-constant adjustment as "clearly crucial for the practical efficiency" and unsolved.
5. **Rebuttal promises versus the final paper** (NeurIPS 2020). The SoftMax and second-order line-search experiments were promised and do not appear in the camera-ready or arXiv v2. A SoftMax experiment appears in a different paper in 2022.
6. **Citation ethics stated versus co-authorship practice.**
   - [stated] NCCR 2023: "The impact of one paper should be divided by the number of authors"; "now there may be 50 or 60. It is meaningless."
   - [practice] He is one of 8 authors on the NIPS 2016 PageRank paper and on arXiv 1506.00292 and 1411.4282 (2014–2016).
   - The statement is from 2023, the papers from 2014–2016. Both are recorded.
7. **Zenodo creators versus the code's author field** (Bankmann et al.). Zenodo lists all four authors as creators; `setup.py` names Daniel Bankmann as author.
8. **Degree label of the 2013 dissertation.** dissercat labels the 2013 dissertation "кандидат наук" (candidate). His PhD (candidate) dates from 1984 (01 §2), so the 2013 work is presumably a Doctor of Sciences thesis [inferred]. Not verified.

## Gaps

- **OpenReview.** Blocked by a bot check, both page and API. The one WebSearch found nothing. Whether any ICLR/NeurIPS/ICML submission with Nesterov was rejected or withdrawn is **unknown**.
- **Referee reports and rejections for journal papers.** None is public. Crossref dates show long reviews but cannot show rejections.
- **Journal full texts.** Springer and SIAM versions of the solo DPs were not readable, so body-level differences between DP and journal versions are unknown beyond abstracts and reference lists.
- **The composite DP 2007/76.** Its text (the one with "preliminary computational experiments, which confirm the superiority of the accelerated scheme") could not be obtained:
  - the UCLouvain Alfresco link needs the document-details app;
  - a Wayback copy is listed (Composit.pdf, 2016 snapshot), but the connection was reset.

  Its test-problem generator is therefore **not read**.
- **Content of the two corrections** (2018 JORSC; 2024 MP): not read.
- **Code for his solo numerics.** Language (MATLAB, C, other) and scripts are never stated. No code was released. How he debugs is **unknown**. No evidence exists beyond the diagnostic rules printed in the papers.
- **The 2006 cubic-regularization and 2008 accelerated-cubic papers.** Not read, including the "Ложное ускорение" (false acceleration) section; only its title is known.
- **The 1984 thesis and the 1989 monograph.** *Эффективные методы нелинейного программирования* (Радио и Связь, 1989, 280 pp.) is listed as ref. [21] in the 2013 dissertation bibliography on dissercat; that is now a tool-seen record, but the book was not read. Soviet-era experimental practice therefore remains **unknown**.
- **Division of labour in joint papers.** Not stated in any source found. Agent 04 (students) may find it.
- **Talks.** No transcript or video of a talk in which he shows how he works was found or saved.

## Sources

Primary = the work itself, his own words, an artefact, or a bibliographic record. Secondary = someone else's account.

1. Yu. Nesterov, "Efficiency of coordinate descent methods on huge-scale optimization problems", CORE DP 2010/2 (Jan 2010), full text; journal *SIAM J. Optim.* 22(2) (2012) 341–362, DOI 10.1137/100802001 (abstract via OpenAlex; references via Crossref). Primary.
2. Yu. Nesterov, "Subgradient methods for huge-scale optimization problems", CORE DP 2012/2 (Jan 2012), full text; journal *Math. Program.* 146 (2014), DOI 10.1007/s10107-013-0686-4 (Crossref references). Primary.
3. Yu. Nesterov, "Universal gradient methods for convex optimization problems", CORE DP 2013/26 (Apr 2013), full text; journal *Math. Program.* 152 (2015) 381–404, DOI 10.1007/s10107-014-0790-0 (Crossref references). Primary.
4. Yu. Nesterov, "Implementable tensor methods in unconstrained convex optimization", *Math. Program.* 186 (2021) 157–183, DOI 10.1007/s10107-019-01449-1, open-access full text PMC7875858; DP 2018/05 abstract on IDEAS (https://ideas.repec.org/p/cor/louvco/2018005.html). Primary.
5. M. Ahookhosh, Yu. Nesterov, "High-order methods beyond the classical complexity bounds: inexact high-order proximal-point methods", *Math. Program.* 208 (2024), DOI 10.1007/s10107-023-02041-4, full text PMC11480125; Correction DOI 10.1007/s10107-024-02067-2 (record only). Primary.
6. N. Doikov, Yu. Nesterov, "Convex optimization based on global lower second-order models", NeurIPS 2020 (Advances in NeurIPS 33): paper, supplement, six reviews, meta-review, author feedback. https://proceedings.neurips.cc/paper_files/paper/2020/hash/c0c3a9fb8385d8e03a46adadde9af3bf-Abstract.html. Paper and rebuttal primary; reviews secondary (observed).
7. Same, arXiv 2006.08518v2 (21 Dec 2020). Primary.
8. Bogolubsky et al., "Learning Supervised PageRank with Gradient-Based and Gradient-Free Optimization Methods", NIPS 2016, reviews page. https://proceedings.neurips.cc/paper_files/paper/2016/hash/1f34004ebcb05f9acda6016d5cc52d5e-Abstract.html. Secondary (reviews).
9. arXiv author search "Nesterov, Yurii", 57 records with submission and version dates, fetched 2026-09-28. https://arxiv.org/search/?query=Nesterov%2C+Yurii&searchtype=author. Primary record.
10. Yu. Nesterov, "Online analysis of epidemics with variable infection rate", arXiv 2007.11429 v1 and v2 (= CORE DP 2020/25); DP 2020/22 "Online prediction of COVID19 dynamics. Belgian case study", abstract on IDEAS (https://ideas.repec.org/p/cor/louvco/2020022.html). Primary.
11. Yu. Nesterov, "Quartic Regularity", arXiv 2201.04852; *Vietnam J. Math.* 53 (2025) 553–575, DOI 10.1007/s10013-024-00720-z. Primary.
12. Yu. Nesterov, "Primal subgradient methods with predefined stepsizes", arXiv 2311.13838; *JOTA* 2024, DOI 10.1007/s10957-024-02456-9. Primary.
13. Yu. Nesterov, "High-Order Reduced-Gradient Methods for Composite Variational Inequalities", arXiv 2311.15154 v1 and v2. Primary.
14. Yu. Nesterov, "Local and Global Convergence of Greedy Parabolic Target-Following Methods for Linear Programming", arXiv 2412.14934. Primary.
15. Yu. Nesterov, "Asymmetric Long-Step Primal-Dual Interior-Point Methods with Dual Centering", arXiv 2503.10155. Primary.
16. Yu. Nesterov, "Universal Complexity Bounds for Universal Gradient Methods in Nonlinear Optimization", arXiv 2509.20902. Primary.
17. Yu. Nesterov, "Theorem of Alternative for Extended Homogeneous Linear System and its Application in Conic Optimization", arXiv 2603.21500 v1 and v2 (dated March 22, 2026). Primary.
18. Yu. Nesterov, M. I. Florea, "Gradient methods with memory", arXiv 2105.09241; *Optim. Methods Softw.* 37 (2022) 936–953, DOI 10.1080/10556788.2020.1858831. Primary.
19. A. Rodomanov, Yu. Nesterov, "Greedy Quasi-Newton Methods with Explicit Superlinear Convergence", arXiv 2002.00657v2; *SIAM J. Optim.* 31 (2021) 785–811, DOI 10.1137/20m1320651. Primary.
20. N. Doikov, K. Mishchenko, Yu. Nesterov, "Super-Universal Regularized Newton Method", arXiv 2208.05888; *SIAM J. Optim.* 34 (2024) 27–56, DOI 10.1137/22m1519444. Primary.
21. github.com/doikov/contracting-newton (git clone; log Oct 2020; README). Primary (student artefact).
22. github.com/doikov/super-newton (git clone; log 12 Aug 2022; README, notebooks). Primary (student artefact).
23. Zenodo record 2643171, "Code and examples for the paper 'Computation of the analytic center …'" (2019-04-17), tarball `setup.py`; paper *Vietnam J. Math.* 48 (2020) 633–659, DOI 10.1007/s10013-020-00427-x. Primary.
24. Crossref REST API: received, accepted and first-online dates and reference counts for about 60 Nesterov DOIs (DBLP pid 00/343 list); the erratum/correction search; title verification. https://api.crossref.org/. Primary record.
25. OpenAlex work records (SIOPT 2012 abstract). https://api.openalex.org/. Primary record.
26. IDEAS/RePEc CORE DP pages 2003/12, 2005/67, 2007/76, 2018/05, 2020/22, 2020/25 (abstracts). Primary.
27. UCLouvain CORE Discussion Papers 2007 index. https://sites.uclouvain.be/core/publications/coredp/coredp2007.html. Primary record.
28. Optimization Online, WordPress API search "Nesterov" and "Rosenbrock"; posts 2011/02/2923, 2011/05/3042, 2011/07/3101. Secondary.
29. M. Gürbüzbalaban, M. L. Overton, "On Nesterov's Nonsmooth Chebyschev-Rosenbrock Functions", preprint 24 Jan 2011 (Optimization Online 2011/02/2923, PDF read); *Nonlinear Anal.* 75 (2012), DOI 10.1016/j.na.2011.07.062. Secondary (observed).
30. F. Jarre, "On Nesterov's smooth Chebyshev–Rosenbrock function", *Optim. Methods Softw.* (2013), DOI 10.1080/10556788.2011.638924 (abstract via Optimization Online 2011/05/3042). Secondary.
31. C. Cartis, N. I. M. Gould, Ph. L. Toint, "A note about the complexity of minimizing Nesterov's smooth Chebyshev–Rosenbrock function", *Optim. Methods Softw.* (2013), DOI 10.1080/10556788.2012.722632 (abstract via Optimization Online 2011/07/3101). Secondary.
32. Yu. Nesterov, "How to advance in Structural Convex Optimization", *Optima* 78 (Nov 2008), MOS newsletter (text read from this run's scratch copy; exact archive URL not re-resolved). Primary.
33. Yu. Nesterov, discussion column "How to Make the Gradients Small", *Optima* 88 (May 2012), pp. 10–11 (text read from this run's scratch copy). Primary.
34. Yu. E. Nesterov, «Алгоритмическая выпуклая оптимизация» (dissertation, 2013, 367 pp.), table of contents, introduction and bibliography as hosted by dissercat.com (OCR text). Primary text via a secondary host.
35. C. Cartis, N. I. M. Gould, Ph. L. Toint, "Adaptive cubic regularisation methods … Part I", *Math. Program.* 127 (2011) 245–295, DOI 10.1007/s10107-009-0286-5, preprint p. 2 (https://pure.unamur.be/ws/files/1332672/cgt31RR_I.pdf). Secondary (observed).
36. R. Weldon, "'This is an unprecedented overflow' …", NCCR Automation interview, 15 Aug 2023. https://nccr-automation.ch/news/2023/unprecedented-overflow-why-progress-his-field-alarms-yurii-nesterov. Primary (stated).
37. A. Jackson, "2026 Gauss Prize: Yurii Nesterov", IMU write-up. https://www.mathunion.org/fileadmin/documents/2026-07/article-gauss-final.pdf. Secondary.
38. DBLP pid 00/343 record export (the same harvest used by 01), for DOIs and conference records. https://dblp.org/pid/00/343. Primary record.
39. Semantic Scholar record for arXiv 2007.11429 (citation count only). Secondary.

Blocked or not usable: OpenReview profile and API (bot challenge); GitHub REST API (not enabled for this session); Wayback Machine copy of CORE DP 2007/76 (connection reset; the plain-HTTP attempt was refused by egress policy); old mathopt.org Optima PDF URLs (404); WebSearch "openreview.net "Yurii Nesterov" submission reviews" (no relevant hit).
