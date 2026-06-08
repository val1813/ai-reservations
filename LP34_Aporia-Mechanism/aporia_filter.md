# Aporia Filter -- 理论诊断工具 v1.0

**用途:** 输入一个物理理论的基本信息结构，输出四个约束的诊断结果并给出裁决。
不是框架，不是生成器——只是一个滤波器。不依赖 DGF 的场方程或物质模型。

**理论基础 (Phase 0+1 已验证 [1]):**
(a) 紧致性定理保证有限约束不能将可能物理理论空间 Omega 缩减到独点集 [2]——
但可以系统性**排除**不自治的理论。
(b) 对 17 个候选约束的依赖网络分析发现不可约硬核大小为 2 [1]:
{C1: 信息容量有界, C2: 因果有向性}。
C3 (回流界) 和 C4 (熵面积界) 是它们的直接推论，添加了开放系统和空间几何的结构信息。

---

## 1. 理论规格书 (输入)

能填多少填多少。"不能确定"是合法回答——触发 APORIA ZONE。

```
理论名称: [  ]
基本信息载体: [bit / qubit / qudit(d=N) / 实数值变量 / 其他]
单载体 Holevo 容量 χ: [数值 或 不能确定]
因果结构:
  影响是否对称? [是/否/不确定]
  若不对称，偏序关系是? [描述]
开放系统:
  是否有开放系统演化? [是/否]
  最大信息回流概率 P_reflux ≈ [数值 或 不能确定]
  环境可访问相干分数 q_E ≈ [数值 或 不能确定]
  系统可访问相干分数 q_S ≈ [数值 或 不能确定]
引力:
  是否包含引力? [是/否]
  弱场极限是否恢复牛顿引力? [是/否/不确定]
  区域内熵是否按边界面积增长? [是/否/不确定]
```

---

## 2. 四个约束

### C1: 容量界 -- χ ≤ 1 bit/基本单元

**定义。** 理论 T 中基本信息载体 C 的 Holevo 容量 [3]:
χ(C) = max_{p_i,ρ_i} [S(∑p_i ρ_i) - ∑p_i S(ρ_i)]。
经典 bit: χ = 1。qubit (d=2): χ ≤ 1。qudit (d=N): χ ≤ log₂ N。
实连续变量 (无限分辨率): χ = ∞ (原则上可编码任意多位信息)。

**排除证明。** 若 χ > 1/单元，N 个单元的总容量 > N bits。
当 N 增大到某一体积 V 满足 Bekenstein 界 [4] S ≤ 2πk_B R E/ħc 的极限时，
总信息量超过 Schwarzschild 半径内的 Bekenstein 上限 S_max = A/4ℓ_P²。
该区域坍缩为黑洞，内部信息无法被外部访问——与"N 个单元都可被同时访问"矛盾。
因此 χ ≤ 1 是与 Bekenstein 界兼容的必要条件。

**排除:** 信息容量无上界的理论（操作可访问的实值状态变量、box-world GPT [5]）。
**豁免:** de Broglie-Bohm 的导引波操作上不可访问——其操作 χ 仍 ≤ 1，PASS C1。
**Aporia zone:** T 未定义可操作性制备和测量的信息载体。

引用: Holevo (1973) [3], Bekenstein (1981) [4], Barrett (2007) [5].

---

### C2: 因果有向性 -- 信息影响是偏序

**定义。** "X 因果影响 Y"(X → Y) 意为 X 处的一个操作改变 Y 处测量结果的概率分布。
T 满足 C2 ⇔:
  (i) 不对称性: 若 X → Y 且 X ≠ Y，则不能同时 Y → X。
  (ii) 传递性: 若 X → Y 且 Y → Z，则 X → Z。
即 (事件集, →) 是一个严格偏序。

