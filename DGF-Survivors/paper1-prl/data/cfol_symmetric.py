"""
Symmetric temporal ring: theta1=theta2=theta
Functional: both RZZ(theta) active
Dead: both identity
Y-basis only. 100k shots. 3 theta values.
"""
import numpy as np, json, argparse
from datetime import datetime
from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate

P_ENV, SHOTS, IDLE_NS = 0.7, 100_000, 500
BACKEND = "ibm_kingston"
THETAS = [np.pi/4, np.pi/8, np.pi/16]
TOKEN = "QFAYt1fKqb517eRjoPZvqCh83jtpvZyG3grWQu-7gWYT"

def make_circuit(theta, functional=True, basis='Y'):
    qc = QuantumCircuit(3, 3)
    qc.h(0); qc.cx(0, 1)
    phi = 2 * np.arccos(np.sqrt(P_ENV))
    qc.ry(phi, 2)
    qc.barrier()
    if functional:
        qc.append(RZZGate(theta), [1, 2])
        qc.delay(IDLE_NS, 1, unit='ns'); qc.delay(IDLE_NS, 2, unit='ns')
        qc.append(RZZGate(theta), [1, 2])
    # dead: no gates at all
    qc.barrier()
    if basis == 'Y':
        qc.sdg(0); qc.h(0); qc.sdg(1); qc.h(1); qc.sdg(2); qc.h(2)
    qc.measure([0,1,2], [0,1,2])
    return qc

circuits, labels = [], []
for theta in THETAS:
    ts = f"pi_{int(np.pi/theta)}"
    for func, fname in [(True,'func'), (False,'dead')]:
        qc = make_circuit(theta, func)
        qc.name = f"sym_{fname}_Y_{ts}"
        circuits.append(qc)
        labels.append((fname, float(theta)))

print(f"Symmetric temporal ring: {len(circuits)} circuits x {SHOTS:,} shots")
print(f"Thetas: pi/4, pi/8, pi/16 | Dead=both identity")

from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

s = QiskitRuntimeService(channel='ibm_cloud', token=TOKEN)
be = s.backend(BACKEND)
pm = generate_preset_pass_manager(optimization_level=1, backend=be)
isa = pm.run(circuits)
print(f"Backend: {be.name} | Max depth: {max(c.depth() for c in isa)}")

sampler = Sampler(mode=be)
job = sampler.run(isa, shots=SHOTS)
jid = job.job_id()

with open("cfol_sym_job.json","w") as f:
    json.dump({"job_id":jid,"backend":be.name,"shots":SHOTS,
               "labels":[(a,float(b)) for a,b in labels],
               "timestamp":datetime.now().isoformat()}, f, indent=2)

print(f"Job ID: {jid} | Status: {job.status()}")
print(f"Retrieve: python cfol_sym_retrieve.py {jid}")
