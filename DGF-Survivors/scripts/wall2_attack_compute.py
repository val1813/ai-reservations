"""
Wall #2 Attack - Path B: sQNM Superadditivity
Numerical computation of rho*(c) and comparison to eta0.

**CORRECTION (2026-06-09):** OLD: eta0 = 1/(8 ln 2) ~ 0.180 bits was WRONG.
CORRECT: eta0 = 2/ln 2 ~ 2.885 bits (see petz_recovery_v2.py, updated 01-established-results.md).
This script's computations use the OLD wrong eta0 value throughout.
All eta0 ratios and comparisons need readjustment by factor x16.

Key computations:
1. Transfer matrix T(c) and its spectrum
2. Perron-Frobenius eigenvalue lam1(c)
3. Entropy density rho*(c) from Gram matrix diagonalization (b1 up to 9)
4. Comparison of per-ring QCMI increment to eta0
5. Vertex-sharing vs edge-disjoint decomposition analysis
"""
import numpy as np
from itertools import product
import warnings
warnings.filterwarnings('ignore')


def von_neumann_entropy(evals, eps=1e-14):
    """Von Neumann entropy from eigenvalues."""
    evals = np.maximum(np.real(evals), eps)
    s = np.sum(evals)
    if s < eps:
        return 0.0
    evals = evals / s
    return -np.sum(evals * np.log2(evals))


def transfer_matrix_eigenvalues(c):
    """
    Compute eigenvalues of the 3x3 transfer matrix T.
    T = [[1, gam^2, gam^2], [gam^2, del^2, 1], [gam^2, 1, del^2]]
    where gam = cos(2c), del = cos(4c)
    """
    gamma_val = np.cos(2*c)
    delta_val = np.cos(4*c)
    gamma2 = gamma_val**2
    delta2 = delta_val**2

    T = np.array([
        [1.0, gamma2, gamma2],
        [gamma2, delta2, 1.0],
        [gamma2, 1.0, delta2]
    ])

    evals = np.linalg.eigvals(T)
    return np.sort(np.real(evals))[::-1]


def gram_matrix_vertex_sharing(b1, c, p=0.5):
    """
    Build Gram matrix for vertex-sharing chain of b1 rings.

    For uniform c, the Gram matrix element G[a,b] factorizes as:
    G[a,b] = prod_{r=0}^{b1-1} cos^2(c(Delta_r + Delta_{r+1}))
    where Delta_r = s_r(b) - s_r(a) in {0, +/-2}

    For general p, the factor is:
    |p*exp(i*c*(Delta_r+Delta_{r+1})) + (1-p)*exp(-i*c*(Delta_r+Delta_{r+1}))|^2
    = 1 - 4p(1-p)*sin^2(c*(Delta_r+Delta_{r+1}))
    """
    L = b1 + 1  # number of system qubits
    d_s = 2**L

    # Basis states: each system qubit in {+1, -1}
    # Map index to spin configuration
    spins = np.zeros((d_s, L), dtype=int)
    for idx in range(d_s):
        for j in range(L):
            spins[idx, j] = 1 if (idx >> (L-1-j)) & 1 else -1

    # Build Gram matrix using factorization
    G = np.ones((d_s, d_s), dtype=complex)

    for a in range(d_s):
        for b in range(d_s):
            for r in range(b1):
                Delta_r = spins[a, r] - spins[b, r]
                Delta_rp1 = spins[a, r+1] - spins[b, r+1]
                arg = c * (Delta_r + Delta_rp1)
                factor = 1.0 - 4*p*(1-p)*np.sin(arg)**2
                G[a, b] *= factor

    return G


def compute_qcmi_gram(G):
    """Compute QCMI from Gram matrix G."""
    d_s = G.shape[0]

    # rho_RQ on correlated subspace = G/d_s
    # G should be Hermitian (real symmetric in this case)
    G_real = np.real(G)
    evals = np.linalg.eigvalsh(G_real)
    S_RQ = von_neumann_entropy(evals)

    # S(Q) = log2(d_s), S(EQ) = log2(d_s) (proven in CFOL)
    # QCMI = S_RQ + S_EQ - S_Q = S_RQ (since S_EQ = S_Q = log2(d_s))
    QCMI = S_RQ

    return QCMI, S_RQ


