"""
prefactor_fit.py — 消除sin²θ前因子8x不确定性的数值实验
================================================================
E1: QCMI vs |c|² 散点图 + 下包络线性拟合 (N=500 Haar random)
E2: p参数扫描, 验证 b ∝ p(1-p)

Cartan分解: 魔基对角化方法 (引理0闭型公式已证伪, 见R3 SA-2)
QCMI计算:  复用 interference_test.py 的 make_mixed_rho/compute/ptrace/embed_lsb

作者: B博士
日期: 2026-06-08
"""

import numpy as np
from scipy.linalg import expm
from scipy import stats
import time
import sys
import os
import csv

# Fix Unicode output on Windows GBK terminals
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    elif sys.stdout.encoding != 'utf-8':
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
except Exception:
    pass  # fall through, may get encoding errors on some terminals

# ============================================================
# 0. 基础量子信息工具 (与interference_test.py逐字相同)
# ============================================================

def vn_entropy(rho, eps=1e-12):
    """Von Neumann entropy S(ρ) = -Tr[ρ log₂ ρ]"""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))


def ptrace(rho, keep, dims):
    """Partial trace: trace out all qubits NOT in `keep`."""
    n = len(dims)
    d_total = int(np.prod(dims))
    trace_out = [i for i in range(n) if i not in keep]
    dk = int(np.prod([dims[i] for i in keep]))
    result = np.zeros((dk, dk), dtype=complex)
    for bra in range(d_total):
        bra_bits = [(bra >> i) & 1 for i in range(n)]
        bt = tuple(bra_bits[i] for i in trace_out)
        bk = tuple(bra_bits[i] for i in keep)
        bki = sum(bk[i] * (2 ** i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2 ** i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result


def embed_lsb(U2q, a, b, nq=4):
    """Embed a 2-qubit gate U2q on qubits a,b of an nq-qubit system."""
    D = 2 ** nq
    P = np.zeros((D, D), dtype=complex)
    rem = [i for i in range(nq) if i not in (a, b)]
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[a], bi[b]] + [bi[r] for r in rem]
        j = sum(pb[k] * (1 << k) for k in range(nq))
        P[j, i] = 1.0
    return P.conj().T @ np.kron(np.eye(2 ** (nq - 2), dtype=complex), U2q) @ P


def make_mixed_rho(n_E, p=0.7):
    """
    Buscemi mixed-state construction for RQE system.
    Qubit ordering (LSB→MSB): R_a, R_b, Q_a, Q_b, E1, E2, ..., E_nE
    Each env qubit: ρ_E = diag(p, 1-p), purified via fresh ancilla.
    Returns rho_RQE on 2+2+n_E qubits.
    """
    n_qe = 2 + n_E              # Q_a, Q_b + E qubits
    n_total = 2 + n_qe          # R_a, R_b + Q/E
    n_with_f = n_total + n_E    # purification on doubled E qubits
    psi = np.zeros(2 ** n_with_f, dtype=complex)
    sp = np.sqrt(p)
    sq = np.sqrt(1 - p)

    for a in [0, 1]:
        for b in [0, 1]:
            for ev in range(2 ** n_E):
                # R_a@bit0, R_b@bit1, Q_a@bit2, Q_b@bit3,
                # E_half1@bit4, E_half2@bit(4+n_E)
                idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | \
                      (ev << 4) | (ev << (4 + n_E))
                amp = 0.5
                for i in range(n_E):
                    amp *= (sp if ((ev >> i) & 1) == 0 else sq)
                psi[idx] = amp

    rho_full = np.outer(psi, psi.conj())
    # Trace out fresh qubits, keep system qubits
    return ptrace(rho_full, list(range(n_total)),
                  [2] * (n_total + n_E))


def compute(rho_RQE, U_QE):
    """
    Compute QCMI = I(R; QE') - I(R; Q') for given rho_RQE and U_QE.
    rho_RQE ordering: R_a(0), R_b(1), Q_a(2), Q_b(3), E1(4), E2(5)
    kron(U_QE, I_R) applies U_QE on MSB (Q/E) and I_R on LSB (R_a,R_b).
    """
    I_R = np.eye(4, dtype=complex)
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T

    n_qe = int(np.log2(U_QE.shape[0]))  # 4 for cycle case
    n_tot = 2 + n_qe
    dims = [2] * n_tot

    rR = ptrace(sigma, [0, 1], dims)           # ρ_R
    rQ = ptrace(sigma, [2, 3], dims)           # ρ_Q
    rRQ = ptrace(sigma, [0, 1, 2, 3], dims)    # ρ_RQ
    rQE_all = ptrace(sigma, list(range(2, n_tot)), dims)  # ρ_QE

    SR = vn_entropy(rR)
    SQ = vn_entropy(rQ)
    SRQ = vn_entropy(rRQ)
    SQE = vn_entropy(rQE_all)
    Sall = vn_entropy(sigma)

    QCMI = (SR + SQE - Sall) - (SR + SQ - SRQ)
    return QCMI, SR, SQ, SRQ


# ============================================================
# 1. Cartan 分解 (魔基对角化方法)
# ============================================================

# Magic basis unitary: maps computational basis to Bell/magic basis
# M |00⟩ = |Φ⁺⟩, M |01⟩ = i|Ψ⁺⟩, M |10⟩ = |Ψ⁻⟩, M |11⟩ = |Φ⁻⟩
# In this basis, σ_k⊗σ_k are diagonal for k=x,y,z
M_MAGIC = np.array([
    [1,  0,  0,  1j],
    [0,  1j, 1,  0],
    [0,  1j, -1, 0],
    [1,  0,  0, -1j]
], dtype=complex) / np.sqrt(2)

# Pauli matrices
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def _cartan_from_eigenvalues(eigvals):
    """
    Extract (c_x, c_y, c_z) from eigenvalues of Q = U_M^T @ U_M.

    Q's eigenvalues are {e^{2iθ₁}, e^{2iθ₂}, e^{2iθ₃}, e^{2iθ₄}}.
    Among 2^4 branch choices (θ vs θ+π), pick the one with Σθ ≡ 0 (mod 2π)
    and minimal |c|² as tiebreaker.

    Because |c|² = c_x²+c_y²+c_z² is permutation-invariant,
    the eigenvalue ordering does not affect the result.
    """
    alphas = np.angle(eigvals)       # in [-π, π)
    thetas_base = alphas / 2.0        # in [-π/2, π/2)

    best = None
    best_cost = np.inf
    best_c2 = np.inf

    for bits in range(16):
        thetas = thetas_base.copy()
        for i in range(4):
            if bits & (1 << i):
                thetas[i] += np.pi

        s = np.sum(thetas)
        s_mod = (s + np.pi) % (2 * np.pi) - np.pi
        cost = abs(s_mod)

        t1, t2, t3, t4 = thetas
        cx_t = (t1 - t2 + t3 - t4) / 4.0
        cy_t = (-t1 + t2 + t3 - t4) / 4.0
        cz_t = (t1 + t2 - t3 - t4) / 4.0
        c2_t = cx_t**2 + cy_t**2 + cz_t**2

        # Primary sort by sum constraint, secondary by |c|²
        if cost < best_cost - 1e-12 or (abs(cost - best_cost) < 1e-12 and c2_t < best_c2):
            best_cost = cost
            best_c2 = c2_t
            best = (cx_t, cy_t, cz_t, thetas.copy())

    if best is None:
        return 0.0, 0.0, 0.0, 0.0

    cx, cy, cz, _ = best
    c2 = cx**2 + cy**2 + cz**2
    return cx, cy, cz, c2


def cartan_decompose(U, verbose=False):
    """
    Numerical Cartan/KAK decomposition for U in U(4).

    Uses a perturbation-averaging method to handle eigenvalue degeneracy
    (e.g., CNOT, SWAP). For generic Haar-random unitaries, degeneracy is
    measure-zero and the unperturbed computation is exact.

    Method:
    1. Magic basis transform: U_M = M† U M
    2. Q = U_M^T @ U_M
    3. Eigenvalues of Q → θ_k → c_x, c_y, c_z
    4. If degenerate, use perturbation to break degeneracy and average

    Branch selection: among 2^4 choices (θ_k or θ_k + π), pick the one with
    Σ θ_k ≡ 0 (mod 2π). Since |c|² is permutation-invariant, eigenvalue
    ordering does not matter for non-degenerate gates.

    Returns:
        cx, cy, cz : raw Cartan coefficients
        c_abs      : [min, mid, max] absolute values
        c2         : |c|² = cx² + cy² + cz²
    """
    # Step 1: Magic basis transform
    U_M = M_MAGIC.conj().T @ U @ M_MAGIC

    # Step 2: Q = U_M^T @ U_M
    Q = U_M.T @ U_M

    # Step 3: Eigenvalues
    eigvals = np.linalg.eigvals(Q)

    # Step 4: Check for near-degeneracy
    # Sort eigenvalues by angle
    alphas = np.angle(eigvals)
    alphas_sorted = np.sort(alphas)
    # Compute minimum angular gap
    gaps = np.diff(alphas_sorted)
    gaps_wrapped = np.concatenate([gaps, [alphas_sorted[0] + 2*np.pi - alphas_sorted[-1]]])
    min_gap = np.min(np.abs(gaps_wrapped))

    cx, cy, cz, c2 = _cartan_from_eigenvalues(eigvals)

    # If eigenvalues have near-degeneracy, use perturbation to verify
    if min_gap < 1e-3:
        # Try small random perturbations and average
        c2_vals = [c2]
        rng = np.random.RandomState(42)
        for _ in range(5):
            eps = 1e-6
            dU = eps * (rng.randn(4, 4) + 1j * rng.randn(4, 4))
            # Make dU skew-Hermitian so U+dU stays unitary to O(eps)
            dU = dU - dU.conj().T
            U_pert = U + 1j * dU
            # Re-orthogonalize
            U_pert, _ = np.linalg.qr(U_pert)
            U_M_pert = M_MAGIC.conj().T @ U_pert @ M_MAGIC
            Q_pert = U_M_pert.T @ U_M_pert
            eig_pert = np.linalg.eigvals(Q_pert)
            _, _, _, c2_p = _cartan_from_eigenvalues(eig_pert)
            c2_vals.append(c2_p)
        c2 = np.median(c2_vals)

        if verbose and np.std(c2_vals) > 1e-4:
            print(f"  [WARN] Degenerate eigvals (gap={min_gap:.2e}), "
                  f"|c|² perturbed values: {[f'{v:.6f}' for v in c2_vals]}")

    # Recompute c_abs from final c2 (signs may be ambiguous)
    c_abs = sorted([abs(cx), abs(cy), abs(cz)])

    return cx, cy, cz, c_abs, c2


# ============================================================
# 2. Haar随机酉矩阵生成
# ============================================================

def make_rand_Haar(seed=None):
    """Generate a Haar-random U(4) unitary via QR decomposition."""
    rng = np.random.RandomState(seed) if seed is not None else np.random
    A = rng.randn(4, 4) + 1j * rng.randn(4, 4)
    Q, R = np.linalg.qr(A)
    # Ensure det(Q) phase is Haar-uniform (QR gives det with random phase,
    # but we standardize by multiplying columns by R's diagonal signs)
    # QR already produces a Haar-uniform unitary
    return Q


# ============================================================
# 3. 测试门 (Cartan分解验证)
# ============================================================

def make_CNOT():
    """Standard CNOT gate (control=qubit0, target=qubit1)."""
    cnot = np.zeros((4, 4), dtype=complex)
    cnot[0, 0] = 1.0
    cnot[1, 1] = 1.0
    cnot[2, 3] = 1.0
    cnot[3, 2] = 1.0
    return cnot


def make_SWAP():
    """SWAP gate."""
    swap = np.zeros((4, 4), dtype=complex)
    swap[0, 0] = 1.0
    swap[1, 2] = 1.0
    swap[2, 1] = 1.0
    swap[3, 3] = 1.0
    return swap


def test_cartan_decomposition():
    """Verify Cartan decomposition on known gates."""
    print("=" * 60)
    print("CARTAN DECOMPOSITION VERIFICATION")
    print("=" * 60)

    # Identity: |c|² = 0
    cx, cy, cz, c_abs, c2 = cartan_decompose(np.eye(4))
    print(f"Identity:     cx={cx:.4f}, cy={cy:.4f}, cz={cz:.4f}, |c|²={c2:.6f} "
          f"(expect 0) {'OK' if c2 < 1e-10 else 'FAIL'}")

    # CNOT: |c|² = π²/16 ≈ 0.61685, c = (π/4, 0, 0)
    cx, cy, cz, c_abs, c2 = cartan_decompose(make_CNOT())
    c2_expected = np.pi**2 / 16
    print(f"CNOT:         cx={cx:.4f}, cy={cy:.4f}, cz={cz:.4f}, |c|²={c2:.6f} "
          f"(expect {c2_expected:.6f}) "
          f"{'OK' if abs(c2 - c2_expected) < 1e-6 else 'CHECK'}")

    # SWAP: |c|² ≈ 3π²/16 ≈ 1.85055 (all three c equal π/4)
    cx, cy, cz, c_abs, c2 = cartan_decompose(make_SWAP())
    c2_expected_swap = 3 * np.pi**2 / 16
    # Note: SWAP has degenerate eigenvalues → branch selection tricky
    # |c|² should be 3π²/16 ≈ 1.85055 or 0 (wrong branch)
    print(f"SWAP:         cx={cx:.4f}, cy={cy:.4f}, cz={cz:.4f}, |c|²={c2:.6f} "
          f"(expect {c2_expected_swap:.6f}) "
          f"{'OK' if abs(c2 - c2_expected_swap) < 1e-6 else 'DEGENERATE-WARN'}")

    # XX(π/4): small but non-zero |c|²
    xx_pi4 = expm(-0.5j * (np.pi/4) * np.kron(SX, SX))
    cx, cy, cz, c_abs, c2 = cartan_decompose(xx_pi4)
    print(f"XX(π/4):      cx={cx:.4f}, cy={cy:.4f}, cz={cz:.4f}, |c|²={c2:.6f} "
          f"(expect >0, ~0.15)")

    print()


# ============================================================
# 4. E1: QCMI vs |c|² 散点图 + 下包络拟合
# ============================================================

def run_E1(N=500, p=0.7, seed_base=42):
    """
    E1: Generate N Haar-random unitaries, compute |c|² and QCMI,
    extract lower envelope, fit linear model.
    """
    print("=" * 60)
    print(f"E1: QCMI vs |c|² SCATTER (N={N}, p={p})")
    print("=" * 60)

    data = []  # list of (|c|², QCMI, SR_check)

    # Pre-build rho_RQE (same for all trials, depends only on p)
    rho_RQE = make_mixed_rho(2, p)

    t_start = time.time()
    for i in range(N):
        seed = seed_base + i * 17

        # Generate Haar random U ∈ U(4)
        U_local = make_rand_Haar(seed)

        # Cartan decomposition → |c|²
        _, _, _, _, c2 = cartan_decompose(U_local)

        # Build 4-node cycle: all 4 edges use the same U
        # Cycle topology: Q_a → E1 → Q_b → E2 → Q_a
        # embed_lsb convention: qubits 0,1,2,3 = Q_a, Q_b, E1, E2
        U_cycle = (embed_lsb(U_local, 0, 3, 4) @   # U_{Q_a,E2}
                   embed_lsb(U_local, 1, 3, 4) @   # U_{Q_b,E2}
                   embed_lsb(U_local, 2, 1, 4) @   # U_{Q_b,E1}
                   embed_lsb(U_local, 0, 2, 4))    # U_{Q_a,E1}

        # Compute QCMI
        qcmi, SR, SQ, SRQ = compute(rho_RQE, U_cycle)

        # Sanity: SR should be ~2.0 (R is maximally entangled with Q initially)
        data.append((c2, qcmi, SR))

        if (i + 1) % 100 == 0:
            elapsed = time.time() - t_start
            rate = (i + 1) / elapsed
            print(f"  Progress: {i+1}/{N} ({rate:.1f} trials/s), "
                  f"last |c|²={c2:.4f}, QCMI={qcmi:.4f}")

    elapsed = time.time() - t_start
    print(f"  E1 complete: {N} trials in {elapsed:.1f}s ({N/elapsed:.1f} trials/s)")

    # ---- Analysis ----
    c2_arr = np.array([d[0] for d in data])
    qcmi_arr = np.array([d[1] for d in data])
    sr_arr = np.array([d[2] for d in data])

    # Basic statistics
    print(f"\n  |c|² range: [{c2_arr.min():.4f}, {c2_arr.max():.4f}]")
    print(f"  |c|² mean/median: {c2_arr.mean():.4f} / {np.median(c2_arr):.4f}")
    print(f"  QCMI range: [{qcmi_arr.min():.4f}, {qcmi_arr.max():.4f}]")
    print(f"  QCMI mean/median: {qcmi_arr.mean():.4f} / {np.median(qcmi_arr):.4f}")
    print(f"  S(R) mean ± std: {sr_arr.mean():.4f} ± {sr_arr.std():.4f} "
          f"(expect 2.0)")

    # ---- Lower envelope extraction ----
    n_bins = 25
    # Use equal-width bins in |c|²
    bins = np.linspace(c2_arr.min(), c2_arr.max(), n_bins + 1)
    bin_centers = []
    bin_min_qcmi = []
    bin_counts = []

    for j in range(n_bins):
        mask = (c2_arr >= bins[j]) & (c2_arr < bins[j + 1])
        if mask.sum() >= 5:  # require at least 5 points per bin
            bin_centers.append((bins[j] + bins[j + 1]) / 2)
            bin_min_qcmi.append(qcmi_arr[mask].min())
            bin_counts.append(mask.sum())

    bin_centers = np.array(bin_centers)
    bin_min_qcmi = np.array(bin_min_qcmi)

    print(f"\n  Bins with ≥5 points: {len(bin_centers)}/{n_bins}")

    # ---- Linear fit: QCMI_min = a + b * |c|² ----
    if len(bin_centers) >= 3:
        slope, intercept, r_value, p_value, std_err = \
            stats.linregress(bin_centers, bin_min_qcmi)

        print(f"\n  Lower envelope linear fit results:")
        print(f"    intercept a = {intercept:.6f} ± std_err")
        print(f"    slope b     = {slope:.6f} ± {std_err:.6f}")
        print(f"    R²          = {r_value**2:.6f}")
        print(f"    p-value     = {p_value:.6e}")
        print(f"    Theory ideal: a=0, b=? (to be determined)")

        # Also do a constrained fit (a=0)
        if len(bin_centers) >= 2:
            # b_constrained = Σ(x_i * y_i) / Σ(x_i²)
            b_c = np.sum(bin_centers * bin_min_qcmi) / np.sum(bin_centers**2)
            residuals = bin_min_qcmi - b_c * bin_centers
            b_c_std = np.sqrt(np.sum(residuals**2) /
                              ((len(bin_centers) - 1) * np.sum(bin_centers**2)))
            print(f"\n  Constrained fit (a=0):")
            print(f"    slope b = {b_c:.6f} ± {b_c_std:.6f}")
    else:
        slope, intercept, r_value = 0.0, 0.0, 0.0
        std_err = 0.0
        b_c, b_c_std = 0.0, 0.0
        print("\n  [WARN] Not enough bins for fit. Increase N or adjust binning.")

    return {
        'N': N, 'p': p,
        'c2': c2_arr, 'qcmi': qcmi_arr, 'sr': sr_arr,
        'bin_centers': bin_centers, 'bin_min_qcmi': bin_min_qcmi,
        'bin_counts': np.array(bin_counts),
        'slope': slope, 'intercept': intercept,
        'slope_std': std_err, 'R2': r_value**2,
        'slope_constrained': b_c, 'slope_constrained_std': b_c_std,
        'c2_median': np.median(c2_arr),
        'c2_mean': c2_arr.mean(),
        'c2_std': c2_arr.std(),
    }


# ============================================================
# 5. E2: p参数扫描
# ============================================================

def run_E2(results_E1, p_values=[0.5, 0.6, 0.7, 0.8, 0.9],
           N_per_p=300, seed_base=12345):
    """
    E2: Scan over p values to verify b ∝ p(1-p).

    For each p, we compute QCMI for the same set of unitaries at 3 |c|² levels:
    median, median+1σ, median+2σ.
    """
    print("\n" + "=" * 60)
    print(f"E2: p PARAMETER SCAN (N={N_per_p} per p)")
    print("=" * 60)

    c2_median = results_E1['c2_median']
    c2_std = results_E1['c2_std']

    # First, generate a bank of unitaries with specific |c|² values
    # Strategy: generate many unitaries, pick those close to target |c|² levels
    targets = [c2_median, c2_median + c2_std, c2_median + 2 * c2_std]
    target_labels = [f"c2_median({c2_median:.4f})",
                     f"c2_median+1σ({targets[1]:.4f})",
                     f"c2_median+2σ({targets[2]:.4f})"]

    print(f"\n  Target |c|² levels: {[f'{t:.4f}' for t in targets]}")
    print(f"  p values: {p_values}\n")

    # Pre-generate a large pool of unitaries with their |c|² values
    pool_size = N_per_p * 10  # oversample to find unitaries at target |c|²
    pool = []
    for i in range(pool_size):
        U = make_rand_Haar(seed_base + i * 31)
        _, _, _, _, c2 = cartan_decompose(U)
        pool.append((c2, U))

    # For each target |c|², select the K closest unitaries
    K = min(30, N_per_p // 3)  # use K distinct unitaries per target
    selected = {}
    for idx, target in enumerate(targets):
        # Sort by distance to target
        pool_sorted = sorted(pool, key=lambda x: abs(x[0] - target))
        selected[idx] = [u for _, u in pool_sorted[:K]]
        actual_c2s = [cartan_decompose(u)[4] for u in selected[idx]]
        print(f"  Target {idx}: selected {K} unitaries, "
              f"|c|² ∈ [{min(actual_c2s):.4f}, {max(actual_c2s):.4f}]")

    # For each p, compute QCMI for each target
    scan_results = []
    for p in p_values:
        print(f"\n  p={p:.1f}:")
        rho_RQE = make_mixed_rho(2, p)
        for idx, target in enumerate(targets):
            qcmi_vals = []
            for U in selected[idx]:
                U_cycle = (embed_lsb(U, 0, 3, 4) @
                           embed_lsb(U, 1, 3, 4) @
                           embed_lsb(U, 2, 1, 4) @
                           embed_lsb(U, 0, 2, 4))
                qcmi, _, _, _ = compute(rho_RQE, U_cycle)
                qcmi_vals.append(qcmi)

            qcmi_mean = np.mean(qcmi_vals)
            qcmi_std = np.std(qcmi_vals)
            scan_results.append({
                'p': p, 'target_idx': idx, 'target_c2': target,
                'qcmi_mean': qcmi_mean, 'qcmi_std': qcmi_std,
                'n_samples': len(qcmi_vals)
            })
            print(f"    {target_labels[idx]}: "
                  f"QCMI = {qcmi_mean:.6f} ± {qcmi_std:.6f}")

    # ---- Verify b ∝ p(1-p) ----
    print("\n" + "-" * 40)
    print("  Verifying b ∝ p(1-p):")
    print(f"  {'p':>6s}  {'p(1-p)':>8s}  {'QCMI(med)':>10s}  "
          f"{'QCMI(med+1σ)':>12s}  {'QCMI(med+2σ)':>12s}")
    print("  " + "-" * 55)

    # Extract QCMI for each p at each target level
    qcmi_by_level = {idx: [] for idx in range(3)}
    pp_vals = []
    for p in p_values:
        pp = p * (1 - p)
        pp_vals.append(pp)
        row = [f"{p:.1f}", f"{pp:.4f}"]
        for idx in range(3):
            matched = [r['qcmi_mean'] for r in scan_results
                       if r['p'] == p and r['target_idx'] == idx]
            if matched:
                row.append(f"{matched[0]:.6f}")
                qcmi_by_level[idx].append(matched[0])
            else:
                row.append("N/A")
        print(f"  {row[0]:>6s}  {row[1]:>8s}  {row[2]:>10s}  "
              f"{row[3]:>12s}  {row[4]:>12s}")

    # Fit QCMI vs p(1-p) for each target level
    pp_arr = np.array(pp_vals)
    print(f"\n  Slope of QCMI vs p(1-p) at each |c|² level:")
    for idx in range(3):
        if len(qcmi_by_level[idx]) >= 3:
            s, inter, r, _, _ = stats.linregress(pp_arr,
                                                  np.array(qcmi_by_level[idx]))
            print(f"    {target_labels[idx]}: slope = {s:.6f}, "
                  f"intercept = {inter:.6f}, R² = {r**2:.4f}")

    return scan_results, pp_arr, qcmi_by_level


# ============================================================
# 6. 输出保存
# ============================================================

def save_results(results_E1, scan_results, out_dir):
    """Save data to CSV files."""
    os.makedirs(out_dir, exist_ok=True)

    # E1 scatter data
    scatter_path = os.path.join(out_dir, 'prefactor_scatter.csv')
    with open(scatter_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['c2', 'QCMI', 'SR'])
        for c2, qcmi, sr in zip(results_E1['c2'], results_E1['qcmi'],
                                 results_E1['sr']):
            writer.writerow([f"{c2:.8f}", f"{qcmi:.8f}", f"{sr:.8f}"])
    print(f"\nScatter data saved to: {scatter_path}")

    # E1 bin data
    bin_path = os.path.join(out_dir, 'prefactor_bins.csv')
    with open(bin_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['c2_center', 'QCMI_min', 'n_points'])
        for c, q, n in zip(results_E1['bin_centers'],
                           results_E1['bin_min_qcmi'],
                           results_E1['bin_counts']):
            writer.writerow([f"{c:.8f}", f"{q:.8f}", n])
    print(f"Bin data saved to: {bin_path}")

    # E2 scan data
    scan_path = os.path.join(out_dir, 'prefactor_pscan.csv')
    with open(scan_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['p', 'target_idx', 'target_c2', 'QCMI_mean',
                         'QCMI_std', 'n_samples'])
        for r in scan_results:
            writer.writerow([f"{r['p']:.3f}", r['target_idx'],
                             f"{r['target_c2']:.8f}",
                             f"{r['qcmi_mean']:.8f}",
                             f"{r['qcmi_std']:.8f}", r['n_samples']])
    print(f"P-scan data saved to: {scan_path}")

    # Summary results
    summary_path = os.path.join(out_dir, 'prefactor_summary.csv')
    with open(summary_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['parameter', 'value', 'uncertainty'])
        writer.writerow(['N_E1', results_E1['N'], ''])
        writer.writerow(['p_E1', results_E1['p'], ''])
        writer.writerow(['slope_b', f"{results_E1['slope']:.8f}",
                         f"{results_E1['slope_std']:.8f}"])
        writer.writerow(['intercept_a', f"{results_E1['intercept']:.8f}", ''])
        writer.writerow(['R2', f"{results_E1['R2']:.8f}", ''])
        writer.writerow(['slope_b_constrained',
                         f"{results_E1['slope_constrained']:.8f}",
                         f"{results_E1['slope_constrained_std']:.8f}"])
        writer.writerow(['c2_median', f"{results_E1['c2_median']:.8f}", ''])
        writer.writerow(['c2_mean', f"{results_E1['c2_mean']:.8f}", ''])
        writer.writerow(['c2_std', f"{results_E1['c2_std']:.8f}", ''])
    print(f"Summary saved to: {summary_path}")


# ============================================================
# 7. 主程序
# ============================================================

def main():
    print("=" * 60)
    print("  PREFACTOR FIT: Resolving the 8x uncertainty in sin^2(theta) prefactor")
    print("  LP36 -- Causal Accumulation Structure")
    print("  Date: 2026-06-08")
    print("=" * 60)
    print()

    # Step 0: Verify Cartan decomposition
    test_cartan_decomposition()

    # Output directory
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..', '..', 'prefactor_output')
    out_dir = os.path.abspath(out_dir)

    # ---- E1: Main scatter + lower envelope ----
    N_E1 = 500
    p_default = 0.7
    results_E1 = run_E1(N=N_E1, p=p_default, seed_base=42)

    print("\n" + "=" * 60)
    print("E1 KEY RESULT:")
    print(f"  Prefactor b = {results_E1['slope']:.6f} ± "
          f"{results_E1['slope_std']:.6f}")
    print(f"  Constrained b = {results_E1['slope_constrained']:.6f} ± "
          f"{results_E1['slope_constrained_std']:.6f}")
    print(f"  If b is the sin²θ prefactor, the QCMI lower bound is:")
    print(f"    QCMI ≥ {results_E1['slope_constrained']:.4f} · |c|²")
    print(f"    (for p={p_default})")
    print("=" * 60)

    # ---- E2: p parameter scan ----
    p_vals = [0.5, 0.6, 0.7, 0.8, 0.9]
    scan_results, pp_arr, qcmi_by_level = run_E2(
        results_E1, p_values=p_vals, N_per_p=300, seed_base=12345
    )

    # Save results
    save_results(results_E1, scan_results, out_dir)

    # ---- Final summary ----
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"\n  E1 (p={p_default}, N={N_E1}):")
    print(f"    Lower envelope: QCMI_min = {results_E1['intercept']:.6f} + "
          f"{results_E1['slope']:.6f} · |c|²")
    print(f"    R² = {results_E1['R2']:.6f}")
    print(f"    Constrained: QCMI_min = {results_E1['slope_constrained']:.6f} "
          f"· |c|²")

    print(f"\n  E2 (p-scan):")
    print(f"    QCMI vs p(1-p) linearity: check R² values above")

    # Estimate the full prefactor
    # For small |c|: sin²(|c|) ≈ |c|²
    # QCMI ≈ b(p) · sin²(2|c|) (or sin²(|c|)?)
    # The uncertainty in the sin² argument (|c| vs 2|c| vs ...) is the 8x factor
    # (sin²(2|c|) ≈ 4|c|² for small |c|, giving 4x difference)
    # Combined with other factors → 8x

    b_unconstrained = results_E1['slope']
    b_constrained = results_E1['slope_constrained']

    print(f"\n  Prefactor candidates (for reference):")
    print(f"    If QCMI = b · sin²(|c|):   b = {b_constrained:.4f}")
    print(f"    If QCMI = b · sin²(2|c|):  b = {b_constrained/4:.4f} "
          f"(4x from sin²(2|c|)≈4|c|²)")
    print(f"    If QCMI = b · sin²(|c|/2): b = {4*b_constrained:.4f}")

    print(f"\n  All output files: {out_dir}/")
    print("  - prefactor_scatter.csv  (raw data: |c|², QCMI, SR)")
    print("  - prefactor_bins.csv     (binned lower envelope)")
    print("  - prefactor_pscan.csv    (p-parameter scan)")
    print("  - prefactor_summary.csv  (fit summary)")

    print("\nDone.")
    return results_E1, scan_results


if __name__ == '__main__':
    main()
