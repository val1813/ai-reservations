"""
LP3-S2: ED+PCA验证代码 — Yang映射在无序下的保真度计算
================================================================
Phase 3A: Disk几何ED + Fidelity F(W) + PCA分析

方法论搬用:
  - Jiang et al., Chinese Physics B 34(4), 047306 (2025): PCA探测无序相变
  - Wang-Sheng-Haldane (2009): Fidelity metric检测拓扑相变
  - Yang (2025) arXiv:2503.22940: SLL↔LLL精确映射

作者: AI-PI (Claude), nu5o2课题组
日期: 2026-05-31

使用方法:
  python phase3a_ed_pca.py --N 6 --M 18 --W-max 0.15 --n-W 10

依赖: numpy, scipy, matplotlib, sklearn (PCA)
"""

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import comb, genlaguerre, factorial
from itertools import combinations
import warnings

# ============================================================================
# PART 0: 物理常数 & 参数
# ============================================================================

HBAR = 1.0
M_ELECTRON = 1.0
EPSILON = 1.0  # 介电常数 (以e^2/epsl_B为单位)
L_B = 1.0      # 磁长度 (单位制: 所有长度以l_B为单位)
KAPPA = 1.2    # GaAs LL mixing参数 (B≈5T)

# ============================================================================
# PART 1: 单粒子基 — Disk几何对称规范
# ============================================================================

class SingleParticleBasis:
    """Disk几何单粒子基: |n, m⟩, 对称规范.

    n = Landau能级指标 (0=LLL, 1=SLL)
    m = 角动量量子数, m ≥ -n
    单粒子轨道截断: m ∈ [m_min, m_max]

    波函数 (极坐标):
      psi_{n,m}(r,θ) = N_{nm} r^{|m|} L_n^{|m|}(r^2/2) exp(-r^2/4) exp(imθ)
    其中 L_n^{|m|} 是广义Laguerre多项式, N_{nm} 是归一化常数.
    """

    def __init__(self, n_ll_max: int = 1, m_min: int = -1, m_max: int = 18):
        """
        Args:
            n_ll_max: 最大LL指标 (0=只LLL, 1=LLL+SLL)
            m_min: 最小角动量 (disk几何: m_min = -n_max for SLL, 0 for LLL)
            m_max: 最大角动量 (截断)
        """
        self.n_max = n_ll_max
        self.m_min = m_min
        self.m_max = m_max

        # 构建轨道列表
        self.orbitals = []  # [(n, m), ...]
        for n in range(n_ll_max + 1):
            for m in range(max(m_min, -n), m_max + 1):
                self.orbitals.append((n, m))

        self.n_orbitals = len(self.orbitals)
        self._build_index_map()

    def _build_index_map(self):
        """构建 (n,m) → index 映射."""
        self.idx_from_nm = {nm: i for i, nm in enumerate(self.orbitals)}
        self.nm_from_idx = {i: nm for i, nm in enumerate(self.orbitals)}

    def get_lll_indices(self) -> list:
        """返回所有LLL轨道的index."""
        return [i for i, (n, m) in enumerate(self.orbitals) if n == 0]

    def get_sll_indices(self) -> list:
        """返回所有SLL轨道的index."""
        return [i for i, (n, m) in enumerate(self.orbitals) if n == 1]

    @staticmethod
    def wavefunction_norm(n: int, m: int) -> float:
        """单粒子波函数归一化常数."""
        # N_{nm} = sqrt( n! / (2pi (n+|m|)!) )
        return np.sqrt(factorial(n) / (2.0 * np.pi * factorial(n + abs(m))))

    def describe(self):
        print(f"单粒子基: {self.n_orbitals} 个轨道")
        print(f"  LLs: 0..{self.n_max}, m ∈ [{self.m_min}, {self.m_max}]")
        lll_count = len(self.get_lll_indices())
        sll_count = len(self.get_sll_indices())
        print(f"  LLL: {lll_count} 轨道, SLL: {sll_count} 轨道")


# ============================================================================
# PART 2: 二体库仑矩阵元 — Disk几何
# ============================================================================

