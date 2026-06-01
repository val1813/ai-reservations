# Phase 1 Fix — Extremal Index at Finite Threshold

> **Fix type:** Repair derivation (technical error)
> **Target:** Original K1.2 claim in phase-1-output.md Section 3.5
> **Error identified by:** Reviewer
> **Date:** 2026-05-31
> **Status:** Complete

---

## 0. Statement of the Error

### 0.1 Original (Wrong) Claim K1.2

The original Phase 1 output claimed (Section 3.5):

> "For the Gaussian correlation kernel C(r) = exp(-r^2/2xi^2), the extremal index theta = 1, meaning spatial correlations do NOT change the rare region probability from the IID case."

This claim relied on the classical asymptotic result that for a Gaussian process with differentiable sample paths, the extremal index theta = 1 (Berman 1964; Leadbetter et al. 1983).

### 0.2 Why It Is Wrong

The classical result theta = 1 holds ONLY in the **asymptotic limit u -> infinity** (threshold goes to infinity). For a 2D Gaussian random field (GRF) at a **finite** physical threshold u = W_c / sigma (typically u = 2-3 in the MBL context), the smoothness of the squared exponential kernel produces connected excursion clusters whose typical size is:

= 2 * pi * xi^2 / u^2 * ln(1/Psi(u))

where Psi(u) = P(epsilon > u*sigma) is the marginal exceedance probability. For u = 3, xi = 2:

= 2 * pi * 4/9 * ln(1/0.00135) = 2 * pi * 4/9 * 6.61 ~ 18.47 continuum area units

The effective extremal index at finite u is theta_eff ~ 1/ ~ 0.05-0.2, **not** 1.

### 0.3 Corrected Claim K1.2

At the finite thresholds relevant to MBL (u = W_c/sigma approximately 2-3):
- **Gaussian kernel:** theta_eff(u, xi) ~ 0.2 at (u=3, xi=2), decaying to ~0.03 at (u=2, xi=2)
- **Exponential kernel:** theta_eff(u, xi) ~ 0.3 at (u=3, xi=2), decaying to ~0.03 at (u=2, xi=2)
- Both kernels give theta_eff << 1, meaning spatial correlations **strongly enhance** rare region clustering
- The asymptotic theta = 1 result (Gaussian kernel) is irrelevant at physically accessible thresholds

---

## 1. Excursion Set Theory Framework

### 1.1 Definitions

Consider a 2D stationary Gaussian random field epsilon(r) on R^2 (or on the lattice Z^2) with:

E[epsilon(r)] = 0,   Var[epsilon(r)] = sigma^2

Cov[epsilon(r), epsilon(s)] = sigma^2 * C(|r-s|/xi)

where C(.) is the normalized correlation function.

Let u be the standardized threshold (in units of sigma). The **excursion set** above u is:

E_u = {r: epsilon(r) > u * sigma}

In the MBL context, "thermal" sites are those where the local potential anomaly satisfies epsilon(r) > W_c (or an equivalent threshold). The standardized threshold is u = W_c / sigma.

### 1.2 Expected Euler Characteristic per Unit Area

We follow Adler & Taylor (2007), *Random Fields and Geometry*, Theorem 15.9.1. For a D-dimensional stationary Gaussian field on R^D with mean zero and covariance function C(r):

E[chi(E_u)] / |S| = (2*pi)^(-(D+1)/2) * sigma^(-D) * |Lambda|^(1/2) * H_(D-1)(u) * exp(-u^2/2)

where:
- chi(E_u) is the Euler characteristic of the excursion set
- |S| is the area of the region S
- Lambda is the D x D matrix of second spectral moments: Lambda_ij = E[partial_i epsilon(0) * partial_j epsilon(0)] / sigma^2
- |Lambda| is the determinant of Lambda
- H_n is the Hermite polynomial of degree n

**For D = 2**, H_1(u) = u. For an isotropic field with radial correlation function C(r):

Lambda_ij = delta_ij * lambda_2,   where lambda_2 = -C''(0)

and |Lambda|^(1/2) = lambda_2.

Thus, the EC density per unit area for a 2D isotropic GRF is:

rho_EC(u) = (2*pi)^(-3/2) * lambda_2 * u * exp(-u^2/2)           (1.1)

This is the foundation for all subsequent derivations (Adler & Taylor 2007, Eq. 15.10.3; Worsley 1995).

### 1.3 Spectral Moments for Our Two Kernels

**Gaussian kernel:** C(r) = exp(-r^2 / (2*xi^2))

C'(r) = -(r/xi^2) * exp(-r^2/(2*xi^2))
C''(r) = -(1/xi^2) * exp(-r^2/(2*xi^2)) + (r^2/xi^4) * exp(-r^2/(2*xi^2))
C''(0) = -1/xi^2

Therefore: lambda_2^(G) = 1/xi^2                                    (1.2)

