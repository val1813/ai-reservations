#!/usr/bin/env python3
"""
Multi-plaquette QCMI: Generalize boundary plaquette theorem from single ring
to N adjacent boundary rings.

Physics: 2D square lattice, left half (i<k) rotated (c not in pi/2 Z),
right half (i>=k) non-rotated (c in pi/2 Z). Boundary at x = k-1/2.
N adjacent boundary plaquettes share horizontal edges.

Single-plaquette result:
  QCMI(c,p) = H_2(1/2 + 1/2 sqrt[1 - p(1-p)(4 sin^2(2c) + sin^2(4c))])
  Gram rank = 2, two zero eigenvalues, QCMI in [0,1] bit.

Multi-plaquette model: Ising chain with 2-state per plaquette (from rank-2 Gram).
Coupling gamma(c,p) from shared-edge constraint.
On-site gap epsilon(c,p) from single-plaquette QCMI.
"""

import numpy as np
from scipy.linalg import eigvalsh
from scipy.special import entr
import sys
import os

# ==============================================================================
# Section 1: Single Plaquette (verification)
# ==============================================================================

def f_geom(c):
    """Geometric factor f(c) = 4 sin^2(2c) + sin^2(4c)."""
    return 4.0 * np.sin(2.0 * c) ** 2 + np.sin(4.0 * c) ** 2


def delta_qcmi(c, p):
    """
    delta = sqrt(1 - p(1-p) f(c))
    Controls eigenvalue splitting of single-plaquette Gram matrix.
    delta=0 -> maximally mixed -> QCMI=1 bit (c=pi/4, p=1/2)
    delta=1 -> pure -> QCMI=0 bit (c=0 or p=0,1)
    """
    arg = 1.0 - p * (1.0 - p) * f_geom(c)
    return np.sqrt(max(0.0, arg))


def qcmi_single(c, p):
    """QCMI for a single boundary plaquette. Returns value in [0, 1] bits."""
    d = delta_qcmi(c, p)
    lam = 0.5 + 0.5 * d  # larger eigenvalue of reduced density matrix
    if lam <= 0.0 or lam >= 1.0:
        return 0.0
    return -lam * np.log2(lam) - (1.0 - lam) * np.log2(1.0 - lam)


def single_plaquette_spectrum(c, p):
    """
    Return eigenvalues of single-plaquette reduced density matrix (4x4).
    Nonzero eigenvalues: [(1+delta)/2, (1-delta)/2]
    Zero eigenvalues: [0, 0] (from Gram rank=2)
    """
    d = delta_qcmi(c, p)
    p0 = 0.5 * (1.0 + d)  # larger
    p1 = 0.5 * (1.0 - d)  # smaller
    return np.array([p0, p1, 0.0, 0.0])


def epsilon_onsite(c, p):
    """
    On-site energy gap epsilon for the Ising-chain entanglement Hamiltonian.
    From single-plaquette spectrum: p1/p0 = (1-delta)/(1+delta) = exp(-epsilon)
    So epsilon = log((1+delta)/(1-delta)).
    epsilon=0 -> doubly degenerate on-site -> maximal QCMI.
    epsilon large -> pure ground state -> zero QCMI.
    """
    d = delta_qcmi(c, p)
    if d >= 1.0 - 1e-15:
        return 20.0  # effectively infinite gap
    if d <= 1e-15:
        return 0.0
    return np.log((1.0 + d) / (1.0 - d))


def gamma_coupling(c, p, kappa=1.0):
    """
    Inter-plaquette coupling gamma from shared-edge constraint.

    Physical motivation:
    - Shared edge in rotated region (angle c) constrains adjacent plaquette states.
    - Constraint strength proportional to sin^2(2c): vanishes at c=0,pi/2 (no
      rotation, no coupling) and maximal at c=pi/4.
    - Factor p(1-p) accounts for state mixedness: pure states (p=0,1) have
      no fluctuations to couple.

    gamma(c,p) = kappa * sin^2(2c) * p(1-p) * 4
    (The factor 4 normalizes so max gamma = kappa at c=pi/4, p=1/2.)

    kappa ~ O(1) is a model parameter; we test sensitivity with kappa in {0.25, 0.5, 1, 2}.
    """
    return kappa * np.sin(2.0 * c) ** 2 * p * (1.0 - p) * 4.0


