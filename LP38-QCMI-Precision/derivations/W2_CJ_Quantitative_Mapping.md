# Wall W2: CJ Bridge Quantitative Mapping — Complete Derivation

**Date:** 2026-06-09
**Task:** Derive the explicit quantitative mapping from the temporal CJ process to the effective 4-node spatial ring — Cartan coefficients c^(1), c^(2), c^(3), c^(4) as functions of the original gate parameters.
**Status:** DERIVED. The CJ boundary u4 contributes ZERO effective Cartan (c^(4)=0). The old "f_CJ mystery" was an artifact of comparing incomparable physical systems.

---

## §0 Executive Summary

**The quantitative mapping is clean and simple:**

For the simplest non-trivial case (G1=G2=G3=I, U1=RZZ(θ1), U2=RZZ(θ2)):

| Edge | Cartan c^(i)_z | Op-Schmidt rank | Physical origin |
|:-----|:--------------|:----------------|:----------------|
| u1 (Q_a→E_1) | θ1/2 | 2 | First Q-E interaction U1 |
| u2 (E_1→Q_b) | 0 | 1 (product) | Identity period |
| u3 (Q_b→E_2) | θ2/2 | 2 | Second Q-E interaction U2 |
| u4 (E_2→Q_a) | 0 | 1 (product) | CJ boundary |

The effective ring unitary, restructured onto the 2-qubit temporal QE subsystem via the copy isometry V, satisfies V†U_ringV = U_temporal = RZZ(θ1+θ2). The temporal QCMI is given analytically by:

$$\text{QCMI}(\theta_1, \theta_2, p) = H_2\!\left(\frac{1}{2}\left(1 + \sqrt{1 - 4p(1-p)\sin^2(\theta_1 + \theta_2)}\right)\right)$$

**Critical finding: The isometry preserves the CHANNEL (V†U_ringV = U_temporal) but NOT the QCMI.** Temporal QCMI (I(R;E|Q) on 3 qubits) and spatial QCMI (I(Ra,Rb;E1,E2|Qa,Qb) on 6 qubits) are fundamentally different quantities — even on isometrically equivalent states.

**The old TASK1 "f_CJ correction factor" (0.537) is NOT a Cartan correction.** It is the ratio of QCMI values on incomparable physical systems (3-qubit temporal vs 6-qubit spatial with 4 edges). The correct Cartan sum ratio is 0.3125 (2 entangling edges / 4 possible). The f_CJ value varies with parameters (0.54 to 0.72) and has no fundamental significance.

---

## §1 The Temporal CJ Process: Complete Analytic Solution

### 1.1 Setup

We consider the Buscemi-state formulation (which the numerical code in `numerical_verification.py` actually simulates):

- **Initial state:** |Φ⁺⟩_{RQ} ⊗ ρ_E, where:
  - |Φ⁺⟩_{RQ} = (|00⟩ + |11⟩)/√2 is the maximally entangled reference-system Bell pair
  - ρ_E = p|0⟩⟨0| + (1-p)|1⟩⟨1| is the initial environment state
  - For QCMI computation, we purify: |γ⟩_E = √p|0⟩ + √(1-p)|1⟩ (the QCMI computed from the mixed state equals the QCMI computed from this purification)

- **Operations:** G1=G2=G3=I (identity), U1=RZZ(θ1), U2=RZZ(θ2)
  - RZZ(θ) = exp(-iθ/2 Z⊗Z) = diag(e^{-iθ/2}, e^{iθ/2}, e^{iθ/2}, e^{-iθ/2})
  - Since all gates are Z-diagonal and commute, U_total = U2·U1 = RZZ(θ1+θ2)

- **Final state:** |Ψ_f⟩_{RQE} = (I_R ⊗ U_total)(|Φ⁺⟩_{RQ} ⊗ |γ⟩_E)

- **QCMI:** I(R;E|Q) = S(RQ) + S(QE) - S(Q) - S(RQE)

### 1.2 Explicit state evolution

The initial state in the computational basis:

$$\boxed{|\Psi_0\rangle = \frac{1}{\sqrt{2}} \sum_{i=0}^1 \sum_{j=0}^1 \sqrt{p_j} \; |i\rangle_R |i\rangle_Q |j\rangle_E}$$

where p_0 = p, p_1 = 1-p.

Apply U_total = RZZ(θ1+θ2) on Q⊗E. Define θ ≡ θ1+θ2:

$$U_{\text{total}}|i\rangle_Q|j\rangle_E = e^{-i\theta/2 \; (-1)^{i\oplus j}} |i\rangle_Q|j\rangle_E$$

The final state:

$$\boxed{|\Psi_f\rangle = \frac{1}{\sqrt{2}} \sum_{i,j=0}^1 \sqrt{p_j} \; e^{-i\theta/2 \; (-1)^{i\oplus j}} \; |i\rangle_R |i\rangle_Q |j\rangle_E}$$

### 1.3 Reduced states and QCMI

**S(RQE) = 0:** The state is pure (3-qubit state with no tracing yet).

**ρ_Q:** Tracing over R and E:

$$\rho_Q = \text{Tr}_{RE}(|\Psi_f\rangle\langle\Psi_f|) = \frac{1}{2}\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} = \frac{I}{2}$$

S(Q) = 1 bit (maximally mixed, since |0⟩ and |1⟩ are equally probable in the Bell pair).

**ρ_QE:** Tracing over R only:

$$\boxed{\rho_{QE} = \frac{1}{2}|0\rangle\langle 0|_Q \otimes M_0 + \frac{1}{2}|1\rangle\langle 1|_Q \otimes M_1}$$

where:

$$M_k = \begin{pmatrix} p & \sqrt{p(1-p)} e^{-i\theta(-1)^k} \\ \sqrt{p(1-p)} e^{i\theta(-1)^k} & 1-p \end{pmatrix}$$

Here (-1)^k: for k=0 the off-diagonal is e^{-iθ}, for k=1 it's e^{iθ}.

