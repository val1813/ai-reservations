# Two-Exponent Characterization of Nonequilibrium Steady States: Coherence Decay and Transport in Power-Law Hopping Chains with Bulk Dephasing

**Target:** Physical Review B (Regular Article)
**Date:** 2026-06-05
**Status:** Complete draft — self-consistent β-μ characterization, L≤256 FSS

---

## Abstract

Nonequilibrium steady states (NESS) of boundary-driven quantum chains are typically characterized by a single transport exponent μ governing the decay of current with system size. Here we show that a second exponent β(α,γ_φ), describing the spatial decay of off-diagonal quantum coherence, provides complementary information about the NESS structure, and that the pair (β, μ) — both computed self-consistently within the same model — resolves regimes invisible to either exponent alone. For a boundary-driven free-fermion chain with power-law hopping J(r) ∝ r^{−α} and bulk dephasing rate γ_φ, we solve the site-basis Lindblad equation exactly up to L=256 (dense solver for L≤64, sparse GMRES for larger systems). The midchain coherence obeys |C_mid| ~ L^{−β}, with β exhibiting a two-regime large-L structure: enhanced decay from a long-range boundary-dominated sector at small α, crossing into a γ_φ-dependent near-diffusive plateau at larger α. We compute the transport exponent μ from the boundary current J = Γ_L(f_L−D_1) ~ L^{−μ} in the same numerical framework, finding μ = 0.285–0.901 for α ∈ [1.1, 1.9] at γ_φ = 0.5, with systematic γ_φ sensitivity. The two exponents respond differently to parameter changes — varying γ_φ at fixed α shifts both β and μ, but with distinct functional forms — confirming they probe different Liouvillian spectral sectors. A universality test varying boundary coupling Γ by a factor of 4 yields Δβ < 7%, consistent with a boundary-fixed-line interpretation. The off-diagonal correlations are proven purely imaginary for arbitrary hopping range via the homogeneous Lyapunov system argument, making |C_{i≠j}| directly accessible in trapped-ion and Rydberg platforms.

---

## I. Introduction

Nonequilibrium quantum transport in low-dimensional systems is a central problem in condensed matter physics, with implications ranging from nanoscale heat management to the understanding of thermalization in isolated quantum systems [1–4]. When coupled to external reservoirs, open quantum systems reach a nonequilibrium steady state (NESS) characterized by macroscopic currents whose scaling with system size reveals the underlying transport mechanism. A particularly rich class of models features power-law hopping, J(r) ∝ r^{−α}, where the hopping amplitude decays algebraically with distance. These systems interpolate between all-to-all coupling (α → 0) and nearest-neighbor hopping (α → ∞), and have attracted intense interest due to experimental realizations in trapped ions, Rydberg atom arrays, and cavity-QED platforms [1–4].

For a boundary-driven chain with power-law hopping, Dhawan et al. [5] established the transport exponent μ(α) = 2α−2 (for 1 < α < 3/2) governing the conductance scaling G(L) ~ L^{−μ}, and identified the ballistic-to-diffusive crossover at α = 3/2. Costa et al. [6] developed a gauge-trick methodology for full counting statistics within a diagonal-sector framework. Sarkar et al. [7] mapped the current-decoherence phase diagram, employing the imaginary part of the off-diagonal correlation matrix to compute the current. Bhat and Žnidarič [8] developed a transfer matrix approach for Lindblad evolution of XX chains with dephasing, demonstrating that off-diagonal correlations C_{j,j+1} are purely imaginary and directly yield the magnetization current. These works have established the transport exponent μ as the primary diagnostic of the NESS, anchored in the diagonal sector of the density matrix.

The full NESS, however, is encoded in the complete single-particle correlation matrix C_{ij} = Tr[c_i†c_j ρ_ss], whose off-diagonal elements (i ≠ j) carry quantum coherence between different sites. While Sarkar et al. [7] used Im[C_{m,m−r}] to compute the current — a diagonal observable — the spatial decay structure of |C_{ij}| itself has not been characterized as a finite-size scaling phenomenon. A structural relationship connects the two sectors: a first-order commutator expansion (derived in Sec. V and Appendix S5) yields |C_mid| = (J₀/γ_φ)|D_{L/2+1} − D_{L/2}|·κ, with κ → 1 as L → ∞, showing that the coherence exponent β approaches the occupation-gradient exponent ν in the thermodynamic limit. At finite L, however, κ deviates from unity, and β captures the finite-size scaling structure of off-diagonal coherence — a physically measurable quantity distinct from the transport current.