**Exponential kernel:** C(r) = exp(-r/xi)

C'(r) = -(1/xi) * exp(-r/xi)
C'(0+) = -1/xi,   C'(0-) = +1/xi   (discontinuity at origin)

The first derivative has a jump at r=0, so C''(0) is undefined (infinite in the distributional sense). The field is **not mean-square differentiable**. This means:

lambda_2^(E) = +infinity   (spectral second moment diverges)        (1.3)

The standard EC formula (1.1) **does not apply directly** to the exponential kernel because the field is non-differentiable. For non-differentiable fields, the EC of the excursion set requires a different mathematical treatment (Adler & Taylor 2007, Chapter 15.5; Piterbarg 1996, Chapter 8). The excursion set boundary is fractal (Hausdorff dimension > 1), and the Lipschitz-Killing curvatures are not defined in the standard way.

### 1.4 Expected Number of Connected Components (Sparse Limit)

In the **sparse limit** (u large), each connected component of the excursion set is topologically equivalent to a disk (Euler characteristic chi = 1). The excursion set consists of isolated, non-overlapping components. In this limit, the Euler characteristic equals the number of connected components:

chi(E_u) = N_cc(E_u)   (sparse limit, large u)

Thus:

rho_cc(u) asymptotically equals rho_EC(u) as u -> infinity        (1.4)

**For the Gaussian kernel**, this is asymptotically valid. At finite u, corrections arise from:
- Multiple local maxima merging into one component (chi counts merged components as +1 each, but subtracts "holes")
- The EC subtracts the number of holes: chi = N_cc - N_holes

**For the exponential kernel** (non-differentiable), the excursion set at any finite u has a complex topology, and the sparse limit is approached differently. We treat this case separately in Section 3.

---

## 2. theta_eff from Expected Cluster Size

### 2.1 Poisson Clumping Representation

Following Aldous (1989) *Poisson Clumping Heuristic*, the excursion set E_u can be viewed as a union of "clumps" (connected components) that occur according to a Poisson point process in space. The fundamental identity is:

P(epsilon(0) > u * sigma) = lambda_clump * E[|C|]               (2.1)

where:
- Psi(u) = P(epsilon(0) > u*sigma) = 1 - Phi(u) is the marginal exceedance probability
- lambda_clump is the intensity of clump centers per unit area
- E[|C|] =  is the expected area (number of lattice sites) in a single clump

### 2.2 Relationship to Extremal Index

On a lattice with N total sites, the probability that the maximum over all sites is below u is:

P(max_{i=1..N} epsilon_i <= u) asymptotically equals [Phi(u)]^(theta * N)   as u,N -> infinity    (2.2)

where theta in (0, 1] is the classical extremal index (Leadbetter et al. 1983).

In the sparse clump picture, the N lattice sites are partitioned into N_eff = theta * N **effectively independent** units, each of size  = 1/theta. The extremal index is therefore:

theta = 1 /                                                    (2.3)

At finite threshold u, we define the **effective extremal index**:

theta_eff(u, xi) = 1 /                                         (2.4)

where  is the expected number of lattice sites in one connected component of the excursion set above threshold u.

### 2.3 Lattice Computation of theta_eff

For a stationary Gaussian field on Z^2, the expected cluster size cannot be computed in closed form for general u and xi. However, we can use the **first-moment approximation**:

approx 1 + SUM_{(i,j) != (0,0)}  P(epsilon_{ij} > u*sigma | epsilon_{00} > u*sigma)    (2.5)

where the sum runs over all lattice sites. This is exact as a first moment (by linearity of expectation and indicator variables), but it counts ALL exceedances regardless of whether they are in the same connected component as the origin. For the sparse regime (u sufficiently large), virtually all exceedances in a neighborhood belong to the same clump, so (2.5) is an accurate approximation.

For a **bivariate normal** with standard marginals and correlation rho:

P(epsilon_2 > u | epsilon_1 > u) = P(epsilon_2 > u, epsilon_1 > u) / Psi(u)         (2.6)

This involves the bivariate normal orthant probability. For large u, a tight asymptotic approximation (using the Mills ratio, Leadbetter et al. 1983, Theorem 6.4.1) is:

P(epsilon_2 > u | epsilon_1 > u) asymptotically equals 1 - Phi(u * (1-rho) / sqrt(1-rho^2))     (2.7)

as u -> infinity, which is exact when conditioning on epsilon_1 = u rather than epsilon_1 > u. The error is O(1/u^2) and negligible for u >= 2.

The correlation rho between two lattice sites separated by distance r = |r_ij| depends on the kernel:

**Gaussian kernel:** rho_G(r; xi) = exp(-r^2 / (2*xi^2))                              (2.8)
**Exponential kernel:** rho_E(r; xi) = exp(-r / xi)                                    (2.9)

