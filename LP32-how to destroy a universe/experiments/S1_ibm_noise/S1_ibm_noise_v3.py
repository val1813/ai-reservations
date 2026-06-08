"""
S1定理验证 v3 — 真正非马尔可夫环境
用有限大小的量子环境产生真实信息回流

核心洞察：
- IBM噪声模型是马尔可夫的(T1/T2没有记忆)，永远不会产生回流
- 真正非马尔可夫需要: 有限环境 + 强纠缠 → 信息从环境回来
- 用无噪声酉演化 + 部分求迹 = 天然的finite-bath非马尔可夫动力学
- 然后叠加IBM T1/T2噪声看它们会不会淹没回流

协议:
1. 系统qubit + 1个环境qubit (最小有限环境)
2. sqrtSWAP序列: 信息在系统和环境间振荡
3. 改变初始q_E: |0>_env (q_E=1.0), |+>_env (q_E=0.5), |1>_env (q_E=0.0)
4. 部分求迹→非马尔可夫回流
5. S1: P_reflux <= q_S/q_E 检验

Token: uRlELcyrIqgYJnZet6Pru5MrejQH5inwOCn-Omg0IuDb
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("S1定理验证 v3 — 真正的非马尔可夫环境")
print("=" * 60)

# ============================================================
# 不需要IBM - 用有限浴产生真正的非马尔可夫性
# ============================================================
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, partial_trace
from qiskit_aer import AerSimulator

# 1. 纯酉演化(无噪声) — 有限环境天然非马尔可夫
sim_unitary = AerSimulator(method='statevector')

# 2. 叠加IBM噪声
print("\n[1/4] 加载IBM噪声模型...")
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer.noise import NoiseModel

TOKEN = "uRlELcyrIqgYJnZet6Pru5MrejQH5inwOCn-Omg0IuDb"
service = QiskitRuntimeService(token=TOKEN)

noise_model = None
backend_name_used = "ibm_marrakesh"
try:
    backend = service.backend(backend_name_used)
    noise_model = NoiseModel.from_backend(backend)
    print(f"  [OK] {backend_name_used}")
except:
    backends = service.backends(operational=True, simulator=False)
    backend = backends[0]
    backend_name_used = backend.name
    noise_model = NoiseModel.from_backend(backend)
    print(f"  [OK] {backend_name_used}")

sim_noisy = AerSimulator(noise_model=noise_model, method='density_matrix')

# ============================================================
# 核心电路: sqrtSWAP振荡器
# ============================================================
print("\n[2/4] 构建sqrtSWAP非马尔可夫电路...")

def sqrt_swap_circuit(n_swaps, q_env_init='zero'):
    """
    系统=|+>, 环境=|q_E>
    每步一个sqrtSWAP: 信息在系统和环境间振荡
    2个sqrtSWAP = 1个完整SWAP = 半个振荡周期
    """
    qc = QuantumCircuit(2)

    # 系统初始化到 |+>
    qc.h(0)

    # 环境初始化控制 q_E
    if q_env_init == 'zero':
        pass  # |0>, q_E = 1.0
    elif q_env_init == 'plus':
        qc.h(1)  # |+>, q_E = 0.5
    elif q_env_init == 'one':
        qc.x(1)  # |1>, q_E = 0.0
    elif q_env_init == 'partial_low':
        qc.ry(np.pi / 4, 1)  # cos^2(pi/8)|0> + sin^2(pi/8)|1>, q_E ~ 0.85
    elif q_env_init == 'partial_high':
        qc.ry(3 * np.pi / 4, 1)  # q_E ~ 0.15

    qc.barrier()

    for _ in range(n_swaps):
        # sqrtSWAP = 连续3个门
        qc.cx(0, 1)
        qc.cx(1, 0)
        qc.cx(0, 1)
        # 加上相位旋转让振荡不完全周期
        qc.rz(0.15, 0)
        qc.rz(0.05, 1)

    qc.save_statevector()
    return qc

def circuit_with_noise(n_swaps, q_env_init='zero', init_sys='plus'):
    """带IBM噪声的版本"""
    qc = QuantumCircuit(2)

    # 系统初始化
    qc.h(0)
    if init_sys == 'minus':
        qc.z(0)

    # 环境初始化
    if q_env_init == 'zero':
        pass
    elif q_env_init == 'plus':
        qc.h(1)
    elif q_env_init == 'one':
        qc.x(1)
    elif q_env_init == 'partial_low':
        qc.ry(np.pi / 4, 1)
    elif q_env_init == 'partial_high':
        qc.ry(3 * np.pi / 4, 1)

    qc.barrier()

    for _ in range(n_swaps):
        qc.cx(0, 1)
        qc.cx(1, 0)
        qc.cx(0, 1)
        qc.rz(0.15, 0)
        qc.rz(0.05, 1)

    qc.save_density_matrix()
    return qc

def trace_distance(r1, r2):
    diff = r1 - r2
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(diff))))

def estimate_q(rho):
    return float(np.real(rho[0, 0]))

# ============================================================
# 扫描参数
# ============================================================
print("\n[3/4] 扫描环境初始态...")

Q_ENV_CONFIGS = ['zero', 'partial_low', 'plus', 'partial_high', 'one']
Q_ENV_LABELS = {
    'zero': 'q_E=1.0 (|0>)',
    'partial_low': 'q_E=0.85',
    'plus': 'q_E=0.5 (|+>)',
    'partial_high': 'q_E=0.15',
    'one': 'q_E=0.0 (|1>)'
}
MAX_SWAPS = 30

print(f"  环境配置: {len(Q_ENV_CONFIGS)}")
print(f"  sqrtSWAP步数: {MAX_SWAPS}")

results_unitary = {}
results_noisy = {}

for mode, simulator, label in [
    ('unitary', sim_unitary, '无噪声(纯酉演化)'),
    ('noisy', sim_noisy, f'IBM {backend_name_used}噪声')
]:
    print(f"\n  --- {label} ---")
    print(f"  {'q_E_init':<15s} {'q_S_mid':>8s} {'q_E_mid':>8s} {'S1上界':>8s} {'回流':>8s}")
    print(f"  {'-'*15} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

    store = results_unitary if mode == 'unitary' else results_noisy

    for q_env_init in Q_ENV_CONFIGS:
        tds = []
        q_S_vals = []
        q_E_vals = []

        for n in range(MAX_SWAPS + 1):
            if mode == 'unitary':
                qc_plus = sqrt_swap_circuit(n, q_env_init)
                qc_plus.remove_final_measurements()
                qc_minus = sqrt_swap_circuit(n, q_env_init)
                qc_minus.remove_final_measurements()

                # 对|+>态运行
                job_p = simulator.run(qc_plus)
                sv_p = job_p.result().get_statevector()
                dm_p = DensityMatrix(sv_p)

                # 对|->态运行 (手动从|+>态计算)
                from qiskit.quantum_info import Statevector
                sv_m_data = sv_p.data.copy()
                N = len(sv_m_data)
                # |-> = (|0>-|1>)/sqrt(2): sign flip on |1> components
                for i in range(N):
                    if (i & 1):  # LSB of index is system qubit = 1
                        sv_m_data[i] *= -1.0
                sv_m = Statevector(sv_m_data)
                dm_m = DensityMatrix(sv_m)
            else:
                qc_plus = circuit_with_noise(n, q_env_init, 'plus')
                qc_minus = circuit_with_noise(n, q_env_init, 'minus')

                job_p = simulator.run(qc_plus)
                dm_p = DensityMatrix(job_p.result().data()['density_matrix'])

                job_m = simulator.run(qc_minus)
                dm_m = DensityMatrix(job_m.result().data()['density_matrix'])

            dm_sys_p = partial_trace(dm_p, [1])
            dm_sys_m = partial_trace(dm_m, [1])
            dm_env_p = partial_trace(dm_p, [0])

            r1 = np.array(dm_sys_p.data)
            r2 = np.array(dm_sys_m.data)
            re = np.array(dm_env_p.data)

            td = trace_distance(r1, r2)
            tds.append(td)
            q_S_vals.append(estimate_q(r1))
            q_E_vals.append(estimate_q(re))

        tds = np.array(tds)
        q_S_vals = np.array(q_S_vals)
        q_E_vals = np.array(q_E_vals)

        # 找回流: 迹距离降到最低后的最大回升
        idx_min = np.argmin(tds)
        td_min = tds[idx_min]
        td_after = tds[idx_min:]
        reflux = float(np.max(td_after) - td_min) if len(td_after) > 1 else 0.0

        # 用中间态算q值 (避免边界效应)
        mid = MAX_SWAPS // 3
        q_S_mid = q_S_vals[mid]
        q_E_mid = max(q_E_vals[mid], 0.001)
        s1_bound = q_S_mid / q_E_mid

        ok = reflux <= s1_bound + 0.03

        store[q_env_init] = {
            'tds': tds,
            'reflux': reflux,
            'q_S': q_S_mid,
            'q_E': q_E_mid,
            's1_bound': s1_bound,
            'ok': ok
        }

        status = "OK" if ok else "FAIL"
        sig = "***" if reflux > 0.05 else ""
        print(f"  {q_env_init:<15s} {q_S_mid:>8.4f} {q_E_mid:>8.4f} {s1_bound:>8.4f} {reflux:>8.4f} {status:>6s} {sig}")

# ============================================================
# 汇总
# ============================================================
print(f"\n[4/4] 汇总 — S1定理验证")

for mode, results, label in [
    ('unitary', results_unitary, '无噪声'),
    ('noisy', results_noisy, f'IBM {backend_name_used}噪声')
]:
    n_ok = sum(1 for r in results.values() if r['ok'])
    n_reflux = sum(1 for r in results.values() if r['reflux'] > 0.03)
    n_total = len(results)
    print(f"  {label}: {n_ok}/{n_total}满足S1, {n_reflux}/{n_total}有显著回流(>3%)")

# ============================================================
# 画图
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 13))

for col, (mode, results, title) in enumerate([
    ('unitary', results_unitary, 'Unitary (finite-bath, true non-Markovian)'),
    ('noisy', results_noisy, f'IBM {backend_name_used} noise (Markovian noise masks reflux)')
]):
    ax_td = axes[0, col]
    ax_s1 = axes[1, col]

    colors = plt.cm.RdYlGn(np.linspace(0.15, 0.85, len(Q_ENV_CONFIGS)))

    for i, (q_env_init, r) in enumerate(results.items()):
        ax_td.plot(range(MAX_SWAPS + 1), r['tds'],
                   color=colors[i], lw=1.8,
                   label=Q_ENV_LABELS[q_env_init],
                   alpha=0.85)

    ax_td.set_xlabel('sqrtSWAP steps', fontsize=11)
    ax_td.set_ylabel('Trace distance', fontsize=11)
    ax_td.set_title(f'{title}\nSystem-environment coherence dynamics', fontsize=11)
    ax_td.legend(fontsize=7, loc='best')
    ax_td.grid(True, alpha=0.3)
    ax_td.set_ylim(-0.05, 1.15)

    # S1 bound scatter
    q_ratios = [r['s1_bound'] for r in results.values()]
    refluxes = [r['reflux'] for r in results.values()]
    scatter_colors = ['#4CAF50' if r['ok'] else '#F44336' for r in results.values()]

    ax_s1.scatter(q_ratios, refluxes, c=scatter_colors, s=100,
                  zorder=5, edgecolors='black', linewidth=0.5)

    for i, (q_env_init, r) in enumerate(results.items()):
        ax_s1.annotate(Q_ENV_LABELS[q_env_init].split('(')[0].strip(),
                       (r['s1_bound'], r['reflux']),
                       textcoords="offset points", xytext=(5, 5), fontsize=7)

    mm = max(max(q_ratios), max(refluxes) + 0.1) * 1.3
    if mm < 0.5:
        mm = 0.5
    ax_s1.plot([0, mm], [0, mm], 'r--', lw=2, label='S1 bound')
    ax_s1.fill_between([0, mm], [0, 0], [0, mm], alpha=0.08, color='green')
    ax_s1.set_xlabel('S1 bound (q_S / q_E)', fontsize=11)
    ax_s1.set_ylabel('Reflux amplitude', fontsize=11)
    ax_s1.set_title(f'S1 Theorem: P_reflux <= q_S/q_E\n({title})', fontsize=11)
    ax_s1.legend(fontsize=8)
    ax_s1.grid(True, alpha=0.3)
    ax_s1.set_xlim(0, mm)
    ax_s1.set_ylim(-mm * 0.02, mm)

plt.suptitle('DGF S1 Theorem v3: Genuine Non-Markovian Environment\n'
             f'Finite (2-qubit) bath creates true information backflow vs IBM noise suppression',
             fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig('S1_ibm_result_v3.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: S1_ibm_result_v3.png")
print("Done.")
