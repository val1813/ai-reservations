## A作业 Phase 1 — Σ_B^{internal}符号分析+Nakagawa N_I映射

类型：A型分析
执行人：博士A（正规军，独立子agent）
日期：2026-05-30

---

### 文献检索结果（任务书§9）

**搜索#1**：`bath entropy production negative finite-size unitary spin-boson` → 10条命中
- 关键发现1（**直接命中**）：Aoki-Matsuzaki-Hakoshima 2021 (arXiv:2103.05308) — 中心HO+有限N HO浴星型耦合，初始全Gibbs乘积态下，**总熵产生率即使在GKSL Markov近似下也可瞬时为负**，但积分二定律仍成立。摘要明确提供了"对GKSL常识的反例"的有限N幺正模型。
- 关键发现2：Tanimura 2020 (arXiv:2012.09546) — HEOM精确数值发现 **von Neumann熵产生在选用全系统thermal equilibrium(关联初态)时变负**；作者断言"必须用Boltzmann熵(含相互作用项)"才保正性。
- 关键发现3：González-Chakraborty-Rivas 2024 (arXiv:2404.15915) — 强耦合非Markov有限浴spin-boson的能/熵/work/heat/ergotropy系统计算框架（结构性引用，未直接给Σ_B符号判据）。
- 与北极星关系：**直接支撑** Σ_B<0 在finite-N幺正下**形式上可发生**；S3结构性声张已有先例。

**搜索#2**：`Nakagawa information backflow finite bath entropy production` → 10条命中
- 关键发现1：Nakagawa 2026a (arXiv:2601.18822) — 提出统一N_I = ∫_{İ>0} İ dt phase-diagram，分数Caputo模型，过渡边界 α≈1/2 在 (α,ω/λ) 平面。**模型不是spin-boson**，是thermo-field embedded两态分数耗散模型。
- 关键发现2：Nakagawa 2026b (arXiv:2602.09054) — Structural Theory: I(t)的标准选择是 −D(ρ_R(t) ‖ σ)（减相对熵）或 von Neumann S 或 trace distance；**absence of backflow** 充分条件为 CP-divisibility（Theorem 1）+ 时变GKSL生成元+γ_k(t)≥0（Theorem 2）。**N_I = ∫_0^∞ Θ(İ)·İ dt**显式定义。
- 关键发现3：Liu-Goan 2022 (arXiv:2209.06541) — 中心spin+有限spin浴，trace-distance意义下信息回流的塌陷-复苏结构，作finite-bath非Markov测度的具体范例（不给Σ_B但给"浴模式有限性"⇔"非Markov"的桥梁）。
- 与北极星关系：**部分支撑**（N_I定义清晰，I(t)选项明确）；**部分挑战** A5（v6-K4）—Nakagawa原始模型不是Ohmic spin-boson, 其映射到Class I 需独立辩护。

**搜索#3**：`Spohn entropy production proof assumptions Lindblad CPTP unitary global` → 10条命中
- 关键发现1：Spohn 1978 JMP 19, 1227 — 原始定理：**Lindblad半群+Gibbs不变态**下，dS(ρ‖ρ_β)/dt ≤ 0；通过CPTP的data-processing+detailed balance得证。
- 关键发现2：Hierarchy 2026 (arXiv:2604.25245) — 非Markov系统熵产生层级与权衡关系，将Spohn拓展到非Markov条件并暗示**非Markov下可瞬时违反Spohn界**。
- 关键发现3：Manatuly et al. 2017 (arXiv:1704.06029) — CPTP带equilibrium的Spohn半群证明的现代Wigner-Yanase形式；将三层前提精确分离为(i)CPTP(ii)invariant Gibbs(iii)Lindblad-Lieb-Ruskai单调性。
- 与北极星关系：**支撑**S3结构声张；提供撞墙#2拆解的标准框架。

---

### §0.5 隐含假设清单

