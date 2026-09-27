# 03 · Process evidence (what Conn actually DID)

Research date: 2026-09-27. Only abstracts and bibliographic snippets could be read, so this is behavioural evidence about paper structure, software and application at the level of abstracts. No code was inspected: the COIN-OR DFO repository page could not be fetched, and LANCELOT sources were not examined.

## 1. The theory → code → test chain, repeated across three eras

| Era | Theory | Code / artefact | Testing | Evidence (primary records) |
|---|---|---|---|---|
| Bound-constrained trust regions (1988) | CGT, SINUM 25(2):433–460 — global convergence for "a class" of TR algorithms with bounds; weak Hessian-accuracy assumptions; reduces to unconstrained after finitely many iterations under strict complementarity | (feeds LANCELOT) | CGT, Math. Comp. 50(182):399–430 — "results of a series of tests upon a class of new methods" | https://www.jstor.org/stable/2157325 ; https://www.numerical.rl.ac.uk/media/people/nick-gould/ConnGoulToin88_mc.pdf |
| Large-scale constrained NLP (1991–1996) | CGT 1991 SINUM 28(2):545–572 augmented Lagrangian (global convergence; penalty parameter bounded away from zero; inner stopping rules designed for bounds) | LANCELOT Release A (Springer 1992) + input format later shared with CUTE (SIF) | CGT 1996 Math. Programming 73:73–110 "intensive numerical tests" of Release A options; CUTE (ACM TOMS 1995) | DOI 10.1137/0728030 ; DOI 10.1007/978-3-662-12211-2 ; DOI 10.1007/BF02592099 ; DOI 10.1145/200979.201043 |
| DFO (1996–2001) | CST 1997 (Powell festschrift) general convergence framework using the Sauer–Xu interpolation error bound | DFO package, COIN-OR (Conn, Scheinberg, Toint) | Conn–Toint 1996: 20 examples with and without noise; CST 1998 "…in practice" at the AIAA MDO symposium (an engineering venue) | DOI 10.1007/978-1-4899-0289-4_3 ; https://projects.coin-or.org/Dfo ; https://researchportal.unamur.be/en/publications/a-derivative-free-optimization-algorithm-in-practice/ |

**Reading:** in each era the convergence theory, a runnable code, and a test on a collection *including the conditions practitioners face* (bounds, large scale, noise) are all produced within a few years. That is the core behavioural signature.

## 2. Test infrastructure as research output

