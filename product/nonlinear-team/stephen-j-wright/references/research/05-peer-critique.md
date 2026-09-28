# 05 · Peer Critique: Blind Spots, Limits and Contested Judgements (Stephen J. Wright)

> **Researcher:** Stephen J. Wright (UW-Madison Computer Sciences; Argonne MCS 1990–2001), living.
> **Dimension:** research agent 05 of 06, peer critique (nuwa research-craft Phase 1). The job is to find where others (and Wright himself, looking back) showed his methods to be limited, fragile or wrong, and to record whether and how he answered.
> **Research date:** 2026-09-28. **Sources consulted:** 46 (37 primary, 9 secondary), listed under "Sources". **WebSearch calls:** 2.
> **Local corpus:** `references/sources/{papers,essays,software}` were empty. `talks/` holds only the UW oral-history transcript that agent 02 saved in this run, which is not user-supplied. Nothing here is marked "from user-supplied material". `private/` was not opened.
> **How items were checked:** every paper named below carries a DOI, an arXiv id, or venue + year + full title, checked in this run against Crossref, arXiv abstract pages, OpenAlex (API key), the zbMATH Open API or the PDF header. Quotations come from full texts I downloaded and read in this run: arXiv PDFs, author-hosted copies, Optimization Online preprints and the NeurIPS press PDF. Page = PDF page of the version named in Sources. Ligatures (ﬁ, ﬂ) and letter-spacing are normalized; nothing else is changed. Items marked "metadata only" were identified but not read.
> **Tags:** [stated] = Wright said or wrote it; [practice] = what his papers, code and records show he did; [observed] = what others (critics, benchmarkers, reviewers) wrote about his work; [inferred] = my reading, not in any source. P = primary, S = secondary.
> **Cross-references:** the self-corrections Wright published himself (errata, corrigenda, NIPS rebuttals) are documented in `03-process-evidence.md` §2. They are only summarized in §7 below and are not re-read here.

---

## 0. Summary

Six critique threads were found. None of them is a public dispute in which Wright wrote a comment or reply. **No published comment/rejoinder by Wright, no failed replication in the strict sense, no retraction and no public rejected paper were found.** The criticism of his work comes as follow-up papers that weaken assumptions, benchmark studies, and rival analyses.

| # | Target (Wright's work) | Main critics | Nature of the critique | Answered by Wright? |
|---|---|---|---|---|
| 1 | Asynchronous parallel analyses: Hogwild! (2011), AsySCD (2014–15), CD survey (2015) | Mania, Pan, Papailiopoulos, **Recht**, Ramchandran & Jordan; De Sa, Zhang, Olukotun & **Ré**; Leblond, Pedregosa & Lacoste-Julien; Sun, Hannah & Yin; Cannelli, Facchinei, Kungurtsev & Scutari; Nguyen et al.; Zhang, Hsieh & Akella | The model of asynchrony is idealized (consistent reads, uniform processing times, delay independent of block, bounded gradients, τ ≈ P). The hardware scaling claim is weaker on NUMA machines | **Partly.** He fixed consistent reads himself (2014). No paper answering the delay-independence or overlap-bound critiques was found. In 2020 he framed later work as "extended" |
| 2 | Stabilized SQP and degenerate NLP (1998–2005) | Hager; Fernández & Solodov; Izmailov & Solodov; Gill & Robinson; Gill, Kungurtsev & Robinson | The theory is local only, its assumptions were later weakened, and in globalized practice sSQP is still often attracted to critical multipliers | **No.** The line ended around 2005–06, before the main critiques (2009–2017). His 2026 return to degeneracy does not cite them |
| 3 | GPSR (2007) and SpaRSA (2009) sparse solvers | Becker, Bobin & Candès (NESTA benchmark) | GPSR degrades sharply with dynamic range and fails on 80/100 dB signals. SpaRSA is not competitive on approximately sparse signals | **Yes, before publication.** Wright commented on the draft, got a better GPSR version used and asked for SpaRSA to be tested |
| 4 | Practical IPM choices (Mehrotra-type correctors in PCx and OOQP; the book) | Salahi, Peng & Terlaky; Cartis | Mehrotra-type heuristics can take tiny steps or fail to converge | Not addressed to Wright personally. No reply found. In 2025 he stated the theory–practice gap himself |
| 5 | Coordinate-descent orderings | Sun & Ye (Ye is a team member) | Cyclic CD can be O(n²) slower than randomized CD | **Yes.** Lee & Wright (2016/2019) explain why random permutations avoid the worst case. Later co-authored with a rival group (Gürbüzbalaban, Ozdaglar, Vanli) |
| 6 | Complexity-driven Newton-CG methods (2018–2021) | Wright himself (2025) | The complexity modifications do not help practice, and the bounds are pessimistic | Self-critique (no outside critic found) |

A further rival analysis runs the other way. In 2001 Wright criticized Forsgren, Gill and Shinnerl (Gill is a team member) for a pivot-order assumption in IPM stability analysis (§5.2). No reply from them was found.

---

## 1. Thread 1: the asynchronous-parallel analyses (Hogwild!, AsySCD, the CD survey)

**Era and resources.** Hogwild! (Niu, Recht, Ré & Wright, arXiv:1106.5730; NIPS 2011) was a four-author UW collaboration run on a two-socket Xeon workstation (see 03 §1.2). The critiques came 2015–2020 from ML and optimization groups with 10–40-core machines and clusters. In the group paper the systems side belonged to Ré and Niu. Wright's own statement says the analysis was his, with Recht's sparsity assumption added (§1.8).

### 1.1 Consistent reads, single-coordinate updates, uniform processing times (Mania et al.)

- **Critic and source** [observed, P]: Mania, Pan, Papailiopoulos, Recht, Ramchandran & Jordan, "Perturbed Iterate Analysis for Asynchronous Stochastic Optimization", arXiv:1507.06970v2; SIAM J. Optim. 27 (2017) 2202–2229, 10.1137/16M1057000.
  - "In [1], the authors analyzed a variant of Hogwild! in which several simplifying assumptions were made." ([1] = Niu, Recht, Ré & Wright; p. 4)
  - They list three: only a single coordinate per hyperedge is updated, consistent reads are assumed, and "the authors make an implicit assumption on the uniformity of the processing times of cores (explained in the following), that does not generically hold in practice." (p. 5)
  - "As we show in the current paper, however, these simplifications are not necessary to obtain a convergence analysis." (p. 5)
  - Their comparison section adds: "We order the samples by the order in which they were sampled, not by completion time. [...] This is unlike [1], where there is an implicit assumption of uniformity with respect to processing times." (p. 9)
