# Roger Fletcher · 01 Publications: signature works and the publication landscape

- **Researcher**: Roger Fletcher FRS FRSE (29 January 1939 – 15 July 2016), University of Dundee (earlier University of Leeds and AERE Harwell). Deceased: historical lens; every "practice" item below is a record, nothing is current behaviour.
- **Dimension**: nuwa research-craft Phase 1, agent 01 (signature works + publication landscape).
- **Research date**: 2026-09-28.
- **Sources consulted**: 24: 5 primary texts by Fletcher or co-authored by him (Sources 1–5), 3 bibliographic databases (DBLP, OpenAlex, Crossref; Sources 6–8) and 16 secondary sources (9–24, including the two web-search locators). Listed under "Sources".
- **Local corpus**: `references/sources/papers|talks|essays|software` held only `.gitkeep` files. No user-supplied material, so nothing here is marked "from user-supplied material".
- **Tags**: [stated] = Fletcher said it · [practice] = what his papers, reports and codes show · [observed] = what others wrote about him · [inferred] = my inference, no primary source. Each item is also marked primary or secondary.
- **Verification**: every paper below carries a DOI checked against Crossref and/or OpenAlex in this run, or a venue + year + full title read in a tool-fetched document (in that case the document is named). Citation counts are OpenAlex counts on 2026-09-28 ("OA n"). Use them for relative comparison only. There is no Google Scholar profile for Fletcher.
- **Quotations**: verbatim. PDF-extraction artifacts (split words such as "Y ou", ligatures) were repaired, and nothing else was changed. Page numbers refer to the printed page of the cited document.

---

## 1. Publication landscape

### 1.1 Data sources and their defects (read before using any count)

- **DBLP** splits Fletcher over two profiles. pid **34/2426** ("Roger Fletcher", 28 records, 1972–2014) and pid **06/4216** ("R. Fletcher", 10 records, 1963–1993: DFP, Fletcher–Reeves, BFGS, the 1965 derivative-free review, the 1983 "Penalty Functions" tutorial, the 1993 QP degeneracy paper). Both are the same person, going by co-authors (Reeves, Powell) and topics. A later harvest must merge them. [practice, primary bibliographic record]
- **OpenAlex** author A5088683774: 114 works, 26,617 citations, h-index 48. Known defects:
  - "Function minimization by conjugate gradients" (1964) is recorded as a *solo* paper. DBLP (pid 06/4216) and Fletcher's own account (Optima 99, p. 2) give **R. Fletcher and C. M. Reeves**. Crossref's author field has the same error.
  - The 3,619 citations credited to "Practical Methods of Optimization." (1989, *Mathematics of Computation*, "Christoph Witzgall; Roger Fletcher", DOI 10.2307/2008742) belong to a **book review** record that absorbed citations of the book. The book's own record (2nd ed., 1987) shows 963. The book's true citation count is split and cannot be read from OpenAlex.
  - It contains records that look misattributed or are out of field: an IEEE audio paper (1973), an EAGE geophysics abstract (2006), two ankle-biomechanics items (2002, 2006; the 2006 one has Al-Homidan, a Fletcher co-author, so it may be genuine). I left them out of the topic counts.
- **The author-position heuristic does not apply.** The `fetch_publications.py` first/last-author table assumes that author order carries meaning. In Fletcher's papers the order is almost always alphabetical: Fletcher–Leyffer, Dai–Fletcher, Chin–Fletcher, Al-Baali–Fletcher, Fletcher–Gould–Leyffer–Toint–Wächter. The only non-alphabetical items I found are Norgett & Fletcher (1970), Sinclair & Fletcher (1974), Holt & Fletcher (1979), Womersley & Fletcher (1986) and Shen, Leyffer & Fletcher (2012). So there is no measurable "first-author to last-author shift". The informative signal is the **solo vs co-authored share** (below). [inferred from the author lists]

### 1.2 Output by five-year period (OpenAlex, cleaned: book reviews, book-chapter duplicates of the 2000 reprint and doubtful records removed; the 1964 paper corrected to two authors)

| Period | Works | Solo | Co-authored | Main topics (from titles; [practice]) | Life stage / setting |
|---|---|---|---|---|---|
| 1960–64 | 3 | 0 | 3 | molecular-integral formula generation with automatic differentiation (Fletcher & Reeves 1963); **DFP** (1963); **Fletcher–Reeves nonlinear CG** (1964) | PhD at Leeds 1960–63 (Ferranti Pegasus computer), then lecturer at Leeds |
| 1965–69 | 6 | 4 | 2 | review of derivative-free minimization with a proposed test set (1965); iterative eigenproblem methods (Bradbury & Fletcher 1966); CACM algorithm certification (1966); generalized-inverse least squares for nonlinear equations (1968); orthogonalization (1969) | Leeds, then AERE Harwell (exact years not verified) |
| 1970–74 | 14 | 6 | 8 | **BFGS** (1970); "a class of methods for nonlinear programming" (1970, Abadie volume; part II with Lill), which I take to be the exact augmented Lagrangian [inferred]; general QP (1971); modified Marquardt code (1971); L_p approximation (Grant, Hebden); physics applications (crystal defects with Norgett, SCF wave functions, saddle points with Sinclair); LDLᵀ modification (with Powell, 1974); bound-constrained QP (Jackson 1974); exact penalty with inequalities (1973) | Harwell Theoretical Physics Division, then Dundee |
| 1975–79 | 7 | 5 | 2 | "ideal" penalty function (1975); **bi-CG for indefinite systems** (1976); symmetric indefinite factorization (1976); modified Newton (Freeman 1977); constrained nonlinear least squares (Holt 1979) | Dundee |
| 1980–84 | 14 | 5 | 9 | *Practical Methods of Optimization* vol. 1 (1980) and vol. 2 (1981); nonsmooth optimality conditions (Watson 1980); exact L1 penalty experiments (1981); **second-order corrections** (1982); composite NDO model algorithm (1982); educational-testing NLP (an early SDP) (1981); state-of-the-art tutorial "Penalty Functions" (1983); stable explicit LU updates (Matthews 1984) | Dundee |
| 1985–89 | 11 | 5 | 6 | semidefinite matrix constraints (1985); expected conditioning (1985); **Sl1QP** (1985); composite nonsmooth algorithm (Womersley 1986); nonlinear least squares (Al-Baali, Xu); cancellation errors in quasi-Newton methods (1986); 2nd edition of the book (1987); degeneracy with round-off (1988); **SLP-EQP** (Sainz de la Maza 1989) | Professor of Optimization, Dundee, from 1984 |
| 1990–94 | 6 | 3 | 3 | low-storage methods (1990; by his own 2009 account it already discussed Barzilai–Borwein, see §2.5); variational result for quasi-Newton formulae (1991); batch-plant retrofit design (Hall, Johns 1991); QP degeneracy (1993); sparse ordering (Hall 1993); **MINLP outer approximation** (Leyffer 1994); overview of unconstrained optimization (1994) | Baxter Professor from 1993 |
| 1995–99 | 9 | 2 | 7 | optimal sparse positive-definite update (1995); nearest Euclidean distance matrix (Al-Homidan); null-space KKT stability (Johnson 1997); MIQP branch-and-bound bounds (Leyffer 1998); LP degeneracy (1998); **filter method**: plenary talk May 1996, report NA/171 Sept 1997, filterSQP manual NA/181 April 1998 | Dundee |
| 2000–04 | 8 | 0 | 8 | reduced-Hessian indefinite QP (2000); distillation-column initialisation (Morton 2000); the three **filter convergence papers** (2002); SLP-filter with EQP steps (Chin 2003); filter for equations and inequalities (2003); MPCCs as NLPs (Leyffer 2004) | Dundee, emeritus from 2005 |
| 2005–09 | 6 | 1 | 5 | **Barzilai–Borwein** analysis with Y.-H. Dai (three papers, 2005) and his own BB chapter (2005); low-rank quasi-Newton scheme for NLP (2005/06); SQP for MPECs (Leyffer, Ralph, Scholtes 2006); brief history of filters (2006); CIME SQP lectures (2007; published 2010); LMSD preprint (2009) | emeritus; preprint issued via Edinburgh ERGO (2009) |
| 2010–14 | 6 | 4 | 2 | SVM training (Acta Numerica 2010, Zanghirati); **LMSD** (2012); nonmonotone filter (Shen, Leyffer 2012); sequential linear constraint programming (2012); Wolfe's degeneracy method (2014) | emeritus, aged 71–75 |
| 2015–17 | 1 | 1 | 0 | augmented Lagrangian for box-constrained QP, up to 10⁸ variables (IMA JNA, published 2 March 2017, after his death) | posthumous |

