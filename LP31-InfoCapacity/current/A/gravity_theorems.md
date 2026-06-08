# Theorem 11 & 12: Gravitational Origin from DGF Information Dynamics

**Author: A (Mathematical Physics)**
**Date: 2026-06-06**
**Target quality: BM Sections IV-V — clean derivation chain, explicit equation correspondence, complete spherical solution**

---

## Preliminaries: The Continuum q-Field

From the continuum limit of DGF (see `continuum_qfield.md`), the q-field obeys:

$$\boxed{\partial_t q = D_0 \nabla^2\!\left(\frac{1}{q}\right)} \tag{P}$$

with $D_0 = a^2/\tau_0 = a \cdot c$ where $a$ is the lattice spacing, $\tau_0 = a/c$ is the cell time, and $c$ is the information propagation speed upper bound. Equivalent forms:

$$\partial_t q = D_0 \nabla\cdot\!\left(\frac{1}{q^2}\nabla q\right) \tag{P'}$$

with effective diffusivity $D(q) = D_0/q^2$.

**Established properties** (from `continuum_qfield.md`):
- $F_1[q] = \int q^{-1} d^dx$ is a Lyapunov functional (monotonic decreasing) — Theorem 3
- $D(q) \to \infty$ as $q \to 0$ — Theorem 6
- $q=0$ is a singular boundary with divergent information flux — Theorem 7

---

## Theorem 11: Static Limit and Gravitational Potential Correspondence

### 11.1 Statement

> **Theorem 11 (Static-Gravity Correspondence).** In the static limit $\partial_t q = 0$, the DGF field $u \equiv 1/q$ satisfies the Laplace equation $\nabla^2 u = 0$. This is mathematically isomorphic to the vacuum Einstein equation in the Newtonian limit $\nabla^2 \Phi = 0$, where $\Phi$ is the gravitational potential. With source terms (spatial regions where information is locked in occupied cells), the field obeys $\nabla^2 u = -\kappa \rho_m$, where $\rho_m$ is the mass density and $\kappa$ is a coupling constant — structurally identical to the Poisson equation $\nabla^2 \Phi = 4\pi G \rho$.

### 11.2 Proof

#### 11.2.1 Vacuum case: $\partial_t q = 0 \Rightarrow \nabla^2(1/q) = 0$

From the q-field equation (P):

$$\partial_t q = D_0 \nabla^2\!\left(\frac{1}{q}\right)$$

Set $\partial_t q = 0$ (static limit). Since $D_0 = a \cdot c > 0$ (finite lattice spacing, finite propagation speed), we have:

$$\boxed{\nabla^2\!\left(\frac{1}{q}\right) = 0} \tag{11.1}$$

Define the **information potential**:

$$u(\mathbf{x}) \equiv \frac{1}{q(\mathbf{x})} \in [1, \infty)$$

Then:

$$\boxed{\nabla^2 u = 0} \tag{11.2}$$

This is the Laplace equation — one of the most fundamental equations in mathematical physics.

**Properties of solutions:**
1. $u$ is harmonic: its value at any point equals the average of its values on any sphere centered at that point (mean value property)
2. Solutions are uniquely determined by boundary conditions (Dirichlet: $u|_{\partial\Omega}$ specified; or Neumann: $\partial_n u|_{\partial\Omega}$ specified)
3. $u$ is $C^\infty$ (analytic) in any region where it is harmonic
4. Maximum principle: $u$ attains its maximum and minimum on the boundary, not in the interior

**Boundary condition at infinity.** For an isolated system, we impose:

$$\lim_{|\mathbf{x}| \to \infty} q(\mathbf{x}) = 1$$

(infinitely far from any mass, all cells are vacant — pure quantum vacuum). Equivalently:

$$\lim_{|\mathbf{x}| \to \infty} u(\mathbf{x}) = 1 \tag{11.3}$$

This is the **asymptotic flatness** condition for the information potential.

#### 11.2.2 Newtonian gravity correspondence

In Newtonian gravity, the gravitational potential $\Phi(\mathbf{x})$ satisfies the Poisson equation:

$$\nabla^2 \Phi = 4\pi G \rho(\mathbf{x})$$

where $\rho(\mathbf{x})$ is the mass density and $G$ is Newton's constant. In vacuum ($\rho = 0$):

$$\nabla^2 \Phi = 0 \tag{11.4}$$

Equations (11.2) and (11.4) are **identical in structure**: both are Laplace equations. The information potential $u = 1/q$ and the Newtonian gravitational potential $\Phi$ satisfy the same PDE in vacuum.

#### 11.2.3 Sourced case: $\nabla^2 u = -\kappa \rho_m$

The Laplace equation describes the field in vacuum. What is the source term when mass is present?

**Definition (Information mass density).** In the DGF, a cell occupied by information ($s_i = 1$) carries exactly 1 bit of locked information (ln 2 in natural units). The **locked information fraction** at position $\mathbf{x}$ is:

$$A(\mathbf{x}) \equiv 1 - q(\mathbf{x}) \in [0, 1]$$

The **information mass density** (bits per unit volume) is:

$$\rho_I(\mathbf{x}) \equiv \frac{A(\mathbf{x})}{a^3} \cdot \ln 2 = \frac{(1 - q(\mathbf{x})) \ln 2}{a^3} \tag{11.5}$$

where $a^3$ is the physical volume per cell. The conventional mass density is:

$$\rho_m(\mathbf{x}) = \eta \cdot \rho_I(\mathbf{x}) = \eta \frac{(1 - q(\mathbf{x})) \ln 2}{a^3} \tag{11.6}$$

where $\eta$ is the **mass-information conversion factor** with units [kg/bit]. This factor is not derived within DGF; it is an external calibration constant (see Caveat 11.C1).

**Poisson-type equation.** From the static limit of (P) with sources, the general form is:

$$\boxed{\nabla^2 u = -\kappa \rho_m} \tag{11.7}$$

where $\kappa$ is the coupling constant. To determine the structure of $\kappa$, compare with the Newtonian Poisson equation:

$$\nabla^2 \Phi = 4\pi G \rho \tag{11.8}$$

From the identification $u \leftrightarrow -\Phi$ (up to an additive constant) — see Theorem 12 for the explicit correspondence — we obtain:

$$\kappa \equiv \frac{4\pi G}{c^2}$$

The factor $c^{-2}$ arises because $\Phi/c^2$ is dimensionless (as is $1/q$), while $\Phi$ has dimensions of [velocity]². Explicitly, from $u = 1 - \Phi/c^2$ (Theorem 12):

$$\nabla^2 u = -\frac{1}{c^2}\nabla^2 \Phi = -\frac{4\pi G}{c^2}\rho$$

confirming $\kappa = 4\pi G/c^2$.

**Important qualification.** The derivation of (11.7) from (P) with sources is at the level of **structural correspondence**, not first-principles deduction. The Poisson equation emerges from the q-field framework when:
1. The static limit is taken
2. Mass is identified with locked information via (11.6)
3. The coupling constant is calibrated to match Newtonian gravity

The Laplace equation ($\nabla^2 u = 0$ in vacuum), however, is a **deduction** from (P) — requiring only $\partial_t q = 0$.

### 11.3 Physical Interpretation

**Information potential as gravitational potential.** The quantity $u = 1/q$ acts as a scalar potential whose gradient drives information flow in the dynamic regime and whose Laplacian encodes mass distribution in the static regime.

| $u = 1/q$ | $\Phi$ (gravitational potential) |
|-----------|----------------------------------|
| Harmonic in vacuum: $\nabla^2 u = 0$ | Harmonic in vacuum: $\nabla^2 \Phi = 0$ |
| Source = locked information: $\nabla^2 u = -\kappa \rho_m$ | Source = mass density: $\nabla^2 \Phi = 4\pi G \rho$ |
| $u = 1$ at spatial infinity | $\Phi = 0$ at spatial infinity (gauge) |
| $u \to \infty$ at $q \to 0$ (capacity exhausted) | $\Phi \to -\infty$ at a point mass (Newtonian singularity) |

**Three regimes:**
1. **Uniform q-field** ($1/q = \text{const}$): No "gravitational" effect — flat spacetime analog
2. **Nonzero $\nabla^2(1/q)$**: "Sources" present — mass density corresponding to spatial inhomogeneity of q
3. **Spatial variation of $1/q$ without sources**: Tidal-like effects in vacuum — curvature without matter (analogous to vacuum GR solutions)

**The "source" is locked information, not active signaling.** A mass does not "send gravitational signals" — the static configuration of the q-field around the mass *is* the gravitational field. The mass (a region where $q \approx 0$) imposes a boundary condition on the q-field, and the Laplace/Poisson equation determines the field everywhere else. Gravity is the **shadow** of information capacity exhaustion in space.

### 11.4 Caveats for Theorem 11

**11.C1: $\kappa$ is not derived.** The coupling constant $\kappa = 4\pi G/c^2$ requires the Newton constant $G$, which DGF does not predict. $G$ is a **Level 4 (accidental) parameter** in the DGF ontology — it must be measured, just as it must be measured in standard physics. What DGF provides is the *structure* of the field equation (Laplace/Poisson type), not the numerical value of the coupling.

**11.C2: The mass-information identification (11.6) is a postulate.** $m \propto (\text{number of occupied cells})$ is a bridge assumption connecting DGF's information-theoretic variables to physical observables. The proportionality constant $\eta$ [kg/bit] is not derived.

**11.C3: Static limit existence.** The static limit $\partial_t q = 0$ requires that the system admits stationary solutions of (P). As noted in `continuum_qfield.md` Theorem 6(c), no classical stationary solution exists that attains $q=0$ at an interior point — the static solutions are valid only in regions where $q > 0$. The $q=0$ "core" of a mass requires a separate treatment (see Theorem 12 discussion of the Schwarzschild radius).

**11.C4: The Laplacian is flat-space.** Equation (11.2) uses the Euclidean Laplacian $\nabla^2 = \delta^{ij}\partial_i\partial_j$. In general relativity, the Laplacian is replaced by the covariant d'Alembertian on a curved background. DGF, in its current form, does not dynamically generate spacetime curvature — the Laplacian structure is inherited from the flat lattice $\Lambda_N \subset \mathbb{Z}^d$. This is a limitation of the current framework (see Caveat 12.C4).

---

## Theorem 12: Spherically Symmetric Weak-Field Solution

### 12.1 Statement

> **Theorem 12 (Spherical Weak-Field Solution).** For a spherically symmetric, static mass distribution of total mass $M$ in $d=3$ spatial dimensions, the DGF $q$-field in the exterior vacuum region satisfies:
>
> $$\boxed{\frac{1}{q(r)} = 1 + \frac{GM}{rc^2}} \quad (r \gg r_s) \tag{12.1}$$
>
> where $r_s = 2GM/c^2$ is the Schwarzschild radius. This is the **Newtonian correspondence**: the DGF information potential $u = 1/q$ maps to the Newtonian gravitational potential via $u = 1 - \Phi/c^2$, where $\Phi(r) = -GM/r$.

### 12.2 Derivation

#### 12.2.1 Spherical symmetry ansatz

Assume the field depends only on the radial coordinate: $q = q(r)$, $r = |\mathbf{x}|$. The Laplace operator in spherical coordinates for a function of $r$ alone:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial}{\partial r}\right) \tag{12.2}$$