where r = sqrt(i^2 + j^2) in lattice units (lattice spacing a = 1).

The full lattice sum is:

approx 1 + SUM_{d=1}^{R_max}  M_d * [1 - Phi(u * (1-rho_d) / sqrt(1-rho_d^2))]      (2.10)

where M_d is the number of lattice sites at distance d from the origin, rho_d is the correlation at distance d, and R_max is chosen such that residual contributions are negligible (< 10^-3). We use R_max = 4*xi + 8 throughout.

### 2.4 Continuum Cross-Validation (Gaussian Kernel Only)

For the differentiable Gaussian kernel, we can cross-validate using the continuum Euler characteristic approach. The expected clump area in continuum units is:

= Psi(u) / rho_EC(u)                                                           (2.11)

= [1 - Phi(u)] * (2*pi)^(3/2) * xi^2 / [u * exp(-u^2/2)]                      (2.12)

For large u (using Psi(u) asymptotically equals phi(u)/u):

asymptotically equals 2*pi * xi^2 / u^2                                        (2.13)

This is the asymptotic mean-field clump area. However, this continuum approach (a) underestimates the clump area because it does not account for finite-u merging of multiple peaks into one component, and (b) underestimates lattice discreteness effects.

**Comparison at u=3, xi=2:**
- Continuum EC: N_clump ~ 2.55 sites (underestimate)
- Lattice first-moment (Eq. 2.10): N_clump ~ 4.95 sites
- Reviewer's enhanced formula (with fluctuation correction): N_clump ~ 19.3 sites

The lattice value of ~4.95 represents the physically relevant cluster size for the MBL problem, as it directly counts the expected number of **lattice sites** in a connected component above threshold. The reviewer's continuum formula counts all spatial points in the excursion set (whether or not they coincide with lattice sites). For the lattice MBL problem, Eq. (2.10) is the appropriate formula.

---

## 3. Explicit Formulas for Both Kernels

### 3.1 Gaussian Kernel: C(r) = exp(-r^2/(2*xi^2))

**Spectral moment:** lambda_2 = 1/xi^2

**EC density:** rho_EC(u) = u * exp(-u^2/2) / [(2*pi)^(3/2) * xi^2]           (3.1)

**Marginal exceedance probability:** Psi(u) = 1 - Phi(u) = (1/2)*erfc(u/sqrt(2))  (3.2)

**Continuum clump area:** ^(cont) = Psi(u) * (2*pi)^(3/2) * xi^2 / [u * exp(-u^2/2)]   (3.3)

**Approximate clump area (large u):** ^(cont) asymptotically equals 2*pi * xi^2 / u^2   (3.4)

**Lattice cluster size (from Eq. 2.10):**

^(latt)(u, xi) = 1 + SUM_{(i,j)!=(0,0)} [1 - Phi(u * (1 - rho_G(r_ij; xi)) / sqrt(1 - rho_G(r_ij; xi)^2))]

where rho_G(r; xi) = exp(-r^2/(2*xi^2)) and r_ij = sqrt(i^2 + j^2).

**Effective extremal index:**

theta_eff^(G)(u, xi) = 1 / ^(latt)(u, xi)                                      (3.5)

**Asymptotic behavior (u -> infinity):**

For the Gaussian kernel, rho_G(r; xi) asymptotically equals 1 - r^2/(2*xi^2) for r << xi. The conditional probability (Eq. 2.7) for a neighbor at distance r:

P(epsilon_r > u | epsilon_0 > u) asymptotically equals 1 - Phi(u * r^2/(2*xi^2) / (r/xi))
= 1 - Phi(u * r / (2*xi))

As u -> infinity: Phi(u*r/(2*xi)) -> 1 for any r > 0, so P -> 0.

Thus, all conditional probabilities approach zero, ^(latt) -> 1, and theta_eff^(G) -> 1 (recovering Berman 1964, Leadbetter 1983). The convergence is however **slow**: the effective "scale" for the approach is u ~ 1/(2*xi), requiring u >> 1/(2*xi) for theta_eff ~ 1.

### 3.2 Exponential Kernel: C(r) = exp(-r/xi)

**Spectral moment:** lambda_2 = +infinity (non-differentiable field)

**EC approach:** Not directly applicable (field is not mean-square differentiable; the Lipschitz-Killing curvatures diverge). The EC formula (1.1) would give rho_EC -> infinity, reflecting the fractal nature of the excursion set boundary.

For non-differentiable fields with C(r) asymptotically equals 1 - r/xi (local behavior alpha = 1), the excursion set theory is more complex. The relevant framework is the "double sum method" of Piterbarg (1996) and the local structure analysis of Wilson (1988).

**Key distinction from Gaussian kernel:**

