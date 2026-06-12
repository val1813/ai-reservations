"""
N rotating particles sharing environment. Decoherence-driven synchronization.
Each particle = causal ring. Equilibrium rotation rate = clock frequency.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

class Particle:
    def __init__(self, c, phase=0.0):
        self.c = c                    # Cartan parameter (rotation angle)
        self.phase = phase            # current rotation phase
        self.qcmi_accumulated = 0.0   # total QCMI deposited
        self.periods = []             # measured rotation periods

    def rotate(self, dt=1.0):
        """Advance phase by c per unit time (bare rotation)"""
        self.phase += self.c * dt
        return self.c * dt  # phase advance

    def qcmi_per_rotation(self):
        """QCMI deposited in one full rotation (2pi phase)"""
        return eta_0 * self.c**2

class Environment:
    def __init__(self, M, p=0.5):
        self.M = M              # number of environment qubits
        self.p = p              # environment purity
        self.qcmi_pool = 0.0    # accumulated QCMI
        self.reflux_rate = 0.01 # small reflux rate (T2 bound)

    def accept_qcmi(self, qcmi):
        self.qcmi_pool += qcmi

    def reflux(self):
        """Small information reflux back to particles"""
        refluxed = self.qcmi_pool * self.reflux_rate
        self.qcmi_pool -= refluxed
        return refluxed

def simulate(N=100, M=20, c_mean=0.5, c_std=0.1, T=1000, seed=42):
    """Simulate N particles sharing M environment qubits."""
    rng = np.random.RandomState(seed)
    env = Environment(M)

    # Create particles with slightly different Cartan parameters
    cs = np.abs(rng.normal(c_mean, c_std, N))
    cs = np.clip(cs, 0.05, np.pi/2 - 0.05)
    particles = [Particle(c, phase=rng.random()*2*np.pi) for c in cs]

    # Track rotation periods
    last_full_rotation = np.zeros(N)
    rotation_count = np.zeros(N, dtype=int)
    periods_history = []

    for t in range(T):
        # Each particle rotates
        for i, p in enumerate(particles):
            p.rotate()

            # Check for full rotation (phase crosses 2pi)
            if p.phase >= 2*np.pi:
                p.phase -= 2*np.pi
                rotation_count[i] += 1

                # Record period
                if rotation_count[i] > 1:
                    period = t - last_full_rotation[i]
                    p.periods.append(period)
                last_full_rotation[i] = t

                # Deposit QCMI to environment
                qcmi = p.qcmi_per_rotation()
                p.qcmi_accumulated += qcmi
                env.accept_qcmi(qcmi)

        # Environment reflux: small amount flows back, perturbs particles
        if t % 50 == 0 and env.qcmi_pool > 0:
            refluxed = env.reflux()
            # Reflux slightly adjusts Cartan parameters (information feedback)
            for p in particles:
                perturbation = refluxed / (N * 1000)
                p.c += rng.normal(0, perturbation)
                p.c = np.clip(p.c, 0.01, np.pi/2 - 0.01)

        # Record mean period every 100 steps
        if t % 100 == 0 and t > 200:
            mean_period = np.mean([np.mean(p.periods[-10:]) if len(p.periods)>=10
                                   else np.nan for p in particles
                                   if len(p.periods) > 0])
            if not np.isnan(mean_period):
                periods_history.append(mean_period)

    # Results
    final_periods = []
    for p in particles:
        if len(p.periods) > 10:
            final_periods.append(np.mean(p.periods[-10:]))

    final_periods = np.array(final_periods)

    return {
        'N': N, 'M': M,
        'initial_c_mean': c_mean,
        'initial_c_std': c_std,
        'final_period_mean': np.mean(final_periods),
        'final_period_std': np.std(final_periods),
        'period_convergence': np.std(final_periods) / np.mean(final_periods),
        'periods_history': periods_history,
        'total_qcmi': env.qcmi_pool,
        'total_rotations': sum(rotation_count),
    }


# Run simulations
print("=" * 70)
print("EQUILIBRIUM CLOCK: N particles + shared environment")
print("=" * 70)

for N in [10, 50, 200]:
    for M_ratio in [0.1, 0.5]:
        M = int(N * M_ratio)
        result = simulate(N=N, M=M, T=2000, seed=42)

        bare_period = 2*np.pi / result['initial_c_mean']
        equilibrium_period = result['final_period_mean']
        convergence = result['period_convergence']

        print(f"\nN={N}, M={M} (ratio={M_ratio}):")
        print(f"  Bare period (no coupling):  {bare_period:.2f}")
        print(f"  Equilibrium period:         {equilibrium_period:.2f}")
        print(f"  Period std/mean (convergence): {convergence:.4f}")
        print(f"  {'SYNCHRONIZED' if convergence < 0.05 else 'NOT SYNCHRONIZED'}")
        print(f"  Total QCMI deposited: {result['total_qcmi']:.1f} bits")
        print(f"  Total rotations: {result['total_rotations']}")

# ================================================================
# Key: does equilibrium period depend on environment size?
# ================================================================
print(f"\n{'='*70}")
print("KEY: EQUILIBRIUM PERIOD vs ENVIRONMENT SIZE")
print(f"{'='*70}")

M_vals = [1, 2, 5, 10, 20, 50, 100]
N_fixed = 50
periods = []
for M in M_vals:
    result = simulate(N=N_fixed, M=M, T=2000)
    periods.append(result['final_period_mean'])
    print(f"  M={M:3d}: T_eq = {result['final_period_mean']:.3f}, "
          f"convergence = {result['period_convergence']:.4f}")

# Does it stabilize?
period_changes = np.diff(periods)
print(f"\n  Period changes with increasing M: {period_changes}")
if np.all(np.abs(period_changes[-3:]) < 0.01):
    print("  -> Period STABILIZES with large M: THERMODYNAMIC LIMIT REACHED")
else:
    print("  -> Period still changing: need larger M")
