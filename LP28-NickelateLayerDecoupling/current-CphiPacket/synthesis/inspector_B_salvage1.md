PASS

审查对象：`current-CphiPacket/B/salvage1.json`

结论：B Salvage 1 可以把 REVIEWER REJECT 条件性挽回为 `bounded technical progress`，但只能在存在至少一行真实 audited pilot 的前提下成立。它没有把一行 pilot 夸大为 `R_oe` 判定、decision-grade 支持、全 campaign 可扩展性，或 nickelate 方向的 universal no-go。

## 审查要点

1. 一行 pilot 的最低真实性条件：PASS

B 明确要求 pilot row 必须是真实数据，来自同一样品或正式 sistered specimen lineage，不能是 literature montage 或 synthetic mock row。它还要求 reveal 前的 immutable raw archive、timestamped hashes 或等价 custody evidence、blind custodian、pre-registered firewall、冻结的 censoring/denominator floor/U_miss、以及 lineage/calibration/mismatch tolerances 预声明。

这满足“一行 pilot 的最低真实性条件”。尤其关键的是，B 没有把“填一行表”误认为 pilot，而是要求该行能通过真实数据、盲化、谱系和原始档案链条审计。

2. `instant_failure_conditions` 是否具体：PASS

失败条件具体且可执行，包括：

- 无 immutable raw archive 或 custody hash。
- `P_oe` 和 `B_min` 共享 fitted extraction state，特别是 qz/c-axis/orbital state。
- 看到 output 或 `B_min` alignment 后修改 labels、row selection、censoring、denominator floor 或 `U_miss`。
- output inspection 后 rescue/add/drop/sister row。
- 非 same-sample/formally sistered 且 lineage 不可审计。
- red rows 进入 primary residual test。
- blind custody absent/broken。

这些不是泛泛的“质量不足”措辞，而是能触发即时失败的具体审计条件。

3. 是否承认一行真实 audited pilot 可挽救为 bounded technical progress：PASS

B 明确写出 `must_concede_salvage_success_if`，并将 concession 类型限定为 `bounded_technical_progress_only`。核心判断是：若至少一行 audited real pilot 存在，并满足 minimum conditions、冻结 firewall reveal 前通过、且 `P_oe` 与 `B_min` 提取独立，则 B 必须承认 salvage success。

因此，B 没有维持不可挽回的 reject；它给出了清晰的 conditional salvage boundary。

4. 是否避免 universal no-go：PASS

B 在 `scope_guard` 中明确声明该边界只适用于 CphiPacket evidence class，不是关于所有未来 nickelate 工作或所有未来 packet designs 的 universal no-go。`cannot_prove` 和 claims 中也重复排除了 universal no-go。

5. 是否清楚说明一行能证明/不能证明什么：PASS

B 清楚区分：

一行能证明：
- 至少一行真实数据上的 blinded audited workflow 可执行。
- `P_oe` 与 `B_min` 在实践中可信息分离。
- firewall/censoring/custody rules 具体到可审计。
- 若真实且通过冻结审计，packet 不再只是 abstract protocol packaging。

一行不能证明：
- 不能证明 `R_oe`。
- 不能建立 statistical decision-grade support/refutation。
- 不能证明 campaign 可扩展至 N=48 或其他目标。
- 不能推出 nickelate measurements 的 universal no-go。
- 不能验证物理理论主张，只能证明 bounded feasibility。

## Salvage 判定

可以挽回 REVIEWER REJECT，但只挽回为 `bounded technical progress`。

最低可接受表述应是：`One real, blind, lineage-audited, extraction-separated pilot row can salvage the packet from pure protocol packaging into bounded technical progress; it cannot adjudicate R_oe or make the evidence decision-grade.`

无 blocker。保留边界条件：若实际不存在这样的 audited real pilot row，或 reveal/custody/extraction separation 任一关键条件失败，则 salvage 不成立，REJECT 仍不能被挽回。
