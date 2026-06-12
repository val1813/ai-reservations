"""
INSPECTOR v2: Adversarial audit of b1-scaling results.

Tests every claim from documents 09-11 for numerical and logical errors.
"""
import numpy as np
from itertools import product
import sys
sys.path.insert(0, 'D:/Claude/ai-reservations/DGF-Survivors')
from b1_scaling import (
    CausalGraph, make_vertex_sharing_chain, make_disjoint_rings,
    make_edge_sharing_chain, von_neumann_entropy
)

def print_header(msg):
    print(f"\n{'='*70}")
    print(f"  {msg}")
    print(f"{'='*70}")

# ============================================================
# CHECK 0: Understand Gram matrix structure for b1=1 (single ring)
# ============================================================
print_header("CHECK 0: Verify factorization formula for b1=1")

g = make_vertex_sharing_chain(1, c_val=0.5)
G = g.gram_matrix(0.5)
d_s = g.d_s

print(f"d_s = {d_s}, G shape = {G.shape}")

# Diagonal should be 1
diag_err = np.max(np.abs(np.diag(G) - 1.0))
print(f"max |G_ii - 1| = {diag_err:.2e}")

# Verify factorization: for single ring, G[a,b] = cos²(c·Δ)² for p=0.5
# where Δ = (b0+b1) - (a0+a1), each in {±1}
c = 0.5
max_err_factor = 0.0
for a_idx, a in enumerate(product([1, -1], repeat=2)):
    for b_idx, b in enumerate(product([1, -1], repeat=2)):
        a_sum = a[0] + a[1]
        b_sum = b[0] + b[1]
        Delta = b_sum - a_sum
        predicted = np.cos(c * Delta) ** 2  # squared once because 2 env qubits, each gives cos(c*Delta)
        # Actually: [p*e^{icΔ}+(1-p)*e^{-icΔ}]² = cos²(cΔ) for p=0.5
        # Each env qubit gives cos(cΔ), so total = cos²(cΔ)
        actual = G[a_idx, b_idx].real
        err = abs(predicted - actual)
        max_err_factor = max(max_err_factor, err)

print(f"Max factorization error (b1=1, p=0.5): {max_err_factor:.2e}")

# Check b1=2 factorization
print("\n--- Factorization for b1=2 ---")
g2 = make_vertex_sharing_chain(2, c_val=0.5)
G2 = g2.gram_matrix(0.5)
d_s2 = g2.d_s
print(f"d_s = {d_s2}")

max_err2 = 0.0
for a_idx, a in enumerate(product([1, -1], repeat=3)):
    for b_idx, b in enumerate(product([1, -1], repeat=3)):
        Delta0 = (b[0]+b[1]) - (a[0]+a[1])
        Delta1 = (b[1]+b[2]) - (a[1]+a[2])
        predicted = np.cos(c * Delta0)**2 * np.cos(c * Delta1)**2
        actual = G2[a_idx, b_idx].real
        err = abs(predicted - actual)
        max_err2 = max(max_err2, err)

print(f"Max factorization error (b1=2, p=0.5): {max_err2:.2e}")

# ============================================================
# CHECK 1: G_{a,a} = 1 for b1=3, p=0.3, c=0.5
# ============================================================
print_header("CHECK 1: Trace-preserving G_{a,a}=1")

for b1 in [3, 4, 5]:
    for p in [0.1, 0.3, 0.5, 0.7, 0.9]:
        g = make_vertex_sharing_chain(b1, c_val=0.5)
        G = g.gram_matrix(p)
        diag = np.diag(G).real
        max_dev = np.max(np.abs(diag - 1.0))
        min_diag = np.min(diag.real)
        if max_dev > 1e-10:
            print(f"  b1={b1} p={p}: max|G_ii-1| = {max_dev:.2e} FAIL")
        else:
            print(f"  b1={b1} p={p}: max|G_ii-1| = {max_dev:.2e} OK")

# ============================================================
# CHECK 2: S(EQ) = log(d_s) for b1=3
# ============================================================
print_header("CHECK 2: S(EQ) = S(Q) = log(d_s)")

