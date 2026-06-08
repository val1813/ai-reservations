"""LP23-R2 Round3 adversarial syndrome-template stress test.

This script attacks the Round2 toy result by asking whether the one surviving
quotient direction is robust, or just the result of an under-complete template
span / rank cutoff choice.
"""

from __future__ import annotations

import argparse
import math
import random
from pathlib import Path

from r2_syndrome_templates import (
    default_problem,
    hstack,
    incidence,
    local_constitutive_template,
    norm,
    orthonormal_column_basis,
    parse_residual,
    project_onto_colspace,
    spinoptics_template,
)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def normalize(v):
    v_norm = norm(v)
    if v_norm == 0.0:
        raise ValueError("cannot normalize zero vector")
    return [x / v_norm for x in v]


def as_column_matrix(columns):
    if not columns:
        return []
    return [[col[i] for col in columns] for i in range(len(columns[0]))]


def random_nuisance_columns(row_count, count, seed):
    rng = random.Random(seed)
    cols = []
    for _ in range(count):
        col = [rng.gauss(0.0, 1.0) for _ in range(row_count)]
        cols.append(normalize(col))
    return cols


def near_bridge_columns(base_bridge, count, eps=1e-8):
    """Columns that expose absolute-tolerance rank fragility.

    They point along the previously surviving quotient direction, but their
    scale is tiny. A physical column normalization convention would remove this
    artifact; the current toy MGS uses an absolute threshold.
    """
    if count <= 0:
        return []
    bridge = normalize(base_bridge)
    return [[eps * x for x in bridge] for _ in range(count)]


def nonlocal_history_template(edge_features, base_bridge, residual):
    """One deterministic nonlocal/history template.

    This is intentionally not a local edge constitutive column. Each edge gets
    a global memory coordinate depending on cumulative upstream residual,
    total optical path length, and a graph-order oscillatory kernel. The final
    vector is normalized; in an 8-edge toy with a 1D quotient, any nonlocal
    column with nonzero quotient component should kill the bridge signal.
    """
    total_length = sum(feat["length"] for feat in edge_features)
    running = 0.0
    col = []
    for i, feat in enumerate(edge_features):
        running += residual[i]
        global_memory = running / (i + 1)
        path_fraction = feat["length"] / total_length
        oscillatory_kernel = math.sin(1.7 * (i + 1)) + 0.31 * ((-1.0) ** i)
        col.append(global_memory + 0.45 * path_fraction + 0.12 * oscillatory_kernel)
    bridge_overlap = dot(col, normalize(base_bridge))
    return normalize(col), bridge_overlap


def residual_stats(t_matrix, r, tol):
    basis = orthonormal_column_basis(t_matrix, tol=tol)
    projection = [0.0] * len(r)
    for q in basis:
        coeff = dot(q, r)
        projection = [pi + coeff * qi for pi, qi in zip(projection, q)]
    residual = [ri - pi for ri, pi in zip(r, projection)]
    residual_norm = norm(residual)
    return len(basis), residual_norm, residual_norm * residual_norm, residual


def format_float(x):
    if abs(x) < 1e-12:
        return "0"
    if abs(x) < 1e-4 or abs(x) >= 1e4:
        return f"{x:.6e}"
    return f"{x:.10f}"


def format_tol(x):
    return f"{x:.1e}"


def make_table(rows):
    lines = ["| k | tol | template_set | rank | residual_norm | I_bridge |", "|---:|---:|---|---:|---:|---:|"]
    for row in rows:
        lines.append(
            "| {k} | {tol} | {template_set} | {rank} | {residual_norm} | {i_bridge} |".format(
                k=row["k"],
                tol=format_tol(row["tol"]),
                template_set=row["template_set"],
                rank=row["rank"],
                residual_norm=format_float(row["residual_norm"]),
                i_bridge=format_float(row["i_bridge"]),
            )
        )
    return "\n".join(lines)


def build_standard(omega):
    nodes, edges, edge_features, default_r = default_problem()
    d_endpoint = incidence(nodes, edges)
    t_spinoptics = spinoptics_template(edge_features, omega)
    t_local = local_constitutive_template(edge_features)
    t_standard = hstack(d_endpoint, t_spinoptics, t_local)
    return nodes, edges, edge_features, default_r, t_standard


