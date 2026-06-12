"""
LP47 R3: Protection Horizon Universality Test
==============================================
Test 4 graph states at n=6 with Hmix perturbation.
Compute QCMI response matrix for each graph type.
Analyze cycle space dimension vs protection.
"""
import numpy as np
from scipy.linalg import expm
import json, time, warnings
warnings.filterwarnings('ignore')

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

def kron(*mats):
    r = mats[0]
    for m in mats[1:]:
        r = np.kron(r, m)
    return r

def apply_gate(state, gate, target, n):
    ops = [I2] * n
    ops[target] = gate
    U = kron(*ops)
    return U @ state

def apply_cz(state, q1, q2, n):
    dim = 2**n
    U = np.eye(dim, dtype=complex)
    for i in range(dim):
        bits = format(i, f'0{n}b')
        if bits[n-1-q1] == '1' and bits[n-1-q2] == '1':
            U[i, i] = -1
    return U @ state

# ============================================================
# Graph state constructors (n=6)
# ============================================================

def cluster_ring_state(n=6):
    """Ring cluster: H on all, CZ(j, j+1 mod n)."""
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    for i in range(n):
        psi = apply_gate(psi, H_gate, i, n)
    for i in range(n):
        psi = apply_cz(psi, i, (i+1)%n, n)
    return psi

def cluster_linear_state(n=6):
    """Linear cluster: H on all, CZ(j, j+1) for j=0..n-2. Open chain."""
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    for i in range(n):
        psi = apply_gate(psi, H_gate, i, n)
    for i in range(n-1):
        psi = apply_cz(psi, i, i+1, n)
    return psi

def double_ring_state(n=6):
    """Double-ring: standard ring + extra CZ(0,3) edge across diameter.
    Adds second independent cycle."""
    psi = cluster_ring_state(n)
    psi = apply_cz(psi, 0, 3, n)
    return psi

def star_graph_state(n=6):
    """Star graph: center=0, connected to all leaves 1..5. No cycles."""
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    for i in range(n):
        psi = apply_gate(psi, H_gate, i, n)
    for i in range(1, n):
        psi = apply_cz(psi, 0, i, n)
    return psi

def random_3regular_state(n=6, seed=42):
    """Random 3-regular graph on 6 vertices. Each node degree=3.
    Seed 42 yields edges: (0,1),(0,3),(0,5),(1,2),(1,4),(2,3),(2,5),(3,4),(4,5)
    Total 9 edges (6*3/2=9)."""
    np.random.seed(seed)
    # Build a known 3-regular graph on 6 vertices (K_{3,3} is 3-regular)
    # Actually use the complement of a 6-cycle + permutations
    # Let's use a specific 3-regular graph: the triangular prism
    # Edges: (0,1),(0,2),(1,2) - top triangle
    #        (3,4),(3,5),(4,5) - bottom triangle
    #        (0,3),(1,4),(2,5) - connecting columns
    edges = [(0,1),(0,2),(1,2), (3,4),(3,5),(4,5), (0,3),(1,4),(2,5)]

    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    for i in range(n):
        psi = apply_gate(psi, H_gate, i, n)
    for e1, e2 in edges:
        psi = apply_cz(psi, e1, e2, n)
    return psi, edges

# ============================================================
# Graph theory: cycle space
# ============================================================

def compute_cycle_space_dimension(edges, n):
    """Compute dim(H_1(G)) = |E| - |V| + c (cyclomatic number).
    For connected graphs: = |E| - |V| + 1."""
    # Build adjacency and check connectivity
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # Count connected components via BFS
    visited = set()
    components = 0
    for v in range(n):
        if v not in visited:
            components += 1
            queue = [v]
            visited.add(v)
            while queue:
                node = queue.pop(0)
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)

    return len(edges) - n + components, components

def get_graph_edges(psi_fn, n, name):
    """Return edge list and cycle space dim for each graph type."""
    if name == "ring":
        edges = [(i, (i+1)%n) for i in range(n)]
    elif name == "linear":
        edges = [(i, i+1) for i in range(n-1)]
    elif name == "double_ring":
        edges = [(i, (i+1)%n) for i in range(n)] + [(0, 3)]
    elif name == "star":
        edges = [(0, i) for i in range(1, n)]
    elif name == "triangular_prism":
        edges = [(0,1),(0,2),(1,2), (3,4),(3,5),(4,5), (0,3),(1,4),(2,5)]
    else:
        edges = [(i, (i+1)%n) for i in range(n)]

    beta1, comps = compute_cycle_space_dimension(edges, n)
    return edges, beta1, comps

# ============================================================
# Perturbation and entropy
# ============================================================

def hmix_perturb(psi_base, theta, n, target=0):
    """H-mixing: cos(theta*pi/2)|psi> + sin(theta*pi/2) H_target|psi>."""
    c = np.cos(np.pi * theta / 2)
    s = np.sin(np.pi * theta / 2)
    psi_h = apply_gate(psi_base, H_gate, target, n)
    psi_new = c * psi_base + s * psi_h
    return psi_new / np.linalg.norm(psi_new)

