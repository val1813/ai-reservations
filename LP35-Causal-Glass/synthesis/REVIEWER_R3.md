# Nature Physics Referee Report — LP35-Causal-Glass

**Manuscript under review:** C1-C6 conclusions from LP35-Causal-Glass (Phase 0, three rounds of AB adversarial exploration)
**Reviewer stance:** Fundamental skepticism — treating all claims as unproven until independently verified
**Date:** 2026-06-08

---

## OVERALL RECOMMENDATION: REJECT

**Reason:** The manuscript exhibits fatal prior-art conflicts with published work (She 2007, JCAP), relies on uncalibrated parameters throughout all quantitative claims, presents postdictions as predictions, and the core mechanism reduces to a Friedmann-equation tautology. The conceptual core (causal structure freezing at horizons, glass transition in cosmology) was published 19 years ago. No quantitative discriminating prediction survives independent scrutiny.

---

## GATE 1: CITATION FABRICATION (引用虚构)

### Finding 1.1: Achlioptas et al. 2009, Science 323, 1453 — mis-cited

A-R3 §4.4 invokes "Achlioptas et al. 2009, Science 323, 1453" to support the claim that directed-graph search time scales as τ_explore ~ τ_0 × N_reachable^{1/d_eff}. The actual Achlioptas et al. (2009) paper in Science 323, page 1453, is titled "Explosive Percolation in Random Networks" — it concerns a specific percolation transition under an edge-selection rule (the "product rule") and does NOT derive or discuss search time scaling on directed acyclic graphs. This is a fabricated citation. The scaling relation asserted has no identifiable source in the peer-reviewed literature.

### Finding 1.2: Adam-Gibbs "falsification" presented as established fact

C2 states that "AG thermal activation (Adam-Gibbs) all variants falsified: N_coop cancels exactly in the exponent." This is presented as if it is a known result. In reality:
- The AG relation has been extensively studied, modified, and empirically tested over 60 years (Ngai et al., J. Chem. Phys. 1991; Ngai, J. Phys. Chem. B 1999; Starr et al., J. Chem. Phys. 2013; MRS Bulletin 2025 review).
- The specific calculation that N_coop cancels in the exponent is an **original derivation by the authors** (A-R3 §4.3), not a published result. It depends on the specific assumption that A = k_B T_eff × N_coop × ln 2, which is not generally true for AG modifications where A scales differently with N_coop (Ngai 1999).
- Presenting this as "AG falsified" without citing any experimental or computational study that supports this cancellation is misleading. The authors have derived a *consequence of their own assumption about A*, not falsified an established theory.

### Finding 1.3: Uncited causal set theory literature

C2 claims that "causal edges in GR can only be added, not deleted (spacelike→timelike, 0→1 only)" as a new discovery. This is standard material in causal set theory (Rideout & Sorkin, "Classical Sequential Growth Dynamics for Causal Sets," Phys. Rev. D 61, 024002, 2000; the entire causal set program since Bombelli, Lee, Meyer & Sorkin 1987). The manuscript presents this as an original logical deduction from GR when it has been known for decades in the quantum gravity literature. No causal set paper is cited.

---

## GATE 2: PRIOR ART CONFLICT (先发冲突)

### Finding 2.1: She (2007) — JCAP 02, 021 — FATAL PRIOR ART

**Jian-Huang She, "An Accelerating Universe Emergent from the Landscape," JCAP02(2007)021, arXiv:hep-th/0702006.**

This paper already proposed — 19 years ago — the following core elements claimed as novel by LP35:

| LP35 Claim | She (2007) Precedent |
|------------|---------------------|
| C1: C[G] landscape non-ergodicity in expanding universe | "The universe exists in a quantum glass state" with "extremely large effective viscosity slowing long-distance dynamics" |
| C2: Freezing at cosmic horizon | "Glass transition point = location of cosmic horizon where viscosity diverges" |
| C3: Λ emerges from glassy dynamics | "Cosmological constant problem solved: Λ ~ 10^{-120} is not fine-tuning but extreme slowing" |
| Freezing = structural, not thermal | "Dynamical arrest" at horizon, "separation of time scales" for short vs long distance dynamics |
| Landscape + expansion → freezing | "Landscape suggests quantum glass → slowing → explanation for slow-roll and dark energy" |

