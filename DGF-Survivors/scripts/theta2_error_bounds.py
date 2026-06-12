"""
Compute rigorous error bounds for the theta^2 ln(1/theta) analytic formula
for single-ring QCMI.

The Gram matrix for b1=1 vertex-sharing chain is:
  G[a,b] = cos^2(c * (Delta_0 + Delta_1))
where Delta_i = s_i(b) - s_i(a) in {0, +/-2}.

For small theta = c:
  cos^2(2*theta) = 1 - 4*theta^2 + O(theta^4)
  cos^2(4*theta) = 1 - 16*theta^2 + O(theta^4)

The Gram matrix has off-diagonals of three types: 1, cos^2(2c), cos^2(4c).
The dominant error analysis uses epsilon = 4*theta^2 (leading off-diagonal deviation).

We compute:
  1) Exact QCMI via Gram matrix eigendecomposition
  2) Leading-order formula: QCMI_LO = (4*theta^2 / ln2) * (1 + ln(1/(4*theta^2)))
  3) Next-order: QCMI_NO = QCMI_LO - theta^4 / (2*ln2)
  4) Relative errors for both
"""
import numpy as np

def von_neumann_entropy(evals, eps=1e-15):
    """Compute von Neumann entropy from eigenvalues (sorted)."""
    evals = np.maximum(evals, eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))

def build_single_ring_gram_matrix(theta, p=0.5):
    """
    Build the exact 4x4 Gram matrix for a single ring (b1=1 vertex-sharing chain).

    G[a,b] = cos^2(theta * (Delta_0 + Delta_1))
    where Delta_i = s_i(b) - s_i(a), s_i in {+1, -1}.

    Basis ordering: (++), (+-), (-+), (--)
    """
    # Spin basis: index 0->(++), 1->(+-), 2->(-+), 3->(--)
    spins = np.array([(1,1), (1,-1), (-1,1), (-1,-1)], dtype=float)

    G = np.zeros((4, 4))
    for a in range(4):
        for b in range(4):
            delta_0 = spins[b, 0] - spins[a, 0]  # 0, +/-2
            delta_1 = spins[b, 1] - spins[a, 1]  # 0, +/-2
            delta = delta_0 + delta_1  # 0, +/-2, +/-4
            G[a, b] = np.cos(theta * delta) ** 2

    return G

def compute_exact_qcmi(theta):
    """Exact QCMI via Gram matrix diagonalization."""
    G = build_single_ring_gram_matrix(theta)
    d_s = 4

    # Verify all diagonal entries are 1 (trace preserving)
    assert np.allclose(np.diag(G), 1.0), f"Diagonal not 1: {np.diag(G)}"

    # rho_RQ' = G/d_s
    evals = np.linalg.eigvalsh(G / d_s)
    S_RQ = von_neumann_entropy(evals)
    S_Q = np.log2(d_s)
    S_EQ = np.log2(d_s)

    qcmi = S_RQ + S_EQ - S_Q
    return qcmi, S_RQ, evals

def qcmi_leading_order(theta):
    """QCMI_LO = (4*theta^2 / ln2) * (1 + ln(1/(4*theta^2)))."""
    if theta < 1e-15:
        return 0.0
    ln2 = np.log(2.0)
    return (4.0 * theta**2 / ln2) * (1.0 + np.log(1.0 / (4.0 * theta**2)))

def qcmi_next_order(theta):
    """QCMI_NO = QCMI_LO - theta^4 / (2*ln2)."""
    lo = qcmi_leading_order(theta)
    ln2 = np.log(2.0)
    return lo - theta**4 / (2.0 * ln2)

def compute_residual_fit(theta_vals, exact_vals):
    """
    Fit the residual (exact - LO) to A * theta^4 * |log(theta)|.
    Return coefficient A.
    """
    residuals = exact_vals - np.array([qcmi_leading_order(t) for t in theta_vals])
    # Model: residual = A * theta^4 * (-log(theta)) for small theta
    # (residual should be negative since LO overestimates)
    basis = theta_vals**4 * np.abs(np.log(theta_vals))
    # Linear fit through origin
    A = np.sum(residuals * basis) / np.sum(basis**2)
    return A

def compute_residual_fit_theta4(theta_vals, exact_vals):
    """
    Fit the residual (exact - NO) to B * theta^6 * |log(theta)|.
    Return coefficient B.
    """
    no_vals = np.array([qcmi_next_order(t) for t in theta_vals])
    residuals = exact_vals - no_vals
    basis = theta_vals**6 * np.abs(np.log(theta_vals))
    B = np.sum(residuals * basis) / np.sum(basis**2)
    return B

# ================================================================
# Main computation
# ================================================================
print("=" * 75)
print("Theta^2 ln(1/theta) Error Bound Analysis")
print("=" * 75)

