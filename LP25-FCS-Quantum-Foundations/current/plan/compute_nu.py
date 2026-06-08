"""
Compute nu(alpha) - the occupation gradient scaling exponent.
Key relationship: C_mid = -i (h_mid/gamma_phi) * grad_mid * correction
where correction -> 1 for large L.
So beta(alpha) = nu(alpha) asymptotically.
"""
import sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov
import json

J0 = 0.3
Gamma_L = 1.0
Gamma_R = 1.0
f_L = 0.65
f_R = 0.35

def construct_h(L, alpha):
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i+1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h

def solve_ness(L, alpha, gamma_phi):
    h = construct_h(L, alpha)
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j
            A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                A[row, row] += gamma_phi
            for k in range(L):
                if abs(h[i, k]) > 1e-15:
                    col = k * L + j
                    A[row, col] += 1j * h[i, k]
                if abs(h[k, j]) > 1e-15:
                    col = i * L + k
                    A[row, col] -= 1j * h[k, j]
            if i == j:
                b_vec[row] = W_in[i]

    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)
    return C, h

# ============================================================
# Compute nu(alpha) and beta(alpha) for larger L values
# ============================================================
print("=" * 100)
print("OCCUPATION GRADIENT SCALING: grad_mid ~ L^{-nu(alpha)}")
print("=" * 100)

gamma_phi = 0.5
L_vals = [4, 8, 16, 32, 64]  # L=128 too slow for linear solve
alphas = [1.1, 1.3, 1.5, 1.7, 1.9]

results = {}
for alpha in alphas:
    grads = []
    cmids = []
    ratios = []
    L_used = []
    for L in L_vals:
        try:
            C, h = solve_ness(L, alpha, gamma_phi)
            mid_i = L // 2 - 1
            mid_j = L // 2
            C_mid = C[mid_i, mid_j]
            D = np.diag(C.real)
            grad_mid = D[mid_j] - D[mid_i]
            h_mid = h[mid_i, mid_j].real

            # First-order prediction
            C_mid_1st = h_mid * abs(grad_mid) / gamma_phi
            ratio = abs(C_mid) / C_mid_1st if C_mid_1st > 1e-20 else 0

            grads.append(abs(grad_mid))
            cmids.append(abs(C_mid))
            ratios.append(ratio)
            L_used.append(L)
        except Exception as e:
            print("  L={}: {}".format(L, e))
            break

    # Log-log fit for gradient
    logL = np.log(L_used)
    logG = np.log(grads)
    nu = -np.polyfit(logL, logG, 1)[0]

    # Log-log fit for C_mid
    logC = np.log(cmids)
    beta = -np.polyfit(logL, logC, 1)[0]

    results[alpha] = {
        'L': L_used, 'grads': grads, 'cmids': cmids,
        'ratios': ratios, 'nu': nu, 'beta': beta
    }

    print("\nalpha={:.1f} (L up to {})".format(alpha, L_used[-1]))
    print("  L      grad_mid         |C_mid|          ratio          C_1st_pred")
    for i in range(len(L_used)):
        c1 = results[alpha]['cmids'][i]
        g = results[alpha]['grads'][i]
        r = results[alpha]['ratios'][i]
        c1st = 0.3 * g / gamma_phi
        print("  {:>4d}  {:>14.6e}  {:>14.6e}  {:>14.6f}  {:>14.6e}".format(
            L_used[i], g, c1, r, c1st))
    print("  nu(alpha) = {:.4f}, beta(alpha) = {:.4f}".format(nu, beta))

# ============================================================
# Summary comparison
# ============================================================
print("\n" + "=" * 100)
print("SUMMARY: nu vs beta")
print("=" * 100)
print("{:>8s} {:>10s} {:>10s} {:>10s} {:>10s}".format(
    'alpha', 'nu', 'beta', 'beta_COH', 'ratio_last'))
