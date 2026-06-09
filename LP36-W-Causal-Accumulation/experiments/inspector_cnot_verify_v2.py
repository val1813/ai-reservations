"""
Inspector CNOT verification v2: Fixed ptrace using explicit basis enumeration.
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace_fixed(rho, keep, dims):
    """Partial trace: explicit basis enumeration. Keep subsystem indices in `keep`."""
    n = len(dims)
    trace_out = [i for i in range(n) if i not in keep]
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_total = int(np.prod(dims))

    # Decode full index -> subsystem multi-indices
    result = np.zeros((d_keep, d_keep), dtype=complex)

    # Precompute strides for encoding/decoding
    strides = [int(np.prod(dims[i+1:])) for i in range(n)]

    def decode(idx):
        """Convert flat index to multi-index tuple."""
        result_list = []
        for i in range(n):
            val = (idx // strides[i]) % dims[i]
            result_list.append(val)
        return tuple(result_list)

    def encode_kept(kept_indices):
        """Encode kept-subsystem indices to flat index in reduced space."""
        kept_dims = [dims[i] for i in keep]
        kept_strides = [int(np.prod(kept_dims[i+1:])) for i in range(len(keep))]
        return sum(kept_indices[i] * kept_strides[i] for i in range(len(keep)))

    for bra_full in range(d_total):
        bra_multi = decode(bra_full)
        bra_kept = tuple(bra_multi[i] for i in keep)
        bra_trace = tuple(bra_multi[i] for i in trace_out)
        bra_kept_idx = encode_kept(bra_kept)

        for ket_full in range(d_total):
            ket_multi = decode(ket_full)
            ket_trace = tuple(ket_multi[i] for i in trace_out)

            # Only accumulate if traced-out indices match
            if bra_trace == ket_trace:
                ket_kept = tuple(ket_multi[i] for i in keep)
                ket_kept_idx = encode_kept(ket_kept)
                result[bra_kept_idx, ket_kept_idx] += rho[bra_full, ket_full]

    return result

def apply_CNOT(state_vec, control, target, n_qubits):
    """Apply CNOT to state vector using explicit basis expansion."""
    d = 2**n_qubits
    result = np.zeros(d, dtype=complex)
    for i in range(d):
        bits = [(i >> k) & 1 for k in range(n_qubits)]
        c_val = bits[control]
        t_val = bits[target]
        new_t = t_val ^ c_val
        bits[target] = new_t
        j = sum(bits[k] << k for k in range(n_qubits))
        result[j] += state_vec[i]
    return result

print("="*60)
print("Inspector CNOT Verification v2 (Fixed ptrace)")
print("="*60)

n_qubits = 6  # R_a, R_b, Q_a, Q_b, E_1, E_2
# Indices:          0    1    2    3    4    5
dims_6 = [2,2,2,2,2,2]

# Initial state: |Phi+>_{R_a,Q_a} ⊗ |Phi+>_{R_b,Q_b} ⊗ |00>_{E}
psi = np.zeros(2**n_qubits, dtype=complex)
for a in range(2):
    for b in range(2):
        idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | (0 << 4) | (0 << 5)
        psi[idx] = 0.5

# Verify initial
rho_init = np.outer(psi, psi.conj())
rho_RQ_init = ptrace_fixed(rho_init, [0,1,2,3], dims_6)
S_RQ_init = vn_entropy(rho_RQ_init)
print(f"Initial S(RQ) = {S_RQ_init:.6f} {'OK' if abs(S_RQ_init)<1e-10 else 'FAIL'}")

# Verify S(R) - should be 2 (two Bell pairs, each R_i has S=1)
rho_R_init = ptrace_fixed(rho_init, [0,1], dims_6)
S_R_init = vn_entropy(rho_R_init)
print(f"Initial S(R) = {S_R_init:.6f} (should be 2 for two Bell pairs)")

# Apply CNOTs
psi_cur = psi.copy()
gates = [
    ("U1: CNOT(Q_a->E_1)", 2, 4),
    ("U2: CNOT(Q_b->E_1)", 3, 4),
    ("U3: CNOT(Q_b->E_2)", 3, 5),
    ("U4: CNOT(Q_a->E_2)", 2, 5),
]
for name, ctrl, tgt in gates:
    psi_cur = apply_CNOT(psi_cur, ctrl, tgt, n_qubits)

rho_final = np.outer(psi_cur, psi_cur.conj())

# Compute all reduced states
rho_R = ptrace_fixed(rho_final, [0,1], dims_6)       # R_a, R_b
rho_Qp = ptrace_fixed(rho_final, [2,3], dims_6)       # Q_a, Q_b
rho_Ep = ptrace_fixed(rho_final, [4,5], dims_6)       # E_1, E_2
rho_RQp = ptrace_fixed(rho_final, [0,1,2,3], dims_6)  # R, Q
rho_QpEp = ptrace_fixed(rho_final, [2,3,4,5], dims_6) # Q, E
rho_RQpEp = ptrace_fixed(rho_final, [0,1,2,3,4,5], dims_6) # all

S_R = vn_entropy(rho_R)
S_Qp = vn_entropy(rho_Qp)
S_Ep = vn_entropy(rho_Ep)
S_RQp = vn_entropy(rho_RQp)
S_QpEp = vn_entropy(rho_QpEp)
S_all = vn_entropy(rho_RQpEp)

print(f"\nFinal entropies:")
print(f"  S(R)     = {S_R:.6f}")
print(f"  S(Q')    = {S_Qp:.6f}")
print(f"  S(E')    = {S_Ep:.6f}  <-- A博士 claims = 1")
print(f"  S(RQ')   = {S_RQp:.6f}")
print(f"  S(Q'E')  = {S_QpEp:.6f}")
print(f"  S(RQ'E') = {S_all:.6f} (should be 0)")

# Mutual informations
I_RQp = S_R + S_Qp - S_RQp
I_R_QpEp = S_R + S_QpEp - S_all
QCMI = I_R_QpEp - I_RQp  # chain rule

print(f"\nMutual informations:")
print(f"  I(R;Q')      = {I_RQp:.6f}")
print(f"  I(R;Q'E')    = {I_R_QpEp:.6f}")
print(f"  I(R;E'|Q')   = {QCMI:.6f}  <-- A博士 claims = 1")
print(f"  Check: {S_R:.1f} - I(R;Q') = {S_R - I_RQp:.6f} (should = QCMI)")
print(f"  Check: 4 - I(R;Q') = {4 - I_RQp:.6f}")

# Verify identity: I(R;E'|Q') = 2*log2(d_R) - I(R;Q') = 4 - I(R;Q')
d_R = 4  # R = 2 qubits
expected_qcmi = 2 * np.log2(d_R) - I_RQp
print(f"  Identity check: QCMI={QCMI:.6f}, expected={expected_qcmi:.6f}")

# E' eigenvalue analysis
eig_Ep = np.sort(np.linalg.eigvalsh(rho_Ep))[::-1]
print(f"\nE' eigenvalues: {eig_Ep}")
print(f"E' rank: {np.sum(eig_Ep > 1e-10)}")

# RQ' eigenvalue analysis
eig_RQp = np.sort(np.linalg.eigvalsh(rho_RQp))[::-1]
print(f"RQ' eigenvalues (>1e-10): {eig_RQp[eig_RQp > 1e-10]}")

print(f"\n{'='*60}")
print(f"VERDICT")
print(f"{'='*60}")
all_ok = True
checks = [
    ("S(RQ)_init = 0 (no QE entanglement)", abs(S_RQ_init) < 1e-10),
    ("S(RQ'E') = 0 (total state pure)", abs(S_all) < 1e-10),
    ("S(R) = 2 (two Bell pairs)", abs(S_R - 2.0) < 1e-10),
    ("S(E') = 1 (A博士 claim)", abs(S_Ep - 1.0) < 1e-6),
    ("I(R;E'|Q') = 1 (A博士 claim)", abs(QCMI - 1.0) < 1e-6),
    ("I(R;Q') = 3", abs(I_RQp - 3.0) < 1e-6),
    ("QCMI = 4 - I(R;Q') (identity)", abs(QCMI - expected_qcmi) < 1e-6),
]
for name, ok in checks:
    all_ok = all_ok and ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

print(f"\n  OVERALL: {'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED'}")