She (2007) has only 1 paper on Semantic Scholar and has been largely uncited — it is obscure but definitively published in a peer-reviewed journal (JCAP, IOP). The LP35 manuscript neither cites nor distinguishes itself from She (2007). Under *Nature Physics* editorial policy, failure to cite and differentiate from pre-existing published work constitutes grounds for outright rejection.

The authors might argue that She (2007) used the string landscape while LP35 uses causal graphs — but She (2007)'s core mechanism (landscape → glass → horizon freezing → Λ) is structurally identical to LP35's C1→C2→C3 chain. The shift from "string landscape" to "causal graph landscape" is a change of substrate, not a new theory.

### Finding 2.2: "Freezing" dark energy models — Jassal (2012), PRD 86, 043528

The C5 predictions reference "freezing" behavior in w(z) as if this terminology and classification are original. Jassal (2012) already classified scalar field dark energy into "freezing" and "thawing" models, with freezing models characterized by w(z) asymptotically approaching -1 — the exact behavior LP35 claims to predict. The LP35 terminology ("freezing" = dynamical arrest, "quench" vs "cooling") overlaps with established cosmology vocabulary in a way that creates confusion rather than clarity.

### Finding 2.3: Λ ~ H₀² M_Pl² is the Friedmann equation tautology

C6 acknowledges "no quantitative discriminating predictions." What C6 does NOT acknowledge is that the central quantitative claim — that the theory "predicts" Λ in the right ballpark — is a tautology. The Friedmann equation for a flat universe is H² = (8πG/3)ρ_total. Expressing this in Planck units gives Λ ~ H₀² M_Pl² automatically for ANY theory that produces a stress-energy tensor comparable to the critical density. This is not a prediction of the causal glass framework — it is dimensional analysis enforced by the Friedmann equation. The real coincidence problem ("why now?") is temporal, not numerical, and the manuscript does not address it.

### Finding 2.4: DESI DR2 w(z) evolution is a measurement, not a prediction

C5/P2 claims to "predict" a w(z) inflection near z_accel ~ 0.8. DESI DR2 (March 2025) already measured w(z) evolution and found phantom crossing at z ~ 0.5 (2.8σ-4.2σ significance depending on dataset combination). The manuscript's "prediction" is a postdiction of a measurement that already exists. Furthermore:
- The redshift of the claimed inflection is "z ~ 0.8 ± 0.3" — a range so wide (z=0.5 to z=1.1) it covers essentially any plausible acceleration redshift and any DESI measurement.
- The CPL parameterization w(z) = w₀ + w_a × z/(1+z) already produces an inflection-like feature for any w_a ≠ 0, with no causal glass required.
- Dinda & Maartens (2025 MNRAS) argue the phantom crossing may be a parameterization artifact — the very feature LP35 claims to predict may not survive.

---

## GATE 3: LOGICAL BREAKS (逻辑断裂)

### Finding 3.1: s(q) concavity → boundary optimum → dynamic constraints prevent reaching it (C1)

The chain is:
1. s(q) is strictly concave → C[G] minimum at boundaries (q→0 or q→1)
2. Observable universe NOT at boundary
3. Therefore "dynamic constraints prevent reaching global optimum" → non-ergodicity

Steps 1 and 2 are logically connected — but step 3 is an **assertion, not a derivation**. What are the "dynamic constraints"? Why do they prevent boundary-reaching? The manuscript never specifies them — it invokes them as a deus ex machina. A universe with finite age might simply not have had enough time to reach the boundary optimum, in which case the "non-ergodicity" is trivial (finite time = finite exploration). Alternatively, the "dynamic constraints" might be the directedness of edge addition — but that is a separate argument (§1.1) that was introduced AFTER the s(q) concavity argument, not derived from it.

The s(q) concavity argument and the edge-directedness argument are two independent claims bolted together without logical connection. The concavity argument alone does NOT establish non-ergodicity — it establishes that the global optimum is at the boundary, which is a different statement from claiming it cannot be reached.

### Finding 3.2: Quench判据 Φ_q is parameter-fitting, not derivation

The core of C2 is that freezing is quench (γ_explore < γ_expand), not cooling. The quench criterion Φ_q = τ_explore/τ_expand > 1 requires:

**τ_explore ~ τ₀ × exp(c × K_eff)**

- τ₀ ~ 10^{-44} s (Planck time) — reasonable
- c = search efficiency factor — ANY value between 2 and 20+ is claimed as "reasonable"
- K_eff ~ 5-15 (B博士 TCD estimate)

