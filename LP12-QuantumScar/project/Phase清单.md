# Phase 执行清单 — LP12-S3 v2

> 每个Phase开始前读取此文件。每完成一步，把 `[ ]` 改成 `[✅]`。

---

## Phase启动

```
[✅] 读 项目/北极星队列.md → 确认当前北极星+优先级分数
[✅] GATE 0: 文献库.md存在？先发检索栏有判定结论？(⚠️部分先发Chioquetta 2407.14691)
[✅] GATE 1: 文献库.md反例栏非空？(A1-A3, B1-B3)
[✅] 写 当前状态.md（含轮次计数+前置检查）
[✅] 写 研究计划.md
[✅] AHA检查: 本次为首轮，无历史AHA记录，不触发
```

## AB探索（第1轮）

```
[✅] 启动A博士Agent（独立实例，交换子代数框架）
[✅] 启动B博士Agent（独立实例，半经典混沌+metastability框架）
[✅] ⛔ 确认A框架 ≠ B框架（A=交换子代数, B=半经典动力学 → 不同✅）
[✅] ⛔ 确认B没读A的产出（独立Agent实例，不共享上下文）
[✅] 等两者都完成
```

## 第1轮交作业

```
[✅] INSPECTOR — 启动独立INSPECTOR Agent检查A推导
[✅] INSPECTOR — 同一INSPECTOR检查B推导（合并检查）
[✅] 读INSPECTOR结果：🟡需修正，A:0🔴/B:2🔴，已记录
[✅] PI综合推导（pi_convergence.md）
[⏳] 更新 知识库.md（新增K条目）← 当前步骤
[ ] 更新 当前状态.md（轮次+1，更新前置检查框）
[ ] ⛔ 检查停止条件：N=1轮 → N<3且未硬停止 → 必须继续下一轮
```

## 第1轮REVIEWER（提前触发用于查重）

```
[✅] GATE 2: 启动REVIEWER Agent（终审查重）
[✅] ⛔ REVIEWER验证: Pizzi et al. (Nat Comms 2025) → PI用WebSearch独立验证 ✅确认
[✅] ⛔ REVIEWER验证: Mohapatra et al. (PRB 2026) → PI用WebSearch独立验证 ✅确认
[⏳] REVIEWER发现GATE 0遗漏5篇关键论文 → GATE 0需重做 ← 当前步骤
```

## GATE 0重做（REVIEWER后发现遗漏）

```
[ ] paper-search-mcp/WebSearch: 补充搜索 Pizzi et al., Mohapatra et al., Ivanov-Motrunich, Banerjee et al., Matsui et al.
[ ] 更新 文献库.md → 重新判定（将遗漏论文纳入）
[ ] 重新评估差异化声张 → 降级或维持
```

## 第1轮补充（SOP违规修正）

```
[✅] Phase清单.md创建（冷启动第0步）
[✅] 北极星队列.md创建（含优先级矩阵）
[✅] 当前状态.md格式修正（v3.7规范：前置检查+轮次+优先级分数）
[✅] GATE 1.5: grep验证 — A:§5(3层)+§6(4层)✅; B:§6(3层)+§7(5层)✅
[✅] GATE 0重做: 补充搜索5篇遗漏论文，修订判定
[✅] REVIEWER验证协议: PI用WebSearch独立验证Pizzi et al.+Mohapatra et al.
```

## 优先级矩阵切换

```
[✅] 重算优先级：LP12-S3=1.5, LP12-S2=4.16
[✅] 切换条件满足：4.16 > 1.5×1.3=1.95
[✅] S3完成度30%<70%，不触发保护
[✅] ⛔ 矩阵裁决：切换至LP12-S2 τ标度分歧
[ ] 保存S3当前状态 → 暂停-优先级低于LP12-S2
[ ] 初始化S2 → 补做GATE 2(REVIEWER)
```
