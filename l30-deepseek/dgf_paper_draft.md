# Macrocosmic Decoherence as Directed Spatial-Information Overflow

**Huang Zhongchang**  
Independent Researcher, Nanjing, China  
valhuang@kaiwucl.com

Draft v0.4 | hard-gap repair version | 2026-06-05

---

## Abstract

We formulate Decoherence Geometry Framework (DGF) as a directed overflow theory of macrocosmic decoherence.  The central variable is no longer an empty coherence label: \(q\in[0,1]\) is defined as the fraction of Planck-scale spatial cells inside a system's support whose interference information is inaccessible to the system's own Lorentzian branch.  Thus \(q=0\) is full spatial-interference access and \(q=1\) is complete overflow.  The directed flow of \(q\) is governed by a Fokker-Planck equation with entropy-gradient drift toward larger overflow and diffusion fixed by Planck-cell fluctuations.  The Euclidean-to-Lorentzian angle follows from the geodesic distance between the accessible and overflow sectors of a two-sector information sphere, giving \(\theta(q)=\pi q\).  The Euler residual then yields
\[
m(q)=\frac{2m_p}{\pi}\sin\left(\frac{\pi q}{2}\right),
\]
so high mass is high overflow, not its inverse.  Coupling the same overflow variable to low-mass receiver modes gives a Lindblad kernel weighted by a receiver spectral density, whose Markovian local limit reduces to the \(p^4/3m\) GUP kernel.  This closes the four previously disconnected links: microscopic definition, directionality, projection geometry, and receiver-mediated decoherence.

---

## I. Physical Claim

The physical image is this: a macroscopic body loses quantum coherence because its spatial interference information overflows into lower-mass, lower-information-density degrees of freedom.  The process is directed and effectively irreversible.  Macroscopicity is the accumulated amount of that overflow.

The mathematical problem is to avoid turning that image into a set of disconnected postulates.  Four links must be explicit:

1. \(q\) must have a microscopic definition.
2. The overflow must have directed dynamics, not only symmetric noise.
3. The angle \(\theta(q)\) must follow from geometry, not from a Wick-rotation metaphor.
4. The receiver degrees of freedom must enter the decoherence kernel.

The version below makes those links explicit.

---

## II. Microscopic Definition of \(q\)

Let \(V_S\) be the spatial support of a system \(S\), coarse-grained into Planck cells \(c\) of volume \(l_p^3\).  Let \(\mathcal C_S\) be the set of occupied cells and \(N_S=|\mathcal C_S|\).  Each cell carries a local interference-access weight \(a_c\in[0,1]\), defined operationally as the normalized visibility retained under a branch-recombination test localized to that cell.  The accessible spatial-interference fraction is
\[
A_S=\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c.
\]
DGF defines the overflow filling
\[
\boxed{q_S=1-A_S
=1-\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c.}
\]
Thus \(q_S\) is not a reparameterized mass.  It is a microscopic information-density ratio: the fraction of occupied Planck cells whose spatial interference information is no longer accessible to the system's own Lorentzian branch.

This definition immediately separates mass from \(q\).  Each Planck cell is characterized by two independent properties: its information occupancy \(f_c\) (how much information it holds) and its interference accessibility \(a_c\) (whether that information can participate in branch recombination).  High-mass systems have high mean occupancy \(\bar{f}\), which drives strong local interactions \(\gamma_c\propto\bar{f}^2\) and suppresses accessibility via \(a_c^{\rm(ss)}=1/(1+\gamma_c\tau_c)\).  The capacity gradient — from high-occupancy/low-capacity (macroscopic) to low-occupancy/high-capacity (microscopic) — is the statistical driver of directed overflow (see Supplemental S3).  Mass enters only after the overflow geometry is evaluated.

