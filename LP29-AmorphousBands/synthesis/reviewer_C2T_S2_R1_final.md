# LP29-AmorphousBands 独立 final REVIEWER 终审

项目：`LP29-C2T-S2-R1 / O_s as provenance-conditioned observable / proof-carrying baseline contract`

输入：
- `synthesis/PI_C2T_S2_R1_final.md`
- `synthesis/reviewer_C2T_S2_R1_N3.md`

工具约束：已按 REVIEWER 协议先用 paper-search-mcp；未降级 WebSearch。

## 终审结论

接受为 **bounded / protocol-ready validator contract closeout**。

不接受为：
- executed validator
- exact Srivastava `O_s` reproduced
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact `O_s` impossible-in-principle theorem

PI final 的当前文字边界基本合格：它明确写出 `not executed validator`、`Current Srivastava exact O_s remains BLOCK`，并把上述危险表述放入 Forbidden Claims，而不是作为成果声称。因此 N=3 reviewer 的 bounded 接受可维持。

## 第零步：幻觉/边界检查

Q0.1 量纲：当前 final synthesis 没有新增公式、单位或量纲推导，不能声称量纲实证通过；但也未发现显式量纲错误。

Q0.2 方向：当前 final synthesis 没有新增方向性不等式或极限论证，未发现方向反转。

Q0.3 循环论证：最大风险仍是把 payload/schema/oracle 一致性误写为物理验证。PI final 已明确 `not executed validator` 和 exact `O_s` BLOCK，因此当前版本没有循环论证性升级；后续实现前仍需防止把 contract 当作 validation result。

Q0.4 数量级：当前 final synthesis 没有数量级估算，无法判定；未发现数量级硬错误。

结论：幻觉检查条件通过。通过范围仅限“协议边界和声明边界可审查”，不等于物理量复现或 validator 执行。

## 三轮 paper-search-mcp 查重

### Round 1：方法层查重

查询：
- `search_arxiv`: `amorphous flat bands singularity observable overlap matrix quantum geometry`
- `search_semantic`: `Srivastava exact O_s amorphous flat band superconductivity quantum geometry`, year `2023-2026`
- `search_semantic`: `amorphous flat bands quantum geometry overlap matrix superfluid weight`, year `2021-2026`

结果：未发现 `Srivastava exact O_s` 或 “provenance-conditioned observable / proof-carrying baseline contract” 的直接同结论先发。相邻命中包括 Julku/Bruun/Törmä 2021 `Quantum geometry and flat band Bose-Einstein condensation`，说明平带量子几何物理主线不是本项目新颖性来源。

判定：方法层未发现直接重复造轮子；必须维持 bounded contract claim。

### Round 2：框架盲区搜索

查询：
- `search_arxiv`: `disordered flat band marker distinguish origin exact observable superconducting weight no-go failure limit`
- `search_semantic`: `disordered flat bands local observable identify geometric origin superconductivity baseline validation contract`, year `2024-2026`
- `search_arxiv`: `amorphous lattice flat band local marker quantum geometry superfluid weight validation protocol`

结果：均无直接结果。

判定：未发现普通语言表述下的直接竞争者；但无结果不构成强新颖性证明，因为本轮术语偏工程化。

### Round 3：否定性/反例搜索

查询：
- `search_arxiv`: `amorphous flat band observable failure problem criticism counterexample`
- `search_arxiv`: `singular flat band quantum geometry local marker disproof counterexample 2024 2025 2026`
- `search_semantic`: `flat band superconductivity quantum geometry disorder counterexample criticism amorphous`, year `2021-2026`
- `search_arxiv`: `Peotta Huhtinen Torma quantum geometry superfluidity superconductivity flat bands 2023`

结果：前三项未发现直接否定本 bounded contract 的文献。第四项命中 Peotta/Huhtinen/Törmä 2023 `Quantum geometry in superfluidity and superconductivity` 及相关平带超导文献，覆盖相邻物理主线，但不覆盖本项目的 proof-carrying reporting contract。

判定：未发现直接否定文献；相邻文献要求本项目不得声称物理优越性、材料验证或 graph-overlap 回归胜出。

三轮结论：查重通过（方法层通过 / 框架盲区通过 / 否定性通过），未发现 direct competitor。未使用 WebSearch。

## 本地文件核对

存在：
- `current/A/artifacts/S2_R1_validator_payload_schema_round3.json`
- `current/A/artifacts/S2_R1_A_expected_cases_round3.csv`
- `current/B/artifacts/S2_R1_transition_oracle_round3.csv`

不存在：
- `validation/validate.py`

因此当前成果是 validator contract specification，不是 executed validator。

## Forbidden Claim 审查

PI final 中以下危险表述只作为 Forbidden Claims 或 Remaining Warnings 出现，未被写成成果：
- exact Srivastava `O_s` has been reproduced
- validator has been executed
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact `O_s` impossible in principle

接受条件：这些 forbidden claims 必须继续保留为显式禁止项。任何摘要、标题、后续 queue 条目或实现说明都不得把它们改写成正面成果。

## 剩余攻击点

1. **contract 仍不能替代 observable。** 当前 exact Srivastava `O_s` remains BLOCK；schema/oracle 只规定 baseline admission，不计算或复现 exact `O_s`。[致命]

2. **validator 未执行。** `validation/validate.py` 不存在，因而当前没有 fixtures run、CLI output、CI evidence 或 executable verdict。[严重]

3. **`PARTIAL_CONTEXT_ONLY` 仍是实现前缺口。** 若它保留为 terminal status，必须映射 target mode/case；否则应删除，避免 transition oracle 出现不可判定终态。[严重]

4. **`CONDITIONAL_CONTEXT_PASS` 不得升格。** 它只能表示 locator-gated context mode；absent locator 不能 PASS，也不能升级 exact certification。[严重]

5. **新颖性只能落在协议合同。** Peotta/Huhtinen/Törmä 2023、Julku/Bruun/Törmä 2021 等相邻文献已覆盖平带量子几何/超流权重主线；本项目不能声称 material discovery、graph beats overlap 或 residual regression superiority。[中等]

## 如果必须挑一个致命错误

如果必须挑一个致命错误：把 “protocol-ready validator contract” 写成 “已经执行 validator 并复现 exact Srivastava `O_s`”。

这不是“可能有问题”——这是我作为审稿人若必须给拒稿理由，会指出的最致命问题。当前 PI final 没有犯这个错误，但下一步实现前后最容易在摘要和结论中越界。

作者的出路：进入实现轮，提交 `validation/validate.py`、最小 fixtures、expected cases、transition oracle 的可执行测试记录和命令输出；同时继续保持 exact `O_s` BLOCK，除非另有独立 exact reproduction evidence。

## 最终建议

最终建议：**接受为 bounded / protocol-ready validator contract closeout**。

是否要求 Round 4 理论轮：**不要求**。继续理论轮不会把 protocol-ready 升级为 executed validation。

是否要求实现轮：**要求下一步进入实现轮**，尤其是若项目要从 closeout 升级为 validator evidence。建议下一候选保持为 `LP29-C2T-S2-R1-I1 / executable O_s baseline-admission validator`。

## 搜索工具使用清单

- Round 1：paper-search-mcp `search_arxiv` x1，`search_semantic` x2；未降级。
- Round 2：paper-search-mcp `search_arxiv` x2，`search_semantic` x1；未降级。
- Round 3：paper-search-mcp `search_arxiv` x3，`search_semantic` x1；未降级。
- WebSearch：未使用；原因是 paper-search-mcp 可用并返回结果或明确空结果。