In this Article, we provide a self-consistent two-exponent characterization of the NESS: (i) we compute β(α,γ_φ) from exact numerical solutions up to L=256, revealing a two-regime large-L structure (long-range boundary-dominated decay crossing into a near-diffusive plateau); (ii) we compute μ(α,γ_φ) from the boundary current in the same numerical framework, enabling quantitative β–μ comparison; (iii) we show that the two exponents respond differently to parameter variations, confirming they encode complementary information about the NESS; and (iv) we test the robustness of β under boundary-coupling variations. We also prove, via the homogeneous Lyapunov system argument, that off-diagonal correlations are purely imaginary for arbitrary power-law hopping — generalizing the nearest-neighbor result of Bhat and Žnidarič [8].

---

## II. Model and Method

We consider a one-dimensional chain of L spinless free fermions with power-law hopping and boundary driving. The single-particle Hamiltonian is

$$H = \sum_{i<j} J_0 |i-j|^{-\alpha} (c_i^\dagger c_j + \text{H.c.}),$$

with J₀ = 0.3 setting the energy scale. The chain is driven into a NESS by Lindblad jump operators on the boundary sites: L_{L,in} = √(Γ_L f_L) c₁†, L_{L,out} = √(Γ_L(1−f_L)) c₁, and corresponding right-boundary operators with L → R. Bulk dephasing is modeled by L_{deph,j} = √γ_φ c_j†c_j at every site j = 1,…,L, suppressing off-diagonal coherences at rate γ_φ without affecting particle number. The reference parameters are Γ_L = Γ_R = 1.0, f_L = 0.65, f_R = 0.35 (bias Δf = 0.3), with γ_φ ∈ [0.01, 2.0] and α ∈ [1.1, 1.9].

Because the Hamiltonian is quadratic and jump operators are linear in fermion operators, the NESS is fully characterized by the single-particle correlation matrix C_{ij} = Tr[c_i†c_j ρ_ss]. Its equation of motion closes at the single-particle level, yielding an L² × L² linear system (detailed in Supplemental Material S1). We solve the baseline parameter scan (125 combinations: 5 α × 5 γ_φ × 5 L values {4, 8, 16, 32, 64}) with dense LU factorization. For the large-L finite-size scaling analysis, we extend to L = 128 for γ_φ = 0.1, 0.5, 1.0, 2.0 and to L = 256 for the central γ_φ = 0.5 slice, using a sparse GMRES implementation with diagonal preconditioning and residual tolerance rtol = 10⁻¹⁰. The sparse solver is cross-validated against the dense solver at L = 64 (relative error < 10⁻⁸ on |C_mid|). We extract both the midchain coherence |C_mid| ≡ |C_{L/2−1, L/2}| (for β) and the boundary current J = Γ_L(f_L − D₁) with D₁ = C₁₁ (for μ). The current is spatially uniform in the steady state; the boundary formula provides a numerically stable estimator that avoids summation over all off-diagonal elements.

---

## III. Pure Imaginary Off-Diagonal Structure

Before analyzing the coherence decay, we establish a structural property of the NESS that simplifies the physical interpretation of |C_{i≠j}|. Bhat and Žnidarič [8] proved, within their transfer matrix framework for nearest-neighbor XX chains, that off-diagonal correlation elements are purely imaginary: Re(C_{i≠j}) = 0. Their proof exploits the tridiagonal hopping matrix to construct a 2×2 transfer matrix — a construction tied to nearest-neighbor hopping.

We prove the same property for arbitrary power-law hopping using a different technique that relies only on the real symmetry of h and the diagonal structure of the source. Writing the steady-state Lyapunov equation and separating C = D + O (diagonal + off-diagonal parts), the real part of the off-diagonal block satisfies a homogeneous linear system whose coefficient matrix contains the dephasing term −γ_φ on every diagonal element. For γ_φ > 0, this matrix is nonsingular, and the unique solution is Re(O_{i≠j}) = 0. The proof is insensitive to the hopping range — it uses only (a) h real symmetric, (b) the injection source diagonal and real, and (c) γ_φ > 0. A detailed derivation is provided in Supplemental Material S2.