**τ_expand ~ t_H × 10^{122}** (claim in A-R3 §4.4) or **τ_expand ~ 1/Γ_expand ~ t_H** (claim in B-R3 §2.3)

These two estimates differ by **122 orders of magnitude.** The INSPECTOR identified that the A-R3 derivation has dimensional problems and that the B-R3 derivation uses undefined causal patch scale l_c. The most fundamental quantity in the theory — whether the universe actually satisfies the quench condition — cannot be computed from the theory itself.

The quench criterion can be satisfied by CHOOSING c ~ 20 (making τ_explore large enough) OR by choosing a small τ_expand definition. This is not a physical prediction — it is parameter selection to fit a pre-determined conclusion.

### Finding 3.3: C3 "Λ = causal freezing residual stress" — missing conversion chain

C3 claims that frozen C[G] stress → effective vacuum energy → Λ. The conversion requires:
1. C[G] configurational stress Σ = ½Δq^T H Δq (in nats)
2. nats → energy via Landauer principle: k_B T_GH per nat
3. Energy density → Friedmann equation contribution

Each step introduces an uncalibrated conversion factor:
- Step 1: H (Hessian of C[G]) is never computed for any realistic causal graph
- Step 2: Uses T_GH = ℏH/(2πk_B) — but H itself depends on ρ_conf via Friedmann equation, creating a self-consistency loop that is never solved
- Step 3: The conversion from energy density to observable Λ requires a "κ" parameter

A-R3 §3.4 honestly admits: "Δq表达式的量纲闭合需要引入l_Pl²因子 → 等价于调用全息原理." This means the theory CANNOT make a physical prediction for Λ without invoking the holographic principle — a framework that (a) is not established for de Sitter space, and (b) is an entirely separate theoretical apparatus that the causal glass framework does not derive.

### Finding 3.4: C4 suboptimal trap — toy model with arbitrary parameters

The N=4 path graph suboptimal trap "proof" uses:
- Arbitrary I(i:j) matrix values (3.0, 0.5, 0.2, 0.1)
- Arbitrary τ(i:j) matrix (1.0, 3.0, 10.0)
- Arbitrary α=0.3, β=2.5
- The condition β > 2.223 is derived FROM these arbitrary choices

None of these parameters are derived from cosmology. Changing any I or τ value changes the β threshold. The existence of a suboptimal trap is proven for THIS specific toy model with THESE specific parameters, but no argument connects these parameters to the actual universe's causal graph. This is an existence proof in an abstract mathematical space with no demonstrated relevance to physical cosmology.

Furthermore, INSPECTOR_B_R3 identified that the N_trans accounting in §1.6 contains arithmetic errors (C for +ac+ad should be -1.887, not +0.633). This error is minor for the qualitative claim but emblematic of the framework's distance from quantitative reliability.

### Finding 3.5: AB diverge on the question that matters most

C3 and C6 acknowledge that A and B disagree on the causal arrow:
- A博士: Initial freezing → dark energy (trigger), then DE → deeper freezing (amplifier) — **bidirectional, freezing predates DE**
- B博士: DE → freezing only — **unidirectional, freezing postdates DE**

This is not a semantic disagreement. It produces opposite observational predictions (see GATE 4). A theory that simultaneously claims "freezing happened before dark energy" and "freezing happened after dark energy" — depending on which author you ask — has not converged on a single physical model. The PI synthesis (PI_synthesis_R3.md) correctly notes that "AB两个R3在因果箭头方向和冻结时间上未汇聚."

---

## GATE 4: MAGNITUDE PARADOX (量级悖论)

### Finding 4.1: τ_expand estimates span 122 orders of magnitude

| Source | τ_expand estimate | Context |
|--------|-------------------|---------|
| A-R3 §4.4 | t_H × 10^{122} ≈ 10^{139} s | From N_edges = A_horizon/l_Pl² |
| B-R3 §2.3 | ~ 1/H ~ t_H ≈ 10^{17} s | From Γ_expand ~ dN_pairs/dt |
| Ratio | **10^{122}** | **Catastrophic disagreement** |

These two estimates come from two different definitions of what "causal edges" are. A博士 treats every Planck area on the horizon as an independent edge endpoint. B博士 treats "causal patches" of undefined scale l_c as the fundamental units. Neither definition is derived from the theory — they are independent assumptions about the ontology of the causal graph. A theory whose central dynamical timescale has 122 orders of magnitude uncertainty is not a quantitative physical theory.

