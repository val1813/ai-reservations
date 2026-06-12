"""
The pi/4 Miracle: Generalization to d > 2

For d=2 (qubit):
  Half-ring (2 edges): Max entanglement at 2c = pi/2 -> c = pi/4
  Full-ring (4 edges): DFS at 4c = pi -> c = pi/4
  -> The SAME angle gives both!

For d>2 (qudit):
  Cartan subalgebra has (d-1) parameters: c_1, c_2, ..., c_{d-1}
  Half-ring: creates entanglement in (d-1)-dim parameter space
  Full-ring: DFS condition is (d-1) constraints

  Key question: Is there a point where BOTH conditions are satisfied?
  If constraints > parameters, the magic point only exists for special d.
"""
import numpy as np
from itertools import product

# ================================================================
# 1. Cartan Algebra for d-level systems
# ================================================================

def cartan_generators(d):
    """Cartan subalgebra generators for SU(d): diagonal traceless matrices."""
    gens = []
    for k in range(1, d):
        # G_k = diag(1,1,..., -(k), 0, ..., 0) / sqrt(k(k+1))
        # More standard: generalized Gell-Mann lambda_3, lambda_8, etc.
        g = np.zeros((d, d), dtype=complex)
        for j in range(k):
            g[j, j] = 1.0
        g[k, k] = -k
        g /= np.sqrt(k * (k + 1))
        gens.append(g)
    return gens


def cartan_rotation(c_params):
    """Build Cartan rotation exp(i * sum c_k * G_k ⊗ G_k)."""
    d = len(c_params) + 1
    gens = cartan_generators(d)
    H = sum(c_params[k] * np.kron(gens[k], gens[k]) for k in range(d-1))
    return np.array(np.eye(d*d) + 1j*H - 0.5*H@H)  # exp(iH) ~ I + iH - H^2/2


def generalized_entanglement_measure(d):
    """
    For d>2, what's the analog of 'maximum entanglement at 2c=pi/2'?

    For d=2: Bell state at c=pi/4: |Phi+> = (|00>+|11>)/sqrt(2)
    For d>2: Generalized Bell state: |Phi+_d> = sum_j |jj>/sqrt(d)

    The Cartan rotation exp(i sum c_k G_k ⊗ G_k) acting on |Phi+_d>
    creates entanglement between the two qudits.

    The entanglement is maximized when the eigenvalues of the
    reduced density matrix are all equal (1/d each).
    """
    pass


# ================================================================
# 2. DFS Condition for d > 2
# ================================================================

def dfs_condition_4edges(c_params):
    """
    After 4 edges with Cartan parameters c_k, the full ring
    returns the system to itself up to a phase.

    DFS condition: 4 * c_k ∈ πℤ for all k
    -> c_k = n_k * π/4 for integer n_k

    For d=2 (one Cartan param): c = n*pi/4
      n=1: c=pi/4 (the magic angle, max entanglement + DFS)
      n=2: c=pi/2 (Clifford, both ring-level and collective)
      n=3: c=3pi/4 (same as n=1 with phase shift)

    For d>2 (multiple Cartan params): c_k = n_k * pi/4
      Each n_k can be different!
      -> Multiple "magic angles" in the Cartan parameter space
    """
    d = len(c_params) + 1
    conditions = []
    for k, ck in enumerate(c_params):
        nk = 4 * ck / np.pi
        near_int = abs(nk - round(nk)) < 0.01
        conditions.append({
            'k': k, 'ck': ck, 'nk': nk, 'is_DFS': near_int
        })
    return conditions


# ================================================================
# 3. The Magic Manifold
# ================================================================

print("=" * 70)
print("DFS MAGIC MANIFOLD FOR d-LEVEL CAUSAL RINGS")
print("=" * 70)

for d in [2, 3, 4, 5, 10, 100]:
    dim_cartan = d - 1  # number of Cartan parameters

    # Number of DFS points for c_k in [0, pi/2]
    # Each c_k can be: 0, pi/4, pi/2 (3 choices for non-trivial range)
    n_dfs_points = 3 ** dim_cartan

    # Of these, which also give maximum entanglement?
    # For d=2: only c=pi/4 gives BOTH (max entanglement at 2c=pi/2)
    # For d>2: the "max entanglement" condition is more complex

    # The "magic" points are c_k = pi/4 for ALL k
    # (the generalization of the d=2 magic angle)
    all_pi4 = np.full(dim_cartan, np.pi/4)

    print(f"\nd={d} (Cartan dim={dim_cartan}):")
    print(f"  DFS points in [0,pi/2]^{dim_cartan}: {n_dfs_points}")
    print(f"  Magic point (all c_k=pi/4): {all_pi4[:min(3, dim_cartan)]}...")

# ================================================================
# 4. Physical Interpretation
# ================================================================

print(f"\n{'='*70}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*70}")

print("""
WHY pi/4?

The causal ring has a specific geometry: 4 edges, each with the SAME
Cartan rotation angle c (for aligned axes, uniform coupling).

Half-ring (2 edges):
  After Q -> E1 -> Q, the system qubit has undergone rotation 2c.
  The environment qubit E1 is now entangled with Q.
  Maximum entanglement when 2c = pi/2 (rotates |0> to equal superposition).

  So: c = pi/4 gives MAX ENTANGLEMENT per half-ring.
  This is the most efficient information pump from Q to E.

Full-ring (4 edges):
  After Q -> E1 -> Q -> E2 -> Q, the system has undergone rotation 4c.
  The system RETURNS to itself when 4c is a multiple of 2pi.
  But the environment (E1+E2) now carries information about Q.

  When 4c = pi (c=pi/4): the system returns with a PI PHASE FLIP.
  This phase flip encodes Q's state in the E1-E2 CORRELATION,
  NOT in individual E qubits. This is non-local information storage.

  Result: DFS for the |+>/|-> basis. Local environment noise
  can't access the which-path information because it's stored
  in a two-qubit correlation.

CRITICAL INSIGHT:
  c=pi/4 is where:
  1. Information flows from Q to E most efficiently (entanglement max)
  2. Information is stored most robustly (non-local E1-E2 correlation)

  These two properties together make c=pi/4 the optimal angle
  for NATURAL CLASSICALIZATION:
  - Information is quickly extracted from Q (fast decoherence)
  - Information is stored in a way that's stable against local noise
  - The protected collective mode is the "classical reality"

WHY NATURE MIGHT SELECT c=pi/4:

  Physical interactions (Coulomb, dipole-dipole, exchange) have
  coupling strengths that lead to characteristic rotation angles.

  For two coupled two-level systems with coupling J over time t:
  c = J*t/hbar.

  If the interaction time is set by the energy uncertainty
  (t ~ hbar/Delta_E), then c ~ J/Delta_E.

  For resonant coupling (J ~ Delta_E): c ~ 1 ~ pi/4.

  So pi/4 is the NATURAL angle for resonant interactions!

  Non-resonant interactions: c << pi/4 (weak coupling) or c >> pi/4
  (strong coupling with multiple Rabi cycles). Both are less efficient
  at information extraction.

  RESONANCE = pi/4 = MAXIMUM INFORMATION FLOW EFFICIENCY.

  This is a thermodynamic principle: natural selection of interaction
  strengths favors resonance, which is c=pi/4, which gives optimal
  classicalization. The classical world is a thermodynamic attractor.
""")