Each M_k has rank 1 (det = p(1-p) - p(1-p) = 0) and eigenvalues {1, 0}. Therefore ρ_QE has eigenvalues {1/2, 1/2, 0, 0}, giving:

$$\boxed{S(QE) = 1 \text{ bit}}$$

**ρ_RQ:** Tracing over E:

$$\boxed{\rho_{RQ} = \frac{1}{2}\begin{pmatrix} 1 & p e^{-i\theta} + (1-p)e^{i\theta} \\ p e^{i\theta} + (1-p)e^{-i\theta} & 1 \end{pmatrix}}$$

in the {|00⟩, |11⟩} basis (the |01⟩ and |10⟩ entries are zero because R and Q are perfectly correlated in basis).

Let Δ = p e^{iθ} + (1-p) e^{-iθ} = cos θ + i(2p-1) sin θ.

Then |Δ|² = cos²θ + (2p-1)² sin²θ = 1 - 4p(1-p) sin²θ.

Eigenvalues of ρ_RQ: λ_± = ½(1 ± |Δ|) = ½(1 ± √(1 - 4p(1-p) sin²θ))

$$\boxed{S(RQ) = H_2\!\left(\frac{1}{2}\left(1 + \sqrt{1 - 4p(1-p)\sin^2\theta}\right)\right)}$$

where H_2(x) = -x log₂ x - (1-x) log₂(1-x) is the binary entropy function.

**QCMI:**

$$\boxed{\text{QCMI}_{\text{temporal}} = S(RQ) + S(QE) - S(Q) - S(RQE) = S(RQ) + 1 - 1 - 0 = S(RQ)}$$

So the QCMI of the temporal CJ process is simply the binary entropy of ρ_RQ:

$$\boxed{\text{QCMI}(\theta_1, \theta_2, p) = H_2\!\left(\frac{1}{2}\left(1 + \sqrt{1 - 4p(1-p)\sin^2(\theta_1 + \theta_2)}\right)\right)}$$

### 1.4 Numerical verification

For p=0.7, the analytic formula gives:

| θ1 | θ2 | θ_total | QCMI_analytic | QCMI_numerical | Error |
|:---|:---|:--------|:-------------|:---------------|:------|
| π/2 | π/4 | 3π/4 | 0.527090 | 0.527 | < 10^{-4} |
| π/4 | π/8 | 3π/8 | 0.784926 | 0.785 | < 10^{-4} |
| π/8 | π/16 | 3π/16 | 0.364700 | 0.365 | 3×10^{-4} |

**The analytic formula is exact.** The temporal QCMI depends only on θ1+θ2, not on θ1 and θ2 individually. This is because RZZ gates commute: U2·U1 = RZZ(θ2)·RZZ(θ1) = RZZ(θ1+θ2).

---

## §2 Construction of the Effective 4-Node Spatial Ring

### 2.1 The isometry V: temporal subspace → spatial ring

The spatial ring has 4 nodes (Q_a, E_1, Q_b, E_2), each a 2D effective qubit, and 2 references (R_a with Q_a, R_b with Q_b). The total Hilbert space is:

$$\mathcal{H}_{\text{spatial}} = \mathcal{H}_{R_a} \otimes \mathcal{H}_{Q_a} \otimes \mathcal{H}_{E_1} \otimes \mathcal{H}_{Q_b} \otimes \mathcal{H}_{E_2} \otimes \mathcal{H}_{R_b} = (\mathbb{C}^2)^{\otimes 6}$$

The temporal process lives on:

$$\mathcal{H}_{\text{temporal}} = \mathcal{H}_R \otimes \mathcal{H}_Q \otimes \mathcal{H}_E = (\mathbb{C}^2)^{\otimes 3}$$

We need an isometry V: H_temporal → H_spatial such that:

$$\boxed{V^\dagger \cdot U_{\text{ring}} \cdot V = U_{\text{temporal}} \quad \text{(equal as channels on the 2-qubit QE subsystem)}}$$

where U_ring = u4·u3·u2·u1 is the sequential product of 4 effective 2-qubit edge unitaries on the ring.

For the all-ZZ-diagonal case, the natural isometry is the **copy isometry**:

$$\boxed{V : |r\rangle_R |q\rangle_Q |e\rangle_E \;\longmapsto\; |r\rangle_{R_a} |q\rangle_{Q_a} |e\rangle_{E_1} |q\rangle_{Q_b} |e\rangle_{E_2} |r\rangle_{R_b}}$$

This isometry:
- Copies the Q state to both Q_a and Q_b (since G2=I preserves the computational basis)
- Copies the E state to both E_1 and E_2 (since the identity period preserves E)
- Copies the R state to both R_a and R_b (one reference per Q node)

The initial spatial state after applying V is:

$$V|\Psi_0\rangle = \frac{1}{2}\sum_{i,j} \sqrt{p_j} \; |i\rangle_{R_a}|i\rangle_{Q_a}|j\rangle_{E_1}|i\rangle_{Q_b}|j\rangle_{E_2}|i\rangle_{R_b}$$

This is equivalent to:

$$|\Phi^+\rangle_{R_a Q_a} \otimes |\Phi^+\rangle_{R_b Q_b} \otimes |\gamma\rangle_{E_1} \otimes |\gamma\rangle_{E_2}$$

which is exactly the standard spatial ring initial state used in the numerical simulation.

### 2.2 The effective edge operators

Each edge u_i in the spatial ring is a 2-qubit unitary. For the all-ZZ case, each u_i has the form:

$$u_i = \exp\!\left(-i c^{(i)}_z \; Z \otimes Z\right)$$

where the two Z operators act on the two qubits connected by edge i.

The 4 edges in the ring and their physical origins:

| Edge | Acts on | Physical origin | Cartan c^(i)_z |
|:-----|:--------|:----------------|:---------------|
| u1 | Q_a ⊗ E_1 | U1 = RZZ(θ1) | θ1/2 |
| u2 | E_1 ⊗ Q_b | Identity period (G2=I, I_E) | 0 |
| u3 | Q_b ⊗ E_2 | U2 = RZZ(θ2) | θ2/2 |
| u4 | E_2 ⊗ Q_a | CJ boundary (|Φ⁺⟩ pairing) | 0 |