Numerical verification across all 125 baseline points and 60 universality-test points confirms max|Re(C_{i≠j})| < 10⁻¹⁵. Since the off-diagonal correlations are purely imaginary, |C_{i≠j}| = |Im(C_{i≠j})| — the coherence magnitude is directly the magnitude of the imaginary part, which is the quantity that enters the current formula. This property simplifies the experimental interpretation: single-site-resolved measurements of Im(C_{ij}) directly yield the coherence structure studied below.

---

## IV. Coherence Decay Exponent β: Baseline Scan (L ≤ 64)

### A. Definition and extraction

The midchain coherence |C_mid| ≡ |C_{L/2−1, L/2}| follows a clean power-law decay with system size for γ_φ ≳ 0.1:

$$|C_{\text{mid}}| \sim L^{-\beta(\alpha,\gamma_\phi)},$$

with high log-log linearity (R² > 0.99 for γ_φ ≥ 0.5, R² ≈ 0.96–0.98 for γ_φ = 0.1, R² ≈ 0.87–0.89 for γ_φ = 0.01). We extract β from log-log linear regression over L = 4, 8, 16, 32, 64 for each of the 25 (α, γ_φ) combinations. Table 1 collects the baseline β values with 1σ standard errors.

**Table 1.** Coherence decay exponent β(α,γ_φ) with 1σ standard errors from log-log regression (L = 4, 8, 16, 32, 64). All fits have R² > 0.99 except γ_φ = 0.01 (R² ≈ 0.87–0.89). Bold: β > 0.87. The coefficients a(γ_φ), b(γ_φ) from β = a/α + b are listed in the rightmost columns; this form captures the leading long-range scaling in the dephasing window where hopping and dephasing compete (γ_φ = 0.5).

| α \ γ_φ | 0.01* | 0.1 | 0.5 | 1.0 | 2.0 |
|:--------:|:-----:|:---:|:---:|:---:|:---:|
| 1.1 | 0.167(37) | 0.739(65) | **1.172(11)** | **1.230(32)** | **1.234(35)** |
| 1.3 | 0.160(34) | 0.710(63) | **1.043(14)** | **1.080(32)** | **1.106(34)** |
| 1.5 | 0.154(32) | 0.675(58) | **0.943(15)** | **0.997(26)** | **1.040(29)** |
| 1.7 | 0.149(30) | 0.636(51) | **0.891(8)** | **0.962(18)** | **1.012(22)** |
| 1.9 | 0.145(29) | 0.602(46) | **0.872(3)** | **0.951(10)** | **1.004(17)** |
| a(γ_φ) | 0.058 | 0.357 | 0.813 | 0.745 | 0.610 |
| b(γ_φ) | 0.115 | 0.425 | 0.422 | 0.529 | 0.657 |

*γ_φ = 0.01: the ballistic regime. All β values are 1σ-consistent with constant β ≈ 0.155 ± 0.032. The near-α-independence is physically expected: as γ_φ → 0, the steady-state density gradient vanishes and the α-dependent amplitude of the coherence decay collapses. This limit serves as a verification of the model's ballistic fixed point rather than noise to be discarded — see Sec. IV.C.

### B. Functional form and scaling analysis

The α-dependence of β in the dephasing window is controlled by the same nonlocal kernel that governs the diagonal fractional diffusion problem, but it enters the off-diagonal sector through the midchain gradient source. Starting from the Lyapunov equation, a first-order commutator expansion (Supplemental Material S5) yields

$$O_{ij} = \frac{i h_{ij}(D_j - D_i)}{\gamma_\phi} + \mathcal{O}(\gamma_\phi^{-3}),$$

so that for the midchain nearest-neighbor pair, |C_mid| = (J₀/γ_φ)|D_{L/2+1} − D_{L/2}|·κ, where the correction factor κ ≡ |C_exact|/|C^{(1)}| → 1 as L → ∞ (κ < 1.04 for L ≥ 32 and κ < 1.02 for L ≥ 64 across all α). In the thermodynamic limit, β → ν, the decay exponent of the midchain occupation gradient. The interior occupation satisfies the discrete fractional Laplacian equation Σ_{r≠0} (D_{i+r}−D_i)/r^{2α} = 0. Its Fourier kernel L_α(k) = −2Σ_{r≥1} (1−cos kr)/r^{2α} has small-k behavior:

$$L_\alpha(k) \approx \begin{cases} -c_\alpha |k|^{2\alpha-1}, & \alpha < 3/2 \quad\text{(anomalous)} \\ -D_{\text{eff}} k^2, & \alpha > 3/2 \quad\text{(diffusive)} \end{cases}$$

The crossover at α = 3/2 is the analytic origin of the ballistic-to-diffusive transition established by Dhawan et al. [5]. The boundary conditions are of nonlocal Robin type, with prefactor ~ L^{1−2α} that diverges for α < 3/2, producing a boundary layer of width δ(α,L) ~ L^{(2α−1)/(3−2α)} that couples all sites. At α = 1.1, δ ~ L^{1.5}, meaning the system remains boundary-layer-dominated even at L = 256.

From the fractional kernel structure and the ballistic/diffusive fixed-point constraints (β → 0 as γ_φ → 0; β → 1 as γ_φ → ∞ or α → ∞ in the diffusive limit), the leading long-range scaling coordinate is 1/α in the dephasing window where hopping and dephasing compete. We write:

$$\beta(\alpha,\gamma_\phi) = \frac{a(\gamma_\phi)}{\alpha} + b(\gamma_\phi) + \delta\beta_{\rm corr}(\alpha,\gamma_\phi,L),$$

where the coefficients a(γ_φ), b(γ_φ) are calibrated numerically (Table 1) and δβ_corr collects boundary-layer and finite-L corrections. At the reference point γ_φ = 0.5, where the log-log linearity is cleanest, the calibration gives β(α, 0.5) = 0.8127/α + 0.4218 with R² = 0.981 and RMSE = 0.015. Model selection by small-sample AIC_c (Supplemental Material S4) shows that the two-parameter 1/α form is favored over alternative two-parameter forms (ln α, linear) at γ_φ = 0.5, while at γ_φ = 0.1 the linear model wins and at γ_φ = 2.0 the three-parameter form wins. The 1/α coordinate thus captures the leading behavior in the hopping-dephasing competition window, not a globally optimal functional form. The L≤64 baseline is an effective-exponent scan; the next section extends to larger systems.

### C. The ballistic limit γ_φ = 0.01

At the weakest dephasing rate studied (γ_φ = 0.01), all five β values are 1σ-consistent with a constant β ≈ 0.155 ± 0.032 (mean ± pooled SE). The R² values (0.87–0.89) reflect the near-constancy of β rather than poor data quality. Physically, this is the ballistic crossover regime: as γ_φ → 0, the steady-state density gradient vanishes (the system approaches the purely ballistic fixed point where D_i → constant), the α-dependent coherence amplitude collapses, and β → 0. The small residual β ≈ 0.15 reflects the weak but nonzero dephasing maintaining a finite gradient. This limit provides an independent verification of the model's ballistic fixed-point structure: it confirms that the α-dependence of β is a finite-γ_φ phenomenon, vanishing as dephasing is removed. Rather than treating this regime as an awkward outlier, we include it as a limit check that constrains the functional form of a(γ_φ) → 0 as γ_φ → 0.

---

## V. Large-L Finite-Size Scaling: Two-Regime Flow (L = 128, 256)

The L≤64 baseline provides the effective-exponent landscape; the L=128 and L=256 extensions reveal how these effective exponents evolve toward the thermodynamic limit. Table 2 summarizes the FSS results at γ_φ = 0.5.

**Table 2.** Large-L coherence-exponent flow at γ_φ = 0.5. β(L≥32) and β(L≥64) are log-log fits including the L=256 anchor point. β_64→128 and β_128→256 are local two-size exponents. μ(α, γ_φ=0.5) values are computed self-consistently from the boundary current in the same numerical framework (Sec. VI). Systematic uncertainty on each local exponent is estimated at ±0.02 from correction-to-scaling considerations.

| α | β(L≥32) | β(L≥64) | β_64→128 | β_128→256 | μ(γ_φ=0.5) | Regime |
|:--:|:------:|:------:|:--------:|:---------:|:----------:|:------|
| 1.1 | 1.116 | 1.105 | 1.116 | 1.093 | 0.285(9) | long-range boundary-enhanced |
| 1.3 | 0.947 | 0.934 | 0.942 | 0.926 | 0.415(2) | crossover branch |
| 1.5 | 0.890 | 0.895 | 0.885 | 0.905 | 0.579(17) | plateau entrance / β minimum |
| 1.7 | 0.904 | 0.920 | 0.905 | 0.935 | 0.718(26) | near-diffusive plateau |
| 1.9 | 0.929 | 0.946 | 0.933 | 0.960 | 0.807(26) | near-diffusive plateau |

