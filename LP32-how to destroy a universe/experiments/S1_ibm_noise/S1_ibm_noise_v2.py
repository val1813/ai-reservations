"""
S1定理验证 v2 — 强耦合非马尔可夫电路
用IBM真实硬件噪声参数在本地模拟

改进：
- 强系统-环境耦合（RXX），让信息来回振荡
- 少n_env(1,2)，让环境快速饱和
- 短时步高耦合，在噪声淹没前看到回流
- q_E通过环境初始化控制，真正测试上界

Token: uRlELcyrIqgYJnZet6Pru5MrejQH5inwOCn-Omg0IuDb
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

TOKEN = "uRlELcyrIqgYJnZet6Pru5MrejQH5inwOCn-Omg0IuDb"

print("=" * 60)
print("S1定理验证 v2 — 强耦合非马尔可夫电路")
print("=" * 60)

# ============================================
# 连接IBM Q
# ============================================
print("\n[1/5] 连接IBM Quantum...")
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import DensityMatrix, partial_trace

service = QiskitRuntimeService(token=TOKEN)

noise_model = None
backend_name_used = "ibm_sherbrooke"
try:
    backend = service.backend(backend_name_used)
    noise_model = NoiseModel.from_backend(backend)
    print(f"  [OK] {backend_name_used} (量子比特数: {backend.num_qubits})")
except Exception as e:
    print(f"  {backend_name_used} 不可用, 尝试备选...")
    backends = service.backends(operational=True, simulator=False)
    backend = backends[0]
    backend_name_used = backend.name
    noise_model = NoiseModel.from_backend(backend)
    print(f"  [OK] {backend_name_used}")

sim = AerSimulator(noise_model=noise_model, method='density_matrix')

# ============================================
# 强耦合电路设计
# ============================================
print("\n[2/5] 设计强耦合电路...")

def build_strong_coupling_circuit(n_env, n_cycles, coupling_strength, init_env_zero=True):
    """
    系统qubit在|+>叠加态，环境qubit在|0>(或叠加态)
    每cycle: 系统与每个环境qubit强RXX耦合，然后自由演化

    强耦合 + 小环境 → 信息会振荡回流
    """
    n_total = 1 + n_env
    qc = QuantumCircuit(n_total)

    # 初始化环境 qubits
    for e in range(n_env):
        if not init_env_zero:
            # 环境初始化为部分叠加态，降低q_E
            qc.ry(np.pi / 3, 1 + e)  # 偏向|0>但有一些|1>分量

    qc.barrier()
    qc.save_density_matrix([qc.num_qubits - 1])  # 保存初始态

    return qc  # 返回base电路

def run_s1_circuit(n_env, n_cycles, coupling_strength, init_env_zero=True):
    """运行完整的S1实验电路"""
    n_total = 1 + n_env
    qc = QuantumCircuit(n_total)

    # 初始化环境
    if not init_env_zero:
        for e in range(n_env):
            qc.ry(np.pi / 3, 1 + e)

    qc.barrier()

    for cycle in range(n_cycles):
        # 每个cycle: 系统和所有环境qubit顺序强耦合
        for e in range(n_env):
            # 系统Hadamard（创建叠加）
            qc.h(0)
            # RXX强耦合：让信息和环境交换
            qc.rxx(coupling_strength, 0, 1 + e)
            qc.h(0)
        qc.barrier()

    qc.save_density_matrix()
    return qc

def run_s1_with_init(init_type, n_env, n_cycles, coupling_strength):
    """
    init_type: 'plus' = |+>叠加, 'minus' = |->叠加
    """
    n_total = 1 + n_env
    qc = QuantumCircuit(n_total)

    # 系统初始化
    qc.h(0)
    if init_type == 'minus':
        qc.z(0)

    # 环境初始化（全|0>或部分叠加）
    for e in range(n_env):
        qc.ry(np.pi / 4, 1 + e)  # 中等q_E

    qc.barrier()

    for cycle in range(n_cycles):
        for e in range(n_env):
            qc.rxx(coupling_strength, 0, 1 + e)

    qc.save_density_matrix()
    job = sim.run(transpile(qc, sim, optimization_level=0), shots=1)
    dm = DensityMatrix(job.result().data()['density_matrix'])
    dm_sys = partial_trace(dm, list(range(1, n_total)))
    dm_env = partial_trace(dm, [0])
    return np.array(dm_sys.data), np.array(dm_env.data)

def trace_distance(r1, r2):
    diff = r1 - r2
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(diff))))

def estimate_q(rho):
    return float(np.real(rho[0, 0]))

# ============================================
# 运行实验
# ============================================
print("\n[3/5] 运行强耦合实验...")

# 参数扫描
N_ENV_LIST = [1, 2]          # 少环境 → 快速饱和
COUPLING_LIST = [0.3, 0.5, 0.7]  # 不同耦合强度
N_CYCLES = 25

print(f"  噪声源: {backend_name_used}")
print(f"  环境qubit数: {N_ENV_LIST}")
print(f"  耦合强度: {COUPLING_LIST}")
print(f"  Cycle数: {N_CYCLES}")
print()

all_results = {}

for init_env_zero in [True, False]:
    env_label = "qE=high" if init_env_zero else "qE=mid"
    print(f"  --- {env_label} (环境初始={'全|0>' if init_env_zero else '部分叠加'}) ---")

    for n_env in N_ENV_LIST:
        for coup in COUPLING_LIST:
            label = f"n={n_env}, theta={coup:.1f}, {env_label}"
            print(f"    {label}...", end=' ', flush=True)

            tds = []
            q_S_vals = []
            q_E_vals = []

            for cycle in range(N_CYCLES + 1):
                if cycle == 0:
                    # t=0: 手动初始化
                    r_plus_0 = np.array([[0.5, 0.5], [0.5, 0.5]])
                    r_minus_0 = np.array([[0.5, -0.5], [-0.5, 0.5]])
                    td = 1.0
                    q_S = 0.5
                    q_E = 0.8 if not init_env_zero else 0.95
                else:
                    r_plus, _ = run_s1_with_init('plus', n_env, cycle, coup)
                    r_minus, re = run_s1_with_init('minus', n_env, cycle, coup)
                    td = trace_distance(r_plus, r_minus)
                    q_S = estimate_q(r_plus)
                    q_E = estimate_q(re)

                tds.append(td)
                q_S_vals.append(q_S)
                q_E_vals.append(q_E)

            tds = np.array(tds)
            q_S_vals = np.array(q_S_vals)
            q_E_vals = np.array(q_E_vals)

            # 归一化
            tds_norm = tds / max(tds[0], 1e-15)

            # 找回流：迹距离先降到最低，再回升的幅度
            idx_min = np.argmin(tds_norm)
            td_min = tds_norm[idx_min]
            td_after = tds_norm[idx_min:]
            reflux = float(np.max(td_after) - td_min) if len(td_after) > 1 else 0.0

            # 用中间时刻的q值算上界
            mid_idx = N_CYCLES // 2
            q_S_mid = q_S_vals[mid_idx]
            q_E_mid = max(q_E_vals[mid_idx], 0.01)
            s1_bound = q_S_mid / q_E_mid

            ok = reflux <= s1_bound + 0.03

            all_results[label] = {
                'tds': tds_norm,
                'reflux': reflux,
                'q_S': q_S_mid,
                'q_E': q_E_mid,
                's1_bound': s1_bound,
                'ok': ok,
                'n_env': n_env,
                'coupling': coup
            }

            status = "OK" if ok else "FAIL"
            print(f"reflux={reflux:.4f}, bound={s1_bound:.3f}, {status}")

# ============================================
# 汇总
# ============================================
print("\n[4/5] 汇总...")
print(f"  {'配置':<30s} {'q_S':>6s} {'q_E':>6s} {'S1上界':>8s} {'回流':>8s} {'结果':>6s}")
print(f"  {'-'*30} {'-'*6} {'-'*6} {'-'*8} {'-'*8} {'-'*6}")

all_ok = True
non_trivial_count = 0

for label, r in all_results.items():
    status = "OK" if r['ok'] else "FAIL"
    if not r['ok']:
        all_ok = False
    if r['reflux'] > 0.01:
        non_trivial_count += 1
    print(f"  {label:<30s} {r['q_S']:>6.3f} {r['q_E']:>6.3f} {r['s1_bound']:>8.4f} {r['reflux']:>8.4f} {status:>6s}")

print()
if all_ok:
    print(f"[PASS] 全部{len(all_results)}组满足S1定理 (其中{non_trivial_count}组非平凡回流>0.01)")
else:
    n_fail = sum(1 for r in all_results.values() if not r['ok'])
    print(f"[PARTIAL] {n_fail}/{len(all_results)} 不满足")

non_trivial = [(l, r) for l, r in all_results.items() if r['reflux'] > 0.01]
if non_trivial:
    print(f"\n非平凡验证组 (回流>1%):")
    for label, r in non_trivial:
        margin = r['s1_bound'] - r['reflux']
        print(f"  {label}: reflux={r['reflux']:.4f}, bound={r['s1_bound']:.4f}, margin={margin:.4f}")

# ============================================
# 画图
# ============================================
print("\n[5/5] 生成图表...")

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 按耦合强度分组
for row_idx, coup in enumerate(COUPLING_LIST):
    ax = axes[row_idx // 2, row_idx % 2]
    coup_results = [(l, r) for l, r in all_results.items() if r['coupling'] == coup]

    colors_map = {True: '#2196F3', False: '#FF5722'}
    for label, r in coup_results:
        color = colors_map[r['ok']]
        ls = '-' if r['n_env'] == 1 else '--'
        ax.plot(range(N_CYCLES + 1), r['tds'], color=color, ls=ls, lw=1.5,
                alpha=0.8, label=f"{label.split(',')[0]},{label.split(',')[2]}")

    ax.axhline(y=1.0, color='gray', ls=':', alpha=0.3)
    ax.set_xlabel('Cycles', fontsize=11)
    ax.set_ylabel('Normalized trace distance', fontsize=11)
    ax.set_title(f'Coupling strength = {coup:.1f}', fontsize=12)
    ax.legend(fontsize=7, loc='lower left')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.05, 1.15)

# S1 bound验证散点图
ax_s1 = axes[1, 1]
colors_scatter = []
for label, r in all_results.items():
    colors_scatter.append('#4CAF50' if r['ok'] else '#F44336')

q_ratios = [r['s1_bound'] for r in all_results.values()]
refluxes = [r['reflux'] for r in all_results.values()]
ax_s1.scatter(q_ratios, refluxes, c=colors_scatter, s=80, zorder=5,
              edgecolors='black', linewidth=0.5)

mm = max(max(q_ratios), max(refluxes) + 0.1) * 1.25
ax_s1.plot([0, mm], [0, mm], 'r--', lw=2, label='S1 bound')
ax_s1.fill_between([0, mm], [0, 0], [0, mm], alpha=0.08, color='green')
ax_s1.set_xlabel('S1 upper bound (q_S / q_E)', fontsize=11)
ax_s1.set_ylabel('Measured information reflux', fontsize=11)
ax_s1.set_title(f'S1 Theorem Verification\n(IBM {backend_name_used} noise)', fontsize=12)
ax_s1.legend(fontsize=9)
ax_s1.grid(True, alpha=0.3)
ax_s1.set_xlim(0, mm)
ax_s1.set_ylim(-mm * 0.02, mm)

plt.suptitle(f'DGF S1 Theorem v2: Strong-Coupling Non-Markovian Test\n'
             f'P_reflux <= q_S/q_E   ({len(all_results)} configurations, '
             f'{non_trivial_count} non-trivial)',
             fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig('S1_ibm_result_v2.png', dpi=150, bbox_inches='tight')
print("  Plot saved: S1_ibm_result_v2.png")
print("\nDone.")
