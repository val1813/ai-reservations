# Bayesian Reflux Diagnostic — 概率化容量约束诊断

**核心:** 不回答"回流是否超过上界"——上界是鸽巢的数学必然。回答"给定你的数据，理论满足'每bit最多toggle一次'这个假设的概率是多少"。

---

## 1. 为什么概率化

鸽巢说：P_reflux ≤ B（数学保证）。但实际操作中：

- q_S和q_E是从有限样本估计的——有误差
- 不是所有forward capacity都被用满——实际forward events是随机变量
- 回流可能不是独立事件——有correlation结构
- 你测到的P_reflux = 0.35, bound = 0.40——算通过还是"太近了可疑"？

**确定性诊断回答不了"有多可信"。概率诊断可以。**

---

## 2. 模型

### H₀：理论满足容量约束
每个基本载体是bit（最多一次|0⟩→|1⟩）。鸽巢上界适用。

### H₁：理论不满足容量约束
载体可能有>1 bit容量，或可能多次toggle。鸽巢不适用。回流可能超过上界。

### 生成模型（H₀下）

```
给定: N_S, N_E, 以及初始q_S, q_E (从population tomography估计)

前向转移: 
  F ~ Hypergeometric(N_E, N_E·q_E, N_S·(1-q_S))
  # 解释: 从N_E个环境格点中, 最多N_E·q_E个|0⟩可被触发
  # F = 实际触发的前向转移数

回流:
  R | F ~ Hypergeometric(N_S, N_S·q_S, min(F, N_E·(1-q_E)))
  # 解释: 从N_S个系统格点中, N_S·q_S个|0⟩可被逆转
  # 但回流源只有min(F, N_E·(1-q_E))个已确定的E格点

观测:
  P_reflux_obs = R / C_F  其中 C_F = N_E·q_E
```

**超几何分布的理由：** 有限格点、不放回抽样——每个格点最多被选中一次。正是鸽巢的随机版本。

### 似然函数

```
L(H₀ | data) = P(P_reflux_obs | N_S, N_E, q_S, q_E, H₀)

通过蒙特卡洛从生成模型采样计算：

1. 从q_S, q_E的测量分布中抽样(如有误差估计)
2. 从Hypergeometric生成(F, R)
3. 计算P_reflux_sample
4. 重复N次→得P_reflux在H₀下的分布
5. 观测P_reflux_obs在此分布中的位置→p值
```

---

## 3. 输出

### 诊断报告格式

```
Bayesian Reflux Diagnostic v1.0
================================
Input:
  N_S=10, N_E=10
  q_S=0.30±0.05, q_E=0.50±0.05
  P_reflux(obs)=0.25

H₀ Distribution (N=10000 MC samples):
  Mean P_reflux = 0.18
  95% CI = [0.02, 0.42]
  
  Observed P_reflux = 0.25
  → Within 95% CI → consistent with H₀

Bayes Factor (H₀ vs H₁_uniform):
  BF = 3.2 (moderate evidence for H₀)

Verdict: ✅ Theory consistent with capacity constraint
         (moderate confidence — larger sample recommended)
```

如果P_reflux_obs = 0.65 而95% CI = [0.02, 0.42]:
```
  → Outside 95% CI → unlikely under H₀

Bayes Factor = 0.08 (strong evidence against H₀)

Verdict: ⚠️ Theory inconsistent with capacity constraint
         Either: (a) carriers not bits, (b) multiple toggles,
         (c) q_S/q_E measurement error, or (d) H₀ wrong
```

---

## 4. 为什么这比确定性诊断好

| 方面 | 确定性 | 概率化 |
|------|:---:|:---:|
| 鸽巢上界 | 数学恒等 | 作为分布的支撑边界 |
| 测量误差 | 无法纳入 | q_S/q_E作为分布→bound作为分布 |
| "太近了可疑" | 无法回答 | p值/BF量化可信度 |
| 小样本 | 不可靠 | 更大的后验方差=诚实 |
| 拒绝H₀的替代解释 | "理论错了" | 列出多个可能(d) |

---

## 5. 诚实边界

1. **超几何模型假设独立不放回抽样**——真实物理中correlation存在。这是近似。
2. **H₁的specification**——"不满足容量约束"是很宽泛的备择假设。BF的具体数值依赖H₁的形式。
3. **先验选择**——如果给出后验概率（而非BF），需要先验。默认无信息先验。
4. **q_S/q_E的误差估计本身可能不准**——垃圾进垃圾出。

---

## 6. 怎么用

```python
# pseudocode
from bayesian_diagnostic import reflux_test

result = reflux_test(
    N_S=10, N_E=10,
    q_S_est=0.30, q_S_err=0.05,
    q_E_est=0.50, q_E_err=0.05,
    P_reflux_obs=0.25,
    n_mc=10000
)

print(result.verdict)     # "consistent" or "inconsistent"
print(result.bayes_factor) # 3.2
print(result.ci_95)        # [0.02, 0.42]
```

**不依赖DGF框架。不依赖静态→动态桥。只依赖：鸽巢上界 + 超几何抽样 + 贝叶斯推断。**
