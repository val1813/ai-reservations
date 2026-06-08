"""
AHA1 Round 3: Firewall Universality Test
=========================================
Tests whether β(α) is universal — independent of microscopic details (Γ, f_L, f_R).

The "firewall" designed by Dr. B: if β deviates by <5% across parameter variations,
the exponent is declared universal (✅). 5-10% deviation = weak dependence (⚠️).
>10% deviation = β depends on microscopic details → AHA1 is killed (❌).

Parameters:
  Fixed: α=1.5, γ_φ=0.5, J0=0.3
  Γ_L = Γ_R = Γ ∈ [0.5, 1.0, 1.5, 2.0]
  Δf = f_L − f_R ∈ [0.1, 0.3, 0.5]  →  f_L = 0.5 + Δf/2, f_R = 0.5 − Δf/2
  L ∈ [4, 8, 16, 32, 64]

Method: site-basis Lindblad approach (same as COH Phase 2).

Criterion:
  Δβ < 5%  → Universality confirmed ✅
  5% < Δβ < 10% → Weak dependence ⚠️
  Δβ > 10% → Non-universal → AHA1 killed ❌

Author: Claude (AHA1 Round 3)
Date: 2026-06-03
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov as solve_lyap
import scipy.stats
import time
import json
import os
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# SECTION 1: System Construction (identical to Phase 2)
# ============================================================

def construct_h(L, alpha, J0=0.3):
    """Single-particle Hamiltonian with power-law hopping J(r) = J0 / r^alpha."""
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def solve_ness_correlation(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Solve for the NESS correlation matrix C_{ij} = Tr[c_i† c_j ρ_ss].

    Steady-state equation:
    i[h, C] + 1/2 {Gamma_diag, C} + gamma_phi (C - diag(C)) = diag(W_in)

    Solved as a linear system A · vec(C) = b.
    """
    h = construct_h(L, alpha, J0)

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            # Diagonal damping: 1/2 (Gamma_i + Gamma_j) + gamma_phi * (1 - delta_ij)
            A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                A[row, row] += gamma_phi

            # Hamiltonian commutator: i[h, C]
            for k in range(L):
                if abs(h[i, k]) > 1e-15:
                    col = k * L + j
                    A[row, col] += 1j * h[i, k]

                if abs(h[k, j]) > 1e-15:
                    col = i * L + k
                    A[row, col] -= 1j * h[k, j]

            # Source term (only on diagonal)
            if i == j:
                b_vec[row] = W_in[i]

    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)

    return C


# ============================================================
# SECTION 2: Universality Scan
# ============================================================

def run_universality_scan():
    """Run the full universality scan over Γ, Δf, L."""
    J0 = 0.3
    alpha = 1.5
    gamma_phi = 0.5

    Gamma_values = [0.5, 1.0, 1.5, 2.0]
    Delta_f_values = [0.1, 0.3, 0.5]
    L_values = [4, 8, 16, 32, 64]

    print("=" * 80)
    print("AHA1 ROUND 3: FIREWALL UNIVERSALITY TEST")
    print("=" * 80)
    print(f"Fixed: alpha={alpha}, gamma_phi={gamma_phi}, J0={J0}")
    print(f"Γ ∈ {Gamma_values}")
    print(f"Δf = f_L - f_R ∈ {Delta_f_values}")
    print(f"L ∈ {L_values}")
    print(f"Total: {len(Gamma_values)} x {len(Delta_f_values)} x {len(L_values)} = "
          f"{len(Gamma_values) * len(Delta_f_values) * len(L_values)} data points")
    print()

    results = []
    n_total = len(Gamma_values) * len(Delta_f_values) * len(L_values)
    n_done = 0

    for Gamma in Gamma_values:
        print(f"\n{'='*60}")
        print(f"Γ = {Gamma}")
        print(f"{'='*60}")

        for delta_f in Delta_f_values:
            f_L = 0.5 + delta_f / 2.0
            f_R = 0.5 - delta_f / 2.0

            print(f"  Δf = {delta_f} (f_L={f_L:.2f}, f_R={f_R:.2f}): ", end='', flush=True)

            for L in L_values:
                t_start = time.time()

                C = solve_ness_correlation(L, alpha, J0, Gamma, Gamma,
                                           f_L, f_R, gamma_phi)

                mid_i = L // 2 - 1
                mid_j = L // 2
                C_mid = C[mid_i, mid_j]
                abs_C_mid = abs(C_mid)

                # Verify pure imaginary
                re_C_mid = C_mid.real
                im_C_mid = C_mid.imag

                t_elapsed = time.time() - t_start

                result = {
                    'alpha': alpha,
                    'gamma_phi': gamma_phi,
                    'Gamma': Gamma,
                    'delta_f': delta_f,
                    'f_L': f_L,
                    'f_R': f_R,
                    'L': L,
                    'abs_C_mid': float(abs_C_mid),
                    're_C_mid': float(re_C_mid),
                    'im_C_mid': float(im_C_mid),
                    'time_s': t_elapsed,
                }
                results.append(result)

                n_done += 1
                print(f'L={L}:|C|={abs_C_mid:.6e} ', end='', flush=True)

            print(f' [{n_done}/{n_total}]', flush=True)

    return results


