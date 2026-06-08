# Macrocosmic Decoherence as Archive-Decompression Dynamics

**Huang Zhongchang**  
Independent Researcher, Nanjing, China  
valhuang@kaiwucl.com

Draft v0.5 | archive-decompression revision | 2026-06-05

---

## Abstract

We revise Decoherence Geometry Framework (DGF) around a sharper distinction between flowing and archived information.  The accessible quantum variable is
\[
q=\frac{N_{\rm accessible}}{N_{\rm total}(V)},
\]
the fraction of Planck-scale spatial cells whose interference information remains branch-recombinable.  Decoherence is the directed archival process \(q\to0\).  Mass is not the lost flowing information; it is the archived information
\[
A=1-q.
\]
This resolves the apparent contradiction that decoherence does not make ordinary masses decrease.  The Euler residual mass map becomes \(m(A)=2m_p\sin(\pi A/2)/\pi\).  The direction of decoherence is supplied by a Fokker-Planck drift toward smaller \(q\), driven by the receiver capacity of low-mass degrees of freedom.  The larger conjecture is an archive-decompression cycle: when local archived information reaches a Planck critical density, the region becomes an empty quantum container and resets toward \(q\to1\).  DGF therefore treats macroscopic classicality as compressed quantum information, not missing information.

---

## I. Core Claim

The macro-world is not classical because quantum mechanics lacks something.  It is classical because flowing spatial-interference information has been archived into a locked form.  Ordinary environmental decoherence is the laboratory-scale face of this archival process.

Two quantities must be separated:

\[
q=\text{accessible / flowing coherence fraction},
\]
\[
A=1-q=\text{archived / locked information fraction}.
\]

Decoherence moves \(q\) downward and \(A\) upward.  Mass follows \(A\), not \(q\).  This is the key repair.  It prevents the false inference that a decohering stone should lose mass.

---

## II. Microscopic Definition of \(q\)

Partition the support volume \(V_S\) of a system \(S\) into Planck cells \(c\in\mathcal C_S\), with \(N_S=|\mathcal C_S|\).  Each cell carries an access weight
\[
a_c=\frac{\mathcal V_c}{\mathcal V_c^{\max}}\in[0,1],
\]
where \(\mathcal V_c\) is the local branch-recombination visibility.  Define
\[
\boxed{
q_S=\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c,
\qquad
A_S=1-q_S.
}
\]
Thus \(q_S\) is, in principle, measurable as a coarse-grained coherence-access ratio.  \(A_S\) is the archived fraction.

