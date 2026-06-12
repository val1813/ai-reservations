# Writing Rationale Matrix

## Paper Structure Analysis (Current Draft)

### Abstract
- **Function**: Summarize theorem + scaling correction + experimental tests in ≤120 words
- **Service**: Q2 (Novelty) — clear distinction between prior work and contribution
- **Evidence**: CFOL theorem, θ² scaling, IBM Q test protocols
- **Issue**: Current abstract is ~130 words (over PRL limit); runs slightly long

### Introduction (Paragraphs 1-3)
- **P1**: "Blind spot" metaphor — causal topology missing from standard theory
  - Function: Hook. Establish broad significance
  - Serves: Q1 (Relevance) — non-specialist can understand why this matters
  - Evidence: Two systems with identical couplings/different topology

- **P2**: Status quo — perturbative treatment predicts θ⁴, anomalies observed
  - Function: Identify the gap precisely
  - Serves: Q2 (Novelty) — what prior work said vs what's actually happening
  - Evidence: References [1-5]

- **P3**: Main result preview — iff theorem + HJPW connection
  - Function: State the core result upfront
  - Serves: Q2/Q3 — what we proved and how it connects to known structure
  - Evidence: Theorem statement, HJPW analogue

### Causal Ring Model
- Function: Define the model precisely
- Serves: Q3 (Trust) — reproducible model definition
- Evidence: Mathematical definitions, Gram matrix derivation

### Theorem (CFOL)
- Function: Prove the main result
- Serves: Q3 (Trust) — complete proof sketch + numerical verification
- Evidence: Proof in SM, 83,521-point grid scan

### Physical Interpretation
- Function: Translate math to physics
- Serves: Q1 (Relevance) — what does this actually mean physically?
- Evidence: Interferometer analogy, Pauli subgroup connection

### Scaling Law
- Function: Correct the θ⁴ prediction
- Serves: Q2/Q3 — quantitative correction to published result
- Evidence: Small-θ expansion, numerical diagonalization, R² > 0.998

### Experimental Tests
- Function: Show testability on existing hardware
- Serves: Q3 (Trust) — each claim has a specific test
- Evidence: Three protocols with S/N estimates, error budgets in SM

### Discussion
- Function: Contextualize + acknowledge limits
- Serves: Q5 (Meaning) — honest boundaries
- Evidence: d>2 open question, qubit case is the relevant one

### Conclusion
- Function: Summarize and project forward
- Serves: All 5 questions converge here
- Evidence: Restatement of main results

## Issues Identified for Phase 2 Review

1. **Abstract too long** (~130 words vs 120 limit)
2. **No experimental data** — all predictions, no measurements (REVIEWER will flag)
3. **Single author + independent researcher** — may trigger credibility scrutiny
4. **Reference count low** (11 refs) for PRL — typical is 20-30
5. **Section naming**: PRL doesn't use numbered section headings — current draft has `\section{}` commands
6. **"Discrepancy factor of 153"** claim needs careful framing — stated as prediction not measurement
7. **SM mentions actual hardware experiments** (19-ibmq-hardware-results.md) but paper only has predictions — inconsistency