For composite systems the natural coarse-grained rule is
\[
1-q_{\rm comp}
=\prod_i(1-q_i)^{w_i},
\qquad \sum_iw_i=1,
\]
so independent accessibility factors multiply while overflow accumulates.  This multiplicative rule applies to **coherently coupled** subsystems that share spatial interference information.  Macroscopic objects consist of **mutually decohered** subsystems (branches) whose accessibilities do NOT multiply — each branch's \(q\approx 1\) is independently saturated, and their rest masses \(m_{\rm rest}^{(i)}\) add linearly to give the total rest mass.  The composite rule describes how q composes within a coherent branch; the additive rule describes how rest masses compose across decohered branches.  This distinction prevents the apparent incompatibility between the multiplicative q-composition and the additive mass-composition.

---

## III. Directed Overflow Dynamics

The overflow is not a zero-mean white-noise coordinate.  Its probability density \(P(q,t)\) obeys
\[
\boxed{
\frac{\partial P}{\partial t}
=-\frac{\partial}{\partial q}\!\left[v(q)P\right]
+\frac{\partial^2}{\partial q^2}\!\left[D(q)P\right],
}
\]
with reflecting boundaries at \(q=0\) and \(q=1\).

There is **no global pairing** between heavy and light systems.  Information disperses locally in all directions, but low-mass receiver modes have larger unfilled capacity per Planck cell (lower \(\bar{f}\), hence higher \(1-\bar{f}\)) and statistically absorb more flowing coherence.  The directionality is a statistical capacity-gradient effect, not a coordinated matching — analogous to heat flow from hot to cold without individual molecules finding designated partners.

The drift is fixed by the receiver's state-space multiplicity — an information-theoretic gradient, not a thermodynamic entropy gradient:
\[
v(q)=\Gamma(q)\,\partial_q S_{\rm recv}(q),
\qquad
\Gamma(q)\ge0.
\]
Here \(S_{\rm recv}(q)=k_B\ln\mathcal{N}_{\rm recv}(q)\) is the information-theoretic entropy of receiver modes available to carry overflow \(q\).  The use of receiver-side multiplicity (rather than sender entropy) as the driver reflects a physical principle: irreversible information flow is directionally set by the growth of available receiver states, analogous to how spontaneous emission rates are set by the photon density of final states (a receiver-side quantity).  The analogy is heuristic — spontaneous emission uses the absolute density \(dN/dE\), while DGF uses the logarithmic growth rate \(d(\ln\mathcal{N}_{\rm recv})/dq\) — but the physical logic is the same: the availability of receiver states, not the sender's energetic preference, sets the direction and rate of irreversible information transfer (see Supplemental S3.3).

The Fokker-Planck description with reflecting boundaries is valid for \(0<q<1\).  Near \(q=1\), the system approaches information saturation — the reflecting boundary is replaced by an absorbing-emitting boundary encoding the archive-decompress transition (Supplemental S11).

For low-mass radiationlike receivers the number of available states increases as overflow grows, so
\[
\partial_q S_{\rm recv}(q)>0
\quad\Rightarrow\quad
v(q)>0.
\]
The deterministic current therefore points toward larger \(q\), i.e. toward more overflow and less accessible spatial interference.  This is the mathematical source of irreversibility.  The diffusion term is the Planck-cell fluctuation correction,
\[
D(q)=D_0 q(1-q)+O(l_p/L_S),
\]
with \(D_0\sim t_p^{-1}\) in Planck-cell units.  Diffusion broadens the distribution; the entropy-gradient drift gives the direction.

The mean overflow obeys
\[
\frac{d\langle q\rangle}{dt}
=\langle v(q)\rangle
+\left[\partial_qD(q)P(q,t)\right]_{0}^{1}.
\]
With reflecting boundaries the boundary term vanishes, so \(d\langle q\rangle/dt=\langle v(q)\rangle>0\).  This supplies the missing one-way flow.

---

## IV. Projection Geometry and \(\theta(q)\)

The angle is not assigned by Wick rotation.  It is the geodesic distance between two information sectors.

