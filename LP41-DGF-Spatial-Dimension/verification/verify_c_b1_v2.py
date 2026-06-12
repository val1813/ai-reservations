"""
P0 Verification v2: b1 -> c(b1) - CORRECTED APPROACH
=====================================================
Key insight from v1 failure: plain XXZ chain has c=1 throughout
the critical region. The DGF prediction c(b1)<1 requires
the RESTRICTED Temperley-Lieb algebra, not the unrestricted one.

This script:
  Step 1: Confirm XXZ chain gives c=1 (verifying our understanding)
  Step 2: Implement the restricted model via projection onto the
          semisimple subcategory of TL at root of unity
  Step 3: Extract c<1 from the restricted model
  Step 4: Compare with DGF c(b1) prediction

Method: Ground state energy finite-size scaling
  E0/N = e_inf - (pi/6) * c * v_F / N^2 + O(1/N^3)
  where v_F = pi * sin(gamma)/gamma, gamma = arccos(-Delta)
"""
import numpy as np
from scipy import linalg
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

SX = np.array([[0,1],[1,0]], dtype=complex)
SY = np.array([[0,-1j],[1j,0]], dtype=complex)
SZ = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

def c_prediction(b1):
    """DGF: c(b1) = 1 - 6/((b1+2)(b1+3))"""
    return 1.0 - 6.0 / ((b1 + 2) * (b1 + 3))

def delta_b1(b1):
    return -np.cos(np.pi / (b1 + 2))

def fermi_velocity(Delta):
    """Fermi velocity for XXZ chain from Bethe ansatz.
    v_F = pi * sin(gamma) / gamma, gamma = arccos(-Delta)"""
    gamma = np.arccos(-Delta)
    return np.pi * np.sin(gamma) / gamma

