"""
DGF P0 Verification: Gram Matrix Rank Collapse with b1

Tests: Does the Gram matrix rank collapse exponentially with increasing
number of causal rings b1? Does the decay rate mu depend on Cartan angle c?

Builds vertex-sharing causal ring chains, computes Gram matrix spectral
statistics, and compares measured decay to analytic predictions.
"""
import numpy as np
import sys
import os

# Add path for importing existing modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'LP44-DGF-Classicality'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'DGF-Survivors'))


# ================================================================
# 1. Gram matrix construction: vertex-sharing chain
# ================================================================

def build_gram_vertex_chain(b1, c, p=0.5):
    """
    Build Gram matrix for vertex-sharing chain of b1 rings.

    Ring r: Q_r -> E_r -> Q_{r+1} -> E'_r -> Q_r
    After summing over env qubits E_r, E'_r, each ring contributes a
    factor to the Gram matrix element.

    The Gram factor for ring r:
        p*exp(i*c*Delta_r) + (1-p)*exp(-i*c*Delta_r)
    where Delta_r = (s_Qr^a + s_{Qr+1}^a) - (s_Qr^b + s_{Qr+1}^b)

    For p=0.5: factor = cos(c * Delta_r)

    Dimension: d = 2^{b1+1} on system qubits Q_0..Q_b1.
    """
    n_sys = b1 + 1
    d_sys = 2 ** n_sys

    if d_sys > 8192:
        print(f"  [SKIP b1={b1}: d_sys={d_sys} > 8192, too large for dense]")
        return None

    G = np.ones((d_sys, d_sys), dtype=complex)

    # Precompute system basis states as +/-1 arrays
    sys_states = np.zeros((d_sys, n_sys), dtype=int)
    for idx in range(d_sys):
        for q in range(n_sys):
            sys_states[idx, q] = 1 if (idx >> q) & 1 else -1

    for r in range(b1):
        for a in range(d_sys):
            s_Qr_a = sys_states[a, r]
            s_Qr1_a = sys_states[a, r + 1]

            for b in range(a, d_sys):  # Use symmetry G[b,a] = G[a,b]*
                s_Qr_b = sys_states[b, r]
                s_Qr1_b = sys_states[b, r + 1]

                delta = (s_Qr_a + s_Qr1_a) - (s_Qr_b + s_Qr1_b)

                # Each ring has TWO env qubits (E_r, E'_r), each contributing
                # the same Gram factor after env-sum. Total: factor^2.
                factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
                G[a, b] *= factor * factor

        # Fill lower triangle via conjugate symmetry
        for a in range(d_sys):
            for b in range(a + 1, d_sys):
                G[b, a] = np.conj(G[a, b])

    return G


# ================================================================
# 2. Use CausalGraph from b1_scaling for cross-validation
# ================================================================

def build_gram_causalgraph(b1, c, p=0.5):
    """Build Gram matrix using full quantum CausalGraph (exact but slow)."""
    from b1_scaling import make_vertex_sharing_chain
    g = make_vertex_sharing_chain(b1, c)
    return g.gram_matrix(p)


# ================================================================
# 3. Spectral analysis
# ================================================================

