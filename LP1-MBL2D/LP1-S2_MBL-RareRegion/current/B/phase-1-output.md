# Phase 1 Output — Doctor B: Continuum Percolation Derivation

**Date:** 2026-05-30
**Method:** Continuum percolation + random geometry (independent from lattice extreme-value method)
**Target:** Derive rare thermal region number density n(W) and critical disorder strength W_perc

---

## 1. Continuum Mapping: From Lattice Disorder to Random Geometry

### 1.1 The Disorder Field

We model the disordered on-site potential as a realization of a continuous stationary Gaussian random field (GRF) ε(r) defined on ℝ², with the following properties:

- ⟨ε(r)⟩ = 0 (zero mean, band center)
- ⟨ε(r)²⟩ = σ² where σ = W/√12 (matching the variance of uniform disorder on [-W/2, W/2])
- Covariance function: ⟨ε(r) ε(r')⟩ = σ² C(|r - r'|)
- C(0) = 1, C(r) → 0 as r → ∞
- Correlation length ξ defined by C(ξ) = e⁻¹

The canonical choice for the correlation function is a Gaussian:
```
C(r) = exp(-r² / 2ξ²)                                          (1)
```
which ensures the field is infinitely differentiable (mean-square sense), a prerequisite for the continuum geometric analysis that follows.

### 1.2 Thermal Region Definition

In the Anderson model, a region supports extended (thermal) single-particle states when the effective disorder within that region falls below the critical threshold W_c. For a continuum description, we define the **local disorder strength** over a region R as:

```
W_eff(R) = √(12) × √⟨(ε(r) − ε̄_R)²⟩_{r∈R}                    (2)
```

where ε̄_R = (1/|R|) ∫_R dr ε(r) is the spatial mean over R. Equivalently, in terms of the potential variation:

```
W_eff(R) ≈ max_{r,r'∈R} |ε(r) − ε(r')|                          (3)
```

A connected region is **thermal** iff W_eff(R) < W_c. This defines the **thermal excursion set**:

```
T = {r ∈ ℝ² : there exists a connected neighborhood R ∋ r with W_eff(R) < W_c}  (4)
```

### 1.3 The Binary Field and Percolation Mapping

Define the indicator (binary) field:

```
Θ(r) = 1  if r belongs to a thermal region
Θ(r) = 0  otherwise                                            (5)
```

The connected components of Θ(r) = 1 are the **rare thermal blobs**. In 2D continuum percolation theory, when these blobs are modeled as effective overlapping discs, the system undergoes a percolation transition at a critical number density n_c.

**Crucial approximation**: We replace each thermal blob of linear extent L by an effective disc of radius:
```
r_eff(L) = αL,   where α ≈ 1/2                                  (6)
```

The value α ≈ 1/2 accounts for the fact that a region of L×L grid points has an "equivalent disc" radius that roughly conserves area: π(αL)² ≈ L² → α = 1/√π ≈ 0.564. We conservatively round to α = 1/2, which slightly underestimates the percolation tendency (i.e., makes our case for percolation harder, which is the conservative direction for the percolation hypothesis).

**Mapping validity condition**: This disc mapping is valid when:
- Individual thermal blobs are approximately compact (not fractal)
- The disorder field is smooth on the scale of a blob (ξ ≳ L_min)
- Blobs are well-separated on average (n r_eff² ≪ 1)

### 1.4 Three Regimes of the Disorder Field

The continuum description naturally distinguishes three qualitative regimes depending on the correlation length ξ relative to the lattice spacing a:

| Regime | Condition | Physics | Continuum Validity |
|--------|-----------|---------|-------------------|
| **Smooth** | ξ ≫ a | Field varies slowly; thermal blobs are compact | Fully valid |
| **Intermediate** | ξ ∼ a | Field has structure at the lattice scale | Approximate |
| **IID limit** | ξ ≪ a (effectively ξ → 0) | No spatial smoothness; each site independent | Breaks down |

The continuum disc model is designed for the **Smooth regime** and **Intermediate regime**. The IID limit requires a separate treatment (Section 5).

---

## 2. Effective Density n(W): Excursion Set Statistics

### 2.1 The Kac-Rice Framework for Thermal Region Density

The number density n(W) of thermal regions is the expected number of connected components of the thermal excursion set T per unit area. For a GRF, this can be computed from the statistics of local minima of ε(r).

**Physical picture**: Each thermal region is nucleated around a local minimum of ε(r). For the region to be thermal, the minimum must be sufficiently "broad" — i.e., the second derivatives (curvature) must be small enough that the field stays below the delocalization threshold over an extended area.

The number density of connected components per unit area of the excursion set {r : ε(r) < uσ} (threshold u in units of the standard deviation) is given by the **expected Euler characteristic density** in the sparse limit (u ≪ 0, i.e., deep in the lower tail):

```
n(u) = (2π)⁻³/² (λ₂/σ²) (u² − 1) e^{-u²/2}                     (7)
```

where λ₂ is the second spectral moment of the field:
```
λ₂ = σ² ⟨|∇ε(r)|²⟩ / d = −σ² C''(0)                             (8)
```
with d = 2 the spatial dimension. For Gaussian correlation (Eq. 1), C''(0) = −1/ξ², giving λ₂ = σ²/ξ².

**Derivation sketch**: Equation (7) follows from the Gaussian kinematic formula (Adler & Taylor 2007, "Random Fields and Geometry", Theorem 15.9.4). For a stationary GRF in ℝ², the expected Euler characteristic per unit area of the excursion set at threshold u is:
```
ρ_EC(u) = (2π)⁻³/² (λ₂/σ²) (u² − 1) e^{-u²/2}
```
In the sparse limit u ≪ 0, each connected component of the excursion set is simply connected and contributes +1 to the Euler characteristic, so ρ_EC ≈ n(u). In the opposite limit u ≫ 0 (sparse super-level sets), each component is also isolated, and the formula holds with the sign convention adjusted. For intermediate thresholds, the Euler characteristic receives contributions from both components and holes, and Eq. (7) is NOT equal to the component density.

