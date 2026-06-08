# REVIEWER Report | PRL_manuscript_v2

**Date:** 2026-06-04
**Scope:** `current/plan/PRL_manuscript_v2.md`
**Auxiliary files checked:** `PRL_supplementary.md`, `cover_letter.md`, `PRL_benchmark.md`, `文献库.md`, local verification outputs.
**Mode:** SOP independent malicious reviewer subagent.

---

## 第零步幻觉检查

- **量纲:** `|C_mid| ~ L^{-β}`、`β=a/α+b` 量纲上可过；`J0/γ_phi` 无量纲需明确单位制。
- **方向:** `β` 随 `α` 降、`μ=2α-2` 随 `α` 升，反相关可能只是参数扫描的直接结果。
- **循环论证:** 用数值拟合出的 `β` 再用 AICc/插值解释 `1/α`，没有独立预测。
- **量级/有限尺寸鸿沟:** `L=4,8,16,32,64` 对 long-range hopping 不足以支持 thermodynamic exponent；`L=4` 进入幂律拟合尤其危险。

## 三轮查重结果

- **方法层:** paper-search-mcp 检到同模型强相关文献：Sarkar et al., PRB 109, 165408 (2024)，Dhawan et al., PRB 110, L081403 (2024)，Bhat & Znidaric, PRB 111, 174306 (2025)。
- **框架盲区:** 检到 Lancaster & Godoy, PRR 1, 033104 (2019) 的 NESS power-law correlations；Jin et al., PRR 4, 013109 (2022) 的 noisy free fermion / Green's-function transport 框架。
- **否定性搜索:** 未发现完全相同的“β 指数”已发表，但有限尺寸漂移、稳态关联函数已知框架、单参数标度误判风险都有文献背景。
- **工具清单:** 全部学术检索使用 paper-search-mcp；未使用 WebSearch。

## 五条拒稿理由

1. **`β=a/α+b` 的证据等级不足。 [致命]**

   `β=a/α+b` 被称为解析推导，但补充材料 S3.6-S3.7 明确承认关键步骤只是 scaling hypothesis。两点极限加五个 `α` 点的 AICc 不能把插值升级为 universality exponent。

   作者若回应，需要证明：从 fractional diffusion + nonlocal Robin BC 推出唯一 `1/α` 形式，并给出不依赖拟合的 `a,b` 或可检验预测。

2. **有限尺寸证据不足以支持 PRL 级“第二标度指数”。 [致命]**

   所有 `β` 来自 `L=4-64` 五点拟合，且 long-range hopping 在 `α=1.1` 附近有限尺寸修正最慢；稿件自己承认 `L=128` 未提取 midchain β。

   作者若回应，需要证明：至少给出 `L=128/256` 的系统 β 外推、去掉 `L=4` 后稳定性、correction-to-scaling 拟合和误差传播。

3. **“β 与 μ 独立”和 speed-coherence trade-off 的逻辑不成立。 [严重]**

   固定 `α` 改 `γ_phi` 只说明 `β` 依赖退相干，而引用的 `μ(α)` 未含 `γ_phi`；稿件写出的 `∂β/∂μ|_α ≈ (∂β/∂γ_phi)/0` 是未定义量，不是物理证明。

   作者若回应，需要证明：同一模型、同一参数扫描下同时测 `μ(α,gamma_phi,Gamma)` 与 `β`，并展示二者来自可分离 Liouvillian 谱投影。

4. **“universality-class exponent” 与 Γ 测试自相矛盾。 [严重]**

   Γ 改变导致 `β` 变化约 6.8%，且是 `3.9σ` 统计显著效应；这不能被包装成普适，只能说明边界条件影响指数估计。

   作者若回应，需要证明：Γ 依赖是有限尺寸 correction 而非 asymptotic exponent 依赖，并给出 RG/边界固定点论证。

5. **纯虚 off-diagonal 的证明存在结构性漏洞。 [严重]**

   主文 Green's-function 表达式只含 `gamma_phi+i(epsilon_m-epsilon_n)`，但边界 Lindblad damping/inhomogeneous source 不在同一对角本征基中；补充材料随后改用“实部 offdiag 是齐次且严格对角占优”的说法，也没有处理 `Re C` 与 `Im C` 经 `i[h,C]` 的耦合。数值到 `1e-15` 更像求解器/对称性检查，不等于证明。

   作者若回应，需要证明：给出完整 Lyapunov superoperator 层面的 symmetry theorem，包括边界 Γ、非厄米阻尼和唯一稳态条件。

## 如果必须挑一个致命错误

最致命的是把 S3.6-S3.7 的插值假设包装成“解析推导的 `β=a/α+b` universality exponent”；这是中心结论的证据等级问题，不是小修语病。

## 建议

**拒稿。** 核心“第二普适指数”的解析性、热力学极限和独立性都没有被证明，当前更像有限尺寸数值现象加事后拟合，达不到 PRL 标准。

## PI 补充观察

本地主上下文检查还发现两个可被审稿人放大的内部风险：

- `referee_response_L128.json` 中 L=128 结果与 L<=64 表格存在明显方向漂移：例如 `alpha=1.7,1.9` 的 L128/tail16 beta 显著升高，可能直接攻击“β 随 α 下降”和“L<=64 effective exponent 可外推”。
- `model_selection_results.json` 中 `1/α` 并非所有 `gamma_phi` 下的最优模型；例如 `gamma_phi=0.1` 下 linear 的 AICc 更低，`gamma_phi=0.01` 下 `ln alpha`/三参数形式更优或近似退化。这会削弱“1/α functional form”作为全局主结论。
