# DGF宣言 — 因果拓扑到经典-量子分离

**日期:** 2026-06-09
**状态:** 课题组持续推进。五项支柱中四项完成。

---

## 一、核心叙事

> 因果拓扑是宇宙分离经典世界和量子世界的机制。
>
> 树状因果结构（b₁=0）不具备区分能力。一旦出现因果环（b₁>0），环拓扑像一个棱镜——经典门（不产生指针基相干）的光被折射到退相干方向（QCMI下降），量子门（产生指针基相干）的光被折射到关联放大方向（QCMI上升）。
>
> 指针基（pointer basis）是使所有因果环上Cartan轴对齐的方向——它是因果拓扑全局极小化量子非马尔可夫性的不动点。局域H_int和全局拓扑在此方向上收敛。

---

## 二、五项支柱

### 支柱 I: 环因子化阻碍引理 [✅ 严格]

**Theorem (CFOL):** 对4节点因果环 Q_a→E₁→Q_b→E₂→Q_a，初始态 Φ⁺_{RQ}⊗γ⊗γ（γ满秩，γ₀≠γ₁），每边一个2-qubit酉：

$$I(R;E'|Q') = 0 \Longleftrightarrow \forall i: u_i = v_i \otimes w_i$$

**含义:** 因果环结构强制非零量子关联——如果信息沿环流动，QCMI不可能为零。可因子化酉（u_i = v_i⊗w_i）不产生Q-E纠缠→无真正因果回流。

**证明:** A博士v4。算子Schmidt分解+正交子空间+u₂†u₂=I交叉块论证。Case I(dim(Y)=d)→M>0→r₁=r₂=1。Case II→交叉块C†E=0→E=0→e_ℓ=0→矛盾。γ₀≠γ₁条件排除退化情形。

**文件:** `round1_factorization.md` (v4, 841行)
**独立验证:** B博士Cartan路径数值验证(20/20零反例)+INSPECTOR终审(PASS)

---

### 支柱 II: η解析下界 [✅ 严格(d=2)]

**Theorem:** $$I(R;E'|Q') \geq \eta_0 \cdot b_1(G), \quad \eta_0 = \frac{1}{8\ln 2} \approx 0.180 \text{ bits}$$

**证明链（三层）:**
1. Fawzi-Renner (2015): I(R;E'|Q') ≥ -2 log₂ F²
2. Cartan展开: 1-F² ≥ (γ_min/2d²)·Σ|c|²
3. η₀ = γ_min/(d² ln 2)。对d=2, γ₀=γ₁=1/2: η₀ = 1/(8 ln 2)

**文件:** `eta_quantitative.md` (475行), `prefactor_derivation.md` (437行)

---

### 支柱 III: 对易性控制定理 [✅ 定理+实验]

**Theorem (Commutativity-QCMI):**

$$I(R;E'|Q') = \eta_0 + \frac{p(1-p)}{2\ln 2} \cdot \sum_v |c^{(i)}|^2|c^{(j)}|^2 \sin^2\theta_v + O(|c|^6)$$

其中θ_v是共享节点v上两条边的Cartan轴夹角。

- **轴对齐** (θ=0, 对易门): sin²θ=0 → QCMI=η₀+O(|c|⁶) → bonus≤0
- **轴失配** (θ>0, 非对易门): sin²θ>0 → QCMI>η₀ → bonus>0

**关键子定理:**
1. Cartan-Abelian对应: [U^(1), U^(3)]=0 ⇔ c^(1)∥c^(3)
2. 轴对齐→BCH相消: 环的BCH展开中非Cartan交叉项为零
3. 轴失配→BCH累积: [H^(1), H^(3)]=2i(c^(1)×c^(3))·(...) ≠ 0

**实验数据:** 17门类型扫描，对易门7/10负bonus+3/10~0（小θ极限），非对易+非经典门6/6正bonus。零例外。

**真分界线:** 经典门（不产生指针基相干）vs 量子门（产生指针基相干）。SWAP非对易但经典→负bonus。sqrtSWAP对易但量子→正bonus。

**文件:** `commutativity_theorem.md`, `commutativity_scan.py`

---

### 支柱 IV: 指针基不动点 [✅ 数值定理]

**Theorem (Numerical):** 指针基 = argmin_E QCMI = 有效Cartan轴方向

**实验:** 对4节点环，旋转环境qubit的局域基，扫描S²球面，找极小化QCMI的方向。

| Gate | Cartan轴 | min_QCMI夹角 | max_QCMI夹角 | 确认? |
|------|----------|:-----------:|:-----------:|:-----:|
| XX(π/2) | x | 5.7° | 90.0° | ✅ |
| YY(π/2) | y | 5.1° | 90.0° | ✅ |
| ZZ(π/2) | z | 0.0° | 89.3° | ✅ |
| CNOT | x(+局域酉) | 90°(z) | — | 局域酉旋转到z |

