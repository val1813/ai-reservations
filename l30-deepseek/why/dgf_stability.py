#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Numerical stability analysis of the DGF (Discrete Gradient Flow) evolution equation.

Exact discrete flux form:
    J_{i->i+1} = (q_{i+1} - q_i) / (q_i * q_{i+1})
    Dq_i = +Dt * (J_{i->i+1} - J_{i-1->i})

We investigate:
1. Stability condition for Dt
2. Adaptive timestepping scheme
3. Homogenization timescale tau_A = L^2 q^2 / (l_p c)
"""

import sys
import io
# Force UTF-8 output to avoid GBK encoding issues on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

OUTDIR = r'D:\Claude\ai-reservations\l30-deepseek\why'
# IMPORTANT: matplotlib on Windows needs a font that supports unicode
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------------
# 1. EXACT FLUX FORM IMPLEMENTATION
# ------------------------------------------------------------------

def compute_flux(q, i):
    """J_{i->i+1} = (q_{i+1} - q_i) / (q_i * q_{i+1})"""
    if q[i] <= 0 or q[i+1] <= 0:
        return 0.0  # handle degenerate case
    return (q[i+1] - q[i]) / (q[i] * q[i+1])


def compute_all_fluxes(q):
    """Compute fluxes across all edges in 1D lattice."""
    n = len(q)
    J = np.zeros(n - 1)
    for i in range(n - 1):
        J[i] = compute_flux(q, i)
    return J


def dq_dt(q):
    """Compute dq_i/dt for all cells (no Dt factor)."""
    n = len(q)
    dq = np.zeros(n)
    for i in range(n):
        J_right = compute_flux(q, i) if i < n - 1 else 0.0
        J_left = compute_flux(q, i - 1) if i > 0 else 0.0
        dq[i] = J_right - J_left
    return dq


def euler_step(q, dt):
    """Single Euler step with fixed dt."""
    dq = dq_dt(q)
    return q + dt * dq


# ------------------------------------------------------------------
# 2. STABILITY ANALYSIS
# ------------------------------------------------------------------

def analyze_reviewer_case():
    """Reproduce the reviewer's 3-cell example."""
    print("=" * 60)
    print("REVIEWER'S 3-CELL TEST")
    print("=" * 60)
    q = np.array([0.1, 0.9, 0.1])
    print("Initial q =", q)

    J = compute_all_fluxes(q)
    print("Fluxes: J01=%s, J12=%s" % (J[0], J[1]))

    dq = dq_dt(q)
    print("dq/dt =", dq)
    print("dq2 (dt=1) = %s" % dq[1])

    q1 = euler_step(q, 1.0)
    print("After 1 step (dt=1): q =", q1)
    print("  q0: %.4f -> %.4f" % (q[0], q1[0]))
    print("  q1: %.4f -> %.4f  <-- BLOWS UP" % (q[1], q1[1]))
    print("  q2: %.4f -> %.4f" % (q[2], q1[2]))
    print("  Sum q: %.6f -> %.6f" % (q.sum(), q1.sum()))

    # What's the actual flux magnitude?
    print("\nJ01 = 1/q0 - 1/q1 = %.6f" % (1/q[0]-1/q[1]))
    print("J12 = 1/q1 - 1/q2 = %.6f" % (1/q[1]-1/q[2]))
    print("dq2 = J12 - J01 = %.6f" % ((1/q[1]-1/q[2]) - (1/q[0]-1/q[1])))

    return q, dq