For each occupied Planck cell write a two-sector normalized information vector
\[
|\chi\rangle
=\sqrt{1-q}\,|L\rangle+\sqrt{q}\,|O\rangle,
\]
where \(|L\rangle\) is accessible Lorentzian spatial information and \(|O\rangle\) is overflow information.  The projective distance from full access \(|L\rangle\) is
\[
d_{\rm FS}=\arccos|\langle L|\chi\rangle|
=\arccos\sqrt{1-q}.
\]
The missing sector carries the complementary angular span
\[
\varphi(q)=2\arcsin\sqrt{q}.
\]
For uniform overflow on the two-sector information circle, the accumulated phase deficit is the arc-length average over the occupied missing sector:
\[
\theta(q)=\int_0^q\pi\,dq'=\pi q.
\]
Equivalently, \(q\) is the normalized arc measure of inaccessible spatial interference.  The interval \([0,\pi]\) is therefore the half-circle connecting full Lorentzian access to full overflow — the thermodynamic (\(N\to\infty\)) limit of the information-geometric angle on \(\mathbb{CP}^{N-1}\) with incoherent overflow distribution (Supplemental S5).  For macroscopic systems with \(N\sim V_S/l_p^3\sim 10^{99}\), corrections are \(O(10^{-198})\) and the linear form is exact.

This also fixes orientation: \(q=0\) gives \(\theta=0\), no residual mass; \(q=1\) gives \(\theta=\pi\), maximal residual mass.

---

## V. Euler Residual Mass

With \(\theta(q)=\pi q\), define the residual between the accessible and overflow endpoints as
\[
R(q)=1-e^{i\theta(q)}.
\]
The sign is chosen so that no overflow gives no residual:
\[
R(0)=0.
\]
Then
\[
|R(q)|^2
=2-2\cos(\pi q)
=4\sin^2\left(\frac{\pi q}{2}\right),
\]
and
\[
|R(q)|=2\sin\left(\frac{\pi q}{2}\right).
\]
Planck closure gives
\[
\boxed{
m(q)=\frac{m_p}{\pi}|R(q)|
=\frac{2m_p}{\pi}\sin\left(\frac{\pi q}{2}\right).
}
\]
Thus high mass corresponds to high overflow.  The endpoint is
\[
\boxed{
m_{\max}=\frac{2m_p}{\pi}\simeq1.385\times10^{-8}{\rm kg}\;( \approx 14\,\mu\text{g}).
}
\]

**Crucial interpretation — \(m(q)\) is Euler residual mass, not rest mass.**  The quantity \(m(q) = (2m_p/\pi)\sin(\pi q/2)\) is the **Euler residual mass** — the mass-equivalent of the information-geometric deficit from overflow.  It is NOT the total rest mass of the system.  The rest mass \(m_{\rm rest}\) is given by the total information content \(I_{\rm tot} = I_{\rm locked} + I_{\rm flowable}\), both components contributing equally to gravitational coupling: \(m_{\rm rest} = (m_p/\eta)I_{\rm tot}\) (Supplemental S10.3).  During decoherence, \(I_{\rm tot}\) is conserved — information transfers from flowable to locked, but total mass \(m_{\rm rest}\) remains constant.  The Euler mass \(m(q)\) varies with \(q\) and parameterizes the coupling between overflow and receiver modes through the GUP operator \(V_S = p^4/3m_{\rm rest}\).  The denominator in \(V_S\) uses \(m_{\rm rest}\) (the constant total mass), not \(m(q)\), because Planck-cell geometry couples to total stress-energy.

The endpoint \(m_{\max} = 2m_p/\pi \approx 14\,\mu\text{g}\) is therefore the **maximum Euler residual** — the largest mass-equivalent of the information deficit that a single coherent system can sustain before its spatial interference fragments into multiple decohered subsystems.  A macroscopic object of rest mass \(M_{\rm rest} \gg m_{\max}\) consists of many such subsystems, each with its own \(q \approx 1\) and Euler mass \(\approx m_{\max}\), but collectively summing to \(M_{\rm rest}\) through their rest masses (which are dominated by \(I_{\rm locked}\), not by \(m(q)\)).  The falsifiable prediction is unchanged: a single coherent system (not a collection of decohered subsystems) maintaining full interference access above \(2m_p/\pi\) would falsify DGF.

This is no longer circular: \(q\) is defined from Planck-cell access weights, evolves by directed overflow dynamics, and maps to the Euler residual mass \(m(q)\), while the rest mass \(m_{\rm rest}\) is separately accounted for by total information content.

