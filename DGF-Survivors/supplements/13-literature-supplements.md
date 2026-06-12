# Missing Literature Supplements for DGF-Survivors

---

## 1. Missing Citation Clusters

Each cluster identifies a body of literature that is absent from the current
`05-literature-context.md` and must be cited in at least one of the DGF papers
(S1 CFOL+eta0, Aporia, or Cencov-Petz).  For each cluster we state what the
cited work established, how it relates to DGF (competitor, precursor, tool), and
what DGF needs to do to differentiate or acknowledge it.

---

### Cluster A: Holographic Entanglement Entropy
**Priority:** HIGH — direct competition with Theorem 3 (BH entropy area law)

| Citation | Contribution |
|---|---|
| Ryu & Takayanagi (2006) *Phys. Rev. Lett.* **96**, 181602 | RT formula: `S = A / 4G` — entanglement entropy of a CFT subregion equals the area of a minimal surface in the bulk dual |
| Hubeny, Rangamani, Takayanagi (2007) *JHEP* **07**, 062 | Covariant generalisation of RT to time-dependent backgrounds (HRT formula) |
| Faulkner, Lewkowycz, Maldacena (2013) *JHEP* **11**, 074 | Quantum corrections to RT — bulk entanglement entropy adds a `O(1/G)` term |

**DGF relationship.**
T3 (BH entropy area law) gives `S \propto A` but with coefficient **2.68**
versus **1.00** in Planck units for the standard Bekenstein-Hawking formula.
DGF must explain how its area law relates to RT:

- Is `b_1(G)` the boundary dual of the bulk minimal surface?  If DGF is a
  boundary theory living on the causal graph, then `S \propto b_1(G)` might be
  the graph-theoretic analogue of `S \propto A_{\text{min}}`.
- The coefficient difference (2.68 vs 1.00) could signal that DGF's entropy is
  **not** gravitational entropy but an information-theoretic precursor — this
  needs to be stated explicitly.
- RT is derived from AdS/CFT; DGF is not AdS/CFT.  If DGF claims to reproduce
  an area law without assuming holographic duality, that is a *stronger* claim
  and must be defended with reference to RT as the benchmark.

**Required actions:**
1. Cite RT/HRT/Faulkner in the T3 section of S1.
2. Add a paragraph comparing `b_1(G)` to the minimal surface area.
3. If DGF does NOT claim a holographic dual, state this explicitly and explain
   why an area law emerges without one.

---

### Cluster B: Tensor Networks and Entanglement Renormalisation
**Priority:** HIGH — provides the mathematical tools DGF already uses implicitly

| Citation | Contribution |
|---|---|
| Vidal (2007) *Phys. Rev. Lett.* **99**, 220405 | MERA (Multi-scale Entanglement Renormalisation Ansatz) — a tensor network that realises real-space RG with explicit entanglement removal at each scale |
| Evenbly & Vidal (2009) *Phys. Rev. B* **79**, 144108 | Scale-invariant MERA — fixed-point tensors for critical systems |
| Swingle (2012) *Phys. Rev. D* **86**, 065007 | Entanglement renormalisation and holography — MERA as a discrete realisation of AdS/CFT |
| Verstraete & Cirac (2004) *Phys. Rev. A* **70**, 060302 | PEPS (Projected Entangled Pair States) — 2D tensor network ansatz for ground states of local Hamiltonians |

**DGF relationship.**
The MPO structure discovered in `11-wall-ab-verified.md` is standard tensor
network language.  The Perron-Frobenius transfer matrix is standard TEBD/DMRG
machinery.  MERA provides the exact coarse-graining protocol that DGF needs for
**Wall #3 (RG flow)**:

- MERA explicitly removes short-range entanglement at each RG step, exactly
  the operation DGF's Wall #3 needs to track `sQNM` under coarse-graining.
- The causal cone in MERA is a directed acyclic graph — isomorphic to DGF's
  causal DAG in the 1+1D case.