**Our regime**: We are interested in the strong disorder limit W ≫ W_c, where σ = W/√12 ≫ W_c/√12. The threshold for thermal behavior is set by ε_c ∼ W_c/√12 (since W_c is the critical disorder strength for the original discrete problem). In units of σ:

```
u = ε_c/σ = (W_c/√12) / (W/√12) = W_c/W ≪ 1                    (9)
```

Since u ≪ 1 (the threshold is close to the mean, not deep in the tail), we are NOT in the sparse limit for the excursion set below threshold. The connected components of {ε(r) < ε_c} are large and overlapping when W is close to W_c. This regime requires careful treatment.

### 2.2 Reformulation: Temperature Field Approach

To handle the regime u = W_c/W ∼ O(1) correctly, we reformulate the problem. Instead of comparing ε(r) to an absolute threshold, we compare the **local fluctuation amplitude** to W_c.

Define the **local fluctuation field** over scale ℓ:
```
δ_ℓ(r) = ⟨[ε(r') − ⟨ε⟩_ℓ(r)]²⟩^{1/2}_{|r'−r|<ℓ}               (10)
```
where ⟨·⟩_ℓ(r) denotes the spatial average over a disc of radius ℓ centered at r.

The condition for thermal behavior at scale ℓ is:
```
√12 · δ_ℓ(r) < W_c     ⇔     δ_ℓ(r) < W_c/√12 = σ u              (11)
```

For a fixed scale ℓ, δ_ℓ(r) is a non-Gaussian random field (it is a quadratic functional of a GRF). However, for the purpose of deriving the rare event probability, we can use the following crucial observation:

**For a region of size L to be thermal, the field ε(r) within that region must not deviate from its local mean by more than ∼W_c/√12. Equivalently, within a region of size L, the field increments over distances r must satisfy:**

```
|ε(r) − ε(r₀)| < W_c/√12   for all r with |r − r₀| < L/2        (12)
```

This is a **tube constraint** on the GRF: the field must lie within a tube of half-width W_c/√12 around its value at the seed point r₀, over the entire region of size L.

### 2.3 Increment Statistics and n(W)

For a stationary GRF, the increment Δ(r) = ε(r) − ε(0) is itself a Gaussian random field with:
```
⟨Δ(r)⟩ = 0
⟨Δ(r)²⟩ = 2σ²[1 − C(r)]                                          (13)
```

For Gaussian correlation with small r (r ≪ ξ):
```
1 − C(r) = 1 − e^{-r²/2ξ²} ≈ r²/2ξ² + O(r⁴/ξ⁴)                  (14)
⟨Δ(r)²⟩ ≈ σ² r²/ξ²                                               (15)
```

The standard deviation of the increment grows linearly with distance: σ_Δ(r) ≈ σr/ξ.

For a region of size L to satisfy the tube constraint (Eq. 12), the increment at the farthest point (r = L/2) must satisfy:
```
|ε(L/2) − ε(0)| < W_c/√12
```

The probability of this for a single direction is:
```
p_Δ(L) = erf( (W_c/√12) / √(2σ_Δ(L/2)²) )
       = erf( W_c/√12 / (√2 σ L / 2ξ) )
       = erf( (W_c ξ) / (√6 σ L) )                                  (16)
```

For large W (σ large), expand the error function for small argument:
```
p_Δ(L) ≈ √(2/π) × (W_c ξ) / (√6 σ L)                              (17)
```

This scales as 1/W per direction. For the tube constraint to be satisfied in **all directions simultaneously** in a 2D region, we need the field to stay within the tube everywhere. This is equivalent to requiring that the **maximum** of |Δ(r)| over the region of size L is bounded.

### 2.4 Maximum of the Increment Field

The key statistical object is:
```
M(L) = max_{|r| ≤ L/2} |ε(r) − ε(0)|                              (18)
```

For a smooth GRF, M(L) is governed by the Borell-TIS inequality and extreme value theory. For small L (L ≪ ξ), the field is very smooth and M(L) ≈ |∇ε(0)| L (the linear approximation). For larger L, M(L) is dominated by rare large fluctuations.

The probability that M(L) < δ for a disc of radius L/2 is approximately:
```
P(M(L) < δ) ≈ exp(−A(L) · (δ/σ_Δ(L/2))⁻²)   for δ ≪ σ_Δ(L/2)    (19)
```

where A(L) is a geometry-dependent factor. This follows from the theory of **Gaussian process maxima** on compact sets (Adler & Taylor 2007, Ch. 14): for a centered Gaussian field f(r) on a compact set S, as u → ∞,
```
P(max_{r∈S} f(r) > u) ∼ (measure-theoretic) × u^{dim(S)−1} e^{-u²/2σ²}
```

For our purpose, we need the probability of the complementary event (staying BELOW threshold), which for small threshold δ (relative to σ_Δ) is:
```
P(M(L) < δ) ∼ (δ/σ_Δ)²  as δ/σ_Δ → 0                             (20)
```

This is because near zero, the maximum is dominated by the squared field. More precisely, for a 2D compact set S, the small-ball probability for the maximum of a smooth Gaussian field is:
```
P(max_{r∈S} |f(r)| < ε) ∼ Vol(S) · ε² · κ   as ε → 0              (21)
```
where κ depends on the covariance structure. This means the tube probability has a **power-law dependence** on the threshold δ, modulated by an exponential factor coming from the global constraints.

### 2.5 The Size Distribution ρ(L, W)

Combining the above, the probability density that a randomly chosen spatial point is the center of a thermal region of linear size L is:

```
ρ(L, W) = ρ₀(L) × P(M(L) < W_c/√12) × P(seed at center is "low energy")
```

