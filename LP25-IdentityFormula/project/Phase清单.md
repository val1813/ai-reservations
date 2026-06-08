# Phase 执行清单 | LP25-S3 欧拉动力学

> 每个Phase开始前读取此文件。每完成一步，把 `[ ]` 改成 `[✅]`。
> 全部勾完才允许进入下一步。

---

## Phase启动

```
[✅] 读 项目/北极星队列.md → 确认当前北极星+优先级分数
[✅] S1+S2战果汇总 → 明确S3的定位（非S1/S2的重复）
[✅] 写 当前状态.md（含轮次计数+前置检查）
[✅] 写 北极星（project/S3_北极星_欧拉动力学.md）→ 已完成
[✅] AHA检查: 首轮不适用（S3是新的探索方向）
```

## AB探索 Round1

```
[✅] 启动A博士Agent — aee6e023（框架：开放量子系统Redfield理论+Robertson不等式）
[✅] 启动B博士Agent — a780018b（框架：动力系统理论——吸引子/分岔/Lyapunov）
[✅] ⛔ 确认A框架 ≠ B框架（A:Redfield/Robertson, B:动力系统/分岔/Lyapunov）
[✅] ⛔ 确认B没读A的产出（独立Agent实例，无交叉读取）
[✅] 等两者都完成（A:924行14CHECK, B:725行9CHECK）
```

## 每轮交作业 Round1

```
[✅] INSPECTOR — Agent启动，传入A推导文件 → ❌阻断（3项错误）
[✅] INSPECTOR — Agent启动，传入B推导文件 → ⚠️警告（1个符号错误）
[✅] 读INSPECTOR结果 → A: 3阻断需修正（核心方程未受影响），B: 1符号可修正
[✅] PI综合推导（synthesis/PI综合_S3_R1.md）
[ ] 更新 知识库.md（新增K条目）
[ ] 更新 当前状态.md
[✅] ⛔ 停止条件：N=1<3，未硬停止 → 继续Round2（实用路线：修正+验证一步完成）
```

## AB探索 Round2

```
[ ] 修正北极星（基于Round1发现）
[ ] 启动A博士Agent Round2
[ ] 启动B博士Agent Round2
[ ] ⛔ 确认A框架 ≠ B框架
[ ] INSPECTOR ×2
[ ] PI综合
[ ] ⛔ 停止条件检查
```

## AB探索 Round3

```
[ ] 同上
```

## 北极星收尾

```
[ ] GATE 1.5: grep A推导文件中"深挖1"和"深挖2"各≥2层？B同？
[ ] Re-escalation: 声张是否比启动时更窄？
[ ] 矛盾深挖: 用"五个为什么"追溯驱动矛盾
[ ] 更新 项目/北极星队列.md
[ ] 检查优先级队列
```

## 收官

```
[ ] PI最终综合推导
[ ] GATE 3: current/B/存在？B的§0≠A的§0？
[ ] GATE 4: 卡点登记册无开放致命卡点
[ ] GATE 2: 启动REVIEWER Agent
[ ] ⛔ REVIEWER验证
[ ] GATE 6: 知识库汇总
[ ] GATE 7: knowledge_graph JSON
[ ] 更新 北极星队列（标记完成）
```

---

## 禁止事项

```
⛔ 禁止1轮就收官
⛔ 禁止PI手写INSPECTOR报告（必须启动独立Agent）
⛔ 禁止跳过INSPECTOR直接进入PI综合
⛔ 禁止PI发明SOP不存在的步骤
⛔ 禁止REVIEWER结论直接采信
```
