# 04 · Mentorship: students, collaborators and group culture (Philippe L. Toint)

- **Researcher**: Philippe Louis Toint, University of Namur (Unamur, formerly FUNDP), Department of Mathematics, Numerical Analysis Unit and naXys; emeritus since 2016. Living.
- **Dimension**: research agent 04 of 06, students and collaborators: supervision style, group habits, lab culture, tacit knowledge (nuwa research-craft Phase 1; framework §一 layer 7 and §二 agent 4).
- **Research date**: 2026-09-28.
- **Sources consulted**: 36 (numbered S01–S36 under Sources). 27 were read in whole or in the parts cited. 9 were metadata records only (registries, Crossref) or were blocked; each is marked. WebSearch calls used: 2 of 2.
- **Local corpus**: `references/sources/papers`, `essays` and `software` hold only `.gitkeep`. `talks/` holds the ASR transcript of the 2026 podcast that research agent 02 saved in this run. It is **not user-supplied material**, so nothing below is marked "from user-supplied material". `private/` was not opened.
- **Method**: I built the supervision roster from the Mathematics Genealogy Project (MGP) and theses.fr. For each student I looked for the other side of the relationship: the thesis itself (jury page, acknowledgements, software chapter), the joint papers (Crossref), and the student's later web page. Seven thesis full texts turned out to be open through CORE (the Namur repository feeds it). HAL and the Namur portal's own list pages were blocked (see Gaps).