- Swingle's MERA/holography connection provides an independent check: if DGF's
  `b_1` area law is correct, it should reduce to the MERA holographic bound in
  the appropriate limit.

**Required actions:**
1. Cite Vidal (2007) and Evenbly & Vidal (2009) in the Wall #3 section.
2. Acknowledge that the Perron-Frobenius transfer matrix technique is standard
   DMRG/TEBD machinery.
3. Use Swingle (2012) as a bridge between DGF's graph-theoretic RG and the
   existing holographic tensor network literature.

---

### Cluster C: Stabiliser Formalism and Clifford Gates
**Priority:** MEDIUM — CFOL's QCMI = 0 result may be a rediscovery

| Citation | Contribution |
|---|---|
| Gottesman (1997) PhD thesis / Gottesman-Knill theorem | Clifford gates generate the Pauli group; circuits using only Clifford gates are classically simulable (stabiliser formalism) |
| Aaronson & Gottesman (2004) *Phys. Rev. A* **70**, 052328 | Improved simulation algorithm for stabiliser circuits with complexity `O(n^3)` |

**DGF relationship.**
CFOL's claim **"QCMI = 0 \iff Clifford gates"** is structurally identical to
the known property that stabiliser states (outputs of Clifford circuits) have
simple entanglement structure — specifically, all stabiliser states are local
unitary equivalent to graph states, for which the entanglement entropy of any
contiguous block is bounded by the number of edges crossing the cut.

**What DGF must clarify:**
- DGF's contribution is **NOT** that Clifford gates are special — that has been
  known since Gottesman (1997).
- DGF's contribution is the **converse**: that in a *causal ring topology*,
  non-Clifford gates necessarily produce non-zero QCMI.  This is a statement
  about the *topology of the causal graph*, not about the gate set per se.
- The stabiliser literature does not consider causal graph topology as a
  constraint on gate sets; DGF's causal DAG framework is the novelty.

**Required actions:**
1. Cite Gottesman (1997) and Aaronson & Gottesman (2004) in CFOL.
2. Add a sentence: "That Clifford gates produce QCMI = 0 is consistent with the
   known simplicity of stabiliser entanglement (Gottesman-Knill); the novel claim
   here is the necessity direction — in a causal ring topology, any gate outside
   the Clifford group introduces irreducibly non-zero QCMI."
3. Search for prior art on the necessity direction specifically (see Section 3).

---

### Cluster D: Entropic / Information-Theoretic Dark Energy
**Priority:** HIGH — saturated field; differentiation is essential

| Citation | Contribution |
|---|---|
| Li (2004) *Phys. Lett. B* **603**, 1 | Holographic dark energy: `\rho_\Lambda \sim 3 M_P^2 / L^2` — DE density set by the future event horizon |
| Easson, Frampton, Smoot (2011) *Phys. Lett. B* **696**, 273 | Entropic dark energy — DE from the entropy associated with the Hubble horizon |
| Verlinde (2011) *JHEP* **04**, 029 | Entropic gravity — gravity as an entropic force from holographic screens |
| Verlinde (2016) *SciPost Phys.* **2**, 016 | Emergent gravity and the dark universe — DE as elastic response of entropic spacetime |
| Padmanabhan (2005) *Phys. Rept.* **406**, 49 | Holographic gravity and the cosmological constant — `\Lambda` from the equipartition of horizon degrees of freedom |
| Cohen, Kaplan, Nelson (1999) *Phys. Rev. Lett.* **82**, 4971 | UV/IR relation — `L^3 \Lambda^4 \leq L M_P^2`, the ancestor of holographic DE |
| Wang, Abdalla, Atrio-Barandela, Pavon (2016) *Rept. Prog. Phys.* **79**, 096901 | Review of holographic dark energy models |

**DGF relationship.**
DGF's "information-theoretic dark energy" with `w_0 \approx -0.80` is one of
many entropic/informational DE models.  The field is saturated.  DGF's
differentiation claim rests on three points:

1. **`w_0 \neq -1`:** Most holographic DE models can fit `w_0 \neq -1` by
   choice of IR cutoff.  DGF must show that its `w_0 \approx -0.80` is a
   *prediction* (derived from `b_1` topology) rather than a *fit*.
2. **Topological origin:** DGF's `b_1(G)` is a discrete topological invariant,
   not a continuous horizon radius.  This is genuinely different from
   holographic DE, where `\rho_\Lambda \propto L^{-2}` with `L` a length scale.
3. **DESI texture as quench:** The connection between `b_1` topology changes
   and the DESI baryon acoustic oscillation texture is DGF's most specific
   prediction — no other entropic DE model makes this link.

**Required actions:**
1. Add a **comparison table** to the dark energy section of the Cencov-Petz
   paper with columns: Model / Origin of DE / `w_0` prediction / Free
   parameters / DESI prediction.
2. Cite all works in the table above.
3. Explicitly state: "Unlike holographic DE where `w_0` is fit from a
   continuous cutoff parameter, DGF's `w_0 \approx -0.80` is derived from
   `b_1(G)` topology and the sQNM monotonicity bound."

---

### Cluster E: Quantum Causal Models
**Priority:** MEDIUM — precursor to DGF's causal DAG approach

| Citation | Contribution |
|---|---|
| Leifer & Spekkens (2013) *Phys. Rev. A* **88**, 052130 | Quantum causal networks — a formal framework for Bayesian causal inference with quantum nodes; defines quantum conditional independence |
| Oreshkov, Costa, Brukner (2012) *Nature Commun.* **3**, 1092 | Quantum correlations without causal order — the quantum switch and indefinite causal structure |
| Chiribella, D'Ariano, Perinotti (2011) *Phys. Rev. A* **84**, 012311 | Quantum theory from informational principles — derives Hilbert space structure from operational axioms including causality |
| Allen, Barrett, Horsman, Lee, Spekkens (2017) *Phys. Rev. X* **7**, 031021 | Quantum common causes and quantum causal models — formal conditions for when quantum correlations admit a causal explanation |

**DGF relationship.**
These works established that causal structure can coexist with quantum
probabilities, and that quantum causal models support conditional independence
constraints analogous to classical d-separation.  DGF's "causal DAG" is a
specific restriction not imposed by these works:

- **DGF's constraint:** Every node carries `\leq 1` bit of classical
  information; edges are directed and carry quantum correlations.
- **Leifer-Spekkens:** No per-node capacity constraint; causality is defined
  purely by the quantum conditional independence relations.
- **Oreshkov et al.:** Causal order itself can be indefinite — DGF's DAG
  assumes definite causal order, which is a restriction.

**Required actions:**
1. Cite Leifer & Spekkens (2013) as the formal framework closest to DGF's
   causal DAG.
2. State DGF's `\leq 1` bit/node constraint as a *specialisation* of the
   general quantum causal network framework.
3. Acknowledge that Oreshkov et al. (2012) raises the question of whether
   indefinite causal order could modify DGF's conclusions — and argue why
   the definite-order case is the physically relevant limit for cosmology.

---

### Cluster F: Quantum Darwinism
**Priority:** MEDIUM — competing theory of pointer basis selection

| Citation | Contribution |
|---|---|
| Zurek (2009) *Nature Phys.* **5**, 181 | Quantum Darwinism — objective classical reality emerges because only pointer-basis information is redundantly copied into the environment |
| Riedel & Zurek (2010) *Phys. Rev. Lett.* **105**, 020404 | Quantitative demonstration of quantum Darwinism in a spin-environment model |
| Brandao, Piani, Horodecki (2015) *Nature Commun.* **6**, 7908 | Generic emergence of objectivity — under broad conditions, any quantum channel broadcasting information leads to a unique pointer basis |
| Knott, Tura, Dunjko, Sanders (2018) *Phys. Rev. Lett.* **121**, 160401 | Resource theory of quantum objectivity |

**DGF relationship.**
`05-literature-context.md` already identifies Zurek (2003-2009) as a competing
pointer basis theory, but the citations are imprecise ("Zurek 2003-2009") and
the comparison is qualitative.  DGF claims:

> Pointer basis = `\argmin_E \text{QCMI}` = Cartan axis

Zurek's einselection claims:

> Pointer basis = eigenbasis of `[H_{\text{int}}, \cdot]`

DGF says `b_1` adds an independent contribution.  The quantitative question is:

> When does the `b_1` contribution dominate `H_{\text{int}}`?

**Required actions:**
1. Cite the specific papers above, not an undifferentiated "Zurek 2003-2009".
2. Add a quantitative estimate: for what range of `b_1` does the causal
   topology contribution exceed the `H_{\text{int}}` contribution?
3. Cite Brandao et al. (2015) for the general result that objectivity emerges
   generically — DGF should explain whether its pointer basis is consistent
   with or orthogonal to the Brandao channel framework.
4. If DGF's pointer basis can be tested in a spin-environment model (Riedel &
   Zurek 2010), propose a concrete experimental signature.

---

## 2. Search Methodology Documentation

The current `05-literature-context.md` states five unique gaps with a
one-line "search strategy" column (e.g., "causal graph + quantum conditional
mutual information + topology") but provides no documentation of:

- Databases searched
- Date ranges
- Exact query strings
- Number of results returned
- How false positives were filtered
- Who performed the searches and when

### Reconstruction assessment

The claim in the current literature file (line 127) reads:

> DGF的核心创新——因果拓扑作为量子非马尔可夫性的独立自由度——在文献中无先发。

This is a **strong negative claim** (absence of prior art), which requires
strong evidence.  The current documentation does not meet the standard expected
for journal submission because:

1. **No database enumeration.**  arXiv-only searches miss INSPIRE-HEP (the
   standard for theoretical physics), Web of Science, and Google Scholar.
2. **No date range.**  Literature before ~1995 may use different terminology.
3. **No query strings.**  The column entries are concept labels, not
   reproducible Boolean queries.
4. **No result counts.**  A "0" in the "Hits" column could mean 0 out of 10
   results or 0 out of 10,000.
5. **No filtering protocol.**  How were near misses handled?

### Recommendation: Re-run the searches with documented methodology

Before submission, execute the following systematic search protocol and
document the results.  For each of the five gaps:

| Gap | Core claim | Recommended query |
|-----|-----------|-------------------|
| 1 | Causal topology controls QCMI | `("causal graph" OR "causal structure" OR "causal DAG") AND ("quantum conditional mutual information" OR "QCMI" OR "squashed entanglement") AND ("topology" OR "Betti" OR "homology")` |
| 2 | Pointer basis from causal graph | `("pointer basis" OR "pointer states" OR "einselection") AND ("causal graph" OR "causal structure" OR "causal model")` |
| 3 | Causal Glass cosmology | `"causal glass" AND ("cosmology" OR "dark energy" OR "Hubble")` |
| 4 | Information-theoretic dark energy at w0~-0.80 | `("information-theoretic" OR "informational" OR "entropic") AND ("dark energy") AND ("equation of state" OR "w0" OR "w_0")` |
| 5 | Apory as physical methodology | `("apory" OR "aporia") AND ("physics" OR "methodology" OR "principle theory")` |

**Search protocol for each query:**

1. **Databases:** arXiv (via API), INSPIRE-HEP, Web of Science, Google Scholar.
2. **Date range:** No lower bound (terminology may differ in older literature);
   upper bound = date of search execution.
3. **Record:** Number of results returned at each database.
4. **Filter:** Title screening first; abstract screening for candidates;
   full-text for any paper that appears relevant.
5. **Document:** Number of papers screened at each stage; number excluded at
   each stage; and for every paper read in full, a one-line justification of
   why it does or does not constitute prior art for the DGF claim.
6. **Independent verification:** Have a second team member execute a subset of
   the queries (at minimum, Gap 1 on INSPIRE-HEP) and report whether they find
   results the primary searcher missed.

### Use of AI tools

If AI-assisted search tools (e.g., Semantic Scholar API, Elicit, Consensus)
were used, document:
- Which tool, which date
- The exact prompt or query
- The result set size
- Any manual filtering applied to the AI output

---

## 3. Recommended Pre-Submission Actions

The following searches target specific claims that, if found to have prior art,
would weaken or invalidate DGF's novelty claims.  Execute these before
submission.

### 3.1  Causal graph + QCMI + non-Markovianity

**Goal:** Verify Gap 1 (no prior art connecting causal graph topology to QCMI).

**Query:**
```
("causal graph" OR "causal network" OR "causal DAG" OR "Bayesian network")
AND
("quantum conditional mutual information" OR "QCMI" OR "squashed entanglement"
 OR "quantum non-Markovianity")
AND
("topology" OR "Betti" OR "homology" OR "persistent homology")
```

**Databases:** arXiv, INSPIRE-HEP, Google Scholar, Web of Science.

**What would constitute prior art:** Any paper that:
- Defines a measure of non-Markovianity in terms of QCMI or squashed entanglement, AND
- Relates this measure to a topological invariant of a graph (causal or otherwise).

**Risk to DGF if found:** High.  Gap 1 is the central novelty claim.  If this
connection exists in the literature, DGF's contribution reduces to applying a
known framework to the specific case of cosmological causal graphs.

### 3.2  Pointer basis + causal / graph

**Goal:** Verify Gap 2 (no prior art connecting pointer basis emergence to
causal graph structure).

**Query:**
```
("pointer basis" OR "pointer states" OR "einselection" OR "quantum Darwinism")
AND
("causal" OR "graph" OR "network" OR "topology")
```

**Databases:** arXiv, INSPIRE-HEP, Google Scholar.

**What would constitute prior art:** Any paper that derives pointer basis
selection criteria from structural properties of a graph (interaction graph,
causal graph, or network topology).

**Risk to DGF if found:** Medium.  Even if prior art exists, DGF's specific
claim (Cartan axis = pointer basis via QCMI minimisation) may still be novel.

### 3.3  Cartan decomposition + quantum non-Markovianity

**Goal:** Verify that CFOL's algebraic formulation (SU(2^n) Cartan decomposition
applied to QCMI) is novel.

