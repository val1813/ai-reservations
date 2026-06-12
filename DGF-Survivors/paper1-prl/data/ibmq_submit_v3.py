"""
LP38 IBM Q Experiment — ibm_kingston
=====================================
Tests: QCMI(theta) > 0 for 4-node causal ring.
Theta values: pi/4, pi/8, pi/16 (S/N ~19, 10, 4 from simulation)

Hard constraints (learned from previous errors):
  - NO RZZ fractionals → decompose RZZ = 2*CZ + Rz + 2*H
  - NO 4-cycles in heavy-hex → let transpiler add SWAPs
  - Max 10M shots/job → use 100k shots/circuit
  - Max execution time → keep circuit depth reasonable

Circuit (8 qubits):
  q0=Qa, q1=E1, q2=Qb, q3=E2  (ring nodes)
  q4=Ra, q5=Rb                  (reference, Bell-entangled)
  q6=anc_E1, q7=anc_E2          (mixed-state ancillae)
"""
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import numpy as np

TOKEN = '0wTawcB4PogS7TQ0Tf8Km59hYGUAdyy3RUkLgahy91wm'
BACKEND = 'ibm_kingston'
SHOTS = 100000
THETAS = [np.pi/4, np.pi/8, np.pi/16]
P_ENV = 0.7

print("=" * 60)
print("LP38 IBM Q Experiment")
print("=" * 60)

# ── Connect ──
service = QiskitRuntimeService(channel='ibm_cloud', token=TOKEN, instance='open-instance')
backend = service.backend(BACKEND)
print(f"Backend: {BACKEND} | {backend.num_qubits}q | Heron r2")

# ── Build ──
def add_rzz(qc, a, b, theta):
    """RZZ(theta) = exp(-i*theta/2 Z⊗Z) via CZ decomposition.
    RZZ = CX(a,b); Rz(theta,b); CX(a,b)  where CX = H(tgt)-CZ-H(tgt)."""
    qc.h(b); qc.cz(a, b); qc.h(b)  # CX(a,b)
    qc.rz(theta, b)
    qc.h(b); qc.cz(a, b); qc.h(b)  # CX(a,b)

circuits = []
for theta in THETAS:
    qc = QuantumCircuit(8, 6)
    qc.name = f"lp38_th{theta/np.pi:.3f}pi"

    # ── Bell pairs Ra-Qa, Rb-Qb ──
    qc.h(4); qc.cx(4, 0)   # |Phi+>_{Ra,Qa}
    qc.h(5); qc.cx(5, 2)   # |Phi+>_{Rb,Qb}

    # ── Mixed environment via ancilla purification ──
    th_p = 2 * np.arccos(np.sqrt(P_ENV))
    qc.ry(th_p, 6); qc.cx(6, 1); qc.reset(6)  # E1 = diag(p,1-p)
    qc.ry(th_p, 7); qc.cx(7, 3); qc.reset(7)  # E2 = diag(p,1-p)

    qc.barrier()

    # ── Causal ring: RZZ on Qa-E1, E1-Qb, Qb-E2, E2-Qa ──
    for a, b in [(0,1), (1,2), (2,3), (3,0)]:
        add_rzz(qc, a, b, theta)

    qc.barrier()

    # ── Measure ring + reference (Z basis) ──
    qc.measure([0,1,2,3,4,5], [0,1,2,3,4,5])

    circuits.append(qc)

for qc in circuits:
    ops = qc.count_ops()
    n_cz = ops.get('cz', 0)
    print(f"  {qc.name}: logical CZ={n_cz}, depth={qc.depth()}, qubits={qc.num_qubits}")

# ── Transpile ──
print(f"\nTranspiling for {BACKEND} (opt_level=3)...")
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
circuits_isa = pm.run(circuits)

for qc in circuits_isa:
    ops = qc.count_ops()
    n_cz = ops.get('cz', 0)
    n_sx = ops.get('sx', 0)
    n_rz = ops.get('rz', 0)
    print(f"  {qc.name}: ISA CZ={n_cz}, SX={n_sx}, RZ={n_rz}, depth={qc.depth()}")

# ── Submit ──
print(f"\nSubmitting {len(circuits_isa)} circuits x {SHOTS} shots...")
sampler = SamplerV2(mode=backend)
job = sampler.run(circuits_isa, shots=SHOTS)
total_shots = SHOTS * len(circuits_isa)

print(f"\n{'='*60}")
print(f"SUBMITTED!")
print(f"  Job ID: {job.job_id()}")
print(f"  Backend: {BACKEND}")
print(f"  Shots: {SHOTS}/circuit ({total_shots} total, limit=10M)")
print(f"  Thetas: pi/4, pi/8, pi/16")
print(f"{'='*60}")
print(f"\nCheck: job.status() or visit quantum.ibm.com")
print(f"To retrieve: result = job.result(); quasi_probs = result[0].data")