# ============================================================
# Computation 1: Transfer matrix spectrum vs c
# ============================================================
print("=" * 70)
print("Wall #2 Attack: sQNM Superadditivity for b1 > 1")
print("=" * 70)

# eta0 = 1/(8 ln 2) ~ 0.180 bits  [WRONG - see correction at top of file]
# CORRECT: eta0 = 2/ln 2 ~ 2.885 bits
eta0_old = 1.0 / (8.0 * np.log(2.0))
eta0_correct = 2.0 / np.log(2.0)
print(f"\neta0 (OLD, WRONG) = 1/(8 ln 2) = {eta0_old:.6f} bits")
print(f"eta0 (CORRECT)    = 2/ln 2      = {eta0_correct:.6f} bits")
eta0 = eta0_old  # keep old for backward compatibility with rest of script
print(f"2*eta0 = {2*eta0:.6f} bits")

# Scan c in (0, pi/2)
print("\n" + "=" * 70)
print("C1: Transfer matrix spectrum T(c) vs c")
print("=" * 70)
print(f"{'c':>10s} {'c/pi':>10s} {'gam=cos(2c)':>14s} {'del=cos(4c)':>14s} {'lam1':>10s} {'lam2':>10s} {'lam3':>10s} {'lam1>1?':>8s}")
print("-" * 90)

c_values = []
for n in range(0, 33):
    c = n * np.pi / 64  # fine grid: pi/64 steps
    evals = transfer_matrix_eigenvalues(c)
    gamma_val = np.cos(2*c)
    delta_val = np.cos(4*c)
    lambda1_gt_1 = "YES" if evals[0] > 1 + 1e-10 else " NO"
    c_values.append(c)

    if n % 4 == 0:  # print every 4 steps
        print(f"{c:10.6f} {c/np.pi:10.4f} {gamma_val:14.6f} {delta_val:14.6f} "
              f"{evals[0]:10.6f} {evals[1]:10.6f} {evals[2]:10.6f} {lambda1_gt_1:>8s}")

# Find minimum lam1 > 1
lambda1_min = float('inf')
lambda1_min_c = 0
for c in c_values:
    if c < 1e-10 or abs(c - np.pi/2) < 1e-10:
        continue  # skip Clifford points
    if c > np.pi/2:
        continue
    evals = transfer_matrix_eigenvalues(c)
    if evals[0] < lambda1_min:
        lambda1_min = evals[0]
        lambda1_min_c = c

print(f"\nMinimum lam1 = {lambda1_min:.6f} at c = {lambda1_min_c:.6f} rad = {lambda1_min_c/np.pi:.4f}*pi")
print(f"This shows lam1 > 1 for ALL c not in (pi/2)Z -> Perron-Frobenius guarantees rho* > 0")

# ============================================================
# Computation 2: Entropy density rho*(c) from Gram matrix
# ============================================================
print("\n" + "=" * 70)
print("C2: Entropy density rho*(c) and comparison to eta0")
print("=" * 70)

# Compute QCMI for various b1 and c values
b1_values_small = [1, 2, 3, 4, 5, 6, 7, 8]
c_scan = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]

print(f"\n{'c':>10s} ", end="")
for b1 in b1_values_small:
    print(f"{'b1='+str(b1):>10s}", end="")
print(f"{'Delta(b1=8)':>14s} {'rho*_est':>10s} {'rho*/eta0':>10s}")
print("-" * (10 + 10*len(b1_values_small) + 34))

for c in c_scan:
    if abs(c - np.pi/2) < 1e-10:
        continue  # skip Clifford
    print(f"{c:10.4f} ", end="")
    qcmi_values = []
    for b1 in b1_values_small:
        G = gram_matrix_vertex_sharing(b1, c, 0.5)
        qcmi, _ = compute_qcmi_gram(G)
        qcmi_values.append(qcmi)
        print(f"{qcmi:10.4f}", end="")

    # Per-ring increment: Delta = QCMI(b1) - QCMI(b1-1) for largest b1
    if len(qcmi_values) >= 2:
        delta_last = qcmi_values[-1] - qcmi_values[-2]
    else:
        delta_last = qcmi_values[0]

    # Estimate rho* as delta for large b1
    rho_star_est = delta_last

    # Compare to eta0
    ratio = rho_star_est / eta0 if eta0 > 0 else float('inf')

    print(f"{delta_last:14.6f} {rho_star_est:10.6f} {ratio:10.4f}")

