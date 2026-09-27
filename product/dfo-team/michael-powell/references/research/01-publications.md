# 01 · Publications: landscape and signature-work anatomy

Research date: 2026-09-27. Method: web-search results plus directly reading Powell's original Fortran distributions (READMEs, cover emails, code comments) as mirrored in the PRIMA repository. `scripts/fetch_publications.py` could not reach OpenAlex from this environment, so this landscape was built by hand. **First pass (sections 1–2): no full-text reading of papers**; paper content there comes from abstracts and search snippets only. Where a claim goes beyond those, it is marked *(inference)* or *(speculation)*.

**Deep-reading pass (same date, section 0 and section 3):** the full publication list was then harvested from Google Scholar (with DBLP and Crossref), every listed work was carded, and 35 works were read in full text. Section 0 gives the coverage; section 3 lists what the full texts change in sections 1–2. Where the two passes disagree, the full texts and `08-deep-reading-synthesis.md` §3 take precedence.

Credibility tags: **[primary]** = Powell's own paper, report, code or cover note · **[secondary]** = obituary, memoir, benchmark or successor project.

---

## 0. Coverage from the Google Scholar list (deep-reading pass)

Sources: `../sources/publications/scholar.md` (the list, sorted by citations, with an audit note), `../sources/publications/works.json` (all records including duplicates), the full-text index `../sources/papers/INDEX.md` (Full text, Role and Read columns), the card index `07-paper-cards.md` and the synthesis `08-deep-reading-synthesis.md`.

| Item | Count | Note |
|---|---|---|
| Google Scholar rows | 211, plus 2 DBLP-only items = 213 records | profile `p3kDmy0AAAAJ`, harvested 2026-09-27 |
| Duplicate or junk records | 29 | marked `dup_of` in `works.json` |
| Distinct works | 184 | 115 with a DOI (checked against Crossref titles); none on arXiv |
| Card entries | 187 | 184 works + R007 (Royal Society memoir, secondary) + X001 (SIAM oral history, 2005) + X002 (CIM Bulletin interview, 2003) |
| Full text read | 35 works (30 full + 5 partial: S057, S074, S078, S121, S170) + R007, X001, X002 | S186 is the same text as S165 and counts once |
| Abstract-level cards | 73 entries (72 works; S175 and S048 are one work at two stages) | no open full text |
| Metadata-only cards | 75 | 11 non-research items; 4 books or edited volumes |
| Skipped | 0 | |

Full-text reads by period (full or partial / carded research works; from `08-deep-reading-synthesis.md` §1): 1960–64 1/7; 1965–69 1/24; 1970–74 0/23; 1975–79 0/17; 1980–84 1/25; 1985–89 2/19; 1990–94 3/20; 1995–99 7/15; 2000–04 8/9; 2005–09 7/7; 2010–15 5/5. The derivative-free period after 1997 is read almost completely; before it, only eight classics have open full texts (S001 1963, S019 1968, S139 1983, S050 1986, S115 1989, S030 1990/91, S090 1990, S089 1992).

Read level of the most-cited works (Scholar citations, 2026): of the ten most cited, two were read in full, S001 (DFP, 7118) and S007 (BOBYQA, 2462). The others are abstract- or metadata-level: S002 (1964 conjugate directions, 6999, abstract), S003 (1978 SQP, 2942, metadata), S004 (1969 augmented Lagrangian, 2709, metadata), S005 (1987 RBF review, 2672, metadata), S006 (1977 CG restarts, 2635, abstract), S008 (COBYLA, 2391, abstract), S009 (Approximation Theory and Methods, 1925, abstract) and S010 (1990 RBF report, 1530, abstract). Of the top twenty, S014, S018 and S019 were also read in full. So the method evidence rests on the DFO reports and a few classics, not on the most-cited early papers.

---

## 1. Publication landscape (DFO-relevant, hand-built)

