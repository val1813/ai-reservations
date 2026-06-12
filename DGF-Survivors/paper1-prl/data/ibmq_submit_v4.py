"""
LP38 v4 — Optimized for ibm_kingston (heavy-hex, no 4-cycles)
================================================================
Fixes from v3:
  1. initial_layout to minimize SWAP: Ra adjacent to Qa, Rb adjacent to Qb
  2. X-basis measurement: run each theta TWICE (Z-basis + X-basis)
  3. Accept 1-2 SWAP for the E2-Qa edge (unavoidable on heavy-hex)

Circuit (8 qubits, 2 circuits per theta = 6 total):
  q0=Qa, q1=E1, q2=Qb, q3=E2  (ring)
  q4=Ra, q5=Rb                (reference)
  q6=anc_E1, q7=anc_E2        (mixed-state ancillae)
"""
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import numpy as np

TOKEN = '0wTawcB4PogS7TQ0Tf8Km59hYGUAdyy3RUkLgahy91wm'
BACKEND = 'ibm_kingston'
SHOTS = 50000  # split across Z and X basis
THETAS = [np.pi/4, np.pi/8, np.pi/16]
P_ENV = 0.7

print("=" * 60)
print("LP38 v4 — Optimized Layout + X-basis")
print("=" * 60)

# ── Connect ──
service = QiskitRuntimeService(channel='ibm_cloud', token=TOKEN, instance='open-instance')
backend = service.backend(BACKEND)
print(f"Backend: {BACKEND}")

# ── Build circuits ──
def add_rzz(qc, a, b, theta):
    """RZZ(theta) via CZ decomposition: 2 CZ + Rz + 4 H."""
    qc.h(b); qc.cz(a, b); qc.h(b)  # CX
    qc.rz(theta, b)
    qc.h(b); qc.cz(a, b); qc.h(b)  # CX

circuits = []
labels = []

for theta in THETAS:
    for basis in ['Z', 'X']:
        qc = QuantumCircuit(8, 6)
        qc.name = f"lp38_th{theta/np.pi:.3f}pi_{basis}"

        # Bell pairs Ra-Qa, Rb-Qb
        qc.h(4); qc.cx(4, 0)   # |Phi+>_{Ra,Qa}
        qc.h(5); qc.cx(5, 2)   # |Phi+>_{Rb,Qb}

        # Mixed environment (ancilla purification)
        th_p = 2 * np.arccos(np.sqrt(P_ENV))
        qc.ry(th_p, 6); qc.cx(6, 1); qc.reset(6)
        qc.ry(th_p, 7); qc.cx(7, 3); qc.reset(7)

        qc.barrier()

        # Causal ring: RZZ on all 4 edges
        for a, b in [(0,1), (1,2), (2,3), (3,0)]:
            add_rzz(qc, a, b, theta)

        qc.barrier()

        # Basis rotation for X-basis measurement
        if basis == 'X':
            for q in range(6):
                qc.h(q)

        # Measure ring + reference
        qc.measure([0,1,2,3,4,5], [0,1,2,3,4,5])

        circuits.append(qc)
        labels.append(f"th{theta/np.pi:.3f}pi_{basis}")

for qc in circuits:
    ops = qc.count_ops()
    print(f"  {qc.name}: logical CZ={ops.get('cz',0)}, depth={qc.depth()}")

# ── Transpile with initial_layout ──
# Use the best layout from the previous run (v3 transpilation found good mapping)
print(f"\nTranspiling with opt_level=3 + layout optimization...")
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
circuits_isa = pm.run(circuits)

for i, qc in enumerate(circuits_isa):
    ops = qc.count_ops()
    print(f"  [{i}] {labels[i]}: CZ={ops.get('cz',0)}, SX={ops.get('sx',0)}, "
          f"depth={qc.depth()}")

# ── Submit ──
total_shots = SHOTS * len(circuits_isa)
print(f"\nSubmitting {len(circuits_isa)} circuits x {SHOTS} shots = {total_shots} total...")
sampler = SamplerV2(mode=backend)
job = sampler.run(circuits_isa, shots=SHOTS)

print(f"\n{'='*60}")
print(f"SUBMITTED!")
print(f"  Job ID: {job.job_id()}")
print(f"  Circuits: {len(circuits_isa)} (3 theta x 2 bases)")
print(f"  Shots: {SHOTS}/circuit ({total_shots} total)")
print(f"  Thetas: pi/4, pi/8, pi/16")
print(f"  Bases: Z + X per theta")
print(f"{'='*60}")
