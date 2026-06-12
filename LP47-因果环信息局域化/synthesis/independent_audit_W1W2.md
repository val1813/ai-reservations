# Independent Numerical Audit Report: LP47 QCMI for n=5 Cluster Ring

**Auditor**: Independent agent (zero trust in Dr. A or Dr. B frameworks)
**Method**: Exact diagonalization, from-scratch Python/numpy/scipy
**Date**: 2026-06-12
**Status**: COMPLETE -- All Dr. A claims FALSIFIED

---

## 1. System Definition and Construction

### 1.1 Cluster Ring State |C5>

Constructed per primary definition: start with |+>^⊗5, apply CZ gates along the ring (0,1), (1,2), (2,3), (3,4), (4,0).

**Verification**: Single-qubit reduced states all maximally mixed (eigenvalues [1/2, 1/2]), two-qubit reduced states all maximally mixed (eigenvalues [1/4, 1/4, 1/4, 1/4]). All entropies consistent with known graph state formulas.

**Note**: The "equivalent construction" listed in the task (H after CZ on |0>^⊗5) is WRONG -- it produces a different state (fidelity 0 with the correct construction). The correct definition is CZ after H on |0>^⊗5, i.e., CZ on |+>^⊗5.

### 1.2 H-mix Perturbation

|psi(theta)> = cos(pi*theta/2) |C5> + sin(pi*theta/2) H0|C5>

where H0 is the Hadamard gate on qubit 0.

**Key property**: <C5|H0|C5> = 0. The two superposed states are orthogonal. No normalization correction needed beyond cos^2 + sin^2 = 1.

---

## 2. Complete Raw Data Tables

### 2.1 Partition k=1 (adjacent): A={0}, C={1}, B={2,3,4}

QCMI identity: I(A:C|B) = I(0:1) (reduces to ordinary mutual information)

| theta | S(rho_A)=S(rho_0) | S(rho_C)=S(rho_1) | S(rho_AC)=S(rho_{0,1}) | S(rho_AB) | S(rho_BC) | S(rho_B) | S(rho_ABC) | QCMI (nats) | QCMI (bits) |
|-------|--------------------|--------------------|------------------------|------------|------------|-----------|-------------|-------------|-------------|
| 0.00 | 0.6931471805599454 | 0.6931471805599454 | 1.3862943611198904 | 0.6931471805599455 | 0.6931471805599455 | 1.3862943611198904 | 0 | 7e-16 | 1e-15 |
| 0.05 | 0.6808609091078945 | 0.6931471805599456 | 1.3740080896678393 | 0.6931471805599455 | 0.6808609091078945 | 1.3740080896678393 | 0 | 9e-16 | 1e-15 |
| 0.10 | 0.6446109393085303 | 0.6931471805599454 | 1.3377581198684754 | 0.6931471805599455 | 0.6446109393085304 | 1.3377581198684754 | 0 | 7e-16 | 1e-15 |
| 0.15 | 0.5862245822102233 | 0.6931471805599455 | 1.2793717627701682 | 0.6931471805599454 | 0.5862245822102232 | 1.2793717627701682 | 0 | 4e-16 | 6e-16 |
| 0.20 | 0.5087533543287812 | 0.6931471805599454 | 1.2019005348887262 | 0.6931471805599455 | 0.5087533543287812 | 1.2019005348887259 | 0 | 9e-16 | 1e-15 |

### 2.2 Partition k=2 (antipodal): A={0}, C={2}, B={1,3,4}

QCMI identity: I(A:C|B) = I(0:2) (reduces to ordinary mutual information)

| theta | S(rho_A)=S(rho_0) | S(rho_C)=S(rho_2) | S(rho_AC)=S(rho_{0,2}) | S(rho_AB) | S(rho_BC) | S(rho_B) | S(rho_ABC) | QCMI (nats) | QCMI (bits) |
|-------|--------------------|--------------------|------------------------|------------|------------|-----------|-------------|-------------|-------------|
| 0.00 | 0.6931471805599454 | 0.6931471805599454 | 1.3862943611198904 | 0.6931471805599456 | 0.6931471805599455 | 1.3862943611198904 | 0 | 9e-16 | 1e-15 |
| 0.05 | 0.6808609091078945 | 0.6931471805599456 | 1.3740080896678393 | 0.6931471805599456 | 0.6808609091078945 | 1.3740080896678393 | 0 | 9e-16 | 1e-15 |
| 0.10 | 0.6446109393085303 | 0.6931471805599455 | 1.3377581198684754 | 0.6931471805599455 | 0.6446109393085304 | 1.3377581198684754 | 0 | 7e-16 | 1e-15 |
| 0.15 | 0.5862245822102233 | 0.6931471805599455 | 1.2793717627701682 | 0.6931471805599456 | 0.5862245822102232 | 1.2793717627701682 | 0 | 7e-16 | 1e-15 |
| 0.20 | 0.5087533543287812 | 0.6931471805599454 | 1.2019005348887264 | 0.6931471805599455 | 0.5087533543287812 | 1.2019005348887259 | 0 | 9e-16 | 1e-15 |

