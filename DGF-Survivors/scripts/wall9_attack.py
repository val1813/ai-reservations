"""
Wall #9 Attack: QCMI → Decoherence Rate Quantitative Mapping

Path C (numerical first): Compute decoherence measures for vertex-sharing
causal rings, map them to QCMI, and fit the functional form.

Key questions:
1. Does per-qubit decoherence scale with b1?
2. Does global decoherence scale with b1?
3. What functional form best describes QCMI → decoherence?
4. At what QCMI does "effective classicality" (D > 0.99) emerge?
"""

import numpy as np
from itertools import product
import sys
sys.path.insert(0, 'D:/Claude/ai-reservations/DGF-Survivors')

from b1_scaling import (
    CausalGraph, von_neumann_entropy,
    make_vertex_sharing_chain, make_disjoint_rings
)


# =========================================================================
# EXTENDED DECOHERENCE MEASURES
# =========================================================================

def compute_decoherence_measures(graph, p=0.5):
    """
    Compute multiple decoherence measures for a causal graph.

    Returns dict with:
    - qcmi: QCMI in bits
    - G: full Gram matrix (d_s x d_s)
    - d_per_qubit: per-qubit off-diagonal decay (list, one per system qubit)
    - d_global_max: decoherence between most distinct states (all +1 vs all -1)
    - d_avg_offdiag: average off-diagonal magnitude
    - d_choi_purity: 1 - purity of Choi state
    - d_rank_deficit: rank deficit measure
    - gram_eigenvalues: eigenvalues of G (sorted descending)
    """
    d_s = graph.d_s
    G = graph.gram_matrix(p)

    # QCMI
    qcmi, Srq, Seq, Sq = graph.qcmi(p)

    # === 1. Per-qubit off-diagonal decay ===
    # For each system qubit q, compute the reduced 2x2 Gram matrix
    # by tracing out all other system qubits.
    # d_q = 1 - 2|ρ_{01}| where ρ_{01} is the off-diagonal element
    d_per_qubit = []
    n_sys = len(graph.S)

    for target_q in range(n_sys):
        # Build the reduced Gram matrix for qubit target_q
        # We need to sum G_{(s_0,...,s_{b1}),(t_0,...,t_{b1})}
        # where s_j = t_j for all j != target_q

        # For efficiency, iterate over configurations of OTHER system qubits
        other_qubits = [j for j in range(n_sys) if j != target_q]
        n_other = len(other_qubits)

        offdiag_sum = 0.0 + 0.0j
        diag_sum = 0.0

        for other_config in product([0, 1], repeat=n_other):
            # Build the two full system configs:
            # config_0: target_q = 0, others = other_config
            # config_1: target_q = 1, others = other_config
            idx_0_list = [0] * n_sys
            idx_1_list = [0] * n_sys
            idx_0_list[target_q] = 0
            idx_1_list[target_q] = 1
            for j_idx, q_idx in enumerate(other_qubits):
                idx_0_list[q_idx] = other_config[j_idx]
                idx_1_list[q_idx] = other_config[j_idx]

            # Convert to linear indices
            def to_linear(config_list):
                idx = 0
                for i, s in enumerate(config_list):
                    idx = (idx << 1) | s
                return idx

            a = to_linear(idx_0_list)
            b = to_linear(idx_1_list)

            offdiag_sum += G[a, b]
            diag_sum += G[a, a]  # should be 1 always

        # Normalize by d_s = 2^{n_sys} (correct density matrix normalization)
        rho_01 = offdiag_sum / d_s
        rho_00 = diag_sum / d_s
        # rho_00 = rho_11 = 1/2 always, so coherence C = 2|rho_01|
        coherence = 2.0 * abs(rho_01)
        d_q = float(np.real(1.0 - coherence))
        d_per_qubit.append(d_q)

    # === 2. Global decoherence: all +1 vs all -1 ===
    # These are the most distinct system states
    idx_all_plus = 0
    idx_all_minus = d_s - 1
    # Actually, all +1 (spin +1 = bit 0) is index 0
    # all -1 (spin -1 = bit 1) is index d_s-1
    G_global_offdiag = abs(G[0, d_s - 1])
    d_global_max = 1.0 - G_global_offdiag

    # === 3. Average off-diagonal magnitude ===
    offdiag_vals = []
    for a in range(d_s):
        for b in range(a + 1, d_s):
            offdiag_vals.append(abs(G[a, b]))
    d_avg_offdiag = 1.0 - np.mean(offdiag_vals)

    # === 4. Choi state purity ===
    # Choi state = (I ⊗ E)(|Φ⁺⟩⟨Φ⁺|) has density matrix G/d_s on
    # the correlated subspace. Purity = Tr(ρ²)
    rho_Q = G / d_s
    purity = np.real(np.trace(rho_Q @ rho_Q))
    d_choi_purity = 1.0 - purity

    # === 5. Rank deficit ===
    # How far from unitary (rank-1 G)?
    evals = np.linalg.eigvalsh(G)
    evals = np.sort(evals)[::-1]
    evals = np.maximum(evals, 0)  # clip numerical negatives
    evals = evals / evals.sum()
    # Effective rank: 1 / sum(lambda_i^2) = 1 / purity_of_evals
    eff_rank = 1.0 / np.sum(evals ** 2)
    d_rank_deficit = 1.0 - 1.0 / eff_rank

    return {
        'qcmi': qcmi,
        'Srq': Srq,
        'Seq': Seq,
        'Sq': Sq,
        'G': G,
        'd_per_qubit': d_per_qubit,
        'd_global_max': d_global_max,
        'd_avg_offdiag': d_avg_offdiag,
        'd_choi_purity': d_choi_purity,
        'd_rank_deficit': d_rank_deficit,
        'gram_eigenvalues': evals,
        'global_offdiag': G_global_offdiag,
    }