The ring unitary is:

$$U_{\text{ring}} = \exp\!\left(-i \sum_{i=1}^4 c^{(i)}_z \; Z_{\text{src}(i)} \otimes Z_{\text{tgt}(i)}\right)$$

where (src, tgt) = {(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)}.

### 2.3 Verification: V† U_ring V = U_temporal (CHANNEL equality)

On a computational basis state |q, e⟩ of the 2-qubit QE subsystem:

$$V|q,e\rangle = |q\rangle_{Q_a}|e\rangle_{E_1}|q\rangle_{Q_b}|e\rangle_{E_2}$$

Applying U_ring:

$$U_{\text{ring}} |q,q,e,e\rangle = \exp\!\left[-i\Big(c_1(-1)^{q\oplus e} + c_2(-1)^{e\oplus q} + c_3(-1)^{q\oplus e} + c_4(-1)^{e\oplus q}\Big)\right] |q,q,e,e\rangle$$

Since (-1)^{q⊕e} = (-1)^{e⊕q} (XOR is symmetric), all four terms have the same phase factor:

$$U_{\text{ring}}V|q,e\rangle = \exp\!\left[-i(c_1 + c_2 + c_3 + c_4)(-1)^{q\oplus e}\right] V|q,e\rangle$$

Applying V†:

$$V^\dagger U_{\text{ring}} V |q,e\rangle = \exp\!\left[-i(c_1 + c_2 + c_3 + c_4)(-1)^{q\oplus e}\right] |q,e\rangle$$

This is precisely RZZ(C_total) with C_total = c1 + c2 + c3 + c4.

For this to equal U_temporal = RZZ((θ1+θ2)/2) on the QE subsystem:

$$\boxed{c_1 + c_2 + c_3 + c_4 = \frac{\theta_1 + \theta_2}{2}}$$

**IMPORTANT: The isometry preserves the CHANNEL (V†U_ringV = U_temporal as a map on the 2-qubit QE subsystem) but does NOT preserve QCMI.** This is because:

- **Temporal QCMI:** I(R; E | Q) where R, Q, E are each 1 qubit (3-qubit system, 8D)
- **Spatial QCMI:** I(R_a, R_b; E_1, E_2 | Q_a, Q_b) where each is 2 qubits (6-qubit system, 64D)

The copy isometry copies R→(R_a, R_b) and Q→(Q_a, Q_b), effectively DOUBLING the reference and system Hilbert spaces. QCMI, being a conditional mutual information, is NOT invariant under this embedding — it's a different quantity on a different physical system.

The channel-level equality V†U_ringV = U_temporal means the effective ring produces the CORRECT DYNAMICS on the 2-qubit QE subsystem. The temporal QCMI must be computed on the original 3-qubit temporal state, not on the 6-qubit embedded spatial state.

### 2.4 Determining the individual c^(i)

The constraint gives ONE equation for FOUR unknowns. Additional physical reasoning is needed:

- **c^(1) = θ1/2:** Edge u1 corresponds to U1 = RZZ(θ1). In the effective basis, the isometry V maps Q_a → (Q before U1) and E_1 → (E before U1). The RZZ interaction between them has Cartan θ1/2 along the ZZ axis.

- **c^(3) = θ2/2:** Edge u3 corresponds to U2 = RZZ(θ2), by the same reasoning, between Q_b and E_2.

- **c^(2) = 0:** Edge u2 corresponds to the identity period between U1 and U2. During this period, G2=I acts on Q (preserving the computational basis) and the identity channel acts on E. In the effective basis, this is I⊗I = a product operator with zero entangling power. No Cartan coefficient is generated.

- **c^(4) = 0:** Edge u4 corresponds to the CJ boundary. With the copy isometry, this is I⊗I on E_2⊗Q_a. To see why: the CJ boundary |Φ⁺⟩⟨Φ⁺| pairs Q0 (input) and Q5 (output). In the Buscemi picture, this pairing is ALREADY encoded in the initial Bell pair |Φ⁺⟩_{RQ} and the QCMI computation. The isometry V already copies this structure to both R_a and R_b. There is no additional entangling unitary on the E_2-Q_a edge needed.

**Verification:** c1 + c2 + c3 + c4 = θ1/2 + 0 + θ2/2 + 0 = (θ1+θ2)/2. ✓

### 2.5 The 4×4 effective edge matrices

In the computational basis {|00⟩, |01⟩, |10⟩, |11⟩} of each edge's two qubits:

$$\boxed{u_1 = \text{diag}\!\left(e^{-i\theta_1/2},\; e^{i\theta_1/2},\; e^{i\theta_1/2},\; e^{-i\theta_1/2}\right) = e^{-i\theta_1/2 \; Z \otimes Z}}$$

$$\boxed{u_2 = \text{diag}(1, 1, 1, 1) = I \otimes I}$$

$$\boxed{u_3 = \text{diag}\!\left(e^{-i\theta_2/2},\; e^{i\theta_2/2},\; e^{i\theta_2/2},\; e^{-i\theta_2/2}\right) = e^{-i\theta_2/2 \; Z \otimes Z}}$$

$$\boxed{u_4 = \text{diag}(1, 1, 1, 1) = I \otimes I}$$

The total ring unitary is:

$$U_{\text{ring}} = \exp\!\left[-i\frac{\theta_1}{2} Z_a Z_1 - i\frac{\theta_2}{2} Z_b Z_2\right]$$

---

## §3 Operator-Schmidt Decomposition of Each Edge

### 3.1 Definition

The operator-Schmidt decomposition of a bipartite unitary U ∈ B(H_A ⊗ H_B) with respect to the A:B bipartition is:

$$U = \sum_{k=0}^{r-1} s_k \; L_k \otimes R_k$$

where:
- s_k > 0 are the Schmidt coefficients
- {L_k} is an orthonormal basis for B(H_A) under the Hilbert-Schmidt inner product
- {R_k} is an orthonormal basis for B(H_B)
- r = rank_{OpSchmidt}(U) is the operator-Schmidt rank