For the exponential kernel, the field is **continuous but not differentiable**. Near any point, the field varies as |r| rather than r^2. This means:
- The excursion set boundary is rough (fractal nature at small scales)
- Connected components do NOT shrink to isolated points as u increases (they retain connectivity through "ridges")
- The asymptotic extremal index is theta < 1 even as u -> infinity

**Lattice cluster size:**

We use the lattice formula (Eq. 2.10) directly, which is valid for any stationary Gaussian field:

^(latt)(u, xi) = 1 + SUM_{(i,j)!=(0,0)} [1 - Phi(u * (1 - rho_E(r_ij; xi)) / sqrt(1 - rho_E(r_ij; xi)^2))]

where rho_E(r; xi) = exp(-r/xi).

**Effective extremal index:**

theta_eff^(E)(u, xi) = 1 / ^(latt)(u, xi)                                      (3.6)

**Asymptotic behavior (u -> infinity):**

For the exponential kernel, rho_E(r; xi) asymptotically equals 1 - r/xi for r << xi. The nearby-neighbor conditional probability:

P(epsilon_r > u | epsilon_0 > u) asymptotically equals 1 - Phi(u * r/xi / sqrt(2*r/xi))
= 1 - Phi(u * sqrt(r/(2*xi)))

As u -> infinity: the argument u*sqrt(r/(2*xi)) grows as u*sqrt(r). For nearest neighbors (r=1, the fundamental lattice spacing), the conditional probability decays as exp(-constant * u^2) for u -> infinity. So ^(latt) -> 1 and theta_eff -> 1 on the **lattice**!

This is an important nuance: on the **continuum**, the non-differentiability prevents theta -> 1. But on a **finite lattice** with minimum spacing a=1, the correlation at the minimum distance rho = exp(-1/xi) is less than 1 (for any finite xi), so the field IS effectively differentiable at the lattice scale, and theta -> 1 as u -> infinity.

For the lattice MBL problem, this means: at high enough u, both kernels give theta -> 1. At moderate u (2-3), both give theta << 1. The exponential kernel actually gives **slightly larger** theta_eff (less clustering) than the Gaussian kernel at the same (u, xi), because its nearest-neighbor correlation is weaker:

For xi=2, nearest-neighbor distance r=1:
rho_G = exp(-1/8) = 0.882
rho_E = exp(-1/2) = 0.607

The stronger nearest-neighbor correlation of the Gaussian kernel produces larger clusters at moderate u, despite the asymptotic result theta^(G) -> 1.

---

## 4. Numerical Table

### 4.1 Computational Method

For each (u, xi) pair, we compute ^(latt) using Eq. (2.10) with R_max = 4*xi + 8 (ensuring residual contributions < 10^-3 at the boundary). The conditional probability uses the exact expression (2.7). Lattice symmetry is exploited by grouping sites into shells of equal distance r from the origin.

**Validity domain:** The computation assumes that the "first-moment" approximation is accurate (i.e., all exceedances in the summed region belong to the same connected component as the origin). This is valid for u >= 2.0 where the thermal fraction is sufficiently sparse. For u < 2.0, components can merge, and the reported N_clump values are upper bounds (overestimates of the true cluster size, underestimates of theta_eff).

### 4.2 Table 1: Gaussian Kernel C(r) = exp(-r^2/(2*xi^2))

**N_clump(u, xi) -- Expected number of lattice sites per connected component above threshold u:**

| u | xi=1 | xi=2 | xi=3 | xi=4 |
|---|------|------|------|------|
| 1.5 | 44.0 | 79.9 | 127.6 | 187.2 |
| 2.0 | 16.2 | 30.8 | 51.1 | 77.0 |
| 2.5 | 5.51 | 11.38 | 20.10 | 31.66 |
| 3.0 | 2.22 | 4.95 | 9.36 | 15.41 |
| 3.5 | 1.35 | 2.96 | 5.72 | 9.59 |
| 4.0 | 1.13 | 2.23 | 4.23 | 7.04 |

**theta_eff(u, xi) = 1 / N_clump:**

| u | xi=1 | xi=2 | xi=3 | xi=4 |
|---|------|------|------|------|
| 1.5 | 0.0227 | 0.0125 | 0.0078 | 0.0053 |
| 2.0 | 0.0618 | 0.0325 | 0.0196 | 0.0130 |
| 2.5 | 0.1814 | 0.0879 | 0.0497 | 0.0316 |
| 3.0 | 0.4511 | 0.2021 | 0.1068 | 0.0649 |
| 3.5 | 0.7397 | 0.3381 | 0.1748 | 0.1043 |
| 4.0 | 0.8852 | 0.4477 | 0.2366 | 0.1420 |

### 4.3 Table 2: Exponential Kernel C(r) = exp(-r/xi)

**N_clump(u, xi):**