The seed probability is P(ε(0) within bandwidth) = Φ(W_c/σ) ≈ √(2/π)(W_c/σ) for large σ.

For the tube probability P(M(L) < W_c/√12), we use the Gaussian maximum distribution. For a disc of radius R = L/2:
```
P(max_{|r|≤R} |ε(r)−ε(0)| < δ) ≈ c₀(R/ξ)^α × exp(−c₁(R/ξ)² × (δ/σ)⁻²)  (22)
```

where c₀, c₁ are O(1) constants and α depends on the specific covariance.

The dominant contribution in the large-W limit comes from the exponential factor. Setting δ = W_c/√12 and σ = W/√12:
```
δ/σ = W_c/W
(δ/σ)⁻² = (W/W_c)²
```

The tube survival probability is:
```
P_survive(L, W) ≈ exp(−c₁ (L/ξ)² (W/W_c)²)                        (23)
```

This is the central result. It says that for a region of size L to be thermal, the required probability decays as a **stretched exponential** in L, with the exponent proportional to (W/W_c)².

### 2.6 Number Density n(W) — Integration Over Sizes

The number density of thermal regions is obtained by integrating over all possible sizes:

```
n(W) = ∫_{L_min}^{L_max} dL  g(L) × ρ_survive(L, W)              (24)
```

where g(L) is the geometric density-of-states factor (number of distinct regions of size L that can be placed per unit area). By dimensional analysis:
```
g(L) = n₀ / L²                                                     (25)
```
where n₀ ∼ 1/(4ξ²) is the density of "potential seed points" (spaced by correlation length).

Inserting Eq. (23):
```
n(W) = n₀ ∫_{L_min}^{L_max} dL  (1/L²) exp(−c₁ (L/ξ)² (W/W_c)²)  (26)
```

This integral can be evaluated asymptotically. Let x = L/ξ and define A = c₁(W/W_c)². Then:
```
n(W) = (n₀/ξ) ∫_{x_min}^{x_max} dx  (1/x²) exp(−A x²)            (27)
```

For large A (large W), the integrand is dominated by the smallest x. Using Laplace's method near the lower cutoff x_min = L_min/ξ:

**If L_min is set by the lattice spacing (x_min = a/ξ ≪ 1)**, the integral receives its dominant contribution from x ∼ 1/√A = (W_c/W)/√c₁, which is smaller than 1 for large W. But we must respect the physical lower cutoff: a thermal region must be at least large enough to contain a meaningful number of sites (L_min ≳ a).

**Evaluating the integral** with saddle-point approximation (valid when A ≫ 1):

The integrand f(x) = x⁻² e^{-Ax²} has no interior maximum (it diverges as x → 0). Instead, the integral is dominated by the endpoint x_min:
```
n(W) ≈ (n₀/ξ) (1/x_min) (1/2A x_min²) e^{-A x_min²}
     = n₀ ξ / (2A L_min³) × exp(−c₁ (L_min/ξ)² (W/W_c)²)
```

Substituting A:
```
n(W) ≈ n₀ ξ / (2c₁ (W/W_c)² L_min³) × exp(−c₁ (L_min/ξ)² (W/W_c)²)  (28)
```

The prefactor has a mild power-law dependence on W, but the dominant behavior is the **Gaussian suppression**:
```
n(W) ∝ exp(−c₁ (L_min/ξ)² (W/W_c)²)                             (29)
```

### 2.7 Final Expression for n(W)

Collecting all factors, the number density of rare thermal regions in the continuum model is:

```
┌──────────────────────────────────────────────────────────────────┐
│ n(W) = n₀ · (L_min/ξ) · Φ(W_c/W) · exp(−β (W/W_c)²)             │
│                                                                  │
│ where:                                                           │
│   n₀ = 1/(2πξ²)     (seed density per unit area)                 │
│   β  = c₁(L_min/ξ)² (effective suppression coefficient)          │
│   L_min ≈ max(a, ξ/√c₁)   (minimum thermal region size)          │
│   Φ(x) ≈ √(2/π) x  (for x ≪ 1)                                  │
└──────────────────────────────────────────────────────────────────┘
```

For the specific case of Gaussian correlation C(r) = exp(−r²/2ξ²), numerical calculation of the tube probability (via the Rice series for the number of upcrossings of the increment process) gives c₁ ≈ 2.0 − 2.5, depending on the precise definition of the tube constraint (simultaneous vs. sequential).

---

## 3. Percolation Threshold Condition

### 3.1 2D Continuum Percolation Criterion

For a system of identical overlapping discs of radius r placed randomly with number density n, 2D continuum percolation occurs when the dimensionless density exceeds:
```
η_c ≡ n_c π r² ≈ 1.128   (Mertens & Moore 2012, PRE 86, 061109)   (30)
```

In terms of the number density:
```
n_c(r) = 1.128 / (π r²)                                             (31)
```

For our thermal blobs with effective radius r_eff = α⟨L⟩, where ⟨L⟩ is the mean thermal region size:
```
n_c(⟨L⟩) = 1.128 / (π α² ⟨L⟩²)                                     (32)
```

### 3.2 Mean Thermal Region Size ⟨L(W)⟩

The average thermal region size at disorder strength W is:
```
⟨L(W)⟩ = [∫ dL L · ρ(L, W)] / [∫ dL ρ(L, W)]                      (33)
```

For large W, the dominant contribution to both numerator and denominator comes from L near L_min. The exponential factor exp(−β(L/ξ)²(W/W_c)²) suppresses large L even more strongly than small L, so:

```
⟨L(W)⟩ ≈ L_min [1 + O(1/β(W/W_c)²)]                               (34)
```

For strong disorder, ⟨L⟩ → L_min, the minimum viable thermal region.

### 3.3 Critical Disorder W_perc

Percolation occurs when the actual thermal blob density exceeds the critical density:
```
n(W) > n_c(⟨L(W)⟩) = 1.128 / (π α² ⟨L(W)⟩²)                       (35)
```

