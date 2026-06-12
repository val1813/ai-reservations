"""Retrieve and analyze Protocols 1+2 results."""
import json, sys, numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService

TOKEN = '0wTawcB4PogS7TQ0Tf8Km59hYGUAdyy3RUkLgahy91wm'
JOB_ID = sys.argv[1] if len(sys.argv) > 1 else 'd8k2e4bnn5bs738q9s70'

def compute_irq(counts_dict, n_shots):
    p_RQ, p_R, p_Q = {}, {}, {}
    for bs, cnt in counts_dict.items():
        r, q = int(bs[2]), int(bs[1])
        rq = (r, q)
        p_RQ[rq] = p_RQ.get(rq, 0) + cnt
        p_R[r] = p_R.get(r, 0) + cnt
        p_Q[q] = p_Q.get(q, 0) + cnt
    for k in p_RQ: p_RQ[k] /= n_shots
    for k in p_R: p_R[k] /= n_shots
    for k in p_Q: p_Q[k] /= n_shots
    def h(d): return -sum(v*np.log2(v) for v in d.values() if v > 1e-12)
    return h(p_R) + h(p_Q) - h(p_RQ)

service = QiskitRuntimeService(token=TOKEN)
job = service.job(JOB_ID)
st = str(job.status())
print(f'Job {JOB_ID}: {st}')

if st != 'DONE':
    print(f'Not done yet. Status: {st}')
    sys.exit(0)

result = job.result()
with open('protocols_job_id.txt') as f:
    meta = json.load(f)
labels = meta['labels']

# Group results
ratio_data = {}  # (theta, gate_type, func_type) -> Irq
for i, (proto, fname, basis, theta, gtype) in enumerate(labels):
    pub = result[i]
    counts = pub.data.c.get_counts()
    irq = compute_irq(counts, meta['shots'])
    key = (proto, theta, gtype, fname)
    ratio_data[key] = irq
    print(f'  [{i}] {proto} theta={theta/np.pi:.3f}pi {gtype} {fname}: I(R;Q)={irq:.6f}')

print()
print('='*60)
print('PROTOCOL 1: RATIO TEST')
print('='*60)
for gtype in ['ZZ']:
    for theta in [np.pi/4, np.pi/8]:
        df = ratio_data.get(('ratio', theta, gtype, 'functional'), 0)
        dd = ratio_data.get(('ratio', theta, gtype, 'dead'), 0)
        delta = dd - df
        ts = f'pi/{int(np.pi/theta)}'
        print(f'  {gtype} {ts}: Delta = {dd:.4f} - {df:.4f} = {delta:.4f}')

dz4 = ratio_data.get(('ratio', np.pi/4, 'ZZ', 'dead'),0) - ratio_data.get(('ratio', np.pi/4, 'ZZ', 'functional'),0)
dz8 = ratio_data.get(('ratio', np.pi/8, 'ZZ', 'dead'),0) - ratio_data.get(('ratio', np.pi/8, 'ZZ', 'functional'),0)
R_exp = dz8 / max(dz4, 1e-10)
print(f'  R_exp = Delta(pi/8)/Delta(pi/4) = {dz8:.4f}/{dz4:.4f} = {R_exp:.4f}')
print(f'  R_LP38 = 0.48, R_CCQ = 0.0625')

print()
print('='*60)
print('PROTOCOL 2: AXIS TEST')
print('='*60)
for theta in [np.pi/4, np.pi/8]:
    dz_zz = ratio_data.get(('ratio', theta, 'ZZ', 'dead'),0) - ratio_data.get(('ratio', theta, 'ZZ', 'functional'),0)
    dz_xx = ratio_data.get(('axis', theta, 'XX', 'dead'),0) - ratio_data.get(('axis', theta, 'XX', 'functional'),0)
    ts = f'pi/{int(np.pi/theta)}'
    print(f'  {ts}: Delta(RZZ)={dz_zz:.4f}, Delta(RXX)={dz_xx:.4f}, RXX/RZZ={dz_xx/max(dz_zz,1e-10):.2f}')

# Save
output = {'job_id': JOB_ID, 'ratio_test': {'R_exp': R_exp, 'dz_pi4': dz4, 'dz_pi8': dz8}}
with open(f'protocols_results_{JOB_ID[:8]}.json', 'w') as f:
    json.dump(output, f, indent=2)
print(f'\nSaved: protocols_results_{JOB_ID[:8]}.json')
