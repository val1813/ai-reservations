"""
LP38 理论预测 — 4节点空间环: 比例测试 + 轴测试
本地计算，不需要IBM Q。提供论文中所有理论数字。

输出:
  协议1 比例测试: R = QCMI(pi/8)/QCMI(pi/4)
    LP38 (theta^2 log):  R = 0.48
    CCQ (theta^4):        R = 0.0625
    差距: 7.7x

  协议2 轴测试: QCMI(RZZ对齐) vs QCMI(RXX+ZZ失配)
    对齐:   1.09 bits
    失配:   2.26 bits
    差距:   2.06x

  轴扫描: phi = 0 -> pi/2, QCMI单调增长 1.09 -> 2.26
"""
import numpy as np
from scipy.linalg import expm
import json

I2 = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)
PAULI = [I2, X, Y, Z]

def kron_rev(mats):
    r = mats[-1]
    for m in reversed(mats[:-1]): r = np.kron(m, r)
    return r

def vn_entropy(rho):
    w = np.linalg.eigvalsh(rho); w = np.maximum(w, 1e-15)
    return -np.sum(w * np.log2(w))

def partial_trace(rho, keep_bits, n_total=6):
    keep = sorted(keep_bits); tr = sorted([i for i in range(n_total) if i not in keep])
    dk = 2**len(keep); res = np.zeros((dk,dk), dtype=complex)
    for a in range(dk):
        for ap in range(dk):
            bk=0; bk_ap=0
            for ki,q in enumerate(keep): bk|=((a>>ki)&1)<<q; bk_ap|=((ap>>ki)&1)<<q
            total=0j
            for b in range(2**len(tr)):
                tp=0
                for ti,q in enumerate(tr): tp|=((b>>ti)&1)<<q
                total+=rho[bk|tp, bk_ap|tp]
            res[a,ap]=total
    return res

def permute_qubits(rho, target_axes_bra, n_total=6):
    d=2; target_axes_ket=[a+n_total for a in target_axes_bra]
    rho_t=rho.reshape([d]*(2*n_total))
    rho_t=np.transpose(rho_t, axes=target_axes_bra+target_axes_ket)
    return rho_t.reshape(2**n_total, 2**n_total)

def build_state_and_evolve(cartan_vectors, p=0.7):
    bell_vec=np.array([1,0,0,1],dtype=complex)/np.sqrt(2)
    rho_bell=np.outer(bell_vec,bell_vec.conj())
    gamma=np.diag([p,1-p])
    rho_block=kron_rev([rho_bell,rho_bell,gamma,gamma])
    axes=[2,0,5,3,4,1]; rho_target=permute_qubits(rho_block,axes)
    edge_pairs=[(0,1),(1,2),(2,3),(3,0)]; U_full=np.eye(64,dtype=complex)
    for edge_idx,(a,b) in enumerate(edge_pairs):
        cv=cartan_vectors[edge_idx]
        H_edge=np.zeros((16,16),dtype=complex)
        for k in range(3):
            if abs(cv[k])<1e-15: continue
            op=PAULI[k+1]; bits=[I2]*4; bits[a]=op; bits[b]=op
            term=bits[0]
            for j in range(1,4): term=np.kron(bits[j],term)
            H_edge+=cv[k]*term
        U_edge=expm(-1j*H_edge)
        U_edge_full=np.kron(np.eye(4),U_edge)
        U_full=U_edge_full@U_full
    rho_f=U_full@rho_target@U_full.conj().T
    SR=vn_entropy(partial_trace(rho_f,[4,5]))
    SQ=vn_entropy(partial_trace(rho_f,[0,2]))
    SRQ=vn_entropy(partial_trace(rho_f,[0,2,4,5]))
    SQE=vn_entropy(partial_trace(rho_f,[0,1,2,3]))
    SRQE=vn_entropy(rho_f)
    return max(0.0, SRQ+SQE-SQ-SRQE)

if __name__ == '__main__':
    p = 0.7
    results = {}

    # === PROTOCOL 1: Ratio Test ===
    print('='*60)
    print('PROTOCOL 1: RATIO TEST')
    print('='*60)
    thetas = [np.pi/4, np.pi/8, np.pi/16]
    qcmis = {}
    for theta in thetas:
        cv = [np.array([0,0,theta/2]) for _ in range(4)]
        qcmi = build_state_and_evolve(cv, p)
        qcmis[float(theta)] = qcmi
        ts = f'pi/{int(np.pi/theta)}'
        print(f'  theta={ts}: QCMI = {qcmi:.4f} bits')

    R_LP38 = qcmis[np.pi/8] / qcmis[np.pi/4]
    R_CCQ = (np.pi/8)**4 / (np.pi/4)**4
    print(f'\n  R_LP38 = QCMI(pi/8)/QCMI(pi/4) = {qcmis[np.pi/8]:.4f}/{qcmis[np.pi/4]:.4f} = {R_LP38:.4f}')
    print(f'  R_CCQ  = (pi/8)^4/(pi/4)^4 = {R_CCQ:.4f}')
    print(f'  Gap = {R_LP38/R_CCQ:.1f}x')
    results['ratio_test'] = {'R_LP38': R_LP38, 'R_CCQ': R_CCQ, 'gap': R_LP38/R_CCQ,
                              'qcmis': {str(k): float(v) for k,v in qcmis.items()}}

    # === PROTOCOL 2: Axis Test ===
    print()
    print('='*60)
    print('PROTOCOL 2: AXIS TEST')
    print('='*60)
    cv_zz = [np.array([0,0,np.pi/8]) for _ in range(4)]
    qcmi_aligned = build_state_and_evolve(cv_zz, p)
    cv_mixed = [
        np.array([np.pi/8,0,0]), np.array([0,0,np.pi/8]),
        np.array([np.pi/8,0,0]), np.array([0,0,np.pi/8]),
    ]
    qcmi_misaligned = build_state_and_evolve(cv_mixed, p)
    print(f'  QCMI(aligned, ZZ)  = {qcmi_aligned:.4f} bits')
    print(f'  QCMI(misaligned)   = {qcmi_misaligned:.4f} bits')
    print(f'  Ratio = {qcmi_misaligned/qcmi_aligned:.2f}x')
    results['axis_test'] = {'aligned': qcmi_aligned, 'misaligned': qcmi_misaligned,
                             'ratio': qcmi_misaligned/qcmi_aligned}

    # === Axis Scan ===
    print()
    print('='*60)
    print('AXIS SCAN: QCMI vs Cartan angle phi')
    print('='*60)
    phis = np.linspace(0, np.pi/2, 11)
    scan = {}
    for phi in phis:
        cv = [
            np.array([np.pi/8*np.sin(phi), 0, np.pi/8*np.cos(phi)]),
            np.array([0,0,np.pi/8]),
            np.array([np.pi/8*np.sin(phi), 0, np.pi/8*np.cos(phi)]),
            np.array([0,0,np.pi/8]),
        ]
        qcmi = build_state_and_evolve(cv, p)
        scan[float(phi)] = qcmi
        print(f'  phi={phi/np.pi:.1f}pi ({phi*180/np.pi:3.0f}deg): QCMI={qcmi:.4f}')
    results['axis_scan'] = {str(k): float(v) for k,v in scan.items()}

    # Save
    with open('theory_predictions.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nSaved: theory_predictions.json')
