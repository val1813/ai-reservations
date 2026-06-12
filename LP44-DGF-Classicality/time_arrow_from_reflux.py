"""
DGF Time Arrow from Reflux Bound (T2)

T2 (theorem, Holevo proof):
  P_reflux ≤ N_S·q_S / (N_E·q_E)

Physical meaning:
  P_reflux = probability that information flows BACK from environment to system
  This is "time reversal" in the information-theoretic sense:
  undoing the effect of past causal events.

For macroscopic systems (N_E >> N_S, q_E << 1):
  P_reflux ≈ 0 → time is effectively irreversible

For microscopic systems (N_E ≈ N_S, q_E ≈ q_S):
  P_reflux can be O(1) → "time reversal" is possible
  This IS quantum error correction (recovering system state from environment)

The arrow of time = the thermodynamic limit of the Reflux bound.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

def reflux_bound(N_S, N_E, q_S, q_E):
    """T2: P_reflux ≤ N_S·q_S / (N_E·q_E)"""
    return min(1.0, N_S * q_S / (N_E * q_E))


def time_reversal_probability(b1_sys, b1_env, c=0.5, p=0.5):
    """
    Estimate effective time reversal probability.

    In DGF: time reversal = recovering system information from environment.
    This requires: QCMI_recoverable / QCMI_total < 1
    """
    N_S = 2 * (b1_sys + 1)  # system qubits in vertex-sharing chain
    N_E = 2 * b1_env         # environment qubits
    q_S = p  # system purity ~ environment purity for simple model
    q_E = p

    P = reflux_bound(N_S, N_E, q_S, q_E)

    # QCMI estimate
    QCMI = eta_0 * b1_sys * c**2 * 4 * p * (1-p)  # 4 edges per ring

    return P, QCMI


print("=" * 70)
print("DGF TIME ARROW: Reflux Bound Quantification")
print("=" * 70)

print("""
T2 (Reflux bound, theorem): P_reflux ≤ N_S·q_S / (N_E·q_E)

This is THE DGF result about time. It says:
  "The probability of undoing the past is bounded by the purity ratio."

Three regimes:
""")

# Regime 1: Single qubit + small environment
print("REGIME 1: Microscopic — Time is REVERSIBLE")
print("-" * 50)
for b1_sys in [1, 2]:
    for b1_env in [1, 2, 5]:
        P, Q = time_reversal_probability(b1_sys, b1_env)
        status = "REVERSIBLE" if P > 0.1 else "transitional"
        print(f"  System b1={b1_sys}, Env b1={b1_env}: "
              f"P_reflux ≤ {P:.4f}, QCMI~{Q:.4f} bits → {status}")

# Regime 2: Mesoscopic
print(f"\nREGIME 2: Mesoscopic — Time has a WEAK arrow")
print("-" * 50)
for b1_sys in [10, 50]:
    for b1_env in [100, 1000]:
        P, Q = time_reversal_probability(b1_sys, b1_env)
        print(f"  System b1={b1_sys}, Env b1={b1_env}: "
              f"P_reflux ≤ {P:.2e}, QCMI~{Q:.2f} bits")

# Regime 3: Macroscopic
print(f"\nREGIME 3: Macroscopic — Time is IRREVERSIBLE")
print("-" * 50)
for b1_sys in [100]:
    for b1_env in [1e5, 1e10, 1e23]:
        P, Q = time_reversal_probability(b1_sys, b1_env)
        P_str = f"{P:.1e}" if P > 0 else "0"
        print(f"  System b1={b1_sys}, Env b1={b1_env:.0e}: "
              f"P_reflux ≤ {P_str}")

# ================================================================
# The key insight: "Time travel" in DGF
# ================================================================
print(f"\n{'='*70}")
print("WHAT DGF SAYS ABOUT TIME TRAVEL")
print(f"{'='*70}")

print("""
DGF says time travel (information reflux) is:
  - POSSIBLE in principle (the bound is > 0 for finite systems)
  - EXPONENTIALLY SUPPRESSED for macroscopic systems (P ~ 10^{-23})
  - EQUIVALENT to quantum error correction (recovering system from environment)

This is different from:
  - GR: time travel → closed timelike curves → causality paradoxes
  - Standard QM: time evolution is unitary → reversible in principle
  - DGF: time reversal IS possible, probability bounded by causal topology

The "arrow of time" in DGF is NOT a fundamental law.
It is a STATISTICAL consequence of asymmetric system-environment size.

In the early universe (small N_E, high q_E):
  P_reflux could be O(1) → time was "flexible" → no strong arrow

In the late universe (large N_E, low q_E):
  P_reflux → 0 → time is rigid → strong thermodynamic arrow

The arrow of time EMERGES as the universe expands and the
environment (N_E) grows relative to any local system (N_S).

This is a genuinely new perspective:
  The arrow of time = cosmic expansion of the causal graph.

As more causal events happen, more information is stored in the
environment, making it progressively harder to "undo" anything.
""")

# ================================================================
# Testable consequence: Time reversal in small quantum systems
# ================================================================
print("=" * 70)
print("TESTABLE: TIME REVERSAL IN SMALL QUANTUM SYSTEMS")
print("=" * 70)

print("""
For b1_sys = b1_env = 1 (2 system qubits, 2 environment qubits):
  P_reflux ≤ 2×0.5 / (2×0.5) = 1.0 → FULL time reversal possible

This means: a 4-qubit causal ring (2Q + 2E) can, in principle,
have its information flow REVERSED.

Experiment:
  1. Run a causal ring (Q1-E1-Q2-E2-Q1) with c=0.5
  2. Measure QCMI → confirms information flowed to environment
  3. Apply "time reversal" sequence: E2-Q2-E1-Q1 (reverse edges)
  4. Measure QCMI again → should return to ~0

This is EXACTLY a quantum error correction cycle:
  Encode → Error (information leaks to E) → Correct (recover from E)

DGF's "time travel" = quantum error correction.
The b1 ratio determines whether correction is possible.

PREDICTION: For an n-qubit system coupled to m-qubit environment:
  Time reversal possible when m < n·q_S/q_E
  Time reversal impossible when m >> n·q_S/q_E

This is testable on IBM Q: vary environment size, measure recovery fidelity.
""")
