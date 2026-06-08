"""
Phase 2: PXP-alpha QMBS exhaustive ED search
LP12-S1: PXP推广模型QMBS完整分类
"""

import numpy as np
from scipy import linalg
from scipy.sparse import lil_matrix, csr_matrix
from itertools import product
import json
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 1. Constrained Hilbert Space Construction
# ============================================================

def build_pxp_basis(L, alpha, pbc=True):
    """Build basis of PXP-alpha constrained Hilbert space.
    Constraint: no two excitations within distance <= alpha.
    Returns: list of bitstrings (as ints), dimension D
    """
    basis = []
    for bits in product([0, 1], repeat=L):
        valid = True
        for i in range(L):
            if bits[i] == 1:
                for d in range(1, alpha + 1):
                    j_right = (i + d) % L if pbc else i + d
                    j_left = (i - d) % L if pbc else i - d
                    if pbc:
                        if bits[j_right] == 1:
                            valid = False; break
                        if bits[j_left] == 1:
                            valid = False; break
                    else:
                        if j_right < L and bits[j_right] == 1:
                            valid = False; break
                        if j_left >= 0 and bits[j_left] == 1:
                            valid = False; break
                if not valid:
                    break
        if valid:
            basis.append(sum(b << (L-1-i) for i, b in enumerate(bits)))
    return sorted(basis)

def bits_to_str(b, L):
    """Convert integer bitstring to binary string."""
    return format(b, f'0{L}b')

def count_excitations(b, L):
    """Count number of excitations (1s) in bitstring."""
    return bin(b).count('1')

# ============================================================
# 2. PXP-alpha Hamiltonian Construction
# ============================================================

def build_pxp_hamiltonian(L, alpha, Omega=1.0, Delta=0.0, pbc=True):
    """Build PXP-alpha Hamiltonian in constrained basis.
    H = sum_i P_i^alpha (Omega * sigma_i^x + Delta * n_i) P_i^alpha
    Using Omega=1 as energy unit.
    """
    basis = build_pxp_basis(L, alpha, pbc)
    D = len(basis)
    H = lil_matrix((D, D), dtype=complex)
    state_to_idx = {b: i for i, b in enumerate(basis)}

    for idx, b in enumerate(basis):
        s = bits_to_str(b, L)
        # Diagonal term: Delta * n_i
        for i in range(L):
            if s[i] == '1':
                # Check if site i is allowed (all neighbors within alpha are empty)
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
                    H[idx, idx] += Delta  # n_i term on excited site

        # Off-diagonal term: Omega * sigma_i^x (flip spin i if constraints allow)
        for i in range(L):
            if s[i] == '1':  # Flip down: |1> -> |0>
                # Check if flipping is allowed (was the excitation originally valid?)
                s_list = list(s)
                s_list[i] = '0'
                new_s = ''.join(s_list)
                new_b = int(new_s, 2)
                if new_b in state_to_idx:
                    H[state_to_idx[new_b], idx] += Omega
                    H[idx, state_to_idx[new_b]] += Omega

            elif s[i] == '0':  # Flip up: |0> -> |1>
                # Check constraints for new excitation at i
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

# ============================================================
# 3. Entanglement Entropy Computation
# ============================================================

def half_chain_entropy(psi, L):
    """Compute half-chain von Neumann entanglement entropy."""
    D = len(psi)
    # Reshape into (2^(L/2), 2^(L/2)) matrix
    LA = L // 2
    LB = L - LA
    dimA = 2**LA
    dimB = 2**LB

    # Embed into full 2^L space (only for the constrained wavefunction)
    # We need to compute rho_A = Tr_B |psi><psi|
    # For small L, we can do this efficiently
    psi_reshaped = psi.reshape(dimA, dimB)
    rho_A = psi_reshaped @ psi_reshaped.conj().T
    # von Neumann entropy
    evals = linalg.eigvalsh(rho_A)
    evals = evals[evals > 1e-15]  # filter positive eigenvalues
    S = -np.sum(evals * np.log(evals))
    return S

def compute_entanglement_entropies(eigvecs, basis, L):
    """Compute half-chain entanglement entropy for all eigenstates.
    Returns array of entropies.
    """
    D = len(basis)
    entropies = np.zeros(D)

    # Create full Hilbert space embedding matrix
    LA = L // 2
    dimA = 2**LA
    dimB = 2**(L - LA)
    basis_arr = np.array(basis)

    for n in range(D):
        # Map constrained wavefunction to full 2^L space
        psi_full = np.zeros(2**L, dtype=complex)
        for i, b in enumerate(basis):
            psi_full[b] = eigvecs[i, n]

        psi_reshaped = psi_full.reshape(dimA, dimB)
        rho_A = psi_reshaped @ psi_reshaped.conj().T
        evals = linalg.eigvalsh(rho_A)
        evals = evals[evals > 1e-15]
        S = -np.sum(evals * np.log(np.maximum(evals, 1e-15)))
        entropies[n] = S

    return entropies

