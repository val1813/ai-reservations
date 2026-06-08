# LP29-AmorphousBands 独立 REVIEWER N=3 报告

项目：LP29-C2T-S2-R1  
审稿人：独立 N=3 REVIEWER  
输入边界：只基于 PI 提供的核心结论审稿；未读取 A/B 详细推导文件。  
工具约束：三轮检索均优先使用 paper-search-mcp；未降级 WebSearch。  

## 第零步：幻觉检查

结论：未发现可由当前输入直接判定的量纲、方向、循环论证或数量级硬错误，但当前输入缺少可执行公式、变量单位、数值估计和真实数据来源，因此第零步只能给出“可审稿但不可实证通过”的判定。

- Q0.1 量纲检查：输入没有给出关键公式、变量定义或 SI 单位；不能声称量纲通过。未发现显式量纲错误。
- Q0.2 方向检查：输入没有给出方向性不等式或极限公式；不能做极限代入。未发现显式方向反转。
- Q0.3 循环论证检查：最大风险是 validator contract 只验证自身 payload/schema/oracle 一致性，而非验证物理命题。若后续把 protocol-ready validator 写成 material validation 或 exact `O_s` reproduction，即构成循环论证/过度声明。
- Q0.4 数量级鸿沟检查：输入没有数量级估计；不能判定。
- 第零步结论：`CONDITIONAL_CONTEXT_PASS` 可保留为 locator-gated context mode；不得升级为 unconditional PASS、exact upgrade 或 executed validator。

## 三轮检索表

| 轮次 | 目的 | paper-search-mcp 查询 | 结果摘要 | 判定 |
|---|---|---|---|---|
| 1 | 方法层查重 | arXiv: `amorphous flat bands singularity observable overlap matrix quantum geometry`; arXiv: `Srivastava exact O_s amorphous flat band superconductivity quantum geometry 2023 2024 2025 2026`; Semantic Scholar: `amorphous flat bands quantum geometry overlap matrix superfluid weight` | `Srivastava exact O_s` 直搜无结果。相邻结果包括 Julku/Bruun/Törmä 2021 `Quantum geometry and flat band Bose-Einstein condensation`、Peotta/Huhtinen/Törmä 2023 `Quantum geometry in superfluidity and superconductivity`、Kawakami/Igarashi/Koshino 2025 `Singular flat bands in three dimensions...`。 | 未发现同结论发表；发现强相邻文献，要求严守 bounded claim。 |
| 2 | 框架盲区搜索 | arXiv: `disordered flat band marker distinguish origin from exact observable superconducting weight no-go failure limit 2024 2025 2026`; Semantic Scholar: `disordered flat bands local observable identify geometric origin superconductivity baseline validation contract`; arXiv: `amorphous lattice flat band local marker quantum geometry superfluid weight validation protocol 2024 2025 2026` | 三个查询均无结果。 | 未发现直接竞争者；但术语可能过工程化，不能把无结果解释成强新颖性证明。 |
| 3 | 否定性搜索 | arXiv: `amorphous flat band observable failure problem criticism counterexample`; arXiv: `singular flat band quantum geometry local marker disproof counterexample 2024 2025 2026`; Semantic Scholar: `flat band superconductivity quantum geometry disorder counterexample criticism amorphous` | 三个查询均无结果。 | 未发现直接否定文献；仍不能解除 exact `O_s` BLOCK。 |

三轮查重结论：三轮查重通过（方法层✓ / 框架盲区✓ / 否定性✓），未发现“provenance-conditioned observable + proof-carrying baseline contract”这一 bounded closeout 的直接竞争论文。未使用 WebSearch。

## 叙事退让检查

发现叙事退让风险，但按当前核心结论版本尚可接受：

- 若最早目标是 exact Srivastava `O_s` reproduced，而当前版本变为 `reported_context` 的 locator-gated `CONDITIONAL_CONTEXT_PASS`，这不是 exact 结果，而是目标降级后的协议化收官。
- 该退让只有在正文显式写成“exact `O_s` remains BLOCK；context mode is conditional and locator-gated”时才是科学收缩；若淡化 BLOCK，则是规避攻击。

## 五条拒稿攻击或剩余风险