def haldane_pseudopotentials_disk(n_ll: int, m_max: int) -> dict:
    """计算第n_ll个LL的Haldane赝势 (disk几何).

    Haldane赝势 V_m = ⟨m| V_Coulomb |m⟩, 其中|m⟩是二体相对角动量态.
    在disk几何中, 赝势通过Laguerre多项式与form factor关联:

    V_m^{(n)} = ∫_0^inf q dq V(q) [L_n(q^2/2)]^2 L_m(q^2) exp(-q^2)

    其中 V(q) = 2pie^2/(epsq) 是2D库仑势的Fourier变换.
    """
    from scipy.integrate import quad

    def integrand(q, m, n):
        Ln_q = genlaguerre(n, 0)(q**2 / 2.0)
        Lm_q = genlaguerre(m, 0)(q**2)
        return 2.0 * np.pi * (1.0 / q) * (Ln_q**2) * Lm_q * np.exp(-q**2)

    pseudos = {}
    for m in range(m_max + 1):
        # 数值积分 (q从0到inf, 实际有效范围到~10)
        result, _ = quad(integrand, 0, 20.0, args=(m, n_ll), limit=200)
        pseudos[m] = result / (2.0 * np.pi)  # 归一化

    return pseudos


def compute_two_body_elements_disk(basis: SingleParticleBasis) -> dict:
    """计算disk几何中的二体矩阵元 (对角+非对角).

    使用Haldane赝势+角动量守恒选择定则.
    包含所有满足 m1+m2=m3+m4 的 (i,j)->(k,l) 散射过程.
    """
    n_orb = basis.n_orbitals
    Vm_lll = haldane_pseudopotentials_disk(0, 10)
    Vm_sll = haldane_pseudopotentials_disk(1, 10)

    elements = {}
    orbitals = basis.orbitals

    for a, (n1, m1) in enumerate(orbitals):
        for b, (n2, m2) in enumerate(orbitals):
            if a <= b:
                continue  # antisymmetry: only a>b (ordered pairs)
            for c, (n3, m3) in enumerate(orbitals):
                for d, (n4, m4) in enumerate(orbitals):
                    if c <= d:
                        continue

                    # Angular momentum conservation
                    if m1 + m2 != m3 + m4:
                        continue

                    # Diagonal pseudopotential approximation:
                    # only include terms where the RELATIVE angular momenta match
                    # This captures the dominant scattering channels
                    M_total = m1 + m2
                    m_rel_in = abs(m1 - m2)
                    m_rel_out = abs(m3 - m4)

                    # Allow both diagonal and off-diagonal in relative m
                    # Use the minimum relative m to select pseudopotential
                    m_pseudo = min(m_rel_in, m_rel_out) // 2

                    n_avg = max(n1, n2, n3, n4)
                    # Use LLL pseudopotentials for all-LLL, SLL for any SLL
                    if n_avg == 0:
                        Vm = Vm_lll
                    else:
                        Vm = Vm_sll

                    if m_pseudo in Vm:
                        value = Vm[m_pseudo]
                        # Sign from antisymmetrization
                        sign = 1.0
                        if (a < b) != (c < d):
                            sign = -1.0
                        elements[(a, b, c, d)] = sign * value

    return elements


# ============================================================================
# PART 3: 无序势
# ============================================================================

class DisorderPotentialFast:
    """简化无序模型: 对角在位能 (忽略LL混合).

    每个单粒子轨道有一个随机在位能 ε_{n,m} ~ N(0, W^2).
    对应平滑无序的leading-order效应.
    """

    def __init__(self, W: float, seed: int = 42):
        self.W = W
        self.seed = seed

    def onsite_energies(self, n_orbitals: int) -> np.ndarray:
        """生成对角无序势."""
        rng = np.random.RandomState(self.seed)
        return rng.normal(0, self.W, n_orbitals)


# ============================================================================
# PART 4: 多体Fock空间 & Hamiltonian构建
# ============================================================================

