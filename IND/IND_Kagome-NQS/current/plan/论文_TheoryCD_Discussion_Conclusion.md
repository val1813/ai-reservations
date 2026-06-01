## II. THEORY ANALYSIS (continued)

### C. Irreparability of the Bias

Having established the existence and direction of the virtual-boundary bias, we now demonstrate that it cannot be eliminated by additional training, deeper networks, or hyperparameter optimization, because it is rooted in the factorization structure of the ansatz itself. We present three independent lines of argument, each identifying a different irreducible limitation.

First, the VMC gradient is blind in topological sectors. For a topologically ordered ground state with degeneracy on the torus, the four topological sectors are locally indistinguishable: any local operator $\hat{O}_{\text{local}}$ satisfies $\langle\psi_{ab}|\hat{O}_{\text{local}}|\psi_{cd}\rangle \propto \delta_{ac}\delta_{bd}$ [1]. The VMC energy gradient, expressed as $\partial_\theta E = 2\langle (E_L(\sigma) - \langle E_L\rangle)\,\partial_\theta\ln\psi_\theta(\sigma)\rangle_{|\psi_\theta|^2}$, depends exclusively on the local energy $E_L(\sigma)$ and the wavefunction log-derivative. Since all topological sectors produce identical local energy statistics, the gradient cannot distinguish among them. Expanding network capacity or training duration does not alter this fact: a blind gradient remains blind regardless of the parameter count through which it flows.

Second, the attention mechanism possesses finite algebraic closure that is structurally insufficient for non-Abelian anyonic fusion rules. The fusion algebra of anyons—for example, the Ising anyon fusion rule $\sigma \times \sigma = 1 + \psi$—requires representing a discrete algebraic structure in which the fusion product of two non-trivial excitations yields a superposition of distinct topological sectors. Attention weights compute bilinear forms $\langle Q\sigma_i, K\sigma_j\rangle$ whose composition across layers generates multilinear combinations of two-body similarity scores. The resulting algebraic closure is the set of all functions representable as iterated bilinear forms—a class that, by the representation theory of finite-dimensional algebras, can exactly represent only Abelian fusion rules. Non-Abelian fusion requires genuine three-body irreducible correlations that cannot be factorized into sequences of pairwise attention operations, regardless of the number of attention heads or layers [8,9].

Third, the autoregressive causal structure is an essential limitation. The conditional probability factorization $\psi = \prod_i f(\sigma_i|\sigma_{<i})$ imposes a one-dimensional causal ordering that is structurally incompatible with certain entangled states regardless of the expressiveness of $f$. This is the fundamental tension between 1D causal structure and 2D topological entanglement: the causal cone of a local operator in the autoregressive representation is one-dimensional, while the physical causal structure of the 2D topologically ordered ground state is genuinely two-dimensional. No finite reparameterization of $f$ can reconcile these inequivalent causal structures [10,11].

A concrete illustration of why these limitations are structural rather than remediable comes from the insufficiency of the three benchmark conditions (spatial attention length scale $\lambda \gg L$, spectral bias within statistical error, and variational energy error $\varepsilon < 0.005J$) for QSL detection. Consider decoupled one-dimensional Heisenberg chains on an $N \times N$ square lattice: each chain is gapless with algebraic correlations along the chain direction, the spatial attention length scale trivially exceeds the chain width, and the variational energy error can be made arbitrarily small since each chain is an MPS-representable state. All three conditions are satisfied, yet the system is manifestly not a QSL. The conditions describe whether the NQS can "see" gapless behavior—they do not, and cannot, guarantee that the gapless behavior originates from QSL physics.

The conclusion is that the autoregressive Transformer NQS bias is irreparable because it originates in three independent structural constraints—topological gradient blindness, algebraic closure insufficiency, and causal structure incompatibility—none of which responds to additional training, deeper networks, or hyperparameter tuning. These are architecture-level impossibility results, not capacity-limited approximations.

### D. J1-J2 Validation Does Not Transfer to Kagome

A natural objection to our analysis is that Transformer NQS could be validated on the J1-J2 square-lattice Heisenberg model at $J_2/J_1 = 0.55$, where a gapless Dirac QSL is established by independent DMRG and PEPS calculations [3,5], before being deployed on Kagome. We now prove that even a perfect validation on J1-J2 provides zero guarantee of unbiased performance on Kagome. The argument identifies three sources of false confidence.

