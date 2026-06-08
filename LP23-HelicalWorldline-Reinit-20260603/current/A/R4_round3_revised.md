# LP23-R4 Round3 A 博士报告修正版：Passive/Causal Linear Response Witness Checker

日期：2026-06-03  
角色：A 博士（学院派，文献驱动）  
输入：`current/A/R4_round3.md`、`synthesis/INSPECTOR_A_R4_round3.md`

## 0. 修正摘要

本修正版只处理 inspector 阻断，不引入 B 路内容。

已修正：
1. `R3-3` 的 Herglotz 表示改为显式参考频率 `\omega_0` 的量纲自洽写法。
2. 结论保持更保守：在 passive/causal linear response 小域内，R4 不能作为新物理命题成立，最多降级为工具命题。
3. 明确标注 `W_nonoracle / holdout / cutoff` 的条件性循环风险。
4. 补入 `INSPECTOR_CHECK_REVISED`。

## 1. 量纲自洽的 Herglotz 表示

对有限频点集合 \(\Omega_K=\{\omega_1,\dots,\omega_K\}\)，观测向量写为

\[
y=(H(i\omega_1),\ldots,H(i\omega_K))\in Y_K .
\tag{R3-1}
\]

为避免 `R3-3` 的量纲混乱，固定参考频率 \(\omega_0>0\)，定义无量纲变量

\[
\zeta = z/\omega_0,\qquad \tau = t/\omega_0,\qquad \widetilde H(\zeta)=H(\omega_0 \zeta).
\]

则标准 Herglotz/Nevalinna 形式可写成

\[
\widetilde H(\zeta)=\tilde a+\tilde b\,\zeta+\int_{\mathbb R}
\left(\frac{1}{\tau-\zeta}-\frac{\tau}{1+\tau^2}\right)d\widetilde\mu(\tau),
\quad \tilde b\ge 0,\quad \widetilde\mu\ge 0 .
\tag{R3-3}
\]

其中 \(\tilde a\) 与 \(\widetilde H\) 同量纲，\(\tilde b\) 为无量纲斜率，\(\widetilde\mu\) 为非负测度。若坚持物理频率变量，也必须显式写出 \(\omega_0\) 并声明 \(a,b,\mu\) 的单位随 \(\omega_0\) 归一化而定。

## 2. 最小 witness schema

保持原先最小 schema，但只把它当作成熟证书的重组，不当作新物理生成器：

\[
W_{\rm passive\_response}(c)=(
W_{\rm pre},
W_{\rm origin},
W_{\rm causality},
W_{\rm passivity},
W_{\rm measurement},
W_{\rm cutoff},
W_{\rm nonoracle}
).
\]

- `W_origin`：只能是已成熟的 passive realization / Herglotz certificate / positive-real certificate。
- `W_causality`：只能来自上半平面解析性、Kramers-Kronig 一致性或 causal impulse response。
- `W_passivity`：只能来自 positive-real / dissipation inequality / KYP-LMI。
- `W_measurement`：只描述通道、单位、噪声协方差与白化规则。
- `W_cutoff`：只允许预先固定的有限阶数、有限 knot、有限带宽、有限 memory depth。
- `W_nonoracle`：必须是可审计的预注册、时间戳、hash、blind split、独立 holdout 记录。

## 3. 条件性循环风险

这里必须单独降温：

- `W_nonoracle` 只有在 **预先固定** 且 **可审计** 时才成立。
- `holdout` 只有在 **未被 residual 反推选择** 时才成立。
- `W_cutoff` 只有在 **未由 residual 后验调参** 时才成立。

因此，这三者不是“写进 schema 就自动成立”的证据，而是最容易发生条件性循环的地方。若它们是看过 residual 后再拟合出来的，那么它们最多是事后拟合记录，不是独立证书。

## 4. 核心判定

### 4.1 不保留为新物理命题

在 passive / causal linear response 的最小域内，`W_origin`、`W_causality`、`W_passivity` 这些证书都已是成熟理论覆盖项。故：

- `R4` 不能作为“新物理 witness checker”成立。
- 若保留，只能降级为 `certified passive-response residual validator` 或 `tool-level linter`。
- 它的输出语义必须限制为：

\[
\texttt{ABSORBED / FINITE\_LIBRARY\_OBSTRUCTION / ILL\_POSED / NONORACLE\_FAILED}
\]

不得输出 `NEW_PHYSICS`。

### 4.2 更保守的结论

若候选列完全来自成熟 passive certificate + finite approximation + independent calibration/holdout，那么它只是证书复用，不是新命题。  
若某些参数、knots、cutoff、basis 或 split 由 residual 之后才决定，则它们在逻辑上仍受条件性循环污染，不能当作独立证据。

## 5. INSPECTOR_CHECK_REVISED

### INSPECTOR_CHECK_REVISED

- [通过] `(R3-1)` 量纲正确：`Y_K` 中每个分量对应同一观测通道与同一单位。
- [通过] `(R3-2)` 仍是证书 tuple，不引入新的物理量纲问题。
- [通过] `(R3-3)` 已改为带参考频率 `\omega_0` 的无量纲 Herglotz 表述，积分项单位闭合。
- [通过] `W_nonoracle / holdout / cutoff` 已显式标出条件性循环风险。
- [通过] 核心判定已收紧：R4 在该最小域内硬停止为新物理命题，只能降级为工具命题。
- [通过] 已加入 `INSPECTOR_CHECK_REVISED`，可直接作为修订版检查锚点。

## 6. 修订后结论

**结论：在 passive / causal linear response 的最小物理域内，R4 不能保留为新物理命题；只能作为受限的证书验证工具。**

若后续还要保留该路线，必须额外提供真正独立的预注册、holdout、cutoff 固定与审计文件，否则 `W_nonoracle` 仍不足以排除事后拟合。
