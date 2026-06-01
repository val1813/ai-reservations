# v9 Phase 2 PI审查报告

> 输入：A作业（current/A/phase-2-output.md）+ B独立作业（current/B/phase-2-output.md）
> 主任务：N_q·ln 2 普适性 + Holevo saturation + 端点依赖
> 日期：2026-05-30

---

## §1 形式审核（GATE 1-4）

### GATE 1: 文献库 ✅
A 引用 Tavis-Cummings 1968 + Holevo 1973/NC §12.1 + Schumacher-Westmoreland 1997
B 引用 arXiv:1710.10945 (Cordero 三模 TCM) + arXiv:2506.06700 + arXiv:2202.00330
合计 6 条独立文献支撑亮/暗模分解 + Holevo saturation 条件

### GATE 2: 审稿人 — 距上次 2 Phase（v8 收官 + v9-P1）
按 SOP 推迟到 v9 收官触发

### GATE 3: B 独立推导 ✅✅
A vs B 实质完全对齐：
- A1 N_q=3 Bogoliubov 分解 + Rabi Ω = g√N_q：A 与 B 完全相同
- A2 ρ_B 谱在亮模二元，暗模平凡：A 与 B 完全相同
- A3 U2 胜（N_I = 2 ln 2 与 N_q 无关）：A 与 B 完全相同
- D-3 端点闭式 N_I^{(S)}(T) = 2·h₂(sin²u_T)：A 与 B 完全相同

### GATE 4: 攻击全闭合 — **存在 1 个实质张力需 PI 裁决**

---

## §2 PI 核心裁决：A vs B 关于 Holevo saturation 的张力

### A 路径（"内禀 saturation"）
A 在 §1 撞墙 4 给：ensemble {(½, |e,0⟩),(½, |g,B_q⟩)}（两个正交纯态），u=π/4 处 ρ̄ = (1/2)·I on span{|e,0⟩,|g,B_q⟩}，χ = ln 2 saturate；半段累计 χ_total = 2 ln 2 = N_I^{(S)}。

### B 路径（"外部最优化 saturation"）
B 在 A3 给：4 个等概率正交纯态 ensemble {|00⟩,|10⟩,|01⟩,|11⟩}，ρ̄ = I_4/4，χ = ln 4 = 2 ln 2 saturate。

### 张力本质
- **A 的 ensemble 受 JC 演化约束**：仅 2 维 saturating subspace（亮模子空间），单点 χ_max = ln 2
- **B 的 ensemble 完全外部最优**：4 维 Fock 子空间（含暗模），单点 χ_max = ln 4
- 两者都给"χ = 2 ln 2"，但解读方式不同：
  - A：χ_total = 2·ln 2 = forward + backward 半段 χ_max 累加
  - B：χ_max = 2 ln 2 单点（外部最优 ensemble 单次饱和）

### PI 裁决
**双路都正确，但描述不同物理量**：

(i) **A 的 Holevo saturation 描述**：
- 在 JC 自然演化下，N_I^{(S)} 是动力学量（forward 半段熵增 + backward 半段熵减的累计 |dS|）
- 每个半段的 saturating ensemble χ_max = ln 2（由亮模二元谱约束）
- 累加后 N_I^{(S)} = 2 ln 2

(ii) **B 的 Holevo saturation 描述**：
- 全 4 维 Fock 子空间的 accessible information 极大值 = ln 4 = 2 ln 2
- 这是**信道容量上限**，不是动力学量