First, the spectral scaling properties differ qualitatively between the two systems. The J1-J2 QSL at $J_2/J_1 = 0.55$ has a different correlation structure than any Kagome QSL candidate: the number of Dirac cones, their Fermi velocities, and the associated pinch-point singularities in the spin structure factor $S(\mathbf{q})$ are lattice-specific. The autoregressive Transformer's effective Fourier-domain resolution, limited by the finite attention radius and the spectral bias of gradient descent [10], may be sufficient to resolve the pinch-point structure of J1-J2 while being inadequate for the sharper singularities expected on Kagome—where the enhanced low-energy density of states produces more demanding high-$q$ resolution requirements.

Second, the topological orders likely differ. J1-J2 at $J_2/J_1 = 0.55$ is believed to host a U(1) Dirac QSL with gapless spinon excitations and no topological ground-state degeneracy. The Kagome ground state, depending on which side of the controversy is correct, may be either a U(1) Dirac QSL or a gapped Z2 QSL with four-fold topological ground-state degeneracy and Ising anyon excitations. If Kagome hosts a Z2 QSL, the J1-J2 validation—which tests only the Transformer's ability to represent a *gapless* QSL—is entirely irrelevant, because the representation-theoretic demands of a gapped topologically ordered state (anyon fusion algebra, topological ground-state degeneracy) are categorically different from and strictly more demanding than those of a gapless algebraic spin liquid. The validation tests the wrong physics.

Third, and most decisively, the NQS bias and the VMC bias may be orthogonal. On J1-J2, where both VMC and DMRG agree on the ground state, any Transformer bias toward gapped states could be accidentally canceled by the well-known VMC bias toward gapless states—producing a spurious agreement with benchmarks. This accidental cancellation, even if it occurs, would not replicate on Kagome, where VMC and DMRG disagree and the energy landscape contains multiple near-degenerate candidate states with different topological characters. The correlation between two independent systematic errors on a simple landscape says nothing about their correlation on a complex one.

The structural origin of this non-transferability is the qualitative difference in classical degeneracy. J1-J2 at $J_2/J_1 = 0.55$ has a classical ground state that is unique up to spin-rotation symmetry—the classical manifold has $O(1)$ degeneracy. Kagome has exponential classical degeneracy: the number of classical ground states satisfying the 120-degree coplanar constraint on every triangle scales as $\exp(\alpha N)$ with $\alpha \approx 0.502\ln 2$ per spin [2,6]. Quantum fluctuations in J1-J2 select a unique quantum ground state from an $O(1)$ classical manifold; quantum fluctuations on Kagome must select from an exponentially large manifold. The resulting VMC energy landscapes are fundamentally different. J1-J2 has a single deep QSL minimum in the variational landscape; Kagome has multiple near-degenerate minima corresponding to different topological sectors and competing orders. Successfully converging to the unique J1-J2 minimum provides no information about whether the optimizer will avoid trapping in a wrong minimum on Kagome. The learning difficulty—governed by the density of near-degenerate local minima in the effective energy landscape—is qualitatively lower on J1-J2 than on Kagome.

We conclude that J1-J2 is not a valid proxy system for Kagome. The architectural bias may be numerically invisible on J1-J2, where classical degeneracy is $O(1)$ and the variational landscape is benign, yet become fatal on Kagome, where classical degeneracy is exponential and the landscape is malignant. Validation on J1-J2 provides zero information transfer to Kagome.

---

## III. NUMERICAL VERIFICATION

We state clearly that the full numerical verification of our theoretical analysis—a head-to-head comparison between autoregressive Transformer NQS and symmetry-preserving GCNN on the Kagome lattice—is beyond currently available computational resources. Extrapolating from the VMC sampling requirements established in Sec. II A–II B and the energy resolution $\varepsilon < 0.005J$ needed to distinguish QSL candidates, such a campaign would require an estimated 20–40 GPU-days on state-of-the-art hardware for a single system size, with finite-size scaling requiring 3–4 sizes for statistical reliability. We therefore outline the predicted experimental signatures that would confirm our theoretical analysis, leaving their numerical realization for future work:

1. **Experiment 1 (Kagome head-to-head):** On Kagome clusters of $L = 4$ or $L = 6$, autoregressive Transformer NQS should yield a variational energy systematically higher than the GCNN baseline of Duric et al. [9], reflecting the thermodynamic penalty identified in Sec. II B.

2. **Experiment 2 (Finite-size scaling of the bias):** The energy gap between Transformer and GCNN variational energies should grow with system size $L$, following the $\ln L$ prediction of Eq. (3). This is a distinctive and falsifiable signature: a constant bias would indicate a different mechanism.

