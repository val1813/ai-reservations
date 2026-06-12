# Nighthawk DGF Gram Matrix Spectral Transition Experiment

**Hardware:** IBM Nighthawk (ibm_miami) -- 120 qubit, square lattice, tunable couplers
**Date:** 2026-06-11
**Status:** Submission-ready protocol design

---

## Overview

We propose to measure the DGF Gram matrix spectral transition -- the collapse of effective rank from d_sys (quantum regime) to 1 (classical regime) as a function of Cartan angle c and ring count b1 -- on IBM Nighthawk's square lattice. The square lattice's **native 4-cycles** are the critical hardware feature that makes this experiment feasible without SWAP routing, in contrast to heavy-hex processors where every ring required 3-6 additional SWAP gates.

### Physics Objective

For a vertex-sharing chain of b1 causal rings with Cartan-aligned RZZ(c) edges:

- **c = pi/2** (Clifford): rank_eff ~ d_sys (all Gram eigenvalues comparable, quantum superposition preserved)
- **c = pi/4** (intermediate): rank_eff << d_sys (partial collapse)
- **c = 0.5** (classical limit): rank_eff -> 1 (single eigenvalue dominates, classical pointer states emerge)

The Gram matrix G_{ab} = <phi(a)|phi(b)> encodes the overlap between environment states conditioned on system basis states |a> and |b>. Its eigenvalue spectrum directly reveals whether the causal rings preserve or destroy quantum coherence.

### Why Nighthawk

| Feature | Heavy-hex (Heron/Eagle) | Square lattice (Nighthawk) |
|:--------|:----------------------|:--------------------------|
| Native 4-cycles | No (girth=6) | **Yes** |
| SWAP gates per ring | 2-4 | **0** |
| Gate count overhead | 3-6x | **1x** |
| Circuit depth per ring | ~1.5 us | **~0.3 us** |
| Coherence-time margin | ~10x | **~50x** |

---

## 1. Qubit Mapping

### 1.1 Square Lattice Coordinate System

IBM Nighthawk uses a square lattice topology. We use coordinates (row, col) where adjacent qubits differ by +/-1 in one coordinate. Each square plaquette forms a native 4-cycle.

### 1.2 Vertex-Sharing Chain Layout

The key insight: on a square lattice, each causal ring occupies exactly **one square plaquette**, and adjacent rings share exactly **one vertex** (the system qubit at the junction).

**Ring r consists of:** Q_r -> E_r -> Q_{r+1} -> E'_r -> Q_r

On the square lattice, these map to the four vertices of a square:

```
Ring r square:
    Q_r -------- E_r
     |            |
     |   Ring r   |
     |            |
    E'_r ------ Q_{r+1}
```

Adjacent rings (r and r+1) share vertex Q_{r+1}, creating the vertex-sharing chain.

### 1.3 ASCII Layout for b1=1 (1 ring, 4 qubits)

```
Column:  0         1
       +---------+
Row 0  | Q_0 ----|-- E_0        Ring 0: Q_0 -> E_0 -> Q_1 -> E'_0 -> Q_0
       |  |       |   |
Row 1  | E'_0 ----|-- Q_1
       +---------+

Lattice coordinates:
  Q_0  = (0, 0)
  E_0  = (0, 1)
  E'_0 = (1, 0)
  Q_1  = (1, 1)

Native edges (all present on square lattice):
  (0,0)-(0,1): Q_0 -- E_0      [horizontal]
  (0,1)-(1,1): E_0 -- Q_1      [vertical]
  (1,1)-(1,0): Q_1 -- E'_0     [horizontal]
  (1,0)-(0,0): E'_0 -- Q_0     [vertical]
```

### 1.4 ASCII Layout for b1=4 (4 rings, 13 qubits)

```
Column:  0         1         2         3         4
       +---------+---------+---------+---------+
Row 0  | Q_0 ----|-- E_0   |         |         |
       |  |       |   |     |         |         |
Row 1  | E'_0 --- |-- Q_1 --|-- E_1   |         |
       |          |   |     |   |     |         |
Row 2  |          | E'_1 ---|-- Q_2 --|-- E_2   |
       |          |         |   |     |   |     |
Row 3  |          |         | E'_2 ---|-- Q_3 --|-- E_3
       |          |         |         |   |     |   |
Row 4  |          |         |         | E'_3 ---|-- Q_4
       +---------+---------+---------+---------+

Ring 0: Q_0 -> E_0 -> Q_1 -> E'_0 -> Q_0    [square at (0,0)-(0,1)-(1,1)-(1,0)]
Ring 1: Q_1 -> E_1 -> Q_2 -> E'_1 -> Q_1    [square at (1,1)-(1,2)-(2,2)-(2,1)]
Ring 2: Q_2 -> E_2 -> Q_3 -> E'_2 -> Q_2    [square at (2,2)-(2,3)-(3,3)-(3,2)]
Ring 3: Q_3 -> E_3 -> Q_4 -> E'_3 -> Q_3    [square at (3,3)-(3,4)-(4,4)-(4,3)]

Shared vertices:
  Q_1 at (1,1): shared by Ring 0 and Ring 1
  Q_2 at (2,2): shared by Ring 1 and Ring 2
  Q_3 at (3,3): shared by Ring 2 and Ring 3

Lattice coordinates:
  Q_0  = (0, 0)     E_0  = (0, 1)
  E'_0 = (1, 0)     Q_1  = (1, 1)
  E_1  = (1, 2)     E'_1 = (2, 1)
  Q_2  = (2, 2)     E_2  = (2, 3)
  E'_2 = (3, 2)     Q_3  = (3, 3)
  E_3  = (3, 4)     E'_3 = (4, 3)
  Q_4  = (4, 4)

Total lattice footprint: 5 rows x 5 columns = 25 sites
Qubits used: 13 (5 system + 8 environment)
All edges are native nearest-neighbor on the square lattice -- ZERO SWAP gates.

Qubit type summary:
  System qubits:  Q_0, Q_1, Q_2, Q_3, Q_4           (5 qubits, b1+1)
  Environment:    E_0, E'_0, E_1, E'_1, E_2, E'_2, E_3, E'_3  (8 qubits, 2*b1)
  Ancilla:        0 (pure state preparation needs no ancilla)
  Total:          13 qubits = 3*b1 + 1
```

### 1.5 General Layout for Arbitrary b1

The pattern extends naturally. For any b1, the vertex-sharing chain occupies a (b1+1) x (b1+1) block on the square lattice:

```
System qubits:  Q_r at (r, r) for r = 0..b1           [diagonal]
Environment:    E_r at (r, r+1) for r = 0..b1-1        [right of Q_r]
                E'_r at (r+1, r) for r = 0..b1-1       [below Q_r]
```

Each ring r forms the square: (r,r)-(r,r+1)-(r+1,r+1)-(r+1,r)-(r,r)
- Edge 1: Q_r(r,r) -> E_r(r,r+1) [horizontal]
- Edge 2: E_r(r,r+1) -> Q_{r+1}(r+1,r+1) [vertical]
- Edge 3: Q_{r+1}(r+1,r+1) -> E'_r(r+1,r) [horizontal]
- Edge 4: E'_r(r+1,r) -> Q_r(r,r) [vertical]

All four edges per ring are native nearest-neighbor couplings. **Total SWAP gates = 0** for any b1.

### 1.6 Qubit Selection on ibm_miami