- **Who the critic is** [observed, P]: Recht, a Hogwild! co-author, is a co-author of the critique. The correction came from inside the original team, not from a rival school.
- **Answered?** For ASCD, Mania et al. say the algorithm "has been previously analyzed in [5, 21]" (Liu et al.; Liu & Wright) and re-derive it "under the same assumptions made for Hogwild!" (p. 10). Wright is not an author, and no reply by Wright was found.

### 1.2 Sparsity and bounded gradients (De Sa et al.; Nguyen et al.)

- [observed, P] De Sa, Zhang, Olukotun & Ré, "Taming the Wild: A Unified Analysis of Hogwild!-Style Algorithms", arXiv:1506.06438v2 (2015):
  - "For the convex case, HOGWILD! requires strict sparsity assumptions. Using our techniques, we are able to relax these assumptions and still derive convergence rates." (p. 2)
  - "This result is more general than the result in Niu et al. [17]. The main differences are: that we make no assumptions about the sparsity structure of the gradient samples" (p. 5)
  - Ré, another Hogwild! co-author, is again on the critique.
- [observed, P] Nguyen, Nguyen, van Dijk, Richtárik, Scheinberg & Takáč, "SGD and Hogwild! Convergence Without the Bounded Gradients Assumption", ICML 2018 (PMLR 80:3747–3755), arXiv:1802.03801v2.
  - They list (Recht et al., 2011), i.e. Hogwild!, among analyses that assume uniformly bounded stochastic gradients: "However, this assumption is clearly false if F is strongly convex." (p. 2)
  - On Hogwild!: the method "requires the assumption of consistent vector reads together with the bounded gradient assumption to prove convergence." (p. 5)
  - [inferred] This is an **internal-consistency critique**: the Hogwild! theorem combines strong convexity with an assumption that cannot hold globally under strong convexity.
- **Answered?** No reply by Wright found.

### 1.3 The "after write" labeling and delay–sample dependence (Leblond, Pedregosa & Lacoste-Julien)

- [observed, P] Leblond, Pedregosa & Lacoste-Julien, "Improved Asynchronous Parallel Optimization Analysis for Stochastic Incremental Methods", J. Mach. Learn. Res. 19 (2018) 1–68 (PDF header), arXiv:1801.03749v3. It extends "ASAGA: Asynchronous Parallel SAGA", AISTATS 2017, arXiv:1606.04809.
  - "We call the “after write” approach the standard global labeling scheme used in Niu et al. (2011) and re-used in all the later papers that we mentioned in the related work section, with the notable exceptions of Mania et al. (2017) and Duchi et al. (2015)." (p. 6)
  - On the dependence this labeling creates between the sample and the labeled iterate: "This assumption seems overly strong in the context of potentially heterogeneous factors fi’s, and is thus a fundamental flaw for analyzing non-uniform asynchronous computation that has mostly been ignored in the recent asynchronous optimization literature." (p. 6)
  - On Mania et al.'s own fix: "However, this “fix” can only be applied in a restricted setup: only for the Hogwild algorithm, with the assumption that the norm of the gradient is uniformly bounded." (p. 6)
  - [inferred] The critics did not settle the matter among themselves either.

### 1.4 The overlap bound τ is not "a modest multiple of P" (Leblond et al. vs the 2015 survey)

- [stated, P] Wright, "Coordinate Descent Algorithms" (arXiv:1502.04759v1; Math. Program. 151 (2015) 3–34, 10.1007/s10107-015-0892-3): "If all processors are performing their updates at approximately the same rates, we could expect τ to be a modest multiple of P — perhaps τ = 2P or τ = 3P, to allow a safety margin for occasional delays." (p. 27)
- [observed, P] Leblond et al. (JMLR 2018) measured the overlap τ for Asaga and Hogwild on three data sets and up to 40 cores:
  - "The results we observe are order of magnitude bigger than p, indicating that τ can indeed not be dismissed as a mere proxy for the number of cores, but has to be more carefully analyzed." (p. 37)
  - "though τ appears to depend linearly on p, it actually depends on several other factors (notably the data sparsity distribution) and can be orders of magnitude bigger than p in real-life experiments." (p. 12)
- [inferred] Wright's statement was conditional ("If all processors ... approximately the same rates") and was about AsySCD, while the measurements were for Asaga and Hogwild. It is still the clearest case where an expectation in his writing was contradicted by later measurement. Kept as a contradiction (see Contradictions §1).

### 1.5 Delay independent of the updated block; uniformly random blocks (Sun–Hannah–Yin; Cannelli et al.)

- [observed, P] Sun, Hannah & Yin, "Asynchronous Coordinate Descent under More Realistic Assumptions", NeurIPS 2017 (venue confirmed via OpenAlex), arXiv:1705.08494v2.
  - Their "previous analyses [12, 13, 15, 9]" are [12] Liu & Wright SIOPT 2015 and [13] Liu, Wright, Ré, Bittorf & Sridhar JMLR 2015. The independence of block index and delay "is unrealistic in practice." (p. 2)
  - Evidence from a 2-node, 32-thread cluster: "Over 2000 epochs, blocks 0, 1, and 15 have average delays of 351, 115, and 28, respectively." (p. 2)
  - Their related-work section: "Our work extends the theory on asynchronous BCD algorithms such as [17, 13, 12]. However, their analysis relies the independence assumption and assume bounded delays." ([17] = Hogwild!; grammar as in the original; p. 4)
  - They also criticize the other critics' remedy. Enforcing independence by relabeling "creates other artificial implementation requirements that may waste computational resources" (p. 4).
- [observed, P] Cannelli, Facchinei, Kungurtsev & Scutari, "Asynchronous parallel algorithms for nonconvex optimization", Math. Program. 184 (2020) 121–154, 10.1007/s10107-019-01408-w, arXiv:1607.04818v3.
  - **Praise and critique in one paper.** Asynchronous BCD "has been introduced and studied in the seminal work [21], which motivated and oriented much of subsequent research in the field" ([21] = Liu & Wright SIOPT 2015; p. 4).
  - But: "All current probabilistic models for asynchronous BCD methods are based on the (implicit or explicit) assumption that the random variables ik and dk are independent; this greatly simplifies the convergence analysis." (p. 4)
  - And: "Another unrealistic assumption often made in the literature [9, 21, 22, 25] is that the block-indices ik are selected uniformly at random." ([21] Liu & Wright, [22] Liu et al., [25] Niu et al.; p. 5)
  - Their measurement on a 10-core Xeon: blocks tied to sparse Hessian rows had delays 0–3 while the other blocks had delays above 20 (p. 5).
