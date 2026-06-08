# REVIEWER Round 3 响应

## 独立核查结果

REVIEWER 的主要先发风险成立。

- Srivastava et al. 2019, DOI `10.1063/1.5096042`: 已明确提出 amorphous oxide / oxynitride transport 可由 orbital overlap integral 从结构信息解释，并关联 effective mass。LP29 的 In-s graph metrics 必须与该 overlap metric 做差异化，不能声称 orbital-overlap/structure-transport 关系为新。
- Nenashev/Baranovskii 2019/2022, DOI `10.1103/physrevb.100.125202`, `10.1002/9781119715641.ch6`: 已有 amorphous oxide semiconductor 的 percolation / random barrier / disorder-dominated band conduction 框架。LP29 不能泛称 percolation transport 新。
- Jankousky et al. 2026, DOI `10.1038/s41567-025-03099-x`: 已覆盖 effective bands、band-like transport、1500 structures、100 QSGW subset、O-O defects、coordination、IPR/linewidth/mobility 解释。LP29 的唯一空间是 same-sample residual comparison / external-label protocol。

## 追加实做

### B1 完成

已创建可复现 synthetic toy benchmark:

- `current/B/scripts/generate_toy_ensemble.py`
- `current/B/artifacts/B1_toy_seed_level.csv`
- `current/B/artifacts/B1_toy_edge_list.csv`
- `current/B/artifacts/B1_toy_ensemble_summary.csv`

该 artifact 只是 synthetic benchmark，不是材料实测或 DFT/Wannier 结果。作用是修复 REVIEWER 指出的“无 seed-level CSV/脚本/edge list”问题。

### A1 部分完成

已创建 A1 待数字化 schema:

- `current/A/artifacts/A1_Furubayashi2019_digitized_transport_schema.csv`

尝试用 MCP 和 publisher URL 下载 Furubayashi 2019 PDF 失败:

- `paper-search-mcp download_with_fallback`: CrossRef 无 PDF，Unpaywall 无 OA URL。
- Springer/SpringerOpen PDF URL 返回 3 KB `Client Challenge` HTML，不是论文 PDF。

因此 A1 真实 digitized CSV 尚未完成。当前状态必须记录为 `blocked_by_pdf_access_or_manual_digitization_needed`，不能声称已有真实 A1 数据。

## 致命卡点登记

1. 缺真实 same-sample external labels: 仍无非循环数据证明 graph metrics 在 mobility-edge/Ioffe-Regel controls 之外有残差预测力。
2. Jankousky raw structures/QSGW subset 尚未取得；只能从 PDF 摘要级文本确认其存在。
3. A1 Furubayashi PDF 下载被 challenge 阻断，需要人工打开/下载或另找可访问镜像。
4. LP29 当前仍是 protocol-development project，不是 publishable physics result。

## 下一步

若继续推进，优先顺序:

1. 获取 Furubayashi 2019 PDF 或手动数字化 Fig/Table，生成 A1 full CSV。
2. 获取 Jankousky SI/raw structures 或记录不可得，转向 Aliano 2011 AIMD fallback。
3. 对 B1 synthetic benchmark 运行 locked ablation，确认脚本输出与 Round 3 表一致。
4. 将 Srivastava orbital-overlap metric 加入 baseline，对比 LP29 graph metrics 是否只是换名。
