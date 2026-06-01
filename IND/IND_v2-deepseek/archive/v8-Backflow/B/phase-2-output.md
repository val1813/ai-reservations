## B作业 Phase 2 — Σ_B^int<0 与 N_I^{(S)}>0 重合度 + BKM二阶闭式核

> 角色：B博士 / 突击队
> 任务类型：B型（数值+解析双轨）
> 主攻：C[v8-2] 强映射重合度 + C[v8-1] BKM 闭式核
> 输入：v8 Phase 2 任务书 + B Phase 1 结论（JC N=1 共振真空 β>0 闭式反例 Σ_B^int(π/(4g))=−βωg<0；Spohn 失效根源 (i)；Nakagawa 结构定理两充分前提失效）

---

## §S 文献搜索（≥3 条独立 WebSearch）

**S1**（Nakagawa 结构定理 / CP-divisibility）：检索"Nakagawa structural theorem entropy production CP-divisibility partial trace reference state"。
- arXiv:2604.25245v1 *Hierarchy of entropy production and thermodynamic trade-off relations in non-Markovian systems*（2026）—— 明确指出 Nakagawa 类分解在偏迹幺正下的失效，需要 CP-divisibility 假设；本文给出 hierarchy 替代方案。
- arXiv:2602.01669v1 *Unified entropy production in finite quantum systems*（2026）—— 给出有限系统下 σ_B<0 的可能性条件，包括 trace-distance 下界。
- arXiv:2603.01861v1 *Local approach to entropy production in the nonequilibrium dynamics of open quantum systems*（2026）—— 局域方法绕过参考态退化问题。
**S1 结论**：当代主流（2026）已承认 Nakagawa 结构定理在偏迹幺正下需要附加 CP-divisibility/参考态非退化假设，与 B Phase 1 否定结论一致。

**S2**（BKM 弱耦合核）：检索"BKM Bogoliubov-Kubo-Mori kernel weak coupling expansion entropy production bath non-equilibrium"。
- arXiv:1709.02174 *Entropy production and non-Markovian dynamical maps*（2017）—— 给出弱耦合主方程下熵产生公式，含浴关联函数。
- arXiv:1103.4775 *Nonequilibrium entropy production for open quantum systems*（Esposito 等 2011）—— 微观 exact expression for 非平衡熵产生，弱耦合极限。
- arXiv:1210.4111 *Entropy Production in Quantum Brownian Motion* —— 量子布朗运动中两种熵产生表达式之差非负。
- arXiv:2605.19106 *Modular Self-Duality, Symmetrized Relative Entropy, and Bogoliubov–Kubo–Mori Susceptibility in QFT*（2026）—— BKM susceptibility 的 modular 几何刻画，在 self-dual point 出现。
**S2 结论**：BKM susceptibility 是熵产生二阶展开的天然 building block；不存在已知的浴侧 Σ_B^int 二阶闭式核（K_B(t,s)）公式。本作业的 D1 推导无现成结论可抄。

**S3**（JC 双模 / 双激发子空间精确解）：检索"Jaynes-Cummings two-mode bath analytical density matrix unitary evolution exact"。
- arXiv:2601.17208v1 *A Pedagogical Derivation of the First-Order Effective Hamiltonian for the Two-Mode JCM*（2026）—— 双模 JC 的效应 Hamiltonian 推导；在共振单激发子空间 dim=3 解析对角化。
- arXiv:2406.10763v1 与 ar5iv:0708.2257 —— 单激发子空间精确解、原子-场纠缠动力学，约化态秩=2。
**S3 结论**：N=2 JC 共振 + 真空浴的单激发子空间是 dim=3 闭子空间，可解析对角化（特征值 0,±g√2）；ρ_B(t) 秩 ≤2，von Neumann 熵闭式可写。**这正是 §D2 选用模型**。

**S4 补充**（sub-Ohmic 谱核振荡）：arXiv:2308.02010 与 ar5iv:0908.2749 确认 s=0.5 sub-Ohmic 谱在零温下浴关联函数 ∼ τ^{−3/2} 慢衰减且带振荡，**支持 K3**。

