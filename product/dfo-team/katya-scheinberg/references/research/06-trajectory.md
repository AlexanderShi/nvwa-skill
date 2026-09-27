# 06 · Research trajectory

> Research date: 2026-09-27. Biographical facts come from institutional bios and Wikipedia as shown in search snippets (secondary unless noted). Exact start/end years not shown in any snippet are marked "≈" or ⚠️.

## 1. Timeline

| Period | Position / event | Research focus (verified works) | Pivot trigger (evidence / inference) | Source |
|---|---|---|---|---|
| to 1992 | Undergraduate degree in operations research, Lomonosov Moscow State University (born in Moscow) | — | — | https://en.wikipedia.org/wiki/Katya_Scheinberg (secondary) |
| 1992–1997 | PhD in operations research, Columbia University (1997). Advisor D. Goldfarb (verified via Wikipedia, 2026-09-27) | DFO begins: Conn–Scheinberg–Toint, Math. Program. 1997 | *Inference*: collaboration with Conn (IBM) during/after PhD | Wikipedia; IDFO blurb (PhD 1997, Columbia; via search summary) |
| ≈1997–≈2010 | Research staff member, IBM T. J. Watson Research Center ("for over a decade") | Model-based DFO (1997; CSV 2008; book 2009; Scheinberg–Toint 2010; Zhang–Conn–Scheinberg 2010), open-source DFO code; ML optimization (Fine–Scheinberg JMLR 2001; Scheinberg–Ma–Goldfarb NIPS 2010) | Industrial lab: applied black-box problems + ML problems side by side | Wikipedia; IDFO blurb (primary co-authored text) |
| 2009 | *Introduction to Derivative-Free Optimization* (SIAM, with Conn and Vicente) | Consolidates Arc 1 | — | http://www.mat.uc.pt/~lnv/idfo/ |
| ≈2010s–2019 | Harvey E. Wagner Endowed Chair Professor, Industrial and Systems Engineering, Lehigh University (start year ⚠️) | **Pivot to probabilistic models**: BSV 2014; STORM 2018; Cartis–Scheinberg 2018; Blanchet et al. 2019; Paquette–Scheinberg 2020; SIAM News essay (Mar 2019, bio lists Lehigh chair) | *Inference*: randomized sampling in DFO + stochastic ML objectives made deterministic model certification the bottleneck | Wikipedia; SIAM News bio (https://www.siam.org/publications/siam-news/articles/knowing-what-to-know-in-stochastic-optimization/) |
| 2015 | Lagrange Prize in Continuous Optimization (MOS–SIAM), with Conn and Vicente, for the IDFO book | Recognition of Arc 1 | — | Wikipedia / KAUST bio (secondary) |
| 2019–2024 | Professor, School of Operations Research and Information Engineering, Cornell University | Gradient-estimator comparison with ML (FoCM 2022); high-probability bounds (Jin–Scheinberg–Xie, arXiv 2021 → SIOPT 2024; Cao–Berahas–Scheinberg, arXiv 2022 → Math. Program. 2024) | *Inference*: move from expected to tail bounds reflects ML-style "single run" guarantees | https://www.orie.cornell.edu/spotlights/welcome-katya-scheinberg (existence; content unread) |
| July 2024– | Coca-Cola Foundation Chair and Professor, H. Milton Stewart School of ISyE, Georgia Tech | Return to Powell-style model-based DFO with complexity (arXiv 2025, 2026); unreliable/heavy-tailed oracles (arXiv 2025) | *Inference*: Arc 2 tools now strong enough to analyse Arc 1 algorithms | https://www.isye.gatech.edu/users/katya-scheinberg (secondary) |
| July 2025– | Chair, Mathematical Optimization Society; co-editor, Mathematical Programming | Service | — | Georgia Tech / KAUST bios (secondary) |
| undated | INFORMS Fellow; SIAM Fellow; Farkas Prize (INFORMS Optimization Society; year ⚠️); past EiC Mathematics of Operations Research; past chair SIAG/OPT; EiC SIAM-MOS book series; editor of Optima | — | — | https://obd.kaust.edu.sa/speakers/detail/katya-scheinberg (secondary) |

## 2. Pivots and their triggers (summary)

1. **Deterministic → probabilistic models (≈2013–2014).** Evidence: BSV 2014 (arXiv:1304.2808) keeps the Arc 1 trust-region machinery and changes only the model-accuracy assumption. Trigger: *inference* (random sampling/sparse recovery ideas; stochastic ML objectives).
2. **Convergence → complexity → high-probability complexity (2015–2024).** Evidence: arXiv:1505.06070 (2015) → arXiv:1609.07428 (2016) → arXiv:2106.06454 (2021) → arXiv:2205.03667 (2022).
3. **Stochastic oracles → unreliable/heavy-tailed oracles (2025).** Evidence: arXiv:2511.19411.
4. **Return to Powell (2025–2026).** Evidence: arXiv:2510.14935; arXiv:2609.09441.

Entry timing: Scheinberg entered model-based DFO early (1997, before the field had a textbook) and entered stochastic adaptive methods (2014) before high-probability analysis of adaptive methods became standard (*inference*: most third-party titles on the topic found in searches date from 2021 onward).

## 3. Latest 12 months (Sept 2025 – Sept 2026)

- **arXiv:2510.14935** (Oct 2025) — "On Complexity of Model-Based Derivative-Free Methods", Chaudhry & Scheinberg. One search summary describes it as an ICM 2026 proceedings contribution ⚠️ (not independently confirmed).
- **arXiv:2511.19411** (Nov 2025) — "Stochastic Adaptive Optimization with Unreliable Inputs: A Unified Framework for High-Probability Complexity Analysis", Scheinberg + one co-author (name ⚠️).
- **arXiv:2609.09441** (submitted 2026-09-08) — "Powell-Style Model-Based Derivative-Free Optimization with Complexity Guarantees", Chaudhry, Scheinberg & Sun.
- Service: MOS Chair and Math. Programming co-editor since July 2025 (just outside the 12-month window, ongoing).
- Leads not attributable (authors unverified ⚠️): "Robust Accelerated Adaptive Search: High-Probability Complexity Bounds under Bounded-Moment Stochastic Oracles" (arXiv:2604.15526, Apr 2026) — same problem family, may or may not involve Scheinberg.

## 4. Not covered

- Exact years for Lehigh start and IBM departure; Farkas Prize year; PhD advisor; full list of recent talks.