- [practice, P] Wright's own survey states the assumption plainly: Liu and Wright's version has "each update component ik is chosen independently and randomly with equal probability" (arXiv:1502.04759v1, p. 27).
- **Answered?** [practice, P; inferred on "not answered"] Wright's DBLP record (pid `w/StephenJWright`, list saved by agent 01 in this run) has no asynchronous-CD or asynchronous-SGD paper after Liu & Wright 2015. His later coordinate work is on orderings, variance reduction and Langevin sampling. I found no paper in which he takes up the delay-dependence critique. *Optimization for Data Analysis* (2022) was **not read** on this point.

### 1.6 Hardware: NUMA scaling (Zhang, Hsieh & Akella)

- [observed, P] Zhang, Hsieh & Akella, "HogWild++: A New Mechanism for Decentralized Asynchronous Stochastic Gradient Descent", ICDM 2016, 629–638, 10.1109/ICDM.2016.0074 (author PDF): "We show that the scalability of HOGWILD! on modern multi-socket CPUs is severely limited, especially on NUMA (Non-Uniform Memory Access) system, due to the excessive cache invalidation requests and false sharing." (p. 1)
- Their code README says HogWild++ "is based on the HogWild! v03a code" (github.com/huanzhang12/hogwildpp README). The critique was built on the original release.
- [inferred] **Era effect**: the 2011 claim ("outperforms alternative schemes that use locking by an order of magnitude", arXiv:1106.5730 abstract) was made on a 2011 two-socket workstation. The limit shows up on the multi-socket NUMA machines of 2016.

### 1.7 What Wright did fix himself: consistent reads

- [practice, P] Liu & Wright, "Asynchronous Stochastic Coordinate Descent: Parallelism and Convergence Properties", arXiv:1403.3862 (Mar 2014); SIAM J. Optim. 25 (2015) 351–376, 10.1137/140961134. The abstract says: "In contrast to previous analyses, our model of asynchronous computation accounts for the fact that components of the unknown vector may be written by some cores simultaneously with being read by others."
- [stated, P] In the 2015 survey he names the weaker assumption of his own group's earlier paper. The earlier analysis in [28] (Liu, Wright, Ré, Bittorf & Sridhar, JMLR 2015; arXiv:1311.1873) "made a stronger assumption on x̂k". Then: "However, the assumption may not always hold, since some parts of x in memory may be altered by some cores as they are being read by another core, a phenomenon referred to in [27] as “inconsistent reading.”" (arXiv:1502.04759v1, p. 29)
- [inferred] **Pattern**: he corrects the assumption that his own implementations showed to be false (inconsistent reads on a multicore). He did not take up assumptions whose failure only shows on other hardware or in heterogeneous workloads (delay–block dependence, τ ≫ P, NUMA).

### 1.8 How Wright frames the aftermath (2020)

- [stated, P] NeurIPS 2020 Test-of-Time press statement for Hogwild!. It is written in the first person of the analyst ("Ben had talked to me the previous year after I did some analysis of a parallel SGD scheme"); [inferred] that makes it Wright's voice.
  - "Ben made a crucial addition to the analysis - an assumption that each model update affected only a small part of the model - and suddenly we had theoretical results showing that the asynchronous scheme could (even in theory) achieve a speedup that is linear in the number of parallel processors, to a constant factor" (p. 1)
  - "our analysis has subsequently been extended in many ways, by us and many others." (p. 2)
- [inferred] The statement calls the sparsity assumption the key to the theorem, and that is exactly what De Sa et al. and Leblond et al. later relaxed. It describes the later literature as extensions. Leblond et al. call part of the shared framework "a fundamental flaw". Both are kept (Contradictions §2).
- [observed, S] Around the award, a news piece reports that Ré was warned after Hogwild! that he was "making a career mistake because you're going into a new, weird area" (Stanford HAI, S. Lynch, 8 Dec 2020, via WebFetch summary). This is about Ré's career, not a critique of Wright's analysis. It is recorded only as context.

---

## 2. Thread 2: stabilized SQP and degenerate NLP (1998–2005)

**Era and resources.** Solo theory papers from Argonne and early UW, with MATLAB test codes (see 01 S3, 03 §4). The critics are Russian/Brazilian variational-analysis groups (Izmailov, Solodov, Fernández, Fischer) and the UCSD SQP school (Gill, Robinson, Kungurtsev). Their numerical work used AMPL with MINOS and SNOPT, MATLAB sSQP and the DEGEN test set.

### 2.1 Weaker assumptions for the same local result (Hager; Fernández & Solodov; Izmailov & Solodov)

- [practice, P; metadata only] Follow-ups on Wright's "Superlinear Convergence of a Stabilized SQP Method to a Degenerate Solution" (Comput. Optim. Appl. 11 (1998) 253–275, 10.1023/A:1018665102534):
  - Hager, "Stabilized Sequential Quadratic Programming", Comput. Optim. Appl. 12 (1999) 253–273, 10.1023/A:1008640419184.
  - Fernández & Solodov, "Stabilized sequential quadratic programming for optimization and a stabilized Newton-type method for variational problems", Math. Program. 125 (2010) 47–73, 10.1007/s10107-008-0255-4.
  - Izmailov & Solodov, "Stabilized SQP revisited", Math. Program. 133 (2012) 93–120, 10.1007/s10107-010-0413-3.
- **Not read**: abstracts and full texts were unavailable (publisher elided the abstracts in Semantic Scholar and OpenAlex, zbMATH content is licence-blocked, and there was no open copy). I therefore make **no claim** about exactly which assumption each paper weakened.
- [stated, P, via 01 S3] Wright's own 2002 paper says his result was "later enhanced by Hager" (P699, p. 1, quoted in 01). He acknowledged the improvement in print.

### 2.2 Local only: the globalization gap (Gill & Robinson; Gill, Kungurtsev & Robinson)

- [observed, P] Gill & Robinson, "A Globally Convergent Stabilized SQP Method", SIAM J. Optim. 23 (2013) 1983–2010, 10.1137/120882913. Published abstract (Crossref): "Existing stabilized SQP methods are essentially local in the sense that both the formulation and analysis focus on the properties of the methods in a neighborhood of a solution." The preprint (Optimization Online 2012/06/3518, p. 2) cites Wright [41, 42], Hager [28] and Oberlin & Wright [35] for these existing methods.
- [observed, P] Gill, Kungurtsev & Robinson, "A stabilized SQP method: superlinear convergence", Math. Program. 163 (2017) 369–410, 10.1007/s10107-016-1066-7 (preprint Optimization Online 2014/07/4417). The companion paper is "A stabilized SQP method: global convergence", IMA J. Numer. Anal. 37 (2017) 407–443, 10.1093/imanum/drw004 (metadata only).
  - A second implicit criticism of the classical local theory: "This rate of convergence is obtained without the need to solve an indefinite QP subproblem, or impose restrictions on which local minimizer of the QP is found. For example, it is not necessary to compute the QP solution closest to the current solution estimate." (preprint p. 40)
  - [inferred] The QP-solution-selection issue is a known assumption in local sSQP theory. The preprint does not attribute it to Wright at that sentence.
  - They re-ran Wright's own test set: "Of the ten cases, pdSQP2 converges superlinearly on seven problems, converges linearly on two problems, and fails to converge on one problem. These results appear to be similar to those obtained by Mostafa, Vicente and Wright using their code sSQPa" (p. 38). That test set is from Mostafa, Vicente & Wright, "Numerical Behavior of a Stabilized SQP Method for Degenerate NLP Problems", LNCS 2861 (2003) 123–141, 10.1007/978-3-540-39901-8_10. This is an outside check that **confirmed** the 2003 numerical picture rather than overturning it.
