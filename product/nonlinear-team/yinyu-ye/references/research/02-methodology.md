# 02 · Stated methodology: what Yinyu Ye SAYS research should be

> **Researcher:** Yinyu Ye (叶荫宇), K. T. Li Professor of Engineering (Emeritus), Stanford MS&E and ICME; now also visiting at SJTU / Shanghai Institute for Mathematics and Interdisciplinary Sciences, CUHK-Shenzhen and HKUST (S21).
> **Dimension:** research agent 02 of 06, stated methodology (claims about how research should be done). Whether he does it is agent 03's job.
> **Research date:** 2026-09-28.
> **Sources consulted:** 29 documents (S1–S29 below: 24 primary, 5 secondary, one of the secondary low-provenance), plus 13 bibliographic records checked by tool (Crossref, arXiv abstract pages, PMLR). No user-supplied material existed: `references/sources/{papers,talks,essays,software}` were empty, and `private/` was not opened. WebSearch calls used: 2 of 2.
> **Evidence base:** Most of the evidence is primary and was read in full text: two book prefaces (1996 and 2021), Chapter 1 of *Interior Point Algorithms* (1997), the 2009 von Neumann Prize acceptance speech, a 2020 first-person profile, a 2023 autobiographical slide deck, about ten talk decks from 2021–2026, a 2026 research note, one edited Chinese talk transcript (2017) and one edited Chinese interview (2025). Chinese sources are quoted in the original, followed by an English translation marked **[tr.]**. English slide quotes are verbatim. Where PDF text extraction lost the spaces, I restored them and checked the wording against a rendered image of the slide (S9 slides 38 and 61; S4 slides 12 and 15).
> **Tags:** [stated] = he said it. [practice] = what he did (noted only in passing, for agent 03). [observed] = what others say about him. [inferred] = my reading. Every row gives primary or secondary.
> **Caveat on authorship of slides:** in the PDF metadata of several recent decks the author is someone else (S10, S11, S18, S17: "xcy27"; S19: "Dongdong Ge"). Ye presented them, but team members prepared them, so wording on those decks may not be his alone. S14 is co-authored with Bento Natura and Takashi Tsuchiya. S8 is co-authored with David Luenberger.

---

## 0. Recurring stated beliefs (a claim counts as a belief when it appears in at least 3 independent sources)

| # | Belief (short form) | Times | Where (years) | Tag |
|---|---|---|---|---|
| R1 | **Theory and practice must meet.** The best algorithm has a proof *and* gets implemented; theory should explain and justify the "tricks" used in practice. | 5 | S7 (1997), S6 (2015), S9 (2021), S4 (2023), S1 (2025/26 homepage framing) | [stated] primary |
| R2 | **Worst-case, size-based complexity is not enough. Find the instance's condition measure (the "bottleneck") and attack it.** | 5 | S7 (1997, twice), S11 and S10 (2023), S12 (2023), S14 (2023), S1 ("LP-IPM with Runing Time Depending only on A") | [stated] primary |
| R3 | **Long-standing open questions are the prize.** Settle them; train students on them. | 5 | S1, S5 (2020), S6 (2015), S14 (2023), S15 (2023) | [stated] primary (S6 secondary) |
| R4 | **Speed and scale decide relevance.** | 5 | S6 (2015), S24 (2017), S9 (2021), S18 (2025), S19 (2026) | [stated] primary |
| R5 | **Pick the "order" of information by need, and combine zeroth-, first- and second-order methods** rather than betting on one. | 6 | S9 (2021), S10 (2023-06), S11 (2023-08), S13 (2023-09), S15 (2023-11), S19 (2026) | [stated] primary |
| R6 | **Quantify.** OR/optimization gives exact, explainable, certifiable answers. Pure data-learning or AI does not replace an algorithm, though the two should be combined. | 5 | S24 (2017), S11 (2023), S23 (2025), S20 (2026), S26 (2024, low provenance) | [stated] primary |
| R7 | **Duality and prices are the working lens**: dual/shadow prices drive decisions; the cost-to-go values are shadow prices. | 5 | S10, S11, S13, S15 (2023), S18 (2025) | [stated] primary |
| R8 | **An algorithm should certify infeasibility** (a homogeneous, one-phase design, with no big-M). | 3 | S8 (2021), S13 (2023), S19 (2026) | [stated] primary |
| R9 | **Move information between online and offline, and between learning and deciding.** | 4 | S10, S11 (2023), S17 (2024, "Online Helps Offline"), S18 (2025) | [stated] primary |
| R10 | **Don't chase fashion. Build a deep specialty and a solid foundation.** | 3 | S25 (2017), S4 (2023), S28 (2024) | [stated]; S25 and S28 are secondary reports |
| R11 | **The sports ethos is also the research ethos**: train hard, work as a team, compete, take a loss, play by the rules. | 4 | S5 (2020), S4 (2023), S27 (2024), S28 (2024) | [stated]; S27 and S28 secondary |

Said twice only, so below the threshold: mentors teach "scholarship, intellectual integrity, curiosity and rigorous thinking" (S5, S4); the 1984 Karmarkar seminar as the origin story (S7, S5); the 1982 AI expert-system episode as the origin of his interest in quantification (S24, S23). "Customized, not universal, algorithms" is one statement at one event, reported twice (S24, S25).

---

## 1. Research taste: what is worth doing, and what counts as a good result

