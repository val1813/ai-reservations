# Referee Report — Nature Physics

**Manuscript:** "Three Whys, One Answer: Information Capacity is Bounded"
**Recommendation:** Reject (with invitation to resubmit after radical rescoping)
**Confidential to Editor:** Yes

---

## Summary of Claims

The manuscript asserts that a framework called "Discrete Graph Field" (DGF), built on three information-theoretic axioms, simultaneously answers three foundational questions:

1. **Why E = mc²?** — Claimed as a theorem-level consequence of introducing a single new dimensional constant, the information-lattice spacing 𝔩.
2. **Why does the equivalence principle hold?** — Claimed as a trivial consequence of identifying both gravitational mass and inertial mass with the same scalar, "archived information A."
3. **Why does time have a direction?** — Claimed via a "T2 theorem": a single-valued scalar q-field implies ∮dq = 0, which forces exactly one overflow direction, yielding temporal unidirectionality.

The paper packages these as "three whys, one answer: information capacity is bounded."

This reviewer has examined each claim with a fundamental-skepticism stance. The conclusions are severe. Only one of the three derivations survives scrutiny.

---

## ATTACK 1: The E = mc² "Derivation" is Dimensional Analysis in Disguise

The paper's derivation proceeds as follows:

> DGF has only one new dimensional constant — the information-lattice spacing 𝔩. From 𝔩, ℏ, c, one can construct exactly three independent scales:
> $$m_0 = \frac{\hbar}{c\mathfrak{l}}, \quad \tau_0 = \frac{\mathfrak{l}}{c}, \quad E_0 = \frac{\hbar}{\tau_0} = \frac{\hbar c}{\mathfrak{l}}$$
> From which it follows immediately that $E_0 = m_0 c^2$.

This is not a physical derivation. It is an algebraic identity dressed as one.

**The tautology is transparent.** The definition $m_0 \equiv \hbar/(c\mathfrak{l})$ *fixes* 𝔩 in terms of $m_0$. The definition $E_0 \equiv \hbar c/\mathfrak{l}$ *fixes* the energy scale. Substituting to eliminate 𝔩 yields $E_0 = m_0 c^2$ — but this is simply verifying that the two definitions are algebraically consistent. One has done nothing more than write the same dimensional relation twice with different symbols. The "derivation" contains zero physical content beyond the decision to call the combination $\hbar/(c\mathfrak{l})$ "mass" and the combination $\hbar c/\mathfrak{l}$ "energy."

**This is not unique to DGF.** Any theory that introduces a single new length scale can perform the identical maneuver. Consider:

- **Stochastic Electrodynamics (SED):** Introduce a zero-point length $\lambda_{\text{ZP}}$. Define $m_{\text{ZP}} = \hbar/(c\lambda_{\text{ZP}})$, $E_{\text{ZP}} = \hbar c/\lambda_{\text{ZP}}$. Then "derive" $E_{\text{ZP}} = m_{\text{ZP}} c^2$.
- **Loop Quantum Gravity:** Introduce the Planck-scale discreteness $\ell_P$. Define $m_P = \hbar/(c\ell_P)$, $E_P = \hbar c/\ell_P$. Then "derive" $E_P = m_P c^2$.
- **Any theory with a fundamental length 𝔩:** The same two definitions produce the same algebraic identity.

The authors have not explained why $E = mc^2$ — they have defined a mass scale and an energy scale that are dimensionally consistent with each other. This is dimensional analysis, not physics.

**The scope problem is fatal.** The paper's "derivation" applies only to the specific mass scale $m_0$ and energy scale $E_0$ defined in terms of 𝔩. But $E = mc^2$ in standard physics holds universally — for electromagnetic field energy, nuclear binding energy, kinetic energy, gravitational potential energy, and rest-mass energy of composite systems. The paper provides no mechanism by which *all* forms of energy and mass are connected by $c^2$ through the information lattice. Unless the authors claim that *all* mass and *all* energy in the universe arise from information archiving on the lattice — which would be an entirely separate, unproven, and extraordinary proposition requiring independent evidence — the "derivation" covers only the characteristic scales of the theory itself, not the universal equivalence.

**Verdict:** The claimed derivation of $E = mc^2$ is a dimensional-analysis tautology. It does not survive scrutiny.

---

## ATTACK 2: $m_{\text{grav}}$ and $m_{\text{inert}}$ Are Not Proven Identical

The paper's argument for the equivalence principle runs:

> Gravitational mass = total archived information $A$.
> Inertial mass = archived information reconfigured during acceleration, also $A$.
> Both are the same $A$. The equivalence principle follows trivially.

This is not a derivation. It is a relabeling that conceals the problem rather than solving it.