# ============================================================
# SECTION 3: β Extraction and Universality Analysis
# ============================================================

def extract_beta(results):
    """
    For each (Γ, Δf) combination, fit |C_mid| ~ A * L^{-β}
    via log-log linear regression across L=4,8,16,32,64.
    """
    print("\n" + "=" * 80)
    print("β EXTRACTION: |C_mid|(L) ~ A * L^{-β} for each (Γ, Δf)")
    print("=" * 80)

    # Organize data
    data_by_params = {}
    for r in results:
        key = (r['Gamma'], r['delta_f'])
        if key not in data_by_params:
            data_by_params[key] = {'L': [], 'abs_C': []}
        data_by_params[key]['L'].append(r['L'])
        data_by_params[key]['abs_C'].append(r['abs_C_mid'])

    print(f"\n{'Γ':>8} {'Δf':>8} {'A':>12} {'β':>10} {'R²':>10} {'|C|(L=64)':>14} {'β-β_ref':>12}")
    print("-" * 80)

    # Reference beta: Γ=1.0, Δf=0.3 (f_L=0.65, f_R=0.35) — same as Phase 2
    ref_key = (1.0, 0.3)

    beta_values = {}
    ref_beta = None

    for (Gamma, delta_f), d in sorted(data_by_params.items()):
        L_arr = np.array(d['L'])
        C_arr = np.array(d['abs_C'])

        mask = C_arr > 1e-15
        if np.sum(mask) < 3:
            beta_values[(Gamma, delta_f)] = {
                'beta': None, 'A': None, 'R2': None, 'error': 'Insufficient data'
            }
            continue

        log_L = np.log(L_arr[mask])
        log_C = np.log(C_arr[mask])

        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(log_L, log_C)
        beta = -slope
        A_fit = np.exp(intercept)
        r_sq = r_value ** 2

        beta_values[(Gamma, delta_f)] = {
            'beta': beta,
            'A': A_fit,
            'R2': r_sq,
            'std_err': std_err,
        }

        if (Gamma, delta_f) == ref_key:
            ref_beta = beta
            delta_beta_str = " (REF)"
        elif ref_beta is not None:
            delta_pct = 100 * abs(beta - ref_beta) / ref_beta
            delta_beta_str = f"{delta_pct:>+10.2f}%"
        else:
            delta_beta_str = "N/A"

        print(f"{Gamma:>8.1f} {delta_f:>8.1f} {A_fit:>12.6f} {beta:>10.4f} "
              f"{r_sq:>10.4f} {C_arr[-1]:>14.6e} {delta_beta_str}")

    return beta_values, ref_beta


def universality_verdict(beta_values, ref_beta):
    """
    Apply the universality criteria:
    Δβ < 5%   → ✅ Universality confirmed
    5-10%     → ⚠️ Weak dependence
    >10%      → ❌ Non-universal → AHA1 killed
    """
    print("\n" + "=" * 80)
    print("UNIVERSALITY VERDICT")
    print("=" * 80)

    if ref_beta is None:
        print("ERROR: Could not determine reference β")
        return None

    print(f"\nReference β (Γ=1.0, Δf=0.3): {ref_beta:.4f}")
    print(f"\nCriterion: Δβ = |β - β_ref| / β_ref")
    print(f"  < 5%  : ✅ Universality confirmed")
    print(f"  5-10% : ⚠️  Weak dependence on microscopic details")
    print(f"  > 10% : ❌ Non-universal, depends on microscopic details → AHA1 killed")

    max_delta_pct = 0.0
    verdicts = []

    for (Gamma, delta_f), info in sorted(beta_values.items()):
        if info['beta'] is None:
            continue
        delta_pct = 100 * abs(info['beta'] - ref_beta) / ref_beta
        max_delta_pct = max(max_delta_pct, delta_pct)

        if delta_pct < 5.0:
            symbol = "✅"
        elif delta_pct < 10.0:
            symbol = "⚠️"
        else:
            symbol = "❌"

        verdicts.append({
            'Gamma': Gamma,
            'delta_f': delta_f,
            'beta': info['beta'],
            'delta_pct': delta_pct,
            'verdict': symbol,
        })

    # Print summary table
    print(f"\n{'Γ':>8} {'Δf':>8} {'β':>10} {'Δβ%':>10} {'Verdict'}")
    print("-" * 50)
    for v in sorted(verdicts, key=lambda x: (x['Gamma'], x['delta_f'])):
        print(f"{v['Gamma']:>8.1f} {v['delta_f']:>8.1f} {v['beta']:>10.4f} "
              f"{v['delta_pct']:>10.2f}% {v['verdict']}")

    # Overall verdict
    print("\n" + "-" * 50)
    print(f"Maximum Δβ: {max_delta_pct:.2f}%")

    if max_delta_pct < 5.0:
        overall = "✅ UNIVERSALITY CONFIRMED"
        detail = "β(α) is robust against variations in Γ and Δf. The exponent is a universal feature."
    elif max_delta_pct < 10.0:
        overall = "⚠️ WEAK DEPENDENCE"
        detail = "β(α) shows mild sensitivity to microscopic parameters. Universality holds approximately."
    else:
        overall = "❌ AHA1 KILLED — NON-UNIVERSAL"
        detail = "β(α) depends strongly on microscopic details (Γ, Δf). The claim of universality fails."

    print(f"\n{'='*60}")
    print(f"  OVERALL VERDICT: {overall}")
    print(f"{'='*60}")
    print(f"  {detail}")
    print()

    return {
        'max_delta_pct': max_delta_pct,
        'verdict': overall,
        'detail': detail,
        'verdicts': verdicts,
        'ref_beta': ref_beta,
    }