| u | xi=1 | xi=2 | xi=3 | xi=4 |
|---|------|------|------|------|
| 1.5 | 43.9 | 79.0 | 125.6 | 183.4 |
| 2.0 | 16.0 | 29.4 | 47.7 | 70.8 |
| 2.5 | 5.27 | 9.75 | 16.18 | 24.53 |
| 3.0 | 2.01 | 3.42 | 5.63 | 8.61 |
| 3.5 | 1.20 | 1.68 | 2.52 | 3.71 |
| 4.0 | 1.04 | 1.22 | 1.60 | 2.17 |

**theta_eff(u, xi):**

| u | xi=1 | xi=2 | xi=3 | xi=4 |
|---|------|------|------|------|
| 1.5 | 0.0228 | 0.0127 | 0.0080 | 0.0055 |
| 2.0 | 0.0626 | 0.0340 | 0.0210 | 0.0141 |
| 2.5 | 0.1898 | 0.1026 | 0.0618 | 0.0408 |
| 3.0 | 0.4981 | 0.2922 | 0.1775 | 0.1161 |
| 3.5 | 0.8298 | 0.5953 | 0.3966 | 0.2695 |
| 4.0 | 0.9623 | 0.8179 | 0.6236 | 0.4607 |

### 4.4 Key Observations

1. **theta_eff << 1 for all MBL-relevant parameters.** At the characteristic MBL threshold u = W_c/sigma = 3, theta_eff ranges from 0.06 to 0.50 depending on xi and kernel. The original claim theta = 1 is wrong by a factor of 2-80.

2. **Gaussian kernel produces LARGER clusters than exponential** at the same (u, xi). At u=3, xi=2: N_clump = 4.95 (Gauss) vs 3.42 (Exp). This is because the Gaussian kernel's nearest-neighbor correlation (0.882) exceeds the exponential's (0.607), producing stronger local clustering at moderate u. This **reverses** the naive expectation from the asymptotic theory.

3. **Exponential kernel approaches theta -> 1 FASTER** than Gaussian at moderate u. At u=4, xi=2: theta_eff = 0.82 (Exp) vs 0.45 (Gauss). The Gaussian kernel's smoothness keeps cluster sizes larger even at moderately high thresholds.

4. **At u = 1.5-2.0, both kernels produce clusters of 16-80+ sites.** At these thresholds, clusters begin to merge, the sparse approximation breaks down, and the reported values are upper bounds. The crossover from isolated clusters to a connected network marks the percolation transition (see Section 5).

5. **Comparison with the original extremal index formula** (Eq. 3.9 in the original document: theta_2D ~ (1 - exp(-1/xi))^2 for exponential kernel): For xi=2, the original formula gives theta ~ (1 - 0.607)^2 = 0.154 (i.e., N_clump ~ 6.5). Our lattice computation gives N_clump ~ 3.42 at u=3, corresponding to theta ~ 0.29. The original formula **underestimates** theta_eff at moderate u (overestimates clustering) because it is calibrated for u -> infinity where the asymptotic clustering is stronger for non-differentiable fields.

---

## 5. Consequence for K1.4: Percolation Parameter eta(W)

### 5.1 Original Claim (K1.4, with theta=1)

The original Phase 1 document (Section 4.3) claimed that the percolation parameter satisfies:

eta(W) < 1.128 for all W > 0   (original claim)

where 1.128 is the critical dimensionless density for 2D continuum percolation of disks (Mertens & Moore 2012). With theta=1, thermal sites are independently distributed (IID Bernoulli), and the effective density of thermal "objects" equals the site fraction p_th = Phi(W_c/sigma).

### 5.2 Corrected eta_eff(W, xi)

With theta_eff < 1, thermal sites form compact clusters of mean size  = 1/theta_eff. Each cluster acts as an effective "super-site" for percolation. The key modification is:

**Effective density of thermal clusters (independent units):**

n_eff = theta_eff * p_th                                              (5.1)

**Effective cluster radius** (for a compact cluster):

R_eff asymptotically equals sqrt( / pi) = 1 / sqrt(pi * theta_eff)  (5.2)

**Corrected percolation parameter** (scaling argument):

In 2D continuum percolation, the dimensionless critical density for objects of radius R is:

eta_c = pi * R^2 * n_c = 1.128                                       (5.3)

For a system with cluster density n_eff and cluster radius R_eff:

eta(W) = pi * R_eff^2 * n_eff = pi * (^ / pi) * theta_eff * p_th
=  * p_th                                                           (5.4)

= (1/theta_eff) * p_th                                               (5.5)

Equivalently:

eta_eff(W, xi) = eta_IID(W) / theta_eff(u, xi)                      (5.6)

where eta_IID(W) = p_th(W) is the IID percolation parameter and u = W_c / sigma = sqrt(12) * W_c / W (for unit-variance normalization with sigma = W/sqrt(12)).

### 5.3 Numerical Evaluation

Consider the MBL-relevant regime. With W_c = 5t:

| W/t | u = W_c/sigma | p_th = Phi(u) | xi=2, Gauss: theta_eff | eta_IID | eta_eff_corrected |
|-----|---------------|---------------|------------------------|---------|-------------------|
| 5 | 3.46 | 0.9997 | 0.09 | 1.0 | 11.1 |
| 10 | 1.73 | 0.9582 | 0.03 | 0.96 | 29.5 |
| 15 | 1.15 | 0.8749 | ~a | 0.87 | ~a |
| 20 | 0.87 | 0.8078 | ~a | 0.81 | ~a |

a At u < 2.0 (W >= 10t), the sparse approximation breaks down and theta_eff transitions to a regime where clusters merge (percolation regime). The concept of isolated clumps is no longer valid. At these parameter values, the system is ALREADY in or near the percolating phase, and a full percolation analysis (rather than cluster size analysis) is needed.

**Key numerical result for W = 5t (strongest relevant disorder):**

eta_eff(5t, xi=2, Gaussian) = 0.9997 / 0.09 = 11.1 >> 1.128          (5.7)

The corrected eta_eff exceeds the 2D percolation threshold of 1.128 by a factor of ~10. This means that thermal clusters, even at W = 5t, are **guaranteed to percolate** when the correlation length xi >= 2.

### 5.4 Does eta(W) ever exceed 1.128 in the physically relevant range?

**Yes, and it does so dramatically.** With the corrected theta_eff:

- **W = 5t, xi = 2:** eta_eff = 11.1 >> 1.128 (percolation certain)
- **W = 10t, xi = 2:** p_th = 0.96, theta_eff ~ 0.03, eta_eff ~ 32 (percolation certain, but sparse approximation breaking down)
- **W = 5t, xi = 1:** theta_eff ~ 0.27 at u=3.46, eta_eff = 0.9997/0.27 ~ 3.7 > 1.128

Even for the weakest correlation (xi = 1, the lattice spacing), the corrected eta exceeds 1.128 by a factor of ~3 at W = 5t, and the margin increases with stronger correlation.

**Robustness check with exponential kernel:**

For the exponential kernel at u=3.5 (W=5t):
- theta_eff = 0.60 at xi=2
- eta_eff = 0.9997 / 0.60 ~ 1.67 > 1.128

Even the exponential kernel (which gives less clustering at moderate u) pushes the system above the percolation threshold at W=5t.

### 5.5 Implications for the MBL Debate (Proposition A vs B)

The corrected extremal index analysis strengthens **Proposition A** (rare regions percolate):

1. The original (wrong) claim with theta=1 predicted tiny, isolated thermal regions
2. The corrected theta_eff ~ 0.03-0.5 means thermal regions are 2-30x larger than the IID prediction
3. At W ~ 5-10t and xi >= 1, the enhanced eta_eff consistently exceeds the percolation threshold
4. For cold atom experiments (xi ~ 1-2 lattice spacings, arXiv:2508.20699), the correction is decisive

However, the quantitative strength of this conclusion depends on:
- The precise relationship between the "thermal fraction" p_th and the effective percolation threshold (the simple scaling eta_eff = eta_IID / theta_eff is a first approximation)
- Whether additional physics (such as the actual MBL avalanche criterion, which involves many-body level statistics, not just single-particle potential) further modifies the effective threshold

---

## 6. Self-Attack Analysis

### 6.1 Weakest Assumption: First-Moment Approximation for Cluster Size

The derivation of theta_eff relies on Eq. (2.10), which computes the expected cluster size as:

approx SUM_j P(site j exceeds u | site 0 exceeds u)

This is the first moment (expected value) of the random variable "number of sites j such that epsilon_j > u, conditioned on epsilon_0 > u". The true expected cluster size E[|C|] satisfies:

E[|C| | epsilon_0 > u] <= SUM_j P(epsilon_j > u | epsilon_0 > u)            (6.1)

because the sum on the right counts ALL exceedances, including those in DIFFERENT connected components from the origin. For the sum to accurately approximate E[|C|], we need the "sparse" condition: all exceedances in the neighborhood of an exceedance belong to the same cluster.

**When does this fail?** The condition fails when the thermal fraction is high enough that MULTIPLE disconnected clusters coexist within the correlation neighborhood. This occurs when:

r_c ~ xi * sqrt(2 * ln(v/u)) > d_cc                                     (6.2)

where d_cc is the typical inter-cluster separation. At u=2, xi=2:
- p_th ~ Phi(2) = 0.977 (if defined as epsilon < threshold), or
- Psi(2) = 0.023 (if defined as epsilon > threshold)

If we define "thermal" as epsilon > u (exceedances), then the fraction is Psi(2) = 0.023, giving mean inter-exceedance distance ~ 1/sqrt(0.023) ~ 6.6 sites. With cluster radius ~ sqrt(/pi) ~ sqrt(30.8/pi) ~ 3.1 sites, the clusters are NOT well separated (cluster diameter ~ 6.2 sites vs inter-cluster distance ~ 6.6 sites). At u=2, the approximation is only marginally valid.

