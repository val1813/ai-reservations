# Supplemental Material
## Macrocosmic Decoherence as Directed Spatial-Information Overflow

**Huang Zhongchang**  
Independent Researcher, Nanjing, China

---

## S1. Microscopic Definition of Cell Access

Let \(V_S\) be the spatial support of system \(S\).  Partition it into Planck cells
\[
\mathcal C_S=\{c: c\subset V_S,\ {\rm Vol}(c)=l_p^3\}.
\]
For each cell define an access weight
\[
a_c=\frac{\mathcal V_c}{\mathcal V_c^{\rm max}},
\qquad
0\le a_c\le1,
\]
where \(\mathcal V_c\) is the local branch-recombination visibility associated with that cell.  Operationally, \(a_c=1\) means that the cell's spatial phase information can be reintroduced into the system branch; \(a_c=0\) means the branch cannot recover it.

The system accessibility and overflow are
\[
A_S=\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c,
\qquad
q_S=1-A_S.
\]
This solves the circularity problem: \(q\) is computed from local access weights, not inferred from mass.

### S1.3 Operational Surrogate for \(a_c\)

While direct measurement of \(a_c\) at individual Planck cells is beyond current technology, a **coarse-grained surrogate** is operationally accessible.  For a mesoscopic system at density \(\rho\) and temperature \(T\), the local decoherence rate per cell is \(\gamma_c \propto \bar{f}^2 \propto (\rho l_p^3)^2\) (Supplemental S3.2).  The branch-recombination time \(\tau_c\) is set by the timescale for re-establishing phase coherence across the cell, which for a system of size \(R\) is \(\tau_c \sim R/c_s\) where \(c_s\) is the sound speed.  The steady-state access weight is:
\[
a_c^{\rm(ss)} = \frac{1}{1+\gamma_c\tau_c},
\]
which can be estimated from measurable quantities:
\[
\bar{f} \approx \frac{\rho}{m_p/l_p^3} \quad\text{(mean occupancy per Planck cell)},
\qquad
\gamma_c \approx \gamma_0 \bar{f}^2,
\qquad
\tau_c \approx R/c_s.
\]
For a nanoparticle (\(R\sim 100\) nm, \(\rho\sim 10^3\) kg/m\(^3\), \(c_s\sim 10^3\) m/s): \(\bar{f}\sim 10^{-90}\), \(\gamma_c\tau_c \ll 1\), hence \(a_c^{\rm(ss)}\approx 1\) and \(q\approx 0\) — the system remains quantum-coherent, consistent with observed nanoparticle interference [8,9].  For a macroscopic object (\(R\sim 1\) cm, same density): \(\gamma_c\tau_c \gg 1\), \(a_c^{\rm(ss)}\approx 0\), \(q\approx 1\).  The crossover from \(q\approx 0\) to \(q\approx 1\) occurs when \(\gamma_c\tau_c \sim 1\), which for typical solid-state parameters corresponds to \(R\sim 1\,\mu\)m — the mesoscopic scale where quantum-to-classical transition is experimentally observed.

This surrogate provides a **falsifiable link** between the microscopic definition of \(q\) and measurable macroscopic parameters: if the coherence lifetime of a mesoscopic system does not decrease as \(\bar{f}\) (estimated from density) increases, the capacity-gradient mechanism is excluded.  Analogue quantum simulators (ultracold atoms in optical lattices) can directly realize the \(a_c\) → \(q\) mapping by measuring site-resolved coherence via time-of-flight imaging [10,11].

---

## S2. Many-Body Composition

For independent subsystems \(S_i\), accessibility multiplies:
\[
A_{\rm comp}=\prod_i A_i^{w_i},
\qquad
\sum_iw_i=1.
\]
Therefore
\[
q_{\rm comp}=1-\prod_i(1-q_i)^{w_i}.
\]
The logarithmic form is
\[
\log(1-q_{\rm comp})
=\sum_iw_i\log(1-q_i).
\]
This is the natural rule if independent accessibility failures compound multiplicatively.  It also predicts that adding subsystems generally increases overflow unless all added subsystems have \(q_i=0\).

---

## S3. Capacity Gradient as the Fundamental Driver

### S3.1 Planck-Cell Occupancy and Interference Accessibility

Let a system \(S\) occupy spatial volume \(V_S\), partitioned into Planck cells \(c\) of volume \(l_p^3\).  Each cell carries two independent properties:

1. **Occupancy** \(f_c\in[0,1]\): the fraction of the cell's maximum information content currently held by the system (both locked and flowable components).

2. **Interference accessibility** \(a_c\in[0,1]\): the normalized visibility of that cell under a branch-recombination test — i.e., whether the cell's spatial phase information can still participate in quantum interference.

These are **independent axes**.  A cell can have high occupancy AND high accessibility (coherent dense matter, rare outside neutron stars); high occupancy AND low accessibility (decohered macroscopic matter); low occupancy AND high accessibility (quantum vacuum fluctuation); or low occupancy AND low accessibility (overflow deposited in environment).

The overflow filling defined in the main text is:
\[
q_S=1-\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c,
\]
which measures the fraction of cells whose interference information has become inaccessible — regardless of their occupancy.

### S3.2 Why High-Mass Systems Have Low Accessibility

