# Task 1: CJ Bridge u₄ Edge — Quantitative Cartan Correction (W2-CORRECTED)

**Date:** 2026-06-09 (corrected after W2 analytic derivation)
**Task:** Determine Cartan coefficient of CJ boundary edge u₄ and effective η₀ correction factor
**Status:** CORRECTED. Previous f_CJ=0.54-0.72 interpretation was WRONG. See W2_CJ_Quantitative_Mapping.md for the analytic derivation.

---

## §0 Executive Summary (CORRECTED)

**Correction:** The previous version claimed f_CJ = QCMI_temporal/QCMI_spatial = 0.537 proves the CJ boundary u₄ contributes entangling Cartan. This was WRONG. W2 proved that this ratio compares QCMI on INCOMPARABLE physical systems (3-qubit temporal vs 6-qubit spatial). It has no fundamental significance as a Cartan correction.

**Correct result (from W2 analytic derivation):**

| Edge | Cartan c^(i)_z | Op-Schmidt rank | Physical origin |
|:-----|:--------------|:----------------|:----------------|
| u₁ (Q_a→E₁) | θ₁/2 | 2 | First Q-E interaction U₁ |
| u₂ (E₁→Q_b) | 0 | 1 (product) | Identity period (I⊗I) |
| u₃ (Q_b→E₂) | θ₂/2 | 2 | Second Q-E interaction U₂ |
| u₄ (E₂→Q_a) | 0 | 1 (product) | CJ boundary (I⊗I) |

**Only 2 of 4 edges carry non-zero Cartan.** The Cartan sum ratio vs a 4-edge spatial ring is:

$$\boxed{\frac{\Sigma|c|^2_{\text{CJ}}}{\Sigma|c|^2_{\text{spatial, 4-edge}}} = \frac{(\theta_1/2)^2 + (\theta_2/2)^2}{4(\theta/2)^2} = \frac{5}{16} = 0.3125}$$

This is CONSTANT for all θ. The previous f_CJ = 0.537 was QCMI_temporal/QCMI_spatial — comparing two different Hilbert spaces (3-qubit vs 6-qubit). The CJ boundary u₄ = I⊗I has ZERO Cartan under the natural copy isometry.

**The temporal QCMI is solved ANALYTICALLY (W2):**

$$\boxed{\text{QCMI}(\theta_1, \theta_2, p) = H_2\!\left(\frac{1}{2}\left(1 + \sqrt{1 - 4p(1-p)\sin^2(\theta_1+\theta_2)}\right)\right)}$$

This matches numerical simulation to < 10⁻⁴. For p=0.7, θ₁=π/2, θ₂=π/4: QCMI = 0.527 bits.

**The <1.5 criterion:** The Cartan sum ratio 0.3125 is well within the criterion. The old f_CJ concern was based on a misinterpretation.

---

## §1 What Went Wrong in the Original Analysis

### 1.1 The erroneous interpretation

The original analysis computed:

```
f_raw = QCMI_temporal / QCMI_spatial
```

and interpreted this as a "Cartan correction factor" — the ratio of effective Cartan sums. This interpretation assumed:

1. **False assumption 1:** QCMI ∝ Σ|c|² (proportional to Cartan sum). **Reality:** QCMI is 2-4× larger than η₀·Σ|c|² due to ring/log enhancement, and the enhancement factor differs between temporal and spatial systems.

2. **False assumption 2:** Temporal and spatial QCMI are comparable. **Reality:** Temporal QCMI = I(R;E|Q) on 3 qubits (8D). Spatial QCMI = I(Ra,Rb;E1,E2|Qa,Qb) on 6 qubits (64D). These are fundamentally different information-theoretic quantities.

### 1.2 Why f_raw varies with θ

| θ₁ | QCMI_temporal | QCMI_spatial (4-edge) | f_raw | Cartan ratio |
|:---|:------------|:--------------------|:----|:------------|
| π/2 | 0.527 | 0.981 | 0.537 | **0.3125** |
| π/4 | 0.785 | 1.094 | 0.717 | **0.3125** |
| π/8 | 0.365 | 0.529 | 0.690 | **0.3125** |

f_raw varies (0.54→0.72) because the log enhancement κ(θ) differs between the two systems. The Caran ratio is CONSTANT at 0.3125.

### 1.3 The correct comparison

The meaningful quantity is:

$$\frac{\Sigma|c|^2_{\text{CJ}}}{\Sigma|c|^2_{\text{spatial}}} = \frac{\text{2 entangling edges}}{\text{4 entangling edges}} = \frac{1}{2} \times \frac{1+(\theta_2/\theta_1)^2}{2} = \frac{5}{16}$$

when θ₂=θ₁/2. This reflects the structural fact that the CJ temporal process has TWO physical entangling interactions (U₁, U₂), while the spatial ring can have up to FOUR.

---

## §2 The Correct Cartan Structure (from W2)

### 2.1 The copy isometry

The copy isometry V: |q,e⟩ → |q⟩_Qa|e⟩_E1|q⟩_Qb|e⟩_E2 maps the 2-qubit temporal QE system to the 4-node spatial ring. Under this isometry:

- **u₁ = RZZ(θ₁/2)** on Q_a⊗E₁: inherits Cartan from U₁
- **u₂ = I⊗I** on E₁⊗Q_b: identity period, no entangling power
- **u₃ = RZZ(θ₂/2)** on Q_b⊗E₂: inherits Cartan from U₂
- **u₄ = I⊗I** on E₂⊗Q_a: CJ boundary, no entangling power

The channel equality holds: V†(u₄u₃u₂u₁)V = RZZ(θ₁+θ₂) = U_temporal.

### 2.2 Why u₄ has zero Cartan

The CJ boundary in the Buscemi picture is the |Φ⁺⟩ pairing between input Q₀ and output Q₅. This pairing is ALREADY encoded in the initial Bell pair |Φ⁺⟩_{RQ} — there is no additional entangling unitary needed on the E₂-Q_a edge. The "feedback" from E₂ to Q_a occurs through the QCMI computation (specifically through the S(RQ) term), not through a dynamical gate.

### 2.3 The lower bound (consistent with CFOL)

$$\text{QCMI}_{\text{temporal}} \geq \eta_0 \cdot \left(|c^{(1)}|^2 + |c^{(3)}|^2\right) = \eta_0 \cdot \left((\theta_1/2)^2 + (\theta_2/2)^2\right)$$

For θ₁=π/2, θ₂=π/4: QCMI ≥ 0.180 × 0.771 = 0.139 bits. Actual QCMI = 0.527 bits (3.8× larger — the log enhancement).

---

## §3 Remaining Caveat: Isometry Dependence

W2's SA-2 acknowledges: c^(4)=0 depends on the choice of isometry V. A different isometry could redistribute Cartan among edges while preserving the total c₁+c₂+c₃+c₄ = (θ₁+θ₂)/2. The copy isometry is the NATURAL choice (it respects the physical interpretation of each effective node), but it is not mathematically unique.

For the all-RZZ-diagonal case, the copy isometry is physically privileged:
- u₂ corresponds to the identity period → MUST be product (no interaction)
- u₄ corresponds to the CJ boundary → information-theoretic, not dynamical

For general non-commuting U₁, U₂ with different Cartan axes, the isometry construction is more subtle (GAP-2 in W2).

---

## §4 Key Formula (CORRECTED)

$$\boxed{\begin{aligned}
\text{CJ Temporal Ring (W2 analytic derivation):} & \\
c^{(1)}_z = \theta_1/2, \quad c^{(2)} = 0, \quad c^{(3)}_z = \theta_2/2, \quad c^{(4)} = 0 & \\
\text{QCMI}(\theta_1,\theta_2,p) &= H_2\!\left(\frac{1}{2}\left(1 + \sqrt{1 - 4p(1-p)\sin^2(\theta_1+\theta_2)}\right)\right) \\
\text{Cartan sum ratio} &= \frac{(\theta_1/2)^2 + (\theta_2/2)^2}{4(\theta/2)^2} = \frac{5}{16} = 0.3125 \quad (\theta_2=\theta_1/2) \\
\text{Criterion } f < 1.5&\text{: SATISFIED } \checkmark \quad (0.3125 \ll 1.5)
\end{aligned}}$$

**Only 2 of 4 effective edges carry non-zero entangling Cartan. The CJ boundary u₄ = I⊗I. The old f_CJ=0.54-0.72 was a QCMI ratio on incomparable systems, not a Cartan correction.**

---
*Task 1 corrected. Previous f_CJ interpretation withdrawn. See W2_CJ_Quantitative_Mapping.md for full analytic derivation.*