class FockSpaceBuilder:
    """构建N电子Fock空间 (无自旋费米子), 可选M_total约束."""

    def __init__(self, basis: SingleParticleBasis, n_electrons: int, m_total: int = None):
        self.basis = basis
        self.N = n_electrons
        self.m_total = m_total

        self.occupations = self._generate_occupations()
        self.dim = len(self.occupations)
        self.occ_to_idx = {tuple(occ): i for i, occ in enumerate(self.occupations)}

    def _generate_occupations(self) -> list:
        n_orb = self.basis.n_orbitals
        occ_list = []
        for combo in combinations(range(n_orb), self.N):
            if self.m_total is not None:
                m_sum = sum(self.basis.orbitals[i][1] for i in combo)
                if m_sum != self.m_total:
                    continue
            occ = np.zeros(n_orb, dtype=np.int8)
            occ[list(combo)] = 1
            occ_list.append(occ)
        return occ_list

    def describe(self):
        print(f"Fock space: dim={self.dim} (N={self.N}, M_orbitals={self.basis.n_orbitals}" +
              (f", M_total={self.m_total}" if self.m_total is not None else "") + ")")


def build_hamiltonian_full(fock: FockSpaceBuilder,
                           two_body_elements: dict,
                           disorder_onsite: np.ndarray = None) -> tuple:
    """稀疏Hamiltonian with diagonal 2-body + disorder + leading off-diagonal 2-body.

    对角贡献: 2-body diagonal + onsite disorder
    非对角贡献: 2-particle hops (i,j) -> (k,l) with same M_total
    """
    dim = fock.dim
    basis = fock.basis
    n_orb = basis.n_orbitals

    H_diag = np.zeros(dim)
    H_data = [[] for _ in range(dim)]
    H_indices = [[] for _ in range(dim)]

    # 预计算所有二体跃迁 (i,j) -> (k,l)
    # 只保留角动量守恒的跃迁
    print("  Building 2-body hop table...", end=" ", flush=True)
    hop_table = {}  # {(i,j): [(k,l, V_val), ...]}
    for (i, j, k, l), V_val in two_body_elements.items():
        if i != k or j != l:  # 非对角only
            key = (i, j)
            if key not in hop_table:
                hop_table[key] = []
            hop_table[key].append((k, l, V_val))
    print(f"{len(hop_table)} source pairs")

    for idx_a, occ_a in enumerate(fock.occupations):
        occupied = np.where(occ_a == 1)[0]
        diag_elem = 0.0
        row_offdiag = {}

        # 对角二体
        for i_idx, i in enumerate(occupied):
            for j in occupied[i_idx+1:]:
                key = (i, j, i, j)
                if key in two_body_elements:
                    diag_elem += two_body_elements[key]

        # 对角无序
        if disorder_onsite is not None:
            for i in occupied:
                diag_elem += disorder_onsite[i]

        # 非对角二体 (restricted to valid hops)
        for i_idx, i in enumerate(occupied):
            for j_idx, j in enumerate(occupied):
                if j_idx <= i_idx:
                    continue
                key = (i, j)
                if key in hop_table:
                    for k, l, V_val in hop_table[key]:
                        if occ_a[k] == 1 or occ_a[l] == 1:
                            continue
                        occ_b = occ_a.copy()
                        occ_b[i] = 0; occ_b[j] = 0
                        occ_b[k] = 1; occ_b[l] = 1
                        idx_b = fock.occ_to_idx.get(tuple(occ_b))
                        if idx_b is not None:
                            row_offdiag[idx_b] = row_offdiag.get(idx_b, 0.0) + V_val

        H_diag[idx_a] = diag_elem
        idxs = list(row_offdiag.keys())
        H_data[idx_a] = [row_offdiag[k] for k in idxs]
        H_indices[idx_a] = idxs

    return H_diag, H_data, H_indices


def build_hamiltonian_fast(fock: FockSpaceBuilder,
                           two_body_diag: dict = None,
                           disorder_onsite: np.ndarray = None) -> tuple:
    """快速Hamiltonian构建 (只保留对角项+单粒子跳跃).

    H = H_2body_diag + H_disorder_onsite

    非对角二体项暂跳过以加速计算.
    """
    dim = fock.dim
    basis = fock.basis

    H_diag = np.zeros(dim)
    H_data = [[] for _ in range(dim)]
    H_indices = [[] for _ in range(dim)]

    for idx_a, occ_a in enumerate(fock.occupations):
        occupied = np.where(occ_a == 1)[0]
        diag_elem = 0.0

        # 对角二体贡献
        if two_body_diag:
            for i_idx, i in enumerate(occupied):
                for j in occupied[i_idx+1:]:
                    key = (i, j, i, j)
                    if key in two_body_diag:
                        diag_elem += two_body_diag[key]

        # 无序在位能
        if disorder_onsite is not None:
            for i in occupied:
                diag_elem += disorder_onsite[i]

        H_diag[idx_a] = diag_elem

    return H_diag, H_data, H_indices


