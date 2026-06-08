"""
Phase 2 深度分析脚本
1. 验证找到的tower是否与已知Kerschbaumer家族一致
2. 搜索非SU(2)疤痕特征
3. 生成分类学报告
"""

import numpy as np
from scipy import linalg
from scipy.sparse import lil_matrix, csr_matrix
from itertools import product
import json

# Reuse the same functions from pxp_scar_search.py
def build_pxp_basis(L, alpha, pbc=True):
    basis = []
    for bits in product([0, 1], repeat=L):
        valid = True
        for i in range(L):
            if bits[i] == 1:
                for d in range(1, alpha + 1):
                    jr = (i + d) % L if pbc else i + d
                    jl = (i - d) % L if pbc else i - d
                    if pbc:
                        if bits[jr] == 1 or bits[jl] == 1:
                            valid = False; break
                    else:
                        if (jr < L and bits[jr] == 1) or (jl >= 0 and bits[jl] == 1):
                            valid = False; break
                if not valid: break
        if valid: basis.append(sum(b << (L-1-i) for i, b in enumerate(bits)))
    return sorted(basis)

def count_excitations(b, L):
    return bin(b).count('1')

def bits_to_str(b, L):
    return format(b, f'0{L}b')

def build_pxp_hamiltonian(L, alpha, Omega=1.0, Delta=0.0, pbc=True):
    basis = build_pxp_basis(L, alpha, pbc)
    D = len(basis)
    H = lil_matrix((D, D), dtype=float)
    state_to_idx = {b: i for i, b in enumerate(basis)}

    for idx, b in enumerate(basis):
        s = bits_to_str(b, L)
        for i in range(L):
            if s[i] == '1':
                allowed = True
                for d in range(1, alpha + 1):
                    jr = (i + d) % L if pbc else i + d
                    jl = (i - d) % L if pbc else i - d
                    if pbc:
                        if s[jr] == '1' or s[jl] == '1':
                            allowed = False; break
                    else:
                        if (jr < L and s[jr] == '1') or (jl >= 0 and s[jl] == '1'):
                            allowed = False; break
                if allowed:
                    H[idx, idx] += Delta

            elif s[i] == '0':
                allowed = True
                for d in range(1, alpha + 1):
                    jr = (i + d) % L if pbc else i + d
                    jl = (i - d) % L if pbc else i - d
                    if pbc:
                        if s[jr] == '1' or s[jl] == '1':
                            allowed = False; break
                    else:
                        if (jr < L and s[jr] == '1') or (jl >= 0 and s[jl] == '1'):
                            allowed = False; break
                if allowed:
                    s_list = list(s)
                    s_list[i] = '1'
                    new_s = ''.join(s_list)
                    new_b = int(new_s, 2)
                    if new_b in state_to_idx:
                        H[state_to_idx[new_b], idx] += Omega
                        H[idx, state_to_idx[new_b]] += Omega

    return csr_matrix(H), basis

def compute_all_entropies(eigvecs, basis, L):
    """Compute half-chain von Neumann entropy for all eigenstates efficiently."""
    D, n_eig = eigvecs.shape
    LA = L // 2
    dimA = 2**LA
    dimB = 2**(L - LA)

    entropies = np.zeros(n_eig)

    for n in range(n_eig):
        psi_full = np.zeros(2**L, dtype=complex)
        for i, b in enumerate(basis):
            psi_full[b] = eigvecs[i, n]

        psi_mat = psi_full.reshape(dimA, dimB)
        rho_A = psi_mat @ psi_mat.conj().T
        evals = linalg.eigvalsh(rho_A)
        evals_pos = evals[evals > 1e-14]
        S = -np.sum(evals_pos * np.log(evals_pos))
        entropies[n] = S

    return entropies

def find_neel_state(basis, L):
    """Find the Neel state |1010...> in the basis."""
    neel_bits = ''.join(['1' if i % 2 == 0 else '0' for i in range(L)])
    neel_alt = ''.join(['0' if i % 2 == 0 else '1' for i in range(L)])
    neel_int = int(neel_bits, 2)
    neel_alt_int = int(neel_alt, 2)
    for i, b in enumerate(basis):
        if b == neel_int or b == neel_alt_int:
            return i
    return None

def find_w_states(basis, L, alpha):
    """Find W-state-like initial states as in Kerschbaumer 2025."""
    w_candidates = []
    for idx, b in enumerate(basis):
        s = bits_to_str(b, L)
        n_exc = s.count('1')
        if 2 <= n_exc <= 4:  # Few excitations
            # Check if excitions are spread out (W-like)
            exc_positions = [i for i, c in enumerate(s) if c == '1']
            min_dist = min((exc_positions[i+1] - exc_positions[i]) % L
                          for i in range(len(exc_positions)-1))
            if min_dist >= alpha + 1:  # Satisfies blockade
                w_candidates.append(idx)
    return w_candidates

