#!/usr/bin/env python3
"""
Independent Numerical Audit — LP47 QCMI for n=5 Cluster Ring
Auditor: Independent agent (no trust in Dr. A or Dr. B frameworks)
Method: Exact diagonalization, from-scratch construction
"""

import numpy as np
from scipy.linalg import sqrtm, eigvalsh
from scipy.optimize import curve_fit
import sys

np.set_printoptions(precision=15, linewidth=180, suppress=True)

# ============================================================
# 1. GATE DEFINITIONS
# ============================================================
I2  = np.eye(2, dtype=complex)
H   = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CZ  = np.diag([1, 1, 1, -1]).astype(complex)  # |00>,|01>,|10>,|11>

# Pauli Z for single-qubit
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def kron(*mats):
    """Kronecker product of a sequence of matrices."""
    result = mats[0]
    for m in mats[1:]:
        result = np.kron(result, m)
    return result

def gate_on_qubits(gate_2qb, q0, q1, n=5):
    """
    Build the 2^n x 2^n matrix for a 2-qubit gate acting on qubits q0, q1.
    gate_2qb is a 4x4 matrix in the |q0,q1> computational basis.
    We need to embed it into the full 2^n space.
    """
    dim = 2**n
    full_gate = np.eye(dim, dtype=complex)
    for i in range(dim):
        # Extract bits: bit 0 = least significant = qubit 0
        bits = [(i >> q) & 1 for q in range(n)]
        b0, b1 = bits[q0], bits[q1]
        for b0p in [0, 1]:
            for b1p in [0, 1]:
                amp = gate_2qb[2*b0p + b1p, 2*b0 + b1]
                if abs(amp) < 1e-15:
                    continue
                # Build target index
                bits_new = bits.copy()
                bits_new[q0] = b0p
                bits_new[q1] = b1p
                j = sum(bits_new[q] << q for q in range(n))
                full_gate[j, i] = amp
    return full_gate

def single_qubit_gate(gate_1qb, q, n=5):
    """Build 2^n x 2^n matrix for a 1-qubit gate on qubit q."""
    dim = 2**n
    full_gate = np.eye(dim, dtype=complex)
    for i in range(dim):
        bits = [(i >> qq) & 1 for qq in range(n)]
        b = bits[q]
        for bp in [0, 1]:
            amp = gate_1qb[bp, b]
            if abs(amp) < 1e-15:
                continue
            bits_new = bits.copy()
            bits_new[q] = bp
            j = sum(bits_new[qq] << qq for qq in range(n))
            full_gate[j, i] = amp
    return full_gate

# ============================================================
# 2. BUILD CLUSTER RING STATE |C5>
# ============================================================
def build_cluster_ring_state(n=5):
    """
    |C_n> = prod_i CZ_{i,i+1} |+>^⊗n  (with i+1 mod n)
    Equivalently: prod_i H_i prod_i CZ_{i,i+1} |0>^⊗n
    Let's use the direct construction: start from |+>^⊗n, apply CZ gates.
    """
    # Start with |+>^⊗n
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    psi = plus.copy()
    for _ in range(n-1):
        psi = np.kron(psi, plus)
    # psi is now |+>^⊗n as a 2^n vector

    # Apply CZ gates along ring edges
    for i in range(n):
        j = (i + 1) % n
        cz_gate = gate_on_qubits(CZ, i, j, n=n)
        psi = cz_gate @ psi

    return psi

def build_alternate_cluster(n=5):
    """
    Alternate construction: |C_n> = prod_i H_i prod_i CZ_{i,i+1} |0>^⊗n
    Verify both match.
    """
    # Start with |0>^⊗n
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0

    # Apply CZ gates
    for i in range(n):
        j = (i + 1) % n
        cz_gate = gate_on_qubits(CZ, i, j, n=n)
        psi = cz_gate @ psi

    # Apply H on all qubits
    h_all = np.eye(2**n, dtype=complex)
    for i in range(n):
        h_all = single_qubit_gate(H, i, n=n) @ h_all
    psi = h_all @ psi

    return psi

