"""
Monodromy between DIFFERENT ghost valleys: (+-) <-> (-+)

Physics:
  b1=1 vertex chain, |E|=4 edges, 2 environment qubit groups (E0, E1)
  E0 controls edges {0,1}; E1 controls edges {2,3}
  Ghost condition: n_E0 = +/- x, n_E1 = +/- x  (at p_eff in {0,1})

Four ghost valleys: (++), (+-), (-+), (--)

  PREVIOUS test (braid_monodromy.py): (++) -> (++) via exchange LOOP
  Both axes start near +x, trace a loop, return to +x.
  Closed loop in ordered conf space -> Berry phase ~ 0 (trivial bundle).
  THIS WAS THE WRONG TEST.

  CORRECT test: (+-) -> (-+) via axis exchange PATH.
  (+-):  n_E0 = +x, n_E1 = -x.  QCMI = 0.
  (-+):  n_E0 = -x, n_E1 = +x.  QCMI = 0.
  These are DIFFERENT ghost valleys with different sign patterns.

Key Physics Questions:
  1. Can we adiabatically deform (+-) into (-+) through the QCMI>0 region
     while keeping axes DISTINCT (in Conf_2(S2))?
  2. Is there a TOPOLOGICAL OBSTRUCTION (Z2 nontrivial)?
  3. What is the Berry phase along the exchange path?
  4. What is the minimum QCMI along the path (energy barrier)?
  5. What is the direct overlap |<psi(+-)|psi(-+)>|?

Also Test: Antipodal Transport
  - Transport n_E0 from +x to -x while n_E1 stays at -x
  - QCMI profile along this path
  - Overlap between start (+-) and end (--)
"""

import numpy as np
from numpy import (pi, sin, cos, sqrt, arccos, arctan2, exp, log, abs,
                   array, zeros, zeros_like, eye, dot, cross, outer)
import json
import time

# ==============================================================================
# 1. PHYSICS PARAMETERS
# ==============================================================================

# Cartan angles for the 4 edges (arbitrary, non-degenerate)
C_ANGLES = [0.3, 0.5, 0.7, 0.9]

# Reference direction for ghost edges
R_VEC = array([1.0, 0.0, 0.0])  # +x

# Number of discretization points for path integrals
N_PATH = 2000

# Ghost valley definitions
VALLEY_PM = (+1, -1)  # (+-) : E0=+x, E1=-x
VALLEY_MP = (-1, +1)  # (-+) : E0=-x, E1=+x
VALLEY_PP = (+1, +1)  # (++) : E0=+x, E1=+x
VALLEY_MM = (-1, -1)  # (--) : E0=-x, E1=-x

# ==============================================================================
# 2. GEOMETRY ON S2
# ==============================================================================

def nhat_to_sph(n):
    """Convert unit vector n to spherical angles (theta, phi)."""
    nx, ny, nz = n
    n_norm = sqrt(nx*nx + ny*ny + nz*nz)
    nx, ny, nz = nx/n_norm, ny/n_norm, nz/n_norm
    theta = arccos(np.clip(nz, -1.0, 1.0))
    phi = arctan2(ny, nx)
    if phi < 0:
        phi += 2*pi
    return theta, phi

def sph_to_nhat(theta, phi):
    """Convert spherical angles back to unit vector."""
    return array([sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta)])

def normalize_nhat(n):
    """Project back to unit sphere."""
    nrm = sqrt(dot(n, n))
    if nrm < 1e-15:
        return array([1.0, 0.0, 0.0])
    return n / nrm

def angle_between(n1, n2):
    """Great-circle angle between two unit vectors on S2."""
    return arccos(np.clip(dot(n1, n2), -1.0, 1.0))

def slerp(n1, n2, t):
    """Spherical linear interpolation from n1 to n2."""
    omega = angle_between(n1, n2)
    if omega < 1e-15:
        return n1.copy()
    return (sin((1-t)*omega)/sin(omega))*n1 + (sin(t*omega)/sin(omega))*n2

# ==============================================================================
# 3. EXCHANGE PATH DEFINITIONS (Conf_2(S2))
# ==============================================================================

def path_equatorial_antipodal(t):
    """Path A: Both axes in x-y plane, antipodal throughout.

    n_E0(t): +x -> +y -> -x  (phi: 0 -> pi/2 -> pi)
    n_E1(t): -x -> -y -> +x  (phi: pi -> -pi/2 -> 0)

    Axes are ALWAYS antipodal: n_E0(t) = -n_E1(t) for all t.
    Antipodal points are DISTINCT on S2, so path stays in Conf_2(S2).
    """
    phi0 = pi * t                     # 0 -> pi
    phi1 = pi * (1.0 + t)             # pi -> 2pi
    if phi1 >= 2*pi:
        phi1 -= 2*pi
    n_E0 = array([cos(phi0), sin(phi0), 0.0])
    n_E1 = array([cos(phi1), sin(phi1), 0.0])
    return n_E0, n_E1

def path_meridional_antipodal(t):
    """Path B: Both axes in x-z plane, antipodal throughout.

    n_E0(t): +x -> +z -> -x  (great circle in xz-plane)
      theta goes pi/2 -> 0 -> -pi/2, phi=0
      n_E0 = (sin(theta), 0, cos(theta)) = (cos(pi*t), 0, sin(pi*t))
      t=0: (1,0,0)=+x, t=0.5: (0,0,1)=+z, t=1: (-1,0,0)=-x

    n_E1(t): -x -> -z -> +x  (antipodal to n_E0 for all t)
      n_E1 = -n_E0 = (-cos(pi*t), 0, -sin(pi*t))
      t=0: (-1,0,0)=-x, t=0.5: (0,0,-1)=-z, t=1: (1,0,0)=+x
    """
    n_E0 = array([cos(pi * t), 0.0, sin(pi * t)])
    n_E1 = -n_E0
    return n_E0, n_E1

def path_tilted_non_antipodal(t, eps=0.3):
    """Path C: Non-antipodal path avoiding the diagonal.

    n_E0(t): in xy-plane, +x -> +y -> -x
    n_E1(t): starts at -x, ends at +x, but goes through +y with z-offset
             to avoid the diagonal (n_E0 never equals n_E1).

    The z-offset ensures axes are NEVER coincident but also NOT
    antipodal (except at endpoints where they're opposite).
    """
    # n_E0: simple rotation in xy-plane
    phi0 = pi * t
    n_E0 = array([cos(phi0), sin(phi0), 0.0])

    # n_E1: rotation in xy-plane with z-bump to avoid antipodal degeneracy
    phi1 = pi * (1.0 - t)            # pi -> 0
    z1 = eps * sin(pi * t)            # z-bump: 0 at endpoints, max at t=0.5
    r1 = sqrt(1.0 - z1*z1)
    n_E1 = array([r1 * cos(phi1), r1 * sin(phi1), z1])

    return n_E0, n_E1

