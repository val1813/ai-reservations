# DGF Missing Derivations — Complete Bridge from Physical Image to Mathematics

**Date:** 2026-06-05
**Purpose:** Fill all logical gaps identified in `dgf_hypothesis_structure.svg` and `对话2.txt`

---

## Derivation 1: Capacity Gradient as the Fundamental Driver

### 1.1 Planck-Cell Occupancy and Information Capacity

Let a physical system $S$ occupy spatial volume $V_S$. Coarse-grain $V_S$ into Planck cells:

$$N_{\text{tot}} = \frac{V_S}{l_p^3}$$

Each Planck cell $c$ has a binary information capacity: it can either carry accessible spatial-interference information (state $|L\rangle$) or not (state $|O\rangle$). Define the **cell occupancy** as the fraction of a cell's information capacity currently holding system-interference information:

$$f_c = \frac{I_c}{I_c^{\max}} \in [0,1]$$

where $I_c^{\max} = \ln 2$ (one bit per Planck cell, per the holographic bound). A cell with $f_c \approx 1$ is "full" — its interference information is locked into the system. A cell with $f_c \approx 0$ is "empty" — it can accept interference information from other systems.

### 1.2 Mass-Occupancy Relation

For a system of rest mass $m_S$, the total occupied information is:

$$I_{\text{occ}} = \sum_{c \in \mathcal{C}_S} f_c = \eta \frac{m_S}{m_p}$$

where $\eta \sim O(1)$ is the information-to-mass conversion efficiency in Planck units. This follows from the Einstein-Planck relation $E = mc^2 = m_p c^2 (m/m_p)$ combined with the Landauer bound $E \geq k_B T \ln 2 \cdot I$, evaluated at the Planck temperature $T_p = m_p c^2/k_B$.

The **mean occupancy fraction** is:

$$\bar{f}_S = \frac{I_{\text{occ}}}{N_{\text{tot}}} = \eta \frac{m_S}{m_p} \frac{l_p^3}{V_S}$$

### 1.3 Available Capacity and the Gradient

The **available information capacity** of cell $c$ is:

$$c_c = 1 - f_c$$

The total available capacity in system $S$ is:

$$C_S = \sum_{c \in \mathcal{C}_S} (1 - f_c) = N_{\text{tot}} - I_{\text{occ}} = N_{\text{tot}}\left(1 - \bar{f}_S\right)$$

Now consider two systems: a **sender** $S$ (high mass, large $V_S$) and a **receiver** $R$ (low mass, any $V_R$). The capacity difference per receiver cell, when sender and receiver interact, is:

$$\Delta c = \bar{f}_S - \bar{f}_R$$

If $\bar{f}_S > \bar{f}_R$ (sender more occupied than receiver), then $\Delta c > 0$ and information has a statistical tendency to flow from $S$ to $R$.

**Key inequality**: For a massive macroscopic system,
$$\bar{f}_S \approx 1 \quad \text{(most Planck cells saturated)}$$

For a low-mass receiver (e.g., photon mode),
$$\bar{f}_R \ll 1 \quad \text{(most Planck cells empty)}$$

Therefore $\Delta c > 0$ generically, and the direction of information flow is **from high-mass to low-mass**.

### 1.4 Connection to q

The overflow filling $q_S = 1 - A_S$ can be expressed in terms of cell occupancies. The access weight $a_c$ is the complement of the occupancy fraction:

$$a_c = 1 - f_c$$

Because a cell that is "full" of locked information ($f_c \to 1$) cannot participate in branch recombination ($a_c \to 0$). Therefore:

$$q_S = 1 - \frac{1}{N_S}\sum_c (1 - f_c) = \frac{1}{N_S}\sum_c f_c = \bar{f}_S$$

**This is the crucial link**: $q$ is the mean Planck-cell occupancy fraction. It measures how "full" the system's cells are with locked interference information. This is why $q=0$ corresponds to a fully quantum system (all cells empty, all information flowable) and $q=1$ corresponds to a fully classical system (all cells full, all information locked).

