"""
HF1 Minimal Prototype: Can we detect DGF's beta1 enhancement?
Pure numpy/scipy, no persistent homology library needed.
~100 lines, runs in < 2 minutes, gives ONE NUMBER.
"""
import numpy as np
from scipy import ndimage
import time

t0 = time.time()
np.random.seed(42)
N, L = 200, 10.0  # 200x200 pixels, 10 degree patch (~0.05 deg/pixel → 1 deg = 20 pixels)

# --- 1. Generate CMB-like Gaussian field ---
kx = np.fft.fftfreq(N, d=L/N) * 2*np.pi
ky = np.fft.fftfreq(N, d=L/N) * 2*np.pi
K = np.sqrt(kx[:,None]**2 + ky[None,:]**2)
beam = np.exp(-K**2 * (np.deg2rad(0.425))**2 / 2)
power = np.where(K > 1e-6, K**(-2.0) * beam**2, 0)
power[K < 1e-6] = power[K > 1e-6].min()

def make_field():
    nf = (np.random.randn(N,N) + 1j*np.random.randn(N,N)) * np.sqrt(power) / np.sqrt(2)
    f = np.fft.ifft2(nf * N).real
    return f / np.std(f)

def add_dgf_rings(field, delta=0.01, n_rings=500):
    """Inject beta1 enhancement: localized ring structures."""
    f = field.copy()
    rx = np.random.randint(20, N-20, n_rings)
    ry = np.random.randint(20, N-20, n_rings)
    for cx, cy in zip(rx, ry):
        x = np.arange(N) - cx
        y = np.arange(N)[:,None] - cy
        rr = np.sqrt(x**2 + y**2)
        amp = 0.01 * delta
        ring = amp * (2 - rr/1.5) * np.exp(-(rr-1.5)**2/0.3)
        ring[np.abs(rr-1.5) > 2] = 0
        f += ring
    return f / np.std(f)

# --- 2. Compute Betti numbers at multiple thresholds ---
def compute_betti(field, n_nu=41):
    """Compute beta0, Euler chi, beta1 = beta0 - chi at each threshold.
    Uses: scipy.ndimage.label for beta0, local 2x2 pattern for chi."""
    nu_vals = np.linspace(-3, 3, n_nu)
    beta0 = np.zeros(n_nu)
    chi = np.zeros(n_nu)
    for i, nu in enumerate(nu_vals):
        binary = (field > nu).astype(np.int32)
        # beta0 = number of connected components
        _, n_comp = ndimage.label(binary, structure=np.ones((3,3)))
        beta0[i] = n_comp
        # Euler characteristic via local 2x2 patterns
        p00 = binary[:-1, :-1]
        p10 = binary[1:, :-1]
        p01 = binary[:-1, 1:]
        p11 = binary[1:, 1:]
        s = p00 + p10 + p01 + p11
        # chi = V - E + F
        n_v = np.sum(s >= 1)  # any pixel = vertex
        n_e = np.sum((p00+p10 >= 1) & (p00+p01 >= 1)) + np.sum((p00+p10 >= 1) & (p10+p11 >= 1))
        # Simpler: use genus formula for 2D thresholded image
        # chi = (# of 2x2 blocks with s=4) - (# corner patterns) ...
        # Fast: chi = V - E_edge + F, and V ~ count of patterns, E ~ edges between
        # Simplest: use total curvature = V - E + F directly from 2x2
        v = 0; e = 0; f = 0
        for sx in [-1, 0]:
            for sy in [-1, 0]:
                if sx == -1 or sy == -1:
                    continue
                # Count this 2x2 block
                # Vertices: 4 corners
                v += 4
                # Edges: 4 perimeter + 2 internal = 6
                e += 6
                # Face: the 2x2 square
                f += 1
        # Actually this overcounts. Use the standard Gauss-Bonnet for digital images:
        # chi = sum over 2x2 blocks of (1 if 1 or 3 pixels set, -1 if 2 diagonal, 0 else)
        chi_block = np.zeros((N-1, N-1))
        chi_block[(s==1) | (s==3)] = 1
        chi_block[(s==2) & (p00==p11) & (p01==p10) & (p00!=p01)] = -2  # 2 diagonal
        chi[i] = chi_block.sum()
    beta1 = beta0 - chi
    return nu_vals, beta0, beta1, chi

# --- 3. Run comparison ---
print("=" * 55)
print("HF1 PROTOTYPE: beta1 detection test")
print(f"  {N}x{N} pixels, {L} deg patch")
print("=" * 55)

# Single realization first
fg = make_field()
fd = add_dgf_rings(fg, delta=0.01)
nu, b0g, b1g, chig = compute_betti(fg)
nu, b0d, b1d, chid = compute_betti(fd)

mask = np.abs(nu) < 1.5
# beta1 peaks near nu=0 for Gaussian fields
b1g_peak = b1g[mask].max()
b1d_peak = b1d[mask].max()
b1_change_single = (b1d_peak - b1g_peak) / b1g_peak * 100

print(f"\n  Single realization:")
print(f"    Gaussian beta1 peak: {b1g_peak:.0f}")
print(f"    DGF beta1 peak:      {b1d_peak:.0f}")
print(f"    Change: {b1_change_single:+.2f}%")

# --- 4. Ensemble to measure SNR ---
n_ens = 200
print(f"\n  Running {n_ens} realizations...")
b1_g_ens = np.zeros((n_ens, 41))
b1_d_ens = np.zeros((n_ens, 41))
for i in range(n_ens):
    fg = make_field()
    fd = add_dgf_rings(fg, delta=0.01, n_rings=300)
    _, _, b1g_i, _ = compute_betti(fg)
    _, _, b1d_i, _ = compute_betti(fd)
    b1_g_ens[i] = b1g_i
    b1_d_ens[i] = b1d_i

b1_diff_ens = b1_d_ens - b1_g_ens  # (200, 41)
mean_diff = b1_diff_ens[:, mask].mean(axis=1)  # per-realization mean diff near nu=0
mean_diff_all = mean_diff.mean()
std_diff_all = mean_diff.std()
snr = abs(mean_diff_all) / std_diff_all if std_diff_all > 0 else 0
n_for_3 = int((3*std_diff_all/abs(mean_diff_all))**2) if mean_diff_all != 0 else float('inf')

# Per-threshold SNR
mean_per_nu = b1_diff_ens.mean(axis=0)
std_per_nu = b1_diff_ens.std(axis=0)
snr_per_nu = abs(mean_per_nu) / (std_per_nu + 1e-10)
best_nu_idx = np.argmax(snr_per_nu[mask])
best_nu = nu[mask][best_nu_idx]
best_snr = snr_per_nu[mask][best_nu_idx]

elapsed = time.time() - t0
print(f"\n{'='*55}")
print(f"RESULT (after {elapsed:.0f}s):")
print(f"="*55)
print(f"  DGF beta1 injection: 1.0%")
print(f"  Mean beta1 change: {mean_diff_all/b1g_peak*100:+.3f}% (abs)")
print(f"  Detection SNR: {snr:.2f}")
print(f"  Best SNR at nu={best_nu:.1f}: {best_snr:.2f}")
print(f"  Realizations needed for 3sigma: {n_for_3}")
print(f"")
if snr > 3:
    print(f"  VERDICT: DETECTABLE — 1% signal is above noise with {n_ens} realizations")
elif snr > 1:
    print(f"  VERDICT: MARGINAL — need ~{n_for_3} realizations for 3sigma")
else:
    print(f"  VERDICT: UNDER THRESHOLD — SNR<1 with {n_ens} realizations, need ~{n_for_3}")
print(f"="*55)
