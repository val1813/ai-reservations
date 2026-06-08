"""
S3 Round2 Numerical Verification Script
Tasks 2-4: L>2 inequality verification, Q_global phase transition, Xi parameter
"""
import numpy as np
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Core: Fermion chain in occupation number basis
# ============================================================

def build_occupation_basis(L, N):
    """Generate all occupation number basis states |n_1...n_L> with N particles."""
    from itertools import combinations as comb
    basis = []
    for sites in comb(range(L), N):
        config = np.zeros(L, dtype=int)
        for s in sites:
            config[s] = 1
        basis.append(config)
    return np.array(basis)

def fermion_sign(config, j, k):
    """Compute (-1)^{sum of occupation numbers between j and k}."""
    if j == k:
        return 1
    lo, hi = (j, k) if j < k else (k, j)
    n_between = np.sum(config[lo+1:hi])
    return -1 if n_between % 2 == 1 else 1

def apply_cdag_c(config, j, k, basis_states, index_map):
    """
    Apply c^dag_j c_k to a configuration.
    Returns (new_config_index, sign) or None if annihilates.
    """
    L = len(config)
    if config[k] == 0:  # nothing to annihilate at k
        return None
    if config[j] == 1:  # cannot create at j (already occupied)
        return None

    new_config = config.copy()
    new_config[k] = 0
    new_config[j] = 1

    sign = fermion_sign(config, j, k)

    # Find the index of new_config in basis
    key = tuple(new_config)
    if key in index_map:
        return (index_map[key], sign)
    return None

def build_operator_matrix(basis, index_map, op_func):
    """Build matrix representation of an operator."""
    D = len(basis)
    mat = np.zeros((D, D), dtype=complex)
    for i, config in enumerate(basis):
        result = op_func(config, basis, index_map)
        if result is not None:
            j, val = result
            mat[i, j] = val
    return mat

def build_cdag_c_matrix(L, N, j, k):
    """Build matrix for c^dag_j c_k operator."""
    basis = build_occupation_basis(L, N)
    index_map = {tuple(config): idx for idx, config in enumerate(basis)}
    D = len(basis)
    mat = np.zeros((D, D), dtype=complex)
    for i, config in enumerate(basis):
        result = apply_cdag_c(config, j, k, basis, index_map)
        if result is not None:
            idx, sign = result
            mat[idx, i] = sign  # mat[new, old] = sign
    return mat

def build_hamiltonian_matrix(L, N, h):
    """Build Hamiltonian H = sum h_mn c^dag_m c_n in occupation basis."""
    basis = build_occupation_basis(L, N)
    index_map = {tuple(config): idx for idx, config in enumerate(basis)}
    D = len(basis)
    H = np.zeros((D, D), dtype=complex)
    for m in range(L):
        for n in range(L):
            if abs(h[m, n]) > 1e-15:
                mat = build_cdag_c_matrix(L, N, m, n)
                H += h[m, n] * mat
    return H

def compute_correlation_matrix(psi, basis, index_map, L):
    """Compute C_mn = <c^dag_n c_m> for a state psi."""
    C = np.zeros((L, L), dtype=complex)
    for m in range(L):
        for n in range(L):
            # <psi|c^dag_n c_m|psi>
            val = 0.0 + 0.0j
            for i, config in enumerate(basis):
                result = apply_cdag_c(config, n, m, basis, index_map)
                if result is not None:
                    j, sign = result
                    val += np.conj(psi[i]) * psi[j] * sign
            C[m, n] = val
    return C

