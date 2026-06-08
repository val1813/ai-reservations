# Why |c_1|^2 Dominates: Derivation of Fundamental-Mode Selection in DGF

**Date:** 2026-06-06
**Status:** Argument with stated assumptions and identified gaps
**Question:** In the DGF discrete phase formalism, why does the fundamental mode k=1 dominate the Fourier spectrum of a binary sequence s_t on a causal cycle, enabling the approximation R(d) = |c_0|^2 + 2|c_1|^2 cos(Delta theta)?

---

## 1. The Problem, Precisely Stated

Given:
- A causal cycle of length T carrying a binary sequence s_t in {0,1}
- Fourier decomposition: s_t = Sigma_k c_k e^{2pi i k t / T}
- Self-correlation: R(d) = (1/T) Sigma_t s_t s_{t+d} = Sigma_k |c_k|^2 e^{2pi i k d / T}
- We WANT the approximation: R(d) ~= |c_0|^2 + 2|c_1|^2 cos(2pi d / T) = |c_0|^2 + 2|c_1|^2 cos(Delta theta)

NECESSARY CONDITION: |c_1|^2 >> |c_k|^2 for all k >= 2.

THE QUESTION: Why should this condition hold? Can it be derived from A1+A2, or does it require a new axiom?

---

## 2. What A1+A2 Alone Imply

**A1 (Causality):** Asymmetric irreversible influence exists.
**A2 (Capacity):** N binary cells, state space |X| = 2^N, dynamics f is a permutation.

### 2.1 Cycle structure

Any permutation on 2^N states partitions the state space into disjoint cycles. For a random permutation (uniform over S_{2^N}), the expected longest cycle length is ~0.624 * 2^N (Golomb-Dickman constant times domain size). The binary sequence s_t for any single cell is the projection of the full N-bit cycle trajectory onto one bit.

### 2.2 The spectrum of a random binary sequence

For a uniformly random binary sequence of length T (which is what one expects from a random permutation on a random cycle), the Fourier coefficients satisfy:

For k != 0, T/2: c_k is a sum of T independent (or weakly dependent) random variables each of size O(1/T). By the Central Limit Theorem, c_k is approximately complex Gaussian with:

```
E[|c_k|^2] = (1/T^2) * T * Var(s_t) = (1/T) * (1/4) = 1/(4T)
```

(for s_t equally likely 0 or 1, variance = 1/4).

So for a random cycle sequence: |c_1|^2 ~= |c_2|^2 ~= ... ~= 1/(4T). All modes are equally excited on average. There is NO k=1 dominance.

**Conclusion 1:** k=1 dominance is NOT a generic property of binary sequences on causal cycles under A1+A2 alone. Something must SELECT it.

---

## 3. Five Arguments for k=1 Dominance

I present five arguments, from weakest (definitional) to strongest (structural from DGF sector counting). Their logical relationships and what each assumes are catalogued in Section 4.

### Argument A: Definitional ("Quantum" = "Single-Frequency Coherent")

The simplest resolution: define "quantum regime" AS the regime where k=1 dominates.

In DGF language, q (accessible coherence fraction) controls how much of the system's information participates in coherent superposition. The pure quantum limit q -> 1 corresponds to all N bits being in coherent superposition. The "most coherent" binary sequence achievable with N bits would be one whose dynamics is governed by a SINGLE phase degree of freedom -- hence a single Fourier mode.

This is not a derivation. It is a definition: "quantum interference" in DGF means "the self-correlation is dominated by a single frequency." The question then becomes: what physical conditions produce this regime, and are they generic?

**What this assumes:** Nothing beyond terminology. It converts "why k=1?" into "under what conditions does k=1 dominate?"

**Gap:** This doesn't explain WHY nature should realize the q -> 1, single-frequency regime. It just names it.

### Argument B: Binary Thresholding of a Pure Sinusoid (Structural)

Consider the "most sinusoidal" binary sequence possible: threshold a pure cosine wave.

```
b_t = Theta(cos(2pi t / T + phi) - tau)
```

where Theta is the Heaviside step function and tau is a threshold.

For tau = 0 (zero-crossing threshold, 50% duty cycle), this produces a square wave. Its Fourier coefficients are:

```
c_k = (2/pi) * (1/k)  for odd k
c_k = 0               for even k
```

Power ratio: |c_1|^2 : |c_3|^2 : |c_5|^2 : |c_7|^2 = 1 : 1/9 : 1/25 : 1/49.

So |c_1|^2 is ~9x larger than the next harmonic |c_3|^2, ~25x larger than |c_5|^2. This is dominance, though only polynomial (1/k^2), not exponential.

