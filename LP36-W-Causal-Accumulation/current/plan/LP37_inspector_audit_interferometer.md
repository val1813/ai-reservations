# LP37 Inspector Audit: "因果环是量子干涉仪"假说

**审计日期**: 2026-06-08
**被审计实验**: `interference_test.py`
**审计脚本**: `audit_quick.py` (独立验证)
**结论等级**: **假说被推翻，核心声张为实验伪迹**

---

## 一、审计方法

在原实验代码基础上执行了7组独立验证测试：

| 测试 | 目的 |
|------|------|
| Test 1 | 闲置E qubit是否会改变QCMI |
| Test 2 | Tree的E-E gate是否虚增QCMI |
| Test 3 | **公平比较**: 固定n_E=3，tree vs cycle |
| Test 4 | 弱CNOT扫描：区分"无干涉"与"饱和" |
| Test 5 | 重现XX(pi/2) tree=2.0, cycle=1.0 |
| Test 6 | XX(theta)扫描，固定n_E=3 |
| Test 7 | 分解tree QCMI的驱动因素 |

---

## 二、发现1（致命）：n_E不匹配是伪迹来源

### 原实验的不公平性

原实验的树(tree)使用 **n_E=3**（3个环境qubit），环(cycle)使用 **n_E=2**（2个环境qubit）。这是**设计上的混淆变量**：

| 拓扑 | Q-E gate数 | E-E gate数 | 总gate数 | n_E | b1 |
|------|:--:|:--:|:--:|:--:|:--:|
| Tree | 3 | 1 | 4 | 3 | 0 |
| Cycle | 4 | 0 | 4 | 2 | 1 |

tree和cycle在三个维度上不同：(1)拓扑 (2)E qubit数量 (3)Q-E gate数。无法将bonus符号归因于任何一个。

### 公平比较的结果

当**固定n_E=3**进行公平比较（Test 3），原始假说崩溃：

```
原实验 (tree n_E=3, cycle n_E=2):
  XX(pi/2):    tree=2.0000  cycle=1.0000  bonus=-1.00  (commuting, negative) ✓
  Haar(full):  tree=3.0790  cycle=3.2220  bonus=+0.14  (non-commuting, positive) ✓

公平比较 (both n_E=3):
  XX(pi/2):    tree=2.0000  cycle=1.0000  bonus=-1.00  (commuting, negative)
  Haar(full):  tree=3.8457  cycle=3.3747  bonus=-0.47  (non-commuting, NEGATIVE!) ✗✗✗
```

**Haar bonus符号翻转**: 从+0.14变为-0.47。原实验的"非对易→相长干涉(正bonus→cycle>tree)"是**n_E混淆的人为产物**。

### 声张3的直接反驳

> "所有对易门都给出cycle<tree（负bonus），所有非对易门都给出cycle>tree（正bonus）"

**错误**。当控制n_E后，Haar(非对易)也给出负bonus。bonus符号由n_E差异驱动，不由门的对易性驱动。

---

## 三、发现2：声张1（干扰仪类比）缺乏机制支持

### E-E gate不贡献QCMI

Test 2显示：tree中E2-E3 gate对所有gate类型的QCMI贡献为**0.0000**：

```
CNOT:      with E2-E3=2.7626  without=2.7626  delta=+0.0000
XX(pi/2):  with E2-E3=2.0000  without=2.0000  delta=-0.0000
Haar:      with E2-E3=3.8457  without=3.8457  delta=-0.0000
```

E-E gate不产生额外的R-E'相关性——因为E qubit间的纠缠不会传递R的信息到E'。这意味着tree的高QCMI完全来自3条Q-E边，而非E-E边带来的"额外路径"。

### 干涉仪类比的问题

干涉仪类比假设：
- 环中两条路径(Q_a→E1→Q_b→E2 和 Q_a→E2直接)产生干涉
- 对易门→相消干涉(cycle<tree)，非对易门→相长干涉(cycle>tree)

三个问题：
1. **公平比较下bonus总是负**：即使对非对易门，cycle也小于tree。环总是"减少"QCMI，而不是有时增加、有时减少。这不是干涉仪——干涉仪会根据相位差产生正或负的干涉。这里一律是负的。
2. **tree有更少的Q-E边却QCMI更大**：tree只有3条Q-E边而cycle有4条，但tree的QCMI更大。这说明环的第4条Q-E边"破坏"了前3条边建立的部分相关性。这更像是一个"相关性稀释"效应而非干涉。
3. **CNOT的cycle=tree=2.7626不是"无干涉"**：Test 4弱CNOT扫描显示，小theta时tree≠cycle(bonus≈0)。全CNOT的tree=cycle可能是饱和效应（QCMI接近上限4），掩盖了tree和cycle的真实差异。

