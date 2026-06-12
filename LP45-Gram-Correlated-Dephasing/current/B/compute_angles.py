"""
LP45 Rekindling Phase — B博士 Cross-Discipline Reframed
Computational analysis for Angles 2, 3, 6

Angle 2: Signal Processing — Walsh-Hadamard spectrum of G(x) and compressibility
Angle 3: Model Selection — AIC/BIC for Gram vs i.i.d. dephasing
Angle 6: Quantum Hypothesis Testing — distinguishability of Phi_gram vs Phi_iid
"""
import numpy as np
from scipy.special import comb, binom
from itertools import product, combinations
import warnings
warnings.filterwarnings('ignore')

# ================================================================
# Shared utilities
# ================================================================

def delta_r(x, r, b1):
    """Delta_r(a,b) for vertex-sharing chain. x = a XOR b in {0,1}-encoding.
    In spin encoding: s_i = (-1)^{bit_i}, sum = s_r + s_{r+1}.
    Delta_r = (s_r^a + s_{r+1}^a) - (s_r^b + s_{r+1}^b).
    For x = a XOR b, s_i^a * s_i^b = (-1)^{x_i}.
    Delta_r = 0 if (x_r, x_{r+1}) = (0,0)
            = +/-4 if (x_r, x_{r+1}) = (1,1) depends on a_r, but abs(Delta)=4
            = +/-2 if exactly one of x_r, x_{r+1} = 1
    Actually: sum(s_r^a + s_{r+1}^a) - (s_r^b + s_{r+1}^b)
    = s_r^a(1 - s_r^b) + s_{r+1}^a(1 - s_{r+1}^b)
    = s_r^a * 2 * x_r + s_{r+1}^a * 2 * x_{r+1}  (when bits differ)
    This depends on a (not just x) in general.

    For the Gram function G(x) = ∏ f_r(x) we average over a:
    G(x) = E_a[∏ cos(c * Δ_r(a, a⊕x))²]
    Actually: G(x) = ∏_r cos(c·Δ_r(a,b))² with a,b specific.
    For the WH transform we need G(x) at each x.

    Better approach: use the analytical factorization directly.
    """
    pass

def gram_Walsh_Hadamard_small(n, c, p=0.5, max_qubits=8):
    """
    Compute the Walsh-Hadamard transform c_z for small n.
    Builds the full Gram matrix G[a,b] and computes WH transform.

    G(x) = G[a, a⊕x] depends on x but NOT on a (translation invariant in Z_2^n).
    For vertex-sharing chain with n = b1+1 qubits:
    x is a binary vector of length n.

    For ring r connecting qubits (r, r+1):
    The Gram factor depends on Δ_r = sum_a - sum_b where sum = s_r + s_{r+1}.
    When spin = (-1)^bit: s^a * s^b = (-1)^{x} where x is XOR of bits.

    Let sum_a = s_r^a + s_{r+1}^a, sum_b = s_r^b + s_{r+1}^b.
    sum_a * sum_b = (s_r^a s_r^b) + (s_{r+1}^a s_{r+1}^b) + s_r^a s_{r+1}^b + s_{r+1}^a s_r^b
                  = (-1)^{x_r} + (-1)^{x_{r+1}} + (cross terms depend on a)

    But for p=0.5: factor = cos(c·Δ_r). cos is even, so |factor| depends on |Δ_r|.
    |Δ_r| ∈ {0, 2, 4}.
    - |Δ_r|=0 if x_r = x_{r+1} = 0
    - |Δ_r|=2 if exactly one of x_r, x_{r+1} = 1
    - |Δ_r|=4 if x_r = x_{r+1} = 1

    For each ring with 2 environment qubits (E_r, E'_r), total factor = cos(c·Δ_r)².

    So G(x) = ∏_{r=1}^{b1} cos(c·Δ_r(x))²
    where Δ_r(x) ∈ {0, 2, 4} depends only on (x_r, x_{r+1}).

    This is the translation-invariant Gram function.
    """
    d = 2**n
    if d > 2**max_qubits:
        raise ValueError(f"d={d} too large")

    b1 = n - 1
    # Compute G_fold(x) for all x — AVERAGE over background states a.
    # KEY FIX (BLOCK-1): For (x_r, x_{r+1}) = (1,1), |Δ_r| depends on
    # the background state a. The correct average is:
    #   f(1,1) = 0.5 * cos(4c)^2 + 0.5 * cos(0)^2 = 0.5*cos(4c)^2 + 0.5
    # B博士 originally used |Δ_r| = 4 for all backgrounds (wrong).
    G = np.zeros(d)
    for idx in range(d):
        x = np.array([(idx >> i) & 1 for i in range(n)], dtype=int)
        g_val = 1.0
        for r in range(b1):
            if x[r] == 0 and x[r+1] == 0:
                # |Δ_r| = 0 always
                factor = 1.0  # cos(0)^2 = 1
            elif x[r] == 1 and x[r+1] == 1:
                # BACKGROUND-AVERAGED: 50% of backgrounds give |Δ|=4, 50% give |Δ|=0
                factor = 0.5 * np.cos(c * 4)**2 + 0.5 * 1.0
            else:
                # Exactly one of x_r, x_{r+1} = 1 → |Δ_r| = 2 always
                factor = np.cos(c * 2)**2
            g_val *= factor
        G[idx] = g_val

    # Walsh-Hadamard transform: c_z = (1/d) * Σ_x G(x) * (-1)^{z·x}
    # Using fast Walsh-Hadamard transform (via Hadamard matrix recursion)
    H = np.ones(d) / np.sqrt(d)
    # Build the WH matrix efficiently
    c_z = np.zeros(d)
    for z_idx in range(d):
        z_bits = np.array([(z_idx >> i) & 1 for i in range(n)], dtype=int)
        # Direct computation
        val = 0.0
        for x_idx in range(d):
            x_bits = np.array([(x_idx >> i) & 1 for i in range(n)], dtype=int)
            parity = np.dot(z_bits, x_bits) % 2
            val += G[x_idx] * (1.0 if parity == 0 else -1.0)
        c_z[z_idx] = val / d

    # Also compute from eigenvalues for verification
    # The Gram matrix in Z_2^n basis: G[a,b] = G(a⊕b) = G(x)
    # Its eigenvalues are exactly d * c_z (because WH diagonalizes circulant matrices)

    return G, c_z


