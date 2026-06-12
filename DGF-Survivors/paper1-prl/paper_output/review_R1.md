# R1 Review Report — PRL Submission
## "Causal Topology Enforces Quantum Non-Markovianity"

**Reviewer Stance:** PRL anonymous reviewer, fundamentally skeptical
**Date:** 2026-06-09
**Verdict:** ⛔ MAJOR REVISION (not reject — the core result is strong)

---

## SECTION A: Manuscript Review

### A1. Core Claim (one sentence)
A single causal cycle in the system-environment interaction graph forces nonzero QCMI iff any edge rotation angle ∉ (π/2)ℤ, and the correct scaling is θ² ln(1/θ), not θ⁴.

### A2. Mathematical Correctness

**✅ Theorem proof:** The CFOL proof is structurally sound. The Gram matrix argument is clean and the convex-combination-on-unit-circle trick is correct. The sufficiency direction is trivial — if all c_j ∈ (π/2)ℤ, the phases collapse to ±1 factors and rank(G)=1.

**⚠️ Hidden assumption:** The proof assumes the environment is a product state |γ⟩^⊗|E|. This is stated but its role is underappreciated. If environment qubits are correlated, the factorization of the Gram matrix no longer holds, and the theorem may fail. The paper should explicitly state this assumption's scope.

**⚠️ Edge case p→0 or p→1:** At p=0 or p=1, the environment is in a pure eigenstate of σ_n̂. The "convex combination" argument then collapses to a single term (weight 1). The theorem states p ∈ (0,1) which excludes these limits — this is correct but the physical meaning is that "partial information in the environment" is essential. Should be explained.

**✅ QCMI identity:** I(R;E'|Q') = S(ρ_RQ') follows correctly from S(E'Q') = S(Q') = log₂(d_S). Lemma S1 is correct.

**⚠️ Small-θ expansion:** QCMI(θ) = (4θ²/ln 2)[1 + ln(1/4θ²)] + O(θ⁴|log θ|). The log singularity is genuine — it comes from −x ln x behavior near pure states. However, the coefficient "4" needs verification. The paper claims "factor of 4 enhancement relative to naive nearest-neighbor expansion" — this factor depends on the ring structure and should be derived more explicitly in SM.

### A3. Physical Claims Audit

**⚠️ "Standard theory predicts identical behavior for systems with different causal topology":**
This is the paper's central rhetorical claim. But it overstates the case. The standard theory of open quantum systems doesn't "predict identical behavior" — it simply doesn't have the vocabulary to distinguish these cases. The distinction is between "standard theory can't tell the difference" (true) and "standard theory predicts they're the same" (misleading). Recommend rephrasing.

**⚠️ Factor of 153 discrepancy:**
At θ = π/16: θ⁴ prediction = 0.004 bits, computed = 0.597 bits. Ratio = 149.25, not 153. The paper rounds to 153 but 149 is more accurate. Minor but precision matters. Also, the "factor of 19.6" at θ = π/8: 1.224/0.063 = 19.43, not 19.6. Check all reported factors.

**✅ "Causal topology is an independent control parameter":**
This is genuinely new. The paper correctly identifies that coupling strength and spectral density don't capture graph topology. The claim is well-supported by the theorem.

### A4. Literature Positioning

**⚠️ Reference [10] (Ferradini et al. arXiv:2502.04168):**
The paper says this "addresses a different question — causal discovery in the presence of cycles." This characterization needs verification. Ferradini et al. developed a framework for cyclic quantum causal models that may overlap more than claimed. At minimum, the differences should be spelled out more precisely.

**⚠️ Missing literature:**
- Vilasini, Colbeck, "General framework for cyclic causal models" (2022) — foundational work on quantum causal structures
- Barrett, Lorenz, Oreshkov, "Cyclic quantum causal models" (2021, Nat. Commun.)
- Costa, Shrapnel, "Quantum causal modelling" (2016, New J. Phys.)

The paper's novelty claim depends on precise positioning against this body of work on quantum causal models.

**✅ Reference to Breuer-Laine-Piilo (2009):** Correct. This is the standard BLP non-Markovianity measure.

**⚠️ References [4,5] (Gangwar 2025, Buscemi 2025):** Very recent (2025). Need fetch-verification. Are these published or preprints?

### A5. Experimental Testability — ⛔ FATAL: MAJOR INCONSISTENCY

**This is the most serious issue with the current manuscript.**

The paper presents three experimental protocols as **predictions** — things that can be tested on existing hardware. The language throughout is future-oriented: "it is now possible to test," "await testing," "estimated signal-to-noise ratios."

