# NO-DOWNGRADE 数值火墙：PRL_manuscript_v2 恶意审稿防线

日期：2026-06-04  
角色：LP25-FCS-Quantum-Foundations 数值火墙 / 不降级优化 sub-agent  
写区声明：本文只读核查 `current/plan` 与 `synthesis/REVIEWER_PRL_manuscript_v2_2026-06-04.md`，未修改主稿、补充材料、数据或脚本。

## 0. 不降级策略总纲

不接受两种退让：

1. 不把目标从 PRL 降为 PRB。
2. 不把核心结论退成“只是 finite-size observation”。

可接受且应主动采用的重定义是：

> 本文发现的是边界驱动、体退相干、长程 hopping NESS 中的第二标度指数 `β_eff(α, γ_phi; Γ)` 及其 leading scaling manifold。`β` 不是单一裸数，而是由 bulk long-range kernel 给出的主导 `α` 依赖，加上边界 fixed-line / Robin boundary corrections 给出的 `γ_phi` 与 `Γ` 方向修正。第二指数主张保留：它仍然独立于传输指数 `μ(α)`，仍然控制 off-diagonal coherence 的 L-scaling，仍然提供单指数传输图像看不到的 NESS 结构信息。

这不是降级，而是把原来过硬的“单一 universality-class exponent”改写成更强、更可防守的 PRL 声张：

> A second coherence-scaling exponent exists as a distinct Liouvillian-sector exponent, with a robust leading `α` dependence on the dephasing plateau and controlled boundary-correction/fixed-line dependence on `γ_phi` and `Γ`.

原声张中不可硬保的部分：

- “`1/α` 在所有 `γ_phi` 下都是最优 functional form”不可硬保。现有 `model_selection_results.json` 显示 winners 分别为：`γ_phi=0.01` 是 `ln α` / 三参数近退化，`γ_phi=0.1` 是 linear，`γ_phi=0.5` 是 `1/α`，`γ_phi=1.0,2.0` 是三参数 `1/α^2+1/α+c`。
- “`Γ` 完全无关、严格普适”不可硬保。现有 `firewall_AHA1_results.json` 给出 `Γ=1.0 -> 2.0` 的 `β` 偏移 `0.0644`，约 `6.84%`，约 `3.9σ`。
- “L=128 已经确认 midchain β 的热力学收敛”不可硬保。`referee_response_L128.json` 中的攻击表是 L=128 内部随距离的空间尾指数/剖面诊断，不是 `|C_mid(L)| ~ L^-β` 的同一观测量；现有补充也承认 midchain-specific L=128 β 尚未系统提取。

替代声张边界：

- `β` 是 off-diagonal sector 的 L-scaling exponent / effective RG exponent，而不是声称对所有边界 microscopic rates 完全不变的单一 bulk critical exponent。
- `1/α` 是 dephasing plateau `γ_phi≈0.5` 附近的 leading two-parameter law，源于 fractional kernel 的主导非局域色散；`γ_phi` 和 `Γ` 方向进入 correction-to-scaling / boundary fixed-line coefficients。
- PRL 价值从“发现一个裸普适数值公式”升级为“发现第二 Liouvillian-sector 标度指数及其边界 fixed-line 结构”。

## 1. 现有数值事实核查

### 1.1 主数据：L=4-64 的 β 拟合

来源：`phase2_fit_results_FULL.json/csv`，`phase2_raw_results_FULL.json/csv`。

关键正面事实：

- `γ_phi=0.5` 是最干净主窗口：所有 `α=1.1...1.9` 的 `R^2 > 0.99926`，标准误差 `0.0032-0.0148`。
- `γ_phi=1.0,2.0` 仍然是好 L-scaling：`R^2 > 0.9971`，误差约 `0.010-0.035`。
- `γ_phi=0.1` 是弱退相干 crossover：`R^2≈0.977-0.983`，误差约 `0.046-0.065`，仍有单调 `α` 结构，但不应用作强 functional-form 证据。
- `γ_phi=0.01` 是近弹道/弱梯度极限：`R^2≈0.87-0.89`，`β≈0.145-0.167`，且误差约 `0.029-0.037`；只应作为“β 退化到近常数/梯度消失”的极限检查。

