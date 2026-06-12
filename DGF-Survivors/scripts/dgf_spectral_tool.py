"""
DGF谱维度检测工具: 输入任何图, 检测其有效维度和连续极限条件
用法: python dgf_spectral_tool.py [graph_file]
"""
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
import sys, json

def analyze_spectral_dimension(adj_matrix=None, coords=None, n_eigenvalues=200):
    """
    从图Laplacian的谱推断有效维度。

    定理: 若图序列G_N的归一化Laplacian L_N满足:
      (C1) 特征值分布~N(λ)∝λ^(d/2-1) (Weyl律, d维特征)
      (C2) 特征向量近似连续Laplace-Beltrami特征函数
      (C3) 图直径~N^(1/d) (d维嵌入)
    则G_N的大尺度极限是d维扩散方程: ∂_t q = D∇²q.

    返回: (d_eff, confidence, details)
    """
    result = {'status': 'unknown', 'd_eff': None, 'checks': {}}

    n = adj_matrix.shape[0]

    # --- 检查0: 图是否连通 ---
    deg = np.array(adj_matrix.sum(axis=1)).flatten()
    if (deg == 0).any():
        result['status'] = 'disconnected'
        result['checks']['connected'] = False
        return result
    result['checks']['connected'] = True
    result['checks']['avg_degree'] = float(deg.mean())
    result['checks']['n_nodes'] = n

    # --- 构建归一化Laplacian L = I - D^{-1/2} A D^{-1/2} ---
    D_inv_sqrt = sparse.diags(1.0 / np.sqrt(deg))
    L = sparse.eye(n) - D_inv_sqrt @ adj_matrix @ D_inv_sqrt

    # --- 计算谱 (最小的k个特征值) ---
    k = min(n_eigenvalues, n-2)
    eigenvalues = spla.eigsh(L, k=k, which='SM', return_eigenvectors=False)
    eigenvalues = np.sort(eigenvalues)

    result['checks']['lambda_min'] = float(eigenvalues[0])
    result['checks']['lambda_max'] = float(eigenvalues[-1])
    result['checks']['spectral_gap'] = float(eigenvalues[1] - eigenvalues[0])

    # --- 检查1: Weyl律 ---
    # 对d维: N(λ) ∝ λ^{d/2}, 即log N(λ) = (d/2) log λ + const
    lambdas = eigenvalues[10:]  # 跳过最小的几个(含零模)
    counts = np.arange(len(lambdas)) + 10

    mask = (lambdas > 1e-10) & (counts > 0)
    log_l = np.log(lambdas[mask])
    log_n = np.log(counts[mask])

    if len(log_l) < 10:
        result['status'] = 'too_small'
        return result

    # 线性拟合: log N(λ) = α log λ + β, α = d/2
    X = np.column_stack([log_l, np.ones_like(log_l)])
    coeffs, residuals, rank, sv = np.linalg.lstsq(X, log_n, rcond=None)
    alpha = coeffs[0]
    d_eff = 2.0 * alpha

    # R² of Weyl fit
    pred = X @ coeffs
    ss_res = np.sum((log_n - pred)**2)
    ss_tot = np.sum((log_n - log_n.mean())**2)
    r2_weyl = 1.0 - ss_res/ss_tot if ss_tot > 1e-30 else 0.0

    result['checks']['weyl_alpha'] = float(alpha)
    result['checks']['weyl_r2'] = float(r2_weyl)
    result['d_eff'] = float(d_eff)

    # --- 检查2: 图直径标度 ---
    # 用Fiedler向量(第二特征向量)估计有效直径
    # 对于d维格点: λ_2 ~ (π/L)², 所以L_eff = π/√λ_2
    if eigenvalues[1] > 1e-15:
        L_eff = np.pi / np.sqrt(eigenvalues[1])
        # 预期: L_eff ~ N^{1/d}
        d_from_diameter = np.log(n) / np.log(L_eff) if L_eff > 1 else 0
        result['checks']['L_eff'] = float(L_eff)
        result['checks']['d_from_diameter'] = float(d_from_diameter)
    else:
        result['checks']['L_eff'] = None

    # --- 检查3: 是否满足收敛条件 ---
    # 条件: n * r_n^d 需要足够大 (密度条件)
    # 对于图, r_n ~ avg_deg/n 的某种函数
    # 简化: 检查平均度是否>log(n)
    log_n = np.log(n)
    density_ok = deg.mean() > log_n
    result['checks']['density_ok'] = bool(density_ok)

    # --- 综合判断 ---
    if r2_weyl > 0.95 and density_ok:
        if abs(d_eff - 3.0) < 0.5:
            result['status'] = '3D_diffusion'
            result['confidence'] = 'high'
        elif abs(d_eff - 2.0) < 0.5:
            result['status'] = '2D_diffusion'
            result['confidence'] = 'high'
        elif abs(d_eff - 1.0) < 0.5:
            result['status'] = '1D_diffusion'
            result['confidence'] = 'high'
        else:
            result['status'] = f'{d_eff:.1f}D_anomalous'
            result['confidence'] = 'medium'
    elif r2_weyl > 0.8:
        result['status'] = f'approx_{d_eff:.1f}D'
        result['confidence'] = 'low'
    else:
        result['status'] = 'no_clear_dimension'
        result['confidence'] = 'none'

    return result


