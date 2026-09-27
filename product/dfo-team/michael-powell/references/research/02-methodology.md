# 02 · Stated methodology: what Powell *said* about method

Scope: statements in Powell's own voice. No "how I do research" essay, interview or lecture on research method by Powell turned up in the searches, and that is a real gap. His stated method therefore has to be read out of (a) the cover notes and READMEs he wrote to go with his codes, (b) the comment headers of his subroutines, and (c) the framing of his survey papers. All quotes below were read directly in files mirrored in the PRIMA repository (https://github.com/libprima/prima, `fortran/original/*`), or seen verbatim in search results. Everything else is marked *(paraphrase)*.

Credibility: all items are **primary** (Powell's own words) unless tagged [secondary].

---

## 1. Taste: what a good DFO algorithm is

| # | Statement | Source | Cred. |
|---|-----------|--------|-------|
| T1 | Efficiency is measured in function evaluations, with the per-iteration cost kept low: "The least Frobenius norm updating procedure with NPT=2N+1 is usually much more efficient when N is large, because the work of each iteration is much less than before, and in some experiments the number of calculations of the objective function seems to be only of magnitude N." | NEWUOA README/email, 16 Dec 2004 (`fortran/original/newuoa/README.txt`) | primary |
| T2 | Treat constraints individually: COBYLA "has an advantage over many of its competitors, however, which is that it treats each constraint individually when calculating a change to the variables, instead of lumping the constraints together into a single penalty function." | COBYLA subroutine header (`fortran/original/cobyla/cobyla.f`) | primary |
| T3 | Scope of interest (paraphrase of abstract): among methods for optimization without derivatives, attention is restricted to those suitable for noisy functions and that change the variables in ways that are not random. The essay notes "the vast majority of unconstrained calculations do not employ any derivatives" (fragment confirmed in search). | "A view of algorithms for optimization without derivatives", Mathematics Today 43 (2007); DAMTP 2007/NA03 | primary |
| T4 | Survey across families before choosing (paraphrase): the Acta Numerica review is "a collection of essays" on line searches, discrete grids, simplices, conjugate directions and trust-region methods with linear or quadratic models. | Acta Numerica 7 (1998), abstract snippet | primary |

## 2. Problem and parameter setup (the instructions Powell gave users)

| # | Statement | Source | Cred. |
|---|-----------|--------|-------|
| S1 | Scale first: "After scaling the individual variables if necessary, so that the magnitudes of their expected changes are similar, RHOBEG is the initial steplength for changes to the variables, a reasonable choice being the mesh size of a coarse grid search. Further, RHOEND should be suitable for a search on a very fine grid. Typically, the software calculates a vector of variables that is within distance 10*RHOEND of a local minimum." | BOBYQA README, 5 Jan 2009 | primary |
| S2 | "Typically, RHOBEG should be about one tenth of the greatest expected change to a variable, while RHOEND should indicate the accuracy that is required in the final values of the variables." | BOBYQA and UOBYQA/NEWUOA subroutine headers | primary |
| S3 | Room to search: "every trial vector of variables is forced to satisfy the lower and upper bounds, but there has to be room to make a search in all directions. Therefore an error return occurs if the difference between the bounds on any variable is less than 2*RHOBEG." | BOBYQA README | primary |
| S4 | Model size: "the value NPT=2*N+1 being recommended for a start … It is often worthwhile to try other choices too, but much larger values tend to be inefficient, because the amount of routine work of each iteration is of magnitude NPT**2, and because the achievement of adequate accuracy in some matrix calculations becomes more difficult. Some excellent numerical results have been found in the case NPT=N+6 even with more than 100 variables." | BOBYQA README | primary |
| S5 | Rounding errors are a design concern: "the contribution to a model from changes to the I-th variable is damaged severely by rounding errors if XU(I)-XL(I) is too small." | BOBYQA subroutine header | primary |

## 3. Judging results

| # | Statement | Source | Cred. |
|---|-----------|--------|-------|
| J1 | The user is responsible for checking the result: "The user, however, should assume responsibility for finding out if the calculations are satisfactory, by considering carefully the values of F that occur." (The same sentence appears in the NEWUOA and BOBYQA notes. UOBYQA's says "by giving careful attention to the values of F that occur"; LINCOA's says "if the calculations are adequate".) | NEWUOA/BOBYQA/UOBYQA/LINCOA READMEs 2002–2013 | primary |
| J2 | Accuracy is not guaranteed: RHOBEG and RHOEND should be set to reasonable initial changes and required accuracy, "but this accuracy should be viewed as a subject for experimentation because it is not guaranteed." | COBYLA header | primary |
| J3 | Multiple starts and parameter variation: "It may be helpful to employ several starting points in the space of the variables and to try different values of the parameters NPT and RHOEND." | LINCOA README, 6 Dec 2013 | primary |
| J4 | No guarantees, and the tested range is stated: "There are no restrictions on the use of the software, nor do I offer any guarantees of success. Indeed, at the time of writing this note I had applied it only to test problems that have up to 10 variables." | COBYLA cover note, 7 May 1992 | primary |

## 4. Expression: how results are communicated

| # | Statement | Source | Cred. |
|---|-----------|--------|-------|
| E1 | Every release follows the same structure: "The attachments in sequence are a suitable Makefile, followed by a main program and a CALFUN routine for the Chebyquad problems, in order to provide an example for testing. Then NEWUOA and its five auxiliary routines … are given. Finally, the computed output that the author obtained for the Chebyquad problems is listed." | NEWUOA README (the same structure appears in the UOBYQA, BOBYQA and LINCOA notes) | primary |
| E2 | Scope limits are stated up front: "LINCOA is not suitable for very large numbers of variables because no attention is given to any sparsity." | LINCOA README | primary |
| E3 | Motivation for release: "It is hoped that the software will be helpful to much future research and to many applications. There are no restrictions on or charges for its use." (NEWUOA). Also "I hope that the time and effort I have spent on developing the package will be helpful to much research and to many applications." (BOBYQA, LINCOA) | READMEs | primary |
| E4 | Documentation debt is acknowledged: "I intend to write a paper that explains briefly the main features of the software." | LINCOA README | primary |

## 5. Research organization
No stated method was found (no advice to students, lab guide or interview). **Gap.**

## 6. Others' description of Powell's stance [secondary]
- The Royal Society memoir (Buhmann, Fletcher, Iserles, Toint 2018, DOI 10.1098/rsbm.2017.0023), as summarized in a search snippet *(paraphrase)*: the subject roughly divides into practical algorithm designers and theoreticians, and Powell refused to follow that dichotomy. An exact-phrase search did not return the memoir, so this is **not** quoted.
- The same memoir, verbatim in its abstract (also quoted in the PRIMA README): Powell was "a British numerical analyst who was among the pioneers of computational mathematics".
- A search summary of Iserles's SIAM News obituary said Powell excelled at systematic numerical experiments whose conclusions fed algorithm design *(paraphrase; the attribution to the SIAM text could not be confirmed)*.

## 7. Repetition check (claims made at least 3 times)
- "User should assume responsibility … values of F": 4 READMEs (UOBYQA, NEWUOA, BOBYQA, LINCOA) → **established method**.
- RHOBEG ≈ coarse scale / RHOEND ≈ required accuracy: COBYLA, UOBYQA, NEWUOA, BOBYQA, LINCOA headers or READMEs → **established**.
- "No restrictions on / charges for use": COBYLA, UOBYQA, NEWUOA, BOBYQA, LINCOA → **established**.
- NPT = 2N+1 "for a start": NEWUOA, BOBYQA, LINCOA → **established**.

## Source URLs (files read directly, primary)
- COBYLA cover note (7 May 1992): https://github.com/libprima/prima/blob/main/fortran/original/cobyla/email.txt
- COBYLA subroutine header: https://github.com/libprima/prima/blob/main/fortran/original/cobyla/cobyla.f
- UOBYQA cover note: https://github.com/libprima/prima/blob/main/fortran/original/uobyqa/email.txt
- NEWUOA README / cover note (16 Dec 2004): https://github.com/libprima/prima/blob/main/fortran/original/newuoa/README.txt
- BOBYQA README / cover note (5 Jan 2009): https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/README.txt
- BOBYQA subroutine header: https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/bobyqa.f
- LINCOA README / cover note (6 Dec 2013): https://github.com/libprima/prima/blob/main/fortran/original/lincoa/README.txt
- 2007 essay (abstract only): https://optimization-online.org/2007/06/1680/
- Acta Numerica 1998 (abstract only): https://doi.org/10.1017/S0962492900002841
- RS memoir abstract (secondary): https://doi.org/10.1098/rsbm.2017.0023