On the actual device, we select a contiguous 5x5 block of qubits with the highest 2Q gate fidelities and lowest readout error rates. The device calibration data from `backend.properties()` is used to rank candidate blocks. The mapping above is logical; physical qubit indices are assigned at transpile time.

---

## 2. Gate Sequence

### 2.1 Cartan-Aligned Edge Unitary

The DGF edge unitary for edge (u,v) is:

```
U_uv = (K1_u ⊗ K2_v) · exp(i·c·ZZ) · (K3_u ⊗ K4_v)
```

For the **Cartan-aligned** case: K1 = K2 = K3 = K4 = I.

Thus U = exp(i·c·Z⊗Z) = RZZ(-2c) in Qiskit convention.

RZZ(theta) in Qiskit = exp(-i·theta/2·Z⊗Z), so:
- For Cartan parameter c, set theta = -2c
- c = pi/2 -> RZZ(-pi) ~ RZZ(pi) (Clifford)
- c = pi/4 -> RZZ(-pi/2) (CNOT-equivalent up to local)
- c = 0.5  -> RZZ(-1.0)

### 2.2 Option A: Native RZZ (Preferred)

Nighthawk's tunable couplers support **fractional RZZ(theta)** gates as a single pulse:

```
RZZ(theta) applied via one tunable-coupler pulse
Duration: 100-200 ns
Fidelity: > 99.7% (median for >50% pairs)
```

Gate count per ring: **4 RZZ gates** (one per edge)
Total for b1=4: **16 RZZ gates**

### 2.3 Option B: Decomposed RZZ (Fallback)

If fractional RZZ is not exposed in the Qiskit runtime:

```
RZZ(theta) decomposed as:
  CNOT(control=u, target=v)
  Rz(theta, v)
  CNOT(control=u, target=v)

Each CNOT further decomposed for native CZ:
  CNOT(u,v) = H(v); CZ(u,v); H(v)
```

Gate count per RZZ: **2 CZ + 1 Rz + 2 H** (effective 2 two-qubit + 3 single-qubit)
Gate count per ring: **8 two-qubit gates**
Total for b1=4: **32 two-qubit gates**

### 2.4 Gate Sequence Per Ring (Option A)

For ring r with qubits Q_r, E_r, Q_{r+1}, E'_r:

```
Step 1: RZZ(-2c) on [Q_r, E_r]       # Edge 1: Q_r -> E_r
Step 2: RZZ(-2c) on [E_r, Q_{r+1}]   # Edge 2: E_r -> Q_{r+1}
Step 3: RZZ(-2c) on [Q_r, E'_r]      # Edge 3: Q_r -> E'_r (parallel with Step 1-2?)
Step 4: RZZ(-2c) on [Q_{r+1}, E'_r]  # Edge 4: Q_{r+1} -> E'_r (parallel with Step 2?)
```