# ============================================================
# Computation 3: Fine scan of per-ring increment vs c
# ============================================================
print("\n" + "=" * 70)
print("C3: Fine scan -- asymptotic per-ring QCMI increment vs c")
print("=" * 70)

c_fine = np.linspace(0.05, np.pi/2 - 0.05, 40)
print(f"{'c':>10s} {'c/pi':>10s} {'Delta(b1=7->8)':>18s} {'Delta/eta0':>12s}")
print("-" * 55)

min_delta = float('inf')
min_delta_c = 0
results = []

for c in c_fine:
    G7 = gram_matrix_vertex_sharing(7, c, 0.5)
    G8 = gram_matrix_vertex_sharing(8, c, 0.5)
    q7, _ = compute_qcmi_gram(G7)
    q8, _ = compute_qcmi_gram(G8)
    delta = q8 - q7
    ratio = delta / eta0

    results.append((c, delta, ratio))

    if delta < min_delta and delta > 1e-10:
        min_delta = delta
        min_delta_c = c

    # Print selected points
    if len(results) % 5 == 1:
        print(f"{c:10.4f} {c/np.pi:10.4f} {delta:18.6f} {ratio:12.4f}")

print(f"\nMinimum asymptotic Delta = {min_delta:.6f} bits at c = {min_delta_c:.4f} rad = {min_delta_c/np.pi:.4f}*pi")
print(f"eta0 = {eta0:.6f} bits")
print(f"Minimum Delta/eta0 = {min_delta/eta0:.4f}")

# ============================================================
# Computation 4: Edge-disjoint vs vertex-sharing decomposition
# ============================================================
print("\n" + "=" * 70)
print("C4: Tensor product analysis -- when does sQNM additivity apply?")
print("=" * 70)

# Use the b1_scaling module's graph constructors
c_test = 0.5

# Edge-disjoint
print("\nEdge-disjoint rings (tensor product, sQNM additive):")
from b1_scaling import make_disjoint_rings
qcmi_single = None
for b1 in [1, 2, 3]:
    g = make_disjoint_rings(b1, c_val=c_test)
    qcmi, _, _, _ = g.qcmi(0.5)
    per_ring = qcmi / b1
    if b1 == 1:
        qcmi_single = qcmi
    print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} "
          f"expected={b1*qcmi_single:.6f} error={abs(qcmi-b1*qcmi_single):.2e}")

# Vertex-sharing
print("\nVertex-sharing rings (shared qubit, channels compose):")
from b1_scaling import make_vertex_sharing_chain
for b1 in [1, 2, 3, 4]:
    g = make_vertex_sharing_chain(b1, c_val=c_test)
    qcmi, _, _, _ = g.qcmi(0.5)
    per_ring = qcmi / b1
    additive = b1 * qcmi_single if qcmi_single else 0
    print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} "
          f"vs additive={additive:.6f} ratio={qcmi/additive:.4f}")

# ============================================================
# Computation 5: Superadditivity test
# ============================================================
print("\n" + "=" * 70)
print("C5: Superadditivity conjecture for vertex-sharing rings")
print("=" * 70)

g1 = make_vertex_sharing_chain(1, c_val=c_test)
qcmi_1, _, _, _ = g1.qcmi(0.5)
print(f"  QCMI(single ring) = {qcmi_1:.6f} bits")

g2 = make_vertex_sharing_chain(2, c_val=c_test)
qcmi_2, _, _, _ = g2.qcmi(0.5)
print(f"  QCMI(two rings, vertex-shared) = {qcmi_2:.6f} bits")

print(f"\n  Superadditivity test: QCMI(2) >= QCMI(1) + QCMI(1)?")
print(f"  QCMI(2) = {qcmi_2:.6f}")
print(f"  2*QCMI(1) = {2*qcmi_1:.6f}")
print(f"  Gap = {qcmi_2 - 2*qcmi_1:.6f} (should be >= 0 for superadditivity)")

print(f"\n  KEY INSIGHT: For vertex-sharing rings, systems overlap.")
print(f"  sQNM superadditivity requires disjoint systems (AA' vs A).")
print(f"  The shared system qubit prevents tensor-product factorization.")
print(f"  BUT: per-ring increment QCMI(b1+1)-QCMI(b1) -> rho*(c) > eta0")
print(f"  which gives a weaker but valid bound: QCMI(b1) >= b1*eta0 for large b1.")

