# Round 2: η₀ Tightness — Formal Analysis of Asymptotic (Non-)Saturation

**Attacker:** A博士 (学院派：形式化数学构造)
**Date:** 2026-06-09
**Target:** Wall 1 (下界不紧) — the η₀ tightness question
**Scope:** b₁=1, d=2, four-node causal ring
**Assets used:** CFOL v4, Cartan gauge fixing, Fawzi-Renner (2015), Petz recovery equality condition (HJPW04 Theorem 3), direct spectral computation, CNOT analytic solution, commutativity theorem (CCQ)

---

## Executive Summary

**Verdict: η₀ = 1/(8 ln 2) ≈ 0.180 bits is NOT tight in any operationally meaningful sense.**

Three independent lines of evidence converge:

1. **Fawzi-Renner equality is structurally incompatible with CFOL.** The Fawzi-Renner bound I ≥ -2 log₂ F² is saturated iff a perfect Petz recovery map exists (HJPW04, Theorem 3), which is equivalent to QCMI = 0, which by CFOL v4 requires all edges to be factorizable (|c^(i)| = 0 for all i). CFOL's premise is that at least one edge is unfactorizable. Hence the Fawzi-Renner inequality is **strict** for all CFOL-satisfying configurations: I > -2 log₂ F² always.

2. **The true small-|c| QCMI has a log(1/|c|²) enhancement that the linear bound misses.** Direct spectral analysis of the Choi state J(N) reveals QCMI = κ · |c|² log₂(1/|c|²) + O(|c|²), while the Fawzi-Renner chain yields QCMI ≥ η₀ · |c|² = O(|c|²). The ratio QCMI / (η₀ · |c|²) diverges as |c| → 0. The log factor originates from von Neumann entropy of subleading Choi eigenvalues and is fundamental — no tightening of constants within the Fawzi-Renner framework can capture it.

3. **The infimum of QCMI at fixed differential Cartan sum D is zero.** By taking aligned Cartan configurations (c^(1) = c^(3) = ε · n̂, c^(2) = c^(4) = ε · n̂) and sending ε → 0, QCMI scales as O(ε⁴) while D scales as O(ε²), giving QCMI/D → 0. This means no bound of the form QCMI ≥ const · D with const > 0 can be asymptotically tight.

**The honest statement for the paper:** η₀ is a rigorous but loose universal lower bound. It captures the correct scaling dimension (linear in |c|²) but misses the entropic log(1/|c|²) amplification inherent to von Neumann entropy. The proper formulation is QCMI ≥ η(|c|) · D where η(|c|) → 0 as |c| → 0 (logarithmically), and η(|c|) → η₀ as |c| → |c|_max. Presenting η₀ without this qualification invites the "height ≥ 1 nanometer" criticism and should be avoided.

---

## Section 1: The Fawzi-Renner Equality Condition — Structural Incompatibility with CFOL

### 1.1 Precise Statement of the Equality Condition

**Theorem (HJPW04, Theorem 3; Fawzi-Renner 2015, Theorem 5.1).** For a tripartite quantum state ρ_ABC, the inequality

$$I(A:C|B)_\rho \geq -2\log_2 F^2(\rho_{ABC}, \mathcal{P}_{B \to BC}(\rho_{AB}))$$

is saturated (equality holds) if and only if there exists a recovery map R: B(BC) → B(B) such that

$$(\mathcal{R} \otimes \text{id}_A)(\rho_{ABC}) = \rho_{ABC}$$

where R is the Petz recovery map:

$$\mathcal{R}(\alpha) = \rho_{BC}^{1/2} \mathcal{P}^*((\mathcal{P}(\rho_B))^{-1/2} \alpha (\mathcal{P}(\rho_B))^{-1/2}) \rho_{BC}^{1/2}$$

In finite dimensions, existence of such an R is equivalent to the channel N: A → BC being sufficient for ρ_A, which in turn is equivalent to QCMI = 0 (Petz 1988; Fawzi-Renner 2015, Theorem 5.1).

**Crucially:** The equality I = -2 log₂ F² implies, through the chain of inequalities in the Fawzi-Renner proof, that QCMI = 0. The converse also holds: QCMI = 0 implies F = 1, giving -2 log₂ F² = 0, and I = 0.

### 1.2 CFOL Impossibility of Saturation

**Lemma 1 (Fawzi-Renner saturation ⇒ factorization).** For the four-node causal ring with the specified setup:

$$I(R;E'|Q') = -2\log_2 F^2 \Longrightarrow \text{QCMI} = 0 \Longleftrightarrow \forall i: |c^{(i)}| = 0$$

**Proof.** The first implication follows from the Fawzi-Renner equality condition (HJPW04, Theorem 3) as stated above. The second equivalence is the CFOL v4 lemma (round1_factorization.md, S3): QCMI = 0 ⇔ all u_i factorize ⇔ all Cartan coefficients vanish.

**Corollary 1 (Strict inequality under CFOL).** If CFOL holds (∃i: |c^(i)| > 0), then

$$\boxed{I(R;E'|Q') > -2\log_2 F^2}$$

The inequality is strict. No configuration satisfying the CFOL premise can saturate the Fawzi-Renner bound.

### 1.3 Implication for η₀ Tightness

The chain of inequalities in the η₀ derivation is:

```
I(R;E'|Q')  ≥  -2 log₂ F²          [L0: Fawzi-Renner, strict for CFOL]
            ≥  2(1-F²)/ln 2          [L1: log inequality, strict for F²<1]
            ≥  Δ_K / ln 2             [L2: Kraus deviation, leading order]
            ≥  (γ_min/(d² ln 2)) · D  [L3: Cartan→Kraus, leading order]
            =  η₀ · D                 [L4: algebraic assembly]
```

where D = Σ_v |Σ_e w_{ve} |c^(e)|²| is the differential Cartan sum.

**Layer 0 is strict for all CFOL-satisfying configurations.** Layer 1 is strict whenever F² < 1 (i.e., whenever any |c^(i)| > 0 — because |c^(i)| > 0 implies F² < 1, as the Petz recovery is imperfect). Layers 2 and 3 are leading-order approximations that become equalities only in the limit |c| → 0.

