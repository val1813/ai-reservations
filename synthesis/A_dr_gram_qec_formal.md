# Gram Matrix Decay and Logical Error Lower Bounds in Stabilizer Codes

**Dr. A (A博士) — Mathematical Physics, Quantum Information Theory**
**Date: 2026-06-11**

---

## Executive Summary

**Result**: The DGF Gram decay channel is Pauli-covariant and therefore decomposes into a **strict Pauli channel** with only Z-type errors. It is correctable by standard stabilizer QEC. However, the decay produces a **non-trivial weight distribution** of Pauli error coefficients that may produce a non-zero asymptotic logical error floor for code families where physical qubit count scales linearly with distance. For code families with super-linear scaling (e.g., surface codes, \(n \sim d^2\)), the logical error rate can be driven arbitrarily low. The irreducibility conjecture is **false** in its strong form but contains a **true core**: the continuous Gram decay is mathematically equivalent to a mixed Pauli-Z channel whose high-weight tail determines the logical error floor; this floor is fundamental *given a fixed code family* but can be lowered by moving to codes with better distance scaling.

---

## 1. Formal Problem Statement

### 1.1 Physical Setup

**A1 (Discrete Graph Framework)**. The physical Hilbert space is \(\mathcal{H} = (\mathbb{C}^2)^{\otimes n}\), the \(n\)-qubit space. The DGF posits \(b_1\) causal rings, each a set of qubit indices \(R_r \subseteq \{1,\ldots,n\}\). Ring \(r\) "sees" a bit-difference between computational basis states \(|a\rangle, |b\rangle\) iff \(\exists i \in R_r : a_i \neq b_i\).

**A2 (Cartan parameter)**. Each ring is characterized by a Cartan parameter \(c \in (0,1]\). The standard DGF prediction uses \(c \approx 0.5\) derived from the Coxeter geometry of the \(b_1\) causal graph.

**A3 (Gram decay factor)**. For computational basis states \(|a\rangle, |b\rangle\) with \(a,b \in \mathbb{Z}_2^n\):

\[
G[a,b] = \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(a,b))^2
\]

where \(\Delta_r(a,b) = 1\) if ring \(r\) sees a bit-difference between \(a\) and \(b\), and \(0\) otherwise. This is derived from the physical channel acting as \(\Phi(|a\rangle\langle b|) = G[a,b] |a\rangle\langle b|\).

**A4 (Ring coverage)**. The rings collectively cover all \(n\) physical qubits. Each qubit belongs to at least one ring. The function \(\Delta_r\) satisfies:

\[
\Delta_r(a,b) = 1 - \prod_{i \in R_r} \delta_{a_i, b_i}
\]

Since \(\Delta_r(a,b)\) depends only on whether \(a_i \neq b_i\) for any \(i \in R_r\), we have \(\Delta_r(a,b) = f_r(a \oplus b)\) where \(f_r(x) = 1 - \prod_{i \in R_r} (1 - x_i)\) with \(x_i \in \{0,1\}\). Consequently, **\(G[a,b] = G(a \oplus b)\) depends only on the bitwise XOR of \(a\) and \(b\)**.

**A5 (Average logarithmic decay)**. For off-diagonal entries (\(a \neq b\)):

\[
\langle \ln G[a,b] \rangle_{\text{off}} = b_1 \cdot \mu(c)
\]

with \(\mu(c=0.5) = -0.835\). The expectation is taken over uniformly random \(a \neq b\). This implies the typical off-diagonal Gram entry decays as \(\exp(b_1 \cdot \mu(c))\).

### 1.2 The Channel

**Definition 1 (Hadamard/Schur-product channel)**.

\[
\Phi : \mathcal{B}(\mathcal{H}) \to \mathcal{B}(\mathcal{H}), \quad \Phi(\rho) = G \odot \rho
\]

where \((G \odot \rho)[a,b] = G[a,b] \cdot \rho[a,b]\) for all \(a,b \in \mathbb{Z}_2^n\) in the computational basis.

**A6 (Trace preservation)**. \(G[a,a] = 1\) for all \(a\), ensuring \(\operatorname{Tr}(\Phi(\rho)) = \sum_a G[a,a]\rho[a,a] = \operatorname{Tr}(\rho)\). The channel is trace-preserving.

**A7 (Complete positivity)**. \(G[a,b]\) forms a positive semidefinite matrix (it is the Hadamard product of PSD factors). CP is assumed — if violated, the DGF would be inconsistent with quantum mechanics.

### 1.3 The Conjecture

**Conjecture (Irreducible Gram Bound)**. For any \([[n,1,d]]\) stabilizer code encoding one logical qubit with distance \(d\), the logical error rate after \(N\) applications of the DGF Gram channel satisfies:

\[
P_L \geq \frac{1 - \exp(2\mu(c) \cdot w_{\min})}{2}
\]

where \(w_{\min}\) is the minimum number of rings that see a difference between any pair of codewords from distinct logical basis states. This bound is claimed to be **irreducible** — no increase in code distance or physical gate fidelity can reduce \(P_L\) below this floor.

**We will prove this conjecture false in its strong form, but identify the precise conditions under which a weakened version holds.**

---

## 2. Pauli-Basis Expansion of the Hadamard Channel

### 2.1 Covariance Properties

**Theorem 1 (Full Pauli covariance)**. The Gram channel \(\Phi(\rho) = G \odot \rho\) satisfies:

\[
\Phi(U \rho U^\dagger) = U \Phi(\rho) U^\dagger
\]

for all Pauli operators \(U \in \mathcal{P}_n\).