def analyze_gram(G, b1_val=None):
    """Full spectral analysis of Gram matrix.

    Args:
        G: Gram matrix (d x d complex)
        b1_val: number of rings (used for computing mu per ring)
    """
    if G is None:
        return None

    # Eigenvalues via Hermitian solver (Gram matrix is PSD Hermitian)
    evals_raw = np.linalg.eigvalsh(G)
    evals_raw = np.maximum(evals_raw, 0.0)  # Clean numerical noise

    total = np.sum(evals_raw)
    if total < 1e-15:
        return None

    evals = evals_raw / total  # Normalize to sum=1
    evals_sorted = np.sort(evals)[::-1]

    d = G.shape[0]

    # Effective rank (participation ratio): PR = (Σ λ_i)^2 / (Σ λ_i^2) = 1/Σ p_i^2
    rank_eff = 1.0 / np.sum(evals ** 2)

    # Number of eigenvalues above machine tolerance
    n_significant = np.sum(evals > 1e-12)

    # Extract off-diagonal entries
    offdiag_abs = []
    for a in range(d):
        for b in range(a + 1, d):
            val = G[a, b]
            offdiag_abs.append(np.abs(val))

    offdiag_abs = np.array(offdiag_abs)

    mean_offdiag = np.mean(offdiag_abs)
    std_offdiag = np.std(offdiag_abs)
    median_offdiag = np.median(offdiag_abs)

    # Ln of off-diagonal magnitude — averaged over non-diagonal entries
    if b1_val is not None and b1_val > 0:
        ln_offdiag_per_ring = []
        for val_abs in offdiag_abs:
            if val_abs > 1e-15:
                ln_offdiag_per_ring.append(np.log(val_abs) / b1_val)
        mu_measured = np.mean(ln_offdiag_per_ring) if ln_offdiag_per_ring else np.nan
    else:
        mu_measured = np.nan

    return {
        'b1': b1_val,
        'd': d,
        'rank_eff': rank_eff,
        'n_significant': n_significant,
        'max_eval': evals_sorted[0],
        'eval_top5': evals_sorted[:5],
        'eval_bottom': evals_sorted[-1] if evals_sorted[-1] > 1e-15 else evals_sorted[evals_sorted > 1e-15][-1] if np.any(evals_sorted > 1e-15) else 0,
        'mean_offdiag': mean_offdiag,
        'std_offdiag': std_offdiag,
        'median_offdiag': median_offdiag,
        'mu_measured': mu_measured,
        'evals_all': evals_sorted,
    }


# ================================================================
# 4. Analytic mu formula
# ================================================================

def analytic_mu_vertex(c, p=0.5):
    """
    Analytic μ for vertex-sharing chain.

    Δ = sum_a - sum_b where sum = s1 + s2, each s_i ∈ {±1}
    sum ∈ {-2, 0, 2} with probs {1/4, 1/2, 1/4}
    Δ ∈ {-4, -2, 0, 2, 4} with probs {1/16, 4/16, 6/16, 4/16, 1/16}

    μ = Σ prob · ln|p·exp(icΔ) + (1-p)·exp(-icΔ)|

    Since each ring has 2 env qubits, the ring-level μ is:
        μ_ring = 2 · μ_env_qubit
    """
    delta_vals = np.array([-4, -2, 0, 2, 4])
    delta_probs = np.array([1, 4, 6, 4, 1]) / 16.0

    mu_env = 0.0
    for dv, prob in zip(delta_vals, delta_probs):
        factor = p * np.exp(1j * c * dv) + (1 - p) * np.exp(-1j * c * dv)
        abs_factor = np.abs(factor)
        if abs_factor < 1e-15:
            return -np.inf  # Exact zero: mu diverges
        mu_env += prob * np.log(abs_factor)

    # Each ring has 2 env qubits: μ_ring = 2 * μ_env_qubit
    return 2.0 * mu_env


def analytic_mu_edge_disjoint(c, p=0.5):
    """Analytic mu for edge-disjoint rings (4 independent qubits per ring)."""
    # Each ring has 4 independent system qubits
    # sum_a = s1 + s2 + s3 + s4, each ±1
    # sum ∈ {-4, -2, 0, 2, 4} with probs {1/16, 4/16, 6/16, 4/16, 1/16}
    # Δ = sum_a - sum_b, range -8 to 8
    sum_vals = np.array([-4, -2, 0, 2, 4])
    sum_probs = np.array([1, 4, 6, 4, 1]) / 16.0

    mu = 0.0
    for i, sa in enumerate(sum_vals):
        for j, sb in enumerate(sum_vals):
            delta = sa - sb
            prob = sum_probs[i] * sum_probs[j]
            factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
            abs_factor = np.abs(factor)
            if abs_factor < 1e-15:
                return -np.inf
            mu += prob * np.log(abs_factor)

    return mu


def analytic_mu_via_mu_analytic_module(c, p=0.5):
    """Use existing mu_analytic module for comparison."""
    from mu_analytic import mu_vertex_sharing, mu_analytic
    mu_v, sig_v = mu_vertex_sharing(c, p)
    mu_e, sig_e = mu_analytic(c, p)
    return {'mu_vertex': mu_v, 'sig_vertex': sig_v,
            'mu_edge': mu_e, 'sig_edge': sig_e}


# ================================================================
# 5. Cross-validation: compare approaches
# ================================================================