**Tags.** [stated] = Toint's own words, alone or co-authored. [practice] = what the record shows he or his group did (theses, papers, juries, code). [observed] = what someone else says about him or his group. [inferred] = my reading; no source says it. Each item is also marked **primary** (Toint's own text or record) or **secondary** (someone else's account). Everything a student or collaborator says about him is secondary by definition. That includes first-hand thesis acknowledgements, which the framework ranks high.

**Quoting conventions.** French passages are quoted verbatim. Line-break hyphens from PDF extraction are rejoined; nothing else is changed; "[sic]" marks original spellings. English renderings are my translations. They are given in *italics* and never inside quotation marks. "PDF p." is the page of the PDF file I read, not the printed folio. Podcast quotes come from an **automatic speech-recognition transcript that no human has checked** (see its header). Timestamps are given, and I say which model produced each wording.

---

## 0. Read this first: what kind of mentor the record shows

- **A real doctoral school, not a lone researcher.** MGP lists **20 doctoral students (1985–2015)**, 18 at Namur plus 2 external co-advisings (Trier 2002, Erlangen 2011), with 49 descendants [S09]. theses.fr adds two Toulouse theses he co-directed that MGP lacks (Tröltzsch 2011, Gürol 2013) [S10]. After retirement there is one more informal case: Jerad (Toulouse, 2024) is formally Gratton's student, but Toint sat on the jury and co-authored 7 of his papers [S10][S08]. [practice, secondary registries + primary papers]
- **Students describe a consistent style**, in seven thesis acknowledgements from 2004 to 2014 [S12–S18]: trust and freedom to choose, a steady supply of ideas, and sending students to conferences where he introduces them to people. It is the same pattern Toint describes receiving from Powell (§5). [observed, secondary; the lineage link is inferred]
- **The group transmits a craft, and the theses show it**: write a package, release it inside GALAHAD, document it in GALAHAD format, build a test library when none exists, compare against the in-house production code, report with performance profiles, choose defaults by systematic variant tests, and end with an application (§4). [practice, from the theses]
- **What is missing**: Toint's own statements about how he supervises; any student recollection outside a thesis acknowledgement (no blog, memoir, Festschrift or interview found); and any account of friction or failure in supervision. Acknowledgements are a genre of praise, so the positive picture in §2 carries a selection bias (§10, §11).

---

## 1. The record: who trained with him, on what, with whom

### 1.1 Doctoral students (formal)

Sources: MGP [S09] for name, year, title and advisors; theses.fr [S10] for the Toulouse theses; jury pages from the thesis PDFs I read [S12–S18]; joint papers from Crossref queries in this run [S08] (only DOIs Crossref returned with both names).

| Year | Student | Thesis (as MGP or theses.fr gives it) | Co-advisor(s) | Joint papers with Toint (DOI, checked) | Notes |
|---|---|---|---|---|---|
| 1985 | Pierre Manneback | Solution of Large-Scale Linear Least-Squares Problems | — | IMA JNA 5(2) 1985, 10.1093/imanum/5.2.221 (with Murigande); SISSC 1986, 10.1137/0907053 (with **Golub**) | 2 descendants [S09] |
| 1986 | Charles Murigande | Linear Least-Squares in Geodesy | — | 10.1093/imanum/5.2.221; Bull. Géodésique 1986, 10.1007/bf02522339 | Applied geodesy |
| 1989 | Marc Lescrenier | Trust-Region Methods and Degenerate Problems | — | Int. J. Supercomputer Appl. 1988, 10.1177/109434208800200105 (FPS 164 and Cray X-MP vector processors); chapter with **Conn & Gould** 1994, 10.1007/978-94-015-8330-5_6 | Joined CGT work |
| 1991 | Annick Sartenaer | On Some Strategies for Handling Constraints in Nonlinear Optimization | — | 8 papers, 3 with **Conn & Gould** (SIOPT 1993, 10.1137/0803009; SIOPT 1996 ×2, 10.1137/s1052623492236481, 10.1137/s1052623493251463) | Stayed at Namur; later co-supervised Orban, sat on juries, supervised Tshimanga [S09][S10] |
| 1991 | Daniel Tuyttens | Large-Scale Nonlinear Network Optimization | — | Math. Prog. 1990, 10.1007/bf01582254; **LSNNO** Fortran code, ACM TOMS 1992, 10.1145/131766.131771 | Student thesis → published software |
| 1992 | Christophe Sebudandi | Trust-Region Methods in Inverse Problems of Seismology | — | Geophys. J. Int. 1993, 10.1111/j.1365-246x.1993.tb01502.x | Application domain |
| 1993 | Didier Burton | Inverse Shortest Paths Problems | — | Math. Prog. 1992, 10.1007/bf01585693; 1994, 10.1007/bf01582056; LNEMS 1997 (with Pulleyblank), 10.1007/978-3-642-59179-2_8 | |
| 1996 | Michel Bierlaire | Mathematical Models for Transportation Demand Analysis | — | LAA 1991 (with Tuyttens), 10.1016/0024-3795(91)90009-l; MEUSE OD estimator "that exploits structure", Transp. Res. B 1995, 10.1016/0191-2615(94)00025-u; Transp. Sci. 1997, 10.1287/trsc.31.4.363 | EPFL page: "Dirigée par Prof. Philippe Toint"; principal developer of the free software Biogeme [S20]; 25 descendants [S09] |
| 2001 | Dominique Orban | Interior-point Methods for Nonlinear Programming (INPT: *Méthodes de points intérieurs pour l'optimisation non-linéaire*) | Daydé (MGP); Sartenaer and Daydé (theses.fr) | 9 papers, incl. **GALAHAD** (TOMS 2003, 10.1145/962437.962438), **CUTEr** (10.1145/962437.962439), **CUTEst** (COAP 2015, 10.1007/s10589-014-9687-3), with Conn & Gould 2000 (10.1007/s101070050112) | Toulouse–Namur thesis; later on Tomanos's jury [S13] |
| 2002 | Michaela Schulze (Trier) | Parameter Identification for Underdetermined Systems … [MGP title with typos] | **Sachs** (advisor 1) | none found | External co-advisor |
| 2003 | Benoît Colson | Trust-Region Algorithms for Derivative-Free Optimization and Nonlinear Bilevel Programming | **Savard** | Optim. Eng. 2001, 10.1023/a:1016090421852; Applied Optim. 2002, 10.1007/978-1-4613-0263-6_7; OMS 2005, 10.1080/10556780500140227 | Partial separability carried over to DFO |
| 2004 | Fabian Bastin | Trust-Region Algorithms for Nonlinear Stochastic Programming and Mixed Logit Models | **Louveaux** | 6 papers, e.g. Math. Prog. 2006, 10.1007/s10107-006-0708-6; Transp. Sci. 2010, 10.1287/trsc.1100.0321 | Thesis software AMLET [S17] |
| 2007 | Caroline Sainvitu | Filter-Trust-Region Methods for Nonlinear Optimization | — | with **Gould**, SIOPT 2005, 10.1137/040603851; OMS 2007, 10.1080/10556780701322970 | Gould on the jury [S14]; solo RAIRO paper 2009, 10.1051/ro/2009016 |
| 2009 | Mélodie Mouffe | Multilevel Optimization in Infinity-Norm and Associated Stopping Criteria | **Gratton** (joint INPT–FUNDP degree) | IMA JNA 2008, 10.1093/imanum/drn034; Math. Prog. 2010 (online 2008), 10.1007/s10107-008-0258-1; OMS 2010 (online 2009), 10.1080/10556780903239295; Numer. Math. 2011, 10.1007/s00211-011-0376-1 | Thesis at CERFACS [S16] |
| 2009 | Dimitri Tomanos | Algorithms and Software for Multilevel Nonlinear Optimization | — | 10.1007/s10107-008-0258-1; OMS 2009, 10.1080/10556780802571467; 10.1080/10556780903239295 | Wrote the GALAHAD package RMTR [S13] |
| 2009 | Melissa Weber Mendonça | Multilevel Optimization: Convergence Theory, Algorithms and Application to Derivative-free Optimization | — | 10.1093/imanum/drn034; 10.1080/10556780802571467 | "advised by Professor Philippe Toint"; then 9 years a professor at UFSC; now at Quansight, working on NumPy, SciPy and other open-source projects [S19] |
| 2010 | Vincent Malmedy | Hessian Approximation In Multilevel Nonlinear Optimization | — (thesis committee: Gratton, Sartenaer, Toint) | 10.1007/s10107-008-0258-1; COAP 2010, 10.1007/s10589-010-9317-7; COAP 2011, 10.1007/s10589-011-9393-3; OMS 2014, 10.1080/10556788.2014.971025 | Took over RMTR, wrote LTS [S12] |
| 2011 | Alexander Thekale (Erlangen) | Trust-Region Methods for Simulation Based Nonlinear [title truncated in MGP] | **Klamroth, Leugering** (advisors 1–2) | none found | External co-advisor |
| 2011 | Anke Tröltzsch (INPT; not in MGP) | An active-set trust-region method for bound-constrained nonlinear optimization without derivatives applied to noisy aerodynamic design problems | **Gratton** (director), Toint co-director | OMS 2011, 10.1080/10556788.2010.549231 | Airbus application; Airbus engineer on the jury [S18] |
| 2013 | Selime Gürol (INPT; not in MGP) | Solving regularized nonlinear least-squares problem in dual space with application to variational data assimilation | **Gratton** | COAP 2012, 10.1007/s10589-012-9478-7; QJRMS 2018 ×2, 10.1002/qj.3262, 10.1002/qj.3355 | Thesis full text not read |
| 2014 | Johan Barthélemy | A parallelized micro-simulation platform for population and mobility behaviour – Application to Belgium | **Cornelis** | Transp. Sci. 2013, 10.1287/trsc.1120.0408 | Transport; last Namur transport PhD found [S15] |
| 2015 | Phillipe Rodrigues Sampaio | A trust-region method for constrained derivative-free optimization and worst-case evaluation complexity of non-monotone gradient-related algorithms … | — | with **Cartis**, Optimization 2015 (online 2014), 10.1080/02331934.2013.869809; COAP 2015, 10.1007/s10589-014-9715-3; OMS 2016, 10.1080/10556788.2015.1135919 | Last MGP student before retirement (2016) |

### 1.2 Informal and adjacent

- **Sadok Jerad** (Toulouse, defended 19 Jan 2024). theses.fr lists **Gratton as sole director**. The jury was Gratton, Bellavia (president), Toint, Bolte, **Frank E. Curtis** and E. Simon, with Krause and **Cartis** as referees [S10]. Crossref returns 7 Gratton–Jerad–Toint papers from 2023 to 2026, e.g. SIOPT 2023, 10.1137/22m1499522, and EJCO 2026, 10.1016/j.ejco.2026.100128 [S08]. Agent 03 found Toint thanking Jerad "for his careful reading of the manuscript" (arXiv:2105.07765 v3; see `03-process-evidence.md` §6). [practice, primary + secondary] The formal and the working relationships differ; see Contradiction K3.
- **Jean Tshimanga (Ilunga)**, Namur 2007, is Sartenaer's student in MGP. He wrote two papers with Gratton and Toint: SIMAX 2011, 10.1137/090780493, and QJRMS 2013, 10.1002/qj.2050 [S08]. A second-generation student works with the first generation's advisor. [practice]
- **Postdocs and junior co-authors** are not covered by MGP and were not traced systematically: Porcelli, Bastin after 2004, Cirillo, and E. Simon. Gap.

### 1.3 Patterns in the record [practice unless marked]

1. **The thesis topic is a branch of Toint's own programme at that moment.** Trust-region and structure theses come in 1989–93, while CGT/LANCELOT is being built. Transport theses (1996, 2004, 2014) track the Transportation Research Group. Interior points (2001) and DFO (2003) come in the GALAHAD/DFO years. Filter trust region (2007) comes after the filter papers. Four multilevel theses (2009–10) follow the recursive trust-region paper (Gratton, Sartenaer & Toint, SIOPT 2008, 10.1137/050623012). Complexity (2015) and OFFO (Jerad 2024) come in the complexity era. Compare with the students' own statements of freedom (§2, Contradiction K1).
2. **A domain co-advisor whenever the thesis leaves core NLP.** Stochastic programming with Louveaux, bilevel programming with Savard, transport with Cornelis, multigrid, data assimilation and aerodynamics with Gratton at CERFACS. In the Trier and Erlangen theses he is the NLP co-advisor to someone else's student.
3. **Students are brought into the senior network early.** He writes that his joint papers with Conn include "eight with Annick Sartenaer and three with Dominique Orban" [S03 p. 9, stated, primary]. Lescrenier co-authored with Conn and Gould (1994); Sainvitu with Gould (2005), who also sat on her jury; Manneback with Golub (1986); Sampaio with Cartis (2015).
4. **Former students become the next cohort's co-supervisors and examiners.** Sartenaer (PhD 1991) co-directed Orban's thesis (theses.fr), sat on the Bastin, Sainvitu, Tomanos, Mouffe and Malmedy juries, and was on Malmedy's thesis committee [S10][S12–S17]. Orban (PhD 2001) examined Tomanos (2009) [S13] and, by Sainvitu's account, invited her several times to present at conferences [S14].
5. **Cohorts, not isolated students (2007–2011).** "A retrospective trust-region method for unconstrained optimization" (Math. Prog. 2010, online 2008, 10.1007/s10107-008-0258-1) has five authors. Four are Namur students or ex-students (Bastin, Malmedy, Mouffe, Tomanos) and Toint is the fifth. Malmedy calls it "our first contribution" (see §4, T6). The multilevel papers mix the same people with Gratton and Sartenaer [S08].
6. **Two-author student papers carry the thesis.** Toint–Tuyttens, Burton–Toint, Sebudandi–Toint, Colson–Toint, Sainvitu–Toint, Malmedy–Toint, Sampaio–Toint. These follow the field's alphabetical order; `01-publications.md` §1 shows that author order carries no role signal here.
7. **Students' later careers repeat the software-as-public-good pattern.** [inferred from verified facts] Orban co-authored CUTEr, CUTEst and GALAHAD. Bierlaire is "le principal développeur de Biogeme, un logiciel libre largement utilisé" [S20] (*the main developer of Biogeme, a widely used free software*). Weber Mendonça works at Quansight and, in her words, dedicates her time "to NumPy, SciPy and other open-source projects" [S19]. Whether this comes from the Namur training or from self-selection cannot be told from these sources.

---

## 2. Supervision style, as students describe it (thesis acknowledgements)

All items are [observed, secondary], first-hand student accounts from the acknowledgement pages of seven theses read in this run. **Genre caveat:** acknowledgements thank; they do not criticise. Read the convergences, not the superlatives.

**A1. Guidance mixed with autonomy, and a flow of ideas.** According to Vincent Malmedy (PhD 2010) [S12, PDF p. 6]:
> "Merci d'avoir toujours su m'orienter sur de nouvelles pistes, tel un geyser d'idées, tout en me laissant de l'espace pour faire mes propres choix, dans un subtil mélange de guidance et d'autonomie."

*Thank you for always pointing me to new leads, like a geyser of ideas, while leaving me room to make my own choices, in a subtle mix of guidance and autonomy.* He also dates the involvement: "depuis nos premières rencontres pour esquisser un projet de thèse jusqu'à ces derniers jours pour peaufiner ce document" (*from our first meetings to sketch a thesis project until these last days polishing this document*).

**A2. Freedom to steer by affinity; enthusiasm passed on.** According to Dimitri Tomanos (PhD 2009) [S13, PDF p. 6]:
> "pour son encadrement ainsi que pour son engouement pour la recherche qu'il a pu me transmettre lors de ces années de collaboration"
> "pour m'avoir toujours permis d'orienter ma recherche selon mes affinités"

*For his supervision and for the enthusiasm for research he was able to pass on to me during these years of collaboration. For always letting me orient my research according to my affinities.* Note that he calls the years "de collaboration", not of supervision.

**A3. Trust and freedom.** According to Johan Barthélemy (PhD 2014, co-supervised with Cornelis) [S15, PDF p. 6]:
> "pour leur encadrement, la confiance qu'ils m'ont accordée et la liberté qu'ils m'ont laissée tout au long de ce travail. Les discussions que nous avons eues ensemble ainsi que leurs conseils et leurs avis éclairés m'ont toujours permis de trouver une solution à chacun des problèmes rencontrés."

*For their supervision, the trust they placed in me and the freedom they left me throughout this work. Our discussions, their advice and informed opinions always let me find a solution to each problem I met.* The praise is addressed to both promoteurs jointly.

**A4. Trust that held in hard times.** According to Fabian Bastin (PhD 2004) [S17, PDF p. 6]:
> "pour la confiance qu'il n'a cessé de m'accorder, même dans les moments difficiles, et les encouragements qui m'ont permis de produire la présente thèse."

*For the trust he never stopped giving me, even in difficult moments, and the encouragement that let me produce this thesis.* Bastin started in the Transportation Research Group (GRT) and then moved to the Numerical Analysis Unit: "qui m'a donné la chance de travailler au sein du Groupe de Recherche sur les Transports (GRT), puis au sein de l'Unité d'Analyse Numérique".

**A5. Constant support, many pieces of advice.** According to Caroline Sainvitu (PhD 2007) [S14, PDF p. 6]:
> "pour m'avoir acceuillie [sic] au sein de l'Unité d'Analyse Numérique ainsi que pour son encadrement, ses nombreux conseils et son soutien constant tout au long de cette thèse."

**A6. "Challenging".** According to Anke Tröltzsch (INPT 2011, co-directed with Gratton) [S18, PDF p. 9]:
> "First of all, I want to thank my advisors, Serge Gratton and Philippe L. Toint, for four years of teaching, mentoring, and challenging me."

It is the only acknowledgement that uses a word for pressure, and it is addressed to both advisors jointly.

**A7. Time and advice (brief).** According to Mélodie Mouffe (INPT–FUNDP 2009, co-directed with Gratton) [S16, PDF p. 5]:
> "Je souhaite remercier tout d'abord mes directeurs de thèse, Serge Gratton et Philippe Toint pour le temps et les conseils qu'ils m'ont donnés tout au long de la thèse."

She credits Iain Duff, not Toint, for the thesis opportunity itself: "Iain Duff pour m'avoir donné la chance de réaliser cette thèse".

**A8. Conferences, and being introduced to people.** This is the most repeated item, in four of seven acknowledgements:
- Malmedy: "Merci enfin de m'avoir donné l'opportunité de participer à plusieurs conférences nationales et internationales, au cours desquelles j'ai pu présenter mes travaux et en discuter avec plusieurs chercheurs." [S12, PDF p. 6]
- Tomanos: "de m'avoir donné l'opportunité de participer à plusieurs conférences internationales et de m'y avoir fait rencontrer plusieurs chercheurs et professeurs avec lesquels j'ai pu avoir des discussions très intéressantes." [S13, PDF p. 6] The phrase *m'y avoir fait rencontrer* means *made me meet*; reading it as Toint actively introducing him is [inferred].
- Sainvitu: "Ce fut pour moi une chance d'y présenter à chaque fois notre travail et d'y rencontrer de nombreux chercheurs." [S14, PDF p. 6] She says she presented *notre travail* (*our work*) each time.
- Barthélemy: "Grâce à eux, j'ai pu côtoyer de nombreuses personnes intéressantes à travers le monde" [S15, PDF p. 6].

**Convergence count** [inferred from A1–A8]: conferences and introductions in 4 of 7 accounts; freedom, autonomy or orienting by affinity in 3 (Malmedy, Tomanos, Barthélemy); trust in 2 (Bastin, Barthélemy); "welcomed into the Numerical Analysis Unit" in 2 (Sainvitu, Malmedy: "Merci d'abord de m'avoir accueilli au sein de l'équipe d'Analyse numérique"). No account mentions weekly meetings, deadlines, reading drafts line by line, or harshness. Their **absence is not evidence** that these did not happen.

---

## 3. Group habits and lab culture

**G1. The Numerical Analysis Unit had about ten junior researchers around 2010 (PhD students and postdocs; roles not stated).** [practice, secondary] Malmedy lists his "collègues scientifiques de l'équipe d'Analyse numérique": Dujol, Gürol, Laloyaux, Legrain, Porcelli, Sainvitu, Tannier, Tomanos, Tshimanga Ilunga, Wanufelle and Weber Mendonça, eleven names [S12, PDF p. 7]. Tomanos's 2009 list is similar [S13, PDF p. 6]. Toint had been "co-director of the Numerical Analysis Unit" since 1979, per the Edinburgh appointment notice [S22]. It does not name the other co-director.

**G2. A named sub-team with seniors who mentor juniors.** [observed, secondary] Malmedy thanks "Dimitri Tomanos et Melissa Weber Mendonça, mes aînés dans l'équipe « multiniveaux »" and adds "Un merci tout particulier à Dimitri pour m'avoir guidé dans l'écriture de logiciels scientifiques et pour la collaboration étroite que nous avons menée en la matière." [S12, PDF p. 6]. *Special thanks to Dimitri for guiding me in writing scientific software.* So the software craft was passed on **student to student**, not only from Toint. Sainvitu says the same of an earlier senior: "Benoît Colson, qui fut toujours présent dans les moments de doutes" [S14, PDF p. 6].

**G3. A formal thesis committee that follows the thesis for four years.** [observed, secondary] According to Malmedy: "mon comité d'accompagnement, qui ont suivi mon travail de thèse durant ces quatre années et se sont assurés que je ne me fourvoyais point : Serge Gratton, Annick Sartenaer et Philippe Toint." [S12, PDF p. 6] *The committee made sure I did not go astray.* The committee included the external partner (Gratton), not only Namur staff.

**G4. Research stays in partner labs as part of the thesis.** [observed, secondary]
- Malmedy spent three months at CERFACS: "de m'avoir accueilli trois mois dans l'équipe Parallel Algorithms du CERFACS" (thanking Duff, Gratton and Vasseur) [S12, PDF p. 7].
- Mouffe's and Tröltzsch's theses were done at CERFACS [S16][S18].
- Barthélemy had a 2012 research stay at SMART, which later hired him [S15, PDF p. 7].
- This matches the long-stay model Toint describes for himself in his 2010 ADTAO talk: `02-methodology.md` O2 records the planned output "une nouvelle thèse et un post-doctorat en cours". I did not re-read that source.

**G5. Funding: individual national fellowships.** [practice] Bastin was an FNRS "aspirant" [S17, PDF p. 6]. Tomanos had an FRIA grant, a fund for research training in industry and agriculture, and his thesis ends with an industrial progressive-lens application [S13, PDF pp. 4, 6]. Malmedy was funded by FNRS [S12, PDF p. 7]. [inferred] Individual fellowships give students some independence of topic, which fits A1–A3.

**G6. Durations.** [practice, secondary] Sainvitu: "ces cinq années" [S14]. Tomanos: "ces quatre années" [S13]. Malmedy: four years of committee follow-up [S12]. Tröltzsch: "four years" [S18]. Barthélemy: "près de six ans et demi" [S15, PDF p. 6].

**G7. Social texture.** [observed, secondary] The accounts mention shared offices, morning coffee, lunches, whist games and conferences as social events ("plusieurs conférences mémorables", Tomanos [S13]). The transport students sat in "le grand bureau du GRT" (Barthélemy [S15, PDF p. 7]). Nothing here is specific to Toint. It is recorded as the unit's culture.

**G8. The jury mixes insiders, the external partner, a former student and a rival-school expert.** [practice] Examples: Sainvitu's jury had Gould and Vicente [S14]; Tomanos's had Orban and Gratton [S13]; Malmedy's had Diehl [S12]; Bastin's had Bierlaire (an ex-student) and Polak [S17]; Tröltzsch's had Vicente, Gilbert and an Airbus engineer [S18]. [inferred] The jury is used to connect the student to people they will work with.

---

## 4. Tacit knowledge: what the students all do that no paper states as a rule

Each item is visible in at least two theses. All are [practice] from the thesis texts [S12–S18]; the "rule" wording is [inferred].

**T1. A thesis ships a released package, inside GALAHAD, documented to GALAHAD conventions.**
- Tomanos: "It was thus decided to construct a software implementing the RMTR∞ algorithm. The package, called RMTR, has been programmed in Fortran 95 and has been made available to the community as a part of the GALAHAD library of packages" [S13, PDF p. 99].
- Malmedy: Chapter 8 "The RMTR and LTS packages" is "devoted to the software engineering that took place during this thesis", on "two software packages that are made publicly available through the GALAHAD library" [S12, PDF p. 200]. His appendices D–E are full package specifications with sections such as "The GALAHAD symbols", "The derived data types", "Argument lists and calling sequences", "Warning and error messages" and "The control and problem specification files" [S12, PDF pp. 13–14, contents].
- Bastin: "notre logiciel AMLET, écrit pour les besoins" [S17, PDF p. 4] (*our software AMLET, written for the purpose*). Tuyttens: LSNNO published in ACM TOMS (10.1145/131766.131771).
- Rule: the software is part of the thesis, not an extra.

**T2. Code is handed from student to student, with maintenance duties.** Malmedy: "The development of the RMTR code was mainly conducted by Dimitri Tomanos. Our contribution to this package consists in its adaptation for use with the LTS package, the improved facilities to define the grids … the fixing of some bugs and the addition of some minor features. The code and documentation maintenance has also been carried out since mid-2009." [S12, PDF p. 200]. Rule: the next student inherits, fixes and maintains the previous student's code, and says exactly what they added.

**T3. When the problem class is new, build its test library first.** Tomanos: "A library of test problems has also been constructed on which we have tested our software." [S13, PDF p. 4]. Among his contributions: "a library of test problems for testing the multilevel algorithms" [S13, PDF p. 122]. Tröltzsch: "To report numerical experiments incorporating noise, we create a test set of noisy problems by adding perturbations to the set of smooth problems. The choice of noisy problems was guided by a desire to mimic simulation-based optimization problems." [S18, PDF p. 7]. [inferred] This is the CUTE origin story repeated at thesis scale: CUTE came "from the need to perform extensive and documented testing on the LANCELOT package" (`02-methodology.md` E1).

**T4. Compare against the house's production code, on the house's test set, with performance profiles.**
- Sainvitu: "Numerical comparisons of our software with LANCELOT-B will be given in Section 5.4, attesting the reliability and the efficiency of our method" [S14, PDF p. 88]. Its testing environment (§5.1) is "the CUTEr (Constrained and Unconstrained Testing Environment, revisited) set of test problem" [sic] [S14, PDF p. 88].
- Tomanos: "In the past, mathematicians used tables of results of their algorithms on the tested problems. However, this strategy may be difficult to use if the number of problems is large. Dolan and Moré (2002) have introduced the notion of performance profiles that we use in this thesis" [S13, PDF p. 41].
- Performance profiles are a section of the basics chapter in both Tomanos (§1.5.2) and Malmedy (§1.5) [S12, S13 contents].
- Tröltzsch tests on "the CUTEr collection" [S18, PDF p. 7].
- The house tools cross into other domains. The transport thesis solves its synthetic-population fitting problem "using an augmented Lagrangian algorithm, as implemented in the (freely available) LANCELOT package", with the SIF file printed as an appendix [S15, PDF pp. 33, 144].

**T5. Choose defaults by systematic variant tests, and say so.** In the cohort paper Gratton, Mouffe, Sartenaer, Toint & Tomanos (report 08/10; OMS 2010, 10.1080/10556780903239295) [S07]:
> "In view of this conclusion, we therefore select the the [sic] Galerkin model as our default and restrict further analysis to this case." (PDF p. 13)
> "As a conclusion of this analysis, we decided to select the defaults as the use of the Galerkin model, 7 smoothing cycles per Taylor iteration, a value of κχ = 1/4, V-form iterations and the (3.26) termination rule." (PDF p. 15)

The same text reports "a substantial spread of the results, with some options being up to fifteen times worse than others" (PDF p. 13). [practice, primary] Rule: a package's defaults are a research result, obtained on a test set and reported. `03-process-evidence.md` §1.5 has more on setting constants.

**T6. A newcomer's first result is a group paper.** Malmedy: "We now present a variant of the trust-region method that we developed in collaboration with Fabian Bastin, Mélodie Mouffe, Philippe Toint and Dimitri Tomanos. This constitutes our first contribution." [S12, PDF p. 63]. Tomanos's thesis lists the same paper among his contributions [S13, PDF p. 122]. [inferred] Onboarding happens through a shared problem, not a solitary warm-up.

**T7. The thesis ends in an application outside mathematics.** Progressive lenses (Tomanos [S13, PDF p. 4]); snake-skin pigmentation patterns (Malmedy [S12, PDF p. 4]); an Airbus wing-shape design problem (Tröltzsch [S18, PDF p. 7]); variational data assimilation (Gürol, title [S10]); Belgian population and mobility (Barthélemy [S15]); mixed logit estimation (Bastin [S17]). Sainvitu's thesis is the exception: its abstract reports only comparisons with "more classical trust-region algorithms" and names no application [S14, PDF p. 4; abstract only for this point]. [inferred] This fits his stated view that applications are "the source of … methodological inspiration" (`02-methodology.md` P6).

**T8. Question-style titles travel to students.** [inferred, weak] Sainvitu's solo paper is "How much do approximate derivatives hurt filter methods?" (RAIRO-OR 2009, 10.1051/ro/2009016). Toint's own talks and the Cartis–Gould–Toint survey use the same form ("How much patience do you have?", Optima 88, 2012; per Cartis CV [S24, PDF p. 4]). One instance only.

---

## 5. His own account: how he was mentored, and what he values in mentors

**M1. Daily contact and high standards (Powell).** [stated, primary; ASR, medium model] "We spent for instance lunchtime together in the Gratz [grad] Center having lunch every day and discussing my progress or my lack of progress. That was quite challenging for me, and I learned a lot from that." [0:22:05–0:22:19]. And: "he was a very person with very high standards for everybody, including himself, but also for his students." [0:24:52–0:25:01] [S01]

**M2. No vagueness allowed, and that is how you learn.** [stated, primary; ASR, medium model] "He didn't let vagueness hang around. If you had a vague idea, that didn't fit with his view of things. The ideas had to be precise and the result had to be verified … And for young students, that is sometimes difficult, but I guess that's how you learn." [0:26:31–0:27:01] [S01; also `02-methodology.md` T6]

**M3. Hard to convince, then your best advocate, who introduces you at conferences.** [stated, primary; ASR, small model, not re-run] "Also, Mike was hard to convince about the new stuff. But once he was convinced, he was your best advocate. That was very helpful. And in later conferences, he would introduce me to other people and mention my results and be very positive about it. So that definitely helped me quite a lot." [0:30:46–0:31:06] [S01]. On his first result: Powell had a visitor in the room (Davidon), "And so Mike told me that I have to explain my result to both of them. And Bill was quite enthusiastic about the results. So that helped me too" [0:30:03–0:30:23].
- [inferred] **This is the same behaviour his students thank him for** (A8: conferences, being introduced to researchers). The lineage is supported on both sides: Toint's account of Powell, and his students' accounts of him. That it is a *conscious* imitation is not stated anywhere.

**M4. The co-authored memoir's version.** [stated, co-authored, primary] Powell's interest in large problems "led him to suggest this research topic to a young PhD student, Philippe Toint, who arrived in Cambridge from Belgium on Royal Society's funding in January 1977 … His interactions with that student were constant … While the subject of sparse quasi-Newton methods was eventually developed mostly by Toint, it also involved Mike in three interesting contributions" [S02, preprint PDF p. 14]. So the advisor chose the topic, stayed in constant contact, and let the student own the result. The same memoir's general paragraph on Powell's students ("His research time was precious – but never too important to listen to them, discuss their ideas and read their work. While Mike could be abrupt with colleagues, his patience with students was exemplary.", PDF p. 11) belongs to a passage built on Iserles's recollections. It is co-signed by Toint but cannot be assigned to him alone.

**M5. What he values in a senior colleague: supporting young people.** [stated, primary] About Conn, whom he met "as a fresh PhD" in 1979 and who invited him to stay at his home: "This was, for me, the first manifestation of several of Andy's qualities: continued supportive interest in young people, hospitality and generosity." [S03, V&N 27(2) 2019, p. 9].

**M6. Credit disputes with another group's student.** [stated, primary; ASR, small model] He got the sparse quasi-Newton result before a student of John Dennis. Powell "wrote to them a letter saying that, well, that was life and that, and you know, I was a nice guy and I could understand that somebody else was working on the topic, which of course I did. And I was quite pleased to meet the other guy in the conference a year after that." [0:27:57–0:28:27] [S01]. [inferred] The advisor handled the priority friction on the student's behalf. There is no evidence of how Toint handled such cases for his own students.

**M7. Students and AI: use it, responsibly and transparently.** [stated, primary; ASR, medium model for the key sentence] "I think preventing them to get access to AI is a real gap models [ASR garble], I think. So it doesn't make much sense. But we should teach them how to use AI efficiently and responsibly." Then: "you're responsible for what you write, not a machine is responsible, you are responsible. And so you better check what you say is correct and meaningful." [1:05:27–1:06:25] [S01; also `02-methodology.md` W6]

**M8. Message to young researchers.** [stated, primary; ASR, small model] Quoting John Dennis: "today is the best time ever to be an optimizer because the field has seen this incredible increase in popularity, in relevance, in activity. So never a better time to be an optimizer than now." [1:09:40–1:10:04] [S01]

**M9. What he does *not* talk about.** [practice, primary] In the 71-minute interview he never discusses his own doctoral students, how he chooses their topics, or how he runs a group. The only group he says he founded is the transport one: "I created a little group of people in my university who were interested in transportation" [0:56:38–0:56:50] [S01]. The host did not ask, so this absence carries little weight.

**M10. As MOS chair, recruiting students into the society.** [stated, primary, minor] "Please suggest MOS membership to your colleagues and students." (Optima 85, April 2011, p. 1) [S04]

---

## 6. What collaborators say about him

**C1. Gould (collaborator since the 1980s).** [observed, secondary] Preface of Gould's course booklet: "And of course to Philippe Toint, without whom my journey through optimization would have been much the poorer, and whose words and deeds have truly been an inspiration." [S23, PDF p. 8; verified in this run, first found by the Gould agent]. His 2019 postscript to Toint's Conn memoir adds only "I share every sentiment that Philippe describes" [S03 p. 10].

**C2. Cartis (collaborator since 2007).** [observed, secondary] "The papers with Gould and Toint are a long term collaboration, with equal contributions. Authors names on papers typically appear alphabetically as it is common in mathematics." [S24, PDF p. 1]. She organised his 2015 Leverhulme and Oliver Smithies lectures at Balliol, "that popularized top quality research in optimization … to a wider audience … including undergraduate students" [S24, PDF p. 9]. Cartis was **Powell's** last student, not Toint's. Toint (ASR): "I was my first student and Corralia was my last student" [0:27:34–0:27:37], where the context makes clear he means Powell's first and last students, so "my" is probably a mishearing of "his" [S01].

**C3. Gratton (Toulouse partner since the mid-1990s).** No statement by Gratton about Toint was found. The record [practice]: co-direction of Mouffe (2009), Tröltzsch (2011) and Gürol (2013); a place on Malmedy's committee; the informal Jerad arrangement; and 41+ joint papers (`01-publications.md` §1.3).

**C4. Orban.** His homepage has no recollection of Namur or Toint [S21]. He describes his own programme as "tightly interconnected theoretical analyses of computational methods and high-quality implementations" [S21, research page]. [inferred] That is close to Toint's theory–experiments–software triad (`02-methodology.md` B1), but nothing links the two explicitly.

---

## 7. Failures, abandoned directions, friction

- **No failed or abandoned thesis was found.** MGP and theses.fr list only completed degrees. The Namur portal's "Supervised Work (92)" could not be read [S05]. The number probably includes master's theses; this is not verified. **Gap**, not evidence of zero.
- **Difficulty is mentioned only in passing** [observed, secondary]:
  - Bastin: "même dans les moments difficiles" [S17].
  - Sainvitu: "la longue et difficile période de la rédaction de cette thèse … les remises en cause" (the thanks are to her partner, not the advisor) [S14, PDF p. 7].
  - Malmedy: the committee made sure "que je ne me fourvoyais point" [S12].
  - Barthélemy: "Enfin ! Une étape de près de six ans et demi qui se termine !" [S15].
  - Tröltzsch: "challenging me" [S18].
- **The transport line ends.** Toint (ASR) says the transportation research "diverge[d] rather far away" from optimization [0:57:24–0:57:29] [S01; `02-methodology.md` P10]. Barthélemy (2014) is the last transport PhD in MGP. [practice]
- **Retirement ends formal supervision.** The last MGP student is 2015; he retired in 2016 (podcast; homepage). Afterwards the pattern becomes informal junior co-authorship through Toulouse (Jerad) and Florence (Porcelli; `03-process-evidence.md` §6). [practice]
- **A correction involving a junior co-author.** The Gould–Toint trust-funnel paper (10.1007/s10107-008-0244-7) had an erratum (10.1007/s10107-011-0491-x). The full corrected version, report naXys-07-2011, adds D. P. Robinson as co-author (`01-publications.md` §3). Robinson was then an Oxford postdoc working with Gould, per the Gould 04 note (S35), not a Toint student. It is recorded here only because it is the one documented correction with a junior on the author list. How the error was found, and by whom, is not stated in the sources read.

---

## 8. Era and resource context

| Period | Toint's seniority and load | Group and supervision mode | Resources visible in the record |
|---|---|---|---|
| 1979–1993 | Lecturer 1979, associate professor 1987, full professor 1993; co-director of the Numerical Analysis Unit and director of the Transportation Research Group from 1979 [S22] | First Namur students on least squares (geodesy with Golub), trust regions, networks and inverse problems; students join the CGT papers | Vector supercomputers (FPS 164, Cray X-MP: Lescrenier 1988, 10.1177/109434208800200105); Fortran; paper-based test-problem exchange (podcast) |
| 1994–2006 | In charge of the University Computer Services 1998–2000 [S22]; GALAHAD, CUTEr and the trust-region book | Theses in transport, DFO, stochastic programming, interior points and filters; co-supervision with Louveaux, Savard and Daydé; Toulouse link via CERFACS | FNRS aspirant grants [S17]; GALAHAD/CUTEr/LANCELOT-B as the students' platform [S14] |
| 2006–2011 | **Director of the Department of Mathematics 2006–2009** [S22]; MOS chair 2010–2013; SIAM Fellow 2009; the complexity programme starts with Cartis and Gould | **The multilevel cohort** (Mouffe, Tomanos, Weber Mendonça, Malmedy) and the Toulouse co-directions (Tröltzsch, Gürol); a formal thesis committee; stays at CERFACS | FNRS/FRIA fellowships; "a 3.0 Ghz single-processor PC with 2 Gbytes of RAM" for the cohort paper's experiments [S07, PDF p. 11]; Fortran 95 |
| 2012–2016 | Vice-rector for research and IT (homepage [S06]; 2012–2015 per the Imperial seminar bio cited in `02-methodology.md` §9) | Last theses: Barthélemy (transport, parallel micro-simulation on a cluster [S15]) and Rodrigues Sampaio (DFO plus complexity, with Cartis) | University cluster (Barthélemy thanks the cluster administrator [S15, PDF p. 7]) |
| 2016– | Emeritus | No formal students; informal work with Jerad (Toulouse) and Porcelli (Florence) | Matlab and laptop-scale experiments (`03-process-evidence.md` §7) |

[inferred] The biggest student cohort (2007–2011) coincided with his heaviest administrative load (department director, then MOS chair). The group practices in §3 fit that load: seniors mentoring juniors, code handoff, a three-person committee, and long stays with Gratton. A skill that says "Toint supervises by X" should keep this era qualifier.

---

## 9. What this means for the skill (inferred; for the synthesis stage)

For a user who asks the Nonlinear team to improve a solver, the Toint "group method" extracted here would say:

1. Put the idea into a package with documented defaults from the start.
2. If the problem class has no test set, build one before claiming anything.
3. Compare against the strongest in-house code on the shared test set, and report with performance profiles.
4. Pick defaults by a systematic variant study and publish the defaults.
5. Hand the code to the next person with a written account of who did what.
6. Close with one real application.

Items 1–5 rest on [practice] evidence from at least two theses each (§4). Item 6 rests on six of seven theses. **None of these is stated by Toint as a supervision rule**; they are observed regularities.

---

## 10. Contradictions (kept, not reconciled)

- **K1. Freedom versus fit.** Three students stress freedom: "selon mes affinités" (Tomanos), "liberté" (Barthélemy), "autonomie" (Malmedy). Yet nearly every thesis topic is a branch of Toint's programme at that moment (§1.3.1). Both may be true: freedom within a programme. The sources do not say which.
- **K2. Powell's harshness versus the students' picture.** Toint approves of Powell's strictness: "He didn't let vagueness hang around … And for young students, that is sometimes difficult, but I guess that's how you learn" (M2). No Toint student describes anything like it; Tröltzsch's "challenging" (A6) is the closest, and it is addressed jointly to Gratton and Toint. Either he did not reproduce that side, or the acknowledgement genre hides it.
- **K3. Formal versus working supervision (Jerad).** theses.fr lists Gratton as sole director and Toint as a jury member [S10]. Crossref shows 7 three-author papers with Toint from 2023 to 2026 [S08], and Toint thanks Jerad for reading his manuscripts (`03-process-evidence.md` §6).
- **K4. Toint's own advisors.** MGP lists two advisors, Powell and Callier [S09]. In the podcast, asked "So ultimately, he was the main advisor of your PhD work?", he answers "Yes, yes, certainly." [0:34:50–0:34:53, ASR] [S01]. The 1977–78 JOTA papers with Callier are listed in `01-publications.md` §1.
- **K5. Orban's co-supervisors.** MGP: Toint and Daydé [S09]. theses.fr: Toint, Sartenaer and Daydé [S10]. The degree-granting institution is Namur in MGP and INPT Toulouse in theses.fr; it was probably a joint degree, but this is not verified.
- **K6. Sainvitu's RAIRO paper.** Crossref lists Sainvitu as sole author (10.1051/ro/2009016). A CORE record of the same title lists Toint as co-author (seen in a CORE search result, record 58124764, not opened).
- **K7. Counts.** MGP: 20 students. Namur portal: "Supervised Work (92)", unread [S05]. Not reconciled.

---

## 11. Gaps

- **HAL full texts blocked.** theses.hal.science answers with an anti-bot proof-of-work page (Anubis) that says it exists to stop AI scraping. I did not try to get around it. That blocked the HAL copies of the Mouffe, Tröltzsch, Gürol and Jerad theses. Mouffe and Tröltzsch were read through CORE. **Gürol's and Jerad's acknowledgements were not read.** Jerad's CORE record (work 161927542, output 604536025) has no downloadable file (HTTP 404), and CORE searches found no record for Gürol's thesis. The same protection blocked DBLP and Bastin's Montréal homepage in this run.
- **Namur research portal list pages returned 403** (student theses, supervised work, activities: external thesis examinations 5 and jury 2). Only the person page was read [S05]. The OAI-PMH endpoint returned HTTP 500.
- **Theses not read**: Weber Mendonça 2009 (CORE record without a file), Rodrigues Sampaio 2015, Colson 2003, Orban 2001, Bierlaire 1996, Sartenaer 1991, and the 1985–1993 theses (probably not digitised). Also Gürol and Jerad (above), Schulze and Thekale (external; not found open).
- **No Festschrift, birthday or retirement volume, or workshop in his honour was found** (WebSearch 1 [S26]; Crossref check of the 2024 OMS preface, which is a special-issue preface he co-signed, not a tribute [S25]).
- **No student blog post, memoir, interview or lab or onboarding guide** was found. Weber Mendonça's blog has one post, not on this topic [S19]. Orban's homepage has no recollection [S21].
- **No collaborator statement about his supervising.** Gould's and Cartis's texts concern collaboration, not students (§6).
- **His own supervision rules** (how he picks student topics, how often he meets students, how he edits drafts, when he lets a student publish alone) were not found stated anywhere.
- **Postdocs** were not traced systematically: Porcelli, E. Simon, Cirillo, and Bastin after 2004.
- **The podcast transcript is unverified ASR.** The M3 and M6 wordings come from the small model only.

---

## 12. Sources

P = primary (Toint's own words or record); S = secondary (someone else's account, or a registry). "Checked" = identifier resolved or record fetched with a tool in this run.

- S01 · "Subject to: Philippe Toint", podcast hosted by Anand Subramanian, 27 July 2026; ASR transcript at `../sources/talks/2026-07-27_subject-to_podcast_toint_ASR-transcript.txt` (saved by agent 02); episode https://podcasters.spotify.com/pod/show/subject-to/episodes/Subject-to-Philippe-Toint-e3mjb27 · P (ASR, unchecked by a human); passages read in full
- S02 · M. Buhmann, R. Fletcher, A. Iserles & P. Toint, "Michael J. D. Powell. 29 July 1936—19 April 2015", *Biogr. Mems Fell. R. Soc.* 64 (2018) 341–366, doi:10.1098/rsbm.2017.0023; preprint https://perso.unamur.be/~phtoint/pubs/Powell.pdf · P, co-authored (PDF pp. 10–11 and 14 read)
- S03 · Ph. L. Toint (postscript by N. Gould), "In memory of Andy Conn / In Memoriam Andrew Conn (1946–2019)", *SIAG/OPT Views and News* 27(2), 2019, pp. 9–10, https://siagoptimization.github.io/assets/views/ViewsAndNews-27-2.pdf · P (read in full)
- S04 · Ph. L. Toint, "MOS Chair's Column", *Optima* 85, April 2011, p. 1, https://mathopt.zib.de/Optima-Issues/optima85.pdf · P (column read)
- S05 · Philippe Toint, University of Namur research portal, https://researchportal.unamur.be/en/persons/phtoint (person page read; sub-pages 403) · S (institutional record)
- S06 · Ph. Toint, homepage, https://perso.unamur.be/~phtoint/toint.html, and publications list https://perso.unamur.be/~phtoint/publications.html · P (read)
- S07 · S. Gratton, M. Mouffe, A. Sartenaer, Ph. L. Toint & D. Tomanos, "Numerical experience with a recursive trust-region method for multilevel nonlinear bound-constrained optimization", report 08/10 (22 June 2008), https://perso.unamur.be/~phtoint/pubs/TR08-10.pdf; *Optim. Methods Softw.* 25(3) 2010, doi:10.1080/10556780903239295 (checked) · P (PDF pp. 11–16 read)
- S08 · Crossref REST API queries, one per student name paired with "Toint" (query.author), 28 Sep 2026; all DOIs in §1.1 and §1.2 come from these results · P (practice; metadata only)
- S09 · Mathematics Genealogy Project, Philippe Louis Toint, id 87096, https://www.mathgenealogy.org/id.php?id=87096, and the 20 student pages linked from it · S (registry; read)
- S10 · theses.fr API records 2001INPT012H (Orban), 2009INPT011G (Mouffe), 2011INPT0031 (Tröltzsch), 2013INPT0040 (Gürol), 2024TLSEP024 (Jerad), https://theses.fr/api/v1/theses/these/<id> · S (registry; read)
- S11 · HAL API records tel-04382258, tel-04234302, tel-04286910, tel-04539100 (file links); files blocked by Anubis · S (metadata only; not read)
- S12 · V. Malmedy, *Hessian approximation in multilevel nonlinear optimization*, PhD thesis, FUNDP Namur, 10 Sept 2010 (promoteur Ph. L. Toint), https://core.ac.uk/download/326315592.pdf · S, first-hand (front matter, acknowledgements PDF pp. 6–7, Ch. 2.8 opening PDF p. 63 and Ch. 8 PDF pp. 200–201 read)
- S13 · D. Tomanos, *Algorithms and software for multilevel nonlinear optimization*, PhD thesis, FUNDP Namur, 7 May 2009 (promoteur Ph. L. Toint), https://core.ac.uk/download/326315404.pdf · S, first-hand (front matter, acknowledgements PDF pp. 6–7, PDF pp. 41, 99 and 122 read)
- S14 · C. Sainvitu, *Filter-Trust-Region Methods for Nonlinear Optimization*, PhD thesis, FUNDP Namur, 17 Apr 2007 (promoteur Ph. L. Toint), https://core.ac.uk/download/326314552.pdf · S, first-hand (front matter, acknowledgements PDF pp. 6–7, PDF p. 88 read)
- S15 · J. Barthélemy, *A parallelized micro-simulation platform for population and mobility behaviour – Application to Belgium*, PhD thesis, Université de Namur, 25 Apr 2014 (promoteurs Ph. Toint and E. Cornelis), https://core.ac.uk/download/326316386.pdf · S, first-hand (front matter, acknowledgements PDF pp. 6–7, PDF pp. 33 and 144 read)
- S16 · M. Mouffe, *Multilevel optimization in infinity norm and associated stopping criteria*, PhD thesis, INPT Toulouse and FUNDP Namur, 10 Feb 2009 (directeurs S. Gratton and Ph. Toint), https://core.ac.uk/download/19938320.pdf · S, first-hand (jury pages and acknowledgements PDF pp. 1–5 read)
- S17 · F. Bastin, *Trust-Region Algorithms for Nonlinear Stochastic Programming and Mixed Logit Models*, PhD thesis, FUNDP Namur, 12 Mar 2004 (promoteur Ph. L. Toint, co-promoteur F. Louveaux), https://core.ac.uk/download/326313371.pdf · S, first-hand (front matter, acknowledgements PDF pp. 6–7 read)
- S18 · A. Tröltzsch, *An active-set trust-region method for bound-constrained nonlinear optimization without derivatives applied to noisy aerodynamic design problems*, PhD thesis, INPT Toulouse, 7 June 2011 (directeur S. Gratton, co-directeur Ph. L. Toint), https://core.ac.uk/download/78383024.pdf · S, first-hand (PDF pp. 1–9 read)
- S19 · M. Weber Mendonça, "About me", https://melissawm.github.io/about-me/ (and blog RSS) · S (read)
- S20 · M. Bierlaire, EPFL people page, https://people.epfl.ch/michel.bierlaire · S (read)
- S21 · D. Orban, homepage (research, appointments, 2017 blog post), https://dpo.github.io/ · S (read; nothing on Toint)
- S22 · University of Edinburgh staff news, "Honorary Professor: Philippe L Toint" (2010 appointment), https://www.ed.ac.uk/news/staff/appointments-awards/2010/philippe-toint-070510 · S (read)
- S23 · N. I. M. Gould, *An introduction to algorithms for continuous optimization*, course booklet, preface, https://www.numerical.rl.ac.uk/media/people/nick-gould/cobook.pdf · S about Toint (PDF p. 8 read)
- S24 · C. Cartis, Curriculum Vitae (2025), https://www.maths.ox.ac.uk/system/files/users/cv/Cartis_CV_2025_0.pdf · S (PDF pp. 1–5 and 9 read)
- S25 · S. Gratton, Ph. Toint, J. Gondzio, Yu. Nesterov & Y. Yuan, "Preface for the special edition of Optimization Methods and Software", *OMS* 39(3) 2024, 457–458, doi:10.1080/10556788.2024.2406663 · P (Crossref metadata only; not read)
- S26 · WebSearch 1: "Philippe Toint" workshop/conference in honour/birthday/retirement Namur (no tribute event found; led to S04 and S22) · search record
- S27 · WebSearch 2: "Philippe Toint" thesis acknowledgements/remerciements supervisor/promoteur (led to S12 via CORE) · search record
- S28 · CORE API v3 records and searches (works 20227735, 20227893, 20227325, 20227260, 7456891, 16216056, 20224251, 20227410, 161927542), https://api.core.ac.uk/v3/ · S (metadata)
- S29 · C. Sainvitu, "How much do approximate derivatives hurt filter methods?", *RAIRO-Oper. Res.* 2009, doi:10.1051/ro/2009016 · S (Crossref metadata only; sole author in Crossref)
- S30 · J. Barthelemy & Ph. L. Toint, "Synthetic Population Generation Without a Sample", *Transp. Sci.* 47 (2013), doi:10.1287/trsc.1120.0408 · P (Crossref metadata only)
- S31 · F. Bastin, V. Malmedy, M. Mouffe, Ph. L. Toint & D. Tomanos, "A retrospective trust-region method for unconstrained optimization", *Math. Program.* 123(2) 2010 (online 2008), doi:10.1007/s10107-008-0258-1 · P (Crossref metadata; the report TR07-08 was downloaded but its text is font-encoded and was not readable)
- S32 · Research note `01-publications.md` (this skill, agent 01, 2026-09-28): collaboration clusters and the "likely students" list verified here · repository cross-reference
- S33 · Research note `02-methodology.md` (agent 02): O2 (ADTAO long stays), E1 (CUTE origin), P6, P10, T6, W6 · repository cross-reference
- S34 · Research note `03-process-evidence.md` (agent 03): §6 (hand-offs to juniors; Jerad thanked), §7 · repository cross-reference
- S35 · Research note `product/nonlinear-team/nicholas-i-m-gould/references/research/04-mentorship.md` (Gould agent 04): pointer to S23 and S24; Robinson's status · repository cross-reference
- S36 · Weber Mendonça thesis, CORE work 20227410 (outputs 326315403, 34082978 returned 404) · S (not read)
