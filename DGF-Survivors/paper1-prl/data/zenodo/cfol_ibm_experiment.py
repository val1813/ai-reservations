"""
CFOL定理实验验证
时序因果环：Q和E经历两次RZZ门，中间500ns间隔
测量：I(R;Q') 来计算 QCMI = 4 - I(R;Q')

使用方法：
  pip install qiskit qiskit-ibm-runtime
  python cfol_ibm_experiment.py --token YOUR_IBM_TOKEN

电路结构：
  R ─[H]─[CNOT]────────────────────[测量]
  Q ─────[CNOT]─[RZZ(θ₁)]─[等待]─[RZZ(θ₂)]─[测量]
  E ─[Ry(φ)]────[RZZ(θ₁)]─[等待]─[RZZ(θ₂)]─[测量]

  θ₁ = π/2（死环：identity，功能环：π/2）
  θ₂ = θ（被测试的Cartan角）
  φ = 2*arccos(√p)，控制环境纯度
"""

import numpy as np
import json
import argparse
from datetime import datetime

# ============================================
# 实验参数
# ============================================
THETAS = [np.pi/4, np.pi/8, np.pi/16]   # 三个Cartan角
P_ENV = 0.7                               # 环境纯度参数
SHOTS = 100_000                           # 每个电路的shots数
IDLE_TIME_NS = 500                        # 时序间隔（纳秒）
BACKEND_NAME = "ibm_kingston"             # 优先选择，备选见下面

# ============================================
# 构造电路
# ============================================
def make_cfol_circuit(theta, theta1=np.pi/2, p=0.7,
                      functional=True, basis='Z'):
    """
    构造时序因果环电路

    functional=True:  功能环（第一个RZZ角度=theta1）
    functional=False: 死环（第一个RZZ替换为identity）
    basis='Z' or 'X': 测量基
    """
    from qiskit import QuantumCircuit
    from qiskit.circuit.library import RZZGate

    # 3个qubit：R（参考），Q（系统），E（环境）
    qc = QuantumCircuit(3, 3)

    # ── 制备阶段 ──
    # Bell态 |Φ+⟩_{RQ}
    qc.h(0)           # R
    qc.cx(0, 1)       # R→Q

    # 环境初态 |γ⟩ = √p|+⟩ + √(1-p)|−⟩
    phi = 2 * np.arccos(np.sqrt(p))
    qc.ry(phi, 2)     # E

    qc.barrier()

    # ── 第一个RZZ门 ──
    if functional:
        qc.append(RZZGate(theta1), [1, 2])   # Q-E，角度θ₁
    # 死环：跳过第一个门（identity）

    # ── 时序间隔（等待） ──
    qc.delay(IDLE_TIME_NS, 1, unit='ns')
    qc.delay(IDLE_TIME_NS, 2, unit='ns')

    # ── 第二个RZZ门 ──
    qc.append(RZZGate(theta), [1, 2])        # Q-E，角度θ₂

    qc.barrier()

    # ── 测量阶段 ──
    if basis == 'X':
        qc.h(0); qc.h(1); qc.h(2)
    elif basis == 'Y':
        qc.sdg(0); qc.h(0)   # Sdg+H rotates Y→Z
        qc.sdg(1); qc.h(1)
        qc.sdg(2); qc.h(2)

    qc.measure([0, 1, 2], [0, 1, 2])

    return qc

# ============================================
# QCMI计算
# ============================================
def compute_mutual_info(counts_dict, n_shots):
    """从计数数据计算 I(R;Q)"""
    # 边际分布
    p_RQ = {}
    p_R = {}
    p_Q = {}

    for bitstring, count in counts_dict.items():
        # bitstring格式：'RQE'（低位=R）
        r = int(bitstring[2])   # R是最高位
        q = int(bitstring[1])   # Q是中间位
        e = int(bitstring[0])   # E是最低位

        rq = (r, q)
        p_RQ[rq] = p_RQ.get(rq, 0) + count
        p_R[r] = p_R.get(r, 0) + count
        p_Q[q] = p_Q.get(q, 0) + count

    # 归一化
    for k in p_RQ: p_RQ[k] /= n_shots
    for k in p_R:  p_R[k]  /= n_shots
    for k in p_Q:  p_Q[k]  /= n_shots

    def h(p_dict):
        return -sum(v * np.log2(v) for v in p_dict.values() if v > 1e-12)

    H_R  = h(p_R)
    H_Q  = h(p_Q)
    H_RQ = h(p_RQ)

    return H_R + H_Q - H_RQ   # I(R;Q)

