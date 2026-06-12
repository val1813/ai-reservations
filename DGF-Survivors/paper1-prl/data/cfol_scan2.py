"""
CFOL sufficiency: clean scan. QCMI = I(R;E'|Q') for aligned 4-node causal ring.
"""
import numpy as np

def von_neumann_entropy(rho, eps=1e-12):
    evals = np.linalg.eigvalsh(rho)
    evals = np.maximum(evals, eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))

def build_kraus(c1, c2, c3, c4, p):
    """K_{s2,s4} diagonal in |s1,s3> basis (sigma_z = computational)."""
    a0 = np.sqrt(p); a1 = np.sqrt(1-p)
    K = []
    for s2v, a2 in [(1, a0), (-1, a1)]:
        for s4v, a4 in [(1, a0), (-1, a1)]:
            K_op = np.zeros((4,4), dtype=complex)
            for idx, (s1, s3) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
                lam = c1*s1*s2v + c2*s2v*s3 + c3*s3*s4v + c4*s4v*s1
                K_op[idx,idx] = a2*a4*np.exp(1j*lam)
            K.append(K_op)
    return K

def qcmi_from_kraus(K_list):
    """QCMI = I(R;E'|Q') where |Psi> = (1/2) sum_i |i>_R sum_k |k>_E K_k|i>_Q."""
    d = 4; de = len(K_list)
    # Build pure state psi[i,k,j] = (K_k)_{j,i} / sqrt(d)
    psi = np.zeros((d, de, d), dtype=complex)
    for i in range(d):
        qi = np.zeros(d, dtype=complex); qi[i] = 1.0
        for k_idx, K in enumerate(K_list):
            psi[i, k_idx, :] = K @ qi
    psi_vec = psi.reshape(-1) / np.sqrt(d)
    rho = np.outer(psi_vec, psi_vec.conj())  # (64,64)
    rho_t = rho.reshape(d, de, d, d, de, d)  # [a,k,j,b,l,m]

    # S(RQ): trace E' (contract k=l: positions 1 and 4)
    rho_RQ = np.einsum('akjbkm->ajbm', rho_t).reshape(d*d, d*d)
    S_RQ = von_neumann_entropy(rho_RQ)

    # S(EQ): trace R (contract a=b: positions 0 and 3)
    rho_EQ = np.einsum('akjalm->kjlm', rho_t).reshape(de*d, de*d)
    S_EQ = von_neumann_entropy(rho_EQ)

    # S(Q): trace RE' (contract a=b and k=l)
    rho_Q = np.einsum('akjakm->jm', rho_t)
    S_Q = von_neumann_entropy(rho_Q)

    return S_RQ + S_EQ - S_Q, S_RQ, S_EQ, S_Q

# ============================================================
print("="*60)
print("CFOL Sufficiency Scan")
print("="*60)

# Test A: c_j in (pi/2)Z at various p -> should be QCMI=0
print("\n--- A: c_j in (pi/2)Z (expected QCMI=0) ---")
for c_list, label in [
    ([0,0,0,0], "all 0"),
    ([np.pi/2]*4, "all pi/2"),
    ([np.pi/2, 0, np.pi/2, 0], "pi/2,0,pi/2,0"),
    ([np.pi/2, np.pi/2, np.pi, -np.pi], "INSPECTOR"),
    ([np.pi]*4, "all pi"),
]:
    for p in [0.3, 0.5, 0.7]:
        qcmi, Srq, Seq, Sq = qcmi_from_kraus(build_kraus(*c_list, p))
        status = "OK" if qcmi < 1e-8 else "FAIL"
        print(f"  {label:25s} p={p}: QCMI={qcmi:.2e} S_RQ={Srq:.4f} {status}")

# Test B: CNOT (all pi/4) — QCMI vs p
print("\n--- B: CNOT (all pi/4) QCMI vs p ---")
print(f"  {'p':>6s}  {'QCMI':>10s}  {'S_RQ':>10s}  {'S_EQ':>10s}  {'S_Q':>10s}")
for p in [0.5, 0.6, 0.7, 0.8, 0.9, 0.99]:
    qcmi, Srq, Seq, Sq = qcmi_from_kraus(build_kraus(np.pi/4, np.pi/4, np.pi/4, np.pi/4, p))
    print(f"  {p:6.4f}  {qcmi:10.6f}  {Srq:10.6f}  {Seq:10.6f}  {Sq:10.6f}")

# Test C: variable c, identical on all edges, p=0.5
print("\n--- C: c uniform, p=0.5, QCMI vs c ---")
for c_n in range(0, 17):
    c = c_n * np.pi / 16
    qcmi, _, _, _ = qcmi_from_kraus(build_kraus(c, c, c, c, 0.5))
    marker = " <-- ZERO" if qcmi < 1e-8 else ""
    print(f"  c={c_n:2d}pi/16: QCMI={qcmi:.6f}{marker}")

# Test D: QCMI vs c1+c2 and c3+c4
print("\n--- D: QCMI=0 manifold (p=0.5, c grid pi/8) ---")
p = 0.5
found = []
for n1 in range(17):
    for n2 in range(17):
        for n3 in range(17):
            for n4 in range(17):
                c = [n*np.pi/16 for n in [n1,n2,n3,n4]]
                qcmi, _, _, _ = qcmi_from_kraus(build_kraus(*c, p))
                if qcmi < 1e-8:
                    found.append((n1,n2,n3,n4, qcmi))
print(f"  Found {len(found)} zero-QCMI configs out of 17^4 = {17**4}")
if len(found) <= 100:
    for c in found[:50]:
        print(f"    c/(pi/16) = ({c[0]:2d},{c[1]:2d},{c[2]:2d},{c[3]:2d}) QCMI={c[4]:.1e}")
else:
    # Summarize patterns
    from collections import Counter
    sums = Counter()
    for n1,n2,n3,n4,_ in found:
        s12 = n1+n2; s34 = n3+n4
        sums[(s12, s34)] += 1
    print(f"  Top (c1+c2, c3+c4) patterns (in pi/16 units):")
    for (s12,s34), cnt in sums.most_common(20):
        print(f"    c1+c2={s12:3d}, c3+c4={s34:3d}: {cnt} configs")

print("\nDone.")