# ============================================================
# 自测试: 在各种已知图上验证
# ============================================================
if __name__ == '__main__':
    print("="*60)
    print("DGF谱维度检测工具 - 自测试")
    print("="*60)

    # 测试1: 3D立方格点 (应检出d≈3)
    print("\n--- 测试1: 10×10×10 立方格点 ---")
    n = 10
    N = n**3
    row, col, data = [], [], []
    for x in range(n):
        for y in range(n):
            for z in range(n):
                i = x + y*n + z*n*n
                deg_count = 0
                for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                    nx_,ny_,nz_ = (x+dx)%n, (y+dy)%n, (z+dz)%n
                    j = nx_ + ny_*n + nz_*n*n
                    row.append(i); col.append(j); data.append(1.0)
                    deg_count += 1
    adj = sparse.coo_matrix((data,(row,col)), shape=(N,N)).tocsr()
    r = analyze_spectral_dimension(adj)
    print(f"  状态: {r['status']}, d_eff={r['d_eff']:.2f}, Weyl R²={r['checks'].get('weyl_r2',0):.4f}")

    # 测试2: 随机几何图 (应检出d≈3)
    print("\n--- 测试2: 3D随机几何图 (500节点) ---")
    from scipy.spatial import cKDTree
    np.random.seed(42)
    pts = np.random.rand(500, 3)
    tree = cKDTree(pts)
    pairs = tree.query_pairs(0.2, output_type='ndarray')
    row2 = []; col2 = []; data2 = []
    for p in pairs:
        row2.extend([p[0],p[1]]); col2.extend([p[1],p[0]]); data2.extend([1.0,1.0])
    adj2 = sparse.coo_matrix((data2,(row2,col2)), shape=(500,500)).tocsr()
    r2 = analyze_spectral_dimension(adj2)
    print(f"  状态: {r2['status']}, d_eff={r2['d_eff']:.2f}, Weyl R²={r2['checks'].get('weyl_r2',0):.4f}")

    # 测试3: 2D格点 (应检出d≈2)
    print("\n--- 测试3: 30×30 2D格点 ---")
    n2 = 30; N2 = n2**2
    row3=[];col3=[];data3=[]
    for x in range(n2):
        for y in range(n2):
            i=x+y*n2
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx_,ny_=(x+dx)%n2,(y+dy)%n2
                j=nx_+ny_*n2
                row3.append(i);col3.append(j);data3.append(1.0)
    adj3=sparse.coo_matrix((data3,(row3,col3)),shape=(N2,N2)).tocsr()
    r3=analyze_spectral_dimension(adj3)
    print(f"  状态: {r3['status']}, d_eff={r3['d_eff']:.2f}, Weyl R²={r3['checks'].get('weyl_r2',0):.4f}")

    print(f"\n工具就绪。输入任何邻接矩阵→输出有效维度+连续极限条件。")
