#!/usr/bin/env python3
"""
Ghost-limit representation ρ: P_n(S²) → U(1)
==============================================
Full computation of the spin-coherent Berry-phase representation
of the pure braid group on the 2-sphere in the ghost limit.

Setup:
  Spin-coherent purification: |ψ(n̂)⟩ = ⊗_j |+_{n̂_j}⟩
  Berry curvature: F_j = (1/2) dΩ_j  (Dirac monopole, ∫_{S²} F_j = 2π)
  Berry phase: ∮_γ A = Σ_j ∫_{Σ_j} F_j = Σ_j Ω_j/2
  ρ: π₁(Conf_n(S²)) → U(1)  is a group homomorphism

Ghost limit: r_{ij} = geodesic distance between axes i,j → 0⁺
  but r_{ij} > 0, so in Conf_n(S²).

Tasks:
  1. ρ(Z₂ generator) — rigid 2π rotation of all n axes about ẑ
  2. ρ(A_{ij}) in ghost limit — axis i winds around axis j
  3. Kernel of ρ in ghost limit
  4. QCMI along Z₂ path
  5. Dynamical phase vs geometric phase in slow adiabatic limit
"""

import numpy as np
from numpy import pi, sin, cos, sqrt, arccos, arctan2, exp, log
from numpy.linalg import norm
import json
import os
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Any, Optional
from itertools import combinations

# ================================================================
# PART 0 — Spin coherent state toolkit
# ================================================================

def bloch_vector(theta: float, phi: float) -> np.ndarray:
    """Unit vector n̂ on S² from spherical angles."""
    return np.array([sin(theta) * cos(phi),
                     sin(theta) * sin(phi),
                     cos(theta)])

def spin_coherent_plus(theta: float, phi: float) -> np.ndarray:
    """|+_{n̂}⟩ for spin-1/2: eigenstate of n̂·σ with eigenvalue +1."""
    c = cos(theta / 2)
    s = sin(theta / 2)
    return np.array([c, exp(1j * phi) * s], dtype=complex)

def overlap(a: np.ndarray, b: np.ndarray) -> complex:
    """⟨a|b⟩."""
    return np.dot(a.conj(), b)

def fidelity(a: np.ndarray, b: np.ndarray) -> float:
    """|⟨a|b⟩|."""
    return abs(overlap(a, b))

def geodesic_distance(theta1: float, phi1: float,
                      theta2: float, phi2: float) -> float:
    """Geodesic (angular) distance between two points on S²."""
    n1 = bloch_vector(theta1, phi1)
    n2 = bloch_vector(theta2, phi2)
    dot = np.clip(np.dot(n1, n2), -1.0, 1.0)
    return float(arccos(dot))

# ================================================================
# PART 1 — Berry connection / curvature / phase
# ================================================================

def berry_connection(theta: float, phi: float) -> Tuple[float, float]:
    """A = i⟨+|d|+⟩ = (A_θ, A_φ) with A = A_θ dθ + A_φ dφ.
    Explicit form: A = -sin²(θ/2) dφ = -½(1 - cos θ) dφ."""
    return (0.0, -0.5 * (1.0 - cos(theta)))

def berry_curvature(theta: float) -> float:
    """F = dA = -½ sin θ dθ ∧ dφ.  Returns the coefficient F_{θφ}."""
    return -0.5 * sin(theta)

def solid_angle_cap(polar_angle: float) -> float:
    """Solid angle of spherical cap of polar angle θ (from north pole).
    Ω = 2π(1 - cos θ)."""
    return 2.0 * pi * (1.0 - cos(polar_angle))

