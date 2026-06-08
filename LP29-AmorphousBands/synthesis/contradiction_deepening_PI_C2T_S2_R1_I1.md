# Contradiction deepening: LP29-C2T-S2-R1-I1

Date: 2026-06-05

## Surface Contradiction

- A: A protocol-ready schema/oracle can be a sufficient closeout artifact for `O_s` baseline admission.
- B: An admission gate is not real until executable fixtures return the expected terminal statuses.

## Five Whys

1. Why is a schema/oracle insufficient as an admission gate?  
   Because a schema can describe valid states without proving that any implementation preserves those states under malformed, incomplete, legacy, or adversarial inputs.

2. Why do malformed, incomplete, legacy, and adversarial inputs matter here?  
   Because the central risk is silent upgrade: context, DOI, scalar closeness, executor narrative, or legacy `PARTIAL_CONTEXT_ONLY` may be promoted into exact admission unless a validator makes the failure terminal and observable.

3. Why is silent upgrade more dangerous than ordinary implementation drift?  
   Because it would collapse the distinction between reported context, candidate replay, diagnosed mismatch, and admitted exact. That collapse would make later graph-vs-overlap or material claims appear stronger than the evidence permits.

4. Why does this become a foundational contradiction rather than a coding detail?  
   Because the same scientific object, `O_s`, has two incompatible meanings unless the admission mode is fixed: a provenance-conditioned reported value versus an exact replay/admission observable. These cannot be treated as the same evidence class.

5. Why is the deepest unresolved layer still open?  
   Because the project has not yet executed the deterministic map from payload evidence to terminal status. Until execution exists, the contract is a firewall specification, not a firewall.

## Deep Contradiction

The deep contradiction is:

> Evidence semantics cannot be both narrative-flexible and exact-admission-safe. Either `O_s` admission is a deterministic, executable state transition over proof-carrying evidence, or it remains a prose judgment that can silently promote weaker evidence into exact admission.

## Consequence

The next north star must directly instantiate the state transition:

`LP29-C2T-S2-R1-I1-X1 / executed O_s baseline-admission regression firewall`

Its minimal success condition is not a stronger essay. It is a runnable validator plus fixtures/tests whose actual outputs preserve:

- current Srivastava exact `O_s` summary evidence -> `BLOCK`
- explicit reported-context F01-F03 evidence -> `CONDITIONAL_CONTEXT_PASS`
- legacy `PARTIAL_CONTEXT_ONLY` -> `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY`
- exact admission only with complete F01-F22 and matching predeclared comparison