Operationally, \(a_c\) is not a new name for coherence; it is a visibility functional of the reduced density matrix at a specified coarse-graining scale \(\ell\).  For a causal diamond or laboratory cell \(c_\ell\),
\[
a_{c,\ell}=
\frac{
\int_{c_\ell\times c_\ell'} W_\ell(x,x')|\rho_S(x,x')|\,dx\,dx'
}{
\int_{c_\ell\times c_\ell'} W_\ell(x,x')|\rho_S^{\rm max}(x,x')|\,dx\,dx'
},
\]
where \(W_\ell\) is a normalized window and \(\rho_S^{\rm max}\) is the maximum-visibility state with the same local populations and conserved charges.  The experimentally compared quantity is
\[
q_{S,\ell}=\frac{1}{N_\ell}\sum_{c_\ell}a_{c,\ell},
\qquad
q_S=\lim_{\ell\to l_p}q_{S,\ell}
\]
when the Planck limit exists.  Thus \(q\) can be computed from an interferometric density matrix or POVM fringe visibility before it is used in the DGF dynamics.

For composite systems,
\[
q_{\rm comp}=\prod_i q_i^{w_i},
\qquad
\sum_iw_i=1,
\]
so independent accessibilities multiply.  The archived fraction is \(A_{\rm comp}=1-q_{\rm comp}\).

---

## III. Directed Archival Dynamics

There is no global pairing between heavy and light systems.  The universe does not need a ranking table.  Information disperses locally, but low-mass receiver modes have larger unfilled capacity and statistically absorb more flowing coherence.

Let \(P(q,t)\) be the probability density of accessible coherence.  DGF uses
\[
\boxed{
\partial_tP(q,t)
=-\partial_q[\mu(q)P]+\partial_q^2[D(q)P].
}
\]
For archival,
\[
\mu(q)<0,
\]
so the mean accessible coherence decreases:
\[
\frac{d\langle q\rangle}{dt}=\langle\mu(q)\rangle<0
\]
under reflecting boundaries.  The diffusion \(D(q)\) is the Planck-cell fluctuation term.  The drift is the irreversibility.

The drift is an entropy-gradient drift in the sender coordinate:
\[
\mu(q_S)=\Gamma(q_S)\partial_{q_S}S_{\rm tot}
=-\Gamma(q_S)\partial_{A_S}S_{\rm tot},
\qquad A_S=1-q_S,
\]
with \(\Gamma(q_S)>0\).  This gives a direction without global pairing.

Equivalently, the irreversible arrow is fixed by total entropy, not by a hand-assigned heavy-light ordering.  For a local transfer \(dA>0\),
\[
dS_{\rm tot}
=\left(\partial_A S_{\rm recv}-\partial_A S_{\rm cost}\right)dA .
\]
Here \(S_{\rm cost}\) is the sender-side cost of losing accessible coherence.  The receiver term is positive because the number of low-mass radiation, phonon, or graviton modes able to carry the archived record increases with the transferred record.  The condition used by DGF is therefore
\[
\partial_A S_{\rm tot}>0,
\qquad
\partial_A S_{\rm recv}>\partial_A S_{\rm cost}.
\]
Then \(\mu(q_S)<0\), so \(d\langle q_S\rangle/dt<0\) and \(d\langle A_S\rangle/dt>0\).  This is the same statistical logic by which spontaneous emission is irreversible: the atomic subsystem loses excitation, but the photon mode density supplies the dominant final-state count.  Low mass means large available mode density and weak saturation, equivalently a large \(S_{\rm recv}\) or \(J_{\rm recv}(\omega)\), not an inverse receiver mass inserted into the system operator.

This drift can be obtained rather than postulated.  Let an archival step change \(A_S\) by \(\delta A\).  The forward/backward local rates obey the final-state-count relation
\[
\frac{W(A\to A+\delta A)}
     {W(A+\delta A\to A)}
=\exp\!\left[\frac{\Delta S_{\rm tot}}{k_B}\right].
\]
A Kramers-Moyal expansion gives
\[
\mu_A(A)=\delta A[W_+-W_-],
\qquad
D_A(A)=\frac{\delta A^2}{2}[W_++W_-],
\]
and \(\mu_q=-\mu_A\).  To leading order,
\[
\mu_q(q)=-\frac{D_A(A)}{k_B}\partial_A S_{\rm tot}+O(\delta A^2),
\]
which is the Fokker-Planck drift above with mobility \(\Gamma=D_A/k_B\).  Receiver examples use \(S_{\rm recv}=k_B\ln[(A+A_0)N_{\rm recv}]\), with \(A_0\) the vacuum/background channel floor, so the \(A\to0\) limit is finite.

---

## IV. Projection Angle from Information Geometry

The accessible and archived sectors form a two-sector information state
\[
|\chi\rangle=\sqrt q\,|Q\rangle+\sqrt A\,|C\rangle,
\qquad A=1-q.
\]
\(|Q\rangle\) is flowing quantum access; \(|C\rangle\) is archived classical storage.  The archived sector occupies a normalized arc fraction \(A\) on the information half-circle, giving
\[
\boxed{\theta(A)=\pi A=\pi(1-q).}
\]
This replaces a Wick-rotation analogy with an information-geometric construction.

The linear angle is not an arbitrary choice of interval.  It is also not the claim that the Bures distance from \(\rho(0)\) to \(\rho(A)\) is itself linear.  In the \(N\)-sector version, archived information is distributed over \(N-1\) orthogonal receiver/archive channels,
\[
\rho(A)=(1-A)|Q\rangle\langle Q|
+\frac{A}{N-1}\sum_{k=2}^{N}|C_k\rangle\langle C_k|.
\]
The Bures/Fubini-Study geometry fixes only the orthogonal endpoint diameter: the accessible sector and the fully archived sector span an information half-circle of length \(\pi\).  The DGF angle is the maximum-entropy archive coordinate on that half-circle.  If \(\mu_{\rm H}\) is the Haar-induced uniform measure on unresolved archive channels,
\[
A=\frac{\mu_{\rm H}(\mathcal C_\theta)}
        {\mu_{\rm H}(\mathcal C_\pi)}
=\frac{\theta}{\pi}.
\]
For macroscopic archival, \(N\gg1\), phases between archive channels are washed out and maximum entropy gives uniform filling of the archive subspace.  Under this explicit condition,
\[
\theta(A)=\pi A+O(N^{-1}),
\]
where the correction is the finite channel-resolution error.  The coherent two-sector expression \(2\arccos\sqrt{1-A}\) describes reversible two-channel interpolation, not irreversible many-channel archival.

The coordinate is unique under three constraints: unresolved archive channels, fixed orthogonal endpoints, and coarse-graining invariance.  For \(N-1\) equiprobable archive channels,
\[
A_j=\frac{j}{N-1},\qquad
\theta_j=\pi\frac{j}{N-1}.
\]
Any nonlinear reparameterization would make the residual mass assigned to a coarse-grained union of equal archive channels depend on the order in which those channels are grouped.  The linear coordinate is therefore the maximum-entropy pushforward measure compatible with branch additivity.

---

## V. Euler Residual Mass

No archived information should give no residual mass, so
\[
R(A)=1-e^{i\pi A}.
\]
Then
\[
|R(A)|^2=2-2\cos(\pi A)=4\sin^2\left(\frac{\pi A}{2}\right),
\]
and
\[
\boxed{
m(A)=\frac{m_p}{\pi}|R(A)|
=\frac{2m_p}{\pi}\sin\left(\frac{\pi A}{2}\right).
}
\]
The endpoint is
\[
\boxed{m_{\max}=\frac{2m_p}{\pi}\simeq14\,\mu{\rm g}.}
\]

This endpoint is not a universal upper bound on the total rest mass of a composite object.  It is the closure mass of one coherent DGF archival branch, or one Planck-closure unit, under the single-branch residual \(R(A)\).  Ordinary macroscopic bodies contain many weakly coherent branches and many local closure units, so their total rest mass is additive over branches while each branch obeys the same residual endpoint.  The claim is therefore a branch-scale decoherence threshold, not a denial that kilogram-scale composite bodies exist.

The branch count is not fitted from the total mass.  A branch is a maximal Planck-closure domain with one unresolved archival phase; two domains are distinct if their cross-recombination visibility is below a fixed coarse-graining threshold \(\epsilon\).  For a composite system \(S\),
\[
\mathcal B_S=\{b\},
\qquad A_b=1-q_b,
\]
\[
m_b(A_b)=\frac{2m_p}{\pi}\sin\!\left(\frac{\pi A_b}{2}\right)
\le \frac{2m_p}{\pi}.
\]
The observed rest mass is extensive over independently closed branches,
\[
M_S^{\rm DGF}
=\sum_{b\in\mathcal B_S}m_b(A_b)
+\frac{E_{\rm bind}}{c^2}
+\frac{E_{\rm field}}{c^2}.
\]
Thus
\[
m(A_{\rm comp})\neq M_S.
\]
\(A_{\rm comp}=1-q_{\rm comp}\) measures global interference recombinability, whereas \(\{A_b\}\) supplies the additive branch masses.

The threshold is fixed dynamically, not chosen to fit mass.  Define a coherence-connectivity graph
\[
G_{ij}(t)=\frac{|\mathcal V_{ij}(t)|}
{\sqrt{\mathcal V_i(t)\mathcal V_j(t)}}.
\]
Receiver-mediated archival gives \(G_{ij}(t)=\exp[-\chi_{ij}(t)]\).  The closure threshold is the one-e-fold loss
\[
\epsilon_\ast=e^{-1},\qquad
i\sim j\ \Longleftrightarrow\ G_{ij}>\epsilon_\ast .
\]
The corresponding closure length \(\xi_{\rm cl}\) is defined by \(\chi(r=\xi_{\rm cl},t_{\rm obs})=1\), so
\[
N_{\rm br}\sim \frac{V_S}{\xi_{\rm cl}^3}
\]
for a roughly homogeneous body.  This makes the branch number a prediction of the same decoherence kernel, not a post-hoc decomposition.

Mass follows archived information \(A\).  Decoherence increases \(A\).  Therefore decoherence and mass are not opposed; they are different faces of the same archival direction.

![Mass map](figures/fig1_mass_map.png)

**Fig. 1.** The endpoint formula is unchanged, but the physical variable is archived information \(A=1-q\), not flowing coherence \(q\).

---

## VI. Receiver-Mediated Decoherence Kernel

Let \(b_\lambda\) be low-mass receiver modes with spectral density
\[
J_{\rm recv}(\omega)=\sum_\lambda |g_\lambda|^2\delta(\omega-\omega_\lambda).
\]
For concrete receiver sectors,
\[
J_{\rm recv}^{(\gamma)}(\omega)
=C_\gamma\,\omega^3 f_\gamma(\omega/\omega_c),
\qquad
J_{\rm recv}^{(g)}(\omega)
\sim C_g\frac{G}{c^5}\,Q_{ij}Q^{ij}\,\omega^3 f_g(\omega/\omega_c),
\]
where \(C_\gamma\) contains the electromagnetic polarizability or dipole coupling, \(Q_{ij}\sim m_SR_S^2\) is the source quadrupole for linearized gravity, and \(f(\omega/\omega_c)\) is the receiver form factor or cutoff.  Phonon or material environments give the corresponding material spectral law.  Different receiver sectors therefore predict different decoherence strengths through \(J_{\rm recv}\), even though the system imprint below remains the same.

The interaction is
\[
H_{\rm int}=\Lambda(A)V_S\otimes
\sum_\lambda g_\lambda(b_\lambda+b_\lambda^\dagger).
\]
The system imprint operator is
\[
V_S=\frac{p^4}{3m_S}.
\]
The receiver mass never appears in the denominator; low-mass receivers enter through their mode density, occupation, coupling, and cutoff in \(J_{\rm recv}\).  For a Gaussian thermal or vacuum receiver, the archival factor is
\[
K_{ab}(t)=e^{-\chi_{ab}(t)},
\]
with
\[
\chi_{ab}(t)=
\frac{\Lambda^2(A)}{\hbar^2}
\left(\Delta V_{ab}\right)^2
\int_0^\infty d\omega\,
J_{\rm recv}(\omega)
\coth\!\left(\frac{\hbar\omega}{2k_BT}\right)
\frac{1-\cos\omega t}{\omega^2},
\]
\[
\Delta V_{ab}
=\Delta\left\langle\frac{p^4}{3m_S}\right\rangle .
\]
For spatial cat states with identical momentum moments, the receiver still records path distinguishability.  The source imprint entering \(\chi_{ab}\) is therefore
\[
\Delta\mathcal V_{ab}
=\Delta\left\langle\frac{p^4}{3m_S}\right\rangle_{ab}
+\Delta\Phi_{\rm recv}[x_a(t),x_b(t)],
\]
where \(\Delta\Phi_{\rm recv}\) is the receiver phase or field record distinguishing the two paths.  The pure GUP expression is the local momentum-imprint limit \(\Delta\Phi_{\rm recv}\to0\), not the full spatial-decoherence kernel.

The replacement \(J_{\rm recv}\to2D_\beta\) is therefore not a new postulate; it is the local coarse-grained limit.  With experimental resolution, geometry, and Planck-cell coarse graining represented by a filter \(F_\tau(\omega)\),
\[
D_\beta^{\rm eff}(\tau)
=\frac12\int_0^\infty d\omega\,
J_{\rm recv}(\omega)
\coth\!\left(\frac{\hbar\omega}{2k_BT}\right)
F_\tau(\omega).
\]
When the filtered receiver noise is approximately flat over the system bandwidth, one recovers
\[
\boxed{
K_{ab}(t)=
\exp\!\left[
-\frac{2t_p l_p^4}{\hbar^6}
\left(\Delta\left\langle\frac{p^4}{3m_S}\right\rangle\right)^2t
\right].
}
\]
Thus the GUP kernel is the local limit of receiver-mediated archival, not a disconnected second postulate.

The matching condition is explicit:
\[
\frac{\Lambda^2(A)D_\beta^{\rm eff}}{\hbar^2}
=\frac{t_pl_p^4}{\hbar^6}.
\]
Equivalently,
\[
D_\beta^{\rm eff}
=\frac{t_pl_p^4}{\hbar^4\Lambda^2(A)}
\]
in the Planck-local GUP limit.  Away from this limit, photon, phonon, and graviton receivers replace the universal coefficient by their measured \(D_\beta^{\rm eff}\), which is a testable sector dependence rather than a contradiction.

---

## VII. Archive-Decompression Cycle

The larger conjecture is not global pairing.  It is local critical cycling:

\[
q\to0,\quad A\to1
\quad
\xrightarrow{\rho_A\sim\rho_p}
\quad
q\to1,\quad A\to0.
\]

When archived information reaches a Planck critical density, the region is effectively an empty quantum container: no flowing classical record remains to suppress quantum fluctuations.  Local quantum access is restored.  This is decompression.

The archive density is
\[
\rho_A(V)=\frac{1}{V}\sum_{b\subset V}A_b I_p,
\qquad I_p=\ln2/l_p^3,
\]
or, in energetic form,
\[
\epsilon_A(V)=\frac{1}{V}\sum_{b\subset V}m_b(A_b)c^2.
\]
The decompression trigger is the local information-density bound
\[
\rho_A\to I_p
\quad \text{or}\quad
\epsilon_A\to \rho_p c^2.
\]
Energy is conserved across the reset:
\[
dM_{\rm branch}c^2+dE_{\rm rad}+dE_{\rm field}=0.
\]
Thus \(A\to0\) is not disappearance of energy; it is conversion of archived branch energy into radiation and field degrees of freedom whose coherence access resets toward \(q\to1\).

The claim is not that ordinary stones periodically lose mass.  The claim is that sufficiently extreme archive density, plausibly in black-hole evaporation end stages or other Planck-critical regions, can reset archived information into flowing quantum degrees of freedom.

![Archive order](figures/fig4_cosmic_decoherence_order.png)

**Fig. 2.** Accessible coherence \(q\) decreases as archived information \(A=1-q\) grows.  Mass follows \(A\), not \(q\).

---

## VIII. What Remains to Prove

The revised initial hypothesis is now coherent, but it creates concrete proof burdens:

1. Define an experimentally meaningful surrogate for \(a_c\).
2. Derive \(S_{\rm recv}(A)\) for photons, phonons, gravitons, or other low-mass modes.
3. Compute \(J_{\rm recv}(\omega)\) for realistic receiver sectors.
4. Justify the information half-circle beyond the two-sector minimal model.
5. Derive the Planck critical condition \(\rho_A\sim\rho_p\) for decompression.

The non-standard predictions are:

1. a visibility kink or percolation-like transition when a single branch approaches \(m_b\to2m_p/\pi\);
2. receiver-sector dependence through \(D_\beta^{\rm eff}[J_\gamma]\), \(D_\beta^{\rm eff}[J_{\rm phonon}]\), and \(D_\beta^{\rm eff}[J_g]\), even for the same source imprint;
3. Planck-critical decompression should produce non-thermal endpoint correlations because archived branch records are released into flowable \(q\)-modes rather than erased.

---

## Data and Code Availability

Figures and numerical tables were generated with `scripts/generate_dgf_figures.py`.  The corresponding CSV files are in `data/`.  The figures are in `figures/`.