Totals (cleaned): 91 works, 36 solo. Solo work dominates his most-cited foundations (BFGS, bi-CG, ideal penalty, the book). Co-authored work dominates 1995–2009 (the Leyffer and Dai collaborations). He went back to solo papers at the end (2010–2017). [practice; counts computed from OpenAlex]

The OpenAlex list is **incomplete**. It lacks, for example, the Sl1QP chapter (1985), the 1970 Abadie-volume paper "A class of methods for nonlinear programming with termination and convergence properties" (probably the exact augmented Lagrangian [inferred]), "Low storage methods for unconstrained optimization" (1990) and the Dundee NA report series. The Gould & Hall memoir's reference list (73 entries, readable through Crossref; see Sources) is the fullest bibliography I could reach.

### 1.3 Usual venues

- 1960s–1970: *The Computer Journal* (DFP, FR, BFGS, 1965 review, 1968 and 1971 papers); 8 OpenAlex records. [practice]
- 1970s: *IMA Journal of Applied Mathematics* (general QP 1971, bound QP 1974, ideal penalty 1975, Holt 1979). [practice]
- 1970s–80s: *Lecture Notes in Mathematics* "Numerical Analysis" proceedings (bi-CG 1976; second-order corrections 1982). That these are the Dundee Biennial NA conference volumes is [inferred], not checked. Toint calls Fletcher the "optimization host" of the Dundee conference (Optima 99, p. 6) [observed, secondary].
- 1980s–2010s: *Mathematical Programming* (12 DBLP records) and *SIAM Journal on Optimization* (9 DBLP records, starting with vol. 1 no. 1 in 1991). Also JOTA, IMA JNA and Math. Comp. [practice]
- One review-style article in *Acta Numerica* (2010). Survey chapters in NATO-ASI and CIME lecture volumes (1994, 2010). [practice]
- Reports: Dundee Numerical Analysis Reports (NA/171 1997, NA/181 1998, NA/183, NA/195 1999, NA/199 and NA/203 2001, NA/223 2005), Namur TRs with Toint (98/13, 99/03, 00/15), Argonne preprint ANL/MCS-P1372-0906 (2006), Edinburgh ERGO 09-014 (2009). Report numbers are verified through Crossref reference lists of citing papers and Optimization Online pages. [practice]

### 1.4 Most-cited works (OpenAlex, 2026-09-28)

| # | Work | Identifier | OA cites |
|---|---|---|---|
| 1 | Fletcher & Reeves, "Function minimization by conjugate gradients", *Comput. J.* 7(2):149–154, 1964 | 10.1093/comjnl/7.2.149 | 4,971 |
| 2 | Fletcher & Powell, "A Rapidly Convergent Descent Method for Minimization", *Comput. J.* 6(2):163–168, 1963 | 10.1093/comjnl/6.2.163 | 4,619 |
| 3 | Fletcher, "A new approach to variable metric algorithms", *Comput. J.* 13(3):317–322, 1970 | 10.1093/comjnl/13.3.317 | 4,138 |
| 4 | *Practical Methods of Optimization* (Wiley; 2nd ed. 1987, ISBN 9780471915478; 2000 reprint) | 10.1002/9781118723203 | 963 + 3,619 on a review record (see 1.1); Crossref shows 1,129 for the 2000 DOI |
| 5 | Fletcher & Leyffer, "Nonlinear programming without a penalty function", *Math. Program.* 91(2):239–269, 2002 | 10.1007/s101070100244 | 871 |
| 6 | Fletcher, "Conjugate gradient methods for indefinite systems", LNM "Numerical Analysis", 1976, pp. 73–89 | 10.1007/bfb0080116 | 803 |
| 7 | Fletcher & Leyffer, "Solving mixed integer nonlinear programs by outer approximation", *Math. Program.* 66:327–349, 1994 | 10.1007/BF01581153 | 675 |
| 8 | Dai & Fletcher, "Projected Barzilai-Borwein methods for large-scale box-constrained quadratic programming", *Numer. Math.* 100:21–47, 2005 | 10.1007/s00211-004-0569-y | 361 |
| 9 | Fletcher, Leyffer & Toint, "On the Global Convergence of a Filter--SQP Algorithm", *SIAM J. Optim.* 13(1):44–59, 2002 | 10.1137/S105262340038081X | 331 |
| 10 | Fletcher, Gould, Leyffer, Toint & Wächter, "Global Convergence of a Trust-Region SQP-Filter Algorithm for General Nonlinear Programming", *SIAM J. Optim.* 13(3):635–659, 2002 | 10.1137/S1052623499357258 | 280 |
| 11 | Fletcher, Leyffer, Ralph & Scholtes, "Local Convergence of SQP Methods for Mathematical Programs with Equilibrium Constraints", *SIAM J. Optim.* 17:259–286, 2006 | 10.1137/S1052623402407382 | 270 |
| 12 | Fletcher, "On the Barzilai-Borwein Method", in *Optimization and Control with Applications* (Applied Optimization 96), 2005, pp. 235–256 | 10.1007/0-387-24255-4_10 | 253 |

Long-tail citation behaviour: the 1970 BFGS paper still draws about 110–250 OpenAlex citations a year (2012–2025 series). [practice, bibliometric]

### 1.5 Collaboration network and likely students