for alpha in alphas:
    r = results[alpha]
    # COH beta from phase2_fit_results_FULL.json for gamma_phi=0.5
    coh_beta = {1.1: 1.1723, 1.3: 1.0428, 1.5: 0.9427, 1.7: 0.8912, 1.9: 0.8715}
    print("{:>8.1f} {:>10.4f} {:>10.4f} {:>10.4f} {:>10.4f}".format(
        alpha, r['nu'], r['beta'], coh_beta[alpha], r['ratios'][-1]))

# ============================================================
# Fit analytic form for nu(alpha)
# ============================================================
print("\n" + "=" * 100)
print("FITTING ANALYTIC FORM FOR nu(alpha)")
print("=" * 100)

alphas_arr = np.array(alphas)
nus = np.array([results[a]['nu'] for a in alphas])
betas = np.array([results[a]['beta'] for a in alphas])

# Try various forms:
# Form 1: nu = c0 + c1/alpha
A = np.column_stack([np.ones_like(alphas_arr), 1.0/alphas_arr])
c = np.linalg.lstsq(A, nus, rcond=None)[0]
print("Form 1: nu = {:.4f} + {:.4f}/alpha".format(c[0], c[1]))
print("  Residuals:", nus - (c[0] + c[1]/alphas_arr))

# Form 2: nu = c0 + c1*alpha
A = np.column_stack([np.ones_like(alphas_arr), alphas_arr])
c = np.linalg.lstsq(A, nus, rcond=None)[0]
print("Form 2: nu = {:.4f} + {:.4f}*alpha".format(c[0], c[1]))
print("  Residuals:", nus - (c[0] + c[1]*alphas_arr))

# Form 3: nu = 2/alpha (motivated by Costa et al. exponent)
print("Form 3: nu = 2/alpha")
print("  Predicted:", 2.0/alphas_arr)
print("  Residuals:", nus - 2.0/alphas_arr)

# Form 4: nu = 2/alpha - 1 (motivated by fractional Laplacian order s=alpha-1/2)
print("Form 4: nu = 2/alpha - 1")
print("  Predicted:", 2.0/alphas_arr - 1)
print("  Residuals:", nus - (2.0/alphas_arr - 1))

# Form 5: nu = 3 - 2*alpha (linear)
print("Form 5: nu = 3 - 2*alpha")
print("  Predicted:", 3 - 2*alphas_arr)
print("  Residuals:", nus - (3 - 2*alphas_arr))

# Form 6: nu = c0 + c1*log(alpha)
A = np.column_stack([np.ones_like(alphas_arr), np.log(alphas_arr)])
c = np.linalg.lstsq(A, nus, rcond=None)[0]
print("Form 6: nu = {:.4f} + {:.4f}*ln(alpha)".format(c[0], c[1]))
print("  Residuals:", nus - (c[0] + c[1]*np.log(alphas_arr)))

# Form 7: nu = (2*alpha - 1) / (2*alpha) ???
print("Form 7: nu = (3-2*alpha)? No... let me try nu = (alpha+1)/(2alpha-1)")
pred7 = (alphas_arr + 1) / (2*alphas_arr - 1)
print("  Predicted:", pred7)
print("  Residuals:", nus - pred7)

# Form 8: nu = 1 + (alpha-1)*something???
# Let me fit the difference from 1
diff = 1.0 - nus  # how much less than 1
print("\nForm 8: 1 - nu vs alpha")
print("  1-nu values:", diff)
# Try: 1-nu = c*(alpha-1)/(2*alpha-1) or similar
print("  (alpha-1)/(2*alpha-1):", (alphas_arr-1)/(2*alphas_arr-1))
print("  Ratio (1-nu) / ((alpha-1)/(2*alpha-1)):", diff / ((alphas_arr-1)/(2*alphas_arr-1)))

# Form 9: nu = (2*alpha - 1)^{-1} * something
print("\nForm 9: nu = 1/(2*alpha-1)")
print("  Predicted:", 1.0/(2*alphas_arr-1))
print("  Residuals:", nus - 1.0/(2*alphas_arr-1))

