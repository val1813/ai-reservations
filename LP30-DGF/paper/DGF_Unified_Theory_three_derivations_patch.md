# Appendix Patch: Three Missing First-Principles Derivations

This patch is written for `DGF_Unified_Theory.docx`.  It uses only the paper's allowed starting points: distinguishable information states, bounded information capacity, irreversible overflow, pure mathematics, and a scalar order parameter in `[0,1]`.  Equations that presuppose an already existing Lorentzian spacetime are not used as starting points.

Notation warning.  The manuscript currently uses `q` as accessible coherence in several places.  In that convention the locked/archived fraction is

```math
q_L = 1 - q_{\rm acc}.
```

The angle law requested as `theta = pi q` is strictly true only when `q` denotes the locked fraction.  If the manuscript keeps `q = q_acc`, the same result must be written as

```math
\theta = \pi q_L = \pi(1-q_{\rm acc}).
```

## A. Non-Circular Derivation of the Newton-Type Scaling, Not the Numerical `G`

The gravitational constant must not be inserted through Planck units or through Newton's law.  This section is not a derivation of the numerical Newton constant.  DGF can derive only a conditional inverse-square response structure from information capacity, and then identify the observed `G` as the macroscopic conversion factor between information curvature and measured mass response.

Start with an information adjacency graph.  Its vertices are minimal capacity units and its edges express only direct distinguishability/transfer adjacency, not a pre-existing metric.  Each vertex carries an accessible fraction `q_i in [0,1]` and a locked fraction

```math
s_i = 1-q_i.
```

The minimal local capacity cost compatible with relabeling invariance and additivity is the quadratic edge cost

```math
{\cal C}[q]
= {1\over 2}\sum_{\langle ij\rangle} w_{ij}(q_i-q_j)^2,
\qquad w_{ij}>0 .
```

This is not a gravitational action.  It is the unique lowest-order penalty for neighboring information units carrying different accessibility.  A localized archived defect is a conserved source charge

```math
S_\Omega=\sum_{i\in\Omega}s_i .
```

Outside the defect, minimizing `C[q]` gives the source-free graph Laplace equation

```math
\sum_{j\sim i} w_{ij}(q_i-q_j)=0.
```

With a source region, the graph problem is the corresponding Poisson problem:

```math
\sum_{j\sim i}w_{ij}(q_i-q_j)=\alpha s_i ,
```

or, equivalently, the boundary flux through a region is fixed by the total archived charge:

```math
\sum_{\partial\Omega} w_{ij}(q_i-q_j) = \alpha S_\Omega ,
```

where `alpha` is an information-response normalization, not Newton's constant.

At large scales, if the adjacency graph has an isotropic three-dimensional continuum limit and the field approaches a constant at infinity, the long-range Green-function term is

```math
\phi(r) = {\alpha S_\Omega\over 4\pi r},
\qquad
|\nabla\phi| = {\alpha S_\Omega\over 4\pi r^2}.
```

The inverse-square form therefore follows from the Green function of the capacity Laplacian only under the additional large-scale condition `d_eff=3`.  In a different effective dimension the long-range power would be different.  No Newtonian force law has been assumed.

A test archived defect with charge `s_t` responds to the same capacity gradient.  The interaction is bilinear because independent archived charges add:

```math
{\cal R}(r)\propto {S_\Omega s_t\over r^2}.
```

Mass is then introduced only after the information derivation, through the independent DGF branch mass map

```math
m_b(s_b)={2m_*\over\pi}\sin\left({\pi s_b\over2}\right).
```

For weakly archived test branches, `m_b \simeq m_* s_b`, so the information response is proportional to the product of the source and test archived charges.  For a macroscopic body, the additive charge is first

```math
Q_S=\sum_{b\subset S}s_b .
```

Only after independent mass calibration may `Q_S` be replaced by the measured mass `M`.  With the same calibration for source and test bodies, the large-scale response can be written in Newton form,

```math
F(r)=-G_{\rm DGF}{M m\over r^2}.
```

Here

```math
G_{\rm DGF}
= {(\hbox{capacity stiffness})\times(\hbox{response normalization})
   \times(\hbox{length conversion})^3
  \over
  (\hbox{mass conversion})^2 } .
```

Thus `G` is not used to define `q`, mass, or the field equation.  It is the late-stage conversion factor that maps the dimensionless information-curvature response into laboratory force units.  The result proved here is only this:

```text
Given effective dimension three, radial isotropy, source-exterior conservation
of information-response flux, and a common archived-charge calibration for
source and test bodies, the long-range response scales as r^{-2}.
```

`G_DGF` is then an empirical conversion factor fixing units and normalization when the information-response law is compared with measured gravitational coupling.  No numerical value of `G` is predicted without calibration.  The paper should therefore avoid the phrases "derive Newton's constant", "derive gravity", or "derive G from information" unless they are immediately qualified as "derive only the inverse-square scaling form under the stated assumptions."

## B. Conditional Uniqueness Proof of the Linear Angle Law

Let `q_L` denote the locked/archived fraction.  The two endpoints are:

```math
q_L=0:\hbox{ fully accessible},\qquad
q_L=1:\hbox{ fully archived}.
```

Normalize the information projection interval between these endpoints to a half-circle:

```math
\theta(0)=0,\qquad \theta(1)=\pi.
```

This normalization is pure geometry.  It is not a Wick rotation and does not presuppose Lorentzian spacetime.

Now take `N` indistinguishable, equal-weight archive microchannels.  If `j` channels are locked, then

```math
q_L={j\over N}.
```

The angle assignment must satisfy four requirements:

1. endpoint normalization;
2. invariance under relabeling of indistinguishable archive channels;
3. coarse-graining additivity: the angle of a union of disjoint equal channels is the sum of the angle increments assigned to those channels.
4. cross-refinement consistency: equivalent fractions such as `1/2` and `2/4` are assigned the same angle.

Relabeling gives every elementary channel the same angle increment.  Additivity gives

```math
\theta\left({j\over N}\right)
= j\,\theta\left({1\over N}\right).
```

The endpoint condition with `j=N` gives

```math
N\,\theta\left({1\over N}\right)=\pi,
```

therefore

```math
\theta\left({j\over N}\right)=\pi {j\over N}.
```

For rational locked fractions this proves the unique additive assignment

```math
\theta(q_L)=\pi q_L.
```

Continuity of the macroscopic coarse-grained limit extends the result to all `q_L in [0,1]`.  Monotonicity or measurability would serve the same role by excluding pathological additive functions.

This is a conditional uniqueness theorem, not an unconditional derivation of `pi` from information existence alone.  The half-circle endpoint normalization is a coordinate convention for the accessible/archive projection interval.  Given that convention, any nonlinear replacement `theta=f(q_L)` with `f(a+b)\ne f(a)+f(b)` would make the result depend on whether disjoint archive channels are grouped before or after assigning angle.  It violates additive coarse-graining.  Hence the linear law is not a fit; it is the unique scalar angle coordinate compatible with endpoint normalization, relabeling invariance, cross-refinement consistency, and archive-channel additivity.

The paper should not say that information principles alone "force" `theta=pi q` or that `pi` is predicted.  The safe claim is:

```text
Under the stated coordinate axioms, theta=pi q_L is the unique compatible
archive-loss angle.  If q denotes accessible coherence, theta=pi(1-q).
```

In the accessible-coherence notation of the current manuscript,

```math
\boxed{\theta=\pi(1-q_{\rm acc})}.
```

If the manuscript instead defines `q` as locked information, then the boxed result is

```math
\boxed{\theta=\pi q}.
```

## C. First-Principles `q` Field Equation

The `q` equation should not begin as a wave equation, diffusion equation, Schrodinger equation, Einstein equation, or Lindblad equation.  It begins as the update law for bounded information access on an adjacency graph.

Use the lowest-order local, relabeling-invariant, additive normal form through second order in neighboring differences:

```math
{\cal F}[q]
=\sum_i U(q_i)
 +{1\over2}\sum_{\langle ij\rangle}\kappa_{ij}(q_i-q_j)^2
 -\sum_i \eta_i q_i .
```

The quadratic edge term is not claimed to be the only possible microscopic law.  It is the minimal smooth normal form when neighboring accessibility differences are small, the graph is undirected at this level, and the cost is invariant under `q_i-q_j -> -(q_i-q_j)`.

Here:

```math
0\le q_i\le1,
```

