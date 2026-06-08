# Phase 执行清单

> 当前 active 北极星: LP29-C2T / provenance-complete external joined table construction。
> 旧 LP29-C2 清单已归档到 `project/Phase清单_LP29-C2_archived_20260604.md`。
> C2T 不是新材料机制命题，而是 C2 的经验验证前置产物。

## Phase 启动

```
[✅] 贡献者身份: anonymous；GATE 7 再确认
[✅] GATE -1: LP29-C2T 核心矛盾结构验证
[✅] 读 项目/北极星队列.md，确认 LP29-C2T 为下一优先执行对象
[✅] 写 当前状态.md
[✅] 写/更新 研究计划.md
[✅] AHA检查: N=0，无需触发
```

## C2T 数据前置

```
[✅] 读取 C2 knowledge_graph 的 required_join_fields
[✅] 建立 C2T joined-table schema 草案
[✅] 建立候选文献/数据源清单
[✅] 标记每个字段的 provenance 要求与 blocker
[✅] GATE: 无 provenance 的字段不得进入 material validation
```

## AB探索 Round 1

```
[✅] 启动A博士Agent Round 1
[✅] 启动B博士Agent Round 1
[✅] 确认A框架 != B框架
[✅] 确认B没读A的产出，A没读B的产出
[✅] 等两者都完成
[✅] INSPECTOR - A Round 1
[✅] INSPECTOR - B Round 1
[✅] 读INSPECTOR结果并登记警告
[✅] A博士Round 1: 文献库存在，先发/数据源检索完成
[✅] R1先发拦截
[✅] PI综合 Round 1
[✅] 突破方向检查
[✅] AHA检查
[✅] Q6.3/Q6.4 声张/替代解释检查
[✅] 重算矩阵
[✅] 检查矩阵切换
[✅] 检查队列饥荒
[✅] 更新知识库
[✅] REVIEWER检查: N=1，跳过
[✅] 更新 当前状态.md 到 N=1
[✅] 停止条件检查: N<3，继续 Round 2
```

## AB探索 Round 2

```
[✅] 启动A博士Agent Round 2
[✅] 启动B博士Agent Round 2
[✅] 确认A框架 != B框架，且互不读对方产出
[✅] 等两者都完成
[✅] INSPECTOR - A Round 2
[✅] INSPECTOR - B Round 2
[✅] PI综合 Round 2 + 更新状态
```

## AB探索 Round 3

```
[✅] 启动A博士Agent Round 3
[✅] 启动B博士Agent Round 3
[✅] 确认A框架 != B框架，且互不读对方产出
[✅] 等两者都完成
[✅] INSPECTOR - A Round 3
[✅] INSPECTOR - B Round 3
[✅] PI综合 Round 3 + 更新状态
[✅] REVIEWER - N=3 强制恶意审稿
```

## AB探索 Round 4

```
[✅] 启动A博士Agent Round 4
[✅] 启动B博士Agent Round 4
[✅] 确认A框架 != B框架，且互不读对方产出
[✅] 等两者都完成
[✅] INSPECTOR - A Round 4
[✅] INSPECTOR - B Round 4
[✅] PI综合 Round 4 + 更新状态
```

## Round 4 executor/witness 补强

```
[✅] 建立 `C2T_executor.py` command/script contract
[✅] 生成 `C2T_executor_actual_results.csv`
[✅] 负例 regression 对齐 expected
[✅] 增加 synthetic unit boundary examples
[✅] unit regression 对齐 expected
[✅] INSPECTOR rerun PASS
[✅] 保持真实候选 material_validation_allowed=false
```

## 北极星收尾

```
[✅] GATE 1.5: grep A/B 推导文件中 deepening_1 和 deepening_2 各 >=2 层
[✅] Re-escalation
[✅] GATE 降级前置
[✅] 矛盾深挖
[✅] 子命题提取
[✅] 更新 项目/北极星队列.md
[✅] 检查优先级队列
[✅] GATE 空转拦截
```

## 收官

```
[✅] PI最终综合推导
[✅] GATE 3: current/B 存在，B框架 != A框架
[✅] GATE 4: 无开放致命卡点
[✅] GATE 2: REVIEWER 终审
[✅] REVIEWER验证
[✅] GATE 6: shared/知识库汇总.md 追加K条目
[✅] 贡献者身份二次确认: anonymous
[✅] GATE 7: knowledge_graph JSON 存在
[✅] 更新 项目/北极星队列.md
[✅] 可选回写 shared/北极星候选池.md: 跳过，项目队列已注册
[✅] 读取优先级矩阵，进入下一个北极星
```
## C2T-S1 Jankousky single-row audit

```
[ ] 定义 Jankousky candidate row_id
[ ] 定位本地/公开 Jankousky source 与可审计字段
[ ] 构造 `C2T_jankousky_single_row_payload.jsonl`
[ ] 运行 `C2T_executor.py`
[ ] 对比 row decision 与 material_validation_allowed
[ ] INSPECTOR 审查 single-row audit
[ ] PI 综合并更新状态
```