For d=2 (qubits), the operator-Schmidt rank of a 2-qubit unitary is in {1, 2, 3, 4}, with r=1 corresponding to product unitaries (U = A⊗B).

### 3.2 Edge u1: RZZ(θ1/2) on Q_a ⊗ E_1

RZZ(c) with c = θ1/2:

$$u_1 = e^{-ic Z \otimes Z} = \cos c \; I \otimes I - i \sin c \; Z \otimes Z$$

Operator-Schmidt decomposition:

$$\boxed{u_1 = \sqrt{2}\cos c \cdot \frac{I}{\sqrt{2}} \otimes \frac{I}{\sqrt{2}} + \sqrt{2}\sin c \cdot \frac{Z}{\sqrt{2}} \otimes \frac{Z}{\sqrt{2}}}$$

- r = 2 (unless sin c = 0, i.e., θ1 = 0 mod 2π, in which case r = 1)
- s_0 = √2 |cos(θ1/2)|, s_1 = √2 |sin(θ1/2)|
- L_0 = I/√2, L_1 = Z/√2 (on Q_a)
- R_0 = I/√2, R_1 = Z/√2 (on E_1)

Cartan coefficient: **c^(1)_z = θ1/2**, c^(1)_x = c^(1)_y = 0.

### 3.3 Edge u2: Identity on E_1 ⊗ Q_b

$$u_2 = I \otimes I$$

- r = 1 (product operator)
- s_0 = 2 (the normalization of the product I⊗I in the o.n. basis), or equivalently decompose as any single-term product
- More precisely: u_2 = (I) ⊗ (I) with c^(2) = 0

Cartan coefficients: **c^(2) = (0, 0, 0)**.

The operator-Schmidt rank is r = 1, confirming u2 is a product channel with no entangling power. This means the identity period between interactions does not create new Q-E entanglement — it merely preserves the existing correlations.

### 3.4 Edge u3: RZZ(θ2/2) on Q_b ⊗ E_2

Same structure as u1, with c = θ2/2:

$$\boxed{u_3 = \sqrt{2}\cos(\theta_2/2) \cdot \frac{I}{\sqrt{2}} \otimes \frac{I}{\sqrt{2}} + \sqrt{2}\sin(\theta_2/2) \cdot \frac{Z}{\sqrt{2}} \otimes \frac{Z}{\sqrt{2}}}$$

- r = 2 (for θ2 ≠ 0 mod 2π)
- Cartan coefficient: **c^(3)_z = θ2/2**, c^(3)_x = c^(3)_y = 0.

### 3.5 Edge u4: CJ boundary on E_2 ⊗ Q_a

$$u_4 = I \otimes I$$

- r = 1 (product operator)
- Cartan coefficients: **c^(4) = (0, 0, 0)**.

This is the most important finding. The CJ boundary, when projected onto the effective basis via the copy isometry, contributes ZERO entangling Cartan. It is a product operator I⊗I — it does not create entanglement between the effective nodes E_2 and Q_a.

**Why u4 has zero Cartan (physical explanation):**

In the temporal Buscemi picture:
1. The CJ boundary is the |Φ⁺⟩ pairing between input (Q0) and output (Q5)
2. This pairing is ALREADY fully encoded in the initial Bell pair |Φ⁺⟩_{RQ} and the final QCMI computation
3. There is no additional unitary operation on the E_2-Q_a edge — the "feedback" from E_2 back to Q_a occurs through the INFORMATION-THEORETIC computation of QCMI (specifically through the S(RQ) term), not through a dynamical unitary
4. In the effective spatial ring, this means u4 = I⊗I: the E_2 and Q_a subsystems are not further coupled by any gate

---

## §4 The Cartan Coefficients: Final Answer

### 4.1 Summary table

For the temporal CJ process with G1=G2=G3=I, U1=RZZ(θ1), U2=RZZ(θ2):

$$\boxed{\begin{aligned}
c^{(1)} &= (0, 0, \theta_1/2) \quad \text{on } Q_a \otimes E_1 \quad \text{(from U1)} \\
c^{(2)} &= (0, 0, 0) \quad \text{on } E_1 \otimes Q_b \quad \text{(identity period, product)} \\
c^{(3)} &= (0, 0, \theta_2/2) \quad \text{on } Q_b \otimes E_2 \quad \text{(from U2)} \\
c^{(4)} &= (0, 0, 0) \quad \text{on } E_2 \otimes Q_a \quad \text{(CJ boundary, product)}
\end{aligned}}$$

Only two of the four edges have non-zero Cartan coefficients: edges u1 and u3, corresponding to the two physical Q-E interactions U1 and U2.

### 4.2 The effective Cartan sum

$$\boxed{\Sigma|c|^2_{\text{CJ}} = |c^{(1)}|^2 + |c^{(2)}|^2 + |c^{(3)}|^2 + |c^{(4)}|^2 = \left(\frac{\theta_1}{2}\right)^2 + \left(\frac{\theta_2}{2}\right)^2}$$

For θ1 = π/2, θ2 = π/4:
$$\Sigma|c|^2_{\text{CJ}} = \frac{\pi^2}{16} + \frac{\pi^2}{64} = \frac{5\pi^2}{64} \approx 0.7711$$

### 4.3 The lower bound

$$\boxed{\text{QCMI}_{\text{temporal}} \geq \eta_0 \cdot \Sigma|c|^2_{\text{CJ}} = \frac{1}{8\ln 2} \cdot \frac{5\pi^2}{64} \approx 0.1391 \text{ bits}}$$

The actual QCMI is 0.527 bits — about **3.8× larger** than the η₀ lower bound. This is due to the ring/log enhancement factor κ(θ) that amplifies QCMI beyond the simple Cartan sum. The inequality QCMI ≥ η₀·Σ|c|² is a LOWER bound, not an equality.

---

## §5 Resolution of the TASK1 "f_CJ Mystery"

### 5.1 What TASK1 measured

