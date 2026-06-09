# R2 Review Report

## Verdict: Major Revision (FATAL=0, MAJOR=4)

## R1 FATAL Status (all resolved)
- F1 (standard decoherence claim): RESOLVED — honest statement re state preparation
- F2 (NM conflation): RESOLVED — reframed as toggle-event backflow, Budini disclaimer
- F3 (determined/undetermined): RESOLVED — standard QM population language
- F4 (missing Budini): RESOLVED — cited in abstract, intro, prior work, discussion

## R1 MAJOR Status
- M1 (collision model): PARTIALLY RESOLVED — formula added but no numerical values
- M2 (T1 correction): RESOLVED — full expression with time-dependent derivation
- M3 (MSV complementarity): RESOLVED — honest qualification
- M4 (L physical origin): RESOLVED — energy gap + Jaynes-Cummings sketch
- M5 (ensemble vs single-run): RESOLVED — explicit floor/ceil + binomial estimate

## New MAJOR Issues (R2→R3 targets)
- NEW-M1: $C_F$ normalization physically unmotivated (dividing by capacity not forward transfer)
- NEW-M2: $N_{\rm back}$ measurement not in main text (only in SM)
- NEW-M3: Expectation bound vs deterministic bound unclear
- M1-STILL: Collision model needs numerical values

## Fix Strategy
1. Add collision model numerical results (Monte Carlo simulation) → closes M1
2. Rewrite $\mathcal{R}$ definition justification: frame capacity as worst-case normalization
3. Add $N_{\rm back}$ measurement paragraph to main text (mid-circuit + ancilla options)
4. Clarify: bound is deterministic conditional on measured initial $n_0$, expectation bound on $q_S$
5. Address MINOR issues (T1 concurrent, pointer basis identification)
