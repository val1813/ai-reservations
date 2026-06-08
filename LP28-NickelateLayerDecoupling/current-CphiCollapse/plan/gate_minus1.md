# GATE -1: LP28-CphiCollapse

## Question

Does an independent input-side `C_phi` exist, or does every operational `C_phi` collapse to c-axis coherence / sample quality?

## Q-1.1: Proposition A Has Independent Support?

YES, but not as validation.

Support:

- LP28 AHA #S1-1 reframed `C_phi` as the observability bottleneck for a zero-leakage input-side variable.
- LP28-S1 A/B showed that `C_phi` can be operationalized before output reveal in at least two formal ways: normal-state Drude fraction and SVD observability score.
- If `C_phi` is real, it should produce pre-output discordant ordering relative to single-variable baselines.

## Q-1.2: Proposition B Has Independent Support?

YES.

Support:

- REVIEWER fatal issue: `C_phi_primary` is normal-state c-axis Drude/interlayer-coherence/sample-quality observable.
- Prior-art boundary: c-axis optical response, interlayer coherence, oxygen stoichiometry, and pressure history are already superconductivity-adjacent in nickelates.
- INSPECTOR/REVIEWER warnings show that baseline collapse is not cosmetic; it would kill theoretical content.

## Q-1.3: Are A And B Logically Incompatible?

YES.

If `C_phi` is independent, it must generate at least one input-side invariant, rank, or discriminator not reducible to c-axis coherence, disorder, dephasing, `dz2` weight, or sample quality.

If every measurable `C_phi` collapses to those baselines, then it is not a new variable and `I_phi` has no theoretical content beyond notation.

## Gate Result

PASS.

LP28-CphiCollapse is a valid new north star. It is sharper than LP28-S1 because it attacks the existence of the central variable, not the packaging of the protocol.

