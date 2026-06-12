"""
CFOL Y-basis experiment — captures the REAL QCMI signal.
Z-basis is blind to QCMI in RZZ rings (preserves Z-diagonality).
Y-basis accesses the off-diagonal coherence that carries the CFOL signal.

Split into 2 jobs to stay under open-plan time limit:
  Job A: Z-basis, 3theta x 2types = 6 circuits x 100k = 600k shots
  Job B: Y-basis, same = 600k shots
"""
import numpy as np, json, argparse, time
from datetime import datetime
from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate

P_ENV = 0.7
SHOTS = 100_000
IDLE_TIME_NS = 500
BACKEND_NAME = "ibm_kingston"

def make_cfol_circuit(theta, theta1=np.pi/2, p=0.7, functional=True, basis='Z'):
    qc = QuantumCircuit(3, 3)
    qc.h(0); qc.cx(0, 1)                         # Bell |Phi+> R-Q
    phi_env = 2 * np.arccos(np.sqrt(p))
    qc.ry(phi_env, 2)                              # Environment |gamma>
    qc.barrier()
    if functional:
        qc.append(RZZGate(theta1), [1, 2])         # First RZZ
    qc.delay(IDLE_TIME_NS, 1, unit='ns')
    qc.delay(IDLE_TIME_NS, 2, unit='ns')
    qc.append(RZZGate(theta), [1, 2])              # Second RZZ
    qc.barrier()
    if basis == 'X':
        qc.h(0); qc.h(1); qc.h(2)
    elif basis == 'Y':
        qc.sdg(0); qc.h(0)                         # Sdg+H = Y->Z rotation
        qc.sdg(1); qc.h(1)
        qc.sdg(2); qc.h(2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

def submit_job(token, basis, dry_run=False):
    circuits, labels = [], []
    for theta in [np.pi/4, np.pi/8, np.pi/16]:
        ts = f"pi_{int(np.pi/theta)}"
        for func, fname in [(True, 'functional'), (False, 'dead')]:
            qc = make_cfol_circuit(theta, functional=func, basis=basis)
            qc.name = f"cfol_{fname}_{basis}_{ts}"
            circuits.append(qc)
            labels.append((fname, basis, float(theta)))

    n_circuits = len(circuits)
    total_shots = SHOTS * n_circuits
    print(f"CFOL {basis}-basis: {n_circuits} circuits x {SHOTS:,} shots = {total_shots:,} total")

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

    with open(f"cfol_{basis}_job.json", "w") as f:
        json.dump({"job_id": jid, "backend": backend.name, "basis": basis,
                   "shots": SHOTS, "labels": [(a,b,float(c)) for a,b,c in labels],
                   "timestamp": datetime.now().isoformat()}, f, indent=2)

    print(f"Job ID: {jid} | Status: {job.status()}")
    print(f"Retrieve: python cfol_ybasis_retrieve.py {jid} {basis}")
    return jid

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True)
    parser.add_argument("--basis", required=True, choices=['Z','Y'])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    submit_job(args.token, args.basis, dry_run=args.dry_run)