for b1 in [1, 2, 3, 4]:
    g = make_vertex_sharing_chain(b1, c_val=0.5)
    qcmi, Srq, Seq, Sq = g.qcmi(0.5)
    d_s = g.d_s
    log_ds = np.log2(d_s)
    print(f"  b1={b1}: S_Q={Sq:.8f} log(d_s)={log_ds:.8f} diff={abs(Sq-log_ds):.2e}")
    print(f"         S_EQ={Seq:.8f} log(d_s)={log_ds:.8f} diff={abs(Seq-log_ds):.2e}")
    print(f"         S_RQ={Srq:.8f}")

# Also check for p=0.3
print("\n--- With p=0.3 ---")
for b1 in [1, 2, 3, 4]:
    g = make_vertex_sharing_chain(b1, c_val=0.5)
    qcmi, Srq, Seq, Sq = g.qcmi(0.3)
    d_s = g.d_s
    log_ds = np.log2(d_s)
    print(f"  b1={b1}: S_Q diff={abs(Sq-log_ds):.2e} S_EQ diff={abs(Seq-log_ds):.2e}")

# ============================================================
# CHECK 3: Negative eigenvalues in G (numerical instability)
# ============================================================
print_header("CHECK 3: Gram matrix positive semi-definiteness")

for b1 in [2, 4, 6, 8]:
    for p in [0.1, 0.3, 0.5, 0.7, 0.9]:
        g = make_vertex_sharing_chain(b1, c_val=0.5)
        G = g.gram_matrix(p)
        evals = np.linalg.eigvalsh(G)
        min_eval = np.min(evals)
        neg_count = np.sum(evals < -1e-10)
        if neg_count > 0:
            print(f"  b1={b1} p={p}: {neg_count} negative evals, min={min_eval:.2e} ***FAIL***")
        else:
            print(f"  b1={b1} p={p}: all >=0, min={min_eval:.2e} OK")

# ============================================================
# CHECK 4: Edge case p=0.001, b1=2
# ============================================================
print_header("CHECK 4: Extreme p=0.001, b1=2")

g = make_vertex_sharing_chain(2, c_val=0.5)
qcmi, Srq, Seq, Sq = g.qcmi(0.001)
print(f"  QCMI={qcmi:.8f}")
print(f"  S_RQ={Srq:.8f} S_EQ={Seq:.8f} S_Q={Sq:.8f}")
print(f"  Expected: should be near 0 since p→0 means almost deterministic env")

G = g.gram_matrix(0.001)
diag = np.diag(G).real
print(f"  G diagonal: max={np.max(diag):.8f} min={np.min(diag):.8f}")
print(f"  |G| off-diagonal max: {np.max(np.abs(G - np.diag(np.diag(G)))):.2e}")

# ============================================================
# CHECK 5: Very small c — QCMI should be near 0
# ============================================================
print_header("CHECK 5: Small c limit (c→0 should give QCMI→0)")

for c_test in [0.01, 0.05, 0.1]:
    g = make_vertex_sharing_chain(2, c_val=c_test)
    qcmi, _, _, _ = g.qcmi(0.5)
    print(f"  c={c_test:.3f}: QCMI={qcmi:.8f}")

# ============================================================
# CHECK 6: p≠0.5 convergence of delta(QCMI)
# ============================================================
print_header("CHECK 6: delta(QCMI) convergence for p≠0.5")

for p_test in [0.3, 0.5, 0.7]:
    print(f"\n  p={p_test}:")
    deltas = []
    prev_qcmi = 0
    for b1 in range(1, 9):
        g = make_vertex_sharing_chain(b1, c_val=0.5)
        try:
            qcmi, _, _, _ = g.qcmi(p_test)
        except Exception as e:
            print(f"    b1={b1}: FAILED: {e}")
            break
        delta = qcmi - prev_qcmi
        deltas.append(delta)
        prev_qcmi = qcmi
        per_ring = qcmi / b1
        print(f"    b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} delta={delta:.6f}")
    if len(deltas) >= 5:
        # Check convergence
        print(f"    delta sequence: {[f'{d:.4f}' for d in deltas[1:]]}")
        if len(deltas) >= 4:
            ratio = (deltas[-2] - deltas[-1]) / (deltas[-3] - deltas[-2]) if (deltas[-3] - deltas[-2]) != 0 else float('nan')
            print(f"    convergence ratio (last step): {ratio:.3f} (expected ~0.5 for geometric)")

