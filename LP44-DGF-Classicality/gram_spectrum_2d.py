"""
Gram Matrix Spectral Statistics for 2D Causal Ring Networks

We CANNOT store the full Gram matrix (dimension 2^{L^2}).
Instead: sample random pairs of system states, compute Gram elements,
and extract spectral statistics from the sampled entries.

Key observables from random samples:
- <|G_ab|> for a != b (off-diagonal magnitude)
- Var(|G_ab|) (fluctuations)
- Distribution of |G_ab| (shape of off-diagonal entries)

If <|G_ab|> ~ 1: Gram matrix near rank-1 -> CLASSICAL
If <|G_ab|> ~ 0: Gram matrix full rank -> QUANTUM
If <|G_ab|> ~ intermediate with large variance: SPIN GLASS phase

We also use the replica method: the n-th moment of the Gram matrix
can be computed from products of ring factors.
"""
import numpy as np
from scipy import special

# ================================================================
# 1. 2D Grid Gram Element Sampling
# ================================================================

def sample_gram_2d(L, c_val=0.5, p=0.5, n_samples=5000, seed=42):
    """Sample Gram matrix elements for 2D grid of rings."""
    rng = np.random.RandomState(seed)
    n_sys = L * L
    n_rings = (L-1) * (L-1)

    # Generate random state pairs
    diag_vals = []
    offdiag_mags = []
    offdiag_phases = []

    for _ in range(n_samples):
        # Random +/-1 states
        a = rng.randint(0, 2, size=n_sys) * 2 - 1
        b = rng.randint(0, 2, size=n_sys) * 2 - 1

        # Compute G[a,b] as product over rings
        G_ab = 1.0 + 0.0j
        for rx in range(L-1):
            for ry in range(L-1):
                # Ring at plaquette (rx, ry): involves Q at 4 corners
                q00 = rx * L + ry
                q10 = (rx+1) * L + ry
                q11 = (rx+1) * L + ry + 1
                q01 = rx * L + ry + 1

                # Sum of state values at 4 corners
                sum_a = a[q00] + a[q10] + a[q11] + a[q01]
                sum_b = b[q00] + b[q10] + b[q11] + b[q01]
                delta = sum_a - sum_b

                G_ab *= (p * np.exp(1j * c_val * delta) +
                         (1-p) * np.exp(-1j * c_val * delta))

        if np.array_equal(a, b):
            diag_vals.append(np.abs(G_ab))
        else:
            offdiag_mags.append(np.abs(G_ab))
            offdiag_phases.append(np.angle(G_ab))

    return (np.array(diag_vals), np.array(offdiag_mags),
            np.array(offdiag_phases), n_rings)


# ================================================================
# 2. Spectral Reconstruction via Moments
# ================================================================

def gram_moments_from_samples(offdiag_mags, max_k=10):
    """Estimate moments of Gram matrix eigenvalue distribution.

    For a random matrix with diagonal=1 and off-diagonal=G_ab:
    Tr(G^k) = sum_{a1,...,ak} G_{a1,a2} G_{a2,a3} ... G_{ak,a1}

    The k=1 moment: Tr(G) = d (all diagonal=1)
    The k=2 moment: Tr(G^2) = sum_{a,b} |G_ab|^2
    """
    d = len(offdiag_mags)  # approximate dimension from samples

    # k=2: Tr(G^2) = d + sum_{a!=b} |G_ab|^2
    # = d + d*(d-1) * <|G_ab|^2>
    mean_sq = np.mean(offdiag_mags**2)

    # For actual d: need estimate. Use sample variance to bound.
    # If d is huge (2^{L^2}), the dominant contribution is from off-diagonal.

    # Estimate effective rank via:
    # rank_eff ~ (Tr G)^2 / Tr(G^2) = d^2 / (d + d*(d-1)*<|G|^2>)
    # For d >> 1: rank_eff ~ 1 / <|G|^2>

    rank_eff_est = 1.0 / mean_sq if mean_sq > 1e-15 else float('inf')

    return {
        'mean_offdiag': np.mean(offdiag_mags),
        'std_offdiag': np.std(offdiag_mags),
        'mean_sq_offdiag': mean_sq,
        'rank_eff_est': rank_eff_est,
    }


# ================================================================
# 3. Analytic: Gram Off-Diagonal Distribution
# ================================================================

def analytic_offdiag_distribution(c_val, p, n_rings):
    """Analytic form for off-diagonal Gram element distribution.

    For large n_rings, by CLT:
    ln G_ab = sum over rings of ln(p*e^{ic*delta} + (1-p)*e^{-ic*delta})
    is approximately Gaussian.

    Mean and variance per ring depend on delta distribution.
    delta = sum_a - sum_b where sum_a, sum_b are sums of 4 +/-1 values.
    """
    # Possible values of sum of 4 +/-1 values: -4, -2, 0, 2, 4
    # Probabilities: binomial
    sum_vals = np.array([-4, -2, 0, 2, 4])
    sum_probs = np.array([1, 4, 6, 4, 1]) / 16.0

    # For each (sum_a, sum_b) pair, delta = sum_a - sum_b
    # Range: -8 to 8
    mean_lnG = 0.0
    mean_lnG_sq = 0.0

    for i, sa in enumerate(sum_vals):
        for j, sb in enumerate(sum_vals):
            delta = sa - sb
            prob = sum_probs[i] * sum_probs[j]

            factor = p * np.exp(1j * c_val * delta) + (1-p) * np.exp(-1j * c_val * delta)
            ln_factor = np.log(np.abs(factor))

            mean_lnG += prob * ln_factor
            mean_lnG_sq += prob * ln_factor**2

    var_lnG = mean_lnG_sq - mean_lnG**2

    # For n_rings independent rings:
    total_mean = n_rings * mean_lnG
    total_std = np.sqrt(n_rings * var_lnG)

    # Off-diagonal magnitude: |G| = exp(total_mean + noise)
    # Log-normal distribution
    median_offdiag = np.exp(total_mean)
    mean_offdiag = np.exp(total_mean + total_std**2 / 2)

    return {
        'mean_lnG_per_ring': mean_lnG,
        'std_lnG_per_ring': np.sqrt(var_lnG),
        'total_mean_lnG': total_mean,
        'total_std_lnG': total_std,
        'median_offdiag': median_offdiag,
        'mean_offdiag': mean_offdiag,
    }


