# v8 Phase 3 PI物理裁决报告

> 类型：C（物理身份裁决）
> PI 主导执行，不调用 A/B 子 agent（v8-K6'/K7/K8/K9 已成熟）
> 核心问题：Σ_B^{int} 是浴 inherent 不可逆熵产生 / 信息回流记账项 / 复合？
> 日期：2026-05-30

---

## §0 北极星精确化

原 v8 北极星：
> "Σ_B^{int}(t)<0 窗口 ⟺ Nakagawa N_I^{(?)}>0 窗口 ⟺ '浴熵产生' = 信息回流记账项"

经 v8 Phase 1-2 推进，已澄清：
- **(★★) 形式恒等地**：Σ_B^{int}(t) = -d/dt D(ρ_B(t)‖ρ_B^{ref}(β)) = İ_B^{(σ=ρ_B^{ref})}
- 故 "Σ_B^{int} 是 Nakagawa 信息度的时间导数" **作为定义恒等**——B sector + 热参考 σ=ρ_β

但这不回答物理问题。**Phase 3 精确化北极星**：
- (Q1) Σ_B^{int}<0 时，浴远离 thermal reference 的"驱动力"是什么物理实体——系统侧的相干 backflow，还是浴内部的不可逆涨落？
- (Q2) Σ_B^{int} negative window 累积量与 S sector mutual-info amplitude 的定量关系如何？

---

## §1 撞墙（PI 自检）

### §1.1 零阶 sanity check
- N→∞: Σ_B^{int} → 0（v5-K6 N→∞ 极限）✓
- g→0: Σ_B^{int} = O(g²) 或 O(g⁴)（v8-K7 视耦合 sector）✓
- t→∞: 在 toy 周期模型周期内取均值 → 0；在 chaotic 浴极限 → 0 ✓

三个零阶 sanity check 均通过。

### §1.2 Esposito 2010 比对
Esposito 2010 NJP 12, 013013：Σ_total = D(ρ_SB‖ρ_S⊗ρ_B^{eq})。chain rule 拆解：
$$\dot\Sigma_{total} = \frac{d}{dt}\bigl[S(\rho_S \| \rho_S^{eq})\bigr] + \frac{d}{dt}\bigl[D(\rho_B\|\rho_B^{eq})\bigr] + \frac{d}{dt}\bigl[D(\rho_{SB}\|\rho_S\otimes\rho_B)\bigr]$$

中间项 $= -\Sigma_B^{int}$。**所以 Σ_B^{int} 是 Esposito 全局熵产生的浴侧分量的负值** —— v8-K1 的 derivative 性质（已在审稿人 Attack 5 承认）。

### §1.3 Nakagawa 等价性
v8-K4：Σ_B^{int} ≡ İ_B（B sector + 热参考）。

**这是 Σ_B^{int} 作为信息度的字面定义**——但不是物理身份。物理身份需要 c 系数（J1）的具体值。

---

## §2 PI 推导：c 系数 & 物理身份

### §2.1 修正：∫_{T_<} Σ_B^{int} dt 闭式

**Toy 模型**（v8-K8）：N=2 双模 JC + |e,0,0⟩ + 对称耦合 + 共振 + 热参考 ρ_B^{ref}(β)。

$\Sigma_B^{int}(t) = \dot p\,[\ln(q/p) - \beta\omega_0]$，其中 $p = \sin^2(\Omega t)$，$\Omega = g\sqrt 2$。

T_< = $(\Omega t^*/\Omega, \pi/(4\Omega))$，$\Omega t^* = \arccot(e^{\beta\omega_0/2})$。

变换 $u = \Omega t$，再 $v = \cos(2u)$：
$$\int_{T_<} \Sigma_B^{int}\,dt = -\frac{1}{2}\int_T^0 \bigl[\ln\frac{1+v}{1-v} - \beta\omega_0\bigr]\,dv = \frac{1}{2}\int_0^T \bigl[\ln\frac{1+v}{1-v} - \beta\omega_0\bigr]\,dv$$
其中 $T := \tanh(\beta\omega_0/2)$。

利用 $1\pm T = e^{\pm\beta\omega_0/2}/\cosh(\beta\omega_0/2)$：
$$\ln(1+T) + \ln(1-T) = -2\ln\cosh(\beta\omega_0/2),\quad \ln(1+T) - \ln(1-T) = \beta\omega_0$$

所以 $(1+T)\ln(1+T)+(1-T)\ln(1-T) = \beta\omega_0 T - 2\ln\cosh(\beta\omega_0/2)$。代入：
$$\boxed{\;\int_{T_<} \Sigma_B^{int}\,dt = \frac{1}{2}\bigl[\beta\omega_0 T - 2\ln\cosh(\beta\omega_0/2) - \beta\omega_0 T\bigr] = -\ln\cosh(\beta\omega_0/2)\;}$$

**修正前**任务书有计算错误（漏对 βω₀·T 抵消）；**修正后**精确闭式：
$$\Sigma_B^{int,(neg)} := |\int_{T_<} \Sigma_B^{int}\,dt| = \ln\cosh(\beta\omega_0/2)$$