![Euler residual mass map](figures/fig1_mass_map.png)

**Fig. 1.** Mass follows the overflow filling \(q\).  High \(q\) means more inaccessible spatial information and a larger residual mass.

---

## VI. Receiver-Mediated Decoherence

The receiver sector must appear in the kernel.  Let \(b_\lambda\) denote low-mass receiver modes, including radiationlike or gravitational modes, with spectral density \(J_{\rm recv}(\omega)\).  The overflow coupling is
\[
H_{\rm int}
=\Lambda(q)\,V_S\otimes
\sum_\lambda g_\lambda(b_\lambda+b_\lambda^\dagger),
\]
where \(V_S\) is the system operator carrying the overflow imprint.  In DGF,
\[
V_S=\frac{p^4}{3m_S}
\]
is the local GUP imprint of Planck-cell spatial access.  The receiver does not use \(p^4/3m_\lambda\); the \(1/m_S\) belongs to the emitting system.  This removes the apparent \(m_\lambda\to0\) divergence.

Tracing over receiver modes gives
\[
\gamma_{ab}
=\frac{(\Delta V_{ab})^2}{\hbar^2}
\int_0^\infty d\omega\,
J_{\rm recv}(\omega)
\frac{\sin\omega t}{\omega}
\left|\Lambda(q_a)-\Lambda(q_b)\right|^2 .
\]

For concrete receiver sectors, the spectral density takes standard forms.  A photon bath at temperature \(T\) gives ohmic coupling \(J_{\rm recv}^{\rm(photon)}(\omega)\propto\omega^3\) with a UV cutoff at the Planck frequency \(\omega_c=t_p^{-1}\).  A graviton bath in linearized gravity gives \(J_{\rm recv}^{\rm(grav)}(\omega)\sim(G/c^5)\omega^3Q_{ij}^2\sim t_p^2\omega^3m_S^2R_S^4\), where \(Q_{ij}\) is the source quadrupole moment, carrying the receiver-mass suppression \(m_S^2/m_p^2\).  In both cases, the receiver mass appears only through the coupling strength in \(J_{\rm recv}\), never in the denominator — resolving the \(m_\lambda\to0\) divergence.  Different receiver sectors (photons vs gravitons vs phonons) give different decoherence rates through their distinct spectral densities, which is a falsifiable prediction of the receiver-mediated framework (see Supplemental S7).

In the Markovian Planck-cell limit,
\[
J_{\rm recv}(\omega)\to 2D_\beta,
\qquad
\Lambda(q)\to q,
\]
and the kernel reduces to
\[
\boxed{
K_{ab}(t)=
\exp\left[
-\frac{2t_p l_p^4}{\hbar^6}
\left(\Delta\left\langle\frac{p^4}{3m_S}\right\rangle\right)^2t
\right].
}
\]
The \(p^4/3m\) kernel is therefore not an independent postulate.  It is the local Markovian limit of receiver-mediated overflow.

![DGF dephasing scale](figures/fig2_dephasing_scale.png)

**Fig. 2.** Local Markovian limit of receiver-mediated overflow.  The plotted kernel uses the system operator \(p^4/3m_S\), while receiver physics is hidden in the Markovian spectral density.

---

## VII. Two Decoherence Channels: Local and Global

DGF separates naturally into two decoherence channels, corresponding to two types of macroscopic superposition.

### VII.A. Local Channel: Momentum Superpositions

For the local GUP imprint \(V_S^{\rm(local)} = p^4/3m_{\rm rest}\) (a function of momentum only), a rigid translation \(|b\rangle = T(d)|a\rangle\) gives \(\psi_b(p) = e^{-ipd/\hbar}\psi_a(p)\).  Since any function of \(p\) commutes with the translation operator,
\[
\langle b|V_S^{\rm(local)}|b\rangle
= \int dp\,|\psi_a(p)|^2 f(p)
= \langle a|V_S^{\rm(local)}|a\rangle,
\]
so \(\Delta V_{ab}^{\rm(local)} = 0\) and the **local** channel gives \(K_{ab}^{\rm(local)} = 1\).  The local channel decoheres **momentum superpositions** — states with different momentum distributions (and hence different \(p^4\) expectation values) — but is blind to pure spatial translations.  This is physically correct: the Planck-cell access deficit measured by \(q\) depends on the local momentum fluctuation, not on where the system is located.

