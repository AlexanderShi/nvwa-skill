# 05 · Peer Critique, Limits, Competing Approaches

> Rule: only methodological differences evidenced by publications. No personal conflict is implied or should be inferred.

## C1 · Counterexample to the discontinuous-functions theorem (direct critique)

- **What**: Audet, Bouchet & Bourdin, "Counterexample and an additional revealing poll step for a result of 'analysis of direct searches for discontinuous functions'", Math. Program. 208 (2024) 411–424, DOI 10.1007/s10107-023-02042-3. The arXiv v1 was titled "Erratum, counterexample and an additional revealing poll step…" (arXiv:2211.09947).
- **Content (search summary)**: a function satisfying all assumptions of the theorem announced in the last part of Vicente & Custódio (Math. Program. 133 (2012) 299–325) contradicts some of its conclusions. The flaw: a directional direct search can converge to a point where f is discontinuous and lower semicontinuous, with f there strictly below lim f(x_k), while generating trial points in only one continuity set. The fix is an additional "revealing" poll step.
- **Lesson for the skill**: the push to extend direct-search theory to ever-weaker smoothness classes has a real failure mode. Claims at the edge of the theory (discontinuity) need adversarial counterexample checking.
- Source: https://link.springer.com/article/10.1007/s10107-023-02042-3 ; https://arxiv.org/pdf/2211.09947 (primary; secondary with respect to Vicente)

## C2 · Sharpness check on probabilistic descent (critique that confirms)

- **What**: Huang & Zhang, "Non-convergence Analysis of Probabilistic Direct Search", arXiv:2606.01320 (May 2026). Zhang co-authored the original 2015 paper.
- **Content**: asks whether the submartingale-like assumption in the existing theory "is essential or merely an artifact". For convex objectives, when polling directions satisfy a probabilistic *ascent* condition, non-convergence has positive probability. For uniform random directions on the sphere, fewer directions than the theory's threshold means the method is **not** globally convergent. So the assumption is essential.
- **Implication**: the GRVZ threshold is sharp, which validates the theory. It is also a hard limit: "use 1 random direction to save evaluations" is unsafe; the direction count must meet the probabilistic-descent threshold.
- Source: https://arxiv.org/abs/2606.01320 (secondary, peer)

## C3 · Competing globalization school: mesh / integer lattice (Audet–Dennis MADS line)

- **Evidence**: Audet, Dennis & Le Digabel, "Globalization strategies for Mesh Adaptive Direct Search", COAP 46 (2010) 193–215, DOI 10.1007/s10589-009-9266-1. The search summary says the convergence theory "does not enforce a notion of sufficient decrease" because iterates lie on a scaled, translated integer lattice.
- **Contrast with Vicente**: Vicente's line relies on sufficient decrease (a forcing function ρ(α)) and needs no mesh. That choice is what makes iteration counting possible (Vicente 2013 abstract: "based on imposing sufficient decrease"). The MADS line keeps simple decrease and mesh structure, which is natural for discrete or granular variables and for the progressive-barrier constraint handling of that school.
- **Where they collide**: multiobjective (DMS 2011 vs DMulti-MADS, COAP 2021, which reports Δ-spread profiles comparing BiMADS, DMS, DMulti-MADS, MOIF, NSGA-II per search summary), constraints (merit function + extreme barrier in Gratton & Vicente 2014 vs progressive barrier in MADS), and discontinuous analysis (C1).
- Sources: https://link.springer.com/article/10.1007/s10589-009-9266-1 ; https://link.springer.com/article/10.1007/s10589-021-00272-9 (primary for the other school)

## C4 · Intrinsic limits stated in Vicente's own work

| Limit | Source |
|---|---|
| Worst-case evaluation complexity of directional DS is O(n²ε⁻²), and the n² factor is **optimal** for this class, so direct search is intrinsically dimension-hungry | Dodangeh, Vicente & Zhang 2016, https://link.springer.com/article/10.1007/s11590-015-0908-1 |
| Nonsmooth via smoothing costs "roughly one order of magnitude" in complexity | Garmanjani & Vicente 2013 |
| Pareto-sensitivity knees need scalarization and 1st/2nd derivatives | arXiv:2501.16993 |
| Non-monotone acceptance makes analysis "significantly more challenging" | arXiv:2609.11567 |
| SMG multi-gradient direction is **biased** even with unbiased per-objective gradients | Liu & Vicente 2021, arXiv:1907.04472 |

## C5 · Competing approach: model-based trust-region DFO (Powell / Conn–Scheinberg lineage)

