# Phase 1：Pf/APf 域壁渗流的定量门槛

**日期：** 2026-06-01
**状态：** 完成
**目标：** 判断域壁 Majorana 网络是否有现实参数窗口可产生 `K=5/2`。

---

## 1. 最小物理模型

把样品看成由局域 Pf 与 APf puddles 组成。局域相由随机 PH-breaking bias `m(r)` 决定：

```text
m(r) > 0  -> Pf
m(r) < 0  -> APf
m(r) = 0  -> Pf/APf domain wall
```

域壁上有 4 个同向 chiral Majorana 模，总中心荷差 `c_- = 2`。相邻域壁靠近时，Majorana 模通过 junction scattering 矩阵耦合。宏观相由三个条件决定：

```text
C1: domain walls can be energetically nucleated
C2: domain walls percolate across the sample
C3: neutral Majorana network localizes into K=5/2 rather than delocalizes into thermal metal
```

S3 的关键不是“域壁是否可能存在”，而是 `C1+C2+C3` 是否在 GaAs 实验窗口同时成立。

---

## 2. 条件 C1：域壁生成门槛

Zhu-Sheng-Yang DMRG 给出 Pf/APf 界面张力：

```text
sigma_DW ~ (1.7-2.1)e-3 e^2/l_B^2
```

界面具有拓扑来源的 electric dipole density，由 guiding-center Hall viscosity mismatch 决定。无序电场可钉扎/稳定域壁，条件为：

```text
E_dis >= sigma_DW / (Delta p_x / L_y)
```

文献估计：

```text
E_dis^crit ~ 2.9e5 V/m
```

高迁移率 GaAs/GaAlAs 远程掺杂层距离约 `d ~ 100 nm`，裸局域电场量级与 `E_dis^crit` 同阶。但这一步不能直接等同于作用在 Pf/APf bias 上的有效电场：2DEG screening、有限量子阱厚度、LL projection 和 disorder form factor 都会重整该分量。因此这里的正确结论只能写成“门槛附近的可能性”，不能写成已定量命中。

**L2-1：域壁生成在实验 GaAs 参数下不是显然不可能；裸估计提示它可能处在门槛附近。但有效 Pf/APf bias 需要 screening/form-factor 修正后才能定量判定。**

边界：
- 若有效 disorder field 低于该门槛，域壁网络退化为直接 Pf/APf 切换。
- 若有效 disorder field 远高于该门槛，则进入 class-D thermal metal 风险区。
- 当前文本只使用裸量级比较，不能替代自洽 electrostatics + LL projection 计算。

---

## 3. 条件 C2：域壁网络渗流门槛

随机场模型中，Pf/APf 面积分数接近 1/2 时，域壁网络接近临界渗流。必要条件：

```text
|<m>| / rms(m) <= O(1)
```

也就是平均 PH-breaking bias 不能远大于无序涨落。若 Landau-level mixing 给出强全局 APf 偏置，则 APf percolates，域壁不形成中间相。

Wang-Vishwanath-Halperin 的相图说明：

- 弱无序/大 domain：直接一阶样 Pf <-> APf。
- 中等无序：可能出现 PH-Pf thermal insulator。
- 强无序：更可能出现 quantized Hall thermal metal。

**L2-2：S3 的可行窗口是窄的“中等无序”窗口，不是无序越强越好。**

---

## 4. 条件 C3：Majorana 网络必须局域化

class-D Majorana 网络在二维中可有局域相，也可有 thermal metal。`K=5/2` 要求：

```text
kappa_xx -> 0
K = 5/2 quantized
```

而 thermal metal 给出：

```text
kappa_xx > 0
K non-universal / continuously varying
```

Wang-Vishwanath-Halperin 的核心警告是：random vortices / random π flux 很容易产生 finite density Majorana zero modes，推动 delocalization。

稳定 `K=5/2` 需要更强的结构性约束：

```text
eta_intra large enough to split local zero modes
eta_inter small enough to avoid delocalized hopping
rho_vortex low or vortices paired
emergent U(1)xU(1) or SO(4) symmetry approximately valid
```

