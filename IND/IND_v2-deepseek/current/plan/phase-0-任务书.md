# Phase 0 任务书 — v10-Scrambler

> 类型：A 型（解析前置）
> 主攻：C[v8-3] ε-Bogoliubov 退化谱正则化
> 目标：移除 v9-K8 的"ε→0 平滑收敛"假设；为 Phase 1 显式幺正 U 构造扫清障碍

---

## 〇、为什么是前置 Phase

v9-K8 收官时含限定前提："**假设 ε→0 极限下 Bogoliubov 分解平滑收敛**，谱交叉点正则化由 v10 / C[v8-3] 处理"。AUDITOR 严重项 #1。NS-1 的 frozen dark sector 严格性依赖此正则化——若 ε-Bogoliubov 极限不存在或不收敛，"frozen dark sector"可能是 ε 依赖的伪相图。

---

## §0 推导目标（一句话，可证伪）

**目标**：在 ε-Bogoliubov 正则化（ρ_B^ε := (1−ε)·ρ_B + ε·I/d_B）下，证明：
$$\lim_{\varepsilon\to 0^+} \Sigma_B^{int,\varepsilon}(t) = \Sigma_B^{int}(t)$$
作为 distributional 极限或在适当函数空间内的等价类，对 v9 toy（N=2 双模 JC 共振+真空+对称耦合）+ N_q≥2 普适推广均成立。

**可证伪声张**：
- **R0（强）**：ε→0 极限是 distributional 强收敛（pointwise a.e. + L¹ 控制）；ρ_B 退化谱处的 ln ρ_B 奇异性在 sin(2u)·ln cot u 形态下被 sin(2u) 的零阶因子压回有限——∫ 良定义且 = ln 2
- **R1（弱）**：ε→0 极限仅在 distributional 意义下良定义；若取 ε→0⁺ 序列依赖（如 ε ∝ u² vs ε ∝ u⁴），积分可能引入 O(ε ln ε) 残差
- **R2（否定）**：ε-正则化方案依赖性破坏 N_I^{(S)} = 2 ln 2 的精确性 → v9-K1 在严格意义下需修正

---

## §1 强制撞墙

A 必须先回答：

1. **退化谱位置识别**：ρ_B(u) 在 u=0 (ρ_B=|0⟩⟨0| 纯态) 与 u=π/2 (ρ_B=|B⟩⟨B| 纯态) 退化；u∈(0, π/2) 内全秩。退化 measure-zero（端点两点），其余区间良定义
2. **ln ρ_B 在 u=0+ε 的展开**：q=cos²u≈1−u²，p=sin²u≈u²；ln q≈−u²，ln p≈2 ln u（log 发散）
3. **被积式 sin(2u)·ln cot u 在 u→0+ 形态**：sin(2u)≈2u，ln cot u = −ln tan u ≈ −ln u（log 发散）；积分 sin(2u)·ln cot u·du ≈ 2u·(−ln u)·du = −2u ln u du——u→0+ 时 −u ln u → 0（log 可积）
4. **ε 正则化路径**：ρ_B^ε(u) = (1−ε)·ρ_B(u) + ε·I/2；谱 q^ε = (1−ε)·q + ε/2, p^ε = (1−ε)·p + ε/2；ε→0+ 时 q^ε → q, p^ε → p；端点 u=0 时 q^ε = 1−ε/2, p^ε = ε/2 → 0；ln p^ε ≈ ln(ε/2)（ε→0 发散但有限 ε 良定义）

撞墙后 A 必须显式判断：R0 / R1 / R2 哪个被支持？

---

## §2 假设

- A1（v9-K1）：dS_q/du = 2·sin(2u)·ln cot u 精确恒等式（在 u∈(0, π/2) 内严格）
- A2（v9-K8）：N_I^{(S)} = 2 ln 2 含 ε→0 平滑收敛假设
- A3（标准）：log 可积性 ∫₀^δ |u ln u| du < ∞ 对任意 δ > 0
- A4（标准）：dominant convergence theorem / monotone convergence theorem（Lebesgue）
- A5（外部 XK21 arXiv:2603.01861 Local approach 2026）：绕过参考态退化的局域方法

---

## §3 禁区

不重复建立 v9-K1~K8 / v8-K1~K10。

**必须**新建立 ≥ 1 项：
1. **R0 严格证明**：ε→0 极限存在且 = 2 ln 2，给出 distributional 收敛阶
2. **R1 反例构造**：找到一个 ε(u) 序列使 ∫_ε ≠ 2 ln 2 的极限（若存在则 R0 否定）
3. **R2 否定构造**：证明 N_I^{(S)} 的"精确恒等式"在严格 ε→0 意义下需修正

---

## §4 工作流（强制）

§S 文献检索（≤ 3 条 WebSearch）：
- "Bogoliubov dilation regularization quantum mechanical observable"
- "log singularity entropy production zero temperature regularization"
- arXiv:2603.01861 Local approach 2026 引文链

§0.5 假设清单
§1 撞墙（4 攻击全处理）
§D 推导：
- D.1 退化谱位置 + measure-zero 论证
- D.2 sin(2u)·ln cot u 的 log 可积性严格证明
- D.3 ε-Bogoliubov 极限收敛性（dominant convergence theorem 应用）
- D.4 ε(u) 序列依赖性测试（u² / u⁴ / e^{−1/u} 三种 ε(u)）
- D.5 v9-K8 假设的严格性裁决（R0 / R1 / R2 哪个）
§K 卡点
§C 结论

---

## §5 输出路径

A：`current/A/phase-0-output.md`，标题 `## A作业 v10 Phase 0 — ε-Bogoliubov 正则化关闭 C[v8-3]`
B：`current/B/phase-0-output.md`（独立推导，禁止读 A 与项目文件）

---

## §6 A 简略质检 B v9 Phase 2（已知双路对齐+1 张力 PI 已裁决，仅写"B v9-P2 形式核验：完全对齐+张力已 PI 裁决"）

---

▶️ 任务书完。