`U(q)` is the local capacity/overflow cost, `kappa_ij>0` is adjacency stiffness, and `eta_i` is an external information source or sink.  If `F` is measured in information units, then `U`, `kappa`, `eta q`, and `U' q` carry the same information-unit normalization.  None of these symbols is a spacetime metric or a gravitational field.

Irreversible overflow means that the system updates in the direction that reduces unavailable capacity cost while respecting the bounds on `q`.  With an ordinal update parameter `lambda`, not pre-existing physical time, the constrained gradient-flow equation is

```math
\tau_i {dq_i\over d\lambda}
\in
-{\partial{\cal F}\over\partial q_i}-N_{[0,1]}(q_i),
```

where `N_[0,1](q_i)` is the normal cone enforcing the capacity bound.  Equivalently: if `q_i=0`, the update cannot push `q_i` below zero; if `q_i=1`, it cannot push `q_i` above one.  Away from the saturated endpoints,

```math
\tau_i {dq_i\over d\lambda}
=
\sum_{j\sim i}\kappa_{ij}(q_j-q_i)
-U'(q_i)+\eta_i .
```

Here `tau_i` is an update impedance or information-relaxation weight, not a physical time constant measured in seconds.  This is the first-principles DGF `q` update law on the information graph in its minimal effective normal form.  It follows from bounded capacity, locality on the adjacency graph, additivity, smooth lowest-order coupling, and irreversible relaxation.  No spacetime field equation is assumed.

The large-scale continuum form is only a later approximation.  When the graph admits a smooth coarse-grained description, the graph Laplacian becomes a divergence operator and the equation becomes

```math
\tau(q)\partial_\lambda q
=\nabla_a\!\left(D^{ab}(q)\nabla_b q\right)
-U'(q)+\eta .
```

`D^{ab}` is a graph-coarse-grained stiffness tensor.  Before physical space has emerged, it should not be called a laboratory diffusion coefficient.  For an isotropic coarse-grained phase,

```math
\tau(q)\partial_\lambda q
=\nabla\!\cdot\!\left(D(q)\nabla q\right)-U'(q)+\eta .
```

The stationary source-free equation is

```math
\nabla\!\cdot\!\left(D(q)\nabla q\right)-U'(q)=0.
```

This is not postulated physics; it is the continuum limit of the graph-capacity variational law.  Physical time, spatial distance, gravitational response, and laboratory units enter only after the `q` order parameter has generated a stable coarse-grained ordering.  The continuum PDE must never be used as a premise to justify the graph equation; the logical direction is graph update law first, continuum equation second.

## Inspector-Ready Claims

1. `G` is not derived from itself.  DGF derives a Newton-type inverse-square information response from the three-dimensional Green function of the capacity Laplacian, then identifies `G_DGF` as the unit-conversion constant.  The numerical value of `G` requires calibration.
2. `theta=pi q` is strict only if `q` is the locked fraction.  With `q` as accessible coherence, the strict result is `theta=pi(1-q)`.
3. The `q` field equation is first a bounded graph-gradient flow.  The PDE is only the continuum limit, so it does not smuggle in pre-existing spacetime dynamics.

# Second Appendix Patch: Remaining Structural Gaps

The following additions address the next six gaps.  The strongest correction is negative: the current principles do not yet prove physical `3+1` Lorentzian spacetime.  They define an information-order structure and identify the extra selection principles needed for `3+1`.

## D. Space as an Equal-`q` Information Antichain and the Status of `d=3`

The manuscript should not state that three-dimensional physical space has already been derived from the present axioms.  What can be derived without circularity is weaker and cleaner: a way to define candidate spatial adjacency after the information-order structure is already present.

Let `L=1-q_acc` be the locked fraction or any monotone equivalent.  Irreversible overflow defines an order relation on information states:

```math
X\prec Y \quad\hbox{only if}\quad L(Y)>L(X).
```

At a fixed value of `L`, states are mutually unordered by the overflow relation.  The fixed-`L` set is therefore an antichain.  Space is not introduced as a coordinate background; the candidate spatial substrate is the adjacency graph induced on this antichain.  To avoid circularity, the adjacency relation must be defined without metric distance, manifold locality, or any prior near/far relation.  It may use only information-theoretic adjacency, such as direct distinguishability, update compatibility, shared record boundary, or non-factorizable record correlation:

```math
{\cal G}_L=(V_L,E_L),
\qquad
V_L=\{i:L_i=L\}.
```

