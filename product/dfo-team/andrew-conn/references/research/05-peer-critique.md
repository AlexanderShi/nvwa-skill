# 05 · Peer critique, limits, later developments

Research date: 2026-09-27. No personal disputes were found or are implied. Everything below is a **methodological difference evidenced by publications**. Several items are not critiques of Conn by name; they are later results that bound where the Conn line of methods applies.

## 1. Is geometry management worth its cost? (the central DFO critique)

| Work | What it shows | Relation to Conn's method | Source | Credibility |
|---|---|---|---|---|
| Fasano, Morales, Nocedal, "On the geometry phase in model-based algorithms for derivative-free optimization", *Optim. Methods Softw.* 24 (2009) 145–154 | Numerical study of a model-based algorithm that **dispenses with the geometry phase altogether**. Tracks the interpolation-matrix condition number and gradient accuracy on smooth problems with n = 2–15. Widely read as evidence that practical performance can survive without explicit geometry steps. | Challenges the *practical necessity* of the poisedness maintenance at the heart of CST 1997 / CSV 2008–2009 | https://www.tandfonline.com/doi/abs/10.1080/10556780802409296 | Primary (critic's own paper) |
| Scheinberg & Toint, "Self-correcting geometry in model-based algorithms for derivative-free unconstrained optimization", *SIAM J. Optim.* 20(6) (2010) 3512–3532 | Geometry-improving steps **cannot be completely eliminated** if global convergence is wanted, but they can be confined to the final stage, where criticality is checked. | A partial vindication *and* a refinement from inside Conn's own circle | https://optimization-online.org/2009/02/2216/ | Primary |
| "Avoiding geometry improvement in derivative-free model-based methods via randomization" (arXiv 2305.17336) | Title indicates randomized models remove explicit geometry steps. Authors not confirmed in snippet. | Later direction (unverified details) | https://arxiv.org/pdf/2305.17336 | ⚠️ lead only |

**Takeaway for the skill:** the Conn lens should defend geometry control as *the thing that makes the theorem true*. It should also admit, citing the two works above, that practical codes may do less of it and still work well on smooth problems.

## 2. Benchmarking standards moved beyond the CUTE-style comparison

| Work | Point | Source |
|---|---|---|
| Moré & Wild, "Benchmarking derivative-free optimization algorithms", *SIAM J. Optim.* 20(1) (2009) 172–191 | Introduces **data profiles** for DFO under computational-budget constraints, on smooth, noisy and piecewise-smooth problem sets. The unit of cost is function evaluations, not iterations. | https://www.mcs.anl.gov/~more/dfo/ (primary) |
| Rios & Sahinidis, "Derivative-free optimization: a review of algorithms and comparison of software implementations", *J. Global Optim.* 56(3) (2013) 1247–1293 | 22 implementations on 502 problems. Global/multistart solvers (e.g., TOMLAB/MULTIMIN, TOMLAB/GLCCLUSTER, MCS, TOMLAB/LGO) did best on average for solution quality within 2,500 evaluations (snippet). This shows that local model-based methods are not automatically the best choice when the goal is the best solution in a fixed budget. | https://www.semanticscholar.org/paper/Derivative-free-optimization:-a-review-of-and-of-Rios-Sahinidis/580b166bab3796ccf35abdff6b0677986913a5d6 (primary) |