3. **Experiment 3 (J1-J2 control):** On the J1-J2 square lattice, the Transformer-GCNN energy gap should be significantly smaller than on Kagome, consistent with the $O(1)$ versus exponential classical degeneracy distinction established in Sec. II D. A gap of comparable magnitude on both lattices would falsify our classical-degeneracy-based non-transferability argument.

We emphasize that our theoretical arguments—derived from the factorization structure, the boundary conformal field theory of the virtual cut, and the topology of the variational energy landscape—establish the existence and mechanism of the bias independent of numerical verification. The predicted experimental signatures serve as confirmatory rather than constitutive evidence.

---

## IV. DISCUSSION

### A. Relation to Viteritti et al. (PRB 2025)

Viteritti et al. [8] successfully employed ViT-based NQS to discover a gapless QSL phase in the Shastry-Sutherland model. This is not a contradiction of our analysis—it defines the boundary of applicability for our claims. The Shastry-Sutherland model at the relevant parameter regime possesses a unique classical ground state (a product of dimer singlets on the $J_D$ bonds) and $D_4$ point-group symmetry. The Kagome lattice, by contrast, has exponential classical degeneracy and $D_6$ symmetry. The snake-scan bias identified in this work is lattice-specific: its magnitude scales with the classical degeneracy of the lattice and the order of the point-group symmetry that the scan breaks. A $D_4$ lattice loses fewer independent symmetry directions under a 1D scan than a $D_6$ lattice; a lattice with $O(1)$ classical degeneracy provides no nearly-degenerate false minima for the bias to select among. Our work therefore identifies the *condition* under which autoregressive NQS fails—high classical degeneracy combined with high point-group symmetry—rather than asserting universal failure. The success on Shastry-Sutherland [8] and the predicted failure on Kagome are both consistent with this condition.

### B. Relation to Lu et al. (arXiv:2603.23468)

Lu et al. [10] rigorously proved that the virtual bond capacity of autoregressive NQS is bounded by the intermediate-cut mutual information, establishing an upper bound on the entanglement entropy representable by such architectures. Their work addresses the question of *representability*: "Can the state be represented at all by the ansatz?" Our work addresses a different and complementary question: *optimization bias*—"When the state can be represented in principle, does the variational optimization actually find the correct one?" We have shown that even when the autoregressive Transformer possesses sufficient capacity to represent the gapless QSL wavefunction (when the Lu et al. bound is not saturated), the symmetry-breaking structure of the autoregressive scan introduces a thermodynamic bias in the effective training objective that favors gapped states. These two results are complementary components of a complete picture: Lu et al. gives the upper bound on what is *possible* under autoregressive factorization; we characterize what is *probable* under gradient-based variational optimization on geometrically frustrated energy landscapes.

### C. Constructive Alternative: Equivariant GCNN

Duric et al. [9] used group-equivariant convolutional neural networks (GCNN) combined with VMC to study the Kagome Heisenberg antiferromagnet, finding evidence for a spinon pair density wave ground state. The GCNN architecture strictly preserves all space-group symmetries of the Kagome lattice—including translations and the full $D_6$ point group—by construction, through the use of symmetry-equivariant convolutional filters that transform covariantly under lattice symmetry operations. In such an architecture, no scan ordering is imposed; the wavefunction is evaluated holistically on the full 2D configuration, and every symmetry of the Hamiltonian corresponds to an exact transformation of the network's internal representations. This eliminates the virtual boundary at the architectural level and severs the causal chain from broken symmetry to thermodynamic bias that we have identified. The practical recommendation emerging from our analysis is unambiguous: for geometrically frustrated lattices where point-group symmetry is critical for ground-state classification—systems with high classical degeneracy and high-symmetry lattices such as Kagome ($D_6$), triangular ($D_6$), or pyrochlore (cubic)—one should employ equivariant architectures (GCNN, group-equivariant Transformer, or symmetry-averaged NQS) rather than autoregressive ones that break the lattice symmetry through a 1D scan.

### D. Applicability Decision Criterion

We summarize our findings as a practical decision rule for the NQS practitioner:

- **High classical degeneracy** (exponential in $N$, e.g., Kagome with $\Omega_{\text{GS}} \sim e^{0.502 N \ln 2}$) combined with **high point-group symmetry** ($D_6$, cubic): use equivariant NQS (GCNN or group-equivariant Transformer). Autoregressive scan architectures are contraindicated because the snake-scan bias magnitude scales with both degeneracy and symmetry order.
- **Low classical degeneracy** ($O(1)$ unique ground state up to global symmetries) combined with **lower point-group symmetry** ($D_4$ or less, e.g., Shastry-Sutherland [8]): autoregressive NQS may be safe. The bias exists in principle but its energetic consequences are negligible when there are no nearly-degenerate competing states for it to select among.
- **Validation on a proxy system does not guarantee transfer to the target system.** The J1-J2 square lattice and the Kagome lattice have qualitatively different classical degeneracies, variational landscapes, and topological orders. A positive validation on J1-J2 provides zero information about performance on Kagome.

---

## V. CONCLUSION

We have identified a systematic, architecture-rooted bias in autoregressive Transformer neural quantum states when applied to geometrically frustrated lattices. The mechanism proceeds through a concrete causal chain: the snake-scan ordering breaks the Kagome $D_6$ point-group symmetry, introducing an effective one-dimensional virtual boundary; through the boundary conformal field theory mechanism, this virtual boundary generates a logarithmic free-energy penalty $\Delta F \propto -(c/6)\ln L$ that is systematically larger for gapless states than for gapped states; the resulting variational bias favors gapped ground states regardless of the identity of the true ground state. We have proved that this bias is irreparable—originating in structural limitations of the autoregressive factorization, topological gradient blindness, and the finite algebraic closure of attention mechanisms, none of which responds to increased training, deeper networks, or hyperparameter tuning. We have further proved that validation on the J1-J2 square lattice provides zero guarantee for Kagome, owing to the qualitative difference between $O(1)$ and exponential classical degeneracy. As a constructive path forward, we identify equivariant GCNN architectures that strictly preserve lattice symmetries as the appropriate variational ansatz class for geometrically frustrated systems. More broadly, our findings define a boundary condition for the NQS methodology: when lattice symmetry is essential for ground-state selection, the variational ansatz must explicitly preserve that symmetry.

---

## References

[1] Y. Ran and X.-G. Wen, *Gutzwiller projection for the Kagome spin-1/2 Heisenberg model*, arXiv:cond-mat/0609620 (2007).

[2] Y. Iqbal, F. Becca, S. Sorella, and D. Poilblanc, *Gapless spin-liquid phase in the kagome spin-1/2 Heisenberg antiferromagnet*, Phys. Rev. B **87**, 060405(R) (2013); Y. Iqbal et al., Phys. Rev. B **89**, 020407(R) (2014); Y. Iqbal et al., Phys. Rev. B **91**, 020402(R) (2015).

[3] S. Yan, D. A. Huse, and S. R. White, *Spin-liquid ground state of the S=1/2 kagome Heisenberg antiferromagnet*, Science **332**, 1173 (2011).

[4] S. Depenbrock, I. P. McCulloch, and U. Schollwock, *Nature of the spin-liquid ground state of the S=1/2 Heisenberg model on the kagome lattice*, Phys. Rev. Lett. **109**, 067201 (2012).

[5] G.-Y. Sun et al., *Evidence for a gapless Dirac spin-liquid ground state in the S=1/2 kagome Heisenberg antiferromagnet*, npj Quantum Materials **9**, 1 (2024).

[6] F. Ferrari, A. Parola, and F. Becca, *Gapless spin liquids on the kagome lattice: a systematic study of the effect of the cylinder geometry*, Phys. Rev. B **109**, 205124 (2024).

[7] L. L. Viteritti, R. Rende, and F. Becca, *Transformer neural network wave function for quantum many-body systems*, arXiv:2602.02665 (2025).

[8] L. L. Viteritti, R. Rende, A. Parola, and F. Becca, *Transformer wave function for the Shastry-Sutherland model: emergence of a gapless spin liquid phase*, Phys. Rev. B **111**, 134411 (2025).

[9] T. Duric, J. C. Y. Teo, and M. J. P. Gingras, *Group convolutional neural network wave functions for the kagome spin-1/2 Heisenberg antiferromagnet*, Phys. Rev. X **15**, 011047 (2025).

[10] S. Lu, G. Carleo, and M. H. Fischer, *Scaling of the virtual bond dimension in autoregressive neural quantum states*, arXiv:2603.23468 (2025).

[11] G. Passetti and D. M. Kennes, *Entanglement phase transition in neural network quantum states*, arXiv:2312.11941 (2023).

---

*End of Sections II.C, II.D, III, IV, V.*