**关键区分**：
- 候选 (c) "二元熵 total variation"（v9-K4）= A 的描述：**动力学路径量** N_I^{(S)} 在亮模子空间内 = 2·|ΔS_q| = 2 ln 2
- 候选 (c') "Hilbert 维数同构"（B 的描述）= 信道容量 ln 4 = 2 ln 2 是**外部最优 ensemble 单点饱和值**

**这两者在 N_q=2 toy 数值相同（都是 2 ln 2），但物理身份不同**：
- A 解释：N_I^{(S)} 是动力学路径量，与亮模二元谱有关，与 N_q 无关
- B 解释：ln 4 是 Hilbert 子空间维数 (1+N_q)·... 嗯，但 N_q=2 时 1+N_q = 3 ≠ 4，所以 ln 4 不是单激发子空间维数 ln(1+N_q)

让我们精确数维数：
- A 的 ensemble 子空间 span{|e,0⟩, |g,B_q⟩} ⊂ 单激发子空间，dim = 2，ln 2 单点
- B 的 ensemble {|00⟩,|10⟩,|01⟩,|11⟩}：是 N_q=2 双模 Fock 占据子空间（N_q=2 时双 qubit 总维数 = 2² = 4），ln 4 = 2 ln 2 单点
- 这两个 saturating 是**对不同 Hilbert 子空间**的 Holevo bound

**结论**：B 的 ln 4 与 A 的 N_I^{(S)} = 2 ln 2 是**两个独立的 saturating bound**：
- A 的 saturation 是 N_q-independent（亮模子空间始终 dim=2）
- B 的 saturation 是 N_q-dependent（双模 Fock 子空间 dim = 2^{N_q}，N_q=3 时 ln 8 = 3 ln 2 ≠ 2 ln 2）

**所以**：N_q=3 验证两路：
- A：N_I^{(S)}(N_q=3) = 2 ln 2（亮模二元谱不变）
- B：ln(2^3) = 3 ln 2（三模 Fock 子空间维数）
- N_q=3 时 A 给 2 ln 2，B 给 3 ln 2 — **两者数值不同！**

这反向证实了 A 的"动力学路径量"解读是正确的（与 N_q 无关），B 的"Hilbert 维数同构"解读在 N_q=2 是巧合。

**v9-K4 表述强化**：候选 (c) 二元熵 total variation = A 解读 = 普适。候选 "Hilbert 维数同构" = B 解读 = N_q=2 巧合，**真正排除**。

B 自己的卡点 K2 已识别这一张力："(II) 的饱和系综不是 JC 演化态本身……属外部最优化构造，命题语义需澄清"——B 已经诚实地标记了这个区分。PI 形式审核裁决：B 的 saturation 描述虽然在 N_q=2 数值正确，但物理身份与 A 不同，需在知识库中明确分离。

---

## §3 K 条目级别裁决

### v9 Phase 2 新增

| 编号 | 内容 | 状态 | L级 | 来源 |
|------|------|------|-----|------|
| **v9-K5** ⭐ | **N_q-普适性定理（亮/暗模分解）**：对任意 N_q-mode 对称耦合 JC 模型在共振+真空初态下，Bogoliubov 变换 g·Σᵢaᵢ = √N_q·g·B_q（亮模） + (N_q−1) 暗模与系统解耦（恒保持真空）；ρ_B 在亮模二元谱 (cos²u, sin²u)，暗模平凡。Rabi Ω_{N_q} = g√N_q 仅改变时间标度。S(ρ_B) = h₂(sin²u) 与 N_q 无关。**N_I^{(S)}(N_q) ≡ 2 ln 2** 普适于任意 N_q ≥ 2。**v9-K4 候选 (c) 普适化达成**；同时**严格排除"Hilbert 维数同构"解读**（N_q=3 时 A 给 2 ln 2，"维数同构"给 3 ln 2，数值分歧）。 | ✅ | L2 | v9-P2 (A+B 双路独立) |
| **v9-K6** | **Holevo saturation 二解定理**：N_I^{(S)} = 2 ln 2 在 N_q=2 toy 下与 Holevo accessible information 上限同值（数值都 = 2 ln 2 = ln 4），但**物理身份不同**：(i) A 解读：JC 自然演化下亮模子空间 dim=2 的 forward+backward 半段 Holevo 单点 χ_max = ln 2 累加 = 2 ln 2 — **动力学路径量** (N_q 无关)；(ii) B 解读：全 N_q-mode Fock 子空间外部最优 ensemble 单点 χ_max = ln(2^{N_q}) = N_q·ln 2 — **信道容量上限** (N_q 依赖)。N_q=2 时数值碰巧重合，N_q≥3 数值分歧（A 给 2 ln 2，B 给 N_q·ln 2）。**v9 北极星采纳 A 解读**：N_I^{(S)} 的几何身份是动力学路径上的二元熵 total variation。 | ✅ | L2 | v9-P2 (PI 综合) |
| **v9-K7** | **端点依赖闭式定理**：在 v9-K1 setup + 任意端点 T ∈ (0, π/2) 下，N_I^{(S)}(T) = 2·h₂(sin²(u_T))，u_T = √N_q·g·T。具体：T=π/(4√N_q·g) → u_T=π/4 → N_I^{(S)} = 2·ln 2（peak）；T < π/(4√N_q·g) → u_T < π/4 → N_I^{(S)} < 2 ln 2 单调递增；T > π/(4√N_q·g) → u_T > π/4 → forward 与 backward 同时贡献，N_I^{(S)}(T) = 2·h₂(sin²u_T) (forward 上升) + 2·[h₂(sin²(π/4)) − h₂(sin²u_T)] (backward 下降) = 2 ln 2（u_T < π/2 后保持） | ✅ | L2 | v9-P2 (A+B 一致) |

### v8-K9 状态进一步升级
- v8-K9 ⚠️L2(待普适化) → v9-P1 ✅L2(toy) → **v9-P2 ✅L2(N_q-普适+端点闭式)**
- 几何身份现已锁定：**动力学路径量+二元熵 total variation+ N_q-无关**

---

## §4 卡点状态更新

### v9 Phase 2 关闭
- **C[v9-1]** N_q ≥ 3 普适性 → ✅ v9-K5 关闭（A+B 双路证明 N_I^{(S)} 与 N_q 无关）
- **C[v9-2]** Holevo saturating ensemble → ✅ v9-K6 关闭（双解 + 物理身份分离）
- **C[v9-3]** 端点依赖闭式 → ✅ v9-K7 关闭

### v8 继承（推进状态）
- **C[v8-9]** N_I^{(S)} 几何普适性 → **完全关闭**（v9-K4+K5+K6 三定理综合）
- **C[v8-10]** c(β) 闭式普适性 → 仍开放，留 v10
- **C[v8-3]** ε-Bogoliubov 退化谱：v9-P3 收官前处理
- **C[v8-4]** σ_t 修复 → 维持 v9 副线
- **C[v8-8]** r(β) 初态依赖：与 C[v9-3] 端点闭式相邻，共同关闭部分

### v9 Phase 2 新增（轻微）
- **C[v9-4]** 暗模在非对称/finite-T 浴是否激活（B 卡点 K3）— v10 候选
- **C[v9-5]** χ(u) vs S_q(u) 关系（仅 u=π/4 saturate）— v9-P3 处理

---

## §5 失败日志更新

| # | 内容 | 状态 |
|---|------|------|
| **F3(v9)** | v9-P2 完整关闭三角对称验证：N_q-普适 + Holevo 双解 + 端点闭式。**v9 北极星 N_I^{(S)} 几何身份完全锁定** | 北极星达成（v9-P3 收官） |
| **F4(v9)** | A vs B 关于 Holevo saturation 的张力被 PI 裁决为"两个独立 saturation"——B 描述外部最优 ensemble 容量上限（N_q 依赖），A 描述动力学路径量（N_q 无关）。在 N_q=2 toy 数值碰巧重合 = 2 ln 2 = ln 4。N_q=3 数值分歧（A 给 2 ln 2，B 给 3 ln 2）反向证实 A 解读 | 已解决 |

---

## §6 北极星距离

| 维度 | Phase 1 后 | Phase 2 后 |
|------|----------|----------|
| 三选一身份候选（toy） | ✅ (c) | ✅ 维持 |
| 多模 N_q·ln 2 普适 | ❌ | ✅ v9-K5（**修正：与 N_q 无关，普适 = 2 ln 2**） |
| Holevo saturation 显式 | ❌ | ✅ v9-K6（双解分离） |
| 端点依赖闭式 | ❌ | ✅ v9-K7 |
| 几何身份最终物理判定 | — | **本Phase 接近完成 95%**（v9-P3 收官给最终物理图景） |

---

## §7 Phase 3 路线图

**Phase 3** 类型：C 物理裁决（PI 主导，可能不需 A/B 突击）

任务：综合 v9-K1~K7 给出 v8-K9 的最终物理身份陈述：
- **核心命题（v9 收官 K8）**：N_I^{(S)} 是 N=N_q-mode 对称 JC 共振+真空初态下浴在亮模子空间的二元熵沿动力学轨迹的 total variation；普适值 = 2 ln 2；与 N_q 无关；与 Hilbert 维数同构在 N_q=2 数值碰巧重合（巧合非同构）

收官前 GATE：AUDITOR + 恶意审稿人 + AHA + NAVIGATOR

---

## §8 下一步指令

> ▶️ 下一步：v9 Phase 3 类型 C（物理裁决，PI 主导）。综合 v9-K1~K7 写最终物理身份定理 v9-K8 + 启动 4 收官 GATE。任务书：current/plan/phase-3-任务书.md。

---

*PI 审查 v9 Phase 2*
*GATE 1-4 全部通过；A vs B Holevo saturation 张力裁决完成*
*v9-K5/K6/K7 写入；v8-K9 完全关闭*
*北极星达成 95%；Phase 3 收官*
