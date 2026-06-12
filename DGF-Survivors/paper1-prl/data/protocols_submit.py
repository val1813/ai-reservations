"""
CFOL Protocol 1+2: Ratio Test + Axis Test
最小化设计 — Z基only, RZZ+RXX, pi/4+pi/8
"""
import numpy as np, json, argparse
from datetime import datetime
from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXXGate

P_ENV = 0.7
SHOTS = 20_000
IDLE_TIME_NS = 500
BACKEND_NAME = "ibm_kingston"

def make_cfol_circuit(theta, theta1=np.pi/2, p=0.7, functional=True, basis='Z', gate_type='ZZ'):
    """gate_type: 'ZZ' for RZZ (aligned), 'XX' for RXX (misaligned)"""
    qc = QuantumCircuit(3, 3)

    # Bell pair R-Q
    qc.h(0); qc.cx(0, 1)

    # Environment
    phi = 2 * np.arccos(np.sqrt(p))
    qc.ry(phi, 2)
    qc.barrier()

    # First gate
    if functional:
        if gate_type == 'ZZ':
            qc.append(RZZGate(theta1), [1, 2])
        else:
            qc.append(RXXGate(theta1), [1, 2])

    # Idle
    qc.delay(IDLE_TIME_NS, 1, unit='ns')
    qc.delay(IDLE_TIME_NS, 2, unit='ns')

    # Second gate
    if gate_type == 'ZZ':
        qc.append(RZZGate(theta), [1, 2])
    else:
        qc.append(RXXGate(theta), [1, 2])

    qc.barrier()

    if basis == 'X':
        qc.h(0); qc.h(1); qc.h(2)
    elif basis == 'Y':
        qc.sdg(0); qc.h(0); qc.sdg(1); qc.h(1); qc.sdg(2); qc.h(2)

    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

def submit(token, dry_run=False):
    circuits, labels = [], []

    # === PROTOCOL 1: Ratio Test (RZZ, pi/4 + pi/8, Z-basis, functional+dead) ===
    for theta in [np.pi/4, np.pi/8]:
        ts = f"pi_{int(np.pi/theta)}"
        for func, fname in [(True, 'functional'), (False, 'dead')]:
            qc = make_cfol_circuit(theta, functional=func, basis='Z', gate_type='ZZ')
            qc.name = f"ratio_{fname}_Z_{ts}"
            circuits.append(qc)
            labels.append(('ratio', fname, 'Z', float(theta), 'ZZ'))

    # === PROTOCOL 2: Axis Test (RXX, pi/4 + pi/8, Z-basis, functional+dead) ===
    for theta in [np.pi/4, np.pi/8]:
        ts = f"pi_{int(np.pi/theta)}"
        for func, fname in [(True, 'functional'), (False, 'dead')]:
            qc = make_cfol_circuit(theta, functional=func, basis='Z', gate_type='XX')
            qc.name = f"axis_{fname}_Z_{ts}"
            circuits.append(qc)
            labels.append(('axis', fname, 'Z', float(theta), 'XX'))

    print(f"Protocols 1+2: Ratio Test + Axis Test")
    print(f"Circuits: {len(circuits)} (2 theta x 2 func/dead x 2 gate types)")
    print(f"Shots: {SHOTS:,}/circuit, Total: {SHOTS*len(circuits):,}")

    if dry_run:
        print("[DRY RUN]")
        print(circuits[0])
        return None

    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

    service = QiskitRuntimeService(token=token)
    backend = service.backend(BACKEND_NAME)
    print(f"Backend: {backend.name}")

    pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
    isa_circuits = pm.run(circuits)
    print(f"Max depth: {max(c.depth() for c in isa_circuits)}")

    sampler = Sampler(mode=backend)
    job = sampler.run(isa_circuits, shots=SHOTS)
    jid = job.job_id()

    with open("protocols_job_id.txt", "w") as f:
        json.dump({"job_id": jid, "backend": backend.name, "shots": SHOTS,
                   "labels": [(a,b,c,float(d),e) for a,b,c,d,e in labels],
                   "timestamp": datetime.now().isoformat()}, f, indent=2)

    print(f"Job ID: {jid}")
    print(f"Status: {job.status()}")
    print(f"Retrieve: python protocols_retrieve.py {jid}")
    return jid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    submit(args.token, dry_run=args.dry_run)