| Year | Item | Venue / ID | What it shows about *how* Powell worked | Source | Cred. |
|------|------|-----------|------------------------------------------|--------|-------|
| 1964 | "An efficient method for finding the minimum of a function of several variables without calculating derivatives" | Computer Journal 7(2):155–162 | Early derivative-free work. It takes the simple "change one parameter at a time" method and alters it so that it chooses conjugate directions on a quadratic (per abstract snippet). | https://academic.oup.com/comjnl/article-abstract/7/2/155/335330 | primary |
| 1992 | COBYLA report | DAMTP 1992/NA5 (Cambridge); presented at the Oaxaca, Mexico conference, Jan 1992 | The code was mailed out with the report on 7 May 1992, two years before the book chapter appeared. The report was followed by release of the code. | Powell's COBYLA cover email, `fortran/original/cobyla/email.txt` in https://github.com/libprima/prima | primary |
| 1994 | "A direct search optimization method that models the objective and constraint functions by linear interpolation" | In *Advances in Optimization and Numerical Analysis* (eds Gomez, Hennart), Kluwer, pp. 51–67. DOI 10.1007/978-94-015-8330-5_4 | Linear interpolation on a simplex, with a trust region. Each constraint gets its own model. | https://link.springer.com/chapter/10.1007/978-94-015-8330-5_4 | primary |
| 1998 | "Direct search algorithms for optimization calculations" | Acta Numerica 7:287–336. DOI 10.1017/S0962492900002841 | Written as "a collection of essays" that covers line searches, discrete grids, simplices, conjugate directions and linear/quadratic-model trust regions (abstract snippet). Before building the next solver, Powell surveyed every family of methods. | https://www.cambridge.org/core/journals/acta-numerica/article/abs/direct-search-algorithms-for-optimization-calculations/23FA5B19EAF122E02D3724DB1841238C | primary |
| 2000/2002 | "UOBYQA: unconstrained optimization by quadratic approximation" | Report DAMTP 2000/NA14 (per code header); Math. Programming 92:555–582 (2002). DOI 10.1007/s101070100290 | Full quadratic interpolation with (n+1)(n+2)/2 points. The paper openly reports that results look promising for n ≤ 20 and that larger n is a problem because each iteration costs O(n⁴) work (search snippet). | https://link.springer.com/article/10.1007/s101070100290 | primary |
| 2004 | "Least Frobenius norm updating of quadratic models that satisfy interpolation conditions" | Math. Programming Ser. B 100:183–215. DOI 10.1007/s10107-003-0490-7 | Theory written specifically to make the next solver cheap. The leftover freedom in the model is fixed by minimizing the Frobenius norm of the change to the Hessian. The inverse of an (m+n+1)×(m+n+1) system then gives the Lagrange functions (abstract snippet). | https://link.springer.com/article/10.1007/s10107-003-0490-7 | primary |
| 2004/2006 | "The NEWUOA software for unconstrained optimization without derivatives" | Report DAMTP 2004/NA08; in *Large-Scale Nonlinear Optimization* (eds Di Pillo, Roma), Springer 2006, pp. 255–297. DOI 10.1007/0-387-30065-1_16 | Uses m = 2n+1 interpolation points with O((m+n)²) work per iteration "to allow for large n" (snippet). The code was mailed on 16 Dec 2004. | https://link.springer.com/chapter/10.1007/0-387-30065-1_16 | primary |
| 2007 | "A view of algorithms for optimization without derivatives" | Mathematics Today 43:170–174; DAMTP 2007/NA03 | Powell's own positioning essay: noisy functions, non-random methods, McKinnon's Nelder–Mead failure example, pattern-search convergence, and his quadratic-model work. It reports that functions of more than 100 variables can be minimized. | https://optimization-online.org/2007/06/1680/ ; https://www.damtp.cam.ac.uk/user/na/NA_papers/NA2007_03.pdf | primary |
| 2009 | "The BOBYQA algorithm for bound constrained optimization without derivatives" | Report DAMTP 2009/NA06 (report only; code README dated 5 Jan 2009) | Extends NEWUOA to bounds. Adds the ALTMOV and RESCUE routines to keep the interpolation set usable when points press against the bounds. | https://www.damtp.cam.ac.uk/user/na/NA_papers/NA2009_06.pdf ; https://optimization-online.org/2010/05/2616/ | primary |
| 2013 | LINCOA Fortran code (no introductory paper) | Cover note dated 6 Dec 2013: "I intend to write a paper that explains briefly the main features of the software." | Code came first and the documentation was planned for later. PRIMA notes that "Powell did not publish a paper to introduce the algorithm." | `fortran/original/lincoa/README.txt`, https://github.com/libprima/prima | primary |
| 2015 | "On fast trust region methods for quadratic models with linear constraints" | Math. Programming Computation 7(3):237–267. DOI 10.1007/s12532-015-0084-4 | Covers only LINCOA's trust-region subproblem, not the whole algorithm (snippet). | https://link.springer.com/article/10.1007/s12532-015-0084-4 | primary |