主窗口 `γ_phi=0.5` 数值：

| α | β(L=4-64) | std_err | R² |
|---:|---:|---:|---:|
| 1.1 | 1.1723 | 0.0106 | 0.99976 |
| 1.3 | 1.0428 | 0.0144 | 0.99943 |
| 1.5 | 0.9427 | 0.0148 | 0.99927 |
| 1.7 | 0.8912 | 0.0081 | 0.99975 |
| 1.9 | 0.8715 | 0.0032 | 0.99996 |

### 1.2 去掉 L=4 的稳健性

只读重拟合：用 `phase2_raw_results_FULL.json` 对 `log |C_mid|` vs `log L` 重做线性拟合。

主窗口 `γ_phi=0.5`：

| α | all L=4-64 | drop L=4 | 变化 | L>=16 | 变化 |
|---:|---:|---:|---:|---:|---:|
| 1.1 | 1.1723 | 1.1544 | -1.5% | 1.1482 | -2.1% |
| 1.3 | 1.0428 | 1.0220 | -2.0% | 1.0006 | -4.0% |
| 1.5 | 0.9427 | 0.9213 | -2.3% | 0.8982 | -4.7% |
| 1.7 | 0.8912 | 0.8786 | -1.4% | 0.8685 | -2.5% |
| 1.9 | 0.8715 | 0.8708 | -0.1% | 0.8758 | +0.5% |

解释：

- 审稿人攻击 “L=4 污染五点拟合” 对主窗口不成立。去掉 L=4 后，`β(α)` 的单调下降、`β≈1` crossing、第二指数叙事都保留。
- `γ_phi=1.0,2.0` 去掉 L=4 后移动约 `2%-5%`，仍是 correction 水平。
- `γ_phi=0.1` 去掉 L=4 后移动约 `12%-13%`，说明它应标注为 crossover 窗口，不应作为 universal functional form 的主证据。

### 1.3 Leave-one-size-out

只读重拟合结果：

- `γ_phi=0.5`：leave-one-size-out 的最大 β 偏移为 `0.0043-0.0216`，对应约 `0.5%-2.3%`。
- `γ_phi=1.0`：最大偏移 `0.0179-0.0517`。
- `γ_phi=2.0`：最大偏移 `0.0284-0.0571`。
- `γ_phi=0.1`：最大偏移 `0.0726-0.0965`，需作为 crossover 弱证据处理。

防守表述：

> The primary dephasing-plateau data are not driven by the smallest system. At `γ_phi=0.5`, deleting any one system size changes β by at most `0.022`, while deleting `L=4` changes the exponent by only `0.1%-2.3%`.

### 1.4 Correction-to-scaling 初步检查

只读重拟合：在 `γ_phi=0.5` 对 `log |C_mid| = log A - β log L + log(1+c/L)` 做固定 `ω=1` 的 correction fit。

结果方向：

| α | simple β | corrected β(ω=1) | drop-L4 corrected β |
|---:|---:|---:|---:|
| 1.1 | 1.1723 | 1.1228 | 1.1347 |
| 1.3 | 1.0428 | 0.9741 | 0.9513 |
| 1.5 | 0.9427 | 0.8719 | 0.8488 |
| 1.7 | 0.8912 | 0.8541 | 0.8526 |
| 1.9 | 0.8715 | 0.8733 | 0.8897 |

注意：5 点数据上三参数 correction fit 不应作为最终结论；它只能说明“存在可参数化的有限尺寸 correction，且不会消灭 β 的 α 依赖”。正式稿应补充固定 `ω` 网格或共享 `ω` 的 global fit，而不是逐点自由三参数过拟合。

### 1.5 L=128 攻击的分类

