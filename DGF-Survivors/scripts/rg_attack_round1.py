"""
DGF Micro->Macro RG Flow: Effective Action, Field Equations, PPN Parameters
==========================================================================
Wall #3 Attack — Round 1

Derives the DGF low-energy effective action from information-theoretic first
principles, computes the static spherically symmetric solution, PPN parameters,
and observational constraints.

Key question: Does the DGF q-field scalar-tensor theory survive solar system
tests while making distinguishable predictions at stronger-field scales?
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import json

# ======================================================================
# 1. DGF EFFECTIVE ACTION
# ======================================================================
#
# The DGF low-energy effective action in the Einstein frame:
#
# S = \int d^4x \sqrt{-g} [ R/(16\pi G) - 1/2 (\partial q)^2 - V(q) ]
#   + S_m[\psi, A^2(q) g_{\mu\nu}]
#
# where:
# - q(x) is the DGF q-field (0 <= q <= 1), fraction of open quantum channels
# - V(q) = V_0 (1-q)^2 + lambda * s(q) is the q-field potential
# - s(q) = -q ln q - kappa (1-q) ln(1-q) is the DGF entropy density
# - A(q) is the conformal factor coupling q to matter
# - Matter fields psi see the Jordan frame metric \tilde{g} = A^2(q) g
#
# The static, vacuum solution for a point mass M gives:
# q(r) = exp(-GM/(r c^2))  (DGF soft boundary)
#
# The conformal factor A(q) is the key unknown function.
# Constraints on A(q):
# 1. A(1) = 1 (GR limit in vacuum)
# 2. dA/dq|_{q=1} = alpha_0 (PPN gamma parameter)
# 3. Cassini: |gamma-1| < 2.3e-5 => alpha_0^2 < 1e-5 (if no screening)
# 4. A(q) must be monotonic (physical: less q = stronger modified gravity)

# ======================================================================
# 2. PPN PARAMETERS FOR DGF SCALAR-TENSOR THEORY
# ======================================================================

def alpha_q(q, model='exponential', alpha0=0.0):
    """
    Scalar-matter coupling function alpha(q) = d ln A / dq.

    Models:
    - 'exponential': alpha(q) = alpha0 * exp(-beta*(1-q))
      (exponentially suppressed near q=1, screened)
    - 'power': alpha(q) = alpha0 * (1-q)^n
      (power-law suppression near q=1)
    - 'chameleon': alpha(q) = alpha0 * (1-q)^2 / (1 + (1-q)/delta)
      (chameleon-like screening at high density)
    """
    if model == 'exponential':
        beta = 10.0  # screening strength
        return alpha0 * np.exp(-beta * (1.0 - q))
    elif model == 'power':
        n = 2.0  # power-law index
        return alpha0 * (1.0 - q)**n
    elif model == 'chameleon':
        delta = 0.01
        return alpha0 * (1.0 - q)**2 / (1.0 + (1.0 - q)/delta)
    else:
        return alpha0 * (1.0 - q)

def A_q(q, model='exponential', alpha0=0.0):
    """
    Conformal factor A(q). Computed by integrating alpha(q) = d ln A / dq.
    A(1) = 1.
    """
    # Numerical integration from q to 1
    qs = np.linspace(q, 1.0, 1000)
    alphas = np.array([alpha_q(qi, model, alpha0) for qi in qs])
    ln_A = -np.trapz(alphas, qs)  # integral from q to 1
    return np.exp(ln_A)

def ppn_gamma(alpha0_at_1):
    """PPN gamma parameter from scalar coupling alpha at q=1."""
    return (1.0 - alpha0_at_1**2) / (1.0 + alpha0_at_1**2)

def ppn_beta(alpha0, dalpha_dq_at_1):
    """PPN beta parameter."""
    gamma_val = ppn_gamma(alpha0)
    beta0 = dalpha_dq_at_1 / alpha0 if abs(alpha0) > 1e-15 else 0.0
    return 1.0 + alpha0**2 * beta0 / (2.0 * (1.0 + alpha0**2)**2)

# ======================================================================
# 3. SOLAR SYSTEM CONSTRAINTS
# ======================================================================

print("=" * 70)
print("DGF SCALAR-TENSOR THEORY: PPN PARAMETERS AND OBSERVATIONAL CONSTRAINTS")
print("=" * 70)

# Cassini bound on gamma
cassini_bound = 2.3e-5  # |gamma - 1| < 2.3e-5

print("\n--- PPN gamma constraint from Cassini ---")
print(f"Cassini bound: |gamma - 1| < {cassini_bound}")

# For power-law model alpha(q) = alpha0 * (1-q)^n:
# alpha(q=1) = 0 for n > 0 => gamma = 1 exactly
# This means ALL screened models with alpha(q=1)=0 satisfy Cassini automatically!
print("\nKey insight: If alpha(q) vanishes at q=1, then gamma=1 exactly.")
print("The q-field is SCREENED in the solar system because:")
print("  q(r_sun) = exp(-GM_sun/(R_sun c^2)) = exp(-1.5e3/7e8) = exp(-2.1e-6)")
print("  1 - q(r_sun) ~ 2.1e-6 is TINY => alpha ~ (2.1e-6)^n is negligible")

# Solar surface q value
G = 6.67430e-11
c = 2.99792458e8
M_sun = 1.98847e30
R_sun = 6.957e8
a_sun = G * M_sun / c**2
q_sun = np.exp(-a_sun / R_sun)
print(f"\n  Sun: GM/c^2 = {a_sun:.1f} m, R = {R_sun:.1e} m")
print(f"  q at solar surface = {q_sun:.10f}")
print(f"  1 - q = {1-q_sun:.2e}")

# ======================================================================
# 4. BINARY PULSAR CONSTRAINTS
# ======================================================================

print("\n--- Binary Pulsar Constraints ---")
# PSR J0737-3039 (double pulsar): measured orbital decay matches GR to 0.05%
# This constrains scalar dipole radiation
# Dipole radiation ~ alpha^2 * (GM/Rc^2)^2 * (v/c)^2

# For PSR J0737-3039A:
M_ns = 1.338 * M_sun
R_ns = 12e3  # ~12 km neutron star radius
a_ns = G * M_ns / c**2
q_ns = np.exp(-a_ns / R_ns)
print(f"  Neutron star: GM/c^2 = {a_ns:.0f} m, R = {R_ns:.0f} m")
print(f"  q at NS surface = {q_ns:.6f}")
print(f"  1 - q = {1-q_ns:.4f}")
print(f"  Compactness GM/(Rc^2) = {a_ns/R_ns:.3f}")

# For power-law model alpha = alpha0 * (1-q)^2:
# alpha(q_ns) = alpha0 * 0.025
# Dipole radiation ~ alpha^2, constrains alpha(q_ns)^2 < 10^-5 (order of magnitude)
alpha_ns_required = np.sqrt(1e-5)  # maximum alpha at NS surface
print(f"\n  Maximum allowed alpha at NS surface: ~{alpha_ns_required:.1e}")
# If alpha(q) = alpha0 * (1-q)^2:
# alpha0_max = alpha_ns_required / (1-q_ns)^2 ~ 3e-3 / 6e-4 ~ 5
alpha0_max_ns = alpha_ns_required / (1 - q_ns)**2
print(f"  => alpha0_max (power-law n=2): ~{alpha0_max_ns:.1f}")

# ======================================================================
# 5. GALACTIC AND COSMOLOGICAL SCALES
# ======================================================================

print("\n--- Where DGF Can Deviate from GR ---")
print("DGF deviations from GR scale with (1-q):")
print("  Solar surface:    1-q ~ 2e-6  (heavily screened)")
print("  Neutron star:     1-q ~ 0.16  (mildly screened)")
print("  Galactic halo:    1-q ~ varies")
print("  Cosmological:     1-q ~ 0.2-0.4 (unscreened)")

# Galactic scale
# Milky Way: M ~ 10^12 M_sun, R_halo ~ 100 kpc
M_mw = 1e12 * M_sun
R_halo = 100e3 * 3.086e16  # 100 kpc in meters
a_mw = G * M_mw / c**2
q_halo = np.exp(-a_mw / R_halo)
print(f"\n  Milky Way halo: GM/c^2 = {a_mw:.1e} m, R_halo = {R_halo:.1e} m")
print(f"  q at 100 kpc = {q_halo:.6f}")
print(f"  1 - q = {1-q_halo:.4f}")

# ======================================================================
# 6. DERIVING q(r) FROM THE ACTION
# ======================================================================

print("\n" + "=" * 70)
print("DERIVING q(r) FROM THE DGF ACTION")
print("=" * 70)

# The DGF entropy density
def s_q(q, kappa=1.0):
    """DGF entropy density: s(q) = -q ln q - kappa (1-q) ln(1-q)"""
    if q <= 0 or q >= 1:
        # Handle boundaries
        s = 0.0
        if q > 0:
            s -= q * np.log(q)
        if q < 1:
            s -= kappa * (1-q) * np.log(1-q)
        return s
    return -q * np.log(q) - kappa * (1-q) * np.log(1-q)

def V_q(q, V0=1.0, kappa=1.0):
    """DGF q-field potential."""
    return V0 * (1-q)**2  # simplest form; entropic term adds corrections

# The effective action in natural units:
# S = \int d^4x \sqrt{-g} [R/(16\pi G) - (1/2)(\partial q)^2 - V(q)]
# + S_m[A^2(q) g]

# Variation gives:
# G_{\mu\nu} = 8\pi G [T^{\phi}_{\mu\nu} + A^2(q) T^m_{\mu\nu}]
# \Box q - V'(q) = -alpha(q) A^4(q) T^m

# For a point mass: T^m = -M \delta^{(3)}(x) / \sqrt{-g} (in rest frame)
# Static, spherical solution in weak field:
# q(r) ≈ 1 - GM/(r c^2) (for alpha0 small enough)

# The key: with sufficient screening (alpha(q=1)=0),
# q(r) = exp(-GM/(r c^2)) is the static solution of the DGF field equations
# in the weak-field limit.

print("\nTheorem sketch:")
print("For alpha(q) with alpha(1)=0 and d(alpha)/dq|_{q=1} finite,")
print("the static vacuum solution q(r) satisfies:")
print("  q'' + (2/r) q' = V'(q) + O(alpha^2)")
print("For V(q) = V0 (1-q)^2 + ..., the solution is:")
print("  q(r) = 1 - (C/r) exp(-m r)")
print("where m = sqrt(2 V0) is the q-field mass.")
print("")
print("If m = 0 (massless q-field, V0 = 0): q(r) = 1 - C/r")
print("Matching to Newtonian limit C = GM/c^2 gives q = 1 - GM/(rc^2)")
print("This is the EXPANSION of q(r) = exp(-GM/rc^2) for r >> GM/c^2")

# ======================================================================
# 7. NUMERICAL: STATIC SOLUTION
# ======================================================================

print("\n" + "=" * 70)
print("NUMERICAL SOLUTION: STATIC SPHERICALLY SYMMETRIC q-FIELD")
print("=" * 70)

def solve_q_static(r_range, V0=0.0, alpha0=0.01, model='power', n=2.0):
    """
    Solve for static q(r) around a point mass M.

    Field equation (in isotropic coordinates):
    q'' + (2/r) q' = V'(q) + alpha(q) * rho_matter / M_P^2

    For vacuum (r > R_source): rho_matter = 0
    Boundary condition: q(infinity) = 1, q(r) ~ 1 - GM/(r c^2) as r -> inf
    """
    # Use the known solution: q(r) = exp(-GM/rc^2)
    # and verify it satisfies the field equations
    a = 1.0  # GM/c^2 in arbitrary units

    def q_exact(r):
        return np.exp(-a / r)

    def q_linear(r):
        """Linear approximation: q = 1 - a/r"""
        return 1.0 - a / r

    rs = np.logspace(np.log10(0.1*a), np.log10(100*a), 200)

    qs_exact = q_exact(rs)
    qs_linear = q_linear(rs)

    # Check: does q(r) = exp(-a/r) satisfy the massless (V0=0) field equation?
    # For V0=0, alpha=0 (decoupled): \Box q = 0 => q'' + (2/r)q' = 0
    # Solution: q = A + B/r
    # q(inf) = 1 => A = 1, q ~ 1 - GM/r for r >> GM/c^2 => B = -GM/c^2
    # So q = 1 - GM/(rc^2), NOT q = exp(-GM/rc^2)!

    print("\nIMPORTANT FINDING:")
    print("For the massless free scalar (V0=0, alpha=0):")
    print("  Box q = 0 => q(r) = 1 - GM/(rc^2)  (Coulomb-like)")
    print("  NOT q(r) = exp(-GM/rc^2)  (the DGF soft boundary)")
    print("")
    print("For q(r) = exp(-a/r) to be a solution, we need:")
    print("  Box q = q'' + (2/r)q' = q * a^2/r^4  != 0")
    print("  => V'(q) + alpha(q)*T = q * a^2/r^4")
    print("  => The q-field is NOT free; it's sourced by matter")
    print("     in a specific way that gives the soft boundary profile.")

    # Compute Box q for the DGF profile
    r = rs
    q_val = q_exact(r)
    dq_dr = a * q_val / r**2
    d2q_dr2 = a * q_val * (a - 2*r) / r**4
    box_q = d2q_dr2 + (2/r) * dq_dr

    # The required source term
    source = box_q  # = V'(q) + alpha(q) * rho
    # = q * a^2/r^4

    print(f"\n  At r = 2a (Schwarzschild radius): Box q = {box_q[np.argmin(np.abs(r-2*a))]:.4f}")
    print(f"  At r = 5a (shadow scale): Box q = {box_q[np.argmin(np.abs(r-5*a))]:.4f}")

    return rs, qs_exact, box_q

rs, qs, box_q = solve_q_static(None)

# ======================================================================
# 8. THE q-FIELD SOURCE TERM
# ======================================================================

print("\n" + "=" * 70)
print("THE q-FIELD SOURCE: WHAT DRIVES q(r) = exp(-GM/rc^2)?")
print("=" * 70)

print("""
The DGF field equation for q(r) = exp(-a/r) requires:
  Box q = q * a^2 / r^4