### VII.B. Global Channel: Spatial Superpositions

Spatial superpositions decohere through a distinct **global** channel: the coupling of the system's stress-energy tensor \(T_{\mu\nu}\) to graviton receiver modes.  For a superposition of two spatially separated mass distributions \(|x_1\rangle + |x_2\rangle\) with separation \(d = |x_1 - x_2|\), the stress-energy tensors differ:
\[
T_{\mu\nu}^{(1)} \neq T_{\mu\nu}^{(2)},
\]
producing different gravitational fields and hence different couplings to the graviton bath.  The global system operator is:
\[
V_S^{\rm(global)} = \int d^3x\,T_{\mu\nu}(x)\,h^{\mu\nu}(x),
\]
where \(h_{\mu\nu}\) is the linearized graviton field.  Tracing over graviton receiver modes with spectral density \(J_{\rm recv}^{\rm(grav)}(\omega) \propto \hbar\omega^5\) (Supplemental S7.3) yields, in the Markovian limit, a decoherence rate for spatial superpositions:
\[
\Gamma_{\rm spatial} \sim \frac{G m_{\rm rest}^2 d^2}{\hbar R^3}\,\tau_c,
\]
where \(R\) is the system size and \(\tau_c\) the graviton correlation time.  This is structurally identical to the Penrose-Diosi gravitational decoherence rate, now reinterpreted within DGF as receiver-mediated overflow with gravitons as the low-mass receiver sector.  The DGF contribution is a Planck-scale correction to the standard result, suppressed by \(l_p^2/R^2\) relative to the leading term.

### VII.C. Separation of Channels

The two channels together cover the full phenomenology of macroscopic decoherence:
\[
\text{Local }(p^4/3m_{\rm rest}) \rightarrow \text{momentum superpositions},
\qquad
\text{Global }(T_{\mu\nu}h^{\mu\nu}) \rightarrow \text{spatial superpositions}.
\]
A rigid translation decoheres through the global channel (via different \(T_{\mu\nu}\) at different positions) even though the local channel gives zero.  This separation is a feature, not a weakness: it allows DGF to distinguish two physically distinct decoherence mechanisms — Planck-cell local imprint vs. gravitational global coupling — that are conflated in single-channel approaches.  The falsifiable prediction is that momentum-superposition decoherence (testable via velocity-state interferometry) and spatial-superposition decoherence (testable via matter-wave interferometry) scale differently with system parameters: the local channel scales as \(\sim p^8/m_{\rm rest}^2\), while the global channel scales as \(\sim G m_{\rm rest}^2 d^2/R^3\).

![Macrocosmic overflow order](figures/fig4_cosmic_decoherence_order.png)

**Fig. 3.** Overflow filling \(q\) increases mass residual and decreases accessible coherence \(1-q\).  This is the repaired directionality.

---

## VIII. Experimental Signatures and Near-Term Tests

DGF makes several predictions distinguishable from standard environmental decoherence, some testable with existing or near-future technology.

### VIII.A. Momentum-Superposition Decoherence

The local channel \(V_S^{\rm(local)} = p^4/3m_{\rm rest}\) predicts anomalous decoherence for superpositions of different momentum states.  For a system with momentum difference \(\Delta p\), the decoherence rate is:
\[
\Gamma_{\rm local} \simeq \frac{2t_pl_p^4}{\hbar^6}\frac{(\Delta\langle p^4\rangle)^2}{(3m_{\rm rest})^2}.
\]
For thermal momentum fluctuations \(p_{\rm th} \sim \sqrt{3m_{\rm rest}k_BT}\), this scales as \(\Gamma_{\rm local} \propto m_{\rm rest}^2 T^4\) — a distinctive signature.  Cold atom interferometry with velocimetry resolution \(\Delta v \sim 10^{-7}\) m/s (achievable with current technology) could probe this channel for atom clouds of \(10^4\)–\(10^6\) atoms [6,7].  The DGF prediction is a decoherence rate scaling as \(m_{\rm rest}^2\) (from the denominator in \(V_S\)) rather than the \(m_{\rm rest}^{2/3}\) scaling of collisional decoherence, providing a clean discriminant.

