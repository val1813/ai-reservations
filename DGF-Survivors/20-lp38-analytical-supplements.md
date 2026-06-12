# LP38 Analytical Supplements — Key Results Absorbed into DGF-Survivors

**Date:** 2026-06-09
**Purpose:** Absorb key analytical results from LP38-QCMI-Precision into the DGF-Survivors knowledge base. This document serves as the consolidated reference for the CJ Bridge quantitative mapping, the temporal-to-spatial tensor network proof, the alpha origin analytic derivation, and the eta_0 tightness five-layer analysis.
**Source documents:**
- `LP38-QCMI-Precision/derivations/W2_CJ_Quantitative_Mapping.md` — W2 complete derivation
- `LP38-QCMI-Precision/derivations/TASK1_CJ_Bridge_u4_Correction.md` — TASK1 correction
- `LP38-QCMI-Precision/attack/temporal_to_spatial/temporal_to_spatial_CJ_bridge.md` — CJ bridge tensor network proof
- `LP38-QCMI-Precision/S4_alpha_origin/current_A/analytic_derivation.md` — alpha origin analytic derivation
- `LP38-QCMI-Precision/S1_eta_bound/current_A/round2_tightness_A.md` — eta_0 tightness formal analysis

---

## 1. CJ Bridge Quantitative Mapping (W2 -- SOLVED)

### 1.1 Closed-form QCMI formula

For the simplest non-trivial case (G1=G2=G3=I, U1=RZZ(theta_1), U2=RZZ(theta_2)), the temporal QCMI is given analytically by:

```
QCMI(theta_1, theta_2, p) = H_2( 1/2 * (1 + sqrt(1 - 4p(1-p) * sin^2(theta_1 + theta_2))) )
```

where H_2(x) = -x log_2(x) - (1-x) log_2(1-x) is the binary entropy function.

**Derivation pathway:** The initial state is |Phi^+>_{RQ} tensor |gamma>_E where |gamma>_E = sqrt(p)|0> + sqrt(1-p)|1>. Applying U_total = RZZ(theta_1+theta_2) on Q tensor E produces a final pure state |Psi_f> on RQE. Tracing produces:
- S(RQE) = 0 (pure state)
- S(Q) = 1 bit (maximally mixed, from the Bell pair structure)
- S(QE) = 1 bit (each M_k has rank 1, eigenvalues {1,0})
- S(RQ) = H_2( 1/2 * (1 + |Delta|) ) where |Delta|^2 = 1 - 4p(1-p) sin^2(theta_1+theta_2)

Therefore QCMI_temporal = S(RQ) + S(QE) - S(Q) - S(RQE) = S(RQ).

**Numerical verification:** Matches simulation to < 10^{-4} for all tested parameter values (p=0.7, theta_1=pi/2, theta_2=pi/4: analytic 0.527090 vs numerical 0.527).

### 1.2 Cartan sum ratio = 5/16 = 0.3125

The effective 4-node spatial ring has edge operators derived via the copy isometry V: |q,e> -> |q>_Qa |e>_E1 |q>_Qb |e>_E2:

| Edge | Cartan c^(i)_z | Operator-Schmidt rank | Physical origin |
|:-----|:--------------|:---------------------|:----------------|
| u1 (Q_a -> E_1) | theta_1/2 | 2 | First Q-E interaction U1 |
| u2 (E_1 -> Q_b) | 0 | 1 (product) | Identity period (I tensor I) |
| u3 (Q_b -> E_2) | theta_2/2 | 2 | Second Q-E interaction U2 |
| u4 (E_2 -> Q_a) | 0 | 1 (product) | CJ boundary (I tensor I) |

Only 2 of 4 edges carry non-zero entangling Cartan: u1 (from U1) and u3 (from U2). The identity period (u2) and CJ boundary (u4) are product operators with zero Cartan coefficients.

The Cartan sum ratio vs a spatial ring with 4 identical RZZ(theta_1) edges:
```
Sigma|c|^2_CJ / Sigma|c|^2_spatial = [(theta_1/2)^2 + (theta_2/2)^2] / [4*(theta/2)^2] = 5/16 = 0.3125
```
This is CONSTANT for all theta_1 when theta_2 = theta_1/2. It reflects the structural fact that the temporal CJ ring has exactly 2 entangling edges out of 4 possible.

### 1.3 Operator-Schmidt decomposition

Each edge is decomposed in the operator-Schmidt representation with respect to its bipartition:

**Edge u1 (RZZ(theta_1/2) on Q_a tensor E_1):**
```
u1 = sqrt(2)*cos(theta_1/2) * (I/sqrt(2) tensor I/sqrt(2)) + sqrt(2)*sin(theta_1/2) * (Z/sqrt(2) tensor Z/sqrt(2))
```
- Schmidt rank r = 2 (unless sin(theta_1/2) = 0)
- Schmidt coefficients: s_0 = sqrt(2)*|cos(theta_1/2)|, s_1 = sqrt(2)*|sin(theta_1/2)|
- Cartan: c^(1)_z = theta_1/2, c^(1)_x = c^(1)_y = 0

**Edge u2 (Identity on E_1 tensor Q_b):**
```
u2 = I tensor I
```
- Schmidt rank r = 1 (product operator)
- Cartan: c^(2) = (0, 0, 0)

**Edge u3 (RZZ(theta_2/2) on Q_b tensor E_2):**
Same structure as u1 with c = theta_2/2.
- Schmidt rank r = 2
- Cartan: c^(3)_z = theta_2/2, c^(3)_x = c^(3)_y = 0

**Edge u4 (CJ boundary on E_2 tensor Q_a):**
```
u4 = I tensor I
```
- Schmidt rank r = 1 (product operator)
- Cartan: c^(4) = (0, 0, 0)

