# THEORY REPAIR SEG1: β=a/α+b 的无降级修复

结论：不要再写“解析推出唯一 β=a/α+b”。改成：

> β 是第二独立标度指数；`1/α` 是 off-diagonal coherence sector 的 leading scaling variable。`β=a(γ_phi)/α+b(γ_phi)` 不是事后插值，而是由两个渐近 fixed points 约束的 leading scaling ansatz，并由 collapse test 验证。系数 `a,b` 是非普适幅度；指数结构和 collapse 是主张核心。

这不是降级成 finite-size observation。降级的是“唯一解析闭式公式”的措辞，不降级的是 PRL 主张：β 独立于 μ，且 β 的主标度由 `1/α` 控制。

## 1. 新主张边界

### Leading scaling window

主文可明确宣称 leading `1/α` scaling 的窗口：

```text
0.5 <= γ_phi <= 2.0,    1.3 <= α <= 1.9,    L >= 8/16
```

理由：

- `γ_phi=0.5,1.0,2.0` 是 hopping-dephasing competition 到 near-diffusive 的稳定窗口。
- `α=1.3-1.9` 避开 `α -> 1+` 的 fully nonlocal boundary layer 最慢收敛区。
- 这里 `β=a(γ_phi)/α+b(γ_phi)` 应被称为 leading scaling law / leading scaling ansatz，不称 exact thermodynamic formula。

### Correction-dominated scaling window

以下不能丢弃，也不能称 finite-size observation；应称 correction-dominated scaling window：

```text
γ_phi = 0.01: ballistic fixed-point dominated window
γ_phi = 0.1: weak-dephasing crossover window
α = 1.1: long-range Robin-boundary correction window
```

口径：

- `γ_phi=0.01` 中 β 近似常数，不承载 `1/α` 斜率主张；它验证 `a(γ_phi)->0` 的 ballistic fixed point。
- `γ_phi=0.1` 是从 ballistic fixed point 流向 interacting hopping-dephasing fixed point 的 crossover；允许出现 competing linear/log fits。
- `α=1.1` 是非局域边界层最强处；它检验 correction-to-scaling 的符号和收敛速度，不用于单独证明 leading form。

## 2. 可粘贴进主稿 III.B 的替换段落

替换 III.B 中从 “The α-dependence...” 到 “analogous to μ...” 的核心论证段：

```markdown
The α-dependence of β is controlled by the same nonlocal kernel that governs the diagonal fractional diffusion problem, but it enters the off-diagonal sector through the midchain gradient source. We therefore do not treat β=a/α+b as an unconstrained empirical interpolation. The scaling statement is the following: in the hopping-dephasing window 0.5<=γ_phi<=2.0 and away from the fully nonlocal boundary-layer edge α=1.1, the leading coherence exponent is governed by the scaling variable 1/α,

β(α,γ_phi)=a(γ_phi)/α+b(γ_phi)+δβ_corr(α,γ_phi,L),

where δβ_corr is subleading in the leading scaling window and becomes visible in the weak-dephasing and α->1+ crossover windows. This form is fixed by two asymptotic constraints. First, as γ_phi->0 the NESS approaches the ballistic fixed point: the density gradient vanishes, the α-dependent amplitude collapses, and a(γ_phi)->0. Second, in the strong-dephasing/short-range limit the Robin boundary layer flows to the diffusive fixed point, so b(γ_phi)->1 and β loses its long-range enhancement. The role of the numerical fit is therefore not to discover an arbitrary curve, but to calibrate the two nonuniversal amplitudes a and b after the leading variable 1/α has been fixed by the fractional kernel and by these two fixed points.

Operationally, the claim is tested by collapse rather than by a five-point curve fit: after subtracting b(γ_phi) and rescaling by a(γ_phi), the data in the leading window collapse onto a straight line in 1/α, while the correction-dominated windows γ_phi=0.01, γ_phi=0.1, and α=1.1 show the expected deviations from the leading curve. Thus the evidence level is a constrained leading-scaling ansatz plus collapse test. The coefficients a(γ_phi), b(γ_phi) are calibrated, but the 1/α variable is not post hoc: it is selected by the fractional-Laplacian dispersion and by the ballistic and diffusive fixed-point limits.
```

## 3. 可粘贴进 Supplement S3 的 theorem/lemma 草案

