# Gram-to-QEC Bridge Theorem for DGF Causal Ring Networks

**Date:** 2026-06-11
**Status:** SOP Phase 1+2: Precise formulation and logical channel derivation
**Dependencies:** spectral_decoherence_theory.md (Gram decay mechanics), verify_p0_gram_rank.py (P0 numerical verification)
**Key Result (Corrected):** G_phys is NOT monotonic in Hamming distance; the bound on G_log depends on maximum G_phys across ALL cross-coset pairs, not just minimum-distance pairs. Sign-cancellation creates loopholes that must be accounted for.

---

## 0. Executive Summary

We establish the Gram-to-QEC bridge: the relationship between Gram matrix decay (from DGF causal rings with non-Clifford Cartan parameter c) and the logical error rate in a CSS stabilizer code. 

**The key corrected finding:** The naive bound G_log <= cos^2(2c)^{2d} is FALSE in general. G_phys is NOT monotonic in Hamming distance d_H. Pairs with larger d_H can have LARGER G_phys through sign cancellation. The correct bound depends on the maximum G_phys across ALL cross-coset pairs:

$$G_{\log}[0,1] \leq \max_{a \in C_0, b \in C_1} G_{\text{phys}}[a,b]$$

This maximum is code-dependent and sensitive to:
1. The embedding of the CSS code onto the vertex-sharing chain
2. Whether the code admits total-complement pairs ((a, a^c) with a in C0, a^c in C1)
3. The bit patterns (spin signs) of codewords in the superposition

**The irreducible error floor remains, but its magnitude depends on the specific code structure, not just the distance d.**

### Numerical Verification (Steane [[7,1,3]], c=0.5)

| Quantity | Value | Notes |
|----------|-------|-------|
| G_log[0,1] | 0.0423 | Mean over all cross-coset pairs |
| G_phys[max] | 1.0000 | From d_H=7 total-complement pairs |
| cos^2(2c)^{2d} (naive bound) | 0.00062 | VIOLATED: G_log >> this |
| P_L (logical error) | 0.479 | Near-maximal dephasing |
| Dominant pairs | d_H=3 (87.5%) | Controlled by minimum-distance pairs |
| Coherence-preserving pairs | d_H=7 (12.5%) | Sign-cancellation loophole |

---

## 1. Physical Setup (Recap from spectral_decoherence_theory.md)

### 1.1 Vertex-Sharing Causal Ring Chain

We have b1 causal rings. Ring r connects qubits Q_r -> E_r -> Q_{r+1} -> E'_r -> Q_r in a 4-cycle. All edges carry Cartan parameter c. After tracing out environment qubits:

$$\Phi(|a\rangle\langle b|) = G_{\text{phys}}[a,b] \cdot |a\rangle\langle b|$$

with computational basis states labeled by s in {+1, -1}^{b1+1}:

$$G_{\text{phys}}[a,b] = \prod_{r=0}^{b_1-1} \cos^2(c \cdot \Delta_r(a,b))$$

where Delta_r(a,b) = (s_r^a + s_{r+1}^a) - (s_r^b + s_{r+1}^b) in {-4, -2, 0, 2, 4}.

### 1.2 Key Properties

1. Diagonal: G_phys[a,a] = 1
2. Nonnegative: G_phys[a,b] in [0,1] for p=0.5
3. Product structure: Each ring contributes cos^2(c . Delta_r)
4. Delta distribution per ring:
   - Delta = 0: cos^2(0) = 1 (no decay) -- either neither qubit differs, or both differ with opposite sign change
   - |Delta| = 2: cos^2(2c) (one qubit differs, or both differ in ways that partially cancel)
   - |Delta| = 4: cos^2(4c) (both qubits differ, same sign direction in s-space)

### 1.3 Critical Anti-Monotonicity

**G_phys is NOT monotonic in the Hamming distance d_H(a,b).** Counterexample:

- Pair with d_H = 3 (isolated differences): 2 or more rings see |Delta| = 2, G_phys = cos^2(2c)^N where N >= 2
- Pair with d_H = n (total complement, perfect sign alternation): ALL rings see Delta = 0, G_phys = 1

The mechanism: for total-complement pairs (s_b = -s_a), we have Delta_r = 2(s_r^a + s_{r+1}^a). If the reference state a has alternating spins (s_r != s_{r+1} for all r), then Delta_r = 0 for ALL rings, and G_phys = 1.