def compute_variance_C_R(psi, basis, index_map, L, m, n):
    """Compute Delta C^R_mn = sqrt(<(C^R)^2> - <C^R>^2)."""
    # C^R_mn = (c^dag_n c_m + c^dag_m c_n) / 2
    # We need <(c^dag_n c_m + c^dag_m c_n)^2> and <c^dag_n c_m + c^dag_m c_n>

    # First: compute <A> where A = c^dag_n c_m + c^dag_m c_n
    A_mean = 0.0 + 0.0j
    for i, config in enumerate(basis):
        # Apply A to config
        res1 = apply_cdag_c(config, n, m, basis, index_map)
        res2 = apply_cdag_c(config, m, n, basis, index_map)

        amp = 0.0 + 0.0j
        if res1 is not None:
            idx1, sign1 = res1
            amp += sign1 * psi[idx1]
        if res2 is not None:
            idx2, sign2 = res2
            amp += sign2 * psi[idx2]

        A_mean += np.conj(psi[i]) * amp

    # For the variance, we need <A^2> = ||A|psi>||^2
    A2_mean = 0.0
    for i, config in enumerate(basis):
        # A|config>
        amp1 = 0.0 + 0.0j
        res1 = apply_cdag_c(config, n, m, basis, index_map)
        res2 = apply_cdag_c(config, m, n, basis, index_map)
        if res1 is not None:
            idx1, sign1 = res1
            amp1 += sign1 * psi[idx1]
        if res2 is not None:
            idx2, sign2 = res2
            amp1 += sign2 * psi[idx2]

        A2_mean += np.abs(amp1)**2

    var = A2_mean - np.abs(A_mean)**2
    if var < -1e-12:
        # Numerical noise
        var = max(var, 0.0)

    delta_C_R = np.sqrt(max(var, 0.0)) / 2.0  # C^R = A/2
    return delta_C_R, A_mean / 2.0

def compute_variance_C_I(psi, basis, index_map, L, m, n):
    """Compute Delta C^I_mn = sqrt(<(C^I)^2> - <C^I>^2)."""
    # C^I_mn = (c^dag_n c_m - c^dag_m c_n) / (2i)
    # B = i(c^dag_n c_m - c^dag_m c_n), so C^I = -B/2

    # First: compute <B> where B = i(c^dag_n c_m - c^dag_m c_n)
    B_mean = 0.0 + 0.0j
    for i, config in enumerate(basis):
        res1 = apply_cdag_c(config, n, m, basis, index_map)
        res2 = apply_cdag_c(config, m, n, basis, index_map)

        amp = 0.0 + 0.0j
        if res1 is not None:
            idx1, sign1 = res1
            amp += 1j * sign1 * psi[idx1]
        if res2 is not None:
            idx2, sign2 = res2
            amp += -1j * sign2 * psi[idx2]

        B_mean += np.conj(psi[i]) * amp

    # ||B|psi>||^2
    B2_mean = 0.0
    for i, config in enumerate(basis):
        amp1 = 0.0 + 0.0j
        res1 = apply_cdag_c(config, n, m, basis, index_map)
        res2 = apply_cdag_c(config, m, n, basis, index_map)
        if res1 is not None:
            idx1, sign1 = res1
            amp1 += 1j * sign1 * psi[idx1]
        if res2 is not None:
            idx2, sign2 = res2
            amp1 += -1j * sign2 * psi[idx2]

        B2_mean += np.abs(amp1)**2

    var = B2_mean - np.abs(B_mean)**2
    if var < -1e-12:
        var = max(var, 0.0)

    delta_C_I = np.sqrt(max(var, 0.0)) / 2.0  # C^I = -B/2
    return delta_C_I, B_mean / (-2.0)

def build_hopping_hamiltonian(L, J=1.0, alpha=3.0, boundary='open'):
    """Build single-particle hopping Hamiltonian h_mn."""
    h = np.zeros((L, L))
    if boundary == 'open':
        for m in range(L):
            for n in range(L):
                if m == n:
                    continue
                d = abs(m - n)
                h[m, n] = -J / (d ** alpha)
    elif boundary == 'periodic':
        for m in range(L):
            for n in range(L):
                if m == n:
                    continue
                d = min(abs(m - n), L - abs(m - n))
                h[m, n] = -J / (d ** alpha)
    return h

