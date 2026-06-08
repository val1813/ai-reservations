# REVIEWER NSF-FCS-2 Final Report

Scope: final REVIEWER audit of the seven supplied core conclusions only. No A/B derivation background is used as defense for the authors. The available paper-search-mcp tools were used; search failures are reported as limitations, not as evidence of absence.

## Narrative retreat check

No fatal narrative retreat is detected if the manuscript is framed as "bounded/current-mainline-keep/continue NSF-FCS-2 Round 2" rather than as a final theorem.

The current conclusion has retreated, appropriately, from any theorem-level statement about anomalous FDT violation scaling to a numerical mainline: equilibrium two-terminal second cumulant obeys a finite-volume FDT corollary, density-biased NESS produces a residual R2, centered scans suggest quadratic bias dependence, reverse-bias checks support evenness, and Qhat looks roughly L^{1/2} only in small-L windows. This retreat is scientifically acceptable only if the text explicitly preserves the distinction between measured finite-window ansatz and proved asymptotics.

Potential retreat risk: if earlier language claimed universal non-equilibrium FDT violation, then the present statement "Qhat appears roughly L^{1/2} in small L windows" is a major weakening. It is not a flaw by itself, but it must be made visible as a narrowing of the claim.

## L-1 hallucination / dimensional / direction / circularity check

Dimensional check:
- lambda_T''(0)=2G_T is dimensionally acceptable only under the manuscript's chosen FCS normalization where the counted integrated current, time scale, temperature/Boltzmann factors, and conductance units have already been nondimensionalized. If G_T is a linear conductance in physical units, a missing factor such as temperature, beta, time, charge, or convention-dependent 2 must be specified.
- R2(L)=lambda_T''(L)-2G_T(L) is dimensionally valid only if lambda_T'' and G_T use the same normalization as the equilibrium FDT identity.
- Qhat=R2/(delta^2 G_T) is dimensionless if delta is a density difference and R2/G_T is dimensionless. This depends on the same FCS/FDT normalization.

Direction check:
- Centered density scans giving R2 nearly quadratic in delta are directionally consistent with the reverse-bias evenness test, because an even residual has no linear-in-delta term.
- Reverse-bias comparison 0.6/0.4 vs 0.4/0.6 supports evenness only at fixed mean density rho_bar=0.5 and delta=0.2. It does not by itself establish evenness for arbitrary rho_bar, L, or microscopic forcing.
- Off-center density tests at rho_bar=0.4, 0.5, 0.65 and delta=0.2 support a nearly unchanged L-slope only over the tested window. They do not prove amplitude/slope factorization.

Circularity check:
- The primary diagnostic Qhat divides by delta^2 and G_T. If the quadratic delta law is inferred from the same finite delta values used to define the diagnostic, the analysis risks baking the quadratic hypothesis into the plotted quantity. The quadratic law should be established on R2 before Qhat is used as the main scaling object.
- Activity forcing must separate reversible_side from nonLDB_site_skew. If reversible activity preserving local detailed balance is used as evidence for a kinetic residual, that is circular: it should instead be an R2 approximately 0 sanity control.
- No explicit order-of-magnitude gulf above 10 orders is present in the supplied conclusions.

L-1 result: no immediate algebraic direction error is found, but two serious normalization/circularity vulnerabilities remain: the exact units/conventions behind lambda_T''(0)=2G_T and the possibility that Qhat presupposes the delta^2 law it is meant to diagnose.

## Three-round prior-art search plan and results

Tool status: paper-search-mcp is available and was used. arXiv searches were tried first where appropriate; several exact arXiv queries returned empty results. CrossRef and Semantic Scholar were then used as broader paper-search-mcp backends. Empty arXiv/Semantic results are not treated as proof of novelty.

Round 1: method-layer duplicate search.

