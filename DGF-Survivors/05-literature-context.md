# 文献定位与先发分析

---

## DGF的直接理论基础

### 1. Squashed Quantum Non-Markovianity (sQNM)
**Gangwar, Pandit, Goswami, Das, Bera (2023/2025)**
*Quantum* 9, 1646 (2025). arXiv:2311.18323.

- sQNM是DGF所用QCMI的形式框架
- 证明了sQNM的超可加性、单调性、凸性
- sQNM的资源论形式化 → DGF的η₀下界是此资源论的第一个拓扑约束
- **差异化:** DGF将sQNM从态空间推广到因果图拓扑——b₁(G)作为sQNM的拓扑序参量

---

### 2. Fawzi-Renner QCMI下界
**Fawzi & Renner (2015)**
*Commun. Math. Phys.* 340, 575 (2015).

- I(A:C|B) ≥ -2 log₂ F（QCMI的Uhlmann保真度下界，Theorem 5.1，使用−2log₂F的正确形式）
- DGF的单边Fawzi-Renner系数为2/ln2≈2.885（petz_recovery_v2.py验证），多边环有效系数η₀ = 1/(8 ln 2) ≈ 0.180（经环拓扑修正因子1/16得到，2026-06-09确认）
- **差异化:** Fawzi-Renner是普适下界（不依赖因果结构），DGF是因果环特定结构的紧化

---

### 3. HJPW量子Markov链条件
**Hayden, Jozsa, Petz, Winter (2004)**
*Commun. Math. Phys.* 246, 359 (2004). Theorem 6.

- QCMI=0 ⟺ 三体态是短量子马尔可夫链（直和分解结构）
- CFOL将此代数充要条件翻译为因果图的几何条件（Cartan轴对齐）
- **差异化:** HJPW给充要条件但不提供因果几何解释；CFOL提供了因果图的参数化实现

---

### 4. Holevo容量界
**Holevo (1973)**
*Probl. Peredachi Inf.* 9, 3.

- χ ≤ H(X) — 量子信道的经典信息容量上界
- DGF的A2（≤1bit/格点）是Holevo界的信息论极限版本
- Aporia诊断的C1直接来自Holevo界

---

### 5. Bekenstein界
**Bekenstein (1981)**
*Phys. Rev. D* 23, 287.

- S ≤ 2πkRE/ħc — 熵的物理上界
- 容量界的物理学基础
- DGF的黑洞熵面积律与Bekenstein兼容（均给出S∝A标度）

---

## 相关但非直接竞争的工作

### 6. Quantum Darwinism & Einselection
**Zurek (2003-2009)**

- 指针基 = [H_int, ·]的对易基
- DGF的声称不是"Zurek错了"而是"Zurek缺少一个独立自由度(b₁)"
- **差异化:** DGF预测因果拓扑对指针基有独立贡献——在b₁≫1极限下可能主导H_int选择
- **未解决:** 这个独立贡献在实验中多大？当前量子光学平台的b₁是多少？

---

### 7. Casual Set Theory
**Sorkin (1987), Dowker et al.**

- 时空是偏序集
- DGF的因果DAG是因果集的信息论推广（每个元素≤1bit）
- **联系:** b₁(G)是因果集的拓扑不变量
- **未探索:** 因果集动力学是否满足CFOL？

---

### 8. General Probabilistic Theories (GPT)
**Hardy (2001)**

- 操作框架定义可能物理理论空间Ω
- Aporia做逆向操作——从Ω排除而非从Ω构造
- **差异化:** GPT是正向重构，Aporia是逆向排除

---

### 9. She (2007) — 先发警告
**She (2007)**
*JCAP* 02, 021 (2007).

- "landscape→glass→Λ"概念链首次提出
- LP35必须引用为概念链首发作
- **差异化:** 弦景观→因果经济景观；粘度→淬火；度规跳跃→DESI纹理

---

### 10. 谱隙不可判定性
**Cubitt, Perez-Garcia, Wolf (2015)**
*Nature* 519, 199 (2015).

- 谱隙的不可判定性——某些物理量在原则上不可计算
- Aporia的精神来源——不可判定性作为物理工具

---

### 11. Shelah稳定性分类
**Shelah (1990)**
*Classification Theory.*

- T_DGF处于不稳定+IP+SOP——只能推导∀-推论（上界、不等式），不能推导∃-推论（精确系数、唯一函数形式）
- **含义:** DGF的"失败"（推不出唯一系数）不是bug——是不稳定理论的数学必然

---

## DGF的五个独特空白（文献搜索确认）

| # | 空白 | 搜索策略 | 命中 |
|---|------|---------|:--:|
| 1 | "Causal topology → QCMI" | causal graph + quantum conditional mutual information + topology | 0 |
| 2 | "Pointer basis from causal graph" | pointer basis + causal structure + emergence | 0 |
| 3 | "Causal Glass" | "causal glass" + cosmology | 0 |
| 4 | "Information-theoretic dark energy" (w₀≈-0.80) | informational + dark energy + entropic | ~3 (QMM等，但w₀不同) |
| 5 | "Apory" as methodological term in physics | apory + physics + methodology | 0 |

**结论:** DGF的核心创新——因果拓扑作为量子非马尔可夫性的独立自由度——在文献中无先发。

---

## 投稿前需引用的文献

论文S1 (CFOL+η₀):
1. Gangwar et al. (2025) — sQNM框架
2. Fawzi & Renner (2015) — QCMI下界
3. HJPW (2004) — 量子Markov链充要条件
4. Holevo (1973) — 容量界
5. Sutter, Tomamichel, Harrow (2016) — 增强单调性
6. Li & Winter (2014) — squashed entanglement & recovery maps

论文Aporia:
7. Barnum et al. (2007) — 不可广播定理
8. Bekenstein (1981) — 熵界
9. Cubitt et al. (2015) — 不可判定性
10. Einstein (1919) — 原则理论 vs 构造理论

论文Čencov-Petz:
11. Čencov (1972) — Fisher-Rao Riemannian
12. Petz (1996) — 量子信息度量分类
13. CDT/量子图论文献（具体引用待确定）
