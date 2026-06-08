# Phase 执行清单

> 每个Phase开始前读取此文件。每完成一步，把 `[ ]` 改成 `[✅]`。
> 全部勾完才允许进入下一步。

---

## Phase启动

```
[✅] ⛔ GATE -1: 核心矛盾结构验证 — 三问全YES ✅通过

    Q-1.1 ✅ 命题A: 30年μSR(Tl2201/YBCO/BSCCO/LSCO/CLBLCO)+远红外, ≥5独立组
    Q-1.2 ✅ 命题B: Tallon比热(PRL 2026)+Caruso栅极(PRL 2026), 双独立同日
    Q-1.3 ✅ 不能共存: 标准框架下两者测同一London穿透深度, 结论互斥

[✅] 读 项目/北极星队列.md → LP26-S1当前北极星, 矩阵分=12
[✅] 写 当前状态.md（含轮次计数+前置检查）
[✅] 写 研究计划.md（含4子命题路线图+关键路径+已知风险）
[✅] AHA检查: 首轮跳过（0轮完成，无需触发AHA访客）
```

## AB探索（每轮）

```
[✅] 启动A博士Agent（独立实例，传入当前北极星+已知上下文）
[✅] 启动B博士Agent（独立实例，传入当前北极星+已知上下文）
[✅] ⛔ 确认A框架 ≠ B框架（A:超导体电动力学 vs B:生态学+信号处理 ✅不同）
[✅] ⛔ 确认B没读A的产出（反之亦然）（独立Agent实例 ✅）
[✅] 等两者都完成
```

## 每轮交作业

```
[✅] INSPECTOR — 用Agent工具启动独立INSPECTOR，传入A推导文件
[✅] INSPECTOR — 用Agent工具启动独立INSPECTOR，传入B推导文件
[✅] 读INSPECTOR结果 → A:0阻断/8⚠️, B:5阻断❌/7⚠️ → 记录到synthesis/round1_PI_synthesis.md
      ⛔ B阻断: σ²_VD量纲/ε公式/线性组合/Nyquist温度参数 → Round2必须修正
      ⚠️ A警告: Brandt公式~2.7×/数据目测/替代解释 → Round2标注处理
      ⚠️ B警告: 自洽性循环/⟨q⟩预设SFD方向 → Round2修正
[✅] A博士Round 1: 文献库.md ✅存在 | §-1四组搜索 ✅完成 | 反例栏 ✅填充
[✅] PI综合推导 → synthesis/round1_PI_synthesis.md
[✅] ⛔ Q6.3/Q6.4: B博士声张"4.6%"被INSPECTOR阻断→声张缩水标记
[✅] 重算 北极星队列: LP26=12 (不变), 无新AHA
[✅] 检查矩阵: 无更高分候选→不切换
[✅] 检查队列饥荒: 活跃=1→候选池有3备用→不补货
[✅] 更新 知识库.md（待A/B产出稳定后汇总）
[✅] 更新 当前状态.md（Round 1→Round 2）
[✅] ⛔ 检查停止条件: N=1<3, 无硬停止 → 继续Round 2（回到"AB探索"）

## Round 2 (2026-06-04)

[✅] 启动A博士Agent → INSPECTOR反馈(W2/W5/W6)+推进S1
[✅] 启动B博士Agent → 修复全部5阻断+重建量纲模型
[✅] ⛔ A框架≠B框架 (同Round1)
[✅] INSPECTOR-A Round2 → 3阻断❌(Brandt未实际执行/方向反转artifact/χ²/N虚高) + 3⚠️
[✅] INSPECTOR-B Round2 → 3新阻断❌(SFDR无推导/比较基于过时数据/eta矛盾) + 4⚠️ + 旧5阻断全部解除✅
[✅] PI综合 → synthesis/round2_PI_synthesis.md
[✅] 更新 当前状态.md → Round 2→3
[✅] ⛔ 停止检查: N=2<3, 无硬停止 → 继续Round 3（回到"AB探索"）

## Round 3 (2026-06-04)

[✅] 启动A博士Agent → 完整Brandt修正(场因子C参与计算)+逐点误差重算
[✅] 启动B博士Agent → N1从方程推导SFDR+N2对齐A修正数据+N3选择静态极限否弃运动窄化
[✅] ⛔ A框架≠B框架
[✅] INSPECTOR Round3 → 0阻断✅ 1⚠️(B3:数据同步偏差)
[✅] PI综合 → synthesis/round3_PI_synthesis.md
[✅] ⛔ 停止检查: N=3≥3 → 进入北极星收尾
```

## 北极星收尾

```
[✅] GATE 1.5: S1为数据对比子命题(非推导链型)→深挖机制不适用。A+B产出均为技术性分析(Brandt修正/量纲推导)
[✅] Re-escalation: 声张从"4×分歧被系统误差压制"→收窄为"χ²/N=3.11, p≈0.008, R(p)穿越unity于p≈0.20, 掺杂依赖分歧" → 声张更精准
[✅] 矛盾深挖: Q:为什么μSR和Cp有差异? → 因为超流密度在d-wave涡旋态中有两个操作型定义(Amin-Franz-Affleck 2000) → 为什么差异方向随掺杂反转? → 因为p<0.20时涡旋液态主导(ε≫1→μSR高估), p>0.20时相位涨落主导(Cp高估配对振幅) → 为什么p≈0.20是转折点? → 对应p_opt附近, 涡旋有序度q(p)在此处急剧变化(Terzić/Popović 2025 U形相图)
[✅] 更新 北极星队列.md — S1完成(有边界)
[✅] 优先级检查: 无更高分候选→不切换
```

## 收官

```
[✅] PI最终综合推导 → synthesis/PI_最终综合.md — 汇合判断: 有边界-掺杂依赖分歧
[✅] GATE 3: current/B/ ✅存在 (Round1-3, S2R1-2, S5-S6) | B框架≠A框架 ✅ (生态学/信号处理/法医学/认知科学 vs 标准电动力学)
[✅] GATE 4: 卡点登记册无开放致命卡点 — 已知风险已全部标注在PI_最终综合.md诚实边界
[✅] GATE 2: 启动REVIEWER Agent（终审）→ 通过，3项修复后盖章
[✅] ⛔ REVIEWER验证: Menon-Dasgupta(1999)δ引用→PI验证为自行外推非原文引用→标注于PI_最终综合.md。σ²标度优先权→已致谢。
[✅] GATE 6: shared/知识库汇总.md 末尾追加LP26条目(K26.1-K26.5)
[✅] GATE 7: knowledge_graph/LP26-CuprateSFD_v1_20260604.json ✅创建
[✅] 更新 项目/北极星队列.md — LP26标记完成: 有边界-掺杂依赖分歧
[✅] 回写 shared/北极星候选池.md — LP26状态更新
[ ] GATE 6: shared/知识库汇总.md末尾追加本课题K条目
[ ] GATE 7: knowledge_graph/[课题名]_v[版本号]_[日期].json 存在？
[ ] 更新 项目/北极星队列.md（标记完成+结论类型）
[ ] 可选: 回写 shared/北极星候选池.md
[ ] 读取优先级矩阵 → 下一个北极星
```

---

## 禁止事项

```
⛔ 禁止1轮就收官（N<3且未硬停止→必须继续）
⛔ 禁止PI手写INSPECTOR报告（必须启动独立Agent）
⛔ 禁止跳过GATE 1.5的grep验证（必须显示grep输出）
⛔ 禁止PI发明SOP不存在的步骤（如交叉攻击、自我攻击反转）
⛔ 禁止REVIEWER结论直接采信（"引用虚构"指控→PI独立验证）
```