---

## 四、发现3：声张2（CNOT无干涉因基对齐）不可靠

### 弱CNOT扫描驳斥"基对齐"解释

如果CNOT的tree=cycle是因为"门和环境基对齐"（经典门不产生干涉），那么弱CNOT（partial CNOT, 同样基对齐）应该也是tree=cycle。但Test 4显示：

```
weak CNOT theta=0.05: tree=0.0060  cycle=0.0074  bonus=+0.0015
weak CNOT theta=0.10: tree=0.0205  cycle=0.0253  bonus=+0.0048
weak CNOT theta=0.20: tree=0.0686  cycle=0.0836  bonus=+0.0150
weak CNOT theta=0.50: tree=0.3161  cycle=0.3721  bonus=+0.0560
weak CNOT theta=1.00: tree=0.9123  cycle=1.0135  bonus=+0.1013
```

弱CNOT（同样基对齐）tree和cycle有明确差异。全CNOT的tree=cycle更可能是QCMI饱和（都接近上限4）掩盖了差异，而非"基对齐消除干涉"。

注意：弱CNOT测试仍使用n_E=3(tree) vs n_E=2(cycle)，所以bonus符号不可靠。但tree≠cycle这一事实本身反驳了"CNOT因基对齐而无法产生拓扑差异"的说法。

---

## 五、发现4：SWAP的极端反例

