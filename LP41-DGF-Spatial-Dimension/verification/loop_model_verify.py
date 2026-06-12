"""
Loop Model Verification: n=2cos(pi/(b1+2)) -> c(b1)
=====================================================
Avoid quantum Hamiltonian issues entirely.
Use the dense O(n) loop model transfer matrix.

Mapping:
  b1=1: n=2cos(pi/3)=1     -> c=1/2 (Ising)
  b1=2: n=2cos(pi/4)=sqrt(2)-> c=7/10 (Tricritical Ising)
  b1=3: n=2cos(pi/5)=phi   -> c=4/5 (3-state Potts)

Method: Transfer matrix on strip of width L.
The free energy f(L) = -ln(Lambda_max)/L.
CFT finite-size scaling: f(L) = f_inf - pi*c/(6*L^2)
Extract c from the 1/L^2 slope.

This is CLASSICAL - pure transfer matrix diagonalization.
"""
import numpy as np
from scipy import linalg
import warnings
warnings.filterwarnings('ignore')

def loop_weight(b1):
    """n = 2cos(pi/(b1+2))"""
    return 2.0 * np.cos(np.pi / (b1 + 2))

def c_prediction(b1):
    return 1.0 - 6.0 / ((b1 + 2) * (b1 + 3))

# ============================================================
# Dense O(n) loop model on a strip
# ============================================================
# The O(n) loop model has loops with weight n.
# Non-intersecting loops on the square lattice.
# Transfer matrix adds one row of vertical edges.
#
# For a strip of width L (L vertical edges per row),
# each configuration is defined by connectivities of the L
# "dangling" loop segments at the boundary.
#
# Non-intersecting loops => planar pairings of L points.
# Number of planar pairings = Catalan number C_{L/2} for even L.

def catalan(n):
    """Catalan number C_n"""
    from math import comb
    return comb(2*n, n) // (n + 1)

def generate_connectivities(L):
    """Generate all planar pairings (non-crossing) of L points.
    Only works for even L."""
    if L % 2 != 0:
        raise ValueError("L must be even")
    if L == 0:
        return [()]
    if L == 2:
        return [((0,1),)]

    result = []
    # First point (0) pairs with some point k (k odd, since must leave even # on each side)
    for k in range(1, L, 2):
        left = generate_connectivities(k - 1)  # points 1..k-1
        right = generate_connectivities(L - k - 1)  # points k+1..L-1
        for l in left:
            for r in right:
                # Shift indices for right side
                shifted_r = tuple((a+k+1, b+k+1) for a,b in r)
                result.append(((0,k),) + l + shifted_r)
    return result

def connectivity_to_state(conn, L):
    """Convert pairing to a state label.
    Each dangling segment is either connected to another (numbered by partner)
    or forms a loop (numbered by loop count)."""
    partner = [-1] * L
    loop_count = 0
    for a, b in conn:
        partner[a] = b
        partner[b] = a
    return tuple(partner)

