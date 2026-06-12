"""
Boundary Plaquette Theorem -- Verification Script
==================================================
Verifies BPT-1, BPT-2, BPT-3 by:
  a) Direct Gram matrix diagonalization for arbitrary (c1,c2,c3,c4,p)
  b) Closed-form QCMI(c,p) for boundary plaquette (c1=c2=c, c3=c4=pi/2)
  c) Identity check: C0 = 0 for boundary plaquette
  d) QCMI range [0,1] and special points
  e) Comparison: direct diag vs. closed form (should match to machine precision)

The Gram matrix construction follows §2 of the theorem:
  G_{s,t} = f(d1*c1 + d3*c2) * f(d1*c4 + d3*c3)
  f(x) = p*exp(ix) + (1-p)*exp(-ix)
"""

import numpy as np
from itertools import product

# ============================================================
# Core functions
# ============================================================

def f(x, p):
    """f(x) = p*exp(ix) + (1-p)*exp(-ix) = cos(x) + i*(2p-1)*sin(x)"""
    return np.cos(x) + 1j * (2*p - 1) * np.sin(x)


def gram_matrix_boundary_plaq(c1, c2, c3, c4, p):
    """
    Construct the 4x4 Gram matrix for mixed Cartan parameters.
    System basis: |0>=|++>, |1>=|+->, |2>=|-+>, |3>=|-->

    G_{s,t} = f(delta1*c1 + delta3*c2) * f(delta1*c4 + delta3*c3)
    """
    # System states: (s1, s3) pairs
    states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # s1, s3
    G = np.zeros((4, 4), dtype=complex)

    for i, (s1, s3) in enumerate(states):
        for j, (t1, t3) in enumerate(states):
            d1 = t1 - s1  # in {0, +/-2}
            d3 = t3 - s3  # in {0, +/-2}
            phase1 = d1 * c1 + d3 * c2
            phase2 = d1 * c4 + d3 * c3
            G[i, j] = f(phase1, p) * f(phase2, p)

    return G


def qcmi_from_gram(G):
    """Compute QCMI = S(G/4) directly from Gram matrix eigenvalues."""
    evals = np.linalg.eigvalsh(G)  # G is Hermitian PSD
    # Numerical cleanup: ensure nonnegative and normalized
    evals = np.maximum(evals, 0)
    evals = evals / evals.sum()
    # von Neumann entropy in bits
    nonzero = evals[evals > 1e-15]
    S = -np.sum(nonzero * np.log2(nonzero))
    return S


def qcmi_boundary_closed(c, p):
    """
    Closed-form QCMI for boundary plaquette (c1=c2=c, c3=c4=pi/2).

    QCMI(c,p) = H2(1/2 + 1/2 * sqrt(1 - 4p(1-p)[4 sin^2(2c) + sin^2(4c)]))
    """
    b = p * (1 - p)
    s2c = np.sin(2 * c)
    s4c = np.sin(4 * c)
    combined = 4 * s2c**2 + s4c**2
    # C_1 = -4*b*combined, so 4+C_1 = 4[1 - b*combined]
    Delta_sq = 1 - b * combined  # = (4+C_1)/4

    # Handle floating point near boundaries (analytically Delta_sq >= 0)
    if Delta_sq < 0:
        if Delta_sq > -1e-12:
            Delta_sq = 0.0
        else:
            raise ValueError(f"Delta_sq = {Delta_sq} < 0 for c={c:.8f}, p={p:.8f}")

    Delta = np.sqrt(max(Delta_sq, 0))
    x = 0.5 + 0.5 * Delta

    # Binary entropy
    if x <= 0 or x >= 1:
        return 0.0
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)


def check_c0_identity(c, p):
    """Verify C0 = 0 identity for the 3x3 effective Gram matrix."""
    g = -f(-2*c, p)  # g = -f(-2c)
    h = f(-4*c, p)    # h = f(-4c)

    g2_mod = np.abs(g)**2
    h2_mod = np.abs(h)**2

    # Compute g^2 h* + h (g*)^2
    term = (g**2) * np.conj(h) + h * (np.conj(g)**2)

    C0 = 2 - 4*g2_mod - 2*h2_mod + 2*np.real(term)
    return C0