# ============================================================
# 4. Scar Detection: Level 1 (Entanglement Outlier)
# ============================================================

def detect_entanglement_outliers(energies, entropies, n_sigma=3.0, edge_fraction=0.05):
    """Detect entropy outlier eigenstates.
    Uses moving-window method to establish local ETH baseline.
    """
    D = len(energies)
    N_min = max(10, int(0.05 * D))
    edge_cut = int(D * edge_fraction)
    n_window = max(N_min, int(0.15 * D))

    is_outlier = np.zeros(D, dtype=bool)
    outlier_scores = np.zeros(D)

    for i in range(edge_cut, D - edge_cut):
        # Define energy window around i
        start = max(edge_cut, i - n_window // 2)
        end = min(D - edge_cut, i + n_window // 2)
        # Exclude states already marked as outliers
        window_ent = [entropies[j] for j in range(start, end) if not is_outlier[j] and j != i]
        if len(window_ent) < 5:
            continue

        mu = np.mean(window_ent)
        sigma = np.std(window_ent)

        if sigma > 1e-10:
            z_score = abs(entropies[i] - mu) / sigma
            outlier_scores[i] = z_score
            # Relative threshold also
            rel_low = entropies[i] / mu < 0.6 if mu > 0 else False
            if z_score > n_sigma or rel_low:
                is_outlier[i] = True

    return is_outlier, outlier_scores

# ============================================================
# 5. Scar Detection: Level 2 (Spectral Equidistance)
# ============================================================

def check_spectral_equidistance(energies, indices, strong_thresh=5.0, weak_thresh=3.0):
    """Check if a set of eigenstates have equidistant energy spacings."""
    if len(indices) < 3:
        return False, 0.0

    E = energies[sorted(indices)]
    spacings = np.diff(E)
    if len(spacings) < 2:
        return False, 0.0

    mu = np.mean(spacings)
    sigma = np.std(spacings)

    if sigma < 1e-10:
        Q = float('inf')
    else:
        Q = mu / sigma

    if Q > strong_thresh:
        return True, Q
    elif Q > weak_thresh:
        return True, Q  # weak equidistance
    return False, Q

# ============================================================
# 6. Main Search Protocol
# ============================================================

def search_scars_pxp(L, alpha, Omega=1.0, Delta=0.0, pbc=True,
                     n_sigma=3.0, edge_fraction=0.05):
    """Complete PXP-alpha QMBS search protocol.
    Returns dictionary of results.
    """
    print(f"\n{'='*60}")
    print(f"PXP-α={alpha}  QMBS Search: L={L}, PBC={pbc}, Δ/Ω={Delta}")
    print(f"{'='*60}")

    # Step 0: Build basis and Hamiltonian
    basis = build_pxp_basis(L, alpha, pbc)
    D = len(basis)
    print(f"  Hilbert space dimension: {D}")
    print(f"  Excitation counts: {[count_excitations(b, L) for b in basis[:10]]}...")

    H, _ = build_pxp_hamiltonian(L, alpha, Omega, Delta, pbc)
    H_dense = H.toarray()

    # Step 1: Full ED
    print(f"  Diagonalizing {D}x{D} matrix...")
    eigvals, eigvecs = linalg.eigh(H_dense)
    print(f"  ED complete. Energy range: [{eigvals[0]:.4f}, {eigvals[-1]:.4f}]")

    # Step 2: Compute entanglement entropies
    print(f"  Computing entanglement entropies...")
    entropies = compute_entanglement_entropies(eigvecs, basis, L)

    # Step 3: Level 1 - Entanglement outlier detection
    is_outlier, scores = detect_entanglement_outliers(eigvals, entropies, n_sigma, edge_fraction)
    C1_indices = np.where(is_outlier)[0]
    print(f"  Level 1 (entropy outlier): {len(C1_indices)} candidates out of {D} states")

    # Step 4: Level 2 - Spectral equidistance (crude grouping)
    # Try to find equidistant sequences among outliers
    scar_candidates = []
    for idx in C1_indices:
        is_eq, Q = check_spectral_equidistance(eigvals, [idx - 1, idx, idx + 1], 4.0, 2.5)
        if is_eq or Q > 2.0:
            scar_candidates.append({
                'index': int(idx),
                'energy': float(eigvals[idx]),
                'entropy': float(entropies[idx]),
                'z_score': float(scores[idx]),
                'Q_equi': float(Q),
                'excitation_count': count_excitations(basis[idx], L)
            })

    # Sort by outlier score
    scar_candidates.sort(key=lambda x: x['z_score'], reverse=True)

    # Step 5: Find Kerschbaumer-like towers (groups of equally spaced states)
    towers = find_scar_towers(eigvals, entropies, is_outlier, basis, L)

    result = {
        'L': L,
        'alpha': alpha,
        'pbc': pbc,
        'Delta_Omega': Delta,
        'D': D,
        'energy_range': [float(eigvals[0]), float(eigvals[-1])],
        'n_scar_candidates': len(scar_candidates),
        'scar_candidates': scar_candidates[:30],  # Top 30
        'n_towers': len(towers),
        'towers': towers,
        'all_entropies_min': float(np.min(entropies)),
        'all_entropies_max': float(np.max(entropies)),
        'all_entropies_mean': float(np.mean(entropies)),
        'n_C1': len(C1_indices)
    }

    return result

def find_scar_towers(energies, entropies, is_outlier, basis, L):
    """Find approximate scar towers (sequences of ~equally-spaced outlier states)."""
    outlier_indices = np.where(is_outlier)[0]
    if len(outlier_indices) < 3:
        return []

    towers = []
    visited = set()

    for i in range(len(outlier_indices)):
        for j in range(i+2, len(outlier_indices)):
            if i in visited and j in visited:
                continue
            idx_i, idx_j = outlier_indices[i], outlier_indices[j]
            spacing = (energies[idx_j] - energies[idx_i]) / (j - i)
            if abs(spacing) < 1e-10:
                continue

            # Try to extend the sequence
            tower_indices = [idx_i, idx_j]
            for k in range(j+1, len(outlier_indices)):
                idx_k = outlier_indices[k]
                expected_k = energies[tower_indices[-1]] + spacing
                if abs(energies[idx_k] - expected_k) / abs(spacing) < 0.15:
                    tower_indices.append(idx_k)
                    visited.add(k)

            if len(tower_indices) >= 3:
                tower_energies = [float(energies[t]) for t in tower_indices]
                tower_entropies = [float(entropies[t]) for t in tower_indices]
                spacings = np.diff(tower_energies)
                mu_s = np.mean(spacings)
                sigma_s = np.std(spacings)

                towers.append({
                    'indices': [int(t) for t in tower_indices],
                    'energies': tower_energies,
                    'entropies': tower_entropies,
                    'avg_spacing': float(mu_s),
                    'spacing_ratio': float(mu_s / sigma_s) if sigma_s > 1e-12 else float('inf'),
                    'n_states': len(tower_indices)
                })
                visited.add(i)
                visited.add(j)

    # Sort by tower size, then by spacing quality
    towers.sort(key=lambda t: (t['n_states'], t['spacing_ratio']), reverse=True)
    return towers[:10]

# ============================================================
# 7. Main Execution
# ============================================================

if __name__ == '__main__':
    results = {}

    # Focus on most informative cases
    configs = [
        # alpha=1 (standard PXP) for all accessible L
        (12, 1, 0.0),
        (14, 1, 0.0),
        (16, 1, 0.0),
        # alpha=2 (extended blockade) — where B博士 predicts non-SU(2) chance
        (12, 2, 0.0),
        (14, 2, 0.0),
        (16, 2, 0.0),
    ]

    for L, alpha, Delta in configs:
        try:
            result = search_scars_pxp(L, alpha, Omega=1.0, Delta=Delta, pbc=True)
            key = f"L{L}_a{alpha}"
            results[key] = result
            print(f"  [OK] {key}: {result['n_scar_candidates']} candidates, "
                  f"{result['n_towers']} towers (D={result['D']})")
            for t in result['towers']:
                print(f"     Tower {t['n_states']} states, "
                      f"spacing={t['avg_spacing']:.4f}, "
                      f"Q_spacing={t['spacing_ratio']:.1f}")
        except Exception as e:
            print(f"  [FAIL] {key}: {e}")
            import traceback
            traceback.print_exc()

    # Save results
    output = {
        'metadata': {
            'task': 'LP12-S1 Phase 2 ED Search',
            'date': '2026-06-02',
            'protocol': 'A博士 Phase 1 search protocol v1'
        },
        'results': results
    }

    with open('D:/Claude/ai-reservations/LP12-QuantumScar/LP12-S1_PXP-Classification/current/phase2_ed_results.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Phase 2 ED search complete. {len(results)} configurations processed.")
    print(f"Results saved to phase2_ed_results.json")
