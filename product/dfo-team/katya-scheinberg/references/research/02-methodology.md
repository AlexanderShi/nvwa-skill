# 02 · Stated methodology (what Scheinberg SAID about method)

> Research date: 2026-09-27. Evidence base: search-result snippets only. No transcript, interview text, or full article body could be read (WebFetch blocked for siam.org, cornell.edu, lehigh.edu, gatech.edu, mathopt.org, wikipedia.org).
> **Big caveat:** the stated-methodology layer for Scheinberg is thin in what could be retrieved. Most "stated" evidence below is (a) titles and one-line descriptions of Scheinberg's own essays, talks and tutorials, (b) the framing sentences of author-written abstracts, and (c) institutional bios (usually author-approved). None is a long-form "how I do research" text. This file records only what was said; whether it was done is checked in 03-process-evidence.md.

## A. Scheinberg's own essays, talks, tutorials (primary, but title/summary level)

| # | Item | What it states (paraphrase unless quoted) | Layer | URL | Cred. |
|---|---|---|---|---|---|
| A1 | SIAM News essay "Knowing What to Know in Stochastic Optimization", by Katya Scheinberg, SIAM News vol. 52 issue 02, March 2019 | Title frames the central question as *what an algorithm needs to know* (which accuracy, from which oracle) rather than how to reduce variance everywhere. Search summary: the article "describes novel continuous optimization algorithms, which lie at the core of most foundational data science topics" (summary wording, paraphrase). | Taste / idea generation | https://www.siam.org/publications/siam-news/articles/knowing-what-to-know-in-stochastic-optimization/ | primary (title + summary only) |
| A2 | Lehigh lecture "Stochastic Oracles and Where to Find Them" | Title again puts the **oracle** (what information is available, how reliable) at the centre of the method. | Taste / problem framing | https://engineering.lehigh.edu/node/172051 | primary (title only) |
| A3 | Tutorial video "Introduction to derivative-free and zeroth order optimization II" (YouTube) | Pairs classical DFO with ML's "zeroth-order optimization" under one heading — treats them as the same field. | Framing / bridging | https://www.youtube.com/watch?v=5j8LvlbzsJQ | primary (title only) |
| A4 | Distinguished Tutte Lecture, University of Waterloo C&O | Invited distinguished lecture (content not retrieved). | — | https://uwaterloo.ca/combinatorics-and-optimization/distinguished-tutte-lecture-katya-scheinberg | primary (existence only) |
| A5 | Lehigh ISE Spencer C. Schantz Technical Talk (as Georgia Tech faculty) | Content not retrieved. | — | https://engineering.lehigh.edu/news/article/lehigh-ise-spencer-c-schantz-technical-talk-katya-scheinberg-georgia-institute | primary (existence only) |

## B. Author-written framing in abstracts (primary; these are claims Scheinberg and co-authors chose to foreground)

| # | Paper | Stated framing (paraphrase of snippet unless in quotes) | Layer |
|---|---|---|---|
| B1 | Cartis & Scheinberg, Math. Program. 2018 | "the use of probabilistic models only increases the complexity by a constant, which depends on the probability of the models being good" (abstract wording as shown in search result). → Stated standard for a good stochastic result: **same order as the deterministic method, randomness costs only a constant.** | Result judgement |
| B2 | Paquette & Scheinberg, SIOPT 2020 | The expected-iteration bound "matches the complexity bound of deterministic gradient descent up to constants" (snippet; treat as paraphrase-level). Same standard as B1. | Result judgement |
| B3 | Jin, Scheinberg & Xie, SIOPT 2024 | Unlike stochastic gradient methods, the algorithm does not use pre-specified step sizes but adapts them according to estimated progress (paraphrase). → Stated preference: **adaptivity over hand-tuned schedules.** | Taste / method |
| B4 | Chen, Menickelly & Scheinberg, Math. Program. 2018 | Models and estimates must be accurate "with high enough, but fixed, probability" (snippet). → Stated modelling choice: fixed probability, not increasing-to-one. | Method |
| B5 | Cao, Berahas & Scheinberg, Math. Program. 2024 | Oracles "are not assumed to be unbiased or consistent" (paraphrase); relaxed acceptance + cautious radius update. → Stated aim: weaken oracle assumptions as far as possible. | Method |
| B6 | Berahas, Cao, Choromanski & Scheinberg, FoCM 2022 | Title: "A theoretical **and empirical** comparison…" → Stated evaluation standard: compare competing estimators both ways. | Experiment design |
| B7 | Chaudhry & Scheinberg, arXiv:2510.14935 (2025) | Classical model-based trust-region methods "can have the same worst case complexity as any other known DFO method" (snippet). → Stated position: Powell-type model-based DFO is **not** theoretically inferior to direct search / finite-difference methods. | Taste / agenda |
| B8 | Chaudhry, Scheinberg & Sun, arXiv:2609.09441 (2026) | Methods "closest to methods initially proposed and implemented by Powell" made "theoretically competitive"; random subspaces give what they "believe to be nearly tight complexity" (snippet). | Agenda |
| B9 | Scheinberg & Toint, SIOPT 2010 | Geometry-improving steps "cannot be completely eliminated" for global convergence, but can be confined to the final stage (paraphrase). → Stated standard: identify the minimal necessary safeguard. | Method |
| B10 | Scheinberg et al., arXiv:2511.19411 (2025) | A "unified" framework encompassing line search and trust region under corrupted gradients and heavy-tailed function noise (paraphrase). → Stated aim: one analysis template for many adaptive methods. | Method |

## C. Bios and book blurb (primary for self-description; secondary when written by institutions)

| # | Source | Stated content | Cred. |
|---|---|---|---|
| C1 | SIAM News author bio (via search summary) | Research interests "lie in the development of efficient and theoretically sound algorithms for continuous optimization and machine learning" (wording as shown in search summary). | primary-ish (author bio) |
| C2 | IDFO book blurb (SIAM 2009; Amazon/Google Books records) | Book presents DFO methods "designed to efficiently and rigorously solve optimization problems", covering "direct search to model-based approaches"; Scheinberg "authored the open source DFO software" (blurb wording via search summary; paraphrase-level). | primary (co-authored publisher text) |
| C3 | Georgia Tech / KAUST / Wikipedia bios | Service record (MOS Chair from July 2025; co-editor Math. Programming; past EiC Mathematics of Operations Research; past chair SIAG/OPT; EiC SIAM-MOS book series; editor of Optima). Signals the community-building layer, not method. | secondary |

## D. Recurring stated themes (≥3 appearances across A–C)

1. **Oracle-first framing** — A1, A2, B4, B5, B10 (5×). What the oracle guarantees, and with what probability, is the problem definition.
2. **Deterministic-parity standard** — B1, B2, B7, B8 (4×). A stochastic or DFO method is "good" when its complexity matches the deterministic/best-known order, with randomness costing constants.
3. **Classical adaptive methods, not schedules** — B3, B4, B5, B10 (4×). Keep line search / trust region; let the step size adapt.
4. **Theory and empirics together** — B6, B8, C1 ("efficient and theoretically sound"), C2 (3–4×).
5. **DFO ≡ zeroth-order optimization** — A3, B6, C1 (3×).

## E. Stated-but-unverified / missing

- No retrieved text where Scheinberg describes *how problems are chosen*, *how papers are written*, or *how mentoring is done*. Those layers have **no stated evidence** here.
- No retrieved quote on reviewing standards or on critiques of other approaches.