def cross_validate_gram_methods(b1_max=2):
    """Compare CausalGraph approach with product approach for small b1."""
    print("=" * 80)
    print("CROSS-VALIDATION: CausalGraph.full vs Product approach")
    print("=" * 80)

    for b1 in [1, 2]:
        for c_test in [0.5, np.pi / 4, np.pi / 2]:
            G_cg = build_gram_causalgraph(b1, c_test)
            G_prod = build_gram_vertex_chain(b1, c_test)

            if G_cg is None or G_prod is None:
                continue

            diff = np.max(np.abs(G_cg - G_prod))
            spec_cg = analyze_gram(G_cg, b1_val=b1)
            spec_prod = analyze_gram(G_prod, b1_val=b1)

            match = "MATCH" if diff < 1e-10 else f"DIFFER {diff:.2e}"
            print(f"  b1={b1} c={c_test:.4f}: {match}")
            if spec_cg and spec_prod:
                print(f"    CausalGraph: rank_eff={spec_cg['rank_eff']:.6f} "
                      f"mean_offdiag={spec_cg['mean_offdiag']:.6e}")
                print(f"    Product:     rank_eff={spec_prod['rank_eff']:.6f} "
                      f"mean_offdiag={spec_prod['mean_offdiag']:.6e}")

    return diff  # Return last diff for checking


# ================================================================
# 6. Main verification scan
# ================================================================

def run_main_scan():
    """Scan (b1, c) space and compute Gram spectral statistics."""
    print("\n" + "=" * 80)
    print("MAIN SCAN: Gram matrix rank vs b1 for Cartan angles c")
    print("=" * 80)

    c_configs = [
        (np.pi / 2, "pi/2", "Clifford"),
        (np.pi / 4, "pi/4", "CNOT"),
        (0.5, "0.5", "Standard"),
        (np.pi / 8, "pi/8", "Small"),
    ]
    p = 0.5
    max_b1 = 8

    all_results = {}

    for c, c_label, c_desc in c_configs:
        print(f"\n{'─' * 80}")
        print(f"c = {c_label} ({c_desc}, c = {c:.6f} rad)")
        print(f"{'─' * 80}")
        header = (f"{'b1':>4s}  {'d_sys':>6s}  {'rank_eff':>10s}  "
                  f"{'mean|G_ab|':>14s}  {'median|G|':>14s}  "
                  f"{'ln(r_eff-1)':>14s}  {'mu_meas':>12s}  {'N_λ>0':>8s}")
        print(header)
        print("-" * len(header))

        results_c = []
        for b1 in range(1, max_b1 + 1):
            G = build_gram_vertex_chain(b1, c, p)
            spec = analyze_gram(G, b1_val=b1)

            if spec is None:
                continue

            ln_r = np.log(max(spec['rank_eff'] - 1.0, 1e-15))

            print(f"{b1:4d}  {spec['d']:6d}  {spec['rank_eff']:10.4f}  "
                  f"{spec['mean_offdiag']:14.6e}  {spec['median_offdiag']:14.6e}  "
                  f"{ln_r:14.6f}  {spec['mu_measured']:12.6f}  "
                  f"{spec['n_significant']:8d}")

            results_c.append(spec)

        all_results[c_label] = results_c

        # Print top eigenvalues for the largest b1
        if results_c:
            spec_last = results_c[-1]
            evals = spec_last['evals_all']
            n_show = min(10, len(evals))
            top_evals_str = ", ".join(f"{evals[i]:.4e}" for i in range(n_show))
            print(f"  Top {n_show} eigenvalues (b1={spec_last['b1']}): [{top_evals_str}]")
            print(f"  Eigenvalue range: max={evals[0]:.6e} min={evals[-1]:.6e}")
            print(f"  # eigenvalues > 1e-12: {spec_last['n_significant']} / {spec_last['d']}")

    return all_results


# ================================================================
# 7. Exponential fit: compare measured vs analytic mu
# ================================================================