**All QCMI values are zero to within numerical precision (~10^-15 to 10^-16).**

---

## 3. Delta QCMI Analysis

### 3.1 Partition k=1 (adjacent)

| theta | Delta QCMI (nats) | Delta QCMI (bits) |
|-------|--------------------|--------------------|
| 0.00 | 0.0000000000000000 | 0.0000000000000000 |
| 0.05 | +0.0000000000000002 | +0.0000000000000003 |
| 0.10 | 0.0000000000000000 | 0.0000000000000000 |
| 0.15 | -0.0000000000000002 | -0.0000000000000003 |
| 0.20 | +0.0000000000000002 | +0.0000000000000003 |

**Delta QCMI(theta=0.10, k=1) = 0.0000000000000000 nats = 0.0000000000000000 bits**

### 3.2 Partition k=2 (antipodal)

| theta | Delta QCMI (nats) | Delta QCMI (bits) |
|-------|--------------------|--------------------|
| 0.00 | 0.0000000000000000 | 0.0000000000000000 |
| 0.05 | 0.0000000000000000 | 0.0000000000000000 |
| 0.10 | -0.0000000000000002 | -0.0000000000000003 |
| 0.15 | -0.0000000000000002 | -0.0000000000000003 |
| 0.20 | 0.0000000000000000 | 0.0000000000000000 |

**Delta QCMI(theta=0.10, k=2) = -0.0000000000000002 nats = -0.0000000000000003 bits** (numerical noise)

### 3.3 Least-Squares Fit

Delta QCMI is **identically zero** (max |Delta QCMI| < 2.3e-16 nats across all data points). The fitting procedure is degenerate:

- **alpha = 0** (exact) for both partitions
- **beta = 0** (exact) for both partitions
- **R^2 = 1.0** (trivially, since all points are zero)

No meaningful fit of the form Delta QCMI = alpha * theta^2 * ln(1/theta) + beta * theta^2 is possible because the response variable is identically zero.

---

## 4. Verification of Dr. A's Claims

### Claim 1: alpha ~ 0.244 for k=1

| | Value |
|---|---|
| Dr. A claimed alpha(k=1) | 0.244 |
| Computed alpha(k=1) | **0.0 (exact)** |
| Absolute difference | 0.244 |

**VERDICT: FALSIFIED.** The true alpha is exactly zero. Dr. A claims a leading-order theta^2*ln(1/theta) contribution of ~0.244, but the QCMI is identically zero -- there is no theta dependence at all.

### Claim 2: alpha ~ -0.1582 for k=2

| | Value |
|---|---|
| Dr. A claimed alpha(k=2) | -0.1582 |
| Computed alpha(k=2) | **0.0 (exact)** |
| Absolute difference | 0.1582 |

**VERDICT: FALSIFIED.** Same as above -- alpha is exactly zero.

### Claim 3: Delta QCMI(theta=0.10, k=1) = 0.02407 bits

| | Value |
|---|---|
| Dr. A claimed | 0.02407 bits |
| Computed | **0.0000000000000000 bits** |
| Absolute difference | 0.02407 bits |

**VERDICT: FALSIFIED.** The claimed value of 0.02407 bits is off by 14 orders of magnitude from the true value of 0. This is not a rounding or precision issue -- the QCMI is identically zero.

### Claim 4: R^2 > 0.98

| | k=1 | k=2 |
|---|---|---|
| R^2 | 1.0 (degenerate) | 1.0 (degenerate) |

**VERDICT: MEANINGLESS.** The R^2 value of 1.0 is a degenerate result -- it reflects the fact that all Delta QCMI values are identically zero, not that a meaningful fit exists. This claim is a category error: Dr. A is reporting fit quality for a nonexistent signal.

---

## 5. W1 Verdict: Sign of Delta QCMI(theta=0.10, k=2)

**Delta QCMI(theta=0.10, k=2) = -2.2e-16 nats = -3.2e-16 bits**

**W1 JUDGMENT: ZERO.** The value is at the level of numerical floating-point noise (machine epsilon for double precision is ~2.2e-16). The true analytical value is exactly zero. The sign is neither positive nor negative -- it is identically zero.

---

## 6. Analytical Proof: Why QCMI = 0

The numerical finding of identically zero QCMI is not a coincidence or precision issue. It follows from an exact analytical identity:

### Step 1: QCMI reduces to mutual information

For the given partitions with pure global state and A U B U C covering all qubits:

- **k=1**: QCMI = I(0:1) -- the ordinary mutual information between qubits 0 and 1
- **k=2**: QCMI = I(0:2) -- the ordinary mutual information between qubits 0 and 2