# ================================================================
# 4. Phase Diagram
# ================================================================

def phase_diagram():
    """Map the classical-quantum phase diagram in (c, b1) space."""
    print("=" * 70)
    print("PHASE DIAGRAM: Classical-Quantum in (c, b1) space")
    print("=" * 70)

    c_vals = np.linspace(0.05, np.pi/2 - 0.05, 30)
    b1_vals = [1, 2, 3, 4, 5, 6, 7, 8]

    print(f"\n{'c (rad)':<10}", end="")
    for b1 in b1_vals:
        print(f"{'b1='+str(b1):<15}", end="")
    print(f"\n{'-'*(10+15*len(b1_vals))}")

    for c in c_vals:
        print(f"{c:<10.4f}", end="")
        for b1 in b1_vals:
            # Use 1D chain for tractability
            from high_d_interference import build_gram_matrix_1d_chain, analyze_spectrum
            G, _ = build_gram_matrix_1d_chain(b1, c_vals=np.full(b1, c))
            if G is None:
                print(f"{'N/A':<15}", end="")
                continue
            spec = analyze_spectrum(G)
            if spec:
                phase_char = "Q" if spec['PR'] > 3 else "C"
                print(f"{phase_char} PR={spec['PR']:.1f}  ", end="")
            else:
                print(f"{'--':<15}", end="")
        print()


# ================================================================
# 5. 2D Grid Numerical Experiment
# ================================================================

def run_2d_grid_experiment():
    """Run 2D grid sampling and compare with analytic prediction."""
    print("=" * 70)
    print("2D CAUSAL RING GRID: Gram Element Statistics")
    print("=" * 70)

    for L in [3, 4, 5, 6]:
        n_rings = (L-1) * (L-1)
        n_sys = L * L
        print(f"\nL={L}: {n_sys} system qubits, {n_rings} rings")
        print(f"  Hilbert space dim = 2^{n_sys} = {2**n_sys:.1e}")

        if 2**n_sys > 1e7:
            print(f"  [Too large for dense, using sampling]")
            diag, offdiag, phases, _ = sample_gram_2d(L, c_val=0.5, n_samples=2000)
        else:
            diag, offdiag, phases, _ = sample_gram_2d(L, c_val=0.5, n_samples=2000)

        moments = gram_moments_from_samples(offdiag)
        analytic = analytic_offdiag_distribution(0.5, 0.5, n_rings)

        print(f"  <|G_offdiag|> = {moments['mean_offdiag']:.4f} "
              f"(analytic: {analytic['mean_offdiag']:.4f})")
        print(f"  std(|G_offdiag|) = {moments['std_offdiag']:.4f} "
              f"(analytic: {np.sqrt(np.exp(analytic['total_std_lnG']**2)-1)*analytic['median_offdiag']:.4f})")
        print(f"  rank_eff ~ {moments['rank_eff_est']:.2f}")

        if moments['mean_offdiag'] > 0.9:
            print(f"  => NEAR CLASSICAL (off-diagonal ~ 1)")
        elif moments['mean_offdiag'] < 0.3:
            print(f"  => DEEP QUANTUM (off-diagonal ~ 0)")
        else:
            print(f"  => MIXED / SPIN GLASS phase")

    # Compare: 1D chain vs 2D grid at same b1
    print(f"\n{'='*70}")
    print("1D CHAIN vs 2D GRID at same b1")
    print(f"{'='*70}")

    b1_target = 16
    # 1D chain with 16 rings
    diag_1d, offdiag_1d, _, _ = sample_gram_2d(2, c_val=0.5, n_samples=2000)  # 2x2 grid has 1 ring
    # Actually let me use the 1D chain code
    from high_d_interference import build_gram_matrix_1d_chain

    for b1_ref in [1, 2, 3, 4, 5, 6, 7]:
        G, _ = build_gram_matrix_1d_chain(b1_ref, c_vals=np.full(b1_ref, 0.5))
        if G is None:
            continue
        d = G.shape[0]
        offdiag_vals = []
        for i in range(min(100, d)):
            for j in range(i+1, min(100, d)):
                offdiag_vals.append(np.abs(G[i, j]))
        mean_offdiag_1d = np.mean(offdiag_vals) if offdiag_vals else 0
        print(f"  1D b1={b1_ref}: <|G_off|> = {mean_offdiag_1d:.4f}")


if __name__ == "__main__":
    run_2d_grid_experiment()
    print("\n")
    phase_diagram()