**排除证明。** 若存在 A ≠ B 使得 A → B 且 B → A，构造闭合循环 A → B → A。
将此循环嵌入 Szilard 引擎 [6]: (1) 在 A 测量获取信息，
(2) 通过 B→A 通道送回，(3) 利用送回的信息提取功——
可在单个热浴中提取功，违反第二定律的开尔文表述。
Stone & Jha (2025) [7] 给出了严格的 GPT 版本。

QM 满足: 幺正演化可逆但投影测量不可逆，整体因果是偏序。
GR 满足: 类时曲线不能闭合。

**排除:** 允许因果循环的理论（任意操纵的 CTCs、允许双向瞬时信号的理论）。
**Aporia zone:** T 无事件因果结构（如纯平衡态理论）。

引用: DGF A1 [8], 热力学第二定律 [6], Stone & Jha (2025) [7].

---

### C3: 回流界 -- P_reflux ≤ min(q_S/q_E, (1-q_E)/q_E)

**定义。** 开放系统中 S 为系统，E 为环境。
q_X ≡ 子系统 X 中可访问量子相干比特占比 (0 ≤ q_X ≤ 1)。
q_X=1: 完全量子（所有信息可访问），q_X=0: 完全经典（所有信息已归档）。
信息回流: 已经从 S 流入 E 的信息自发地从 E 回到 S。
P_reflux: 单次信息传输事件中回流的概率。

**排除证明 (q_S/q_E 项)。** S 有 N_S 个细胞，E 有 N_E 个细胞，每细胞 1 bit (C1)。
前向流容量 C_F = N_E·q_E (环境中可接收信息的 |0⟩ 态细胞数)。
回流需要 E 的 |1⟩ 态翻转为 |0⟩ 并发回。
S 侧最多 N_S·q_S 个细胞可接收。稳态系综中:
P_reflux ≤ (N_S q_S)/(N_E q_E) = q_S/q_E (取 N_S=N_E)。
纯粹容量计数——不需要动力学哈密顿量 [8]。

**排除证明 ((1-q_E)/q_E 项)。** 回流需要 E 中已归档细胞 (|1⟩ 态, 占比 1-q_E)
翻转为 |0⟩。在 GKSL 方向性假设下 (Lindblad 生成元只生成 |0⟩→|1⟩)，
翻转仅来自 L_swap 部分的 Lindblad 算符，相对强度 ε = ||L_swap||/||L_copy||。
回流率 ∝ ε²，容量论证要求 ε² ≤ (1-q_E)/q_E [8]。
结合: P_reflux ≤ min(q_S/q_E, (1-q_E)/q_E)。

热力学极限 (N→∞, q_S << q_E): P_reflux → 0——退相干在宏观极限下不可逆。

**排除:** 允许完美退相干逆转的理论（P_reflux→1 即使系统已宏观经典化）。
**Aporia zone:** T 无开放系统描述；q_X 无操作定义；环境无细胞层结构。

引用: DGF S1 Theorem [8], Breuer-Laine-Piilo (2009) [9], GKSL (1976) [10].

---

### C4: 熵面积界 -- S(Ω) ≤ const × A

**定义。** 对 T 中任何有界空间区域 Ω (边界 ∂Ω 面积 A):
S(Ω) ≤ k·A/ℓ², 其中 ℓ 为 T 的基本长度尺度，k = O(1)。

**排除证明。** 设 T 的信息图 G = (V,E)，顶点为信息细胞，边为细胞间通道。
每边容量 ≤ 1 bit (C1)。∂Ω 是割 (cut): 移除 ∂Ω 边后 Ω 内部与外部不连通。
由 Ford-Fulkerson 最大流最小割定理 [11]:
max-flow(Ω→外部) = min-cut(∂Ω) ≤ N_∂Ω bits。
外部最多区分 2^(N_∂Ω) 个内部构型。由 Boltzmann: S = ln(可区分微态数)。
∴ S(Ω) ≤ N_∂Ω·ln 2 ∝ A/ℓ²。严格图论定理——仅需 C1 和图连通性 [8]。