#### 12.2.2 Exterior vacuum equation

In the exterior region (outside the mass distribution), $\rho_m = 0$. From Theorem 11, the static equation is $\nabla^2(1/q) = 0$:

$$\frac{1}{r^2}\frac{d}{dr}\!\left(r^2 \frac{d}{dr}\frac{1}{q}\right) = 0 \tag{12.3}$$

#### 12.2.3 First integration

Multiply by $r^2$:

$$\frac{d}{dr}\!\left(r^2 \frac{d}{dr}\frac{1}{q}\right) = 0$$

Integrate:

$$r^2 \frac{d}{dr}\frac{1}{q} = C_1 = \text{const} \tag{12.4}$$

The constant $C_1$ is proportional to the total "charge" (mass) enclosed — this is the information-theoretic analog of Gauss's law.

**Physical interpretation of $C_1$.** By Gauss's theorem applied to $\nabla^2 u = -\kappa \rho_m$:

$$\oint_{S^2} \nabla u \cdot d\mathbf{S} = \int_V \nabla^2 u \, dV = -\kappa \int_V \rho_m \, dV = -\kappa M$$

The left-hand side:

$$\oint_{S^2} \frac{du}{dr} \hat{\mathbf{r}} \cdot \hat{\mathbf{r}} \, r^2 d\Omega = \frac{du}{dr} \cdot 4\pi r^2$$