Queries executed:
- arXiv: "free fermion transport full counting statistics fluctuation dissipation theorem second cumulant conductance finite volume" -> no results returned.
- arXiv: "Landauer free fermion full counting statistics noise conductance fluctuation dissipation equilibrium" -> no results returned.
- arXiv: "nonequilibrium steady state free fermion current noise density bias second cumulant full counting statistics 2023 2024 2025 2026" -> no results returned.
- arXiv: "boundary driven free fermion chain full counting statistics noise cumulants density bias" -> no results returned.
- Semantic Scholar: "free fermion transport full counting statistics fluctuation dissipation theorem second cumulant conductance finite volume" -> no useful direct result returned.
- Semantic Scholar: "Landauer free fermion full counting statistics noise conductance fluctuation dissipation equilibrium" -> returned a generic statistical physics text, not a direct duplicate.
- CrossRef: "free fermion transport full counting statistics fluctuation dissipation theorem second cumulant conductance" -> returned closely related FCS/fluctuation-theorem transport literature:
  - Saito and Utsumi, "Symmetry in full counting statistics, fluctuation theorem, and relations among nonlinear transport coefficients in the presence of a magnetic field", Phys. Rev. B 78, 115429 (2008), DOI 10.1103/physrevb.78.115429.
  - Harbola, Esposito, and Mukamel, "Statistics and fluctuation theorem for boson and fermion transport through mesoscopic junctions", Phys. Rev. B 76, 085408 (2007), DOI 10.1103/physrevb.76.085408.
  - Esposito, Harbola, and Mukamel, "Fluctuation theorem for counting statistics in electron transport through quantum junctions", Phys. Rev. B 75, 155316 (2007), DOI 10.1103/physrevb.75.155316.

Round 1 finding: no exact duplicate of the NSF-FCS-2 finite-volume density-bias residual/scaling claim was found. However, the equilibrium FDT/FCS and nonlinear transport coefficient territory is established prior art, so the manuscript cannot present lambda_T''(0)=2G_T or general FCS fluctuation-symmetry structure as a novel result.

Round 2: framework blind-spot search using ordinary-language descriptions.

Queries executed:
- CrossRef: "current noise conductance relation nonequilibrium quantum transport full counting statistics fluctuation theorem nonlinear coefficients" -> returned Saito and Utsumi 2008, Esposito/Harbola/Mukamel 2007, Esposito/Harbola/Mukamel RMP 2009, and related FCS transport entries.
- Semantic Scholar: same query -> no results returned.
- arXiv: same query -> no results returned.
- CrossRef: "violation fluctuation dissipation relation current noise nonequilibrium steady state quantum transport full counting statistics" -> returned:
  - Ness and Dash, "Nonequilibrium fluctuation-dissipation relations for one- and two-particle correlation functions in steady-state quantum transport", J. Chem. Phys. 140, 144106 (2014), DOI 10.1063/1.4870637.
  - Hsiang and Hu, "Fluctuation-dissipation relation for open quantum systems in a nonequilibrium steady state", Phys. Rev. D 102, 105006 (2020), DOI 10.1103/physrevd.102.105006.
  - Roussel, Degiovanni, and Safi, "Perturbative fluctuation dissipation relation for nonequilibrium finite-frequency noise in quantum circuits", Phys. Rev. B 93, 045102 (2016), DOI 10.1103/physrevb.93.045102.
  - Esposito, Harbola, and Mukamel, "Nonequilibrium fluctuations, fluctuation theorems, and counting statistics in quantum systems", Rev. Mod. Phys. 81, 1665 (2009), DOI 10.1103/RevModPhys.81.1665.

Round 2 finding: the literature already contains general and model-specific nonequilibrium fluctuation-dissipation relations, failures of universal NESS FDT, and FCS fluctuation theorems. This does not directly preempt the supplied finite-volume/free-fermion numerical residual, but it creates a serious positioning requirement: the manuscript must state precisely what is new relative to known FCS fluctuation relations and nonequilibrium FD relations.

Round 3: negative/counterexample/conflict search.