# ============================================================
# CHECK 7: Verify edge-disjoint additivity is exact
# ============================================================
print_header("CHECK 7: Edge-disjoint additivity")

# Build 2 independent rings using disjoint constructor
g2 = make_disjoint_rings(2, c_val=0.5)
qcmi2, _, _, _ = g2.qcmi(0.5)

g1 = make_disjoint_rings(1, c_val=0.5)
qcmi1, _, _, _ = g1.qcmi(0.5)

print(f"  b1=1: QCMI={qcmi1:.8f}")
print(f"  b1=2: QCMI={qcmi2:.8f}")
print(f"  2*b1=1: {2*qcmi1:.8f}")
print(f"  ratio (b1=2)/(2*b1=1): {qcmi2/(2*qcmi1):.10f} (should be 1.0)")

# Also check b1=3
g3 = make_disjoint_rings(3, c_val=0.5)
qcmi3, _, _, _ = g3.qcmi(0.5)
print(f"  b1=3: QCMI={qcmi3:.8f}")
print(f"  3*b1=1: {3*qcmi1:.8f}")
print(f"  ratio (b1=3)/(3*b1=1): {qcmi3/(3*qcmi1):.10f} (should be 1.0)")

# ============================================================
# CHECK 8: Transfer matrix dimension — is it 3×3 or 5×5?
# ============================================================
print_header("CHECK 8: Transfer matrix dimension analysis")

# For vertex-sharing chain, p=0.5:
# G_{a,b} = Π_r cos²(c·Δ_r) where Δ_r ∈ {0, ±2, ±4}
# How many distinct values does cos²(c·Δ) take?
c = 0.5
for Delta in [-4, -2, 0, 2, 4]:
    val = np.cos(c * Delta)**2
    print(f"  Δ={Delta:+2d}: cos²(c·Δ) = {val:.8f}")

# If we use |Δ|, does cos²(c·|Δ|) match?
print("\n  Using absolute value:")
for absDelta in [0, 2, 4]:
    val = np.cos(c * absDelta)**2
    print(f"  |Δ|={absDelta}: cos²(c·|Δ|) = {val:.8f}")

# Check: can Δ=±4 actually occur in a sequential calculation?
# For the MPO, the bond variable between site r and r+1 is related to Δ_r
# Let's enumerate all possible (a_r, a_{r+1}, b_r, b_{r+1}) patterns
print("\n  All possible (S_a, S_b, Δ) triples:")
from collections import Counter
triples = Counter()
for a_r, a_rp1 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    for b_r, b_rp1 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        S_a = a_r + a_rp1
        S_b = b_r + b_rp1
        Delta = S_b - S_a
        triples[(S_a, S_b, Delta)] += 1

for (sa, sb, d), cnt in sorted(triples.items()):
    print(f"  S_a={sa:+2d}, S_b={sb:+2d}, Δ={d:+2d}: {cnt} combinations")

print(f"\n  Unique Δ values: {sorted(set(d for _,_,d in triples.keys()))}")
print(f"  Number of unique Δ: {len(set(d for _,_,d in triples.keys()))}")
print(f"  So transfer matrix should be {len(set(d for _,_,d in triples.keys()))}×{len(set(d for _,_,d in triples.keys()))}")

# ============================================================
# CHECK 9: Edge-sharing chain topology
# ============================================================
print_header("CHECK 9: Edge-sharing chain detailed analysis")

for b1 in range(1, 5):
    g = make_edge_sharing_chain(b1, c_val=0.5)
    qcmi, Srq, Seq, Sq = g.qcmi(0.5)
    per_ring = qcmi / b1 if b1 > 0 else 0
    print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} V={g.V} d_s={g.d_s}")

# Check if edge-sharing has the same degenerate per_ring pattern
print("\n  Per-ring deltas:")
prev = 0
for b1 in range(1, 5):
    g = make_edge_sharing_chain(b1, c_val=0.5)
    qcmi, _, _, _ = g.qcmi(0.5)
    delta = qcmi - prev
    prev = qcmi
    print(f"    b1={b1}: delta(QCMI) = {delta:.6f}")