**Query:**
```
("Cartan decomposition" OR "KAK decomposition" OR "Cartan subalgebra")
AND
("quantum non-Markovianity" OR "QCMI" OR "quantum conditional mutual information")
```

**Databases:** arXiv, INSPIRE-HEP, Google Scholar.

**What would constitute prior art:** Any paper that uses Cartan decomposition to
parameterise or bound quantum conditional mutual information.

**Risk to DGF if found:** Medium-High.  The Cartan parameterisation (`\eta_0 =
1/(8 \ln 2) \approx 0.180`, Fawzi-Renner下界有效环系数) is a specific technical result in CFOL.  If it has been derived
elsewhere, the CFOL paper's technical novelty is compromised, though the
application to causal topology may still be original.

*(2026-06-09确认：单边Cartan信道Fawzi-Renner系数为2/ln2≈2.885（petz_recovery_v2.py验证），多边环有效系数η₀=1/(8ln2)≈0.180由单边系数经环拓扑修正因子1/16得到)*

### 3.4  Clifford gates and QCMI in stabiliser literature

**Goal:** Verify that the "QCMI = 0 iff Clifford" connection has not been noted
in the stabiliser formalism literature.

**Query:**
```
("Clifford" OR "stabilizer" OR "Gottesman-Knill")
AND
("quantum conditional mutual information" OR "QCMI" OR "squashed entanglement"
 OR "tripartite mutual information")
```

**Databases:** arXiv, INSPIRE-HEP, Google Scholar, Quantum journal.

**What would constitute prior art:** Any paper that notes that Clifford/stabiliser
circuits produce zero QCMI, or that non-Clifford gates are necessary for
non-zero QCMI.

**Risk to DGF if found:** Medium.  As discussed in Cluster C above, the novelty
is not the Clifford direction but the necessity direction in a causal ring
topology.  However, if even the necessity direction has prior art, CFOL's
technical core is invalidated.