Lian-Wang 把这写成 disorder energy scale `Lambda` 的阈值图：

```text
Lambda < Lambda1       -> direct Pf/APf transition
Lambda1 < Lambda < Lambda2 -> K=5/2 window possible
Lambda > Lambda2       -> four transitions or thermal metal
```

**L2-3：域壁机制的最大风险不是域壁能否形成，而是形成后是否不可避免地进入 thermal metal。**

---

## 5. 与 S1/S2 的合并判断

S1 已经说明纯 APf 边缘机制有 tradeoff：压低分数通道会同时压低总 `kappa_xy`。

S2 已经说明 bulk APf 与 edge PHPf-like 信号可以原则上共存。

S3 当前 Phase 1 给出的新增判断是：

```text
domain-wall mechanism can solve S1 tradeoff only if it enters a localized K=5/2 thermal insulator, not if it enters thermal metal.
```

因此 `K=5/2` 的域壁解释需要同时满足：

```text
E_dis ~ E_dis^crit
|<m>|/rms(m) <= O(1)
Lambda1 < Lambda < Lambda2
rho_vortex not too high
kappa_xx experimentally negligible
```

这是一组窄窗条件。

---

## 6. 首轮判定

**结论类型：有边界，尚未收官。**

Pf/APf 域壁 Majorana 渗流是原则上可行的第三路径，但它不是一个自动解释。现有文献给出两面约束：

- 支持侧：界面张力与 GaAs 无序电场同阶；域壁 strong hybridization 与 charged-mode gapping 有 DMRG 支持；`K=5/2` 相在网络模型中存在。
- 反对侧：`K=5/2` 位于受限参数区；random vortices 倾向 thermal metal；强无序并不增强量子化 plateau，反而可能破坏它。

**Phase 2 必须做的事：** 把上述条件转成二维随机场 + class-D 网络代理模拟，扫描 `(bias/rms, xi_dis/d_DW, rho_vortex, eta_inter/eta_intra)`，判断 GaAs 是否自然落在 `K=5/2` 窄窗，而非 thermal metal。

---

## SOP-4 四问

### Q1：最意外发现是什么？

域壁生成本身未必是最硬的障碍。Zhu-Sheng-Yang 的张力估计和 GaAs 掺杂无序裸电场同阶，说明“形成 Pf/APf domain wall”不是荒唐假设；但有效 bias 仍需 screening 和 LL projection 修正。真正硬的是 Majorana 网络的局域化。

### Q2：现在最不确定的一件事是什么？

random vortex / π-flux 的有效密度。它决定 network 是 `K=5/2` thermal insulator 还是 class-D thermal metal，但现有实验参数没有直接给出这个量。

### Q3：有没有算出来但解释不了的结果？

有：Lian-Wang 的 emergent symmetry 阈值 `Lambda1, Lambda2` 是理论相图的关键，但它们如何从 GaAs 的 disorder correlation length、domain wall tension 和 quasiparticle density 定量换算，仍没有闭式公式。

### Q4：如果本 Phase 结论错了，最可能错在哪里？

把掺杂无序电场量级与域壁稳定电场门槛直接比较可能过粗。真实无序势经过 2DEG screening、有限厚度、LL projection 后，作用在 Pf/APf bias 上的有效分量可能小一个数量级，也可能局域增强。

---

## 卡点登记

### 卡点 #1：`Lambda` 与实验参数的映射

- 位置：Lian-Wang 相图中的 `Lambda1, Lambda2`。
- 问题：`Lambda` 是域壁网络能量尺度/无序尺度，不等同于迁移率散射率。
- 状态：Phase 2 通过代理参数扫描绕过。

### 卡点 #2：random vortex 密度

- 位置：class-D thermal metal 风险判据。
- 问题：真实样品中 e/4 quasiparticle/vortex 的空间分布缺乏直接测量。
- 状态：Phase 2 作为独立扫描轴。