**Implication:** the IBM promotional comparison (4 vs 351 iterations; 82 vs 23,402 simulations against NOMAD, per https://researcher.watson.ibm.com/researcher/view_group.php?id=3346) should be treated cautiously. The problem, the tolerances, whether gradient information was used, and the NOMAD settings are not stated. A Moré–Wild-style data profile would be the fair test. The Conn lens must *apply its own benchmarking discipline* to such claims.

## 3. Limits evidenced by Conn's own later work

- **Constraints and nonsmoothness.** In 2018 Conn co-authored a trust-region method that *imports* the progressive barrier from the MADS school. It is "competitive with COBYLA" on 40 smooth problems and "can be competitive with NOMAD" on nonsmooth MDO problems (DOI 10.1007/s10589-018-0020-4). Smooth-model methods did not dominate on nonsmooth engineering problems.
- **Direct search plus models.** Conn & Le Digabel (2013) show quadratic models improve MADS "significantly". The best practical recipe was a hybrid, not a pure model-based method.
- **Own software superseded.** LANCELOT was replaced by IPOPT inside IBM's circuit tuner (MAM 2015 profile). The augmented-Lagrangian approach was overtaken by interior-point filter methods for that application.

## 4. Where the field went after Conn (context for roundtable disagreements)

| Development | Source | Status |
|---|---|---|
| Comprehensive review organising DFO by assumptions on the black box (deterministic/noisy/stochastic, smooth/nonsmooth, structured) | Larson, Menickelly, Wild, "Derivative-free optimization methods", *Acta Numerica* 28 (2019) 287–404, DOI 10.1017/S0962492919000060 | ✅ primary |
| "Fully linear / fully quadratic" model theory (from the CSV monograph) became the common language for later model-based DFO analyses, including probabilistic and random-subspace variants | Secondary descriptions in later arXiv papers (e.g., https://arxiv.org/pdf/2605.30845) | ✅ as a description of influence (secondary) |
| Powell's own survey of DFO algorithms | Powell, "A view of algorithms for optimization without derivatives", DAMTP 2007/NA03 | ✅ title/author/year. **Content regarding Conn not read**, so no claim is made about Powell's view of CSV geometry. |

## 5. Critiques NOT found (declared)

- No published critique of LANCELOT/CUTE by name was retrieved.
- No reproduction failures, errata or retractions were found for Conn's papers. *Update 2026-09-27:* the full-text reading and the book material found public errata, none a retraction: D001 (1981, with Coleman), S059 (1989, with Gould and Toint) and the authors' errata for two printings of the 2009 book (B002, B003; 2015). See §6 and `08-deep-reading-synthesis.md` §12.
- No direct Conn rebuttal to Fasano–Morales–Nocedal was found.


## 6. Reviews of *Introduction to Derivative-Free Optimization* (2009) (added 2026-09-27)

Two published reviews of the book, read in full from the copies on the authors' book page (cards B005 and B006 in `cards/k01.md`). Everything below is the **reviewer's voice**, not Conn's; passages of the book that a reviewer quotes are marked *relayed*. The book is joint work with Scheinberg and Vicente, and its body was not read here, so these are readings of the book, not checks of it.

### 6.1 J. L. Nazareth, *Mathematics of Computation* 79(271), July 2010, pp. 1867–1869 (DOI 10.1090/S0025-5718-10-02379-3) [B005]

| Point | The reviewer's words or reading | Page |
|---|---|---|
| Problem class | Problems that are "benign": reasonably smooth, unconstrained, with relatively few variables ("say up to a hundred"), hard because derivatives cannot be supplied and evaluations are expensive or noisy | p. 1 |
| DFO vs nonsmooth optimization | DFO algorithms "remain gradient-related", since their convergence relies on smoothness; non-differentiable optimization uses subgradients | p. 1 |
| Aim (relayed) | The preface's main aims include "a detailed description of the basic theory to the extent that the reader can well understand what is needed to ensure convergence, how it affects algorithm design, and what kind of success one can expect and where" (book pp. xi–xii) | p. 1 |
| Structure | Part I "nicely organized and well presented"; the first direct-search chapter considers global convergence "for both continuously differentiable and nonsmooth cases"; the trust-region chapters are "the centerpiece of the monograph", with two frameworks and first- and second-order convergence proofs underlying the "DFO" approach, Powell's methods and wedge methods; Part III brief; the software appendix "a useful list" | pp. 1–2 |
| Criticisms | Exercises mostly elaborate the theory, which limits use in an introductory course; the introductory examples are, in the book's words (relayed, book p. 3), "atypical of applications of derivative-free optimization but are easy to understand"; "few numerical illustrations" and no implementation details, "its focus is not on the “algorithmic engineering” side of the subject"; no one-dimensional derivative-free methods (Brent); "The important intersection between derivative-free optimization and non-differentiable optimization is not adequately addressed." | pp. 2–3 |
| Verdict | The authors met their main goals "admirably"; "gracefully-written, well-organized, and timely"; useful guidance to practitioners and theoretical advice to software developers. His framing of the book as "emblematic" of algorithmic science & engineering rests on his own SIAM News article and is not used by the skill | p. 3 |

### 6.2 Dominique Orban, *SIAM Review* 53(2), 2011, Book Reviews, pp. 395–396 [B006]

Year: the batch file and INDEX.md first gave 2010; Crossref dates the Book Reviews section of *SIAM Review* 53(2) to 2011 (pp. 375–405, DOI 10.1137/SIREAD000053000002000375000001), and its editor's note lists a derivative-free-optimization review. INDEX.md, `works.json` and the k01 digest now say 2011.

| Point | The reviewer's words or reading | Page |
|---|---|---|
| Standing | "bound to become the de facto authoritative text"; "one of the very few textbooks available on this topic"; "essential both as an introductory text and as a reference volume"; the authors "central players in the field" | pp. 1–2 |
| Motivating example | The introduction's first application, "the tuning of algorithmic parameters—a nonsmooth noisy problem", is his "personal favorite" | p. 1 |
| Comparison of methods | The introduction gives a taste of how kinds of method compare, but "This is, however, the only comparison between methods to be found in the book"; relayed stance: comparing derivative-free methods "is intricate and is not an objective of the book" | p. 1 |
| Limitations and structure | Readers learn both families "as well as about their limitations—an aspect I particularly appreciated"; Part I (background) and Part II (algorithms) are separated, so a reader can start with the algorithms and refer back | p. 1 |
| Rigor | Part I's "clarity, consistency, and rigor" make Nelder–Mead "almost a simple and didactic illustration of the direct-search framework" | p. 2 |
| Smooth vs nonsmooth | A reader of *Trust-Region Methods* "will appreciate the clearly stated similarities and differences" between smooth and derivative-free trust-region methods; that book gives 30 pages to nonsmooth trust-region minimization, while this one (in his paragraph on the trust-region model-based chapters) assumes a Lipschitz-continuous gradient or Hessian and a well-poised sample set (a difference of context, not called a flaw) | p. 2 |
| Surrogates | A surrogate plays "the role of a fortune teller"; to the practitioner a good surrogate "may turn out to be the most important ingredient" | p. 2 |
| Criticisms | Exercises mostly extend the theory and there are few examples; he wishes the Part II exercises asked for "bare-bones implementations"; the software the book points to is "research grade and not necessarily accessible to the nonexpert" | p. 2 |

### 6.3 What the skill takes from the reviews

- **Agreement between the two**: exercises that extend the theory; few numbers or examples; limited treatment of nonsmooth problems (for Nazareth the overlap with non-differentiable optimization is "not adequately addressed", a flaw; for Orban the model-based chapters assume a Lipschitz-continuous gradient or Hessian, a difference of context); the Part I/Part II split works.
  - ⚠ Neither places nonsmooth problems wholly outside the book: its contents list §7.4 "Global convergence in the nonsmooth case" [B001 p. 2], and Nazareth reports that Ch. 7 covers global convergence "for both continuously differentiable and nonsmooth cases" [B005 p. 2]. ✗ Corrected on review: the first version of this line said both put nonsmooth problems outside the book.
- **Disagreement**: Nazareth sees limited use in an introductory course; Orban calls the book appropriate for a graduate class. Nazareth places the simplex-gradient line-search chapter between the two classes; Orban files it under model-based methods.
- **Used in SKILL.md** (attributed to the reviewer by name): the Reception row of the first Signature Work, the Method 1 "Book level" variant, warning sign 7, the Domain fit caution for hyperparameter tuning, and the Roundtable blind spots. Not used as evidence of Conn's personal practice (`08-deep-reading-synthesis.md` §12.4).