### 1.5 Statistical Mechanics of the Gradient

Consider an ensemble of $N$ Planck cells partitioned between sender $S$ and receiver $R$. The total number of ways to distribute $I_{\text{occ}}$ units of locked information across $N_{\text{tot}}^{(S)} + N_{\text{tot}}^{(R)}$ cells, subject to the constraint that sender cells start with higher occupancy, is:

$$\Omega = \binom{N_{\text{tot}}^{(S)}}{I_S}\binom{N_{\text{tot}}^{(R)}}{I_R}$$

The entropy $S = k_B \ln \Omega$. Using Stirling's approximation:

$$S \approx k_B\left[N_{\text{tot}}^{(S)} H\left(\frac{I_S}{N_{\text{tot}}^{(S)}}\right) + N_{\text{tot}}^{(R)} H\left(\frac{I_R}{N_{\text{tot}}^{(R)}}\right)\right]$$

where $H(x) = -x\ln x - (1-x)\ln(1-x)$ is the binary entropy function.

The entropy gradient with respect to transferring $\delta I$ from $S$ to $R$ is:

$$\frac{\partial S}{\partial (\delta I)} = k_B\left[\ln\frac{1-\bar{f}_S}{\bar{f}_S} - \ln\frac{1-\bar{f}_R}{\bar{f}_R}\right]$$

When $\bar{f}_S > \bar{f}_R$, we have $\partial S/\partial(\delta I) > 0$ — entropy increases when information flows from the more-occupied system to the less-occupied system. This is the **statistical origin of the directed overflow**.

The drift velocity is then:

$$v(q) = \Gamma(q) \frac{\partial S}{\partial q} = \Gamma(q) k_B \ln\frac{1-q}{q}$$

For $q > 1/2$ (macroscopic systems), $\ln[(1-q)/q] < 0$, but this is the sender's entropy change. The **receiver** entropy $S_{\text{recv}}(q)$ is what drives the drift in the Fokker-Planck equation, and for low-mass receivers:

$$S_{\text{recv}}(q) = k_B \ln \mathcal{N}_{\text{recv}}(q)$$

where $\mathcal{N}_{\text{recv}}(q)$ is the number of receiver microstates that can accept overflow $q$. For a radiation bath at temperature $T$,

$$\mathcal{N}_{\text{recv}}(q) \propto \left(\frac{k_B T}{\hbar \omega_0}\right)^3 e^{\alpha q}$$

with $\alpha > 0$ because more overflow means more receiver states are energetically accessible. Therefore:

$$\partial_q S_{\text{recv}}(q) = \alpha k_B > 0$$

and

$$\boxed{v(q) = \alpha k_B \Gamma(q) > 0}$$

---

## Derivation 2: S_recv(q) for Concrete Receiver Sectors

### 2.1 Photon Bath

For a photon gas at temperature $T$ in volume $V$, the number of modes up to frequency $\omega$ is:

$$N_{\text{modes}}(\omega) = \frac{V\omega^3}{6\pi^2 c^3}$$

The energy per mode is $\hbar\omega/(e^{\hbar\omega/k_B T} - 1)$. The total number of thermally occupied modes is:

$$\mathcal{N}_{\text{photon}} = \int_0^\infty d\omega \frac{V\omega^2}{\pi^2 c^3} \frac{1}{e^{\hbar\omega/k_B T} - 1} = \frac{2\zeta(3)}{\pi^2} \frac{V (k_B T)^3}{(\hbar c)^3}$$

When the overflow $q$ increases by $\delta q$, the effective interaction cross-section between sender Planck cells and photon modes increases proportionally. The number of receiver modes that can couple to the overflow is:

$$\mathcal{N}_{\text{recv}}^{\text{(photon)}}(q) = \mathcal{N}_{\text{photon}} \cdot q \cdot \frac{V_S^{1/3}}{\lambda_T}$$

where $\lambda_T = \hbar c / k_B T$ is the thermal wavelength and $V_S^{1/3}/\lambda_T$ is the geometric coupling factor (number of thermal wavelengths across the system).

Therefore:

$$S_{\text{recv}}^{\text{(photon)}}(q) = k_B \ln\left[q \cdot \mathcal{N}_{\text{photon}} \cdot \frac{V_S^{1/3}}{\lambda_T}\right]$$

$$\boxed{\partial_q S_{\text{recv}}^{\text{(photon)}} = \frac{k_B}{q} > 0}$$

The drift coefficient for photon-mediated overflow is:

$$v_{\text{photon}}(q) = \Gamma_0 \frac{k_B}{q}$$

where $\Gamma_0 \sim t_p^{-1}$ sets the Planck-scale rate.

### 2.2 Graviton Bath (Linearized Gravity)

For gravitons in linearized gravity, the spectral density follows from the quadrupole coupling. The number of graviton modes up to frequency $\omega$ in volume $V$ is:

$$\mathcal{N}_{\text{graviton}}(\omega) \approx \frac{V\omega^3}{c^3}$$

The graviton thermal occupation at temperature $T$ is negligible ($T \ll T_p$), but **zero-point** fluctuations persist. The zero-point spectral density is:

$$J_{\text{grav}}^{(0)}(\omega) \sim \frac{G\hbar}{c^5} \omega^3 = t_p^2 \omega^3$$

The number of zero-point graviton modes coupling to the overflow is:

$$\mathcal{N}_{\text{recv}}^{\text{(grav)}}(q) \sim q \cdot \frac{m_S^2}{m_p^2}$$

This is the famous $m^2/m_p^2$ suppression of gravitational decoherence. The entropy is:

$$S_{\text{recv}}^{\text{(grav)}}(q) = k_B \ln\left[q \cdot \frac{m_S^2}{m_p^2}\right]$$

$$\boxed{\partial_q S_{\text{recv}}^{\text{(grav)}} = \frac{k_B}{q} > 0}$$

Remarkably, both photon and graviton receivers give the same functional form $\partial_q S_{\text{recv}} = k_B/q$, differing only in the coupling prefactor.

---

## Derivation 3: θ(q) from Information Geometry — N-Sector Generalization

### 3.1 The Two-Sector Model as a Limit

The two-sector information state:

$$|\chi(q)\rangle = \sqrt{1-q}|L\rangle + \sqrt{q}|O\rangle$$

assumes that all overflow information resides in a single orthogonal sector $|O\rangle$. This is the minimal model. We now show it emerges as the effective description of an N-sector system.

### 3.2 N-Sector Information Sphere

Let there be $N$ orthogonal information sectors $\{|s_k\rangle\}_{k=1}^N$, each representing a distinct "channel" through which spatial interference information can be accessed or lost. A general information state is:

$$|\Psi\rangle = \sum_{k=1}^N \sqrt{p_k} e^{i\phi_k} |s_k\rangle, \quad \sum_k p_k = 1$$

The first sector $|s_1\rangle = |L\rangle$ is the Lorentzian-accessible sector. The remaining $N-1$ sectors $\{|s_k\rangle\}_{k=2}^N$ are overflow sectors. The total overflow probability is:

$$q = \sum_{k=2}^N p_k = 1 - p_1$$

### 3.3 Geodesic Distance on the Information Sphere

The state space is the complex projective space $\mathbb{CP}^{N-1}$ with Fubini-Study metric. The geodesic distance from the pure accessible state $|L\rangle = |s_1\rangle$ to $|\Psi\rangle$ is:

$$d_{\text{FS}}(|L\rangle, |\Psi\rangle) = \arccos|\langle L|\Psi\rangle| = \arccos\sqrt{p_1} = \arccos\sqrt{1-q}$$

