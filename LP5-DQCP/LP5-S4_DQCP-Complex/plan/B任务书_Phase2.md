# B博士任务书 — Phase 2

**课题：** DQCP-Complex v1
**Phase：** Phase 2（P2: 跨域攻击）

---

## 当前命题

**P2：非厄米J-Q模型连续相变的机制鉴别**

P2-A：连续化来自非厄米特有机制（例外点凝聚或NHSE），属于Bernard-LeClair分类中的独立普适类
P2-B：γ驱动的"连续化"是伪连续赝象——I_γ(m)对所有有限γ保持非凸，Δ(γ)指数衰减但永不真正为零

---

## 本Phase突击任务

### 主攻方向：独立验证Bernard-LeClair分类归属 + 排除P2-B

**任务1（优先）：搜索非厄米量子多体系统临界现象的最新实验/数值证据**

- 搜索："exceptional point quantum phase transition numerical evidence 2025"
- 搜索："non-Hermitian skin effect critical exponents measurement"
- 关键问题：在已知的非厄米临界现象中，标度指数是否与任何厄米CFT匹配？还是总是独立的新普适类？
- 特别关注：Hanai-Littlewood d_c=8普适类是否有任何格点模型的数值验证？

**任务2：攻击P2-B（伪连续赝象假说）**

若P2-B成立（Δ(γ)指数衰减但永不真正为零）：
- 非厄米Potts模型（Tang 2024）在γ_c处是否真的连续？还是指数衰减的一阶特征？
- 搜索："pseudo-critical weakly first-order exponential suppression"
- 从大偏差理论角度：什么样的率函数结构使Δ(γ)~exp(-c/γ)？这是BKT-like（本质奇异）还是不同机制？
- 若Δ(γ)~exp(-c/γ)，则dΔ/dγ在γ→0⁺时为零到所有阶→Δ(γ)是"无限阶平坦"的→在操作上等价于真正的零但在数学上非零。这与A博士Phase 1发现的"δ是边缘相关微扰(Re(Δ_δ)=0)"如何对话？

**任务3：搜索非厄米J-Q模型或类似模型的独立复现/挑战**

- 搜索Zou et al. (arXiv:2511.03456)之后的引用或独立复现
- 是否有其他课题组在非厄米DQCP方向上的工作？
- 特别关注：arXiv上最近180天内"non-Hermitian J-Q"或"non-Hermitian deconfined"的论文

---

## 禁止使用的学科

- 谱理论/泛函分析（A博士Phase 1已用）
- 范畴论（第二轮苏格拉底已用）

## 优先探索的学科

- 非厄米量子光学/激子极化激元（非厄米临界现象的实验实现）
- 冷原子物理（Floquet非厄米系统的量子模拟）
- 张量网络/数值方法（非厄米临界指数的独立计算）
- 随机矩阵理论（Bernard-LeClair分类的谱统计）

---

## 输出格式

⚡ 本Phase推进了什么 / 最关键的跨域连接 / 预测 vs 实际 / 卡在哪里
§1 结论预测
§N 推导正文（每步：学科工具 + 依据 + 反驳检验）
§末 结论对比
