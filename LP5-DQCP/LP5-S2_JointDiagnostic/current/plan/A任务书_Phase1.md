# A 博士任务书 — LP5-S2' Phase 1

**课题：** LP5-S2' DQCP 多观测量联合诊断
**Phase：** 1（数据汇编 + 信号强度分解）
**价值分类：** [核心]

---

## 攻击目标

**核心问题：** 已有多个独立观测量各自给出 DQCP 一阶 vs 连续的信号（EE对数修正、关联长度指数ν、Binder cumulant、emergent SO(5)），但各自单独达不到 3σ。联合它们能否达到？

## 任务

### 第1步：数据汇编

从已发表文献中提取 DQCP 数值结果：

| 观测量 | 来源 | 结论方向 | 置信度 |
|--------|------|---------|--------|
| EE 对数修正 b | Deng (b≈2→连续), D'Emidio-Sandvik (a≈0→一阶) | 矛盾 | ~2σ each |
| 关联长度指数 ν | Takahashi (ν_t≈0.63→一阶, L=1024) | 一阶 | ~3σ |
| Binder cumulant | 待汇编 | ? | ? |
| SO(5) emergent symmetry | 待汇编 | ? | ? |

### 第2步：层次贝叶斯信号分解

对每个观测量 O_i：
- 模型 M_cont: O_i ~ f_i^cont(L, θ) + noise
- 模型 M_1st: O_i ~ f_i^1st(L, θ) + noise  
- 计算 Bayes factor BF_i = P(data|M_cont)/P(data|M_1st)

### 第3步：联合诊断

- 假设各观测量独立 → log BF_joint = Σ log BF_i
- 计算达到 3σ（log BF=3）所需的最小系统尺寸 L_min
- 若 L_min ≤ 512 → 联合诊断可行
- 若 L_min > 512 → 需更大系统或新观测量

---

文件：D:\Claude\ai-reservations\LP5-DQCP\LP5-S2_JointDiagnostic\current\A\Phase1_A_output.md