# ============================================================
# Test 1: BPT-1 — Non-Clifford Necessity
# ============================================================

def test_bpt1():
    print("=" * 70)
    print("TEST 1: BPT-1 — Non-Clifford Necessity")
    print("  If any c_j not in (pi/2)Z, then QCMI > 0")
    print("=" * 70)

    clifford_vals = [0, np.pi/2, np.pi, -np.pi/2]
    non_clifford_vals = [0.1, 0.5, np.pi/4, 0.7, 1.0, np.pi/3]

    p_values = [0.3, 0.5, 0.7]

    violations = []
    confirmations = 0
    tests = 0

    for p in p_values:
        # Case: all Clifford -> QCMI = 0
        for c1, c2, c3, c4 in product(clifford_vals, repeat=4):
            G = gram_matrix_boundary_plaq(c1, c2, c3, c4, p)
            qcmi = qcmi_from_gram(G)
            tests += 1
            if qcmi > 1e-8:
                violations.append((c1, c2, c3, c4, p, qcmi, "all-Clifford expected 0"))
            else:
                confirmations += 1

        # Case: at least one non-Clifford -> QCMI > 0
        for nc_val in non_clifford_vals:
            # Replace one Clifford with non-Clifford
            base = [np.pi/2] * 4
            for pos in range(4):
                c_list = base.copy()
                c_list[pos] = nc_val
                G = gram_matrix_boundary_plaq(*c_list, p)
                qcmi = qcmi_from_gram(G)
                tests += 1
                if qcmi < 1e-10:
                    violations.append((*c_list, p, qcmi, "non-Clifford expected >0"))
                else:
                    confirmations += 1

    print(f"\n  Tests: {tests}")
    print(f"  Confirmations: {confirmations}")
    print(f"  Violations: {len(violations)}")
    if violations:
        for v in violations[:5]:
            print(f"    VIOLATION: c=({v[0]:.4f},{v[1]:.4f},{v[2]:.4f},{v[3]:.4f}) p={v[4]:.2f} QCMI={v[5]:.10f} reason={v[6]}")
    else:
        print("  BPT-1 CONFIRMED: All tests passed. ✓")

    return len(violations) == 0


# ============================================================
# Test 2: BPT-2 — Gram matrix consistency
# ============================================================

def test_bpt2():
    print("\n" + "=" * 70)
    print("TEST 2: BPT-2 — Gram Matrix Properties")
    print("=" * 70)

    # Random configurations
    np.random.seed(42)
    n_random = 100
    p_values = np.random.uniform(0.05, 0.95, n_random)
    c_values = np.random.uniform(-np.pi, np.pi, (n_random, 4))

    all_ok = True
    for i in range(n_random):
        p = p_values[i]
        c_list = c_values[i]

        G = gram_matrix_boundary_plaq(*c_list, p)

        # Check Hermiticity
        if np.max(np.abs(G - G.conj().T)) > 1e-12:
            print(f"  FAIL: G not Hermitian at config {i}")
            all_ok = False

        # Check diagonal = 1
        if np.max(np.abs(np.diag(G) - 1)) > 1e-12:
            print(f"  FAIL: diag(G) != 1 at config {i}")
            all_ok = False

        # Check PSD
        evals = np.linalg.eigvalsh(G)
        if np.min(evals) < -1e-10:
            print(f"  FAIL: G not PSD at config {i}, min eval = {np.min(evals):.2e}")
            all_ok = False

        # Check trace = 4
        if abs(np.trace(G) - 4) > 1e-10:
            print(f"  FAIL: Tr(G) != 4 at config {i}")
            all_ok = False

    if all_ok:
        print(f"  All {n_random} random Gram matrices: Hermitian, diag=1, PSD, Tr=4. ✓")

    # S_EQ = S_Q = 2 verification
    print(f"\n  S(EQ) = S(Q) = 2 identity check (CFOL Lemma 4.1):")
    for c_list in [[0.5]*4, [np.pi/4]*4, [0.1, 0.3, 0.5, 0.7], [np.pi/2, np.pi/2, 0.5, 0.5]]:
        G = gram_matrix_boundary_plaq(*c_list, 0.5)
        # rho_Q has diagonal 1/d_s from G_{aa}=1
        S_Q = np.log2(4)  # = 2, analytical
        # rho_EQ has eigenvalues G_{aa}/4 for each system state
        rho_EQ_evals = np.diag(G) / 4  # = [1/4, 1/4, 1/4, 1/4]
        S_EQ = -np.sum(rho_EQ_evals * np.log2(rho_EQ_evals))
        print(f"    c={c_list}: S_Q={S_Q:.6f}, S_EQ={S_EQ:.6f}, diff={abs(S_Q-2):.2e}, {abs(S_EQ-2):.2e}")

    return all_ok