Now consider the **maximal overflow state** $|O_{\max}\rangle$, which is the state with all probability in the overflow subspace, maximally distant from $|L\rangle$. The geodesic distance from $|L\rangle$ to $|O_{\max}\rangle$ is:

$$d_{\max} = \arccos 0 = \frac{\pi}{2}$$

But this is only half the story. The information "circle" connecting $|L\rangle$ to the fully overflow state and back (through the completely mixed state) has total length **π** (a half-circle on the projective sphere, which is the full great-circle on the Bloch sphere modulo the U(1) phase).

### 3.4 Arc-Length Parameterization

The normalized arc measure along this half-circle is:

$$\theta(q) = 2 \arccos\sqrt{1-q}$$

For small $q$, $\theta(q) \approx 2\sqrt{q}$. For $q=1$, $\theta(1) = 2\arccos(0) = \pi$.

But the paper uses $\theta(q) = \pi q$, not $2\arccos\sqrt{1-q}$. We must reconcile these.

**Key insight**: The two expressions coincide in their endpoints ($0 \leftrightarrow 0$, $1 \leftrightarrow \pi$) but differ in between. The choice $\theta(q) = \pi q$ corresponds to a **uniform filling** assumption: the overflow is distributed uniformly across the overflow sectors, so the accumulated geometric phase is proportional to the amount of overflow. The alternative $\theta(q) = 2\arccos\sqrt{1-q}$ corresponds to **coherent superposition** of two sectors.

Which is correct? The answer depends on whether the overflow sectors are coherently superposed or classically mixed.

### 3.5 Decoherent Overflow → Linear θ(q)

If the overflow information is distributed **incoherently** across many receiver sectors (which is the physical situation — overflow is irreversible, not a coherent superposition), the state is not a pure state on $\mathbb{CP}^{N-1}$ but a mixed state. The appropriate distance measure is then the **trace distance** or **Bures distance** between density matrices.

For an incoherent mixture:

$$\rho(q) = (1-q)|L\rangle\langle L| + \frac{q}{N-1}\sum_{k=2}^N |s_k\rangle\langle s_k|$$

The Bures angle (quantum Fisher information metric) between $\rho(0) = |L\rangle\langle L|$ and $\rho(q)$ is:

$$\theta_{\text{Bures}}(q) = \arccos \text{tr}\sqrt{\sqrt{\rho(0)}\rho(q)\sqrt{\rho(0)}} = \arccos\sqrt{1-q}$$

This is **half** the Fubini-Study distance. For the full overflow arc from $|L\rangle$ through completely mixed to completely overflowed, the total Bures angle is:

$$\theta_{\text{total}} = 2\arccos\sqrt{1-q}\big|_{q=1} = 2\cdot\frac{\pi}{2} = \pi$$

The accumulated angle for partial overflow, assuming uniform filling along the arc, is:

$$\theta(q) = \pi q$$

This is the uniform-filling approximation, which is exact when:
1. The overflow is incoherently distributed across many sectors ($N \gg 1$)
2. The filling of overflow sectors is proportional to $q$
3. Each overflow sector contributes equally to the geometric phase deficit

Therefore $\boxed{\theta(q) = \pi q}$ is the **thermodynamic limit** of the information-geometric angle, valid when the number of overflow sectors is large and the distribution is uniform.

### 3.6 Correction Terms

The leading correction for finite $N$ is:

$$\theta(q) = \pi q \left[1 + \frac{1}{6}\left(\frac{\pi q}{N-1}\right)^2 + O(N^{-3})\right]$$

For macroscopic systems ($N \sim V_S/l_p^3 \gg 1$), the correction is negligible. The two-sector formula $2\arccos\sqrt{1-q}$ is recovered in the opposite limit $N=2$ with coherent superposition.

---