- **Answered?** [practice, P; inferred] Wright's own globalization work stops at 2005–06. His 2002 paper set globalization aside explicitly ("we focus on the local properties of the SQP approach and ignore the various algorithmic devices used to ensure global convergence", P699, p. 2, quoted in 01). The globalized stabilized SQP was built by the Gill school, not by Wright.

### 2.3 Critical multipliers: the local theory does not survive globalized practice (Izmailov & Solodov)

- [observed, P] Izmailov & Solodov, "On attraction of linearly constrained Lagrangian methods and of stabilized and quasi-Newton SQP methods to critical multipliers", Math. Program. 126 (2011) 231–257, 10.1007/s10107-009-0279-4 (journal PDF hosted at cs.wisc.edu/~solodov).
  - Abstract: "Experiments also show that in the stabilized version of SQP the attraction phenomenon still exists but appears less persistent." (p. 232)
  - Their sSQP (Wright [19] and others) had to be "supplied with the globalization strategy based on linesearch for a nonsmooth exact penalty function" (p. 253).
  - Results: "the effect of attraction to critical multipliers still exists [...] but the attraction is much less persistent. The runs clearly split into two groups." (p. 255)
  - Verdict: "Thus, by itself, sSQP does not seem to be a reliable tool for avoiding the effect of attraction." (p. 256)
- [observed, P] Gill, Kungurtsev & Robinson (preprint p. 39) summarize the state of play: stabilized SQP subproblems are used "as a way of accelerating local convergence in the presence of critical multipliers. However, such algorithms have had mixed results in practice (see, e.g., Izmailov [25])."
- [practice, P; metadata only] The fullest statement is an invited TOP discussion paper: Izmailov & Solodov, "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it", TOP 23 (2015) 1–26, 10.1007/s11750-015-0372-1.
  - Comments came from A. Fischer (10.1007/s11750-015-0368-x), J. M. Martínez (10.1007/s11750-015-0369-9), B. S. Mordukhovich (10.1007/s11750-015-0370-3) and D. P. Robinson (10.1007/s11750-015-0371-2), with a rejoinder (10.1007/s11750-015-0373-0). **Wright is not among the discussants.** None of these was read.
- **Answered?** [practice, P; inferred] No. Wright's degenerate-NLP line ends before the critical-multiplier papers (2009–2015). His 2026 return to degeneracy (Lee & Wright, "Revisiting superlinear convergence of proximal Newton-like methods to degenerate solutions", arXiv:2602.10470) treats regularized problems and generalized equations under Hölderian error bounds. A text search of that PDF finds no mention of Izmailov, Solodov, Hager, Fischer, "critical multiplier" or "stabilized". [inferred] The critique landed after he had moved on, and he did not re-enter that debate.
- **Limit of applicability** [inferred from the above]: "superlinear convergence to a degenerate solution" in Wright's sense is a statement about a neighbourhood of a primal-dual point with a suitable multiplier. Once the method is globalized, whether it reaches that neighbourhood is not covered by his theory.

---

## 3. Thread 3: sparse-recovery solvers (GPSR, SpaRSA) in outside benchmarks

**Era and resources.** 2009, MATLAB codes. The benchmark ran "on a dual core MacPro G5" (NESTA p. 23). GPSR is Figueiredo, Nowak & Wright, IEEE JSTSP 1 (2007) 586–597, 10.1109/JSTSP.2007.910281. SpaRSA is Wright, Nowak & Figueiredo, IEEE TSP 57 (2009) 2479–2493, 10.1109/TSP.2009.2016892.

- [observed, P] Becker, Bobin & Candès, "NESTA: A Fast and Accurate First-order Method for Sparse Recovery", arXiv:0904.3367v1; SIAM J. Imaging Sci. 4 (2011) 1–39, 10.1137/090756855. Only the arXiv v1 was read; the published version may differ.
  - GPSR: "GPSR performs well in the case of low-dynamic range signals; its performance, however, decreases dramatically as the dynamic range increases" (p. 23). Table 5.2 "shows that it does not converge for 80 and 100 dB signals" (p. 24).
  - GPSR with continuation "does much better than the regular GPSR version on the high dynamic range signals, though it is slower than NESTA with continuation by more than a factor of 10." (p. 24)
  - SpaRSA: "SpaRSA performs well at low dynamic range, comparable to NESTA, and begins to outperform GSPR with continuation as the dynamic range increases, although it begins to underperform NESTA with continuation in this regime." ("GSPR" as in the original; p. 24)
  - On approximately sparse signals: "FISTA and SpaRSA converge for these tests, but are not competitive with the best methods." (p. 26). And: "One conclusion from these tests is that SPGL1, Bregman and NESTA (with continuation) are the only methods dealing with approximately sparse signals effectively." (p. 26)
- **How Wright answered (before publication)** [observed, P]:
  - Acknowledgements: "We are grateful to Stephen Wright for his comments on an earlier version of this paper, for suggesting to use a better version of GPSR, and encouraging us to test SpaRSA. Thanks Stephen!" (p. 35)
  - The tuning came from the GPSR side: "per the recommendation of one of the GPSR authors to increase performance, the number of continuation steps was set to 40 [...] In addition, the code itself was tweaked a bit; in particular, the stopping criteria for continuation steps (other than the final step) was changed. Future releases of GPSR will probably contain a similarly updated continuation stopping criteria." (p. 19)
  - SpaRSA parameters were likewise set "as per the recommendations of one of the SpaRSA authors" (p. 20).
- [inferred] **Response style**: he did not dispute the rival benchmark. He made sure his code was run at its best and that his newer method was included. The benchmark then confirmed the weakness he had already admitted: GPSR's own abstract says "the performance of GP methods tends to degrade as the regularization term is de-emphasized" (JSTSP 2007, quoted in 01 S3). **Caveat**: the numbers depend on author-supplied tuning and a patched code, so they are not a neutral default-settings comparison.