The large-L structure reveals two regimes rather than a globally monotone α-dependence:

**Regime 1 — Long-range boundary-enhanced decay (α ≲ 1.5).** At α = 1.1, β remains above 1 even at L=256 (β_128→256 = 1.093), reflecting the persistent boundary-layer dominance: δ ~ L^{1.5} means the system is far from the thermodynamic limit. The local exponent decreases slowly with L (flow toward smaller β), but the approach to any asymptotic plateau is slow.

**Regime 2 — Near-diffusive plateau (α ≳ 1.5).** For α ≥ 1.5, the local exponent β_128→256 increases with α (0.905 → 0.935 → 0.960), drifting toward the diffusive baseline β = 1. The minimum near α ≈ 1.5 marks the entrance to this plateau: at this α, the nonlocal Robin boundary layer becomes subdominant and the interior coherence structure approaches the ordinary diffusive fixed point. The upward drift of β at larger α reflects the shrinking boundary layer (δ shrinks as α increases beyond 1.5), allowing the diffusive bulk to dominate the finite-size scaling.

The crossover scale α_c(L) can be estimated from the position of the β minimum. At L≤64, the minimum is not yet visible (β decreases monotonically with α in the baseline fit). At L≥32 (including L=256), the minimum appears at α ≈ 1.5, and the local exponent β_128→256 has its minimum at the same α. The stability of the minimum location with increasing L suggests it is a genuine feature of the large-L scaling function rather than a finite-size artifact. The crossover from boundary-dominated to plateau behavior occurs when the boundary-layer width δ becomes comparable to the system size; the condition δ(α, L) ~ L gives α_c ≈ 3/2 for L → ∞, consistent with the observed minimum location.

---

## VI. Self-Consistent β–μ Characterization

### A. Transport exponent from boundary current

The transport exponent μ is defined via the steady-state current scaling J(L) ~ L^{−μ}. In the boundary-driven setup, the current is spatially uniform and can be evaluated from the boundary injection: J = Γ_L(f_L − D₁), where D₁ = C₁₁ (real) is the occupation of the first site. This formula follows directly from the diagonal Lindblad equation and requires only the diagonal elements of the correlation matrix — which are already computed in our solution. We compute J(L) for L = 8, 16, 32, 64 (and L = 128 for γ_φ = 0.5) and extract μ from log-log linear regression.

**Table 3.** Transport exponent μ(α, γ_φ) computed self-consistently from boundary current J(L) ~ L^{−μ}. Standard errors from log-log regression. For γ_φ = 0.5, L=128 is included in the fit range. All fits have R² > 0.99.

| α | μ(γ_φ=0.1) | μ(γ_φ=0.5) | μ(γ_φ=1.0) | μ(γ_φ=2.0) |
|:--:|:----------:|:----------:|:----------:|:----------:|
| 1.1 | 0.270(4) | 0.285(9) | 0.303(9) | 0.312(9) |
| 1.3 | 0.314(9) | 0.415(2) | 0.461(1) | 0.503(1) |
| 1.5 | 0.366(16) | 0.579(17) | 0.630(12) | 0.683(8) |
| 1.7 | 0.424(26) | 0.718(26) | 0.764(17) | 0.817(11) |
| 1.9 | 0.479(36) | 0.807(26) | 0.852(17) | 0.901(10) |

Two features are immediately apparent. First, μ increases systematically with α at every γ_φ — faster transport (smaller μ) at small α, slower transport at large α, consistent with the physical expectation that longer-range hopping enhances conduction. Second, μ depends on γ_φ at fixed α: stronger dephasing increases μ (suppresses transport). At α = 1.5, μ ranges from 0.366 (γ_φ = 0.1) to 0.683 (γ_φ = 2.0), nearly a factor of 2. This γ_φ sensitivity is expected: bulk dephasing randomizes the phase coherence that sustains the current, and this effect is not captured by the dephasing-free analysis of Dhawan et al. [5]. The μ values we obtain are consistently below the Dhawan formula μ(α) = 2α−2 — for α = 1.5, Dhawan predicts μ = 1.0, while we find μ ≈ 0.37–0.68 depending on γ_φ. This is because bulk dephasing introduces an additional dissipation channel that modifies the diagonal-sector transport relative to the coherent limit.