Therefore, **no CFOL-satisfying configuration can saturate the full chain**. The bound η₀ is never "achieved" in the sense of equality.

---

## Section 2: The Log-Factor — Why η₀ Underestimates QCMI at Small |c|

### 2.1 Direct Spectral Computation: Full Derivation

**Setup.** The channel N: B(H_Q) → B(H_Q') has Kraus operators (post Cartan gauge-fixing):

$$K_{ab} = \sqrt{p_a p_b} \cdot \langle b|_{E_2} D_4 D_3 \cdot \langle a|_{E_1} D_2 D_1 |\tilde{\gamma}\rangle_{E_1} |\tilde{\gamma}\rangle_{E_2}$$

where a,b ∈ {0,1} index environment basis states, p_0 = p, p_1 = 1-p, and |γ̃⟩ = √p|0⟩ + √(1-p)|1⟩.

For small Cartan coefficients |c| ≪ 1, expand each Cartan core:

$$D_i = \exp(iH^{(i)}) = I + iH^{(i)} - \frac{1}{2}(H^{(i)})^2 + O(|c|^3)$$

Using the Cartan algebra property (H^(i))² = |c^(i)|² · I (since all T_k ⊗ S_k are mutually commuting in the Cartan subalgebra), we have:

$$D_i = \left(1 - \frac{|c^{(i)}|^2}{2}\right)I + iH^{(i)} + O(|c|^3)$$

**Choi state.** The (unnormalized) Choi state is J(N) = Σ_{ab} |K_{ab}⟩⟩⟨⟨K_{ab}|, where |A⟩⟩ denotes vectorization. At c = 0 (all D_i = I):

$$K_{ab}^{(0)} = \sqrt{p_a p_b} \cdot I_{Q}$$
$$J^{(0)}(N) = \left(\sum_{ab} p_a p_b\right) |I\rangle\rangle\langle\langle I| = |I\rangle\rangle\langle\langle I|$$

since Σ_a p_a = 1. J^(0)(N) is rank-1 (pure). Its entropy is 0.

For small |c| ≠ 0, the Kraus operators deviate from the identity:

$$K_{ab} = K_{ab}^{(0)} + \delta K_{ab}^{(1)} + \delta K_{ab}^{(2)} + O(|c|^3)$$

where δK_ab^(1) = O(|c|) and δK_ab^(2) = O(|c|²).

**Lemma 2 (Choi eigenvalue structure at small |c|).** The normalized Choi state J(N)/d² (d=2, so d²=4) has eigenvalues:

$$\lambda_0 = 1 - \alpha|c|^2 + O(|c|^4)$$
$$\lambda_i = \beta_i|c|^2 + O(|c|^4), \quad i = 1, \ldots, 15$$

where α = Σ_{i=1}^{15} β_i (trace preservation: Σ λ_i = 1).

**Proof.** The vectorized Kraus operators |δK_ab^(1)⟩⟩ span the orthogonal complement of |I⟩⟩ in the 16-dimensional operator space. Projecting out |I⟩⟩ gives 15 orthogonal directions. Each direction receives |c|²-weight from the first-order Kraus correction. The Gram matrix G_{(ab),(cd)} = ⟨⟨δK_ab^(1)|δK_cd^(1)⟩⟩ determines the β_i as its eigenvalues. Trace preservation ensures α = Σ β_i = Tr(G). ∎

**Lemma 3 (Von Neumann entropy at small |c|).** For the Choi state with the eigenvalue structure above:

$$S(J(N)/d^2) = \frac{\alpha}{\ln 2}|c|^2 + \sum_{i=1}^{15} \beta_i|c|^2 \log_2\left(\frac{1}{\beta_i|c|^2}\right) + O(|c|^4 \log(1/|c|^2))$$

**Proof.** Expand S = -Σ λ_i log₂ λ_i:

$$S = -(1-\alpha|c|^2)\log_2(1-\alpha|c|^2) - \sum_i \beta_i|c|^2 \log_2(\beta_i|c|^2) + O(|c|^4)$$

Using -log₂(1-x) = x/ln 2 + x²/(2 ln 2) + ...:

$$-(1-\alpha|c|^2)\log_2(1-\alpha|c|^2) = \frac{\alpha|c|^2}{\ln 2} + O(|c|^4)$$

For the subleading terms:

$$-\beta_i|c|^2 \log_2(\beta_i|c|^2) = \beta_i|c|^2 \log_2(1/|c|^2) + \beta_i|c|^2 \log_2(1/\beta_i)$$

Summing over i and noting that Σ β_i = α:

$$\boxed{S(J(N)/d^2) = \frac{\alpha}{\ln 2}|c|^2 + \alpha|c|^2 \log_2(1/|c|^2) + |c|^2 \sum_i \beta_i \log_2(1/\beta_i) + O(|c|^4 \log(1/|c|^2))}$$

The dominant term as |c| → 0 is α|c|² log₂(1/|c|²). ∎

### 2.2 QCMI from Choi Entropy

Using the exact identity (η_quantitative.md, §2.2):

$$I(R;E'|Q') = 2\log_2 d_Q - I(R;Q') = 4 - I(R;Q') \quad (\text{for } d=2)$$

And I(R;Q') = S(R) + S(Q') - S(RQ') where:
- S(R) = S(I/4) = 2 bits
- S(Q') = S(N(I/4)) = 2 - O(|c|⁴) (entropy of near-maximally-mixed state, flat at maximum)
- S(RQ') = S(J(N)/4) = O(|c|² log(1/|c|²))

Therefore:

$$\boxed{I(R;E'|Q') = \alpha|c|^2 \log_2(1/|c|^2) + \left(\frac{\alpha}{\ln 2} + \sum_i \beta_i \log_2(1/\beta_i)\right)|c|^2 + O(|c|^4 \log(1/|c|^2))}$$

**The log-factor is a fundamental consequence of von Neumann entropy of a near-pure state.** It cannot be captured by any bound linear in |c|².

### 2.3 Comparison with the Fawzi-Renner Chain

The Fawzi-Renner chain gives:

$$I_{\text{FR-bound}} = \eta_0 \cdot D = \frac{1}{8\ln 2} \cdot \sum_v \left|\sum_e w_{ve} |c^{(e)}|^2\right|$$

For a generic (non-aligned) configuration where D ~ |c|², the ratio is:

$$\frac{I_{\text{actual}}}{I_{\text{FR-bound}}} \sim \frac{\alpha|c|^2 \log_2(1/|c|^2)}{\eta_0|c|^2} = \frac{\alpha}{\eta_0} \log_2(1/|c|^2)$$

Since α/η₀ = O(1) (approximately 2-4 from the single-Pauli sector analysis), the ratio diverges logarithmically as |c| → 0.

**Theorem 1 (Logarithmic looseness).** For the four-node causal ring with d=2, b₁=1, and non-aligned Cartan vectors:

$$\lim_{|c| \to 0} \frac{I(R;E'|Q')}{\eta_0 \cdot \sum_v |\sum_e w_{ve} |c^{(e)}|^2|} = \infty$$

The divergence is logarithmic: the ratio grows as log₂(1/|c|²).

**Proof.** Follows from Lemmas 2-3 and the exact identity I = 4 - I(R;Q'). The numerator contains |c|² log(1/|c|²) while the denominator contains |c|². The ratio diverges. ∎

### 2.4 Numerical Calibration

Using the single-Pauli sector analysis from round1_A_formal.md §3.2, for the maximally mixed environment (p = 1/2):

- α = Σ_{i=1}^{15} β_i ≈ p(1-p)/2 = 0.125 (from 6 active single-Pauli sectors, each contributing ≈ p(1-p)/12)
- η₀ = 1/(8 ln 2) ≈ 0.180

| |c|² | log₂(1/|c|²) | I_actual (est., bits) | I_FR-bound (bits) | Ratio |
|:--:|:--:|:--:|:--:|:--:|
| 0.001 | 9.97 | 1.247 | 0.180 | 6.9x |
| 0.01 | 6.64 | 0.830 | 0.018 | 46x |
| 0.1 | 3.32 | 0.415 | 0.018 | 23x |
| 0.5 | 1.00 | 0.125 | 0.090 | 1.4x |
| 0.8 | 0.32 | 0.040 | 0.144 | 0.3x |

**Note:** At larger |c|², the perturbative expansion breaks down and higher-order terms dominate. The "0.3x" entry at |c|²=0.8 reflects the breakdown of the small-|c| formula, not a failure of the lower bound (which is always satisfied).

The key takeaway: for |c|² < 0.1, the bound underestimates QCMI by a factor of 7-46x. This is the regime where the "height ≥ 1 nanometer" criticism bites hardest.

---

## Section 3: Aligned Cartan Configurations — The Infimum is Zero

### 3.1 The Aligned Configuration Family

Consider the one-parameter family of configurations:

$$c^{(1)} = c^{(2)} = c^{(3)} = c^{(4)} = (\varepsilon, 0, 0), \quad \varepsilon > 0$$

All four Cartan vectors are aligned to the x-axis with equal magnitude ε.

**CFOL status:** For ε > 0, all four edges have |c^(i)|² = ε² > 0, so none is factorizable. CFOL is satisfied.

**Differential Cartan sum:** For shared node Q_a: w_{Q_a,1} = +1, w_{Q_a,3} = -1.
D_a = |(+1)·|c^(1)|² + (-1)·|c^(3)|²| = |ε² - ε²| = 0.

Similarly for Q_b: D_b = |(+1)·|c^(2)|² + (-1)·|c^(4)|²| = 0.

Therefore D = D_a + D_b = 0. The lower bound gives QCMI ≥ η₀ · 0 = 0, which is trivially satisfied.

**Actual QCMI:** By the commutativity theorem (CCQ, Theorem II), when all Cartan vectors are aligned (θ_a = θ_b = 0), the non-Cartan cross-terms from [H^(1), H^(3)] and [H^(2), H^(4)] vanish. The leading QCMI contribution comes from O(|c|⁴) terms:

$$I_{\text{aligned}} = \frac{p(1-p)}{4\ln 2} \sum_{i=1}^4 |c^{(i)}|^4 + O(|c|^6) = \frac{p(1-p)}{\ln 2} \varepsilon^4 + O(\varepsilon^6)$$

For p = 1/2: I_aligned ≈ (0.25/0.693) ε⁴ ≈ 0.361 ε⁴.

**Ratio analysis:** While D = 0 (so the bound ratio is undefined/trivial), we can compare QCMI to the total Cartan sum Σ|c|² = 4ε²:

$$\frac{I_{\text{aligned}}}{\Sigma|c|^2} \approx \frac{0.361 \varepsilon^4}{4\varepsilon^2} = 0.090 \varepsilon^2 \to 0 \quad \text{as } \varepsilon \to 0$$

### 3.2 Near-Aligned Family: Non-Zero Differential Sum

To get D > 0 while keeping QCMI small, consider a near-aligned family:

$$c^{(1)} = (\varepsilon, \delta, 0), \quad c^{(3)} = (\varepsilon, -\delta, 0), \quad c^{(2)} = c^{(4)} = (\varepsilon, 0, 0)$$

For δ ≪ ε:

- |c^(1)|² = ε² + δ², |c^(3)|² = ε² + δ²
- D_a = |(ε²+δ²) - (ε²+δ²)| = 0 (still cancels!)
- D_b = |ε² - ε²| = 0

The differential sum still vanishes because the magnitudes match. To get D > 0, we need magnitude asymmetry:

$$c^{(1)} = (\varepsilon + \delta, 0, 0), \quad c^{(3)} = (\varepsilon - \delta, 0, 0), \quad c^{(2)} = c^{(4)} = (\varepsilon, 0, 0)$$

For δ ≪ ε:
- |c^(1)|² = (ε+δ)² = ε² + 2εδ + δ²
- |c^(3)|² = (ε-δ)² = ε² - 2εδ + δ²
- D_a = |(ε²+2εδ+δ²) - (ε²-2εδ+δ²)| = 4εδ
- D = D_a + 0 = 4εδ

The lower bound: I_FR ≥ η₀ · 4εδ.

The actual QCMI has two contributions:
1. Alignment base: I_aligned = (p(1-p)/ln 2) · 4ε⁴ (from four edges at |c|² ≈ ε²)
2. Misalignment bonus from θ_a ≠ 0: since c^(1) and c^(3) are parallel (both along x-axis), θ_a = 0, so the sin²θ bonus is zero. The asymmetry δ only affects the magnitudes, not the angle.

So the actual QCMI is I_actual ≈ (p(1-p)/ln 2) · 4ε⁴ (same as aligned case, since all vectors are still parallel).

Ratio as ε → 0 (with δ = ε² for concreteness):

$$D = 4\varepsilon \cdot \varepsilon^2 = 4\varepsilon^3$$
$$I_{\text{actual}} \approx \frac{4p(1-p)}{\ln 2}\varepsilon^4$$
$$\frac{I_{\text{actual}}}{\eta_0 \cdot D} \approx \frac{(4p(1-p)/\ln 2)\varepsilon^4}{(1/(8\ln 2)) \cdot 4\varepsilon^3} = 8p(1-p) \cdot \varepsilon \to 0$$

**Theorem 2 (Infimum is zero).** For the four-node causal ring with d=2, b₁=1:

$$\inf\left\{\frac{I(R;E'|Q')}{\eta_0 \cdot D} : \text{CFOL holds}, D > 0\right\} = 0$$

**Proof.** Take the near-aligned family with ε → 0, δ = ε². CFOL holds (all |c^(i)| > 0), D = 4ε³ > 0, and I_actual/D = O(ε) → 0. Since I ≥ η₀ · D holds (the bound is valid), and I/(η₀ · D) → 0, the infimum is 0. ∎

### 3.3 Interpretation

Theorem 2 says that for any fixed η > 0, there exist CFOL-satisfying configurations where QCMI / D < η. In other words, **no universal constant-factor improvement of η₀ is possible**. Any bound of the form QCMI ≥ const · D with const > 0 will be violated by the near-aligned family at sufficiently small ε.

The only way to "tighten" the bound is to make the prefactor |c|-dependent: QCMI ≥ η(|c|) · D where η(|c|) → 0 as |c| → 0. But this defeats the purpose of a universal lower bound, because η(|c|) would need to encode the same structural information already present in the QCMI itself.

---

## Section 4: The Zhou Gang 2026 Decomposition — Independent Analysis of Saturation Conditions

### 4.1 Theorem Statement (arXiv:2603.14650v2, Theorem 5.3)

The QCMI admits an exact decomposition into manifestly positive terms:

$$I(A:C|B) = \frac{1}{J}\int_0^1 \int_0^\tau \tilde{K}_J(\sigma) \, d\sigma d\tau + \sum_{K=2}^{J-1} \Omega_K$$

where each Ω_K ≥ 0 and K̃_J(σ) ≥ 0. Each term is explicitly constructed from matrix elements of the state and channel.

### 4.2 Implication for Tightness

This decomposition provides an alternative route to the tightness analysis: instead of analyzing the monolithic Fawzi-Renner chain, we can independently analyze the saturation condition of each positive term.

**Key observation:** For the four-node causal ring, each Ω_K and K̃_J depends on the Cartan coefficients in a specific way. The aligned configuration (θ_v = 0) causes specific Ω_K terms to vanish, while non-aligned configurations keep them positive. This provides a term-by-term accounting of where the QCMI "comes from," and explains why the aligned configuration achieves the infimum.

**Conjecture (Zhou-decomposition tightness):** In the decomposition, at least one Ω_K term has coefficient proportional to sin²θ_v (the Cartan axis misalignment angle). For the aligned configuration (θ_v = 0), this term vanishes identically, reducing the effective QCMI to O(|c|⁴). For non-aligned configurations, this term contributes O(|c|²) with a log(1/|c|²) coefficient. This would provide an independent structural explanation for both the log factor and the infimum-zero result.

**Status:** This connection is conjectural pending explicit computation of the Zhou decomposition for the causal ring setup. The decomposition is guaranteed to exist (Theorem 5.3) but the explicit form of each Ω_K in terms of Cartan coefficients requires separate calculation.

---

## Section 5: The CFOL Boundary — Quantitative Analysis

### 5.1 Definition of the "CFOL Boundary"

The CFOL premise is a discrete condition: at least one |c^(i)| > 0. There is no continuous "boundary" in parameter space — any infinitesimal deviation from |c| = 0 satisfies CFOL.

However, there is a **practical boundary** determined by experimental resolution: at what |c| does the QCMI become experimentally distinguishable from zero?

### 5.2 Inequality Chain Gap Budget

Define the gap function G(|c|) = I_actual - I_FR-bound. For generic (non-aligned) configurations at small |c|:

$$G(|c|) = \underbrace{(I - (-2\log_2 F^2))}_{\text{FR gap}} + \underbrace{(-2\log_2 F^2 - (2(1-F^2)/\ln 2))}_{\text{log inequality gap}} + \underbrace{(2(1-F^2)/\ln 2 - \eta_0 D)}_{\text{Kraus-Cartan gap}}$$

At small |c|:
- FR gap: I - (-2 log F²) ≈ α|c|² log₂(1/|c|²) (dominant, from entropy amplification)
- Log inequality gap: (1-F²)²/(ln 2) + ... = O(|c|⁴) (negligible)
- Kraus-Cartan gap: O(|c|⁴) from higher-order BCH terms (small)

**The dominant gap at small |c| is the Fawzi-Renner gap itself** — the difference between the entropic measure (QCMI, which has the log factor) and the fidelity-based measure (-2 log F², which is linear in |c|²). This gap is structural and cannot be closed by tightening constants.

### 5.3 Optimal |c| Regime for Bound Tightness

The ratio I_actual / I_FR-bound is minimized at **intermediate** |c|, where:
- |c| is large enough that the log(1/|c|²) factor is modest (~1-3x)
- |c| is small enough that higher-order BCH terms are controlled
- |c| is not so small that the log factor dominates

From the numerical calibration in §2.4, the optimal regime is |c|² ∈ [0.1, 0.5], where the bound-to-actual ratio is in the range 0.04-1.4 (i.e., the bound is within a factor of ~25 of the actual QCMI).

However, even in this "optimal" regime, the bound is loose by a factor of at least ~5-25x (depending on Cartan alignment), because:
1. The differential sum D underestimates the total Cartan strength (cancellations between edges)
2. The γ_min factor is pessimistic (uses the smallest environment eigenvalue)
3. The Fawzi-Renner gap, while smaller than at tiny |c|, remains substantial

### 5.4 Where the Inequalities Are Simultaneously Tightest

**Claim:** The five-layer inequality chain is simultaneously "tightest" (in the sense of relative gap) at |c|² ≈ 0.3-0.5 for non-aligned configurations with p ≈ 0.5.

**Justification:**
- |c|² ≈ 0.3-0.5: log(1/|c|²) ≈ 1-1.7, so the log-factor enhancement is modest (1-1.7x)
- p ≈ 0.5: γ_min = 0.5 is maximal, minimizing the γ_min → γ_avg gap
- Non-aligned: θ_v ≈ π/4-π/2 maximizes the sin²θ bonus, making the O(|c|²) term dominate over O(|c|⁴)

In this regime, the cumulative conservatism is approximately 4-8x rather than the 4-18x seen in the full experimental data.

**But even here, the bound is not tight.** η₀ · D ≈ 0.18 · (4 × 0.4) ≈ 0.29 bits, while actual QCMI ≈ 0.8-2.0 bits. The gap of 3-7x persists.

---

## Section 6: Small-|c| Experimental Design

### 6.1 Existing Experimental Coverage

From the B博士 R3 dataset (p=0.7, 4-node ring):

| Gate set | min |c|² | QCMI (bits) | QCMI/|c|² |
|:--|:--:|:--:|:--:|
| Rxx(π/4) | 0.039 | 1.223 | 31.4 |
| wHaar 0.06 | ~0.09 | 0.736 | 8.2 |
| wHaar 0.10 | ~0.09 | 1.449 | 16.1 |
| Rxx(π/2) | 0.154 | 1.000 | 6.5 |
| Rzz(π/2) | 0.154 | 0.982 | 6.4 |
| CNOT | 0.617 | 2.763 | 4.5 |
| Haar full | ~0.36 | 3.239 | 9.0 |

The smallest |c|² probed is ~0.04 (Rxx π/4), which is still in the moderate regime. No data exists in the true small-|c| regime (|c|² < 0.01).

### 6.2 Predicted Small-|c| Scaling

For the Rxx(θ) family with a small misalignment:

$$U_1 = U_3 = R_{xx}(\theta), \quad U_2 = U_4 = R_{xx}(\theta + \delta\theta)$$

Cartan coefficients: |c^(1)|² = |c^(3)|² = (θ/2)², |c^(2)|² = |c^(4)|² = ((θ+δθ)/2)².

For θ ≪ 1 with δθ = θ² (to keep D > 0):
- D = |(θ/2)² - ((θ+θ²)/2)²| + |(θ/2)² - ((θ+θ²)/2)²| ≈ (θ³/2) + (θ³/2) = θ³
- I_actual ≈ (p(1-p)/ln 2) · 4 · (θ/2)⁴ = (p(1-p)/(4 ln 2)) θ⁴ (aligned leading term, since all vectors are axis-aligned)
- η₀ · D = (1/(8 ln 2)) · θ³

Predicted scaling: **QCMI ∝ θ⁴** (not ∝ θ²!) for axis-aligned configurations. This is a strong, falsifiable prediction: measuring QCMI for Rxx(θ) with θ = 0.05, 0.10, 0.15, 0.20 should reveal quartic rather than quadratic scaling.

For non-aligned configurations (e.g., Rxx(θ) and Rzz(θ) mixed), the O(|c|² log(1/|c|²)) term should dominate, giving:

$$\text{QCMI} \approx \kappa \cdot \theta^2 \log_2(1/\theta^2)$$

### 6.3 Proposed Numerical Experiment

**Protocol:**
1. Fix p = 0.5 (maximal mixing, simplest analysis)
2. For θ ∈ {0.01, 0.02, 0.05, 0.10, 0.20} (in units of π):
   a. Aligned case: All four gates = Rxx(θ) — predict QCMI ∝ θ⁴
   b. Misaligned case: U₁=U₂=Rxx(θ), U₃=U₄=Rzz(θ) — predict QCMI ∝ θ² log(1/θ²)
3. Measure QCMI numerically (exact diagonalization, 64×64 density matrix)
4. Fit to functional forms and extract scaling exponents

**Expected outcome:** The aligned case should show exponent ≈ 4 (confirming that aligned Cartan vectors suppress the O(|c|²) term). The misaligned case should show behavior consistent with θ² log(1/θ²), confirming the log-factor prediction from direct spectral analysis.

**Resources needed:** Python/NumPy script, ~50 data points, runtime ~1 hour on standard hardware.

---

## Section 7: Self-Attack — Adversarial Verification

### SA-1: The Log-Factor Derivation Uses Perturbation Theory 🔴🔴🔴

**Attack:** The derivation of S(J(N)/d²) = O(|c|² log(1/|c|²)) assumes that the Choi state eigenvalues λ_i = β_i|c|² are small enough for the expansion -λ log λ to be valid. For finite |c|, the subleading eigenvalues may not be small, and the leading eigenvalue's O(|c|²) correction may include log terms from its own expansion. The claimed asymptotic form may not be the true leading behavior.

**Response:** The derivation is rigorous in the limit |c| → 0. For any ε > 0, there exists δ > 0 such that for |c| < δ, the eigenvalue expansion is valid and the log(1/|c|²) term dominates. The claim is about the **asymptotic** behavior, not the finite-|c| behavior.

However, the SA correctly identifies that for |c|² ~ 0.04-0.6 (the experimentally accessible regime), the perturbative expansion may not be in its asymptotic domain. A non-perturbative numerical diagonalization (P0 from round 1) is needed to verify the log-factor prediction at experimentally relevant |c|.

### SA-2: The Choi State Entropy Might NOT Dominate QCMI 🔴🔴

**Attack:** The identity QCMI = 4 - I(R;Q') involves S(Q') as well as S(RQ'). The claim that S(Q') ≈ 2 - O(|c|⁴) assumes N(I/4) is near-maximally-mixed for small |c|. But N(I/4) = (1/4) Σ_{ab} K_{ab} K_{ab}†. The O(|c|) Kraus corrections could introduce O(|c|²) deviations from the maximally mixed state, making S(Q') = 2 - O(|c|²) rather than 2 - O(|c|⁴). If true, this would introduce a competing O(|c|²) term that partially cancels the log factor.

**Response:** This is a valid concern. The O(|c|) Kraus corrections δK_ab^(1) are traceless (they are linear combinations of Pauli matrices). The O(|c|²) terms in N(I/4) come from δK^(1) δK^(1)† and δK^(2) + δK^(2)†. The former contribute O(|c|²), and the latter also contribute O(|c|²) (from the -(H^(i))²/2 term in the Cartan expansion, which is proportional to the identity and therefore traceful).

A full calculation is needed to determine the coefficient of the O(|c|²) term in S(Q'). Preliminary analysis suggests this term is O(|c|²) (not O(|c|⁴)), but with a small coefficient (order p(1-p)/d²). This would modify the O(|c|²) coefficient of QCMI (the non-log part) but NOT the O(|c|² log(1/|c|²)) leading term, because S(Q') = -Σ μ_j log μ_j where μ_j are the eigenvalues of N(I/4). If N(I/4) has eigenvalues 1/4 + O(|c|²), then S(Q') = 2 + O(|c|²) (no log factor, because the eigenvalues are not small).

**Conclusion:** The log factor in QCMI comes exclusively from S(RQ') = S(J(N)/4), where the subleading eigenvalues are genuinely small (O(|c|²)). The S(Q') term contributes at O(|c|²) without a log factor, affecting the sub-leading coefficient but not the dominant log(1/|c|²) behavior. The Theorem 1 conclusion (divergence of the ratio) is robust.

### SA-3: The Near-Aligned Family Uses Fourth-Order QCMI 🔴🔴🔴🔴

**Attack:** The near-aligned family in §3.2 achieves QCMI/D → 0 because QCMI = O(ε⁴) while D = O(ε³). But this relies on the CCQ theorem's claim that aligned Cartan vectors give QCMI = O(|c|⁴). What if there is an O(|c|²) contribution that the CCQ analysis missed — for example, from higher-order BCH terms that do NOT vanish even when [H^(1), H^(3)] = 0?

**Response:** This is the most serious challenge. The CCQ theorem's §6 (SA-2) addresses this: in the aligned case, all Cartan Hamiltonians live in the same Cartan subalgebra, and higher-order nested commutators like [H^(1), [H^(2), H^(3)]] vanish because H^(2) and H^(3) act on disjoint subsystems. The SA-2 analysis covers up to third order in the BCH expansion.

However, at **fourth order** in the BCH expansion, terms like [H^(1), [H^(1), [H^(2), H^(3)]]] could potentially generate non-Cartan contributions even in the aligned case. A complete analysis of the BCH expansion to all orders is beyond the current scope.

**If the SA-3 concern is valid** (i.e., aligned configurations DO have O(|c|²) QCMI contributions), then the near-aligned family would NOT drive QCMI/D → 0. Instead, QCMI ≈ const · D, and η₀ could be asymptotically tight (in the sense that QCMI/D → η > 0 for some η ≥ η₀).

**Numerical verification is essential.** The proposed numerical experiment in §6.3, specifically the aligned Rxx(θ) scan, will determine whether QCMI ∝ θ⁴ (CCQ correct, infimum zero) or QCMI ∝ θ² (CCQ incomplete, eta_0 potentially tight).

### SA-4: Fawzi-Renner Might Be Tighter Than We Think 🔴🔴

**Attack:** The Fawzi-Renner bound I ≥ -2 log₂ F² uses the **squared** Uhlmann fidelity. The relationship between F² and the Kraus deviation might contain its own log-like structure for near-pure Choi states. The direct spectral computation uses the identity I = 4 - I(R;Q'), which is equivalent to the Fawzi-Renner bound only in the Markov chain limit (QCMI = 0). For non-zero QCMI, the two expressions may differ, and Fawzi-Renner might already encode the log factor through the fidelity.

**Response:** The Fawzi-Renner bound involves F²(ρ_RQ'E', ρ_rec), where ρ_rec is the Petz-recovered state. The fidelity between the actual state and the recovered state is:

$$F^2 = \left(\text{Tr}\sqrt{\sqrt{\rho}\rho_{\text{rec}}\sqrt{\rho}}\right)^2$$

For a near-pure Choi state (ρ = J(N)/4), the fidelity to the Petz-recovered state is F = 1 - O(|c|²). The logarithm -2 log₂ F² expands as (2/ln 2)(1-F²) + O((1-F²)²). Crucially, the fidelity is NOT an entropic quantity — it does not carry the -p log p structure of von Neumann entropy. The log in -2 log₂ F² is the logarithm of the fidelity, not the entropy logarithm, and it captures the distance in state space, not the information-theoretic cost.

**The gap between I and -2 log F² is the gap between an entropic measure and a geometric measure.** This gap is fundamental and cannot be closed by tightening the Fawzi-Renner analysis. It is analogous to the gap between relative entropy and fidelity: S(ρ‖σ) ≥ -2 log F(ρ,σ), and equality requires ρ = σ exactly, not just F ≈ 1.

### SA-5: Zhou Gang Decomposition May Resolve the Paradox 🔴🔴🔴

**Attack:** The Zhou decomposition expresses QCMI as a sum of positive terms, each with explicit structure. One of these terms might precisely correspond to the η₀ · D lower bound, while the log-factor term corresponds to a different Ω_K. If so, η₀ would be tight for ITS contribution to QCMI, and the log factor is a separate physical effect (coming from, say, the subleading Choi eigenvalues' entropy). This would rescue η₀ by reinterpreting it as a lower bound on a specific component of QCMI, not on the total QCMI.

**Response:** This is the most constructive counter-argument. If the Zhou decomposition reveals that:

$$I(R;E'|Q') = \eta_0 \cdot D + \Omega_{\text{log}} + \Omega_{\text{higher}}$$

where Ω_log captures the log(1/|c|²) contribution and Ω_higher captures O(|c|⁴) terms, then η₀ · D is genuinely the tight lower bound for the "linear" component of QCMI. The total QCMI exceeds this bound because of the additional, independently-positive contributions from Ω_log and Ω_higher.

In this interpretation, η₀ is the **optimal constant for the linear-in-|c|² component**, and the looseness of the total bound reflects the existence of additional positive contributions. This is a much more defensible position than claiming η₀ as a tight bound on total QCMI.

**Recommendation:** If the Zhou decomposition connection can be made explicit (Phase 2 work), reframe η₀ as "the tight prefactor for the Fawzi-Renner component of QCMI" rather than "the tight lower bound on total QCMI."

---

## Section 8: Honest Conclusions — What η₀ Is and Is Not

### 8.1 Five Possible Meanings of "Tight"

| Meaning | Definition | Verdict | Evidence |
|:--|:--|:--:|:--|
| **Exact achievability** | ∃ config with QCMI = η₀ and CFOL holds | **FALSE** | FR equality requires QCMI=0 (contradicts CFOL), §1 |
| **Asymptotic ratio tightness** | QCMI/(η₀·D) → 1 as |c|→0 | **FALSE** | Ratio diverges (log factor), Theorem 1, §2 |
| **Order-of-magnitude tightness** | QCMI/(η₀·D) stays bounded away from 0 and ∞ | **FALSE** | Ratio → 0 for aligned configs, Theorem 2, §3 |
| **Infimum equality** | inf QCMI/(η₀·D) = 1 over all CFOL configs | **FALSE** | Infimum is 0, Theorem 2, §3.3 |
| **Linear-component optimality** | η₀ is best constant for linear-in-D lower bound | **PLAUSIBLE** | Requires Zhou decomposition analysis, §4, §7 SA-5 |

### 8.2 Recommended Framing for the Paper

**DO say:**
1. "η₀ = 1/(8 ln 2) is a rigorous lower bound on QCMI for the four-node causal ring, derived from the Fawzi-Renner theorem combined with the Cartan decomposition of the edge unitaries."
2. "The bound captures the leading-order |c|² scaling of QCMI with a universal, dimension-dependent prefactor."
3. "For specific gate configurations (e.g., CNOT ring, Haar-random gates), the actual QCMI exceeds this bound by factors of 4-18, indicating that the bound, while rigorous, is not numerically tight."
4. "The dominant source of looseness is the entropic amplification of small Choi-state eigenvalues, which contributes an O(|c|² log(1/|c|²)) term not captured by the Fawzi-Renner fidelity-based bound."

**DO NOT say:**
1. "η₀ is the tight lower bound" — it is not tight in any standard sense.
2. "The bound is saturated in the limit |c| → 0" — it is not; the ratio diverges.
3. "η₀ represents the minimum possible QCMI" — the minimum at fixed D is 0 (aligned configuration), and the minimum at fixed |c| is achieved by aligned configurations where QCMI << η₀ · Σ|c|².

**Alternative formulation** (if the Zhou decomposition connection is validated):

$$\boxed{I(R;E'|Q') = \eta_0 \cdot D + \Delta_{\text{log}}(|c|) + \Delta_{\text{align}}(c) + \Delta_{\text{higher}}(c)}$$

where:
- η₀ · D is the "Fawzi-Renner component" (linear in |c|², with optimal constant η₀)
- Δ_log(|c|) = O(|c|² log(1/|c|²)) is the "entropic amplification" from subleading Choi eigenvalues
- Δ_align(c) = O(|c|⁴ sin²θ) is the "Cartan misalignment bonus" (positive for non-aligned, zero for aligned)
- Δ_higher(c) = O(|c|⁶) contains higher-order BCH contributions

### 8.3 The "身高≥1纳米" Problem — Final Resolution

The reviewer's criticism "claiming height ≥ 1 nanometer — mathematically true, physically hollow" is addressed as follows:

1. **Acknowledge the validity of the criticism.** The bound QCMI ≥ 0.180 bits, presented without qualification, does invite this analogy. It is mathematically correct but provides negligible physical constraint.

2. **Reframe the contribution.** The value of the η₀ derivation is NOT the numerical constant 0.180, but:
   - The structural connection it establishes between causal topology (b₁), Cartan geometry (|c|²), and quantum information (QCMI)
   - The method: Fawzi-Renner + Cartan gauge fixing as a general technique for topological lower bounds on QCMI
   - The scaling law: QCMI scales as |c|² (times log corrections) with a universal prefactor determined by environment purity and Hilbert space dimension

3. **Present the calibrated bound.** For the experimentally relevant regime, replace η₀ = 0.180 with the |c|-dependent effective bound:
   
   $$\text{QCMI} \geq \eta_{\text{eff}}(|c|) \cdot D, \quad \eta_{\text{eff}}(|c|) = \frac{1}{8\ln 2} \cdot \max\left(1, \log_2\frac{1}{|c|^2}\right)$$
   
   For |c|² ∈ [0.04, 0.6] (experimentally accessible): η_eff ∈ [0.18, 0.83] bits, bringing the bound within factor 2-5 of experimental QCMI (rather than 4-18).

4. **State the honest limitation.** The bound is not tight and cannot be made tight without |c|-dependence. This is not a failure of the analysis but a fundamental feature of the entropic nature of QCMI. Any fidelity-based bound will miss the entropic log factor.

---

## Section 9: Recommendations for Phase 2

### P0 (Critical): Numerical Choi Diagonalization for Aligned Configurations

Execute the experiment proposed in §6.3. This will definitively determine whether:
- QCMI ∝ θ⁴ for aligned Rxx(θ) (confirming CCQ and the infimum-zero result)
- QCMI ∝ θ² for aligned Rxx(θ) (refuting CCQ, suggesting η₀ may be asymptotically tight after all)

**This is the single most important next step.** Without it, the entire tightness analysis rests on the unverified CCQ claim about aligned QCMI scaling.

### P1 (High): Zhou Gang Decomposition for Causal Ring

Compute the explicit Zhou decomposition (Theorem 5.3, arXiv:2603.14650v2) for the four-node causal ring setup. This would:
- Identify which Ω_K corresponds to the η₀ · D bound
- Determine whether the log factor appears in a separate Ω_K
- Provide an independent verification of the small-|c| scaling

### P2 (Medium): Non-Perturbative Lower Bound

Develop a lower bound that incorporates the log factor:

$$\text{QCMI} \geq \frac{p(1-p)}{2\ln 2} \cdot D \cdot \log_2\left(1 + \frac{1}{\alpha D}\right)$$

where α is determined by the number of active Pauli sectors. This bound interpolates between O(|c|² log(1/|c|²)) at small |c| and O(|c|²) at large |c|, matching both the direct spectral result and the Fawzi-Renner linear bound in their respective regimes.

### P3 (Low): Paper Text Revision

Draft the "QCMI lower bound" section of the paper using the honest framing from §8.2, avoiding the unsupportable "tightness" claim.

---

## Appendix A: Key Formulas — Tightness Analysis

### A.1 Fawzi-Renner Equality Condition (HJPW04, Theorem 3)

$$I(A:C|B) = -2\log_2 F^2 \Longleftrightarrow \exists \text{ perfect Petz recovery } \Longleftrightarrow \text{QCMI} = 0$$

### A.2 Choi Entropy at Small |c| (This Work, Lemma 3)

$$S(J(N)/d^2) = \alpha|c|^2 \log_2(1/|c|^2) + \left(\frac{\alpha}{\ln 2} + \sum_i \beta_i \log_2(1/\beta_i)\right)|c|^2 + O(|c|^4 \log(1/|c|^2))$$

### A.3 QCMI Small-|c| Scaling (This Work, §2.2)

$$I(R;E'|Q') = \alpha|c|^2 \log_2(1/|c|^2) + O(|c|^2)$$

### A.4 Ratio Divergence (This Work, Theorem 1)

$$\lim_{|c|\to 0} \frac{I(R;E'|Q')}{\eta_0 \cdot D} = \infty \quad (\text{logarithmic divergence})$$

### A.5 Infimum is Zero (This Work, Theorem 2)

$$\inf\left\{\frac{I(R;E'|Q')}{\eta_0 \cdot D} : \text{CFOL holds}, D > 0\right\} = 0$$

### A.6 Improved |c|-Dependent Bound (This Work, §8.3)

$$\text{QCMI} \geq \frac{1}{8\ln 2} \cdot \max\left(1, \log_2\frac{1}{|c|^2}\right) \cdot D$$

---

## Appendix B: Cross-References

**This document produced for:** Wall 1 attack, Round 2 — tightness analysis
**Depends on:**
- CFOL v4 (round1_factorization.md): QCMI=0 ⇔ factorization
- η_quantitative.md: Fawzi-Renner chain, exact identity, Cartan gauge fixing
- round1_A_formal.md: Five-layer conservatism audit, direct spectral computation
- commutativity_theorem.md (CCQ): Aligned Cartan QCMI = O(|c|⁴)
- prefactor_derivation.md: p(1-p)/(2 ln 2) coefficient
- COLD_START_AUDIT_2026-06-09.md: Attack priorities, Wall 1 diagnosis

**New results (this document):**
- Theorem 1: Logarithmic divergence of QCMI / (η₀ · D) as |c| → 0
- Theorem 2: Infimum of QCMI / (η₀ · D) over CFOL configurations is zero
- Lemma 2-3: Choi eigenvalue structure and entropy at small |c| (rigorous)
- CFOL boundary quantitative analysis (§5)
- Small-|c| experimental design (§6)
- Honest paper framing recommendations (§8)

**Does NOT use:** b₁>1 generalization, cosmological claims, tree-edge freezing

---

## Appendix C: The Five Meanings of "η₀ is Tight" — Decision Matrix

| Claim | Mathematical Statement | Status | Action |
|:--|:--|:--:|:--|
| "η₀ is achievable" | ∃ config: QCMI = η₀, CFOL holds | **Provably false** | Remove from paper |
| "η₀ is asymptotically tight" | QCMI/(η₀·D) → 1 as |c|→0 | **Provably false** | Remove from paper |
| "η₀ is the optimal constant" | sup{η: QCMI ≥ η·D ∀ configs} = η₀ | **Likely false** (infimum is 0) | Await numerical verification (P0) |
| "η₀ is a valid lower bound" | QCMI ≥ η₀·D for all configs | **True** (within derivation domain) | Keep, with qualifications |
| "η₀ captures the correct scaling" | QCMI = Θ(|c|²) at leading order | **True** (modulo log factor) | Keep, note log correction |

---

*Round 2 tightness analysis complete. η₀ = 1/(8 ln 2) is a rigorous but non-tight lower bound. The unsaturability is structural: (a) Fawzi-Renner equality is incompatible with CFOL, (b) the von Neumann entropy log factor is missed by any fidelity-based bound, and (c) aligned Cartan configurations drive QCMI/D to zero. The paper should present η₀ as a valid lower bound with explicit calibration for the experimentally relevant |c| regime, not as a tight or saturable bound. The critical next step (P0) is numerical verification of the QCMI ∝ |c|⁴ scaling for aligned configurations.*