def run_exponential_fit(all_results):
    """Fit ln(rank_eff - 1) vs b1 and ln|G_ab| vs b1."""
    print("\n" + "=" * 80)
    print("EXPONENTIAL FIT ANALYSIS")
    print("=" * 80)
    print()

    c_configs_map = {
        "pi/2": (np.pi / 2, "pi/2", "Clifford"),
        "pi/4": (np.pi / 4, "pi/4", "CNOT"),
        "0.5": (0.5, "0.5", "Standard"),
        "pi/8": (np.pi / 8, "pi/8", "Small"),
    }
    p = 0.5

    print(f"{'c':<10s} {'mu_analytic':<14s} {'mu_meas(ln|G|)':<16s} "
          f"{'gamma(rank)':<14s} {'|mu|-|gamma|':<14s} {'ratio':<10s}")
    print("-" * 82)

    for c_label, (c_val, _, c_desc) in c_configs_map.items():
        results = all_results.get(c_label, [])
        if len(results) < 2:
            print(f"{c_label:<10s} {'N/A':<14s}")
            continue

        # Analytic mu
        mu_a = analytic_mu_vertex(c_val, p)

        # Measured mu from ln|G_ab|/b1
        mu_meas_vals = [r['mu_measured'] for r in results
                        if not np.isnan(r['mu_measured'])]
        mu_meas_avg = np.mean(mu_meas_vals) if mu_meas_vals else np.nan

        # Fit ln(rank_eff - 1) = A - gamma * b1
        b1_vals = []
        ln_r_vals = []
        for r in results:
            if r['rank_eff'] > 2.0:  # Only fit decay region
                b1_vals.append(r['b1'])
                ln_r_vals.append(np.log(r['rank_eff'] - 1.0))

        if len(b1_vals) >= 2:
            coeffs = np.polyfit(b1_vals, ln_r_vals, 1)
            gamma_rank = -coeffs[0]  # Slope, positive if rank decays
            r_sq = 1 - np.sum((ln_r_vals - np.polyval(coeffs, b1_vals))**2) / \
                   np.sum((ln_r_vals - np.mean(ln_r_vals))**2)
        else:
            gamma_rank = np.nan
            r_sq = np.nan

        # Fit ln(mean|G_ab|) = mu * b1
        b1_vals_g = []
        ln_g_vals = []
        for r in results:
            if r['mean_offdiag'] > 1e-15:
                b1_vals_g.append(r['b1'])
                ln_g_vals.append(np.log(r['mean_offdiag']))

        if len(b1_vals_g) >= 2:
            coeffs_g = np.polyfit(b1_vals_g, ln_g_vals, 1)
            gamma_offdiag = -coeffs_g[0]
        else:
            gamma_offdiag = np.nan

        if np.isinf(mu_a):
            mu_str = "-inf"
        else:
            mu_str = f"{mu_a:.6f}"

        g_str = f"{gamma_rank:.6f}" if not np.isnan(gamma_rank) else "N/A"
        mu_m_str = f"{mu_meas_avg:.6f}" if not np.isnan(mu_meas_avg) else "N/A"
        go_str = f"{gamma_offdiag:.6f}" if not np.isnan(gamma_offdiag) else "N/A"

        if not np.isnan(gamma_rank) and not np.isinf(mu_a):
            delta = abs(gamma_rank - abs(mu_a))
            ratio = gamma_rank / abs(mu_a)
            print(f"{c_label:<10s} {mu_str:<14s} {mu_m_str:<16s} "
                  f"{g_str:<14s} {delta:<14.6f} {ratio:<10.4f}")
        else:
            print(f"{c_label:<10s} {mu_str:<14s} {mu_m_str:<16s} "
                  f"{g_str:<14s} {'N/A':<14s} {'N/A':<10s}")

        # Also show off-diagonal fit
        print(f"  └─ ln|G_ab| fit slope = {go_str} (should ≈ mu_analytic)")

        if not np.isnan(r_sq):
            print(f"  └─ ln(rank_eff-1) fit R^2 = {r_sq:.6f}")

    # Additional: compare with mu_analytic module
    print(f"\n{'─' * 80}")
    print("Comparison with mu_analytic.py module (Monte Carlo, 200k samples):")
    print(f"{'─' * 80}")
    print(f"{'c (rad)':<12s} {'mu_vertex (MC)':<16s} {'mu_vertex (anal)':<16s} "
          f"{'match':<8s}")
    print("-" * 56)

    for c_val, _, c_desc in c_configs_map.values():
        mu_anal = analytic_mu_vertex(c_val, p)
        try:
            mc = analytic_mu_via_mu_analytic_module(c_val, p)
            mu_mc = mc['mu_vertex']
            match = "OK" if abs(mu_mc - mu_anal) < 1e-4 else \
                    f"DIFF {abs(mu_mc - mu_anal):.2e}"
            mu_a_str = f"{mu_anal:.6f}" if not np.isinf(mu_anal) else "-inf"
            print(f"{c_val:<12.6f} {mu_mc:<16.6f} {mu_a_str:<16s} {match:<8s}")
        except Exception as e:
            mu_a_str = f"{mu_anal:.6f}" if not np.isinf(mu_anal) else "-inf"
            print(f"{c_val:<12.6f} {'error':<16s} {mu_a_str:<16s} {str(e)[:20]:<8s}")