### Finding 4.2: c parameter elasticity enables any conclusion

The quench factor c determines whether τ_explore > τ_expand:
- c ~ 2: τ_explore tiny → universe is NOT frozen → theory is false
- c ~ 20: τ_explore large → universe IS frozen → theory is true

Both c=2 and c=20 are claimed as "physical" by A-R3, with no method to determine which is correct. This means the theory currently has **zero empirical constraint on its central prediction.** The quench criterion Φ_q > 1 can be made true or false by choosing c within a factor of 10 — a range the authors themselves consider reasonable.

### Finding 4.3: Λ estimate misses by 32 orders of magnitude

B-R3 §5.1 attempts to compute ρ_Λ from causal graph properties:
- Simple counting: ρ_Λ ~ 10^{-15} GeV⁴
- Observed: ρ_Λ ~ 10^{-47} GeV⁴
- **Mismatch: 32 orders of magnitude**

The "fix" introduces a "fractal dimension A ~ 10^{40}" — a parameter invented to absorb the 32-order discrepancy, with no independent derivation, no physical motivation beyond making the numbers work, and no way to measure it independently of Λ itself. B博士 honestly admits: "这不是对Λ的解释，而是将Λ的值转化为对因果图分形结构的约束" — i.e., this is not an explanation of Λ, it merely translates the problem into an equally mysterious parameter.

### Finding 4.4: "Prediction" of w(z) inflection — threshold too wide to fail

C5/P2 "predicts" w(z) inflection at z_accel ~ 0.8 with an uncertainty of ±0.3. This range (z=0.5 to z=1.1) covers:
- The observed acceleration redshift (~0.6-0.8)
- DESI DR2 phantom crossing (~0.5)
- The matter-Λ equality epoch (~0.3-0.7)
- Essentially any plausible transition redshift in ΛCDM

A "prediction" that cannot be falsified by any plausible measurement is not a prediction — it's a restatement of ignorance. The authors acknowledge this in C6 ("均缺乏定量证伪阈值") but continue to present these as "discriminating predictions."

### Finding 4.5: The 10^{30096} → 2.7×10^{-44}s → quench trajectory

R1 predicted τ_α ~ 10^{30096} s (absolute freeze), then R2-R3 discovered this was based on a category error (total BH entropy vs per-CRR entropy), corrected to τ_α ~ 2.7×10^{-44} s (no freeze under AG), then switched to quench mechanism (freeze by expansion, not thermal activation). The predicted relaxation time has swung by **10^{30140} orders of magnitude** across three rounds. A theory whose central numerical prediction is unstable by a factor that vastly exceeds the number of particles in the observable universe is not a predictive physical theory.

---

## GATE 5: FATAL ALTERNATIVE EXPLANATION (致命替代解释)

### The simplest alternative that covers ALL claims

**ΛCDM + standard causal set theory + known glass physics metaphors**

1. **C1 (C[G] non-ergodicity):** Causal set theory (Rideout & Sorkin 2000) already describes spacetime as a growing directed acyclic graph where edges are added sequentially. The non-ergodicity of this growth process is well-known — the set of all causets that can be reached from a given initial causet by sequential growth is a subset of all causets. No new principle is needed.

2. **C2 (Freezing = quench):** She (2007) already argued that cosmic expansion creates a glass transition at the horizon. The "cooling vs quench" distinction is a reclassification of mechanisms within an already-established analogy. The specific claim that AG is "falsified" is an original calculation, not an independent verification, and depends on a specific assumption about activation energy scaling.

3. **C3 (Λ = residual stress):** The Friedmann equation gives Λ ~ H₀²M_Pl² for any theory where dark energy is comparable to the critical density. This is dimensional analysis, not a theory-specific prediction. The manuscript's "κ ~ M_Pl²H₀²" is the Friedmann equation written in different notation.

4. **C4 (Suboptimal trap):** A mathematical existence proof on N=4 graphs with arbitrarily chosen parameters. The actual universe has ~10^{80} particles. There is no reason to believe this toy model captures any feature of cosmological dynamics.

5. **C5 (Discriminating predictions):** Every "prediction" is either (a) already measured by DESI (w(z) evolution), (b) already predicted by ΛCDM (late ISW), or (c) unfalsifiable due to parameter elasticity (z~0.8±0.3 freeze texture).

