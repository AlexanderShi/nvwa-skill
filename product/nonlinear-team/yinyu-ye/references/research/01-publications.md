# Yinyu Ye: Signature Works and the Publication Landscape

| Field | Value |
|---|---|
| Researcher | Yinyu Ye (叶荫宇). K.T. Li Professor of Engineering (Emeritus), Stanford MS&E and ICME; since 2024 Distinguished Professor, Antai School of Management, Shanghai Jiao Tong University, plus fractional visiting posts at SIMIS, CUHK-Shenzhen and HKUST (CV, updated Oct 2025). PhD Stanford 1988 (Engineering-Economic Systems), advisor Edison Tse |
| Dimension | Research agent 01 of 06: signature works and the publication landscape (nuwa research-craft, Phase 1) |
| Research date | 2026-09-28 |
| Sources consulted | 34 in total (25 primary, 7 secondary, 2 that failed: Google Scholar and Semantic Scholar). All are listed under "Sources". About 95 distinct identifiers (77 DOIs, 18 arXiv ids), each checked in this run through Crossref, DBLP, OpenAlex or arXiv |
| WebSearch calls | 1 (of 2 allowed) |
| User-supplied material | none. `references/sources/{papers,talks,essays,software}/` held only `.gitkeep`; `private/` was not opened |
| Raw landscape files | `references/sources/publications/publications.md` and `abstracts.md` (OpenAlex, written by `scripts/fetch_publications.py` in this run). DBLP JSON and the extracted slide texts stay in scratch (`/tmp/nonlinear-team-scratch/base-skills/yinyu-ye/`) |

**Evidence tags.** [stated] means Ye said or wrote it about his own work (CV, homepage, slides, prefaces, interviews, the prose of his papers). [practice] means what the papers, software and records show he did. [observed] means a third party reported it (journalists, prize committees, other authors, bibliographic databases). [inferred] means my reading, with the basis given. (P) marks a primary source and (S) a secondary one. Numbers such as [S12] point to the "Sources" list at the end.