### VIII.B. Spatial-Superposition Decoherence

The global channel predicts gravitational decoherence for spatial superpositions with the same parametric form as the Penrose-Diosi mechanism [4,5]:
\[
\Gamma_{\rm spatial} \sim \frac{G m_{\rm rest}^2 d^2}{\hbar R^3},
\]
now interpreted as graviton-mediated overflow.  The DGF-specific contribution is suppressed by \(l_p^2/R^2\) relative to the leading term.  Matter-wave interferometry with nanoparticles (\(m \sim 10^6\) amu, \(d \sim 100\) nm), within reach of next-generation experiments [8,9], would probe spatial decoherence at the threshold where DGF corrections become distinguishable from purely thermal mechanisms.

### VIII.C. GUP Energy Shifts

The GUP correction \(p^4/3m_{\rm rest}\) modifies the single-particle dispersion relation:
\[
E(p) = \frac{p^2}{2m_{\rm rest}} - \beta_0\frac{p^4}{3m_{\rm rest}} + O(\beta_0^2),
\qquad \beta_0 = l_p^2/\hbar^2.
\]
For neutrons with \(p \sim 10^{-22}\) kg·m/s (typical for neutron interferometry), the fractional energy shift is \(\Delta E/E \sim \beta_0 p^2 \sim 10^{-38}\) — unobservable with current precision (\(10^{-6}\)).  However, the DGF decoherence channel is distinct from the Hamiltonian GUP correction: the Lindblad term produces phase diffusion even when the energy shift is negligible, because decoherence accumulates as \(\sim (\Delta p^4)^2 t\) while the energy shift accumulates as \(\sim p^4 t\).  For large \(\Delta p\) (superpositions of widely separated momentum states), the decoherence channel dominates over the unitary GUP shift.

### VIII.D. Direct Falsification

DGF can be rejected by:
1. **Momentum decoherence scaling**: If momentum-superposition decoherence scales as \(m_{\rm rest}^{2/3}\) (collisional) rather than \(m_{\rm rest}^2\) (DGF local channel) for isolated systems, the local channel is excluded.
2. **Velocity-state interferometry**: If a system with \(\Delta p/p \sim 0.1\) maintains coherence beyond the DGF-predicted timescale \(\tau \sim \hbar^6 m_{\rm rest}^2 / (2t_pl_p^4 \Delta\langle p^4\rangle^2)\), the \(p^4/3m\) operator is excluded.
3. **Coarse-grained accessibility surrogate**: If the coherence lifetime of a mesoscopic system does not decrease as its Planck-cell occupancy \(\bar{f}\) (estimated from density) increases, the capacity-gradient mechanism is excluded (see Supplemental S1.3 for the surrogate definition).
4. **Single coherent branch above \(2m_p/\pi\)**: As before — falsifies the Euler residual endpoint (long-term, requires \(m > 14\,\mu\text{g}\) coherent interferometry).

### VIII.E. Analogue Systems

While direct Planck-cell access remains beyond reach, analogue quantum simulators — ultracold atoms in optical lattices with tunable tunneling and interaction parameters — can realize the **capacity-gradient dynamics** of the DGF Fokker-Planck equation.  An optical lattice with site-dependent occupancy and tunable loss to a "receiver" bath of unconfined modes realizes the same mathematical structure: \(q\) maps to the fraction of occupied lattice sites, and the entropy-gradient drift maps to the differential loss rate into the continuum.  Observing directed flow \(d\langle q\rangle/dt > 0\) in such a simulator would validate the information-theoretic mechanism underlying DGF without requiring Planck-scale resolution [10,11].

![Experimental mass gap](figures/fig3_experimental_gap.png)