def build_xxz_hamiltonian(L, J=1.0, Delta=0.5, alpha=3.0, boundary='open'):
    """
    Build XXZ-like single-particle Hamiltonian.
    For simplicity, use free fermion limit determined by hopping parameters.
    The XXZ interaction term is treated at mean-field level via effective hopping.
    """
    h = build_hopping_hamiltonian(L, J, alpha, boundary)
    # Add on-site potential from mean-field interaction
    # Simple model: staggered or uniform potential
    # For testing the inequality, the specific H form doesn't matter much
    # as long as it's Hermitian
    return h

# ============================================================
# Task 2: L>2 inequality verification
# ============================================================

def verify_inequality_for_system(L, N, h, psi=None):
    """
    Verify inequality Delta C^R_mn * Delta C^I_mn >= 0.25 * |<n_n> - <n_m>|
    for all pairs (m,n) with m < n.
    """
    basis = build_occupation_basis(L, N)
    index_map = {tuple(config): idx for idx, config in enumerate(basis)}

    # Get ground state
    if psi is None:
        H_mat = build_hamiltonian_matrix(L, N, h)
        evals, evecs = np.linalg.eigh(H_mat)
        psi = evecs[:, 0].astype(complex)  # ground state

    C = compute_correlation_matrix(psi, basis, index_map, L)

    violations = []
    results = []

    for m in range(L):
        for n in range(m+1, L):
            # Compute variances
            delta_CR, CR_mean = compute_variance_C_R(psi, basis, index_map, L, m, n)
            delta_CI, CI_mean = compute_variance_C_I(psi, basis, index_map, L, m, n)

            # <n_n> = C_nn (diagonal of correlation matrix)
            n_n = np.real(C[n, n])
            n_m = np.real(C[m, m])
            delta_n = abs(n_n - n_m)

            product = delta_CR * delta_CI
            lower_bound = 0.25 * delta_n

            results.append({
                'm': m, 'n': n,
                'delta_CR': delta_CR, 'delta_CI': delta_CI,
                'product': product, 'lower_bound': lower_bound,
                'n_n': n_n, 'n_m': n_m, 'delta_n': delta_n,
                'CR_mean': CR_mean, 'CI_mean': CI_mean,
                'satisfied': product >= lower_bound - 1e-10
            })

            if product < lower_bound - 1e-10:
                violations.append({
                    'm': m, 'n': n,
                    'product': product, 'lower_bound': lower_bound,
                    'violation': lower_bound - product,
                    'relative': (lower_bound - product) / max(abs(lower_bound), 1e-15)
                })

    return results, violations

def scan_parameters(L_values, J_values, alpha_values, N_filling='half'):
    """Scan parameters and verify the inequality."""
    all_results = {}

    for L in L_values:
        print(f"\n{'='*60}")
        print(f"Scanning L={L}...")
        print(f"{'='*60}")

        N = L // 2 if N_filling == 'half' else N_filling
        total_pairs = 0
        total_violations = 0

        for J in J_values:
            for alpha in alpha_values:
                h = build_hopping_hamiltonian(L, J, alpha, boundary='open')

                try:
                    results, violations = verify_inequality_for_system(L, N, h)

                    n_pairs = len(results)
                    n_viol = len(violations)
                    total_pairs += n_pairs
                    total_violations += n_viol

                    key = (L, J, alpha)
                    all_results[key] = {
                        'n_pairs': n_pairs,
                        'n_violations': n_viol,
                        'violations': violations,
                        'results': results
                    }

                    if n_viol > 0:
                        print(f"  L={L}, J={J:.1f}, alpha={alpha:.1f}: "
                              f"{n_viol}/{n_pairs} VIOLATIONS!")
                        for v in violations:
                            print(f"    pair ({v['m']},{v['n']}): "
                                  f"prod={v['product']:.6e}, "
                                  f"bound={v['lower_bound']:.6e}, "
                                  f"violation={v['violation']:.2e}")
                    else:
                        if len(J_values) * len(alpha_values) <= 4:
                            min_ratio = min(r['product'] / max(r['lower_bound'], 1e-15)
                                          for r in results)
                            print(f"  L={L}, J={J:.1f}, alpha={alpha:.1f}: "
                                  f"ALL {n_pairs} pairs SATISFIED "
                                  f"(min ratio={min_ratio:.4f})")
                except Exception as e:
                    print(f"  L={L}, J={J:.1f}, alpha={alpha:.1f}: ERROR - {e}")

        print(f"  L={L} total: {total_violations}/{total_pairs} violations "
              f"({100*total_violations/max(total_pairs,1):.2f}%)")

    return all_results