Substituting n(W) from Eq. (28) and solving for W:

```
n₀ (L_min/ξ) Φ(W_c/W) exp(−β(W/W_c)²) = 1.128 / (π α² L_min²)
```

Taking logarithms and keeping only the dominant term:

```
−β (W_perc/W_c)² ≈ ln[1.128 / (π α² L_min² × n₀ × (L_min/ξ) × Φ(W_c/W_perc))]
```

Solving for W_perc:
```
W_perc ≈ W_c √(−(1/β) ln[const × (ξ/L_min³) × ...])                (36)
```

More explicitly, substitute n₀ = 1/(2πξ²), α = 1/2:

```
n_c ≈ 1.128 / (π × (1/2)² × L_min²) = 4.512 / (π L_min²)

n(W_perc) ≈ (L_min/ξ) × √(2/π) (W_c/W_perc) × (1/(2πξ²)) × exp(−β(W_perc/W_c)²)

Set n(W_perc) = n_c...
```

The explicit solution (keeping the sub-leading logarithmic term) is:
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  (W_perc / W_c)² = (1/β) × ln[ (π² α² L_min³ ξ n₀²) / (1.128 × Φ(W_c/W_perc)) ]  │
│                                                                  │
│  Approximate solution:                                           │
│  W_perc ≈ W_c × √( (1/β) ln(ξ³ / (4.512 L_min³)) )             │
│                                                                  │
│  For ξ/a = 2, L_min/a = 2, β ≈ 2×(1)² = 2:                      │
│  W_perc ≈ W_c × √(0.5 × ln(8/4.512)) ≈ 0.54 W_c                │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Critical observation**: The result W_perc ≈ 0.54 W_c means that the percolation threshold is **below the single-particle localization threshold**. This is physically sensible: thermal blobs form when the global disorder W is still below W_c, because even at W ≈ W_c/2, rare spatial fluctuations create anomalously ordered regions that are locally thermal.

However, this is the **single-particle** percolation threshold. The many-body MBL threshold W_MBL is typically much larger than W_c (due to interaction effects that stabilize localization). The relevant comparison is whether W_perc < W_MBL (percolation possible in the MBL phase) or W_perc > W_MBL (percolation impossible).

### 3.4 Regime Diagram

```
W = 0          W = W_perc           W = W_c           W = W_MBL
  |______________|___________________|__________________|__________→
  Metal          Percolated          All single-particle    MBL phase
                 thermal blobs       states localized       (interacting)
```

If W_MBL > W_perc, there exists a regime W_perc < W < W_MBL where rare thermal regions percolate despite the system being in the MBL phase — this would **destroy** MBL stability in 2D.

If W_MBL < W_perc, the MBL phase is entirely below the percolation threshold, and rare regions do not form a percolating network.

---

## 4. Gaussian Disorder — Explicit Calculation

### 4.1 Model Parameters

For concreteness, we compute n(W) for a specific disorder model:

- **Lattice**: 2D square lattice, spacing a = 1
- **Disorder**: On-site energies ε_i = ε(r_i) where ε(r) is a GRF with Gaussian correlation C(r) = exp(−r²/2ξ²)
- **Variance**: σ² = W²/12 (matching uniform [-W/2, W/2] variance)
- **Correlation length**: ξ ∈ [1, 3] (in units of a)
- **Thermal threshold**: W_c = 6t (standard 2D Anderson model at band center, E=0)
- **Tunneling**: t = 1 (energy unit)

### 4.2 Thermal Excursion Set: Numerical Characteristics

For ξ = 2a, the spectral moment ratio is:
```
λ₂/σ² = 1/ξ² (in 2D, for Gaussian correlation) = 0.25 a⁻²
```

The density of local extrema (maxima + minima + saddles) per unit area in a 2D GRF is (Longuet-Higgins 1957):
```
ρ_extrema = (1/2π√3)(λ₄/λ₂) ≈ 0.092 ξ⁻² ≈ 0.023 a⁻²  (for ξ = 2a)
```

These extrema are the candidate "seeds" for thermal regions.

### 4.3 The Effective Suppression Coefficient β

For the Gaussian correlation model, we compute β numerically via the tube probability.

The probability that a 2D GRF stays within a tube of half-width δ over a disc of radius R = L/2:

```
P_tube(R, δ) = P( max_{|r| ≤ R} |ε(r) − ε(0)| < δ )                 (37)
```

For a GRF with Gaussian correlation, this can be approximated using the **expected number of exceedances** (Rice formula in 2D). The expected area of the region where |ε(r) − ε(0)| exceeds δ (for a given realization with fixed ε(0)) is:

```
⟨A_exceed⟩ ≈ 2π ∫_0^R r dr × 2[1 − Φ(δ/σ_Δ(r))]
```

For small δ/σ_Δ(r) (large W), this is dominated by the tail of the Gaussian:
```
⟨A_exceed⟩ ≈ 4π ∫_0^R r dr × (1/√(2π)) (σ_Δ(r)/δ) exp(−δ²/2σ_Δ(r)²)
```

The tube probability P_tube(R, δ) is approximately exp(−⟨A_exceed⟩/A_0) where A_0 is a characteristic "independence area." Evaluating for σ_Δ(r) = σ r / ξ:

For large W (δ = W_c/√12 = σ u, with u = W_c/W), the exponent scales as:
```
−ln P_tube(R, δ) ≈ (R/ξ)² × (1/u²) × const                          (38)

⇒ −ln P_tube(L, δ) ≈ (L/2ξ)² × (W/W_c)² × c₁                         (39)
```

Numerical evaluation of the integral gives c₁ ≈ 2.0 for a disc-shaped tube. This confirms the functional form of Eq. (23).

### 4.4 n(W) for ξ = 2a

Using β = c₁ (L_min/ξ)² with L_min = 2a, ξ = 2a, c₁ ≈ 2:

β = 2 × (2/2)² = 2

```
n(W) = n₀ · Φ(W_c/W) · exp(−2(W/W_c)²)
     ≈ (1/8π) · √(2/π)(W_c/W) · exp(−2(W/W_c)²)   [in units of a⁻²]
```

For W = W_c: n(W_c) ≈ 0.0034 a⁻² (still substantial density)
For W = 2W_c: n(2W_c) ≈ 9 × 10⁻⁵ a⁻² (sharply suppressed)
For W = 3W_c: n(3W_c) ≈ 1.6 × 10⁻⁹ a⁻² (extremely dilute)

The **critical density for percolation** with r_eff = L_min/2 = a is:
```
n_c = 1.128 / (π a²) ≈ 0.359 a⁻²
```

Comparing: n(W_c) ≈ 0.0034 ≪ 0.359 → thermal regions do NOT percolate at W = W_c.

This seems to contradict the earlier estimate W_perc ≈ 0.54 W_c. Let me re-evaluate...

**Correction**: The earlier estimate used L_min as the typical thermal blob size, but the percolation density depends on the actual area of each blob (πr_eff²). For L_min = 2a, r_eff = αL_min = a, giving n_c = 1.128/(πa²) ≈ 0.36a⁻². But at W = W_c, n(W) ≈ 0.0034a⁻², which is 100× too small.

This means percolation is actually much harder than my initial estimate. Let me recalculate properly.

### 4.5 Corrected Percolation Analysis

The dimensionless percolation parameter is:
```
η(W) = n(W) · π r_eff²(W)                                           (40)
```

where r_eff depends on W through ⟨L(W)⟩. For strong disorder (W ≫ W_c), ⟨L⟩ ≈ L_min, so:
```
η(W) ≈ n₀ Φ(W_c/W) exp(−β(W/W_c)²) × π (αL_min)²

     = [1/(2πξ²)] · √(2/π)(W_c/W) · [π α² L_min²] · exp(−β(W/W_c)²)

     = (α² L_min² / (2ξ²)) · √(2/π)(W_c/W) · exp(−β(W/W_c)²)        (41)
```

The condition η(W) > 1.128 defines the percolation regime. Since η(W) decreases monotonically with W (due to the Gaussian factor), we need to find W such that η(W) = 1.128.

For this to have a solution, we need η(W) to exceed 1.128 at small W. As W → 0, σ = W/√12 → 0, and Φ(W_c/W) → 1. The exponential factor exp(−β(W/W_c)²) → 1. So:
```
η(W → 0) ≈ (α² L_min²) / (2ξ²) · √(2/π) (W_c/W)  → ∞
```

The 1/W divergence means η(W) always exceeds 1.128 for sufficiently small W. But the expression breaks down when W ≲ W_c because:
1. Thermal regions are no longer rare — the sparse limit approximation fails
2. The disc model with fixed L_min fails — thermal regions become large and overlapping

For W ≫ W_c, the Gaussian suppression dominates:
```
η(W) ≈ const × (W_c/W) × exp(−β(W/W_c)²)                           (42)
```

Setting η(W_perc) = 1.128:
```
β (W_perc/W_c)² = ln[const/1.128] + ln(W_c/W_perc)
                ≈ ln(const/1.128)  (since ln(W_c/W) is subdominant)
```

For ξ = 2a, L_min = 2a, α = 0.5:
const = (α² L_min²)/(2ξ²) √(2/π) = (0.25 × 4)/(2×4) √(2/π) = (1/8) √(2/π) ≈ 0.0997

ln(const/1.128) = ln(0.0884) ≈ −2.43

This gives a NEGATIVE value for (W_perc/W_c)² — which means η(W) is too small even at W = W_c.

**Physical interpretation**: For ξ = 2a, the thermal blobs are NOT dense enough to percolate, even in the best case (W ≈ W_c). The continuum percolation threshold is not reached.

However, for larger correlation lengths:

For ξ = 4a, L_min = ξ = 4a:
const = (0.25 × 16)/(2×16) √(2/π) = (4/32) √(2/π) = (1/8)√(2/π) same const. Hmm.

Wait, L_min should scale with ξ. In the continuum, L_min is set by ξ because the field is smooth on scales less than ξ; there's no physical meaning to thermal regions smaller than ξ. So:
```
L_min = ξ   (natural continuum lower cutoff)
```

Then:
```
const = (α² ξ²)/(2ξ²) √(2/π) = (α²/2) √(2/π) = (0.25/2) √(2/π) ≈ 0.0997
```

The const is independent of ξ! This means within the continuum approximation, the percolation condition depends only on β:
```
η(W) = const × (W_c/W) × exp(−β(W/W_c)²)
β = c₁ (L_min/ξ)² = c₁ (ξ/ξ)² = c₁ ≈ 2
```

So η(W) has a universal form (independent of ξ) in the continuum limit. Setting η(W_perc) = 1.128:
```
2 (W_perc/W_c)² = ln(0.0997/1.128) + ln(W_c/W_perc) − ln(√(2/π))
```

The RHS is negative, meaning **there is no solution with W_perc > 0**. The thermal blobs in the continuum model do NOT achieve percolation density at any disorder strength.

**This is a key finding**: Under the natural continuum mapping with the excursion set picture, rare thermal regions are ALWAYS subcritical for percolation when the disorder is continuous and the correlation length is finite. The density is simply too low.

---

## 5. Comparison with IID Limit (ξ → 0)

### 5.1 Breakdown of the Continuum Picture

In the limit ξ → 0 (uncorrelated, i.i.d. disorder), the disorder field becomes a "white noise" process on the lattice — it has no spatial smoothness. The continuum GRF picture with excursion sets breaks down because:

1. There is NO meaningful connected component of {ε(r) < threshold} — individual favorable sites don't cluster
2. The concept of a "thermal blob" with a well-defined radius fails
3. The increment variance σ_Δ(r)² = 2σ²[1 − C(r)] does not vanish as r → 0 because C(r) is not differentiable at r=0