def transfer_matrix(L, n):
    """
    Build the transfer matrix for the dense O(n) loop model
    on a strip of width L (L even).

    States: planar pairings of L points.
    The number of states = Catalan(L/2).

    At each step, we add a row of:
    - Horizontal edges (connecting adjacent vertical lines)
    - The spectral parameter x controls edge weight

    For the dense (fully-packed) loop model at the critical point,
    the transfer matrix only depends on the loop weight n.

    Simplification: Use the Temperley-Lieb algebra on L strands.
    T = sum_{i=1}^{L-1} e_i  (the TL transfer matrix)
    where e_i acts on strands i and i+1.

    In terms of connectivities:
    e_i connects strand i to i+1, adding a factor n for each closed loop.
    """
    n_states = catalan(L//2)
    conns = generate_connectivities(L)

    # Map connectivity to index
    conn_to_idx = {connectivity_to_state(c, L): i for i, c in enumerate(conns)}

    T = np.zeros((n_states, n_states))

    for idx, conn in enumerate(conns):
        partner = list(range(L))
        for a, b in conn:
            partner[a] = b
            partner[b] = a

        # Action of each e_i
        for i in range(L-1):
            # e_i connects strands i and i+1
            # If i and i+1 are already connected: multiply by n (closed loop)
            # If i and i+1 are connected to others: rewire

            if partner[i] == i+1:
                # Already connected: closed loop -> multiply by n
                T[idx, idx] += n
            else:
                # Rewire: connect i to i+1, reconnect their old partners
                a, b = partner[i], partner[i+1]
                # New pairing: (a,b) instead of (a,i) and (b,i+1)
                new_conn_list = []
                for (x, y) in conn:
                    if (x, y) == (min(i, a), max(i, a)):
                        continue  # remove (i, a)
                    elif (x, y) == (min(i+1, b), max(i+1, b)):
                        continue  # remove (i+1, b)
                    elif x == i or x == i+1 or y == i or y == i+1:
                        continue  # remove any pair involving i or i+1
                    else:
                        new_conn_list.append((x, y))
                # Add new pair (a, b)
                if a != b:
                    new_conn_list.append((min(a,b), max(a,b)))
                # Re-sort and create new connectivity
                new_conn = tuple(sorted(new_conn_list))
                new_state = connectivity_to_state(new_conn, L)
                if new_state in conn_to_idx:
                    T[idx, conn_to_idx[new_state]] += 1.0

    return T

def extract_c_from_T(T_vals, L_vals):
    """Extract c from free energy finite-size scaling.
    f(L) = -ln(Lambda_max)/L
    f(L) = f_inf - pi*c/(6*L^2) for periodic BC
    For open BC (our case): f(L) = f_inf - pi*c/(24*L^2)
    """
    f_vals = []
    for T, L in zip(T_vals, L_vals):
        evals = linalg.eigvals(T)
        lambda_max = max(abs(evals))
        f_vals.append(-np.log(lambda_max) / L)

    f_vals = np.array(f_vals)
    L_arr = np.array(L_vals, dtype=float)

    # Fit: f(L) = f_inf + A/L^2
    # c = -24*A/pi (open BC)
    coeffs = np.polyfit(1.0/L_arr**2, f_vals, 1)
    A = coeffs[0]
    c = -24.0 * A / np.pi

    return c, f_vals, coeffs

def main():
    print("=" * 60)
    print("  Loop Model: n = 2cos(pi/(b1+2)) -> c(b1)")
    print("  Classical transfer matrix, no quantum Hilbert space")
    print("=" * 60)

    for b1 in [1, 2, 3]:
        n = loop_weight(b1)
        c_pred = c_prediction(b1)
        print(f"\n  b1={b1}: n={n:.6f}, c_pred={c_pred:.4f}")

        T_vals = []
        L_vals = []
        for L in [2, 4, 6]:
            n_states = catalan(L//2)
            print(f"    L={L} ({n_states} states): ", end="", flush=True)
            try:
                T = transfer_matrix(L, n)
                evals = linalg.eigvals(T)
                lam_max = max(abs(evals))
                f = -np.log(lam_max) / L
                print(f"Lambda_max={lam_max:.6f}, f={f:.6f}")
                T_vals.append(T)
                L_vals.append(L)
            except Exception as e:
                print(f"error: {e}")

        if len(L_vals) >= 3:
            c_extracted, f_vals, coeffs = extract_c_from_T(T_vals, L_vals)
            print(f"    c_extracted = {c_extracted:.4f} (target: {c_pred:.4f})")
        else:
            print(f"    Not enough data points for fit")

    print(f"\n{'='*60}")
    print(f"  KEY: b1 determines loop weight n=2cos(pi/(b1+2)),")
    print(f"  which determines the central charge through the")
    print(f"  dense O(n) loop model -> CFT correspondence.")
    print(f"  This is a CLASSICAL model. No quantum spin chain issues.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
