"""Check CFOL job status and retrieve results when done.
Usage: python check_and_retrieve.py
"""
import json, time, sys
import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService

TOKEN = '0wTawcB4PogS7TQ0Tf8Km59hYGUAdyy3RUkLgahy91wm'
JOB_ID = 'd8k1kcj2d42s73c9kipg'
OUTPUT_FILE = f'cfol_results_{JOB_ID[:8]}.json'

service = QiskitRuntimeService(token=TOKEN)
job = service.job(JOB_ID)

status = str(job.status())
print(f'Job {JOB_ID}: {status}')

if status == 'DONE':
    print('Retrieving results...')
    result = job.result()

    # Load metadata
    with open('cfol_job_id.txt') as f:
        meta = json.load(f)
    labels = meta['labels']
    thetas = meta['thetas']

    def compute_irq(counts_dict, n_shots):
        """Compute I(R;Q) from counts."""
        p_RQ, p_R, p_Q = {}, {}, {}
        for bitstring, count in counts_dict.items():
            r = int(bitstring[2])
            q = int(bitstring[1])
            rq = (r, q)
            p_RQ[rq] = p_RQ.get(rq, 0) + count
            p_R[r] = p_R.get(r, 0) + count
            p_Q[q] = p_Q.get(q, 0) + count
        for k in p_RQ: p_RQ[k] /= n_shots
        for k in p_R: p_R[k] /= n_shots
        for k in p_Q: p_Q[k] /= n_shots
        def h(d): return -sum(v*np.log2(v) for v in d.values() if v > 1e-12)
        return h(p_R) + h(p_Q) - h(p_RQ)

    results_by_theta = {}
    for i, (ring_type, basis, theta) in enumerate(labels):
        pub_result = result[i]
        counts = pub_result.data.c.get_counts()
        irq = compute_irq(counts, meta['shots'])
        key = (theta, basis)
        if key not in results_by_theta:
            results_by_theta[key] = {}
        results_by_theta[key][ring_type] = irq
        print(f'  [{i}] theta={theta/np.pi:.3f}pi {ring_type:>10s} {basis}: I(R;Q)={irq:.6f}')

    # Compute differential signals
    print()
    print('=' * 60)
    print('RESULTS: Delta I(R;Q) = Dead - Functional')
    print('=' * 60)
    print(f"{'theta':>10s} {'Delta_Z':>10s} {'Delta_X':>10s} {'Bell_fid':>10s}")
    print('-' * 45)

    output_data = {'job_id': JOB_ID, 'results': {}}
    for theta in thetas:
        delta_Z = (results_by_theta.get((theta, 'Z'), {}).get('dead', 0) -
                   results_by_theta.get((theta, 'Z'), {}).get('functional', 0))
        delta_X = (results_by_theta.get((theta, 'X'), {}).get('dead', 0) -
                   results_by_theta.get((theta, 'X'), {}).get('functional', 0))
        bell_fid = results_by_theta.get((theta, 'Z'), {}).get('functional', 0) / 2.0
        ts = f'pi/{int(np.pi/theta)}'
        print(f'{ts:>10s} {delta_Z:10.4f} {delta_X:10.4f} {bell_fid:10.4f}')
        output_data['results'][ts] = {
            'delta_Z': delta_Z, 'delta_X': delta_X,
            'bell_fidelity': bell_fid,
            'irq_functional_Z': results_by_theta.get((theta, 'Z'), {}).get('functional', 0),
            'irq_dead_Z': results_by_theta.get((theta, 'Z'), {}).get('dead', 0),
        }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f'Saved: {OUTPUT_FILE}')

elif status == 'ERROR':
    print(f'Error: {job.error_message()}')
elif status in ('QUEUED', 'RUNNING'):
    print(f'Still {status}. Check again later.')
    print(f'python check_and_retrieve.py')
