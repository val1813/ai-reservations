# Malicious PRL Review — Round 2 (Revised Manuscript)

**Reviewer**: Adversarial PRL referee, quantum error correction and metrology specialization
**Manuscript under review**: Combined revised work of A博士 (non-Pauli breakthrough) and B博士 (Gram-QFIM metrology wall)
**Date**: 2026-06-11
**Round 1 disposition**: REJECT (fatal error in logical error rate formula — equality should have been inequality)
**Round 2 disposition**: See below

---

## 0. Overall Verdict

**RECOMMENDATION: REJECT**

The authors have responded to Round 1 by producing two new claims rather than fixing the original fatal flaw. The Round 1 rejection was based on a single, definitive error: $P_L = (1 - G(x_L))/2$ confuses correctable and uncorrectable errors, making it an upper bound, not an equality. The revised manuscript **does not fix this error**. Instead, it pivots to entirely new claims (non-Markovianity, coherent enhancement, Gram-QFIM identity, metrology trade-off), many of which **depend on the same uncorrected equality** and therefore inherit its flaw.

Worse: the two new claims (A博士's non-Pauli proof and B博士's metrology trade-off) are **internally inconsistent with each other**. A博士 proves the Gram channel is non-Markovian with memory across rings; B博士 assumes Fisher information is additive (independent ring contributions), which implies Markovianity. The manuscript cannot simultaneously assert both without contradiction.

Below I analyze all eight attack dimensions. Four are FATAL, three are SEVERE, one is MODERATE.

---

## Attack 1: The "Pauli Twirl = Non-Markovian" Argument

**Severity: FATAL**

### 1.1 The Claim

A博士 argues that the Walsh-Hadamard decomposition $\Phi(\rho) = \sum_z c_z Z^z \rho Z^z$ is a "Pauli twirl" in the sense of Kattemölle et al. (2026), and therefore the resulting Pauli Z channel is non-Markovian (negative Pauli-Lindblad parameters). This is supposed to prove that the Gram channel and its Pauli Z representation have different physical behavior.

### 1.2 The Fatal Flaw: The Walsh-Hadamard Transform is NOT a Pauli Twirl

A Pauli twirl, as defined by Kattemölle et al. (Eq. 7), is a **stochastic averaging procedure**:

$$\mathcal{E}^P(\rho) = \frac{1}{4^n} \sum_a P_a \mathcal{E}(P_a \rho P_a) P_a$$

This is an **approximation** — it replaces the original channel $\mathcal{E}$ with a Pauli-averaged version $\mathcal{E}^P$ that has the same single-time action but different multi-time properties. The stochastic nature of the twirl (randomly inserting Pauli gates before and after the channel) is what introduces the auxiliary classical memory that breaks Markovianity.

The Walsh-Hadamard transform, by contrast, is a **deterministic, exact, invertible linear transformation**:

$$c_z = \frac{1}{2^n} \sum_{x \in \mathbb{Z}_2^n} G(x) (-1)^{z \cdot x}$$

This is NOT a stochastic averaging. It is simply a change of basis in the space of channel representations — going from the Gram representation $G(x)$ to the Pauli coefficient representation $c_z$. Both representations describe **the exact same channel** $\Phi(\rho) = G \odot \rho$ at the single-time level. There is no auxiliary classical memory, no random choice of Pauli, no twirl.

To see why this matters, consider the simplest case: the single-qubit dephasing channel $\Phi(\rho) = (1-p)\rho + p Z\rho Z$. Write this as $\Phi(\rho) = G \odot \rho$ with $G = \begin{pmatrix}1 & 1-2p \\ 1-2p & 1\end{pmatrix}$. The Walsh-Hadamard transform gives $c_0 = 1-p$, $c_1 = p$ — which is exactly the Pauli representation. This is NOT a twirl. It is an **identity**. The channel IS a Pauli Z channel. The Walsh-Hadamard transform didn't "create" the Pauli representation — it revealed it.

Kattemölle et al.'s theorem applies when you take an **arbitrary** channel (e.g., a unitary channel with coherent errors) and twirl it into a Pauli channel. But the Gram channel is **already Pauli** (as A博士's Round 1 proved). The Walsh-Hadamard transform does not approximate it — it exactly diagonalizes it in the Pauli basis.

### 1.3 The Self-Contradiction in Section 1.2

A博士's own computation in Section 1.2 shows that $\lambda_{(z,0)} = 0$ for pure Z-type Pauli operators. The derivation is:

$$\lambda_{(z,0)} = \frac{1}{4^n} \sum_{(z',x')\neq 0} (-1)^{z\cdot x' \oplus z'\cdot 0} \ln(G(x')) = \frac{1}{2^n} \sum_{x'\neq 0} \ln(G(x')) \delta_{x',0} = 0$$

A博士 then says "Wait — this requires more careful analysis" and tries to find negative $\lambda$ by a different route. But the initial computation is **correct**. For the Gram channel in the Cartan-aligned case, $f_{(z,x)} = G(x)$ depends only on $x$, and the Pauli-Lindblad parameter for any pure-Z Pauli operator vanishes because $\ln(G(0)) = \ln(1) = 0$.

Lemma 1 (claiming $\lambda_{(z,0)} < 0$) is then argued by hand-waving: "for generic z with weight 1, approximately half the x' have $(-1)^{z\cdot x'} = -1$, giving a negative overall sum." This is NOT a proof. It is a heuristic that ignores the fact that the sum over $z'$ of the phase factor $(-1)^{z\cdot x'}$ gives $\delta_{x',0}$, which makes the sum zero for all $x' \neq 0$. The author's attempt to circumvent their own correct computation by going to a different formula is transparently motivated reasoning.

**The non-Markovianity claim is mathematically false for the Cartan-aligned Gram channel.**

### 1.4 What About Section 1.3 (Physical Meaning)?

A博士 appeals to Kattemölle et al.'s physical interpretation: "the auxiliary classical degree of freedom has to 'memorize' a." But for the Gram channel, there IS no auxiliary classical degree of freedom — the Pauli coefficients $c_z$ are computed analytically from $G(x)$, not by stochastically applying and undoing Pauli gates. The Gram channel's environment qubits already provide whatever memory exists; the Walsh-Hadamard transform does not add new memory.

### 1.5 Fix Required

1. Prove that $\lambda_{(z,0)} < 0$ for at least one specific, numerically computed case (b1=3, c=0.5), not by heuristic argument.
2. Or acknowledge that the Walsh-Hadamard transform is not a Pauli twirl and the Kattemölle argument is inapplicable.
3. Either way: retract the claim that the Pauli Z description is non-Markovian.

---

## Attack 2: The "Coherent Enhancement Factor"

**Severity: FATAL**

### 2.1 The Claim

A博士 claims that the logical error rate under true Gram decay exceeds the Pauli Z prediction by a "coherent enhancement factor" $F(c,d,N) \approx 3\times$ for c=0.5, d=3, N=100, using the Greenbaum-Dutton (G&D) framework.

### 2.2 The Fundamental Category Error

Greenbaum & Dutton (2018) analyze **coherent errors** — specifically, unitary over-rotations of the form $U = \exp(-i\varepsilon H)$ where $\varepsilon$ is a rotation angle error and $H$ is a Hamiltonian. Their framework distinguishes:

- $\varepsilon$: the **coherent** rotation angle (unitary error)
- $q$: the **stochastic** error probability (Pauli error)

Gram decay is $\Phi(\rho) = G \odot \rho$ — it reduces off-diagonal magnitudes by a multiplicative factor. This is a **decoherence** process (loss of coherence, not unitary rotation). There is NO unitary operator $U = \exp(-i\varepsilon H)$ whose action on density matrices produces $G \odot \rho$.

A博士 maps $\varepsilon \sim c$ (Cartan parameter as rotation angle) and $q \sim (1-G_{\min})/2$ (Gram decay as stochastic error probability). This mapping is **asserted, not derived**. The Cartan parameter $c$ appears inside $\cos(c \cdot \Delta_r)$ — this is a trigonometric factor in the decay of off-diagonal elements, not a rotation angle in an exponential map. The G&D formalism requires:

$$\varepsilon_L = 2C(d)(\varepsilon/2)^d$$

where $\varepsilon$ is the physical rotation angle per gate. A博士 needs to show that Gram decay produces a unitary rotation of angle $c$ on the logical subspace. There is no such derivation. Gram decay does not rotate — it shrinks.

### 2.3 The Mapping is Incoherent (Literally)

Gram decay produces an incoherent mixture (reduction of off-diagonal magnitude). G&D's "coherent error" produces a unitary rotation (preservation of purity with wrong angle). These are different physical processes with different signatures:

| Property | Gram Decay | Coherent Error (G&D) |
|----------|-----------|----------------------|
| Purity | Decreases | Preserved |
| Off-diagonals | Shrink multiplicatively | Rotate (maintain magnitude) |
| Generator | Dissipator (Lindblad) | Hamiltonian (unitary) |
| Pauli twirl | Trivial (already Pauli) | Non-trivial (creates stochastic error) |

A博士 is applying a formalism designed for one error type to a completely different error type without justification.

### 2.4 Numerical Estimate is Back-of-Envelope at Best

The estimate $F(c=0.5, d=3, N=100) \approx 2.9$ uses:
- $\varepsilon \approx 0.5$ — pulled from the Cartan parameter with no justification
- $q \approx (1-0.59)/2 \approx 0.205$ — using the Round 1 upper bound formula which was already proven false
- $\varepsilon_L \sim (0.5)^3 = 0.125$ — this is $c^d$, not derived from any logical channel computation

These numbers are not derived from any model. They are illustrative guesses dressed as quantitative predictions.

### 2.5 The Deeper Problem: This Depends on the Round 1 Error

The entire G&D mapping assumes that the logical error channel under Gram decay has the same structure as a coherent-plus-stochastic error channel. But Round 1 proved that Gram decay IS a Pauli Z channel at single time. A Pauli Z channel has $\varepsilon = 0$ in the G&D classification — it is purely stochastic ($q$ only). If $\varepsilon = 0$, then $F = 1$ and there is NO coherent enhancement.

A博士 is trying to have it both ways: Gram decay is Pauli Z (Round 1) AND Gram decay has coherent enhancement (Round 2). These are contradictory unless the "coherent" part comes from multi-time effects — but G&D's framework applies to single-time error channels, not multi-time correlations.

### 2.6 Fix Required

1. Derive the effective unitary rotation angle $\varepsilon$ produced by Gram decay on the logical subspace, starting from the Gram channel's Kraus operators.
2. If $\varepsilon = 0$ (as the Pauli Z proof implies), retract the coherent enhancement claim entirely.
3. If a non-zero $\varepsilon$ exists, compute it rigorously for at least one specific code (e.g., Steane [[7,1,3]]) and compare with numerical simulation.

---

## Attack 3: The "Non-Cartan Genuinely Non-Pauli" Claim

**Severity: SEVERE**

### 3.1 The Claim

A博士 claims that when spin axes $\sigma_n$ are not aligned with $\hat{z}$, the Gram channel acquires X, Y, and off-diagonal chi-matrix elements, making it "genuinely non-Pauli."

### 3.2 What is Correct

The mathematical observation is valid: if the Gram decay acts in a basis rotated relative to the computational basis, the channel's Pauli Transfer Matrix in the computational basis will have off-diagonal elements and X/Y components. This is essentially the statement that dephasing in a rotated basis is not diagonal in the computational Pauli basis.

### 3.3 What is Missing: The Pauli Frame Resolution

The "non-Pauli" nature is **basis-dependent**. If I apply the inverse rotation to align the axes back to $\hat{z}$, the channel becomes Pauli Z again. This is not a passive basis change — it is an active unitary transformation on the system qubits.

In the QEC context, this is handled by **Pauli frame tracking** (also known as "randomized compiling" or "Pauli twirling in software"). The idea is simple: instead of physically rotating all axes to $\hat{z}$ (which may be impractical), you track the axis rotation in classical software and reinterpret measurement outcomes accordingly. This is standard practice on all major quantum computing platforms.

Claiming that misaligned axes produce "genuinely non-Pauli" channels is misleading. They produce Pauli channels **in a different basis**. The mathematical structure is still Pauli — just not Pauli Z. The chi-matrix is still diagonal **in the basis aligned with the Cartan axes**. If the authors claim otherwise, they need to exhibit a specific non-zero off-diagonal chi-matrix element that persists even after optimal basis alignment. Section 4.2 does not do this.

### 3.4 The Physical Relevance Question

Even if the channel is non-Pauli in the computational basis, does this matter for QEC? Standard randomized compiling (Wallman & Emerson, 2016) converts any Markovian noise into a stochastic Pauli channel. If the Gram channel with misaligned axes is Markovian (which A博士 has not disproven — see Attack 1), randomized compiling will convert it to a Pauli channel. The "non-Pauli" nature is then a **choice of experimental protocol**, not a fundamental property.

### 3.5 Fix Required

1. Specify whether the channel is Pauli in the Cartan-aligned basis. If yes, acknowledge that the "non-Pauli" claim is basis-dependent.
2. Show that randomized compiling / Pauli frame tracking cannot remove the non-Pauli structure, or explain why these standard techniques fail for Gram decay specifically.
3. Provide an explicit example (n=2, specific c and axis angles) where the chi-matrix has provably non-zero off-diagonal elements in ALL single-qubit Pauli bases.

---

## Attack 4: The QFIM = Gram Identity

**Severity: FATAL**

### 4.1 The Claim

B博士 claims "the Gram matrix IS the Quantum Fisher Information Matrix." This is the central pillar of the entire metrology argument.

### 4.2 Proof That They Are Different Objects

Let me write both down explicitly:

**Gram matrix** (dimension $d \times d$, indexed by system states $a, b \in \{0,1\}^n$):
$$G[a,b] = \langle E_a | E_b \rangle = \sum_k \kappa^*(a,k;c) \kappa(b,k;c)$$

**Quantum Fisher Information Matrix** (dimension $b_1 \times b_1$, indexed by Cartan parameters $r, s \in \{1,\ldots,b_1\}$):
$$F_{rs}(a;c) = 4\text{Re}\left[\langle \partial_r E_a | \partial_s E_a \rangle - \langle \partial_r E_a | E_a \rangle \langle E_a | \partial_s E_a \rangle\right]$$

These are matrices of **different dimensions, indexed over different spaces, encoding different physical quantities**:

| Property | Gram Matrix G | QFIM F |
|----------|--------------|--------|
| Dimension | $2^n \times 2^n$ | $b_1 \times b_1$ |
| Indices | System states a, b | Cartan parameters r, s |
| What it measures | Overlap of environment states | Sensitivity of environment state to parameters |
| Depends on | System state pairs (a,b) | Derivatives w.r.t. c_r, c_s |
| Physical meaning | Distinguishability of system states | Precision bound for parameter estimation |

B博士's Section 1.3 "critical identity" (line 112-124) says: "Both are constructed from the same $\kappa_k(a)$ coefficients." This is true but irrelevant. The Hamiltonian of a harmonic oscillator and its partition function are both constructed from the same energy eigenvalues — that does not make them "the same matrix."

### 4.3 B博士 Already Concedes This

Section 6.1 (Honest Weaknesses) states: **"The Gram Matrix is Not EXACTLY the QFIM."** The precise text reads:

> "Strict equality holds only for pure environment states and the specific measurement basis $\{|k\rangle_E\}$. For general system-environment states... the Gram matrix is related to, but not identical to, the QFIM... The QFIM is not the Gram matrix itself, but rather the Gram matrix's Hessian in parameter space."

This is a **self-retraction of the central claim**. The paper's title and executive summary say "Gram matrix IS the QFIM." The honesty section says it isn't. Which is it?

If the Gram matrix is only approximately related to the QFIM via a Hessian, then:
1. The QEC-Metrology trade-off (Theorem in Section 2.2) does not follow from the Gram structure alone
2. The "Clifford blindness" prediction (which relies on f(c) computed from the Gram matrix) may not be exact
3. The entire metrology wall is a first-order approximation, not a fundamental identity

### 4.4 The Index Mismatch is a Category Error

The Gram matrix $G[a,b]$ tells you how distinguishable the environment states $|E_a\rangle$ and $|E_b\rangle$ are. The QFIM $F_{rs}$ tells you how sensitive $|E_a\rangle$ is to small changes in $c_r$ and $c_s$. The indices $a,b$ run over system states (size $2^n$). The indices $r,s$ run over Cartan parameters (size $b_1$).

Even if both matrices are functions of the same underlying environment state structure, they are functions of **different arguments** evaluated at **different points**. Calling them "the same" is like saying the metric tensor $g_{\mu\nu}(x)$ on a manifold IS the Riemann curvature tensor $R_{\mu\nu\rho\sigma}(x)$ because both are built from derivatives of the metric — a basic confusion of tensor order.

### 4.5 Fix Required

1. Delete all claims that "the Gram matrix IS the QFIM." Replace with the corrected statement: "The QFIM can be expressed in terms of derivatives of the Gram matrix."
2. Re-derive all subsequent results (trade-off theorem, Clifford blindness, pointer basis connection) using the corrected relationship. This will likely change the quantitative predictions.
3. Acknowledge that the index mismatch means there is no direct equality between the two objects.

---

## Attack 5: The QEC-Metrology Trade-off

**Severity: FATAL**

### 5.1 The Claim

B博士 derives a "Quantum Cramér-Rao Uncertainty Principle for Error Correction":
$$\varepsilon_{\text{QEC}} \times N \times (\Delta c)^2 \geq \frac{1 - G(x_L)}{2 \cdot b_1 \cdot f(c)}$$

### 5.2 It Depends on the Round 1 Error (Still Unfixed)

The derivation uses $\varepsilon_{\text{QEC}} = (1 - G(x_L))/2$, which Round 1 proved is an **upper bound**, not an equality. With the inequality:
$$\varepsilon_{\text{QEC}} \leq \frac{1 - G(x_L)}{2}$$

the trade-off inequality becomes:
$$\varepsilon_{\text{QEC}} \times N \times (\Delta c)^2 \leq \frac{1 - G(x_L)}{2 \cdot b_1 \cdot f(c)}$$

But the RHS is now an upper bound on the product, not a lower bound! The inequality direction reverses the meaning of the result. Instead of "QEC and metrology cannot both be good," we get "QEC and metrology cannot both be WORSE than this bound" — which is a trivial statement.

For the trade-off to be meaningful as a lower bound, we would need a **lower bound** on $\varepsilon_{\text{QEC}}$ (showing QEC cannot do better than some floor). But the Round 1 error showed that $(1-G(x_L))/2$ is an UPPER bound, and the true $\varepsilon_{\text{QEC}}$ can be much smaller (because correctable errors are removed by syndrome measurement). With no lower bound on $\varepsilon_{\text{QEC}}$, the trade-off product can be arbitrarily small, making the "uncertainty principle" vacuous.

### 5.3 The Trade-off May Be a Tautology

Even if we ignore the Round 1 error, the trade-off inequality has the form:
$$\text{(upper bound on QEC error)} \times \text{(lower bound on estimation error)} \geq \text{something}$$

This is the product of two independent bounds. It is not a trade-off — it is two separate facts about the same system:

1. *Fact 1*: The logical error rate is bounded above by Gram decay of the logical operator.
2. *Fact 2*: The estimation precision is bounded below by the Cramér-Rao bound.

Multiplying these bounds does not create a new physical constraint. It is algebraically equivalent to stating both facts separately. The product inequality is a tautology — it adds no information beyond Facts 1 and 2 individually.

A genuine trade-off would require showing that improving one quantity **necessarily worsens** the other, i.e., that the set of achievable $(\varepsilon_{\text{QEC}}, \Delta c)$ pairs has a Pareto frontier that neither quantity can cross. The product of two independent bounds does not establish this.

### 5.4 The Small-c "Universal Constant" is Artifact

Prediction 3 claims that $\lim_{c \to 0} \varepsilon_{\text{QEC}} \times (\Delta c)^2 \times N \times b_1 = 1/320$. But this constant comes from plugging specific numbers into an inequality that was already shown to be non-binding. Worse, B博士's own recomputation gives different constants (1/32, 1/64) depending on the encoding, showing that even the claimed "universality" is code-dependent.

### 5.5 Fix Required

1. Derive a genuine **lower bound** on $\varepsilon_{\text{QEC}}$ (not an upper bound disguised as equality). This is the prerequisite for any trade-off.
2. Prove that the Pareto frontier is non-trivial — i.e., that improving QEC necessarily degrades metrology and vice versa. The product of bounds does not prove this.
3. If no lower bound on $\varepsilon_{\text{QEC}}$ exists (because standard QEC can make it arbitrarily small), acknowledge that the "trade-off" is a one-way street: metrology can be arbitrarily good at fixed QEC performance, limited only by the Cramér-Rao bound, which QEC does not affect.

---

## Attack 6: The "Clifford Blindness" Claim

**Severity: SEVERE**

### 6.1 The Claim

At Clifford points $c = \pi/2$, $f(c) = 0$, implying $\Delta c \to \infty$ — "metrological blindness." This is the metrological dual of the Gottesman-Knill theorem.

### 6.2 The Observation is Trivial, The Interpretation is Misleading

At $c = \pi/2$, the Gram factor is $\cos(\pi/2 \cdot \Delta)^2$. For $\Delta \in \{0, \pm 2, \pm 4\}$:
- $\Delta = 0$: $\cos(0)^2 = 1$
- $\Delta = \pm 2$: $\cos(\pm\pi)^2 = 1$
- $\Delta = \pm 4$: $\cos(\pm 2\pi)^2 = 1$

So $G[a,b] = 1$ for all $a,b$. The environment state $|E_a\rangle$ is **independent** of $a$ — all system states produce the same environment state. Therefore $\partial_c |E_a\rangle = 0$ — no derivative, no Fisher information.

But this is just saying: "at a parameter value where the channel doesn't depend on the parameter, you can't estimate the parameter." This is not "blindness" — it is elementary calculus. It is equally true of any physical system at any stationary point of any observable with respect to any parameter.

The claim that this is "the metrological dual of Gottesman-Knill" is a false equivalence. Gottesman-Knill is a theorem about **classical simulatability of quantum circuits** — a computational complexity statement. The fact that Fisher information vanishes at a stationary point is a **calculus identity** — a statement about derivatives. These are not duals; they operate in different conceptual domains and have different physical content.

### 6.3 B博士 Already Concedes This May Be an Artifact

Section 6.3: "The Clifford Blindness Prediction May Be an Artifact... the second-order term in the Fisher information (involving $\partial^2 p/\partial c^2$) may remain finite even at the Clifford point." 

If the second-order Fisher information (which contributes to estimation via the Bhattacharyya bound, not the Cramér-Rao bound) is finite, then $\Delta c$ does NOT diverge — it is merely larger than the first-order bound would suggest. The "blindness" would be "blurred vision" — reduced but finite sensitivity. This is a significantly weaker claim.

### 6.4 Fix Required

1. Compute the second-order (Bhattacharyya) bound at $c = \pi/2$. If it is finite, retract the claim that $\Delta c \to \infty$.
2. Remove the false equivalence with Gottesman-Knill, or provide a rigorous mapping between classical simulatability and Fisher information vanishing that goes beyond the fact that both involve Clifford gates.
3. Clarify that the vanishing Fisher information at $c = \pi/2$ is a generic property of any parameter at a stationary point of the likelihood, not a special feature of Clifford gates.

---

## Attack 7: Experimental Feasibility

**Severity: SEVERE**

### 7.1 The Claim

B博士's Section 5 claims the predictions are "testable on today's hardware with zero QEC overhead" and provides a detailed protocol.

### 7.2 The Fisher Information is NOT Directly Measurable

B博士's protocol (Section 5.3) proposes to:
1. Collect measurement data at fixed $c$
2. Estimate probabilities $\hat{p}(m|a)$
3. **Vary $c$ and repeat**
4. Fit $\partial p/\partial c$ from the data
5. Compute Fisher information

Step 3 is the problem. The Fisher information $F(c) = \mathbb{E}[(\partial_c \ln p)^2]$ is a **theoretical quantity** computed from the model's derivative. To estimate it experimentally, you need to measure $p(m|a, c)$ at multiple nearby values of $c$ and numerically differentiate. This introduces:

- **Discretization error**: The finite difference $\Delta p / \Delta c$ approximates $\partial p / \partial c$ with error $O(\Delta c)$. For the Fisher information (which involves squares of derivatives), this error is $O(\Delta c^2)$. To beat this down, you need very fine $c$-grids — which requires **precise control** of the Cartan parameter.

- **Precision requirement**: On IBM Q, the RZZ gate angle implements the Cartan parameter. Gate calibration precision is typically $\sim 10^{-3}$ radians. For $c = 0.5$, B博士 predicts $\Delta c \approx 0.002$ — which is comparable to the calibration precision. The experiment would be **calibration-limited**, not statistics-limited.

- **Drift**: Gate parameters drift over time (hours). A full parameter sweep across multiple $c$ values requires stable calibration across the entire experiment duration.

### 7.3 SPAM Errors Break Unbiased Estimation

The Cramér-Rao bound applies to **unbiased** estimators. On a real device with state preparation and measurement (SPAM) errors:

$$p_{\text{measured}}(m|a) = \sum_{m'} R_{m,m'} p_{\text{true}}(m'|a; c) + \text{preparation errors}$$

where $R$ is the measurement response matrix. If $R$ is not perfectly characterized (and it never is), the estimator for $c$ will be biased. With biased estimation, the Cramér-Rao bound does not apply — the actual variance can be larger OR smaller than $1/F(c)$.

B博士 mentions SPAM mitigation (Section 6.4) but does not analyze how residual SPAM errors affect the bound. This is a gap between the theoretical bound and the proposed experiment.

### 7.4 The Protocol's Own Numbers Show the Problem

For $b_1 = 4$, $c = 0.5$, $N = 5000$: the predicted $\Delta c \approx 0.001$. With $b_1 = 4$, the circuit requires $(b_1+1) + 2b_1 = 5 + 8 = 13$ qubits and $b_1 \times (\text{CNOTs per ring}) \approx 12$ CNOT gates. At 98% two-qubit gate fidelity (optimistic for 13 qubits), the total circuit fidelity is $\approx 0.98^{12} \approx 0.78$. The 22% error rate from gates alone dwarfs the Fisher information signal, which is derived assuming perfect gates.

### 7.5 Fix Required

1. Provide a complete error budget including gate infidelity, SPAM errors, and calibration drift. Show that the predicted $\Delta c$ is achievable after accounting for all error sources.
2. Explicitly construct an unbiased estimator that works in the presence of realistic SPAM errors, or derive the biased Cramér-Rao bound for the proposed protocol.
3. Acknowledge that the Fisher information is a model-derived quantity, not a direct observable, and the experimental protocol measures an **estimator** whose variance may exceed the Cramér-Rao bound.

---

## Attack 8: Internal Consistency (A博士 vs B博士)

**Severity: FATAL**

### 8.1 The Contradiction

A博士 (Section 2): The Gram channel is **non-Markovian** and has multi-time correlations that differ from the single-time Pauli Z description. Ring $r$ and ring $r+1$ have correlated effects that depend on the full history.

B博士 (Section 1.3): The Fisher information is **additive**: $F(c) = b_1 \cdot f(c) + O(1)$, with each ring contributing independently to the total Fisher information.

These are **incompatible**. Additivity of Fisher information requires that measurements on different rings are **statistically independent** (or at least that their contributions to the Fisher information are additive). If ring-ring correlations exist (as A博士 claims via non-Markovianity), then the Fisher information from $b_1$ rings is NOT $b_1 \cdot f(c)$ — it includes cross-terms that may enhance or suppress the total.

To see this explicitly: for correlated measurements $k_1$ and $k_2$, the joint probability $p(k_1, k_2|a; c) \neq p(k_1|a; c)p(k_2|a; c)$. The joint Fisher information:
$$F_{12}(c) = \mathbb{E}\left[\left(\frac{\partial}{\partial c} \ln p(k_1, k_2)\right)^2\right]$$
does NOT decompose as $F_1 + F_2$ when the measurements are correlated. The cross-term $\mathbb{E}[\partial_c \ln p(k_1) \cdot \partial_c \ln p(k_2)]$ may be positive (super-additivity) or negative (sub-additivity).

### 8.2 The Specific Mechanism of Contradiction

A博士's multi-time analysis (Section 2.1) shows that for $N \geq 2$ applications, $\Phi_{\text{Gram}}^N \neq \Phi_{\text{Pauli}}^N$. This means the Gram channel has **memory** — the effect of ring $r$ depends on what happened in rings $1, \ldots, r-1$. If the channel has memory, then the environment states after ring $r$ are not independent of the environment states after ring $r-1$. The Fisher information from ring $r$ then depends on the outcomes of previous rings — breaking additivity.

B博士's $F(c) = b_1 \cdot f(c)$ assumes that each ring provides an independent "look" at the Cartan parameter $c$, with the total Fisher information scaling linearly. This is the additivity property of Fisher information for **independent and identically distributed** (i.i.d.) measurements. Non-Markovian dynamics violate the "independent" part.

### 8.3 Both Cannot Be True

The manuscript asserts two propositions:

> (A) The Gram channel is non-Markovian; ring-ring correlations make multi-time behavior different from single-time behavior [A博士]

> (B) Fisher information from rings is additive; $F = b_1 \cdot f(c)$ [B博士]

If (A) is true, (B) fails (Fisher information is not additive for correlated rings).
If (B) is true, (A) fails (additivity requires independence, which requires Markovianity).

The authors must choose. They cannot publish a manuscript whose two halves contradict each other on a question (Markovianity) that is central to both.

### 8.4 Fix Required

1. Resolve whether the Gram channel is Markovian or non-Markovian. This is a prerequisite for both lines of argument.
2. If Markovian: A博士 must retract the non-Markovianity claim and multi-time distinguishability result (Section 2) or show they are consistent with Markovianity.
3. If non-Markovian: B博士 must re-derive the Fisher information scaling with correlated ring contributions, which will change the $1/\sqrt{b_1}$ scaling and all quantitative predictions.
4. The alternative — both claims surviving — requires a proof that the specific type of non-Markovianity in (A) does not affect Fisher information additivity. No such proof exists in the manuscript.

---

## Summary of Attacks

| # | Attack | Target | Severity | Core Issue |
|---|--------|--------|----------|------------|
| 1 | Pauli Twirl = Non-Markovian | A博士 Sec 1-2 | **FATAL** | Walsh-Hadamard is not a Pauli twirl; self-contradiction in $\lambda$ computation |
| 2 | Coherent Enhancement Factor | A博士 Sec 3 | **FATAL** | G&D applies to coherent (unitary) errors; Gram decay is decoherence. $\varepsilon$ mapping is unjustified |
| 3 | Non-Cartan Non-Pauli | A博士 Sec 4 | SEVERE | Pauli frame tracking removes basis-dependent non-Pauli structure |
| 4 | QFIM = Gram Identity | B博士 Sec 1 | **FATAL** | Category error: different matrix dimensions, index spaces, and physical meanings. Self-retracted in Section 6.1 |
| 5 | QEC-Metrology Trade-off | B博士 Sec 2 | **FATAL** | Depends on Round 1 error ($P_L$ bound vs equality); product of independent bounds is tautology, not trade-off |
| 6 | Clifford Blindness | B博士 Sec 3 | SEVERE | Trivial consequence of derivative vanishing at stationary point; false equivalence with Gottesman-Knill; second-order terms may be finite |
| 7 | Experimental Feasibility | B博士 Sec 5 | SEVERE | Fisher information is theoretical quantity not directly measurable; SPAM + calibration errors dominate at predicted precision |
| 8 | Internal A博士/B博士 Consistency | Both | **FATAL** | Non-Markovianity (A) contradicts Fisher information additivity (B). Manuscript cannot assert both |

---

## The SINGLE Most Damaging Finding

**Attack 4 (Category Error) + Attack 5 (Tautology) together form a complete demolition of B博士's metrology wall.**

B博士's central claim is that the Gram matrix IS the QFIM, and this creates a fundamental trade-off. But:

1. The Gram matrix and QFIM are different objects (Attack 4). They have different dimensions, different index spaces, and different physical interpretations. B博士 concedes this in Section 6.1.
2. Even if we accept the claimed relationship, the trade-off inequality uses the Round 1 bound $\varepsilon_{\text{QEC}} = (1-G(x_L))/2$, which was proven false as an equality. With the corrected inequality $\varepsilon_{\text{QEC}} \leq (1-G(x_L))/2$, the trade-off direction reverses or becomes vacuous (Attack 5).
3. Even if both issues were fixed, the trade-off is the product of two independent bounds — a tautology, not a physical constraint.

**The metrology wall is built on sand. Two independent fatal errors (category error + reliance on Round 1 false equality) make the entire edifice unsalvageable in its current form.**

Meanwhile, the **internal inconsistency** (Attack 8) kills any possibility of an integrated manuscript: A博士 and B博士 contradict each other on whether the Gram channel is Markovian, which affects both of their central claims.

---

## Bottom Line: What Survives?

From A博士:
- **Survives**: The recognition that the Walsh-Hadamard transform is exact at single time (this was already established in Round 1).
- **Survives with qualification**: The multi-time analysis for n >= 2 showing $\Phi_{\text{Gram}}^N \neq \Phi_{\text{Pauli}}^N$ for N >= 2. This is mathematically interesting but its physical relevance for QEC (where syndrome measurements project at each round) is not established.
- **Survives with qualification**: The non-Cartan generalization. However, Pauli frame tracking / randomized compiling may handle this in practice.
- **Dies**: Non-Markovianity from Pauli-Lindblad parameters (mathematical error in $\lambda$ computation).
- **Dies**: Coherent enhancement factor (category error between coherent errors and decoherence).

From B博士:
- **Survives** (in corrected form): The observation that Fisher information about Cartan parameters can be extracted from the environment. This is essentially a reframing of known parameter estimation problems in open quantum systems. It is correct but not novel.
- **Dies**: Gram matrix = QFIM (category error, self-retracted).
- **Dies**: QEC-Metrology uncertainty principle (depends on Round 1 false equality; product of independent bounds).
- **Survives with major revision**: Clifford blindness, but only as the trivial statement that Fisher information vanishes where the likelihood is stationary. Not a deep result.
- **Survives**: The proposed experiment, as a protocol for measuring Cartan parameters (not for testing a fundamental trade-off). This is engineering, not fundamental physics.

---

## Journal Recommendation

**The revised manuscript should be REJECTED from Physical Review Letters.**

The Round 1 error ($P_L$ equality should be inequality) remains unfixed. The manuscript pivots to new claims rather than addressing the central flaw, and several of those new claims are either mathematically incorrect (Attack 1, Attack 2), logically inconsistent with each other (Attack 8), or based on category errors (Attack 4).

**What could be publishable after thorough revision:**

1. **A博士's Section 2 (multi-time distinguishability)**, if reworked to (a) provide rigorous proof of the Walsh-Hadamard vs convolution inequality for n >= 2, (b) establish physical relevance for QEC by showing that syndrome projection does NOT eliminate the multi-time effect, and (c) correctly identify that the Walsh-Hadamard transform is NOT a Pauli twirl. **Venue: PRA** (as a technical result on multi-time channel distinguishability).

2. **B博士's observation about Fisher information extraction**, if reworked to (a) remove the false "Gram = QFIM" identity, (b) properly handle the correlated ring structure, (c) clarify that this is a parameter estimation protocol, not a fundamental trade-off, and (d) resolve the Markovianity inconsistency with A博士. **Venue: PRA or Quantum** (as a metrology protocol).

3. **The non-Cartan generalization**, if reworked to (a) analyze whether Pauli frame tracking removes the non-Pauli structure, and (b) provide explicit numerical examples of residual non-Pauli effects after optimal frame alignment. **Venue: PRA**.

**Neither the integrated manuscript nor either half independently meets the PRL standard of broad fundamental significance with rigorous proof.** The crucial errors (mathematical in Attack 1, conceptual in Attacks 2 and 4, logical in Attack 8) are too severe for a "revise and resubmit." A complete rewrite from corrected foundations would be required.

---

## References Cited in This Review

1. J. Hines et al., "Simulating Quantum Error Correction beyond Pauli Stochastic Errors," arXiv:2603.18457 (2026).
2. J. Kattemölle, B. Gulácsi, G. Burkard, "Non-Markovianity induced by Pauli-twirling," arXiv:2602.08464 (2026).
3. D. Greenbaum, Z. Dutton, "Modeling coherent errors in quantum error correction," Quantum Sci. Technol. 3, 015007 (2018).
4. J.J. Wallman, J. Emerson, "Noise tailoring for scalable quantum computation via randomized compiling," Phys. Rev. A 94, 052325 (2016).
5. S.L. Braunstein, C.M. Caves, "Statistical distance and the geometry of quantum states," Phys. Rev. Lett. 72, 3439 (1994). [Standard reference on QFIM, notably absent from the manuscript]
6. M.G.A. Paris, "Quantum estimation for quantum technology," Int. J. Quantum Inf. 7, 125 (2009). [Standard review of QFIM and Cramér-Rao bound]
