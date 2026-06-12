# Referee Report — Nature Physics

**Manuscript:** "Effective Metric from Information Processing Rate: A Derivation Without Ansatz"
**Recommendation:** Reject (the claimed derivation is a chain of five unevidenced choices; the core function $\tau_{\text{eff}}(q)$ is a deeper ansatz, not a derivation)
**Confidential to Editor:** Yes
**Benchmark Standard:** Bojowald-Duque, PRD 109, 084006 (2024) — constraint algebra closure

---

## Summary of Claims

The manuscript asserts that the DGF effective metric

$$ds^2 = -q^2 c^2 dt^2 + q^{-2} dr^2 + r^2 d\Omega^2$$

is not an ansatz but a rigorous derivation from an operational definition of the information processing rate. The derivation chain is:

1. Lattice processing time $\tau_{\text{eff}} = \tau_0/q$ (lower $q$ → less capacity → slower processing)
2. Proper time $d\tau = q\,dt$ (lattice update count measures local time)
3. Signal crossing time $t_{\text{prop}} = \tau_0/q$ → effective separation $dR = dr/q$
4. Local inertial frame $ds^2 = -c^2 d\tau^2 + dR^2 + R^2 d\Omega^2$
5. Substitution → $ds^2 = -q^2 c^2 dt^2 + q^{-2} dr^2 + R^2 d\Omega^2$

The manuscript claims this derivation matches the rigor of Bojowald-Duque (PRD 109, 084006), where the effective metric emerges from closure of the hypersurface deformation algebra. The claimed "closure condition" is: *lattice update count = proper time measure*.

This reviewer has examined each step with a fundamental-skepticism stance. None of the five steps survive scrutiny. The derivation is a sequence of five unevidenced choices, each of which — if made differently — would produce a different metric. The claim of "rigorous derivation" is therefore false.

---

## ATTACK 1: $\tau_{\text{eff}} = \tau_0/q$ — The Linear Form Is Chosen, Not Derived

This is the foundational step. Every subsequent step inherits its form from this choice. The manuscript states:

> "$\tau_{\text{eff}} = \tau_0/q$ — lower $q$ → less capacity → slower processing."

The DGF axioms specify that a lattice node has bounded information capacity and that $q \in [0,1]$ measures the fraction of capacity available. They do **not** specify the functional form of the processing time $\tau_{\text{eff}}(q)$.

**The space of admissible functions.** Any monotone decreasing function satisfies the qualitative requirement "lower $q$ → slower processing":

| Functional form | $\tau_{\text{eff}}(q)$ | $d\tau$ | $dR$ | Metric $g_{rr}$ |
|---|---|---|---|---|
| Linear (chosen) | $\tau_0/q$ | $q\,dt$ | $dr/q$ | $1/q^2$ |
| Quadratic | $\tau_0/q^2$ | $q^2\,dt$ | $dr/q^2$ | $1/q^4$ |
| Square-root | $\tau_0/\sqrt{q}$ | $\sqrt{q}\,dt$ | $dr/\sqrt{q}$ | $1/q$ |
| Exponential | $\tau_0 e^{1-q}$ | $e^{-(1-q)}dt$ | $e^{-(1-q)}dr$ | $e^{2(1-q)}$ |
| Logarithmic | $\tau_0(1-\ln q)$ | $dt/(1-\ln q)$ | $dr/(1-\ln q)$ | $(1-\ln q)^{-2}$ |

**Every one of these functions satisfies "lower $q$ → slower processing."** Every one produces a different effective metric. Every one produces different 2PN deviations, different light deflection, different gravitational wave predictions. The linear $1/q$ form is the **only** one that reproduces the Newtonian limit $g_{rr} \approx 1 + 2GM/rc^2$ at 1PN. The choice is teleological: the function was selected to produce the desired answer.

**The Bojowald-Duque contrast.** In Bojowald-Duque, the structure functions that determine the metric are not chosen — they are **computed** from the Poisson brackets of the Hamiltonian constraint:

$$[H[N_1], H[N_2]] = D[q^{ab}(N_1 \nabla_b N_2 - N_2 \nabla_b N_1)]$$

The function $q^{ab}$ that appears in the metric is the same function forced by algebraic closure. There is no freedom to choose $f(q)$ — the algebra either closes or it does not. DGF's derivation has no constraint bracket, no algebraic closure condition, and hence no mechanism to force the $1/q$ form from internal consistency.

**What would be needed.** To claim a derivation rather than an ansatz, the manuscript would need to prove that the $1/q$ form is the **unique** function consistent with DGF axioms. This would require:
- An algebraic structure analogous to the hypersurface deformation algebra
- A proof that any deviation from $1/q$ produces an internal inconsistency
- Or, failing that, a derivation of $f(q)$ from the microscopic dynamics of the causal graph

The manuscript provides none of these. The function is simply asserted.

**Verdict:** Step 1 is an unevidenced choice among infinitely many admissible functions. The "derivation" is already ansatz-dependent at its foundation.

---

## ATTACK 2: $d\tau = q\,dt$ — The $q \to 1$ Limit Is Unanalyzed and Potentially Singular

The manuscript states:

> "Proper time $d\tau = q\,dt$ — lattice update count measures local time."

**What is an "update"?** The operational definition is critical. An "update" is defined as an information processing event at a lattice node. But the relationship between $q$ and the occurrence of updates is never specified:

- **If updates occur regardless of $q$:** Then when $q=1$ (no overflow, full capacity available), the lattice is still updating at the base rate $\tau_0$. In this case, proper time flows at the same rate everywhere — $d\tau = dt$ — and $d\tau = q\,dt$ is false at $q=1$.
- **If updates are tied to overflow events:** Then when $q=1$, there are no overflow events, no updates, and $\tau_{\text{eff}}$ is undefined. Proper time stops. The limit $q \to 1$ is singular.
- **If updates are tied to capacity usage:** Then the relationship could be $d\tau \propto (1-q)\,dt$ (time flows faster when more capacity is used) or any other monotone function.

The manuscript provides no operational definition of "update" that makes $d\tau = q\,dt$ follow necessarily.

**The $q \to 1$ problem.** Take the vacuum: $q=1$ everywhere (no archived information, full capacity). The metric becomes:

$$ds^2 = -c^2 dt^2 + dr^2 + r^2 d\Omega^2$$

This is Minkowski space — correct. But the derivation of this limit is path-dependent:

- Under $\tau_{\text{eff}} = \tau_0/q$: as $q \to 1$, $\tau_{\text{eff}} \to \tau_0$, $d\tau \to dt$, $dR \to dr$. Smooth limit.
- Under $\tau_{\text{eff}} = \tau_0/q^2$: as $q \to 1$, $\tau_{\text{eff}} \to \tau_0$, $d\tau \to dt$, $dR \to dr$. Also smooth.
- Under $\tau_{\text{eff}} = \tau_0 e^{1-q}$: as $q \to 1$, $\tau_{\text{eff}} \to \tau_0$, $d\tau \to dt$, $dR \to dr$. Also smooth.

**All candidate functions give the same vacuum limit.** The vacuum cannot discriminate among them. This means the "derivation" has zero empirical content at the $q \to 1$ boundary condition — it is consistent with any $f(q)$ satisfying $f(1)=1$. The Newtonian limit check in the manuscript (Section 4.1 of the DGF wall document) verifies only that the chosen function reproduces GR at 1PN — it does not verify uniqueness.

**Verdict:** The operational definition of "update" is underspecified. The relationship $d\tau = q\,dt$ does not follow from DGF axioms without additional assumptions about what constitutes an update event. The $q \to 1$ limit is consistent with any $f(q)$ where $f(1)=1$, providing zero constraint on the functional form.

---

## ATTACK 3: $dR = dr/q$ Uses the Wrong Speed of Light

The manuscript states:

> "Signal crossing time $t_{\text{prop}} = \tau_0/q$ → effective separation $dR = c \cdot t_{\text{prop}} = \mathfrak{l}/q$."

**Which $c$ is being used?** The speed of light $c$ appears in this step as a conversion factor between time and distance. But in the DGF framework, what is $c$?

If $c$ is the **vacuum** speed of light ($c = \mathfrak{l}/\tau_0$, the speed at $q=1$), then using it in a $q<1$ region is an implicit assumption: *signals propagate through regions of slowed processing at the same speed as through vacuum.* This assumption requires justification.

**The effective speed of light.** In a region with $q<1$, the local effective light speed is:

$$c_{\text{eff}} = \frac{\mathfrak{l}}{\tau_{\text{eff}}} = \frac{\mathfrak{l}}{\tau_0/q} = c \cdot q$$

A signal takes $\tau_0/q$ to cross one lattice spacing $\mathfrak{l}$, so its effective speed is $c q$, not $c$. This is the speed that would be measured by a local observer using local clocks and rulers.

**The fork.** There are two consistent ways to compute the effective separation:

**Option A (use vacuum $c$):** $dR = c \cdot t_{\text{prop}} = c \cdot (\tau_0/q) = \mathfrak{l}/q$. This is the manuscript's choice. It produces spatial stretching $dR > \mathfrak{l}$ for $q<1$.

**Option B (use effective $c_{\text{eff}}$):** $dR = c_{\text{eff}} \cdot t_{\text{prop}} = (c q) \cdot (\tau_0/q) = c \tau_0 = \mathfrak{l}$. This gives **no** spatial stretching — the effective separation is exactly the lattice spacing, independent of $q$.

Both options are logically self-consistent. Option A says: "Signals always travel at vacuum $c$, so when processing is slow, they cover more effective distance." Option B says: "Signals travel at the local effective speed, which is slower in high-$q$ regions, exactly compensating the longer crossing time."

**The manuscript provides no argument for choosing Option A over Option B.** This is not a minor technical detail — it is the step that produces spatial stretching ($g_{rr} \neq 1$). Without this choice, $dR = dr$ and the spatial part of the metric is flat. The entire gravitational phenomenology (light deflection, perihelion precession, GW deviations) traces back to this unargued choice.

**Physical interpretation of the fork.** Option A treats $c$ as a global constant of nature — the speed at which information propagates along causal edges, independent of the processing state of the nodes. Option B treats $c$ as an emergent quantity that varies with the local information density. The DGF axioms specify neither. The manuscript's choice of Option A is a physical postulate, not a derivation.

**Verdict:** The step $dR = c \cdot t_{\text{prop}}$ uses the vacuum speed of light without justifying why the effective speed $c_{\text{eff}} = c q$ should not be used instead. Using $c_{\text{eff}}$ yields $dR = \mathfrak{l}$ (no spatial stretching), destroying the entire gravitational phenomenology. The choice is unargued and consequential.

---

## ATTACK 4: The Local Inertial Frame Is Presupposed, Not Derived

Step 4 of the derivation states:

> "In physical coordinates $(\tau, R, \theta, \phi)$, spacetime is Minkowski: $ds^2 = -c^2 d\tau^2 + dR^2 + R^2 d\Omega^2$."

**This is the conclusion dressed as a premise.** The claim that the local inertial frame is Minkowski is precisely the claim that the effective geometry is pseudo-Riemannian with Lorentzian signature. This is what the derivation is supposed to **produce**, not what it is allowed to **assume**.

**What Bojowald-Duque does differently.** In Bojowald-Duque, the starting point is not "spacetime is locally Minkowski." The starting point is the set of constraints on a spatial hypersurface. The algebra of these constraints either closes or it does not. If it closes, the structure functions of the algebra **determine** the spacetime metric — including whether it is Lorentzian, Euclidean, or something else. The signature is an **output** of the constraint algebra, not an input.