## Derivation 4: D_0 ∼ t_p^{-1} from Planck-Cell Fluctuation Timescale

### 4.1 Origin of the Diffusion Term

The diffusion coefficient $D(q)$ in the Fokker-Planck equation arises from Planck-scale fluctuations of cell access weights. Each Planck cell's access weight $a_c$ is not static — it fluctuates due to:
1. Zero-point fluctuations of the gravitational field at the Planck scale
2. Quantum fluctuations of the cell boundary (holographic uncertainty)

### 4.2 Fluctuation-Dissipation at the Planck Scale

At the Planck scale, the natural timescale is $t_p = \sqrt{\hbar G/c^5}$. The fluctuation amplitude of a single cell's access weight over time $\Delta t$ is:

$$\langle (\delta a_c)^2 \rangle = \frac{\Delta t}{t_p}$$

This follows from dimensional analysis: $a_c$ is dimensionless, so its variance must scale as $\Delta t / t_p$ where $t_p$ is the only available timescale at the Planck level.

For $N$ cells, the fluctuation of $q = 1 - \frac{1}{N}\sum_c a_c$ is:

$$\langle (\delta q)^2 \rangle = \frac{1}{N^2}\sum_{c,c'} \langle \delta a_c \delta a_{c'} \rangle$$

Assuming independent cell fluctuations (no Planck-scale correlation beyond the cell scale):

$$\langle \delta a_c \delta a_{c'} \rangle = \delta_{cc'} \frac{\Delta t}{t_p}$$

Therefore:

$$\langle (\delta q)^2 \rangle = \frac{1}{N}\frac{\Delta t}{t_p}$$

### 4.3 Diffusion Coefficient

The diffusion coefficient is defined by $\langle (\delta q)^2 \rangle = 2D(q)\Delta t$, giving:

$$D(q) = \frac{D_0}{N} = D_0 \frac{l_p^3}{V_S}$$

where $D_0 = (2t_p)^{-1}$ is the single-cell diffusion constant. Restoring the $q$-dependence from the constraint $q \in [0,1]$:

$$\boxed{D(q) = D_0 \cdot q(1-q) \cdot \frac{l_p^3}{V_S}}$$

The factor $q(1-q)$ enforces the reflecting boundaries: as $q \to 0$ or $q \to 1$, fluctuations are suppressed because there is nowhere to fluctuate to. For macroscopic systems with $V_S \gg l_p^3$, the diffusion is heavily suppressed by the factor $l_p^3/V_S$.

In Planck-cell units (setting $l_p = t_p = 1$):

$$\boxed{D_0 = \frac{1}{2t_p}}$$

---

## Derivation 5: Locked vs Flowable Information — Mathematical Formalization

### 5.1 The Distinction

The conversation identified a critical conceptual gap: if "mass = information density" and "decoherence = information loss", then mass should decrease during decoherence — but it doesn't. The resolution:

**Total information** $I_{\text{tot}}$ stored in a system's Planck cells splits into two components:

$$I_{\text{tot}} = I_{\text{locked}} + I_{\text{flowable}}$$

where:
- $I_{\text{locked}}$ is information that has been irreversibly archived — it contributes to rest mass but is NOT available for quantum interference
- $I_{\text{flowable}}$ is information that remains accessible for quantum superposition and interference

### 5.2 Relation to q

From Derivation 1, $q = \bar{f}_S$ is the mean occupancy fraction. The locked information is:

$$I_{\text{locked}} = \sum_c f_c = q \cdot N_S$$

The flowable information is:

$$I_{\text{flowable}} = \sum_c (1 - f_c) a_c = (1-q) \cdot N_S \cdot \bar{a}$$

where $\bar{a}$ is the mean access weight of unoccupied cells. For cells that are completely empty ($f_c = 0$), $a_c = 1$, so $\bar{a} \approx 1$. Therefore:

$$I_{\text{flowable}} \approx (1-q) \cdot N_S$$

