# 06 · Trajectory

Research date: 2026-09-27. Biographical facts come from the SIAM News obituary (M. L. Overton, SIAM News 52(5), June 2019 — https://www.siam.org/publications/siam-news/articles/obituary-andrew-r-conn, secondary), the University of Waterloo C&O obituary (https://uwaterloo.ca/combinatorics-and-optimization/news/andrew-conn-1946-2019, secondary), and INFORMS "Remembering Andrew Conn" (https://connect.informs.org/communities/community-home/digestviewer/viewthread?GroupId=469&MessageKey=6436a936-2b44-49e5-9905-c3a6d143b611&CommunityKey=1d5653fa-85c8-46b3-8176-869b140e5e3c&tab=digestviewer, secondary).

## Timeline

| Year(s) | Event | Source |
|---|---|---|
| 1946 | Born in London, 6 August | SIAM obituary |
| 1967 | B.Sc. (honours) in mathematics, Imperial College London | SIAM obituary |
| 1968 | M.Sc. in computer science, University of Manitoba | SIAM obituary |
| 1971 | Ph.D., Dept. of Applied Analysis and Computer Science, University of Waterloo. Thesis title reported by one snippet as "A gradient type method of locating constrained minima" (⚠️ unconfirmed; advisor not found) | SIAM & Waterloo obituaries |
| 1971–72 | Postdoctoral fellowship, Hebrew University of Jerusalem | Waterloo obituary |
| 1972–1990 | Faculty, Dept. of Combinatorics & Optimization and Dept. of Computer Science, Waterloo. 10 PhD students | SIAM & Waterloo obituaries |
| 1973 | Nondifferentiable penalty function paper, SIAM J. Numer. Anal. | DOI 10.1137/0710063 |
| 1979–1988 | Students Coleman (1979, penalty), Calamai (1983, location), Li (1988, minimax) | Wikipedia entries; SIAM obituary |
| 1988–1996 | CGT collaboration: bounds TR theory + testing (1988), augmented Lagrangian (1991), SR1 (1991), LANCELOT (1992), CUTE (1995), LANCELOT experiments (1996) | records in 01-publications.md |
| 1990 | **Pivot 1:** moves to IBM T. J. Watson Research Center, Yorktown Heights, with the encouragement of Ellis L. Johnson | SIAM obituary; Wikipedia "Ellis L. Johnson" |
| 1994 | Beale–Orchard-Hays Prize (with Gould & Toint) for LANCELOT | SIAM obituary |
| 1996–1998 | **Pivot 2:** derivative-free optimization (Conn–Toint 1996; CST 1997 ×2; CST 1998 AIAA) | records |
| 1998–2005 | Circuit tuning: JiffyTune (1998), EinsTuner (DAC 1999; FGCS 2005). IBM Outstanding Technical Achievement Award | records; SIAM obituary |
| 2000 | *Trust-Region Methods* (first book in the MPS-SIAM Series on Optimization) | DOI 10.1137/1.9780898719857; SIAM obituary |
| ~2001 | DFO code released on COIN-OR (date as cited by secondary sources) | https://projects.coin-or.org/Dfo |
| 2006 | Joins technical board of NTNU Center for Integrated Operations (Statoil collaboration). **Pivot 3:** energy applications | IBM Research group page (secondary) |
| 2008–2010 | CSV geometry papers (2008 ×2), general convergence (2009), book *Introduction to DFO* (2009), least-squares DFO (2010) | records |
| 2012–2013 | Bilevel/robust DFO (Conn & Vicente 2012). **Pivot 4:** hybridizing with MADS (Conn & Le Digabel 2013) | records |
| 2014–2016 | Shale-gas scheduling (2014), air traffic (2015), satellite-image matrix completion (CVPR 2016) | dblp |
| 2015 | Lagrange Prize in Continuous Optimization (with Scheinberg & Vicente), awarded at ISMP 2015, Pittsburgh | SIAM prize history; Univ. of Coimbra news — https://www.uc.pt/en/fctuc/dmat/noticias/LagrangePrize |
| 2018 | Progressive-barrier DF trust-region (COAP); QCQP subproblems in MADS (EJOR) — last confirmed papers | records |
| 2019 | Dies 14 March, Westchester County, NY, still at IBM and "very active in the field until shortly before his death" | SIAM obituary |

## Pivots and triggers

| Pivot | Trigger (evidence level) |
|---|---|
| Penalty/nonsmooth → trust regions + large-scale software (mid-1980s) | **Inference**: the CGT collaboration, and the need for robust large-scale codes. No first-hand account. |
| Academia → IBM (1990) | Encouragement by Ellis Johnson (secondary). The access to "extremely knowledgeable people" and "an area rich in problems" (paraphrase, MAM 2015) is Conn's stated reason for enjoying the IBM setting. |
| Derivative-based → derivative-free (mid-1990s) | **Inference**: simulation-based industrial objectives. CST 1997 says the methods are in high demand by practitioners (paraphrase). |
| Pure model-based → hybrid with direct search (2011–2018) | **Inference**: constrained, nonsmooth engineering blackboxes, and the Montréal collaboration. The 2018 results are "competitive" with NOMAD rather than dominant. |

## Entry/exit timing (taste signal)

- Entered DFO **early** (1996–97), before the major benchmarking studies (Moré–Wild 2009; Rios–Sahinidis 2013) and before complexity analysis became the dominant theoretical currency (inference).
- Never "exited" nonlinear programming. Each new area added to the toolkit rather than replacing it. The ℓ1 penalty and augmented Lagrangian reappear in 2018.

## Latest

- Conn died on 14 March 2019. The last confirmed publications are the two 2018 papers with the Montréal group. No posthumous papers were confirmed, and there has been **no activity in the last 12 months** (research date 2026-09-27).
- This skill is therefore a **historical lens**. It captures a craft that ends in 2018 and does not reflect DFO developments since then (e.g., probabilistic models, complexity-driven design, large-scale ML-driven DFO).
