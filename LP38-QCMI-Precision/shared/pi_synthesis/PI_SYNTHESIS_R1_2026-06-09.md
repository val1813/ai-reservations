# PI综合 — LP36 Round 1 双墙攻克

**日期:** 2026-06-09
**来源:** Round 1 AB产出 + INSPECTOR独立审查
**状态:** Round 1完成 → 进入Round 2
**SOP:** Phase清单驱动，最低3轮硬约束

---

## 0. 执行摘要

Round 1产出质量总体良好但发现4个BLOCK级错误和13个WARNING。核心教训：**INSPECTOR独立审查的价值被再次验证**——B博士的P2路径（看起来最有希望的绕行策略）在两个致命前提上犯错，若未被审查会在投稿中崩溃。

### 关键数字

| 指标 | Wall 1 | Wall 2 |
|------|:------:|:------:|
| PASS项 | 9 | 5 |
| BLOCK项 | 2 | 2(+1) |
| WARNING项 | 7 | 6 |
| 过度声张 | 5 | 5 |
| A博士评级 | — | A- |
| B博士评级 | — | C+ |
| Round 1判定 | CONDITIONAL PASS | NEEDS MAJOR REPAIR |

---

## 1. Wall 1: 下界不紧 — Round 1状态

### 1.1 已确认的产出（PASS级）

| # | 产出 | 验证状态 |
|---|------|:---:|
| W1-1 | QCMI = S(J(N)/d) 恒等式（绕过Fawzi-Renner） | ✅ INSPECTOR独立验算确认 |
| W1-2 | ZZ(θ)对齐轴精确解QCMI(θ=π/2,p=0.5)=1.5 bits | ✅ INSPECTOR独立验算确认 |
| W1-3 | 五层保守性审计方法学（每层定量分解） | ✅ 框架正确 |
| W1-4 | Log-factor O(|c|² log(1/|c|²)) 在小|c|下的数学结构 | ✅ 微扰展开在|c|≪1严格 |
| W1-5 | Haar典型QCMI≈2.25 bits，下尾(μ-3σ)≈1.71 bits | ✅ 与实验一致 |

### 1.2 需要修正的BLOCK

**BLOCK-1 (B博士):** "物理下界至少~0.5-1.0 bits"混淆了典型值与普适下界。
- **问题:** 同时承认|c|→0时QCMI→0，但又声称正普适下界。自相矛盾。
- **修正:** 严格区分三概念：普适下界(0)、条件界f(|c|)、典型值(~2.25)

**BLOCK-2 (A博士):** §1.6声称gap "fully explained" No "mystery gap"，但§6.2报告1.5-2.7 bits "UNACCOUNTED"。
- **修正:** 改为"gap qualitatively attributed to five-layer conservatism, quantitative bridging incomplete"

### 1.3 核心结论

**η₀=0.180是不可改进的普适常数下界**（在|c|-independent形式下）。这不是弱点——它是"最坏情况"的正确数学界。改进路径不是增大η₀，而是**将下界重构为|c|-条件函数**。

**重构策略：**
```
旧表述: "QCMI ≥ 0.180 bits（普适常数）" → 审稿人攻击"4-18×太松"
新表述: "QCMI ≥ f(|c|, θ, p)，其中f在实验相关区域给出0.3-1.5 bits"
         + "η₀=0.180是最坏情况渐近极限(|c|→0, 对齐轴)"
```

### 1.4 Round 2优先级

| 优先级 | 行动 | 理由 |
|:---:|------|------|
| P0 | 数值Choi对角化验证log-factor | INSPECTOR GAP-4；审稿人要求 |
| P1 | 修正两个BLOCK项（措辞矛盾） | 投稿前必须 |
| P1 | Buscemi vs 乘积态36%差异分析 | INSPECTOR GAP-1 |
| P2 | 对齐轴单调性证明或强数值证据 | INSPECTOR GAP-2 |

---

## 2. Wall 2: b₁>1推广 — Round 1状态

### 2.1 已确认的产出（PASS级）

| # | 产出 | 验证状态 |
|---|------|:---:|
| W2-1 | sQNM超可加性不能直接应用于共享节点环 | ✅ A博士的gap分析正确完整 |
| W2-2 | 顶点不相交环的可加性严格成立 | ✅ 张量积可加性，标准结果 |
| W2-3 | A博士的分层定理体系：Theorem A(严格)→B(条件)→C(猜想)→D(保守) | ✅ 状态标注诚实 |
| W2-4 | A博士的自我攻击§7——尤其自攻击A4（QCMI可能不被b₁主导） | ✅ 最深刻的自我批评 |
| W2-5 | 树边冻结：小Cartan严格 + 非退化配置局部成立 | ✅ Sard+隐函数定理 |

### 2.2 需要修正的致命BLOCK

**BLOCK-1 (B博士):** P2路径的核心前提错误——将"顶点不相交"混为"边不相交"。
- **根本原因:** `b1_additivity.md` Theorem 1的精确条件是V_A ∩ V_B = ∅（顶点不相交），证明依赖张量积分解。但标题写的是"Edge-Disjoint Additivity"→命名混乱向下游传播
- **后果:** 边不相交但共享顶点的两个环的张量积可加性**不适用**。P2"完全绕过"共享节点干涉的声称虚假
- **修正:** 所有声张限制为"顶点不相交的环"；P2从"主攻"降级为"待修复"
- **连带修复:** `b1_additivity.md`的命名混乱必须立即修复

