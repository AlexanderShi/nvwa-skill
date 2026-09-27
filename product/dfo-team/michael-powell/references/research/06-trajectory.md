# 06 · Research trajectory

Credibility: [primary] = dated Powell documents · [secondary] = memoirs, obituaries, successor projects. Unverified dates are marked ⚠️.

---

## Timeline

| Year | Event | Source | Cred. |
|---|---|---|---|
| 1936 | Born 29 July, Kensington | RS memoir title; OMS obituary snippet | secondary |
| ⚠️ c.1959–1976 | AERE Harwell. SIAM News (Iserles) says "seventeen years". The exact start and end years were not verified; 1976 is inferred as the move date. | https://www.siam.org/publications/siam-news/articles/obituaries-michael-jd-powell/ | secondary |
| 1960s | Derivative-based breakthroughs: the DFP formula (Buhmann 2019 mentions "the famous DFP formula"). Paper titles not verified here. | https://www.sciencedirect.com/science/article/pii/S0021904517301053 | secondary |
| 1964 | Conjugate-direction method without derivatives, Computer Journal 7(2):155–162 | https://academic.oup.com/comjnl/article-abstract/7/2/155/335330 | primary |
| 1970 | First convergence result for trust-region methods (unconstrained) | OMS obituary snippet, DOI 10.1080/10556788.2015.1051808 | secondary |
| ⚠️ ~1976 | Moves to Cambridge as John Humphrey Plummer Professor of Applied Numerical Analysis (the title is confirmed by the memoir; the year is not) | RS memoir | secondary |
| 1982 | First Dantzig Prize (one of two inaugural recipients per PRIMA README) | search snippet; PRIMA README | secondary |
| 1983 | Fellow of the Royal Society | search snippet | secondary |
| 1992 | COBYLA: report DAMTP 1992/NA5, Oaxaca conference (Jan), code mailed 7 May 1992 | `cobyla/email.txt` | primary |
| 1994 | COBYLA chapter published (Kluwer) | DOI 10.1007/978-94-015-8330-5_4 | primary |
| 1997 | 60th-birthday tributes volume (CUP), with Conn, Scheinberg and Toint among contributors | CUP page | secondary |
| 1998 | Acta Numerica survey of direct search algorithms | DOI 10.1017/S0962492900002841 | primary |
| 2000–2002 | UOBYQA (DAMTP 2000/NA14; Math. Program. 2002) | DOI 10.1007/s101070100290 | primary |
| 2001 | Elected to the US National Academy of Sciences (snippet wording: "member") | search snippet | secondary |
| 2004 | Least-Frobenius-norm updating (Math. Program. B 100); NEWUOA code 16 Dec 2004 | DOI 10.1007/s10107-003-0490-7; README | primary |
| 2006 | NEWUOA chapter (Springer) | DOI 10.1007/0-387-30065-1_16 | primary |
| 2007 | "A view of algorithms for optimization without derivatives" (Mathematics Today 43) | DAMTP 2007/NA03 | primary |
| 2007 | Fellow of the Australian Academy of Science | search snippet | secondary |
| 2009 | BOBYQA report (DAMTP 2009/NA06); code note 5 Jan 2009 | README | primary |
| 2009 | Moré & Wild benchmark shows NEWUOA the fastest on ~50% of problems | SIAM J. Optim. 20(1) | secondary |
| 2013 | LINCOA code (note 6 Dec 2013); all codes sent to Zaikun Zhang 15–16 Dec 2013 | READMEs | primary |
| 2015 | "On fast trust region methods for quadratic models with linear constraints", Math. Prog. Comp. 7(3) | DOI 10.1007/s12532-015-0084-4 | primary |
| 2015 | **Died 19 April 2015, Cambridge** | RS memoir; OMS obituary | secondary |
| 2015 | Obituaries: OMS (Cartis, Griewank, Toint, Yuan); SIAM News (Iserles) | see 04 | secondary |
| 2018 | Royal Society memoir (Buhmann, Fletcher, Iserles, Toint) | DOI 10.1098/rsbm.2017.0023 | secondary |
| 2019 | Buhmann, J. Approx. Theory 238 | ScienceDirect | secondary |

## After 2015: what happened to the codes (verified)
- **Custodianship.** Powell had asked Zaikun Zhang and Nick Gould to maintain his solvers [secondary: PRIMA README].
- **PDFO** (Ragonneau & Zhang): cross-platform MATLAB/Python interfaces wrapping Powell's Fortran. "PDFO: a cross-platform package for Powell's derivative-free optimization solvers", Math. Program. Comput. 16:535–559 (2024), DOI 10.1007/s12532-024-00257-9. PDFO is Chapter 3 of Ragonneau's PolyU thesis [secondary: PRIMA README; https://github.com/pdfo/pdfo].
- **PRIMA** ("Reference Implementation for Powell's methods with Modernization and Amelioration"): started by Zhang in July 2020 on the basis of PDFO. The modern Fortran version was finished by December 2022, with C, Python, MATLAB and Julia interfaces. It is mathematically equivalent to Powell's code except for intentional bug fixes and improvements, and faithfulness is checked by differential testing. Cite as Zenodo DOI 10.5281/zenodo.8052654 [secondary: https://github.com/libprima/prima].
- **SciPy 1.16.0** replaced the F77 COBYLA under `scipy.optimize.minimize` with PRIMA's Python translation [secondary: PRIMA README].
- **Other translations:** NLopt (C, close to f2c style), Py-BOBYQA (NAG; a "true translation … with significant improvements"), R `minqa` [secondary].

## Pivots and their triggers (analysis)
| Pivot | Trigger (evidence) | Type |
|---|---|---|
| Derivative-based (1960s–80s) → derivative-free model-based (1990s–2015) | *Speculation:* the 2007 essay's premise that "the vast majority of unconstrained calculations do not employ any derivatives" [primary fragment]. Powell went where practitioners actually were. | Demand-driven |
| Linear (COBYLA) → quadratic (UOBYQA) | *Speculation:* linear models converge slowly near a solution. No primary statement was found. | Accuracy-driven |
| UOBYQA → NEWUOA | UOBYQA's O(n⁴) work, n ≤ 20 [primary] | Cost-driven |
| NEWUOA → BOBYQA → LINCOA | Constraint class widened one step at a time [primary: READMEs] | Scope-driven |

## Latest (2023–2026)
- PRIMA is being adopted (SciPy 1.16.0; NVIDIA CUDA-QX, AWS CQC listed as users) [secondary].
- ⚠️ arXiv 2609.09441 (2026), "Powell-Style Model-Based Derivative-Free Optimization with Complexity Guarantees": title only, content not read. It suggests Powell's design style remains a live template.