比对 Bekenstein-Hawking S_BH = A/4ℓ_P²:
若细胞间距 a = ℓ_P, S_DGF/S_BH = 4ln2 ≈ 2.77 (同数量级)。
系数 O(1) 模型依赖；面积缩放是严格定理。

**排除:** 熵按体积增长的理论 (S∝V)；外部可获取黑洞内部全部信息的理论；
弱场极限不恢复牛顿引力的含引力理论 (如 g_μν = q²η_μν → γ_PPN = -1，
与 Cassini [12] 测得的 γ_PPN = 1 ± 2.3×10⁻⁵ 在 ~10⁵σ 处冲突)。

**非适用:** T 不含引力 → N/A (不适用)，非 FAIL。

引用: DGF S4 Min-Cut Theorem [8], Ford-Fulkerson [11], Bekenstein-Hawking [13], Cassini [12].

---

## 3. 决策程序

```
输入 T 规格书
        │
C1: χ≤1? ──NO──→ ❌ EXCLUDED (C1: 容量无界)
   │YES/UNDECIDED
C2: 偏序? ──NO──→ ❌ EXCLUDED (C2: 无时间箭头)
   │YES/UNDECIDED
C3: P_reflux≤min(...)? ──NO──→ ❌ EXCLUDED (C3: 完美逆转)
   │YES/SKIP/UNDECIDED
C4: S≤const×A? ──NO──→ ❌ EXCLUDED (C4: 信息悖论)
   │YES/N/A/UNDECIDED
   ✅ SURVIVES
```

UNDECIDED 不阻断流程。C1-C4 全部 UNDECIDED → 全局 APORIA ZONE。
C1 和 C2 是不可约硬核，违反即致命；C3/C4 违反可通过引入结构修正。

---

## 4. 输出格式

```
Aporia Filter 诊断报告
============================
理论: [名称]    检测日期: [YYYY-MM-DD]

C1 容量界:      PASS/FAIL/UNDECIDED  理由: [...]
C2 因果有向性:  PASS/FAIL/UNDECIDED  理由: [...]
C3 回流界:      PASS/FAIL/UNDECIDED/SKIP  理由: [...]
C4 熵面积界:    PASS/FAIL/UNDECIDED/N/A   理由: [...]

裁决: SURVIVES / EXCLUDED (违反 C[n1], C[n2]) / APORIA ZONE

EXCLUDED → 被排除的理论类 + 排除依据 + 可否修正
APORIA ZONE → 无法判定的约束 + 需要澄清的信息 + 建议
```

---

## 5. 工作示例

### 示例 1: 标准量子力学 (非相对论)

- C1: qubit χ ≤ log₂2 = 1 → PASS
- C2: 测量投影不可逆 → 因果偏序 → PASS
- C3: 宏观退相干不可逆 (N→∞ 时 P_reflux→0) → PASS
- C4: 无引力 → N/A

**裁决: SURVIVES**

### 示例 2: 操作可访问的实值隐变量 (λ∈R, 可任意制备和测量)

λ∈R 具有无限精度: 可选择 λ 的前 n 位二进制小数编码 n bit 消息 → χ=∞ > 1。
C1: FAIL。

**裁决: EXCLUDED (违反 C1——无限信息容量)**
注: de Broglie-Bohm 不在此类——λ 不可操作访问，操作 χ 仍由 QM 决定。

### 示例 3: DGF pre-S3 (缺陷时空指标: g_μν = q²η_μν)

- C1: cell bit χ=1 → PASS
- C2: A3 有向 → PASS
- C3: S1 定理 → PASS
- C4: g_μν = (q_∞+δq)² η_μν → γ_PPN = -1
  vs Cassini γ=1±2.3×10⁻⁵ [12] → FAIL

**裁决: EXCLUDED (违反 C4——弱场极限与 Cassini 冲突)**
注: DGF v3.1 的复指标 Q_ττ=exp(iπ(1-q)) 自动恢复 γ_PPN=1 [8]——此处排除的仅是 g_μν=q²η_μν 形式。

---

## 6. Aporia Zones: 诚实边界