# Theta values for analysis
theta_list = [np.pi / 256, np.pi / 128, np.pi / 64, np.pi / 32,
              np.pi / 16, np.pi / 8, np.pi / 4, 3 * np.pi / 8]

print("\n--- Step 1: Exact QCMI vs Analytic Formulas ---")
print(f"{'theta':>12s}  {'theta/pi':>10s}  {'Exact':>12s}  {'LO_formula':>12s}  {'NO_formula':>12s}  "
      f"{'Err_LO%':>10s}  {'Err_NO%':>10s}")
print("-" * 95)

results = []
for theta in theta_list:
    exact, Srq, evals = compute_exact_qcmi(theta)
    lo = qcmi_leading_order(theta)
    no = qcmi_next_order(theta)
    err_lo = 100.0 * abs(exact - lo) / max(exact, 1e-15) if exact > 1e-15 else 0.0
    err_no = 100.0 * abs(exact - no) / max(exact, 1e-15) if exact > 1e-15 else 0.0

    results.append({
        'theta': theta,
        'exact': exact,
        'lo': lo,
        'no': no,
        'err_lo': err_lo,
        'err_no': err_no,
        'Srq': Srq,
        'evals': evals
    })

    print(f"  {theta:10.6f}  {theta/np.pi:10.6f}  {exact:12.8f}  {lo:12.8f}  {no:12.8f}  "
          f"{err_lo:8.4f}%  {err_no:8.4f}%")

# ================================================================
# Step 2: Detailed Gram matrix analysis at each theta
# ================================================================
print("\n\n--- Step 2: Gram Matrix Spectral Analysis ---")
print(f"{'theta/pi':>10s}  {'evals (sorted)':>55s}  {'S_RQ':>10s}")
print("-" * 80)
for r in results:
    theta = r['theta']
    evals_4 = sorted(r['evals'] * 4, reverse=True)  # Multiply by d_s=4
    evals_str = "  ".join(f"{e:10.6f}" for e in evals_4)
    print(f"  {theta/np.pi:8.6f}  {evals_str}  {r['Srq']:10.6f}")

# ================================================================
# Step 3: Validity Regimes
# ================================================================
print("\n\n--- Step 3: Validity Regimes ---")
regimes = [
    ("Asymptotic",  lambda t: t < np.pi/32,    results),
    ("Transition",  lambda t: np.pi/32 <= t < np.pi/8, results),
    ("Breakdown",   lambda t: t >= np.pi/8,     results),
]

print(f"\n{'Regime':>15s}  {'theta range':>25s}  {'Max Err(LO)':>15s}  {'Max Err(NO)':>15s}")
print("-" * 75)
for name, pred, res_list in regimes:
    regime_res = [r for r in res_list if pred(r['theta'])]
    if regime_res:
        max_err_lo = max(r['err_lo'] for r in regime_res)
        max_err_no = max(r['err_no'] for r in regime_res)
        if len(regime_res) >= 1:
            theta_range = f"theta <= {max(r['theta']/np.pi for r in regime_res):.4f}*pi"
            if len([r for r in res_list if not pred(r['theta'])]) == 0:
                theta_range = "all theta"
            print(f"  {name:>15s}  {theta_range:>25s}  {max_err_lo:13.4f}%  {max_err_no:13.4f}%")

# More precise version with actual max error per regime
print(f"\n{'Regime':>15s}  {'theta range':>30s}  {'Max Err(LO)':>15s}  {'Max Err(NO)':>15s}")
print("-" * 80)
regime_defs = [
    ("Asymptotic", "theta < pi/32", lambda t: t < np.pi/32),
    ("Asymptotic", "theta < pi/16", lambda t: t < np.pi/16),
    ("Transition", "pi/32 <= theta < pi/8", lambda t: np.pi/32 <= t < np.pi/8),
    ("Breakdown", "theta >= pi/8", lambda t: t >= np.pi/8),
    ("Breakdown", "theta >= pi/4", lambda t: t >= np.pi/4),
]
for name, desc, pred in regime_defs:
    regime_res = [r for r in results if pred(r['theta'])]
    if regime_res:
        max_err_lo = max(r['err_lo'] for r in regime_res)
        max_err_no = max(r['err_no'] for r in regime_res)
        print(f"  {name:>15s}  {desc:>30s}  {max_err_lo:13.4f}%  {max_err_no:13.4f}%")

# ================================================================
# Step 4: Derive rigorous error bound
# ================================================================
print("\n\n--- Step 4: Rigorous Error Bound Fit ---")

