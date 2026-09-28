# Jorge Nocedal · 05 Peer critique: blind spots, limits of applicability, judgements shown wrong

- **Researcher**: Jorge Nocedal (Walter P. Murphy Professor, IEMS, Northwestern University)
- **Dimension**: research-craft Phase 1, agent 05 of 06: peer critique (framework §二 row 5): failed replications, published comments, counterexamples, public reviews, rival schools, benchmark studies, predictions that did not come true.
- **Research date**: 2026-09-28
- **Sources consulted**: 47 (listed under "Sources"): 17 primary (Nocedal's own papers, preprints, code, talk and interview transcripts, and the public ICLR 2017 review record of his paper), 30 secondary (critics' papers, rival benchmark studies, public referee reports, independent benchmarks, book reviews, bibliographic databases, 2 WebSearch calls).
- **Local corpus**: `references/sources/{papers,essays,software}` hold only `.gitkeep`, so nothing here is "from user-supplied material". The seven transcripts in `../sources/talks/` were saved earlier in this run by research agent 02 (not user-supplied). `private/` was not opened.
- **WebSearch calls used**: 2 of 2.

**Labels.** [stated] = Nocedal said or wrote it; [practice] = what his papers, code or records show he did; [observed] = what others (critics, reviewers, benchmarkers) reported; [inferred] = my inference, with its basis. Every item also carries **P** (primary) or **S** (secondary). A critic's own paper is primary evidence of *the critique* but secondary evidence about Nocedal; I mark critics' papers S throughout.

**Quotes.** Quotes from PDFs are copied from text extracted with PyMuPDF. I rejoined words split by end-of-line hyphenation and restored spacing in the pre-2005 PostScript preprints ("No cedal"); I changed no wording. Page numbers are **PDF pages of the file named in Sources**, not journal pages. Transcript quotes are verbatim *captions* with the block timestamp, marked "caption-derived"; the Purdue 2017 captions are uploader-provided, the NITMB 2024 and 2026 interview captions are automatic speech recognition (ASR), not checked against audio.

---

## 0. Bottom line (what a user of this skill should take from this note)

1. **The most-contested Nocedal claim is the 2017 large-batch / sharp-minima paper.** It was praised in review (ICLR 2017 oral, one reviewer rating 10). Within two years, four lines of critique appeared:
   - a reparametrization counter-argument (Dinh et al. 2017);
   - a training-budget explanation (Hoffer et al. 2017);
   - large-scale counter-evidence (Goyal et al. 2017);
   - a methodological audit (Shallue et al. 2019): two batch sizes, one fixed learning rate with Adam, batch-norm statistics over the full batch.

   Nocedal's group **never published a rebuttal**. It accepted the Goyal result in its next ML paper (2018). In 2024 Nocedal still presented the example as "still valid today to some extent". The later literature itself splits: sharpness was the best generalization predictor in one large study (2019) and did not correlate well in another (2023). [§1]
2. **His rival-benchmark weak points in constrained NLP were answered with new algorithm variants inside the code, not with rebuttal papers.** [inferred from the sequence of papers; §4]

   | Critique | Critic | Later Nocedal paper or code change |
   |---|---|---|
   | Line-search interior methods fail on the Wächter–Biegler example | Wächter & Biegler 2000 | Byrd–Marazzi–Nocedal failure analysis (2001/2004) |
   | NITRO "significantly slower and far less robust" | LOQO authors, 2000 | Knitro-Direct hybrid (2004/2006) |
   | CG-based steps up to 20,001 CG iterations per major iteration | LOQO authors, 2002 | Direct factorization step (2004/2006) |
   | Fails to flag infeasible problems | IPOPT authors, 2004 | Byrd–Curtis–Nocedal infeasibility detection (2010) |
   | Penalty-parameter pathology (ADLITTLE) | Fletcher | Steering rules (2007/2008) |
3. **A 1992 theoretical judgement was later shown wrong in the worst case.** Nocedal wrote that "the numerical experience of many years suggests that the BFGS method always converges" and that "Nobody has been able to construct an example in which the BFGS method fails". Dai (2002) then showed that BFGS with Wolfe line searches "need not converge for nonconvex objective functions". Mascarenhas (2004) showed the same for exact line searches. No response by Nocedal was found. [§3]
4. **Critics' suggestion to add a weak-Wolfe option to L-BFGS / L-BFGS-B was not adopted.** Lewis & Overton suggested it in a December 2008 preprint (published 2013). The March 2011 L-BFGS-B 3.0 code still enforces the strong-Wolfe curvature test. [practice, P: code; §3.2]
5. **In the noise programme he pre-empted the main critique himself.** The 2021 finite-difference paper concedes three things:
   - NEWUOA is better on noisy problems, "but not by a wide margin";
   - interpolation methods are "more robust in the presence of noise than we expected";
   - the study covers only one noise model.

   Rival-school follow-ups (PDFO 2024; Full-Low Evaluation 2023) press the same two limits: finite differences need a noise estimate, and line-search FD methods break on nonsmooth problems. [§5]
6. **He solicits critique in talks** ("please shoot it down"), hedges his own pictures ("probably wrong"), and names the field's review system as "almost random". He credits critics who changed his work (Fletcher, Gould). [stated/practice; §6]

---

## 1. Machine learning: the large-batch / sharp-minima claim (2016–2024)

**The claim** [practice, P]: Keskar, Mudigere, Nocedal, Smelyanskiy & Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", ICLR 2017, arXiv:1609.04836 (v2, 9 Feb 2017). The abstract says large-batch methods "tend to converge to sharp minimizers of the training and testing functions - and as is well known, sharp minima lead to poorer generalization". Setup:
- ADAM for both regimes;
- 10% of the training data as the large batch, 256 as the small batch;
- "The networks were trained, without any budget or limits, until the loss function ceased to improve" (p. 4).

Era and resources: an Intel-funded collaboration (three Intel co-authors); six networks on MNIST, TIMIT, CIFAR-10 and CIFAR-100; 5 runs each (p. 4).

### 1.1 Pre-publication review (ICLR 2017, OpenReview H1oyRlYgg) [observed + practice, P: review record]

Read from the Internet Archive snapshot (captured 2024-03-21) of the OpenReview API. Research agent 03 saved it to the shared scratch folder; I read the saved text in this run. The live site and the Wayback Machine were both blocked for me (bot challenge; egress policy). Agent 03 has the full table (`03-process-evidence.md` §4.1). The points relevant to critique:

| Critic | Point | Answered? |
|---|---|---|
| AnonReviewer2 (2016-12-02) | The claimed scale invariance fails with "1+f(x)" in the denominator | Yes. Keskar: "You are right, this metric is not scale invariant, and we will remove that statement from the paper in our next update." The reviewer then rated the paper "10: Top 5% of accepted papers, seminal paper" and titled the review "Little novelty but valuable empirical evidence". |
| AnonReviewer3 (2016-12-03) | "true "local minima" or just "local minima" of one-dimensional slices" | Conceded: "we cannot guarantee that the solutions obtained by the SB and LB methods are indeed local minima of the problem (as we did not attempt to verify second-order optimality)". Agent 03 reports the promised terminology change was only partly made in v2. |
| AnonReviewer3; Alex Lamb (public) | Would noise injection rescue large batches? | A negative result was disclosed only in the thread: "despite significant tuning of the hyperparameters of the random noise, we did not observe any consistent improvements in testing error". |
| Program chairs (2017-02-06) | "All reviews (including the public one) were extremely positive" | Accept (Oral). |
| Amir H. Abdi (public, 2019-10-08) | "Potential mistake in Appendix C" (the performance model); "Typo in Figure 5" | No reply in the archived thread. |

Every reply is signed by the student first author, Keskar. **No reviewer raised** the points the post-publication critics made (learning-rate scaling, training budget, batch normalization, reparametrization). [inferred from comparing the two records]

### 1.2 Post-publication critiques

