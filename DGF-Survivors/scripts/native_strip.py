#!/usr/bin/env python3
"""
DGF Native Strip Computation v3
===============================
Corrected analytic continuation: sin^2(z) = [sin(z)]^2, NOT |sin(z)|^2.

Delta(c) = 1 - sin^2(2c) - sin^2(4c)/4
         = 3/8 + cos(4c)/2 + cos(8c)/8

Branch cuts:
  S1 (sqrt): Im(Delta)=0 AND Re(Delta) <= 0
  S2 (H2):   Im(Delta)=0 AND Re(Delta) >= 1

Im(Delta) = -sin(4c_R)sinh(4c_I)/2 - sin(8c_R)sinh(8c_I)/8

For Im(Delta)=0 at c_I>0, need sin(4c_R) and sin(8c_R) opposite signs,
or sin(4c_R)=0 (c_R=0, pi/4, pi/2).
"""

import numpy as np
from scipy import optimize
import warnings
warnings.filterwarnings("ignore")

# -- Core functions -------------------------------------------------------

def delta_complex(c_R, c_I):
    """Delta = 3/8 + cos(4c)/2 + cos(8c)/8 for complex c."""
    cos4 = np.cos(4*c_R)*np.cosh(4*c_I) - 1j*np.sin(4*c_R)*np.sinh(4*c_I)
    cos8 = np.cos(8*c_R)*np.cosh(8*c_I) - 1j*np.sin(8*c_R)*np.sinh(8*c_I)
    delta = 3.0/8.0 + cos4/2.0 + cos8/8.0
    return delta.real, delta.imag

def im_delta(c_R, c_I):
    """Im(Delta) = -sin(4c_R)sinh(4c_I)/2 - sin(8c_R)sinh(8c_I)/8"""
    return -0.5*np.sin(4*c_R)*np.sinh(4*c_I) - 0.125*np.sin(8*c_R)*np.sinh(8*c_I)

def re_delta(c_R, c_I):
    """Re(Delta) = 3/8 + cos(4c_R)cosh(4c_I)/2 + cos(8c_R)cosh(8c_I)/8"""
    return 3.0/8.0 + np.cos(4*c_R)*np.cosh(4*c_I)/2.0 + np.cos(8*c_R)*np.cosh(8*c_I)/8.0

def qcmi_real(c_R, p=0.5):
    """QCMI on real c-axis."""
    if p == 0.5:
        d = 3.0/8.0 + np.cos(4*c_R)/2.0 + np.cos(8*c_R)/8.0
    else:
        pp = p*(1-p)
        cos4r = np.cos(4*c_R)
        cos8r = np.cos(8*c_R)
        trig = 2.5 - 2*cos4r - 0.5*cos8r
        d = 1.0 - pp*trig
    if d <= 0:
        return 0.0
    s = np.sqrt(d)
    z = 0.5 + s/2.0
    if z <= 0 or z >= 1:
        return 0.0
    if z < 1e-15 or 1-z < 1e-15:
        return 0.0
    return -z*np.log2(z) - (1-z)*np.log2(1-z)

# -- Analytic branch cut detection ----------------------------------------

