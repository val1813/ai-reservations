# Phase 执行清单

> 当前 active 北极星: LP29-C2T-S2-R1-I1-X1 / executed O_s baseline-admission regression firewall.
> 旧 LP29-C2T-S2-R1-I1 清单已归档到 `project/Phase清单_LP29-C2T-S2-R1-I1_archived_20260605.md`.
> 每完成一步，把 `[ ]` 改成 `[✅]`。从第一个 `[ ]` 继续。
> REVIEWER 明确要求：本 Phase 必须直接实现并运行 validator；不得用 Round4 prose/theory 替代。

## Phase 启动

```
[✅] 贡献者身份: anonymous；GATE 7 再确认
[✅] GATE -1: LP29-C2T-S2-R1-I1-X1 核心矛盾结构验证
[✅] 读 项目/北极星队列.md，确认 LP29-C2T-S2-R1-I1-X1 为当前执行对象
[✅] 写 当前状态.md
[✅] 写/更新 研究计划.md
[✅] AHA检查: N=0，无需触发
```

## 实现前置

```
[✅] 读取 I1 implementation package 与 B regression contract
[✅] 定义 validator 输入/输出 schema 与状态机边界
[✅] 建立 validation/ 与 tests/ 文件结构
```

## Validator 实现

```
[✅] 实现 validation/validate.py: validate_payload API + CLI
[✅] 实现 raw PARTIAL_CONTEXT_ONLY 严格 BLOCK 分支
[✅] 实现 reported_context / candidate_exact_replay / diagnosed_mismatch / admitted_exact gates
[✅] 实现 diagnostics / missing_fields / invalid_fields / first_failed_predicate / predicate_results / comparison 输出
```

## Fixtures 与测试

```
[✅] 写 validation/fixtures/a_expected_cases.jsonl
[✅] 写 validation/fixtures/legacy_partial_context.jsonl
[✅] 写 validation/fixtures/expected_results.csv
[✅] 写 tests/test_validate.py
[✅] 写 validation/README.md
```

## 执行回归

```
[✅] 运行 python -m pytest tests/test_validate.py
[✅] 运行 CLI smoke/regression command 并生成 actual results
[✅] 核验 17-case regression firewall：current Srivastava summary BLOCK、reported_context CONDITIONAL_CONTEXT_PASS、legacy PARTIAL_CONTEXT_ONLY BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY
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