# ============================================================
# Task 3: Q_global phase transition search
# ============================================================

def compute_Q_global(psi, basis, index_map, L):
    """Compute Q_global = (1/N_pairs) * sum_{m<n} Delta C^R_mn * Delta C^I_mn."""
    total = 0.0
    n_pairs = 0
    for m in range(L):
        for n in range(m+1, L):
            delta_CR, _ = compute_variance_C_R(psi, basis, index_map, L, m, n)
            delta_CI, _ = compute_variance_C_I(psi, basis, index_map, L, m, n)
            total += delta_CR * delta_CI
            n_pairs += 1
    return total / n_pairs if n_pairs > 0 else 0.0

def build_driven_hamiltonian(L, J, alpha, g, drive_type='tilt'):
    """
    Build driven Hamiltonian. Drives the system away from equilibrium.

    drive_type='tilt': Add a tilt potential g * sum_m m * n_m
    drive_type='boundary': Add boundary driving g * (n_0 - n_{L-1})
    """
    h = build_hopping_hamiltonian(L, J, alpha, boundary='open')

    if drive_type == 'tilt':
        # Tilt potential: E * sum_m m * n_m
        for m in range(L):
            h[m, m] += g * (m - (L-1)/2.0)  # center the tilt
    elif drive_type == 'boundary':
        h[0, 0] += g
        h[L-1, L-1] -= g
    elif drive_type == 'staggered':
        for m in range(L):
            h[m, m] += g * (-1)**m

    return h

def scan_Q_global(L, N, J, alpha, g_values, drive_type='boundary'):
    """Scan Q_global as function of driving strength g."""
    basis = build_occupation_basis(L, N)
    index_map = {tuple(config): idx for idx, config in enumerate(basis)}

    Q_values = []
    delta_n_avg = []

    for g in g_values:
        h = build_driven_hamiltonian(L, J, alpha, g, drive_type)
        H_mat = build_hamiltonian_matrix(L, N, h)
        evals, evecs = np.linalg.eigh(H_mat)
        psi = evecs[:, 0]

        Q = compute_Q_global(psi, basis, index_map, L)
        Q_values.append(Q)

        # Also compute average |delta_n|
        C = compute_correlation_matrix(psi, basis, index_map, L)
        delta_n_sum = 0.0
        n_pairs = 0
        for m in range(L):
            for n in range(m+1, L):
                delta_n_sum += abs(np.real(C[n, n] - C[m, m]))
                n_pairs += 1
        delta_n_avg.append(delta_n_sum / n_pairs if n_pairs > 0 else 0.0)

    return np.array(Q_values), np.array(delta_n_avg)

def find_kinks(Q_values, g_values):
    """Look for non-analytic behavior: kinks/discontinuities in derivative."""
    if len(g_values) < 3:
        return []

    # First derivative (finite difference)
    dg = g_values[1] - g_values[0]
    dQ = np.gradient(Q_values, dg)

    # Second derivative
    d2Q = np.gradient(dQ, dg)

    # Look for peaks in |d2Q| (kink candidates)
    kinks = []
    for i in range(1, len(d2Q) - 1):
        # A kink has large second derivative relative to neighbors
        if abs(d2Q[i]) > 3 * np.std(np.abs(d2Q)) and abs(d2Q[i]) > 1e-10:
            kinks.append({
                'index': i,
                'g': g_values[i],
                'Q': Q_values[i],
                'dQ': dQ[i],
                'd2Q': d2Q[i],
                'd2Q_rel': abs(d2Q[i]) / (np.std(np.abs(d2Q)) + 1e-15)
            })

    return kinks

