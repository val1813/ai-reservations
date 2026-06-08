# NSF-FCS-2 Round 2 研究计划

## Goal

把 NSF-FCS-2 从“小系统 ansatz”推进为可审稿的 bounded claim。

## Task 1: Direct Delta Test

Run centered density pairs around `rho_bar=0.5`:

- `delta=0.05`: `0.475 -> 0.525`
- `delta=0.10`: `0.45 -> 0.55`
- `delta=0.15`: `0.425 -> 0.575`
- `delta=0.20`: `0.40 -> 0.60`
- `delta=0.30`: `0.35 -> 0.65`

Use raw `R2`, not only `Qhat`. Minimal acceptable output:

- slope of `log R2` vs `log delta` at fixed `L,alpha`;
- show whether slope is near 2 before normalizing by `delta^2`.

## Task 2: Off-Center Reverse Bias

Run:

- `0.50 -> 0.30` compared with `0.30 -> 0.50`
- `0.75 -> 0.55` compared with `0.55 -> 0.75`

Minimal acceptable output:

- max absolute difference in `R2`;
- max absolute difference in `S_T`;
- note whether odd contamination appears.

## Task 3: Model Comparison for Qhat

For available `L` values compare:

- power law `Qhat ~ L^p`;
- constant plus correction `Qhat = q_inf + a L^{-b}`;
- logarithmic drift `Qhat = a + b log L`;
- crossover power on sliding windows.

Do not claim asymptotic `L^{1/2}` unless larger-L and model comparison support it.

## Task 4: Activity Controls

Inspect `scripts/nsf_fcs_transport_ledger.py` for the lowest-risk extension:

- `activity_mode=none`
- `activity_mode=reversible_side`
- `activity_mode=nonLDB_site_skew`

If implementation is too large for this round, write exact CLI/CSV design first.
