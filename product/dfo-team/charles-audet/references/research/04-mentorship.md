# 04 · Mentorship, co-authors and group culture

Honest scope: **no first-hand student recollection, thesis acknowledgment text, lab guide, or interview was found** in the available budget. What follows is reconstructed from primary artifacts: (1) Polytechnique theses listed in the group bibliography, (2) co-authorship patterns, (3) NOMAD acknowledgments and bbopt repository conventions. Supervisor roles are **not verified**. Many of these students may have been supervised mainly by Le Digabel or co-supervised. Treat every "student of Audet" as "student in the Audet/Le Digabel GERAD group, co-author with Audet".

Sources: https://raw.githubusercontent.com/bbopt/bibtex/master/bibliography.bib (primary); https://raw.githubusercontent.com/bbopt/nomad/master/doc/user_guide/source/Introduction.rst (primary); bbopt READMEs (primary).

---

## 1. Thesis → paper pipeline (observed, primary bibliographic evidence)

| Thesis (Polytechnique Montréal) | Level, year | Later co-authored paper with Audet [B] |
|---|---|---|
| V. Béchard, *Optimisation d'un procédé de traitement des brasques* | MSc 2004 | Spent potliner treatment (Optim. Eng. 2008); STYRENE code (JOGO 2008) |
| S. Le Digabel, *Extensions à l'algorithme de recherche directe MADS pour l'optimisation non-lisse* | PhD 2008 | PSD-MADS 2008, OrthoMADS 2009, globalization 2010, then 48 joint entries; became Audet's long-term co-lead of NOMAD |
| V. Garnier, *La gestion des groupes de variables en recherche directe* | MSc 2010 | Snow water equivalent (PJO 2013) |
| D. Cartier, hydrological model under constraints | MSc 2012 | Minville et al. 2014; performance indicators (EJOR 2021) |
| A. Ihaddadene, *Algorithme de recherche directe pour l'optimisation robuste de fonctions bruitées* | MSc 2014 | Robust optimization of noisy blackboxes (Opt. Lett. 2018) |
| M. Lemyre Garneau, *Modelling of a solar thermal power plant for benchmarking blackbox optimization solvers* | MSc 2015 | SOLAR (Optim. Eng. 2024/25), 9 years later |
| M. Peyrega, *Optimisation sans dérivées sous contraintes* | PhD 2016 | Linear equalities (COAP 2015); PBTR with Conn (COAP 2018) |
| N. Amaioua, *Modèles quadratiques et décomposition parallèle pour l'optimisation sans dérivées* | PhD 2018 | Quadratic subproblems within direct search, with Conn (EJOR 2018) |
| P.-Y. Bouchet, *Optimisation de boîtes noires à précision variable* | MSc 2019 | Adaptive precision (SIAM J. Optim. 2021); counterexample note (Math. Prog. 2024); covering step (2025); partitioned framework (JOTA 2026) |
| K.J. Dzahini, *Méthodes de recherche directe pour l'optimisation stochastique de boîtes noires* | PhD 2020 | StoMADS (COAP 2021); later first author of the survey "Direct-search methods in the year 2025" (with Rinaldi, Royer, Zeffiro; arXiv 2403.05322) |
| D. Lakhmiri, *Optimisation des hyperparamètres des réseaux de neurones profonds* | PhD 2021 | HyperNOMAD repo |
| L. Salomon, *Contributions to Multiobjective Blackbox Optimization* | PhD 2022 | Performance indicators (EJOR 2021); DMultiMads, integrated in NOMAD 4 |
| E. Hallé-Hannan, *Cadre mathématique pour l'optimisation de boîtes noires avec variables métas et catégorielles* | MSc 2022 | ORF 2023 framework; distance (Neurocomputing 2025); Cat-Suite; CatMADS (2025/26) |
| X. Lebeuf, *Optimisation de boîtes noires multifidélités avec contraintes hiérarchisées* | MSc 2023 | Inter-DS (COAP 2025); multi-fidelity constraints (2026); SOLAR; Micro-PRIAD |
| S. Mendoza, *Répartition computationnelle efficace entre boîte noire et solveur* | MSc 2024 | (Parallel MADS survey 2026 is by Le Digabel et al., without Audet) |

Observed pattern (inference, medium confidence):
- **Each thesis owns one blackbox pathology** (noise, precision, multi-fidelity, categorical, constraints, parallelism). The pathology is then added to the MADS family and often to NOMAD.
- **Master's students publish.** Several MSc theses lead directly to journal papers (Ihaddadene, Bouchet, Hallé-Hannan, Lebeuf).
- **Applied theses become benchmark problems** (Béchard → STYRENE; Lemyre Garneau → SOLAR).
- Theses are mostly written **in French**; the papers are in English.

## 2. Co-author structure (primary, bib counts)
- **Mentors / senior partners:** P. Hansen, B. Jaumard, G. Savard (1997–2013, global and bilevel optimization); J.E. Dennis Jr. (2000–2012, pattern search, MADS).
- **Peer co-leads:** S. Le Digabel (48), C. Tribes (18, research software engineer on NOMAD), W. Hare (textbook), M. Kokkolaras (engineering design, surrogates), D. Orban (algorithm tuning), Y. Diouane (2023–2026, ADS, Mads-PIP, categorical).
- **Industry-embedded co-authors:** S. Alarie (12 entries; thanked in NOMAD acknowledgments for "feedbacks and tests"), P. Côté (hydropower; PyNomad), A.E. Gheribi (materials), M. Diago, X. Lebeuf.
- **Cross-school collaborations with other DFO lenses:** A.R. Conn (two 2018 papers), A.L. Custódio (2008 erratum), L.N. Vicente (co-editor of a 2004 *Optimization and Engineering* special issue on surrogate optimization with Audet and Dennis [B]).

## 3. Group culture visible in artifacts (primary)
- **Credit to contributors in the product itself.** The NOMAD guide names testers, interns and users: "Some features of NOMAD have been developed under the impulsion of enthusiastic users/developers/interns: [...]"; the STYRENE README credits the students who found the current and previous best-known solutions (Lameynardie; Kojtych, Tanneau).
- **Shared infrastructure with discipline.** One group BibTeX file with a strict entry template: "**NEVER** change a key, even if it is not standard or with the wrong year". Every group paper has a GERAD cahier number, and recent ones also an arXiv ID.
- **Open prototypes.** "The current code is a proof of concept. While the code is shared for transparency [...]" (CatMADS_prototype).
- **Service to the community.** *Scheduling ISMP 2024* (GERAD tech report, Audet, Gervais-Dubé, Hertz, Le Digabel, Legrain) [B]. Audet's exact organizing role at ISMP 2024 is not verified.

## 4. Teaching (primary bibliographic)
- French course notes: MTH6404 *Programmation en nombres entiers* (2001), MTH1101 *Calcul I* (2011).
- *Optimisation continue* (Presses internationales Polytechnique, 2021, 305 pp).
- Audet & Hare textbook (2017; 2nd ed. 2026), designed for self-study or an upper-year course; companion repo `bbopt/dfbbo`.
- Reviewer view (secondary): Brezhneva (Math. Reviews 2018): "The authors pay equal attention to careful theoretical development and analysis of the methods, and to practical details of the algorithms." Kokkolaras (Optim. Eng. 2019): "a wonderful textbook". Kokkolaras is a frequent co-author of Audet (7 entries), so this review is not independent.

## 5. Tacit knowledge that could NOT be extracted
- How Audet runs meetings, gives feedback on drafts, or picks the next thesis topic.
- The division of supervision between Audet and Le Digabel.
- Unpublished failed directions.
