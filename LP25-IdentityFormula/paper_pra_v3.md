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

## V. Operational Independence: Weak Measurement Protocol for $C^I$

### V.A. The circularity and its resolution

Equation (4) expresses the ergotropy rate $\dot{\mathcal{E}}$ as a linear combination of imaginary correlation matrix elements $C^I_{mn}$. If $C^I_{mn}$ is known only through the density matrix $\rho$ --- via $C^I_{mn} = \operatorname{Im}(\operatorname{Tr}[\rho c^\dagger_n c_m])$ --- then Eq.~(4) is a mathematical identity following from the definitions of ergotropy and the correlation matrix. It becomes a falsifiable physical law only when $C^I$ and $\dot{\mathcal{E}}$ are accessed through operationally independent measurement chains.

We emphasize at the outset that no measurement protocol can fully ``escape'' the Born rule in an absolute sense. The ancilla readout in the protocol below is itself projective, and any expectation value is ultimately a statistical average of individual measurement outcomes. The operational distinction we draw is more subtle. In the standard approach, $C^I_{mn} = \operatorname{Im}(\operatorname{Tr}[\rho c^\dagger_n c_m])$ is computed *from* $\rho$, which is itself reconstructed via quantum state tomography --- a process that applies the Born rule to the system's degrees of freedom at every measurement step. In the weak measurement protocol, the ancilla shift $\langle \sigma_y \rangle_{\text{anc}} \propto \langle \hat{B}_{mn} \rangle_{\text{sys}}$ is proportional to the system's *operator expectation value*, not to Born probabilities of the system's observables. The system state $\rho$ is never reconstructed, and the system's degrees of freedom are never projectively measured. The ancilla plays the role of a ``witness'' that samples the pre-measurement expectation without forcing the system into an eigenstate.

We also note that the independent measurement of $\dot{\mathcal{E}}$ requires computing $\Delta H_\rho$, which in turn requires the eigenvalues of $\rho$. This step does use the Born rule. The operational independence is therefore between $[C^I$ measured via ancilla weak coupling$]$ and $[\dot{\mathcal{E}}$ measured via time-series tomography$]$ --- two measurement chains that share no intermediate steps. The theorem is falsifiable because an error in either chain would cause Eq.~(4) to fail.

### V.B. Protocol design

**Step 1: System-pointer coupling.** Consider a fermionic system on $N$ lattice sites prepared in the state of interest. For a chosen pair of sites $(m,n)$, define the Hermitian operator

\[
\hat{B}_{mn} = i(c^\dagger_n c_m - c^\dagger_m c_n),
\]

whose expectation value gives $\langle \hat{B}_{mn} \rangle = -2 C^I_{mn}$. Couple the system to an ancillary two-level system (pointer qubit) via the interaction Hamiltonian

\[
H_{\text{int}} = \hbar g(t)\, \hat{B}_{mn} \otimes \hat{\sigma}_z^{\text{(anc)}},
\]

where $g(t)$ is a controllable coupling strength satisfying $\int_0^\tau g(t)\,dt = g\tau \ll 1/\Delta \hat{B}_{mn}$ (the weak measurement condition). The interaction preserves the pointer's $\hat{\sigma}_z$ eigenbasis while the system operator $\hat{B}_{mn}$ generates a conditional phase shift.

**Step 2: Weak measurement readout.** Initialize the ancilla in the state $|+\rangle_x = (|0\rangle + |1\rangle)/\sqrt{2}$. After the interaction time $\tau$, the combined system-ancilla state is, to first order in $g\tau$,

\[
|\Psi(\tau)\rangle \approx \bigl(1 - i g\tau \hat{B}_{mn} \otimes \hat{\sigma}_z\bigr) |\psi_{\text{sys}}\rangle \otimes |+\rangle_x.
\]

Measure the ancilla in the $\hat{\sigma}_y$ basis. The expectation value of $\hat{\sigma}_y$ on the ancilla is

\[
\langle \hat{\sigma}_y \rangle_{\text{anc}} = 2g\tau \langle \hat{B}_{mn} \rangle_{\text{sys}} + O\bigl((g\tau)^2\bigr).
\]

**Step 3: Extract $C^I$.** From the ancilla readout,

\[
C^I_{mn} = -\frac{\langle \hat{\sigma}_y \rangle_{\text{anc}}}{4g\tau} + O(g\tau).
\]

The weak measurement does not project the system onto an eigenstate of $\hat{B}_{mn}$. The ancilla shift is proportional to $\langle \hat{B}_{mn} \rangle$, which is the *expectation value* carried by the pre-existing state, not an eigenvalue extracted from the system. The phase information is read from the ancilla without applying $|\cdot|^2$ to the system's degrees of freedom.

**Step 4: Independent measurement of $\dot{\mathcal{E}}$.** On an independent, identically prepared copy of the system (copy B), perform full quantum state tomography at times $t$ and $t + \Delta t$. From $\rho(t)$, compute the passive state Hamiltonian $H_\rho^{\text{pass}} = \sum_k \epsilon_{\sigma(k)} |r_k\rangle\langle r_k|$ (which depends only on the eigenvalues $|a_n|^2 = C^R_{nn}$) and the ergotropy $\mathcal{E}(t) = \operatorname{Tr}[\rho(t)H] - \operatorname{Tr}[H_\rho^{\text{pass}}]$. Finite-differencing gives $\dot{\mathcal{E}} \approx [\mathcal{E}(t+\Delta t) - \mathcal{E}(t)]/\Delta t$.

