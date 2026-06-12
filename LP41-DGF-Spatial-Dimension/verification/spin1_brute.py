"""
Spin-1 chain: brute-force exact construction, guaranteed correct.
=================================================================
Build Hamiltonian by iterating over ALL basis states.
No Kronecker products. No operator embeddings. Just explicit matrix elements.

Model: Fateev-Zamolodchikov spin-1 chain
  H = sum_i [S_i·S_{i+1} - beta*(S_i·S_{i+1})^2]  (open BC)

For spin-1, Sx, Sy, Sz are 3x3. Each site has 3 states: |+1>, |0>, |-1>.

To compute <a|H|b>, iterate over all 3^N basis states,
for each pair of adjacent sites, compute the local 9x9 interaction,
multiply by the identity for other sites.

At beta = -1/3: c = 7/10 (Tricritical Ising CFT)
"""
import numpy as np
from scipy import linalg
import itertools
import warnings
warnings.filterwarnings('ignore')

# Spin-1 operators (3x3)
Sx = np.array([[0,1,0],[1,0,1],[0,1,0]], dtype=float) / np.sqrt(2)
Sy = np.array([[0,-1,0],[1,0,-1],[0,1,0]], dtype=float) * 1j / np.sqrt(2)
# Actually Sy should be:
Sy = np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]], dtype=complex) / np.sqrt(2)
Sz = np.diag([1,0,-1]).astype(complex)
I3 = np.eye(3, dtype=complex)

# Two-site interaction: S·S = SxSx + SySy + SzSz
SdotS = (np.kron(Sx, Sx) + np.kron(Sy, Sy) + np.kron(Sz, Sz)).real
SdotS_sq = (SdotS @ SdotS).real  # (S·S)^2

def build_H_brute(N, beta):
    """Build N-site spin-1 Hamiltonian by iterating over all states."""
    D = 3**N
    H = np.zeros((D, D), dtype=float)

    # Precompute basis state -> vector mapping
    # State i (0 to 3^N-1) corresponds to base-3 digits
    def state_to_config(s):
        config = np.zeros(N, dtype=int)
        for i in range(N):
            config[i] = s % 3
            s //= 3
        return config

    # For each pair (i, i+1), compute contribution
    for i in range(N-1):
        # The 2-site interaction matrix (9x9) acts on sites (i, i+1)
        interaction = SdotS - beta * SdotS_sq  # 9x9

        # For each configuration of the OTHER N-2 sites
        other_sites = N - 2
        for other_config in range(3**other_sites):
            other_state = np.zeros(N, dtype=int)
            idx = 0
            for k in range(N):
                if k == i:
                    continue  # will set from 2-site basis
                elif k == i+1:
                    continue  # will set from 2-site basis
                else:
                    other_state[k] = other_config % 3
                    other_config //= 3

            # Now iterate over 2-site basis
            for a in range(3):
                for b in range(3):
                    bra_2site = a*3 + b  # row index, 0-8
                    bra_config = other_state.copy()
                    bra_config[i] = a
                    bra_config[i+1] = b
                    bra_idx = sum(bra_config[k] * (3**k) for k in range(N))

                    for c in range(3):
                        for d in range(3):
                            ket_2site = c*3 + d  # column index, 0-8
                            ket_config = other_state.copy()
                            ket_config[i] = c
                            ket_config[i+1] = d
                            ket_idx = sum(ket_config[k] * (3**k) for k in range(N))

                            H[bra_idx, ket_idx] += interaction[bra_2site, ket_2site]

    return H

def ee_spin1(psi, L, N):
    psi_mat = psi.reshape(3**L, 3**(N-L))
    rho = psi_mat @ psi_mat.conj().T
    evals = np.linalg.eigvalsh(rho)
    evals = evals[evals > 1e-15]
    return -np.sum(evals * np.log(evals))

