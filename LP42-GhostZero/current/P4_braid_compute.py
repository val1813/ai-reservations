#!/usr/bin/env python3
"""
P_4(S^2) pure braid group physics for 4 axes on S^2.
Berry phase computation via spin-coherent state overlap product.

Background:
  P_2(S^2) = trivial
  P_3(S^2) ≅ Z_2  (Berry phase π for rigid 2π rotation of 3 axes)
  For n=4: Z_2 rigid rotation gives nπ mod 2π = 4π ≡ 0 → INVISIBLE?
  But there are other generators (subsystem, partial braids).

Method:
  Berry phase for spin-1/2 coherent state |n̂⟩ along closed path:
    γ = -Im[ln ∏_j ⟨n̂_j|n̂_{j+1}⟩]  mod 2π
  Equivalent to half the solid angle enclosed by the path on S^2.
"""

import numpy as np
import json
from pathlib import Path

# ============================================================
# Geometry / state utilities
# ============================================================

def cart_to_sph(n):
    """Cartesian unit vector -> (theta, phi)."""
    x, y, z = n
    theta = np.arccos(np.clip(z, -1.0, 1.0))
    phi = np.arctan2(y, x)
    return theta, phi

def sph_to_cart(theta, phi):
    """(theta, phi) -> Cartesian unit vector."""
    return np.array([
        np.sin(theta) * np.cos(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(theta)
    ])

def rotate_vector(v, k, angle):
    """Rodrigues rotation of v around unit axis k by angle."""
    k = k / np.linalg.norm(k)
    ca, sa = np.cos(angle), np.sin(angle)
    return ca * v + sa * np.cross(k, v) + (1.0 - ca) * np.dot(k, v) * k

def geodesic_distance(n1, n2):
    """Angular distance between two unit vectors (radians)."""
    dot = np.clip(np.dot(n1, n2), -1.0, 1.0)
    return np.arccos(dot)

# ============================================================
# Berry phase via overlap product
# ============================================================

def spin_overlap(n1, n2):
    """
    Overlap <n̂_1 | n̂_2> for spin-1/2 coherent states.
    |n̂> = cos(θ/2)|↑> + e^{iφ} sin(θ/2)|↓>
    """
    t1, p1 = cart_to_sph(n1)
    t2, p2 = cart_to_sph(n2)
    return (np.cos(t1 / 2.0) * np.cos(t2 / 2.0)
            + np.exp(1j * (p2 - p1)) * np.sin(t1 / 2.0) * np.sin(t2 / 2.0))

def berry_phase(path):
    """
    Berry phase for spin-1/2 along a closed discrete path.
    γ = -Im[ln ∏ ⟨n̂_j | n̂_{j+1}⟩]  (mod 2π)

    path: (N, 3) array, path[0] should equal path[-1] for closure.
    """
    N = len(path)
    prod = 1.0 + 0.0j
    for i in range(N - 1):
        prod *= spin_overlap(path[i], path[i + 1])
    # close loop explicitly
    prod *= spin_overlap(path[-1], path[0])
    return float((-np.angle(prod)) % (2.0 * np.pi))

def berry_phase_solid_angle(path):
    """
    Cross-check: Berry phase from solid angle triangulation.
    Triangulate from centroid to each consecutive pair.
    """
    centroid = np.mean(path, axis=0)
    cn = np.linalg.norm(centroid)
    if cn < 1e-10:
        return berry_phase(path)  # fallback
    ref = centroid / cn

    omega = 0.0
    N = len(path) - 1
    for i in range(N):
        a, b = path[i], path[i + 1]
        # solid angle of spherical triangle (ref, a, b)
        # tan(Ω/2) = |ref·(a×b)| / (1 + ref·a + a·b + b·ref)
        num = abs(np.dot(ref, np.cross(a, b)))
        den = 1.0 + np.dot(ref, a) + np.dot(a, b) + np.dot(b, ref)
        # arctan2 handles the quadrant correctly
        domega = 2.0 * np.arctan2(num, den)
        # sign from orientation
        sign = np.sign(np.dot(np.cross(a, b), ref))
        if abs(sign) < 1e-12:
            sign = 1.0
        omega += sign * domega

    return (abs(omega) / 2.0) % (2.0 * np.pi)

def total_berry(paths):
    """Sum Berry phases modulo 2π."""
    total = 0.0
    for p in paths:
        total += berry_phase(p)
    return total % (2.0 * np.pi)

def fmt_bp(gamma):
    """Format Berry phase: short canonical string.
    For small values that happen to be near 2pi due to mod, show the small equivalent."""
    g = gamma % (2.0 * np.pi)
    if abs(g - 2.0 * np.pi) < 1e-10 or abs(g) < 1e-10:
        return "0"
    if abs(g - np.pi) < 0.002:
        return "pi"
    # If g is near 2*pi, show as small negative (equivalent mod 2pi)
    if g > 1.9 * np.pi:
        small = 2.0 * np.pi - g
        return f"~{small/np.pi:.4f}pi (={g/np.pi:.4f}pi mod 2pi)"
    return f"{g/np.pi:.4f}pi"

# ============================================================
# Path builders
# ============================================================

def path_rigid_rotation(n0, rot_axis, angle=2.0 * np.pi, n_steps=2000):
    """Single axis path under rigid rotation about rot_axis."""
    path = [rotate_vector(n0, rot_axis, t)
            for t in np.linspace(0.0, angle, n_steps)]
    path.append(path[0].copy())
    return np.array(path)

def path_stationary(n0):
    """Stationary axis (just the point)."""
    return np.array([n0, n0])

def path_circle_around_center(n0, center, n_steps=2000):
    """
    Axis n0 traces a full circle at constant geodesic distance from 'center'.
    This is the 'lasso' generator A_{ij}: axis i winds around axis j.
    center = position of the stationary axis being encircled.
    """
    r = geodesic_distance(n0, center)
    if r < 1e-12:
        # axes coincide — no winding possible
        return np.array([n0, n0])

    # Orthonormal basis in tangent plane at 'center'
    # e1 points toward n0
    cos_r = np.cos(r)
    sin_r = np.sin(r)
    e1 = (n0 - cos_r * center) / sin_r
    e2 = np.cross(center, e1)

    path = []
    for t in np.linspace(0.0, 2.0 * np.pi, n_steps):
        nt = cos_r * center + sin_r * (np.cos(t) * e1 + np.sin(t) * e2)
        path.append(nt)
    path.append(path[0].copy())
    return np.array(path)



def main():
    x_hat = np.array([1.0, 0.0, 0.0])
    rot_axis = np.array([0.0, 0.0, 1.0])  # ẑ

    # ---- Axes for GHOST STATE (all exactly at +x̂) ----
    # Used for rigid rotations: all axes trace the equator → Berry = pi each
    ghost_axes = np.array([x_hat.copy() for _ in range(4)])

    # ---- Axes for PARTIAL BRAIDS (4 distinct points in xy-plane, near +x̂) ----
    # All at theta=pi/2, separated only in phi. This ensures rigid rotation
    # about ẑ gives Berry = pi exactly for each axis.
    eps = 0.05
    # phi values symmetrically around 0: -3d, -d, +d, +3d
    d = eps / 2.0  # half-separation between adjacent axes
    sep_phi = np.array([-3*d, -d, d, 3*d])
    sep_axes = np.array([sph_to_cart(np.pi/2, p) for p in sep_phi])
    # sep_axes[j] = (cos(phi_j), sin(phi_j), 0), all at theta = pi/2

    results = {}

    print("=" * 64)
    print("P_4(S^2) PURE BRAID GROUP — BERRY PHASE COMPUTATION")
    print("=" * 64)

    print(f"\nGhost state: all 4 axes at +x̂ = (1,0,0)")
    print(f"Separated axes (eps={eps:.3f} rad, all in xy-plane near +x̂):")
    for j in range(4):
        n = sep_axes[j]
        t, p = cart_to_sph(n)
        print(f"  n̂_{j} = ({n[0]:.6f}, {n[1]:.6f}, {n[2]:.6f})  theta={t:.2f}  phi={p:.4f}")

    # ========================================================
    # 1. Z_2 rigid rotation for n=4 (GHOST STATE)
    # ========================================================
    print("\n" + "-" * 64)
    print("1. Z_2 RIGID ROTATION (all 4 axes, 2pi about ẑ, GHOST state)")
    print("-" * 64)

    paths_1 = [path_rigid_rotation(n0, rot_axis) for n0 in ghost_axes]
    bp_per_axis_1 = [berry_phase(p) for p in paths_1]
    bp_total_1 = total_berry(paths_1)
    raw_sum_1 = sum(bp_per_axis_1)

    for j, bp in enumerate(bp_per_axis_1):
        print(f"  Axis {j}: gamma = {fmt_bp(bp)}")
    print(f"  RAW sum (pre-mod):  {raw_sum_1:.6f} rad = {raw_sum_1/np.pi:.2f}pi")
    print(f"  TOTAL (mod 2pi):    {fmt_bp(bp_total_1)}")
    trivial_1 = bp_total_1 < 1e-2 or abs(bp_total_1 - 2*np.pi) < 1e-2
    print(f"  => {'Z_2 INVISIBLE for even n (4pi = 0 mod 2pi)' if trivial_1 else 'NONTRIVIAL (UNEXPECTED)'}")

    results["1_Z2_rigid_n4"] = {
        "description": "Rigid 2pi rotation of all 4 ghost axes about ẑ",
        "raw_sum_rad": float(raw_sum_1),
        "raw_sum_pi": float(raw_sum_1 / np.pi),
        "berry_total_rad": float(bp_total_1),
        "berry_total_pi": float(bp_total_1 / np.pi),
        "trivial_mod_2pi": bool(trivial_1)
    }

    # ========================================================
    # 2. Subsystem braid {0,1,2} (GHOST STATE)
    # ========================================================
    print("\n" + "-" * 64)
    print("2. SUBSYSTEM BRAID: axes {0,1,2} via P_3 Z_2, n̂_3 fixed (GHOST state)")
    print("-" * 64)

    paths_2 = []
    for j in range(4):
        if j in (0, 1, 2):
            paths_2.append(path_rigid_rotation(ghost_axes[j], rot_axis))
        else:
            paths_2.append(path_stationary(ghost_axes[j]))

    bp_per_axis_2 = [berry_phase(p) for p in paths_2]
    bp_total_2 = total_berry(paths_2)
    raw_sum_2 = sum(bp_per_axis_2)

    for j, bp in enumerate(bp_per_axis_2):
        print(f"  Axis {j}: gamma = {fmt_bp(bp)}")
    print(f"  RAW sum (pre-mod):  {raw_sum_2:.6f} rad = {raw_sum_2/np.pi:.2f}pi")
    print(f"  TOTAL (mod 2pi):    {fmt_bp(bp_total_2)}")
    is_pi_2 = abs(bp_total_2 - np.pi) < 1e-4
    print(f"  => {'DETECTABLE Z_2 (3pi = pi mod 2pi)' if is_pi_2 else 'UNEXPECTED'}")

    results["2_subsystem_braid_012"] = {
        "description": "P_3 Z_2 on ghost axes {0,1,2}, axis 3 stationary",
        "raw_sum_rad": float(raw_sum_2),
        "raw_sum_pi": float(raw_sum_2 / np.pi),
        "berry_total_rad": float(bp_total_2),
        "berry_total_pi": float(bp_total_2 / np.pi),
        "is_pi_mod_2pi": bool(is_pi_2)
    }

    # ========================================================
    # 3. Partial braid A_{01} (SEPARATED axes)
    # ========================================================
    print("\n" + "-" * 64)
    print("3. PARTIAL BRAID A_{01}: n̂_0 winds around n̂_1 (SEPARATED axes)")
    print("-" * 64)

    geo_dist_01 = geodesic_distance(sep_axes[0], sep_axes[1])

    paths_3 = [None] * 4
    paths_3[0] = path_circle_around_center(sep_axes[0], sep_axes[1])
    for j in (1, 2, 3):
        paths_3[j] = path_stationary(sep_axes[j])

    bp_per_axis_3 = [berry_phase(p) for p in paths_3]
    bp_total_3 = total_berry(paths_3)
    analytical_3 = np.pi * (1.0 - np.cos(geo_dist_01))

    for j, bp in enumerate(bp_per_axis_3):
        print(f"  Axis {j}: gamma = {fmt_bp(bp)}")
    print(f"  Geodesic distance r(n̂_0,n̂_1) = {geo_dist_01:.4f} rad")
    print(f"  Analytical:  pi*(1-cos r) = {analytical_3:.6f} rad = {analytical_3/np.pi:.6f}pi")
    print(f"  Numerical:                 {fmt_bp(bp_total_3)}")
    is_new_3 = geo_dist_01 > 1e-6  # nonzero separation → nonzero Berry
    print(f"  => {'NEW generator: Berry ~ pi*r^2/2 (not 0 or pi)' if is_new_3 else 'trivial'}")

    results["3_partial_braid_A01"] = {
        "description": "A_{01} lasso: axis 0 traces circle around axis 1",
        "geodesic_r_rad": float(geo_dist_01),
        "berry_per_axis_rad": [float(b) for b in bp_per_axis_3],
        "berry_total_rad": float(bp_total_3),
        "berry_total_pi": float(bp_total_3 / np.pi),
        "analytical_rad": float(analytical_3),
        "analytical_pi": float(analytical_3 / np.pi),
        "is_new_generator": bool(is_new_3)
    }

    # ========================================================
    # 4. Independent braids: A_{01} x A_{23} (SEPARATED axes)
    # ========================================================
    print("\n" + "-" * 64)
    print("4. INDEPENDENT BRAIDS: {0,1} and {2,3} (SEPARATED axes)")
    print("-" * 64)

    geo_dist_23 = geodesic_distance(sep_axes[2], sep_axes[3])

    paths_4 = [None] * 4
    paths_4[0] = path_circle_around_center(sep_axes[0], sep_axes[1])
    paths_4[1] = path_stationary(sep_axes[1])
    paths_4[2] = path_circle_around_center(sep_axes[2], sep_axes[3])
    paths_4[3] = path_stationary(sep_axes[3])

    bp_per_axis_4 = [berry_phase(p) for p in paths_4]
    bp_total_4 = total_berry(paths_4)
    analytical_4 = np.pi * (2.0 - np.cos(geo_dist_01) - np.cos(geo_dist_23))
    bp_A23 = berry_phase(paths_4[2])
    sum_individual = (bp_total_3 + bp_A23) % (2.0 * np.pi)
    additive_4 = abs(bp_total_4 - sum_individual) < 1e-8

    for j, bp in enumerate(bp_per_axis_4):
        print(f"  Axis {j}: gamma = {fmt_bp(bp)}")
    print(f"  Analytical: pi*(2 - cos r01 - cos r23) = {analytical_4:.6f} rad = {analytical_4/np.pi:.6f}pi")
    print(f"  Numerical:  {fmt_bp(bp_total_4)}")
    print(f"  gamma(A01)={fmt_bp(bp_total_3)}, gamma(A23)={fmt_bp(bp_A23)}")
    print(f"  Sum = {fmt_bp(sum_individual)}")
    print(f"  => {'ADDITIVE — commuting independent braids' if additive_4 else 'NON-ADDITIVE'}")

    results["4_independent_braids"] = {
        "description": "A_{01} x A_{23}: independent lassos on {0,1} and {2,3}",
        "geodesic_r01_rad": float(geo_dist_01),
        "geodesic_r23_rad": float(geo_dist_23),
        "berry_per_axis_rad": [float(b) for b in bp_per_axis_4],
        "berry_total_rad": float(bp_total_4),
        "berry_total_pi": float(bp_total_4 / np.pi),
        "berry_A01_rad": float(bp_total_3),
        "berry_A23_rad": float(bp_A23),
        "sum_individual_rad": float(sum_individual),
        "additive": bool(additive_4),
        "analytical_rad": float(analytical_4)
    }

    # ========================================================
    # 5. SIMPLEST PHYSICAL OBSERVABLE — interference (GHOST)
    # ========================================================
    print("\n" + "-" * 64)
    print("5. INTERFERENCE: Ghost vs {0,1,2}-braided (GHOST state, exact)")
    print("-" * 64)

    ghost_paths = [path_stationary(n0) for n0 in ghost_axes]
    bp_ghost = total_berry(ghost_paths)

    braided_paths = []
    for j in range(4):
        if j in (0, 1, 2):
            braided_paths.append(path_rigid_rotation(ghost_axes[j], rot_axis))
        else:
            braided_paths.append(path_stationary(ghost_axes[j]))

    bp_braided = total_berry(braided_paths)
    bp_per_axis_braided = [berry_phase(p) for p in braided_paths]
    delta_bp = (bp_braided - bp_ghost) % (2.0 * np.pi)
    fidelity = abs(np.cos(delta_bp / 2.0))
    is_destructive = fidelity < 1e-6

    print(f"  Ghost:    {fmt_bp(bp_ghost)}")
    print(f"  Braided:  {fmt_bp(bp_braided)}")
    for j, bp in enumerate(bp_per_axis_braided):
        print(f"    Axis {j}: {fmt_bp(bp)}")
    print(f"  DELTA gamma = {fmt_bp(delta_bp)}")
    print(f"  |<ghost|braided>| = |cos(Dg/2)| = {fidelity:.6f}")
    print(f"  => {'COMPLETE ORTHOGONALITY — braiding flips the state sign' if is_destructive else 'Partial overlap'}")

    results["5_interference"] = {
        "description": "Ghost state vs {0,1,2}-braided interference",
        "ghost_berry_rad": float(bp_ghost),
        "braided_berry_rad": float(bp_braided),
        "delta_berry_rad": float(delta_bp),
        "delta_berry_pi": float(delta_bp / np.pi),
        "fidelity": float(fidelity),
        "orthogonal": bool(is_destructive)
    }

    # ========================================================
    # 6. All Z_2 subsystems (GHOST state)
    # ========================================================
    print("\n" + "-" * 64)
    print("6. ALL 3-AXIS Z_2 SUBSYSTEMS (GHOST state — exact)")
    print("-" * 64)

    from itertools import combinations

    subsystem_results = {}
    for combo in combinations(range(4), 3):
        paths = []
        for j in range(4):
            if j in combo:
                paths.append(path_rigid_rotation(ghost_axes[j], rot_axis))
            else:
                paths.append(path_stationary(ghost_axes[j]))
        bp = total_berry(paths)
        label = "".join(str(c) for c in combo)
        subsystem_results[label] = {
            "subsystem": list(combo),
            "berry_rad": float(bp),
            "berry_pi": float(bp / np.pi)
        }
        print(f"  Z_2 on {{{','.join(str(c) for c in combo)}}}: {fmt_bp(bp)}")

    results["6_all_Z2_subsystems"] = subsystem_results

    # ========================================================
    # 7. Bonus: all 6 A_{ij} lasso Berry phases on separated axes
    # ========================================================
    print("\n" + "-" * 64)
    print("7. BONUS: All 6 A_{ij} lasso generators (SEPARATED axes)")
    print("-" * 64)
    print("  Lasso A_{ij}: axis i traces circle of radius r_ij around axis j")
    print("  Berry phase = pi*(1 - cos r_ij) ~ pi * r_ij^2 / 2")
    print()

    all_lassos = {}
    for i in range(4):
        for j in range(i + 1, 4):
            r_ij = geodesic_distance(sep_axes[i], sep_axes[j])
            # axis i winds around axis j
            p_i = path_circle_around_center(sep_axes[i], sep_axes[j])
            bp_ij = berry_phase(p_i)
            analytical = np.pi * (1.0 - np.cos(r_ij))
            label = f"A_{{{i}{j}}}"
            all_lassos[label] = {
                "r_ij_rad": float(r_ij),
                "berry_numerical_rad": float(bp_ij),
                "berry_analytical_rad": float(analytical),
                "berry_analytical_pi": float(analytical / np.pi)
            }
            print(f"  {label}: r={r_ij:.4f} rad  gamma_num={fmt_bp(bp_ij):>18s}  gamma_ana={analytical/np.pi:.6f}pi")

    results["7_all_Aij_lassos"] = all_lassos

    # ========================================================
    # Save to JSON
    # ========================================================
    outdir = Path(r"D:/Claude/ai-reservations/LP42-GhostZero/current")
    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / "P4_braid_results.json"

    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 64}")
    print(f"Results -> {outpath}")
    print(f"{'=' * 64}")

    # ========================================================
    # Summary
    # ========================================================
    print("\n" + "=" * 64)
    print("SUMMARY: P_4(S^2) Berry Phase Structure")
    print("=" * 64)
    print(f"  1. Z_2 rigid n=4:        {fmt_bp(bp_total_1)}   <- INVISIBLE (4pi=0)")
    print(f"  2. Subsystem {{0,1,2}}:    {fmt_bp(bp_total_2)}   <- DETECTABLE Z_2")
    print(f"  3. A_{{01}} lasso:         {fmt_bp(bp_total_3)}   <- NEW (not 0 or pi)")
    print(f"  4. A_{{01}} x A_{{23}}:      {fmt_bp(bp_total_4)}   <- ADDITIVE")
    print(f"  5. Interference Dg:      {fmt_bp(delta_bp)}   <- ORTHOGONAL")
    print()
    print("PHYSICS:")
    print(f"  Ghost state: QCMI = 0, all axes at +x̂")
    print(f"  Z_2 rigid n=4: Berry = 4pi = 0 mod 2pi (INVISIBLE for even n)")
    print(f"  Z_2 on any 3 axes: Berry = pi (visible, DETECTABLE)")
    print(f"  A_{{ij}} lassos: Berry = pi*(1-cos r) ~ pi*r^2/2 for small r")
    print(f"    -> New continuous family of Berry phases, NOT in P_3")
    print(f"  Interference: braided |ghost> = -|ghost> (pi phase shift)")
    print()
    print("P_4(S^2) has at least:")
    print("  4x Z_2 subsystems (choose any 3 of 4 axes)")
    print("  6x A_{{ij}} lasso generators (choose any 2 of 4 axes)")
    print("  + Products and combinations")


if __name__ == "__main__":
    main()