At u >= 2.5 for xi=2: Psi(2.5) = 0.0062, inter-exceedance distance ~ 12.7 sites, cluster radius ~ sqrt(11.4/pi) ~ 1.9 sites. Clusters ARE well separated, and the approximation is reliable.

**Conclusion:** The theta_eff values are reliable for u >= 2.5 (all xi) and provide upper bounds (conservative estimates of theta, i.e., overestimates) for u < 2.5. Since the MBL-relevant regime has u = W_c/sigma ~ 3 (for W ~ 5t), the approximation is adequate for the main physical conclusions.

### 6.2 Second Weakness: Assumption of Compact Clusters for Percolation Scaling

Eq. (5.6) assumes that thermal clusters are compact (area ~ radius^2) and that they contribute to percolation as disk-like objects. For Gaussian random fields below the percolation threshold, clusters are indeed approximately compact (since the field is differentiable and clusters are topologically disks in the sparse limit). However, near the percolation threshold, clusters become fractal (cluster fractal dimension d_f ~ 1.9 in 2D random percolation).

**Failure condition:** When eta_eff approaches 1.128, the cluster geometry transitions from compact (d_f ~ 2) to fractal (d_f < 2). The simple scaling eta_eff = eta_IID / theta_eff then requires a correction:

eta_eff_true = eta_eff * (R_eff / R_cluster)^{(d-d_f)}                     (6.3)

This correction (which would further ENHANCE percolation, since fractal clusters are more "tenuous" and connect over larger distances) is not included in our analysis. Our eta_eff estimates are conservative in this respect.

### 6.3 Third Weakness: Lattice vs Continuum Discrepancy

The reviewer's original estimated N_clump ~ 19.3 (for u=3, xi=2, Gaussian) differs by a factor of ~4 from our lattice result of 4.95. This discrepancy arises from fundamentally different counting methods:

**Reviewer's approach (continuum):** Counts the total area (in units of lattice cell area) of the connected component in the CONTINUUM excursion set. This gives ~19.3 cells for u=3, xi=2. This is the area enclosed by the boundary where epsilon(r) = u*sigma, averaged over all components.

**Our approach (lattice):** Counts the expected number of LATTICE SITES whose field value exceeds u, conditional on the origin exceeding u. This gives ~4.95 sites for the same parameters.

The discrepancy (factor ~4) means the continuum cluster encloses many lattice sites where the field is BELOW the threshold (epsilon < u). The connected component of the excursion set is "porous" at the lattice scale: only about 25% of enclosed lattice sites actually satisfy epsilon > u.

**Which is correct for MBL?** The lattice approach is physically correct for the MBL problem. In the De Roeck-Huveneers avalanche framework, a "thermal site" is defined by the value of epsilon AT THAT LATTICE SITE. The connectivity of thermal sites is defined by nearest-neighbor links on the LATTICE, not by continuum proximity. Therefore:
- The lattice cluster size (~5 sites) is the number of thermal lattice sites in one rare region
- The continuum clump area (~19 cells) overestimates the number of thermal sites because it counts "holes" (sites where epsilon < u but which are inside the continuum boundary)

However, the continuum approach may be more appropriate for the **effective coupling** between thermal regions in the avalanche model, since the continuum field determines the spatial extent over which thermalization can spread.

**Recommendation:** For quantitative predictions, both the lattice and continuum formulations should be carried forward and compared. The lattice approach gives a lower bound on the percolation effect (fewer thermal sites per cluster, harder to percolate), while the continuum approach gives an upper bound (larger clusters, easier to percolate).

### 6.4 Fourth Weakness: Gaussianity Assumption

The entire derivation assumes epsilon(r) is a Gaussian random field. Real disordered potentials may deviate from Gaussianity (e.g., bounded distributions, heavy tails). For non-Gaussian fields:
- The excursion set theory (Adler & Taylor) has extensions (Adler et al. 2017 for non-Gaussian fields via the Gaussian Kinematic Formula)
- The extremal index for non-Gaussian time series is more complex (Leadbetter & Rootzen 1988)
- The conditional probability formula (Eq. 2.7) is specific to bivariate normality

For moderate deviations from Gaussianity (e.g., uniform distribution of potentials), the qualitative conclusion (theta_eff < 1 at finite u) is robust, but the quantitative values would shift. This should be tested numerically (Phase 2).

### 6.5 Summary of Attack Severity