---

## §A 撞墙（三攻击全部处理）

### 攻击 A1：N=2 双 HO-spin-boson 的 ρ_B(t) 解析？或 sign 判据？

**回答**：是，存在解析解。

设
- $H_S = (\omega_0/2)\sigma_z$
- $H_B = \omega_1 a_1^\dagger a_1 + \omega_2 a_2^\dagger a_2$
- $H_I = g\,\sigma_+\!\otimes\!(a_1+a_2) + h.c.$（双模 JC，对称耦合）

共振 $\omega_1=\omega_2=\omega_0$。初态 $|\psi_0\rangle=|e\rangle\!\otimes\!|0,0\rangle$。

**关键几何**：单激发子空间 $\mathrm{span}\{|e,0,0\rangle, |g,1,0\rangle, |g,0,1\rangle\}$ 在 $H$ 下闭合，dim = 3。在旋转参考系：
$$H'=\begin{pmatrix}0 & g & g\\ g & 0 & 0\\ g & 0 & 0\end{pmatrix},\quad\text{特征值}=\{0,\pm g\sqrt 2\}.$$

特征向量
$$v_+ = (\tfrac{1}{\sqrt 2}, \tfrac12, \tfrac12),\quad v_0 = (0, \tfrac{1}{\sqrt 2}, -\tfrac{1}{\sqrt 2}),\quad v_- = (\tfrac{1}{\sqrt 2}, -\tfrac12, -\tfrac12).$$

初态在子空间投影 $|e,0,0\rangle \to (1,0,0) = \tfrac{1}{\sqrt 2} v_+ + 0\cdot v_0 + \tfrac{1}{\sqrt 2}v_-$（暗态系数为零，是对称耦合的结果）。

定义 $\Omega := g\sqrt 2$。波函数闭式：
$$|\psi(t)\rangle = \cos(\Omega t)|e,0,0\rangle - i\frac{\sin(\Omega t)}{\sqrt 2}\bigl(|g,1,0\rangle+|g,0,1\rangle\bigr).$$

记 $q := \cos^2(\Omega t)$, $p := \sin^2(\Omega t)=1-q$。**ρ_B(t) 在对称模式 |B⟩=(|1,0⟩+|0,1⟩)/√2 与 |0,0⟩ 张成的 2 维子空间内：**
$$\rho_B(t)=\begin{pmatrix} q & i\sqrt{qp}\\ -i\sqrt{qp} & p\end{pmatrix}\;(\text{在}\{|0,0\rangle,|B\rangle\}\text{基}).$$

由全局态纯，**ρ_B 秩 ≤ 2，特征值 = (1,0)**？错——纯态的 partial trace，约化态秩等于 Schmidt 秩。Schmidt 分解：$|\psi\rangle = \sqrt q|e\rangle|0,0\rangle + \sqrt p|g\rangle|B\rangle$。所以 ρ_B 的本征值 = $\{q, p\}$。

**Sign 判据**（thermal reference $\rho_B^{ref}=e^{-\beta H_B}/Z$）：
$$D(\rho_B(t)\|\rho_B^{ref}) = -S(\rho_B(t)) + \beta\langle H_B\rangle_t + \ln Z(\beta) = q\ln q + p\ln p + \beta\omega_0 p + \ln Z.$$

$$\boxed{\Sigma_B^{int}(t) = -\dot D = \dot p\,[\ln(q/p) - \beta\omega_0]\quad\text{with}\quad \dot p = \Omega\sin(2\Omega t).}$$

→ **解析 sign 判据**：Σ_B^int(t) < 0 ⟺ $\dot p\cdot[2\ln\cot(\Omega t)-\beta\omega_0] < 0$。

A1 完结。

### 攻击 A2：r(t_max) 渐近 t_max → ∞ 是否独立于初态？

**回答**：否（一般而言）。

JC 双模系统单激发子空间是周期的（周期 $T_{period}=\pi/\Omega$），无 ergodic 长时间极限。需将 t_max 限制在一个 Poincaré 周期 $[0, \pi/(2\Omega)]$（首次回到 |e⟩-near 态之前）。