**1.1 A good algorithm has both a guarantee and practical efficiency (R1)** [stated, primary]
- 1996/97: "We have to admit that the criterion of polynomiality is somewhat controversial. Many algorithms may not be polynomial but work fine in practice." … "Furthermore, it is ideal to develop an algorithm with both polynomiality and practical efficiency." (S7, Ch. 1, p. 31)
- 1996/97, on why implementations differ from theory: "It is common to have a gap between a theoretical algorithm and its practical implementation: theoretical algorithm makes sure that it works for all instances and never fails, while practical implementation emphasizes average performance and uses many clever "tricks" and ingenious techniques." "Our objective is to provide theoretical justification for these techniques and to explain their practical pros and cons." (S7, p. 5)
- 2015, explaining his MDP strong-polynomiality work (P1): "There was a significant gap between theoretical research and practical application," "It bothered me." (S6; direct quote in a department news article, so secondary.) The article paraphrases his aim as proving the methods efficient "to increase confidence" (reporter's wording, not his).
- 2021, summary slide: "The innovation of efficient optimization methods/algorithms should be driven by scientific/theoretical research, besides software engineering and coding" (S9, slide 61).
- 2025/26 homepage, how he frames his own selected work: "Predictor-Corrector IPM and Homogeneous and Self-Dual Algorithm that are implementaed in all Linear Programming Commercial Solvers"; DRO and online LP are "both are populary applied in business and industries"; complexity work is described as work "where we settled long-time open questions" (S1, verbatim including typos). The papers named are P4 (predictor-corrector), P3 (HSD), P5 (DRO) and P1 (MDP). [stated self-description]
- Era: the 1997 statements come from a sole-authored monograph written at Iowa, supported by NSF grants (S7 acknowledgements), before any solver company existed. The 2021 and later statements come after COPT (2019) and inside a large team.

**1.2 Judge an algorithm by its condition measure, not only by its size-based bound (R2)** [stated, primary]
- "The worst-case complexity bound alone hardly serves as a practical criterion for judging the efficiency of algorithms." (S7, p. 4)
- "This condition number represents the degree of difficulty of the problem instance." (S7, p. 4). He adds that the classification "will help us to understand algorithm efficiency and possibly improve the condition and, therefore, improve the complexity of the problem."
- "It is our goal to study this phenomenon and to improve the condition number and, thereby, the performance of an algorithm." (S7, p. 32)
- 2023: the bandits-with-knapsacks algorithm (P13) "identifies a number of LP-related parameters as the bottleneck or condition-numbers for the problem", namely the "Minimum non-zero reduced cost" and the "Minimum singular-values of the optimal basis matrix" (S10 slide 9; S11 slide 13).
- 2023, Simons bootcamp (co-authored deck): "Question: How many iterations to solve an LP exactly? Can the condition numbers be bounded Polynomially in dimensions?" He also says of his own Vavasis–Ye algorithm (P2): "The algorithm is not scale-invariant." (S14, slides 9 and 11)
- **Counter-taste:** a bound *free* of condition numbers is advertised as a merit. For nonconvex QP by potential reduction: "(no condition-numbers!)" (S13, slide 33, citing P8). And: "GHM-Lanczos (eigenvalue) is immune to ill-conditioning"; "In theory, Lanczos method for eigenvalue is depends on gaps instead of cond. #" (S12, slides 24–25).

**1.3 Settling an open question is the highest form of result (R3)** [stated]
- The homepage phrase above (S1). The 2023 Simons workshop talk ends with a list of open questions, for example "Is the policy iteration method strongly polynomial for the deterministic MDP?" and "Is there a strongly polynomial-time algorithm for MDP regardless the discount factor?" (S15, final slide). The co-authored bootcamp deck closes with "LP remains an open research field…" (S14).

**1.4 Speed matters (R4)** [stated]
- "Speed is always very crucial for real applications. Every millisecond counts," "If you are not faster than someone else, you're behind." (S6, 2015; direct quote, secondary)
- 2017: "我个人认为高频交易的竞赛也就是算法速度的这个竞赛。" **[tr.]** "I personally think the competition in high-frequency trading is just a competition in algorithm speed." (S24)
- 2021: "Large-scale Applications Demand Faster Algorithms" (S9, slide 36)
- 2025: "Can we develop new algorithms based on GPU to increase the scale and speed of solvable problems by a hundredfold or even ten thousandfold?" (S18, slide 36)

**1.5 Elegance and geometry** [stated, said once each]
- IPM is "one of the most beautiful and elegant numerical algorithms" (S9, slide 53, 2021).
- "These geometries are always helpful for teaching, learning, and research." (S7, p. 3, about "center", "volume" and "potential" of a polytope)

**1.6 What a model is worth: exactness, explainability, robustness (R6)** [stated]
- 2023 slide "Differences of OR and AI Models". The OR column reads "Based on Science/Logic; Physical/Economical Principles; Objective; Definitive; Explainable Insights; Online Training&Decision-Making". The AI column reads "Based on Cases/Experience; Observation/Behaviour; Subjective; Probabilistic; Black-box; Offline Training". Takeaway: "Know the pros and cons of OR and AI models and use them intelligently" (S11, slides 6 and 42).
- 2025: "相比于人工智能，运筹学的显著优点是：设计一种算法无需真实数据参与，可将问题和数据抽象化……以不变应万变，以"一"对"无穷"。" **[tr.]** "Compared with AI, the notable advantage of OR is that designing an algorithm needs no real data; the problem and data can be abstracted … meeting all changes with the unchanging, 'one' against 'infinity'." (S23)
- 2026 note (S20, sole-authored): the LP optimal basis can change arbitrarily between two nearby data points that share the same optimal basis, so "the pure offline learning from data, basic on data similarity, is unlikely to accurately predict its optimal basis or optimal solutions for linear programming." And: "Data learning may be more helpful to Integer Programming due to its solution-Immutability." (S20, p. 3, verbatim)
- 2024 (low provenance, S26) lists four traits of decision problems: precision, causal explainability, robustness, and time/resource sensitivity. It argues that pure learning has trouble giving high-precision solutions, is a black box, and cannot bound catastrophic outcomes. It agrees with S11 but gets no extra weight.

---

## 2. Problem choice: where problems come from, why now, when to leave

**2.1 Origin: applicability, not hype** [stated, primary]
- 1996 preface: "I was not particular enthusiastic about the statement from the speaker that a new interior-point method would be 40 times faster than the simplex method, but I was amazed by the richness and applicability of linear programming as a whole. That was how and when I determined to devote my Ph.D. study to mathematical programming." (S7, p. xiii; this is his account of Karmarkar's 1984 Stanford seminar)
- 2020 retelling: "I was amazed by the richness and applicability of linear programming, which can be used to optimize all sorts of real-world processes …" (S5). This version drops the skepticism about the "40 times faster" claim.

**2.2 A contradiction between theory and practice is a signal to work there** [stated]
- 1997: the ellipsoid-versus-simplex "contradiction, the fact that an algorithm with the desirable theoretical property of polynomiality might nonetheless compare unfavorably with the (worst-case exponential) simplex method, set the stage for exciting new developments." (S7, p. 3)
- 2015: the MDP gap "bothered me" (S6). See 1.1.

**2.3 Follow the scale of applications and the computing platform** [stated]
- 2017: "我们以前比较重视凸规划，大量的问题是凸规划。现在需要考虑如何集群化、软硬件结合，如何利用 GPU 实现并行运算" **[tr.]** "We used to focus on convex programming … Now we need to consider clustering, hardware–software integration, and how to use GPUs for parallel computation." (S24). This was said about six years before cuPDLP-C (P12, 2023). [inferred: the GPU pivot was stated as an agenda years before he acted on it; agent 06 should check the timing.]
- 2021 LNLP preface (co-authored): "linear programs are nowadays solved by computers rather than by hand. Therefore, we focus on introducing methods and algorithms most efficiently implementable by computer codes." And: "we have also removed a few sections where the methods and /or materials are not suitable for large-scale optimization and computer-coding in our modern computation age." (S8, pp. viii–ix)
- 2026: he lists why GPUs look ill-suited to classical optimization ("First-order algorithms suffer from low precision …", "Second-order algorithms involve matrix inversion/factorization, for which parallel acceleration on GPU yields limited improvement", integer programming involves "massive sequential and complex logical operations"), then writes: "But we made breakthroughs …" (S19, slide 8). [stated: he names the obstacles to a direction before entering it]

**2.4 Late-career turn toward impact** [stated, primary, 2017]
- "我原来比较重视理论，很多问题都是写文章，证明一些东西，也小有成就……我觉得最大的利益还是对一般人生活产生一些影响，因为谁也不知道很多理论证明的结果有什么东西。" **[tr.]** "I used to emphasise theory: for many problems I wrote papers and proved things, with some success … [now] I think the greatest benefit is still to have some effect on ordinary people's lives, because nobody knows what many theoretical proofs are good for." (S24)
- "OR 是一个接地气的科学，是一个落地的科学" **[tr.]** "OR is a down-to-earth science, a science that lands in practice." (S24)
- Era: this was said at an industry forum co-hosted by Cardinal Operations (杉数科技), where he was chief scientific adviser; the leiphone report also names him chair of MOSEK's technical advisory board. The audience may have shaped the emphasis.

**2.5 Choose a specialty; don't chase what is fashionable (R10)** [stated]
- 2017 Q&A: "我觉得不是人才紧缺的问题，而是导向的问题。我个人认为，中国学生学理工科都是很强的，但是，他们也是永远追那个最时髦的，我觉得这个风气要改一改。" **[tr.]** "It is not a talent shortage but a question of orientation … students always chase the most fashionable thing; this habit should change." He adds that students should "把基础打好" **[tr.]** "get the foundations right" (S25; report of the Q&A, secondary).
- 2023 slide "Advises to Students": "Have a Specialty: find something deep and interesting" (S4, slide 12; confirmed on the rendered slide).
- 2024 (NJU report): "但搞学术研究不能盲目跟风，每个学科都有自己的重要性" **[tr.]** "academic research must not blindly follow trends; every discipline has its own importance". He also "鼓励大家放下功利心……找到真正感兴趣的方向，并持之以恒地努力" **[tr.]** "encouraged everyone to put aside utilitarian motives … find a direction of genuine interest and persist" (S28; paraphrase by the reporter, secondary).
- **Caution:** a WebSearch summary attributed to Ye the advice "even if you study deep learning/AI, still learn optimization and statistics". In the source (S25) that advice is **Li Jian's**, not Ye's. It is not recorded as Ye's here.

**2.6 "Research Preference" axes (2023)** [stated as a list; his position is not stated]
- The "Research Tips" slide lists pairs without marking which side he prefers: "Theory vs Practice (IPO vs HSD/SNL)", "Model vs Methodology (DRO/CLP vs LP/NLP)", "Focus vs Broadness (MP vs OLP/AGT/MDP/APPROX)", "Quality vs Quantity (MDP vs SDR)". Under "Research Style" it lists "Individual vs Group" and "In mind vs On paper" (S4, slide 15; confirmed on the rendered slide).
- [inferred] Each sub-bullet seems to pair his own work with the two poles. For example, "Quality vs Quantity" is illustrated by MDP (P1, a single-author result on a long-open question) against SDR (semidefinite relaxation, many papers). **The talk itself was not found**, so his verdict on each axis is unknown. See Gaps.

**2.7 Models as contributions, not only algorithms** [stated]
- Homepage: DRO is work "where we created the name DRO first time" (S1; P5). Online LP is presented "as a general model for dynamic resource allocations" (S1). The "Model vs Methodology" axis appears in S4.

---

## 3. Idea generation: where ideas come from

**3.1 The order-of-information lens (R5)** [stated, primary]
- "We use Zeroth order f(x) First order ∇f(x) Second order ∇²f(x) information to design numerical algorithms. The more information we use, the more accurate solution is, the more computation is needed. We choose algorithm by need" (S9, slide 38, 2021; checked against the rendered slide).
- ADMM "is an 1.5th order algorithm (access 2nd order information once)" (S9, slide 49).
- Classic MDP methods are re-labelled the same way: "Value-Iteration (VI, first-order)" and "Policy-Iteration or multiple-pivot (PI, second-order)" (S15, slide 10).
- Takeaways: "Second-Order Derivative information matters and better to integrate FOM and SOM for nonlinear optimization!" (S10, final slide, 2023-06-30). "Better to integrate ZOM, FOM and SOM for Nonlinear and/or Black-Box Optimization!" (S11, final slide, 2023-08-11).
- Hybrid recipe: "First-order method solves to 1e-02 accuracy and then switch to second-order" (S13, slide 32; FOM potential reduction used as a presolver).

**3.2 Ask whether a cheaper step can do the expensive step's job** [stated]
- "Disadvantage: each iteration requires O(n3) operations: How to reduce it?" (S12, slide 3; motivation for HSODM, P11)
- "-gk is the first-order steepest descent direction but ignores Hessian; the most-left eigenvector of Hk would be a descent direction for the second order term. Could we construct a direction integrating both? Answer: Use the most-left eigenvector of the SDP homogenized quadratic function!" (S12, slide 4)
- "Typically, the factor representation method uses 2m rank based on theoretical results. But it is too large in practice, can we do better?" (S18, slide 42)
- The DRSOM idea (P10) is described as "Motivation from Multi-Directional FOM and Subspace Method, such as CG and ADAM, DRSOM applies the trust-region method in low dimensional subspace." (S10, slide 25; S11, slide 32)
- Takeaway: "Homogeneous second-order direction as an extreme eigenvalue computation is a "cheaper" alternative to the Trust-Region or Newton step computation" (S12, final slide)

**3.3 Homogenise or embed, so that special cases need no special handling** [stated rationale; the pattern is inferred]
- The HSD algorithm (P3): "It solves the linear programming problem without any regularity assumption concerning the existence of optimal, feasible, or interior feasible solutions, while it retains the currently best complexity result"; "it does not use any big M penalty parameter or lower bound" (S13, slide 36).
- LNLP 2021: "the homogeneous model/algorithm that is a one-phase algorithm with capability to detect possible primal or dual infeasibility, which becomes an important task in nonlinear optimization." (S8, p. ix)
- [inferred] The same homogenising move appears in the "SDP homogenized quadratic function" of HSODM (S12). Agent 03 should check whether this is one habit across 30 years.

**3.4 Prices and duality as the lens (R7)** [stated]
- "The key is to learn "ideal" itemized-prices"; "Such ideal prices exist and they are shadow/dual prices of the offline LP - How to Learn？" (S18, slide 6; the same table appears in S10 slide 7 and S11 slide 11).
- MDP: "The cost-to-go values are the "shadow Prices" of the LP problem." (S15, slide 4)

**3.5 Transfer between online and offline, and between learning and acting (R9)** [stated]
- "Learning-while-Doing vs Learning-First and Deciding-Second" (S10, slide 6; S11, slide 10). "LP Warm-Start: Online Helps Offline" (S17, section title). An online-learning step size for gradient descent, with the claim: "The method allows optimizing any learnable algorithm hyper-parameters" (S18, slide 28). "Can we take the best-of-both-worlds for the first-order and LP-resolving methods?" (S18, slide 12)

**3.6 Customized rather than universal algorithms (2017)** [stated, one event]
- "以前我认为我就要搞出个万能的算法，解所有的线性规划都要解得快，但是我后来反观看AI是非常定制的……不是追求某一个统一的算法……反而是比较定制化的，用中国话来讲比较实用主义一些。" **[tr.]** "I used to think I had to create a universal algorithm that solves every LP fast; but looking at AI, it is highly customized … not pursuing one unified algorithm … more customized; in Chinese terms, more pragmatic." (S24). The S25 report of the same talk: "所以这点上，AI 对我们的思维有所改变。" **[tr.]** "so on this point AI has changed our thinking."

**3.7 Ideas from applications** [stated]
- "modeling that tells the problem / algorithm that tells the answer" (S9, slide 36). 2017: "所以我们一般是从建模到求解，然后再到决策" **[tr.]** "so we generally go from modelling to solving, then to decision." (S24)
- The robust-decision motivation, from forecasting limits: "在测不准的情况下，在决策上是不是可以做点工作" **[tr.]** "when things cannot be predicted accurately, can we do some work on the decision side" (S24, 2017; this is the stated rationale behind the DRO line, P5).

---

## 4. Experiments and execution: what he says about building and testing

- **Solvers need theory and a small dedicated team** [stated, 2021]: "The development of mathematical programming solvers is best done by a small dedicated team whose members have passion and love in optimization" (S9, slide 61; checked against the rendered slide).
- **Own the core algorithms; patience** [stated, 2017]: "中国发展过程中忽略了算法的力量，他们通常是以问题为根本，找了一些参考资料在开源软件中找一个算法进行试一试……确实是要耐得住寂寞，但是要用人家的开源软件，不给的话永远会被牵着鼻子走。" **[tr.]** "China's development has neglected the power of algorithms: people start from the problem, look up some references, and try an algorithm found in open-source software … it really takes enduring loneliness [patience]; but if you rely on others' open-source software, when they withhold it you are led by the nose forever." (S24). Also: "要耐得住寂寞，要有核心的技术" **[tr.]** "one must endure loneliness and have core technology" (S24).
- **Aim for best in the world, not for a substitute** [stated, 2025]: "我们要做就要做到最好，要做到未来全世界都用我们的产品。" **[tr.]** "If we do it, we must do it best, so that in future the whole world uses our product." (S23)
- **Separate algorithmic gains from hardware gains** [stated in slides]: "Excluding hardware improvement, LP (COPT and others) speed becomes 3.5x faster on average in the past 4 years" (S18, slide 37; S19, slide 14). "SDP (COPT) speed is 2.5x faster on average in the past 3 years on a same machine" (S18, slide 50).
- **Historical "milestones" tables for a hard instance.** The same instance, zib03, is tracked from "2009: Cplex Barrier (without crossover) 139 days" to cuPDLP-C (S18, S19). [practice in talks; agent 03]
- **Candid about limits in the same deck as the results** [stated]: the DRSOM-for-deep-learning slide lists "Cons: DRSOM may over-fit the models" next to "Good potential to be a standard optimizer for deep learning!" (S10, slide 29). "Finding the optimal preconditioner seems impractical in a real-time fashion" (S16, slide 10). The last slide of S16 reads only "scalable?....".
- **Merit-function design preference** [stated, 2023]: "Typically, a single merit-function driven algorithm is preferred since it can adaptively take large step sizes as long as the merit value is sufficiently reduced, comparing to check and balance of hyper-parameters/measures of the path-following type of algorithms." (S13, slide 28, on primal-dual potential reduction with the "Tanabe-Todd-Ye primal-dual potential function"; cf. P9). Also: "Allow to take longer step-size !" (S13, slide 29). See Contradiction C4.
- Era and resources: 1989 SOLNP in Matlab; 1997 COPL codes distributed from the book page (S22). From 2019 COPT at Cardinal Operations; 2023–26 NVIDIA A6000/H100 and multi-GPU (S19). [practice, context only]

---

## 5. Judging results

- **Polynomiality is a qualitative guarantee, not a verdict on practice** (S7, p. 31, quoted in 1.1). "this criterion generally provides a qualitative statement: if a problem is polynomial solvable, then the problem is indeed relatively easy to solve regardless of the algorithm used." [stated, 1997]
- **Local rates count too:** asymptotic convergence rates "have been widely accepted by the numerical and continuous optimization community as major criteria in judging efficiency of iterative procedures." (S7, p. 4) [stated, 1997]
- **Certificates over trust (R8):** in 2026 he asks, with question marks, "How to "prove" a math theorem using (inexact) numerical Algorithms?", answers "Infeasibility Certificate: a dual solution with positive objective value", and titles two slides ""Proof" based on Algorithmic Convergence Behavior I ?" and "… II ?" (S19, slides 37–39; the context is the quantum ordered-search SDP). [stated; hedged]
- **Does proof matter to users? He gives two answers:** (a) in 2015 the theory–practice gap "bothered me" (S6); (b) in 2017, "你证明不证明，我可能还是用这个方法" **[tr.]** "whether you prove it or not, I would probably still use this method" (spoken in the voice of users of a routing tool, S24). See Contradiction C1.
- **Failures he reports himself** [stated, primary]:
  - Max-Bisection (P6): "had a provable approximation rate of 0.699 … I tried very hard but could not prove it [0.7]. Later, somebody did use a stronger SDP relaxation to make the bound 0.701, which still stands as the best today." (S3, 2009). He does not name the "somebody". Halperin & Zwick (P7) is a title-matching candidate, but its ratio was not checked here.
  - The 1982 AI detour: "那时候要搞所谓的专家系统……没有很多的数据，人家有些就总结不出来，AI 就慢慢的冷下去了。" **[tr.]** "back then it was so-called expert systems … there wasn't much data, people couldn't summarise [the rules], and AI slowly cooled." (S24; the 2025 version is S23)
  - The abandoned ambition of a universal LP algorithm (3.6).
- No retracted claim, rejected paper or published erratum was found where he discusses the failure. An errata list exists for LNLP 5th ed. (S1 link) but was not read. See Gaps.

---

## 6. Writing, books and talks

- **What a monograph should highlight** [stated, 1996]: "I chose to highlight the underlying interior-point geometry, combinatorica, and potential theory for convex inequalities. I did not intend to cover the entire progress of linear programming and interior-point algorithms during the last decade in this write-up." (S7, p. xiii). He says that less-noticed results deserve coverage: "many other complexity results were quietly established during the past several years. We try to cover these less-noticeable but significant results." (S7, p. 4)
- **What a textbook should connect** [stated, co-authored, 2021]: "One major insight is the connection between the purely analytical character of an optimization problem, expressed perhaps by properties of the optimality conditions, and the behavior of algorithms used to solve a problem." (S8, p. vii). Exercises matter: "One should attempt at least four or five exercises from each chapter." (S8, p. viii)
- **Prune what does not scale** (S8, p. ix; quoted in 2.3).
- **Talk structure** [practice in talks; agent 03]: at least five decks (S9, S10, S11, S18, S19) open with a toy example (golden section 0.618, a 5-item knapsack, a job/bid table) and a "LP giants" slide (Kantorovich, Koopmans, Dantzig, von Neumann), then theorems, then benchmark tables, and end with "Takeaways" or "Long Live Optimization". The SJTU 2024 report confirms the knapsack/ChatGPT opening (S27, secondary). No statement of his on how to write a paper was found.

---

## 7. Research organisation: students, collaborators, teams

- **How he picks and runs students** [stated, primary, 2020]: "As a professor, I like students who have a great intellectual curiosity and who are willing to look into open questions that have been studied but not solved. I challenge them to do some research around that topic, and then we hold weekly meetings and continue working together. My proudest moments are when students come into my office and tell me they have found something really eye-opening, that they've conquered a scientific mystery." (S5)
- **How he used his own advisor** [stated]: "I actively sought out his advice and showed him my research ideas." (S5, about Dantzig)
- **What mentors give** [stated, twice]: "One way mentors help the next generation of researchers is by introducing them to other people in the field. Your career isn't just your research. It's a network. The most important thing my mentors gave me, however, was an understanding of scholarship, intellectual integrity, curiosity and rigorous thinking." (S5, 2020). In 2023 the slide on Stanford's OR faculty reads: "Learnt: Scholarship, Intellectual Integrity, Academic Curiosity, and Rigorous Thinking." (S4, slide 7)
- **Community** [stated, 2009]: "I felt so lucky, at the beginning of my career, to associate with such a wonderful, unselfish, and supporting group in a very competitive research environment. Everyone was cheering for everyone else; it was like a family." (S3, about the IPM community: Todd, Anstreicher, Nemirovskii, Vavasis, …). A role model: "Pete [Veinott] has been a mentor for me. His devotion and love for OR&MS set a role model for me to follow." (S3)
- **Industry partners are named as enablers** [stated]: "I also thank the Boeing Company for picking me as a research partner." (S3, 2009)
- **Advice to students (2023 slide)** [stated]: "Be Grateful and Hopeful: no envy and nor self-doubt / Be Kind and Tolerant: love others and love yourself too / Have a Specialty: find something deep and interesting / Have a Hobby: find something to relax / Have a Faith: find something to believe" (S4, slide 12; checked on the rendered slide).
- **Sports ethos (R11)** [stated]: "I learned a lot from playing basketball: the importance of training hard, of team-work, of competitive spirit, but also playing by the rules." (S5). The 2023 slide list reads "Competitive spirit, Training hard, Team work, Take a loss, Play by rules" (S4, slide 5). The 2024 SJTU report says he "鼓励学子敢于竞争，乐于接受失败，学会团队合作，以及最重要的——遵守准则" **[tr.]** "encouraged students to dare to compete, accept failure gladly, learn teamwork, and most importantly obey the rules" (S27, secondary). The NJU report links this explicitly to research rigour, "在学术研究中坚持严谨的学术态度" **[tr.]** "keep a rigorous academic attitude in research" (S28, secondary paraphrase).
- **Research style axes** [stated as a list only]: "Individual vs Group", "In mind vs On paper" (S4, slide 15). His position on either axis is unknown.
- **Career stage and role** [stated, 2017]: "这就是到一定年龄的时候，就追求鼓励这些年轻人，不光是有一定的学术造诣，把自己的学术成果转化成技术" **[tr.]** "at a certain age one seeks to encourage young people not only to have academic attainment but to turn their results into technology" (S24).
- **Spinning students into solver builders** [stated, low provenance, 2024]: "我有两位斯坦福培养的博士生，回国建立了一个公司Cardinal Operations，杉数科技。为什么建议他们回国发展求解器？" **[tr.]** "Two PhD students I trained at Stanford went back to China and founded Cardinal Operations. Why did I advise them to go back and develop solvers?" (S26). Treat as a lead only; agent 04 should look for a better source.

---

## Contradictions (kept, not reconciled)

- **C1. Does a proof matter?** In 2015 the gap between MDP theory and practice "bothered me", and he set out to prove the methods efficient (S6, P1). In 2017 he said "谁也不知道很多理论证明的结果有什么东西" (**[tr.]** "nobody knows what many theoretical proofs are good for") and "你证明不证明，我可能还是用这个方法" (S24). The 2021 slide (S9) returns to "driven by scientific/theoretical research". So the order is 2015 pro-proof, 2017 impact-first, 2021 theory-driven. The audiences differ: department news, an industry forum, and a popular talk.
- **C2. Universal algorithm or customized pragmatism?** In 2017 he gave up the "万能的算法" (universal algorithm) for customized, pragmatic methods (S24, S25). Yet the ideal he states in 1997 is one algorithm with "both polynomiality and practical efficiency" (S7). From 2019 he leads a general-purpose solver (COPT, S1), and in 2023 his open questions still target general strongly-polynomial algorithms (S15).
- **C3. Condition numbers: attack them or avoid them?** His 1997 goal is condition-based complexity and improving the condition number (S7). His 2023 decks praise bounds with "(no condition-numbers!)" (S13) and eigenvalue methods "immune to ill-conditioning" (S12). Both positions are stated, and neither text says which comes first.
- **C4. Merit function versus path-following.** In 2023 he says "a single merit-function driven algorithm is preferred … comparing to check and balance of hyper-parameters/measures of the path-following type" (S13). But the work he highlights most (homepage, S1) is the predictor–corrector *path-following* method (P4), "implementaed in all … Commercial Solvers". A stated preference and a celebrated result point in different directions. Agent 03 should check.
- **C5. AI's black box: a virtue or a flaw?** In 2017 he likened deep learning to Chinese medicine and said it suits a culture of "不问缘由只看效果" (**[tr.]** "not asking why, only looking at effect"), with the West "比较保守" (**[tr.]** "rather conservative"), and said AI's customization "changed our thinking" (S24, S25). From 2023 to 2026 he stresses OR's explainability against AI's "Black-box" (S11) and doubts that pure data-learning can replace LP algorithms (S20). At the same time he promotes an "AI + Algorithms/Solvers" paradigm (S19, slide 48).
- **C6. Rhetoric about speed-ups.** In 1996 he "was not particular enthusiastic" about Karmarkar's "40 times faster" claim (S7). From 2021 to 2026 his own talks lead with multiplicative speed-up claims ("hundredfold or even ten thousandfold", S18). The 2020 retelling (S5) leaves out his early skepticism.
- **C7. Sources disagree on the edition.** The LNLP preface file (S8) has a "Fifth Edition" title page and an August 2021 preface, but its copyright page carries the 4th-edition ISBN/DOI (978-3-319-18842-3, 2016). Crossref confirms that the 5th-edition DOI is 10.1007/978-3-030-85450-8 (2021). The file seems to reuse old front matter; the quotes are attributed to the 2021 preface.

---

## Gaps (searched for and not found, or not read)

- **No long-form "how I do research" text.** The one list of "Research Tips" (S4, slide 15) gives dichotomies without his verdict. The spoken talk behind it (Stanford 2023; repeated at NJU on 2024-04-09 per S28) was not found as video or transcript.
- **Videos not transcribed:** the SJTU 大师讲坛 video (v.sjtu.edu.cn playDetail id 13428, linked from S27) and the Stanford Zoom recording linked from talks.html for "Recent Computational Progress on LP Solvers" (S17). Neither was tried with the subtitle scripts: the first sits on a Chinese university video platform and the second needs Zoom, and neither is likely to have downloadable subtitles. The S17 slides are mostly images; only section titles and tables were read.
- **Prize lectures:** the SIAM Optimization Prize 2014 lecture page (siam.org/meetings/op14/prize.php) returned 403. No Tseng Lectureship (ISMP 2012) slides, Farkas Prize (2006) text or Caratheodory Prize (2025) remarks were found. The 2009 von Neumann text is the acceptance speech only (S3).
- **Pages that failed:** the PKU CFCS visit page (404) and a China Daily interview page (404).
- **No statements** on refereeing standards, rejected papers or retractions, how to structure a paper, or how to pick co-authors.
- **Excluded by rule:** Zhihu, WeChat official accounts and Baidu Baike. Many Chinese interviews with Ye probably exist only there. S26 is a Sina self-media repost of unknown origin (source "管理智慧") and is used only where other sources corroborate it.
- **Read only in part:** Chapter 1 and the front matter of the 1997 monograph (S7); Chapter 10 on implementation, likely rich in stated practice, was not read. MS&E 310/314 lecture notes, the LNLP errata and the full CV (cvYYYE25.pdf) were not read for this dimension.
- **Unconfirmed:** who produced the "0.701" improvement he mentions (S3).
- **About 5 minutes without results:** English-language long interviews (OR/MS Today, IFORS or INFORMS podcasts). The one English WebSearch found only S5 and S6.

---

## Sources

Documents consulted (29):
- S1: Yinyu Ye, personal homepage, accessed 2026-09-28, https://web.stanford.edu/~yyye/. Primary.
- S2: Ye, talks index, https://web.stanford.edu/~yyye/talks.html, accessed 2026-09-28. Primary (titles only).
- S3: Ye, "Yinyu Ye's speech after winning the John von Neumann Theory Prize (10/11/2009)", https://web.stanford.edu/~yyye/Yinyu-accept-speech.pdf, with the Chinese version at https://web.stanford.edu/~yyye/yinyu-speech-Chinese.pdf. Primary.
- S4: Ye, "My Academic, Sport, and Life as a Whole" (slides, 2023; PDF created 2023-07-06; labelled 8/2023 on family.html), https://web.stanford.edu/~yyye/MyacademicSportlife.pdf. Primary.
- S5: Stanford Engineering, "Yinyu Ye: Sports led me from the rice fields to Stanford" (first-person essay), 2020-12-08, https://engineering.stanford.edu/news/yinyu-ye-sports-led-me-rice-fields-stanford. Primary (first person, institution-edited).
- S6: Stanford MS&E News, "Professor Yinyu Ye Awarded Optimization Prize: Proves Efficiency of Popular Markov Decision Process Algorithms", 2015-01-29, https://msande.stanford.edu/news/professor-yinyu-ye-awarded-optimization-prize-proves-efficiency-popular-markov-decision. Secondary (with direct quotes).
- S7: Yinyu Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley, 1997, DOI 10.1002/9781118032701. Preface ("Iowa City, 1996") and Chapter 1 read from the author's front-matter PostScript file https://web.stanford.edu/~yyye/main.ps ("June 1996, Revised January 1997"). Primary.
- S8: D. G. Luenberger and Y. Ye, *Linear and Nonlinear Programming*, 5th ed., Springer, 2021, DOI 10.1007/978-3-030-85450-8. Preface dated August 2021, https://web.stanford.edu/~yyye/LYPrefaceTablecontents.pdf. Primary (co-authored).
- S9: Ye, "From 0.618 to Mathematical Optimization" (slides; PDF created 2021-06-15), https://web.stanford.edu/~yyye/618Slides.pdf. Primary.
- S10: Ye, "Mathematical Optimization in Machine Learning/Decision-Making", Zhijiang Lab, Hangzhou, 2023-06-30, https://web.stanford.edu/~yyye/YE20230630.pdf. Primary (team-prepared deck).
- S11: Ye, "AI Big-Model and OR Mathematical Optimization", 2023-08-11, https://web.stanford.edu/~yyye/YE20230811.pdf. Primary (team-prepared deck).
- S12: Ye, "An Alternative to the Trust-Region: Homogeneous Second-Order Descent Framework", WOEC, 2023-08-18, https://web.stanford.edu/~yyye/hsodm-230818.pdf. Primary.
- S13: Ye, "Bootcamp: Interior Point Algorithms I", Simons Institute, 2023-09-01, https://web.stanford.edu/~yyye/BootcampIPM1.pdf. Primary.
- S14: B. Natura, T. Tsuchiya, Y. Ye, "Bootcamp: Interior Point Methods II", Simons Institute, 2023-09-01, https://web.stanford.edu/~yyye/BootcampIPM2.pdf. Primary (co-authored).
- S15: Ye, "Open Questions on the Markov Decision/Game Process", Simons workshop, 2023-11-29, https://web.stanford.edu/~yyye/MDPopenqs.pdf. Primary.
- S16: Ye et al., "Optimal Diagonal Preconditioner: Theory and Practice" (slides, 2023), https://web.stanford.edu/~yyye/OPTPRECOND2023-v3.pdf. Primary (mostly images; fragments only).
- S17: Ye, "Recent Computational Progress on Linear Programming Solvers" (slides; PDF created 2024-02-14), https://web.stanford.edu/~yyye/LPProgress-slides.pdf. Primary (mostly images; video not watched).
- S18: Ye, "Mathematical Optimization in the Era of AI", INFORMS International 2025, Singapore (PDF created 2025-07-20), https://web.stanford.edu/~yyye/MPinEraofAI20250720.pdf. Primary (team-prepared deck).
- S19: Ye, "Mathematical Programming in the Era of AI", HORIZONS 2026, CEI VinUni, 2026-07-02, https://web.stanford.edu/~yyye/20260701Solver.pdf. Primary (PDF author metadata: Dongdong Ge).
- S20: Ye, "Can Pure Offline Data Learning Replace Linear Programming Algorithms?" (note), 2026-09-23, https://web.stanford.edu/~yyye/LPsolutionsensitivity.pdf. Primary.
- S21: Ye, very short bio 2025, https://web.stanford.edu/~yyye/VeryShortbio2025.pdf. Primary.
- S22: Ye, book information page for *Interior-Point Algorithms* (software distribution), https://web.stanford.edu/~yyye/book.html. Primary.
- S23: 中新社 (王宗汉, 裴心语), "东西问丨叶荫宇：AI与OR，共促人类未来", 2025-03-06, https://www.chinanews.com/gn/2025/03-06/10378972.shtml. Primary (edited interview Q&A).
- S24: 雷峰网 (王金许), "运筹学教授叶荫宇：作为 AI 基石，优化算法如何在实际中应用？", 2017-06-27; edited transcript of Ye's talk 《优化算法的思想及应用》 at the 2017 AI 大师论坛, Beijing, 2017-06-24, https://www.leiphone.com/category/industrynews/DwILBnyYJPMfv7WX.html. Primary (edited transcript).
- S25: 凤凰网财经 (from 雷锋网), "集齐叶荫宇、蓝光辉、陈溪、李建、王子卓的大牛圆桌会，关于算法优化他们都聊了什么", 2017-06-26, https://finance.ifeng.com/a/20170626/15486483_0.shtml. Secondary (report plus edited Q&A).
- S26: 新浪财经 self-media (source "管理智慧"), "斯坦福大学杰出教授叶荫宇：AI智能决策的真正威力", 2024-11-10, https://finance.sina.com.cn/wm/2024-11-10/doc-incvpuqs1958958.shtml. Secondary, low provenance.
- S27: 上海交通大学研究生院, "斯坦福大学李国鼎讲席教授叶荫宇做客第218期大师讲坛", 2024-04-28, https://www.gs.sjtu.edu.cn/post/detail/Z3MyMDMz. Secondary.
- S28: 南京大学工程管理学院, "《我的学术、体育以及人生发展》——叶荫宇教授赴仙林校区与我院本科生开展交流", 2024-04-18, https://sme.nju.edu.cn/5f/15/c2039a679701/pagem.htm. Secondary.
- S29: 香港中文大学（深圳）数据科学学院, "活动回顾 | 叶荫宇教授做客港中大（深圳）大师讲堂", 2023-04-06, https://sds.cuhk.edu.cn/event/942. Secondary (only the closing line on sports and dreams was used).

Papers named above (each identifier checked by tool in this run):
- P1: Y. Ye, "The Simplex and Policy-Iteration Methods Are Strongly Polynomial for the Markov Decision Problem with a Fixed Discount Rate", *Mathematics of Operations Research*, 2011, DOI 10.1287/moor.1110.0516.
- P2: S. A. Vavasis and Y. Ye, "A primal-dual interior point method whose running time depends only on the constraint matrix", *Mathematical Programming*, 1996, DOI 10.1007/BF02592148.
- P3: Y. Ye, M. J. Todd and S. Mizuno, "An O(√nL)-Iteration Homogeneous and Self-Dual Linear Programming Algorithm", *Mathematics of Operations Research*, 1994, DOI 10.1287/moor.19.1.53.
- P4: S. Mizuno, M. J. Todd and Y. Ye, "On Adaptive-Step Primal-Dual Interior-Point Algorithms for Linear Programming", *Mathematics of Operations Research*, 1993, DOI 10.1287/moor.18.4.964.
- P5: E. Delage and Y. Ye, "Distributionally Robust Optimization Under Moment Uncertainty with Application to Data-Driven Problems", *Operations Research*, 2010, DOI 10.1287/opre.1090.0741.
- P6: Y. Ye, "A .699-approximation algorithm for Max-Bisection", *Mathematical Programming*, 2001, DOI 10.1007/PL00011415.
- P7: E. Halperin and U. Zwick, "A unified framework for obtaining improved approximation algorithms for maximum graph bisection problems", *Random Structures & Algorithms*, 2002, DOI 10.1002/rsa.10035. This is a candidate only; the text was not read.
- P8: Y. Ye, "On the complexity of approximating a KKT point of quadratic programming", *Mathematical Programming*, 1998, DOI 10.1007/BF01581726.
- P9: M. J. Todd and Y. Ye, "A Centered Projective Algorithm for Linear Programming", *Mathematics of Operations Research*, 1990, DOI 10.1287/moor.15.3.508.
- P10: C. Zhang, D. Ge, C. He, B. Jiang, Y. Jiang, Y. Ye, "DRSOM: A Dimension Reduced Second-Order Method", arXiv:2208.00208 (2022).
- P11: C. Zhang, D. Ge, C. He, et al., "A homogeneous second-order descent method for nonconvex optimization", arXiv:2211.08212 (2022).
- P12: H. Lu, J. Yang, H. Hu, et al. (incl. Y. Ye), "cuPDLP-C: A Strengthened Implementation of cuPDLP for Linear Programming by C language", arXiv:2312.14832 (2023).
- P13: X. Li, C. Sun, Y. Ye, "The Symmetry between Arms and Knapsacks: A Primal-Dual Approach for Bandits with Knapsacks", ICML 2021, PMLR vol. 139, https://proceedings.mlr.press/v139/li21s.html.
