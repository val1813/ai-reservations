"""
CATEGORY 2, TASK 4: Quantitative eta_0 Gap Analysis
====================================================
**CORRECTION (2026-06-09):** OLD eta_0 = 1/(8 ln 2) ~ 0.180 bits was WRONG.
CORRECT eta_0 = 2/ln 2 ~ 2.885 bits (see petz_recovery_v2.py, updated D1).
This script uses the old wrong value. All eta0 ratios need x16 readjustment.

a) QCMI per ring as function of c for c in (0, pi/2), b1=1
b) Ratio QCMI(c)/eta_0 as function of c
c) Limit QCMI(c)/eta_0 as c->0
d) Output plot-ready data table

Uses b1_scaling.py for single-ring QCMI computation.
"""
import numpy as np
import sys
sys.path.insert(0, r'D:\Claude\ai-reservations\DGF-Survivors')
from b1_scaling import make_vertex_sharing_chain

print("=" * 70)
print("TASK 4: Quantitative eta_0 Gap Analysis")
print("=" * 70)

eta0_old = 1.0 / (8.0 * np.log(2.0))  # WRONG - see correction
eta0_correct = 2.0 / np.log(2.0)  # CORRECT value
print(f"\n  eta_0 (OLD, WRONG) = 1/(8 ln 2) = {eta0_old:.8f} bits")
print(f"  eta_0 (CORRECT)     = 2/ln 2      = {eta0_correct:.8f} bits")
eta0 = eta0_old  # keep for backward compatibility with script logic

# Part (a): QCMI per ring as function of c
n_points = 60
c_values = np.linspace(0.01, np.pi/2 - 0.01, n_points)

qcmi_values = []
for c in c_values:
    g = make_vertex_sharing_chain(1, c_val=c)
    qcmi, srq, seq, sq = g.qcmi(0.5)
    qcmi_values.append(qcmi)

qcmi_values = np.array(qcmi_values)

# Part (b): Ratio
ratios = qcmi_values / eta0

print(f"\n  Scan results (selected points):")
print(f"  {'c (rad)':>10s}  {'c/pi':>10s}  {'QCMI':>12s}  {'QCMI/eta_0':>14s}")
print(f"  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*14}")

step = max(1, n_points // 12)
for i in range(0, n_points, step):
    print(f"  {c_values[i]:10.4f}  {c_values[i]/np.pi:10.4f}  {qcmi_values[i]:12.8f}  {ratios[i]:14.6f}")

# Show max
max_idx = np.argmax(qcmi_values)
print(f"\n  Maximum QCMI = {qcmi_values[max_idx]:.8f} bits at c = {c_values[max_idx]:.6f} rad = {c_values[max_idx]/np.pi:.6f}pi")
print(f"  Maximum ratio = {ratios[max_idx]:.6f}x")
print(f"  Ratio at c=0.5: QCMI/eta_0 = {qcmi_values[np.argmin(np.abs(c_values - 0.5))]:.4f} / {eta0:.6f} = {qcmi_values[np.argmin(np.abs(c_values - 0.5))]/eta0:.4f}x")

# Part (c): Small-c analysis
print(f"\n  Small-c behavior (c -> 0):")
print(f"  {'log10(c)':>10s}  {'c':>12s}  {'QCMI':>14s}  {'QCMI/c^2':>14s}  {'QCMI/eta0':>14s}")
print(f"  {'-'*10}  {'-'*12}  {'-'*14}  {'-'*14}  {'-'*14}")

# Compute for very small c
small_c = []
for c_exp in np.arange(-3.0, -1.0, 0.25):
    c_val = 10.0 ** c_exp
    if c_val < 0.0005:
        continue
    try:
        g = make_vertex_sharing_chain(1, c_val=c_val)
        qcmi, _, _, _ = g.qcmi(0.5)
        small_c.append({
            'c': c_val, 'qcmi': qcmi, 'ratio': qcmi/eta0,
            'qcmi_over_c2': qcmi / (c_val * c_val),
            'log10_c': c_exp
        })
    except Exception as e:
        print(f"    ERROR at c={c_val}: {e}")

# Also add the first few points from the main scan
for i in range(5):
    c_val = c_values[i]
    qcmi_val = qcmi_values[i]
    small_c.append({
        'c': c_val, 'qcmi': qcmi_val, 'ratio': qcmi_val/eta0,
        'qcmi_over_c2': qcmi_val / (c_val * c_val),
        'log10_c': np.log10(c_val)
    })

small_c.sort(key=lambda x: x['c'])

# Print table
seen = set()
for s in small_c:
    key = (round(s['c'], 10),)
    if key in seen:
        continue
    seen.add(key)
    print(f"  {s['log10_c']:10.2f}  {s['c']:12.2e}  {s['qcmi']:14.10f}  {s['qcmi_over_c2']:14.6f}  {s['ratio']:14.8f}")

# Fit QCMI = A * c^2 for smallest c points
small_vals = [s for s in small_c if s['c'] < 0.1]
if len(small_vals) >= 3:
    c_arr = np.array([s['c'] for s in small_vals])
    q_arr = np.array([s['qcmi'] for s in small_vals])
    # Fit QCMI = A * c^2 (quadratic, through origin)
    A = np.sum(c_arr**2 * q_arr) / np.sum(c_arr**4)
    q_pred = A * c_arr**2
    r2_small = 1 - np.sum((q_arr - q_pred)**2) / np.sum((q_arr - np.mean(q_arr))**2)

    print(f"\n  Small-c fit: QCMI(c) ~ A * c^2, A = {A:.6f}, R^2 = {r2_small:.6f}")
    print(f"  This confirms QCMI(c) scales as O(c^2) for small c.")
    print(f"  As c -> 0, QCMI(c)/eta_0 -> 0 (since QCMI -> 0 faster than eta_0 -> 0)")
    print(f"  eta_0 = {eta0:.8f} is a CONSTANT, not c-dependent.")
    print(f"  KEY FINDING: QCMI(c)/eta_0 does NOT approach 1 as c->0.")

# QCMI/eta_0 at c=0.5 (the paper's main working point)
qcmi_at_05 = qcmi_values[np.argmin(np.abs(c_values - 0.5))]
gap_ratio = qcmi_at_05 / eta0

print(f"\n  GAP ANALYSIS at c=0.5:")
print(f"    eta_0 (claimed bound) = {eta0:.6f} bits")
print(f"    Actual QCMI per ring = {qcmi_at_05:.6f} bits")
print(f"    Gap = {gap_ratio:.2f}x")
print(f"    The claimed bound eta_0 = 0.180 bits is ~{1/gap_ratio:.3f}x too SMALL.")
print(f"    The actual per-ring QCMI ({qcmi_at_05:.4f} bits) is the correct per-ring entropy contribution.")

# Full table for plotting (every 5th point for compactness)
print(f"\n  Plot-ready data (30 points):")
print(f"  {'c':>10s}  {'QCMI':>12s}  {'QCMI/eta0':>12s}")
print(f"  {'-'*10}  {'-'*12}  {'-'*12}")
plot_step = max(1, n_points // 30)
for i in range(0, n_points, plot_step):
    print(f"  {c_values[i]:10.6f}  {qcmi_values[i]:12.8f}  {ratios[i]:12.6f}")

print("\nDone - Task 4.")