The effective spatial dimension is then a graph observable, not an assumed coordinate count.  Two usable definitions are:

```math
d_H=\lim_{R\to\infty}{d\log |B(R)|\over d\log R},
```

where `B(R)` is the graph ball, and the spectral dimension

```math
d_s=-2\lim_{\sigma\to\infty}{d\log P_{\rm ret}(\sigma)\over d\log\sigma},
```

where `P_ret` is the return probability for a graph random walk.  In this language, "space is three-dimensional" means

```math
d_H\simeq d_s\simeq 3
```

on large equal-`L` antichains.

The present DGF principles do not by themselves force this value.  To select `d=3`, the paper must add a stability-selection principle.  A cautious formulation is:

```text
Macroscopic records must be locally isolable, allow information paths to bypass
localized defects, support stable boundary/encapsulation records, and admit a
nondegenerate long-range conserved-flux response.
```

This is a graph-theoretic selection rule, not a theorem yet.  The intended topological content is that dimensions below three do not generically supply enough independent adjacency to combine bypassing with stable encapsulation, while dimensions above three make linking/encapsulation non-minimal and generically unstable as a local record primitive.  If this selection rule is later proven, `d=3` becomes the selected minimal stable record dimension.

The safe claim for the manuscript is therefore:

```text
DGF defines a candidate effective space as the equal-locked-fraction information
graph. Its dimension is measured only after the graph is built, for example by
Hausdorff/spectral graph dimension. The choice d=3 is presently a
stable-local-record selection postulate or candidate mechanism, not a completed
first-principles proof and not yet a derivation of physical space.
```

With the single irreversible order parameter below, the large-scale candidate structure is "three effective adjacency dimensions plus one irreversible order parameter."  This is not yet a derivation of full Lorentzian `3+1` spacetime, light cones, or metric signature.

## E. Why There Is One Temporal Order Dimension

The phrase "time is the direction of decreasing `q`" is too compressed and risks circularity.  It should be replaced by an order-theoretic statement.

Let `L` denote locked fraction, equivalently a monotone functional of accessible `q`.  Irreversible overflow defines an ordinal update relation.  This relation is primitive in the minimal formalism; it should not be described using prior physical notions of evolution, duration, clock rate, or proper time:

```math
X\prec Y \quad\Longleftrightarrow\quad L(Y)>L(X)
```

for states connected by allowed overflow updates.  No physical time variable is assumed here.  The relation only says which state can stand after another in the irreversible update order.

Because current DGF contains one bounded scalar order parameter, regular level sets

```math
L=\hbox{constant}
```

are antichains of this order, and all irreversible updates cross them in one monotone ordinal coordinate.  This selects one temporal order dimension, not a unique trajectory and not a pre-existing Lorentzian time vector.

Zero temporal order dimensions would erase the nontrivial monotone relation required by irreversible overflow.  Two or more temporal order dimensions would require two or more independent Lyapunov/order parameters, not functionally reducible to `L`:

```math
L_1,\ L_2,\ldots
```

That would be a different theory with a vector-valued update order.  It is not implied by a single bounded-capacity scalar `q`.

The safe claim is:

```text
In the minimal DGF formulation, temporal ordering is represented by one
ordinal update relation generated by a single monotonic locked-fraction
functional. This is not metric time: it defines no duration, clock rate,
proper time, or relativistic temporal geometry. A map from this ordinal
parameter to observable clock readings is an additional calibration step.
```

## F. Non-Circular Information Form of `E=mc^2`

The manuscript should not start from `m_p c^2`, because `c` is not an allowed primitive in the first-principles layer.  The non-circular statement is instead an information-rate calibration.  This is not an independent derivation of mass-energy equivalence and does not predict the numerical value of `c`.

Define `v_I` as the maximum effective propagation/update rate on the emergent information adjacency structure after independent length and ordinal-update scales have been calibrated:

```math
v_I={\Delta \ell_{\rm info}\over \Delta \tau_{\rm update}} .
```

This definition must not use the modern SI definition of the meter through light speed, Lorentzian spacetime, or electromagnetic light propagation as a premise.  `v_I` is first an information-processing speed.

Mass `m` is the inertial response calibration of archived information: it measures how strongly a locked record resists changes of the update pattern.  Energy `E` is the same calibration system's releasable work capacity of an archived record.  The structural relation is

```math
E=m v_I^2 .
```

