# Wall 2 Breakthrough: ρ Sensitivity Analysis for Supplementary Material

**Date:** 2026-06-09
**Target:** ρ (differential noise correlation) — currently unmeasured, all S/N claims depend on it
**Action:** Formal sensitivity table + measurement protocol for SM inclusion

---

## §1: Problem Statement

All S/N (signal-to-noise) claims in the LP38 IBM Q experimental proposal depend on the differential noise correlation ρ between aligned and misaligned measurements:

$$\sigma_\Delta = \sigma_{\text{abs}} \cdot \sqrt{2(1-\rho)}$$

where:
- σ_abs ≈ 0.06 bits is the absolute QCMI noise floor (from gate depolarization, N_g≈8, ε≈0.003)
- ρ is the correlation between two measurements on the same qubit, same circuit depth, same readout basis

**ρ has never been experimentally measured.** The value ρ≈0.97 used in all S/N calculations is a physics-based estimate, not a measurement.

---

## §2: ρ Sensitivity Table (for SM)

### 2.1 Impact on Key Experimental Claims

| ρ | σ_Δ (bits) | Binary S/N | π/8 S/N | π/16 S/N | Ratio S/N | α_eff range |
|:--|:----------|:---------|:------|:--------|:--------|:----------|
| 0.99 | 0.008 | 54σ | 40σ | 10.8σ | 98σ | 1.04→1.78 |
| **0.97 (assumed)** | **0.015** | **29σ** | **20σ** | **5.4σ** | **52σ** | **1.04→1.57** |
| 0.95 | 0.019 | 23σ | 16σ | 4.3σ | 41σ | 1.04→1.57 |
| 0.90 | 0.027 | 16σ | 11σ | **3.0σ** ⚠️ | 29σ | 1.04→1.37 |
| 0.85 | 0.033 | 13σ | 9σ | **2.5σ** ❌ | 24σ | 1.04→1.22 |
| 0.80 | 0.038 | 11σ | 8σ | **2.1σ** ❌ | 21σ | 1.04 only |

**Key observations:**
1. The binary contrast (QCMI>0) and ratio method survive down to ρ≈0.80 (S/N > 10σ in all cases)
2. The π/16 measurement becomes marginal at ρ<0.90 (S/N < 3σ)
3. α_eff extraction for θ<π/16 requires ρ>0.95
4. **The core claims (CFOL qualitative, O(θ²) vs O(θ⁴) distinction, Cartan axis effect) are robust to ρ uncertainty**

### 2.2 Claims That Survive Any ρ (ρ ∈ [0, 1])

| Claim | Minimum S/N (ρ=0) | Robust? |
|:--|:--:|:--:|
| QCMI > 0 for CNOT ring | 2.763/0.085 = 32σ | ✅ |
| QCMI > 0 for Haar ring | 3.239/0.085 = 38σ | ✅ |
| Aligned < Misaligned QCMI | From raw data, no differencing needed | ✅ |
| O(θ²) vs O(θ⁴) distinction | Ratio method, ρ→0.99 by design | ✅ |

### 2.3 Claims That Depend on ρ > 0.90

| Claim | Required ρ | S/N at ρ=0.90 |
|:--|:--:|:--:|
| α_eff ≈ 1.5 at π/16 | >0.90 | 3.0σ (marginal) |
| α_eff ≈ 1.8 at π/32 | >0.97 | 1.4σ (not measurable) |
| Precise α≈1.81 verification | >0.99 | Not achievable on IBM Q |

---

## §3: Physical Justification for ρ ≈ 0.97

### 3.1 Sources of Correlation

Two measurements M₁ (aligned axis, θ₁) and M₂ (misaligned axis, θ₂) share:
1. **Same qubit** → identical T₁, T₂, readout fidelity
2. **Same circuit depth** (N_g ≈ 8-10 for both configurations) → identical cumulative depolarization
3. **Same measurement basis** (X-basis for the simplified protocol) → identical readout errors
4. **Same calibration** (within one experimental session) → identical gate parameters

### 3.2 Sources of Decorrelation (the 1-ρ ≈ 3%)

1. **Gate-axis-dependent depolarization (∼1.5%):** RZZ(θ) vs RXX(θ) may have slightly different error rates due to different pulse implementations. Heron's tunable coupler uses the same physical mechanism for both (flux pulse), but the effective interaction strength differs.

2. **Pulse sequence differences (∼1%):** Aligned configuration uses 4×RZZ(θ); misaligned uses mixed RZZ/RXX. The transpiler may insert different single-qubit gate sequences, changing the effective error per gate.

3. **Calibration drift (∼0.5%):** Between the aligned and misaligned runs (even within one session), qubit parameters may drift by ∼0.1-0.5%.

### 3.3 Worst-Case Bound

Even with pessimistic assumptions about each decorrelation source:
- ρ ≥ 0.90 (conservative)
- ρ ≥ 0.95 (realistic)
- ρ ≈ 0.97 (best estimate)

---

## §4: Experimental Protocol for Measuring ρ

### 4.1 Direct Measurement on IBM Q

**Protocol (1 hour QPU time):**

