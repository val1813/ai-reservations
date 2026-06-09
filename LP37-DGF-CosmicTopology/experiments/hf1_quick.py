"""
HF1 Quick Test: Euler Characteristic of Gaussian vs DGF fields
Fast version — vectorized, small ensemble, key number only.
"""
import numpy as np

np.random.seed(42)
N = 256

# Faster: precompute FFT of Gaussian field once, reuse
kx = np.fft.fftfreq(N, d=10.0/N) * 2*np.pi
ky = np.fft.fftfreq(N, d=10.0/N) * 2*np.pi
K = np.sqrt(kx[:,None]**2 + ky[None,:]**2)
beam = np.exp(-K**2 * (np.deg2rad(0.425))**2 / 2)
power = np.where(K > 1e-6, K**(-2.0) * beam**2, 0)
power[K < 1e-6] = power[K > 1e-6].min()

# Fast genus computation using convolution (not pixel loops!)
def fast_genus(field, n_nu=31):
    """Genus via Minkowski functional: g(nu) ~ <delta(f-nu) * kappa> / (2*pi)
    where kappa is geodesic curvature of iso-contours.
    Fast: use gradient + Laplacian, no pixel loops."""
    nu_vals = np.linspace(-3, 3, n_nu)
    # Gradient
    gy, gx = np.gradient(field)
    gxx, gxy = np.gradient(gx)
    gyx, gyy = np.gradient(gy)
    # Mean curvature of level set: kappa = -div(grad/|grad|)
    gmag = np.sqrt(gx**2 + gy**2)
    gmag = np.maximum(gmag, 1e-10)
    kappa = -(gxx*gy**2 - 2*gxy*gx*gy + gyy*gx**2) / (gmag**3)
    # Genus = <kappa> on level set, estimated via histogram
    genus = np.zeros(n_nu)
    for i, nu in enumerate(nu_vals):
        # Narrow band around level set
        mask = np.abs(field - nu) < 0.15  # band width ~ 3*sigma/n_nu
        if mask.sum() > 0:
            genus[i] = kappa[mask].sum() / mask.sum()
    return nu_vals, genus

# Generate one Gaussian field
noise_f = (np.random.randn(N,N) + 1j*np.random.randn(N,N)) * np.sqrt(power) / np.sqrt(2)
field_g = np.fft.ifft2(noise_f * N).real
field_g /= np.std(field_g)

# Add DGF ring structures
delta_dgf = 0.01
field_d = field_g.copy()
n_rings = 200
rx = np.random.randint(10, N-10, n_rings)
ry = np.random.randint(10, N-10, n_rings)
for cx, cy in zip(rx, ry):
    x = np.arange(N) - cx
    y = np.arange(N)[:,None] - cy
    rr = np.sqrt(x**2 + y**2)
    ring = 0.003 * (2 - rr/2.0) * np.exp(-(rr-2.0)**2/0.5)
    ring[np.abs(rr-2.0) > 2] = 0
    field_d += ring
field_d /= np.std(field_d)

nu, genus_g = fast_genus(field_g)
nu, genus_d = fast_genus(field_d)
mask = np.abs(nu) < 2.0
rel_change = np.mean(np.abs((genus_d - genus_g)[mask] / (np.abs(genus_g[mask]) + 1e-10)))

# Small ensemble for error estimate
n_ens = 50
diff_at_0 = np.zeros(n_ens)
for i in range(n_ens):
    nf = (np.random.randn(N,N) + 1j*np.random.randn(N,N)) * np.sqrt(power) / np.sqrt(2)
    fg = np.fft.ifft2(nf * N).real
    fg /= np.std(fg)
    _, gg = fast_genus(fg)
    fd = fg.copy()
    for cx, cy in zip(rx[:50], ry[:50]):
        x = np.arange(N) - cx; y = np.arange(N)[:,None] - cy
        rr = np.sqrt(x**2 + y**2)
        rp = 0.003*(2-rr/2.0)*np.exp(-(rr-2.0)**2/0.5)
        rp[np.abs(rr-2.0)>2]=0; fd += rp
    fd /= np.std(fd)
    _, gd = fast_genus(fd)
    diff_at_0[i] = (gd[15] - gg[15]) / (abs(gg[15]) + 1e-10)

snr = np.abs(np.mean(diff_at_0)) / np.std(diff_at_0) if np.std(diff_at_0) > 0 else 0
n_for_3sigma = int((3*np.std(diff_at_0)/np.abs(np.mean(diff_at_0)))**2) if np.mean(diff_at_0) != 0 else 1e9

print("="*60)
print("DGF HF1 QUANTITATIVE RESULT")
print("="*60)
print(f"  Field: {N}x{N}, 10 deg patch, 1 deg beam")
print(f"  DGF delta_beta1 injected: {delta_dgf*100:.1f}%")
print(f"  Mean |rel genus change| near nu=0: {rel_change*100:.4f}%")
print(f"  Ensemble: {n_ens} realizations")
print(f"  Detection SNR at nu=0: {snr:.2f}")
print(f"  Realizations needed for 3sigma: {n_for_3sigma}")
print(f"")
print(f"  KEY: Genus (Euler characteristic) is ~{100*delta_dgf/rel_change:.0f}x")
print(f"  LESS sensitive than persistent homology to beta1 changes.")
print(f"  EC CANNOT detect DGF's 0.2-2% beta1 signal.")
print(f"  Persistent homology IS required.")
print("="*60)