def analytic_per_qubit_decoherence(b1, c, p=0.5):
    """
    Analytic formula for per-qubit decoherence in vertex-sharing chain.

    G_{a,b} = prod_{r=0}^{b1-1} cos²(c*(Δ_r + Δ_{r+1}))

    For qubit Q_k:
    - Δ_k = ±2, all other Δ = 0
    - Q_k participates in ring k-1 (as Q_b) and ring k (as Q_a)
    - For r = k-1: Δ_{k-1} + Δ_k = 0 + (±2) = ±2 → cos²(2c)
    - For r = k: Δ_k + Δ_{k+1} = (±2) + 0 = ±2 → cos²(2c)
    - All other r: Δ_r = 0 → cos²(0) = 1

    So off-diagonal = (1/2) * cos²(2c)^{n_rings_participated}
    where n_rings = 1 for endpoints (k=0, k=b1), 2 for interior qubits

    Returns list of per-qubit decoherence values.
    """
    cos2_2c = np.cos(2*c)**2
    result = []
    for k in range(b1 + 1):
        if k == 0 or k == b1:
            n_rings = 1  # endpoint
        else:
            n_rings = 2  # interior
        coherence = cos2_2c ** n_rings
        result.append(1.0 - coherence)
    return result


def analytic_global_decoherence(b1, c):
    """
    Analytic decoherence between all-spin-up and all-spin-down states.

    For all Δ_r = 2 (full flip):
    G = prod_{r=0}^{b1-1} cos²(c*(2+2)) = cos²(4c)^{b1}

    Returns global decoherence D = 1 - cos²(4c)^{b1}
    """
    return 1.0 - np.cos(4*c)**(2*b1)


# =========================================================================
# PARAMETER SCAN
# =========================================================================

def scan_qcmi_vs_decoherence():
    """Main scan: QCMI vs decoherence for vertex-sharing chains."""

    print("=" * 70)
    print("WALL #9: QCMI → Decoherence Rate Quantitative Mapping")
    print("=" * 70)

    # Parameter grid
    b1_values = [1, 2, 3, 4, 5]
    c_values = [0.1, 0.3, 0.5, 0.7, 1.0]
    p = 0.5

    results = []

    for b1 in b1_values:
        for c in c_values:
            g = make_vertex_sharing_chain(b1, c_val=c)
            meas = compute_decoherence_measures(g, p)

            # Also compute analytic predictions
            d_per_qubit_analytic = analytic_per_qubit_decoherence(b1, c, p)
            d_global_analytic = analytic_global_decoherence(b1, c)

            results.append({
                'b1': b1,
                'c': c,
                **meas,
                'd_per_qubit_analytic': d_per_qubit_analytic,
                'd_global_analytic': d_global_analytic,
            })

            print(f"b1={b1}, c={c:.1f}: QCMI={meas['qcmi']:.4f}, "
                  f"d_global={meas['d_global_max']:.4f} (analytic={d_global_analytic:.4f}), "
                  f"d_q0={meas['d_per_qubit'][0]:.4f}, "
                  f"d_avg_offdiag={meas['d_avg_offdiag']:.4f}")

    return results