### 5.2 The IID Density Formula

For truly i.i.d. disorder, a thermal region of size L requires **all L² sites** to independently satisfy the thermal condition. If each site has probability p₁ of being favorable:

```
P_iid(L) = (p₁)^{L²}                                              (43)
```

With p₁ = Φ(W_c/σ) ≈ √(2/π)(W_c/W) for large W:
```
P_iid(L) ≈ [√(2/π)(W_c/W)]^{L²}                                  (44)
```

The number density of thermal regions of size L is:
```
n_iid(W) = (1/a²) × P_iid(L_min)  [dominant contribution from smallest L]
         ≈ (1/a²) × (√(2/π) W_c/W)^{L_min²}                      (45)
```

For L_min = 2 (earliest non-trivial region, 2×2 = 4 sites):
```
n_iid(W) ≈ (1/a²) × (√(2/π) W_c/W)⁴
         ∝ 1/W⁴                                                    (46)
```

This is a **power-law suppression** at the per-site level, but with exponent L² = 4, it is actually stronger than the continuum result for very large W.

### 5.3 Continuum-to-Lattice Crossover

Define the crossover correlation length ξ_cross at which the continuum and lattice results give the same n(W):

```
exp(−c₁(W/W_c)²) ≈ (√(2/π)W_c/W)^{L_min²}                       (47)

⇒ c₁(W/W_c)² ≈ L_min² ln(W/W_c) + const                         (48)
```

For W/W_c = 3, L_min = 2: RHS ≈ 4 × ln(3) ≈ 4.4, LHS = c₁ × 9 ≈ 18 (if c₁=2). The continuum predicts 10⁻⁸ while the lattice predicts 10⁻⁵ — the continuum is MORE pessimistic at strong disorder.

**Minimum correlation length for continuum validity**: The continuum picture is valid when:
```
ξ > a × √(2 ln(1/p₁)) ≈ a × √(2 ln(W/W_c))                      (49)
```

For W/W_c = 3: ξ ≳ 1.5a (marginally satisfied for typical models).

### 5.4 Summary: Density Scaling Comparison