- **Leeds (1960s)**: C. M. Reeves (PhD supervisor per the Mathematics Genealogy Project; co-author 1963, 1964, 1965); M. J. D. Powell (DFP 1963; LDLᵀ updates 1974, DOI 10.1090/s0025-5718-1974-0359297-1); W. W. Bradbury (1966); S. A. Lill (1970). [practice]
- **Harwell (about 1969–73; dates [inferred])**: physicists M. J. Norgett (10.1088/0022-3719/3/11/003) and J. E. Sinclair (10.1088/0022-3719/7/5/009); J. A. Grant and M. D. Hebden (L_p approximation, 1971–74). Optimization here was **applied inside a physics division**. [practice + inferred]
- **Dundee PhD students** listed by the Mathematics Genealogy Project (id 52148): R. S. Womersley (1981), M. Al-Baali (1984), C. X. Xu (1987), J. A. J. Hall (1992), S. Leyffer (1994). Each co-authored with him (Womersley 1986, 10.1007/bf00940574; Al-Baali 1985/86/96; Xu 1987, 10.1093/imanum/7.3.371; Hall 1991/93; Leyffer 1994–2012). [practice, secondary record]
- **Other likely Dundee students or postdocs** [inferred, not verified]: E. Sáinz de la Maza (Fletcher calls him "a PhD student", Optima 99 p. 4 [stated]); C. M. Chin; S. Al-Homidan; T. Johnson; A. Grothey; S. P. J. Matthews; W. A. Morton; C. Shen (visitor). Dundee colleagues: G. A. Watson and D. F. Griffiths.
- **Dominant collaborator**: Sven Leyffer, 13 joint works 1994–2012 (MINLP outer approximation, MIQP, filter, MPCC/MPEC, nonmonotone filter). The student-to-peer trajectory runs from Dundee PhD (1994) to Argonne. [practice]
- **International circle**: Ph. L. Toint and N. I. M. Gould (filter convergence theory), A. Wächter (TR-SQP-filter 2002), D. Ralph and S. Scholtes (MPEC), Y.-H. Dai (Barzilai–Borwein, 2005), G. Zanghirati (SVM 2010), D. C. Sorensen (Jordan form, 1983). [practice]
- **Co-author of Powell's Royal Society memoir**: Buhmann, Fletcher, Iserles & Toint, "Michael J. D. Powell. 29 July 1936—19 April 2015", *Biogr. Mems Fell. R. Soc.*, 2018, DOI 10.1098/rsbm.2017.0023 (Crossref-verified; **not read**). [practice]

### 1.6 Recent (last) works

- Fletcher, "A Sequential Linear Constraint Programming Algorithm for NLP", *SIAM J. Optim.* 22(3):772–794, 2012, 10.1137/110844362. The abstract states: "Open source production quality software is available. Results on a large selection of CUTEr test problems are presented and discussed and show that the method is reliable and reasonably efficient." [stated/practice, primary]
- Fletcher, "On Wolfe's Method for Resolving Degeneracy in Linearly Constrained Optimization", *SIAM J. Optim.* 24(3):1122–1137, 2014, 10.1137/130930522. The abstract says: "The simplicity and reliability of the method makes it an excellent choice in this author's opinion." [stated, primary]
- Fletcher, "Augmented Lagrangians, box constrained QP and extensions", *IMA J. Numer. Anal.* 37(4):1635–1656, 2017 (online 2 March 2017, after his death), 10.1093/imanum/drx002. Numerical evidence "on a range of practical problems of up to 10⁸ variables". [practice, primary abstract] This is the "nonnegative QP, which I am quite excited about" from the 2015 interview (Optima 99, p. 4) [stated].
- Last co-authored items: Shen, Leyffer & Fletcher (2012, 10.1007/s10589-011-9430-2); the Powell memoir (2018, posthumous).

### 1.7 Recognition that dates the reception (secondary unless noted)

- 1997 Dantzig Prize, shared with Stephen M. Robinson (Wikipedia, "Dantzig Prize", fetched with the MediaWiki API). [observed, secondary]
- 2003 FRS; 2008 Royal Medal of the Royal Society of Edinburgh; SIAM Fellow (Wikipedia, "Roger Fletcher (mathematician)"). [observed, secondary]
- 2006 **Lagrange Prize in Continuous Optimization** (MPS and SIAM) with Leyffer and Toint for the two 2002 filter papers. The citation text was read on mathprog.org (see Sources). [observed, secondary-official]
- Positions: *Who Was Who* entry title (via Crossref, 10.1093/ww/9780199540884.013.u44012): "Baxter Professor of Mathematics, 1993–2005, and Professor of Optimization, 1984–2005, University of Dundee, then Emeritus". [secondary record]
- Royal Society biographical memoir: N. I. M. Gould & J. A. J. Hall, "Roger Fletcher. 29 January 1939—15 July 2016", *Biogr. Mems Fell. R. Soc.* 78:127–146, 2025, DOI 10.1098/rsbm.2024.0037 (CC-BY). Only its abstract and its Crossref-deposited reference list were read; the full text is behind a Cloudflare challenge (see Gaps). The abstract says he "was the 'F' in the highly influential FR, DFP and BFGS methods for unconstrained optimization, and the inventor of the exact augmented Lagrangian, filterSQP and filterSD methods" and describes "clever design, inspired analysis and detailed implementation". [observed, secondary]

---

## 2. Signature works (framework §五)

Selection logic: the most cited cluster (DFP/FR, BFGS); the work Fletcher himself names first (BFGS, "because it was my own idea"); the constrained-optimization turning point (the exact-penalty → Sl1QP → SLP-EQP line, which Toint and Curtis both single out); the prize-winning later turning point (filter); and the late-career re-examination (Barzilai–Borwein → LMSD), where he publicly changed his mind.

### 2.1 DFP (1963), with Fletcher–Reeves (1964) as its twin

- **Works**:
  - R. Fletcher & M. J. D. Powell, "A Rapidly Convergent Descent Method for Minimization", *The Computer Journal* 6(2):163–168, Aug. 1963, DOI 10.1093/comjnl/6.2.163.
  - R. Fletcher & C. M. Reeves, "Function minimization by conjugate gradients", *The Computer Journal* 7(2):149–154, Feb. 1964, DOI 10.1093/comjnl/7.2.149.
  - Background: W. C. Davidon, "Variable Metric Method for Minimization", Argonne report ANL-5990 (1959), reprinted *SIAM J. Optim.* 1(1):1–17, 1991, DOI 10.1137/0801001.
  - Full texts **not read** (OUP, closed access). Only the abstracts were read (via OpenAlex).
- **Origin** [stated, primary: Optima 99, p. 2]: his PhD needed energy minimization over model parameters for molecular-structure calculations. Following Householder's and (he thinks) Hildebrand's books he tried steepest descent: "it generated reams and reams of paper, punched paper tape output as the iterations progressed, and didn't make a lot of progress. So after that I developed a great suspicion of what people were writing in books." Reeves then obtained Davidon's Argonne report: "Try that for your problem." Fletcher found it "so many times superior to steepest descent" and was writing it up for the *Computer Journal*. Powell, invited to Leeds to talk about his derivative-free method, asked to talk about Davidon's report instead; "when he got to Leeds, he found that we already knew about it, and had codes for it … so we pooled our resources and that was the basis for the famous DFP thing."
  - Fletcher–Reeves [stated, p. 2]: "Colin Reeves suggested to me that if you had some sort of search, you could use it to solve nonquadratic problems. So that became nonlinear CG, and I did the computations and wrote the paper [17] but his was the idea."
- **Why then** [inferred]: Davidon's method existed only as an unpublished lab report (ANL-5990, 1959) until 1991. Leeds had one of the few Ferranti Pegasus machines (Optima 99, p. 1 [stated]), so a PhD student could run a real quasi-Newton code on a real application. The idea arrived through Reeves and Powell; the code and the test problem were Fletcher's.
- **Key insight** (DFP abstract, OpenAlex): an iterative descent method with provable convergence ("A number of theorems are proved to show that it always converges and that it converges rapidly") that is also demonstrated at scale: "The method has been used to solve a system of one hundred non-linear simultaneous equations." FR abstract: "Particular advantages are its simplicity and its modest demands on storage, space for only three vectors being required. An ALGOL procedure is presented". [practice, primary abstracts]
- **Minimum evidence**: the head-to-head comparison against steepest descent on his own thesis problem [stated]. In the paper: theorems + "Numerical tests on a variety of functions" + the 100-equation system [practice].
- **Abandoned paths**: steepest descent, abandoned *by experiment* against textbook advice [stated]. Nothing else is documented.
- **Reception**: the two papers now have 4,619 and 4,971 OpenAlex citations. Curtis (Optima 99, p. 7 [observed]) quotes Nocedal & Wright calling the Fletcher–Powell development a "dramatic advance [that] transformed nonlinear optimization overnight." Fletcher on the moment itself [stated, p. 2]: "Well, I didn't realize how important it was at the time; you don't. For me, it's just okay, it works well, so that's good."
- **Method it shows**: (a) test textbook claims by computation on your own real problem; (b) ship code with the paper (ALGOL procedure, storage count); (c) when two groups hold the same idea, pool resources instead of racing. Credit attribution: he assigns the ideas to Davidon, Reeves and Powell and keeps the computations for himself ("two huge good ideas given to me by people").
- **Era and resources**: 1960–64, first-generation British computers (EDSAC at Cambridge, Pegasus at Leeds), paper-tape output, ALGOL. Team: PhD student + supervisor + one external peer. Fletcher was 24.