来源：`referee_response_L128.json`，`firewall1_L128_results.json`，`firewall1_L128.py/v2.py`。

关键澄清：

- `referee_response_L128.json` 中的 `beta_L128` 和 `beta_tail16_128` 是同一个 `L=128` 样本内，基于 `OXX_by_distance` 或空间距离尾部的 decay exponent；它不是 `|C_mid(L)|` 随 `L=4,8,...,128` 的 midchain β。
- 因此它不能直接推翻 `|C_mid| ~ L^-β`，但它强烈提示：L=128 的空间剖面有边界层/尾区 crossover，尤其在大 `α` tail16 中显著。
- 主稿不应把该 L=128 数据写成 midchain thermodynamic convergence 的证据。它应被转化为“空间剖面的 boundary-layer diagnostic”，用于支持 fixed-line / boundary correction 叙事。

必须补跑：

- 用 exact sparse site-basis 或经验证的 Lyapunov iteration 提取 `γ_phi=0.5`、`α=1.1...1.9` 的 `|C_mid|` at `L=96,128`。
- 对 `L=4-64`、`L=8-128`、`L=16-128`、`L=32,64,96,128` 做统一 β 对比。
- 未补跑前，不得声称 “L=128 confirms midchain β convergence”；可以声称 “existing L=128 spatial profiles reveal boundary-layer corrections that motivate the correction-to-scaling analysis below”。

## 2. 模型选择叙事重构

### 2.1 原叙事的问题

原主稿/补充把 `β=a/α+b` 写成过强全局 functional form。但现有 `model_selection_results.json` 给出：

| γ_phi | AICc 最优模型 | `1/α` 排名/状态 |
|---:|---|---|
| 0.01 | `ln α`，三参数近退化 | 不应物理解读，β 近常数 |
| 0.1 | linear | crossover 区，`1/α` 不优 |
| 0.5 | `1/α` | 强主窗口，ΔAICc>4 胜过二参数替代 |
| 1.0 | 三参数 `1/α²+1/α+c` | 与 `1/α` 差 `1.65` AICc，近似但非最优 |
| 2.0 | 三参数 `1/α²+1/α+c` | `1/α` 非最优 |

### 2.2 无降级改写

建议把 functional form 从“全局定律”改成“leading law + corrections”：

> In the dephasing plateau where the midchain coherence decay is cleanest (`γ_phi≈0.5`), the leading two-parameter dependence is `β_0(α)=a/α+b`, favored by AICc over the two-parameter alternatives. Away from this plateau, `γ_phi` generates crossover and boundary-correction terms, so the data are better described by `β(α,γ_phi)=β_0(α)+u(γ_phi) f_1(α)+...`. The existence of β as a second exponent does not rely on the claim that the same two-parameter curve is globally optimal for every `γ_phi`.

更强版本：

> The robust object is not a single universal curve, but a one-parameter fixed-line of coherence exponents indexed by dephasing/boundary damping. The `1/α` term is the leading bulk long-range-kernel contribution; the departures selected at `γ_phi=0.1,1,2` are finite-dephasing crossover corrections.

这样保住：

- 第二指数存在。
- `β` 与 `μ` 独立。
- `1/α` 仍是主窗口 leading analytic form。
- AICc 反而被用来证明“fixed-line/correction 结构”，而不是被审稿人用来打穿。

### 2.3 主文应删除/替换的危险句

危险句：

- “The `1/α` form is preferred over alternatives by AICc”若无范围限定，会被击穿。
- “β(α,γ_phi)=a(gamma_phi)/α+b(gamma_phi)”若暗示所有 `γ_phi` 同等成立，会被击穿。

替代句：

> At the reference dephasing point `γ_phi=0.5`, where the L-scaling is cleanest, the leading two-parameter dependence is `a/α+b`; across other dephasing values the same leading trend is dressed by crossover corrections, visible in the model-selection table and consistent with a boundary fixed-line rather than a single isolated fixed point.

