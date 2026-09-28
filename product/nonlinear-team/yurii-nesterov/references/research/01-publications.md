# 01 · Publications: landscape and signature-work anatomy (Yurii Nesterov)

- **Researcher**: Yurii Evgenievich Nesterov (Юрий Евгеньевич Нестеров), b. 1956. CORE / INMA, UCLouvain (Belgium) since 1993. Earlier at the Central Economic-Mathematical Institute (CEMI / ЦЭМИ), USSR Academy of Sciences, Moscow.
- **Dimension**: research agent 01 of 06. Signature works and the publication landscape (framework §二 Agent 1, §五 anatomy).
- **Research date**: 2026-09-28.
- **Sources consulted**: 19. 14 gave usable content. 4 were blocked: Google Scholar (CAPTCHA), Springer, SIAM ePubs (Cloudflare) and the old UCLouvain CORE-DP PDF host. 1 web search returned only a low-value blog snippet. WebSearch calls used: 1.
- **Full texts read**:
  - the 1983 Doklady paper (Russian original, Math-Net.ru);
  - Nesterov's ICM 2010 invited paper;
  - the IMU 2026 Gauss Prize citation and write-up;
  - the NCCR Automation interview (2023);
  - the Cartis–Gould–Toint ARC Part I preprint (introduction and references only).
- **Abstract level only**: every other paper. Abstracts came from IDEAS/RePEc, arXiv or Semantic Scholar, and bibliographic records from Crossref, DBLP and zbMATH.
- **Local corpus**: `references/sources/{papers,talks,essays,software}` hold only `.gitkeep`. There is no user-supplied material, and nothing under `private/` was opened.

**Tags.**
- **[stated]**: what Nesterov himself wrote or said.
- **[practice]**: what the record shows he did (papers, dates, co-authors, venues).
- **[observed]**: what others wrote about him or his work.
- **[inferred]**: my inference. It has no direct source.