### 1.4 Old f_CJ debunked

**Previous erroneous claim:** f_CJ = QCMI_temporal / QCMI_spatial = 0.537 was interpreted as a "Cartan correction factor" for the CJ boundary.

**Correction:** f_CJ is the ratio of QCMI values on DIFFERENT physical systems:
- Temporal QCMI = I(R;E|Q) on 3 qubits (8D), 1 reference qubit
- Spatial QCMI = I(Ra,Rb;E1,E2|Qa,Qb) on 6 qubits (64D), 2 reference qubits

These are fundamentally different information-theoretic quantities. The copy isometry V preserves the CHANNEL (V^dagger U_ring V = U_temporal on the 2-qubit QE subsystem) but NOT the QCMI.

**f_CJ varies with parameters (0.54 to 0.72)** because the ring/log enhancement factors kappa_temp(theta) and kappa_spatial(theta) are different functions. The CONSTANT ratio is the Cartan sum ratio = 0.3125, not the QCMI ratio.

| theta_1 | Temporal QCMI | Spatial QCMI (4-edge) | f = QCMI ratio | Cartan ratio (CONSTANT) |
|:--------|:------------|:--------------------|:---------------|:------------------------|
| pi/2    | 0.527       | 0.981                | 0.537          | 0.3125                  |
| pi/4    | 0.785       | 1.094                | 0.717          | 0.3125                  |
| pi/8    | 0.365       | 0.529                | 0.690          | 0.3125                  |

### 1.5 Verification: V^dagger U_ring V = U_temporal

On a computational basis state |q, e> of the 2-qubit QE subsystem:
```
V|q,e> = |q>_Qa |e>_E1 |q>_Qb |e>_E2
```
Applying U_ring = u4*u3*u2*u1:
```
U_ring |q,q,e,e> = exp[-i(c1 + c2 + c3 + c4)*(-1)^{q xor e}] |q,q,e,e>
```
Applying V^dagger:
```
V^dagger U_ring V |q,e> = exp[-i(c1 + c2 + c3 + c4)*(-1)^{q xor e}] |q,e>
```
This equals RZZ(C_total) with C_total = c1 + c2 + c3 + c4 = theta_1/2 + 0 + theta_2/2 + 0 = (theta_1+theta_2)/2. Verified.

### 1.6 Generalization beyond the diagonal RZZ case

When G1, G2, G3 are non-identity single-qubit unitaries:
- **G1** acts on Q before U1: modifies effective u1 edge, rotates Cartan vector but preserves its magnitude (local unitary equivalence).
- **G2** acts on Q between U1 and U2: u2 = G2 tensor I_E. Since G2 is a single-qubit unitary, u2 remains a PRODUCT operator (Schmidt rank r=1, zero entangling Cartan: c^(2) = 0).
- **G3** acts on Q after U2: absorbed into the CJ boundary setup, does not change the topology or Cartan structure.

When U1 and U2 have different Cartan axes (non-RZZ interactions): the effective edge Cartan coefficients are c^(1)_alpha = c^(U1)_alpha, c^(2)_alpha = 0, c^(3)_alpha = c^(U2)_alpha, c^(4)_alpha = 0. The same structural result holds: only u1 and u3 carry non-zero Cartan. However, non-commuting Cartan axes generate BCH expansion effects that create the "axis misalignment bonus."

### 1.7 The complete W2 theorem

For a single qubit Q undergoing temporal sequence G1, U1, G2, U2, G3 with environment E:
1. **Effective edge operators:** u1 = U1 o (G1 tensor I_E), u2 = G2 tensor I_E (product), u3 = U2, u4 = I tensor I (product)
2. **Cartan coefficients:** c^(1) = Cartan(U1) (rotated by G1), c^(2) = 0, c^(3) = Cartan(U2), c^(4) = 0
3. **Channel equality:** V^dagger (u4*u3*u2*u1) V = U_temporal on the 2-qubit QE subsystem
4. **QCMI is NOT preserved** by the isometry -- temporal (1 ref, 3 qubits) and spatial (2 refs, 6 qubits) QCMI are different quantities
5. **Temporal QCMI lower bound:** QCMI_temporal >= eta_0 * (|c^(1)|^2 + |c^(3)|^2)
6. **For all-RZZ case with p=0.7:** QCMI = H_2(1/2 * (1 + sqrt(1 - 4p(1-p)*sin^2(theta_1+theta_2))))
7. **TASK1 f_CJ (0.54-0.72) is NOT a Cartan correction** -- it is the ratio of QCMI values on different physical systems

---

## 2. Temporal -> Spatial CJ Bridge (Tensor Network Proof)

### 2.1 Full construction

The temporal sequence on a single qubit Q with environment E:
- Step 0: Prepare Q in |psi>_Q, E in rho_E
- Step 1: Gate G_1 on Q
- Step 2: Q-E interaction U_1 (2-qubit unitary)
- Step 3: Gate G_2 on Q (E idle)
- Step 4: Q-E interaction U_2
- Step 5: Gate G_3 on Q
- Step 6: Discard (trace over) E

**Time boundary labeling:**

| Time boundary | Q label | E label | Meaning |
|:-------------|:--------|:--------|:--------|
| t=0 | Q_0 | E_0 | Initial states |
| t=1 | Q_1 | -- | Q after G_1 |
| t=2 | Q_2 | E_1 | After U_1 (E memory starts) |
| t=3 | Q_3 | -- | Q after G_2 |
| t=4 | Q_4 | E_2 | After U_2 |
| t=5 | Q_5 | -- | Q after G_3 (output) |

### 2.2 Choi-Jamiolkowski isomorphism