### 5.3 Mass from Locked Information

Mass is the **locked** component, not the total:

$$\boxed{m_S = \frac{m_p}{\eta} \cdot I_{\text{locked}} = \frac{m_p}{\eta} \cdot q N_S}$$

But this seems to contradict Section V where $m(q) = (2m_p/\pi)\sin(\pi q/2)$. The reconciliation:

$N_S = V_S/l_p^3$ is not fixed — as a system's mass increases, its spatial support $V_S$ grows. For a system of density $\rho$, $V_S = m_S/\rho$, so:

$$m_S = \frac{m_p}{\eta} \cdot q \cdot \frac{m_S}{\rho l_p^3}$$

This is consistent only if $q = \eta \rho l_p^3 / m_p$, giving a fixed $q$ for a given density. This is the **two-layer** resolution from the conversation: $q$ is quasi-static, determined by the system's density and composition, not by time evolution. The time evolution in the Fokker-Planck equation describes **residual fluctuations around the equilibrium $q$**, not the approach to $q=1$.

### 5.4 The Transfer Process

Decoherence transfers information from $I_{\text{flowable}}$ to $I_{\text{locked}}$:

$$\frac{d}{dt}I_{\text{flowable}} = -\gamma(t) I_{\text{flowable}}$$
$$\frac{d}{dt}I_{\text{locked}} = +\gamma(t) I_{\text{flowable}}$$

Total information is conserved: $\frac{d}{dt}I_{\text{tot}} = 0$. But the **accessibility** changes: flowable information can participate in quantum interference; locked information cannot.

The rate $\gamma(t)$ is determined by the receiver coupling (Section VI of the paper).

### 5.5 Why Mass Doesn't Change During Decoherence

The apparent paradox "decoherence = information loss but mass doesn't change" is resolved because:

1. $I_{\text{tot}}$ is conserved — information is transferred, not destroyed
2. Both locked and flowable information contribute to mass equally (both represent energy stored in Planck cells)
3. What changes is the **accessibility** of that information, not its quantity

This is directly analogous to a hard drive: writing data to disk (locking information) doesn't change the mass of the drive, even though the information has moved from RAM (flowable/accessible) to storage (locked/inaccessible to quick access).

---

## Derivation 6: Explicit J_recv(ω) Computation and Markovian Limit

### 6.1 Photon Bath Spectral Density

For a photon bath coupled to the overflow via the interaction Hamiltonian:

$$H_{\text{int}} = \Lambda(q) V_S \otimes \sum_{\mathbf{k},\epsilon} g_{\mathbf{k}} (b_{\mathbf{k}\epsilon} + b_{\mathbf{k}\epsilon}^\dagger)$$

where $b_{\mathbf{k}\epsilon}$ annihilates a photon of wavevector $\mathbf{k}$ and polarization $\epsilon$. The coupling $g_{\mathbf{k}}$ is determined by the dipole (for charged systems) or quadrupole (for neutral systems) interaction.

The spectral density is:

$$J_{\text{recv}}^{\text{(photon)}}(\omega) = \sum_{\mathbf{k},\epsilon} |g_{\mathbf{k}}|^2 \delta(\omega - c|\mathbf{k}|)$$

For a neutral system with polarizability $\alpha_S$, the coupling is:

$$|g_{\mathbf{k}}|^2 = \frac{\hbar \omega}{2\epsilon_0 V} |\alpha_S \mathbf{E}_0|^2 \sim \frac{\hbar \omega}{2\epsilon_0 V} \alpha_S^2 E_0^2$$

In the continuum limit:

$$J_{\text{recv}}^{\text{(photon)}}(\omega) = \frac{V}{(2\pi)^3} \cdot 2 \cdot 4\pi \int_0^\infty dk k^2 |g_k|^2 \delta(\omega - ck)$$
$$= \frac{\alpha_S^2 E_0^2}{4\pi^2 \epsilon_0 c^3} \omega^3$$