# ============================================================
# CHECK 10: The "α≈1" claim: what does alpha actually converge to?
# ============================================================
print_header("CHECK 10: Asymptotic alpha analysis")

# Full scan up to b1=8 (vertex-sharing)
qcmis = []
for b1 in range(1, 9):
    g = make_vertex_sharing_chain(b1, c_val=0.5)
    qcmi, _, _, _ = g.qcmi(0.5)
    qcmis.append(qcmi)

print("  b1 | QCMI   | QCMI/b1 | delta   | delta_delta")
print("  ---|--------|---------|---------|------------")
deltas = []
for i, b1 in enumerate(range(1, 9)):
    delta = qcmis[i] - (qcmis[i-1] if i > 0 else 0)
    deltas.append(delta)
    delta_delta = deltas[i] - (deltas[i-1] if i > 0 else 0)
    print(f"  {b1:2d} | {qcmis[i]:.4f} | {qcmis[i]/b1:.4f}  | {delta:.4f}  | {delta_delta:+.4f}")

# Extrapolate
print("\n  Extrapolation of asymptotic delta:")
# delta sequence shows approximately geometric convergence
# delta(n) ≈ δ_∞ + A·r^n
# From deltas: d2=1.1865, d3=1.0829, d4=1.0345, d5=1.0106, d6=1.0009, d7=0.9951, d8=0.9928
# d_n - d_{n-1}: -0.1036, -0.0484, -0.0239, -0.0097, -0.0058, -0.0023
# Ratio of successive differences: 0.467, 0.494, 0.406, 0.598, 0.397
d = deltas[1:]  # skip b1=1
print(f"  d_n - d_{{n-1}} sequence: {[f'{d[i+1]-d[i]:.4f}' for i in range(len(d)-1)]}")
ratios = [(d[i+1]-d[i])/(d[i]-d[i-1]) for i in range(1, len(d)-1) if abs(d[i]-d[i-1]) > 1e-12]
print(f"  Convergence ratios: {[f'{r:.3f}' for r in ratios]}")

