"""Derive mu(c,p) — decoherence amplification per causal ring."""
import numpy as np

def mu_analytic(c, p, n_samples=200000):
    """mu for edge-disjoint rings (Delta = sum of 4 independent {+-2,0})"""
    s = np.random.randint(0, 2, size=(n_samples, 4)) * 2 - 1
    sp = np.random.randint(0, 2, size=(n_samples, 4)) * 2 - 1
    Delta = np.sum(s - sp, axis=1)
    factor = p * np.exp(1j * c * Delta) + (1-p) * np.exp(-1j * c * Delta)
    ln_abs = np.log(np.maximum(np.abs(factor), 1e-15))
    return np.mean(ln_abs), np.std(ln_abs)

def mu_vertex_sharing(c, p, n_samples=200000):
    """mu for vertex-sharing (Delta from 2 qubits per ring)"""
    s = np.random.randint(0, 2, size=(n_samples, 2)) * 2 - 1
    sp = np.random.randint(0, 2, size=(n_samples, 2)) * 2 - 1
    Delta = np.sum(s - sp, axis=1)
    factor = p * np.exp(1j * c * Delta) + (1-p) * np.exp(-1j * c * Delta)
    ln_abs = np.log(np.maximum(np.abs(factor), 1e-15))
    return np.mean(ln_abs), np.std(ln_abs)

print("mu(c,p) -- Decoherence amplification per ring")
print("=" * 65)
print(f"{'c (rad)':<10} {'mu_edge':<12} {'sig_edge':<12} {'mu_vert':<12} {'sig_vert':<12}")
print("-" * 65)

for c in [0.1, 0.3, 0.5, 0.7, 0.9, np.pi/4, 1.2, 1.5]:
    mu_e, sig_e = mu_analytic(c, 0.5)
    mu_v, sig_v = mu_vertex_sharing(c, 0.5)
    print(f"{c:<10.4f} {mu_e:<12.6f} {sig_e:<12.6f} {mu_v:<12.6f} {sig_v:<12.6f}")

print()
print("Comparison with 2D grid measurement (c=0.5):")
print("  2D grid: mu ~ -0.47/ring")
mu_e, _ = mu_analytic(0.5, 0.5)
mu_v, _ = mu_vertex_sharing(0.5, 0.5)
print(f"  Edge-disjoint model: mu = {mu_e:.4f}/ring")
print(f"  Vertex-sharing model: mu = {mu_v:.4f}/ring")
print(f"  2D grid is between these (each ring shares 2 edges)")

print()
print("Critical rings for classicality (<|G|> < 1/d_sys):")
mu = mu_e
for n_bits in [5, 10, 20, 50, 100]:
    d = 2**n_bits
    n_crit = -np.log(d) / abs(mu)
    print(f"  d_sys=2^{n_bits}: {n_crit:.0f} rings to reach <|G|><1/d")

print()
print("Physical estimates:")
# Atom: ~10^5 internal causal rings
n_atom = 1e5
g_atom = np.exp(mu * n_atom)
print(f"  Atom (~10^5 rings): <|G|> ~ {g_atom:.2e}")
print(f"    -> {'CLASSICAL' if g_atom < 1e-3 else 'QUANTUM'} (|G|<<1?)")

# Dust grain: ~10^15 rings
n_dust = 1e15
g_dust = np.exp(mu * n_dust)
print(f"  Dust grain (~10^15 rings): <|G|> ~ 10^{{{np.log10(g_dust):.0f}}}")
print(f"    -> {'CLASSICAL' if g_dust < 1e-3 else 'QUANTUM'}")

# Football: ~10^23 rings
n_football = 1e23
print(f"  Football (~10^23 rings): <|G|> ~ exp({mu * n_football:.1e}) -> 0")
print(f"    -> PERFECTLY CLASSICAL")
