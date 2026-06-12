# R1 Fix Plan

## FATAL Fixes (priority order)

### F1: ⛔ IBM Q Hardware Results — integrate into main text
- **Fix:** Update "Experimental Tests" section to include actual ibm_kingston results
- **Change:** "Three experimentally testable predictions" → "Two predictions confirmed by measurement + one data re-analysis"
- **Add:** Table of v3/v4 measurement results with S/N values
- **Impact:** Huge strengthening of paper

### F2: ⛔ SM Tables — complete empty tables
- **Fix:** Fill Table S1 with actual Kraus operator data, complete Table S2
- **Impact:** SM submission-compliant

### F3: ⛔ CJ Bridge derivation — add to SM
- **Fix:** Add §S6 Choi-Jamiołkowski bridge derivation
- **Impact:** SM cross-reference complete

### F4: ⛔ Cover Letter — acknowledge limitations
- **Fix:** Add limitations paragraph (qubits only, product state assumption)

## MAJOR Fixes

### M1: Lemma S1 — provide explicit eigenvalue proof
### M2: Add quantum causal models references (Barrett 2021, Vilasini-Colbeck 2022)
### M3: Verify numerical factors (149 vs 153)
### M4: Add correlated-environment discussion to Discussion
### M5: Add code repository link

## Execution
Files to modify: main.tex, supplemental.tex, cover_letter.tex
