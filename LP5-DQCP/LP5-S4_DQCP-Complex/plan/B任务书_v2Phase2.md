# B博士任务书 — v2 Phase 2

**课题：** DQCP-Complex v2
**Phase：** v2 Phase 2（跨域攻击：非幺正CFT签名的可检测性与信号处理视角）
**对应A博士命题：** P4 — 幽灵不动点的非幺正签名在L~64-1024下可检测

---

## 当前命题 P4

**AHA #1驱动矛盾:**
- **命题A:** 非幺正CFT算符的虚部Δ_I在L~64-1024产生可检测的关联函数振荡G(r)~cos[Im(Δ)log r]
- **命题B:** 非幺正签名被Miransky标度+有限尺寸效应压制，在现有系统尺寸下不可区分于统计噪声

---

## 本Phase突击任务

### 任务1（优先）：搜索已知的非幺正/复CFT有限尺寸签名的文献

搜索是否有其他系统已经探测到复CFT的有限尺寸效应：
- 搜索："complex CFT finite size scaling oscillatory"
- 搜索："non-unitary conformal field theory lattice simulation logarithmic oscillation"
- 搜索："walking technicolor lattice gauge theory correlation function oscillation"
- 搜索："Lee-Yang edge singularity finite size oscillatory correlator"
- 搜索："complex scaling dimension Monte Carlo detection"

特别关注：
- Lee-Yang边缘奇点（最简单的非幺正CFT, c=-22/5）——有格点实现吗？关联函数振荡被探测到了吗？
- 5-state Potts模型（Tang et al. 2024）——复平面上c=1.14-0.02i，在实轴附近是否有振荡残留？
- Walking technicolor的格点规范理论研究——是否讨论过"walking"的有限尺寸签名？

### 任务2：攻击命题A的可检测性 — 信号处理视角

将问题重新表述为信号检测问题：
- "信号" = G(r)中的对数周期振荡 ~ cos(η_I log r + φ₀)
- "噪声" = 量子蒙特卡洛统计误差 + 有限尺寸效应 + 激发态污染
- 信号频率 = η_I（对数空间中的角频率）
- 信号窗口 = log(L_min) 到 log(L_max)（对数空间中的有限带宽）

关键攻击点：
1. **频率分辨率限制:** 在L∈[L_min, L_max]的窗口内，对数空间的有效带宽是Δlog L = log(L_max/L_min)。可分辨的最小η_I ≈ 2π/Δlog L。对于L_max/L_min=1024/8=128, Δlog L≈4.85 → η_I_min≈1.3。如果η_I远小于此值（如η_I~0.01-0.1），则在现有窗口内连一个完整周期都看不完。
2. **振幅衰减:** 对数振荡被r^{-2Δ_R}的幂律衰减包络调制——在大的r处信号振幅被严重压制
3. **信噪比:** QMC统计误差通常~1-5%。η_I~0.01-0.1的对数周期振荡振幅能超过这个阈值吗？

### 任务3：攻击命题B — 寻找替代解释

如果确实在数值数据中看到了"振荡"，它们可能来自：
1. **壳层效应(shell effect):** 有限格点的离散壳层结构在关联函数中产生伪振荡
2. **次领头标度修正:** 标准（幺正）CFT的次领头 irrelevant 算符贡献 ~ r^{-(Δ+ω)} 可能与对数周期振荡混淆
3. **边界条件效应:** 周期边界 vs 开放边界在关联函数中产生不同的有限尺寸伪影
4. **DMRG截断误差:** 柱面几何中的有限键维数产生的人工周期性
5. **多分量序参量干涉:** 若DQCP的VBS和AF序参量在有限系统中混合，干涉可产生拍频效应

搜索："spurious oscillation correlation function DMRG finite size"
搜索："subleading correction mimic logarithmic oscillation CFT"

### 任务4（如时间允许）：提出判决性检验

设计一个数值实验可以干净区分命题A（真非幺正CFT签名）和命题B（噪声/伪影）：
- 如果振荡频率η_I独立于系统尺寸 → 支持命题A（CFT预测）
- 如果振荡频率随L变化 → 支持命题B（有限尺寸伪影）
- 如果振荡幅度随L增大而减小（~1/log L）→ 支持命题A（速率函数Γ⁽⁴⁾预测）
- 如果改变边界条件后振荡消失 → 支持命题B（边界伪影）

---

## 禁止使用的学科
- 共形场论/重整化群（A博士已用 — 推导复标度维数）
- 群论/对称性分析（v2 Phase 1 A博士已用）

## 优先探索的学科
- 信号处理/时间序列分析（对数周期振荡的检测统计）
- 格点规范理论（walking technicolor的数值经验）
- 量子蒙特卡洛（统计误差分析和有限尺寸效应）
- 冷原子实验（Floquet工程中的非幺正动力学签名）

---

## 输出格式

⚡ 本Phase推进了什么 / 最关键的跨域连接 / 预测 vs 实际 / 卡在哪里
§1 结论预测
§N 推导正文（每步：学科工具 + 依据 + 反驳检验）
  - Task 1: 已知非幺正CFT有限尺寸签名的文献
  - Task 2: 信号处理视角的可检测性分析
  - Task 3: 替代解释搜索
  - Task 4: 判决性检验设计
§末 结论对比（命题A vs 命题B vs 改进命题）
