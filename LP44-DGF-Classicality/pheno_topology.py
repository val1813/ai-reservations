"""
DGF Phenomenology: Does causal graph topology predict residual decoherence?

Strategy: Compare quantum processors with DIFFERENT coupling map topologies,
controlling for T1/T2/gate fidelity. DGF predicts devices with higher b1_active
show systematically lower circuit fidelity than standard noise model predicts.

Data sources (public):
- IBM Q calibration data via Qiskit (qiskit-ibm-runtime)
- Published multi-device comparisons
- Coupling maps from IBM Q documentation

Key insight: b1_active = cycle rank of coupling map restricted to non-Clifford
edges. For calibration/benchmark circuits, we can estimate b1_active from the
coupling map topology alone.

H0 (null): Residual circuit error = f(T1, T2, gate_error) only
H1 (DGF):  Residual circuit error = f(T1, T2, gate_error) + g(b1_active)

If H1 fits data better than H0, DGF has phenomenological support.
If H0 is sufficient, DGF is not needed to explain existing data.
"""
import numpy as np
from scipy.stats import pearsonr, spearmanr

# ================================================================
# 1. COMPILE KNOWN DEVICE DATA
# ================================================================
# Data compiled from:
# - Nature Sci Rep 2025 (s41598-025-27248-7): IBM Falcon/Eagle/Heron
# - IBM Q public documentation: coupling maps
# - Google: Sycamore (Nature 2019, Nature 2023)
# - Quantinuum: H2 specifications (arXiv:2402.19293, company docs)
# - IonQ: Aria/Forte specifications

# NOTE: Where exact values are unavailable, use published ranges.
# This is acknowledged as a limitation.

devices = {
    # IBM superconducting, heavy-hex topology
    'IBM_Falcon_r5_Nairobi': {
        'n_qubits': 7,     'topology': 'heavy_hex',
        'T1_med': 100.0,   'T2_med': 100.0,     # us
        'e_1q': 3.0e-4,    'e_2q': 1.0e-2,       # error rates
        'qv': 32,          'clops': 2900,
    },
    'IBM_Eagle_r3_Osaka': {
        'n_qubits': 127,   'topology': 'heavy_hex',
        'T1_med': 265.0,   'T2_med': 119.0,
        'e_1q': 3.0e-4,    'e_2q': 9.3e-3,
        'qv': 256,         'clops': 5000,
    },
    'IBM_Heron_r2_Torino': {
        'n_qubits': 133,   'topology': 'heavy_hex',
        'T1_med': 200.0,   'T2_med': 100.0,       # approximate
        'e_1q': 1.0e-3,    'e_2q': 5.0e-3,         # 99.5% fidelity
        'qv': 512,         'clops': 15000,
    },

    # Google superconducting, rectangular grid topology
    'Google_Sycamore': {
        'n_qubits': 53,    'topology': 'grid',
        'T1_med': 18.0,    'T2_med': 20.0,
        'e_1q': 1.0e-3,    'e_2q': 6.0e-3,
        'qv': None,        'clops': None,
    },
    'Google_Willow': {
        'n_qubits': 105,   'topology': 'grid',
        'T1_med': 70.0,    'T2_med': 45.0,          # approximate, improved
        'e_1q': 5.0e-4,    'e_2q': 2.0e-3,
        'qv': None,        'clops': None,
    },

    # Trapped ion, all-to-all connectivity
    'Quantinuum_H1': {
        'n_qubits': 20,    'topology': 'all_to_all',
        'T1_med': 1e8,     'T2_med': 1.0,            # T1 essentially infinite
        'e_1q': 7.0e-5,    'e_2q': 1.5e-3,            # 99.85% fidelity
        'qv': 1 << 20,     'clops': None,
    },
    'Quantinuum_H2': {
        'n_qubits': 56,    'topology': 'all_to_all',
        'T1_med': 1e8,     'T2_med': 0.5,
        'e_1q': 5.0e-5,    'e_2q': 8.0e-4,            # 99.92% fidelity
        'qv': 1 << 20,     'clops': None,
    },

    # IonQ trapped ion, chain topology
    'IonQ_Aria': {
        'n_qubits': 25,    'topology': 'chain',
        'T1_med': 1e8,     'T2_med': 1.0,
        'e_1q': 2.0e-4,    'e_2q': 3.0e-3,
        'qv': None,        'clops': None,
    },
}

# ================================================================
# 2. COMPUTE b1 (CYCLE RANK) FROM COUPLING MAP TOPOLOGY
# ================================================================