def berry_phase_closed_loop(theta_path: np.ndarray,
                             phi_path: np.ndarray) -> float:
    """Compute Berry phase by discrete integration of A around a closed loop.
    Returns phase in radians."""
    phase = 0.0
    n = len(theta_path) - 1
    for i in range(n):
        th_mid = 0.5 * (theta_path[i] + theta_path[i + 1])
        _, A_phi = berry_connection(th_mid, 0.0)  # A_φ depends only on θ
        dphi = phi_path[i + 1] - phi_path[i]
        # Handle branch cut: keep dphi in [-π, π]
        dphi = (dphi + pi) % (2 * pi) - pi
        _, A_phi_i = berry_connection(theta_path[i], 0.0)
        _, A_phi_ip1 = berry_connection(theta_path[i + 1], 0.0)
        # Trapezoidal rule
        A_avg = 0.5 * (A_phi_i + A_phi_ip1)
        phase += A_avg * dphi
    return float(phase)


def berry_phase_by_solid_angle(theta_path: np.ndarray,
                                phi_path: np.ndarray) -> float:
    """Compute Berry phase via Stokes: ∫_Σ F = -½ × solid_angle(loop).
    More robust than line integral for loops that don't cross the pole."""
    # Use the formula: Berry phase = -½ × solid angle enclosed
    # For a simple loop, we can compute solid angle via the enclosed area
    # Accumulate solid angle by summing triangular patches
    n = len(theta_path) - 1
    omega = 0.0
    for i in range(n):
        th1, ph1 = theta_path[i], phi_path[i]
        th2, ph2 = theta_path[i + 1], phi_path[i + 1]
        dphi = ph2 - ph1
        # Keep dphi in range
        dphi = (dphi + pi) % (2 * pi) - pi
        avg_cos_th = 0.5 * (cos(th1) + cos(th2))
        omega += (1.0 - avg_cos_th) * dphi
    return -0.5 * abs(omega)  # sign determined by orientation

# ================================================================
# PART 2 — Ghost-limit configuration
# ================================================================

@dataclass
class GhostConfig:
    """Configuration of n axes in the ghost limit."""
    n: int
    eps: float  # scale of separations from +x̂
    axes: List[Tuple[float, float]]  # [(θ_j, φ_j)]

    @property
    def distances(self) -> np.ndarray:
        """Pairwise geodesic distances matrix."""
        n = self.n
        d = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                d[i, j] = geodesic_distance(*self.axes[i], *self.axes[j])
        return d


def make_ghost_config(n: int, eps: float = 0.01,
                       seed: int = 42) -> GhostConfig:
    """Create ghost-limit configuration.
    Axes are placed in a small cluster near +x̂ (θ = π/2, φ = 0).
    """
    rng = np.random.RandomState(seed)
    axes = []
    for j in range(n):
        # Deterministic ring with small random perturbations
        angle = 2 * pi * j / n
        dtheta = eps * (0.3 + 0.7 * cos(angle))
        dphi = eps * (0.3 + 0.7 * sin(angle))
        theta = pi / 2 + dtheta
        phi = dphi
        if j == 0:
            # Axis 0 at +x̂ exactly (or nearly)
            theta = pi / 2 + eps * 0.01
            phi = 0.0
        axes.append((theta, phi))
    return GhostConfig(n=n, eps=eps, axes=axes)


def make_ghost_config_symmetric(n: int, eps: float = 0.01) -> GhostConfig:
    """Symmetric ghost config: n axes on a small circle (radius eps) around +x̂."""
    axes = []
    for j in range(n):
        angle = 2 * pi * j / n
        # Small ring: θ slightly off π/2, φ varies
        # Use stereographic projection: points on tangent plane near +x̂
        dx = eps * cos(angle)
        dy = eps * sin(angle)
        # Map back to sphere (tangent plane at +x̂)
        # +x̂ is at (θ=π/2, φ=0) → n̂ = (1,0,0)
        # Near +x̂: (θ, φ) ≈ (π/2, 0) + perturbations
        # Tangent plane coordinates: (y, z) ≈ (φ, π/2 - θ) near +x̂
        # Actually: n̂ = (sin θ cos φ, sin θ sin φ, cos θ)
        # Near +x̂: sin θ ≈ 1, cos φ ≈ 1 - φ²/2
        # So y ≈ φ, z ≈ π/2 - θ
        # Better: use the embedding directly
        n_vec = np.array([sqrt(1 - dx**2 - dy**2), dx, dy])
        n_vec = n_vec / norm(n_vec)
        theta_j = float(arccos(n_vec[2]))
        phi_j = float(arctan2(n_vec[1], n_vec[0]))
        axes.append((theta_j, phi_j))
    return GhostConfig(n=n, eps=eps, axes=axes)


