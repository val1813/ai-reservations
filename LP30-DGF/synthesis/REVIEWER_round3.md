# REVIEWER Round 3

裁定：建议拒稿。

## 第零步幻觉检查

- `V_env(t)=V_floor+(V_ref-V_floor)exp(-Gamma_env t)`：量纲可接受，若 `Gamma_env` 为 `s^-1`。
- `V_DGF=V_ref*sin(pi*q/2)`：量纲可接受。
- `m_model=(2*m_p/pi)*sin(pi*q/2)`：量纲可接受。
- `x_i=log(M_cal_i)`：量纲错误。应为 `log(M_cal_i/M_ref)`。

## 查重摘要

REVIEWER 使用 paper-search-mcp，未降级 WebSearch。未发现 exact `DGF-N4 / latent-q / 13.85 microgram` 直接先发，但第三轮否定性搜索未完整完成，因此不能声称否定性查重完全通过。

## 叙事退让

发现重大退让：

- 从“自然质量上界”退到“模型约束边界”。
- 从“物理机制证明”退到“经验 latent visibility 拟合”。
- 从“fold caustic”退到“fold-type critical endpoint”。
- 从“q 独立性判据”退到“尚需定义样本空间、rank、bootstrap/null”。

## 五条拒稿理由

1. 核心物理声张已坍缩为模型参数化。`13.85 microgram` 不是证明出的自然上界，只是 `2*m_p/pi` 的模型边界。[致命]
2. M1 逐点自由 `q_i` 导致不可接受的过拟合。[致命]
3. `q_visibility=q_DGF_mass` 是未证明桥接假设。[严重]
4. B 路线术语和量纲均不合格：`log(M_cal_i)` 量纲错误，`fold caustic` 缺 Jacobian / density 支撑。[严重]
5. LLR 表和独立性判据不完整，统计判别不可复现。[严重]

## 致命一击

M1 的逐点自由 `q_i` 加上未证明的 `q_visibility=q_DGF_mass` 桥接，使 DGF 模型同时获得过拟合能力和伪物理解释；因此 LLR 不能被解释为 DGF 物理机制的证据。

## 作者出路

- 固定或层级化 `q`。
- 预注册 null/M1 参数数目。
- 给出惩罚化 likelihood 或 out-of-sample 预测。
- 独立证明 visibility-q 与 mass-q 桥接。
- 补全 LLR 表、bootstrap/null、rank 判据。
- 删除 “自然质量上界” 和 “fold caustic” 强措辞。