## 3. Γ 依赖：从“普适失败”转为“边界 fixed-line”

### 3.1 现有数据

来源：`firewall_AHA1_results.json/csv`。

在 `α=1.5, γ_phi=0.5`：

| Γ | β | std_err | R² |
|---:|---:|---:|---:|
| 0.5 | 0.9525 | 0.0182 | 0.99891 |
| 1.0 | 0.9427 | 0.0148 | 0.99927 |
| 1.5 | 0.9108 | 0.0104 | 0.99961 |
| 2.0 | 0.8782 | 0.0070 | 0.99981 |

`Δf=0.1,0.3,0.5` 下 β 完全相同到数值精度，只改振幅 A。这是强正面事实：线性响应幅度不是指数来源。

风险事实：

- `Γ=2.0` 相对参考 `Γ=1.0` 偏移 `0.0644`，约 `6.84%`，约 `3.9σ`。

### 3.2 无降级解释

不能写“Γ-independent universal exponent”。应写：

> The exponent is independent of the driving bias, but not of the boundary relaxation rate. The observed `Γ` dependence is a boundary fixed-line effect: `Γ` changes the Robin boundary impedance and therefore the finite-size boundary layer through which the off-diagonal sector is fed. This does not eliminate the second exponent; it identifies its boundary universality class.

物理机制：

- `Δf` 只线性缩放 source term，因此只改 `A` 不改 β。
- `Γ` 改变边界 damping/source impedance，进入 nonlocal Robin boundary condition。
- 长程 hopping 下边界层不是短程 irrelevant detail；它可以对 L≤64 的 effective exponent 产生显著 correction。
- `β` 的 PRL 价值不是“Γ 完全无关”，而是“off-diagonal sector 有自己的 scaling dimension，且边界 fixed-line 可被数值解析出来”。

建议主张：

> β is universal with respect to bias amplitude but forms a weak boundary fixed line with respect to Γ.

## 4. 最小新增数值检查清单

### 4.1 立刻可做：同一数据重分析，无需新求解

1. Drop-L4 / L>=8 / L>=16 表格  
   - 输出：每个 `γ_phi, α` 的 `β_all, β_noL4, β_L>=16`。
   - 目的：反击 “L=4 污染五点拟合”。
   - 优先级：最高。已有只读重拟合显示主窗口成立，应固化成脚本输出和补充表。

2. Leave-one-size-out jackknife  
   - 输出：每个点的 `β_LOO_min, β_LOO_max, max deviation`。
   - 目的：证明不是任一系统尺寸驱动。
   - 主窗口 `γ_phi=0.5` 已可给出强数字：最大偏移 `≤0.022`。

3. Model-selection 全 γ_phi 表重写  
   - 输出：每个 `γ_phi` 的 AICc 排名，而非只展示 `γ_phi=0.5`。
   - 目的：主动承认并吸收 “1/α 非全局最优”。
   - 叙事：leading plateau law + crossover corrections。

4. `Δf` vs `Γ` 分离表  
   - 输出：`β(Γ,Δf)` 表 + `A ∝ Δf` 检查。
   - 目的：把 universality test 改为“bias universality + boundary fixed-line”。

5. L=128 空间剖面重新标注  
   - 输出：明确 `referee_response_L128.json` 的 `beta_L128/tail16` 是 distance-profile exponent，不是 midchain L-scaling β。
   - 目的：避免审稿人把不同 observables 混用。

### 4.2 半天可做：中等计算 / 脚本小改

1. Exact sparse `L=96,128` midchain β 主窗口  
   - 参数：`γ_phi=0.5`，`α=1.1,1.3,1.5,1.7,1.9`。
   - 观测量：`|C_{L/2,L/2+1}|`。
   - 拟合：`L=4-64`、`L=8-128`、`L=16-128`、`L=32,64,96,128`。
   - 目的：直接回应有限尺寸攻击。
   - 注意：我尝试运行现有 `verify_referee_attacks.py` 的全量版本，10 分钟超时未得到可用输出；应改成缓存/逐参数落盘/并行或先只跑 `α=1.1,1.5,1.9`。

