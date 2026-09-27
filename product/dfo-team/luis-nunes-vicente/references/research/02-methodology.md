# 02 · Stated Methodology (what Vicente SAID about method)

> Scope: statements by Vicente (alone or as a co-author speaking in the author voice of an abstract or talk description) about *how* to do the research: aims, design principles, what counts as a good result. Whether Vicente actually does this is checked in 03-process-evidence.md.
>
> **Evidence gap, stated up front**: no interview, "how I do research" essay, PhD-advice piece or transcribed lecture by Vicente turned up in ~45 searches. The stated layer therefore rests on (a) one on-record quote, (b) talk abstracts, (c) the author-voice framing in paper abstracts and the book description. Abstract framing is weaker evidence of personal methodology than an essay would be, and it is co-authored. Treat everything here as **stated in a publication voice**, not as personal testimony.

## Layer 1 · Research taste

| # | Statement | Exact / paraphrase | Source | Credibility |
|---|---|---|---|---|
| S1 | "I have been interested in optimization all my research life, from various viewpoints: Theory and algorithms, software development, and industrial applications." Also: "I am thus eager to chair a Department of Industrial and Systems Engineering where optimization and operations research play such a crucial role." | **Exact** (quoted in Lehigh news, shown in search result) | https://engineering.lehigh.edu/news/article/industrial-and-systems-engineering-welcomes-luis-nunes-vicente-new-chairs (2018) | primary (on-record quote) |
| S2 | The DFO book explains "how these methods are designed to efficiently and rigorously solve optimization problems". Rigor and efficiency are named together. | Paraphrase of book description (co-authored with Conn and Scheinberg; may be publisher copy) | http://www.mat.uc.pt/~lnv/idfo/ ; https://books.google.com/books/about/Introduction_to_Derivative_Free_Optimiza.html?id=tGbUshriSyYC | primary-ish (book blurb) |
| S3 | Full-low evaluation methods are a "new class of rigorous methods" designed to deliver "efficient and robust numerical performance for functions of all types, from smooth to non-smooth, and under different noise regimes". | Paraphrase close to abstract wording (via search summary) | https://arxiv.org/pdf/2107.11908 | primary (abstract) |

## Layer 2 · Problem choice

| # | Statement | Exact / paraphrase | Source | Credibility |
|---|---|---|---|---|
| S4 | Goal of the stochastic-DFO line: "new probabilistic strategies for enforcing sufficient decrease conditions in stochastic derivative-free optimization, with the goal of reducing sample complexity and simplifying convergence analysis". | Paraphrase of the talk abstract (search summary) | Pitt IE seminar: https://calendar.pitt.edu/event/ie-seminar-luis-nunes-vicente-reducing-sample-complexity-in-stochastic-derivative-free-optimization-via-tail-bounds-and-hypothesis-testing-416 ; Rice CMOR colloquium (same title): https://events.rice.edu/event/419767-cmor-colloquium-series-luis-nunes-vicente-lehigh | primary (talk abstract) |
| S5 | The knee-solution paper computes Pareto knees "according to their verbal (informal) definition of least maximal change". The stated aim is to formalize a practitioners' informal notion. | Paraphrase close to abstract | https://arxiv.org/abs/2501.16993 | primary (abstract) |
| S6 | Two-level stochastic formulations "have become instrumental in machine learning contexts such as continual learning, neural architecture search, adversarial learning, and hyperparameter tuning". Problem choice is justified by ML demand. | Paraphrase (search summary of abstract) | https://arxiv.org/abs/2110.00604 | primary (abstract) |

## Layer 3 · Idea generation

| # | Statement | Exact / paraphrase | Source | Credibility |
|---|---|---|---|---|
| S7 | "Recent numerical results indicated that randomly generating the polling directions without imposing the positive spanning property can improve the performance". A numerical observation motivates new theory. | Paraphrase close to abstract | https://www.zhangzk.net/docs/publications/2015dspd.pdf | primary (abstract) |
| S8 | Evolution strategies: show "how to modify a large class of evolution strategies … to achieve global convergence". The modifications consist "essentially" of reducing the step size when a sufficient-decrease condition fails. | Paraphrase | https://link.springer.com/article/10.1007/s10107-014-0793-x | primary (abstract) |
| S9 | DMS "does not aggregate any of the objective functions" and is "inspired by the search/poll paradigm of direct-search methods of directional type". | Paraphrase close to abstract | https://epubs.siam.org/doi/10.1137/10079731X | primary (abstract) |
| S10 | SMG is "seen as an extension of the classical stochastic gradient method for single-objective optimization". The Tran–Vicente framework "recover[s] classical convergence rates of single-objective methods". | Paraphrase | https://arxiv.org/abs/1907.04472 ; https://arxiv.org/abs/2605.12432 | primary (abstract) |