def path_braid_half_twist(t, eps=0.3):
    """Path D: Non-antipodal exchange through different hemispheres.

    n_E0 goes +x -> +y -> -x in xy-plane.
    n_E1 goes -x -> -y -> +x BUT with a z-offset to avoid
    lying exactly antipodal to n_E0 (which would make the path
    symmetric and potentially miss topological features).

    At t=0.5: n_E0 = +y, n_E1 has z=eps (not exactly -y).
    """
    phi0 = pi * t
    n_E0 = array([cos(phi0), sin(phi0), 0.0])

    # n_E1: starts at -x, goes through region near -y but with a
    # z-bump to stay away from being antipodal to n_E0
    phi1 = pi * (1.0 - t)  # pi -> 0
    z1 = eps * sin(pi * t)
    r1 = sqrt(max(1.0 - z1*z1, 0.0))
    n_E1 = array([r1 * cos(phi1), r1 * sin(phi1), z1])
    n_E1 = normalize_nhat(n_E1)

    return n_E0, n_E1

# ==============================================================================
# 4. SPIN COHERENT STATES
# ==============================================================================

def spin_coherent(theta, phi):
    """Spin-1/2 coherent state |n>.
    |n> = cos(theta/2)|0> + e^{i*phi} sin(theta/2)|1>
    """
    return array([cos(theta/2), exp(1j*phi)*sin(theta/2)])

def spin_overlap(theta1, phi1, theta2, phi2):
    """<n1|n2> for spin coherent states."""
    return (cos(theta1/2)*cos(theta2/2) +
            exp(1j*(phi1 - phi2))*sin(theta1/2)*sin(theta2/2))

# ==============================================================================
# 5. EDGE PHYSICS (Gram factor / QCMI)
# ==============================================================================

def p_eff(n_hat):
    """Effective probability for ghost edge: p_eff = (1 + n.r_vec)/2.
    r_vec = +x, so p_eff = (1 + n_x)/2.
    """
    return 0.5 * (1.0 + n_hat[0])

def F_factor(p, c):
    """Gram factor for a single edge: F = 1 - 2p(1-p)(1-cos(4c))."""
    return 1.0 - 2.0 * p * (1.0 - p) * (1.0 - cos(4.0 * c))

def QCMI_gram(n_E0, n_E1):
    """QCMI = -log(|f_total|^2) = -log(prod_j F_j).

    Edges 0,1 use n_E0 with c[0], c[1].
    Edges 2,3 use n_E1 with c[2], c[3].
    """
    p0 = p_eff(n_E0)
    p1 = p_eff(n_E1)
    F0 = F_factor(p0, C_ANGLES[0])
    F1 = F_factor(p0, C_ANGLES[1])
    F2 = F_factor(p1, C_ANGLES[2])
    F3 = F_factor(p1, C_ANGLES[3])
    prod = F0 * F1 * F2 * F3
    if prod <= 0:
        return np.inf
    return -log(prod)

# ==============================================================================
# 6. PURIFICATION STATE CONSTRUCTION
# ==============================================================================

def psi_extremal(a, b, n_hat, c, sign):
    """Wavefunction <a,b|psi_{sign}(n,c)> for extremal edge state.

    |psi_+> = cos(c)|00> - i sin(c)|n,n>
    |psi_-> = cos(c)|00> + i sin(c)|n,n>
    sign = +1 for psi_+, -1 for psi_-
    """
    theta, phi = nhat_to_sph(n_hat)
    sc = spin_coherent(theta, phi)
    delta_00 = 1.0 if (a == 0 and b == 0) else 0.0
    return cos(c) * delta_00 - 1j * sign * sin(c) * sc[a] * sc[b]

def edge_ancilla_overlap(a, b, n1, p1, n2, p2, c):
    """Overlap <T[a,b](n1,c,p1)|T[a,b](n2,c,p2)> for the ancilla part.

    |T[a,b]> = sqrt(p) psi_+(a,b) |0>_A + sqrt(1-p) psi_-(a,b) |1>_A
    """
    psi_p1 = psi_extremal(a, b, n1, c, sign=+1)
    psi_m1 = psi_extremal(a, b, n1, c, sign=-1)
    psi_p2 = psi_extremal(a, b, n2, c, sign=+1)
    psi_m2 = psi_extremal(a, b, n2, c, sign=-1)
    return (sqrt(max(p1 * p2, 0)) * np.conj(psi_p1) * psi_p2 +
            sqrt(max((1.0 - p1) * (1.0 - p2), 0)) * np.conj(psi_m1) * psi_m2)

def purification_overlap(n_E0_a, n_E1_a, n_E0_b, n_E1_b):
    """<Psi(n_E0_a, n_E1_a)|Psi(n_E0_b, n_E1_b)>.

    Sum over v,e0,e1 in {0,1} of product of 4 edge ancilla overlaps.
    """
    p0a = p_eff(n_E0_a)
    p0b = p_eff(n_E0_b)
    p1a = p_eff(n_E1_a)
    p1b = p_eff(n_E1_b)

    total = 0.0 + 0.0j
    for v in [0, 1]:
        for e0 in [0, 1]:
            for e1 in [0, 1]:
                # Edge 0: (v, e0), axis n_E0, c_0
                o0 = edge_ancilla_overlap(v, e0,
                                          n_E0_a, p0a,
                                          n_E0_b, p0b, C_ANGLES[0])
                # Edge 1: (e0, v), axis n_E0, c_1
                o1 = edge_ancilla_overlap(e0, v,
                                          n_E0_a, p0a,
                                          n_E0_b, p0b, C_ANGLES[1])
                # Edge 2: (v, e1), axis n_E1, c_2
                o2 = edge_ancilla_overlap(v, e1,
                                          n_E1_a, p1a,
                                          n_E1_b, p1b, C_ANGLES[2])
                # Edge 3: (e1, v), axis n_E1, c_3
                o3 = edge_ancilla_overlap(e1, v,
                                          n_E1_a, p1a,
                                          n_E1_b, p1b, C_ANGLES[3])
                total += o0 * o1 * o2 * o3
    return total

def purification_state_norm_sq(n_E0, n_E1):
    """||Psi||^2 = <Psi|Psi>."""
    return purification_overlap(n_E0, n_E1, n_E0, n_E1).real

def normalized_overlap(n_E0_a, n_E1_a, n_E0_b, n_E1_b):
    """<psi_normalized(a)|psi_normalized(b)>."""
    ovlp = purification_overlap(n_E0_a, n_E1_a, n_E0_b, n_E1_b)
    norm_a = purification_state_norm_sq(n_E0_a, n_E1_a)
    norm_b = purification_state_norm_sq(n_E0_b, n_E1_b)
    denom = sqrt(max(norm_a * norm_b, 1e-300))
    return ovlp / denom

# ==============================================================================
# 7. GHOST VALLEY STATE CONSTRUCTION
# ==============================================================================