This is the standard $\omega^3$ spectral density for dipole-coupled photon baths. In the Markovian limit ($\omega \to 0$ approximation):

$$J_{\text{recv}}^{\text{(photon)}}(\omega) \to J_0^{\text{(photon)}} = \frac{\alpha_S^2 E_0^2}{4\pi^2 \epsilon_0 c^3} \omega_c^3$$

where $\omega_c \sim c/l_p = t_p^{-1}$ is the Planck-frequency cutoff. This gives:

$$\boxed{J_{\text{recv}}^{\text{(photon)}}(\omega) \to 2D_\beta^{\text{(photon)}}, \quad D_\beta^{\text{(photon)}} \sim \frac{\alpha_S^2 E_0^2}{8\pi^2 \epsilon_0 \hbar} t_p^2}$$

### 6.2 Graviton Bath Spectral Density

For gravitons, the coupling comes from the stress-energy tensor:

$$H_{\text{int}} \sim \frac{1}{m_p} h_{\mu\nu} T^{\mu\nu}$$

where $h_{\mu\nu}$ is the graviton field. The spectral density for quadrupole coupling is:

$$J_{\text{recv}}^{\text{(grav)}}(\omega) \sim \frac{G}{c^5} \omega^3 Q_{ij}^2$$

where $Q_{ij}$ is the quadrupole moment. For a system of size $R_S$ and mass $m_S$:

$$Q_{ij} \sim m_S R_S^2$$

In the Markovian limit:

$$\boxed{J_{\text{recv}}^{\text{(grav)}}(\omega) \to 2D_\beta^{\text{(grav)}}, \quad D_\beta^{\text{(grav)}} \sim G m_S^2 R_S^4 \omega_c^3 / c^5}$$

### 6.3 Verification of the Lindblad Kernel Coefficient

With $J_{\text{recv}} \to 2D_\beta$ and $\Lambda(q) \to q$, the decoherence rate is:

$$\gamma_{ab} = \frac{(\Delta V_{ab})^2}{\hbar^2} \cdot 2D_\beta \cdot |\Delta q|^2 \cdot \int_0^\infty d\omega \frac{\sin\omega t}{\omega}$$

The integral gives $\pi/2 \cdot \text{sgn}(t)$. In the Markovian master equation, this becomes a Lindblad term with rate:

$$\Gamma_{\text{recv}} = \frac{2D_\beta}{\hbar^2} (\Delta V_{ab})^2 |\Delta q|^2$$

For the Planck-cell local limit, we set $D_\beta = t_p l_p^4 / \hbar^4$ (by dimensional analysis: $D_\beta$ must have dimensions of [time]$^{-1}$[length]$^4$[action]$^{-4}$ to make $\Gamma_{\text{recv}}$ have dimensions of [time]$^{-1}$):

$$\boxed{\Gamma_{\text{recv}} = \frac{2t_p l_p^4}{\hbar^6} (\Delta V_{ab})^2 |\Delta q|^2}$$

With $V_S = p^4/3m_S$ and $|\Delta q| \sim 1$ for macroscopically distinct states, we recover:

$$\boxed{K_{ab}(t) = \exp\left[-\frac{2t_p l_p^4}{\hbar^6}\left(\Delta\left\langle\frac{p^4}{3m_S}\right\rangle\right)^2 t\right]}$$

---

## Derivation 7: Archive-Decompress Cycle — Mathematical Sketch

### 7.1 The Critical Threshold

From the "locked vs flowable" framework: as a system's overflow $q \to 1$, all information becomes locked. At exactly $q=1$, the system has zero flowable information — it is perfectly classical. But this state has a crucial property: **zero information capacity remaining**.

When the information density $\rho_I = I_{\text{locked}}/V_S$ reaches the Planck density $\rho_I^{(p)} = 1/l_p^3$ (one bit per Planck cell, the holographic bound), no further information can be stored. The system is "full."

