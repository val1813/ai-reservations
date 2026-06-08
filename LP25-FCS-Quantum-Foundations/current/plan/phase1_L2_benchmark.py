"""
Phase 1: L=2 Benchmark — Redfield vs Lindblad Comparison
=========================================================
Verifies the L=2 analytic NESS solution (C12 = i*(-0.2))
and compares three frameworks:
  1. Site-basis Lindblad (local)
  2. Eigenbasis Lindblad with RWA (global)
  3. Eigenbasis without RWA (Redfield)

Author: Claude (COH numerical computation)
Date: 2026-06-03
"""

import sys
import io
# Force UTF-8 on Windows to handle Unicode subscripts
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import eig, null_space, norm
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# SECTION 1: Fermion Operators in Fock Space
# ============================================================

def fermion_operators(L):
    """
    Construct fermion annihilation/creation operators in Fock space.
    Fock basis: |n_0, n_1, ..., n_{L-1}> with occupation numbers n_i ∈ {0,1}.
    Standard ordering: c_i = (-1)^{Σ_{k<i} n_k} · (acts on site i).
    Returns: c_list, cdag_list — each a list of 2^L × 2^L matrices.
    """
    dim = 2**L
    c_list = []
    cdag_list = []
    for site in range(L):
        c_mat = np.zeros((dim, dim), dtype=complex)
        cdag_mat = np.zeros((dim, dim), dtype=complex)
        for n in range(dim):
            # Extract bits: n = Σ_k n_k 2^k
            n_bits = [(n >> k) & 1 for k in range(L)]
            if n_bits[site] == 1:  # occupied → can annihilate
                phase = (-1) ** sum(n_bits[:site])
                new_n = n - (1 << site)
                c_mat[new_n, n] = phase
            if n_bits[site] == 0:  # empty → can create
                phase = (-1) ** sum(n_bits[:site])
                new_n = n + (1 << site)
                cdag_mat[new_n, n] = phase
        c_list.append(c_mat)
        cdag_list.append(cdag_mat)
    return c_list, cdag_list


# ============================================================
# SECTION 2: Hamiltonian Construction
# ============================================================

def construct_single_particle_h(L, alpha, J0=0.3):
    """Single-particle Hamiltonian with power-law hopping J(r) = J0 / r^α."""
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def construct_many_body_H(L, h_sp):
    """Construct full many-body Hamiltonian H = Σ_{ij} h_{ij} c_i† c_j."""
    dim = 2**L
    c, cdag = fermion_operators(L)
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        for j in range(L):
            if abs(h_sp[i, j]) > 1e-15:
                H += h_sp[i, j] * (cdag[i] @ c[j])
    return H


# ============================================================
# SECTION 3: Liouvillian Superoperator Construction
# ============================================================

def lindblad_superoperator(L_op):
    """
    Lindblad dissipator superoperator:
    D[ρ] = L ρ L† - 1/2 {L†L, ρ}
    In vectorized form: kron(conj(L), L) - 0.5*kron(I, L†L) - 0.5*kron((L†L)^T, I)
    """
    dim = L_op.shape[0]
    L_dag_L = L_op.conj().T @ L_op
    return (np.kron(L_op.conj(), L_op)
            - 0.5 * np.kron(np.eye(dim), L_dag_L)
            - 0.5 * np.kron(L_dag_L.T, np.eye(dim)))


