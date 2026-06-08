"""
LP12-S3 Phase 2: PXP-alpha QMBS perturbation stability ED study
Systematically test 5 perturbation types on PXP-alpha (alpha=1,2,3)
"""

import numpy as np
from scipy import linalg
from scipy.sparse import lil_matrix, csr_matrix
import json, warnings
warnings.filterwarnings('ignore')

def build_pxp_basis(L, alpha, pbc=True):
    basis = []
    for b in range(2**L):
        bits = [(b >> (L-1-i)) & 1 for i in range(L)]
        valid = True
        for i in range(L):
            if bits[i] == 1:
                for d in range(1, alpha + 1):
                    jr = (i + d) % L if pbc else i + d
                    jl = (i - d) % L if pbc else i - d
                    if pbc:
                        if bits[jr] == 1 or bits[jl] == 1: valid = False; break
                    else:
                        if (jr < L and bits[jr] == 1) or (jl >= 0 and bits[jl] == 1): valid = False; break
                if not valid: break
        if valid: basis.append(b)
    return sorted(basis)

def bits_to_str(b, L): return format(b, f'0{L}b')

def build_full_hamiltonian(L, alpha, Omega=1.0, Delta=0.0, pbc=True,
                           J_heis=0.0, V_ising=0.0, W_disorder=0.0,
                           h_boundary=0.0):
    """Build PXP-alpha Hamiltonian with perturbations."""
    basis = build_pxp_basis(L, alpha, pbc)
    D = len(basis)
    H = lil_matrix((D, D), dtype=float)
    s2i = {b: i for i, b in enumerate(basis)}
    rng = np.random.RandomState(42)

    # Disorder potentials (fixed per site)
    eps = rng.uniform(-1, 1, L) * W_disorder

    for idx, b in enumerate(basis):
        s = bits_to_str(b, L)

        # --- PXP-alpha base Hamiltonian ---
        for i in range(L):
            if s[i] == '1':
                allowed = True
                for d in range(1, alpha+1):
                    jr = (i+d)%L if pbc else i+d
                    jl = (i-d)%L if pbc else i-d
                    if pbc:
                        if s[jr]=='1' or s[jl]=='1': allowed=False; break
                    else:
                        if (jr<L and s[jr]=='1') or (jl>=0 and s[jl]=='1'): allowed=False; break
                if allowed: H[idx,idx] += Delta
            elif s[i] == '0':
                allowed = True
                for d in range(1, alpha+1):
                    jr = (i+d)%L if pbc else i+d
                    jl = (i-d)%L if pbc else i-d
                    if pbc:
                        if s[jr]=='1' or s[jl]=='1': allowed=False; break
                    else:
                        if (jr<L and s[jr]=='1') or (jl>=0 and s[jl]=='1'): allowed=False; break
                if allowed:
                    sl = list(s); sl[i]='1'; ns=''.join(sl); nb=int(ns,2)
                    if nb in s2i: H[s2i[nb],idx]+=Omega; H[idx,s2i[nb]]+=Omega

        # --- Perturbations ---
        # Heisenberg exchange: J * S_i · S_{i+1}
        if J_heis != 0:
            for i in range(L):
                j = (i+1)%L if pbc else i+1
                if pbc or j < L:
                    si = 1 if s[i]=='1' else -1  # sigma^z representation
                    sj = 1 if s[j]=='1' else -1
                    H[idx,idx] += J_heis * 0.25 * si * sj  # S^z_i S^z_j
                    # S^+_i S^-_j + h.c. (flip-flop)
                    if s[i]=='1' and s[j]=='0':
                        allowed = True
                        for d in range(1, alpha+1):
                            jr=(i+d)%L if pbc else i+d; jl=(i-d)%L if pbc else i-d
                            if pbc:
                                if (jr==j and s[jr]=='1') or (jl==j and s[jl]=='1'): pass
                        sl=list(s); sl[i]='0'; sl[j]='1'; ns=''.join(sl); nb=int(ns,2)
                        if nb in s2i: H[s2i[nb],idx] += J_heis*0.5; H[idx,s2i[nb]]+=J_heis*0.5
                    elif s[i]=='0' and s[j]=='1':
                        allowed = True
                        for d in range(1, alpha+1):
                            jr=(i+d)%L if pbc else i+d; jl=(i-d)%L if pbc else i-d
                        sl=list(s); sl[i]='1'; sl[j]='0'; ns=''.join(sl); nb=int(ns,2)
                        if nb in s2i: H[s2i[nb],idx] += J_heis*0.5; H[idx,s2i[nb]]+=J_heis*0.5

        # Ising interaction: V * n_i n_{i+1}
        if V_ising != 0:
            for i in range(L):
                j = (i+1)%L if pbc else i+1
                if pbc or j < L:
                    if s[i]=='1' and s[j]=='1':
                        H[idx,idx] += V_ising

        # Onsite disorder
        if W_disorder != 0:
            for i in range(L):
                if s[i]=='1': H[idx,idx] += eps[i]

        # Boundary field
        if h_boundary != 0:
            if s[0]=='1': H[idx,idx] += h_boundary
            if s[L-1]=='1': H[idx,idx] -= h_boundary

    return csr_matrix(H), basis