**The structural independence problem.** The paper identifies gravitational mass $m_{\text{grav}}$ with the *global* scalar $A$ — the total amount of archived information associated with an object. It then identifies inertial mass $m_{\text{inert}}$ with the *reconfiguration cost* of $A$ under acceleration — the amount of archival information that must be rewritten when the object's state changes.

The claim that these are "the same $A$" is asserted, not derived. Consider:

1. **A is a global scalar.** The total archived information $A$ of an object is a single number — a volume integral of information density. It says nothing about spatial distribution.

2. **Reconfiguration cost depends on internal structure.** The amount of information that must be rewritten during acceleration plausibly depends on *how* $A$ is distributed and organized internally — what the paper's own framework would call the causal graph structure of the archived information. A ping-pong ball and a lead sphere of equal mass have completely different internal information structures (different materials, different atomic arrangements, different numbers of degrees of freedom). Yet they have identical ratios of gravitational to inertial mass to within experimental precision ($\eta < 10^{-13}$ from MICROSCOPE).

3. **The paper never proves that reconfiguration cost is determined solely by total $A$ and independent of its internal distribution.** If inertial resistance depends on the spatial distribution of $A$ — as rotational inertia depends on the distribution of mass (moment of inertia $I = \int r^2 dm$) — then $m_{\text{inert}} \propto f(A, \text{internal structure})$ while $m_{\text{grav}} \propto \int A \, dV$. These are not automatically equal.

**The argument conflates identity of referent with identity of functional role.** That both gravitational coupling and inertial resistance "refer to" the same ontological entity $A$ does not entail that they are numerically equal in all physical circumstances. A bank account balance and a credit score both "refer to" the same person's financial state — they are not the same number.

**What would be required to make this a genuine derivation:** The paper would need to show that the equations of motion derived from DGF's causal graph dynamics yield a *single* coefficient $A$ that couples both to the gravitational field equation *and* to the inertial term in the geodesic equation, with the *same numerical value*, for *arbitrary* internal configurations of archived information. This is not done. What is done is a definitional identification followed by the assertion that the identification constitutes a derivation.

**Verdict:** The claimed derivation of the equivalence principle is a definitional relabeling. The structural independence of $m_{\text{grav}}$ and $m_{\text{inert}}$ is not addressed.

---

## ATTACK 3: The T2 Theorem Produces the Wrong Arrow

The T2 theorem is the strongest element of the paper. The mathematical structure is clean:

> The q-field is a single-valued scalar on the information graph.
> Therefore $\oint dq = 0$ on any closed loop.
> Therefore there is exactly one direction in which $dq < 0$ (information overflow).
> Therefore time has a direction.

The theorem is rigorous within its domain. The problem is that its domain is not the one the paper claims.

**The T2 theorem proves an *information-theoretic* arrow, not a *thermodynamic* arrow, not a *cosmological* arrow, and not a *perceptual* arrow.** Standard physics recognizes (at least) three distinct temporal asymmetries:

| Arrow | Origin | Status |
|-------|--------|--------|
| Thermodynamic | Second law: $\Delta S \geq 0$ | Derived from low-entropy initial conditions + dynamics |
| Cosmological | Expansion of the universe | Observed; relation to thermodynamic arrow debated |
| Perceptual/Psychological | We remember the past, not the future | Generally considered derivative of thermodynamic arrow |

The T2 theorem introduces a **fourth** arrow: an information-flow arrow ($dq < 0$ direction on the causal graph). The paper then implicitly claims that demonstrating *one* arrow suffices to "explain why time has a direction" — as if the existence of *any* arrow discharges the explanatory burden for *all* arrows.

**The alignment problem is unaddressed.** Why do all four arrows point in the same direction? The thermodynamic arrow points from low entropy to high entropy. The cosmological arrow points in the direction of cosmic expansion. The perceptual arrow points from remembered past to predicted future. The information arrow points from high-q to low-q. The probability that four independent arrows coincidentally align is far smaller than the probability that one arrow exists. The paper not only fails to explain this alignment — it fails to *notice* that alignment requires explanation.

A skeptic's formulation: the paper has found a mechanism that produces *an* arrow of time, but standard physics already has *three* arrows whose mutual alignment is the actual deep puzzle. Introducing a fourth arrow without connecting it to the existing three *deepens* the mystery rather than resolving it.

**What would be required:** The paper would need to demonstrate that the information arrow ($dq < 0$) *entails* the thermodynamic arrow ($\Delta S \geq 0$), or that the two arrows are mathematically identical within DGF, or that the cosmological arrow emerges from the same q-field dynamics. None of this is attempted.

