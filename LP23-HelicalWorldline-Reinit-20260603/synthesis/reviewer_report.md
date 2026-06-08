# REVIEWER report: LP23-S1

## 第零步：AI幻觉检查

✅ 幻觉检查通过（量纲✅/方向✅/循环✅/量级✅）。

- `ds^2=-c^2dt^2+dX^2+dY^2`：`ds^2,dX^2,dY^2,c^2dt^2` 均为 `m^2`。符号约定为 `(-,+,+)`。
- `X=ell cos(omega t+phi)`, `Y=ell sin(omega t+phi)`：`X,Y,ell` 为 `m`；`omega t+phi` 无量纲；并集 `X^2+Y^2=ell^2` 两侧均为 `m^2`。
- `X^2+Y^2=c^2t^2`：两侧均为 `m^2`。
- `theta=(Et-p·x)/hbar=p_mu x^mu/hbar`：`Et` 与 `p·x` 均为 `J s`，除以 `hbar` 后无量纲。`p_mu x^mu` 需声明采用 `x^0=ct,p_0=E/c` 或等价约定，否则符号层面易误读。
- `cos alpha'=(cos alpha-beta)/(1-beta cos alpha)`：全部无量纲。
- `k^mu=xi^dagger sigma^mu xi`：若 `xi` 取 projective spinor/方向自旋量，`k^mu` 为归一化 null direction；若要当物理四动量或仿射切向量，必须另给归一化尺度。
- `B_ab=q_a^c q_b^d nabla_d k_c` 与 `omega_ab=B_[ab]`：在 `k` 为无量纲方向场、`nabla` 为 `1/m` 时，`B_ab,Theta,sigma_ab,omega_ab` 为 `1/m`。若 `k` 重新缩放，光学标量随仿射规范改变，作者必须固定规范。
- 无方向性数值结论可做极限反号检查；无实验数据拟合，循环论证项未触发；无量级估算列表，量级鸿沟项未触发。

## 三轮查重

三轮查重已执行（方法层✅/框架盲区✅/否定性✅）。未发现一篇覆盖“固定半径螺旋完整编码 QM+GR、包络即光锥、轴弯曲即引力”这一原始强声张的直接竞争论文；但发现当前 LP23-R1 的 contact/null-geodesic/projective-spinor 关键部件存在明确先发冲突，且当前稿件没有给出足以越过这些先发工作的独立定理。

⛔ 先发冲突警告：Adrià Marín-Salvador, “On the Canonical Contact Structure of the Space of Null Geodesics of a Spacetime”, 2021, arXiv:2109.03656；Adrià Marín-Salvador and Roberto Rubio, “On the space of null geodesics of a spacetime: the compact case, Engel geometry and retrievability”, 2023, arXiv:2112.06955。发现于第2轮（框架盲区），关键词：`space of null geodesics contact structure Engel Lorentz prolongation`。这些工作已经把 null geodesics 的空间、canonical contact structure、Lorentz prolongation/Engel geometry 与 spacetime retrievability 建成明确定理；LP23-R1 的“null cone 是商-投影、optical data 是水平/screen 分布曲率”若不新增严格结构，只是在改名。

否定性/冲突检索还检出：Ezra T. Newman, “Light-Cones, Almost Light-Cones and Almost-Complex Light-Cones”, 2017, arXiv:1704.04971。该文将普通 light cone congruence、twisting shear-free congruence 与 complex world-line 区分开，并把 twist 归于 complex coordinate/imaginary displacement，而不是一般 `U(1)` 相位。另检出 Marco Budinich, “On Spinors and Null Vectors”, 2014, arXiv:1208.0881，说明 spinor-null vector 关系已有成熟 Clifford/pure spinor 条件，不能由整体 `U(1)` 相位直接取得 null direction。

## 高风险引用核实

无 `[摘要级]` 或 `[印象引用]` 引用条目，输入也未给出 AUDITOR 标注的“引用内容疑似偏差”。按协议跳过内容核实。未发现“引用虚构”；本报告不对不存在的引用作虚构判定。

## 叙事退让警告

⛔ 叙事退让警告：原声张“`e^(iθ)` 为基元，单位螺旋在 `(Re, Im, t)` 中完整编码 QM+GR，螺旋包络给出光锥，轴弯曲给出引力” → 当前声张“原始强声张证伪，收官为有边界；固定半径螺旋不是光锥，`Re/Im` 不能直接当 Minkowski 坐标，相位 holonomy 只可影响干涉/偏振/screen-frame 运输”。退让方式：从无条件统一论退到一组标准几何否定句和一个未成型的新候选框架。这不是科学进步，是在规避原核心攻击。要求恢复原声张并补强推导，或承认 LP23-S1 不是可投稿物理论文命题。