From (12.4), $du/dr = C_1/r^2$, so:

$$\frac{C_1}{r^2} \cdot 4\pi r^2 = 4\pi C_1 = -\kappa M$$

Therefore:

$$C_1 = -\frac{\kappa M}{4\pi} \tag{12.5}$$

#### 12.2.4 Second integration

From (12.4) and (12.5):

$$\frac{d}{dr}\frac{1}{q} = -\frac{\kappa M}{4\pi r^2}$$

Integrate:

$$\frac{1}{q(r)} = \frac{\kappa M}{4\pi r} + C_2 \tag{12.6}$$

#### 12.2.5 Boundary condition at infinity

As $r \to \infty$, the influence of the mass vanishes: $q \to 1$, $1/q \to 1$. Therefore:

$$C_2 = 1$$

$$\frac{1}{q(r)} = 1 + \frac{\kappa M}{4\pi r} \tag{12.7}$$

#### 12.2.6 Newtonian calibration of $\kappa$

The Newtonian gravitational potential for a point mass is:

$$\Phi(r) = -\frac{GM}{r}$$

For the DGF result (12.7) to reproduce Newtonian gravity in the correspondence $u = 1/q = 1 - \Phi/c^2$:

$$1 + \frac{\kappa M}{4\pi r} = 1 - \frac{1}{c^2}\!\left(-\frac{GM}{r}\right) = 1 + \frac{GM}{rc^2}$$

$$\Rightarrow \frac{\kappa}{4\pi} = \frac{G}{c^2} \quad \Rightarrow \quad \kappa = \frac{4\pi G}{c^2} \tag{12.8}$$

Thus:

$$\boxed{\frac{1}{q(r)} = 1 + \frac{GM}{rc^2}} \tag{12.9}$$

This is the **weak-field DGF solution** — valid for $r \gg r_s = 2GM/c^2$, where $q \approx 1$ and the linear approximation holds.

#### 12.2.7 Explicit Newtonian correspondence

The identification is:

$$\boxed{\frac{1}{q(\mathbf{x})} = 1 - \frac{\Phi(\mathbf{x})}{c^2}} \tag{12.10}$$

or equivalently:

$$q(\mathbf{x}) = \frac{1}{1 - \Phi(\mathbf{x})/c^2} \approx 1 + \frac{\Phi(\mathbf{x})}{c^2} + \mathcal{O}\!\left(\frac{\Phi^2}{c^4}\right) \tag{12.11}$$