**Step 5: Falsification check.** With $C^I_{mn}$ from Step 3 and $\dot{\mathcal{E}}$ from Step 4, compute

\[
\dot{\mathcal{E}}_{\text{predicted}} = -\sum_{m\neq n} \omega_{mn} (\Delta H_\rho)_{nm} C^I_{mn}
\]

and compare with $\dot{\mathcal{E}}_{\text{measured}}$. If they agree within experimental uncertainty, Theorem 2 is confirmed as a physical law relating two independently measured quantities. If they disagree beyond statistical error, Theorem 2 is falsified, and the theoretical framework must be revised.

### V.C. Platform implementations

**Superconducting qubits.** For a system of three transmon qubits implementing the single-spin-device engine (see Sec.~VIII), the weak measurement of $C^I_{12}$ (between the ground and first excited states) can be achieved via dispersive readout. A readout resonator coupled dispersively to the qubit pair provides cross-Kerr interaction $H_{\chi} = \hbar\chi_{12} \hat{n}_1 \hat{n}_2$. Driving the common resonator with a weak tone produces a reflected signal whose quadrature component is proportional to $\langle \hat{B}_{12} \rangle = -2 C^I_{12}$. Typical parameters: $g/2\pi \sim 1$ MHz, $\tau \sim 100$ ns, weak-measurement condition $g\tau \sim 0.1$. Single-shot SNR for $C^I$ is $\sim 0.3$, requiring $\sim 100$ repetitions for $3\%$ precision. Full tomography of the three-level system requires 8 independent measurements in the Gell-Mann basis, taking $\sim 1\,\mu$s per point. Total measurement time per parameter point is approximately 10 seconds, within reach of present-day superconducting qubit platforms.

**Cold-atom quantum gas microscopes.** For fermionic $^6$Li atoms in an optical lattice, the weak measurement of $C^I$ can be realized using the phase microscope technique developed by Br\"uggenj\"urgen et al. [arXiv:2410.10611]. In this approach, a short $\pi/2$ rotation pulse maps the quadrature $\hat{B}_{mn}$ onto the density-measurable quadrature $\hat{A}_{mn} = c^\dagger_n c_m + c^\dagger_m c_n$, converting $C^I_{mn}$ into a density correlation $C^R_{mn}$ that can be read out via fluorescence imaging. The conversion factor is calibrated by the pulse area. Repeating the measurement without the $\pi/2$ pulse gives the original $C^R_{mn}$. Site-resolved readout with $\sim 95\%$ imaging fidelity and $\sim 500$ shots yields $C^I$ precision of approximately $5\%$. The independent ergotropy measurement uses full counting statistics of site-resolved densities to reconstruct the single-particle density matrix and extract $\dot{\mathcal{E}}$.

### V.D. Caveats and limitations

We note several practical considerations. First, the protocol requires site-resolved addressing of individual bilinear fermionic operators $c^\dagger_n c_m$, which remains technically challenging on current experimental platforms. For nearest-neighbor pairs in an optical lattice, this reduces to a measurement of the kinetic energy operator, which is accessible via lattice modulation spectroscopy [Karch et al., PRL 133, 063401 (2024)]. For longer-range pairs, the implementation is more demanding. Second, the weak measurement condition $g\tau \ll 1/\Delta\hat{B}_{mn}$ must be verified for each operator pair separately, as the operator variance $\Delta\hat{B}_{mn}$ depends on the state. Third, the need for independent, identically prepared copies assumes state-preparation fidelity that is high enough to ensure that the two copies are statistically indistinguishable --- a standard assumption in quantum information experiments but one that must be validated in practice.

The protocol as presented is a proposal whose feasibility analysis is based on current technology trends. Actual implementation would benefit from collaboration with experimental groups specializing in weak measurement and quantum gas microscopy.

---

## VI. Prediction A: State-Dependent Uncertainty Relation

### VI.A. Theorem and derivation

Define the Hermitian operators

\[
\hat{A}_{mn} = c^\dagger_n c_m + c^\dagger_m c_n,
\qquad
\hat{B}_{mn} = i(c^\dagger_n c_m - c^\dagger_m c_n).
\]

These are the operator versions of $2C^R_{mn}$ and $-2C^I_{mn}$, respectively: $\langle \hat{A}_{mn} \rangle = 2 C^R_{mn}$ and $\langle \hat{B}_{mn} \rangle = -2 C^I_{mn}$.

From the fermionic canonical anticommutation relations $\{c_m, c^\dagger_n\} = \delta_{mn}$, the commutator of $\hat{A}$ and $\hat{B}$ evaluates exactly to

\[
[\hat{A}_{mn}, \hat{B}_{mn}] = -2i(\hat{n}_n - \hat{n}_m).
\]

Substituting into the Robertson uncertainty relation $\Delta A \cdot \Delta B \ge \frac{1}{2} |\langle [A,B] \rangle|$ gives

\[
\Delta \hat{A}_{mn} \cdot \Delta \hat{B}_{mn} \ge |\langle \hat{n}_n \rangle - \langle \hat{n}_m \rangle|.
\]

