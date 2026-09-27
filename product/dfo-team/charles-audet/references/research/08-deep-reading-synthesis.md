# Deep-reading synthesis: Charles Audet

> What the full texts say about the research methods in `SKILL.md`, aggregated from all 193 paper cards (`cards/*.md` and `cards/*.digest.json`; index in `07-paper-cards.md`). Date: 2026-09-27.
>
> Rules applied: conservative update (`references/paper-reading-card.md` §3), four-way validation (`references/research-extraction-framework.md` §3: cross-project recurrence, say–do consistency, executable and different from standard practice, exclusivity) and the quality checklist (§11). This note proposes changes. It does not edit SKILL.md.

**Conventions**

- `[S012 p. 9]` points to the card of work S012. The page is the `[[page N]]` marker of the version named on that card, which is often an arXiv or GERAD preprint.
- "Full" means read in full or in part. Abstract-level and metadata-only cards are listed but never decide a promotion.
- Counts are of distinct works. The duplicate pairs S101 = S128, D002 = S067, S019 = S202, S112 = S163, S204 ≈ S145 (same case study), S089 = S215 and S208 = S207 each count once.
- S213 is M. A. Abramson's Rice PhD thesis (2002). It is misattributed to Audet on Scholar, and Audet co-chaired the committee [S213 p. 1]. It is cited only as evidence of the research programme Audet co-directed, never as his writing. D008 is an edited proceedings volume with no Audet content. Both are excluded from all Audet counts.
- S022 (Audet 7th of 15 authors), S174 (4th of 5, power-systems Benders) and S160 (origami, collaborator-led) are low weight, marked †. None of them is ever the sole support for a claim.
- Cards also contain reading notes on slips inside papers: typos, tables that disagree with the text, loosely worded proof steps. By house rule these are not findings about the researcher, and none of them is used below.

---

## 1. Coverage