Specifically, in canonical gravity, the Hamiltonian constraint $H[N]$ generates time reparameterization and the diffeomorphism constraint $D[N^a]$ generates spatial diffeomorphisms. The algebra:

$$[D[M^a], D[N^b]] = D[\mathcal{L}_M N^a]$$
$$[D[M^a], H[N]] = H[\mathcal{L}_M N]$$
$$[H[M], H[N]] = D[q^{ab}(M\nabla_b N - N\nabla_b M)]$$

The inverse spatial metric $q^{ab}$ appearing in the last bracket is the **same** $q^{ab}$ that appears in the spacetime metric. The Lorentzian signature $(-,+,+,+)$ is encoded in the relative sign between the $[H,H]$ and $[D,D]$ brackets. None of this is assumed — it is computed.

**What DGF does.** DGF simply writes down the Minkowski line element in $(\tau, R)$ coordinates and declares it to be the local inertial frame. There is no derivation of the signature, no derivation of the $(-,+,+,+)$ structure, no proof that the geometry must be pseudo-Riemannian rather than, say, Finslerian or something with a preferred frame.

**The circularity.** The argument structure is:

1. We want to derive $ds^2 = -q^2 c^2 dt^2 + q^{-2} dr^2 + R^2 d\Omega^2$
2. We assume that in some coordinates $(\tau, R)$, the line element is Minkowski
3. We relate $(\tau, R)$ to $(t, r)$ via $d\tau = q\,dt$ and $dR = dr/q$
4. Substituting yields the desired metric

But step 2 **is** the assumption that the geometry is locally Minkowski with a specific relationship between the $(t,r)$ and $(\tau,R)$ coordinates. The substitution in step 4 is just coordinate algebra — it contains no physics beyond what was assumed in steps 1-3. The "derivation" is:

$$\text{Minkowski}(\tau, R) + \text{coordinate transformation}(\tau,R) \to (t,r) = \text{desired metric}$$

This is not deriving the metric from DGF axioms. This is finding a coordinate transformation that maps Minkowski space to the desired metric — which is always possible for any metric that is conformally related to Minkowski.

**What would be needed.** To match Bojowald-Duque rigor, DGF would need:
- An algebraic structure on the causal graph whose closure conditions force a specific metric
- A proof that the signature is $(-,+,+,+)$ rather than $(+,+,+,+)$ or degenerate
- An emergence of local Lorentz invariance from the discrete causal structure, not an assertion of it

**Verdict:** Step 4 presupposes the pseudo-Riemannian geometry it claims to derive. The substitution $(\tau,R) \to (t,r)$ is coordinate algebra, not physics. The step contains no derivation of Lorentzian signature or metric structure from DGF axioms.

---

## ATTACK 5: $R(r) = \int dr/q$ — The Metric Contains an Undetermined Function

The angular part of the metric is written as $R^2 d\Omega^2$, where $R(r)$ is the "physical area radius." The derivation gives only the differential relation $dR = dr/q$, from which:

$$R(r) = \int_0^r \frac{dr'}{q(r')}$$

**This is not a fully determined metric.** The function $q(r)$ is the DGF scalar field — it is the dynamical variable of the theory. The metric components $g_{tt} = -q^2 c^2$ and $g_{rr} = q^{-2}$ are expressed directly in terms of $q(r)$. But $g_{\theta\theta} = R(r)^2$ and $g_{\phi\phi} = R(r)^2 \sin^2\theta$ require an integral of $1/q$, which depends on the global profile of $q(r)$ from the origin outward.

For a spherically symmetric static configuration, the DGF metric is:

$$ds^2 = -q(r)^2 c^2 dt^2 + \frac{dr^2}{q(r)^2} + \left(\int_0^r \frac{dr'}{q(r')}\right)^2 d\Omega^2$$

**Comparison to GR.** In GR, for a static spherically symmetric vacuum solution, Birkhoff's theorem forces the metric to be Schwarzschild:

$$ds^2 = -\left(1 - \frac{2GM}{rc^2}\right)c^2 dt^2 + \left(1 - \frac{2GM}{rc^2}\right)^{-1} dr^2 + r^2 d\Omega^2$$