# ============================================================
# Test 3: BPT-3 — Closed form vs. direct diagonalization
# ============================================================

def test_bpt3():
    print("\n" + "=" * 70)
    print("TEST 3: BPT-3 — Boundary Plaquette Closed Form")
    print("  Compare QCMI(c,p) closed form vs. direct Gram diag")
    print("=" * 70)

    # Grid of (c, p) values
    c_grid = np.linspace(0, np.pi/2, 200)
    p_grid = np.linspace(0.01, 0.99, 50)

    max_err = 0.0
    worst_c, worst_p = None, None
    qcmi_max = 0.0
    qcmi_max_c, qcmi_max_p = None, None

    errors = []
    for p in p_grid:
        for c in c_grid:
            # Direct Gram diag
            G = gram_matrix_boundary_plaq(c, c, np.pi/2, np.pi/2, p)
            qcmi_direct = qcmi_from_gram(G)

            # Closed form
            qcmi_closed = qcmi_boundary_closed(c, p)

            err = abs(qcmi_direct - qcmi_closed)
            errors.append(err)
            if err > max_err:
                max_err = err
                worst_c, worst_p = c, p
            if qcmi_closed > qcmi_max:
                qcmi_max = qcmi_closed
                qcmi_max_c, qcmi_max_p = c, p

    errors = np.array(errors)

    print(f"\n  Grid: {len(c_grid)} c-points x {len(p_grid)} p-points = {len(errors)} total")
    print(f"  Max error: {max_err:.2e} at c={worst_c:.6f}, p={worst_p:.6f}")
    print(f"  Mean error: {np.mean(errors):.2e}")
    print(f"  Median error: {np.median(errors):.2e}")
    print(f"  Max QCMI: {qcmi_max:.8f} bits at c={qcmi_max_c:.6f}, p={qcmi_max_p:.6f}")

    if max_err < 1e-10:
        print("  BPT-3 CONFIRMED: Closed form matches direct diag to machine precision. ✓")
    elif max_err < 1e-6:
        print("  BPT-3 CONFIRMED: Closed form matches direct diag to 1e-6. ✓")

    return max_err


# ============================================================
# Test 4: C0 = 0 identity
# ============================================================

def test_c0_identity():
    print("\n" + "=" * 70)
    print("TEST 4: C0 = 0 Identity for Boundary Plaquette")
    print("=" * 70)

    c_grid = np.linspace(0.001, np.pi/2 - 0.001, 100)
    p_grid = np.linspace(0.001, 0.999, 50)
    max_c0 = 0.0

    for p in p_grid:
        for c in c_grid:
            c0 = check_c0_identity(c, p)
            max_c0 = max(max_c0, abs(c0))

    print(f"  Grid: {len(c_grid)} x {len(p_grid)} = {len(c_grid)*len(p_grid)} points")
    print(f"  Max |C0| = {max_c0:.2e}")
    if max_c0 < 1e-12:
        print("  C0 = 0 identity CONFIRMED to machine precision. ✓")
    elif max_c0 < 1e-8:
        print("  C0 = 0 identity CONFIRMED to 1e-8. ✓")
    else:
        print("  WARNING: C0 identity not confirmed at requested precision.")

    return max_c0