# Let me try forms motivated by the Costa et al. current scaling J ~ L^{1-2*alpha}
# If conductance G ~ L^{2-2*alpha} for alpha < 3/2, then delta_mu ~ G^{-1} ~ L^{2*alpha-2}
# The gradient ~ delta_mu / L ~ L^{2*alpha-3}
# So nu = 3 - 2*alpha for alpha < 3/2? Check:
# alpha=1.1: nu=3-2.2=0.8, actual nu=1.12 -- NO, wrong sign!

# Actually, the Costa et al. result is for the OPEN system (infinite leads).
# Our system has finite leads (Gamma_L, Gamma_R), which changes the boundary conditions.

# Let me try: nu = 1 - (alpha-1)/(2*alpha-1) or related
print("\nForm 10: nu = 1 + (1-alpha)/(2*alpha-1)")
pred10 = 1 + (1-alphas_arr)/(2*alphas_arr-1)
print("  Predicted:", pred10)
print("  Residuals:", nus - pred10)

# Maybe a rational function
# nu = (a*alpha + b) / (c*alpha + d)
# Using 2 data points:
# (1.1, 1.1175) and (1.9, 0.8310)
# a*1.1 + b = 1.1175*(c*1.1 + d)
# a*1.9 + b = 0.8310*(c*1.9 + d)
# Six unknowns, 2 equations.
# Try: nu = p + q/alpha (already done - Form 1)

# Let me fit to a padé approximant: nu = (a + b*alpha)/(c + d*alpha)
# With c=1 normalization: nu = (a + b*alpha)/(1 + d*alpha)

# From Form 1: nu = 0.45 + 0.72/alpha = (0.45*alpha + 0.72)/alpha
# This is already a rational function with denominator alpha.

# Let me check the quality
print("\n" + "="*100)
print("BEST FIT: nu(alpha) = a + b/alpha")
print("="*100)
from numpy import polyfit
# Fit to a + b/alpha using all points
X = 1.0 / alphas_arr
coeffs = polyfit(X, nus, 1)
a, b = coeffs[0], coeffs[1]  # nu = a*(1/alpha) + b
print("nu = {:.6f}/alpha + {:.6f}".format(a, b))
nu_pred = a/alphas_arr + b
print("alpha  nu_data  nu_pred  residual")
for i, alpha in enumerate(alphas):
    print("{:.1f}   {:.4f}   {:.4f}   {:.6f}".format(alpha, nus[i], nu_pred[i], nus[i]-nu_pred[i]))

# Check if the residual pattern suggests a different functional form
residuals = nus - nu_pred
print("\nResidual pattern:", residuals)
print("This is a very good fit. Let me see if I can derive this form.")

# The fitted form: nu = a/alpha + b
# From physics: nu ~ 1 for alpha -> infinity (nearest-neighbor, diffusive)
# nu(infinity) = 1 -> b = 1?
# b from fit: ~0.44, not ~1. So nu(infinity) = 0.44, not 1.
# This suggests either:
# 1. Our L values aren't large enough to see the true asymptotic
# 2. The asymptotic for pure power-law with alpha->infinity isn't the same as NN

# Actually, let me check: for alpha -> infinity, our model approaches strict NN hopping.
# For strict NN with these parameters, what is nu?
print("\n--- NN check ---")
for L in [16, 32, 64]:
    C, h = solve_ness(L, 5.0, 0.5)  # Use alpha=5 as proxy for NN
    mid_i = L // 2 - 1
    mid_j = L // 2
    D = np.diag(C.real)
    grad = abs(D[mid_j] - D[mid_i])
    Cmid = abs(C[mid_i, mid_j])
    print("L={}: grad={:.6e}, |C_mid|={:.6e}".format(L, grad, Cmid))

# The issue might be that the gradient at the midpoint doesn't scale as simple power-law.
# Let me fit with three-parameter form.
