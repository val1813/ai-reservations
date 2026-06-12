"""
INSPECTOR: Adversarial Audit of RG Flow Results (Wall #3, Rounds 1-2)
======================================================================
Checks every claim made in rg_flow.py and rg_fq_derivation.py.
Tests for: numerical artifacts, circular reasoning, overclaimed novelty,
logical gaps, and consistency with known literature.
"""

import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh
from collections import deque
import json
import warnings
warnings.filterwarnings('ignore')

# Re-use the same CausalGraph class for consistency
class CausalGraph:
    def __init__(self, L, dim=3, seed=42):
        self.dim, self.L = dim, L
        self.rng = np.random.RandomState(seed)
        if dim == 1:
            self.n = L
            self.coords = np.arange(L).reshape(-1, 1)
        elif dim == 2:
            self.n = L*L
            xs, ys = np.meshgrid(np.arange(L), np.arange(L))
            self.coords = np.column_stack([xs.ravel(), ys.ravel()])
        else:
            self.n = L**3
            xs, ys, zs = np.meshgrid(np.arange(L), np.arange(L),
                                     np.arange(L), indexing='ij')
            self.coords = np.column_stack([xs.ravel(), ys.ravel(), zs.ravel()])
        self.adj = lil_matrix((self.n, self.n))
        for i in range(self.n):
            for j in range(i+1, self.n):
                diff = self.coords[i] - self.coords[j]
                if dim == 1:
                    d = min(abs(diff[0]), L - abs(diff[0]))
                elif dim == 2:
                    dx = min(abs(diff[0]), L - abs(diff[0]))
                    dy = min(abs(diff[1]), L - abs(diff[1]))
                    d = np.sqrt(dx**2 + dy**2)
                else:
                    dx = min(abs(diff[0]), L - abs(diff[0]))
                    dy = min(abs(diff[1]), L - abs(diff[1]))
                    dz = min(abs(diff[2]), L - abs(diff[2]))
                    d = np.sqrt(dx**2 + dy**2 + dz**2)
                if d <= 1.5:
                    self.adj[i,j] = 1
                    self.adj[j,i] = 1
        self.adj = self.adj.tocsr()
        self.n_edges = self.adj.nnz // 2
        self.q = np.ones(self.n)

    def insert_mass(self, M_pl):
        dist = self._bfs(self.n // 2)
        for i in range(self.n):
            d = max(dist.get(i, 1.0), 0.5)
            self.q[i] = np.exp(-M_pl / d)

    def _bfs(self, src):
        dist = {src: 0}
        qq = deque([src])
        while qq:
            u = qq.popleft()
            for v in self.adj[u].indices:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    qq.append(v)
        return dist

def rg_block(graph, block=2):
    """Same as rg_fq_derivation.py for reproducibility."""
    if graph.dim == 3:
        Ln = graph.L // block
        if Ln < 2: return None
        ng = CausalGraph(Ln, dim=3, seed=graph.rng.randint(0, 2**30))
        for bx in range(Ln):
            for by in range(Ln):
                for bz in range(Ln):
                    b = (bx * Ln + by) * Ln + bz
                    qs = []
                    for dx in range(block):
                        for dy in range(block):
                            for dz in range(block):
                                x, y, z = bx*block+dx, by*block+dy, bz*block+dz
                                if x < graph.L and y < graph.L and z < graph.L:
                                    qs.append(graph.q[(x*graph.L + y)*graph.L + z])
                    if qs:
                        ln_q_avg = np.mean([np.log(max(qi, 1e-15)) for qi in qs])
                        ng.q[b] = np.exp(ln_q_avg)
        return ng
    elif graph.dim == 2:
        Ln = graph.L // block
        if Ln < 2: return None
        ng = CausalGraph(Ln, dim=2, seed=graph.rng.randint(0, 2**30))
        for bx in range(Ln):
            for by in range(Ln):
                b = bx * Ln + by
                qs = []
                for dx in range(block):
                    for dy in range(block):
                        x, y = bx*block+dx, by*block+dy
                        if x < graph.L and y < graph.L:
                            qs.append(graph.q[x * graph.L + y])
                if qs:
                    ln_q_avg = np.mean([np.log(max(qi, 1e-15)) for qi in qs])
                    ng.q[b] = np.exp(ln_q_avg)
        return ng
    else:
        Ln = graph.L // block
        if Ln < 2: return None
        ng = CausalGraph(Ln, dim=1, seed=graph.rng.randint(0, 2**30))
        for b in range(Ln):
            qs = [graph.q[i] for i in range(b*block, min((b+1)*block, graph.n))]
            ln_q_avg = np.mean([np.log(max(qi, 1e-15)) for qi in qs])
            ng.q[b] = np.exp(ln_q_avg)
        return ng

def extract_G_eff_geom(graph):
    degrees = np.array([graph.adj[i].nnz for i in range(graph.n)], dtype=float)
    q_positive = np.maximum(graph.q, 1e-15)
    ln_q_weighted = np.average(np.log(q_positive), weights=degrees)
    sigma_geom = np.exp(ln_q_weighted)
    return 1.0 / sigma_geom if sigma_geom > 1e-10 else np.inf

# ============================================================================
# AUDIT 1: Is ln q additivity a genuine result or built-in?
# ============================================================================
print("=" * 70)
print("AUDIT 1: ln q ADDITIVITY — GENUINE OR TAUTOLOGICAL?")
print("=" * 70)

print("""
CLAIM: ln q transforms additively under RG blocking.
  ln q_eff = <ln q_micro>_block

CRITICAL QUESTION: Is this a DERIVED property or BUILT INTO the blocking?

ANALYSIS:
  In rg_block(), we explicitly compute:
    ln_q_avg = mean(log(q_i))
    q_eff = exp(ln_q_avg)

  This MEANS we chose geometric averaging. The "ln q additivity" we
  then "discover" is a TAUTOLOGY — we built it into the blocking!

  The question is: WHY is geometric averaging the correct choice?

  POSSIBLE JUSTIFICATIONS:
  A. Entropy s(q) ~ -q ln q is additive under geometric averaging
  B. Information-theoretic: q is a multiplicative channel capacity
  C. Physics: the Poisson equation for ln q is linear

  Without a first-principles derivation of WHY geometric averaging
  is correct, the "ln q additivity" result is circular.

VERDICT: WARNING — The claim "ln q additivity is derived" is overstated.
  We CHOSE geometric averaging (implicitly assuming ln q is the correct
  variable). The real question is WHY geometric averaging.
""")

# ============================================================================
# AUDIT 2: Test sensitivity to averaging method
# ============================================================================
print("=" * 70)
print("AUDIT 2: SENSITIVITY TO BLOCKING METHOD")
print("=" * 70)

print("""
What if we used arithmetic averaging instead of geometric?
  q_eff_arith = mean(q_i)
  q_eff_geom = exp(mean(ln q_i))

For q near 1: both give ~same result (q_eff ~ 1)
For q << 1: they differ significantly.
  Example: q = [0.1, 0.9]
    arithmetic: (0.1+0.9)/2 = 0.5
    geometric: exp((ln 0.1 + ln 0.9)/2) = exp((-2.303-0.105)/2) = exp(-1.204) = 0.300

This means our results are SENSITIVE to the choice of averaging.
""")

# Test sensitivity numerically
g = CausalGraph(8, dim=3, seed=42)
g.insert_mass(1.0)

print("\nNumerical test of averaging sensitivity:")
# Geometric blocking
g_geom = rg_block(g, block=2)
q_geom = np.mean(g_geom.q)

# Arithmetic blocking (hacking)
g_arith = CausalGraph(4, dim=3, seed=42)
for bx in range(4):
    for by in range(4):
        for bz in range(4):
            b = (bx*4 + by)*4 + bz
            qs = []
            for dx in range(2):
                for dy in range(2):
                    for dz in range(2):
                        x, y, z = bx*2+dx, by*2+dy, bz*2+dz
                        if x < 8 and y < 8 and z < 8:
                            qs.append(g.q[(x*8 + y)*8 + z])
            if qs:
                g_arith.q[b] = np.mean(qs)  # arithmetic
q_arith = np.mean(g_arith.q)

print(f"  Initial <q> = {np.mean(g.q):.4f}")
print(f"  Geometric blocking: <q> = {q_geom:.4f}")
print(f"  Arithmetic blocking: <q> = {q_arith:.4f}")
print(f"  Difference: {abs(q_geom - q_arith):.4f}")

# ============================================================================
# AUDIT 3: Is alpha=1 real or an artifact of the 1/<q> definition?
# ============================================================================
print("\n" + "=" * 70)
print("AUDIT 3: IS alpha=1 REAL OR CIRCULAR?")
print("=" * 70)

print("""
We defined G_eff = 1/<q> (geometric mean of q).
Then we fit G_eff = G/q^alpha and got alpha ~ 1.

But if G_eff is DEFINED as 1/<q>, then trivially G_eff = 1/<q> = <q>^{-1}.
The "fit" returns alpha=1 because we DEFINED it that way.

This is CIRCULAR REASONING.

The real question is: WHY should G_eff = 1/<q>?
We argued it's from "causal conductivity" sigma = <q>.
But this is an ANSATZ, not a derivation.

To properly derive G_eff, we need:
1. Compute the effective metric from the causal graph connectivity
2. Read off G_eff from the metric's Newtonian limit
3. Compare G_eff to <q>

None of this was done. G_eff = 1/<q> was ASSUMED, not derived.

VERDICT: FAIL — alpha ~ 1 is a tautology from the definition G_eff = 1/<q>.
  The claim "G_eff = G/q is DERIVED from causal conductivity" is false.
  It was assumed in the definition of G_eff.
""")

# ============================================================================
# AUDIT 4: Check if q = exp(-GM/rc^2) is the UNIQUE static solution
# ============================================================================
print("=" * 70)
print("AUDIT 4: IS q = exp(-GM/rc^2) THE UNIQUE SOLUTION?")
print("=" * 70)

print("""
The field equation Box q = -alpha0 * q * rho_grav was shown to be satisfied
by q = exp(-GM/rc^2).

But is this the UNIQUE solution?
- For Box q = 0 (free field), the general solution is q = A + B/r
- For Box q = source, the solution depends on boundary conditions

If q = exp(-GM/rc^2) is just ONE solution among many, we need to argue
why it's the PHYSICAL one. Possible arguments:
1. q >= 0 always (automatic for exponential)
2. q(infinity) = 1 (vacuum boundary condition)
3. q is bounded (0 <= q <= 1)

The free-field solution q = 1 - GM/(rc^2) violates q >= 0 at small r.
The exponential solution q = exp(-GM/rc^2) always satisfies 0 < q <= 1.

This is a legitimate physical selection criterion: q must stay in [0,1].
""")

# ============================================================================
# AUDIT 5: LITERATURE OVERLAP CHECK
# ============================================================================
print("=" * 70)
print("AUDIT 5: LITERATURE OVERLAP — HONEST ASSESSMENT")
print("=" * 70)

print("""
CLAIM: "DGF derives GR from information theory."

REALITY CHECK:
1. Jacobson (1995) derived Einstein equations from delta Q = T dS
   applied to local Rindler horizons. This IS "GR from thermodynamics."
   DGF uses a different entropy (causal graph entropy vs horizon entropy)
   but the LOGICAL STRUCTURE is the same.

2. DGF's result G_eff = G/q is mathematically equivalent to the dilaton
   gravity result G_eff = G e^{-2 phi} with phi = -(1/2) ln q.
   The FORM is identical. Only the INTERPRETATION differs.

3. The q-field action S = int d^4x sqrt(-g)(R/(16 pi G) - 1/2(dq)^2 - V(q))
   is the standard scalar-tensor action. DGF's s(q) determines V(q),
   but the action STRUCTURE is standard.

WHAT IS GENUINELY NEW:
A. CFOL theorem: causal topology -> QCMI (no prior art)
B. eta_0 = 1/(8 ln 2): quantitative lower bound (no prior art)
C. q = exp(-Phi/c^2) from information-theoretic derivation,
   NOT from assuming an action (mildly new — the ln q -> Poisson
   derivation path is different from standard dilaton stabilization)
D. The causal graph as a SPECIFIC discrete microstructure,
   with computable RG flow (new, but needs HPC for real verification)

WHAT IS NOT NEW:
A. Gravity from entropy (Jacobson 1995)
B. G_eff varying with a scalar field (dilaton, Brans-Dicke)
C. Exponential coupling (string theory dilaton)
D. Screening mechanisms (chameleon, symmetron)

VERDICT: DGF's gravitational sector is a scalar-tensor theory in the
  Jacobson-Verlinede-Padmanabhan emergent gravity tradition. Its novelty
  lies in the quantum information MICROPHYSICS (CFOL, QCMI, causal graph),
  not in the macrophysics (which converges to known forms).
""")

# ============================================================================
# AUDIT 6: NUMERICAL ARTIFACTS
# ============================================================================
print("=" * 70)
print("AUDIT 6: NUMERICAL ARTIFACTS IN RG FLOW")
print("=" * 70)

# Test: does the R^2=1.0000 for ln<q> vs 1/L come from too few points?
Ls = np.array([2, 4])
ln_qs = np.log(np.array([0.7675, 0.7731]))
inv_L = 1.0 / Ls

# With only 2 points, R^2 = 1.0 ALWAYS (two points define a line)
r2 = np.corrcoef(inv_L, ln_qs)[0, 1]**2
print(f"\n  WARNING: R^2 = {r2:.4f} for ln<q> vs 1/L")
print(f"  But this is based on only {len(Ls)} data points!")
print(f"  Two points ALWAYS give R^2 = 1.0 (perfect line).")
print(f"  This 'perfect correlation' is a MATHEMATICAL TRIVIALITY, not evidence.")

# Test: with more RG steps, does the linearity hold?
g2 = CausalGraph(16, dim=2, seed=42)
g2.insert_mass(1.0)

graphs = [g2]
for step in range(4):
    gn = rg_block(graphs[-1], block=2)
    if gn is None: break
    graphs.append(gn)

if len(graphs) >= 3:
    qs = [np.mean(g.q) for g in graphs[1:]]
    Ls_multi = [2**(i+1) for i in range(len(qs))]
    ln_qs_multi = np.log(np.maximum(qs, 1e-15))
    inv_L_multi = 1.0 / np.array(Ls_multi)

    r2_multi = np.corrcoef(inv_L_multi, ln_qs_multi)[0, 1]**2
    print(f"\n  With {len(qs)} RG steps (2D, L=16):")
    print(f"    R^2 = {r2_multi:.4f}")
    if r2_multi < 0.99:
        print(f"    WARNING: Linearity breaks down with more steps!")
    else:
        print(f"    Linearity holds with more steps. OK (but still depends on geometric averaging choice).")

# ============================================================================
# AUDIT 7: THE BIGGEST GAP
# ============================================================================
print("\n" + "=" * 70)
print("AUDIT 7: THE BIGGEST GAP — NO DERIVATION OF THE METRIC")
print("=" * 70)

print("""
All our RG work derives q(r) = exp(-GM/rc^2) as the static q-field profile.
But we NEVER derive the METRIC g_{mu nu} from the causal graph.

The chain "causal graph -> ln q -> Poisson -> GR" has a MISSING LINK:
  How does the causal graph connectivity determine g_{mu nu}?

We ASSUMED:
  G_eff = 1/<q>  (causal conductivity ansatz)
  But we never showed that this gives the correct metric.

The missing derivation:
  1. From the blocked causal graph at scale L, compute the effective
     light-cone structure (which edges are timelike/spacelike)
  2. From the light-cone structure, extract the metric g_{mu nu}
  3. From g_{mu nu}, read off G_eff in the Newtonian limit
  4. Compare G_eff with <q> to determine f(q)

NONE of steps 1-4 have been done. The "derivation" stops at q(r)
and then JUMPS to "therefore GR" via the Poisson equation.

VERDICT: MAJOR GAP. The causal graph -> metric mapping is not derived.
  q(r) = exp(-GM/rc^2) is derived (modulo the geometric averaging choice).
  But the connection from q(r) to the metric g_{mu nu} is ASSUMED.
""")

# ============================================================================
# FINAL VERDICT
# ============================================================================
print("=" * 70)
print("INSPECTOR FINAL VERDICT")
print("=" * 70)

audit_results = {
    "A1_ln_q_additivity": {
        "verdict": "WARNING — tautological from geometric averaging choice",
        "severity": "medium",
        "fix": "Derive geometric averaging from entropy additivity, not assume it"
    },
    "A2_sensitivity": {
        "verdict": "CONFIRMED — results depend on averaging method",
        "severity": "medium",
        "fix": "Show geometric averaging is uniquely selected by DGF axioms"
    },
    "A3_alpha_circular": {
        "verdict": "FAIL — alpha~1 is built into G_eff definition",
        "severity": "high",
        "fix": "Derive G_eff from metric, not from 1/<q> ansatz"
    },
    "A4_uniqueness": {
        "verdict": "PASS — q=exp(-GM/rc^2) is selected by q in [0,1] + boundary conditions",
        "severity": "low",
        "fix": "None needed, but make the selection argument explicit"
    },
    "A5_literature": {
        "verdict": "PASS — honest about overlaps, novelty in microphysics not macrophysics",
        "severity": "low",
        "fix": "Cite Jacobson 1995, Verlinde 2017, dilaton gravity explicitly"
    },
    "A6_numerical": {
        "verdict": "WARNING — R^2=1 from 2-point fit is trivial, not evidence",
        "severity": "medium",
        "fix": "Run more RG steps to verify linearity, use >= 5 points"
    },
    "A7_metric_gap": {
        "verdict": "FAIL — causal graph -> metric mapping not derived",
        "severity": "critical",
        "fix": "This is the real remaining wall #3. Need to derive g_{mu nu}[q]."
    },
    "overall_penetration_revised": "40% (down from 65% — A3 and A7 are significant gaps)",
    "wall_status": "Partially penetrated but not broken. The q-field is derived. The metric is not.",
    "next_must_do": "Derive g_{mu nu} from the causal graph connectivity at scale L",
}

for k, v in audit_results.items():
    if isinstance(v, dict):
        print(f"\n{k}:")
        for k2, v2 in v.items():
            print(f"  {k2}: {v2}")
    else:
        print(f"\n{k}: {v}")

with open("D:\\Claude\\ai-reservations\\DGF-Survivors\\inspector_rg_results.json", "w") as f:
    json.dump(audit_results, f, indent=2)

print("\nSaved to inspector_rg_results.json")