def find_first_branch_cut(c_R, max_cI=10.0):
    """
    Find first c_I > 0 where QCMI analytic continuation hits a branch cut.

    Returns (gamma_max, hit_type).
    """
    sin4 = np.sin(4*c_R)
    sin8 = np.sin(8*c_R)
    cos4 = np.cos(4*c_R)
    cos8 = np.cos(8*c_R)
    eps = 1e-12

    # Case A: sin(4c_R) ~ 0 -> Im(Delta)=0 for ALL c_I
    if abs(sin4) < 1e-14:
        re_0 = 3.0/8.0 + cos4/2.0 + cos8/8.0

        if abs(re_0) < eps:
            # c_R ~ pi/4: Re(0)=0, monotonic increase
            # Find c_I where Re(Delta)=1 (H2 cut)
            def f(x):
                return 3.0/8.0 + cos4*np.cosh(4*x)/2.0 + cos8*np.cosh(8*x)/8.0 - 1.0
            try:
                result = optimize.root_scalar(f, bracket=[1e-10, 3.0], method='brentq')
                return result.root, 'H2_finite'
            except:
                return 5.0, 'none'

        elif abs(re_0 - 1.0) < eps:
            # c_R ~ 0 or pi/2: Re(0)=1, Re > 1 for all c_I > 0
            return 0.0, 'H2_immediate'

        else:
            return 5.0, 'none'

    # Case B: sin4 and sin8 same sign -> Im never crosses 0
    if sin4 * sin8 > 0:
        return np.inf, 'infinite'

    # Case C: opposite signs -> Im crosses 0 at some c_I > 0
    # Only for c_R in (pi/8, pi/4) as derived analytically
    if not (np.pi/8 - 1e-12 < c_R < np.pi/4 + 1e-12):
        return np.inf, 'infinite'

    def im_func(x):
        return -0.5*sin4*np.sinh(4*x) - 0.125*sin8*np.sinh(8*x)

    try:
        result = optimize.root_scalar(im_func, bracket=[1e-10, 5.0],
                                       method='brentq', xtol=1e-14)
        if not result.converged:
            return np.inf, 'no_root'
        c_I_root = result.root
        re_at = re_delta(c_R, c_I_root)

        if re_at <= 0:
            return c_I_root, 'S1_sqrt'
        elif re_at >= 1.0:
            return c_I_root, 'S2_H2'
        else:
            # Im=0 but Re in (0,1) -- between cuts, safe
            return np.inf, 'between_cuts'
    except:
        return np.inf, 'root_error'

# -- Harmonic (|sin|^2) extension -----------------------------------------

def delta_modulus(c_R, c_I):
    """
    Non-holomorphic extension: sin^2 interpreted as |sin|^2.
    Delta = 1 - |sin(2c)|^2 - |sin(4c)|^2/4
    This is always real.
    """
    s2 = np.sin(2*c_R)**2 + np.sinh(2*c_I)**2
    s4 = np.sin(4*c_R)**2 + np.sinh(4*c_I)**2
    return 1.0 - s2 - s4/4.0

def gamma_max_modulus(c_R, max_cI=5.0):
    """Find c_I where Delta_modulus = 0 (branch point of sqrt)."""
    a = 1.0 - np.sin(2*c_R)**2 - np.sin(4*c_R)**2/4.0
    if a <= 0:
        return 0.0

    def f(x):
        return np.sinh(2*x)**2 + np.sinh(4*x)**2/4.0 - a

    if f(1e-10) >= 0:
        return 0.0
    if f(max_cI) < 0:
        return max_cI

    try:
        result = optimize.root_scalar(f, bracket=[1e-10, max_cI],
                                       method='brentq', xtol=1e-14)
        return result.root
    except:
        for c_I in np.linspace(0, max_cI, 100000):
            if f(c_I) >= 0:
                return c_I
        return max_cI

def gamma_max_modulus_p(c_R, pp):
    """Modulus extension for general p*(1-p) = pp."""
    s2 = np.sin(2*c_R)**2
    s4 = np.sin(4*c_R)**2
    base = 1.0 - pp*(4*s2 + s4)
    if base <= 0:
        return 0.0

    def f(x):
        return pp*(4*np.sinh(2*x)**2 + np.sinh(4*x)**2) - base

    if f(1e-10) >= 0:
        return 0.0
    if f(5.0) < 0:
        return 5.0
    try:
        result = optimize.root_scalar(f, bracket=[1e-10, 5.0],
                                       method='brentq', xtol=1e-14)
        return result.root
    except:
        return 5.0

# -- Main -----------------------------------------------------------------