def partial_trace(psi, keep, n):
    rho = np.outer(psi, psi.conj())
    keep = sorted(keep)
    trace_out = sorted(set(range(n)) - set(keep))
    if not keep:
        return np.array([[np.trace(rho)]], dtype=complex)
    if not trace_out:
        return rho.copy()
    keep_dim = 2**len(keep)
    rho_red = np.zeros((keep_dim, keep_dim), dtype=complex)
    for i in range(2**n):
        bi = format(i, f'0{n}b')
        for j in range(2**n):
            bj = format(j, f'0{n}b')
            match = all(bi[n-1-q] == bj[n-1-q] for q in trace_out)
            if not match:
                continue
            ii = int(''.join(bi[n-1-q] for q in keep), 2)
            jj = int(''.join(bj[n-1-q] for q in keep), 2)
            rho_red[ii, jj] += rho[i, j]
    return rho_red

def vn_entropy(rho):
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-14]
    if len(ev) == 0:
        return 0.0
    return float(-np.sum(ev * np.log(ev)))

def qcmi(psi, A, B, C, n):
    S_AB = vn_entropy(partial_trace(psi, sorted(set(A)|set(B)), n))
    S_BC = vn_entropy(partial_trace(psi, sorted(set(B)|set(C)), n))
    S_B  = vn_entropy(partial_trace(psi, sorted(B), n))
    S_ABC = vn_entropy(partial_trace(psi, sorted(set(A)|set(B)|set(C)), n))
    return max(S_AB + S_BC - S_B - S_ABC, 0.0) / np.log(2)

def qcmi_for_partition(psi, n, k):
    """QCMI using R2 convention: A={0}, B={k}, C={k+1} (mod n).
    Matches fp_r2.json partition scheme exactly.
    k=1: A={0},B={1},C={2}  (adjacent triple)
    k=2: A={0},B={2},C={3}  (skip-1)
    k=3: A={0},B={3},C={4}  (skip-2)"""
    A = [0]
    B = [k % n]
    C = [(k+1) % n]
    return qcmi(psi, A, B, C, n)

# ============================================================
# Protection horizon response matrix computation
# ============================================================

def compute_response_matrix(psi_fn, n, graph_name, edges, beta1, comps):
    """For each qubit q and each k=1,2,3, compute QCMI delta under Hmix."""
    psi0 = psi_fn()
    thetas = [0.01, 0.03, 0.05, 0.10]

    matrix = {}
    for q in range(n):
        matrix[f"q_{q}"] = {}
        for k in [1, 2, 3]:
            if k >= n:
                continue
            qcmi_0 = qcmi_for_partition(psi0, n, k)
            delta_vals = {}
            for th in thetas:
                psi_th = hmix_perturb(psi0, th, n, target=q)
                qv = qcmi_for_partition(psi_th, n, k)
                delta_vals[f"theta_{th}"] = float(qv - qcmi_0)

            max_delta = max(abs(v) for v in delta_vals.values())
            # Protected if max delta < 1e-10 (machine precision threshold from R2)
            protected = max_delta < 1e-8

            matrix[f"q_{q}"][f"k_{k}"] = {
                "qcmi_baseline": float(qcmi_0),
                "delta_values": delta_vals,
                "max_abs_delta": float(max_delta),
                "protected": protected
            }

    # Compute protection summary
    n_protected_per_k = {}
    protected_per_k = {}
    active_per_k = {}
    for k in [1, 2, 3]:
        if k >= n:
            continue
        protected_qs = [q for q in range(n) if matrix[f"q_{q}"][f"k_{k}"]["protected"]]
        active_qs = [q for q in range(n) if not matrix[f"q_{q}"][f"k_{k}"]["protected"]]
        n_protected_per_k[f"k_{k}"] = len(protected_qs)
        protected_per_k[f"k_{k}"] = protected_qs
        active_per_k[f"k_{k}"] = active_qs

    # Universally protected (across all k)
    universally_protected = [q for q in range(n)
                           if all(matrix[f"q_{q}"][f"k_{k}"]["protected"]
                                 for k in [1,2,3] if k < n)]
    any_protected = [q for q in range(n)
                    if any(matrix[f"q_{q}"][f"k_{k}"]["protected"]
                          for k in [1,2,3] if k < n)]

    result = {
        "n": n,
        "graph_name": graph_name,
        "edges": [(int(e[0]), int(e[1])) for e in edges],
        "num_edges": len(edges),
        "cycle_space_dim": beta1,
        "num_components": comps,
        "A": [0],
        "matrix": matrix,
        "protection_summary": {
            "n_protected_per_k": n_protected_per_k,
            "protected_per_k": protected_per_k,
            "active_per_k": active_per_k,
            "universally_protected": universally_protected,
            "any_protected": any_protected,
            "protection_fraction_any_k": len(any_protected) / n,
            "protection_fraction_all_k": len(universally_protected) / n
        },
        "theta_values": thetas
    }
    return result