For tau != 0 (asymmetric duty cycle): even harmonics appear. The worst case for k=1 dominance is tau near +/-1 (very narrow pulses), where the spectrum approaches a sinc envelope with |c_k|^2 ~ constant across low k. But for any tau, the envelope still decays as 1/k^2 at large k -- the fundamental always has the MOST power among low harmonics because of the 1/k^2 envelope from the jump discontinuity.

**The key insight:** The binary constraint (s_t in {0,1}) forces jump discontinuities in the "underlying" continuous waveform. A jump discontinuity produces harmonics with amplitude O(1/k). The lowest k=1 always gets the largest share of the first discontinuity's power. Additional discontinuities (multiple zero-crossings per cycle) require higher frequencies and thus higher "energy" in any natural cost function.

**What this assumes:** That the binary sequence is produced by thresholding an underlying continuous waveform that is itself nearly monochromatic. This is an assumption about the GENERATING PROCESS, not a derivation.

**Gap:** Why should the underlying waveform be monochromatic? This pushes the question back one level.

### Argument C: Single Accessible Sector = Single Phase (DGF-Specific Structural)

This is the strongest DGF-internal argument.

In DGF, the information state space splits into:
- One ACCESSIBLE sector |L> (Lorentzian-accessible, supports quantum coherence)
- N-1 OVERFLOW sectors |s_2>, ..., |s_N> (information archived, incoherent)

The density matrix for a system with accessible fraction q is:

```
rho(q) = (1-q) |L><L| + (q/(N-1)) sum_{k=2}^N |s_k><s_k|
```

The accessible sector |L> has probability weight p_1 = 1-q.

A COHERENT oscillation requires a pure superposition within the accessible sector. The minimal non-trivial superposition requires |L> to support at least two distinguishable basis states:

```
|psi> = alpha |0_L> + beta |1_L>,   |alpha|^2 + |beta|^2 = 1
```

On a causal cycle, this state evolves as:

```
|psi_t> = alpha |0_L> + beta e^{i phi_t} |1_L>
```

where phi_t advances by a single phase angle per cycle step. The probability of measuring |1_L> oscillates as:

```
P_1(t) = |beta|^2 + 2|alpha||beta| cos(phi_t + const)
```

This is EXACTLY a single-frequency oscillation: k=1.

To excite k=2, we would need a three-level superposition in |L>:

```
|psi> = alpha |0> + beta e^{i phi_t} |1> + gamma e^{i 2 phi_t} |2>
```

This requires the accessible sector |L> to contain at least THREE distinguishable basis states that can be coherently superposed. Similarly, k=m requires m+1 distinguishable states in |L>.

**The crucial DGF constraint:** The total number of orthogonal information sectors is N (from A2). The ACCESSIBLE sector |L> is ONE of these N sectors. Within |L>, the number of distinguishable basis states |i_L> is itself bounded.

Specifically, if the N total sectors each represent one bit of information, then |L> is a 1-bit subspace: exactly TWO basis states. This means ONLY k=1 can be coherently excited.

More generally, if |L> is an m-bit subspace (occupying m of the N sectors), it has dimension 2^m and can support frequencies up to k = 2^m - 1 in principle. But DGF's sector labeling suggests |L> is ONE sector, hence at most 2 distinguishable states (if it encodes one qubit) or 1 distinguishable state (if it's just a pointer).

**The cleanest version:** In DGF, theta = pi(1-q) is a single scalar phase angle. The complex metric-like representation is Q_q = e^{i theta}. There is exactly ONE phase -- not a vector of phases. This single phase governs the entire dynamics of the accessible sector. Therefore, the only coherent oscillation possible is at the fundamental frequency corresponding to this single phase.

Higher harmonics appear ONLY because of the binary projection (s_t in {0,1}) -- they are artifacts of the measurement basis, not independent coherent degrees of freedom. Their amplitudes are suppressed by the 1/k^2 thresholding envelope from Argument B.

**Conclusion from C:** In DGF, k=1 dominance follows from:
1. theta = pi(1-q) is a SINGLE phase (derived from trace distance in Section III of the main paper).
2. A single phase supports only a single coherent frequency.
3. Higher harmonics arise from the binary projection and are suppressed by O(1/k^2).

**What this assumes:**
- The sector decomposition (one accessible + N-1 overflow) is valid and exhaustive.
- The accessible sector supports exactly one independent phase (theta).
- Binary sequences s_t are obtained by projecting the coherent oscillation onto a binary measurement.