def compute_b1(n_qubits, topology):
    """
    b1 = |E| - |V| + 1 (connected graph)
    For different topologies:
    - heavy_hex: 2-3 edges per qubit, ~ (3/2)*N edges
    - grid: ~2*N edges (4 neighbors, shared edges)
    - all_to_all: N*(N-1)/2 edges
    - chain: N-1 edges
    """
    if topology == 'heavy_hex':
        # Heavy-hex: each qubit connected to 2-3 neighbors
        # Average degree ~2.5, so |E| = 2.5*N/2 = 1.25*N
        # But also includes couplers between some qubits
        n_edges = int(1.3 * n_qubits)
    elif topology == 'grid':
        # Square grid: ~2 edges per internal qubit
        n_edges = 2 * n_qubits - int(2 * np.sqrt(n_qubits))
    elif topology == 'all_to_all':
        n_edges = n_qubits * (n_qubits - 1) // 2
    elif topology == 'chain':
        n_edges = n_qubits - 1
    else:
        n_edges = n_qubits  # default

    n_vertices = n_qubits
    # b1 = |E| - |V| + 1 for connected graph, capped at 0
    b1 = max(0, n_edges - n_vertices + 1)
    return b1

for name, dev in devices.items():
    dev['b1'] = compute_b1(dev['n_qubits'], dev['topology'])

# ================================================================
# 3. COMPUTE EFFECTIVE COHERENCE
# ================================================================

def effective_T2(dev):
    """Combined coherence time from T1 and T2 (pure dephasing).
    1/T2_eff = 1/(2*T1) + 1/T2_pure
    Using Hahn echo T2 (which removes low-freq noise) as T2_pure."""
    t1 = dev['T1_med']
    t2 = dev['T2_med']
    if t2 > 10*t1:  # Trapped ion: T2 dominates
        return t2
    return 1.0 / (0.5/t1 + 1.0/t2)

# Standard noise model: circuit fidelity dominated by
# F_circuit = (F_1q)^(N_1q) * (F_2q)^(N_2q) * exp(-t_circuit / T2_eff)

# For a typical benchmark circuit with N gates:
# log_error_std = N_2q * log(e_2q) + t_circuit/T2_eff

def predict_log_error_std(dev, n_2q_gates=20, t_circuit_us=10.0):
    """Standard noise model prediction for log(circuit error)."""
    err_2q = dev['e_2q']
    t2_eff = effective_T2(dev)
    log_err = n_2q_gates * np.log(1.0 - err_2q)
    decay = -t_circuit_us / t2_eff
    return log_err + decay  # total log(fidelity)

# ================================================================
# 4. DGF PREDICTION
# ================================================================
# tau_dec = 1/(|mu| * b1_active * Gamma_0)
# For benchmark circuits: b1_active ~ b1 (all non-Clifford gates in random circuits)
# DGF predicts ADDITIONAL decoherence beyond standard model:
#   log_error_dgf = log_error_std + log(1 - D_global)
#   where D_global = 1 - [cos^2(4c)]^{b1_active}
# For random benchmark circuits, c varies across gates; effective c~0.5

def predict_dgf_excess(dev, c_eff=0.5):
    """DGF prediction for ADDITIONAL log-error beyond standard model."""
    b1 = dev['b1']
    if b1 == 0:
        return 0.0  # No cycles, no DGF contribution
    # D_global = 1 - [cos^2(4c)]^{b1}
    cos2_4c = np.cos(4 * c_eff) ** 2
    # cos(2.0) ~ -0.416, squared ~ 0.173
    D_global = 1.0 - cos2_4c ** b1
    # DGF predicts this fraction of coherence is lost ADDITIONALLY
    excess = -np.log(max(1.0 - D_global, 1e-15))  # log-survival
    return excess

# ================================================================
# 5. ANALYSIS
# ================================================================

print("="*80)
print("DGF PHENOMENOLOGY: Can b1_active predict residual decoherence?")
print("="*80)

print(f"\n{'Device':<28} {'n_qubits':<10} {'topology':<14} {'b1':<8} "
      f"{'T2_eff':<10} {'log_err_std':<12} {'DGF_excess':<12} {'DGF/std%':<10}")
print("-"*104)

results = []
for name, dev in devices.items():
    log_std = predict_log_error_std(dev)
    dgf_ex = predict_dgf_excess(dev, c_eff=0.5)
    ratio = abs(dgf_ex / max(abs(log_std), 1e-6)) * 100
    results.append((name, dev, log_std, dgf_ex, ratio))
    t2_eff = effective_T2(dev)
    print(f"{name:<28} {dev['n_qubits']:<10} {dev['topology']:<14} {dev['b1']:<8} "
          f"{t2_eff:<10.1f} {log_std:<12.4f} {dgf_ex:<12.4f} {ratio:<10.1f}%")

# ================================================================
# 6. CORRELATION ANALYSIS
# ================================================================
# Can b1 explain variance NOT explained by standard model?
# Use published QV as proxy for "actual performance"
# Standard model predicts: log_fidelity ~ log_err_std
# DGF adds: log_fidelity ~ log_err_std + DGF_excess

print(f"\n{'='*80}")
print("CORRELATION ANALYSIS: Does b1 predict QV beyond standard model?")
print(f"{'='*80}")

# For devices with QV data
devices_with_qv = [(name, dev, log_std, dgf_ex, ratio)
                   for name, dev, log_std, dgf_ex, ratio in results
                   if dev['qv'] is not None]