Here the area radius is simply $r$ — the coordinate $r$ is **defined** so that spheres have area $4\pi r^2$. The DGF metric uses $r$ as a lattice coordinate and must compute the physical area radius as a separate integral. This means:

1. **The $r$-coordinate in DGF is not the area radius.** It is a lattice index. Physical predictions (light deflection, perihelion precession, shadow size) depend on $R(r)$, not $r$, but $R(r)$ is not known until $q(r)$ is solved.
2. **The angular part introduces non-locality.** $g_{\theta\theta}$ at radius $r$ depends on the integral of $q(r')$ from $0$ to $r$ — it depends on the entire interior profile of the $q$ field, not just its local value.
3. **The metric is underdetermined until the field equation for $q(r)$ is solved.** The manuscript presents the metric as a "derivation," but without the field equation that determines $q(r)$, it is a template with an unknown function.

**The Bojowald-Duque contrast.** In Bojowald-Duque, the structure functions of the constraint algebra determine **all** metric components simultaneously. There is no undetermined integral — the effective metric is fully specified (up to the choice of quantization ambiguities, which are parameterized explicitly). DGF's metric has an integral that depends on the global solution of $q(r)$, which in turn depends on the field equation that has not been derived from the same first principles.

**Verdict:** The metric is not fully derived. It contains an undetermined function $R(r) = \int dr/q$ whose form depends on the global solution for $q(r)$. The angular components are non-local in the $q$ field, a feature absent in the Bojowald-Duque benchmark.

---

## COUP DE GRACE: $\tau_{\text{eff}}(q)$ Is a Deeper Ansatz, Not a Derivation

Having examined the five-step derivation chain and found each step to contain an unevidenced choice or an undefended assumption, we now state the structural diagnosis.

**The claim of "derivation without ansatz" is false.** What the manuscript has done is relocate the ansatz from the metric level to the processing-rate level. The old argument was:

> "Light propagation in a medium with refractive index $n(q) = 1/q$ gives the effective metric."

This was recognized as an ansatz — $n(q) = 1/q$ was acknowledged as a choice. The new argument is:

> "Information processing rate $\tau_{\text{eff}}(q) = \tau_0/q$ gives time dilation $d\tau = q\,dt$ and spatial stretching $dR = dr/q$, from which the metric follows."

But $\tau_{\text{eff}}(q) = \tau_0/q$ is the **same** functional choice as $n(q) = 1/q$ — just expressed in different variables. The ansatz has been moved one level deeper, from the emergent geometry to the underlying information dynamics. Moving an ansatz deeper does not turn it into a derivation.

**The structural asymmetry with Bojowald-Duque is fatal.** The benchmark the manuscript invokes (Bojowald-Duque, PRD 109, 084006) earns the word "derivation" because:

1. The structure functions are **computed** from constraint brackets, not chosen
2. The algebra either closes or it does not — internal consistency forces the form
3. The metric (including signature) is an **output** of the algebraic closure condition
4. Quantization ambiguities are parameterized explicitly, not hidden in unevidenced functional choices

DGF's derivation has none of these properties:
1. $\tau_{\text{eff}}(q)$ is **chosen** from an infinite family of admissible functions
2. No internal consistency condition forces the $1/q$ form — any $f(q)$ with $f(1)=1$ is equally consistent
3. The Lorentzian signature and Minkowski local frame are **inputs**, not outputs
4. The choice of vacuum $c$ over effective $c_{\text{eff}}$ is unargued

**The sensitivity analysis quantifies the problem.** Changing $\tau_{\text{eff}}(q)$ from $1/q$ to any other monotone function changes:
- The $g_{rr}$ component (from $1/q^2$ to $1/f(q)^2$)
- The 2PN deviation from GR
- The predicted gravitational wave phase shift
- The light deflection angle
- The black hole shadow size

**Every observational prediction of the theory is a function of the unevidenced choice of $f(q)$.** A theory whose predictions change qualitatively when you alter an unconstrained function at its foundation is not a derived theory — it is a parameterized framework.

**The "closure condition" is not a closure condition.** The manuscript states that "lattice update count = proper time measure" is the DGF analogue of Bojowald-Duque's constraint algebra closure. But this is a physical motivation, not a mathematical consistency condition. It does not constrain the functional form of $\tau_{\text{eff}}(q)$. It does not force a specific algebraic structure. It is a sentence, not an equation.

**The minimal fix.** To elevate the claim from "ansatz" to "derivation," the manuscript would need at minimum:

1. **A uniqueness proof for $\tau_{\text{eff}}(q) = \tau_0/q$.** Show that any other $f(q)$ leads to an internal contradiction with DGF axioms, or that the $1/q$ form is forced by an algebraic consistency condition on the causal graph.
2. **An operational definition of "update" that forces $d\tau = q\,dt$.** Specify what physical process constitutes a lattice update, and prove that the relationship between $q$ and proper time follows from that definition without additional assumptions.
3. **A justification for using vacuum $c$ rather than $c_{\text{eff}}$.** Either prove that $c$ is a global invariant of the theory (in which case $c_{\text{eff}} = cq$ is the effective speed but $c$ is the fundamental one used for distance calibration), or acknowledge that this is a postulate.
4. **A derivation of local Lorentz invariance from the causal graph structure.** Do not assume the local frame is Minkowski — prove that it must be, from the discrete causal structure of the information graph.
5. **A field equation for $q(r)$ derived from the same first principles**, so that $R(r) = \int dr/q$ becomes a computable function rather than an undetermined template.

Until these are provided, the manuscript's central claim — "this is a derivation, not an ansatz" — is unsupported. The metric remains an ansatz. It is a more deeply embedded ansatz than the refractive-index version, but it is an ansatz nonetheless.

---

## Summary Assessment

| Criterion | Bojowald-Duque (PRD 109, 084006) | DGF (this manuscript) |
|---|---|---|
| Origin of metric functions | Computed from constraint brackets | Chosen from admissible family |
| Uniqueness | Forced by algebraic closure | Not established; infinite degeneracy |
| Signature | Output of constraint algebra | Assumed as Minkowski local frame |
| Speed of light | Fundamental constant | Vacuum $c$ vs $c_{\text{eff}}$ unresolved |
| Field equation | Einstein equations from constraints | Not derived; $q(r)$ unsolved |
| Ansatz location | Quantization ambiguities (explicit) | $\tau_{\text{eff}}(q)$ functional form (implicit) |

**Recommendation:** Reject. The manuscript's central claim — that the DGF effective metric is rigorously derived rather than assumed — does not survive scrutiny. The five-step derivation chain contains unevidenced choices at every step, and the core function $\tau_{\text{eff}}(q) = \tau_0/q$ is one choice among infinitely many equally consistent alternatives. The metric is not derived; the ansatz has been moved one level deeper. This is an improvement over the refractive-index version — it locates the ansatz at a more fundamental level — but it does not constitute a derivation, and it does not approach the rigor of the Bojowald-Duque benchmark the manuscript invokes.

The manuscript could be reconsidered if the authors provide: (1) a uniqueness proof for the $1/q$ form of $\tau_{\text{eff}}(q)$, and (2) a derivation of local Lorentz invariance from the causal graph structure that does not presuppose a Minkowski local frame. Absent these, the word "derivation" should be replaced with "motivated ansatz" throughout.

---

**Confidential note to Editor:** The manuscript's claim of rigor matching Bojowald-Duque is a significant overstatement. Bojowald-Duque's constraint algebra closure is a mathematical consistency condition that forces the form of the effective metric. DGF's "closure condition" is a physical motivation, not a mathematical constraint. These are different categories of argument. Publishing this as a "derivation" would set a precedent that equates physical motivation with mathematical proof, which I believe is detrimental to the field's standards.
