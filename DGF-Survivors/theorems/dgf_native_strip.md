# DGF Native Strip Theorem

**Status**: Negative result -- bridge does NOT hold
**Date**: 2026-06-12
**Script**: `scripts/native_strip.py`

## 1. Problem Statement

DGF-Schwarzschild consistency check found: DGF has no true horizon (q > 0 everywhere), hence no conical singularity, no Euclidean regularity, and no strip-width constraint of the Schwarzschild type.

Question: What is the DGF-native "strip" structure, derived entirely from the boundary plaquette theorem without borrowing GR?

Core function:
```
QCMI(c,p) = H2(1/2 + 1/2 sqrt(1 - p(1-p)(4 sin^2(2c) + sin^2(4c))))
```

At p=1/2:
```
Delta(c) = 1 - sin^2(2c) - sin^2(4c)/4
         = 3/8 + cos(4c)/2 + cos(8c)/8
```

## 2. Two Competing Extensions to Complex c-Plane

### 2.1 Holomorphic Extension (Analytic Continuation)

sin^2(z) = [sin(z)]^2 (complex square). This is the mathematically correct analytic continuation.

For complex c = c_R + i c_I:
```
Im(Delta) = -sin(4c_R)sinh(4c_I)/2 - sin(8c_R)sinh(8c_I)/8
Re(Delta) = 3/8 + cos(4c_R)cosh(4c_I)/2 + cos(8c_R)cosh(8c_I)/8
```

Branch cuts:
- **S1 (sqrt)**: Im(Delta) = 0 AND Re(Delta) <= 0
- **S2 (H2)**:   Im(Delta) = 0 AND Re(Delta) >= 1 (since sqrt(Delta) >= 1 => z = 1/2 + sqrt(Delta)/2 >= 1, on the H2 branch cut)

### 2.2 Harmonic Extension (|sin|^2)

sin^2(z) interpreted as |sin(z)|^2 = sin(z)sin(z_bar). NOT holomorphic, but preserves reality.

```
Delta_modulus = 1 - |sin(2c)|^2 - |sin(4c)|^2/4
              = 1 - [sin^2(2c_R) + sinh^2(2c_I)] - [sin^2(4c_R) + sinh^2(4c_I)]/4
```

Always real. Branch condition: Delta_modulus <= 0 (sqrt branch cut).

## 3. Results: Holomorphic Extension

### 3.1 Im(Delta) Zero Structure

| c_R range | sin(4c_R) | sin(8c_R) | Im(Delta)=0 for c_I>0? |
|-----------|-----------|-----------|------------------------|
| [0, pi/8] | + | + | NO (same sign) |
| [pi/8, pi/4] | + | - | YES (opposite signs) |
| pi/4 | 0 | 0 | YES (always zero, special) |
| [pi/4, 3pi/8] | - | + | YES (opposite signs) |
| [3pi/8, pi/2] | - | - | NO (same sign) |
| pi/2 | 0 | 0 | YES (always zero, special) |

### 3.2 gamma_max(c_R) Table

| c_R/pi | gamma_max(analytic) | Hit Type |
|--------|---------------------|----------|
| 0.0000 | 0.00000000 | H2_immediate |
| 0.0312 | inf | infinite |
| 0.0625 | inf | infinite |
| 0.0938 | inf | infinite |
| 0.1250 | inf | infinite |
| 0.2500 | 0.44068679 | H2_finite (exact) |
| 0.2812 | 0.58389946 | S1_sqrt |
| 0.3750 | 0.21826170 | S1_sqrt |
| 0.4375 | 0.09893830 | S1_sqrt |
| 0.5000 | 0.00196844 | S1_sqrt |

At c_R = pi/4 exactly: sin(pi)=0, Im(Delta)=0 always. Re(Delta) = 3/8 - cosh(4c_I)/2 + cosh(8c_I)/8 ~ 16c_I^4 > 0 for c_I>0. S1 never hit. H2 cut at Re=1 => gamma_max = 0.4406867935.

### 3.3 Key Finding

**The holomorphic extension does NOT produce a uniform strip.**

- gamma_max = 0 at c_R = 0, pi/2 (H2 branch cut at the real axis origin)
- gamma_max = inf for c_R in (0, pi/8) U (3pi/8, pi/2) (no Im=0 crossing on principal sheet)
- gamma_max ~ 0.441 at c_R = pi/4 (H2 branch cut at finite c_I)
- QCMI(c) is **complex-valued** for Im(c) != 0 -- physically problematic for entropy

## 4. Results: Harmonic Extension

### 4.1 User's Derivation Error

The user computed `|sin(2c_I)|^2 = sinh^2(c_I)`. This is incorrect.

Correct: `|sin(2c)|^2 = |sin(2c_R + 2i c_I)|^2 = sin^2(2c_R) + sinh^2(2c_I)`

At c_R = 0: `|sin(2i c_I)|^2 = sinh^2(2c_I)`, NOT sinh^2(c_I).

The argument inside sinh is `2c_I`, not `c_I`. This is a **factor-of-2** error.

### 4.2 Correct gamma_max(c_R)

At c_R = 0:
```
Delta = 1 - sinh^2(2c_I) - sinh^2(4c_I)/4 = 0
=> sinh^2(2c_I) + sinh^2(4c_I)/4 = 1
=> c_I = 0.3029227993
```

This is **not** arcsinh(1) = 0.8814. The user's simplified 1 - sinh^2(c_I) = 0 is incorrect.

### 4.3 Full gamma_max Table