### 2.2 BFGS: "A new approach to variable metric algorithms" (1970)

- **Work**: R. Fletcher, *The Computer Journal* 13(3):317–322, 1970, DOI 10.1093/comjnl/13.3.317 (solo). Full text **not read** (closed); abstract read.
- The independent 1970 papers, all Crossref-verified:
  - C. G. Broyden, *IMA J. Appl. Math.* 6(1):76–90, 10.1093/imamat/6.1.76;
  - D. Goldfarb, *Math. Comp.* 24(109):23–26, 10.1090/S0025-5718-1970-0258249-6;
  - D. F. Shanno, *Math. Comp.* 24(111):647–656, 10.1090/S0025-5718-1970-0274029-X.
- **Origin** [stated, Optima 99 p. 2]: "Well, BFGS, one has to say because it was my own idea. There were four papers published independently in 1970 … But I still like mine as the best way to describe BFGS." Where he was when he conceived it: at Harwell, going by the career path in the memoir abstract ([inferred]; the dates are not verified). The thought process itself is not documented in anything I could read → **origin detail: inferred / unknown**.
- **Why then** [inferred]: seven years of DFP use had exposed its sensitivity to inexact line searches and to near-singular updates. The abstract frames the paper around exactly those two issues.
- **Key insight** (abstract, OpenAlex [practice, primary]): "An approach to variable metric algorithms has been investigated in which the linear search sub-problem no longer becomes necessary. The property of quadratic termination has been replaced by one of monotonic convergence of the eigenvalues of the approximating matrix to the inverse hessian. A convex class of updating formulae which possess this property has been established, and a strategy has been indicated for choosing a member of the class so as to keep the approximation away from both singularity and unboundedness." The design criterion itself was swapped: quadratic termination was replaced by eigenvalue behaviour.
- **Minimum evidence**: "A FORTRAN program has been tested extensively with encouraging results." [practice, abstract] The experiments themselves are not read.
- **Abandoned paths**:
  - Quadratic termination as the governing criterion, explicitly dropped [practice, abstract].
  - The paper's headline goal (no line search) did not become the way BFGS is used; later practice pairs BFGS with line searches. This is [inferred] from general knowledge of later practice; I found no Fletcher statement about it.
  - Later he proposed an "ultra-BFGS" formula: "it never attracted any interest. It only gets you a 5 or 10% performance gain, so it's not worth making a big deal about it." (Optima 99, p. 2) [stated]. No identifier is known for the ultra-BFGS papers; the interview says "mentioned in a couple of papers" → **not located**.
- **Return to the result 21 years later** [practice]: "A New Variational Result for Quasi-Newton Formulae", *SIAM J. Optim.* 1(1):18–21, 1991, DOI 10.1137/0801002. Abstract: "The recent measure function of Byrd and Nocedal … is considered and simple proofs of some of its properties are given. It is then shown that the BFGS and DFP formulae satisfy a least change property with respect to this new measure." It is printed directly after Davidon's reprint (pp. 1–17) in the journal's inaugural issue (Crossref).
- **Reception**: 4,138 OpenAlex citations, still roughly 200 a year. His later re-examination of BFGS's dominance (LMSD, §2.5) is read by Curtis as exemplary [observed].
- **Method it shows**: when a method works in practice but fails a design criterion, change the criterion (termination → eigenvalue monotonicity; exact → no line search), identify a *family* (convex class), then choose within it by a safeguarding strategy. Theory serves a tested code.
- **Era and resources**: 1970, FORTRAN, solo author, national lab (physics division). Aged 31.

### 2.3 The exact-penalty line: exact L1 penalty → second-order correction → composite NDO → Sl1QP → SLP-EQP (1973–1989)

- **Works** (all DOIs Crossref-verified unless noted):
  - "An exact penalty function for nonlinear programming with inequalities", *Math. Program.* 5:129–150, 1973, 10.1007/BF01580117.
  - "An Ideal Penalty Function for Constrained Optimization", *IMA J. Appl. Math.* 15(3):319–342, 1975, 10.1093/imamat/15.3.319. This is the augmented-Lagrangian paper, with a "wide selection of numerical evidence" per the abstract.
  - Fletcher & Watson, "First and second order conditions for a class of nondifferentiable optimization problems", *Math. Program.* 18:291–307, 1980, 10.1007/BF01588325.
  - "Numerical experiments with an exact L1 penalty function method", in *Nonlinear Programming 4*, 1981, pp. 99–129, 10.1016/b978-0-12-468662-5.50009-4.
  - "Second order corrections for non-differentiable optimization", LNM "Numerical Analysis", 1982, pp. 85–114, 10.1007/bfb0093151.
  - "A model algorithm for composite nondifferentiable optimization problems", *Mathematical Programming Studies* ("Nondifferential and Variational Techniques in Optimization"), 1982, pp. 67–76, 10.1007/bfb0120959.
  - "Penalty Functions", in *Mathematical Programming: The State of the Art*, 1983, pp. 87–114, 10.1007/978-3-642-68874-4_5.
  - "An l1 penalty method for nonlinear constraints", in *Numerical Optimization 1984* (eds. Boggs, Byrd & Schnabel), SIAM, 1985, pp. 26–40. No DOI. Venue, year and title were verified only through the Gould & Hall memoir's Crossref reference list; **text not read**.
  - Fletcher & Sáinz de la Maza, "Nonlinear programming and nonsmooth optimization by successive linear programming", *Math. Program.* 43:235–256, 1989, 10.1007/BF01582292.
- **Origin** [stated, Optima 99 pp. 3–4]:
  - L1 penalties were not his: "L1 penalty functions go back yonks [34] to Andy Conn [35], his supervisor, Pietrzykowski, was a big L1 man".
  - The structure was: "composite nonsmooth optimization [33], which I did with Alistair Watson [13]. That sort of enables you to do L1, L-infinity, all sorts of polyhedral norms, all in a very nice structure … You wouldn't say I invented it or anything, but I was there in the early early days of it."
  - Sl1QP was the novelty: "the linearized constraints stay in the function. You don't take them out and linearize them. The subproblems involve L1 constraints . . . So that was new."