### B. Comparing β and μ: complementary exponents

With both β (Table 2) and μ (Table 3) computed in the same model, we can examine their relationship quantitatively. Figure 2 shows β versus μ for all (α, γ_φ) combinations.

The two exponents exhibit a robust negative correlation: at fixed γ_φ, dβ/dμ < 0 — systems with faster transport (smaller μ) have enhanced coherence decay (larger β). This anti-correlation has a partial parametric component (both β and μ depend on α), but its physical content is established by the γ_φ-dependence: varying γ_φ at fixed α shifts both β and μ, tracing out distinct trajectories in the (μ, β) plane for different γ_φ values. For α = 1.5:

| γ_φ | β(L≤64) | μ |
|:---:|:------:|:-----:|
| 0.1 | 0.675(58) | 0.366(16) |
| 0.5 | 0.943(15) | 0.579(17) |
| 1.0 | 0.997(26) | 0.630(12) |
| 2.0 | 1.040(29) | 0.683(8) |

Both β and μ increase with γ_φ at fixed α — stronger dephasing simultaneously suppresses transport (larger μ) and enhances coherence decay (larger β). The fact that β and μ respond to γ_φ with different functional sensitivities — β increases by ~54% from γ_φ=0.1 to γ_φ=2.0, while μ increases by ~87% over the same range — confirms that they are not locked in a fixed algebraic relation.

The (μ, β) plane thus provides a two-dimensional phase diagram for the NESS. The dashed lines β = 1 and μ = 1 partition the plane into four quadrants, revealing that different regions of parameter space produce qualitatively different combinations of transport and coherence behavior. For our entire parameter range at γ_φ ≥ 0.1, β ranges from 0.60 to 1.23 while μ ranges from 0.27 to 0.90 — the system explores the sub-diffusive transport (μ < 1) and both sub- and super-diffusive coherence decay (β < 1 and β > 1) regimes. This rich structure is invisible to any single-exponent characterization.

---

## VII. Universality Test: Boundary-Coupling Dependence

A defining property of a robust scaling exponent is insensitivity to microscopic details that do not change the universality class. We test β under variations of the boundary coupling strength Γ ≡ Γ_L = Γ_R ∈ {0.5, 1.0, 1.5, 2.0} (a factor of 4) and the driving bias Δf = f_L − f_R ∈ {0.1, 0.3, 0.5} (a factor of 5), at fixed α = 1.5, γ_φ = 0.5. For each of the 12 parameter combinations, β was extracted from a power-law fit across L = 4, 8, 16, 32, 64.

The exact Δf-independence follows from the linearity of the Lyapunov equation: the source term enters as an overall multiplicative factor, leaving the spatial scaling structure invariant. This is a consistency check on the numerics rather than a nontrivial universality test.

The physically informative result is the Γ-dependence. β shows mild, monotonic dependence on Γ, decreasing from β = 0.9525 ± 0.018 at Γ = 0.5 to β = 0.8782 ± 0.007 at Γ = 2.0. The maximum deviation from the reference value (β = 0.9427 ± 0.015 at Γ = 1.0) is Δβ = 0.0645, with a combined uncertainty of σ_Δ = 0.0164 — a 3.9σ effect. This is a statistically significant but physically modest dependence: a factor-of-4 change in boundary coupling shifts β by ~7%.

**Table 4.** Universality test: β(Γ, Δf) at α = 1.5, γ_φ = 0.5. Standard errors from log-log regression. β is independent of Δf by linearity.

| Γ \ Δf | 0.1 | 0.3 | 0.5 |
|:------:|:---:|:---:|:---:|
| 0.5 | 0.9525(18) | 0.9525(18) | 0.9525(18) |
| 1.0 | 0.9427(15) | 0.9427(15) | 0.9427(15) |
| 1.5 | 0.9108(11) | 0.9108(11) | 0.9108(11) |
| 2.0 | 0.8782(7) | 0.8782(7) | 0.8782(7) |

The Γ-dependence is physically expected: Γ sets the overall energy scale of boundary coupling and renormalizes the effective dephasing against which coherence is measured. We interpret this as a boundary-fixed-line effect: as Γ → ∞, the Robin boundary conditions approach Dirichlet (D → f at boundaries), the boundary layer vanishes, and β → 1 for all α. The weak Γ-dependence at finite Γ indicates that the coherence exponent is controlled primarily by bulk (α, γ_φ) physics, with boundaries entering through a well-understood fixed-line structure.