## 五条拒稿理由

1. 核心假设存在最简可计算反例。取 `c=1, ell=1, omega=1, phi=0`，螺旋为 `X=cos t,Y=sin t`，所以所有点满足 `X^2+Y^2=1`；光锥截面要求 `X^2+Y^2=t^2`。在 `t=2` 时螺旋点半径仍为 1，而光锥半径为 2；在 `t=0` 时光锥半径为 0，而螺旋半径为 1。两者只可能在孤立时刻相交，不能作为包络等同。作者需要证明存在非任意、协变、非逐点调参的映射把圆柱族变成完整 null cone。[致命；作者需证明什么：给出一个 Lorentz 协变的构造，使固定半径相位族在全部 `t` 上自然产生 `X^2+Y^2=c^2t^2`，而不是事后重定义尺度。]

2. 推导链最薄弱处是把无量纲相位空间坐标、observer celestial angle 和 spacetime null direction 混成同一对象。`theta=(Et-p·x)/hbar` 是 Lorentz 标量；`alpha` 是观察者天球坐标，boost 下按 aberration 变换；`Re/Im` 是 `U(1)` 纤维坐标而非 Minkowski 坐标。把 `theta=alpha` 或把 `e^{i theta}` 的实虚部当作空间坐标，会同时破坏量纲、协变性和纤维/底空间区分。作者需要证明相位纤维到 null direction 的投影是自然变换，并与 Lorentz 群作用交换。[致命；作者需证明什么：构造明确的 bundle map/自然变换，并证明 `boost ∘ map = map ∘ phase-action`。]

3. 与已有文献发生冲突。Marín-Salvador 与 Rubio, “On the space of null geodesics of a spacetime: the compact case, Engel geometry and retrievability”, arXiv:2112.06955，给出 `N ~= PC/W` 与 canonical contact structure `H ~= p_*E`，并刻画哪些三维 contact manifolds 可作为 spacetime null geodesics 的空间。LP23-R1 若声称“因果光锥、contact 主丛、horizontal/screen 曲率”的共同来源是本工作新结构，就与这篇文献的核心定理重叠；若声称加入 `U(1)` phase holonomy 才是新点，则仍未证明该垂直 holonomy 改变 null cone/contact structure 而非只是在既有结构上附加一个无关纤维。条件覆盖：该文覆盖三维 Lorentz/contact/Engel 框架，与输入的 `(Re,Im,t)` 三维设置直接相关。[严重；作者需证明什么：逐一定义 LP23-R1 与 arXiv:2112.06955 的对象、态射和定理差异，并给出一个该文不能推出的新命题。]

4. 数值合理性不能由“选择尺度”补救。若取 `ell=c/omega` 让固定半径螺旋在 `t=1/omega` 与光锥半径相等，则在 `t=10/omega` 有 `ell/(ct)=0.1`，在 `t=0.1/omega` 有 `ell/(ct)=10`；相对半径误差分别为 90% 与 900%。若取 `ell` 为 Planck 长度，在 `t=1 s` 时 `ell/(ct)≈5.4e-44`。这不是小修正，而是圆柱与锥的全局形状不相容。作者需要证明一个区间内的误差控制，而不是在单点调平半径。[严重；作者需证明什么：给出无量纲误差函数、尺度选择规则和在非零时间区间上的上界。]

5. 最近似的已有工作已经占据了当前稿件想退到的位置。Newman, “Light-Cones, Almost Light-Cones and Almost-Complex Light-Cones”, arXiv:1704.04971，把 ordinary light-cones、almost-complex light-cones、twisting shear-free congruences 和 complex world-lines 的关系写成标准 null-congruence 语言；Budinich, “On Spinors and Null Vectors”, arXiv:1208.0881，把 spinor 与 null vector/纯 spinor 条件写成 Clifford algebra 定理。LP23 的差异若只是把这些对象称为“螺旋/扭转共同来源”或“相位 holonomy”，不是新颖物理结论；若差异是宣称 Berry/Hopf 曲率推出 optical twist，则与输入第6条自身承认的“非零 holonomy 可与零 optical twist 共存”相矛盾。作者需要证明新结构不仅复述已有 twistor/contact/spinor 语言，而且推出一个已有框架不含的可检验或可判定命题。[严重；作者需证明什么：给出与 arXiv:1704.04971、arXiv:1208.0881 不等价的定理或观测后果，并说明为何不是术语替换。]

建议拒稿。一句话理由：当前稿件从原始统一声张退化为标准反例和未定型的 contact/spinor 重新命名，且关键候选方向已有先发结构覆盖。

## 改动文件路径

- `D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\synthesis\reviewer_report.md`
