# Supplemental Material
## Macrocosmic Decoherence as Archive-Decompression Dynamics

---

## S1. Variable Convention

The repaired DGF notation separates two quantities:

\[
q=\frac{N_{\rm accessible}}{N_{\rm total}(V)}
\]
is flowing, branch-recombinable spatial interference information.

\[
A=1-q
\]
is archived, locked, non-flowing information.

This solves the earlier contradiction:

- decoherence: \(q\downarrow\), \(A\uparrow\);
- mass: follows \(A\), not \(q\);
- no ordinary mass loss is implied by decoherence.

---

## S2. Cell Access Definition

Let
\[
a_c=\mathcal V_c/\mathcal V_c^{\max}.
\]
Then
\[
q_S=\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c,
\qquad
A_S=1-q_S.
\]
The access weight \(a_c\) is a local visibility surrogate.  In an experiment it may be estimated only after coarse graining, but conceptually it anchors \(q\) to Planck-cell accessibility instead of mass.

An operational coarse-grained definition is
\[
a_{c,\ell}=
\frac{
\int_{c_\ell\times c_\ell'}W_\ell(x,x')|\rho_S(x,x')|\,dx\,dx'
}{
\int_{c_\ell\times c_\ell'}W_\ell(x,x')|\rho_S^{\rm max}(x,x')|\,dx\,dx'
},
\]
\[
q_{S,\ell}=\frac{1}{N_\ell}\sum_{c_\ell}a_{c,\ell}.
\]
Here \(W_\ell\) is a causal-diamond or laboratory window and \(\rho_S^{\rm max}\) has the same local populations and conserved charges but maximal branch visibility.  The Planck-cell \(q_S\) is the renormalized \(\ell\to l_p\) limit; experiments compare at finite \(\ell\).

---

## S3. Archival Drift

The corrected dynamics is
\[
\partial_tP(q,t)=-\partial_q[\mu(q)P]+\partial_q^2[D(q)P].
\]
Archive direction requires
\[
\mu(q)<0.
\]
Let the receiver entropy be \(S_{\rm recv}(A)\).  Since \(A=1-q\),
\[
\mu(q)=\Gamma(q)\partial_qS_{\rm tot}(q)
=-\Gamma(q)\partial_AS_{\rm tot}(A).
\]
If total entropy grows with archived information, \(\partial_A S_{\rm tot}>0\), then \(\mu(q)<0\).  This replaces the old zero-drift white-noise-only formulation.

The sign is fixed by total entropy.  For a local archival increment \(dA>0\),
\[
dS_{\rm tot}
=\left(\partial_A S_{\rm recv}-\partial_A S_{\rm cost}\right)dA .
\]
DGF requires
\[
\partial_A S_{\rm tot}>0
\quad\Longleftrightarrow\quad
\partial_A S_{\rm recv}>\partial_A S_{\rm cost} .
\]
Here \(S_{\rm cost}\) is the sender-side entropy cost of losing accessible coherence; it replaces an ambiguous sign convention for \(S_S\).  Irreversibility comes from the larger receiver final-state count, exactly as spontaneous emission is selected by the photon mode density.  For a receiver sector with \(N_{\rm recv}(A)=N_0 e^{\alpha A}\), \(\alpha>0\),
\[
S_{\rm recv}=k_B\ln N_{\rm recv},
\qquad
\mu(q)=-\alpha k_B\Gamma(q)<0 .
\]

For thermal photon receivers in volume \(V\),
\[
N_\gamma(T)=\frac{2\zeta(3)}{\pi^2}\frac{V(k_BT)^3}{(\hbar c)^3}.
\]
If an archival record opens \(A\)-proportional coupling area to these modes,
\[
S_{\rm recv}^{(\gamma)}(A)
=k_B\ln\!\left[A\,N_\gamma(T)\,\frac{L_S}{\lambda_T}\right],
\qquad
\partial_A S_{\rm recv}^{(\gamma)}=\frac{k_B}{A}>0 ,
\]
where \(L_S\sim V_S^{1/3}\) and \(\lambda_T=\hbar c/k_BT\).  The same positive derivative follows for zero-point graviton receivers, with the sector-dependent prefactor moved into \(J_{\rm recv}\).

The Fokker-Planck form follows from local detailed balance.  Let a step change \(A\) by \(\delta A\), and define
\[
\frac{W_+}{W_-}
=\exp[\Delta S_{\rm tot}/k_B].
\]
Kramers-Moyal expansion gives
\[
\mu_A=\delta A(W_+-W_-),\qquad
D_A=\frac{\delta A^2}{2}(W_++W_-),
\]
and because \(q=1-A\),
\[
\mu_q=-\mu_A
=-\frac{D_A}{k_B}\partial_A S_{\rm tot}+O(\delta A^2).
\]
Receiver entropies should be regularized as \(S_{\rm recv}=k_B\ln[(A+A_0)N_{\rm recv}]\), where \(A_0\) is the vacuum or background receiver channel floor.

---

## S4. Angle and Residual

The two-sector information state is
\[
|\chi\rangle=\sqrt q\,|Q\rangle+\sqrt A\,|C\rangle.
\]
The archived sector occupies arc fraction \(A\), hence
\[
\theta(A)=\pi A.
\]
The precise condition behind the linear law is many-sector incoherent archival.  Let
\[
\rho(A)=(1-A)|Q\rangle\langle Q|
+\frac{A}{N-1}\sum_{k=2}^{N}|C_k\rangle\langle C_k|.
\]
The Bures/Fubini-Study geometry fixes only the orthogonal endpoint diameter, i.e. the information half-circle length \(\pi\).  The DGF angle is not the Bures distance \(2\arccos\sqrt{1-A}\); it is the maximum-entropy archive coordinate on this half-circle.  With Haar-induced uniform measure \(\mu_{\rm H}\),
\[
A=\frac{\mu_{\rm H}(\mathcal C_\theta)}
        {\mu_{\rm H}(\mathcal C_\pi)}
=\frac{\theta}{\pi}.
\]
When \(N\gg1\), archive phases are inaccessible and maximum entropy fixes uniform filling of the archive subspace.  Then
\[
\theta(A)=\pi A+O(N^{-1}).
\]
The coherent two-sector distance \(2\arccos\sqrt{1-A}\) is the opposite limit: it describes reversible two-channel motion, not irreversible macro-archival.

For finite \(N\), the maximum-entropy archive coordinate is
\[
A_j=\frac{j}{N-1},\qquad
\theta_j=\pi\frac{j}{N-1}.
\]
This is the unique coordinate that is invariant under regrouping of equiprobable unresolved archive channels.  A nonlinear coordinate would assign different residual masses to the same archive after different coarse-graining orders, violating branch additivity.

The residual is
\[
R(A)=1-e^{i\pi A},
\]
so
\[
|R(A)|=2\sin(\pi A/2).
\]
Therefore
\[
m(A)=\frac{2m_p}{\pi}\sin(\pi A/2).
\]
The endpoint \(2m_p/\pi\) is a single-branch closure value:
\[
m_{\rm branch}(A)=\frac{2m_p}{\pi}\sin(\pi A/2),
\qquad
M_{\rm composite}=\sum_{\alpha=1}^{N_{\rm br}}m_{\rm branch}^{(\alpha)} .
\]
Thus DGF predicts a branch-scale closure threshold, not an upper bound on the total rest mass of a composite macroscopic object.

More explicitly, the global composite accessibility is not the mass input:
\[
m(A_{\rm comp})\neq M_S.
\]
\(A_{\rm comp}=1-q_{\rm comp}\) measures whole-object interference visibility.  Rest mass is computed from a local branch partition
\[
\mathcal B_S=\{b\},\qquad A_b=1-q_b,
\]
where \(b\) is a maximal Planck-closure domain with one unresolved archival phase.  If the cross-visibility between two domains is below a fixed coarse-graining threshold \(\epsilon\), they are counted as distinct branches.  Then
\[
M_S^{\rm DGF}
=\sum_{b\in\mathcal B_S}
\frac{2m_p}{\pi}\sin\!\left(\frac{\pi A_b}{2}\right)
+\frac{E_{\rm bind}}{c^2}
+\frac{E_{\rm field}}{c^2}.
\]
The branch number is therefore fixed by coherence connectivity, not by fitting \(M_S\) after the fact.

The partition can be made operational through the coherence graph
\[
G_{ij}(t)=\frac{|\mathcal V_{ij}(t)|}
{\sqrt{\mathcal V_i(t)\mathcal V_j(t)}}.
\]
Receiver archival gives \(G_{ij}=\exp[-\chi_{ij}]\).  The threshold is the natural closure point
\[
\epsilon_\ast=e^{-1},
\qquad
i\sim j \iff G_{ij}>\epsilon_\ast .
\]
For a homogeneous object, define \(\xi_{\rm cl}\) by \(\chi(r=\xi_{\rm cl},t_{\rm obs})=1\).  Then
\[
N_{\rm br}\sim V_S/\xi_{\rm cl}^3.
\]

---

## S5. Receiver Spectral Density

The receiver-mediated interaction is
\[
H_{\rm int}=\Lambda(A)V_S\otimes B_{\rm recv},
\]
with
\[
B_{\rm recv}=\sum_\lambda g_\lambda(b_\lambda+b_\lambda^\dagger),
\]
and
\[
J_{\rm recv}(\omega)=\sum_\lambda |g_\lambda|^2\delta(\omega-\omega_\lambda).
\]
The system operator is
\[
V_S=p^4/(3m_S).
\]
Receiver masses do not appear in this denominator.  Low-mass receiver physics enters through \(J_{\rm recv}\).

For photon receivers,
\[
J_{\rm recv}^{(\gamma)}(\omega)
=\sum_{\mathbf k,\epsilon}|g_{\mathbf k\epsilon}|^2
\delta(\omega-c|\mathbf k|)
=C_\gamma\omega^3 f_\gamma(\omega/\omega_c) ,
\]
where \(C_\gamma\) contains the dipole, polarizability, or material coupling.  For linearized gravitational receivers,
\[
H_{\rm int}\sim m_p^{-1}h_{\mu\nu}T^{\mu\nu},
\qquad
J_{\rm recv}^{(g)}(\omega)
\sim C_g\frac{G}{c^5}Q_{ij}Q^{ij}\omega^3f_g(\omega/\omega_c),
\]
with \(Q_{ij}\sim m_SR_S^2\).  The receiver sector changes the rate through
\[
\Gamma_{ab}^{\rm recv}
=\frac{|\Delta\Lambda_{ab}|^2}{\hbar^2}
\left(\Delta\langle V_S\rangle\right)^2
S_B(\omega_{ab}),
\]
where \(S_B\) is determined by \(J_{\rm recv}\) and occupation numbers.  The old local GUP kernel follows only after taking the Markov local limit \(J_{\rm recv}\to 2D_\beta\) and \(|\Delta\Lambda_{ab}|\sim1\).

More explicitly, for a Gaussian receiver bath,
\[
K_{ab}(t)=e^{-\chi_{ab}(t)},
\]
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
The full source imprint for spatial interference is
\[
\Delta\mathcal V_{ab}
=\Delta\left\langle\frac{p^4}{3m_S}\right\rangle_{ab}
+\Delta\Phi_{\rm recv}[x_a(t),x_b(t)].
\]
The second term is the path-conditioned receiver record.  It prevents the kernel from vanishing for two spatial branches with identical momentum moments.
The effective white-noise strength is the filtered quantity
\[
D_\beta^{\rm eff}(\tau)
=\frac12\int_0^\infty d\omega\,
J_{\rm recv}(\omega)
\coth\!\left(\frac{\hbar\omega}{2k_BT}\right)
F_\tau(\omega),
\]
where \(F_\tau\) represents measurement time resolution, geometry, and Planck-cell coarse graining.  Only when this filtered noise is flat over the system bandwidth does the expression reduce to the local exponential GUP kernel.

The Planck-local matching condition is
\[
\frac{\Lambda^2(A)D_\beta^{\rm eff}}{\hbar^2}
=\frac{t_pl_p^4}{\hbar^6},
\qquad
D_\beta^{\rm eff}
=\frac{t_pl_p^4}{\hbar^4\Lambda^2(A)}.
\]
If this condition is not met, the old universal coefficient is replaced by the measured receiver-sector value \(D_\beta^{\rm eff}[J_{\rm recv}]\).

---

## S6. Archive-Decompression Criticality

The open cosmological conjecture is
\[
q\to0,\quad A\to1
\quad \xrightarrow{\rho_A\sim\rho_p}\quad
q\to1,\quad A\to0.
\]
Interpretation:

- \(q\to0\): archive complete, no branch-recombinable coherence left.
- \(\rho_A\sim\rho_p\): local archived-information density reaches Planck criticality.
- \(q\to1\): local decompression; quantum fluctuations regain dominance.

This is not global pairing.  It is local critical reset.

Define archive information density and archived energy density by
\[
\rho_A(V)=\frac{1}{V}\sum_{b\subset V}A_bI_p,\qquad
I_p=\ln2/l_p^3,
\]
\[
\epsilon_A(V)=\frac{1}{V}\sum_{b\subset V}m_b(A_b)c^2.
\]
The critical condition is
\[
\rho_A\to I_p
\quad \text{or}\quad
\epsilon_A\to\rho_pc^2.
\]
The reset conserves energy:
\[
dM_{\rm branch}c^2+dE_{\rm rad}+dE_{\rm field}=0.
\]
For black-hole endpoints, the archived branch component is released into radiation/field modes whose accessible fraction resets toward \(q\to1\).

---

## S7. Remaining Derivations

The next derivations needed are:

1. a measurable coarse-grained definition of \(a_c\);
2. receiver entropy \(S_{\rm recv}(A)\) for specific sectors;
3. \(J_{\rm recv}(\omega)\) for photons/phonons/gravitons;
4. a derivation of \(\rho_A\sim\rho_p\) from an information-density bound;
5. a bridge from archive density to black-hole evaporation end-stage observables.

Three non-standard observables should be carried into the main submission:

1. a visibility kink as \(m_b\to2m_p/\pi\);
2. receiver-sector-dependent rates through \(D_\beta^{\rm eff}[J_{\rm recv}]\);
3. non-thermal endpoint correlations from Planck-critical decompression.