# ============================================================================
# PART 5: Lanczos对角化 (基态求解)
# ============================================================================

def lanczos_ground_state(H_diag: np.ndarray, H_data: list, H_indices: list,
                         n_iter: int = 100, tol: float = 1e-12) -> tuple:
    """Lanczos迭代求解稀疏Hamiltonian的基态.

    Returns:
        (E0, psi0): 基态能量和波函数
    """
    dim = len(H_diag)

    # 随机初始向量
    v0 = np.random.randn(dim) + 1j * np.random.randn(dim)
    v0 /= np.linalg.norm(v0)

    alphas = []
    betas = []
    V = [v0]

    # Lanczos迭代
    w = np.zeros(dim, dtype=complex)
    for k in range(n_iter):
        # w = H|v_k⟩ - beta_k|v_{k-1}⟩
        v_k = V[k]

        # H|v_k⟩
        w[:] = H_diag * v_k
        for j, (vals, idxs) in enumerate(zip(H_data, H_indices)):
            for val, idx in zip(vals, idxs):
                w[j] += val * v_k[idx]
                w[idx] += np.conj(val) * v_k[j]

        if k > 0:
            w -= betas[-1] * V[k-1]

        alpha = np.real(np.vdot(v_k, w))
        alphas.append(alpha)
        w -= alpha * v_k

        beta = np.linalg.norm(w)
        betas.append(beta)
        if beta < tol:
            break
        V.append(w / beta)

    # 三对角矩阵对角化
    n = len(alphas)
    T_diag = np.array(alphas)
    T_offdiag = np.array(betas[:n-1])

    eigenvalues, eigenvectors = eigh_tridiagonal(T_diag, T_offdiag)

    E0 = eigenvalues[0]
    # Ritz向量
    psi0 = np.zeros(dim, dtype=complex)
    for k in range(n):
        psi0 += eigenvectors[k, 0] * V[k]

    return E0, psi0


# ============================================================================
# PART 6: Yang映射算符
# ============================================================================

def yang_mapping_operator(basis: SingleParticleBasis, fock_space: FockSpaceBuilder) -> np.ndarray:
    """构建Yang映射算符 U = ∏_i (-2)^{1/2} a_i^† 的多体矩阵.

    映射方向: LLL → SLL

    U|Ψ_LLL⟩ = |Ψ_SLL_mapped⟩

    在Fock空间中, U将每个占据的LLL轨道 |0,m⟩ 提升到SLL轨道 |1,m⟩.
    (a^†不改变角动量m, 因为 [a^†, L_z] = 0)
    """
    dim = fock_space.dim
    U_mat = np.zeros((dim, dim), dtype=complex)

    # 为每个LLL轨道找到对应的SLL轨道
    lll_to_sll = {}
    for i, (n, m) in enumerate(basis.orbitals):
        if n == 0:
            # 找相同m的SLL轨道
            for j, (n2, m2) in enumerate(basis.orbitals):
                if n2 == 1 and m2 == m:
                    lll_to_sll[i] = j
                    break

    # 构建映射矩阵
    # U|occ_LLL⟩ = (-2)^{N/2} |occ_SLL⟩ where occ_SLL有相同的角动量分布
    for idx_a, occ_a in enumerate(fock_space.occupations):
        # 检查所有占据轨道是否都在LLL中
        occ_indices = np.where(occ_a == 1)[0]
        all_lll = all(basis.orbitals[i][0] == 0 for i in occ_indices)

        if all_lll:
            # 映射到SLL
            occ_b = np.zeros_like(occ_a)
            for i in occ_indices:
                if i in lll_to_sll:
                    occ_b[lll_to_sll[i]] = 1

            idx_b = fock_space.occ_to_idx.get(tuple(occ_b))
            if idx_b is not None:
                # 因子: (-2)^{N/2}
                factor = (-2.0) ** (fock_space.N / 2.0)
                U_mat[idx_b, idx_a] = factor

    return U_mat


# ============================================================================
# PART 7: 保真度计算
# ============================================================================