This anti-monotonicity is THE central obstacle to a simple d-based bound.

---

## 2. Phase 1: Precise Formulation

### 2.1 CSS Stabilizer Codes

Consider a [[n, k=1, d]] CSS code with C_X = C_Z = C (a classical linear code). The stabilizer group is:

S = < X(w) : w in C^\perp, Z(w) : w in C^\perp >

The X-stabilizers are X(w) for w in C^\perp, and Z-stabilizers similarly.

The logical basis states are labeled by cosets of C^\perp in C:

$$|j_L\rangle = \frac{1}{\sqrt{|C^\perp|}} \sum_{w \in C^\perp} |w \oplus v_j\rangle$$

where v_0, v_1 in C are distinct coset representatives (v_1 - v_0 not in C^\perp).
k = dim(C) - dim(C^\perp) = 1 for Steane code.

Define codeword sets:
- C0 = {w XOR v_0 : w in C^\perp} -- support of |0_L>
- C1 = {w XOR v_1 : w in C^\perp} -- support of |1_L>
- |C0| = |C1| = |C^\perp| = 2^{n-k} for k=1

Cross-coset pairs (a in C0, b in C1):
- Minimum Hamming distance >= d
- Maximum possible distance = n (total complement, if structurally admitted)

### 2.2 Logical Gram Entry

The logical channel after applying rings:

$$\Phi(|\tilde{0}_L\rangle\langle \tilde{1}_L|) = \frac{1}{|C^\perp|} \sum_{a \in C_0} \sum_{b \in C_1} G_{\text{phys}}[a,b] \cdot |a\rangle\langle b|$$

The logical Gram entry:

$$G_{\log}[0,1] = \langle 0_L| \Phi(|\tilde{0}_L\rangle\langle \tilde{1}_L|) |1_L\rangle = \frac{1}{|C_0| \cdot |C_1|} \sum_{a \in C_0} \sum_{b \in C_1} G_{\text{phys}}[a,b]$$

This is the arithmetic mean of G_phys over all cross-coset pairs.

### 2.3 Corrected Bounding Strategy

Since G_phys in [0,1]:

$$G_{\text{phys}}[\min] \leq G_{\log}[0,1] \leq G_{\text{phys}}[\max]$$

where G_phys[max] = max_{a in C0, b in C1} G_phys[a,b] and similarly for min.

The upper bound on G_log (lower bound on P_L) uses G_phys[MAX]:

$$P_L = \frac{1 - G_{\log}[0,1]}{2} \geq \frac{1 - G_{\text{phys}}[\max]}{2}$$

But G_phys[max] is NOT simply cos^2(2c)^{2d}. It depends on whether the code admits "coherence-preserving" pairs.

### 2.4 Characterizing G_phys for a Given Pair

For a pair (a,b) with spin representations s^a, s^b in {+1,-1}^n:

**Ring activation classification** (for each ring r connecting qubits r, r+1):

| Condition | Delta_r | Contribution to G_phys |
|-----------|---------|----------------------|
| Neither qubit differs: s_r^a = s_r^b AND s_{r+1}^a = s_{r+1}^b | 0 | 1 |
| One qubit differs | +/-2 | cos^2(2c) |
| Both differ, SAME sign change: s_r^a=-s_r^b and s_{r+1}^a=-s_{r+1}^b and s_r^a s_{r+1}^a = s_r^b s_{r+1}^b | +/-4 | cos^2(4c) |
| Both differ, OPPOSITE sign change: s_r^a=-s_r^b and s_{r+1}^a=-s_{r+1}^b and s_r^a s_{r+1}^a = -s_r^b s_{r+1}^b | 0 | 1 |
| Total complement (s^b = -s^a): Delta_r = 2(s_r^a + s_{r+1}^a) | 0 if s_r^a != s_{r+1}^a, else +/-4 | 1 or cos^2(4c) |

### 2.5 Three Pair Classes

**Class I: Isolated differences (non-adjacent differing qubits)**
- Each differing qubit activates 2 boundary rings with |Delta|=2
- No sign-cancellation possible (adjacent qubits are SAME in spin for both a and b)
- G_phys = cos^2(2c)^{2w} where w = number of differing qubits (if all differences isolated)

