"""Retrieve CFOL Z/Y-basis results from queued jobs."""
import json, sys, numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService

TOKEN = 'uRlELcyrIqgYJnZet6Pru5MrejQH5inwOCn-Omg0IuDb'
JOB_ID = sys.argv[1] if len(sys.argv) > 1 else 'd8kaa4bnn5bs738qjq6g'
BASIS = sys.argv[2] if len(sys.argv) > 2 else 'Y'

def compute_irq(counts_dict, n_shots):
    p_RQ, p_R, p_Q = {}, {}, {}
    for bs, cnt in counts_dict.items():
        r, q = int(bs[2]), int(bs[1])
        rq = (r, q)
        p_RQ[rq] = p_RQ.get(rq,0) + cnt
        p_R[r] = p_R.get(r,0) + cnt
        p_Q[q] = p_Q.get(q,0) + cnt
    for k in p_RQ: p_RQ[k] /= n_shots
    for k in p_R: p_R[k] /= n_shots
    for k in p_Q: p_Q[k] /= n_shots
    def h(d): return -sum(v*np.log2(v) for v in d.values() if v>1e-12)
    return h(p_R) + h(p_Q) - h(p_RQ)

service = QiskitRuntimeService(channel='ibm_cloud', token=TOKEN)
job = service.job(JOB_ID)
st = str(job.status())
print(f'Job {JOB_ID} ({BASIS}-basis): {st}')

if st != 'DONE':
    print(f'Not ready. python cfol_ybasis_retrieve.py {JOB_ID} {BASIS}')
    sys.exit(0)

result = job.result()
print(f'Retrieved {len(result)} results')

# The labels aren't saved with this job (submitted with cfol_ybasis_submit.py)
# Read from the job metadata file
for fname in [f'cfol_{BASIS}_job.json', 'cfol_job_id.txt']:
    try:
        with open(fname) as f: meta = json.load(f)
        break
    except: pass

print(f'{"theta":>10s} {"type":>12s} {"I(R;Q)":>12s}')
print('-'*40)

data = {}
for i, pub in enumerate(result):
    counts = pub.data.c.get_counts()
    irq = compute_irq(counts, 100000)
    # Attempt to identify circuit from metadata
    label = meta.get('labels', [])[i] if i < len(meta.get('labels', [])) else (f'unknown_{i}',)
    print(f'{str(label):>22s} {irq:12.6f}')
    data[i] = {'label': str(label), 'I_RQ': irq}

# Compute deltas if we can identify func/dead pairs
with open(f'cfol_{BASIS}_results.json', 'w') as f:
    json.dump({'job_id': JOB_ID, 'basis': BASIS, 'data': data}, f, indent=2)
print(f'Saved: cfol_{BASIS}_results.json')