# ==============================================================================
# Section 2: Exact Diagonalization for N plaquettes (N <= 12)
# ==============================================================================

def build_hamiltonian_sparse(N, eps, gam):
    """
    Build entanglement Hamiltonian for N-plaquette Ising chain.

    H(s_1,...,s_N) = eps * sum_i s_i + gam * sum_i (s_i - s_{i+1})^2

    s_i in {0, 1}. eps = on-site gap. gam = coupling.

    Returns: (energies, degeneracies) for all 2^N states.
    """
    n_states = 2 ** N
    energies = np.zeros(n_states)

    # Convert state index to binary configuration
    for idx in range(n_states):
        # Extract bits
        s = np.zeros(N, dtype=int)
        tmp = idx
        for i in range(N):
            s[i] = tmp & 1
            tmp >>= 1

        # On-site energy
        E = eps * np.sum(s)

        # Nearest-neighbor interaction
        for i in range(N - 1):
            if s[i] != s[i + 1]:
                E += gam

        energies[idx] = E

    return energies


def qcmi_from_energies(energies):
    """
    Compute QCMI = von Neumann entropy of rho = exp(-H)/Z
    where H has eigenvalues given by `energies`.

    S = -sum_i (e^{-E_i}/Z) log_2(e^{-E_i}/Z)
      = log_2(Z) + (1/Z) sum_i E_i e^{-E_i} / ln(2)
      = log_2(Z) + <E> / ln(2)
    """
    # Shift by minimum energy for numerical stability
    E_min = np.min(energies)
    E_shifted = energies - E_min

    # Boltzmann weights (beta=1 for entanglement Hamiltonian)
    log_w = -E_shifted
    log_w_max = np.max(log_w)
    w = np.exp(log_w - log_w_max)  # normalized to avoid overflow
    Z = np.sum(w)
    p = w / Z

    # von Neumann entropy in bits
    # S = -sum p_i log_2(p_i)
    entropy = 0.0
    for pi in p:
        if pi > 1e-15:
            entropy -= pi * np.log2(pi)

    return entropy


def qcmi_exact_n(N, c, p, kappa=1.0):
    """Compute QCMI for N adjacent boundary plaquettes via exact diagonalization."""
    eps = epsilon_onsite(c, p)
    gam = gamma_coupling(c, p, kappa)
    energies = build_hamiltonian_sparse(N, eps, gam)
    return qcmi_from_energies(energies)


# ==============================================================================
# Section 3: Transfer Matrix for Large N
# ==============================================================================

def transfer_matrix(eps, gam):
    """
    Build 2x2 transfer matrix for the Ising chain.

    T(s, s') = exp(-eps*(s+s')/2 - gam*(s-s')^2)

    T = [[1,            exp(-eps/2 - gam)],
         [exp(-eps/2 - gam), exp(-eps)      ]]
    """
    T = np.array([
        [1.0, np.exp(-eps / 2.0 - gam)],
        [np.exp(-eps / 2.0 - gam), np.exp(-eps)]
    ])
    return T


def transfer_matrix_free_energy(eps, gam):
    """
    Compute eigenvalues and eigenvectors of transfer matrix.
    Returns eigenvalues [lambda_+, lambda_-] sorted descending.
    Also returns eigenvectors for boundary computations.
    """
    T = transfer_matrix(eps, gam)
    evals, evecs = np.linalg.eigh(T)
    # Sort descending
    idx = np.argsort(evals)[::-1]
    return evals[idx], evecs[:, idx]


