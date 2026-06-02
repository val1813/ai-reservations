# B 博士任务书 — LP5-S2' Phase 1

**课题：** LP5-S2' DQCP 联合诊断
**Phase：** 1（攻击联合诊断的逻辑基础）
**价值分类：** [防守/核心]

---

## 攻击目标

检验 "联合多个不够显著的观测量能达到 3σ" 的逻辑是否有根本缺陷。

## 三条攻击链

### 攻击 1：观测量独立性假设
联合诊断假设各观测量独立（log BF_joint = Σ log BF_i）。但 EE、ν、Binder cumulant 都从同一 QMC 数据的同一组态计算——它们高度相关！

**跨域工具：** 多元统计中的 copula 模型。若观测量相关，有效独立观测量数 n_eff < n_nominal → 真实 log BF_joint 小于名义值。

### 攻击 2："方向矛盾"的不可调和性
Deng 的 EE (b≈2→连续) 和 D'Emidio-Sandvik 的 EE (a≈0→一阶) 用的是同一观测量但得出相反结论！
- 这不能被"联合"解决——这是方法论分歧，不是统计不足。
- 任何联合诊断必须先解决这个矛盾。

**具体攻击：** 如果在联合框架中先验地选 Deng 的 b≈2 作为输入（忽略 D-S 的 a≈0），联合诊断可能偏向"连续"结论。反之亦然。这不是客观的联合诊断——这是先验驱动的结论选择。

### 攻击 3：Takahashi 的结果是否使联合诊断 moot
Takahashi et al. (L=1024) 用关联函数独立确认一阶（ν_t≈0.63, β≈0.85）。如果这个结果的置信度已经接近或超过 3σ，那么联合诊断的边际价值是什么？

**检验：** 计算 Takahashi 结果的独立 Bayes factor。若 log BF_Takahashi > 2 → 联合诊断的新增信息量有限 → 论文应写成 "Takahashi 已经基本解决 + 联合诊断提供交叉验证" 而非 "联合诊断首次区分"。

---

文件：D:\Claude\ai-reservations\LP5-DQCP\LP5-S2_JointDiagnostic\current\B\Phase1_B_output.md