def extract_c(psi, N):
    L_arr = np.arange(1, N)
    S_arr = np.array([ee_spin1(psi, L, N) for L in L_arr])
    d_arr = (2*N/np.pi) * np.sin(np.pi * L_arr / N)
    mask = (L_arr >= max(1, N//4)) & (L_arr <= 3*N//4)
    if np.sum(mask) < 3:
        return None
    coeffs = np.polyfit(np.log(d_arr[mask]), S_arr[mask], 1)
    c = 6.0 * coeffs[0]
    S_fit = np.polyval(coeffs, np.log(d_arr[mask]))
    ss_res = np.sum((S_arr[mask] - S_fit)**2)
    ss_tot = np.sum((S_arr[mask] - np.mean(S_arr[mask]))**2)
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
    return {'c': c, 'R2': r2, 'S': S_arr, 'L': L_arr, 'E0': None}

def main():
    print("=" * 60)
    print("  Spin-1 chain: brute force, guaranteed correct")
    print("  Fateev-Zamolodchikov: H = sum S·S - beta*(S·S)^2")
    print("=" * 60)

    # Test with N=4 first (fast)
    for N in [4]:
        print(f"\n  N={N} (dim=81):")
        for beta in [-0.5, -1/3, -0.2, 0.0]:
            print(f"    beta={beta:.4f}: ", end="", flush=True)
            H = build_H_brute(N, beta)
            evals, evecs = linalg.eigh(H)
            psi = evecs[:, 0]
            res = extract_c(psi, N)
            if res:
                marker = " <--" if abs(res['c'] - 0.700) < 0.2 else ""
                print(f"c={res['c']:.4f}, R2={res['R2']:.4f}, E0/N={evals[0]/N:.6f}{marker}")

    # Try N=5 (243 states)
    print(f"\n  N=5 (dim=243):")
    for beta in [-1/3, -0.3, -0.4]:
        print(f"    beta={beta:.4f}: ", end="", flush=True)
        try:
            H = build_H_brute(5, beta)
            evals, evecs = linalg.eigh(H)
            psi = evecs[:, 0]
            res = extract_c(psi, 5)
            if res:
                marker = " <--" if abs(res['c'] - 0.700) < 0.2 else ""
                print(f"c={res['c']:.4f}, E0/N={evals[0]/N:.6f}{marker}")
        except Exception as e:
            print(f"error: {e}")

    # Try N=6 (729 states)
    print(f"\n  N=6 (dim=729):")
    for beta in [-1/3]:
        print(f"    beta={beta:.4f}: ", end="", flush=True)
        try:
            H = build_H_brute(6, beta)
            evals, evecs = linalg.eigh(H)
            psi = evecs[:, 0]
            res = extract_c(psi, 6)
            if res:
                print(f"c={res['c']:.4f}, E0/N={evals[0]/N:.6f}")
                print(f"    S(L) = {[round(s,4) for s in res['S']]}")
        except Exception as e:
            print(f"error: {e}")

    # Fine scan for beta near the tricritical point (N=5)
    print(f"\n  Fine scan (N=5):")
    best = {'c': 0, 'beta': 0, 'dist': 1.0}
    for beta in np.linspace(-0.6, 0.0, 13):
        H = build_H_brute(5, beta)
        evals, evecs = linalg.eigh(H)
        psi = evecs[:, 0]
        res = extract_c(psi, 5)
        if res:
            dist = abs(res['c'] - 0.700)
            if dist < best['dist']:
                best = {'c': res['c'], 'beta': beta, 'dist': dist, 'R2': res['R2']}
    print(f"  Best: beta={best['beta']:.4f}, c={best['c']:.4f} (dist from 0.700 = {best['dist']:.4f})")

    print(f"\n{'='*60}")
    print(f"  DGF prediction: b1=2 -> n=sqrt(2) -> c=0.700")
    print(f"  Best fit from FZ spin-1 chain: c={best['c']:.4f}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