触发 UNDECIDED 的条件:

| 约束 | 触发条件 |
|:-----|:--------|
| C1 | 无操作制备/测量定义；信息载体未定义 |
| C2 | 纯静态/平衡态理论，无事件因果结构 |
| C3 | 无开放系统描述；q_X 无操作定义；环境无细胞层 |
| C4 | 无空间结构/边界定义；无标准熵定义 |
| 全部 | 全局 APORIA ZONE: 理论太模糊，无法被任何约束测试 |

三种"不知道" (Phase 0 [1]):
1. 偶然不知 — 约束池太弱 → 改进规格书后再测
2. 语言界不知 — 一阶语言中不可判定 → 需形式化增强
3. 原则不知 — 任何可公理化扩张中都不可判定 → 承认它

Aporia Filter 针对层次 1，标注层次 2，接受层次 3。

---

## 7. 数学基础

| 约束 | 核心定理 | 数学前置 |
|:-----|:--------|:-------|
| C1 | Holevo 界 + Bekenstein 界 | 量子信息论 [3] + 黑洞热力学 [4] |
| C2 | 因果循环→Szilard→第二定律违反 | 偏序理论 + 热力学 [6] + GPT [7] |
| C3 | 容量计数 + GKSL 方向性 | 开放量子系统 [10] + 容量理论 [8] |
| C4 | Ford-Fulkerson 最大流最小割 | 图论 [11] + 黑洞热力学 [13] |

不使用的前提: DGF q-场方程、有效度规表示、质量公式、引力校准——
这些是"理论"，不是"滤波器"。滤波器只需要 A1-A3: 信息存在 + 容量有界 + 溢出不可逆。
A1-A3 等价于"信息可被谈论"——比 DGF 的范围小得多。

---

## 参考文献

[1] LP34 Phase 0 & Phase 1 Conclusions. Internal (2026).
[2] Marker, D. "Model Theory." Springer GTM 217 (2002); Chang & Keisler, "Model Theory." Dover (1990).
[3] Holevo, A.S. Probl. Peredachi Inf. 9(3), 3-11 (1973).
[4] Bekenstein, J.D. Phys. Rev. D 23, 287 (1981).
[5] Barrett, J. Phys. Rev. A 75, 032304 (2007).
[6] Landauer, R. IBM J. Res. Dev. 5, 183 (1961); Bennett, C.H. Int. J. Theor. Phys. 21, 905 (1982).
[7] Stone, M.H. & Jha, R.K. "Causal asymmetry from information-theoretic constraints in GPTs." (2025).
[8] Huang, Z. "DGF v3.1-prd" and "Supplement S1+S4." Internal (2026).
[9] Breuer, H.-P., Laine, E.-M., Piilo, J. Phys. Rev. Lett. 103, 210401 (2009).
[10] Gorini, V., Kossakowski, A., Sudarshan, E.C.G. J. Math. Phys. 17, 821 (1976).
[11] Ford, L.R. Jr., Fulkerson, D.R. Can. J. Math. 8, 399-404 (1956).
[12] Bertotti, B., Iess, L., Tortora, P. Nature 425, 374-376 (2003).
[13] Bekenstein, J.D. Phys. Rev. D 7, 2333 (1973); Hawking, S.W. Commun. Math. Phys. 43, 199 (1975).

---

## 附录: 快速参考卡

```
C1 容量界: χ≤1 bit/单元             违反=无限信息密度=Bekenstein 冲突
C2 因果有向性: 偏序(不对称+传递)    违反=因果循环=无时间箭头
C3 回流界: P_reflux≤min(q_S/q_E,(1-q_E)/q_E)  违反=退相干可完美逆转
C4 熵面积界: S≤const×A              违反=信息悖论/弱场极限错
```

---

*工具版本: v1.0. 基于 LP34 Phase 0+1 验证结论. 不推导新物理——只滤波已有物理.
下一版本: Phase 2 加入约束量化和稳定性分层审计.*