- **Why then** [inferred]: SQP with quasi-Newton updates had just become popular (Fletcher, p. 3: "about the same time was when Mike Powell popularized it; he did SQP with a quasi-Newton update"). Merit-function globalization was the open problem. Fletcher already had the nonsmooth-optimality machinery with Watson (1980).
- **Key insight**: treat the constrained problem as the minimization of a *structured nonsmooth* (polyhedral) function and globalize with a trust region on that function. The subproblem is then always feasible: "You get guaranteed convergence to a minimum of the L1 function, which may be feasible or may be not . . . it sort of bundles it all together." [stated, p. 3]
- **Minimum evidence** [inferred from titles and order]: the 1981 chapter is titled "Numerical experiments with…" and precedes the 1982 theory papers and the 1985 method paper, which suggests experiments came first. Not confirmed from the texts, which were not read.
- **Abandoned or lost paths**:
  - The SQP student's work was never published: "the student never published anything on it, went in industry and never wrote it up, so I never got a paper out of that." [stated, p. 3]
  - The implementation is undocumented even to him. Asked what solver he used for the L1QP subproblem: "Good question. Don't know what I did." Leyffer reports Steve Wright re-implemented it via slacks with "very good results", unpublished. [stated + observed, p. 3]
  - Exact augmented Lagrangians (multipliers as least-squares functions of x): "It's not a popular approach now but it attracted a lot of interest at the time." [stated, p. 2]
  - Later he moved away from penalty functions altogether (§2.4) while still believing Sl1QP "would still be a competitor with filter methods" [stated, p. 3].
- **Reception**:
  - Fletcher on SLP-EQP [stated, p. 4]: "That's a nice result, I believe my own. It relies on the fact that you can discover the active constraints without solving QPs … And that has caught on a lot. Nocedal uses it". The specific Nocedal code is not named in the interview; [inferred] it refers to the SLQP active-set work around KNITRO, not verified here.
  - Toint (Optima 99, p. 6 [observed]) lists "SL1QP, SLP-EQP, exact augmented Lagrangians, and filter methods" as major and says Fletcher "downplays his contribution to trust-region methods (he called them "restricted step methods" in his wonderful book) … This is far too modest in my view".
  - Curtis (p. 7 [observed]): "as they form the foundations of much recent work on the subject (including my own), I am well aware of his fantastic contributions to constrained nonlinear optimization related to Sl1QP, SLP-EQP, and filters".
  - Nocedal (Optima 102, p. 6 [observed]): Fletcher "was the first researcher to understand how to use polyhedral structure in non-smooth optimization to derive efficient, practical algorithms."
- **Method it shows**: find the *structure* (polyhedral / composite) behind a hard nonsmooth object and design the subproblem to keep it; keep subproblems feasible by construction; use cheap LP steps to identify the active set and then switch to equality-constrained QP (SLP-EQP).
- **Era and resources**: 1973–1989, Dundee, mostly solo; student collaborators on SLP-EQP (Sáinz de la Maza) and composite NDO (Womersley). The subproblem solvers were his own Fortran codes [inferred; he later wrote bqpd in Fortran 77, Optima 99 p. 4].

### 2.4 The filter: "Nonlinear programming without a penalty function" (talk 1996, report 1997, journal 2002)

- **Works**:
  - Fletcher & Leyffer, *Math. Program.* 91(2):239–269, 2002, 10.1007/s101070100244. Earlier: Dundee Numerical Analysis Report NA/171, Sept. 1997 (verified in the Crossref reference list of Leyffer, *Comput. Optim. Appl.* 2001, 10.1023/A:1011241421041).
  - Fletcher & Leyffer, "User manual for filterSQP", Dundee NA/181, April 1998 (same verification).
  - Fletcher, Leyffer & Toint, *SIAM J. Optim.* 13(1):44–59, 2002, 10.1137/S105262340038081X (Namur TR 00/15).
  - Fletcher, Gould, Leyffer, Toint & Wächter, *SIAM J. Optim.* 13(3):635–659, 2002, 10.1137/S1052623499357258 (Namur TR 99/03).
  - Chin & Fletcher, *Math. Program.* 96:161–177, 2003, 10.1007/s10107-003-0378-6.
  - Fletcher, Leyffer & Toint, "A Brief History of Filter Methods", Argonne preprint ANL/MCS-P1372-0906, Sept. 26, 2006 (rev. Oct. 9, 2006), **read in full** (Optimization Online 2006/10/1489).
  - The 2002 *Math. Program.* full text was **not read** (Springer challenge page).
- **Origin** [stated, Optima 99 p. 4]: "It made much tingle when I thought of it. I was just thinking why, why penalty functions didn't work. You often look at the numbers and think, why can't I take SQP steps? Why am I having to throw this stuff away when it's obviously working well? A simple idea there – nobody thought of it, and now quite a number of people take it up."
  - The co-authored history [practice, primary, p. 2] gives the same empirical trigger: "Yet we have noticed that the unmodified SQP method is able to quickly solve a large proportion of test problems without the need for modifications to induce global convergence."
  - It also states the goal: "the development of global optimization safeguards that interfere as little as possible with Newton's method."
- **Why then** [inferred]: two decades of penalty-function SQP (§2.3) had made penalty-parameter tuning and Newton-step rejection a visible, recurring cost. His own QP solver (bqpd) and his former PhD student Leyffer (PhD 1994) were in place. On the rejected steps, the brief history (p. 2) says: "if the penalty parameter is too large, then any monotonic method would be forced to follow the nonlinear constraint manifold very closely, resulting in much shortened Newton steps and slow convergence."
- **Key insight**: treat NLP as a biobjective problem in (f, h) and accept any step not *dominated* by a stored list of past pairs. "We borrow the concept of domination from multiobjective optimization" (brief history, p. 2).
- **Minimum evidence**: numerical experience first. The Lagrange Prize citation says the first paper "includes extensive numerical results, which attest to the potential of the algorithm". The convergence theory came afterwards, with Toint and Gould: "The first global convergence proof of a filter method was given in [11] for a sequential linear programming (SLP) method. This proof was later generalized to SQP methods in [10]." (brief history, p. 5) [practice, primary]
- **Abandoned paths** [practice, primary, brief history]:
  - Heuristics dropped once proved unnecessary (p. 5): "The initial filter method contained features, such as the NW/SE corner rule and unblocking, that were shown to be redundant in the subsequent convergence analysis."
  - A failed hope (p. 6): "Early on, we conjectured that filter methods may be able to avoided the Maratos effect. … We applied filter methods to the original example by Maratos and observed second-order convergence. However, the following example shattered the hope that filter methods can avoid the Maratos effect in general". The fix was to add second-order correction steps, a device Fletcher had introduced in 1982 (§2.3).
  - An assumption the theory could not remove (p. 6): "One undesirable assumption in [10] is the need for global solution to the QP subproblem (2.1)."
  - The Prize citation also records that the second paper "simplified" the earlier algorithm.
- **Reception**:
  - Timeline: plenary talk at the SIAM Optimization Conference, Victoria, May 1996 → report Sept. 1997 → journal Jan. 2002. The reviewing history (rejections, revisions) is **unknown**: the Springer received/accepted dates were not reachable.
  - 2006 Lagrange Prize. The citation reads: "an outstanding new idea has been the introduction of the filter … quickly picked up by other researchers".
  - Adopted in interior-point methods:
    - Wächter & Biegler, "Line Search Filter Methods for Nonlinear Programming: Motivation and Global Convergence", *SIAM J. Optim.* 16(1):1–31, 2005, 10.1137/S1052623403426556;
    - the IPOPT implementation paper, *Math. Program.* (online 28 April 2005), 10.1007/s10107-004-0559-y, which cites Fletcher & Leyffer 2002 (Crossref reference list);
    - Benson, Shanno & Vanderbei, *Comput. Optim. Appl.* 23:257–272, 2002, 10.1023/A:1020533003783.
  - Counter-programme: Gould & Toint, "Nonlinear programming without a penalty function or a filter", *Math. Program.* 122(1):155–196 (online 23 Sept. 2008), 10.1007/s10107-008-0244-7.
  - The brief history (p. 5) records precedents found afterwards: "Filter methods for NLP were developed independently of earlier similar ideas" (Surry et al. 1995, a genetic-algorithm multiobjective approach; Lemaréchal, Nemirovskii & Nesterov 1995, bundle exclusion regions).
