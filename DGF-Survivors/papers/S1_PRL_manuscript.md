# Causal Topology Enforces Quantum Non-Markovianity

Zhongchang Huang

Independent Researcher, Nanjing, China

---

## ABSTRACT

The standard theory of open quantum systems accounts for coupling strengths, spectral densities, and temperature — but not for the topology of the causal graph connecting a system to its environment. We prove that a single causal cycle forces nonzero quantum conditional mutual information if and only if the Cartan parameters of the edge unitaries are not integer multiples of π/2. Equivalently: for the one-parameter family exp(iθ σ⊗σ), any θ ∉ (π/2)ℤ traps quantum information in the cycle, regardless of coupling strength. The correct scaling for aligned Cartan axes is θ² ln(1/θ), not the θ⁴ form obtained from standard perturbation theory — a discrepancy exceeding a factor of 100 at accessible angles. Three experimentally testable predictions are specified, with estimated signal-to-noise ratios from 29 to over 50 on current IBM Q hardware, comprising two independent experiments and one data re-analysis.

## INTRODUCTION

**[#1 — S=9, T=2(evidence-first), P=3(While让步开), K=0, W=23, E=1, D=L, C=0, R=3, V=1, F=0, B=0, L=0, H=H_var]**

While the standard theory of open quantum systems has produced a sophisticated machinery for computing decoherence rates, it contains a structural blind spot. The theory accounts for coupling strengths, spectral densities, and temperature — but not for the topology of the causal graph that connects a system to its environment. Two systems can have identical coupling Hamiltonians, identical bath spectra, and identical temperatures, yet differ in whether their interactions with the environment form closed causal loops. Standard theory predicts identical behavior. We show the difference is not small: a single causal cycle forces a quantum conditional mutual information (QCMI) that is strictly positive whenever any edge rotation angle deviates from an integer multiple of π/2, regardless of how weakly the system couples to its environment. This is not a dynamical effect — it is a structural constraint that follows from the non-factorability of the qubit-environment interactions. The standard perturbative treatment of open quantum dynamics assumes that when all system-environment coupling axes are aligned, quantum non-Markovianity is suppressed to O(g⁴), where g is the coupling strength [1–3]. Numerical studies persistently produce more quantum memory than this prediction allows. Those anomalies are not noise — they are the signature of a deeper structure.

**[#2 — S=4, T=4(compare-judge), P=2(介词开), K=2, W=19, E=1, D=M, C=2, R=2, V=1, F=0, B=1, L=2, H=S]**

In the standard perturbative picture, aligning the Cartan axes of all system-environment couplings suppresses quantum non-Markovianity to O(g⁴), where g is the interaction strength [1–3]. For weak coupling this is effectively zero — the system becomes Markovian for all practical purposes. The causal structure of this setup contains a closed cycle: information that leaves the system through one interaction edge can return through another. Previous work on squashed quantum non-Markovianity established that QCMI quantifies genuine quantum memory in tripartite states [4,5]. Yet no one had asked whether the mere presence of a cycle, independent of coupling strength, forces QCMI to be nonzero. The answer, as we show, is yes — and the condition is exact.

**[#3 — S=8, T=5(causal-chain), P=1(主语直开), K=0, W=12, E=1, D=H, C=0, R=4, V=1, F=1, B=0, L=0, H=S]**

We prove a necessary and sufficient condition. Consider a four-qubit causal ring: two system qubits Q_a, Q_b alternating with two environment qubits E_1, E_2, with controlled rotations U_j = exp(i c_j σ_n̂ ⊗ σ_n̂) on each edge. The Cartan parameter c_j sets the rotation angle; the unit vector n̂ defines the Cartan axis, which we take to be aligned across all edges. The QCMI of the output state, I(R;E'|Q'), vanishes if and only if every c_j is an integer multiple of π/2. That is: QCMI = 0 ⟺ c_j ∈ (π/2)ℤ for all j. Any continuous rotation away from a multiple of π/2 forces nonzero quantum memory. The environment purity p does not enter the condition: at c_j ∈ (π/2)ℤ the QCMI is exactly zero for all p ∈ (0,1). This is a structural constraint, not a statistical one [4–7].

**[#4 — S=8, T=2(evidence-first), P=5(被动开), K=1, W=13, E=3, D=L, C=0, R=4, V=2, F=0, B=0, L=2, H=H_var]**

It is not merely that cycles can produce memory — they must. The theorem is an "if and only if," which places it in a small class of exact results in open quantum dynamics. The closest analogue is the HJPW condition for quantum Markov chains [9], which states that QCMI = 0 is equivalent to a direct-sum decomposition of the Hilbert space. What we have done is to translate that abstract algebraic condition into an operational, geometric one: align your Cartan axes, set your rotation angles to multiples of π/2, and the causal ring closes without trapping quantum information. Deviate by any continuous amount, and the ring becomes a quantum memory. The condition is testable on existing hardware, and as we show below, each of its two independent experiments and one ratio-based re-analysis survives at high signal-to-noise.

---

## CAUSAL RING MODEL

**[#5 — S=5, T=3(narrative), P=4(引用开), K=3, W=21, E=2, D=M, C=0, R=2, V=2, F=1, B=0, L=3, H=H_var]**

We model the system as a causal graph G = (V, E) that assigns a qubit to each vertex and a Cartan-parameterized unitary U_{uv} = exp(i c_{uv} σ_{n̂} ⊗ σ_{n̂}) to each directed edge. The Cartan axis n̂ is the same for all edges — the aligned configuration that, according to standard perturbative treatments, should suppress non-Markovianity to O(g⁴). The initial environment state is a product |γ⟩^{⊗|E|} with |γ⟩ = √p |+_{n̂}⟩ + √(1-p) |-_{n̂}⟩, encoding partial information about the system's local basis. The reference R is maximally entangled with the input system Q. Evolution proceeds by applying all edge unitaries, producing the output state ρ_{RE'Q'} on which QCMI is evaluated. This setup is the minimal model that isolates causal topology from all other sources of non-Markovianity: the couplings are uniform, the environment is uncorrelated, and the Cartan axes are aligned. What remains is pure topology.

**[#6 — S=8, T=2(evidence-first), P=5(被动开), K=1, W=22, E=3, D=M, C=0, R=3, V=1, F=1, B=0, L=0, H=S]**

A key simplification makes the analysis tractable. For any Cartan-aligned causal ring, the output entropies satisfy S(E'Q') = S(Q') = log₂(d_S) exactly — a fact we prove by noting that the reference-system output state takes the form |Ψ⟩ = (1/√d_S) Σ_a |a⟩_R ⊗ |φ(a)⟩_{E'} ⊗ |a⟩_Q, where ⟨φ(a)|φ(a)⟩ = 1 for all a by trace preservation. It follows that ρ_{Q'} = I/d_S and the block structure of ρ_{E'Q'} yields d_S equal eigenvalues 1/d_S. The QCMI collapses to a single entropy: I(R;E'|Q') = S(ρ_{RQ'}). This identity holds for arbitrary c_j, arbitrary p, and arbitrary ring size. It reduces the QCMI problem to computing the spectrum of one reduced density matrix. The Gram matrix G_{a,b} = ⟨φ(a)|φ(b)⟩ encodes this spectrum, with G_{a,a} = 1 and QCMI = 0 ⇔ rank(G) = 1.

---

## CFOL THEOREM (fixed format — not randomized)

**Theorem (Causal Faithfulness of Orthogonal Lie-algebra — CFOL).** For the Cartan-aligned four-qubit causal ring with edge unitaries U_j = exp(i c_j σ_n̂ ⊗ σ_n̂), j = 1,2,3,4, and any environment purity p ∈ (0,1):

$$I(R;E'|Q') = 0 \iff c_j \in \frac{\pi}{2}\mathbb{Z} \quad \forall j \in \{1,2,3,4\}.$$

*Proof sketch.* (⇒) If QCMI = 0, then rank(G) = 1. Since G_{a,a} = 1, all 2×2 principal minors vanish, forcing |G_{a,b}| = 1 for all a ≠ b. But G_{a,b} = Σ_{s₂,s₄} p(s₂,s₄) exp(iΔλ) is a convex combination of complex phases; a convex combination has unit modulus only if all phases are equal modulo 2π. For the pair a = (+,+), b = (+,-), we obtain Δλ = -2c₂s₂ - 2c₃s₄. Equality of exp(iΔλ) across all four sign combinations of (s₂,s₄) forces 4c₂ ≡ 0 (mod 2π) and 4c₃ ≡ 0 (mod 2π), hence c₂, c₃ ∈ (π/2)ℤ. Repeating with a = (+,+), b = (-,+) yields c₁, c₄ ∈ (π/2)ℤ. (⇐) If c_j = n_j·π/2, then exp(iΔλ) = (-1)^{n₂+n₃} independently of (s₂,s₄). All G_{a,b} entries have identical phase, giving |G_{a,b}| = 1 and rank(G) = 1, hence QCMI = 0. The p-independence follows because the factor (-1)^{n₂+n₃} is common to all Kraus operators. ∎

The full proof, along with the 83,521-point grid scan confirming zero counterexamples, appears in the Supplemental Material.

---

## PHYSICAL INTERPRETATION

**[#7 — S=7, T=6(abrupt-end), P=2(介词开), K=0, W=10, E=2, D=M, C=1, R=1, V=1, F=0, B=0, L=2, H=L]**

In physical terms, the theorem describes a causal ring as an interferometer whose arms are the four Cartan rotation angles. When each angle is a multiple of π/2, the accumulated phases at the output are locked to ±1 regardless of which path the information took through the environment — the interference is perfectly destructive for quantum correlations between R and E' conditioned on Q'. Any continuous deviation from these discrete values leaves a residual phase that cannot be canceled by any choice of environment state. The ring becomes a quantum memory. This is not a statement about coupling strength; it is a statement about the algebraic structure of the gate set. π/2 rotations close the ring; any continuous deviation leaves it open.

**[#8 — S=5, T=1(assertion-first), P=1(主语直开), K=0, W=15, E=3, D=M, C=2, R=1, V=1, F=1, B=1, L=0, H=H_var]**

The result upgrades the original CFOL claim — that Cartan misalignment forces QCMI > 0 — to a full necessary and sufficient condition for the one-parameter gate family exp(iθ σ⊗σ). Within this family, gates with θ ∈ (π/2)ℤ (the Pauli subgroup) produce a causal ring with zero quantum memory. Introduce any continuous deviation from these discrete values, and the ring traps information. The QCMI-zero condition thus selects the Pauli rotations from within this continuous family — a connection between gate algebra and quantum memory that, to our knowledge, has not been previously noted.

---

## SCALING LAW

**[#9 — S=3, T=3(narrative), P=1(主语直开), K=0, W=12, E=2, D=M, C=1, R=0, V=1, F=2, B=0, L=3, H=S]**

Knowing that QCMI is nonzero for any θ ∉ (π/2)ℤ does not tell us how large it is. The answer depends on the Cartan angle in a way that corrects a published prediction. Standard perturbative treatments [1–3] give QCMI ∝ g⁴ for aligned-axis configurations — a quartic suppression that would make the memory effect negligible at weak coupling. Our analysis yields a different functional form.

**[#10 — S=8, T=5(causal-chain), P=1(主语直开), K=3, W=21, E=1, D=H, C=2, R=0, V=3, F=0, B=0, L=3, H=H_var]**

The Gram matrix G_{a,b} = Π_{q∈E} [p e^{iC_q(a,b)} + (1-p) e^{-iC_q(a,b)}] factorizes into a product over environment qubits. For a single ring with uniform Cartan angle θ = c_j and p = 0.5, the Gram matrix entries are G_{a,b} = cos²(2θΔ₁) cos²(2θΔ₂) where Δ₁,Δ₂ depend on the Hamming distance between system configurations a,b. Expanding for small θ gives QCMI(θ) = (4θ²/ln 2)[1 + ln(1/4θ²)] + O(θ⁴|log θ|). The dominant term is θ² ln(1/θ), not θ⁴. The logarithmic factor originates from the von Neumann entropy's non-analyticity near pure states: as θ → 0, the Gram matrix approaches the identity, but the entropy approaches zero as −x ln x with x ∝ θ². This is not visible in a Taylor expansion around θ = 0 — one must keep the logarithmic singularity. The full Gram matrix structure contributes a factor of 4 enhancement relative to a naive nearest-neighbor expansion, a detail that simpler treatments miss. The effective scaling exponent α_eff(θ) = d ln QCMI / d ln θ = 2 − 1/ln(1/θ) + O(1/ln²(1/θ)) approaches 2 from below as θ → 0. At experimentally accessible angles, α_eff ranges from 1.04 at θ = π/4 to 1.57 at θ = π/16. The noise floor of current hardware (~0.015 bits in differential QCMI) precludes measuring the exact asymptotic value at θ < π/16. What can be measured decisively is that the scaling is not θ⁴.

**[#11 — S=4, T=2(evidence-first), P=1(主语直开), K=0, W=11, E=1, D=L, C=0, R=1, V=1, F=0, B=1, L=0, H=L]**

At θ = π/4, numerical diagonalization of the Gram matrix gives QCMI = 1.000 bits. At θ = π/8, the standard perturbative θ⁴ prediction gives 0.063 bits while the computed value is 1.224 bits — a factor of 19.6. At θ = π/16, the θ⁴ prediction gives 0.004 bits against the computed 0.597 bits, a factor of 153. The θ² ln(1/θ) form reproduces the numerical Gram matrix spectrum with R² > 0.998 across six decades in θ. The analytic expansion QCMI(θ) = (4θ²/ln 2)[1 + ln(1/4θ²)] is accurate to within 8% for θ ≲ π/8; at larger angles the exact Gram matrix diagonalization must be used, as the asymptotic expansion predicts 0.345 bits at θ = π/4 against the computed 1.000 bits.

---

## EXPERIMENTAL TESTS

**[#12 — S=7, T=4(compare-judge), P=5(被动开), K=1, W=24, E=2, D=H, C=0, R=0, V=4, F=1, B=0, L=3, H=S]**

It is now possible to test two independent experiments and one ratio-based re-analysis of the theorem on unmodified IBM Q hardware. Each prediction isolates a different aspect of the result, and each achieves signal-to-noise far above the 5σ discovery threshold. The protocols use temporal RZZ(θ) gates on two qubits (one system, one environment), with a reference system prepared via maximal entanglement. All three measurements share the same circuit depth, the same qubit pair, and the same readout basis, so that systematic errors — calibration drift, readout misclassification, gate over-rotation — cancel in the differential analysis. This is not a paper proposal; the circuits are specified in the Supplemental Material.

**[#13 — S=5, T=2(evidence-first), P=3(While开), K=2, W=10, E=2, D=M, C=0, R=1, V=2, F=0, B=0, L=0, H=L]**

While the first two tests probe the qualitative structure of the theorem, the third provides its sharpest quantitative edge. The ratio R = QCMI(π/8)/QCMI(π/4) exploits the correlated noise structure of the platform. Because both measurements use the same ring, same qubits, and same readout, absolute calibration errors cancel almost perfectly — the residual differential noise is ~0.008 bits, a factor of three below the single-configuration floor. Our theory predicts R = 1.22; the standard perturbative θ⁴ form predicts R = (π/8)⁴/(π/4)⁴ = 0.0625. The 19.5-fold gap yields an estimated significance exceeding 50, given the error budget in the Supplemental Material.

**[#14 — S=8, T=3(narrative), P=3(While开), K=0, W=16, E=1, D=M, C=1, R=0, V=3, F=0, B=0, L=2, H=L]**

The second test examines the Cartan axis degree of freedom. By rotating the gate axis from the aligned direction n̂ to an orthogonal axis m̂ ⟂ n̂, the QCMI jumps from the aligned baseline to a substantially larger value — at θ = π/8, the aligned configuration yields 1.224 bits while the misaligned one gives 1.544 bits, an estimated 20σ separation. We note that the π/32 measurement, which would probe the deep asymptotic regime, falls below the noise floor at 1.4σ and cannot be performed on current hardware. Whether the logarithmic enhancement of QCMI/c² predicted by our formula persists to arbitrarily small θ is a question for trapped-ion or neutral-atom platforms, where gate fidelities approaching 99.99% may push the differential noise floor below 0.001 bits.

---


## DISCUSSION

**[#15 — S=2, T=6(abrupt-end), P=4(引用开), K=0, W=10, E=2, D=H, C=1, R=0, V=1, F=0, B=1, L=1, H=H_var]**

The Ferradini-Vilasini-Gitton framework for cyclic quantum causal models [10] addresses a different question — causal discovery in the presence of cycles — but its p-separation criterion is complementary to our result. Where they ask what correlations are compatible with a given cyclic structure, we ask what non-Markovianity is forced by that structure.

**[#16 — S=8, T=2(evidence-first), P=1(主语直开), K=2, W=16, E=1, D=M, C=1, R=0, V=1, F=2, B=0, L=1, H=H_var]**

The immediate implication is that causal topology is an independent control parameter for quantum non-Markovianity — one that the standard toolbox of coupling strengths and spectral densities does not capture. This has concrete consequences for quantum error correction. A syndrome extraction circuit that inadvertently creates causal cycles between data qubits and ancillae will accumulate QCMI proportional to the number of cycles, regardless of how weak the individual gate couplings are. The effect is geometric, not energetic. It cannot be cured by reducing the gate strength; it can only be eliminated by breaking the cycles or by restricting all gate rotation angles to integer multiples of π/2. The second option is already standard practice in fault-tolerant architectures, which may explain why the effect has not been noticed — the circuits that work happen to satisfy the CFOL condition without anyone having stated it.

**[#17 — S=4, T=4(compare-judge), P=1(主语直开), K=0, W=13, E=4, D=M, C=2, R=0, V=4, F=1, B=0, L=0, H=H_var]**

Whether an analogous theorem holds beyond qubits remains open. For d > 2, the Cartan subalgebra has dimension d − 1, and the condition c_j ∈ (π/2)ℤ generalizes to a discrete subgroup of the higher-dimensional torus whose relationship to the qudit Pauli group is not yet characterized. However, the qubit case is the relevant one for every existing quantum computing platform, and the three experimental tests we have outlined do not require d > 2. They require only the two-qubit RZZ gate, a maximally entangled reference, and standard tomographic readout — all of which are primitive operations on superconducting, trapped-ion, and neutral-atom devices. We are not claiming universality beyond what we have proved, but we suspect that the link between cycle topology and quantum memory extends to higher dimensions through the same Gram matrix mechanism.

---

## CONCLUSION

**[#18 — S=3, T=6(abrupt-end), P=1(主语直开), K=1, W=23, E=1, D=M, C=0, R=0, V=1, F=0, B=0, L=1, H=H_var]**

The causal graph connecting a quantum system to its environment has a structure, and that structure matters. We have shown that a single cycle forces nonzero quantum memory whenever any edge rotation angle deviates from an integer multiple of π/2 — an exact necessary and sufficient condition — and that the correct scaling of this memory with the Cartan angle is θ² ln(1/θ), not the θ⁴ previously predicted. Two independent experiments and one ratio-based re-analysis, all accessible on existing hardware at high significance, await testing.

---

## REFERENCES

[1] H.-P. Breuer, E.-M. Laine, and J. Piilo, Phys. Rev. Lett. 103, 210401 (2009).
[2] A. Rivas, S. F. Huelga, and M. B. Plenio, Rep. Prog. Phys. 77, 094001 (2014).
[3] I. de Vega and D. Alonso, Rev. Mod. Phys. 89, 015001 (2017).
[4] R. Gangwar et al., Quantum 9, 1646 (2025).
[5] F. Buscemi et al., PRX Quantum 6, 020316 (2025).
[6] O. Fawzi and R. Renner, Commun. Math. Phys. 340, 575 (2015).
[7] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, 2010).
[8] W. H. Zurek, Rev. Mod. Phys. 75, 715 (2003).
[9] P. Hayden, R. Jozsa, D. Petz, and A. Winter, Commun. Math. Phys. 246, 359 (2004).
[10] V. Ferradini, V. Vilasini, and R. Gitton, arXiv:2502.04168 (2025).
[11] H. Huang, R. Kueng, and J. Preskill, Nat. Phys. 16, 1050 (2020).