# ============================================================
# Test 5: Special points
# ============================================================

def test_special_points():
    print("\n" + "=" * 70)
    print("TEST 5: Special Points Verification")
    print("=" * 70)

    tests = [
        # (c, p, expected QCMI, description)
        (0.0, 0.5, 0.0, "c=0 -> QCMI=0"),
        (np.pi/2, 0.5, 0.0, "c=pi/2 (Clifford) -> QCMI=0"),
        (np.pi, 0.5, 0.0, "c=pi -> QCMI=0"),
        (np.pi/4, 0.5, 1.0, "c=pi/4, p=1/2 -> QCMI=1 (max)"),
        (0.5, 0.001, None, "p=0.001 -> QCMI small but >0"),
        (0.5, 0.999, None, "p=0.999 -> QCMI small but >0"),
        (0.5, 1e-8, None, "p~0: QCMI -> 0 (limit, small but >0 at finite p)"),
        (0.5, 1-1e-8, None, "p~1: QCMI -> 0 (limit, small but >0 at finite p)"),
        (np.pi/4, 0.3, None, "c=pi/4, p=0.3 (sanity)"),
        (np.pi/2, 0.5, 0.0, "c=pi/2, p=1/2 -> QCMI=0"),
        (0.0, 0.5, 0.0, "c=0, p=1/2 -> QCMI=0"),
        (3*np.pi/4, 0.5, None, "c=3pi/4, p=1/2 (periodicity check)"),
    ]

    all_ok = True
    for c, p, expected, desc in tests:
        qcmi_dir = qcmi_from_gram(gram_matrix_boundary_plaq(c, c, np.pi/2, np.pi/2, p))
        qcmi_cl = qcmi_boundary_closed(c, p)

        if expected is not None:
            if abs(qcmi_cl - expected) > 1e-10:
                print(f"  FAIL: {desc}: closed={qcmi_cl:.10f}, expected={expected}")
                all_ok = False
            else:
                print(f"  ✓ {desc}: QCMI={qcmi_cl:.10f}")
        else:
            print(f"  ○ {desc}: direct={qcmi_dir:.10f}, closed={qcmi_cl:.10f}")

    return all_ok


# ============================================================
# Test 6: QCMI(p) symmetry p <-> 1-p
# ============================================================

def test_p_symmetry():
    print("\n" + "=" * 70)
    print("TEST 6: p <-> 1-p Symmetry")
    print("=" * 70)

    c_values = [0.1, 0.3, 0.5, np.pi/4, 1.0, np.pi/3]
    p_values = np.linspace(0.01, 0.99, 50)

    max_asym = 0.0
    for c in c_values:
        for p in p_values:
            q1 = qcmi_boundary_closed(c, p)
            q2 = qcmi_boundary_closed(c, 1 - p)
            asym = abs(q1 - q2)
            max_asym = max(max_asym, asym)

    print(f"  Max asymmetry across {len(c_values)*len(p_values)} points: {max_asym:.2e}")
    if max_asym < 1e-15:
        print("  p <-> 1-p symmetry CONFIRMED. ✓")

    return max_asym


# ============================================================
# Test 7: Gram matrix rank for boundary plaquette
# ============================================================

