# Decoherence Geometry Framework (DGF)
## A Unified Theory: Euclidean Quantum Origin → Spacetime → Mass → Gravity

**Huang Zhongchang**  
Independent Researcher, Nanjing, China | valhuang@kaiwucl.com  
Draft v2.0 | 2026-06-05

---

## Abstract

We present the Decoherence Geometry Framework (DGF), a theory in which Lorentzian spacetime, inertial mass, and gravitational interaction all emerge from a single irreversible process: the overflow of spatial interference information from high-density to low-density regions at the Planck scale. Three founding assumptions — information exists, capacity is bounded, overflow is irreversible — are sufficient.

The theory introduces one fundamental length $\mathfrak{l}$ (the information cell scale) as its only dimensional input beyond $\hbar$ and $c$. From these, without circularity, we derive: (1) the accessible coherence fraction $q \in [0,1]$ from Planck-cell occupancy; (2) the unique projection angle $\theta = \pi(1-q)$ from the trace distance of the maximum-entropy incoherent mixture; (3) the complex metric $ds^2 = e^{i\pi(1-q)}d\tau^2 + d\mathbf{x}^2$ as a partial Wick rotation parameterized by $q$; (4) the Euler residual mass $m = (2m_0/\pi)\sin(\pi A/2)$ with $A = 1-q$; (5) the spatial $q$ field equation from an entropy variational principle; (6) the gravitational constant $G = (\pi q_\infty/8)(c^3\mathfrak{l}^2/\hbar)$, non-circularly from $\mathfrak{l}$; and (7) the Fokker-Planck equation for $q$ dynamics from a microscopic master equation.

Four falsifiable predictions follow: a coherent mass ceiling $m_{\max} = \sqrt{2/\pi}\,m_p \approx 17\,\mu\mathrm{g}$; suppression of $G_\mathrm{eff} \approx G/\pi$ near quantum-coherent systems; a $p^4/3m$ decoherence channel distinct from Diosi-Penrose; and a secular drift $\dot{G}/G \sim H_0$.

---

## I. Founding Assumptions and the Inversion

### 1.1 The Standard Picture Inverted

Conventional physics treats the classical world as the default and asks how quantum mechanics emerges. DGF inverts this. The Euclidean quantum state is complete. The classical world is what remains after information has been irreversibly archived at the Planck scale.

> *Classicality is not an approximation to quantum mechanics. It is the overflow.*

### 1.2 Three Founding Assumptions

All subsequent structure follows from three assumptions that are independent of any pre-existing spacetime:

**Assumption 1 — Information exists.** There are distinguishable states. No time, space, or mass is presupposed.

**Assumption 2 — Capacity is bounded.** Each minimum information unit (Planck cell, scale $\mathfrak{l}$) carries at most $O(1)$ bits. This postulate introduces $\mathfrak{l}$ as DGF's one new dimensional constant — not defined through $G$.

**Assumption 3 — Overflow is irreversible.** When local information density exceeds cell capacity, the excess transfers to lower-density cells and cannot spontaneously return. This is the information-theoretic arrow of time.

### 1.3 The Founding Principle

> **Any equation that presupposes Lorentzian spacetime already exists cannot be a starting point. Only expressions depending solely on information states and information capacity are valid inputs.**

This principle rules out as starting points: the Schrödinger equation, Einstein field equations, Lindblad equation, Friedmann equations, GUP, and any equation containing $c$, $t$, $\mathbf{x}$, or $g_{\mu\nu}$ as background parameters.

The allowed inputs are: $\hbar$ (quantum of action), $c$ (maximum information propagation speed — derived as a necessary consistency condition, Section III), $k_B$ (information-energy conversion), $\mathfrak{l}$ (cell scale, the one new constant), and pure mathematics.

### 1.4 Derived Scales

From $\mathfrak{l}$, $\hbar$, $c$ alone:

$$\tau_0 = \frac{\mathfrak{l}}{c}, \quad m_0 = \frac{\hbar}{c\mathfrak{l}}, \quad \rho_0 = \frac{m_0}{\mathfrak{l}^3} = \frac{\hbar}{c\mathfrak{l}^4}$$