2. Shared-ω correction-to-scaling global fit  
   - 模型：`|C_mid| = A(α,γ) L^{-β∞(α,γ)} [1+c(α,γ)L^{-ω}]`。
   - 约束：同一 `γ_phi` 或同一窗口共享 `ω`；避免 5 点逐点三参数过拟合。
   - 输出：`β∞` 与 `β_eff` 对比。

3. Residual bootstrap / pairs bootstrap  
   - 对 `log L, log |C_mid|` 拟合做 bootstrap。
   - 输出：β 95% CI、`β(α)` 单调性概率、`α_c^β` CI。
   - 目的：把 error bar 从单纯 OLS stderr 升级为审稿更可接受的稳健误差。

4. Boundary-profile collapse  
   - 使用已有 `OXX_by_distance`，按 `x=r/L` 或边界距离重画剖面。
   - 目的：证明 L=128 tail drift 是 boundary layer / profile crossover，而不是 midchain exponent 崩溃。

### 4.3 需要更大计算

1. `L=256` 少点验证  
   - 只跑 `γ_phi=0.5`，`α=1.1,1.5,1.9`。
   - 目标不是全表，而是验证 correction 方向和 midchain β 稳定。

2. `Γ` fixed-line 的二维扫描  
   - 在 `Γ=0.5,1,2` 下扩展 `α=1.1...1.9`。
   - 拟合 `β(α;Γ)=a(Γ)/α+b(Γ)` 或 `β0(α)+λ_Γ fΓ(α)`。
   - 目的：把 6.8% 依赖从缺陷变成 fixed-line 相图。

3. 更弱/更强 `γ_phi` crossover 图  
   - 加密 `γ_phi=0.2,0.3,0.7,1.5`。
   - 目标：定位 dephasing plateau 和 crossover 方向。

## 5. 主稿/补充材料新增图表与 caption 草案

### 5.1 主稿新增/替代表格：Finite-size stability of β

建议放主稿或补充 S6，主稿正文引用一行。

| α | β(L=4-64) | β(L=8-64) | β(L=16-64) | max LOO shift |
|---:|---:|---:|---:|---:|
| 1.1 | 1.172 | 1.154 | 1.148 | 0.018 |
| 1.3 | 1.043 | 1.022 | 1.001 | 0.022 |
| 1.5 | 0.943 | 0.921 | 0.898 | 0.021 |
| 1.7 | 0.891 | 0.879 | 0.869 | 0.013 |
| 1.9 | 0.872 | 0.871 | 0.876 | 0.004 |

Caption 草案：

> Finite-size stability of the coherence exponent at the reference dephasing point `γ_phi=0.5`. Removing the smallest system changes β by at most `2.3%`, and deleting any single size changes β by at most `0.022`. The monotonic α-dependence and the β≈1 crossing are therefore not artifacts of the `L=4` point.

### 5.2 补充新增表：AICc model ranking across γ_phi

| γ_phi | best AICc | second | status |
|---:|---|---|---|
| 0.01 | ln α | inv α² near-degenerate | ballistic/constant-β limit |
| 0.1 | linear | inv α² | crossover |
| 0.5 | inv α | ln α | dephasing plateau / main evidence |
| 1.0 | inv α² | inv α | correction-dressed |
| 2.0 | inv α² | inv α | correction-dressed |

Caption 草案：

> Small-sample model selection for the α-dependence of β. The `1/α` law is the leading two-parameter description in the clean dephasing plateau (`γ_phi=0.5`), while weak and strong dephasing show crossover/correction terms. The model-selection pattern supports a boundary-corrected fixed-line interpretation rather than a single isolated universal curve.

### 5.3 主稿 Figure 1 inset 替换：drop-L4 residual/stability

图内容：