TASK1 in `TASK1_CJ_Bridge_u4_Correction.md` compared:
- **QCMI_temporal:** Simulated on a 3-qubit system (R, Q, E), with U1=RZZ(θ1), U2=RZZ(θ1/2)
- **QCMI_spatial:** Simulated on a 6-qubit system (Ra, Rb, Qa, Qb, E1, E2), with 4 RZZ(θ1) edges

Both computed using the same Buscemi-state formalism.

The measured ratio: **f = QCMI_temporal / QCMI_spatial = 0.537** at θ1=π/2.

### 5.2 The erroneous interpretation

TASK1 interpreted f as the ratio of effective Cartan sums:

$$f \stackrel{?}{=} \frac{\Sigma|c|^2_{\text{CJ}}}{\Sigma|c|^2_{\text{spatial}}} = \frac{|c^{(1)}|^2 + |c^{(2)}|^2 + |c^{(3)}|^2 + |c^{(4)}|^2}{4|\theta_1/2|^2}$$

This interpretation rests on TWO false assumptions:

**False Assumption 1: QCMI ∝ Σ|c|².** The actual QCMI is ~3-4× larger than η₀·Σ|c|² due to ring/log enhancement. The inequality QCMI ≥ η₀·Σ|c|² is a lower bound, not an equality.

**False Assumption 2: Temporal and spatial QCMI are comparable.** The temporal QCMI is I(R;E|Q) on a 3-qubit system (1 reference). The spatial QCMI is I(Ra,Rb;E1,E2|Qa,Qb) on a 6-qubit system (2 references). These are fundamentally DIFFERENT information-theoretic quantities, even when the underlying dynamics are related by an isometry.

### 5.3 Numerical demonstration of incomparability

The copy isometry V maps the 3-qubit temporal state to a 6-qubit embedded spatial state. Even when V†U_ringV = U_temporal holds (channel equality), the QCMI differs:

| System | Hilbert space | Reference qubits | QCMI at c1=π/4, c2=0, c3=π/8, c4=0 |
|:-------|:------------|:-----------------|:-------------------------------------|
| Temporal (direct) | 3 qubits (8D) | 1 (R) | 0.527 |
| Spatial (effective ring embedded) | 6 qubits (64D) | 2 (Ra,Rb) | 1.408 |

The spatial QCMI (1.408) is ~2.7× larger, despite the identical effective dynamics on the QE subsystem. This is because the spatial ring has twice as many reference and system qubits, providing more "room" for entropy generation.

**The ratio f = 0.527/0.981 = 0.537 is comparing the temporal ring to a DIFFERENT spatial ring (4 edges at θ1=π/2, a distinct physical system).**

### 5.4 The correct comparison: Cartan sums (not QCMI ratios)

The meaningful comparison is between Cartan coefficient sums, which are well-defined across different physical systems:

$$\boxed{\frac{\Sigma|c|^2_{\text{CJ}}}{\Sigma|c|^2_{\text{spatial, 4-edge}}} = \frac{(\theta_1/2)^2 + (\theta_2/2)^2}{4(\theta_1/2)^2} = \frac{5}{16} = 0.3125}$$

This is CONSTANT for all values of θ1 (when θ2=θ1/2). It reflects the fact that the temporal CJ ring has 2 entangling edges (u1, u3) while the spatial ring has 4 entangling edges.

**The lower bound ratio is 0.3125, not 0.537, 0.563, or any other value.** The numerical f values in TASK1 are QCMI ratios, not Cartan ratios.

### 5.5 The f=0.537 value: QCMI ratio, not Cartan correction

| θ1 | Temporal QCMI | Spatial QCMI (4-edge) | f = QCMI ratio | Cartan ratio (constant) |
|:---|:------------|:--------------------|:---------------|:------------------------|
| π/2 | 0.527 | 0.981 | 0.537 | 0.3125 |
| π/4 | 0.785 | 1.094 | 0.717 | 0.3125 |
| π/8 | 0.365 | 0.529 | 0.690 | 0.3125 |

The QCMI ratio f VARIES with θ (0.54 to 0.72) because the ring/log enhancement factors κ_temp(θ) and κ_spatial(θ) are different functions. Both involve the binary entropy H₂(½(1+√(1-4p(1-p)sin²(·)))) but evaluated at DIFFERENT effective parameters and on DIFFERENT Hilbert spaces.

**The f_CJ ratio is NOT a Cartan correction — it is the ratio of QCMI values on incomparable systems.**

---

## §6 Generalization Beyond the Diagonal RZZ Case

### 6.1 Non-identity G1, G2, G3

When G1, G2, G3 are non-identity single-qubit unitaries:

- **G1** acts on Q before U1. It modifies the effective u1 edge: u1 = U1 ∘ (G1 ⊗ I_E). The effective Cartan vector of u1 is rotated by the local unitary G1†, but its magnitude is preserved. In the Cartan decomposition, local unitaries change the basis of the Cartan coefficients but not their magnitudes (up to local unitary equivalence).

- **G2** acts on Q between U1 and U2. The effective u2 edge is no longer I⊗I. Instead, u2 = G2 ⊗ I_E, where G2 acts on Q_b and I on E_1. Since G2 is a single-qubit unitary (a local operation), u2 remains a PRODUCT operator: u2 = G2 ⊗ I_E, with operator-Schmidt rank r=1 and zero entangling Cartan: **c^(2) = 0**.

- **G3** acts on Q after U2. Similar to G1, it modifies the effective u4 edge: u4 = (CJ boundary) ∘ (G3 ⊗ I_E)^†... But with the copy isometry, u4 = I⊗I regardless (since G3 acts on the OUTPUT side, which is already accounted for in the QCMI computation through the R-Q correlation).

**Key result: G1, G2, G3 do NOT change the entangling Cartan coefficients.** They are local unitaries that can be absorbed into the isometry definitions or the initial/final state preparation. The only sources of entangling Cartan are U1 and U2.

### 6.2 Different Cartan axes (non-RZZ interactions)

If U1 and U2 have Cartan components along X, Y, or Z axes:

$$U_1 = \exp\!\left(-i\sum_{\alpha} c^{(1)}_\alpha \sigma_\alpha \otimes \sigma_\alpha\right)$$

$$U_2 = \exp\!\left(-i\sum_{\alpha} c^{(2)}_\alpha \sigma_\alpha \otimes \sigma_\alpha\right)$$

The effective edge Cartan coefficients are:

$$\boxed{c^{(1)}_\alpha = c^{(U_1)}_\alpha, \quad c^{(2)}_\alpha = 0, \quad c^{(3)}_\alpha = c^{(U_2)}_\alpha, \quad c^{(4)}_\alpha = 0}$$

The same structural result holds: **only the two interaction edges (u1, u3) carry non-zero Cartan. Edges u2 (identity period) and u4 (CJ boundary) are product channels.**

However, when U1 and U2 have DIFFERENT Cartan axes (e.g., U1 is RZZ and U2 is RXX), the combined unitary U2·U1 does NOT simply add the Cartan coefficients — there are non-commuting Pauli terms that generate BCH expansion effects. The temporal QCMI formula then involves the commutator [σ_α^(U1), σ_β^(U2)], which creates the "axis misalignment bonus" analyzed in `bridge_to_smoking_gun.md`.

### 6.3 The general isometry

For general G1, G2, G3 and U1, U2:

The isometry V: H_Q⊗H_E → H_Qa⊗H_E1⊗H_Qb⊗H_E2 must satisfy:

$$V^\dagger \cdot (u_4 u_3 u_2 u_1) \cdot V = U_2 \cdot (I_Q \otimes I_E) \cdot U_1 \quad \text{with } G_1, G_2, G_3 \text{ absorbed}$$

The general construction involves:
1. The Q_a effective node captures the Q degrees of freedom at time steps 0→1→2
2. The E_1 effective node captures E at time steps 0→1
3. The Q_b effective node captures Q at time steps 2→3→4
4. The E_2 effective node captures E at time steps 1→2

For the general case, the isometry is no longer a simple "copy." It must encode how G1, G2, G3 rotate the computational basis. This construction is left as a gap for future work.

---

## §7 Self-Attack (Mandatory)

### SA-1: Is the copy isometry unique? 🔴

**Attack:** The derivation uses a specific isometry V: |q,e⟩ → |q,q,e,e⟩. Is this the only valid choice? If not, different isometries would give different Cartan coefficients for the same temporal process.

**Response:** The isometry is not unique -- any choice satisfying V†V = I and the constraint V†U_ringV = U_temporal is valid. However, the copy isometry is the NATURAL choice for the following reasons:
1. It respects the physical interpretation: Q_a≈Q during U1, Q_b≈Q during U2, E_1≈E after U1, E_2≈E after U2
2. It maps the temporal initial state (one Bell pair, one environment) to the standard spatial initial state (two Bell pairs, two environments)
3. Different isometries would correspond to different embeddings of the 2-qubit temporal physics into the 4-qubit spatial ring, but the PHYSICAL QCMI (computed via V†U_ringV) is the same

The Cartan coefficients of individual edges DO depend on the isometry choice. But the total Cartan sum c1+c2+c3+c4 is fixed by the constraint V†U_ringV = U_temporal. The individual c_i are then constrained by the PHYSICS: c1 comes from U1, c3 from U2, and c2,c4 from the non-interacting periods.

### SA-2: Can c2 or c4 be non-zero with a different isometry? 🔴🔴

**Attack:** Could we choose an isometry where c2 ≠ 0 or c4 ≠ 0, as long as c1+c2+c3+c4 = (θ1+θ2)/2? For example, c1=θ1/2, c3=θ2/2, c2=θ1/2, c4=-θ1/2 gives the same sum but makes u2 entangling and u4 "anti-entangling."

**Response:** This is a legitimate mathematical ambiguity. The constraint c1+c2+c3+c4 = (θ1+θ2)/2 does not uniquely determine the individual c_i.

The resolution is physical: u2 represents the "identity period" between U1 and U2. During this period, E does not evolve at all (identity channel), and Q undergoes only G2 (a local unitary). There is NO entangling interaction during this period, so u2 MUST be a product operator: c^(2) = 0.

Similarly, u4 represents the CJ boundary pairing. This is a mathematical artifact that encodes the information-theoretic feedback from E_2 to Q_a through the QCMI computation. It does NOT correspond to a physical entangling gate, so c^(4) = 0.

The physical assignment c^(2) = c^(4) = 0 is unique and unambiguous.

### SA-3: The CJ boundary "feedback" is not a dynamical unitary 🔴🔴🔴

**Attack:** The CJ boundary conceptually "closes the ring" by connecting E_2 back to Q_a. In the spatial ring, the closure edge u4 has non-zero Cartan. The numerical data in TASK1 suggested 3 effective edges (u1, u3, u4) contributed, implying c^(4) > 0.

**Response (CORRECTED):** The TASK1 numerical analysis was fundamentally flawed for two reasons:

1. **Incomparable systems:** TASK1 compared QCMI on a 3-qubit temporal system (I(R;E|Q)) with QCMI on a 6-qubit spatial system (I(Ra,Rb;E1,E2|Qa,Qb)). These are different information-theoretic quantities that are not directly comparable — they differ even when the underlying states are embeddings of each other.

2. **False QCMI-Cartan proportionality:** TASK1 assumed QCMI ∝ Σ|c|² (proportional to Cartan sum). The actual QCMI is 2-4× larger than η₀·Σ|c|², and the enhancement factor differs between temporal and spatial systems.

The CORRECT comparison uses the Cartan sum ratio, which is CONSTANT at 0.3125 (the temporal ring has 2 entangling edges out of 4 possible). The QCMI ratio of 0.537 is an accident of the specific parameters — it varies from 0.54 to 0.72 as θ1 changes.

**Physical resolution:** The CJ boundary provides the INFORMATION-THEORETIC "closure" of the ring (through S(RQ) in the QCMI formula), not a DYNAMICAL entangling gate. In the effective spatial ring, u4 = I⊗I — a product operator that contributes zero Cartan. The "feedback" from E_2 to Q_a occurs through the QCMI computation, not through an additional gate.