This source term can be decomposed as:
  Box q = V'(q) + alpha(q) * T_matter

For a point mass at the origin (T_matter ~ delta function),
the vacuum equation (r > 0) is:
  Box q = V'(q)

For q(r) = exp(-a/r) to be a vacuum solution:
  V'(q) = q * a^2 / r^4 = q * (ln q)^2 * (ln q + 2)^2 / a^2...

Wait. Let's express the RHS in terms of q only.
q = exp(-a/r) => r = -a/ln(q)
a^2/r^4 = a^2 / (a/ln(q))^4 = (ln q)^4 / a^2

So: Box q = q * (ln q)^4 / a^2

This means the potential must satisfy:
  V'(q) = q * (ln q)^4 / a^2

But a = GM/c^2 depends on the source mass! This means the potential
is SOURCE-DEPENDENT. Different masses M would require different V(q).

=> q(r) = exp(-GM/rc^2) is NOT a solution of a universal field equation.
   It's a PHENOMENOLOGICAL profile that fits the DGF information-theoretic
   ansatz but doesn't follow from a standard local action.

THIS IS THE CORE OF WALL #3:
  The q-field profile q(r) = exp(-GM/rc^2) is currently an ansatz,
  not a solution of a derived field equation.
  To make it a solution, we need to derive the DGF effective action
  from the microscopic causal graph dynamics -- the RG flow.
