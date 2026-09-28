# Roger Fletcher · 05 Peer critique: blind spots, limits, judgements shown wrong

| Field | Value |
|---|---|
| Researcher | Roger Fletcher (1939–2016), University of Dundee; deceased, so this is a historical lens |
| Dimension | Research agent 05 of 06: peer critique (framework §二, row 5) |
| Research date | 2026-09-28 |
| Sources consulted | 52 source entries. 35 were read as full text, relevant sections or abstract: 6 primary (Fletcher's own words or co-authored texts) and 29 secondary (peers' papers, abstracts, benchmarks, obituaries, the memoir). 17 were checked for bibliographic identity only (Crossref or OSTI metadata) and are marked "not read". Entries 50–52 each bundle several records. See Sources |
| Searches | WebSearch: 2 of the 2 allowed. The rest used curl and WebFetch on known URLs, plus the Crossref, OpenAlex, Semantic Scholar and zbMATH APIs |
| User-supplied material | None. `references/sources/papers`, `essays` and `software` contain only `.gitkeep`. `private/` was not opened |

**What was read and how.** Fletcher never published a reply to a critic, an erratum or a comment that I could find. Research agent 03 found the same: Crossref shows no `update-to` relations on his DOIs. There are also no open reviews, because his field and era had none. The critique record is therefore indirect. It consists of (a) papers by peers that name a limitation of one of his methods and propose a fix, (b) benchmark studies that include his codes or methods, (c) obituaries and the Royal Society memoir, where colleagues judge his work and his self-assessment, and (d) his own and co-authored admissions (*A Brief History of Filter Methods*, 2006; the LMSD preprint, 2009; the Leyffer interview, 2015).