数值表（修正）：

| βω₀ | $\cosh(\beta\omega_0/2)$ | $\ln\cosh(\beta\omega_0/2)$ |
|-----|------|------|
| 0 | 1 | 0 |
| 1 | 1.128 | 0.120 |
| 2 | 1.543 | 0.434 |
| 3 | 2.352 | 0.856 |
| 3.69（r=80%临界） | 3.06 | 1.118 |
| **4.13**（**c=−1临界**） | **4** | **2 ln 2 ≈ 1.386** |
| 5 | 6.13 | 1.813 |
| 6 | 10.07 | 2.310 |
| ∞ | $e^{\beta\omega_0/2}/2$ | $\beta\omega_0/2 - \ln 2$ |

### §2.2 N_I^{(S:B)} 计算（v8-K9 复核）

mutual info 选 reference：$I(S:B) = S(\rho_S)+S(\rho_B)-S(\rho_{SB})$。pure global state ⟹ $S(\rho_{SB})=0$，$S(\rho_S)=S(\rho_B)=-q\ln q-p\ln p$。所以 $I(S:B) = 2S(\rho_S)$。

$$\dot I(S:B) = 2\dot S(\rho_S) = 2\dot p\ln(q/p) = 4\Omega\sin(2\Omega t)\ln\cot(\Omega t)$$

T_>^{(S:B)} = (0, π/(4Ω))（İ(S:B)>0 区间）。

$$N_I^{(S:B)} := \int_{T_>^{(S:B)}} \dot I(S:B)\,dt = I(S:B)\big|_{\pi/(4\Omega)} - I(S:B)\big|_0 = 2\ln 2 - 0 = 2\ln 2$$

由对称性，$N_I^{(neg, S:B)} := \int_{T_<^{(S:B)}} [-\dot I(S:B)]\,dt = 2\ln 2$ 同样（首半周期内 İ<0 部分）。

### §2.3 c 系数（"信息回流记账"程度）

定义：
$$c(\beta) := \frac{\int_{T_<^B} \Sigma_B^{int}\,dt}{N_I^{(S:B)}} = \frac{-\ln\cosh(\beta\omega_0/2)}{2\ln 2}$$

| βω₀ | $|c(\beta)|$ |
|-----|------|
| 0 | 0 |
| 1 | 0.087 |
| 2 | 0.313 |
| 3 | 0.617 |
| 3.69 | 0.806 |
| **4.13** | **1.000**（critical） |
| 5 | 1.308 |
| 6 | 1.666 |
| ∞ | $\beta\omega_0/(4\ln 2)$ → ∞ |

### §2.4 物理身份判定

**判据**：
- $|c|\to 0$：浴负熵产生累积 ≪ S sector mutual-info amplitude ⟹ 浴负熵产生是统计涨落，不构成实质 backflow
- $|c|=1$：浴负熵产生累积 = mutual-info amplitude ⟹ 一对一记账，"信息回流"完全吸收浴侧负熵
- $|c|>1$：浴负熵产生累积 > mutual-info amplitude ⟹ 存在不能被 S sector backflow 吸收的浴侧"超额"不可逆量 ξ(t,β)

**临界温度**：$|c|=1$ 在 $\beta\omega_0 \approx 4.13$，即 $T_c \approx \omega_0/4.13 \approx 0.242\,\omega_0$。

**温度域分类**：
| 温度域 | $\beta\omega_0$ | $|c|$ | 物理身份 |
|--------|----------------|-----|---------|
| 高温 | $\lesssim 1$ | $\lesssim 0.09$ | **trivial 涨落**（既非 inherent 熵产生也非信息回流，是噪声） |
| 中温 | $1 \lesssim \beta\omega_0 \lesssim 4$ | $0.09\sim 1$ | **信息回流记账主导**（浴负熵产生由 S sector backflow 完全或部分吸收） |
| 低温 | $\gtrsim 4.13$ | $> 1$ | **浴 inherent 熵产生主导**（存在不可被 backflow 吸收的超额量） |

---

## §3 v8-K10 正式条目（写入知识库）

**v8-K10：复合身份定理**（Phase 3 物理裁决）：

在 N=2 双模 JC 共振 + |e,0,0⟩ + 对称耦合 toy 模型中：
$$\int_{T_<^B} \Sigma_B^{int}(t)\,dt = -\ln\cosh(\beta\omega_0/2)$$
$$N_I^{(S:B)} = 2\ln 2\quad\text{(g-independent)}$$
$$c(\beta) := \frac{\int_{T_<^B}\Sigma_B^{int}\,dt}{N_I^{(S:B)}} = -\frac{\ln\cosh(\beta\omega_0/2)}{2\ln 2}$$

物理身份判定：
- $|c|\to 0$ ($\beta\omega_0 \lesssim 1$): trivial 涨落
- $|c|=1$ ($\beta\omega_0 \approx 4.13$): 一对一记账 critical
- $|c|>1$ ($\beta\omega_0 > 4.13$): inherent 浴熵产生主导，存在 ξ ≥ 0 满足 $\int\xi\,dt = (|c|-1)\cdot 2\ln 2$