**Class II: Clustered differences (adjacent differing qubits)**
- Internal edges of clusters can have Delta=0 via opposite sign change
- Only boundary edges contribute |Delta|=2
- G_phys = cos^2(2c)^{2 . N_clusters} where N_clusters = number of connected components of differing positions
- Best case: single cluster of size w => only 1 or 2 active rings (depending on chain boundary)

**Class III: Total complement (s^b = -s^a everywhere)**
- Delta_r = 2(s_r^a + s_{r+1}^a) for each ring
- If s^a has PERFECT alternation: s_r != s_{r+1} for all r => ALL Delta_r = 0 => G_phys = 1
- If s^a has alternating blocks: some rings see |Delta|=4 => G_phys = cos^2(4c)^k
- Worst (most coherent) case: alternating s^a => G_phys = 1, zero Gram decay

**This Class III pair is the "loophole" — if the code admits it, the bound is independent of d.**

### 2.6 Assumptions (Corrected)

1. Cartan-aligned axes: n_hat = z_hat for all rings (computational basis diagonalization)
2. Product environment initial state: p=0.5 (G_phys is real, nonnegative)
3. Vertex-sharing chain topology: b1 rings connect b1+1 physical qubits
4. CSS stabilizer code with X-distance d
5. **NEW:** The code is considered "generic" if it does NOT admit total-complement cross-coset pairs with alternation. For such codes, the minimum-distance bound applies.
6. For codes WITH total-complement loophole: the bound is given by the MOST coherent admissible pair.

---

## 3. Phase 2: Derivation (Corrected)

### 3.1 Three-Regime Analysis

**Regime A: Generic CSS code (no total-complement loophole)**

If C0 and C1 contain NO pair (a, a^c) where a^c is the bitwise complement, or if ALL such pairs in the code have non-alternating spin patterns, then:

G_phys[max] is achieved by the minimum-distance pair with optimal sign arrangement. For a code where the minimum-weight cross-coset pair has isolated support:

$$G_{\text{phys}}[\max] = \cos^2(2c)^{2d}$$

$$P_L \geq \frac{1 - \cos^2(2c)^{2d}}{2}$$

**Regime B: Code with total-complement loophole**

If the code admits a total-complement pair (a in C0, a^c in C1) with alternating spin pattern:

$$G_{\text{phys}}[\max] = 1$$

$$P_L \geq 0$$

In this case, the lower bound on P_L is trivial (0). The logical error is controlled by the AVERAGE over pairs, not the max.

**Regime C: Code with clustered minimum-weight support**

If the minimum-weight cross-coset pair has clustered (adjacent) differing qubits:

$$G_{\text{phys}}[\max] = \cos^2(2c)^{2 \cdot N_{\text{clusters}}} \geq \cos^2(2c)^2$$

where N_clusters is the number of connected components of differing bits. This can be as low as 1 (for a single cluster at a chain boundary), giving G_phys[max] = cos^2(2c)^2.

### 3.2 Steane Code: Regime A with Class III contamination

The Steane [[7,1,3]] code falls in a MIXED regime:

- **d_H=3 pairs (87.5%):** Clustered support at chain boundary => 1-2 active rings => G_phys up to cos^2(2c)
- **d_H=7 pairs (12.5%):** Total-complement pairs, some with favorable alternation => G_phys up to 1.0
- **G_log = 0.0423** (at c=0.5): Dominated by d_H=3 pairs, with minor upward pull from d_H=7 pairs
- **G_phys[max] = 1.0**: From d_H=7 pairs (loophole present but low-weight)

The logical error P_L = 0.479 is near the maximum of 0.5, despite the loophole, because the loophole pairs are only 12.5% of the total.

### 3.3 Refined Bound Formula

For a CSS code with distance spectrum {n_w : w = d, d+1, ..., n} where n_w = number of cross-coset pairs at Hamming distance w:

$$G_{\log}[0,1] = \sum_{w} \frac{n_w}{|C_0||C_1|} \cdot \langle G_{\text{phys}} \rangle_{w}$$

where <G_phys>_w is the mean G_phys for distance-w pairs.

The upper bound (worst for QEC = best for coherence):

$$G_{\log}[0,1] \leq \max_{w} G_{\text{phys}}[\max]_w$$

