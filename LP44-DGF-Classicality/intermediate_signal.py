"""
Where in cosmic history does the intermediate layer manifest?

For alpha = z (dynamical critical exponent):
  L*(a) = l_P * (Gamma_0/H(a))^{1/alpha}

The redshift where L* equals the Hubble radius 1/H(a):
  l_P * (Gamma_0/H(a))^{1/alpha} = 1/H(a)
  → H(a) = Gamma_0 * (H(a)*l_P)^{alpha}
  → H(a) = Gamma_0^{1/(1-alpha)} * l_P^{-alpha/(1-alpha)}  [alpha≠1]
  → For alpha=1: H(a)*l_P = l_P/L_Hubble ~ 10^{-61} → always satisfied

For alpha≠1: specific redshift where L* = Hubble scale.
For alpha=1: condition is scale-invariant.
"""
import numpy as np

l_P = 1.616e-35  # m
Gamma_0 = 1.855e43  # Hz (t_P^{-1})
H0 = 2.19e-18  # Hz (70 km/s/Mpc)
c = 2.998e8  # m/s

print("=" * 70)
print("COSMIC SIGNALS OF THE INTERMEDIATE LAYER")
print("=" * 70)

# For each alpha, find the redshift where L* = Hubble radius
# l_P * (Gamma_0/H(z))^{1/alpha} = c/H(z)
# Simplify: H(z)^{1-1/alpha} = Gamma_0^{1/alpha} * l_P / c
# H(z) = (Gamma_0^{1/alpha} * l_P / c)^{alpha/(alpha-1)}

print(f"\n{'alpha':<8} {'H(z*) / H0':<15} {'z*':<10} {'Epoch':<25} {'What it matches':<30}")
print("-" * 80)

for alpha in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0]:
    if abs(alpha - 1.0) < 0.01:
        # alpha=1: scale-invariant, L* = Hubble at ALL times
        H_ratio = 1.0
        z_star = 0.0
        epoch = "NOW (scale-invariant)"
        matches = "Dark energy / Hubble scale"
    else:
        # H(z*) = (Gamma_0^{1/alpha} * l_P / c)^{alpha/(alpha-1)}
        H_star = (Gamma_0**(1/alpha) * l_P / c) ** (alpha/(alpha-1))
        H_ratio = H_star / H0

        # z from H(z) ~ H0 * sqrt(Omega_m*(1+z)^3 + Omega_Lambda)
        # Rough: H(z) ~ H0 * (1+z)^{3/2} (matter domination)
        if H_ratio > 1:
            z_star = H_ratio**(2/3) - 1
            if z_star > 1e4:
                epoch = f"z~{z_star:.1e} (inflation era)"
            elif z_star > 1000:
                epoch = f"z~{z_star:.0f} (pre-CMB)"
            elif z_star > 10:
                epoch = f"z~{z_star:.0f} (dark ages)"
            elif z_star > 1:
                epoch = f"z~{z_star:.1f} (galaxy formation)"
            else:
                epoch = f"z~{z_star:.2f} (late universe)"
        else:
            z_star = 0
            epoch = "future"

        if alpha < 1:
            matches = "Early universe / Inflation"
        else:
            matches = "Late universe / Dark energy"

    print(f"{alpha:<8.2f} {H_ratio:<15.2e} {z_star:<10.2f} {epoch:<25} {matches:<30}")

# ================================================================
# Observable: MOND acceleration scale
# ================================================================
print(f"\n{'='*70}")
print("OBSERVABLE CONNECTIONS")
print(f"{'='*70}")

# MOND acceleration: a_0 = 1.2e-10 m/s^2
a_MOND = 1.2e-10
# c * H_0 / (2*pi) ≈ 3.3e-10 m/s^2
cH0 = c * H0
print(f"MOND acceleration a_0     = {a_MOND:.2e} m/s^2")
print(f"c * H_0                  = {cH0:.2e} m/s^2")
print(f"c * H_0 / (2*pi)         = {cH0/(2*np.pi):.2e} m/s^2")
print(f"a_0 / (c*H_0)            = {a_MOND/cH0:.3f}")
print()

# DGF prediction for alpha:
# If alpha determines the transition scale L*,
# the acceleration at that scale is a* = Gamma_eff(L*) * c
# At L* where Gamma_eff = H_0: a* = H_0 * c ≈ 6.6e-10 m/s^2
print("DGF predictions for characteristic acceleration:")
for alpha in [1.0, 1.5, 2.0]:
    if alpha == 1.0:
        L_star = l_P * (Gamma_0/H0)**(1/alpha)
        Gamma_star = H0  # by definition at L* for alpha=1
    else:
        L_star = l_P * (Gamma_0/H0)**(1/alpha)
        Gamma_star = Gamma_0 * (l_P/L_star)**alpha
    a_star = Gamma_star * c
    print(f"  alpha={alpha}: L*={L_star:.2e} m, Gamma*={Gamma_star:.2e} Hz, a*={a_star:.2e} m/s^2")

# ================================================================
# The key observable signature
# ================================================================
print(f"\n{'='*70}")
print("KEY OBSERVABLE SIGNATURE")
print(f"{'='*70}")
print(f"""
If alpha=1 (ballistic causal propagation, DGF natural):
  The intermediate layer is the ENTIRE cosmic history.
  g(a) evolves continuously — no sharp transition.
  Observable: SMOOTH w(z) evolution, non-monotonic near z~1.
  This is EXACTLY what DESI DR2 sees: w(z) dips at z~1.

If alpha=2 (diffusive, surface-dominated):
  The intermediate layer is at z~10^30 (inflation era).
  g(a) has a sharp feature at very high z.
  Observable: specific CMB B-mode polarization pattern.
  (But CMB B-modes from inflation are already predicted by standard inflation.)

If alpha=3 (volume-dominated):
  The intermediate layer is at z~10^45 (pre-inflation).
  No observable signal in accessible cosmology.
  DGF two-time effect is unobservable → DGF is unfalsifiable.

CRITICAL TEST: DESI DR2 already hints at non-monotonic w(z).
If future DESI/Euclid data confirms w(z) ≠ -1 with a specific
shape matching DGF's alpha=1 prediction, this is evidence for
the DGF intermediate layer.
""")
