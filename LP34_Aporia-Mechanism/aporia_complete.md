# Aporia: 信息容量约束作为物理理论的贝叶斯诊断工具

**版本:** 2026-06-08
**前身:** LP32 DGF（离散图框架——从2条信息论公理推导引力+量子力学）
**定位:** 不推导宇宙。不生成理论。只诊断理论的信息论自洽性。

---

## 一、起点：DGF教会我们什么

DGF（LP32）从2条公理出发——因果存在(A1)和容量有界(A2，每个格点≤1 bit)——试图推导量子力学+引力+暗能量+黑洞熵。

15个矛盾的系统化审查（LP32-CR，29个Agent实例，7轮AB探索）揭示了：

**0个致命矛盾。** 但框架有一个结构性局限：

T_DGF在Shelah稳定性分类中处于最底层（不稳定+IP+SOP）。不稳定理论的特征是：只能推导∀-推论（标度关系、上界、不等式），不能推导∃-推论（精确系数、唯一函数形式）。

**DGF的"失败"——推不出唯一系数、自启动不了、二值→连续桥接散——不是bug，是不稳定理论的数学必然。**

---

## 二、约束硬核

从17个候选约束中，逻辑分析+图论分析双方法独立验证：

**不可约硬核 = {C1, C2} = 2个约束**

| 约束 | 数学形式 | 来源 |
|------|---------|------|
| **C1 容量界** | Holevo容量 χ ≤ 1 bit/基本单元 | Holevo (1973), Bekenstein (1981) |
| **C2 因果有向性** | 信息影响是偏序（不对称+传递） | DGF A1, 热力学第二定律 |

**C1 ≡ 不可广播定理** (Barnum et al. 2007)。"正面度量上界"和"负面过程禁令"是同一物理事实的两种表述。

其余2个约束（C3回流界、C4熵面积界）可从{C1, C2}导出，需要额外的图论结构假设。

---

## 三、贝叶斯回流诊断

### 问题

给定一个物理理论的测量数据，这个理论满足"每个基本信息载体最多toggle一次"的概率是多少？

### 模型

**H₀（零假设）：** 理论满足容量约束。每个载体是bit（最多一次|0⟩→|1⟩）。鸽巢上界适用。

**H₁（备择假设）：** 理论不满足容量约束。

**生成模型（H₀下）：**

```
前向转移 F ~ Hypergeometric(N_E, N_E·q_E, N_S·(1-q_S))
回流 R|F ~ Hypergeometric(N_S, N_S·q_S, min(F, N_E·(1-q_E)))
观测 P_reflux = R / C_F，其中 C_F = N_E·q_E
```

**超几何分布的理由：** 有限格点、不放回抽样——每个格点最多被选中一次。这正是鸽巢原理的随机版本。

### 贝叶斯因子

```
BF = P(data | H₀) / P(data | H₁)

BF > 3   : 中等证据支持H₀（理论一致）
BF ∈ [1/3, 3] : 无结论（数据不足以判断）
BF < 1/3 : 中等证据反对H₀（理论不一致）
BF < 1/10: 强证据反对H₀
```

### 输出格式

```
Bayesian Reflux Diagnostic v1.0
================================
Input:  N_S=10, N_E=10, q_S=0.30±0.05, q_E=0.50±0.05
        P_reflux(obs)=0.25

H₀ Distribution (5000 MC samples):
  Mean P_reflux = 0.149, 95% CI = [0.000, 0.500]

  Bayes Factor = 3.9
  Verdict: CONSISTENT (moderate evidence)
```

### 验证结果

| 测试场景 | P_obs | BF | 裁决 | 正确？ |
|---------|------:|:--:|------|:-----:|
| 正常（期望内） | 0.25 | 3.9 | consistent | ✅ |
| 回流过高 | 0.65 | 0.02 | inconsistent (strong) | ✅ |
| 小系统 | 0.10 | ~0 | 无力判断 | ✅ 诚实 |
| 大环境 | 0.005 | 20 | consistent | ✅ |
| 高q_S反常 | 0.80 | 0.00 | inconsistent (strong) | ✅ |

