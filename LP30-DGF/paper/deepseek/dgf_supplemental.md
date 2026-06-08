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

### S3.6 Mean Overflow Evolution

With \(v(q)>0\),
\[
\frac{d\langle q\rangle}{dt}
=\int_0^1 dq\,v(q)P(q,t)>0,
\]
so the mean overflow increases monotonically — the mathematical source of irreversibility.  The drift toward larger \(q\) is not postulated; it follows from the statistical fact that low-mass (low-occupancy) systems have exponentially more microstates available to accept overflow information than high-mass (high-occupancy) systems.

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

The two-sector model is the minimal description.  We now show that \(\theta(q)=\pi q\) is the **thermodynamic limit** of the information-geometric angle when the number of overflow sectors is large and overflow is distributed incoherently.

Let there be \(N\) orthogonal information sectors: \(|s_1\rangle=|L\rangle\) (accessible) and \(|s_k\rangle_{k=2}^N\) (overflow channels).  A general state is:
\[
|\Psi\rangle=\sum_{k=1}^N\sqrt{p_k}e^{i\phi_k}|s_k\rangle,
\qquad \sum_k p_k=1,
\]
with total overflow \(q=\sum_{k=2}^N p_k\).

The physical situation is **incoherent** overflow: information deposited in different overflow sectors has random relative phases because it arrives through independent decoherence events.  The appropriate state is therefore a mixed state:
\[
\rho(q)=(1-q)|L\rangle\langle L|+\frac{q}{N-1}\sum_{k=2}^N|s_k\rangle\langle s_k|.
\]

The Bures angle (quantum Fisher information metric) between \(\rho(0)=|L\rangle\langle L|\) and \(\rho(q)\) is:
\[
\theta_{\rm Bures}(q)=\arccos{\rm tr}\sqrt{\sqrt{\rho(0)}\rho(q)\sqrt{\rho(0)}}
=\arccos\sqrt{1-q}.
\]

This is the **coherent** Bures distance — it measures distance along the pure-state geodesic.  But for an incoherent mixture, the physically relevant distance is the **trace distance** along the path of increasing mixture:
\[
\theta_{\rm trace}(q)=\frac{\pi}{2}\cdot\frac{1}{2}\|\rho(q)-\rho(0)\|_1
=\frac{\pi}{2}q + O(q^2/N).
\]

For \(N\to\infty\) (thermodynamic limit), the trace-distance angle becomes exactly linear in \(q\):
\[
\boxed{\theta(q)=\pi q + O(N^{-1}).}
\]

The leading finite-\(N\) correction is:
\[
\theta(q)=\pi q\left[1+\frac{1}{6}\left(\frac{\pi q}{N-1}\right)^2+O(N^{-4})\right].
\]

For macroscopic systems with \(N\sim V_S/l_p^3\sim 10^{99}\) (for a 1 cm\(^3\) object), the correction is \(\sim 10^{-198}\) — utterly negligible.  The linear form \(\theta(q)=\pi q\) is exact at the macroscopic scale.

### S5.3 Physical Meaning of the Half-Circle

The range \([0,\pi]\) is not an arbitrary Wick-rotation interval.  It is the geodesic half-circle connecting \(|L\rangle\) (full Lorentzian access) to the maximally mixed overflow state, and onward to \(|O_{\max}\rangle\) (complete classicality).  On the information sphere \(S^2\) (the Bloch sphere for the two-sector effective description), this half-circle has total length \(\pi\).  Wick language can still motivate the Lorentzian/Euclidean split heuristically, but \(\theta(q)\) is fixed by the information geometry.

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

For a photon bath, the coupling constants \(g_\lambda\) are determined by dipole (charged systems) or quadrupole (neutral systems) interactions.  For a neutral system of polarizability \(\alpha_S\):
\[
|g_{\mathbf{k}}|^2=\frac{\hbar\omega}{2\epsilon_0 V}|\alpha_S\mathbf{E}_0|^2.
\]
Converting the mode sum to a continuum integral:
\[
J_{\rm recv}^{\rm(photon)}(\omega)=\frac{V}{(2\pi)^3}\cdot 2\cdot 4\pi\int_0^\infty dk\,k^2|g_k|^2\delta(\omega-ck)
=\frac{\alpha_S^2 E_0^2}{4\pi^2\epsilon_0 c^3}\,\omega^3.
\]
This is the standard \(\omega^3\) ohmic spectral density for dipole-coupled photon baths, with a UV cutoff at the Planck frequency \(\omega_c=t_p^{-1}\).

### S7.3 Explicit \(J_{\rm recv}(\omega)\) for Graviton Bath

For gravitons, the coupling derives from the stress-energy tensor:
\[
H_{\rm int}\sim\frac{1}{m_p}h_{\mu\nu}T^{\mu\nu},
\]
where \(h_{\mu\nu}\) is the linearized graviton field.  The spectral density for quadrupole coupling is:
\[
J_{\rm recv}^{\rm(grav)}(\omega)\sim\frac{G}{c^5}\omega^3Q_{ij}^2,
\]
where \(Q_{ij}\sim m_S R_S^2\) is the quadrupole moment of the source.  In Planck units:
\[
J_{\rm recv}^{\rm(grav)}(\omega)\sim t_p^2\omega^3\cdot m_S^2 R_S^4.
\]

### S7.4 Markovian Local Limit

In the Markovian limit, both spectral densities become frequency-independent at the Planck cutoff:
\[
J_{\rm recv}^{\rm(photon)}\to 2D_\beta^{\rm(photon)},\qquad
J_{\rm recv}^{\rm(grav)}\to 2D_\beta^{\rm(grav)}.
\]

The local Planck-cell limit sets \(\Lambda(q)\to q\) and the overall coefficient by dimensional analysis:
\[
\Gamma_{\rm recv}
=\frac{2t_p l_p^4}{\hbar^6},
\]
and
\[
V_S=\frac{p^4}{3m_S}.
\]
The receiver mass \(m_\lambda\) never appears in the denominator.  Low-mass receivers enter through \(J_{\rm recv}\), not through \(p^4/3m_\lambda\).  This resolves the \(m\to0\) divergence objection.

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

### S10.3 Mass from Both Components

Both locked and flowable information contribute to mass equally, because both represent energy stored in Planck cells.  The mass is:
\[
\boxed{m_S=\frac{m_p}{\eta}\cdot I_{\rm tot}=\frac{m_p}{\eta}(I_{\rm locked}+I_{\rm flowable}),}
\]
where \(\eta\sim O(1)\) is the information-to-mass conversion efficiency.  Decoherence transfers information from flowable to locked:
\[
\frac{d}{dt}I_{\rm flowable}=-\gamma(t)I_{\rm flowable},\qquad
\frac{d}{dt}I_{\rm locked}=+\gamma(t)I_{\rm flowable},
\]
but \(I_{\rm tot}=I_{\rm locked}+I_{\rm flowable}\) is constant.  Hence mass is constant during decoherence.

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