For a system of mass \(m_S\), the number of Planck cells within its spatial support is \(N_S=V_S/l_p^3\).  Each cell interacts with its neighbors via the Hamiltonian flow.  The decoherence rate per cell scales with the local interaction density.  In a high-mass system:

1. **Cell occupancy is high**: more particles per Planck cell → stronger local interactions → faster scrambling of relative phases.
2. **Interaction graph is dense**: each cell couples to many neighbors → information about relative phases diffuses rapidly through the system.

The steady-state accessibility of a cell in a system of mean occupancy \(\bar{f}\) is:
\[
a_c^{\rm(ss)} = \frac{1}{1+\gamma_c\tau_c},
\qquad
\gamma_c \propto \bar{f}^2,
\]
where \(\gamma_c\) is the local decoherence rate (from two-body interactions scaling as \(\bar{f}^2\)) and \(\tau_c\) is the branch-recombination timescale.  For macroscopic densities, \(\gamma_c\tau_c \gg 1\) and \(a_c^{\rm(ss)} \ll 1\): cells are driven to low accessibility by their own interaction density.  This is the microscopic origin of the mass-accessibility correlation: high mass → high occupancy → high interaction rate → low accessibility → high \(q\).

### S3.3 Entropy-Gradient Drift: Why Low-Mass Systems Are Receivers

Given two interacting systems with overflow fillings \(q_S\) (sender, high mass) and \(q_R\) (receiver, low mass), the direction of information overflow is determined by the entropy gradient of the combined system.

Let \(P(q,t)\) be the distribution of overflow fillings across coarse-grained branches.  The directed overflow equation is
\[
\partial_tP=-\partial_q(vP)+\partial_q^2(DP).
\]
The probability current is
\[
J(q,t)=v(q)P-\partial_q[D(q)P],
\]
with reflecting boundaries \(J(0,t)=J(1,t)=0\).

The drift is fixed by the entropy of receiver modes:
\[
v(q)=\Gamma(q)\,\partial_q S_{\rm recv}(q),
\qquad \Gamma(q)\ge0,
\]
where
\[
S_{\rm recv}(q)=k_B\ln\mathcal N_{\rm recv}(q),
\]
and \(\mathcal N_{\rm recv}(q)\) counts receiver microstates able to accept the overflow \(q\).