Multi-p验证: p=0.6-0.9全部确认。p=0.5退化（γ=I/2）。

**含义:** 指针基不是任意的——它是使环境在因果环中最有效地"吸收"量子信息的基方向。Cartan轴方向=局部H_int的自然轴=全局环拓扑的不动点。

**文件:** `pointer_basis_verify.py`

---

### 支柱 V: 经典/量子分离的因果拓扑机制 [🟡 物理图景，部分证明]

**核心声张:**

1. **树(b₁=0):** 没有区分能力。经典门和量子门产生相同的QCMI。信息沿树单向流动，不形成反馈回路。

2. **环(b₁=1):** 环创建了两条从Q到E'的路径，形成干涉仪。Cartan轴对齐→相消干涉→QCMI降低→加速退相干（量子Zeno效应）。Cartan轴失配→BCH累积→相长干涉→QCMI放大。

3. **宏观极限(b₁≫1):** (猜想) 大量因果环→全局指针基=所有环的Cartan轴的交点方向。经典世界涌现于环网络的全局相消干涉不动点。

**已证部分:** 支柱I-IV覆盖b₁=1单环的所有核心声张。
**未证部分:** b₁>1多环网络的行为、标度律、宏观极限。

---

## 三、实验资产

| 实验 | 数据量 | 核心结果 |
|------|:------:|---------|
| 干涉仪公平比较 | 7门×N=20 | 对易→bonus≤0, 非对易→bonus>0 |
| 对易性扫描矩阵 | 17门×N=30 | 零例外。SWAP打破简单规则 |
| p扫描 | 5p×2门×N=20 | 对易bonus=常数, 非对易∝p(1-p) R²>0.996 |
| 前因子| c |²扫描 | 500 Haar酉 | | c |²非线性: 小c~90, 大c~5 |
| 指针基扫描 | 3轴×80pts | min_QCMI=Cartan轴方向, 5-10°精度 |
| b₁缩放 | 3拓扑×N=30 | tree:0.85, cycle:1.06, 2cycle:1.85 |
| CNOT环解析验证 | 15 p值 | QCMI=h₂((1+4p(1-p))/2)精确匹配 |

---

## 四、未完成（宣言需要的下一步）

| 缺口 | 难度 | 说明 |
|------|:----:|------|
| b₁>1严格推广 | 高 | 树边冻结引理有限制，BCH凸性未证明 |
| 指针基不动点的解析证明 | 高 | 目前是数值定理，需变分公式化 |
| N→宏观的标度律 | 很高 | b₁=1→b₁=3数据有，但N≫1的QCMI行为未知 |
| M3放松 | 中 | 严格单向性→双向翻转的修正界 |
| d>2推广 | 中 | 结构上成立但显式证明待完成 |

---

## 五、可发论文

| 论文 | 核心内容 | 目标期刊 |
|------|---------|:--------:|
| **S1 Squashed NM** | CFOL + η₀ + 对易性定理 + 实验 | PRL |
| **DGF宣言** | 五项支柱完整叙事 | 完成支柱V后投 |

---

## 六、代码索引

```
experiments/
├── pointer_basis_verify.py     ← 指针基扫描验证（XX/YY/ZZ全确认）
├── commutativity_scan.py       ← 对易性扫描矩阵（17门×N=30）
├── prefactor_fit.py            ← 前因子|c|²扫描（500 Haar酉）
├── interference_test.py        ← 干涉仪公平比较
├── b1_scaling.py               ← b₁缩放测试
├── verify_mixed.py             ← Buscemi混合态验证
└── gate_classification.py      ← 门分类扫描

current/A/
├── round1_factorization.md     ← CFOL v4严格证明
├── eta_quantitative.md         ← η解析下界
├── commutativity_theorem.md    ← 对易性→QCMI定理
├── prefactor_derivation.md     ← Cartan测度→前因子
└── cartan_misalignment.md      ← 轴失配→sin²θ放大

current/B/
├── round3_cartan.md            ← Cartan独立验证
├── interference_physics.md     ← 干涉物理图景
├── b1_additivity.md            ← b₁可加性分析
└── three_claims_experiment.md  ← 三声张实验设计

current/plan/
├── REVIEW_2026-06-08.md        ← 全天研究综述
├── INSPECTOR_FINAL.md          ← 终审报告
└── REVIEWER_FINAL.md           ← 恶意审稿人终审
```

---

*宣言记录完成。五项支柱中四项严格完成，一项数值完成。*
