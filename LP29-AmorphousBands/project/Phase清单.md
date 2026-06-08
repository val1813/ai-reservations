# Phase 执行清单

> 当前 active 北极星: LP29-C2T-S2-R1-I1-X1-P1 / proof-object authenticity validation before terminal-status admission.
> 旧 LP29-C2T-S2-R1-I1-X1 清单已归档到 `project/Phase清单_LP29-C2T-S2-R1-I1-X1_archived_20260605.md`.
> 每完成一步，把 `[ ]` 改成 `[✅]`。从第一个 `[ ]` 继续。

## Phase 启动

```
[✅] 贡献者身份: anonymous；GATE 7 再确认
[✅] GATE -1: LP29-C2T-S2-R1-I1-X1-P1 核心矛盾结构验证
[✅] 读 项目/北极星队列.md，确认 LP29-C2T-S2-R1-I1-X1-P1 为当前执行对象
[✅] 写 当前状态.md
[✅] 写/更新 研究计划.md
[✅] AHA检查: N=0，无需触发
```

## 证据真实性协议

```
[✅] 读取 X1 reviewer residual risk 与 S2-R1 F01-F22 schema
[✅] 定义 proof-object authenticity schema：source / structure / pairs / arithmetic / execution / comparison
[✅] 定义 authenticity validator 与 terminal-status validator 的接口边界
[✅] 建立 authenticity fixtures：valid proof-object、missing locator、bad digest、pair-count mismatch、formula-code mismatch、unbound trace、missing tolerance
```

## 实现与测试

```
[✅] 实现 validation/authenticity.py
[✅] 将 authenticity result 接入 validate.py 或定义明确前置调用契约
[✅] 写 tests/test_authenticity.py
[✅] 运行 authenticity pytest
[✅] 运行 combined smoke：authenticity PASS 才允许进入 terminal-status validation
```

## 收官

```
[✅] PI最终综合推导
[✅] GATE 3: current/B 存在，B框架 != A框架
[✅] GATE 4: 无开放致命卡点
[✅] GATE 2: REVIEWER 终审
[✅] REVIEWER验证
[✅] GATE 6: shared/知识库汇总.md 追加K条目
[✅] 贡献者身份二次确认
[✅] GATE 7: knowledge_graph JSON 存在
[✅] 更新 项目/北极星队列.md
[✅] 可选回写 shared/北极星候选池.md
[✅] 读取优先级矩阵，进入下一个北极星
```