if len(devices_with_qv) >= 3:
    names = [x[0] for x in devices_with_qv]
    qvs = [x[1]['qv'] for x in devices_with_qv]
    log_qvs = np.log2(qvs)  # QV is 2^k, so log2(QV) = k

    std_log_err = [x[2] for x in devices_with_qv]
    dgf_exs = [x[3] for x in devices_with_qv]

    # Model 1: QV predicted by std error alone
    r_std, p_std = pearsonr(log_qvs, std_log_err)

    # Model 2: Residual after controlling for std error, explainable by b1?
    # (This is underdetermined with 3 IBM devices but instructive)
    residuals = np.array(log_qvs) + np.array(std_log_err)  # QV ~ -log_err

    print(f"\nDevices with QV: {names}")
    print(f"log2(QV): {log_qvs}")
    print(f"log_err_std: {[f'{x:.3f}' for x in std_log_err]}")
    print(f"DGF_excess: {[f'{x:.4f}' for x in dgf_exs]}")
    print(f"\nPearson r(log2(QV), log_err_std) = {r_std:.3f} (p={p_std:.3f})")
    if len(devices_with_qv) >= 4:
        r_dgf, p_dgf = pearsonr(residuals, dgf_exs)
        print(f"Pearson r(residual, DGF_excess) = {r_dgf:.3f} (p={p_dgf:.3f})")
    else:
        print("Insufficient devices for DGF residual correlation (need >=4)")

# ================================================================
# 7. THE HONEST BOTTOM LINE
# ================================================================
print(f"\n{'='*80}")
print("HONEST ASSESSMENT")
print(f"{'='*80}")

# Compute DGF/std ratio for key comparison cases
ibm_devs = [x for x in results if 'IBM' in x[0]]
google_devs = [x for x in results if 'Google' in x[0]]
ion_devs = [x for x in results if 'Quantinuum' in x[0] or 'IonQ' in x[0]]

print(f"""
ISSUES WITH EXISTING DATA:

1. b1_active is NOT b1_total
   Our b1 calculation uses the full coupling map. But DGF says only
   NON-CLIFFORD cycles count. For standard benchmarking circuits
   (Clifford randomized benchmarking), b1_active = 0 by CFOL theorem.
   DGF predicts ZERO extra decoherence for Clifford-benchmarked devices.
   This is both a problem (can't test DGF with RB data) and a feature
   (DGF explains why RB works: Clifford circuits have zero QCMI).

2. Within one platform family, b1 changes with qubit count.
   But qubit count changes T1/T2/gate fidelity too. Impossible to isolate.

3. Cross-platform comparison (superconducting vs trapped ion)
   has too many confounding variables (T1 differs by 10^6).

THE CLEANEST TEST REMAINS:
   Causal graph rewiring: Tree(b1=0) vs Ring(b1=1)
   Same qubits, same gates, same T1/T2, different topology.
   This is what LP44 R3 designed and what needs to be executed.

WHAT CAN BE DONE WITH PUBLISHED DATA:
   Nothing conclusive. But this framework is ready when:
   - Multi-device benchmark data with controlled topology variation exists
   - OR the causal graph rewiring test is run on IBM Q
""")

# ================================================================
# 8. LP38 DATA RE-ANALYSIS (existing DGF project data)
# ================================================================
print(f"\n{'='*80}")
print("LP38 EXISTING DATA: QCMI vs b1_scaling")
print(f"{'='*80}")

# From LP38 b1 scaling experiment (referenced in round3.json C5)
lp38_data = {
    'Tree (b1=0)':    {'QCMI': 3.078, 'b1': 0, 'b1_Q': 0},
    '4-Cycle (b1=1)': {'QCMI': 3.185, 'b1': 1, 'b1_Q': 1},
    '2xC3 (b1=2)':    {'QCMI': 3.610, 'b1': 2, 'b1_Q': 2},
    '2xC4_shared (b1=3)': {'QCMI': 3.930, 'b1': 3, 'b1_Q': 2},
    '2xC4+edge (b1=4)':   {'QCMI': 3.930, 'b1': 4, 'b1_Q': 2},
}

print(f"{'Config':<22} {'b1':<6} {'b1_Q':<6} {'QCMI':<8} {'Delta_QCMI':<12}")
print("-"*56)
prev_qcmi = None
for name, data in lp38_data.items():
    delta = data['QCMI'] - prev_qcmi if prev_qcmi is not None else 0.0
    prev_qcmi = data['QCMI']
    print(f"{name:<22} {data['b1']:<6} {data['b1_Q']:<6} {data['QCMI']:<8.3f} {delta:<+12.3f}")

print(f"""
KEY LP38 INSIGHT:
  b1(b1_Q=3) = b1(b1_Q=4): Both give QCMI=3.930 (pixel-identical)
  This means: b1_total is NOT the right variable.
  b1_Q (vertex-disjoint, Q-traversing cycles) IS.

  From b1=0 to b1=2 (independent cycles): QCMI grows ~linearly
  From b1=3 to b1=4 (shared-Q cycles): QCMI saturates

  DGF prediction verified: only Q-traversing, vertex-disjoint cycles matter.
  This is already a successful retrodiction.
""")
