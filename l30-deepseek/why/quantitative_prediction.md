# DGF Quantitative Predictions: Derivations and Critical Assessment

**Date:** 2026-06-05
**Purpose:** Derive at least one quantitative, testable, falsifiable prediction from the DGF framework, expressed in terms of framework variables, distinguishable from standard QM, and honestly assessed.

---

## 0. Framework Variables (Reference)

| Symbol | Meaning | Units |
|--------|---------|-------|
| $q$ | Accessible coherence fraction; $q=1$ fully quantum, $q=0$ fully classical | dimensionless |
| $A = 1-q$ | Archived (locked) information fraction | dimensionless |
| $N$ | Number of Planck cells in system; $N = V_S / \mathfrak{l}^3$ | dimensionless |
| $\mathfrak{l}$ | Information cell scale; $\mathfrak{l} \approx 2.26\,\ell_p \approx 3.66 \times 10^{-35}\,\mathrm{m}$ | L |
| $\tau_0 = \mathfrak{l}/c$ | Cell crossing time | T |
| $m_0 = \hbar/(c\mathfrak{l})$ | Fundamental mass unit ($\approx 0.443\,m_p \approx 9.6\,\mu\mathrm{g}$) | M |
| $\rho_0 = m_0/\mathfrak{l}^3$ | Reference density ($\sim 2\times 10^{95}\,\mathrm{kg/m^3}$) | M/L³ |
| $v(q) = \Gamma_0 k_B/q$ | Drift coefficient in Fokker-Planck (rate of classicalization) | 1/T |
| $D(q) = D_0 q(1-q) \mathfrak{l}^3/V_S$ | Diffusion coefficient; $D_0 = 1/(2\tau_0)$ | 1/T |
| $\Gamma_0 \sim 1/\tau_0$ | Planck-scale drift rate | 1/T |
| $\varepsilon$ | Spontaneous occupation probability per empty cell per $\tau_0$ (Process B) | dimensionless |

**Critical note on $\varepsilon$:** This parameter does not appear explicitly in the DGF paper's Fokker-Planck formulation. It is introduced here to separate Process B (spontaneous occupation, the source term) from Process A (diffusion/homogenization). In the current DGF formulation, the drift $v(q)$ combines both processes. To make a testable prediction about the *residual* decoherence floor, we need to identify the Process B component separately, which requires introducing $\varepsilon$ as a phenomenological parameter.

---

## 1. Prediction A: Residual Decoherence Rate for Perfectly Isolated Systems

### 1.1 Derivation

**Assumption:** Process B (spontaneous occupation) acts independently on each empty Planck cell. An empty cell at time $t$ has probability $\varepsilon$ of becoming occupied within one cell time $\tau_0$. This is the microscopic engine of classicalization.

**Step 1 — Rate of spontaneous occupation events.**

For a system with $N$ Planck cells and coherence fraction $q$, there are $Nq$ empty cells. The expected number of spontaneous occupation events per unit time is:

$$\dot{n}_{\text{occ}} = \frac{\varepsilon N q}{\tau_0} \qquad (1)$$

Equivalently, the rate of change of $q$ from Process B alone (no diffusion) is:

$$\left.\frac{dq}{dt}\right|_B = -\frac{\dot{n}_{\text{occ}}}{N} = -\frac{\varepsilon q}{\tau_0} \qquad (2)$$

**Step 2 — From occupation events to decoherence.**

Each spontaneous occupation event "locks" one bit of information into a specific Planck cell. In the density matrix picture, this corresponds to a projection onto the occupation basis for that cell. For a superposition that involves $\Delta N$ distinct cells (cells whose state differs between the two branches), each such event that hits one of these $\Delta N$ cells will partially or completely decohere the superposition.

The rate of decoherence-relevant events is:

$$\gamma_{\text{DGF}} = \frac{\varepsilon \Delta N}{\tau_0} \qquad (3)$$