**Leads not verified (⚠️ in RESOURCES.md, not cited as fact):** "Beyond symmetric Broyden for updating quadratic models in minimization without derivatives" (Springer URL seen, DOI 10.1007/s10107-011-0510-y, but no author or year in the snippet). "Developments of NEWUOA for unconstrained minimization without derivatives" (Optimization Online PDF seen, venue unconfirmed). Powell's pre-DFO landmark papers from memory: the DFP formula with Fletcher (1963), the 1970 hybrid/dogleg method, the 1969 augmented Lagrangian paper, the 1978 SQP paper, the 1984 PRP counterexample. The *contributions* are confirmed in secondary sources: the OMS obituary snippet credits the BFGS convex global-convergence proof, the original augmented-Lagrangian idea and the first (1970) trust-region convergence result; Buhmann's 2019 abstract mentions "the famous DFP formula". The individual titles, however, were not verified here.

### Pattern in the landscape (inference)
- **A single long series of solvers (1992–2013).** COBYLA → UOBYQA → NEWUOA → BOBYQA → LINCOA. Each new solver either relaxes one limitation of its predecessor (model order, per-iteration cost, constraint type) or adds one constraint class. Evidence: NEWUOA README, "The new software was developed from UOBYQA …" [primary].
- **Report first, code by email, book chapter or journal later.** DAMTP reports (1992/NA5, 2000/NA14, 2004/NA08, 2009/NA06) appear before the formal publications. BOBYQA and LINCOA never received a standard journal paper introducing the full algorithm [primary: READMEs; secondary: PRIMA README].
- **Mostly single-author work in the DFO period.** Every DFO item above is Powell alone (inference from the confirmed author lists).
- **Surveys at turning points:** Acta Numerica 1998, written between COBYLA and UOBYQA, and the 2007 "view", written between NEWUOA and BOBYQA.

---

## 2. Signature-work anatomies

### A. COBYLA: "A direct search optimization method that models the objective and constraint functions by linear interpolation" (1994; DAMTP 1992/NA5; DOI 10.1007/978-94-015-8330-5_4)

| Dimension | Content |
|---|---|
| Origin | Powell's cover note says the report was presented at the Numerical Analysis and Optimization conference in Oaxaca, Mexico, January 1992 [primary]. *Speculation:* the intellectual origin (why linear models on a simplex) is not documented in anything read here. |
| Why then | *Speculation:* by 1992 trust-region theory for derivative-based methods was mature (the OMS obituary credits Powell with the first trust-region convergence result in 1970 [secondary]). Moving it to interpolation models was the natural next step. |
| Key insight | Use n+1 interpolation points (a simplex) to get linear models of the objective *and of every constraint*. Restrict the step with a trust region whose size RHO shrinks from RHOBEG to RHOEND. Treat "each constraint individually … instead of lumping the constraints together into a single penalty function" (code header, verbatim) [primary]. |
| Minimal evidence | Ten test problems: a simple quadratic, unit circle, ellipsoid, weak and intermediate Rosenbrock, two problems from Fletcher's *Practical Methods of Optimization*, Hock–Schittkowski #43 and #100, and Luenberger's hexagon (`cobyla/main.f`). The cover note says: "at the time of writing this note I had applied it only to test problems that have up to 10 variables" [primary]. |
| Abandoned paths | Unknown. The cover note does mention that "some cosmetic restructuring of the software has caused the given output to differ slightly from Table 1 of the report" [primary], so the code changed after the report was written. |
| Reception | Wrapped by SciPy (`fmin_cobyla`), NLopt and others. Downstream issue trackers recorded infinite loops, and cases where the best point evaluated is not returned. PRIMA calls these Fortran 77 implementation bugs "rather than flaws in the algorithms". SciPy 1.16.0 replaced the F77 COBYLA with PRIMA's version [secondary: PRIMA README]. |
| Methods shown | M1 (relax one limitation, as the base of the series), M2 (RHO schedule), M5 (honest scope), M6 (code-as-deliverable). |

