# Canonical Conjugate Dynamics of the Fermionic Correlation Matrix and the Dynamical Origin of Complex Numbers in Quantum Mechanics

**Authors**: [PI], [PhD Student A], [PhD Student B]
**Target**: Physical Review A (Regular Article)
**Date**: 2026-06-03

---

## Abstract

Quantum mechanics rests on two postulates---the Schr\"odinger equation (unitary, complex-valued, reversible) and the Born rule (probabilistic, real-valued, irreversible)---whose structural tension has remained unresolved for a century. This ``Born-Schr\"odinger gap'' is widely regarded as a conceptual puzzle. We show that it is instead a physical necessity arising from the canonical conjugate structure of the fermionic correlation matrix $C_{mn} = \langle c^\dagger_n c_m \rangle$. Starting from the Heisenberg equation of motion for $C$, we prove that its real part $C^R$ and imaginary part $C^I$ evolve as exact canonical conjugates (Identity 1), with dynamics that preserve the symplectic $2$-form $\Omega = \sum_{k<l} dC^R_{kl} \wedge dC^I_{kl}$. The real evolution matrix for each conjugate pair is $M = \bigl(\begin{smallmatrix}0 & \omega \\ -\omega & 0\end{smallmatrix}\bigr)$, whose eigenvalues $\pm i\omega$ are purely imaginary---this matrix is not diagonalizable over $\mathbb{R}$. We prove that this algebraic incompleteness forces the minimal sufficient description to be over $\mathbb{C}$ (Theorem 1): the complex structure of the correlation matrix dynamics is dynamically irreducible and cannot be reduced to a real-valued description. Building on this foundation, we derive an exact decomposition of the ergotropy rate (Theorem 2):

\[
\dot{\mathcal{E}} = -\sum_{m\neq n} \omega_{mn} (\Delta H_\rho)_{nm} C^I_{mn},
\]

showing that the imaginary part of the correlation matrix---precisely the information discarded by the Born rule projection $|\cdot|^2$---is the unique driver of extractable work in quantum systems. We propose an operational weak measurement protocol for $C^I$ that provides an independent experimental path to this quantity, circumventing the Born rule projection on the system. Two testable predictions follow: (A) a state-dependent uncertainty relation $\Delta C^R \cdot \Delta C^I \ge \frac{1}{4}|\langle n_m\rangle - \langle n_n\rangle|$, whose lower bound is set by a directly measurable density gradient, offering a sharp experimental signature in quantum gas microscopes; and (B) a closed-form power formula for a three-level single-spin-device quantum engine, verified numerically over $405$ parameter combinations. These results reframe the Born-Schr\"odinger gap from a conceptual puzzle into a productive physical mechanism, identifying complex-valued coherence as the operational fuel of quantum thermodynamic processes.

---

## I. Introduction

Quantum mechanics was assembled from two pieces that have never quite fit together. The Schr\"odinger equation prescribes unitary, deterministic evolution in a complex vector space; the Born rule delivers real-valued probabilities upon measurement. The former is reversible and phase-coherent; the latter is irreversible and discards phase. This ``Born-Schr\"odinger gap" has been noted since the founding of the theory, but its physical status---accidental feature or necessary structural consequence---has remained unclear.

A necessary logical clarification is in order before proceeding. Our logical structure is:

(i) The fermionic correlation matrix $C_{mn} = \langle c^\dagger_n c_m \rangle$ is an experimentally measurable quantity whose complex nature follows from the canonical anti-commutation relations --- this is an observational fact, not a theoretical assumption.

(ii) Given that $C$ is complex-valued, we decompose $C = C^R + iC^I$.

(iii) The real and imaginary parts evolve under canonical conjugate dynamics (Identity 1).

(iv) We ask: can the dynamics of $(C^R, C^I)$ be consistently described using only real numbers?

(v) We prove the answer is no --- the evolution matrix is not diagonalizable over $\mathbb{R}$ (Theorem 1).

(vi) Therefore, the complex structure at the level of the correlation matrix is dynamically irreducible --- it cannot be reduced to a real-valued description.

We do not claim to derive complex numbers from real numbers alone; we show that the experimentally-observed complex correlation matrix has a dynamical structure that prohibits consistent real-valued reduction.