def compute_qcmi_from_irq(irq):
    """QCMI = 4 - I(R;Q') 基于恒等式"""
    # 注意：这里用的是近似关系
    # 完整QCMI需要三方密度矩阵
    # 但差分 ΔQCMI = I(R;Q')_dead - I(R;Q')_functional
    # 可以从两个电路的差直接得到
    return irq

# ============================================
# 主实验
# ============================================
def run_experiment(token, dry_run=False):
    """
    提交实验到IBM Q队列

    dry_run=True: 只打印电路，不提交
    """
    print("CFOL定理实验验证")
    print("=" * 55)
    print(f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"θ值：{[f'π/{int(np.pi/t)}' for t in THETAS]}")
    print(f"环境纯度：p = {P_ENV}")
    print(f"Shots：{SHOTS:,}")
    print()

    # 构造所有电路
    circuits = []
    labels = []

    for theta in THETAS:
        theta_str = f"pi_{int(np.pi/theta)}"

        # 功能环（Z基）
        qc = make_cfol_circuit(theta, functional=True, basis='Z')
        qc.name = f"functional_Z_{theta_str}"
        circuits.append(qc)
        labels.append(('functional', 'Z', theta))

        # 死环（Z基）
        qc = make_cfol_circuit(theta, functional=False, basis='Z')
        qc.name = f"dead_Z_{theta_str}"
        circuits.append(qc)
        labels.append(('dead', 'Z', theta))

        # 功能环（Y基）
        qc = make_cfol_circuit(theta, functional=True, basis='Y')
        qc.name = f"functional_Y_{theta_str}"
        circuits.append(qc)
        labels.append(('functional', 'Y', theta))

        # 死环（Y基）
        qc = make_cfol_circuit(theta, functional=False, basis='Y')
        qc.name = f"dead_Y_{theta_str}"
        circuits.append(qc)
        labels.append(('dead', 'Y', theta))

    print(f"Total circuits: {len(circuits)}")
    print(f"  = {len(THETAS)} theta x 2 (functional/dead) x 2 (Z/Y basis)")
    print()

    if dry_run:
        print("[DRY RUN] 电路构造完成，未提交")
        print()
        print("示例电路（θ=π/4，功能环，Z基）：")
        print(circuits[0])
        return None

    # 连接IBM Q
    print("连接IBM Q...")
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

    service = QiskitRuntimeService(token=token)

    # 选择后端：优先选响应快的
    # 时序环只需要2个相邻qubit，任何IBM处理器都可以
    try:
        backend = service.backend(BACKEND_NAME)
        print(f"使用后端：{backend.name}")
    except Exception:
        # 备选：找最短队列的处理器
        backends = service.backends(
            operational=True,
            simulator=False,
            min_num_qubits=5
        )
        # 按队列长度排序
        backend = min(backends,
                     key=lambda b: b.status().pending_jobs)
        print(f"备选后端：{backend.name}")
        print(f"当前队列：{backend.status().pending_jobs} jobs")

    print()

    # 编译电路
    print("编译电路...")
    pm = generate_preset_pass_manager(
        optimization_level=1,
        backend=backend
    )
    isa_circuits = pm.run(circuits)
    print(f"编译完成，最大电路深度：{max(c.depth() for c in isa_circuits)}")
    print()

    # 提交 (open plan不支持Session，直接用Sampler)
    print("提交到队列...")
    sampler = Sampler(mode=backend)
    job = sampler.run(isa_circuits, shots=SHOTS)

    job_id = job.job_id()
    print(f"Job ID: {job_id}")
    print(f"状态: {job.status()}")
    print()
    print("保存Job ID到 cfol_job_id.txt...")

    with open("cfol_job_id.txt", "w") as f:
        f.write(json.dumps({
            "job_id": job_id,
            "backend": backend.name,
            "thetas": [float(t) for t in THETAS],
            "p_env": P_ENV,
            "shots": SHOTS,
            "labels": [(a, b, float(c)) for a, b, c in labels],
            "timestamp": datetime.now().isoformat()
        }, indent=2))

    print("完成。用以下命令查看结果:")
    print(f"  python cfol_ibm_experiment.py --token TOKEN --retrieve {job_id}")

    return job_id

