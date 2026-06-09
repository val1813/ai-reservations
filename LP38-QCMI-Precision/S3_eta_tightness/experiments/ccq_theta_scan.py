"""
CCQ Theta Scan: Test the Commutativity Control Theorem (CCQ) claim.

CCQ claims: when all Cartan axes are aligned (all gates use the same generator,
e.g., all Rxx), the QCMI scales as O(|c|^4) rather than O(|c|^2).

Experiment: 4-node cycle Q_a->E1->Q_b->E2->Q_a, all edges Rxx(theta).
Scan theta: pi/2, pi/4, pi/8, pi/16, pi/32, pi/64, pi/128.
Log-log fit: log(QCMI) vs log(theta).

Interpretation:
  slope ~ 4 -> CCQ correct -> inf QCMI/Sigma|c|^2 = 0 -> eta_0 not tight
  slope ~ 2 -> CCQ wrong   -> inf = eta_0 possible    -> eta_0 asymptotically optimal

Output: ccq_theta_scan_results.md
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import curve_fit
import sys, os

# ========== Quantum information utilities ==========

def vn_entropy(rho, eps=1e-14):
    """von Neumann entropy S(rho) = -Tr(rho log2 rho)"""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    """Partial trace: keep specified qubit indices, trace out the rest."""
    n = len(dims)
    d_total = int(np.prod(dims))
    trace_out = [i for i in range(n) if i not in keep]
    dk = int(np.prod([dims[i] for i in keep]))
    result = np.zeros((dk, dk), dtype=complex)
    for bra in range(d_total):
        bra_bits = [(bra >> i) & 1 for i in range(n)]
        bt = tuple(bra_bits[i] for i in trace_out)
        bk = tuple(bra_bits[i] for i in keep)
        bki = sum(bk[i] * (2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2**i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result

def embed_lsb(U2q, a, b, nq):
    """Embed a 2-qubit gate on qubits (a,b) into nq-qubit Hilbert space.
    LSB encoding: qubit 0 is LSB (rightmost bit)."""
    D = 2**nq
    P = np.zeros((D, D), dtype=complex)
    rem = [i for i in range(nq) if i not in (a, b)]
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[a], bi[b]] + [bi[r] for r in rem]
        j = sum(pb[k] * (1 << k) for k in range(nq))
        P[j, i] = 1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2), dtype=complex), U2q) @ P

def make_mixed_rho(n_E, p=0.7):
    """Buscemi mixed state: Phi+_{RQ} ⊗ gamma_E^{⊗ n_E}

    R = (R_a, R_b) is two-qubit reference purifying Q = (Q_a, Q_b).
    gamma_E = diag(p, 1-p) is the single-qubit environment state.

    Returns rho_RQE after tracing out the F purifying system.
    Total system size: 2(R) + 2(Q) + n_E(E) = 4 + n_E qubits (after F trace).
    """
    n_total = 4 + n_E  # R_a,R_b + Q_a,Q_b + E_1..E_nE
    n_with_f = n_total + n_E  # + F_1..F_nE
    dim_F = 2**n_with_f
    psi = np.zeros(dim_F, dtype=complex)
    sp, sq = np.sqrt(p), np.sqrt(1 - p)

    for a in [0, 1]:
        for b in [0, 1]:
            for e_val in range(2**n_E):
                f_val = e_val  # F mirrors E for |psi_p> purification
                # Bit layout: R_a:0, R_b:1, Q_a:2, Q_b:3, E:4.., F:4+n_E..
                idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | (e_val << 4) | (f_val << (4 + n_E))
                amp = 0.5
                for i in range(n_E):
                    bit = (e_val >> i) & 1
                    amp *= (sp if bit == 0 else sq)
                psi[idx] = amp

    rho_full = np.outer(psi, psi.conj())
    keep = list(range(n_total))
    return ptrace(rho_full, keep, [2] * (n_total + n_E))

def compute(rho_RQE, U_QE):
    """Compute QCMI = I(R:QE) - I(R:Q).

    QCMI = S(rho_R) + S(rho_QE) - S(rho_RQE) - [S(rho_R) + S(rho_Q) - S(rho_RQ)]
         = S(rho_QE) + S(rho_RQ) - S(rho_RQE) - S(rho_Q)

    Args:
        rho_RQE: Initial state on R+Q+E (after F traceout)
        U_QE: Unitary on Q+E subsystem
    Returns:
        QCMI, S(R), S(Q), S(RQ), S(QE), S(RQE)
    """
    d_R = 4
    I_R = np.eye(d_R, dtype=complex)

    # Apply U_QE on QE system, identity on R
    # Layout: qubits 0,1=R (fast); 2,3=Q; 4+=E
    # kron(U_QE, I_R) puts U_QE on slow bits (QE), I_R on fast bits (R)
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T

    n_qe = int(np.log2(U_QE.shape[0]))
    n_tot = 2 + n_qe
    dims = [2] * n_tot

    rR = ptrace(sigma, [0, 1], dims)
    rQ = ptrace(sigma, [2, 3], dims)
    rRQ = ptrace(sigma, [0, 1, 2, 3], dims)
    rQE_all = ptrace(sigma, list(range(2, n_tot)), dims)

    SR = vn_entropy(rR)
    SQ = vn_entropy(rQ)
    SRQ = vn_entropy(rRQ)
    SQE = vn_entropy(rQE_all)
    Sall = vn_entropy(sigma)

    qcmi = (SR + SQE - Sall) - (SR + SQ - SRQ)
    return qcmi, SR, SQ, SRQ, SQE, Sall


# ========== Gate factories ==========

def make_Rxx(theta):
    """Rxx(theta) = exp(-i * theta/2 * sigma_x ⊗ sigma_x)"""
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sx, sx))


def build_aligned_cycle(theta):
    """Build 4-cycle Q_a(0)-E1(2)-Q_b(1)-E2(3)-Q_a(0) with Rxx(theta) on all edges.

    All gates share the same Cartan generator sigma_x⊗sigma_x → all axes aligned.
    CCQ claims this yields QCMI = O(theta^4).

    Args:
        theta: Rxx rotation angle
    Returns:
        U_QE: 16x16 unitary (n_qe=4)
    """
    g = make_Rxx(theta)
    # 4-cycle edges: Q_a-E1, E1-Q_b, Q_b-E2, E2-Q_a
    # QE indices: Q_a=0, Q_b=1, E1=2, E2=3
    U1 = embed_lsb(g, 0, 2, 4)  # Q_a(0) - E1(2)
    U2 = embed_lsb(g, 2, 1, 4)  # E1(2) - Q_b(1)
    U3 = embed_lsb(g, 1, 3, 4)  # Q_b(1) - E2(3)
    U4 = embed_lsb(g, 0, 3, 4)  # Q_a(0) - E2(3)
    return U4 @ U3 @ U2 @ U1


# ========== Verification ==========

def verify_setup():
    """Run sanity checks before main scan."""
    print("=" * 60)
    print("SETUP VERIFICATION")
    print("=" * 60)

    n_E = 2
    rho = make_mixed_rho(n_E, p=0.7)

    # 1. Check initial state entropies
    SR = vn_entropy(ptrace(rho, [0, 1], [2]*6))
    SRQ = vn_entropy(ptrace(rho, [0, 1, 2, 3], [2]*6))
    SQ = vn_entropy(ptrace(rho, [2, 3], [2]*6))
    print(f"S(R)_init = {SR:.8f} (expect 2.0): {'OK' if abs(SR-2.0) < 1e-8 else 'WARN: '+str(SR-2.0)}")
    print(f"S(RQ)_init = {SRQ:.8f} (expect 0.0): {'OK' if abs(SRQ) < 1e-8 else 'WARN: '+str(SRQ)}")
    print(f"S(Q)_init = {SQ:.8f} (expect 2.0): {'OK' if abs(SQ-2.0) < 1e-8 else 'WARN: '+str(SQ-2.0)}")

    # 2. Check identity gives QCMI=0
    I16 = np.eye(16, dtype=complex)
    qcmi_id, SR, SQ, SRQ, SQE, Sall = compute(rho, I16)
    print(f"\nQCMI(identity) = {qcmi_id:.12f} (expect 0): {'OK' if abs(qcmi_id) < 1e-10 else 'WARN'}")
    print(f"  S(R)={SR:.8f}  S(Q)={SQ:.8f}  S(RQ)={SRQ:.8f}  S(QE)={SQE:.8f}  S(RQE)={Sall:.8f}")

    # 3. Check Rxx gate commutativity
    print(f"\nCommutativity check (Rxx on shared qubit):")
    for th in [np.pi/2, np.pi/4, np.pi/8]:
        g = make_Rxx(th)
        U01 = np.kron(g, np.eye(2))  # qubits 0,1
        P = np.zeros((8,8), dtype=complex)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    P[i*4 + k*2 + j, i*4 + j*2 + k] = 1.0
        U02 = P.conj().T @ np.kron(g, np.eye(2)) @ P  # qubits 0,2
        comm = np.linalg.norm(U01 @ U02 - U02 @ U01)
        print(f"  theta={th/np.pi:.4f}pi: ||[U01,U02]|| = {comm:.2e} {'COMMUTING' if comm < 1e-10 else 'NON-COMMUTING'}")

    # 4. Check S(R) invariance under cycle
    Uc = build_aligned_cycle(np.pi/4)
    qcmi_test, SR, SQ, SRQ, SQE, Sall = compute(rho, Uc)
    print(f"\nAfter Rxx(pi/4) cycle: S(R)={SR:.8f} (expect 2.0): {'OK' if abs(SR-2.0) < 1e-8 else 'WARN'}")
    print(f"  QCMI={qcmi_test:.8f}  S(Q)={SQ:.8f}  S(RQ)={SRQ:.8f}")

    # 5. Verify unitarity
    print(f"\nU_cycle unitary: {np.allclose(Uc @ Uc.conj().T, np.eye(16))}")

    print("=" * 60)
    return rho


# ========== Main scan ==========

def run_theta_scan(rho, theta_values):
    """Scan QCMI vs theta for aligned Rxx cycle.

    Args:
        rho: Initial RQE state
        theta_values: list of theta angles to scan
    Returns:
        dict: theta -> (qcmi, SR, SQ, SRQ, SQE, Sall)
    """
    results = {}
    for theta in theta_values:
        U = build_aligned_cycle(theta)
        qcmi, SR, SQ, SRQ, SQE, Sall = compute(rho, U)
        results[theta] = (qcmi, SR, SQ, SRQ, SQE, Sall)
        print(f"  theta={theta/np.pi:.6f}pi  QCMI={qcmi:.12e}  S(R)={SR:.8f}")
    return results


def fit_loglog(theta_arr, qcmi_arr):
    """Fit log(QCMI) = alpha * log(theta) + log(A)
    i.e., QCMI = A * theta^alpha

    Excludes theta=0 (log(0) undefined).

    Returns:
        alpha, A, alpha_err, A_err, r_squared
    """
    # Filter out theta=0 and non-positive QCMI
    mask = (theta_arr > 0) & (qcmi_arr > 0)
    t = theta_arr[mask]
    q = qcmi_arr[mask]

    logt = np.log(t)
    logq = np.log(q)

    # Linear fit: log(QCMI) = alpha * log(theta) + log(A)
    coeffs = np.polyfit(logt, logq, 1)
    alpha = coeffs[0]
    logA = coeffs[1]
    A = np.exp(logA)

    # R-squared
    logq_pred = np.polyval(coeffs, logt)
    ss_res = np.sum((logq - logq_pred)**2)
    ss_tot = np.sum((logq - np.mean(logq))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    # Standard errors via standard linear regression formulas
    n = len(t)
    residuals = logq - logq_pred
    sigma2 = np.sum(residuals**2) / (n - 2) if n > 2 else 0
    x_mean = np.mean(logt)
    ssx = np.sum((logt - x_mean)**2)
    alpha_err = np.sqrt(sigma2 / ssx) if ssx > 0 else 0
    A_err = A * np.sqrt(sigma2 * (1/n + x_mean**2 / ssx)) if ssx > 0 else 0

    return alpha, A, alpha_err, A_err, r_squared


# ========== Main ==========

if __name__ == "__main__":
    print("=" * 60)
    print("CCQ THETA SCAN: Testing commutativity-control theorem")
    print("4-node cycle with Rxx(theta) on all edges (aligned Cartan axes)")
    print("=" * 60)

    # --- Setup ---
    rho = verify_setup()

    # --- Theta values ---
    theta_values = [np.pi/2, np.pi/4, np.pi/8, np.pi/16, np.pi/32, np.pi/64, np.pi/128, 0.0]

    print(f"\n{'='*60}")
    print(f"MAIN SCAN: {len(theta_values)-1} nonzero theta values")
    print(f"{'='*60}")

    results = run_theta_scan(rho, theta_values)

    # --- Extract arrays ---
    theta_arr = np.array(theta_values)
    qcmi_arr = np.array([results[t][0] for t in theta_values])
    SR_arr = np.array([results[t][1] for t in theta_values])

    # --- Log-log fit ---
    print(f"\n{'='*60}")
    print("LOG-LOG FIT: QCMI = A * theta^alpha")
    print(f"{'='*60}")

    alpha, A, alpha_err, A_err, r_squared = fit_loglog(theta_arr, qcmi_arr)

    print(f"  alpha = {alpha:.4f} +/- {alpha_err:.4f}")
    print(f"  A     = {A:.6e} +/- {A_err:.6e}")
    print(f"  R^2   = {r_squared:.6f}")

    # --- Residuals ---
    mask = (theta_arr > 0) & (qcmi_arr > 0)
    t_fit = theta_arr[mask]
    q_fit = qcmi_arr[mask]
    q_pred = A * t_fit**alpha
    residuals = q_fit - q_pred
    rel_residuals = residuals / q_fit

    print(f"\n  Residuals:")
    for i in range(len(t_fit)):
        print(f"    theta={t_fit[i]/np.pi:.6f}pi  QCMI={q_fit[i]:.6e}  pred={q_pred[i]:.6e}  "
              f"res={residuals[i]:+.2e}  rel_res={rel_residuals[i]:+.4f}")

    # --- Per-point scaling exponents (local slope between consecutive points) ---
    print(f"\n  Local scaling exponents (d log QCMI / d log theta):")
    local_alphas = []
    for i in range(len(t_fit) - 1):
        la = (np.log(q_fit[i+1]) - np.log(q_fit[i])) / (np.log(t_fit[i+1]) - np.log(t_fit[i]))
        local_alphas.append(la)
        print(f"    theta [{t_fit[i]/np.pi:.4f}pi -> {t_fit[i+1]/np.pi:.4f}pi]: alpha_local = {la:.4f}")

    # --- Compare to CCQ prediction ---
    print(f"\n{'='*60}")
    print("VERDICT")
    print(f"{'='*60}")

    ccq_pred = 4.0
    alt_pred = 2.0

    dist_to_4 = abs(alpha - ccq_pred)
    dist_to_2 = abs(alpha - alt_pred)

    if dist_to_4 < dist_to_2 and dist_to_4 < 0.5:
        verdict = "CCQ CORRECT: QCMI ~ O(theta^4), aligned axes suppress leading order"
        implication = ("inf QCMI / Sigma|c|^2 = 0 -> eta_0 is NOT tight.\n"
                       "The commutativity-based suppression means the QCMI can be made\n"
                       "arbitrarily small relative to the sum of squared Cartan coefficients,\n"
                       "so the inequality bound is not approachable from below.")
    elif dist_to_2 < dist_to_4 and dist_to_2 < 0.5:
        verdict = "CCQ WRONG: QCMI ~ O(theta^2), commutativity does NOT suppress leading order"
        implication = ("inf QCMI / Sigma|c|^2 > 0 -> eta_0 IS asymptotically optimal.\n"
                       "The inequality bound is tight: one can approach eta_0 arbitrarily\n"
                       "closely but never exceed it. This validates the core tightness\n"
                       "direction for LP36.")
    elif alpha > 3.0:
        verdict = f"WEAK CCQ SUPPORT: alpha={alpha:.2f}, closer to 4 than 2 but not definitive"
        implication = ("The data leans toward CCQ being qualitatively correct (suppression exists)\n"
                       "but the quantitative O(theta^4) prediction is not cleanly confirmed.\n"
                       "Requires further investigation with smaller theta or analytic calculation.")
    elif alpha < 2.5:
        verdict = f"WEAK CCQ REJECTION: alpha={alpha:.2f}, closer to 2 than 4"
        implication = ("The data suggests CCQ's O(theta^4) claim is wrong, but some suppression\n"
                       "may still exist. The tightness direction may be viable but needs\n"
                       "more evidence before committing.")
    else:
        verdict = f"INCONCLUSIVE: alpha={alpha:.2f}, between CCQ(4) and alternative(2)"
        implication = ("Cannot cleanly distinguish between O(theta^4) and O(theta^2).\n"
                       "Possible explanations: (a) finite-theta effects mask asymptotic scaling,\n"
                       "(b) subleading O(theta^4) term comparable to leading O(theta^2),\n"
                       "(c) numerical precision limits at small theta.\n"
                       "Recommend: extend scan to theta = pi/256, pi/512 with higher precision.")

    print(f"  Fitted alpha = {alpha:.4f} +/- {alpha_err:.4f}")
    print(f"  Distance to CCQ prediction (alpha=4): {dist_to_4:.4f}")
    print(f"  Distance to alternative (alpha=2): {dist_to_2:.4f}")
    print(f"  R^2 = {r_squared:.6f}")
    print(f"\n  VERDICT: {verdict}")
    print(f"\n  IMPLICATION: {implication}")

    # Check S(R) stability
    print(f"\n  S(R) stability check (should be 2.0 always):")
    SR_max_dev = np.max(np.abs(SR_arr - 2.0))
    print(f"    Max |S(R) - 2.0| = {SR_max_dev:.2e} {'OK' if SR_max_dev < 1e-6 else 'SUSPICIOUS'}")

    # --- Write output ---
    output_path = r'D:\Claude\ai-reservations\LP36-W-Causal-Accumulation\experiments\ccq_theta_scan_results.md'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# CCQ Theta Scan: Commutativity Control Theorem Test\n\n")
        f.write(f"**Date**: 2026-06-09\n")
        f.write(f"**Experiment**: LP36 P0 priority -- test CCQ claim that aligned Cartan axes give QCMI=O(|c|^4)\n\n")

        f.write("## 1. Motivation\n\n")
        f.write("The INSPECTOR review identified that the eta_0 tightness problem hinges on "
                "a key claim of the Commutativity Control Theorem (CCQ):\n\n")
        f.write("> When all Cartan axes are aligned (all gates share the same generator, e.g., all Rxx), "
                "QCMI = O(|c|^4) rather than O(|c|^2).\n\n")
        f.write("If this claim is correct, then inf QCMI / Sigma|c|^2 = 0, meaning eta_0 is NOT tight "
                "(the inequality bound cannot be approached from below).\n\n")
        f.write("If this claim is wrong, then inf QCMI / Sigma|c|^2 > 0, meaning eta_0 IS asymptotically "
                "optimal (the inequality is tight).\n\n")
        f.write("**This experiment determines the entire tightness direction.**\n\n")

        f.write("## 2. Experimental Design\n\n")
        f.write("### Setup\n\n")
        f.write("- **Topology**: 4-node causal ring Q_a -> E1 -> Q_b -> E2 -> Q_a\n")
        f.write("- **Qubits**: 4 QE qubits (Q_a=0, Q_b=1, E1=2, E2=3) + 2 R qubits (R_a=0, R_b=1)\n")
        f.write("- **State**: Buscemi mixed, p=0.7, n_E=2\n")
        f.write("- **Gates**: Rxx(theta) = exp(-i*theta/2 * sigma_x ⊗ sigma_x) on ALL 4 edges\n")
        f.write("- **Key property**: All gates share the same Cartan generator sigma_x⊗sigma_x\n")
        f.write("  -> All Cartan axes aligned in the x-direction\n")
        f.write("  -> CCQ predicts QCMI = O(theta^4)\n\n")

        f.write("### Theta values\n\n")
        f.write("Geometric series: pi/2, pi/4, pi/8, pi/16, pi/32, pi/64, pi/128 (plus theta=0 for baseline)\n\n")

        f.write("### Analysis\n\n")
        f.write("Log-log fit: log(QCMI) = alpha * log(theta) + C\n")
        f.write("- alpha ~ 4 -> CCQ correct -> inf QCMI/Sigma|c|^2 = 0 -> eta_0 not tight\n")
        f.write("- alpha ~ 2 -> CCQ wrong   -> inf > 0 -> eta_0 asymptotically optimal\n\n")

        f.write("## 3. Results\n\n")
        f.write("### Primary data\n\n")
        f.write("| theta (x pi) | theta (rad) | QCMI | S(R) | S(Q) | S(RQ) | S(QE) | S(RQE) |\n")
        f.write("|-------------|-------------|------|------|------|-------|-------|--------|\n")

        for theta in theta_values:
            qcmi, SR, SQ, SRQ, SQE, Sall = results[theta]
            tp = theta / np.pi
            f.write(f"| {tp:.6f} | {theta:.6f} | {qcmi:.8e} | {SR:.6f} | {SQ:.6f} | {SRQ:.6f} | {SQE:.6f} | {Sall:.6f} |\n")

        f.write(f"\n### Rxx gate matrix (first 2x2 block)\n\n")
        g_example = make_Rxx(np.pi/4)
        f.write("Rxx(pi/4) = exp(-i*pi/8 * sigma_x ⊗ sigma_x):\n\n")
        f.write("```\n")
        for i in range(4):
            row = "  ".join(f"{g_example[i,j]:.6f}" for j in range(4))
            f.write(f"  [{row}]\n")
        f.write("```\n\n")

        f.write("## 4. Log-Log Fit\n\n")
        f.write(f"Fitting: log(QCMI) = alpha * log(theta) + log(A)\n\n")
        f.write(f"- **alpha** = {alpha:.4f} +/- {alpha_err:.4f}\n")
        f.write(f"- **A** = {A:.6e} +/- {A_err:.6e}\n")
        f.write(f"- **R^2** = {r_squared:.6f}\n\n")

        f.write("### Fit residuals\n\n")
        f.write("| theta (x pi) | QCMI (actual) | QCMI (predicted) | residual | relative |\n")
        f.write("|-------------|---------------|-----------------|----------|----------|\n")
        for i in range(len(t_fit)):
            f.write(f"| {t_fit[i]/np.pi:.6f} | {q_fit[i]:.6e} | {q_pred[i]:.6e} | {residuals[i]:+.2e} | {rel_residuals[i]:+.4f} |\n")

        f.write("\n### Local scaling exponents\n\n")
        f.write("| theta range (x pi) | local alpha |\n")
        f.write("|-------------------|-------------|\n")
        for i in range(len(local_alphas)):
            f.write(f"| {t_fit[i]/np.pi:.4f} -> {t_fit[i+1]/np.pi:.4f} | {local_alphas[i]:.4f} |\n")

        f.write("\n### Diagnostic: QCMI / theta^2 and QCMI / theta^4\n\n")
        f.write("If CCQ is correct, QCMI/theta^4 should approach a constant as theta -> 0.\n")
        f.write("If CCQ is wrong, QCMI/theta^2 should approach a constant as theta -> 0.\n\n")
        f.write("| theta (x pi) | QCMI / theta^2 | QCMI / theta^4 | QCMI / theta^3 |\n")
        f.write("|-------------|-----------------|-----------------|----------------|\n")
        for theta in theta_values:
            if theta > 0:
                qcmi = results[theta][0]
                f.write(f"| {theta/np.pi:.6f} | {qcmi/theta**2:.6e} | {qcmi/theta**4:.6e} | {qcmi/theta**3:.6e} |\n")

        f.write("\n## 5. Verdict\n\n")
        f.write(f"### Statistical assessment\n\n")
        f.write(f"- Fitted exponent: alpha = {alpha:.4f} +/- {alpha_err:.4f}\n")
        f.write(f"- CCQ prediction (alpha=4): distance = {dist_to_4:.4f}\n")
        f.write(f"- Alternative (alpha=2): distance = {dist_to_2:.4f}\n")
        f.write(f"- R^2 = {r_squared:.6f}\n\n")

        f.write(f"### Diagnosis\n\n")
        f.write(f"**{verdict}**\n\n")

        f.write(f"### Implications for eta_0 tightness\n\n")
        f.write(f"{implication}\n\n")

        f.write("## 6. Numerical Validation\n\n")
        f.write(f"- S(R) max deviation from 2.0: {SR_max_dev:.2e}\n")

        # Identity check
        qcmi_zero = results[0.0][0]
        f.write(f"- QCMI(theta=0) = {qcmi_zero:.2e} (should be 0 for identity gate)\n")
        f.write(f"- All gates mutually commute (same generator sigma_x⊗sigma_x)\n")
        f.write(f"- 4-cycle on 4 QE qubits, R on 2 qubits -> total 6 qubit Hilbert space (64x64)\n\n")

        f.write("## 7. Raw Data\n\n")
        f.write("```\n")
        for theta in theta_values:
            qcmi, SR, SQ, SRQ, SQE, Sall = results[theta]
            f.write(f"theta={theta:.10f} rad ({theta/np.pi:.6f} pi): "
                    f"QCMI={qcmi:.15e} SR={SR:.10f} SQ={SQ:.10f} SRQ={SRQ:.10f} SQE={SQE:.10f} Sall={Sall:.10f}\n")
        f.write("```\n\n")

        f.write("## 8. Limitations\n\n")
        f.write("- Classical simulation limited to n_qe=4 (Hilbert space dim 16 for QE, 64 total)\n")
        f.write("- Only Rxx gates tested; other aligned Cartan directions (Ryy, Rzz) not yet scanned\n")
        f.write("- Single deterministic computation per theta (no statistical averaging)\n")
        f.write("- p=0.7 fixed; other p values may affect prefactor but not scaling exponent\n")
        f.write("- Finite-theta effects: asymptotic O(theta^4) vs O(theta^2) distinction may require theta << pi/128\n")
        f.write("- Numerical precision: double-precision floats, QCMI values as small as ~1e-8 at smallest theta\n")

    print(f"\n{'='*60}")
    print(f"Results written to: {output_path}")
    print(f"{'='*60}")

    sys.exit(0)