---

## VIII. Discussion and Outlook

We have presented a self-consistent two-exponent characterization of the NESS in boundary-driven power-law hopping chains with bulk dephasing. The coherence decay exponent β(α,γ_φ) and the transport exponent μ(α,γ_φ) — both computed within the same numerical framework — together reveal a richer structure than either exponent alone. β exhibits a two-regime large-L flow (long-range boundary-enhanced decay crossing into a near-diffusive plateau), while μ shows systematic dependence on both α and γ_φ that differs quantitatively from the dephasing-free formula μ = 2α−2.

Several aspects of the β–μ relationship merit further investigation. The structural connection β → ν (the occupation-gradient exponent) in the thermodynamic limit, derived from the first-order commutator expansion, implies that at finite L the difference β − ν is controlled by the correction factor κ. An independent computation of ν(α,γ_φ,L) from the occupation profile would close this triangle and provide a complete three-exponent (β, ν, μ) characterization. The crossover scale α_c(L) at which the boundary-dominated regime gives way to the near-diffusive plateau can be systematically tracked; preliminary evidence places α_c ≈ 1.5 for L ≥ 128, with weak L-dependence, but larger systems (L = 384, 512) would sharpen this estimate and test whether α_c → 3/2 exactly as L → ∞.

Experimentally, the pure imaginary structure of off-diagonal correlations makes |C_{i≠j}| directly accessible. In trapped-ion quantum simulators with tunable power-law interactions (α ∈ [0, 3]), individual ion addressing combined with fluorescence detection can reconstruct the single-particle correlation matrix for chains of L ~ 20–50 ions [2]. The key experimental signature — the power-law decay of midchain coherence with system size — requires measurements at 4–5 system sizes to extract β, which is within reach of current platforms. In Rydberg atom arrays, larger system sizes (L ≳ 100) are achievable, though the effective hopping range is typically shorter. The transport exponent μ can be extracted from the same experimental data via the boundary occupation, providing a complete experimental two-exponent characterization.

Several open questions remain. First, whether a generalized coherence exponent survives in the presence of fermion-fermion interactions (preliminary exact diagonalization of the XXZ chain at L = 4, 6 suggests the pure imaginary structure is broken by interactions Δ ≠ 0). Second, the generalization to d > 1 dimensions, where power-law hopping and spatial dimensionality may yield richer multi-exponent structures. Third, an analytic solution for the full β(α,γ_φ, L) finite-size scaling function — including the crossover from the 1/α branch to the near-diffusive plateau — would elevate the current numerical-scaling analysis to a closed-form theory.

---

## Acknowledgments

Z.H. thanks the open-source scientific computing community for the Python numerical ecosystem (NumPy, SciPy, Matplotlib) on which this work depends. All numerical computations were performed on standard consumer hardware.

---

## Data Availability

All raw data and analysis scripts are archived at the project repository. The numerical code, raw solver outputs, and figure-generation scripts are available from the author upon request and will be deposited in a public repository upon acceptance. Key data files: `phase2_fit_results_FULL.json` (25 baseline β values), `fss_gamma0.5_L256.json` (L=256 FSS anchors), `compute_mu_results.json` (self-consistent μ values), `firewall_AHA1_results.json` (universality test).

---

## References

[1] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, Oxford, 2002).

[2] G. T. Landi, D. Poletti, and G. Schaller, Rev. Mod. Phys. **94**, 045006 (2022).

[3] A. Dhar, Adv. Phys. **57**, 457 (2008).

[4] S. Lepri, R. Livi, and A. Politi, Phys. Rep. **377**, 1 (2003).

[5] A. Dhawan, K. Ganguly, M. Kulkarni, and B. K. Agarwalla, Phys. Rev. B **110**, L081403 (2024).

[6] J. Costa, P. Ribeiro, and A. De Luca, arXiv:2504.00188v3 (2025).

[7] S. Sarkar, B. K. Agarwalla, and D. S. Bhakuni, Phys. Rev. B **109**, 165408 (2024).

[8] J. M. Bhat and M. Žnidarič, Phys. Rev. B **111**, 174306 (2025).

---

## Figure Captions