def compute_cz_distribution(n, c, p=0.5):
    """Compute c_z distribution and weight structure."""
    G, c_z = gram_Walsh_Hadamard_small(n, c, p)

    # Compute weight of each z
    weights = np.array([bin(z).count('1') for z in range(len(c_z))])

    # Average c_z by weight
    c_z_by_weight = {}
    for w in range(n+1):
        mask = weights == w
        if np.any(mask):
            c_z_by_weight[w] = {
                'mean': np.mean(c_z[mask]),
                'std': np.std(c_z[mask]),
                'min': np.min(c_z[mask]),
                'max': np.max(c_z[mask]),
                'count': np.sum(mask),
            }

    return c_z, c_z_by_weight, G


# ================================================================
# Angle 2: Signal Processing / Compressed Sensing
# ================================================================

def angle2_analysis():
    """Analyze Walsh-Hadamard spectrum compressibility."""
    print("=" * 72)
    print("ANGLE 2: Signal Processing / Compressed Sensing")
    print("=" * 72)

    for n in [3, 4, 5, 6]:
        b1 = n - 1
        for c_val, c_label in [(0.5, "0.5"), (np.pi/4, "pi/4")]:
            try:
                c_z, c_z_by_w, G = compute_cz_distribution(n, c_val)
                d = 2**n

                # Sparsity metrics
                sorted_cz = np.sort(np.abs(c_z))[::-1]
                # K-sparse approximation error
                for K in [1, 2, 4, 8]:
                    if K <= d:
                        residual = 1.0 - np.sum(sorted_cz[:K])
                        if K <= 4:
                            pass  # Print only for key K values

                # Effective sparsity: number of coefficients > 1e-6
                n_sig = np.sum(np.abs(c_z) > 1e-6)

                # Entropy of c_z distribution
                cz_pos = np.abs(c_z) + 1e-15
                cz_pos = cz_pos / np.sum(cz_pos)
                entropy = -np.sum(cz_pos * np.log2(cz_pos))
                max_entropy = np.log2(d)

                # Dominant weight
                weight_contributions = np.zeros(n+1)
                for w in range(n+1):
                    mask = np.array([bin(z).count('1') for z in range(d)]) == w
                    weight_contributions[w] = np.sum(np.abs(c_z[mask]))

                dominant_weight = np.argmax(weight_contributions)

                print(f"\nn={n}, b1={b1}, c={c_label}:")
                print(f"  Coefficients: {n_sig}/{d} > 1e-6")
                print(f"  Max |c_z|: {np.max(np.abs(c_z)):.4f}")
                print(f"  Top coeff: c_0={c_z[0]:.4f} (all-Z)")
                if d > 1:
                    top_idx = np.argsort(np.abs(c_z))[::-1][:5]
                    top_info = ", ".join(f"z={z}(w={bin(z).count('1')}): {c_z[z]:.4f}"
                                        for z in top_idx)
                    print(f"  Top 5: {top_info}")
                print(f"  Spectral entropy: {entropy:.2f} / {max_entropy:.1f} ({entropy/max_entropy*100:.1f}% of max)")
                print(f"  Dominant weight: w={dominant_weight} ({weight_contributions[dominant_weight]:.4f})")

                # Weight distribution
                weight_str = ", ".join(f"w={w}:{weight_contributions[w]:.3f}"
                                      for w in range(n+1) if weight_contributions[w] > 1e-6)
                print(f"  Weight dist: [{weight_str}]")

                # Compare with i.i.d. dephasing
                # For i.i.d. dephasing with per-qubit error rate p_z:
                # c_z = p_z^|z| * (1-p_z)^{n-|z|}
                # We can compute the "best fit" p_z and compare
                p_z_eff = 1 - np.exp(np.log(c_z[0]) / n) if c_z[0] > 0 else 0.5

            except Exception as e:
                print(f"  n={n}, c={c_label}: ERROR {e}")

    # Compressibility: how well do low-weight c_z approximate full channel?
    print("\n--- Compressibility Analysis ---")
    for n in [4, 5]:
        b1 = n - 1
        c_val = 0.5
        try:
            c_z, _, _ = compute_cz_distribution(n, c_val)
            d = 2**n

            # Truncation error at weight cutoff
            for w_cut in range(n+1):
                mask = np.array([bin(z).count('1') for z in range(d)]) <= w_cut
                approximate_sum = np.sum(c_z[mask])
                error = 1.0 - approximate_sum
                if w_cut <= 2 or w_cut == n:
                    print(f"  n={n}, c=0.5, truncate w≤{w_cut}: Σc_z≈{approximate_sum:.6f}, err={error:.6f}")
        except:
            pass

    return