1. **核心 observable 未被复现，协议不能替代物理量。** 当前 Srivastava exact `O_s` remains BLOCK；payload/schema/oracle 只能证明报告上下文被定位和分类，不能证明 `O_s` 被计算、复现或可由该协议逼近。作者必须证明 exact `O_s` 的定义、输入、输出和失败条件，或明确移除 exact claim。[致命]

2. **validator contract 尚未执行，`protocol-ready` 可能被误读成 validator 已通过。** 项目尚无 `validation/validate.py`，因此 schema/oracle 只是规格书，不是可运行验证器。作者必须提交可执行 validator、fixture、expected cases、CI/命令输出，并把报告语言从 “validated” 改为 “specified but not executed”。[严重]

3. **`reported_context` 的通过语义有升级风险。** 当前允许的状态只能是 locator-gated context mode / `CONDITIONAL_CONTEXT_PASS`；任何 unconditional PASS 都会把“找到了上下文定位”伪装成“物理结论通过”。作者必须在 schema 中把 gate、locator、source span、failure mode 写成必填字段，并禁止 absent locator 的 PASS。[严重]

4. **A 侧 `PARTIAL_CONTEXT_ONLY` terminal status 未定义 target mode/case。** 这会让 transition oracle 出现不可判定终态：到底是预期失败、部分通过、还是 schema 错误？作者必须在实现前定义对应 target mode、expected case 和 oracle transition，或删除该 terminal status。[严重]

5. **相邻文献已经覆盖“平带量子几何/超流权重/奇异平带”的物理主线，新颖性只能落在审计协议，不在物理优越性。** Peotta/Huhtinen/Törmä 2023 综述、Julku/Bruun/Törmä 2021、Kawakami/Igarashi/Koshino 2025 等都使“量子几何与平带响应相关”不新。作者必须逐句限定贡献：不是 material validation，不是 graph beats overlap，不是 residual regression，而是 provenance-conditioned reporting contract。[中等]

## 禁止声明核对

以下声明在当前证据下必须禁止：

- exact Srivastava `O_s` reproduced。
- material validation。
- graph-vs-overlap residual regression。
- graph beats overlap。
- exact `O_s` impossible in principle。
- `reported_context` unconditional PASS。
- 从 `CONDITIONAL_CONTEXT_PASS` 升级到 exact `O_s`。

## 如果必须挑一个致命错误

如果必须挑一个致命错误：把“protocol-ready validator contract”写成“已经验证/复现 Srivastava exact `O_s`”。

这不是“可能有问题”——这是我作为审稿人，如果有编辑要求我必须找出拒稿理由，我会指出的最致命问题。即使我认为这篇工作总体方向可以 bounded closeout，这个条目也必须填写。

作者的出路：提交 `validation/validate.py`、最小 fixtures、expected cases、transition oracle 的可执行测试记录；同时在正文中把 exact `O_s` 保持为 BLOCK，把 `reported_context` 限定为 locator-gated `CONDITIONAL_CONTEXT_PASS`，不得写成 unconditional PASS 或 exact upgrade。

## 最终建议

建议：接受为 **bounded / protocol-ready closeout**，前提是报告标题、摘要、结论和 schema 文档全部显式承认：

- exact Srivastava `O_s` remains BLOCK。
- 当前成果是 protocol-ready validator contract，不是 executed validator。
- `reported_context` 只能是 locator-gated `CONDITIONAL_CONTEXT_PASS`。
- `PARTIAL_CONTEXT_ONLY` 必须在实现前定义或移除。

是否要求 Round 4：不要求为了“更多推导”启动 Round 4；要求下一步优先做 validator implementation。若 PI 想把结论从 bounded closeout 升级为 executed validation，则必须开实现轮而不是继续理论轮。

## 搜索工具使用清单

- Round 1：paper-search-mcp `search_arxiv` x2，`search_semantic` x1；无降级。
- Round 2：paper-search-mcp `search_arxiv` x2，`search_semantic` x1；无降级。
- Round 3：paper-search-mcp `search_arxiv` x2，`search_semantic` x1；无降级。
- WebSearch：未使用；原因是 paper-search-mcp 已明确返回结果或空结果，不需要降级。