Queries executed:
- CrossRef: "violation fluctuation dissipation relation current noise nonequilibrium steady state quantum transport full counting statistics" -> same relevant conflict-risk results as Round 2.
- CrossRef: "local detailed balance activity reversible traffic nonequilibrium Markov processes kinetic activity fluctuation theorem" -> returned general fluctuation theorem, detailed-balance, and Markov process entries, but no direct duplicate of the reversible_side vs nonLDB_site_skew diagnostic.
- Semantic Scholar: "local detailed balance reversible activity kinetic activity nonequilibrium Markov processes fluctuation theorem" -> no results returned.

Round 3 finding: no direct published counterexample to the seven supplied conclusions was found under available paper-search-mcp tools. The closest conflict-risk paper from the search results is Ness and Dash 2014, whose abstract explicitly says there is no single universal FD theorem for NESS and that relations depend on the problem class. This is not a contradiction if the manuscript claims a bounded model-specific numerical residual, but it would conflict with any broad universal NESS-FDT claim.

Three-round duplicate judgment: three-round search completed (method-layer yes, framework blind-spot yes, negative/counterexample yes). No exact direct competitor was found under available tools. Strong adjacent prior art was found and must be cited/positioned.

## Five reviewer attacks, each severity-tagged: fatal/serious/medium/light

1. The equilibrium identity lambda_T''(0)=2G_T is presented as a finite-volume FDT corollary, but the supplied conclusions do not specify the normalization of counting field, time, temperature, charge, and conductance. A factor-of-beta or convention-dependent factor could make the central anchor formally wrong. The authors must give the exact generating function convention and derive the identity in those units. [serious]

2. The primary diagnostic Qhat=R2/(delta^2 G_T) risks circularly assuming the quadratic delta law. If R2 is only shown at a few centered densities and then normalized by delta^2, the apparent L^{1/2} scaling may be a normalization artifact rather than a property of the residual. The authors must first establish R2 proportional to delta^2 across multiple smaller deltas at fixed L before using Qhat as the main scaling observable. [serious]

3. The reverse-bias check 0.6/0.4 vs 0.4/0.6 supports evenness only at rho_bar=0.5 and delta=0.2. It does not rule out odd terms off center, finite-size odd contamination, or asymmetric boundary effects outside the tested point. The authors must repeat reversal checks at rho_bar=0.4 and 0.65 or explicitly limit evenness to the centered tested setup. [medium]

4. The claimed roughly L^{1/2} behavior is an ansatz from small-L windows, not a theorem. Without larger L, competing fits such as constant plus finite-size correction, logarithmic drift, or crossover exponent cannot be excluded. The authors must present model comparison/error bars and avoid asymptotic language. [serious]

5. The activity-forcing conclusion is currently under-separated. Reversible_side activity that preserves local detailed balance should be an R2 approximately 0 sanity control, whereas nonLDB_site_skew is the only candidate for kinetic residual evidence. Combining them would falsely attribute equilibrium-compatible activity to nonequilibrium residual physics. The authors must split these controls in tables, plots, and claims. [medium]

## Any explicit claims of citation fabrication or prior-art conflict, if found

Citation fabrication: none found under available tools. No supplied citation list was provided for verification, so this is not a full citation audit.

Prior-art conflict: no exact direct conflict was found. Adjacent prior art creates positioning constraints:
- Saito and Utsumi 2008 and related FCS fluctuation-theorem work cover symmetry relations and nonlinear transport coefficient constraints in FCS. The manuscript must not imply that FCS-FDT/Onsager-type relations are newly discovered here.
- Esposito, Harbola, and Mukamel 2009 reviews nonequilibrium fluctuations, fluctuation theorems, and counting statistics in quantum systems; it is likely essential background.
- Ness and Dash 2014 states, in the search-returned abstract, that there is no single universal FD theorem for NESS and that FD relations depend on the class of problem. This supports bounded, model-specific framing and would conflict with universal NESS-FDT language.

## Final recommendation: reject / major revision / minor revision, with one-sentence reason

Final recommendation: major revision.

Reason: the project is worth continuing as a bounded NSF-FCS-2 Round 2 numerical mainline, but the normalization of the FDT anchor, the non-circular establishment of the delta^2 law, and the small-L status of the L^{1/2} ansatz must be fixed before the claims are publishable.