def qcmi_from_transfer_paths(N, eps, gam):
    """
    Compute QCMI exactly via transfer matrix path summation.

    For each of the 2^N states, compute the unnormalized log-probability:
      log P(s) = log v[s₀] + Σᵢ log T[sᵢ,sᵢ₊₁] + log v[s_{N-1}]
    where v[a] = exp(-h(a)/2) and T[a,b] = exp(-h(a)/2 - J(a,b) - h(b)/2).

    This gives exact probabilities without numerical derivatives.
    For N ≤ 15, 2^N ≤ 32768, computation is fast.
    For N > 15, falls back to asymptotic density * N.
    """
    if N <= 0:
        return 0.0

    if N > 15:
        # Use asymptotic density for very large N
        return qcmi_density_asymptotic(eps, gam) * N

    n_states = 2 ** N
    log_probs = np.zeros(n_states)

    v = np.array([1.0, np.exp(-eps / 2.0)])
    T = transfer_matrix(eps, gam)
    log_v = np.log(v)
    log_T = np.log(T)

    for idx in range(n_states):
        # Extract bits
        s = [(idx >> i) & 1 for i in range(N)]

        # log P(s) = log v[s₀] + Σᵢ log T[sᵢ,sᵢ₊₁] + log v[s_{N-1}]
        # Note: T already includes half on-site energies for both sites
        # so the product v[s₀] T[s₀,s₁] ... T[s_{N-2},s_{N-1}] v[s_{N-1}]
        # = exp(-h(s₀)/2) exp(-h(s₀)/2-J(s₀,s₁)-h(s₁)/2) ... exp(-h(s_{N-1})/2)
        # = exp(-h(s₀)-J(s₀,s₁)-h(s₁)-J(s₁,s₂)-...-h(s_{N-1}))
        # = exp(-H(s))
        log_p = log_v[s[0]] + log_v[s[N-1]]
        for i in range(N - 1):
            log_p += log_T[s[i], s[i + 1]]
        log_probs[idx] = log_p

    # Normalize
    log_p_max = np.max(log_probs)
    probs = np.exp(log_probs - log_p_max)
    probs /= np.sum(probs)

    # Entropy in bits
    entropy = 0.0
    for p in probs:
        if p > 1e-15:
            entropy -= p * np.log2(p)

    return entropy


# ==============================================================================
# Section 4: Asymptotic Analysis (N -> infinity)
# ==============================================================================

def qcmi_density_asymptotic(eps, gam):
    """
    Compute QCMI per plaquette in the thermodynamic limit (N -> infinity).

    For the 1D Ising chain, the entropy density in the thermodynamic limit is:
    s = lim_{N->infty} S/N

    Using transfer matrix:
    F = -log Z / N -> -log(lambda_max) as N -> infinity.
    U = <E>/N is the energy density.

    For the Ising chain with Hamiltonian H = eps sum s_i + gam sum (s_i-s_{i+1})^2:
    The partition function per site is determined by the largest eigenvalue of T.

    The reduced density matrix in the TDL is well-approximated by the
    stationary distribution of the transfer matrix.

    Entropy density s = lim S/N can be computed from:
    - The dominant eigenvectors of T (left and right)
    - The single-site and two-site marginal probabilities

    Specifically:
    P(s_i = a) = L_a R_a / (L^T R)  (from left and right dominant eigenvectors)
    P(s_i=a, s_{i+1}=b) = L_a T_{ab} R_b / (lambda_max * L^T R)

    Then the entropy density is:
    s = -sum_{a,b} P(a,b) log_2 P(a,b) + sum_a P(a) log_2 P(a)
      = I(s_i : s_{i+1}) (mutual information between adjacent sites)
      = -sum_a P(a) log_2 P(a) [single-site entropy] + ... wait, need more care

    Actually, the entropy density of a 1D Markov chain is:
    s = H(s_i | s_{i-1}) = H(s_i, s_{i-1}) - H(s_{i-1})
      = -sum_{a,b} P(a,b) log_2 P(a,b) + sum_a P(a) log_2 P(a)
    where the second sum uses the marginal, not conditional.

    Let me use the standard formula:
    s = -sum_{a,b} mu(a) T_norm(a,b) log_2 T_norm(a,b)
    where mu is the stationary distribution and T_norm is the normalized
    transfer matrix (stochastic matrix).
    """
    T = transfer_matrix(eps, gam)
    evals, evecs = np.linalg.eigh(T)
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:, idx]

    lambda_max = evals[0]
    vR = evecs[:, 0]  # Right dominant eigenvector
    vL = evecs[:, 0]  # Left = right for symmetric T

    # Ensure positivity
    vR = np.abs(vR)
    vR = vR / np.sum(vR)

    # Stationary distribution (single-site marginal)
    # P(a) = vL[a] * vR[a] (since T is symmetric, vL = vR)
    P1 = vR ** 2
    P1 = P1 / np.sum(P1)

    # Two-site marginal
    # P(a,b) = vL[a] * T[a,b] * vR[b] / lambda_max
    P2 = np.outer(vR, vR) * T / lambda_max
    P2 = P2 / np.sum(P2)

    # Single-site entropy
    H1 = 0.0
    for p in P1:
        if p > 1e-15:
            H1 -= p * np.log2(p)

    # Two-site entropy
    H2 = 0.0
    for a in range(2):
        for b in range(2):
            p = P2[a, b]
            if p > 1e-15:
                H2 -= p * np.log2(p)

    # Entropy density: s = H2 - H1 (conditional entropy)
    entropy_density = H2 - H1
    return max(0.0, entropy_density)