Proof: S(rho_ABC) = 0 (pure state). S(rho_AB) = S(rho_C_complement) = S(rho_C) by purity, and similarly S(rho_BC) = S(rho_A). Also S(rho_B) = S(rho_AC) by purity. So QCMI = S(rho_A) + S(rho_C) - S(rho_AC) = I(A:C).

### Step 2: Cross-term structure of the perturbed state

For |psi> = cos(phi)|C5> + sin(phi) H0|C5> with phi = pi*theta/2 and <C5|H0|C5> = 0:

**Single-qubit reduced state of qubit 0:**
```
rho_0 = I/2 + c*H
```
where c = cos(phi)*sin(phi) and H is the 2x2 Hadamard matrix.

**Single-qubit reduced state of qubit j (j != 0):**
```
rho_j = I/2   (constant, no change from cluster state)
```
The cross term Tr_{all except j}(|C5><C5| H0) vanishes for j != 0 because Tr(H) = 0.

**Two-qubit reduced state of {0, j} (j != 0):**
```
rho_{0,j} = I/4 + c*(H ⊗ I)/2
```
Eigenvalues: {1/4 + c/2, 1/4 + c/2, 1/4 - c/2, 1/4 - c/2}

### Step 3: Entropy relationship

Define x = 1/2 + c (so 0 < x < 1 for |c| < 1/2). Then:

```
S(rho_0)     = -x*ln(x) - (1-x)*ln(1-x)
S(rho_j)     = ln(2)
S(rho_{0,j}) = -x*ln(x) - (1-x)*ln(1-x) + ln(2)
```

### Step 4: Mutual information vanishes identically

```
I(0:j) = S(rho_0) + S(rho_j) - S(rho_{0,j})
       = [-x*ln(x) - (1-x)*ln(1-x)] + ln(2)
         - [-x*ln(x) - (1-x)*ln(1-x) + ln(2)]
       = 0   (IDENTICALLY, for all x)
```

The terms cancel exactly. This holds for **any** value of c = cos(phi)*sin(phi) = sin(pi*theta)/2, hence for **any** theta.

### Step 5: Physical interpretation

The H-mix perturbation acts only on qubit 0. While it changes S(rho_0) (reducing it from ln(2) as theta increases), it does so in a way that is perfectly mirrored by the corresponding reduction in S(rho_{0,j}). The "extra" entropy in the joint state rho_{0,j} is exactly the amount by which S(rho_0) decreases, leaving the mutual information zero.

This is a manifestation of the fact that **a local unitary on a single qubit, applied in superposition, cannot create mutual information between that qubit and any other qubit** when the initial state has zero mutual information and all reduced states are maximally mixed.

---

## 7. Conclusions

1. **QCMI is identically zero** for both partitions (k=1 adjacent, k=2 antipodal) at all theta values (0, 0.05, 0.10, 0.15, 0.20).

2. **All four of Dr. A's claims are FALSIFIED:**
   - Claimed alpha ~ 0.244 (k=1): True alpha = 0
   - Claimed alpha ~ -0.1582 (k=2): True alpha = 0
   - Claimed Delta QCMI(0.10, k=1) = 0.02407 bits: True value = 0
   - Claimed R^2 > 0.98: Degenerate/misleading

3. **W1 Judgement**: Delta QCMI(0.10, k=2) is ZERO, not positive or negative.

4. **The analytical proof** (Section 6) demonstrates that the zero result is exact and robust -- it is not a numerical artifact but a mathematical identity arising from the cluster state's maximal entropy structure and the locality of the H-mix perturbation.

5. **Possible explanations for Dr. A's erroneous claims:**
   - Dr. A may have used a different perturbation scheme (not pure H-mix as specified)
   - Dr. A may have made an error in computing partial traces or entropy
   - Dr. A's fitting procedure may have been applied to noise or a different quantity
   - The "equivalent construction" for the cluster state given in the task is incorrect; Dr. A may have used this wrong construction

---

## Appendix: Computation Script

The full computation script is at:
`D:\Claude\ai-reservations\LP47-因果环信息局域化\synthesis\audit_qcmi_v2.py`

Key specifications:
- Language: Python 3
- Libraries: numpy, scipy (scipy.linalg.eigvalsh for Hermitian eigenvalue decomposition)
- Method: Exact diagonalization of 32-dimensional Hilbert space (2^5)
- Gate construction: Explicit Kronecker-product embedding of 1-qubit and 2-qubit gates
- Partial trace: Direct computation summing over traced-out indices
- Entropy: von Neumann entropy S = -Tr(rho ln rho) using eigenvalue decomposition, natural log (nats)
- Numerical precision: Double-precision floating point (IEEE 754 float64, ~15-16 decimal digits)

All code is self-contained with no external dependencies beyond numpy/scipy. The script can be independently verified by running:
```
python audit_qcmi_v2.py
```