# ================================================================
# 8. Deep dive: eigenvalue spectrum evolution for c=0.5
# ================================================================

def run_deep_dive():
    """Detailed eigenvalue spectrum evolution for c=0.5."""
    print("\n" + "=" * 80)
    print("DEEP DIVE: Eigenvalue spectrum vs b1 at c=0.5")
    print("=" * 80)

    c = 0.5
    p = 0.5

    for b1 in [1, 2, 3, 4, 5, 6, 7, 8]:
        G = build_gram_vertex_chain(b1, c, p)
        if G is None:
            break
        spec = analyze_gram(G, b1_val=b1)
        if spec is None:
            continue

        evals = spec['evals_all']
        d = spec['d']

        # Show eigenvalues and effective rank breakdown
        cumsum = np.cumsum(evals)
        n95 = np.searchsorted(cumsum, 0.95) + 1  # eigenvalues needed for 95% of trace

        print(f"\n  b1={b1}, d={d}, rank_eff={spec['rank_eff']:.2f}, "
              f"n_significant={spec['n_significant']}")
        print(f"    top 10: {[f'{evals[i]:.4e}' for i in range(min(10, len(evals)))]}")
        print(f"    λ1 / Σλ = {evals[0]:.6f} (dominance of largest mode)")
        print(f"    λ2 / λ1 = {evals[1]/evals[0]:.6f}" if len(evals) > 1 and evals[0] > 1e-15 else "    λ2/λ1 = N/A")
        print(f"    N_95% = {n95} eigenvalues for 95% of spectral weight")
        print(f"    mean|G_ab| = {spec['mean_offdiag']:.6e}")

        # Check Gram matrix structure: are off-diagonals becoming uniform?
        d_check = min(d, 32)
        offdiag_sample = []
        for a in range(d_check):
            for b in range(a + 1, d_check):
                offdiag_sample.append(np.abs(G[a, b]))
        if offdiag_sample:
            offdiag_arr = np.array(offdiag_sample)
            print(f"    offdiag sample (first {d_check}x{d_check}): "
                  f"mean={np.mean(offdiag_arr):.4e} "
                  f"std={np.std(offdiag_arr):.4e} "
                  f"min={np.min(offdiag_arr):.4e} "
                  f"max={np.max(offdiag_arr):.4e}")


# ================================================================
# 9. Verdict synthesis
# ================================================================