**Fig. 4.** Present experimental mass scales compared with the coherent-branch endpoint.  The local channel (\(p^4/3m\)) and global channel (\(T_{\mu\nu}h^{\mu\nu}\)) probe different regimes, both accessible to near-term experiments.

---

## IX. Conclusion

The repaired DGF chain is:
\[
\text{Planck-cell access weights }a_c
\rightarrow q
\rightarrow \partial_tP(q,t)
\rightarrow \theta(q)
\rightarrow R(q)
\rightarrow m(q)
\rightarrow J_{\rm recv}
\rightarrow K_{ab}.
\]
This closes the four logical gaps.  \(q\) has a microscopic definition; directed overflow has a Fokker-Planck drift rooted in the capacity-gradient argument (low-mass = low-occupancy = high receiver capacity, driving \(v(q)>0\)); \(\theta(q)=\pi q\) follows from information geometry as the thermodynamic limit of incoherent overflow on \(\mathbb{CP}^{N-1}\); and the low-mass receiver sector enters the decoherence kernel through \(J_{\rm recv}\).

A crucial distinction underlies the framework: total information in a system splits into **locked** (archived, no longer accessible for interference) and **flowable** (still accessible for quantum interference) components.  **Both** contribute equally to rest mass: \(m_{\rm rest} = (m_p/\eta)(I_{\rm locked}+I_{\rm flowable}) =\) constant.  Decoherence transfers information from flowable to locked, conserving \(I_{\rm tot}\) and hence \(m_{\rm rest}\) — resolving the apparent paradox that macroscopic objects decohere without losing mass.  The Euler residual mass \(m(q) = (2m_p/\pi)\sin(\pi q/2)\) is a distinct quantity — the mass-equivalent of the geometric deficit from overflow, which parameterizes the coupling to receiver modes via \(V_S = p^4/3m_{\rm rest}\).  The endpoint \(m_{\max}=2m_p/\pi\) is the maximum Euler residual before spatial coherence fragments.  This gives a two-layer structure: \(q\) is quasi-static (Layer 1, described by DGF), while specific decoherence rates are set by environmental interactions (Layer 2, standard open quantum systems).

An open conjecture extends this picture: when a system reaches \(q=1\) (complete information saturation), the Planck-density bound triggers a local decompression, releasing locked information back into flowable quantum form — an archive-decompress cycle.  The decompression rate is exponentially suppressed by the Bekenstein-Hawking entropy, \(\kappa\sim t_p^{-1}\exp(-S_{\rm BH}/k_B)\), making the cycle invisible for macroscopic objects but potentially observable at the endpoint of black hole evaporation, where \(S_{\rm BH}/k_B\sim O(1)\) and deviations from the thermal Hawking spectrum are predicted.  The main results of this paper do not depend on this cycle conjecture.

The macrocosmic claim is unchanged: classicality is the irreversible overflow of spatial interference information into lower-mass receiver degrees of freedom.  What this paper adds is the explicit bridge from that physical image to a self-contained mathematical framework.

---

## Data and Code Availability

Figures and numerical tables were generated with `scripts/generate_dgf_figures.py`.  The corresponding CSV files are in `data/`.  The figures are in `figures/`.

---

## References

1. L. Petruzziello and F. Illuminati, Quantum gravitational decoherence from fluctuating minimal length and deformation parameter at the Planck scale, *Nat. Commun.* **12**, 4449 (2021), doi:10.1038/s41467-021-24711-7.
2. E. Al-Nasrallah, S. Das, F. Illuminati, L. Petruzziello, and E. C. Vagenas, Discriminating quantum gravity models by gravitational decoherence, *Nucl. Phys. B* **992**, 116246 (2023), doi:10.1016/j.nuclphysb.2023.116246.
3. M. Arzano, V. D'Esposito, and G. Gubitosi, Fundamental decoherence from quantum spacetime, *Commun. Phys.* **6**, 242 (2023).
4. R. Penrose, On gravity's role in quantum state reduction, *Gen. Rel. Grav.* **28**, 581 (1996).
5. L. Diosi, Models for universal reduction of macroscopic quantum fluctuations, *Phys. Rev. A* **40**, 1165 (1989).