# ============================================================
# Task 4: Xi safety parameter verification (L=2 Redfield)
# ============================================================

def verify_xi_parameter_L2(gamma_RR, gamma_RI, gamma_II, lambda_val):
    """
    For L=2 Redfield-like system, compute Xi and check dynamics classification.

    The 2x2 matrix M = [[gamma_RR, gamma_RI - lambda], [gamma_IR + lambda, gamma_II]]
    with gamma_IR = -gamma_RI.
    """
    gamma_IR = -gamma_RI

    M = np.array([
        [gamma_RR, gamma_RI - lambda_val],
        [gamma_IR + lambda_val, gamma_II]
    ])

    evals = np.linalg.eigvals(M)

    # Classify dynamics
    real_parts = np.real(evals)
    imag_parts = np.imag(evals)

    if max(abs(imag_parts)) < 1e-10:
        # Both real
        if np.all(real_parts < 0):
            dyn_type = 'stable_node'
        elif np.all(real_parts > 0):
            dyn_type = 'unstable_node'
        else:
            dyn_type = 'saddle'
    else:
        # Complex conjugate pair
        if np.all(real_parts < -1e-10):
            dyn_type = 'stable_focus'
        elif np.all(real_parts > 1e-10):
            dyn_type = 'unstable_focus'
        elif max(abs(real_parts)) < 1e-10:
            dyn_type = 'center'
        else:
            dyn_type = 'mixed'

    # Compute Xi
    Xi = max(abs(gamma_RI), abs(gamma_RR)) / max(abs(gamma_II), 1e-15)

    return {
        'Xi': Xi,
        'evals': evals,
        'dyn_type': dyn_type,
        'gamma_RR': gamma_RR,
        'gamma_RI': gamma_RI,
        'gamma_II': gamma_II,
        'lambda': lambda_val
    }

def scan_xi_parameter():
    """Scan Xi parameter and check dynamics changes."""
    lambda_val = 1.0  # Fix system frequency

    # Scan ranges
    gamma_II_values = np.logspace(-2, 2, 50)  # 0.01 to 100
    gamma_RR_values = np.logspace(-2, 1, 20)   # 0.01 to 10
    gamma_RI_values = np.logspace(-2, 1, 20)   # 0.01 to 10

    all_xi = []
    dyn_transitions = []  # Points where dynamics type changes

    prev_type = None
    prev_xi = None

    # More systematic: fix gamma_II, scan gamma_RR and gamma_RI
    for gamma_II in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        for gamma_RR in np.linspace(0, gamma_II*2, 30):
            for gamma_RI in np.linspace(0, gamma_II*2, 30):
                result = verify_xi_parameter_L2(gamma_RR, gamma_RI, gamma_II, lambda_val)

                if prev_type is not None and result['dyn_type'] != prev_type:
                    dyn_transitions.append({
                        'xi': result['Xi'],
                        'from_type': prev_type,
                        'to_type': result['dyn_type'],
                        'gamma_RR': gamma_RR,
                        'gamma_RI': gamma_RI,
                        'gamma_II': gamma_II
                    })

                prev_type = result['dyn_type']
                all_xi.append(result)

    # Analyze: at what Xi value do transitions typically occur?
    trans_xi = [t['xi'] for t in dyn_transitions]

    # Check specifically: does Xi=1 correspond to dynamics changes?
    near_one = [t for t in dyn_transitions if abs(t['xi'] - 1.0) < 0.2]
    xi_histogram = {}
    for t in dyn_transitions:
        xi_bin = round(t['xi'], 1)
        xi_histogram[xi_bin] = xi_histogram.get(xi_bin, 0) + 1

    return {
        'n_total': len(all_xi),
        'n_transitions': len(dyn_transitions),
        'trans_xi_mean': np.mean(trans_xi) if trans_xi else None,
        'trans_xi_std': np.std(trans_xi) if trans_xi else None,
        'transitions': dyn_transitions[:20],  # First 20
        'xi_histogram': dict(sorted(xi_histogram.items())),
        'near_xi_1': len(near_one),
        'near_xi_1_fraction': len(near_one) / max(len(dyn_transitions), 1)
    }