# ================================================================
# Angle 3: Model Selection (AIC/BIC)
# ================================================================

def angle3_analysis():
    """Model selection: Gram vs i.i.d. dephasing."""
    print("\n" + "=" * 72)
    print("ANGLE 3: Model Selection — AIC/BIC for Gram vs i.i.d.")
    print("=" * 72)

    # Setup: n qubits, b1 = n-1 rings
    # Measurement: Pauli Z measurements in computational basis
    # Observed: transition counts T_{a→b} for N measurements

    # True model: Gram-correlated dephasing with c = 0.5
    c_true = 0.5
    p_true = 0.5

    for n in [3, 4, 5]:
        b1 = n - 1
        d = 2**n

        try:
            # Build the Gram channel transition probabilities
            # P(b|a) = |⟨b|Φ(|a⟩⟨a|)|b⟩|² = |G[a,b]|² (for pure dephasing)
            # Actually Φ(|a⟩⟨a|) has diagonal elements = 1/d and off-diagonal
            # coherences = G[a,b]. In computational basis, the diagonal
            # of Φ(|a⟩⟨a|) remains 1/d (only Z errors, no X).
            # Transition: P_gram(b|a) = probability of seeing |b⟩ from input |a⟩

            # For a pure Pauli Z channel: Φ(ρ) = Σ_z c_z Z^z ρ Z^z
            # P(b|a) = ⟨b| Φ(|a⟩⟨a|) |b⟩ = Σ_z c_z |⟨b|Z^z|a⟩|²
            # Z^z|a⟩ = (-1)^{z·a}|a⟩  (diagonal in computational basis!)
            # So P(b|a) = δ_{a,b} * Σ_z c_z  (only a=b survives)

            # Wait - this is wrong. For Pauli Z channel, the channel is
            # diagonal in computational basis, so it doesn't cause transitions.
            # The decoherence affects OFF-DIAGONAL elements of ρ.
            # To detect it, measure in X basis or prepare superposition.

            # Better approach: measure Pauli expectation values
            # ⟨Z_i⟩ in Gram model vs i.i.d. model

            # Correct approach for model selection:
            # Prepare |+⟩^⊗n state, apply channel, measure in X basis
            # |+⟩ has density ρ_0 = |+⟩⟨+|^⊗n
            # After channel: ρ = Σ_z c_z Z^z ρ_0 Z^z
            # Measure: P(x_out) = ⟨x_out| ρ |x_out⟩ in computational basis
            # (actually need to measure in X basis, or equivalently apply H^⊗n)

            # Simplified: measure in all Pauli bases (Pauli tomography)
            # P(a|P,z) = ⟨a| P Φ(|+⟩⟨+|^⊗n) P^† |a⟩ for P ∈ {I, X, Y}^⊗n
            # This gives 3^n × 2^n = 6^n measurement outcomes

            # Even simpler: just use the model's prediction for observables
            # and compute likelihood ratio

            # Compute c_z for Gram model
            c_z_gram, _, G_gram = compute_cz_distribution(n, c_true)

            # Compute optimal i.i.d. fit
            # For i.i.d. dephasing with rate p_per_qubit:
            # c_z_iid = (1-p)^(n-|z|) * p^|z|
            # Total dephasing: find p s.t. channel is "closest" to Gram

            # Fit p by matching c_0 (survival probability)
            c0_gram = c_z_gram[0]
            # For i.i.d.: c_0 = (1-p)^n
            p_iid_best = 1 - c0_gram**(1/n) if c0_gram > 0 else 1.0

            # Compute c_z for i.i.d. model
            c_z_iid = np.zeros(2**n)
            for z in range(2**n):
                w = bin(z).count('1')
                c_z_iid[z] = (1 - p_iid_best)**(n - w) * p_iid_best**w

            # Kullback-Leibler divergence
            kl_gram_iid = np.sum(c_z_gram * np.log((c_z_gram + 1e-15) / (c_z_iid + 1e-15)))

            # Compute expected likelihood ratio for N measurements
            # For Pauli channel tomography with M measurements per Pauli basis

            # AIC: 2k - 2ln(L)
            # Gram model: k_gram = n (one parameter c, plus ring structure encoded
            # in topology — but c is the single free parameter)
            # Actually: Gram model has 1 parameter (c), chain topology is known
            # i.i.d. model: could have n parameters (per-qubit rate) or 1 parameter (uniform)

            # For fair comparison: 1-parameter i.i.d. (uniform p)
            k_iid = 1
            k_gram = 1  # c is the only free parameter

            # Expected log-likelihood ratio for N measurements
            # Using Pauli tomography with N copies:
            # LLR = N * KL(gram || iid)
            # AIC difference: ΔAIC = 2(k_gram - k_iid) - 2 * N * KL

            # Number of measurements needed for ΔAIC < -2 (strong preference)
            N_strong = 1.0 / kl_gram_iid if kl_gram_iid > 1e-12 else np.inf

            print(f"\nn={n}, b1={b1}, c={c_true}:")
            print(f"  c_0 (Gram): {c0_gram:.6f}")
            print(f"  Best i.i.d. p: {p_iid_best:.6f}")
            print(f"  KL(Gram || i.i.d.): {kl_gram_iid:.6f} nats")
            print(f"  KL per qubit (approx): {kl_gram_iid/n:.6f}")
            print(f"  N needed for strong preference (ΔAIC<-2): {N_strong:.1f}")
            print(f"  N needed for 95% confidence (LLR): {3.84/kl_gram_iid:.1f}")

            # Check: does KL grow with n?
            # If KL ~ O(n), then distinguishability improves with system size
            # If KL ~ O(1), then it doesn't

            # Compare c_z distributions
            if n <= 4:
                print("  c_z (Gram) vs c_z (iid) by weight:")
                for w in range(n+1):
                    mask = np.array([bin(z).count('1') for z in range(2**n)]) == w
                    gram_avg = np.mean(c_z_gram[mask])
                    iid_avg = np.mean(c_z_iid[mask])
                    diff = abs(gram_avg - iid_avg)
                    print(f"    w={w}: Gram={gram_avg:.6f}, IID={iid_avg:.6f}, diff={diff:.6f}")

        except Exception as e:
            import traceback
            print(f"  n={n}: ERROR {e}")
            traceback.print_exc()

    # Scaling analysis
    print("\n--- Scaling Analysis ---")
    n_values = [3, 4, 5, 6]
    kl_values = []
    for n in n_values:
        try:
            c_z_gram, _, _ = compute_cz_distribution(n, 0.5)
            c0 = c_z_gram[0]
            p_iid = 1 - c0**(1/n) if c0 > 0 else 1.0
            c_z_iid = np.array([(1-p_iid)**(n-w) * p_iid**w
                               for z in range(2**n) for w in [bin(z).count('1')]])
            kl = np.sum(c_z_gram * np.log((c_z_gram + 1e-15) / (c_z_iid + 1e-15)))
            kl_values.append(kl)
            print(f"  n={n}: KL={kl:.6f}")
        except:
            kl_values.append(np.nan)

    # Fit KL = a * n + b
    valid = [(n, k) for n, k in zip(n_values, kl_values) if not np.isnan(k)]
    if len(valid) >= 2:
        ns, ks = zip(*valid)
        fit = np.polyfit(ns, ks, 1)
        print(f"  KL scaling: KL ≈ {fit[0]:.6f} * n + {fit[1]:.6f}")
        if abs(fit[0]) > 1e-4:
            print(f"  → KL grows with n: distinguishability IMPROVES with system size")
        else:
            print(f"  → KL ~ constant: distinguishability DOES NOT improve with system size")

    return