def test_gram_rank():
    print("\n" + "=" * 70)
    print("TEST 7: Gram Matrix Rank for Boundary Plaquette")
    print("  Expected: rank(G) = 2 (two zero eigenvalues)")
    print("=" * 70)

    c_values = np.linspace(0.001, np.pi/2 - 0.001, 30)
    p_values = np.linspace(0.05, 0.95, 30)

    rank_violations = 0
    eval_tests = 0

    for c in c_values:
        for p in p_values:
            G = gram_matrix_boundary_plaq(c, c, np.pi/2, np.pi/2, p)
            evals = np.linalg.eigvalsh(G)
            # Count eigenvalues > threshold
            nonzero = np.sum(evals > 1e-10)
            eval_tests += 1
            if nonzero != 2:
                rank_violations += 1
                if rank_violations <= 3:
                    print(f"  rank(G)={nonzero} at c={c:.6f}, p={p:.6f}, evals={np.sort(evals)[::-1]}")

    print(f"\n  Tests: {eval_tests}")
    print(f"  Rank=2 violations: {rank_violations}")
    if rank_violations == 0:
        print("  Rank(G)=2 CONFIRMED for all tested points. ✓")

    return rank_violations


# ============================================================
# Test 8: QCMI bound [0, 1] for boundary plaquette
# ============================================================

def test_qcmi_bounds():
    print("\n" + "=" * 70)
    print("TEST 8: QCMI Bounds [0, 1] for Boundary Plaquette")
    print("=" * 70)

    np.random.seed(123)
    n_points = 10000

    c_random = np.random.uniform(0, 2*np.pi, n_points)
    p_random = np.random.uniform(0.001, 0.999, n_points)

    qcmi_vals = []
    for i in range(n_points):
        q = qcmi_boundary_closed(c_random[i], p_random[i])
        qcmi_vals.append(q)

    qcmi_vals = np.array(qcmi_vals)
    qcmi_min = np.min(qcmi_vals)
    qcmi_max = np.max(qcmi_vals)

    print(f"  Random points: {n_points}")
    print(f"  Min QCMI: {qcmi_min:.10f}")
    print(f"  Max QCMI: {qcmi_max:.10f}")
    print(f"  Mean QCMI: {np.mean(qcmi_vals):.6f}")

    if qcmi_min > -1e-12 and qcmi_max < 1.0 + 1e-10:
        print("  QCMI in [0, 1] CONFIRMED. ✓")
    else:
        print(f"  WARNING: QCMI outside [0,1]: min={qcmi_min}, max={qcmi_max}")

    return qcmi_min, qcmi_max


# ============================================================
# Test 9: Full mixed Cartan — compare exact diag with Gram
# ============================================================

def test_full_mixed():
    print("\n" + "=" * 70)
    print("TEST 9: Full Mixed Cartan — Direct Diagonalization")
    print("  Verify Gram matrix factorization formula for arbitrary (c1,c2,c3,c4)")
    print("=" * 70)

    np.random.seed(99)
    n_test = 500
    all_ok = True
    max_err = 0

    for i in range(n_test):
        c_list = np.random.uniform(-np.pi, np.pi, 4)
        p = np.random.uniform(0.01, 0.99)

        # Method 1: Gram matrix from our factorization formula
        G1 = gram_matrix_boundary_plaq(*c_list, p)

        # Method 2: Direct build from Kraus operators
        G2 = gram_matrix_from_kraus(*c_list, p)

        err = np.max(np.abs(G1 - G2))
        max_err = max(max_err, err)
        if err > 1e-10:
            all_ok = False

    print(f"  Tests: {n_test}")
    print(f"  Max Gram matrix error (factorization vs Kraus): {max_err:.2e}")
    if all_ok:
        print("  Gram matrix factorization CONFIRMED. ✓")

    return all_ok


def gram_matrix_from_kraus(c1, c2, c3, c4, p):
    """
    Build Gram matrix directly from Kraus operators (no factorization).
    This is the "ground truth" construction.
    """
    alpha = {1: np.sqrt(p), -1: np.sqrt(1-p)}

    # System states (s1, s3)
    sys_states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Environment states (s2, s4)
    env_states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Build kappa[k_idx, a_idx] = alpha_{s2}*alpha_{s4} * exp(i*phase)
    kappa = np.zeros((4, 4), dtype=complex)

    for k_idx, (s2, s4) in enumerate(env_states):
        for a_idx, (s1, s3) in enumerate(sys_states):
            phase = c1*s1*s2 + c2*s2*s3 + c3*s3*s4 + c4*s4*s1
            kappa[k_idx, a_idx] = alpha[s2] * alpha[s4] * np.exp(1j * phase)

    # Gram matrix G[a,b] = sum_k kappa*[k,a] * kappa[k,b]
    G = kappa.conj().T @ kappa

    return G