- **Method it shows**: diagnose the globalization device by *looking at the numbers* of the unsafeguarded method. Design the safeguard to interfere minimally. Ship the algorithm with code and numerical results first (filterSQP manual NA/181, April 1998). Let collaborators with a theory bent prove convergence, and prune the heuristics the proof shows to be redundant. Toint (Optima 99, p. 6 [observed]): "I always felt that his real interest was in algorithm design, making sure a particular problem could be solved efficiently and reliably."
- **Era and resources**: 1996–2002, aged 57–63. Fortran 77 for bqpd [stated, Optima 99 p. 4]; that filterSQP is also Fortran and is built on bqpd is [inferred], not checked. Test sets: CUTE, plus Chin & Fletcher's NA/203 report on "Selected Cute Test Problems" (Crossref reference list of 10.1137/S105262340038081X). Team: Fletcher + former student Leyffer, with Toint, Gould and Wächter for the theory.

### 2.5 Barzilai–Borwein → limited-memory steepest descent (2005–2012): the documented change of mind

- **Works**:
  - Dai & Fletcher, *Numer. Math.* 100:21–47, 2005, 10.1007/s00211-004-0569-y;
  - Dai & Fletcher, *Math. Program.* 103:541–559, 2005, 10.1007/s10107-004-0516-9;
  - Dai & Fletcher, *Math. Program.* 106:403–421, 2006 (online 2005), 10.1007/s10107-005-0595-2;
  - Fletcher, "On the Barzilai-Borwein Method", 2005, 10.1007/0-387-24255-4_10 (not read);
  - Fletcher, "A limited memory steepest descent method", *Math. Program.* 135:413–436, 2012 (online 2011), 10.1007/s10107-011-0479-6. The preprint (Edinburgh ERGO 09-014, 2 Dec. 2009, Optimization Online 2009/12/2487) was **read in full**.
  - Antecedents: Barzilai & Borwein, *IMA J. Numer. Anal.* 8(1):141–148, 1988, 10.1093/imanum/8.1.141; Raydan, *SIAM J. Optim.* 7(1):26–33, 1997, 10.1137/S1052623494266365.
- **Origin**:
  - The referee episode [stated, Optima 99 p. 4]: "Yuhong Dai [50] wrote a paper about Barzilai-Borwein and I was the referee, and I said this paper was of no interest – something along those lines. And then he wrote back and said, "Have you seen the paper of Marcos Raydan [51], where he is solving problems with 10⁶ variables with this method." The original paper solves a two-variable problem, you see. So that's a case where I changed my mind."
  - The LMSD motivation [stated, preprint p. 1]: "The study has been motivated by some on-going work concerning a Sequential Linear Programming (SLP) algorithm for large scale Nonlinear Programming (NLP), in which a suitable algorithm is required for carrying out unconstrained optimization in the null space. … Currently the obvious Conjugate Gradient (CG) methods have been used, but these have not proved to be very suitable."
  - An incubated idea [stated, preprint p. 2]: "I have therefore returned to some thoughts that I had some 20 years ago (Fletcher [8]), occasioned by innovative ideas inherent in the Barzilai-Borwein (BB) methods … it is suggested that a limited memory approach might be fashioned by using a limited number of eigenvalue estimates … However the idea was not taken any further at the time". Ref. [8] is "Low storage methods for unconstrained optimization", in *Computational Solution of Nonlinear Systems of Equations* (eds. Allgower & Georg), AMS Lectures in Applied Mathematics 26, 1990, pp. 165–179. It was verified only as an entry in the preprint's reference list; **not read**.
- **Why then** [inferred]: application pull (the SLP/SLCP null-space solver that became the 2012 *SIAM J. Optim.* SLCP paper and, per the memoir abstract, filterSD), plus the new evidence of BB at 10⁶ variables.
- **Key insight** [practice, preprint]: store m back gradients, compute Ritz values of the Hessian from the Krylov structure, and use their inverses as step lengths over a "sweep". m = 1 recovers BB.
- **Minimum evidence** [practice, preprint]: quadratic-case theory (a convergence theorem in the appendix, following Raydan) plus tables against BB, CG-FR, CG-PR, BFGS and l-BFGS, including n = 10⁶ problems with timings.
- **Results reported honestly, including losses** [practice, primary]:
  - p. 14: "The Chained Rosenbrock problem provides a different picture with lmsd showing up badly relative to l-BFGS, and to CG-PR to a lesser extent. It is difficult to provide any very convincing reason for this."
  - p. 16: "The results provide no conclusive outcome either way."
  - p. 17: "It is a little disappointing that there seems to be a limit to the number of back vectors that can be utilised effectively."
  - A negative theoretical result from the Dai collaboration: projected BB steps on box-constrained QP can cycle. Fletcher's account of the division of labour [stated, Optima 99 p. 4]: "Yuhong Dai answered it, I checked the results."
- **Abandoned paths**: using more than about 5 back vectors (the conjectured cause is "numerical loss of rank in the bundle of back vectors, in which case there may be nothing that can usefully be done", p. 17); CG as the null-space solver (p. 1).
- **Reception**:
  - Curtis & Guo, "Handling nonpositive curvature in a limited memory steepest descent method", *IMA J. Numer. Anal.* 36(2):717–742 (online 8 July 2015), 10.1093/imanum/drv034.
  - Curtis & Guo, "R-Linear Convergence of Limited Memory Steepest Descent", *IMA J. Numer. Anal.* 38(2):720–742, 2018 (venue per Optimization Online 2016/10/5669; DOI not checked).
  - Curtis (Optima 99, p. 7 [observed]): "his recent work on limited memory steepest descent methods, which he shows personally to be competitive with quasi-Newton methods for certain large-scale problems. While others take the superiority of BFGS-type methods almost as fact, Fletcher himself (the "F"!) is reexamining them".
- **Method it shows**: (a) change your mind when shown evidence at scale, even against your own referee verdict; (b) keep old half-ideas and revive them when an application needs them; (c) report where your method loses and say when the evidence is inconclusive; (d) judge methods on storage and housekeeping too, not only on iteration counts (the preprint compares "long vectors" of storage: 7 for lmsd with m = 5 vs 10 and 14 for l-BFGS with m = 3 and 5, p. 16).
- **Era and resources**: 2005–2012, aged 66–73, emeritus. Solo on LMSD, with Dai (Beijing) for the BB theory. Problems up to 10⁶ variables on a single workstation [inferred from the timings].

### 2.6 Other work that shows the same craft (brief, for cross-reference)

- **Practical Methods of Optimization**: vol. 1 *Unconstrained Optimization* (Wiley, 1980) and vol. 2 *Constrained Optimization* (1981); 2nd ed. 1987 (ISBN 9780471915478); paperback reprint 2000 (DOI 10.1002/9781118723203).
  - The Dennis review of vol. 1 (*SIAM Review* 24(1):97–98, 1982, 10.1137/1024028) exists; **not read**.
  - Nocedal (Optima 102, p. 6 [observed]): "He tried to derive things himself rather than relying on the literature, and this gave his famous textbook a unique flavor." Also: "His papers felt very personal, as if they were addressing the reader directly, and contained very few references (to the consternation of some)."