Each item is also marked **primary** (the work itself, his own words, or a bibliographic record of the work) or **secondary** (someone else's account). Russian quotes are verbatim from the 1983 paper. The English after them is **my translation, not a quote**.

---

## 1. Bibliometric overview (how big and where)

| Source | What it shows | Notes |
|---|---|---|
| DBLP pid 00/343 (SPARQL, via `scripts/dblp_works.py`) | 122 records, 1991–2026: 106 articles, 11 inproceedings, 2 books, 3 informal. 115 have DOIs. | Nothing before 1991: the Soviet period is missing. **primary record** |
| zbMATH Open, author `nesterov.yurii` | 177 documents, 1978–2026. MSC profile: 90 (OR/mathematical programming) 47%, 65 (numerical analysis) 17%, 49 (calculus of variations/optimal control) 10%. Lists the 2026 Carl Friedrich Gauss Prize. | The only source here that covers 1978–1990. **primary record** |
| OpenAlex A5067792459 (`scripts/fetch_publications.py`) | 257 works pulled, 19,442 citations, h = 39. Current institution: Corvinus University of Budapest. | The ID is split: the 2005 smoothing paper, the 2012 coordinate-descent paper and others are missing. Treat as a lower bound. File: `../sources/publications/publications.md`. **primary record** |
| Semantic Scholar author 143676697 | 216 papers, ≈40,000 citations summed, h = 57 | Also split across several IDs. **secondary aggregator** |
| Google Scholar DJ8Ep8YAAAAJ | not accessible (CAPTCHA redirect) | The IMU citation says "more than 50,000 times on Google Scholar" [observed, secondary]. |

**Most-cited works.** Counts are from Semantic Scholar (S2), with OpenAlex (OA) and Crossref (CR) where available; the three disagree, so they are for ranking only.

| # | Work | Identifier | S2 / OA / CR | Mode |
|---|---|---|---|---|
| 1 | *Introductory Lectures on Convex Optimization: A Basic Course* (Kluwer, Applied Optimization 87, 2004) | DOI 10.1007/978-1-4419-8853-9 | 6614 / 2735 / 2399 | solo book |
| 2 | "A method of solving a convex programming problem with convergence rate O(1/k²)", *Dokl. Akad. Nauk SSSR* 269(3) (1983) 543–547; English: *Soviet Math. Dokl.* 27 (1983) 372–376 | Math-Net.ru dan46009; zbMATH | 4886 + a duplicate record of 1299 / 1790 + 878 | solo |
| 3 | Nesterov & Nemirovskii, *Interior-Point Polynomial Algorithms in Convex Programming* (SIAM Studies in Applied Mathematics 13, 1994) | DOI 10.1137/1.9781611970791 | 4376 / 4401 / 3071 | joint book |
| 4 | "Smooth minimization of non-smooth functions", *Math. Program.* 103(1) (2005) 127–152 | DOI 10.1007/s10107-004-0552-5 | 2990 / — / 1639 | solo |
| 5 | "Gradient methods for minimizing composite functions", *Math. Program.* 140(1) (2013) 125–161 | DOI 10.1007/s10107-012-0629-5 (CORE DP 2007/76) | 1580 + 1290 for the DP / — / 964 | solo |
| 6 | "Efficiency of coordinate descent methods on huge-scale optimization problems", *SIAM J. Optim.* 22(2) (2012) 341–362 | DOI 10.1137/100802001 (CORE DP 2010/2) | 1551 / — / 722 | solo |
| 7 | Nesterov & Spokoiny, "Random gradient-free minimization of convex functions", *Found. Comput. Math.* 17(2) (2017) 527–566 | DOI 10.1007/s10208-015-9296-2 | 1431 / 879 / 612 | joint |
| 8 | *Lectures on Convex Optimization* (Springer Optimization and Its Applications 137, 2018) | DOI 10.1007/978-3-319-91578-4 | 1306 / 1028 / 792 | solo book |
| 9 | Nesterov & Polyak, "Cubic regularization of Newton method and its global performance", *Math. Program.* 108(1) (2006) 177–205 | DOI 10.1007/s10107-006-0706-8 | 1228 / 824 / 521 | joint |
| 10 | "Primal-dual subgradient methods for convex problems", *Math. Program.* 120(1) (2009) 221–259 | DOI 10.1007/s10107-007-0149-x (CORE DP 2005/67) | 1086 / 870 / 526 | solo |
| 11 | Nesterov & Todd, "Self-scaled barriers and interior-point methods for convex programming", *Math. Oper. Res.* 22(1) (1997) 1–42 | DOI 10.1287/moor.22.1.1 | 741 / — / 431 | joint |
| 12 | "Universal gradient methods for convex optimization problems", *Math. Program.* 152 (2015) 381–404 | DOI 10.1007/s10107-014-0790-0 (CORE DP 2013/26) | 409 / — / 179 | solo |

Seven of the top twelve works are single-authored, counting the two solo books [practice, primary].

---

## 2. Landscape by period

Periods follow career setting (Moscow → Louvain) and theme. Five-year counts from DBLP and zbMATH are given where useful.

| Period (setting) | Themes | Confirmed works (examples; all tool-checked) |
|---|---|---|
| **1977–1984**. Moscow State Univ. MSc 1977; researcher at CEMI; PhD 1984 at the Institute of Control Sciences, advisor B. T. Polyak (thesis "Numerical methods for degenerate optimization problems", per his own CV; thesis not read) | Uniformly convex functionals; testing first-order methods; line search; the optimal (fast) gradient method; nonsmooth and quasiconvex minimization; cost of computing gradients | Vladimirov, Nesterov, Chekanov, "On uniformly convex functionals", *Vestn. Mosk. Univ. Ser. XV* 1978 no. 3 (zbMATH) · Nesterov & Skokov, "The first order methods of nonlinear unconditional optimization", in *Numerical Methods of Mathematical Programming*, Moscow 1980, 6–60 (zbMATH) · "On a one-dimensional search procedure in methods of unconstrained minimization of a function of several variables", *USSR Comput. Math. Math. Phys.* 22(3) (1982) 233–238, DOI 10.1016/0041-5553(82)90144-6 · **the 1983 Doklady paper** (Math-Net.ru dan46009) · "One class of methods of unconditional minimization of a convex function, having a high rate of convergence", *USSR Comput. Math. Math. Phys.* 24(4) (1984) 80–82, DOI 10.1016/0041-5553(84)90234-9 · Kim, Nesterov, Cherkasskii, "An estimate of the effort in computing the gradient", *Sov. Math. Dokl.* 29 (1984) 384–387 (zbMATH; not read. The title suggests work on the cost of gradient evaluation, i.e. reverse-mode differentiation [inferred]). |
| **1985–1992**. Moscow, CEMI; with Nemirovski | Optimal smooth methods; nonsmooth (lexicographic) differentiation; the polynomial-time barrier theory for LP → QP → convex programming; conic duality | Nemirovskii & Nesterov, "Optimal methods of smooth convex minimization", *USSR Comput. Math. Math. Phys.* 25(2) (1985) 21–30, DOI 10.1016/0041-5553(85)90100-4 · Nesterov & Cherkasskii, "Lexicographic rules for differentiation of nonsmooth functions", *Sov. Math. Dokl.* 36(2) (1988) 233–235 (zbMATH) · "Method of linear programming with cubic complexity", *Èkon. Mat. Metody* 24 (1988) 174–176 (zbMATH) · "Polynomial methods in the linear and quadratic programming", *Sov. J. Comput. Syst. Sci.* 26(5) (1988) 98–101 (zbMATH) · Nesterov & Nemirovskii, "Polynomial barrier methods in convex programming", *Èkon. Mat. Metody* 24(6) (1988) 1084–1091 (zbMATH) · Nesterov & Nemirovskii, "Acceleration and parallelization of the path-following interior point method for a linearly constrained convex quadratic problem", *SIAM J. Optim.* 1(4) (1991) 548–564, DOI 10.1137/0801033 · Nesterov & Nemirovsky, "Conic formulation of a convex programming problem and duality", *Optim. Methods Softw.* 1(2) (1992) 95–115, DOI 10.1080/10556789208805510. Nesterov also lists a 1989 CEMI preprint, "Self-concordant functions and polynomial time methods in Convex Programming", on his Academia Europaea page [stated]; I found no independent record of it. |
| **1993–2002**. Louvain I (CORE; co-director of CORE 1999–2003 per his CV) | The IPM book and its extensions (self-scaled cones, long-step, surface-following, infeasibility detection); cutting-plane and bundle methods; SDP relaxations of nonconvex QP; economics and control side projects | 1994 SIAM book · Lemaréchal, Nemirovskii, Nesterov, "New variants of bundle methods", *Math. Program.* 69 (1995) 111–147, DOI 10.1007/BF01585555 · "Complexity estimates of some cutting plane methods based on the analytic barrier", *Math. Program.* 69 (1995) 149–176, DOI 10.1007/BF01585556 · Anderson, de Palma, Nesterov, "Oligopolistic competition and the optimal provision of products", *Econometrica* 63(6) (1995) 1281–1301, DOI 10.2307/2171770 · "Long-step strategies in interior-point primal-dual methods", *Math. Program.* 76 (1997) 47–94, DOI 10.1007/BF02614378 · "Interior-point methods: an old and new approach to nonlinear programming", *Math. Program.* 79 (1997) 285–297, DOI 10.1007/BF02614321 · Nesterov & Todd 1997 (MOR, above); "Primal-dual interior-point methods for self-scaled cones", *SIAM J. Optim.* 8(2) (1998) 324–364, DOI 10.1137/S1052623495290209 · "Semidefinite relaxation and nonconvex quadratic optimization", *Optim. Methods Softw.* 9 (1998) 141–160, DOI 10.1080/10556789808805690 · Nesterov, Todd, Ye, "Infeasible-start primal-dual methods and infeasibility detectors for nonlinear programming problems", *Math. Program.* 84 (1999) 227–267, DOI 10.1007/s10107980009a · Nesterov & Vial, "Homogeneous analytic center cutting plane methods…", *SIAM J. Optim.* 9(3) (1999) 707–728, DOI 10.1137/S1052623497324813 · Nesterov & Todd, "On the Riemannian geometry defined by self-concordant barriers and interior-point methods", *Found. Comput. Math.* 2 (2002) 333–361, DOI 10.1007/s102080010032 |
| **2003–2009**. Louvain II: "structural" first-order methods. DBLP 2005–09: 11 of 18 records single-authored, the highest solo share of any period | Smoothing; excessive gap; the second textbook; cubic regularization and its acceleration; dual extrapolation for VIs; primal-dual subgradient (dual averaging); relative-scale optimization; nonsmooth calculus; joint spectral radius (with Blondel) | 2004 book · "Smooth minimization of non-smooth functions" (2005; CORE DP 2003/12 per the ICM 2010 reference list) · "Excessive gap technique in nonsmooth convex minimization", *SIAM J. Optim.* 16 (2005) 235–249, DOI 10.1137/S1052623403422285 · "Lexicographic differentiation of nonsmooth functions", *Math. Program.* 104 (2005) 669–700, DOI 10.1007/s10107-005-0633-0 · Nesterov & Polyak 2006 · "Dual extrapolation and its applications to solving variational inequalities and related problems", *Math. Program.* 109 (2007) 319–344, DOI 10.1007/s10107-006-0034-z · "Modified Gauss–Newton scheme with worst case guarantees for global performance", *Optim. Methods Softw.* 22 (2007) 469–483, DOI 10.1080/08927020600643812 · "Smoothing technique and its applications in semidefinite optimization", *Math. Program.* 110 (2007) 245–259, DOI 10.1007/s10107-006-0001-8 · "Accelerating the cubic regularization of Newton's method on convex problems", *Math. Program.* 112 (2008) 159–181, DOI 10.1007/s10107-006-0089-x · "Parabolic target space and primal-dual interior-point methods", *Discrete Appl. Math.* 156 (2008) 2079–2100, DOI 10.1016/j.dam.2007.05.002 · "Rounding of convex sets and efficient gradient methods for linear programming problems", *Optim. Methods Softw.* 23 (2008) 109–128, DOI 10.1080/10556780701550059 · primal-dual subgradient 2009 · "Unconstrained convex minimization in relative scale", *Math. Oper. Res.* 34 (2009) 180–193, DOI 10.1287/moor.1080.0348 · Blondel & Nesterov, "Computationally efficient approximations of the joint spectral radius", *SIAM J. Matrix Anal. Appl.* 27 (2005) 256–272, DOI 10.1137/040607009 |
| **2010–2014**. Huge-scale, randomized and inexact | Coordinate descent; subgradient methods for huge-scale problems; gradient-free random search; inexact oracles; double smoothing; non-symmetric conic; first applications of network science | Coordinate descent 2012 · "Barrier subgradient method", *Math. Program.* 127 (2011) 31–56, DOI 10.1007/s10107-010-0421-3 · "Towards non-symmetric conic optimization", *Optim. Methods Softw.* 27 (2012) 893–917, DOI 10.1080/10556788.2011.567270 · Devolder, Glineur, Nesterov, "Double smoothing technique for large-scale linearly constrained convex optimization", *SIAM J. Optim.* 22 (2012) 702–727, DOI 10.1137/110826102 · Composite 2013 · Nesterov & Nemirovski, "On first-order algorithms for ℓ1/nuclear norm minimization", *Acta Numerica* 22 (2013) 509–575, DOI 10.1017/S096249291300007X · Devolder, Glineur, Nesterov, "First-order methods of smooth convex optimization with inexact oracle", *Math. Program.* 146 (2014) 37–75, DOI 10.1007/s10107-013-0677-5 · "Subgradient methods for huge-scale optimization problems", *Math. Program.* 146 (2014) 275–297, DOI 10.1007/s10107-013-0686-4 · Journée, Nesterov, Richtárik, Sepulchre, "Generalized power method for sparse principal component analysis", *JMLR* 11 (2010) 517–553, arXiv 0811.4724 · Traag, Van Dooren, Nesterov, "Narrow scope for resolution-limit-free community detection", *Phys. Rev. E* 84 (2011) 016114, DOI 10.1103/PhysRevE.84.016114 |
| **2015–2019**. Universality and a second-order revival | Universal (parameter-free) gradient methods; relative smoothness; regularized Newton with Hölder Hessians; implementable tensor methods; the third textbook; Russian applied network (Gasnikov, Dvurechensky) | Universal 2015 · Random gradient-free 2017 · Nesterov & Shikhman, "Quasi-monotone subgradient methods for nonsmooth convex minimization", *J. Optim. Theory Appl.* 165 (2015) 917–940, DOI 10.1007/s10957-014-0677-5 · Nesterov & Tunçel, "Local superlinear convergence of polynomial-time interior-point methods for hyperbolicity cone optimization problems", *SIAM J. Optim.* 26 (2016) 139–170, DOI 10.1137/140998950 · Grapiglia & Nesterov, "Regularized Newton methods for minimizing functions with Hölder continuous Hessians", *SIAM J. Optim.* 27 (2017) 478–506, DOI 10.1137/16M1087801 · Nesterov & Stich, "Efficiency of the accelerated coordinate descent method on structured optimization problems", *SIAM J. Optim.* 27 (2017) 110–123, DOI 10.1137/16M1060182 · Lu, Freund, Nesterov, "Relatively smooth convex optimization by first-order methods, and applications", *SIAM J. Optim.* 28 (2018) 333–354, DOI 10.1137/16M1099546, arXiv 1610.05708 · 2018 book · "Complexity bounds for primal-dual methods minimizing the model of objective function", *Math. Program.* 171 (2018) 311–330, DOI 10.1007/s10107-017-1188-6 · Grapiglia & Nesterov, "Accelerated regularized Newton methods for minimizing composite convex functions", *SIAM J. Optim.* 29 (2019) 77–99, DOI 10.1137/17M1142077 · "Implementable tensor methods in unconstrained convex optimization", *Math. Program.* 186 (2021) 157–183, DOI 10.1007/s10107-019-01449-1 (CORE DP 2018/05) |
| **2020–2026**. High-order, quasi-Newton, and a return to IPMs. Now with student teams and several affiliations: emeritus at UCLouvain; Corvinus Budapest per OpenAlex and Wikipedia; fractional professor at CUHK-Shenzhen from 2024 per Wikipedia | Contracting-point and tensor methods; superfast second-order; explicit superlinear rates for classical quasi-Newton; high-order proximal point; quartic regularity; universal complexity bounds; lower bounds; LP/SDO interior-point methods with a Hungarian group | Doikov & Nesterov, "Local convergence of tensor methods", *Math. Program.* 193 (2022) 315–336, DOI 10.1007/s10107-020-01606-X · Rodomanov & Nesterov, "Greedy quasi-Newton methods with explicit superlinear convergence", *SIAM J. Optim.* 31 (2021) 785–811, DOI 10.1137/20M1320651, arXiv 2002.00657 · Rodomanov & Nesterov, "Rates of superlinear convergence for classical quasi-Newton methods", *Math. Program.* 194 (2022) 159–190, DOI 10.1007/s10107-021-01622-5, arXiv 2003.09174 · "Superfast second-order methods for unconstrained convex optimization", *J. Optim. Theory Appl.* 191 (2021) 1–30, DOI 10.1007/s10957-021-01930-y · Doikov, Mishchenko, Nesterov, "Super-universal regularized Newton method", *SIAM J. Optim.* 34 (2024) 27–56, DOI 10.1137/22M1519444, arXiv 2208.05888 · Doikov & Nesterov, "Gradient regularization of Newton method with Bregman distances", *Math. Program.* 204 (2024) 1–25, DOI 10.1007/s10107-023-01943-7, arXiv 2112.02952 · "Quartic regularity", *Vietnam J. Math.* 53 (2025) 553–575, DOI 10.1007/s10013-024-00720-z, arXiv 2201.04852 (CORE DP 2022/01) · Florea & Nesterov, "An optimal lower bound for smooth convex functions", *Found. Comput. Math.* 25 (2025) 1939–1973, DOI 10.1007/s10208-025-09712-y, arXiv 2404.18889 · Dvurechensky & Nesterov, "Improved global performance guarantees of second-order methods in convex minimization", *Found. Comput. Math.* 26 (2026) 2165–2205, DOI 10.1007/s10208-025-09726-6, arXiv 2408.11022 · E.-Nagy, Illés, Nesterov, Rigó, "New interior-point algorithm for linear optimization based on a universal tangent direction", *SIAM J. Optim.* 36 (2026) 185–203, DOI 10.1137/24M1705780 · "Asymmetric long-step primal-dual interior-point methods with dual centering", arXiv 2503.10155 (2025) · "Universal complexity bounds for universal gradient methods in nonlinear optimization", arXiv 2509.20902 (2025) · Doikov & Nesterov, "Universal reduced-operator method and high-order global curvature bounds", arXiv 2511.07341 · "Theorem of alternative for extended homogeneous linear system and its application in conic optimization", arXiv 2603.21500 (2026) |

### 2.1 Patterns in the landscape

1. **New lines start with a solo paper; collaborators come later.** [practice, primary]
   - The conceptual turns are single-authored: 1983 (fast gradient), 2005 (smoothing), CORE DP 2007/76 (composite), 2009 (dual averaging), 2012 (coordinate descent), 2015 (universal), 2019/2021 (implementable tensor). So are all three textbooks except the 1994 IPM book.
   - Joint work follows. After the tensor paper came Grapiglia, Doikov, Ahookhosh and Dvurechensky. After coordinate descent came Stich, Necoara and Shpirko. After smoothing came Devolder and Glineur.
   - Exceptions are the IPM theory (Nemirovski), cubic regularization (Polyak) and self-scaled cones (Todd): the foundational joint works are with senior peers.
2. **Preprint first, journal much later. The preprint carries the idea.** [practice, primary]
   - Smoothing: CORE DP 2003/12 → *Math. Program.* 2005.
   - Primal-dual subgradient: CORE DP 2005/67 → 2009.
   - Composite: CORE DP 2007/76 → *Math. Program.* 2013, six years later. It was already cited as a DP in his ICM 2010 paper.
   - Coordinate descent: CORE DP 2010/2 (dated 2010-02-02 on IDEAS) → *SIAM J. Optim.* 2012.
   - Universal: CORE DP 2013/26 → 2015.
   - Tensor: CORE DP 2018/05. Received by *Math. Program.* 29 March 2018, accepted 4 November 2019, in an issue in 2021 (Crossref dates).
   - arXiv enters mostly through co-authors. Russian co-authors from 2014, students from 2019. His own solo arXiv postings start in 2022 ("Quartic regularity" = CORE DP 2022/01).
   - All eight arXiv abstract pages I checked have a single version (v1). He does not post revised versions publicly.
3. **Few venues.** [practice, primary]
   - Of 119 non-preprint DBLP records: *Math. Program.* 33, *SIAM J. Optim.* 22, *JOTA* 14, *Optim. Methods Softw.* 12, *SIMAX* 6, *Found. Comput. Math.* 5, *Math. Oper. Res.* 4.
   - Machine-learning venues are rare and always with co-authors: NIPS 2016, NeurIPS 2020, ICML 2020 ×2, ICIP 2018.
   - The CORE / RePEc discussion-paper series is his working-paper channel. OpenAlex counts 42 RePEc items.
4. **Author order is not alphabetical, so position statistics mislead.** [observed + practice]
   - The IMU citation notes: "It is noteworthy that Nesterov was listed as the first author of the book, although Nemirovski was more senior and would appear first alphabetically in both English and Russian languages." (IMU Gauss Prize 2026 citation, p. 1) [observed, secondary].
   - The Nesterov–Nemirovski papers of 1991, 1994, 1995, 1998, 2008, 2013 and 2015 all list Nesterov first. The 1985 paper is "Nemirovskii, Nesterov", and the three-author 1990 and 1995 papers are alphabetical [practice].
   - With students the order is mostly alphabetical ("Doikov, Nesterov"; "Grapiglia, Nesterov"; "Rodomanov, Nesterov"), but not always ("Nesterov, Florea" 2022; "Nesterov, Gasnikov, Guminov, Dvurechensky" 2021).
   - OpenAlex's "last author" count for 2020–24 (32 of 54) therefore mostly reflects the alphabet, not a PI role [inferred].
   - The solo share does fall, and that is real [practice, DBLP]: 2005–09, 11 of 18; 2010–14, 5 of 17; 2015–19, 2 of 20; 2020–24, 8 of 37; 2025–26, 0 of 7.
5. **Textbooks consolidate each decade.** [practice + observed]
   - 1994 (IPM theory), 2004 (a course: the zbMATH review says each of four chapters has three sections, each "corresponding approximately to a two-hour lecture"), 2018 (xxiii + 589 pp.).
   - The 2018 book is split into Part I "Black-Box Optimization" and Part II "Structural Optimization" (zbMATH review by Anholcer). This mirrors the ICM 2010 programme (§3).
   - His CV lists the course "Nonlinear Optimization (INMA 2460; 1996 - now)" [stated]. That the 2004 book grew out of this course is [inferred].
6. **He comes back to old themes decades later.** [practice, primary]
   - Interior-point methods: 1988 → 1994 → 2008 (parabolic target space) → 2024–26 (greedy parabolic target-following for LP, asymmetric long-step SDO, theorem-of-alternative infeasible start).
   - Newton / second-order: 1984 thesis on degenerate problems (not read) → 2006 cubic → 2017–2025 regularized Newton, tensor, quasi-Newton rates, quartic regularity.
   - Nonsmooth differentiation: 1987–88 Soviet notes → 2005 *Math. Program.*
   - Line search and adaptivity: 1982 → the backtracking in the 1983 method → the "line search" procedures in the 2007 composite DP → universal methods 2015 and 2025.
7. **"The only input is the accuracy" recurs.** [practice, primary; abstracts]
   - 1983: the step-size search starts from the previous a_{k−1}, so L need not be known, at the cost of at most O(log₂ L) halvings.
   - 2007 DP abstract: estimating the unknown class parameters "can only multiply the complexity of each iteration by a small constant factor".
   - 2013 universal DP: "The only essential input parameter is the required accuracy of the solution."
   - 2022 super-universal Newton: "no a priori knowledge of parameters is needed".
   - 2025 universal bounds: "the only input parameter is the required accuracy of the approximate solution".
   - 2026 conic IPM: "Given by the target upper bound ε > 0 for the duality gap as the only input parameter".
8. **Side streams come from CORE's economics and systems setting.** [practice]
   - Economics and transport with de Palma, Anderson, Shikhman, Vial and Babonneau (e.g. *Econometrica* 1995; Babonneau, Nesterov, Vial, "Design and operations of gas transmission networks", *Oper. Res.* 60 (2012) 34–47, DOI 10.1287/opre.1110.1001).
   - Control and matrices with Van Dooren, Genin and Blondel.
   - Networks with Traag.
   - Traffic and PageRank with Gasnikov's group.
   - These application papers are almost always co-authored. The methods papers are often solo.

### 2.2 Collaboration network and likely students

| Collaborator | Span | Records | Relation (evidence) |
|---|---|---|---|
| Arkadi Nemirovski | 1985–2026 | ≈10 in DBLP under three spellings, plus the 1980s zbMATH items | Peer. Acknowledged in the 1983 paper (§4A). IPM book. Acta Numerica 2013. Joint editor of the 2026 Polyak memorial issue. [practice] |
| Boris T. Polyak | 1984 PhD; 2006; memorial issues 2017 and 2026 | 1 research paper + 2 prefaces | PhD advisor (Math Genealogy; Wikipedia) [observed, secondary] |
| Michael J. Todd; Yinyu Ye | 1997–2002; 1999 | 4; 1 | Self-scaled cones; infeasibility detectors. Ye is a member of this team. |
| Jean-Philippe Vial | 1999–2012 | 4 | Cutting planes, stochastic programming, gas networks |
| Paul Van Dooren; Vincent Blondel; Yves Genin | 1999–2020 | 7; 3; 3 | Control, matrices, joint spectral radius (UCLouvain INMA colleagues) |
| François Glineur | 2012–2023 | 5 | Inexact oracle, double smoothing, NMF |
| Olivier Devolder; Vincent Traag | 2009–2014; 2010–2013 | 2 + DPs; 2–3 | **Students.** Math Genealogy lists both as his PhD students, UCLouvain 2013 [observed, secondary]. It also lists Vania Dos Santos Eleuterio (ETH Zürich 2009). |
| Geovani N. Grapiglia | 2016–2023 | 6 | Regularized Newton, tensor. Postdoc or visitor role [inferred; not verified]. |
| Nikita Doikov | 2019–2026 | 10–15 | Likely PhD student (14 of 15 papers "Doikov, Nesterov"; UCLouvain) [inferred]. |
| Anton Rodomanov | 2019–2023 | 5–6 | Likely PhD student [inferred]. |
| Mihai I. Florea | 2021–2025 | 2 | Likely student [inferred]. |
| Alexander Gasnikov; Pavel Dvurechensky; Vladimir Spokoiny | 2014–2026 | 3–17 depending on database | Russian and Berlin (WIAS) applied network: traffic, PageRank, stochastic. |
| Vladimir Shikhman | 2015–2022 | 5 | Economics: price adjustment, Fisher–Gale equilibrium, discrete choice. |
| M. E.-Nagy, T. Illés, P. R. Rigó | 2025–2026 | 3 + arXiv | Budapest interior-point group (matches the Corvinus affiliation). |

His Academia Europaea CV says "Five Ph.D.-students (5 defended)" (page revision of 3 July 2021) [stated]. Math Genealogy lists three. The full student list goes to agent 04.

---

## 3. What Nesterov himself calls important

- **He refuses to name a best work.** [stated, primary; NCCR Automation interview, 15 Aug 2023] "I have been working in optimization for 45 years," … "I have had moments where I managed to understand some things, but I don't think I can say, 'This is the best.'" His yardstick in the same interview: "Before you started to think about something, you had methods which were able to somehow solve the problem, and it took an hour to find the solution. And then after your contribution, it's reduced to one minute. So you can see that you did something useful."
- **His self-curated list.** [stated, primary; Academia Europaea page "Yurii Nesterov - Selected Publications", date not shown] Ten items:
  - the 2018 and 2004 books;
  - the 1994 IPM book, cited under the title "Interior point polynomial methods in convex programming. Theory and Applications";
  - the 1989 CEMI preprint on self-concordant functions;
  - implementable tensor methods (2019);
  - Grapiglia–Nesterov, accelerated regularized Newton (2019);
  - Gasnikov, Gasnikova, Nesterov on transportation equilibria (2018);
  - complexity bounds for primal-dual methods (2018);
  - coordinate descent (2012);
  - Baes, Del Pia, Nesterov, Onn, Weismantel on integer minimization (2012).

  **Not on the list**: the 1983 paper, smoothing (2005) and cubic regularization (2006). The list may be recency-weighted [inferred].
- **How he groups his own work.** [stated, primary; ICM 2010] He presents his contributions as one programme, "Structural Optimization": "we use additional information on the structure of specific problem instances for accelerating standard Black-Box methods" (abstract, p. 2964). His worked examples are:
  - primal-dual subgradient methods;
  - polynomial-time IPMs (self-concordant barriers);
  - smoothing;
  - composite minimization;
  - relative scale.
- **Current turning point.** [stated, primary; NCCR 2023] "Several years ago, we started to study the higher order methods, and it appears that they cannot be explained by standard Optimization Theory. And now we understand that in the standard Optimization we did only the first step by developing the first-order methods."

---

## 4. Signature-work anatomies

Five works were chosen:

| Work | Why chosen |
|---|---|
| A. 1983 | Most cited article and origin of the accelerated method |
| B. 1988–1994 IPM | Most cited overall. His "first example" of the Golden Rules (§3). On his self-selected list. |
| C. 2005 smoothing | Turning point into structural first-order methods |
| D. 2006 cubic regularization → 2019/21 tensor | Turning point into global-complexity second-order and high-order methods. Most relevant to an NLP-solver team. |
| E. 2012 coordinate descent | Huge-scale turn. On his self-selected list. |

"Origin" and "abandoned paths" are marked **inferred** wherever no first-hand account was found.

### A. "A method of solving a convex programming problem with convergence rate O(1/k²)" (*Dokl. Akad. Nauk SSSR* 269(3) 1983, 543–547; *Sov. Math. Dokl.* 27, 372–376). Full text read (Russian original, Math-Net.ru).

| Dimension | Content |
|---|---|
| Origin | **[stated, primary]** Acknowledgement, p. 547: "Автор искренне признателен А.С. Немировскому за беседы, которые стимулировали его интерес к рассмотренным вопросам." (my translation: the author thanks A. S. Nemirovski for conversations that stimulated his interest in the questions considered). The paper has two references: Nemirovski–Yudin 1979, cited for the unimprovable bound, and Pshenichny–Danilin 1975, cited for the line search. Presented to the journal by academician L. V. Kantorovich on 9 VII 1982 and received on 19 VII 1982. Affiliation: Центральный экономико-математический институт АН СССР. **[inferred]**: The problem framed itself. Nemirovski–Yudin's lower bound for smooth convex problems left a gap above the plain gradient method, and the paper's §1 claim is precisely a rate "неулучшаемую на рассматриваемом классе задач" (unimprovable on the class; p. 543). |
| Why then | **[inferred]** Information-based complexity (Nemirovski–Yudin 1979) had just made "optimal method" a well-posed target. Jackson's IMU write-up says Soviet mathematicians "emphasized worst-case analysis of algorithms much more than mathematicians in the West" [observed, secondary, p. 2]. |
| Key insight | Give up monotonicity. p. 543: "этот метод строит минимизирующую последовательность точек {x_k}, которая не является релаксационной. Эта особенность позволяет свести к минимуму вычислительные затраты на каждом шаге." (my translation: the sequence is not relaxational, i.e. not monotone, and this keeps per-step cost minimal). The extrapolation is described as an "овражный" (ravine) step, and the paper states that the method does not ensure monotone decrease of f (p. 543). The update is y_{k+1} = x_k + (a_k − 1)(x_k − x_{k−1})/a_{k+1}, with a_{k+1} = (1 + √(4a_k² + 1))/2. |
| Minimum evidence | The proof alone. Theorem 1 gives f(x_k) − f* ≤ C/(k+2)². The paper contains no numerical experiment [practice, primary]. |
| Built-in engineering choices | Three are already in the 5-page note [practice, primary]. **(1) Adaptive step size.** Backtracking "начиная с a_{k−1} (а не с единицы, как в [2])" (starting from a_{k−1}, not from one as in [2]; p. 543), with at most O(log₂ L) halvings in total. **(2) Restart for strong convexity.** Every ⌈4√(L/m)⌉ − 1 iterations the method is restarted from x_N; p. 545: "необходимо обновить метод и опять начать счет … из точки x_N как из начальной". This gives the optimal linear rate. **(3) Extension** to max-type composite objectives F(f(x)) over a set Q via the "gradient mapping" of Nemirovski–Yudin, and to projection onto simple sets (pp. 545–547). |
| Abandoned paths | None stated in the paper. Later simplifications show he kept re-deriving the constants. ICM 2010 gives a "simplified version" with momentum coefficient k/(k+3), and footnote 2 says a_k = 1 + k/2 suffices "since in the proof we need only to ensure a²_{k+1} − a²_k ≤ a_{k+1}" (p. 2966) [stated, primary]. Re-derivations appeared in 1985 (with Nemirovski) and 1988 ("On an approach to the construction of optimal methods for minimizing smooth convex functions", *Èkon. Mat. Metody* 24(3) 509–517; zbMATH; **not read**). |
| Reception | **Slow, then enormous.** Jackson (IMU write-up, p. 1) [observed, secondary]: "Though an ingenious and decisive result, it went largely unnoticed. One reason was the Cold War … A more important reason was that the kinds of problems people were trying to solve back in the 1980s were not amenable to Nesterov's method." Also: "Since in the mid-2000s, Nesterov's thesis work has racked up thousands of citations". The IMU 2026 citation highlights "Nesterov momentum" in ML training. **His own explanation of why his variants won over older prototypes** (ICM 2010, p. 2976) [stated]: the heavy-ball method and others "did not result in a significant change in computational practice since they were not provided with a convincing complexity analysis." |
| Methods shown | Close the gap between a proven lower bound and the best known method. Trade monotonicity for rate. Make unknown constants adaptive. Restart to get strongly convex rates. Proof is the evidence. |

### B. Self-concordant barriers and polynomial-time IPMs: 1988 papers → 1989 CEMI preprint → *Interior-Point Polynomial Algorithms in Convex Programming* (SIAM 1994, with A. Nemirovskii, DOI 10.1137/1.9781611970791). The book was not read. Evidence comes from Nesterov's ICM 2010 account, the dated record, the IMU citation and the zbMATH review.

| Dimension | Content |
|---|---|
| Origin | **[stated, primary; ICM 2010 p. 2971]** "Historically, the first example of that type was the theory of polynomial-time interior-point methods (IPM) based on self-concordant barriers [15]. The first step in the development of this theory was discovery of unconstrained minimization problems which can be solved efficiently by the Newton method." **[practice, primary]** Dated record: first LP and QP ("Method of linear programming with cubic complexity", 1988; "Polynomial methods in the linear and quadratic programming", 1988); then the convex generalization with Nemirovski ("Polynomial barrier methods in convex programming", 1988); then the 1989 CEMI preprint (self-listed); then the 1991 SIOPT paper, the 1992 conic-duality paper and the 1994 book. |
| Why then | **[observed, secondary; IMU citation p. 1]** "While polynomial-time interior-point algorithms for LP had been known since the work of Karmarkar in 1984, such algorithms for semidefinite and conic linear programs were completely new." **[stated; his 2004 preface as quoted in the IMU citation, p. 2; the preface itself not read]** On Karmarkar: "… the most surprising feature of this algorithm was that the theoretical prediction of its high efficiency was supported by excellent computational results. This unusual fact dramatically changed the style and direction of the research in nonlinear optimization." |
| Key insight | An affine-invariant condition, D³f(x)[h]³ ≤ 2 D²f(x)[h]^{3/2}, under which the damped Newton method has a checkable region of quadratic convergence. Adding the barrier parameter ν gives path-following in O(√ν ln(ν/ε)) (ICM pp. 2971–2973). The universal barrier shows that every convex set has an O(n)-self-concordant barrier. **His reading of why this beats the black-box lower bounds** (p. 2973): "something should violate the Black-Box assumptions. And indeed, this is the process of creating the self-concordant barriers. There exists a kind of calculus for doing this. However, it needs a direct access to the structure of the problem". |
| Minimum evidence | The Newton analysis on self-concordant functions: "It appears that the properties of these functions fit very well the Newton scheme." (p. 2971) [stated]. The 1994 book has no computations. The zbMATH review (M. A. Hanson) says: "Algorithms are given, but numerical results are omitted." [observed, secondary] |
| Abandoned paths | **[stated, ICM p. 2969]** He rejected structure-by-analytic-type: "One possible way to describe the structure is to fix the analytical type of functional components. … It can help, but this approach is very fragile: If we add just a single constraint of another type, then we get a new problem class, and all theory must be redone from scratch." He later partly left heavy IPM iterations for first-order methods (p. 2973): "each iteration of the path-following schemes is quite heavy. This is the reason for development of the cheap gradient schemes". He came back to IPMs in 2008 and again in 2024–26. |
| Reception | The IMU citation (p. 1): the book "settled his reputation"; "The study of algorithms and applications for SDP subsequently exploded". Dantzig Prize 2000 (Wikipedia, secondary). It is the most cited item in OpenAlex (4401). |
| Methods shown | The "Golden Rules" (ICM p. 2970, boxed [stated]): "1. Find a class of problems which can be solved very efficiently. 2. Describe the transformation rules for converting the initial problem into desired form. 3. Describe the class of problems for which these transformation rules are applicable." Structure beats the black box. |

### C. "Smooth minimization of non-smooth functions" (*Math. Program.* 103(1) 2005 127–152, DOI 10.1007/s10107-004-0552-5; CORE DP 2003/12). Companions: excessive gap (SIOPT 2005) and SDP smoothing (MP 2007). The paper was not read. Evidence comes from ICM 2010 §4, where he explains its genesis himself.

| Dimension | Content |
|---|---|
| Origin | **[stated, primary; ICM p. 2973]** He presents it as the second application of the Golden Rules: "in accordance to Rule 1 in (15), we need to find a class of very easy problems. And this class can be discovered directly in the table (6)!" He compares the lower bounds for nonsmooth (C1) and smooth (C2) classes at ε = 10⁻² and asks: "Can the easy problems from C2 help us somehow in finding an approximate solution to the difficult problems from C1?" |
| Why then | **[stated, p. 2973]** "By certain circumstances, these results were discovered with a delay of twenty years. Perhaps they were too simple. Or maybe they are in a seemingly very sharp contradiction with the rigorously proved lower bounds of Complexity Theory." **[inferred]** The ingredients (the 1983 fast method, max-type representations, prox-functions) had existed since the 1980s. What changed was his willingness to "open the black box" (§3). |
| Key insight | For f(x) = max_u {⟨Ax − b, u⟩ − φ(u)}, subtract μ·d(u) with a strongly convex prox-function d. The gradient becomes Lipschitz with constant O(1/μ), and the fast gradient method then gives O(1/ε) instead of O(1/ε²). No lower bound is violated, because (p. 2974) "in order to minimize a smooth approximation of nonsmooth function by an oracle-based scheme, we need to change the initial oracle. Therefore, from mathematical point of view, we violate the Black-Box assumption. On the other hand, in the majority of practical applications this change is not difficult." |
| Minimum evidence | A worked complexity comparison on max_j ⟨a_j, x⟩ over the simplex. Smoothing gives 4√(ln n · ln m)/N; subgradient gives √(ln n)/√(N+1) (pp. 2974–2975). Entropy smoothing makes the smoothed oracle a log-sum-exp as cheap as the original (p. 2975). |
| Abandoned paths | None known for his own work. He says smoothing for minimax was "also not new" (R. Polyak 1988), but it lacked "a convincing complexity analysis" (p. 2976) [stated about others]. |
| Reception | His most cited article (S2 2990). In ICM 2010 he points to follow-ups (d'Aspremont–Banerjee–El Ghaoui on sparse covariance; Hoda–Gilpin–Peña on Nash equilibria of sequential games) as evidence of "new and interesting research directions" (p. 2976). |
| Methods shown | Compare complexity classes to find the "easy" class. Change the oracle, not the theorem. Complexity analysis as the filter for which methods deserve attention. |

### D. "Cubic regularization of Newton method and its global performance" (Nesterov & Polyak, *Math. Program.* 108(1) 2006 177–205, DOI 10.1007/s10107-006-0706-8) → "Implementable tensor methods in unconstrained convex optimization" (*Math. Program.* 186 2021 157–183, DOI 10.1007/s10107-019-01449-1; CORE DP 2018/05). The 2006 paper was **not read** (paywalled). The 2019/21 abstract was read.

| Dimension | Content |
|---|---|
| Origin | **Not found. [inferred]** Polyak was his PhD advisor. His 1984 thesis title was "Numerical methods for degenerate optimization problems" (Academia Europaea CV). Whether the thesis anticipates cubic regularization is **not known** (thesis not read). |
| Prior art | **[observed, secondary; Cartis, Gould, Toint, ARC Part I, *Math. Program.* 127 (2011) 245–295, DOI 10.1007/s10107-009-0286-5, preprint p. 2]** Using the cubic model for steps "was, as far as we know, first considered by Griewank (in an unpublished technical report [19])". That report is A. Griewank, "The modification of Newton's method for unconstrained optimization by bounding cubic terms", Technical Report NA/12, DAMTP, Univ. of Cambridge, 1981 (as listed in CGT's references; **the report itself not verified**). CGT continue: "More recently, Nesterov and Polyak [25] considered a similar idea and the unmodified model m_k^C(s), although from a different perspective." Weiser, Deuflhard and Erdmann (2007) are credited as independent. |
| Why then | **[inferred]** By the early 2000s he had global worst-case complexity for first-order methods (the 2004 book). Newton's method had only local theory. So a global complexity result for second-order methods was the missing cell in his table. |
| Key insight | As summarized by CGT (p. 2) [observed]: if the step globally minimizes the cubic model and the Hessian is Lipschitz, then "the resulting algorithm has a better global-complexity bound than that achieved by the steepest descent method"; the model's global minimizer "could be computed in a manner acceptable from the complexity point of view"; and there are better bounds for star-convex and other special cases. |
| Minimum evidence | Proofs only. CGT (p. 2) [observed]: "Global convergence to second-order critical points and asymptotically quadratic rate of convergence were also proved for this method, but no numerical results were provided." |
| Follow-through | [practice, primary] 2007 modified Gauss–Newton (solo) → 2008 accelerated cubic regularization (solo) → 2017 Hölder-Hessian regularized Newton, 2019 accelerated (Grapiglia) → **2019/21 implementable tensor methods (solo)**. The abstract of the tensor paper: its methods "solve at each iteration an auxiliary problem of minimizing convex multivariate polynomial"; for third order, "an efficient technique for solving the auxiliary problem, which is based on the recently developed relative smoothness condition (Bauschke et al. …; Lu et al. in SIOPT 28(1):333–354, 2018)". Lu et al. is his own 2018 paper, so one of his lines supplied the tool for another. Result: O(1/k⁴), "very close to the lower bound of the order O(1/k⁵), which is also justified in this paper". Cost: "the computational cost of one iteration of this method remains on the level typical for the second-order methods". Then: superfast second-order (2021), quasi-Newton superlinear rates (2021–22), super-universal Newton (2022–24), quartic regularity (2022/25), improved global second-order guarantees (FoCM 2026). |
| Abandoned paths | **[inferred]** The standard Taylor model of order p ≥ 3 is nonconvex. The tensor paper takes the regularization large enough to make the auxiliary problem convex. That is a choice against nonconvex subproblems, but no source says he tried and dropped them. **[practice]** A published correction exists: Ahookhosh & Nesterov, "Correction: High-order methods beyond the classical complexity bounds: inexact high-order proximal-point methods", *Math. Program.* 208 (2024) 409–410, DOI 10.1007/s10107-024-02067-2. What it corrects was **not read**. |
| Reception | CGT turned the idea into ARC (called "ACO" in the preprint). Their abstract, preprint p. 1 [observed]: the new method "uses an adaptive estimation of the local Lipschitz constant and approximations to the global model-minimizer which remain computationally-viable even for large-scale problems", and "Numerical experiments with small-scale test problems from the CUTEr set show superior performance of the ACO algorithm when compared to a trust-region implementation." So the theory came from Nesterov–Polyak and the algorithm engineering from the trust-region school. See the tension in "Contradictions" on whether tensor methods are practical. |
| Methods shown | Put second-order methods on the same global worst-case footing as first-order ones. Make the subproblem convex by over-regularizing. Reuse your own tools across lines (relative smoothness → tensor). A lower bound accompanies every new rate. |

### E. "Efficiency of coordinate descent methods on huge-scale optimization problems" (*SIAM J. Optim.* 22(2) 2012 341–362, DOI 10.1137/100802001; CORE DP 2010/2, dated 2010-02-02 on IDEAS). Abstract and keywords read.

| Dimension | Content |
|---|---|
| Origin | **[stated, primary; DP keywords]** "Convex optimization; coordinate relaxation; worst-case efficiency estimates; fast gradient schemes; Google problem". So PageRank-type problems were the motivating application. Abstract: "For problems of this size, even the simplest full-dimensional vector operations are very expensive." |
| Why then | **[inferred]** Web-scale linear-algebra problems made full-vector operations the bottleneck, so the complexity model had to count them. |
| Key insight | Random partial update of variables with global rate estimates, plus an accelerated variant. Abstract: "Surprisingly enough, for certain classes of objective functions, our results are better than the standard worst-case bounds for deterministic algorithms." |
| Minimum evidence | Abstract [stated]: "Our numerical test confirms a high efficiency of this technique on problems of very big size." Here, unlike A–D, he reports numerics. |
| Abandoned paths | Unknown. |
| Reception | Jackson (IMU write-up, p. 3) [observed, secondary]: coordinate methods "had been in use for decades with little theoretical understanding of why they worked. Nesterov's paper provided a comprehensive theoretical development that opened the way for new uses of these methods." S2 1551 citations. On his self-selected list. Follow-ups: "Subgradient methods for huge-scale optimization problems" (MP 2014); Nesterov & Shpirko, SIOPT 24 (2014) 1444–1457, DOI 10.1137/130929345; Nesterov & Stich 2017; Necoara, Nesterov, Glineur, JOTA 173 (2017) 227–254, DOI 10.1007/s10957-016-1058-z. |
| Methods shown | Let problem scale redefine the cost model, then redo worst-case accounting. Randomization as an analysable design choice. |

---

## 5. Era and resource context

- **1977–1992, Moscow (CEMI).** [practice, primary] Short Doklady-style notes: the 1983 paper is 5 pages with 2 references and no numerics. Many results appeared only in Russian journals such as *Èkon. Mat. Metody* and *Zh. Vychisl. Mat. Mat. Fiz.*
  - He recalls the pace [stated, NCCR 2023]: "I got a letter once a month. I had to go to another floor to fetch it." Also: "There was no rush; you had time to think and to write a paper, check different variants etc. Now it's just impossible."
  - Isolation: Jackson cites the Cold War as a reason the 1983 result "went largely unnoticed" [observed].
  - In ICM 2010 he describes the software setting of the black-box era [stated, p. 2966]: "the interface between the general optimization packages and the problem's data was established by Fortran subroutines created independently by the users".
- **1993–2009, UCLouvain / CORE.** [practice] A single senior researcher. Working papers go out through the CORE DP series. Peers join the flagship joint works (Nemirovski, Todd, Polyak, Vial). The 2003–09 solo peak falls here.
- **2010–2026.** [practice] Student-driven teams (Devolder, Doikov, Rodomanov, Florea) and postdocs or visitors (Grapiglia). A Russian applied network (Gasnikov, Dvurechensky). A Budapest IPM group. Several affiliations: UCLouvain emeritus, Corvinus, CUHK-Shenzhen from 2024. arXiv appears from ≈2019. Machine learning appears mainly as motivation. There is almost no benchmark-heavy empirical work.

---

## 6. Contradictions (kept, not reconciled)

1. **Title of the 1983 paper.**
   - The Russian original and the zbMATH/Sov. Math. Dokl. record: "A method of solving a convex programming problem with convergence rate O(1/k²)".
   - Nesterov's own ICM 2010 reference [7] and Wikipedia: "A method for unconstrained convex minimization problem with the rate of convergence O(1/k²)". Note also that the Russian paper covers constrained max-type problems, not only unconstrained ones.
   - OpenAlex and Semantic Scholar carry both titles as separate records, one of them as "o(1/k^2)", and OpenAlex gives the venue as "Medical Entomology and Zoology". These are metadata errors.
2. **Dates of the 1983 paper.** The paper reads "Представлено академиком Л.В. Канторовичем 9 VII 1982" (presented 9 July 1982) and "Поступило 19 VII 1982" (received 19 July 1982). Presented before received, as printed. Math-Net.ru gives Received 19.07.1982.
3. **Are tensor methods practical?**
   - Nesterov (2019/21 abstract): with the relative-smoothness subsolver, "the third-order methods become implementable and very fast", with per-iteration cost "on the level typical for the second-order methods".
   - Jackson (IMU write-up, 2026, p. 3): "Requiring huge computing capacity, tensor methods remain theoretical constructs for now".
4. **How the 1983 method works, as described.**
   - The paper: a two-point extrapolation ("ravine" step) plus backtracking.
   - Jackson (p. 2): the method "combined information about all previous steps to generate a kind of average of the gradients". That fits later estimate-sequence and dual-averaging forms, not the 1983 text.
5. **Where he worked in 1983.** The paper's affiliation line is CEMI of the USSR Academy of Sciences. A blog post surfaced by the web search (Medium, "Gradient Descent Comes to the Five-Year Plan") calls him "a young mathematician at Moscow State University". His PhD was from the Institute of Control Sciences (Academia Europaea CV; Math Genealogy).
6. **Number of PhD students.** "Five Ph.D.-students (5 defended)" (Academia Europaea CV, 2021) vs three in Math Genealogy vs a co-authorship pattern suggesting more (Doikov, Rodomanov, Florea) [inferred].
7. **Page numbers of the primary-dual subgradient paper.** ICM 2010 reference [14] gives *Math. Program.* 120(1), 261–283. Crossref and DBLP give 221–259.
8. **Title of the 1994 book.** Published title: *Interior-Point Polynomial Algorithms in Convex Programming*. Nesterov's own lists (ICM 2010 [15]; Academia Europaea) cite "Interior point polynomial methods in convex programming: Theory and Applications".
9. **Citation counts** disagree by up to 2× across S2, OpenAlex and Crossref (e.g. the 2004 book: 6614 / 2735 / 2399). Google Scholar could not be checked. The IMU says ">50,000".
10. **Numerics.** His flagship theory works carry no computations: the 1983 paper, the 1994 book ("numerical results are omitted", zbMATH review) and the 2006 paper ("no numerical results were provided", CGT). Several first-order DPs report "preliminary" or "encouraging" experiments (the 2007 composite, 2010 coordinate-descent and 2013 universal abstracts). Both patterns are real. Which dominates depends on the line of work.

---

## 7. Gaps

- **Google Scholar profile** not accessible (CAPTCHA). No Scholar citation counts or ordering. The complete harvest is a later step.
- **Full texts not read**, because Springer, SIAM and the UCLouvain CORE-DP PDF host were blocked:
  - 2006 cubic regularization;
  - 2005 smoothing;
  - 2012 coordinate descent;
  - 2013 composite;
  - 2015 universal;
  - 2019/21 tensor;
  - the prefaces of the 2004 and 2018 books;
  - the 1994 book.

  So the origin of cubic regularization, and any abandoned variants in these papers, are unknown. The later reading step should target the prefaces and introductions first.
- **PhD thesis (1984)**, "Numerical methods for degenerate optimization problems": content not found or read.
- **1989 CEMI preprint** "Self-concordant functions and polynomial time methods in Convex Programming": known only from his own list. No library or database record was found.
- **Russian monograph(s) of the 1980s**: I did not find a tool-checkable record, so none is listed. For example, I have a memory-only lead on a 1989 book on effective methods in nonlinear programming, which stays unlisted.
- **Rejected papers and referee exchanges**: none found. The only published correction found is the 2024 Ahookhosh–Nesterov correction, and its content was not read.
- **First-hand origin stories** for the 1983 method beyond the acknowledgement, and for self-concordance beyond ICM 2010: none found with the 1-search budget. An interview-style account may exist in talks; that is agent 02 and 06 territory.
- **Student list**: to be verified by agent 04 (Doikov, Rodomanov, Florea, Devolder, Traag, Dos Santos Eleuterio).

---

## 8. Sources

1. DBLP, person 00/343 "Yurii E. Nesterov" (SPARQL export via `scripts/dblp_works.py`, 2026-09-28). https://dblp.org/pid/00/343. Primary (bibliographic record).
2. zbMATH Open author profile `nesterov.yurii` and 177 document records, incl. reviews by M. I. Todorov (2004 book), M. A. Hanson (1994 book), M. Anholcer (2018 book). https://zbmath.org/authors/nesterov.yurii. Primary records; reviews secondary.
3. OpenAlex author A5067792459, harvested 2026-09-28 into `../sources/publications/publications.md`. Primary record (split ID).
4. Semantic Scholar Graph API, author 143676697 and paper records. https://api.semanticscholar.org/. Secondary aggregator.
5. Crossref REST API records for the DOIs cited above (titles, volumes, pages, received/accepted dates). https://api.crossref.org/. Primary record.
6. arXiv author search "Nesterov, Yurii" (57 results) and abstract pages 2107.05958, 2509.20902, 2201.04852, 2503.10155, 2412.14934, 2603.21500, 2511.07341, 2208.05888. https://arxiv.org/. Primary.
7. Yu. E. Nesterov, "Метод решения задачи выпуклого программирования со скоростью сходимости O(1/k²)", *Dokl. Akad. Nauk SSSR* 269(3) (1983) 543–547. Full text read. https://www.mathnet.ru/eng/dan46009. Primary.
8. Yu. Nesterov, "Recent advances in structural optimization", *Proc. ICM 2010* (Hyderabad), Vol. IV, 2964–2978 (World Scientific / Hindustan Book Agency, 2011). Full text read. https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2010.4/ICM2010.4.pdf. Primary.
9. IMU / DMV, "Carl Friedrich Gauss Prize 2026: Yurii Nesterov" (short and long citation), ICM 2026, Philadelphia. https://www.mathunion.org/fileadmin/documents/2026-07/Gauss_Yurii_Nesterov_2026_Citation.pdf. Secondary (quotes the 2004 preface).
10. Allyn Jackson, "2026 Gauss Prize: Yurii Nesterov" (IMU write-up). https://www.mathunion.org/fileadmin/documents/2026-07/article-gauss-final.pdf. Secondary.
11. IMU Gauss Prize pages (laureate list; 2026 page). https://www.mathunion.org/imu-awards/carl-friedrich-gauss-prize. Secondary.
12. Robynn Weldon, "'This is an unprecedented overflow': Why the progress of his field alarms Yurii Nesterov", NCCR Automation, 15 Aug 2023 (interview). https://nccr-automation.ch/news/2023/unprecedented-overflow-why-progress-his-field-alarms-yurii-nesterov. Primary (stated; interview write-up).
13. Academia Europaea, Yurii Nesterov CV and "Selected Publications" (CV page revision of 3 Jul 2021). https://www.ae-info.org/ae/Member/Nesterov_Yurii/CV. Primary (self-written).
14. Mathematics Genealogy Project, id 102203. https://www.mathgenealogy.org/id.php?id=102203. Secondary.
15. Wikipedia, "Yurii Nesterov" (wikitext fetched 2026-09-28). https://en.wikipedia.org/wiki/Yurii_Nesterov. Secondary.
16. C. Cartis, N. I. M. Gould, Ph. L. Toint, "Adaptive cubic regularisation methods for unconstrained optimization. Part I: motivation, convergence and numerical results", *Math. Program.* 127 (2011) 245–295, DOI 10.1007/s10107-009-0286-5. Preprint read (intro and references): https://pure.unamur.be/ws/files/1332672/cgt31RR_I.pdf. Secondary (peer account).
17. IDEAS/RePEc pages of CORE Discussion Papers 2005/67, 2007/76, 2010/2, 2013/26, 2018/05 (abstracts, keywords, dates). https://ideas.repec.org/p/cor/louvco/2010002.html (and siblings). Primary (author abstracts).
18. UCLouvain CORE DP index 2010 (via WebFetch). https://sites.uclouvain.be/core/publications/coredp/coredp2010.html. Primary record (partial).
19. Web search result snippet: V. Manokhin, "Gradient Descent Comes to the Five-Year Plan" (Medium). https://valeman.medium.com/gradient-descent-comes-to-the-five-year-plan-4296f5e242ea. Secondary, low reliability; used only in Contradiction 5.

Blocked or not usable: Google Scholar (CAPTCHA); link.springer.com (JS challenge); epubs.siam.org (Cloudflare); www.uclouvain.be/cps/… CORE-DP PDFs (connection reset).