""")

# ======================================================================
# 9. FORWARD: CONSTRUCTING THE EFFECTIVE ACTION FROM ENTROPY
# ======================================================================

print("=" * 70)
print("FORWARD: ENTROPY-DRIVEN EFFECTIVE ACTION")
print("=" * 70)

# Alternative approach: the q-field profile is determined by
# entropy maximization, not by a standard Lagrangian.
#
# The DGF entropy: S[q] = \int d^3x s(q(x))
# s(q) = -q ln q - kappa (1-q) ln(1-q)
#
# For a fixed total energy E (including gravitational binding energy),
# q(r) extremizes S[q] subject to \int H[q] d^3x = E.
#
# This is a CONSTRAINED OPTIMIZATION problem, not a Lagrangian field theory.

print("""
Alternative formulation: Entropy-driven statics

Instead of a Lagrangian field equation Box q = V'(q), the DGF q-field
profile is determined by maximizing the total entropy:

  S[q] = \int d^3x \sqrt{h} s(q(x))

subject to the constraint that the total energy (including gravitational
binding energy) equals the source mass M:

  \int d^3x \sqrt{h} rho_E[q](x) = M c^2

where rho_E[q] is the energy density functional of the q-field.

This is a variational principle with a Lagrange multiplier:
  delta S - lambda * delta E = 0