where the expansion is valid in the weak-field regime $|\Phi|/c^2 \ll 1$.

**Table: Newtonian-DGF dictionary**

| Newtonian gravity | DGF q-field | Relationship |
|-------------------|-------------|--------------|
| $\Phi(\mathbf{x})$ | $u(\mathbf{x}) = 1/q(\mathbf{x})$ | $u = 1 - \Phi/c^2$ |
| $\nabla^2 \Phi = 4\pi G\rho$ | $\nabla^2 u = -\kappa \rho_m$ | $\kappa = 4\pi G/c^2$ |
| $\mathbf{g} = -\nabla\Phi$ | $-\nabla u = \nabla(1/q)$ | $\mathbf{g} = c^2 \nabla u$ |
| $\oint \mathbf{g} \cdot d\mathbf{S} = -4\pi GM$ | $\oint \nabla u \cdot d\mathbf{S} = -\kappa M$ | Gauss laws match |

### 12.3 Physical Verification: Earth

**Numerical test.** For Earth:
- $M_\oplus \approx 5.97 \times 10^{24}$ kg
- $R_\oplus \approx 6.37 \times 10^6$ m
- $G = 6.67 \times 10^{-11}$ m³ kg⁻¹ s⁻²
- $c = 3.00 \times 10^8$ m/s

$$\frac{GM_\oplus}{R_\oplus c^2} = \frac{(6.67 \times 10^{-11})(5.97 \times 10^{24})}{(6.37 \times 10^6)(3.00 \times 10^8)^2} = \frac{3.98 \times 10^{14}}{5.73 \times 10^{23}} = 6.95 \times 10^{-10}$$

$$\frac{1}{q(R_\oplus)} = 1 + 6.95 \times 10^{-10}$$

$$q(R_\oplus) = \frac{1}{1 + 6.95 \times 10^{-10}} \approx 1 - 6.95 \times 10^{-10} = 0.999999999305$$

**What this means.** At Earth's surface, the vacant fraction differs from the pure vacuum value $q=1$ by less than one part in $10^9$. Earth is an **extraordinarily quantum object** in the DGF sense — less than $10^{-7}$% of its cells are occupied. Yet this tiny deviation, when amplified by the $D(q) = D_0/q^2$ diffusivity and integrated over Earth's volume, produces the gravitational acceleration $g = 9.8$ m/s² that we experience daily.

**Scale comparison:**

| System | $M$ [kg] | $R$ [m] | $GM/Rc^2$ | $q$ at surface |
|--------|----------|---------|-----------|----------------|
| Proton | $1.67\times 10^{-27}$ | $8.4\times 10^{-16}$ | $1.5\times 10^{-39}$ | $\approx 1 - 10^{-39}$ |
| Human | $70$ | $0.5$ | $1.0\times 10^{-25}$ | $\approx 1 - 10^{-25}$ |
| Earth | $5.97\times 10^{24}$ | $6.37\times 10^6$ | $7.0\times 10^{-10}$ | $0.9999999993$ |
| Sun | $1.99\times 10^{30}$ | $6.96\times 10^8$ | $2.1\times 10^{-6}$ | $0.9999979$ |
| White dwarf | $1.4 M_\odot$ | $6\times 10^6$ | $3.4\times 10^{-4}$ | $0.99966$ |
| Neutron star | $1.4 M_\odot$ | $10^4$ | $0.21$ | $0.83$ |
| Black hole | $10 M_\odot$ | $3\times 10^4$ (at $r_s$) | $0.5$ (at $r_s$) | $2/3 \to 0$ |

The progression is clear: as compactness $GM/Rc^2$ approaches $\sim 1$, $q$ deviates significantly from 1, and the weak-field approximation breaks down. Neutron stars enter the strong-field regime; black holes represent $q \to 0$ at the horizon.

### 12.4 Alternative Derivation: Direct Mass-Information Integral

An alternative route to (12.9) that explicitly shows the role of locked information:

**Mass from locked information.** The total mass is:

$$M = \eta \int_V \rho_I(\mathbf{x}) \, d^3x = \eta \frac{\ln 2}{a^3} \int_V (1 - q(\mathbf{x})) \, d^3x \tag{12.12}$$

For the weak-field exterior solution $1/q = 1 + \alpha/r$ with $\alpha \ll r$, we have:

$$1 - q = 1 - \frac{1}{1 + \alpha/r} = \frac{\alpha/r}{1 + \alpha/r} \approx \frac{\alpha}{r} \quad (r \gg \alpha) \tag{12.13}$$

The total locked information integral:

$$I_{\text{locked}} \equiv \int_{r_s}^\infty (1 - q(r)) \cdot 4\pi r^2 dr \approx 4\pi\alpha \int_{r_s}^R r\,dr = 2\pi\alpha(R^2 - r_s^2) \tag{12.14}$$