# Use only small-theta regime for fitting (theta < pi/16)
fit_results = [r for r in results if r['theta'] < np.pi/16]
theta_fit = np.array([r['theta'] for r in fit_results])
exact_fit = np.array([r['exact'] for r in fit_results])

# Fit residual = exact - LO
residuals_lo = exact_fit - np.array([qcmi_leading_order(t) for t in theta_fit])
basis_theta4_log = theta_fit**4 * np.abs(np.log(theta_fit))
A = np.sum(residuals_lo * basis_theta4_log) / np.sum(basis_theta4_log**2)

print(f"\n  Residual fit (exact - LO) = A * theta^4 * |log(theta)|")
print(f"  A = {A:.6f}")
print(f"  Data points (theta_pi, residual, fit):")
for i, r in enumerate(fit_results):
    t = r['theta']
    res = residuals_lo[i]
    fit_val = A * t**4 * np.abs(np.log(t))
    print(f"    theta={t/np.pi:.6f}*pi: residual={res:+.8e}, fit={fit_val:+.8e}, diff={res-fit_val:+.8e}")

# Also fit residual after next-order correction
residuals_no = exact_fit - np.array([qcmi_next_order(t) for t in theta_fit])
basis_theta6_log = theta_fit**6 * np.abs(np.log(theta_fit))
B = np.sum(residuals_no * basis_theta6_log) / np.sum(basis_theta6_log**2)

print(f"\n  Residual fit (exact - NO) = B * theta^6 * |log(theta)|")
print(f"  B = {B:.6f}")
for i, r in enumerate(fit_results):
    t = r['theta']
    res = residuals_no[i]
    fit_val = B * t**6 * np.abs(np.log(t))
    print(f"    theta={t/np.pi:.6f}*pi: residual={res:+.8e}, fit={fit_val:+.8e}, diff={res-fit_val:+.8e}")

# ================================================================
# Step 5: Dense scan for fitting and verification
# ================================================================
print("\n\n--- Step 5: Dense Log-Spaced Scan ---")
dense_theta = np.logspace(-6, -0.3, 100)  # 10^-6 to ~0.5

dense_exact = []
dense_lo = []
dense_no = []
for t in dense_theta:
    exact, _, _ = compute_exact_qcmi(t)
    lo = qcmi_leading_order(t)
    no = qcmi_next_order(t)
    dense_exact.append(exact)
    dense_lo.append(lo)
    dense_no.append(no)

dense_exact = np.array(dense_exact)
dense_lo = np.array(dense_lo)
dense_no = np.array(dense_no)

# Compute relative errors
dense_err_lo = np.where(dense_exact > 1e-15,
                        100.0 * np.abs(dense_exact - dense_lo) / dense_exact, 0.0)
dense_err_no = np.where(dense_exact > 1e-15,
                        100.0 * np.abs(dense_exact - dense_no) / dense_exact, 0.0)

# Find regimes
asymp_mask = dense_theta < np.pi/32
trans_mask = (np.pi/32 <= dense_theta) & (dense_theta < np.pi/8)
break_mask = dense_theta >= np.pi/8

for name, mask in [("Asymptotic (theta < pi/32)", asymp_mask),
                    ("Transition (pi/32 <= theta < pi/8)", trans_mask),
                    ("Breakdown (theta >= pi/8)", break_mask)]:
    if np.any(mask):
        max_lo = np.max(dense_err_lo[mask])
        max_no = np.max(dense_err_no[mask])
        print(f"  {name:>40s}: max Err_LO={max_lo:.4f}%, max Err_NO={max_no:.4f}%")

# Global fit for A using all data up to pi/8
fit_mask = dense_theta < np.pi/8
t_fit = dense_theta[fit_mask]
e_fit = dense_exact[fit_mask]
lo_fit = dense_lo[fit_mask]
no_fit = dense_no[fit_mask]

res_lo_fit = e_fit - lo_fit
basis_fit = t_fit**4 * np.abs(np.log(t_fit))
A_global = np.sum(res_lo_fit * basis_fit) / np.sum(basis_fit**2)

res_no_fit = e_fit - no_fit
basis_no_fit = t_fit**6 * np.abs(np.log(t_fit))
B_global = np.sum(res_no_fit * basis_no_fit) / np.sum(basis_no_fit**2)

print(f"\n  Global fit (theta < pi/8, 100 points):")
print(f"    A (theta^4 correction) = {A_global:.6f}")
print(f"    B (theta^6 correction) = {B_global:.6f}")

# Verify the bound
print(f"\n  Verification: max |exact - (LO + A*theta^4*|log theta|)| for theta < pi/8:")
corrected_lo = lo_fit + A_global * t_fit**4 * np.abs(np.log(t_fit))
max_residual = np.max(np.abs(e_fit - corrected_lo))
print(f"    {max_residual:.6e} bits")