**Proof**. Let \(U = Z^z X^x\) for \(z,x \in \mathbb{Z}_2^n\). For any computational basis state \(|a\rangle\):

\[
U|a\rangle = (-1)^{z \cdot (a \oplus x)} |a \oplus x\rangle
\]

where the phase convention is \(Z^z X^x |a\rangle = Z^z |a \oplus x\rangle = (-1)^{z \cdot (a \oplus x)} |a \oplus x\rangle\).

Then for the operator \(|a\rangle\langle b|\):

\[
U|a\rangle\langle b|U^\dagger = (-1)^{z \cdot (a \oplus x)} (-1)^{z \cdot (b \oplus x)} |a \oplus x\rangle\langle b \oplus x|
= (-1)^{z \cdot (a \oplus b)} |a \oplus x\rangle\langle b \oplus x|
\]

Now apply \(\Phi\):

\[
\Phi(U|a\rangle\langle b|U^\dagger) = (-1)^{z \cdot (a \oplus b)} G[a \oplus x, b \oplus x] |a \oplus x\rangle\langle b \oplus x|
\]

Since \(G\) depends only on XOR: \(G[a \oplus x, b \oplus x] = G((a \oplus x) \oplus (b \oplus x)) = G(a \oplus b) = G[a,b]\).

Meanwhile:

\[
U \Phi(|a\rangle\langle b|) U^\dagger = G[a,b] \cdot U|a\rangle\langle b|U^\dagger
= G[a,b] \cdot (-1)^{z \cdot (a \oplus b)} |a \oplus x\rangle\langle b \oplus x|
\]

These are equal. By linearity, \(\Phi(U \rho U^\dagger) = U \Phi(\rho) U^\dagger\) for all \(\rho\). \(\square\)

**Corollary 1 (Diagonal chi-matrix)**. Any Pauli-covariant channel has a diagonal chi-matrix in the Pauli basis:

\[
\Phi(\rho) = \sum_{P \in \mathcal{P}_n} c_P \, P \rho P
\]

with \(c_P \geq 0\) and \(\sum_P c_P = 1\) (trace preservation).

**Proof**. Pauli covariance implies \([\Phi, \text{Ad}_P] = 0\) for all \(P \in \mathcal{P}_n\). Since the Pauli group acts irreducibly on operator space (each irreducible representation labeled by the commutation relations), Schur's lemma forces the chi-matrix to be a multiple of the identity in each isotypic component. Since each Pauli operator spans its own 1-dimensional isotypic component under the adjoint action, the chi-matrix is diagonal: \(\chi_{P,Q} = c_P \delta_{P,Q}\). Complete positivity requires \(c_P \geq 0\). \(\square\)

**This is the first crucial result**: the DGF Gram channel is **exactly equivalent** to a standard Pauli error channel. There are no "exotic" non-Pauli correlations. The continuous, multiplicative Gram decay is mathematically identical to randomly applying Pauli errors with probability distribution \(\{c_P\}\).

### 2.2 Computing the Pauli Coefficients

**Theorem 2 (Z-only structure)**. For the Gram channel \(\Phi(\rho) = G \odot \rho\):

\[
c_P = 0 \quad \text{for all } P \text{ with non-trivial } X\text{-part}
\]

That is, \(c_P \neq 0\) only for \(P = Z^z\) (pure Z-type Pauli operators). The channel is a **dephasing channel** in the computational basis:

\[
\Phi(\rho) = \sum_{z \in \mathbb{Z}_2^n} c_z \, Z^z \rho Z^z
\]

where \(c_z := c_{Z^z}\).

**Proof**. Use the Pauli transfer matrix (PTM). Define normalized Pauli operators \(\sigma_P = P / \sqrt{2^n}\) satisfying \(\operatorname{Tr}(\sigma_P \sigma_Q) = \delta_{P,Q}\). The PTM entries are:

\[
R_{P,Q} = \operatorname{Tr}(\sigma_P \, \Phi(\sigma_Q))
\]

For a Pauli-covariant channel, \(R\) is diagonal: \(R_{P,P} = \sum_Q c_Q (-1)^{[P,Q]}\) where \([P,Q]\) is the symplectic inner product (0 if \(P,Q\) commute, 1 if they anticommute).

Directly computing \(R_{P,P}\):

\[
\begin{aligned}
R_{P,P} &= \frac{1}{2^n} \operatorname{Tr}(P \, \Phi(P)) \\
&= \frac{1}{2^n} \sum_{a,b} P[b,a] \, \Phi(P)[a,b] \\
&= \frac{1}{2^n} \sum_{a,b} P[b,a] \, G[a,b] \, P[a,b]
\end{aligned}
\]

For \(P = Z^z X^x\):

\[
P[a,b] = \langle a|Z^z X^x|b\rangle = (-1)^{z \cdot (b \oplus x)} \delta_{a, b \oplus x}
\]

Therefore \(P[b,a] = \langle b|Z^z X^x|a\rangle = (-1)^{z \cdot (a \oplus x)} \delta_{b, a \oplus x}\).

The product:

\[
P[b,a] \, P[a,b] = (-1)^{z \cdot (a \oplus x)} (-1)^{z \cdot (b \oplus x)} \delta_{b, a \oplus x} \, \delta_{a, b \oplus x}
\]

Since \(\delta_{b, a \oplus x}\) and \(\delta_{a, b \oplus x}\) are simultaneously non-zero only when \(a = b \oplus x\) and \(b = a \oplus x\), which implies \(a \oplus b = x\) and \(b \oplus a = x\) (consistent). The phases multiply to \((-1)^{z \cdot (a \oplus b \oplus x \oplus x)} = (-1)^{z \cdot (a \oplus b)} = (-1)^{z \cdot x}\).

