# INSPECTOR report: NSF-FCS-1 B Round 2

Input checked:

- `current/B/NSF_FCS_round2_B.md`

Forbidden input:

- Did not read any A file.

## Q1. 量纲校对

### Formula 1: `S_R(L)=lambda_R''(0)/G_R(L)`

Assume the counting field is dimensionless and `lambda_R(chi)` is the scaled cumulant generating function per unit time.

- LHS SI unit: unit of `S_R`; not intrinsically fixed unless defined.
- RHS: `lambda_R''(0)` has unit `count^2 / time`. If `G_R` is linear response of mean count current to a dimensionless affinity, then `G_R` has unit `count / time`, so RHS has unit `count`, effectively dimensionless for particle-count convention.
- Match: conditionally pass.

Warning: this formula is dimensionally clean only if `G_R(L)` is conductance with respect to a dimensionless driving force/affinity, for example `beta Delta mu`, or if the physical bias unit is explicitly absorbed into `G_R`. If `G_R=dJ_R/d(Delta mu)` with `Delta mu` carrying energy units, then `lambda_R''/G_R` has energy units and should not be called a dimensionless noise/conductance ratio without an extra thermal/bias conversion factor.

Verdict: ⚠️ dimension convention missing. Not a blocker for scaling comparison, but the file should explicitly state the affinity convention.

### Formula 2: `lambda_R''(0)=A_R(L)+K_R(L)`

- LHS SI unit: `count^2 / time`.
- `A_R=<a_R>_pi`, with `a_R(x)=sum_y k(x,y)g_R(x,y)^2`: rate times count squared, hence `count^2 / time`.
- `K_R=2<h_R,phi_R>_pi`, with `h_R=b_R-J_R`: `count / time`. Since `-L phi_R=h_R` and `L` has unit `1/time`, `phi_R` has unit `count`. Therefore `K_R` has unit `count^2 / time`.
- Match: pass.

### Formula 3: `K_R(L)=2<b_R-J_R,phi_R>_pi`; `-L phi_R=b_R-J_R`

- `L` unit: `1/time`.
- `b_R-J_R` unit: `count/time`.
- `phi_R` unit from Poisson equation: `count`.
- Inner product unit: `count^2/time`.
- Match: pass.

### Transcendental arguments

No relevant `exp`, `sin`, `log`, or `sinh` formula with dimensional argument appears in the inspected block.

## Q2. 符号/方向校对

### Poisson solve direction

For the stated generator `(Lf)(x)=sum_y k(x,y)[f(y)-f(x)]`, `L` has non-positive spectrum on centered functions. The equation

`-L phi_R=h_R`, where `h_R=b_R-J_R`,

therefore gives `phi_R=(-L)^(-1)h_R`, and the Green correction

`K_R=2<h_R,phi_R>_pi`

has the standard non-negative resolvent direction in the reversible benchmark case. The sign is not reversed.

Verdict: pass.

### `A_R/K_R` extraction direction

The sequence

1. compute `pi`;
2. calibrate `G_R`;
3. compute `A_R,K_R,lambda_R''`;
4. form `S_R=lambda_R''/G_R`;
5. compare reservoir implementations

does not use `lambda_R''` to tune `G_R`. This avoids the self-confirming direction error called out in the task.

Verdict: pass.

### 保留/击毙 B 假说

The main criterion is internally consistent:

- keep B alive if calibrated same-scale `G_R` also yields reservoir-independent constant `S_R`;
- kill B if same-scale `G_R` yields drifting or reservoir-sensitive `S_R`.

This direction is not reversed in the INSPECTOR_CHECK block, section 3.1, section 3.2, or the next-step plan.

Minor warning: the sentence in section 5.2 saying that constant single-particle `S_R(L)` looks like "B only holds in special implementations" is directionally ambiguous. A constant `S_R` in the single-particle test is evidence that B survives that test, not by itself evidence of non-universality. It can only support "special implementation only" if combined with another implementation or many-particle test that fails.

Verdict: main direction pass; one local explanatory sentence should be clarified.

## Q3. 循环论证校对

The INSPECTOR_CHECK block separates:

- input assumptions: finite generator, right-boundary counting, low-density/single-particle compression;
- computed objects: `pi`, boundary jump graph, Poisson solution, `A_R,K_R,lambda_R''`;
- independent calibration: `G_R`;
- diagnostic output: scaling and reservoir sensitivity of `S_R`.

The document explicitly warns against using `lambda_R''(0)` to tune parameters before computing `S_R`. No circular proof is found in the stated workflow.

Verdict: pass.

## Q4. 量级鸿沟标记

No explicit numeric comparison of the form `10^N` vs `10^M` appears in the inspected derivation. No numerical order-of-magnitude gulf can be checked yet.

Verdict: not applicable for this round.

## Q5. 代数验算

### Additive functional decomposition

Definitions:

- `b_R(x)=sum_y k(x,y)g_R(x,y)`
- `a_R(x)=sum_y k(x,y)g_R(x,y)^2`
- `J_R=<b_R>_pi`
- `h_R=b_R-J_R`
- `-L phi_R=h_R`, with `<phi_R>_pi=0`

Then:

- `A_R=<a_R>_pi`
- `K_R=2<h_R,phi_R>_pi`
- `lambda_R''(0)=A_R+K_R`

Given the generator convention in the file, this is the standard Poisson/resolvent structure for the second cumulant rate of a jump-count additive functional, modulo model-specific nonreversible adjoint conventions. The file does not introduce an algebraic sign flip.

Verdict: pass, with the caveat that a future implementation should document whether the numerical solver uses row-generator or column-generator convention. If the matrix is transposed in code, the Poisson equation must be transposed consistently.

### Limit checks

- If `h_R=0`, then `phi_R=0`, `K_R=0`, and `lambda_R''=A_R`. The formula reduces correctly to pure local activity noise.
- If all right-boundary jumps are removed, then `g_R=0`, `a_R=0`, `b_R=0`, `J_R=0`, `h_R=0`, hence `lambda_R''=0`. The formula reduces correctly.
- If two reservoirs have same calibrated `G_R` but different `a_R` or different Green correction, the formula allows different `S_R`, matching the stated kill criterion.

Verdict: pass.

## Q6. 综合判定

⚠️ INSPECTOR warning: `S_R=lambda_R''/G_R` requires an explicit conductance convention. State that `G_R` is response to dimensionless affinity, or include the missing physical-unit conversion.

⚠️ INSPECTOR warning: section 5.2 has one directionally ambiguous explanatory sentence about constant single-particle `S_R`; the main retain/kill criterion is correct and not reversed.

✅ INSPECTOR pass for the requested blockers: no fatal量纲错误 under dimensionless-affinity convention, no `A_R/K_R` Poisson sign reversal, and no reversal of the main "retain/kill B hypothesis" direction.