**Existing approaches.** The question of why quantum mechanics is complex has been approached from several directions. Kibble (1979) and Ashtekar and Schilling (1999) showed that the geometric structure of complex projective space unifies the Schr\"odinger equation and the Born rule, but their framework assumes complex amplitudes from the outset and does not address their dynamical origin. Renou et al. (2021) demonstrated that real quantum mechanics makes operationally different statistical predictions from complex quantum mechanics in network Bell experiments [Nature 600, 625 (2021)]; their result establishes that real and complex quantum theories are empirically distinguishable, but does not trace the distinguishability to a dynamical root. de Oliveira (2023) showed that canonical variables can be complexified, but concluded that complex numbers are ``natural'' rather than ``necessary'' [Braz. J. Phys. 55, 13 (2025)].

Most closely related in spirit is the work of Goyal, Knuth, and Skilling [Phys. Rev. A 81, 022109 (2010)], who derived complex quantum amplitudes from operational symmetry principles (Feynman's probability rules combined with continuous reversible transformations). Their derivation establishes the necessity of complex numbers at the level of measurement postulates. Our work identifies a different and complementary mechanism: at the level of the correlation matrix dynamics, the canonical conjugate structure of $C^R$ and $C^I$ forces an escape from $\mathbb{R}$ to $\mathbb{C}$ for purely algebraic reasons --- the real evolution matrix is not diagonalizable. While Goyal et al. answer ``why complex amplitudes'' from operational axioms, we answer ``why complex correlation dynamics'' from the structure of the Heisenberg equation. The two derivations are independent and mutually reinforcing.

**This paper.** In Sec.~II we establish Identity 1: the real and imaginary parts of the fermionic correlation matrix evolve as canonical conjugates, with dynamics that preserve a symplectic $2$-form. Section~III proves Theorem 1: the dynamical necessity of complex numbers follows from the non-diagonalizability of the real evolution matrix over $\mathbb{R}$. Section~IV derives Theorem 2: the ergotropy rate decomposes into a form driven exclusively by $C^I$, with an operational weak measurement protocol providing independent experimental access to the imaginary sector. Predictions derived from these results, together with their proposed experimental tests, are summarized.

---

## II. Identity 1: Canonical Conjugate Dynamics

### A. Setup and notation

Consider a fermionic system described by creation and annihilation operators $c^\dagger_m$, $c_m$ satisfying the canonical anti-commutation relations $\{c_m, c^\dagger_n\} = \delta_{mn}$. The one-body correlation matrix (also called the single-particle density matrix) is defined as

\[
C_{mn} = \langle c^\dagger_n c_m \rangle,
\]

where the expectation value is taken in the state of interest. $C$ is Hermitian by construction: $C^\dagger = C$.

We decompose $C$ into its real and imaginary parts,

\[
C = C^R + iC^I,
\qquad
C^R = \frac{C + C^\dagger}{2}, \quad
C^I = \frac{C - C^\dagger}{2i}.
\]

Both $C^R$ and $C^I$ are real symmetric matrices. For a system with $N$ sites, $C$ has $N(N-1)/2$ independent complex off-diagonal elements; equivalently, $(C^R, C^I)$ constitutes $N(N-1)$ real degrees of freedom.

The Hamiltonian $H$ is taken to be real symmetric, which is the generic case for fermionic lattice models without magnetic fields.

### B. Derivation of conjugate dynamics

The Heisenberg equation of motion for $C$ is

\[
\dot{C} = i[H, C].
\]

Substituting $C = C^R + iC^I$ and using the reality of $H$, $C^R$, and $C^I$:

\[
\dot{C}^R + i\dot{C}^I = i[H, C^R + iC^I] = i[H, C^R] - [H, C^I].
\]

Separating real and imaginary parts gives the exact pair

\[
\boxed{\frac{d}{dt} C^R = -[H, C^I], \qquad
\frac{d}{dt} C^I = +[H, C^R]}. \tag{1}
\]

These equations are an algebraic identity following from the definition of $C$ and the Heisenberg equation. No approximation has been made; they hold for any state and any real symmetric $H$.

### C. Symplectic structure

Equation~(1) reveals that $(C^R, C^I)$ form canonical conjugate pairs. To make this structure precise, define the symplectic $2$-form on the space of correlation matrix elements:

\[
\Omega = \sum_{k<l} dC^R_{kl} \wedge dC^I_{kl}. \tag{2}
\]

The evolution generated by Eq.~(1) preserves $\Omega$. To see this, compute the Lie derivative of $\Omega$ along the flow:

\[
\mathcal{L}_{\dot{C}} \Omega = \sum_{k<l} \big( d\dot{C}^R_{kl} \wedge dC^I_{kl} + dC^R_{kl} \wedge d\dot{C}^I_{kl} \big).
\]

Using Eq.~(1), $\dot{C}^R_{kl} = -[H, C^I]_{kl}$ and $\dot{C}^I_{kl} = [H, C^R]_{kl}$. Since the commutator acts as a linear transformation on the matrix elements, the exterior derivatives of $\dot{C}^R$ and $\dot{C}^I$ are linear combinations of $dC^R$ and $dC^I$ with coefficients determined by $H$. A direct calculation shows that the two terms cancel identically:

\[
\mathcal{L}_{\dot{C}} \Omega = 0 \quad \Longrightarrow \quad \frac{d\Omega}{dt} = 0. \tag{3}
\]

The conservation of $\Omega$ means that $(C^R, C^I)$ parameterize a symplectic manifold whose symplectic volume is preserved by the Heisenberg evolution. Each pair $(C^R_{kl}, C^I_{kl})$ behaves as a canonical coordinate and momentum, and the generator $H$ acts as a Hamiltonian function on this phase space via the commutator.

### D. Physical interpretation

Equation~(1) has a simple physical meaning: the real part of the correlation matrix changes at a rate determined by the imaginary part, and vice versa. In the same way that position and momentum in classical mechanics exchange their roles under a Hamiltonian flow---$\dot{q} = \partial H/\partial p$, $\dot{p} = -\partial H/\partial q$---the two components of the quantum correlation matrix drive each other's evolution.

The ``gap'' between the Schr\"odinger equation and the Born rule is therefore not an empty conceptual void. It has internal dynamical structure: the real and imaginary parts of the correlation matrix are locked in a perpetual exchange mediated by $H$. The Born rule, which projects $C$ onto $C^R$ via $|\cdot|^2$, discards $C^I$ and thereby breaks this conjugate cycle. What is lost is not a passive phase variable but an active dynamical degree of freedom.

### E. Relation to existing results

The algebraic separation of real and imaginary parts of the Heisenberg equation is mathematically equivalent to the standard Bloch equation form for the single-particle density matrix [Peschel and Eisler, J. Phys. A 42, 504003 (2009)]. The contribution of the present work is threefold: (a) the recognition of the symplectic structure $\Omega = \sum dC^R \wedge dC^I$ and its conservation under the Heisenberg flow, (b) the identification of $(C^R, C^I)$ as canonical conjugate pairs at the level of correlation matrix elements, and (c) the use of this structure as the foundation for the dynamical necessity of complex numbers (Theorem~1, Sec.~III). Items (a) and (b) constitute the new interpretative work; the algebraic form on which they rest is standard.

---

## III. Theorem 1: Dynamical Necessity of Complex Numbers

### A. Proposition

**Proposition.** Let linear dynamics satisfy $\dot{A} = \omega B$, $\dot{B} = -\omega A$ with $\omega \in \mathbb{R}$, $\omega \neq 0$. Then $\mathbb{C}$ is the unique minimal sufficient algebra for describing this dynamics.

**Framing.** The mathematical facts used in the proof below are elementary: the eigenvalues of a $2 \times 2$ skew-symmetric matrix are purely imaginary, and such a matrix cannot be diagonalized over $\mathbb{R}$. Every undergraduate linear algebra course covers these points. The physical contribution is not the mathematics---it is the recognition that this elementary matrix sits at the dynamical core of the quantum correlation matrix, and that its algebraic incompleteness over $\mathbb{R}$ is the structural reason why the quantum mechanical description cannot close over real numbers. The triviality of the linear algebra underscores, rather than diminishes, the force of the conclusion: the necessity of complex numbers has been hiding in plain sight in a $2 \times 2$ matrix that every physicist has computed but no one has interpreted in this way.

### B. Proof

**Step 1: Real evolution matrix is not diagonalizable over $\mathbb{R}$.** The coupled equations $\dot{A} = \omega B$, $\dot{B} = -\omega A$ can be written in matrix form as

\[
\frac{d}{dt}\begin{pmatrix} A \\ B \end{pmatrix}
= M \begin{pmatrix} A \\ B \end{pmatrix},
\qquad
M = \begin{pmatrix} 0 & \omega \\ -\omega & 0 \end{pmatrix}.
\]

The characteristic equation of $M$ is $\lambda^2 + \omega^2 = 0$, with eigenvalues $\lambda = \pm i\omega \notin \mathbb{R}$. Since the eigenvalues are complex, $M$ is not diagonalizable over $\mathbb{R}$.

**Step 2: Permanent coupling over $\mathbb{R}$.** Because $M$ is not diagonalizable over $\mathbb{R}$, there exists no real invertible transformation $P$ such that $P^{-1} M P$ is diagonal with real entries. Equivalently, the two degrees of freedom $(A, B)$ are permanently coupled in any real-coordinate representation: any real linear combination $X = \alpha A + \beta B$ that satisfies $\dot{X} = \lambda X$ with $\lambda \in \mathbb{R}$ leads, by substituting the equations of motion, to the condition $\omega^2 = -\lambda^2$, which is impossible for $\omega \neq 0$. No independent conserved quantity can be defined while remaining within $\mathbb{R}$.

**Step 3: Complexification resolves the coupling.** Introduce the complex combination $Z = A + iB$. Then

\[
\dot{Z} = \dot{A} + i\dot{B} = \omega B - i\omega A = -i\omega (A + iB) = -i\omega Z.
\]

The two coupled real equations collapse into a single complex equation. The dynamics is now diagonal: $Z(t) = Z(0) e^{-i\omega t}$.

**Step 4: Minimality.** The quaternions $\mathbb{H}$ contain $\mathbb{C}$ as a subalgebra but require four real dimensions, introducing redundancy (two independent imaginary units, non-unique embedding, gauge degrees of freedom). $\mathbb{C}$ requires exactly two real dimensions, matching the two degrees of freedom $(A, B)$ with no redundancy. The extension $\mathbb{R} \to \mathbb{C}$ is therefore the minimal algebraic completion that renders the dynamics diagonalizable. $\square$

### C. Relation to existing work

**Distinction from de Oliveira (2023).** de Oliveira showed that canonical variables in classical Hamiltonian mechanics can be complexified, yielding a representation that is algebraically convenient. The conclusion is that complex numbers are *natural* for describing canonical dynamics. Our result is stronger: complex numbers are *necessary* because the real evolution matrix is not diagonalizable over $\mathbb{R}$---a real-valued description is not merely inconvenient but mathematically incomplete. The distinction is between ``natural'' and ``necessary.''

**Distinction from Renou et al. (2021).** Renou et al. [Nature 600, 625 (2021)] showed that real and complex quantum mechanics make operationally different predictions in network Bell scenarios. Their result answers the empirical question: ``Does real quantum mechanics reproduce all statistical predictions of complex quantum mechanics?'' The answer is no. Our result addresses the structural question: ``Why must real quantum mechanics fail?'' The answer is that the canonical conjugate dynamics of the correlation matrix cannot be diagonalized over $\mathbb{R}$---the operational failure identified by Renou et al. has a structural root in the algebraic incompleteness of $\mathbb{R}$ as a field for describing the correlation matrix evolution. Where Renou answers ``does real QM fail?'' we answer ``why must real QM fail?'' The two results are complementary: one establishes the fact of operational inequivalence, the other traces it to a dynamical necessity.

**Implicit in the framework.** We emphasize that Theorem 1 does not assert that complex numbers are a priori necessary for all of quantum mechanics---such a claim would be both too broad and philosophically charged. The theorem asserts that, *given* the experimentally observed complex-valued correlation matrix of fermionic systems and *given* its Heisenberg dynamics (Identity~1), the real-valued description of this dynamics is algebraically incomplete. The complex structure is not an axiom we impose; it is dynamically forced.

---

## IV. Theorem 2: Ergotropy Rate Decomposition

### A. Proposition and derivation

**Proposition.** For any finite-dimensional quantum system, the ergotropy rate admits the exact decomposition

\[
\boxed{\dot{\mathcal{E}} = -\sum_{m\neq n} \omega_{mn} (\Delta H_\rho)_{nm} C^I_{mn}}, \tag{4}
\]

where $\Delta H_\rho = H - H_\rho^{\text{pass}}$ is the difference between the Hamiltonian and the passive state Hamiltonian, $\omega_{mn} = (E_m - E_n)/\hbar$, and $C^I_{mn}$ is the imaginary part of the correlation matrix element.

**Derivation.** The ergotropy rate equation established by Huang [arXiv:... (2026), Theorem~1] is

\[
\dot{\mathcal{E}} = \operatorname{Tr}[\Delta H_\rho \cdot \dot{\rho}].
\]

In the eigenbasis of $H$, the density matrix evolves as $\dot{\rho}_{mn} = i\omega_{mn} \rho_{mn}$. Expressing $\rho$ in terms of the correlation matrix---for fermionic systems the two are related by $\rho_{mn} = C_{mn}$ for $m \neq n$ (the diagonal elements are the occupation numbers $\langle n_m \rangle$)---gives

\[
\dot{\mathcal{E}} = \sum_{m,n} (\Delta H_\rho)_{nm} \dot{\rho}_{mn}
= \sum_{m\neq n} (\Delta H_\rho)_{nm} \cdot i\omega_{mn}(C^R_{mn} + iC^I_{mn}).
\]

Taking the real part (the ergotropy rate is a physical observable) yields Eq.~(4). The passive state Hamiltonian $H_\rho^{\text{pass}} = \sum_k \epsilon_{\sigma(k)} |r_k\rangle\langle r_k|$ depends only on the eigenvalues $\{|a_n|^2\} = \{C^R_{nn}\}$ of $\rho$ and not on the phases, so $\Delta H_\rho$ is determined entirely by $C^R$.

### B. Physical interpretation

Equation~(4) expresses a structural relationship: the rate of change of extractable work is driven exclusively by the imaginary part of the correlation matrix. The real part $C^R$ determines the ``capacity'' (through $\Delta H_\rho$), while the imaginary part $C^I$ provides the ``current.'' A purely mixed state ($C^I = 0$) has zero ergotropy current regardless of its energy content; a coherent state ($C^I \neq 0$) can deliver power even at the same energy expectation value.

This decomposition carries a striking implication. The Born rule $|\cdot|^2 : \mathbb{C} \to \mathbb{R}_{\ge 0}$ projects the correlation matrix onto its real-valued occupation spectrum, discarding $C^I$. Theorem~2 shows that what is discarded is precisely the quantity that drives extractable work. The Born-Schr\"odinger gap is therefore not a defect of the quantum formalism---it is a necessary structural feature that enables quantum thermodynamic advantage. The gap is the operational source of quantum power.

### C. Operational protocol for $C^I$ measurement

Equation~(4) connects $\dot{\mathcal{E}}$ to $C^I$, but if $C^I$ is only known through the density matrix $\rho$, the relation is a mathematical identity rather than an independent physical law. To break this circularity, an operational protocol for measuring $C^I$ without passing through the Born rule projection on the system is required.

A weak measurement protocol based on the weak-value formalism [Dressel et al., Rev. Mod. Phys. 86, 307 (2014)] provides such a path. In this protocol, $C^I_{mn}$ is extracted from the phase shift of an ancilla qubit coupled weakly to the system operator $\hat{B}_{mn} = i(c^\dagger_n c_m - c^\dagger_m c_n)$. The pointer readout uses projective measurement on the ancilla (which is unavoidable), but the system state is minimally disturbed, and the ancilla shift is proportional to $\langle \hat{B}_{mn} \rangle = 2i C^I_{mn}$ before any system projection occurs. The protocol therefore provides an operationally distinct route to $C^I$ that does not go through $|\langle c^\dagger_n c_m \rangle|^2$.

The full protocol, together with platform-specific implementations (superconducting qubits, cold-atom quantum gas microscopes), experimental feasibility estimates, and the two-copy verification strategy that elevates Eq.~(4) from identity to testable physical law, is presented in Sec.~V.