**Dimensional check:** $[\tau_0] = T$, $[m_0] = M$, $[\rho_0] = ML^{-3}$. ✓  
**Circularity check:** No $G$ appears anywhere. $\mathfrak{l}$ is primary; $G$ is derived (Section VI). ✓

---

## II. The Accessible Coherence Fraction $q$

### 2.1 Planck-Cell Occupancy

Partition the support volume $V_S$ of system $S$ into cells of volume $\mathfrak{l}^3$, giving $N_S = V_S/\mathfrak{l}^3$ cells. Each cell $c$ carries an occupancy fraction:

$$f_c = \frac{I_c}{I_c^{\max}} \in [0,1]$$

where $I_c^{\max} = \ln 2$ (one bit per cell, holographic bound). A full cell ($f_c \to 1$) cannot participate in quantum branch recombination.

### 2.2 Definition of $q$

$$\boxed{q_S = \frac{1}{N_S}\sum_c f_c = \bar{f}_S}$$

$q = 1$: pure quantum (all cells empty, full interference access).  
$q = 0$: pure classical (all cells full, all information archived).  
$A = 1 - q$: archived fraction.

**Circularity check:** $q$ is a counting ratio. No mass, no $G$, no spacetime. ✓

### 2.3 Information Flow Direction

The available capacity of cell $c$ is $(1-f_c)$. A massive object has $\bar{f} \sim 1$ (near zero available capacity). A low-mass system has $\bar{f} \ll 1$ (large available capacity). The entropy gradient for transferring $\delta I$ bits from sender $S$ to receiver $R$:

$$\frac{\partial S}{\partial(\delta I)} = k_B\left[\ln\frac{1-\bar{f}_S}{\bar{f}_S} - \ln\frac{1-\bar{f}_R}{\bar{f}_R}\right] > 0 \quad \text{when } \bar{f}_S > \bar{f}_R$$

Entropy increases when information flows from high-occupancy (massive, classical) to low-occupancy (light, quantum) systems. **No pairing mechanism is required.** The flow is a consequence of combinatorial entropy maximization.

---

## III. The Projection Angle: Theorem $\theta = \pi(1-q)$

### 3.1 Physical Setup

Decoherence events are independent and uncorrelated — each overflow event deposits a small amount of information into a randomly selected overflow sector with no phase memory. The appropriate mathematical object is therefore an **incoherent mixture** (density matrix), not a coherent superposition (pure state).

### 3.2 Maximum Entropy Uniquely Fixes the Distribution

Let there be $N$ orthogonal information sectors: $|L\rangle$ (accessible) and $|s_2\rangle,\ldots,|s_N\rangle$ (overflow). Total overflow is $A = \sum_{k=2}^N p_k$. The maximum-entropy distribution subject to $\sum_{k=2}^N p_k = A$ is unique:

$$p_k = \frac{A}{N-1}, \quad k = 2,\ldots,N$$

**No thermodynamic limit required.** The uniform distribution is uniquely selected by maximum entropy for any $N \geq 2$.

### 3.3 Theorem: $\theta(A) = \pi A$

**Density matrix:**
$$\rho(A) = (1-A)|L\rangle\langle L| + \frac{A}{N-1}\sum_{k=2}^N |s_k\rangle\langle s_k|$$

**Trace distance from accessible state $\rho(0) = |L\rangle\langle L|$:**

$$\Delta = \rho(A) - \rho(0) = -A|L\rangle\langle L| + \frac{A}{N-1}\sum_{k=2}^N |s_k\rangle\langle s_k|$$

Eigenvalues: $-A$ (once) and $+A/(N-1)$ ($N-1$ times). Trace norm:

$$\|\Delta\|_1 = |-A| + (N-1)\cdot\frac{A}{N-1} = 2A$$

$$\boxed{d_{\mathrm{tr}}(\rho(0),\rho(A)) = \frac{1}{2}\|\Delta\|_1 = A}$$