- **CUTE** (Bongartz, Conn, Gould, Toint, ACM TOMS 21(1):123–160, 1995): a "versatile environment for testing small- and large-scale nonlinear optimization algorithms" with a major problem collection in SIF (snippet). Successor environments CUTEr (ACM TOMS 29(4), 2003) and CUTEst (Comput. Optim. Appl., 2015) exist (https://dl.acm.org/doi/10.1145/962437.962439 ; https://link.springer.com/article/10.1007/s10589-014-9687-3). Their author lists were not shown in the snippets, so Conn's role in them is unconfirmed. Primary for CUTE itself.
- **Late-career testing habits**, from the Audet–Conn–Le Digabel–Peyrega 2018 abstract: 40 smooth constrained problems against COBYLA, plus nonsmooth multidisciplinary engineering problems against NOMAD. The result is claimed as "competitive", not "superior" (DOI 10.1007/s10589-018-0020-4). Primary. This shows two benchmark tiers (academic set + engineering set) and a baseline chosen from the *other* school.

## 3. Industrial practice at IBM

| Project | What was done | Evidence |
|---|---|---|
| Circuit tuning: JiffyTune (1998) | A fast circuit simulator plus time-domain sensitivities, fed to a general-purpose NLP package. Features: minimax and power optimization, simultaneous transistor/wire tuning, recovery from nonworking circuits, designer-friendly interfaces that automate the problem specification. | IEEE TCAD 17(12):1292–1309 — https://ieeexplore.ieee.org/document/736569/ (primary) |
| EinsTuner (1999–2005) | Static-timing formulation, so no user input patterns are needed. Gradient-based NLP with per-component time-domain simulation and gradient computation. Later, a large-scale nonconvex NLP solved with an interior-point method. | DAC 1999 pp. 452–459, DOI 10.1145/309847.309979 ; Wächter, Visweswariah, Conn, FGCS 21(8):1251–1262 (2005) (primary) |
| Tool evolution | The optimizer inside the circuit tool was LANCELOT and was **later replaced** by IPOPT (interior-point filter method). The tool became "a standard tool within IBM" for all custom circuits (paraphrase). | MAM 2015 profile — https://ww2.amstat.org/mam/2015/highlighted/MAM2015profile_Conn.pdf (primary-ish) |
| Recognition | IBM Outstanding Technical Achievement Award with Ruud Haring and Chandu Visweswariah | SIAM News obituary (secondary) |
| Energy (from 2006) | Seat on the technical board of NTNU's Center for Integrated Operations (from 2006), working with Statoil. Hosted NTNU summer interns at IBM each year. Started an oil-and-gas optimization project. The IBM page claims their model-based approach needed 4 iterations / 82 well simulations versus NOMAD's 351 / 23,402 on one case. | IBM Research group page — https://researcher.watson.ibm.com/researcher/view_group.php?id=3346 (secondary, **promotional**; the comparison set-up is unknown, and the figures are not peer-reviewed as quoted) |
| Shale gas | Lagrangian-relaxation decomposition for well scheduling (with Knudsen, Grossmann, Foss), Computers & Chemical Engineering 2014 | dblp (secondary aggregator) |
| Air traffic | Local continuous optimization for conflict resolution (with Peyronne, Mongeau, Delahaye), EJOR 2015 | dblp |
| Earth observation | Robust matrix completion for cloud removal in satellite image sequences (with Wang, Olsen, Lozano), CVPR 2016 | dblp |

**Reading:**
1. Conn did not insist on DFO when derivatives could be had. The flagship industrial project was *gradient-based*, with derivatives from simulator sensitivities.
2. Conn did not insist on his own solver either. LANCELOT was swapped for IPOPT when that served the users better.
3. Applications were entered through people: a colleague's question, a workshop, a board seat, interns.

## 4. How the DFO theory papers are built (from abstracts)

- **Build the object before the algorithm.** CSV 2008 (Math. Programming) is about the *geometry of interpolation sets* (poisedness, error estimates) independent of any specific algorithm. CSV 2008 (IMA JNA) extends the same concepts to regression (more points) and underdetermined interpolation (fewer points), and shows that "the mechanisms and concepts controlling sample set quality and approximation error bounds extend" (paraphrase).
- **Then one general theorem.** CSV 2009 proves first- and second-order global convergence for *general* DF trust-region algorithms that use such models.
- **Then consolidate in a book** (IDFO 2009) that teaches both the model-based and the direct-search frameworks.
- Timeline detail: CSV 2008 Math. Programming was received 27 Sept 2004, accepted 24 March 2006, and appeared online Dec 2006 (Springer snippet). That is a long, careful theory pipeline.

## 5. Hybridization with the direct-search school (2011–2018)

- Conn & Le Digabel 2013: quadratic models inside MADS's search step. Intensive tests show significant improvement (abstract).
- Audet, Conn, Le Digabel, Peyrega 2018: the progressive-barrier constraint handling (a MADS-school device) moved *into* a trust-region method. Models are built around the best feasible *and* best infeasible points.
- Amaioua, Audet, Conn, Le Digabel 2018: solves the quadratically constrained quadratic subproblems inside MADS with (i) an ℓ1 exact penalty, (ii) an augmented Lagrangian, and (iii) a new combination of the two. These are Conn's 1973–1991 tools reused 30+ years later.

## 6. Failures, abandonments, negative results

- None are documented publicly in what was found. Implicit evidence: the LANCELOT → IPOPT replacement inside EinsTuner, and a "competitive" rather than "better" claim in 2018. **Gap declared.**

## 7. Era and resource context

- 1970s–80s: university setting, Fortran, small test sets. Waterloo students did much of the work.
- 1990s: Fortran packages built by a three-country trio (Conn at IBM, Gould at Rutherford Appleton Laboratory, Toint at Namur). CUTE/SIF was a shared infrastructure.
- 1996–2010: an industrial research lab with access to real simulation problems and in-house engineers. That resource is not available to most users of this skill.