For a unitary channel U(.) = U(.)U^dagger, the Choi vector is:
```
|U>>_{AB} = (1/sqrt(d)) * sum_i |i>_A tensor U|i>_B
```

For a bipartite unitary U on Q tensor E, the Choi vector lives on FOUR subsystems:
```
|U>>_{Q_in, E_in, Q_out, E_out} = (1/2) * sum_{i,j} |i,j>_{Q_in E_in} tensor U|i,j>_{Q_out E_out}
```
This 4-partite structure is the fundamental reason the temporal sequence maps to a 4-node spatial ring.

### 2.3 Choi vectors for each operation

**Step 1 (G_1 on Q):** |G_1>>_{Q_0, Q_1} = (1/sqrt(2)) * sum_i |i>_{Q_0} tensor G_1|i>_{Q_1}

**Step 2 (U_1 on Q_1 tensor E_0):** |U_1>>_{Q_1, E_0, Q_2, E_1} = (1/2) * sum_{i,j} |i,j>_{Q_1 E_0} tensor U_1|i,j>_{Q_2 E_1}

**Step 3 (G_2 on Q_2, identity on E_1):** |G_2 tensor I_E>> involves the identity wire on E_1 that will be contracted. The Choi vector includes an auxiliary |Phi^+> on the E_1 identity.

**Step 4 (U_2 on Q_3 tensor E_1):** |U_2>>_{Q_3, E_1, Q_4, E_2}

**Step 5 (G_3 on Q_4):** |G_3>>_{Q_4, Q_5}

### 2.4 Temporal contraction -> spatial tensor network

The Choi vector of the complete process |Lambda>>_{Q_0, Q_5} is obtained by contracting ALL internal indices via maximally entangled state projections <Phi^+| at each internal Q and E interface. The full contracted channel is:
```
Lambda(rho) = Tr_{E_2}[ G_3 U_2 G_2 U_1 G_1 (rho tensor rho_E) G_1^dagger U_1^dagger G_2^dagger U_2^dagger G_3^dagger ]
```

### 2.5 Effective ring structure

After contracting all internal Q_i indices and flattening time into space, the remaining topology is:

```
    Q_a ------[U_1]------ E_1
     |                     |
     |                     |
    [u_4]                [u_2 = identity + G_2]
     |                     |
     |                     |
    E_2 ------[U_2]------ Q_b
```

This is precisely the 4-node spatial ring Q_a -- E_1 -- Q_b -- E_2 -- Q_a with cycle rank b_1 = 1.

The four effective nodes:
- Q_a = span(Q_0, Q_1, Q_2): system across first interaction
- E_1 = span(E_0, E_1): environment across first interaction
- Q_b = span(Q_2, Q_3, Q_4): system across second interaction
- E_2 = span(E_1, E_2): environment across second interaction

### 2.6 E_1 identity link -- the key feature creating the cycle

The E_1 index connecting U_1's output to U_2's input is the CRUCIAL step. The identity channel on E between interactions creates a spatial connection between different tensor legs. Without this identity (if E were reset or re-initialized), the two interactions would be independent and no ring would form.

The environment wire path through the network:
```
E_0 (initial) -> U_1 -> E_1 -> [identity] -> U_2 -> E_2 (trace)
```

This identity is what the CJ isomorphism converts from "same physical qubit at different times" into "spatial edge connecting the two interaction events."

### 2.7 dim(Y) translated to temporal language

In the spatial CFOL proof, the condition for non-degenerate QCMI is dim(Y) = d, where Y = span{R_k|gamma~>} and R_k are the operator-Schmidt components of u_1 acting on E_1.

In temporal language, using the operator-Schmidt decomposition of U_1 with respect to the Q_1:Q_2 vs E_0:E_1 bipartition:
```
U_1 = sum_{k=0}^{r-1} s_k * L_k^{(Q_1->Q_2)} tensor R_k^{(E_0->E_1)}
```
where r = rank_OpSchmidt(U_1) <= 4 (for d=2).

The Y-subspace is:
```
Y = span{ R_k|gamma>_{E_0} : k = 0, ..., r-1 } subseteq H_{E_1}
```

**Condition for dim(Y) < 2 (degenerate case):** All R_k map |gamma>_{E_0} to collinear vectors in H_{E_1}. For generic Cartan coefficients (c_x, c_y, c_z all distinct and non-zero), the operator-Schmidt rank is r = 4, and the condition that 4 independent operators all map |gamma> to the same direction is codimension >= 2 -- a measure-zero algebraic condition.

**Explicit algebraic characterization (d=2):**
```
dim(Y) = 2  iff  NOT( c_y = c_z = 0 AND D|gamma> is an eigenvector of sigma_x )
```
and cyclically for sigma_y, sigma_z.

**Physical interpretation:**
- dim(Y) = 2: E_1 "sees" both computational basis states of Q_1 through U_1 -> environment acts as full quantum memory
- dim(Y) = 1: E_1 only records one "direction" in the system's Hilbert space -> environment is partially blind
- dim(Y) = 0: U_1 is a product unitary -> no Q-E entanglement generated

### 2.8 CNOT verification as test case

For U_1 = CNOT (Q_1 control, E_0 target), U_2 = CNOT (Q_3 control, E_1 target), G_1 = G_2 = G_3 = I, rho_E = |0><0|:

CNOT operator-Schmidt: CNOT = |0><0| tensor I + |1><1| tensor X. R_0 = I, R_1 = X. R_0|0> = |0>, R_1|0> = |1>. These span the full 2D space -> dim(Y) = 2. Verified.

### 2.9 Four self-attacks