For a superposition of spatial extent characterized by a displacement $\Delta x$ and cross-sectional area $\mathcal{A}$ (the geometric overlap of the two branches), the number of Planck cells that differ is:

$$\Delta N = \frac{\Delta x \cdot \mathcal{A}}{\mathfrak{l}^3} \qquad (4)$$

**Step 3 — The decoherence timescale.**

$$\boxed{\tau_{\text{decoherence}}^{\text{DGF}} = \frac{1}{\gamma_{\text{DGF}}} = \frac{\tau_0}{\varepsilon \Delta N} = \frac{\mathfrak{l}}{c \varepsilon \Delta N}} \qquad (5)$$

For a compact object of mass $M$ and density $\rho$, with volume $V_S = M/\rho$, the total number of cells is $N = M/(\rho \mathfrak{l}^3)$. If the entire object participates in the superposition (e.g., center-of-mass delocalization), then $\Delta N \sim N$, giving:

$$\boxed{\tau_{\text{decoherence}}^{\text{DGF}}(M,\rho) = \frac{\tau_0}{\varepsilon N} = \frac{\rho \mathfrak{l}^4}{c \varepsilon M}} \qquad (6)$$

**The scaling is $\tau \propto \rho/M$.** Denser objects decohere SLOWER (they have fewer cells per unit mass). More massive objects decohere FASTER.

### 1.2 Comparison with Competing Predictions