---

## 4. Thread 4: practical IPM heuristics (Mehrotra-type correctors)

**Relation to Wright** [practice, P, via 03]: PCx (Czyzyk, Mehrotra, Wagner & Wright, Optim. Methods Softw. 11 (1999) 397–430, 10.1080/10556789908805757) and OOQP (Gertz & Wright, ACM TOMS 29 (2003) 58–81, 10.1145/641876.641880) rely on Mehrotra and Gondzio correctors. The OOQP paper says these "have proved to be the most effective methods for linear programming problems and in our experience are just as effective for QP" (quoted in 03 §1).

- [observed, P] Salahi, Peng & Terlaky, "On Mehrotra-Type Predictor-Corrector Algorithms", SIAM J. Optim. 18 (2007) 1377–1397, 10.1137/050628787 (preprint Optimization Online 2005/03/1104).
  - "By an example we show that in this variant the usual Mehrotra-type adaptive choice of the parameter µ might force the algorithm to take many small steps to keep the iterates in a certain neighborhood of the central path" (preprint p. 1).
  - Their proofs lean on Wright's book (Lemma 5.3 and Theorem 3.2 of *Primal-Dual Interior-Point Methods* are cited), so the critique is framed inside his theory.
- [observed, P; abstract only] Cartis, "Some disadvantages of a Mehrotra-type primal-dual corrector interior point algorithm for linear programming", Appl. Numer. Math. 59 (2009) 1110–1119, 10.1016/j.apnum.2008.05.006. Preprint abstract (Oxford NA TR 04/27, Optimization Online 2005/02/1062): "We present examples, however, that show that the PDC algorithm may fail to converge to a solution of the LP problem, in both exact and finite arithmetic, regardless of the choice of stepsize that is employed." Full text not read (the PDF uses Type-3 fonts that did not extract).
- **Answered?** [stated, P] Not addressed to him, and no reply was found. In 2025 he stated the gap himself: "the most successful practical primal-dual approach is closest to the methods with O(n² log ϵ) complexity; methods with the slightly better O(n^1/2 log ϵ) bound are somewhat slower in practice." (arXiv:2510.15734v2, p. 9)
- [inferred] His practice is to trust the heuristic that wins on benchmarks (PCx, OOQP) while keeping the theory for the simpler variants. The critics show that this leaves the production heuristic without a guarantee. That is a known and accepted blind spot of the IPM school, not specific to Wright.

---

## 5. Thread 5: rival results where Wright answered, and where he was the critic

### 5.1 Coordinate-descent orderings: answered by analysis, then by collaboration

- [observed, P] Sun & Ye, "Worst-case complexity of cyclic coordinate descent: O(n²) gap with randomized version", Math. Program. 185 (2021) 487–520, 10.1007/s10107-019-01437-5, arXiv:1604.07130: "It implies that in the worst case C-CD can indeed be O(n²) times slower than R-CD" (arXiv abstract). Ye is a member of this team.
- [stated, P] Lee & Wright, "Random permutations fix a worst case for cyclic coordinate descent", IMA J. Numer. Anal. 39 (2019) 1246–1275, 10.1093/imanum/dry040, arXiv:1607.08320. The abstract:
  - admits the known gap: "Known convergence guarantees are weaker for CCD and RPCD than for RCD, though in most practical cases, computational performance is similar among all these variants."
  - engages the critique by name: "a recent paper by \cite{SunY16a} has explored the poor behavior of CCD on functions of this type. The RPCD approach performs well on these functions, even better than RCD in a certain regime. This paper explains the good behavior of RPCD with a tight analysis." (the raw \cite is in the arXiv abstract)
- [practice, P] He followed up with Wright & Lee, "Analyzing random permutations for cyclic coordinate descent", Math. Comp. 89 (2020) 2217–2248, 10.1090/mcom/3530. He also co-authored with a group that had published a competing ordering analysis: Gürbüzbalaban, Ozdaglar, Vanli & Wright, "Randomness and permutations in coordinate descent methods", Math. Program. 181 (2020) 349–376, 10.1007/s10107-019-01438-4.
- [inferred] **Response style**: he treats a worst-case example as a new problem to analyse, not as an attack. He answers with a sharper theorem for the practical variant (random permutations) and then with joint work.

### 5.2 IPM linear-algebra stability: Wright as critic of a team member's school

- [stated, P] Wright, "Effects of Finite-Precision Arithmetic on Interior-Point Methods for Nonlinear Programming", SIAM J. Optim. 12 (2001) 36–78, 10.1137/S1052623498347438, arXiv:math/0103102v1:
  - Related work by Forsgren, Gill and Shinnerl "deals with one formulation of the step equations for the nonlinear programming problem—the so-called augmented form treated here in Section 6—but makes assumptions on the pivot sequence that do not always hold in practice." (p. 2)
  - "a key assumption of the analysis of Forsgren, Gill, and Shinnerl [9, Theorem 4.4]—namely, that all the diagonals of size Θ(µ^-1) are chosen as 1×1 pivots before any of the other diagonals are chosen—may not be satisfied by the Bunch-Kaufman procedure." (p. 33)
- Target: Forsgren, Gill & Shinnerl, "Stability of Symmetric Ill-Conditioned Systems Arising in Interior Methods for Constrained Optimization", SIAM J. Matrix Anal. Appl. 17 (1996) 187–211, 10.1137/S0895479894270658 (metadata only, **not read**).
- **Answered?** No reply by Forsgren, Gill or Shinnerl was found (not searched in depth; see Gaps). [inferred] For the roundtable: Wright's objection is the same one he meets in thread 1, an analysis assumption about the order in which things happen that real software does not guarantee. Here he raises it; there it is raised against him.

---

## 6. Thread 6: complexity-driven Newton methods, a self-critique

- [stated, P] Wright, "Optimization in Theory and Practice", arXiv:2510.15734v2 (2025). On Royer, O'Neill & Wright (Math. Program. 2020, 10.1007/s10107-019-01362-7) and Curtis, Robinson, Royer & Wright (SIAM J. Optim. 2021, 10.1137/19M130563X): "They are based on practical methods, but the modifications that are made to admit nonasymptotic theory do not improve the practical performance. Moreover, the complexity bounds are quite pessimistic for small ϵ; there remains a large gap between these bounds and practical performance." (p. 23)
- General framing: "In other classes, there is a wide gap between theory and practice, with practical performance being much faster on typical problems than the theory predicts." (p. 2)
- [inferred] No outside critic of this line was found in this run (see Gaps). Wright names the limitation first, as he did for GPSR.

---

## 7. Criticism recorded inside his own record (cross-reference to 03)

