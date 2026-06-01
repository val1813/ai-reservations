# Phase 2 任务书 — v8-Backflow

> 类型：B型（数值+解析双轨）
> 北极星距离：v8 Phase 1 锚定形式判据+反例+passive criterion；Phase 2 攻数值重合度+BKM闭式核
> 主攻卡点：C[v8-2]（强映射重合度）+ C[v8-1]（BKM二阶闭式核）
> 次目标：C[v8-3]（退化谱正则化）部分推进

---

## 〇、北极星距离检查（强制）

| 维度 | Phase 1 后状态 | Phase 2 目标 |
|------|---------------|-------------|
| Σ_B^int 形式判据 | ✅ v8-K1 (★★) 形式 | 维持 |
| Σ_B^int<0 存在性 | ✅ v8-K3 N=1 JC闭式反例 | 推广到 N=2/N=3 解析+趋势外推到 N=15-30 |
| Spohn 三层失效 | ✅ v8-K2 | 维持 |
| Σ_B^int 与 N_I^{(S)} 重合 | ⚠️ 仅形式蕴含 | **本Phase核心**：可解析检验的具体重合度判据 |
| Σ_B^int 充分不可能条件 | ✅ v8-K6 passive | 检验 K6 在数值反例中是否被遵守 |
| BKM 二阶核 | ❌ 未闭式 | **本Phase核心**：闭式核 K(t,s) |

---

## §0 本Phase推导目标（一句话，可证伪）

**主目标P[v8-2]**（强映射方向）：在解析可计算 toy 模型（JC双模/N=2 spin-boson/Rabi-spin-boson）中，量化 Σ_B^{int}<0 时间窗口与 Nakagawa N_I^{(S)}>0 时间窗口的重合度 r(t_max)。

**可证伪声张**：
- **R1（强）**：在至少一个 toy 模型中，重合度 r ≥ 80%（窗口完全或近完全重合）⟹ 北极星方向"浴熵产生 = 信息回流记账项"获得正面证据
- **R2（中）**：r ∈ [50%, 80%] ⟹ 部分重合，需要 Phase 3 更精细判据
- **R3（否定）**：r < 50% 或重合度系统性依赖于 toy 模型选择 ⟹ 北极星受到挑战，需要修正或转向

**次目标P[v8-1]**（BKM二阶核）：构造 Σ_B^{int}(t) 的 Bogoliubov-Kubo-Mori 二阶（弱耦合）闭式核 K_B(t,s)，使
$$\Sigma_B^{int}(t) = g^2 \int_0^t ds\, K_B(t,s) + O(g^4)$$
其中 K_B 仅依赖浴侧自相关函数 + 系统侧 cumulant。

**可证伪声张**：
- **K1**：K_B(t,s) 可写成 Im[χ_B^{neq}(t,s) − χ_B^{eq}(t-s)] · ⟨A_S(t)A_S(s)⟩_S 形式，其中 χ_B^{neq/eq} 是非平衡/平衡浴 susceptibility
- **K2**：K_B(t,s) 在 Ohmic 浴下的 t→∞ 极限给出 Σ_B^{int}^{∞} = 0（与热化极限相容）
- **K3**：K_B(t,s) 在 sub-Ohmic s=0.5 下出现非衰减振荡核（与 Nakagawa α≈1/2 边界形式一致）

**次目标P[v8-3]**（退化谱正则化）：证明 ε-Bogoliubov 极限 lim_{ε→0⁺} Σ_B^{int,ε} = Σ_B^{int}（其中 ρ_B^ε := (1-ε)ρ_B + ε I/d_B）的良定义性。

---

## §1 强制撞墙（推导开始前完成）

B 必须先回答以下三个最强攻击：

1. **Toy 模型可数值反例**：对 N=2 双 HO-spin-boson 模型（spin + 两模式 Ohmic 浴 + 截断到 Fock-3），能否手工计算 ρ_B(t) 的全谱演化？如果不能解析得到 ρ_B(t)，是否能给出**下界估计** Σ_B^{int}(t) 的某个 sign 判据？
2. **r(t_max) 的依赖问题**：r 显然依赖于 t_max（积分上限）和模型参数；能否给出 r 的**渐近** t_max → ∞ 极限？该极限是否独立于初态选择？
3. **N_I^{(S)} 的定义二义性**：Nakagawa N_I 的定义需要选择 reduced sector R 与参考态 σ。在 spin-boson 中标准选择 R=S, σ=ρ_S^{Gibbs}，但 ρ_S^{Gibbs} 在 H*∝I 的 Class I 下退化（H*∝I ⟹ ρ_S^{eq} 由 H_S 决定）。这个选择对 N_I^{(S)} 的影响是什么？

撞墙后，B 必须显式判断这3个攻击中哪些被推导化解、哪些转化为本Phase 卡点继承。

---

## §2 原始假设列表（B 可使用）

A1（v5-K6）：Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt − Σ_B^{internal}（精确恒等式）
A2（v8-K1）：Σ_B^{int}(t) = −d/dt D(ρ_B(t)‖ρ_B^{ref}(β))（精确浴侧表达式）
A3（v8-K2）：Spohn 三层在有限维全局幺正下失效
A4（v8-K6）：Σ_B^{int}<0 ⟹ ρ_B 非passive + modular flow 与 H_I 失锁相
A5（外部 L13/L14）：Nakagawa N_I = ∫_0^t [İ(s)]_+ ds, I = −D(ρ_R(t)‖σ)
A6（外部 L11 Nishiyama-Hasegawa）：瞬时参考 β*_t 思路
A7（外部 L9 Esposito 2010）：Σ_total = D(ρ_SB‖ρ_S⊗ρ_B^eq)（全局形式）

---

## §3 禁区（不重复建立）