where G_phys[max]_w = max_{d_H=w} G_phys[a,b].

**If no Class III loophole:** G_phys[max]_w is maximized at w = d (minimum distance), with:
- Isolated support: G_phys[max]_d = cos^2(2c)^{2d}
- Clustered support: G_phys[max]_d = cos^2(2c)^{2 . N_clusters}

**If Class III loophole exists:** G_phys[max]_n = 1 for some distance-n pairs.

### 3.4 The Logical Channel (Still Valid)

The logical channel remains a dephasing channel regardless:

$$\Phi_L(\rho_L) = (1 - \varepsilon)\rho_L + \varepsilon \cdot Z_L \rho_L Z_L$$

with epsilon = (1 - G_log[0,1])/2. The correctness of this channel form does NOT depend on the bound -- it follows from the diagonal structure of G_phys.

### 3.5 The QEC Blindness (Still Valid)

Syndrome extraction remains blind to Gram-decay-induced logical Z errors, because:
- Both |0_L> and |1_L> are +1 eigenstates of all stabilizers
- The dephased state Phi_L(rho_L) is in the code subspace
- Only logical measurements can detect the error

This conclusion is independent of the bound's tightness.

### 3.6 Tightness Table

| Code Feature | Bound G_log <= | Tight? | Why |
|-------------|----------------|--------|-----|
| Isolated min-weight, no total-complement | cos^2(2c)^{2d} | TIGHT for worst pair | Only boundary edges contribute |
| Clustered min-weight, no total-complement | cos^2(2c)^{2 . N_clusters} | LOOSE | Average includes broader pairs |
| Total-complement loophole present | 1.0 | TRIVIAL | Sign-cancellation loophole |
| Steane [[7,1,3]] (mixed) | 1.0 | TRIVIAL | d_H=7 pairs dominate max |

---

## 4. Phase 3: Syndrome Extraction Frequency (Corrected Sketch)

The syndrome extraction analysis carries through with the corrected bound:

Between syndrome extractions, M rounds of non-Clifford gates accumulate Gram decay. For a code WITHOUT the total-complement loophole:

$$P_L^{(M)} \geq \frac{1 - \cos^2(2c)^{2dM}}{2}$$

and for target error epsilon: M <= epsilon / (d . |ln cos^2(2c)|).

For a code WITH the total-complement loophole:
- The bound softens to P_L >= 0 (trivial)
- But the average G_log still decays because loophole pairs are typically a small fraction
- The effective error rate depends on the FRACTION of loophole pairs

**Design implication:** To maximize protection, codes should:
1. Avoid total-complement cross-coset pairs (if possible)
2. Use qubit permutations to ensure isolated minimum-weight support
3. Minimize the fraction of "coherence-preserving" pairs

**But:** Even under optimal design, if ANY cross-coset pair has G_phys close to 1, the LOWER BOUND on P_L approaches 0, though the ACTUAL average G_log may still produce significant decay.

---

## 5. Corrected Theorem Statement

### Gram-to-QEC Bridge Theorem (v2, Corrected)

For a CSS stabilizer code [[n, k, d]] embedded in a vertex-sharing chain of causal rings (Cartan c, p=0.5):

1. **Channel structure:** The logical channel is a dephasing channel in the computational basis, with epsilon = (1 - G_log[0,1])/2.

2. **Upper bound (worst pair):** G_log[0,1] <= max_{a in C0, b in C1} G_phys[a,b].

3. **If the code has NO total-complement cross-coset pairs AND minimum-weight pairs have isolated support:** max G_phys = cos^2(2c)^{2d}. This gives the strongest bound.

4. **If the code admits total-complement pairs with alternating spin pattern:** max G_phys = 1. The bound is trivial; actual G_log depends on the FRACTION of such pairs.

5. **QEC blindness:** Syndrome extraction cannot detect Gram-decay logical Z errors, regardless of distance or code structure. The ONLY defenses are:
   a. Operate at Clifford points (c = pi/2): mu = 0, no decay
   b. Operate at extremely weak coupling (c -> 0): mu -> 0
   c. Choose code embeddings that exclude total-complement loophole pairs
   d. Minimize the fraction of low-ring-activation pairs in the code structure