def correlation_length(eps, gam):
    """
    Correlation length of the Ising chain.

    xi = 1 / log(lambda_max / lambda_2nd)
    where lambda_max, lambda_2nd are the two eigenvalues of the transfer matrix.

    xi determines the length scale over which plaquettes are correlated.
    For N << xi: effectively independent (area law with full coefficient).
    For N >> xi: saturated (sub-area-law).
    """
    evals, _ = transfer_matrix_free_energy(eps, gam)
    if evals[1] <= 0:
        return float('inf')
    ratio = evals[0] / evals[1]
    if ratio <= 1.0 + 1e-15:
        return float('inf')
    return 1.0 / np.log(ratio)


# ==============================================================================
# Section 5: Main Analysis
# ==============================================================================

def analyze_point(c, p, kappa=1.0, N_max=12):
    """Full analysis at a given (c, p) point."""
    eps = epsilon_onsite(c, p)
    gam = gamma_coupling(c, p, kappa)
    q1 = qcmi_single(c, p)

    print(f"\n{'='*70}")
    print(f"Analysis point: c = {c:.4f} ({c/np.pi*180:.1f} deg), p = {p:.4f}")
    print(f"  Single-plaquette QCMI: {q1:.6f} bits")
    print(f"  delta = {delta_qcmi(c,p):.6f}")
    print(f"  epsilon (on-site gap) = {eps:.6f}")
    print(f"  gamma (coupling) = {gam:.6f}")
    print(f"  gamma/epsilon = {gam/eps if eps > 1e-10 else float('inf'):.6f}")
    xi = correlation_length(eps, gam)
    print(f"  Correlation length xi = {xi:.3f} plaquettes")

    # Exact diagonalization for N = 1..min(N_max, 12)
    N_vals = list(range(1, min(N_max, 12) + 1))
    qcmi_vals = []
    for N in N_vals:
        qN = qcmi_exact_n(N, c, p, kappa)
        qcmi_vals.append(qN)

    print(f"\n  {'N':>4s}  {'QCMI(N)':>12s}  {'QCMI(N)/N':>12s}  {'N*QCMI(1)':>12s}  {'Ratio':>10s}")
    print(f"  {'-'*4}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*10}")
    for N, qN in zip(N_vals, qcmi_vals):
        additive = N * q1
        ratio = qN / additive if additive > 1e-15 else 1.0
        print(f"  {N:4d}  {qN:12.6f}  {qN/N:12.6f}  {additive:12.6f}  {ratio:10.6f}")

    # Asymptotic density
    s_density = qcmi_density_asymptotic(eps, gam)
    print(f"\n  Asymptotic QCMI density (N->inf): {s_density:.6f} bits/plaquette")
    print(f"  Single-plaquette QCMI:            {q1:.6f} bits/plaquette")
    print(f"  Ratio (asymptotic/single):        {s_density/q1 if q1 > 1e-15 else 1.0:.6f}")

    return {
        'c': c, 'p': p, 'kappa': kappa,
        'eps': eps, 'gam': gam, 'xi': xi,
        'qcmi_1': q1,
        'N_vals': N_vals,
        'qcmi_vals': qcmi_vals,
        'density': s_density,
    }