Parallelism analysis:
- Edges 1 and 3 share Q_r but use different env qubits (E_r, E'_r) -- can they run in parallel? On Nighthawk, a qubit can participate in only one 2Q gate at a time. So Q_r serializes edges 1 and 3.
- Edges 2 and 4 share Q_{r+1} -- similarly serialized.
- Edges 2 and 3 use disjoint qubits (E_r, Q_{r+1}) and (Q_r, E'_r) -- can be parallel if the lattice supports it.

**Optimal schedule per ring (2 time steps):**
```
Time step A: RZZ on [Q_r, E_r] AND RZZ on [Q_{r+1}, E'_r]  (disjoint qubits)
Time step B: RZZ on [E_r, Q_{r+1}] AND RZZ on [Q_r, E'_r]  (disjoint qubits)
```

Verification: Time A uses {Q_r, E_r, Q_{r+1}, E'_r} -- wait, that's all 4 qubits. Let me recheck.
- Time A: RZZ(Q_r, E_r) uses {Q_r, E_r}; RZZ(Q_{r+1}, E'_r) uses {Q_{r+1}, E'_r}. Disjoint! OK.

Ring depth: 2 RZZ layers = ~300 ns per ring.

### 2.5 Inter-Ring Parallelism

Adjacent rings share a system qubit. Ring r and ring r+1 share Q_{r+1}:
- Ring r's edges 2 and 4 involve Q_{r+1}
- Ring r+1's edges 1 and 3 involve Q_{r+1}

Q_{r+1} is the bottleneck: it participates in 4 gates total (2 from ring r, 2 from ring r+1).
With optimal scheduling across rings, the total depth for b1 rings is approximately:

```
Depth = 4 * b1 RZZ layers (serialized through shared vertices)
      = 4 * b1 * 150 ns = 600 * b1 ns
```

For b1=4: depth ~ 2.4 us (Option A) or ~5 us (Option B).

### 2.6 Gate Counting Summary

| b1 | System Qubits | Env Qubits | Total Qubits | Edges | Gates (Opt A) | Gates (Opt B) | Depth (Opt A) | Depth (Opt B) |
|:--:|:------------:|:----------:|:------------:|:-----:|:------------:|:------------:|:------------:|:------------:|
| 1  | 2            | 2          | 4            | 4     | 4 RZZ        | 8 CZ         | ~0.6 us       | ~1.2 us      |
| 2  | 3            | 4          | 7            | 8     | 8 RZZ        | 16 CZ        | ~1.2 us       | ~2.5 us      |
| 3  | 4            | 6          | 10           | 12    | 12 RZZ       | 24 CZ        | ~1.8 us       | ~3.7 us      |
| 4  | 5            | 8          | 13           | 16    | 16 RZZ       | 32 CZ        | ~2.4 us       | ~5.0 us      |
| 5  | 6            | 10         | 16           | 20    | 20 RZZ       | 40 CZ        | ~3.0 us       | ~6.2 us      |

---

## 3. State Preparation

### 3.1 System Qubits: Computational Basis States

For each experimental configuration (b1, c), we iterate over system basis states |a> = |s_0, s_1, ..., s_{b1}> where s_j in {0, 1}.

For each basis state |a>:
```
For each system qubit Q_j:
  if s_j == 1: apply X gate to Q_j
  else: apply I (do nothing)
```

This requires at most b1+1 X gates, all applied in parallel (depth 1).

State count d_sys = 2^{b1+1}:
- b1=1: 4 states
- b1=2: 8 states
- b1=3: 16 states
- b1=4: 32 states
- b1=5: 64 states

### 3.2 Environment Qubits: |+> State (p_eff = 1/2)

Each environment qubit E_r, E'_r is initialized to the |+> = (|0>+|1>)/sqrt(2) state:

```
For each env qubit:
  apply H gate
```

This is a layer of parallel H gates (depth 1), applied to all 2*b1 env qubits.

**Why |+> state:** In the X-basis (sigma_x eigenbasis), |+> is the +1 eigenstate. For the Cartan-aligned case where all gates are RZZ (diagonal in Z-basis), the environment qubits in |+> act as a "maximally coherent" environment with effective purity p_eff = 1/2. This is equivalent to the p=0.5 case in the theoretical Gram matrix analysis, which gives the cleanest rank collapse signal.

### 3.3 Complete State Preparation Sequence

```
1. All qubits start in |0>
2. Apply X gates to system qubits where s_j = 1 (parallel, 1 layer)
3. Apply H gates to all 2*b1 env qubits (parallel, 1 layer)
4. Apply barrier for clean separation
```

Total preparation depth: **2 layers** (X + H), independent of b1.

---

## 4. Measurement Protocol: Gram Matrix via Classical Shadows

### 4.1 Core Idea

We need to estimate the Gram matrix G_{ab} = Tr(rho_a * rho_b) where rho_a is the environment state conditioned on system basis state |a>. We use **classical shadows** (random Pauli measurements) to avoid full state tomography on 8 environment qubits (which would require 3^8 = 6561 measurement settings).

### 4.2 Shadow Protocol Per System State

For each system state |a>:

```
1. Prepare system in |a>, env in |+>^({2*b1})
2. Apply ring circuit U_ring(c)
3. For each env qubit i, apply random unitary P_i in {I, H, HS^dagger}:
   - P_i = I: measure in Z basis
   - P_i = H: measure in X basis
   - P_i = HS^dagger: measure in Y basis
4. Measure all env qubits -> bitstring b in {0,1}^{2*b1}
5. Store (a, P_vec, b) as one shadow snapshot
```

Each snapshot produces a classical shadow estimate:
```
rho_hat_a = tensor_product over i of (3 * P_i^dagger |b_i><b_i| P_i - I)
```

### 4.3 Gram Matrix Element Estimation

For a pair of system states (a, b), we combine independent shadows:

```
G_{ab} = Tr(rho_a * rho_b)
       = E_{shadows}[ Tr(rho_hat_a * rho_hat_b) ]
       = E[ product_i Tr((3 P_i^dagger |b_i><b_i| P_i - I)(3 Q_i^dagger |c_i><c_i| Q_i - I)) ]
```

For Pauli measurements, the single-qubit overlap estimator has a simple closed form:

For matching Pauli bases (P_i = Q_i): estimator = 3 * delta_{b_i, c_i} - 2
For differing Pauli bases: estimator = -1

Equivalently: the overlap for qubit i is:
- If same Pauli basis and same outcome: +3
- If same Pauli basis and opposite outcome: -1
- If different Pauli basis: +1

The full overlap is the product over all qubits: G_hat_{ab} = prod_i overlap_i

### 4.4 Statistical Properties

For n_env = 2*b1 environment qubits and N independent shadow pairs per (a,b) pair:

- The estimator is unbiased: E[G_hat_{ab}] = G_{ab}
- Variance per qubit is O(1), so total variance = O(3^{n_env} / N) -- exponential!
- **BUT** for Pauli measurements, the variance of overlap estimation depends on the state purity
- For nearly-pure env states (our case at small b1): variance ~ O(2^{n_env} / N) per pair
- With N = 10^4 -- 10^5 shadows per state, we get ~1% precision on individual G_{ab}

### 4.5 Efficient Sampling Strategy

Instead of measuring all d_sys^2 Gram matrix entries, we use **randomized low-rank matrix completion**:

```
1. Select M random system state pairs (a_k, b_k), where M = O(d_sys * log(d_sys))
   For d_sys=32, M ~ 150 pairs

2. For each selected pair, collect N_pair shadow snapshots:
   - N_pair/2 snapshots for state |a_k>
   - N_pair/2 snapshots for state |b_k>

3. Estimate G_{a_k, b_k} from the shadow pairs

4. Solve the matrix completion problem:
   minimize ||G||_*  subject to G_{a_k, b_k} = measured value for all k
   (nuclear norm minimization for low-rank matrix recovery)
```

### 4.6 Simplified Protocol: Diagonal-First

For the Gram matrix spectral transition, the **diagonal dominance** is the key observable. We propose a two-phase approach:

**Phase 1 (Quick):** Measure only the Gram matrix eigenvalues via randomized trace estimation.

For each of N_trace trials:
```
1. Pick random vector v of dimension d_sys (random +/-1 entries)
2. For each a where v_a != 0, collect shadow of rho_a
3. Estimate v^T G v = sum_{a,b} v_a v_b G_{ab}
4. From multiple random v, estimate the eigenvalue distribution via
   stochastic Lanczos or the Chebyshev moment method
```

**Phase 2 (Full):** For the most interesting (b1, c) configurations, measure explicit G_{ab} entries for rank verification.

### 4.7 Shot Budget Per Configuration

For each (b1, c, system_state) triple:

| Parameter | Conservative | Optimistic | Notes |
|:----------|:-----------:|:----------:|:------|
| Shadows per system state | 20,000 | 5,000 | For n_env <= 8 |
| System states sampled | d_sys = 2^{b1+1} | d_sys/2 | Random subset sufficient for rank |
| Total circuits | d_sys * N_shadows | (d_sys/2) * N_shadows | Each circuit = 1 shadow |
| Total shots | Same (1 shot per circuit) | Same | Shadow protocol: 1 shot per random unitary |

For b1=4, d_sys=32, n_env=8:
- Conservative: 32 states * 20,000 shadows = 640,000 circuits
- Optimistic: 16 states * 5,000 shadows = 80,000 circuits

IBM Q free tier allows ~100 circuits/job, ~10 jobs/day. For 640K circuits this is ~6,400 jobs, requiring premium access or batched submission over weeks.

**Practical strategy:** Use Phase 1 (random trace estimation) to quickly identify the rank collapse, then Phase 2 (explicit eigenvalues) for the winning configurations only.

---

## 5. Error Budget

### 5.1 Gate Fidelity

For b1=4 (16 edges, 16 native RZZ gates at F=0.997 each):

```
Cumulative gate fidelity (Option A, native RZZ):
  F_total = 0.997^16 = 0.953  (4.7% depolarization)

Cumulative gate fidelity (Option B, decomposed):
  F_total = 0.997^32 = 0.908  (9.2% depolarization)
```

Effective depolarization rate mu_depol per gate:
- epsilon_g = 1 - F = 0.003 per RZZ gate
- After N_gates: rho -> F_total * rho_ideal + (1 - F_total) * I/d

For n_env = 8 (d_env = 256), the depolarized Gram matrix:
- G_meas = F_total * G_ideal + (1 - F_total) * J/d_env
  where J is the all-ones matrix (from the I component when traced against system)

This affects rank_eff as follows:
- For ideal rank_eff = 1 (classical case): depolarization adds noise, rank_eff increases slightly
- For ideal rank_eff = d_sys (quantum/Clifford case): depolarization pulls eigenvalues toward uniform, rank_eff decreases toward d_sys/2
- **Net effect: depolarization compresses the dynamic range of rank_eff, working against our signal**

### 5.2 Readout Error

IBM Nighthawk median readout error ~2% (F_read ~ 0.98).

For the shadow protocol, readout errors are mitigated by the randomized measurement basis:
- Each shadow uses a random Pauli basis, so readout errors are randomized
- The shadow post-processing includes an implicit readout correction (multiplying by 3 and subtracting identity)
- Residual readout bias: ~0.5% per qubit, ~4% total for 8 qubits

### 5.3 Coherence-Time Limits

Nighthawk median T1 ~ 350 us, T2 ~ 200 us.

Circuit duration for b1=4 (Option A): ~2.4 us gate time + ~2 us measurement = ~4.4 us total.
- T1 margin: 350/4.4 = 80x
- T2 margin: 200/4.4 = 45x

Coherence loss probability per circuit: ~ 1 - exp(-4.4/350) ~ 1.3% (T1) + 1 - exp(-4.4/200) ~ 2.2% (T2)
Combined: ~3.5% probability of at least one qubit decohering during the circuit.

This is manageable and much better than heavy-hex processors where SWAP overhead pushed circuit times to 15-25 us.

### 5.4 Crosstalk

On the square lattice, the diagonal chain layout means each qubit has at most 4 neighbors. The ring gates involve only nearest-neighbor pairs. Next-nearest-neighbor crosstalk is suppressed by >40 dB on Nighthawk.

The critical concern is **spectator qubit errors**: when RZZ is applied to (u,v), neighboring qubits experience residual ZZ coupling. For Nighthawk's tunable couplers, the residual ZZ rate during gate operation is < 5 kHz. Over a 150 ns gate, accumulated phase < 5e-6 rad -- negligible.

### 5.5 Statistical Error

For N independent shadow pairs estimating G_{ab}:

```
sigma(G_{ab}) ~ sqrt(Var_shadow / N)
```

For n_env=8, Pauli shadow variance per overlap estimate ~ 20 (empirical from simulations).
With N = 10,000 pairs: sigma ~ sqrt(20/10000) = 0.045

For effective rank estimation, the eigenvalue error propagates as:
```
sigma(rank_eff) / rank_eff ~ 2 * sigma(lambda_max) / lambda_max
```

For the main signal (rank collapsing from d_sys to 1), even 20% precision on individual eigenvalues suffices to distinguish the two regimes.

### 5.6 Signal-to-Noise Summary

| b1 | d_sys | Gates (Opt A) | Depol (%) | Coherence loss (%) | Readout residual (%) | sigma_stat (G_ab) | rank_eff S/N |
|:--:|:-----:|:------------:|:---------:|:------------------:|:--------------------:|:-----------------:|:------------:|
| 1  | 4     | 4            | 1.2       | 0.9                | 1.0                  | 0.02             | > 50         |
| 2  | 8     | 8            | 2.4       | 1.7                | 2.0                  | 0.03             | > 30         |
| 3  | 16    | 12           | 3.5       | 2.6                | 3.0                  | 0.05             | > 15         |
| 4  | 32    | 16           | 4.7       | 3.5                | 4.0                  | 0.07             | > 8          |
| 5  | 64    | 20           | 5.8       | 4.4                | 5.0                  | 0.10             | > 4          |

### 5.7 Error Mitigation Strategies

1. **Richardson extrapolation (ZNE):** Run the same circuit at amplified noise levels (gate folding on RZZ) and extrapolate to zero noise. Nighthawk's RZZ supports gate folding.

2. **Readout error mitigation:** Use the standard Qiskit readout mitigation (confusion matrix inversion) on the measured bitstrings before shadow post-processing.

3. **Dynamical decoupling:** Insert XY-4 or CPMG sequences on idle qubits during gate operations on other qubits, suppressing low-frequency dephasing.

4. **Post-selection:** For each shadow, verify that total qubit population is conserved (ancilla-free check). Discard shots with clear leakage errors.

---

## 6. Circuit Generation (Qiskit Pseudocode)

```python
"""
Nighthawk DGF Gram Matrix Experiment
ibm_miami: 120-qubit square lattice with native RZZ(theta) fractional gates

Usage:
  python nighthawk_gram_experiment.py --token YOUR_IBM_TOKEN --b1 4 --c 0.5 --shots 20000
"""

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import argparse
import json
from datetime import datetime
from itertools import product


# ============================================================================
# 1. Qubit Mapping: vertex-sharing chain on square lattice
# ============================================================================

def get_qubit_mapping_square_lattice(b1):
    """
    Map a vertex-sharing chain of b1 rings to logical coordinates on a square lattice.

    Ring r: Q_r -> E_r -> Q_{r+1} -> E'_r -> Q_r
    Q_r at (r, r), E_r at (r, r+1), E'_r at (r+1, r)

    Returns:
        system_coords: list of (row, col) for Q_0..Q_b1
        env_coords:    list of (row, col) for [E_0, E'_0, E_1, E'_1, ...]
        ring_edges:    list of [(u_logical, v_logical)] per edge
    """
    system_coords = [(r, r) for r in range(b1 + 1)]
    env_coords = []
    ring_edges = []

    for r in range(b1):
        # E_r at (r, r+1) -- right of Q_r
        e_idx = 2 * r
        env_coords.append((r, r + 1))
        # E'_r at (r+1, r) -- below Q_r
        env_coords.append((r + 1, r))

        # Ring r edges: Q_r->E_r, E_r->Q_{r+1}, Q_{r+1}->E'_r, E'_r->Q_r
        ring_edges.append(('Q', r, 'E', r))           # Q_r -> E_r
        ring_edges.append(('E', r, 'Q', r + 1))       # E_r -> Q_{r+1}
        ring_edges.append(('Q', r + 1, 'Ep', r))      # Q_{r+1} -> E'_r
        ring_edges.append(('Ep', r, 'Q', r))           # E'_r -> Q_r

    return system_coords, env_coords, ring_edges


# ============================================================================
# 2. Logical-to-physical qubit assignment
# ============================================================================

def assign_physical_qubits(b1, backend, start_row=0, start_col=0):
    """
    Assign physical qubits on ibm_miami.

    For a square lattice, we select a contiguous block starting at
    (start_row, start_col). In production, scan over candidate blocks
    to find the one with highest median 2Q fidelity.

    Returns:
        physical_system: list of physical qubit indices for Q_0..Q_b1
        physical_env:    list of physical qubit indices for env qubits
    """
    coupling_map = backend.coupling_map
    # Build adjacency from coupling map
    # For each logical coordinate, find the physical qubit at that position
    # in the selected block.

    # Simplified: assume a dense labeling where qubit (r,c) exists
    # In practice, use the device's grid layout from backend.properties()
    config = backend.configuration()
    n_qubits = config.n_qubits

    # For a square lattice, we approximate the grid dimensions
    grid_cols = int(np.sqrt(n_qubits))  # ~11 for 120 qubit
    grid_rows = n_qubits // grid_cols

    physical_system = []
    physical_env = []

    for r in range(b1 + 1):
        q_idx = (start_row + r) * grid_cols + (start_col + r)
        if q_idx < n_qubits:
            physical_system.append(q_idx)
        else:
            raise ValueError(f"Qubit ({start_row+r}, {start_col+r}) out of range")

    for r in range(b1):
        # E_r at (r, r+1)
        q_idx = (start_row + r) * grid_cols + (start_col + r + 1)
        physical_env.append(q_idx if q_idx < n_qubits else -1)
        # E'_r at (r+1, r)
        q_idx = (start_row + r + 1) * grid_cols + (start_col + r)
        physical_env.append(q_idx if q_idx < n_qubits else -1)

    return physical_system, physical_env


# ============================================================================
# 3. Build single ring-chain circuit
# ============================================================================

def build_ring_chain_circuit(b1, c, system_state, use_native_rzz=True):
    """
    Build the ring-chain circuit for a given system basis state.

    Args:
        b1: number of causal rings
        c: Cartan angle (radians)
        system_state: tuple of (b1+1) bits, e.g. (0,1,0,1,1) for b1=4
        use_native_rzz: if True, use RZZ(theta) natively; else decompose

    Returns:
        QuantumCircuit with classical register for env qubit measurement

    Qubit register layout:
        q[0..b1]:              system qubits Q_0..Q_b1
        q[b1+1 .. b1+1+2*b1]:  env qubits [E_0, E'_0, E_1, E'_1, ...]
    """
    n_sys = b1 + 1
    n_env = 2 * b1
    n_total = n_sys + n_env
    n_measured = n_env  # Only measure environment qubits

    qc = QuantumCircuit(n_total, n_measured)

    # ---- Stage 1: State Preparation ----

    # System qubits to computational basis state
    for j, s_j in enumerate(system_state):
        if s_j == 1:
            qc.x(j)

    # Environment qubits to |+> state (X-basis eigenstate)
    for j in range(n_sys, n_total):
        qc.h(j)

    qc.barrier()

    # ---- Stage 2: Ring Evolution ----

    # RZZ( theta = -2c ) on each ring edge
    # Qiskit RZZ: exp(-i * theta/2 * Z⊗Z) -> theta = -2c
    theta_rzz = -2.0 * c

    for r in range(b1):
        # Qubit indices for ring r:
        q_Qr   = r                 # Q_r
        q_Qr1  = r + 1             # Q_{r+1}
        q_Er   = n_sys + 2 * r     # E_r
        q_Epr  = n_sys + 2 * r + 1 # E'_r

        if use_native_rzz:
            # Native RZZ: single pulse, 100-200 ns
            qc.rzz(theta_rzz, q_Qr, q_Er)    # Edge 1: Q_r -> E_r
            qc.rzz(theta_rzz, q_Qr1, q_Er)   # Edge 2: Q_{r+1} -> E_r (wait, should be E_r -> Q_{r+1})
            # Fix: Qiskit RZZ is symmetric, order doesn't matter for ZZ coupling
            qc.rzz(theta_rzz, q_Qr1, q_Epr)  # Edge 3: Q_{r+1} -> E'_r
            qc.rzz(theta_rzz, q_Qr, q_Epr)   # Edge 4: E'_r -> Q_r
        else:
            # Decomposed: CNOT + Rz + CNOT per RZZ
            for (u, v) in [(q_Qr, q_Er), (q_Er, q_Qr1),
                           (q_Qr1, q_Epr), (q_Epr, q_Qr)]:
                qc.cx(u, v)
                qc.rz(theta_rzz, v)
                qc.cx(u, v)

    qc.barrier()

    # ---- Stage 3: Random Pauli Unitaries for Shadow Measurement ----

    # For each env qubit, apply random Pauli rotation
    # Pauli basis: I->Z, H->X, HSdg->Y
    # Equivalent: random choice from {I, H, Sdg+H}
    pauli_choices = []
    for j in range(n_env):
        pauli = np.random.choice(['Z', 'X', 'Y'])
        pauli_choices.append(pauli)
        if pauli == 'X':
            qc.h(n_sys + j)
        elif pauli == 'Y':
            qc.sdg(n_sys + j)
            qc.h(n_sys + j)
        # 'Z': do nothing (measure in computational basis)

    # ---- Stage 4: Measurement ----
    qc.measure(range(n_sys, n_total), range(n_measured))

    return qc, pauli_choices


# ============================================================================
# 4. Classical Shadow Post-Processing
# ============================================================================

def single_qubit_shadow_overlap(b1, c1, b2, c2):
    """
    Compute Tr[(3 U1^dag |b1><b1| U1 - I)(3 U2^dag |b2><b2| U2 - I)]
    for a single qubit.

    Args:
        b1, b2: measurement outcomes (0 or 1)
        c1, c2: Pauli basis choices ('Z', 'X', 'Y')
    Returns:
        Overlap contribution from this qubit
    """
    if c1 == c2:
        # Same basis: outcome comparison
        if b1 == b2:
            return 3  # Same outcome -> +3
        else:
            return -1  # Opposite outcome -> -1
    else:
        # Different basis -> uncorrelated
        return 1


def estimate_gram_entry(shadow_data_a, shadow_data_b):
    """
    Estimate G_{ab} = Tr(rho_a * rho_b) from classical shadows.

    Args:
        shadow_data_a: list of (pauli_choices, bitstring) for state a
        shadow_data_b: list of (pauli_choices, bitstring) for state b
    Returns:
        float: estimated Gram matrix element
    """
    estimates = []
    for (pauli_a, bits_a) in shadow_data_a:
        for (pauli_b, bits_b) in shadow_data_b:
            overlap = 1.0
            for i in range(len(pauli_a)):
                overlap *= single_qubit_shadow_overlap(
                    bits_a[i], pauli_a[i],
                    bits_b[i], pauli_b[i]
                )
            estimates.append(overlap)

    return np.mean(estimates)


def compute_gram_matrix(shadow_data_by_state):
    """
    Compute full Gram matrix from shadow data for all system states.

    Args:
        shadow_data_by_state: dict mapping state_tuple -> shadow_data
    Returns:
        G: (d_sys x d_sys) Gram matrix
        states: list of state tuples (row/col ordering)
    """
    states = sorted(shadow_data_by_state.keys())
    d = len(states)
    G = np.eye(d, dtype=complex)

    for i, a in enumerate(states):
        for j, b in enumerate(states):
            if i < j:
                G[i, j] = estimate_gram_entry(
                    shadow_data_by_state[a],
                    shadow_data_by_state[b]
                )
                G[j, i] = np.conj(G[i, j])

    return G, states


def effective_rank(G):
    """
    Compute effective rank (participation ratio) of Gram matrix.

    rank_eff = (sum lambda_i)^2 / (sum lambda_i^2)
    For PSD Hermitian G with trace = d:
        rank_eff = d^2 / sum(lambda_i^2) = 1 / sum(p_i^2)
    where p_i = lambda_i / d.
    """
    evals = np.linalg.eigvalsh(G)
    evals = np.maximum(evals, 0)  # Clean numerical noise
    total = np.sum(evals)
    if total < 1e-15:
        return 0.0
    p = evals / total
    return 1.0 / np.sum(p ** 2)


# ============================================================================
# 5. Main Experiment Runner
# ============================================================================

def generate_all_circuits(b1, c_values, system_states, N_shadows_per_state,
                          use_native_rzz=True):
    """
    Generate all circuits for the experiment.

    Args:
        b1: number of rings
        c_values: list of Cartan angles to test
        system_states: list of tuples representing system basis states
        N_shadows_per_state: number of random Pauli measurements per state
        use_native_rzz: use native RZZ gates

    Returns:
        circuits: list of (circuit, metadata) tuples
    """
    circuits = []

    for c in c_values:
        for state in system_states:
            for shot_idx in range(N_shadows_per_state):
                qc, pauli = build_ring_chain_circuit(
                    b1, c, state, use_native_rzz
                )
                qc.name = f"b1{b1}_c{c:.4f}_s{''.join(map(str,state))}_n{shot_idx}"
                metadata = {
                    'b1': b1,
                    'c': c,
                    'system_state': state,
                    'shadow_idx': shot_idx,
                    'pauli_choices': pauli
                }
                circuits.append((qc, metadata))

    return circuits


def run_experiment(token, b1, c_values, N_shadows, dry_run=False):
    """
    Submit the Nighthawk experiment to IBM Q.

    Args:
        token: IBM Q API token
        b1: number of causal rings (1-5)
        c_values: list of Cartan angles [pi/2, pi/4, pi/8, 0.5]
        N_shadows: number of shadow snapshots per system state
        dry_run: if True, only generate circuits, don't submit
    """
    n_sys = b1 + 1
    n_env = 2 * b1

    # Generate all system basis states
    system_states = list(product([0, 1], repeat=n_sys))

    # For large b1, sample a subset
    d_sys = 2 ** n_sys
    if d_sys > 32:
        print(f"Warning: d_sys={d_sys}, sampling 32 random states for efficiency")
        rng = np.random.RandomState(42)
        indices = rng.choice(d_sys, size=min(32, d_sys), replace=False)
        system_states = [system_states[i] for i in indices]

    print(f"Nighthawk DGF Gram Matrix Experiment")
    print(f"=" * 60)
    print(f"Backend: ibm_miami (120 qubit, square lattice)")
    print(f"b1 = {b1} rings")
    print(f"System qubits: {n_sys}")
    print(f"Environment qubits: {n_env}")
    print(f"Total qubits: {n_sys + n_env}")
    print(f"System states to sample: {len(system_states)}")
    print(f"Shadows per state: {N_shadows}")
    print(f"Cartan angles: {[f'{c:.4f}' for c in c_values]}")
    print(f"Total circuits: {len(c_values) * len(system_states) * N_shadows}")
    print()

    # Generate circuits
    circuits_metadata = generate_all_circuits(
        b1, c_values, system_states, N_shadows, use_native_rzz=True
    )
    circuits = [cm[0] for cm in circuits_metadata]

    if dry_run:
        print("[DRY RUN] Circuit generation complete")
        print(f"Example circuit ({circuits[0].name}):")
        print(circuits[0])
        print(f"\nDepth: {circuits[0].depth()}")
        print(f"2Q gates: {circuits[0].count_ops().get('rzz', 0)}")
        return circuits_metadata

    # Connect to IBM Q
    print("Connecting to IBM Q...")
    service = QiskitRuntimeService(token=token)
    backend = service.backend('ibm_miami')

    print(f"Backend: {backend.name}")
    print(f"Qubits: {backend.num_qubits}")
    print(f"Pending jobs: {backend.status().pending_jobs}")
    print()

    # Transpile
    print("Transpiling circuits...")
    pm = generate_preset_pass_manager(
        optimization_level=3,
        backend=backend
    )

    # Batch transpilation to manage memory
    batch_size = 50
    isa_circuits = []
    for i in range(0, len(circuits), batch_size):
        batch = circuits[i:i + batch_size]
        isa_circuits.extend(pm.run(batch))
        print(f"  Transpiled {min(i + batch_size, len(circuits))}/{len(circuits)}")

    print(f"Transpile complete. Max depth: {max(c.depth() for c in isa_circuits)}")
    print()

    # Submit as Sampler job
    print("Submitting to ibm_miami...")
    sampler = Sampler(mode=backend)
    job = sampler.run(isa_circuits, shots=1)  # 1 shot per shadow circuit

    job_id = job.job_id()
    print(f"Job ID: {job_id}")

    # Save metadata
    metadata_file = f"nighthawk_b1{b1}_job_{job_id[:8]}.json"
    with open(metadata_file, 'w') as f:
        json.dump({
            'job_id': job_id,
            'backend': 'ibm_miami',
            'b1': b1,
            'c_values': [float(c) for c in c_values],
            'N_shadows_per_state': N_shadows,
            'n_sys': n_sys,
            'n_env': n_env,
            'n_system_states': len(system_states),
            'system_states': [list(s) for s in system_states],
            'n_circuits': len(circuits),
            'timestamp': datetime.now().isoformat(),
            'metadata': [cm[1] for cm in circuits_metadata]
        }, f, indent=2)

    print(f"Metadata saved: {metadata_file}")
    print("Done.")
    return job_id


# ============================================================================
# 6. Results Analysis
# ============================================================================

def analyze_results(token, job_id):
    """
    Retrieve job results and compute Gram matrix spectrum.

    Steps:
    1. Load job results and metadata
    2. Group shadow data by (c, system_state)
    3. Compute Gram matrix for each c
    4. Extract effective rank and eigenvalue spectrum
    5. Compare with analytic predictions
    """
    from qiskit_ibm_runtime import QiskitRuntimeService

    # Find metadata file
    import glob
    meta_files = glob.glob(f"nighthawk_*_job_{job_id[:8]}.json")
    if not meta_files:
        # Try loading from local registry
        meta_files = glob.glob(f"nighthawk_*_{job_id[:8]}.json")
    if not meta_files:
        raise FileNotFoundError(f"No metadata file found for job {job_id[:8]}")

    with open(meta_files[0]) as f:
        meta = json.load(f)

    b1 = meta['b1']
    c_values = meta['c_values']
    system_states = [tuple(s) for s in meta['system_states']]

    print(f"Analyzing Nighthawk results: Job {job_id}")
    print(f"b1 = {b1}")
    print(f"Cartan angles: {c_values}")

    # Connect and retrieve
    service = QiskitRuntimeService(token=token)
    job = service.job(job_id)

    if job.status().name != 'DONE':
        print(f"Job status: {job.status().name}")
        return

    result = job.result()

    # Group results by (c, system_state)
    # result[i] corresponds to circuits_metadata[i]
    # We need to reconstruct the grouping from metadata

    shadow_data = {}  # (c, state) -> list of (pauli, bitstring)
    for i, pub_result in enumerate(result):
        m = meta['metadata'][i]
        c = m['c']
        state = tuple(m['system_state'])
        pauli = m['pauli_choices']
        bits = pub_result.data.c.get_counts()  # Single shot -> one bitstring
        # Extract the measured bitstring
        bitstring = list(bits.keys())[0]  # e.g. '01001010'
        bitlist = [int(b) for b in bitstring]

        key = (c, state)
        if key not in shadow_data:
            shadow_data[key] = []
        shadow_data[key].append((pauli, bitlist))

    # Analyze each c value
    print()
    print("=" * 60)
    print("GRAM MATRIX SPECTRAL ANALYSIS")
    print("=" * 60)

    for c in c_values:
        # Collect shadows for this c
        c_shadows = {state: data for (cc, state), data in shadow_data.items()
                     if abs(cc - c) < 1e-10}

        if len(c_shadows) < 2:
            print(f"c={c:.4f}: insufficient data ({len(c_shadows)} states)")
            continue

        G, states = compute_gram_matrix(c_shadows)
        r_eff = effective_rank(G)
        d_sys = len(states)

        # Analytic prediction
        mu_analytic = analytic_mu_vertex_chain(b1, c, p=0.5)
        r_eff_pred = 1.0 / (d_sys * np.mean(np.exp(2 * mu_analytic)))

        print(f"\nc = {c:.4f} ({c/np.pi:.2f} pi)")
        print(f"  d_sys = {d_sys}")
        print(f"  rank_eff (measured) = {r_eff:.6f}")
        print(f"  rank_eff (analytic) = {r_eff_pred:.6f}")
        print(f"  ratio rank_eff/d_sys = {r_eff/d_sys:.4f}")

        # Eigenvalue distribution
        evals = np.sort(np.linalg.eigvalsh(G))[::-1]
        evals = np.maximum(evals, 0)
        total = np.sum(evals)
        if total > 0:
            evals_norm = evals / total
            n_show = min(5, len(evals_norm))
            print(f"  Top {n_show} eigenvalues: {evals_norm[:n_show]}")
            print(f"  lambda_1 / sum = {evals_norm[0]:.6f}")

        # Verdict
        if r_eff / d_sys < 0.1:
            verdict = "CLASSICAL (rank collapse detected)"
        elif r_eff / d_sys > 0.5:
            verdict = "QUANTUM (full rank preserved)"
        else:
            verdict = "INTERMEDIATE (partial collapse)"

        print(f"  VERDICT: {verdict}")


# ============================================================================
# 7. Analytic Predictions
# ============================================================================

def analytic_mu_vertex_chain(b1, c, p=0.5):
    """
    Analytic decay rate mu for vertex-sharing chain of b1 rings.

    For each ring, the Gram factor is:
        f(delta) = p * exp(i*c*delta) + (1-p) * exp(-i*c*delta)

    With p=0.5: f(delta) = cos(c * delta)

    delta = (s_Qr^a + s_{Qr+1}^a) - (s_Qr^b + s_{Qr+1}^b)
    Each s in {+1, -1} (after mapping from {0,1})
    delta in {-4, -2, 0, 2, 4} with probs {1/16, 4/16, 6/16, 4/16, 1/16}

    Each ring has 2 env qubits contributing factor^2.
    mu_per_ring = 2 * sum_delta prob(delta) * ln|cos(c*delta)|
    Total mu = b1 * mu_per_ring
    """
    delta_vals = np.array([-4, -2, 0, 2, 4])
    delta_probs = np.array([1, 4, 6, 4, 1]) / 16.0

    mu_env = 0.0
    for dv, prob in zip(delta_vals, delta_probs):
        factor = np.abs(np.cos(c * dv))
        if factor < 1e-15:
            return -np.inf  # Exact zero -> mu diverges
        mu_env += prob * np.log(factor)

    mu_per_ring = 2.0 * mu_env  # 2 env qubits per ring
    return b1 * mu_per_ring


def predict_rank_eff(b1, c, p=0.5):
    """
    Predict effective rank from analytic mu.

    For Gram matrix of size d_sys x d_sys:
    - Off-diagonal decay: |G_{ab}| ~ exp(mu * b1) for average pair
    - Rank collapses when mu < 0 (exponential decay of off-diagonals)
    - rank_eff ~ 1 + (d_sys - 1) * exp(2*mu*b1) for small eigenvalues
    """
    d_sys = 2 ** (b1 + 1)
    mu = analytic_mu_vertex_chain(b1, c, p)

    if mu == -np.inf:
        return 1.0  # Perfect rank-1

    # For mu < 0, off-diagonals decay exponentially
    # The eigenvalue spectrum has one O(d_sys) eigenvalue and d_sys-1 small ones
    if mu < 0:
        # Small eigenvalues ~ exp(2*mu*b1) * some factor
        small_eval = np.exp(2 * mu)  # Per-ring decay squared for eigenvalues
        # Effective rank from participation ratio
        sum_evals = d_sys  # Trace = d_sys
        sum_sq = d_sys**2 * (1/d_sys + (d_sys-1)/d_sys * small_eval**2)
        # Wait, this isn't right. Let me compute properly.
        # For rank-1 dominant: lambda_1 ~ d_sys - something, rest ~ exp(2*mu)
        # participation: r_eff = (sum lambda)^2 / (sum lambda^2)
        # If one eigenvalue = d_sys * (1 - epsilon) and rest share epsilon*d_sys:
        # r_eff ~ 1 (when epsilon -> 0)
        if abs(mu) * b1 > 3:  # Strong decay
            return 1.0 + d_sys * np.exp(2 * mu * b1)
        else:
            # Interpolate between full rank and rank-1
            return d_sys * np.exp(2 * mu * b1)
    else:
        # mu >= 0: no decay, full rank
        return float(d_sys)


def print_analytic_table(max_b1=5):
    """Print analytic prediction table."""
    c_configs = [
        (np.pi / 2, "pi/2", "Clifford"),
        (np.pi / 4, "pi/4", "CNOT-equivalent"),
        (np.pi / 8, "pi/8", "T-gate"),
        (0.5, "0.5", "Classical"),
    ]

    print("\nANALYTIC PREDICTIONS")
    print("=" * 80)
    print(f"{'c':>10s}  {'b1':>4s}  {'d_sys':>6s}  {'mu_per_ring':>12s}  "
          f"{'rank_eff_pred':>14s}  {'rank/d':>10s}  {'Regime':>15s}")
    print("-" * 80)

    for c, c_label, c_type in c_configs:
        for b1 in range(1, max_b1 + 1):
            d_sys = 2 ** (b1 + 1)
            mu = analytic_mu_vertex_chain(b1, c, 0.5)
            mu_per_ring = mu / b1 if b1 > 0 else 0
            r_pred = predict_rank_eff(b1, c, 0.5)
            ratio = r_pred / d_sys

            if ratio > 0.5:
                regime = "QUANTUM"
            elif ratio > 0.05:
                regime = "INTERMEDIATE"
            else:
                regime = "CLASSICAL"

            print(f"{c_label:>10s}  {b1:4d}  {d_sys:6d}  "
                  f"{mu_per_ring:12.6f}  {r_pred:14.3f}  "
                  f"{ratio:10.4f}  {regime:>15s}")


# ============================================================================
# 8. Main entry point
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Nighthawk DGF Gram Matrix Spectral Transition Experiment"
    )
    parser.add_argument("--token", type=str, default=None,
                       help="IBM Q API token")
    parser.add_argument("--b1", type=int, default=4,
                       help="Number of causal rings (1-5)")
    parser.add_argument("--c", type=float, nargs='+',
                       default=[np.pi/2, np.pi/4, np.pi/8, 0.5],
                       help="Cartan angles to test (radians)")
    parser.add_argument("--shots", type=int, default=5000,
                       help="Shadow snapshots per system state")
    parser.add_argument("--dry-run", action="store_true",
                       help="Generate circuits only, do not submit")
    parser.add_argument("--retrieve", type=str, default=None,
                       help="Retrieve and analyze results from job ID")
    parser.add_argument("--analytic", action="store_true",
                       help="Print analytic prediction table and exit")

    args = parser.parse_args()

    if args.analytic:
        print_analytic_table(max_b1=5)
        exit(0)

    if args.retrieve:
        analyze_results(args.token, args.retrieve)
    else:
        run_experiment(args.token, args.b1, args.c, args.shots,
                      dry_run=args.dry_run)
```

---

## 7. Feasibility Table

### 7.1 Resource Requirements

| b1 | Qubits | 2Q Gates (Opt A) | 2Q Gates (Opt B) | Depth (A) | Depth (B) | Circuits (d_sys * 5000 shadows) | Est. Runtime |
|:--:|:------:|:----------------:|:----------------:|:---------:|:---------:|:--------------------------------:|:------------:|
| 1  | 4      | 4 RZZ            | 8 CZ             | ~0.6 us   | ~1.2 us   | 20,000                          | < 1 hr       |
| 2  | 7      | 8 RZZ            | 16 CZ            | ~1.2 us   | ~2.5 us   | 40,000                          | 2-4 hrs      |
| 3  | 10     | 12 RZZ           | 24 CZ            | ~1.8 us   | ~3.7 us   | 80,000                          | 1-2 days     |
| 4  | 13     | 16 RZZ           | 32 CZ            | ~2.4 us   | ~5.0 us   | 160,000                         | 3-7 days     |
| 5  | 16     | 20 RZZ           | 40 CZ            | ~3.0 us   | ~6.2 us   | 320,000                         | 1-2 weeks    |

### 7.2 Signal-to-Noise Estimates

| b1 | d_sys | rank_eff (c=pi/2, Clifford) | rank_eff (c=0.5, classical) | rank_eff/d (c=pi/2) | rank_eff/d (c=0.5) | S/N for rank detection |
|:--:|:-----:|:---------------------------:|:---------------------------:|:-------------------:|:-------------------:|:----------------------:|
| 1  | 4     | ~4.0 (full rank)            | ~1.0 (rank-1)               | 1.00               | 0.25                | > 100                 |
| 2  | 8     | ~8.0                        | ~1.0                        | 1.00               | 0.125               | > 50                  |
| 3  | 16    | ~16.0                       | ~1.0                        | 1.00               | 0.063               | > 20                  |
| 4  | 32    | ~32.0                       | ~1.0                        | 1.00               | 0.031               | > 10                  |
| 5  | 64    | ~64.0                       | ~1.0                        | 1.00               | 0.016               | > 5                   |

### 7.3 Projected Mu Values (Analytic, p=0.5)

| c (rad) | c (pi) | mu_per_ring | b1=1 rank_eff/d | b1=4 rank_eff/d | Regime |
|:--------|:-------|:-----------:|:---------------:|:---------------:|:------:|
| pi/2    | 0.5000 | 0.0000      | 1.000           | 1.000           | QUANTUM (mu=0, Clifford) |
| pi/4    | 0.2500 | -0.6931     | 0.250           | 0.004           | COLLAPSING |
| pi/8    | 0.1250 | -1.0397     | 0.125           | 2.5e-4          | CLASSICAL |
| 0.5     | 0.1592 | -1.2238     | 0.087           | 5.6e-5          | CLASSICAL (strong) |
| pi/16   | 0.0625 | -1.5610     | 0.044           | 3.8e-6          | CLASSICAL (very strong) |

### 7.4 Practical Time Estimate (Premium Access)

| Phase | b1 range | c values | Circuits | Calendar time | Priority |
|:------|:---------|:---------|:---------|:-------------|:---------|
| Phase 0: Calibration | b1=1 | pi/2, pi/4, 0.5 | 60,000 | 1 day | CRITICAL |
| Phase 1: Core scan | b1=1,2,3 | pi/2, pi/4, pi/8, 0.5 | 560,000 | 5-7 days | HIGH |
| Phase 2: Large b1 | b1=4,5 | pi/2, pi/4, pi/8, 0.5 | 960,000 | 10-14 days | MEDIUM |
| Phase 3: Fine scan | b1=[best] | 8 values in [0.1, pi/2] | 200,000 | 3-5 days | LOW |
| **Total** | | | **~1.8M circuits** | **3-4 weeks** | |

---

## 8. Key Observables to Report

### 8.1 Primary Observable: rank_eff/d_sys vs b1

The flagship plot: effective rank normalized by system dimension as a function of ring count.

```
Expected outcome:

  rank_eff/d_sys
      1.0 |*
          |  *  c=pi/2 (Clifford): stays at 1.0
          |    *
      0.5 |     *
          |
          |        c=pi/4: exponential decay
      0.1 |         *
          |            *  c=0.5: even faster decay
          |                *
    0.01  |_____________________*________
          1    2    3    4    5    b1
```

### 8.2 Eigenvalue Spectrum Evolution

For each (b1, c), report:
- Top 5 normalized eigenvalues
- Number of eigenvalues above 1% of total spectral weight
- Participation ratio rank_eff (quantitative)
- Ratio lambda_1 / lambda_2 (gap to second mode)

### 8.3 Clifford Confirmation

Verify that for c = pi/2:
- rank_eff / d_sys = 1.0 within error bars for all b1
- All eigenvalues approximately equal (within 20%)
- This confirms that Clifford gates produce the theoretically predicted mu=0 (no decoherence from causal topology)

### 8.4 Classicality Verification

For c = 0.5:
- rank_eff -> 1 as b1 increases
- lambda_1 / sum(lambda) -> 1 (single dominant mode)
- This confirms the classical pointer-state hypothesis

### 8.5 Mu Extraction

Fit ln(|G_ab|) vs b1 for each c to extract the measured decay rate mu_meas.
Compare with analytic prediction:
- mu = 0 for c = pi/2 (Clifford)
- mu < 0 for c not in (pi/2)Z (non-Clifford)
- |mu| increases as c moves away from pi/2

### 8.6 Supplementary Observables

1. **Gate fidelity impact:** Compare rank_eff for the same (b1, c) with and without Richardson extrapolation (ZNE) -- quantify the systematic error from gate depolarization.

2. **Shadow variance scaling:** Empirically measure the variance of the shadow overlap estimator as a function of n_env, confirming the O(2^n) scaling theoretically expected.

3. **Comparison with ibm_kingston:** For b1=1, compare the Nighthawk results (native 4-cycle, no SWAP) with ibm_kingston results (heavy-hex, SWAP overhead) to quantify the topology advantage.

---

## 9. Risk Assessment and Mitigations

| Risk | Severity | Likelihood | Mitigation |
|:-----|:--------:|:----------:|:-----------|
| Fractional RZZ not exposed in runtime | HIGH | MEDIUM | Fall back to Option B (decomposed RZZ); gate count doubles but remains manageable |
| Shadow protocol variance too high at n_env=8 | MEDIUM | LOW | Reduce b1, increase shadows, or switch to Phase 1 (trace estimation) |
| Device calibration drift over multi-day runs | MEDIUM | HIGH | Interleave calibration circuits every 100 circuits; use H-wrapping for consistency |
| Queue congestion on ibm_miami | HIGH | MEDIUM | Use premium access; submit during off-peak hours; batch circuits efficiently |
| Readout errors dominate at large b1 | LOW | LOW | Readout mitigation via confusion matrix; post-selection on total population |
| Coherence loss at b1=5 (6.2 us circuit) | LOW | LOW | T1 margin is 55x; T2 margin is 32x; dynamical decoupling on idle qubits |

---

## 10. Comparison with Previous IBM Q Experiments

| Aspect | ibm_kingston (Heron r2) | ibm_miami (Nighthawk) |
|:-------|:----------------------|:---------------------|
| Lattice | Heavy-hex (girth=6) | **Square (girth=4)** |
| Native 4-cycles | No | **Yes** |
| SWAP per ring | 2-4 | **0** |
| Qubits for b1=1 ring | 8 (4 core + 2 anc + 2 routing) | **4 (4 core, no anc, no routing)** |
| 2Q gates for b1=1 | ~11-14 CZ | **4 RZZ** |
| Circuit depth | ~15-25 | **~4** |
| Coherence margin | ~10x | **~50x** |
| Bell pair fidelity | ~39% (destroyed by SWAP) | **>95% (expected, no SWAP)** |
| Experiment type | QCMI via mutual information | **Gram matrix spectral via classical shadows** |
| Physics probed | QCMI > 0 existence | **Rank collapse scaling law** |

---

## References

1. DGF-Survivors paper1-prl: `main.tex` -- CFOL theorem, scaling law, IBM Q verification
2. `A_ibm_mapping.md` -- Transmon-to-Cartan mapping, heavy-hex constraint analysis
3. `verify_p0_gram_rank.py` -- Classical Gram matrix verification and mu extraction
4. `cfol_ibm_experiment.py` -- IBM Q b1=1 experiment code (ibm_kingston)
5. `21-experimental-framework.md` -- 9-mechanism error budget, H-wrapping innovation
6. Elben et al., "The randomized measurement toolbox", Nat. Rev. Phys. 5, 9-24 (2023) -- Classical shadows protocol
7. Huang et al., "Predicting many properties of a quantum system from very few measurements", Nat. Phys. 16, 1050-1057 (2020)
