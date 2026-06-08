# LP29-C2 GATE -1 核心矛盾结构验证

## 当前北极星

LP29-C2: LP29 graph metrics 是否只是 Srivastava orbital-overlap metric 的重参数化？

## 命题

命题A: Srivastava-style orbital-overlap integral 已吸收结构对 transport/effective mass 的主要解释力；LP29 graph metrics 只是换名或弱重参数化。

命题B: 控制 orbital-overlap、onsite variance、density、mobility-edge margin 与 batch/finite-size 后，graph spectral features (`lambda_2`, spectral radius, high-betweenness damage) 仍对 external Hall/Drude/Wannier/spectral residual labels 有独立预测力。

## paper-search-mcp 核查

- A 侧证据: Srivastava et al., "Electronic structure and transport in amorphous metal oxide and amorphous metal oxynitride semiconductors", DOI `10.1063/1.5096042`。MCP 返回摘要指出 electron transport 可由 orbital overlap integral 从结构信息解释，并与 effective mass 相关。
- B 侧证据: Jankousky et al., "Effective bands and band-like electron transport in amorphous solids", DOI `10.1038/s41567-025-03099-x`。MCP 确认该文献存在；项目内 PDF/REVIEWER 已记录其覆盖 a-In2O3 effective bands、O-O defects、coordination、IPR/linewidth/mobility。

## 三问

Q-1.1 命题A是否有独立实验/观测证据支持为真？YES。Srivastava 2019 给出 orbital-overlap integral 与 transport/effective mass 的结构解释路径。

Q-1.2 命题B是否有独立实验/观测证据支持为真？YES。Jankousky 2025/2026 对 a-In2O3 给出结构/缺陷/effective-band/transport 关联；B 的“残差独立性”尚未验证，但其结构图谱可能含额外信息有独立基础。

Q-1.3 命题A和命题B在逻辑上是否不能同时为真？YES, 在“graph metrics 是否提供 orbital-overlap baseline 之外的独立残差预测力”这一层面互斥。若 A 为真，加入 overlap baseline 后 graph residual power 应消失；若 B 为真，graph spectral features 在严格 controls 后仍有外部标签残差预测力。

## 判定

GATE -1 通过。LP29-C2 可以进入 Phase 启动后续步骤。
