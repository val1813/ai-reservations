"""
S1定理验证 — IBM真实硬件噪声参数
原理：用IBM硬件校准参数(T1/T2/门错误)的噪声模型在本地模拟，
      验证P_reflux <= q_S/q_E

S1定理: P_reflux <= q_S/q_E
  q_S = 系统细胞空置率 = Tr[rho_sys |0><0|]
  q_E = 环境细胞空置率 = Tr[rho_env |0><0|]
  P_reflux = 迹距离回升幅度 (非马尔可夫回流)

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
print("S1定理验证 — IBM Q真实噪声参数")
print("=" * 60)

# ============================================
# 连接IBM Q
# ============================================
print("\n[1/4] 连接IBM Quantum...")
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import DensityMatrix, partial_trace

service = QiskitRuntimeService(token=TOKEN)

# 选真实后端
backend_name = "ibm_sherbrooke"
noise_model = None
backend_name_used = backend_name
try:
    backend = service.backend(backend_name)
    noise_model = NoiseModel.from_backend(backend)
    print(f"  [OK] 读取 {backend_name} 噪声参数")
    print(f"  量子比特数: {backend.num_qubits}")
except Exception as e:
    print(f"  {backend_name} 不可用: {e}")
    backends = service.backends(operational=True, simulator=False)
    if len(backends) > 0:
        backend = backends[0]
        backend_name_used = backend.name
        noise_model = NoiseModel.from_backend(backend)
        print(f"  [OK] 使用 {backend.name}")
    else:
        print("  [FAIL] 无可用后端，使用理想模拟器")
        noise_model = None
        backend_name_used = "ideal"

sim = AerSimulator(noise_model=noise_model, method='density_matrix')
print(f"  噪声模型: {'启用' if noise_model else '无(理想)'}")

# ============================================
# 实验设计
# ============================================
print("\n[2/4] 设计实验电路...")

def run_s1_experiment(n_env, t_steps, init='plus'):
    """
    系统qubit在叠加态, 与环境qubit耦合演化t_steps步
    返回系统约化密度矩阵
    """
    n_total = 1 + n_env
    qc = QuantumCircuit(n_total)

    # 初始化到叠加态
    qc.h(0)
    if init == 'minus':
        qc.z(0)  # |+> -> |->

    # 时步演化: 系统和每个环境qubit依次弱耦合
    for step in range(t_steps):
        e_idx = step % n_env
        # 弱CPhase: 不完全纠缠, 让信息逐渐流入环境
        theta = 0.05 * (1.0 + 0.5 * np.sin(step * 0.7))
        qc.cp(theta, 0, 1 + e_idx)

    qc.save_density_matrix()

    job = sim.run(transpile(qc, sim, optimization_level=0), shots=1)
    dm = DensityMatrix(job.result().data()['density_matrix'])
    dm_sys = partial_trace(dm, list(range(1, n_total)))
    dm_env = partial_trace(dm, [0])
    return np.array(dm_sys.data), np.array(dm_env.data)

def trace_distance(r1, r2):
    """BLP度量: 1/2 * ||rho1 - rho2||_1"""
    diff = r1 - r2
    return 0.5 * np.sum(np.abs(np.linalg.eigvalsh(diff)))

def estimate_q(rho):
    """
    q = 细胞空置率 = probability of |0> state
    对混合态: q = <0|rho|0>
    """
    return float(np.real(rho[0, 0]))

# ============================================
# 主实验
# ============================================
print("\n[3/4] 运行实验...")
print(f"  {'N_env':>6s}  {'q_S':>8s}  {'q_E':>8s}  {'S1上界':>8s}  {'回流':>8s}  {'满足?':>6s}")
print(f"  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*6}")

N_ENV_LIST = [1, 2, 3, 4, 5, 6]
T_MAX = 20
results = {}

for n_env in N_ENV_LIST:
    tds = []

    # 对每个时步计算迹距离
    for t in range(T_MAX + 1):
        r_plus, _ = run_s1_experiment(n_env, t, 'plus')
        r_minus, _ = run_s1_experiment(n_env, t, 'minus')
        td = trace_distance(r_plus, r_minus)
        tds.append(td)

    tds = np.array(tds)
    tds_norm = tds / (tds[0] + 1e-15)

    # 找最大退相干(最小迹距离)后的回流幅值
    idx_min = np.argmin(tds_norm)
    td_min = tds_norm[idx_min]
    td_after = tds_norm[idx_min:]
    reflux = float(np.max(td_after) - td_min) if len(td_after) > 1 else 0.0

    # q_S: 用中间时刻系统态对|0>的投影
    rho_sys_mid, rho_env_mid = run_s1_experiment(n_env, T_MAX // 2, 'plus')
    q_S = estimate_q(rho_sys_mid)
    q_E = estimate_q(rho_env_mid)

    # S1上界
    s1_bound = q_S / max(q_E, 0.01)

    ok = reflux <= s1_bound + 0.03
    results[n_env] = {
        'tds': tds_norm,
        'reflux': reflux,
        'q_S': q_S,
        'q_E': q_E,
        's1_bound': s1_bound,
        'ok': ok
    }

    status = "OK" if ok else "FAIL"
    print(f"  {n_env:>6d}  {q_S:>8.3f}  {q_E:>8.3f}  {s1_bound:>8.3f}  {reflux:>8.3f}  {status:>6s}")

# ============================================
# 汇总
# ============================================
print(f"\n[4/4] 结果汇总 (噪声模型: {backend_name_used})")
print("-" * 60)

all_ok = all(r['ok'] for r in results.values())
if all_ok:
    print("[PASS] 所有n_env满足 S1定理: P_reflux <= q_S/q_E")
else:
    n_fail = sum(1 for r in results.values() if not r['ok'])
    print(f"[PARTIAL] {n_fail}/{len(results)} 不满足, 需检查")

print(f"\nS1上界验证完成。")
print(f"噪声源: {backend_name_used}")
print(f"结论: DGF S1定理{'通过' if all_ok else '部分通过'}噪声模型检验")

# ============================================
# 画图
# ============================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(N_ENV_LIST)))

for i, (n_env, r) in enumerate(results.items()):
    ax1.plot(range(T_MAX + 1), r['tds'],
             color=colors[i], marker='.', ms=3,
             label=f'n_env={n_env}', alpha=0.85)
ax1.set_xlabel('Time step', fontsize=12)
ax1.set_ylabel('Normalized trace distance', fontsize=12)
ax1.set_title(f'Quantum Coherence Decay\n(noise model: {backend_name_used})', fontsize=11)
ax1.legend(loc='lower left', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-0.05, 1.15)

q_ratios = [r['s1_bound'] for r in results.values()]
refluxes = [r['reflux'] for r in results.values()]

ax2.scatter(q_ratios, refluxes, c=colors, s=120, zorder=5, edgecolors='black', linewidth=0.5)
for n_env, qr, rf in zip(results.keys(), q_ratios, refluxes):
    ax2.annotate(f'{n_env}', (qr, rf),
                textcoords="offset points", xytext=(8, 5), fontsize=9)

mm = max(max(q_ratios), max(refluxes)) * 1.3
ax2.plot([0, mm], [0, mm], 'r--', lw=2, label='S1 bound (slope=1)')
ax2.fill_between([0, mm], [0, 0], [0, mm], alpha=0.08, color='green', label='Allowed region')
ax2.set_xlabel('S1 upper bound (q_S / q_E)', fontsize=12)
ax2.set_ylabel('Measured information reflux', fontsize=12)
ax2.set_title('S1 Theorem Verification', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, mm)
ax2.set_ylim(0, mm)

plt.suptitle(f'DGF S1 Theorem: P_reflux <= q_S/q_E\n(IBM {backend_name_used} noise model)', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig('S1_ibm_result.png', dpi=150, bbox_inches='tight')
print("Plot saved: S1_ibm_result.png")
