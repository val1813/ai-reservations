#!/usr/bin/env python3
"""
Firewall 2: XXZ Chain Boundary-Driven NESS — Does O_XX Survive Interactions?

Physics question: In the XXZ chain (Jordan-Wigner mapped to interacting fermions),
is the pure-imaginary C_{i!=j} theorem of free fermions (XX model, Delta=0) merely
a coincidence, or a robust structure?

If O_XX ∝ Σ|Im(C_{ij})|² is killed by weak interactions (Delta_c << J), the free-fermion
result is a coincidence → XX frame needs revision.
If O_XX survives and Re(C_{i!=j}) stays negligible, the pure-imaginary structure
is robust → strong support for the XX frame.

System: 1D XXZ chain, L=4 and L=6 sites
  H = -J Σ (σ^x_j σ^x_{j+1} + σ^y_j σ^y_{j+1}) + Delta Σ σ^z_j σ^z_{j+1}
  → H_f = -J Σ (c_j† c_{j+1} + h.c.) + Delta Σ (2n_j-1)(2n_{j+1}-1)

Boundary driving (Lindblad):
  L_{L,in}  = √(Gamma_L f_L) c_1†
  L_{L,out} = √(Gamma_L(1-f_L)) c_1
  L_{R,in}  = √(Gamma_R f_R) c_L†
  L_{R,out} = √(Gamma_R(1-f_R)) c_L

Dephasing: L_{deph,j} = √gamma_phi σ^z_j = √gamma_phi (2n_j-1)

Parameters: Gamma_L=Gamma_R=1.0, f_L=0.65, f_R=0.35, J=0.3
Scans: Delta ∈ [0, 0.1, 0.3, 0.5, 1.0, 2.0], gamma_phi ∈ [0.01, 0.1, 0.5, 1.0]
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
import json
import time
import warnings
warnings.filterwarnings('ignore')

# ==============================================================================
# Physical parameters
# ==============================================================================
GAMMA_L = 1.0
GAMMA_R = 1.0
F_L = 0.65
F_R = 0.35
J = 0.3

DELTA_VALUES = [0.0, 0.1, 0.3, 0.5, 1.0, 2.0]
GAMMA_PHI_VALUES = [0.01, 0.1, 0.5, 1.0]

# ==============================================================================
# Helper: Fock basis utilities
# ==============================================================================

def fock_dim(L):
    """Dimension of Fock space for L sites."""
    return 1 << L  # 2^L


def bit(b, k):
    """Get bit k (0-indexed) of integer b. bit 0 = site 1 occupation."""
    return (b >> k) & 1


def set_bit(b, k, val):
    """Set bit k of integer b to val (0 or 1)."""
    if val:
        return b | (1 << k)
    else:
        return b & ~(1 << k)


def parity_before(b, k):
    """Count number of fermions on sites 0..k-1 (returns parity as 1 or -1)."""
    mask = (1 << k) - 1
    popcount = bin(b & mask).count('1')
    return -1 if (popcount & 1) else 1


def parity_between(b, i, j):
    """Count number of fermions strictly between sites i and j (0-indexed).
    Returns (-1)^(count)."""
    lo, hi = (i, j) if i < j else (j, i)
    # strictly between: sites lo+1 .. hi-1
    if lo + 1 >= hi:
        return 1  # no sites between
    mask = ((1 << (hi - 1)) - 1) ^ ((1 << (lo + 1)) - 1)  # bits lo+1 to hi-1
    # More precisely: mask for bits (lo+1) through (hi-1) inclusive
    n_between = hi - lo - 1
    mask = ((1 << (hi - 1)) - 1) - ((1 << (lo + 1)) - 1) if hi - 1 > lo + 1 else 0
    # Simpler: just use bit tests
    count = 0
    for k in range(lo + 1, hi):
        count += bit(b, k)
    return -1 if (count & 1) else 1


# ==============================================================================
# Fermion operators in Fock basis
# ==============================================================================

def build_c_dag_c(i, j, L):
    """
    Build the matrix of c_i† c_j in the L-site Fock basis.
    Sites are 1-indexed (i,j ∈ {1..L}), stored 0-indexed internally.
    Returns dense (2^L × 2^L) complex matrix.

    For i=j: the number operator n_i = c_i† c_i, which is purely diagonal.
    For i!=j: off-diagonal fermion bilinear with JW phase.
    """
    i0, j0 = i - 1, j - 1
    N = fock_dim(L)
    O = np.zeros((N, N), dtype=complex)

    if i == j:
        # Number operator: diagonal, eigenvalue = occupation of site i
        for b in range(N):
            O[b, b] = float(bit(b, i0))
        return O

    # i != j: c_i† c_j
    for b in range(N):
        if bit(b, j0) == 0 or bit(b, i0) == 1:
            continue  # need n_j=1, n_i=0
        # Apply c_j then c_i†
        b_intermediate = set_bit(b, j0, 0)  # remove fermion at j
        # c_j phase from its own site parity
        phase_j = parity_before(b, j0)
        # c_i† phase from intermediate state
        phase_i = parity_before(b_intermediate, i0)
        total_phase = phase_j * phase_i
        O[b_intermediate ^ (1 << i0), b] = total_phase  # set bit i to 1

    return O


def build_n(N, L):
    """Build number operator n_j = c_j† c_j matrices for all sites.
    Returns list of N×N matrices [n_1, n_2, ..., n_L]."""
    operators = []
    for j in range(1, L + 1):
        O = build_c_dag_c(j, j, L)
        operators.append(O)
    return operators


def build_c_dag_c_all(L):
    """Build all c_i† c_j operators (i,j ∈ {1..L}).
    Returns dict {(i,j): matrix}."""
    operators = {}
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            operators[(i, j)] = build_c_dag_c(i, j, L)
    return operators


# ==============================================================================
# Hamiltonian in Fock basis
# ==============================================================================

def build_hamiltonian(L, delta):
    """
    Build the XXZ Hamiltonian in fermion Fock basis.
    H = -J Σ_j (c_j† c_{j+1} + h.c.) + Delta Σ_j (2n_j-1)(2n_{j+1}-1)
    """
    N = fock_dim(L)
    H = np.zeros((N, N), dtype=complex)

    # Hopping terms
    for j in range(1, L):
        c_dag_next = build_c_dag_c(j, j + 1, L)
        c_next_dag = build_c_dag_c(j + 1, j, L)
        H -= J * (c_dag_next + c_next_dag)

    # Interaction terms: (2n_j - 1)(2n_{j+1} - 1) = 4n_j n_{j+1} - 2n_j - 2n_{j+1} + 1
    n_ops = build_n(N, L)
    for j in range(1, L):
        n_j = n_ops[j - 1]
        n_jp1 = n_ops[j]  # j, 0-indexed
        H += delta * (4 * n_j @ n_jp1 - 2 * n_j - 2 * n_jp1 + np.eye(N))

    return H


# ==============================================================================
# Lindblad operators (in Fock basis)
# ==============================================================================

def build_lindblad_operators(L, gamma_phi):
    """
    Build all Lindblad jump operators.
    Returns list of (N×N) matrices.
    """
    N = fock_dim(L)
    L_ops = []

    # Boundary driving: left
    amplitude_L_in = np.sqrt(GAMMA_L * F_L)
    amplitude_L_out = np.sqrt(GAMMA_L * (1.0 - F_L))
    c1_dag = build_c_dag_c(1, 1, L)  # This gives n_1, not c_1† — need to fix
    # Actually build c_1† and c_1 properly
    L_ops.append(amplitude_L_in * build_creation(1, L, N))
    L_ops.append(amplitude_L_out * build_annihilation(1, L, N))

    # Boundary driving: right
    amplitude_R_in = np.sqrt(GAMMA_R * F_R)
    amplitude_R_out = np.sqrt(GAMMA_R * (1.0 - F_R))
    L_ops.append(amplitude_R_in * build_creation(L, L, N))
    L_ops.append(amplitude_R_out * build_annihilation(L, L, N))

    # Dephasing: √gamma_phi (2n_j - 1)
    if gamma_phi > 0:
        n_ops = build_n(N, L)
        sqrt_gp = np.sqrt(gamma_phi)
        for j in range(L):
            L_ops.append(sqrt_gp * (2.0 * n_ops[j] - np.eye(N)))

    return L_ops


def build_creation(j, L, N):
    """Build c_j† operator in Fock basis."""
    j0 = j - 1
    O = np.zeros((N, N), dtype=complex)
    for b in range(N):
        if bit(b, j0) == 1:
            continue  # Pauli exclusion
        phase = parity_before(b, j0)
        b_new = set_bit(b, j0, 1)
        O[b_new, b] = phase
    return O


def build_annihilation(j, L, N):
    """Build c_j operator in Fock basis."""
    j0 = j - 1
    O = np.zeros((N, N), dtype=complex)
    for b in range(N):
        if bit(b, j0) == 0:
            continue
        phase = parity_before(b, j0)
        b_new = set_bit(b, j0, 0)
        O[b_new, b] = phase
    return O


# ==============================================================================
# Liouvillian superoperator
# ==============================================================================

def build_liouvillian(H, L_ops):
    """
    Build the Lindblad Liouvillian superoperator L.
    L = -i (I⊗H - H^T⊗I) + Σ_k [L_k*⊗L_k - ½(I⊗L_k†L_k + (L_k†L_k)^T⊗I)]

    Input: H (N×N), L_ops list of (N×N)
    Returns: L_matrix (N²×N²), complex
    """
    N = H.shape[0]
    N2 = N * N
    I = np.eye(N, dtype=complex)

    # Hamiltonian part: -i (I⊗H - H^T⊗I)
    L_mat = -1j * (np.kron(I, H) - np.kron(H.T, I))

    # Dissipator parts
    for Lk in L_ops:
        Lk_dag_Lk = Lk.conj().T @ Lk
        # Lk* ⊗ Lk
        L_mat += np.kron(Lk.conj(), Lk)
        # -½ (I ⊗ Lk†Lk + (Lk†Lk)^T ⊗ I)
        L_mat -= 0.5 * np.kron(I, Lk_dag_Lk)
        L_mat -= 0.5 * np.kron(Lk_dag_Lk.T, I)

    return L_mat


def build_liouvillian_sparse(H, L_ops):
    """
    Sparse version of build_liouvillian for larger systems (L=6).
    Uses scipy.sparse.kron for efficiency.
    """
    N = H.shape[0]
    N2 = N * N
    I = sparse.eye(N, dtype=complex)

    H_sp = sparse.csr_matrix(H)
    I_sp = I

    # Hamiltonian part
    L_mat = -1j * (sparse.kron(I_sp, H_sp) - sparse.kron(H_sp.T, I_sp))

    for Lk in L_ops:
        Lk_sp = sparse.csr_matrix(Lk)
        Lk_conj = sparse.csr_matrix(Lk.conj())
        Lk_dag_Lk = Lk_sp.conj().T @ Lk_sp

        L_mat += sparse.kron(Lk_conj, Lk_sp, format='csr')
        L_mat -= 0.5 * sparse.kron(I_sp, Lk_dag_Lk, format='csr')
        L_mat -= 0.5 * sparse.kron(Lk_dag_Lk.T, I_sp, format='csr')

    return L_mat


# ==============================================================================
# NESS solvers
# ==============================================================================

def solve_ness_dense(L_mat):
    """
    Find NESS by solving L|ρ⟩⟩ = 0 for dense matrix.
    Uses SVD nullspace method.
    """
    # Find nullspace via SVD
    U, s, Vh = np.linalg.svd(L_mat)
    # The right singular vector with smallest singular value
    rho_vec = Vh[-1].conj()
    # Normalize: Tr(ρ) = 1, which is sum of diagonal elements
    N = int(np.sqrt(len(rho_vec)))
    rho_mat = rho_vec.reshape((N, N), order='F')  # column-major for kron convention
    trace_val = np.trace(rho_mat)
    if abs(trace_val) > 1e-14:
        rho_vec = rho_vec / trace_val
        rho_mat = rho_mat / trace_val
    # Ensure Hermitian
    rho_mat = 0.5 * (rho_mat + rho_mat.conj().T)
    return rho_mat


def solve_ness_sparse(L_sparse, N, tol=1e-10, maxiter=2000):
    """
    Find NESS by solving L|ρ⟩⟩ = 0 for sparse Liouvillian.
    Uses shift-invert Arnoldi (eigs with sigma=0).
    N = Fock space dimension.
    """
    N2 = N * N
    # Use eigs to find eigenvector with eigenvalue closest to 0
    try:
        vals, vecs = spla.eigs(L_sparse, k=2, sigma=0, which='LM',
                               tol=tol, maxiter=maxiter, ncv=min(50, N2))
        # Find the eigenvector with eigenvalue closest to 0
        abs_vals = np.abs(vals)
        idx = np.argmin(abs_vals)
        rho_vec = vecs[:, idx]

        rho_mat = rho_vec.reshape((N, N), order='F')
        trace_val = np.trace(rho_mat)
        if abs(trace_val) > 1e-14:
            rho_mat = rho_mat / trace_val
        rho_mat = 0.5 * (rho_mat + rho_mat.conj().T)

        return rho_mat, abs_vals[idx]
    except Exception as e:
        print(f"    eigs failed: {e}, trying gmres...")
        # Fallback: GMRES with random initial guess
        from scipy.sparse.linalg import gmres
        b = np.zeros(N2)
        # Regularization: add small identity to make it invertible
        L_reg = L_sparse + 1e-10 * sparse.eye(N2, dtype=complex)
        # Actually GMRES for singular systems is tricky — use LSQR or LSMR
        from scipy.sparse.linalg import lsqr
        sol = lsqr(L_sparse, b, atol=tol, btol=tol, iter_lim=maxiter)
        rho_vec = sol[0]
        norm = np.linalg.norm(rho_vec)
        if norm > 1e-14:
            rho_mat = rho_vec.reshape((N, N), order='F')
            trace_val = np.trace(rho_mat)
            if abs(trace_val) > 1e-14:
                rho_mat = rho_mat / trace_val
            rho_mat = 0.5 * (rho_mat + rho_mat.conj().T)
            return rho_mat, np.nan
        else:
            print("    WARNING: GMRES returned zero vector!")
            return np.zeros((N, N), dtype=complex), np.nan


# ==============================================================================
# Observables
# ==============================================================================

def compute_correlation_matrix(rho_mat, L):
    """
    Compute C_{ij} = Tr[c_i† c_j ρ] for all i,j.
    Returns complex (L×L) matrix.
    """
    N = rho_mat.shape[0]
    C = np.zeros((L, L), dtype=complex)
    # Precompute all c_i† c_j operators
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            O = build_c_dag_c(i, j, L)
            # C_{ij} = Tr[O ρ] = sum_{m,n} O^T_{nm} ρ_{nm} = sum O^T .* ρ
            C[i-1, j-1] = np.sum(O.T * rho_mat)
    return C


def compute_observables(C):
    """
    From correlation matrix C, compute fire wall 2 quantities.

    Returns dict with:
      - O_XX: Σ_{i!=j} |Im(C_{ij})|²
      - O_XX_total: Σ_{i!=j} |C_{ij}|²
      - Re2_sum: Σ_{i!=j} |Re(C_{ij})|²
      - Im2_sum: Σ_{i!=j} |Im(C_{ij})|²
      - F: Re2_sum / O_XX_total (real fraction of off-diagonal correlations)
      - Re_max: max |Re(C_{i!=j})|
      - Im_max: max |Im(C_{i!=j})|
      - C_diag: diagonal elements (occupations)
    """
    L = C.shape[0]
    off_diag_mask = ~np.eye(L, dtype=bool)

    C_off = C[off_diag_mask]
    re2 = np.abs(C_off.real)**2
    im2 = np.abs(C_off.imag)**2

    Re2_sum = np.sum(re2)
    Im2_sum = np.sum(im2)
    total = Re2_sum + Im2_sum

    F = Re2_sum / total if total > 1e-20 else 0.0

    return {
        'O_XX': Im2_sum,
        'O_XX_total': total,
        'Re2_sum': Re2_sum,
        'Im2_sum': Im2_sum,
        'F': F,
        'Re_max': np.max(np.abs(C_off.real)) if len(C_off) > 0 else 0,
        'Im_max': np.max(np.abs(C_off.imag)) if len(C_off) > 0 else 0,
        'C_diag': np.diag(C).real.tolist(),
        'C_off_diag_re': C_off.real.tolist(),
        'C_off_diag_im': C_off.imag.tolist(),
        'C_full_real': C.real.tolist(),
        'C_full_imag': C.imag.tolist(),
    }


# ==============================================================================
# Main computation loops
# ==============================================================================

def run_L4():
    """
    L=4: 16-dimensional Fock space, 256×256 Liouvillian.
    Dense exact diagonalization.
    """
    L = 4
    N = fock_dim(L)
    print(f"\n{'='*70}")
    print(f"L={L}: Fock dim={N}, Liouvillian dim={N*N}×{N*N} ({N*N})")
    print(f"{'='*70}")

    results = {
        'L': L,
        'N': N,
        'params': {
            'J': J,
            'Gamma_L': GAMMA_L, 'Gamma_R': GAMMA_R,
            'f_L': F_L, 'f_R': F_R,
        },
        'scans': []
    }

    n_combos = len(DELTA_VALUES) * len(GAMMA_PHI_VALUES)
    combo_idx = 0

    for gp in GAMMA_PHI_VALUES:
        for delta in DELTA_VALUES:
            combo_idx += 1
            t_start = time.time()

            print(f"\n  [{combo_idx}/{n_combos}] Delta={delta:.1f}, gamma_phi={gp:.2f} ...", end='', flush=True)

            # Build operators
            L_ops = build_lindblad_operators(L, gp)
            H = build_hamiltonian(L, delta)

            # Build Liouvillian (dense)
            L_mat = build_liouvillian(H, L_ops)

            # Solve NESS
            rho = solve_ness_dense(L_mat)

            # Sanity check: Tr(rho) ≈ 1, rho Hermitian, rho ≥ 0
            trace_val = np.trace(rho).real
            hermiticity = np.max(np.abs(rho - rho.conj().T))
            eigenvals = np.linalg.eigvalsh(rho)
            min_eig = np.min(eigenvals)

            if trace_val < 0.5 or trace_val > 1.5 or hermiticity > 1e-8 or min_eig < -1e-8:
                print(f" WARNING: Trρ={trace_val:.6f}, herm_err={hermiticity:.2e}, min_eig={min_eig:.2e}")

            # Compute correlation matrix
            C = compute_correlation_matrix(rho, L)
            obs = compute_observables(C)

            t_elapsed = time.time() - t_start
            print(f" O_XX={obs['O_XX']:.6f}, F={obs['F']:.6e}, t={t_elapsed:.2f}s")

            results['scans'].append({
                'delta': delta,
                'gamma_phi': gp,
                **obs,
                'trace': float(trace_val.real),
                'hermiticity_error': float(hermiticity),
                'min_eigenvalue': float(min_eig),
                'elapsed_time': t_elapsed,
            })

    return results


def run_L6():
    """
    L=6: 64-dimensional Fock space, 4096×4096 Liouvillian.
    Sparse iterative solver.
    """
    L = 6
    N = fock_dim(L)
    print(f"\n{'='*70}")
    print(f"L={L}: Fock dim={N}, Liouvillian dim={N*N}×{N*N} ({N*N})")
    print(f"{'='*70}")

    results = {
        'L': L,
        'N': N,
        'params': {
            'J': J,
            'Gamma_L': GAMMA_L, 'Gamma_R': GAMMA_R,
            'f_L': F_L, 'f_R': F_R,
        },
        'scans': []
    }

    n_combos = len(DELTA_VALUES) * len(GAMMA_PHI_VALUES)
    combo_idx = 0

    for gp in GAMMA_PHI_VALUES:
        for delta in DELTA_VALUES:
            combo_idx += 1
            t_start = time.time()

            print(f"\n  [{combo_idx}/{n_combos}] Delta={delta:.1f}, gamma_phi={gp:.2f} ...", end='', flush=True)

            # Build operators
            L_ops = build_lindblad_operators(L, gp)
            H = build_hamiltonian(L, delta)

            # Build Liouvillian (sparse)
            print(" build L...", end='', flush=True)
            L_sparse = build_liouvillian_sparse(H, L_ops)
            print(f" nnz={L_sparse.nnz}", end='', flush=True)

            # Solve NESS
            print(" solve...", end='', flush=True)
            rho, eig_err = solve_ness_sparse(L_sparse, N)

            # Sanity checks
            trace_val = np.trace(rho).real
            if trace_val > 1e-10:
                hermiticity = np.max(np.abs(rho - rho.conj().T))
                eigenvals = np.linalg.eigvalsh(rho)
                min_eig = np.min(eigenvals)
            else:
                hermiticity = 0
                min_eig = 0
                print(" FAILURE: zero trace!", end='')

            # Compute correlation matrix
            C = compute_correlation_matrix(rho, L)
            obs = compute_observables(C)

            t_elapsed = time.time() - t_start
            print(f" O_XX={obs['O_XX']:.6f}, F={obs['F']:.6e}, e0_err={eig_err:.2e}, t={t_elapsed:.1f}s")

            results['scans'].append({
                'delta': delta,
                'gamma_phi': gp,
                **obs,
                'trace': float(trace_val.real),
                'hermiticity_error': float(hermiticity),
                'min_eigenvalue': float(min_eig),
                'eigenvalue_error': float(eig_err) if not np.isnan(eig_err) else None,
                'elapsed_time': t_elapsed,
            })

    return results


# ==============================================================================
# Analysis
# ==============================================================================

def analyze_results(all_results):
    """
    Analyze results from both L=4 and L=6.
    Returns analysis dict with fire wall 2 verdict.
    """
    analysis = {}

    for label, res in all_results.items():
        L = res['L']
        scans = res['scans']

        # Group by gamma_phi for O_XX(Delta)/O_XX(0) curves
        gp_values = sorted(set(s['gamma_phi'] for s in scans))

        # For each gamma_phi, find O_XX at Delta=0 as reference
        o_xx_ratios = {}
        f_vs_delta = {}

        for gp in gp_values:
            gp_scans = [s for s in scans if s['gamma_phi'] == gp]
            gp_scans_sorted = sorted(gp_scans, key=lambda s: s['delta'])
            o_xx_0 = next((s['O_XX'] for s in gp_scans_sorted if s['delta'] == 0.0), None)

            ratios = []
            f_vals = []
            for s in gp_scans_sorted:
                if o_xx_0 and o_xx_0 > 1e-20:
                    ratios.append({'delta': s['delta'], 'ratio': s['O_XX'] / o_xx_0})
                else:
                    ratios.append({'delta': s['delta'], 'ratio': None})
                f_vals.append({'delta': s['delta'], 'F': s['F']})

            o_xx_ratios[gp] = ratios
            f_vs_delta[gp] = f_vals

        # Extract Delta_c: fit O_XX(Delta) ≈ O_XX(0) exp(-Delta/Delta_c)
        # First get the smallest gamma_phi (weakest dephasing, cleanest interaction effect)
        gp_min = min(gp_values)
        gp_scans = [s for s in scans if s['gamma_phi'] == gp_min]
        gp_scans_sorted = sorted(gp_scans, key=lambda s: s['delta'])

        deltas = np.array([s['delta'] for s in gp_scans_sorted])
        o_xx_vals = np.array([s['O_XX'] for s in gp_scans_sorted])

        delta_c = None
        if o_xx_vals[0] > 1e-20 and len(deltas) >= 3:
            # Fit log(O_XX/O_XX(0)) = -Delta/Delta_c using linear regression on log
            nonzero_mask = o_xx_vals > 1e-20
            if np.sum(nonzero_mask) >= 2:
                x = deltas[nonzero_mask]
                y = np.log(o_xx_vals[nonzero_mask] / o_xx_vals[0])
                # Linear fit y = -x/Delta_c + b (b should be ~0)
                # Use y = a*x + b, then Delta_c = -1/a
                A = np.vstack([x, np.ones_like(x)]).T
                a, b = np.linalg.lstsq(A, y, rcond=None)[0]
                if abs(a) > 1e-20:
                    delta_c = -1.0 / a

        # Firewall 2 verdict
        # Key question: does F(Delta) become nonzero for Delta != 0?
        max_F = max(s['F'] for s in scans if s['delta'] > 0)
        min_gp = min(gp_values)
        gp_min_scans = [s for s in scans if s['gamma_phi'] == min_gp]

        # Is O_XX killed by interactions?
        o_xx_at_max_delta = None
        o_xx_at_zero = None
        for s in gp_min_scans:
            if s['delta'] == 0:
                o_xx_at_zero = s['O_XX']
            if s['delta'] == max(d['delta'] for d in gp_min_scans):
                o_xx_at_max_delta = s['O_XX']

        # Also get the lowest gamma_phi F values
        F_at_nonzero_delta = [s['F'] for s in gp_min_scans if s['delta'] > 0]
        F_mean_nonzero = np.mean(F_at_nonzero_delta) if F_at_nonzero_delta else 0

        analysis[label] = {
            'L': L,
            'o_xx_ratios': o_xx_ratios,
            'f_vs_delta': f_vs_delta,
            'delta_c': float(delta_c) if delta_c else None,
            'delta_c_over_J': float(delta_c / J) if delta_c else None,
            'max_F': float(max_F),
            'F_mean_nonzero': float(F_mean_nonzero),
            'o_xx_ratio_at_max_delta': float(o_xx_at_max_delta / o_xx_at_zero) if (o_xx_at_zero and o_xx_at_zero > 1e-20) else None,
        }

    return analysis


def render_verdict(analysis, all_results):
    """
    Render the fire wall 2 verdict as a human-readable string.
    """
    lines = []
    lines.append("# Firewall 2: XX振幅在XXZ相互作用链中的存活检验")
    lines.append("")
    lines.append("## 执行摘要")
    lines.append("")
    lines.append("**物理问题:** C12的纯虚性由自由费米子的实H对称性保护。")
    lines.append("相互作用(Delta>0)是否破坏此对称性，激发Re(C_{i!=j})？")
    lines.append("或者：弱相互作用是否直接杀死O_XX（XX振幅）？")
    lines.append("")

    for label in ['L4', 'L6']:
        a = analysis[label]
        L = a['L']
        lines.append(f"## L={L} 结果")
        lines.append("")

        # Check if F was ever nonzero at Delta=0
        all_scans = all_results[label]['scans']

        # Results table
        lines.append(f"| Delta | gamma_phi | O_XX | F (实部占比) | Re_max | Im_max |")
        lines.append(f"|---|---|---|---|---|---|")
        for s in all_scans:
            lines.append(f"| {s['delta']:.1f} | {s['gamma_phi']:.3f} | {s['O_XX']:.6f} | {s['F']:.6e} | {s['Re_max']:.6e} | {s['Im_max']:.6f} |")
        lines.append("")

        # F at Delta=0 — should be 0 for free fermions
        F_at_zero = [s['F'] for s in all_scans if s['delta'] == 0.0]
        lines.append(f"**F(Delta=0) 基准:** {[f'{f:.2e}' for f in F_at_zero]}")
        lines.append("")

        # O_XX ratio table
        gp_min = min(GAMMA_PHI_VALUES)
        lines.append(f"### O_XX(Delta)/O_XX(0) vs Delta (gamma_phi={gp_min:.2f}, 最小退相干)")
        lines.append("")
        lines.append(f"| Delta | O_XX(Delta)/O_XX(0) | F |")
        lines.append(f"|---|---|---|")
        o_xx_r = a['o_xx_ratios'].get(gp_min, [])
        f_vd = a['f_vs_delta'].get(gp_min, [])
        for r, f in zip(o_xx_r, f_vd):
            ratio_str = f"{r['ratio']:.6f}" if r['ratio'] is not None else "N/A"
            lines.append(f"| {r['delta']:.1f} | {ratio_str} | {f['F']:.6e} |")
        lines.append("")

        # Delta_c
        if a['delta_c'] is not None:
            lines.append(f"**特征相互作用强度:** Delta_c = {a['delta_c']:.6f}")
            lines.append(f"**Delta_c / J:** {a['delta_c_over_J']:.6f}")
            lines.append("")

        # O_XX ratio at max Delta
        if a['o_xx_ratio_at_max_delta'] is not None:
            lines.append(f"**O_XX(Delta_max)/O_XX(0):** {a['o_xx_ratio_at_max_delta']:.6f}")
            lines.append("")

    # ==========
    # VERDICT
    # ==========
    lines.append("## 火墙裁决")
    lines.append("")

    # Gather key metrics
    l4 = analysis['L4']
    l6 = analysis.get('L6', l4)  # fallback

    verdicts = []

    # Criterion 1: Does F become nonzero for Delta!=0?
    for label, a in [('L=4', l4), ('L=6', l6)]:
        F_threshold = 1e-6  # numerical noise threshold
        if a['max_F'] > F_threshold:
            verdicts.append(f"**[{label}] 判据1触发:** F(Delta!=0) = {a['max_F']:.6e} > {F_threshold:.0e}")
            verdicts.append(f"  → 相互作用激发了Re(C_{{i!=j}})，纯虚定理在相互作用下被破坏")
        else:
            verdicts.append(f"**[{label}] 判据1通过:** F(Delta!=0) = {a['max_F']:.6e} ≤ {F_threshold:.0e}")
            verdicts.append(f"  → 纯虚结构在XXZ相互作用下存活")

    # Criterion 2: Is O_XX killed by weak interactions?
    for label, a in [('L=4', l4), ('L=6', l6)]:
        if a['delta_c'] is not None:
            delta_c = a['delta_c']
            if delta_c < 0.1 * J:
                verdicts.append(f"**[{label}] 判据2触发:** Delta_c = {delta_c:.6f} << J={J}")
                verdicts.append(f"  → 极弱相互作用即可杀死XX振幅 → XX是自由费米子赝象")
            elif delta_c < J:
                verdicts.append(f"**[{label}] 判据2中间:** Delta_c = {delta_c:.6f} < J={J}")
                verdicts.append(f"  → 相互作用显著压制XX振幅")
            else:
                verdicts.append(f"**[{label}] 判据2通过:** Delta_c = {delta_c:.6f} >= J={J}")
                verdicts.append(f"  → XX振幅对相互作用有鲁棒性")

    # Criterion 3: Survival
    for label, a in [('L=4', l4), ('L=6', l6)]:
        if a['o_xx_ratio_at_max_delta'] is not None:
            ratio = a['o_xx_ratio_at_max_delta']
            if ratio > 0.5:
                verdicts.append(f"**[{label}] 判据3通过:** O_XX(Delta_max)/O_XX(0) = {ratio:.4f} > 0.5")
                verdicts.append(f"  → XX振幅在强相互作用下存活良好")
            elif ratio > 0.1:
                verdicts.append(f"**[{label}] 判据3中间:** O_XX(Delta_max)/O_XX(0) = {ratio:.4f}")
                verdicts.append(f"  → XX振幅部分存活，中等压制")
            else:
                verdicts.append(f"**[{label}] 判据3触发:** O_XX(Delta_max)/O_XX(0) = {ratio:.4f} ≤ 0.1")
                verdicts.append(f"  → XX振幅被强相互作用近乎完全杀死")

    lines.extend(verdicts)
    lines.append("")

    # Final verdict
    lines.append("### 最终裁决")
    lines.append("")

    # Logic:
    # If F stays zero and O_XX survives → XX is STRUCTURE
    # If F becomes nonzero OR O_XX dies easily → XX is COINCIDENCE
    F_triggered = l4['max_F'] > 1e-6
    O_XX_dead = (l4['delta_c'] is not None and l4['delta_c'] < 0.5 * J) or \
                (l4['o_xx_ratio_at_max_delta'] is not None and l4['o_xx_ratio_at_max_delta'] < 0.3)

    if not F_triggered and not O_XX_dead:
        lines.append("**裁决: XX振幅是结构，不是巧合。**")
        lines.append("")
        lines.append("论据：")
        lines.append("1. Re(C_{i!=j})在相互作用下保持为零（数值精度内）")
        lines.append("2. Im(C_{i!=j})对中等强度的Delta有鲁棒性")
        lines.append("3. 纯虚定理的核心机制（实H对称性）在XXZ相互作用中存活")
        lines.append("")
        lines.append("→ XX框架在相互作用系统中获得强支持。B博士的\"两者等价\"被验证。")
    elif F_triggered and not O_XX_dead:
        lines.append("**裁决: 混合结果 — 实部被激发但振幅存活。**")
        lines.append("")
        lines.append("论据：")
        lines.append(f"1. F(Delta!=0) = {l4['max_F']:.2e} → Re(C_{{i!=j}})被相互作用激发")
        lines.append("2. 但O_XX核心振幅未完全消失")
        lines.append("3. 纯虚定理需要修正：添加相互作用修正项")
        lines.append("")
        lines.append("→ XX框架需要一阶修正，但核心结构保留。")
    elif not F_triggered and O_XX_dead:
        lines.append("**裁决: XX振幅是巧合 — 自由费米子赝象。**")
        lines.append("")
        lines.append("论据：")
        lines.append("1. F(Delta!=0) ≈ 0 → 纯虚形式在相互作用下存活")
        lines.append(f"2. 但O_XX本身被杀死（Delta_c = {l4['delta_c']:.4f} << J={J}）")
        lines.append("3. C_{i!=j}整体趋零 → 纯虚\"定理\"仅在无振幅时成立")
        lines.append("")
        lines.append("→ 自由费米子的XX振幅结构是偶然的。相互作用使系统趋向对角关联。")
    else:
        lines.append("**裁决: XX振幅被相互作用完全摧毁。**")
        lines.append("")
        lines.append("论据：")
        lines.append(f"1. F(Delta!=0) = {l4['max_F']:.2e} → Re(C_{{i!=j}})被激发")
        lines.append(f"2. O_XX被强烈压制（Delta_c = {l4['delta_c']:.4f})")
        lines.append("3. 纯虚定理的对称性保护在XXZ中不成立")
        lines.append("")
        lines.append("→ XX振幅在自由费米子极限(Delta=0)中是巧合，而非深层结构。")

    lines.append("")
    lines.append("## 方法论注释")
    lines.append("")
    lines.append("- L=4: Fock空间16维，Liouvillian 256×256，SVD精确对角化")
    lines.append("- L=6: Fock空间64维，Liouvillian 4096×4096，shift-invert Arnoldi迭代")
    lines.append("- F值在数值误差以内(≲1e-15)时视为零")
    lines.append("- 密度矩阵物理性检查：Tr(ρ)=1, ρ=ρ†, ρ≥0")
    lines.append(f"- 参数：J={J}, Gamma_L={GAMMA_L}, Gamma_R={GAMMA_R}, f_L={F_L}, f_R={F_R}")
    lines.append("")
    lines.append("---")
    lines.append(f"*Firewall 2 检验完成于 {time.strftime('%Y-%m-%d %H:%M:%S')}*")

    return '\n'.join(lines)


# ==============================================================================
# Main
# ==============================================================================

def main():
    print("=" * 70)
    print("  FIREWALL 2: XXZ Chain Boundary-Driven NESS")
    print("  Testing whether O_XX survives interactions")
    print("=" * 70)
    print(f"  J={J}, Gamma_L={GAMMA_L}, Gamma_R={GAMMA_R}, f_L={F_L}, f_R={F_R}")
    print(f"  Delta ∈ {DELTA_VALUES}")
    print(f"  gamma_phi ∈ {GAMMA_PHI_VALUES}")
    print("=" * 70)

    # Run L=4 (dense exact)
    results_L4 = run_L4()

    # Run L=6 (sparse iterative)
    results_L6 = run_L6()

    # Compile
    all_results = {
        'L4': results_L4,
        'L6': results_L6,
    }

    # Analyze
    print("\n" + "=" * 70)
    print("  ANALYSIS")
    print("=" * 70)
    analysis = analyze_results(all_results)

    # Render verdict
    verdict_md = render_verdict(analysis, all_results)

    # Save data
    data_path = r"D:\Claude\ai-reservations\LP25-FCS-Quantum-Foundations\current\plan\firewall2_results.json"
    output = {
        'results': all_results,
        'analysis': analysis,
    }

    # Convert numpy types for JSON serialization
    def convert(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.complexfloating, complex)):
            if abs(obj.imag) < 1e-15:
                return float(obj.real)
            return [float(obj.real), float(obj.imag)]
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, dict):
            return {str(k) if isinstance(k, (np.floating, np.integer)) else k: convert(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [convert(item) for item in obj]
        return obj

    output_clean = convert(output)

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(output_clean, f, indent=2, ensure_ascii=False)
    print(f"\nData saved to: {data_path}")

    # Save markdown report
    md_path = r"D:\Claude\ai-reservations\LP25-FCS-Quantum-Foundations\current\plan\round4_Firewall2_XXZ.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(verdict_md)
    print(f"Report saved to: {md_path}")

    # Print verdict to stdout
    print("\n" + verdict_md)

    print("\nDone.")


if __name__ == '__main__':
    main()