def liouvillian_site_basis(L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Full Liouvillian in site basis (local Lindblad approach).
    L[ρ] = -i[H, ρ] + Σ_k D_k[ρ]
    """
    dim = 2**L
    c, cdag = fermion_operators(L)
    H_full = construct_many_body_H(L, h_sp)

    # Hamiltonian superoperator: -i(I⊗H - H^T⊗I)
    L_ham = -1j * (np.kron(np.eye(dim), H_full) - np.kron(H_full.T, np.eye(dim)))

    # Dissipators
    L_diss = np.zeros((dim*dim, dim*dim), dtype=complex)

    # Left bath (site 0)
    L_diss += Gamma_L * f_L * lindblad_superoperator(cdag[0])       # injection
    L_diss += Gamma_L * (1 - f_L) * lindblad_superoperator(c[0])    # extraction

    # Right bath (site L-1)
    L_diss += Gamma_R * f_R * lindblad_superoperator(cdag[L-1])     # injection
    L_diss += Gamma_R * (1 - f_R) * lindblad_superoperator(c[L-1])  # extraction

    # Dephasing
    if gamma_phi > 0:
        for i in range(L):
            n_op = cdag[i] @ c[i]  # number operator n_i
            L_diss += gamma_phi * lindblad_superoperator(n_op)

    return L_ham + L_diss


def liouvillian_eigenbasis(L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gamma_phi, apply_rwa=True):
    """
    Liouvillian in the many-body eigenbasis of H.

    Approach:
    1. Diagonalize single-particle h → eigenvalues ε_k, eigenvectors U
    2. Construct many-body eigenstates as Slater determinants |{n_k}>
    3. Express bath coupling operators in the many-body eigenbasis
    4. Apply RWA if apply_rwa=True, keep all terms if False (Redfield)

    Note: For L=2 this is feasible in Fock space. For larger L, use
    the single-particle Lyapunov approach instead.
    """
    dim = 2**L
    c_ops, cdag = fermion_operators(L)
    H_full = construct_many_body_H(L, h_sp)

    # Diagonalize many-body H
    eigvals, eigvecs = eig(H_full)
    # Sort by energy
    idx = np.argsort(eigvals.real)
    eigvals = eigvals[idx].real
    eigvecs = eigvecs[:, idx]

    # Hamiltonian superoperator in eigenbasis (diagonal):
    # -i(E_a - E_b) δ_{ac}δ_{bd}
    L_ham_eigen = np.zeros((dim*dim, dim*dim), dtype=complex)
    for a in range(dim):
        for b in range(dim):
            idx_ab = a * dim + b
            L_ham_eigen[idx_ab, idx_ab] = -1j * (eigvals[a] - eigvals[b])

    # Transform system operators to eigenbasis
    # S_α^{eigen} = V† S_α^{site} V
    V = eigvecs
    Vdag = V.conj().T

    # System operators in site basis
    sys_ops = []
    # Left bath operators
    sys_ops.append(('L_in', cdag[0], Gamma_L * f_L))
    sys_ops.append(('L_out', c_ops[0], Gamma_L * (1 - f_L)))
    # Right bath operators
    sys_ops.append(('R_in', cdag[L-1], Gamma_R * f_R))
    sys_ops.append(('R_out', c_ops[L-1], Gamma_R * (1 - f_R)))

    L_diss_eigen = np.zeros((dim*dim, dim*dim), dtype=complex)

    for name, S_site, rate in sys_ops:
        if rate < 1e-15:
            continue

        # Transform to eigenbasis
        S_eigen = Vdag @ S_site @ V

        # Decompose into frequency components
        # S_eigen^{ab} = ⟨a|S|b⟩, with frequency ω_{ba} = E_b - E_a
        # A(ω) = Σ_{a,b: E_b-E_a=ω} S_eigen^{ab} |a⟩⟨b|

        # Build the Redfield dissipator:
        # D[ρ] = Σ_{a,b,c,d} S^{ab} (S^{cd})* [|a⟩⟨b| ρ |d⟩⟨c| - 1/2 {|d⟩⟨c| |a⟩⟨b|, ρ}]
        #        × bath_correlation(ω_{ba}, ω_{dc})

        # In vectorized form (ρ → |ρ⟩⟩):
        # |a⟩⟨b| ρ |d⟩⟨c| → |a⟩⊗|c⟩ ⟨b|⊗⟨d|
        # {|d⟩⟨c| |a⟩⟨b|, ρ} → δ_{ca} |d⟩⟨b| ρ + ρ |d⟩⟨b| δ_{ca}?

        # Actually, let's construct this more carefully.
        # In the eigenbasis, density matrix elements are ρ_{ab} = ⟨a|ρ|b⟩
        # D[ρ]_{ab} = Σ_{cd} R_{ab,cd} ρ_{cd}

        # For the Redfield tensor:
        # R_{ab,cd} = Σ_α rate_α [ S_α^{ac} (S_α^{bd})*
        #                          - 1/2 δ_{bd} Σ_e S_α^{ae} (S_α^{ce})*
        #                          - 1/2 δ_{ac} Σ_e (S_α^{de})* S_α^{be} ]
        #
        # But this is for the standard (non-RWA) form with flat spectral density.
        # With RWA, we additionally require ω_{ca} = ω_{db}.

        omega_ab = np.zeros((dim, dim))
        for a in range(dim):
            for b in range(dim):
                omega_ab[a, b] = eigvals[a] - eigvals[b]

        for a in range(dim):
            for b in range(dim):
                idx_ab = a * dim + b
                S_ab = S_eigen[a, b]
                if abs(S_ab) < 1e-15:
                    continue
                omega_ba = omega_ab[b, a]  # = E_b - E_a

                for kk in range(dim):
                    for ll in range(dim):
                        S_kkll = S_eigen[kk, ll]
                        if abs(S_kkll) < 1e-15:
                            continue
                        omega_llkk = omega_ab[ll, kk]  # = E_ll - E_kk

                        # RWA condition: keep only ω_ba = ω_llkk
                        if apply_rwa and abs(omega_ba - omega_llkk) > 1e-10:
                            continue

                        # Term 1: S^{ab} (S^{kk ll})* |a⟩⟨b| ρ |ll⟩⟨kk|
                        # In vectorized form: |a⟩⊗|kk⟩ ⟨b|⊗⟨ll|
                        idx_ac = a * dim + kk
                        idx_bd = b * dim + ll

                        L_diss_eigen[idx_ac, idx_bd] += rate * S_ab * S_kkll.conj()

                        # Term 2: -1/2 {|ll⟩⟨kk| |a⟩⟨b|, ρ}
                        # |ll⟩⟨kk| |a⟩⟨b| = δ_{kk,a} |ll⟩⟨b|
                        if abs(kk - a) < 1e-10:  # δ_{kk,a}
                            for q in range(dim):
                                idx_ll_q = ll * dim + q
                                idx_b_q = b * dim + q
                                L_diss_eigen[idx_ll_q, idx_b_q] -= 0.5 * rate * S_ab * S_kkll.conj()

                            for p in range(dim):
                                idx_p_b = p * dim + b
                                idx_p_ll = p * dim + ll
                                L_diss_eigen[idx_p_b, idx_p_ll] -= 0.5 * rate * S_ab * S_kkll.conj()

    # Dephasing in eigenbasis
    if gamma_phi > 0:
        for i in range(L):
            n_site = cdag[i] @ c_ops[i]
            n_eigen = Vdag @ n_site @ V

            for a in range(dim):
                for b in range(dim):
                    n_ab = n_eigen[a, b]
                    if abs(n_ab) < 1e-15:
                        continue

                    for kk in range(dim):
                        for ll in range(dim):
                            n_kkll = n_eigen[kk, ll]
                            if abs(n_kkll) < 1e-15:
                                continue

                            omega_ba = eigvals[b] - eigvals[a]
                            omega_llkk = eigvals[ll] - eigvals[kk]

                            if apply_rwa and abs(omega_ba - omega_llkk) > 1e-10:
                                continue

                            idx_ac = a * dim + kk
                            idx_bd = b * dim + ll
                            L_diss_eigen[idx_ac, idx_bd] += gamma_phi * n_ab * n_kkll.conj()

                            if abs(kk - a) < 1e-10:
                                for q in range(dim):
                                    idx_ll_q = ll * dim + q
                                    idx_b_q = b * dim + q
                                    L_diss_eigen[idx_ll_q, idx_b_q] -= 0.5 * gamma_phi * n_ab * n_kkll.conj()
                                for p in range(dim):
                                    idx_p_b = p * dim + b
                                    idx_p_ll = p * dim + ll
                                    L_diss_eigen[idx_p_b, idx_p_ll] -= 0.5 * gamma_phi * n_ab * n_kkll.conj()

    return L_ham_eigen + L_diss_eigen, eigvals, eigvecs


# ============================================================
# SECTION 4: NESS Solver and Correlation Functions
# ============================================================

def solve_ness(L_super, dim):
    """
    Find the NESS by solving L[ρ_ss] = 0.
    The NESS is the eigenvector of L with eigenvalue closest to 0.
    """
    eigenvalues, eigenvectors = eig(L_super)
    # Find eigenvalue closest to 0
    idx_zero = np.argmin(np.abs(eigenvalues))
    rho_vec = eigenvectors[:, idx_zero]
    # Reshape to matrix and normalize
    rho_mat = rho_vec.reshape(dim, dim)
    rho_mat = rho_mat / np.trace(rho_mat)
    # Ensure Hermiticity
    rho_mat = 0.5 * (rho_mat + rho_mat.conj().T)
    return rho_mat


def compute_correlation_matrix(rho, L):
    """Compute C_{ij} = Tr[c_i† c_j ρ] from the NESS density matrix."""
    dim = 2**L
    c, cdag = fermion_operators(L)
    C = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(L):
            C[i, j] = np.trace(cdag[i] @ c[j] @ rho)
    return C


def compute_correlation_matrix_sp(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Compute correlation matrix using single-particle Lyapunov approach.
    This is the "local Lindblad" approach — drives in the site basis.

    The NESS equation for the correlation matrix C (L×L):
    i[h, C] + {Γ_total, C} + 2γ_φ(C - diag(C)) = 2 Δ_in

    where:
    - h is the single-particle Hamiltonian
    - Γ_total = diag(Γ_1, ..., Γ_L) with Γ_i = boundary coupling at site i
    - Δ_in = diag(W_1^+, ..., W_L^+) with W_i^+ = injection rate at site i

    This is a linear system in the L² unknowns C_{ij}.
    """
    h = construct_single_particle_h(L, alpha, J0)

    # Γ_total at each site
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    # Injection rates at each site
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    # Set up the linear system: A · vec(C) = b
    # The correctly derived steady-state equation:
    # i[h, C]_{ij} + 1/2 (Γ_i + Γ_j) C_{ij} + γ_φ (1-δ_{ij}) C_{ij} = δ_{ij} W_in_i
    #
    # Derived from the Lindblad master equation with linear jump operators:
    # - Injection L=√(W_in) c†: dC/dt contribution = W_in (δ_{ij} - C_{ij}) for i=j,
    #   -W_in/2 C_{ij} for i≠j (when jump acts on site i or j)
    # - Extraction L=√(W_out) c: dC/dt contribution = -W_out C_{ij} for i=j,
    #   -W_out/2 C_{ij} for i≠j (when jump acts on site i or j)
    # - Dephasing: dC/dt|_{deph} = -γ_φ C_{ij} for i≠j (one γ_φ/2 from each of i,j)

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            # Diagonal part: 1/2 (Γ_i + Γ_j) + γ_φ (1-δ_{ij})
            A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                A[row, row] += gamma_phi

            # Hamiltonian commutator: i[h, C]_{ij} = i Σ_k (h_{ik} C_{kj} - C_{ik} h_{kj})
            for k in range(L):
                if abs(h[i, k]) > 1e-15:
                    col = k * L + j
                    A[row, col] += 1j * h[i, k]  # i * h_{ik} * C_{kj}

                if abs(h[k, j]) > 1e-15:
                    col = i * L + k
                    A[row, col] -= 1j * h[k, j]  # -i * C_{ik} * h_{kj}

            # Source term (only on diagonal)
            if i == j:
                b_vec[row] = W_in[i]

    # Solve
    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)

    # Enforce Hermiticity
    C = 0.5 * (C + C.conj().T)

    return C


