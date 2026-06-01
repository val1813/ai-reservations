# Phase 2 任务书 — v9-Geometry

> 类型：A 型（解析推广）
> 主攻：C[v9-1] N_q·ln 2 普适性 + C[v9-2] Holevo saturation 显式 + C[v9-3] 端点依赖闭式

---

## 〇、北极星距离

| 维度 | Phase 1 后 | Phase 2 目标 |
|------|----------|------------|
| 三选一身份（toy） | ✅ (c) 支持，(a)(b)(d) 排除 | 维持 |
| 多模 N_q·ln 2 普适 | ❌ | **本Phase核心**（C[v9-1]） |
| Holevo saturating ensemble | ❌ | **本Phase核心**（C[v9-2]） |
| 端点依赖闭式 | ❌ | **本Phase核心**（C[v9-3]） |

---

## §0 推导目标（一句话，可证伪）

**目标**：把 v9-K1~K4 在 N=2 toy 下的几何身份裁决推广到任意 N_q：(I) 计算 N=3, 4 双模 JC 共振+真空+对称耦合（推广到 N_q-mode 单激发对称浴）下的浴熵记账积分；(II) 显式构造 Holevo saturating ensemble；(III) 给出任意端点 T∈(0, π/2) 下 N_I^{(S)}(T) 闭式。

**可证伪声张**：
- **U1（强）**：N_q-mode 对称浴下，单激发对称模 |B_q⟩ = (1/√N_q)·Σᵢ aᵢ†|0⟩，约化态 ρ_B(u) 谱 (q,p) 在 {|0⟩^⊗N_q, |B_q⟩} 子空间，浴熵记账积分 N_I^{(S)} = N_q · ln 2 ⟹ U1 成立 ⟹ Holevo accessible information 同构成立
- **U2（弱）**：N_q-mode 下积分给与 N_q 无关或非线性依赖 ⟹ "动力学路径量"独立于"维数同构"⟹ 候选 (c) 在 N=2 是巧合，普适身份不同
- **S1（Holevo）**：ensemble {(½, |e,0,0⟩), (½, |g,B⟩)} 在 u=π/4 处 χ = ln 2 saturating；前后向半段累计 χ_total = 2 ln 2 = N_I^{(S)} ⟹ Holevo saturation 严格成立
- **E1（端点闭式）**：N_I^{(S)}(T) = 2·[S_q(T) − S_q(0)] = −2·[cos²T·ln cos²T + sin²T·ln sin²T] 闭式

---

## §1 强制撞墙

A 必须先回答：

1. **N_q=3 setup**：H_I = g·σ_+·(a₁+a₂+a₃)/√3 + h.c.，单激发子空间在 |e,0,0,0⟩ 与 |g,B₃⟩ = (1/√3)·(|e†|0⟩...) 两态间。Rabi 频率 Ω_3 = ?；约化态谱是否仍 (cos²Ωt, sin²Ωt)？
2. **是否仍是 single bath excitation 二元谱**？— 关键：对称耦合 g·Σᵢ aᵢ ↔ √N_q g·B 模式（其余模式黑暗），所以 N_q-mode 对称耦合 reduces to N=2 单亮模 + (N_q−1) 黑暗模。**ρ_B 在亮模 |B_q⟩ 上谱 (q,p)，在黑暗模上谱平凡** ⟹ S(ρ_B) 仍 = h₂(p)（二元熵）⟹ N_I^{(S)} 仍 = 2 ln 2，**不**给 N_q·ln 2
3. **若 N_I^{(S)} = 2 ln 2 不依赖 N_q（U2 成立）**：候选 (c) 二元熵 total variation 普适——但与 Hilbert 维数同构 ln dim 在 N_q=2 是巧合（dim=4 时 ln 4 = 2 ln 2）。验证：N_q=3 时维数 = 2^3 = 8（system+3 mode），ln 8 = 3 ln 2；N_I^{(S)} = 2 ln 2 ≠ 3 ln 2 ⟹ **维数同构是 N_q=2 巧合**
4. **Holevo saturation**：单激发对称耦合限制约化态谱在 (q, p) 二元，χ ≤ ln 2 而非 ln d_total；ensemble {(½, |e,0,...,0⟩), (½, |g,B_q⟩)} 在 u=π/4 处 ρ̄ = ½·|e,0⟩⟨e,0| + ½·|g,B_q⟩⟨g,B_q|，χ = S(ρ̄) − Σpᵢ S(ψᵢ) = ln 2 − 0 = ln 2 ✓

撞墙后 A 必须显式回答：U1 vs U2 哪个正确？

---

## §2 假设

A1（v9-K1）：dS_q/du = 2·sin(2u)·ln cot u 精确恒等式
A2（v9-K2~K3）：Bures + Berry candidates 排除（toy）
A3（v9-K4）：Phase 1 三选一裁决（toy）
A4（v8-K1~K10 + v5-K6 + v3-K10 + v4-K3）：禁区，仅可调用
A5（标准）：N_q-mode 对称耦合 g·Σᵢ aᵢ = √N_q · g · B_q（其中 B_q = (1/√N_q)·Σᵢ aᵢ）+ (N_q−1) 黑暗模式
A6（标准）：单激发子空间 = system 2-state ⊗ {|0⟩^⊗N_q, |B_q⟩} 共振 Rabi 振荡
A7（标准）：Holevo bound χ ≤ S(ρ̄) − Σpᵢ S(ψᵢ)，纯 ensemble 时 S(ψᵢ) = 0

---

## §3 禁区

不重复建立 v9-K1~K4 + v8-K1~K10 等。

**必须**新建立至少 2 项：
1. N_q ≥ 3 浴熵记账积分（U1 vs U2 裁决）
2. Holevo saturation 显式 ensemble + χ 计算
3. 端点 T 闭式 N_I^{(S)}(T)

---

## §4 工作流（强制）

§S 文献检索（≤ 3 条）
§0.5 假设清单
§1 撞墙（4 攻击全处理）
§D 推导：
- D.1 N_q=3, 4 setup + 亮模/黑暗模分解
- D.2 ρ_B(u) 谱（亮模二元 + 黑暗模平凡）
- D.3 N_I^{(S)} 计算（U1 vs U2 裁决）
- D.4 Holevo ensemble 显式 + χ 计算
- D.5 任意端点 T 闭式 N_I^{(S)}(T) = 2·[S_q(T) − S_q(0)]
§K 卡点
§C 结论

---

## §5 输出路径

A：`current/A/phase-2-output.md`（标题 `## A作业 v9 Phase 2 — N_q普适+Holevo+端点`）
B：`current/B/phase-2-output.md`（独立推导，禁止读 A 与项目文件）

---

## §6 A 同时质检 B Phase 1（已对齐，仅形式核验）
A 简略写"B Phase 1 形式核验：完全对齐 A，无客观错误"即可。

---

▶️ 任务书完。