**C1. Dinh, Pascanu, S. Bengio & Y. Bengio, "Sharp Minima Can Generalize For Deep Nets", ICML 2017 (PMLR 70), arXiv:1703.04933** [observed, S]
- Argument: flatness notions "can not be directly applied to explain generalization" (abstract). For rectifier networks, "every minimum is observationally equivalent to a minimum that generalizes as well but with high ϵ-sharpness. This also applies when using the full-space ϵ-sharpness used by Keskar et al. (2017)" (p. 7).
- Limit the critics state themselves: "We have not been able to show a similar problem with random subspace ϵ-sharpness used by Keskar et al. (2017)" (p. 7).
- Conclusion: "the conclusion that flat minima should generalize better than sharp ones cannot be applied as is without further context" (p. 9).
- **Answered?** No published reply found.
  - The 2018 group paper cites Dinh et al. without comment (§1.3).
  - In 2024 [stated, P, caption-derived, NITMB [0:25:05]]: "here's an example that we produced um in 2017 and it's still valid today to some extent."
  - Same talk [0:25:39]: "it is known now after many years in the area of machine learning is that if you can encourage your optimization algorithms to go to flat minimizers, you are in fact going to get better generalization. What happens with these minimizers? That's subject to discussion."

**C2. Hoffer, Hubara & Soudry, "Train longer, generalize better: closing the generalization gap in large batch training of neural networks", NeurIPS 2017, arXiv:1705.08741** [observed, S]
- They restate Keskar's four observations and hypothesis (p. 3), then offer "a somewhat different explanation".
- Conclusion: "This implies that the problem is not related to the batch size but rather to the amount of updates" (p. 9).
- They re-ran Keskar's own networks F1, C1 and C3, closing the gap with learning-rate scaling, Ghost Batch Normalization and "regime adaptation". Validation accuracy, Table 1, p. 8:

  | Network | SB | LB | LB + adaptation |
  |---|---|---|---|
  | F1 (MNIST) | 98.27% | 97.05% | 98.53% |
  | C1 (CIFAR-10) | 87.80% | 83.95% | 88.20% |
  | C3 (CIFAR-100) | 61.25% | 51.50% | 63.20% |

- It targets Keskar's "without any budget or limits" condition: "until the loss function ceased to improve" is not the same as the same number of updates.
- **Answered?** Cited in the 2018 group paper as one of the studies that "explored larger batch sizes and steplengths to reduce the number of updates" (§1.3). No rebuttal.

**C3. Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", arXiv:1706.02677 (v2 Apr 2018)** [observed, S]
- "Our comprehensive experiments in §5 show that optimization difficulty is the main issue with large minibatches, rather than poor generalization (at least on ImageNet), in contrast to some recent studies [20]." [20] is Keskar et al. (p. 2).
- Abstract: "no loss of accuracy when training with large minibatch sizes up to 8192 images", with a linear learning-rate scaling rule and warmup, on 256 GPUs.
- **Answered?** Accepted in print (§1.3).

**C4. Shallue, Lee, Antognini, Sohl-Dickstein, Frostig & Dahl, "Measuring the Effects of Data Parallelism on Neural Network Training", JMLR 20 (2019), arXiv:1811.03600** [observed, S]. A methodological audit:
- Footnote 9 (p. 10): the term "large batch" "accompanies experiments in Keskar et al. (2017) that only compare two absolute batch sizes per data set, rather than charting out a curve to its apparent extremes".
- p. 11: "trained several neural network architectures on MNIST and CIFAR-10, each with two batch sizes, using the Adam optimizer and without changing the learning rate between batch sizes".
- pp. 11–12: all models used batch normalization and "presumably computed the batch normalization statistics using the full batch size". Hoffer et al.'s finding on this "suggests an alternative explanation for the results of Keskar et al. (2017)".
- p. 12: "Moreover, Keskar et al. (2017) reported that data augmentation eliminated the difference in solution quality between small and large batch experiments."
- Overall (abstract): "disagreements in the literature on how batch size affects model quality can largely be explained by differences in metaparameter tuning and compute budgets at different batch sizes. We find no evidence that larger batch sizes degrade out-of-sample performance."
- The Keskar text I read does not describe any learning-rate change between the SB and LB runs; I searched it for "learning rate" and "step size".
- **Answered?** Nothing found. Scale context: Shallue et al. trained "168,160 individual models across 35 workloads" (abstract), orders of magnitude beyond the 2016 study. [observed; the resource asymmetry is inferred]

**C5. Andriushchenko, Croce, Müller, Hein & Flammarion, "A Modern Look at the Relationship between Sharpness and Generalization", ICML 2023 (PMLR 202), arXiv:2302.07011** [observed, S]
- "The magnitude-aware sharpness of Keskar et al. (2016) mitigates but does not completely resolve reparametrization invariance" (p. 2).
- Abstract: "we observe that sharpness does not correlate well with generalization but rather with some training parameters like the learning rate … in multiple cases, we observe a consistent negative correlation of sharpness with out-of-distribution error implying that sharper minima can generalize better".
- The same paper credits Keskar et al. as "The seminal work" showing the degradation "is correlated with sharpness of minima" (p. 2).

**Partial support (kept, not dropped)** [observed, S]:
- Jiang, Neyshabur, Mobahi, Krishnan & S. Bengio, "Fantastic Generalization Measures and Where to Find Them", arXiv:1912.02178 (2019): "sharpness measure proposed by Keskar et al. (2016) perform the best overall and seem to be promising candidates for further research" (p. 2). The study trained over 10,000 CIFAR-10/SVHN models.
- Smith & Le, "A Bayesian Perspective on Generalization and Stochastic Gradient Descent", ICLR 2018, arXiv:1710.06451. They call Keskar's fixed-learning-rate observation a "striking result" (p. 1). They re-attribute it: "it is not the batch size itself which controls this tradeoff" but the noise scale (p. 6). They also note "Dinh et al. (2017) challenged this interpretation" (p. 1).
- Masters & Luschi, "Revisiting Small Batch Training for Deep Neural Networks", arXiv:1804.07612 (2018). The best results come from "mini-batch sizes between m = 2 and m = 32, which contrasts with recent work advocating the use of mini-batch sizes in the thousands" (abstract). They cite Keskar et al. for improved small-batch generalization (p. 1).

### 1.3 How the group answered [practice, P]

Bollapragada, Mudigere, Nocedal, Shi & Tang, "A Progressive Batching L-BFGS Method for Machine Learning", ICML 2018, arXiv:1802.05374, p. 2:

> "Keskar et al. (2016) empirically observed that large-batch methods converge to solutions with inferior generalization properties; however, Goyal et al. (2017) showed that large-batch methods can match the performance of small-batch methods when a warm-up strategy is used in conjunction with scaling the step length by the same factor as the batch size."

p. 1 reframes the 2017 claim as speculation: "some researchers have speculated that SG is endowed with certain regularization properties that are essential in the minimization of such complex nonconvex functions (Hardt et al., 2015; Keskar et al., 2016)". The paper then moves on to progressive batching rather than defending sharp minima. **Pattern** [inferred]: concede the empirical counter-result in one sentence, keep the research programme (batch-size control), do not litigate.

### 1.4 His own hedges at the time [stated, P, caption-derived, Purdue 2017-02-15]

- [0:35:39]: "I keep showing it to some of my colleagues, some of my friends who are the real experts on this. And I tell them, please shoot it down."
- [0:36:47], on the sharpness measure: "we didn't do that, we did something that [COUGH] an undergraduate student would do." This concedes the crudeness that Dinh et al. and Andriushchenko et al. later attacked.
- [0:39:16]: "my geometrical interpretation. It's gonna be really good, but probably wrong."
- NITMB 2024 [0:12:22]: "I always have one picture that I know is wrong."
- NITMB 2024 [0:27:50], on sharpness-aware minimization: "it's not right solution. It's a a empirical solution."