This integral **diverges** as $R \to \infty$ (linearly with area), reflecting the long-range nature of gravity. The physical interpretation is that the gravitational "charge" (locked information) is distributed throughout space as the q-field gradient, not localized at the source. The divergence is cut off physically by the finite size of the universe or by embedding the system in a cosmological background (see Caveat 12.C3).

**Connection to $\alpha$.** Matching (12.12) with (12.14) is subtle because (12.14) is a UV-divergent quantity in the continuum. The correct matching uses **Gauss's law** (as in 12.2.6), which localizes the mass to the flux integral, avoiding the divergence:

$$M \propto \oint_{S^2_\infty} \nabla u \cdot d\mathbf{S} = 4\pi\alpha$$

up to the conversion factor, yielding $\alpha = GM/c^2$ as before.

### 12.5 Physical Meaning: How Mass "Causes" Gravity in DGF

The DGF picture of gravity is qualitatively distinct from both the Newtonian "action at a distance" and the Einsteinian "curved spacetime" pictures:

1. **Mass is a region of low $q$.** A material body consists of a large number of occupied cells ($s_i = 1$). These cells have exhausted their information capacity. In the continuum description, the body's interior has $q(\mathbf{x}) < 1$, approaching $q \approx 0$ for sufficiently compact objects.

2. **The q-field relaxes to a static configuration.** In dynamic equilibrium, the information flux $-\nabla(1/q)$ balances the tendency of information to spread (entropic preference for $q = 1/2$, Theorem 8). The static configuration is determined by $\nabla^2(1/q) = 0$ in vacuum.

3. **The spatial variation of $1/q$ IS the gravitational field.** There is no separate "gravitational field" over and above the q-field. The gradient $\nabla(1/q)$ is what we measure as gravitational acceleration:
   $$\mathbf{g} = -c^2 \nabla u = -c^2 \nabla\!\left(\frac{1}{q}\right) \tag{12.15}$$

4. **The $1/r$ decay is a consequence of 3D space.** In $d$ spatial dimensions, the Laplace equation Green's function decays as $r^{-(d-2)}$ (for $d \geq 3$) or $\log r$ (for $d = 2$). The $1/r$ gravitational potential arises because we live in $d = 3$ spatial dimensions — it is a geometric fact about the Laplace equation, not a separate postulate about gravity.

5. **Gravity is not a "force" — it is an information gradient.** Test particles move not because mass "pulls" them, but because the local q-field configuration makes it statistically overwhelmingly likely for them to move toward regions of lower $q$ (higher occupation). This is the information-theoretic analog of the geodesic principle.

---

## Honest Caveats: What Theorem 11-12 Do and Do Not Establish

### What IS Derived (Logical Consequences of DGF + Continuum Limit)

| Claim | Status | Derivation Chain |
|-------|--------|------------------|
| Static limit of (P) yields Laplace equation $\nabla^2(1/q) = 0$ | **Deduced** | (P) + $\partial_t q = 0$ → $\nabla^2(1/q) = 0$ |
| Spherical exterior solution: $1/q = 1 + \alpha/r$ | **Deduced** | Spherical symmetry + Laplace equation + boundary condition $q(\infty) = 1$ |
| $1/r$ decay of gravitational "potential" | **Deduced** | Consequence of Laplace equation in $d=3$ |
| Gauss's law structure: flux $\propto$ enclosed "charge" | **Deduced** | Divergence theorem applied to $\nabla^2 u = -4\pi G\rho/c^2$ |
| Structural identity with Newtonian gravity's PDE | **Deduced** | Both are Laplace/Poisson-type |

### What is NOT Derived (External Inputs)

| Ingredient | Status | Why Not Derived |
|------------|--------|-----------------|
| Numerical value of $G$ | **Input** | $G$ is Level 4 (accidental) — like particle masses in the Standard Model |
| $\kappa = 4\pi G/c^2$ | **Calibrated** | The form $\nabla^2 u = -\kappa\rho_m$ is derived; the value of $\kappa$ is set by matching to experiment |
| $\rho_m = \eta \rho_I$ (mass = information × conversion) | **Postulated** | The proportionality of mass to locked information is a bridge postulate; $\eta$ [kg/bit] is not derived |
| $D_0 = a \cdot c$: the identification of lattice speed with $c$ | **Assumed** | $c$ enters as the information propagation speed bound; its identification with the speed of light is a physical postulate |
| $d=3$ | **Input** | DGF does not predict spatial dimensionality |
| Gravitational waves (time-dependent solutions) | **Not addressed** | Equation (P) is parabolic (diffusion-type), not hyperbolic (wave-type). Gravitational waves require an extension of DGF to a hyperbolic field equation |

### Critical Limitations

**12.C1: Propagation speed — the parabolic problem.** The q-field equation $\partial_t q = D_0 \nabla^2(1/q)$ is **parabolic**, implying infinite propagation speed for disturbances. Physical gravity propagates at finite speed $c$ (confirmed by GW170817). This is the single most serious mismatch between the current DGF and gravitational physics.