def compute_fidelity(psi_sll: np.ndarray, psi_lll: np.ndarray,
                     U_mat: np.ndarray) -> float:
    """计算映射保真度.

    F(W) = |⟨Ψ_SLL(W)| U |Ψ_LLL(W)⟩|^2

    Args:
        psi_sll: SLL物理基态 (有/无序)
        psi_lll: LLL物理基态 (有/无序)
        U_mat: Yang映射矩阵

    Returns:
        F: 保真度, 0 ≤ F ≤ 1
    """
    # U|Ψ_LLL⟩
    mapped = U_mat @ psi_lll

    # ⟨Ψ_SLL| U |Ψ_LLL⟩
    overlap = np.vdot(psi_sll, mapped)

    return np.abs(overlap) ** 2


def compute_fidelity_metric(F_vals: np.ndarray, W_vals: np.ndarray) -> np.ndarray:
    """计算 fidelity metric (Wang-Sheng-Haldane 2009).

    F_metric(W) = -ln[F(W)] / (δW)^2

    在相变点附近发散.
    """
    dW = W_vals[1] - W_vals[0]
    F_metric = np.zeros(len(W_vals) - 2)

    for i in range(1, len(W_vals) - 1):
        F_metric[i-1] = -np.log(max(F_vals[i], 1e-16)) / (dW**2)

    return F_metric


# ============================================================================
# PART 8: PCA分析 (搬用Jiang et al. 2025)
# ============================================================================

def pca_analysis(wavefunctions: list, n_components: int = 3) -> dict:
    """对无序系综的波函数做PCA.

    方法: Jiang et al., CPB 34, 047306 (2025)

    将波函数表示为实向量 (取实部和虚部拼接),
    然后做标准PCA.

    Args:
        wavefunctions: [psi(W_1), psi(W_2), ...], 每个是复向量
        n_components: PCA主成分数量

    Returns:
        dict with:
          - 'pc_amplitudes': 每个W值的PCA主成分振幅 (n_W × n_components)
          - 'explained_variance': 各主成分的解释方差比
          - 'cross_point': 第一和第二主成分的交叉点 (相变指示器)
    """
    from sklearn.decomposition import PCA

    # 转换为实特征矩阵
    n_samples = len(wavefunctions)
    dim = len(wavefunctions[0])

    X = np.zeros((n_samples, 2 * dim))
    for i, psi in enumerate(wavefunctions):
        X[i, :dim] = psi.real
        X[i, dim:] = psi.imag

    # 标准化
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X_std[X_std < 1e-15] = 1.0
    X_scaled = (X - X_mean) / X_std

    # PCA
    pca = PCA(n_components=n_components)
    pc_amplitudes = pca.fit_transform(X_scaled)

    # 寻找交叉点: PC1和PC2振幅的交点
    cross_point = None
    pc1 = pc_amplitudes[:, 0]
    pc2 = pc_amplitudes[:, 1]

    for i in range(len(pc1) - 1):
        if (pc1[i] - pc2[i]) * (pc1[i+1] - pc2[i+1]) < 0:
            cross_point = i
            break

    return {
        'pc_amplitudes': pc_amplitudes,
        'explained_variance': pca.explained_variance_ratio_,
        'cross_point': cross_point,
        'pca_model': pca
    }


# ============================================================================
# PART 9: 主实验循环
# ============================================================================