6. **C6 (Structural limitations):** The authors' own honesty in listing these limitations is commendable but self-defeating. When a theory acknowledges it has "no quantitative discriminating predictions," "structural barriers" to its main mathematical mapping, and an "uncalibrated" central criterion, it has not met the burden of proof for publication as a physics theory.

### How would ΛCDM + existing glass metaphors produce the same "predictions"?

- **w(z) evolution:** DESI already measures it. ΛCDM+quintessence fits it. No causal glass needed.
- **Late ISW:** Standard ΛCDM predicts it. Planck has measured it. No causal glass needed.
- **Λ ~ H₀²M_Pl²:** Friedmann equation. No causal glass needed.
- **"Freezing" at horizon:** She 2007. No causal glass needed.
- **Causal structure as DAG:** Causal set theory (1987-present). No causal glass needed.

The LP35 framework adds one genuinely novel element: the specific C[G] cost function (C[G] = -Σs(q_i) + ΣI(i:j) + τ|E| + β·N_trans). But (a) the function has uncalibrated parameters (s(q) functional form, α, β, I matrix, τ matrix), (b) the function has never been fit to or tested against any cosmological data, and (c) the function's supposed prediction (Λ ~ 10^{-47} GeV⁴) misses by 32 orders of magnitude without a fractal-dimension fudge factor. A cost function with this many free parameters and this poor predictive performance is not a theory — it's a framework for curve-fitting that hasn't even begun to fit curves.

---

## SUMMARY OF FINDINGS

| Gate | Finding | Severity |
|------|---------|----------|
| **G1: Citation fabrication** | Achlioptas et al. (2009) mis-cited; AG "falsification" presented as established; causal set literature uncited | ⛔ Reject |
| **G2: Prior art** | She (2007) JCAP published core mechanism 19 years ago; Λ~H₀²M_Pl² is Friedmann tautology; DESI w(z) is a measurement not prediction | ⛔ Reject |
| **G3: Logical breaks** | s(q) concavity→non-ergodicity is asserted not derived; quench criterion is parameter-fitting; Λ = frozen stress has no quantitative conversion chain; AB diverge on causal arrow | ⛔ Reject |
| **G4: Magnitude paradox** | τ_expand estimates span 122 orders; c factor elastic by 10x; Λ estimate off by 32 orders; prediction swung by 10^{30140} across rounds | ⛔ Reject |
| **G5: Fatal alternative** | ΛCDM + causal set theory + She (2007) cover all claims with fewer assumptions and better quantitative precision | ⛔ Reject |

---

## DECISION

**RECOMMENDATION: REJECT**

No path to Major Revision exists because the core claim is pre-empted by prior art (She 2007, JCAP), the quantitative framework cannot make a single prediction without uncalibrated parameters, and the framework's predictions have been unstable across three internal rounds by factors exceeding 10^{30000}.

### What would change this recommendation

1. **Demonstrate that She (2007) does not pre-empt the work** — by showing a specific, quantitative difference between the "string landscape → quantum glass" mechanism and the "causal graph → quench freeze" mechanism that produces different observable predictions. The current manuscript does not even cite She (2007), much less differentiate from it.

2. **Produce ONE quantitative prediction with a specified falsification threshold** — not "w(z) has an inflection somewhere near z~0.8" but "the causal glass theory predicts w(z=0.5) = -0.93 ± 0.01, which differs from ΛCDM's w = -1 at >5σ given DESI DR2 precision." The current manuscript has no such prediction and acknowledges (C6) that it cannot produce one.

3. **Calibrate the quench criterion from first principles** — derive c, K_eff, and τ_expand from the causal graph structure of the ΛCDM universe without free parameters. The current elasticity (c can be anywhere from 2 to 20) means the theory can accommodate any observation.

4. **Close the 32-order magnitude gap** — derive Λ ~ 10^{-47} GeV⁴ without invoking a fractal dimension A ~ 10^{40} that is itself fit to match Λ. The current "derivation" is Λ → A → Λ, i.e., circular.

5. **Resolve the AB causal arrow divergence** — a theory whose two independent exploration paths produce opposite predictions (freezing at z>1 vs freezing at z<0.8) is not a single theory. The authors must either demonstrate that one path is correct and the other wrong, or show that both are limits of a unified framework that makes a definite (not ambiguous) prediction.

Unless the authors can address all five points with substantive new work (not minor revisions), the manuscript does not meet *Nature Physics* standards for publication.

---

*Reviewer 3, Nature Physics*
*Confidential — not for distribution to authors in identifiable form*