def find_stability_bound(q, max_allowed_step=0.1):
    """
    Find maximum Dt that keeps all q_i in [epsilon, 1-epsilon].

    The flux magnitude diverges as q -> 0:
        J_{i->i+1} = 1/q_i - 1/q_{i+1}
    If q_i << 1, |J| ~ 1/q_i which is huge.

    Constraint 1: q_i(t+dt) >= epsilon
        For dq_i < 0: dt <= (q_i - epsilon) / (-dq_i)

    Constraint 2: q_i(t+dt) <= 1-epsilon
        For dq_i > 0: dt <= (1 - epsilon - q_i) / dq_i
    """
    epsilon = 1e-6
    dq = dq_dt(q)

    max_dt = np.inf

    for i in range(len(q)):
        if dq[i] < -1e-15:
            # q decreasing: must stay above epsilon
            dt_limit = (q[i] - epsilon) / (-dq[i])
            max_dt = min(max_dt, dt_limit)
        elif dq[i] > 1e-15:
            # q increasing: must stay below 1-epsilon
            dt_limit = (1.0 - epsilon - q[i]) / dq[i]
            max_dt = min(max_dt, dt_limit)

    if max_dt == np.inf:
        max_dt = 1.0

    # Also cap at max_allowed_step
    max_dt = min(max_dt, max_allowed_step)

    return max_dt


def analyze_stability_condition():
    """Analytic stability condition."""
    print("\n" + "=" * 60)
    print("STABILITY CONDITION")
    print("=" * 60)

    # The flux J = 1/q_i - 1/q_{i+1}
    # So dq_i/dt = (1/q_i - 1/q_{i+1}) - (1/q_{i-1} - 1/q_i)
    #            = 2/q_i - 1/q_{i-1} - 1/q_{i+1}
    #
    # The maximum |dq/dt| occurs at the boundary of a sharp gradient.
    # For a step: q_left = q_small, q_right = q_large:
    # |J| ~ 1/q_small (dominant term)
    #
    # To keep Dq bounded by delta, we need:
    #   Dt * |dq/dt| <= delta
    #   Dt * (2/q_min) <= delta  (worst case: one neighbor also small)
    #   Dt <= delta * q_min / 2
    #
    # More rigorously, for the 3-cell case with (q, 1-q, q) where q << 1:
    #   dq_center/dt = 2/(1-q) - 2/q ~= -2/q
    # So to keep q_center from going negative:
    #   (1-q) + Dt * (-2/q) >= 0
    #   Dt <= (1-q) * q / 2 ~= q/2 for q << 1

    q_min_vals = np.logspace(-3, -1, 20)
    dt_max_vals = []

    for q_min in q_min_vals:
        q = np.array([q_min, 1.0 - q_min, q_min])
        dq = dq_dt(q)
        dt_safe = (q[1]) / abs(dq[1])  # safe dt to avoid crossing zero
        dt_max_vals.append(dt_safe)

    analytic_bound = q_min_vals[0]**2 / 2
    print("For q_min = %.3f: Dt_max ~= %.2e" % (q_min_vals[0], analytic_bound))
    print("  Analytic bound:  Dt <= q_min^2 / 2  (for symmetric 3-cell)")
    print("  General bound:   Dt <= q_min * dq_max / 2")
    print("  Physical meaning: Flux diverges as 1/q_small, so timestep must")
    print("                    shrink quadratically with the minimum occupation.")

    return q_min_vals, dt_max_vals


# ------------------------------------------------------------------
# 3. ADAPTIVE TIMESTEPPING
# ------------------------------------------------------------------

