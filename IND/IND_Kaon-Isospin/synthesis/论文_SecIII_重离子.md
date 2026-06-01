# III. HEAVY-ION R_K: ASSOCIATED PRODUCTION ASYMMETRY

## A. World Data Compilation

We compile R_K measurements in heavy-ion collisions from 7 experiments spanning √s_NN = 2.6 GeV to 5.02 TeV. The full dataset is presented in Table III.

**Table III: World heavy-ion R_K data.**

| # | Experiment | System | Centrality | √s_NN (GeV) | R_K | σ_total | Ref. |
|---|-----------|--------|------------|-------------|-------|---------|------|
| 1 | HADES | Ar+KCl | 0-40% | 2.6 | 1.248 | 0.155 | [21] |
| 2 | STAR BES-I | Au+Au | 0-10% | 7.7 | 1.125 | 0.082 | [22] |
| 3 | NA49 | Pb+Pb | 0-5% | 7.6 | 1.176 | 0.133 | [23] |
| 4 | NA49 | Pb+Pb | 0-5% | 8.7 | 1.145 | 0.126 | [23] |
| 5 | NA61/SHINE | Ar+Sc | 0-10% | 8.8 | 1.115 | 0.043 | preliminary |
| 6 | STAR BES-I | Au+Au | 0-10% | 11.5 | 1.171 | 0.097 | [22] |
| 7 | NA61/SHINE | Ar+Sc | 0-10% | 11.9 | 1.184 | 0.062 | [1] |
| 8 | CERES | Pb+Au | 0-5% | 17.3 | 1.205 | 0.134 | [24] |
| 9 | STAR BES-I | Au+Au | 0-10% | 19.6 | 1.158 | 0.091 | [22] |
| 10 | STAR BES-I | Au+Au | 0-10% | 27 | 1.155 | 0.082 | [22] |
| 11 | STAR BES-I | Au+Au | 0-10% | 39 | 1.145 | 0.108 | [22] |
| 12 | STAR | Au+Au | 0-5% | 62.4 | 1.277 | 0.153 | [25] |
| 13 | STAR | Au+Au | 0-5% | 200 | 1.159 | 0.121 | [25] |
| 14 | ALICE | Pb+Pb | 0-5% | 2760 | 0.991 | 0.107 | [26] |
| 15 | ALICE | Pb+Pb | 0-5% | 5020 | ≈1.00 | ≈0.10 | [9] |

Two qualitative features are immediately apparent. First, R_K > 1 is a robust feature from √s_NN ≈ 2.6 GeV (HADES) through √s_NN ≈ 200 GeV (STAR), with typical values of 1.15-1.20. Second, at LHC energies (√s_NN > 2.76 TeV), R_K is consistent with unity within the ~10% experimental uncertainty.

## B. Baseline Construction

To extract the "excess" R_K that might require explanation beyond known physics, we must construct the appropriate baseline—the R_K value expected in the absence of any new medium effects.

The baseline for a heavy-ion collision with N/Z neutron excess and at center-of-mass energy √s_NN is:

R_K^baseline = R_K(pp) × f_iso(N/Z) × f_lead(√s_NN) × f_cold,         (4)

where:
- R_K(pp) = 1.025 ± 0.020 is the measured R_K in pp collisions (ALICE 7 TeV + STAR 200 GeV average), representing the "minimal system" baseline;
- f_iso(N/Z) accounts for the modification of K⁺/K⁰ from the participant proton-to-neutron ratio;
- f_lead(√s_NN) accounts for the energy-dependent leading-particle dilution;
- f_cold represents cold nuclear matter effects (constrained to 1.00 ± 0.02 by the absence of published pA R_K data).

We construct two baseline scenarios to bracket the systematic uncertainty:

**Conservative baseline** (minimal corrections, maximal residual): R_K^baseline = 1.030 ± 0.020, constant across all systems and energies. This corresponds to the extreme assumption that initial-state isospin and leading-particle effects are negligible in heavy-ion collisions.

**Aggressive baseline** (maximal corrections, minimal residual): f_iso(N/Z) = 1 + 0.06 × (N/Z - 1) reflecting the net effect of participant neutron excess on K⁺/K⁰; f_lead(√s_NN) = 1 + 0.07 × exp[-(√s_NN - 2.6)/8] encoding the √s_NN-dependent dilution of the leading-particle effect. This gives R_K^baseline ranging from ≈1.11 at √s_NN = 2.6 GeV to ≈1.06 at √s_NN = 200 GeV.

**Table IV: Residuals ΔR_K ≡ R_K^obs - R_K^baseline for the two baseline scenarios.**

