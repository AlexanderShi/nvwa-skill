# Powell's original Fortran distributions: reading notes

Source: https://github.com/libprima/prima/tree/main/fortran/original (files as Powell emailed them to Zaikun Zhang, 15–16 Dec 2013). Read as raw text on 2026-09-27. Powell's notes say "There are no restrictions on or charges for its use"; only short excerpts are kept here.

| Solver | Files read | Cover-note date | Test problem in driver |
|---|---|---|---|
| COBYLA | `cobyla/email.txt`, `cobyla.f`, `cobylb.f`, `main.f` | 7 May 1992 ("Mike Powell") | 10 problems from DAMTP 1992/NA5 (Fletcher, Hock–Schittkowski #43/#100, Luenberger hexagon, Rosenbrock variants) |
| UOBYQA | `uobyqa/email.txt`, `uobyqa.f` | undated in note; report DAMTP 2000/NA14 | Chebyquad N = 2,4,6,8; RHOEND 1e-8 |
| NEWUOA | `newuoa/README.txt`, `email.txt`, `newuoa.f`, `newuob.f`, `biglag.f`, `bigden.f`, `main.f` | 16 Dec 2004 | Chebyquad N = 2,4,6,8, NPT = 2N+1, RHOEND 1e-6 |
| BOBYQA | `bobyqa/README.txt`, `bobyqa.f`, `bobyqb.f`, `altmov.f`, `rescue.f`, `main.f` | 5 Jan 2009 | Invdist2, (N,NPT) = (10,16),(10,21),(20,26),(20,41) |
| LINCOA | `lincoa/README.txt`, `email.txt`, `lincoa.f`, `main.f` | 6 Dec 2013 | PtsinTet, 12 variables, NPT = 15…40 |

## Key verbatim excerpts
- COBYLA note: "There are no restrictions on the use of the software, nor do I offer any guarantees of success. Indeed, at the time of writing this note I had applied it only to test problems that have up to 10 variables."
- COBYLA note: "some cosmetic restructuring of the software has caused the given output to differ slightly from Table 1 of the report."
- COBYLA header: "this accuracy should be viewed as a subject for experimentation because it is not guaranteed."
- COBYLA header: "it treats each constraint individually when calculating a change to the variables, instead of lumping the constraints together into a single penalty function."
- NEWUOA/BOBYQA note: "The user, however, should assume responsibility for finding out if the calculations are satisfactory, by considering carefully the values of F that occur."
- NEWUOA note: "in some experiments the number of calculations of the objective function seems to be only of magnitude N."
- BOBYQA note: "RHOBEG is the initial steplength for changes to the variables, a reasonable choice being the mesh size of a coarse grid search. Further, RHOEND should be suitable for a search on a very fine grid. Typically, the software calculates a vector of variables that is within distance 10*RHOEND of a local minimum."
- BOBYQA note: "Some excellent numerical results have been found in the case NPT=N+6 even with more than 100 variables."
- BOBYQA driver: "Convergence to a local minimum that is not global occurs in both the N=10 cases. The details of the results are highly sensitive to computer rounding errors."
- LINCOA note: "It may be helpful to employ several starting points in the space of the variables and to try different values of the parameters NPT and RHOEND. I intend to write a paper that explains briefly the main features of the software."
- LINCOA note: "LINCOA is not suitable for very large numbers of variables because no attention is given to any sparsity. A few calculations with 1000 variables, however, have been run successfully overnight".

## Control logic observed in `newuob.f` (NEWUOA)
- A short step (< RHO/2) leads to DELTA ← DELTA/10 (floored at RHO). If recent model errors (DIFFA/B/C, the last three |F − Q| discrepancies) are all below 0.125·CRVMIN·RHO² after enough new evaluations, RHO is reduced directly. Otherwise there is a check for far interpolation points (> 2·DELTA); if one exists, a "model step" is taken to that point (via BIGLAG/BIGDEN) before RHO may drop.
- Ratio test thresholds 0.1 / 0.7. DELTA snaps to RHO when ≤ 1.5·RHO.
- RHO reduction: to RHOEND if RHO/RHOEND ≤ 16; to sqrt(RHO·RHOEND) if ≤ 250; else RHO/10.
- The base point XBASE is shifted when XOPT is far from it, to control rounding errors.
- Exit message: "Return from NEWUOA because a trust region step has failed to reduce Q."