---

## 2. Stochastic and batch quasi-Newton methods for ML: reviews, rivals, adoption

**2.1 NeurIPS 2016 public referee reports.** Berahas, Nocedal & Takáč, "A Multi-Batch L-BFGS Method for Machine Learning", NIPS 2016 (arXiv:1605.06049). Reviews page: `papers.nips.cc/paper_files/paper/2016/file/8ebda540cbcc4d7336496819a46a1b68-Reviews.html` [observed, S; read in full]

| Reviewer | Critique (verbatim) |
|---|---|
| Reviewer 3 ("3-Expert") | "the comparison to SGD in the paper is not very fair. A mini-batch SGD with parallel implementation is required for the comparison."; "a comparison of prediction accuracy w.r.t. running time (not epochs) is required."; "The paper analyzed the nonconvex cases, but no experiment is performed to verify the theoretical results." |
| Reviewer 4 | "The convergence analysis is neat but not surprising."; "It would have been impressive if the authors conducted experiments with such settings" (limited communication) |
| Reviewer 1 | If the strong-convexity bound "mu_1 is very small, then it seems that the resulting limit in Theorem 3.2 will be worse than the limit obtained by a first-order version of your algorithm when one would choose simply H_k = I" |

- The author rebuttal is not public.
- **Answered?** Partly, and later, without Nocedal: the journal version (Berahas & Takáč, "A robust multi-batch L-BFGS method for machine learning", *OMS* 35 (2020) 191–219, doi:10.1080/10556788.2019.1658107; arXiv:1707.08552) adds "neural network training problems" (abstract). [practice, S: former student]
- Note: `03-process-evidence.md` Gaps item 2 says these reviews were "not public or not found". They are public at the URL above (see Contradictions 9).

**2.2 Rival stochastic L-BFGS.** Moritz, Nishihara & Jordan, "A Linearly-Convergent Stochastic L-BFGS Algorithm", AISTATS 2016, arXiv:1508.02087 [observed, S]
- They build on Byrd, Hansen, Nocedal & Singer (SQN; arXiv:1401.7020; *SIOPT* 26 (2016), doi:10.1137/140954362). They adopt its key idea: "Our algorithm addresses this problem in the same ways as Byrd et al. (2014), by computing Hessian vector products formed from larger minibatches" (p. 2).
- They add variance reduction and report: "SLBFGS performs well … over a large range of step sizes, whereas the performance of SVRG, SQN, and SGD degrade much more rapidly with poor step-size choices" (p. 7).
- Critique: SQN has no linear rate and is step-size sensitive. **Answered?** No direct reply found. Nocedal's later ML work moved to adaptive sampling and progressive batching, which control variance by sample size (arXiv:1710.11258; arXiv:1802.05374). [inferred link]

**2.3 Independent evidence that cuts the other way.** Le, Ngiam, Coates, Lahiri, Prochnow & Ng, "On Optimization Methods for Deep Learning", ICML 2011 [observed, S]: "off-the-shelf optimization methods such as Limited memory BFGS (L-BFGS) and Conjugate gradient (CG) with line search can significantly simplify and speed up the process of pretraining deep algorithms" (abstract). Set it beside:
- Nocedal's report of LeCun's 1987 negative test (2026 interview [1:04:28], see `02-methodology.md` F2);
- the 2018 abstract's "L-BFGS is currently not considered an algorithm of choice for large-scale machine learning applications".

**2.4 A forecast not borne out in mainstream deep-learning practice (so far)** [inferred from his own later statements]:
- 2018 SIAM Review, co-authored (p. 39): "We argue, however, that this is far from settled" (that SG is the ideal approach).
- 2017 Purdue [0:41:02]: "the stochastic method is a very good method, except that it doesn't exist."
- 2024 NITMB [0:08:27], on Adam: "a method called atom [sic: Adam] that everybody's using. And so the perception is that if you come up with an idea that cannot be trained with atom then it gets rejected".
- 2026 interview, his own regret: "machine learning people developed methods like Adam and so on … but they're not satisfactory" (`02-methodology.md` F5, C5).

He concedes the adoption fact and keeps the normative judgement.

---

## 3. Quasi-Newton theory and the L-BFGS / L-BFGS-B codes

**3.1 The 1992 BFGS judgement, and the counterexamples** [stated, P → observed, S]
- Nocedal, "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1 (1992), doi:10.1017/S0962492900002270. Author preprint pp. 21–22:
  - "Even though the numerical experience of many years suggests that the BFGS method always converges to a solution point, this has not been proved."
  - Open Question II asks whether BFGS with Wolfe line searches gives lim inf ‖g_k‖ = 0 on smooth nonconvex functions: "This is one of the most fundamental questions in the theory of unconstrained optimization … Nobody has been able to construct an example in which the BFGS method fails".
- Y.-H. Dai, "Convergence Properties of the BFGS Algoritm" [sic, Crossref title], *SIOPT* 13(3) (2002) 693–701, doi:10.1137/S1052623401383455 (abstract only): "It is also noted through the examples that the BFGS method with Wolfe line searches need not converge for nonconvex objective functions."
- W. F. Mascarenhas, "The BFGS method with exact line searches fails for non-convex objective functions", *Math. Program.* 99 (2004) 49–61, doi:10.1007/s10107-003-0421-7. Metadata only; not read.
- Y.-H. Dai, "A perfect example for the BFGS method", *Math. Program.* 138 (2013) 501–530, doi:10.1007/s10107-012-0522-2. Metadata only; not read.
- **Answered?** Not found. Whether *Numerical Optimization* (2nd ed., 2006) discusses these examples was **not read**.
- Reading [inferred]:
  - the practical half of the 1992 judgement ("numerical experience … suggests") is not refuted by constructed examples;
  - the stronger sentence "Nobody has been able to construct an example" was overtaken within ten years.
  - The question was well posed: it was answered, negatively.

**3.2 Nonsmooth use of BFGS, and a code-level suggestion not taken** [observed, S → practice, P]
- A. S. Lewis & M. L. Overton, "Nonsmooth optimization via quasi-Newton methods", *Math. Program.* 141 (2013) 135–163, doi:10.1007/s10107-012-0514-2. Read: the author preprint "Nonsmooth Optimization via BFGS" (PDF creation date 2008-12-08).
- Finding: BFGS with an inexact line search "consistently converges to local minimizers on all but the most difficult class of examples" (abstract).
- Suggestion aimed at Nocedal's codes (p. 4): "in our opinion a key change should be made to the widely used codes L-BFGS and L-BFGS-B [ZBN97] so that they are more generally applicable to nonsmooth problems: include the weak Wolfe line search defined in Section 2 as an optional alternative to the strong Wolfe line search that is currently implemented". They add: "Our experience with this is minimal".
- **Answered?** Not in the code. L-BFGS-B "version 3.0 march, 2011" (README; author tarball from the homepage, extracted in the shared scratch) still calls Moré–Thuente `dcsrch`. Its header states the curvature condition `abs(f'(stp)) <= gtol*abs(f'(0))` (`lbfgsb.f`, dcsrch comments), i.e. strong Wolfe. [practice, P: code]
- Ten years later the group cites the result approvingly: "Based on the results by Lewis and Overton [31] and Curtis et al. [19], a finite-difference implementation of BFGS (not L-BFGS) could prove a strong competitor to current DFO methods. However, how to perform finite differencing robustly in the nonsmooth setting is still an open research question." (Shi, Xuan, Oztoprak & Nocedal, arXiv:2102.09762 v1, p. 7) [stated, P]

**3.3 Early critique of L-BFGS itself (1979–80)** [stated, P, caption-derived, 2026 interview]. Nocedal reports:
- "the reviews were not so good but the editor of the paper was Horge Mor [Jorge Moré] … he made sure that it got published" [0:50:32];
- "by the time I published that paper and it was difficult for me people did not like it. I was sure that it was right because I tried everything else" [0:51:38];
- on Powell: "he didn't like it for reasons that are a little bit technical … It didn't bother me because I told you I've tried everything else" [0:52:48].