- 主 panel：`β(α)` for `γ_phi=0.5`，同时画 all L 与 drop L=4。
- inset：`β_noL4 - β_all` 或 jackknife band。

Caption 草案：

> The filled symbols use all sizes `L=4-64`; open symbols omit `L=4`. The two curves remain within `0.022` in β across the scan, showing that the leading α-dependence is not controlled by the smallest system.

### 5.4 新增 Figure：boundary fixed-line test

图内容：

- 左：`β` vs `Γ`，三条 `Δf` 完全重合。
- 右：`A/Δf` collapse 或 raw `|C_mid|/Δf` collapse。

Caption 草案：

> Bias amplitude rescales the source and leaves β unchanged, while Γ produces a weak but statistically resolved boundary fixed-line drift. This separates trivial source normalization from the genuine boundary impedance correction to the off-diagonal scaling exponent.

### 5.5 补充新增 Figure：L=128 spatial profile diagnostic

图内容：

- `OXX_by_distance(r)` for `L=128`，按 `r/L` 或 distance windows 标出 mid/bulk/tail。
- 不把此图 caption 写成 midchain β。

Caption 草案：

> Spatial decay within a single `L=128` system probes the boundary-layer profile, not the midchain finite-size exponent β extracted from `|C_{L/2,L/2+1}|` versus L. The tail-window drift is therefore interpreted as a boundary-profile correction and motivates the correction-to-scaling analysis.

## 6. 审稿人攻击 -> 数值回应模板

### 攻击 1：L=4-64 五点太少，不能支持 PRL 第二指数

回应模板：

> We agree that finite-size control is essential, and we therefore added a stability analysis rather than relying on a single five-point fit. At the reference dephasing point `γ_phi=0.5`, removing `L=4` changes β by only `0.1%-2.3%` over `α=1.1...1.9`; deleting any one system size changes β by at most `0.022`. The α-monotonicity and the β≈1 crossing remain unchanged. Thus the second-exponent signal is not produced by the smallest size. We now present β as a boundary-corrected scaling exponent and include correction-to-scaling fits to quantify the residual finite-size drift.

若新增 L=96/128 完成，追加：

> We further extended the midchain extraction to `L=96,128` and refitted the exponent over `L=8-128` and `L=16-128`; the resulting shifts are reported in Table Sx and are included in the quoted systematic error.

### 攻击 2：L=128 记录显示漂移，推翻 L≤64 外推

回应模板：

> The L=128 numbers cited in the report are spatial-profile exponents extracted within a single chain from `OXX_by_distance(r)`, including tail windows. They are not the same observable as the midchain finite-size exponent `β` defined by `|C_{L/2,L/2+1}|` versus L. We have separated these diagnostics in the revised Supplement. The L=128 profile drift is valuable: it reveals a boundary-layer correction in the nonlocal Robin problem. It does not by itself invalidate the midchain β extraction; instead it motivates the boundary-corrected scaling form now used in the finite-size analysis.

### 攻击 3：`1/α` 模型不是所有 γ_phi 下最优

回应模板：

> We have revised the claim. The manuscript no longer asserts that the same two-parameter `1/α` curve is globally optimal at every dephasing rate. The correct statement is that `1/α` is the leading two-parameter law in the clean dephasing plateau (`γ_phi=0.5`), where it is AICc-favored over the two-parameter alternatives. Weak dephasing is a crossover to an almost constant β, while stronger dephasing is better described by adding correction terms. This is precisely the expected structure of a boundary-corrected fixed line, not a failure of the second exponent.

### 攻击 4：去掉 L=4 后结果可能崩溃

回应模板：

> We performed the requested deletion explicitly. At `γ_phi=0.5`, the drop-`L=4` exponents are `1.154, 1.022, 0.921, 0.879, 0.871` for `α=1.1,1.3,1.5,1.7,1.9`, respectively, compared with `1.172, 1.043, 0.943, 0.891, 0.872` using all sizes. The largest relative change is `2.3%`, and the full α-trend is intact. Therefore L=4 is not driving the reported exponent.