# ================================================================
# Angle 6: Quantum Hypothesis Testing
# ================================================================

def angle6_analysis():
    """Quantum hypothesis testing: distinguish Phi_gram vs Phi_iid."""
    print("\n" + "=" * 72)
    print("ANGLE 6: Quantum Metrology — Distinguishing Gram vs i.i.d. dephasing")
    print("=" * 72)

    # Quantum hypothesis testing:
    # H0: channel is Phi_iid (i.i.d. Pauli Z dephasing)
    # H1: channel is Phi_gram (Gram-correlated Z dephasing)

    # Both are Pauli Z channels with different c_z distributions.
    # For Pauli channels, the optimal probe state is maximally entangled
    # with an ancilla: |Ψ⁺⟩ = (1/√d) Σ_i |i⟩_S |i⟩_A

    # Quantum Chernoff bound:
    # P_e ≤ exp(-N * ξ) where ξ = -log(min_{0≤s≤1} Tr[ρ_0^s ρ_1^{1-s}])

    # For Pauli channels on maximally entangled state:
    # ρ_i = (Φ_i ⊗ I)(|Ψ⁺⟩⟨Ψ⁺|) = (1/d) Σ_z c_z^{(i)} |Φ_z⟩⟨Φ_z|
    # where |Φ_z⟩ are Bell states.

    # Tr[ρ_0^s ρ_1^{1-s}] = (1/d) Σ_z (c_z^{(0)})^s (c_z^{(1)})^{1-s}

    # This is independent of s for Pauli channels!
    # Wait: (c_z^{(0)})^s (c_z^{(1)})^{1-s} depends on s unless c_z^{(0)} = c_z^{(1)}
    # But we can compute the Chernoff distance numerically.

    c_true = 0.5

    for n in [2, 3, 4, 5]:
        b1 = n - 1
        d = 2**n

        try:
            # Compute c_z for true Gram channel
            c_z_gram, _, _ = compute_cz_distribution(n, c_true)

            # Best-fit i.i.d. channel
            c0 = c_z_gram[0]
            p_iid = 1 - c0**(1/n) if c0 > 0 else 1.0
            c_z_iid = np.array([(1-p_iid)**(n - bin(z).count('1')) * p_iid**bin(z).count('1')
                               for z in range(d)])

            # Quantum Chernoff bound
            # Chernoff distance: ξ = -log(Q) where Q = min_s Σ_z (c_z^{(0)})^s (c_z^{(1)})^{1-s}

            s_values = np.linspace(0, 1, 101)
            Q_values = np.zeros(len(s_values))
            for i, s in enumerate(s_values):
                Q_values[i] = np.sum((c_z_gram + 0)**s * (c_z_iid + 0)**(1-s))
            Q_min = np.min(Q_values)
            s_opt = s_values[np.argmin(Q_values)]

            xi = -np.log(max(Q_min, 1e-15))

            # Fidelity-based bound
            # F(ρ_0, ρ_1) = Tr[√(√ρ_0 ρ_1 √ρ_0)]
            # For Pauli channels with same eigenbasis: F = Σ_z √(c_z^{(0)} c_z^{(1)})
            fidelity = np.sum(np.sqrt(c_z_gram * c_z_iid))

            # Bures angle distance
            d_bures = np.sqrt(2 * (1 - fidelity))

            # Helstrom bound: P_e ≥ 0.5 * (1 - √(1 - F^N) * ...)  (complicated)
            # Simpler: 1 - F provides a distinguishability measure

            # Trace distance
            tvd = 0.5 * np.sum(np.abs(c_z_gram - c_z_iid))

            print(f"\nn={n}, b1={b1}:")
            print(f"  Chernoff distance ξ: {xi:.6f}")
            print(f"  Optimal s: {s_opt:.3f}")
            print(f"  Fidelity F(ρ_0, ρ_1): {fidelity:.6f}")
            print(f"  1 - F: {1-fidelity:.6f}")
            print(f"  Bures distance: {d_bures:.6f}")
            print(f"  Trace distance: {tvd:.6f}")
            print(f"  N for P_e < 0.05 (Chernoff): {int(np.ceil(np.log(0.05)/(-xi)))}")
            print(f"  N for P_e < 0.01 (Chernoff): {int(np.ceil(np.log(0.01)/(-xi)))}")

            # Also check: is the Quantum Chernoff distance larger than classical?
            # Classical: measure in some basis first
            # If classical KL ≪ quantum Chernoff: quantum advantage
            kl = np.sum(c_z_gram * np.log((c_z_gram + 1e-15) / (c_z_iid + 1e-15)))
            print(f"  KL divergence: {kl:.6f}")
            print(f"  Quantum/Classical ratio (ξ/KL): {xi/(kl+1e-15):.4f}")

        except Exception as e:
            print(f"  n={n}: ERROR {e}")

    # Scaling with n
    print("\n--- Scaling of Distinguishability ---")
    n_values = [2, 3, 4, 5]
    xi_values = []
    for n in n_values:
        try:
            c_z_gram, _, _ = compute_cz_distribution(n, 0.5)
            c0 = c_z_gram[0]
            p_iid = 1 - c0**(1/n) if c0 > 0 else 1.0
            c_z_iid = np.array([(1-p_iid)**(n - bin(z).count('1')) * p_iid**bin(z).count('1')
                               for z in range(2**n)])
            s_vals = np.linspace(0, 1, 101)
            Q = [np.sum(c_z_gram**s * c_z_iid**(1-s)) for s in s_vals]
            xi = -np.log(max(np.min(Q), 1e-15))
            xi_values.append(xi)
            print(f"  n={n}: ξ={xi:.6f}")
        except:
            xi_values.append(np.nan)

    valid = [(n, x) for n, x in zip(n_values, xi_values) if not np.isnan(x) and x > 1e-12]
    if len(valid) >= 2:
        ns, xs = zip(*valid)
        fit = np.polyfit(ns, xs, 1)
        print(f"  ξ scaling: ξ ≈ {fit[0]:.6f} * n + {fit[1]:.6f}")
        if fit[0] > 0.001:
            print(f"  → Distinguishability GROWS with n: Gram-specific correlations become MORE distinguishable at larger sizes")
        else:
            print(f"  → Distinguishability ~ constant or decreasing with n")

    return