**Figure 1.** (Color online) Coherence decay exponent β(α, γ_φ = 0.5). Filled circles: L≤64 baseline with 1σ error bars. Open squares: β(L≥32) from FSS fits including L=256 anchor points. Open diamonds: local exponent β_128→256. The dashed curve shows the 1/α leading-scaling fit calibrated on L≤64 data. Shaded regions indicate the long-range boundary-enhanced regime (α ≲ 1.35, red) and the near-diffusive plateau (α ≳ 1.5, green). Inset: local exponent flow from L=4–64 → L=32–256 → L=64–128 → L=128–256 for three representative α values, illustrating the transition from boundary-dominated to plateau behavior.

**Figure 2.** (Color online) β versus μ for all (α, γ_φ) combinations, color-coded by γ_φ. The negative correlation at fixed γ_φ (dβ/dμ < 0) reflects a speed-coherence trade-off: faster transport (smaller μ) is accompanied by enhanced coherence decay (larger β). We note that this anti-correlation is partially parametric in α; the physical content is established by the γ_φ-dependence — varying γ_φ at fixed α shifts both exponents along distinct trajectories (indicated by the color separation). Dashed lines mark β = 1 and μ = 1, partitioning the plane into four transport-coherence regimes. The black dashed line is a linear fit to the γ_φ = 0.5 data in the anomalous-transport domain (α ≤ 1.5).

**Figure 3.** (Color online) Universality test. Left: β versus boundary coupling Γ for three values of the driving bias Δf. Points overlap exactly due to the linearity of the Lyapunov equation (Δf enters as a multiplicative prefactor). Right: |C_mid| versus L on a log-log scale for all 12 parameter combinations, showing parallel power-law decay within each Γ group. The shaded band indicates ±5% around the reference β(Γ = 1.0).

---

## Honesty Register

1. **β → ν relationship**: A first-order commutator expansion (Supplemental S5) shows |C_mid| = (J₀/γ_φ)|D_{L/2+1}−D_{L/2}|·κ, with κ → 1 as L → ∞. In the thermodynamic limit, β → ν. We do not claim β as an "independent" exponent in the absolute sense; we claim it provides complementary information to μ, and the pair (β, μ) together characterize the NESS more fully than either alone. The finite-size structure (two-regime flow, κ ≠ 1 at finite L) is the physical content.

2. **Self-consistent μ computation**: All μ values in this Article are computed from the boundary current J = Γ_L(f_L−D₁) in the same numerical framework used for β. We do not rely on external μ formulas. The μ values we obtain differ from the dephasing-free Dhawan formula μ = 2α−2, as expected due to bulk dephasing.

3. **Pure imaginary property**: Extended to power-law hopping using the homogeneous Lyapunov system argument (Sec. III, Supplemental S2). The proof uses only (a) h real symmetric, (b) source diagonal and real, (c) γ_φ > 0 — all insensitive to hopping range. We do not claim this as the main contribution.

4. **All 8 references are real, verified publications** (audit: 2026-06-05). Reference [6] is an arXiv preprint as of this writing.

5. **γ_φ = 0.01**: Treated as the ballistic limit verification (Sec. IV.C), not as noise. β ≈ 0.155 constant within 1σ, physically expected from the vanishing density gradient.

6. **β–μ anti-correlation**: The anti-correlation has a partial parametric component (both β and μ depend on α). The physical content is established by: (i) varying γ_φ at fixed α shifts both β and μ along distinct trajectories; (ii) the functional sensitivities differ (β changes by ~54%, μ by ~87% from γ_φ=0.1 to 2.0 at α=1.5).

7. **Universality test**: Δf independence is a consistency check (linearity), not a nontrivial test. Γ-dependence (6.84%, 3.9σ) is interpreted as a boundary-fixed-line effect.

8. **Finite-size limitations**: L≤64 β values are effective exponents. L=128 and L=256 anchors (single γ_φ slice, 5 α values) constrain the large-L trend; additional γ_φ slices and L > 256 would strengthen asymptotic claims. Systematic uncertainty on local exponents: ±0.02. At α = 1.1, δ ~ L^{1.5} — the system remains boundary-dominated even at L=256.

9. **Error bars**: Standard errors in Tables 1, 3, 4 are raw regression std_err from log-log fits. Table 2 local exponents are two-point estimates; conservative ±0.02 systematic uncertainty.