**However**, supporting materials (19-ibmq-hardware-results.md) document actual IBM Q measurements that have ALREADY BEEN PERFORMED:
- ibm_kingston (Heron r2)
- Run v3: S/N = 285 (π/4), 617 (π/8), 198 (π/16)
- Run v4: S/N = 284 (π/4), 194 (π/8), 670 (π/16)
- All measurements used 50k-100k shots per circuit
- Actual S/N is 10-62x BETTER than conservative predictions

**The paper has two choices, and it must pick one:**
1. Include the hardware results as experimental confirmation — this STRENGTHENS the paper enormously
2. Remove all mention of actual measurements from SM and present only predictions — but this is dishonest if measurements exist

**Current state is inconsistent:** main text says "predictions," SM implies measurements exist. This is unacceptable for PRL submission.

**Verdict on this point: FATAL.** Must be resolved before resubmission.

---

## SECTION B: Supplemental Material Review

### B1. Cross-reference Completeness
- Main text: "The full proof...appears in the Supplemental Material" → SM §S1 exists ✅
- Main text: "circuits are specified in the Supplemental Material" → SM §S5 exists ✅
- Main text: "the Choi-Jamiołkowski bridge mapping...is derived in the Supplemental Material" → ⚠️ Not found in SM. The SM §S5 mentions CJ bridge only in passing. Missing derivation.

### B2. SM Self-Consistency
- **⚠️ FATAL: Table S1 is empty.** Caption says "(See accompanying data file.)" — no data presented.
- **⚠️ Table S2 is incomplete.** Table environment lacks proper closure.
- SM §S2 Gram Matrix Factorization: Eq notation uses σ_n̂ eigenbasis but doesn't define the computational basis mapping explicitly enough for reproduction.

### B3. Numerical Verification
- 83,521-point grid scan: sampling c_j ∈ {0, π/16, ..., π} for all 4 edges = 17^4 = 83,521. Correct.
- 81 zero-QCMI configurations found = 3^4 (c_j ∈ {0, π/2, π} ∩ [0,π] = 3 values). Correct.
- Minimum non-zero QCMI: 7.7×10⁻⁵ bits — need to verify this is above numerical noise floor.
- p-independence: 180 tests across 30 configs, all <10⁻⁹ bits. Convincing.

### B4. Code Reproducibility
- `cat2_task5_precision_small_c.py` referenced but not provided in submission
- `cfol_scan.py` referenced but not provided
- **⚠️ Code should be archived (Zenodo/Figshare) and linked in SM**

### B5. SM-Main Text Inconsistency
- **SM mentions "IBM Q Kingston Heron r2" and S/N=617×** but main text presents as predictions → ⛔ FATAL inconsistency

---

## SECTION C: Cover Letter Review

### C1. Claim-Accuracy Check
- "θ² ln(1/θ), not θ⁴" → Matches main text ✅
- "factor of 19.6 at θ = π/8 and 153 at θ = π/16" → Numbers need verification as noted in A3 ⚠️
- "Two independent experiments and one ratio-based re-analysis, all testable on unmodified IBM Q hardware with estimated S/N from 29 to over 50" → These are estimated, not measured. But hardware results exist. ⚠️
- "Complete circuit specifications in the Supplemental Material" → Partially true but CJ bridge missing ⚠️

### C2. Limitation Acknowledgment
- Cover letter does NOT mention that the theorem is proved only for qubits (d=2)
- Cover letter does NOT mention that π/32 measurement falls below noise floor
- **⚠️ Cover letter should honestly state key limitations**

### C3. Forbidden Language
- No "We hope" or "We are confident" found ✅
- No "原则上可能" / "in principle" found ✅

---

## SECTION D: Five Rejection Reasons

### 1. Core Assumption's Simplest Counterexample [FATAL]
The proof critically depends on the environment being initialized as a product state |γ⟩^⊗|E|. For any correlated environment — e.g., two environment qubits prepared in a Bell state — the Gram matrix no longer factorizes, and the QCMI-zero condition may change. Can the authors construct a correlated-environment example where c_j ∉ (π/2)ℤ yet QCMI = 0? If such counterexamples exist, the theorem's scope is narrower than claimed.
**What the author needs to prove:** That the product-state assumption is physically motivated (not just mathematically convenient) and that correlated environments either (a) don't change the condition, or (b) are not physically relevant for the experimental protocols proposed.

### 2. Weakest Link in Derivation Chain [MAJOR]
The reduction QCMI = S(ρ_RQ') depends on S(E'Q') = S(Q') = log₂(d_S). The proof sketch in Lemma S1 states "the block structure of ρ_E'Q' yields d_S equal eigenvalues 1/d_S." But the block structure depends on ⟨φ(a)|φ(b)⟩ being the Gram matrix entries — these aren't orthogonal in general. The claim that eigenvalues are exactly 1/d_S needs a more rigorous justification. A counterexample would be: if G is not the identity, can ρ_E'Q' still have spectrum {1/d_S, ..., 1/d_S}?
**What the author needs to prove:** Explicit eigenvalue decomposition of ρ_E'Q' showing the d_S × d_S block structure yields exactly d_S eigenvalues of 1/d_S, regardless of G.

