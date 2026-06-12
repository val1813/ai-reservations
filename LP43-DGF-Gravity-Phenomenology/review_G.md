# Referee Report G: Final Nature Audit of DGF Gravity

**Referee expertise:** Theoretical physics — foundations of general relativity, equivalence principle, information theory, and scientific methodology
**Manuscript under review:** DGF Gravity Final Version — Claim of "no free parameters," single hypothesis dτ = q·dt, derivation of GR with 2PN corrections
**Key files examined:** `DGF_CLOSURE.md`, `DGF_FINAL_COMPLETE.py`, `knowledge_graph.json`, `first_principles.py`, `THE_TRUTH.md`, `parameterization.md`, `FINAL_SYNTHESIS.md`, `literature_audit.md`, all prior reviews A-F

---

## Summary Verdict: REJECT — With Prejudice

After six rounds of malicious review, the DGF theory has been reduced to its minimum viable core: the assertion that dτ = q·dt, combined with Weyl-integrable geometry, yields a metric ds² = -q²dt² + q^{-2}dx² with q = exp(-GM/rc²). The authors claim this is a "parameter-free" theory that "derives GR" while making falsifiable predictions at 2PN.

I evaluate DGF against four specific attacks and identify one fatal internal contradiction that has survived all six review rounds. **The conclusion is that DGF is not a scientific theory — it is a mathematically dressed reparameterization of GR with no independent empirical content at the foundational level.** The "single hypothesis" is not falsifiable, and the authors' own first-principles simulation code contradicts the theory's central claim.

---

## ATTACK 1: The "No Free Parameters" Claim Is Circular

### The Circularity

The authors state: "Alpha=1 is UNIQUELY fixed by the Newtonian limit (alpha != 1 gives wrong g_00)."

Let me trace this logic:

1. The causal graph gives dp ~ q^t (weighted path count).
2. This implies dτ/dt = q^α for any real α (the authors' own analysis in `g00_derivation.md` identifies three cases: α = 1, -1/2, 1/2).
3. For α = 1: dτ/dt = q, so g_00 = -q² ≈ -(1 - 2GM/rc²).
4. This matches the Newtonian gravitational potential Φ = -GM/r.
5. Therefore α = 1 is "uniquely fixed."

**Step 4 is the circular step.** The Newtonian potential Φ = -GM/r is GR's weak-field limit. It is not a graph-theoretic fact. The causal graph contains no masses, no G, no r — only nodes, edges, and q-weights. The statement that "the Newtonian limit requires g_00 ≈ -(1 - 2GM/rc²)" imports GR's Newtonian limit into DGF. DGF then uses this imported fact to calibrate α, and then claims to have "derived" the Newtonian limit.

**The correct logical chain is:**
```
Want GR's Newtonian limit → demand g_00 ≈ -(1-2GM/rc²) → solve for α → α = 1 → "derive" GR
```
This is not derivation. It is calibration. α is a free parameter whose value is selected to reproduce the known answer.

### What Would Non-Circular Fixing Require?

To fix α without circularity, the authors would need to derive it from properties of the causal graph alone — e.g., from the fanout structure, the continuum limit of path counting, or the dynamics of q. The code in `first_principles.py` computes dp and notes that dp^(1/t) converges to q (line 261), but the identification of dp^(1/t) with dτ/dt is itself an assertion, not a derivation. The code simply declares this equivalence without argument.

**The "no free parameters" claim is false.** There is one parameter (α) whose value is externally imposed by demanding consistency with GR. This is the definition of a theory with a calibrated parameter.

---

## ATTACK 2: The Cosmological Emptiness of DGF

### The Claim vs. Reality

The DGF code and documentation claim that DGF predicts w_eff(z) with a phantom crossing at z ~ 1-2 (peak star formation). The cosmic q_bg varies by ~10^{-5} over cosmic history.

### The Problem

A theory that claims to derive gravity from "information propagation on causal graphs" — a revolutionary conceptual leap — produces a universe that is **observationally indistinguishable from ΛCDM on the largest scales.** The cosmological predictions are:

- w_eff ≈ -1.0000 today
- q_bg variations ~10^{-5}
- No new cosmological observables
- No explanation for dark energy (Λ remains an "independent parameter" — line 145 of `DGF_FINAL_COMPLETE.py`)

This is methodologically suspicious. When a theory claims to replace the fundamental ontology of spacetime but produces the same predictions as the established theory, one must ask: is the new ontology doing any scientific work?

### The Argument from Scales

DGF has a built-in escape hatch: the screening mechanism (`q ≈ 1` in weak fields, deviations only at strong fields). But screening mechanisms exist in standard scalar-tensor theories (chameleon, symmetron, Vainshtein) — DGF's version adds nothing new. And the screening is so effective that:

- **Solar System:** DGF = GR (PPN γ=1, β=1)
- **Binary pulsars:** DGF ≈ GR to measurement precision
- **Cosmology:** DGF ≈ ΛCDM
- **EHT black hole shadows:** DGF ≈ GR (authors' own admission, `STATUS_2026-06-10.md`)

**The only claimed observable deviation is at 2PN in GWs.** Everything else is hidden. A theory with one observable difference from GR, in one regime (strong-field GW), that is just at the edge of current detectability, is a theory engineered to be unfalsifiable.

### Comparison with Other Theories

Contrast with:
- **Brans-Dicke:** One parameter ω_BD, constrained by Cassini to ω_BD > 40,000, limiting but not killing the theory.
- **f(R) gravity:** Observable in galaxy clusters, cosmological structure formation, and solar system (chameleon).
- **Einstein-aether:** Four parameters, each constrained independently by multiple observables.

DGF has zero independently constrained parameters and one regime where it might (eventually, with third-generation detectors) be distinguishable from GR. This is not the profile of a falsifiable scientific theory.

---

## ATTACK 3: dτ = q·dt Has No Independent Empirical Content

### The Operability Problem

The authors' central postulate is dτ = q·dt — "proper time of information propagation is proportional to quantum channel openness." I ask: **describe any experiment, even a gedankenexperiment, that can verify or falsify dτ = q·dt without using gravitational phenomena whose description already presupposes GR.**

The only way to "measure" whether dτ = q·dt is correct is to compute gravitational predictions and compare them with GR. This makes the hypothesis equivalent to "GR is correct" — not because the hypothesis implies GR from first principles, but because the hypothesis is calibrated to reproduce GR and tested against GR's predictions.

### The Logical Structure

```
Claim: dτ = q·dt
Test: Does this produce the correct gravitational predictions?
If yes: dτ = q·dt is confirmed.
If no: adjust parameters until it does (this is what happened — see attack 1).
```

This is curve-fitting, not theory testing. A genuine hypothesis would make predictions in a domain where GR is silent or ambiguous, and those predictions could be tested independently. dτ = q·dt makes no such predictions. Every "prediction" of DGF is a gravitational prediction, and every gravitational prediction is tested against GR.

### The Authors' Own Admission

In `THE_TRUTH.md`, the authors acknowledge: "dτ = q·dt is a physical interpretation, not a graph-theoretic derivation." And in `RESPONSE_TO_REVIEW.md`: "DGF is GR's microscopic foundation (statistical mechanics ←→ thermodynamics), not a replacement for GR."

If DGF is merely a reinterpretation of GR — a "microscopic foundation" — then it does not belong in a physics journal as a new theory of gravity. It belongs in a foundations or philosophy of physics journal, with the clear disclaimer that it reproduces GR identically and offers no new testable predictions at the foundational level.

### The Only Potentially Distinct Prediction

The authors claim 2PN GW phase deviations distinguish DGF from GR. But:
1. The 2PN coefficient is extracted by numerical fitting from a binding energy formula whose correct form is disputed (see review E's fatal Ω² error).
2. The binding energy formula uses standard GR geodesics, contradicting the claim that DGF particles follow "information-prioritized paths" (a concept that has no equation of motion — see review F, Attack 4).
3. Even at face value, the deviation (~4%) is small enough to be degenerate with spin parameters (review E, Section 5).

**There is no clean, unambiguous prediction.** Every attempt to extract one collapses under scrutiny.

---

## ATTACK 4: The CFOL-dτ Disconnect — Two Unrelated Results

### The Two Pillars of DGF

The `knowledge_graph.json` and `literature_audit.md` identify DGF's unique contributions:

**Quantum Information Side (CFOL):**
- CFOL theorem: causal topology ↔ QCMI (necessary and sufficient condition)
- η_0 = 1/(8 ln 2): causal ring minimum QCMI
- QCMI → decoherence mapping: D = 1 - exp(-κ·QCMI)

**Classical Gravity Side (dτ = q·dt):**
- q = exp(-GM/rc²) from RG flow
- Metric ds² = -q²dt² + q^{-2}dx²
- 2PN GW deviations

### Where Is the Connection?

CFOL is a theorem about quantum non-Markovianity on causal graphs. It relates the topology of a causal graph (specifically, the existence of causal rings, measured by the first Betti number b1) to the conditional quantum mutual information (QCMI) between nodes. It is a statement about quantum information flow on discrete structures.

dτ = q·dt is a classical hypothesis about proper time in a continuous spacetime. q is interpreted as "quantum channel openness" — the fraction of quantum channels that remain coherent on a causal edge.

**The gap is enormous.** CFOL establishes that b1 > 0 ⇒ QCMI > 0 (causal rings force quantum non-Markovianity). But CFOL says nothing about:
- How q scales with distance from a mass
- Why q should equal exp(-GM/rc²)
- How proper time relates to q
- How the metric emerges

**There is no derivation in any DGF document that connects CFOL to dτ = q·dt.** The two are presented as parts of the same framework, but the mathematical connection is absent. One could publish CFOL as a theorem in quantum information theory, and dτ = q·dt as a hypothesis in gravitational physics, and neither paper would need to cite the other.

### What the Authors Would Need to Show

At minimum:
1. A proof that the q appearing in CFOL (as a channel openness fraction) is the same q that appears in the metric.
2. A derivation showing that the QCMI bound from CFOL (η_0 = 1/(8 ln 2)) constrains the metric field equation.
3. An explicit mapping from the CFOL graph structure (with b1, Cartan axes, etc.) to the emergent metric.

**None of this exists in any DGF document.** The framework claims unity but demonstrates juxtaposition.

---

## FATAL INTERNAL CONTRADICTION: The Graph Does Not Yield a Riemannian Metric

### The Authors' Own Code Demonstrates This

This is the most devastating finding. In `first_principles.py`, lines 173-178:

```python
print(f"\n  KEY FINDING: Graph Laplacian L = div(q grad) is NOT a")
print(f"  Laplace-Beltrami operator for any Riemannian metric.")
print(f"  The continuum limit gives a DIVERGENCE-FORM operator,")
print(f"  not a Laplace-Beltrami operator.")
print(f"  This means the effective metric is not Riemannian.")
print(f"  It is something else -- a Finsler or Weyl structure?")
```

The code then demonstrates (lines 145-178) that for the graph Laplacian L = div(q grad), the continuum limit produces:

```
L f → -h² [q f'' + q' f']  (divergence form)
```

while the Laplace-Beltrami operator for a conformally flat Riemannian metric g_{ij} = Ω² δ_{ij} is:

```
Δ_g f → Ω^{-2}[f'' + (d-2)Ω^{-1} Ω' f']  (not divergence form)
```

The code proves that **no choice of Ω² can make these two operators equal in any dimension d.** The mathematical mismatch is structural, not parametric.

### Why This Is Fatal

The entire DGF phenomenology is built on the assumption that the causal graph's continuum limit is described by a Riemannian metric:

```
ds² = -q² c² dt² + q^{-2}[dr² + r² dΩ²]
```

All DGF predictions — binding energy, GW phase shifts, PPN parameters, cosmological w(z) — follow from this metric. But the authors' own first-principles simulation code proves that the graph Laplacian (which is supposed to give the spatial metric) does NOT converge to a Laplace-Beltrami operator for any Riemannian metric.

**The metric used in DGF_FINAL_COMPLETE.py is mathematically incompatible with the causal graph from which it allegedly derives.**

### The Authors' Response to This (and Why It Fails)

In `THE_TRUTH.md`, the authors acknowledge this incompatibility and propose several "unexplored directions":

1. **Direction 1: "Accept the dual geometry, compute correct Ω²."** The correct Ω² (review E) produces 92% 1PN deviation — already ruled out by LIGO. This kills the theory, not saves it.

2. **Direction 2: "Abandon the metric, use graph operators directly."** This would require rebuilding all phenomenology from scratch. No such calculations exist.

3. **Direction 3: "Weyl geometry — autoparallel vs. geodesic."** This is a classification problem, not a derivation. Which path do particles follow, and why?

4. **Direction 4: "g_{φφ} ≠ R²."** This would change the 2PN predictions in unknown ways.

5. **Direction 5: "Stop claiming to derive GR."** This is the only honest statement in the document.

Despite writing `THE_TRUTH.md` — which honestly acknowledges that "the graph does not yield a single Riemannian metric" and that "dτ = q·dt is a physical interpretation, not a graph-theoretic derivation" — the authors proceed to publish `DGF_FINAL_COMPLETE.py` and `DGF_CLOSURE.md` which claim exactly the opposite: that the graph yields a unique Riemannian metric and that all predictions follow from the single hypothesis dτ = q·dt.

**This is not just a contradiction — it is a documented internal inconsistency.** The authors know (and have written) that their core claim is false, and have released final versions that assert it anyway.

---

## SYNTHESIS: What DGF Actually Is

Stripped of its packaging, DGF consists of:

1. **A quantum information theorem (CFOL):** Causal topology forces quantum non-Markovianity. This is a genuine contribution to quantum information theory. It has nothing to do with gravity.

2. **A classical scalar-tensor theory:** q = exp(-GM/rc²) + the metric ds² = -q²dt² + q^{-2}dx². This is mathematically equivalent to dilaton gravity with an exponential coupling (the authors' own literature audit confirms this). It was not "derived" from information theory — the parameter α=1 was calibrated to reproduce the Newtonian limit, and the spatial metric exponent b=2 was selected by demanding consistency with the equivalence principle.

3. **A claim of unification:** The q in (1) and the q in (2) are asserted to be the same entity. This is the entire "unification" — an identification, not a derivation.

**The unification is performed by fiat, not by mathematics.**

### What This Means for the GW Predictions

Even if the GW 2PN predictions were technically correct (which review E demonstrates they are not), they would not constitute a test of the information-theoretic foundation. They would test the classical scalar-tensor theory, which happens to be dilaton gravity in a particular gauge. Deviations from GR at 2PN in dilaton gravity are not evidence that "information creates spacetime" — they are evidence that a scalar field couples non-minimally to gravity, which has been known since Brans-Dicke (1961).

---

## COMPARATIVE ASSESSMENT

### Against Review A-F

| Review | Finding | Fate in Final Version |
|--------|---------|----------------------|
| A (first principles) | g_00 not derived | Addressed by asserting dτ = q·dt → g_00 = -q² |
| B (cross-discipline) | Literature gap | Partially filled (literature_audit.md) |
| C (cosmology) | H₀ = 120 error | Fixed (was calculation error) |
| D (completeness) | Inspector immunity | Partially addressed |
| E (GW 2PN) | **FATAL: Ω² wrong, 92% 1PN deviation already ruled out** | **NOT addressed in final version** |
| F (foundations) | **FATAL: 7 hidden choices, circular α, no operational definition of q** | **NOT addressed in final version** |

Review E's central finding — that the correct Ω² formula produces 92% 1PN deviation, already excluded by LIGO GWTC-3 — is never addressed in any final DGF document. The final code (`DGF_FINAL_COMPLETE.py`) uses an Omega² formula that review E proved is incorrect. The numerical "predictions" in the final summary are computed from formulas that the authors know (or should know, having received review E) are wrong.

Review F's finding — that "dτ = q·dt" packages at least 7 independent choices — is similarly unaddressed. The final documents continue to present dτ = q·dt as a "single hypothesis."

### The Degeneration Pattern

Over six rounds of review, the pattern is clear: when an error is found, the authors adjust definitions, add caveats, or change the formula — but never confront the structural problem. The theory has been immunized against falsification through continuous redefinition.

- **Round 1:** Binding energy sign error → fixed
- **Round 2-3:** GW phase integration errors → fixed
- **Round 4:** Inspector immunity → "addressed" by changing labels
- **Round 5:** Ω² formula is wrong → NOT FIXED, final version still uses wrong formula
- **Round 6:** 7 hidden choices, circular foundation → NOT ADDRESSED

The theory is now in a state where the final code uses formulas that have been mathematically demonstrated to be incorrect, the foundation has been shown to be circular, and the authors' own first-principles code contradicts the central claim.

---

## FINAL SUMMARY TABLE

| Attack | Finding | Severity |
|--------|---------|----------|
| 1: No free parameters | α=1 is calibrated against GR's Newtonian limit, not derived; the claim of "no free parameters" is false | **FATAL** |
| 2: Cosmological emptiness | DGF ≈ ΛCDM on all cosmological scales; no new observable predictions; screening hides all deviations | **MAJOR** |
| 3: dτ = q·dt unfalsifiable | The hypothesis cannot be tested independently of gravitational phenomena; it is a reinterpretation, not a new theory | **FATAL** |
| 4: CFOL-dτ disconnect | No mathematical connection between the quantum information theorem and the classical gravity hypothesis; two unrelated results | **FATAL** |
| INTERNAL CONTRADICTION | `first_principles.py` proves the graph Laplacian is NOT a Laplace-Beltrami operator for any Riemannian metric, yet the entire DGF phenomenology uses a Riemannian metric | **FATAL — SELF-DOCUMENTED** |

---

## RECOMMENDATION

**REJECT. Do not encourage resubmission.**

The DGF project exhibits a structural failure mode that no amount of revision can fix: the central claim (that a causal graph with q-weighted edges yields a Riemannian metric from which GR is "derived") is mathematically false — as demonstrated by the authors' own first-principles simulation code. The remaining components are either (a) an independent quantum information theorem with no gravitational content (CFOL), or (b) a classical scalar-tensor theory mathematically equivalent to dilaton gravity with calibrated parameters.

The CFOL theorem may merit publication in a quantum information journal (Physical Review A, Quantum, or similar), where it can be evaluated as a theorem in quantum information science without the gravitational baggage. The classical scalar-tensor theory — once its parameters are acknowledged as calibrated rather than derived — may be of minor interest to the scalar-tensor gravity community, though its predictions are already inconsistent with LIGO constraints when correctly computed (review E).

**What should NOT happen:** The authors should not attempt to resubmit DGF as a unified theory of quantum gravity. The unification is a claim, not a derivation. The derivation contains a documented mathematical contradiction. The "predictions" are artifacts of incorrect formulas. Six rounds of review have not resolved these issues because they are structural, not cosmetic.

The honest scientific contribution of this work is the CFOL theorem. Everything beyond that — the metric "derivation," the GW "predictions," the cosmological "explanation" — is infrastructure built on a foundation that the authors' own code proves cannot support it.

---

*Referee G, Nature Physics Panel*
*Date: 2026-06-10*