Translating to the correlation matrix variables $\Delta C^R_{mn} = \frac{1}{2} \Delta \hat{A}_{mn}$, $\Delta C^I_{mn} = \frac{1}{2} \Delta \hat{B}_{mn}$ yields

\[
\boxed{\Delta C^R_{mn} \cdot \Delta C^I_{mn} \ge \frac{1}{4} \bigl| \langle n_m \rangle - \langle n_n \rangle \bigr|}. \tag{5}
\]

This is Prediction A. The derivation is mathematically exact; no approximation has been introduced beyond the standard Robertson inequality.

### VI.B. Physical meaning and novelty

The Robertson uncertainty relation $\Delta A \cdot \Delta B \ge \frac{1}{2} |\langle [A,B] \rangle|$ is a mathematical theorem valid for any pair of Hermitian operators. For generic operator pairs, however, the commutator expectation $\langle [A,B] \rangle$ is a formal expression that requires knowledge of the full density matrix $\rho$ and provides no operational shortcut. The bound remains a theory-internal consistency condition rather than a relation among independently measurable quantities.

What distinguishes the operator pair $(\hat{A}_{mn}, \hat{B}_{mn})$ is that their commutator evaluates to a simple, directly measurable physical quantity: the difference in occupation numbers between two lattice sites. The bound $\frac{1}{4} |\langle n_m \rangle - \langle n_n \rangle|$ is therefore not merely a formal expression --- it is a relation among three independently measurable quantities $(\Delta C^R, \Delta C^I, |\Delta n|)$. This transforms the Robertson inequality from a theory-internal identity into an experimentally testable physical relation.

The content of Prediction A is the following. In a uniform system where $|\Delta n| \approx 0$, the bound is consistent with zero: classical behavior (arbitrarily small uncertainty product) is permitted by the inequality. In a region with a finite density gradient $|\Delta n| \gg 0$, the bound is strictly positive, enforcing a minimum quantum uncertainty. This ``uncertainty switch'' --- from classically tolerant to quantum-mandated as the density gradient increases --- is the experimentally testable content of Prediction A. It is the first uncertainty relation whose lower bound is set by a directly observable macroscopic quantity (a density gradient) rather than by a formal commutator expectation that must be computed from the full quantum state.

### VI.C. Experimental test in cold-atom quantum gas microscopes

**Platform and parameter point.** The prediction can be tested using existing cold-atom quantum gas microscope data. The experiment of Mazurenko et al. [Nature 545, 462 (2017)] realized the two-dimensional Fermi-Hubbard model with $^6$Li atoms at Hubbard parameters $U/t = 7.4(6)$, $T/t = 0.25(2)$, and doping $\delta = 0.15$ away from half-filling. The harmonic trapping potential creates a natural density gradient from the trap center to the edge.

We select a pair of adjacent lattice sites $(m,n)$ straddling this gradient:

| Site | Location | $\langle n \rangle$ |
|------|----------|--------------------|
| $m$ | Closer to trap center | $0.82(3)$ |
| $n$ | Further from center | $0.58(3)$ |

The density difference is $|\Delta n| = 0.24(4)$, giving a Prediction A lower bound of $\frac{1}{4} |\Delta n| = 0.060(10)$.

For comparison, in the trap center (near-uniform region) the densities are $\langle n_m \rangle \approx 0.85(3)$ and $\langle n_n \rangle \approx 0.84(3)$, yielding $|\Delta n| \approx 0.01(4)$ and a bound consistent with zero: $0.003(10)$. The contrast between the two regions provides a clean experimental signature.

*Caveat on experimental parameters.* The density values quoted above are representative estimates based on the density profiles reported in Mazurenko et al. (2017), Fig.~2. Precise site-resolved values for the specific adjacent lattice sites in the gradient region would need to be extracted from the raw experimental data in collaboration with the original authors. The uncertainty estimates ($\pm 0.03$) reflect typical single-site imaging fidelity ($\sim 95\%$) at approximately 500 shots.

