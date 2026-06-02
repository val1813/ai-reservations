# PI审核 Phase 2 — MasslessGravity-Island v1

> PI 主上下文执行，对照 A/B 双博士 Phase 2 独立输出
> 时间：2026-06-01

## ⚠️ 重大发现（A/B 独立确认）

**Antonini et al. (2506.04311, 49页) 完全不提及 BMS 或 supertranslation。**
- 论文的真实绕过策略：**子代数选择**（A_rad,u0 = 排除 H_ADM 的辐射子代数），不是 dressing。
- BMS 群推广被显式标记为 "future work" (§5.2)。
- 这篇论文**不构成对 C1 的正面回答**。

---

## 一、A/B 审核入口对比

| 维度 | A博士 | B博士 |
|------|-------|-------|
| C1 判决 | 不可满足。δ_f A(∂I) ≠ 0, δ_f S_bulk=0, Q_f/4G+0≠0 | 同判决。Q_f ≠ 0 不可被 dressing 消去 |
| 子代数 vs dressing | Antonini 策略 = 子代数限制（排除 H_ADM），≠ dressing | 同确认 |
| 最致命发现 | 论文不讨论 BMS → C1 的 burden of proof 完全未承担 | Attack 1: Dressing × Replica 互斥圈 → C1 与 C2 不能同时激活 |
| 命题A 存活概率 | 低（论文自身标记 BMS 为 "未来工作"） | 15-20% |

**A/B 独立收敛程度：极高。** 双博士在不交流的情况下得出相同核心结论：Antonini et al. 的论文不解决 C1 问题。

---

## 二、PI 裁决

### 核心判决

**命题A（Antonini et al. 2506.04311 = "岛屿可推广到 flat space"）在 BMS-invariance 问题上是沉默的。**

这不是说论文错了——而是说论文的结论域是 "在 fixed Bondi frame + 排除 ADM Hamiltonian 的子代数中，Page 曲线存在"。这个命题在论文自身范围内可能是正确的，但它不回答 "在 BMS-invariant 意义下岛屿是否存在"。

B博士的 Attack 1（Dressing × Replica 互斥圈）将问题进一步精化：
- C1（BMS-invariance）需要 dressing → 使 Q_f 变成代数中心元素
- C2（replica wormhole）需要 Q_f 有非平凡谱 → 边界条件未改动
- 两者不能同时成立

这是接近 ✅L2 级别的推理（如果 B 博士的 Lemma 1/2 能被严格化）。

### 北极星进展评估

原始北极星："无质量引力中纠缠岛屿是否存在？"

**Phase 2 答案：Antonini et al. (2506.04311) 不构成对 "岛屿在 flat space 中存在" 的完整回答。论文在固定的 Bondi frame subalgebra 中有效，但 BMS-invariance（规范不变性的真正检验）被推迟为未来工作。C1-C2 互斥构成对 "完整岛屿公式" 的原理性障碍。**

---

## 三、知识库增量

**K2.1** ⚠️L1（Antonini 不解决 BMS）— 2506.04311 49页零命中 BMS/supertranslation。策略是子代数选择 A_rad,u0（排除 H_ADM），非 dressing。BMS 推广标记为 §5.2 future work。
- math_object: Antonini subalgebra strategy

**K2.2** ⚠️L1（C1-C2 互斥定理）— C1 bypass（dressing → Q_f 中心化）与 C2 bypass（replica trick 需 Q_f 非平凡谱）不能同时成立。B 博士 Lemma 1（Q_f 投影）+ Lemma 2（互斥引理）。
- math_object: dressing-replica incompatibility

**K2.3** ⚠️L1（命题A 存活概率 15-20%）— 仅剩逃生路径：Antonini §4.4 state-dependent dressing 的开放问题，或发现 C1 不是岛屿公式的必要条件。
- math_object: proposition A survival

---

## 四、下一步

Phase 2 结论强烈偏向命题B。Phase 3 应做两件事：
1. **建立否定性定理**：C1-C2 互斥的严格版本（从 B 博士 Lemma 1/2 出发）
2. **正面表达命题B**：Geng et al. (2602.06543) 的 "规范不变算符不能局域化" + 本课题的 C1-C2 互斥 → flat space island formula 的适用范围被精确定界

▶️ 下一步：生成 Phase 3 AB 任务书（否定性定理 + 命题B 精化），按 SOP 直接执行。
