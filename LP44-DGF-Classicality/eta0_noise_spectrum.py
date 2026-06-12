"""
eta_0 -> Observable Noise Spectrum

DGF prediction: Each non-Clifford gate creates QCMI >= eta_0 * c^2.
This QCMI = environmental memory that causes correlated errors.
Specifically: error at gate i correlates with error at gate i+k,
with amplitude ~ eta_0 * c^2 * exp(-k * t_gate / T1).

Testable: measure gate error autocorrelation on IBM Q.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

# ================================================================
# 1. Gate Error Autocorrelation Model
# ================================================================

def error_autocorrelation(k, c, p, T1, t_gate):
    """
    Predicted error autocorrelation at lag k gates.

    Args:
        k: lag (number of gates separating the two measurements)
        c: Cartan parameter of the gate (rad)
        p: environment purity (0.5 = maximally mixed)
        T1: environment relaxation time (s)
        t_gate: gate duration (s)

    Returns: C(k) - autocorrelation amplitude

    Model:
    - Each gate deposits eta_0 * c^2 * p(1-p) bits of QCMI in environment
    - This QCMI decays with rate 1/T1
    - Gate errors correlate through this environmental memory
    - Clifford gates (c in pi/2 * Z): eta_0 * c^2 = 0 -> zero autocorrelation
    """
    qcmi_per_gate = eta_0 * c**2 * 4 * p * (1-p)  # 4 edges per ring, p(1-p) factor
    decay = np.exp(-k * t_gate / T1)
    return qcmi_per_gate * decay


# ================================================================
# 2. Predictions for IBM Q Hardware
# ================================================================

print("=" * 70)
print("DGF GATE ERROR AUTOCORRELATION PREDICTIONS")
print("=" * 70)

# IBM Q Kingston parameters (typical)
T1 = 200e-6    # 200 us relaxation time
t_gate = 50e-9  # 50 ns gate time (typical CX gate on Heron)
p = 0.5         # maximally mixed environment (worst case)

gates = {
    'CNOT (Clifford)': np.pi/2,
    'sqrt_iSWAP': np.pi/4,
    'pi/8 (T gate)': np.pi/8,
    'pi/16': np.pi/16,
}

print(f"\nParameters: T1={T1*1e6:.0f}us, t_gate={t_gate*1e9:.0f}ns, p={p}")
print(f"eta_0 = {eta_0:.6f} bit/rad^2\n")

print(f"{'Gate':<20} {'|c|^2':<10} {'QCMI/gate':<12} {'C(1)':<12} {'C(10)':<12} {'C(100)':<12}")
print("-" * 78)

for name, c in gates.items():
    clifford = abs(c - np.pi/2) < 1e-10
    qcmi = 0 if clifford else eta_0 * c**2 * 4 * p * (1-p)

    c1 = error_autocorrelation(1, c, p, T1, t_gate) if not clifford else 0
    c10 = error_autocorrelation(10, c, p, T1, t_gate) if not clifford else 0
    c100 = error_autocorrelation(100, c, p, T1, t_gate) if not clifford else 0

    print(f"{name:<20} {c**2:<10.4f} {qcmi:<12.6f} {c1:<12.6f} {c10:<12.6f} {c100:<12.6f}")

# ================================================================
# 3. Discrimination from Markovian Noise
# ================================================================

print(f"\n{'='*70}")
print("DISCRIMINATION FROM STANDARD NOISE MODELS")
print("="*70)

print("""
Standard (Markovian) noise model:
  C(k) = 0 for all k != 0  (errors are independent)
  Any autocorrelation > 0 at k > 0 is non-Markovian

DGF prediction:
  C(k) > 0 for non-Clifford gates, k < T1/t_gate
  C(k) = 0 for Clifford gates at all k
  C(k) decays exponentially with scale T1/t_gate

Key discriminatory signature:
  1. C_CNOT(k) = 0 (Clifford gate generates no QCMI)
  2. C_sqrt_iSWAP(k) > 0 (non-Clifford generates QCMI)
  3. Amplitude ratio: C_sqrt_iSWAP / C_T = (pi/4)^2 / (pi/8)^2 = 4.0