不得作为新结论引用：v8-K1~K6（仅可调用）；v5-K6；v3-K10；v4-K3；v6-K1~K4；v7-K1。

**必须**新建立的结构性产出（任意一项视为完成，三项中至少二项必须）：
1. **重合度数值/解析量化**：在至少一个 toy 模型中给出 r(t_max) 的解析或半解析数值
2. **BKM 二阶闭式核**：K_B(t,s) 的显式公式 + 至少一个浴谱（Ohmic 或 sub-Ohmic）下的求值
3. **退化谱正则化**：ε→0⁺ 极限收敛性证明（至少形式证明）

---

## §4 相关 K 条目列表（B 可引用）

| K | 内容 | 级别 |
|---|------|------|
| **v8-K1** | Σ_B^{int} = −d/dt D(ρ_B‖ρ_B^{ref}(β)) | ⚠️L2 |
| **v8-K3** | N=1 JC 闭式反例 | ⚠️L2 |
| **v8-K4** | Nakagawa structural-domain 失效 | ⚠️L2 |
| **v8-K6** ⭐ | passive 充分不可能条件 | ⚠️L2 |
| v5-K6 | 精确恒等式 | ✅L2 |

---

## §5 知识库前置检查（强制）

- 引用 Nakagawa N_I 时必须显式标注 reduced sector R 与参考态 σ
- 引用"r(t_max) 重合度 ≥ X%" 类声张时必须给出 r 的精确定义（time-fraction / weighted Lebesgue measure / 其他）
- 引用 BKM 内积时必须给出该内积在浴 Hilbert 空间的具体定义（"Mori-Lippmann inner product" 或类似）
- 引用 toy 模型解析解时必须给参数+truncation+误差量级

---

## §6 文献库参考条目

- L7 Spohn 1978
- L9 Esposito 2010 NJP 12, 013013
- L11 Nishiyama-Hasegawa arXiv:2602.01669（瞬时参考 β*_t）
- L13 Nakagawa structural theorem arXiv:2602.09054
- L14 Nakagawa unifying revivals arXiv:2601.18822
- L10 Aoki 2021 PRA 103, 052208 / arXiv:2103.05308
- L12 Buscemi-Schindler-Strasberg arXiv:2404.15915
- C4 Leggett 1987 RMP 59, 1（spin-boson）

---

## §7 声张与可证伪预测

| 声张 | O级 | 可观测/可证伪条件 | 校准方法 |
|------|-----|-------------------|---------|
| R1（重合度 r≥80%）| O3 toy | JC双模 / N=2 spin-boson 解析或半解析 | 算 r(t_max) |
| K1（BKM 核形式）| O4 | K_B = Im[χ^{neq}-χ^{eq}]·⟨A·A⟩ | 解析推导 |
| K2（Ohmic t→∞ 极限）| O4 | K_B^{Ohmic}(t→∞)=0 | 渐近展开 |
| K3（sub-Ohmic 振荡核）| O4→O3 | K_B^{s=1/2} 含非衰减振荡 | sub-Ohmic 谱代入 |

---

## §8 北极星距离与最长卡点压力（强制）

最长开放卡点：C1(v5)（6 Phase 活跃）+ C[v8-2]（0 Phase，本Phase 主攻）

**本Phase 是否直接攻击最长卡点**：
- C[v8-2] 是 Phase 2 主目标 ✅
- C1(v5) 间接被 v8-K1 推进（modular flow 表示）但未实质关闭——本Phase 不直接攻；若 Phase 3 仍未关闭则按 Codex SOP 必须降级为原则性限制或下一驱动矛盾

---

## §9 工作流（B 强制按以下顺序）

1. **§S 文献检索**（≥3 条独立检索）
   - "Bogoliubov-Kubo-Mori inner product entropy production"
   - "Nakagawa backflow time window coincidence"
   - "spin-boson sub-Ohmic finite N exact diagonalization"
2. **§A 撞墙**（三攻击全部处理）
3. **§D 解析推导**：
   - **D1 BKM 核**：从 v8-K1 (★★) 形式出发，弱耦合二阶展开 ρ_B(t) = ρ_B^{ref} + g²·ρ_B^{(2)}(t)，求 K_B(t,s)
   - **D2 Toy 模型**：选 JC 双模 / N=2 spin-boson / Rabi-spin-boson 中的一个，给 ρ_SB(t) 的截断解析解（Hilbert 维度 ≤ 16）
   - **D3 重合度 r**：定义 r := |T_<∩T_>|/|T_<|，T_< := {t : Σ_B^{int}(t)<0}, T_> := {t : İ_S(t)>0}；给 r 的具体数值/解析下界
4. **§N Nakagawa N_I^{(S)} 计算**：选 R=S, σ=ρ_S^{eq}（ρ_S^{eq} 取定义清楚的初态 long-time average 或 Gibbs），算 İ_S(t)
5. **§K 卡点更新**
6. **§C 本Phase 结论**

---

## §10 输出路径

B 推导：`D:\Claude\ai-reservations\v2-deepseek\current\B\phase-2-output.md`
标题：`## B作业 Phase 2 — Σ_B^int<0 与 N_I^{(S)}>0 重合度 + BKM二阶闭式核`

---

## §11 A 同时执行的任务

A 在 Phase 2 同时执行：
1. A 自己的正规推导任务（**简化版**）：给 Σ_B^{int} 在**纯解析视角**下的 BKM 二阶展开（与 B 数值/toy 路径互补）
2. A 对 B 的 Phase 1 作业的质检报告（B 已完成 Phase 1，A 现在须做质检）

A 输出：`D:\Claude\ai-reservations\v2-deepseek\current\A\phase-2-output.md`

---

▶️ 任务书完。
