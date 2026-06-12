"""
Non-Equilibrium Steady State (NESS) as the origin of time dilation.

The clock = NESS of mutually decohering particles.
q-field changes the NESS balance point -> clock rate changes -> time dilation.

Compute: NESS frequency as function of q.
Show: f_clock(q) / f_clock(q_ref) = q/q_ref = exp(-Phi/c^2).
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

def ness_frequency(N=100, M=30, c0=0.5, q_env_init=0.5, T=3000, coupling=0.1, seed=42):
    """
    Compute NESS frequency for given environment purity q.
    Returns equilibrium <c_eff>.
    """
    rng = np.random.RandomState(seed)
    c_intrinsic = np.abs(rng.normal(c0, 0.05, N))
    c_intrinsic = np.clip(c_intrinsic, 0.1, np.pi/2 - 0.1)
    c_eff = c_intrinsic.copy()
    phases = rng.random(N) * 2*np.pi
    q_env = np.full(M, q_env_init)

    all_c_eff = []

    for t in range(T):
        phases += c_eff
        for i in range(N):
            if phases[i] >= 2*np.pi:
                phases[i] -= 2*np.pi
                k = max(1, M // N)
                indices = rng.choice(M, size=k, replace=False)
                qcmi = eta_0 * c_eff[i]**2 / k
                for j in indices:
                    q_env[j] *= (1.0 - qcmi)
                    q_env[j] = max(q_env[j], 0.01)

        for i in range(N):
            k = max(1, M // N)
            indices = rng.choice(M, size=k, replace=False)
            avg_q = np.mean(q_env[indices])
            c_eff[i] = c_intrinsic[i] * (1.0 - coupling * (0.5 - avg_q))
            c_eff[i] = np.clip(c_eff[i], 0.01, np.pi/2 - 0.01)

        q_env += 0.001 * (0.5 - q_env)

        if t > T//2:
            all_c_eff.append(np.mean(c_eff))

    return np.mean(all_c_eff[-T//4:]), np.std(all_c_eff[-T//4:])


print("=" * 70)
print("NESS FREQUENCY vs ENVIRONMENT PURITY q")
print("=" * 70)
print(f"{'q_env':<10} {'<c_eff>':<12} {'f/f_ref':<12} {'exp(-Phi/c^2) equiv':<25}")
print("-" * 60)

q_vals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
results = []
for q in q_vals:
    mean_c, std_c = ness_frequency(q_env_init=q, T=3000, seed=42)
    results.append((q, mean_c, std_c))

# Normalize to q=0.5 (reference)
ref_q = 0.5
ref_c = [r[1] for r in results if abs(r[0]-ref_q) < 0.01][0]

print(f"{'q_env':<10} {'<c_eff>':<12} {'<c>/<c>_ref':<14} {'q/q_ref':<12} {'match?':<10}")
print("-" * 60)
for q, mean_c, std_c in results:
    ratio = mean_c / ref_c
    expected = q / ref_q
    match = abs(ratio - expected) / expected < 0.1
    print(f"{q:<10.2f} {mean_c:<12.4f} {ratio:<14.4f} {expected:<12.4f} {str(match):<10}")

# ================================================================
# The key: does <c_eff>_eq ∝ q?
# ================================================================
qs = np.array([r[0] for r in results])
cs = np.array([r[1] for r in results])

# Fit: c = A * q^alpha
log_q = np.log(qs)
log_c = np.log(cs)
slope, intercept = np.polyfit(log_q, log_c, 1)
r2 = np.corrcoef(log_q, log_c)[0,1]**2

print(f"\n{'='*70}")
print("SCALING ANALYSIS")
print(f"{'='*70}")
print(f"<c_eff>_eq ∝ q^{slope:.3f}")
print(f"R^2 = {r2:.4f}")
print(f"Expected: slope = 1.0 (from q=exp(-Phi/c^2), dtau/dt=q)")
print(f"Measured: slope = {slope:.3f}")
print(f"Deviation: {abs(slope-1.0)*100:.1f}%")