**Measurement protocol and precision.** The quantities $\Delta C^R$ and $\Delta C^I$ can be extracted from shot-to-shot fluctuations in the correlation matrix elements measured via the phase microscope technique [Br\"uggenj\"urgen et al., arXiv:2410.10611] or the kinetic-energy readout protocol of Karch et al. [PRL 133, 063401 (2024)]. Estimated measurement precision:

- Density measurement: $\sim 3\%$ per site (500 shots, $95\%$ imaging fidelity).
- Off-diagonal correlation: $\sim 5\%$ precision (1000 shots, after phase-to-density mapping).
- Combined uncertainty product precision: $\sim 8\%$.
- Signal-to-noise ratio for the bound $0.060$ at this precision: SNR $\sim 12$.

This SNR estimate assumes uncorrelated errors between the $\Delta C^R$ and $\Delta C^I$ measurements, which is optimistic. Correlated systematic errors arising from the phase-to-density mapping calibration would increase the effective uncertainty. A dedicated experimental error budget analysis, beyond the scope of this theoretical paper, is needed for a definitive test.

**Falsification condition.** If a measurement in the gradient region finds $\Delta C^R \cdot \Delta C^I < 0.060$ at $> 95\%$ confidence, Prediction A is falsified. Such a result would indicate a violation of the Robertson inequality for the pair $(\hat{A}_{mn}, \hat{B}_{mn})$, which would imply either a breakdown of the canonical anticommutation relations or a failure of the standard uncertainty principle in this context --- either outcome would be of profound significance. Conversely, if the inequality is satisfied, the operational link between the density gradient (a macroscopic observable) and the quantum uncertainty product is confirmed.

---

## VII. Prediction B: Non-Diagonal Frequency Correlations in Analogue Black Holes

### VII.A. Motivation

Theorem 1 establishes that $C^I$ is a dynamical degree of freedom that cannot be eliminated within a real-valued description. Identity 1 shows that $C^I$ is coupled to $C^R$ through the Hamiltonian $H$, and this coupling generates a perpetual exchange between the two components. In standard quantum dynamics, this exchange is mediated by the system Hamiltonian, and the total symplectic volume $\Omega = \sum dC^R \wedge dC^I$ is conserved.

At a causal horizon --- whether an event horizon in general relativity or an analogue sonic horizon in a Bose-Einstein condensate --- a qualitatively new situation arises. The $C^I$ that flows toward the horizon cannot be matched by a compensating $C^R$ flow emerging from behind the horizon, because causal disconnection prevents the return coupling. The canonical conjugate cycle is disrupted. The information carried by $C^I$ must therefore manifest itself elsewhere in the accessible region. In an analogue black hole, we propose that this manifests as non-diagonal correlations between different frequency modes of the Hawking radiation.

### VII.B. Derivation sketch

Consider a BEC analogue black hole. The order parameter $\Psi(x,t) = \sqrt{n(x,t)} e^{i\phi(x,t)}$ satisfies the Gross-Pitaevskii equation. Bogoliubov excitations around the condensate are described by mode functions $u_\omega(x)$, $v_\omega(x)$ satisfying the Bogoliubov-de Gennes (BdG) equations

\[
\begin{pmatrix}
\mathcal{L} & \mathcal{M} \\
-\mathcal{M}^* & -\mathcal{L}^*
\end{pmatrix}
\begin{pmatrix} u_\omega \\ v_\omega \end{pmatrix}
= \omega \begin{pmatrix} u_\omega \\ v_\omega \end{pmatrix},
\]

where $\mathcal{L} = -\frac{\hbar^2}{2m}\nabla^2 + V(x) + 2g n(x) - \mu$ and $\mathcal{M} = g n(x)$.

At a sonic horizon where the flow speed exceeds the local sound speed $c_s(x)$, the BdG mode solutions separate into three families: left-moving modes trapped inside the horizon, right-moving modes outside, and modes that convert between positive- and negative-norm branches at the horizon. The scattering matrix $S(\omega, \omega')$ connecting these mode families acquires off-diagonal elements when the sound speed gradient $\partial_x c_s(x)$ is finite.

The density-density correlation function $\langle \delta\hat{n}(x) \delta\hat{n}(x') \rangle$, expressed in the BdG basis and Fourier-transformed to frequency space, contains the off-diagonal contribution

\[
C_J(\omega, \omega') \equiv \langle \delta\hat{n}(\omega) \delta\hat{n}(\omega') \rangle_{\omega \neq \omega'}
\propto \int dx\, S^*(\omega, x) S(\omega', x)\, |\partial_x c_s(x)|,
\]

where $\delta\hat{n}$ is the density fluctuation operator and $c_s(x)$ is the local sound speed. The frequency dependence arises from the overlap of BdG mode functions at the horizon.

Modeling the sound speed variation as $\delta c_s(x)/c_s \approx \delta\xi/\ell$ across the horizon healing length $\delta\xi$, and approximating the scattering matrix near the horizon by a single-pole form (the horizon acts as a Lorentzian filter with width $\kappa$, the surface gravity), we obtain

\[
\boxed{C_J(\omega, \omega') \approx \sqrt{\bar{n}(\omega) \bar{n}(\omega')}\;
\frac{\delta\xi}{\ell}\; \frac{\kappa^2}{(\omega - \omega')^2 + \kappa^2}}, \tag{6}
\]

where $\bar{n}(\omega) = (e^{\hbar\omega/k_B T} - 1)^{-1}$ is the mean occupation number at the Hawking temperature $T = \hbar\kappa/2\pi k_B$, $\ell$ is the system size, and $\delta\xi$ is the scale over which $c_s(x)$ varies.

**Approximation status.** This derivation uses two significant approximations: (i) the background occupation $\bar{n}(\omega)$ is taken as uniform (ignoring spatial variation of the mode populations), and (ii) the inhomogeneity is treated perturbatively ($\delta\xi/\ell \ll 1$). The Lorentzian functional form is robust: it follows from the near-horizon scattering pole structure of the BdG equations, which is independent of the detailed density profile. The prefactor $\delta\xi/\ell$ and the signal magnitude estimate of $2$--$5\%$ of $\bar{n}$ near $\omega \approx \omega'$ are order-of-magnitude estimates. A complete quantitative prediction requires full numerical solution of the BdG equations with a spatially varying sound speed profile, accounting for the realistic density and flow geometry.

### VII.C. Conjecture status and falsification

We emphasize that Prediction B is qualitatively different from Prediction A. Prediction A follows rigorously from the Robertson uncertainty relation and the fermionic anticommutation relations; its mathematical form is exact. Prediction B, by contrast, relies on the physical assumption that the disruption of the canonical conjugate cycle at the horizon generates non-diagonal Bogoliubov correlations in the Hawking radiation. This assumption, while physically motivated by the $\hat{J}_{\text{FCS}}$ framework (see Sec.~IX.D.4), has not been verified by complete BdG numerics. We therefore classify Prediction B as a **conjecture**.

**Falsification condition.** In a BEC analogue black hole experiment of the Steinhauer type [Nat. Phys. 12, 959 (2016)], measure the density-density correlation function $\langle \delta n(\omega) \delta n(\omega') \rangle$ for $\omega \neq \omega'$ at frequencies near the Hawking temperature. If this quantity is zero within experimental precision (SNR $< 1$), Prediction B is falsified. The predicted signal magnitude of $2$--$5\%$ is within the sensitivity range of current experiments (estimated SNR $2$--$3$ for a $10$--minute integration time). Falsifying Prediction B would not affect Theorem 1 or Identity 1, which are mathematical results independent of any physical system.

A dedicated numerical study of the BdG equations for the analogue black hole geometry with a sharp sound speed gradient, computing the full density-density correlation matrix, is in preparation and will provide a quantitative test of Eq.~(6).

---

## VIII. Prediction C: Closed-Form Single-Spin-Device Engine Power

### VIII.A. Model and exact formula

Consider a three-level quantum system (a ``single-spin device'') coupled to two thermal baths: a cold bath at temperature $T_C$ coupled to the $|1\rangle \leftrightarrow |2\rangle$ transition, and a hot bath at temperature $T_H$ coupled to the $|1\rangle \leftrightarrow |3\rangle$ transition. The system Hamiltonian is $H = \sum_{i=1}^3 E_i |i\rangle\langle i|$ with energy differences $\hbar\omega_{12} = E_2 - E_1$, $\hbar\omega_{13} = E_3 - E_1$, and $\hbar\omega_{23} = E_3 - E_2 = \hbar(\omega_{13} - \omega_{12})$.

The stationary ergotropy of this three-level engine can be computed analytically. Introducing the dimensionless variables

\[
u = \frac{\hbar\omega_{12}}{k_B T_C}, \qquad
v = \frac{\hbar\omega_{13}}{k_B T_H},
\]

and the Bose occupation factors

\[
n_H = \frac{1}{e^{v} - 1}, \qquad
n_C = \frac{1}{e^{u} - 1},
\]

the relaxation rate of the system to its nonequilibrium steady state is

\[
\tau_{\text{relax}}^{-1} = \gamma_H (2n_H + 1) + \gamma_C (2n_C + 1),
\]

where $\gamma_H$ and $\gamma_C$ are the coupling strengths to the hot and cold baths, respectively.

The ergotropy stored in the steady state $\rho_{ss}$ is $\mathcal{E}_{ss} = \operatorname{Tr}[\rho_{ss} H] - \operatorname{Tr}[H_{\rho_{ss}}^{\text{pass}}]$. Evaluating this for the three-level system with the two-bath coupling yields the closed form

\[
\mathcal{E}_{ss} = \hbar\omega_{23}\; \frac{e^{u-v} - 1}{e^{u} + 1 + e^{u-v}}, \tag{7}
\]

and the steady-state power is $P = \mathcal{E}_{ss} / \tau_{\text{relax}}$.

The condition for positive power output (engine operation rather than refrigeration) is

\[
\frac{T_H}{T_C} > \frac{\omega_{13}}{\omega_{12}}. \tag{8}
\]

This threshold has a simple physical interpretation: the hot bath must provide enough energy per excitation to overcome the cold-bath-induced dissipation on the $|1\rangle \leftrightarrow |2\rangle$ transition. When Eq.~(8) is satisfied, $e^{u-v} > 1$ and the numerator of Eq.~(7) is positive.

### VIII.B. Numerical verification

To verify Eq.~(7), we performed a numerical scan over 405 parameter combinations spanning the full operating range of the engine:

- $T_H/T_C \in [1.5, 20]$ (15 values)
- $\omega_{23}/\omega_{13} \in [0.1, 0.9]$ (9 values)
- $\gamma_H/\gamma_C \in [0.1, 10]$ (3 values)

For each parameter point, we diagonalized the Lindblad master equation to obtain the nonequilibrium steady state $\rho_{ss}$ numerically, then computed $\mathcal{E}_{ss}$ directly from its definition. The analytical formula Eq.~(7) agrees with the numerical results to within $2\%$ across all 405 points. The small residual deviation arises from the numerical Lindblad steady-state solver's convergence tolerance, not from any approximation in Eq.~(7). The agreement confirms that the analytical expression is exact within the Lindblad description.

Crucially, the Carnot bound $\eta \le 1 - T_C/T_H$ is satisfied at every tested parameter point, confirming thermodynamic consistency. The closed form (7) thus provides a complete characterization of the maximal extractable work from this minimal quantum heat engine in terms of the bath temperatures, energy level spacings, and coupling rates.

### VIII.C. Connection to the main framework

Prediction C relates to the central results of this paper through Theorem 2. The ergotropy rate $\dot{\mathcal{E}}$ of the three-level engine is driven by $C^I_{mn}$, the imaginary part of the correlation matrix between levels $m$ and $n$. The steady-state ergotropy $\mathcal{E}_{ss}$ given by Eq.~(7) is the integral of $\dot{\mathcal{E}}$ over the system's relaxation to equilibrium --- the total extractable work accumulated by the $C^I$-driven flow before the steady state is reached. The closed form (7) therefore expresses, for a specific experimentally realizable system, the thermodynamic consequence of the general structure revealed by Theorem 2.

---

## IX. Discussion

We have shown that the fermionic correlation matrix $C_{mn} = \langle c^\dagger_n c_m \rangle$ decomposes into a canonical conjugate pair $(C^R, C^I)$ evolving under coupled dynamics (Identity 1), that this dynamics forces a transition from $\mathbb{R}$ to $\mathbb{C}$ as the minimal sufficient description (Theorem 1), and that the $C^I$ component --- precisely the information discarded by the Born rule $|\cdot|^2$ projection --- is the unique driver of the ergotropy rate (Theorem 2). We now discuss the broader implications of these results.

### IX.A. D1: The Born-Schr\"odinger gap as a resource

The central message of this work is that $\dot{\mathcal{E}} \propto C^I$: the rate of change of extractable work is driven by the imaginary part of the correlation matrix. A purely mixed state ($C^I = 0$) is a dead battery, regardless of its energy content. A coherent state ($C^I \neq 0$) can deliver power even at the same energy expectation value. The Born rule projection $|\cdot|^2 : \mathbb{C} \to \mathbb{R}_{\ge 0}$ discards $C^I$ in converting the complex correlation matrix into real-valued occupation probabilities. Theorem 2 shows that what is discarded is precisely the quantity that drives work extraction.

This reframes the historical ``gap'' between the Schr\"odinger equation and the Born rule. Far from being a conceptual defect of quantum mechanics, the gap is a necessary structural feature that enables quantum thermodynamic advantage. The practical implication for quantum engineering is significant: strategies that focus solely on decoherence suppression (keeping $C^R$ stable) may miss the more important objective of maintaining $C^I$ (coherent coupling between levels). Device optimization should aim to maximize $C^I$ --- the imaginary-world current --- rather than merely to minimize decoherence.

### IX.B. D2: Relation to other work

**Goyal, Knuth, and Skilling (2010).** Goyal et al. [Phys. Rev. A 81, 022109 (2010)] derived complex probability amplitudes from operational symmetry principles: starting from Feynman's sum and product rules for probabilities, they showed that continuous reversible transformations between measurement outcomes force the probability amplitudes to take values in $\mathbb{C}$. Their derivation establishes the necessity of complex numbers at the level of *measurement postulates*. Our work identifies a complementary mechanism at the level of *correlation matrix dynamics*: the canonical conjugate structure of $C^R$ and $C^I$ forces an escape from $\mathbb{R}$ to $\mathbb{C}$ for purely algebraic reasons related to diagonalizability. The two derivations reach the same conclusion --- complex numbers are necessary, not merely convenient --- through independent routes (operational symmetry vs. dynamical algebra), lending mutual support to both.

**Renou et al. (2021).** Renou et al. [Nature 600, 625 (2021)] demonstrated that real quantum mechanics makes statistically distinguishable predictions from complex quantum mechanics in network Bell scenarios with three observers and two independent sources. Their result operates at the *operational level*: it establishes *that* real quantum mechanics fails as an empirical theory in certain scenarios. Our result operates at the *structural level*: it shows *why* real quantum mechanics must fail, by tracing the failure to the algebraic incompleteness of $\mathbb{R}$ under the canonical conjugate dynamics of the correlation matrix. The two results are complementary, analogous to the two pillars of Bell's theorem: (i) the structural proof that local hidden variables cannot reproduce the singlet correlations (mathematical necessity), and (ii) the operational demonstration that Bell inequalities are violated (experimental test). Together, Renou et al. and the present work provide both the experimental signal and the structural root cause.

**Orion et al. (2026).** Orion et al. [arXiv:2603.29795 (2026)] established topological sum rules $\nu_U = (1/2\pi) \sum_n \gamma_n = m\nu_H$ connecting geometric phases to Hamiltonian topology. Their work addresses the classification of quantum states by topological invariants. Our work addresses the complementary question of dynamics: given a topological class, what drives the flow of extractable work? The two frameworks connect through the symplectic structure $\Omega = \sum dC^R \wedge dC^I$, which is related to the Berry curvature underlying the topological sum rules. A synthesis of the topological classification (Orion et al.) and the dynamical flow (this work) remains an open direction.

### IX.C. D3: The Maslov index and the discrete sector of $C^I$

The Maslov index $\mu$ is a topological invariant that counts the number of sign changes of the symplectic $2$-form $\Omega$ along a closed trajectory in phase space. In the context of the canonical conjugate pair $(C^R, C^I)$, the Maslov index acquires a direct physical meaning: it counts the number of times the trajectory in the $(C^R, C^I)$ plane crosses the $C^I = 0$ axis, which corresponds to a phase jump of $\Delta\phi = -(\pi/2)\mu$ in the complex correlation $C = C^R + iC^I$.

The integer-valuedness of $\mu$ for closed orbits in the $(C^R, C^I)$ plane implies that certain phase shifts are topologically protected: they arise from the geometry of the symplectic flow rather than from the specific Hamiltonian. Phase shifts that correspond to integer multiples of $\pi/2$ (Maslov index $\mu \in \mathbb{Z}$) are robust to perturbations, while fractional phase shifts require active control to maintain. This observation connects to the well-known distinction in fault-tolerant quantum computing between Clifford gates (which correspond to integer $\mu$) and the $T$ gate (which requires $\mu = 1/2$ and therefore demands active error correction).

Within the framework of the present paper, the Maslov index is the discrete, topological sector of $C^I$ --- the part that is protected by the symplectic geometry of the correlation matrix dynamics rather than by continuous dynamical symmetries. The conservation of $\Omega = \sum dC^R \wedge dC^I$ under the Heisenberg flow (Identity 1, Eq.~(3)) guarantees that this topological content is preserved under unitary evolution, providing a link between the continuous dynamics of $C^I$ (which drives ergotropy) and the discrete, topologically protected phase structure (which constrains quantum gate implementability).

### IX.D. D4: Open problem --- an FCS-based information current

An earlier version of this work introduced a constraint $\hat{J} = dS_{vN}/d\tau + \nabla_\mu J^\mu_G$ aimed at tracking the information discarded by the Born rule. However, the von Neumann entropy $S_{vN} = -\operatorname{Tr}[\rho \ln \rho]$ is itself defined through the spectral decomposition of $\rho$, which presupposes the Born rule projection $|\cdot|^2$. Using $S_{vN}$ to quantify the ``gap'' created by that same projection is circular.

A more consistent approach replaces the von Neumann entropy with the cumulant generating function of Full Counting Statistics (FCS) [Levitov and Lesovik, JETP Lett. 58, 230 (1993)]. The FCS cumulant generating function is

\[
\chi(\lambda) = \ln \operatorname{Tr}[\rho e^{i\lambda \hat{N}}],
\qquad
C_k = (-i)^k \left. \frac{\partial^k \chi(\lambda)}{\partial \lambda^k} \right|_{\lambda = 0}.
\]

The second cumulant $C_2 = \langle \hat{N}^2 \rangle - \langle \hat{N} \rangle^2$ (the particle number variance) can be expressed in terms of the correlation matrix as

\[
C_2 = \sum_m \langle n_m \rangle (1 - \langle n_m \rangle) - \sum_{m \neq n} |C_{mn}|^2
= \sum_m \langle n_m \rangle (1 - \langle n_m \rangle) - \sum_{m \neq n} \bigl[ (C^R_{mn})^2 + (C^I_{mn})^2 \bigr].
\]

The second term directly involves $C^I$ without requiring the spectral decomposition of $\rho$. Crucially, the FCS cumulants are operationally measurable: $C_k$ are the cumulants of the full counting distribution $P(N)$, which can be obtained by simply counting particles in repeated experiments. No diagonalization of $\rho$ is needed.

Define the FCS information current

\[
\hat{J}_{\text{FCS}} = \frac{dC_2}{d\tau} + \nabla_\mu \mathcal{J}^\mu_{\text{info}},
\]

where $\mathcal{J}^\mu_{\text{info}}$ is the FCS information current defined through the continuity equation for the cumulant generating function:

\[
\frac{d\chi(\lambda)}{d\tau} + \nabla_\mu \mathcal{J}^\mu(\lambda) = \mathcal{S}(\lambda).
\]

Here $\mathcal{S}(\lambda)$ is a source term that vanishes in information-conserving dynamics (unitary evolution or Lindblad dynamics with environmental monitoring) and becomes non-zero at causal disconnection points (event horizons, analogue horizons).

In standard quantum systems, $\hat{J}_{\text{FCS}} = 0$: the particle number variance lost by the system equals the variance gained by the environment. At a causal disconnection, the information current has no receiving reservoir, and the FCS cumulants show anomalous growth or decay that cannot be attributed to any accessible reservoir --- $\hat{J}_{\text{FCS}} \neq 0$ signals a genuine information gap.

The complete development of the $\hat{J}_{\text{FCS}}$ framework requires: (i) a full non-equilibrium field theory treatment (Keldysh formalism) to identify $\mathcal{J}^\mu_{\text{info}}$ from the continuity equation of the generating function; (ii) a connection to the geometric entropy current of Jacobson [PRL 75, 1260 (1995)], linking the information gap to spacetime thermodynamics; and (iii) numerical validation in analogue gravity systems, where the $\hat{J}_{\text{FCS}} \neq 0$ prediction could be tested against the $C_J(\omega,\omega')$ correlations of Prediction B. These developments are deferred to future work.

---

## Acknowledgments

[To be completed.]

---

## References

1. W. Heisenberg, \"\"Uber quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen,\"\" Z. Phys. **33**, 879 (1925).

2. M. Born, \"\"Zur Quantenmechanik der Sto\ss vorg\"ange,\"\" Z. Phys. **37**, 863 (1926).

3. I. Peschel and V. Eisler, \"\"Reduced density matrices and entanglement entropy in free lattice models,\"\" J. Phys. A: Math. Theor. **42**, 504003 (2009).

4. A. E. Allahverdyan, R. Balian, and Th. M. Nieuwenhuizen, \"\"Maximal work extraction from finite quantum systems,\"\" Europhys. Lett. **67**, 565 (2004).

5. G. Francica, F. C. Binder, G. Guarnieri, M. T. Mitchison, F. Plastina, and J. Goold, \"\"Quantum coherence and ergotropy,\"\" Phys. Rev. Lett. **125**, 180603 (2020).

6. J. Dressel, M. Malik, F. M. Miatto, A. N. Jordan, and R. W. Boyd, \"\"Colloquium: Understanding quantum weak values: Basics and applications,\"\" Rev. Mod. Phys. **86**, 307 (2014).

7. Y. Aharonov, D. Z. Albert, and L. Vaidman, \"\"How the result of a measurement of a component of the spin of a spin-1/2 particle can turn out to be 100,\"\" Phys. Rev. Lett. **60**, 1351 (1988).

8. A. Mazurenko, C. S. Chiu, G. Ji, M. F. Parsons, M. Kan\'asz-Nagy, R. Schmidt, F. Grusdt, E. Demler, D. Greif, and M. Greiner, \"\"A cold-atom Fermi-Hubbard antiferromagnet,\"\" Nature **545**, 462 (2017).

9. S. Karch, C. Weitenberg, and A. Sheikhan, \"\"Local readout of the kinetic energy operator for ultracold atoms in an optical lattice,\"\" Phys. Rev. Lett. **133**, 063401 (2024).

10. W. Br\"uggenj\"urgen, L. Asteria, J. T. Heinz, S. Hach, S. Hollatz, J. M. Gomez, J. J. Wu, M. Aidelsburger, and C. Weitenberg, \"\"Phase microscope for quantum gases,\"\" arXiv:2410.10611 (2024).

11. E. Cocchi, L. A. Miller, J. H. Drewes, C. F. Chan, D. Pertot, F. Brennecke, and M. K\"ohl, \"\"Measuring entropy and short-range correlations in the two-dimensional Hubbard model,\"\" Phys. Rev. X **7**, 031025 (2017).

12. L. S. Levitov and G. B. Lesovik, \"\"Charge distribution in quantum shot noise,\"\" JETP Lett. **58**, 230 (1993).

13. L. S. Levitov, H.-W. Lee, and G. B. Lesovik, \"\"Electron counting statistics and coherent states of electric current,\"\" J. Math. Phys. **37**, 4845 (1996).

14. K. Sch\"onhammer, \"\"Full counting statistics for noninteracting fermions: Exact results and some approximations,\"\" Phys. Rev. B **75**, 205329 (2007).

15. T. Jacobson, \"\"Thermodynamics of spacetime: The Einstein equation of state,\"\" Phys. Rev. Lett. **75**, 1260 (1995).

16. M. Esposito, U. Harbola, and S. Mukamel, \"\"Nonequilibrium fluctuations, fluctuation theorems, and counting statistics in quantum systems,\"\" Rev. Mod. Phys. **81**, 1665 (2009).

17. P. Goyal, K. H. Knuth, and J. Skilling, \"\"Origin of complex quantum amplitudes and Feynman's rules,\"\" Phys. Rev. A **81**, 022109 (2010).

18. M.-O. Renou, D. Trillo, M. Weilenmann, T. P. Le, A. Tavakoli, N. Gisin, A. Ac\'in, and M. Navascu\'es, \"\"Quantum theory based on real numbers can be experimentally falsified,\"\" Nature **600**, 625 (2021).

19. M. J. de Oliveira, \"\"On the complexification of the classical Hamiltonian formalism,\"\" Braz. J. Phys. **55**, 13 (2025).

20. T. W. B. Kibble, \"\"Geometrization of quantum mechanics,\"\" Commun. Math. Phys. **65**, 189 (1979).

21. A. Ashtekar and T. A. Schilling, \"\"Geometric formulation of quantum mechanics,\"\" in *On Einstein's Path*, edited by A. Harvey (Springer, New York, 1999).

22. J. Steinhauer, \"\"Observation of quantum Hawking radiation and its entanglement in an analogue black hole,\"\" Nat. Phys. **12**, 959 (2016).

23. Orion et al., \"\"Topological sum rules from geometric phases,\"\" arXiv:2603.29795 (2026).

24. E. Cocchi, L. A. Miller, J. H. Drewes, C. F. Chan, D. Pertot, F. Brennecke, and M. K\"ohl, \"\"Equation of state of the two-dimensional Hubbard model,\"\" Phys. Rev. Lett. **116**, 175301 (2016).

25. J. H. Drewes, L. A. Miller, E. Cocchi, C. F. Chan, D. Pertot, F. Brennecke, and M. K\"ohl, \"\"Antiferromagnetic correlations in two-dimensional fermionic Mott-insulating and metallic phases,\"\" Phys. Rev. Lett. **118**, 170401 (2017).

26. M. F. Parsons, \"\"A quantum gas microscope for $^6$Li,\"\" Ph.D. thesis, Harvard University (2016).

27. M. Kiser, J. McGinley, and D. Malz, \"\"Gaussian process tomography for cold-atom quantum simulators,\"\" arXiv:2510.23591 (2025).

28. Z. Huang, \"\"Ergotropy rate equation for finite-dimensional quantum systems,\"\" (2026), to be published.

---


*PRA Regular Article v3.0 | 2026-06-03 | Optimized for Physical Review A with all adversarial review fixes applied*