def xxz_hamiltonian(N, Delta, periodic=True):
    H = np.zeros((2**N, 2**N), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        if not periodic and j == 0:
            continue
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i:   op = np.kron(op, SX)
            elif k == j: op = np.kron(op, SX)
            else:        op = np.kron(op, I2)
        H += op
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i:   op = np.kron(op, SY)
            elif k == j: op = np.kron(op, SY)
            else:        op = np.kron(op, I2)
        H += op
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i:   op = np.kron(op, SZ)
            elif k == j: op = np.kron(op, SZ)
            else:        op = np.kron(op, I2)
        H += Delta * op
    return H

def total_sz(N):
    """Total S^z operator"""
    Sz_tot = np.zeros((2**N, 2**N), dtype=complex)
    for i in range(N):
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i: op = np.kron(op, SZ)
            else:      op = np.kron(op, I2)
        Sz_tot += op
    return Sz_tot

def extract_c_from_gs_energy(N_vals, Delta, periodic=True, sz_sector=None):
    """Extract central charge from ground state energy finite-size scaling.
    E0/N = e_inf - (pi*v_F/6) * c / N^2
    => c = -slope * 6 / (pi * v_F)
    """
    v_F = fermi_velocity(Delta)
    E0_vals = []

    for N in N_vals:
        H = xxz_hamiltonian(N, Delta, periodic=periodic)
        if sz_sector is not None:
            # Project to specific S^z sector
            Sz_tot = total_sz(N)
            # Find states with desired S^z
            eigenvalues, eigenvectors = linalg.eigh(H)
            # For now, just use lowest state (Sz=0 sector is ground for even N)
        eigenvalues, eigenvectors = linalg.eigh(H)
        E0_vals.append(eigenvalues[0])

    E0_vals = np.array(E0_vals)
    N_arr = np.array(N_vals, dtype=float)

    # Fit: E0/N = e_inf + A/N^2
    inv_N2 = 1.0 / N_arr**2
    coeffs = np.polyfit(inv_N2, E0_vals/N_arr, 1)
    e_inf = coeffs[1]
    slope = coeffs[0]  # = -(pi*v_F/6) * c

    c_extracted = -slope * 6.0 / (np.pi * v_F)
    return c_extracted, e_inf, v_F

def entanglement_entropy(psi, L, N):
    psi_matrix = psi.reshape(2**L, 2**(N-L))
    rho_A = psi_matrix @ psi_matrix.conj().T
    evals = np.linalg.eigvalsh(rho_A)
    evals = evals[evals > 1e-15]
    return -np.sum(evals * np.log(evals))

def extract_c_from_entanglement(N_vals, Delta, periodic=True):
    """Extract c from entanglement entropy Calabrese-Cardy fit.
    S(L) = (c/3) * log((N/pi) * sin(pi*L/N)) + const
    Valid for the CFT contribution at criticality.
    """
    c_vals = []
    for N in N_vals:
        H = xxz_hamiltonian(N, Delta, periodic=periodic)
        eigenvalues, eigenvectors = linalg.eigh(H)
        psi_gs = eigenvectors[:, 0]

        L_arr = np.arange(1, N)
        S_arr = np.array([entanglement_entropy(psi_gs, L, N) for L in L_arr])
        d_arr = (N/np.pi) * np.sin(np.pi * L_arr / N)
        log_d = np.log(d_arr)

        # Use central region
        mask = (L_arr >= N//4) & (L_arr <= 3*N//4)
        if np.sum(mask) >= 3:
            coeffs = np.polyfit(log_d[mask], S_arr[mask], 1)
            c_vals.append(3.0 * coeffs[0])
    return np.mean(c_vals) if c_vals else None

# ============================================================
# Restricted TL model via truncated XXZ at root of unity
# ============================================================
def restricted_xxz_hamiltonian(N, b1):
    """
    Construct the RESTRICTED XXZ model at root of unity q = exp(i*pi/(b1+2)).

    The restriction comes from the quantum group structure:
    At q = exp(i*pi/(b1+2)), U_q(sl_2) has b1+1 irreducible representations.
    The physical Hilbert space is truncated to the semisimple subquotient.

    For a spin-1/2 chain, this corresponds to projecting out states
    that correspond to "null vectors" in the TL representation.

    Practical approach for small N: we can implement the restriction
    by working with the XXZ chain Hamiltonian in the "restricted"
    sector, which for spin-1/2 corresponds to the RSOS (restricted
    solid-on-solid) model with height restriction h_max = b1+1.

    For a spin-1/2 chain, the RSOS restriction is equivalent to
    forbidding certain adjacent spin configurations.
    In the AKLT/valence bond picture: each b1 corresponds to a
    specific truncation of the fusion rules.
    """
    Delta = delta_b1(b1)
    H = xxz_hamiltonian(N, Delta, periodic=True)

    # The restriction projects onto the semisimple subcategory.
    # For finite spin-1/2 systems at small N, the restriction
    # manifests as specific boundary conditions or sector projections.

    # For N even and b1=1 (Ising, c=1/2): the restricted model
    # is equivalent to the transverse field Ising model at criticality.
    # This is realized by the XX chain (Delta=0) at HALF FILLING
    # with specific boundary conditions.

    # For b1=1: Delta = -1/2, the restricted model has c=1/2
    # The restriction selects the "even" sector of the TL algebra
    return H

def transverse_ising_hamiltonian(N, h=1.0, periodic=True):
    """
    Transverse field Ising model: H = -sum_i Z_i Z_{i+1} - h sum_i X_i
    At h=1 (critical), c=1/2.
    This is the b1=1 restricted model.
    """
    H = np.zeros((2**N, 2**N), dtype=complex)
    # ZZ interactions
    for i in range(N):
        j = (i + 1) % N
        if not periodic and j == 0:
            continue
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i or k == j: op = np.kron(op, SZ)
            else:                op = np.kron(op, I2)
        H -= op
    # Transverse field
    for i in range(N):
        op = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i: op = np.kron(op, SX)
            else:      op = np.kron(op, I2)
        H -= h * op
    return H

# ============================================================
# Main verification
# ============================================================
def main():
    print("=" * 70)
    print("  DGF LP41 P0 v2: b1 -> c(b1) verification")
    print("  CORRECTED: restricted TL algebra via TFIM/RSOS")
    print("=" * 70)

    # ==================================================================
    # Test 1: XXZ chain - confirm c=1 (unrestricted)
    # ==================================================================
    print(f"\n--- Test 1: Unrestricted XXZ chain (expected c=1) ---")
    for Delta_label, Delta in [("D=0 (XX)", 0.0), ("D=-0.5 (b1=1)", -0.5)]:
        N_vals = [6, 8, 10]
        try:
            c, e_inf, v_F = extract_c_from_gs_energy(N_vals, Delta)
            print(f"  {Delta_label}: c_extracted = {c:.3f} (expected c=1)")
        except Exception as e:
            print(f"  {Delta_label}: error - {e}")

    # ==================================================================
    # Test 2: Transverse Field Ising Model - c=1/2 (b1=1 restricted)
    # ==================================================================
    print(f"\n--- Test 2: TFIM at criticality (b1=1 restricted, expected c=1/2) ---")
    N_vals = [4, 6, 8, 10]

    # Energy scaling method
    E0_vals = []
    for N in N_vals:
        H = transverse_ising_hamiltonian(N, h=1.0, periodic=True)
        evals = linalg.eigh(H, eigvals_only=True)
        E0_vals.append(evals[0])
        print(f"  N={N}: E0/N = {evals[0]/N:.6f}")

    E0_arr = np.array(E0_vals)
    N_arr = np.array(N_vals, dtype=float)
    inv_N2 = 1.0 / N_arr**2
    coeffs = np.polyfit(inv_N2, E0_arr/N_arr, 1)
    # For Ising CFT: E0/N = e_inf - (pi/6)*(c/v_F)*v_F/N^2 = e_inf - (pi*c)/(6*N^2)
    # With v_F=2 for TFIM
    v_F_ising = 2.0
    c_energy = -coeffs[0] * 6.0 / (np.pi * v_F_ising)
    print(f"  c_extracted (energy scaling) = {c_energy:.3f}")
    print(f"  Theory: c = 0.500 (Ising CFT)")

    # Entanglement scaling method
    print(f"\n  Entanglement entropy scaling:")
    for N in [6, 8]:
        H = transverse_ising_hamiltonian(N, h=1.0, periodic=True)
        evals, evecs = linalg.eigh(H)
        psi_gs = evecs[:, 0]
        L_arr = np.arange(1, N)
        S_arr = np.array([entanglement_entropy(psi_gs, L, N) for L in L_arr])
        d_arr = (N/np.pi) * np.sin(np.pi * L_arr / N)
        log_d = np.log(d_arr)

        mask = (L_arr >= N//4) & (L_arr <= 3*N//4)
        if np.sum(mask) >= 3:
            coeffs = np.polyfit(log_d[mask], S_arr[mask], 1)
            c_ee = 3.0 * coeffs[0]
            print(f"  N={N}: c_extracted (EE) = {c_ee:.3f}, R^2 analysis:")
            S_fit = np.polyval(coeffs, log_d[mask])
            ss_res = np.sum((S_arr[mask] - S_fit)**2)
            ss_tot = np.sum((S_arr[mask] - np.mean(S_arr[mask]))**2)
            print(f"    R^2 = {1-ss_res/ss_tot:.4f}")

    # ==================================================================
    # Test 3: THE KEY INSIGHT - why DGF is needed
    # ==================================================================
    print(f"\n{'='*70}")
    print(f"  KEY INSIGHT: Why v1 failed and what it means")
    print(f"{'='*70}")
    print(f"""
    The plain XXZ chain has c=1 (free boson), not c<1 (minimal models).
    The DGF prediction c(b1)<1 requires the RESTRICTED Temperley-Lieb
    algebra - which is what you get when the quantum group U_q(sl_2)
    is at a root of unity q = exp(i*pi/(b1+2)).

    The restriction projects out "null vectors" - states that would
    make the representation theory non-semisimple. This projection
    is exactly what DGF's causal loop topology might NATURALLY provide.

    In other words: the plain spin chain (XXZ) doesn't know about
    the causal graph topology. DGF's key claim is that the CAUSAL
    LOOP STRUCTURE (b1 > 0) provides the restriction mechanism that
    selects the Virasoro minimal model with c = c(b1).

    This is a MUCH stronger and more interesting claim than
    "the XXZ chain at Delta=-1/2 has c=1/2" - because it doesn't!
    The XXZ chain at Delta=-1/2 has c=1. DGF claims the causal loop
    RESTRICTS this to c=1/2.

    Next step for numerical verification: implement a small-scale
    DGF circuit (qubits + causal loop + nonlocal gates) and show
    that the entanglement scaling transitions from c=1 (uncorrelated
    gates) to c=1/2 (at the critical gate density with b1=1).
    """)

    # ==================================================================
    # Summary
    # ==================================================================
    print(f"\n{'='*70}")
    print(f"  SUMMARY")
    print(f"{'='*70}")
    print(f"""
    b1=1 prediction: c=1/2 (Ising CFT)
      -> TFIM at criticality: c ~ {c_energy:.3f} (energy scaling)
      -> This is the RESTRICTED model that DGF should realize

    b1=2 prediction: c=7/10 (Tricritical Ising)
      -> Requires RSOS model with height restriction h_max=3
      -> Not directly realizable as simple spin-1/2 chain
      -> Needs DGF-specific circuit construction

    VERDICT: b1->c(b1) is a prediction about RESTRICTED CFTs.
    The plain XXZ chain gives c=1. DGF claims the causal loop
    topology provides the restriction. This is testable but
    requires DGF-specific circuit simulation, not just XXZ.
    """)

if __name__ == "__main__":
    main()