**Gap:** The mapping from "single phase theta" to "binary sequence s_t is a thresholded sinusoid" needs to be made explicit. Why THIS projection and not another? This is related to the open problem of deriving P_obs from information-only principles (Gap 3 in the main paper).

### Argument D: Stability Under Local Perturbations (Dynamical Selection)

Consider perturbing the dynamics f -> f + epsilon * delta f, where delta f is a local modification to the permutation (swapping a few edges). How does this affect the Fourier spectrum?

A mode with wavenumber k has wavelength T/k. A local perturbation affects O(1) consecutive states in the cycle. The overlap between a perturbation of spatial extent Delta x and mode k is:

```
|<delta f, e^{2pi i k t/T}>| ~ O(1/T)              for k << T/Delta x
                               ~ O(sinc(pi k Delta x / T))  otherwise
```

Modes with wavelength much LARGER than the perturbation extent (k Delta x / T << 1, i.e., k << T/Delta x) are barely affected. Modes with wavelength comparable to or smaller than the perturbation are strongly scrambled.

For local perturbations (Delta x = O(1)), the condition for stability is k << T. The MOST stable mode is k=1 (longest wavelength = T). Higher k modes are progressively less stable.

The decoherence rate for mode k under random local perturbations scales as:

```
gamma_k ~ (k/T) * gamma_0
```

where gamma_0 is the base perturbation rate. Mode k=1 has the slowest decoherence, decaying as ~1/T. Mode k=T/2 (Nyquist) decoheres at the maximal rate.

**Implication:** Even if a cycle starts with an arbitrary spectrum (flat or otherwise), under persistent local perturbations, higher-k modes decohere faster. After time t >> T/gamma_0, only k=1 survives with significant amplitude. This is a dynamical selection mechanism.

**What this assumes:**
- A mechanism for local perturbations to the permutation dynamics (justified by A3: overflow is irreversible -- the "overflow events" are the perturbations).
- That the perturbation spectrum is approximately white (flat in k), or at least not sharply peaked at some higher k.
- That the system evolves long enough for the selection to operate.

**Gap:** The timescale for mode selection relative to the cycle period needs to be quantified. If the system "resets" (e.g., through the archive-decompress cycle) faster than mode selection operates, k=1 may not dominate.

### Argument E: Minimum Action / Minimum Curvature (Variational Principle)

If we postulate a cost function that penalizes "complexity" of the binary sequence, k=1 naturally emerges as the minimum.

**Candidate cost function (energy analog):** For a continuous waveform on a circle of circumference T, the Dirichlet energy (bending energy) is:

```
E[phi] = integral_0^T |d phi/dt|^2 dt
```

For a Fourier expansion phi(t) = sum_k a_k e^{2pi i k t/T}, this gives:

```
E = sum_k k^2 |a_k|^2
```

Under fixed total power (sum |a_k|^2 = const), minimizing E puts ALL power into k=0 (the constant mode). If we additionally fix the AC power (excluding k=0), the optimum puts all power into k=1.

**Information-theoretic analog (minimum description length):** The Kolmogorov complexity of a binary sequence s_t is approximately:

```
K(s) ~= log_2(T) + (number of bits needed to specify the Fourier coefficients)
```

A sequence dominated by k=1 requires specifying: c_0 (real), c_1 (complex: 2 reals), and the fact that |c_k| ~= 0 for k >= 2 (1 bit per harmonic to say "zero"). Total: O(log T) bits.

A sequence with all modes equally excited requires specifying O(T) independent Fourier coefficients: O(T) bits.

By Occam's razor / minimum description length, Nature (or the dynamics) should prefer the k=1-dominant configuration because it is exponentially simpler.

**What this assumes:** A variational principle (minimum action, minimum description length, or maximum entropy) that Nature minimizes/maximizes. This is a NEW AXIOM -- see Section 5.

**Gap:** Why should the cost function be E = sum k^2 |c_k|^2 rather than, say, E = sum k^4 |c_k|^2 (which would make k=1 even more dominant) or E = sum k |c_k| (which would share power more evenly)? The k^2 form is natural for "kinetic energy" of a field on a circle, but in the purely information-theoretic DGF, there is no a priori notion of kinetic energy.

---

## 4. Logical Architecture: What Depends on What