def scan_parameter_space(kappa=1.0):
    """Scan c-p parameter space and report QCMI additivity."""
    print("\n" + "=" * 70)
    print("PARAMETER SPACE SCAN: QCMI(N) vs N for various (c, p)")
    print("=" * 70)

    # Key points in parameter space
    points = [
        # (c, p, description)
        (np.pi / 4, 0.5, "Maximal single-QCMI (c=pi/4, p=1/2)"),
        (np.pi / 8, 0.5, "Intermediate c (c=pi/8, p=1/2)"),
        (np.pi / 16, 0.5, "Small c (c=pi/16, p=1/2)"),
        (np.pi / 4, 0.25, "Max c, asymmetric p (c=pi/4, p=0.25)"),
        (np.pi / 4, 0.1, "Max c, near-pure p (c=pi/4, p=0.1)"),
        (np.pi / 8, 0.25, "Intermediate c, p (c=pi/8, p=0.25)"),
    ]

    results = []
    for c, p, desc in points:
        print(f"\n--- {desc} ---")
        res = analyze_point(c, p, kappa)
        results.append(res)

    return results


def scan_kappa_dependence():
    """Test sensitivity to coupling strength kappa."""
    print("\n" + "=" * 70)
    print("KAPPA SENSITIVITY: QCMI(N) for different coupling strengths")
    print("=" * 70)

    c, p = np.pi / 4, 0.5  # Maximal single-QCMI point
    kappa_vals = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]
    N_max = 12

    print(f"\n  c = {c:.4f} ({c/np.pi*180:.1f} deg), p = {p:.4f}")
    print(f"  Single-plaquette QCMI = {qcmi_single(c,p):.6f} bits")
    print(f"\n  {'kappa':>8s}  {'eps':>10s}  {'gam':>10s}  {'xi':>10s}  ", end="")
    for N in range(1, N_max + 1):
        print(f"{'N='+str(N):>10s}  ", end="")
    print(f"{'dens':>10s}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*10}  ", end="")
    for N in range(1, N_max + 1):
        print(f"{'-'*10}  ", end="")
    print(f"{'-'*10}")

    for kappa in kappa_vals:
        eps = epsilon_onsite(c, p)
        gam = gamma_coupling(c, p, kappa)
        xi = correlation_length(eps, gam)
        density = qcmi_density_asymptotic(eps, gam)

        print(f"  {kappa:8.3f}  {eps:10.4f}  {gam:10.4f}  {xi:10.3f}  ", end="")
        for N in range(1, N_max + 1):
            qN = qcmi_exact_n(N, c, p, kappa)
            print(f"{qN:10.6f}  ", end="")
        print(f"{density:10.6f}")


