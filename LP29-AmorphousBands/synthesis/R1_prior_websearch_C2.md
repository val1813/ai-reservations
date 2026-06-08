# LP29-C2 R1 先发拦截 WebSearch

## 查询

按 Phase 清单要求，PI 独立 WebSearch，不依赖 A博士 §-1:

1. `amorphous oxide semiconductor graph metrics residual predictive power orbital overlap mobility edge 2023 2024 2025`
2. `amorphous oxide orbital overlap graph connectivity residual transport effective mass 2023 2024 2025`
3. `same sample orbital overlap graph spectral features amorphous oxide transport mobility 2023 2024 2025`

## 命中与判定

- Jankousky et al., *Effective Bands and Band-Like Electron Transport in Amorphous Solids*, Nature Physics 2026: 与 LP29 大背景高度相关，覆盖 a-In2O3 effective bands、band-like transport、disorder-limited mobility。不是 C2 的 OI-vs-graph residual 同样品比较。
- Current Opinion in Solid State and Materials Science 2023 AOS review: 强背景综述，说明 AOS 高 mobility 与材料体系已成熟；不是 C2 同样品 residual protocol。
- Amorphous In2O3 structure/properties PMC 旧文: 结构网络、In-O-In 角、extended conductivity paths 与 mobility 相关，构成强先发压力；不是 OI baseline 后 graph residual 检验。
- 2025 ACS/Purdue PDF 命中 equivariant graph neural network 与 amorphous mobility 相关: 与 graph-to-mobility 方向相关，需后续核查是否包含 OI baseline；当前搜索片段不足以判定完全重合。
- 未发现题名/摘要层面直接声称: “在 same-sample amorphous oxide 数据上，控制 Srivastava orbital-overlap integral 后，graph spectral features 仍预测 Hall/Drude/Wannier/spectral residual labels”。

## PI 判定

部分重合，继续但收窄声张。

被吞掉的部分:

- AOS mobility 与 metal-s orbital overlap/structural connectivity 的一般关系不是新。
- effective bands / band-like amorphous In2O3 transport 不是新。
- graph/ML structure-to-mobility 方向已有新近压力。

C2 的剩余差异化:

> 以 Srivastava orbital-overlap integral 作为强 baseline，在同一样品 external labels 上测试 graph spectral features 是否还有 residual predictive power，并用 target-leakage、degree/weight-preserving rewiring 和 leave-one-family-out 控制防止自证循环。

## 后续要求

下一轮必须补查 2025 graph/GNN mobility 文献是否已经包含 orbital-overlap baseline 或等价 ablation；若包含，C2 将进一步降级。