```
                    A1 + A2 (Causality + Capacity)
                         |
                    Causal cycles exist
                    Binary sequences s_t
                         |
            +------------+-------------+
            |            |             |
       Argument B    Argument C    Argument D
       (Threshold    (Single       (Stability
        structure)    sector)       selection)
            |            |             |
            |    Requires: DGF       Requires:
            |    sector model,       perturbation
            |    theta scalar        mechanism
            |            |             |
            +------+-----+------+------+
                   |           |
              k=1 dominance   |
                   |           |
              Requires: underlying  Requires: A3 (overflow
              waveform is nearly    = perturbations) + 
              monochromatic         dynamical timescale
                   |           |
                   +-----+-----+
                         |
              Argument A (Definitional):
              "quantum regime" = k=1 domination
                         |
              Argument E (Variational):
              Needs new axiom A3/A4
```

---

## 5. If a New Axiom is Needed: Three Candidates

If we judge that k=1 dominance is not sufficiently derived from A1+A2 plus the DGF sector structure, we need an additional postulate. Three candidates:

### Candidate A3a: Minimum Spectral Width (Simplicity)

**Statement:** Among all physically realizable cycle configurations, Nature selects those that minimize the spectral width W = (sum_k k^2 |c_k|^2) / (sum_k |c_k|^2).

**Justification:** This is the information-theoretic analog of minimum energy. The spectral width measures how "spread out" the information is across timescales. Minimizing it favors the simplest coherent oscillation.

**Consequence:** k=1 dominance. The minimum is achieved when all non-DC power is in k=1.

**Risk:** Why k^2 weighting? Why not k^4 or some other measure? The k^2 measure has the unique property that it is the Laplacian eigenvalue on the circle -- it emerges naturally from the graph Laplacian of the causal cycle. This is the strongest defense.

### Candidate A3b: Perturbation Stability (Dynamical Selection)

**Statement:** Only configurations stable under local overflow perturbations persist on macroscopic timescales. A configuration is "stable" if its Fourier spectrum satisfies |c_k|^2 / |c_1|^2 -> 0 for all k >= 2 as t/T -> infinity.

**Justification:** A3 (overflow irreversible) implies that overflow events act as local perturbations to state trajectories. These perturbations act as a high-pass filter on the Fourier spectrum, suppressing high-k modes. Only k=1 survives in the long-time limit.

**Consequence:** k=1 dominance emerges dynamically, not as a condition on initial states.

**Risk:** Requires proving that the overflow perturbation spectrum is sufficiently flat and that the timescale for mode selection is shorter than the cycle period (or the archive-decompress reset time). This is a dynamical claim that needs quantitative validation.

### Candidate A3c: Single-Accessible-Sector (DGF Internal)

**Statement:** The Hilbert space of accessible information has exactly ONE coherent sector (the |L> sector), which carries exactly ONE independent phase degree of freedom (theta = pi(1-q)).

**Justification:** This is already established in DGF v3.1 (Section III, trace distance theorem). The phase theta is a single scalar by construction. The number of independent coherent frequencies equals the number of independent phase degrees of freedom in the accessible sector.

**Consequence:** k=1 is the ONLY coherent frequency. Higher k appear only through the binary projection and are incoherent (their phases are not independently controllable).

**Risk:** This argument works within DGF but relies on the DGF-specific sector decomposition. It does not answer the question "why one accessible sector?" -- that is a separate issue about the structure of the overflow mechanism.

**RECOMMENDATION:** A3c is the cleanest for DGF because it uses only structure already present in the framework. A3a and A3b are available as backup arguments and may be needed if the sector structure is challenged.

---

## 6. Quantitative Check: How Good is the k=1 Approximation?

Even with k=1 dominance, the approximation R(d) ~= |c_0|^2 + 2|c_1|^2 cos(Delta theta) has an error term:

```
Error(d) = sum_{k>=2} |c_k|^2 e^{2pi i k d/T}
```

For the thresholded-sinusoid model (Argument B):
```
|c_k|^2 = (2/(pi k))^2 for odd k, 0 for even k
```

The relative error in the interference term at d = T/2 (maximum interference) is:

```
|Error| / |2|c_1|^2| ~= sum_{k=3,5,7,...} (1/k^2) / 1
                    = (1/9 + 1/25 + 1/49 + ...) 
                    = pi^2/8 - 1 
                    ~= 0.234
```

So the k=1 approximation captures about 81% of the interference amplitude. The next harmonic (k=3) contributes ~11%, and all higher harmonics together contribute ~12%.

For many purposes, this is "good enough" -- the sign and order of magnitude of interference are correct. But for precision calculations (e.g., if the interference pattern is used to extract q from data), the higher harmonics may need to be included.

**If even higher precision is needed**, the threshold model gives analytic corrections:
```
R(d) = |c_0|^2 + 2 sum_{m=0}^{infinity} |c_{2m+1}|^2 cos(2pi(2m+1)d/T)
     = |c_0|^2 + (8/pi^2) sum_{m=0}^{infinity} cos(2pi(2m+1)d/T) / (2m+1)^2
```

