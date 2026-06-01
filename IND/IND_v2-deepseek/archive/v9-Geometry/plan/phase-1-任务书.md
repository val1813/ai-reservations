# Phase 1 任务书 — v9-Geometry

> 类型：A 型（解析推导，纯几何）
> 北极星：N_I^{(S)} = 2 ln 2 几何身份裁决
> 主攻：候选身份 (a) Crooks-Sivak length / (b) Berry-Uhlmann winding / (c) Holevo accessible information / (d) toy 数值巧合 — 三选一+排除

---

## 〇、北极星距离检查

| 维度 | 状态 |
|------|------|
| v8-K9 形式 | ✅ 已知：4∫₀^{π/4} sin(2u)·ln cot u·du = 2 ln 2（u=Ωt，Ω=g√2） |
| 路径量 vs 信息量同构 | ❌ 未裁决（v9 Phase 1 主攻） |
| 多模 N_q ln 2 普适 | ❌ 未验证（v9 Phase 2） |
| Bures-Uhlmann 度规对应 | ❌ 未计算（v9 Phase 1 第一步） |

---

## §0 本Phase 推导目标（一句话，可证伪）

**目标**：在 N=2 双模 JC 共振+真空+对称耦合的轨迹 ρ(u) 上，显式计算 Bures-Uhlmann 度规线元 ds²(u)、Fisher 信息度规 F(u)、Berry connection ⟨ψ(u)|i∂_u|ψ(u)⟩，比对被积式 sin(2u)·ln cot u du，给出 v8-K9 几何身份的初步裁决（候选 a/b/c/d 中至少排除一个）。

**可证伪声张**：
- **R1**：4·sin(2u)·ln cot u = ds²(u)/du 的某种 Bures 长度元 ⟹ (a) thermodynamic length 候选成立
- **R2**：4·∫₀^{π/4} sin(2u)·ln cot u·du = 2π·n（整数 winding）⟹ (b) Berry/Uhlmann winding 候选成立
- **R3**：sin(2u)·ln cot u 的形式无 Bures/Berry 几何对应，仅是 q ln(1/q) + p ln(1/p) 的导数 = 二元熵率 ⟹ (c) Holevo/dimension counting 候选成立
- **R4**：以上三选一全部失败（无几何对应+多模 N_q ln 2 不普适）⟹ (d) 数值巧合候选成立

至少必须排除其中**一个**候选才算 Phase 1 推进。

---

## §1 强制撞墙（推导开始前）

A 必须先回答：

1. **被积式形状识别**：sin(2u)·ln cot u 在 u∈(0, π/4) 是奇函数 vs 偶函数？根（端点）行为是什么？是否等于已知特殊函数（Catalan β-function / dilogarithm）的导数？写出 indefinite integral 闭式
2. **Bures 度规先验估算**：N=2 JC 单激发子空间内的 ρ(u)=q|0,0⟩⟨0,0|+p|B⟩⟨B|（q+p=1，q=cos²u，p=sin²u），对角态，Bures 度规退化为 Fisher 度规 F(u) = (dp/du)² · [1/(p(1-p))]——展开得 F(u) = 4 sin²(2u) / (sin²u · cos²u) = 16。**度规常数！**
3. **Fisher 度规给的不是 sin(2u)·ln cot u**：Fisher 度规给 ds = 4 du，∫₀^{π/4} ds = π；而 v8-K9 被积式 ∫₀^{π/4} 4·sin(2u)·ln cot u·du = 2 ln 2 ≠ π
4. **形状对比**：被积式 sin(2u)·ln cot u **= dS_q/du** 其中 S_q = q ln q + p ln p 的二元熵——所以 v8-K9 的 N_I^{(S)} = ∫|dS_q/du|·du = S_q(0)−2·S_q(π/4)+S_q(π/2) = 0 − 2·(−ln 2) + 0 = 2 ln 2 ⟹ **本身就是熵 traversal 的 total variation**

撞墙后，A 必须显式判断：v8-K9 的 2 ln 2 是 Fisher 度规积分？Bures 长度积分？还是 q ln q 的 total variation？

---

## §2 原始假设列表（A 可使用）