Not re-read here; see `03-process-evidence.md` §2.1 and §2.3.
- *Primal-Dual Interior-Point Methods* errata (43 items, 1999) include repaired proofs and a withdrawn overclaim about the homogeneous self-dual formulation of Ye, Todd and Mizuno. That overclaim was refuted by an example in the YTM paper itself [practice, P, via 03]. It is the clearest case of a **judgement shown wrong in print** and corrected by Wright. Nine readers are thanked, among them Forsgren and Higham.
- A student found equation errors in Rao, Wright & Rawlings (JOTA 1998) while reimplementing it. The errata were posted on Wright's page [observed, P, via 03].
- NIPS 2013/2014/2017 reviews. Reviewers asked for a missing baseline (answered with a new table) and noted a missing computational comparison (2017, no rebuttal published) [observed, P, via 03].

---

## 8. Public reviews of the books (checked; no critique found)

- [observed, P] zbMATH Open reviews:
  - K. Schittkowski on *Primal-Dual Interior-Point Methods* (Zbl 0863.65031): "It is a pleasure to read the book. The presentation of basic analysis, algorithms and convergence results is very clear and complete."
  - N. Curteanu on *Numerical Optimization* 1st ed. (Zbl 0930.65067) and 2nd ed. (Zbl 1104.65059): descriptive, with no critical remark.
- *Optimization for Data Analysis* (Wright & Recht, CUP 2022, 10.1017/9781009004282): its zbMATH entry is licence-blocked. The WebSearch returned only publisher endorsement blurbs (e.g. J. C. Duchi, S. Shalev-Shwartz), which are promotional and not reviews [observed, S].
- [inferred] The public reviews are uniformly positive and miss what the errata record: repaired proofs, a reversed algorithm specification and an overclaim. For this researcher, **errata are more informative than reviews** (Contradictions §5).

---

## 9. Mapping to the seven layers (framework §一)

| Layer | What the critiques show | Evidence |
|---|---|---|
| 1 Taste | He values analyses that explain a practical success (Hogwild!, RPCD, Mehrotra-like IPMs). Critics show that the explaining model can be idealized: independence, uniform timing, bounded gradients, τ ≈ P | §1, §4, §5.1 [inferred] |
| 2 Problem choice / when to stop | He leaves a line once its core theorem is done (degenerate SQP ~2005, async ~2015). Later critiques of those lines go unanswered | §1.5, §2.3 [practice, inferred] |
| 4 Execution | Benchmarks by others depend on tuning he supplied. Hardware-dependent claims age (NUMA) | §1.6, §3 [observed] |
| 5 Judging results | Local convergence theory was taken as the result, and globalized behaviour was left open, then shown mixed by others. Conditional expectations (τ = 2P–3P) were contradicted by measurement | §1.4, §2.2–2.3 [observed] |
| 5 Response to critique | Corrects what his own implementations reveal (inconsistent reads, errata). Answers worst-case examples with sharper analysis and collaboration. Engages rival benchmarks privately before publication. No published rebuttals or comment/reply exchanges | §1.7, §3, §5.1, §7 [practice] |
| 6 Expression | States limitations in abstracts (GPSR 2007; 2025 essay) before critics do | §3, §6 [stated] |
| 3, 7 | No critique evidence on idea generation or group organization | — (left empty) |

**Use in the roundtable** [inferred]. When the Wright skill proposes a solver change backed by a local-convergence or complexity result, the critique record says to check four things:
1. Does the globalized method actually reach the region where the local theory applies? (sSQP and critical multipliers.)
2. Do the concurrency or sampling assumptions match the target hardware and data? (Async.)
3. Was the benchmark run with the rival's best settings? (NESTA shows he cares about this for his own codes.)
4. Does the production heuristic still have a safeguard? (Mehrotra.)

---

## Contradictions

Kept as found; not reconciled.

1. **τ as "a modest multiple of P" vs "orders of magnitude bigger than p".** Wright 2015 (arXiv:1502.04759v1, p. 27, conditional on equal update rates) against Leblond et al. 2018 (JMLR, pp. 12, 37, measured for Asaga and Hogwild up to 40 cores).
2. **"Extended" vs "fundamental flaw".** Wright's 2020 statement says the Hogwild! analysis "has subsequently been extended in many ways". Leblond et al. call the after-write labeling "a fundamental flaw for analyzing non-uniform asynchronous computation". Mania et al. (with co-author Recht) say the original simplifications "are not necessary".
3. **"Seminal" and "unrealistic" in the same paper.** Cannelli et al. call Liu & Wright "the seminal work [21]" (p. 4) and list [21] among works with an "unrealistic assumption" (p. 5).
4. **Lock-free speedup vs NUMA scaling.** Hogwild! "outperforms alternative schemes that use locking by an order of magnitude" (2011 abstract) vs HogWild++: scalability "severely limited" on multi-socket NUMA (2016). Different hardware eras.
5. **Positive reviews vs errata.** The zbMATH review calls the IPM book's analysis "very clear and complete". Wright's own errata list a proof that "is inadequate since it assume feasibility of the primal problem" and a withdrawn overclaim (via 03).
6. **Squared variables: received critique vs Wright's reassessment.** Ding & Wright's own abstract states both sides. Squared-slack formulations have "clear disadvantages, not least being that first-order optimal points for the squared-variable reformulation may not correspond to first-order optimal points for the original problem", yet "algorithms built on these formulations are surprisingly competitive with standard methods" (arXiv:2310.01784 abstract; SIAM J. Optim. 35 (2025) 2265–2293, 10.1137/23M1608343). What *Numerical Optimization* itself says about squared slacks was **not read**.
7. **Critics disagree with each other.** Leblond et al. say Mania et al.'s fix works only in a restricted setup. Sun, Hannah & Yin say the Leblond/Mania relabeling fix "creates other artificial implementation requirements". There is no consensus replacement for the Hogwild!-era model.

---

## Gaps