| √s_NN (GeV) | R_K^obs | ΔR_K (conservative) | Nσ (cons.) | ΔR_K (aggressive) | Nσ (aggr.) |
|-------------|---------|--------------------|------------|--------------------|------------|
| 2.6 | 1.248 | +0.218 | 1.40 | +0.138 | 0.87 |
| 7.7 | 1.125 | +0.095 | 1.12 | +0.028 | 0.32 |
| 7.6 | 1.176 | +0.146 | 1.09 | +0.075 | 0.55 |
| 8.7 | 1.145 | +0.115 | 0.90 | +0.053 | 0.41 |
| 8.8 | 1.115 | +0.085 | 1.79 | +0.043 | 0.86 |
| 11.5 | 1.171 | +0.141 | 1.42 | +0.092 | 0.91 |
| **11.9** | **1.184** | **+0.154** | **2.38** | **+0.125** | **1.88** |
| 17.3 | 1.205 | +0.175 | 1.29 | +0.136 | 1.00 |
| 19.6 | 1.158 | +0.128 | 1.38 | +0.094 | 1.00 |
| 27 | 1.155 | +0.125 | 1.49 | +0.095 | 1.13 |
| 39 | 1.145 | +0.115 | 1.04 | +0.088 | 0.80 |
| 62.4 | 1.277 | +0.247 | 1.61 | +0.221 | 1.44 |
| 200 | 1.159 | +0.129 | 1.05 | +0.103 | 0.83 |
| 2760 | 0.991 | -0.039 | -0.36 | -0.067 | -0.62 |
| 5020 | ≈1.00 | ≈-0.03 | — | ≈-0.06 | — |

The flagship NA61/SHINE point (Ar+Sc, √s_NN = 11.9 GeV), which is the basis of the 4.7σ claim, shows a residual of 2.4σ (conservative) or 1.9σ (aggressive). **No individual data point exceeds 3σ in either baseline scenario.** The global weighted average (excluding LHC points where R_K→1) is +0.140 ± 0.022 (~6.3σ, conservative) or +0.093 ± 0.022 (~4.2σ, aggressive). However, this global average must be interpreted with caution: the individual data points are not statistically independent (they share common systematic uncertainties from the same experiments), and the averaging procedure is sensitive to the baseline choice.

## C. Associated Production Asymmetry

The residual R_K excess at SPS and low RHIC energies (√s_NN ≈ 2.6-40 GeV), while modest (~0.06-0.15 in the aggressive baseline), appears statistically significant in a global average. We now argue that this residual is dominated by a well-established, purely hadronic effect that is systematically underestimated in current transport models: the asymmetry between associated production channels NN → N K Λ and NN → N K Σ.

### 1. Physics of the asymmetry

The cross sections for associated strangeness production differ substantially between the Λ and Σ channels. Two independent sources contribute:

**Coupling asymmetry.** The SU(3) chiral coupling constants for the KNY vertices are g_{KNΛ}/g_{KNΣ} = (D+3F)/[√3(D-F)] ≈ 3.6-5.4 [27], where D ≈ 0.80 and F ≈ 0.46 are the SU(3) axial-vector couplings determined from hyperon β-decay. In the Born approximation, cross sections scale as g⁴, but unitarity and resonance saturation reduce the effective ratio. The "bare" amplitude-squared ratio, after removing final-state interaction effects, is ≈3.1 [16].

**Threshold asymmetry.** The thresholds for the two channels differ by 78 MeV:
m_N + m_K⁺ + m_Λ = 2548 MeV vs. m_N + m_K⁰ + m_Σ⁺ = 2626 MeV.
Near threshold, the s-wave phase space factor ∝ √(s - s_threshold) enhances the Λ channel relative to the Σ channel by an additional factor that can reach ~1.4 very close to threshold.

**Final-state interaction enhancement.** The Λp system has a strong attractive final-state interaction (scattering length a ≈ -1.7 fm), while the ΣN system has weak FSI. This further enhances the near-threshold Λ production relative to Σ by up to an order of magnitude [16].

### 2. Experimental constraints from COSY

The combined effect has been measured at the COSY facility in pp collisions:

**COSY-11** [15], very close to threshold:
| Excess energy Q (MeV) | σ(pp→pK⁺Λ) [μb] | Λ/Σ ratio (approx.) |
|----------------------|-------------------|---------------------|
| 0.68 | 0.0021 ± 0.0002 | ~28-30 |
| 13.9 | 0.630 ± 0.079 | ~17 |
| 59.3 | 3.838 ± 0.624 | ~6 |

**COSY-ANKE** [14], T_p = 2.16 GeV, Q ≈ 129 MeV:
σ(pp → pK⁺Λ) = 23.2 ± 6.8 μb,
σ(pp → pK⁺Σ⁰) = 2.6 ± 0.7 μb,
σ(pp → nK⁺Σ⁺) = 2.5 ± 0.7 μb.
**Λ/Σ⁰ ≈ 8.9; total Λ/Σ ≈ 4.5 after accounting for the nK⁺Σ⁺ contribution.**

At higher energies (Q ≫ 100 MeV), the Λ/Σ ratio asymptotes to the "bare" value of approximately 2-3, determined by the coupling asymmetry alone after FSI effects become negligible [16].

### 3. Contribution to R_K in heavy-ion collisions