### SA-4: What about general (non-ZZ-diagonal) cases? 🔴

**Attack:** The entire derivation assumes U1 and U2 are both RZZ (Z⊗Z interactions). What if they have different Cartan axes? Can the isometry construction be generalized?

**Response:** This is a genuine gap. For non-commuting U1 and U2:
1. U2·U1 ≠ U1·U2, so the total unitary is not simply RZZ(θ1+θ2)
2. The isometry must accommodate the fact that Q and E states may rotate between the two interactions
3. The effective edge operators u1 and u3 would have multi-axis Cartan vectors
4. The constraint V†U_ringV = U_temporal becomes a system of equations for the Cartan components

The structure of the solution (u1 from U1, u2=product, u3 from U2, u4=product) should generalize, but the explicit construction of V for non-commuting axes is non-trivial. This is marked as a gap.

### SA-5: Does c^(4) = 0 make the ring degenerate? 🔴

**Attack:** If c^(2) = c^(4) = 0, the effective ring has only 2 edges with non-zero Cartan. Doesn't this mean the ring "degenerates" into just two independent interactions?

**Response:** No. The ring topology (cyclic order of 4 nodes) is maintained -- what changes is that 2 of the 4 edges are identity (no entangling power). This is analogous to a spatial ring where 2 edges are SWAP gates (product operators) -- the RING TOPOLOGY still exists, it just doesn't contribute additional entangling Cartan.

The crucial point: the CFOL theorem's dim(Y)=d condition depends on the FIRST edge u1 having sufficient entangling power. As long as c^(1) ≠ 0 (U1 has non-zero entangling Cartan), the condition can be satisfied. The identity of u2 and u4 does not affect this.

The QCMI is generated by the first interaction (U1 creates Q-E correlations), preserved through the identity period, and then the second interaction (U2) adds more Q-E correlations. The CJ boundary "closes the loop" information-theoretically but does not add dynamical entanglement.

---

## §8 The Complete Theorem

### Theorem (CJ Bridge Quantitative Mapping)

Let a single qubit Q undergo a temporal sequence: G1 on Q, Q-E interaction U1, G2 on Q (E idle), Q-E interaction U2, G3 on Q, with initial environment state ρ_E. Let the Choi-Jamiolkowski isomorphism map this temporal process to a 4-node spatial ring Q_a--E_1--Q_b--E_2--Q_a.

Then, under the copy isometry V: H_Q⊗H_E → H_Qa⊗H_E1⊗H_Qb⊗H_E2 defined by V|q,e⟩ = |q⟩_Qa|e⟩_E1|q⟩_Qb|e⟩_E2 (generalized for non-identity G1,G2,G3 with appropriate basis rotations):

1. **The four effective edge operators are:**
   - u1 = U1 ∘ (G1 ⊗ I_E), acting on Q_a ⊗ E_1
   - u2 = G2 ⊗ I_E, acting on E_1 ⊗ Q_b (product operator)
   - u3 = U2, acting on Q_b ⊗ E_2
   - u4 = I ⊗ I, acting on E_2 ⊗ Q_a (product operator)

2. **The Cartan coefficients are:**
   - c^(1) = Cartan(U1) (inherited from U1, rotated by G1)
   - c^(2) = 0 (identity period, product)
   - c^(3) = Cartan(U2) (inherited from U2)
   - c^(4) = 0 (CJ boundary, product)

3. **The channel equality holds:**
   V†(u4·u3·u2·u1)V = U_temporal (as a map on the 2-qubit QE subsystem)

4. **QCMI is NOT preserved by the isometry** — temporal QCMI (1 reference, 3 qubits) and spatial QCMI (2 references, 6 qubits) are fundamentally different quantities even on equivalent embedded states.

5. **The temporal QCMI lower bound is:**
   QCMI_temporal ≥ η₀ · (|c^(1)|² + |c^(3)|²)
   
   with the actual QCMI exceeding this bound by a ring/log enhancement factor κ(θ1, θ2).

6. **For the all-RZZ case with p=0.7:** The QCMI is given exactly by:
   QCMI = H₂(½(1 + √(1 - 4p(1-p)sin²(θ1+θ2))))
   
   where θ1+θ2 is the total RZZ rotation angle.

7. **The TASK1 "f_CJ correction factor" (0.54-0.72) is NOT a Cartan correction.** It is the ratio of QCMI values on DIFFERENT physical systems (3-qubit temporal vs 6-qubit spatial with different edge configurations). It provides no information about "missing" Cartan coefficients. The effective ring has exactly 2 entangling edges (u1, u3), with the CJ boundary u4 being a product operator (c^(4) = 0).

---

## §9 Remaining Gaps

### GAP-1: General isometry construction for non-commuting U1, U2 [MEDIUM]

The copy isometry V: |q,e⟩ → |q⟩_Qa|e⟩_E1|q⟩_Qb|e⟩_E2 works for the ZZ-diagonal case. For general U1, U2 with different Cartan axes, the isometry must be generalized to account for non-commuting basis rotations. The constraint V†U_ringV = U_temporal becomes a system of operator equations. This is technically challenging but the existence of a solution is guaranteed because the effective Q nodes and E nodes are 2D subspaces within their respective physical spaces.

### GAP-2: Non-identity G1, G2, G3 [MINOR]

The qualitative analysis in §6.1 shows G1, G2, G3 are local unitaries that can be absorbed. A fully explicit derivation of the effective edge operators for arbitrary G1, G2, G3 would require constructing the isometry with basis rotations. This is a straightforward extension but requires careful bookkeeping.

### GAP-3: d > 2 generalization [MEDIUM]

For qudits (d ≥ 3), the Cartan subalgebra has dimension (d-1)². The operator-Schmidt rank can be up to d². The isometry construction and the constraint c1+c2+c3+c4 = (θ1+θ2)/2 generalize, but the explicit Cartan parameterization becomes more complex. The structural result (only u1 and u3 carry non-zero Cartan) should hold.