**This result is exact for all $N \geq 2$. No approximation.**

Normalizing to the half-circle $[0,\pi]$ (Euclidean at $A=0$, Lorentzian at $A=1$):

$$\boxed{\theta(A) = \pi \cdot d_{\mathrm{tr}} = \pi A = \pi(1-q)}$$

**Why trace distance, not Bures angle?** The Bures angle gives $\arccos\sqrt{1-A}$ — treating all mixtures as if they were coherent superpositions. DGF overflow is incoherent (probabilities add, not amplitudes), so trace distance is the correct metric.

**Why $[0,\pi]$ normalization?** The Euclidean metric $e^{i\cdot 0} = 1$ and the Lorentzian metric $e^{i\pi} = -1$ are the two fixed points of the partial Wick rotation. The half-circle is the natural coordinate between them.

---

## IV. Time, Space, and the Complex Metric

### 4.1 Time Emerges as the Direction of Decreasing $q$

In the primordial Euclidean state, all four directions of $d\tau^2 + dx^2 + dy^2 + dz^2$ are equivalent. Decoherence breaks this symmetry by singling out a preferred direction: the direction along which $q$ decreases.

$$dt \equiv -dq \cdot \tau_0$$

Time is not a pre-existing parameter. Time is the name given to the direction of monotonically decreasing accessible coherence. The arrow of time follows from Assumption 3 (overflow is irreversible) — no additional postulate required.

### 4.2 Space Emerges as the Geometry of $q$ Iso-Surfaces

Spatial structure emerges when $\nabla q \neq 0$ — different regions have different $q$ values. Two points are separated in "space" to the extent that their $q$ values differ in a direction orthogonal to the time direction. The spatial metric element is determined by the geometry of $q$ iso-surfaces.

**Note on dimensionality:** The information adjacency graph that underlies the $q$ field equation (Section V) has a continuum limit with effective dimension $d$. The inverse-square law for gravity (Section VI) requires $d=3$. The question of *why* $d=3$ is an open problem (Section VIII, Gap 1).

### 4.3 The Complex Metric from Partial Wick Rotation

From $\theta = \pi(1-q)$, a partial Wick rotation by angle $\theta/2$:

$$\tau \to e^{i\theta/2}\tau'$$

gives the complex temporal metric component:

$$g_{\tau\tau} = e^{i\theta} = e^{i\pi(1-q)}$$

