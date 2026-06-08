# INSPECTOR_A_R4_round2

输入文件：`current/A/R4_round2.md`  
输出角色：LP23-R4 Round2 A 路 INSPECTOR 重跑  
范围限制：只做量纲、符号方向、循环论证、量级鸿沟、代数验算和综合判定；不评价发表价值或先发覆盖；未读取 B 路输出。

## Q1. 量纲校对

### 公式 1

`Accept(c)=1 iff Verify_P(c,W_c)=1 and NonOracle_P(c,W_c,r)=1`

- 左边 SI 单位：无量纲布尔值。
- 右边 SI 单位：`Verify_P` 与 `NonOracle_P` 均为无量纲布尔值，逻辑 `and` 后仍为无量纲布尔值。
- `c` 与 `r`：输入声明二者同属观测输出空间 `Y`，其 SI 单位由测量通道给定。
- 匹配：✅

### 公式 2

`W_c=(W_pre,W_origin,W_locality,W_symmetry,W_redundancy,W_causality,W_passivity,W_measurement,W_identifiability,W_cutoff,W_nonoracle)`

- 左边 SI 单位：witness tuple，不是物理标量等式；无统一 SI 单位要求。
- 右边 SI 单位：元组分量包含证据、规则、约束、测量映射和非 oracle 证明；不是可相加物理量。
- 匹配：✅，作为结构定义成立。

### 公式 3

`Verify_P(c,W_c) = Pre(...) and Origin(...) and ... and NonOracle(W_nonoracle,r)`

- 左边 SI 单位：无量纲布尔值。
- 右边 SI 单位：各子谓词均为无量纲布尔值，逻辑合取后仍为无量纲布尔值。
- 注意：`NonOracle(W_nonoracle,r)` 依赖 `r` 只适合作为拒绝/审计条件；若用于生成 `G_W`，会进入 Q3 的 oracle 风险。输入文件随后改写为 `Verify_P^pre` 与 `G_W(P)`。
- 匹配：✅

### 公式 4

`G_W(P,r) = { c | exists W_c : Verify_P(c,W_c)=1 }`  
`S_W(P,r) = span { c in G_W(P,r) }`  
`Obs^W_P(r) = [r] in Y / S_W(P,r)`

- `G_W` 元素单位：`c` 的单位为 `Y`。
- `S_W` 单位：由 `Y` 中同单位列张成的子空间，单位仍为 `Y`。
- `Obs^W_P(r)` 单位：`Y/S_W` 中的等价类；要求 `r` 与 `S_W` 元素同单位。输入已声明 `c` 必须与 `r` 同单位。
- 匹配：✅
- 标记：⚠️ 该式若被当作强判据使用，会让候选列集合依赖 residual。输入文件已给出修正式 `G_W(P)`，后续必须采用修正式。

### 公式 5

`G_W(P) = { c | exists W_c : Verify_P^pre(c,W_c)=1 }`  
`S_W(P) = span G_W(P)`  
`Obs^W_P(r) = [r] in Y / S_W(P)`

- `G_W(P)` 元素单位：`Y`。
- `S_W(P)` 单位：`Y` 的子空间。
- `Obs^W_P(r)` 单位：`Y/S_W(P)` 中的等价类。
- 匹配：✅

### 公式 6

`Reject(c,W_c,r)=1 if Dep(c; r | P_pre, D_independent) > 0 and no independent source channel proves c before r`

- 左边 SI 单位：无量纲布尔值。
- `Dep(...)`：依赖度/信息依赖判据，按文本用途为无量纲判别量。
- `0`：无量纲阈值。
- 时间顺序子条件要求 `timestamp(W_pre)` 与 `timestamp(r_unblinded)` 同为时间单位，可比较。
- 匹配：✅

### 公式 7

`I(c ; r | P_pre, D_c) = 0`

- 左边 SI 单位：信息依赖量；按信息论 convention 为无量纲或以固定信息单位计量。
- 右边 SI 单位：同一信息依赖量的零值。
- 匹配：✅

### 公式 8

若 `G_W(P)` 在有限 `Y_K` 中生成满秩，则 `S_W(P)=Y_K`，故任意 `r in Y_K` 有 `Obs^W_P(r)=0`。若 `G_W` 依赖 `r`，则存在 `c=r` 使 `Obs^W_P(r)=0`。

- `S_W(P)=Y_K`：同一有限观测空间内的子空间等式，单位匹配。
- `r in Y_K`：成员关系，单位由 `Y_K` 给定。
- `Obs^W_P(r)=0`：quotient 中零等价类；单位与 quotient 空间一致。
- 匹配：✅

### 超越函数自变量

未发现 `exp()`、`sin()`、`log()`、`sinh()` 等超越函数。✅

## Q2. 符号/方向校对

### 方向结论 1

结论：PCC/type/capability 已覆盖“携证书可机检”的抽象结构；R4a 的新增只能是物理 witness 的来源独立性。

- 极限/退化 1：若 witness 只是形式 `proof : Legal(c)`，则 checker 退化为 PCC 类结构，新增为零。方向一致。✅
- 极限/退化 2：若 witness 包含独立物理来源、测量映射、非 oracle 证据，则相对 PCC 增加的是来源独立性约束。方向一致。✅

### 方向结论 2

结论：witness checker 的最小对象不是 proof term，而是预注册来源、物理约束、冗余商、观测映射和非 oracle 证明的组合。