**BLOCK-2 (B博士):** 贪心算法ν(G)/b₁(G)下界论证数学错误。
- 混淆b₁(G)（圈空间维数）与圈计数
- 贪心算法实际给出上界而非下界
- ν(G) ≥ b₁(G)/(4Δ²)没有有效证明

**BLOCK-3 (B博士):** "QCMI在边不相交环上的可加性"列为"严格已证明"——实为顶点不相交。

### 2.3 可证vs猜想的分界线（经INSPECTOR修正后）

**严格可证：**
> **Theorem (Vertex-Disjoint Components):** 设G = ∪ᵢ Gᵢ，各Gᵢ顶点集互不相交且每个Gᵢ包含至少一个因果环。则 I(R;E'|Q') ≥ η(d)·k，其中k是分量数。[张量积可加性，严格]

**猜想（有力证据支撑）：**
> **Conjecture (General Hasse Diagram):** I(R;E'|Q') ≥ η(d)·b₁(G)。支持证据：(i)顶点不相交情况已证明；(ii)树边冻结对非退化配置局部成立；(iii)有限数值数据显示共享节点环的QCMI不低于单环下界。

### 2.4 Round 2优先级

| 优先级 | 行动 | 理由 |
|:---:|------|------|
| **P0** | **运行b₁扫描实验** | A博士自攻击A4：如果QCMI不随b₁增长，Wall 2核心主张需要根本修正 |
| **P0** | 修复`b1_additivity.md`命名混乱 | 错误已向下游传播（BLOCK-1根源） |
| P1 | 完成dephasing解耦分析（共享顶点边不相交环） | WARN-5；Gap G2 |
| P1 | ν(G)/b₁(G)图论研究（从正确前提出发） | BLOCK-1/2修复后重新开始 |
| P2 | 树边冻结局部→全局论证（Sard延拓） | WARN-2；Gap G1 |

---

## 3. 交叉污染防火墙 — Round 1后状态

| 检查项 | 状态 |
|--------|:--:|
| Wall 1产出包含b₁>1声张？ | ✅ 无——两人均严格遵守范围 |
| Wall 2产出依赖Wall 1定理但声称b₁>1结论？ | ✅ 无循环论证 |
| 旧墙定理与猜想捆绑？ | ✅ 未捆绑——A博士明确建议分拆投稿 |
| b1_additivity.md命名混乱导致交叉污染？ | ❌ **已发生**——Edge-Disjoint vs Vertex-Disjoint混乱向下游传播到B博士R1 |

**防火墙修复行动：** 立即修复`b1_additivity.md`中所有"Edge-Disjoint"为"Vertex-Disjoint"。

---

## 4. 投稿策略（经Round 1验证后更新）

### 论文S1: "Causal Cycle Topology Enforces Quantum Non-Markovianity" (目标PRL)

**内容（全部严格）：**
- CFOL (v4证明): QCMI=0 ⇔ 所有u_i可因子化
- η₀ = 1/(8 ln 2): 普适下界（最坏情况）
- 对易性定理 + ZZ(θ)精确解
- 指针基数值定理
- **仅b₁=1, d=2**——无b₁>1声张，无宏观极限

**与旧墙四支柱的关系：** 这是支柱I-IV的完整呈现。支柱V（经典/量子分离）移除。

### 论文S2: "Toward Macroscopic Classicality from Causal Topology" (后续)

**内容：**
- 顶点不相交分量的严格可加性
- 树边冻结（小Cartan严格 + 非退化局部成立）
- b₁>1猜想 + 数值证据
- 明确标注为"theoretical conjecture with evidence"

---

## 5. Round 2执行计划

### 5.1 立即修正（P0，本轮内完成）

1. **修复命名混乱** → Agent修复`b1_additivity.md`
2. **运行b₁扫描** → 数值实验确定QCMI标度行为
3. **修正Wall 1的2个BLOCK** → A博士和B博士修正措辞

### 5.2 Round 2攻击（AB并行）

**Wall 1 Round 2:**
- A博士: 数值Choi对角化 + 精准log-factor验证
- B博士: Buscemi框架下的对齐轴精确解 + 修正"物理下界"措辞

**Wall 2 Round 2:**
- A博士: Dephasing解耦分析 + 树边冻结延拓论证
- B博士: 从修正前提重新攻击ν(G)/b₁(G) + 新跨域路径

### 5.3 后续轮次

- Round 2 + INSPECTOR → PI综合
- Round 3: 收尾（剩余gap诚实降级或攻克）
- 收官: GATE 6/7 + 投稿准备

---

## 6. 课题状态更新

| 墙 | Round 1状态 | 核心缺口 | Round 2目标 |
|----|:----------:|---------|:----------:|
| Wall 1 (下界不紧) | CONDITIONAL PASS | BLOCK措辞修正 + 数值验证 | 重构|c|-条件界 + 完成数值验证 |
| Wall 2 (b₁>1推广) | NEEDS MAJOR REPAIR | BLOCK级错误需修复 + b₁标度未确定 | 修复前提 → 确定可证边界 → 诚实降级猜想 |

**对用户的诚实汇报：** 
- Wall 1可以在投稿前收紧到可辩护状态（修正措辞+数值验证）
- Wall 2的完整严格证明在当前框架下不可行——我们将产出"严格部分+诚实猜想的清晰分界线"
- b1_additivity.md的命名混乱是今天发现的最重要的结构性错误——如不修复会在投稿中被审稿人发现

---

*PI综合完成。进入Round 2修正+攻击。*