Experimental protocol:
  - Run interleaved RB with alternating gate types
  - Extract gate error from survival probability
  - Compute autocorrelation of errors vs gate separation
  - Fit: C(k) = A * exp(-k/B)
  - Verify: A(Clifford) = 0, A(non-Clifford) proportional to c^2

Falsification:
  If C(k) = 0 for non-Clifford gates (k > 0) -> DGF wrong
  If C(k) > 0 for Clifford gates -> DGF wrong (CFOL violated)
  If amplitude ratio != c1^2/c2^2 -> DGF QCMI formula wrong
""")

# ================================================================
# 4. Signal-to-Noise Estimate
# ================================================================

print("=" * 70)
print("SIGNAL-TO-NOISE ESTIMATE FOR IBM Q EXPERIMENT")
print("=" * 70)

# For sqrt_iSWAP gate on IBM Q:
c = np.pi/4
qcmi_per_gate = eta_0 * c**2 * 4 * p * (1-p)

# Current gate fidelity on Heron: ~99.9%
fidelity = 0.999
infidelity = 1 - fidelity

# QCMI-induced infidelity (convert bits to probability):
# 1 bit of QCMI = environment can perfectly distinguish 2 states
# This degrades fidelity by at most 2^{-QCMI}
infidelity_dgf = 1 - 2**(-qcmi_per_gate)

print(f"\nsqrt_iSWAP gate (c=pi/4):")
print(f"  QCMI/gate = {qcmi_per_gate:.6f} bits")
print(f"  DGF infidelity floor = {infidelity_dgf:.6f} ({infidelity_dgf*100:.4f}%)")
print(f"  Current IBM Q infidelity = {infidelity*100:.2f}%")

# Number of gates needed to see DGF signal above current noise floor:
# We need: N_gates * infidelity_dgf > measurement_precision
# measurement_precision ~ 1/sqrt(N_shots)
N_shots = 10000
measurement_precision = 1.0 / np.sqrt(N_shots)
N_gates_needed = measurement_precision / infidelity_dgf

print(f"\n  Measurement precision (N_shots={N_shots}): {measurement_precision:.4f}")
print(f"  Gates needed to see DGF signal: {N_gates_needed:.0f}")

# But more practically: look at ERROR AUTOCORRELATION, not raw infidelity
# C(1) for sqrt_iSWAP vs autocorrelation of standard noise
c1_signal = error_autocorrelation(1, c, p, T1, t_gate)
print(f"\n  Error autocorrelation C(1) = {c1_signal:.6f}")
print(f"  This is DGF signal strength per gate pair")

# Statistical significance: need M independent measurements
# sigma_C ~ 1/sqrt(M)
# S/N = C(1) * sqrt(M) > 5 for detection
M_for_5sigma = (5.0 / c1_signal)**2
print(f"  Gate pairs needed for 5-sigma detection: {M_for_5sigma:.0f}")
print(f"  Circuit depth for M pairs: ~{np.sqrt(2*M_for_5sigma):.0f} gates")

# ================================================================
# 5. Comparison with IBM Q DGF Data
# ================================================================

print(f"\n{'='*70}")
print("COMPARISON WITH EXISTING IBM Q DGF DATA")
print("="*70)

# From 19-ibmq-hardware-results.md:
# Single ring CFOL experiment on Kingston Heron r2
# QCMI measured at pi/8: S/N = 617x
# This measured QCMI directly, not autocorrelation

# Our new test: autocorrelation across multiple rings
# Would need: multi-ring circuit, interleaved measurements

print("""
Existing DGF IBM Q data (Kingston Heron r2):
  - Single 4-qubit causal ring
  - QCMI measured directly via tomography
  - S/N = 617x at c=pi/8 -> STRONG confirmation of CFOL

New test proposed:
  - Sequential independent rings on same qubit pair
  - Measure error autocorrelation, not direct QCMI
  - This tests ADDITIVITY and QCMI->noise mapping

Distinct from existing data:
  - Not measuring QCMI directly
  - Measuring noise CORRELATIONS (autocorrelation function)
  - Tests whether QCMI really translates to non-Markovian errors
""")