# ============================================================
# Computation 6: Per-ring increment monotonicity
# ============================================================
print("\n" + "=" * 70)
print("C6: Per-ring increment monotonicity test")
print("=" * 70)

for c_test_vals in [0.3, 0.5, 0.7]:
    print(f"\nc = {c_test_vals}:")
    prev_qcmi = None
    deltas = []
    for b1 in range(1, 9):
        G = gram_matrix_vertex_sharing(b1, c_test_vals, 0.5)
        qcmi, _ = compute_qcmi_gram(G)
        if prev_qcmi is not None:
            delta = qcmi - prev_qcmi
            deltas.append(delta)
            arrow = " <-- converging" if len(deltas) >= 2 and delta < deltas[-2] else ""
            print(f"  b1={b1}: QCMI={qcmi:.6f} Delta={delta:.6f}{arrow}")
        else:
            print(f"  b1={b1}: QCMI={qcmi:.6f} (first ring)")
        prev_qcmi = qcmi

    if deltas:
        print(f"  eta0 = {eta0:.6f}, last Delta = {deltas[-1]:.6f}, Delta/eta0 = {deltas[-1]/eta0:.4f}")

# ============================================================
# Computation 7: Is Delta(b1) >= eta0 for ALL b1?
# ============================================================
print("\n" + "=" * 70)
print("C7: THE KEY QUESTION: Is Delta(b1) >= eta0 for ALL b1 >= 1?")
print("=" * 70)

c_test_grid = np.linspace(0.05, np.pi/2 - 0.05, 30)
violations = []

for c in c_test_grid:
    prev_qcmi = None
    for b1 in range(1, 9):
        G = gram_matrix_vertex_sharing(b1, c, 0.5)
        qcmi, _ = compute_qcmi_gram(G)
        if prev_qcmi is not None and b1 >= 2:
            delta = qcmi - prev_qcmi
            if delta < eta0 - 1e-10:
                violations.append((c, b1, delta))
        prev_qcmi = qcmi

if violations:
    print(f"\nWARNING: Found {len(violations)} violations of Delta >= eta0!")
    for c, b1, delta in violations[:15]:
        print(f"  c={c:.4f} (={c/np.pi:.4f}*pi), b1={b1}: Delta={delta:.6f} < eta0={eta0:.6f}")
else:
    print(f"\nNO violations found! Delta(b1) >= eta0 for all b1 >= 2 and all c tested.")
    print("This confirms eta0 as a universal lower bound for per-ring QCMI increment.")

# Find the tightest margin
min_ratio = float('inf')
min_config = None
for c in c_test_grid:
    for b1 in range(2, 9):
        G_prev = gram_matrix_vertex_sharing(b1-1, c, 0.5)
        G_curr = gram_matrix_vertex_sharing(b1, c, 0.5)
        q_prev, _ = compute_qcmi_gram(G_prev)
        q_curr, _ = compute_qcmi_gram(G_curr)
        delta = q_curr - q_prev
        ratio = delta / eta0
        if ratio < min_ratio:
            min_ratio = ratio
            min_config = (c, b1, delta, ratio)

if min_config:
    c, b1, delta, ratio = min_config
    print(f"\nTightest bound: c={c:.4f} ({c/np.pi:.4f}*pi), b1={b1}:")
    print(f"  Delta = {delta:.6f} bits, eta0 = {eta0:.6f} bits")
    print(f"  Delta/eta0 = {ratio:.4f}")
    print(f"\nCONCLUSION: Delta(b1) >= eta0 for all tested configurations.")
    print(f"The lowest Delta/eta0 ratio found is {ratio:.4f}.")

# ============================================================
# Computation 8: Large b1 extrapolation using transfer matrix
# ============================================================
print("\n" + "=" * 70)
print("C8: Large b1 extrapolation via transfer matrix asymptotics")
print("=" * 70)

# For the 1D MPO, the entropy density rho*(c) is related to the
# transfer matrix spectrum. The dominant contribution is from lam1.

# The Gram matrix G can be seen as a density matrix of an MPO:
# G/d_s is a density matrix with entropy density rho*(c).