# ================================================================
# Additional: c_z weight analysis (for Angles 2, 4)
# ================================================================

def weight_correlation_analysis():
    """Analyze whether c_z is dominated by low-weight z patterns."""
    print("\n" + "=" * 72)
    print("WEIGHT CORRELATION ANALYSIS (for Angles 2, 4)")
    print("=" * 72)

    for n in [4, 5, 6]:
        c_val = 0.5
        try:
            c_z, _, _ = compute_cz_distribution(n, c_val)
            d = 2**n

            # Compute the average c_z for each weight
            # and compare with product distribution
            c0 = c_z[0]
            # For product: c_z = ∏_i f_i(z_i) where f(0)=1-p_eff, f(1)=p_eff
            # Compute p_eff per qubit
            # Single-qubit marginals
            p_eff = np.zeros(n)
            for q in range(n):
                # Probability of Z on qubit q
                prob_z_q = 0.0
                for z in range(d):
                    if (z >> q) & 1:
                        prob_z_q += c_z[z]
                p_eff[q] = prob_z_q

            # Product prediction
            c_z_product = np.ones(d)
            for z in range(d):
                for q in range(n):
                    if (z >> q) & 1:
                        c_z_product[z] *= p_eff[q]
                    else:
                        c_z_product[z] *= (1 - p_eff[q])

            # Normalize
            c_z_product = c_z_product / np.sum(c_z_product)

            # Compare
            max_dev = np.max(np.abs(c_z - c_z_product))
            mean_dev = np.mean(np.abs(c_z - c_z_product))

            # Correlation: compute ⟨Z_i Z_j⟩ - ⟨Z_i⟩⟨Z_j⟩
            correlation = np.zeros((n, n))
            for i in range(n):
                for j in range(i+1, n):
                    E_Zi = np.sum([c_z[z] for z in range(d) if (z >> i) & 1])
                    E_Zj = np.sum([c_z[z] for z in range(d) if (z >> j) & 1])
                    E_ZiZj = np.sum([c_z[z] for z in range(d)
                                    if ((z >> i) & 1) and ((z >> j) & 1)])
                    correlation[i,j] = E_ZiZj - E_Zi * E_Zj

            corr_max = np.max(np.abs(correlation)) if n > 1 else 0

            print(f"\nn={n}:")
            print(f"  Max deviation from product: {max_dev:.6f}")
            print(f"  Mean deviation from product: {mean_dev:.6f}")
            print(f"  Max 2-body correlation: {corr_max:.6f}")

            # Check if the correlation is in the "errors are anti-correlated" direction
            if n > 1:
                # In Gram model, adjacent qubits share rings.
                # Ring r connects qubits r and r+1.
                # The Z errors should be correlated because cos(c·Δ_r)² depends
                # on (x_r, x_{r+1}) jointly.
                print("  2-body correlations (Z_i Z_j - Z_i Z_j):")
                for i in range(n):
                    for j in range(i+1, n):
                        if abs(correlation[i,j]) > 1e-6:
                            print(f"    ({i},{j}): {correlation[i,j]:.6f} "
                                  f"{'(adjacent)' if j==i+1 else '(non-adjacent)'}")

            # Is the correlation positive or negative?
            # Positive: Z errors on adjacent qubits happen TOGETHER more than expected
            # Negative: Z errors anti-correlated (one suppresses the other)
            if n > 1:
                adj_corr = correlation[range(n-1), range(1, n)]
                print(f"  Adjacent pair correlations: mean={np.mean(adj_corr):.6f}, "
                      f"min={np.min(adj_corr):.6f}, max={np.max(adj_corr):.6f}")
                if np.mean(adj_corr) > 1e-4:
                    print(f"  → Z errors on adjacent qubits are POSITIVELY correlated (cluster together)")
                elif np.mean(adj_corr) < -1e-4:
                    print(f"  → Z errors on adjacent qubits are NEGATIVELY correlated (anti-bunch)")
                else:
                    print(f"  → No significant 2-body correlation")

        except Exception as e:
            print(f"  n={n}: ERROR {e}")

    return