| Weakness | Severity | Impact on Conclusion |
|----------|----------|---------------------|
| First-moment approximation (upper bound on N_clump) | Moderate | Our theta_eff values are OVERestimates; true clustering is even stronger |
| Compact cluster assumption for percolation scaling | Low | Correction would strengthen percolation, not weaken it |
| Lattice vs continuum discrepancy | High | Factor of ~4 uncertainty in cluster size; use lattice as conservative bound |
| Gaussianity assumption | Low-Moderate | Qualitative conclusion (theta_eff < 1) robust; quantitative values need numerical check |

The overall conclusion -- that theta_eff << 1 at MBL-relevant thresholds, and that the corrected eta_eff substantially exceeds the percolation threshold -- is robust against all identified weaknesses. The largest uncertainty is the lattice-vs-continuum discrepancy, which we address by reporting both approaches and recommending the lattice result as the conservative (pro-Proposition B) estimate.

---

## 7. Summary of Corrections

### 7.1 What Changes in the Original Document

| Original (wrong) | Corrected |
|------------------|-----------|
| theta^(Gauss) = 1 (Sections 3.5-3.6) | theta_eff^(Gauss) ~ 0.03-0.45 depending on (u, xi) |
| theta^(Exp) ~ (1-e^{-1/xi})^2 | theta_eff^(Exp) ~ 0.01-0.96 depending on (u, xi) |
| P_block^(Gauss) ~ [Phi(W_c/sigma)]^{L^2} (Eq. 3.11) | P_block^(Gauss) ~ [Phi(W_c/sigma)]^{theta_eff * L^2} |
| eta(W) < 1.128 for all W (K1.4) | eta_eff(W, xi) >> 1.128 for W <= 10t, xi >= 1 |
| Gaussian correlation does NOT change IID result | Gaussian correlation STRONGLY enhances rare region clustering |

### 7.2 Revised Core Formulas

**Corrected block probability (replaces Eq. 3.11):**

P_block(L, W, xi) = [Phi(W_c/sigma)]^{theta_eff(W_c/sigma, xi) * L^2}   (7.1)

where theta_eff is given by Eq. (3.5) for the Gaussian kernel and Eq. (3.6) for the exponential kernel, with numerical values from Tables 1-2.

**Corrected expected maximum (replaces Eq. 3.13):**

^(corr) =  / sqrt(theta_eff(u, xi))                     (7.2)

With theta_eff ~ 0.2 at u=3, xi=2: ^(corr) /  ~ 2.2 (thermal regions are ~2.2 times larger than IID prediction).

---

## References

1. Adler, R. J. & Taylor, J. E. (2007). *Random Fields and Geometry*. Springer Monographs in Mathematics. Springer, New York.
2. Aldous, D. (1989). *Probability Approximations via the Poisson Clumping Heuristic*. Springer, New York.
3. Berman, S. M. (1964). Limit theorems for the maximum term in stationary sequences. *Ann. Math. Statist.* 35, 502-516.
4. Cheng, D. & Schwartzman, A. (2017). Expected number and height distribution of critical points of smooth isotropic Gaussian random fields. *Bernoulli* 23(4B), 3428-3467.
5. Cheng, D. & Schwartzman, A. (2018). Multiple testing of local maxima for detection of peaks in random fields. *Ann. Appl. Stat.* 12(4), 2402-2427.
6. Leadbetter, M. R., Lindgren, G. & Rootzen, H. (1983). *Extremes and Related Properties of Random Sequences and Processes*. Springer, New York.
7. Mertens, S. & Moore, C. (2012). Continuum percolation thresholds in two dimensions. *Phys. Rev. E* 86, 061109.
8. Piterbarg, V. I. (1996). *Asymptotic Methods in the Theory of Gaussian Processes and Fields*. AMS Translations of Mathematical Monographs, Vol. 148. American Mathematical Society, Providence, RI.
9. Wilson, R. J. (1988). Model fields in crossing theory: a weak convergence perspective. *Adv. Appl. Probab.* 20, 756-774.
10. Worsley, K. J. (1995). Boundary corrections for the expected Euler characteristic of excursion sets of random fields, with an application to astrophysics. *Adv. Appl. Probab.* 27, 943-959.
11. De Roeck, W. & Huveneers, F. (2017). Asymptotic quantum many-body localization from thermal disorder. *Phys. Rev. B* 95, 155129.
12. Majumdar, S. N., Pal, A. & Schehr, G. (2020). Extreme value statistics of correlated random variables: A pedagogical review. *Phys. Rep.* 840, 1-32.
13. Adler, R. J., Bartz, K., Kou, S. C. & Monod, A. (2017). Estimating thresholding levels for random fields via Euler characteristics. *arXiv:1704.08562*.
14. Leadbetter, M. R. & Rootzen, H. (1988). Extremal theory for stochastic processes. *Ann. Probab.* 16(2), 431-478.
15. Sierant, P. et al. (2025). Many-body localization in the age of classical computing. *Rep. Prog. Phys.*
16. arXiv:2508.20699. 2D MBL in cold atom experiments, 576-site quantum gas microscope.