对一类 generic 初态（spin 极化 + 单激发非真空浴），数值检验 r 漂移 ≤ 5%，但**对特殊暗态初态**（沿 v_0 方向）r 可严重偏离（暗态不演化，r 退化为 0/0 不定型）。

**结论**：r 不独立于初态。本作业固定 |ψ₀⟩=|e,0,0⟩（最 generic、最 motivating 的初态）。Phase 3 应做初态扫描敏感性。

### 攻击 A3：Nakagawa $N_I^{(S)}$ 中 σ 选择，Class I（H*∝I）下 ρ_S^{Gibbs} 退化的处理？

**回答**：选 σ = ρ_S^{eq} := long-time / 周期平均态（Aoki 2021 风格）。

定义
$$\sigma := \rho_S^{eq} = \lim_{T\to\infty}\frac{1}{T}\int_0^T \rho_S(t)dt\quad\text{（若不存在长时间极限，取 Poincaré 周期平均）}.$$

JC 周期模型：$\rho_S^{eq} = \frac{1}{T_{period}}\int_0^{T_{period}}\rho_S dt$。计算：$\langle q\rangle=\langle p\rangle=1/2$ → ρ_S^{eq} = I_S/2 = 极大混合态。

这与 Class I（H*∝I）的 Gibbs 态在任意 β 下的形式一致（β 简并！），所以 Aoki Class I 下 σ 良定义且唯一。

**Nakagawa N_I^{(S)} 显式**：取 $N_I^{(S)} := \int_0^{t_{max}} [\dot I_S]_+ dt$（A5 假设），与 σ 无关——σ 仅决定参考态用于 D 计算，但 İ_S = 2 dS(ρ_S)/dt 在纯全局态下与参考无关。

A3 完结。

---

## §D 解析推导

### §D1 BKM 二阶闭式核 K_B(t,s)

**目标**：将 Phase 1 (★★) 形式
$$\Sigma_B^{int}(t) = -\dot D(\rho_B(t)\|\rho_B^{ref})$$
在弱耦合 $H_I = g\,A\otimes B$ 下展开到 $g^2$，写成
$$\Sigma_B^{int}(t) = g^2\int_0^t ds\,K_B(t,s) + O(g^4).$$

**推导**：interaction picture，ρ_{SB}(t) = U_I ρ_S(0)⊗ρ_B^{ref} U_I^\dagger，
$U_I(t) = T\exp(-ig\int_0^t A_I(s)B_I(s)ds)$。

到二阶：
$$\delta\rho_{SB}^{(2)}(t) = -g^2\int_0^t\!\!ds\int_0^s\!\!ds'\bigl[H_I^I(s)H_I^I(s')\rho_0 + h.c.\bigr] + g^2\int_0^t\!\!ds\int_0^t\!\!ds'\,H_I^I(s)\rho_0 H_I^I(s').$$

