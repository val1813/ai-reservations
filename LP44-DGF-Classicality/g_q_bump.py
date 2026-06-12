"""
g(q) = g_floor + A * q(1-q)

Physical origin:
  g_floor: irreducible causal event rate (vacuum + thermal fluctuations)
  A*q(1-q): decoherence-driven excess, peaks at q=0.5

The BUMP at intermediate q suppresses H_meas, mimicking dark energy.
"""
import numpy as np

def g_q(q, g_floor=0.97, A=3.0):
    """dt/dT — measured time per true time"""
    return g_floor + A * q * (1.0 - q)

def q_of_a(a, q_vac=0.99, beta=2.0, a_star=0.5):
    x = (a / a_star) ** beta
    return q_vac * x / (1.0 + x)

def H_meas(a, H0=70.0, g_floor=0.97, A=3.0, q_vac=0.99, beta=2.0, a_star=0.5):
    q = q_of_a(a, q_vac, beta, a_star)
    g = g_q(q, g_floor, A)
    H_true = H0 * a**(-1.5)
    return H_true / max(g, 1e-10)

def H_lcdm(z, H0=70.0, Om=0.3):
    a = 1.0/(1.0+z)
    return H0 * np.sqrt(Om * a**(-3) + (1-Om))

# Grid search
print("=" * 70)
print("g(q) = g_floor + A*q(1-q)  —  BUMP MODEL")
print("=" * 70)

best_chi2 = np.inf
best = None
for g_floor in [0.90, 0.93, 0.95, 0.97, 0.98, 0.99]:
    for A in [1.0, 2.0, 3.0, 4.0, 5.0, 8.0, 10.0]:
        for beta in [1.0, 1.5, 2.0, 2.5, 3.0]:
            for a_star in [0.3, 0.4, 0.5, 0.6, 0.7]:
                for q_vac in [0.95, 0.98, 0.99, 0.999]:
                    chi2 = 0
                    for z in [0, 0.5, 1.0, 1.5, 2.0]:
                        a = 1.0/(1.0+z)
                        Hd = H_meas(a, 70.0, g_floor, A, q_vac, beta, a_star)
                        Hl = H_lcdm(z)
                        chi2 += ((Hd-Hl)/Hl)**2
                    if chi2 < best_chi2:
                        best_chi2 = chi2
                        best = (g_floor, A, q_vac, beta, a_star)

gf, A, qv, bt, ast = best
print(f"Best: g_floor={gf:.4f}, A={A:.2f}, q_vac={qv:.4f}, beta={bt:.2f}, a_star={ast:.2f}")
print(f"Chi2 = {best_chi2:.4f}")

# Detailed comparison
print(f"\n{'z':<8} {'q':<10} {'g(q)':<10} {'H_DGF':<12} {'H_LCDM':<12} {'Diff':<10}")
print("-" * 62)
for z in [0, 0.2, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
    a = 1.0/(1.0+z)
    q = q_of_a(a, qv, bt, ast)
    g = g_q(q, gf, A)
    Hd = H_meas(a, 70.0, gf, A, qv, bt, ast)
    Hl = H_lcdm(z)
    diff = (Hd-Hl)/Hl*100
    print(f"{z:<8.2f} {q:<10.4f} {g:<10.4f} {Hd:<12.2f} {Hl:<12.2f} {diff:<+10.2f}%")

# Show the BUMP
print(f"\n{'='*70}")
print("THE g(q) BUMP — Physical origin of dark energy in DGF")
print(f"{'='*70}")
qs = np.linspace(0.01, 0.99, 50)
gs = [g_q(q, gf, A) for q in qs]
peak_q = qs[np.argmax(gs)]
peak_g = max(gs)
print(f"g(q) peaks at q={peak_q:.2f} with g={peak_g:.3f}")
print(f"At q->0: g->{gf:.3f}, at q->1: g->{gf:.3f}")
print(f"Peak height above floor: {peak_g-gf:.3f}")
print(f"-> This peak suppresses H(z) at intermediate z by factor ~{peak_g:.1f}x")
print(f"-> Equivalent to Omega_m ~ 1/{peak_g**2:.1f} ~ {1/peak_g**2:.2f}")
print(f"-> LambdaCDM: Omega_m = 0.3")
