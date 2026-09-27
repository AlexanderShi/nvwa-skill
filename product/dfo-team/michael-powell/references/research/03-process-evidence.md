# 03 · Process evidence: what Powell actually *did*

Primary evidence: Powell's original Fortran 77 distributions (code, test drivers, cover emails), which Powell sent to Zaikun Zhang on 15–16 Dec 2013 and which are now mirrored at https://github.com/libprima/prima/tree/main/fortran/original. The files were read directly as raw text. Notes and excerpts are in `../sources/software/powell-fortran-notes.md`. Secondary evidence: the PRIMA README (Zhang), and benchmark results (Moré & Wild 2009).

---

## P1 · A solver series in which each step removes one limitation (practice for Method 1)
| Solver | Model | Points | Constraint class | Date on Powell's cover note / header | Evidence |
|---|---|---|---|---|---|
| COBYLA | linear | n+1 (simplex) | nonlinear inequalities | 7 May 1992 | `cobyla/email.txt` [primary] |
| UOBYQA | full quadratic | (n+1)(n+2)/2 | none | report DAMTP 2000/NA14 | `uobyqa/uobyqa.f` header [primary] |
| NEWUOA | quadratic, least-Frobenius update | NPT in [n+2,(n+1)(n+2)/2], 2n+1 recommended | none | 16 Dec 2004 | `newuoa/README.txt` [primary] |
| BOBYQA | same as NEWUOA | same; "Choices that exceed 2*N+1 are not recommended" | bounds | 5 Jan 2009 | `bobyqa/bobyqa.f`, README [primary] |
| LINCOA | same | 2n+1 recommended | linear inequalities | 6 Dec 2013 | `lincoa/README.txt` [primary] |

The subroutine interfaces stay deliberately uniform: (N, NPT, X, [bounds/constraints], RHOBEG, RHOEND, IPRINT, MAXFUN, W) plus a user CALFUN/CALCFC. Anyone who can run one solver can run the next [primary: headers].

## P2 · Two radii in the code: RHO (resolution) vs DELTA (step bound) (practice for Method 2)
From `newuoa/newuob.f` [primary, read directly]:
- If the trust-region step is short (`DNORM < HALF*RHO`), Powell does **not** immediately shrink RHO. He first reduces DELTA (`DELTA=TENTH*DELTA`, floored at RHO). RHO is reduced straight away only if the recent model errors (DIFFA, DIFFB, DIFFC) are all below `0.125*CRVMIN*RHO*RHO`, i.e. the model has been predicting F well at this resolution. Otherwise he checks whether an interpolation point lies further than `2*DELTA` from the best point. If one does, it is replaced by a "model step" before RHO is allowed to drop. The comments read: "Alternatively, find out if the interpolation points are close enough to the best point so far." and "If KNEW is positive … branch back for the next iteration, which will generate a 'model step'."
- DELTA update rule after a trust-region step: ratio ≤ 0.1 → `DELTA=HALF*DNORM`; ratio ≤ 0.7 → `max(HALF*DELTA, DNORM)`; otherwise `max(HALF*DELTA, 2*DNORM)`. If DELTA ≤ 1.5·RHO, set DELTA = RHO.
- RHO schedule, from the comment "The calculations with the current value of RHO are complete. Pick the next values of RHO and DELTA.": if RHO/RHOEND ≤ 16 → RHO = RHOEND; ≤ 250 → RHO = sqrt(RHO/RHOEND)·RHOEND; else RHO = RHO/10. RHO never increases.
- Explicit failure exit: "Return from NEWUOA because a trust region step has failed to reduce Q."
- COBYLA uses the same logic on a simplex (`cobyla/cobylb.f`): "set IFLAG=0 if the current simplex is not acceptable"; "Otherwise reduce RHO if it is not at its least value and reset PARMU."

## P3 · Geometry maintenance as separate, named routines (practice for Methods 2–3)
- NEWUOA: BIGLAG, where "The step D is calculated in a way that attempts to maximize the modulus of LFUNC(XOPT+D), subject to the bound ||D|| .LE. DELTA, where LFUNC is the KNEW-th Lagrange function"; and BIGDEN, used "If KNEW is positive and if the cancellation in DENOM is unacceptable" [primary].
- BOBYQA: ALTMOV, which picks a new point that "should provide a large denominator in the next call of UPDATE", with an alternative "constrained version of the Cauchy step"; and RESCUE, which gives new point positions "in case changes are needed to restore the linear independence of the interpolation conditions", with matrices "set in a well-conditioned way" [primary].
- *Inference:* the geometry safeguards are engineered as local, cheap, bounded-cost repairs triggered by numerical symptoms (a small denominator, a far point, a short step). They are not global re-poising procedures.

## P4 · Cost and rounding-error engineering (practice for Method 4)
- Moving the origin to avoid cancellation: "Shift XBASE if XOPT may be too far from XBASE" (`newuob.f`) [primary].
- Working storage sized by formula and partitioned by hand, e.g. UOBYQA needs "( N**4 + 8*N**3 + 23*N**2 + 42*N + max [ 2*N**2 + 4, 18*N ] ) / 4" and BOBYQA "(NPT+5)*(NPT+N)+3*N*(N+5)/2" [primary]. The O(n⁴) storage of UOBYQA is visible in the interface itself, which is the limitation NEWUOA removed.
- An inverse-matrix factorization (BMAT, ZMAT, IDZ) is updated in place by UPDATE instead of re-solving the interpolation system [primary: BIGLAG argument comments].
- Downstream observation [secondary, PRIMA README]: Powell's F77 codes are "more efficient in terms of memory usage and flops thanks to the careful and ingenious (but unmaintained and unmaintainable) implementation by Powell."