def ghost_axes(valley):
    """Return (n_E0, n_E1) for a ghost valley.

    valley: '++', '+-', '-+', '--'
    """
    signs = {
        '++': (+1, +1),
        '+-': (+1, -1),
        '-+': (-1, +1),
        '--': (-1, -1),
    }
    s0, s1 = signs[valley]
    n_E0 = array([float(s0), 0.0, 0.0])
    n_E1 = array([float(s1), 0.0, 0.0])
    return n_E0, n_E1

# ==============================================================================
# 8. DIRECT OVERLAP MATRIX BETWEEN ALL GHOST VALLEYS
# ==============================================================================

def compute_valley_overlap_matrix():
    """Compute |<psi(valley_i)|psi(valley_j)>| for all 4 ghost valleys.

    This reveals which valleys are connected by the purification bundle.
    """
    print("=" * 70)
    print("COMPUTATION 0: GHOST VALLEY OVERLAP MATRIX")
    print("=" * 70)
    print()

    valleys = ['++', '+-', '-+', '--']
    matrix = np.zeros((4, 4), dtype=complex)
    mag_matrix = np.zeros((4, 4))

    for i, vi in enumerate(valleys):
        for j, vj in enumerate(valleys):
            n0_i, n1_i = ghost_axes(vi)
            n0_j, n1_j = ghost_axes(vj)
            ovlp = normalized_overlap(n0_i, n1_i, n0_j, n1_j)
            matrix[i, j] = ovlp
            mag_matrix[i, j] = abs(ovlp)

    # Print matrix
    header = "       " + "".join(f"{v:>12s}" for v in valleys)
    print(header)
    print("-" * len(header))
    for i, vi in enumerate(valleys):
        row = f"  {vi:4s} "
        for j in range(4):
            row += f"{mag_matrix[i,j]:12.8f}"
        print(row)

    print()
    print("  Interpretation:")
    print(f"  |<++|+->| = {mag_matrix[0,1]:.8f}  (E0 same +x, E1 +x vs -x)")
    print(f"  |<++|-+>| = {mag_matrix[0,2]:.8f}  (E1 same +x, E0 +x vs -x)")
    print(f"  |<++|-->| = {mag_matrix[0,3]:.8f}  (both flipped)")
    print(f"  |<+-|-+>| = {mag_matrix[1,2]:.8f}  <<< KEY: cross-valley exchange >>>")
    print(f"  |<+-|-->| = {mag_matrix[1,3]:.8f}")
    print(f"  |<-+|-->| = {mag_matrix[2,3]:.8f}")

    # Analyze: which pairs are orthogonal?
    orthogonal_pairs = []
    connected_pairs = []
    for i in range(4):
        for j in range(i+1, 4):
            if mag_matrix[i,j] < 1e-10:
                orthogonal_pairs.append((valleys[i], valleys[j]))
            else:
                connected_pairs.append((valleys[i], valleys[j], mag_matrix[i,j]))

    print(f"\n  Orthogonal pairs: {orthogonal_pairs}")
    print(f"  Connected pairs (overlap > 0):")
    for pair in connected_pairs:
        print(f"    {pair[0]}<->{pair[1]}: |overlap| = {pair[2]:.8f}")

    # Expectation: <+-|-+> should be ~0 due to ancilla space orthogonality
    # Explanation: at (+-), p0=1 (ancilla=|0>), p1=0 (ancilla=|1>)
    #              at (-+), p0=0 (ancilla=|1>), p1=1 (ancilla=|0>)
    #              The ancilla spaces for each edge are different -> orthogonal

    return {
        'valleys': valleys,
        'overlap_magnitudes': mag_matrix.tolist(),
        'orthogonal_pairs': [(p[0], p[1]) for p in orthogonal_pairs],
        'connected_pairs': [(p[0], p[1], float(p[2])) for p in connected_pairs],
    }

# ==============================================================================
# 9. QCMI ALONG EXCHANGE PATHS
# ==============================================================================

def compute_qcmi_along_exchange_paths():
    """Compute QCMI along multiple exchange paths from (+-) to (-+)."""
    print("\n" + "=" * 70)
    print("COMPUTATION 1: QCMI ALONG (+-) -> (-+) EXCHANGE PATHS")
    print("=" * 70)

    paths = {
        'eq_antipodal': (path_equatorial_antipodal,
                         "Equatorial antipodal (axes always opposite in xy-plane)"),
        'mer_antipodal': (path_meridional_antipodal,
                          "Meridional antipodal (axes always opposite in xz-plane)"),
        'tilted': (path_tilted_non_antipodal,
                   "Tilted non-antipodal (z-bump avoids diagonal)"),
        'half_braid': (path_braid_half_twist,
                       "Half-braid (Z2 generator lift)"),
    }

    t_vals = np.linspace(0, 1, N_PATH)
    all_results = {}

    for path_name, (path_fn, desc) in paths.items():
        print(f"\n  Path: {path_name} — {desc}")

        qcmi_vals = np.zeros(N_PATH)
        p0_vals = np.zeros(N_PATH)
        p1_vals = np.zeros(N_PATH)
        separations = np.zeros(N_PATH)

        for i, t in enumerate(t_vals):
            n_E0, n_E1 = path_fn(t)
            qcmi_vals[i] = QCMI_gram(n_E0, n_E1)
            p0_vals[i] = p_eff(n_E0)
            p1_vals[i] = p_eff(n_E1)
            separations[i] = angle_between(n_E0, n_E1)

        # Verify endpoints
        qcmi_start = qcmi_vals[0]
        qcmi_end = qcmi_vals[-1]
        max_qcmi = np.max(qcmi_vals)
        t_max = t_vals[np.argmax(qcmi_vals)]
        min_sep = np.min(separations[1:-1])  # minimum separation in interior

        n0_start, n1_start = path_fn(0.0)
        n0_end, n1_end = path_fn(1.0)

        print(f"    Start: n_E0=({n0_start[0]:.3f},{n0_start[1]:.3f},{n0_start[2]:.3f}), "
              f"n_E1=({n1_start[0]:.3f},{n1_start[1]:.3f},{n1_start[2]:.3f})")
        print(f"    End:   n_E0=({n0_end[0]:.3f},{n0_end[1]:.3f},{n0_end[2]:.3f}), "
              f"n_E1=({n1_end[0]:.3f},{n1_end[1]:.3f},{n1_end[2]:.3f})")
        print(f"    QCMI(t=0):      {qcmi_start:.12f}")
        print(f"    QCMI(t=1):      {qcmi_end:.12f}")
        print(f"    QCMI max:       {max_qcmi:.8f} at t={t_max:.4f}")
        print(f"    QCMI avg:       {np.mean(qcmi_vals[1:-1]):.8f}")
        print(f"    Min separation: {np.rad2deg(min_sep):.2f} deg")
        print(f"    QCMI>0 inside:  {np.all(qcmi_vals[1:-1] > 1e-12)}")

        # QCMI symmetry check
        qcmi_sym = np.max(np.abs(qcmi_vals - qcmi_vals[::-1]))
        print(f"    QCMI symmetry:  {qcmi_sym:.2e} (QCMI(t) vs QCMI(1-t))")

        # Verify p_eff endpoints
        print(f"    p0: {p0_vals[0]:.6f} -> {p0_vals[-1]:.6f}")
        print(f"    p1: {p1_vals[0]:.6f} -> {p1_vals[-1]:.6f}")

        all_results[path_name] = {
            'description': desc,
            'qcmi_start': float(qcmi_start),
            'qcmi_end': float(qcmi_end),
            'qcmi_max': float(max_qcmi),
            't_max': float(t_max),
            'qcmi_mean_interior': float(np.mean(qcmi_vals[1:-1])),
            'min_separation_deg': float(np.rad2deg(min_sep)),
            'symmetry_error': float(qcmi_sym),
            'n_path_points': N_PATH,
        }

    return all_results

