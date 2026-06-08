# S1定理数值估算
## 信息回流上限：用已发表实验参数的验证

**日期：** 2026-06-06
**用途：** 论文Section V的数值支撑，标注为"proposed experimental test"

---

## 一、S1定理

**定理陈述：**

在任何有界信息系统中，系统S向环境E的信息回流幅度满足：

$$\boxed{P_{reflux} \leq \frac{q_S}{q_E}}$$

其中：
- $q_S$：系统的有效空余容量比（可操作近似：$q_S \approx T_2/(T_1+T_2)$）
- $q_E$：环境的有效空余容量比
- $P_{reflux}$：迹距离的最大复活幅度

**与标准Lindblad的差别：**
- 标准Lindblad（零温）：$P_{reflux} = 0$（严格）
- DGF S1定理：$P_{reflux} \leq q_S/q_E$（非零上界）

---

## 二、实验参数来源

### 参数集A：Yale 3D腔
**来源：** Vlastakis et al., Yale University, 已发表

| 参数 | 数值 |
|------|------|
| $T_1$（qubit） | 6.4 μs |
| $T_2^{echo}$ | 11.7 μs |
| $g/2\pi$（耦合强度） | 49 MHz |
| 腔寿命 | 34.3 μs |

### 参数集B：标准transmon（文献典型值）
**来源：** Koch et al., 电路QED综述

| 参数 | 数值 |
|------|------|
| $T_1$ | 10–100 μs |
| $g/2\pi$ | 100 MHz |
| $\kappa/2\pi$（腔衰减） | 1 MHz |
| qubit频率 | 5 GHz |

### 参数集C：IBM 127-qubit处理器
**来源：** arXiv:2510.12894（2025），非马尔可夫噪声表征

| 参数 | 数值 |
|------|------|
| $T_1$ | ~100 μs |
| $T_2$ | ~50 μs |
| 观测到的迹距离复活幅度 | ~5% |
| 处理器温度 | ~10 mK |

---

## 三、q值的操作定义

**注意：** $q$与实验可测量量的精确映射是开放问题（O5）。以下使用操作近似：

$$q_S \approx \frac{T_2}{T_1 + T_2}$$

**物理动机：** $T_2$描述相位相干性（量子容量），$T_1$描述能量弛豫（容量锁定）。比值近似描述系统"还有多少空余量子容量"。

**环境q值估算：**
- 大环境（多模腔/大量qubit）：$q_E \approx 0.85–0.95$
- 小环境（单模腔）：$q_E \approx 0.3–0.5$

---

## 四、数值结果

### 四种情况的S1上界

| 情况 | $q_S$ | $q_E$ | DGF上限 $q_S/q_E$ | Lindblad预言 |
|------|--------|--------|-------------------|-------------|
| 高相干qubit + 大腔 | 0.80 | 0.90 | 0.889 | 0.000 |
| 高相干qubit + 小腔 | 0.80 | 0.30 | 2.667* | 0.000 |
| 低相干qubit + 大腔 | 0.20 | 0.90 | 0.222 | 0.000 |
| 低相干qubit + 小腔 | 0.20 | 0.30 | 0.667 | 0.000 |

*注：上界>1时无约束力，系统不在DGF的适用范围内（$q_S > q_E$意味着信息从环境流向系统）

### IBM 127-qubit数据的初步验证

$$q_S = \frac{50}{100+50} = 0.333, \quad q_E = 0.85$$

$$\text{DGF上界} = \frac{0.333}{0.85} = 0.392$$

$$\text{IBM观测回流幅度} \approx 0.05 \leq 0.392 \quad \checkmark$$

**结论：** IBM已发表数据与S1定理一致。

---

## 五、建议实验方案

**目标：** 在零温极限下区分DGF和标准Lindblad

**装置：** IBM量子计算机（现有，无需新实验室）或电路QED装置

**步骤：**

1. 准备两个正交初态 $|0\rangle$ 和 $|1\rangle$
2. 让系统自由演化，时间步长 $t = 0, T_1/10, T_1/5, \ldots, T_1$
3. 测量迹距离 $D(\rho(t), \sigma(t))$
4. 记录 $D$ 的最大复活幅度 = 信息回流幅度 $P_{reflux}$
5. 改变环境大小（改变耦合qubit数量），重复测量
6. 验证 $P_{reflux} \leq q_S/q_E$ 是否成立

**判决标准：**

| 实验结果 | 含义 |
|---------|------|
| 零温下 $P_{reflux} > 0$ 且 $\leq q_S/q_E$ | 支持DGF，标准Lindblad被证伪 |
| 零温下 $P_{reflux} = 0$ | 支持Lindblad，DGF被证伪 |
| 零温下 $P_{reflux} > q_S/q_E$ | DGF被证伪 |

**与现有工作的关系：**

IBM 127-qubit处理器上已观测到迹距离和量子相对熵的复活现象，证实了信息从环境回流到qubit，这与标准Lindblad的预言矛盾，与DGF的S1定理一致。

---

## 六、诚实声明

**这个估算的局限：**

1. $q_S \approx T_2/(T_1+T_2)$ 是操作近似，不是严格推导（开放问题O5）
2. IBM数据的"5%回流幅度"是从已发表论文图中读取的估算值，非精确数值
3. $q_E$的估算依赖对环境规模的假设，未精确测量

**这个估算能说明什么：**

- S1定理与现有实验数据不矛盾
- 提供了一个可设计的实验方案来精确检验
- 给出了DGF和Lindblad的可区分判决标准

**论文中应标注为：**

> "Proposed experimental test. The numerical estimates use published parameters from [refs]. The precise mapping between $q$ and experimental observables remains an open problem (O5)."

---

## 七、参考文献

1. arXiv:2510.12894 — IBM 127-qubit非马尔可夫噪声表征
2. Vlastakis et al., Yale — 3D腔参数
3. arXiv:2312.05329 — transmon电路QED综述参数
4. arXiv:2302.09092 — transmon非马尔可夫效应的smoking-gun特征
5. npj Quantum Information (2020) — IBM Q作为开放量子系统实验平台