| c_R/pi | gamma_max(|sin|^2) | QCMI | tau_DGF | tau_Sch | ratio |
|--------|--------------------|------|---------|---------|-------|
| 0.0200 | 0.30201108 | 0.020557 | 14.6916 | 152.8253 | 0.0961 |
| 0.1000 | 0.28021864 | 0.276743 | 1.0126 | 11.3520 | 0.0892 |
| 0.2000 | 0.21426049 | 0.663948 | 0.3227 | 4.7317 | 0.0682 |
| 0.3000 | 0.11928148 | 0.912096 | 0.1308 | 3.4444 | 0.0380 |
| 0.4000 | 0.03369750 | 0.993412 | 0.0339 | 3.1624 | 0.0107 |
| 0.4800 | 0.00139393 | 0.999989 | 0.0014 | 3.1416 | 0.0004 |

### 4.4 Bridge Factor

```
DGF tau-strip / Schwarzschild tau-strip = mean(ratio) = 0.05097
Correction factor needed: 19.62
```

**The DGF native strip does NOT reproduce the Schwarzschild strip.** The ratio is ~5%, not ~100%.

## 5. P-Dependence

| p | gamma(c_R=0) | gamma(c_R=pi/8) | gamma(c_R=pi/4) |
|---|-------------|-----------------|-----------------|
| 0.1 | 0.430509 | 0.389518 | 0.372749 |
| 0.5 | 0.302923 | 0.168569 | 0.000000 |
| 0.9 | 0.430509 | 0.389518 | 0.372749 |

- Symmetric around p=0.5 (as expected from p(1-p) symmetry)
- gamma_max decreases with increasing p(1-p) (stronger QCMI -> narrower strip)
- gamma_max(c_R=pi/4) = 0 at p=0.5, nonzero for p != 0.5

## 6. Why the Bridge Fails

### 6.1 Structural Reason

DGF has no true horizon (q > 0 everywhere). The Schwarzschild strip emerges from Euclidean regularity at the horizon -- a conical singularity would form unless the imaginary time has period 2*pi/kappa.

DGF's boundary plaquette theorem defines a *different* analytic structure. The QCMI function's branch cuts in the complex Cartan plane do not map to the Schwarzschild imaginary-time periodicity.

### 6.2 The Mapping is Wrong

The naive mapping tau = c / kappa_eff assumes:
1. Cartan parameter c is proportional to Euclidean time
2. kappa_eff serves the same role as GR's surface gravity

Both assumptions fail quantitatively. The DGF Cartan parameter measures *quantum information distance* on the boundary plaquette, not proper time in the bulk. The mapping requires an area-renormalization factor that is not unity.

### 6.3 Three Possible Resolutions

1. **DGF needs a correction**: The boundary plaquette action may need an additional term that enforces Euclidean regularity at an effective horizon. This would introduce a new scale that matches kappa.

2. **The strip is fundamentally different**: DGF predicts a different thermodynamic structure near the boundary -- narrower strips, different Hawking temperature. This is a testable prediction that distinguishes DGF from GR.

3. **A different Cartan->time mapping**: The correct mapping may be `tau = f(c_R) * c / kappa_eff` where `f(c_R)` is a c_R-dependent renormalization factor that accounts for the non-trivial Jacobian between boundary Cartan coordinates and bulk proper time.

## 7. The Correct DGF Native Strip

The DGF native strip in the harmonic extension is:

```
S_DGF = {c_R + i c_I : 0 <= c_R <= pi/2, |c_I| < gamma_max(c_R)}
```

where gamma_max(c_R) solves:
```
sinh^2(2*gamma_max) + sinh^2(4*gamma_max)/4 = 1 - sin^2(2c_R) - sin^2(4c_R)/4
```

Properties:
- gamma_max(0) = 0.3029227993... (not arcsinh(1) = 0.8814)
- gamma_max(pi/4) = 0
- Smooth, monotonically decreasing from c_R=0 to c_R=pi/4
- Symmetric: gamma_max(pi/2 - c_R) = gamma_max(c_R)
- gamma_max(c_R) * kappa_eff(c_R) / pi ~ 0.051, not ~1

The strip width in Euclidean time domain:
```
Im(tau) in [-gamma_max/kappa_eff, gamma_max/kappa_eff]
```

This is ~5% of the Schwarzschild value pi/kappa.

## 8. Summary

| Quantity | Schwarzschild (GR) | DGF Native |
|----------|-------------------|------------|
| Origin | Euclidean regularity at horizon | QCMI analytic continuation |
| Parameter space | Euclidean time tau | Cartan parameter c |
| Strip | Im(tau) in [0, pi/kappa] | Im(c) in [-gamma_max, gamma_max] |
| Width | pi/kappa | 2*gamma_max |
| Mapping | N/A (fundamental) | tau = c/kappa_eff |
| Effective width | pi/kappa | gamma_max/kappa_eff |
| Bridge ratio | 1 (by definition) | ~0.051 |

**Conclusion**: The DGF native strip is a well-defined mathematical object derived from the boundary plaquette theorem's QCMI function. However, it does NOT quantitatively reproduce the Schwarzschild strip. The bridge between DGF and GR thermodynamics requires a correction factor of ~19.6, reflecting the fundamental difference between DGF's quantum-information boundary structure and GR's classical horizon geometry. This is a genuine physical gap in DGF that needs to be addressed -- either through a modified boundary action, a corrected Cartan-to-time mapping, or the acceptance that DGF makes a distinct prediction for near-boundary thermodynamics.

## References

- Boundary plaquette theorem: QCMI(c,p) from Gram matrix eigenvalues
- Schwarzschild Euclidean regularity: Gibbons-Hawking 1977, Euclidean approach to black hole thermodynamics
- DGF consistency check: See `dgf_schwarzschild_consistency.md`