| Model | Decoherence timescale $\tau$ | Mass scaling | Density scaling |
|-------|------------------------------|--------------|-----------------|
| **DGF (this work)** | $\frac{\rho \mathfrak{l}^4}{c \varepsilon M}$ | $\propto 1/M$ | $\propto \rho$ |
| **Penrose (1996)** | $\frac{\hbar}{G M^2 / R} \propto \frac{\hbar}{G \rho^{1/3} M^{5/3}}$ | $\propto 1/M^{5/3}$ | $\propto 1/\rho^{1/3}$ |
| **Diosi (1989)** | $\frac{\hbar}{G \int d^3r d^3r' \frac{\rho(r)\rho(r')}{|r-r'|}} \sim \frac{\hbar R}{G M^2}$ | $\propto 1/M^2$ | $\propto 1/\rho^{1/3}$ |
| **Environmental** | $\frac{1}{\gamma_0 N_{\text{env}}}$ | Independent of $M$ | Independent of $\rho$ |
| **Standard QM** | $\infty$ (no intrinsic decoherence) | N/A | N/A |

### 1.3 Distinctive Signature

DGF predicts that **for fixed mass, lower-density objects decohere faster** ($\tau \propto \rho$). This is the OPPOSITE of Penrose and Diosi, which predict that **lower-density (larger) objects decohere slower** ($\tau \propto 1/\rho^{1/3}$).

The sign of the density dependence is a clean experimental discriminator:

$$\frac{\tau_{\text{DGF}}(\rho_1)}{\tau_{\text{DGF}}(\rho_2)} = \frac{\rho_1}{\rho_2} \quad \text{vs.} \quad \frac{\tau_{\text{Penrose}}(\rho_1)}{\tau_{\text{Penrose}}(\rho_2)} = \left(\frac{\rho_2}{\rho_1}\right)^{1/3}$$

For silica ($\rho \approx 2.2$ g/cm³) vs. gold ($\rho \approx 19.3$ g/cm³) nanoparticles of equal mass:
- **DGF:** Gold decoheres $19.3/2.2 \approx 8.8\times$ SLOWER than silica (gold is denser, fewer cells)
- **Penrose:** Gold decoheres $(2.2/19.3)^{1/3} \approx 0.48\times$ — gold decoheres about $2\times$ FASTER (more compact, higher self-energy)

The predicted RATIO is opposite in sign. This is a qualitative, model-independent discriminator.

### 1.4 Falsifiability

**Falsifiable claim:** Even with perfect environmental isolation (zero photon scattering, zero gas collisions, zero blackbody radiation, zero vibrational coupling), a quantum superposition of spatial extent $\Delta N$ Planck cells has a finite lifetime $\tau = \tau_0/(\varepsilon \Delta N)$.

**Falsification condition:** If a superposition of known $\Delta N$ is maintained for time $T \gg \tau_0/(\varepsilon \Delta N)$, then either (a) the predicted $\tau$ is too short (constraining $\varepsilon$ from above), or (b) the framework's identification of $\Delta N$ as the number of differing Planck cells is incorrect.

**Current experimental bound:** Matter-wave interferometry with molecules of mass $M \sim 10^{-24}$ kg maintains coherence for $\tau_{\text{obs}} \sim 10^{-2}$ s (e.g., C$_{70}$ fullerenes, Arndt group). Taking $\Delta N \sim (R/\mathfrak{l})^3 \sim (10^{-9}/3.7\times 10^{-35})^3 \sim 2 \times 10^{76}$ (spatial cells in a 1 nm molecule):

$$\varepsilon < \frac{\tau_0}{\tau_{\text{obs}} \Delta N} \approx \frac{1.2 \times 10^{-43}}{10^{-2} \times 2 \times 10^{76}} \approx 6 \times 10^{-118}$$

This is an **extremely strong constraint** on $\varepsilon$. It means either:
1. $\varepsilon$ is finely tuned to be astronomically small ($< 10^{-117}$)
2. $\Delta N$ is not $(V_S/\mathfrak{l}^3)$ — only a tiny fraction of Planck cells participate in any given superposition
3. The decoherence mechanism does not scale with the total number of cells, but with some other quantity (e.g., the difference in $q$ between branches, not the number of cells)

**Honest assessment:** Prediction 1 requires the free parameter $\varepsilon$ and produces an uncomfortably strong bound from current experiments.

---

## 2. Prediction B: $q$-Fluctuation Spectrum and System-Size Scaling

### 2.1 Derivation from the Fokker-Planck Equation

Unlike Prediction A, this derivation uses only quantities already present in the DGF paper (no new free parameter $\varepsilon$).

The Fokker-Planck equation for the probability distribution $P(q, t)$:

$$\frac{\partial P}{\partial t} = -\frac{\partial}{\partial q}[v(q)P] + \frac{\partial^2}{\partial q^2}[D(q)P] \qquad (7)$$

with:
$$v(q) = \frac{\Gamma_0 k_B}{q}, \quad D(q) = D_0 q(1-q) \frac{\mathfrak{l}^3}{V_S}, \quad D_0 = \frac{1}{2\tau_0}, \quad \Gamma_0 \sim \frac{1}{\tau_0}$$

**Step 1 — Steady-state distribution.**

Setting $\partial P/\partial t = 0$ and integrating once with reflecting boundary conditions ($J = vP - \partial_q(DP) = 0$ at $q = 0, 1$):

$$v(q) P_{\text{eq}}(q) = \frac{d}{dq}[D(q) P_{\text{eq}}(q)] \qquad (8)$$

$$P_{\text{eq}}(q) = \frac{\mathcal{N}}{D(q)} \exp\left(\int_0^q \frac{v(q')}{D(q')} dq'\right) \qquad (9)$$

where $\mathcal{N}$ is a normalization constant.

**Step 2 — Evaluate the integral.**

Define the dimensionless system size:
$$n = \frac{V_S}{\mathfrak{l}^3} = N \qquad (10)$$

Then:
$$D(q) = \frac{q(1-q)}{2\tau_0 n} \qquad (11)$$

$$\frac{v(q)}{D(q)} = \frac{\Gamma_0 k_B / q}{q(1-q)/(2\tau_0 n)} = \frac{2\Gamma_0 k_B \tau_0 n}{q^2(1-q)} \qquad (12)$$

Let $\alpha = 2\Gamma_0 k_B \tau_0 \sim O(1)$ (in natural units where $k_B = 1$, $\Gamma_0 \sim 1/\tau_0$). This is a dimensionless constant of order unity that we cannot compute without a complete microscopic model of the drift.

$$\frac{v(q)}{D(q)} = \frac{\alpha n}{q^2(1-q)} \qquad (13)$$

**Step 3 — The integral.**

$$I(q) = \int_0^q \frac{\alpha n}{q'^2(1-q')} dq' = \alpha n \int_0^q \left(\frac{1}{q'^2} + \frac{1}{q'} + \frac{1}{1-q'}\right) dq' \qquad (14)$$

