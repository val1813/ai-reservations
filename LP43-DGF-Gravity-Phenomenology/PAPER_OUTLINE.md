# DGF: Gravity as Quantum Information

## Abstract

We show that the gravitational potential can be expressed as the logarithm of a quantum channel fraction: q = exp(-GM/rc²), where q ∈ [0,1] is the openness of quantum information channels on a causal graph. This mapping is derived from the renormalization group flow of the causal graph under coarse-graining (ln q additivity). Combined with the equivalence principle and spatial isotropy — which fix the metric's coupling to q — the resulting effective theory recovers general relativity at Newtonian and first post-Newtonian orders, and predicts a 4.07% deviation in the second post-Newtonian binding energy coefficient. This deviation produces a cumulative gravitational-wave phase shift of ~0.7 rad for GW170817-like events and ~1.9 rad for next-generation detectors, offering a parameter-free, falsifiable test of the information-theoretic origin of gravity.

## 1. Introduction

- Gravity remains the only fundamental force without a quantum-information formulation
- Previous work: Jacobson (1995) derived Einstein equations from thermodynamics; Verlinde (2011, 2017) proposed entropic/emergent gravity; Padmanabhan established the emergent gravity paradigm
- DGF takes a different approach: gravity IS quantum information — specifically, the gravitational potential IS the logarithm of quantum channel openness
- This paper: derive q = exp(-Φ/c²) from causal graph RG flow, combine with symmetry to fix the metric, compute testable 2PN GW predictions

## 2. Causal Graph and q-Field

- Define causal graph G = (V,E) with edge weights q ∈ [0,1]
- q = quantum channel openness: fraction of quantum information that passes through edge
- Entropy: s(q) = -q ln q - (1-q) ln(1-q)
- RG blocking: ln q additive under coarse-graining
- Continuum limit: □(ln q) = source → static solution q = exp(-GM/rc²)
- This is DERIVED, not assumed

## 3. Effective Metric

- Spatial geometry from graph Laplacian + equivalence principle + isotropy → g_{ij} = q^{-2}δ_{ij}
- Temporal geometry from proper time: dτ = q·dt → g_{00} = -q²
- Full metric: ds² = -q²c²dt² + q^{-2}[dr² + r²dΩ²]
- PPN: γ = 1, β = 1 (verified in area-radius coordinates)
- This metric is the Jordan frame of Weyl-integrable geometry (Quiros et al. 2013)

## 4. Post-Newtonian Expansion

- Expand binding energy E(v) for test particle in circular orbit
- Newtonian: 0% deviation (exact match)
- 1PN: 0.03% deviation (matches GR within observational bounds)
- 2PN: 4.07% deviation ← DGF SIGNATURE
- 3PN: 20.74% deviation
- No free parameters: α=1 in dτ = q^α·dt uniquely fixed by Newtonian limit

## 5. Gravitational Wave Predictions

- 2PN GW phase shift: ΔΨ = 2π·Δe₂·⟨v⁴⟩·N_cycles
- GW170817: 0.67 rad (marginal with O4/O5)
- ET BNS: 1.9 rad (>100σ with Einstein Telescope)
- LISA EMRI: ~3100 rad (enormous)
- ppE parameterization: β(b=4) = 0.030
- Within current LIGO bounds; detectable with 3G detectors

## 6. Cosmology

- Cosmic q_bg(z) evolves with structure formation
- w_eff(z) = -1 - (1/3) d ln q_bg/d ln(1+z)
- q_bg variation ~10^{-5} from z=10 to z=0
- G_eff(z) = G/q_bg(z) — tiny variation
- BBN safe: q(z~10^9) ≈ 1
- DGF is consistent with ΛCDM; Λ remains independent parameter

## 7. Discussion

### What is derived
- q = exp(-GM/rc²) from causal graph RG flow
- dτ = q·dt as the proper time for information propagation
- 2PN GW deviation as a parameter-free consequence

### What is assumed (by symmetry)
- Equivalence principle → metric coupling b=2
- Spatial isotropy → conformally flat spatial metric
- Newtonian limit → α=1 in dτ = q^α·dt

### Relation to prior work
- Weyl-integrable geometry: Quiros et al. (2013)
- Jacobson thermodynamics: Jacobson (1995)
- Dilaton gravity: standard scalar-tensor theory in IR limit
- DGF unique: information-theoretic origin of q-field

## 8. Conclusion

DGF provides an information-theoretic foundation for gravity. The gravitational potential is the logarithm of quantum channel openness. The metric follows from symmetry principles. The theory is consistent with all current observations and makes one falsifiable prediction: a 4% deviation in the 2PN GW phase, testable with next-generation detectors.