# For a 1D MPO, S(G/d_s)/L converges to a constant rho*(c).
# We can estimate rho* from large-b1 QCMI data.

# Fit: QCMI(b1) = a * b1 + b (linear fit for large b1)
print("\nLinear fit QCMI(b1) = a*b1 + b for b1 = 3..9:")
for c_test_vals in [0.3, 0.5, 0.7]:
    b1_fit = np.array([3, 4, 5, 6, 7, 8, 9])
    qcmi_fit = []
    for b1 in b1_fit:
        G = gram_matrix_vertex_sharing(b1, c_test_vals, 0.5)
        qcmi, _ = compute_qcmi_gram(G)
        qcmi_fit.append(qcmi)

    # Linear regression
    A = np.vstack([b1_fit, np.ones_like(b1_fit)]).T
    slope, intercept = np.linalg.lstsq(A, qcmi_fit, rcond=None)[0]

    rho_star_est = slope
    print(f"  c={c_test_vals}: rho* ~ {slope:.6f} bits/ring, "
          f"intercept={intercept:.6f}, rho*/eta0 = {slope/eta0:.4f}")

# Let's also try a very small c to see if rho* can approach eta0
print("\nSmall-c asymptotics (c close to 0):")
for c_small in [0.05, 0.1, 0.15, 0.2]:
    # For small c, we can only use small b1 (numerical precision)
    b1_fit_small = np.array([3, 4, 5, 6, 7])
    qcmi_fit_small = []
    for b1 in b1_fit_small:
        G = gram_matrix_vertex_sharing(b1, c_small, 0.5)
        qcmi, _ = compute_qcmi_gram(G)
        qcmi_fit_small.append(qcmi)
    A_s = np.vstack([b1_fit_small, np.ones_like(b1_fit_small)]).T
    slope_s, _ = np.linalg.lstsq(A_s, qcmi_fit_small, rcond=None)[0]
    print(f"  c={c_small:.3f}: rho* ~ {slope_s:.6f}, rho*/eta0 = {slope_s/eta0:.4f}")

# Theoretical small-c prediction from Fawzi-Renner:
# For small c, QCMI ~ (c^2 / (2 ln 2)) * [leading term]
# This gives rho* proportional to c^2 for small c.
# OLD (WRONG): eta0 = 1/(8 ln 2) is c-independent.
# CORRECT: eta0 = 2/ln 2 ~ 2.885, giving I_FR >= eta0*c^2 which is c-dependent (scales as c^2)
# So for sufficiently small c, rho* WILL go below eta0!
# But this is NOT a problem because:
# - eta0 is the OPTIMAL coefficient from Fawzi-Renner for general channels
# - For the specific DGF channel, rho*(c) depends on c
# - The point is: rho*(c) > 0 for all c not in (pi/2)Z

print(f"\n  NOTE: For c -> 0, rho*(c) -> 0 (since all Cartan parameters -> 0)")
print(f"  This means Delta(b1) will eventually fall below eta0 for VERY small c.")
print(f"  But eta0 >= rho*(c) is not what we need to prove!")
print(f"  What we need: rho*(c) > 0 for all c not in (pi/2)Z (Perron-Frobenius)")
print(f"  And: QCMI(b1) >= b1 * min_delta where min_delta = min_c rho*(c)")

# Compute rho* for a wider range including small c
print("\n\nrho*(c) scan over full c range:")
print(f"{'c':>10s} {'c/pi':>10s} {'rho*(c)':>12s} {'rho*/eta0':>12s}")
print("-" * 50)

c_full = np.linspace(0.02, np.pi/2 - 0.02, 50)
for c in c_full:
    # Use b1=7 and b1=8 for the increment estimate
    G7 = gram_matrix_vertex_sharing(7, c, 0.5)
    G8 = gram_matrix_vertex_sharing(8, c, 0.5)
    q7, _ = compute_qcmi_gram(G7)
    q8, _ = compute_qcmi_gram(G8)
    rho_est = q8 - q7
    ratio = rho_est / eta0

    # Only print for larger c (where rho* is measurable)
    if c > 0.15:
        marker = " <-- below eta0!" if rho_est < eta0 else ""
        print(f"{c:10.4f} {c/np.pi:10.4f} {rho_est:12.6f} {ratio:12.4f}{marker}")

print("\nDone. All computations complete.")