### B. UOBYQA → least-Frobenius updating → NEWUOA (2002 / 2004 / 2006)

| Dimension | Content |
|---|---|
| Origin | NEWUOA README (verbatim): "The new software was developed from UOBYQA, which also forms quadratic models from interpolation conditions. That method requires NPT=(N+1)(N+2)/2 conditions, however, because they have to define all the parameters of the model." [primary] |
| Why then | UOBYQA's own paper reported promise for n ≤ 20 and trouble beyond that because each iteration needs O(n⁴) work [primary, snippet]. That limitation was the trigger for the next design. |
| Key insight | Interpolate at only about 2n+1 points. Take up the remaining freedom by minimizing the Frobenius norm of the *change* to the model Hessian, which is a least-change update. Maintain the inverse of the KKT-type interpolation matrix, whose entries give the Lagrange functions, so each iteration costs O((m+n)²) [primary: 2004 abstract; README]. |
| Minimal evidence | Chebyquad (Fletcher 1965) for N = 2, 4, 6, 8 with NPT = 2N+1, shipped as `main.f` together with "the computed output that the author obtained". README: "in some experiments the number of calculations of the objective function seems to be only of magnitude N" [primary]. |
| Abandoned paths | Full quadratic interpolation (UOBYQA) for large n. UOBYQA was kept for small n rather than withdrawn [primary: READMEs]. |
| Reception | Moré & Wild (SIAM J. Optim. 2009) found NEWUOA the fastest solver on about 50% of their problems at τ = 10⁻⁵ [secondary]. It was adopted in R (`minqa`), NLopt and elsewhere [secondary]. |
| Methods shown | M1, M3 (underdetermined least-change models), M4 (cost and rounding engineering), M5. |

### C. BOBYQA: "The BOBYQA algorithm for bound constrained optimization without derivatives" (DAMTP 2009/NA06)

| Dimension | Content |
|---|---|
| Origin | An extension of NEWUOA to simple bounds. The header repeats NEWUOA's least-Frobenius description and adds XL/XU [primary]. |
| Why then | *Speculation:* users asked for bounds. No primary statement of motive was found. (NLopt also has a bound-handling "NEWUOA_BOUND" variant, named in a PRIMA-listed NLopt issue [secondary], but its date relative to BOBYQA was not checked.) |
| Key insight | Every trial point respects the bounds. New routines ALTMOV (choose a replacement point giving "a large denominator in the next call of UPDATE") and RESCUE (restore "the linear independence of the interpolation conditions", setting matrices "in a well-conditioned way") keep the model usable [primary: code comments]. |
| Minimal evidence | "Invdist2": sum of reciprocal pairwise distances of points in the plane, with (N, NPT) = (10,16), (10,21), (20,26), (20,41). The driver comment admits: "Convergence to a local minimum that is not global occurs in both the N=10 cases. The details of the results are highly sensitive to computer rounding errors." [primary] |
| Abandoned paths | Large NPT: "much larger values tend to be inefficient, because the amount of routine work of each iteration is of magnitude NPT**2, and because the achievement of adequate accuracy in some matrix calculations becomes more difficult" [primary README]. |
| Reception | About 1,400 citations per a Scispace listing [secondary]. There is a Python re-implementation (Py-BOBYQA, NAG repository), which PRIMA calls "a true translation … with significant improvements". NAG also has a product page [secondary]. |
| Methods shown | M2, M3, M4, M5, M6. |

### D. LINCOA and the 2015 subproblem paper (code 2013; Math. Prog. Comp. 7(3), 2015, DOI 10.1007/s12532-015-0084-4)

| Dimension | Content |
|---|---|
| Origin | Linear inequality constraints, the next constraint class after bounds [primary README]. |
| Key insight | Same quadratic-model machinery, with an active-set routine (GETACT) and a trust-region step for linear constraints (TRSTEP). The 2015 paper analyses only the subproblem [primary; snippet]. |
| Minimal evidence | "PtsinTet": the least-volume tetrahedron containing given points, with 12 variables and 4·NP linear constraints. The comment says "The smaller final value of the objective function in the case NPT=35 shows that the problem has local minima." [primary] |
| Stated limits | "not suitable for very large numbers of variables because no attention is given to any sparsity. A few calculations with 1000 variables, however, have been run successfully overnight"; there may be evaluations "at points that do not satisfy the linear constraints, especially if an equality constraint is expressed as two inequalities" [primary]. |
| Abandoned paths | The planned paper describing LINCOA never appeared. Powell died on 19 April 2015 [secondary: memoir]. |
| Methods shown | M1, M5, M6. |