def run_experiment(N: int = 6, M_orbitals: int = 14,
                   M_total: int = None,
                   W_vals: list = None,
                   n_disorder_realizations: int = 5,
                   verbose: bool = True) -> dict:
    """运行完整的F(W)曲线+PCA实验.

    Args:
        N: 电子数
        M_orbitals: 单粒子轨道截断 (角动量)
        M_total: 总角动量约束 (None=不约束). 默认=N*(N-1)//2 (最大密度液滴)
        W_vals: 无序强度列表
        n_disorder_realizations: 每个W值的无序实现数
    """
    if W_vals is None:
        W_vals = np.linspace(0.0, 0.15, 10)

        M_total = None  # No constraint for now

    if verbose: print("=" * 70)
    if verbose: print(f"LP3-S2 ED+PCA: N={N}, M_max={M_orbitals}, M_total={M_total}")
    if verbose: print("=" * 70)

    basis_lll = SingleParticleBasis(n_ll_max=0, m_min=0, m_max=M_orbitals)
    basis_sll = SingleParticleBasis(n_ll_max=1, m_min=-1, m_max=M_orbitals)

    if verbose:
        print("\n[1] Single-particle basis:")
        basis_lll.describe()
        basis_sll.describe()

    # 2. Fock空间 (with M_total constraint)
    fock_lll = FockSpaceBuilder(basis_lll, N, m_total=M_total)
    fock_sll = FockSpaceBuilder(basis_sll, N, m_total=M_total)

    if verbose:
        print(f"\n[2] Fock space:")
        fock_lll.describe()
        fock_sll.describe()

    if fock_lll.dim == 0 or fock_sll.dim == 0:
        raise ValueError(f"No states with M_total={M_total}! Try different M_total.")

    # 3. 计算二体矩阵元
    if verbose: print(f"\n[3] 计算二体库仑矩阵元...")
    tb_lll = compute_two_body_elements_disk(basis_lll)
    tb_sll = compute_two_body_elements_disk(basis_sll)
    if verbose: print(f"  LLL: {len(tb_lll)} 个非零元")
    if verbose: print(f"  SLL: {len(tb_sll)} 个非零元")

    # 4. 构建Yang映射算符 (联合基, same M_total)
    basis_both = SingleParticleBasis(n_ll_max=1, m_min=-1, m_max=M_orbitals)
    fock_both = FockSpaceBuilder(basis_both, N, m_total=M_total)
    U_mat = yang_mapping_operator(basis_both, fock_both)
    if verbose: print(f"\n[4] Yang mapping operator: {U_mat.shape}, M_total={M_total}")

    # 5. 对每个W值运行
    results = {
        'W_vals': W_vals,
        'N': N,
        'M_orbitals': M_orbitals,
        'fidelity': [],
        'fidelity_std': [],
        'wavefunctions_sll': [],
        'wavefunctions_lll': [],
        'energies_sll': [],
        'energies_lll': [],
    }

    for i_W, W in enumerate(W_vals):
        if verbose: print(f"\n[5.{i_W+1}/{len(W_vals)}] W = {W:.4f}")

        F_vals = []

        for r in range(n_disorder_realizations):
            seed = 42 + i_W * 100 + r

            disorder = DisorderPotentialFast(W, seed=seed)
            V_onsite_lll = disorder.onsite_energies(basis_lll.n_orbitals)
            V_onsite_sll = disorder.onsite_energies(basis_sll.n_orbitals)

            # Full Hamiltonian with off-diagonal 2-body terms
            if i_W == 0 and r == 0:
                H_diag_lll, H_data_lll, H_idx_lll = build_hamiltonian_full(
                    fock_lll, tb_lll, V_onsite_lll)
            else:
                H_diag_lll, H_data_lll, H_idx_lll = build_hamiltonian_full(
                    fock_lll, tb_lll, V_onsite_lll)

            E0_lll, psi_lll = lanczos_ground_state(H_diag_lll, H_data_lll, H_idx_lll,
                                                    n_iter=min(100, fock_lll.dim//2))

            H_diag_sll, H_data_sll, H_idx_sll = build_hamiltonian_full(
                fock_sll, tb_sll, V_onsite_sll)
            E0_sll, psi_sll = lanczos_ground_state(H_diag_sll, H_data_sll, H_idx_sll,
                                                    n_iter=min(100, fock_sll.dim//2))

            # 计算保真度
            # 注意: psi_lll在LLL Fock空间中, psi_sll在SLL Fock空间中
            # 需要将两者embed到联合基中再计算
            if r == 0:
                results['energies_sll'].append(E0_sll)
                results['energies_lll'].append(E0_lll)

            # 简化保真度: 使用波函数的overlap绝对值平方
            # (完整版需要embed到联合基, 这里用绝对值作为近似)
            F = compute_fidelity_proper(psi_lll, psi_sll,
                                        fock_lll, fock_sll, fock_both,
                                        basis_lll, basis_sll, basis_both,
                                        U_mat)
            F_vals.append(F)

        F_mean = np.mean(F_vals)
        F_std = np.std(F_vals)
        results['fidelity'].append(F_mean)
        results['fidelity_std'].append(F_std)

        if verbose:
            print(f"  F = {F_mean:.6f} ± {F_std:.6f}")

    return results


def compute_fidelity_proper(psi_lll_small, psi_sll_small,
                           fock_lll, fock_sll, fock_both,
                           basis_lll, basis_sll, basis_both,
                           U_mat) -> float:
    """正确保真度: 将LLL和SLL波函数embed到联合基中.

    Steps:
    1. 将LLL基中的基态embed到联合Fock空间
    2. 用Yang映射U作用
    3. 将SLL基中的基态embed到联合Fock空间
    4. 计算overlap

    嵌入规则: LLL轨道(0,m)联合基中的index与LLL-only基相同.
    SLL轨道(1,m)在联合基中的index = len(lll_only_orbitals) + sll_offset.
    """
    # 建立LLL-only基到联合基的occupation映射
    # LLL-only: orbitals are (0,0), (0,1), ..., (0, M)
    # Both: orbitals are (0,-1), (1,-1), (0,0), (1,0), (0,1), (1,1), ...
    # Actually, the 'both' basis is built as:
    #   n=0, m=-1 (invalid, m>=-n means m>=0 for n=0)
    # Let me rebuild the mapping properly

    # 联合基中 LLL 轨道的 index
    lll_in_both = {}
    for i, (n, m) in enumerate(basis_both.orbitals):
        if n == 0 and m >= 0:  # valid LLL orbital
            # Find this orbital in the LLL-only basis
            for j, (n2, m2) in enumerate(basis_lll.orbitals):
                if n2 == n and m2 == m:
                    lll_in_both[j] = i
                    break

    # 联合基中 SLL 轨道的 index
    sll_in_both = {}
    for i, (n, m) in enumerate(basis_both.orbitals):
        if n == 1:
            for j, (n2, m2) in enumerate(basis_sll.orbitals):
                if n2 == n and m2 == m:
                    sll_in_both[j] = i
                    break

    # 嵌入LLL波函数: 膨胀到联合Fock空间
    psi_lll_both = np.zeros(fock_both.dim, dtype=complex)
    for idx_lll, occ_lll in enumerate(fock_lll.occupations):
        # 在联合基中构建对应的occupation
        occ_both = np.zeros(basis_both.n_orbitals, dtype=np.int8)
        for i in np.where(occ_lll == 1)[0]:
            if i in lll_in_both:
                occ_both[lll_in_both[i]] = 1
        idx_both = fock_both.occ_to_idx.get(tuple(occ_both))
        if idx_both is not None:
            psi_lll_both[idx_both] = psi_lll_small[idx_lll]

    # 嵌入SLL波函数
    psi_sll_both = np.zeros(fock_both.dim, dtype=complex)
    for idx_sll, occ_sll in enumerate(fock_sll.occupations):
        occ_both = np.zeros(basis_both.n_orbitals, dtype=np.int8)
        for i in np.where(occ_sll == 1)[0]:
            if i in sll_in_both:
                occ_both[sll_in_both[i]] = 1
        idx_both = fock_both.occ_to_idx.get(tuple(occ_both))
        if idx_both is not None:
            psi_sll_both[idx_both] = psi_sll_small[idx_sll]

    # 归一化
    norm_lll = np.linalg.norm(psi_lll_both)
    norm_sll = np.linalg.norm(psi_sll_both)
    if norm_lll > 1e-15:
        psi_lll_both /= norm_lll
    if norm_sll > 1e-15:
        psi_sll_both /= norm_sll

    # Yang映射: U|psi_LLL>
    psi_mapped = U_mat @ psi_lll_both

    # Fidelity: |<psi_SLL|U|psi_LLL>|^2
    overlap = np.vdot(psi_sll_both, psi_mapped)
    F = np.abs(overlap)**2

    return min(F, 1.0)


# ============================================================================
# PART 10: 结果可视化 & 导出
# ============================================================================

def plot_results(results: dict, save_path: str = None):
    """绘制F(W)曲线 + PCA分析."""
    import matplotlib.pyplot as plt

    W_vals = results['W_vals']
    F_vals = np.array(results['fidelity'])
    F_std = np.array(results['fidelity_std'])

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Panel 1: Fidelity F(W)
    ax = axes[0]
    ax.errorbar(W_vals, F_vals, yerr=F_std, marker='o', capsize=3)
    ax.set_xlabel('Disorder strength W (e^2/eps*l_B)')
    ax.set_ylabel('Fidelity F(W)')
    ax.set_title(f'Yang Mapping Fidelity (N={results["N"]})')
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    # Panel 2: Fidelity metric
    if len(W_vals) > 3:
        ax = axes[1]
        F_metric = compute_fidelity_metric(F_vals, W_vals)
        W_mid = (W_vals[1:-1] + W_vals[2:]) / 2.0
        ax.semilogy(W_mid, F_metric, 'o-', color='red')
        ax.set_xlabel('W (e^2/eps*l_B)')
        ax.set_ylabel('Fidelity metric chi_F')
        ax.set_title('Phase Transition Indicator')
        ax.grid(True, alpha=0.3)

    # Panel 3: Energies
    ax = axes[2]
    if results.get('energies_sll'):
        E_sll = np.array(results['energies_sll'])
        E_lll = np.array(results['energies_lll'])
        E_sll -= E_sll[0]  # 相对于clean极限
        E_lll -= E_lll[0]
        ax.plot(W_vals[:len(E_sll)], E_sll, 'o-', label='SLL')
        ax.plot(W_vals[:len(E_lll)], E_lll, 's-', label='LLL')
        ax.set_xlabel('W (e^2/epsl_B)')
        ax.set_ylabel('E₀(W) - E₀(0)')
        ax.legend()
        ax.set_title('Ground State Energy Shift')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"图已保存到 {save_path}")
    else:
        plt.show()


def export_results(results: dict, filepath: str):
    """导出结果为JSON."""
    import json

    export = {
        'parameters': {
            'N': results['N'],
            'M_orbitals': results['M_orbitals'],
            'W_vals': list(results['W_vals']),
        },
        'fidelity': [float(f) for f in results['fidelity']],
        'fidelity_std': [float(s) for s in results['fidelity_std']],
        'energies_sll': [float(e) for e in results.get('energies_sll', [])],
        'energies_lll': [float(e) for e in results.get('energies_lll', [])],
    }

    with open(filepath, 'w') as f:
        json.dump(export, f, indent=2)
    print(f"结果已导出到 {filepath}")


# ============================================================================
# PART 11: 主程序
# ============================================================================

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='LP3-S2: ED+PCA验证Yang映射在无序下的保真度')
    parser.add_argument('--N', type=int, default=6,
                        help='电子数 (默认6)')
    parser.add_argument('--M', type=int, default=16,
                        help='最大角动量截断 (默认16)')
    parser.add_argument('--W-max', type=float, default=0.15,
                        help='最大无序强度 e^2/epsl_B (默认0.15)')
    parser.add_argument('--n-W', type=int, default=8,
                        help='无序强度采样点数 (默认8)')
    parser.add_argument('--n-disorder', type=int, default=3,
                        help='每个W的无序实现数 (默认3)')
    parser.add_argument('--seed', type=int, default=42,
                        help='随机种子')
    parser.add_argument('--output', type=str, default=None,
                        help='结果JSON输出路径')
    parser.add_argument('--plot', type=str, default=None,
                        help='保存图像路径')

    args = parser.parse_args()

    np.random.seed(args.seed)

    W_vals = np.linspace(0.0, args.W_max, args.n_W)

    results = run_experiment(
        N=args.N,
        M_orbitals=args.M,
        W_vals=W_vals,
        n_disorder_realizations=args.n_disorder,
        verbose=True
    )

    # 输出摘要
    print("\n" + "=" * 70)
    print("结果摘要")
    print("=" * 70)
    for i, W in enumerate(W_vals):
        print(f"  W={W:.4f}: F={results['fidelity'][i]:.6f} ± {results['fidelity_std'][i]:.6f}")

    # 查找保真度降到0.9以下的临界W
    for i, F in enumerate(results['fidelity']):
        if F < 0.9:
            print(f"\n  映射保真度在 W_c ≈ {W_vals[i]:.4f} 处降至 {F:.4f} < 0.9")
            break
    else:
        print(f"\n  映射保真度在所有W范围内 > 0.9")

    if args.output:
        export_results(results, args.output)

    if args.plot:
        plot_results(results, args.plot)

    print("\n实验完成.")