# ==============================================================================
# 10. BERRY PHASE ALONG EXCHANGE PATHS
# ==============================================================================

def compute_berry_phase_for_path(path_fn, path_name):
    """Compute Berry phase along a specific exchange path.

    Berry phase gamma = -Im log Pi_k <psi_k|psi_{k+1}>
    """
    t_vals = np.linspace(0, 1, N_PATH)

    berry_sum = 0.0
    overlap_mags = np.zeros(N_PATH - 1)
    overlap_phases = np.zeros(N_PATH - 1)

    for i in range(N_PATH - 1):
        n0_a, n1_a = path_fn(t_vals[i])
        n0_b, n1_b = path_fn(t_vals[i+1])

        ovlp = normalized_overlap(n0_a, n1_a, n0_b, n1_b)

        mag = abs(ovlp)
        ph = np.angle(ovlp)
        if np.isnan(ph):
            ph = 0.0
            mag = 1.0

        overlap_mags[i] = mag
        overlap_phases[i] = ph
        berry_sum += ph

    # Normalize to [-pi, pi)
    berry_phase = berry_sum % (2*pi)
    if berry_phase > pi:
        berry_phase -= 2*pi

    # Direct start-end overlap
    n0_start, n1_start = path_fn(0.0)
    n0_end, n1_end = path_fn(1.0)
    direct_ovlp = normalized_overlap(n0_start, n1_start, n0_end, n1_end)

    # Minimum overlap magnitude (measures "closest approach" in state space)
    min_overlap_mag = np.min(overlap_mags)

    return {
        'berry_phase': float(berry_phase),
        'berry_phase_over_pi': float(berry_phase / pi),
        'direct_overlap_magnitude': float(abs(direct_ovlp)),
        'direct_overlap_phase': float(np.angle(direct_ovlp)),
        'direct_overlap_real': float(direct_ovlp.real),
        'direct_overlap_imag': float(direct_ovlp.imag),
        'min_overlap_mag': float(min_overlap_mag),
        'mean_overlap_mag': float(np.mean(overlap_mags)),
        'n_points': N_PATH,
    }

def compute_all_berry_phases():
    """Compute Berry phase for all exchange paths."""
    print("\n" + "=" * 70)
    print("COMPUTATION 2: BERRY PHASES ALONG (+-) -> (-+) EXCHANGE PATHS")
    print("=" * 70)

    paths = {
        'eq_antipodal': (path_equatorial_antipodal,
                         "Equatorial antipodal"),
        'mer_antipodal': (path_meridional_antipodal,
                          "Meridional antipodal"),
        'tilted': (path_tilted_non_antipodal,
                   "Tilted non-antipodal"),
        'half_braid': (path_braid_half_twist,
                       "Half-braid (Z2 generator lift)"),
    }

    all_berry = {}
    for path_name, (path_fn, desc) in paths.items():
        print(f"\n  Path: {path_name} — {desc}")
        result = compute_berry_phase_for_path(path_fn, path_name)

        print(f"    Berry phase:           {result['berry_phase']:.8f}")
        print(f"    Berry phase / pi:      {result['berry_phase_over_pi']:.8f}")
        print(f"    Direct |<start|end>|:  {result['direct_overlap_magnitude']:.8f}")
        print(f"    Direct overlap phase:  {result['direct_overlap_phase']:.8f}")
        print(f"    Direct overlap real:   {result['direct_overlap_real']:.8f}")
        print(f"    Min step |overlap|:    {result['min_overlap_mag']:.8f}")
        print(f"    Mean step |overlap|:   {result['mean_overlap_mag']:.8f}")

        # Classify
        bp = result['berry_phase']
        is_zero = abs(bp) < 0.01
        is_pi = abs(abs(bp) - pi) < 0.01
        result['is_zero'] = bool(is_zero)
        result['is_pi'] = bool(is_pi)
        result['classification'] = ('Z2 TRIVIAL (Berry=0)' if is_zero else
                                     'Z2 NON-TRIVIAL (Berry=pi)' if is_pi else
                                     'UNEXPECTED')

        print(f"    Classification:        {result['classification']}")

        all_berry[path_name] = result

    # Check path-independence
    berry_phases = [r['berry_phase'] for r in all_berry.values()]
    bp_spread = max(berry_phases) - min(berry_phases)
    print(f"\n  Berry phase spread across paths: {bp_spread:.8f}")
    print(f"  Path-independent? {'YES' if bp_spread < 0.01 else 'NO (path-dependent = geometric, not topological)'}")

    return all_berry

# ==============================================================================
# 11. ANTIPODAL TRANSPORT TEST
# ==============================================================================

