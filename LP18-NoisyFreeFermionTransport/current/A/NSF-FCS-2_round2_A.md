# NSF-FCS-2 Round 2 A Review

**Role:** A博士, academy / literature / standard-framework driven.

**Date:** 2026-06-03

**Scope constraint:** I reviewed the revised Round 2 package supplied by PI and did not use new Round 2 B outputs.

## 1. Strongest Retainable Revised Claim

The strongest defensible claim is not an asymptotic theorem and not an equilibrium FCS claim. It is:

> In the ledger's dimensionless Markov-affinity convention, equilibrium finite-volume FDT gives `lambda_T''(0)=2G_T`. For the long-jump open exclusion ledger under density-biased NESS, the finite-volume residual `R2=lambda_T''-2G_T` is robustly nonzero over the accessible small-`L` windows; raw `R2` scales quadratically in the density bias before `Qhat` normalization, survives centered and off-center reverse-bias checks, and produces a dimensionless normalized residual `Qhat=R2/(delta^2 G_T)` whose size increases over the tested windows, while its asymptotic functional form remains unresolved.

This is a current-mainline claim because Round 2 materially answered the reviewer attacks that would have made the signal circular or convention-dependent:

- FDT anchor is now convention-explicit: `lambda_T''`, `G_T`, and `R2` all have inverse-time units in the script convention.
- Raw `R2 ~ delta^2` is directly observed before dividing by `delta^2`.
- Off-center reverse-bias checks at `rho_bar=0.4` and `0.65` show no detectable odd-bias contamination.
- `reversible_side` is correctly demoted to an LDB sanity check; `nonLDB_site_skew` is separated as a distinct non-LDB perturbation.

## 2. Maximum Weakness Under Standard Frameworks

The maximum weakness is that the package is still finite-volume numerical evidence in a regime where standard hydrodynamic and large-deviation frameworks are strong. In particular, open exclusion processes are already a canonical testbed for nonequilibrium steady-state correlations, current fluctuations, and large deviations. Therefore, the revised package cannot claim conceptual novelty merely from observing `lambda_T'' != 2G_T` away from equilibrium.

The real unresolved point is whether the finite-window `R2` and `Qhat` behavior is a new long-jump transport signature or just the finite-size projection of known MFT / fluctuating-hydrodynamic structure. The current evidence supports a stable ledger phenomenon, not yet a derived universality class.

Technical weak points:

- `L=4..8` is too small to infer asymptotic scaling.
- `Qhat` growth is model-underdetermined; Round 2 itself finds log drift favored over power law by AIC.
- Density-bias NESS and non-LDB kinetic forcing must stay rhetorically separate.
- The result depends on the finite-state tilted-generator ledger convention; physical SI noise/conductance language would require restoring beta, charge, and time units.

## 3. Prior / Standard Framework Coverage Risk

Coverage risk is real but not currently fatal.

Relevant standard anchors from paper-search-mcp:

- Bertini, De Sole, Gabrielli, Jona-Lasinio, Landim, "Macroscopic fluctuation theory", Rev. Mod. Phys. 87, 593, DOI `10.1103/RevModPhys.87.593`.
- Derrida, Lebowitz, Speer, "Large Deviation of the Density Profile in the Steady State of the Open Symmetric Simple Exclusion Process", DOI `10.1023/A:1014555927320`.
- Landim, Milanes, Olla, "Stationary and Nonequilibrium Fluctuations in Boundary Driven Exclusion Processes", arXiv `math/0608165`.
- Gorissen, Vanderzande, "Current fluctuations in the weakly asymmetric exclusion process with open boundaries", DOI `10.1103/PhysRevE.86.051114`.
- Erhard, Franco, Xu, "Nonequilibrium joint fluctuations for current and occupation time in the symmetric exclusion process", DOI `10.1214/24-EJP1137`.
- Search also found "Exclusion process with long jumps in contact with reservoirs", DOI `10.70675/fb0d43d2z62c4z4ccdzb3adzaf2185d0e2c3`, as a direct long-jump/reservoir background item, though not a direct FCS residual match from the metadata alone.

My reading of the risk:

- High risk that equilibrium normalization and broad NESS fluctuation structure are already covered by FDT/MFT.
- Moderate risk that the `R2` residual can be derived as a standard near-equilibrium second-order response or MFT correction.
- Lower, still open risk of direct prior coverage for the exact revised subclaim: finite-density long-jump open-exclusion ledger residual, raw `delta^2`, off-center reversal sanity, and unresolved `Qhat` growth.

This argues for keeping the project only if the contribution is framed as a sharp diagnostic/residual program inside the standard framework, not as a replacement for FDT/MFT.

## 4. Recommendation On `Qhat` Growth Language

Remove all hard scaling language:

- Do not write `Qhat ~ L^{1/2}`.
- Do not write "square-root growth" except as "previous finite-window effective-exponent language now withdrawn".
- Do not call the observed growth asymptotic.

Use:

> `Qhat` grows systematically over the accessible finite-size windows. Simple model comparison currently favors a logarithmic drift over a power-law ansatz, so the asymptotic growth law is unresolved.

Stronger but still acceptable:

> The finite-window local slopes around `0.47..0.56` should be treated as effective exponents, not as evidence for an established power law.

## 5. Next Minimal Verifiable Proposition

The next minimal proposition should be narrower than "NESS FDT residual scaling":

> For fixed long-jump exponent `alpha` and fixed centered density `rho_bar=0.5`, the raw finite-volume residual satisfies
> `R2(L,delta,alpha)=C_L(alpha) delta^2 + O(delta^4)`
> with `C_L(alpha) != 0`, and the same even-in-bias coefficient is recovered under reverse bias up to numerical tolerance.

This is the right next target because it avoids unresolved asymptotic `L` growth and attacks the part of the package that is already strongest: non-circular raw `delta^2` plus reverse-bias parity. The next verification should extend one dimension at a time:

- first, smaller `delta` and a quartic correction fit at fixed `L`;
- second, off-center density only after centered coefficient stability is established;
- third, `L`-dependence of `C_L(alpha)` only after the coefficient extraction is robust.

## 6. Verdict

**Verdict: KEEP.**

Reason: The revised package should remain current-mainline because Round 2 converted the claim from a vulnerable `Qhat~L^{1/2}` scaling story into a defensible finite-volume residual program. The major reviewer attacks on circular normalization, reverse-bias contamination, FDT units, and activity conflation are materially answered at the ledger level.

However, the keep is conditional and narrow:

- KEEP as a current-mainline empirical/diagnostic claim about finite-volume NESS FDT residuals in the long-jump open exclusion ledger.
- DOWNGRADE any asymptotic scaling language.
- REDIRECT the next proof/numerics to the sharper coefficient proposition `R2=C_L(alpha)delta^2+O(delta^4)` before reopening `Qhat(L)` growth.
