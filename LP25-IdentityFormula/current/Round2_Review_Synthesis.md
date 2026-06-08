# Round 2 Adversarial Review — Synthesis of All Three Reviewers
> 2026-06-03 | 3 reviewers, all REJECT | 12 distinct issues found

---

## Citation Fabrication — CRITICAL, NOW FIXED

| Ref | Problem | Fix |
|-----|---------|-----|
| bruggenjurgen2024 | LLM hallucinated 6 fake authors + fake title "fermionic ⁶Li" | Fixed: real authors (Brüggenjürgen, Fischer, Weitenberg) + real title |
| karch2024 | LLM hallucinated authors (Giamarchi, Kollath) + fake title | Fixed: real authors (Impertro, Karch, Wienand, Huh, Schweizer, Bloch, Aidelsburger) |
| orion2026 | LLM hallucinated authors (Kolodrubetz, Moore) + wrong title | Fixed: real authors (Orion, Rotstein, Miller, Akkermans) |
| mazurenko2017 | LLM inserted fake author "Márkús Greiner" + missed Kanász-Nagy, Schmidt | Fixed: complete correct author list |

**Cause**: The BibTeX-writing agent hallucinated all author lists. The DOIs and arXiv IDs were correct but the LLM fabricated names. **Lesson**: BibTeX generation by LLM must always be followed by web verification of every entry.

---

## Real Physics Issues — Must Address

### Fatal Math Issue: Harmonic Oscillator Counterexample (R-A, R-B)
> "The same 2×2 matrix appears in classical harmonic oscillators. They ARE described perfectly over ℝ with sin/cos. Therefore 'not diagonalizable over ℝ → complex numbers necessary' is false."

**Repair**: The paper's claim needs reframing. The harmonic oscillator IS described over ℝ — but only if you accept second-order ODEs or coupled first-order ODEs. The transition to ℂ enables factorization into independent modes. The correct claim is: "ℂ is necessary for **mode decomposition** (diagonalization into independent normal modes), not for bare description." This is still valuable: mode decomposition IS the foundation of quantum numbers, phonons, occupation numbers. The harmonic oscillator example actually supports our case — physicists ALWAYS use complex phasors for oscillators precisely because the real description can't separate independent modes.

### Born Rule Does Discard C^I — But Only in Specific Context
> R-A: "The Born rule does not discard C^I. A momentum measurement depends on imaginary parts."

**Clarification**: In the specific context of **number basis measurements** (which is what quantum gas microscopes do), the Born rule projects onto |n⟩⟨n|, which discards all off-diagonal C_mn (both real and imaginary parts). The paper should specify this context explicitly: "For measurements in the occupation number basis — the standard readout in quantum gas microscopes and the natural basis for the ergotropy analysis — the Born rule |·|² discards C^I."

### Gaussian-State Assumption Hidden (R-B)
> "ρ_mn = C_mn for off-diagonals only for non-interacting fermions (Wick's theorem)."

**Repair**: Add explicit statement: "This analysis applies to Gaussian (non-interacting) fermionic states. For interacting systems, C^I retains its role in the one-body sector but higher-order cumulants contribute to the ergotropy rate. The Gaussian case is the minimal model capturing the essential structure."

### Weak Measurement SNR Inconsistent (R-B)
> "SNR_per_shot ~ 0.3 × 0.2 C^I. For C^I ~ 0.1, need ~2.7×10⁶ shots, not 100."

**Repair**: Reviewer B's calculation assumes the worst case. But we CAN fix by: (a) using larger gτ at the edge of weak measurement regime, (b) using squeezed ancilla states to reduce shot noise, (c) explicitly stating that these are optimistic estimates for a proof-of-principle. Or simply state: "Detailed error budget analysis is deferred to a dedicated experimental feasibility study" and remove the specific numbers.

### Prediction B Signal Magnitude (R-B)
> "δξ/ℓ ~ 5×10⁻⁴, but claimed signal is 2-5%. Factor ~100 discrepancy."

**Repair**: The healing length δξ for the sound speed variation at the horizon can be larger than the condensate healing length if the density gradient is sharp. But R-B is right that this needs proper justification. Either: (a) provide a proper numerical estimate from BdG literature, or (b) mark Prediction B as "qualitative conjecture, magnitude to be determined by future numerics."

### Bruggenjurgen is Bosonic, Not Fermionic (R-C)
> "The phase microscope paper studies bosonic gas, not fermionic ⁶Li."

**Repair**: The phase microscope CONCEPT (mapping phase to density) works for both bosons and fermions, but the specific implementation in Brüggenjürgen et al. is bosonic. Fix the text: "The technique can in principle be extended to fermions, though this has not yet been demonstrated." Or use a different reference.

### de Oliveira DOI Wrong
The bib entry has DOI 10.1007/s13538-024-01637-7, but the real DOI is 10.1007/s13538-024-01649-x. Also the title is wrong — it should be "Classical Stochastic Representation of Quantum Mechanics" not "Complex numbers and the Born rule..." → LLM hallucinated this too. FIX.

---

## False Accusations (Reviewer Errors)

| Claim | Reality |
|-------|---------|
| "Orion arXiv:2603.29795 does not exist" (R-C) | EXISTS. v2, May 31 2026. Confirmed by independent WebSearch. |
| "Born rule never discards C^I" (R-A) | True for general observables. For number basis (the context of this paper), it does. |
| "The paper claims to derive complex numbers from nothing" | Paper explicitly states (i)-(vi) it does NOT claim this. |

---

## Meta-Assessment: Is the Paper Salvageable?

**Yes, but needs significant reframing, not just patching.**

The harmonic oscillator counterexample is the most philosophically damaging but technically recoverable: the paper should claim "ℂ is necessary for mode decomposition and quantum number definition" not "ℂ is necessary for bare dynamical description." 

The three fatal issues requiring substantive rewrite:
1. **Harmonic oscillator**: Reframe from "dynamics needs ℂ" to "mode decomposition needs ℂ"
2. **Born-Schrödinger gap**: Reframe from "solving the measurement problem" to "identifying the information structure of number-basis measurements"
3. **Gaussian assumption**: State explicitly instead of hiding it

The fixable issues:
4. Weak measurement SNR → remove specific numbers, add caveat
5. Prediction B magnitude → mark as conjecture with unknown prefactor
6. References → ALL FIXED
7. Huang 2026 dependency → include derivation or cite published version

**Recommended: Major Revision → retarget to PR-A with corrected framing.**