*Mitigation pathway.* The infinite propagation speed is a continuum artifact analogous to the infinite propagation speed of the non-relativistic heat equation and the non-relativistic Schrödinger equation. A relativistic extension would require either:
- A hyperbolic reformulation: $\partial_t^2 q + \gamma \partial_t q = D_0 \nabla^2(1/q)$ (telegrapher's equation with finite propagation speed)
- A full information-spacetime correspondence where the "lattice" itself is dynamical, producing effective light cones

Neither exists in the current DGF. This is the most important open problem for the gravity connection.

**12.C2: Strong-field regime ($q \to 0$).** The weak-field solution $1/q = 1 + GM/rc^2$ is an **expansion valid for $r \gg GM/c^2$**. At the Schwarzschild radius $r_s = 2GM/c^2$, the weak-field expression gives:

$$\frac{1}{q(r_s)} = 1 + \frac{GM}{r_s c^2} = 1 + \frac{GM}{2GM/c^2 \cdot c^2} = 1 + \frac{1}{2} = \frac{3}{2}$$

$$q(r_s) = \frac{2}{3}$$

This means: **in the weak-field approximation, $q$ at the horizon is $2/3$, not $0$**. The actual condition $q(r_s) = 0$ requires the full nonlinear equation. The approach to $q=0$ at the horizon is a strong-field effect not captured by the linear Laplace equation.

The full nonlinear static equation from (P) with $\partial_t q = 0$ is:

$$\nabla^2\!\left(\frac{1}{q}\right) = 0 \quad \text{(exact, no approximation)}$$

The exact spherical solution that satisfies $q \to 0$ at $r = r_s$ and $q \to 1$ as $r \to \infty$ is:

$$\frac{1}{q(r)} = \frac{r}{r - r_s} \quad \text{(conjectured exact strong-field solution)}$$

This gives the correct weak-field expansion:

$$\frac{1}{q} = 1 + \frac{r_s}{r} + \frac{r_s^2}{r^2} + \cdots = 1 + \frac{2GM}{rc^2} + \mathcal{O}\!\left(\frac{G^2 M^2}{r^2 c^4}\right)$$

Note the factor of 2 difference from the Newtonian correspondence ($GM/rc^2$ vs. $2GM/rc^2$). This factor of 2 is **exactly** the difference between the Newtonian deflection angle and the GR deflection angle of light — a famous test of GR. Whether the DGF full solution reproduces this factor of 2, and whether it matches the GR Schwarzschild metric's $1 - r_s/r$ structure, requires solving the full nonlinear static equation — which is currently **conjectured but not proved**.

**12.C3: The divergent mass integral.** The integral $\int (1-q) dV$ for the $1/r$ exterior solution diverges as $R^2$ (see equation 12.14). This is a well-known feature of long-range fields — the "total energy" of the Coulomb field or the Newtonian gravitational field diverges similarly. In DGF, this reflects the fact that the q-field gradient extends to infinity. Physical regularization requires:
- Embedding the system in a cosmological background with finite total mass
- Or treating the integral as a renormalized quantity (subtracting the vacuum $q=1$ contribution)

This is not a fatal flaw but a standard feature of massless field theories. The physical mass $M$ is defined via the Gauss flux (12.15), not via the divergent volume integral.

**12.C4: No spacetime curvature.** DGF, in its current lattice formulation, lives on a fixed flat background $\mathbb{Z}^d$. There is no mechanism for the q-field to "curve" the lattice itself. The correspondence $u \leftrightarrow \Phi$ is at the level of the Newtonian limit only. Full general relativity — with its metric $g_{\mu\nu}$, geodesic equation, and Einstein field equations — is not contained in the current DGF. The claim is limited to: **the structure of the Newtonian gravitational field equation emerges from DGF in the static, weak-field limit**.

**12.C5: The Equivalence Principle is not addressed.** The DGF derivation says nothing about whether gravitational mass equals inertial mass, or whether all objects fall with the same acceleration. These are additional inputs (or additional tests) for any theory claiming a gravitational connection.

### Summary: Claim Calibration

| Claim Level | Statement |
|-------------|-----------|
| **Proved** | $\partial_t q = 0 \Rightarrow \nabla^2(1/q) = 0$ (vacuum Laplace equation) |
| **Proved** | Spherical exterior solution: $1/q = 1 + \alpha/r$ |
| **Derived (structure only)** | Poisson-type equation $\nabla^2(1/q) = -\kappa \rho_m$ — the *form* is derived; $\kappa$ is calibrated |
| **Correspondence** | $1/q = 1 - \Phi/c^2$ — a dictionary mapping between DGF and Newtonian variables |
| **Not derived** | $G$, $\eta$, finite propagation speed, spacetime curvature, strong-field solution, gravitational waves |

---

## Comparison with Barbour-Magueijo (BM)

### BM Framework (Recap)

Barbour and Magueijo's approach (e.g., `arXiv:1503.08043` and related works on unimodular gravity and shape dynamics):

1. **Foundation:** Relational dynamics on shape space. The universe is described entirely by ratios of distances; absolute scale is meaningless.
2. **Gravity:** Emerges from *unimodular gravity* — general relativity with the constraint $\det g = -1$ (fixed spacetime volume element). The cosmological constant appears as a constant of integration, not a fundamental parameter.
3. **Method:** Variational principles (Best Matching) + symmetry (spatial diffeomorphisms + volume-preserving conformal transformations).
4. **Key insight:** Time and scale emerge from the relational structure — the "arrow of time" is tied to the expansion of the universe.

### Comparison Table

| Dimension | BM | DGF (Theorem 11-12) |
|-----------|-----|---------------------|
| **Starting point** | Relational configuration space (shapes) | Information capacity $X = \{0,1\}^N$ |
| **Fundamental entity** | Ratios of distances | Cell occupancy $s_i \in \{0,1\}$ |
| **Gravity equation** | $\nabla^2 \Phi = 4\pi G\rho$ *input* via Einstein | $\nabla^2(1/q) = 0$ *derived* from static limit |
| **$G$ status** | Input (or derived from cosmological constant?) | Input (Level 4 accidental) |
| **$1/r$ potential** | Input (Green's function of Laplacian in 3D) | Derived (spherical solution of $\nabla^2(1/q) = 0$) |
| **Spacetime** | Dynamical (relational 3-geometries) | Fixed flat background (limitation) |
| **Strong field** | Full GR (Schwarzschild, cosmology) | Not yet developed |
| **Cosmology** | $\Lambda$ as integration constant | Not yet developed |
| **Arrow of time** | Expansion-driven | Entropy-driven (Theorem 2: coarse-grained entropy increase) |
| **Mathematical depth** | Very high (differential geometry, fiber bundles) | Moderate (PDE theory, information theory) |
| **Number of assumptions** | Many (Best Matching, conformal symmetry, ...) | Few (A1: distinguishability, A2: finite capacity) |
| **Tesability** | Cosmological (difficult) | Mesoscopic (circuit QED, information flow) |

### What DGF Does Better (Arguably)

1. **Fewer assumptions.** DGF starts from two axioms (A1: distinguishability, A2: bounded capacity) that are definitional to any finite information system. BM requires Best Matching, spatial relationalism, and unimodularity — each a substantive physical postulate.

2. **Laplace equation is derived, not input.** BM takes the Einstein equations (hence the Poisson equation) as a starting point. DGF derives $\nabla^2(1/q) = 0$ from the static limit of the q-field PDE, which in turn derives from the discrete flux ansatz. The *structure* of the vacuum gravitational field equation is a theorem, not an axiom.

3. **Direct connection to statistical mechanics.** DGF's gravitational field emerges from the same q-field that governs thermodynamic behavior (Theorems 1-3). Gravity and thermodynamics are unified in a single field — not separate domains.

### What BM Does Better (Definitively)

1. **Full GR limit.** BM can reproduce the Einstein equations in the appropriate limit, including the Schwarzschild and Friedmann solutions. DGF currently has only the Newtonian weak-field correspondence.

2. **Spacetime is dynamical.** BM's shape dynamics provides a framework where spacetime geometry is not fixed — it is the evolving relational configuration. DGF's fixed lattice is a serious limitation for gravitational physics.

3. **Cosmological constant.** BM's $\Lambda$ as an integration constant is an elegant result. DGF has no cosmological extension.

4. **Maturity.** BM is a developed research program with decades of work. DGF's gravity connection is new (Theorems 11-12).

### Complementary Strengths

The two frameworks are potentially **complementary** rather than competitive:

- **BM provides the "how"**: a rigorous mathematical machine for relational dynamics, shape space, and emergent spacetime.
- **DGF provides the "why"**: an information-theoretic origin story for why gravitational equations have the structure they do.

A synthesis might work as follows:
1. DGF explains *why* the Poisson/Laplace structure appears (information capacity exhaustion)
2. BM explains *how* this structure is embedded in a full dynamical spacetime (shape dynamics)
3. Together they might yield a theory where gravity = information geometry of configuration space

This synthesis is speculative and far beyond the scope of Theorems 11-12.

---

## Appendix A: Gauss's Law in the DGF Context

### A.1 Integral Form

From the Poisson-type equation $\nabla^2 u = -\kappa \rho_m$:

$$\oint_{\partial V} \nabla u \cdot d\mathbf{S} = -\kappa \int_V \rho_m \, dV = -\kappa M_{\text{enc}} \tag{A.1}$$

For the spherical solution $u = 1 + \alpha/r$, the left-hand side is:

$$\oint_{S^2} \left(-\frac{\alpha}{r^2}\right) r^2 d\Omega = -4\pi\alpha$$

Hence $\alpha = \kappa M/(4\pi)$, recovering the Newtonian calibration $\alpha = GM/c^2$.

### A.2 Mass as a Topological Charge

Equation (A.1) reveals that mass in DGF is a **topological charge** — it is measured by the flux of $\nabla u$ through a surface at infinity. The mass does not need to be "localized" inside the surface; the flux integral counts it regardless of distribution. This is exactly the structure of Gauss's law in electrostatics and Newtonian gravity.

### A.3 The q-Field as a Gauss Law for Information

Rewrite (A.1) in terms of $q$:

$$\oint_{\partial V} \nabla\!\left(\frac{1}{q}\right) \cdot d\mathbf{S} = -\frac{4\pi G}{c^2} M_{\text{enc}}$$

Define the **information field strength** $\mathbf{E}_I \equiv -\nabla(1/q)$ (analogous to the gravitational field $\mathbf{g} = -\nabla\Phi$):

$$\oint_{\partial V} \mathbf{E}_I \cdot d\mathbf{S} = \frac{4\pi G}{c^2} M_{\text{enc}} \tag{A.2}$$

This is **Gauss's law for information**: the flux of the information field through a closed surface is proportional to the enclosed mass. Mass, in this picture, is the **source of information field flux**.

---

## Appendix B: Dimensional Analysis

### B.1 Dimensions of DGF quantities

| Quantity | Symbol | Dimensions |
|----------|--------|------------|
| q-field | $q$ | dimensionless, $[0,1]$ |
| Information potential | $u = 1/q$ | dimensionless, $[1,\infty)$ |
| Lattice spacing | $a$ | $[L]$ |
| Diffusion constant | $D_0 = a \cdot c$ | $[L^2/T]$ |
| Information mass density | $\rho_I$ | $[1/L^3]$ (bits/volume) |
| Physical mass density | $\rho_m$ | $[M/L^3]$ |
| Conversion factor | $\eta$ | $[M \cdot \text{bit}^{-1}]$ |
| Coupling constant | $\kappa = 4\pi G/c^2$ | $[T^2/LM] = [L/M]$ ??? |

Wait — check: $\nabla^2 u$ has dimensions $[1/L^2]$ (u is dimensionless). $\kappa\rho_m$ must have dimensions $[1/L^2]$. 

$$\kappa \cdot \frac{M}{L^3} = \frac{1}{L^2} \Rightarrow \kappa = \frac{L}{M}$$

Check: $G/c^2$ has dimensions:
$$[G] = L^3 M^{-1} T^{-2}, \quad [c^2] = L^2 T^{-2}$$
$$[G/c^2] = L M^{-1}$$

Yes, $4\pi G/c^2$ has dimensions $L/M$, consistent with $\nabla^2 u = -\kappa \rho_m$.

### B.2 Planck Scale Emergence

The Planck length $\ell_P = \sqrt{\hbar G/c^3}$ and Planck mass $m_P = \sqrt{\hbar c/G}$ do not appear in the DGF derivation. This is expected: DGF is a *classical* (non-quantum) theory of information. The Planck scale would enter only when quantum information theory (with $\hbar$) is incorporated — which is beyond the current framework.

---

## Appendix C: Open Problems

1. **Hyperbolic extension (gravity waves).** Reformulate the q-field equation as a hyperbolic PDE: $\Box u = \text{source}$, preserving finite propagation speed while retaining the Laplace correspondence in the static limit. Candidate: $\partial_t^2 q + \gamma \partial_t q - D_0 \nabla^2(1/q) = 0$.

2. **Strong-field exact solution.** Find the exact solution to $\nabla^2(1/q) = 0$ in spherical symmetry with the boundary condition $q(r_s) \to 0$, $q(\infty) = 1$, and determine whether the factor of 2 (light deflection) emerges.

3. **Cosmological embedding.** Extend the q-field equation to a cosmological background with time-dependent boundary conditions. Derive the Friedmann-like equation from conservation of total $q$.

4. **Equivalence principle.** Derive the equality of gravitational and inertial mass from DGF's information-theoretic structure. If all objects are "made of" occupied cells, does their response to $\nabla(1/q)$ automatically satisfy the equivalence principle?

5. **Cell basis problem.** The identification of the gravitational field with $1/q$ requires that the cell basis $\{|0\rangle, |1\rangle\}$ is physically distinguished. Why is this basis preferred? This connects to the quantum measurement problem and quantum Darwinism (Zurek).

---

## References

1. Barbour, J., & Magueijo, J. (2015). *Shape Dynamics and Unimodular Gravity*. arXiv:1503.08043.

2. Barbour, J., Koslowski, T., & Mercati, F. (2014). *Identification of a gravitational arrow of time*. Physical Review Letters, 113(18), 181101.

3. Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley-Interscience.

4. Vazquez, J.L. (2007). *The Porous Medium Equation: Mathematical Theory*. Oxford University Press.

5. Aronson, D.G. (1986). The porous medium equation. In *Nonlinear Diffusion Problems* (pp. 1-46). Springer.

6. Zurek, W.H. (2009). Quantum Darwinism. *Nature Physics*, 5(3), 181-188.

7. Will, C.M. (2014). The Confrontation between General Relativity and Experiment. *Living Reviews in Relativity*, 17, 4.

---

*Document version 1.0 — Theorems 11-12 establish the Newtonian gravity correspondence from DGF. The key result: the structure of the vacuum gravitational field equation ($\nabla^2\Phi = 0$) is a theorem of DGF in the static limit. The strongest caveat is the parabolic (infinite-speed) nature of the governing PDE, which limits the derivation to the static case.*