# ============================================
# 结果分析
# ============================================
def retrieve_and_analyze(token, job_id):
    """从Job ID读取结果并分析"""
    from qiskit_ibm_runtime import QiskitRuntimeService

    print(f"读取结果：{job_id}")
    service = QiskitRuntimeService(token=token)
    job = service.job(job_id)

    if job.status().name != 'DONE':
        print(f"Job状态：{job.status().name}，还未完成")
        return

    result = job.result()

    # 读取之前保存的标签
    with open("cfol_job_id.txt") as f:
        meta = json.load(f)
    labels = meta['labels']
    thetas = meta['thetas']

    # 分析每个θ值
    print()
    print("=" * 55)
    print("实验结果")
    print("=" * 55)
    print(f"{'θ':>8} {'ΔI(R;Q) Z':>12} {'ΔI(R;Q) X':>12} {'Bell保真度':>12}")
    print("-" * 50)

    results_by_theta = {}

    for i, (ring_type, basis, theta) in enumerate(labels):
        pub_result = result[i]
        counts = pub_result.data.c.get_counts()
        irq = compute_mutual_info(counts, meta['shots'])

        key = (theta, basis)
        if key not in results_by_theta:
            results_by_theta[key] = {}
        results_by_theta[key][ring_type] = irq

    # 计算差分信号
    for theta in thetas:
        delta_Z = (results_by_theta[(theta, 'Z')].get('dead', 0) -
                   results_by_theta[(theta, 'Z')].get('functional', 0))
        delta_X = (results_by_theta[(theta, 'X')].get('dead', 0) -
                   results_by_theta[(theta, 'X')].get('functional', 0))

        # Bell保真度：理想情况I(R;Q)初始=2，实际值
        bell_fidelity = results_by_theta[(theta, 'Z')].get('dead', 0) / 2.0

        theta_str = f"π/{int(np.pi/theta)}"
        print(f"{theta_str:>8} {delta_Z:>12.4f} {delta_X:>12.4f} {bell_fidelity:>12.4f}")

    print()

    # 理论预测对比
    print("理论预测（θ²ln(1/θ)标度律）：")
    print(f"{'θ':>8} {'QCMI理论':>12} {'θ⁴预测':>12} {'增强因子':>12}")
    print("-" * 50)
    for theta in thetas:
        qcmi_theory = (4*theta**2/np.log(2)) * (1 + np.log(1/(4*theta**2)))
        qcmi_t4 = theta**4 * 16 / np.log(2)
        enhancement = qcmi_theory / qcmi_t4 if qcmi_t4 > 0 else float('inf')
        theta_str = f"π/{int(np.pi/theta)}"
        print(f"{theta_str:>8} {qcmi_theory:>12.4f} {qcmi_t4:>12.4f} {enhancement:>12.1f}×")

    # 保存结果
    output_file = f"cfol_results_{job_id[:8]}.json"
    with open(output_file, "w") as f:
        json.dump({
            "job_id": job_id,
            "results_by_theta": {
                str(k): v for k, v in results_by_theta.items()
            }
        }, f, indent=2)
    print(f"\n结果已保存：{output_file}")

# ============================================
# 命令行接口
# ============================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CFOL定理IBM Q实验"
    )
    parser.add_argument("--token", required=True,
                       help="IBM Q API token")
    parser.add_argument("--dry-run", action="store_true",
                       help="只构造电路，不提交")
    parser.add_argument("--retrieve", type=str, default=None,
                       help="从Job ID读取结果")
    args = parser.parse_args()

    if args.retrieve:
        retrieve_and_analyze(args.token, args.retrieve)
    else:
        run_experiment(args.token, dry_run=args.dry_run)
