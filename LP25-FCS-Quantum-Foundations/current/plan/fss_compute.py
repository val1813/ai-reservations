"""
Finite-Size Scaling Computation for Power-Law Hopping NESS
===========================================================
Computes |C_mid(L, alpha, gamma_phi)| for L=32,64,128,256.
Performs proper FSS analysis with correction-to-scaling.

Strategy:
  - Fit beta from L>=32 (drop L<=16 to reduce finite-size bias)
  - Fit correction-to-scaling: |C_mid| = A * L^(-beta) * (1 + B/L^omega)
  - Compare beta_raw (simple powerlaw) vs beta_corrected
  - If beta_corrected converges across L-subsets → asymptotic exponent exists

Usage:
  python3 fss_compute.py [--Lmax 128] [--gamma 0.5] [--output results.json]

Author: Claude (referee response computation)
Date: 2026-06-04
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import gmres
from scipy.optimize import curve_fit
import scipy.stats
import time
import json
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# SECTION 1: Physical System
# ============================================================

def make_system(L, alpha, gamma_phi, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                f_L=0.65, f_R=0.35, hop_tol=1e-10):
    """
    Build sparse linear system for NESS correlation matrix.
    
    Steady-state equation:
        i[h, C] + 1/2 {Gamma_diag, C} + gamma_phi (C - diag(C)) = diag(W_in)
    
    Returns (A_sparse_csr, b, h_matrix).
    """
    # Hamiltonian: power-law hopping J(r) = J0 / r^alpha
    # Keep only hops above hop_tol for sparsity
    h = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, L):
            J = J0 / (j - i) ** alpha
            if J > hop_tol:
                h[i, j] = h[j, i] = J

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L - 1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L - 1] = Gamma_R * f_R

    L2 = L * L
    rows, cols, data_vals = [], [], []
    b = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            # Damping diagonal
            damp = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                damp += gamma_phi
            rows.append(row); cols.append(row); data_vals.append(damp)

            # Commutator i[h, C]: i * h_{ik} C_{kj} - i * C_{ik} h_{kj}
            for k in range(L):
                if abs(h[i, k]) > hop_tol:
                    rows.append(row); cols.append(k * L + j)
                    data_vals.append(1j * h[i, k])
                if abs(h[k, j]) > hop_tol:
                    rows.append(row); cols.append(i * L + k)
                    data_vals.append(-1j * h[k, j])

            # Source
            if i == j:
                b[row] = W_in[i]

    A = sparse.coo_matrix(
        (data_vals, (rows, cols)), shape=(L2, L2)
    ).tocsr()
    return A, b, h


def solve_ness(L, alpha, gamma_phi, **kwargs):
    """Solve and return C_mid = |C[L//2-1, L//2]|."""
    A, b, h = make_system(L, alpha, gamma_phi, **kwargs)
    
    # Diagonal preconditioner
    diag = A.diagonal()
    diag[diag == 0] = 1.0
    M = sparse.diags(1.0 / np.abs(diag))
    
    x, info = gmres(A, b, M=M, rtol=1e-10, maxiter=2000,
                    restart=min(200, L * L))
    if info != 0:
        print(f"  WARNING: GMRES did not converge (info={info}), L={L}, alpha={alpha}")
    
    C = x.reshape(L, L)
    C = 0.5 * (C + C.conj().T)  # enforce Hermiticity
    
    mid_i = L // 2 - 1
    mid_j = L // 2
    return abs(C[mid_i, mid_j]), np.imag(C[mid_i, mid_j]), np.real(C[mid_i, mid_j])


# ============================================================
# SECTION 2: Fitting
# ============================================================

def fit_powerlaw(L_arr, C_arr, min_L=None):
    """Simple power-law fit: C = A * L^(-beta)."""
    if min_L is not None:
        mask = np.array(L_arr) >= min_L
        L_arr = np.array(L_arr)[mask]
        C_arr = np.array(C_arr)[mask]
    
    if len(L_arr) < 3:
        return None
    
    log_L = np.log(L_arr)
    log_C = np.log(np.array(C_arr))
    slope, intercept, r, p, se = scipy.stats.linregress(log_L, log_C)
    beta = -slope
    A = np.exp(intercept)
    
    residuals = log_C - (intercept + slope * log_L)
    n = len(L_arr)
    rmse = np.sqrt(np.mean(residuals**2))
    
    return {
        'beta': beta,
        'A': A,
        'R2': r**2,
        'std_err': se,
        'p_value': p,
        'rmse': rmse,
        'n_points': n,
        'L_range': [int(L_arr[0]), int(L_arr[-1])]
    }


def fit_correction_to_scaling(L_arr, C_arr, omega_fixed=None):
    """
    Fit with correction to scaling:
      C = A * L^(-beta) * (1 + B * L^(-omega))
    
    If omega_fixed is None, fit omega as free parameter.
    """
    L_arr = np.array(L_arr, dtype=float)
    C_arr = np.array(C_arr, dtype=float)
    
    if len(L_arr) < 4:
        return None
    
    def model_free(L, A, beta, B, omega):
        return A * L**(-beta) * (1 + B * L**(-omega))
    
    def model_fixed(L, A, beta, B):
        return A * L**(-beta) * (1 + B * L**(-omega_fixed))
    
    try:
        if omega_fixed is None:
            # Initial guess from simple powerlaw
            simple = fit_powerlaw(L_arr.tolist(), C_arr.tolist())
            if simple is None:
                return None
            p0 = [simple['A'], simple['beta'], 0.1, 1.0]
            popt, pcov = curve_fit(model_free, L_arr, C_arr, p0=p0,
                                   maxfev=10000, bounds=([0, 0, -10, 0.1], [10, 5, 10, 4]))
            A, beta, B, omega = popt
            perr = np.sqrt(np.diag(pcov))
        else:
            simple = fit_powerlaw(L_arr.tolist(), C_arr.tolist())
            p0 = [simple['A'], simple['beta'], 0.1]
            popt, pcov = curve_fit(model_fixed, L_arr, C_arr, p0=p0,
                                   maxfev=10000, bounds=([0, 0, -10], [10, 5, 10]))
            A, beta, B = popt
            omega = omega_fixed
            perr = np.sqrt(np.diag(pcov))
        
        C_pred = model_free(L_arr, A, beta, B, omega) if omega_fixed is None else model_fixed(L_arr, A, beta, B)
        ss_res = np.sum((C_arr - C_pred)**2)
        ss_tot = np.sum((C_arr - np.mean(C_arr))**2)
        R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        
        result = {
            'beta': beta,
            'beta_err': perr[1] if omega_fixed is None else perr[1],
            'A': A,
            'B': B,
            'omega': omega,
            'R2': R2,
            'L_range': [int(L_arr[0]), int(L_arr[-1])]
        }
        if omega_fixed is None:
            result['omega_err'] = perr[3]
        return result
    except Exception as e:
        return {'error': str(e)}


def compute_beta_stability(L_arr, C_arr):
    """
    Check if beta stabilizes as we include larger L.
    Returns beta from successive L-subsets.
    """
    L_arr = list(L_arr)
    C_arr = list(C_arr)
    results = {}
    
    # Drop L=4 always (too small)
    pairs = [(L, C) for L, C in zip(L_arr, C_arr) if L >= 8]
    if len(pairs) < 2:
        return results
    
    L_filt, C_filt = zip(*pairs)
    
    # All points >= 8
    r = fit_powerlaw(list(L_filt), list(C_filt))
    if r: results['all_L>=8'] = r
    
    # Drop L=8
    if len(L_filt) >= 3:
        r = fit_powerlaw(list(L_filt[1:]), list(C_filt[1:]))
        if r: results[f'all_L>={L_filt[1]}'] = r
    
    # Drop two smallest
    if len(L_filt) >= 3:
        r = fit_powerlaw(list(L_filt[2:]), list(C_filt[2:]))
        if r: results[f'all_L>={L_filt[2]}'] = r
    
    # Only two largest (sequential ratio estimate)
    if len(L_filt) >= 2:
        # beta from consecutive pair: log(C1/C2) / log(L2/L1)
        for i in range(len(L_filt) - 1):
            L1, L2 = L_filt[i], L_filt[i+1]
            C1, C2 = C_filt[i], C_filt[i+1]
            if C1 > 0 and C2 > 0:
                beta_local = -np.log(C2 / C1) / np.log(L2 / L1)
                results[f'local_{L1}_{L2}'] = {'beta': beta_local, 'L_range': [L1, L2]}
    
    return results


# ============================================================
# SECTION 3: Main Scan
# ============================================================

def run_scan(L_values, alpha_values, gamma_phi_values, output_file):
    """Main computation loop."""
    
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35
    
    n_total = len(L_values) * len(alpha_values) * len(gamma_phi_values)
    print(f"Total points to compute: {n_total}")
    print(f"L values: {L_values}")
    print(f"alpha values: {alpha_values}")
    print(f"gamma_phi values: {gamma_phi_values}")
    print()
    
    raw_results = []
    n_done = 0
    
    t_start = time.time()
    
    for alpha in alpha_values:
        for gamma_phi in gamma_phi_values:
            print(f"alpha={alpha:.1f}, gamma_phi={gamma_phi}:")
            L_data = []
            C_data = []
            
            for L in sorted(L_values):
                t0 = time.time()
                C_mid, C_im, C_re = solve_ness(L, alpha, gamma_phi,
                                                J0=J0, Gamma_L=Gamma_L, Gamma_R=Gamma_R,
                                                f_L=f_L, f_R=f_R)
                dt = time.time() - t0
                
                row = {
                    'L': L, 'alpha': alpha, 'gamma_phi': gamma_phi,
                    'abs_C_mid': C_mid, 'im_C_mid': C_im, 're_C_mid': C_re,
                    'time_s': dt
                }
                raw_results.append(row)
                L_data.append(L)
                C_data.append(C_mid)
                
                n_done += 1
                elapsed = time.time() - t_start
                rate = n_done / elapsed if elapsed > 0 else 0
                eta = (n_total - n_done) / rate if rate > 0 else 0
                
                print(f"  L={L:4d}: |C_mid|={C_mid:.6e}  [{dt:.1f}s]  "
                      f"[{n_done}/{n_total}, ETA {eta/60:.0f}min]")
                sys.stdout.flush()
                
                # Save incrementally
                with open(output_file.replace('.json', '_raw.json'), 'w') as f:
                    json.dump(raw_results, f, indent=2)
            
            print()
    
    # ============================================================
    # SECTION 4: FSS Analysis
    # ============================================================
    print("\n" + "="*70)
    print("FINITE-SIZE SCALING ANALYSIS")
    print("="*70)
    
    fss_results = {}
    
    for alpha in alpha_values:
        for gamma_phi in gamma_phi_values:
            key = f"{alpha}_{gamma_phi}"
            subset = [(r['L'], r['abs_C_mid']) for r in raw_results
                      if r['alpha'] == alpha and r['gamma_phi'] == gamma_phi]
            if not subset:
                continue
            subset.sort(key=lambda x: x[0])
            L_arr, C_arr = zip(*subset)
            
            result = {
                'alpha': alpha, 'gamma_phi': gamma_phi,
                'L_values': list(L_arr),
                'C_values': list(C_arr),
            }
            
            # Simple powerlaw fits at different L-cutoffs
            result['fit_L>=4']  = fit_powerlaw(list(L_arr), list(C_arr), min_L=4)
            result['fit_L>=8']  = fit_powerlaw(list(L_arr), list(C_arr), min_L=8)
            result['fit_L>=16'] = fit_powerlaw(list(L_arr), list(C_arr), min_L=16)
            result['fit_L>=32'] = fit_powerlaw(list(L_arr), list(C_arr), min_L=32)
            result['fit_L>=64'] = fit_powerlaw(list(L_arr), list(C_arr), min_L=64)
            
            # Correction-to-scaling (omega=1 is standard leading correction)
            result['fit_correction_omega1'] = fit_correction_to_scaling(
                list(L_arr), list(C_arr), omega_fixed=1.0)
            result['fit_correction_free'] = fit_correction_to_scaling(
                list(L_arr), list(C_arr), omega_fixed=None)
            
            # Local (consecutive-L) beta estimates
            result['stability'] = compute_beta_stability(list(L_arr), list(C_arr))
            
            fss_results[key] = result
            
            # Print summary
            print(f"\nalpha={alpha:.1f}, gamma_phi={gamma_phi}:")
            for fit_key in ['fit_L>=8', 'fit_L>=16', 'fit_L>=32', 'fit_L>=64']:
                r = result.get(fit_key)
                if r and 'beta' in r:
                    print(f"  {fit_key}: beta={r['beta']:.4f} ± {r['std_err']:.4f}, "
                          f"R2={r['R2']:.4f}, n={r['n_points']}")
            
            r = result.get('fit_correction_omega1')
            if r and 'beta' in r:
                print(f"  correction(omega=1): beta={r['beta']:.4f} ± {r.get('beta_err',0):.4f}")
            
            # Local betas
            for lk, lv in result['stability'].items():
                if lk.startswith('local_'):
                    print(f"  {lk}: beta={lv['beta']:.4f}")
    
    # ============================================================
    # SECTION 5: Save full results
    # ============================================================
    output = {
        'parameters': {
            'L_values': list(L_values),
            'alpha_values': list(alpha_values),
            'gamma_phi_values': list(gamma_phi_values),
            'J0': J0, 'Gamma_L': Gamma_L, 'Gamma_R': Gamma_R,
            'f_L': f_L, 'f_R': f_R
        },
        'raw': raw_results,
        'fss': fss_results
    }
    
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n\nResults saved to {output_file}")
    print(f"Total time: {(time.time()-t_start)/60:.1f} min")
    
    return output


# ============================================================
# SECTION 6: Summary Report
# ============================================================

def print_summary(output):
    """Print key FSS table for referee response."""
    fss = output['fss']
    alpha_vals = sorted(set(v['alpha'] for v in fss.values()))
    gamma_vals = sorted(set(v['gamma_phi'] for v in fss.values()))
    
    print("\n" + "="*80)
    print("SUMMARY: beta values by L-cutoff (gamma_phi=0.5)")
    print("="*80)
    print(f"{'alpha':>6} | {'L>=8':>8} | {'L>=16':>8} | {'L>=32':>8} | {'L>=64':>8} | {'corr(ω=1)':>10}")
    print("-"*70)
    
    for alpha in alpha_vals:
        key = f"{alpha}_0.5"
        if key not in fss:
            continue
        r = fss[key]
        
        def get_beta(fk):
            fr = r.get(fk)
            if fr and 'beta' in fr: return f"{fr['beta']:.4f}"
            return "N/A"
        
        b8  = get_beta('fit_L>=8')
        b16 = get_beta('fit_L>=16')
        b32 = get_beta('fit_L>=32')
        b64 = get_beta('fit_L>=64')
        bc  = get_beta('fit_correction_omega1')
        
        print(f"{alpha:>6.1f} | {b8:>8} | {b16:>8} | {b32:>8} | {b64:>8} | {bc:>10}")
    
    print()
    print("Local beta (consecutive-L ratio) for gamma_phi=0.5:")
    for alpha in alpha_vals:
        key = f"{alpha}_0.5"
        if key not in fss: continue
        stab = fss[key].get('stability', {})
        locals_ = [(k, v['beta']) for k, v in stab.items() if k.startswith('local_')]
        locals_.sort(key=lambda x: int(x[0].split('_')[1]))
        parts = ', '.join(f"L{a}-{b}: {beta:.3f}" for (k, beta) in locals_
                         for a, b in [k.replace('local_','').split('_')])
        print(f"  alpha={alpha:.1f}: {parts}")


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--Lmax', type=int, default=128,
                        help='Maximum L to compute (32/64/128/256)')
    parser.add_argument('--gamma', type=float, default=None,
                        help='Single gamma_phi value (default: all 5)')
    parser.add_argument('--alpha', type=float, default=None,
                        help='Single alpha value (default: all 5)')
    parser.add_argument('--output', type=str, default='fss_results.json')
    args = parser.parse_args()
    
    # L values: always include 32,64 + up to Lmax
    L_base = [4, 8, 16, 32, 64]
    if args.Lmax >= 128:
        L_base.append(128)
    if args.Lmax >= 256:
        L_base.append(256)
    L_values = [L for L in L_base if L <= args.Lmax]
    
    alpha_values = [1.1, 1.3, 1.5, 1.7, 1.9]
    if args.alpha is not None:
        alpha_values = [args.alpha]
    
    gamma_phi_values = [0.01, 0.1, 0.5, 1.0, 2.0]
    if args.gamma is not None:
        gamma_phi_values = [args.gamma]
    
    output = run_scan(L_values, alpha_values, gamma_phi_values, args.output)
    print_summary(output)