This should be read as a common normalization of inertial response and work capacity.  The square appears because the maximum information rate limits both the response to update displacement and the capacity to transfer that response through the update network; in laboratory dimensions this is the same `L^2/T^2` factor that converts mass response into work capacity.

The coefficient is set to one by the joint definition of the inertial-mass and energy scales.  This is not yet a numerical prediction.  If large-scale propagation experiments later identify

```math
v_I=c_{\rm obs},
```

then the laboratory expression becomes

```math
E=m c_{\rm obs}^2 .
```

Thus `c^2` is not a first-principles input.  It is the square of the calibrated maximum information-processing rate.  The numerical value of `c` still requires an independent calibration of information length and update interval.  The paper should not claim to predict `c` without that calibration.

The safe claim is:

```text
E=m v_I^2 is a non-predictive structural rewriting. v_I denotes the invariant
upper scale at which stable physical records can be updated. Its empirical
value is fixed a posteriori by the relativistic causal scale, yielding v_I=c.
This does not derive c; it only keeps c out of the first-principles premise.
```

## G. Projection Rule from Complex Information Encoding to Observables

The complex object used in the manuscript should not be presented as a physical complex metric.  It is safer to treat it as a generating object

```math
Z(q)
```

that encodes two layers:

1. record-stable archived information;
2. transition/coherence bookkeeping that may affect interference but is not itself a directly archived record.

Physical observables must be obtained by an observation map, not by arbitrary real-part selection.  This is only a projection constraint principle; it does not by itself derive a GR metric or a unique observable without a measurement protocol:

```math
{\cal O}=P_{\rm obs}[Z].
```

Mathematically, `Z` must first be placed in a representation space `\mathcal Z`, with an unobservable rephasing group `\mathcal R` acting as

```math
Z\sim RZ,\qquad R\in{\cal R}.
```

Admissible record functionals are maps on equivalence classes:

```math
{\cal O}:{\cal Z}/{\cal R}\to{\cal V}_{\rm rec}.
```

The map `P_obs` must satisfy:

1. rephasing invariance: unobservable transformations `Z -> e^{i\alpha}Z` do not change the archived observable;
2. coarse-graining stability: regrouping unresolved record channels does not change the macroscopic record;
3. locked-limit reality: in the fully locked limit, repeatable records are real-valued;
4. record additivity: independent repeated records add at the record-density level.

Therefore `P_obs` is not simply `Re Z`.  For a general complex object, `Re(e^{i\alpha}Z)` is not invariant.  The correct order is:

```text
quotient by unobservable rephasing first, then project to the stable record
functional.
```

One may distinguish a linear record projection

```math
P_{\rm rec}[Z]
```

from a positive intensity map

```math
I[Z],
```

where `I[Z]` may involve `|Z|` or `|Z|^2` and is used only for positive weights or probabilities.  These two maps should not be conflated.

If the manuscript writes

```math
g_{\rm eff}=P_{\rm obs}[Z(q)],
```

then `g_eff` denotes an effective real record/response object produced by the observation rule.  It is not a GR metric derived from a physical complex metric, and it does not presuppose a Lorentzian observer.  Imaginary or phase-like components can affect observations only through rephasing-invariant interference or transition functionals; they are not directly archived classical records.

The safe claim is:

```text
The projection rule removes representational phase redundancy and restricts
observable candidates to record-stable functionals. It does not guarantee
unique observables, does not provide a measurement protocol by itself, and
does not derive a GR metric from Z(q).
```

## H. Dark-Energy Dynamics as a Fit Interface, Not Yet a Prediction

The manuscript's current dark-energy language should be lowered.  A slow increase of archived fraction can imitate a quasi-static dark component, but this is not yet a quantitative prediction until the mean archived-fraction dynamics is specified and fitted.

This section does not use GR/Friedmann equations as DGF first principles.  Any `H(z)` expression below is only a posterior cosmology interface for comparison with CMB, supernova, and BAO data.

Start from the graph `q` update law and define the cosmological locked fraction

```math
\bar A(\lambda)=1-\langle q\rangle_\lambda .
```

For a large closed averaging domain, graph-divergence terms vanish after averaging.  With the sign convention

```math
\tau {dq\over d\lambda}=\eta-U'(q)+\cdots ,
```

and `\bar A=1-\langle q\rangle`, the remaining mean equation has the schematic form