| Read level | Scholar works (S###) | Non-Scholar works (D###) | Total |
|---|---|---|---|
| Full text, full card | 102 | 6 | 108 |
| Full text, partial card | 5 | 1 | 6 |
| Unreadable as named (S025: the file is the 1998 precursor report, read via OCR; S067: the file is D002's text) | 2 | 0 | 2 |
| Abstract-level card (no open full text) | 53 | 4 | 57 |
| Metadata-only card | 15 | 5 | 20 |
| Skipped, no card (talks, conference duplicates of journal papers, Scholar junk rows) | 19 | 0 | 19 |
| **Total works on the list** | **196** | **16** | **212** |

- There are 193 cards. After merging the four duplicate pairs among full or partial cards, 110 distinct works were read in full or in part. Of these, **108 are Audet-authored**; the other two are S213 and D008.
- Depth of reading by period (cards, including duplicates):

| Period | Cards | full | partial | unreadable | abstract | metadata |
|---|---|---|---|---|---|---|
| 1994–1999 | 8 | 1 | 0 | 0 | 6 | 1 |
| 2000–2004 | 24 | 12 | 0 | 1 | 8 | 3 |
| 2005–2009 | 35 | 18 | 0 | 0 | 14 | 3 |
| 2010–2014 | 36 | 14 | 1 | 1 | 16 | 4 |
| 2015–2019 | 32 | 18 | 1 | 0 | 8 | 5 |
| 2020–2024 | 29 | 21 | 4 | 0 | 4 | 0 |
| 2025–2026 | 27 | 24 | 0 | 0 | 1 | 2 |
| undated | 2 | 0 | 0 | 0 | 0 | 2 |

- Reading is thin before 2005. 1994–1999 is represented in full only by the thesis [S070]. Work from 2020 on is read almost completely.
- Many versions read are preprints or reports: StoMADS arXiv v1 [S053 p. 1], NOMAD 4 arXiv v2 [S021 p. 1], the 2012 GERAD version of the direct-search survey [S023 p. 1], the 3.7.2 revision (2015) of the NOMAD guide [S019 p. 1], arXiv versions of the hierarchical-constraint and counterexample notes [S123; S138 p. 1], the 1998 technical report instead of the 2004 tightness article [S025]. Section 11 lists where this matters.

---

## 2. Evidence per existing method

### 2.1 Counts

The raw counts are the links as recorded on the 193 cards. The distinct counts exclude S213 and D008 and merge duplicates. Values in parentheses count full or partial cards only.

| Method | Raw links: evidence / variant / contradiction | Distinct Audet works: evidence / variant / contradiction | Five-year periods with full-text evidence | Verdict |
|---|---|---|---|---|
| 1 Free Search, rigid Poll | 40 / 35 / 1 | 39 (32) / 33 (30) / 1 (1) | 6 | Keep. Add the ordering slot (§4.3) and correct one practice item (§3.1 #6) |
| 2 Constraint semantics first | 45 / 36 / 0 | 41 (35) / 33 (29) / 0 | 6 | Keep. Extend to inputs (§4.3) and to evaluation cost (§3.2) |
| 3 Guarantee ladder, bounded by counterexamples | 40 / 43 / 4 | 39 (32) / 43 (41) / 4 (3) | 7 | Keep. Correct the complexity claim (§3.1 #3). Add adversarial instances and instrument audits (§4.3) |
| 4 Real blackboxes → public benchmark artifacts | 37 / 27 / 1 | 35 (33) / 27 (23) / 1 (1) | 6 | Keep. Re-scope: no public release is mentioned for most partner problems (§3.2) |
| 5 Budget-aware, cross-community benchmarking | 33 / 58 / 4 | 32 (26) / 54 (51) / 4 (4) | 6 | Keep. Re-scope: the most variants of any method, so say–do is only partly consistent (§2.2) |
| 6 Solver as research instrument | 43 / 19 / 0 | 40 (34) / 19 (15) / 0 | 6 | Keep. Add the second instrument and prototypes outside NOMAD (§3.2) |

Every method has at least 26 full-text evidence cards spread over at least six five-year periods, so none is the weak link that a promotion would have to replace (§4.1).

### 2.2 Strongest cards and say–do update, per method

**Method 1: Free Search, rigid Poll**
- *Stated*, with pages:
  - the Search "freedom must be retained" [S002 p. 3];
  - "The flexibility of our theory ensures that such heuristics can be part of a rigorously convergent algorithm" [S005 p. 22];
  - the Search "contributes nothing to the convergence theory" but gains early improvement [S031 p. 5];
  - "The search step is crucial in practice because it is so flexible, but it is a difficulty for the theory for the same reason" [S019 p. 16];
  - "the MADS theory assumes that trial search points must be lying on the current mesh" [S019 p. 100];
  - the Search exists so that users can inject problem knowledge without destroying the Poll structure [S023 p. 9];
  - the poll ensures convergence while the search implements efficiency and global exploration [S046 p. 5].
- *Practiced*:
  - a dynamic ordering trick is recast as a one-point Search so that it stays on the mesh [S001 p. 17];
  - convergence is "independent of the surrogate function and of the search step" [S016 p. 10];
  - all parallel subspace work is treated as Search, with a single-direction pollster [S027 pp. 8, 14–16];
  - an off-mesh surrogate optimum is projected onto the mesh although off-mesh is "often more efficient" [S046 pp. 7–8];
  - ensembles and Bayesian-style subproblems live in the Search [S099 pp. 6–7, 15–16];
  - a cross-entropy Search [S133 pp. 1, 3];
  - searches bring performance, polls carry guarantees (card paraphrase, not the paper's words); verbatim: "The extended poll is optional, but is labeled as a poll, since it affects the convergence guarantees." [S121 p. 6].
- *Say–do*: ✅ stated and practiced, 1998–2026.
- *Update*:
  - The full texts show two more theory-free slots: the evaluation order under opportunism [S072 p. 6; S114 p. 10; S143 p. 10] and a wrapper around the blackbox [S112 p. 14; S173 pp. 6–7] (§4.3, §5).
  - CatMADS is Poll-side, not Search-side (§3.1 #6).
  - In ADS the Search is also freed from the mesh while the Poll still carries the proof [S129 pp. 4, 9, 14; S172 pp. 3, 8–11]. This answers the Method 1 limitation "the mesh itself restricts trial points".

**Method 2: Constraint semantics first**
- *Stated*:
  - the 3.7.2 guide's EB/PB/hidden wording, the c_j ≤ 0 convention and CSTR = PB [S019 pp. 16, 39, 41, 48, 53];
  - the survey's taxonomy with reasons: unrelaxable because the simulation cannot be trusted (log, sqrt), hidden because the simulation fails inexplicably, relaxable with a measurable violation [S023 pp. 10, 12];
  - equalities need their own mechanism [S158 pp. 3–4, 25].
- *Practiced*:
  - the closed/open split that became EB/PB, with STYRENE's 4 closed yes-no and 7 open constraints [S007 pp. 2–4, 31];
  - linear constraints by barrier vs nonlinear constraints by filter [S005 pp. 1–2, 6–7];
  - binary constraints as relaxable but unquantifiable [S072 pp. 5, 7];
  - a priori constraints checked before simulation and not counted [S071 pp. 18–23; D006 p. 15; S175 pp. 6, 9–10];
  - infeasible inner problems return a quantified violation to PB rather than +∞ [S151 pp. 7–8].
- *Say–do*: ✅.
- *Update*:
  - The later papers add two classification axes: when a constraint can be computed, and at what cost (a priori vs simulation, fidelity, position in a pipeline) [S123 pp. 2–3, 6, 8; S173 pp. 1, 5, 7].
  - Semantics are also applied to inputs (§4.3).
  - "Relaxable → PB" is overridden when evaluations are interrupted (§3.1 #12).

**Method 3: Guarantee ladder, bounded by counterexamples**
- *Stated*:
  - "the stronger the hypotheses on the objective and feasible region, the stronger the resulting theoretical guarantees" [S023 p. 7];
  - results "sharp in that they predict the behavior" [S002 p. 3], with an example for each rung of the ladder [S002 pp. 9–12].
- *Practiced*:
  - three minimal counterexamples to Torczon's results (1998 TR) [S025 TR pp. 3–12];
  - hierarchy (i)–(vii) [S002 p. 12];
  - Example 3.10 plus a deliberately hypothesis-violating run [S001 pp. 11–13, 25];
  - second-order rungs each bounded by an example, plus a GPS instance proved to converge to a saddle [S020 pp. 10–15];
  - hierarchy (i)–(x) with a counterexample that forces assumption A3 [S007 pp. 19–25];
  - a peer's theorem refuted, the false step located, a repair given, and the counterexample re-run through the repaired algorithm [S138 pp. 2–9];
  - the ladder raised from stationarity to local minima, with the new assumption shown strictly weaker and tight, and an unused Lipschitz hypothesis dropped [S137 pp. 4–6, 11–12];
  - a counterexample for every characterization [S120 pp. 5–11];
  - the rational-τ hypothesis of 2004 shown unnecessary for ADS [S129 pp. 7, 11–14];
  - the MADS proof erratum [D001 pp. 1–2].
- *Say–do*: ✅.
- *Update*:
  - Worst-case complexity is not absent from the corpus (§3.1 #3).
  - The counterexample half is practiced mainly in the theory papers. Many later algorithm papers state a ladder without necessity counterexamples [S053 pp. 11–20; S084 pp. 10, 15–19; S121 pp. 12–15; S158 pp. 13–16; S172 pp. 13–15].
  - The craft moved to adversarial instances, rival-failure toys and measuring instruments (§4.3).

**Method 4: Turn real blackboxes into public benchmark artifacts**
- *Stated*:
  - testing on CUTEr or Hock–Schittkowski problems "is not ideal, as these problems do not possess the same kind of difficulties" [S023 p. 19];
  - "no work exhibits a realistic application specifically developed for BBO benchmarking" [S071 p. 3];
  - DFO solvers are "too often benchmarked on problems that do not fully capture the challenges of the field" [S175 p. 4].
- *Practiced*:
  - STYRENE C++ code released in 2009 with its constraint types and both feasible and infeasible starts [S007 p. 31];
  - source code and best points posted [S027 p. 22];
  - pooling instance data online as early as 2004 [S015 pp. 5, 15–16];
  - the `bb.exe x.txt` contract already fixed in the NOMAD 3 guide [S019 pp. 39–40];
  - SOLAR: a thesis model turned into a frozen, platform-reproducible executable with classified constraints, fidelities, seeds, starting points and credited best-known values [S071 pp. 3, 13–32];
  - Micro-PRIAD [D006 pp. 6, 13, 23–31];
  - Cat-Suite [S130 pp. 3, 5];
  - a solver-selection guide over SOLAR [S175 pp. 7, 9].
- *Say–do*: ✅, with a scope correction.
  - No public release is mentioned for the partner blackboxes in S013 (pp. 2–10), S032 (pp. 18–19, 29), S145 (p. 14), S084 (pp. 24–26), S143 (pp. 12–13) and S167 (pp. 4, 10). The texts do not say the blackboxes are private; this is inferred from the absence of a release statement.
  - Public artifacts come from dedicated benchmark papers and, once, from a scaled-down public twin: Micro-PRIAD, open-source on GitHub [D006 pp. 4, 6, 22]. S074 built a cheaper surrogate problem "to be accessible for testing outside of HQ", with no public release stated [S074 pp. 3–4]. (Corrected after review: S074 was first cited as a second public twin.)

**Method 5: Budget-aware, cross-community benchmarking**
- *Stated*:
  - the benchmarking summary, read in full [S128 pp. 4–16; S101];
  - "having a test set that is representative of the ultimate goal is crucial" [S128 p. 4];
  - "comparing DFO algorithms to algorithms that explicitly use derivatives should be avoided" [S128 p. 5];
  - Pareto-compliant indicators are recommended for multiobjective profiles [S004 pp. 19–21];
  - blackbox and derivative-free algorithms "are not competitors of gradient-based methods; they are a fallback when gradient-based algorithms cannot be used" [S034 p. 1].
- *Practiced*:
  - COBYLA on its smooth home ground plus NOMAD on MDO blackboxes [S063 pp. 6, 17–23];
  - three other-family competitors with a shared design of experiments (DoE) [S121 pp. 22–23];
  - a same-solver ablation first, then three other families including the rival's own code [S172 pp. 16–19];
  - four families including a commercial solver, with h-profiles for infeasible starts [S175 pp. 8, 11];
  - profiles rebuilt in Monte Carlo draws when evaluation counts are irrelevant [S084 pp. 19–20];
  - two-level effort currency [S156 pp. 13–19];
  - the competitor's home ground conceded with CPU-speed-adjusted ratios, already in 2004 [S015 pp. 9–15].
- *Say–do*: ✅ for evaluation currency, profiles and fair baselines. ⚠ for "cross-community".
  - Cross-family competitors appear in 16 full cards: S022†, S027, S063, S064, S068, S071, S073, S099, S116, S121, S133, S140, S157, S158, S172, S175.
  - Most other algorithm papers compare variants inside NOMAD: S001, S006, S007, S021, S046, S053, S061, S072, S112, S114, S123, S125, S129, S137, S144, S173.
  - The summary itself bounds step 3: no derivative-based competitors, and very few algorithms at a time [S128 pp. 5, 9].
- *Update*: re-scope step 3 and add explicit effort weights (§3.1 #17; §5 N3–N4). Lift the "not read in full" limitation (§3.1 #8).

**Method 6: The solver as research instrument**
- *Stated*:
  - "In continuous development since 2001, it constantly evolved with the integration of new algorithmic features published in scientific publications" [S021 p. 1];
  - defaults as a benchmark compromise, the symptom table, bug reports, and release notes mapping versions to papers [S019 pp. 18–20, 73–74, 103–107];
  - NOMAD was improved "mainly thanks to the lessons learned" in applications [S013 p. 4].
- *Practiced*:
  - a 2014 preprint's anisotropic mesh is the default by the 2015 guide [S061 pp. 13, 17; S202 pp. 80, 104];
  - NOMAD in library mode inside a genetics package [S066 pp. 4, 8];
  - NOMAD C++ already carried research features to industry in 2000–2003 [D016 pp. 3, 5];
  - a user-requested feature and a parity check against NOMAD 3 [S021 pp. 13–14];
  - new algorithms implemented on NOMAD 3.9 and 4 [S090 p. 17; S099 p. 16; S112 p. 16; S121 p. 19].
- *Say–do*: ✅.
- *Update*:
  - A second shared instrument, the RunnerPost post-processor, produces every benchmarking plot [S128 p. 16], reused in [S156; S157].
  - Several algorithms live as prototypes outside NOMAD: Python [S063 p. 16; S084 p. 19], MATLAB on request [S120 p. 21], or a solver-agnostic wrapper [S173 pp. 18, 23].
  - Features lag papers [S021 p. 18; S053 p. 21].

---

## 3. Variants and contradictions

### 3.1 Contradictions and corrections, verified against the card texts

The full texts win over the search snippets SKILL.md was built from. Each item names the SKILL.md location, what changes, and the cards.

1. **Signature Work Anatomy, GPS tightness paper: Origin and Why-then rows.**
   - *SKILL.md says*: the paper "follows the 2003 GPS analysis".
   - *Full texts*:
     - the counterexamples first appear in the Rice report CRPC-TR98779, "Convergence Results for Pattern Search Algorithms are Tight", dated 17 November 1998. It has three examples targeting Torczon's 1997 results and was written at the start of the NSERC postdoc [S025 TR pp. 1–3];
     - the GPS analysis presents its own examples as ones "that supplement those in [1]" and cites the report [S002 pp. 3, 14];
     - the mixed-variable paper cites it too [S011 pp. 15, 22], and Abramson's thesis cites it three times [S213 pp. 36, 87, 171–172].
   - *Change*: Origin = a 1998 probe of Torczon's 1997 theorems. The GPS reanalysis came after it and cites it. Why then = Torczon's theory was new and Audet had just arrived at Rice.
   - The 2004 journal version was not available, so "six counterexamples" is not verified by a full text.
2. **Signature Work Anatomy, progressive barrier.**
   - *SKILL.md says*: "NOMAD 3 (2008) needed a default treatment for quantifiable relaxable constraints" (Why then, marked inference).
   - *Full text*: that inference is not stated. The paper's motivations are four user situations [S007 pp. 3–4]:
     - no feasible start was available for an aircraft planform problem;
     - GPS-filter users valued its constraint-sensitivity information;
     - industrial codes fail, return Boolean values or are undefined outside X;
     - violations may save evaluations.
   - NOMAD appears only as the host of STYRENE [S007 p. 31].
   - *Rows that can now be filled*:
     - Origin, now stated rather than inferred: the paper combines GPS-filter and MADS-EB [S007 p. 2].
     - Abandoned path: "We do not use a filter, but we do use the notion of dominance fundamental to filters" [S007 p. 3].
     - Minimal evidence: a three-case analysis, hierarchy (i)–(x), a counterexample that forces A3, and two analytic problems plus STYRENE [S007 pp. 15–31].
3. **Weak spots, Method 3 limitations, Roundtable vs Scheinberg.**
   - *SKILL.md says*: "No verified Audet title or abstract states a complexity bound".
   - *Full texts*:
     - S140 proves expectation rates for a zeroth-order Signum method and an evaluation complexity of O(n⁶L^{7/2}/ε^{7/2}) for its sequential smoothing method [S140 pp. 14–15, 21–22]. The card is a partial read, and Audet is coauthor with Bigeon, Couderc and Kokkolaras (alphabetical order).
     - S120 gives non-asymptotic O(Δ) and O(Δ²) projected-gradient bounds at a failed poll [S120 pp. 15–16].
     - S124 gives exact oracle-count bounds [S124 pp. 10–11].
     - The MADS line itself stays asymptotic [S053 pp. 11–20; S172 pp. 12–15].
   - *Change*: "worst-case complexity is absent from the MADS line. It appears in a zeroth-order gradient-estimation paper (S140), and exact or local quantitative bounds appear in S120 and S124."
   - The Roundtable inference that StoMADS shares probabilistic-estimate conditions with the Scheinberg school is now verified: its analysis borrows devices from that line [S053 pp. 2, 12]. Remove the "(inference)" tag.
4. **Heuristic 9, Warning sign 6, Taste mark 3: "keep the direct-search backbone".**
   - *Full texts*:
     - RAMSA has no mesh and no poll; its convergence comes from a multi-timescale stochastic-approximation ODE argument [S150 pp. 14–17];
     - SSO exports the Search/local split to a stochastic gradient method with no mesh [S140 pp. 7–8].
   - *Change*: "keep a convergence backbone (direct search in most of the corpus; stochastic approximation in the Couderc line)". Both papers are coauthored works of a doctoral line and are weighted accordingly.
5. **Method 5 practice and Agentic Protocol step 5: StoMADS on the YATSOp/STARS problems.**
   - *Full text*: the version read (arXiv v1) tests 66 unconstrained instances of 22 Moré–Wild CUTEst sum-of-squares functions with artificial noise [S053 p. 21]. The published COAP version was not read.
   - *Change*: mark YATSOp/STARS as version-dependent (published version or repository), not verified in the text read.
6. **Method 1 practice: "CatMADS categorical neighborhoods" listed among Search-step contributions.**
   - *Full texts*:
     - in CatMADS the categorical neighbourhoods feed an extended poll that is "labeled as a poll, since it affects the convergence guarantees" [S121 p. 6; also pp. 15, 21];
     - the surrogate-based neighbourhoods also live in the poll and keep the theory because "the proposed method remains an instance of the CatMADS framework" [S157 p. 21].
   - *Change*: move CatMADS out of the Search list and into Method 7 (inheritance through a framework) and a Method 1 variant (a Poll-side idea).
7. **Inner Tensions ("Audet's own flagship needed an erratum (2008)") and Honest Boundary ("erratum not read").**
   - *Full text*: the erratum states that "even though the statement of Proposition 4.2 is correct, its proof is not compatible with the final notation". It restates the proposition as three checkable conditions and re-proves each one [D001 pp. 1–2].
   - *Change*: call it a proof erratum and lift "not read".
8. **Method 5 limitation and Honest Boundary: "The 2026 benchmarking summary was not read in full".**
   - *Full text*: it has now been read in full, as a preprint [S128 pp. 4–16], together with its GERAD twin [S101]. Lift the limitation.
9. **NOMAD quotes in Methods 1 and 2.**
   - Two quotes are not in the 3.7.2 guide that was read. The Search being "constrained by the theory to return points on the underlying mesh", and Mads-PB being "not very good" for equalities, come from the NOMAD 4 documentation (EQPB does not exist in 3.7.2) [S019 card, synthesis note].
   - The 3.7.2 counterparts are "The search step is crucial in practice because it is so flexible, but it is a difficulty for the theory for the same reason" [S019 p. 16] and "the MADS theory assumes that trial search points must be lying on the current mesh" [S019 p. 100].
   - The other guide quotes can now carry 3.7.2 page numbers: preface scoping [S019 p. 11], EB/PB/hidden constraints and CSTR [S019 p. 53], defaults as a compromise [S019 p. 73], bug reports [S019 p. 18], batch-mode crashes [S019 p. 48], tricks table [S019 p. 74].
   - *Change*: keep the two NOMAD 4 quotes with their NOMAD 4 source, and add 3.7.2 pages to the rest.
10. **Academic Lineage: formal advisor ⚠.**
    - *Full text*: the jury page of the November 1997 thesis names B. Jaumard as *directrice de recherche* and G. Savard as *codirecteur*. J. Gauvin chaired, and P. Marcotte and J.-P. Vial were members [S070 pp. 1–3].
    - *Change*: resolve the ⚠. Add downstream: M. A. Abramson (Rice PhD 2002), whose committee Audet co-chaired with Dennis [S213 pp. 1, 5].
11. **Research Trajectory rows.**
    - (a) The move to derivative-free methods starts in November 1998 at Rice [S025 TR p. 2]. Exact QCQP work continues in parallel: S010 is a Rice CRPC report of January 1999 [S010 pp. 1–2].
    - (b) The extremal-polygon side line starts in the 1997 thesis, with Graham's octagon [S070 pp. 166–171], and runs to 2022 [S113 pp. 1–2; S142 p. 9; D003 pp. 5–7], not only 2002–2013.
    - (c) The game-equilibria line runs to 2014 [S134 pp. 1, 13].
    - (d) The MADS anatomy "Origin" can cite text instead of an inference. The 2000–2003 AFOSR report states the fixed-direction limitation of GPS as the research problem and MADS as the fix [D016 p. 4], and the filter paper states the finite-direction limitation [S005 pp. 1–2, 20–27].
12. **Method 2 step 3 and Heuristic 1: "relaxable and quantifiable → PB".**
    - *Full texts*: when evaluations are interrupted or run at low fidelity, relaxable constraints are run under EB because interrupted points return no true values [S123 pp. 3, 6; S112 pp. 16, 20; S173 pp. 7, 18].
    - *Change*: record this as a variant. The algorithm's need can override the semantic default.
13. **Anti-pattern "wrapping a crashing simulator with a large finite penalty".**
    - *Full text*: DiscoMads deliberately makes STYRENE return an artificially high value on hidden-constraint failures, so that its discontinuity detector can see them [S090 p. 22].
    - *Change*: scope the anti-pattern to smooth or model-based solvers, as its wording already implies.
14. **Method 4 steps 2 and 5 (variables scaled to [0,100]; best-known solution).**
    - *Full texts*:
      - SOLAR keeps physical units and some unbounded integers [S071 pp. 17–18];
      - it credits best-known values rather than points [S071 pp. 23, 28];
      - the Micro-PRIAD report prints neither starting points nor best-known values [D006 pp. 13, 20].
    - *Change*: present these steps as the STYRENE/MDO pattern, not a universal rule.
15. **Heuristic 8 (deterministic for repeatability).**
    - *Full texts*:
      - from NOMAD 3.7.1, OrthoMADS directions come from a seeded pseudo-random generator, and "Halton directions are deprecated" [S202 p. 104]. Repeatability now rests on the seed;
      - randomness is added on purpose when a guarantee needs dense, non-shrinking sampling (revealing poll), at the price of almost-sure results [S138 pp. 7–9; S090 p. 10].
    - The deterministic motive itself is confirmed: "Because of the random component of LTMADS, we felt that numerical experiments had to be performed on series of several runs" [S006 p. 3].
16. **Taste mark 3 ("practical freedom never costs the theory").**
    - *Full text*: in an application-led collaboration (Audet second of three authors), a constrained filter-MADS variant was run while the authors stated that "no convergence proof has been published yet for the MADS technique with the filter approach", and PB was deferred [S039 pp. 11, 18].
    - *Change*: keep mark 3 for Audet-led algorithm papers, and mark it as an aim rather than a rule for collaborations.
17. **Method 5 step 3 ("competitors from at least one other family").**
    - *Full text*: the benchmarking summary bounds this step. Derivative-based competitors are excluded, and the number of algorithms is kept "very low" because performance profiles switch [S128 pp. 5, 9, 13–14].
    - *Change*: "include another derivative-free family on its home ground, a few algorithms at a time".

**Recorded without change** (low weight or out of scope):
- **S174†** (Methods 3 and 5). A power-systems paper that Audet did not lead [S174 pp. 3, 5, 7, 9–10].
- **S186 and S107** (Method 5). Application papers led by collaborators that use NOMAD as a tool, with single runs [S186 p. 6; S107 pp. 11–19]. Scope Method 5 to algorithm papers.
- **S116** (Method 3). An algorithmic GERAD report with no convergence analysis [S116 pp. 5–10]. Its companion PBTR paper carries the theory [S063 pp. 14–16].
- **S117** (Method 4). A side-line geometry paper without model files; S142 does release its AMPL models [S142 p. 9].

### 3.2 Variants by method (practice that differs from the SKILL.md wording, without contradicting it)

**Method 1**
- *Other slots the proof does not see*:
  - poll ordering [S016 pp. 6, 20; S114 p. 10; S143 p. 10];
  - evaluation order under opportunism [S072 p. 6];
  - a wrapper around the blackbox [S112 p. 14; S173 pp. 6–7; S064 pp. 6, 10; S039 pp. 6–7].
- *Poll-side ideas, admitted by inheritance rather than by the Search* (Method 7):
  - neighbour sets [S028 pp. 9–10; S031 pp. 4–6];
  - pruned directions [S029 pp. 13–15];
  - anisotropic meshes [S061 pp. 6, 8];
  - a revealing poll [S090 pp. 10, 13];
  - categorical neighbourhoods [S121 p. 6; S157 p. 21];
  - the default n+1-th direction chosen by a quadratic model [S019 pp. 55, 83].
- *Inversions*:
  - a mandatory covering step carries the guarantee and the poll becomes optional [S137 pp. 9–10; S155 pp. 7–8];
  - an outer-parameter gate shares the proof with the Poll [S158 pp. 5–7].
- *Sequencing instead of nesting*:
  - a global heuristic runs before MADS, with the handover measured in MADS's own failure unit [S073 pp. 21–24; S166 pp. 7–8];
  - a variable-block split [S151 pp. 3–5].
- *Exact-optimization ancestor*: a heuristic proposes and branch-and-cut certifies [S015 pp. 3, 9–11; S050 pp. 11–14; S070 pp. 74–78, 168–169; S037 pp. 6–14; S098 p. 4].
- *No direct search at all*: [S150 pp. 14–17; S140 pp. 7–8]. The PB module is exported to a trust-region method [S063 pp. 10–12].

**Method 2**
- *Semantics applied to inputs*: categorical, meta and decreed variables [S011 pp. 2–3; S058 pp. 7–11; S092 pp. 8–12].
- *Early work classifies constraints by form* (linear vs nonlinear) rather than relaxability [S031 pp. 1, 7; S022† pp. 13–14]. The same classification is in the co-directed programme [S213 pp. 16, 56–57].
- *EB-only phases in early MADS work*, with PB named as the future fix [S001 pp. 2, 4, 7; S027 pp. 22, 26; S061 pp. 7, 15].
- *Evaluation cost and pipeline position as new axes*; EB chosen so that evaluations can be interrupted [S123 pp. 2–3, 6, 8; S112 pp. 16, 20; S173 pp. 1, 5, 7, 18].
- *Equalities*:
  - removed by reformulation [S064 pp. 4, 6; S066 p. 4];
  - given their own penalty mechanism [S158 pp. 3–4, 7].
- *Lagrangian or augmented-Lagrangian handling outside MADS* [S150 p. 13; S116 pp. 5–7].
- *Partner-led application papers without a stated EB/PB choice*: they give no evidence for step 3 either way [S204 pp. 15–18; S069 p. 12; S060 p. 7; S160† pp. 8–9].

**Method 3**
- *Outside DFO, rigor takes the form of certificates* rather than ladders:
  - ε-optimal branch-and-cut [S010 pp. 17, 21–22];
  - interval branch-and-bound certificates with the tolerance written into the theorem [S080 pp. 9–12; S117 pp. 1, 10; S142 pp. 1, 9];
  - bound sandwiches with stated gaps [S093 pp. 6–10; S113 pp. 2, 6–8; S152 p. 14];
  - an iff reduction to infeasibility [D003 pp. 5–7].
- *Ladders along other axes*:
  - cost vs strength of the optimality notion [S121 pp. 12–14, 20];
  - properties of direction sets [S120 pp. 6–15];
  - probabilistic [S053 pp. 11–20; S084 pp. 10, 15–19];
  - smoothed → original → feasible [S150 pp. 11–17].
- *Ladders imported or inherited rather than built* [S039 pp. 9–11; S121 pp. 15, 17–18; S123 pp. 4–5; S016 p. 10].
- *Counterexamples aimed at measuring instruments and benchmark logs* rather than theorems [S004 pp. 7–10, 13, 18; S156 p. 11].

**Method 4**
- *No public release is mentioned for most partner blackboxes*. Public artifacts come from purpose-built benchmark papers [S071; S130; S175; D006] or, once, a scaled-down public twin [D006 pp. 4, 6, 22]; S074's cheaper surrogate problem has no stated public release [S074 pp. 3–4].
- *Synthetic collections built by documented transformations* (Cat-Suite) [S130 pp. 5–7].
- *The artifact is a tool front end*, not an instance [S159 pp. 7, 16, 19].
- *Printed instances in the pre-web era* [S070 pp. 157–167; S010 pp. 25–26].
- *Released code that needs a commercial solver*: [S160† pp. 4, 9–10].

**Method 5**
- *Most algorithm papers compare variants inside NOMAD* (list in §2.2).
- *Currency*:
  - CPU time, nodes and cuts in the exact-optimization era [S010 p. 23; S015 pp. 10–13; S050 pp. 18–23; S070 pp. 79–84];
  - blackbox time when evaluation times differ, with preprocessing charged [S112 pp. 16–19; S163 pp. 15–18; S173 pp. 18, 23];
  - Monte Carlo draws [S084 pp. 19–20].
- *Solvers anonymized in methodology papers* [S128 p. 4; S156 p. 15; D006 p. 21].
- *Application papers use single runs* [S204 pp. 17–19; S186 p. 6; S107 pp. 11–19; S184 pp. 16, 22–24; S160† pp. 9–11].
- *Qualitative claims in the software manual* are deferred to benchmark studies not reported there [S019 pp. 53, 73, 95–97].

**Method 6**
- *Pre-NOMAD instruments* were exact research codes reused across papers: the thesis QCQP branch-and-cut [S070 p. 79; S015 pp. 8–9; S037 pp. 6, 11, 14; S098 pp. 3–4] and interval branch-and-bound [S108 pp. 12, 14–15, 20].
- *Other lines ship separate packages* (XGame) [S076 p. 10; S134 p. 3].
- *Prototypes outside NOMAD*, with integration later or never [S063 p. 16; S064 p. 24; S084 p. 19; S120 p. 21].
- *The instrument is the post-processor* [S128 p. 16] or a wrapper [S173 pp. 18, 23].
- *Benchmark and solver come from the same group* [S071 pp. 3, 24; S175 p. 12], so the Method 6 limitation "a single codebase can bias the benchmarks it defines" stays relevant.

---

## 4. Promotions

### 4.1 Decision summary

- SKILL.md has **6** core methods, so one slot is left before the cap of **7**.
- **Clusters with at least 3 distinct full Audet cards that pass all four checks**:
  - *theory by inheritance*: generalize-and-recover plus framework theorem with plug-in instance, 25 full cards;
  - *surrogates judged and used as rankers*: 9 full cards;
  - *user-defined neighbourhoods as a priced optimality knob*: 4 full cards;
  - *rival-failure and adversarial counterexamples, plus instrument audits*: 8 + 3 full cards.
- **Decisions**:
  - Promote *theory by inheritance* as **Method 7**. It has the largest evidence base, and it explains about twenty Method 1 and Method 3 variant notes where a Poll-side or framework-level change needed no new proof.
  - Once at 7, the other three passing clusters are promoted by **merging into the existing method whose logic they share**: rankers into Method 1, neighbourhoods into Method 2, adversarial counterexamples and instrument audits into Method 3.
  - **No method is replaced.** The weakest candidates for replacement are Method 5 (most variants) and Method 4 (partner problems mostly private). Both still have at least 26 full evidence cards over six periods (§2.1), and their variants re-scope them rather than refute them.
- **Clusters with at least 3 full cards that fail at least one check** become heuristics or method steps (§4.4, §5).

### 4.2 New core method: Method 7, "Generalize, then inherit"

**One line**: Design each new algorithm so that the previous one is a special case of it and it is itself an instance of a framework whose theorems are already proved. Then prove membership (a short list of instance obligations, a parameter map, finitely many adaptive changes) instead of a new convergence theory.

**Steps**
1. **Write the framework's theory once**, against a short list of instance obligations.
   - The MADS results rest on mesh/frame properties plus dense refining directions [S001 pp. 13, 26].
   - OrthoMADS discharges four instance axioms and inherits everything [S006 p. 14].
2. **Make each new rule collapse to the old rule when the new feature is off**:
   - Δᵖ = Δᵐ gives GPS [S001 p. 4];
   - h^max_0 = 0 with a feasible start gives MADS-EB [S007 p. 12];
   - r_d = 0 gives Mads [S090 p. 6];
   - the cosine measure relative to ℝⁿ is the classical one [S120 p. 5];
   - bilevel profile groups (nx+1)(ny+1) reduce to np+1 when ny = 0 [S156 p. 14].
3. **Prove instance membership, in both directions.** Prove the new method is an instance of the framework. Also prove that your own earlier flagship is an instance of the new framework, via a parameter map and an induction on iterations:
   - OrthoMADS and QRMADS are ADS instances [S129 pp. 16–19];
   - LTMADS is a MADS instance [D001 pp. 1–2];
   - PSD-MADS is an "apparent pollster" MADS [S027 pp. 14–16];
   - a cheaper variant is proved to take the baseline's decisions [S123 p. 4].
4. **Let every adaptive mechanism change only finitely often**, then invoke the old analysis after the last change:
   - merge-only regrouping [S074 pp. 12, 14];
   - at most one weight change per constraint [S144 p. 10];
   - finitely many barrier migrations [S158 pp. 18–19];
   - a categorical distance frozen after some iteration [S121 p. 15].
5. **Where inheritance fails, say exactly what is lost**, or build new analysis only for that part:
   - PSD-MADS loses the zeroth-order result [S027 p. 17];
   - dynamic models void the decision-equivalence [S123 p. 4];
   - StoMADS rehosts a supermartingale argument [S053 pp. 12–19].
6. **State the inheritance in one sentence and separate the classes with one example**:
   - "remains an instance of the CatMADS framework" [S157 p. 21];
   - "reduce seamlessly to existing results" [S031 p. 1];
   - GPS converges to a saddle where MADS cannot [S020 pp. 13–15];
   - toy functions f1 and f2 separate SDDS and MADS from ADS [S129 pp. 5–6].

**Four checks**
1. *Cross-project recurrence* ✅. There are 25 distinct full Audet cards across six five-year periods, 2001–2026: S011, S002, S005, S001, S020, S031, S027, S006, S007, S062, S074, S061, S144, S021, S090, S123, S058, S092, S120, S121, S129, S137, S155, S156, S157. They span mixed variables, constraints, parallelism, directions, discontinuities, interruption, measures, frameworks and software. Supporting devices appear in D001, S016, S099, S133, S138, S158, S186 and S104.
2. *Say–do* ✅.
   - Stated in the papers: [S031 p. 1]; "The convergence results for ORTHOMADS follow directly from those already published for MADS" [S006 p. 1]; [S157 p. 21]; the covering step is "a self-sufficient algorithmic step" for "any algorithm it is fitted into" [S137 p. 10].
   - Stated in the software documentation as an extension contract [S019 p. 100; S021 pp. 6–7, 11].
   - Practiced in the proofs: Theorem 2.8 [S006 p. 14]; Theorem 4.6 [S129 pp. 17–18]; Props 4.1–4.3 [S027 pp. 15–16].
3. *Executable, different from standard practice* ✅. Each step leaves a concrete artifact: an obligation list, a collapse parameter, a parameter-map proof, a finite-change rule. The default elsewhere is a fresh convergence proof per variant. The corpus itself does that only where membership cannot give the result [S053 pp. 12–19; S084 pp. 12–18].
4. *Exclusivity* ✅ (moderate).
   - Framework theorems exist elsewhere. The corpus builds on Torczon's GPS framework [S002 pp. 1, 11], so "use a framework" alone is not exclusive.
   - Distinctive to this corpus:
     - re-proving one's own flagship as an instance of each successor framework: GPS → MADS [S001 p. 4], MADS → ADS [S129 pp. 16–18], MV-MADS neighbourhoods inside CatMADS [S121 p. 7];
     - eventually-static adaptation as the standard admission ticket for adaptive heuristics [S074; S144; S158; S121];
     - the theory contract exposed as a software extension point [S019 p. 100; S021 pp. 6–7].

**Applies to stage**: algorithm design, theory, software design.
**Different from standard practice**: new variants usually come with new proofs. Here membership in an already-proved class is the default, and new analysis is reserved for what membership cannot give.
**Limitations**:
- A method inherits only what the parent class proves: asymptotic, Clarke-type results [S023 p. 7].
- Stochastic variants and wrappers do not inherit automatically:
  - the application survey says stochastic variants lack the same guarantees [S013 p. 3];
  - the Inter-DS paper states inheritance at the solver level [S112 p. 14];
  - the IDS paper analyses only its assignment subproblem [S173 pp. 10–16].
- Instance proofs must be kept in the final notation of the paper [D001 p. 1].

**Revision after review (2026-09-27)**
- *Exclusivity narrowed*: the framework proof and the collapse check (steps 1–2 above) are shared ground with the Conn lens (framework theorems, one-component reduction checks) and the Vicente lens (collapse check as a standard sub-step). Check 4 therefore passes only for three devices: re-proving one's own flagship as an instance of each successor framework, eventually-static adaptation, and the theory contract as the software plug-in interface. SKILL.md Method 7 is narrowed to these devices and marks exclusivity ⚠ moderate, with an Honest Boundary line.
- *Recount*: counting only cards that carry an instance, collapse or finite-change proof gives 22 distinct cards: S001, S002, S005, S006, S007, S011, S020, S021, S027, S031, S061, S074, S090, S120, S121, S123, S129, S144, S155, S157, S158, D001. S156 (a benchmark normalization that reduces to n+1), S062 (an equivalence of bilevel definitions), S058 (a notation framework), S092 and S137 are dropped as weak support; D001 (an instance proof) and S158 (a finite-change proof), listed above as supporting devices, are counted.
- *Step 1 made concrete*: the four MADS instance properties OrthoMADS discharges are listed verbatim in SKILL.md [S006 p. 14].

**Relation to Methods 1 and 3**
- Method 1 is the special case where the new idea sits in the Search. Method 7 covers ideas that change the Poll, the mesh or the acceptance rule [S001; S006; S061; S090; S121; S129; S158].
- Method 3 states and audits a guarantee; Method 7 constructs it cheaply. The two appear together in the same papers [S001 pp. 11–13; S129 pp. 7, 11–18].

### 4.3 Promotions by merging (cap reached)

**(a) Surrogates judged and used as rankers → Method 1, new step between steps 2 and 3.**
- *Proposed step*: "If a surrogate or model cannot be trusted to accept or reject points, use it only to order trial points (Poll or Search) under opportunistic evaluation. Select or tune it by order or feasibility agreement (order error, rank correlation), not by fit error."
- *Four checks*:
  - recurrence ✅: 9 full cards over 2006–2020 [S016; S074; S023; S046; S068; S114; S167; S072; S143], plus reuse in 2022 [S099 pp. 5, 11];
  - say–do ✅: a poor but similar surrogate is still useful for ordering [S023 pp. 13–14]; "Our main concern in SBO is to find the correct optimizer, not necessarily the correct optimum" [S046 p. 6]; a surrogate "should be used to assist the process of optimizing the original problem, not substitute it entirely" [S068 p. 5]; ordering "has no impact on the convergence analysis" [S072 p. 6];
  - executable ✅: order-error metrics OE/OECV [S046 pp. 12–13]; leave-one-out order error to tune a hyperparameter [S068 pp. 12–13]; Spearman correlation plus a scatter zoomed on the optimal zone [S167 p. 8]; the Poll reordered but never pruned [S016 pp. 6, 10];
  - exclusivity ✅ (partial): fit-based model choice is the norm, and the metrics rank the same models differently [S046 pp. 14–15]. Comparison-based surrogates exist in evolutionary computation, but their pairing with the opportunistic ordering slot of a convergent method is specific.
- *Why merge rather than promote*: the logic is Method 1's own, a slot the proof cannot see [S072 p. 6; S016 p. 10]. Three of the nine cards were already recorded as Method 1 evidence or variants [S016; S114; S143].

**(b) User-defined neighbourhoods as a priced optimality knob → Method 2, generalized to "semantics first, for inputs as well as outputs".**
- *Proposed step*: "For categorical or meta variables, have the user define the neighbourhood that fixes what 'local' means (or learn it once from data). Offer stronger optimality as an explicit knob with a stated evaluation price."
- *Four checks*:
  - recurrence ✅: S011 (2001), S028 (2001), S031 (2007), S121 (2025), with S058 and S092 in support; the co-directed programme has the same idea [S213 pp. 76–78, 133];
  - say–do ✅: "It would be surprising if one could run the simulation code with a continuous variable where the simulation expects a discrete input" [S011 p. 2]; speed and quality depend "on the user-defined set of neighbors" [S028 p. 13]. Practiced with measured prices: separate evaluations to find and to certify, with a ξ = 5% extended poll [S011 p. 22]; knowledge-restricted neighbours cost about 90% fewer evaluations for about 5.7% worse f [S028 p. 18]; ξ chosen by data profiles [S121 pp. 20, 23];
  - executable ✅;
  - exclusivity ✅: Bayesian optimization and metaheuristics are the usual routes for categorical variables, and they lack these guarantees [S121 p. 3].
- *Why merge*: the cards already record these papers as Method 2 variants (card label: semantics first applied to inputs) [S011; S058; S092].

**(c) Adversarial-but-legal instances, rival-failure toys and instrument audits → Method 3, revised steps 2 and 4.**
- *Proposed wording*:
  - Step 2 becomes "break each hypothesis with a small example; when the algorithm has free choices (Search, pattern, polling order), choose them adversarially but legally".
  - Step 4 becomes "run the same audit on the theorem you build on, on the rival method (a toy where it fails) and on your measuring instruments (indicators, surrogate-quality scores, benchmark protocols)".
- *Four checks*:
  - recurrence ✅: 1998–2026, with S025 (TR), S020, S005, S007, S062, S001, S129, S138 and S172, plus instrument audits in S004, S016, S156, S046, S099 and S144;
  - say–do ✅: "We admit that the flexibility in the choice of polling directions is exploited to lead to a weak result, but our point is that it can happen" [S005 p. 24]; a hypothesis-violating limit run "to run the algorithms to their limits" [S001 p. 25]; "A referee does not certify the admissibility of a point" [S156 p. 11];
  - executable ✅:
    - geometrically scaled copies of one polynomial [S138 p. 4];
    - a period-3 induction table [S020 pp. 13–15];
    - an adversarial Search step at iterations 3ℓ+2 [S007 pp. 19–21];
    - a toy problem figure before the algorithm [S172 pp. 7–8];
    - one counterexample per indicator [S004 pp. 7–10];
    - invariance thought experiments [S099 p. 8];
    - rescaled twin problems [S144 pp. 13–14];
  - exclusivity ✅: most convergence papers stop at sufficiency.
- *Why merge*: this is Method 3's own discipline extended to new targets, so a separate method would add no explanatory unit.

### 4.4 Evaluated, not promoted (at least 3 full cards, at least one check failed)

| Cluster | Full cards | Recurrence | Say–do | Executable | Exclusive | Outcome |
|---|---|---|---|---|---|---|
| Cheap-first evaluation gating and interruption | 9: S001, S019, S059, S069, S112, S123, S175, D006, S022† (+ S005, S064, S071, S173) | ✅ 2004–2026 | ✅ [S019 pp. 11, 51, 64; S001 p. 4] | ✅ | ✗: checking cheap constraints first is common engineering practice. The distinctive part (the proof needs it [S001 p. 4]; count flags [S071 pp. 18–23; D006 p. 30]) is already Method 2/4 content | Method 2 step + heuristic N1 |
| Evaluation cache as shared memory and data source | 4: S019, S027, S073, S090 (+ 10 supporting, e.g. S125, S158, S172) | ✅ 2008–2026 | ✅ [S019 pp. 58, 80, 96, 98–99] | ✅ | ⚠: caches are standard in DFO codes. Only the use of cached points inside proofs is distinctive [S090 pp. 12, 15–16; S172 pp. 14–15] | Method 6 practice + heuristic N1 |
| Same-solver controlled comparison / ablation | 4: S006, S029, S061, S172 (+ S001, S019, S063, S116, S129, S158) | ✅ | ✅ [S172 p. 20; S019 p. 83] | ✅ | ✗: ablation is standard practice | Method 5 step + heuristic N3 |
| Common effort currency with explicit weights | 4: D006, S101/S128, S155, S156 (+ S084, S019, S112, S173, S007, S027) | ✅ 2008–2026 | ✅ [S128 p. 15] | ✅ | ⚠ | Method 5 step 1 extension + N4 |
| Solver-agnostic wrapper | 4: S039, S112, S173, D006 (+ S064, S095, S186, S074) | ✅ 2010–2026 | ✅ [S112 p. 14; S173 pp. 6–7] | ✅ | ⚠ | Heuristic N5 + Method 1 variant |
| Proposer–certifier / price the proof | 4: S015, S050, S070, S011 (+ S098, S037, D007) | ⚠: mostly 1997–2004 | ✅ [S015 p. 9] | ✅ | ⚠ | Heuristic N6 (exact-optimization era, transfers via S011) |
| Audit inherited instances | 5: S010, S015, S028, S057, S070 (+ S048, S040) | ✅ 1997–2010 | ✅ | ✅ | ⚠ | Heuristic N7 / Workflow D step |
| Reformulation as a lens | 4: S050, S070, S076, S093 (+ S062, S064, S124, S151, S155; 10 abstract cards 1994–2009) | ✅ 1997–2026 | ✅ [S070 pp. 20, 174] | ✅ | ✗: the GERAD school's shared tool, not Audet-specific | Heuristic N10 |
| Cross-family transplant and retuning | 6: S053, S063, S116, S124, S129, S158 | ✅ 2016–2026 | ✅ [S063 p. 13; S158 pp. 1, 3] | ✅ | ✗: cross-pollination is common | Heuristic N8 |
| Couple auxiliary parameters to the step size | 3: S053, S140, S158 (+ S129) | ✅ 2021–2026 | ⚠: stated only in [S053 p. 9] | ✅ | ⚠ | Heuristic N8 (algorithm design) |
| Train/held-out split for tuning | 4: S057, S073, S095, S150 | ✅ | ⚠ [S073 p. 6] | ✅ | ✗: standard in ML | Revise Heuristic 7 |
| Nested split: DFO on the pathological block | 3: S151, S155, S186 (+ S095) | ✅ 2021–2026 | ✅ [S151 p. 3] | ✅ | ⚠ | Revise Heuristic 9 |
| Catalogue open cells, then fill them | 7: S040, S080, S093, S108, S117, S146, S034 (+ S092, S156, S084, S004) | ✅ | ✅ [S080 p. 2] | ✅ | ⚠ (mostly side line) | Heuristic N9 (topic choice) |
| Public self-correction | 3: D001, S040, S173 (+ S132) | ✅ | ✅ | ⚠ | ⚠ | Method 3 step 4 practice only |
| Seeded start relay | 4: S204, S186, S184, S022† | ✅ | ⚠ | ✅ | ⚠ | Pool: collaborator-led papers only |
| Extremal-geometry numeric-first, certificate-later | 12 (see §6) | ✅ 1997–2022 | ✅ | ✅ | ✅ | Kept out of core by instruction: side line. Its transferable devices go to §7 |

---

## 5. New heuristics

Each item is executable and passes at least one more check. "Checks" lists R (recurrence), S (say–do) and X (exclusivity).

| # | If … then … | Evidence | Checks | Placement |
|---|---|---|---|---|
| N1 | **If some outputs are cheaper than the full simulation, or earlier in its pipeline, then evaluate them first, stop as soon as the point can no longer become the incumbent, flag a-priori rejections as not counted, and mine the cache before paying for a new evaluation** (seed x0 and initial mesh sizes, sensitivities, re-scoring after a merit change) | Gating: [S001 p. 4; S019 pp. 11, 51, 64; S059 p. 10; S069 p. 10; S123 p. 3; S112 pp. 7–8; S175 p. 10; D006 pp. 13, 17, 30]. Cache: [S019 pp. 58, 80, 98–99; S027 pp. 11–12; S073 pp. 22–23; S090 pp. 8–12; S125 p. 10; S158 p. 20; S172 pp. 14–15] | R, S | New H2 ("evaluation economy"), merging the cache into the same heuristic |
| N2 | **If a model is not trustworthy enough to accept points, then use it only to order candidates under opportunism, and judge it by order error** | §4.3(a) | R, S, X | Replaces H3. The Search content of H3 stays in Method 1 |
| N3 | **If you claim a mechanism works, then first compare it with the baseline inside one code base where every other component is shared** (quadratic models off or on in both, same direction generator, the solver's current default included). **Only then add other derivative-free families on their home ground, a few at a time** | [S001 p. 19; S029 pp. 14–15; S061 p. 14; S129 pp. 19, 23; S172 pp. 16–17, 20; S158 p. 18; S019 p. 83]; bound [S128 pp. 5, 9] | R, S | Merge with H6 |
| N4 | **If methods differ in what one "evaluation" costs, then charge everything in one currency with explicit weights** (N = N_t + w·N_s; 1+τ per reformulated call; λ·N_UL + N_LL; preprocessing time on the axis) **and show that the verdict holds for more than one weight** | [S128 p. 15; S155 pp. 19, 25, 27; S156 pp. 13–16; D006 p. 22; S084 pp. 19–20; S112 pp. 18–19] | R, S | Method 5 step 1; merge with H6 |
| N5 | **If the idea concerns evaluation cost (fidelity, interruption, uncertainty), then put it in a wrapper around the blackbox so that any solver runs unchanged. Pay for one true evaluation before a cheap verdict changes the incumbent** | [S039 pp. 6–7; S064 pp. 6, 10; S112 pp. 7–8, 14; S173 pp. 6–8; D006 p. 26] | R, S | Merge with H9 |
| N6 | **If a heuristic feeds an exact or certified method, then price the proof separately**: run cold and warm, and report evaluations to find vs evaluations to certify | [S015 p. 9; S070 p. 168; S098 p. 4; S050 pp. 19–25; S011 p. 22] | R, S | Workflow D step (not in the top-10 list) |
| N7 | **If you benchmark on inherited instances, then first re-derive or re-evaluate them**: publish which collapse to easy cases and which published solutions reproduce | [S015 pp. 7–9; S070 pp. 125, 160; S010 p. 27; S028 pp. 14–15; S057 p. 14] | R, S | Workflow D step |
| N8 | **If you import a mechanism from another algorithm family, then re-prove it in your framework and retune every parameter that encoded the donor's evaluations per iteration. If it needs an auxiliary parameter that must vanish (accuracy, penalty, smoothing), tie it to the step size** | [S063 pp. 13, 20–22; S053 pp. 2, 9, 12–15; S158 pp. 1, 3, 6–7, 9–11; S116 p. 7; S129 p. 11; S140 pp. 6–7] | R, S | Workflow C steps |
| N9 | **If you are choosing the next problem, then map the problem family as a grid (fixed attribute × optimized attribute, or method × defect), mark each cell trivial, solved (by whom, for which cases) or open, and pick from the open cells** | [S146 pp. 2–3; S040 pp. 2, 15–16; S080 p. 2; S093 p. 11; S117 pp. 1–2, 10; S092 pp. 7, 10; S156 p. 10; S084 pp. 2–3] | R, S | Merge with H10 |
| N10 | **If a new problem class neighbours a solved one, then build a reformulation that provably transfers optimal (and local) solutions, give one counterexample per hypothesis, and carry tests, cuts or solvers across** | [S070 pp. 33, 96–97; S050 pp. 2, 10–11; S076 p. 8; S062 pp. 5–6; S064 pp. 8–10; S151 pp. 6–7; S155 pp. 9–11] | R, S | Workflow A/C step |

**Revisions to existing heuristics**
- **H1**: add that interrupted or low-fidelity evaluations push relaxable constraints to EB [S123; S112; S173] (§3.1 #12).
- **H4**: extend to adversarial-but-legal instances, rival-failure toys and instrument audits (§4.3c).
- **H7**: tune on one problem subset and report on held-out problems [S057 p. 18; S095 p. 9; S073 p. 6; S150 pp. 19–22]; later tuning papers hold out problems.
- **H8**: deterministic or seeded, with randomness only where the guarantee needs it [S202 p. 104; S138 pp. 7–9].
- **H9**: keep a convergence backbone instead of the direct-search backbone (SKILL.md wording) [S150; S140]. Add the nested split, with DFO on the pathological block and a specialized or certified solver inside [S151 pp. 3–5; S155 pp. 5–6; S186 pp. 4–5; S095 pp. 6–7].
- **H10**: the full texts confirm students as first or corresponding authors of the late categorical, multi-fidelity and penalty-interior-point papers [S121 p. 1; S157; S158 p. 1; S173 p. 1; S092 p. 1]. Formal supervision roles are still not stated in the texts.

**Recommended list after the update, keeping 10 heuristics**:
1. H1 + H2, merged: constraint semantics and crashes.
2. N1, evaluation economy.
3. N2, which replaces H3.
4. H4, revised.
5. H5, plus the benchmark-construction devices of §7.3 (census, transformations).
6. H6 + N3 + N4.
7. H7, revised.
8. H8, revised.
9. H9 + N5, revised.
10. H10 + N9.

N6, N7, N8 and N10 go into Workflows C and D as steps.

---

## 6. Candidate pool

All clusters formed from the 267 new-pattern candidates on the cards, grouped by reading, not by string match. "Candidate cards" counts every card that proposed the pattern. "Full" counts distinct full or partial Audet works. Supporting cards show the same device in their proofs or techniques without naming the pattern.

| Cluster | Candidate cards | Full, Audet-authored | Supporting full cards | Outcome |
|---|---|---|---|---|
| Generalize-and-recover + framework theorem with plug-in instance + eventually-static adaptation | 28 | 25: S001, S002, S005, S006, S007, S011, S020, S021, S027, S031, S058, S061, S062, S074, S090, S092, S120, S121, S123, S129, S137, S144, S155, S156, S157 (+ S017, S033 abstract; S213 programme) | D001, S016, S099, S104, S133, S138, S158, S186 | **Promoted: Method 7** |
| Surrogates judged and used as rankers | 9 | 9: S016, S023, S046, S068, S072, S074, S114, S143, S167 | S019, S099, S144, S157, S166 | **Promoted by merge into Method 1** |
| User-defined neighbourhood / optimality as a priced knob | 5 | 4: S011, S028, S031, S121 (+ S213 programme) | S058, S143 | **Promoted by merge into Method 2** |
| Rival-failure toys / adversarial-but-legal counterexamples | 9 | 8: S001, S005, S007, S020, S062, S129, S138, S172 (+ S025 TR) | S046, S092, S114, S120, S137, S144, S151 | **Promoted by merge into Method 3**; H4 revised |
| Audit the measuring instrument; invariance tests | 5 | 5: S004, S016, S156, S099, S144 | S046 | **Merged into Method 3** (with the row above) |
| Cheap-first evaluation gating and interruption | 9 | 9: D006, S001, S019, S022†, S059, S069, S112, S123, S175 | S005, S064, S071, S173 | Method 2 step + N1 |
| Evaluation cache as shared memory and data source | 5 | 4: S019, S027, S073, S090 (+ S055 abstract) | S046, S053, S114, S125, S129, S133, S158, S166, S172, S204 | Method 6 practice + N1 |
| Same-solver controlled comparison | 5 | 4: S006, S029, S061, S172 (+ S024 abstract) | S001, S019, S063, S116, S129, S158 | Method 5 step + N3 |
| Common evaluation currency with explicit weights | 4 | 4: D006, S101/S128, S155, S156 | S007, S019, S027, S084, S112, S173 | Method 5 step 1 + N4 |
| Solver-agnostic blackbox wrapper | 5 | 4: D006, S039, S112/S163, S173 | S064, S074, S095, S186 | N5 + Method 1 variant |
| MADS-as-subroutine composition | 7 | 2: S019, S027 (+ S018, S026, S078, S086, S091 abstract) | S013, S073, S133, S166 | Method 7 practice (inheritance through composition) |
| Proposer–certifier / price the proof | 6 | 4: S011, S015, S050, S070 (+ D009, S083 abstract) | D007, S037, S098 | N6 |
| Audit inherited instances; certify published solutions | 6 | 5: S010, S015, S028, S057, S070 (+ S105 abstract) | S040, S048 | N7 |
| Cross-family transplant and retuning | 6 | 6: S053, S063, S116, S124, S129, S158 | S140 | N8 |
| Couple auxiliary parameters to the step size | 3 | 3: S053, S140, S158 | S129 | N8 |
| Catalogue open cells, then fill them | 9 | 7: S034, S040, S080, S093, S108, S117, S146 (+ S082 abstract, S213 programme) | S004, S084, S092, S103, S156 | N9 |
| Reformulation as a lens | 14 | 4: S050, S070, S076, S093 (+ 10 abstract cards 1994–2009) | S062, S064, S124, S151, S155 | N10 |
| Train/held-out split for tuning | 4 | 4: S057, S073, S095, S150 (S016 is the original tuning-as-blackbox case) | S092, S118 | H7 revised |
| Nested split (DFO outside, specialized solver inside) | 3 | 3: S151, S155, S186 | S095 | H9 revised |
| Public self-correction and self-successor repair | 4 | 3: D001, S040, S173 (+ S154 abstract) | S132 | Method 3 step 4 practice |
| LHS feasibility census / benchmark non-triviality | 2 | 2: S071, S175 | S022†, S123, S157 | Method 4 step (§7.3) |
| Benchmark by documented transformation | 1 | 1: S130 | S072, S121 | Method 4 variant (§7.3) |
| Frozen versioned benchmarks, reproducibility switches | 1 | 1: S071 | S019/S202, S021 | Method 4/6 evidence |
| Noise census before comparisons | 1 | 1: S060 | D006, S016, S071 | Method 5 step 5 evidence |
| Report degenerate-to-baseline and failure instances | 2 (one work) | 1: S112/S163 | S029, S101, S133, S167 | Method 5 evidence |
| Scaled-down public twin of a proprietary blackbox | 1 | 1: D006 (S074 builds a cheaper test surrogate but states no public release) | S123 | Method 4 variant |
| Non-shrinking probes (revealing poll, covering step) | 2 | 2: S090, S138 | S137 | §7.1 technique |
| Terminology hygiene | 2 | 2: S002, S058 | S121 | §7.4 writing move |
| Extremal-geometry side line (numeric first, certified or exact later; analytic pruning; optimality conditions as cuts; ε-uniqueness) | 19 | 12: D002, D003, S037, S040, S070, S080, S094, S104, S108, S117, S142, S146 (+ 7 abstract) | S093, S103, S113, S118, S152, S177 | Side line, out of core (§7.1, §8) |
| Seeded start from another solver or stage | 5 | 4: S022†, S184, S186, S204/S145 | S107 | Pool: all collaborator-led |
| Build the missing blackbox-callable tool for a new field | 5 | 2: S159, S184 (+ S036, S042, S075 abstract/metadata) | — | Pool: 2 full, collaborator-led |
| Validate the blackbox physically before optimizing | 3 | 3: S107, S160†, S184 | S090 | Pool: S107 and S184 are one project |
| Report surrogate-to-truth reversals | 3 | 3: S074, S107, S184 | S112, S166, S173 | Pool (folded into N2's wording) |
| Price a constraint by relaxing it | 2 | 1: S160† (+ S078 abstract) | S019 | Pool |
| Exhaustive enumeration on a small instance as ground truth | 2 | 2: S060, S064 | — | Pool |
| Challenge the sophisticated model with the simplest operational baseline | 2 | 2: S032, S060 (one project) | — | Pool |
| Prefer hypotheses checkable or enforceable a priori | 2 | 2: S031, S137 | — | Pool |
| Give a menu or interval, not a single optimum | 3 | 1: S166 (+ S089/S215 abstract) | — | Pool |
| When the optimizer exploits a modelling gap, fix the model | 1 | 1: S028 | S160† | Pool |
| Reference works as a research output | 7 | 0 (D004, D005, S003, S082, S102, S122, S190: abstract or metadata) | S023, S034 | Rejected as method (§10) |
| Popular and historical accounts of the octagon results | 5 | 0 (S208/S207, S198, D011, S221: metadata) | — | Rejected (§10) |
| Community building and community-service OR | 3 | 1: D007 (+ D010, S218 metadata) | S071 | Rejected as method (§10) |
| Singletons (one card each, e.g. data-derived big-M S048, exact rational arithmetic S076, minimax-error parameter choice S010/S070, stability-weighted re-optimization D007, freeze gameable parameters S057, learned selection with random fallback S125, asymmetric scenario aggregate S069, round outputs to decision precision S073) | 1 each | — | — | Technique inventory where transferable (§7); otherwise pool |

---

## 7. Technique inventory

### 7.1 Proof devices

- **Failed-poll quotient read as one term of the Clarke derivative**, with limsup taken along refining subsequences [S002 pp. 9–10; S001 p. 12; S007 pp. 16–17; S031 pp. 16–19; S061 p. 20; S129 pp. 13–14; S172 pp. 14–15; S158 pp. 16–18]. The same device appears in the co-directed programme [S213 p. 89].
- **Integer-lattice argument for lim inf Δ = 0 with a rational τ** [S002 p. 8; S011 p. 12; S031 p. 13; S001 p. 7; S061 p. 19]. Later replaced by **exclusion balls plus packing**, which give a full limit [S129 p. 12; S172 pp. 12–13].
- **Density of directions**: a Halton sequence, a scaled Householder matrix and a density transfer through the reflection [S006 pp. 5–14]; counting integers to get a probability bound [S001 p. 18]; volume ratios for random revealing or covering probes [S090 pp. 14–15; S138 p. 8; S137 pp. 7–8, 16].
- **Adversarial-but-legal instances proved by induction over a periodic block**:
  - [S025 TR pp. 4–12; S020 pp. 13–15; S007 pp. 19–21; S005 pp. 24–25];
  - geometrically scaled copies of one polynomial [S138 p. 4; S007 p. 19].
- **One counterexample per hypothesis or converse** [S120 pp. 5–11; S151 p. 7; S137 pp. 11–12, 17; S092 p. 11; S144 p. 10; S070 pp. 43, 60, 84].
- **Eventually-static adaptation** [S074 p. 14; S144 p. 10; S158 pp. 18–19; S121 p. 15].
- **Decision equivalence or a parameter map plus induction**, to prove one algorithm is an instance of another [S123 p. 4; S129 pp. 16–18; S006 p. 14; D001 p. 2; S070 pp. 96–97].
- **Mirror proof** swapping (f, Ω) for (h, X) [S007 p. 18; S172 p. 15]. **Scale-then-limit**: multiply the failed-poll inequality by the penalty parameter [S158 pp. 12, 15].
- **Symmetric-direction cancellation / a never-evaluated mirror point** [S020 pp. 12–13; S120 pp. 15–16].
- **Stochastic analysis**:
  - a potential ν(f − f_min) + (1 − ν)Δ² with a 2×3 case split, and a log-step submartingale dominated by a random walk [S053 pp. 12–19];
  - the strong law of large numbers and Borel–Cantelli for adaptive precision [S084 pp. 12–18];
  - multi-timescale ODE analysis [S150 pp. 16–17].
- **Exchange lemma plus enumeration** for small design subproblems, instead of calling a MINLP solver [S112 pp. 12–13; S163 pp. 12–14; S173 p. 13].
- **Reformulation equivalence proofs**: optimal-solution transfer, local-optima transfer, and the hypertangent cone preserved by a linear map [S070 p. 33; S064 pp. 8–10; S151 p. 6; S155 pp. 9–11; S062 pp. 5–6].
- **Side line, transferable only to certification tasks**:
  - incumbent-cutoff infeasibility and ε-exclusion constraints [S037 pp. 10–14; S117 p. 10; S142 p. 9; D003 pp. 6–7; D002 p. 5];
  - optimality conditions added as cuts [S108 p. 14; S037 pp. 12–14];
  - minimax error equalization to choose parameters [S010 pp. 13–16; S070 pp. 147–152].

### 7.2 Algorithm-design moves

- **Split an overloaded parameter** (mesh size vs poll size) so that the old method is the equal case [S001 p. 4]. Per-variable meshes [S061 pp. 11–12].
- **Put the idea where the proof cannot see it**: the Search (Method 1), the evaluation order [S016; S072; S114; S143], a wrapper [S039; S112; S173; D006].
- **Two incumbents**, feasible and least-infeasible, with dominance-driven monotone thresholds whose extreme value recovers the old rule [S007 pp. 6, 9–12; S005 pp. 8–9; S063 pp. 11–12].
- **Couple auxiliary parameters to the step size** [S053 p. 9; S158 pp. 6–7, 9–11; S129 p. 11; S140 pp. 6–7].
- **Cheap-first gating, interruption, and an incumbent guard** (pay for one true evaluation before accepting) [S001 p. 4; S019 pp. 51, 64; S123 p. 3; S112 pp. 7–8; S173 pp. 6–7; D006 pp. 13, 17, 30].
- **The cache as a data source**: initial mesh sizes, sensitivities, re-scoring after a merit change, cached points reused as poll points [S073 pp. 22–23; S125 p. 10; S158 p. 20; S172 pp. 14–15; S090 p. 12].
- **Convergent runs as subroutines** in drivers (biobjective, VNS, extended polls, decomposition) [S019 pp. 88, 90, 96–99; S027 pp. 11, 18–19; S013 p. 8].
- **Nested split**: DFO on the pathological block, and a specialized or certified solver inside [S151 pp. 3–5; S155 pp. 5–6; S186 pp. 4–5; S095 pp. 6–7].
- **Cross-family transplant with retuning** [S063 pp. 13, 20–22; S053 pp. 2, 12–15; S158 pp. 1, 3; S116 p. 7].
- **Optimality strength as a priced user knob** [S011 pp. 3, 8; S028 p. 18; S031 pp. 4–6; S121 pp. 20, 23].
- **Non-shrinking probes** (revealing poll, covering step) to reach stronger guarantees [S090 p. 10; S138 pp. 6–9; S137 pp. 7–10].
- **A priori checkable assumptions** preferred over run-dependent ones [S031 p. 20; S137 pp. 8, 12].

### 7.3 Experiment protocols

- **Effort currency with explicit weights, with every phase charged** [S128 p. 15; S155 pp. 19, 25, 27; S156 pp. 13–16; D006 p. 22; S084 pp. 19–20; S019 pp. 50, 79–82]. Feasibility and preprocessing phases are charged [S007 p. 25; S027 p. 22; S112 pp. 18–19].
- **Fair baselines**: common f0 and f*, instances flagged and dropped when no solver improves f0, a two-phase h-then-f plot for infeasible starts [S128 pp. 5–6, 10–11; S175 p. 11; S157 pp. 22–23]. S128 illustrates the switching effect of performance profiles by removing the fastest solver [S128 pp. 9, 13–14]; re-plotting without it is a check derived from that illustration, not a step the paper prescribes.
- **Same-solver controlled comparison** [S001 p. 19; S029 pp. 14–15; S061 p. 14; S129 p. 19; S172 pp. 16–17, 20; S158 p. 18; S019 p. 83].
- **Purpose-labelled problems**, including the competitor's home ground and a hypothesis-violating case [S001 pp. 3, 19–25; S063 pp. 17–23; S034 p. 1].
- **Noise census, seeds and replications**: 100 replications of one point [S060 p. 8], differences judged against two standard deviations [S060 pp. 11–12]; Micro-PRIAD uses ±3σ bands [D006 pp. 13–14]; also [S071 p. 25; S016 p. 21; S021 pp. 14–16; S027 p. 23; S006 p. 15; S150 pp. 18–19].
- **Held-out tuning** [S057 p. 18; S095 p. 9; S073 p. 6; S150 pp. 19–22].
- **Benchmark construction**:
  - an LHS feasibility census [S175 p. 9; S071 p. 24; S157 pp. 7–8; S123 p. 8];
  - a non-triviality certificate [S071 pp. 11, 24–32];
  - documented transformations of known problems and feasible-by-construction constraints [S130 pp. 5–7; S121 p. 19];
  - constraints of an existing realistic benchmark converted into the new class [S072];
  - frozen versioned releases and a self-check [S071 pp. 13–14, 20–21];
  - a switch that keeps old behaviour reproducible [S202 p. 110];
  - a parity check after a rewrite [S021 p. 14].
- **Price the proof**: cold vs warm runs, evaluations to find vs to certify [S015 p. 9; S070 p. 168; S098 p. 4; S011 p. 22].
- **Audit inherited instances** [S015 pp. 7–9; S070 pp. 125, 160; S010 p. 27; S028 pp. 14–15; S057 p. 14].
- **Mechanism diagnostics beside profiles**:
  - divergence-from-baseline tables [S173 pp. 19–23];
  - mechanism counters [S129 p. 23];
  - cumulative outcome ratios [S137 p. 15];
  - internal-quantity plots [S061 pp. 16–18];
  - direction-coverage plots [S006 p. 21].
- **Report losses and reversals**:
  - surrogate-to-truth reversals [S074 pp. 20, 22; S107 pp. 17–19];
  - the case the method loses [S032 pp. 27–28; S092 pp. 22–25; S114 p. 11];
  - a test set that favours the baseline [S129 pp. 21–22].

### 7.4 Writing moves

- **Open with the pathologies and scope the tool negatively** [S019 p. 11; S023 p. 7; S034 p. 1; S071 p. 3; S173 p. 3].
- **Pose *why not keep the existing method?*** (template question; S007 asks "what motivates us to undertake this research rather than to abandon the filter in favor of the barrier") and answer it with concrete user situations [S007 pp. 3–4].
- **Show a toy pathology figure before the algorithm** [S172 pp. 7–8; S129 pp. 5–6; S046 p. 13].
- **Position by similarity and difference**: *as in X … unlike Y* clauses (template) in the abstract [S007 p. 1]; a literature table whose columns are the gaps the paper fills [S156 p. 10; S092 pp. 7, 10].
- **Summarize the ladder** as a numbered hierarchy or a case → theorem → assumptions table [S002 p. 12; S007 pp. 24–25; S090 p. 14].
- **Write limitations as confessions with a point** [S005 p. 24; S001 p. 25]. **Say which rung is lost** [S027 p. 17].
- **Erratum style**: restate the result, split it into checkable bullets, and say whether the statement or only the proof is affected [D001 p. 1].
- **Terminology hygiene**: rename to what the proof uses, and avoid clashes with engineering terms [S002 p. 3; S058 p. 8; S121 pp. 13–14].
- **Open-problem ledger** with the blocker for each item [S108 pp. 18–19; S040 pp. 15–16; S093 p. 11]. The co-directed programme keeps one too [S213 pp. 170–175].
- **One running example through all definitions** [S058 pp. 5–6, 16–18; S006 pp. 4–7; S155 p. 2].
- **An itemized forecast in editorials** [S034 p. 2].

---

## 8. Trajectory as seen in the full texts

**Topics by five-year period.** Works are counted after merging duplicates. Ids in parentheses are full or partial cards.

| Period | Works | Topics |
|---|---|---|
| 1994–1999 | 8 | GO 5 (S070); GT 2; MIX 1 |
| 2000–2004 | 23 | GO 6 (S010, S015, S050, S098); MIX 4 (S011, S028, S213 programme); DST 3 (S002, S029); SUR 2 (D016); SW 2; APP 2; GEO 2 (S037); GT 1; CON 1 (S005) |
| 2005–2009 | 35 | GEO 8 (S040, S080, S103, S104, S108); DST 5 (S001, S006, S020, D001); GO 4 (S062); APP 3; GT 3 (S048, S076); MIX 3 (S031); SW 2 (S019); SUR 2; MOO 1; TUN 1 (S016); BEN 1 (S022†); CON 1 (S007); PAR 1 (S027) |
| 2010–2014 | 33 | APP 9 (S066, S074, S118, S204); GEO 6 (S093, S117, S146, S152); TUN 4 (S057, S059); MOO 3; SW 3 (S023); GT 2 (D002, S134); CON 1; DST 1; GO 1; SUR 1; PAR 1; NOI 1 (S039) |
| 2015–2019 | 31 | APP 10 (S032, S060, S069, S073, S166, S167); SUR 6 (S046, S068, S114, S116); GEO 3; CON 3 (S063, S064, S144); NOI 2; SW 2 (S034); DST 2 (S061, S124); MIX 1; TUN 1 (S095); PAR 1 (S125) |
| 2020–2024 | 28 | SW 6 (S013, S021); NOI 3 (S053, S084, S140); MOO 3 (S004, D003, S132); GEO 3 (S094, S113, S142); APP 3 (S107, S184, S186); CON 2 (S072, S090); PAR 2 (S143, S151); SUR 2 (S099, S133); BEN 1; FID 1 (S123); DST 1 (S138); MIX 1 (S058) |
| 2025–2026 | 26 | BEN 6 (D006, S071, S101/S128, S130, S156, S175); APP 4 (D007, S159, S160†, S174†); MIX 3 (S092, S121, S157); DST 3 (S120, S129, S137); SW 2; GEO 2 (S177); FID 2 (S112, S173); CON 2 (S158, S172); NOI 1 (S150); PAR 1 (S155) |

Topic codes:
- `GO`: exact global optimization (bilevel, bilinear, QCQP);
- `GT`: game-equilibrium enumeration;
- `GEO`: extremal geometry and other exact mathematics (side line);
- `DST`: direct-search convergence theory;
- `CON`: constraint handling;
- `SUR`: surrogates and models;
- `NOI`: noise, stochastic and robust optimization;
- `MIX`: mixed, categorical, granular and periodic variables;
- `MOO`: multiobjective optimization and indicators;
- `PAR`: parallelism, decomposition and structure;
- `TUN`: algorithm tuning;
- `FID`: multi-fidelity and evaluation cost;
- `BEN`: benchmarks and benchmarking methodology;
- `SW`: software, books, surveys, editorials, teaching;
- `APP`: applications with partners.

**Turns**
1. **Late 1998: from exact global optimization to pattern search.** The thesis links structured classes by proven reformulations [S070 pp. 33, 174]. Within a year of it, the Rice report probes Torczon's theorems [S025 TR pp. 1–3]. Exact QCQP and pooling work continues in parallel until 2004 [S010; S015; S098].
2. **2004–2009: finite directions give way to dense directions, and the filter gives way to the progressive barrier.** The GPS limitation is stated [D016 p. 4; S005 pp. 1–2]. MADS decouples mesh and poll [S001 p. 4], OrthoMADS removes the randomness [S006 p. 1], and PB replaces the filter mechanism while keeping dominance [S007 p. 3].
3. **About 2010: applications with partners and adoption of NOMAD.** Hydro-Québec [S204; S074], thermochemistry [S042; S036], genetics [S066], and algorithm tuning [S057; S059].
4. **2015–2022: consolidation.** Surrogate management by order error [S046; S068; S114], noise [S053; S084], hidden constraints and discontinuities [S072; S090; S138], measurement of multiobjective indicators [S004], and the NOMAD 4 rewrite [S021].
5. **2025–2026: benchmarks as outputs, and the mesh relaxed.**
   - Five benchmark or benchmarking works in two years: [S071; S130; S175; D006; S101/S128], plus bilevel benchmarking [S156].
   - The group that made the mesh central proposes mesh-free ADS [S129 p. 1; S172 p. 3].
   - Categorical [S121; S157], equalities [S158], multi-fidelity [S112; S173], covering and partition theory [S137; S155].

**What stayed constant**
- *The Clarke-calculus ladder* from 1998 to 2026 [S002 p. 12; S001 pp. 11–13; S007 pp. 24–25; S129 pp. 13–14; S172 pp. 14–15; S158 pp. 16–18].
- *Inheritance as the way new methods get theory* (Method 7), 2001–2026.
- *Constraint semantics*, from the closed/open split [S007 p. 2] to KARQ-style assignment [S173 p. 5].
- *The same testbeds reused for 17 years*: STYRENE was released in 2009 [S007 p. 31] and run again in 2026 [S172 p. 18].
- *A taste for exact or certified answers in the side line*: the 1997 thesis octagon [S070 pp. 166–171], 2002–2013 polygons [S037; S040; S117], 2022 certificates [S142; D003].

**What moved**
- The counterexample craft moved from GPS theory (1998–2009) to algorithm-design toys [S129; S172], measuring instruments [S004] and benchmark referees [S156].
- The currency moved from CPU time in the exact era [S015; S070] to evaluations [S001; S128], and then to explicitly weighted effort [S155; S156; D006].

---

## 9. Collaboration pattern

Distinct coauthors per period, over 184 Audet works after merging duplicates. Surnames are normalized from the card coauthor fields.

| Period | Works | Sole-authored | Distinct coauthors | Most frequent coauthors (works) |
|---|---|---|---|---|
| 1994–1999 | 8 | 0 | 4 | Jaumard 7, Savard 7, Hansen 6, Dennis 1 |
| 2000–2004 | 22 | 2 (S025, D013) | 25 | Dennis 9, Hansen 8, Jaumard 3, Savard 3, Abramson 2, Perron 2, Messine 2, Le Digabel 2 |
| 2005–2009 | 35 | 0 | 36 | Hansen 13, Dennis 9, Messine 8, Abramson 6, Le Digabel 6, Savard 5, Béchard 3, Belhaiza 3 |
| 2010–2014 | 33 | 5 (S023, S065, S146, S152, D014) | 44 | Le Digabel 11, Hansen 6, Dang 4, Orban 4, Dennis 3, Messine 3, Gheribi 3, Savard 2 |
| 2015–2019 | 31 | 3 (S095, S115, S203) | 39 | Le Digabel 12, Tribes 5, Côté 5, Alarie 4, Amaioua 3, Séguin 3, Kokkolaras 3, Peyrega 3 |
| 2020–2024 | 27 | 2 (S122, S190) | 32 | Le Digabel 9, Tribes 3, Kokkolaras 3, Alarie 3, Bouchet 3, Bigeon 3, Batailly 3, Kojtych 3 |
| 2025–2026 | 26 | 1 (S177) | 37 | Le Digabel 13, Tribes 9, Diouane 8, Diago 5, Lebeuf 5, Hallé-Hannan 4, Hare 3, Alarie 2 |

Counting rule for this table and the next paragraph: coauthor surnames from the card coauthor fields of the carded Audet works, duplicates merged. SKILL.md instead uses a rule reproducible from `works.json`: distinct non-talk entries after merging duplicates (including S101 = S128, D002 = S067, S019 = S202, S112 = S163, S145 ≈ S204), with S213 and D008 excluded (186 entries). That gives Le Digabel 54, Dennis 21 and Tribes 19.

Over all periods there are 157 distinct coauthors. The most frequent (card rule), with their first and last year, are: Le Digabel 54 (2004–2026), Hansen 36 (1997–2021), Dennis 22 (1999–2012), Tribes 20 (2009–2026), Messine 18 (2002–2025), Savard 17 (1994–2011), Alarie 12, Jaumard 10, Abramson 9, Diouane 9 (2025–2026), Kokkolaras 8 and Hare 7 (2017–2026).

**Observations**
- **Hubs change by era**:
  - the GERAD school (Hansen, Jaumard, Savard) until about 2011, with Hansen continuing in the geometry side line to 2021 [S094];
  - Rice (Dennis, Abramson) from 1999 to about 2012;
  - geometry (Messine, Perron, Ninin, Bingane) from 2002 to 2025;
  - the NOMAD core (Le Digabel from 2004, Tribes from 2009) throughout the DFO period;
  - Diouane as a new co-lead of the 2025–2026 algorithm papers [S121; S129; S156; S157; S158; S172].
- **Industrial coauthors are named co-researchers, not only funders**:
  - Hydro-Québec / IREQ: Alarie, Diago, Lebeuf [S123 p. 1; S112; S173 p. 1];
  - Rio Tinto: Côté [S032; S060];
  - thermochemistry: Gheribi [S042; S013].
  - The application survey is co-written with partners [S013 pp. 4–7].
- **Late papers are student-led**: Hallé-Hannan [S121 p. 1; S157], Brilli [S158 p. 1], Lebeuf [S173 p. 1], Bouchet [S151 p. 1; S155], Kojtych [S107; S184], Bingane [S113; S142], and the Couderc line [S140; S150].
- **Author order is mostly alphabetical**, so Audet's position is not a lead signal. Role statements ("first and corresponding author") and authorship counts (S022†, 7th of 15; S174†, 4th of 5) are used instead.
- **Sole-authored work is exposition, notes and puzzles**: surveys [S023; S122], the French textbook [S190], short notes [S065; S203; S115], puzzles [S152; S177], an application note [S095] and a talk abstract [S146]. The 1998 report [S025] is the only sole-authored theory work.
- **Cross-lens contacts**: Conn [S063; S079], Custódio [D001], Vicente as co-editor [D012], Hare on the textbook and the theory notes [S120; S124; S128].
- **Interdisciplinary partners reach the group through NOMAD**:
  - bioequivalence with FDA and industry statisticians [S069 p. 4];
  - genetics [S066];
  - metamaterials [S102];
  - hydrology [S073; S166; S167];
  - structural dynamics [S090; S107; S184];
  - origami [S160†];
  - cellular solids [S159].

---

## 10. Rejected updates

1. **Extremal geometry as a core method** (numeric first, certificate later). It is a side line, and it transfers to DFO only through certification tasks [D003; S186]. Keep it in the Trajectory and §7.1.
2. **Reference works as a research method** [S082; S102; S003; D004; S190; S122; D005]. These are abstract or metadata cards with no process evidence. The textbook's content remains unread (§11).
3. **Popular accounts, tributes and symposia** [S208; S207; S198; D011; S221; D010; S218]. Metadata only, and biography rather than method.
4. **Separate methods for cheap-first gating, the evaluation cache and the effort currency.** The exclusivity check fails or is weak, and the content already fits Methods 2, 5 and 6 plus N1 and N4 (§4.4).
5. **Surrogates as rankers, and neighbourhood knobs, as separate core methods.** Promoted by merging instead, because the cap is reached and the logic is Method 1's and Method 2's (§4.3).
6. **Promoting "rival-failure toy examples" separately.** Its content is Method 3's own (§4.3c).
7. **Using reading notes as findings.** Slips, table/text mismatches and loosely worded proof steps recorded on some cards are excluded by house rule.
8. **Evidence from collaborations Audet did not lead** as sole support for any method: S174†, S160†, S022†.
9. **Quoting S213 as Audet's voice.** The words are Abramson's [S213 p. 1].
10. **Mentor Voice changes.** No first-person teaching or feedback material appears in the full texts. The only personal note is Abramson's acknowledgment that Audet got mathematical details right [S213 p. 5], which is not Audet's own voice.
11. **Exact-era techniques as heuristics**: formulation-size accounting [S015 pp. 6–7], data-derived big-M [S048 pp. 5, 10–11], exact rational arithmetic [S076 pp. 9–10], minimax error equalization [S010; S070]. They do not transfer to blackbox optimization. They stay in §7 or the pool.
12. **Dropping cross-family comparison from Method 5.** Rejected: 16 full cards practice it (§2.2). Re-scope it instead (§3.1 #17).
13. **Replacing Method 4 or Method 5.** Rejected: both keep at least 26 full evidence cards over six periods (§2.1).

---

## 11. Open gaps

- **Unread key works (no open full text)**. Their SKILL.md claims still rest on abstracts:
  - the textbook, first and second editions [S003 metadata; D005 abstract], so the stated side of Method 5 ("Comparing Optimization Methods") and the accuracy-profile warning still come from a secondary quotation;
  - VNS search [S009], poll reduction to n+1 points [S038] (✗ first labelled "quadratic-model search"; its abstract describes a Poll-side reduction), mesh-based Nelder–Mead [S043], Robust-MADS [S055];
  - BiMADS and MultiMads [S018; S026], MV-MADS [S017], globalization strategies [S024], granular variables [S033], COCO [S141];
  - the AIAA 2000 surrogate paper [S008] and the NOMAD project record [S012].
- **The 2004 tightness article.** Only the 1998 report was read [S025], so "six counterexamples" is unverified.
- **Version dependence.** StoMADS test problems [S053 p. 21]; NOMAD 4 details [S021 p. 1]; the survey [S023 p. 1]; the multi-fidelity preprint vs the published paper [S163 vs S112]. The published versions may differ.
- **Early period.** 1994–1999 is read in full only through the thesis [S070]. Six of eight cards are abstract-level, so reformulation-era claims rest mainly on S070 and S050.
- **Tacit knowledge.** Still missing: no interviews, lectures or student recollections. Acknowledgments add little [S213 p. 5]. How topics are chosen and how counterexamples are found remains undistillable.
- **Supervision.** Audet's own advisors are resolved [S070 p. 3], and so is one co-supervision [S213 p. 1]. Other supervision roles are still inferred from coauthorship and scholarship notes [S121 p. 1; S173 p. 24; S092 p. 1].
- **Skipped items.** 19 skipped works: talks such as "Industrial Strength Derivative-Free Optimization", conference duplicates and junk rows (see `../sources/papers/INDEX.md`). They are unlikely to change the methods but were not checked.
- **NOMAD 4 documentation.** Two SKILL.md quotes come from it and are not covered by any card (§3.1 #9).
- **Complexity results.** S140 was read only in part: its bias lemmas and several proofs were not read [S140 card]. The complexity statement in §3.1 #3 rests on theorem statements.