# ============================================================
# Task 2 extended: Verify correct L=2 formula
# ============================================================

def verify_L2_formula():
    """Verify the correct L=2 variance formula derived by INSPECTOR."""
    print("\n" + "="*60)
    print("Verifying correct L=2 variance formula")
    print("="*60)

    L, N = 2, 1  # Single particle on 2 sites

    basis = build_occupation_basis(L, N)
    index_map = {tuple(config): idx for idx, config in enumerate(basis)}

    # Test various alpha, beta values
    test_cases = [
        (1.0, 0.0),        # Fock state |10>
        (0.0, 1.0),        # Fock state |01>
        (1/np.sqrt(2), 1/np.sqrt(2)),          # Equal superposition (real)
        (1/np.sqrt(2), 1j/np.sqrt(2)),         # Equal superposition (phase pi/2)
        (np.sqrt(0.7), np.sqrt(0.3)),          # Asymmetric
        (np.sqrt(0.3), np.sqrt(0.7)),          # Asymmetric reversed
        (np.sqrt(0.8), np.sqrt(0.2)*np.exp(1j*np.pi/4)), # Complex phase
        (np.sqrt(0.6), np.sqrt(0.4)*np.exp(1j*np.pi/3)), # Complex phase
    ]

    for alpha, beta in test_cases:
        # Construct |psi> = alpha|10> + beta|01>
        psi = np.zeros(len(basis), dtype=complex)
        for i, config in enumerate(basis):
            if config[0] == 1 and config[1] == 0:
                psi[i] = alpha
            elif config[0] == 0 and config[1] == 1:
                psi[i] = beta

        # Normalize
        psi = psi / np.sqrt(np.sum(np.abs(psi)**2))

        # Numerical computation
        delta_CR_num, CR_mean = compute_variance_C_R(psi, basis, index_map, L, 0, 1)
        delta_CI_num, CI_mean = compute_variance_C_I(psi, basis, index_map, L, 0, 1)

        # Correct formula (INSPECTOR)
        delta_CR_correct = 0.5 * np.sqrt(1 - 4*(np.real(np.conj(alpha)*beta))**2)
        delta_CI_correct = 0.5 * np.sqrt(1 - 4*(np.imag(np.conj(alpha)*beta))**2)

        # Wrong formula (original R1)
        delta_CR_wrong = abs(alpha*beta) / np.sqrt(2)
        delta_CI_wrong = abs(alpha*beta) / np.sqrt(2)

        # Lower bound
        n1 = abs(alpha)**2
        n2 = abs(beta)**2
        lower_bound = 0.25 * abs(n1 - n2)
        product = delta_CR_num * delta_CI_num
        inequality_holds = product >= lower_bound - 1e-10

        print(f"  alpha={alpha:.4f}, beta={beta:.4f}:")
        print(f"    Numerical: delta_CR={delta_CR_num:.6f}, delta_CI={delta_CI_num:.6f}, "
              f"prod={product:.6f}")
        print(f"    Correct:   delta_CR={delta_CR_correct:.6f}, delta_CI={delta_CI_correct:.6f}, "
              f"prod={delta_CR_correct*delta_CI_correct:.6f}")
        print(f"    Wrong:     delta_CR={delta_CR_wrong:.6f}, delta_CI={delta_CI_wrong:.6f}, "
              f"prod={delta_CR_wrong*delta_CI_wrong:.6f}")
        print(f"    Lower bound: {lower_bound:.6f}, inequality: {'PASS' if inequality_holds else 'FAIL'}")

        # Check correspondence
        num_ok = abs(delta_CR_num - delta_CR_correct) < 1e-8
        if not num_ok:
            print(f"    WARNING: Numerical vs correct formula mismatch for delta_CR! "
                  f"(diff={abs(delta_CR_num - delta_CR_correct):.2e})")
        print()

# ============================================================
# Main execution
# ============================================================

