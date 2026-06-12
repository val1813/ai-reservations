"""
RG flow of Gamma_eff — finding the intermediate layer where
microscopic ring formation rate meets cosmological expansion.

Key: Gamma_eff(scale) = Gamma_0 * f(scale)
The scale where Gamma_eff ~ H0 is where two-time dynamics becomes relevant.
"""
import numpy as np

# Planck and Hubble scales
Gamma_0 = 1.855e43  # t_P^{-1} in Hz
H_0 = 2.19e-18      # 70 km/s/Mpc in Hz
scale_ratio = Gamma_0 / H_0  # ~10^61

print("=" * 70)
print("RG FLOW OF Gamma_eff: FINDING THE INTERMEDIATE LAYER")
print("=" * 70)
print(f"Gamma_0 (Planck) = {Gamma_0:.2e} Hz")
print(f"H_0 (Hubble)     = {H_0:.2e} Hz")
print(f"Ratio            = {scale_ratio:.2e}")
print()

# Models for Gamma_eff(scale)
# Each RG step (blocking factor b) renormalizes Gamma
# Gamma_eff(L) = Gamma_0 * (l_P / L)^alpha

print("Model: Gamma_eff(L) = Gamma_0 * (l_P / L)^alpha")
print()
print(f"{'alpha':<8} {'L* (m)':<15} {'L*/l_P':<15} {'Physical scale':<25}")
print("-" * 63)

l_P = 1.616e-35  # Planck length in meters

for alpha in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    # Critical scale where Gamma_eff = H_0
    # Gamma_0 * (l_P/L)^alpha = H_0
    # L = l_P * (Gamma_0/H_0)^{1/alpha}
    L_star = l_P * (scale_ratio) ** (1.0/alpha)

    # Physical identification
    if L_star < 1e-15:
        phys = "Sub-nuclear (<1fm)"
    elif L_star < 1e-10:
        phys = "Atomic scale (0.1nm)"
    elif L_star < 1e-6:
        phys = "Microscopic (1um)"
    elif L_star < 1e-2:
        phys = "Mesoscopic (1mm)"
    elif L_star < 1e3:
        phys = "Macroscopic (1km)"
    elif L_star < 1e15:
        phys = "Solar system scale"
    elif L_star < 1e26:
        phys = "Galactic scale"
    else:
        phys = "Hubble scale"

    print(f"{alpha:<8.2f} {L_star:<15.2e} {L_star/l_P:<15.2e} {phys:<25}")

# ================================================================
# The RG layers between Planck and Hubble
# ================================================================
print(f"\n{'='*70}")
print("RG LAYER STRUCTURE")
print(f"{'='*70}")

# For alpha=1 (each dimension contributes equally):
# L* = l_P * (Gamma_0/H_0) = 1.6e-35 * 10^61 = 1.6e26 m ≈ 17 Glyr ≈ Hubble radius
# This means Gamma_eff(L) = Gamma_0 * l_P/L → linear in 1/L

# For alpha=2 (surface effects dominate):
# L* = 1.6e-35 * sqrt(10^61) = 1.6e-35 * 3.2e30 = 5e-5 m = 50 um

# For alpha=3 (volume effects dominate):
# L* = 1.6e-35 * (10^61)^{1/3} = 1.6e-35 * 2.15e20 = 3.4e-15 m ≈ nuclear scale

print("""
alpha determines how fast Gamma_eff falls with scale:

alpha=1: Gamma_eff ~ 1/L (linear)
  -> L* ~ Hubble radius. The ENTIRE universe is one RG layer.
  -> Two-time effect is cosmological from the start.
  -> Every scale contributes equally to time drift.

alpha=2: Gamma_eff ~ 1/L^2 (surface/area)
  -> L* ~ 50um. Mesoscopic scale.
  -> Rings at >50um are "frozen on cosmological timescales"
  -> Two-time effect comes from sub-50um structure.

alpha=3: Gamma_eff ~ 1/L^3 (volume)
  -> L* ~ 3fm. Nuclear scale.
  -> Only sub-nuclear rings are "active" cosmologically.
  -> Most macroscopic structure is frozen → g≈constant.

The alpha value is determined by the CAUSAL GRAPH CONNECTIVITY:
  - 1D chain: alpha=1 (each node has O(1) neighbors)
  - 2D grid:  alpha=2 (surface effects dominate ring formation)
  - 3D lattice: alpha=3 (volume effects dominate)

In a realistic 3+1D causal graph (our universe):
  alpha depends on the spectral dimension d_s of the causal graph.
  For d_s ≈ 4 (our observed spacetime dimension):
  alpha = d_s - 1? or d_s/2? Need to compute from graph structure.
""")

# ================================================================
# The answer: which intermediate layer matters?
# ================================================================
print("=" * 70)
print("WHICH INTERMEDIATE LAYER?")
print("=" * 70)
print("""
The intermediate layer is determined by alpha:

- If alpha ~ 1: The entire RG flow from Planck to Hubble contributes.
  Every scale adds to the time drift. g(a) integrates over all layers.

- If alpha ~ 2-3: There's a SPECIFIC scale L* where Gamma_eff = H_0.
  This is where the two-time dynamics "freezes out" cosmologically.
  Scales below L* have Gamma > H_0 → active ring formation → time drift.
  Scales above L* have Gamma < H_0 → frozen → no time drift.

The alpha value is NOT a free parameter. It comes from the spectral
dimension d_s of the causal graph, which is computable from DGF.

From the high_d_interference data:
  PR ~ exp(0.88 * b1) for c=0.5
  b1 ~ N^gamma with gamma ~ 1.12 (from rg_flow_v2.py on 2D lattice)

  For 3D: expected gamma ~ 1 (volume scaling of cycles)
  This suggests alpha ~ 1 for the RG flow of Gamma_eff.

alpha ~ 1 → L* ~ Hubble radius → the ENTIRE cosmic history contributes
to the two-time drift. There's no single intermediate layer — ALL
scales between Planck and Hubble are active.
""")