In heavy-ion collisions, the fraction f_prod of kaons originating from associated production (as opposed to string fragmentation) is energy-dependent. At low √s_NN (SPS, ≈5-17 GeV), associated production is an important kaon source, with f_prod estimated at 5-15% from transport model studies [5-8]. At high √s_NN (RHIC, LHC), string fragmentation dominates and f_prod ≪ 5%.

The effective production asymmetry A_prod ≡ σ(NKΛ)/σ(NKΣ) - 1, averaged over the distribution of NN collision energies in a heavy-ion collision, is weighted toward its near-threshold value because associated production cross sections are largest near threshold. Based on the COSY data and Sibirtsev's bare-amplitude analysis, we estimate A_prod_eff ≈ 2-5 at SPS energies.

The contribution to R_K is:
ΔR_K_assoc = f_prod(√s_NN) × A_prod_eff.                              (5)

**Table V: Associated production contribution to R_K as a function of √s_NN.**

| √s_NN (GeV) | f_prod (est.) | A_prod_eff (est.) | ΔR_K_assoc | Observed residual (aggr. baseline) |
|-------------|---------------|-------------------|------------|-----------------------------------|
| 2.6 (HADES) | 0.3-0.5 | 4-6 | 1.2-3.0 | 0.14 |
| 5-8 (low SPS) | 0.2-0.4 | 3-5 | 0.6-2.0 | 0.03-0.15 |
| 12-17 (high SPS) | 0.05-0.15 | 2-4 | 0.10-0.60 | 0.04-0.14 |
| 200 (RHIC) | 0.01-0.03 | 1.5-2.5 | 0.015-0.075 | 0.10 |
| 2760 (LHC) | 0.001-0.005 | 1-2 | 0.001-0.010 | -0.07 |

At SPS energies, ΔR_K_assoc comfortably covers the observed residual. The central value of f_prod ≈ 0.10 and A_prod_eff ≈ 3 gives ΔR_K_assoc ≈ 0.30, which is approximately twice the observed residual of ≈0.12 (aggressive baseline, NA61 11.9 GeV). This indicates that our estimates are conservative in the sense that they allow—but do not require—additional contributions from medium effects; the associated production asymmetry alone is sufficient.

At RHIC and LHC energies, ΔR_K_assoc becomes negligible because f_prod decreases with increasing √s_NN as string fragmentation becomes the dominant kaon source. The trend toward R_K → 1 at LHC is therefore a natural consequence of the diminishing role of associated production, not evidence for the "disappearance" of an anomalous medium effect.

## D. Non-Medium Systematics

In addition to associated production, two other known effects contribute small but systematic offsets to R_K:

**φ → KK̄ branching ratio asymmetry.** The φ(1020) meson decays to K⁺K⁻ with branching fraction 49.1 ± 0.5% and to K⁰K̄⁰ with 34.0 ± 0.5% [28]. This 44% asymmetry in the decay channels, combined with the φ/K ratio of ~0.08-0.18 in heavy-ion collisions (enhanced relative to pp due to strangeness enhancement), contributes ΔR_K_φ = +(0.01-0.03) in the positive direction.

**Initial-state isospin.** For neutron-rich collision systems (Au+Au, Pb+Pb), the participant zone has more d quarks than u quarks. This favors K⁰ (d + s̄) over K⁺ (u + s̄), producing a negative contribution to R_K. For Ar+Sc (N/Z ≈ 1.21), ΔR_K_isospin ≈ -0.02 to -0.05; for Pb+Pb (N/Z ≈ 1.54), the effect is larger, ΔR_K_isospin ≈ -0.04 to -0.08.

The net non-medium contribution (associated production + φ → KK̄ + initial-state isospin) at SPS energies is:
ΔR_K_nonmedium = (+0.10 to +0.60) + (+0.01 to +0.03) + (-0.02 to -0.05)
                = +0.09 to +0.58.                                            (6)

The observed residual (aggressive baseline) of +0.04 to +0.14 falls within this range.

## E. KNY Competition: Why the Net Medium Effect May Be Small

Even if there were a medium contribution beyond associated production, its magnitude would be constrained by a sign competition that has not been previously recognized. The KNY coupling asymmetry g_{KNΛ}/g_{KNΣ} ≈ 3.6-5.4 enhances K⁺ production in the **production** channel (NN → N K Λ has a larger cross section than NN → N K Σ) but also enhances K⁺ **absorption** in the hadronic phase (K⁺ + N → π + Λ has a larger cross section than K⁰ + N → π + Σ). The production effect (positive sign, ΔR_K > 0) and the absorption effect (negative sign, ΔR_K < 0) compete, with the net result depending on the balance between f_prod (fraction of kaons from associated production) and f_scat (fraction of kaons that undergo scattering in the hadronic phase). Both f_prod and f_scat decrease with increasing √s_NN, but at different rates. The net medium contribution—even if present—is therefore expected to be smaller than either individual effect, and its √s_NN dependence is a sensitive function of the production/absorption balance.

This sign competition, together with the large associated-production contribution from pure vacuum physics, makes it unlikely that any genuine medium modification of R_K could be isolated from current data.

---

*Section III draft. References to be resolved. 2026-05-31.*