def compute_antipodal_transport():
    """Transport n_E0 from +x to -x while n_E1 stays at -x.

    This takes us from (+-) to (--) valley.

    As soon as n_E0 leaves +x, p_eff(E0) < 1, and QCMI becomes positive.
    The QCMI profile reveals the "energy barrier" for single-axis transport.
    """
    print("\n" + "=" * 70)
    print("COMPUTATION 3: ANTIPODAL TRANSPORT (+-) -> (--)")
    print("=" * 70)

    t_vals = np.linspace(0, 1, N_PATH)
    qcmi_vals = np.zeros(N_PATH)
    p0_vals = np.zeros(N_PATH)

    for i, t in enumerate(t_vals):
        # n_E0: great circle from +x to -x in xy-plane
        phi = pi * t
        n_E0 = array([cos(phi), sin(phi), 0.0])
        # n_E1: fixed at -x
        n_E1 = array([-1.0, 0.0, 0.0])

        qcmi_vals[i] = QCMI_gram(n_E0, n_E1)
        p0_vals[i] = p_eff(n_E0)

    # Key metrics
    qcmi_start = qcmi_vals[0]
    qcmi_end = qcmi_vals[-1]
    max_qcmi = np.max(qcmi_vals)
    t_max = t_vals[np.argmax(qcmi_vals)]

    print(f"\n  n_E1 fixed at: (-1, 0, 0) [constant]")
    print(f"  n_E0: +x -> -x along great circle in xy-plane")
    print(f"  QCMI(t=0) (+- valley):   {qcmi_start:.12f}")
    print(f"  QCMI(t=1) (-- valley):   {qcmi_end:.12f}")
    print(f"  Max QCMI along path:     {max_qcmi:.8f} at t={t_max:.4f}")
    print(f"  QCMI > 0 for interior:   {np.all(qcmi_vals[1:-1] > 1e-12)}")

    # QCMI profile shape: should be symmetric since p_eff goes 1->0.5->0
    qcmi_sym = np.max(np.abs(qcmi_vals - qcmi_vals[::-1]))
    print(f"  QCMI symmetry:           {qcmi_sym:.2e}")

    # Find t where p_eff = 0.5 (maximum QCMI expected)
    t_half_idx = np.argmin(np.abs(p0_vals - 0.5))
    t_half = t_vals[t_half_idx]
    qcmi_at_half = qcmi_vals[t_half_idx]
    print(f"  QCMI at p=0.5 (t={t_half:.4f}): {qcmi_at_half:.8f}")

    # Berry phase
    berry_sum = 0.0
    for i in range(N_PATH - 1):
        n0_a = array([cos(pi*t_vals[i]), sin(pi*t_vals[i]), 0.0])
        n0_b = array([cos(pi*t_vals[i+1]), sin(pi*t_vals[i+1]), 0.0])
        n1_fixed = array([-1.0, 0.0, 0.0])

        ovlp = normalized_overlap(n0_a, n1_fixed, n0_b, n1_fixed)
        ph = np.angle(ovlp)
        if not np.isnan(ph):
            berry_sum += ph

    berry_phase = berry_sum % (2*pi)
    if berry_phase > pi:
        berry_phase -= 2*pi

    # Direct overlap: start (+-) vs end (--)
    n0_start = array([1.0, 0.0, 0.0])
    n0_end = array([-1.0, 0.0, 0.0])
    n1_fixed = array([-1.0, 0.0, 0.0])
    direct_ovlp = normalized_overlap(n0_start, n1_fixed, n0_end, n1_fixed)

    print(f"\n  Berry phase:             {berry_phase:.8f} = {berry_phase/pi:.6f} * pi")
    print(f"  Direct |<+-|-->|:        {abs(direct_ovlp):.8f}")
    print(f"  Direct overlap phase:    {np.angle(direct_ovlp):.8f}")

    return {
        'qcmi_start': float(qcmi_start),
        'qcmi_end': float(qcmi_end),
        'qcmi_max': float(max_qcmi),
        't_max': float(t_max),
        'qcmi_at_p_half': float(qcmi_at_half),
        't_p_half': float(t_half),
        'symmetry_error': float(qcmi_sym),
        'berry_phase': float(berry_phase),
        'berry_phase_over_pi': float(berry_phase / pi),
        'direct_overlap_magnitude': float(abs(direct_ovlp)),
        'direct_overlap_phase': float(np.angle(direct_ovlp)),
        'n_path_points': N_PATH,
    }

# ==============================================================================
# 12. ANTIPODAL TRANSPORT: ALL FOUR SINGLE-AXIS PATHS
# ==============================================================================

def compute_all_single_axis_transports():
    """Transport each axis individually, profiling QCMI and Berry phase.

    Four paths:
      A: (+-) -> (--): E0 moves +x->-x, E1 fixed at -x
      B: (+-) -> (++): E1 moves -x->+x, E0 fixed at +x
      C: (-+) -> (--): E0 moves -x->+x, E1 fixed at +x
      D: (-+) -> (++): E1 moves +x->-x, E0 fixed at -x

    Each path takes us from one ghost valley to an adjacent valley
    (differing by one sign flip).
    """
    print("\n" + "=" * 70)
    print("COMPUTATION 4: ALL SINGLE-AXIS TRANSPORTS")
    print("=" * 70)

    transports = [
        {
            'name': 'E0_move_(+-)_to_(--)',
            'start_valley': '+-',
            'end_valley': '--',
            'moving_axis': 'E0',
            # E0: +x -> -x via great circle in xy-plane
            'n_E1_fixed': array([-1.0, 0.0, 0.0]),
            'get_axes': lambda t: (
                array([cos(pi*t), sin(pi*t), 0.0]),  # E0 goes +x -> +y -> -x
                array([-1.0, 0.0, 0.0])               # E1 fixed at -x
            ),
        },
        {
            'name': 'E1_move_(+-)_to_(++)',
            'start_valley': '+-',
            'end_valley': '++',
            'moving_axis': 'E1',
            # E1: -x -> +x via great circle in xy-plane
            'n_E0_fixed': array([1.0, 0.0, 0.0]),
            'get_axes': lambda t: (
                array([1.0, 0.0, 0.0]),                # E0 fixed at +x
                array([cos(pi*(1.0-t)), sin(pi*(1.0-t)), 0.0])  # E1 goes -x -> -y -> +x
            ),
        },
        {
            'name': 'E0_move_(-+)_to_(++)',
            'start_valley': '-+',
            'end_valley': '++',
            'moving_axis': 'E0',
            # E0: -x -> +x via great circle in xz-plane
            'n_E1_fixed': array([1.0, 0.0, 0.0]),
            'get_axes': lambda t: (
                array([cos(pi*(1.0-t)), 0.0, sin(pi*(1.0-t))]),  # E0 goes -x -> +z -> +x
                array([1.0, 0.0, 0.0])                            # E1 fixed at +x
            ),
        },
        {
            'name': 'E1_move_(-+)_to_(--)',
            'start_valley': '-+',
            'end_valley': '--',
            'moving_axis': 'E1',
            # E1: +x -> -x via great circle in xz-plane
            'n_E0_fixed': array([-1.0, 0.0, 0.0]),
            'get_axes': lambda t: (
                array([-1.0, 0.0, 0.0]),                           # E0 fixed at -x
                array([cos(pi*t), 0.0, sin(pi*t)])                 # E1 goes +x -> +z -> -x
            ),
        },
    ]

    results = {}
    for trans in transports:
        name = trans['name']
        moving = trans['moving_axis']
        get_axes = trans['get_axes']
        print(f"\n  {name} (moving {moving}):")

        t_vals_trans = np.linspace(0, 1, 500)
        qcmi_trans = np.zeros(500)

        for i, t in enumerate(t_vals_trans):
            n0, n1 = get_axes(t)
            qcmi_trans[i] = QCMI_gram(n0, n1)

        # Berry phase
        berry_sum = 0.0
        for i in range(499):
            n0_a, n1_a = get_axes(t_vals_trans[i])
            n0_b, n1_b = get_axes(t_vals_trans[i+1])
            ovlp = normalized_overlap(n0_a, n1_a, n0_b, n1_b)
            phase = np.angle(ovlp)
            if not np.isnan(phase):
                berry_sum += phase

        berry = berry_sum % (2*pi)
        if berry > pi:
            berry -= 2*pi

        print(f"    QCMI max:      {np.max(qcmi_trans):.8f} at t={t_vals_trans[np.argmax(qcmi_trans)]:.4f}")
        print(f"    QCMI at midpoint: {qcmi_trans[250]:.8f}")
        print(f"    Berry phase:   {berry:.8f} = {berry/pi:.6f} * pi")
        print(f"    QCMI>0 inside: {np.all(qcmi_trans[1:-1] > 1e-12)}")
        print(f"    QCMI symmetry: {np.max(np.abs(qcmi_trans - qcmi_trans[::-1])):.2e}")

        results[name] = {
            'qcmi_max': float(np.max(qcmi_trans)),
            'qcmi_midpoint': float(qcmi_trans[250]),
            'qcmi_start': float(qcmi_trans[0]),
            'qcmi_end': float(qcmi_trans[-1]),
            'berry_phase': float(berry),
            'berry_phase_over_pi': float(berry / pi),
            'moving_axis': moving,
            'start_valley': trans['start_valley'],
            'end_valley': trans['end_valley'],
        }

    return results