The referee reports themselves were not found (Gap). Answered by later practice: L-BFGS became his most-cited work (`01-publications.md` Contradictions 13).

**3.4 Self-corrections recorded elsewhere** (cross-reference, not repeated): the 2011 L-BFGS-B Remark (doi:10.1145/2049662.2049669), the book and SIAM Review errata, and the 2004 non-stationary-points paper (`01-publications.md` §4.1–4.2).

---

## 4. Constrained NLP: the interior-point rivalry and KNITRO benchmarks

**4.1 The Wächter–Biegler counterexample (2000)** [observed, S]
- A. Wächter & L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", *Math. Program.* 88 (2000) 565–574, doi:10.1007/PL00011386. Metadata only; the paper itself was **not read**. Its content below comes from two readers who did read it.
- Byrd, Marazzi & Nocedal (preprint OTC 2001/01, 23 Apr 2001; *Math. Program.* 99 (2004), doi:10.1007/s10107-003-0376-8) summarize: "They show that a class of interior methods can fail to generate a feasible point for a simple problem in three variables, and that the iterates do not approach a stationary point of any measure of infeasibility" (PDF p. 2).
- **Nocedal's answer** [practice, P]: a paper on *why* Newton iterations stall. Three results:
  - a second, bound-free example where "a class of Newton methods cannot attain feasibility, regardless of the choice of merit function and of the step selection strategy" (§4.3, PDF pp. 22–23);
  - "A trust region approach, on the other hand, performs efficiently on the same example" (for Powell's example; PDF p. 3);
  - a proof "that a class of line search feasible interior methods cannot exhibit convergence to non-stationary points" (abstract).
- The rival camp's reading of that answer [observed, S]: "Nocedal and Marazzi further examined this nonconvergence issue and proposed a general trust region method as a resolution" (Benson, Shanno & Vanderbei, ORFE-00-02 rev. 28 Aug 2000, PDF p. 2). They also propose their own fixes (shifting slacks, trust region, modified barrier; abstract).

**4.2 LOQO authors vs NITRO (2000): "significantly slower and far less robust"** [observed, S]
Source: H. Y. Benson, D. F. Shanno & R. J. Vanderbei, "Interior-Point Methods for Nonconvex Nonlinear Programming: Jamming and Numerical Testing". Preprint title "…Jamming and Comparative Numerical Testing", ORFE-00-02, rev. 28 Aug 2000; *Math. Program.* 99 (2004) 35–48, doi:10.1007/s10107-003-0418-2.

Test set: 889 AMPL models (CUTE + Schittkowski), default settings, SUN SPARC 400 MHz. Solved counts (Table 1, PDF p. 16):

| Problem size | SNOPT | NITRO | LOQO |
|---|---|---|---|
| small (585) | 558 | 516 | 555 |
| medium (101) | 79 | 73 | 81 |
| large (109) | 73 | 98 | 96 |
| very large (94) | 30 | 18 | 56 |

"NITRO has a limit of 10,000 variables, so that of the 94 problems categorized as very large, NITRO was able to attempt only 30" (p. 16). Their verdicts:
- "NITRO, however, is significantly slower and far less robust" (small problems) (pp. 16–17);
- "NITRO finds slightly less accurate ones" (p. 16);
- "On the large problems, NITRO and LOQO are equally robust and efficient" (p. 17);
- "a line search interior-point algorithm exhibits excellent robustness, as well as efficiency, compared to a trust-region method" (p. 17).

Caveats they state: "As we felt unqualified to tune either SNOPT or NITRO, we chose to run and compare all three codes on the default settings" (p. 15). They are the LOQO authors (conflict of interest noted by me). [observed]

- In his 2026 retrospective, Nocedal describes the rival without reference to the benchmark: Vanderbei "was trying to extend the ideas of quadratic programming with minimal changes and we were designing the elements from scratch … Vunder by [Vanderbei] finished first published loco [LOQO]" [1:18:21–1:18:55] [stated, P, caption-derived].

**4.3 LOQO authors vs KNITRO 1.00 (2002): the conjugate-gradient step** [observed, S]
Source: Benson, Shanno & Vanderbei, "A Comparative Study of Large-Scale Nonlinear Optimization Algorithms", ORFE-01-04 rev. 17 Jul 2002; in *High Performance Algorithms and Software for Nonlinear Optimization*, Springer 2003, pp. 95–127, doi:10.1007/978-1-4613-0241-4_5.

Cases:
- curly10: "knitro … performs up to 20001 conjugate gradient iterations per major iteration and as a result requires 954.58 seconds", against LOQO's 15.35 s (PDF p. 21);
- svanberg: up to 1260 CG iterations per major iteration (p. 19);
- in KNITRO's favour: cvxqp3 needs "only one to four conjugate gradient iterations at each step", 5.60 s against LOQO's 6173.21 s (p. 17);
- mixed equality/inequality NLPs: "knitro outperforms the other solvers largely due to the fact that it solves most of these problems on the defaults" (p. 19).

Conclusion (p. 22): "Results on sparse NLPs with sparse factorizations for the reduced KKT matrix strongly indicate that a true Newton step is more efficient than one employing conjugate gradients on this type of problem."

**Answered (4.2 + 4.3)** [practice, P]: R. A. Waltz, J. L. Morales, J. Nocedal & D. Orban, "An interior algorithm for nonlinear optimization that combines line search and trust region steps". Preprint 8 Sep 2004; *Math. Program.* 107 (2006) 391–408, doi:10.1007/s10107-004-0560-5.
- "The motivation for this paper is to develop a new interior point algorithm, implemented in the Knitro software package, which is more robust and efficient than either a pure trust region or a pure line search interior approach" (PDF p. 1).
- Mechanism: primal-dual steps by direct factorization with a line search, falling back to a trust-region CG step.
- It credits the rival: convexifying the Hessian "was first shown to be effective in the context of nonlinear interior methods by the Loqo software package" (p. 2).
- The paper does not name the Benson et al. benchmarks as its motivation. The link from critique to response is [inferred] from timing and content.

**4.4 IPOPT authors vs KNITRO 3.1.1 (2004): robustness and infeasibility detection** [observed, S]
Source: A. Wächter & L. T. Biegler, "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming". Preprint 19 Mar 2004 (Optimization Online 2004/03/836); *Math. Program.* 106 (2006) 25–57, doi:10.1007/s10107-004-0559-y.
- On 954 CUTEr problems: "IPOPT in default mode terminated successfully for 895 … KNITRO terminated successfully in 829 cases, and LOQO for 847 problems" (PDF p. 25).
- "KNITRO seems to require overall less function evaluations than IPOPT" (p. 25).
- On likely-infeasible problems: IPOPT produced "a user message indicating that the problem seems locally infeasible, whereas the other methods (except in two cases) exceeded the iteration limit" (p. 21).
- The filter's advantage over a penalty (merit) function, which KNITRO uses: "An evaluation of several line-search options has been presented, indicating increased robustness due to the filter approach" (p. 27).
- Caveats they state: "not meant to be a rigorous assessment" (p. 24); IPOPT used a tighter tolerance (1e-8 vs 1e-6).
- Collegial context: Nocedal commented on the rival manuscript. "We are also very grateful to Andrew Conn and Jorge Nocedal, whose comments on the manuscript greatly helped to improve the exposition" (p. 27).
- **Answered?**
  - The limitation was already stated in Nocedal's own 2005/2006 Knitro overview: it cannot distinguish infeasibility from convergence to an infeasible stationary point (`01-publications.md` §4.4) [stated, P].
  - It was then addressed in R. H. Byrd, F. E. Curtis & J. Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", *SIOPT* 20 (2010) 2281–2299, doi:10.1137/080738222. The abstract (Crossref) "addresses the need for nonlinear programming algorithms that provide fast local convergence guarantees regardless of whether a problem is feasible or infeasible". [practice, P; abstract only]

**4.5 Neutral and independent benchmarks** [observed, S]
- **COPS 3.0** (E. D. Dolan, J. J. Moré & T. S. Munson, "Benchmarking Optimization Software with COPS 3.0", ANL/MCS-TM-273, 2004, OSTI doi:10.2172/834714).
  - Compares FILTER, KNITRO 3.0, LOQO, MINOS and SNOPT per problem. Its method is stricter than self-benchmarks: tolerances are tightened until an independent "analyzer" accepts the solution (PDF p. 6).
  - It gives no overall ranking. The PDF's embedded fonts defeat text extraction, so I read only the introduction and one table as page images.
  - Henon problem (Table 22.2, PDF p. 56), m = 10: KNITRO returned f = 1.93254e+01 while FILTER and MINOS returned 7.21915e+00 (a different local solution); for m = 20, 40 KNITRO was fastest (70 s, 160.69 s).
  - The other 21 tables were **not read**.
- **Mittelmann, "AMPL-NLP Benchmark"** (plato.asu.edu/ftp/ampl-nlp.html, dated 9 Sep 2026; read):
  - KNITRO-16.0 solves 47 of 47 instances;
  - "scaled shifted geom mean" 1.17 against COPT 1, POUNCE 5.82, UNO 11.1, IPOPT 11.6, WORHP 11.8, FMINCON 37.0, CONOPT 38.4, SNOPT 103; solved counts 47 (KNITRO, COPT, POUNCE), 46 (IPOPT), 45 (WORHP, UNO), 39 (CONOPT), 36 (FMINCON), 30 (SNOPT); all codes "run in default mode";
  - this is the commercial Artelys code (developer R. Waltz), not Nocedal's research code [observed; attribution inferred from `01-publications.md`, `04-mentorship.md`].
  - Read together with 4.2–4.4 [inferred]: the weak points the rivals found in 2000–2004 (small-problem speed, CG cost, robustness on defaults) are no longer visible in this independent test.

**4.6 Fletcher's penalty-method example, absorbed into the design** [observed via practice, P]
Source: Byrd, Nocedal & Waltz, "Steering exact penalty methods for nonlinear programming". Preprint 10 Apr 2007; *OMS* 23 (2008) 197–213, doi:10.1080/10556780701394169.
- Diagnosis: Sℓ1QP-type methods "were never incorporated into production-quality software. We conjecture that this was mainly due to the difficulties of choosing the penalty parameter" (PDF p. 5).
- Test case: they use Fletcher's ADLITTLE example of how a fixed penalty parameter fails (pp. 14–15; "We confirmed this behavior experimentally").
- Credit: "We thank R. Fletcher for his comments in Example 3 concerning problem ADLITTLE, and N. Gould for many valuable discussions on penalty methods" (p. 20).
- The filter school (Fletcher–Leyffer; IPOPT) is the standing rival to the penalty/merit approach used in KNITRO; see 4.4 for IPOPT's claim. [observed]

---

## 5. Noisy and derivative-free optimization (2018–2024)

**5.1 His own concessions (pre-empting critics)** [stated, P]
Source: Shi, Xuan, Oztoprak & Nocedal, arXiv:2102.09762 v1 (19 Feb 2021) / *OMS* 38 (2023) 289–311, doi:10.1080/10556788.2022.2121832.
- "For noisy functions, we observed that newuoa is more efficient and accurate than the finite-difference l-bfgs method for unconstrained optimization, but not by a wide margin" (p. 6).
- "One striking observation from our study is that interpolation-based trust-region methods are more robust in the presence of noise than we expected … newuoa and dfo-ls do not require knowledge of the noise level in the objective function or estimates of derivatives, and yet performed reliably" (pp. 6–7).
- Limitations (p. 7):
  - "For each problem class, we employed only one established DFO code";
  - "Nonsmooth problems were not considered in this study";
  - "Perhaps the most important limitation of this study is that it considers only one model of noise: additive uniformly-distributed bounded noise."
- Existing procedures for estimating derivative bounds "are not robust" (p. 6).
- A WebSearch summary (search 2) repeats these concessions; I verified them in the arXiv text.

**5.2 Powell school: noise-level dependence** [observed, S]
Source: T. M. Ragonneau & Z. Zhang, "PDFO: a cross-platform package for Powell's derivative-free optimization solvers", *Math. Program. Comput.* 16 (2024) 535–559, doi:10.1007/s12532-024-00257-9 (arXiv:2302.13246, latest version, Oct 2024).
- The noise-adapted difference interval they test "relies on the knowledge of the noise level σ. In contrast, PDFO does not require the knowledge of σ and as we will see, provides better performance" (p. 14).
- "To summarize, the performance of finite-difference CG and BFGS is encouraging when there is no noise, yet much more care is needed when the problems are noisy" (p. 16).
- They cite Nocedal-group papers [43, 67, 68] for adapting the interval to noise.
- They credit adaptive-interval FD as sharing the geometry-control property, via [67] (Shi, Xie, Xuan & Nocedal, *SISC* 44 (2022), doi:10.1137/21M1452470) (p. 16).
- Caveat [inferred]: the finite-difference solvers tested are SciPy's CG and BFGS with a hand-set interval, not Nocedal's FDLM code with its noise estimation and recovery procedure. The critique hits the *class*, not his implementation.

**5.3 Direct-search school: nonsmoothness and efficiency** [observed, S]
Source: A. S. Berahas, O. Sohab & L. N. Vicente, "Full-low evaluation methods for derivative-free optimization", *OMS* 38 (2023) 386–411, doi:10.1080/10556788.2022.2142582 (arXiv:2107.11908, version 31 Oct 2022).
- On FD quasi-Newton line-search methods, including [9] = Berahas–Byrd–Nocedal: "These methods are moderately efficient and potentially scalable in the smooth case. However, when the objective function under consideration is non-smooth, such line-search methods are no longer suitable" (p. 3).
- Head-to-head with FDLM, the Berahas–Byrd–Nocedal code:
  - "In all the tests for smooth problems, FDLM … delivers poor efficiency but strong robustness" (p. 17);
  - on nonsmooth problems, "FDLM is not much better than these two [pDS, DFO-TR]. Note that none of these methods were designed to handle problems with non-smoothness" (p. 19).
- Berahas is Nocedal's former student and FDLM co-author, so this is critique from inside the lineage.
- Extension to bound and linear constraints: Royer, Sohab & Vicente, arXiv:2310.00755 (abstract only): FD steps give "good performance on smooth problems but at the expense of more function evaluations"; space-exploration steps handle "non-smoothness or noise in the objective better".

**5.4 Citing literature scanned** [observed, S]: the Semantic Scholar list of 31 works citing the 2023 FD paper (titles only). Only PDFO and Full-Low (above) engage it critically as far as titles and two abstracts show. Kimiaei & Neumaier, *Math. Program. Comput.* 2024 (doi:10.1007/s12532-024-00261-z) and Pham, Mordukhovich & Tran, *Math. Program.* 2025 (doi:10.1007/s10107-025-02255-8) were **not read**.

**5.5 Stated failures in this programme** (cross-reference): the regression-based quasi-Newton for noisy functions that "could never … scale up" (UCLA 2021, `02-methodology.md` F4). The 2009 geometry-phase claim was tested only in dimensions 2–15 (`01-publications.md` §4.4); its reception was not checked here either.

---

## 6. How Nocedal handles critique (process evidence) [stated/practice, P unless marked]

| Behaviour | Evidence |
|---|---|
| Invites refutation of surprising results | Purdue 2017 [0:35:39] "please shoot it down" (caption-derived) |
| Presents results with a hedge | "really good, but probably wrong" (2017); "one picture that I know is wrong" (2024) |
| Accepts hostile review as validation | 2026 [1:18:21]: "Mike Powell spent almost a year reviewing the paper because he told us he wanted to find something wrong in it but he couldn't … and he always finds something wrong in a paper" (caption-derived; paper unnamed) |
| Answers benchmarks with algorithms, not rebuttals | Knitro-Direct 2004/06; infeasibility detection 2010; steering 2007/08 (§4) [inferred pattern] |
| Concedes ML counter-evidence in one sentence and moves on | Progressive batching 2018, p. 2 (§1.3) |
| Pre-empts critics with a limitations section | FD-DFO 2021 §1.3 (§5.1) |
| Publishes his own corrections | L-BFGS-B Remark 2011; errata (`01` §4.1) |
| Does not answer every public critique | Abdi's 2019 OpenReview comments unanswered; no reply to Dinh, Hoffer or Shallue; the Lewis–Overton weak-Wolfe suggestion not adopted in L-BFGS-B 3.0 [practice] |
| Distrusts the ML review system | 2026 [1:36:48]: conference papers "reviewed by the PhD students, not by the professors. This a totally broken system. It's almost random, right?" (caption-derived) |
| Delegates the public defence to the student first author | All ICLR 2017 replies signed by Keskar (§1.1) [practice] |

---

## 7. Mapping to the seven layers (framework §一) [inferred]

- **Layer 1, taste.** Critics repeatedly reward what he values: robust defaults, careful benchmarks, codes over theory. Where his taste met a field with different norms (ML generalization), the critique was about the *experimental design* (budgets, learning-rate scaling, the measure), not the mathematics.
- **Layer 2, problem choice.** He enters fields with a strong prior imported from deterministic optimization ("batch methods should win"; "quasi-Newton after trying everything else"). Critiques cluster where that prior meets statistical or nonsmooth structure: ML generalization, nonsmooth BFGS, noise-level dependence.
- **Layer 4, execution.** The recurring external objection is **scope of evidence**: two batch sizes; dimensions 2–15; one noise model; one rival code per class; default settings. He often names the scope limit himself (§4.4 of `01`; §5.1). He does not always widen it before publishing.
- **Layer 5, judging results.** His own benchmarks and his rivals' benchmarks disagree in the direction of self-interest on both sides (LOQO, IPOPT, KNITRO authors each test on their own terms). The one independent, strict benchmark read (COPS 3.0) gives per-problem data, not a verdict.
- **Layer 6, expression.** "As is well known, sharp minima lead to poorer generalization" (2017 abstract) states as settled what critics then contested. Compare the careful limitations sections of the DFO papers.

## 8. Era and resource context

| Critique | Era and resources | Context for the critique |
|---|---|---|
| Benson–Shanno–Vanderbei | 2000–2002; SUN SPARC 400 MHz and AMPL | NITRO capped at 10,000 variables; three-person academic code teams |
| IPOPT | 2004; Pentium-class Linux, Fortran | IPOPT developed at CMU/IBM |
| COPS 3.0 | 2004; Pentium 4 1.8 GHz, 512 MB RAM (PDF p. 6) | |
| Keskar et al. | 2016 | Intel collaboration, a PhD student intern at Intel, single-node GPU-scale experiments [inferred from affiliations and the paper] |
| Critics of Keskar et al. | 2017–2019 | Google Brain (Shallue et al.: 168,160 models) and Facebook (Goyal et al.: 256 GPUs); far larger compute and metaparameter sweeps than the 2016 study [observed; asymmetry inferred] |
| Noise and DFO critiques | 2021–2024 | CUTEst via PyCUTEst, workstation scale, on both sides |

---

## Contradictions (kept, not reconciled)

1. **What the data-augmentation experiment showed (Keskar et al. 2017).** Four readings:
   - Paper (p. 6): these approaches "help reduce the generalization gap but still lead to relatively sharp minimizers and as such, do not completely remedy the problem". Its Table 6 (p. 14) shows augmented large-batch accuracy comparable to or above the augmented small-batch baseline (C2 90.26% vs 89.82%; C4 65.88% vs 63.05%; C1 82.50% vs 83.63%; C3 53.03% vs 54.55%).
   - Nocedal, Purdue 2017 [0:35:39]: "We did data augmentation to see if that would solve the problem. Various other techniques, there was still a gap. Less but there's still a gap."
   - Shallue et al. 2019 (p. 12): data augmentation "eliminated the difference in solution quality".
   - The paper judges by sharpness, the critics by accuracy.
2. **Does sharpness predict generalization?**
   - Jiang et al. 2019: Keskar's measure performs "the best overall".
   - Andriushchenko et al. 2023: sharpness "does not correlate well with generalization"; sharper minima sometimes generalize better out of distribution.
   - Dinh et al. 2017: sharpness can be made arbitrarily large by reparametrization.
   - Nocedal 2024: encouraging flat minimizers gives "better generalization".
3. **Where the generalization gap comes from.**
   - Keskar 2017: sharp minima, due to lack of gradient noise.
   - Hoffer 2017: "not related to the batch size but rather to the amount of updates".
   - Smith & Le 2018: the noise scale, with an optimum batch size at fixed learning rate.
   - Goyal 2017: "optimization difficulty", not generalization (on ImageNet).
   - Shallue 2019: "no evidence" of degradation once metaparameters and budgets are matched.
4. **L-BFGS in neural networks.**
   - LeCun 1987, as reported by Nocedal in 2026: "it didn't work well".
   - Le et al. 2011: L-BFGS/CG "significantly simplify and speed up" pretraining.
   - Nocedal's group 2018: "not considered an algorithm of choice".
5. **Robustness of the Byrd–Nocedal interior codes.** Different code versions and test sets, all kept:
   - NITRO 2000: "far less robust" on small problems (LOQO authors);
   - KNITRO 1.00: "outperforms the other solvers" on mixed NLPs on defaults (same authors, 2002);
   - KNITRO 3.1.1: 829/954, below LOQO 847 and IPOPT 895 (IPOPT authors, 2004);
   - KNITRO-16.0: 47/47, near-best geometric mean (Mittelmann, 2026).
6. **Line search or trust region?**
   - Benson et al. 2000: a line-search interior method "exhibits excellent robustness, as well as efficiency, compared to a trust-region method".
   - Byrd–Marazzi–Nocedal 2001: "A trust region approach, on the other hand, performs efficiently on the same example".
   - Waltz et al. 2004/06: a hybrid is "more robust and efficient than either".
7. **Finite differences vs model-based DFO under noise.**
   - Nocedal's group 2021: NEWUOA better "but not by a wide margin"; the FD approach "has much to be recommended" (abstract, p. 1, verified in the arXiv text). The same abstract states the assumption PDFO targets: "It is assumed that noise level is known or can be estimated by means of difference tables or sampling."
   - PDFO 2024: PDFO "provides better performance" without a noise estimate.
   - Full-Low 2023: FDLM "poor efficiency but strong robustness".
8. **Pre- vs post-publication judgement of the ICLR 2017 paper.**
   - ICLR program chairs: "All reviews (including the public one) were extremely positive".
   - Within two years, four independent groups published critiques of its design or interpretation (§1.2).
9. **Between research notes.** `03-process-evidence.md` (Gaps 2) says the NeurIPS 2016 multi-batch L-BFGS reviews are "not public or not found". This note found and read them at `papers.nips.cc/…/8ebda540cbcc4d7336496819a46a1b68-Reviews.html` (§2.1). The author rebuttal remains unpublished.
10. **1992 theoretical judgement vs later results.**
    - 1992: "Nobody has been able to construct an example in which the BFGS method fails".
    - Dai 2002: BFGS with Wolfe line searches "need not converge for nonconvex objective functions".
    - The 1992 "numerical experience" claim stands; the "no example exists" statement does not.

## Gaps (could not find or did not read)

1. **OpenReview (live) and the Wayback Machine were blocked** for me (bot challenge; "Blocked by egress policy"). The ICLR 2017 thread was read only from agent 03's saved snapshot of 2024-03-21. Later comments, if any, are unknown.
2. **No published reply** by Nocedal or Keskar to Dinh et al., Hoffer et al., Goyal et al. or Shallue et al. was found, beyond the one-sentence concession in the 2018 ICML paper. One WebSearch (search 1) looking for reviewer or rebuttal content returned only the papers themselves.
3. **Not read, metadata only**:
   - Wächter & Biegler 2000 (content taken from two readers who did read it);
   - Dai 2002 (abstract only), Dai 2013 and Mascarenhas 2004.
   - Whether *Numerical Optimization* (2nd ed.) discusses the BFGS counterexamples: **not read**.
4. **Lewis & Overton**: only the December 2008 preprint was read. Whether the published 2013 version keeps the L-BFGS-B recommendation is unchecked. Whether Nocedal ever responded is unknown. That the later SciPy L-BFGS-B port (a C translation) added a weak-Wolfe option was not checked.
5. **COPS 3.0**: 21 of 22 per-problem tables not read (the PDF's embedded fonts defeat text extraction; no OCR available). No overall KNITRO record was compiled.
6. **Mittelmann logs** (`plato.asu.edu/ftp/ampl-nlp_logs/`) and other Mittelmann NLP pages were not read. Older snapshots (to date when KNITRO's position changed) were not reachable (Wayback blocked).
7. **NeurIPS 2016 author rebuttal**, and ICML 2018 / NIPS 2012 reviews: not public.
8. **Critiques of the noise / FD programme** beyond PDFO and Full-Low: the citing list was scanned by title only. OpenAlex's daily budget was exhausted, and Semantic Scholar returned HTTP 429 for some queries.
9. **Rejected papers and referee reports**: none found beyond the interview anecdotes (L-BFGS 1980 reviews; Powell's review of an unnamed Knitro theory paper).
10. **Critique of the SIAM Review 2018 survey, the dynamic-sampling "norm test" line, or the weather / data-assimilation work**: none found. The only self-critique found is the 2018 abstract's claim that the new inner-product test "improves upon the well known norm test" (arXiv:1710.11258).
11. **Complexity-theory school**: no published reply to Nocedal's criticism of complexity results (`02-methodology.md` C4) was found or searched for (budget).
12. **zbMATH reviews** of *Numerical Optimization* (1st and 2nd eds., reviewer N. Curteanu) are descriptive. They contain no criticism beyond noting that the treatment of modelling "is light" (1999 review).

## Sources

Retrieval date for all: 2026-09-28. P = primary (Nocedal's own words, work, code, or the review record of his paper); S = secondary.

**Nocedal's papers, code, and review record**
1. N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy & P. T. P. Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", ICLR 2017, arXiv:1609.04836 v2 (read in part: abstract, pp. 2, 4, 6, 9, 13–14) — P
2. OpenReview forum H1oyRlYgg (ICLR 2017 paper76): reviews, author replies, decision. Read from agent 03's saved Internet Archive snapshot (2024-03-21) of `api.openreview.net/notes?forum=H1oyRlYgg`; live site not reachable — P (review record)
3. R. Bollapragada, D. Mudigere, J. Nocedal, H.-J. M. Shi & P. T. P. Tang, "A Progressive Batching L-BFGS Method for Machine Learning", ICML 2018 (PMLR 80), arXiv:1802.05374 (pp. 1–2 read) — P
4. A. S. Berahas, J. Nocedal & M. Takáč, "A Multi-Batch L-BFGS Method for Machine Learning", NIPS 2016, arXiv:1605.06049 (abstract page) — P
5. L. Bottou, F. E. Curtis & J. Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Rev.* 60 (2018), doi:10.1137/16M1080173 (arXiv:1606.04838; p. 39 passage) — P
6. R. H. Byrd, S. L. Hansen, J. Nocedal & Y. Singer, "A Stochastic Quasi-Newton Method for Large-Scale Optimization", *SIOPT* 26 (2016), doi:10.1137/140954362 (arXiv:1401.7020, abstract) — P
7. R. Bollapragada, R. Byrd & J. Nocedal, "Adaptive Sampling Strategies for Stochastic Optimization", arXiv:1710.11258 / *SIOPT* 28 (2018), doi:10.1137/17M1154679 (abstract) — P
8. J. Nocedal, "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1 (1992) 199–242, doi:10.1017/S0962492900002270 (author preprint `acta.pdf`, pp. 21–22) — P
9. R. H. Byrd, M. Marazzi & J. Nocedal, "On the convergence of Newton iterations to non-stationary points", preprint OTC 2001/01 (`failofconv.pdf`) / *Math. Program.* 99 (2004), doi:10.1007/s10107-003-0376-8 (abstract, pp. 2–3, 22–23 read) — P
10. R. A. Waltz, J. L. Morales, J. Nocedal & D. Orban, "An interior algorithm for nonlinear optimization that combines line search and trust region steps", preprint 8 Sep 2004 (http://users.iems.northwestern.edu/~nocedal/PDFfiles/directpaper.pdf) / *Math. Program.* 107 (2006) 391–408, doi:10.1007/s10107-004-0560-5 (pp. 1–4, 14–15 read) — P
11. R. H. Byrd, J. Nocedal & R. A. Waltz, "Steering exact penalty methods for nonlinear programming", preprint 10 Apr 2007 (http://users.iems.northwestern.edu/~nocedal/PDFfiles/steering.pdf) / *OMS* 23 (2008) 197–213, doi:10.1080/10556780701394169 (pp. 1, 4–5, 13–15, 20 read) — P
12. R. H. Byrd, F. E. Curtis & J. Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", *SIOPT* 20 (2010) 2281–2299, doi:10.1137/080738222 (abstract via Crossref) — P
13. H.-J. M. Shi, M. Q. Xuan, F. Oztoprak & J. Nocedal, "On the Numerical Performance of Derivative-Free Optimization Methods Based on Finite-Difference Approximations", arXiv:2102.09762 v1 / *OMS* 38 (2023) 289–311, doi:10.1080/10556788.2022.2121832 (pp. 6–7 read) — P
14. L-BFGS-B version 3.0 (March 2011), Fortran source `lbfgsb.f` and README, from the author tarball on http://users.iems.northwestern.edu/~nocedal/lbfgsb.html (extracted copy in the shared scratch folder) — P (code)
15. J. Nocedal, Purdue IE Distinguished Seminar, 2017-02-15, https://www.youtube.com/watch?v=srg3Rx2HvfQ; transcript `../sources/talks/2017-02-15_purdue-distinguished-seminar_srg3Rx2HvfQ.txt` (uploader captions; 0:29–0:44 read) — P
16. J. Nocedal, "How is it Possible to Train Deep Neural Networks?", NITMB, 2024-10-25, https://www.youtube.com/watch?v=XrX7MEMbdYw; transcript `../sources/talks/2024-10-25_nitmb-seminar-train-dnns_XrX7MEMbdYw.txt` (ASR; 0:08–0:28 read) — P
17. "Subject to" interview with J. Nocedal, 2026-03-18, https://www.youtube.com/watch?v=CfR-llfmb6E; transcript `../sources/talks/2026-03-18_subject-to-interview_CfR-llfmb6E.txt` (ASR; 0:47–0:54, 1:17–1:19, 1:32–1:38 read) — P

**Critiques of the large-batch / sharp-minima paper and related studies**
18. L. Dinh, R. Pascanu, S. Bengio & Y. Bengio, "Sharp Minima Can Generalize For Deep Nets", ICML 2017 (PMLR 70), arXiv:1703.04933 v2 (pp. 1–2, 6–7, 9 read) — S
19. E. Hoffer, I. Hubara & D. Soudry, "Train longer, generalize better: closing the generalization gap in large batch training of neural networks", NeurIPS 2017, arXiv:1705.08741 v2 (pp. 1–3, 8–9 read) — S
20. P. Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", arXiv:1706.02677 v2 (abstract, p. 2) — S
21. C. J. Shallue, J. Lee, J. Antognini, J. Sohl-Dickstein, R. Frostig & G. E. Dahl, "Measuring the Effects of Data Parallelism on Neural Network Training", *JMLR* 20 (2019), arXiv:1811.03600 (abstract, pp. 10–12) — S
22. D. Masters & C. Luschi, "Revisiting Small Batch Training for Deep Neural Networks", arXiv:1804.07612 (abstract, p. 1) — S
23. S. L. Smith & Q. V. Le, "A Bayesian Perspective on Generalization and Stochastic Gradient Descent", ICLR 2018, arXiv:1710.06451 (pp. 1, 3, 5–7) — S
24. Y. Jiang, B. Neyshabur, H. Mobahi, D. Krishnan & S. Bengio, "Fantastic Generalization Measures and Where to Find Them", arXiv:1912.02178 v1 (2019) (pp. 1–2, 10) — S
25. M. Andriushchenko, F. Croce, M. Müller, M. Hein & N. Flammarion, "A Modern Look at the Relationship between Sharpness and Generalization", ICML 2023 (PMLR 202), arXiv:2302.07011 (abstract, pp. 1–2) — S

**Stochastic quasi-Newton: reviews, rivals, independent evidence**
26. NIPS 2016 reviews of "A Multi-Batch L-BFGS Method for Machine Learning" (Paper ID 611), https://papers.nips.cc/paper_files/paper/2016/file/8ebda540cbcc4d7336496819a46a1b68-Reviews.html (read in full) — S (public referee reports)
27. A. S. Berahas & M. Takáč, "A robust multi-batch L-BFGS method for machine learning", *OMS* 35 (2020) 191–219, doi:10.1080/10556788.2019.1658107 (arXiv:1707.08552, abstract) — S (former student; journal follow-up without Nocedal)
28. P. Moritz, R. Nishihara & M. I. Jordan, "A Linearly-Convergent Stochastic L-BFGS Algorithm", AISTATS 2016, arXiv:1508.02087 v2 (pp. 1–2, 7) — S
29. Q. V. Le, J. Ngiam, A. Coates, A. Lahiri, B. Prochnow & A. Y. Ng, "On Optimization Methods for Deep Learning", ICML 2011, https://icml.cc/2011/papers/210_icmlpaper.pdf (abstract, p. 1) — S

**Quasi-Newton theory counterexamples and nonsmooth BFGS**
30. Y.-H. Dai, "Convergence Properties of the BFGS Algoritm", *SIOPT* 13(3) (2002) 693–701, doi:10.1137/S1052623401383455 (abstract via Crossref) — S
31. W. F. Mascarenhas, "The BFGS method with exact line searches fails for non-convex objective functions", *Math. Program.* 99 (2004) 49–61, doi:10.1007/s10107-003-0421-7 (metadata only) — S
32. Y.-H. Dai, "A perfect example for the BFGS method", *Math. Program.* 138 (2013) 501–530, doi:10.1007/s10107-012-0522-2 (metadata only) — S
33. A. S. Lewis & M. L. Overton, "Nonsmooth optimization via quasi-Newton methods", *Math. Program.* 141 (2013) 135–163, doi:10.1007/s10107-012-0514-2; author preprint "Nonsmooth Optimization via BFGS" (Dec 2008), https://cs.nyu.edu/overton/papers/pdffiles/bfgs_inexactLS.pdf (abstract, p. 4, p. 29 read) — S

**Constrained NLP rivals and benchmarks**
34. A. Wächter & L. T. Biegler, "Failure of global convergence for a class of interior point methods for nonlinear programming", *Math. Program.* 88 (2000) 565–574, doi:10.1007/PL00011386 (metadata only; content via sources 9 and 35) — S
35. H. Y. Benson, D. F. Shanno & R. J. Vanderbei, "Interior-Point Methods for Nonconvex Nonlinear Programming: Jamming and (Comparative) Numerical Testing", ORFE-00-02 rev. 28 Aug 2000, https://vanderbei.princeton.edu/ps/loqo3_5.pdf / *Math. Program.* 99 (2004) 35–48, doi:10.1007/s10107-003-0418-2 (pp. 1–2, 12, 14–17 read) — S
36. H. Y. Benson, D. F. Shanno & R. J. Vanderbei, "A Comparative Study of Large-Scale Nonlinear Optimization Algorithms", ORFE-01-04 rev. 17 Jul 2002, https://vanderbei.princeton.edu/tex/loqo5/loqo5_5.pdf / Springer 2003, doi:10.1007/978-1-4613-0241-4_5 (pp. 7, 10–22 read) — S
37. A. Wächter & L. T. Biegler, "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming", preprint 19 Mar 2004, https://optimization-online.org/wp-content/uploads/2004/03/836.pdf / *Math. Program.* 106 (2006) 25–57, doi:10.1007/s10107-004-0559-y (pp. 1, 21, 24–27 read) — S
38. E. D. Dolan, J. J. Moré & T. S. Munson, "Benchmarking Optimization Software with COPS 3.0", ANL/MCS-TM-273 (2004), doi:10.2172/834714, https://www.osti.gov/servlets/purl/834714 (PDF pp. 3, 5–6, 55–56 viewed as images) — S
39. H. D. Mittelmann, "AMPL-NLP Benchmark" (dated 9 Sep 2026), https://plato.asu.edu/ftp/ampl-nlp.html (read) — S

**Noisy / derivative-free rivals**
40. T. M. Ragonneau & Z. Zhang, "PDFO: a cross-platform package for Powell's derivative-free optimization solvers", *Math. Program. Comput.* 16 (2024) 535–559, doi:10.1007/s12532-024-00257-9 (arXiv:2302.13246, pp. 3, 13–16, 20, 24) — S
41. A. S. Berahas, O. Sohab & L. N. Vicente, "Full-low evaluation methods for derivative-free optimization", *OMS* 38 (2023) 386–411, doi:10.1080/10556788.2022.2142582 (arXiv:2107.11908, pp. 1–3, 13–22) — S
42. C. W. Royer, O. Sohab & L. N. Vicente, "Full-Low Evaluation Methods For Bound and Linearly Constrained Derivative-Free Optimization", arXiv:2310.00755 (abstract) — S
43. Semantic Scholar Graph API, citations of doi:10.1080/10556788.2022.2121832 (31 citing works, titles), plus paper records for doi:10.1007/s12532-024-00261-z, doi:10.1007/s10107-025-02255-8, doi:10.3390/a16020084 — S

**Reviews, databases, searches**
44. zbMATH Open API: reviews of *Numerical Optimization* 1st ed. (Zbl 0930.65067) and 2nd ed. (Zbl 1104.65059) by N. Curteanu; review of Nash & Nocedal 1991 (Zbl 0756.65091) by P. Stavre — S
45. Crossref REST API: metadata checks for every DOI in this file — S
46. WebSearch 1 (2026-09-28): `Keskar Nocedal "sharp minima" ICLR 2017 openreview reviewer comments large-batch criticism`. It returned the papers only, no review text; it confirmed Dinh et al. appeared in ICML 2017 Vol. 70 — S
47. WebSearch 2 (2026-09-28): `"finite-difference" derivative-free Shi Xuan Oztoprak Nocedal comparison criticized model-based NEWUOA noisy benchmark response`. It returned the paper's own concessions, which were then verified in the arXiv text — S

**Scratch materials** (not committed): `/tmp/nonlinear-team-scratch/base-skills/jorge-nocedal/critique/`. It holds the arXiv, NeurIPS, OSTI, Vanderbei, Optimization Online and Overton PDFs with their extracted text, the Mittelmann page, the Crossref, zbMATH and Semantic Scholar JSON, and the COPS page images.