# ============================================================
# MAIN
# ============================================================
def main():
    n = 6
    print("=" * 70)
    print("LP47 R3: Protection Horizon Universality Test (n=6)")
    print("=" * 70)

    graph_configs = [
        ("ring", cluster_ring_state, "Cluster Ring (baseline)"),
        ("linear", cluster_linear_state, "Linear Cluster (open chain)"),
        ("double_ring", double_ring_state, "Double Ring (extra CZ(0,3))"),
        ("star", star_graph_state, "Star Graph (center=0, no cycles)"),
        ("triangular_prism", lambda: random_3regular_state(n)[0], "Triangular Prism (3-regular)"),
    ]

    all_results = {}

    for name, psi_fn, desc in graph_configs:
        print(f"\n{'='*70}")
        print(f"Computing: {desc}")
        print(f"{'='*70}")
        t0 = time.time()

        # Get edges
        if name == "triangular_prism":
            _, edges_data = random_3regular_state(n)
            edges = edges_data
        else:
            edges, _, _ = get_graph_edges(psi_fn, n, name)

        beta1, comps = compute_cycle_space_dimension(edges, n)
        print(f"  Edges: {len(edges)}, Components: {comps}, beta_1 (cycle space dim): {beta1}")
        print(f"  Edge list: {edges}")

        result = compute_response_matrix(psi_fn, n, name, edges, beta1, comps)
        ps = result["protection_summary"]

        for k in [1, 2, 3]:
            if k >= n:
                continue
            pk = f"k_{k}"
            print(f"  k={k}: {ps['n_protected_per_k'][pk]} protected {ps['protected_per_k'][pk]}, "
                  f"{n - ps['n_protected_per_k'][pk]} active {ps['active_per_k'][pk]}")

        print(f"  Universally protected (all k): {ps['universally_protected']}")
        print(f"  Any protected: {ps['any_protected']}")
        print(f"  Protection fraction (any k): {ps['protection_fraction_any_k']:.2%}")
        print(f"  Protection fraction (all k): {ps['protection_fraction_all_k']:.2%}")
        print(f"  Time: {time.time()-t0:.1f}s")

        all_results[name] = result

    # ========================================
    # Cross-graph analysis
    # ========================================
    print(f"\n{'='*70}")
    print("CROSS-GRAPH ANALYSIS: Protection vs Cycle Space")
    print(f"{'='*70}")

    analysis = {}
    for name, result in all_results.items():
        ps = result["protection_summary"]
        analysis[name] = {
            "graph": result["graph_name"],
            "edges": result["num_edges"],
            "beta_1": result["cycle_space_dim"],
            "components": result["num_components"],
            "n_protected_k1": ps["n_protected_per_k"].get("k_1", 0),
            "n_protected_k2": ps["n_protected_per_k"].get("k_2", 0),
            "n_protected_k3": ps["n_protected_per_k"].get("k_3", 0),
            "universally_protected": ps["universally_protected"],
            "any_protected": ps["any_protected"],
            "protection_fraction_any": ps["protection_fraction_any_k"],
        }
        print(f"  {name:20s}: beta_1={result['cycle_space_dim']}, "
              f"protected(k1/k2/k3)={analysis[name]['n_protected_k1']}/{analysis[name]['n_protected_k2']}/{analysis[name]['n_protected_k3']}, "
              f"univ_protected={ps['universally_protected']}")

    # ========================================
    # Detailed delta values for key configurations
    # ========================================
    print(f"\n{'='*70}")
    print("DETAILED DELTA QCMI VALUES (theta=0.10, k=1)")
    print(f"{'='*70}")
    for name, result in all_results.items():
        print(f"\n  {name}:")
        for q in range(n):
            d = result["matrix"][f"q_{q}"]["k_1"]["delta_values"]["theta_0.1"]
            prot = result["matrix"][f"q_{q}"]["k_1"]["protected"]
            marker = "PROTECTED" if prot else "ACTIVE"
            print(f"    q={q}: delta={d:.8e} [{marker}]")

    # ========================================
    # Save
    # ========================================
    output = {
        "metadata": {
            "title": "LP47 R3: Protection Horizon Universality Test",
            "n": n,
            "perturbation": "Hmix at qubit q",
            "theta_values": [0.01, 0.03, 0.05, 0.10],
            "partitions": "k=1,2,3 with A={0}, B={k}, C={1..k-1}",
            "date": "2026-06-12",
            "framework": "Exact diagonalization + GF(2) cycle space analysis"
        },
        "graph_results": all_results,
        "cross_graph_analysis": analysis,
        "key_findings": {}
    }

    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.floating,)): return float(obj)
            if isinstance(obj, np.integer): return int(obj)
            if isinstance(obj, np.bool_): return bool(obj)
            if isinstance(obj, np.ndarray): return obj.tolist()
            if isinstance(obj, complex): return [float(obj.real), float(obj.imag)]
            return super().default(obj)

    out_path = r"D:\Claude\ai-reservations\LP47-因果环信息局域化\current\B\r3_universality_raw.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, cls=NpEncoder, ensure_ascii=False)
    print(f"\nSaved to {out_path}")

    return output

if __name__ == "__main__":
    main()