=> ds/dq = lambda * d(rho_E)/dq

For s(q) = -q ln q - (1-q) ln(1-q) (kappa=1):
  ds/dq = -ln q + ln(1-q) = ln((1-q)/q)

For the energy density, the simplest ansatz is:
  rho_E = (c^4/(8\pi G)) (grad q)^2 / q^2

(This comes from: the q-field determines the effective gravitational
coupling, and the gradient energy is the gravitational field energy.)

Then: d(rho_E)/dq ~ -(grad q)^2 / q^3

And the variational equation gives a PDE for q(r).
The solution q(r) = exp(-GM/rc^2) should emerge for a specific
choice of rho_E[q].

Let's check: for q(r) = exp(-a/r),
  grad q = dq/dr = q * a/r^2
  (grad q)^2 = q^2 * a^2/r^4
  rho_E = (c^4/(8\pi G)) * a^2/r^4

  Total energy:
  E = \int_0^\infty 4\pi r^2 rho_E dr
    = (c^4/(2G)) * a^2 \int_0^\infty dr / r^2

This DIVERGES at r -> 0! The energy density ~ 1/r^4 is too singular.

=> Need a UV cutoff at r ~ l_P (Planck length).
   This is the quantum gravity regime where DGF is defined.
   The RG flow from l_P to macroscopic scales would regularize this.