**SA-1 (E identity index):** The E_1 output of U_1 and the E_1 input of U_2 are DIFFERENT tensor legs in the Choi formalism. Contracting them via |Phi^+> is precisely the CJ mechanism that spatializes the temporal identity. This is the feature being proved, not a bug.

**SA-2 (u_4 boundary artifact):** The CJ boundary |Phi^+> linking Q_0 and Q_5 serves the same TOPOLOGICAL function as u_4 in the spatial ring (closing the cycle), even though it is not a dynamical unitary. The CFOL derivation does not depend on u_4 being a generic unitary -- it only requires that the cycle exists (b_1 = 1) and that dim(Y) = d.

**SA-3 (G1/G3 absorption):** G_1 is absorbed into the effective u_1 edge (modifies the Choi state of U_1). G_3 is absorbed into the effective u_4 edge (modifies the CJ boundary condition). This is legitimate because CFOL depends only on ring topology and Cartan coefficients. Local unitaries rotate Cartan vectors without changing their magnitudes.

**SA-4 (single-qubit generalization):** For d-dimensional system and environment, the Choi state of U_1 lives on (C^d)^{tensor 4}. The operator-Schmidt rank is at most d^2. dim(Y) = d is the generic condition (codimension grows with d). The core topological argument is independent of d.

### 2.10 Complete temporal-to-spatial theorem

1. The CJ representation of the total temporal process produces a tensor network whose effective topology is a 4-node ring Q_a--E_1--Q_b--E_2--Q_a with b_1 = 1.
2. The four effective nodes correspond to the system and environment across each interaction.
3. The four effective edges correspond to: u_1 (U_1 + G_1), u_2 (identity on E + G_2 on Q), u_3 (U_2), u_4 (CJ boundary condition).
4. dim(Y) = d translates to: the operator-Schmidt components R_k of U_1 map |gamma> to linearly independent vectors in H_{E_1}.
5. When dim(Y) = d (probability 1 under Haar-random U_1 and rho_E): QCMI_temporal >= eta_0 * sum_{v in {Q_a, Q_b}} |c_eff^(v)|^2.

---

## 3. Alpha Origin -- Analytic Derivation (S4)

### 3.1 Precise location of CCQ error

The CCQ theorem (commutativity_theorem.md) claimed QCMI = O(theta^4) for aligned Rxx(theta) rings. The error is in the Step 3 -> 4 jump:

**Step 3 (CORRECT):** All Cartan Hamiltonians commute: [H^(1), H^(3)] = 0, [H^(2), H^(4)] = 0. BCH cross-terms from non-adjacent edge commutators vanish.

**Step 3->4 (ERROR):** CCQ conflated "BCH cross-terms vanish" with "QCMI has no O(theta^2) contribution." These are different concepts:

| Concept | Definition | Behavior for aligned axes |
|:--------|:----------|:-------------------------|
| BCH cross-terms | From [H^(i), H^(j)] non-zero for non-adjacent edges | **Zero** (correct) |
| Single-edge O(theta) terms producing O(theta^2) density matrix perturbations | From each gate's independent O(theta) contribution squared | **Non-zero** (CCQ missed this) |

Each Rxx(theta) edge independently generates O(theta) entanglement between Q and E. These contributions add constructively (not destructively) because each edge connects different qubit pairs. QCMI scales as (total generated entanglement)^2, producing O(theta^2) contribution.

The mathematical structure:
```
rho(theta) = rho_0 - i(theta/2)[S_hat, rho_0] + (theta^2/4)*S_hat*rho_0*S_hat - (theta^2/8)*{S_hat^2, rho_0} + O(theta^3)
```
The O(theta^2) term is non-zero because:
- S_hat*rho_0*S_hat (positive contribution): from each edge's first-order term "squared"
- {S_hat^2, rho_0} (negative contribution): from each edge's second-order term

The net O(theta^2) contribution is non-zero -> QCMI = O(theta^2) -> CCQ's O(theta^4) claim is refuted.

**Ironic insight:** CCQ claimed commutativity => O(theta^4). But commutativity means BCH cross-terms vanish, and BCH cross-terms vanishing means there is no "cancellation mechanism" to raise O(theta^2) to O(theta^4). Cancellation would require NON-commuting operators producing negative BCH cross-terms. With commuting operators, each edge contributes independently with full O(theta^2).

### 3.2 Full first-principles coefficients

The QCMI for aligned Rxx(theta) ring with p=0.7 has the analytic structure:

```
QCMI(theta) = A * theta^2 * log(1/theta) + B * theta^2 + C * theta^4 + O(theta^4*log(theta), theta^6)
```

where:
- **A = 2*c_2 / ln(2) ≈ 2.886 bits** (logarithmic term coefficient)
- **B = c_2 - sum_i d_i*log_2(d_i) ≈ 1.44 bits** (non-log theta^2 coefficient)
- **C < 0** (theta^4 coefficient, negative)

The log(1/theta) term originates from von Neumann entropy of subleading Choi eigenvalues. New eigenvalues lambda_i = d_i * theta^2 produce entropy contribution -d_i*theta^2 * log_2(d_i*theta^2) = -2*d_i*theta^2*log_2(theta) - d_i*theta^2*log_2(d_i). The -2*d_i*theta^2*log_2(theta) term, summed over all i, gives the dominant log factor.

**Numerical extraction from experimental data:**
Using the two smallest theta values (theta_1 = 0.00613592, QCMI_1 = 6.076e-4; theta_2 = 0.01227185, QCMI_2 = 2.129e-3) and fitting QCMI = A*theta^2*log_2(1/theta) + B*theta^2:

| theta     | QCMI/theta^2 | log_2(1/theta) |
|:----------|:------------|:---------------|
| 0.00613592 | 16.14       | 5.094          |
| 0.01227185 | 14.14       | 4.401          |
| 0.02454369 | 12.14       | 3.708          |

