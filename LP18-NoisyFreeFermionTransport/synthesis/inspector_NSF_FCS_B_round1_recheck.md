# INSPECTOR recheck: NSF_FCS_round1_B

输入文件：
- `current/B/NSF_FCS_round1_B.md`
- `synthesis/inspector_NSF_FCS_B_round1.md`

执行限制记录：未读取 A 文件。只复查 B 对上一轮 INSPECTOR 阻断与警告的修复情况。

## 复审结论

`INSPECTOR 通过，可继续。`

上一轮阻断项已经修复：B 当前稿的核心二阶增长率公式已统一为

`lambda_R''(0)= a_R + 2 <b_R-j_R, phi_R>_pi`

其中 `b_R(x)=sum_y k(x,y) g_R(x,y)` 是状态函数，`<.,.>_pi` 只作用于状态函数。未再发现把边跳变函数 `g_R(x,y)` 直接与 `j_R` 相减并放入 `pi` 状态内积的核心公式错误。

仍保留两个非阻断警告：renewal 公式只能作为满足适用条件时的启发/诊断层；buffer reservoir 目前是避免循环的诊断设计，不是已经证明的模型内反例。

## 1. `b_R` 状态函数内积复查

B 当前稿明确定义：

`b_R(x)=sum_y k(x,y) g_R(x,y)`

并写明：

`<f,h>_pi=sum_x pi(x) f(x) h(x)`

同时强调 `g_R(x,y)` 只用于定义状态函数 `b_R(x)` 和 activity `a_R`，不直接进入 `pi` 内积。

复查结果：

- `g_R(x,y)` 是边跳变 reward，定义在跃迁边上。
- `b_R(x)` 对出边按速率求和后成为状态函数，单位为 `time^-1`。
- `j_R=sum_x pi(x)b_R(x)` 可视为常数状态函数，单位为 `time^-1`。
- `b_R-j_R` 是合法状态函数，可与 `phi_R` 做 `pi` 内积。

判定：通过。上一轮关于 `g_R-j_R` 类型不匹配、内积空间错误的阻断已经消除。

## 2. `lambda_R''=a_R+2<b_R-j_R,phi_R>` 量纲/符号复查

量纲：

- `lambda_R''(0)=lim_{t->infty} t^-1 Var Q_R(t)`，单位 `time^-1`。
- `a_R=sum_x pi(x)sum_y k(x,y)g_R(x,y)^2`，单位 `time^-1`。
- `b_R-j_R`，单位 `time^-1`。
- Poisson 方程 `-L phi_R=b_R-j_R` 中 `L` 单位 `time^-1`，因此 `phi_R` 无量纲。
- `<b_R-j_R,phi_R>_pi` 单位 `time^-1`。

因此右边 `a_R+2<b_R-j_R,phi_R>_pi` 与左边 `lambda_R''(0)` 同为 `time^-1`。

符号：

- B 采用 `-L phi_R=b_R-j_R` 的约定。
- 在该约定下，Markov additive functional 的方差率写作 `a_R+2<b_R-j_R,phi_R>_pi` 是符号自洽的。
- `K_R=2<b_R-j_R,phi_R>_pi` 可为负，但总和 `lambda_R''=A_R+K_R` 必须非负；B 的数值流程应继续显式检查 `A_R+K_R>=0`。

判定：量纲通过，符号约定通过。非负性检查作为后续数值实现要求，不构成本轮阻断。

## 3. renewal 适用条件复查

上一轮警告要求 B 不得把 renewal 公式当作无条件证明，尤其要处理独立性、有限二阶矩、`X-tau` 相关项和零平均 reward 情形。

B 当前稿已补充适用条件：

- 相邻更新近似独立或只有短程相关。
- 等待时间 `tau` 有有限二阶矩。
- 单次净转移 `X_n` 与等待时间的相关可忽略，或可用有限协方差修正。
- 不存在随 `t` 不收敛的 aging。
- 若条件失败，应回到 Markov Poisson 方程，而不是把 renewal 公式当证明。

复查结果：

- 这些条件覆盖了上一轮指出的主要适用性缺口。
- B 当前稿把 renewal 公式称为“启发”，没有把它作为最终证明。
- 仍需注意：若用于平衡或线性响应 leading variance，简化式
  `Var(X)/E[tau] + (E[X])^2 Var(tau)/E[tau]^3`
  在 `E[X]=0` 或 `X` 与 `tau` 显著相关时不够完整，应使用 `Var(X-j tau)/E[tau]` 或加入协方差项。

判定：阻断解除。保留警告：renewal 层只能作为诊断解释，最终判定必须落回 Poisson 方程或显式验证 renewal 条件。

## 4. buffer reservoir 诊断是否避免循环

上一轮警告的核心是：不能为了得到不同 variance 反向选择 `u_L,v_L`，再把差异当作反例；必须先只用平均 current / conductance 固定参数，再盲算 FCS。

B 当前稿已经明确：

- 调参步骤只允许使用平均 current / linear-response 数据。
- 校准 `G_R(L)` 时不得查看 `lambda_R''(0)` 或 `S_R(L)`。
- 校准冻结后，第二阶段才盲算 `A_R,K_R,lambda_R''(0),S_R(L)`。
- 只有盲算结果显示 `S_R(L)` 不同，才记为诊断性分离证据。
- 若标准物理问题固定为 Markovian Bernoulli bath，buffer reservoir 可能只是改变模型；B 已把它降格为诊断实验，而非直接模型内反例。

复查结果：

- 该设计避免了直接循环论证，因为选参输入不包含目标 variance。
- 当前文本仍没有证明一定存在两组同 `G_R` 标度而不同 `S_R` 的参数；它只是给出可检验构造。
- 因此它可以作为后续数值诊断方案，但不能在未计算前作为已成立结论引用。

判定：循环论证阻断不存在。保留范围警告：buffer reservoir 是否属于原问题允许的 reservoir class，需要 PI 或后续 REVIEWER/AUDITOR 判定。

## 5. 综合判定

上一轮唯一阻断项：

`lambda_R''(0)=a_R+2<g_R-j_R,phi_R>_pi`

已经修正为状态函数版本：

`lambda_R''(0)=a_R+2<b_R-j_R,phi_R>_pi`

并且 B 当前稿对 renewal 条件和 buffer reservoir 盲校准流程做了足够限定。

最终结论：

`INSPECTOR 通过。B 可继续作为诊断框架推进。`

后续不得把 renewal 近似或 buffer reservoir 构造当作已证明反例；必须按 B 自己列出的最小计算流程，先计算 `G_R,A_R,K_R,lambda_R''(0)`，再比较 `S_R(L)=lambda_R''(0)/G_R(L)`。