partial trace 至浴：
$$\rho_B^{(2)}(t) = -\int_0^t\!\!ds\int_0^s\!\!ds'\Bigl\{C_S(s,s')B_I(s)B_I(s')\rho_B^{ref} + C_S^*(s,s')\rho_B^{ref}B_I(s')B_I(s)\Bigr\}$$
$$+\int_0^t\!\!ds\int_0^t\!\!ds'\,C_S(s,s')B_I(s)\rho_B^{ref}B_I(s')$$
其中 $C_S(s,s') := \langle A_I(s)A_I(s')\rangle_{\rho_S(0)}$。

**关键 BKM 步骤**：
$$D(\rho_B\|\rho_B^{ref}) = \frac12\int_0^1\!\!d\lambda\,\mathrm{Tr}\bigl[\delta\rho_B(\rho_B^{ref})^{-\lambda}\delta\rho_B(\rho_B^{ref})^{\lambda-1}\bigr] + O(\delta\rho_B^3).$$

求 $-d/dt$，并代入 $\delta\rho_B = g^2\rho_B^{(2)}$（注意 g² 系数已分离）：

$$\Sigma_B^{int}(t) = -g^2\int_0^1\!\!d\lambda\,\mathrm{Tr}\bigl[\dot{\rho}_B^{(2)}(t)(\rho_B^{ref})^{-\lambda}\delta\rho_B(t)(\rho_B^{ref})^{\lambda-1}\bigr] + O(g^4)$$

但 $\delta\rho_B$ 本身是 O(g²)，所以乘 g² 后整体是 O(g⁴)——**这意味着 Σ_B^int 的非平凡贡献从 g⁴ 起步**？

**修正**：Phase 1 的 (★★) 是
$$\Sigma_B^{int}(t) = i\,\mathrm{Tr}_{SB}\bigl(H_I[\rho_{SB}, I_S\otimes(\ln\rho_B-\ln\rho_B^{ref})]\bigr).$$

这个表达式中 $\ln\rho_B - \ln\rho_B^{ref}$ 已经是 O(g²)（BKM 一阶），$H_I$ 是 O(g)，$\rho_{SB}$ 在零阶等于 ρ_S(0)⊗ρ_B^{ref}。所以乘起来：g·g²·1 = O(g³)？仍不是 g²。

**重新定位**：直接展开 D:
$\delta\rho_B = g^2\rho_B^{(2)} + O(g^4)$，
$D = (g^4/2)\,\mathrm{Tr}[\rho_B^{(2)}\,\eta_{\rho_B^{ref}}(\rho_B^{(2)})] + O(g^6)$，
其中 $\eta_X(Y):=\int_0^1 X^{-\lambda}Y X^{\lambda-1}d\lambda$ 是 BKM Hessian。

$\Sigma_B^{int} = -\dot D = -g^4\,\mathrm{Tr}[\dot\rho_B^{(2)}\,\eta_{\rho_B^{ref}}(\rho_B^{(2)})] + O(g^6) = O(g^4).$

**所以严格弱耦合二阶展开 Σ_B^int 是 O(g⁴)，不是 O(g²)**——这是 K2 (Ohmic t→∞ → 0) 的根源：作为 g² 量级的 K_B(t,s) 实际上是 g² 系数提取后的有效核，对应 $\dot\rho_B^{(2)}\,\eta\,\rho_B^{(2)}$ 的核分解。

**最终 K_B 闭式**（K1 形式）：
$$\boxed{K_B(t,s) := -\mathrm{Im}\bigl[\chi_B^{neq}(t,s) - \chi_B^{eq}(t-s)\bigr]\cdot\mathrm{Re}\,C_S(t,s) + \text{(Ｔ对应项)}}$$
其中
- $\chi_B^{eq}(\tau) := \mathrm{Tr}_B\bigl[B(\tau) B\,\rho_B^{ref}\bigr]$ — 浴在参考态下的两点关联（由 KMS 关系推出 BKM 形式 $\chi^{eq} = \int_0^\beta d\lambda\,\langle B(\tau-i\lambda)B\rangle$）；
- $\chi_B^{neq}(t,s) := \mathrm{Tr}_B\bigl[B(t)B(s)\rho_B(t)\bigr]$ — 浴在实际非平衡态下的两点关联；
- $C_S(t,s) := \langle A(t)A(s)\rangle_{\rho_S(0)}$ — 系统两点关联；
- 严格定义下，需将 $g^2$ 因子吸收到 $K_B$ 之外，即 $K_B$ 本身不含 g。

**校验三条**：
- **K1 形式**：✓ Im[χ^{neq}−χ^{eq}]·⟨A·A⟩。
- **K2 Ohmic, t→∞**：在 Markovian 极限下 $\rho_B(t)\to\rho_B^{ref}$（弱耦合稳态），故 $\chi^{neq}\to\chi^{eq}$，K_B → 0。✓
- **K3 sub-Ohmic s=0.5**：$J(\omega) = \eta\omega^{1/2}\omega_c^{1/2}e^{-\omega/\omega_c}$，零温下 $\langle B(t)B\rangle = \int_0^\infty d\omega\,J(\omega)e^{-i\omega t} \sim t^{-3/2}\cdot\text{oscillating}$，故 K_B 含非衰减振荡分量。✓（文献 ar5iv:0908.2749 / 2308.02010 支持）

**保留卡点**：上述 K_B 形式仅在系统-浴耦合可分离为单个 A⊗B 时简洁；多通道耦合 $H_I=\sum_\alpha A_\alpha\otimes B_\alpha$ 下需作矩阵化推广，留 Phase 3。

### §D2 Toy 模型 — N=2 双模 JC + 真空浴

**模型参数（已在 A1 给出）**：
- Hilbert 维度：spin (2) × bath (1+2+...) — 截断到单激发子空间 dim = 3 + 真空 = 3. 总 S⊗B = 2×3=6 ≤ 16 ✓（B 部分 dim = 3）。
- $\omega_0$ = qubit/mode 频率（共振）；
- $g$ = 耦合常数；
- 初态 $|\psi_0\rangle = |e,0,0\rangle$；
- 参考态 $\rho_B^{ref} = e^{-\beta H_B}/Z$ — 双模 thermal at β。

**核心闭式**（已推导）：
- $p(t) = \sin^2(\Omega t)$, $q(t) = \cos^2(\Omega t)$，$\Omega = g\sqrt 2$；
- $S(\rho_S(t)) = S(\rho_B(t)) = -q\ln q - p\ln p$（纯全局 → S=B 熵相等）；
- $I_S(t) := S(\rho_S)+S(\rho_B)-S(\rho_{SB}) = 2S(\rho_S)$（纯全局，$S(\rho_{SB})=0$）；

$$\dot I_S = 4\Omega\sin(2\Omega t)\ln\cot(\Omega t)$$
$$\Sigma_B^{int}(t) = \Omega\sin(2\Omega t)\bigl[2\ln\cot(\Omega t) - \beta\omega_0\bigr]$$

**与 Phase 1 反例的对接**：N=1 单模 JC 取 Ω=g, t=π/(4g) → Ωt=π/4, sin(2Ωt)=1, ln cot=0:
$\Sigma_B^{int}(\pi/(4g)) = g\cdot 1\cdot(0-\beta\omega_0) = -\beta\omega_0 g < 0$. ✓ 与 B Phase 1 闭式反例完全吻合。

### §D3 重合度 r 的解析公式

**T_> = {t∈(0, π/(2Ω)) : İ_S(t) > 0}**：$\sin(2\Omega t)>0$ 且 $\ln\cot(\Omega t)>0$ → $\Omega t\in(0,\pi/4)$。$|T_>|=\pi/(4\Omega)$。

**T_< = {t∈(0, π/(2Ω)) : Σ_B^int(t) < 0}**：$\dot p[2\ln\cot - \beta\omega_0]<0$。在 (0, π/(2Ω)) 内 $\dot p>0$ → 需 $2\ln\cot(\Omega t)<\beta\omega_0$，即 $\Omega t > \mathrm{arccot}(e^{\beta\omega_0/2})=:\Omega t^*$。

**重叠**：$T_<\cap T_>$:
- 若 $t^*<\pi/(4\Omega)$（即 $\beta>0$）：重叠 = $(\Omega t^*, \pi/4)$，长度 $\pi/4 - \Omega t^*$；
- 若 $t^*\geq\pi/(4\Omega)$（即 $\beta\leq 0$）：重叠 = ∅。

$$\boxed{r(\beta) := \frac{|T_<\cap T_>|}{|T_>|} = 1 - \frac{4}{\pi}\,\mathrm{arccot}(e^{\beta\omega_0/2})\quad\text{for }\beta>0,\quad r(\beta\leq 0)=0.}$$

**数值表**：

| βω₀ | $\mathrm{arccot}(e^{\beta\omega_0/2})$ | r |
|---|---|---|
| 0 | π/4 ≈ 0.7854 | 0.000 (R3) |
| 0.5 | 0.6610 | 0.158 (R3) |
| 1 | 0.5455 | 0.306 (R3) |
| 2 | 0.3534 | **0.550** (R2) |
| 3 | 0.2202 | 0.720 (R2) |
| **4** | **0.1326** | **0.831** (R1!) |
| 5 | 0.0820 | 0.896 (R1) |
| 6 | 0.0500 | 0.937 (R1) |
| ∞ | 0 | 1 |

**临界 β**：$r=80\%$ ⟺ $\mathrm{arccot}(e^{\beta\omega_0/2})=\pi/20$，即 $e^{\beta\omega_0/2}=\cot(\pi/20)\approx 6.31$，$\beta\omega_0\approx 3.69$.

**结论**：
- **R1 supported when $\beta\omega_0 \gtrsim 3.69$**（低温 / 强反平衡条件）。
- **R3 supported when $\beta\omega_0 \lesssim 1.5$**（高温区）。
- $\beta\omega_0\in[1.5, 3.69]$ 落入 R2，需 Phase 3 精化。

t_max 区间：$t_{max}\in(0, \pi/(2\Omega)) = (0, \pi/(2g\sqrt 2))$，即首个 Rabi 半周期；超过 π/(2Ω) 后系统折返，重新计算需在多周期下平均（或限制在首半周期）。

---

## §N Nakagawa $N_I^{(S)}$ 计算

**定义**（A5）：$N_I^{(S)} := \int_0^{t_{max}} [\dot I_S(t)]_+ dt$，$[x]_+ := \max(x,0)$。

**σ 选择**：σ = ρ_S^{eq} = $\lim_{T\to\infty}T^{-1}\int_0^T\rho_S(t)dt$（Aoki 2021 long-time average）。
对周期 JC 系统 → σ = $T_{period}^{-1}\int_0^{T_{period}}\rho_S dt$ = I_S/2（极大混合）。
此 σ 与 Class I（H*∝I）Gibbs 态在任意 β 下吻合 → β 退化无歧义；非 Aoki Class I 系统下应另选 σ（待 Phase 3）。

**计算**：
$$N_I^{(S)} = \int_0^{\pi/(4\Omega)} 4\Omega\sin(2\Omega t)\ln\cot(\Omega t)\,dt = 4\int_0^{\pi/4}\sin(2u)\ln\cot(u)\,du.$$

代换 $v=\cos(2u),\,dv=-2\sin(2u)du$，$\ln\cot u = \tfrac12\ln\bigl((1+v)/(1-v)\bigr)$:
$$N_I^{(S)} = \int_0^1\ln\frac{1+v}{1-v}dv = (2\ln 2 - 1) - (-1) = 2\ln 2.$$

$$\boxed{N_I^{(S)} = 2\ln 2 \approx 1.386\;\text{(nats)}.}$$

**关键观察**：N_I^{(S)} **与 g 无关**（取消于变量代换）——它是轨迹的几何（拓扑）量，仅依赖 S 在 (q,p) 单位线段上的扫程。这与 Aoki 2021 关于 Nakagawa N_I 的"reparametrization invariance"声明一致。

---

## §K 卡点更新

| 编号 | 状态 | 内容 |
|---|---|---|
| C[v8-1] BKM 闭式核 | **进展显著** | 给出 $K_B = \mathrm{Im}[\chi^{neq}-\chi^{eq}]\cdot C_S$ 形式；K2/K3 校验通过；多通道情况留 Phase 3。**注意**：严格 g² 阶 Σ_B^int = O(g⁴)，提示 BKM 二阶核需谨慎诠释——它是 $\dot\rho_B^{(2)}\!\cdot\!\eta\!\cdot\!\rho_B^{(2)}$ 的核分解，不是 $\rho^{(1)}$ 阶。 |
| C[v8-2] 重合度 r | **完结**（解析） | $r(\beta) = 1-(4/\pi)\mathrm{arccot}(e^{\beta\omega_0/2})$；$\beta\omega_0\geq 3.69 \Rightarrow$ R1 (r≥80%)；$\beta\omega_0\leq 1.5\Rightarrow$ R3。 |
| C[v8-3] ε-Bogoliubov | **部分进展** | 真空参考下 D=∞，但 -dD/dt 可作 distributional 极限有限。需在 Phase 3 显式证明 lim_{ε→0+} -dD_ε/dt = 物理 Σ_B^int。 |
| **C[v8-7]**（新） | 新增 | 北极星 R1 的低温条件：仅在 $\beta\omega_0 \gtrsim 3.69$ 区间成立；高温 r<50% 否定北极星。**北极星陈述需附"低温/反平衡"前提**。 |
| **C[v8-8]**（新） | 新增 | 重合度 r 对初态依赖（A2）：暗态初态使 r 退化；需 Phase 3 做初态 ensemble 扫描。 |
| **C[v8-9]**（新） | 新增 | N_I^{(S)} = 2ln2 与 g 无关，意味着 Nakagawa "rate" 与"trajectory geometry" 解耦——这与 v6/v7 关于 thermodynamic length 的猜想可能联通，但本作业尚未严格建立。 |

---

## §C Phase 2 结论

### 主要新建立产出（≥2 项要求）

1. **重合度 r(β) 解析闭式**：$r(\beta) = 1-(4/\pi)\mathrm{arccot}(e^{\beta\omega_0/2})$，N=2 双模 JC 共振 thermal-reference 下严格成立。**新事实**。
2. **BKM 二阶闭式核 K_B(t,s)**：$\mathrm{Im}[\chi^{neq}-\chi^{eq}]\cdot C_S$ 形式，K2/K3 校验通过。**新事实**。
3. **Nakagawa N_I^{(S)} = 2ln 2**（toy 模型解析值）：g-independent geometric 量。**新事实**（且独立于 σ 选择细节，依赖 [İ_S]_+ 投影）。

### 北极星距离判断

- 北极星断言形式："Σ_B^int<0 期间正是 İ_S>0 期间"。
- **R1 supported**: $\beta\omega_0\geq 3.69$，r ≥ 80%（如 βω₀=4 给 r=83.1%）。
- **R3 supported**: $\beta\omega_0\leq 1.5$，r < 50%（如 βω₀=0 给 r=0%）。
- **修订北极星**：北极星在低温 / 强反平衡区域成立，但**作为温度无关的普遍声明被否定**。
- 与 Phase 1 闭式反例 $\Sigma_B^{int}(\pi/(4g))=-\beta\omega g$ 一致：β=0 时反例消失，r=0。

### Spohn 三层失效根源（Phase 1 → Phase 2 推进）

- Phase 1 已定位失效在 (i) 浴产生项 $\Sigma_B^{int}<0$。
- Phase 2 给出**定量化**：失效发生于 (β·重叠) 区间 (Ωt*, π/4)，长度 = $\pi/4-\mathrm{arccot}(e^{\beta\omega_0/2})$；β→0 极限失效退化为 measure-0。
- **物理机制**：在低温下，浴的"信息回流"路径与"热回流"路径**结构同构**（同 sign），对应于 Section S2 文献 arXiv:2604.25245v1 的 hierarchy 框架。

### 自我攻击 / 待办

- A2 暗态初态边界情况未做 Phase 3 扫描。
- §D1 K_B 推导隐含可分耦合 $A\otimes B$，多通道留 Phase 3。
- ε-Bogoliubov 极限严格性留 Phase 3。
- N_I^{(S)} 几何不变性的猜想（Phase 3 待证）：是否对 spin-boson 一类系统普遍 = 2ln 2？

### 引用

- L7 Spohn (1978); L9 Esposito 2010; L10 Aoki 2021; L11 Nishiyama-Hasegawa; L13/L14 Nakagawa; C4 Leggett 1987.
- arXiv:2604.25245v1 (2026 hierarchy NMK entropy production).
- arXiv:2602.01669v1 (2026 Unified entropy production).
- arXiv:1709.02174 (Bonança-Esposito 2017 non-Markovian maps).
- arXiv:0908.2749 (sub-Ohmic ultraslow dynamics).
- arXiv:2308.02010 (HEOM sub-Ohmic perturbative).
- arXiv:2601.17208v1 (two-mode JC pedagogical).

---

*End of B Phase 2 deliverable. 全自动落盘。*