**Verdict:** The T2 theorem is mathematically valid but physically incomplete. It produces an information-theoretic arrow while leaving the thermodynamic, cosmological, and perceptual arrows — and their mutual alignment — entirely unexplained.

---

## ATTACK 4: Narrative Overclaim — Marketing, Not Physics

The paper's title and abstract package the three results as a unified triumph:

> "Three Whys, One Answer: Information Capacity is Bounded."

This six-character slogan (in Chinese: 六个字) is rhetorically powerful. It is also physically misleading.

**The implied structure is that three independent deep puzzles are resolved by a single theoretical insight.** The reality, as established above:

- The "derivation" of $E = mc^2$ is dimensional analysis that any theory with a single new length scale can replicate. It is not a resolution of *why* mass and energy are equivalent — it is a statement that the theory's characteristic scales are dimensionally consistent.
- The "derivation" of the equivalence principle is a definitional identification that does not address the structural independence of gravitational and inertial mass.
- The derivation of the time arrow is genuine but produces the wrong arrow — an information-theoretic arrow disconnected from the thermodynamic and cosmological arrows.

**The narrative packaging — "three whys, one answer" — inflates one genuine result (the information arrow) and two compatibility statements (dimensional self-consistency, definitional consistency) into three independent derivations.** This is marketing logic, not scientific logic. A paper that honestly reported its findings would be structured very differently.

---

## FATAL BLOW: Survival Analysis

Let us assess which of the three claims would survive rigorous peer review if each were submitted independently:

| Claim | Survival Probability | Reasoning |
|-------|---------------------|-----------|
| E = mc² derived from DGF | **~0%** | Dimensional-analysis tautology. Any theory with a length scale can do this. |
| Equivalence principle derived from DGF | **~0%** | Definitional relabeling. Structural independence of $m_{\text{grav}}$ and $m_{\text{inert}}$ is not proved. |
| Time arrow from T2 theorem | **~40-60%** | The theorem is rigorous. It genuinely produces an information-theoretic arrow. The limitation is scope (wrong arrow) and the unaddressed alignment problem — but these are fixable with further work connecting the information arrow to thermodynamic entropy. |

**Net assessment:** At most one of three claims survives. The honest presentation would be:

> "DGF rigorously derives an information-theoretic arrow of time (theorem-level result). DGF is dimensionally compatible with $E = mc^2$ (the theory's characteristic scales satisfy the relation, but this is dimensional consistency, not a derivation of universal mass-energy equivalence). DGF is definitionally compatible with the equivalence principle (both gravitational and inertial mass can be *defined* in terms of archived information $A$, but their numerical equality across diverse internal structures is not derived)."

This is a significantly more modest paper — but it is an *honest* paper.

---

## Recommendation

**Reject.** The manuscript claims three theorem-level derivations of foundational results. One is a tautology, one is a relabeling, and one is genuine but scope-limited. The narrative packaging inflates these into a unified resolution of three "deep whys" that the paper does not deliver.

**However**, the T2 theorem on the information-theoretic arrow of time is mathematically interesting and may merit publication if:

1. The scope is honestly stated (information-theoretic arrow, not "time has a direction" simpliciter).
2. The alignment problem with thermodynamic/cosmological/perceptual arrows is at minimum acknowledged as an open problem, and ideally addressed.
3. The claims regarding $E = mc^2$ and the equivalence principle are downgraded from "derivations" to "dimensional consistency" and "definitional compatibility" respectively.
4. The "three whys, one answer" framing is abandoned in favor of an accurate description of what was actually achieved.

**I would be willing to re-review a radically rescoped manuscript that follows these guidelines.** The information-theoretic arrow result deserves a venue. The other two claims, in their current form, do not.

---

## Questions for Author Rebuttal (if the editor permits revision)

1. Demonstrate that $E = mc^2$ in DGF applies to electromagnetic field energy, not just to the characteristic mass scale $m_0$. If it does not, state this limitation explicitly.

2. Prove that $m_{\text{inert}} = m_{\text{grav}}$ in DGF for two objects with identical total archived information $A$ but maximally different internal causal-graph structures. If this cannot be proved, acknowledge that the equivalence principle is a definitional input to DGF, not a derivational output.

3. Derive the thermodynamic arrow ($\Delta S \geq 0$) from the T2 arrow ($dq < 0$). If this cannot be done, explain why the information arrow and the thermodynamic arrow coincide in our universe — and under what conditions they could point in opposite directions.

4. State clearly: which of the three "whys" does DGF *derive* (theorem-level, from axioms alone), and which does DGF merely *accommodate* (consistent with, but not uniquely implied by)?

---

**Referee 3**
*Anonymous*
*Nature Physics*
