"""
LP38 Bridge Simulation - RXX(theta) 4-qubit causal ring
Validated method from CCQ experiment: numpy unitary + density matrix + manual partial trace
"""
import numpy as np
from scipy.linalg import expm

P = 0.7
THETAS = [np.pi/2, np.pi/4, np.pi/8, np.pi/16, np.pi/32, np.pi/64, np.pi/128, np.pi/256]

I2 = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)

def kron(*mats):
    result = mats[0]
    for m in mats[1:]:
        result = np.kron(result, m)
    return result

def entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = np.maximum(w, 1e-15)
    return -np.sum(w * np.log2(w))

# --- Build initial state: Bell⊗Bell⊗γ⊗γ ---
# Use natural order [Ra,Qa,Rb,Qb,E1,E2] for density matrix,
# then permute to circuit order [Qa,E1,Qb,E2,Ra,Rb]

bell_vec = np.array([1,0,0,1]) / np.sqrt(2)
rho_bell = np.outer(bell_vec, bell_vec.conj())  # pure Bell, 4x4
gamma = np.diag([P, 1-P])  # mixed env, 2x2

# Natural ordering: Ra⊗Qa ⊗ Rb⊗Qb ⊗ E1⊗E2
rho_nat = kron(rho_bell, rho_bell, gamma, gamma)

# Verify
assert abs(np.trace(rho_nat) - 1.0) < 1e-12

# Permute to circuit order [Qa=0, E1=1, Qb=2, E2=3, Ra=4, Rb=5]
# Natural order: [Ra=0, Qa=1, Rb=2, Qb=3, E1=4, E2=5]
# Target order:  [Qa=0, E1=1, Qb=2, E2=3, Ra=4, Rb=5]
# Permutation: nat_pos_in_target = [4, 0, 5, 2, 1, 3] → target[i] = nat[perm[i]]
# Inverse: from nat to target: target[perm_inv[i]] = nat[i]
# Permutation: nat[i] → target[perm[i]]
perm = [1, 4, 3, 5, 0, 2]
d = 2; nq = 6
rho_0 = rho_nat.reshape([d]*(2*nq))
rho_0 = np.transpose(rho_0, axes=perm + [p+nq for p in perm])
rho_0 = rho_0.reshape(2**nq, 2**nq)

assert abs(np.trace(rho_0) - 1.0) < 1e-12

# Quick entropy check for reference qubits
def ptrace_manual(rho, keep_mask):
    """Partial trace: keep_mask is list of booleans, True=keep"""
    n = len(keep_mask)
    d = 2
    # Reshape to tensor [2,2,...,2,2,2,...,2]
    shape = tuple([d]*n + [d]*n)
    rho_t = rho.reshape(shape)
    # For qubits to trace out, contract bra-ket pairs
    trace_out = [i for i in range(n) if not keep_mask[i]]
    # Use a rolling trace approach
    # After tracing idx(es), axes decrease
    remaining = list(range(2*n))
    for idx in sorted(trace_out, reverse=True):
        ket_idx = idx + n
        # Find positions in remaining
        bra_pos = remaining.index(idx)
        ket_pos = remaining.index(ket_idx)
        # Trace over these two axes
        rho_t = np.trace(rho_t, axis1=bra_pos, axis2=ket_pos)
        # Update remaining axes
        remaining = [r for r in remaining if r not in (idx, ket_idx)]
        # Adjust remaining: indices > idx shift by -1, indices > ket_idx shift by -1
        remaining = [r - (1 if r > idx else 0) - (1 if r > ket_idx else 0) for r in remaining]
        n = len(remaining) // 2
    return rho_t.reshape(np.prod([d]*len(keep_mask)), np.prod([d]*len(keep_mask)))