替换 S3 标题和 S3.6-S3.7。把 “seven-step derivation / interpolation” 改成下面这个 theorem/lemma 结构。

```markdown
## S3. Leading scaling ansatz for β from two fixed points and collapse

**Lemma S3.1 (off-diagonal exponent reduces to the midchain-gradient exponent).**
In the dephasing-controlled regime where the first commutator expansion is asymptotically stable,

|C_mid|=(J0/γ_phi)|D_{L/2+1}-D_{L/2}| κ(L,α,γ_phi),

with κ(L,α,γ_phi)->1 as L increases. Therefore the leading exponent of |C_mid| equals the leading exponent ν of the midpoint occupation gradient. Corrections to κ contribute only to δβ_corr.

**Lemma S3.2 (fixed-point constraints).**
The fractional kernel

L_α(k)=-2 Σ_{r>=1}(1-cos kr)/r^{2α}

has two relevant asymptotic limits for the present exponent:

(i) Ballistic/dephasing-irrelevant fixed point, γ_phi->0: the steady-state gradient vanishes and the α-dependent amplitude must collapse, a(γ_phi)->0.

(ii) Diffusive/short-range fixed point, γ_phi large or α large: the nonlocal Robin layer flows to the ordinary diffusive boundary problem, giving β->1 and suppressing the long-range correction.

These limits constrain the leading exponent to the form

β(α,γ_phi)=b(γ_phi)+a(γ_phi) X(α)+δβ_corr,

where X(α) is the long-range scaling coordinate.

**Lemma S3.3 (choice of scaling coordinate).**
For power-law hopping h(r)~r^{-α}, the nonlocal dispersion and Robin boundary prefactor depend on α through inverse powers of the hopping decay exponent. On any compact interval away from the singular boundary-layer edge α=1, the leading long-range coordinate may be chosen as

X(α)=1/α,

with higher analytic corrections absorbed into δβ_corr = c1/α^2 + c2 L^{-ω(α,γ_phi)} + ... . Thus

β(α,γ_phi)=a(γ_phi)/α+b(γ_phi)+δβ_corr(α,γ_phi,L).

This is a leading scaling ansatz, not a claim of an exact closed-form theorem for the full thermodynamic exponent.

**Collapse test.**
The ansatz makes a falsifiable prediction independent of the raw two-parameter fit: in the leading scaling window,

Y(α,γ_phi) = [β(α,γ_phi)-b(γ_phi)]/a(γ_phi)

must collapse onto Y=1/α across γ_phi. The correction-dominated windows are not discarded; they must show controlled deviations with the expected signs:

- γ_phi->0: a(γ_phi)->0, so the collapse becomes ill-conditioned and β becomes nearly α-independent.
- α->1+: boundary-layer corrections grow and produce the largest L-drift.
- weak γ_phi: crossover corrections allow competing local fits, but should flow toward the same collapse as γ_phi increases.
```

## 4. 三个最小理论预测，交给数值 agent 检查

1. **Collapse prediction.** 在 `γ_phi=0.5,1.0,2.0` 且 `α=1.3,1.5,1.7,1.9` 上，计算 `Y=(β-b)/a`。`Y` 对 `1/α` 应近似落在同一直线 `Y=1/α`；`γ_phi=0.01` 不应 collapse，因为 `a->0`。

2. **Correction hierarchy prediction.** 去掉 `L=4` 或加入 `β_eff(Lmax)=β_inf+c L^{-ω}` 后，leading window 的 `1/α` 斜率应稳定；最大漂移必须出现在 `α=1.1` 和/或 `γ_phi=0.1`，不是随机出现在 `α=1.7,1.9`。

3. **Fixed-point flow prediction.** `a(γ_phi)` 必须在中等退相干附近有峰，并在 ballistic 与 strong-dephasing 极限下降；`b(γ_phi)` 必须向 diffusive baseline 上升。若新增 `γ_phi=0.25` 或 `γ_phi=3.0/5.0`，应分别落在从 weak-dephasing 流向 peak、从 peak 流向 diffusive baseline 的趋势上。

硬口径：如果数值只支持这三条，主张仍是 PRL 级别的 “second independent scaling exponent with 1/α leading scaling”。如果三条失败，才需要降级；现在不要主动降级。