- **Test-problem practice, early and late**:
  - 1965: "A set of test functions representative of a wide range of minimization problems is proposed and is used as a basis for comparison" ("Function Minimization Without Evaluating Derivatives--a Review", *Comput. J.* 8(1):33–41, 10.1093/comjnl/8.1.33; abstract) [practice].
  - 1966: an independent certification of a published algorithm (Communications of the ACM 9:686–687, "Certification of algorithm 251: function minimisation", 10.1145/365813.365833) [practice].
  - 2015: "everybody publishes solves with 500 test problems from CUTE [54]. I'd rather see half a dozen real industrial problems" (Optima 99, p. 5) [stated].
  - Contrast [practice]: his own 2012 SLCP and 2017 papers still report CUTEr/CUTE results.
- **Application-born methods** [practice]:
  - educational testing → an early SDP (1981, 10.1137/0902021; 1985, 10.1137/0323032);
  - crystal defects and saddle points (Harwell);
  - batch-plant retrofit (1991, 10.1016/0098-1354(91)80029-u);
  - distillation columns (2000, 10.1016/s0098-1354(00)00295-7);
  - SVM training (2010, 10.1017/S0962492910000024).
  - On the SDP origin [stated, Optima 99 p. 2]: three M.Sc. students in turn got slow convergence; "I just though they weren't very good students. But it was only after the third one that I realized that it was something to do with nondifferentiability of eigenvalue constraints". The slow convergence was a signal he first misread as student weakness.
- **Numerical linear algebra in service of optimization** [practice]:
  - bi-CG for indefinite systems (1976, 10.1007/bfb0080116; "never got referenced very much" [stated]);
  - stable LU updates (1984, 10.1007/BF02591933; "nice to do something that people said couldn't be done" [stated]);
  - expected conditioning (1985, 10.1093/imanum/5.3.247; "it never caught on. I just liked that paper" [stated]);
  - null-space stability (1997, 10.1137/S0895479896297732);
  - degeneracy (1988, 10.1016/0024-3795(88)90026-2; 1993, 10.1007/BF02023102; 1998, 10.1137/S1052623494277470; 2014, 10.1137/130930522).
- **MINLP** (with Leyffer) [practice]: outer approximation (1994, 10.1007/BF01581153) and MIQP bounds (1998, 10.1137/S1052623494268455). This is the thesis line of his student Leyffer. It is Fletcher's highest-cited work outside continuous NLP; he does not mention it among his favourites in the 2015 interview.

---

## 3. Failures, abandoned directions and ideas that "never caught on" (collected)

All [stated, primary, Optima 99] unless marked otherwise.