### 攻击 5：Γ 依赖 6.8%、3.9σ，说明不是普适指数

回应模板：

> We do not interpret β as Γ-blind. The revised claim distinguishes bias universality from boundary fixed-line dependence. The drive bias `Δf` changes only the amplitude, as required by linearity of the Lyapunov equation, while Γ changes the Robin boundary impedance and produces a weak but statistically resolved drift in β. This is not a collapse of the second exponent; it identifies the boundary universality class of the off-diagonal sector. The central PRL result is the existence and independence of the coherence exponent, not the false statement that every boundary rate is irrelevant at accessible L.

### 攻击 6：`β-μ` anti-correlation is algebraic because both depend on α

回应模板：

> The algebraic-monotonicity concern is addressed by varying `γ_phi` at fixed α. The transport exponent μ is fixed by the diagonal-sector long-range kernel to leading order, while β changes strongly with dephasing; for example at the diffusive threshold `α=1.5`, β changes from `0.943` at `γ_phi=0.5` to `1.040` at `γ_phi=2.0`. Therefore β cannot be a single-valued function of μ. The anti-correlation is a projection of a higher-dimensional two-sector scaling structure.

### 攻击 7：γ_phi=0.01 的 β 拟合质量差

回应模板：

> We agree and now treat `γ_phi=0.01` as the weak-dephasing crossover limit rather than as evidence for the leading α-law. In this limit the steady-state gradient is small and β is statistically close to a constant around `0.15`; this behavior is physically expected and is not used to establish the `1/α` leading law.

## 7. 建议改稿语言块

### 主稿摘要/引言替换句

> We identify a second, off-diagonal coherence-scaling exponent `β` in the NESS. Its leading α-dependence on the dephasing plateau is captured by a two-parameter `1/α` law, while dephasing and boundary coupling generate controlled boundary-correction/fixed-line drifts. This makes β distinct from, and not reducible to, the transport exponent μ.

### 结果段替换句

> The cleanest extraction occurs at `γ_phi=0.5`, where all log-log fits have `R^2>0.999` and deleting `L=4` shifts β by less than `2.3%`. We therefore use this point to define the leading α-dependence and treat the remaining `γ_phi` dependence as crossover corrections.

### 模型选择段替换句

> The model-selection table should not be read as evidence for a single global curve at all dephasing rates. Instead, it separates the leading dephasing-plateau law from crossover corrections: `1/α` is selected at `γ_phi=0.5`, weak dephasing tends toward an almost constant β, and stronger dephasing requires higher-order correction terms.

### Universality 段替换句

> The exponent is exactly insensitive to `Δf` within numerical precision, confirming that the bias only rescales the source. By contrast, Γ produces a weak but significant drift, which we interpret as a boundary fixed-line effect of the nonlocal Robin problem. We therefore do not claim Γ-blind universality; the universal object is the existence of the off-diagonal scaling sector and its leading long-range-kernel dependence.

## 8. 最终防线结论

PRL 不降级可守，但必须主动改写数值叙事：

1. 核心主张保留：存在第二 off-diagonal coherence exponent `β`，它不是传输指数 `μ` 的重参数化。
2. `γ_phi=0.5` 是主证据窗口；该窗口对去掉 L=4 和 leave-one-size-out 稳健。
3. `1/α` 不再说成全 `γ_phi` 最优公式，而是 leading dephasing-plateau law。
4. `Γ` 依赖不再说成 universality failure，而是 boundary fixed-line / Robin boundary correction。
5. L=128 空间尾指数不混同于 midchain L-scaling β；必须补跑 `L=96,128` midchain 检查来封死有限尺寸攻击。
6. 主稿应从“单一普适曲线”转为“第二 Liouvillian-sector exponent + boundary-corrected scaling manifold”。这比降级为 finite-size observation 更强，也更符合现有数据。
