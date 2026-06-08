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
so independent accessibility factors multiply while overflow accumulates.

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
with reflecting boundaries at \(q=0\) and \(q=1\).  The drift is fixed by an entropy gradient:
\[
v(q)=\Gamma(q)\,\partial_q S_{\rm recv}(q),
\qquad
\Gamma(q)\ge0.
\]
Here \(S_{\rm recv}(q)\) is the entropy of receiver modes available to carry the overflow information.  For low-mass radiationlike receivers the number of available states increases as overflow grows, so
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
m_{\max}=\frac{2m_p}{\pi}\simeq1.385\times10^{-8}{\rm kg}.
}
\]
This is no longer circular: \(q\) is defined from Planck-cell access weights, evolves by directed overflow dynamics, and only then maps to mass.

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

## VII. Rigid Translation

For a rigid translation \(|b\rangle=T(d)|a\rangle\),
\[
\psi_b(p)=e^{-ipd/\hbar}\psi_a(p).
\]
Since \(V_S=f(p)=p^4/3m_S\),
\[
\langle b|V_S|b\rangle
=\int dp\,|\psi_a(p)|^2f(p)
=\langle a|V_S|a\rangle.
\]
Thus \(\Delta V_{ab}=0\) and the local DGF channel gives \(K_{ab}=1\).  A rigid translation can still be macrocosmically classical through large \(q\); it simply does not create a new \(p^4/m_S\) contrast.  This separates global overflow from position-collapse models.

![Macrocosmic overflow order](figures/fig4_cosmic_decoherence_order.png)

**Fig. 3.** Overflow filling \(q\) increases mass residual and decreases accessible coherence \(1-q\).  This is the repaired directionality.

---

## VIII. Falsification and Experimental Meaning

DGF strong form can be rejected by any of the following:

1. A direct microscopic readout of cell access weights \(a_c\) shows no monotone relation between overflow and macroscopicity.
2. The entropy-gradient drift \(v(q)>0\) is absent in controlled receiver-mode coupling.
3. The two-sector information geometry does not produce \(\theta(q)=\pi q\).
4. The receiver spectral density does not reduce to the GUP-Lindblad kernel in the local Markovian limit.
5. A single coherent branch above \(2m_p/\pi\) maintains full spatial interference access.

The endpoint and the kernel are therefore not free-floating formulas.  They are consequences of a directed overflow theory with explicit microscopic and dynamical content.

![Experimental mass gap](figures/fig3_experimental_gap.png)

**Fig. 4.** Present experimental mass scales compared with the coherent-branch endpoint.

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

A crucial distinction underlies the framework: total information in a system splits into **locked** (archived, contributing to rest mass) and **flowable** (accessible for quantum interference) components.  Decoherence transfers information from flowable to locked without changing total mass — resolving the apparent paradox that macroscopic objects decohere without losing mass.  This gives a two-layer structure: \(q\) is a quasi-static quantity set by the system's density and composition (Layer 1, described by DGF), while specific decoherence rates are set by environmental interactions within the constraint of \(q\) (Layer 2, described by standard open quantum systems).

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
