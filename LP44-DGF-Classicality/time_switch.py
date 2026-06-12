"""
DGF Time Switch: controllable time arrow via N_E/N_S ratio.

T2 (Reflux): P_reflux <= N_S * q_S / (N_E * q_E)

Binary condition:
  N_E < N_S:  P_reflux ~ O(1) -> time REVERSIBLE (quantum recurrence)
  N_E = N_S:  CRITICAL POINT -> phase transition in time direction
  N_E > N_S:  P_reflux -> 0    -> time IRREVERSIBLE (thermodynamic arrow)

Testable: sweep N_E/N_S, measure information reflux probability.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

def reflux_probability(N_S, N_E, q_S=0.5, q_E=0.5):
    """T2 bound: upper limit on information reflux."""
    return min(1.0, N_S * q_S / (N_E * q_E))

def time_phase(N_S, N_E):
    """Binary time phase from N_E/N_S ratio."""
    ratio = N_E / N_S
    P = reflux_probability(N_S, N_E)
    if ratio < 1.0:
        return "REVERSIBLE", P
    elif ratio < 2.0:
        return "CRITICAL", P
    else:
        return "IRREVERSIBLE", P

print("=" * 70)
print("DGF TIME SWITCH: N_E/N_S controls the arrow of time")
print("=" * 70)

print(f"\n{'N_S':<8} {'N_E':<8} {'N_E/N_S':<10} {'P_reflux':<12} {'Phase':<15}")
print("-" * 55)

for N_S in [1, 2, 5, 10, 100]:
    for N_E in [1, 2, 5, 10, 100, 1000, 1e23]:
        P = reflux_probability(N_S, N_E)
        phase, _ = time_phase(N_S, N_E)
        ratio = N_E / N_S
        marker = " <<<" if abs(ratio - 1.0) < 0.5 else ""
        print(f"{N_S:<8} {str(N_E):<8} {ratio:<10.2f} {P:<12.2e} {phase:<15}{marker}")

# ================================================================
# The critical point
# ================================================================
print(f"\n{'='*70}")
print("CRITICAL POINT: N_E = N_S")
print(f"{'='*70}")
print("""
At N_E = N_S:
  P_reflux = q_S/q_E ~ O(1) for similar purities
  Forward and reverse information flows are COMPARABLE
  Time has no well-defined arrow
  -> The system shows QUANTUM RECURRENCE (Poincare-like)
  -> Information can flow back from environment
  -> This IS time reversal at the microscopic scale

At N_E >> N_S:
  P_reflux ~ N_S/N_E -> 0
  Forward flow dominates overwhelmingly
  -> THERMODYNAMIC ARROW emerges
  -> Information never returns

THE SWITCH:
  To REVERSE time: reduce N_E below N_S.
  In practice: isolate the system from its environment.
  This is what quantum error correction does:
  it creates an effective environment with N_E_eff < N_S.

  To ACCELERATE time (faster decoherence):
  increase N_E. Couple to a large, cold bath.

  To STOP time:
  tune all Cartan parameters to Clifford (c = pi/2, 0, pi...).
  QCMI = 0 for all rings -> no information flows -> time freezes.
""")

# ================================================================
# Three control knobs for time
# ================================================================
print("=" * 70)
print("THREE CONTROL KNOBS FOR TIME")
print("=" * 70)
print("""
KNOB 1: Environment size N_E
  Smaller N_E -> more reversible time
  N_E = 0 -> perfectly reversible (isolated quantum system)
  N_E -> infinity -> perfectly irreversible (macroscopic classical)

KNOB 2: Environment purity q_E
  q_E -> 1 (pure environment) -> P_reflux larger -> time less rigid
  q_E -> 0 (mixed, classical) -> P_reflux small -> time rigid
  Cool and purify the environment to soften the time arrow.

KNOB 3: Cartan parameter c (the "Clifford switch")
  c in (pi/2)*Z (Clifford) -> QCMI = 0 -> NO TIME FLOW
  c = pi/4 -> maximum QCMI per ring -> FASTEST TIME FLOW
  c -> 0 -> weak coupling -> SLOW TIME FLOW

  This is a CONTINUOUS control: time rate can be tuned smoothly.
""")