def render_verdict(all_results_scan):
    """Synthesize findings into a clear verdict."""
    print("\n" + "=" * 80)
    print("VERDICT: Does the Gram rank collapse exponentially with b1?")
    print("=" * 80)

    verdict_lines = []

    # Summary table
    verdict_lines.append("")
    verdict_lines.append("SUMMARY TABLE")
    verdict_lines.append("─" * 60)
    verdict_lines.append(f"{'c':<10s} {'μ_anal':<12s} {'Prediction':<18s} "
                         f"{'Actual trend':<20s}")
    verdict_lines.append("-" * 60)

    c_configs = [
        (np.pi / 2, "pi/2", "Clifford"),
        (np.pi / 4, "pi/4", "CNOT"),
        (0.5, "0.5", "Standard"),
        (np.pi / 8, "pi/8", "Small"),
    ]
    p = 0.5

    for c_val, c_label, c_desc in c_configs:
        mu_a = analytic_mu_vertex(c_val, p)
        mu_str = f"{mu_a:.6f}" if not np.isinf(mu_a) else "-inf"

        results = all_results_scan.get(c_label, [])
        if len(results) >= 2:
            r_start = results[0]['rank_eff']
            r_end = results[-1]['rank_eff']
            d_start = results[0]['d']
            d_end = results[-1]['d']
            trend = f"{r_start:.2f} -> {r_end:.2f} (d: {d_start}->{d_end})"

            if r_end < r_start:
                qualitative = "COLLAPSING (classical)"
            elif r_end > r_start and r_end < d_end * 0.5:
                qualitative = f"GROWING slower than d"
            else:
                qualitative = f"GROWING ~d (quantum)"
        else:
            trend = "N/A"
            qualitative = "N/A"

        prediction = f"μ→0: rank stable" if abs(mu_a) < 1e-10 else \
                     f"μ={mu_str}: rank→1" if mu_a < 0 else \
                     f"μ>0: rank→d"

        verdict_lines.append(f"{c_label:<10s} {mu_str:<12s} {prediction:<18s} "
                             f"{qualitative:<20s} ({trend})")

    # Core findings
    verdict_lines.append("")
    verdict_lines.append("CORE FINDINGS")
    verdict_lines.append("─" * 60)

    # Compute key results for c=0.5
    results_05 = all_results_scan.get("0.5", [])
    if len(results_05) >= 2:
        for b1_test in [1, 4, 8]:
            for r in results_05:
                if r['b1'] == b1_test:
                    verdict_lines.append(
                        f"  c=0.5, b1={b1_test}: rank_eff={r['rank_eff']:.3f}, "
                        f"mean|G_ab|={r['mean_offdiag']:.4e}, "
                        f"d={r['d']}")
                    break

    # Clifford behavior
    results_cliff = all_results_scan.get("pi/2", [])
    if results_cliff:
        for b1_test in [1, 4, 8]:
            for r in results_cliff:
                if r['b1'] == b1_test:
                    verdict_lines.append(
                        f"  c=pi/2, b1={b1_test}: rank_eff={r['rank_eff']:.3f}, "
                        f"mean|G_ab|={r['mean_offdiag']:.4e}, "
                        f"d={r['d']}")
                    break

    # Compute the actual trend
    verdict_lines.append("")
    verdict_lines.append("NUMERICAL VERIFICATION OF PREDICTION")
    verdict_lines.append("─" * 60)
    verdict_lines.append("Prediction: rank_eff → 1 as b1 → ∞ (exponential decay)")
    verdict_lines.append("Prediction: |G_ab| = exp(μ·b1) with μ<0")

    # Check if the prediction holds
    prediction_holds = True
    for c_val, c_label, _ in c_configs:
        if abs(c_val - np.pi/2) < 1e-10:
            continue  # Clifford is special
        results = all_results_scan.get(c_label, [])
        if len(results) < 2:
            continue
        r_first = results[0]['rank_eff']
        r_last = results[-1]['rank_eff']
        if r_last < r_first:
            verdict_lines.append(f"  c={c_label}: rank DECREASES -> prediction POSSIBLY CORRECT")
        else:
            prediction_holds = False
            mu_a = analytic_mu_vertex(c_val, p)
            verdict_lines.append(
                f"  c={c_label}: rank INCREASES ({r_first:.2f}->{r_last:.2f}) "
                f"while d grows {results[0]['d']}->{results[-1]['d']}")
            verdict_lines.append(
                f"    μ_anal={mu_a:.6f}, |G_ab|={results[0]['mean_offdiag']:.4e}"
                f"->{results[-1]['mean_offdiag']:.4e}")

    for line in verdict_lines:
        print(line)

    return verdict_lines


# ================================================================
# MAIN
# ================================================================

if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True, linewidth=120)

    print("DGF P0 VERIFICATION: Gram Matrix Rank Collapse")
    print(f"Date: 2026-06-11")
    print(f"Method: Dense Gram matrix for vertex-sharing causal ring chains")
    print(f"Matrix dimension: d = 2^(b1+1), max b1=8 → max d=512")

    # Step 1: Cross-validate the two Gram construction methods
    print("\n" + "=" * 80)
    print("STEP 1: Cross-validate CausalGraph vs Product approach")
    print("=" * 80)
    cross_validate_gram_methods(b1_max=2)

    # Step 2: Main scan
    print("\n" + "=" * 80)
    print("STEP 2: Full (b1, c) scan")
    print("=" * 80)
    all_results = run_main_scan()

    # Step 3: Exponential fit analysis
    print("\n" + "=" * 80)
    print("STEP 3: Fit analysis")
    print("=" * 80)
    run_exponential_fit(all_results)

    # Step 4: Deep dive at c=0.5
    print("\n" + "=" * 80)
    print("STEP 4: Eigenvalue spectrum deep dive")
    print("=" * 80)
    run_deep_dive()

    # Step 5: Verdict
    print("\n" + "=" * 80)
    print("STEP 5: Final verdict")
    print("=" * 80)
    verdict = render_verdict(all_results)

    print("\nDone.")