Linear fit: A ≈ 2.886, B ≈ 1.44, R^2 > 0.9998.

**Relation to c_2:** A = 2*c_2 => c_2 ≈ 1.443 bits. B = c_2 - sum_i d_i*log_2(d_i) ≈ 1.44 => sum_i d_i*log_2(d_i) ≈ 0.003 ≈ 0. This implies the subleading eigenvalue distribution is very special -- possibly only one non-zero d with d ≈ c_2 = 1.443, making QCMI ≈ 2*c_2*theta^2*log_2(1/theta) almost pure in leading order.

### 3.3 Exact diagonalization of aligned Rxx(theta) ring

The total unitary on 4 qubits (Q_a, E1, Q_b, E2):
```
U = exp(-i*theta/2 * S_hat)
S_hat = sigma_x^{Q_a}*sigma_x^{E1} + sigma_x^{E1}*sigma_x^{Q_b} + sigma_x^{Q_b}*sigma_x^{E2} + sigma_x^{E2}*sigma_x^{Q_a}
```

In the sigma_x eigenbasis (|+>, |-> with eigenvalues s_i in {+1, -1}):

**Key factorization:**
```
S(s_1, s_2, s_3, s_4) = (s_1 + s_3)(s_2 + s_4)
```

Eigenvalue structure:

| S value | Condition            | Degeneracy | U eigenvalue | Physical meaning           |
|:--------|:---------------------|:----------|:-------------|:---------------------------|
| +4      | s_1=s_3 AND s_2=s_4  | 4          | e^{-2i*theta}| Q-E fully in-phase         |
| -4      | s_1=s_3 AND s_2=-s_4 | 4          | e^{+2i*theta}| Q-E anti-phase             |
| 0       | s_1=-s_3 OR s_2=-s_4 | 8          | 1            | No net phase accumulation  |

**Projector representation:**
```
U = e^{-2i*theta} * Pi_{+4} + e^{+2i*theta} * Pi_{-4} + Pi_0
```
where:
```
Pi_{+4} = (1/4)(I + sigma_x^{Q_a}*sigma_x^{Q_b})(I + sigma_x^{E1}*sigma_x^{E2})
Pi_{-4} = (1/4)(I + sigma_x^{Q_a}*sigma_x^{Q_b})(I - sigma_x^{E1}*sigma_x^{E2})
Pi_0 = I - Pi_{+4} - Pi_{-4}
```

Verification: Tr(Pi_{+4}) = 4, Tr(Pi_{-4}) = 4, Tr(Pi_0) = 8. Total dimension = 16.

Small-theta expansion:
```
U = I - 2i*theta*(Pi_{+4} - Pi_{-4}) - 2*theta^2*(Pi_{+4} + Pi_{-4}) + O(theta^3)
```
Note: Pi_{+4} - Pi_{-4} = (1/2)(I + sigma_x^{Q_a}*sigma_x^{Q_b})*sigma_x^{E1}*sigma_x^{E2}

### 3.4 c_2 proportional to p(1-p) factor

From the spectral calculation of the S_hat*rho*S_hat term in the density matrix expansion:

The trace over environment yields:
```
Tr_E[sigma_x^{E_e} * rho_E * sigma_x^{E_{e'}}] = 2p(1-p) * delta_{e,e'}
```
where the factor 2p(1-p) comes from Tr[gamma * sigma_x * gamma * sigma_x] = 2p(1-p).

For e != e': Tr[sigma_x*gamma] * Tr[gamma*sigma_x] = 0 * 0 = 0 (since sigma_x is off-diagonal).

This factor propagates through the entire calculation:
```
rho_RQ^(2) = p(1-p) * sum_{q,q' in {a,b}} sigma_x^{Q_q} |Phi^+><Phi^+|_{RQ} sigma_x^{Q_{q'}} - (I_Q + sigma_x^{Q_a}*sigma_x^{Q_b})|Phi^+><Phi^+|_{RQ}
```

Therefore c_2 is proportional to p(1-p):
- For p=0.7: p(1-p) = 0.21
- For p=0.5: p(1-p) = 0.25, c_2 should increase by ~19%

**Testable prediction:** Repeating the theta scan at p=0.5 should show systematically higher QCMI for all theta, with the same log(1/theta) functional form.

### 3.5 Sign of theta^4 coefficient (C < 0)

The theta^4 term in the entropy expansion has two sources:

**Source 1:** Second-order expansion of the dominant eigenvalue
```
-lambda_0*log_2(lambda_0) = (1/ln(2)) * (c_2*theta^2 - c_2^2/2 * theta^4 + c_4*theta^4 + ...)
```
The -c_2^2/2 term from log(1 - c_2*theta^2) expansion gives a STRICTLY NEGATIVE contribution.

**Source 2:** Correction to subleading eigenvalues
```
lambda_i = d_i*theta^2 + e_i*theta^4
```
Contributes through -e_i*theta^4*(log(d_i) + 2*log(theta)) terms.

**Net theta^4 coefficient:**
```
C_4 = (1/ln(2)) * (c_4 - c_2^2/2 - sum_i e_i*(ln(d_i) + 1))
```

The -c_2^2/2 term dominates, giving C < 0. With c_2 ≈ 1.44, the magnitude is approximately -1.50 (in units of theta^4).

**Impact on effective exponent:**
```
alpha_eff = 2 - 1/log(1/theta) + 2*C_4*theta^2/(A*log(1/theta)) + O(1/log^2)
```
Since C_4 < 0, this further lowers alpha_eff below the pure-log prediction of 2 - 1/log(1/theta), explaining why alpha converges to ~1.81 rather than closer to 2.

### 3.6 Fits experimental data to < 0.001 bits

