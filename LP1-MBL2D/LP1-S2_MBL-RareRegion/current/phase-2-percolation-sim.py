#!/usr/bin/env python3
"""
Phase 2: Numerical percolation simulation for 2D MBL rare thermal regions.
Generates 2D Gaussian random fields with correlation, thresholds, and checks percolation.
"""
import numpy as np
from scipy.ndimage import label, labeled_comprehension
from scipy.stats import norm
import json, os, sys
from datetime import datetime

def generate_grf_fft(N, xi, kernel='gaussian', seed=None):
    """Generate 2D Gaussian random field with correlation xi via FFT convolution."""
    if seed is not None:
        np.random.seed(seed)
    # White noise in real space
    white = np.random.randn(N, N)
    # FFT
    white_hat = np.fft.fft2(white)
    # Frequency grid
    freqs = np.fft.fftfreq(N) * N
    kx, ky = np.meshgrid(freqs, freqs)
    k = np.sqrt(kx**2 + ky**2)
    # Correlation kernel in Fourier space
    if kernel == 'gaussian':
        # C(r) = exp(-r^2/(2*xi^2)) -> power spectrum ~ exp(-k^2*xi^2/2)
        kernel_hat = np.exp(-k**2 * xi**2 / 2)
    elif kernel == 'exponential':
        # C(r) = exp(-r/xi) -> power spectrum ~ (1 + k^2*xi^2)^(-3/2) in 2D
        kernel_hat = (1 + k**2 * xi**2) ** (-0.75)
    else:
        raise ValueError(f"Unknown kernel: {kernel}")
    kernel_hat[0, 0] = 0  # Zero mean
    # Convolve
    field_hat = white_hat * kernel_hat
    field = np.fft.ifft2(field_hat).real
    # Normalize to unit variance
    field /= np.std(field)
    return field

def threshold_field(field, u):
    """Threshold GRF to binary thermal/non-thermal map.
    Thermal sites: local disorder < W_c, i.e., field < u (lower tail)."""
    return (field < u).astype(np.int8)

def analyze_clusters(binary_map):
    """Find connected components (4-connected) and compute statistics."""
    structure = np.ones((3, 3), dtype=bool)
    labeled, n_clusters = label(binary_map, structure=structure)
    if n_clusters == 0:
        return {'n_clusters': 0, 'max_size': 0, 'mean_size': 0, 'spans': False,
                'eta': 0.0, 'cluster_sizes': []}
    # Cluster sizes
    sizes = np.bincount(labeled.ravel())[1:]  # Skip background (label 0)
    max_size = sizes.max()
    mean_size = sizes.mean()
    # System spanning: any cluster touches all 4 boundaries?
    N = binary_map.shape[0]
    spans = False
    for cluster_id in range(1, n_clusters + 1):
        mask = (labeled == cluster_id)
        rows, cols = np.where(mask)
        if rows.min() == 0 and rows.max() == N-1 and cols.min() == 0 and cols.max() == N-1:
            spans = True
            break
    # Effective radius for percolation parameter
    # Each cluster of size S -> effective radius r = sqrt(S/pi)
    r_eff = np.sqrt(max_size / np.pi)
    eta = n_clusters * np.pi * r_eff**2 / (N * N)
    return {
        'n_clusters': int(n_clusters),
        'max_size': int(max_size),
        'mean_size': float(mean_size),
        'spans': spans,
        'eta': float(eta),
        'cluster_sizes': sizes.tolist()
    }

def run_simulation(N, W, W_c, xi, kernel, N_real=200):
    """Run percolation simulation for given parameters."""
    sigma = W / np.sqrt(12)
    u = W_c / sigma
    p_th = norm.cdf(u)  # fraction of sites with ε < W_c (thermal)

    results = []
    n_spans = 0
    # Also track non-thermal (localized) cluster spanning
    n_nonthermal_spans = 0
    for i in range(N_real):
        field = generate_grf_fft(N, xi, kernel, seed=i)
        binary = threshold_field(field, u)
        stats = analyze_clusters(binary)
        stats['realization'] = i
        if stats['spans']:
            n_spans += 1

        # Non-thermal (= localized, field > u) cluster analysis
        binary_nt = 1 - binary  # invert: localized = 1
        stats_nt = analyze_clusters(binary_nt)
        if stats_nt['spans']:
            n_nonthermal_spans += 1

        results.append(stats)

    # Aggregate statistics
    max_sizes = [r['max_size'] for r in results]
    etas = [r['eta'] for r in results]
    n_clusters_list = [r['n_clusters'] for r in results]

    return {
        'parameters': {
            'N': N, 'W': W, 'W_c': W_c, 'xi': xi,
            'kernel': kernel, 'N_real': N_real,
            'u': float(u), 'p_th': float(p_th)
        },
        'spanning_probability': n_spans / N_real,
        'nonthermal_spanning_probability': n_nonthermal_spans / N_real,
        'max_size_mean': float(np.mean(max_sizes)),
        'max_size_std': float(np.std(max_sizes)),
        'eta_mean': float(np.mean(etas)),
        'eta_std': float(np.std(etas)),
        'n_clusters_mean': float(np.mean(n_clusters_list)),
        'percolates': (n_spans / N_real) > 0.5,
        'nonthermal_percolates': (n_nonthermal_spans / N_real) > 0.5,
        'timestamp': datetime.now().isoformat()
    }

if __name__ == '__main__':
    # Parameter grid
    N_values = [24, 50, 100]
    W_values = [5, 10, 15, 20, 30, 40, 50]
    xi_values = [1, 2, 3]
    kernel = 'gaussian'
    W_c = 5.0
    N_real = 200  # Realizations per parameter set

    all_results = {}
    print("=" * 70)
    print("Phase 2: 2D MBL Rare Region Percolation Simulation")
    print(f"Parameters: N={N_values}, W={W_values}, xi={xi_values}")
    print(f"Kernel: {kernel}, W_c={W_c}, N_real={N_real}")
    print("=" * 70)

    for N in N_values:
        for xi in xi_values:
            for W in W_values:
                key = f"N{N}_xi{xi}_W{W}"
                print(f"Running: {key} ...", end=' ', flush=True)
                result = run_simulation(N, W, W_c, xi, kernel, N_real)
                all_results[key] = result
                p_span = result['spanning_probability']
                verdict = "PERCOLATES" if result['percolates'] else "NO PERC"
                print(f"P_span={p_span:.3f} eta={result['eta_mean']:.4f} {verdict}")

    # Save results
    output_path = os.path.join(os.path.dirname(__file__), 'phase-2-results.json')
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Summary table
    print("\n" + "=" * 70)
    print("SUMMARY: Percolation Phase Diagram")
    print("=" * 70)
    print(f"{'N':>4} {'xi':>4} {'W':>5} {'P_span':>8} {'eta_mean':>10} {'<S_max>':>8} {'Verdict':>12}")
    print("-" * 60)
    for N in N_values:
        for xi in xi_values:
            for W in W_values:
                key = f"N{N}_xi{xi}_W{W}"
                r = all_results[key]
                verdict = "PERCOLATES" if r['percolates'] else "NO PERC"
                print(f"{N:4} {xi:4} {W:5} {r['spanning_probability']:8.3f} "
                      f"{r['eta_mean']:10.4f} {r['max_size_mean']:8.1f} {verdict:>12}")