""")

# ======================================================================
# 10. SUMMARY: WHAT WE LEARNED AND WHAT'S NEXT
# ======================================================================

print("=" * 70)
print("WALL #3 STATUS AFTER ROUND 1")
print("=" * 70)

results = {
    "wall": "#3 (Micro->Macro RG Flow)",
    "round": 1,
    "findings": [
        "q(r)=exp(-GM/rc^2) is NOT a solution of a standard local Lagrangian field theory",
        "It CAN be the solution of an entropy-maximization variational principle",
        "But this requires specifying the energy density functional rho_E[q]",
        "The simplest rho_E ~ (grad q)^2 leads to UV divergence at r->0",
        "This divergence needs regularization at Planck scale -- the RG flow",
        "",
        "PPN constraints (solar system) are TRIVIALLY satisfied:",
        "  - q(r_sun) ~ 1 - 2e-6 => screening is automatic",
        "  - Any alpha(q) with alpha(1)=0 gives gamma=1 exactly",
        "  - DGF only deviates from GR in strong-field (NS, BH) and cosmology",
        "",
        "The path forward has two branches:",
        "Branch 1 (theory): Derive rho_E[q] from DGF microscopic causal graph",
        "  -> This IS the RG flow; needs new mathematical tools",
        "Branch 2 (phenomenology): Parametrize rho_E[q] and constrain with data",
        "  -> Fit to binary pulsar, EHT, DESI; make predictions for new regimes",
    ],
    "wall_nature": "Theoretical structure gap -- q(r) is currently an ansatz, not a derived solution",
    "wall_penetrability": "Partially penetrable via Branch 2 (phenomenological parametrization)",
    "next_step": "Parametrize rho_E[q] with 2-3 free functions, constrain with binary pulsar + EHT data",
}

for k, v in results.items():
    if k == "findings":
        print("\nFindings:")
        for f in v:
            print(f"  {f}")
    else:
        print(f"{k}: {v}")

with open("D:\\Claude\\ai-reservations\\DGF-Survivors\\rg_round1_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

print("\nResults saved to rg_round1_results.json")