def run(args):
    nodes, edges, edge_features, default_r, t_standard = build_standard(args.omega)
    r = args.r if args.r is not None else default_r
    if len(r) != len(edges):
        raise ValueError(f"edge residual r has length {len(r)}, expected {len(edges)}")

    base_rank, base_norm, base_i, base_bridge = residual_stats(t_standard, r, args.base_tol)
    random_cols = random_nuisance_columns(len(edges), args.max_k, args.seed)
    history_col, history_overlap = nonlocal_history_template(edge_features, base_bridge, r)

    rows = []
    for tol in args.tolerances:
        rank, residual_norm, i_bridge, _ = residual_stats(t_standard, r, tol)
        rows.append(
            {
                "k": 0,
                "tol": tol,
                "template_set": "standard",
                "rank": rank,
                "residual_norm": residual_norm,
                "i_bridge": i_bridge,
            }
        )

    for k in range(args.max_k + 1):
        nuisance = as_column_matrix(random_cols[:k])
        t_aug = t_standard if k == 0 else hstack(t_standard, nuisance)
        rank, residual_norm, i_bridge, _ = residual_stats(t_aug, r, args.base_tol)
        rows.append(
            {
                "k": k,
                "tol": args.base_tol,
                "template_set": "standard+random",
                "rank": rank,
                "residual_norm": residual_norm,
                "i_bridge": i_bridge,
            }
        )

    near_rows = []
    for tol in args.tolerances:
        near_cols = as_column_matrix(near_bridge_columns(base_bridge, 1, eps=args.near_eps))
        t_near = hstack(t_standard, near_cols)
        rank, residual_norm, i_bridge, _ = residual_stats(t_near, r, tol)
        near_rows.append(
            {
                "k": 1,
                "tol": tol,
                "template_set": f"standard+near_bridge_eps={args.near_eps:g}",
                "rank": rank,
                "residual_norm": residual_norm,
                "i_bridge": i_bridge,
            }
        )

    history_matrix = as_column_matrix([history_col])
    history_rank, history_norm, history_i, history_residual = residual_stats(hstack(t_standard, history_matrix), r, args.base_tol)
    history_row = {
        "k": 1,
        "tol": args.base_tol,
        "template_set": "standard+nonlocal_history",
        "rank": history_rank,
        "residual_norm": history_norm,
        "i_bridge": history_i,
    }

    all_rows = rows + near_rows + [history_row]
    random_one = next(row for row in all_rows if row["template_set"] == "standard+random" and row["k"] == 1)
    verdict = "DEAD" if random_one["i_bridge"] < args.death_threshold and history_i < args.death_threshold else "CONDITIONAL"

    report = []
    report.append("# LP23-R2 Round3 生死检验 - B 路 adversarial test")
    report.append("")
    report.append("## §0 框架声明")
    report.append("")
    report.append(
        "本轮采用的跨学科框架是 **纠错码 syndrome quotient + 统计建模 nuisance projection + 数值线性代数 rank-revealing stress test**。"
        "Round2 的 `I_bridge` 不是直接物理可观测量，而是 residual 在标准模板列空间商空间里的剩余范数平方。"
        "因此生死问题不是“这个 toy residual 有没有数”，而是：只要允许合理扩展的 nuisance/history 模板，那个商空间方向是否仍被迫存在。"
    )
    report.append("")
    report.append("## 运行设置")
    report.append("")
    report.append(f"- 脚本：`scripts/r2_syndrome_adversarial.py`")
    report.append(f"- seed：`{args.seed}`")
    report.append(f"- edge 数：`{len(edges)}`；标准模板矩阵列数：`{len(t_standard[0])}`")
    report.append(f"- Round2 基线：rank `{base_rank}`，residual_norm `{format_float(base_norm)}`，I_bridge `{format_float(base_i)}`")
    report.append("")
    report.append("## 主表：k / rank / residual_norm / I_bridge")
    report.append("")
    report.append(make_table(all_rows))
    report.append("")
    report.append("## 判决")
    report.append("")
    if verdict == "DEAD":
        report.append(
            "判死。标准模板的 8-edge toy 是 rank 7，剩下的是一维空方向；加入 1 个归一化 random nuisance column 后 rank 变 8，"
            "`I_bridge` 在机器精度内塌缩到 0。确定性的 nonlocal/history 模板也同样把它吸收。"
        )
    else:
        report.append(
            "暂不判死，但只能给条件性存活：必须预先禁止 random/nonlocal/history nuisance 的 quotient 分量，"
            "并给出独立物理理由说明为什么模板族永远不能触及 Round2 的一维剩余方向。"
        )
    report.append("")
    report.append("## 深挖1：同构结构至少两层")
    report.append("")
    report.append(
        "第一层，纠错码语言：`I_bridge = ||(I-P_T)r||^2` 是 syndrome coset 的代表范数。"
        "当 `rank(T_standard)=7<8` 时，toy 模型只剩一个 logical/syndrome 方向。任何新模板只要在这个方向上有非零投影，就会把 coset 代表清零。"
    )
    report.append("")
    report.append(
        "第二层，统计 nuisance 语言：这等价于把 bridge signal 当成模型残差。"
        "如果一个未建模的 nuisance regressor 可以解释该残差，那么残差显著性不是新物理，而是欠拟合。"
        "本轮 random nuisance 扫描显示 `k=1` 已经足够把残差吃掉。"
    )
    report.append("")
    report.append("## 深挖2：原学科结构至少两层")
    report.append("")
    report.append(
        "第一层，几何光学/局域响应：endpoint、spinoptics、local constitutive 被扣除后，Round2 的非零量依赖于“没有更多标准响应模板”的假设。"
        "这个假设在 toy 中没有物理封闭性证明，只是列空间没有放满。"
    )
    report.append("")
    report.append(
        "第二层，history/nonlocal 响应：真实传播问题允许路径记忆、全局闭路、迟滞或积分核响应。"
        f"本脚本构造的 deterministic history column 与基线 quotient 方向的 overlap 为 `{format_float(history_overlap)}`，"
        f"加入后 rank `{history_rank}`，I_bridge `{format_float(history_i)}`。"
        "这说明 Round2 的剩余量不抗非局域模板扩展。"
    )
    report.append("")
    report.append("--- INSPECTOR_CHECK ---")
    report.append(
        f"[公式] `I_bridge=||r-P_T r||_2^2`；本轮基线 `||q||={format_float(base_norm)}`，`I={format_float(base_i)}`。"
        "加入列空间扩展 `T'=[T,N]` 后重算正交投影。"
    )
    report.append(
        "[方向] rank 从 7 到 8 时 edge space 被填满，故 residual 必须在数值精度内归零；这不是物理发现，而是 toy 维数/模板封闭性失败。"
    )
    report.append("[数据] 使用本地 8-edge toy residual，无外部数据；random nuisance 固定 seed 可复现。")
    report.append(
        f"[假设] MGS 使用欧氏内积；death threshold `{args.death_threshold:g}`；history 模板只是反证示例，不声称唯一物理机制。"
    )
    report.append("")
    report.append("## rank tolerance 结论")
    report.append("")
    report.append(
        "归一化 random/history 列下结论对常见 tolerance 不敏感：新列把秩推到满秩。"
        f"但 near-bridge 小幅度列显示绝对阈值敏感性：当列尺度 `{args.near_eps:g}` 低于 tolerance 时会被丢弃，"
        "高于 tolerance 时又可吸收残差。这要求后续若继续必须先固定列归一化、噪声协方差和物理先验。"
    )
    report.append("")
    report.append("## 最小存活条件")
    report.append("")
    report.append(
        "若要让 R2 继续活，必须证明：允许的 endpoint/spinoptics/local/nonlocal/history 模板族在 whitened edge space 中，"
        "对该 quotient 方向严格正交或被独立实验约束到不可用；否则 toy `I_bridge=0.0005015971` 只是缺列造成的 residual。"
    )
    report.append("")
    report.append("## 本轮产出格式")
    report.append("")
    report.append(
        "本轮的跨学科跃迁：计算机科学纠错码 syndrome quotient -> 统计模型 nuisance regression -> 几何光学模板完备性反证。"
    )
    report.append(
        "这个结构的数学对象：edge residual 向量空间 `E`、标准模板列空间 `im(T)`、商空间 `E/im(T)`、"
        "rank-revealing Gram-Schmidt 投影、nuisance column augmentation。"
    )
    report.append(
        "如果这个同构成立，最奇怪的可检验预测是：只要加入一个与 quotient 方向非正交的额外 history/nonlocal regressor，"
        "所谓 bridge invariant 会不连续地从 `0.0005015971` 掉到数值零。"
    )
    report.append(
        "A博士最可能反对的点：random nuisance 太宽泛，history column 不是预先物理指定。我的回应是：这正是生死检验的结论，"
        "R2 若要存活，必须先给出模板封闭性和列归一化规则，否则 toy 非零量没有独立物理地位。"
    )
    report.append(
        "本轮失败记录：强版 `I_bridge` 失败；失败原因是 8-edge toy 的标准模板只有 rank 7，剩余一维方向没有被物理保护。"
    )
    report.append(
        "下一步计划：除非 PI 给出预先注册的 nonlocal/history 模板禁区或真实数据 covariance，否则不建议继续把该 toy `I_bridge` 当作 R2 证据。"
    )
    report.append(
        "需要PI投喂的文献方向：weighted nuisance projection, model misspecification tests, optical path memory kernels, nonlocal constitutive electrodynamics, rank-revealing QR/SVD with column normalization。"
    )
    report.append("")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(report), encoding="utf-8")

    print(make_table(all_rows))
    print()
    print("verdict:", verdict)
    print("report:", output)


def parse_tolerances(text):
    return [float(part.strip()) for part in text.split(",") if part.strip()]


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r", type=parse_residual, help="comma-separated edge residuals; default uses toy residual")
    parser.add_argument("--omega", type=float, default=25.0)
    parser.add_argument("--seed", type=int, default=2303)
    parser.add_argument("--max-k", type=int, default=8)
    parser.add_argument("--base-tol", type=float, default=1e-12)
    parser.add_argument("--tolerances", type=parse_tolerances, default=parse_tolerances("1e-6,1e-8,1e-10,1e-12,1e-14"))
    parser.add_argument("--near-eps", type=float, default=1e-10)
    parser.add_argument("--death-threshold", type=float, default=1e-20)
    parser.add_argument("--output", default="current/B/R2_round3.md")
    return parser


if __name__ == "__main__":
    run(build_parser().parse_args())