## P5 · Test-driver habits (practice for Method 5)
| Solver | Driver problem(s) | Sweep | Honest failure note in the driver |
|---|---|---|---|
| COBYLA | 10 problems: simple quadratic, unit circle, ellipsoid, 2× Rosenbrock variants, 2 from Fletcher's *Practical Methods of Optimization*, Hock–Schittkowski #43 (Rosen–Suzuki) and #100, Luenberger's hexagon | n ≤ 10 | Cover note: tested "only to test problems that have up to 10 variables" |
| UOBYQA | Chebyquad (Fletcher 1965) | N = 2,4,6,8; RHOEND = 1e-8 | — |
| NEWUOA | Chebyquad | N = 2,4,6,8, NPT = 2N+1; RHOEND = 1e-6; RHOBEG = 0.2·X(1) | — |
| BOBYQA | Invdist2 (reciprocal pairwise distances, bounds [-1,1]) | (N,NPT) = (10,16), (10,21), (20,26), (20,41), i.e. NPT = N+6 and 2N+1; RHOBEG = 0.1, RHOEND = 1e-6 | "Convergence to a local minimum that is not global occurs in both the N=10 cases. The details of the results are highly sensitive to computer rounding errors." |
| LINCOA | PtsinTet (least-volume enclosing tetrahedron, 12 variables, 4·NP linear constraints) | six NPT values, NPT = 5·JCASE+10 = 15…40 (the "JCASE=1,6 loop"); RHOBEG = 1, RHOEND = 1e-6 | "The smaller final value of the objective function in the case NPT=35 shows that the problem has local minima." |

The pattern: small, fully specified problems with known structure; loops over n and NPT; IPRINT levels that expose each RHO reduction; and the author's own output listing shipped so users can check that their build reproduces it. Failures such as local minima and rounding sensitivity are documented instead of cherry-picked away [primary].

## P6 · Release practice (practice for Method 6)
- Every distribution: Makefile → main program → CALFUN example → solver + auxiliary routines → "the computed output that the author obtained" [primary].
- Licence: "There are no restrictions on or charges for its use" (all five) [primary].
- Honest reproducibility note: "some cosmetic restructuring of the software has caused the given output to differ slightly from Table 1 of the report" (COBYLA 1992) [primary].
- Modularity invitation: for COBYLA's LP-with-trust-region subproblem, "SUBROUTINE TRSTLP is provided too, but you may have some software that you prefer to use instead" [primary].
- Handover: "Before he passed, Professor Powell had asked me and Professor Nick Gould to maintain his solvers" (Zhang, PRIMA README) [secondary].

## P7 · External validation of the practice [secondary]
- Moré & Wild, "Benchmarking derivative-free optimization algorithms", SIAM J. Optim. 20(1):172–191 (2009): with data profiles at τ = 10⁻⁵, NEWUOA, NMSMAX and APPSPACK were fastest on roughly 50%, 30% and 20% of problems (search snippet). https://www.mcs.anl.gov/uploads/cels/papers/P1471.pdf
- PRIMA's own performance profiles (CUTEst, up to 200 variables) show that the modernized versions use fewer evaluations than Powell's F77. PRIMA attributes this to intentional "bug fixes and improvements", with the algorithms "essentially the same" [secondary].

## P8 · Era and resource context
- The codes are Fortran 77 (COBYLA originally "a single-precision Fortran implementation", 1992), built with `f77`/`ifort -g` Makefiles and tested on one workstation ("A few calculations with 1000 variables, however, have been run successfully overnight", LINCOA 2013) [primary].
- Single author, no team, no CI, no public repository: distribution was by email. PRIMA later added automated randomized tests on GitHub Actions, CUTEst via MatCUTEst, and fuzz and stress tests [secondary]. Today's equivalent of Powell's "author's output listing" is differential testing plus CI.

## Source URLs (files read directly)
- NEWUOA main loop (RHO/DELTA logic, model steps): https://github.com/libprima/prima/blob/main/fortran/original/newuoa/newuob.f (primary)
- NEWUOA geometry routines: https://github.com/libprima/prima/blob/main/fortran/original/newuoa/biglag.f, https://github.com/libprima/prima/blob/main/fortran/original/newuoa/bigden.f (primary)
- NEWUOA driver (Chebyquad): https://github.com/libprima/prima/blob/main/fortran/original/newuoa/main.f (primary)
- BOBYQA main loop / ALTMOV / RESCUE: https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/bobyqb.f, https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/altmov.f, https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/rescue.f (primary)
- BOBYQA driver (Invdist2): https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/main.f (primary)
- COBYLA main loop and driver: https://github.com/libprima/prima/blob/main/fortran/original/cobyla/cobylb.f, https://github.com/libprima/prima/blob/main/fortran/original/cobyla/main.f (primary)
- LINCOA driver (PtsinTet): https://github.com/libprima/prima/blob/main/fortran/original/lincoa/main.f (primary)
- UOBYQA header: https://github.com/libprima/prima/blob/main/fortran/original/uobyqa/uobyqa.f (primary)
- PRIMA README (bug list, performance, handover): https://github.com/libprima/prima (secondary)
- Moré & Wild 2009: https://www.mcs.anl.gov/uploads/cels/papers/P1471.pdf (secondary)