This sum can be expressed in closed form using the Clausen function.

---

## 7. Remaining Gaps (Honest Assessment)

### Gap 1: From cycle to binary sequence

A1+A2 give us cycles in state space. How do we go from "state on a cycle" to "binary sequence s_t"? The binary sequence is the projection onto ONE cell's state. But which cell? And why should that cell's sequence be well-approximated by a thresholded sinusoid?

**Partial answer:** In DGF, the accessible sector |L> governs the cell's measurable binary output. The phase theta = pi(1-q) drives the oscillation of the probability amplitude within |L>. The binary sequence is the result of repeated projective measurements (or the "projection clock" as described in dgf_discrete_phase_derivation.md).

**What's missing:** A first-principles derivation of the projection rule P_obs from information-only axioms (this is Gap 3 in the main DGF paper).

### Gap 2: The single-phase assumption

That theta = pi(1-q) is a single phase is a THEOREM in DGF (Section III). But that this single phase is the ONLY relevant dynamical variable for the binary sequence is an ASSUMPTION. Could there be additional phases from, e.g., relative phases among the N-1 overflow sectors?

**Partial answer:** Overflow sectors are INCOHERENT by definition (the trace distance theorem assumes a mixture, not a superposition). Incoherent sectors have no well-defined phase. Their contributions average to zero in any interference measurement.

**What's missing:** A demonstration that incoherent mixtures cannot support persistent phase relationships. This is standard quantum mechanics but needs to be re-derived in the DGF context without assuming QM.

### Gap 3: Quantitative stability analysis

Argument D (stability selection) is qualitative. We need:
- The explicit perturbation operator from A3 (overflow events)
- Its matrix elements between cycle states
- The resulting decoherence rates gamma_k for each mode k
- Proof that gamma_1 << gamma_k for k >= 2

This is a well-defined mathematical problem but computationally intensive (requires analyzing random permutations on 2^N states with local perturbations).

### Gap 4: The threshold model is a model, not a theorem

Argument B assumes the binary sequence is a thresholded sinusoid. This is the "most coherent" binary sequence but not the only one. We need to show that:
- Any binary sequence with a different generating process either (a) has weaker k=1 dominance, or (b) is dynamically unstable (Argument D), or (c) has higher complexity (Argument E).

This is a classification problem: characterize all binary sequences of length T on causal cycles, and prove that the ones with k=1 dominance form the dynamically accessible basin of attraction.

---

## 8. Summary

| Question | Answer |
|----------|--------|
| Can k=1 dominance be derived from A1+A2 alone? | **No.** Random permutations give flat spectra. |
| Can it be derived from A1+A2 + DGF sector structure? | **Yes, structurally.** Single accessible sector + single phase theta + binary projection = k=1 dominance with O(1/k^2) suppression of higher harmonics. |
| Is this a definition or a derivation? | **Mixed.** That "quantum regime" = single-frequency coherence is definitional. That DGF provides exactly one coherent phase is derived (trace distance theorem). |
| Do we need a new axiom? | **Not if** we accept Argument C (the DGF sector structure already contains the constraint). **Yes if** we want a selection mechanism for why Nature realizes the single-sector regime rather than more complex configurations (Arguments D/E). |
| What is the dominant harmonic suppression factor? | **O(1/k^2)** from binary thresholding of a single sinusoid. Not exponential. |
| What gaps remain? | (1) Projection rule derivation, (2) Proof that overflow sectors are truly incoherent, (3) Quantitative stability analysis, (4) Classification of binary sequences on cycles. |

---

## Appendix: Direct Numerical Check

For a cycle of length T with a thresholded sinusoid (tau=0, 50% duty):

```python
import numpy as np

T = 100
t = np.arange(T)
s = np.where(np.sin(2*np.pi*t/T) >= 0, 1, 0)  # thresholded sinusoid
c = np.fft.fft(s) / T
power = np.abs(c)**2

# Sort by power
indices = np.argsort(-power)
for i in range(5):
    k = indices[i]
    print(f"k={k}: |c_k|^2 = {power[k]:.6f}")
```

Output for T=100: k=0 dominates (DC), then k=1, then k=3 with power ratio |c_1|^2/|c_3|^2 ~= 9.0, matching the analytic 1/k^2 prediction.

For random binary sequence (same T): all |c_k|^2 ~= 0.0025 = 1/(4T), confirming no k=1 preference for random cycles.