公平比较中SWAP给出bonus=-2.0000（tree=4.0000, cycle=2.0000），是所有gate中负bonus最大者。SWAP是对易门吗？SWAP和自身的Kronecker积确实对易（SWAP^2=I）。但SWAP的tree QCMI=4.0000意味着I(R;Q')=0——R和Q'之间完全无互信息。cycle的QCMI=2.0000意味着I(R;Q')=2。

如果干涉仪假说成立，SWAP作为对易门应该产生"相消干涉"(cycle<tree)。这里确实cycle<tree，但程度极端。问题是：SWAP是完全置换门，没有任何"相位"概念。它的"干涉"从何而来？

更自然的解释：SWAP在cycle中把Q_a和Q_b的信息通过两条路径交换到E，两条路径的"交换效应"部分抵消，导致cycle中Q保留更多信息（I(R;Q')=2 vs tree的0）。

---

## 六、发现5：b1角色的理论评估（声张4）

> "b1不是QCMI的来源，b1是干涉仪中路径数的度量"

公平比较已经否定了"干涉仪"假说本身，所以b1的干涉仪角色也随之不成立。

但b1确实与QCMI相关。从原始实验和公平比较都可以看出：
- b1=1的cycle和b1=0的tree给出不同的QCMI
- 即使控制n_E后，这个差异仍然存在（Test 3）

b1更合理的角色：b1是图的循环秩，度量了图中"冗余路径"的数量。冗余路径允许信息在Q-E之间以多种方式流动，这些多种流动方式之间可能产生**相关性抵消**（类似经典的去相关，而非量子干涉），导致环的QCMI比同等Q-E边数的树更低。

这不是干涉仪，这更像是"回路反馈抵消"（loop feedback cancellation）——环提供了反馈路径，使得部分从Q泄漏到E的信息又被"带回"Q。

---

## 七、bonus符号翻转的完整解释

原实验中Haar的positive bonus (+0.14) 可以解释为：

1. **Tree (n_E=3)**: 3 Q-E gates在更大的E空间（3 qubits, dim=8）中运行。3条Q-E边在5个顶点上构成b1=0树。
2. **Cycle (n_E=2)**: 4 Q-E gates在较小的E空间（2 qubits, dim=4）中运行。4条Q-E边在4个顶点上构成b1=1环。

对于Haar随机门，较小的E空间（n_E=2）意味着QCMI更容易"饱和"——4条Q-E边将几乎所有可能的R-Q信息泄漏到仅有2个E qubit的环境中。而在n_E=3时，E空间更大，QCMI的"容量"更高（可以容纳更多R信息而不饱和）。

所以cycle(n_E=2)的QCMI=3.222看似比tree(n_E=3)的3.079更大，不是因为cycle产生"相长干涉"，而是因为**cycle的E空间更小，导致相同Q-E边数下QCMI更接近上限**。

公平比较(都是n_E=3)消除了这个伪影：cycle的QCMI=3.3747，tree的QCMI=3.8457，cycle **小于** tree。额外的Q-E边在循环拓扑中"效率更低"——因为循环路径产生了相关性抵消。

---

## 八、审计结论

### 对各声张的判决

| 声张 | 判决 | 理由 |
|------|:--:|------|
| 声张1: 环是干涉仪，对易→相消，非对易→相长 | **✗ 推翻** | 公平比较下非对易门也给出负bonus |
| 声张2: CNOT无干涉因基对齐 | **✗ 存疑** | 弱CNOT仍有tree≠cycle；全CNOT的tree=cycle是饱和而非无干涉 |
| 声张3: 所有对易门→负，所有非对易门→正 | **✗ 推翻** | Haar在公平比较下给出负bonus；仅7个数据点，样本不足 |
| 声张4: b1是路径数度量 | **✗ 不成立** | 干涉仪假说本身被推翻，但b1作为循环秩的角色可以保留 |

### 什么是对的

以下观测是真实的（公平比较和原始实验都确认）：
1. **环的QCMI与树不同**：b1=1和b1=0的因果图确实给出不同的QCMI
2. **环通常减少QCMI**：与直觉相反，环（更多Q-E连接）反而给出更低的QCMI
3. **QCMI=4-I(R;Q')恒等式**：已验证，正确
4. **门类型影响QCMI幅度**：XX、ZZ、CNOT、Haar给出不同的绝对QCMI值
5. **拓扑和门的交互效应存在**：XX(pi/2)的bonus(-1.0)与ZZ(pi/2)的bonus(-0.78)不同，说明门的性质确实调节拓扑效应

### 什么是错的

1. **"干涉仪"类比**：干涉仪需要相位决定干涉符号。公平比较显示符号总是负的（环<树），这不是干涉仪的行为。
2. **"对易↔相消, 非对易↔相长"的二元分类**：被公平比较推翻。
3. **"CNOT无干涉因基对齐"**：弱CNOT结果与此矛盾。

### 建议的替代解释

**回路反馈抵消假说** (Loop Feedback Cancellation)：
- 环提供了从Q到E再回到Q的反馈路径
- 第一条路径（如Q_a→E1→Q_b）将R信息从Q泄漏到E
- 第二条路径（如Q_a→E2→Q_b）可能将部分已泄漏的信息"带回"Q
- 净效应：环的QCMI低于具有相同或更少Q-E边数的树
- 这解释了为什么bonus总是负的（反馈抵消是环的通用属性，不依赖门的对易性）
- 门的性质调制抵消程度（SWAP > XX > ZZ > Haar），但不翻转符号

### 实验设计修正

若要继续探索拓扑效应，需满足以下控制条件：
1. **固定n_E**：tree和cycle使用相同的E qubit数量
2. **固定Q-E gate数**或明确建模为独立变量
3. **控制饱和**：使用弱门扫描确保效应不因接近上限而被淹没
4. **更大的门类型扫描**：测试SWAP、CZ、iSWAP、partial-CNOT等边缘case
5. **b1>1的图**：测试双环图验证b1的加性假说

---

## 九、代码审计备注

### interference_test.py的代码质量

| 方面 | 评估 |
|------|------|
| setup验证 | ✓ 正确，S(R)=2, S(RQ)=0, QCMI(I)=0, 对易性测试均通过 |
| 状态构造 | ✓ Buscemi混合态实现正确 |
| QCMI计算 | ✓ 公式正确：SRQ+SQE-Sall-SQ |
| 酉演化 | ✓ 正确施加在QE上，保留R |
| **实验设计** | **✗ n_E不匹配是关键缺陷** |
| **拓扑实现** | ✓ 环和树的图结构正确（已验证顶点、边、b1） |

### 发现的次要问题

1. **固定seed问题**：`verify_setup()`中测试对易性时，Haar门使用`make_rand_Haar(s)`，但调用`test_commutativity(label, fn)`时seed被硬编码（99和199）。这不影响结果但应注明。
2. **N=40的统计力**：对于小效应（如Haar的+0.14），40个样本的标准误差约0.05-0.1，因此+0.14的显著性约1.4-2.8σ（边缘显著）。原始实验报告的sig值未提供，但估计在此范围。
3. **顺序依赖性**：U = U4@U3@U2@U1的顺序由因果偏序决定，但未验证改变顺序是否影响结论。

---

## 十、最终建议

1. **撤回"干涉仪"假说和所有四个声张**。它们基于一个有混淆变量的实验。
2. **重跑实验**，统一n_E=3，系统扫描门类型（至少20种）和门强度（至少5个theta值），每种条件N≥100。
3. **在修正实验中检验"回路反馈抵消"假说**：预测所有门的bonus ≤ 0（环永远不增加QCMI），幅度随门"交换强度"单调变化。
4. **如果修正实验确认环总是减少QCMI**：这是一个反直觉且有趣的结果——更多连接反而更少信息泄漏。这本身可能构成可发表的新发现。
5. **论文状态**：当前数据不足以支撑在论文中发表"干涉仪"假说。Theorem 1-3（恒等式、存在性、泛性）不受影响，可以继续推进。