## Layer 4 · Experiments and execution

| # | Statement | Exact / paraphrase | Source | Credibility |
|---|---|---|---|---|
| S11 | Minimum Frobenius norm models are used to "improve the performance of direct-search methods". The models are built from "the set of previously evaluated points generated during a direct-search run". | Paraphrase | https://link.springer.com/article/10.1007/s10589-009-9283-0 | primary (abstract) |
| S12 | SID-PSM combines "global convergence properties with the efficiency of the use of quadratic polynomials to enhance the search step and of the use of simplex gradients for guiding the function evaluations of the poll step". | Paraphrase close to software page | http://www.mat.uc.pt/sid-psm/ | primary (software page) |

## Layer 5 · Judging results

| # | Statement | Exact / paraphrase | Source | Credibility |
|---|---|---|---|---|
| S13 | Direct search with sufficient decrease "shares the worst case complexity bound of steepest descent". The benchmark for judging a DFO method is the corresponding gradient method. | Paraphrase close to abstract | https://link.springer.com/article/10.1007/s13675-012-0003-7 | primary (abstract) |
| S14 | Smoothing direct search has complexity "roughly one order of magnitude worse" than smooth direct search. The cost of generality is stated explicitly. | Paraphrase | https://optimization-online.org/2012/01/3331/ | primary (abstract) |
| S15 | Pareto-sensitivity approach: "restricted to scalarized methods … and requires the computation or approximations of first- and second-order derivatives". Limitations are stated in the abstract. | Paraphrase | https://arxiv.org/abs/2501.16993 | primary (abstract) |
| S16 | Non-monotone direct search "can help navigate narrow curved valleys; however, its theoretical analysis is significantly more challenging due to the lack of monotonic decrease". | Paraphrase | https://arxiv.org/abs/2609.11567 | primary (abstract) |

## Layer 6 · Communication

- No stated writing advice found. The book is described as the "first contemporary comprehensive treatment" of DFO, organized around two frameworks, direct search and model-based (book page, search summary). *Inference*: Vicente communicates through framework → theory → software → numerics papers. See 03 for practice.

## Layer 7 · Research organization

- S1 above (theory + algorithms + software + applications as one career-long programme).
- The SIAM Fellow citation (2024), written by others, credits "exemplary leadership in editorial and organizational service to the SIAM community" (quoted in search result from Lehigh news). This is service, not a stated method.
- No statement found on how Vicente runs a group, chooses students, or allocates time.

## Claims repeated ≥3 times (strongest stated signals)

1. **Rigor + efficiency together** (S2, S3, S12, and the ES and PSwarm abstracts in 03). Stated in at least 4 separate texts across 2007–2023.
2. **Extend a known single-objective or deterministic method; do not invent from scratch** (S8, S9, S10, the merit-function abstract "equip direct-search methods").
3. **Measure against the gradient method's rate** (S13, S10 "recovering classical convergence rates", and the tail-bound abstract's sample-count comparison).
4. **Reduce cost (evaluations/samples) while simplifying analysis** (S4, S7, S11).

## Contradictions or evolutions over time

- **Early (2007–2016)**: DFO means directional direct search with a poll step that guarantees convergence. **Later (2019–2026)**: gradient-based stochastic multi-objective and bilevel methods (S6, S10). The Pareto-sensitivity work requires first- and second-order derivatives (S15). This is a scope widening, not a stated reversal; no source explains the pivot in Vicente's words. Speculation: the ML focus of Lehigh ISE and funding (AFOSR FA9550-23-1-0217, ONR N000142412656 are acknowledged in arXiv:2509.14505).