**Why the receiver entropy, not the sender entropy?**  The sender's information-theoretic entropy \(S_{\rm sender}(q) = N_S k_B H(q)\) (where \(H(q)=-q\ln q-(1-q)\ln(1-q)\) is the binary entropy per cell) has \(\partial_q S_{\rm sender} < 0\) for \(q>1/2\) — a fully classical system (\(q=1\)) returns to a pure state.  If the drift were proportional to the sender's entropy gradient, macroscopic objects would resist further decoherence (\(v<0\)), contrary to observation.  The resolution: decoherence is an **information-flow process driven by the receiver's state-space multiplicity**, not by thermodynamic entropy production.  This is an information-theoretic arrow: information flows from configurations with lower multiplicity (sender's remaining accessible states) to configurations with higher multiplicity (receiver's available states).  The receiver's state count \(\mathcal{N}_{\rm recv}(q)\) grows with \(q\) because more overflow means more receiver modes are coupled, providing an ever-larger multiplicity sink.

This is **analogous to spontaneous emission** in the following limited sense: in spontaneous emission, the transition rate \(\Gamma \propto \rho(E_f) = dN/dE\) is proportional to the density of final states (a receiver-side quantity).  In DGF, \(v(q) \propto \partial_q S_{\rm recv} = k_B \cdot d(\ln\mathcal{N}_{\rm recv})/dq\) is proportional to the logarithmic growth rate of receiver states — a related but distinct quantity.  The analogy is heuristic, not structural: spontaneous emission uses the absolute density of states \(dN/dE\); DGF uses the relative growth rate \(d(\ln\mathcal{N})/dq\).  Both are receiver-side quantities that determine the rate of an irreversible process, but they are different mathematical objects.  The important physical point is that the **direction** of overflow is set by the receiver's multiplicity gradient, not by the sender's entropy gradient.

The Fokker-Planck equation as written is an effective description valid for \(q\) not too close to 0 or 1.  Near \(q=0\), the drift \(v(q)\propto 1/q\) diverges — a known feature of diffusion equations with logarithmic potentials, reflecting the fact that a fully quantum system (\(q=0\)) is an unstable fixed point (any small fluctuation seeds decoherence).  Near \(q=1\), the reflecting boundary condition \(J(1,t)=0\) cannot be simultaneously satisfied with \(v(1)>0\) and \(D(1)=0\) — this is not a bug but a feature: at \(q=1\), the system reaches information saturation and the Fokker-Planck description breaks down.  The proper boundary condition at \(q=1\) is absorbing-emitting, as developed in S11 for the archive-decompress cycle.  The reflecting-boundary Fokker-Planck equation is the effective description for \(0<q<1\); the full theory including \(q=1\) requires the decompression boundary condition of S11.

### S3.4 Explicit \(S_{\rm recv}(q)\) for Photon Receivers

For a photon bath at temperature \(T\) in volume \(V\), the number of thermally occupied modes is:
\[
\mathcal N_{\rm photon}=\frac{2\zeta(3)}{\pi^2}\frac{V(k_B T)^3}{(\hbar c)^3}.
\]
When the overflow \(q\) increases, the effective coupling between sender Planck cells and photon modes grows proportionally.  The number of receiver modes that couple to overflow \(q\) is:
\[
\mathcal N_{\rm recv}^{\rm(photon)}(q)=\mathcal N_{\rm photon}\cdot q\cdot\frac{V_S^{1/3}}{\lambda_T},
\]
where \(\lambda_T=\hbar c/k_B T\) is the thermal wavelength and \(V_S^{1/3}/\lambda_T\) counts thermal wavelengths across the system (geometric coupling factor).  Therefore:
\[
S_{\rm recv}^{\rm(photon)}(q)=k_B\ln q+k_B\ln\!\left(\mathcal N_{\rm photon}\frac{V_S^{1/3}}{\lambda_T}\right),
\]
\[
\boxed{\partial_q S_{\rm recv}^{\rm(photon)}=\frac{k_B}{q}>0.}
\]

### S3.5 Explicit \(S_{\rm recv}(q)\) for Graviton Receivers

For gravitons in linearized gravity, the zero-point spectral density is:
\[
J_{\rm grav}^{(0)}(\omega)\sim\frac{G\hbar}{c^5}\omega^3=t_p^2\omega^3.
\]
The number of zero-point graviton modes coupling to overflow \(q\) in a system of mass \(m_S\) is:
\[
\mathcal N_{\rm recv}^{\rm(grav)}(q)\sim q\cdot\frac{m_S^2}{m_p^2},
\]
where the \(m_S^2/m_p^2\) factor is the famous quadrupole suppression of gravitational decoherence.  Then:
\[
\boxed{\partial_q S_{\rm recv}^{\rm(grav)}=\frac{k_B}{q}>0.}
\]

Remarkably, both photon and graviton receivers give the same functional form \(\partial_qS_{\rm recv}=k_B/q\), differing only in the coupling prefactor \(\Gamma(q)\).  The drift velocity is universally:
\[
\boxed{v(q)=\Gamma(q)\frac{k_B}{q}>0.}
\]

### S3.6 Regularization and Mean Overflow Evolution

The drift \(v(q)=\Gamma(q)k_B/q\) diverges as \(q\to 0\), reflecting the fact that a perfectly coherent system (\(q=0\)) is an unstable fixed point: any infinitesimal fluctuation initiates decoherence.  For physical applications, the divergence is regulated by the finite number of Planck cells:
\[
v_{\rm reg}(q)=\Gamma(q)\frac{k_B}{q+\varepsilon},
\qquad \varepsilon=\frac{l_p^3}{V_S}=N_S^{-1},
\]
where \(N_S=V_S/l_p^3\) is the total number of Planck cells in the system.  For a macroscopic system (\(N_S\sim 10^{99}\)), \(\varepsilon\sim 10^{-99}\) and the regularization is negligible for all \(q\gg\varepsilon\).  For a mesoscopic system (\(N_S\sim 10^{30}\) for a 1 \(\mu\)m grain), \(\varepsilon\sim 10^{-30}\) — still negligible at all accessible q.  Only for truly Planck-scale systems (\(N_S\sim 1\)) does the regularization become important, and in that regime the Fokker-Planck description itself breaks down (individual cell fluctuations dominate).

With the regularization, the mean overflow evolution is:
\[
\frac{d\langle q\rangle}{dt}
=\int_0^1 dq\,v_{\rm reg}(q)P(q,t)>0,
\]
so the mean overflow increases monotonically — the mathematical source of irreversibility.  The drift toward larger \(q\) follows from the statistical fact that low-mass (low-occupancy) systems have exponentially more microstates available to accept overflow information than high-mass (high-occupancy) systems.

---

## S4. Why White Noise Alone Was Insufficient

A zero-mean correlator
\[
\langle\delta q(t)\delta q(t')\rangle=t_p\delta(t-t')
\]
describes fluctuations but not direction.  It contributes to \(D(q)\), not to \(v(q)\).  Irreversibility requires \(v(q)>0\).  The repaired DGF structure is therefore:

\[
\text{entropy-gradient drift }v(q)
+\text{ Planck diffusion }D(q).
\]

The Lindblad kernel arises after tracing receiver modes; the monotonic increase of macrocosmic overflow arises from the drift.

### S4.1 Diffusion Coefficient Derivation

The diffusion term \(D(q)\) originates from Planck-scale fluctuations of cell access weights.  For a single Planck cell, the access weight variance over time \(\Delta t\) is:
\[
\langle(\delta a_c)^2\rangle=\frac{\Delta t}{t_p},
\]
by dimensional analysis (\(a_c\) dimensionless, \(t_p\) the only Planck-scale timescale).  For \(N_S\) independent cells:
\[
\langle(\delta q)^2\rangle=\frac{1}{N_S^2}\sum_{c,c'}\langle\delta a_c\delta a_{c'}\rangle
=\frac{1}{N_S}\frac{\Delta t}{t_p}.
\]
The diffusion coefficient satisfies \(\langle(\delta q)^2\rangle=2D(q)\Delta t\), giving:
\[
D(q)=\frac{D_0}{N_S},\qquad D_0=\frac{1}{2t_p}.
\]
Restoring the \(q(1-q)\) factor that enforces reflecting boundaries at \(q=0,1\):
\[
\boxed{D(q)=\frac{1}{2t_p}\frac{l_p^3}{V_S}\,q(1-q).}
\]
For macroscopic systems (\(V_S\gg l_p^3\)), the diffusion is heavily suppressed, consistent with the quasi-static nature of \(q\) for macroscopic objects.

---

## S5. Information-Geometric Derivation of \(\theta(q)\)

### S5.1 Two-Sector Model

Represent each Planck cell by a two-sector information state
\[
|\chi\rangle
=\sqrt{1-q}|L\rangle+\sqrt q\,|O\rangle.
\]
Here \(|L\rangle\) is Lorentzian-accessible information and \(|O\rangle\) is overflow information.  The Fubini-Study distance from full access is
\[
d_{\rm FS}=\arccos\sqrt{1-q}.
\]

### S5.2 N-Sector Generalization: Why \(\theta(q)=\pi q\)

The two-sector model is the minimal description.  We now show that \(\theta(q)=\pi q\) is the **thermodynamic limit** of the information-geometric angle when the number of overflow sectors is large and overflow is distributed incoherently.  The derivation has three steps: (i) maximum entropy fixes the distribution, (ii) trace distance gives the radial chord, (iii) arc-length doubling gives \(\theta=\pi q\).

Let there be \(N\) orthogonal information sectors: \(|s_1\rangle=|L\rangle\) (accessible) and \(|s_k\rangle_{k=2}^N\) (overflow channels).  A general state is:
\[
|\Psi\rangle=\sum_{k=1}^N\sqrt{p_k}e^{i\phi_k}|s_k\rangle,
\qquad \sum_k p_k=1,
\]
with total overflow \(q=\sum_{k=2}^N p_k\).

**Step 1: Maximum entropy → uniform filling.** The overflow information arrives through \(M \gg 1\) independent decoherence events, each depositing a small amount of phase information into a random overflow sector.  With no preferred sector, the distribution \(\{p_k\}_{k=2}^N\) that maximizes the Shannon entropy \(H=-\sum_{k=2}^N p_k\ln p_k\) subject to \(\sum_{k=2}^N p_k=q\) is the uniform distribution:
\[
p_k=\frac{q}{N-1},\qquad k=2,\ldots,N.
\]
This is the unique maximum-entropy distribution — any non-uniform distribution would imply prior information about which sector is preferred, which does not exist for independent decoherence events.  The physical state is therefore the **incoherent mixture** (random relative phases between sectors):
\[
\rho(q)=(1-q)|L\rangle\langle L|+\frac{q}{N-1}\sum_{k=2}^N|s_k\rangle\langle s_k|.
\]

**Step 2: Trace distance → radial chord.** The Bures angle between \(\rho(0)=|L\rangle\langle L|\) and \(\rho(q)\) is:
\[
\theta_{\rm Bures}(q)=\arccos{\rm tr}\sqrt{\sqrt{\rho(0)}\rho(q)\sqrt{\rho(0)}}
=\arccos\sqrt{1-q},
\]
but this measures the coherent (pure-state) geodesic and is not the physically relevant distance for an incoherent mixture.  For mixed states, the appropriate metric is the **trace distance**:
\[
\|\rho(q)-\rho(0)\|_1={\rm tr}|\rho(q)-\rho(0)|=2q,
\]
where the factor 2 comes from the two extremal eigenvalues (\(-q\) from the \(|L\rangle\) deficit and \(+q/(N-1)\) from each of the \(N-1\) overflow sectors, summing to \(q\) in absolute value in each of the two half-spaces).  Normalizing to the half-circle range \([0,\pi]\):
\[
\theta_{\rm chord}(q)=\frac{\pi}{2}\cdot\frac{1}{2}\|\rho(q)-\rho(0)\|_1
=\frac{\pi}{2}q.
\]

**Step 3: Trace-distance normalization → \(\theta=\pi q\).** The trace distance \(d_{\rm tr}(q) = \|\rho(q)-\rho(0)\|_1 = 2q\) ranges from 0 to 2.  The information-geometric projection angle should span \([0,\pi]\) (a half-circle from full access to full overflow).  The natural normalization is therefore:
\[
\boxed{\theta(q) = \frac{\pi}{2}\cdot d_{\rm tr}(q) = \frac{\pi}{2}\cdot 2q = \pi q.}
\]
The factor \(\pi/2\) is a normalization convention mapping the trace-distance range \([0,2]\) to the half-circle \([0,\pi]\).  This is not a geometric theorem about \(S^2\) arc lengths — it is a definitional choice motivated by the physical requirement that orthogonal information sectors (\(|L\rangle\) and \(|O_{\max}\rangle\)) be separated by \(\pi\).  The trace distance is the appropriate metric because it is sensitive to the distribution of overflow among sectors (distinguishing coherent from incoherent overflow), unlike the Bures angle which treats all mixtures along the pure-state geodesic identically.

The result \(\theta(q)=\pi q\) is **exact** for all \(N\geq 2\) — the trace distance \(2q\) is independent of \(N\) (one eigenvalue \(-q\) and \(N-1\) eigenvalues \(+q/(N-1)\), summing to \(2q\) in absolute value).  No \(N\to\infty\) limit or finite-\(N\) correction is needed.  The validity rests on two conditions: (a) maximum-entropy uniform filling of overflow sectors, and (b) incoherent (random-phase) overflow deposition justifying the mixed-state description.  Both are satisfied for macroscopic systems where decoherence events are independent and uncorrelated.

### S5.3 Physical Meaning of the Half-Circle

The range \([0,\pi]\) is not an arbitrary Wick-rotation interval.  It is the normalization of the trace distance to span a half-circle, reflecting that \(|L\rangle\) (full Lorentzian access) and \(|O_{\max}\rangle\) (complete classicality) are orthogonal information sectors separated by geodesic distance \(\pi\) on the effective two-sector Bloch sphere.  The linear relationship \(\theta(q)=\pi q\) follows from the trace-distance normalization, not from assumed arc-length geometry.  Wick language can still motivate the Lorentzian/Euclidean split heuristically, but \(\theta(q)\) is fixed by the two-step derivation: maximum entropy → uniform filling → trace distance → normalization to \([0,\pi]\).

---

## S6. Euler Residual

The residual is
\[
R(q)=1-e^{i\pi q}.
\]
The minus sign is required by the boundary condition \(R(0)=0\).  Then
\[
|R(q)|^2
=2-2\cos(\pi q)
=4\sin^2\left(\frac{\pi q}{2}\right).
\]
Thus
\[
m(q)=\frac{m_p}{\pi}|R(q)|
=\frac{2m_p}{\pi}\sin\left(\frac{\pi q}{2}\right).
\]

Boundary checks:

| \(q\) | access \(1-q\) | overflow | mass |
|---|---|---|---|
| 0 | full | none | 0 |
| 1/2 | half | half | \(\sqrt2m_p/\pi\) |
| 1 | none | full | \(2m_p/\pi\) |

### S6.1 Per-Branch Interpretation (Critical Clarification)

The mass \(m(q)\) is the residual mass of a **single coherent branch**, not the total mass of a macroscopic object.  A macroscopic object of total mass \(M_{\rm total}\) contains \(N_{\rm branches}\approx M_{\rm total}/m_{\max}\) mutually decohered branches, each with overflow \(q\approx 1\) and per-branch mass \(\approx m_{\max}\).  The total mass can be arbitrarily large while each branch respects the \(m_{\max}\) bound.  This interpretation resolves three potential objections:

1. **"Why is \(m_{\max}\approx 14\,\mu\text{g}\) so small?"**  It is not a limit on total mass; it is the maximum mass at which a single branch can maintain \(q<1\) (partial spatial-interference access).  Above \(m_{\max}\), coherent spatial interference necessarily fragments.

2. **"Why don't macroscopic objects have \(m=m_{\max}\)?"**  They do — per branch.  A 1\,kg object contains \(\sim 7\times 10^7\) decohered branches, each saturating at \(m_{\max}\).  The object's classicality is precisely this fragmentation.

3. **"Does the variable swap (q vs A) affect this?"**  No.  Whether one uses \(q\) (overflow, as in the main text) or \(A=1-q\) (archived, as in the GPT variant), the endpoint is the same: a single branch cannot exceed \(2m_p/\pi\).  The variable choice is a convention; the physics is invariant.

The falsifiable prediction is: any experiment demonstrating a **single coherent branch** with mass above \(2m_p/\pi\) maintaining full spatial-interference access falsifies DGF.  Present experiments remain far below this threshold.

---

## S7. Receiver-Mediated Kernel

### S7.1 Interaction Hamiltonian

The interaction Hamiltonian is
\[
H_{\rm int}
=\Lambda(q)V_S\otimes B,
\qquad
B=\sum_\lambda g_\lambda(b_\lambda+b_\lambda^\dagger).
\]
The receiver spectral density is
\[
J_{\rm recv}(\omega)
=\sum_\lambda |g_\lambda|^2\delta(\omega-\omega_\lambda).
\]
After tracing the receiver bath in the Born-Markov limit,
\[
\dot\rho
=-\frac{i}{\hbar}[H_S,\rho]
-\Gamma_{\rm recv}[V_S,[V_S,\rho]],
\]
where
\[
\Gamma_{\rm recv}
=\frac{1}{\hbar^2}
\int_0^\infty d\tau\,\langle B(\tau)B(0)\rangle
\left|\Delta\Lambda\right|^2.
\]

### S7.2 Explicit \(J_{\rm recv}(\omega)\) for Photon Bath

For a photon bath with dipole coupling (relevant for charged systems), the spectral density follows from the standard interaction Hamiltonian \(H_{\rm int} = -\mathbf{d}\cdot\mathbf{E}\).  The mode expansion of the electric field gives coupling constants \(|g_{\mathbf{k}}|^2 = (\hbar\omega/2\epsilon_0 V)|\mathbf{d}\cdot\hat{\epsilon}_{\mathbf{k}}|^2\).  Converting the mode sum to a continuum integral with polarization sum:
\[
J_{\rm recv}^{\rm(photon)}(\omega)=\frac{V}{(2\pi)^3}\cdot 2\cdot 4\pi\int_0^\infty dk\,k^2|g_k|^2\delta(\omega-ck)
=\frac{|\mathbf{d}|^2}{6\pi^2\epsilon_0\hbar c^3}\,\hbar\omega^3.
\]
In compact form: \(J_{\rm recv}^{\rm(photon)}(\omega) = \eta_{\rm ph}\,\hbar\omega^3\), where \(\eta_{\rm ph}=|\mathbf{d}|^2/(6\pi^2\epsilon_0\hbar c^3)\) has dimensions of [time²].  For neutral systems, the dipole coupling is replaced by the polarizability interaction \(\sim\alpha_S E^2\), giving the same \(\omega^3\) scaling with a different prefactor.  The UV cutoff is set by the Planck frequency \(\omega_c=t_p^{-1}\), beyond which the continuum mode description breaks down.

### S7.3 Explicit \(J_{\rm recv}(\omega)\) for Graviton Bath

For gravitons in linearized gravity, the coupling derives from the stress-energy tensor:
\[
H_{\rm int}\sim\frac{1}{m_p}h_{\mu\nu}T^{\mu\nu},
\]
where \(h_{\mu\nu}\) is the linearized graviton field expanded in plane-wave modes.  The spectral density for **quadrupole** coupling follows from the quadrupole power formula \(P\sim(G/c^5)\omega^6Q_{ij}^2\).  Converting to a spectral density (energy²×time dimensions) yields:
\[
J_{\rm recv}^{\rm(grav)}(\omega)\sim\frac{G}{c^5}\,\hbar\omega^5\,Q_{ij}^2,
\]
where \(Q_{ij}\sim m_S R_S^2\) is the quadrupole moment of the source.  The \(\omega^5\) scaling (not \(\omega^3\)) reflects the quadrupole nature of gravitational radiation — each derivative in the coupling brings one power of \(\omega\), and the quadrupole formula has two additional derivatives compared to dipole.  In Planck units:
\[
J_{\rm recv}^{\rm(grav)}(\omega)\sim t_p^2\,\hbar\omega^5\,m_S^2 R_S^4.
\]

### S7.4 Effective Planck-Cell Limit

The Markovian limit \(J_{\rm recv}(\omega)\to\text{const}\) is not directly applicable to super-ohmic spectral densities (\(\propto\omega^3\) or \(\propto\omega^5\)), which vanish at \(\omega\to 0\).  The standard procedure evaluates the bath correlation function at the system's characteristic frequency, or uses a UV cutoff approximation.  For DGF, the relevant cutoff is the Planck frequency \(\omega_c=t_p^{-1}\), giving effective low-frequency plateau values:
\[
J_{\rm recv}^{\rm(photon)}(\omega_c)\sim\eta_{\rm ph}\,\hbar t_p^{-3},\qquad
J_{\rm recv}^{\rm(grav)}(\omega_c)\sim t_p^{-3}\,\hbar\,m_S^2R_S^4.
\]

However, the decoherence kernel's prefactor \(2t_p l_p^4/\hbar^6\) is NOT obtained by evaluating \(J_{\rm recv}\) at \(\omega_c\).  It is set by **dimensional analysis** requiring the kernel exponent to be dimensionless.  Define an effective parameter:
\[
D_{\rm eff}\equiv\frac{t_p l_p^4}{\hbar^4},
\]
which has the dimensions needed to make \(\Gamma_{\rm recv}=2D_{\rm eff}(\Delta V)^2/\hbar^2\) a rate.  The relationship between \(D_{\rm eff}\) and the physical spectral densities \(J_{\rm recv}^{\rm(photon)}(\omega)\) and \(J_{\rm recv}^{\rm(grav)}(\omega)\) is through the bath correlation function integrated over the Planck timescale — a specific UV completion of the theory would compute this, but DGF treats \(D_{\rm eff}\) as the phenomenological parameter encoding Planck-scale geometry.  The local Planck-cell limit sets \(\Lambda(q)\to q\) and:
\[
\Gamma_{\rm recv}
=\frac{2t_p l_p^4}{\hbar^6},
\qquad
V_S=\frac{p^4}{3m_{\rm rest}},
\]
where \(m_{\rm rest}\) is the constant rest mass (Supplemental S10.3).  The receiver mass \(m_\lambda\) never appears in the denominator.  Low-mass receivers enter through \(J_{\rm recv}\), not through \(p^4/3m_\lambda\).  Different receiver sectors (photons vs gravitons) give different \(J_{\rm recv}(\omega)\) functional forms — and hence different non-Markovian corrections — but in the effective Planck-cell limit, the dimensional-analysis prefactor \(D_{\rm eff}\) is universal.  This is a limitation of the current level of UV completion, not a contradiction.

### S7.5 Full Kernel

The decoherence kernel between states \(|a\rangle,|b\rangle\) is:
\[
\boxed{
K_{ab}(t)=
\exp\left[
-\frac{2t_p l_p^4}{\hbar^6}
\left(\Delta\left\langle\frac{p^4}{3m_S}\right\rangle\right)^2
|\Delta q|^2\,t
\right].
}
\]
For macroscopically distinct states, \(|\Delta q|\sim 1\), recovering the main-text result.  The \(p^4/3m_S\) operator is the GUP imprint of Planck-cell spatial access; the \(2t_p l_p^4/\hbar^6\) prefactor encodes both Planck-scale geometry and the receiver spectral density in the Markovian limit.

---

## S8. Relation to GUP

The local system operator follows from the GUP expansion:
\[
k(p)=l_p^{-1}\tanh(l_p p/\hbar),
\]
\[
[x,p]=i\hbar(1+\beta_0p^2+\cdots),
\qquad \beta_0=l_p^2/\hbar^2.
\]
The canonical generator is
\[
P=p-\frac{\beta_0}{3}p^3+O(\beta_0^2),
\]
and therefore
\[
H=\frac{P^2}{2m_S}
=H_0-\beta_0\frac{p^4}{3m_S}+O(\beta_0^2).
\]
Thus \(p^4/3m_S\) is a local imprint operator of Planck-cell access, while \(J_{\rm recv}\) supplies the information receiver sector.

---

## S9. Falsification Tests

DGF strong form fails if:

1. \(q\) defined from cell access weights does not increase with controlled macroscopicity.
2. Receiver entropy does not generate positive drift \(v(q)>0\).
3. The two-sector information geometry does not give \(\theta(q)=\pi q\).
4. The receiver-mediated kernel cannot reduce to the GUP local kernel.
5. Coherent single-branch mass exceeds \(2m_p/\pi\) without loss of access \(A_S\).

---

## S10. Locked vs Flowable Information

### S10.1 The Conceptual Problem

If "mass = information density" and "decoherence = information loss," then mass should decrease during decoherence — but stones do not lose mass when they decohere.  This apparent contradiction is resolved by splitting total information into two components.

### S10.2 Two-Component Information

The total information \(I_{\rm tot}\) stored in a system's Planck cells splits as:
\[
I_{\rm tot}=I_{\rm locked}+I_{\rm flowable},
\]
where:
- \(I_{\rm locked}\): information archived in Planck cells that is no longer accessible for quantum interference but still contributes to rest mass and gravitational coupling.
- \(I_{\rm flowable}\): information that remains accessible for quantum superposition, interference, and branch-recombination tests.

In terms of the cell variables:
\[
I_{\rm locked}=\sum_{c\in\mathcal C_S}f_c\cdot(1-a_c),\qquad
I_{\rm flowable}=\sum_{c\in\mathcal C_S}f_c\cdot a_c,
\]
where \(f_c\) is the cell occupancy and \(a_c\) is the interference accessibility.  A cell with \(a_c=1\) has all its information flowable; a cell with \(a_c=0\) has all its information locked.

The overflow filling \(q\) is:
\[
q=1-\frac{1}{N_S}\sum_c a_c,
\]
which measures the fraction of cells that have lost accessibility — NOT the fraction of information that has been lost.  The total information \(I_{\rm tot}\) is conserved; only the locked/flowable ratio changes.

### S10.3 Two Distinct Mass Concepts

The framework introduces two distinct mass quantities:

**Rest mass** \(m_{\rm rest}\): The gravitational mass from total information content.  Both locked and flowable information contribute equally, because both represent energy stored in Planck cells:
\[
\boxed{m_{\rm rest}=\frac{m_p}{\eta}\cdot I_{\rm tot}=\frac{m_p}{\eta}(I_{\rm locked}+I_{\rm flowable}),}
\]
where \(\eta\sim O(1)\) is the information-to-mass conversion efficiency.  Decoherence transfers information from flowable to locked:
\[
\frac{d}{dt}I_{\rm flowable}=-\gamma(t)I_{\rm flowable},\qquad
\frac{d}{dt}I_{\rm locked}=+\gamma(t)I_{\rm flowable},
\]
but \(I_{\rm tot}=I_{\rm locked}+I_{\rm flowable}\) is constant.  Hence \(m_{\rm rest}\) is constant during decoherence — macroscopic objects do not lose mass.

**Euler residual mass** \(m(q)\): The mass-equivalent of the information-geometric deficit, defined in Section V/S6:
\[
m(q)=\frac{2m_p}{\pi}\sin\left(\frac{\pi q}{2}\right).
\]
This is NOT the rest mass.  It parameterizes the coupling between overflow and receiver modes through the GUP operator \(V_S=p^4/3m_{\rm rest}\) (note: the denominator uses \(m_{\rm rest}\), the constant total mass, not \(m(q)\)).  The endpoint \(m_{\max}=2m_p/\pi\approx 14\,\mu\text{g}\) is the maximum Euler residual a single coherent system can sustain before spatial interference fragments — it is a coherence limit, not a rest-mass limit.  A macroscopic object of \(m_{\rm rest}=1\) kg has \(m_{\rm rest}\gg m_{\max}\) but its Euler residual per coherent subsystem is \(\approx m_{\max}\).

This distinction resolves the confusion in 对话3.txt about the GPT variable swap: whether one uses \(q\) (overflow) or \(A=1-q\) (archived), the Euler mass formula is \(m\propto\sin(\pi\times\text{variable}/2)\), and the endpoint is the same.  The variable choice is a convention; the physics — that \(m(q)\neq m_{\rm rest}\) — is invariant.

### S10.4 Two-Layer Resolution

The conversation identified a two-layer structure:

- **Layer 1 (Planck-scale, quasi-static)**: \(q\) is determined by the system's density and composition (via \(f_c\) and interaction rates).  For macroscopic objects, \(q\approx 1\) because interaction density drives \(a_c\to 0\) for most cells.  This sets the system's "quantum capacity" — how much coherence it can sustain.

- **Layer 2 (Laboratory-scale, dynamical)**: Within the constraint set by \(q\), the specific decoherence rate is determined by environmental interactions.  This is the domain of Zurek-style quantum Darwinism.

DGF describes Layer 1.  The Fokker-Planck equation describes fluctuations of \(q\) around its quasi-static value, not the approach to \(q=1\) from \(q=0\).  This is why macroscopic objects do not "become more classical" over time — their \(q\) is already saturated.

### S10.5 Analogy

The locked/flowable distinction is analogous to computer memory: RAM (flowable, quickly accessible for computation) vs hard disk storage (locked, archived, not directly accessible for computation).  Writing data from RAM to disk does not change the computer's mass; it only changes the accessibility of the data.  Similarly, decoherence archives quantum interference information without destroying it or changing the system's mass.

---

## S11. Archive-Decompress Cycle (Open Conjecture)

### S11.1 The Natural Question

If the overflow \(q\) increases monotonically (\(d\langle q\rangle/dt>0\)), what happens when \(q\to 1\)?  Does the universe asymptotically approach total classicality, or is there a mechanism that resets \(q\)?

The conversation identified a candidate answer: **archive-decompress cycling** — when information density reaches the Planck bound, a local decompression is triggered, resetting \(q\) and releasing locked information back into flowable quantum form.

### S11.2 The Planck-Density Trigger

Each Planck cell has a maximum information capacity of \(\ln 2\) (one bit).  When a cell reaches saturation (\(f_c=1, a_c=0\)), it cannot accept any more locked information.  At the system level, when the mean occupancy \(\bar{f}=q\) approaches 1 in a local region, the region becomes "information-saturated."

At this point, the reflecting boundary condition \(J(1,t)=0\) in the Fokker-Planck equation must be replaced by an **absorbing-emitting** boundary:
\[
J(1,t)=-\kappa\left[P(1,t)-P_{\rm reset}\right],
\]
where \(P_{\rm reset}\) is a distribution concentrated near \(q\approx 0\) (freshly decompressed systems).  The decompression rate \(\kappa\) is:
\[
\kappa\sim\frac{1}{t_p}\exp\!\left(-\frac{S_{\rm BH}}{k_B}\right),
\]
where \(S_{\rm BH}\) is the Bekenstein-Hawking entropy of the saturated region.  For macroscopic objects, \(S_{\rm BH}/k_B\sim 10^{70}\) and \(\kappa\) is exponentially suppressed — decompression is effectively impossible, consistent with everyday experience.

### S11.3 Full Fokker-Planck with Decompression

\[
\frac{\partial P}{\partial t}=-\frac{\partial}{\partial q}[v(q)P]+\frac{\partial^2}{\partial q^2}[D(q)P]
-\kappa\delta(q-1)P(q,t)+\kappa P_{\rm reset}(q)\int_0^1 dq'\,\delta(q'-1)P(q',t).
\]

The last two terms represent removal of saturated systems at \(q=1\) and injection of reset systems at \(q\approx 0\).  In steady state, this gives a circulation:
\[
\text{quantum }(q\approx 0)\xrightarrow{\text{decoherence}}\text{classical }(q\approx 1)
\xrightarrow{\text{decompression}}\text{quantum }(q\approx 0).
\]

The circulation time for a system of mass \(m_S\) is:
\[
\tau_{\rm cycle}\sim t_p\exp(S_{\rm BH}/k_B)\sim t_p\exp\!\left(\frac{m_S^2}{m_p^2}\right).
\]
For a 1 kg object, \(\tau_{\rm cycle}\sim t_p\exp(10^{140})\gg\) age of the universe.  For a Planck-mass object, \(\tau_{\rm cycle}\sim t_p\) — immediate cycling.  This is why the cycle is invisible for macroscopic objects but potentially relevant at the Planck scale.

### S11.4 Testable Window: Black Hole Evaporation Endpoint

The archive-decompress transition becomes observable when \(S_{\rm BH}/k_B\sim O(1)\), i.e., for Planck-mass black holes at the endpoint of Hawking evaporation.  The DGF prediction is:

1. As a black hole evaporates, its horizon area shrinks, reducing \(S_{\rm BH}\).
2. When \(S_{\rm BH}/k_B\sim 1\), the decompression rate \(\kappa\sim t_p^{-1}\) becomes competitive with the evaporation rate.
3. At this point, the locked information in the black hole is released as coherent quantum information, not as thermal Hawking radiation.

This is a **falsifiable prediction**: the final stage of black hole evaporation should show deviations from the thermal Hawking spectrum, with information released in a non-thermal, potentially coherent form.  This is testable in principle with future Planck-scale experiments or analogue gravity systems.

### S11.5 Caveat

The archive-decompress cycle is an **open conjecture**, not a derived consequence of DGF.  It is included here as a "larger picture" speculation that naturally extends the DGF framework.  The main results of the paper — the microscopic definition of \(q\), the directed overflow dynamics, the information-geometric derivation of \(\theta(q)\), and the receiver-mediated decoherence kernel — do not depend on the cycle conjecture.

---

## S12. Reproducibility

Run:

```powershell
python .\scripts\generate_dgf_figures.py
```

Outputs:

| File | Purpose |
|---|---|
| `figures/fig1_mass_map.png` | mass map |
| `figures/fig2_dephasing_scale.png` | local Markovian kernel scale |
| `figures/fig3_experimental_gap.png` | mass gap |
| `figures/fig4_cosmic_decoherence_order.png` | overflow/access order |
| `data/cosmic_decoherence_order.csv` | \(q\), access, classicality proxy |


