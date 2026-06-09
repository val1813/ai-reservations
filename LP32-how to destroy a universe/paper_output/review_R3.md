# R3 Review Report

## Verdict: Accept with Minor Revision (FATAL=0, MAJOR=0, MINOR=7)

## R2 MAJOR Status (all resolved)
- NEW-M1 (C_F normalization): RESOLVED
- NEW-M2 (N_back measurement): RESOLVED (residual weakness noted)
- NEW-M3 (expectation vs deterministic): RESOLVED (conflation sentence flagged)
- M1-STILL (collision computation): RESOLVED

## MINOR Fixes Applied (7/7)
1. N_back measurement: "subset" → "all S-qubits measured after each step" (deterministic count)
2. Conflation sentence: "either interpretation... N_back ≤ N_S q_S" → rephrased with separate deterministic/ensemble bounds
3. Finite-size effects: N_S=3 caveat added — binomial fluctuations noted, deterministic interpretation robust
4. Title-content: Not changed (title is defensible — "finite information capacity" = one-bit-per-qubit condition)
5. Ancilla measurement: Added "platform-specific; SM provides parameters"
6. Collision model citation: Added Ciccarello, Palma, Giovannetti PRA 87, 040103(R) (2013)
7. T1 concurrent: Added sequential-is-conservative statement + tau_prot ≪ T1 justification
