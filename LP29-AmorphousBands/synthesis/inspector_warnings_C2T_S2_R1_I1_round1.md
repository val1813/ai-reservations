# Inspector warnings registry: LP29-C2T-S2-R1-I1 Round 1

Date: 2026-06-05

## A Inspector

Verdict: PASS WITH WARNING.

Warning:

- Clarify legacy `PARTIAL_CONTEXT_ONLY` compatibility semantics before coding. Choose either automatic conversion to `CONDITIONAL_CONTEXT_PASS` when F01-F03 pass, or strict `BLOCK` unless target mode is explicitly converted to `reported_context`.

## B Inspector

Verdict: PASS with one non-blocking synchronization warning.

Warning:

- JSON lists 12 adversarial cases while CSV lists 17. Next round should either mirror all CSV cases into JSON or declare the CSV as authoritative.

## PI Action

Carry both warnings into Round 2. No BLOCK prevents continuing.