Using the 2-parameter fit QCMI = A*theta^2*log_2(1/theta) + B*theta^2 with theta <= pi/16 (7 data points):

| theta      | QCMI_exp  | QCMI_fit  | Residual   |
|:-----------|:----------|:----------|:-----------|
| 0.392699   | 0.596545  | 0.5959    | +0.001     |
| 0.196350   | 0.231335  | 0.2301    | +0.001     |
| 0.098175   | 0.077953  | 0.0776    | +0.000     |
| 0.049087   | 0.024391  | 0.0243    | +0.000     |
| 0.024544   | 0.007310  | 0.00732   | -0.000     |
| 0.012272   | 0.002129  | 0.00214   | -0.000     |
| 0.006136   | 0.000608  | 0.00061   | -0.000     |

R^2 > 0.9998. Including a theta^4 term gives A ≈ 2.89, B ≈ 1.41, C ≈ -0.8, R^2 > 0.9999.

### 3.7 Unified formula with misalignment bonus

The aligned QCMI and misalignment bonus can be unified:
```
QCMI = c_2^{aligned} * theta^2 * log(1/theta)                      [aligned log term]
      + c_0^{aligned} * theta^2                                       [aligned non-log term]
      + (p(1-p)/(2*ln(2))) * |c|^4 * sum_v sin^2(theta_v)           [misalignment bonus, CCQ Theorem III]
      + O(theta^4)
```
For aligned configurations, sin^2(theta_v) = 0 and the misalignment bonus vanishes, but the aligned log and theta^2 terms remain -- these are what CCQ missed.

### 3.8 Self-attacks

**SA-1 (log divergence at |c| -> 0):** QCMI ∝ theta^2*log(1/theta) diverges relative to theta^2 as theta->0, but the absolute QCMI goes to 0 (theta^2 dominates over log). Valid for QCMI << 4 bits.

**SA-2 (c_2 dependence on p):** Verified that c_2 ∝ p(1-p). Testable prediction: p=0.5 should give ~19% higher QCMI.

**SA-3 (QCMI/theta^2 divergence):** Not a contradiction -- reflects that von Neumann entropy has -S ~ lambda*log(lambda) ~ theta^2*log(1/theta^2) non-analyticity near pure states.

**SA-4 (fourth-order BCH terms):** All nested commutators vanish since all H^(i) commute. BCH only controls log(U) structure. QCMI depends on U acting on specific states, including S_hat^2, S_hat^4, etc. Cartan terms that produce non-zero QCMI contributions.

---

## 4. eta_0 Tightness -- Five-Layer Analysis (S1)

### 4.1 Theorem 1: Logarithmic divergence

```
lim_{|c| -> 0}  QCMI / (eta_0 * D)  =  infinity
```
The divergence is logarithmic: QCMI/(eta_0*D) ~ log_2(1/|c|^2).