def verify_area_law(kappa=1.0):
    """
    Verify if QCMI(N) follows area law (proportional to N) or volume law.

    Area law: QCMI(N) ~ sigma * N  (sigma = surface density)
    Volume law: QCMI(N) ~ sigma * N^2
    Logarithmic: QCMI(N) ~ sigma * N * log(N)

    We fit: QCMI(N) = a * N^b and check if b ~ 1 (area law).

    Also check if QCMI(N)/N converges to a constant.
    """
    print("\n" + "=" * 70)
    print("AREA LAW VERIFICATION")
    print("=" * 70)

    points = [
        (np.pi / 4, 0.5, "Maximal QCMI"),
        (np.pi / 8, 0.5, "Intermediate"),
        (np.pi / 16, 0.5, "Small rotation"),
        (np.pi / 4, 0.25, "Asymmetric p"),
    ]

    for c, p, desc in points:
        eps = epsilon_onsite(c, p)
        gam = gamma_coupling(c, p, kappa)
        xi = correlation_length(eps, gam)
        q1 = qcmi_single(c, p)

        N_vals = np.arange(1, 13)
        qcmi_vals = np.array([qcmi_exact_n(N, c, p, kappa) for N in N_vals])

        # Fit: log QCMI = log a + b * log N
        log_N = np.log(N_vals)
        log_Q = np.log(qcmi_vals)
        coeffs = np.polyfit(log_N, log_Q, 1)
        b = coeffs[0]  # scaling exponent
        a = np.exp(coeffs[1])

        # Fit: QCMI/N = sigma_inf + const/N (convergence test)
        density_vals = qcmi_vals / N_vals
        # Fit sigma(N) = sigma_inf + C/N
        inv_N = 1.0 / N_vals
        coeffs2 = np.polyfit(inv_N[-4:], density_vals[-4:], 1)  # Use last 4 points
        sigma_inf = coeffs2[1]  # intercept = lim_{N->inf} QCMI/N

        # Asymptotic from transfer matrix
        sigma_tm = qcmi_density_asymptotic(eps, gam)

        print(f"\n  {desc}: c={c:.4f}, p={p:.4f}")
        print(f"    Single QCMI: {q1:.6f} bits")
        print(f"    Correlation length xi: {xi:.3f}")
        print(f"    Scaling exponent b: {b:.4f} (b=1 -> area law, b=2 -> volume law)")
        print(f"    QCMI(1)/1 = {qcmi_vals[0]:.6f}")
        print(f"    QCMI(12)/12 = {density_vals[-1]:.6f}")
        print(f"    sigma_inf (extrapolated): {sigma_inf:.6f}")
        print(f"    sigma_TM (transfer matrix): {sigma_tm:.6f}")
        print(f"    sigma_inf / QCMI(1): {sigma_inf/q1 if q1>0 else 0:.4f}")

        if abs(b - 1.0) < 0.1:
            law_type = "AREA LAW (b ~ 1)"
        elif b < 0.5:
            law_type = "SUB-AREA (saturation)"
        elif b > 1.5:
            law_type = "SUPER-AREA / VOLUME-LIKE"
        else:
            law_type = f"INTERMEDIATE (b={b:.3f})"
        print(f"    Verdict: {law_type}")


# ==============================================================================
# Section 6: Physical Mechanism Analysis
# ==============================================================================

def analyze_interference(c= np.pi/4, p=0.5, kappa=1.0):
    """
    Analyze whether multi-plaquette QCMI shows:
    - Additivity: QCMI(2) = 2 * QCMI(1)
    - Destructive interference: QCMI(2) < 2 * QCMI(1)
    - Constructive interference: QCMI(2) > 2 * QCMI(1)
    """
    print("\n" + "=" * 70)
    print("INTERFERENCE ANALYSIS: N=2 vs 2*N=1")
    print("=" * 70)

    q1 = qcmi_single(c, p)
    eps = epsilon_onsite(c, p)
    gam = gamma_coupling(c, p, kappa)

    # N=2 exact: 4 states
    energies_2 = build_hamiltonian_sparse(2, eps, gam)
    q2 = qcmi_from_energies(energies_2)

    # Also compute from transfer matrix
    q2_tm = qcmi_from_transfer_paths(2, eps, gam)

    additive = 2 * q1
    interference = q2 - additive

    print(f"\n  Parameters: c={c:.4f}, p={p:.4f}, kappa={kappa}")
    print(f"  QCMI(1) = {q1:.8f} bits")
    print(f"  QCMI(2) = {q2:.8f} bits (exact diag)")
    print(f"  QCMI(2) = {q2_tm:.8f} bits (transfer matrix)")
    print(f"  2*QCMI(1) = {additive:.8f} bits")
    print(f"  Interference = QCMI(2) - 2*QCMI(1) = {interference:+.8f} bits")

    if interference < -1e-6:
        print(f"  VERDICT: DESTRUCTIVE INTERFERENCE (sub-additive)")
        print(f"  Reduction: {-interference/additive*100:.2f}%")
    elif interference > 1e-6:
        print(f"  VERDICT: CONSTRUCTIVE INTERFERENCE (super-additive)")
        print(f"  Enhancement: {interference/additive*100:.2f}%")
    else:
        print(f"  VERDICT: ADDITIVE (no interference)")

    # Also show the 4-state probabilities for N=2
    print(f"\n  N=2 state probabilities (Ising chain):")
    Z = np.sum(np.exp(-energies_2 + np.min(energies_2)))
    for idx in range(4):
        s0 = idx & 1
        s1 = (idx >> 1) & 1
        prob = np.exp(-energies_2[idx] + np.min(energies_2)) / Z
        print(f"    |{s0}{s1}>: E={energies_2[idx]:.6f}, p={prob:.6f}")

    return q1, q2, interference


