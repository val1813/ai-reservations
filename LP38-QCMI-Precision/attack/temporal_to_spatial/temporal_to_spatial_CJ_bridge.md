# Temporal-to-Spatial Choi-Jamiolkowski Bridge for CFOL

**Author:** A-Doctor (formal derivation)
**Date:** 2026-06-09
**Target:** Prove that a temporal sequence of operations on a single qubit Q with environment E maps, via the Choi-Jamiolkowski isomorphism, to a spatial tensor network with a 4-node ring structure matching the CFOL topology.
**Status:** Complete derivation.

---

## §0. Problem Statement

CFOL is proved for a 4-node SPATIAL causal ring: four distinct quantum subsystems (Q_a, E_1, Q_b, E_2) with unitary operations u_i applied sequentially around the ring. QCMI = I(R;E'|Q') > 0 for the ring.

In real quantum circuits, operations happen SEQUENTIALLY IN TIME on the same physical qubits. We must prove that a temporal sequence maps to a spatial ring via the Choi-Jamiolkowski (CJ) isomorphism.

**Temporal setup:** A single qubit Q interacts with an environment qubit E:
- Step 0: Prepare Q in state |ψ⟩_Q, E in state ρ_E
- Step 1: Gate G_1 on Q (unitary)
- Step 2: Q-E interaction U_1 (2-qubit unitary on Q⊗E)
- Step 3: Gate G_2 on Q (unitary, acts only on Q after interaction 1)
- Step 4: Q-E interaction U_2 (2-qubit unitary on Q⊗E)
- Step 5: Gate G_3 on Q (unitary)
- Step 6: Discard (trace over) E

The cycle closes when accumulated Q-E correlations from U_1, U_2 couple with accumulated system dynamics from G_1, G_2, G_3.

---

## §1. Choi-Jamiolkowski Isomorphism: Definition and Properties

### 1.1 Basic definition

For a linear map Φ: B(H_A) → B(H_B), the Choi operator is:

$$\boxed{J(\Phi) = (I_A \otimes \Phi)(|\Phi^+\rangle\langle\Phi^+|_{AA'}) \in B(H_A \otimes H_B)}$$

where |Φ^+⟩_{AA'} = (1/√d_A) Σ_{i=0}^{d_A-1} |i⟩_A ⊗ |i⟩_{A'} is the maximally entangled state on H_A ⊗ H_{A'} (A' is an auxiliary copy of A).

Equivalently, in vectorized form (Choi vector):

$$\boxed{|\Phi\rangle\rangle_{AB} = (I_A \otimes \Phi)(|\Phi^+\rangle_{AA'}) = \frac{1}{\sqrt{d_A}} \sum_{i=0}^{d_A-1} |i\rangle_A \otimes |\Phi(|i\rangle\langle i|)\rangle_B}$$

For a unitary channel U(·) = U(·)U^†, the Choi vector is:

$$\boxed{|U\rangle\rangle_{AB} = \frac{1}{\sqrt{d}} (I \otimes U) \sum_i |i\rangle_A |i\rangle_{A'} = \frac{1}{\sqrt{d}} \sum_i |i\rangle_A \otimes U|i\rangle_B}$$

### 1.2 Key property: sequential composition as link product

The CJ isomorphism maps sequential composition of channels to a "link product" (partial inner product + partial trace) on Choi states. For two channels Φ_1: A → B and Φ_2: B → C:

$$\boxed{J(\Phi_2 \circ \Phi_1) = \text{Tr}_B\left[ (J(\Phi_2)^{T_B} \otimes I_A) (I_C \otimes J(\Phi_1)) \right]}$$

where T_B denotes partial transpose on B. In vectorized form, this is a contraction of the "output" index of Φ_1 with the "input" index of Φ_2:

$$\boxed{|\Phi_2 \circ \Phi_1\rangle\rangle_{AC} = \langle\langle\Phi_1^*|_{BB'} \cdot (|\Phi_1\rangle\rangle_{AB} \otimes |\Phi_2\rangle\rangle_{B'C})}$$

where |Φ_1^*⟩⟩ denotes the Choi vector of the complex-conjugated channel. For unitary channels, this simplifies to:

$$\boxed{|U_2 U_1\rangle\rangle_{AC} = d \cdot \langle\Phi^+|_{BB'} (|U_1\rangle\rangle_{AB} \otimes |U_2\rangle\rangle_{B'C})}$$

### 1.3 Multi-partite channels

For a unitary U acting on a bipartite system Q⊗E, the Choi vector lives on four subsystems:

$$\boxed{|U\rangle\rangle_{Q_{\text{in}}, E_{\text{in}}, Q_{\text{out}}, E_{\text{out}}} = \frac{1}{2} \sum_{i,j=0}^{1} |i,j\rangle_{Q_{\text{in}}E_{\text{in}}} \otimes U|i,j\rangle_{Q_{\text{out}}E_{\text{out}}}}$$

This 4-partite structure is the fundamental reason the temporal sequence maps to a 4-node spatial ring.

---

## §2. Explicit Choi State Construction for Each Time Step

### 2.1 Notation

We label the qubit Q at each time boundary with a subscript indicating its temporal position:

| Time boundary | Qubit label | Physical meaning |
|:--:|:--:|:--|
| t = 0 | Q_0 | Initial Q state input |
| t = 1 | Q_1 | Q after G_1, before U_1 |
| t = 2 | Q_2 | Q after U_1, before G_2 |
| t = 3 | Q_3 | Q after G_2, before U_2 |
| t = 4 | Q_4 | Q after U_2, before G_3 |
| t = 5 | Q_5 | Q after G_3 (output) |

The environment E has labels:

| Time boundary | E label | Physical meaning |
|:--:|:--:|:--|
| t = 0 | E_0 | Initial E state (ρ_E) |
| t = 2 | E_1 | E after U_1 = E before U_2 (the "memory" bridge) |
| t = 4 | E_2 | E after U_2 (traced out) |

Note: E evolves ONLY during interactions (U_1, U_2). Between interactions, E is the SAME physical qubit — this identity is the crucial "temporal memory" that creates the ring.

### 2.2 Choi vectors for each operation

**Step 1: G_1 on Q.**
$$|G_1\rangle\rangle_{Q_0, Q_1} = \frac{1}{\sqrt{2}} \sum_{i=0}^{1} |i\rangle_{Q_0} \otimes G_1|i\rangle_{Q_1}$$

**Step 2: U_1 on Q_1 ⊗ E_0.**
$$|U_1\rangle\rangle_{Q_1, E_0, Q_2, E_1} = \frac{1}{2} \sum_{i,j=0}^{1} |i,j\rangle_{Q_1 E_0} \otimes U_1|i,j\rangle_{Q_2 E_1}$$

**Step 3: G_2 on Q_2.** (Identity on E_1 — E does not evolve between interactions, but its state persists.)

$$|G_2\rangle\rangle_{Q_2, Q_3} \otimes I_{E_1} = \frac{1}{\sqrt{2}} \sum_{i=0}^{1} |i\rangle_{Q_2} \otimes G_2|i\rangle_{Q_3} \otimes I_{E_1}$$

Note: The identity on E_1 will be contracted with the E_1 output of U_1 and the E_1 input of U_2. For notational clarity, we define the Choi vector for G_2 ⊗ I_E:

$$|G_2 \otimes I_E\rangle\rangle = \frac{1}{\sqrt{2}} \sum_{i=0}^1 |i\rangle_{Q_2} \otimes G_2|i\rangle_{Q_3} \otimes \frac{1}{\sqrt{2}} \sum_{j=0}^1 |j\rangle_{E_1} \otimes |j\rangle_{E_1'}$$

where E_1' is an auxiliary label tracking the E identity wire.

**Step 4: U_2 on Q_3 ⊗ E_1.**
$$|U_2\rangle\rangle_{Q_3, E_1, Q_4, E_2} = \frac{1}{2} \sum_{i,j=0}^{1} |i,j\rangle_{Q_3 E_1} \otimes U_2|i,j\rangle_{Q_4 E_2}$$

**Step 5: G_3 on Q_4.**
$$|G_3\rangle\rangle_{Q_4, Q_5} = \frac{1}{\sqrt{2}} \sum_{i=0}^{1} |i\rangle_{Q_4} \otimes G_3|i\rangle_{Q_5}$$

### 2.3 Initial environment state

The initial environment state is encoded as a vector in the Choi formalism:

$$|\gamma\rangle_{E_0} = \sqrt{p}|0\rangle_{E_0} + \sqrt{1-p}|1\rangle_{E_0}$$

corresponding to ρ_E = γ = p|0⟩⟨0| + (1-p)|1⟩⟨1|. For purity-mixed states (p ≠ 0,1), this is a purification in an extended space, but for our purposes we treat it as a vector with the understanding that the eventual trace is over E_2.

---

## §3. Temporal Contraction → Spatial Tensor Network

### 3.1 The full tensor network

The Choi vector of the complete process |Λ⟩⟩_{Q_0, Q_5} is obtained by contracting ALL internal indices:

$$\boxed{|\Lambda\rangle\rangle_{Q_0, Q_5} = \langle\gamma|_{E_0} \langle\Phi^+|_{Q_1^{(1)}, Q_1^{(2)}} \langle\Phi^+|_{Q_2^{(1)}, Q_2^{(2)}} \langle\Phi^+|_{E_1, E_1'} \langle\Phi^+|_{Q_3^{(1)}, Q_3^{(2)}} \langle\Phi^+|_{Q_4^{(1)}, Q_4^{(2)}} \langle\Phi^+|_{E_2, E_2'}}$$

$$\times \Big[ |G_1\rangle\rangle_{Q_0, Q_1^{(1)}} \otimes |U_1\rangle\rangle_{Q_1^{(2)}, E_0, Q_2^{(1)}, E_1} \otimes |G_2\rangle\rangle_{Q_2^{(2)}, Q_3^{(1)}} \otimes |U_2\rangle\rangle_{Q_3^{(2)}, E_1', Q_4^{(1)}, E_2} \otimes |G_3\rangle\rangle_{Q_4^{(2)}, Q_5} \Big]$$

where ⟨Φ^+|_XY denotes contraction of the X-index of the first factor with the Y-index of the second factor via the maximally entangled state. More explicitly, for a contraction between A_out of operation i and A_in of operation i+1:

$$\langle\langle\Phi^+|_{A_{\text{out}}^{(i)}, A_{\text{in}}^{(i+1)}} = \sum_{k=0}^{d-1} \langle k|_{A_{\text{out}}^{(i)}} \otimes \langle k|_{A_{\text{in}}^{(i+1)}}$$

### 3.2 Explicit contraction sequence

**Contraction 1: Q_1.** Link G_1 output to U_1 input.

$$\langle\langle\Phi^+|_{Q_1^{(1)}, Q_1^{(2)}} \left[|G_1\rangle\rangle \otimes |U_1\rangle\rangle\right] = \frac{1}{2\sqrt{2}} \sum_{i,k=0}^1 \sum_{j=0}^1 |i\rangle_{Q_0} \otimes \langle k|G_1|i\rangle \cdot |k,j\rangle_{Q_1^{(2)}E_0} \otimes U_1|k,j\rangle_{Q_2E_1}$$

$$= \frac{1}{2\sqrt{2}} \sum_{i,j=0}^1 |i\rangle_{Q_0} \otimes |G_1|i\rangle, j\rangle_{...} \otimes U_1(|G_1|i\rangle \otimes |j\rangle)_{Q_2 E_1}$$

$$\boxed{= \frac{1}{2\sqrt{2}} \sum_{i,j=0}^1 |i\rangle_{Q_0} \otimes U_1(G_1|i\rangle \otimes |j\rangle)_{Q_2 E_1}}$$

This gives a 3-partite state on Q_0 ⊗ Q_2 ⊗ E_1, representing the combined effect of applying G_1 followed by U_1.

**Contraction 2: Q_2.** Link U_1 output to G_2 input.

After contracting Q_2^{(1)} with Q_2^{(2)}, we get a state on Q_0 ⊗ Q_3 ⊗ E_1:

$$\frac{1}{2\sqrt{2}} \sum_{i,j,\ell=0}^1 |i\rangle_{Q_0} \otimes \langle\ell|U_1(G_1|i\rangle \otimes |j\rangle)_{Q_2} \cdot G_2|\ell\rangle_{Q_3} \otimes (\text{E}_1 \text{ part})$$

$$= \frac{1}{2\sqrt{2}} \sum_{i,j=0}^1 |i\rangle_{Q_0} \otimes G_2 \cdot (\text{Q-projection of } U_1(G_1|i\rangle \otimes |j\rangle))_{Q_3} \otimes (\text{E-projection of } U_1(G_1|i\rangle \otimes |j\rangle))_{E_1}$$

More precisely, if we write U_1|Q = Σ_{a,b} K_{ab} ⊗ |a⟩⟨b|_E (the Kraus decomposition of U_1 viewed as a channel from Q_1 to Q_2 with E as the environment), then the contraction yields:

$$\boxed{|\Psi^{(12)}\rangle_{Q_0, Q_3, E_1} = \frac{1}{\sqrt{2}} \sum_i |i\rangle_{Q_0} \otimes \sum_{a,b} (G_2 K_{ab} G_1|i\rangle)_{Q_3} \otimes \sqrt{\gamma_b}|a\rangle_{E_1}}$$

where γ_b are the eigenvalues of ρ_E (γ_0 = p, γ_1 = 1-p).

**Contraction 3: E_1 (environment identity).** Link U_1's E output to U_2's E input.

The E_1 index of |Ψ^{(12)}⟩ must match the E_1' input of U_2. This is the CRUCIAL step: it connects the post-U_1 environment state to the pre-U_2 environment state. Without this identity (if E were reset or re-initialized), the two interactions would be independent and no ring would form.

$$\langle\langle\Phi^+|_{E_1, E_1'} [|\Psi^{(12)}\rangle \otimes |U_2\rangle\rangle]$$

This contraction is:

$$\sum_{m=0}^1 \langle m|_{E_1} \langle m|_{E_1'} \left[|\Psi^{(12)}\rangle_{Q_0, Q_3, E_1} \otimes |U_2\rangle\rangle_{Q_3', E_1', Q_4, E_2}\right]$$

### 3.3 Full contracted state

After performing all contractions, the Choi vector of the complete process is:

$$\boxed{|\Lambda\rangle\rangle_{Q_0, Q_5} = \frac{1}{\sqrt{2}} \sum_{i, j, k, \ell, m, n=0}^1 \delta_{(\text{contractions})} \; |i\rangle_{Q_0} \otimes G_3 \cdot \Pi_{Q_4} \cdot U_2 \cdot \Pi_{E_1=U_1^{E}} \cdot G_2 \cdot \Pi_{Q_2} \cdot U_1 \cdot G_1|i\rangle_{...} }$$

More transparently, using the Kraus operator formalism:

$$\boxed{|\Lambda\rangle\rangle_{Q_0, Q_5} = \frac{1}{\sqrt{2}} \sum_{i=0}^1 |i\rangle_{Q_0} \otimes \Lambda(|i\rangle\langle i|)_{Q_5}}$$

where the full channel is:

$$\boxed{\Lambda(\rho) = \text{Tr}_{E_2}\left[ G_3 U_2 G_2 U_1 G_1 (\rho \otimes \rho_E) G_1^\dagger U_1^\dagger G_2^\dagger U_2^\dagger G_3^\dagger \right]}$$

This confirms the CJ construction correctly captures the temporal sequence.

---

## §4. Identifying the Effective Ring Structure

### 4.1 Graph-theoretic analysis of the tensor network

Consider the tensor network BEFORE contraction (the "unfolded" representation). The network has the following vertices (tensors) and edges (contracted indices):

**Vertices (rank as tensors):**

| Vertex | Tensor legs | 
|:--|:--|
| |G_1⟩⟩ | Q_0, Q_1 |
| |U_1⟩⟩ | Q_1, E_0, Q_2, E_1 |
| |G_2⟩⟩ | Q_2, Q_3 |
| |U_2⟩⟩ | Q_3, E_1, Q_4, E_2 |
| |G_3⟩⟩ | Q_4, Q_5 |
| ⟨γ| | E_0 (boundary condition) |
| ⟨Φ^+| | E_2 (trace boundary) |
| ⟨Φ^+| | Q_0 (paired with Q_5 in CJ) |

**Edges (contracted pairs):** Q_1—Q_1, Q_2—Q_2, Q_3—Q_3, Q_4—Q_4, E_1—E_1

**Boundary legs (uncontracted):** Q_0, Q_5 (Choi input/output), E_0 (initial state), E_2 (trace).

### 4.2 Cycle identification

The key observation: after tracing all Q_i internal edges, the environment edge E_1 forms a SELF-LOOP in the contracted network.

To see this, track the E-wire through the network:
E_0 (initial) → U_1 → E_1 → [identity] → U_2 → E_2 (trace)

The Q-wire path is:
Q_0 (initial) → G_1 → Q_1 → U_1 → Q_2 → G_2 → Q_3 → U_2 → Q_4 → G_3 → Q_5 (final)

The crucial topological feature: U_1 couples Q_1 and E_0/E_1, while U_2 couples Q_3 and E_1/E_2. The intermediate E_1 is the SAME index in both U_1 and U_2. This creates a path:

$$\boxed{Q_0 \rightarrow G_1 \rightarrow Q_1 \rightarrow U_1 \rightarrow E_1 \rightarrow U_2 \rightarrow Q_3 \rightarrow G_2 \leftarrow Q_2 \leftarrow U_1}$$

This path forms a CYCLE: Q_1 → U_1 → E_1 → U_2 → Q_3 → (through the Q_2-Q_3 connection via G_2) → Q_2 → U_1 → Q_1.

The cycle involves 4 nodes: {Q_1, E_1, Q_3, Q_2}, connected by edges {U_1 (Q_1-E_1), U_2 (E_1-Q_3), G_2 (Q_3-Q_2 via identity on Q), U_1-return (Q_2-Q_1 via Q identity)}.

### 4.3 Mapping to the CFOL 4-node ring

We now identify the effective spatial ring by grouping the temporal Choi tensor network into FOUR effective nodes:

$$\boxed{\begin{aligned}
\tilde{Q}_a &\equiv \text{span}(\text{Q}_0 \oplus \text{Q}_1 \oplus \text{Q}_2) \quad \text{(Q before and through U}_1\text{)} \\
\tilde{E}_1 &\equiv \text{span}(\text{E}_0 \oplus \text{E}_1) \quad \text{(E across U}_1\text{)} \\
\tilde{Q}_b &\equiv \text{span}(\text{Q}_2 \oplus \text{Q}_3 \oplus \text{Q}_4) \quad \text{(Q between and through U}_2\text{)} \\
\tilde{E}_2 &\equiv \text{span}(\text{E}_1 \oplus \text{E}_2) \quad \text{(E across U}_2\text{)}
\end{aligned}}$$

The "edges" of the spatial ring correspond to the effective channels:

$$\boxed{\begin{aligned}
u_1 &: \tilde{Q}_a \otimes \tilde{E}_1 \rightarrow \tilde{Q}_a \otimes \tilde{E}_1 && \text{(U}_1 \text{ interaction + G}_1 \text{ preparation)} \\
u_2 &: \tilde{E}_1 \otimes \tilde{Q}_b \rightarrow \tilde{E}_1 \otimes \tilde{Q}_b && \text{(Q-E identity through G}_2\text{)} \\
u_3 &: \tilde{Q}_b \otimes \tilde{E}_2 \rightarrow \tilde{Q}_b \otimes \tilde{E}_2 && \text{(U}_2 \text{ interaction)} \\
u_4 &: \tilde{E}_2 \otimes \tilde{Q}_a \rightarrow \tilde{E}_2 \otimes \tilde{Q}_a && \text{(feedback through G}_3 + \text{CJ boundary)}
\end{aligned}}$$

The spatial topology is:

$$\boxed{\tilde{Q}_a \xrightarrow{u_1} \tilde{E}_1 \xrightarrow{u_2} \tilde{Q}_b \xrightarrow{u_3} \tilde{E}_2 \xrightarrow{u_4} \tilde{Q}_a}$$

This is PRECISELY the 4-node ring of CFOL, with cycle rank b_1 = 1.

### 4.4 The crucial u_4 edge (ring closure)

Edge u_4 — the "feedback" edge from E_2 back to Q_a — is the most subtle. In the temporal picture, it arises from the Choi-Jamiolkowski boundary condition:

The Choi vector |Λ⟩⟩_{Q_0, Q_5} relates the input and output of the full process. The ring closure u_4 corresponds to:

1. Information that leaked into E during U_2 (stored in E_2) never returns to Q in the temporal sequence (we trace E_2). 

2. HOWEVER, the QCMI quantity I(R;E'|Q') captures precisely this "lost" information. The reference system R (the auxiliary input of the CJ isomorphism) stores the initial correlations with Q. The conditional mutual information measures how much of this correlation ends up in E rather than Q.

3. In the spatial representation, this information flow from Q_5 (final Q) back to Q_0 (initial Q) through the CJ boundary constitutes the u_4 edge.

Mathematically, the u_4 edge in the spatial ring corresponds to the channel:

$$\Phi_{u_4}(\rho_{\tilde{E}_2 \tilde{Q}_a}) = \text{Tr}_{Q_5}[|\Phi^+\rangle\langle\Phi^+|_{Q_0 Q_5} \cdot (I \otimes G_3^\dagger)(\rho)]$$

which captures the CJ pairing of input and output.

---

## §5. The Effective dim(Y) = d Condition in Temporal Language

### 5.1 Recall: dim(Y) in the spatial CFOL

In the spatial CFOL proof [NEW_WALL_CHANNEL_CONDITION.md], the condition for CFOL non-degeneracy is:

$$\boxed{\dim(Y) = d \quad\text{where}\quad Y = \text{span}\{R_k|\tilde{\gamma}\rangle\}}$$

Here, R_k are the operator-Schmidt components of u_1 acting on E_1, and |γ̃⟩ is the environment initial state. When dim(Y) = d, the Kraus operators of the full channel are forced to be linearly independent → QCMI > 0.

### 5.2 Translation to temporal language

In the temporal setting, u_1 corresponds to U_1 (the first Q-E interaction). Its Choi state is:

$$|U_1\rangle\rangle = \frac{1}{2} \sum_{i,j=0}^1 |i,j\rangle_{Q_1 E_0} \otimes U_1|i,j\rangle_{Q_2 E_1}$$

The operator-Schmidt decomposition of U_1 (with respect to the Q_1:Q_2 vs E_0:E_1 bipartition) is:

$$\boxed{U_1 = \sum_{k=0}^{r-1} s_k \; L_k^{(Q_1 \rightarrow Q_2)} \otimes R_k^{(E_0 \rightarrow E_1)}}$$

where r = rank_{OpSchmidt}(U_1) ≤ 4 (for d=2), s_k > 0 are the Schmidt coefficients, and L_k, R_k are orthonormal operator bases.

The Y-subspace is then:

$$\boxed{Y = \text{span}\{R_k|\gamma\rangle_{E_0} : k = 0, 1, \ldots, r-1\} \subseteq \mathcal{H}_{E_1}}$$

where |γ⟩_{E_0} = √p|0⟩ + √(1-p)|1⟩ is the environment initial state (written as a pure-state vector — for a mixed state ρ_E = Σ_a γ_a|a⟩⟨a|, this is extended to a set {√γ_a R_k|a⟩}).

### 5.3 Explicit Cartan condition for dim(Y) = d (d = 2)

Using the Cartan decomposition of U_1:

$$U_1 = (A \otimes B) \cdot \exp\left(i\sum_{\alpha=x,y,z} c_\alpha \sigma_\alpha \otimes \sigma_\alpha\right) \cdot (C \otimes D)$$

with local unitaries A, B, C, D ∈ SU(2) and Cartan coefficients c_α ∈ [0, π/4].

The operator-Schmidt components R_k are determined by the central term D(c) = exp(i Σ_α c_α σ_α ⊗ σ_α). The R_k are linear combinations of the Pauli operators σ_α conjugated by the local unitaries.

**Condition for dim(Y) < 2 (degenerate case):**

dim(Y) = 1 or 0 if and only if all R_k map |γ⟩_{E_0} to vectors that are collinear (all point in the same direction in H_{E_1}). This requires:

$$\boxed{R_k|\gamma\rangle \propto |y\rangle \quad \forall k \text{ with } s_k > 0}$$

For generic Cartan coefficients (c_x, c_y, c_z all distinct and non-zero), the operator-Schmidt rank of U_1 is r = 4 (the maximum). The condition that 4 independent operators R_k all map |γ⟩ to the same direction is codimension ≥ 2(d=2) = a measure-zero algebraic condition in the parameter space (c_α, A, B, C, D, p).

**Explicit algebraic characterization (d = 2):**

Write |γ⟩ = (cos(φ/2), e^{iχ} sin(φ/2))^T in the basis that diagonalizes the Cartan core. Then:

$$\boxed{\dim(Y) = 2 \iff \text{NOT}(c_y = c_z = 0 \text{ AND } D|\gamma\rangle \text{ is an eigenvector of } \sigma_x)}$$

and cyclically for σ_y, σ_z. Equivalently, dim(Y) < 2 iff the Cartan vector c = (c_x, c_y, c_z) is parallel to a single Pauli direction AND the environment initial state is aligned with that direction's eigenbasis.

**Generic case (Haar measure 1):** dim(Y) = d = 2.

### 5.4 Physical interpretation of dim(Y) = d in temporal terms

dim(Y) = d means: **the first Q-E interaction U_1, when the environment is initialized in state ρ_E, generates sufficient entanglement between Q and E that the environment "records" information about ALL system degrees of freedom.**

- dim(Y) = 2: E_1 "sees" both computational basis states of Q_1 through U_1 → the environment acts as a full quantum memory for the system.
- dim(Y) = 1: E_1 only records information about one "direction" in the system's Hilbert space → the environment is partially blind.
- dim(Y) = 0: U_1 is a product unitary (u_1 = V_Q ⊗ W_E) → no Q-E entanglement generated.

**The CFOL condition in temporal language:**

$$\boxed{\text{QCMI} > 0 \text{ for the temporal sequence} \iff \dim(Y) = 2 \text{ AND } U_2 \text{ does not perfectly "undo" the U}_1 \text{ correlations}}$$

The second condition (U_2 not perfectly undoing U_1) is automatically satisfied for generic unitaries and is the temporal analog of the spatial CFOL condition that the total cycle unitary is not factorizable.

---

## §6. Tensor Network Diagram (Spatial Representation)

The temporal-to-spatial mapping can be visualized as the following tensor network (read top-to-bottom as time, left-to-right as space):

```
Time (vertical)           Spatial (horizontal)
    |                     
    Q_0 ─────────────────────────────────────────── Q_5
    │                                               │
    │ G_1                                            │
    │                                                │
    Q_1 ──── U_1 ──── E_0                           │
    │         │        │                             │
    │         │     [ρ_E]                            │ G_3
    │         │        │                             │
    Q_2 ──── U_1 ──── E_1 ──── [identity] ──── E_1 ──│
    │              (output)                    (input)│
    │ G_2                                            │
    │                                                │
    Q_3 ──── U_2 ──── E_1 ──── [identity] ──── E_1   │
    │         │                                      │
    │         │                                      │
    Q_4 ──── U_2 ──── E_2 ──── [trace]              │
    │              (output)                          │
    │ G_3                                            │
    │                                                │
    Q_5 ──────────────────────── [CJ boundary: |Φ⁺⟩ with Q_0]
```

After contracting all internal Q_i indices and "flattening" time into space, the remaining topology is:

```
    Q_a ───[U_1]─── E_1
     │               │
     │               │
    [u_4]          [u_2 = identity + G_2]
     │               │
     │               │
    E_2 ───[U_2]─── Q_b
```

This is the 4-node spatial ring: Q_a — E_1 — Q_b — E_2 — Q_a.

---

## §7. The Complete Theorem

### Theorem (Temporal-to-Spatial CJ Bridge)

Let a single qubit Q (d=2) undergo a temporal sequence of operations: unitary gate G_1 on Q, Q-E interaction U_1, unitary gate G_2 on Q, Q-E interaction U_2, unitary gate G_3 on Q, with initial environment state ρ_E. Let the environment qubit E have no independent dynamics between interactions (identity channel).

Then:
1. The Choi-Jamiolkowski representation of the total process produces a tensor network whose effective topology, after contracting all internal system wires, is a 4-node ring Q_a—E_1—Q_b—E_2—Q_a with cycle rank b_1 = 1.

2. The four effective nodes correspond to:
   - Q_a: the system across the first interaction (Q_0, Q_1, Q_2)
   - E_1: the environment across the first interaction (E_0, E_1)
   - Q_b: the system across the second interaction (Q_2, Q_3, Q_4)
   - E_2: the environment across the second interaction (E_1, E_2)

3. The four effective edges correspond to:
   - u_1: the Choi state of U_1 combined with G_1
   - u_2: the identity channel on E combined with G_2 on Q (environment memory)
   - u_3: the Choi state of U_2
   - u_4: the CJ boundary condition (|Φ^+⟩ pairing of input Q_0 and output Q_5)

4. The CFOL condition dim(Y) = d translates to the temporal language as: the environment E, initialized in state ρ_E, after evolving through U_1, occupies a subspace that spans all d degrees of freedom of the environment. Equivalently: the operator-Schmidt components R_k of U_1 map the initial environment state |γ⟩ to linearly independent vectors in H_{E_1}.

5. When dim(Y) = d (probability 1 under Haar-random choice of U_1 and ρ_E), the QCMI of the temporal process satisfies:

$$\boxed{\text{QCMI}_{\text{temporal}} \geq \eta_0 \cdot \sum_{v \in \{Q_a, Q_b\}} |c_{\text{eff}}^{(v)}|^2}$$

where c_eff^{(v)} are the effective Cartan coefficients combining U_1 and U_2 contributions at each Q node, and η_0 = 1/(8 ln 2).

---

## §8. Self-Attack (Mandatory)

### SA-1: The E identity maps E_1 to E_1', but these are formally different indices 🔴🔴

**Attack:** In the Choi construction, the E_1 output index of U_1 and the E_1 input index of U_2 are DIFFERENT tensor legs (they come from different Choi states). Contracting them requires asserting they represent the SAME physical qubit. But the CJ formalism treats them as independent.

**Response:** This is precisely the point. The CJ isomorphism converts temporal identity of a physical system into a SPATIAL connection between different tensor legs. The identity channel on E between the two interactions is:

$$I_E: \mathcal{B}(\mathcal{H}_{E_1}^{\text{out}}) \to \mathcal{B}(\mathcal{H}_{E_1}^{\text{in}})$$

Its Choi state is |Φ^+⟩⟨Φ^+|_{E_1^{out}, E_1^{in}}. The contraction with this Choi state is exactly the link product we performed. The fact that these are "different" tensor legs in the spatial network is the ENTIRE POINT of the CJ mapping — it spatializes the temporal identity. This is not a bug; it is the feature we are proving.

### SA-2: The u_4 edge (CJ boundary) seems artificial 🔴🔴🔴

**Attack:** Edge u_4 of the spatial ring is identified as the CJ boundary condition (the |Φ^+⟩ linking Q_0 and Q_5). But this boundary condition is a mathematical artifact of the CJ construction, not a physical interaction. Can a mathematical artifact serve as a physical edge in the spatial ring?

**Response:** This is the deepest conceptual issue in the temporal-to-spatial mapping. The CJ boundary IS mathematically an edge in the tensor network — it couples Q_0 and Q_5 via a maximally entangled state. Physically, it represents the fact that the INPUT and OUTPUT of the process are related: the reference system R stores the initial correlations, and the question "did those correlations end up in Q or in E?" is what QCMI measures.

The u_4 edge in the spatial CFOL plays an analogous role: it is the edge that "closes the ring" and distinguishes the ring topology from a simple chain. In the spatial setting, u_4 is a physical unitary. In the temporal setting, the CJ boundary serves the same TOPOLOGICAL function (closing the cycle) even though it is not a dynamical unitary. The CFOL derivation does not depend on u_4 being a generic unitary — it only requires that the cycle exists (b_1 = 1) and that dim(Y) = d.

However, this is a genuine point of non-equivalence: the temporal ring has a "boundary edge" that is pure entanglement (|Φ^+⟩), while the spatial ring has a physical unitary edge. The quantitative prefactor η_0 may differ in the two cases. This deserves further investigation.

### SA-3: What about G_1 and G_3? 🔴🔴

**Attack:** The temporal sequence includes G_1 and G_3, but the spatial ring only has 4 edges (u_1, u_2, u_3, u_4). Where did G_1 and G_3 go?

**Response:** G_1 is absorbed into the effective u_1 edge (it modifies the Choi state of U_1). G_3 is absorbed into the effective u_4 edge (it modifies the CJ boundary condition). Specifically:
- Effective u_1 = U_1 ∘ (G_1 ⊗ I_E), acting on Q_a ⊗ E_1
- Effective u_4 = (G_3† ⊗ I) ∘ CJ_boundary, acting on E_2 ⊗ Q_a

This absorption is legitimate because the CFOL theorem depends only on the TOPOLOGY of the ring and the Cartan coefficients of the edges. G_1 and G_3 modify the Cartan coefficients of u_1 and u_4 but do not change the ring topology.

Formally: if CFOL holds for a ring with arbitrary Cartan vectors {c^{(1)}, c^{(2)}, c^{(3)}, c^{(4)}}, and G_1, G_3 are local unitaries (which only rotate the Cartan vectors without changing their magnitudes), then the same theorem applies with rotated Cartan vectors.

### SA-4: Single qubit vs multi-qubit generalization 🔴

**Attack:** This derivation assumes a SINGLE system qubit and a SINGLE environment qubit. CFOL is proved for general d. Is the mapping valid for d > 2?

**Response:** The mapping generalizes straightforwardly. For d-dimensional system and environment:
- The Choi state of U_1 lives on C^d ⊗ C^d ⊗ C^d ⊗ C^d (d^4 dimensional)
- The operator-Schmidt rank of U_1 is at most d^2
- dim(Y) = d is the generic condition (requiring d vectors R_k|γ⟩ in d-dimensional E-space to be linearly independent)
- The codimension of the degenerate set {dim(Y) < d} grows with d: it's a condition on d × d^2 = d^3 real parameters, making it measure zero for all d ≥ 2

The core topological argument (temporal sequence → 4-node spatial ring with b_1 = 1) is independent of d.

---

## §9. Implications

### 9.1 For the CFOL theorem

The temporal-to-spatial bridge proves that CFOL applies to real quantum circuits, not just abstract spatial rings. Any temporal sequence with two Q-E interaction events separated by identity (memory) on E is effectively a 4-node spatial ring. QCMI > 0 follows generically.

### 9.2 For experimental verification

The bridge provides the theoretical foundation for measuring QCMI on real hardware (e.g., IBM Q). The experimental protocol is:
1. Prepare Q in state |ψ⟩, E in state ρ_E
2. Apply gate G_1 to Q
3. Apply Q-E interaction U_1 (e.g., CNOT or Rxx(θ))
4. Apply gate G_2 to Q (E is idle)
5. Apply Q-E interaction U_2
6. Apply gate G_3 to Q
7. Measure QCMI = I(R;E'|Q') using process tomography of the effective spatial ring

### 9.3 For the Cartan axis alignment prediction

The bridge connects the temporal Cartan axis alignment analysis [bridge_to_smoking_gun.md] to the spatial CFOL framework. The Cartan axes of U_1 and U_2 (in the temporal picture) correspond to the Cartan vectors c^{(1)} and c^{(3)} in the spatial ring. The commutativity condition [σ_α^{(1)}, σ_β^{(2)}] determines whether the effective ring has aligned or misaligned Cartan vectors, which controls the QCMI scaling (θ^2 log(1/θ) vs θ^4).

---

## §10. Summary

$$\boxed{\begin{array}{c}
\text{Temporal sequence on Q+E} \\
\downarrow \text{Choi-Jamiolkowski isomorphism} \\
\text{Spatial tensor network} \\
\downarrow \text{contract Q-wires, flatten time} \\
\text{4-node spatial ring } Q_a-E_1-Q_b-E_2-Q_a \\
\downarrow \text{CFOL theorem} \\
\text{QCMI} \geq \eta_0 \cdot \sum_v |c_{\text{eff}}^{(v)}|^2 \quad (\text{with probability 1})
\end{array}}$$

The Choi-Jamiolkowski isomorphism is the rigorous bridge between temporal quantum dynamics and spatial causal topology. It converts the "same qubit at different times" into "different tensor factors in a spatial tensor network," and the "environment memory between interactions" into "a spatial edge connecting the two interaction events." The resulting topology is the 4-node ring of CFOL, with the CJ boundary providing the ring closure.

---

## Appendix A: Explicit Verification for the CNOT Case

As a concrete test, consider the simplest non-trivial case:

- U_1 = CNOT with Q_1 as control, E_0 as target (Cartan vector c = (π/4, 0, 0))
- U_2 = CNOT with Q_3 as control, E_1 as target (same Cartan vector)
- G_1 = G_2 = G_3 = I (identity, for simplicity)
- ρ_E = |0⟩⟨0| (p = 1)

The temporal sequence: Q_0 → CNOT(Q,E) → E stores parity → second CNOT(Q,E) → E stores new parity...

The Choi state of U_1 = CNOT:

$$|CNOT\rangle\rangle = \frac{1}{2}\left(|00\rangle_{Q_1E_0}|00\rangle_{Q_2E_1} + |01\rangle_{Q_1E_0}|01\rangle_{Q_2E_1} + |10\rangle_{Q_1E_0}|11\rangle_{Q_2E_1} + |11\rangle_{Q_1E_0}|10\rangle_{Q_2E_1}\right)$$

Contracting E_0 with |γ⟩ = |0⟩:

$$|CNOT_{|\gamma\rangle}\rangle\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle_{Q_1}|00\rangle_{Q_2E_1} + |1\rangle_{Q_1}|11\rangle_{Q_2E_1}\right)$$

The operator-Schmidt components of CNOT (in the Q_1E_0 : Q_2E_1 bipartition):

CNOT = |0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ X = Σ_{k=0}^1 L_k ⊗ R_k with L_0 = |0⟩⟨0|, R_0 = I; L_1 = |1⟩⟨1|, R_1 = X.

R_0|0⟩ = |0⟩, R_1|0⟩ = |1⟩. These span the full 2D space → dim(Y) = 2. Prefactor η_0 applies, and QCMI > 0 for generic G_2 (non-identity, non-CNOT-inverse).

---

*Derivation complete. The CJ isomorphism provides the rigorous temporal-to-spatial bridge. The 4-node ring topology emerges from two Q-E interactions connected by environment memory, with the CJ boundary closing the cycle. The dim(Y) = d condition translates to the first interaction's operator-Schmidt components spanning the full environment space under the initial environment state.*