### 3. Conflict with Existing Literature [MAJOR]
The quantum causal models literature (Vilasini-Colbeck 2022, Barrett-Lorenz-Oreshkov 2021) has established frameworks for analyzing correlations in cyclic causal structures. The paper claims these address "causal discovery" rather than "forced non-Markovianity," but this distinction may be thinner than presented. Specifically, Vilasini and Colbeck's analysis of when cyclic causal structures produce non-classical correlations directly relates to the question of what correlations are forced by topology.
**What the author needs to prove:** A precise, technical distinction between their result and what can be derived from existing quantum causal model frameworks. Cite specific theorems from those papers and show why they don't imply the CFOL result.

### 4. Numerical Plausibility [MAJOR]
The paper claims QCMI = 1.000 bits at θ = π/4 and QCMI = 1.224 bits at θ = π/8. The QCMI is bounded above by 2 log₂ d_S = 2 bits (for d_S=2 system qubits). The value 1.224 bits at π/8 exceeds half the maximum — for a "small" angle. Is this physically plausible? The Gram matrix entries are cos²(2θΔ₁)cos²(2θΔ₂). At θ=π/8: cos²(π/4)=0.5. Off-diagonal entries G_{a,b} = 0.25 for the dominant (Δ₁=2, Δ₂=0) case. A 4×4 Gram matrix with diagonal 1 and strongest off-diagonal 0.25 — what entropy does this produce? My back-of-envelope: dominant eigenvalue ~1.75, others ~0.083, giving S ≈ 0.69 bits. The paper claims 1.224 bits. Please verify.
**What the author needs to prove:** Explicit numerical verification of the Gram matrix eigenvalue calculation for θ=π/8, showing the eigenvalue spectrum and entropy calculation step by step.

### 5. Closest Prior Work — Novelty Assessment [MAJOR]
The closest prior work is not Ferradini et al. but the foundational quantum causal models literature:
- Costa & Shrapnel (2016, New J. Phys. 18, 063032): "Quantum causal modelling" — first framework for quantum causal structures with cycles
- Barrett, Lorenz, Oreshkov (2021, Nat. Commun. 12, 885): "Cyclic quantum causal models" — proved that cyclic quantum causal structures can produce correlations impossible in acyclic structures

The paper's claim that "no one had asked whether the mere presence of a cycle forces QCMI to be nonzero" needs to be checked against Barrett et al., who proved that cycles enable classically impossible correlations. The QCMI result is more specific (exact iff condition + specific measure), but the general insight that cycles force non-classical behavior is not new.
**What the author needs to prove:** A side-by-side comparison table: Barrett et al. result vs CFOL result, showing the precise technical difference.

---

## SECTION E: Summary Verdict

### Verdict: MAJOR REVISION

### FATAL Issues (must fix before resubmission):
1. ⛔ IBM Q hardware results exist but paper presents as predictions → resolve inconsistency
2. ⛔ SM Table S1 empty, Table S2 incomplete → provide complete SM
3. ⛔ Missing CJ bridge derivation in SM (referenced in main text)
4. ⛔ Cover letter doesn't acknowledge key limitations

### MAJOR Issues (must address):
1. Correlated environment counterexample (Rejection Reason 1)
2. Precise positioning against quantum causal models literature
3. Numerical verification of θ=π/8 QCMI value
4. Gram matrix eigenvalue claim in Lemma S1

### Acceptable Aspects:
- The core CFOL theorem is mathematically sound and significant
- The θ² ln(1/θ) scaling correction is an important finding
- The connection between gate algebra (Pauli subgroup) and quantum memory is original
- Experimental testability is genuine and protocols are specified

### 致命一击:
> The Lemma S1 claim that ρ_E'Q' has exactly d_S eigenvalues equal to 1/d_S regardless of the Gram matrix G is the most vulnerable step. If G ≠ I (i.e., ⟨φ(a)|φ(b)⟩ ≠ 0 for some a≠b), the blocks in ρ_E'Q' are not diagonal, and the spectrum is not trivially {1/d_S}. The authors must provide a rigorous eigenvalue decomposition or the entire QCMI = S(ρ_RQ') reduction fails.

### 作者出路:
> Provide explicit matrix representation of ρ_E'Q' in the computational basis, compute its eigenvalues analytically for the general Gram matrix G, and prove that S(E'Q') = log₂(d_S) independently of G. If this cannot be proved for arbitrary G, restrict the claim to cases where G is rank-1 (QCMI=0) and adjust the scaling law derivation accordingly.