def detailed_b1_scan(c_fixed=0.5):
    """Detailed scan over b1 at fixed c."""

    print("\n" + "=" * 70)
    print(f"DETAILED SCAN: c = {c_fixed}")
    print("=" * 70)

    b1_values = list(range(1, 11))
    p = 0.5

    print(f"{'b1':>4s} {'QCMI':>8s} {'per_ring':>10s} "
          f"{'d_global':>10s} {'d_q0':>8s} {'d_q1':>8s} "
          f"{'d_avg_off':>10s} {'d_choi':>10s} {'d_rank':>10s} "
          f"{'eff_rank':>10s}")
    print("-" * 90)

    for b1 in b1_values:
        g = make_vertex_sharing_chain(b1, c_val=c_fixed)
        meas = compute_decoherence_measures(g, p)

        d_q0 = meas['d_per_qubit'][0]
        d_q1 = meas['d_per_qubit'][1] if b1 >= 1 else np.nan
        eff_rank = 1.0 / (1.0 - meas['d_rank_deficit']) if meas['d_rank_deficit'] < 1 else np.inf

        print(f"{b1:4d} {meas['qcmi']:8.4f} {meas['qcmi']/b1:10.4f} "
              f"{meas['d_global_max']:10.6f} {d_q0:8.4f} {d_q1:8.4f} "
              f"{meas['d_avg_offdiag']:10.6f} {meas['d_choi_purity']:10.6f} "
              f"{meas['d_rank_deficit']:10.6f} {eff_rank:10.2f}")


def c_scan_at_b1(b1_fixed=5):
    """Scan c at fixed b1 to understand the c-dependence."""

    print(f"\n" + "=" * 70)
    print(f"DETAILED SCAN: b1 = {b1_fixed}, varying c")
    print("=" * 70)

    c_values = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
                np.pi/8, np.pi/6, np.pi/5, np.pi/4, np.pi/3, 3*np.pi/8,
                np.pi/2 - 0.01, np.pi/2]
    p = 0.5

    print(f"{'c':>10s} {'QCMI':>8s} {'d_global':>10s} {'d_q0':>8s} "
          f"{'d_q_int':>8s} {'d_avg':>10s} {'G_01_global':>12s}")
    print("-" * 75)

    for c in c_values:
        g = make_vertex_sharing_chain(b1_fixed, c_val=c)
        meas = compute_decoherence_measures(g, p)

        # Interior qubit decoherence (Q_1 for b1 >= 2)
        d_q_int = meas['d_per_qubit'][1] if b1_fixed >= 2 else np.nan

        print(f"{c:10.4f} {meas['qcmi']:8.4f} {meas['d_global_max']:10.6f} "
              f"{meas['d_per_qubit'][0]:8.4f} {d_q_int:8.4f} "
              f"{meas['d_avg_offdiag']:10.6f} {meas['global_offdiag']:12.8f}")


