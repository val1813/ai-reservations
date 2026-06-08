# NSF-FCS-2R Validation Review A

**Role:** A doctor, standard-framework / literature-driven review  
**Date:** 2026-06-03  
**Object reviewed:** coefficient / parity / separability package

## Scope Read

Read project SOP and required state/synthesis files:

- `D:\Claude\ai-reservations\AGENTS.md`
- `D:\Claude\ai-reservations\ai\CLAUDE.md`
- `D:\Claude\ai-reservations\ai\A_AGENT.md`
- `project\Phase清单.md`
- `synthesis\PI_NSF_FCS2R_stop_check.md`
- `current\plan\NSF-FCS-2R_当前状态与实验计划.md`
- `synthesis\PI_NSF_FCS2R_coefficient_extraction.md`
- `synthesis\PI_NSF_FCS2R_activity_parity.md`
- `synthesis\PI_NSF_FCS2R_separability_synthesis.md`
- `synthesis\PI_NSF_FCS2_round2_AB_synthesis.md`

I did not read `current\B` for this round.

## Standard-Framework Check

Relevant prior framework:

- Baiesi, Maes, Wynants, "Nonequilibrium Linear Response for Markov Dynamics, I: Jump Processes and Overdamped Diffusions," J. Stat. Phys. 137, 1094-1116, DOI `10.1007/s10955-009-9852-8`.
- Baiesi, Maes, Wynants, "Fluctuations and Response of Nonequilibrium States," Phys. Rev. Lett. 103, 010602, DOI `10.1103/physrevlett.103.010602`.
- Bertini, De Sole, Gabrielli, Jona-Lasinio, Landim, "Macroscopic Fluctuation Theory for Stationary Non-Equilibrium States," J. Stat. Phys. 107, 635-675, DOI `10.1023/A:1014525911391`.

These references make the main coverage risk sharp: nonequilibrium response theory already treats response away from equilibrium as containing both entropic/time-antisymmetric and frenetic/time-symmetric contributions, while MFT already supplies a broad nonlinear fluctuation-response language for boundary-driven diffusive systems. Therefore NSF-FCS-2R cannot claim a new general FDT violation principle or a new universal nonequilibrium curvature theory without a metric/projection definition and an asymptotic derivation.

## 1. Strongest Keepable Proposition

The strongest proposition worth keeping is finite-volume and ledger-conventional:

> In the ledger's dimensionless Markov-affinity convention, for the tested long-jump open exclusion windows `L=4..7`, `alpha=0.5,1.0`, the finite-volume residual `R2=lambda_T''-2G_T` gives a parity-resolved diagnostic: centered density bias contributes a stable positive `delta^2` coefficient, equal-density `nonLDB_site_skew` contributes an even `A^2` coefficient, and the two channels are additive to current numerical precision in the tested mixed window.

This is not an asymptotic scaling theorem. It is a finite-volume response-coordinate proposition with explicit ledger provenance.

## 2. Maximum Coverage Risk Under Standard FDT/MFT/Near-Equilibrium Response

The largest risk is overclaiming novelty and geometry.

Standard near-equilibrium response already permits deviations from the equilibrium FDT form once the dynamics is driven out of equilibrium, and the Baiesi-Maes-Wynants framework identifies traffic/frenetic terms as standard response ingredients. MFT likewise gives a mature response/fluctuation structure for boundary-driven exclusion-like systems. Thus:

- `R2` must not be advertised as a universal FDT anomaly.
- `R2/G_T` must not be called a proven normal curvature unless the equilibrium FDT surface, metric, and projection are explicitly defined.
- `reversible_side` changing the NESS coefficient is not surprising enough by itself; it is consistent with traffic/frenetic response language.
- Any reviewer will likely ask whether the observed `C_L`, `A^2`, and additivity are consequences of symmetry plus local detailed balance bookkeeping rather than a new transport mechanism.

The package survives only if framed as a precise finite-volume diagnostic and coefficient ledger, not as a new general FDT/MFT principle.

## 3. Most Worth Retaining

The most valuable part is the parity-resolved coefficient extraction:

- density bias: `R2 = C_L(alpha) delta^2 + D_L(alpha) delta^4`, with `C_L(alpha)>0` in all tested cells;
- non-LDB skew at equal density: leading resolved response is even, `A^2`, with odd term near numerical floor;
- reversible-side control: equilibrium residual remains numerical floor, separating LDB-preserving traffic from non-LDB forcing at equilibrium.

This is the part most likely to withstand review because it is modest, falsifiable, and tied to sign/parity checks rather than exponent fitting.

## 4. Must Be Downgraded

The following must be downgraded:

- Any asymptotic `L` law, including `Qhat~L^{1/2}` or any power-law/exponent language.
- Any claim that `R2/G_T` is a proven geometric second normal curvature.
- Any statement that separability is symmetric across all perturbations: `reversible_side` is not a strict null under density-biased NESS, because it renormalizes the curvature coefficient at a few-percent level.
- Any generic "FDT violation discovery" phrasing. The correct statement is ledger-conventional finite-volume FDT residual response.

## 5. Next Minimal Analytic/Numeric Proposition

The next proposition should be narrower than a reviewer gate theorem:

> At fixed finite `L` and `alpha`, the generator perturbation has a symmetry-implied expansion  
> `R2(delta,A)=C_L delta^2 + E_L A^2 + H_L delta^2 A^2 + O(delta^4,A^4)`  
> for centered density bias and equal-density `nonLDB_site_skew`, while odd terms vanish by the tested left/right and `A -> -A` symmetries.

Minimum work:

1. Analytic: derive the absence of `delta`, `A`, and `delta A` terms from the finite Markov generator symmetries and the chosen counting-field convention.
2. Numeric: extend mixed fits beyond the single `delta=0.04`, `A=0.10` slice to at least `delta=0.02,0.04,0.06` and `A=0.05,0.10`, fitting `delta^2`, `A^2`, and `delta^2 A^2`.
3. Control: report whether `reversible_side` enters only through NESS coefficient renormalization and bound its effect relative to `C_L`.

This is the minimum bridge from ledger evidence to an analytic coefficient theorem.

## 6. Verdict

**Verdict: DOWNGRADE.**

The package should be kept as a finite-volume diagnostic program, but it is not yet sufficient for a REVIEWER gate as a standalone claim. The coefficient/parity evidence is real and should remain active; the separability statement must be asymmetric and finite-window; the next step should redirect toward a symmetry-derived coefficient theorem plus expanded mixed-fit confirmation.