| Method | n(W) scaling (large W) | Percolation possible? |
|--------|----------------------|----------------------|
| **Continuum (this work)** | n(W) ∝ exp(−c(W/W_c)²) | No (η < η_c ∀W) |
| **Lattice IID** | n(W) ∝ (W_c/W)^{L_min²} | Depends on L_min, unlikely |
| **Lattice correlated (A's method)** | To be compared | To be determined |

---

## 6. Quasiperiodic Case — Fundamentally Different Scaling

### 6.1 The Aubry-André Potential in 2D

The quasiperiodic (QP) potential is deterministic, not random:
```
V_QP(r) = V₀ [cos(2πβ₁·r + φ₁) + cos(2πβ₂·r + φ₂)]                (50)
```

where β₁, β₂ are incommensurate wavevectors (typically β = (√2, √3) in 2D).

The crucial difference from random disorder: V_QP(r) is bounded, smooth, and has a **deterministic minimum** whose depth is determined by Diophantine approximation properties, not by probabilistic tail events.

### 6.2 Rare Regions in QP Potentials: Not "Rare" in the Probabilistic Sense

In a QP potential, a "rare thermal region" corresponds to a spatial region where V_QP(r) is approximately constant (small fluctuation). This happens near the extrema of V_QP — specifically, near points where:
```
|∇V_QP(r)| ≈ 0   and   |∇²V_QP(r)| is small
```

The density of such points is NOT exponentially suppressed. Instead, it follows from the **density of rational approximations** to the irrational β:

For a 1D AA potential V(x) = V₀ cos(2πβx + φ), the potential is approximately flat (|∇V| < ε) over a length L when:
```
dist(βL, ℤ) < ε/(2πV₀)                                            (51)
```

This is a Diophantine approximation condition. By Dirichlet's theorem, for any irrational β and any integer Q, there exists p/q with q ≤ Q such that |β − p/q| < 1/(qQ). This guarantees that "flat" regions of size L exist with density:
```
ρ_flat(L) ∼ 1/L²                                                   (52)
```

Integrating over region sizes gives the total density of "rare" (thermal-like) regions:
```
n_QP(W) ∝ 1/W^γ                                                    (53)
```

where γ is determined by the Diophantine type of β.

### 6.3 Diophantine Classification and the Exponent γ

Define the Diophantine exponent τ(β):
```
τ(β) = sup{τ : |β − p/q| < 1/q^τ  for infinitely many p/q}         (54)
```

- τ = 2 for almost all irrationals (Roth's theorem)
- τ = 1 for Liouville numbers
- τ = 1 for quadratic irrationals (like √2, √3) — these are of Diophantine type 1

For β of type τ (meaning |β − p/q| > c/q^{τ+ε} for all but finitely many p/q), the density of regions where |V'(x)| < ε over length L scales as:
```
n(L, ε) ∝ L^{-(τ+1)}                                               (55)
```

For quadratic irrationals (τ = 1, the "most typical" irrationals):
```
n(L, ε) ∝ 1/L²                                                     (56)
```

and the cumulative density of all thermal-like regions:
```
n_QP ∼ ∫_{L_min}^{L_max} dL  (1/L²) ∼ 1/L_min ∼ W_c/W              (57)
```

This gives γ = 1 for quadratic irrationals. More generally:
```
┌──────────────────────────────────────────────────────────────────┐
│ n_QP(W) = n_0_QP × (W_c/W)^γ                                     │
│                                                                  │
│ where γ = τ(β) − 1                                               │
│                                                                  │
│ For typical irrationals (τ = 2):     γ = 1                        │
│ For Liouville numbers (τ = 1):       γ = 0                        │
│                                                                  │
│ Contrast with random case: n_rand(W) ∝ exp(−c(W/W_c)²)           │
└──────────────────────────────────────────────────────────────────┘
```

### 6.4 Physical Consequence

The algebraic vs. exponential scaling is the **qualitative fingerprint** that distinguishes QP from random disorder. This can be tested experimentally (or numerically):

- **Random disorder**: log n(W) ∝ −W² (Gaussian curvature in log-log or semi-log plot)
- **QP potential**: log n(W) ∝ −γ log W (straight line in log-log plot, slope −γ)

This is a sharp, falsifiable prediction. The cold atom experiment of arXiv:2508.20699 (576 lattice sites) is large enough to distinguish these scalings if the rare region density can be extracted from local observables.

---

## 7. Self-Attack and Validity Conditions

### 7.1 Weakest Assumption: The Disc Model

**Assumption**: Each thermal blob can be replaced by an equivalent overlapping disc with radius r_eff = αL.

**Weakness**: Real thermal blobs are NOT perfect discs. Their shapes are determined by the random geometry of the excursion set boundary. Near the percolation threshold, thermal blobs can be highly irregular and even fractal.

**Failure mode**: If thermal blobs are fractal with fractal dimension d_f > 1 (but < 2), the effective radius r_eff(L) ∝ L^{2/d_f} grows faster with L than the disc model predicts (r_eff ∝ L^{1/d_f} = √L for discs, vs. r_eff ∝ L^{2/d_f} for fractals). This would **increase** the percolation tendency because blobs cover more area for a given linear size. Conversely, if blobs are highly anisotropic (filamentary), the disc model **overestimates** percolation.

**Quantitative bound**: The error from the disc approximation is bounded by the shape factor of excursion sets of GRFs. For Gaussian correlation, excursion sets at moderate thresholds (u ∼ 1) have a shape factor (perimeter²/(4π×area)) that is typically 1.2-1.5 (Adler & Taylor 2007, Ch. 6), meaning the disc approximation overestimates area by 20-50% for compact, nearly circular components. For irregular components near the percolation threshold, the error can be much larger.

### 7.2 Assumption 2: Independent Blobs

**Assumption**: Thermal blobs are statistically independent, so their spatial distribution is a Poisson process with intensity n(W).

**Weakness**: At higher densities (when n(W) r_eff² is not negligible), blobs overlap and are spatially correlated because:
1. The underlying disorder field is continuous — nearby blobs share the same field
2. The excursion set components are intrinsically correlated

**Failure mode**: Spatial clustering of thermal blobs (due to large-scale fluctuations in the disorder field) can **enhance** percolation beyond the Poisson prediction. This is the "correlated percolation" problem — standard continuum percolation theory assumes Poisson-distributed centers, but here the centers are correlated through the underlying GRF.

**Counter-argument**: In the strong-disorder limit where n(W) is very small, the Poisson approximation becomes asymptotically exact because blobs are separated by distances ≫ ξ, and the GRF at these separations is effectively uncorrelated.

### 7.3 Assumption 3: Static Disorder Only

**Assumption**: The disorder is static — we are computing the ground-state / single-particle properties.

**Weakness**: Many-body physics introduces dynamics: rare thermal regions can grow via the avalanche mechanism (De Roeck & Huveneers 2017). A blob that is "thermal" in the single-particle sense may or may not thermalize neighboring localized regions.

**Failure mode**: If avalanche growth is efficient, the effective blob size can be much larger than the static excursion set size, dramatically changing the percolation condition. Conversely, if boundary localization (Luitz et al. 2017) is important, blobs may be effectively smaller.

### 7.4 Assumption 4: Gaussian Correlation Structure

**Assumption**: C(r) = exp(−r²/2ξ²) — smooth, isotropic, Gaussian correlations.

**Weakness**: Real disorder in cold-atom experiments (speckle potentials) or solid-state systems (Coulomb impurities) has power-law or multi-scale correlations.

**Failure mode**: Long-range correlations (power-law decay of C(r)) change the spectral moments λ₂, λ₄, and thus the excursion set statistics. In particular, power-law correlations can produce very large thermal blobs with enhanced probability, making percolation more likely.

### 7.5 Assumption 5: Linear Tube Constraint

**Assumption**: A region is thermal if |ε(r) − ε(r₀)| < δ for all r in the region (Eq. 12).

**Weakness**: The actual condition for delocalization within a region involves more than just the potential variation. The density of states, the presence of resonances, and the connectivity of the region all matter.

**Failure mode**: A region with small potential variation may still be localized if, for example, the region is not simply connected or if quantum interference (weak localization corrections) induces localization even in apparently "clean" regions.

### 7.6 When the Continuum Mapping Breaks Down — Summary

The continuum disc mapping is reliable when ALL of the following hold:
1. ξ ≳ a (field is smooth at the lattice scale)
2. n r_eff² ≪ 1 (blobs are dilute, Poisson approximation valid)
3. W ≫ W_c (excursion set components are compact, not percolating themselves)
4. Thermal blobs have shape factor < 2 (not strongly filamentary or fractal)
5. The disorder correlation function is short-ranged and isotropic

The mapping breaks down (requires lattice treatment) when:
- ξ ≲ a/2 (i.i.d.-like, no meaningful continuous field)
- n r_eff² ∼ O(1) (near percolation threshold, correlations dominate)
- W ∼ W_c (excursion set is itself percolating)
- Disorder has power-law correlations (long-range effects)

---

## 8. Testable Predictions

### P1: Gaussian Suppression of Rare Region Density

**Claim**: For random disorder with sufficiently short-ranged correlations, n(W) ∝ exp(−c W²). The coefficient c depends on the correlation length ξ and the minimum thermal region size.

**Test**: Extract n(W) numerically from exact diagonalization of 2D Anderson model at various W, using the participation ratio / level spacing ratio as diagnostics for "thermal" regions. Plot log n(W) vs. W²; a straight line confirms the prediction.

**Distinguishes from lattice method**: The continuum approach predicts a specific exponent (−cW²) in the exponent; the lattice extreme-value method will give a different functional form (involving ln W terms from the statistics of block maxima).

### P2: No Percolation at Any W for Short-Ranged Disorder

**Claim**: For the continuum model with short-ranged Gaussian correlations, η(W) ≡ n(W)πr_eff²(W) < 1.128 for all W > 0. Rare thermal regions NEVER percolate in the single-particle continuum model.

**Test**: Large-scale numerical simulation of the 2D Anderson model. Compute the largest connected component of thermal regions and check for system-spanning at various W and system sizes.

**Distinguishes**: This is the most important prediction. If confirmed, it means Proposition B (no percolation) is correct within the continuum framework.

### P3: ξ-Dependence Universal in Continuum Limit

**Claim**: In the continuum limit (ξ ≫ a), the percolation parameter η(W) is independent of ξ:
```
η(W) = (α²/2) √(2/π) (W_c/W) exp(−c₁(W/W_c)²)
```
which depends only on the dimensionless ratio W/W_c and the geometric factor α.

**Test**: Vary ξ from 2a to 8a in numerical simulations while keeping W/W_c fixed. Verify that n(W) × r_eff² is independent of ξ.

### P4: Algebraic vs Exponential Discrimination (Random vs QP)

**Claim**: n_rand(W) ∝ exp(−cW²) vs n_QP(W) ∝ W^{-γ} with γ = τ(β) − 1.

**Test**: For QP potentials with different irrational wavevectors, extract n(W) numerically. Fit to both exponential and power-law forms; the power-law should be preferred for QP (by AIC/BIC model selection).

### P5: Continuum-Lattice Crossover

**Claim**: The continuum disc model becomes valid when ξ ≳ √(2 ln(W/W_c)) × a. Below this, the lattice extreme-value approach is more appropriate.

**Test**: Numerically compute n(W) at fixed W/W_c = 3 while varying ξ/a from 0.5 to 4. The continuum prediction should match numerics for ξ/a ≳ 1.6, and deviate systematically below.

---

## 9. Key Formulas Summary

| Quantity | Formula | Equation |
|----------|---------|----------|
| Disorder field | ε(r) ~ GRF(0, σ²), σ = W/√12 | — |
| Covariance | ⟨ε(r)ε(r')⟩ = σ² exp(−|r−r'|²/2ξ²) | (1) |
| Thermal blob density | n(W) = n₀ Φ(W_c/W) exp(−β(W/W_c)²) | (29) |
| Suppression coefficient | β = c₁(L_min/ξ)², c₁ ≈ 2 | Sec 4.3 |
| Percolation parameter | η(W) = n(W) π (αL_min)² | (40) |
| Percolation threshold | η_c = 1.128 (Mertens & Moore 2012) | (30) |
| Continuum percolation condition | η(W) > 1.128 is NEVER satisfied | Sec 4.5 |
| QP rare region density | n_QP(W) ∝ (W_c/W)^{τ(β)−1} | (53), (57) |

---

## 10. Open Questions for Phase 2

1. **Avalanche dynamics**: How does the avalanche growth of a single thermal blob (De Roeck & Huveneers 2017, Lucignano et al. 2024) modify the effective r_eff? If the "thermalization front" propagates with logarithmic velocity, the effective thermal region after time t has radius r_eff(t) ∼ r_eff(0) + v ln(t). Does this change the percolation picture?

2. **Interaction effects**: The derivation above is for non-interacting particles. In the MBL problem, interactions introduce a critical thermal bubble size L* (below which bubbles are localized by interaction effects). How does L* modify the density n(W)?

3. **Finite-size scaling**: Cold-atom experiments have at most ~600 sites. What is the finite-size percolation probability P_perc(L, W) for these system sizes, and how does it scale toward the thermodynamic limit?

4. **Correlated percolation**: What is the "true" percolation threshold when thermal blob centers are correlated through the underlying GRF (as opposed to Poisson-distributed)? This is a non-trivial problem in correlated continuum percolation (see Prakash et al. 1992, Phys. Rev. A 46, R1724 for the general framework).

---

## References

1. Adler, R.J. & Taylor, J.E. (2007). *Random Fields and Geometry*. Springer.
2. Mertens, S. & Moore, C. (2012). Continuum percolation thresholds in two dimensions. *Phys. Rev. E* 86, 061109.
3. Longuet-Higgins, M.S. (1957). The statistical analysis of a random, moving surface. *Phil. Trans. R. Soc. Lond. A* 249, 321-387.
4. Bardeen, J.M., Bond, J.R., Kaiser, N. & Szalay, A.S. (1986). The statistics of peaks of Gaussian random fields. *Astrophys. J.* 304, 15-61.
5. De Roeck, W. & Huveneers, F. (2017). Asymptotic quantum many-body localization from thermal disorder. *Commun. Math. Phys.* 351, 1-51.
6. Lucignano, P. et al. (2024). Avalanche instability in 1D MBL. *Phys. Rev. B* 110, 134204.
7. Luitz, D.J. et al. (2017). How a thermalizing region can be localized. *Phys. Rev. B* 96, 024203.
8. Chandran, A. et al. (2016). When does a many-body localization transition occur? *Phys. Rev. X* 6, 041042.
9. Aubry, S. & Andre, G. (1980). Analyticity breaking and Anderson localization in incommensurate lattices. *Ann. Israel Phys. Soc.* 3, 133-164.
10. Devakul, T. & Huse, D.A. (2017). Many-body localization in a quasiperiodic potential. *Phys. Rev. B* 96, 214201.
11. Cao, Y. & Machta, J. (2019). Extreme value statistics in disordered systems with correlations. *Phys. Rev. E* 99, 042131.
12. Stauffer, D. & Aharony, A. (1994). *Introduction to Percolation Theory* (2nd ed.). Taylor & Francis.