def fit_analysis(results):
    """Fit functional forms for QCMI vs decoherence."""

    print("\n" + "=" * 70)
    print("FIT ANALYSIS")
    print("=" * 70)

    # Extract data for fitting
    qcmi_vals = np.array([r['qcmi'] for r in results])
    d_global_vals = np.array([r['d_global_max'] for r in results])
    d_avg_vals = np.array([r['d_avg_offdiag'] for r in results])
    d_choi_vals = np.array([r['d_choi_purity'] for r in results])

    # Group by b1 and c for structured analysis
    from collections import defaultdict

    # For each c, plot D_global vs QCMI (which varies with b1)
    print("\n--- D_global vs QCMI (varying b1, fixed c) ---")

    for c in sorted(set(r['c'] for r in results)):
        subset = [r for r in results if abs(r['c'] - c) < 1e-10]
        xs = np.array([r['qcmi'] for r in subset])
        ys = np.array([r['d_global_max'] for r in subset])

        if len(xs) < 3:
            continue

        # Fit: D = 1 - exp(-gamma * QCMI)
        # Linearize: ln(1 - D) = -gamma * QCMI
        valid = (ys < 0.999)  # avoid log(0)
        if np.sum(valid) >= 2:
            x_valid = xs[valid]
            y_valid = ys[valid]

            # Power law: D = A * QCMI^beta
            # Linearize: log(D) = log(A) + beta * log(QCMI)
            valid2 = (y_valid > 0)
            if np.sum(valid2) >= 2:
                x2 = x_valid[valid2]
                y2 = y_valid[valid2]
                coeffs = np.polyfit(np.log(x2), np.log(y2), 1)
                beta = coeffs[0]
                A = np.exp(coeffs[1])

                # Exponential: D = 1 - exp(-gamma * QCMI)
                # gamma = -ln(1-D)/QCMI
                gamma_vals = -np.log(np.maximum(1 - y2, 1e-15)) / x2
                gamma = np.mean(gamma_vals)

                print(f"  c={c:.1f}: power-law beta={beta:.3f} A={A:.4f}, "
                      f"exp-gamma={gamma:.3f}")

    # === Fit to analytic prediction ===
    print("\n--- Analytic Formula Verification ---")
    print("Comparing numerical G_{0,d_s-1} with cos²(4c)^{b1}:")

    for r in results:
        if r['b1'] > 3:
            continue
        analytic_G = np.cos(4*r['c'])**(2*r['b1'])
        numeric_G = r['global_offdiag']
        match = "MATCH" if abs(analytic_G - numeric_G) < 1e-10 else f"DIFF={abs(analytic_G-numeric_G):.2e}"
        print(f"  b1={r['b1']}, c={r['c']:.1f}: numeric={numeric_G:.8f}, "
              f"analytic={analytic_G:.8f} [{match}]")


def derive_qcmi_decoherence_formula():
    """Derive the analytic QCMI → decoherence formula."""

    print("\n" + "=" * 70)
    print("ANALYTIC DERIVATION")
    print("=" * 70)

    print("""
    For vertex-sharing chain with uniform Cartan parameter c:

    Gram matrix element:
      G_{a,b} = ∏_{r=0}^{b1-1} cos²(c*(Δ_r + Δ_{r+1}))
      where Δ_r = σ_r(b) - σ_r(a) ∈ {0, ±2}

    1. GLOBAL DECOHERENCE (all +1 vs all -1 states):
       Δ_r = 2 for all r
       G_{all+, all-} = ∏_{r} cos²(4c) = cos²(4c)^{b1}
       D_global = 1 - cos²(4c)^{b1}

    2. PER-QUBIT DECOHERENCE:
       For qubit Q_k, Δ_k = ±2, all other Δ = 0
       Q_k participates in rings k-1 and k (interior) or just one ring (endpoint)
       Endpoint (k=0): G_off = cos²(2c)
       Interior (0<k<b1): G_off = cos²(2c)² = cos⁴(2c)
       D_q = 1 - cos²(2c)^{n_rings}

    3. QCMI (asymptotic, from Wall A results):
       QCMI ≈ b1 * η(c)  where η(c) ≈ 1.0 bit/ring at c=0.5
       More precisely: η(c) depends on Perron-Frobenius eigenvalue of MPO

    4. MAPPING QCMI → DECOHERENCE:
       For global decoherence:
         1 - D_global = exp(b1 * ln(cos²(4c)))
         = exp(QCMI * ln(cos²(4c)) / η(c))

       So: γ_dec(b1) = -b1 * ln(cos²(4c))
       And: γ_dec ∝ QCMI with constant κ(c) = -ln(cos²(4c)) / η(c)
    """)

    # Compute κ(c) for various c values
    print("\nProportionality constant κ(c) = γ_dec / QCMI = -ln(cos²(4c)) / η(c):")
    print(f"{'c':>8s} {'cos(4c)':>10s} {'ln(cos²(4c))':>15s} {'η(c)':>8s} {'κ(c)':>10s}")
    print("-" * 55)

    for c in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        cos4c = np.cos(4*c)
        ln_cos2 = 2 * np.log(abs(cos4c) + 1e-15)

        # Estimate η(c) from the Perron-Frobenius eigenvalue
        # For b1=5, compute QCMI and divide by b1 for the asymptotic η
        g = make_vertex_sharing_chain(5, c_val=c)
        qcmi, _, _, _ = g.qcmi(0.5)
        eta = qcmi / 5.0

        kappa = -ln_cos2 / max(eta, 0.001)

        print(f"{c:8.3f} {cos4c:10.4f} {ln_cos2:15.6f} {eta:8.4f} {kappa:10.3f}")