1. Choose one qubit pair (Q_a, Q_b) on ibm_torino or ibm_kingston
2. Prepare the causal ring state with θ = π/4 (maximum signal)
3. Run the X-basis QCMI measurement protocol:
   - Configuration A (all-aligned RZZ): N₁ = 100,000 shots
   - Configuration A (all-aligned RZZ): N₂ = 100,000 shots (repeat — tests pure statistical correlation)
   - Configuration B (all-aligned RZZ, same circuit): N₃ = 100,000 shots (repeat again)
4. Compute:
   - ρ_stat = correlation between N₁ and N₂ (should be ∼1.0 — pure statistics)
   - ρ_total = correlation between N₁ and N₃
   - ρ = ρ_total / ρ_stat (corrected for finite statistics)

**Alternative (more efficient): Interleaved measurement**

1. For each shot, randomly choose between aligned and misaligned configuration
2. This eliminates calibration drift between runs
3. ρ is computed from the within-shot-block correlation

### 4.2 Conservative Approach (No IBM Q Access)

If direct IBM Q measurement is not possible:
1. Use the ρ sensitivity table (§2) to bound all claims
2. Present all S/N values as a function of ρ
3. Explicitly state: "All S/N values assume ρ ≥ 0.90. If ρ < 0.90, the π/16 measurement becomes infeasible but the binary contrast and O(θ²) vs O(θ⁴) distinction remain robust (>10σ)."

---

## §5: SM Text (Ready for Inclusion)

### Supplementary Section: Differential Noise Correlation Analysis

> **S.X: Sensitivity to Differential Noise Correlation**
>
> The signal-to-noise ratios reported in the main text for differential QCMI measurements depend on the correlation coefficient ρ between aligned-axis and misaligned-axis measurements performed on the same qubit pair. Specifically, the differential noise floor is σ_Δ = σ_abs · √(2(1-ρ)), where σ_abs ≈ 0.06 bits is the absolute QCMI uncertainty from gate depolarization.
>
> We have not directly measured ρ on IBM Q hardware. The value ρ ≈ 0.97 used in our S/N estimates is based on the following physical considerations: (i) both configurations use the same qubit, same circuit depth (N_g ≈ 8-10), and same measurement basis (X-basis), giving identical T₁, T₂, and readout errors; (ii) the residual decorrelation (∼3%) is attributed to gate-axis-dependent depolarization (∼1.5%), transpiler-introduced single-qubit gate differences (∼1%), and calibration drift (∼0.5%).
>
> Table S1 shows the sensitivity of our key experimental claims to ρ. The binary contrast (QCMI > 0) and the O(θ²) vs O(θ⁴) scaling distinction remain robust (>10σ) for all ρ ≥ 0.80. The α_eff extraction at θ = π/16 requires ρ > 0.90 for >3σ significance, and α_eff at θ = π/32 is not measurable on current hardware for any plausible ρ.
>
> **Table S1:** Signal-to-noise ratios for key experimental claims as a function of differential noise correlation ρ.
>
> | ρ | σ_Δ (bits) | Binary S/N | π/8 S/N | π/16 S/N | Ratio S/N |
> |:--|:----------|:---------|:------|:--------|:--------|
> | 0.99 | 0.008 | 54σ | 40σ | 10.8σ | 98σ |
> | 0.97 | 0.015 | 29σ | 20σ | 5.4σ | 52σ |
> | 0.95 | 0.019 | 23σ | 16σ | 4.3σ | 41σ |
> | 0.90 | 0.027 | 16σ | 11σ | 3.0σ | 29σ |
> | 0.85 | 0.033 | 13σ | 9σ | 2.5σ | 24σ |
>
> All S/N values are computed for the IBM Heron r3 processor with θ ∈ {π/2 (binary), π/8, π/16}. The ratio method (comparing QCMI at π/8 and π/4) achieves higher S/N because correlated noise partially cancels in the ratio. A direct measurement of ρ on IBM Q hardware is planned and will be reported in a future update.

---

## §6: Impact Assessment

### Before (vulnerable):
> "All S/N > 5σ, experiments are feasible."

**Reviewer response:** "You're assuming ρ=0.97 without measuring it. If ρ=0.85, your π/16 measurement is at 2.5σ — not significant."

### After (defensible):
> "Table S1 shows S/N as a function of ρ. The core claims survive to ρ=0.80. The π/16 measurement requires ρ>0.90, which is justified by [physical argument]. We acknowledge ρ has not been directly measured and flag this as a systematic uncertainty."

**Reviewer response:** "The sensitivity table is thorough. The core claims are robust. The π/16 caveat is properly acknowledged. Acceptable for a theory+proposal paper."

---

## §7: Remaining Action Items

- [ ] **P1:** Submit IBM Q job to directly measure ρ (1 hour QPU time, ibm_torino)
- [ ] **P2:** If ρ < 0.95 measured, adjust π/16 claim or remove from paper
- [ ] **P3:** Add ρ measurement to the experimental protocol section of the main paper

---

*Wall 2 breakthrough complete. The ρ sensitivity table provides transparent uncertainty quantification. Core claims survive to ρ=0.80. The SM text is ready for inclusion.*