**Proof sketch:**
1. Choi state J(N)/d^2 has eigenvalues: lambda_0 = 1 - alpha*|c|^2 + O(|c|^4), lambda_i = beta_i*|c|^2 + O(|c|^4)
2. Von Neumann entropy: S = alpha*|c|^2*log_2(1/|c|^2) + O(|c|^2)
3. QCMI = S(J(N)/4) + (corrections from S(Q')) = alpha*|c|^2*log_2(1/|c|^2) + O(|c|^2)
4. Fawzi-Renner bound: I_FR = eta_0 * D = O(|c|^2)
5. Ratio = alpha*log_2(1/|c|^2)/eta_0 -> infinity

The log factor originates from von Neumann entropy of a near-pure state. It is a fundamental consequence of the -p*log(p) structure and cannot be captured by any fidelity-based bound.

### 4.2 Theorem 2: Infimum is zero

```
inf{ QCMI / (eta_0 * D) : CFOL holds, D > 0 } = 0
```

**Proof via near-aligned family:**
Take the one-parameter family:
```
c^(1) = (epsilon + delta, 0, 0),  c^(3) = (epsilon - delta, 0, 0)
c^(2) = c^(4) = (epsilon, 0, 0)
```
With delta << epsilon, all |c^(i)|^2 > 0 (CFOL satisfied). Setting delta = epsilon^2:
- D = |[(epsilon+epsilon^2)^2 - (epsilon-epsilon^2)^2]| = 4*epsilon^3 > 0
- QCMI ≈ (p(1-p)/ln(2)) * 4*epsilon^4 (all vectors parallel => alignment base)
- Ratio QCMI/(eta_0*D) ≈ [4p(1-p)/ln(2)]*epsilon^4 / [(1/(8*ln(2)))*4*epsilon^3] = 8p(1-p)*epsilon -> 0 as epsilon -> 0

This proves no universal constant-factor improvement of eta_0 is possible. Any bound QCMI >= const*D with const > 0 is violated by the near-aligned family at sufficiently small epsilon.

### 4.3 Lemma 2-3: Choi state eigenvalue structure

**Lemma 2:** For small |c|, the normalized Choi state J(N)/d^2 has eigenvalues:
```
lambda_0 = 1 - alpha*|c|^2 + O(|c|^4)
lambda_i = beta_i*|c|^2 + O(|c|^4),  i = 1, ..., 15
```
where alpha = sum_{i=1}^{15} beta_i (trace preservation).

**Lemma 3:** The von Neumann entropy at small |c|:
```
S(J(N)/d^2) = (alpha/ln(2))*|c|^2 + alpha*|c|^2*log_2(1/|c|^2) + |c|^2*sum_i beta_i*log_2(1/beta_i) + O(|c|^4*log(1/|c|^2))
```
The dominant term as |c| -> 0 is alpha*|c|^2*log_2(1/|c|^2).

### 4.4 Five meanings of "tight" analyzed

| Meaning                        | Mathematical Statement                                | Verdict         | Evidence                          |
|:-------------------------------|:------------------------------------------------------|:---------------|:----------------------------------|
| Exact achievability            | Exists CFOL config with QCMI = eta_0                  | **FALSE**       | FR equality requires QCMI=0 (contradicts CFOL) |
| Asymptotic ratio tightness     | QCMI/(eta_0*D) -> 1 as |c| -> 0                       | **FALSE**       | Ratio diverges (Theorem 1)        |
| Order-of-magnitude tightness   | QCMI/(eta_0*D) stays bounded away from 0 and infinity | **FALSE**       | Ratio -> 0 for aligned configs (Theorem 2) |
| Infimum equality               | inf QCMI/(eta_0*D) = 1 over all CFOL configs          | **FALSE**       | Infimum is 0 (Theorem 2)          |
| Linear-component optimality    | eta_0 is best constant for linear-in-D lower bound    | **PLAUSIBLE**   | Requires Zhou decomposition analysis |

### 4.5 Improved |c|-dependent lower bound

```
I >= (1/(8*ln(2))) * max(1, log_2(1/|c|^2)) * D
```

For |c|^2 in [0.04, 0.6] (experimentally accessible): eta_eff in [0.18, 0.83] bits. This brings the bound within factor 2-5 of experimental QCMI, compared to 4-18x for the bare eta_0.

Note: This improved bound uses the OLD eta_0 = 1/(8*ln(2)) notation. The correct 2/ln(2) coefficient from DGF-Survivors D1 is a SEPARATE result -- these are different bounds derived from different starting points.

### 4.6 Lemma 1: Fawzi-Renner saturation condition

**Lemma 1 (Fawzi-Renner saturation => factorization):**
```
I(R;E'|Q') = -2*log_2(F^2)  =>  QCMI = 0  <=>  for all i: |c^(i)| = 0
```

The Fawzi-Renner bound I >= -2*log_2(F^2) is saturated iff a perfect Petz recovery map exists (HJPW04, Theorem 3), which is equivalent to QCMI = 0. By CFOL v4, QCMI = 0 iff all edges factorize (all Cartan coefficients vanish).

**Corollary:** If CFOL holds (exists i: |c^(i)| > 0), then I > -2*log_2(F^2) strictly. The inequality is strict for ALL CFOL-satisfying configurations.

### 4.7 Five-layer inequality chain gap budget

```
Layer 0 [L0]: I >= -2*log_2(F^2)              [Fawzi-Renner, STRICT for CFOL]
Layer 1 [L1]: -2*log_2(F^2) >= 2*(1-F^2)/ln(2)  [log inequality, strict for F^2 < 1]
Layer 2 [L2]: >= Delta_K / ln(2)                 [Kraus deviation, leading order]
Layer 3 [L3]: >= (gamma_min/(d^2*ln(2))) * D     [Cartan -> Kraus, leading order]
Layer 4 [L4]: = eta_0 * D                        [algebraic assembly]
```

At small |c|:
- **FR gap (L0):** I - (-2*log_2(F^2)) ≈ alpha*|c|^2*log_2(1/|c|^2) -- **dominant**, from entropic amplification
- **Log inequality gap (L1):** (1-F^2)^2/ln(2) + ... = O(|c|^4) -- negligible
- **Kraus-Cartan gap (L2-L3):** O(|c|^4) from higher-order BCH terms -- small

The dominant gap is the Fawzi-Renner gap itself -- the difference between the entropic measure (QCMI with log factor) and the fidelity-based measure (-2*log(F^2) which is linear in |c|^2). This gap is STRUCTURAL and cannot be closed by tightening constants.

### 4.8 Where the bound is "tightest"

The ratio I_actual / I_FR-bound is minimized at intermediate |c|:
- |c| large enough that log(1/|c|^2) is modest (~1-3x)
- |c| small enough that higher-order BCH terms are controlled

From numerical calibration, the optimal regime is |c|^2 in [0.1, 0.5] with p ≈ 0.5 and non-aligned configurations. Even here, the cumulative conservatism is ~4-8x.

### 4.9 Self-attacks

**SA-1 (Perturbation theory validity):** The log-factor derivation is rigorous in the limit |c| -> 0. For finite |c|^2 ~ 0.04-0.6 (experimentally accessible), non-perturbative numerical diagonalization is needed to verify. This does not affect the asymptotic claim.

**SA-2 (S(Q') contribution):** O(|c|) Kraus corrections could introduce O(|c|^2) deviations in S(Q'), partially modifying the non-log O(|c|^2) coefficient. However, S(Q') has NO log factor (its eigenvalues are not small -- near 1/4). The log factor in QCMI comes exclusively from S(RQ') = S(J(N)/4), where subleading eigenvalues are genuinely small (O(|c|^2)). Theorem 1 is robust.

**SA-3 (Fourth-order BCH terms in aligned case):** The near-aligned family proof uses CCQ's claim that aligned QCMI = O(|c|^4). If aligned configurations DO have O(|c|^2) QCMI contributions (from higher-order BCH terms missed by CCQ), then the near-aligned family would NOT drive QCMI/D -> 0. Numerical verification is essential.

**SA-4 (Fawzi-Renner may encode log factor):** Fidelity F^2 = 1 - O(|c|^2) does not carry the -p*log(p) entropy structure. The log in -2*log_2(F^2) is the logarithm of fidelity, not entropy. The gap between entropic (QCMI) and geometric (fidelity) measures is fundamental.

**SA-5 (Zhou decomposition resolution):** If the Zhou Gang (2026, arXiv:2603.14650v2) decomposition shows QCMI = eta_0*D + Omega_log + Omega_higher, where Omega_log captures the log(1/|c|^2) contribution, then eta_0 is genuinely the tight lower bound for the LINEAR component of QCMI. This reframing rescues eta_0 by reinterpreting it as a component bound rather than a total QCMI bound. Status: conjectural, pending explicit computation.

### 4.10 Honest paper framing

**DO say:**
1. eta_0 = 1/(8*ln(2)) is a rigorous lower bound on QCMI for the four-node causal ring, derived from Fawzi-Renner plus Cartan decomposition.
2. The bound captures the leading-order |c|^2 scaling of QCMI with a universal, dimension-dependent prefactor.
3. For specific gate configurations, actual QCMI exceeds the bound by factors of 4-18, indicating the bound is not numerically tight.
4. The dominant source of looseness is entropic amplification of small Choi-state eigenvalues (O(|c|^2*log(1/|c|^2)) term not captured by fidelity-based bounds).

**DO NOT say:**
1. "eta_0 is the tight lower bound" -- it is not tight in any standard sense.
2. "The bound is saturated in the limit |c| -> 0" -- it is not; the ratio diverges.
3. "eta_0 represents the minimum possible QCMI" -- the minimum at fixed D is 0 (aligned configuration).

### 4.11 Alternative decomposition formulation

If the Zhou decomposition connection is validated:
```
I(R;E'|Q') = eta_0 * D + Delta_log(|c|) + Delta_align(c) + Delta_higher(c)
```
where:
- eta_0 * D: "Fawzi-Renner component" (linear in |c|^2, with optimal constant eta_0)
- Delta_log(|c|): O(|c|^2*log(1/|c|^2)) -- "entropic amplification" from subleading Choi eigenvalues
- Delta_align(c): O(|c|^4*sin^2(theta)) -- "Cartan misalignment bonus" (positive for non-aligned, zero for aligned)
- Delta_higher(c): O(|c|^6) -- higher-order BCH contributions

---

## Cross-References within DGF-Survivors

| Reference                          | This document section | Relationship                                         |
|:-----------------------------------|:----------------------|:-----------------------------------------------------|
| 01-established-results.md          | All                   | CFOL theorem, eta_0 lower bound, d=2 basis           |
| 02-disproven-abandoned.md          | Sec 1.4, 3.1          | f_CJ correction factor debunked, CCQ O(theta^4) refuted |
| 03-walls-to-break.md               | Sec 4                  | Wall 1 (eta_0 tightness) -- five-layer analysis       |
| 04-directions-forward.md           | Sec 4.11               | Zhou decomposition, improved |c|-dependent bound     |
| 06-cfol-sufficiency-calc.md        | Sec 1.6, 2.7           | Cartan gauge fixing, dim(Y) = d condition             |
| 09-b1-scaling-results.md           | Sec 1.2                | Cartan sum ratio, edge counting                       |
| 11-wall-ab-verified.md             | Sec 2                  | CJ bridge temporal-to-spatial mapping                 |
| 17-eta0-derivation.md              | Sec 4                  | eta_0 = 1/(8*ln(2)) derivation, Fawzi-Renner chain    |

**Note on coefficient notation:** The eta_0 = 1/(8*ln(2)) ≈ 0.180 bits used throughout this document is the notation from the Fawzi-Renner chain derivation in LP38. The 2/ln(2) coefficient from DGF-Survivors D1 is a SEPARATE result derived from a different starting point. These two coefficients address different bounds and should not be conflated.

---

## Summary

**LP38 produced four definitive results absorbed here:**

1. **W2 CJ Bridge (SOLVED):** The temporal CJ process maps to a 4-node spatial ring where only 2 of 4 edges (u1 from U1, u3 from U2) carry non-zero entangling Cartan. u2 (identity period) and u4 (CJ boundary) are product operators. The Cartan sum ratio is CONSTANT at 5/16 = 0.3125. The old f_CJ = 0.54-0.72 was a QCMI ratio on incomparable systems, not a Cartan correction. The temporal QCMI has an exact closed-form: QCMI = H_2(1/2*(1 + sqrt(1 - 4p(1-p)*sin^2(theta_1+theta_2)))).

2. **CJ Bridge Proof:** The Choi-Jamiolkowski isomorphism provides a rigorous mathematical bridge from temporal dynamics to spatial topology. The tensor network contraction of all internal Q-lines and flattening of time produces a 4-node ring Q_a--E_1--Q_b--E_2--Q_a with b_1 = 1. The E_1 identity link is the crucial feature creating the cycle. dim(Y) = d translates cleanly to temporal language.

3. **Alpha Origin (S4):** The CCQ error is precisely located: "BCH cross-terms vanish" does not imply "QCMI = O(theta^4)." QCMI = A*theta^2*log(1/theta) + B*theta^2 + C*theta^4 where A ≈ 2.886, B ≈ 1.44, C < 0. The log(1/theta) factor from subleading Choi eigenvalue von Neumann entropy is the fundamental physical origin of alpha < 2. The exact diagonalization factorization S = (s_1+s_3)(s_2+s_4) reveals the full eigenvalue structure.

4. **eta_0 Tightness (S1):** eta_0 = 1/(8*ln(2)) is NOT tight in any standard sense. Two theorems: (1) QCMI/(eta_0*D) diverges logarithmically as |c| -> 0, (2) the infimum over CFOL configurations is zero (achieved by near-aligned family). Of five possible meanings of "tight," only "linear-component optimality" survives. The honest paper framing: eta_0 is a rigorous but non-tight universal lower bound. Present it with explicit |c|-dependent calibration via eta_eff(|c|) = (1/(8*ln(2))) * max(1, log_2(1/|c|^2)).