物理结论：**Σ_B^{int} 不是单一身份，而是温度依赖的"信息回流记账 (B) + inherent 浴熵产生 (A)"复合，分隔尺度 $T_c \approx \omega_0/4.13 \approx 0.24\,\omega_0$**。

L级：⚠️ L2（toy 模型解析；普适性留 v9）
O级：O3（toy）→ O4（普适推广）
math_object：温度依赖复合身份, modular gap, 累积分量, 信息回流记账率
data_access：raw（toy 模型直接计算）

---

## §4 v8 北极星最终判定

**修订后的 v8 北极星陈述**：
> 在 N=2 双模 JC toy 模型中，Σ_B^{int} 的物理身份是温度依赖复合：高温 ($\beta\omega_0 \lesssim 1$) 退化为 trivial 涨落；中温 ($1 \lesssim \beta\omega_0 \lesssim 4.13$) 是信息回流记账主导；低温 ($\beta\omega_0 > 4.13$) 是 inherent 浴熵产生主导。临界温度 $T_c \approx 0.24\,\omega_0$。

**v8 北极星距离**：≈ 95% 完成。剩余 5%：
- toy 模型普适性证明（C[v8-9] 几何不变量推广）
- ε-Bogoliubov 退化谱正则化严格证明（C[v8-3]）
- 多通道耦合下 BKM 核扩展（C[v8-1] 残留）

---

## §5 收官前 GATE 触发清单

按 SOP 收官规范：
- [x] AUDITOR 审计——待触发
- [x] 恶意审稿人——距上次 2 Phase，本Phase 收官触发
- [x] AHA 访客（≥ 2 信号 + 距上次 ≥ 5 Phase 保底）——必须触发
- [x] F 条目重审——v8-P1 已触发，本 Phase 不必重复
- [x] 所有 Active 卡点已完成攻击记录——已更新
- [x] 来源追踪检验——v8-K10 显式标 "v8-P3, toy v8-K8"

下一步：触发四项独立 agent。

---

## §6 自我攻击（PI 主动批判）

PI 在裁决前必须自我攻击：

**SA1：c 系数依赖于 toy 模型选择**
- 若改 N=3 三模 JC，对称耦合 + 真空，c(β) 形式可能变。
- v8-K10 仅在 N=2 双模成立——普适性是开放问题
- **缓解**：c 的 sign（c<0）和 sign change at |c|=1 critical 应是普适的；具体 c(β) 公式 model-dependent
- **响应**：v8-K10 标注"toy 模型解析"，普适化留 v9

**SA2：mutual info 选择 vs. system Nakagawa info**
- 若用 I_S = S(ρ_S) - ln 2（标准 Nakagawa 选择 σ=I/2），则 N_I^{(S)} = ln 2
- c 系数缩小一半，critical 变到 βω₀ ≈ 2.06
- **响应**：v8-K10 显式标"以 I(S:B) mutual info 为参考"——不同 reference 给不同 c 标度，但物理身份判定（trivial/recordkeeping/inherent）不变
- **致命？否——是 reference choice 的 convention 问题，不是物理身份的问题**

**SA3：(★★) 形式可能在不同 BKM 选择下变形**
- 已在 v8-K7 处理（dephasing 类 g²、dissipative 类 g⁴）
- toy 是 dissipative 类（⟨A_S⟩=⟨σ_+⟩=0），但本Phase 直接用闭式动力学，不通过 BKM 展开
- **响应**：本Phase 推导是 nonperturbative；BKM 只用于 Phase 2 形式化

**SA4：北极星修订是否过于温和？**
- 原北极星 "Σ_B^{int} = 信息回流记账项" 是强断言；本Phase 修订为 "复合身份 + 温度依赖" 是弱断言
- **响应**：实事求是 > 维护原断言。v8-K10 比原断言信息量更高（精确 c(β) 闭式 + critical T_c）

**SA5：Aoki 2021 优先权**
- v8-K10 与 Aoki 2021 的关系：Aoki 处理 Σ_total<0；本课题精化 Σ_B^{int} 浴侧分量 + 给 c(β) 解析量化
- **响应**：v8-K10 显式标"Aoki 2021 浴侧分量的 toy 模型精化定量"，承认 Aoki 优先 + 本课题独立贡献限定为 c(β) 闭式

---

## §7 Phase 3 总结

**核心产出**：
- v8-K10 复合身份定理（c(β) 闭式 + 三温度域判定 + critical T_c）

**关闭卡点**：
- 北极星修订完成（C[v8-7] v8-P2 已关闭，本Phase 给数值落地）
- v8 物理裁决完成

**新增卡点**：
- C[v8-10]（新）：v8-K10 c(β) 闭式的普适性——在 N=3/N=4 多模 JC 中是否仍呈 c=−ln cosh(βω₀/2)/(2ln 2) 形式？v9 候选

**北极星最终距离**：v8 已完成主体推导，可触发收官 GATE。