# ==============================================================================
# 13. ANALYTICAL CHECK: WHY IS |<+-|-+>| = 0?
# ==============================================================================

def analyze_ancilla_orthogonality():
    """Analyze why the direct overlap between (+-) and (-+) is zero."""
    print("\n" + "=" * 70)
    print("COMPUTATION 5: ANALYTICAL ANALYSIS OF CROSS-VALLEY OVERLAP")
    print("=" * 70)

    # At (+-): p0=1, p1=0
    # At (-+): p0=0, p1=1
    #
    # Edge ancilla: |T[a,b]> = sqrt(p) psi_+ |0>_A + sqrt(1-p) psi_- |1>_A
    #
    # For p1=1, p2=0:
    #   <T(p1)|T(p2)> = sqrt(1*0) conj(psi_+)psi_+ + sqrt(0*1) conj(psi_-)psi_- = 0
    #
    # This is true for ALL (a,b) values! The ancilla overlap vanishes identically
    # due to the sqrt(p1*p2) and sqrt((1-p1)(1-p2)) factors.

    print("\n  Edge ancilla structure:")
    print("  |T[p, n, c]>(a,b)> = sqrt(p) psi_+(a,b,n,c) |0>_A + sqrt(1-p) psi_-(a,b,n,c) |1>_A")
    print()
    print("  (+-) valley: p0 = p_eff(+x) = 1,  p1 = p_eff(-x) = 0")
    print("  (-+) valley: p0 = p_eff(-x) = 0,  p1 = p_eff(+x) = 1")
    print()
    print("  Overlap <T[p=1]|T[p=0]> = sqrt(1*0)*psi_+*psi_+ + sqrt(0*1)*psi_-*psi_- = 0")
    print("  This vanishes IDENTICALLY for all edge configurations (a,b).")
    print()
    print("  CONSEQUENCE:")
    print("  The direct overlap |<psi(+-)|psi(-+)>| = 0 is ENFORCED by the")
    print("  ancilla space structure, NOT by a topological obstruction.")
    print("  It reflects the fact that p=1 and p=0 correspond to different")
    print("  ancilla basis states (|0>_A vs |1>_A), which are orthogonal.")

    # Verify numerically for a single edge
    print("\n  Numerical verification for a single edge (c=0.3):")
    c = C_ANGLES[0]
    n_plus_x = array([1.0, 0.0, 0.0])
    n_minus_x = array([-1.0, 0.0, 0.0])

    total_edge_overlap = 0.0 + 0.0j
    for a in [0, 1]:
        for b in [0, 1]:
            ovlp = edge_ancilla_overlap(a, b, n_plus_x, 1.0, n_minus_x, 0.0, c)
            total_edge_overlap += ovlp
            print(f"    (a,b)=({a},{b}): overlap = {ovlp:.12f}")

    print(f"    Total edge overlap: {total_edge_overlap:.12f}")

    # But: the overlap ALONG THE PATH (between consecutive points) is nonzero
    # because consecutive points have similar p values
    print("\n  Why adiabatic transport WORKS despite orthogonal endpoints:")
    print("  Along a continuous path, p changes continuously:")
    print("  p(t) = (1 + n_x(t))/2 varies smoothly from 1 to 0.")
    print("  For consecutive path points: sqrt(p(t_i) * p(t_{i+1})) > 0")
    print("  So the step overlaps are nonzero and the Berry phase is well-defined.")
    print("  The direct endpoint overlap being 0 just means the ancilla has")
    print("  'flipped' completely — this is geometric, not topological.")

    return {
        'reason': 'ancilla_basis_orthogonality',
        'detail': 'sqrt(p1*p2)=0 and sqrt((1-p1)(1-p2))=0 for p1=1,p2=0',
        'is_topological_obstruction': False,
    }

# ==============================================================================
# 14. CONSISTENCY CHECK: NORM INVARIANCE
# ==============================================================================

def check_norm_along_path(path_fn, path_name):
    """Verify that the purification state norm is constant along the path."""
    t_check = np.linspace(0, 1, 21)
    norms = np.zeros(21)
    for i, t in enumerate(t_check):
        n0, n1 = path_fn(t)
        norms[i] = purification_state_norm_sq(n0, n1)

    norm_mean = np.mean(norms)
    norm_std = np.std(norms)
    norm_rel_std = norm_std / norm_mean if norm_mean > 1e-15 else 0

    return {
        'norm_mean': float(norm_mean),
        'norm_std': float(norm_std),
        'norm_rel_std': float(norm_rel_std),
        'is_constant': norm_rel_std < 1e-6,
    }