| 假设 | 原始来源 | 原文适用条件 | v8语境是否满足 |
|------|---------|--------------|--------------|
| A1: v5-K6精确恒等式 Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt − Σ_B^{internal} | v5-K6 | 幺正全系统+能量守恒+∂_t H*=0 (静态H*) | ✓ 满足，但∂_t H*=0仅在Class I严格 (v6-K2) ⚠️边缘 |
| A2: Spohn 1978, dS(ρ‖ρ_β)/dt ≤ 0 | L7 | Lindblad CPTP半群+Gibbs不变态+(热力极限N→∞) | **✗ 全部失效**(见撞墙#2) |
| A3: Class I下H*∝I (linked-cluster精确) | v3-K10 | Ohmic spin-boson, 线性耦合 | ✓ 满足 |
| A4: ∂_t H*=0仅对静态形式H*；H*_eff(t)需绝热近似 | v6-K2 | 时间无关算符 | ✓ 满足；Phase 2若用H*_eff(t)需重写A1 |
| A5: Nakagawa α≈1/2严格映射到sub-Ohmic s≈1/2；Ohmic记忆核非Mittag-Leffler | v6-K4 | Mittag-Leffler或分数Caputo动力学 | **⚠️ Class I (Ohmic)不在原始适用域**, 需独立论证（见N.3） |
| A6: N_I(t) = ∫_0^t [İ(s)]_+ ds, I(t) := −D(ρ_R‖σ)是标准选择 | arXiv:2602.09054 Def.1 | reduced sector R+不变参考态σ | **⚠️未匹配**：v8需指明R=S还是R=B及σ=何（见N.3） |
| A7: N=4不构成合法浴；N_c≈15量子-热力crossover | v2-K1, v2-K5 | spin系统耦合谐振子浴 | ✓ 满足；Phase 2数值需N≥15 |

---

### §1 强制撞墙

#### 攻击#1: 最简反例 — N=1单振子浴 + Jaynes-Cummings

**模型**：H = ε σ_z + ω b†b + g(σ_+ b + σ_- b†)（旋转波近似的JC模型，共振 ε=ω）。初态 |Ψ_0⟩ = (cos θ |g⟩+ sin θ |e⟩)⊗|0⟩；为使 ρ_B(0)=Tr_S|Ψ_0⟩⟨Ψ_0|=|0⟩⟨0|纯态。

**JC闭式解**（共振，单激发子空间）：
$$|\Psi(t)\rangle = \cos\theta\, |g,0\rangle + \sin\theta\, [\cos(gt)|e,0\rangle - i\sin(gt)|g,1\rangle]$$

得到 $\rho_B(t) = (1 - \sin^2\theta\sin^2(gt))|0\rangle\langle 0| + \sin^2\theta\sin^2(gt)|1\rangle\langle 1|$。
记 $p(t):=\sin^2\theta\sin^2(gt)$。

- $\langle H_B\rangle(t) = \omega p(t)$
- $S_B(t) = -p\ln p - (1-p)\ln(1-p)$
- $dp/dt = g\sin^2\theta\,\sin(2gt)$
- $d\langle H_B\rangle/dt = \omega g\sin^2\theta\,\sin(2gt)$
- $dS_B/dt = \ln\!\frac{1-p}{p}\cdot dp/dt$

**关键代入**：取 $\theta=\pi/4$（$\sin^2\theta=1/2$，$p_{\max}=1/2$，使 $S_B$ 在峰处取 $\ln 2$），考察区间 $t\in(\pi/(4g),\pi/(2g))$:
- $\sin(2gt)>0$（直到 $\pi/(2g)$）⇒ $d\langle H_B\rangle/dt>0$
- $p(t)\in(1/4,1/2)$ ⇒ $\ln\frac{1-p}{p}>0$ ⇒ $dS_B/dt>0$

代入 $\Sigma_B^{internal} = dS_B/dt - \beta\,d\langle H_B\rangle/dt$:
$$\Sigma_B^{int} = g\sin^2\theta\sin(2gt)\,[\ln\!\tfrac{1-p}{p} - \beta\omega]$$

**符号判据**：$\Sigma_B^{int}<0$ ⟺ $\ln\!\tfrac{1-p(t)}{p(t)} < \beta\omega$。

在 $p(t)\to 1/2^-$ 极限（$t\to\pi/(2g)^-$）：$\ln\frac{1-p}{p}\to 0^+$。任何 $\beta\omega>0$（任何正温）都能让 $\Sigma_B^{int}<0$ 在该窗口非空。

**反例量级**：$\beta\omega=1$ ⟹ $p_{\rm crit}$ 由 $\ln((1-p)/p)=1$ ⟹ $p_{\rm crit}\approx 0.269$ ⟹ $\sin^2(gt)>0.538$ ⟹ $t\in(0.412/g,\,0.588/g)\approx (\pi/2.42g,\,\pi/1.70g)$；持续约 $0.18/g$，宽约 $5.7\%$ 周期。

**结论(撞墙#1)**：N=1 JC在共振+正温下，$\Sigma_B^{int}<0$ **存在显式有限时间窗口**，无需Markov+Lindblad假设。"finite-N浴中Σ_B^{int}可负"在最简形式下即成立。但 N=1 ≪ N_c (v2-K1/K5) ⟹ 此结果**仅证 Σ_B<0 不被禁戒**，不蕴含 v8 北极星 Phase 2 "合法浴 N≥15"下也成立——后者需独立数值。

#### 攻击#2: Spohn 1978三层拆解

**Layer 1（Lindblad CPTP半群）**：要求 ρ(t)=Φ_t[ρ(0)] 为CPTP且生成元为时间无关Lindblad form（Markovian）。
- v8设定：浴 ρ_B(t) = Tr_S U(t)(ρ_S⊗ρ_B(0))U†(t)。从初态固定看，{ρ_B(0)→ρ_B(t)}是partial-trace-of-unitary即CPTP map（Stinespring）。但**generator并非Markov Lindblad**：BLP非Markov测度+CP-divisibility失败已是finite-N+gapped bath的通识（Liu-Goan 2022 arXiv:2209.06541对中心spin+有限spin浴明示）。
- **结论：Layer 1 形式上失败**（Markov前提不成立）。

**Layer 2（Gibbs不变态）**：要求 L[ρ_β]=0，即detailed balance使Gibbs为fixed point。
- v8: 浴单独的演化由全系统幺正裁决；任何"自由Gibbs ρ_β = e^{-βH_B}/Z"在 H_I 关联下被破坏；**没有不变Gibbs态**作为浴侧动力学的fixed point。
- **结论：Layer 2 形式上失败**。

**Layer 3（相对熵单调性 / data-processing）**：在Layer 1+2 satisfied下，dD(ρ_B(t)‖ρ_β)/dt ≤ 0。
- v8: 仅partial-trace-of-unitary是CPTP，data-processing只给**端点不等式**：D(ρ_B(t)‖σ) ≤ D(ρ_B(0)‖σ)（concatenation of CPTP）。**沿途单调性不保**：dD/dt 可正可负（即 Σ_B^{int} 任意符号）。
- **结论：Layer 3 退化为端点不等式，沿途强单调失败**。

**总结**：Spohn证明在v8设定下三层全部形式失效或退化。**Σ_B^{int} ≥ 0 没有先验保证**。S3结构声张成立。

#### 攻击#3: v5-K6 + Σ_S^{(gauge)}≥0 + I(S:B)≥0 + C_coup有界 能否锁定 Σ_B^{int} 符号？

由A1：$\Sigma_B^{int} = \frac{d}{dt}I(S:B) + \beta\,\frac{dC_{coup}}{dt} - \Sigma_S^{(gauge)}$

已知约束：
- $\Sigma_S^{(gauge)}\ge 0$ （v5-K6+热力学极限附加假设）
- $I(S:B)\ge 0$ 始终（Klein不等式）
- $|C_{coup}|\le C^*$ 有界

**关键观察**：约束**仅限制端点值与符号**，不限制**时间导数**：
- $I(S:B)\ge 0$ 不蕴含 $dI/dt$ 任意符号；非Markov系统 $dI/dt$ 可正可负（信息回流）
- $|C_{coup}|\le C^*$ 不蕴含 $dC/dt$ 符号
- $\Sigma_S^{(gauge)}\ge 0$ 仅给上界 $\Sigma_S^{(gauge)}\ge 0$

代回得：
$$\Sigma_B^{int} \le \frac{dI(S:B)}{dt} + \beta\frac{dC_{coup}}{dt}$$
（以 $\Sigma_S^{(gauge)}\ge 0$ 移项）

这是**单边上界**，不锁定符号。$\Sigma_B^{int}<0$ 当且仅当 $\frac{dI}{dt}+\beta\frac{dC}{dt} < \Sigma_S^{(gauge)}$；该条件与三个非负约束**相容**（即没有矛盾），所以 v5-K6 + 三非负 **无法**单独迫使 $\Sigma_B^{int}\ge 0$ 或 $\Sigma_B^{int}\le 0$。

**结论(攻击#3)**：S2弱命题被证伪。$\Sigma_B^{int}$ 符号承载独立信息，需要独立的浴侧动力学结构（如Nakagawa N_I 或更细的浴-modular结构）来判定。**v5-K6没有让Nakagawa映射变得不必要**；北极星方向不被绕过。

---

### §N 推导

#### N.1 Σ_B^{internal} 的浴侧重写（产出#1）

**setup**：$H = H_S + H_B + H_I$，$\partial_t H_\alpha = 0$，全系统幺正 $|\Psi(t)\rangle = U(t)|\Psi_0\rangle$，$\rho_B(t) = \text{Tr}_S |\Psi(t)\rangle\langle\Psi(t)|$。

**(a) 浴能量演化** [Heisenberg, $\partial_t H_B=0$]:
$$\frac{d\langle H_B\rangle}{dt} = -i\langle [H_B, H]\rangle = -i\langle [H_B, H_I]\rangle_{\rho_{SB}}$$
（[H_B,H_S]=0；[H_B,H_B]=0）

**(b) 浴熵演化**：$\rho_B$ 满足
$$\dot\rho_B = -i[H_B,\rho_B] - i\,\text{Tr}_S[H_I,\rho_{SB}]$$
（partial trace of Liouville-von Neumann; $\text{Tr}_S[H_S,\rho_{SB}]=[H_S,\rho_B]_S$ 在 partial trace 下消失因 $H_S$ 仅作用于S）

由 $S_B = -\text{Tr}\rho_B\ln\rho_B$ 与 $\text{Tr}\dot\rho_B=0$：
$$\frac{dS_B}{dt} = -\text{Tr}_B(\dot\rho_B\ln\rho_B)$$

代入 $\dot\rho_B$：
- 第一项 $i\,\text{Tr}_B([H_B,\rho_B]\ln\rho_B) = i\,\text{Tr}_B(H_B[\rho_B,\ln\rho_B])=0$（$\rho_B$ 与 $\ln\rho_B$ 对易）
- 第二项 $i\,\text{Tr}_B(\text{Tr}_S[H_I,\rho_{SB}]\ln\rho_B) = i\,\text{Tr}_{SB}([H_I,\rho_{SB}](I_S\otimes\ln\rho_B))$

利用 $\text{Tr}([A,B]C) = \text{Tr}(B[C,A])$：
$$\frac{dS_B}{dt} = i\,\text{Tr}_{SB}(\rho_{SB}[I_S\otimes\ln\rho_B,\,H_I]) = i\langle [\ln\rho_B(\text{ext}),\,H_I]\rangle_{\rho_{SB}}$$

引入瞬时浴modular Hamiltonian $K_B(t) := -\ln\rho_B(t)$（视为 $I_S\otimes K_B$ on $\mathcal{H}_S\otimes\mathcal{H}_B$）：
$$\boxed{\;\frac{dS_B}{dt} = -i\langle[H_I, K_B(t)]\rangle_{\rho_{SB}}\;}$$

**(c) 综合**：定义 modular gap
$$\Delta K_B(t) := K_B(t) - \beta H_B = -\ln\rho_B(t) - \beta H_B$$
（衡量瞬时浴态对 Gibbs $\rho_\beta = e^{-\beta H_B}/Z_B$ 的偏离；当 $\rho_B(t)=\rho_\beta$ 时 $\Delta K_B = -\ln Z_B$ 为常数）。

合并 (a)+(b)：
$$\boxed{\;\Sigma_B^{int}(t) = \frac{dS_B}{dt} - \beta\frac{d\langle H_B\rangle}{dt} = -i\langle[H_I,\,\Delta K_B(t)]\rangle_{\rho_{SB}(t)}\;}\quad\text{【产出#1】}$$

**自洽检查**：
1. 若 $\rho_B(t)=\rho_\beta$（瞬时Gibbs）⟹ $\Delta K_B = -\ln Z_B$ 为标量 ⟹ $[H_I,\Delta K_B]=0$ ⟹ $\Sigma_B^{int}=0$。✓ 与 Spohn$=$0 平衡相容。
2. $-i\langle[H_I,\Delta K_B]\rangle$ 为实数（Hermitian commutator的期望乘 $-i$ 实），与 $\Sigma_B^{int}$ 实数相容。✓
3. 不显含 $\rho_S$、$H_S$、$\Sigma_S$，**仅依赖** $\rho_{SB}$、$H_I$、$\rho_B$、$H_B$ ⟹ 满足产出#1要求"仅浴侧+耦合算符"。✓

**评论**：$\Delta K_B$ 是经典Gibbs偏离的非平衡推广；$-i\langle[H_I,\Delta K_B]\rangle$ 是浴modular flow与thermal flow的算符差驱动 $H_I$ 的"非补偿热流"。

#### N.2 Σ_B^{internal}<0 的充分条件（产出#2）

由产出#1，$\Sigma_B^{int}<0$ ⟺ $\text{Im}\langle[H_I, K_B-\beta H_B]\rangle > 0$（去掉 $-i$）。

**充分条件A（modular-thermal flow misalignment）**：
$$\text{Im}\langle[H_I, K_B(t)]\rangle > \beta\cdot\text{Im}\langle[H_I, H_B]\rangle$$
即"浴modular flow在 $H_I$ 方向产生的虚相位"超过"thermal flow在同方向的虚相位"。**物理意义**：浴态 $\rho_B(t)$ 已偏离Gibbs，使 $K_B$ 不再正比于 $\beta H_B$，且偏离方向与 $H_I$ 耦合方向有锁相结构。

**充分条件B（弱耦合二阶 Bogoliubov-Kubo-Mori 形式）**：弱耦合 $g\to 0$ 下展开 $\Delta K_B(t) = g^2\,\Delta K_B^{(2)}(t) + O(g^3)$。Born-近似下:
$$\Sigma_B^{int}(t) \approx 2g^2\,\text{Im}\!\int_0^t ds\,\big[\,\chi_B^{neq}(t,s) - \chi_B^{eq}(t-s)\,\big]\,\langle B(t)A_S(s)\rangle_{cum} + c.c.$$
其中 $H_I = g\,A_S\otimes B_B$，$\chi_B^{eq}$ 是 Gibbs 浴 $\rho_\beta$ 下的 retarded susceptibility（满足 KMS），$\chi_B^{neq}(t,s)$ 是瞬时态 $\rho_B(t)$ 下susceptibility。**$\Sigma_B^{int}<0$ 充分条件**：$\chi_B^{neq}-\chi_B^{eq}$ 与系统cumulant的相位差 $>\pi/2$ 在某区间。

**充分不可能条件（passive bath）**：若 $\rho_B(t)$ 始终 passive（任意 $H_I$ 扰动下能不增 — 即 $\rho_B = f(H_B)$ 单调减函数），则 $K_B = \tilde\beta(t)H_B + \text{const}$ for some $\tilde\beta(t)$。代入产出#1：
$$\Sigma_B^{int} = -i(\tilde\beta(t)-\beta)\langle[H_I, H_B]\rangle = (\tilde\beta(t)-\beta)\frac{d\langle H_B\rangle}{dt}$$
若 $\tilde\beta(t)$ 与 $d\langle H_B\rangle/dt$ 同号（浴升温吸能 / 降温放能）则 $\Sigma_B^{int}\ge 0$。⟹ **passive + 同号率 ⟹ Σ_B^{int}≥0**。这是Spohn-类陈述在 v8 设定下的精确替代物；**Σ_B^{int}<0 必然伴随浴态非passive**。

**有限N可显式检验判据（产出#2核心）**：
$$\boxed{\text{Σ}_B^{int}(t)<0\ \iff\ \rho_B(t) \notin\{\rho:\rho=f(H_B)\}\ \text{且 modular flow 与 H_I 失锁相}}$$
（passive 退化情形给 $\Sigma_B^{int}\ge 0$；非passive + 锁相条件给 $<0$）

#### N.3 与 Nakagawa N_I 的形式映射（产出#3）

**(i) reduced-bath 映射（A的反直觉桥）**：
取 Nakagawa setup 的 reduced sector $R := B$，参考态 $\sigma := \rho_\beta$（Gibbs）。定义信息度
$$I_B(t) := -D(\rho_B(t)\|\rho_\beta) = S(\rho_B) - \beta\langle H_B\rangle - \ln Z_B$$

时间导数：
$$\dot I_B(t) = \frac{dS_B}{dt} - \beta\frac{d\langle H_B\rangle}{dt} = \Sigma_B^{int}(t)$$

⟹ **形式恒等式（产出#3-A）**：
$$\boxed{\;\Sigma_B^{int}(t) \equiv \dot I_B(t)\quad\text{for}\quad I_B := -D(\rho_B\|\rho_\beta)\;}$$

**Nakagawa N_I^{(B)} 与 Σ_B^{int} 关系**：
$$N_{I_B}(t) = \int_0^t [\dot I_B(s)]_+\,ds = \int_{[0,t]\cap\{\Sigma_B^{int}>0\}} \Sigma_B^{int}(s)\,ds$$

注意符号方向：
- $\dot I_B>0$ ⟺ $D(\rho_B\|\rho_\beta)$ 下降 ⟺ 浴**接近**Gibpps（标准热化方向）
- $\Sigma_B^{int}<0$ ⟺ $\dot I_B<0$ ⟺ $D(\rho_B\|\rho_\beta)$ 上升 ⟺ 浴**远离**Gibbs

⟹ **Nakagawa原始 N_I 是"浴趋近Gibbs的累积量"**；我们关心的负性区间对应 Nakagawa **负部分** $N^{neg}_{I_B}(t) := \int [\dot I_B]_-\,ds$。

**(ii) standard-system 映射（与 v5-K6 联动）**：
若按 Nakagawa 原始物理意图，reduced sector $R := S$，参考态 $\sigma := \rho_S^{steady}$ 或 $\rho_S^{Gibbs}$。
- $\dot I_S = -d/dt\,D(\rho_S\|\sigma)$
- N_I^{(S)}>0 ⟺ ρ_S 接近 σ — 即"信息从 S+B 关联流回 S"

将 v5-K6 改写：
$$\Sigma_B^{int} = \frac{d I(S:B)}{dt} + \beta\frac{dC_{coup}}{dt} - \Sigma_S^{(gauge)}$$

**形式映射定理（产出#3-B，弱声张）**：
$$\Sigma_B^{int}(t) < 0\ \Rightarrow\ \frac{dI(S:B)}{dt} < \Sigma_S^{(gauge)} - \beta\frac{dC_{coup}}{dt}$$
（即"浴反热化"必伴随S-B互信息上升较慢或下降）

但**此映射不锁定 $\dot I_S$ 符号**（$\dot I_S$ 由 $\Sigma_S^{(gauge)}$ 与 $\rho_S$ steady 关系决定，需独立动力学输入）。⟹ **$\Sigma_B^{int}<0$ 与 N_I^{(S)}>0 无强制时间重合**。

**(iii) Class I / Ohmic 适用性（A5/v6-K4 警告）**：
Nakagawa 2026a (arXiv:2601.18822) 原始模型是 **fractional Caputo two-state thermo-field embedded** 模型；过渡边界 $\alpha\approx 1/2$ 在 $(\alpha,\omega/\lambda)$ 平面上对应 **sub-Ohmic s≈1/2**；**Ohmic Class I 记忆核非Mittag-Leffler** 已在 v6-K4 指出。

⟹ §7 S1 强声张 "重合度>80%" **仅在 sub-Ohmic s≈1/2 域有先验保障**；Class I/Ohmic 必须Phase 2 数值独立检验。

#### N.4 finite-N 浴的具体阶估算

**spin-boson Class I-like benchmark**：单 spin + N=20 谐振子，Ohmic 谱 $J(\omega)=\alpha\omega e^{-\omega/\omega_c}$，$\alpha=0.4$，$\beta\omega_c\sim 1$。

弱耦合下 $\Delta K_B^{(2)}\sim g^2/\omega_c$（$g$ 为典型耦合）。每模式平均 $g^2\sim \alpha\omega_c^2/N$。
$$|\Sigma_B^{int}|_\text{peak}\sim g^2\cdot |[H_I,\Delta K_B]|/\hbar\sim g^4 N/\omega_c\sim \alpha^2\omega_c \approx 0.16\,\omega_c$$

负性窗口典型时间尺度 $\Delta t\sim \omega_c^{-1}$（信息回流时间），故 $\int |\Sigma_B^{int}|_-\,dt\sim 0.16$（自然单位 $k_B=1$）。

**数值可行性**：N=20 谐振子 + truncation $n_{max}=4$/模式 ⟹ Hilbert 维数 $2\cdot 5^{20}\approx 2\cdot 10^{14}$（不可行 ED）。需用 **chain mapping (Lanczos) + TEBD/HEOM**，或 hierarchical equations (HEOM with N_K≤6 hierarchy levels) ⟹ 与v2-K5 N_c≈15 量子-热力crossover一致；Phase 2实操推荐 N=15-30 + chain-TEBD。

---

### 新增卡点

```
卡点编号：C[v8-1]
目标：Σ_B^{internal}(t) 的 Bogoliubov-Kubo-Mori 二阶可观测重写之闭式核 K(t,s)
卡住位置：§N.2 充分条件B 仅给示意性双相关展开，χ_B^{neq} 与 χ_B^{eq} 系数关系未闭式
类型：解析-计算
关闭路径：Phase 2 B正规军 完成 Bogoliubov-Kubo 展开 + Class I sub-Ohmic数值印证
预计关闭Phase：Phase 2
三轮攻击尝试：
  第1轮 (本Phase)：线性响应展开给出示意公式，未闭式
  第2轮 (待Phase 2)：Bogoliubov-Kubo-Mori inner product 显式核
  第3轮 (待Phase 2)：path-integral 表示交叉验证
最小失败证据：当前公式无法直接代入 Class I sub-Ohmic 数值脚本
```

```
卡点编号：C[v8-2]
目标：严格证明或证伪 "Σ_B^{int}<0 时间窗口 ⊆ Nakagawa N_I^{(S)}>0 时间窗口"（强映射）
卡住位置：§N.3 (ii) 给出弱方向蕴含但未给反向，重合度需Phase 2数值
类型：动力学-数值
关闭路径：Phase 2 数值 spin-boson sub-Ohmic s≈0.5, N=15-30, α∈[0.3,0.5]
预计关闭Phase：Phase 2
三轮攻击尝试：
  第1轮 (本Phase)：仅形式映射，无数值
  第2-3轮：待 Phase 2
最小失败证据：仅有形式蕴含，无数值重合度
```

C1(v5) 状态更新：本Phase产出#1已给出 $d/dt I(S:B)$ 的浴侧重写路径——结合 v5-K6 反推：
$$\frac{dI(S:B)}{dt} = \Sigma_S^{(gauge)} - \beta\frac{dC_{coup}}{dt} + \Sigma_B^{int} = \Sigma_S^{(gauge)} - \beta\frac{dC_{coup}}{dt} - i\langle[H_I,\Delta K_B]\rangle$$
此为 C1(v5) 的 **modular-flow 显式表示**，但仍依赖于 $\rho_B(t)$ 的瞬时谱（等同重新打开），**未实质关闭 C1(v5)**——需独立的 $\rho_B(t)$ 动力学输入。状态：维持开放，攻击轮次 +1 (现 6 Phase 活跃)。

---

### 本Phase结论（一句话）

**v8有限N幺正全系统下 $\Sigma_B^{int}(t) = -i\langle[H_I, -\ln\rho_B(t) - \beta H_B]\rangle_{\rho_{SB}}$ ≡ $\dot I_B$ 其中 $I_B := -D(\rho_B\|\rho_\beta)$；其符号由瞬时浴modular gap $\Delta K_B(t)$ 与耦合 $H_I$ 的对易期望决定，Spohn 1978 三层前提（CPTP半群 / Gibbs不变 / 沿途相对熵单调）在 v8 设定下全部失效，N=1 Jaynes-Cummings 共振区已显式构造 $\Sigma_B^{int}<0$ 时间窗口（$\Sigma_B^{int}\propto \sin(2gt)[\ln\frac{1-p}{p}-\beta\omega]$），且 v5-K6+三非负无法独立锁定 $\Sigma_B^{int}$ 符号（攻击#3否定 S2弱），故北极星方向需 Phase 2 在 sub-Ohmic s≈1/2, N=15-30 数值检验 S1 强声张（Σ_B<0 与 N_I^{(S)}>0 重合度 >80%），S3 结构性声张已被三层失效拆解+文献(Aoki 2021, Tanimura 2020)双重支撑。**

北极星距离判断：**已锚定形式判据（产出#1精确）+ Spohn 三层失效结构清晰（S3确立）+ S2 弱命题已在攻击#3 否定（北极星不被绕过）；S1 强声张待 Phase 2 数值定夺**。

---

### 对未来B的预判攻击点

**攻击点1**：**N.1 partial trace 在 ρ_B 退化谱处的正则性 / 奇异性**
- 问题：$dS_B/dt = -\text{Tr}_B(\dot\rho_B \ln\rho_B)$ 在 $\rho_B$ 出现零本征值瞬间（如 N=1 JC 拉比谷 $p(t)=0$ 或 $p(t)=1$）$\ln\rho_B$ 发散；$\Sigma_B^{int}$ 是否在该时刻是 well-defined 实数还是 distributional？
- 产出#1 是否仅在 $\rho_B$ 满秩区间适用，零本征区间需重新定义（regularization or replica）？
- **建议 B 用算子代数 / 信息几何视角进攻**：检查 Lieb-Robinson regularization 或 quantum modular theory（Tomita-Takesaki）下 $\Delta K_B$ 在退化谱的延拓是否良态；若 $\Sigma_B^{int}$ 在退化点出现 distributional 奇异，攻击#1 的 N=1 JC 反例需重新审视（可能是奇异点而非真负值区间）。

**攻击点2**：**N.3 reduced-bath 映射 (R=B, σ=ρ_β) 是否合法 / 物理上等同于Nakagawa 原意**
- 问题：Nakagawa 原始 setup 的 R 是"open system"（被环境扰动的小子系统），σ 是该子系统的稳态。我反过来取 R=B（"环境本身"）、σ=自由Gibbs，这在 Nakagawa structural theory (arXiv:2602.09054 Theorem 1) 的 CP-divisibility 条件下是否仍 well-defined？
- 浴在 v8 中既不是 CP-divisible 也无 invariant Gibbs（攻击#2 已证），那么 N_{I_B} 是否仍承袭 Nakagawa 框架的物理解释，还是退化为 trivial relabeling？
- **建议 B 用物理化学 / 泛函分析 视角进攻**：检查 Nakagawa 结构理论的 reduced sector 对称性是否真的允许 R=B 的反向映射；若该映射在物理上是空的（仅符号代换），则产出#3-A 的"形式恒等式"虽数学正确但物理上不构成 Nakagawa 框架内的真实 backflow 量化，S1 强声张需重新陈述为"reduced-bath 信息度的负反流"而非"标准 Nakagawa 信息回流"。