def analyze_interference_scan(kappa=1.0):
    """Scan interference across parameter space."""
    print("\n" + "=" * 70)
    print("INTERFERENCE SCAN: QCMI(2) - 2*QCMI(1) across (c,p)")
    print("=" * 70)

    c_vals = np.linspace(0.01, np.pi/2 - 0.01, 10)
    p_vals = np.linspace(0.05, 0.95, 10)

    print(f"\n  {'c/pi':>8s}  {'p':>8s}  {'QCMI(1)':>10s}  {'QCMI(2)':>10s}  {'2*QCMI(1)':>12s}  {'Delta':>10s}  {'Type':>20s}")
    print(f"  {'-'*8}  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*10}  {'-'*20}")

    for c in c_vals:
        for p in p_vals:
            q1 = qcmi_single(c, p)
            eps = epsilon_onsite(c, p)
            gam = gamma_coupling(c, p, kappa)
            energies_2 = build_hamiltonian_sparse(2, eps, gam)
            q2 = qcmi_from_energies(energies_2)
            delta = q2 - 2*q1

            if delta < -1e-6:
                itype = "DESTRUCTIVE"
            elif delta > 1e-6:
                itype = "CONSTRUCTIVE"
            else:
                itype = "ADDITIVE"

            print(f"  {c/np.pi:8.4f}  {p:8.4f}  {q1:10.6f}  {q2:10.6f}  {2*q1:12.6f}  {delta:+10.6f}  {itype:>20s}")


# ==============================================================================
# Section 7: Entanglement spectrum analysis
# ==============================================================================

def entanglement_spectrum(N, c, p, kappa=1.0):
    """
    Compute and display the entanglement spectrum (eigenvalues of
    reduced density matrix) for N plaquettes.
    """
    eps = epsilon_onsite(c, p)
    gam = gamma_coupling(c, p, kappa)
    energies = build_hamiltonian_sparse(N, eps, gam)

    # Boltzmann weights
    E_shifted = energies - np.min(energies)
    w = np.exp(-E_shifted)
    Z = np.sum(w)
    spectrum = w / Z

    # Sort descending
    spectrum = np.sort(spectrum)[::-1]

    # Only show nonzero entries
    nonzero = spectrum[spectrum > 1e-10]

    return nonzero


def analyze_spectrum(c=np.pi/4, p=0.5, kappa=1.0):
    """Analyze entanglement spectrum for N=1,2,3,4."""
    print("\n" + "=" * 70)
    print("ENTANGLEMENT SPECTRUM ANALYSIS")
    print("=" * 70)

    for N in [1, 2, 3, 4, 8]:
        spec = entanglement_spectrum(N, c, p, kappa)
        entropy = -np.sum(spec * np.log2(spec + 1e-300))

        print(f"\n  N={N}: {len(spec)} nonzero eigenvalues, entropy={entropy:.6f} bits")
        print(f"    Top 10 eigenvalues: {spec[:10]}")
        print(f"    Sum of eigenvalues: {np.sum(spec):.10f}")
        print(f"    Effective rank (exp(S)): {2**entropy:.3f}")

        # Compare with independent case
        q1 = qcmi_single(c, p)
        print(f"    Independent entropy: {N*q1:.6f}")
        print(f"    Ratio: {entropy/(N*q1) if N*q1 > 0 else 1:.6f}")


# ==============================================================================
# Section 8: Generate Report Data
# ==============================================================================