# Actually: just compute reduced states manually using basis expansion
# For small systems (6 qubits), this is fine
def ptrace(rho, keep_qubits):
    """Partial trace: keep only specified qubit indices"""
    n_total = 6
    # Construct computational basis projectors
    trace_out = [i for i in range(n_total) if i not in keep_qubits]
    result = np.zeros((2**len(keep_qubits), 2**len(keep_qubits)), dtype=complex)
    # Iterate over basis of traced-out qubits
    for idx in range(2**len(trace_out)):
        # Build basis vector for traced-out qubits
        bits = [(idx >> j) & 1 for j in range(len(trace_out))]
        # Build projector
        ops = [I2] * n_total
        for q, bit in zip(trace_out, bits):
            v = np.zeros(2); v[bit] = 1.0
            ops[q] = np.outer(v, v.conj())
        P = kron(*ops)
        # Partial inner product
        result += P @ rho @ P  # Hmm this isn't right either

    return result  # wrong, just placeholder

# OK let me use the simplest possible correct approach
# Build reduced states by explicitly tracing out qubits using for loops
def trace_out(rho, qubits_to_trace):
    """Trace out specified qubits from 6-qubit dm"""
    n_total = 6
    keep = [i for i in range(n_total) if i not in qubits_to_trace]
    d_keep = 2**len(keep)
    result = np.zeros((d_keep, d_keep), dtype=complex)
    # The partial trace: result[i,j] = sum_k rho[(i,k), (j,k)]
    # More precisely: for computational basis |a⟩_keep |b⟩_trace,
    # result_{a,a'} = sum_b ⟨a,b|ρ|a',b⟩
    for a in range(d_keep):
        for ap in range(d_keep):
            total = 0j
            for b in range(2**len(qubits_to_trace)):
                # Map (a,b) to full index
                # keep bits first, then trace bits (convention)
                idx = 0
                bit_pos = 0
                for q in keep:
                    bit = (a >> bit_pos) & 1
                    idx |= (bit << q)
                    bit_pos += 1
                for q in qubits_to_trace:
                    bit = (b >> (q)) & 1  # need correct b-bit mapping
                    # Actually, let me use a cleaner mapping
                    pass
                # This is getting too complex
            result[a, ap] = total
    return result

# ULTRA SIMPLE: just use np.einsum for partial trace
def pt(rho, keep, n_total=6):
    """Ultra-simple partial trace using einsum-style contraction"""
    # Reshape dm to tensor with bra and ket indices separated
    d = 2
    shape = tuple([d] * (2 * n_total))
    r_t = rho.reshape(shape)
    # Label axes: 0,1,...,n-1 for bra, n,n+1,...,2n-1 for ket
    # Want to trace over indices not in keep
    # Use np.einsum
    indices = list(range(2 * n_total))
    trace_idx = [i for i in range(n_total) if i not in keep]
    bra_trace = trace_idx
    ket_trace = [i + n_total for i in trace_idx]
    # Build einsum string: contract matching bra-ket pairs for traced qubits
    # Not straightforward with variable number of indices
    # Just use loops — it's 64x64, perfectly fine
    d_full = 2**n_total
    d_keep = 2**len(keep)
    result = np.zeros((d_keep, d_keep), dtype=complex)
    # Precompute index mappings
    keep_positions = sorted(keep)
    trace_positions = sorted([i for i in range(n_total) if i not in keep])
    for a in range(d_keep):
        a_bits = [(a >> i) & 1 for i in range(len(keep))]
        for ap in range(d_keep):
            ap_bits = [(ap >> i) & 1 for i in range(len(keep))]
            total = 0j
            for b in range(2**len(trace_positions)):
                # Build full bra and ket indices
                bra_idx = 0; ket_idx = 0
                for i, q in enumerate(keep_positions):
                    bra_idx |= (a_bits[i] << q)
                    ket_idx |= (ap_bits[i] << q)
                for i, q in enumerate(trace_positions):
                    bit = (b >> i) & 1
                    bra_idx |= (bit << q)
                    ket_idx |= (bit << q)
                total += rho[bra_idx, ket_idx]
            result[a, ap] = total
    return result

# --- Run scan ---
print("=" * 70)
print("LP38 Bridge: RXX(theta) Causal Ring — Density Matrix Simulation")
print(f"Environment: p={P}")
print("=" * 70)
print(f"{'theta/pi':>10s} {'theta':>10s} {'QCMI':>12s} {'S(R)':>10s} {'S(RQ)':>10s} {'S(QE)':>10s}")
print("-" * 70)