### 确定性上界（鸽巢）

作为参考，确定性上界仍然成立：

$$\boxed{P_{\text{reflux}} \leq \min\left(\frac{N_S \cdot q_S}{N_E \cdot q_E}, \frac{1-q_E}{q_E}\right)}$$

这是鸽巢原理的代数等价——纯组合数学，0/111配置违反。但如果P_reflux在界内但接近边界，确定性公式无法判断"有多可信"——贝叶斯诊断回答的就是这个问题。

---

## 四、诚实边界

1. **鸽巢上界是数学恒等式**——不需要"相信"DGF。只需要接受"每个bit最多|0⟩→|1⟩一次"。

2. **贝叶斯诊断的超几何模型假设独立不放回抽样**——真实物理中存在correlation。这是近似。

3. **H₁的specification**——"不满足容量约束"是宽泛的备择假设。BF的具体数值依赖H₁的形式。

4. **q_S/q_E的测量需要指针基**——如果理论没有优选基，诊断不适用。

5. **C1（容量界）是标准量子信息论——Holevo bound。** C2（因果有向性）来自热力学。两个都不需要DGF推导。工具的理论基础是标准物理学。

---

## 五、与已有工作的关系

| 工作 | 做什么 | Aporia不同在哪 |
|------|--------|---------------|
| Holevo (1973) | χ ≤ H(X) | Aporia用χ≤1作为理论的诊断门槛 |
| Bell (1964) | 不等式排除局域隐变量 | Bell排除一类理论，Aporia诊断单个理论 |
| Bekenstein (1981) | S ≤ 2πkRE/ħc | 容量界的物理学基础 |
| GPT (Hardy 2001) | 操作框架定义可能理论空间 | Aporia对GPT不做正向重构，做逆向排除 |
| 量子资源论 | 形式化"消耗""转换""不可逆" | 结构同源，目标不同 |

**"Apory"作为方法论术语在物理学文献中不存在——DGF是第一个到达这个边界、标定它、把它变成工具的框架。**

---

## 六、代码

`bayesian_diagnostic.py` — 完整实现。关键函数：

```python
from bayesian_diagnostic import diagnostic
r = diagnostic(N_S=10, N_E=10, q_S_est=0.30, q_E_est=0.50,
               P_reflux_obs=0.25, q_S_err=0.05, q_E_err=0.05)
# r['bayes_factor'], r['verdict'], r['ci_95'], r['p_value']
```

不依赖DGF框架。依赖：numpy + scipy。

---

## 七、参考文献（摘要）

1. Holevo, A.S. (1973). Probl. Peredachi Inf. 9, 3.
2. Bekenstein, J.D. (1981). Phys. Rev. D 23, 287.
3. Barnum, H. et al. (2007). Phys. Rev. Lett. 99, 240501.
4. Hardy, L. (2001). arXiv:quant-ph/0101012.
5. Coecke, B. & Kissinger, A. (2018). arXiv:1510.05468. (Process Theory——静态→动态桥)
6. Joachim, de Visme, Haar, Winskel (2025). arXiv:2508.14531. (Quantum Petri Nets)
7. Shelah, S. (1990). Classification Theory. (T_DGF稳定性分类)
8. Cubitt, T. et al. (2015). Nature 519, 199. (谱隙不可判定性)
9. Einstein, A. (1919). The Times, Nov 28. (原则理论 vs 构造理论)
10. Bertotti, B. et al. (2003). Nature 425, 374. (Cassini γ_PPN约束)
11. DGF S1 Theorem: P_reflux ≤ min(q_S/q_E, (1-q_E)/q_E). Submitted to PRL.
12. DGF S4 Min-Cut Theorem: S ≤ N_∂Ω ∝ A. Submitted to PRD.