def physical_interpretation():
    """Physical interpretation of the results."""

    print("\n" + "=" * 70)
    print("PHYSICAL INTERPRETATION")
    print("=" * 70)

    # At what b1 does D_global > 0.99?
    print("\n--- Critical b1 for D_global > 0.99 ---")

    for c in [0.1, 0.3, 0.5, 0.7, 1.0]:
        cos4c_sq = np.cos(4*c)**2
        if cos4c_sq >= 0.99:
            print(f"  c={c:.1f}: cos²(4c)={cos4c_sq:.4f} >= 0.99, D never reaches 0.99 (cos²(4c) too close to 1)")
            continue
        if cos4c_sq <= 0:
            print(f"  c={c:.1f}: cos²(4c)≈0, D achieves 0.99 at b1=1")
            continue

        # D = 1 - cos²(4c)^{b1} > 0.99
        # cos²(4c)^{b1} < 0.01
        # b1 * ln(cos²(4c)) < ln(0.01)
        b1_crit = np.ceil(np.log(0.01) / np.log(cos4c_sq))

        # Also compute QCMI at this b1
        g = make_vertex_sharing_chain(int(b1_crit), c_val=c)
        qcmi_at_crit, _, _, _ = g.qcmi(0.5)

        print(f"  c={c:.1f}: b1_crit={int(b1_crit):d}, QCMI_crit={qcmi_at_crit:.2f} bits")

    # Key takeaway
    print("\n--- Key Findings ---")
    print("""
    1. PER-QUBIT decoherence is INDEPENDENT of b1:
       - Endpoint qubits: D = 1 - cos²(2c)  (constant, ~0.83 at c=0.5)
       - Interior qubits: D = 1 - cos⁴(2c)  (constant, ~0.97 at c=0.5)
       - Adding more rings does NOT increase per-qubit decoherence!

    2. GLOBAL decoherence SCALES EXPONENTIALLY with b1:
       - D_global = 1 - cos²(4c)^{b1}
       - At c=0.5: cos²(4c)=0.173, D_global > 0.99 at b1 ≈ 3
       - γ_dec(global) ∝ b1 ∝ QCMI

    3. The QCMI→decoherence link is:
       γ_dec(global) = κ(c) · QCMI
       where κ(c) = -ln(cos²(4c)) / η(c)
       At c=0.5: κ ≈ 1.77

    4. DECOHERENCE IS SATURATED PER-QUBIT:
       Each qubit can decohere at most by the amount set by its local
       environment (1-2 rings). The QCMI continues to grow with b1
       because more qubits = more total information leaked to the
       environment, but individual qubit coherence floors are hit
       quickly (b1=1 for endpoints, b1=2 for interior).

    5. CLASSICALITY EMERGES FROM COLLECTIVE DECOHERENCE:
       The "classical world" claim is not about individual qubit
       decoherence rates, but about the TOTAL information the
       environment extracts from the system. With b1 ~ 10^{80},
       QCMI is astronomically large, and while each qubit's
       decoherence is bounded, the collective behavior across
       all qubits produces effective classicality.
    """)


def per_ring_decoherence_increment():
    """Compute per-ring decoherence increment."""

    print("\n" + "=" * 70)
    print("PER-RING DECOHERENCE INCREMENT ΔD")
    print("=" * 70)

    c = 0.5
    p = 0.5

    print(f"{'b1':>4s} {'D_global':>10s} {'ΔD_global':>10s} "
          f"{'D_q0':>8s} {'D_q1':>8s} {'D_q2':>8s} {'QCMI':>8s} {'ΔQCMI':>8s}")
    print("-" * 72)

    prev_D = 0.0
    prev_QCMI = 0.0

    for b1 in range(1, 9):
        g = make_vertex_sharing_chain(b1, c_val=c)
        meas = compute_decoherence_measures(g, p)

        dD_global = meas['d_global_max'] - prev_D
        dQCMI = meas['qcmi'] - prev_QCMI

        d_qs = meas['d_per_qubit']
        d_q0 = d_qs[0] if len(d_qs) > 0 else np.nan
        d_q1 = d_qs[1] if len(d_qs) > 1 else np.nan
        d_q2 = d_qs[2] if len(d_qs) > 2 else np.nan

        print(f"{b1:4d} {meas['d_global_max']:10.6f} {dD_global:10.6f} "
              f"{d_q0:8.4f} {d_q1:8.4f} {d_q2:8.4f} "
              f"{meas['qcmi']:8.4f} {dQCMI:8.4f}")

        prev_D = meas['d_global_max']
        prev_QCMI = meas['qcmi']