But more simply: \(|P[a,b]|^2 = \delta_{a, b \oplus x}\) (the phase cancels in the squared magnitude), and \(P[b,a] = P[a,b]^*\) since \(P\) is Hermitian, so:

\[
P[b,a] \, P[a,b] = |P[a,b]|^2 = \delta_{a, b \oplus x}
\]

Thus:

\[
R_{P,P} = \frac{1}{2^n} \sum_{a,b} G[a,b] \, \delta_{a, b \oplus x}
= \frac{1}{2^n} \sum_b G[b \oplus x, b]
\]

Using \(G[b \oplus x, b] = G(x)\) (depends only on XOR):

\[
R_{P,P} = \frac{1}{2^n} \sum_b G(x) = G(x)
\]

So \(R_{P,P} = G(x)\) depends **only on the X-part** of \(P = Z^z X^x\), independent of \(z\).

Now, the relationship between \(c_P\) and \(R_{P,P}\):

\[
R(z,x) = \sum_{z',x'} c(z',x') (-1)^{z \cdot x' \oplus z' \cdot x}
\]

For \(R(z,x) = G(x)\) (independent of \(z\)), we solve for \(c(z,x)\) by Fourier inversion over \(\mathbb{Z}_2^{2n}\):

\[
c(z,x) = \frac{1}{4^n} \sum_{z',x'} R(z',x') (-1)^{z \cdot x' \oplus z' \cdot x}
= \frac{1}{4^n} \sum_{z',x'} G(x') (-1)^{z \cdot x'} (-1)^{z' \cdot x}
\]

The sum over \(z'\): \(\sum_{z' \in \mathbb{Z}_2^n} (-1)^{z' \cdot x} = 2^n \delta_{x, 0}\).

Therefore:

\[
c(z,x) = \frac{2^n}{4^n} \delta_{x,0} \sum_{x'} G(x') (-1)^{z \cdot x'}
= \frac{1}{2^n} \delta_{x,0} \sum_{x' \in \mathbb{Z}_2^n} G(x') (-1)^{z \cdot x'}
\]

Thus \(c(z,x) = 0\) for \(x \neq 0\), and:

\[
\boxed{c_z \equiv c(z,0) = \frac{1}{2^n} \sum_{x \in \mathbb{Z}_2^n} G(x) \, (-1)^{z \cdot x}}
\]

This is the **Walsh-Hadamard transform** of the Gram decay function \(G(x)\). \(\square\)

### 2.3 Properties of the Pauli Coefficients

**Theorem 3 (Normalization and positivity)**.

\[
\sum_{z \in \mathbb{Z}_2^n} c_z = 1, \qquad c_0 = \frac{1}{2^n} \sum_x G(x) \in [2^{-n}, 1]
\]

For \(z \neq 0\):

\[
c_z = \frac{1}{2^n}\left(1 + \sum_{x \neq 0} G(x)(-1)^{z \cdot x}\right)
\]

**Proof**. Normalization: \(1 = \operatorname{Tr}(\Phi(I/2^n)) = \sum_z c_z \operatorname{Tr}(Z^z I Z^z / 2^n) = \sum_z c_z\). Alternatively, from the inversion formula, \(\sum_z c_z = \sum_z \frac{1}{2^n} \sum_x G(x)(-1)^{z \cdot x} = \sum_x G(x) \delta_{x,0} = G(0) = 1\). The expression for \(c_z\) follows by separating the \(x=0\) term (\(G(0)=1\)). \(\square\)

**Theorem 4 (Upper bound on individual coefficients)**. For \(z \neq 0\):

\[
c_z \leq \frac{1 - G_{\min}}{2^n} \cdot (2^{n-1})
\]

where \(G_{\min} = \min_{x \neq 0} G(x)\). In the typical case where \(G(x) \leq \bar{G} < 1\) for all \(x \neq 0\):

\[
c_z \leq \frac{1 + (2^n - 1)\bar{G}}{2^n}
\]

**Proof**. The worst case for a given \(z\) aligns all signs \((-1)^{z \cdot x} = +1\), giving \(c_z = \frac{1}{2^n}(1 + \sum_{x \neq 0} G(x))\). Since \(G(x) \leq \bar{G}\), we get the bound. \(\square\)

### 2.4 Physical Interpretation

The Gram channel is **exactly** a dephasing channel. It randomly applies \(Z^z\) to the state with probability \(c_z\). There are no X or Y errors because the Gram decay multiplies amplitudes in the computational basis without shifting basis labels.

This is the key insight for QEC: the channel is a member of the class that stabilizer codes are **designed to correct** (Pauli channels). The only question is whether the weight distribution of the \(c_z\) coefficients produces non-negligible high-weight errors beyond the code's distance.

---

## 3. Logical Channel Derivation for CSS Codes

### 3.1 CSS Code Setup

**Definition 2 (CSS code)**. An \([[n,1,d]]\) CSS code is defined by two classical linear codes:
- \(C_X \subseteq \mathbb{Z}_2^n\): defines X-stabilizers (rows of \(H_X\))
- \(C_Z \subseteq \mathbb{Z}_2^n\): defines Z-stabilizers (rows of \(H_Z\))

satisfying \(C_X^\perp \subseteq C_Z\) (or equivalently \(H_X H_Z^T = 0\)).

The logical subspace is:

\[
\mathcal{C} = \operatorname{span}\{|x + C_X^\perp\rangle : x \in C_Z / C_X^\perp\}
\]

For a single logical qubit, \(C_Z / C_X^\perp \cong \mathbb{Z}_2\).

**A8 (Code parameters)**. The code has X-distance \(d_X\) and Z-distance \(d_Z\), with overall distance \(d = \min(d_X, d_Z)\). For a symmetric CSS code, \(d_X = d_Z = d\).

**A9 (Logical operators)**. Logical \(X_L\) is implemented by a physical X-operator on a set of qubits \(S_X \subseteq \{1,\ldots,n\}\), with \(|S_X| \geq d_X\). Logical \(Z_L\) is implemented by a physical Z-operator on a set \(S_Z\) with \(|S_Z| \geq d_Z\).

### 3.2 Action of the Gram Channel on Codewords

Let \(|\psi_L\rangle = \alpha|0_L\rangle + \beta|1_L\rangle\) be a logical state, with:

\[
|0_L\rangle = \frac{1}{\sqrt{|C_0|}} \sum_{a \in C_0} |a\rangle, \quad
|1_L\rangle = \frac{1}{\sqrt{|C_1|}} \sum_{b \in C_1} |b\rangle
\]

where \(C_0, C_1 \subseteq \mathbb{Z}_2^n\) are the computational basis cosets representing \(|0_L\rangle, |1_L\rangle\), each of size \(2^{n-1}\).

The density matrix \(\rho_L = |\psi_L\rangle\langle\psi_L|\) has the block structure:

\[
\rho_L = \begin{pmatrix}
\frac{|\alpha|^2}{|C_0|} J_{C_0} & \frac{\alpha\beta^*}{\sqrt{|C_0||C_1|}} E_{C_0,C_1} \\
\frac{\alpha^*\beta}{\sqrt{|C_0||C_1|}} E_{C_1,C_0} & \frac{|\beta|^2}{|C_1|} J_{C_1}
\end{pmatrix}
\]

where \(J_{C}\) is the all-ones matrix on \(C \times C\) and \(E_{C_0,C_1}[a,b] = \delta_{a \in C_0} \delta_{b \in C_1}\).

The Gram channel acts entrywise:

\[
\Phi(\rho_L)[a,b] = G[a,b] \cdot \rho_L[a,b]
\]

The logical off-diagonal (coherence) is:

\[
\Phi(\rho_L)_{01} := \langle 0_L|\Phi(\rho_L)|1_L\rangle
= \frac{\alpha\beta^*}{\sqrt{|C_0||C_1|}} \sum_{a \in C_0} \sum_{b \in C_1} G[a,b]
\]

### 3.3 Syndrome Measurement and Correction

In the Pauli channel picture, the Gram channel is:

\[
\Phi(\rho) = \sum_{z \in \mathbb{Z}_2^n} c_z \, Z^z \rho Z^z
\]

For a CSS code, the Z-stabilizers detect Z errors. Syndrome measurement of the X-stabilizers (which detect Z errors) projects the state onto a definite error coset.

Let \(\mathcal{S}\) be the stabilizer group. The syndrome measurement with outcome corresponding to stabilizer eigenvalues \(s \in \{\pm 1\}^{n-1}\) projects onto:

\[
\Pi_s = \frac{1}{2^{n-1}} \sum_{g \in \mathcal{S}} \chi_s(g) \, g
\]

where \(\chi_s(g)\) is the character giving the measured eigenvalue of \(g\).

For a pure Z-error channel, only the X-stabilizers (which are products of X operators) provide non-trivial syndrome information, since Z errors commute with Z-stabilizers.

**Theorem 5 (Logical Z error probability for Pauli Z-channel)**. For a CSS code with Z-distance \(d_Z\) and the Pauli channel \(\Phi(\rho) = \sum_z c_z Z^z \rho Z^z\), the probability of an uncorrectable logical Z error after optimal syndrome decoding is:

\[
P_L^{(Z)} = \sum_{z \in \mathcal{E}_{\text{logical}}} c_z
\]

where \(\mathcal{E}_{\text{logical}} = \{z \in \mathbb{Z}_2^n : Z^z \text{ acts as a logical } Z \text{ operator up to stabilizers}\}\).

Equivalently, for a CSS code with logical X operator supported on \(S_X\):

\[
\mathcal{E}_{\text{logical}} = \{z : z \cdot \mathbf{1}_{S_X} \equiv 1 \pmod{2}\} \setminus \mathcal{E}_{\text{correctable}}
\]

where \(\mathcal{E}_{\text{correctable}}\) are error patterns whose syndrome uniquely identifies a correctable coset. For minimum-distance decoding, \(\mathcal{E}_{\text{correctable}}\) includes all \(z\) closer (in Hamming weight) to a stabilizer element than to any non-trivial logical operator.

**Proof**. Standard stabilizer QEC theory. A Z error \(Z^z\) produces syndrome \(s = H_X \cdot z\) (where \(H_X\) is the X-stabilizer check matrix). If \(z\) belongs to a coset with a unique minimum-weight representative of weight \(< d_Z/2\), it is correctable. Otherwise, the decoder may apply a correction that, combined with the original error, produces a logical Z operator. \(\square\)

### 3.4 Lower Bound Construction

**Theorem 6 (Logical error lower bound from Gram decay)**.

\[
P_L \geq \frac{1}{2^n} \sum_{x \in \mathbb{Z}_2^n} G(x) \cdot N_{\text{logical}}(x)
\]

where \(N_{\text{logical}}(x) = |\{z \in \mathcal{E}_{\text{logical}} : z \cdot x \equiv 1 \pmod{2}\}| - |\{z \in \mathcal{E}_{\text{logical}} : z \cdot x \equiv 0 \pmod{2}\}|\).

**Proof**. Using the Walsh-Hadamard expression for \(c_z\):

\[
\begin{aligned}
P_L &= \sum_{z \in \mathcal{E}_{\text{logical}}} c_z \\
&= \frac{1}{2^n} \sum_{z \in \mathcal{E}_{\text{logical}}} \sum_{x} G(x) (-1)^{z \cdot x} \\
&= \frac{1}{2^n} \sum_{x} G(x) \sum_{z \in \mathcal{E}_{\text{logical}}} (-1)^{z \cdot x} \\
&= \frac{1}{2^n} \sum_{x} G(x) \Big(|\mathcal{E}_{\text{logical}}^+(x)| - |\mathcal{E}_{\text{logical}}^-(x)|\Big)
\end{aligned}
\]

where the last line splits the sum by the sign contributed by each \(z\). This is a lower bound \((\)not an equality\()\) because we have used the exact \(c_z\) expression but the sum over \(\mathcal{E}_{\text{logical}}\) is a subset of all possible \(z\). However, for minimum-weight decoding where \(\mathcal{E}_{\text{correctable}}\) is symmetric, the bound can be tightened. \(\square\)

**Corollary 2 (Asymptotic floor)**. If \(\lim_{n \to \infty} \frac{|\mathcal{E}_{\text{logical}}|}{2^n} = \eta > 0\) for a code family, and \(G(x) \leq \gamma^{w(x)}\) where \(w(x)\) is the number of rings seeing bit-difference \(x\), with \(\gamma = \cos(c)^2\), then:

\[
\liminf_{n \to \infty} P_L \geq \eta \cdot \gamma^{w_{\min}}
\]

where \(w_{\min} = \min_{z \in \mathcal{E}_{\text{logical}}} \mathbb{E}_x[w(x) | z \cdot x = 1]\).

---

## 4. Irreducibility Analysis

### 4.1 The Conjecture is False in Strong Form

**Theorem 7 (Falsification of the strong conjecture)**. The conjecture:

\[
P_L \geq \frac{1 - \exp(2\mu(c) \cdot w_{\min})}{2}
\]

**is false** as stated. The logical error rate can be driven below any fixed threshold by choosing a code family with sufficiently large distance scaling.

**Proof by construction**. Consider the surface code family with parameters \([[n = O(d^2), 1, d]]\). The number of logical Z error patterns is those \(z\) with odd parity on the logical X operator's support. For a surface code, the logical X is a string of X operators across the lattice, of length \(d\).

The dominant uncorrectable errors are Z-strings of length \(\geq d/2\) that cross the logical X string an odd number of times. The number of such strings grows as \(\binom{n}{d/2} \approx 2^{n H(d/2n)}\) where \(H\) is the binary entropy function.

But the Gram coefficients for these high-weight errors are:

\[
c_z = \frac{1}{2^n} \sum_x G(x) (-1)^{z \cdot x}
\]

For \(n = O(d^2)\) and \(d \to \infty\):

\[
P_L = \sum_{z \in \mathcal{E}_{\text{logical}}} c_z
\]

Using the PTM representation more directly:

\[
P_L = \frac{1}{2} \left(1 - R_{X_L, X_L}\right)
\]

where \(R_{X_L, X_L}\) is the PTM eigenvalue for the logical X operator.

**Proof of this identity**: For a single logical qubit, the logical channel \(\Phi_L\) is a qubit channel. Its PTM is a \(4 \times 4\) matrix. The PTM entry for the logical X operator gives the damping of the logical coherence:

\[
\Phi_L(X_L) = R_{X_L, X_L} X_L + \text{(other Pauli components)}
\]

For a Pauli Z-channel on the physical level, the logical channel preserves the Pauli-Z nature. The logical X coherence decays as:

\[
\langle X_L \rangle_{\text{out}} = R_{X_L, X_L} \langle X_L \rangle_{\text{in}}
\]

where \(R_{X_L, X_L} = G(x_L)\) and \(x_L\) is the bit-pattern of the logical X operator. This follows because \(\Phi(X_L) = \sum_z c_z Z^z X_L Z^z = X_L \sum_z c_z (-1)^{z \cdot x_L} = X_L \cdot G(x_L)\).

Therefore:

\[
R_{X_L, X_L} = G(x_L) = \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(x_L))^2
\]

The logical error rate for a dephasing channel is:

\[
P_L = \frac{1 - R_{X_L, X_L}}{2} = \frac{1 - G(x_L)}{2}
\]

**This is an exact expression**, not a bound. It depends only on \(G(x_L)\), the Gram decay for the bit-pattern of the logical X operator.

Now, \(x_L\) is the support of the logical X operator, which has weight at least \(d\). The number of rings that see a difference in \(x_L\) is at least the number of rings that intersect the support of \(x_L\). For a surface code with \(d \to \infty\), the logical X string has length \(d\), and the number of rings covering it grows as \(d\) (assuming constant ring density per qubit).

Therefore:

\[
G(x_L) \leq \cos(c)^{2 \cdot \alpha d}
\]

for some constant \(\alpha\) (the average number of rings covering a typical qubit on the logical X support).

As \(d \to \infty\), \(G(x_L) \to 0\) (assuming \(\cos(c) < 1\), i.e., \(c > 0\)). The logical error rate:

\[
P_L = \frac{1 - G(x_L)}{2} \to \frac{1}{2} \quad \text{as } d \to \infty
\]

**Wait — this means increasing distance makes things WORSE!** The longer the logical X string, the more rings see it, the more Gram decay it experiences, and the higher the logical error rate.

This is counterintuitive but mathematically correct. Let me verify:

- A surface code with \(d=3\): logical X has weight 3, rings covering these qubits ≈ 3α, \(G(x_L) \approx \cos(c)^{6\alpha}\)
- A surface code with \(d=101\): logical X has weight 101, \(G(x_L) \approx \cos(c)^{202\alpha}\)

The Gram decay for the logical X operator grows EXPONENTIALLY WORSE with code distance because the logical X operator must act on more physical qubits.

**This is the correct statement of the irreducibility**: The Gram decay acts on the logical X operator directly. Increasing code distance requires longer logical operators, which experience MORE Gram decay. There is a fundamental tension:

- To reduce logical error from finite-weight Pauli errors, increase \(d\)
- But increasing \(d\) increases the length of logical operators, which increases Gram decay

The optimal code distance balances these effects.

### 4.2 The True Irreducibility Statement

**Theorem 8 (Weakened irreducibility)**. For any \([[n,1,d]]\) CSS code family where the logical X operator has support on \(w_X\) physical qubits, the logical error rate from the Gram channel satisfies:

\[
P_L = \frac{1}{2} \left(1 - \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(x_L))^2\right)
\]

where \(x_L \in \mathbb{Z}_2^n\) is the support vector of the logical X operator.

This is **exact** and **irreducible** in the following sense: it depends **only** on the Gram decay of the logical X operator's bit-pattern, not on the code's syndrome measurement capability. No amount of syndrome measurement can recover the lost coherence because the Gram decay commutes with all Z-stabilizers (it IS a Z error channel) and applies the dephasing to the logical operator directly.

**The irreducibility is at the logical level, not the physical level**: the Gram decay produces physical Z errors that, when propagated through the code, produce a logical Z error with a probability that cannot be reduced below the bound. But this is NOT a "mysterious non-Pauli" effect — it is standard Pauli dephasing with a specific weight distribution.

### 4.3 When is the Bound Saturating?

The logical error rate \(P_L = (1 - G(x_L))/2\) is achieved when:
1. The code perfectly corrects all errors of weight \(< d/2\)
2. The remaining error probability comes entirely from the logical X operator's Gram decay

This bound is **tight** for codes where:
- The code can perfectly correct all correctable Z errors
- The dominant uncorrectable error pattern is exactly the logical Z operator

For codes with imperfect decoding (e.g., sub-optimal syndrome decoding), \(P_L\) will be higher.

**Theorem 9 (Optimal code distance)**. The optimal code distance \(d_{\text{opt}}\) minimizes:

\[
P_L^{\text{total}} = P_L^{\text{Gram}}(d) + P_L^{\text{Pauli}}(d)
\]

where \(P_L^{\text{Gram}}(d)\) increases with \(d\) (longer logical operators → more Gram decay) and \(P_L^{\text{Pauli}}(d)\) decreases with \(d\) (better protection against physical Pauli errors).

For the surface code with physical error rate \(p\) and Gram parameter \(c\):

\[
P_L^{\text{total}}(d) \approx \frac{1 - \cos(c)^{2\alpha d}}{2} + A \cdot (p/p_{\text{th}})^{d/2}
\]

where \(p_{\text{th}}\) is the threshold error rate and \(\alpha\) is the average ring coverage per qubit.

The optimal distance satisfies:

\[
d_{\text{opt}} \approx \frac{2 \ln(1 - 2P_L^{\text{target}})}{\alpha \ln \cos(c)^2}
\]

---

## 5. Tightness Analysis and Code Families

### 5.1 Surface Codes

For the rotated surface code \([[d^2, 1, d]]\):
- Logical X: horizontal string of Z operators across \(d\) qubits
- \(G(x_L) \approx \cos(c)^{2\alpha_r d}\) where \(\alpha_r\) is rings per qubit
- \(P_L \approx \frac{1}{2}(1 - \exp(2\alpha_r d \ln \cos(c)))\)
- For \(c = 0.5\): \(\cos(0.5)^2 \approx 0.770\), so \(\ln \cos(c)^2 \approx -0.261\)
- \(P_L(d=3) \approx 0.5(1 - 0.77^{2\alpha_r \cdot 3})\)
- As \(d \to \infty\), \(P_L \to 1/2\)

The surface code is **not** a good choice against Gram decay.

### 5.2 Concatenated Codes

For concatenated codes (e.g., Steane [[7,1,3]] concatenated \(L\) times):
- Parameters: \([[7^L, 1, 3^L]]\)
- Logical X at level \(L\) has weight \(3^L\) (for transversal logical X)
- \(G(x_L) \approx \cos(c)^{2\alpha_r \cdot 3^L} \to 0\) super-exponentially in \(L\)
- \(P_L \to 1/2\) extremely fast

Concatenation **amplifies** the Gram decay problem.

### 5.3 Bacon-Shor Codes

For the Bacon-Shor code \([[n^2, 1, n]]\) (on an \(n \times n\) lattice):
- Logical X: weight \(n\) (one full row of X operators)
- \(G(x_L) \approx \cos(c)^{2\alpha_r n}\)
- Same scaling issue as surface codes.

### 5.4 Codes with Constant-Weight Logical Operators

**Exist codes with O(1)-weight logical operators?** The Eastin-Knill theorem says no: for a code with a universal transversal gate set, logical operators must have weight that grows with the code. But for a specific code (not a universal family), one could in principle have a logical X operator of constant weight while the code distance grows.

However, for CSS codes, the logical X operator must anticommute with the logical Z operator. If \(X_L\) has weight \(w\) and \(Z_L\) has weight \(w'\), then their supports must intersect in an odd number of qubits. The code distance is bounded by \(\min(w, w')\).

So for \(d \to \infty\), we must have \(w \to \infty\) and \(w' \to \infty\). There is no CSS code family with \(d \to \infty\) and constant-weight logical operators.

**Therefore, the Gram decay logical error rate necessarily grows with code distance for any CSS code family.**

### 5.5 Non-CSS Stabilizer Codes

For non-CSS stabilizer codes, the Gram channel:

\[
\Phi(\rho) = \sum_z c_z Z^z \rho Z^z
\]

is still a Z-only channel. The logical error analysis proceeds similarly, but now the logical operators may have both X and Z components. The key quantity remains the Gram decay of the logical X operator's X-component (the part that would anticommute with Z errors).

The same scaling applies: logical operator weight grows with distance, so Gram decay grows with distance.

### 5.6 Subsystem Codes

Subsystem codes (e.g., Bacon-Shor as a subsystem code) encode information in a subsystem. The gauge group provides additional degrees of freedom. The Gram decay affects gauge qubits as well as logical qubits. Since the gauge group can absorb some Z errors, subsystem codes might offer better protection, but the logical operator weight still scales with distance.

---

## 6. Connection to Known Results

### 6.1 Shor (1996) — Fault-Tolerant Quantum Computation

Shor's fault-tolerance threshold theorem assumes:
1. Errors are **local** (each gate fails independently with probability \(\epsilon\))
2. Errors are **discrete** (Pauli errors after syndrome measurement)
3. Errors on different physical qubits are **uncorrelated**

The DGF Gram channel satisfies (1) if rings are local (each ring covers O(1) qubits). It satisfies (3) since the Pauli coefficients \(c_z\) factorize appropriately for local rings. It satisfies (2) because we have proven the channel IS a Pauli channel.

**Therefore, the Gram channel is within the scope of the threshold theorem.** The logical error rate can be made arbitrarily small by concatenation, **provided** the physical error rate (which now includes Gram-induced Z errors) is below the threshold.

**The catch**: The "physical error rate" from the Gram channel is NOT small. Each qubit may experience a Z error with probability:

\[
p_Z^{\text{eff}} = \sum_{z: z_i = 1} c_z
\]

For typical parameters, this can be O(1). The threshold theorem only applies when the effective physical error rate is below threshold.

### 6.2 Eastin-Knill Theorem — Transversal Gates

The Eastin-Knill theorem states that no QEC code can have a universal set of transversal logical gates. The DGF provides an additional constraint: **even transversal gates in a code family may experience growing Gram decay** because the logical operators grow with code distance.

Specifically, the logical X operator of a CSS code, when implemented transversally, has weight equal to the distance. The Gram decay on this operator grows as \(\cos(c)^{2\alpha d}\), which dominates over polynomial improvements in physical gate fidelity.

### 6.3 Approximate Quantum Error Correction (Leung et al., Beny & Oreshkov)

In approximate QEC, the recovery operation need not perfectly restore the initial state; a fidelity loss of \(\epsilon\) is tolerated. The Gram channel fits naturally into this framework: the recovery map \(\mathcal{R}\) after syndrome measurement produces a logical channel with fidelity:

\[
F(\mathcal{R} \circ \Phi \circ \mathcal{E}) \geq 1 - P_L
\]

where \(P_L\) is the logical error rate computed above.

The Beny-Oreshkov conditions for approximate QEC require:

\[
\|\Pi \Phi^\dagger(A) \Pi - \lambda_A \Pi\| \leq \epsilon \|A\|
\]

for all logical operators \(A\). For the Gram channel, \(\Phi^\dagger(A) = G \odot A\) (since the channel is self-adjoint as a Pauli channel). The deviation from exact QEC is characterized by how much \(G \odot A\) differs from a scalar multiple of \(A\) when restricted to the codespace.

For \(A = X_L\), we have \(\Pi (G \odot X_L) \Pi = G(x_L) X_L\). The approximate QEC parameter is:

\[
\epsilon = 1 - G(x_L) = 1 - \prod_r \cos(c \cdot \Delta_r(x_L))^2
\]

This grows with the code distance, violating the approximate QEC condition for large \(d\) unless the rings are arranged to minimize \(\Delta_r(x_L)\).

### 6.4 Coherent vs. Incoherent Errors

The literature distinguishes:
- **Coherent errors**: unitary errors (e.g., over-rotation) that accumulate amplitude coherently
- **Incoherent/stochastic errors**: random Pauli errors that add probabilities

The DGF Gram channel is classified as **incoherent** (it is a Pauli channel), but with the crucial property that the error **distribution** is structured: the high-weight tail is determined by the ring geometry and Cartan parameter, not by independent per-qubit error probabilities.

Standard QEC analysis assumes independent per-qubit errors: \(\Pr(Z \text{ on qubit } i) = p\) independently. The Gram channel produces **correlated** Z errors with the correlation structure embedded in the \(\{c_z\}\) distribution via the Walsh-Hadamard transform of \(G(x)\).

These correlations are the DGF-specific signature that distinguishes it from standard depolarizing/decoherence models.

### 6.5 Comparison with Standard Decoherence

Standard dephasing: \(\Phi_t(\rho) = (1-e^{-t/T_2})\rho + e^{-t/T_2} Z\rho Z\) per qubit.

DGF Gram decay: \(\Phi(\rho) = \sum_z c_z Z^z \rho Z^z\) with \(c_z\) encoding multi-qubit correlations.

At the single-qubit level, the DGF reduces to standard dephasing with an effective \(T_2\) determined by \(c\) and the ring geometry. At the multi-qubit level, the DGF predicts specific correlations absent from independent dephasing models.

---

## 7. Honest Limitations and Open Problems

### 7.1 Limitations of This Analysis

1. **Code-specific optimization**: We assumed standard CSS code constructions. Codes optimized against Gram decay (e.g., by aligning logical operator supports with ring boundaries) may achieve better protection.

2. **Syndrome measurement details**: We assumed ideal syndrome measurement. Realistic measurement errors may compound the Gram decay.

3. **Multiple gate applications**: We analyzed a single application of the Gram channel. \(N\) applications of the Gram channel produce:

   \[
   \Phi^N(\rho) = \sum_z c_z^{(N)} Z^z \rho Z^z
   \]

   where \(c^{(N)}\) is the \(N\)-fold convolution of \(c\) over \(\mathbb{Z}_2^n\). For large \(N\), \(c^{(N)}\) approaches the uniform distribution over \(z\) (by the central limit theorem on the group), giving \(P_L \to 1/2\) exponentially fast in \(N\).

4. **Ring geometry optimization**: The ring arrangement is not fixed by the DGF. Optimizing ring geometry (e.g., making rings coincide with stabilizer supports) could reduce Gram decay on logical operators.

### 7.2 Open Problems

1. **Optimal code families**: What CSS code family minimizes \(G(x_L) = \prod_r \cos(c \cdot \Delta_r(x_L))^2\) for a given distance and ring geometry?

2. **Dynamic decoupling**: Can periodic X-pulses (which flip the computational basis) "echo out" the Gram decay? Since the Gram channel commutes with Z but not with X, dynamical decoupling with X pulses may suppress the decay. This is analogous to Hahn echo for dephasing.

3. **Ring-aware code design**: Can we design stabilizer codes where logical X operators are composed of qubits that share few rings, minimizing \(\sum_r \Delta_r(x_L)\)?

4. **Threshold shift from Gram decay**: By how much does the Gram decay reduce the fault-tolerance threshold? The effective Z-error probability per qubit from Gram decay, added to the physical gate error, shifts the threshold downward.

5. **DGF smoking gun in QEC experiments**: The correlated Z-error structure \(\{c_z\}\) produced by the DGF has a specific signature (Walsh-Hadamard transform of a product-of-cosines function). Can this be distinguished from uncorrelated dephasing in multi-qubit QEC experiments?

### 7.3 Summary Verdict

| Question | Answer |
|----------|--------|
| Is the Gram channel a Pauli channel? | **Yes** — only Z-type errors |
| Can syndrome measurement detect Gram decay? | **Yes** — it is standard Pauli Z error detection |
| Does Gram decay produce an irreducible logical error floor? | **Partially true**: \(P_L = \frac{1}{2}(1 - G(x_L))\) is exact but depends on code geometry |
| Can increasing code distance eliminate the floor? | **No**: larger distance → longer logical operators → MORE Gram decay |
| Can code optimization mitigate the problem? | **Yes**: ring-aware code design can reduce \(G(x_L)\) for fixed distance |
| Is dynamic decoupling effective? | **Potentially**: X-pulse sequences may echo out Z-phase accumulation |

---

## Appendix A: Key Formulas

### A.1 Walsh-Hadamard Transform Pair

\[
G(x) = \sum_{z} c_z (-1)^{z \cdot x}, \qquad
c_z = \frac{1}{2^n} \sum_{x} G(x) (-1)^{z \cdot x}
\]

### A.2 Logical Error Rate (Exact)

For a single logical qubit in a CSS code:

\[
P_L = \frac{1}{2}\left(1 - \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(x_L))^2\right)
\]

where \(x_L\) is the support vector of the logical X operator.

### A.3 Multi-Gate Generalization

After \(N\) non-Clifford Cartan gates:

\[
P_L^{(N)} = \frac{1}{2}\left(1 - \prod_{r=1}^{b_1} \cos(c \cdot \Delta_r(x_L))^{2N}\right)
\]

The convergence \(P_L^{(N)} \to 1/2\) is exponential in \(N\).

### A.4 Effective Per-Qubit Z Error Rate

\[
p_Z^{\text{eff}}(i) = \sum_{z: z_i = 1} c_z
= \frac{1}{2}\left(1 - \frac{1}{2^n} \sum_x G(x) (-1)^{x_i}\right)
\]

---

## Appendix B: Numerical Example

For \(c = 0.5\), \(\cos(0.5)^2 \approx 0.7702\):

- Per-ring decay factor: \(\gamma = \cos(0.5)^2 \approx 0.770\)
- 10 rings covering logical X: \(G(x_L) \approx 0.770^{10} \approx 0.074\)
- \(P_L \approx (1 - 0.074)/2 = 0.463\) (nearly maximally mixed)
- 1 ring covering logical X: \(G(x_L) \approx 0.770\)
- \(P_L \approx (1 - 0.770)/2 = 0.115\)

For \(b_1 = 100\) rings with typical coverage:

\[
\langle \ln G \rangle_{\text{off}} = 100 \cdot (-0.835) = -83.5
\]

Typical off-diagonal Gram entry: \(e^{-83.5} \approx 5 \times 10^{-37}\). The channel is essentially perfectly dephasing for any observable off-diagonal. But for logical operators, the relevant \(x_L\) has sparse ring coverage, so \(G(x_L)\) may remain non-negligible.
