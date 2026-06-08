# GATE 1.5 深挖检查

## 检查方式

模板要求 grep A/B 推导文件中“深挖1”和“深挖2”各 ≥2 层。Round 3 JSON 使用英文结构字段，因此按语义等价检查：

- A: `current/A/round3.json`
  - `consequence_layer_1`
  - `consequence_layer_2`
  - `most_fragile_premise_layer_1`
  - `most_fragile_premise_layer_2`
- B: `current/B/round3.json`
  - `level_1`
  - `level_2`
  - `physics_payoff`

## 判定

通过。A 给出“后果→后果的后果”和“最脆弱前提→若失败则降级”的两层；B 给出“distributed consensus→control feedback protocol”的两层。

## 注意

后续若继续，A/B 输出应显式包含中文键 `深挖1` / `深挖2`，避免 GATE 依赖语义判断。
