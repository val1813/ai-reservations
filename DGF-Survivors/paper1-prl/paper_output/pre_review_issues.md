# Pre-Review Issues Identified

## FATAL-level Issues

### F1: IBM Q Hardware Results Exist But Not in Paper
- **Evidence:** 19-ibmq-hardware-results.md documents actual measurements on ibm_kingston (Heron r2)
  - Run v3: S/N = 285 (π/4), 617 (π/8), 198 (π/16)
  - Run v4: S/N = 284 (π/4), 194 (π/8), 670 (π/16)
  - All far above 5σ threshold
- **Paper states:** "Three experimentally testable predictions" — implies NOT YET DONE
- **Impact:** Either (a) paper is obsolete because experiments already done, or (b) paper needs to include the results
- **Recommendation:** Update Experimental Tests section to include actual hardware results as confirmation

### F2: SM Tables Are Empty
- Table S1 caption says "(See accompanying data file.)" — no actual data
- Table S2 has content but table environment is incomplete (no \end{table})
- **Impact:** SM is incomplete, would fail PRL submission check

### F3: SM Mentions Hardware Results Not in Main Text
- SM Error Budget: "The differential noise floor σ_Δ ≈ 0.015 bits"
- SM references IBM Q error rates but main text says "estimated signal-to-noise"
- **Impact:** Three-material inconsistency (main/SM/CoverLetter)

## MAJOR-level Issues

### M1: Abstract Too Long
- Current: ~127 words | PRL limit: 120 words
- Needs trimming

### M2: Low Reference Count
- Currently 11 references | PRL typical: 20-30
- Missing: recent PRL quantum info papers, experimental non-Markovianity papers

### M3: Section Headers May Conflict With PRL Style
- PRL doesn't use numbered section headers
- Current uses `\section{}` — revtex4-2 PRL style handles this but should verify

### M4: Paper States Predictions But Has Actual Data
- The IBM Q results show QCMI is measurable at S/N >> 5
- Paper should update from "predictions" to "measurements" or clearly explain

## MINOR-level Issues

### m1: Cover Letter mentions "factor of 153" without full context
### m2: Reference [4] Gangwar 2025 and [5] Buscemi 2025 need fetch verification
### m3: Reference [10] Ferradini arXiv:2502.04168 — verify content matches paper's characterization