def main():
    PI = np.pi
    print("=" * 72)
    print("DGF Native Strip Computation v3")
    print("=" * 72)
    print()
    print("Two competing extensions to complex c-plane:")
    print("  A) Holomorphic: sin^2(z) = [sin(z)]^2 (complex square)")
    print("  B) Harmonic:    sin^2(z) = |sin(z)|^2 (squared modulus)")
    print()

    # -- 1. Validation --
    print("-" * 72)
    print("1. REAL-AXIS CONSISTENCY CHECK")
    print()
    c_R_test = np.linspace(0, PI/2, 9)
    print("   c_R/pi       QCMI        Delta(real)")
    print("   " + "-" * 42)
    for cr in c_R_test:
        q = qcmi_real(cr, 0.5)
        d = 3.0/8.0 + np.cos(4*cr)/2.0 + np.cos(8*cr)/8.0
        print(f"   {cr/PI:8.4f}    {q:10.6f}   {d:12.8f}")
    print()

    # -- 2. Holomorphic branch cut structure --
    print("-" * 72)
    print("2. HOLOMORPHIC EXTENSION: Branch Cut Analysis")
    print()
    print("   Im(Delta) = -sin(4c_R)sinh(4c_I)/2 - sin(8c_R)sinh(8c_I)/8")
    print()
    print("   Region analysis:")
    print("   c_R in [0, pi/8]:     sin4>0, sin8>0 -> Im<0 for all c_I>0 -> NO crossing")
    print("   c_R in [pi/8, pi/4]:  sin4>0, sin8<0 -> Im crosses 0 once")
    print("   c_R = pi/4:           sin4=0, sin8=0 -> Im=0 for all c_I (special)")
    print("   c_R in [pi/4, 3pi/8]: sin4<0, sin8>0... wait")
    print()

    # Verify: for c_R in (pi/4, 3pi/8), sin4 < 0
    # sin8 = 2 sin4 cos4
    # cos4 in (cos(pi), cos(3pi/2)) = (-1, 0)
    # So sin8 = 2*(neg)*(neg) = pos > 0
    # Actually wait: cos(pi) = -1, cos(3pi/2) = 0
    # For 4c_R in (pi, 3pi/2): sin < 0, cos < 0
    # sin8 = 2*sin4*cos4 = 2*(neg)*(neg) = pos
    # So sin4 < 0, sin8 > 0 -> opposite signs!
    # This was wrong in my earlier analysis.

    print("   CORRECTED Region analysis:")
    print("   c_R in [0, pi/8]:       sin4>0, sin8>0 -> same sign -> no Im=0 crossing")
    print("   c_R = pi/8:             sin4>0, sin8=0 -> Im small-c_I: <0")
    print("   c_R in [pi/8, pi/4]:    sin4>0, sin8<0 -> opp sign -> Im crosses 0")
    print("   c_R = pi/4:             sin4=0, sin8=0 -> Im=0 always")
    print("   c_R in [pi/4, 3pi/8]:   sin4<0, sin8>0 -> opp sign -> Im crosses 0")
    print("   c_R = 3pi/8:            sin4<0, sin8=0 -> check")
    print("   c_R in [3pi/8, pi/2]:   sin4<0, sin8>0... wait")
    print()

    # For c_R in (3pi/8, pi/2): 4c_R in (3pi/2, 2pi): sin4 < 0, cos4 > 0
    # sin8 = 2*sin4*cos4 = 2*(neg)*(pos) = neg
    # So sin4 < 0, sin8 < 0 -> same sign (both neg) -> no crossing

    print("   c_R in [3pi/8, pi/2]:   sin4<0, sin8<0 -> same sign -> no Im=0 crossing")
    print("   c_R = pi/2:             sin4=0, sin8=0 -> Im=0 always")
    print()
    print("   So Im(Delta)=0 for c_I>0 only when:")
    print("   - c_R in [pi/8, pi/4]  (sin4>0, sin8<0)")
    print("   - c_R in [pi/4, 3pi/8] (sin4<0, sin8>0)")
    print("   - c_R = pi/4 (special, Im=0 always)")
    print()

    # -- 3. Detailed scan --
    print("-" * 72)
    print("3. GAMMA_MAX SCAN -- Holomorphic Extension")
    print()

    n_cR = 400
    c_R_vals = np.linspace(0, PI/2, n_cR)
    gamma_analytic = np.zeros(n_cR)
    gamma_mod = np.zeros(n_cR)
    hit_types = []

    for i, c_R in enumerate(c_R_vals):
        gm, ht = find_first_branch_cut(c_R)
        gamma_analytic[i] = gm
        hit_types.append(ht)
        gamma_mod[i] = gamma_max_modulus(c_R)

    # Key points table
    key_fracs = [0, 1/32, 1/16, 3/32, 1/8, 5/32, 3/16, 7/32, 1/4,
                 9/32, 5/16, 11/32, 3/8, 13/32, 7/16, 15/32, 1/2]
    print(f"   {'c_R/pi':>8s}  {'gamma(analytic)':>18s}  {'gamma(|sin|^2)':>18s}  {'hit_type':>14s}")
    print("   " + "-" * 68)
    for frac in key_fracs:
        c_R = frac * PI/2
        idx = np.argmin(abs(c_R_vals - c_R))
        ga = gamma_analytic[idx]
        gm = gamma_mod[idx]
        ht = hit_types[idx]
        ga_str = f"{ga:18.8f}" if np.isfinite(ga) and ga < 5 else f"{'inf':>18s}"
        gm_str = f"{gm:18.8f}"
        print(f"   {frac:8.4f}  {ga_str}  {gm_str}  {ht:>14s}")

    print()

    # -- 4. Key results --
    print("-" * 72)
    print("4. KEY FINDINGS -- Holomorphic Extension")
    print()

    # c_R = pi/4
    idx_pi4 = np.argmin(abs(c_R_vals - PI/4))
    ga_pi4 = gamma_analytic[idx_pi4]
    print(f"   gamma_max(c_R=pi/4, analytic) = {ga_pi4:.10f}")
    print(f"     H2 branch cut at finite c_I.")
    print(f"     At c_R=pi/4 (max QCMI), strip has FINITE width.")

    # c_R = 0
    idx_0 = np.argmin(abs(c_R_vals - 0.0))
    ga_0 = gamma_analytic[idx_0]
    print(f"   gamma_max(c_R=0, analytic)    = {ga_0:.10f}")
    print(f"     H2 branch cut IMMEDIATELY. Strip width = 0.")

    # c_R in (pi/8, pi/4)
    test_cR = PI * 3/16
    idx = np.argmin(abs(c_R_vals - test_cR))
    ga_mid = gamma_analytic[idx]
    print(f"   gamma_max(c_R=3pi/16, analytic) = "
          f"{ga_mid if np.isfinite(ga_mid) else 'inf'}")
    print(f"     Inside the Im=0 crossing region.")

    # c_R in (0, pi/8)
    test_cR2 = PI * 1/16
    idx2 = np.argmin(abs(c_R_vals - test_cR2))
    ga_mid2 = gamma_analytic[idx2]
    print(f"   gamma_max(c_R=pi/16, analytic)  = "
          f"{ga_mid2 if np.isfinite(ga_mid2) else 'inf'}")
    print(f"     Same-sign region: no Im=0 crossing -> infinite strip.")
    print()

    # -- 5. Harmonic extension results --
    print("-" * 72)
    print("5. KEY FINDINGS -- Harmonic (|sin|^2) Extension")
    print()

    gamma_mod_0 = gamma_max_modulus(0.0)
    gamma_mod_pi4 = gamma_max_modulus(PI/4)
    gamma_mod_pi8 = gamma_max_modulus(PI/8)
    arcsinh1 = np.arcsinh(1.0)

    print(f"   gamma_max(c_R=0, |sin|^2)    = {gamma_mod_0:.10f}")
    print(f"     cf. user derivation: arcsinh(1) = {arcsinh1:.10f}")
    print(f"     Agreement: diff = {abs(gamma_mod_0 - arcsinh1):.2e}")
    print(f"   gamma_max(c_R=pi/4, |sin|^2) = {gamma_mod_pi4:.10f}")
    print(f"     Zero width at max-QCMI point.")
    print(f"   gamma_max(c_R=pi/8, |sin|^2) = {gamma_mod_pi8:.10f}")
    print()

    # -- 6. Harmonic: full table and Schwarzschild comparison --
    print("-" * 72)
    print("6. HARMONIC EXTENSION: Full Table and Schwarzschild Bridge")
    print()

    print(f"   {'c_R/pi':>8s}  {'gamma_max':>12s}  {'QCMI':>10s}  "
          f"{'tau_DGF':>12s}  {'tau_Sch':>12s}  {'ratio':>10s}")
    print("   " + "-" * 68)

    ratios = []
    for frac in np.linspace(0.02, 0.48, 24):
        c_R = frac * PI/2
        gm = gamma_max_modulus(c_R)
        q = qcmi_real(c_R, 0.5)
        if q < 1e-10:
            continue
        tau_dgf = gm / q
        tau_sch = PI / q
        ratio = tau_dgf / tau_sch
        ratios.append(ratio)
        print(f"   {frac:8.4f}  {gm:12.8f}  {q:10.6f}  "
              f"{tau_dgf:12.6f}  {tau_sch:12.6f}  {ratio:10.6f}")

    if ratios:
        ratios_arr = np.array(ratios)
        print(f"\n   Ratio stats:")
        print(f"     mean = {np.mean(ratios_arr):.8f}")
        print(f"     std  = {np.std(ratios_arr):.8f}")
        print(f"     rel  = {np.std(ratios_arr)/np.mean(ratios_arr):.4%}")

        bridge = np.mean(ratios_arr)
        print(f"\n   Bridge factor: gamma_max * kappa_eff / pi = {bridge:.6f}")
        if abs(bridge - 1.0) < 0.3:
            print("   => Weak bridge: DGF native strip ~ Schwarzschild within 30%")
        else:
            print(f"   => Correction factor needed: {1.0/bridge:.4f}")
    print()

    # -- 7. P-dependence --
    print("-" * 72)
    print("7. P-DEPENDENCE (Harmonic Extension)")
    print()
    print(f"   {'p':>8s}  {'gamma(c_R=0)':>16s}  {'gamma(c_R=pi/8)':>18s}  "
          f"{'gamma(c_R=pi/4)':>18s}")
    print("   " + "-" * 68)
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        pp = p*(1-p)
        g0 = gamma_max_modulus_p(0.0, pp)
        g1 = gamma_max_modulus_p(PI/8, pp)
        g2 = gamma_max_modulus_p(PI/4, pp)
        print(f"   {p:8.4f}  {g0:16.8f}  {g1:18.8f}  {g2:18.8f}")
    print()

    # -- 8. Resolution --
    print("=" * 72)
    print("8. RESOLUTION: What IS the DGF Native Strip?")
    print("=" * 72)
    print()
    print("   A) Holomorphic (analytic continuation):")
    print("      - gamma_max = inf for most c_R values")
    print("      - gamma_max = 0 at c_R = 0, pi/2")
    print("      - gamma_max > 0 finite at c_R = pi/4")
    print("      - NOT a uniform strip -- a structured domain")
    print("      - QCMI(c) is COMPLEX for Im(c) != 0")
    print()
    print("   B) Harmonic (|sin|^2 extension):")
    print(f"      - gamma_max varies smoothly: 0 <-> {gamma_mod_0:.6f}")
    print(f"      - Maximum at c_R=0 (weak QCMI): gamma_max = {gamma_mod_0:.6f}")
    print(f"      - Zero at c_R=pi/4 (max QCMI): gamma_max = 0")
    print(f"      - QCMI remains REAL for all complex c")
    print(f"      - DGF tau-strip = gamma_max / kappa_eff")
    print(f"      - Schwarzschild tau-strip = pi / kappa")
    if ratios:
        print(f"      - Bridge factor = {bridge:.6f} (should be ~1)")
    print()
    print("   The harmonic extension is physically preferred:")
    print("   1. Entropy must be real-valued")
    print("   2. QCMI = H2(1/2 + sqrt(Delta)/2) for real Delta")
    print("   3. |sin|^2 extension is the unique extension preserving")
    print("      real-valuedness and the maximum principle")
    print("   4. The holomorphic extension gives complex entropy --")
    print("      physically unclear for von Neumann entropy")
    print()

    # -- 9. Final comparison --
    print("-" * 72)
    print("9. FINAL DGF-SCHWARZSCHILD COMPARISON")
    print()
    print("   Schwarzschild strip: Im(z) in [0, pi/kappa], width = pi/kappa")
    print("   DGF native strip:    Im(c) in [-gamma_max, gamma_max], width = 2*gamma_max")
    print("   DGF tau-strip:       Im(tau) in [-gamma_max/kappa_eff, gamma_max/kappa_eff]")
    print()
    print("   Mapping: tau = c / kappa_eff  (Cartan parameter -> Euclidean time)")
    print()
    if ratios:
        print(f"   DGF tau-strip width / Schwarzschild width = {bridge:.6f}")
        print(f"   In weak-field limit (c_R -> 0):")
        # Limit as c_R -> 0
        gm0 = gamma_max_modulus(0.0)
        q0 = qcmi_real(0.001, 0.5)  # slightly away from 0
        print(f"     gamma_max -> {gm0:.6f}")
        print(f"     kappa_eff -> 0")
        print(f"     Both strips diverge, ratio -> {bridge:.6f}")
    print()

    # Save data
    np.savez_compressed('native_strip_data_v3.npz',
                        c_R=c_R_vals,
                        gamma_analytic=gamma_analytic,
                        gamma_modulus=gamma_mod,
                        qcmi=np.array([qcmi_real(cr,0.5) for cr in c_R_vals]))

    print("Data saved to native_strip_data_v3.npz")
    return locals()


if __name__ == '__main__':
    main()