# ============================================================
# 3. PERTURBED STATE |ψ(θ)>
# ============================================================
def build_perturbed_state(theta, n=5):
    """
    |ψ(θ)> = cos(πθ/2)|C_n> + sin(πθ/2) H_0|C_n>
    then normalize.
    H_0 is Hadamard on qubit 0.
    """
    c5 = build_cluster_ring_state(n)

    # H_0 |C_n>
    h0_gate = single_qubit_gate(H, 0, n=n)
    h0_c5 = h0_gate @ c5

    # Overlap
    overlap = np.vdot(c5, h0_c5)  # <C5|H0|C5>

    # Raw superposition
    c = np.cos(np.pi * theta / 2)
    s = np.sin(np.pi * theta / 2)
    psi_raw = c * c5 + s * h0_c5

    # Normalize
    norm2 = c**2 + s**2 + 2*c*s*np.real(overlap)
    psi = psi_raw / np.sqrt(norm2)

    return psi, c5, h0_c5, overlap

# ============================================================
# 4. REDUCED DENSITY MATRIX AND VON NEUMANN ENTROPY
# ============================================================
def partial_trace(psi, keep_qubits, n=5):
    """
    Compute reduced density matrix by tracing out all qubits NOT in keep_qubits.
    psi: 2^n state vector.
    keep_qubits: list of qubit indices to keep.
    Returns: density matrix of dimension 2^{|keep_qubits|}.
    """
    dim_keep = 2**len(keep_qubits)
    rho = np.zeros((dim_keep, dim_keep), dtype=complex)

    keep_set = set(keep_qubits)
    trace_out = [q for q in range(n) if q not in keep_set]

    for i in range(2**n):
        if abs(psi[i]) < 1e-15:
            continue
        for j in range(2**n):
            if abs(psi[j]) < 1e-15:
                continue
            # Extract bits
            bits_i = [(i >> q) & 1 for q in range(n)]
            bits_j = [(j >> q) & 1 for q in range(n)]

            # Check if traced-out qubits match
            match = all(bits_i[q] == bits_j[q] for q in trace_out)
            if not match:
                continue

            # Build indices in the kept subspace
            idx_i = sum(bits_i[q] << (list(keep_qubits).index(q)) for q in keep_qubits)
            idx_j = sum(bits_j[q] << (list(keep_qubits).index(q)) for q in keep_qubits)
            rho[idx_i, idx_j] += psi[i] * np.conj(psi[j])

    return rho

def entropy_vn(rho):
    """von Neumann entropy S(ρ) = -Tr(ρ ln ρ). Natural log (nats)."""
    # Use eigvalsh for Hermitian matrices
    evals = eigvalsh(rho)
    # Filter out tiny negative eigenvalues from numerical noise
    evals = np.maximum(evals, 0)
    # Compute entropy: -sum λ ln λ
    ent = 0.0
    for lam in evals:
        if lam > 1e-15:
            ent -= lam * np.log(lam)
    return ent

# ============================================================
# 5. QCMI COMPUTATION
# ============================================================
def compute_qcmi(psi, A, C, B, n=5):
    """
    Compute QCMI I(A:C|B) for pure global state psi.
    I(A:C|B) = S(ρ_AB) + S(ρ_BC) - S(ρ_B) - S(ρ_ABC)
    Since global state is pure and A∪B∪C = all qubits, S(ρ_ABC) = 0.
    """
    AB = sorted(set(A) | set(B))
    BC = sorted(set(B) | set(C))
    B_only = sorted(set(B))

    rho_AB = partial_trace(psi, AB, n=n)
    rho_BC = partial_trace(psi, BC, n=n)
    rho_B = partial_trace(psi, B_only, n=n)

    S_AB = entropy_vn(rho_AB)
    S_BC = entropy_vn(rho_BC)
    S_B = entropy_vn(rho_B)

    qcmi = S_AB + S_BC - S_B  # S(ρ_ABC) = 0 for pure state with all qubits accounted
    return qcmi, S_AB, S_BC, S_B