### 3.5  Betti number + quantum information / entanglement

**Goal:** Verify that `b_1(G)` as a parameter controlling entanglement
properties is novel.

**Query:**
```
("Betti number" OR "Betti numbers" OR "b_1" OR "first Betti")
AND
("quantum" OR "entanglement" OR "QCMI" OR "mutual information")
```

**Databases:** arXiv, INSPIRE-HEP, Google Scholar.

**What would constitute prior art:** Any paper that relates a topological
invariant (Betti numbers, homology groups) to entanglement or quantum
information measures.

**Risk to DGF if found:** Medium-Low.  `b_1(G)` as a graph-theoretic invariant
is standard; the novelty is in its role as an sQNM order parameter.  Even if
similar connections exist (e.g., in topological quantum computing literature
where homology codes relate to entanglement), the application to non-Markovianity
is likely novel.

---

## 4. Summary of Non-Negotiable Citations

The following papers **must** appear in the references of at least one DGF
paper before submission.  Papers marked with `[EXISTING]` are already in
`05-literature-context.md`; all others are new additions from this supplement.

| # | Paper | DGF Paper | Cluster | Status |
|---|-------|-----------|---------|--------|
| 1 | Ryu & Takayanagi (2006) | S1 (T3) | A | NEW |
| 2 | Hubeny, Rangamani, Takayanagi (2007) | S1 (T3) | A | NEW |
| 3 | Faulkner, Lewkowycz, Maldacena (2013) | S1 (T3) | A | NEW |
| 4 | Vidal (2007) MERA | S1 (Wall #3) | B | NEW |
| 5 | Evenbly & Vidal (2009) | S1 (Wall #3) | B | NEW |
| 6 | Swingle (2012) | S1 (Wall #3) | B | NEW |
| 7 | Verstraete & Cirac (2004) PEPS | S1 (Wall #3) | B | NEW |
| 8 | Gottesman (1997) | S1 (CFOL) | C | NEW |
| 9 | Aaronson & Gottesman (2004) | S1 (CFOL) | C | NEW |
| 10 | Li (2004) holographic DE | Cencov-Petz | D | NEW |
| 11 | Easson, Frampton, Smoot (2011) | Cencov-Petz | D | NEW |
| 12 | Verlinde (2011, 2016) | Cencov-Petz | D | NEW |
| 13 | Padmanabhan (2005) | Cencov-Petz | D | NEW |
| 14 | Leifer & Spekkens (2013) | Aporia | E | NEW |
| 15 | Oreshkov, Costa, Brukner (2012) | Aporia | E | NEW |
| 16 | Chiribella, D'Ariano, Perinotti (2011) | Aporia | E | NEW |
| 17 | Allen et al. (2017) | Aporia | E | NEW |
| 18 | Zurek (2009) Nature Phys. | S1 (A1-A5) | F | NEW |
| 19 | Riedel & Zurek (2010) | S1 (A1-A5) | F | NEW |
| 20 | Brandao, Piani, Horodecki (2015) | S1 (A1-A5) | F | NEW |
| 21 | Gangwar et al. (2025) sQNM | S1 | — | EXISTING |
| 22 | Fawzi & Renner (2015) | S1 | — | EXISTING |
| 23 | HJPW (2004) | S1 | — | EXISTING |
| 24 | Holevo (1973) | Aporia | — | EXISTING |
| 25 | Bekenstein (1981) | Aporia | — | EXISTING |
| 26 | Cubitt et al. (2015) | Aporia | — | EXISTING |
| 27 | She (2007) JCAP | LP35 / Čencov-Petz | — | EXISTING |
| 28 | Sutter, Tomamichel, Harrow (2016) | S1 | — | EXISTING |
| 29 | Li & Winter (2014) | S1 | — | EXISTING |
| 30 | Barnum et al. (2007) | Aporia | — | EXISTING |
| 31 | Einstein (1919) | Aporia | — | EXISTING |
