# 05 · Peer critique, limits and later improvements by others

Credibility: [primary] = Powell's own admissions · [secondary] = others' benchmarks, bug reports and re-implementations. Items marked ⚠️ are leads whose authorship or content could not be confirmed. They are listed for follow-up and never used as fact.

---

## 1. Limits Powell stated himself [primary]
| Limit | Quote / fact | Source |
|---|---|---|
| Per-iteration cost of full quadratic models | UOBYQA: promising for n ≤ 20; larger n is problematic because each iteration takes fourth-order work (abstract snippet) | Math. Program. 92 (2002), DOI 10.1007/s101070100290 |
| Tested range | COBYLA "applied … only to test problems that have up to 10 variables" | COBYLA note 1992 |
| No accuracy guarantee | "this accuracy should be viewed as a subject for experimentation because it is not guaranteed" | COBYLA header |
| No sparsity | LINCOA "not suitable for very large numbers of variables because no attention is given to any sparsity" | LINCOA README 2013 |
| Infeasible evaluations | LINCOA may evaluate "at points that do not satisfy the linear constraints, especially if an equality constraint is expressed as two inequalities" | LINCOA README |
| Local minima and rounding sensitivity | Invdist2: "Convergence to a local minimum that is not global … highly sensitive to computer rounding errors"; PtsinTet: "the problem has local minima" | BOBYQA and LINCOA drivers |
| Large NPT | "much larger values tend to be inefficient … adequate accuracy in some matrix calculations becomes more difficult" | BOBYQA README |

## 2. External benchmark evidence [secondary]
- **Moré & Wild (2009)**, "Benchmarking derivative-free optimization algorithms", SIAM J. Optim. 20(1):172–191. They introduced *data profiles* (share of problems solved within k evaluations). At τ = 10⁻⁵, NEWUOA was fastest on about 50% of problems, NMSMAX on about 30% and APPSPACK on about 20%. https://www.mcs.anl.gov/uploads/cels/papers/P1471.pdf. This supports Powell's evaluation-economy priority on smooth test sets, and changed how the field measures DFO solvers: by budget in evaluations, not by final accuracy alone.

## 3. Implementation critique after Powell's death [secondary: PRIMA README, https://github.com/libprima/prima]
- **Bugs in the Fortran 77 code** (reported to SciPy, NLopt, nloptr, OpenTURNS and others): infinite loops (e.g. "optimize: COBYLA hangs / infinite loop", scipy#8998; "BOBYQA gets stuck in infinite loop"); segmentation faults from uninitialized variables used as indices (NLopt#36, #133, #134); COBYLA "may **not return the best point** that is evaluated", sometimes with large constraint violation from a feasible start. Zhang's classification: "all of them are problems in the Fortran 77 code rather than flaws in the algorithms."
- **Precision sensitivity**: "The Fortran 77 version of UOBYQA encounters infinite cyclings very often if PRIMA_REAL_PRECISION is 32" (PRIMA issue #98).
- **Maintainability**: the F77 code "is nontrivial to understand or maintain, let alone extend", and this "has hindered researchers from exploring the wealth left by Professor Powell."
- **Performance trade-off**: PRIMA "generally produces better solutions with fewer function evaluations", while Powell's F77 is "likely to be faster" when evaluations take milliseconds, because it uses less memory and fewer flops.
- **Robustness to failed evaluations**: PRIMA tests check that solvers "behave properly even if they are invoked with improper inputs or encounter failures of function evaluations". *Inference:* the original codes did not treat this systematically; it is a modern requirement they were not written for.
- **Reproducibility norm set by the successors**: "it is important to point out that you are using PRIMA rather than the original solvers if you want your results to be reproducible."

## 4. Theory-side critique and later developments (leads, ⚠️ unless stated)
- ⚠️ "Incorporating minimum Frobenius norm models in direct search" (Comput. Optim. Appl., DOI 10.1007/s10589-009-9283-0). The title and URL were seen, the authors were not confirmed. It indicates that Powell's minimum-Frobenius-norm models were imported into direct-search frameworks, which bridges to the Vicente and Audet lenses.
- ⚠️ "Sobolev seminorm of quadratic functions with applications to derivative-free optimization" (arXiv 1111.4576) and ⚠️ "Least H² norm updating quadratic interpolation model function for derivative-free trust-region algorithms" (arXiv 2302.12017): titles seen only. They suggest others kept re-examining the *choice of norm* in Powell's least-change update.
- ⚠️ "Powell-Style Model-Based Derivative-Free Optimization with Complexity Guarantees" (arXiv 2609.09441, 2026): title seen only. *Inference from the title:* worst-case complexity guarantees for Powell-style methods were still being added a decade after his death, so Powell's own solvers were validated mainly by experiment rather than by complexity theory.
- ⚠️ Moré–Wild-style comparisons that include direct-search and noisy-function solvers (e.g. Rios & Sahinidis 2013) were not searched because the budget ran out.
- ⚠️ The Conn–Scheinberg–Vicente textbook treatment of interpolation-set geometry (Λ-poisedness) could not be verified in this session. It is recorded as the theory-first counterpart to Powell's engineered geometry steps, but is not cited as fact.

## 5. Summary of blind spots (synthesis)
1. **Nonsmooth, discontinuous, or stochastic objectives.** The solvers assume a locally smooth F that quadratic interpolation can capture. The 2007 essay scopes itself to "noisy" functions, but the codes contain no explicit noise model. *(Inference from the code and READMEs.)*
2. **Large-scale / sparse structure.** Explicitly not handled (LINCOA README).
3. **Formal guarantees shipped with the code.** No complexity guarantees are stated in any README. Acceptance rests on test problems plus user checking ("user … should assume responsibility").
4. **Engineering for longevity.** The single-author F77 style, GOTO-heavy with no test suite in the modern sense, produced latent bugs that surfaced only through wide adoption.
5. **Global optimization.** The solvers seek local minima by design ("close to a local minimum"). The multi-start advice is only a heuristic.

## Source URLs
- PRIMA README (bug list, performance comparison, reproducibility note): https://github.com/libprima/prima (secondary)
- Issues linked from the PRIMA README, not opened here (secondary): https://github.com/scipy/scipy/issues/8998 · https://github.com/stevengj/nlopt/issues/36 · https://github.com/stevengj/nlopt/issues/133 · https://github.com/stevengj/nlopt/issues/57 · https://github.com/libprima/prima/issues/98
- Moré & Wild 2009: https://www.mcs.anl.gov/uploads/cels/papers/P1471.pdf (secondary)
- UOBYQA abstract (n ≤ 20 limit): https://doi.org/10.1007/s101070100290 (primary)
- LINCOA and BOBYQA notes: https://github.com/libprima/prima/blob/main/fortran/original/lincoa/README.txt · https://github.com/libprima/prima/blob/main/fortran/original/bobyqa/README.txt (primary)