How each source was read:
- Full texts I downloaded in this run: Nocedal, *Acta Numerica* 1992 (author preprint); Lewis & Overton (preprint introduction); Wächter & Biegler's Ipopt paper (Optimization Online preprint 2004/03/836); Gould & Toint's funnel paper (Namur repository preprint, 2 June 2008); Byrd, Curtis & Nocedal 2010 (Curtis's homepage copy); Curtis & Guo 2016 (the same); arXiv 2409.09208 and 2406.13454.
- Copies other research agents fetched from public URLs earlier in this run, in `/tmp/nonlinear-team-scratch/base-skills/roger-fletcher/`: the Gould & Hall memoir (Wayback copy of the CC-BY PDF, per 04-mentorship.md), *Optima* 73, 99 and 102, the Dai interview, the filter brief history, the LMSD preprint, the PBB paper and the MPEC report.
- Springer abstract pages returned a bot challenge for curl and WebFetch. For Springer papers I therefore rely on titles checked on Crossref and on how other authors describe them, and I say so each time.
- Quotes are verbatim. PDF-extraction artifacts (split words, ligatures, stray spaces) were repaired, and nothing else was changed. Page numbers are the printed numbers of the copy read.

**Tags.** [stated] = Fletcher's own words. [practice] = what papers and code show was done. [observed] = what others wrote about him or his methods. [inferred] = my reading, to be checked. Each item also carries **primary** or **secondary**.

---

## 0. Critiques that recur (three or more independent critics)

| # | Critique | Independent critics (source) | Answered? |
|---|---|---|---|
| R1 | **The filter's separate feasibility-restoration phase is a weak point.** The switch rule is hard to design, it can be costly, and the objective is ignored while restoring | Byrd, Curtis & Nocedal 2010 (pp. 2281–2282); Shen, Xue & Pu 2009 (abstract); Gould, Loh & Robinson 2014 and 2015 (abstracts); Gould & Toint 2010 (funnel, "without a penalty function or a filter") | Not by Fletcher in print (none found). Rivals built restoration-free filters (§A7.3). [observed, secondary] |
| R2 | **Fast local convergence (the Maratos effect) is not automatic** for his exact-penalty SQP line, nor for the filter | Chamberlain, Powell, Lemaréchal & Pedersen 1982 (the watchdog, a rival fix); Fletcher–Leyffer–Toint 2006 (a counterexample to their own conjecture); Ulbrich 2004; Wächter & Biegler 2005; Gould & Toint 2008 (the funnel has the same problem) | Yes: Fletcher's second-order correction (SOC) steps (1982, reused in filterSQP). Ulbrich showed an alternative that needs no SOC, and FLT answered that they "currently prefer" SOC (§A7.1) |
| R3 | **His methods' global theory is thin outside convexity or rests on strong assumptions**. DFP: global convergence with Wolfe line searches is open even on convex functions. BFGS: no theory for nonconvex functions, and counterexamples exist. LMSD: proved only on strictly convex quadratics, with no rate. Filter-SQP: the first proof needed global QP solutions | Nocedal 1992; Powell 1984/1986 (as described by Dai 2002 and Nocedal 1992); Dai 2002; Mascarenhas 2004; Lewis & Overton; Curtis & Guo 2016/2018; FLT 2006 (self-critique) | Partly. The filter QP assumption was removed in the 2002 trust-region SQP-filter paper. The LMSD rate and nonconvex handling were supplied by Curtis & Guo. The BFGS nonconvex question is still open in the sources read |
| R4 | **Fletcher misjudged his own work, mostly by underrating it** | Toint (Optima 99, p. 6); Nocedal (Optima 102, p. 6); Gould & Hall memoir (p. 131: "Roger modestly claimed later that the code he developed as part of his thesis … was simply a result of ideas fed to him by Reeves"; p. 142: "extremely modest"). See B5 | Not applicable (posthumous and anecdotal) |
| R5 | **Parts of his stack were not built for sparsity or scale at first** | Memoir pp. 137–138 (sparsity "of lesser importance initially"; the LU update "unable to exploit sparsity"); his co-authored admission that QP steps are "computationally demanding" next to IPMs (Brief History, p. 8); his own NA/223 abstract (via 03-process-evidence.md: "slow convergence on large problems with large null spaces") | Partly, by his students (Hall's sparse linear algebra for blpd/BQPD, memoir p. 139) and by LMSD/filterSD in retirement |

---

## A. Limits of applicability, method by method (critic → source → answered?)

### A1. DFP (Fletcher & Powell 1963, DOI 10.1093/comjnl/6.2.163)

- **Critique: poor self-correction and poor conditioning.** Memoir [observed, secondary] (p. 134): "Although the DFP method proved a major advance over steepest-descent methods, there was some concern that in exceptional circumstances the Hessian approximations generated could become badly conditioned, leading to poorly determined steps."
- **Quantified later by Powell.** Powell, "How bad are the BFGS and DFP methods when the objective function is quadratic?", *Math. Program.* 34:34–47, 1986, DOI 10.1007/BF01582161. Title and venue checked on Crossref; **not read** (Springer). Nocedal's summary of it [observed, secondary] (1992 preprint, p. 23) reports "vast differences of performance between the DFP and BFGS methods" when the initial eigenvalue is large. Nocedal notes a limit of that analysis (p. 24): "Therefore Powell's analysis has some limitations". He then gives a test by Byrd, Nocedal & Yuan (1987) on a two-variable, strongly convex function. There BFGS "obtained the solution to high accuracy in 15 iterations", whereas "the DFP method required 4041 iterations to obtain the solution" (p. 24).
- **Theory gap.** Nocedal (p. 17–18) [observed, secondary]: "It is rather surprising that, even though the DFP method has been known for almost 30 years, we have little idea of what the answer to this basic question will turn out to be. DFP can be made to perform extremely poorly on convex problems, making a negative result plausible. On the other hand, the method has never been observed to fail [...] even in the worst examples we can see the DFP method creeping towards a solution point." The "basic question" is global convergence of DFP with Wolfe line searches on convex functions. Related: Byrd, Nocedal & Yuan, *SIAM J. Numer. Anal.* 24(5):1171–1190, 1987, DOI 10.1137/0724077, whose Crossref title reads "…a Cass [sic] of Quasi-Newton Methods on Convex Problems" (not read).
- **Answered?** Yes, by the field and by Fletcher himself: BFGS (1970) replaced DFP in practice. Memoir (p. 134) [observed]: BFGS "usually performs far better in practice than the DFP one, and to date remains by far the most popular choice". Fletcher [stated, primary] (Optima 99, p. 2) singles out BFGS "because it was my own idea".
- **Era:** 1963 Ferranti Pegasus / Atlas era; the critique matured over 1970–1992.

### A2. Fletcher–Reeves nonlinear CG (1964, DOI 10.1093/comjnl/7.2.149)

- **Critique: erratic efficiency and "jamming" (runs of tiny steps).** Nocedal 1992 preprint [observed, secondary]:
  - p. 11: "The numerical performance of the Fletcher-Reeves method (4.3) is somewhat erratic: it is sometimes as efficient as the Polak-Ribière method, but it is often much slower. It is safe to say that the Polak-Ribière method is, in general, substantially more efficient than the Fletcher-Reeves method."
  - p. 12, crediting Powell (1977): "This propensity for short steps, causes the Fletcher-Reeves algorithm to sometimes stall away from the solution, and this behavior can be observed in practice. For example, I have observed that when solving the minimal surface problem (Toint, 1983) with 961 variables, the Fletcher-Reeves method generates tiny steps for hundreds of iterations, and is only able to terminate this pattern after a restart is performed."
  - p. 12, on a 2-D quadratic: "the Fletcher-Reeves method can be slower than the steepest descent method."
  - Powell, "Restart procedures for the conjugate gradient method", *Math. Program.* 12:241–254, 1977, DOI 10.1007/BF01593790 (Crossref-checked; not read). Nocedal (p. 15): "Motivated by the inefficiencies of the Fletcher-Reeves method, … (Powell, 1977) proposed a conjugate gradient method which restarts automatically". This became Harwell VE04.
- **Replication in Fletcher's own late tests** [practice, primary]. LMSD preprint 2009, Table 5 (p. 14), Chained Rosenbrock, n = 50 and 100: CG-FR "> 9999" iterations against 551 and 874 for CG-PR. On the Trigonometric problem (Table 3, p. 12), however, CG-FR beat CG-PR (319 vs 558 at n = 50). The critique that FR is erratic is thus reproduced in his own numbers, in both directions.
- **Answered? (theory side)** by his own PhD student. Al-Baali, "Descent Property and Global Convergence of the Fletcher—Reeves Method with Inexact Line Search", *IMA J. Numer. Anal.* 5(1):121–124, 1985, DOI 10.1093/imanum/5.1.121 (Crossref-checked; not read; the memoir, p. 138, names Al-Baali as Fletcher's PhD student). Gilbert & Nocedal, *SIAM J. Optim.* 2(1):21–42, 1992, DOI 10.1137/0802003, abstract [observed]: "Some properties of the Fletcher–Reeves method play an important role in the first family". The efficiency critique stands. The global-convergence critique was answered.

### A3. BFGS (Fletcher 1970, DOI 10.1093/comjnl/13.3.317)

- **Critique: no convergence theory for nonconvex functions, and counterexamples.**
  - Dai, "Convergence Properties of the BFGS Algoritm" [sic, Crossref title], *SIAM J. Optim.* 13(3):693–701, 2002, DOI 10.1137/S1052623401383455, abstract [observed, secondary]: "In 1984, Powell presented an example of a function of two variables that shows that the Polak--Ribière--Polyak (PRP) conjugate gradient method and the BFGS quasi-Newton method may cycle around eight nonstationary points if each line search picks a local minimum that provides a reduction in the objective function. … It is also noted through the examples that the BFGS method with Wolfe line searches need not converge for nonconvex objective functions." The Powell 1984 paper is *Lecture Notes in Math.* 1066:122–141, DOI 10.1007/BFb0099521 (Crossref-checked; not read).
  - Mascarenhas, "The BFGS method with exact line searches fails for non-convex objective functions", *Math. Program.* 99(1):49–61, 2004, DOI 10.1007/s10107-003-0421-7. Title checked; text **not read** (Springer). The claim is taken from the title only.
  - Lewis & Overton (preprint of *Math. Program.* 141:135–163, 2013, DOI 10.1007/s10107-012-0514-2), p. 1 [observed, secondary], on Powell's 1976 convex result: "The result has never been extended to the nonconvex case. Indeed, very little is known in theory about the convergence of the standard BFGS algorithm when f is a nonconvex smooth function, although it is widely accepted that the method works well in practice".
- **The applicability turned out wider than designed** [observed]. Lewis & Overton (p. 1): "when applied to a wide variety of nonsmooth, locally Lipschitz functions, not necessarily convex, BFGS is very effective". They cite Lemaréchal (1982) for the early observation.
- **Rival: SR1.** Khalfan, Byrd & Schnabel, *SIAM J. Optim.* 3(1):1–24, 1993, DOI 10.1137/0803001, abstract [observed]: "The experiments show that the SR1 is very competitive with the widely used BFGS method" (OpenAlex renders "SR1" as "SRi"). Conn, Gould & Toint, *Math. Program.* 50:177–195, 1991, DOI 10.1007/BF01594934 (checked; not read). Fletcher's own later position [stated, primary] (Dai interview, Q15, c.2005): "There is some evidence that the SR1 method converges faster than BFGS, especially when line searches are not used (say in a trust region context). However there is the problem of retaining a positive definite Hessian with SR1." His 2005 BFGS/SR1 hybrid was his answer. Curtis (Optima 99, p. 7) [observed]: "While others take the superiority of BFGS-type methods almost as fact, Fletcher himself (the "F"!) is reexamining them".
- **Was BFGS the best update?** Nocedal (1992, p. 25) [observed]: "Even though these studies are interesting, it is too soon to know if any of these new methods can perform significantly better than the BFGS method."
- **Answered?** The nonconvex question is not answered in anything I read. No reply by Fletcher was found.

### A4. Exact augmented Lagrangian (1970; Abadie volume and Fletcher & Lill)

- **Critique, unspecified.** Memoir (p. 134) [observed, secondary]: "Although there were still some drawbacks, later work by others has sought to overcome these." The drawbacks are not named in anything I read.
- **Fletcher's own verdict** [stated, primary] (Optima 99, p. 2): "It's not a popular approach now but it attracted a lot of interest at the time. … They keep getting used from time to time. Mike Powell took it up with a student at a much later date."
- **Answered?** Unknown. A later line of exact augmented Lagrangians exists: Di Pillo & Grippo, *SIAM J. Control Optim.* 17(5):618–628, 1979, DOI 10.1137/0317044. Its abstract does not name Fletcher, so any link to his function is [inferred] only. → Gaps.

### A5. Bi-CG (1976)

- **Critique** [observed, secondary] (memoir, p. 137): "Although subtle instabilities have proved to be its Achilles heel in practice, BiCG is the basis of subsequent stabilized methods such as the much-used BiCGStab". The answer came from others: van der Vorst's Bi-CGSTAB, *SIAM J. Sci. Stat. Comput.* 13(2):631–644, 1992, DOI 10.1137/0913035 (see Contradictions for the date).
- Fletcher [stated, primary] (Optima 99, p. 3): "My original paper in 1976 never got referenced very much."

### A6. Exact-penalty SQP line: ℓ1 penalty, second-order correction, Sl1QP, SLP-EQP (1980s)

- **A6.1 The Maratos effect and rival fixes.** A non-smooth merit function can reject the full SQP step near a solution. FLT (Brief History, p. 6) [stated, co-authored, primary] define it: "This effect causes penalty function SQP methods to reject the full SQP step arbitrarily close to a solution, leading to a loss of second-order convergence."
  - Fletcher's answer: second-order correction steps, 1982 (*Numerical Analysis*, Lecture Notes in Math. 912, DOI 10.1007/BFb0093144; Crossref gives only the volume title, so the chapter title is not checked).
  - Rival answer from Powell's group: Chamberlain, Powell, Lemaréchal & Pedersen, "The watchdog technique for forcing convergence in algorithms for constrained optimization", *Math. Program. Studies* 16:1–17, 1982, DOI 10.1007/BFb0120945 (checked; not read). [observed]
  - Memoir (p. 137) [observed] frames the underlying critique of the Han–Powell approach, to which Sl1QP was Fletcher's answer: "imposing such a merit function upon a step-selection subproblem is problematic; one can trip up the other. Roger, by contrast, viewed the penalty function as the essence, and chose the step-selection subproblem with this in mind."
- **A6.2 The penalty parameter.** Fletcher later made this critique himself, as the motivation for filters. FLT (Brief History, p. 2) [stated, co-authored, primary]: "Unfortunately, a suitable penalty parameter depends on the solution of (1.1) … This fact makes it difficult to find a suitable penalty parameter. Worse, if the penalty parameter is too large, then any monotonic method would be forced to follow the nonlinear constraint manifold very closely, resulting in much shortened Newton steps and slow convergence."
  - **The penalty school's answer** [observed, secondary]. Byrd, Nocedal & Waltz, "Steering exact penalty methods for nonlinear programming", *Optim. Methods Softw.* 23(2):197–213, 2008, DOI 10.1080/10556780701394169, abstract: "In contrast with classical approaches, the choice of the penalty parameter ceases to be a heuristic and is determined, instead, by a subproblem with clearly defined objectives." Also Curtis & Nocedal, "Flexible penalty functions…", *IMA J. Numer. Anal.* 28(4):749–769, 2008, DOI 10.1093/imanum/drn003, abstract: "the penalty parameter can be chosen as any number within a prescribed interval, rather than a fixed value." And Byrd, Gould, Nocedal & Waltz, *SIAM J. Optim.* 16(2):471–489, 2005, DOI 10.1137/S1052623403426532, abstract: "A procedure for dynamically adjusting the penalty parameter is described, and global convergence results for it are established." [inferred] The penalty school answered the filter's founding critique inside the penalty framework rather than conceding it.
- **A6.3 Infeasible problems.** Byrd, Curtis & Nocedal, "Infeasibility Detection and SQP Methods for Nonlinear Optimization", *SIAM J. Optim.* 20(5):2281–2299, 2010, DOI 10.1137/080738222 [observed, secondary], p. 2283: "The penalty SQP method proposed by Fletcher, otherwise known as an Sℓ1QP method [16,17] or elastic SQP method [19,4], was designed to overcome the difficulties posed by incompatibility of the constraints (1.3b). The subproblem in such a penalty SQP method is, in fact, always feasible, meaning that the search direction is always well defined. What the method lacks, however, are fast local convergence guarantees when (1.1) is infeasible." The paper then supplies those guarantees. Its acknowledgment (p. 2298) credits Fletcher with the agenda: "The authors would like to thank Roger Fletcher for having stressed throughout the years the need to build fast infeasibility detection capabilities in optimization algorithms."
- **A6.4 Sl1QP survived in rivals' codes** [observed]. BCN 2010 (p. 2283): "the snopt software package [19] reverts to an ℓ1 penalty approach when the Lagrange multipliers are deemed too large or when the quadratic subproblem is inconsistent." KNITRO's SLQP descends from Fletcher & Sainz de la Maza's SLP-EQP: Byrd, Gould, Nocedal & Waltz, *Math. Program.* 100(1):27–48, 2004, DOI 10.1007/s10107-003-0485-4. The paper is checked but **not read**; the link rests on the title and on the 2005 abstract, which names "successive linear programming approaches". Fletcher's claim [stated, primary] (Optima 99, p. 3): "I think that is something that would still be a competitor with filter methods." He supports it with an unpublished Steve Wright implementation ("He had very good results with it. I don't think that work was published"). I found **no benchmark that tests this claim** (→ Gaps).

### A7. Filter methods and filterSQP (talk 1996; *Math. Program.* 91:239–269, 2002, DOI 10.1007/s101070100244; *SIAM J. Optim.* 13(1):44–59, 2002, DOI 10.1137/S105262340038081X)

- **A7.1 A conjecture refuted: filters do not avoid the Maratos effect** [stated, co-authored, primary] (Brief History, p. 6): "Early on, we conjectured that filter methods may be able to avoided [sic] the Maratos effect. … However, the following example shattered the hope that filter methods can avoid the Maratos effect in general". The fix was SOC steps.
  - **Alternative answer by a peer**: S. Ulbrich, "On the superlinear local convergence of a filter-SQP method", *Math. Program.* 100(1):217–245, 2004, DOI 10.1007/s10107-003-0491-6 (checked; not read). FLT's own summary of it (pp. 6–7) [stated]: "Ulbrich [27] proves fast local convergence without the use of SOC steps by making three modifications to the filter SQP method". **How they answered** (p. 7): "We currently prefer to use SOC steps to obtain fast local convergence because this approach allows us to keep the original filter definition with f(x), rather than the Lagrangian L(x,y). This approach also avoids the need for a multiplier function." That is, they kept their design and rejected the alternative on simplicity grounds.
  - Wächter & Biegler, "Line Search Filter Methods for Nonlinear Programming: Local Convergence", *SIAM J. Optim.* 16(1):32–48, 2005, DOI 10.1137/S1052623403426544, abstract [observed]: with SOC steps, "the proposed method does not suffer from the Maratos effect". This is independent confirmation of the SOC route.
- **A7.2 The global-QP assumption** [stated, co-authored, primary] (Brief History, p. 6): "One undesirable assumption in [10] is the need for global solution to the QP subproblem (2.1). This assumption may be difficult to ensure, unless Hk is positive semi-definite." **Answered** (p. 7): the trust-region SQP-filter paper "removes the need for a global solution of the QP" (Fletcher, Gould, Leyffer, Toint & Wächter, *SIAM J. Optim.* 13(3):635–659, 2002, DOI 10.1137/S1052623499357258). The claim sits in tension with his own 2005 statement that there is "little evidence that this is a serious difficulty in practice" (02-methodology.md, C3).
- **A7.3 The restoration phase** (R1) [observed, secondary]:
  - Byrd, Curtis & Nocedal 2010 (pp. 2281–2282): "Such an approach has been advocated by Fletcher and Leyffer [18] and has the benefit that infeasibility can be declared when a minimizer of the infeasibility measure is found that violates one or more constraints. The main difficulty faced by this type of approach, however, lies in the design of effective criteria for determining when such a switch should be made, since an inappropriate technique can lead to inefficiencies. In particular, since the objective function is ignored during iterations that care only about minimizing a measure of infeasibility, the iterates may stray from an optimal solution, thus delaying the optimization process."
  - Shen, Xue & Pu, "A filter SQP algorithm without a feasibility restoration phase", *Comput. Appl. Math.* 28(2), 2009, DOI 10.1590/s1807-03022009000200003, abstract: "Compared with other filter SQP algorithms, our algorithm does not require any restoration phase procedure which may spend a large amount of computation." [inferred, not checked] Chungen Shen is probably the same person who co-authored the 2012 nonmonotone filter with Leyffer and Fletcher (DOI 10.1007/s10589-011-9430-2). If so, a critic of the filter became a co-author.
  - Gould, Loh & Robinson, *SIAM J. Optim.* 24(1):175–209, 2014, DOI 10.1137/130920599, abstract: "This contrasts traditional filter methods that use a (separate) restoration phase designed to reduce infeasibility until a feasible subproblem is obtained. Therefore, an advantage of our approach is that every trial step is computed from subproblems that value reducing both the constraint violation and the objective function." Their follow-up, *SIAM J. Optim.* 25:1885–1911, 2015, DOI 10.1137/140996677, abstract: "This contrasts previous filter methods that require a separate restoration phase based on subproblems solely designed to reduce infeasibility."
  - The memoir (p. 139) [observed] treats the restoration phase as a necessary refinement: "this simple idea needed a number of refinements, most especially to stop a sequence of iterates from converging to a non-optimal point, and to escape from regions in which this happened using a 'restoration' phase."
  - **Answered?** No reply by Fletcher found.
- **A7.4 Strength of the convergence theory.**
  - FLT's own outline (Brief History, pp. 5–6) [stated, co-authored] lists as one possible outcome: "There exists a feasible accumulation point that either is stationary or the Mangasarian-Fromowitz constraint qualification fails", and calls these results "as strong as can be expected for general NLPs".
  - Gould & Toint, "Nonlinear programming without a penalty function or a filter" (preprint 2 June 2008 of *Math. Program.* 122(1):155–196, 2010, DOI 10.1007/s10107-008-0244-7), p. 29 [observed, secondary]: "It is also interesting to note that we have proved that every limit point of the sequence of iterates must be first-order critical, a result which has not been established for filter algorithms."
  - Against that: Gonzaga, Karas & Vanti, *SIAM J. Optim.* 14(3):646–669, 2004, DOI 10.1137/S1052623401399320, abstract: "for a slightly larger filter, all accumulation points are stationary." (Kept as a contradiction, see C4.) Note that Gould and Toint were Fletcher's own co-authors on filter theory: the critique comes from inside the collaboration.
- **A7.5 The "funnel" as a simpler rival** [observed, secondary].
  - Gould & Toint 2008 preprint (pp. 1–2): their method "does not use any merit function (penalty, or otherwise), thereby avoiding the practical problems associated with the setting of the merit function parameters, but nor does it use the filter idea first proposed by Fletcher and Leyffer (2002)." They concede (p. 30) that their own method "like many SQP methods, might suffer from the Maratos effect."
  - Kiessling, Leyffer & Vanaret, "A Unified Funnel Restoration SQP Algorithm", arXiv 2409.09208 (v1, 13 Sept 2024); published *Math. Program.* 217:323–367, 2025, DOI 10.1007/s10107-025-02284-3. p. 2: "We wish to demonstrate that the funnel method obtains performance similar to that of the filter method, while being simpler to implement." p. 11: "We can now interpret the funnel as a filter with a single entry". p. 24: "An implementation of the funnel strategy in the Uno solver proved to slightly outperform its filter counterpart with respect to constraint evaluations for a subset of CUTEst instances, while being also easier to implement." Leyffer, Fletcher's filter co-inventor, co-authored this, so it is an insider's revision, not a hostile critique.
- **A7.6 Independent benchmark support for the filter's premise** [observed, secondary]. Wächter & Biegler (Ipopt preprint 2004; *Math. Program.* 106(1):25–57, 2006, DOI 10.1007/s10107-004-0559-y) compared filter and exact-penalty line searches inside Ipopt on 932 CUTEr problems:
  - p. 23: "As one can see, the filter option is indeed more robust than the penalty function method, even when the heuristics are disabled."
  - The limit they reported with it (p. 23): "Note that the "Full Step" option still does relatively well in terms of robustness (86.1% of the problems solved); this might indicate that in many cases Newton's method does not require a safeguarding scheme …, or alternatively, that many problems in the test set are not very difficult." And: "On the other hand, the different options do not seem to differ very much in terms of efficiency." p. 24: "The filter option seems to be only slightly more efficient for those problems."
  - [inferred] This both supports and qualifies the observation on which Fletcher founded the filter: "the unmodified SQP method is able to quickly solve a large proportion of test problems" (Brief History, p. 2). Such evidence may reflect easy test sets.
- **A7.7 Filters and interior-point methods.** The memoir (pp. 139–140) [observed]: "NLP filters are a key component of perhaps the overall most successful current nonlinear optimization software package, IPOPT (Wächter & Biegler 2006)." Wächter & Biegler (preprint p. 1) on the LOQO variant: Benson, Shanno and Vanderbei "proposed several heuristics based on the idea of filter methods, for which improved efficiency is reported compared to their previous merit function approach, although no convergence analysis is given." (Benson, Vanderbei & Shanno, *Comput. Optim. Appl.* 23(2):257–272, 2002, DOI 10.1023/A:1020533003783; checked, not read.)
- **A7.8 Prize-committee prediction** [observed, secondary] (Lagrange Prize citation, Optima 73, Jan. 2007, p. 5): "Currently, some of the most effective nonlinear optimization codes are based on filter methods. The importance of the work cited here will continue to grow as more algorithms and codes are developed." The committee also noted what the theory did to the design: "The earlier algorithm is simplified, and in so doing the analysis plays its natural role with respect to algorithmic design." Whether the prediction held is mixed (C5).

### A8. Barzilai–Borwein and LMSD (2005–2012)

- **A8.1 Nonconvexity left open** [observed, secondary]. Curtis & Guo, "Handling nonpositive curvature in a limited memory steepest descent method", *IMA J. Numer. Anal.* 36(2):717–742, 2016, DOI 10.1093/imanum/drv034:
  - p. 723: "Despite the sophisticated mechanisms employed in his step-size computation procedure, Fletcher admits that his approach leaves unanswered the question of how to handle nonconvexity."
  - p. 723: "In his implementation, Fletcher employs a strategy that carries out a line search whenever a nonpositive step size is computed, and then terminates the sweep to effectively throw out previously computed information. By contrast, in our approach, we avoid discarding previously computed information, yet are still able to obtain reasonable step sizes."
  - The admission they refer to [stated, primary] (LMSD preprint 2009, p. 12), on the non-quadratic case including "various effects related to the existence of non-positive curvature": "None of these issues admits a single obvious solution, and various possibilities might be followed up."
- **A8.2 No convergence rate.** Fletcher's appendix proves only that the basic sweep method "converges when applied to minimize a strictly convex quadratic function" [practice, primary] (preprint p. 17). Curtis & Guo, "R-linear convergence of limited memory steepest descent", *IMA J. Numer. Anal.* 38(2):720–742, 2018, DOI 10.1093/imanum/drx016, abstract [observed]: "it is shown that, under reasonable assumptions, the method is R-linearly convergent for any choice of the history length parameter." The gap was answered by others, after his death.
- **A8.3 Poor case and a ceiling** [stated, primary]. LMSD preprint p. 14: "The Chained Rosenbrock problem provides a different picture with lmsd showing up badly relative to l-BFGS, and to CG-PR to a lesser extent. It is difficult to provide any very convincing reason for this." And p. 17: "It is a little disappointing that there seems to be a limit to the number of back vectors that can be utilised effectively." **Independent replication** [observed]: Curtis & Guo 2016 (p. 733): "results for larger values of m did not lead to improved performance beyond the values considered here. This is consistent with Fletcher's experience with his LMSD method, and in some previous studies of L-BFGS."
- **A8.4 A "fix" by others that Fletcher and Dai found harmful.** This is Fletcher as critic (see D1).

### A9. Active-set QP/LP software (VE02 → BQPD, blpd)

- **Sparsity** [observed, secondary] (memoir p. 137): "Of paramount importance was his insistence that the methods he proposed should be robust to floating-point computation. Of lesser importance initially to Roger was the issue of methods being computationally efficient for sparse problems." On the Fletcher–Matthews LU update (p. 138): "Although unable to exploit sparsity, this update was remarkably reliable, and was the foundation of Roger's computational work for a while." **Answered** by students: Julian Hall "improving its computational efficiency by developing its sparse numerical linear algebra routines" (p. 139).
- **Precision** (see B3).

---

## B. Judgements shown wrong, reversed or disputed

| # | Judgement | Who showed it wrong or disputed it, and how | Tag |
|---|---|---|---|
| B1 | As referee, he judged Dai's Barzilai–Borwein paper "of no interest" | Dai pointed to Raydan's 10⁶-variable results: *SIAM J. Optim.* 7(1):26–33, 1997, DOI 10.1137/S1052623494266365. Fletcher: "So that's a case where I changed my mind" (Optima 99, p. 4). Memoir (p. 140): "Roger was initially cynical since the steepest-descent method generally has a notoriously poor reputation in practice, but he gradually changed his mind." | stated (primary) + observed (secondary) |
| B2 | In his book: convex analysis "never very useful for computation" | He reversed it himself: "Then I changed my mind when I needed to use it for things like semidefinite matrices" (Optima 99, p. 2) | stated, primary |
| B3 | Powell's maxim, which he adopted: a good algorithm "should work in single precision" | Shown wrong by his own LP work: "It was a sort of misapprehension on my part that I thought it might be a good idea. I don't believe it anymore; I wouldn't write in single precision now." (Optima 99, p. 5) | stated, primary |
| B4 | Co-authored conjecture that filters avoid the Maratos effect | Refuted by a 2-D counterexample (Brief History, p. 6) | stated, co-authored, primary |
| B5 | His self-assessment of his contributions | Disputed by peers. Toint (Optima 99, p. 6): "I must admit I was really surprised that he downplays his contribution to trust-region methods (he called them "restricted step methods" in his wonderful book), giving a pointer to a paper by Beale (which I confess ignoring). This is far too modest in my view (and quite typical of him)". Nocedal (Optima 102, p. 6), quoting Fletcher on structured non-smooth optimization ("You wouldn't say I invented it or anything . . ."): "Yes, Roger, you did." | observed, secondary |
| B6 | Filter originality: "A simple idea there – nobody thought of it" (Optima 99, p. 4) | Precedents named afterwards. FLT themselves (Brief History, p. 5): "Filter methods for NLP were developed independently of earlier similar ideas" (Surry et al. 1995; Lemaréchal, Nemirovskii & Nesterov 1995). The memoir (p. 139): Christine Zoppke-Donaldson's "unpublished work on 'tolerance tubes' for nonlinear programming (NLP) helping to pave the way for the groundbreaking work done by Roger with Sven Leyffer". Gould & Toint (2008 preprint, p. 2) relate the funnel to Himmelblau's 1972 "flexible tolerance method" and Zoppke-Donaldson's 1995 "tolerance tube method", of which they say: "No convergence seems to be available for the method, although the numerical results appear satisfactory." (The Surry, Lemaréchal, Himmelblau and Zoppke-Donaldson works themselves are not verified here) | stated vs observed |
| B7 | MPECs: SQP "at present outperform[s] Interior Point solvers both in terms of speed and reliability" (Fletcher & Leyffer, NA/210, 2002, abstract; *Optim. Methods Softw.* 19:15–40, 2004, DOI 10.1080/10556780410001654241) | A time-bound claim. Leyffer himself then co-authored interior-penalty methods for MPCCs: Leyffer, López-Calva & Nocedal, *SIAM J. Optim.* 17(1):52–77, 2006, DOI 10.1137/040621065, whose abstract says "the need for adaptive penalty update strategies is motivated with examples" and reports efficiency and robustness "on an extensive collection of test problems". Whether IPMs then matched SQP on MPECs: **not read** | stated vs observed; outcome unknown |
| B8 | Prediction (Dai interview, Q15, c.2005): "I find it very hard to envisage significant new ideas in nonlinear CG and quasi-Newton methods." | Unsettled [inferred]. Later activity includes his own LMSD (a limited-memory steepest descent, arguably outside CG/QN proper), BFGS on nonsmooth problems (Lewis & Overton, 2013), and Curtis & Guo's LMSD extensions. Whether these are "significant new ideas" in CG/QN is a judgement I cannot settle from the sources | stated; outcome inferred |
| B9 | His codes' reliability | Curtis (Optima 99, p. 7) once "spoke critically in my talk about the performance of one of his codes on a certain class of problems"; which code and which class are not stated. The same text calls "filterSQP, filterSD, BQPD, etc." "some of the most reliable software available today" | observed, secondary |

---

## C. Blind spots and the rival schools

- **C1. Interior-point methods.**
  - Memoir (p. 137) [observed, secondary]: "Roger had little interest in the latter since they only yield approximate solutions (and often poor estimates of the optimal active set that is so fundamental for SQP methods)."
  - Practice [primary]: in 2002 he benchmarked against IPM codes (LOQO, KNITRO) and judged SQP better on MPECs (B7). The 2006 review he co-signed concedes the IPM advantage on cost (Brief History, p. 8): "Interior-point methods (IPMs) are an attractive alternative to SQP methods for solving NLPs. Instead of computing a step by solving a QP, which can be computationally demanding, IPMs compute a step by solving a linear system."
  - [inferred] Evidence that this was a blind spot: the most widely adopted carrier of his filter idea became an interior-point code (Ipopt; memoir p. 140). Evidence that it was not: his own reasons (accurate active sets for SQP) are the same ones his rivals cite for active-set methods, and he did benchmark against IPMs rather than ignore them.
- **C2. Sparsity and scale came second at first** (A9, R5).
- **C3. Scholarship and citation practice** [observed, secondary]. Nocedal (Optima 102, p. 6): "His papers felt very personal, as if they were addressing the reader directly, and contained very few references (to the consternation of some). He tried to derive things himself rather than relying on the literature, and this gave his famous textbook a unique flavor." [inferred] B6 (priority on the filter) is consistent with this habit of deriving first and meeting the literature later.
- **C4. Test problems.**
  - His stated preference [stated, primary] (Optima 99, p. 5): "I'd much rather get my problems from the people who have problems to solve, rather than taking them from a library of test problems."
  - His practice: CUTE/CUTEr in the filter and LMSD work (03-process-evidence.md §2.2).
  - The peer caveat on what CUTEr results mean: Wächter & Biegler's remark that "many problems in the test set are not very difficult" (A7.6).
- **C5. Division of labour on theory.**
  - Fletcher advised against long proofs [stated, primary] (Optima 99, p. 5: "don't write convergence proofs that are 30 pages long").
  - The filter convergence theory was written with Toint, Gould and Wächter [practice].
  - Toint [observed] (Optima 99, p. 6): "I always felt that his real interest was in algorithm design".
  - [inferred] The theory critiques in A7.2 and A7.4 (the global-QP assumption; limit-point strength) landed where he had delegated. The fixes also came from the theory side.

---

## D. Fletcher as critic, and whether his critiques were answered

- **D1. Against the GLL nonmonotone line search in projected BB/SPG** [stated, co-authored, primary]. Dai & Fletcher, *Numer. Math.* 100:21–47, 2005, DOI 10.1007/s00211-004-0569-y.
  - Abstract (p. 21): "We show by many numerical experiments that the performance of the PBB method deteriorates if the GLL line search is used."
  - p. 26: "the GLL nonmonotone line search may significantly degrade the performance of the PBB and PABB methods. In fact, numerical results of the two methods without line searches are often better than those with the GLL line search."
  - The target: Birgin, Martínez & Raydan, "Nonmonotone Spectral Projected Gradient Methods on Convex Sets", *SIAM J. Optim.* 10(4):1196–1211, 2000, DOI 10.1137/S1052623497330963 (checked; not read). GLL itself: Grippo, Lampariello & Lucidi, *SIAM J. Numer. Anal.* 23(4):707–716, 1986, DOI 10.1137/0723046.
  - Memoir (p. 140) [observed]: "Roger found that a common generalization for general objectives can sometimes behave badly (54)". Item 54 is his 2005 chapter "On the Barzilai-Borwein Method", DOI 10.1007/0-387-24255-4_10 (checked; not read).
  - **Reply by Birgin, Martínez or Raydan: not found** (→ Gaps).
- **D2. Against earlier MPEC studies and IPMs** [stated, co-authored, primary] (NA/210, 2002).
  - Report p. 10: "Previous numerical studies of MPECs and complementarity problems have sometimes made erroneous conclusions, attributing the failure of solvers to the failure of MFCQ."
  - p. 12: "The challenge for developers of interior point methods is to match the performance obtained without the complementarity constraint in the NLP formulation of the MPECs."
  - Taken up by Leyffer, López-Calva & Nocedal 2006 (B7); outcome not read.
- **D3. Against LOQO's single-entry "filter"** [stated, co-authored, primary] (Brief History, p. 10): "The filter used in LOQO consists of a single entry. We are not sure that this device alone can guarantee convergence. The practical performance of LOQO has been encouraging, however, underlining the computational advantage of filter methods." The critique is carefully hedged, and it concedes the numbers. [inferred] Eighteen years later Leyffer's group proved convergence for a funnel that they "interpret … as a filter with a single entry" (A7.5), which partly vindicates the single-entry idea that the 2006 text doubted.
- **D4. Against penalty functions** (A6.2). Answered by steering and flexible penalties (2008) and penalty-based infeasibility detection (2010). The rival school did not concede.
- **D5. How he received critique in person** [observed, secondary]. Curtis (Optima 99, p. 7) on the talk that criticised one of his codes: "one might think that the experience could have been quite intimidating for me! But with Roger the experience was nothing but a pleasure". [observed] Curtis later co-maintained filterSD on COIN-OR (03-process-evidence.md §6).

---

## E. Replications and benchmarks

| Study | What it tested | Outcome for Fletcher's work | Read? |
|---|---|---|---|
| Wächter & Biegler, Ipopt 2006 (preprint 2004), 932 CUTEr problems | Filter vs exact-penalty line search in one IPM | Filter "more robust"; efficiency similar; test-set difficulty caveat | read (§4.1) |
| Dolan, Moré & Munson, "Benchmarking optimization software with COPS 3.0", ANL/MCS-TM-273, 2004, DOI 10.2172/834714 | FILTER vs KNITRO, LOQO, MINOS, SNOPT on COPS | OSTI abstract only: "They also provide a comparison of the FILTER, KNITRO, LOQO, MINOS, and SNOPT solvers on these problems." Results **not read** (PDF 403/503) | no |
| Vanaret & Leyffer, arXiv 2406.13454 v2 (2025); *Math. Program. Comput.* 2026, DOI 10.1007/s12532-026-00310-9 | Uno's `filtersqp` preset vs filterSQP (version 20010817, with BQPD) and six other solvers on 429 small CUTE problems | A successful re-implementation: "These performance profiles demonstrate that the Uno presets filtersqp and ipopt mimic the corresponding state-of-the-art solvers well and perform well with respect to all the state-of-the-art solvers" (pp. 21–23). filterSQP 2001 is still a reference baseline in 2024–26. Not independent (Leyffer) | relevant pages |
| Kiessling, Leyffer & Vanaret 2024/2025 | Funnel vs filter inside Uno, CUTEst subset | Funnel "slightly outperform[s]" the filter on constraint evaluations and is "easier to implement" | relevant pages |
| Curtis & Guo 2016 | LMSD variants on nonconvex problems | Confirms the ceiling on history length; improves nonconvex handling | relevant pages |
| Fletcher's own LMSD tables (2009) | CG-FR, CG-PR, BB, l-BFGS, BFGS, LMSD | Reproduces the FR stall (A2); "no conclusive outcome either way" against l-BFGS (p. 16) | read |

**No failed replication** of a Fletcher result was found. The nearest thing is the refuted filter/Maratos conjecture (B4), which his own team reported.

---

## F. Era and resource context of the critiques

| Critique | When raised | Context |
|---|---|---|
| DFP conditioning; FR jamming | 1970s–1992 (Powell 1977, 1984, 1986; Nocedal 1992) | Small dense problems. The critique came from analysis of 2-D quadratics plus modest test sets (e.g. a 961-variable minimal surface) |
| BFGS nonconvex counterexamples | 1984 (Powell); 2002 (Dai); 2004 (Mascarenhas) | Pure theory: constructed low-dimensional examples. No practical failure is reported in these sources |
| Maratos / watchdog / SOC | 1978–1982 | Early SQP. Powell's Cambridge group vs Fletcher's Dundee group, which were rival British schools with shared Harwell roots |
| Penalty-parameter heuristics; restoration phase | 2004–2015 | The large-scale NLP era: KNITRO, Ipopt, LOQO, SNOPT, all benchmarked on CUTEr/COPS with performance profiles. The Northwestern group (Nocedal, Byrd, Waltz, Curtis) led the penalty-side answer |
| Filter theory strength; the funnel | 2004–2025 | Namur/RAL (Gould, Toint) inside the collaboration; later Argonne (Leyffer) with Uno |
| LMSD nonconvexity and rate | 2015–2018 | Posthumous for the 2018 paper. Lehigh (Curtis, a Fletcher admirer). Workstation-scale tests up to 10⁶ variables |
| IPM stance; sparsity | Memoir 2025, looking back at the 1970s–2000s | Fletcher's team was rarely more than one PhD student at a time (memoir p. 138). Sparse linear algebra was delegated to students |

---

## Contradictions (kept, not reconciled)

- **C1. Interest in interior-point methods.** Memoir (p. 137): he "had little interest" in IPMs. Brief History (p. 8, co-signed by Fletcher): IPMs "are an attractive alternative to SQP methods". NA/210 (2002): SQP "at present" beats IPMs on MPECs.
- **C2. What the unmodified-SQP evidence shows.** FLT (Brief History, p. 2): "the unmodified SQP method is able to quickly solve a large proportion of test problems", which is the premise for the filter. Wächter & Biegler (preprint p. 23): the full-step option's 86.1% success "might indicate that in many cases Newton's method does not require a safeguarding scheme …, or alternatively, that many problems in the test set are not very difficult."
- **C3. Whether the filter beats penalties.** Wächter & Biegler: the filter is "more robust" than a penalty line search. The penalty school (steering 2008, flexible 2008, infeasibility detection 2010) kept and strengthened penalty-SQP. Fletcher himself says Sl1QP "would still be a competitor with filter methods" (Optima 99, p. 3). No head-to-head benchmark of Sl1QP against filterSQP was found.
- **C4. Strength of filter convergence theory.** Gould & Toint (2008 preprint, p. 29): convergence of every limit point to first-order criticality "has not been established for filter algorithms". Gonzaga, Karas & Vanti (2004 abstract): "for a slightly larger filter, all accumulation points are stationary". The two may be about different classes of filter method. I have not checked this.
- **C5. The filter's future.** Lagrange Prize committee (2006): its importance "will continue to grow". Kiessling, Leyffer & Vanaret (2024): a funnel "slightly outperform[s] its filter counterpart … while being also easier to implement". The memoir (2025): filters are "a key component" of Ipopt. filterSQP 2001 is still a benchmark reference in 2024–26 (Vanaret & Leyffer).
- **C6. Originality of the filter.** Fletcher: "nobody thought of it". Co-authored review: developed "independently of earlier similar ideas". Memoir: Zoppke-Donaldson's unpublished tolerance tubes helped "pave the way" (see B6). Same entry as 01-publications.md contradiction 5, with the memoir and Gould–Toint evidence added.
- **C7. Worst case versus practice (DFP).** Nocedal (1992): DFP "can be made to perform extremely poorly on convex problems", yet it "has never been observed to fail".
- **C8. Date errors in the memoir.**
  - Lagrange Prize: "2012" (memoir pp. 139, 143) against 2006 (Optima 73 citation, p. 5; already recorded as 04-mentorship.md C7).
  - Bi-CGSTAB: "proposed by Henk van der Vorst in the early 1980s" (memoir p. 137), whereas Crossref dates van der Vorst's Bi-CGSTAB paper to 1992 (DOI 10.1137/0913035). The memoir may be thinking of earlier unpublished work. Not resolved.
- **C9. Fletcher-Reeves versus Polak-Ribière.** Nocedal (1992): PR is "in general, substantially more efficient" than FR. Fletcher's own 2009 Table 3: FR needed fewer iterations than PR on the Trigonometric problem (319 vs 558 at n = 50). Table 5: FR failed (> 9999) where PR succeeded.

---

## Gaps (what I could not find or read)

- **Book reviews of *Practical Methods of Optimization*.** Six reviews exist (Crossref-verified):
  - J. E. Dennis Jr., *SIAM Review* 24(1):97–98, 1982, DOI 10.1137/1024028 (vol. 1);
  - T. M. Williams, *J. Oper. Res. Soc.* 33(7):675, 1982, DOI 10.2307/2581735 (vol. 2);
  - R. Tapia, *SIAM Review* 26(1):143–144, 1984, DOI 10.1137/1026027 (vol. 2);
  - W. M. Anderson, *Optimal Control Appl. Methods* 5(2):195, 1984, DOI 10.1002/oca.4660050213 (vol. 2);
  - C. Witzgall, *Math. Comp.* 53(188):768, 1989, DOI 10.2307/2008742 (2nd ed.);
  - Ll. G. Chambers, *Math. Gazette* 85(504):562–563, 2001, DOI 10.2307/3621816 (2nd ed.).

  **None was read**: SIAM and AMS returned 403 or a Cloudflare challenge, and JSTOR needs a login. The zbMATH entries for the book show "contents unavailable due to conflicting licenses". These are the most direct public critiques of his main book → high priority for a user-supplied copy.
- **Springer abstracts and texts** (bot challenge): Powell 1986, Mascarenhas 2004, Ulbrich 2004, Byrd–Gould–Nocedal–Waltz 2004, Benson–Vanderbei–Shanno 2002, Gould–Toint 2010 (the journal version; the preprint was read), Fletcher's own "On the Barzilai-Borwein Method" (2005). For these I used titles and other authors' descriptions only.
- **COPS 3.0 results for FILTER** (Dolan, Moré & Munson 2004): PDF blocked (403 on mcs.anl.gov, 503 on OSTI). Which problems filterSQP failed on is unknown.
- **What the "drawbacks" of the exact augmented Lagrangian were** (memoir p. 134): not named in any source read. Powell's later work "with a student" on it (Optima 99, p. 2) was not identified.
- **Curtis's critical talk** (Optima 99, p. 7): which code and which problem class. Not identified.
- **A benchmark of Sl1QP against filterSQP**, to test Fletcher's claim that Sl1QP "would still be a competitor": none found. Steve Wright's implementation was unpublished, per Fletcher.
- **Replies to Dai & Fletcher's critique of GLL in SPG** by Birgin, Martínez or Raydan: none found. Grippo & Sciandrone's "Nonmonotone Globalization Techniques for the Barzilai-Borwein Gradient Method" (*Comput. Optim. Appl.*, DOI 10.1023/A:1020587701058) surfaced in a search result but was not verified or read.
- **Powell's own views of Fletcher's methods**: the Powell memoir (DOI 10.1098/rsbm.2017.0023) and DAMTP NA2007/03 were unreachable (agent 01). Powell's 1986 and 1984 papers were not read.
- **Referee reports and rejections of Fletcher's papers**: none public. The only refereeing record is his own (B1).
- **An OpenAlex search** for further critiques of the exact penalty line stopped when the shared daily API budget ran out.
- **Interviewer versus interviewee**: in the flat-text copy of Optima 99, some sentences on test problems ("everybody publishes solves with 500 test problems from CUTE") cannot be attributed reliably to Fletcher or to Leyffer. They are not used here.

---

## Sources

Format: title — author(s) — date — identifier/URL — primary or secondary — read status.

1. "Roger Fletcher. 29 January 1939—15 July 2016", *Biogr. Mems Fell. R. Soc.* 78:127–146 — N. I. M. Gould & J. A. J. Hall — 2025 — DOI 10.1098/rsbm.2024.0037 (CC-BY; copy fetched by agent 04 from a Wayback snapshot) — secondary — read pp. 131–143
2. "It's to Solve Problems – An Interview with Roger Fletcher", *Optima* 99, pp. 1–5 — S. Leyffer (interviewer), R. Fletcher — Dec. 2015 — https://www.mathopt.org/optima/99/optima_99.pdf — primary (Fletcher's words) — read
3. "Impressions of Roger's Interview", *Optima* 99, p. 6 — Ph. L. Toint — Dec. 2015 — same PDF — secondary — read
4. "Young Researchers Would Be Wise to Read this Interview!", *Optima* 99, pp. 6–7 — F. E. Curtis — Dec. 2015 — same PDF — secondary — read
5. "Roger Fletcher (1939–2016)", *Optima* 102, p. 6 — J. Nocedal — Apr. 2017 — https://www.mathopt.org/optima/102/optima_102.pdf — secondary — read
6. "An Interview with Roger Fletcher" — Y.-H. Dai — c.2005–06 (*Pac. J. Optim.* 2, 2006) — http://www-optima.amp.i.kyoto-u.ac.jp/ORB/issue22/flectcher_interview.html — primary — read (Q15 used)
7. "A Brief History of Filter Methods", ANL/MCS-P1372-0906 — R. Fletcher, S. Leyffer, Ph. L. Toint — Sept./Oct. 2006 — Optimization Online 2006/10/1489 — primary (co-authored) — read
8. Lagrange Prize 2006 citation, *Optima* 73, p. 5 — MPS/SIAM prize committee (Dennis, Gould, Lewis, Todd) — Jan. 2007 — https://mathopt.zib.de/Optima-Issues/optima73.pdf — secondary — read
9. "A limited memory steepest descent method" (preprint ERGO 09-014; *Math. Program.* 135:413–436, 2012) — R. Fletcher — 2009/2012 — DOI 10.1007/s10107-011-0479-6; Optimization Online 2009/12/2487 — primary — read
10. "Projected Barzilai-Borwein methods for large-scale box-constrained quadratic programming", *Numer. Math.* 100:21–47 — Y.-H. Dai & R. Fletcher — 2005 — DOI 10.1007/s00211-004-0569-y — primary (co-authored) — read (relevant parts)
11. "Numerical experience with solving MPECs as NLPs", Dundee NA/210 (journal: *Optim. Methods Softw.* 19:15–40, 2004) — R. Fletcher & S. Leyffer — 2002/2004 — DOI 10.1080/10556780410001654241 — primary (co-authored) — read (relevant parts)
12. "Theory of algorithms for unconstrained optimization", *Acta Numerica* 1:199–242 — J. Nocedal — 1992 — DOI 10.1017/S0962492900002270; preprint http://users.iems.northwestern.edu/~nocedal/PDFfiles/acta.pdf — secondary — read (§§4–5)
13. "How bad are the BFGS and DFP methods when the objective function is quadratic?", *Math. Program.* 34:34–47 — M. J. D. Powell — 1986 — DOI 10.1007/BF01582161 — secondary — not read (via Nocedal)
14. "Nonconvex minimization calculations and the conjugate gradient method", LNM 1066:122–141 — M. J. D. Powell — 1984 — DOI 10.1007/BFb0099521 — secondary — not read (via Dai 2002)
15. "Restart procedures for the conjugate gradient method", *Math. Program.* 12:241–254 — M. J. D. Powell — 1977 — DOI 10.1007/BF01593790 — secondary — not read (via Nocedal)
16. "Convergence Properties of the BFGS Algoritm" [sic], *SIAM J. Optim.* 13(3):693–701 — Y.-H. Dai — 2002 — DOI 10.1137/S1052623401383455 — secondary — abstract read
17. "The BFGS method with exact line searches fails for non-convex objective functions", *Math. Program.* 99:49–61 — W. F. Mascarenhas — 2004 — DOI 10.1007/s10107-003-0421-7 — secondary — title only
18. "Nonsmooth optimization via quasi-Newton methods", *Math. Program.* 141:135–163 — A. S. Lewis & M. L. Overton — 2013 — DOI 10.1007/s10107-012-0514-2; preprint titled "Nonsmooth optimization via BFGS", https://www.cs.nyu.edu/overton/papers/pdffiles/bfgs_inexactLS.pdf — secondary — introduction read
19. "Descent Property and Global Convergence of the Fletcher—Reeves Method with Inexact Line Search", *IMA J. Numer. Anal.* 5:121–124 — M. Al-Baali — 1985 — DOI 10.1093/imanum/5.1.121 — secondary — not read
20. "Global Convergence Properties of Conjugate Gradient Methods for Optimization", *SIAM J. Optim.* 2:21–42 — J. C. Gilbert & J. Nocedal — 1992 — DOI 10.1137/0802003 — secondary — abstract read
21. "A Theoretical and Experimental Study of the Symmetric Rank-One Update", *SIAM J. Optim.* 3:1–24 — H. F. Khalfan, R. H. Byrd, R. B. Schnabel — 1993 — DOI 10.1137/0803001 — secondary — abstract read
22. "Convergence of quasi-Newton matrices generated by the symmetric rank one update", *Math. Program.* 50:177–195 — A. R. Conn, N. I. M. Gould, Ph. L. Toint — 1991 — DOI 10.1007/BF01594934 — secondary — not read
23. "Global Convergence of a Cass [sic] of Quasi-Newton Methods on Convex Problems", *SIAM J. Numer. Anal.* 24:1171–1190 — R. H. Byrd, J. Nocedal, Y.-X. Yuan — 1987 — DOI 10.1137/0724077 — secondary — not read
24. "The watchdog technique for forcing convergence in algorithms for constrained optimization", *Math. Program. Studies* 16:1–17 — R. M. Chamberlain, M. J. D. Powell, C. Lemaréchal, H. C. Pedersen — 1982 — DOI 10.1007/BFb0120945 — secondary — not read
25. "On the superlinear local convergence of a filter-SQP method", *Math. Program.* 100:217–245 — S. Ulbrich — 2004 — DOI 10.1007/s10107-003-0491-6 — secondary — not read (via Brief History)
26. "Line Search Filter Methods for Nonlinear Programming: Local Convergence", *SIAM J. Optim.* 16:32–48 — A. Wächter & L. T. Biegler — 2005 — DOI 10.1137/S1052623403426544 — secondary — abstract read
27. "On the implementation of an interior-point filter line-search algorithm for large-scale nonlinear programming", *Math. Program.* 106:25–57 — A. Wächter & L. T. Biegler — 2006 — DOI 10.1007/s10107-004-0559-y; preprint https://optimization-online.org/wp-content/uploads/2004/03/836.pdf — secondary — §1 and §4.1 read
28. "Interior-Point Methods for Nonconvex Nonlinear Programming: Filter Methods and Merit Functions", *Comput. Optim. Appl.* 23:257–272 — H. Y. Benson, R. J. Vanderbei, D. F. Shanno — 2002 — DOI 10.1023/A:1020533003783 — secondary — not read
29. "Nonlinear programming without a penalty function or a filter", *Math. Program.* 122:155–196 — N. I. M. Gould & Ph. L. Toint — 2010 (preprint 2 June 2008) — DOI 10.1007/s10107-008-0244-7; https://pure.unamur.be/ws/files/1332682/gt15_MP.pdf — secondary — introduction and §3 comments read
30. "A Globally Convergent Filter Method for Nonlinear Programming", *SIAM J. Optim.* 14:646–669 — C. C. Gonzaga, E. Karas, M. Vanti — 2004 — DOI 10.1137/S1052623401399320 — secondary — abstract read
31. "A filter SQP algorithm without a feasibility restoration phase", *Comput. Appl. Math.* 28(2) — C. Shen, W. Xue, D. Pu — 2009 — DOI 10.1590/s1807-03022009000200003 — secondary — abstract read
32. "A Filter Method with Unified Step Computation for Nonlinear Optimization", *SIAM J. Optim.* 24:175–209 — N. I. M. Gould, Y. Loh, D. P. Robinson — 2014 — DOI 10.1137/130920599 — secondary — abstract read
33. "A Nonmonotone Filter SQP Method: Local Convergence and Numerical Results", *SIAM J. Optim.* 25:1885–1911 — N. I. M. Gould, Y. Loh, D. P. Robinson — 2015 — DOI 10.1137/140996677 — secondary — abstract read
34. "Steering exact penalty methods for nonlinear programming", *Optim. Methods Softw.* 23:197–213 — R. H. Byrd, J. Nocedal, R. A. Waltz — 2008 — DOI 10.1080/10556780701394169 — secondary — abstract read
35. "On the Convergence of Successive Linear-Quadratic Programming Algorithms", *SIAM J. Optim.* 16:471–489 — R. H. Byrd, N. I. M. Gould, J. Nocedal, R. A. Waltz — 2005 — DOI 10.1137/S1052623403426532 — secondary — abstract read
36. "An algorithm for nonlinear optimization using linear programming and equality constrained subproblems", *Math. Program.* 100:27–48 — R. H. Byrd, N. I. M. Gould, J. Nocedal, R. A. Waltz — 2004 — DOI 10.1007/s10107-003-0485-4 — secondary — not read
37. "Flexible penalty functions for nonlinear constrained optimization", *IMA J. Numer. Anal.* 28:749–769 — F. E. Curtis & J. Nocedal — 2008 — DOI 10.1093/imanum/drn003 — secondary — abstract read
38. "Infeasibility Detection and SQP Methods for Nonlinear Optimization", *SIAM J. Optim.* 20:2281–2299 — R. H. Byrd, F. E. Curtis, J. Nocedal — 2010 — DOI 10.1137/080738222; http://coral.ise.lehigh.edu/frankecurtis/files/papers/ByrdCurtNoce10b.pdf — secondary — pp. 2281–2283 and 2298 read
39. "A Unified Funnel Restoration SQP Algorithm" — D. Kiessling, S. Leyffer, C. Vanaret — arXiv 2409.09208 (v1, 13 Sept 2024); *Math. Program.* 217:323–367, 2025, DOI 10.1007/s10107-025-02284-3 — secondary — pp. 2, 11, 20, 24 read
40. "Implementing a unified solver for nonlinearly constrained optimization" — C. Vanaret & S. Leyffer — arXiv 2406.13454 (v2, 9 Nov 2025); *Math. Program. Comput.* 2026, DOI 10.1007/s12532-026-00310-9 — secondary — §7 read
41. "Benchmarking optimization software with COPS 3.0", ANL/MCS-TM-273 — E. D. Dolan, J. J. Moré, T. S. Munson — 2004 — DOI 10.2172/834714 (OSTI) — secondary — abstract only
42. "Handling nonpositive curvature in a limited memory steepest descent method", *IMA J. Numer. Anal.* 36:717–742 — F. E. Curtis & W. Guo — 2016 — DOI 10.1093/imanum/drv034; http://coral.ise.lehigh.edu/frankecurtis/files/papers/CurtGuo16.pdf — secondary — pp. 717–723 and 733 read
43. "R-linear convergence of limited memory steepest descent", *IMA J. Numer. Anal.* 38:720–742 — F. E. Curtis & W. Guo — 2018 — DOI 10.1093/imanum/drx016 — secondary — abstract read
44. "Interior Methods for Mathematical Programs with Complementarity Constraints", *SIAM J. Optim.* 17:52–77 — S. Leyffer, G. López-Calva, J. Nocedal — 2006 — DOI 10.1137/040621065 — secondary — abstract read
45. "Nonmonotone Spectral Projected Gradient Methods on Convex Sets", *SIAM J. Optim.* 10:1196–1211 — E. G. Birgin, J. M. Martínez, M. Raydan — 2000 — DOI 10.1137/S1052623497330963 — secondary — not read
46. "A Nonmonotone Line Search Technique for Newton's Method", *SIAM J. Numer. Anal.* 23:707–716 — L. Grippo, F. Lampariello, S. Lucidi — 1986 — DOI 10.1137/0723046 — secondary — not read
47. "The Barzilai and Borwein Gradient Method for the Large Scale Unconstrained Minimization Problem", *SIAM J. Optim.* 7:26–33 — M. Raydan — 1997 — DOI 10.1137/S1052623494266365 — secondary — not read
48. "A New Class of Augmented Lagrangians in Nonlinear Programming", *SIAM J. Control Optim.* 17:618–628 — G. Di Pillo & L. Grippo — 1979 — DOI 10.1137/0317044 — secondary — abstract read (does not name Fletcher)
49. "Bi-CGSTAB: A Fast and Smoothly Converging Variant of Bi-CG…", *SIAM J. Sci. Stat. Comput.* 13:631–644 — H. A. van der Vorst — 1992 — DOI 10.1137/0913035 — secondary — Crossref metadata only (date check)
50. Fletcher's own papers checked on Crossref for this note — R. Fletcher et al. — primary — bibliographic check:
    - *Math. Program.* 91:239–269 (2002), DOI 10.1007/s101070100244;
    - *SIAM J. Optim.* 13:44–59 (2002), DOI 10.1137/S105262340038081X;
    - *SIAM J. Optim.* 13:635–659 (2002), DOI 10.1137/S1052623499357258;
    - *Math. Program.* 103:541–559 (2005), DOI 10.1007/s10107-004-0516-9;
    - *Comput. Optim. Appl.* 52:583–607 (2012), DOI 10.1007/s10589-011-9430-2;
    - "On the Barzilai-Borwein Method", *Applied Optimization* (2005), DOI 10.1007/0-387-24255-4_10 (not read);
    - LNM 912 (1982), DOI 10.1007/BFb0093144 (chapter not read).
51. Book reviews of *Practical Methods of Optimization* (Dennis 1982; Williams 1982; Tapia 1984; Anderson 1984; Witzgall 1989; Chambers 2001) — DOIs in Gaps — secondary — Crossref metadata only, not read
52. zbMATH Open API records for the book (Zbl 0439.93001, 0474.65043, 0905.65002, 0988.65043) and for FLT 2002 (Zbl 1029.65063, a descriptive review by S. Zlobec) — https://api.zbmath.org — secondary — read (no critique content)