class AdaptiveDGFSimulator:
    """DGF simulator with adaptive timestepping."""

    def __init__(self, n_cells, safety_factor=0.5, max_step=0.1, min_step=1e-12):
        self.n = n_cells
        self.safety = safety_factor
        self.max_step = max_step
        self.min_step = min_step

    def compute_dt(self, q):
        """Compute safe timestep."""
        dt = find_stability_bound(q, self.max_step)
        return max(self.min_step, self.safety * dt)

    def step(self, q):
        """Take one adaptive step."""
        dt = self.compute_dt(q)
        dq = dq_dt(q)
        q_new = q + dt * dq

        # Enforce bounds
        q_new = np.clip(q_new, 1e-12, 1.0 - 1e-12)

        # Re-normalize to conserve Sum(q)
        sum_before = q.sum()
        sum_after = q_new.sum()
        if sum_after > 1e-15:
            q_new *= sum_before / sum_after

        return q_new, dt

    def evolve(self, q0, t_max, n_steps_max=100000, callback=None):
        """Evolve from q0 for total time t_max."""
        q = q0.copy()
        t = 0.0
        history = [(t, q.copy())]
        dts = []

        for step_idx in range(n_steps_max):
            if t >= t_max:
                break

            q_new, dt = self.step(q)

            # Cap dt to not overshoot t_max
            if t + dt > t_max:
                dt = t_max - t
                dq = dq_dt(q)
                q_new = q + dt * dq
                q_new = np.clip(q_new, 1e-12, 1.0 - 1e-12)
                sum_before = q.sum()
                sum_after = q_new.sum()
                if sum_after > 1e-15:
                    q_new *= sum_before / sum_after

            q = q_new
            t += dt
            dts.append(dt)

            if callback and step_idx % callback['freq'] == 0:
                callback['fn'](t, q, dt, step_idx)

            if len(history) == 0 or t - history[-1][0] > t_max / 1000:
                history.append((t, q.copy()))

            # Convergence check
            if step_idx > 0 and step_idx % 1000 == 0:
                grad = np.max(np.abs(np.diff(q)))
                if grad < 1e-8:
                    print("  Converged at t=%.6e, step %d, grad=%.2e" % (t, step_idx, grad))
                    break

        history.append((t, q.copy()))
        return q, history, dts


# ------------------------------------------------------------------
# 4 & 5. TEST INITIAL CONDITIONS
# ------------------------------------------------------------------

def make_big_bang(n_cells, peak_height=0.99, width=3):
    """'Big Bang' perturbation: narrow peak at center."""
    q = np.ones(n_cells) * 1e-6
    center = n_cells // 2
    for i in range(n_cells):
        dist = abs(i - center)
        if dist <= width:
            q[i] = peak_height * np.exp(-0.5 * (dist / (width/3))**2)
    # Normalize so total = n_cells * 0.5 (representative of average q=0.5)
    q = q / q.sum() * (n_cells * 0.5)
    q = np.clip(q, 1e-6, 0.999)
    return q


def make_near_deadlock(n_cells):
    """Near-deadlock: alternating high/low occupancy."""
    q = np.zeros(n_cells)
    for i in range(n_cells):
        if i % 2 == 0:
            q[i] = 0.99
        else:
            q[i] = 0.01
    return q


def make_mid_density(n_cells):
    """Mid-density: smooth sinusoidal variation."""
    x = np.linspace(0, 2*np.pi, n_cells)
    q = 0.5 + 0.3 * np.sin(x)
    q = np.clip(q, 0.01, 0.99)
    return q


def make_step_function(n_cells):
    """Sharp step: left half low, right half high."""
    q = np.zeros(n_cells)
    half = n_cells // 2
    q[:half] = 0.01
    q[half:] = 0.99
    return q


def make_random(n_cells, seed=42):
    """Random initial condition."""
    np.random.seed(seed)
    q = np.random.uniform(0.1, 0.9, n_cells)
    return q


# ------------------------------------------------------------------
# 6. PLOTTING
# ------------------------------------------------------------------