- The 2009 book itself treats model-based methods (interpolation, geometry control) as the second main framework alongside direct search (book description). The table of contents confirms this at title level: Part II has two direct-search chapters, one on simplex-derivative line search and two on trust regions, and Part I has a chapter on ensuring well poisedness [B001 pp. 1–3]. One reviewer calls the trust-region part the book's "centerpiece" (C7) [B005 p. 2]. Vicente works on both. Vicente's *own* direct-search papers import models only into the **search step** (SID-PSM 2007, MFN 2010), where the poll step carries convergence. The model-based school makes model quality and geometry management the core of the algorithm.
- Vicente's probabilistic-model TR work (2014, 2018) relaxes the deterministic "fully linear every iteration" requirement of the classical model-based theory to a probabilistic one. That is a methodological departure from deterministic geometry control.
- Contradictory evidence about neural or learned surrogates in DFO exists (Bian & Xie, arXiv:2608.24963, 2026, not about Vicente). It is relevant because Vicente's rule of keeping the true function as the acceptance judge ("a surrogate that proposes candidates the true objective must still approve helps", Bian & Xie's finding) is consistent with the search/poll separation. This is an inference linking two sources.

## C6 · Gaps in the critique record

- No published rebuttal or response by Vicente to C1 was found.
- No public review reports or OpenReview threads (the optimization journals Vicente publishes in do not have open review). Published book reviews exist for the 2009 book and are read (C7).
- No critique found of the DMS benchmarking metrics or of the Lehigh-era fairness formulation. Absence of evidence, not evidence of absence.

## C7 · Published reviews of the 2009 book (peer view; added 2026-09-27)

> Voice: every claim below is the reviewer's. The book is joint (Conn, Scheinberg & Vicente), so the reviews assess three authors' work, not Vicente's alone. Cards: `cards/k01.md` (B005, B006); decisions: `08-deep-reading-synthesis.md` §12.

**Nazareth, *Mathematics of Computation* 79(271), July 2010, pp. 1867–1869** [B005]
- Scope as he states it: the book's problems are "benign" (reasonably smooth, unconstrained, "say up to a hundred" variables), yet hard because derivatives are unavailable and evaluations are expensive or noisy [B005 p. 1].
- Reading: Part I is well-presented "mathematical machinery". "The discussion of the other main class of methods—trust-region algorithms based on derivative-free linear and quadratic models—is the centerpiece of the monograph." [B005 p. 2].
- Criticisms:
  - the exercises are mostly elaborations of theory, which "diminishes the book’s usefulness as a textbook for an introductory course" [B005 p. 2];
  - "few numerical illustrations" and "no implementational details" [B005 p. 3];
  - no one-dimensional derivative-free methods (Brent) [B005 p. 3];
  - "The important intersection between derivative-free optimization and non-differentiable optimization is not adequately addressed." [B005 p. 3].
- Verdict: "gracefully-written, well-organized, and timely" [B005 p. 3]. His "theoretical algorithmic science mode" frame comes from his own 2006 article [B005 p. 3], so it is his lens, not the authors'.

**Orban, *SIAM Review* 53(2), 2011, book reviews pp. 395–396** [B006] (volume, issue and year are not in the text: Crossref places the Book Reviews section of 53(2), online 5 May 2011, at pp. 375–405, DOI 10.1137/SIREAD000053000002000375000001; the batch file first listed 2010)
- Verdict: he expects the book to become the authoritative text on its subject [B006 p. 1], and calls it "essential both as an introductory text and as a reference volume" [B006 p. 2].
- Strengths: "In the course of the book, the reader learns about both direct-search methods and model-based methods, as well as about their limitations—an aspect I particularly appreciated." [B006 p. 1]; the clarity of Part I; the notes and bibliography [B006 p. 2].
- Criticisms: the introduction gives a taste of how the methods compare in practice, and "This is, however, the only comparison between methods to be found in the book." [B006 p. 1]. He reports the authors as saying that comparing derivative-free methods is intricate and not an objective of the book [B006 p. 1]. The exercises are mostly extensions of the theory, with few examples; most of the software pointed to is research grade; he wishes for "bare-bones implementations" as exercises [B006 p. 2].

**Across the two reviews**
- Agree: theory-heavy exercises, few numerics or examples, weak implementation support [B005 pp. 2–3; B006 p. 2].
- Disagree: use as an introductory textbook, and whether trust region is the centre of the book or one of two frameworks [B005 p. 2; B006 pp. 1–2].

**Bearing on the skill** (methodological, not personal)
- Method 5: a genre variant (a theory-first book whose one comparison of methods is in its introduction), not a contradiction.
- Taste mark 7 / H10: a peer singles out the treatment of limitations.
- Method 4: the book's scope is smooth; the nonsmooth overlap is named as a gap. Vicente's own nonsmooth papers (2008–2013) are chronology only; no source links them to the review.