```math
{d\bar A\over d\lambda}
=\left\langle {U'(q)-\eta\over\tau(q)}\right\rangle .
```

A minimal phenomenological closure is

```math
{d\bar A\over d\lambda}
=\gamma \bar A(1-\bar A)-\xi(\bar A-\bar A_{\rm eq})+\cdots ,
```

where `gamma`, `xi`, and `A_eq` are not predicted by the current first-principles layer.  They encode the mean archival drive, leakage/reset, and endpoint tendency.

Here `q` and `\bar A` are dimensionless.  `lambda` is the evolution parameter of the fit interface, `tau` has the same dimension as `lambda`, `U'(q)-eta` is dimensionless, and `gamma` and `xi` have dimension `1/[lambda]`.  The replacement of the average by a closed ODE for `\bar A` assumes a large-scale homogeneous, no-boundary, or small-fluctuation closure; in general `\langle U'(q)\rangle\ne U'(\langle q\rangle)`.

The archived component may then be parameterized as

```math
\rho_A(z)=\rho_{A0}{f[\bar A(z)]\over f[\bar A(0)]}.
```

Only at the observational comparison layer may one use the standard cosmology fit interface

```math
H^2(z)=H_0^2\left[
\Omega_m(1+z)^3+\Omega_r(1+z)^4+
\Omega_A{f[\bar A(z)]\over f[\bar A(0)]}
\right],
```

and

```math
w_{\rm eff}(z)
=-1+{1+z\over3}{d\log\rho_A\over dz}.
```

This use of `H(z)` is not a first-principles derivation from DGF.  It is a data-interface layer for CMB, supernova, and BAO comparison.  The safe claim is:

The map requires `f(\bar A)>0` and `f[\bar A(0)]\ne0`.  To close the model one must also specify `\lambda(z)` or `d\lambda/dz`.  If that relation is imported from standard cosmology, it remains part of the posterior fit interface and cannot be used to claim an independent DGF derivation of acceleration.

```text
DGF supplies a candidate archived-fraction order parameter for dark-sector
phenomenology.  Quantitative acceleration requires fitting the mean archival
dynamics.  The current manuscript does not yet provide a parameter-free
prediction of H(z), w(z), or the observed dark-energy density.
```

The manuscript should also state:

```text
We do not claim that DGF predicts dark-energy dynamics from first principles.
The dark-energy sector is used only as a posterior phenomenological interface
to cosmological data, assuming the standard GR/Friedmann background. Any
inferred DGF parameters in this sector are numerical fit parameters, not
independent predictions. Model comparison must report parameter counts and
baseline comparisons against Lambda/CDM, wCDM, and CPL, for example through
AIC/BIC or Bayesian evidence.
```

## I. Standard-Model Masses: Electron as a Mapping, Not a Prediction

The branch mass map

```math
m(A)={2m_*\over\pi}\sin\left({\pi A\over2}\right)
```

can be inverted:

```math
A(m)={2\over\pi}\arcsin\left({\pi m\over2m_*}\right).
```

Using `m_*=2.176434e-8 kg` and `m_e=9.1093837139e-31 kg`,

```math
m_{\max}={2m_*\over\pi}=1.38556091765306\times10^{-8}{\rm kg},
```

and

```math
A_e
={2\over\pi}\arcsin\left({\pi m_e\over2m_*}\right)
\simeq 4.1854628782219\times10^{-23}.
```

Since `A_e` is extremely small,

```math
A_e\simeq {m_e\over m_*}.
```

This is only a consistency mapping from a known mass to the DGF archived fraction.  It is not a derivation of the electron mass.  To become a prediction, DGF must compute `A_e` independently from an internal information structure, representation count, coupling invariant, topological record number, or another non-mass input.

The input-output chain must remain explicit:

```text
input: observed m_e
operation: invert the DGF mass map
output: matched A_e
status: numerical matching, not prediction
```

The safe claim is:

```text
Known particle masses can be mapped into tiny archived fractions under the DGF
mass map.  This shows how the formula would encode standard masses, but it does
not explain the Standard Model spectrum until A-values are independently
derived.
```

The manuscript should not use "derive", "predict", or "explain" for Standard Model masses unless the corresponding `A_i` values are fixed independently of those masses and the number of shared structural inputs is smaller than the number of masses being matched.