A1（v8-K9）：N=2 双模 JC 共振+真空+对称耦合下，单激发子空间 dim=3，ρ_B(t) 在 |0,0⟩|B⟩ 子空间秩 ≤ 2，谱 (q,p)=(cos²Ωt, sin²Ωt)
A2（标准）：Bures-Uhlmann 距离 d_B(ρ,σ) = √(2−2 F(ρ,σ)^{1/2})，F = ‖√ρ √σ‖₁²
A3（标准）：对角态 ρ=diag(q,p), σ=diag(q+dq, p+dp)，d_B² = ¼·(dq²/q + dp²/p) = ¼·(dp)²·[1/(p(1−p))]
A4（标准）：Fisher 信息度规 F(u) = ∑_i (dp_i/du)²/p_i = (dp/du)² · [1/p + 1/q]
A5（标准）：Berry connection 沿 |ψ(u)⟩ = √q·|e,0,0⟩ − i√p·|g,B⟩ 路径
A6（标准）：Holevo bound χ(E) ≤ S(∑p_i ρ_i) − ∑p_i S(ρ_i) ≤ ln d
A7（v8-K10）：c(β) = −ln cosh(βω₀/2)/(2 ln 2) 在 toy 模型成立

---

## §3 禁区（不重复建立）

不得作为新结论引用 v8-K1~K10 / v5-K6 / v3-K10 / v4-K3 / v6-K1 / v7-K1（仅可调用）。

**必须**新建立至少 1 项：
1. **Bures-Uhlmann 度规对照**：显式 ds²(u) 表达式 + 与 sin(2u)·ln cot u 关系（可能是"无关"的负面结论）
2. **二元熵 total variation 识别**：证明 4∫₀^{π/4} sin(2u)·ln cot u·du = 2·ΔS_q（沿轨迹两端 q=1 → q=1/2 → q=0 的熵 total variation）
3. **Fisher / Berry / Holevo 三框架排除**：至少排除一个候选

---

## §4 工作流（A 强制按以下顺序）

### §S 文献检索（≥3 条独立 WebSearch）
- "Bures-Uhlmann metric two-level system arc length entropy"
- "Crooks-Sivak thermodynamic length quantum two-level"
- "Berry phase Jaynes-Cummings dark state geometric phase"
- "Holevo information accessibility two-qubit identity bound saturation"

### §0.5 隐含假设清单
[逐条列出 A1-A7 在本Phase 是否满足]

### §1 撞墙（三攻击全部处理）

### §D 推导
- **D.1**：sin(2u)·ln cot u 的 indefinite integral 闭式（用 dilogarithm 或基础函数）
- **D.2**：Bures-Uhlmann 度规线元 ds²(u) on ρ(u)=diag(q,p) — 给闭式
- **D.3**：Fisher 信息度规 F(u) — 给闭式
- **D.4**：Berry connection ⟨ψ(u)|i∂_u|ψ(u)⟩ — 给闭式（可能为 0，因实波函数）
- **D.5**：v8-K9 = 2·ΔS_q 的 total variation 识别（用二元熵 S_q = −q ln q − p ln p 的端点值 + monotonic intervals）
- **D.6**：三选一裁决——排除哪个候选

### §K 卡点更新

### §C 本Phase 结论

---

## §5 文献库参考
- L7 Spohn 1978
- L9 Esposito 2010
- L11 Nishiyama-Hasegawa 2026
- L13 Nakagawa 2602.09054
- XK9 Crooks 2007 PRL 99, 100602
- XK10 Sivak-Crooks 2012 PRL 108, 190602
- XK11 Berry-Phase Chirality arXiv:2605.13685
- XK12 Geometric Heat Pump arXiv:2511.16591
- XK14 Bures-Uhlmann 1976

---

## §6 声张与可证伪预测

| 声张 | O级 | 条件 |
|------|-----|------|
| R1 (length 候选) | O4 | 4·sin(2u)·ln cot u = ds²/du 某种几何长度 |
| R2 (winding 候选) | O4 | 2 ln 2 = 2π·n（整数 winding） |
| R3 (Holevo 候选) | O4 | sin(2u)·ln cot u = dS_q/du，2 ln 2 = 2·ΔS_q（total variation） |
| R4 (数值巧合) | O4 | 三选一全部失败 |

---

## §7 输出路径

A 推导：`D:\Claude\ai-reservations\v2-deepseek\current\A\phase-1-output.md`
标题：`## A作业 v9 Phase 1 — Bures-Uhlmann度规 vs sin(2u)·ln cot u 比对 + 三选一裁决`

---

## §8 本Phase 无 B 上次作业
v9 Phase 1 启动后第一个 Phase。A "质检 B" 任务跳过。但作业末尾给"对未来 B 的预判攻击点"。

---

▶️ A 任务书完，直接开始推导，全自动到落盘。
