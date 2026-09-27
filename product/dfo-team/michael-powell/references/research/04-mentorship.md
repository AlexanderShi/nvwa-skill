# 04 · Students, colleagues, memoirs

**Evidence level for this dimension: thin.** Web search found the memorial literature, but no student recollections of how Powell supervised or ran day-to-day work were readable here: WebFetch was blocked for siam.org, the memorial blogspot, tandfonline and the Cambridge hosts. Everything below is either a confirmed bibliographic fact or a search-snippet paraphrase.

---

## 1. Memorial and tribute literature (confirmed to exist)

| Item | Authors | Year / venue | Link | What the snippet says (paraphrase unless quoted) | Cred. |
|---|---|---|---|---|---|
| Royal Society biographical memoir "Michael J. D. Powell. 29 July 1936—19 April 2015" | M. D. Buhmann, R. Fletcher, A. Iserles, P. Toint | Biogr. Mems Fell. R. Soc. 64:341–366 (2018), DOI 10.1098/rsbm.2017.0023 | https://royalsocietypublishing.org/doi/abs/10.1098/rsbm.2017.0023 | Verbatim in the abstract: "a British numerical analyst who was among the pioneers of computational mathematics". Paraphrase: he refused the split between practical algorithm designers and theoreticians; he contributed decisively to making optimization "an effective tool of scientific enquiry"; he also worked on splines and radial basis functions. | secondary |
| Supplementary "M.J.D. Powell's bibliography" | (memoir supplement) | 2018 | https://royalsocietypublishing.org/rsbm/article-supplement/63941/pdf/rsbm20170023supp1/ | Full bibliography. Not read (fetch blocked). | secondary |
| "Obituary for Mike Powell" | C. Cartis, A. Griewank, P. Toint, Y. Yuan | Optimization Methods & Software 30(3), 2015, DOI 10.1080/10556788.2015.1051808 | https://www.tandfonline.com/doi/full/10.1080/10556788.2015.1051808 | Paraphrase: "probably the most influential optimizer in Europe"; contributions include the BFGS convex global-convergence proof and the original augmented-Lagrangian idea; he pioneered trust-region algorithms and proved the first trust-region convergence result (1970). | secondary |
| "Obituaries: Michael J.D. Powell", SIAM News | A. Iserles | 2015 | https://www.siam.org/publications/siam-news/articles/obituaries-michael-jd-powell/ | Paraphrase: one of the giants who established numerical analysis as a discipline; spent seventeen years at AERE Harwell. | secondary |
| "Michael J.D. Powell's work in approximation theory and optimisation" | M. D. Buhmann | J. Approx. Theory 238 (2019) | https://www.sciencedirect.com/science/article/pii/S0021904517301053 | Covers splines (Powell–Sabin split), radial basis functions, unconstrained optimization including "the famous DFP formula". From a conference in his memory at Rauischholzhausen. | secondary |
| *Approximation Theory and Optimization: Tributes to M. J. D. Powell* | eds M. D. Buhmann, A. Iserles | Cambridge University Press, 1997 | https://www.cambridge.org/ca/universitypress/subjects/mathematics/numerical-analysis/approximation-theory-and-optimization-tributes-m-j-d-powell | 60th-birthday volume. Contributors include R. Fletcher, C. de Boor, C. A. Micchelli, **A. R. Conn, K. Scheinberg, Ph. L. Toint**, J. J. Moré, M. J. Todd and Powell himself. | secondary |

## 2. Colleagues and collaborators (confirmed at the level of co-authorship or tribute authorship)
- **Roger Fletcher**: co-author of the DFP line of work (Buhmann 2019 mentions DFP) and co-author of the RS memoir.
- **Arieh Iserles**, **Martin Buhmann**: Cambridge colleagues, editors of the 1997 tributes volume and memoir authors.
- **Philippe Toint**, **Coralia Cartis**, **Andreas Griewank**, **Ya-xiang Yuan**: authors of the OMS obituary. A search snippet also notes a 1984 Powell–Yuan article on ℓp-approximation.
- **Conn, Scheinberg and Toint** wrote in the 1997 tributes volume, so the later DFO trust-region community was engaging directly with Powell's work in his lifetime.

## 3. Succession of the codes (confirmed from primary files)
- The Fortran READMEs record: "The code was sent by Professor Powell to Zaikun Zhang on December 16th, 2013" (NEWUOA, BOBYQA), and on 15 Dec 2013 (LINCOA) [primary: https://github.com/libprima/prima/tree/main/fortran/original].
- Zhang: "Before he passed, Professor Powell had asked me and Professor Nick Gould to maintain his solvers." [secondary: PRIMA README]
- Zhang thanks "Professor Ya-xiang Yuan … for his everlasting encouragement and support" [secondary].

## 4. PhD students
**Not verified.** Memory leads (Ya-xiang Yuan, Martin Buhmann and others as Powell's doctoral students) are recorded as ⚠️ in RESOURCES.md. A Mathematics Genealogy page for Yuan (id 98372) appeared in results, but the snippet did not show the advisor. These names are **not** stated as students in SKILL.md.

## 5. Tacit knowledge that can be recovered
Tacit knowledge that no paper states, recovered from others working through the code [secondary, PRIMA README]:
- "The mission of PRIMA is nontrivial due to the delicacy of Powell's algorithms and the unique style of his code."
- "I hope I am the last one in the world to decode a maze of 244 GOTOs in 7939 lines of Fortran 77 code." Much of Powell's craft (the magic constants 0.1, 0.7, 1.5, 16, 250; the trigger order of model steps vs RHO reduction) lives only in code, not in the papers. *(Inference; the constants themselves are in `newuob.f`, see 03.)*

## 6. Supervision style, group habits, lab culture
**No evidence found.** SKILL.md states in its Honest Boundary that nothing Powell-specific about supervision can be distilled.