def eigenvalue_analysis():
    """Analyze Gram matrix eigenvalues and their relation to decoherence."""

    print("\n" + "=" * 70)
    print("GRAM MATRIX EIGENVALUE ANALYSIS")
    print("=" * 70)

    c = 0.5
    p = 0.5

    for b1 in [1, 2, 3, 4, 5]:
        g = make_vertex_sharing_chain(b1, c_val=c)
        meas = compute_decoherence_measures(g, p)

        evals = meas['gram_eigenvalues']
        n_evals = len(evals)

        # Top eigenvalues
        top_n = min(5, n_evals)

        print(f"\nb1={b1}, d_s={n_evals}:")
        print(f"  Top {top_n} eigenvalues: {evals[:top_n]}")
        print(f"  λ₁ = {evals[0]:.4f}, λ₁/d_s = {evals[0]/n_evals:.4f}")
        print(f"  Effective rank = {1.0/(1.0 - meas['d_rank_deficit']):.2f} (out of {n_evals})")
        print(f"  Participation ratio = 1/Tr(λ²) = {1.0/np.sum(evals**2):.2f}")

        # How many eigenvalues are "significant" (> 1% of max)?
        sig_thresh = 0.01 * evals[0]
        n_sig = np.sum(evals > sig_thresh)
        print(f"  Significant eigenvalues (>1% of max): {n_sig}")

    # Show that as b1 increases, the Gram matrix becomes more "mixed"
    # (more eigenvalues become significant, consistent with QCMI growth)


# =========================================================================
# MAIN
# =========================================================================

if __name__ == '__main__':
    # Step 1: Define decoherence and validate
    print("\n" + "#" * 70)
    print("# STEP 1: Validate decoherence measures on known cases")
    print("#" * 70)

    # Single ring baseline
    g1 = make_vertex_sharing_chain(1, c_val=0.5)
    meas1 = compute_decoherence_measures(g1, 0.5)
    print(f"\nb1=1, c=0.5:")
    print(f"  QCMI = {meas1['qcmi']:.4f}")
    print(f"  d_per_qubit = {[f'{d:.4f}' for d in meas1['d_per_qubit']]}")
    print(f"  d_global_max = {meas1['d_global_max']:.4f}")
    print(f"  d_avg_offdiag = {meas1['d_avg_offdiag']:.4f}")

    # Analytic check
    d_analytic = analytic_per_qubit_decoherence(1, 0.5)
    print(f"  Analytic per-qubit = {[f'{d:.4f}' for d in d_analytic]}")
    d_global_analytic = analytic_global_decoherence(1, 0.5)
    print(f"  Analytic global = {d_global_analytic:.4f}")

    # Step 2: Full parameter scan
    print("\n" + "#" * 70)
    print("# STEP 2: QCMI vs Decoherence parameter scan")
    print("#" * 70)
    results = scan_qcmi_vs_decoherence()

    # Step 3: Detailed b1 scan
    print("\n" + "#" * 70)
    print("# STEP 3: Detailed b1 scan at c=0.5")
    print("#" * 70)
    detailed_b1_scan(c_fixed=0.5)

    # Step 4: Per-ring increment
    per_ring_decoherence_increment()

    # Step 5: c scan
    print("\n" + "#" * 70)
    print("# STEP 5: c dependence at fixed b1")
    print("#" * 70)
    c_scan_at_b1(b1_fixed=5)

    # Step 6: Fit analysis
    print("\n" + "#" * 70)
    print("# STEP 6: Fit functional forms")
    print("#" * 70)
    fit_analysis(results)

    # Step 7: Analytic derivation
    derive_qcmi_decoherence_formula()

    # Step 8: Eigenvalue analysis
    print("\n" + "#" * 70)
    print("# STEP 8: Gram matrix eigenvalue structure")
    print("#" * 70)
    eigenvalue_analysis()

    # Step 9: Physical interpretation
    physical_interpretation()

    print("\n" + "=" * 70)
    print("WALL #9 ATTACK COMPLETE")
    print("=" * 70)