def generate_report_data(kappa=1.0):
    """Generate comprehensive data for the report."""
    print("=" * 70)
    print("MULTI-PLAQUETTE QCMI: COMPREHENSIVE ANALYSIS")
    print("=" * 70)

    # 1. Single plaquette verification
    print("\n--- Single Plaquette Verification ---")
    for c_deg in [0, 15, 30, 45, 60, 75, 90]:
        c = c_deg * np.pi / 180
        for p in [0.1, 0.25, 0.5, 0.75, 0.9]:
            q = qcmi_single(c, p)
            if c_deg == 45 and p == 0.5:
                print(f"  c={c_deg} deg, p={p}: QCMI = {q:.6f} bits")

    # 2. N=2 interference
    print("\n--- N=2 Interference Analysis ---")
    for c, p, desc in [
        (np.pi/4, 0.5, "Maximal (c=45deg, p=0.5)"),
        (np.pi/8, 0.5, "Intermediate (c=22.5deg, p=0.5)"),
        (np.pi/4, 0.25, "Asymmetric (c=45deg, p=0.25)"),
    ]:
        q1 = qcmi_single(c, p)
        eps = epsilon_onsite(c, p)
        gam = gamma_coupling(c, p, kappa)
        energies_2 = build_hamiltonian_sparse(2, eps, gam)
        q2 = qcmi_from_energies(energies_2)
        print(f"  {desc}: QCMI(1)={q1:.6f}, QCMI(2)={q2:.6f}, "
              f"2*Q1={2*q1:.6f}, delta={q2-2*q1:+.6f}")

    # 3. N-dependence
    print("\n--- N-Dependence (c=45deg, p=0.5) ---")
    for N in [1, 2, 3, 4, 5, 6, 8, 10, 12]:
        qN = qcmi_exact_n(N, np.pi/4, 0.5, kappa)
        print(f"  N={N:2d}: QCMI={qN:.6f}, QCMI/N={qN/N:.6f}")

    # 4. Asymptotic density
    print("\n--- Asymptotic Density (c=45deg, p=0.5) ---")
    eps = epsilon_onsite(np.pi/4, 0.5)
    gam = gamma_coupling(np.pi/4, 0.5, kappa)
    dens = qcmi_density_asymptotic(eps, gam)
    xi = correlation_length(eps, gam)
    print(f"  eps={eps:.6f}, gam={gam:.6f}, xi={xi:.3f}")
    print(f"  sigma_QCMI (N->inf) = {dens:.6f} bits/plaquette")
    print(f"  sigma_QCMI / QCMI(1) = {dens/qcmi_single(np.pi/4,0.5):.6f}")

    # 5. Area law verification
    print("\n--- Area Law Verification ---")
    for c, p, desc in [
        (np.pi/4, 0.5, "Max QCMI"),
        (np.pi/8, 0.5, "Intermediate"),
        (np.pi/16, 0.5, "Small rotation"),
    ]:
        eps = epsilon_onsite(c, p)
        gam = gamma_coupling(c, p, kappa)
        xi = correlation_length(eps, gam)
        q1 = qcmi_single(c, p)
        dens = qcmi_density_asymptotic(eps, gam)

        Ns = np.arange(1, 13)
        Qs = np.array([qcmi_exact_n(N, c, p, kappa) for N in Ns])
        log_fit = np.polyfit(np.log(Ns), np.log(Qs), 1)
        b = log_fit[0]

        print(f"  {desc}: b={b:.4f}, xi={xi:.2f}, "
              f"sigma_inf/QCMI(1)={dens/q1 if q1>0 else 0:.4f}")

    print("\nDone.")


# ==============================================================================
# Section 9: Main Entry Point
# ==============================================================================

if __name__ == "__main__":
    # Set print options
    np.set_printoptions(precision=6, suppress=True, linewidth=120)

    # Kappa = coupling strength multiplier
    # kappa=0: independent plaquettes (additive QCMI)
    # kappa>0: coupled plaquettes via shared edges
    KAPPA = 1.0

    print("=" * 70)
    print("DGF MULTI-PLAQUETTE QCMI ANALYSIS")
    print("=" * 70)
    print(f"Coupling strength kappa = {KAPPA}")
    print(f"Model: 1D Ising chain with on-site gap epsilon and")
    print(f"nearest-neighbor coupling gamma from shared-edge constraints.")

    # Run all analyses
    generate_report_data(KAPPA)

    print("\n" + "=" * 70)
    print("DETAILED ANALYSIS")
    print("=" * 70)

    analyze_interference(np.pi/4, 0.5, KAPPA)
    analyze_interference(np.pi/8, 0.5, KAPPA)

    scan_kappa_dependence()

    verify_area_law(KAPPA)

    analyze_spectrum(np.pi/4, 0.5, KAPPA)

    analyze_interference_scan(KAPPA)