# ============================================================
# Deep analysis for L=16
# ============================================================

print("=" * 70)
print("DEEP ANALYSIS: PXP-alpha QMBS Classification")
print("=" * 70)

for alpha in [1, 2]:
    for L in [16]:
        print(f"\n{'='*60}")
        print(f"alpha={alpha}, L={L}")
        print(f"{'='*60}")

        basis = build_pxp_basis(L, alpha, pbc=True)
        D = len(basis)
        print(f"D={D}")

        H, _ = build_pxp_hamiltonian(L, alpha, Omega=1.0, Delta=0.0, pbc=True)
        eigvals, eigvecs = linalg.eigh(H.toarray())

        # Compute entropies for all states
        print(f"Computing entropies for all {D} eigenstates...")
        entropies = compute_all_entropies(eigvecs, basis, L)

        # Plot entropy vs energy scatter (text-based)
        print(f"\nEntropy statistics:")
        print(f"  S_min={entropies.min():.3f}, S_max={entropies.max():.3f}, "
              f"S_mean={entropies.mean():.3f}, S_std={entropies.std():.3f}")

        # Find top outliers
        edge_cut = D // 20
        n_window = D // 6
        outlier_data = []
        for i in range(edge_cut, D - edge_cut):
            w_start = max(edge_cut, i - n_window // 2)
            w_end = min(D - edge_cut, i + n_window // 2)
            w_ent = [entropies[j] for j in range(w_start, w_end) if j != i]
            if len(w_ent) < 5:
                continue
            mu, sigma = np.mean(w_ent), np.std(w_ent)
            if sigma > 1e-10:
                z = (entropies[i] - mu) / sigma
                if z < -2.0:  # Low-entropy outlier
                    s = bits_to_str(basis[i], L)
                    outlier_data.append({
                        'idx': i, 'E': eigvals[i], 'S': entropies[i],
                        'z': z, 'n_exc': s.count('1'),
                        'state': s
                    })

        outlier_data.sort(key=lambda x: x['z'])

        # Find Neel state overlap with eigenstates
        neel_idx = find_neel_state(basis, L)
        if neel_idx is not None:
            print(f"\nNeel state overlap analysis:")
            print(f"  Neel state index in basis: {neel_idx}")
            # Compute overlap of each eigenstate with Neel state
            overlaps = np.abs(eigvecs[neel_idx, :])**2
            top_overlaps = np.argsort(overlaps)[::-1][:10]
            print(f"  Top 10 eigenstates with Neel overlap:")
            for rank, idx in enumerate(top_overlaps):
                S = entropies[idx]
                s = bits_to_str(basis[idx], L)
                print(f"    #{rank+1}: E={eigvals[idx]:.4f}, "
                      f"S={S:.4f}, overlap={overlaps[idx]:.4f}, "
                      f"state={s[:8]}... n_exc={s.count('1')}")

        # W-state analysis
        w_indices = find_w_states(basis, L, alpha)
        print(f"\nW-state-like candidates in basis: {len(w_indices)}")

        # Check Kerschbaumer known families:
        # For alpha=1: Z_2 state (Neel) should have revival with omega ~ 2*Omega
        # Expect equally spaced eigenstates with high Neel overlap

        print(f"\n--- Scar Tower Analysis ---")
        # Find eigenstates with significant Neel overlap
        if neel_idx is not None:
            overlaps = np.abs(eigvecs[neel_idx, :])**2
            scar_thresh = 0.01
            high_overlap = np.where(overlaps > scar_thresh)[0]
            high_overlap_sorted = high_overlap[np.argsort(overlaps[high_overlap])[::-1]]

            print(f"  States with Neel overlap > {scar_thresh}: {len(high_overlap)}")
            print(f"  Top 8 by overlap:")
            for rank, idx in enumerate(high_overlap_sorted[:8]):
                print(f"    idx={idx}: E={eigvals[idx]:.4f}, "
                      f"S={entropies[idx]:.4f}, "
                      f"overlap={overlaps[idx]:.4f}")

            # Check equidistance among top high-overlap states
            if len(high_overlap_sorted) >= 3:
                top = high_overlap_sorted[:8]
                top_energies = eigvals[top]
                spacings = np.diff(top_energies)
                print(f"\n  Energy spacings between top-overlap states:")
                print(f"  {[f'{s:.4f}' for s in spacings]}")
                mu_s = np.mean(spacings)
                sigma_s = np.std(spacings)
                print(f"  Mean spacing: {mu_s:.4f}, std: {sigma_s:.4f}")
                if sigma_s > 1e-12 and mu_s > 1e-12:
                    print(f"  Q (mu/sigma): {mu_s/sigma_s:.2f}")
                    print(f"  This corresponds to oscillation period T = 2*pi/omega = {2*np.pi/mu_s:.2f}")

print("\n" + "="*70)
print("Analysis complete.")
