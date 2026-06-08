# REVIEWER N=3: LP29-C2T-S2-R1-I1

Date: 2026-06-05

Scope: independent reviewer of `PI_C2T_S2_R1_I1_round3.md` only. Core claim under review: I1 is an implementation-ready specification; `validation/validate.py` is not implemented or run.

## 第零步：AI 幻觉检查

- Q0.1 量纲：本轮输入没有新公式或量纲等式；不可判定为物理公式通过，只能判定“无可检公式”。
- Q0.2 方向：核心方向性声明是状态机声明：current Srivastava exact `O_s` remains `BLOCK`; context-only remains `CONDITIONAL_CONTEXT_PASS`; no silent upgrade。该方向与输入一致。
- Q0.3 循环论证：若把 regression contract 当作已通过验证，即构成循环论证；当前 PI 明确说 validator 尚未实现/运行，因此暂未犯此错。
- Q0.4 数量级：本轮输入没有数量级估算；无可检项。

结论：第零步条件通过，但只限于“specification status”层面；不得外推为 exact `O_s` reproduced、material validation、graph regression、graph beats overlap 或 impossible claim。

## 三轮 paper-search-mcp 检索

### 第一轮：方法层查重

- Tool: `paper-search-mcp.search_papers`
- Query: `amorphous flat bands superfluid weight quantum metric exact Os Srivastava validation`
- Sources: arXiv, Semantic Scholar, CrossRef
- Result: 未发现与“LP29 I1 validation contract / exact O_s reproduced”直接重合的已有工作。相邻结果包括 Brzezicki & Hyart, *Geometric and Conventional Contributions to Superfluid Weight in the Minimal Models for Superconducting Flat Bands Induced by Doping*, 2026, DOI `10.5506/aphyspolb.57.5-a13`; Jiang, Törmä & Barlas, *Superfluid weight cross-over and critical temperature enhancement in singular flat bands*, 2025, DOI `10.1073/pnas.2416726122`。

### 第二轮：框架盲区检索

- Tool: `paper-search-mcp.search_papers`
- Query: `disordered amorphous lattice flat band superconductivity geometric superfluid weight validation benchmark no go 2024 2025 2026`
- Sources: arXiv, Semantic Scholar, CrossRef
- Result: 未发现同一 implementation-ready validator closeout。相邻结果包括 Bouzerar & Thumin, *Robustness of flat band superconductivity against disorder in a two-dimensional Lieb lattice model*, 2025, DOI `10.1103/physrevb.111.l020506`; Thumin & Bouzerar, *Constraint relations for superfluid weight and pairings in a chiral flat band superconductor*, 2023, DOI `10.1209/0295-5075/ad0dc6`。

### 第三轮：否定性检索

- Tool: `paper-search-mcp.search_papers`
- Query: `amorphous disordered flat band superfluid weight exact overlap graph counterexample failure criticism disproof 2024 2025 2026`
- Sources: arXiv, Semantic Scholar, CrossRef
- Result: 未发现对本轮“只做 implementation-ready spec”的直接否定；也未发现可支持 exact `O_s` reproduced 或 graph beats overlap 的证据。检索返回若干不直接相关的 disproof/counterexample 条目，以及 flat-band superfluid-weight 相邻文献。

三轮查重通过（方法层、框架盲区、否定性），未发现直接竞争或直接反证；本结论只覆盖 implementation specification，不覆盖物理验证。

## 五条攻击

1. `validation/validate.py` 未实现/未运行，因此 regression command contract 只是承诺，不是证据；若 closeout 被理解为验证完成，结论立即失效。[严重]  
作者需证明：下一步提交可执行 validator、fixtures、expected outputs，并给出真实运行日志。

2. PI 摘要只列出 package 类目，没有暴露 fixture 内容、golden outputs、exit-code 语义和失败模式；reviewer 无法核验 minimal package 是否足够最小且完整。[严重]  
作者需证明：每个 expected status 都有独立 fixture，且失败消息能区分 `BLOCK` 与 conditional pass。

3. `PARTIAL_CONTEXT_ONLY -> BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY` 是本轮最脆弱状态转换；若测试未钉死，context-only 很容易被静默升级为 pass。[严重]  
作者需证明：legacy partial context fixture 必须失败，并同时输出 deprecation marker。

4. 相邻文献显示 flat-band superfluid weight 对模型条件、gap、disorder、pairing structure 高度敏感；因此禁止 material validation 和 exact `O_s` reproduced 是必要边界。[中等]  
作者需证明：validator 只检查命令契约，不把模型条件性解释为材料或物理验证。

5. “implementation-ready”不是科学新颖性结论；三轮检索未发现直接重复，但这不能替代实现后的 regression evidence。[轻微]  
作者需证明：closeout 名称明确为 spec closeout，而不是 I1 scientific validation closeout。

## 叙事退让检查

发现可接受的叙事收缩：早先若有任何 exact `O_s`、material validation、graph regression、graph beats overlap 或 impossible claim，本轮已退回到 implementation-ready spec。此退让不是科学证明，但它是合规的范围收缩；不得再反向扩张。

## 如果必须挑一个致命错误

如果必须挑一个致命错误：把“validator specification complete”写成或执行成“validator passed / exact `O_s` validated”。

这不是“可能有问题”——这是我作为审稿人，如果有编辑要求我必须找出拒稿理由，我会指出的最致命问题。即使我认为当前 spec closeout 可以成立，这个条目也必须填写。

作者的出路：下一步直接实现 `validation/validate.py`、fixtures、expected outputs、tests 和 README/CLI contract；运行 regression command contract，保留 current Srivastava exact `O_s = BLOCK`、context-only = `CONDITIONAL_CONTEXT_PASS`，并让 legacy partial context 明确输出 `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY`。

## 最终建议

接受 `implementation-ready closeout`，但只按字面接受：I1 可以关闭为“规格已准备好实现”，不能关闭为“验证已完成”。

要求下一步直接 implementation。不得再开 Round 4 文字论证来替代实现；下一轮交付物必须是可运行的 `validation/validate.py`、fixtures/tests 和 regression command 实际输出。