# ================================================================
# Tensor Network / MPO structure analysis (Angle 4)
# ================================================================

def tensor_network_analysis():
    """Analyze whether c_z has MPO structure with small bond dimension."""
    print("\n" + "=" * 72)
    print("ANGLE 4: Tensor Network / MPO Structure")
    print("=" * 72)

    # The Pauli transfer matrix for the Gram channel is:
    # T_{z,z'} = c_z δ_{z,z'}  (diagonal in Pauli basis)
    # where z ∈ {0,1}^n indexes Pauli Z strings.

    # An MPO representation of c_z as a function of the bits of z:
    # c_z = A^{(0)}_{α_0} A^{(z_1)}_{α_0,α_1} A^{(z_2)}_{α_1,α_2} ... A^{(z_{n-1})}_{α_{n-2},α_{n-1}} A^{(z_n)}_{α_{n-1}}

    # For i.i.d. dephasing: bond dimension χ = 1 (product state)
    # c_z = ∏_i p(z_i) where p(0) = 1-p, p(1) = p

    # For Gram: the factorization G(x) = ∏_r f_r(x_r, x_{r+1})
    # After Walsh-Hadamard, c_z is NOT a simple product.
    # But is c_z a matrix product state (MPS) in the z-basis?

    # Key observation: G(x) is a product of local factors:
    # G(x) = f_1(x_1, x_2) * f_2(x_2, x_3) * ... * f_{n-1}(x_{n-1}, x_n)
    # This is a 1D Markov random field.

    # Walsh-Hadamard transform: c_z = (1/d) Σ_x G(x) (-1)^{z·x}
    # Since G(x) = ∏_r f_r(x_r, x_{r+1}), the WH transform of a product
    # of local factors is a convolution in the frequency domain.

    # But the WH transform diagonalizes: (-1)^{z·x} = ∏_i (-1)^{z_i x_i}
    # So: c_z = (1/d) Σ_{x_1...x_n} [∏_r f_r(x_r, x_{r+1})] [∏_i (-1)^{z_i x_i}]
    # This IS a tensor network contraction.

    # Each f_r(x_r, x_{r+1}) acts on a 2×2 matrix:
    # F_r = [[f_r(0,0), f_r(0,1)], [f_r(1,0), f_r(1,1)]]

    # c_z can be computed as contraction of an MPS:
    # Bond dimension χ of f_r is at most 2 (since x_r is binary).
    # WH transform adds (2^2) = 4 but can be absorbed.

    # Actually, we can explicitly check:
    # G(x) is a Matrix Product State (normalized):
    # G(x_1...x_n) = L^T M_1(x_1) M_2(x_2) ... M_n(x_n) R
    # where M_i(x_i) is (χ_{i-1} × χ_i) matrix

    # For the vertex-sharing chain with nearest-neighbor factors f_r(x_r, x_{r+1}):
    # This is a 1D MRF with bond dimension χ = 2

    # After WH transform:
    # c_z = (1/d) Σ_x (-1)^{z·x} G(x)
    # = (1/d) Σ_x (∏_i (-1)^{z_i x_i}) (∏_r f_r(x_r, x_{r+1}))

    # Define T_i(z_i) = [[(-1)^{z_i·0}, 0], [0, (-1)^{z_i·1}]] = [[1,0],[0,(-1)^{z_i}]]
    # Then c_z = (1/d) Σ G(x) ∏ T_i(z_i) = (1/d) * (tensor contraction)

    # The combined tensor network has bond dimension χ = 2.
    # So c_z CAN be represented as an MPS with bond dimension χ = 2.

    # Let's verify numerically by computing c_z and checking SVD ranks.

    for n in [4, 5]:
        c_val = 0.5
        try:
            c_z, _, _ = compute_cz_distribution(n, c_val)
            d = 2**n

            # Reshape c_z as a function of bits: c_z[z_1, z_2, ..., z_n]
            c_z_tensor = np.zeros([2]*n)
            for z in range(d):
                bits = tuple((z >> i) & 1 for i in range(n))
                c_z_tensor[bits] = c_z[z]

            # Schmidt decomposition across cut at position k
            for k in range(1, n):
                # Left: qubits 0..k-1, Right: qubits k..n-1
                dim_left = 2**k
                dim_right = 2**(n-k)
                mat = c_z_tensor.reshape(dim_left, dim_right)
                U, S, Vt = np.linalg.svd(mat)
                # Number of singular values > 1e-10
                rank = np.sum(S > 1e-10)
                print(f"  n={n}, cut at k={k}: SVD rank = {rank} (max possible = {min(dim_left, dim_right)})")
                if rank <= 4:
                    print(f"    Non-zero SVs: {S[:rank]}")

            # Also compute MPO bond dimension for the channel itself
            # The channel Φ acts on n qubits and its PTM is diagonal
            # MPO of Φ is simpler: the Choi state has the same structure

        except Exception as e:
            print(f"  n={n}: ERROR {e}")

    return


# ================================================================
# RUN ALL
# ================================================================

if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True, linewidth=120)

    print("LP45 Rekindling — B博士 Cross-Discipline Computational Analysis")
    print("=" * 72)
    print()

    try:
        angle2_analysis()
    except Exception as e:
        print(f"Angle 2 FAILED: {e}")

    try:
        angle3_analysis()
    except Exception as e:
        print(f"Angle 3 FAILED: {e}")

    try:
        angle6_analysis()
    except Exception as e:
        print(f"Angle 6 FAILED: {e}")

    try:
        weight_correlation_analysis()
    except Exception as e:
        print(f"Weight correlation FAILED: {e}")

    try:
        tensor_network_analysis()
    except Exception as e:
        print(f"Tensor network FAILED: {e}")

    print("\nDone.")
