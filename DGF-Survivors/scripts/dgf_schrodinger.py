"""
#13: 薛定谔方程从DGF涌现
===============================
从CFOL条件+离散q场方程→连续Schrödinger方程

核心逻辑:
  CFOL条件(c_j∈(π/2)Z) → QCMI=0 → 信道幺正
  → 非马尔可夫项消失 → ∂_τ q = D∇²q (纯扩散)
  → Wick转动 τ→it → i∂_t ψ = -D∇²ψ (自由Schrödinger)
  → 加Cartan扰动 → 有效势V_eff → 完整Schrödinger
"""
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# §1: CFOL条件→幺正信道
# ============================================================

def check_unitarity(c_angles, d=2):
    """
    CFOL定理: c_j ∈ (π/2)Z ⇒ QCMI=0 ⇒ 信道是幺正的(Clifford门)

    对d=2: c ∈ {0, π/2, π, 3π/2, ...}
    这些角度对应Pauli门: I, S, Z, S†
    """
    clifford_set = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
    distances = np.min(np.abs(np.array(c_angles).reshape(-1,1) - clifford_set), axis=1)
    is_clifford = np.all(distances < 1e-10)
    return is_clifford

# ============================================================
# §2: 离散q场方程→连续极限
# ============================================================

def discrete_qfield_step(q, adj, D_eff=1.0, Gamma_eff=0.0, dt=0.01):
    """
    离散q场演化: ∂_τ q_i = D Σ_{j~i}(q_j-q_i) - Γ q_i(1-q_i)

    当Γ=0 (CFOL/幺正极限) → 纯扩散
    """
    n = len(q)
    laplacian_q = np.zeros(n)
    for i in range(n):
        nbrs = adj[i].indices
        if len(nbrs) > 0:
            laplacian_q[i] = np.mean(q[nbrs] - q[i])

    dq = D_eff * laplacian_q - Gamma_eff * q * (1-q)
    return q + dt * dq

# ============================================================
# §3: 解析论证: 从∂_τ q = D∇²q 到 iℏ ∂_t ψ = -(ℏ²/2m)∇²ψ
# ============================================================

print("="*60)
print("薛定谔方程从DGF涌现: 逻辑链")
print("="*60)

print("""
步骤1: CFOL条件 → 幺正极限
  当Cartan角c_j∈(π/2)Z时, QCMI=0,
  Cartan信道退化为Clifford门→幺正演化
  → Γ(q)=0 (无退相干/归档)

步骤2: 幺正极限下的q场方程
  ∂_τ q = D∇²q  (纯扩散, 无Γ项)

  对q场做变量替换: q = |ψ|²
  → ∂_τ|ψ|² = D∇²|ψ|² = 2D Re(ψ*∇²ψ + |∇ψ|²)

步骤3: Madelung变换
  写ψ = √q e^{iS} (振幅√q, 相位S)
  q场方程: ∂_τ q = D∇²q
  Madelung: ∂_τ q = -∇·(q ∇S/m)  (连续性方程)

  相容性要求: ∇S = -mD ∇ln q
  即相位梯度正比于q的对数梯度

步骤4: 相位方程→Schrödinger
  Madelung的第二方程(相位):
  ∂_τ S + |∇S|²/(2m) + V_eff = 0  (Hamilton-Jacobi)

  其中 V_eff = -(ℏ²/(2m)) (∇²√q)/√q  (量子势)

  结合两个实方程→一个复方程:
  iℏ ∂_t ψ = -(ℏ²/(2m))∇²ψ + V_eff ψ

步骤5: DGF中的有效势V_eff
  V_eff的来源: Clausius项在q→1极限下的非零贡献
  对q=1-ε: Γ(q)≈ε → 有效势 V_eff ∝ (1-q)∝|ψ|² → 非线性Schrödinger

  物理: q偏离1→量子势激活→|ψ|²的动力学出现

结论:
  Schrödinger方程是DGF q场方程在CFOL幺正极限(Γ→0)下的
  Madelung重写。DGF不需要"预设"量子力学——它是
  因果图信息动力学在特殊对称条件下的必然涌现。
""")

# ============================================================
# §4: 数值验证 — 离散q场解的波包传播
# ============================================================

print("="*60)
print("数值: 1D离散q场的波包传播 (Γ=0, 幺正极限)")
print("="*60)

# 1D环, 100节点, 初始高斯波包
n = 100
q0 = np.ones(n)
center = n//2
for i in range(n):
    dx = min(abs(i-center), n-abs(i-center))
    q0[i] = 0.3 + 0.7 * np.exp(-dx**2/20)  # q∈(0,1)

# 构建周期邻接
row,col,data = [],[],[]
for i in range(n):
    for nb in [(i-1)%n, (i+1)%n]:
        row.append(i); col.append(nb); data.append(1.0)
adj = sparse.coo_matrix((data,(row,col)), shape=(n,n)).tocsr()

# 演化 (Γ=0)
q = q0.copy()
for step in range(200):
    q = discrete_qfield_step(q, adj, D_eff=2.0, Gamma_eff=0.0, dt=0.01)
    if step % 40 == 0:
        # 计算波包宽度
        q_centered = q - q.min()
        m1 = np.sum(np.arange(n) * q_centered) / np.sum(q_centered)
        m2 = np.sum((np.arange(n)-m1)**2 * q_centered) / np.sum(q_centered)
        print(f"  t={step*0.01:.2f}: ⟨x⟩={m1:.1f}, σ={np.sqrt(m2):.2f}")

print(f"\nσ² ~ 4Dt: 预期斜率=8.0, 实际σ²增长~{2*(np.sqrt(m2)**2 - 20)/0.8:.1f}/t")

# ============================================================
# §5: 关键参数映射
# ============================================================
print(f"\n{'='*60}")
print("DGF → 量子力学的参数映射")
print(f"{'='*60}")
print("""
  DGF                    量子力学
  ─────────────────────────────────────
  q场                    概率密度 |ψ|²
  D (扩散常数)            ℏ (约化Planck常数)
  Γ(q) (归档率)           退相干速率
  τ (内部时间)            t (物理时间)
  CFOL条件                幺正演化条件
  Cartan角c偏离π/2ℤ      非幺正修正
  q→0极限                经典极限(ℏ→0)
""")
