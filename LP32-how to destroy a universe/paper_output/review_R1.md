# R1 Review Report — Classification & Verdict

## Reviewer Verdict: REJECT
**AI4 Instant-Death Check**: None of 5 R1 instant-death triggers activated:
1. Testability death: ❌ (bound IS testable with projective measurements)
2. Core proof error: ❌ (proof is mathematically correct within assumptions)
3. Prior art ≥70% coverage: ❌ (Budini 2018 is related but doesn't cover core result)
4. Category error: ❌ (framework is physically coherent)
5. Data unavailable: ❌ ($q_S$, $q_E$, $N_{\rm back}$ are measurable)

**Decision per AI4 §5**: Proceed to R2. FATALs are about framing/interpretation, not mathematical correctness.

---

## Issue Classification

### FATAL Issues (4)

| # | Issue | Root Cause | Fixable? |
|---|-------|-----------|----------|
| F1 | Non-trivial regime ($q_S<q_E$) not "standard decoherence" | Overclaim about physical regime | ✅ Reframe as prepared states |
| F2 | Bound doesn't specifically constrain non-Markovianity | Conceptual gap between toggle-counting and NM measures | ✅ Reframe scope: constraint on determination transfer, one mechanism contributing to backflow |
| F3 | "Determined/undetermined" lacks operational definition | Epistemic language unnecessary for the math | ✅ Replace with standard QM population language |
| F4 | Missing Budini PRA 97, 052133 (2018) — NM without backflow | Literature gap | ✅ Add citation + discussion |

### MAJOR Issues (5)

| # | Issue | Fix |
|---|-------|-----|
| M1 | Collision model has no actual computation | Add explicit dynamics or remove "illustration" claim |
| M2 | $T_1$ correction not derived, breaks counting | Derive properly or acknowledge limitation |
| M3 | MSV complementarity overstated | Honest comparison: trade generality for simplicity |
| M4 | Physical origin of $L_{S\to E}$ insufficient in main text | Add paragraph sketching microscopic origin |
| M5 | Ensemble vs single-run conflation | Add probabilistic bound or restrict to asymptotic |

### MINOR Issues (4)

| # | Issue | Fix |
|---|-------|-----|
| m1 | $\mathcal{R}$ definition confusing in abstract | Clarify in abstract |
| m2 | Einselection→binary capacity connection asserted not argued | Separate basis selection from dimension constraint |
| m3 | Abstract implies $N_{\rm back}$ is easily measured | Clarify measurement challenge |
| m4 | Figure not verifiable | Figure exists, accessible to editor |

---

## Key Strategic Decisions for Revision

1. **Title**: Remove "Non-Markovian" → emphasize "Determination Transfer" or "Information Backflow"
2. **Reframe**: Bound constrains toggle-event backflow, which is ONE mechanism for NM but not all NM
3. **Language**: Replace "determined/undetermined" with standard $\langle 0|\rho|0\rangle$ population language
4. **Scope**: Honestly acknowledge $q_S < q_E$ requires state preparation
5. **Literature**: Add Budini 2018 + clarify Buscemi relationship