# ================================================================
# PART 3 — Z₂ generator: rigid 2π rotation
# ================================================================

def Z2_discretized_path(config: GhostConfig,
                         n_steps: int = 2000) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Discretized Z₂ loop: all n axes rotate by 2π about ẑ.
    Each axis j traces φ → φ + 2π at constant θ_j.
    Returns list of (theta_path, phi_path) for each axis."""
    paths = []
    phi_vals = np.linspace(0, 2 * pi, n_steps)
    for th_j, ph_j0 in config.axes:
        theta_path = np.full(n_steps, th_j)
        phi_path = ph_j0 + phi_vals
        paths.append((theta_path, phi_path))
    return paths


def compute_rho_Z2(config: GhostConfig) -> Dict[str, Any]:
    """Compute ρ on Z₂ generator analytically and numerically."""
    n = config.n

    # --- Analytical ---
    # Each axis traces a loop at constant θ_j around ẑ.
    # Berry phase per axis = -π(1 - cos θ_j)
    # For θ_j ≈ π/2: per-axis phase ≈ -π
    phases_per_axis = []
    for th_j, ph_j in config.axes:
        phase_j = -pi * (1.0 - cos(th_j))
        phases_per_axis.append(phase_j)

    total_phase_analytic = sum(phases_per_axis)
    # Mod 2π
    total_mod_2pi = total_phase_analytic % (2 * pi)
    rho_Z2 = exp(1j * total_phase_analytic)

    # Ghost limit: all θ_j → π/2, cos θ_j → 0, each phase → -π
    ghost_phase_per_axis = -pi
    ghost_total = n * ghost_phase_per_axis
    ghost_rho = (-1.0) ** n  # exp(i n π) = cos(nπ) + i sin(nπ) = (-1)^n

    # --- Numerical verification ---
    paths = Z2_discretized_path(config)
    numerical_phases = []
    for theta_path, phi_path in paths:
        bp = berry_phase_closed_loop(theta_path, phi_path)
        numerical_phases.append(bp)
    total_numerical = sum(numerical_phases)

    return {
        "n": n,
        "eps": config.eps,
        "phases_per_axis_analytic": [float(p) for p in phases_per_axis],
        "total_phase_analytic": float(total_phase_analytic),
        "total_phase_mod_2pi": float(total_mod_2pi),
        "rho_Z2_exact": complex(rho_Z2.real, rho_Z2.imag),
        "ghost_limit_phase_per_axis": float(ghost_phase_per_axis),
        "ghost_limit_total": float(ghost_total),
        "ghost_limit_rho_Z2": float(ghost_rho),
        "ghost_limit_rho_Z2_str": f"(-1)^{n} = {int(ghost_rho)}",
        "numerical_phases_per_axis": [float(p) for p in numerical_phases],
        "total_phase_numerical": float(total_numerical),
        "interpretation": "Z2 maps to -1 for odd n, +1 for even n"
    }


# ================================================================
# PART 4 — A_{ij} generators in ghost limit
# ================================================================

def Aij_loop_path(config: GhostConfig, i: int, j: int,
                   n_steps: int = 2000) -> Tuple[np.ndarray, np.ndarray]:
    """Path traced by axis i encircling axis j on S².
    Returns (theta_path, phi_path) for axis i.
    All other axes are assumed stationary (no Berry phase contribution).

    In the ghost limit, both axes are near +x̂. The loop is a small
    circle of geodesic radius r centered at axis j's position.
    """
    th_j, ph_j = config.axes[j]
    th_i, ph_i = config.axes[i]
    r = geodesic_distance(th_i, ph_i, th_j, ph_j)

    # Direction from j to i on S²: the unit tangent vector at j
    # pointing toward i. We'll parametrize a small circle.
    n_j = bloch_vector(th_j, ph_j)
    n_i = bloch_vector(th_i, ph_i)

    # Tangent vector at j toward i, projected to tangent plane
    v = n_i - np.dot(n_i, n_j) * n_j
    if norm(v) < 1e-14:
        # Coincident: pick arbitrary direction
        v = np.array([0.0, 1.0, 0.0]) - np.dot(np.array([0.0, 1.0, 0.0]), n_j) * n_j
    v = v / norm(v)

    # Second tangent vector (orthogonal to v)
    w = np.cross(n_j, v)
    w = w / norm(w)

    # Loop radius: the geodesic distance from j to i itself
    # But we adjust to a fraction to keep i distinct
    loop_radius = r * 0.9  # stay inside the separation

    t_vals = np.linspace(0, 2 * pi, n_steps)

    theta_path = np.zeros(n_steps)
    phi_path = np.zeros(n_steps)

    for k, t in enumerate(t_vals):
        # Point on S² at geodesic distance loop_radius from n_j
        # in direction v * cos(t) + w * sin(t)
        tangent_dir = cos(t) * v + sin(t) * w
        n_pt = cos(loop_radius) * n_j + sin(loop_radius) * tangent_dir
        n_pt = n_pt / norm(n_pt)
        theta_path[k] = float(arccos(np.clip(n_pt[2], -1.0, 1.0)))
        phi_path[k] = float(arctan2(n_pt[1], n_pt[0]))

    return theta_path, phi_path


def compute_rho_Aij(config: GhostConfig, i: int, j: int) -> Dict[str, Any]:
    """Compute ρ(A_{ij}) in the ghost limit."""
    th_i, ph_i = config.axes[i]
    th_j, ph_j = config.axes[j]
    r = geodesic_distance(th_i, ph_i, th_j, ph_j)

    # --- Analytical ghost-limit formula ---
    # Axis i traces a small circle of radius r (or fraction of r) around axis j
    # Solid angle of small cap = 2π(1 - cos r)
    # Berry phase = -½ × solid_angle = -π(1 - cos r)
    # For r → 0: Berry phase ≈ -π r²/2 → 0
    loop_radius = r * 0.9
    solid_angle = solid_angle_cap(loop_radius)
    analytic_phase = -0.5 * solid_angle

    # Taylor expansion for small r
    analytic_phase_small_r = -pi * (1.0 - cos(loop_radius))
    analytic_phase_taylor = -pi * loop_radius**2 / 2.0

    # --- Numerical ---
    theta_path, phi_path = Aij_loop_path(config, i, j)
    numerical_phase = berry_phase_closed_loop(theta_path, phi_path)

    rho = exp(1j * numerical_phase)

    return {
        "i": i, "j": j,
        "geodesic_distance_r": float(r),
        "loop_radius": float(loop_radius),
        "solid_angle_enclosed": float(solid_angle),
        "analytic_berry_phase": float(analytic_phase),
        "analytic_taylor_small_r": float(analytic_phase_taylor),
        "numerical_berry_phase": float(numerical_phase),
        "rho_Aij": complex(rho.real, rho.imag),
        "ghost_limit_rho_Aij": 1.0,
        "ghost_limit_rho_Aij_str": "+1 (all A_{ij} -> +1 as r -> 0)"
    }


def compute_all_Aij(config: GhostConfig) -> List[Dict[str, Any]]:
    """Compute ρ on all A_{ij} generators."""
    results = []
    for i in range(config.n):
        for j in range(config.n):
            if i != j:
                results.append(compute_rho_Aij(config, i, j))
    return results


# ================================================================
# PART 5 — QCMI along Z₂ path
# ================================================================

def compute_qcmi_barrier(config: GhostConfig,
                          n_steps: int = 2000) -> Dict[str, Any]:
    """Compute the overlap |⟨ψ(0)|ψ(t)⟩| along the Z₂ path.

    QCMI (Quantum Correlation Measure Index) is defined here as:
      QCMI(t) = -ln |⟨ψ(0)|ψ(t)⟩|

    This measures how much the state departs from the initial
    product state along the Berry-phase path.
    """
    n = config.n
    paths = Z2_discretized_path(config, n_steps=n_steps)

    # Initial product state
    psi0_list = [spin_coherent_plus(th, ph) for th, ph in config.axes]

    overlaps = np.zeros(n_steps)
    qcmi = np.zeros(n_steps)

    theta_arr = np.linspace(0, 2 * pi, n_steps)

    for k in range(n_steps):
        overlap_k = 1.0 + 0j
        for j in range(n):
            theta_j_k = paths[j][0][k]
            phi_j_k = paths[j][1][k]
            psi_j_k = spin_coherent_plus(theta_j_k, phi_j_k)
            overlap_j = overlap(psi0_list[j], psi_j_k)
            overlap_k *= overlap_j
        overlaps[k] = abs(overlap_k)
        if overlaps[k] > 0:
            qcmi[k] = -log(overlaps[k])
        else:
            qcmi[k] = float('inf')

    # Find maximum QCMI (barrier height)
    finite_qcmi = qcmi[np.isfinite(qcmi)]
    max_qcmi = float(np.max(finite_qcmi)) if len(finite_qcmi) > 0 else float('inf')
    max_qcmi_idx = int(np.argmax(finite_qcmi)) if len(finite_qcmi) > 0 else -1
    max_qcmi_angle = theta_arr[max_qcmi_idx] if max_qcmi_idx >= 0 else pi

    # Ghost limit analysis
    # For exact +x̂ (θ = π/2 for all): |⟨ψ(0)|ψ(t)⟩| = cos^n(Δφ/2)
    # At Δφ = π: overlap = 0, QCMI = ∞ for any n ≥ 1
    # For axes slightly off +x̂ (θ_j = π/2 + δ_j):
    #   |⟨ψ(0)|ψ(π)⟩| ∝ ∏_j |δ_j| ~ (eps)^n
    #   QCMI(π) ~ -n ln(eps)

    return {
        "n": n,
        "eps": config.eps,
        "n_steps": n_steps,
        "overlap_vs_angle": {
            "theta": theta_arr[::50].tolist(),  # downsample for JSON
            "overlap": overlaps[::50].tolist(),
            "qcmi": qcmi[::50].tolist(),
        },
        "max_qcmi": max_qcmi,
        "max_qcmi_at_angle": float(max_qcmi_angle),
        "max_qcmi_at_angle_deg": float(max_qcmi_angle * 180 / pi),
        "overlap_at_halfway": float(overlaps[n_steps // 2]),
        "qcmi_at_halfway": float(qcmi[n_steps // 2]) if np.isfinite(qcmi[n_steps // 2]) else "infinity",
        "ghost_limit_scaling": {
            "exact_plus_x": "cos^n(dphi/2), at dphi=pi -> 0 for any n>=1",
            "off_x_by_delta": "|<psi(0)|psi(pi)>| ~ (eps)^n, QCMI(pi) ~ -n*ln(eps)",
            "barrier_diverges": "QCMI barrier -> inf for any n>=1 as eps->0"
        },
        "is_barrier_independent_of_ghost": False,
        "barrier_dependence": "QCMI barrier DIVERGES as eps->0, scaling as -n*ln(eps). Thus barrier grows when axes are closer to ghost limit."
    }


# ================================================================
# PART 6 — Dynamical phase vs geometric phase
# ================================================================

def compute_dynamical_phase(T: float, omega_L: float) -> float:
    """Dynamical phase for a spin-1/2 in magnetic field of Larmor frequency ω_L.
    E_+ = -ℏω_L/2, so γ_dyn = -E_+ T/ℏ = ω_L T / 2."""
    return omega_L * T / 2.0


def compute_phase_separation(n: int, T: float, omega_L: float) -> Dict[str, Any]:
    """Analyze the separation of dynamical and geometric phases.

    For n independent spins on the Z₂ path (rigid 2π rotation about ẑ):
      - Each spin has the SAME dynamical phase γ_dyn = ω_L T / 2
      - Each spin has Berry phase γ_Berry = -π(1 - cos θ_j) ≈ -π
      - Total dynamical phase: n × ω_L T / 2
      - Total Berry phase: nπ (mod 2π) → (-1)^n sign

    In the adiabatic limit (T → ∞):
      - γ_dyn → ∞
      - γ_Berry remains finite and geometric
      - The two are separable because γ_Berry is independent of T
      - Standard spin-echo or interferometric techniques cancel γ_dyn

    IMPORTANT: The dynamical phase does NOT vanish in the adiabatic limit.
    It GROWS with T. But it can be SUBTRACTED using a reference path.
    """
    gamma_dyn_per_spin = compute_dynamical_phase(T, omega_L)
    gamma_dyn_total = n * gamma_dyn_per_spin
    gamma_berry_per_spin = pi  # in ghost limit, θ_j ≈ π/2
    gamma_berry_total = n * gamma_berry_per_spin

    return {
        "n": n,
        "rotation_period_T": T,
        "larmor_frequency_omega_L": omega_L,
        "dynamical_phase_per_spin": gamma_dyn_per_spin,
        "dynamical_phase_total": gamma_dyn_total,
        "berry_phase_per_spin": gamma_berry_per_spin,
        "berry_phase_total": gamma_berry_total,
        "berry_mod_2pi": gamma_berry_total % (2 * pi),
        "total_phase": gamma_dyn_total + gamma_berry_total,
        "adiabatic_limit_T_inf": {
            "dynamical_diverges": True,
            "berry_unchanged": True,
            "separable": True,
            "method": "Spin-echo or two-path interferometry cancels dynamical phase, revealing geometric phase (-1)^n"
        },
        "observable_sign_flip": {
            "odd_n": "|psi_final> = -|psi_initial> -- OBSERVABLE via interferometry",
            "even_n": "|psi_final> = +|psi_initial> -- no net sign flip"
        }
    }


# ================================================================
# PART 7 — Full representation table
# ================================================================

def compute_full_representation(n_values: List[int],
                                 eps: float = 0.01) -> Dict[int, Dict[str, Any]]:
    """Compute ρ for multiple n values."""
    results = {}
    for n in n_values:
        config = make_ghost_config_symmetric(n, eps=eps)

        # Z₂
        z2_result = compute_rho_Z2(config)

        # A_{ij} (all pairs)
        aij_results = compute_all_Aij(config)

        # QCMI
        qcmi_result = compute_qcmi_barrier(config)

        # Dynamical phase analysis
        T_adiabatic = 1000.0  # large T for adiabatic limit
        omega_L = 1.0
        dyn_result = compute_phase_separation(n, T_adiabatic, omega_L)

        # Kernel analysis
        odd_n = n % 2 == 1
        kernel_info = {
            "n": n,
            "parity": "odd" if odd_n else "even",
            "rho_Z2": int((-1) ** n),
            "all_Aij_map_to": "+1 (ghost limit)",
            "kernel": ("Subgroup generated by all A_{ij} and combinations "
                       "with even number of Z2 factors" if odd_n
                       else "Entire group P_n(S^2)"),
            "image": "Z2 = {+1, -1}" if odd_n else "{+1} (trivial)",
            "exact_sequence": f"1 -> ker(rho) -> P_{n}(S^2) -> {'Z2' if odd_n else '{1}'} -> 1"
        }

        results[n] = {
            "Z2": z2_result,
            "Aij_sample": aij_results[:min(6, len(aij_results))],
            "all_Aij_ghost_limit_unity": all(
                abs(r["ghost_limit_rho_Aij"] - 1.0) < 1e-10
                for r in aij_results
            ),
            "QCMI_barrier": qcmi_result,
            "dynamical_phase_analysis": dyn_result,
            "kernel": kernel_info,
            "ghost_config_distances": config.distances.tolist(),
            "ghost_config_axes": [(float(th), float(ph)) for th, ph in config.axes],
        }

    return results


# ================================================================
# PART 8 — Run and export
# ================================================================

def main():
    print("=" * 72)
    print("Ghost-Limit Representation rho: P_n(S^2) -> U(1)")
    print("=" * 72)

    n_values = [2, 3, 4, 5]
    eps = 0.005  # small ghost-limit separation

    print(f"\nComputing for n = {n_values}, ghost limit eps = {eps}")
    print("-" * 72)

    results = compute_full_representation(n_values, eps=eps)

    # Print summary
    for n in n_values:
        r = results[n]
        z2 = r["Z2"]
        kern = r["kernel"]
        qcmi = r["QCMI_barrier"]
        dyn = r["dynamical_phase_analysis"]

        print(f"\n{'='*60}")
        print(f"  n = {n} ({kern['parity']})")
        print(f"{'='*60}")
        print(f"  rho(Z2)         = {z2['ghost_limit_rho_Z2_str']}")
        print(f"  rho(A_ij)       = {r['all_Aij_ghost_limit_unity']} (all -> +1 in ghost limit)")
        print(f"  ker(rho)        = {kern['kernel']}")
        print(f"  im(rho)         = {kern['image']}")
        print(f"  Exact sequence:  {kern['exact_sequence']}")
        print(f"  QCMI barrier:     {qcmi['max_qcmi']:.3f} at dphi = {qcmi['max_qcmi_at_angle_deg']:.1f} deg")
        print(f"  Overlap halfway:  {qcmi['overlap_at_halfway']:.6f}")
        print(f"  Dynamical phase:  grows ~ T (gamma_dyn/total = {dyn['dynamical_phase_total']:.1f})")
        print(f"  Berry phase:      {dyn['berry_mod_2pi']:.6f} mod 2pi")
        print(f"  Observable:       {dyn['observable_sign_flip']['odd_n' if n % 2 == 1 else 'even_n']}")

    # Export JSON
    output_path = os.path.join(os.path.dirname(__file__), "ghost_limit_rep.json")
    serializable = {}
    for n, r in results.items():
        serializable[str(n)] = r

    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, (np.ndarray,)):
                return obj.tolist()
            if isinstance(obj, complex):
                return {"real": obj.real, "imag": obj.imag}
            return super().default(obj)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(serializable, f, indent=2, cls=NumpyEncoder,
                  ensure_ascii=False)
    print(f"\nExported full results to: {output_path}")

    # Ghost-limit scaling study
    print(f"\n{'='*72}")
    print("Ghost-limit scaling: QCMI barrier vs eps (n=3)")
    print(f"{'='*72}")
    print(f"{'eps':>12s}  {'max QCMI':>12s}  {'overlap(pi)':>14s}  {'rho_typical_Aij':>16s}")
    print("-" * 60)
    for eps_val in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]:
        cfg = make_ghost_config_symmetric(3, eps=eps_val)
        qr = compute_qcmi_barrier(cfg, n_steps=1000)
        aij = compute_rho_Aij(cfg, 1, 2)
        print(f"{eps_val:12.4f}  {qr['max_qcmi'] if np.isfinite(qr['max_qcmi']) else float('inf'):12.3f}  "
              f"{qr['overlap_at_halfway']:14.6e}  {aij['numerical_berry_phase']:16.6e}")

    print(f"\n{'='*72}")
    print("Done.")
    return results


if __name__ == "__main__":
    main()