| Item | What happened | Page / source |
|---|---|---|
| Steepest descent for his PhD | "didn't make a lot of progress" → distrust of books | p. 2 |
| ultra-BFGS | "never attracted any interest"; 5–10% gain judged not worth pushing | p. 2 |
| Exact augmented Lagrangians | "not a popular approach now" | p. 2 |
| SDP via BFGS/SQP (M.Sc. projects) | slow convergence misattributed to students for three projects | p. 2 |
| "convex analysis was never very useful for computation" (book) | reversed later | p. 2 |
| bi-CG 1976 | "never got referenced very much" | p. 3 |
| SQP student project | never written up, "I never got a paper out of that" | p. 3 |
| Expected conditioning | "it never caught on" | p. 3 |
| L-implicit-U factors | "another one that has not caught on" | p. 4 |
| Wolfe's degeneracy method | "never caught on very much"; written up only after Margaret Wright's urging | p. 4 |
| Single-precision codes (Powell's maxim) | abandoned after LP experience; a half-precision experiment "works even more badly" | pp. 4–5 |
| Filter heuristics (NW/SE corner rule, unblocking) | shown redundant by the convergence analysis | brief history p. 5 [practice] |
| Filter vs Maratos effect | hope "shattered" by a counterexample → SOC steps | brief history p. 6 [practice] |
| Low-rank quasi-Newton scheme for SQP (2005) | "reasonably encouraging, although there is some evidence of slow convergence on large problems with large null spaces" | NA/223 abstract, Optimization Online 2005/08/1192 [practice] |
| LMSD with many back vectors | "a little disappointing" limit; Chained Rosenbrock poor | preprint pp. 14, 17 [practice] |

No rejected paper, erratum or retraction was found in any source reached. The only refereeing record is his own rejection of Dai's BB paper, which he later reversed.

---

## Contradictions (kept as found; not reconciled)

1. **PhD dates vs Cambridge enrolment.** Fletcher: the Leeds PhD "was '60 to '63" (Optima 99, p. 2). Nocedal's obituary: "He enrolled in Cambridge University in 1960, majoring in theoretical physics … after graduation he enrolled in PhD studies at Leeds" (Optima 102, p. 6). Both cannot hold. The memoir probably settles it, but it was not read.
2. **Credit.** Fletcher: "I got this undeserved reputation for being intelligent" (p. 2); "I've never discovered any of these things myself" (about Wolfe's method, p. 4); composite NDO: "You wouldn't say I invented it" (p. 3). Others: Curtis, "shame on us if we believe that such a thing can happen merely by chance so often" (p. 7); Nocedal, "Yes, Roger, you did" (Optima 102, p. 6); Toint, "far too modest" about trust regions (p. 6).
3. **Barzilai–Borwein timeline.** The LMSD preprint (2009, p. 2) says he had BB-inspired limited-memory "thoughts … some 20 years ago" (the 1990 paper). In 2015 he says that, as referee of Dai's BB paper, he judged it "of no interest" until shown Raydan's 10⁶-variable results (published 1997). So he engaged with BB in 1990 yet dismissed it later. The date of the refereeing is not known.
4. **"Published it just recently" (Wolfe's method).** In the interview, the bibliography links attached to this phrase (refs [41, 42], compiled by Leyffer) point to the 1993 QP-degeneracy paper (10.1007/BF02023102) and the 2000 reduced-Hessian paper (10.1007/s101070050113), not to the 2014 *SIAM J. Optim.* paper whose title is Wolfe's method (10.1137/130930522).
5. **Originality of the filter.** Fletcher: "A simple idea there – nobody thought of it" (Optima 99, p. 4). The co-authored brief history (p. 5) notes earlier similar ideas (Surry et al. 1995; Lemaréchal, Nemirovskii & Nesterov 1995), developed independently.
6. **Test problems.** In 2015 he prefers "half a dozen real industrial problems" to "500 test problems from CUTE" (p. 5), yet his own last method papers (2012 SLCP, 2017 box-QP) validate on CUTEr/CUTE collections (abstracts). He proposed his own test set as early as 1965.
7. **Dates of the SLP-filter report NA/183.** "August 1998" (brief history, ref. [11]) vs "1999" (reference list of 10.1137/S105262340038081X). The Namur twin (TR 98/13) is dated 1998.
8. **Bibliographic metadata.** Fletcher–Reeves 1964 is two-author in DBLP and in Fletcher's own account, but solo in Crossref and OpenAlex. Optima 99 is dated December 2015 on its PDF, but the MOS API gives publishedOn 2016-05-01. The Dai interview is "pp. 3–10" on the Pacific J. Optim. contents page but "2, 1–10" in the memoir's reference list.

---

## Gaps (what I could not find or read)

- **Gould & Hall Royal Society memoir (2025, CC-BY)**: full text blocked by a Cloudflare challenge on royalsocietypublishing.org, for both curl and WebFetch. Only the abstract and the reference list were read. It is probably the single best source on the origins of BFGS, the exact augmented Lagrangian, filterSD and his working habits → high priority for agents 04 and 06, or for the user to supply as a PDF.
- **Y.-H. Dai, "An interview with Roger Fletcher", *Pacific J. Optim.* 2(1):3–10, 2006**: exists (contents page read), but the PDF is marked "ONLINE SUBSCRIPTION". Not read; no attempt to bypass.
- **Fletcher's homepage** (http://www.maths.dundee.ac.uk/~fletcher/): the host no longer resolves. A Wayback snapshot exists (2019-12-22), but web.archive.org is blocked by this session's egress policy (HTTP 403 from the proxy) → not read. His own publication list, software pages (filterSQP, bqpd, filterSD) and NA reports could not be checked.
- **Full texts of DFP 1963, FR 1964 and BFGS 1970** (OUP, closed): only abstracts. The BFGS thought process, the test functions and the experiments are unread.
- **Full text and submission history of the 2002 filter paper** (Springer challenge page; NA/171 not found online): no received/accepted dates; no evidence either way on rejections.
- **SIAM News obituary by Leyffer (2016)**: Cloudflare 403 → not read.
- **Powell's own account of DFP**: the DAMTP report NA2007/03 failed with a TLS error under curl and HTTP 503 under WebFetch. The Powell memoir co-authored by Fletcher (10.1098/rsbm.2017.0023) is Cloudflare-blocked. There is therefore no independent check of the Leeds seminar story.
- **Sl1QP 1985 chapter, "Low storage methods" 1990, the ultra-BFGS papers, the L-implicit-U paper in the Powell tribute volume**: only bibliographic traces (memoir references, preprint references, interview links); texts not read. For ultra-BFGS no citation was located at all.
- **Exact Harwell years** and the year he moved to Dundee: not verified (the memoir abstract gives only the sequence Leeds → Harwell → Dundee).
- **Complete student list**: MGP lists 5 PhD students; others above are [inferred].
- **Software as practice evidence** (bqpd, filterSQP, filterSD source code): not inspected. The GitHub API is restricted in this session. Left to agent 03.
- **Google Scholar**: no profile exists for Fletcher. Semantic Scholar returned HTTP 429 after one call.

---

## Sources

(one line each: title — author — date — URL/DOI — primary/secondary)

1. "It's to Solve Problems – An Interview with Roger Fletcher" (with Toint and Curtis commentaries), *Optima* 99 — S. Leyffer (interviewer), R. Fletcher — Dec. 2015 — https://www.mathopt.org/optima/99/optima_99.pdf — **primary** (Fletcher, stated); Toint/Curtis secondary (observed). Notes: `../sources/talks/2015-12-optima99-leyffer-interview-notes.md`
2. "A Brief History of Filter Methods", Argonne preprint ANL/MCS-P1372-0906 — R. Fletcher, S. Leyffer, Ph. L. Toint — Sept./Oct. 2006 — https://optimization-online.org/2006/10/1489/ — **primary** (practice)
3. "A Limited Memory Steepest Descent Method", Edinburgh ERGO 09-014 (preprint of 10.1007/s10107-011-0479-6) — R. Fletcher — 2 Dec. 2009 — https://optimization-online.org/2009/12/2487/ — **primary** (practice/stated)
4. "A New Low Rank Quasi-Newton Update Scheme for Nonlinear Programming", Dundee NA/223 (Optimization Online abstract page) — R. Fletcher — Aug. 2005 — https://optimization-online.org/2005/08/1192/ — **primary** (abstract only)
5. Author abstracts of Fletcher papers via Crossref/OpenAlex (1963, 1964, 1965, 1970, 1971, 1975, 1991, 2002 FLT, 2002 FGLTW, 2004, 2006, 2012 SLCP, 2014, 2017) — R. Fletcher et al. — various — DOIs as cited above — **primary** (abstract text only)
6. DBLP person records pid 34/2426 and 06/4216 (via scripts/dblp_works.py, SPARQL) — DBLP — fetched 2026-09-28 — https://dblp.org/pid/34/2426.html, https://dblp.org/pid/06/4216.html — primary bibliographic record
7. OpenAlex author A5088683774 (114 works; scripts/fetch_publications.py + direct API) — OpenAlex — fetched 2026-09-28 — `../sources/publications/publications.md` — secondary bibliographic record
8. Crossref work metadata and deposited reference lists (dates, pages, report numbers) — Crossref — fetched 2026-09-28 — https://api.crossref.org — secondary bibliographic record
9. "Roger Fletcher. 29 January 1939—15 July 2016", *Biogr. Mems Fell. R. Soc.* 78:127–146 — N. I. M. Gould, J. A. J. Hall — 14 May 2025 — https://doi.org/10.1098/rsbm.2024.0037 — secondary (**only abstract + reference list read**)
10. "Roger Fletcher (1939–2016)", obituary, *Optima* 102, p. 6 — J. Nocedal — April 2017 — https://www.mathopt.org/optima/102/optima_102.pdf — secondary (observed)
11. 2006 Lagrange Prize in Continuous Optimization citation — MPS/SIAM — 2006 — http://www.mathprog.org/prz/citations/lagrange_2006.htm — secondary (official)
12. Mathematics Genealogy Project, Roger Fletcher (id 52148) — MGP — fetched 2026-09-28 — https://www.mathgenealogy.org/id.php?id=52148 — secondary
13. "Roger Fletcher (mathematician)" and "Dantzig Prize" — Wikipedia — fetched 2026-09-28 — https://en.wikipedia.org/wiki/Roger_Fletcher_(mathematician) — secondary
14. *Optima* 73 (CIME Cetraro school announcement: Fletcher lecturing on SQP, 1–7 July 2007) — MPS — Jan. 2007 — https://mathopt.zib.de/Optima-Issues/optima73.pdf — secondary
15. *Pacific J. Optim.* 2(1) contents (Dai, "An interview with Roger Fletcher", pp. 3–10) — Yokohama Publishers — Jan. 2006 — http://www.yokohamapublishers.jp/online2/pjov2n1.html — secondary (interview itself not read)
16. *Who Was Who* entry title "Fletcher, Prof. Roger, (29 Jan. 1939–2016) …" — OUP — 2007– — https://doi.org/10.1093/ww/9780199540884.013.u44012 — secondary (title only)
17. Leyffer, "Integrating SQP and Branch-and-Bound for Mixed Integer Nonlinear Programming", *Comput. Optim. Appl.* (reference list used to date NA/171 and NA/181) — S. Leyffer — 2001 — https://doi.org/10.1023/A:1011241421041 — secondary
18. Benson, Shanno & Vanderbei, "Interior-Point Methods for Nonconvex Nonlinear Programming: Filter Methods and Merit Functions" — 2002 — https://doi.org/10.1023/A:1020533003783 — secondary (reception)
19. Wächter & Biegler, "Line Search Filter Methods for Nonlinear Programming: Motivation and Global Convergence" — 2005 — https://doi.org/10.1137/S1052623403426556 — secondary (reception)
20. Wächter & Biegler, "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming" — online 2005 — https://doi.org/10.1007/s10107-004-0559-y — secondary (reception; reference list)
21. Gould & Toint, "Nonlinear programming without a penalty function or a filter" — online 2008 — https://doi.org/10.1007/s10107-008-0244-7 — secondary (reception)
22. Curtis & Guo, "Handling nonpositive curvature in a limited memory steepest descent method" — online 2015 — https://doi.org/10.1093/imanum/drv034 — secondary (reception)
23. Curtis & Guo, "R-Linear Convergence of Limited Memory Steepest Descent" (Optimization Online entry) — 2016/2018 — https://optimization-online.org/2016/10/5669/ — secondary (reception)
24. Web search results (2 queries: Lagrange Prize 2006; NA/171 report), used only to locate sources 11 and 17 — 2026-09-28 — secondary (locator only)