if __name__ == '__main__':
    print("="*60)
    print("S3 Round2: Numerical Verification Suite")
    print("="*60)

    # --- L=2 formula verification ---
    verify_L2_formula()

    # --- Task 2: L>2 inequality scan ---
    print("\n" + "="*60)
    print("Task 2: L>2 Inequality Verification")
    print("="*60)

    # Quick scan: moderate parameter ranges
    L_values = [4, 6, 8]
    J_values = [0.1, 0.5, 1.0, 2.0, 5.0]
    alpha_values = [0.5, 1.0, 1.5, 2.0, 3.0]

    results_inequality = scan_parameters(L_values, J_values, alpha_values, 'half')

    # --- Task 3: Q_global phase transition ---
    print("\n" + "="*60)
    print("Task 3: Q_global Phase Transition Search")
    print("="*60)

    for L in [4, 6, 8]:
        N = L // 2
        for alpha in [0.5, 1.0, 3.0]:
            for J in [0.5, 1.0, 2.0]:
                print(f"\n  L={L}, N={N}, J={J}, alpha={alpha}")

                # Scan g
                g_values = np.linspace(0, 5.0, 100)

                # Try boundary driving
                Q_boundary, dn_boundary = scan_Q_global(L, N, J, alpha, g_values, 'boundary')
                kinks_boundary = find_kinks(Q_boundary, g_values)

                # Try tilt driving
                Q_tilt, dn_tilt = scan_Q_global(L, N, J, alpha, g_values, 'tilt')
                kinks_tilt = find_kinks(Q_tilt, g_values)

                print(f"    Boundary drive: Q range=[{Q_boundary.min():.6f}, {Q_boundary.max():.6f}], "
                      f"kinks found: {len(kinks_boundary)}")
                if kinks_boundary:
                    for k in kinks_boundary[:3]:
                        print(f"      g={k['g']:.3f}, Q={k['Q']:.6f}, "
                              f"d2Q={k['d2Q']:.6e}")

                print(f"    Tilt drive:     Q range=[{Q_tilt.min():.6f}, {Q_tilt.max():.6f}], "
                      f"kinks found: {len(kinks_tilt)}")
                if kinks_tilt:
                    for k in kinks_tilt[:3]:
                        print(f"      g={k['g']:.3f}, Q={k['Q']:.6e}, "
                              f"d2Q={k['d2Q']:.6e}")

    # --- Task 4: Xi parameter ---
    print("\n" + "="*60)
    print("Task 4: Xi Safety Parameter Verification")
    print("="*60)

    xi_results = scan_xi_parameter()
    print(f"  Total configurations: {xi_results['n_total']}")
    print(f"  Dynamics transitions: {xi_results['n_transitions']}")
    print(f"  Xi at transitions: mean={xi_results['trans_xi_mean']:.4f}, "
          f"std={xi_results['trans_xi_std']:.4f}")
    print(f"  Transitions near Xi=1: {xi_results['near_xi_1']} "
          f"({100*xi_results['near_xi_1_fraction']:.1f}%)")
    print(f"  Xi histogram at transitions:")
    for xi_bin, count in xi_results['xi_histogram'].items():
        bar = '#' * min(count, 50)
        print(f"    {xi_bin:5.1f}: {count:4d} {bar}")

    # Detailed analysis of Xi=1 boundary
    print("\n  Detailed Xi analysis (gamma_II=1.0, lambda=1.0):")
    for gamma_RR in [0.0, 0.5, 1.0, 2.0]:
        for gamma_RI in [0.0, 0.5, 1.0, 2.0]:
            result = verify_xi_parameter_L2(gamma_RR, gamma_RI, 1.0, 1.0)
            print(f"    RR={gamma_RR:.1f}, RI={gamma_RI:.1f}: "
                  f"Xi={result['Xi']:.3f}, type={result['dyn_type']}, "
                  f"evals={np.round(result['evals'], 3)}")

    print("\n" + "="*60)
    print("Numerical verification complete.")
    print("="*60)