def compute_neel_overlap_and_tower(eigvecs, basis, L):
    """Find Neel state overlap and extract scar tower."""
    neel = ''.join(['1' if i%2==0 else '0' for i in range(L)])
    neel_alt = ''.join(['0' if i%2==0 else '1' for i in range(L)])
    neel_int = int(neel,2); neel_alt_int = int(neel_alt,2)

    neel_idx = None
    for i,b in enumerate(basis):
        if b==neel_int or b==neel_alt_int: neel_idx=i; break

    if neel_idx is None: return None

    overlaps = np.abs(eigvecs[neel_idx,:])**2
    scar_thresh = 0.005
    high_ov = np.where(overlaps > scar_thresh)[0]
    high_ov = high_ov[np.argsort(overlaps[high_ov])[::-1]]
    return {'neel_idx': neel_idx, 'overlaps': overlaps,
            'scar_indices': high_ov[:12].tolist(),
            'n_scar': len(high_ov),
            'top_overlaps': overlaps[high_ov[:8]].tolist()}

def compute_fidelity_revival(eigvals, eigvecs, neel_idx):
    """Compute fidelity revival from Neel state."""
    if neel_idx is None: return None
    # F(t) = |<psi0|e^{-iHt}|psi0>|^2 = |sum_i |<i|psi0>|^2 e^{-iE_i t}|^2
    overlaps = np.abs(eigvecs[neel_idx,:])**2
    # Compute F(t) at multiples of pi (approximate revival period for PXP)
    # The revival period T_rev ~ 2*pi/omega where omega ~ 1.3 for PXP
    # For analysis we compute F_max = max_t F(t) using the first few periods
    omega_est = 1.31  # from S1 results
    T_rev = 2*np.pi/omega_est
    times = np.linspace(0, 4*T_rev, 200)
    F = np.zeros(len(times))
    for ti, t in enumerate(times):
        phase = np.exp(-1j*eigvals*t)
        F[ti] = np.abs(np.sum(overlaps * phase))**2
    return {'t_max': float(times[np.argmax(F)]),
            'F_max': float(np.max(F)),
            'F_first_revival': float(F[np.argmin(np.abs(times-T_rev))]),
            'times': times.tolist(), 'F': F.tolist()}

def run_perturbation_scan(L=14, alpha=1):
    """Scan perturbation types and strengths."""
    pert_types = {
        'Heisenberg': {'J_heis': [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]},
        'Ising': {'V_ising': [0.0, 0.1, 0.5, 1.0, 2.0]},
        'disorder': {'W_disorder': [0.0, 0.1, 0.5, 1.0, 2.0]},
        'boundary': {'h_boundary': [0.0, 0.1, 0.5, 1.0, 2.0]},
    }

    results = {}
    for pname, pvals in pert_types.items():
        results[pname] = []
        for pkey, pstrengths in pvals.items():
            for lam in pstrengths:
                kwargs = {'L': L, 'alpha': alpha, 'Omega': 1.0, 'pbc': True}
                kwargs[pkey] = lam
                print(f"  {pname} lambda={lam:.3f}...", end=' ', flush=True)
                H, basis = build_full_hamiltonian(**kwargs)
                eigvals, eigvecs = linalg.eigh(H.toarray())
                scar_data = compute_neel_overlap_and_tower(eigvecs, basis, L)
                if scar_data:
                    fid_data = compute_fidelity_revival(eigvals, eigvecs,
                                                        scar_data['neel_idx'])
                    results[pname].append({
                        'lambda': lam, 'n_scar': scar_data['n_scar'],
                        'F_max': fid_data['F_max'] if fid_data else None,
                        'top_ov': scar_data['top_overlaps'][:4]
                    })
                else:
                    results[pname].append({'lambda': lam, 'n_scar': 0, 'F_max': 0})
                print(f"n_scar={results[pname][-1]['n_scar']}")

    return results

if __name__ == '__main__':
    print("LP12-S3: PXP-alpha Perturbation Stability Phase Diagram")
    print("="*60)

    all_results = {}
    for alpha in [1, 2]:
        print(f"\n--- alpha={alpha}, L=14 ---")
        all_results[f'a{alpha}'] = run_perturbation_scan(L=14, alpha=alpha)

    with open('D:/Claude/ai-reservations/LP12-QuantumScar/LP12-S3_PerturbStability/current/phase2_perturb_results.json',
              'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2)

    print("\nDone! Results saved.")
    # Print summary
    for ak, res in all_results.items():
        print(f"\n{ak}:")
        for pname, scans in res.items():
            if scans:
                alive = [s for s in scans if s.get('n_scar',0) > 0]
                print(f"  {pname}: {len(alive)}/{len(scans)} strengths maintain scars")
                if alive and 'F_max' in alive[0]:
                    print(f"    F_max range: {min(s['F_max'] for s in alive if s['F_max']):.3f} - {max(s['F_max'] for s in alive if s['F_max']):.3f}")