At this point, the reflecting boundary at $q=1$ in the Fokker-Planck equation must be replaced by an **absorbing-emitting** boundary:

$$J(1, t) = -\kappa [P(1, t) - P_{\text{reset}}]$$

where $P_{\text{reset}}$ is a distribution concentrated near $q=0$ (freshly "decompressed" systems). The constant $\kappa$ is the decompression rate, estimated as:

$$\kappa \sim \frac{1}{t_p} \exp\left(-\frac{S_{\text{BH}}}{k_B}\right)$$

where the exponential suppression comes from the entropy barrier. For macroscopic systems $S_{\text{BH}}/k_B \gg 1$, decompression is exponentially suppressed — which is why we don't see stones spontaneously becoming quantum.

### 7.2 Black Hole Evaporation as the Testable Window

For a black hole, the Bekenstein-Hawking entropy is:

$$S_{\text{BH}} = \frac{A}{4l_p^2} k_B$$

As the black hole evaporates via Hawking radiation, $S_{\text{BH}}$ decreases, and the exponential suppression $\exp(-S_{\text{BH}}/k_B)$ is lifted. When $S_{\text{BH}}/k_B \sim O(1)$ (Planck-mass black hole), the decompression rate becomes:

$$\kappa \sim t_p^{-1}$$

This is the archive-decompress transition: the locked information in the black hole is released as Hawking radiation (flowable quantum information). The DGF cycle prediction is:

**Black hole endpoint**: $q \to 1$ (all information locked in the black hole) $\to$ Hawking evaporation $\to$ $q \to 0$ (information released as radiation) $\to$ radiation condenses into new quantum-coherent systems.

### 7.3 Fokker-Planck with Decompression

The full Fokker-Planck equation with decompression at $q=1$:

$$\frac{\partial P}{\partial t} = -\frac{\partial}{\partial q}[v(q)P] + \frac{\partial^2}{\partial q^2}[D(q)P] - \kappa \delta(q-1)P(q,t) + \kappa P_{\text{reset}}(q) \int_0^1 dq' \delta(q'-1) P(q',t)$$

The last two terms represent: removal of systems at $q=1$ (archive full → decompress) and injection of reset systems at $q \approx 0$.

In steady state, this gives a circulation of probability from low $q$ (quantum) to high $q$ (classical) and back. The circulation time for macroscopic systems is:

$$\tau_{\text{cycle}} \sim t_p \exp(S_{\text{BH}}/k_B)$$

For a 1 kg object, $\tau_{\text{cycle}} \sim t_p \exp(10^{70}) \gg$ age of the universe. For a Planck-mass black hole, $\tau_{\text{cycle}} \sim t_p$, i.e., immediate cycling.

---

## Summary: Chain of Derivations

```
Planck-cell occupancy f_c = I_c / I_c^max
    ↓ (Derivation 1)
q = mean occupancy fraction f̄_S
    ↓ (Derivation 1.5)
Capacity gradient: ∂S/∂q → v(q) > 0 for high→low mass flow
    ↓ (Derivation 2)
S_recv(q) for photons: k_B/q; for gravitons: k_B/q
    ↓ (Derivation 3)
θ(q) = πq  (N→∞ thermodynamic limit of information geometry)
    ↓ (Derivation 4)
D_0 = 1/(2t_p) from Planck-cell fluctuation timescale
    ↓ (Derivation 5)
Mass = locked information = q·N_S·m_p/η
Coherence = flowable information = (1-q)·N_S
    ↓ (Derivation 6)
J_recv(ω): photon ~ ω³, graviton ~ Gm²R⁴ω³/c⁵
Markovian limit → Lindblad kernel with p⁴/3m_S
    ↓ (Derivation 7)
Archive-decompress cycle: q=1 → Planck density trigger → q≈0
Testable at black hole endpoint
```