**Full metric:**
$$\boxed{ds^2 = e^{i\pi(1-q)}\,d\tau'^2 + dx^2 + dy^2 + dz^2}$$

**Boundary conditions — verified:**

| $q$ | $\theta$ | $e^{i\theta}$ | Metric | Physics |
|---|---|---|---|---|
| $1$ | $0$ | $+1$ | $d\tau^2 + d\mathbf{x}^2$ | Pure Euclidean ✓ |
| $1/2$ | $\pi/2$ | $+i$ | $i\,d\tau^2 + d\mathbf{x}^2$ | Quantum-classical boundary ✓ |
| $0$ | $\pi$ | $-1$ | $-d\tau^2 + d\mathbf{x}^2$ | Minkowski (with $\tau' = ct$) ✓ |

### 4.4 Physical Meaning of the Imaginary Part

The metric decomposes as:

$$e^{i\pi(1-q)} = \underbrace{\cos[\pi(1-q)]}_{\text{Lorentzian residue}} + i\underbrace{\sin[\pi(1-q)]}_{\text{Euclidean residue}}$$

The imaginary part is **not** a mathematical artifact. It represents the surviving Euclidean structure — the quantum coherence that has not yet been archived. Discarding it (as standard Wick rotation does) is physically wrong in DGF: it discards the quantum sector.

---

## V. Mass from Archived Information

### 5.1 The Euler Residual

The information state vector is:
$$|\chi(A)\rangle = \sqrt{1-A}\,|Q\rangle + \sqrt{A}\,|C\rangle$$

where $|Q\rangle$ is the flowing quantum sector and $|C\rangle$ is the archived classical sector. The Euler residual — the complex amplitude after projection — is:

$$R(A) = 1 - e^{i\pi A}$$

$$|R(A)|^2 = 2 - 2\cos(\pi A) = 4\sin^2\!\left(\frac{\pi A}{2}\right) \implies |R(A)| = 2\sin\!\left(\frac{\pi A}{2}\right)$$

### 5.2 The Mass Formula

$$\boxed{m(A) = \frac{2m_0}{\pi}\sin\!\left(\frac{\pi A}{2}\right), \quad m_0 = \frac{\hbar}{c\mathfrak{l}}}$$

**Properties:**
- $m(0) = 0$: fully quantum system has zero rest mass (photons, massless bosons: $A \to 0$)
- $m(1) = m_{\max} = 2m_0/\pi$: the coherent mass ceiling
- $m_{\max} = \sqrt{2/\pi}\,m_p \approx 17\,\mu\mathrm{g}$ (after fixing $\mathfrak{l}$ from $G$, Section VI)

**Dimensional check:** $[m_0] = M$, $|R(A)|$ dimensionless, $[m(A)] = M$. ✓  
**Circularity check:** $m_0 = \hbar/(c\mathfrak{l})$ contains no $G$. ✓

### 5.3 Why Mass Does Not Change During Decoherence

Total information is conserved. Decoherence converts $I_{\mathrm{flowable}}$ to $I_{\mathrm{locked}}$. Both contribute equally to energy because both represent real physical states of Planck cells. What changes is accessibility, not quantity.

$$I_{\mathrm{tot}} = I_{\mathrm{locked}} + I_{\mathrm{flowable}} = \text{const}$$

### 5.4 Why $E = mc^2$

Each Planck cell stores one bit at characteristic energy $E_0 \sim \hbar c/\mathfrak{l} = m_0 c^2$. For a system with $N_S \cdot A$ archived bits:

$$E = N_S \cdot A \cdot m_0 c^2 = m \cdot c^2$$

$E = mc^2$ is not a fundamental axiom. It is the information-energy conversion at the Planck boundary: each archived bit contributes $m_0 c^2 = \hbar c/\mathfrak{l}$ to the rest energy.

---

## VI. Gravity from $q$-Gradients

### 6.1 The $q$ Field Equation (from Entropy Variational Principle)

The information entropy functional for the $q$-field in the presence of locked information density $\rho$:

$$S[q] = \int d^3\!x\left[s_{\mathrm{bin}}(q) - \frac{\mathfrak{l}^2}{2}(\nabla q)^2 - \frac{\rho}{\rho_0}\,q\right]$$

where $s_{\mathrm{bin}}(q) = -q\ln q - (1-q)\ln(1-q)$ is the binary entropy per cell.

The three terms encode: (1) local information entropy; (2) gradient penalty (spatial structure costs entropy); (3) matter coupling (high $\rho$ suppresses $q$).

Variational principle $\delta S/\delta q = 0$:

$$\boxed{\mathfrak{l}^2\nabla^2 q = \frac{\rho}{\rho_0} - \ln\frac{1-q}{q}}$$

**Both sides dimensionless.** This corrects the dimensional error in earlier drafts ($\nabla^2 q = (l_p^2/2\pi)(\rho/\rho_p)$ had inconsistent dimensions).

**Note on coordinates:** The coordinates $\mathbf{x}$ label information cells on the adjacency graph — they are not points of a pre-existing space. Physical space emerges from the $q$ distribution on this graph. The continuum PDE is the large-scale limit; the graph update law is primary.

### 6.2 Point-Mass Solution

For macroscopic matter ($q \ll 1$, $\rho/\rho_0 \gg |\ln q|$) with a point mass $M$ at the origin:

$$q(r) = q_\infty - \frac{M}{4\pi m_0}\frac{\mathfrak{l}}{r}$$

$q$ decreases toward the mass — coherence is suppressed where information is archived. ✓

### 6.3 Christoffel Symbols and Geodesic Acceleration

From $g_{\tau\tau} = e^{i\pi(1-q)}$:

$$\Gamma^k_{\tau\tau} = \frac{i\pi}{2}e^{i\pi(1-q)}\partial_k q$$

Near complete decoherence ($q \to 0$, $e^{i\pi(1-q)} \to -1$):

$$\delta g_{\tau\tau} \equiv \mathrm{Re}(e^{i\pi(1-q)}) + 1 \approx \frac{\pi^2 q^2}{2}$$

Observable acceleration (real part, slow-motion limit):

$$\mathbf{a} = -\frac{c^2\pi^2}{2}\,q\,\nabla q$$

Substituting the point-mass solution:

$$|\nabla q| = \frac{M\mathfrak{l}}{4\pi m_0 r^2}, \quad q \approx q_\infty \sim 1$$

$$\mathbf{a} = -\frac{c^2\pi^2 q_\infty}{2} \cdot \frac{M\mathfrak{l}}{4\pi m_0 r^2}\hat{\mathbf{r}} = -\frac{c^2\pi q_\infty \mathfrak{l}}{8m_0}\frac{M}{r^2}\hat{\mathbf{r}}$$

### 6.4 The Non-Circular Identification of $G$

Comparing with Newton $\mathbf{a} = -GM/r^2$:

$$\boxed{G = \frac{\pi q_\infty}{8}\cdot\frac{c^3\mathfrak{l}^2}{\hbar}}$$

**Circularity check:** $\mathfrak{l}$, $\hbar$, $c$, $q_\infty$ — no $G$ anywhere. ✓  
**Dimensional check:** $[c^3\mathfrak{l}^2/\hbar] = (L^3T^{-3})(L^2)/(ML^2T^{-1}) = L^3M^{-1}T^{-2} = [G]$. ✓

**Logical inversion:** The observed $G$ fixes $\mathfrak{l}$:
$$\mathfrak{l} = \sqrt{\frac{8}{\pi q_\infty}\frac{\hbar G}{c^3}} \approx \sqrt{\frac{8}{\pi}}\,l_p \approx 1.60\,l_p$$

### 6.5 Why Gravity is Always Attractive

$q$ is lower near mass (more information archived). $\nabla q$ points away from mass ($q$ increases with distance). The geodesic response drives test bodies toward lower $q$ — toward mass. Gravity has no repulsive branch because information overflow is unidirectional (Assumption 3).

### 6.6 Causal Chain

$$\text{Archived information} \to \text{Low } q \to \nabla q \neq 0 \to \text{Complex metric curvature} \to \text{Geodesic deflection} \to \text{Gravity}$$

Every link is either a definition or a derived consequence. No gravitational force law is postulated.

---

## VII. $q$ Dynamics: The Fokker-Planck Equation

### 7.1 Microscopic Master Equation

Each cell's access weight $a_c$ evolves under decoherence (loss rate $\gamma_c$) and Planck-scale fluctuations (variance $\sigma_c^2 = c/\mathfrak{l} = 1/\tau_0$). For $N$ independent cells, the Central Limit Theorem and the Kramers-Moyal expansion truncate exactly at second order (Pawula's theorem, since $M_3 = 0$):

$$\boxed{\frac{\partial P}{\partial t} = -\frac{\partial}{\partial q}\left[v(q)P\right] + \frac{\partial^2}{\partial q^2}\left[D(q)P\right]}$$

### 7.2 Drift Coefficient

The drift is driven by the **receiver** entropy gradient (not the sender's), because irreversibility is determined by where information goes:

$$S_{\mathrm{recv}}(q) = \ln\mathcal{N}_{\mathrm{recv}}(q) \propto \ln q \implies \partial_q S_{\mathrm{recv}} = \frac{1}{q}$$

$$\boxed{v(q) = \frac{\Gamma(q)}{q} > 0}$$

$v > 0$ always: mean overflow monotonically increases. This is the mathematical source of the time arrow.

### 7.3 Diffusion Coefficient

$$\boxed{D(q) = \frac{c}{2\mathfrak{l}}\cdot\frac{\mathfrak{l}^3}{V_S}\cdot q(1-q)}$$

The $q(1-q)$ factor enforces reflecting boundaries. For macroscopic systems ($V_S \gg \mathfrak{l}^3$), diffusion is exponentially suppressed — $q$ is quasi-static on laboratory timescales.

### 7.4 Mean Overflow is Monotone

$$\frac{d\langle q\rangle}{dt} = \left\langle\frac{\Gamma(q)}{q}\right\rangle > 0$$

### 7.5 Decompression at $q = 1$

When local information density reaches $\rho_0$ (Planck saturation), the reflecting boundary at $q=1$ becomes absorbing-emitting. Decompression rate:

$$\kappa \sim \tau_0^{-1}\exp\!\left(-S_{\mathrm{BH}}/k_B\right)$$

For macroscopic objects ($S_{\mathrm{BH}}/k_B \sim 10^{70}$): $\kappa \approx 0$ — no spontaneous re-quantization.  
For Planck-mass black holes ($S_{\mathrm{BH}}/k_B \sim 1$): $\kappa \sim \tau_0^{-1}$ — immediate cycling.

The Big Bang was the first global decompression event: $q \to 0$ everywhere triggered local resets $q \to 1$, seeding the initial quantum state.

---

## VIII. GUP-Lindblad Decoherence Kernel

The same $q$-fluctuation that generates the complex metric also drives a GUP-modified decoherence channel. With the effective Planck length $l_{\mathrm{eff}}(t) = \mathfrak{l}[1 + \delta A(t)]$ and the bounded wave-number map $k(p) = \mathfrak{l}^{-1}\tanh(\mathfrak{l}p/\hbar)$:

$$[x,p] = i\hbar\left(1 + \frac{\mathfrak{l}^2 p^2}{\hbar^2} + \cdots\right) \implies H = H_0 - \frac{\mathfrak{l}^2}{\hbar^2}\frac{p^4}{3m} + O(\mathfrak{l}^4)$$

Setting $V = p^4/3m$ and using $\langle\delta A(t)\delta A(t')\rangle = \tau_0\delta(t-t')$:

$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H_0 + \beta_0 V, \rho] - \frac{D_\beta}{\hbar^2}[V,[V,\rho]]$$

$$\boxed{K_{ab}(t) = \exp\!\left[-\frac{2\tau_0\mathfrak{l}^4}{\hbar^6}\left(\Delta\!\left\langle\frac{p^4}{3m}\right\rangle\right)^{\!2}t\right]}$$

**Null channel:** Rigid translations have $\Delta\langle p^4/3m\rangle = 0$, giving $K_{ab} = 1$. DGF predicts zero intrinsic decoherence for ideal rigid displacements — a clean experimental discriminator.

---

## IX. Dark Energy

### 9.1 The Cosmic Spiral

The universe's mean archived fraction $\bar{A}(t)$ increases monotonically. In complex information space:

$$z(t) = \bar{A}\,e^{i\pi\bar{A}}, \quad |\dot{z}|^2 = \dot{A}^2(1 + \pi^2\bar{A}^2)$$

The second term $\pi^2\bar{A}^2\dot{A}^2$ grows as cosmic decoherence accumulates — this is dark energy.

### 9.2 Equation of State $w = -1$

In the quasi-static limit ($\dot{A}$ slowly varying), $\dot{\rho}_\Lambda \approx 0$, giving:

$$p_\Lambda = -\rho_\Lambda \implies w = -1$$

$w = -1$ is not imposed by hand. It is the thermodynamic limit of slow irreversible decoherence accumulation. The cosmological constant is the geometric shadow of cosmic information archiving.

---

## X. Falsifiable Predictions

### Prediction 1: Suppression of $G$ near Quantum Systems

$$G_{\mathrm{eff}}(q) = \frac{G}{\sqrt{1 + \pi^2 q^2}}$$

Near quantum-coherent systems ($q \approx 1$): $G_{\mathrm{eff}} \approx G/\pi \approx 0.318\,G$.  
**Target:** Precision $G$ measurements using BEC interferometers or levitated nanoparticles below $14\,\mu\mathrm{g}$.

### Prediction 2: The Coherent Mass Ceiling

$$m_{\max} = \sqrt{\frac{2}{\pi}}\,m_p \approx 17\,\mu\mathrm{g}$$

No single coherent branch can carry more mass than this — a geometric hard limit, not an engineering limitation. Current experiments reach $\sim 1\,\mu\mathrm{g}$ (2023); factor $\sim 17$ needed.

### Prediction 3: Secular Drift of $G$

As $q_\infty$ decreases with cosmic decoherence:

$$\frac{\dot{G}}{G} = \frac{\dot{q}_\infty}{1-q_\infty} \sim H_0 \approx 2.3\times10^{-18}\,\mathrm{s}^{-1}$$

Current limit: $|\dot{G}/G| < 10^{-13}\,\mathrm{yr}^{-1}$. DGF predicts $\sim 10^{-10}\,\mathrm{yr}^{-1}$ — within reach of next-generation pulsar timing arrays.

### Prediction 4: $p^4/3m$ Decoherence Channel

$$K_{ab}(t) = \exp\!\left[-\frac{2\tau_0\mathfrak{l}^4}{\hbar^6}\left(\Delta\!\left\langle\frac{p^4}{3m}\right\rangle\right)^{\!2}t\right]$$

Decoherence rate scales as $(\Delta\langle p^4/3m\rangle)^2$, not gravitational self-energy (Diosi-Penrose) or position separation (standard environmental decoherence).  
**Target:** Compare decoherence times of equal-mass levitated nanoparticles with different momentum distributions (achieved by varying trap frequency). Existing ETH Zürich and Tokyo U datasets are candidate data for retrospective analysis.

| Prediction | DGF Value | Current Status |
|---|---|---|
| $G_\mathrm{eff}$ suppression | $\approx G/\pi$ at $q=1$ | Not yet tested |
| Coherent mass ceiling | $17\,\mu\mathrm{g}$ | $1\,\mu\mathrm{g}$ reached |
| Secular $G$ drift | $\sim 10^{-10}\,\mathrm{yr}^{-1}$ | Factor $10^3$ sensitivity needed |
| $p^4/3m$ decoherence channel | $\propto(\Delta\langle p^4/3m\rangle)^2$ | Retrospective test possible now |

---

## XI. Relation to Existing Work

| Framework | Relation to DGF |
|---|---|
| **Greensite 1993** | Uses same $e^{i\theta}$ metric; selects $\theta=\pi$ in $D=4$ via one-loop. DGF adds: $\theta = \pi(1-q)$, $q$ has microscopic definition, signature change is driven by information overflow, not field loops. |
| **Verlinde 2011 (entropic gravity)** | Both derive gravity from thermodynamics. DGF differs: explicit causal direction (decoherence → gravity, not entropy gradient → force); microscopic carrier $q$; non-circular $G$. |
| **Penrose-Diosi** | Opposite causal direction. Penrose: gravity causes collapse. DGF: decoherence causes apparent gravity. Experimental discrimination via decoherence channel ($p^4/3m$ vs gravitational self-energy). |
| **Zurek quantum Darwinism** | Environmental decoherence is the lab-scale face of DGF. DGF provides the geometric origin Zurek takes as given. |
| **Hartle-Hawking no-boundary** | No-boundary = Euclidean hemisphere glued to Lorentzian spacetime. DGF provides the gluing mechanism: partial Wick rotation parameterized by $q$. |

---

## XII. Open Problems

The following derivations remain open and are the primary agenda for completion.

**Gap 1 (Critical): Why $d = 3$ spatial dimensions?**

The inverse-square law requires the information adjacency graph to have a three-dimensional continuum limit. Greensite 1993 shows $D = 4$ spacetime is special for the Lorentzian fixed point via one-loop field theory, but this uses a Lorentzian background. DGF needs an independent derivation from the combinatorial structure of the information graph.

**Gap 2 (Critical): Why one time direction?**

The primordial Euclidean state has four equivalent directions. Decoherence selects one as "time." DGF gives the mechanism (decreasing $q$), but not the uniqueness: why does a single decoherence front select exactly one preferred direction rather than zero or two?

**Gap 3 (Medium): Numerical value of $q_\infty$**

$G = (\pi q_\infty/8)(c^3\mathfrak{l}^2/\hbar)$ depends on the cosmic background coherence $q_\infty$. The theory predicts $q_\infty \lesssim 1$ but does not yet predict its precise value. Observational constraints from CMB homogeneity could provide a bound.

**Gap 4 (Medium): Connection to the Standard Model**

The mass formula $m(A) = (2m_0/\pi)\sin(\pi A/2)$ gives a parametric family. What determines the specific $A$ values for the electron, muon, quarks? DGF does not yet explain the particle mass spectrum.

**Gap 5 (Small): $G_\mathrm{eff}(q)$ projection rule**

The suppression formula $G_\mathrm{eff} = G/\sqrt{1+\pi^2 q^2}$ uses a modulus projection from the complex metric. A first-principles derivation of this projection rule — which component of the complex metric is physically observable — is needed.

---

## XIII. Conclusion

DGF derives Lorentzian spacetime, mass, and gravity from three founding assumptions about information and one new fundamental constant $\mathfrak{l}$. Every step respects the founding principle: no equation presupposing Lorentzian spacetime is used as a starting point.

The complete non-circular chain:

```
Assumption 1: Information exists
Assumption 2: Capacity bounded → fundamental cell scale ℓ
Assumption 3: Overflow irreversible
    ↓
q = ⟨f_c⟩ (cell occupancy average)
    ↓
θ = π(1-q)  [Theorem: trace distance of max-entropy incoherent mixture]
    ↓
ds² = e^{iπ(1-q)}dτ² + dx²  [partial Wick rotation]
    ↓
m(A) = (2m₀/π)sin(πA/2),  m₀ = ℏ/cℓ  [Euler residual mass]
    ↓
ℓ²∇²q = ρ/ρ₀ - ln((1-q)/q)  [entropy variational principle]
    ↓
G = (πq∞/8)(c³ℓ²/ℏ)  [geodesic comparison, non-circular]
    ↓
∂_tP = -∂_q(vP) + ∂²_q(DP),  v = Γ/q,  D = D₀ℓ³/V_S  [Kramers-Moyal]
    ↓
K_{ab}(t) = exp[-(2τ₀ℓ⁴/ℏ⁶)(Δ⟨p⁴/3m⟩)²t]  [GUP-Lindblad kernel]
```

Five open problems remain. The two critical ones — why $d=3$ and why one time direction — are the primary targets for the next phase of development.

> *The classical world is not the ground state of quantum mechanics. It is the overflow.*

---

## References

1. Greensite, J. (1993). Dynamical origin of the Lorentzian signature of spacetime. *arXiv:gr-qc/9210008*.
2. Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *JHEP* **04**, 029.
3. Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Rel. Grav.* **28**, 581.
4. Diosi, L. (1989). Models for universal reduction of macroscopic quantum fluctuations. *Phys. Rev. A* **40**, 1165.
5. Petruzziello, L. & Illuminati, F. (2021). Quantum gravitational decoherence from fluctuating minimal length. *Nat. Commun.* **12**, 4449.
6. Zurek, W.H. (1981). Pointer basis of quantum apparatus. *Phys. Rev. D* **24**, 1516.
7. Hartle, J. & Hawking, S. (1983). Wave function of the universe. *Phys. Rev. D* **28**, 2960.
8. Rossi, M. et al. (2025). Quantum delocalization of a levitated nanoparticle. *Phys. Rev. Lett.* **135**, 083601.
9. Kamba, M., Hara, N. & Aikawa, K. (2025). Quantum squeezing of a levitated nanomechanical oscillator. *Science* **389**, 1225.
10. Schrinski, B. et al. (2023). Macroscopic quantum test with bulk acoustic wave resonators. *Phys. Rev. Lett.* **130**, 133604.
11. Lee, J.-W. (2010). On the origin of entropic gravity and inertia. *arXiv:1003.4464*.