- **No comment/reply exchange involving Wright** was found. The TOP 2015 critical-multiplier discussion had four discussants, none of them Wright. SIAM Review or journal "Comments on" items were not found.
- **No critical book review found.** zbMATH reviews are descriptive and positive. SIAM Review or MAA reviews of his books were not located (Crossref queries returned none). *Optimization for Data Analysis* reviews: publisher blurbs only.
- **Not read (paywalled, no abstract in any API, no open copy found)**: Hager 1999; Fernández & Solodov 2010; Izmailov & Solodov 2012; the TOP 2015 paper, comments and rejoinder; Gill, Kungurtsev & Robinson IMA JNA 2017; Forsgren, Gill & Shinnerl 1996; Cartis 2009 full text (preprint PDF not extractable).
- **Whether Gill's group answered Wright's 2001 pivot-order criticism** was not established.
- **Whether Wright answered the delay-dependence / τ critiques** anywhere other than papers: *Optimization for Data Analysis* (2022) and course notes were not checked. His 2020 Test-of-Time talk (YouTube / SlidesLive, per the WebSearch result list) was not watched, and no transcript was found.
- **Post-2014 ML reviews** (OpenReview) are inaccessible from this environment (browser challenge / login), as 03 also found.
- **Outside critiques of the Newton-CG complexity line** were not found; only Wright's self-assessment. **PCx/OOQP in independent LP/QP benchmarks** (e.g. Mittelmann's) were not found in current or archived form within the time box.
- **MPC**: no critique aimed specifically at Rao, Wright & Rawlings (IPMs for MPC) was found. The active-set MPC literature (e.g. Ferreau, Bock & Diehl, Int. J. Robust Nonlinear Control 18 (2008) 816–830, 10.1002/rnc.1251) does not criticize it in its abstract; full text not read.
- **No failed replication, retraction or public rejected paper** was found (see also 01 §3, 03 §4).
- **Tooling limits this run**: the DBLP search API returned a bot challenge; Semantic Scholar rate-limited; the arXiv export API returned HTTP 406 (abstract pages were used instead).

---

## Sources

Primary (P) = the critic's or Wright's own text. Secondary (S) = reports, blurbs or metadata only. "read" = full text or the named pages read in this run.