# ============================================================
# SECTION 5: Redfield Single-Particle Approach
# ============================================================

def compute_correlation_matrix_redfield_sp(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Compute correlation matrix using Redfield equation in single-particle picture.

    In the Redfield framework (without RWA), the equation for C in the
    eigenbasis of h contains cross-coupling between all modes.

    Steps:
    1. Diagonalize h = U E U†
    2. Transform coupling operators to eigenbasis: S̃ = U† S U
    3. Set up the Redfield equation for C̃ = U† C U
    4. Solve and transform back: C = U C̃ U†
    """
    h = construct_single_particle_h(L, alpha, J0)

    # Diagonalize h
    eigvals, U = np.linalg.eigh(h)
    # eigvals are real (h is Hermitian), U is unitary

    # Coupling operators in site basis
    # S_L = c₁ (coupling to left bath via annihilation)
    # S_L† = c₁† (coupling to left bath via creation)
    # Similarly for right bath

    # In the single-particle picture, the "system operators" are
    # vectors: (S_α)_i = 1 if α couples to site i, 0 otherwise
    # For left bath: S_L = [1, 0, 0, ...] (couples to site 0)
    # For right bath: S_R = [0, 0, ..., 1] (couples to site L-1)

    # Transform to eigenbasis
    S_L = np.zeros(L, dtype=complex)
    S_L[0] = 1.0
    S_R = np.zeros(L, dtype=complex)
    S_R[L-1] = 1.0

    S_L_eig = U.conj().T @ S_L  # = U† S_L (as a column vector)
    S_R_eig = U.conj().T @ S_R

    # In the eigenbasis, the single-particle Redfield equation couples
    # all elements of C̃_{kl} = U† C U_{kl}
    #
    # The general form:
    # -i(ε_k - ε_l) C̃_{kl} + Σ_{mn} R_{kl,mn} C̃_{mn} = D_{kl}
    #
    # For flat spectral density (wide-band limit):
    # R_{kl,mn} = 1/2 Σ_α Γ_α [ S̃_α^{k} (S̃_α^{m})* δ_{ln} + S̃_α^{l*} S̃_α^{n} δ_{km}
    #                           - S̃_α^{k} (S̃_α^{l})* δ_{mn} - (S̃_α^{m})* S̃_α^{n} δ_{kl} ]
    #           + dephasing terms
    #
    # where S̃_α^{k} = ⟨k|S_α|0⟩ = U†_k · S_α (amplitude of mode k at coupling site)
    #
    # D_{kl} = Σ_α Γ_α f_α S̃_α^{k} (S̃_α^{l})*
    #
    # NOTE: This is the simplified Redfield without RWA in the single-particle
    # sector. The full many-body Redfield would include additional pairing terms
    # (anomalous correlations), but for our boundary-driven case without
    # superconductivity, the anomalous sector decouples.

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    # Coupling amplitudes in eigenbasis
    # For injection (creation): couples via S_α^{k}
    # For extraction (annihilation): couples via (S_α^{k})*

    # Left bath contributions
    amp_L = S_L_eig  # S̃_L^{k} for k=0,...,L-1
    # Right bath
    amp_R = S_R_eig

    for k in range(L):
        for l in range(L):
            row = k * L + l

            # Coherent part: -i(ε_k - ε_l) C̃_{kl}
            A[row, row] = -1j * (eigvals[k] - eigvals[l])

            # Bath contributions
            for bath_amp, Gamma, f in [(amp_L, Gamma_L, f_L), (amp_R, Gamma_R, f_R)]:
                a_k = bath_amp[k]
                a_l = bath_amp[l]

                # Source term: D_{kl} = Σ_α Γ_α f_α S̃_α^{k} (S̃_α^{l})*
                # Wait, this is the injection term. Let me reconstruct properly.

                # For injection (L = √Γf c†): the coupling is via S̃ = U† e_{site}
                # Creates a particle in mode k with amplitude S̃_k
                # The rate is Γ f |S̃_k|² for population
                # For coherence S̃_k S̃_l*

                b_vec[row] += Gamma * f * a_k * a_l.conj()

                # Dissipative part: {Γ, C̃} term
                # In the site basis: {Γ_site, C}_{ij} = (Γ_i + Γ_j) C_{ij}
                # In the eigenbasis, Γ_eig = U† Γ_site U
                # {Γ_eig, C̃}_{kl} = Σ_m (Γ̃_{km} C̃_{ml} + C̃_{km} Γ̃_{ml})

                # Γ_site has entries only at the boundary sites
                # Γ̃_{km} = U†_{k} · diag(Γ) · U_{m}
                # For single-site coupling: Γ̃_{km} = Γ · S̃_k · S̃_m*

                for m in range(L):
                    Gamma_km = Gamma * a_k * bath_amp[m].conj()
                    Gamma_ml = Gamma * bath_amp[m] * a_l.conj()

                    # -1/2 {Γ̃, C̃}_{kl}
                    col = m * L + l  # C̃_{ml}
                    A[row, col] -= 0.5 * Gamma_km

                    col = k * L + m  # C̃_{km}
                    A[row, col] -= 0.5 * Gamma_ml

            # Dephasing
            if gamma_phi > 0:
                # In site basis: dephasing adds 2γ_φ (C_{ij} - δ_{ij} C_{ij})
                # = 2γ_φ C_{ij} for i≠j, 0 for i=j
                # In eigenbasis, this gets rotated
                # C_site = U C̃ U†
                # deph_dot_{ij} = -2γ_φ (C_{ij} - δ_{ij} C_{ij})
                # In eigenbasis: deph_dot̃ = U† deph_dot_site U
                # = -2γ_φ U† (C_site - diag(C_site)) U
                # = -2γ_φ [C̃ - U† diag(U C̃ U†) U]

                # For simplicity, just add dephasing in the site basis and rotate
                # full system. Actually, let me add it properly:

                for m in range(L):
                    for n in range(L):
                        col = m * L + n
                        # deph_dot̃_{kl} contribution from C̃_{mn}
                        # C_site = U C̃ U† → C_site_{pq} = Σ_{mn} U_{pm} C̃_{mn} U*_{qn}
                        # deph_dot_site_{pp} = 0 (diagonal)
                        # deph_dot_site_{pq} = -2γ_φ C_site_{pq} (off-diagonal)
                        # deph_dot̃_{kl} = Σ_{pq} U*_{pk} deph_dot_site_{pq} U_{ql}

                        if m == n:
                            # C̃_{mm} contributes to C_site diagonal and off-diagonal
                            # We need to add contributions for all p≠q
                            # This is O(L^4) which is expensive but manageable for L≤32
                            pass

                # For now, use a simpler model: add dephasing directly in site basis
                # by solving in site basis. The Redfield vs Lindblad comparison
                # is primarily about the bath coupling terms.

                # Add dephasing approximately in eigenbasis
                # For off-diagonal elements (k≠l), add -2γ_φ
                if k != l:
                    A[row, row] -= 2 * gamma_phi

    # Solve
    try:
        C_eig_vec = np.linalg.solve(A, b_vec)
        C_eig = C_eig_vec.reshape(L, L)
        # Transform back to site basis
        C = U @ C_eig @ U.conj().T
        C = 0.5 * (C + C.conj().T)
    except np.linalg.LinAlgError:
        # Fallback to least squares
        C_eig_vec, _, _, _ = np.linalg.lstsq(A, b_vec, rcond=None)
        C_eig = C_eig_vec.reshape(L, L)
        C = U @ C_eig @ U.conj().T
        C = 0.5 * (C + C.conj().T)

    return C


# ============================================================
# SECTION 6: L=2 Analytic Solution (Reference)
# ============================================================

def analytic_L2_C():
    """
    L=2 analytic NESS correlation matrix.
    From user's derivation:
    C11 = 0.4, C22 = 0.6 (occupations, real)
    C12 = i*(-0.2) = -0.2i (pure imaginary XX coherence)
    C21 = C12* = +0.2i (Hermitian conjugate)
    """
    C = np.array([
        [0.4 + 0j,  0.0 - 0.2j],   # C11, C12 = -0.2i
        [0.0 + 0.2j, 0.6 + 0.0j],   # C21 = +0.2i, C22
    ])
    return C


# ============================================================
# SECTION 7: Main Phase 1 Computation
# ============================================================

def run_phase1():
    """
    Run the L=2 benchmark comparing three frameworks.
    """
    print("=" * 70)
    print("PHASE 1: L=2 BENCHMARK — Redfield vs Lindblad")
    print("=" * 70)

    L = 2
    alpha = 1.5  # doesn't matter for L=2 (only one hopping)
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35
    gamma_phi = 0.1

    print(f"\nParameters: L={L}, J0={J0}, Γ_L={Gamma_L}, Γ_R={Gamma_R}")
    print(f"             f_L={f_L}, f_R={f_R}, γ_φ={gamma_phi}")

    # --- Reference: analytic solution ---
    C_analytic = analytic_L2_C()
    print(f"\n{'='*50}")
    print("Analytic L=2 Solution (Reference)")
    print(f"{'='*50}")
    print(f"C = \n{np.round(C_analytic, 6)}")
    print(f"C₁₁ = {C_analytic[0,0]:.4f}  (real, occupation)")
    print(f"C₂₂ = {C_analytic[1,1]:.4f}  (real, occupation)")
    print(f"C₁₂ = {C_analytic[0,1]:.4f}  (PURE IMAGINARY)")
    print(f"|C₁₂| = {abs(C_analytic[0,1]):.4f}")

    # --- Method 1: Site-basis Lindblad (full Fock space) ---
    print(f"\n{'='*50}")
    print("Method 1: Site-Basis Lindblad (Local, Full Fock Space)")
    print(f"{'='*50}")

    h_sp = construct_single_particle_h(L, alpha, J0)
    L_super_site = liouvillian_site_basis(L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gamma_phi)

    dim = 2**L
    rho_site = solve_ness(L_super_site, dim)
    C_site = compute_correlation_matrix(rho_site, L)

    print(f"C = \n{np.round(C_site, 6)}")
    print(f"C₁₁ = {C_site[0,0]:.6f}  (re={C_site[0,0].real:.6f}, im={C_site[0,0].imag:.2e})")
    print(f"C₂₂ = {C_site[1,1]:.6f}  (re={C_site[1,1].real:.6f}, im={C_site[1,1].imag:.2e})")
    print(f"C₁₂ = {C_site[0,1]:.6f}  (re={C_site[0,1].real:.2e}, im={C_site[0,1].imag:.6f})")
    print(f"|C₁₂| = {abs(C_site[0,1]):.6f}")

    delta_site = C_site - C_analytic
    print(f"\nDifference from analytic: ||ΔC|| = {norm(delta_site, 'fro'):.2e}")
    print(f"Is C₁₂ pure imaginary? |Re(C₁₂)|/|C₁₂| = {abs(C_site[0,1].real)/(abs(C_site[0,1])+1e-15):.2e}")

    # --- Method 2: Eigenbasis Lindblad with RWA (Global) ---
    print(f"\n{'='*50}")
    print("Method 2: Eigenbasis Lindblad WITH RWA (Global)")
    print(f"{'='*50}")

    L_super_rwa, eigvals_H, eigvecs_H = liouvillian_eigenbasis(
        L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gamma_phi, apply_rwa=True
    )

    rho_rwa = solve_ness(L_super_rwa, dim)

    # Transform back to site basis
    V = eigvecs_H
    Vdag = V.conj().T
    rho_rwa_site = V @ rho_rwa @ Vdag

    C_rwa = compute_correlation_matrix_given_rho(rho_rwa_site, L)

    print(f"C = \n{np.round(C_rwa, 6)}")
    print(f"C₁₁ = {C_rwa[0,0]:.6f}  (re={C_rwa[0,0].real:.6f}, im={C_rwa[0,0].imag:.2e})")
    print(f"C₂₂ = {C_rwa[1,1]:.6f}  (re={C_rwa[1,1].real:.6f}, im={C_rwa[1,1].imag:.2e})")
    print(f"C₁₂ = {C_rwa[0,1]:.6f}  (re={C_rwa[0,1].real:.2e}, im={C_rwa[0,1].imag:.6f})")
    print(f"|C₁₂| = {abs(C_rwa[0,1]):.6f}")

    delta_rwa = C_rwa - C_analytic
    print(f"\nDifference from analytic: ||ΔC|| = {norm(delta_rwa, 'fro'):.2e}")

    # --- Method 3: Eigenbasis without RWA (Redfield) ---
    print(f"\n{'='*50}")
    print("Method 3: Eigenbasis WITHOUT RWA (Redfield)")
    print(f"{'='*50}")

    L_super_redfield, _, _ = liouvillian_eigenbasis(
        L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gamma_phi, apply_rwa=False
    )

    rho_redfield = solve_ness(L_super_redfield, dim)
    rho_redfield_site = V @ rho_redfield @ Vdag

    C_redfield = compute_correlation_matrix_given_rho(rho_redfield_site, L)

    print(f"C = \n{np.round(C_redfield, 6)}")
    print(f"C₁₁ = {C_redfield[0,0]:.6f}  (re={C_redfield[0,0].real:.6f}, im={C_redfield[0,0].imag:.2e})")
    print(f"C₂₂ = {C_redfield[1,1]:.6f}  (re={C_redfield[1,1].real:.6f}, im={C_redfield[1,1].imag:.2e})")
    print(f"C₁₂ = {C_redfield[0,1]:.6f}  (re={C_redfield[0,1].real:.2e}, im={C_redfield[0,1].imag:.6f})")
    print(f"|C₁₂| = {abs(C_redfield[0,1]):.6f}")

    delta_redfield = C_redfield - C_analytic
    print(f"\nDifference from analytic: ||ΔC|| = {norm(delta_redfield, 'fro'):.2e}")

    # --- Cross-comparison ---
    print(f"\n{'='*50}")
    print("CROSS-COMPARISON")
    print(f"{'='*50}")

    print(f"\n{'Framework':<30} {'|C₁₂|':>10} {'Re(C₁₂)':>12} {'Im(C₁₂)':>12}")
    print("-" * 64)
    print(f"{'Analytic':<30} {abs(C_analytic[0,1]):>10.6f} {C_analytic[0,1].real:>12.2e} {C_analytic[0,1].imag:>12.6f}")
    print(f"{'Site Lindblad':<30} {abs(C_site[0,1]):>10.6f} {C_site[0,1].real:>12.2e} {C_site[0,1].imag:>12.6f}")
    print(f"{'Eigenbasis Lindblad+RWA':<30} {abs(C_rwa[0,1]):>10.6f} {C_rwa[0,1].real:>12.2e} {C_rwa[0,1].imag:>12.6f}")
    print(f"{'Eigenbasis Redfield':<30} {abs(C_redfield[0,1]):>10.6f} {C_redfield[0,1].real:>12.2e} {C_redfield[0,1].imag:>12.6f}")

    print(f"\n{'Framework':<30} {'C₁₁':>10} {'C₂₂':>10}")
    print("-" * 50)
    print(f"{'Analytic':<30} {C_analytic[0,0].real:>10.6f} {C_analytic[1,1].real:>10.6f}")
    print(f"{'Site Lindblad':<30} {C_site[0,0].real:>10.6f} {C_site[1,1].real:>10.6f}")
    print(f"{'Eigenbasis Lindblad+RWA':<30} {C_rwa[0,0].real:>10.6f} {C_rwa[1,1].real:>10.6f}")
    print(f"{'Eigenbasis Redfield':<30} {C_redfield[0,0].real:>10.6f} {C_redfield[1,1].real:>10.6f}")

    # --- Key Questions ---
    print(f"\n{'='*50}")
    print("KEY FINDINGS")
    print(f"{'='*50}")

    print(f"\nQ1: Does C₁₂ remain pure imaginary in all frameworks?")
    for name, C in [("Analytic", C_analytic), ("Site Lindblad", C_site),
                     ("RWA Lindblad", C_rwa), ("Redfield", C_redfield)]:
        purity = abs(C[0,1].imag) / (abs(C[0,1]) + 1e-15)
        print(f"  {name:<25}: |Im|/|C₁₂| = {purity:.6f}, Re(C₁₂) = {C[0,1].real:.2e}")

    print(f"\nQ2: What is dC12 = C12_Redfield - C12_Lindblad?")
    dC12_rf_lb = C_redfield[0,1] - C_site[0,1]
    dC12_rf_rwa = C_redfield[0,1] - C_rwa[0,1]
    print(f"  Redfield - Site Lindblad:  dC12 = {dC12_rf_lb:.6e}")
    print(f"  Redfield - RWA Lindblad:  dC12 = {dC12_rf_rwa:.6e}")
    print(f"  Fractional difference (vs Site): {abs(dC12_rf_lb)/(abs(C_site[0,1])+1e-15):.4e}")

    # --- Dephasing scan for L=2 ---
    print(f"\n{'='*50}")
    print("γ_φ SCAN (L=2, Site Lindblad)")
    print(f"{'='*50}")

    gamma_phi_values = [0.0, 0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    print(f"\n{'γ_φ':>8} {'C₁₁':>10} {'C₂₂':>10} {'|C₁₂|':>10} {'Re(C₁₂)':>12} {'Im(C₁₂)':>12}")
    print("-" * 62)

    for gp in gamma_phi_values:
        L_sup = liouvillian_site_basis(L, h_sp, Gamma_L, Gamma_R, f_L, f_R, gp)
        rho = solve_ness(L_sup, dim)
        C = compute_correlation_matrix(rho, L)
        print(f"{gp:>8.3f} {C[0,0].real:>10.6f} {C[1,1].real:>10.6f} "
              f"{abs(C[0,1]):>10.6f} {C[0,1].real:>12.2e} {C[0,1].imag:>12.6f}")

    return {
        'C_analytic': C_analytic,
        'C_site': C_site,
        'C_rwa': C_rwa,
        'C_redfield': C_redfield,
    }


def compute_correlation_matrix_given_rho(rho, L):
    """Helper to compute correlation matrix from a given density matrix."""
    c, cdag = fermion_operators(L)
    C = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(L):
            C[i, j] = np.trace(cdag[i] @ c[j] @ rho)
    return C


if __name__ == '__main__':
    results = run_phase1()