# ============================================================
# SECTION 4: Pure Imaginarity Check
# ============================================================

def check_purity(results):
    """Verify C_mid remains pure imaginary across all parameter combinations."""
    print("=" * 80)
    print("PURE IMAGINARITY CHECK (across all universality scan points)")
    print("=" * 80)

    max_re = max(abs(r['re_C_mid']) for r in results)
    max_im = max(abs(r['im_C_mid']) for r in results)
    ratio = max_re / max_im if max_im > 1e-20 else 0

    print(f"  max |Re(C_mid)| = {max_re:.2e}")
    print(f"  max |Im(C_mid)| = {max_im:.2e}")
    print(f"  ratio Re/Im    = {ratio:.2e}")
    print(f"  => {'PASS' if max_re < 1e-12 else 'FAIL'}: off-diagonals remain pure imaginary")

    return max_re, max_im, ratio


# ============================================================
# SECTION 5: Detailed β Table
# ============================================================

def print_beta_table(beta_values):
    """Print a 2D table of β(Γ, Δf)."""
    print("\n" + "=" * 80)
    print("β(Γ, Δf) TABLE")
    print("=" * 80)

    gamma_vals = sorted(set(k[0] for k in beta_values.keys()))
    df_vals = sorted(set(k[1] for k in beta_values.keys()))

    # Header
    header = f"{'Γ\\Δf':>8}"
    for df in df_vals:
        header += f" {f'Δf={df:.1f}':>12}"
    print(header)
    print("-" * (8 + 12 * len(df_vals)))

    for Gamma in gamma_vals:
        line = f"{Gamma:>8.1f}"
        for df in df_vals:
            key = (Gamma, df)
            if key in beta_values and beta_values[key].get('beta') is not None:
                line += f" {beta_values[key]['beta']:>12.4f}"
            else:
                line += f" {'N/A':>12}"
        print(line)


# ============================================================
# SECTION 6: Main
# ============================================================

if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # Run universality scan
    print("PHASE A: Running universality scan...")
    results = run_universality_scan()

    # Check pure imaginarity
    print("\nPHASE B: Pure imaginarity check...")
    max_re, max_im, purity_ratio = check_purity(results)

    # Extract β values
    print("\nPHASE C: β extraction...")
    beta_values, ref_beta = extract_beta(results)

    # Print β table
    print_beta_table(beta_values)

    # Universality verdict
    print("\nPHASE D: Universality verdict...")
    verdict = universality_verdict(beta_values, ref_beta)

    # Save results
    json_path = os.path.join(output_dir, 'firewall_AHA1_results.json')

    output = {
        'parameters': {
            'alpha': 1.5,
            'gamma_phi': 0.5,
            'J0': 0.3,
            'Gamma_values': [0.5, 1.0, 1.5, 2.0],
            'Delta_f_values': [0.1, 0.3, 0.5],
            'L_values': [4, 8, 16, 32, 64],
        },
        'raw_results': results,
        'purity_check': {
            'max_Re': float(max_re),
            'max_Im': float(max_im),
            'ratio': float(purity_ratio),
        },
        'beta_values': {},
        'verdict': verdict,
    }

    # Convert beta_values for JSON
    for key, val in beta_values.items():
        Gamma, delta_f = key
        output['beta_values'][f"Gamma_{Gamma}_deltaf_{delta_f}"] = {
            'Gamma': float(Gamma),
            'delta_f': float(delta_f),
            'beta': float(val['beta']) if val.get('beta') is not None else None,
            'A': float(val['A']) if val.get('A') is not None else None,
            'R2': float(val['R2']) if val.get('R2') is not None else None,
            'std_err': float(val['std_err']) if val.get('std_err') is not None else None,
        }

    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to: {json_path}")
    print(f"Total data points: {len(results)}")

    print("\n" + "=" * 80)
    print("AHA1 ROUND 3: FIREWALL UNIVERSALITY TEST COMPLETE")
    print("=" * 80)
