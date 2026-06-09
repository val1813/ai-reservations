"""
Inspector verification: Explicit CNOT cycle density matrix computation.
Verify A博士's claim: CNOT cycle gives S(E') = 1, I(R;E'|Q') = 1.

No unicode, minimal, verified.
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    n = len(dims)
    keep = sorted(keep)
    trace_out = [i for i in range(n) if i not in keep]
    perm = keep + trace_out
    shape = tuple(dims) + tuple(dims)
    rho_tensor = rho.reshape(shape)
    new_order = list(perm) + [p + n for p in perm]
    rho_permuted = rho_tensor.transpose(new_order)
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_trace = int(np.prod([dims[i] for i in trace_out]))
    rho_reshaped = rho_permuted.reshape(d_keep, d_trace, d_keep, d_trace)
    return np.trace(rho_reshaped, axis1=1, axis2=3)

def qmi(rho_AB, d_A, d_B):
    H_AB = vn_entropy(rho_AB)
    rho_A = ptrace(rho_AB, [0], [d_A, d_B])
    rho_B = ptrace(rho_AB, [1], [d_A, d_B])
    return vn_entropy(rho_A) + vn_entropy(rho_B) - H_AB

def qcmi(rho_ABC, d_A, d_B, d_C):
    H_ABC = vn_entropy(rho_ABC)
    rho_AB = ptrace(rho_ABC, [0, 1], [d_A, d_B, d_C])
    rho_BC = ptrace(rho_ABC, [1, 2], [d_A, d_B, d_C])
    rho_B  = ptrace(rho_ABC, [1], [d_A, d_B, d_C])
    return vn_entropy(rho_AB) + vn_entropy(rho_BC) - vn_entropy(rho_B) - H_ABC

# CNOT gate in computational basis: |c,t> -> |c, t⊕c>
CNOT = np.zeros((4,4), dtype=complex)
CNOT[0,0] = 1.0   # |00> -> |00>
CNOT[1,1] = 1.0   # |01> -> |01>
CNOT[2,3] = 1.0   # |10> -> |11>
CNOT[3,2] = 1.0   # |11> -> |10>

def apply_CNOT(state_vec, control, target, n_qubits):
    """Apply CNOT to state vector using explicit basis expansion."""
    d = 2**n_qubits
    result = np.zeros(d, dtype=complex)
    for i in range(d):
        # Decode binary
        bits = [(i >> k) & 1 for k in range(n_qubits)]
        c_val = bits[control]
        t_val = bits[target]
        new_t = t_val ^ c_val  # XOR
        bits[target] = new_t
        j = sum(bits[k] << k for k in range(n_qubits))
        result[j] += state_vec[i]
    return result

print("="*60)
print("Inspector: Explicit CNOT Cycle Verification")
print("="*60)

# System: R_a, R_b, Q_a, Q_b, E_1, E_2 (6 qubits)
# Indices:   0    1    2    3    4    5
n_qubits = 6
d_total = 2**n_qubits

# Initial state: |Phi+>_{R_a,Q_a} ⊗ |Phi+>_{R_b,Q_b} ⊗ |00>_{E_1,E_2}
# |Phi+> = (|00>+|11>)/sqrt(2)
# |Phi+>_{R_a,Q_a} = (|0,0> + |1,1>)/sqrt(2) * |0,0>_{R_b,Q_b}... wait
# Let me be precise about the state vector

psi = np.zeros(d_total, dtype=complex)
# |Phi+>_{R_a Q_a}: R_a(bit0), Q_a(bit2)
# |Phi+>_{R_b Q_b}: R_b(bit1), Q_b(bit3)
# |00>_{E_1 E_2}: E_1(bit4)=0, E_2(bit5)=0
# Sum over a,b ∈ {0,1}: |a>_{R_a}|a>_{Q_a}|b>_{R_b}|b>_{Q_b}|00>_{E}
for a in range(2):
    for b in range(2):
        idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | (0 << 4) | (0 << 5)
        psi[idx] = 0.5  # 1/sqrt(4) = 0.5 (normalization: sum over a,b)

rho_init = np.outer(psi, psi.conj())

# Verify initial state
rho_RQ = ptrace(rho_init, [0,1,2,3], [2,2,2,2,2,2])
S_RQ_init = vn_entropy(rho_RQ)
print(f"\nInitial S(RQ) = {S_RQ_init:.6f} (should be 0)")

# Apply CNOT gates in order:
# U1: CNOT(Q_a -> E_1)  control=2, target=4
# U2: CNOT(Q_b -> E_1)  control=3, target=4
# U3: CNOT(Q_b -> E_2)  control=3, target=5
# U4: CNOT(Q_a -> E_2)  control=2, target=5
psi_cur = psi.copy()
for name, ctrl, tgt in [("U1: Q_a->E_1", 2, 4), ("U2: Q_b->E_1", 3, 4),
                          ("U3: Q_b->E_2", 3, 5), ("U4: Q_a->E_2", 2, 5)]:
    psi_cur = apply_CNOT(psi_cur, ctrl, tgt, n_qubits)
    # Verify normalization
    norm = np.sum(np.abs(psi_cur)**2)
    print(f"  After {name}: norm={norm:.6f}")

rho_final = np.outer(psi_cur, psi_cur.conj())

# Compute reduced states
# R = indices 0,1; Q' = indices 2,3; E' = indices 4,5
rho_R = ptrace(rho_final, [0,1], [2,2,2,2,2,2])
rho_Qp = ptrace(rho_final, [2,3], [2,2,2,2,2,2])
rho_Ep = ptrace(rho_final, [4,5], [2,2,2,2,2,2])
rho_RQp = ptrace(rho_final, [0,1,2,3], [2,2,2,2,2,2])
rho_QpEp = ptrace(rho_final, [2,3,4,5], [2,2,2,2,2,2])
rho_RQpEp = ptrace(rho_final, [0,1,2,3,4,5], [2,2,2,2,2,2])

S_R = vn_entropy(rho_R)
S_Qp = vn_entropy(rho_Qp)
S_Ep = vn_entropy(rho_Ep)
S_RQp = vn_entropy(rho_RQp)
S_QpEp = vn_entropy(rho_QpEp)
S_RQpEp = vn_entropy(rho_RQpEp)

print(f"\nFinal entropies:")
print(f"  S(R)    = {S_R:.6f}")
print(f"  S(Q')   = {S_Qp:.6f}")
print(f"  S(E')   = {S_Ep:.6f}  <-- Inspector check: A博士 claims = 1")
print(f"  S(RQ')  = {S_RQp:.6f}  <-- Inspector check: should be >0")
print(f"  S(Q'E') = {S_QpEp:.6f}")
print(f"  S(RQ'E')= {S_RQpEp:.6f} (should be 0, pure total state)")

# Compute mutual informations
I_RQp = S_R + S_Qp - S_RQp
I_REp = S_R + S_Ep - vn_entropy(ptrace(rho_final, [0,1,4,5], [2,2,2,2,2,2]))
I_R_QpEp = S_R + S_QpEp - S_RQpEp

# QCMI = I(R;E'|Q')
qcmi_val = qcmi(rho_final, 4, 4, 4)  # d_R=4, d_Q=4, d_E=4
I_RQp_direct = qmi(rho_RQp, 4, 4)

print(f"\nMutual informations:")
print(f"  I(R;Q')     = {I_RQp:.6f}")
print(f"  I(R;Q'E')   = {I_R_QpEp:.6f}")
print(f"  I(R;E'|Q')  = {qcmi_val:.6f}  <-- Inspector check: A博士 claims = 1")
print(f"  Check: 4 - I(R;Q') = {4 - I_RQp:.6f}")
print(f"  Check: I(R;Q'E') - I(R;Q') = {I_R_QpEp - I_RQp:.6f}")

# Direct S(E') check: is it really = 1?
print(f"\nE' eigenvalues: {np.sort(np.linalg.eigvalsh(rho_Ep))[::-1]}")
print(f"\nE' density matrix:")
print(np.round(rho_Ep, 4))

# VERDICT
print(f"\n{'='*60}")
print(f"INSPECTOR VERDICT")
print(f"{'='*60}")
checks = [
    ("S(RQ) initial = 0", abs(S_RQ_init) < 1e-10),
    ("Total state pure (S=0)", abs(S_RQpEp) < 1e-10),
    ("S(E') = 1 (A博士 claim)", abs(S_Ep - 1.0) < 1e-10),
    ("I(R;E'|Q') = 1 (A博士 claim)", abs(qcmi_val - 1.0) < 1e-10),
    ("I(R;Q') = 3", abs(I_RQp - 3.0) < 1e-10),
    ("4 - I(R;Q') = QCMI", abs((4 - I_RQp) - qcmi_val) < 1e-10),
]
for name, ok in checks:
    print(f"  [{('PASS' if ok else 'FAIL')}] {name}")