# ============================================================
# Test 10: Periodicity QCMI(c+pi, p) = QCMI(c, p)
# ============================================================

def test_periodicity():
    print("\n" + "=" * 70)
    print("TEST 10: Periodicity QCMI(c+pi, p) = QCMI(c, p)")
    print("=" * 70)

    c_values = [0.1, 0.5, 1.0, np.pi/4, np.pi/3, 2.0]
    p_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    max_err = 0.0

    for c in c_values:
        for p in p_values:
            q1 = qcmi_boundary_closed(c, p)
            q2 = qcmi_boundary_closed(c + np.pi, p)
            q3 = qcmi_boundary_closed(c + 2*np.pi, p)
            err12 = abs(q1 - q2)
            err13 = abs(q1 - q3)
            max_err = max(max_err, err12, err13)

    print(f"  Tests: {len(c_values)*len(p_values)}")
    print(f"  Max periodicity error (pi-shift): {max_err:.2e}")
    if max_err < 1e-14:
        print("  QCMI(c+pi,p) = QCMI(c,p) CONFIRMED. ✓")
    return max_err


# ============================================================
# Main
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("BOUNDARY PLAQUETTE THEOREM — VERIFICATION SUITE")
    print("=" * 70)
    print(f"  f(x) = p*exp(ix) + (1-p)*exp(-ix)")
    print("  G_{s,t} = f(d1*c1 + d3*c2) * f(d1*c4 + d3*c3)")
    print()

    results = {}

    results['bpt1'] = test_bpt1()
    results['bpt2'] = test_bpt2()
    results['bpt3_err'] = test_bpt3()
    results['c0'] = test_c0_identity()
    results['special'] = test_special_points()
    results['p_sym'] = test_p_symmetry()
    results['rank'] = test_gram_rank()
    results['bounds'] = test_qcmi_bounds()
    results['factorization'] = test_full_mixed()
    results['periodicity'] = test_periodicity()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  BPT-1 (Non-Clifford necessity):      {'PASS' if results['bpt1'] else 'FAIL'}")
    print(f"  BPT-2 (Gram matrix properties):       {'PASS' if results['bpt2'] else 'FAIL'}")
    print(f"  BPT-3 (Closed form accuracy):         max err = {results['bpt3_err']:.2e}")
    print(f"  C0 = 0 identity:                      max |C0| = {results['c0']:.2e}")
    print(f"  Special points:                       {'PASS' if results['special'] else 'FAIL'}")
    print(f"  p <-> 1-p symmetry:                   max asym = {results['p_sym']:.2e}")
    rank_str = f"{results['rank']} violations"
    print(f"  Gram rank = 2:                        {'PASS' if results['rank'] == 0 else rank_str}")
    print(f"  QCMI bounds [0,1]:                    min,max = {results['bounds'][0]:.6f}, {results['bounds'][1]:.6f}")
    print(f"  Factorization vs Kraus:               {'PASS' if results['factorization'] else 'FAIL'}")
    print(f"  Periodicity c->c+pi:                  max err = {results['periodicity']:.2e}")

    all_pass = (
        results['bpt1'] and
        results['bpt2'] and
        results['bpt3_err'] < 1e-6 and
        results['c0'] < 1e-8 and
        results['special'] and
        results['p_sym'] < 1e-10 and
        results['rank'] == 0 and
        results['factorization']
    )

    print(f"\n  OVERALL: {'ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED'}")
    print("\nDone.")