# Simple Aitken acceleration
if len(d) >= 4:
    d6, d7, d8 = d[-3], d[-2], d[-1]
    # Aitken: δ_∞ = d8 - (d8-d7)²/(d8-2*d7+d6)
    denom = d8 - 2*d7 + d6
    if abs(denom) > 1e-12:
        delta_inf = d8 - (d8-d7)**2/denom
        print(f"  Aitken extrapolation: δ_∞ ≈ {delta_inf:.6f}")

    # Exponential fit: d_n = δ_∞ + A·e^{-λn}
    # log(d_n - δ_∞) ≈ log(A) - λn
    # Try different δ_∞ to minimize curvature
    import numpy as np
    best_curv = float('inf')
    best_delta = None
    for delta_try in np.linspace(0.98, 0.995, 100):
        vals = [d[i] - delta_try for i in range(len(d))]
        if any(v <= 0 for v in vals):
            continue
        log_vals = np.log(vals)
        n_arr = np.arange(2, 2+len(vals))
        # Check linearity via R² of linear regression
        A = np.vstack([n_arr, np.ones_like(n_arr)]).T
        coeffs = np.linalg.lstsq(A, log_vals, rcond=None)[0]
        pred = A @ coeffs
        ss_res = np.sum((log_vals - pred)**2)
        ss_tot = np.sum((log_vals - np.mean(log_vals))**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
        curv = -r2  # maximize R² = minimize -R²
        if curv < best_curv and r2 > 0.99:
            best_curv = curv
            best_delta = delta_try

    if best_delta:
        print(f"  Best-fit asymptotic δ_∞ ≈ {best_delta:.6f}")

# ============================================================
# CHECK 11: Verify the Gangwar sQNM additivity claim
# ============================================================
print_header("CHECK 11: Independent QCMI for disjoint rings")

# Two separate ring graphs, QCMI should add
qcmis_indep = []
for _ in range(3):
    g = make_disjoint_rings(1, c_val=0.5)
    qcmi, _, _, _ = g.qcmi(0.5)
    qcmis_indep.append(qcmi)

print(f"  Three independent b1=1 rings: {[f'{q:.6f}' for q in qcmis_indep]}")
print(f"  Sum: {sum(qcmis_indep):.6f}")
g3 = make_disjoint_rings(3, c_val=0.5)
qcmi3, _, _, _ = g3.qcmi(0.5)
print(f"  b1=3 combined: {qcmi3:.6f}")
print(f"  Ratio: {qcmi3/sum(qcmis_indep):.10f}")

# ============================================================
# CHECK 12: p-symmetry QCMI(p) = QCMI(1-p) exact check
# ============================================================
print_header("CHECK 12: QCMI(p) = QCMI(1-p) symmetry")

for b1 in [1, 2, 3, 4]:
    g = make_vertex_sharing_chain(b1, c_val=0.5)
    qcmi_p = g.qcmi(0.3)[0]
    qcmi_1mp = g.qcmi(0.7)[0]
    diff = abs(qcmi_p - qcmi_1mp)
    print(f"  b1={b1}: QCMI(0.3)={qcmi_p:.8f} QCMI(0.7)={qcmi_1mp:.8f} diff={diff:.2e}")

# ============================================================
# CHECK 13: Environment qubit independence — crucial assumption
# ============================================================
print_header("CHECK 13: Verify env qubit independence in Gram matrix")

# The factorization relies on env qubits being initially in product state
# which means they're independent. Let's verify this by comparing direct
# Gram computation with the factorization formula for b1=3, p=0.5

g = make_vertex_sharing_chain(3, c_val=0.5)
G_direct = g.gram_matrix(0.5)

# Factorization prediction for p=0.5:
# G[a,b] = Π_{r=0}^{b1-1} cos²(c·Δ_r) where Δ_r = (b_r+b_{r+1}) - (a_r+a_{r+1})
c = 0.5
max_err = 0.0
n_total = 0
n_exact = 0
for a_idx, a in enumerate(product([1, -1], repeat=4)):  # L=b1+1=4 qubits
    for b_idx, b in enumerate(product([1, -1], repeat=4)):
        pred = 1.0
        for r in range(3):  # b1=3 rings
            S_a = a[r] + a[r+1]
            S_b = b[r] + b[r+1]
            Delta = S_b - S_a
            pred *= np.cos(c * Delta)**2
        actual = G_direct[a_idx, b_idx].real
        err = abs(pred - actual)
        max_err = max(max_err, err)
        n_total += 1
        if err < 1e-12:
            n_exact += 1

print(f"  b1=3: {n_exact}/{n_total} entries exact, max error = {max_err:.2e}")

# ============================================================
# CHECK 14: The per-qubit QCMI claim (anti-screening)
# ============================================================
print_header("CHECK 14: Per-qubit QCMI (anti-screening) analysis")

# Document claims per-qubit QCMI increases:
# b1=1: 0.704, 2:0.865, 4:0.942, 8:0.968
# But QCMI/qubit = QCMI / L where L = b1+1 (number of system qubits)
for b1 in [1, 2, 3, 4, 5, 6, 7, 8]:
    g = make_vertex_sharing_chain(b1, c_val=0.5)
    qcmi, _, _, _ = g.qcmi(0.5)
    L = b1 + 1
    per_qubit = qcmi / L
    per_ring = qcmi / b1
    print(f"  b1={b1} L={L}: QCMI={qcmi:.4f} per_qubit={per_qubit:.4f} per_ring={per_ring:.4f}")

# ============================================================
# CHECK 15: Edge-sharing chain — does it converge to 0 or constant?
# ============================================================
print_header("CHECK 15: Edge-sharing asymptotics")

qcmis_es = []
for b1 in range(1, 7):
    g = make_edge_sharing_chain(b1, c_val=0.5)
    qcmi, _, _, _ = g.qcmi(0.5)
    qcmis_es.append(qcmi)

print("  b1 | QCMI    | delta")
for i, b1 in enumerate(range(1, 7)):
    delta = qcmis_es[i] - (qcmis_es[i-1] if i>0 else 0)
    print(f"  {b1:2d} | {qcmis_es[i]:.4f} | {delta:.4f}")

# Check if per_ring is decaying to 0 or to constant
if len(qcmis_es) >= 3:
    # Try exponential fit: QCMI(b1) = A + B·exp(-λ·b1)
    # or power law: QCMI(b1) = A + B·b1^c
    pass  # Not enough data but document trend

print("\nDone.")