# ============================================================
# 6. MAIN COMPUTATION
# ============================================================
def main():
    n = 5
    thetas = [0.0, 0.05, 0.10, 0.15, 0.20]

    partitions = {
        'k=1 (adjacent)': {'A': [0], 'C': [1], 'B': [2, 3, 4]},
        'k=2 (antipodal)': {'A': [0], 'C': [2], 'B': [1, 3, 4]},
    }

    # Verify cluster state constructions match
    c5_method1 = build_cluster_ring_state(n)
    c5_method2 = build_alternate_cluster(n)
    fidelity = np.abs(np.vdot(c5_method1, c5_method2))**2
    print(f"=== Construction Verification ===")
    print(f"Fidelity between two cluster state constructions: {fidelity:.15f}")
    print(f"Cluster state norm: {np.linalg.norm(c5_method1):.15f}")
    print()

    # Precompute cluster state properties
    _, c5, h0_c5, overlap = build_perturbed_state(0.0, n)
    print(f"=== Cluster State Properties ===")
    print(f"<C5|H0|C5> = {overlap.real:.15f} + {overlap.imag:.15f}i")
    print(f"|<C5|H0|C5>| = {np.abs(overlap):.15f}")
    print()

    # Storage for results
    results = {}

    for label, part in partitions.items():
        A = part['A']
        C_ = part['C']
        B = part['B']
        print(f"{'='*70}")
        print(f"PARTITION: {label}")
        print(f"  A = {A}, C = {C_}, B = {B}")
        print(f"{'='*70}")

        results[label] = []
        for theta in thetas:
            psi, _, _, _ = build_perturbed_state(theta, n)
            norm_check = np.linalg.norm(psi)
            qcmi, S_AB, S_BC, S_B = compute_qcmi(psi, A, C_, B, n)

            results[label].append({
                'theta': theta,
                'qcmi': qcmi,
                'S_AB': S_AB,
                'S_BC': S_BC,
                'S_B': S_B,
                'norm': norm_check,
            })

            print(f"θ = {theta:.2f}:")
            print(f"  S(ρ_AB)     = {S_AB:.10f} nats")
            print(f"  S(ρ_BC)     = {S_BC:.10f} nats")
            print(f"  S(ρ_B)      = {S_B:.10f} nats")
            print(f"  S(ρ_ABC)=0  (pure global)")
            print(f"  QCMI        = {qcmi:.10f} nats")
            print(f"  |ψ| check   = {norm_check:.15f}")
            print()

    # ============================================================
    # 7. DELTA QCMI AND FITTING
    # ============================================================
    print(f"{'='*70}")
    print("DELTA QCMI ANALYSIS")
    print(f"{'='*70}")

    for label, data in results.items():
        theta_vals = np.array([d['theta'] for d in data])
        qcmi_vals = np.array([d['qcmi'] for d in data])
        qcmi0 = qcmi_vals[0]  # theta=0 baseline
        delta_qcmi = qcmi_vals - qcmi0

        print(f"\n--- {label} ---")
        print(f"QCMI(0) baseline = {qcmi0:.10f} nats")
        print(f"{'θ':>8s}  {'QCMI(nats)':>14s}  {'ΔQCMI(nats)':>14s}  {'ΔQCMI(bits)':>14s}")
        print("-" * 60)
        for th, q, dq in zip(theta_vals, qcmi_vals, delta_qcmi):
            dq_bits = dq / np.log(2)
            print(f"{th:8.2f}  {q:14.10f}  {dq:14.10f}  {dq_bits:14.10f}")
        print(f"\nΔQCMI(θ=0.10) = {delta_qcmi[2]:.10f} nats = {delta_qcmi[2]/np.log(2):.10f} bits")

        # Fit: ΔQCMI = α × θ² × ln(1/θ) + β × θ²
        # Only fit non-zero theta points (theta > 0)
        mask = theta_vals > 0
        th_fit = theta_vals[mask]
        dq_fit = delta_qcmi[mask]

        def model(theta, alpha, beta):
            """ΔQCMI = α * θ² * ln(1/θ) + β * θ²"""
            th = np.asarray(theta, dtype=float)
            result = np.zeros_like(th)
            for i, t in enumerate(th):
                if t > 0:
                    result[i] = alpha * t**2 * np.log(1.0/t) + beta * t**2
                else:
                    result[i] = 0.0
            return result

        # Initial guess
        p0 = [0.1, 0.0]
        try:
            popt, pcov = curve_fit(model, th_fit, dq_fit, p0=p0, maxfev=10000)
            alpha, beta = popt
            alpha_err, beta_err = np.sqrt(np.diag(pcov))

            # R²
            dq_pred = model(th_fit, alpha, beta)
            ss_res = np.sum((dq_fit - dq_pred)**2)
            ss_tot = np.sum((dq_fit - np.mean(dq_fit))**2)
            r_squared = 1 - ss_res / ss_tot

            print(f"\n  Fit: ΔQCMI = α × θ² × ln(1/θ) + β × θ²")
            print(f"  α = {alpha:.8f} ± {alpha_err:.8f}")
            print(f"  β = {beta:.8f} ± {beta_err:.8f}")
            print(f"  R² = {r_squared:.8f}")

            # Predicted vs actual
            print(f"\n  {'θ':>6s}  {'ΔQCMI(actual)':>16s}  {'ΔQCMI(pred)':>16s}  {'residual':>14s}")
            print("  " + "-" * 60)
            for th, dq_a in zip(th_fit, dq_fit):
                dq_p = model([th], alpha, beta)[0]
                res = dq_a - dq_p
                print(f"  {th:6.2f}  {dq_a:16.10f}  {dq_p:16.10f}  {res:14.3e}")

        except Exception as e:
            print(f"  Fit failed: {e}")
            alpha, beta, r_squared = None, None, None

        results[label].append({
            'alpha': alpha,
            'beta': beta,
            'r_squared': r_squared,
        })

    # ============================================================
    # 8. VERIFY DR. A'S CLAIMS
    # ============================================================
    print(f"\n{'='*70}")
    print("DR. A CLAIM VERIFICATION")
    print(f"{'='*70}")

    # Claim 1: α ≈ 0.244 (k=1)
    alpha_k1 = results['k=1 (adjacent)'][-1]['alpha']
    print(f"\nClaim 1: α ≈ 0.244 for k=1")
    print(f"  Computed α(k=1) = {alpha_k1:.8f}")
    if alpha_k1 is not None:
        diff = abs(alpha_k1 - 0.244)
        print(f"  |α_computed - α_claimed| = {diff:.6f}")
        if diff < 0.01:
            print(f"  VERDICT: CLAIM VERIFIED (within 0.01)")
        elif diff < 0.05:
            print(f"  VERDICT: CLOSE BUT NOT EXACT (±{diff:.4f})")
        else:
            print(f"  VERDICT: CLAIM FALSIFIED")

    # Claim 2: α ≈ -0.1582 (k=2)
    alpha_k2 = results['k=2 (antipodal)'][-1]['alpha']
    print(f"\nClaim 2: α ≈ -0.1582 for k=2")
    print(f"  Computed α(k=2) = {alpha_k2:.8f}")
    if alpha_k2 is not None:
        diff = abs(alpha_k2 - (-0.1582))
        print(f"  |α_computed - α_claimed| = {diff:.6f}")
        if diff < 0.01:
            print(f"  VERDICT: CLAIM VERIFIED (within 0.01)")
        elif diff < 0.05:
            print(f"  VERDICT: CLOSE BUT NOT EXACT (±{diff:.4f})")
        else:
            print(f"  VERDICT: CLAIM FALSIFIED")

    # Claim 3: ΔQCMI(θ=0.10, k=1) = 0.02407 bits
    dq_k1_010 = results['k=1 (adjacent)'][2]['qcmi'] - results['k=1 (adjacent)'][0]['qcmi']
    dq_k1_010_bits = dq_k1_010 / np.log(2)
    print(f"\nClaim 3: ΔQCMI(θ=0.10, k=1) = 0.02407 bits")
    print(f"  Computed ΔQCMI(θ=0.10, k=1) = {dq_k1_010_bits:.8f} bits")
    diff = abs(dq_k1_010_bits - 0.02407)
    print(f"  |computed - claimed| = {diff:.8f}")
    if diff < 0.001:
        print(f"  VERDICT: CLAIM VERIFIED (within 0.001 bits)")
    elif diff < 0.005:
        print(f"  VERDICT: CLOSE BUT NOT EXACT (±{diff:.5f} bits)")
    else:
        print(f"  VERDICT: CLAIM FALSIFIED")

    # Claim 4: R² > 0.98
    r2_k1 = results['k=1 (adjacent)'][-1]['r_squared']
    r2_k2 = results['k=2 (antipodal)'][-1]['r_squared']
    print(f"\nClaim 4: R² > 0.98 for both partitions")
    print(f"  R²(k=1) = {r2_k1:.8f}")
    print(f"  R²(k=2) = {r2_k2:.8f}")
    if r2_k1 is not None and r2_k2 is not None:
        if r2_k1 > 0.98 and r2_k2 > 0.98:
            print(f"  VERDICT: CLAIM VERIFIED (both > 0.98)")
        elif r2_k1 > 0.98:
            print(f"  VERDICT: PARTIALLY TRUE (k=1 > 0.98, k=2 fails)")
        elif r2_k2 > 0.98:
            print(f"  VERDICT: PARTIALLY TRUE (k=2 > 0.98, k=1 fails)")
        else:
            print(f"  VERDICT: CLAIM FALSIFIED (neither > 0.98)")

    # ============================================================
    # 9. W1 VERDICT
    # ============================================================
    print(f"\n{'='*70}")
    print("W1 VERDICT: SIGN OF ΔQCMI(θ=0.10, k=2)")
    print(f"{'='*70}")
    dq_k2_010 = results['k=2 (antipodal)'][2]['qcmi'] - results['k=2 (antipodal)'][0]['qcmi']
    sign = "POSITIVE (+)" if dq_k2_010 > 0 else "NEGATIVE (-)" if dq_k2_010 < 0 else "ZERO"
    print(f"  ΔQCMI(θ=0.10, k=2) = {dq_k2_010:.10f} nats = {dq_k2_010/np.log(2):.10f} bits")
    print(f"  SIGN: {sign}")
    print(f"  W1 JUDGMENT: {sign}")
    if dq_k2_010 < 0:
        print(f"  INTERPRETATION: Negative QCMI indicates genuine quantum information")
        print(f"  scrambling — the conditional mutual information can be negative")
        print(f"  for quantum states, revealing non-classical correlations.")

    # ============================================================
    # 10. DETAILED INTERMEDIATE VALUES TABLE
    # ============================================================
    print(f"\n{'='*70}")
    print("COMPLETE RAW DATA TABLE")
    print(f"{'='*70}")

    for label, data in results.items():
        fit_info = data[-1]
        data_points = data[:-1]
        print(f"\n### {label}")
        print(f"| {'θ':>5s} | {'S(ρ_AB)':>14s} | {'S(ρ_BC)':>14s} | {'S(ρ_B)':>14s} | {'S(ρ_ABC)':>12s} | {'QCMI(nats)':>14s} | {'ΔQCMI(nats)':>14s} |")
        print(f"|{'-'*7}|{'-'*16}|{'-'*16}|{'-'*16}|{'-'*14}|{'-'*16}|{'-'*16}|")
        q0 = data_points[0]['qcmi']
        for d in data_points:
            dq = d['qcmi'] - q0
            print(f"| {d['theta']:5.2f} | {d['S_AB']:14.10f} | {d['S_BC']:14.10f} | {d['S_B']:14.10f} | {'0':>12s} | {d['qcmi']:14.10f} | {dq:14.10f} |")

    print()
    print("AUDIT COMPLETE.")

if __name__ == '__main__':
    main()