def plot_evolution(history, title, n_cells, dts=None):
    """Plot q(x,t) evolution."""
    fig = plt.figure(figsize=(14, 5))
    gs = GridSpec(1, 3, width_ratios=[1.2, 0.8, 0.8])

    # Panel 1: q(x,t) evolution
    ax1 = fig.add_subplot(gs[0])

    # Select time slices to plot
    n_slices = min(10, len(history))
    indices = np.linspace(0, len(history)-1, n_slices, dtype=int)

    x = np.arange(n_cells)
    colors = plt.cm.viridis(np.linspace(0, 1, n_slices))

    for idx, (t, q) in enumerate([history[i] for i in indices]):
        tag = 't=%.3f' % t
        ax1.plot(x, q, color=colors[idx], alpha=0.7, linewidth=1.5,
                 label=tag if idx == 0 or idx == n_slices-1 else None)

    # Highlight final state
    t_final, q_final = history[-1]
    ax1.plot(x, q_final, 'r-', linewidth=2, label='Final (t=%.3f)' % t_final)

    ax1.set_xlabel('Cell index i')
    ax1.set_ylabel('q_i')
    ax1.set_title('%s\nq(x,t) evolution' % title)
    ax1.legend(fontsize=8, loc='best')
    ax1.set_ylim(-0.05, 1.05)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Conservation of Sum(q)
    ax2 = fig.add_subplot(gs[1])
    sums = [q.sum() for _, q in history]
    times = [t for t, _ in history]
    ax2.plot(times, sums, 'b-', linewidth=1)
    ax2.axhline(y=history[0][1].sum(), color='r', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Time t')
    ax2.set_ylabel('Sum(q)')
    ax2.set_title('Conservation check')
    ax2.grid(True, alpha=0.3)

    # Show relative error
    ref = history[0][1].sum()
    rel_err = abs(sums[-1] - ref) / ref if ref > 0 else 0
    ax2.text(0.95, 0.05, 'Rel err: %.2e' % rel_err, transform=ax2.transAxes,
             ha='right', fontsize=9,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Panel 3: Gradient decay
    ax3 = fig.add_subplot(gs[2])
    max_grads = [np.max(np.abs(np.diff(q))) for _, q in history]
    ax3.semilogy(times, max_grads, 'g-', linewidth=1)
    ax3.set_xlabel('Time t')
    ax3.set_ylabel('max|grad q|')
    ax3.set_title('Gradient decay')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def plot_stability_analysis(q_min, dt_max):
    """Plot stability bound."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    ax.loglog(q_min, dt_max, 'b.-', markersize=3, label='Numerical bound')
    ax.loglog(q_min, q_min**2 / 2, 'r--', linewidth=1.5, label='Dt = q^2 / 2')
    ax.loglog(q_min, q_min / 2, 'g--', linewidth=1, alpha=0.5, label='Dt = q / 2')

    ax.set_xlabel('q_min')
    ax.set_ylabel('Dt_max')
    ax.set_title('Stability Boundary: Dt_max vs q_min\n(3-cell symmetric case)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def plot_timescale_comparison():
    """Plot homogenization timescale for different q values."""
    fig, ax = plt.subplots(1, 1, figsize=(9, 5))

    l_p = 1.62e-35  # m
    c = 3.0e8       # m/s
    L = 1e26        # m (Hubble radius)

    q_vals = np.logspace(-6, np.log10(0.9999), 100)
    tau_A = L**2 * q_vals**2 / (l_p * c)

    ax.loglog(q_vals, tau_A, 'b-', linewidth=2)

    # Annotations
    for q_ref in [0.99, 0.9, 0.5, 0.1, 0.01, 0.001]:
        tau_ref = L**2 * q_ref**2 / (l_p * c)
        tau_years = tau_ref / (365.25 * 24 * 3600)
        ax.axvline(x=q_ref, color='gray', linestyle=':', alpha=0.4)
        ax.annotate('q=%.2f\ntau=%.1e yr' % (q_ref, tau_years),
                   xy=(q_ref, tau_ref), fontsize=8,
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

    ax.set_xlabel('Occupation probability q')
    ax.set_ylabel('tau_A (seconds)')
    ax.set_title('Homogenization Timescale tau_A = L^2 q^2 / (l_p c)\n'
                 'l_p=%.2e m, L=%.1e m' % (l_p, L))
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def plot_adaptive_dt(dts, title):
    """Plot adaptive timestep history."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 3))

    ax.semilogy(range(len(dts)), dts, 'b-', linewidth=0.5, alpha=0.7)
    ax.set_xlabel('Step number')
    ax.set_ylabel('Dt')
    ax.set_title('Adaptive timestep history: %s' % title)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


# ------------------------------------------------------------------
# 7. MAIN ANALYSIS
# ------------------------------------------------------------------

def main():
    print("=" * 60)
    print("DGF NUMERICAL STABILITY ANALYSIS")
    print("=" * 60)

    # --- Step 1: Reproduce reviewer's concern ---
    q0, dq0 = analyze_reviewer_case()

    # --- Step 2: Stability condition ---
    q_min_vals, dt_max_vals = analyze_stability_condition()
    fig_stab = plot_stability_analysis(q_min_vals, dt_max_vals)
    fig_stab.savefig(OUTDIR + r'\stability_bound.png', dpi=150)
    plt.close(fig_stab)
    print("Saved: stability_bound.png")

    # --- Step 3 & 4 & 5: Adaptive simulation ---
    n_cells = 51
    t_max = 10.0

    initial_conditions = {
        'Big Bang perturbation': make_big_bang(n_cells),
        'Near-deadlock': make_near_deadlock(n_cells),
        'Mid-density sinusoid': make_mid_density(n_cells),
        'Sharp step': make_step_function(n_cells),
        'Random': make_random(n_cells),
    }

    sim = AdaptiveDGFSimulator(n_cells, safety_factor=0.5, max_step=0.1)

    results = {}

    for name, q0 in initial_conditions.items():
        print("\n" + "-" * 50)
        print("Testing:", name)
        print("  q range: [%.4f, %.4f]" % (q0.min(), q0.max()))
        print("  Sum(q) = %.6f" % q0.sum())
        print("  Initial max gradient: %.6f" % np.max(np.abs(np.diff(q0))))

        q_final, history, dts = sim.evolve(q0, t_max)

        grad_initial = np.max(np.abs(np.diff(q0)))
        grad_final = np.max(np.abs(np.diff(q_final)))

        print("  Final q range: [%.6f, %.6f]" % (q_final.min(), q_final.max()))
        print("  Final Sum(q) = %.6f" % q_final.sum())
        cons_err = abs(q_final.sum() - q0.sum()) / q0.sum() if q0.sum() > 0 else 0
        print("  Conservation error: %.2e" % cons_err)
        grad_ratio = grad_initial / grad_final if grad_final > 0 else np.inf
        print("  Gradient: %.4f -> %.4e (reduction: %.1e x)" % (grad_initial, grad_final, grad_ratio))
        print("  Steps taken: %d" % len(dts))
        print("  Mean Dt: %.4e, Min Dt: %.4e, Max Dt: %.4e" % (np.mean(dts), np.min(dts), np.max(dts)))
        print("  Total time: %.4f" % history[-1][0])

        results[name] = {
            'q0': q0, 'q_final': q_final, 'history': history, 'dts': dts,
            'grad_initial': grad_initial, 'grad_final': grad_final,
            'n_steps': len(dts)
        }

        # Plot evolution
        fig_evol = plot_evolution(history, name, n_cells, dts)
        fname = 'evolution_%s.png' % name.lower().replace(' ', '_')
        fig_evol.savefig(OUTDIR + '\\' + fname, dpi=150)
        plt.close(fig_evol)
        print("  Plot saved:", fname)

        # Plot adaptive dt
        fig_dt = plot_adaptive_dt(dts, name)
        fname_dt = 'adaptive_dt_%s.png' % name.lower().replace(' ', '_')
        fig_dt.savefig(OUTDIR + '\\' + fname_dt, dpi=150)
        plt.close(fig_dt)
        print("  Plot saved:", fname_dt)

    # --- Step: Homogenization timescale ---
    print("\n" + "=" * 60)
    print("HOMOGENIZATION TIMESCALE  tau_A = L^2 q^2 / (l_p c)")
    print("=" * 60)

    l_p = 1.62e-35
    c = 3.0e8
    L = 1e26
    age_universe_yr = 13.8e9
    sec_per_year = 365.25 * 24 * 3600

    for q_val in [0.99, 0.9, 0.5, 0.1, 0.01]:
        tau_s = L**2 * q_val**2 / (l_p * c)
        tau_yr = tau_s / sec_per_year
        tau_Gyr = tau_yr / 1e9
        tau_universe = tau_yr / age_universe_yr
        print("\n  q = %.3f:" % q_val)
        print("    tau_A = %.4e seconds" % tau_s)
        print("          = %.4e years" % tau_yr)
        print("          = %.4f Gyr" % tau_Gyr)
        print("          = %.4f x age of universe" % tau_universe)

    fig_tau = plot_timescale_comparison()
    fig_tau.savefig(OUTDIR + r'\timescale.png', dpi=150)
    plt.close(fig_tau)
    print("\nSaved: timescale.png")

    # --- Bonus: Demonstrate that flux form IS diffusive ---
    print("\n" + "=" * 60)
    print("DIFFUSIVE BEHAVIOR CHECK")
    print("=" * 60)
    print("\nThe exact flux J = 1/q_i - 1/q_{i+1} can be Taylor expanded:")
    print("  For small gradients: q_{i+1} = q_i + dx * dq/dx")
    print("  J ~= -dx * (dq/dx) / q^2")
    print("  dq/dt = -dJ/dx ~= dx^2 * d/dx[(1/q^2) * dq/dx]")
    print("  This is a nonlinear diffusion equation with diffusivity D(q) = 1/q^2")
    print("  Information flows from high-q to low-q regions because D increases as q->0")
    print("  The sharp gradient at the low-q edge produces the dominant flux.")

    # Verify on a smooth gradient
    n_smooth = 201
    x = np.linspace(0, 1, n_smooth)
    q_smooth = 0.3 + 0.4 * np.exp(-((x-0.5)**2) / 0.01)
    q_smooth = np.clip(q_smooth, 0.01, 0.99)

    dq = dq_dt(q_smooth)
    J = compute_all_fluxes(q_smooth)

    print("\nSmooth Gaussian test (%d cells):" % n_smooth)
    print("  q range: [%.4f, %.4f]" % (q_smooth.min(), q_smooth.max()))
    print("  J signs at peak region:", np.sign(J[90:110]))
    print("  dq/dt at center: %.6f" % dq[100])
    print("  dq/dt at edges: dq[0]=%.6f, dq[-1]=%.6f" % (dq[0], dq[-1]))
    print("  -> Flux is positive (left->right) left of peak, negative right of peak")
    print("  -> This means: q DECREASES at peak, INCREASES at edges = DIFFUSION")

    # Show this with a figure
    fig_diff, axes = plt.subplots(2, 1, figsize=(10, 7))
    axes[0].plot(x, q_smooth, 'b-', linewidth=2)
    axes[0].set_ylabel('q')
    axes[0].set_title('Smooth Gaussian profile')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(x[:-1] + 0.5*(x[1]-x[0]), J, 'r-', linewidth=1.5, label='Flux J')
    ax1b = axes[1].twinx()
    ax1b.plot(x, dq, 'g--', linewidth=1.5, label='dq/dt')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('Flux J', color='r')
    ax1b.set_ylabel('dq/dt', color='g')
    axes[1].set_title('Flux and rate of change')
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(loc='upper left')
    ax1b.legend(loc='upper right')

    plt.tight_layout()
    fig_diff.savefig(OUTDIR + r'\diffusive_check.png', dpi=150)
    plt.close(fig_diff)
    print("Saved: diffusive_check.png")

    return results


if __name__ == '__main__':
    results = main()
    print("\n" + "=" * 60)
    print("DONE - All results saved to %s" % OUTDIR)
    print("=" * 60)
