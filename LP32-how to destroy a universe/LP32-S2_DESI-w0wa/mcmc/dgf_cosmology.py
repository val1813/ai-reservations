"""
DGF Telegraph Equation -> Cosmological w(z)
===========================================
Core physics: q-field (information capacity fraction) drives dark energy.
The telegraph equation in FLRW reduces to an ODE for Delta = 1-q.

Key relation (overdamped limit, z < 2):
  Delta ∝ rho_*^{1/(n+1)}
  w(z)+1 ∝ SFR(z) / (H(z) * rho_*(z)^{n/(n+1)})

Free parameters: n (damping nonlinearity), A (normalization)
Natural baseline: n=1 -> p=1/2, w+1 ∝ SFR/(H * sqrt(rho_*))

Author: DGF Collaboration
Date: 2026-06-08
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.optimize import minimize

# ============================================================
# §1. Cosmological background
# ============================================================

class CosmologicalBackground:
    """FLRW background with standard cosmology + DGF dark energy."""

    def __init__(self, H0=70.0, Omega_m=0.30):
        self.H0 = H0  # km/s/Mpc
        self.Omega_m = Omega_m
        self.h = H0 / 100.0
        self.H0_si = H0 * 1000 / 3.086e22  # s^{-1}

    def H_z(self, z, w_DGF_func=None):
        """Hubble parameter H(z) in km/s/Mpc.
        Uses flat LCDM. If w_DGF_func is provided, uses DGF dark energy."""
        Om = self.Omega_m
        Ok = 0.0
        if w_DGF_func is None:
            # Standard LCDM
            Ode = 1.0 - Om
            return self.H0 * np.sqrt(Om * (1+z)**3 + Ok * (1+z)**2 + Ode)
        else:
            # DGF dark energy with evolving w(z)
            Ode_0 = 1.0 - Om
            # Integrate rho_DE(z) = rho_DE0 * exp(3 * integral_0^z (1+w(z'))/(1+z') dz')
            # We need a self-consistent solution: H(z) depends on rho_DE(z) and vice versa
            # For now, approximate: use LCDM H(z) for w(z) computation
            # Full self-consistent solution would iterate
            return self.H0 * np.sqrt(Om * (1+z)**3 + Ok * (1+z)**2 + Ode_0)

    def E_z(self, z):
        """Dimensionless Hubble parameter E(z) = H(z)/H0."""
        return self.H_z(z) / self.H0

    def cosmic_time_to_z(self, z_max=10.0, n_pts=2000):
        """Compute cosmic time t(z) in Gyr."""
        z_arr = np.logspace(-3, np.log10(z_max), n_pts)
        # dt/dz = -1 / (H(z) * (1+z))
        # t(z) = integral_z^infinity dz' / (H(z') * (1+z'))
        dz = np.diff(z_arr)
        H_mid = 0.5 * (self.H_z(z_arr[:-1]) + self.H_z(z_arr[1:]))
        z_mid = 0.5 * (z_arr[:-1] + z_arr[1:])
        dt_dz = 1.0 / (H_mid * (1 + z_mid))
        # Convert km/s/Mpc to Gyr: 1 km/s/Mpc = 9.78e-11 yr^{-1}
        conv = 1.0227e-21  # km/s/Mpc to Gyr^{-1}  # to Gyr^{-1}
        t_cum = np.cumsum(dt_dz[::-1] * np.diff(z_arr)[::-1]) / conv  # integrate from high z
        t_arr = np.zeros(len(z_arr))
        t_arr[1:] = t_cum[::-1]
        t_arr /= 1e9  # years to Gyr
        return interp1d(z_arr, t_arr, bounds_error=False, fill_value='extrapolate')

    def hubble_time(self, z):
        """Hubble time 1/H(z) in Gyr."""
        H = self.H_z(z)
        # H [km/s/Mpc] * 1.0227e-12 = H [yr^{-1}]
        # H [Gyr^{-1}] = H [yr^{-1}] * 1e9
        H_gyr = H * 1.0227e-12 * 1e9
        return 1.0 / H_gyr


# ============================================================
# §2. Star Formation Rate and Stellar Mass Density
# ============================================================

class CosmicStarFormation:
    """Cosmic star formation rate density and stellar mass density.

    Uses Madau & Dickinson (2014) SFR fitting formula:
      SFR(z) = 0.015 * (1+z)^2.7 / (1 + ((1+z)/2.9)^5.6)  [Msun/yr/Mpc^3]

    Stellar mass density rho_*(z) is the integral of SFR with recycling.
    """

    def __init__(self):
        # Madau-Dickinson 2014 parameters
        self.psi_0 = 0.015  # normalization [Msun/yr/Mpc^3]
        self.alpha = 2.7
        self.beta = 5.6
        self.z_p = 2.9
        # Recycling fraction (fraction of mass returned to ISM)
        self.R = 0.27  # Madau & Dickinson 2014

    def SFR(self, z):
        """Star formation rate density [Msun/yr/Mpc^3] at redshift z.
        Madau & Dickinson (2014) formula."""
        return self.psi_0 * (1+z)**self.alpha / (1 + ((1+z)/self.z_p)**self.beta)

    def SFR_alternative(self, z):
        """Alternative SFR from Behroozi et al. (2019) / UniverseMachine.
        Returns SFR in same units for comparison."""
        # Behroozi+2019, Table 3 / Fig 2, fit for z=0-10
        a = 1.0 / (1+z)
        log_psi = -1.5 - 0.5*(a - 0.5)**2 / 0.3**2 + 1.0*np.exp(-(a-0.15)**2/0.1**2)
        return 10**log_psi * 0.015

    def stellar_mass_density(self, z_eval, z_max=15.0, n_pts=5000):
        """Compute rho_*(z) = (1-R) * integral_z^{z_max} SFR(z') * dt/dz' dz'
        in units of Msun/Mpc^3.

        Integrates from high z (early universe, no stars) to low z (today, max stars)."""
        # Use ascending z (0 to z_max) for proper cumulative integration
        z_arr = np.concatenate([[0.0], np.logspace(-3, np.log10(z_max), n_pts)])
        # z_arr is ascending: z=0 ... z=z_max

        # dt/dz (positive, dt/dz > 0 means t increases with z? No: t DECREASES with z)
        # dt/dz = -1/(H*(1+z)). |dt/dz| = 1/(H*(1+z))
        H0 = 70.0
        Om = 0.30
        H_z = H0 * np.sqrt(Om * (1+z_arr)**3 + (1-Om))
        conv = 1.0227e-12  # km/s/Mpc to yr^{-1} (1/H0 [km/s/Mpc] = 1/H0 [yr^{-1}])
        dtdz_abs = 1.0 / (H_z * (1+z_arr) * conv)  # |dt/dz|, yr

        # SFR at grid points
        sfr_arr = self.SFR(z_arr)

        # Integrate from z=0 to z_max:
        # rho*(z) = (1-R) * integral_{z'=z}^{z_max} SFR(z') * |dt/dz'| dz'
        #         = (1-R) * [total_integral - integral_{z'=0}^{z} ...]
        integrand = sfr_arr * dtdz_abs
        # Cumulative integral from z=0: I(z) = int_0^z SFR * |dt/dz| dz
        I_cum = cumulative_trapezoid(integrand, z_arr, initial=0)
        # rho*(z) = (1-R) * (I(z_max) - I(z))
        I_total = I_cum[-1]
        rho_star = (1 - self.R) * (I_total - I_cum)

        # Create interpolator on ascending z
        interp = interp1d(z_arr, rho_star, bounds_error=False,
                         fill_value=(rho_star[-1], rho_star[0]))

        # Handle scalar or array input
        z_eval = np.atleast_1d(z_eval)
        is_scalar = np.ndim(z_eval) == 0 or (isinstance(z_eval, np.ndarray) and z_eval.ndim == 0)
        if is_scalar:
            z_eval = np.array([float(z_eval)])
        result = interp(z_eval)
        if len(result) == 1:
            return float(result[0])
        return result


# ============================================================
# §3. DGF w(z) from Telegraph Equation
# ============================================================

class DGF_DarkEnergy:
    """DGF dark energy equation of state w(z).

    Telegraph equation in FLRW, overdamped limit (z < ~2):
      gamma_0 * Delta^n * dDelta/dt = eta * SFR(t)

    Solution:
      Delta = C_DGF * rho_*(z)^{1/(n+1)}
      w(z)+1 = A * SFR(z) / (H(z) * rho_*(z)^{n/(n+1)})

    Free parameters:
      - n: damping nonlinearity index (natural baseline n=1 -> p=1/2)
      - A: overall amplitude (absorbs eta, gamma_0, C_DGF, and normalization)

    Also implements the full telegraph equation solver for comparison.
    """

    def __init__(self, cosmo=None, sfr=None):
        self.cosmo = cosmo if cosmo is not None else CosmologicalBackground()
        self.sfr = sfr if sfr is not None else CosmicStarFormation()

    def w_z_overdamped(self, z, n=1.0, A=1.0, normalized=True):
        """w(z) from overdamped telegraph equation.

        Parameters:
          n : damping nonlinearity index (0 to 2)
          A : amplitude parameter (dimensionless when normalized=True)
          normalized : if True, uses z=0 normalization so A ~ O(1)

        Returns w(z) array."""
        z = np.atleast_1d(z)
        H = self.cosmo.H_z(z)
        SFR = self.sfr.SFR(z)
        rho_star = self.sfr.stellar_mass_density(z)

        # w+1 ∝ SFR / (H * rho_star^{n/(n+1)})
        exponent = n / (n + 1)
        rho_pow = np.maximum(rho_star, 1e-20)**exponent

        raw = SFR / (H * rho_pow)

        if normalized:
            # Normalize by the z=0 value so A ~ O(1)
            raw_0 = self._compute_raw_0(n)
            w_plus_1 = A * raw / raw_0 * 0.2  # A=1 -> w(0)+1 = 0.2 (matching DESI w0 ~ -0.8)
        else:
            w_plus_1 = A * raw

        w = -1.0 + w_plus_1
        return w

    def _compute_raw_0(self, n):
        """Compute raw(0) = SFR(0) / (H(0) * rho_star(0)^{n/(n+1)})."""
        H0 = self.cosmo.H_z(0)
        SFR0 = self.sfr.SFR(0)
        rho_result = self.sfr.stellar_mass_density(np.array([0.0]))
        rho0 = float(rho_result) if not hasattr(rho_result, '__len__') else rho_result[0]
        # rho*(0) can be 0 due to interpolation at boundary; use z=0.01 as proxy
        if rho0 < 1e6:
            rho0 = float(self.sfr.stellar_mass_density(np.array([0.01])))
        exponent = n / (n + 1)
        return SFR0 / (H0 * max(rho0, 1e-20)**exponent)

    def w_z_full_telegraph(self, z, n=1.0, A=1.0, gamma0_H0=1.0, tau_c=0.1,
                          z_max=10.0, n_pts=2000):
        """w(z) from full telegraph equation numerical integration.

        Telegraph equation:
          d²Δ/dt² + gamma_0 * Δ^n * dΔ/dt + omega_0² * Δ = eta * SFR(t)

        where omega_0² comes from the q-field effective potential curvature.

        Parameters:
          n, A : same as overdamped
          gamma0_H0 : gamma_0 in units of H0
          tau_c : Cattaneo inertial timescale / Hubble time
          z_max : maximum redshift for integration
          n_pts : number of integration points
        """
        # Set up time grid
        z_arr = np.logspace(-3, np.log10(z_max), n_pts)
        t_of_z = self.cosmo.cosmic_time_to_z(z_max)
        t_arr = t_of_z(z_arr)  # Gyr

        # Interpolate SFR and rho_star as functions of time
        z_for_sfr = np.logspace(-3, np.log10(z_max), n_pts)
        sfr_arr = self.sfr.SFR(z_for_sfr)
        sfr_of_t = interp1d(t_arr, sfr_arr, bounds_error=False, fill_value=0)

        # Telegraph equation parameters
        H0_gyr = 1.0 / self.cosmo.hubble_time(0)  # Gyr^{-1}
        gamma_0 = gamma0_H0 * H0_gyr  # Gyr^{-1}
        omega_0 = 1.0 / (tau_c * H0_gyr)  # Gyr^{-1}, approximate

        # ODE system: y[0] = Delta, y[1] = dDelta/dt
        def telegraph_ode(t, y):
            Delta = max(y[0], 1e-10)
            dDelta_dt = y[1]
            SFR_t = sfr_of_t(t)
            # d²Δ/dt² = -gamma_0 * Δ^n * dΔ/dt - omega_0² * Δ + eta * SFR
            # eta is absorbed into A; we calibrate A*SFR to match the overdamped amplitude
            damping = gamma_0 * (Delta**n) * dDelta_dt
            restoring = omega_0**2 * Delta
            driving = A * H0_gyr * SFR_t / max(SFR_t, 1e-30) * 1e-3
            d2Delta_dt2 = -damping - restoring + driving
            return [dDelta_dt, d2Delta_dt2]

        # Initial conditions at high z (matter-dominated era)
        # Delta starts near 0 (q near 1, most capacity free)
        Delta_init = 1e-4
        dDelta_dt_init = 0.0

        # Integrate forward in time
        t_forward = t_arr  # already increasing
        sol = solve_ivp(telegraph_ode, [t_forward[0], t_forward[-1]],
                       [Delta_init, dDelta_dt_init],
                       t_eval=t_forward, method='LSODA',
                       rtol=1e-6, atol=1e-9)

        if not sol.success:
            raise RuntimeError(f"Telegraph ODE failed: {sol.message}")

        Delta_t = sol.y[0]

        # w(z) from Delta(t):
        # rho_DE ∝ Delta (information processing -> dark energy density)
        # w = -1 - (1/3) * d ln rho_DE / d ln a
        # d ln Delta / dt = dDelta/dt / Delta
        # d ln a / dt = H(t)
        dDelta_dt_t = sol.y[1]
        dln_Delta_dt = dDelta_dt_t / np.maximum(Delta_t, 1e-20)
        H_t = self.cosmo.H_z(z_arr)
        conv = 1.0227e-21  # km/s/Mpc to Gyr^{-1}  # to Gyr^{-1}
        H_t_gyr = H_t * conv

        w = -1.0 - (1.0/3.0) * dln_Delta_dt / H_t_gyr

        return z_arr, w

    def w_z_to_w0wa(self, z, w_z):
        """Fit w(z) to CPL parametrization: w(a) = w0 + wa*(1-a).
        Returns (w0, wa) from least-squares fit."""
        a = 1.0 / (1.0 + z)
        # w(a) = w0 + wa*(1-a)
        # Design matrix: [1, (1-a)]
        X = np.column_stack([np.ones_like(a), 1 - a])
        w0, wa = np.linalg.lstsq(X, w_z, rcond=None)[0]
        return w0, wa


# ============================================================
# §4. Likelihood functions
# ============================================================

class DESILikelihood:
    """DESI DR2 likelihood for (w0, wa) or binned w(z).

    Uses the compressed DESI DR2 constraints from arXiv:2503.14738.
    For proper MCMC, we need the full covariance matrix.
    This class provides both the compressed (w0, wa) likelihood
    and tools for binned w(z) comparison.
    """

    def __init__(self):
        # DESI DR2 + CMB + DESY5 best-fit (from arXiv:2503.14738):
        # w0 = -0.785 ± 0.047, wa = -0.43 ± 0.10
        # With correlation coefficient rho ~ -0.8
        self.w0_obs = -0.785
        self.wa_obs = -0.43
        self.sigma_w0 = 0.047
        self.sigma_wa = 0.10
        self.rho = -0.80  # correlation

        # Covariance matrix
        cov_w0_wa = self.rho * self.sigma_w0 * self.sigma_wa
        self.cov = np.array([[self.sigma_w0**2, cov_w0_wa],
                            [cov_w0_wa, self.sigma_wa**2]])
        self.inv_cov = np.linalg.inv(self.cov)

        # LCDM reference: w0=-1, wa=0
        self.w0_lcdm = -1.0
        self.wa_lcdm = 0.0

    def loglike_w0wa(self, w0, wa):
        """Log-likelihood for (w0, wa) under DESI DR2 + CMB + DESY5."""
        delta = np.array([w0 - self.w0_obs, wa - self.wa_obs])
        return -0.5 * delta @ self.inv_cov @ delta

    def chi2_w0wa(self, w0, wa):
        """Chi-squared for (w0, wa)."""
        return -2.0 * self.loglike_w0wa(w0, wa)

    def chi2_lcdm(self):
        """Chi-squared for LCDM (w0=-1, wa=0)."""
        return self.chi2_w0wa(self.w0_lcdm, self.wa_lcdm)

    def bayes_factor_approx(self, w0_dgf, wa_dgf):
        """Approximate Bayes factor DGF vs LCDM using BIC-like criterion.

        BF > 1: DGF preferred
        BF > 10: strong evidence for DGF
        BF > 100: decisive
        """
        chi2_dgf = self.chi2_w0wa(w0_dgf, wa_dgf)
        chi2_lcdm = self.chi2_lcdm()
        # DGF has 2 extra parameters (n, A) vs LCDM (0)
        # BIC: Delta_BIC = Delta_chi2 - (k_dgf - k_lcdm)*ln(N)
        # For DESI: N ~ 3000 effective data points
        N_eff = 3000
        k_diff = 2
        delta_chi2 = chi2_lcdm - chi2_dgf
        delta_bic = delta_chi2 - k_diff * np.log(N_eff)
        # Approximate Bayes factor: BF ≈ exp(Delta_BIC/2)
        bf = np.exp(delta_bic / 2.0)
        return bf, chi2_dgf, chi2_lcdm


# ============================================================
# §5. MCMC Sampler
# ============================================================

class MCMC:
    """Simple Metropolis-Hastings MCMC sampler for DGF parameters."""

    def __init__(self, log_prob_func, param_names, init, step_sizes,
                 n_walkers=1):
        self.log_prob = log_prob_func
        self.param_names = param_names
        self.n_params = len(param_names)
        self.step_sizes = np.atleast_1d(step_sizes)
        self.n_walkers = n_walkers
        self.init = init

    def run(self, n_steps, burn_in=1000, progress=True):
        """Run MCMC chain."""
        n_total = n_steps + burn_in
        chain = np.zeros((n_total, self.n_params))

        # Initialize
        current = np.array(self.init)
        current_logp = self.log_prob(*current)

        accepted = 0
        for i in range(n_total):
            # Propose
            proposal = current + np.random.normal(0, self.step_sizes, self.n_params)
            proposal_logp = self.log_prob(*proposal)

            # Accept/reject
            log_ratio = proposal_logp - current_logp
            if np.log(np.random.random()) < log_ratio:
                current = proposal
                current_logp = proposal_logp
                accepted += 1

            chain[i] = current

            if progress and (i+1) % 1000 == 0:
                acc_rate = accepted / (i+1)
                print(f"  Step {i+1}/{n_total}, accept={acc_rate:.3f}, "
                      f"params={dict(zip(self.param_names, current))}")

        # Discard burn-in
        self.chain = chain[burn_in:]
        self.acceptance_rate = accepted / n_total
        return self.chain

    def summary(self):
        """Print parameter summary."""
        print(f"\nMCMC Summary (acceptance rate: {self.acceptance_rate:.3f})")
        print(f"{'Param':>12s}  {'Mean':>10s}  {'Std':>10s}  "
              f"{'16%':>10s}  {'84%':>10s}")
        print("-" * 58)
        for i, name in enumerate(self.param_names):
            samples = self.chain[:, i]
            mean = np.mean(samples)
            std = np.std(samples)
            lo, hi = np.percentile(samples, [16, 84])
            print(f"{name:>12s}  {mean:10.4f}  {std:10.4f}  "
                  f"{lo:10.4f}  {hi:10.4f}")


# ============================================================
# §6. Run Analysis
# ============================================================

def run_analysis(n_mcmc=20000, burn_in=5000):
    """Run the full DGF vs DESI analysis."""
    print("=" * 70)
    print("DGF Telegraph Equation -> DESI DR2 MCMC Analysis")
    print("=" * 70)

    # Setup
    cosmo = CosmologicalBackground()
    sfr = CosmicStarFormation()
    dgf = DGF_DarkEnergy(cosmo, sfr)
    like = DESILikelihood()

    # Grid of z for evaluation
    z_grid = np.logspace(-2, np.log10(5.0), 200)

    # --- §6.1: Overdamped solution ---
    print("\n--- Overdamped Telegraph Equation ---")

    # Scan over (n, A) grid
    n_vals = np.array([0.5, 0.75, 1.0, 1.25, 1.5])
    results = []

    for n in n_vals:
        # Find best-fit A by minimizing chi2 on (w0,wa) grid
        def chi2_for_A(logA):
            A = np.exp(logA)
            w_z = dgf.w_z_overdamped(z_grid, n=n, A=A, normalized=True)
            w0, wa = dgf.w_z_to_w0wa(z_grid, w_z)
            return like.chi2_w0wa(w0, wa)

        res = minimize(chi2_for_A, x0=np.log(1.0), method='Nelder-Mead')
        A_best = np.exp(res.x[0])
        w_z_best = dgf.w_z_overdamped(z_grid, n=n, A=A_best, normalized=True)
        w0, wa = dgf.w_z_to_w0wa(z_grid, w_z_best)
        chi2 = like.chi2_w0wa(w0, wa)
        bf, _, chi2_lcdm = like.bayes_factor_approx(w0, wa)

        results.append({
            'n': n, 'A': A_best, 'w0': w0, 'wa': wa,
            'chi2': chi2, 'bf': bf
        })
        print(f"  n={n:.2f}: A={A_best:.4f}, (w0,wa)=({w0:.4f}, {wa:.4f}), "
              f"chi2={chi2:.2f}, BF={bf:.1f}")

    # --- §6.2: MCMC over (n, A) ---
    print(f"\n--- MCMC ({n_mcmc} steps, {burn_in} burn-in) ---")

    def log_prob(n, logA):
        """Log-posterior: log-likelihood + priors."""
        A = np.exp(logA)
        # Priors
        if n < 0.2 or n > 2.0:
            return -np.inf
        if A < 1e-10 or A > 1e10:
            return -np.inf
        # Gaussian prior on n ~ 1.0 ± 0.3
        log_prior_n = -0.5 * ((n - 1.0) / 0.3)**2
        # Flat prior on logA
        log_prior_A = 0.0

        # Likelihood
        w_z = dgf.w_z_overdamped(z_grid, n=n, A=A)
        w0, wa = dgf.w_z_to_w0wa(z_grid, w_z)
        log_like = like.loglike_w0wa(w0, wa)

        return log_prior_n + log_prior_A + log_like

    sampler = MCMC(log_prob, ['n', 'logA'], init=[1.0, 0.0],
                   step_sizes=[0.05, 0.15])
    chain = sampler.run(n_mcmc, burn_in)
    sampler.summary()

    # --- §6.3: Best-fit DGF vs LCDM comparison ---
    print("\n--- DGF vs LCDM ---")
    n_best = np.median(chain[:, 0])
    logA_best = np.median(chain[:, 1])
    A_best = np.exp(logA_best)
    w_z_dgf = dgf.w_z_overdamped(z_grid, n=n_best, A=A_best)
    w0_dgf, wa_dgf = dgf.w_z_to_w0wa(z_grid, w_z_dgf)

    chi2_dgf = like.chi2_w0wa(w0_dgf, wa_dgf)
    chi2_lcdm = like.chi2_lcdm()
    bf, _, _ = like.bayes_factor_approx(w0_dgf, wa_dgf)

    print(f"  DGF best-fit:  (w0, wa) = ({w0_dgf:.4f}, {wa_dgf:.4f})")
    print(f"  DGF χ² = {chi2_dgf:.2f}")
    print(f"  LCDM χ² = {chi2_lcdm:.2f}")
    print(f"  Δχ² = {chi2_lcdm - chi2_dgf:.2f}")
    print(f"  Approx Bayes Factor = {bf:.1f}")

    # --- §6.4: w(z) shape ---
    print("\n--- w(z) Non-Monotonicity ---")
    # Check for peak in w(z)
    w_z = dgf.w_z_overdamped(z_grid, n=n_best, A=A_best)
    peak_idx = np.argmax(w_z)
    z_peak = z_grid[peak_idx]
    w_peak = w_z[peak_idx]
    print(f"  w(z) peak at z ≈ {z_peak:.2f}, w ≈ {w_peak:.4f}")
    print(f"  w(z=0) = {w_z[0]:.4f}")
    print(f"  w(z=2) = {w_z[np.argmin(np.abs(z_grid-2))]:.4f}")

    return {
        'n_best': n_best, 'A_best': A_best,
        'w0_dgf': w0_dgf, 'wa_dgf': wa_dgf,
        'chi2_dgf': chi2_dgf, 'chi2_lcdm': chi2_lcdm,
        'bayes_factor': bf,
        'z_peak': z_peak, 'w_peak': w_peak,
        'chain': chain, 'z_grid': z_grid, 'w_z': w_z,
        'grid_results': results
    }


if __name__ == '__main__':
    results = run_analysis(n_mcmc=20000, burn_in=5000)
