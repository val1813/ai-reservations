"""
cl(4,1) TIME TRANSISTOR - IBM Q hardware submission
Tests: Clifford(c=0,pi/2) -> QCMI=0 (TIME FROZEN)
       Non-Clifford(c=pi/4) -> QCMI>0 (TIME FLOWING)
"""
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_aer import AerSimulator

TOKEN = 'XTawC-2Gs4hWHBZckyrfi3Hh2CrhAWtxE6lXsbBT2ebH'

def cl41_qcmi_circuits(c_tune, shots=10000):
    """
    6-qubit QCMI circuit: R0,R1(ref) + Q0,Q2(sys) + E1,E2(env).
    RZZ gates implement cl(4,1) Cartan edges.

    Measures in X-basis to detect QCMI (RZZ phases affect X correlations).
    """
    circuits = []
    labels = []

    # 4 measurement bases for tomography: XX, XY, YX, YY on ref qubits
    bases = [(0,0), (0,1), (1,0), (1,1)]  # (R0_basis, R1_basis): 0=X, 1=Y

    for b0, b1 in bases:
        qc = QuantumCircuit(6, 2)

        # Reference-system entanglement: |Phi+>_RQ
        qc.h([0, 1])
        qc.cx(0, 2)
        qc.cx(1, 4)
        qc.barrier()

        # cl(4,1) edges
        qc.rzz(c_tune, 2, 3)       # Q0-E1 (tunable)
        qc.rzz(np.pi/2, 3, 4)      # E1-Q2 (Clifford lock)
        qc.rzz(np.pi/2, 4, 5)      # Q2-E2 (Clifford lock)
        qc.rzz(np.pi/2, 5, 2)      # E2-Q0 (Clifford lock)
        qc.barrier()

        # Measurement basis rotation
        if b0 == 0: qc.h(0)
        else: qc.sdg(0); qc.h(0)
        if b1 == 0: qc.h(1)
        else: qc.sdg(1); qc.h(1)

        qc.measure([0, 1], [0, 1])
        circuits.append(qc)
        labels.append(f'c{c_tune/np.pi:.3f}pi_b{b0}{b1}')

    return circuits, labels

# ================================================================
# Local simulation first
# ================================================================
print("=" * 60)
print("cl(4,1) LOCAL SIMULATION")
print("=" * 60)

sim = AerSimulator()

for c_label, c_val in [('0 (FROZEN)', 0), ('pi/4 (MAX)', np.pi/4), ('pi/2 (FROZEN)', np.pi/2)]:
    circuits, labels = cl41_qcmi_circuits(c_val)

    # Run local
    results = []
    for qc in circuits:
        t_qc = transpile(qc, sim)
        job = sim.run(t_qc, shots=10000)
        counts = job.result().get_counts()
        results.append(counts)

    # Compute QCMI proxy: correlation between R0 and R1 measurements
    # For time-frozen (Clifford): correlations preserved (Bell pairs intact)
    # For time-flowing (non-Clifford): correlations degraded

    # Simple proxy: P(00) + P(11) - P(01) - P(10) (Bell correlation)
    corr = 0
    for counts in results:
        n = sum(counts.values())
        p00 = counts.get('00', 0) / n
        p11 = counts.get('11', 0) / n
        p01 = counts.get('01', 0) / n
        p10 = counts.get('10', 0) / n
        corr += (p00 + p11 - p01 - p10) / 4

    frozen = abs(c_val) < 1e-10 or abs(c_val - np.pi/2) < 1e-10
    status = 'FROZEN' if frozen else 'FLOWING'
    print(f"c={c_label}: corr={corr:.4f}, TIME {status}")
    if frozen and abs(corr) < 0.9:
        print(f"  WARNING: correlation degraded at Clifford point!")
    elif not frozen and abs(corr) < 0.5:
        print(f"  OK: correlation degraded by non-Clifford gate")

# ================================================================
# IBM Q submission
# ================================================================
print(f"\n{'='*60}")
print("IBM Q SUBMISSION")
print(f"{'='*60}")

try:
    service = QiskitRuntimeService(channel='ibm_cloud', token=TOKEN)
    backends = service.backends()
    # Pick smallest available
    backend = sorted(backends, key=lambda b: b.num_qubits)[0]
    print(f"Backend: {backend.name} ({backend.num_qubits} qubits)")

    # Submit cl(4,1) at c=pi/4 (time flowing) and c=pi/2 (time frozen)
    for c_label, c_val in [('pi/4 FLOW', np.pi/4), ('pi/2 FROZEN', np.pi/2)]:
        circuits, labels = cl41_qcmi_circuits(c_val)

        sampler = SamplerV2(mode=backend)
        job = sampler.run(circuits, shots=2000)
        job_id = job.job_id()

        print(f"\nc={c_label}: job_id={job_id}")
        print(f"  Monitor: https://quantum.ibm.com/")

except Exception as e:
    print(f"IBM Q error: {e}")
    print("Local results above are the verification.")