6. **Counter-intuitive d-dependence (isolated support):** When minimum-weight pairs have isolated support, larger d INCREASES Gram decay (opposite of QEC benefit). Optimal d balances stochastic error protection (improves with d) against Gram decay (worsens with d).

### Key Numerical Reference (Steane [[7,1,3]], c=0.5)

| Quantity | Formula | Value |
|----------|---------|-------|
| cos^2(2c) | Per-ring |Delta|=2 factor | 0.291927 |
| G_phys[max over d_H=3] | cos^2(2c) (clustered at boundary) | 0.291927 |
| G_phys[max over d_H=7] | 1.0 (sign-cancellation) | 1.000000 |
| G_log[0,1] | Mean over 64 cross-coset pairs | 0.042307 |
| P_L | (1 - G_log)/2 | 0.478847 |
| G_bound (naive, cos^2(2c)^6) | Would-be bound | 0.000619 |
| Ratio G_log / G_bound | | 68.4x (bound vastly violated) |

---

## 6. Honest Limitations

### 6.1 Anti-Monotonicity (G_phys not monotonic in d_H)

This is the critical correction. The bound G_log <= cos^2(2c)^{2d} is FALSE because:
- Total-complement pairs can have G_phys = 1 (zero ring activation)
- Clustered differences activate fewer rings than isolated differences
- Sign patterns affect ring activation independent of Hamming distance

### 6.2 Code Dependency

The bound depends on the SPECIFIC code structure, not just parameters (n, k, d). The distance spectrum AND the spin-sign patterns both matter. A "good" code for Gram decay protection is characterized by:
- No Class III loophole pairs
- Isolated minimum-weight support
- Small fraction of low-ring-activation pairs

### 6.3 G_log is Still Controlled

Despite the loophole, G_log for the Steane code at c=0.5 is 0.042 (not 1.0), because:
- Loophole pairs constitute only 12.5% of cross-coset pairs
- The dominant pairs (d_H=3, 87.5%) have G_phys ~ 0.027-0.29
- The average is pulled down by the dominant low-weight pairs

### 6.4 General Code Question

Open question: Does EVERY CSS code with k=1 necessarily admit total-complement loophole pairs? Conjecture: Yes, if the all-ones vector is in C but not in C^\perp, which is generic for many CSS codes. If so, the bound G_log <= 1 is universal and trivial.

### 6.5 Missing Factors (unchanged)

Same as before: CFOL constraints, ghost zeros, non-product initial states, non-CSS codes, Gamma_0, inter-ring communication.

---

## 7. Summary

### Key Formulas

| Quantity | Expression | Notes |
|----------|-----------|-------|
| G_phys[a,b] | prod_r cos^2(c.Delta_r) | Per-ring product |
| G_log[0,1] | mean_{C0 x C1} G_phys[a,b] | Average over cross-coset |
| G_log bound | <= max_{C0 x C1} G_phys[a,b] | Tightest possible upper bound |
| Isolated d-bound | <= cos^2(2c)^{2d} | Valid only for Class I pairs |
| Clustered d-bound | <= cos^2(2c)^{2.N_clusters} | Class II pairs |
| Loophole bound | <= 1 | Class III pairs (trivial) |
| P_L | (1 - G_log[0,1])/2 | Logical Z error probability |
| Channel | (1-eps)rho + eps.Z.rho.Z | Dephasing in logical basis |

### What Survives the Correction

1. **The logical channel IS a dephasing channel** -- this is robust
2. **QEC blindness to Gram decay** -- syndrome extraction sees nothing
3. **Gram decay produces irreducible error floor** -- but magnitude is code-dependent
4. **The tension between d and Gram decay** -- persists for isolated-support codes

### What Changed

1. **G_phys is not monotonic in d_H** -- the original "additive bound" was false
2. **The bound `cos^2(2c)^{2d}` is a SPECIAL CASE** (Class I only)
3. **Most CSS codes likely have the total-complement loophole** -- making the absolute bound trivial (G_log <= 1)
4. **The effective P_L depends on the FRACTION of favorable pairs, not just d**

---

*This document completes SOP Phase 1+2 (corrected) for the Gram-QEC bridge. The numerical verification (verify_qec_bound.py) confirms the anti-monotonicity and loophole effects for the Steane code. A general code characterization of the loophole remains open.*