The $1/q'^2$ term diverges as $q \to 0$, making the integral improper at the lower limit. After regularization (physical cutoff at $q_{\min} = 1/n$, one empty cell in the entire system):

$$I(q) \approx \alpha n \left(\frac{1}{q_{\min}} - \frac{1}{q} + \ln\frac{q(1-q_{\min})}{q_{\min}(1-q)}\right) \qquad (15)$$

The dominant term is $\alpha n / q_{\min} = \alpha n^2$, which is ENORMOUS for macroscopic systems ($n \gg 1$). This means $P_{\text{eq}}(q)$ is exponentially peaked.

**Step 4 — Most probable $q$ and variance.**

The exponent is minimized at the $q$ that maximizes the argument of the exponential (or equivalently, where $v(q) = D'(q)$, which from the steady-state condition means the most probable $q$ satisfies a balance condition). The precise location depends on the competition between drift and diffusion, but the key result is:

$$\boxed{\text{Var}(q) \sim \frac{1}{\alpha n} = \frac{\mathfrak{l}^3}{\alpha V_S}} \qquad (16)$$

For macroscopic systems ($V_S \gg \mathfrak{l}^3$), $q$ is sharply pinned — the system's classicality/quantumness does not fluctuate.

For microscopic systems ($V_S \sim \mathfrak{l}^3$, $n \sim 1$), $q$ undergoes large fluctuations and can explore the full range $[0, 1]$.

### 2.2 Observable Consequence: Fluctuation-Dissipation in the Decoherence Rate

If $q$ controls the local decoherence rate (via the GUP-Lindblad kernel in Section VIII of the DGF paper), then the decoherence rate itself fluctuates. The relative fluctuation amplitude is:

$$\frac{\delta \gamma}{\gamma} \sim \frac{1}{\sqrt{\alpha n}} = \sqrt{\frac{\mathfrak{l}^3}{\alpha V_S}} \qquad (17)$$

**Quantitative prediction:** Repeated measurements of the decoherence rate of a mesoscopic system should show excess variance beyond what is expected from environmental and measurement noise. This excess variance scales as $1/\sqrt{V_S}$.

For a system of volume $V_S = (100\,\text{nm})^3 = 10^{-21}\,\text{m}^3$:
$$\frac{\delta \gamma}{\gamma} \sim \sqrt{\frac{(3.7 \times 10^{-35})^3}{10^{-21}}} \sim \sqrt{5 \times 10^{-83}} \sim 7 \times 10^{-42}$$

This is far too small to observe.

For a system of volume $V_S = (1\,\text{nm})^3 = 10^{-27}\,\text{m}^3$:
$$\frac{\delta \gamma}{\gamma} \sim \sqrt{\frac{5 \times 10^{-104}}{10^{-27}}} \sim \sqrt{5 \times 10^{-77}} \sim 7 \times 10^{-39}$$

Still unobservably small.

**Honest assessment:** Prediction B, while derived entirely from existing DGF quantities, predicts fluctuations that are unobservably small for any system larger than a single Planck cell. This is not a practical prediction.

---

## 3. Prediction C: Homogenization Timescale and the Process A/Process B Crossover

### 3.1 Two Competing Processes

DGF posits two distinct dynamical processes:

- **Process A (Diffusion/Homogenization):** Information flows from high-$q$ to low-$q$ regions, smoothing out spatial variations in $q$. Timescale (from the DGF stability analysis, `dgf_stability.py`):

$$\tau_A = \frac{L^2 q^2}{\mathfrak{l} c} \qquad (18)$$

where $L$ is the characteristic spatial scale of the $q$-variation.

- **Process B (Spontaneous Occupation/Classicalization):** Empty cells spontaneously fill at rate $\varepsilon/\tau_0$, driving the mean $q$ toward zero. Timescale:

$$\tau_B = \frac{\tau_0}{\varepsilon} = \frac{\mathfrak{l}}{\varepsilon c} \qquad (19)$$

### 3.2 The Crossover Scale

The competition between these processes determines whether a system homogenizes before it classicalizes, or vice versa. The crossover occurs when $\tau_A = \tau_B$:

$$\frac{L_c^2 q^2}{\mathfrak{l} c} = \frac{\mathfrak{l}}{\varepsilon c} \quad\Rightarrow\quad \boxed{L_c = \frac{\mathfrak{l}}{q\sqrt{\varepsilon}}} \qquad (20)$$

In terms of the number of cells $N_c = (L_c/\mathfrak{l})^3$:

$$\boxed{N_c = \frac{1}{(q^2 \varepsilon)^{3/2}}} \qquad (21)$$

**Regime behavior:**

| Regime | Condition | Physical behavior |
|--------|-----------|-------------------|
| **Homogenization-dominated** | $N \ll N_c$ | System homogenizes, then uniformly classicalizes. $q$ decreases together everywhere. Smooth quantum-to-classical transition. |
| **Occupation-dominated** | $N \gg N_c$ | Spontaneous occupation outruns diffusion. Classical "islands" nucleate and grow. Inhomogeneous classicalization. |

### 3.3 Observable Signature: Spatial Inhomogeneity of Classicalization

For $N \gg N_c$, DGF predicts that classicalization proceeds inhomogeneously. Different spatial regions of the same system reach $q \approx 0$ at different times. The boundary between quantum and classical regions is a **classicalization front** that propagates at speed:

$$v_{\text{front}} \sim \frac{\mathfrak{l}}{\tau_0} \sqrt{\frac{\varepsilon}{q}} = c \sqrt{\frac{\varepsilon}{q}} \qquad (22)$$

This is a novel, testable prediction: if you prepare a large ($N > N_c$) system in a pure quantum state and measure $q$ locally, you should observe:
1. Spatially correlated decay of $q$ (neighboring cells classicalize together)
2. A propagation speed $v_{\text{front}} < c$ (unless $\varepsilon \sim q$, which is unlikely)
3. Classical "domains" that grow and merge, rather than uniform global decay

### 3.4 Comparison with Standard Models

- **Environmental decoherence:** For a homogeneous environment, decoherence is spatially uniform. No classicalization fronts.
- **Penrose/Diosi:** Gravitational self-energy is a global quantity; decoherence rate is the same everywhere in the system.
- **Continuous spontaneous localization (CSL):** Collapses are spatially uncorrelated (Poisson-distributed in space); no front propagation.

**DGF is the only model predicting spatially coherent classicalization fronts.** This is a qualitative, model-independent discriminator.

### 3.5 Falsifiability

**Falsifiable claim:** For a system with $N > N_c$, the spatial coherence of $q$-decay (measured via spatially resolved decoherence probes) should exhibit domain structure and front propagation, not uniform decay or uncorrelated local collapse.

**Current experimental status:** Spatially resolved decoherence measurements do not yet exist. This prediction is not currently testable but is falsifiable in principle with future technology.

**Honest assessment:** Prediction C requires the parameter $\varepsilon$ (to determine $N_c$ and $v_{\text{front}}$), and the required experimental capability (spatially resolved $q$-measurement) does not exist. However, the qualitative prediction — spatially coherent classicalization fronts — is a distinctive DGF signature that no other model produces, making it a valuable future target.

---

## 4. Prediction D: Density-Dependent Decoherence (The Cleanest Test)

### 4.1 Derivation (Reprise of Prediction A, distilled to its most testable form)

From Eq. (6), the decoherence timescale for an object of mass $M$ and density $\rho$ is:

$$\tau_{\text{DGF}} = \frac{\rho \mathfrak{l}^4}{c \varepsilon M} \qquad (23)$$

The key observable is the **ratio** of decoherence times for two objects of equal mass but different densities. This ratio is independent of $\varepsilon$:

$$\boxed{\frac{\tau(\rho_1, M)}{\tau(\rho_2, M)} = \frac{\rho_1}{\rho_2}} \qquad (24)$$

**This is a parameter-free prediction.** It does not require knowing $\varepsilon$, $\mathfrak{l}$, or any other DGF parameter. It only requires:
1. Two objects of equal mass $M$
2. Different densities $\rho_1, \rho_2$
3. Measured decoherence times $\tau_1, \tau_2$

### 4.2 Experimental Design

**Candidate systems:** Levitated nanoparticles of different materials but equal mass.

| Material | Density $\rho$ (g/cm³) | Radius for $M = 10^{-18}$ kg | $\Delta N$ (spatial cells) |
|----------|------------------------|------------------------------|---------------------------|
| Silica (SiO$_2$) | 2.2 | 48 nm | $\sim 1.1 \times 10^7$ |
| Gold (Au) | 19.3 | 23 nm | $\sim 1.3 \times 10^6$ |
| Polystyrene | 1.05 | 61 nm | $\sim 2.3 \times 10^7$ |

DGF prediction: $\tau_{\text{silica}} / \tau_{\text{gold}} = 2.2/19.3 \approx 0.11$. The silica nanoparticle should decohere about $9\times$ FASTER than the gold nanoparticle of equal mass.

Penrose/Diosi prediction (dipole approximation, $\tau \propto R/GM^2$): $\tau_{\text{silica}} / \tau_{\text{gold}} = R_{\text{silica}}/R_{\text{gold}} = (19.3/2.2)^{1/3} \approx 2.06$. The silica nanoparticle should decohere about $2\times$ SLOWER.

**Direction of the ratio:**
- **DGF:** $\tau_{\text{dense}} > \tau_{\text{diffuse}}$ (denser decoheres slower)
- **Penrose/Diosi:** $\tau_{\text{dense}} < \tau_{\text{diffuse}}$ (denser decoheres faster)
- **Environmental:** $\tau_{\text{dense}} \approx \tau_{\text{diffuse}}$ (if environment similar)
- **Standard QM:** $\tau = \infty$ for both (no intrinsic decoherence)

The sign of the density-dependence of decoherence rate is a **qualitative discriminator** between DGF and all other models.

### 4.3 Falsifiability

**Claim:** For levitated nanoparticles of equal mass but different densities, maintained in identical environmental conditions (same pressure, temperature, trapping laser intensity, photon scattering rate), the measured decoherence time $\tau_{\text{dec}}$ should be:
- **Shorter** for lower-density particles (DGF prediction)
- **Longer** for lower-density particles (Penrose/Diosi prediction)
- **Equal** within error bars (environmental/standard QM prediction)

**Falsification condition:** If $\tau_{\text{diffuse}} > \tau_{\text{dense}}$ (denser decoheres faster), DGF Prediction D is falsified. This would be established by the first statistically significant measurement showing the density-dependence goes the Penrose/Diosi way.

**Experimental feasibility:** Levitated optomechanics experiments (Aspelmeyer group, Vienna; Kamba et al. 2025, Science) can trap nanoparticles of different materials and measure decoherence rates. The challenge is achieving sufficient environmental isolation that the intrinsic decoherence signal exceeds the environmental background. Current experiments are environment-dominated; this prediction tests a regime that requires better isolation than currently available.

**Honest assessment:** This is the cleanest prediction. It requires no free parameters, makes a qualitative (sign-based) claim that distinguishes DGF from all competitors, and is falsifiable in principle. The main obstacle is experimental: current levitated optomechanics experiments have not yet reached the environmental-isolation threshold where intrinsic decoherence would be measurable.

### 4.4 Calibration: Using the Prediction to Measure $\varepsilon$

If the density-ratio prediction (Eq. 24) is confirmed, the absolute decoherence time then provides a measurement of $\varepsilon$:

$$\varepsilon = \frac{\rho \mathfrak{l}^4}{c M \tau_{\text{measured}}} \qquad (25)$$

With $\mathfrak{l} \approx 3.66 \times 10^{-35}$ m, $c = 3.0 \times 10^8$ m/s, for a gold nanoparticle ($\rho = 1.93 \times 10^4$ kg/m³, $M = 10^{-18}$ kg):

$$\varepsilon \approx \frac{1.93 \times 10^4 \times (3.66 \times 10^{-35})^4}{3.0 \times 10^8 \times 10^{-18} \times \tau_{\text{measured}}} \approx \frac{3.5 \times 10^{-135}}{\tau_{\text{measured}}}$$

If $\tau_{\text{measured}} \sim 1$ ms (optimistic for current technology):
$$\varepsilon \sim 3.5 \times 10^{-132}$$

If $\tau_{\text{measured}} \sim 1$ s:
$$\varepsilon \sim 3.5 \times 10^{-135}$$

These are extremely small numbers. If $\varepsilon$ turns out to be this small (or smaller), it raises the question of naturalness: why would the spontaneous occupation probability be fine-tuned to $10^{-132}$? This is a legitimate theoretical concern for the DGF framework.

---

## 5. Summary of Predictions

| Prediction | Requires $\varepsilon$? | Falsifiable? | Distinctive? | Experimental reach |
|------------|------------------------|--------------|--------------|-------------------|
| **A:** Residual decoherence floor $\gamma = \varepsilon \Delta N / \tau_0$ | Yes | Yes | Yes (volume scaling vs. mass scaling) | Bounds $\varepsilon$ from molecular interferometry |
| **B:** $q$-fluctuation spectrum $\text{Var}(q) \sim 1/N$ | No | In principle | Weakly (all models predict macro stability) | Unobservably small for $N > 1$ |
| **C:** Classicalization fronts, Process A/B crossover at $N_c$ | Yes | Yes (qualitative) | **Strongly** (unique to DGF) | Requires new experimental capability |
| **D:** Density-dependent decoherence $\tau(\rho_1)/\tau(\rho_2) = \rho_1/\rho_2$ | **No** | **Yes** | **Strongly** (opposite sign to Penrose/Diosi) | Current levitated optomechanics |

## 6. The Single Most Important Result: Prediction D

**DGF predicts that for objects of equal mass, denser objects maintain quantum coherence LONGER than diffuse objects.**

This is the opposite of what Penrose and Diosi predict, and it does not depend on knowing $\varepsilon$ or any other free parameter. The ratio $\tau_1/\tau_2 = \rho_1/\rho_2$ is a direct, parameter-free consequence of the DGF assumption that decoherence is driven by the number of Planck cells that differ between superposition branches ($\Delta N$), which in turn is proportional to the physical volume of the superposition divided by the cell volume.

The sign of the density dependence of decoherence rate is the cleanest experimental discriminator between DGF and all competing models of intrinsic decoherence.

---

## 7. Critical Caveats

### 7.1 The $\Delta N$ Problem

All predictions that depend on $\Delta N$ (Predictions A, C, D) assume that $\Delta N$ is proportional to the geometric volume of the superposition difference. This is the most natural reading of "number of Planck cells that differ between branches," but it is not the only possible reading.

If instead $\Delta N$ scales with the *mass* of the system (each Planck-mass unit contributes one differing cell regardless of spatial volume), then $\tau_{\text{DGF}} \propto 1/M$, density dependence vanishes, and Prediction D's distinctive density-ratio test fails.

The question of what exactly determines $\Delta N$ is **not resolved in the current DGF formulation**. This ambiguity is the single largest obstacle to making clean quantitative predictions.

### 7.2 The Free Parameter $\varepsilon$

Process B's rate parameter $\varepsilon$ does not appear in the DGF paper's Fokker-Planck equation. It has been absorbed into the drift coefficient $v(q) = \Gamma_0 k_B/q$. To the extent that $\Gamma_0$ can be computed from first principles (the paper estimates $\Gamma_0 \sim 1/\tau_0$), the decoherence rate is in principle fixed. But the current derivation of $\Gamma_0$ is dimensional analysis, not a microscopic calculation.

If $\Gamma_0$ is indeed $\sim 1/\tau_0 \sim 10^{43}$ s$^{-1}$, then for any $\Delta N > 1$, the predicted decoherence is effectively instantaneous. This contradicts all observations of quantum coherence in mesoscopic systems. The framework requires either:
1. $\Gamma_0 \ll 1/\tau_0$ (suppressed by many orders of magnitude)
2. $\Delta N \ll V_S/\mathfrak{l}^3$ (only a tiny fraction of cells participate)
3. A different decoherence mechanism not captured by $\gamma = \varepsilon \Delta N/\tau_0$

### 7.3 The Observability Gap

All four predictions face a severe observability gap: the predicted effects are either (a) unobservably small for systems larger than a few Planck cells (Prediction B), (b) require extreme environmental isolation not yet achieved (Predictions A, D), or (c) require experimental capabilities that do not exist (Prediction C).

This is not unique to DGF — Penrose, Diosi, and CSL face similar challenges. But it means that experimental verification or falsification of any DGF prediction is years to decades away, not imminent.

---

## Appendix: Derivation of the Homogenization Timescale $\tau_A$

From the discrete flux form in `dgf_stability.py`:

$$J_{i \to i+1} = \frac{q_{i+1} - q_i}{q_i q_{i+1}}$$

For small gradients ($q_{i+1} \approx q_i + \Delta x \cdot \partial_x q$):

$$J \approx -\frac{\Delta x}{q^2} \partial_x q$$

The continuity equation $\partial_t q = -\partial_x J$ gives:

$$\partial_t q = \partial_x\left(\frac{\Delta x}{q^2} \partial_x q\right) = \frac{\Delta x}{q^2} \partial_x^2 q - \frac{2\Delta x}{q^3} (\partial_x q)^2$$

This is a nonlinear diffusion equation with effective diffusivity $D_{\text{eff}} = \Delta x / q^2$. In Planck units ($\Delta x = \mathfrak{l}$, time step = $\tau_0$):

$$D_{\text{eff}} = \frac{\mathfrak{l}^2}{\tau_0 q^2}$$

For a system of characteristic size $L$, the homogenization timescale is:

$$\tau_A = \frac{L^2}{D_{\text{eff}}} = \frac{L^2 q^2 \tau_0}{\mathfrak{l}^2} = \frac{L^2 q^2}{\mathfrak{l} c}$$

This is Eq. (18) in the main text, and matches the timescale computed in `dgf_stability.py` line 394.

Note: this derivation confirms that Process A (diffusion/homogenization) has the scaling $\tau_A \propto L^2$ — it slows down quadratically with system size. Process B (spontaneous occupation) has $\tau_B \propto L^0$ — it is independent of system size. This competition is the physical origin of the crossover scale $L_c$ (Eq. 20).