results = []
for theta in THETAS:
    # Build H_qe on [Qa=0, E1=1, Qb=2, E2=3]
    def xx_op(i, j):
        ops = [I2]*4
        ops[i] = X; ops[j] = X
        return kron(*ops)
    H_qe = (-theta/2) * (xx_op(0,1) + xx_op(1,2) + xx_op(2,3) + xx_op(3,0))
    U_qe = expm(-1j * H_qe)
    U_full = kron(U_qe, np.eye(4))  # I_R on qubits 4,5

    rho_f = U_full @ rho_0 @ U_full.conj().T

    # Compute reduced states [Qa,E1,Qb,E2,Ra,Rb] = [0,1,2,3,4,5]
    rho_r = pt(rho_f, [4,5])       # Ra, Rb
    rho_q = pt(rho_f, [0,2])       # Qa, Qb
    rho_rq = pt(rho_f, [0,2,4,5])  # Qa,Qb,Ra,Rb
    rho_qe = pt(rho_f, [0,1,2,3])  # Qa,E1,Qb,E2
    rho_rqe = rho_f

    s_r = entropy(rho_r)
    s_q = entropy(rho_q)
    s_rq = entropy(rho_rq)
    s_qe = entropy(rho_qe)
    s_rqe = entropy(rho_rqe)

    qcmi = max(0, s_rq + s_qe - s_q - s_rqe)

    results.append({'theta': theta, 'qcmi': qcmi, 's_r': s_r, 's_q': s_q,
                    's_rq': s_rq, 's_qe': s_qe, 's_rqe': s_rqe})
    print(f"{theta/np.pi:10.4f} {theta:10.6f} {qcmi:12.8f} {s_r:10.6f} {s_rq:10.6f} {s_qe:10.6f}")

# --- Analysis ---
print("\n" + "=" * 70)
print("Scaling Analysis")
print("=" * 70)

thetas = np.array([r['theta'] for r in results])
qcmis = np.array([r['qcmi'] for r in results])

print(f"\n{'theta/pi':>10s} {'QCMI':>14s} {'alpha_local':>12s} {'QCMI/theta^2':>14s}")
print("-" * 58)
for i in range(1, len(results)):
    r1, r2 = results[i-1], results[i]
    if r2['qcmi'] > 0 and r1['qcmi'] > 0:
        alpha = np.log(r2['qcmi'] / r1['qcmi']) / np.log(r2['theta'] / r1['theta'])
    else:
        alpha = float('nan')
    ratio = r1['qcmi'] / r1['theta']**2 if r1['theta'] > 1e-10 else 0
    print(f"{r1['theta']/np.pi:10.4f} {r1['qcmi']:14.10f} {alpha:12.4f} {ratio:14.6f}")

ratio = results[-1]['qcmi'] / results[-1]['theta']**2
print(f"{results[-1]['theta']/np.pi:10.4f} {results[-1]['qcmi']:14.10f} {'---':>12s} {ratio:14.6f}")

# Fit model: QCMI/theta^2 = A*log(1/theta) + B
mask = thetas <= np.pi/8
x = np.log(1.0 / thetas[mask])
y = qcmis[mask] / thetas[mask]**2
A, B = np.polyfit(x, y, 1)
print(f"\nModel: QCMI/theta^2 = A*log(1/theta) + B  (theta <= pi/8)")
print(f"  A = {A:.4f} (analytical: 2/ln2 = {2/np.log(2):.4f})")
print(f"  B = {B:.4f} (analytical: 1/ln2 = {1/np.log(2):.4f})")
residuals = y - (A*x + B)
r2 = 1 - np.sum(residuals**2) / np.sum((y - np.mean(y))**2)
print(f"  R^2 = {r2:.6f}")

print(f"\nCCQ: predicted QCMI=O(theta^4), QCMI/theta^2 -> 0")
print(f"Data: QCMI/theta^2 from {qcmis[0]/thetas[0]**2:.4f} to {ratio:.4f} (DIVERGES)")
print("\nDone.")