**Reading depth.** I read these in full or nearly in full: the CV (23 pp.), the homepage and its sub-pages, the front matter and Preface of *Interior Point Algorithms* (PostScript on his site), the 12-page preprint of the 2011 MDP paper, three short notes on his site (2015, 2017, 2026), and the text of nine slide decks (2021–2026). For every other paper I read only the abstract (OpenAlex or arXiv), the arXiv metadata and comments, or the bibliographic record. I read no proofs. **Not read: the full texts of the 1991 potential-reduction paper, the 1994 HSD paper, the 2004/2007 sensor-network papers, and the DRSOM/HSODM papers** (for these I used abstracts plus Ye's own slides about them).

**Slide quotations.** Most slide PDFs lose the spaces between words when their text is extracted. In quotations from [S9]–[S15] I restored the word spacing and changed nothing else; "(sic)" marks spelling that is Ye's own.

---

## 0. A caveat on authorship order

- [practice] (P, computed from DBLP [S23]) "Ye" sorts last in almost any alphabetical list, so the OpenAlex count of "last-author" papers (e.g. 87 of 107 in 2020–2024, `publications.md`) cannot on its own show a move from doing the work to supervising it. Among DBLP's journal and conference records with more than one author, the share in alphabetical order is 9/15 for 1990–94, 21/24 for 1995–99, 19/23 for 2000–04, 24/32 for 2005–09, 19/32 for 2010–14, 13/22 for 2015–19, 23/35 for 2020–24 and 7/20 for 2025–26.
- [practice] (P) The informative signal lies in the **non-alphabetical** papers:
  - *Ye first, before 1995 (he led):* Ye & Kojima 1987 (MP, 10.1007/BF02592079); Ye & Tse 1989 (MP, 10.1007/BF01587086, his advisor second); Ye, Güler, Tapia & Zhang 1993, "A quadratically convergent O(√nL)-iteration algorithm for linear programming", MP 59 (10.1007/BF01581242); Ye, Kortanek, Kaliski & Huang 1993 (MP, 10.1007/BF01581269); Ye, Todd & Mizuno 1994 (MOR, 10.1287/moor.19.1.53). After 2004 DBLP shows no paper with Ye as first author.
  - *Solo papers:* 12 in 1990–94, 8 in 1995–99, 1 in 2000–04, 7 in 2005–09 (e.g. the Arrow–Debreu paper, MP 2008, 10.1007/s10107-006-0065-5, and the MDP paper, MOR 2005, 10.1287/moor.1050.0149), 1 in 2010–14 (the MDP paper, MOR 2011, 10.1287/moor.1110.0516), and none after 2014.
  - *Student-first and Ye-last, from about 2015:* e.g. Zhang, Ge, He, Jiang, Jiang, Xue & Ye (HSODM, MOR 2026, 10.1287/moor.2023.0132); He, Jiang, Zhang, Ge, Jiang & Ye (MP 2026, 10.1007/s10107-025-02230-3). In 2025–26, 13 of the 20 multi-author records are not alphabetical.
- [inferred] The real shift is from **solo and first-author theory (1987–1999)** to **team papers with students first (after about 2010)**. Team size grows alongside: the mean number of authors per DBLP record is 1.9 in 1990–94, 2.8 in 2000–04, 3.6 in 2015–24 and 5.5 in 2025–26.

---

## 1. Publication landscape

### 1.1 Size and sources (the numbers disagree; I keep them as they are)

| Source | Count | Notes |
|---|---|---|
| CV, updated Oct 2025 [S2] (P) | journal papers J1–J207; conference papers and chapters C1–C95; working papers W1–W16; 3 books (the 1997 monograph; *Linear and Nonlinear Programming* with Luenberger, 3rd ed. 2008 and 5th ed. 2022) | The self-listing, taken as authoritative. Numbering includes some duplicates (e.g. J181/J187 and J180/J185 are the online and print versions of the same papers) |
| DBLP pid 42/1372-1 [S23] (S), SPARQL, 2026-09-28 | 330 records, 1987–2026 (177 Article, 84 Informal, 55 Inproceedings, 9 Reference, 3 Editorship, 1 Book, 1 Incollection); 268 with DOI, 83 with arXiv id; ORCID 0009-0001-3239-2622; alias 叶荫宇 | **Coverage before 1990 is thin**: 2 DBLP records against at least 7 CV entries for 1987–1989 |
| OpenAlex A5041526408 [S24] (S) | 504 works; 28,530 citations; h = 72; i10 = 232 | The profile it chose lists Shenzhen University and HKUST as affiliations and includes 2025–26 medical-imaging papers (breast ultrasound, low-dose bone reconstruction). CV C82 (MICCAI 2022, with Dong Ni et al.) confirms at least one medical-imaging co-authorship, so these may be genuine; **not resolved**. The 50 papers "with Luenberger" are editions and chapters of one textbook, counted separately |
| Google Scholar BgOXDogAAAAJ (the ID is linked from his homepage) | **not read** | WebFetch was redirected to Google's CAPTCHA page (`/sorry/`) |
| Semantic Scholar | **not read** | HTTP 429 (rate limit), twice |

### 1.2 Topics by five-year period

Main sources: the CV [S2] and DBLP [S23], with topics labeled by me. Every example paper was checked by DOI or arXiv id.

| Period | Setting | Main topics | Example papers (identifier checked) |
|---|---|---|---|
| 1982–1989 | Stanford EES PhD student (1983–88), research scientist at Integrated Systems Inc. (1987–88), visiting PhD student of Todd at Cornell (1987) | Karmarkar's projective method: recovering dual and basic solutions, and extension to convex QP; ball-constrained ("trust region") QP inside interior methods | Ye & Kojima 1987, MP 39 (10.1007/BF02592079); Ye & Tse 1989, MP 44 (10.1007/BF01587086); Ye 1989, "An Extension of Karmarkar's Algorithm and the Trust Region Method for Quadratic Programming", *Progress in Mathematical Programming* (Springer), 10.1007/978-1-4613-9617-8_3 |
| 1990–1994 | Assistant, then associate professor, Univ. of Iowa; mostly solo or 2–3 authors | Potential-reduction IPMs; primal-dual predictor-corrector; quadratic and finite convergence; column generation; LCP; nonconvex QP by affine scaling; HSD | Ye 1990, SIAM J. Comput. (10.1137/0219030); Ye 1991, MP 50, "An O(n³L) potential reduction algorithm for linear programming" (10.1007/BF01594937); Kojima, Megiddo & Ye 1992 (10.1007/BF01586054); Ye 1992, "On affine scaling algorithms for nonconvex quadratic programming", MP 56 (10.1007/BF01580903); Ye 1992, SIOPT 2 (10.1137/0802002); Mizuno, Todd & Ye 1993, MOR 18 (10.1287/moor.18.4.964); Ye, Todd & Mizuno 1994, MOR 19 (10.1287/moor.19.1.53) |
| 1995–1999 | Professor at Iowa; visiting student Erling Andersen; the monograph (1997) | Condition-number complexity (Vavasis–Ye); implementing HSD; homogeneous monotone CP; infeasibility detection; cutting planes; lower bounds; first SDP relaxations | Vavasis & Ye 1996, MP 74 (10.1007/BF02592148); Xu, Hung & Ye 1996, Ann. OR (10.1007/BF02206815); Todd & Ye 1996, Ann. OR, "A lower bound on the number of iterations of long-step primal-dual linear programming algorithms" (10.1007/bf02206818); Andersen & Ye 1998, COA 10 (10.1023/A:1018369223322); Ye 1998, MP 80, "On the complexity of approximating a KKT point of quadratic programming" (10.1007/BF01581726); Nesterov, Todd & Ye 1999, MP 84 (10.1007/s10107980009a); Andersen & Ye 1999, MP 84 (10.1007/s101070050027); Ye 1999, MP 84 (10.1007/s10107980012a); *Interior Point Algorithms* (Wiley 1997, 10.1002/9781118032701) |
| 2000–2004 | Iowa, then Stanford (from April 2002) | SDP relaxations and approximation algorithms (Max-Bisection, graph partition, QP); facility location; the DSDP solver; sensor-network localization begins | Benson, Ye & Zhang 2000, SIOPT (10.1137/S1052623497328008); Ye 2001, MP, ".699-approximation algorithm for Max-Bisection" (10.1007/pl00011415); Ye & Zhang 2003, SIOPT (10.1137/S105262340139001X); Tseng & Ye 2002, MP (10.1007/s10107-002-0310-5); Biswas & Ye 2004, IPSN (10.1145/984622.984630) |
| 2005–2009 | Stanford; large cohort of PhD students (So, Biswas, Ge, Carlsson, Delage, Agrawal …) | SDP theory for sensor-network localization and rigidity; market equilibria (Arrow–Debreu, Leontief) and algorithmic game theory (WINE, SODA); DRO; parimutuel markets; DSDP5; disciplined convex programming (CVX) | So & Ye 2007, MP 109 (10.1007/s10107-006-0040-1); Ye 2005, MOR (10.1287/moor.1050.0149); Ye 2008, MP 111 (10.1007/s10107-006-0065-5); Grant, Boyd & Ye 2006 (10.1007/0-387-30528-9_7); Benson & Ye 2008, ACM TOMS (10.1145/1356052.1356057); Delage & Ye 2010, OR 58 (10.1287/opre.1090.0741; CV lists it as 2009) |
| 2010–2014 | Stanford | Strong polynomiality of simplex and policy iteration for MDPs; online LP; Lp-sparse nonconvex complexity; statistical ranking via Hodge theory; applications (radiation therapy, reservoirs, power grids) | Ye 2011, MOR 36 (10.1287/moor.1110.0516); Ge, Jiang & Ye 2011, MP 129 (10.1007/s10107-011-0470-2); Jiang, Lim, Yao & Ye 2011, MP 127 (10.1007/s10107-010-0419-x); Agrawal, Wang & Ye 2014, OR 62 (10.1287/opre.2014.1289); Post & Ye 2015, MOR (10.1287/moor.2014.0699) |
| 2015–2019 | Stanford; students Hinder, Sun (postdoc), Li; ML venues appear | Negative and positive results on multi-block ADMM and coordinate descent; nonconvex IPMs (Hinder); MDP sample complexity; nonsmooth IPM complexity | Chen, He, Ye & Yuan 2016, MP 155 (10.1007/s10107-014-0826-5); Bian, Chen & Ye 2015, MP 149 (10.1007/s10107-014-0753-5); Haeser, Liu & Ye 2019, MP (10.1007/s10107-018-1290-4); Hinder & Ye, arXiv 1801.03072 (one-phase IPM); Sidford, Wang, Wu, Yang & Ye, "Near-Optimal Time and Sample Complexities for Solving Markov Decision Processes with a Generative Model", NeurIPS 2018 (DBLP record; CV C68) |
| 2020–2024 | Stanford, then SJTU and CUHK-SZ; team at SUFE and the COPT solver company | Second-order methods in low dimension (DRSOM, HSODM); ADMM-based IPM (ABIP); first-order LP on GPU (cuPDLP-C); SDP software (HDSDP); derivative-free SOLNP+; preconditioning; crossover; online LP and Fisher markets; MDP sample complexity | Zhang et al. arXiv 2208.00208 (DRSOM); arXiv 2211.08212 (HSODM); Qu, Gao, Hinder, Ye & Zhou, OR 2025 (10.1287/opre.2022.0592); Lu et al. arXiv 2312.14832 (cuPDLP-C); Gao, Ge & Ye, ACM TOMS 2025 (10.1145/3721123); Ge et al., ACM TOMS 2024 (10.1145/3699956); Hinder & Ye, MOR 49 2024 (10.1287/moor.2020.0274) |
| 2025–2026 | SJTU/SIMIS/HKUST; teams of about 5–6 authors | GPU solvers (D-PDLP, PDHCG, PDCS, low-rank SDP); trust-region theory; interior-point market equilibrium; LLM-serving scheduling as online LP; LLM agents for OR modeling | Jiang et al., JSC 2026 (10.1007/s10915-025-03154-y; arXiv 2311.11489); arXiv 2511.00680; Huang et al., IJOC 2025 (10.1287/ijoc.2024.0983); Li et al. arXiv 2601.07628; Su et al. arXiv 2604.24488; Chen, Ye & Zhou arXiv 2607.03948; Zhou et al. arXiv 2605.28158 |

- [stated] (P) The homepage [S1] names his own "Research Interests/Selected-Work" in five groups: (i) LP and mathematical programming (the predictor-corrector IPM, the HSD algorithm, convex relaxation of nonconvex problems); (ii) algorithm design and analysis (Hodge ranking, sample complexity of generative MDPs, an LP IPM whose running time depends only on A); (iii) OR models (DRO, online LP, disciplined convex programming and the early CVX); (iv) complexity and algorithmic game theory (simplex and policy iteration, multi-block ADMM, linear market equilibria); (v) optimization solvers on GPU (cuPDLP-C, low-rank SDP, PDHCG). Each item links to a paper, so this is his own choice of signature works.

### 1.3 Collaboration network and students

- [stated] (P) The CV lists 28 PhD advisees, with dates and last known positions [S2]: Kaliski 1992, Bosch 1994 (co-advised), Huang 1995, **Erling Andersen 1996 (visiting; "Founder of MOSEK.com")**, Qian 1997 (co-advised), **Steve Benson 1999** (DSDP), **Jiawei Zhang 2004**, **Anthony So 2007**, **Pratik Biswas 2007**, Mark Peters 2008, **Dongdong Ge 2009**, John Carlsson 2009, **Erick Delage 2009**, Zhisu Zhu 2010, **Shipra Agrawal 2011**, **Zizhuo Wang 2012**, Qi Qi 2012, Nicole Taheri 2012, Yichuan Ding 2013 (co-advised), Robert Eberhart 2013 (co-advised), Onkar Dalal 2013 (co-advised), Tiago Akle 2014 (co-advised), Andy Nguyen 2014 (co-advised), Tailai Wen 2014, **Ian Post 2015**, Davood Shamsi 2016, Zhisu Zhu 2017 (listed a second time), Ron Estrin 2018 (co-advised), **Oliver Hinder 2019**, Carry Wu 2019, **Xiaocheng Li 2020**, Guanting Chen 2022 (co-advised), Mingxi Zhu 2023 (co-advised), **Chunlin Sun 2024**. Postdocs: Dachuan Xu 2006, Roger Behling 2014, **Ruoyu Sun 2017**. Bold names co-author at least one paper cited in this file.
- [stated] (P) Mentors: Dantzig, Luenberger and Todd, as he names them in the 2020 profile [S21]. The 1988 thesis committee was "Sam Chiu, George Dantzig, David Luenberger, Edison Tse (Advisor)" [S2].
- [practice] (P) The most frequent DBLP co-authors [S23] are Dongdong Ge 37, Jiawei Zhang 27, Wenzhi Gao 21, Anthony Man-Cho So 20, Zizhuo Wang 17, Chunlin Sun 11, Shipra Agrawal 10, Chuwen Zhang 10, Michael J. Todd 9, Chuangyin Dang 9, Peter W. Glynn 9, Mengdi Wang 9, Xiaocheng Li 9, Madeleine Udell 9 and Oliver Hinder 6. By period:
  - *1987–2001, the IPM circle:* Todd, Mizuno, Kojima, Megiddo, Güler, Tapia, Y. Zhang, Anstreicher, Potra, Vavasis, Z.-Q. Luo, Nesterov, Andersen.
  - *2000–2012, SDP, approximation and markets:* J. Zhang, So, Benson, Biswas, Saberi, Vazirani, Boyd, Toh.
  - *2019–2026, solvers and second-order methods:* the Shanghai group (D. Ge, Chuwen Zhang, Bo Jiang, Yuntian Jiang, Chang He, Chenyu Xue, Qi Deng), the Stanford and ICME group (W. Gao, Y.-C. Chu, Udell, Hinder), and the GPU team (Hongpei Li, Yicheng Huang, Huikang Liu).
- [inferred] Wenzhi Gao (21 records, 2022–26) and Chuwen Zhang (10) are probably students or junior members of his groups, but **neither appears in the CV advisee list, which ends with Chunlin Sun in 2024**. Their status is not verified.
- [stated] (P) Industry ties, all from the CV [S2]: "Chairman of the technical advisory board of MOSEK (2009-)"; "AT&T (1992-1993), Linear Programming Solver Development"; Huawei 2005–2010; Polaris Wireless 2006–07 ("Mobile Phone Localization"); JD.com 2015–; and others. The homepage says: "I have led the Optimization Solver COPT development" [S1]. The 2026 slides say: "2019 Our team released the professional solver COPT" [S15].

### 1.4 Venues

- [practice] (P, DBLP by period [S23]) In the 1990s the venues were Mathematical Programming, MOR, SIOPT and Annals of OR. In 2005–2009 theoretical-CS venues were added: WINE (7 records), SODA and SIAM J. Comput. From 2010 Operations Research becomes prominent, and from 2018 NeurIPS, ICML and AAAI. In 2024–26 there are software papers in ACM TOMS (DSDP5 2008, SOLNP+ 2024, HDSDP 2025) and solver papers in INFORMS J. Computing. Over the whole career the biggest venues are Math. Program. (51), CoRR (83), MOR (19), SIOPT (14) and Oper. Res. (14).
- [inferred] The venue mix follows the audience of each application area, while the theoretical core stays in Math. Program. and MOR in every decade.

### 1.5 Most-cited works (OpenAlex 2026-09-28; for relative comparison only [S24])

| # | Work | Identifier | OpenAlex cites | Ye's position |
|---|---|---|---|---|
| 1 | Luo, Ma, So, Ye & Zhang, "Semidefinite Relaxation of Quadratic Optimization Problems", IEEE Signal Processing Magazine 27(3) 2010 | 10.1109/MSP.2010.936019 | 3,777 | middle (tutorial); 2015 IEEE SPS Signal Processing Magazine Best Paper Award (CV) |
| 2 | Luenberger & Ye, *Linear and Nonlinear Programming*, 3rd ed. 2008 | 10.1007/978-0-387-74503-9 | 2,827 | textbook co-author (the 4th and 5th editions are counted separately: 669 and 703) |
| 3 | Delage & Ye, "Distributionally Robust Optimization Under Moment Uncertainty …", OR 58 2010 | 10.1287/opre.1090.0741 | 1,979 | advisor; won the 2008 Nicholson first prize for Delage (CV) |
| 4 | Grant, Boyd & Ye, "Disciplined Convex Programming", 2006 | 10.1007/0-387-30528-9_7 | 1,033 | third author |
| 5 | Ye, *Interior Point Algorithms: Theory and Analysis*, Wiley 1997 | 10.1002/9781118032701 | 963 | sole author |
| 6 | Chen, He, Ye & Yuan, "The direct extension of ADMM for multi-block convex minimization problems is not necessarily convergent", MP 155 2016 | 10.1007/s10107-014-0826-5 | 774 | alphabetical |
| 7 | Biswas & Ye, "Semidefinite programming for ad hoc wireless sensor network localization", IPSN 2004 | 10.1145/984622.984630 | 572 | advisor |
| 8 | Biswas, Liang, Wang & Ye, ACM TOSN 2(2) 2006 | 10.1145/1149283.1149286 | 546 | advisor |
| 9 | Mizuno, Todd & Ye, "On Adaptive-Step Primal-Dual Interior-Point Algorithms for LP", MOR 18 1993 | 10.1287/moor.18.4.964 | 393 | alphabetical |
| 10 | Ye, Todd & Mizuno, "An O(√nL)-Iteration Homogeneous and Self-Dual LP Algorithm", MOR 19 1994 | 10.1287/moor.19.1.53 | 371 | first (not alphabetical) |
| 11 | So & Ye, "Theory of semidefinite programming for Sensor Network Localization", MP 109 | 10.1007/s10107-006-0040-1 | 333 | advisor |
| 12 | Ye, "An O(n³L) potential reduction algorithm for linear programming", MP 50 1991 | 10.1007/BF01594937 | 292 | solo |
| 13 | Ye, "The Simplex and Policy-Iteration Methods Are Strongly Polynomial for the MDP with a Fixed Discount Rate", MOR 36 2011 | 10.1287/moor.1110.0516 | 165 | solo; 2014 SIAM Optimization Prize |

- [observed] (S) Prizes, from the CV and bio [S2][S3]: INFORMS Farkas Prize 2006 (inaugural); INFORMS John von Neumann Theory Prize 2009 ("Co-Recipient"; **the co-recipient's name was not verified in this run**, since the INFORMS page returned "PAGE NOT FOUND"); inaugural ISMP Tseng Lectureship 2012; SIAM Optimization Prize 2014; Constantin Carathéodory Prize 2025. The 2014 SIAM prize was for the 2011 MDP paper, according to Stanford MS&E news [S22] and the WebSearch summary [S28]. The SIAM prize page itself returned HTTP 403.

### 1.6 Recent works (about the last 12 months, each verified on arXiv or by DOI)

- Jiang, He, Zhang, Ge, Jiang & Ye, "Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses", J. Sci. Comput. 106 (2026), 10.1007/s10915-025-03154-y. arXiv 2311.11489, v1 20 Nov 2023, v4 23 Jan 2026. The homepage lists v1 as "A Universal Trust-Region Method for Convex and Nonconvex Optimization" [S5].
- Jiang, Zhang, Jiang & Ye, "Accelerating Trust-Region Methods: An Attempt to Balance Global and Local Efficiency", arXiv 2511.00680 (1 Nov 2025).
- Zhang, He, Jiang, Xue, Jiang, Ge & Ye, "A Homogeneous Second-Order Descent Method for Nonconvex Optimization", MOR 51(2) 2026, 10.1287/moor.2023.0132 (arXiv 2211.08212, seven versions from Nov 2022 to Jun 2026).
- He, Jiang, Zhang, Ge, Jiang & Ye, "Homogeneous second-order descent framework: a fast alternative to Newton-type methods", Math. Program. 2026, 10.1007/s10107-025-02230-3 (arXiv 2306.17516).
- Su, Zhang, Huang, Li & Ye, "Scalable First-Order Interior Point Trust Region Algorithms for Linearly Constrained Optimization", arXiv 2604.24488 (27 Apr 2026).
- Huang, Zhang, Li, Ge, Liu & Ye, "A Restarted Primal-Dual Hybrid Conjugate Gradient Method for Large-Scale Quadratic Programming", INFORMS J. Comput. (Nov 2025), 10.1287/ijoc.2024.0983.
- Li, Huang, Liu, Ge & Ye, "D-PDLP: Scaling PDLP to Distributed Multi-GPU Systems", arXiv 2601.07628 (v3 May 2026; DBLP has an earlier title, "Beyond Single-GPU: …"). Li et al., "GPU-Accelerated Conic Quadratic Programming with Local Linear Convergence under Strict Complementarity", arXiv 2608.09159 (Aug 2026).
- Zhang, He, Jiang & Ye, "The Second-Order Tâtonnement: Decentralized Interior-Point Methods for Market Equilibrium", arXiv 2508.04822. DBLP records the title "The Implicit Barrier of Utility Maximization: An Interior-Point Approach for Market Equilibria".
- Gao, Qu, Udell & Ye, "Scalable approximate optimal diagonal preconditioning", Comput. Optim. Appl. 2026, 10.1007/s10589-026-00770-8. Chu, Gao, Ye & Udell, "Gradient Methods with Online Scaling Part II. Practical Aspects", arXiv 2509.11007.
- LLM-era work: Chen, Ye & Zhou, "Online Linear Programming for Multi-Objective Routing in LLM Serving", arXiv 2607.03948; Zhou et al., "OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents", arXiv 2605.28158.
- A note on his site, "Can Pure Offline Data Learning Replace Linear Programming Algorithms?" (dated September 23, 2026) [S20]. It constructs a 2-variable, 1-constraint covering LP whose data points lie arbitrarily close together yet have different optimal bases, and concludes: "Therefore, the pure offline learning from data, basic on data similarity, is unlikely to accurately predict its optimal basis" (sic). [stated]

### 1.7 Software as a publication channel

- [practice] (P) The Computational Optimization Laboratory page [S6] lists public codes: COPL_LP (interior-point LP; MPS input; options "to return an optimal basic solution and to detect infeasibility or unboundedness"; DOS/HP/Linux, 1998–2000), COPL_QP, COPL_LC (Fortran; linearly constrained convex), COPL_GP (geometric programming), COPL_SDP and COPL_DSDP (dual-scaling SDP with rank reduction, 1999), DSDP 5.8 (C; 2009/2014), and Matlab suites for sensor-network localization. The SNL codes note that they "all need to use SDP solver Sedumi in order to run".
- [practice] (P) Later solver papers: DSDP5 (ACM TOMS 2008, 10.1145/1356052.1356057), SOLNP+ (ACM TOMS 2024, 10.1145/3699956), HDSDP (ACM TOMS 2025, 10.1145/3721123), the COPT user guide (arXiv 2208.14314), cuPDLP-C (arXiv 2312.14832), and the low-rank SDP GPU paper (arXiv 2407.15049). The homepage links Mittelmann's benchmark pages as the scoreboard ("with performances" → plato.asu.edu/bench.html) [S1].
- [stated] (P) The book's companion page [S7] distributes the COPL solvers with the 1997 monograph, and Chapter 10 of the book is "Implementation Issues" (presolver, normal equations versus augmented system, HSD method, optimal-basis identifier) [S8, Contents].

### 1.8 Era and resource context

| Era | Context of the practice | Evidence |
|---|---|---|
| 1984–1988 | Graduate student at Stanford right after Karmarkar (1984). The work is pencil-and-paper complexity, with one advisor and 1–2 co-authors. Industry job at Integrated Systems Inc. in "Optimization Software Development" (1987–88) | [S2][S8] |
| 1988–2002 (Iowa) | Small department (Management Sciences), mostly solo work, NSF grants, a few PhD students. Codes in C and Fortran for DOS/HP/Linux, tested on Netlib-style MPS problems. Visits to Cornell, Rice, Delft, MSRI | [S2][S6][S8 Preface grants] |
| 2002–2024 (Stanford) | Large PhD cohorts (about 25 advisees). Cross-disciplinary applications (wireless, markets, radiation therapy, energy). Industry projects (Boeing, Huawei, Polaris Wireless). Matlab codes on top of SeDuMi | [S2][S6] |
| 2017–2026 (Shanghai and Stanford, COPT) | A solver company plus university groups; releases of LEAVES (2017) and COPT (2019) are mentioned in [S15]. GPU hardware: cuPDLP-C solved zib03 in "1.7 hours on NVIDIA A6000" and "27 minutes on NVIDIA H100", and in 2026 "247 Seconds on Nvidia 8 H100s" [S15 slide 14]. Teams of 5–11 authors; ML venues | [S15][S23] |

---

## 2. Signature works (dissected per framework §5)

I chose these five because they combine what is most cited, what Ye himself selects on his homepage [S1], and the turning points of his career. The two most-cited research articles on OR modeling (DRO 2010 and online LP 2014) are listed in §1.5 but not dissected here, because they matter less for NLP-solver craft. For a later run they are a known gap.

### SW1. The potential-reduction line: Ye & Tse 1989 → Ye 1991, "An O(n³L) potential reduction algorithm for linear programming", Math. Program. 50:239–258 (10.1007/BF01594937)

Companion papers: Ye & Tse, "An extension of Karmarkar's projective algorithm for convex quadratic programming", MP 44:157–179, 1989 (10.1007/BF01587086); Ye, "An Extension of Karmarkar's Algorithm and the Trust Region Method for Quadratic Programming", 1989 (10.1007/978-1-4613-9617-8_3); Kojima, Megiddo & Ye 1992 (LCP, 10.1007/BF01586054); Ye 1992, column generation (10.1137/0802002); Ye 1992, nonconvex QP by affine scaling (10.1007/BF01580903).

- **Origin.**
  - [stated] (P) In the Preface of the 1997 monograph (p. xiii) he writes about the 1984 Karmarkar seminar: "I was not particular enthusiastic about the statement from the speaker that a new interior-point method would be 40 times faster than the simplex method, but I was amazed by the richness and applicability of linear programming as a whole." [S8]. The 2020 profile gives the same event: "I quickly decided to devote my PhD to this branch of mathematics." [S21]
  - [practice] (P) The PhD thesis (1988) was titled "Interior Algorithms for Linear, Quadratic and Linearly Constrained Convex Programming" [S2].
  - [inferred] The 1989 QP papers come from the thesis: their titles match it and the second author of one is his advisor.
- **Why then.** [inferred] Karmarkar's 1984 potential function was the one analysis tool everyone had. The open problems of 1986–1990 were to lower the iteration bound from O(nL) toward O(√nL), to obtain primal-dual (symmetric) versions, and to extend the method beyond LP. In his 2023 bootcamp slides Ye presents Karmarkar's primal potential as giving "n iteration complexity" and the "Tanabe-Todd-Ye primal-dual potential function" as giving "√n iteration complexity" [S10, slides 27–28].
- **Key insight.** [stated retrospectively, 2023] (P) One potential function drives everything: reducing it by a constant per step bounds the duality gap. When the primal step can no longer reduce it by a constant, a dual update must be able to: "if by updating primal only one cannot reduce the potential function by a constant anymore, then one must be able to update the dual … and reduce the potential function by a constant; see Y 1989" [S10, slide 30]. On the same slide he notes that this result "was the first one extended to solving SDP by Alizadeh 1992" [S10]. **Full text of the 1991 paper not read.**
- **Minimum evidence.** [inferred] A per-iteration constant-reduction lemma for the potential; the slides call it "the" argument. The first calculation that convinced him is not documented.
- **Abandoned paths.** [inferred, from the publication record] Karmarkar's *projective* framework ("A Class of Projective Transformations for LP", SIAM J. Comput. 1990, 10.1137/0219030; Todd & Ye, "A Centered Projective Algorithm for LP", MOR 1990, 10.1287/moor.15.3.508) and the "build-down"/"build-up" column-elimination schemes (CV J7 1990; W3, a Dantzig–Ye SOL report, 1990) disappear from his titles after 1991. Affine and primal-dual potential formulations replace them. No primary statement explains the switch.
- **Reception.**
  - [observed] (S) OpenAlex counts 292 citations for the 1991 paper [S24]. He wrote the Encyclopedia of Optimization entry "Potential Reduction Methods for Linear Programming" (2009, 10.1007/978-0-387-74759-0_515).
  - [practice] (P) The idea keeps coming back. A 2015 note, "On a First-Order Potential Reduction Algorithm for Linear Programming", is footnoted "This was a teaching note for course MS&E310, Linear Optimization" and says "no matrix needs to be ever inversed so that it is a pure first-order method" [S18]. In 2022–23 the potential function returns to his talks: minimizing the (nonconvex) potential with DRSOM using negative curvature [S12, slides 38–39], and a first-order potential-reduction "presolver" that switches to second order at 1e-2, reporting "An average reduction of 30% iterations compared to trivial start" [S14, slide 11].
- **Method it shows.** M2 (one merit function instead of tuned neighborhoods), M3 (a ball-constrained subproblem as the primitive), M7 (teaching notes as an incubator).

### SW2. Ye, Todd & Mizuno 1994, "An O(√nL)-Iteration Homogeneous and Self-Dual Linear Programming Algorithm", MOR 19(1):53–67 (10.1287/moor.19.1.53)

- **Origin.**
  - [practice] (P) Contemporary work: Mizuno, Todd & Ye, "A Surface of Analytic Centers and Primal-Dual Infeasible-Interior-Point Algorithms for LP", MOR 1995 (10.1287/moor.20.1.135). Ye was a visiting scientist at Cornell ORIE (Todd's department) from 08/93 to 12/93 [S2].
  - [stated retrospectively, 2023] (P) Ye frames HSD as the answer to *initialization*. He lists the options it replaced: combining primal and dual into one feasibility problem, "The bigM method", "Phase I-then-Phase II method", and "Combined Phase I-Phase II method", whose "best" complexity he gives as O(n log(R/ε)) [S10, slide 35].
  - **No first-hand origin story was found.** Whether it was inspired by the Goldman–Tucker homogeneous system was **not verified in this run**.
- **Why then.** [inferred] By the early 1990s, primal-dual IPMs worked in practice from infeasible starts, but the theory with the best bounds assumed a known interior feasible point. The gap between theory and practice was the opening.
- **Key insight.** [stated] (P, abstract [S27]) Embed the primal, the dual and both infeasibility alternatives in a single homogeneous self-dual system, so that "It solves the linear programming problem without any regularity assumption concerning the existence of optimal, feasible, or interior feasible solutions" and "it does not use any big M penalty parameter or lower bound". The slides state the structural fact that makes this work: the system is always feasible, every feasible solution is self-complementary, and a strictly self-complementary solution exists; τ>0 means solvable and κ>0 means infeasible [S10, slides 38–39].
- **Minimum evidence.** [inferred] The self-complementarity theorem on slide 39 of [S10] carries the whole method. Which result convinced him first is not documented.
- **Abandoned or simplified paths.** [practice] (P) The 1994 formulation was followed within two years by "A generalized homogeneous and self-dual algorithm for LP" (Xu & Ye, ORL 17 1995, 10.1016/0167-6377(95)00002-2) and "A simplified homogeneous and self-dual LP algorithm and its implementation" (Xu, Hung & Ye, Ann. OR 62 1996, 10.1007/BF02206815). [inferred] The original version was reworked to make it implementable. **What was dropped: not read.**
- **Reception.**
  - [observed] (S) OpenAlex counts 371 citations. [practice] (P) Andersen & Ye, "A Computational Study of the Homogeneous Algorithm for Large-scale Convex Optimization", COA 10 1998 (10.1023/A:1018369223322). Andersen & Ye, "On a homogeneous algorithm for the monotone complementarity problem", MP 84 1999 (10.1007/s101070050027).
  - [observed] (S) Andersen & Andersen, "The Mosek Interior Point Optimizer for Linear Programming: An Implementation of the Homogeneous Algorithm" (2000, 10.1007/978-1-4757-3216-0_8) [S29]. O'Donoghue, Chu, Parikh & Boyd, "Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding", JOTA 169 2016 (10.1007/s10957-016-0892-3) [S30].
  - [practice] (P) Ye's own later extensions: to LCP (MP 76 1997, 10.1007/BF02614384); warm-starting HSD (Skajaa, Andersen & Ye, MPC 5 2013, 10.1007/s12532-012-0046-z); nonsymmetric cones (Skajaa & Ye, MP 150 2015, 10.1007/s10107-014-0773-1).
  - [stated] (P) The homepage claims the predictor-corrector IPM and HSD "are implementaed in all Linear Programming Commercial Solvers" (sic) [S1]. See Contradiction C2.
- **Method it shows.** M1 (homogenize or embed to remove regularity assumptions and get certificates), M4 (complexity first, then implementation papers and a solver partner). The homogenization idea comes back in 2022 in HSODM (SW5).

### SW3. Semidefinite programming for sensor-network localization: Biswas & Ye 2004 (IPSN, 10.1145/984622.984630; IEEE copy 10.1109/IPSN.2004.1307322) → So & Ye, "Theory of semidefinite programming for Sensor Network Localization", MP 109:367–384, 2007 (10.1007/s10107-006-0040-1; SODA 2005)

- **Origin.**
  - [practice] (P) SDP was already his tool before this work: the DSDP and COPL_SDP solvers [S6]; Benson, Ye & Zhang 2000 (10.1137/S1052623497328008); the .699 Max-Bisection paper (10.1007/pl00011415); approximating QP with quadratic constraints (10.1007/s10107980012a).
  - [stated] (P) The CV records "2004 BASES Innovators' Challenge First-Place Winners: Pratik Biswas and Yinyu Ye on sensor network localization", a Stanford patent "A Semi-Definite Programming Method for AD HOC Network Node Localization, 2005", and an industry project with Polaris Wireless (2006–07, "Mobile Phone Localization") [S2].
  - **No first-hand account of how the problem was chosen was found.**
- **Why then.** [inferred] Ad hoc wireless sensor networks were a young field (IPSN 2004 was the "3rd international symposium", according to its Crossref container title), SDP solvers had matured, and he had just moved to Stanford (2002), where EE collaborators were close.
- **Key insight.** [stated] (P, SODA 2005 abstract [S27]) "We use SDP duality and interior-point algorithm theories to prove that the SDP localizes any network or graph that has unique sensor positions to fit given distancemeasures. Therefore, we show, for the first time, that these networks can be localized in polynomial time." The same abstract introduces "strong localizability" and ties the question to graph rigidity.
- **Minimum evidence.** [practice] (P) The empirical paper came first (IPSN 2004): "Very few anchor nodes are required to accurately estimate the position of all the unknown nodes in a network" (abstract [S27]). The exactness theory followed in 2005–07. [inferred] Numerical success preceded the theory.
- **Abandoned paths and evolution.** [practice] (P) The full SDP proved too expensive, so a series of reductions followed:
  - distributed SDP (Biswas, Toh & Ye, SISC 30(3) 2008, 10.1137/05062754X);
  - adaptive subproblems in SpaseLoc (Carter, Jin, Saunders & Ye, SIOPT 2006, 10.1137/040621600);
  - weaker edge-based relaxations (Wang, Zheng, Ye & Boyd, SIOPT 2008, 10.1137/060669395);
  - "Full SDP with Objective Regularization and gradient refinement" (code on [S6]);
  - universal rigidity (Zhu, So & Ye, SIOPT 2010, 10.1137/090772009);
  - finally, abandoning the convex relaxation: "Beyond convex relaxation: A polynomial-time non-convex optimization approach to network localization" (Ji, Sze, Zhou, So & Ye, INFOCOM 2013, 10.1109/INFCOM.2013.6567056).
  - By 2022, SNL is a nonlinear least-squares *test problem* for DRSOM, with the SDP used only for initialization: "Graphical results using SDP relaxation (Biswas et al. 2004) to initialize the NLS" and then "DRSOM can still converge to optimal solutions … without SDP relaxation initialization" [S12, slides 23–24]. Tang, Toh, Xiao & Ye, SISC 2024 (10.1137/23M1567229).
- **Reception.** [observed] (S) OpenAlex counts 572 citations for the IPSN paper and 546 for the TOSN paper. The 2010 tutorial on SDR won the IEEE SPS Magazine Best Paper Award in 2015 [S2].
- **Method it shows.** M6 (carry a proven tool into a new application domain), M8 (relax, then scale down, then refine nonconvexly).

### SW4. Ye 2011, "The Simplex and Policy-Iteration Methods Are Strongly Polynomial for the Markov Decision Problem with a Fixed Discount Rate", MOR 36(4):593–603 (10.1287/moor.1110.0516)

- **Origin.**
  - [observed/stated] (S, with a paraphrase by the writer) "Professor Ye said that he developed his personal interest in this field while working with Professor Ben Van Roy and Professor Emeritus Arthur Veinott at Stanford." [S22]
  - [stated] (S, quoted) "There was a significant gap between theoretical research and practical application," said Professor Ye. "It bothered me." [S22]
  - [practice] (P) His own earlier step was a strongly polynomial *interior-point* algorithm for discounted MDPs (Ye 2005, MOR 30, 10.1287/moor.1050.0149). The 2011 preprint sets the classic methods against that benchmark [S17].
- **Why then.** [stated] (P) The preprint frames the question with a run of negative results: Klee–Minty 1972, Melekopoglou–Condon 1994 (smallest-index rule exponential even with a fixed discount), and, "Most recently, Fearnley (2010)", policy iteration exponential for undiscounted MDPs [S17, pp. 4–5]. [inferred] His 2005 IPM bound gave him a target the simplex method could be measured against.
- **Key insight.** [stated] (P) Dantzig's original most-negative-reduced-cost rule makes the simplex method, and hence Howard's policy iteration, strongly polynomial for a fixed discount, with at most m²(k−1)/(1−γ)·log(m²/(1−γ)) iterations; "The result seems surprising, given the earlier negative results" [S17, p. 5]. The structural fact used is that every basic feasible solution of the DMDP LP has bounded entries (between 1 and m/(1−γ); [S17, §5]). **Lemmas 3.2, 4.1 and 4.2 not read in detail.**
- **Minimum evidence.** [inferred] The bounded-basic-variable property (Lemma 3.1) is the first step that makes a strongly polynomial count possible. The order of discovery is not documented.
- **Abandoned paths and open questions he kept.** [stated] (P) "one cannot rule out the simplex method simply because the behavior of one pivoting rule on one problem is shown to be exponential" [S17, p. 11]. He leaves open whether policy iteration or simplex is polynomial when the discount rate is an input [S17, p. 5].
- **Reception and review.**
  - [practice] (P) The preprint header reads: "Initial submission date: May 15, 2010; first revision Nov. 30, 2010; second revision August 16, 2011." The acknowledgments thank "Pete Veinott and five anonymous referees for many insightful discussions and suggestions on this subject, which have greatly improved the presentation of the paper." [S17]
  - [observed] (S) The paper won the 2014 SIAM Optimization Prize [S22][S28]. Follow-ups: Post & Ye, deterministic MDPs regardless of discount (SODA 2013, 10.1137/1.9781611973105.105; MOR 2015, 10.1287/moor.2014.0699; Ian Post received a 2013 Nicholson second prize [S2]); Scherrer, "Improved and Generalized Upper Bounds on the Complexity of Policy Iteration", MOR 41 2016 (10.1287/moor.2015.0753). OpenAlex counts 165 citations.
- **Method it shows.** M5 (settle a long-open question about a method practitioners already trust), and the strongly polynomial, condition-free thread shared with Vavasis & Ye 1996 (10.1007/BF02592148).

### SW5. Second-order methods in reduced dimension (2022–2026): DRSOM (arXiv 2208.00208) → HSODM (MOR 2026, 10.1287/moor.2023.0132; arXiv 2211.08212) → universal trust region (JSC 2026, 10.1007/s10915-025-03154-y). Companion line on nonconvex IPMs with Hinder (2017–2024)

- **Origin.**
  - [stated] (P, Lehigh ISE seminar, 1 Nov 2022 [S12])
    - Motivation, in the slide's own words: "Motivation: using few directions in SOM", under the heading "Motivation from multi-directional FOM" (slide 11).
    - His verdict on the competing Hessian negative-curvature hybrids of Carmon et al. and Agarwal et al.: "They are hybrid and/or randomized methods and seem difficult to be implemented", followed by "Our approach: Reduce dimension in SOM" (slide 9).
  - [stated] (P) He places the work in a line going back to his own early results. Under the slide title "Early Complexity Analyses for Nonconvex Optimization" he cites the ball-constrained nonconvex QP ("Y (1989,93)") and nonconvex QP with polyhedral constraints ("Interior-Trust-Region method Y (1998)") [S12, slide 4; S13, slide 2].
- **Why then.** [stated] (P) Hessian-vector products are cheap with automatic differentiation: "Analytic approach to fit modern automatic differentiation" and "Computing Hessian-Vector Product in DRSOM is the Key" [S12, slide 15]. The complexity target O(ε^{-3/2}) had already been set by Nesterov–Polyak, Cartis–Gould–Toint and Curtis–Robinson–Samadi, whom he cites on slide 7 of [S12]. [practice] (P) He had a team at SUFE/CUHK-SZ, cited on the slides as "Zhang at al. SHUFE" (sic).
- **Key insight.**
  - [stated] (P) DRSOM: restrict the trust-region model to span{−g_k, d_k}, with d_k = x_k − x_{k−1} the momentum, and solve a 2×2 trust-region problem to "decide 'two step-sizes'" [S12, slide 13]. The arXiv abstract adds that it keeps "the convergence of the second-order method while using only curvature information in a few directions".
  - [stated] (P) HSODM: homogenize the quadratic model and step along the leftmost eigenvector of the gradient–Hessian matrix. The MOR abstract says it is "motivated from the homogenization trick in quadratic programming", and the slides make the link explicit: "The Homogenization Trick was Also Successful in LP", pointing to HSD [S12, slides 43–44].
  - [stated] Takeaway in the 2023 talk: "Homogeneous second-order direction as an extreme eigenvalue computation is a 'cheaper' alternative to the Trust-Region or Newton step computation" [S13, slide 26], supported by "GHM-Lanczos (eigenvalue) is immune to ill-conditioning" [S13, slide 24].
- **Minimum evidence.** [stated] (P) For convex QP the 2-D method terminates in n steps, and on a CUTEst example it is compared with GD and L-BFGS (Hager–Zhang line search) [S12, slides 14 and 19]. HSODM is benchmarked on CUTEst against Newton-TR and ARC with performance profiles and shifted geometric means [S13, slide 10].
- **Abandoned paths and repairs.**
  - [stated] (P) The first DRSOM analysis needed "Assumption (c)", a Cartis-et-al.-type bound on how well the subspace Hessian approximates the full one [S12, slide 18]. The next step was posed as "Big Question: How to drop Assumption (c) in DRSOM analyses?" with the answer "Use the homogenized quadratic model!" [S12, slide 41]; in the arXiv abstract the answer is a periodic "corrector step using a Krylov-like method".
  - [practice] (P) The DRSOM arXiv v3 (Jul 2023) comment reads "Considerable changes in the main text", and the title lost "and Preliminary Analyses". **No journal version of DRSOM was found** in DBLP or Crossref (2026-09-28). This is not evidence of rejection. The universal-TR paper was renamed between versions (see §1.6).
  - [stated] (P) Deep learning was tried and its limits recorded: "DRSOM may overfit the models", "Needs 4~5x time than Adam to run same number of epoch", yet "Good potential to be a standard optimizer for deep learning!" [S12, slide 26].
- **Companion line: IPMs for nonconvex constraints (Hinder & Ye).** These papers bear directly on NLP solvers.
  - [practice] (P) "A one-phase interior point method for nonconvex optimization" (arXiv 1801.03072) starts from a negative claim: "The work of Wachter and Biegler suggests that infeasible-start interior point methods (IPMs) developed for linear programming cannot be adapted to nonlinear optimization without significant modification". It answers by moving the LP idea over, "we reduce primal feasibility at the same rate as the barrier parameter". It reports on CUTEst: "fails on only 9% of the problems compared with 16% for IPOPT". **No journal version found.**
  - [practice] (P) Haeser, Hinder & Ye, MP 186 2021 (10.1007/s10107-019-01454-4; arXiv 1707.07327): "we show that IPOPT, an algorithm that does not carefully control primal feasibility has practical issues with the dual multipliers values growing to unnecessarily large values."
  - [practice] (P) Hinder & Ye, "Worst-Case Iteration Bounds for Log Barrier Methods on Problems with Nonconvex Constraints", MOR 49(4) 2024 (10.1287/moor.2020.0274). The arXiv version (1807.00404) went through five versions from 2018 to 2023, and its first title was "A polynomial time log barrier method for problems with nonconvex constraints" (DBLP). The acceptance comment reads: "several results were removed from the previous version most notably the results on convex case. These results were removed due to reviewer suggestions to focus the paper on the most significant contributions."
- **Reception.** [observed] (S) Too recent to judge. HSODM and its framework appeared in MOR and MP in 2026, and the universal TR in JSC 2026. DRSOM was a spotlight at a NeurIPS 2022 workshop (CV C80). OpenAlex counts for the arXiv records (DRSOM 2, one-phase IPM 10) are unreliable because arXiv records are split.
- **Method it shows.** M3 (the trust-region or ball-constrained subproblem as the primitive), M1 (homogenization reused 28 years later), M4 (benchmark on CUTEst against named public solvers), M9 (move an LP-IPM principle into NLP and test it against IPOPT).

---

## 3. Cross-cutting research moves visible in the publication record (candidates for Phase 2)

Each move is tagged and backed by at least two works. None is yet validated by the four checks in framework §三.

- **M1. Homogenize or embed the problem to remove regularity assumptions and obtain certificates.** [practice] HSD 1994 (10.1287/moor.19.1.53) → LCP 1997 (10.1007/BF02614384) → monotone CP 1999 (10.1007/s101070050027) → nonsymmetric cones 2015 (10.1007/s10107-014-0773-1) → HSD embedding as the model behind DR potential reduction (2022, [S12] slide 38) → HSODM 2026 (10.1287/moor.2023.0132). [stated] "The Homogenization Trick was Also Successful in LP" [S12, slide 44].
- **M2. Prefer one merit or potential function over tuned neighborhoods.** [stated, 2023] "Typically, a single merit-function driven algorithm is preferred since it can adaptively take large step sizes as long as the merit value is sufficiently reduced, comparing to check and balance of hyper-parameters/measures of the path-following type of algorithms." [S10, slide 28]. Potential reduction is described as "implemented as a neighborhood-tuning-free method comparing with the path-following methods" [S14, slide 4]. [practice] 1991 (10.1007/BF01594937); 2015 note [S18]; 2023 first-order and second-order potential reduction [S14]; the "novel descent property" of the universal TR (arXiv 2311.11489). See Contradiction C6.
- **M3. Treat the ball-constrained quadratic (trust-region) subproblem as the computational primitive.** [practice] 1989 (10.1007/978-1-4613-9617-8_3); 1991/92 sphere-constrained QP (10.1515/9781400862528.19); 1992 nonconvex affine scaling (10.1007/BF01580903); 1998 KKT approximation (10.1007/BF01581726); Hinder–Ye 2024, which counts trust-region subproblem solves (10.1287/moor.2020.0274); DRSOM's 2-D trust region; HSODM's eigenvector reformulation of the TR step; interior-point trust region at scale (arXiv 2604.24488).
- **M4. Complexity first, then an implementation paper, then a solver and a public benchmark.** [practice] HSD 1994 → the implementation paper of 1996 → the computational study of 1998 → MOSEK (2000, [S29]); DSDP → ACM TOMS 2008; COPT and cuPDLP-C on Mittelmann's benchmarks [S1][S15]; DRSOM/HSODM on CUTEst [S12][S13]. [stated] "The innovation of efficient optimization methods/algorithms should be driven by scientific/theoretical research, besides software engineering and coding" [S9, slide 61].
- **M5. Settle a long-open question about a method practitioners already trust, or refute one, with a sharp construction.** [practice] The MDP simplex result of 2011 (positive); the multi-block ADMM counterexample (10.1007/s10107-014-0826-5, negative); hardness of Lp minimization (10.1007/s10107-011-0470-2); the lower bound on long-step IPM iterations (10.1007/bf02206818); the 2026 two-variable LP note against purely learned basis prediction [S20]. [stated] The homepage says of these: "where we settled long-time open questions" [S1].
- **M6. Carry a proven tool into a new application domain.** [practice] SDP → sensor localization (SW3); LP duality and prices → online LP and revenue management (10.1287/opre.2014.1289); IPMs → market equilibria (10.1007/s10107-006-0065-5; arXiv 2508.04822); IPMs → Wasserstein barycenters (Ge, Wang, Xiong & Ye, "Interior-Point Methods Strike Back: Solving the Wasserstein Barycenter Problem", NeurIPS 2019, DBLP record); DRSOM → RL and deep learning [S12].
- **M7. Teaching notes as an idea incubator.** [stated] The 2015 potential-reduction note is "a teaching note for course MS&E310" [S18]. The 2017 path-following note gives "more details of the minimal-norm path following algorithm … described in the lecture note of CME307 and MS&E311" [S19]. The fixed-radius TR complexity is credited to "the lecture notes by Y since 2005" [S13, slide 3]. **The lecture notes themselves were not read.**
- **M8. Relax, then scale down, then refine nonconvexly.** [practice] The SNL sequence in SW3. Also, in LP: first-order to low accuracy, then second-order, then crossover, with the observation "In general, interior point solutions tell more valueble information for crossover" (sic) [S14, slide 10]; Smart Crossover, IJOC 2025 (10.1287/ijoc.2022.0291).
- **M9. Move an LP-IPM principle into nonlinear programming and test it against the incumbent NLP solver.** [practice] The one-phase IPM and the Lagrange-multiplier paper, both benchmarked against or critical of IPOPT (SW5 companion); Nesterov, Todd & Ye 1999, infeasibility detectors for nonlinear programming (10.1007/s10107980009a).

### Solver-relevant threads for the Nonlinear Team (pointers only; content not evaluated)

These are factual pointers for later synthesis, [practice]: infeasibility certificates from homogeneous embeddings (SW2); moving primal feasibility at the rate of μ, with bounded multipliers (10.1007/s10107-019-01454-4; arXiv 1801.03072); log-barrier complexity with trust-region subproblems (10.1287/moor.2020.0274); warm-starting HSD (10.1007/s12532-012-0046-z); optimal diagonal preconditioning (10.1287/opre.2022.0592; 10.1007/s10589-026-00770-8); eigenvalue-based second-order steps (HSODM); 2-D subspace trust regions (DRSOM); crossover (10.1287/ijoc.2022.0291); first-order presolve before an IPM [S14]; ADMM-based IPM (ABIP, 10.1287/ijoc.2023.0017); derivative-free SOLNP+ (10.1145/3699956).

---

## 4. Failures, corrections, abandoned and unfinished directions

- [practice] (P) The projective-transformation and build-down lines ended around 1990–91 (SW1). No statement explains why.
- [practice] (P) Hinder–Ye removed its convex-case results at the request of reviewers; they "still appear in the first author's PhD thesis (Principled Algorithms for Finding Local Minima)" (arXiv 1807.00404 comment). The paper took about six years from arXiv (2018) to print (2024).
- [practice] (P) A published erratum: "Correction to: Exact semidefinite formulations for a class of (random and non-random) nonconvex quadratic programs", Burer & Ye, MP 2021 (10.1007/s10107-021-01684-5), correcting MP 2020 (10.1007/s10107-019-01367-2). **The content of the correction was not read.**
- [practice] (P) DRSOM (2022) and the one-phase IPM (2018) have no journal version in DBLP or Crossref as of 2026-09-28. The reason is unknown and this is not evidence of rejection.
- [stated] (P) Recorded weaknesses of his own methods: DRSOM on ResNet18 was slower per epoch than Adam and "may overfit" [S12, slide 26]. His DR potential-reduction model was self-critiqued on a slide: "The homogeneous QP seems so restrictive!" [S12, slide 38].
- [stated] (P) Limits of GPU methods, as he states them in 2026: "First-order algorithms suffer from low precision; numerically difficult problems converge slowly and unstably" and "Second-order algorithms involve matrix inversion/factorization, for which parallel acceleration on GPU yields limited improvement" [S15, slide 8].
- [practice] (P) Questions left open on purpose: discount-rate-as-input MDP complexity [S17]; the ongoing work listed on the 2023 HSODM takeaway slide, "Ongoing: HSODM for IPMs, non-smooth optimization." [S13, slide 26]. **No follow-up paper on HSODM for IPMs was found.**
- **No rejected papers or retracted claims were found** in public records.

---

## Contradictions (kept, not reconciled)

- **C1. Who was his advisor?** The CV says "Edison Tse (Advisor)", with Dantzig on the committee [S2]. The 2020 Stanford Engineering profile calls him "A student of George Dantzig" (journalist's framing), while Ye in the same piece says "My first mentor was George Dantzig" and "George was a great advisor" [S21].
- **C2. Where HSD and the predictor-corrector method are implemented.** The homepage says "implemented in all Linear Programming Commercial Solvers" [S1]. The 2020 profile says an algorithm written with Todd "is widely implemented in current open-source linear programming problem-solving software" [S21]. The two claims differ (commercial versus open-source, "all" versus "widely"), and the profile does not say which algorithm it means.
- **C3. How old are the lecture notes on fixed-radius trust-region complexity?** The DRSOM slides of Nov 2022 say "see the lecture notes by Y since 20??" [S12, slide 7]. The HSODM slides of Aug 2023 say "since 2005" [S13, slide 3]. The notes were not checked.
- **C4. Bibliographic variants.**
  - The sphere-constrained QP chapter is dated 1991 by Crossref (10.1515/9781400862528.19) but 1992 by the CV (C6).
  - The Todd–Ye lower-bound paper has the Crossref title "... long-step primal-dual linear programming algorithms", while the CV gives "... long-step and polynomial interior-point linear programming algorithms".
  - The Delage–Ye DRO paper appears as 2010 (Crossref, DBLP) and as 2009 (CV J120).
  - So–Ye appears as 2006 (OpenAlex) and as 2007 (Crossref, print).
  - Hinder–Ye appears as 2023 (OpenAlex, online) and as 2024 (print).
  - arXiv 2508.04822 has two titles: the DBLP title and the current arXiv title.
- **C5. How big and whose is the body of work?** The 2020 profile says "more than 170 peer-reviewed papers" [S21]; the CV numbers journal papers up to J207 by 2025 (a date difference, plus duplicates). OpenAlex counts 504 works on a profile whose affiliations (Shenzhen University) and medical-imaging papers are not fully confirmed as this Yinyu Ye; CV C82 supports at least one of them.
- **C6. Preferred algorithm style.** In 2023 he states a preference for "a single merit-function driven algorithm" over the "check and balance of hyper-parameters/measures of the path-following type of algorithms" [S10]. Yet the first signature work named on his homepage is the predictor-corrector *path-following* IPM (Mizuno–Todd–Ye 1993) [S1]. He keeps both; the tension is recorded here, not resolved.

---

## Gaps

- **Google Scholar** (BgOXDogAAAAJ) was blocked by a CAPTCHA and **Semantic Scholar** returned HTTP 429, so this file has no Scholar citation counts. OpenAlex numbers are used for relative comparison only.
- **No first-hand origin account for HSD (1994) or for the sensor-network project (2004).** The link between HSD and the Goldman–Tucker homogeneous system was not verified. The full text of the 1994 MOR paper, whose introduction may say more, was not read.
- **The full text of the 1991 potential-reduction paper was not read.** The attribution of the primal-dual potential ("Tanabe-Todd-Ye") rests only on Ye's 2023 slides.
- **DRO (2010) and online LP (2014)**, the two most-cited research articles, are not dissected.
- **Talk videos and transcripts.** One Stanford Zoom recording (LP solver progress, Feb 2024) is linked from [S4] but was not watched, and no transcript was saved to `sources/talks/`. The LP-progress slides (2024) are mostly images, so their text could not be extracted.
- **Prize citations.** The SIAM prize page returned HTTP 403 and the INFORMS von Neumann page returned 404. The 2014 prize paper is confirmed only by secondary sources ([S22], [S28]). The 2009 co-recipient was not verified.
- **Students.** The advisee status of recent frequent co-authors (Wenzhi Gao, Chuwen Zhang, Yuntian Jiang, Chang He) was not verified.
- **Coverage.** DBLP is incomplete for 1987–1989. The CV was used for those years, but only the entries re-checked through Crossref or DBLP are cited with identifiers.
- **Review history.** No referee reports, rebuttals or rejected submissions are public. OpenReview entries for the ML-venue papers (e.g. openreview.net/forum?id=AM1UcqDDDv) were not opened.
- **Lecture notes** for MS&E310, MS&E311 and CME307, cited by Ye as the origin of several ideas, were not read.

---

## Sources

- [S1] Yinyu Ye, homepage (index), https://web.stanford.edu/~yyye/, fetched 2026-09-28. Primary.
- [S2] Yinyu Ye, Curriculum Vitae ("Updated October, 2025"), https://web.stanford.edu/~yyye/cvYYYE25.pdf. Primary.
- [S3] Yinyu Ye, "VeryShortbio2025", https://web.stanford.edu/~yyye/VeryShortbio2025.pdf. Primary.
- [S4] Yinyu Ye, Talks page, https://web.stanford.edu/~yyye/talks.html. Primary.
- [S5] Yinyu Ye, Recent Papers page, https://web.stanford.edu/~yyye/newpapers.html. Primary.
- [S6] Computational Optimization Laboratory software page (Ye, director), https://web.stanford.edu/~yyye/Col.html. Primary.
- [S7] Book page for *Interior-Point Algorithms: Theory and Analysis*, https://web.stanford.edu/~yyye/book.html. Primary.
- [S8] Yinyu Ye, *Interior-Point Algorithm: Theory and Analysis*, front matter, Contents and Preface (PostScript "June 1996, Revised January 1997"), https://web.stanford.edu/~yyye/main.ps; published by Wiley 1997, 10.1002/9781118032701. Primary.
- [S9] Yinyu Ye, "From 0.618 to Mathematical Optimization", slides (listed June 2021), https://web.stanford.edu/~yyye/618Slides.pdf. Primary.
- [S10] Yinyu Ye, "Bootcamp: Interior Point Algorithms I", Simons Institute, 1 Sep 2023, https://web.stanford.edu/~yyye/BootcampIPM1.pdf. Primary.
- [S11] B. Natura, T. Tsuchiya, Y. Ye, "Bootcamp: Interior Point Methods II", Simons Institute, 1 Sep 2023, https://web.stanford.edu/~yyye/BootcampIPM2.pdf. Primary (co-authored).
- [S12] Yinyu Ye, "Dimension-Reduced Second-Order Steepest Descent Methods for Optimization", ISE Seminar, Lehigh, 1 Nov 2022, https://web.stanford.edu/~yyye/DRSOM-221101-v1.pdf. Primary.
- [S13] Yinyu Ye, "An Alternative to the Trust-Region: Homogeneous Second-Order Descent Framework", WOEC Hong Kong, 18 Aug 2023, https://web.stanford.edu/~yyye/hsodm-230818.pdf. Primary.
- [S14] Yinyu Ye, "Fast Potential Reduction for LP and its Applications", SIAM OP23, 31 May 2023, https://web.stanford.edu/~yyye/pot-mip-20230531-v2.pdf. Primary.
- [S15] Yinyu Ye, "Mathematical Programming in the Era of AI", HORIZONS 2026, VinUni, 2 Jul 2026, https://web.stanford.edu/~yyye/20260701Solver.pdf. Primary.
- [S16] Yinyu Ye, "Mathematical Optimization in the Era of AI", INFORMS International 2025 plenary, 20 Jul 2025, https://web.stanford.edu/~yyye/MPinEraofAI20250720.pdf. Primary (skimmed).
- [S17] Yinyu Ye, "The Simplex and Policy-Iteration Methods are Strongly Polynomial for the Markov Decision Problem with a Fixed Discount Rate", preprint (12 pp.), https://web.stanford.edu/~yyye/SimplexMDP4.pdf; published MOR 36(4) 2011, 10.1287/moor.1110.0516. Primary.
- [S18] Yinyu Ye, "On a First-Order Potential Reduction Algorithm for Linear Programming", note dated July 30, 2015, https://web.stanford.edu/~yyye/FO-potential-reduction.pdf. Primary.
- [S19] Yinyu Ye, "A Second-Order Path-Following Algorithm for Unconstrained Convex Optimization", note dated May 31, 2017, https://web.stanford.edu/~yyye/min-norm-path0.pdf. Primary.
- [S20] Yinyu Ye, "Can Pure Offline Data Learning Replace Linear Programming Algorithms?", note dated September 23, 2026, https://web.stanford.edu/~yyye/LPsolutionsensitivity.pdf. Primary.
- [S21] Edmund L. Andrews (writer), "Yinyu Ye: Sports led me from the rice fields to Stanford", Stanford School of Engineering, 8 Dec 2020, https://engineering.stanford.edu/news/yinyu-ye-sports-led-me-rice-fields-stanford. A first-person as-told-to piece: primary for Ye's statements, secondary for the framing.
- [S22] Rachel Street, Theresa Lina Stevens, "Professor Yinyu Ye Awarded Optimization Prize: Proves Efficiency of Popular Markov Decision Process Algorithms", Stanford MS&E news, 29 Jan 2015, https://msande.stanford.edu/news/professor-yinyu-ye-awarded-optimization-prize-proves-efficiency-popular-markov-decision. Secondary (contains quotes).
- [S23] DBLP, person 42/1372-1 (Yinyu Ye), queried through sparql.dblp.org by `scripts/dblp_works.py`, 2026-09-28, https://dblp.org/pid/42/1372-1.html. Secondary (bibliographic).
- [S24] OpenAlex author A5041526408, via `scripts/fetch_publications.py`, 2026-09-28; output in `references/sources/publications/publications.md`. Secondary (bibliographic).
- [S25] Crossref REST API, work records for each DOI cited above, api.crossref.org, 2026-09-28. Secondary (bibliographic).
- [S26] arXiv abstract pages (metadata, version history, comments): 2208.00208, 2211.08212, 2306.17516, 2311.11489, 2511.00680, 1807.00404, 1707.07327, 1801.03072, 2312.14832, 2407.15049, 2508.04822, 2604.24488, 2608.09159, 2605.28158, 2601.07628, https://arxiv.org/abs/<id>. Primary (the authors' own abstracts and comments).
- [S27] Abstracts retrieved through the OpenAlex works API: Ye, Todd & Mizuno 1994 (10.1287/moor.19.1.53); Biswas & Ye 2004 (10.1145/984622.984630); So & Ye SODA 2005 (OpenAlex record with DOI 10.5555/1070432.1070488); Agrawal, Wang & Ye 2014 (10.1287/opre.2014.1289); Hinder & Ye 2024 (10.1287/moor.2020.0274); Zhang et al. 2026 (10.1287/moor.2023.0132); Smart Crossover (10.1287/ijoc.2022.0291); Optimal Diagonal Preconditioning (10.1287/opre.2022.0592). Primary text, secondary retrieval.
- [S28] WebSearch, 2026-09-28, query on the 2014 SIAG/OPT prize for Yinyu Ye. It returned [S22] and the MOR article page. Secondary.
- [S29] E. D. Andersen, K. D. Andersen, "The Mosek Interior Point Optimizer for Linear Programming: An Implementation of the Homogeneous Algorithm", in *High Performance Optimization* (Applied Optimization, Springer), 2000, 10.1007/978-1-4757-3216-0_8. Secondary (observed reception; title and record only).
- [S30] B. O'Donoghue, E. Chu, N. Parikh, S. Boyd, "Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding", JOTA 169 (2016) 1042–1068, 10.1007/s10957-016-0892-3. Secondary (observed reception; title and record only).
- [S31] Google Scholar profile BgOXDogAAAAJ (linked from [S1]). Attempted; **not read** (CAPTCHA).
- [S32] Semantic Scholar Graph API author search. Attempted; **not read** (HTTP 429).
- [S33] Yinyu Ye, "Recent Developments of Online Linear Programming" (Tsuchiya 60th, Nov 2021) and "Online Linear Programming: Applications and Extensions" (ISMP 2022 plenary), https://web.stanford.edu/~yyye/Tsuchiya60.pdf and https://web.stanford.edu/~yyye/ISMP2022.pdf. Primary (skimmed only).
- [S34] Yinyu Ye, "Recent Computational Progress on Linear Programming Solvers", Stanford LA/OPT, 14 Feb 2024, https://web.stanford.edu/~yyye/LPProgress-slides.pdf. Primary (mostly image-based; little text extracted).