print(f"\n  Verification: max |exact - (NO + B*theta^6*|log theta|)| for theta < pi/8:")
corrected_no = no_fit + B_global * t_fit**6 * np.abs(np.log(t_fit))
max_residual_no = np.max(np.abs(e_fit - corrected_no))
print(f"    {max_residual_no:.6e} bits")

# ================================================================
# Step 6: Check the S4 claim about epsilon = 4*theta^2
# ================================================================
print("\n\n--- Step 6: Verify epsilon_model vs exact ---")
# The SM claims the Gram matrix is approximated as "diagonal=1, off-diagonal=1-epsilon"
# with epsilon = 4*theta^2. Check how well this simplified model matches.

def entropy_epsilon_model(eps, d=4):
    """Entropy of d x d matrix with diagonal 1 and all off-diagonals 1-eps."""
    # Eigenvalues: lambda_1 = 1 + (d-1)*(1-eps) = d - (d-1)*eps
    #              lambda_{2..d} = 1 - (1-eps) = eps  (d-1 fold)
    evals = np.array([d - (d-1)*eps] + [eps] * (d-1), dtype=float)
    evals = np.maximum(evals, 1e-15)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))

print(f"\n  epsilon=4*theta^2 model entropy vs exact S_RQ:")
print(f"  {'theta/pi':>10s}  {'epsilon':>12s}  {'S_eps_model':>12s}  {'S_exact':>12s}  {'diff':>10s}")
for theta in theta_list[:6]:  # small theta only
    eps = 4.0 * theta**2
    s_eps = entropy_epsilon_model(eps)
    exact, s_rq, _ = compute_exact_qcmi(theta)
    print(f"  {theta/np.pi:10.6f}  {eps:12.6e}  {s_eps:12.8f}  {exact:12.8f}  {s_eps-exact:+10.8f}")

# The true Gram matrix has three types of off-diagonals:
# - cos^2(0) = 1
# - cos^2(2*theta) = 1 - 4*theta^2 + O(theta^4)  (dominant, 8 entries)
# - cos^2(4*theta) = 1 - 16*theta^2 + O(theta^4)  (2 entries)
print(f"\n  True Gram matrix off-diagonal distribution:")
for theta in [np.pi/16, np.pi/32, np.pi/64]:
    G = build_single_ring_gram_matrix(theta)
    # collect off-diagonal values (upper triangle)
    offdiag = []
    for i in range(4):
        for j in range(i+1, 4):
            offdiag.append(G[i,j])
    offdiag = np.array(offdiag)
    eps_2 = 1.0 - np.cos(2*theta)**2  # approx 4*theta^2
    eps_4 = 1.0 - np.cos(4*theta)**2  # approx 16*theta^2
    # Count occurrences
    n_type_0 = np.sum(np.abs(offdiag - 1.0) < 1e-12)  # G=1 off-diagonals
    n_type_2 = np.sum(np.abs(offdiag - np.cos(2*theta)**2) < 1e-12)
    n_type_4 = np.sum(np.abs(offdiag - np.cos(4*theta)**2) < 1e-12)
    print(f"    theta={theta/np.pi:.6f}*pi: 1.0:{n_type_0}, cos^2(2t):{n_type_2}, cos^2(4t):{n_type_4}")

# ================================================================
# Step 7: Analytical eigenvalue structure verification
# ================================================================
print("\n\n--- Step 7: Analytical eigenvalue verification ---")
# As derived: eigenvalues are:
#   lambda_1 = 1 - cos^2(4*theta) = sin^2(4*theta)
#   lambda_2, lambda_3 from 2x2 submatrix [1+cos^2(4t), 2cos^2(2t); 2cos^2(2t), 2]
# These should match eigvalsh of G

for theta in theta_list[:5]:
    G = build_single_ring_gram_matrix(theta)
    evals_exact = sorted(np.linalg.eigvalsh(G), reverse=True)

    # Analytical eigenvalues
    a = np.cos(2*theta)**2
    b = np.cos(4*theta)**2
    lam1 = 1.0 - b  # sin^2(4*theta)
    # 2x2 submatrix
    s = 1.0 + b
    t = 2.0 * a
    disc = np.sqrt((s - 2.0)**2 + 4.0 * t**2)
    lam2 = (s + 2.0 + disc) / 2.0
    lam3 = (s + 2.0 - disc) / 2.0
    evals_analytic = sorted([lam1, lam2, lam3, 0.0], reverse=True)

    match = np.allclose(evals_exact, evals_analytic)
    print(f"  theta={theta/np.pi:.6f}*pi: exact={np.round(evals_exact, 10)}, "
          f"analytic={np.round(evals_analytic, 10)}, match={match}")

print("\nDone.")