def verify_consistency():
    """Verify the computational framework is consistent."""
    print("=" * 70)
    print("CONSISTENCY CHECKS")
    print("=" * 70)

    # 1. Check norm constancy along each path
    print("\n  1. Norm constancy along exchange paths:")
    paths = {
        'eq_antipodal': path_equatorial_antipodal,
        'mer_antipodal': path_meridional_antipodal,
        'tilted': path_tilted_non_antipodal,
    }
    for name, fn in paths.items():
        result = check_norm_along_path(fn, name)
        status = "OK" if result['is_constant'] else "WARNING"
        print(f"    {name}: mean={result['norm_mean']:.8f}, "
              f"std={result['norm_std']:.2e}, "
              f"rel_std={result['norm_rel_std']:.2e} [{status}]")

    # 2. Check ghost valley QCMI
    print("\n  2. QCMI at ghost valleys:")
    for valley in ['++', '+-', '-+', '--']:
        n0, n1 = ghost_axes(valley)
        qcmi = QCMI_gram(n0, n1)
        p0 = p_eff(n0)
        p1 = p_eff(n1)
        print(f"    {valley}: QCMI={qcmi:.12f}, p0={p0:.6f}, p1={p1:.6f}, "
              f"n0_x={n0[0]:.1f}, n1_x={n1[0]:.1f}")

    # 3. Check that mid-path has nonzero QCMI
    print("\n  3. QCMI at path midpoints (should be > 0):")
    for name, fn in paths.items():
        n0, n1 = fn(0.5)
        qcmi = QCMI_gram(n0, n1)
        print(f"    {name} t=0.5: n0=({n0[0]:.3f},{n0[1]:.3f},{n0[2]:.3f}), "
              f"n1=({n1[0]:.3f},{n1[1]:.3f},{n1[2]:.3f}), QCMI={qcmi:.8f}")

    # 4. Gram factor vs direct norm ratio (should be constant)
    print("\n  4. Gram factor vs direct norm ratio:")
    test_ts = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
    for name, fn in paths.items():
        ratios = []
        for t in test_ts:
            n0, n1 = fn(t)
            qcmi = QCMI_gram(n0, n1)
            gf_norm_sq = exp(-qcmi)
            direct_norm = purification_state_norm_sq(n0, n1)
            if gf_norm_sq > 1e-300:
                ratios.append(direct_norm / gf_norm_sq)

        if ratios:
            r_mean = np.mean(ratios)
            r_std = np.std(ratios)
            status = "OK" if r_std < 1e-6 * r_mean else "WARNING"
            print(f"    {name}: ratio mean={r_mean:.8f}, std={r_std:.2e} [{status}]")

    print()

# ==============================================================================
# 15. Z2 OBSTRUCTION ANALYSIS
# ==============================================================================

def analyze_z2_obstruction(valley_overlap, berry_results, qcmi_results,
                            antipodal_result, single_axis_results):
    """Synthesize all results to determine if Z2 acts nontrivially."""
    print("=" * 70)
    print("Z2 OBSTRUCTION ANALYSIS")
    print("=" * 70)

    # Evidence item 1: Direct valley overlap
    pm_mp_overlap = None
    for pair in valley_overlap['connected_pairs']:
        if (pair[0] == '+-' and pair[1] == '-+') or (pair[0] == '-+' and pair[1] == '+-'):
            pm_mp_overlap = pair[2]
    if pm_mp_overlap is None:
        pm_mp_overlap = 0.0  # orthogonal

    overlap_zero = pm_mp_overlap < 1e-10

    # Evidence item 2: Berry phase consensus
    berry_vals = [r['berry_phase'] for r in berry_results.values()]
    berry_mean = np.mean(berry_vals)
    berry_std = np.std(berry_vals)
    berry_is_pi = abs(abs(berry_mean) - pi) < 0.1
    berry_is_zero = abs(berry_mean) < 0.1

    # Evidence item 3: QCMI barrier
    qcmi_barriers = [r['qcmi_max'] for r in qcmi_results.values()]
    min_barrier = min(qcmi_barriers)
    max_barrier = max(qcmi_barriers)

    # Evidence item 4: Antipodal transport Berry phase
    ant_berry = antipodal_result['berry_phase']

    print(f"""
  EVIDENCE SUMMARY:

  1. DIRECT OVERLAP |<psi(+-)|psi(-+)>|:
     Value: {pm_mp_overlap:.8f}
     Orthogonal? {'YES' if overlap_zero else 'NO'}
     Interpretation: {'Ancilla-space orthogonality (p=1 vs p=0 → |0>_A vs |1>_A)' if overlap_zero else 'States connected in purification bundle'}

  2. BERRY PHASE along exchange paths:
     Values across paths: {[f'{v:.6f}' for v in berry_vals]}
     Mean: {berry_mean:.8f} = {berry_mean/pi:.6f} * pi
     Std:  {berry_std:.2e}
     Path-independent? {'YES' if berry_std < 0.05 else 'NO'}
     Is pi? {'YES (topological Z2)' if berry_is_pi else 'NO'}
     Is 0?  {'YES (trivial)' if berry_is_zero else 'NO'}

  3. QCMI BARRIER (minimum QCMI along exchange):
     Min across paths: {min_barrier:.8f}
     Max across paths: {max_barrier:.8f}
     Interpretation: Exchange requires passing through QCMI>0 region.
     The barrier height depends on Cartan angles (c_j).

  4. SINGLE-AXIS TRANSPORT:
     Antipodal (+-)->(--): Berry={ant_berry:.6f} = {ant_berry/pi:.6f}*pi
     All single-axis Berry phases:
""")
    for name, r in single_axis_results.items():
        print(f"     {name}: Berry={r['berry_phase']:.6f} = {r['berry_phase_over_pi']:.6f}*pi, "
              f"QCMI_max={r['qcmi_max']:.6f}")

    # FINAL VERDICT
    print(f"""
  ======================================================================
  FINAL VERDICT: IS THERE A Z2 TOPOLOGICAL OBSTRUCTION?
  ======================================================================

  The Z2 generator of pi_1(Conf_2(S2)) = B_2(S2) = Z2 corresponds to
  exchanging the two axes: (a,b) -> (b,a).

  For ghost valleys: (+x,-x) -> (-x,+x) is such an exchange.

  KEY FINDINGS:
""")

    if berry_is_pi and berry_std < 0.05:
        print("  *** Z2 ACTS NON-TRIVIALLY: Berry phase = pi ***")
        print("  The purification state acquires a pi phase upon valley exchange.")
        print("  The bundle has Z2 holonomy: transporting around the nontrivial")
        print("  loop in Conf_2(S2) gives a -1 sign on the state.")
        z2_action = 'NON-TRIVIAL (Berry = pi, Z2 holonomy)'
        topological = True
    elif berry_is_zero and berry_std < 0.05:
        print("  Z2 acts TRIVIALLY: Berry phase = 0")
        print("  Despite the orthogonal endpoints, the geometric phase accumulated")
        print("  along the exchange path is 0 (mod 2pi).")
        print("  The purification bundle is TRIVIAL — no Z2 obstruction.")
        z2_action = 'TRIVIAL (Berry = 0, no holonomy)'
        topological = False
    else:
        print(f"  Berry phase = {berry_mean:.6f} (neither 0 nor pi)")
        print(f"  Path-dependent (std = {berry_std:.2e})")
        print("  Berry phase is GEOMETRIC (depends on path), not topological.")
        print("  This means Z2 does NOT produce a topological obstruction — the")
        print("  phase depends on the specific path taken, indicating the bundle")
        print("  has curvature but no Z2 holonomy.")
        z2_action = f'GEOMETRIC (Berry={berry_mean/pi:.4f}*pi, path-dependent)'
        topological = False

    print(f"""
  Physics interpretation:
  - The orthogonal direct overlap is due to ancilla basis change, not topology
  - The Berry phase measures geometric rotation during adiabatic transport
  - QCMI > 0 along the entire exchange path (QCMI barrier exists)
  - The barrier height ({min_barrier:.6f} to {max_barrier:.6f}) quantifies
    the "cost" of inter-valley tunneling in the QCMI landscape
""")

    return {
        'z2_action': z2_action,
        'is_topological_obstruction': topological,
        'direct_overlap_zero': overlap_zero,
        'berry_mean': float(berry_mean),
        'berry_std': float(berry_std),
        'berry_is_pi': bool(berry_is_pi),
        'berry_is_zero': bool(berry_is_zero),
        'qcmi_barrier_min': float(min_barrier),
        'qcmi_barrier_max': float(max_barrier),
    }