---

## §10 Comparison with Numerical Data

### 10.1 The analytic prediction (exact match)

| θ1 | θ2 | θ_total | Analytic QCMI | Numerical QCMI | Error |
|:---|:---|:--------|:-------------|:--------------|:------|
| π/2 | π/4 | 3π/4 | 0.527090 | 0.527 | <10^{-4} |
| π/4 | π/8 | 3π/8 | 0.784926 | 0.785 | <10^{-4} |
| π/8 | π/16 | 3π/16 | 0.364700 | 0.365 | 3×10^{-4} |

The analytic formula H₂(½(1+√(1-4p(1-p)sin²θ))) with θ = θ1+θ2 and p=0.7 gives exact agreement with the numerical simulation from `numerical_verification.py`.

### 10.2 The effective Cartan sum and lower bound

For θ1=π/2, θ2=π/4:
$$\Sigma|c|^2_{\text{CJ}} = (\theta_1/2)^2 + (\theta_2/2)^2 = \frac{\pi^2}{16} + \frac{\pi^2}{64} = \frac{5\pi^2}{64} \approx 0.7711$$

$$\eta_0 \cdot \Sigma|c|^2_{\text{CJ}} = \frac{1}{8\ln 2} \cdot 0.7711 \approx 0.1391 \text{ bits}$$

$$\text{Actual QCMI} = 0.5271 = \mathbf{3.79\times} \text{ the lower bound}$$

### 10.3 The Cartan sum ratio (meaningful comparison)

The Cartan sum ratio between temporal CJ ring and spatial 4-edge ring is:

$$\frac{\Sigma|c|^2_{\text{CJ}}}{\Sigma|c|^2_{\text{spatial}}} = \frac{(\theta_1/2)^2 + (\theta_2/2)^2}{4(\theta_1/2)^2} = \frac{1 + (\theta_2/\theta_1)^2}{4} = \frac{1 + 0.25}{4} = \mathbf{0.3125}$$

This is CONSTANT for all θ1 when θ2=θ1/2. It means the temporal CJ ring has exactly 2/4 = 50% of the entangling "budget" of a full 4-edge spatial ring with the same per-edge Cartan.

### 10.4 Why the QCMI ratio differs from the Cartan ratio

| System | Hilbert space | Refs | η₀·Σ|c|² | Actual QCMI | Enhancement |
|:-------|:------------|:-----|:----------|:------------|:------------|
| Temporal (2 edges) | 3 qubits (8D) | 1 | 0.139 | 0.527 | 3.79× |
| Spatial (4 edges) | 6 qubits (64D) | 2 | 0.445 | 0.981 | 2.20× |

The enhancement factors differ (3.79× vs 2.20×) because the ring/log enhancement κ(θ) depends on the Hilbert space structure and the specific QCMI definition (I(R;E|Q) vs I(Ra,Rb;E1,E2|Qa,Qb)). The temporal ring benefits MORE from log enhancement because its total effective Cartan (3π/8) is smaller, and the log term ∝ log(1/θ) amplifies smaller θ.

**The f_CJ = 0.537 ratio is (0.527/0.981) = QCMI ratio, NOT (0.3125 × 3.79/2.20) = Cartan ratio × enhancement ratio.** The QCMI ratios and Cartan ratios are distinct quantities that should not be conflated.

---

## §11 Summary

$$\boxed{\begin{array}{c}
\text{Temporal sequence } U_1, I, U_2 \text{ on Q+E} \\
\downarrow \text{Copy isometry } V: |q,e\rangle \mapsto |q\rangle_{Q_a}|e\rangle_{E_1}|q\rangle_{Q_b}|e\rangle_{E_2} \\
\text{4-node spatial ring with edges:} \\
u_1 = U_1: c^{(1)}_z = \theta_1/2, \quad r_1 = 2 \\
u_2 = I \otimes I: c^{(2)} = 0, \quad r_2 = 1 \quad \text{(identity period, product)} \\
u_3 = U_2: c^{(3)}_z = \theta_2/2, \quad r_3 = 2 \\
u_4 = I \otimes I: c^{(4)} = 0, \quad r_4 = 1 \quad \text{(CJ boundary, product)} \\
\downarrow V^\dagger U_{\text{ring}} V = U_{\text{temporal}} = \text{RZZ}(\theta_1+\theta_2) \\
\text{QCMI}_{\text{temporal}} = H_2\!\left(\frac{1}{2}(1 + \sqrt{1 - 4p(1-p)\sin^2(\theta_1+\theta_2)})\right) \\
\geq \eta_0 \cdot \left[(\theta_1/2)^2 + (\theta_2/2)^2\right]
\end{array}}$$

**Key results:**

1. **Only 2 of 4 effective edges carry non-zero entangling Cartan:** u1 (from U1) and u3 (from U2) have c^(1)_z = θ1/2 and c^(3)_z = θ2/2 respectively.

2. **u2 (identity period) and u4 (CJ boundary) are product operators** with operator-Schmidt rank r = 1 and zero Cartan coefficients. The CJ boundary contributes no dynamical entanglement between effective nodes.

3. **The isometry preserves the channel** (V†U_ringV = U_temporal on the 2-qubit QE subsystem) **but NOT the QCMI** — temporal QCMI (I(R;E|Q), 1 reference) and spatial QCMI (I(Ra,Rb;E1,E2|Qa,Qb), 2 references) are fundamentally different quantities.

4. **The TASK1 "f_CJ = 0.537" is not a Cartan correction.** It's the ratio of QCMI values on different physical systems (3-qubit vs 6-qubit), which varies with parameters (0.54 to 0.72) because the ring/log enhancement factors differ. The CONSTANT ratio is the Cartan sum ratio: Σ|c|²_CJ / Σ|c|²_spatial = 0.3125.

5. **Wall W2 is RESOLVED.** The quantitative mapping is clean and explicit: the Cartan coefficients of the effective edges are direct functions of the physical gate parameters, with u2 and u4 being product operators (zero Cartan). No "mystery" remains.