1. Mania, Pan, Papailiopoulos, Recht, Ramchandran, Jordan. "Perturbed Iterate Analysis for Asynchronous Stochastic Optimization". SIAM J. Optim. 27 (2017) 2202–2229, 10.1137/16M1057000; arXiv:1507.06970v2 (read pp. 2–10, 19). P
2. Leblond, Pedregosa, Lacoste-Julien. "Improved Asynchronous Parallel Optimization Analysis for Stochastic Incremental Methods". J. Mach. Learn. Res. 19 (2018) 1–68; arXiv:1801.03749v3 (read pp. 1–7, 12, 35–37). P
3. Leblond, Pedregosa, Lacoste-Julien. "ASAGA: Asynchronous Parallel SAGA". AISTATS 2017; arXiv:1606.04809 (abstract). P
4. Sun, Hannah, Yin. "Asynchronous Coordinate Descent under More Realistic Assumptions". NeurIPS 2017; arXiv:1705.08494v2 (read pp. 1–4). P
5. Cannelli, Facchinei, Kungurtsev, Scutari. "Asynchronous parallel algorithms for nonconvex optimization". Math. Program. 184 (2020) 121–154, 10.1007/s10107-019-01408-w; arXiv:1607.04818v3 (read pp. 4–6). P
6. De Sa, Zhang, Olukotun, Ré. "Taming the Wild: A Unified Analysis of Hogwild!-Style Algorithms". arXiv:1506.06438v2, 2015 (read pp. 2, 5). P
7. Nguyen, Nguyen, van Dijk, Richtárik, Scheinberg, Takáč. "SGD and Hogwild! Convergence Without the Bounded Gradients Assumption". ICML 2018, PMLR 80:3747–3755; arXiv:1802.03801v2 (read pp. 2, 5). P
8. Zhang, Hsieh, Akella. "HogWild++: A New Mechanism for Decentralized Asynchronous Stochastic Gradient Descent". ICDM 2016, 629–638, 10.1109/ICDM.2016.0074; author PDF https://www.huan-zhang.com/pdf/wildSGD.pdf (read p. 1). P
9. HogWild++ code README, https://github.com/huanzhang12/hogwildpp (raw README, read 2026-09-28). P
10. Niu, Recht, Ré, Wright. "HOGWILD!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent". arXiv:1106.5730 (abstract); NIPS 2011. P
11. Wright et al. NeurIPS 2020 Test-of-Time press statement, "Hogwild: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent", https://neurips.cc/media/Press/SWright_HogWild_ToT_Press_Statement.pdf (read, 5 pp.). P
12. Lynch, S. "How a 'Crazy Idea' Overturned the Conventional Rules of Machine Learning". Stanford HAI, 8 Dec 2020, https://hai.stanford.edu/news/how-crazy-idea-overturned-conventional-rules-machine-learning (WebFetch summary). S
13. Wright, S. J. "Coordinate Descent Algorithms". Math. Program. 151 (2015) 3–34, 10.1007/s10107-015-0892-3; arXiv:1502.04759v1 (read pp. 26–29). P
14. Liu, Wright. "Asynchronous Stochastic Coordinate Descent: Parallelism and Convergence Properties". SIAM J. Optim. 25 (2015) 351–376, 10.1137/140961134; arXiv:1403.3862 (abstract). P
15. Liu, Wright, Ré, Bittorf, Sridhar. "An Asynchronous Parallel Stochastic Coordinate Descent Algorithm". JMLR 16 (2015) 285–322; arXiv:1311.1873 (abstract). P
16. Wright, S. J. "Superlinear Convergence of a Stabilized SQP Method to a Degenerate Solution". Comput. Optim. Appl. 11 (1998) 253–275, 10.1023/A:1018665102534 (metadata; content via 01). P
17. Wright, S. J. "Modifying SQP for Degenerate Problems". SIAM J. Optim. 13 (2002) 470–497, 10.1137/S1052623498333731 (metadata; quotes via 01). P
18. Wright, S. J. "Constraint identification and algorithm stabilization for degenerate nonlinear programs". Math. Program. 95 (2003) 137–160, 10.1007/s10107-002-0344-8 (metadata). P
19. Wright, S. J. "An Algorithm for Degenerate Nonlinear Programming with Rapid Local Convergence". SIAM J. Optim. 15 (2005) 673–696, 10.1137/030601235 (metadata). P
20. Mostafa, Vicente, Wright. "Numerical Behavior of a Stabilized SQP Method for Degenerate NLP Problems". LNCS 2861 (2003) 123–141, 10.1007/978-3-540-39901-8_10 (metadata; discussed in 24). P
21. Hager, W. W. "Stabilized Sequential Quadratic Programming". Comput. Optim. Appl. 12 (1999) 253–273, 10.1023/A:1008640419184 (metadata only). S
22. Fernández, Solodov. "Stabilized sequential quadratic programming for optimization and a stabilized Newton-type method for variational problems". Math. Program. 125 (2010) 47–73, 10.1007/s10107-008-0255-4 (metadata only). S
23. Izmailov, Solodov. "Stabilized SQP revisited". Math. Program. 133 (2012) 93–120, 10.1007/s10107-010-0413-3 (metadata only). S
24. Gill, Kungurtsev, Robinson. "A stabilized SQP method: superlinear convergence". Math. Program. 163 (2017) 369–410, 10.1007/s10107-016-1066-7; preprint https://optimization-online.org/2014/07/4417/ (read pp. 3, 37–40). P
25. Gill, Kungurtsev, Robinson. "A stabilized SQP method: global convergence". IMA J. Numer. Anal. 37 (2017) 407–443, 10.1093/imanum/drw004 (metadata only). S
26. Gill, Robinson. "A Globally Convergent Stabilized SQP Method". SIAM J. Optim. 23 (2013) 1983–2010, 10.1137/120882913 (Crossref abstract; preprint https://optimization-online.org/2012/06/3518/, read pp. 1–3). P
27. Izmailov, Solodov. "On attraction of linearly constrained Lagrangian methods and of stabilized and quasi-Newton SQP methods to critical multipliers". Math. Program. 126 (2011) 231–257, 10.1007/s10107-009-0279-4; author-hosted PDF http://www.cs.wisc.edu/~solodov/izmsol08iSQP.pdf (read pp. 231–232, 249, 253–256). P
28. Izmailov, Solodov. "Critical Lagrange multipliers: what we currently know about them, how they spoil our lives, and what we can do about it". TOP 23 (2015) 1–26, 10.1007/s11750-015-0372-1, with comments by Fischer (10.1007/s11750-015-0368-x), Martínez (10.1007/s11750-015-0369-9), Mordukhovich (10.1007/s11750-015-0370-3), Robinson (10.1007/s11750-015-0371-2) and a rejoinder (10.1007/s11750-015-0373-0) (metadata only). S
29. Lee, Wright. "Revisiting superlinear convergence of proximal Newton-like methods to degenerate solutions". arXiv:2602.10470 (text search of full PDF). P
30. Becker, Bobin, Candès. "NESTA: A Fast and Accurate First-order Method for Sparse Recovery". SIAM J. Imaging Sci. 4 (2011) 1–39, 10.1137/090756855; arXiv:0904.3367v1 (read pp. 19–26, 35). P
31. Figueiredo, Nowak, Wright. "Gradient Projection for Sparse Reconstruction: Application to Compressed Sensing and Other Inverse Problems". IEEE JSTSP 1 (2007) 586–597, 10.1109/JSTSP.2007.910281 (metadata; abstract quote via 01). P
32. Wright, Nowak, Figueiredo. "Sparse Reconstruction by Separable Approximation". IEEE TSP 57 (2009) 2479–2493, 10.1109/TSP.2009.2016892 (metadata). P
33. Salahi, Peng, Terlaky. "On Mehrotra-Type Predictor-Corrector Algorithms". SIAM J. Optim. 18 (2007) 1377–1397, 10.1137/050628787 (Crossref abstract; preprint https://optimization-online.org/2005/03/1104/, read p. 1 and reference list). P
34. Cartis, C. "Some disadvantages of a Mehrotra-type primal-dual corrector interior point algorithm for linear programming". Appl. Numer. Math. 59 (2009) 1110–1119, 10.1016/j.apnum.2008.05.006 (preprint abstract, https://optimization-online.org/2005/02/1062/). P
35. Czyzyk, Mehrotra, Wagner, Wright. "PCx: an interior-point code for linear programming". Optim. Methods Softw. 11 (1999) 397–430, 10.1080/10556789908805757; and Gertz, Wright, "Object-oriented software for quadratic programming", ACM TOMS 29 (2003) 58–81, 10.1145/641876.641880 (metadata; quotes via 03). P
36. Sun, Ye. "Worst-case complexity of cyclic coordinate descent: O(n²) gap with randomized version". Math. Program. 185 (2021) 487–520, 10.1007/s10107-019-01437-5; arXiv:1604.07130 (abstract). P
37. Lee, Wright. "Random permutations fix a worst case for cyclic coordinate descent". IMA J. Numer. Anal. 39 (2019) 1246–1275, 10.1093/imanum/dry040; arXiv:1607.08320 (abstract). P
38. Wright, Lee. "Analyzing random permutations for cyclic coordinate descent". Math. Comp. 89 (2020) 2217–2248, 10.1090/mcom/3530; Gürbüzbalaban, Ozdaglar, Vanli, Wright, "Randomness and permutations in coordinate descent methods", Math. Program. 181 (2020) 349–376, 10.1007/s10107-019-01438-4 (metadata). P
39. Wright, S. J. "Effects of Finite-Precision Arithmetic on Interior-Point Methods for Nonlinear Programming". SIAM J. Optim. 12 (2001) 36–78, 10.1137/S1052623498347438; arXiv:math/0103102v1 (read pp. 2, 33). P
40. Forsgren, Gill, Shinnerl. "Stability of Symmetric Ill-Conditioned Systems Arising in Interior Methods for Constrained Optimization". SIAM J. Matrix Anal. Appl. 17 (1996) 187–211, 10.1137/S0895479894270658 (metadata only). S
41. Wright, S. J. "Optimization in Theory and Practice". arXiv:2510.15734v2, 2025 (read pp. 2, 9, 23). P
42. Ding, Wright. "On Squared-Variable Formulations". SIAM J. Optim. 35 (2025) 2265–2293, 10.1137/23M1608343; arXiv:2310.01784 (abstract). P
43. zbMATH Open reviews: Schittkowski on *Primal-Dual Interior-Point Methods* (SIAM 1997, 10.1137/1.9781611971453), Zbl 0863.65031, https://zbmath.org/964349; Curteanu on *Numerical Optimization* 1st ed. (10.1007/b98874), Zbl 0930.65067, and 2nd ed. (10.1007/978-0-387-40065-5), Zbl 1104.65059 (read via API). P
44. WebSearch result blurbs for *Optimization for Data Analysis* (CUP 2022, 10.1017/9781009004282): Cambridge Core / retailer pages, endorsement quotes only (search 1 of 2). S
45. WebSearch "Hogwild! NeurIPS 2020 test of time award talk" (search 2 of 2): led to 11 and 12, plus video links (YouTube c5T7600RLPc; SlidesLive 38942365), which were not watched. S
46. UW-Madison Oral History Program, "Oral History Interview, Stephen Wright (2179)", 2022-10-04, transcript at `../sources/talks/2022-10-04_uw-oral-history-2179_transcript.txt`. Used for the SGD admission at [24:55]: "Because it's very slow, we thought it's very slow. But machine learning people found this was exactly the tool they needed". This is a judgement Wright says the community, himself included ("we"), got wrong. P

Also consulted but not counted as sources: sibling notes `01-publications.md`, `02-methodology.md`, `03-process-evidence.md` and `04-mentorship.md` (this run); the DBLP title list saved by agent 01 in scratch; Optimization Online search pages; Crossref and OpenAlex metadata calls.