- 极限/退化 1：移除 `W_origin`、`W_measurement`、`W_nonoracle` 后，仅剩 proof/checker，不能阻止 residual-shaped column。方向一致。✅
- 极限/退化 2：加入全部 witness tuple 后，checker 可在 residual 投影前约束候选列来源。方向一致。✅

### 方向结论 3

结论：若 `G_W(P)` 满秩覆盖有限 `Y_K`，则任意 `r` 的 obstruction 为零。

- 极限/退化 1：`rank S_W(P)=0` 时，非零 `r` 通常保留非零 quotient 类；不会被吸收。方向一致。✅
- 极限/退化 2：`rank S_W(P)=dim Y_K` 时，`S_W(P)=Y_K`，任意 `r in Y_K` 都在子空间内，quotient 类为零。方向一致。✅

### 方向结论 4

结论：若 `G_W` 依赖 `r`，则存在 `c=r` 使 `Obs^W_P(r)=0`。

- 极限/退化 1：若禁止 `G_W` 查询 `r`，不能由该机制保证 `c=r` 出现。方向一致。✅
- 极限/退化 2：若允许 `G_W` 查询 `r` 且模板族可包含 residual-shaped column，则取 `c=r`，`r in span{c}`，quotient 为零。方向一致。✅

未发现分子分母放反或负号吞掉问题。✅

## Q3. 循环论证校对

### 验证/检验操作 1：文献元数据与 DOI 检索

- 检验数据如何生成：来自文献元数据与 DOI 检索。
- 输入假设：A 路报告用成熟框架作参照。
- 检验数据是否由输入假设生成：否；但本 INSPECTOR 不评价先发覆盖，只确认其未作为实验数值或代数验证输入。
- 循环论证：未发现。✅

### 验证/检验操作 2：`W_pre` / `W_nonoracle` 独立性检查

- 检验数据如何生成：预注册、时间戳、独立校准数据、blind split、holdout 等。
- 输入假设：候选列 `c` 的来源必须先于或独立于 residual `r`。
- 检验数据是否由输入假设生成：若真实使用独立通道，则否；若事后构造 witness，则会循环。
- 判定：文本已显式要求独立预注册或独立测量通道；未发现当前推导把事后 witness 当作独立检验。✅
- 标记：⚠️ 后续实现若使用 `G_W(P,r)` 生成候选列，再用同一 residual 验证 `W_nonoracle`，将构成循环论证。当前文本已用 `G_W(P)` 修正。

### 验证/检验操作 3：holdout 检查

- 检验数据如何生成：未参与 residual 发现的通道、频段、边界条件或 intervention。
- 输入假设：合法补列必须不只是吸收训练 residual。
- 检验数据是否由输入假设生成：若 holdout 真正隔离，则否。
- 循环论证：未发现。✅

## Q4. 量级鸿沟标记

未发现 `10^N` vs `10^M` 的量级比较，未发现具体数量级估算。✅

## Q5. 代数验算

### 5a. 逐步展开

#### 满秩吸收

给定：`G_W(P)` 在有限 `Y_K` 中生成满秩。

1. `S_W(P)=span G_W(P)`。
2. 满秩于有限 `Y_K` 表示 `dim S_W(P)=dim Y_K` 且 `S_W(P) subset Y_K`。
3. 因此 `S_W(P)=Y_K`。
4. 任取 `r in Y_K`，有 `r in S_W(P)`。
5. quotient 中 `[r] in Y_K/S_W(P)` 等于零等价类。
6. 所以 `Obs^W_P(r)=0`。

代数结论：✅

#### residual-shaped column

给定：`G_W` 可依赖 `r`，并允许 `c=r`。

1. 取 `c=r`。
2. `S_W` 至少包含 `span{c}`。
3. 因 `c=r`，故 `r in span{c} subset S_W`。
4. quotient 中 `[r]=0`。
5. 所以 `Obs^W_P(r)=0`。

代数结论：✅

#### 强判据改写

给定中间式：`G_W(P,r)`。  
强判据：`G_W(P)={ c | exists W_c : Verify_P^pre(c,W_c)=1 }`。

1. 将候选列枚举阶段的输入从 `(P,r)` 改为 `P`。
2. 将 residual `r` 的出现位置限制到最终 quotient projection：`Obs^W_P(r)=[r] in Y/S_W(P)`。
3. 因此候选空间不能通过定义阶段直接取 `c=r`，除非 `c` 已由 pre 阶段独立生成。

代数/依赖方向结论：✅

### 5b. 极限退化

- 空候选极限：`G_W(P)=empty` 时，`S_W(P)={0}`，`Obs^W_P(r)=[r]`，非零 residual 不被吸收。✅
- 满秩候选极限：`S_W(P)=Y_K` 时，任意 `r in Y_K` 有 `Obs^W_P(r)=0`。✅
- 非 oracle 极限：`I(c;r|P_pre,D_c)=0` 时，`c` 不从 residual 形状取信息；若 `I>0` 且无独立来源，则触发拒绝条件。✅

### 5c. 数值量级验证

输入文件未给出需要代入的具体物理数值或数量级估算。✅

### 5d. 引用数值来源级别

输入文件列出 DOI、年份等文献元数据，但未将其作为数值推导参数。没有需要验算的物理数值来源。✅

## Q6. 综合判定

✅ INSPECTOR通过。

⚠️ INSPECTOR警告：`G_W(P,r)` 作为中间定义会产生 residual 依赖风险；输入文件已给出强判据 `G_W(P)` 与 `Verify_P^pre` 修正。后续推导必须只把 `r` 用于最终 projection/holdout 检验，不能用 `r` 生成候选列或 witness。

阻断项：无。
