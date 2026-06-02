# 跨课题卡点追踪：Griffiths 尾巴修正 L_eff > ξ_perc

> 来源：LP1-补6 Phase 1 B 博士 Attack 3
> 影响范围：LP1-S3 (MBL-Quasiperiodic)、LP1-综合推导
> 严重性：高（可能改变 LP-1 S3 的稳定性结论）
> 创建：2026-06-01

---

## 问题陈述

B 博士 Phase 1 Attack 3 发现：准周期 MBL 中罕见低无序区域的有效尺寸需计入 Griffiths 尾巴修正：

$$L_{\text{eff}} = L_{\text{max}} + 2\zeta \cdot \ln(W/g)$$

对黄金比例参数（ζ ≈ 3, W/g ≈ 10）：
$$L_{\text{eff}} \approx 19 + 6 \cdot \ln(10) \approx 33 > \xi_{\text{perc}} \approx 30$$

**这意味着：即使 Diophantine 保护严格成立，Griffiths 尾巴可能使单个罕见区域的有效尺寸超过逾渗阈值。**

---

## 受影响结论

| 结论 | 受影响程度 | 说明 |
|------|-----------|------|
| LP1-S3 K3.1 "MBL 在准周期势中严格稳定" | 🔴 需重审 | 当前判据用 L_max，需改用 L_eff |
| LP1-S3 K3.2 "数论保护=热力学稳定性" | 🟡 需精确化 | 结论可能从"严格稳定"降为"L_eff 边界条件依赖" |
| LP1-综合推导 "2D MBL 是真正的热力学相" | 🟡 需 caveat | 需标注 ζ 和 W/g 参数窗口 |
| LP1-补7 K7.2 "非可分离 WPL 宽度 ≪ ξ_perc" | 🟢 可能强化 | WPL 上 Griffiths 尾巴为幂律衰减（非指数）→ 非可分离情形更脆弱 |

---

## 下游任务

1. **数值验证**：在 LP-1 参数域中计算 L_eff 的精确分布（需量子波函数求解）
2. **论文 caveat**：LP-1 论文必须标注 "稳定性的严格形式要求 L_eff < ξ_perc，当前仅验证了 L_max < ξ_perc"
3. **后续子命题**：开立 LP1-补12（Griffiths尾巴定量 + 数值验证）

---

## 状态

- **卡点编号：** CP-Griffiths-001
- **严重性：** 高
- **状态：** 定量分析已完成 → GriffithsTail-Analysis.md
- **分析日期：** 2026-06-01
- **核心结论：** L_eff > xi_perc 在81/81参数组合下成立 (用户指定的percolation参数化)，在S3参考参数化下14/81危险、18/81边界。声张需从"严格稳定"降级为"条件稳定" (Option C)。
- **责任人：** LP-1 综合推导 Phase