### E. Early precursor: the 1964 conjugate-direction method (Computer Journal 7(2):155–162)
One sentence, from the abstract snippet: a simple variation of the one-parameter-at-a-time method that yields conjugate directions on quadratics, "resulting in fast convergence". *Inference:* the same move recurs 30 years later: take a crude practical method, find the smallest modification that gives it the right behaviour on quadratics, and prove it on test functions. Now in SciPy as `fmin_powell` [secondary].

---

## 3. What the deep-reading pass changes in sections 1–2

Each item points to the cards; the full reasoning is in `08-deep-reading-synthesis.md` §3.

- **⚠️ leads now verified.** "Beyond symmetric Broyden for updating quadratic models in minimization without derivatives" is Powell's (Math. Program. 138:475–500, 2013, DOI 10.1007/s10107-011-0510-y; read in full, card S108). "Developments of NEWUOA for minimization without derivatives" is Powell's (IMA J. Numer. Anal. 2008, DOI 10.1093/imanum/drm047; read in full, card S036). The pre-DFO classics are on the Scholar list with checked metadata: DFP with Fletcher (S001, 1963, read in full), "A hybrid method for nonlinear equations" (S011, 1970, metadata), "A method for non-linear constraints in minimization problems" (S004, 1969, metadata), the 1978 SQP papers (S003, S013 metadata; S016 abstract) and "Nonconvex minimization calculations and the conjugate gradient method" (S020, 1984, abstract).
- **UOBYQA's limit** is given as three figures in Powell's texts: "very promising" for n ≤ 20 [S025 p. 1], prohibitive beyond about 50 [S025 p. 30; S047 p. 2; S045 p. 3], about 100 in practice [S029 p. 10]. NEWUOA superseded it [S029 p. 10], and the full-quadratic regime stays a choice of NPT in NEWUOA and BOBYQA [S018 p. 2; S007 p. 34].
- **Anatomy A (COBYLA), Origin and Abandoned paths**: Powell's own later account names IMSL's wrapping of TOLMIN with differences, the popularity of simulated annealing and genetic algorithms, and a four-variable, ten-constraint problem from Westland Helicopters [S029 pp. 2–3; S014 pp. 2, 45]. COBYLA had one radius (Δ = ρ); the two radii came later from research student Evan Jones [S047 p. 5; S014 pp. 26–28, 34–35]. RBF models were tried for the local model and dropped; the memoir places the RBF attempt first and the polynomial-interpolation codes after it [R007 pp. 17, 21], and Powell's own accounts of COBYLA's origin do not mention it [S029 pp. 2–3; S014 p. 2]. The COBYLA paper itself stays abstract-only [S008].
- **Anatomy B (NEWUOA), Why then**: least-Frobenius updating was first tried in January 2002 [S072 pp. 7–8]; eighteen months of rounding trouble followed, ended by the factored Ω [S124 pp. 3, 14, 22]; the release came in December 2003 [S018 p. 3].
- **Anatomy C (BOBYQA), Origin**: NEWUOA's success with 320 variables encouraged the extension to bounds [S036 p. 6]; the speculation about user demand is dropped. Five versions of the alternative step were published before the release decision [S036 pp. 11–14, 19].
- **Anatomy D (LINCOA)**: the 2015 paper is a design record of the trust-region step, with two rejected techniques (Krylov steps, boundary searches) and about two years of work that did not enter the software [S067 pp. 1, 25, 30].
- **Pattern "mostly single-author work in the DFO period"**: verified. Every DFO paper read is sole-authored; across the whole list 48 of 170 research works are co-authored (`08-deep-reading-synthesis.md` §9).
- **Pattern "report first, code by email"**: verified and older than the DFO series. The practice dates from the 1968 Harwell report for NS01A [S019 pp. 9–13, 45] and code reports from 1970 on [R007 pp. 27–30].