# ==============================================================================
# 16. MAIN
# ==============================================================================

def main():
    print("=" * 70)
    print("MONODROMY BETWEEN DIFFERENT GHOST VALLEYS: (+-) <-> (-+)")
    print("pi_1(Conf_2(S2)) = B_2(S2) = Z_2")
    print("=" * 70)
    print(f"\nParameters:")
    print(f"  Cartan angles c_j: {C_ANGLES}")
    print(f"  Reference vector r: {R_VEC}")
    print(f"  Path discretization: {N_PATH} points")
    print(f"  Ghost valleys: ++, +-, -+, --")

    t_start = time.time()

    # 0. Valley overlap matrix
    valley_overlap = compute_valley_overlap_matrix()

    # 1. QCMI along all exchange paths
    qcmi_results = compute_qcmi_along_exchange_paths()

    # 2. Berry phases for all paths
    berry_results = compute_all_berry_phases()

    # 3. Antipodal transport
    antipodal_result = compute_antipodal_transport()

    # 4. All single-axis transports
    single_axis_results = compute_all_single_axis_transports()

    # 5. Analytical analysis
    ancilla_analysis = analyze_ancilla_orthogonality()

    # 6. Consistency checks
    verify_consistency()

    # 7. Z2 obstruction analysis
    z2_analysis = analyze_z2_obstruction(
        valley_overlap, berry_results, qcmi_results,
        antipodal_result, single_axis_results)

    # Final physics conclusions
    print("=" * 70)
    print("PHYSICS CONCLUSIONS")
    print("=" * 70)

    berry_vals = [r['berry_phase'] for r in berry_results.values()]
    berry_mean = np.mean(berry_vals)

    print(f"""
  1. GHOST VALLEY CONNECTIVITY:
     - |<++|+->| = 0 (E1 differs: +x vs -x, ancilla orthogonal)
     - |<++|-+>| = 0 (E0 differs: +x vs -x, ancilla orthogonal)
     - |<+-|-+>| = 0 (BOTH differ: ancilla orthogonal for both edges)
     - All four valleys are MUTUALLY ORTHOGONAL in the purification space
     - Reason: p_eff in {{0,1}} forces ancilla into |0>_A or |1>_A,
       which are orthogonal (different ancilla basis states)

  2. ADIABATIC CONNECTION:
     - Despite orthogonal endpoints, the valleys ARE continuously connected
       through the QCMI>0 region (intermediate p values)
     - The exchange path stays in Conf_2(S2) (axes never coincide)
     - Berry phase: {berry_mean:.6f} = {berry_mean/pi:.4f} * pi
     - {'Z2 acts NON-TRIVIALLY (Berry = pi)' if z2_analysis['berry_is_pi'] else 'Z2 acts TRIVIALLY (Berry != pi)' if z2_analysis['berry_is_zero'] else 'Berry phase is geometric (path-dependent)'}

  3. QCMI BARRIER:
     - Minimum QCMI along exchange: {z2_analysis['qcmi_barrier_min']:.6f}
     - Maximum QCMI along exchange: {z2_analysis['qcmi_barrier_max']:.6f}
     - QCMI > 0 throughout interior (axes distinct -> p_eff != 0,1 -> F_j < 1)

  4. TOPOLOGICAL SIGNIFICANCE:
     - pi_1(Conf_2(S2)) = B_2(S2) = Z2
     - The Z2 generator corresponds to exchanging the two axes
     - For ghost valleys, this is the (+-) <-> (-+) exchange
     - Berry phase classification: {z2_analysis['z2_action']}

  5. COMPARISON WITH PREVIOUS (WRONG) TEST:
     - Previous test (braid_monodromy.py): closed loop (++)->(++)
       Found Berry ~ 0. This was EXPECTED: any contractible loop
       in ordered space has trivial holonomy.
     - THIS test: open path (+-)->(-+) between DIFFERENT valleys.
       The path is NOT a loop — it connects distinct points in
       ordered configuration space.
     - Key difference: the ancilla basis flips during the exchange,
       which is captured by the Berry phase.

  6. PHYSICAL INTERPRETATION:
     - The ghost valleys are degenerate ground states (QCMI=0) of
       the QCMI landscape
     - They are separated by QCMI barriers (analogous to energy barriers
       in a potential landscape)
     - The Z2 monodromy determines whether wrapping around in axis
       space changes the state's sign
     - This is analogous to anyonic braiding statistics:
       exchanging two anyons can give phase exp(i*theta)
""")

    t_end = time.time()
    print(f"  Total computation time: {t_end - t_start:.1f}s")

    # Assemble results
    results = {
        'parameters': {
            'cartan_angles': [float(c) for c in C_ANGLES],
            'r_vector': [float(x) for x in R_VEC],
            'n_path': int(N_PATH),
            'ghost_valleys': ['++', '+-', '-+', '--'],
            'test_valleys': ['+-', '-+'],
            'description': 'Monodromy between DIFFERENT ghost valleys (+-)<->(-+) — the CORRECT Z2 test',
        },
        'valley_overlap_matrix': valley_overlap,
        'qcmi_along_exchange_paths': qcmi_results,
        'berry_phases': berry_results,
        'antipodal_transport': antipodal_result,
        'single_axis_transports': single_axis_results,
        'ancilla_analysis': ancilla_analysis,
        'z2_obstruction_analysis': z2_analysis,
        'conclusions': {
            'valleys_mutually_orthogonal': True,
            'reason_for_orthogonality': 'ancilla basis: p=1->|0>_A, p=0->|1>_A',
            'adiabatically_connected': True,
            'qcmi_barrier_exists': True,
            'z2_topological_obstruction': z2_analysis['is_topological_obstruction'],
            'berry_phase_mean': float(berry_mean),
            'berry_phase_mean_over_pi': float(berry_mean / pi),
            'z2_verdict': z2_analysis['z2_action'],
            'comparison_with_previous': 'Previous test (closed loop ++->++) was trivial by construction. '
                                        'This test (+-)->(-+) is the CORRECT Z2 monodromy test.',
        }
    }

    return results


if __name__ == '__main__':
    results = main()

    # Custom JSON encoder for numpy types
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, (np.bool_,)):
                return bool(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, complex):
                return [obj.real, obj.imag]
            return super().default(obj)

    # Save to JSON
    json_path = 'D:/Claude/ai-reservations/LP42-GhostZero/current/braid_valleys.json'
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"\nResults saved to: {json_path}")
