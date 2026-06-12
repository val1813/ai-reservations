"""
Mutual decoherence clock: particles decohere EACH OTHER through shared env.
Feedback: particle A's QCMI -> env purity -> particle B's effective Cartan -> B's rate.
This is the DGF version of Kuramoto synchronization.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

def simulate_mutual(N=50, M=10, c0=0.5, T=5000, coupling=0.1, seed=42):
    """
    N particles, M shared environment qubits.
    Each particle has intrinsic Cartan c_i (slightly different).
    They share M env qubits; env purity evolves based on total QCMI.
    Particle i's effective Cartan: c_eff_i = c_i + coupling * (env_feedback_i)
    """
    rng = np.random.RandomState(seed)

    # Intrinsic Cartan parameters (slightly different)
    c_intrinsic = np.abs(rng.normal(c0, 0.05, N))
    c_intrinsic = np.clip(c_intrinsic, 0.1, np.pi/2 - 0.1)

    # Current effective Cartan (= intrinsic initially)
    c_eff = c_intrinsic.copy()

    # Phases
    phases = rng.random(N) * 2*np.pi

    # Environment: M qubits, each with purity q_j
    q_env = np.full(M, 0.5)  # start at max mixed

    # Tracking
    last_full_rotation = np.zeros(N)
    rotation_count = np.zeros(N, dtype=int)
    all_periods = [[] for _ in range(N)]

    period_history = []

    for t in range(T):
        # 1. Each particle rotates by c_eff
        phases += c_eff

        # 2. Check for full rotations
        for i in range(N):
            if phases[i] >= 2*np.pi:
                phases[i] -= 2*np.pi
                rotation_count[i] += 1

                if rotation_count[i] > 1:
                    period = t - last_full_rotation[i]
                    all_periods[i].append(period)
                last_full_rotation[i] = t

                # QCMI deposited: which env qubits?
                # Particle i couples to ~k env qubits
                k_coupled = max(1, M // N)
                env_indices = rng.choice(M, size=k_coupled, replace=False)

                # Each env qubit receives QCMI proportional to c_eff^2
                qcmi_per_env = eta_0 * c_eff[i]**2 / k_coupled

                for j in env_indices:
                    # QCMI deposition reduces env purity
                    q_env[j] *= (1.0 - qcmi_per_env)
                    q_env[j] = max(q_env[j], 0.01)

        # 3. Environment feedback: purity modulates effective Cartan
        # Each particle's env feedback = average purity of its coupled qubits
        for i in range(N):
            k_coupled = max(1, M // N)
            env_indices = rng.choice(M, size=k_coupled, replace=False)
            avg_q = np.mean(q_env[env_indices])

            # Feedback: low env purity -> reduce c_eff (less coherent rotation)
            # High env purity -> toward intrinsic c
            c_eff[i] = c_intrinsic[i] * (1.0 - coupling * (0.5 - avg_q))

            # Clamp
            c_eff[i] = np.clip(c_eff[i], 0.01, np.pi/2 - 0.01)

        # 4. Environment relaxation: purity slowly recovers
        q_env += 0.001 * (0.5 - q_env)  # drift back toward 0.5

        # Record
        if t % 200 == 0 and t > 500:
            current_periods = []
            for i in range(N):
                if len(all_periods[i]) > 5:
                    current_periods.append(np.mean(all_periods[i][-5:]))
            if len(current_periods) > N//2:
                period_history.append({
                    't': t,
                    'mean': np.mean(current_periods),
                    'std': np.std(current_periods),
                    'cv': np.std(current_periods)/np.mean(current_periods),
                    'avg_q_env': np.mean(q_env),
                })

    # Final statistics
    final_ps = []
    for i in range(N):
        if len(all_periods[i]) > 10:
            final_ps.append(np.mean(all_periods[i][-10:]))
    final_ps = np.array(final_ps)

    return {
        'N': N, 'M': M, 'coupling': coupling,
        'final_period_mean': np.mean(final_ps),
        'final_period_std': np.std(final_ps),
        'convergence': np.std(final_ps)/np.mean(final_ps),
        'period_history': period_history,
        'c_intrinsic_mean': np.mean(c_intrinsic),
        'c_intrinsic_std': np.std(c_intrinsic),
        'c_eff_final_mean': np.mean(c_eff),
        'c_eff_final_std': np.std(c_eff),
        'final_q_env': np.mean(q_env),
    }


print("=" * 70)
print("MUTUAL DECOHERENCE CLOCK")
print("Particles decohere each other through shared environment")
print("=" * 70)

# Scan coupling strength
for coupling in [0.01, 0.05, 0.1, 0.2, 0.5]:
    r = simulate_mutual(N=100, M=30, coupling=coupling, T=5000, seed=42)
    cv = r['convergence']
    sync = "SYNCHRONIZED" if cv < 0.02 else ("WEAK SYNC" if cv < 0.1 else "NOT SYNC")
    print(f"coupling={coupling:.2f}: T={r['final_period_mean']:.2f}, "
          f"CV={cv:.4f}, c_eff_std={r['c_eff_final_std']:.4f}, "
          f"q_env={r['final_q_env']:.4f} -> {sync}")

# Scan N (system size) at optimal coupling
print(f"\n{'='*70}")
print("THERMODYNAMIC LIMIT: Period vs N")
print(f"{'='*70}")
for N in [10, 30, 100, 300]:
    r = simulate_mutual(N=N, M=max(10, N//3), coupling=0.1, T=5000)
    print(f"N={N:4d}: T={r['final_period_mean']:.3f}, "
          f"CV={r['convergence']:.4f}, q_env={r['final_q_env']:.4f}")

# Show convergence over time
print(f"\n{'='*70}")
print("CONVERGENCE OVER TIME (N=100, coupling=0.1)")
print(f"{'='*70}")
r = simulate_mutual(N=100, M=30, coupling=0.1, T=5000, seed=123)
print(f"{'t':<8} {'T_mean':<10} {'CV':<10} {'q_env':<10}")
print("-" * 40)
for h in r['period_history'][::3]:
    print(f"{h['t']:<8} {h['mean']:<10.3f} {h['cv']:<10.4f} {h['avg_q_env']:<10.4f}")
