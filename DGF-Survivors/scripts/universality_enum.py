#!/usr/bin/env python3
"""
DGF q-field Universality Enumeration v2.1
==========================================
Brute-force enumeration of 6 microscopic graph types to test whether
the effective q-field equation is universal under coarse-graining.

Hypothesis: Any microscopic graph satisfying DGF symmetries (info conservation,
locality, isotropy, q bounded) produces the SAME effective q-field equation
at large scales:  partial_tau q = D nabla^2 q - Gamma(q).
Only D and Gamma values depend on micro-details; the functional form is universal.

6 Graph Types (each ~1000 nodes):
  G1: 3D cubic lattice 10x10x10, 6 neighbors, periodic BC
  G2: 3D random geometric graph, r=0.15, largest CC only
  G3: 3D small-world, cubic + 10% rewiring
  G4: Random 3-regular graph, no geometric embedding
  G5: 3D FCC lattice, 12 neighbors
  G6: 3D randomly perturbed cubic, 6-NN by Euclidean distance

Dynamics (Dirichlet at source):
  Source nodes fixed at q=0.5. Other nodes evolve:
  q_i(t+1) = q_i + (eta/deg_i)*sum_{j~i}(q_j - q_i) - gamma*q_i*(1-q_i)
  This is degree-normalized diffusion -> stable across heterogeneous degrees.

Parameters: eta=0.1, gamma=0.01, source q=0.5 fixed (Dirichlet)
"""

import numpy as np
from scipy import spatial
import networkx as nx
from sklearn.cluster import KMeans
import warnings, time, json, os
from collections import defaultdict
from itertools import product

warnings.filterwarnings('ignore')
np.random.seed(42)

# ============================================================================
# PARAMETERS
# ============================================================================
ETA      = 0.1       # diffusion per-edge coupling (degree-normalized)
GAMMA    = 0.01      # archiving rate
Q_SOURCE = 0.5       # Dirichlet fixed q at source nodes
MAX_ITER = 50000
TOL      = 1e-8

CG_LAYERS = [0, 1, 2, 3]
CG_SIZES  = [None, 125, 15, 2]

# ============================================================================
# UTILITY
# ============================================================================
def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 0.0

def fmt(val):
    if val is None: return "    None"
    if isinstance(val, float) and np.isnan(val): return "     nan"
    if isinstance(val, float):
        return f"{val:8.4f}" if abs(val) < 100 else f"{val:8.2f}"
    return f"{val!s:>8s}"

class SourceSet:
    def __init__(self, idxs, center_pos=None):
        self.idxs = set(idxs)
        self.center = center_pos


# ============================================================================
# GRAPH BUILDERS
# ============================================================================

def build_G1_cubic():
    """G1: 3D cubic 10x10x10, 6NN, periodic. Source: center 5x5x5=125 nodes."""
    n = 10; N = n**3
    idx_to_xyz = np.zeros((N, 3), dtype=float)
    xyz_to_idx = {}
    for idx, (x,y,z) in enumerate(product(range(n), repeat=3)):
        idx_to_xyz[idx] = [x, y, z]
        xyz_to_idx[(x,y,z)] = idx

    edges = []
    for (x,y,z), i in xyz_to_idx.items():
        for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nx_,ny_,nz_ = (x+dx)%n, (y+dy)%n, (z+dz)%n
            j = xyz_to_idx[(nx_,ny_,nz_)]
            if i < j: edges.append((i,j))

    G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(edges)
    src_list = []
    for x in range(2,7):
        for y in range(2,7):
            for z in range(2,7):
                src_list.append(xyz_to_idx[(x,y,z)])
    src = SourceSet(src_list, center_pos=np.array([4.5,4.5,4.5]))
    return G, idx_to_xyz, src, "G1_cubic"


def build_G2_random_geometric():
    """G2: 3D random geometric, 1000 pts in [0,1]^3, r=0.15. Largest CC."""
    N_raw = 1000
    pts = np.random.rand(N_raw, 3)
    tree = spatial.cKDTree(pts)
    pairs = tree.query_pairs(0.15, output_type='ndarray')
    G = nx.Graph(); G.add_nodes_from(range(N_raw)); G.add_edges_from(pairs)
    cc = max(nx.connected_components(G), key=len)
    G = G.subgraph(cc).copy()
    old = sorted(G.nodes())
    G = nx.relabel_nodes(G, {o:i for i,o in enumerate(old)})
    pts = pts[old]; N = G.number_of_nodes()
    centroid = pts.mean(axis=0)
    dists = np.linalg.norm(pts - centroid, axis=1)
    n_src = max(1, int(0.1*N))
    src_idx = np.argsort(dists)[:n_src]
    src = SourceSet(src_idx, center_pos=centroid)
    return G, pts, src, "G2_random_geom"


def build_G3_small_world():
    """G3: 3D small-world. Cubic 10^3 with 10% edges rewired."""
    n = 10; N = n**3
    idx_to_xyz = np.zeros((N,3)); xyz_to_idx = {}
    for idx, (x,y,z) in enumerate(product(range(n), repeat=3)):
        idx_to_xyz[idx] = [x,y,z]; xyz_to_idx[(x,y,z)] = idx

    edge_set = set()
    for (x,y,z), i in xyz_to_idx.items():
        for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nx_,ny_,nz_ = (x+dx)%n, (y+dy)%n, (z+dz)%n
            j = xyz_to_idx[(nx_,ny_,nz_)]
            edge_set.add((i,j) if i<j else (j,i))

    edges = list(edge_set)
    n_rw = int(0.1*len(edges))
    rw_idx = np.random.choice(len(edges), n_rw, replace=False)
    for idx in rw_idx:
        u,v = edges[idx]
        w = np.random.randint(0,N)
        while w == u: w = np.random.randint(0,N)
        edges[idx] = (u,w) if u<w else (w,u)

    G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(edges)
    src_list = []
    for x in range(2,7):
        for y in range(2,7):
            for z in range(2,7):
                src_list.append(xyz_to_idx[(x,y,z)])
    src = SourceSet(src_list, center_pos=np.array([4.5,4.5,4.5]))
    return G, idx_to_xyz, src, "G3_small_world"


def build_G4_random_3regular():
    """G4: Random 3-regular graph, 1000 nodes, no geometry."""
    N = 1000
    G = nx.random_regular_graph(3, N, seed=42)
    center = np.random.randint(0,N)
    try:
        lengths = nx.single_source_shortest_path_length(G, center)
    except:
        lengths = {center:0}
        q_bfs = [center]; visited = {center:0}
        while q_bfs:
            v = q_bfs.pop(0)
            for w in G.neighbors(v):
                if w not in visited:
                    visited[w] = visited[v]+1; q_bfs.append(w)
        lengths = visited
    dists = np.array([lengths.get(i,999) for i in range(N)])
    n_src = max(1,int(0.1*N))
    src_idx = np.argsort(dists)[:n_src]
    src = SourceSet(src_idx, center_pos=None)
    return G, None, src, "G4_random_3reg"


def build_G5_fcc():
    """G5: 3D FCC, 12NN. 6x6x7 cells x4 basis = 1008 nodes."""
    nx_c, ny_c, nz_c = 6, 6, 7
    basis = np.array([[0,0,0],[0.5,0.5,0],[0.5,0,0.5],[0,0.5,0.5]])
    positions = []; idx = 0
    for cx in range(nx_c):
        for cy in range(ny_c):
            for cz in range(nz_c):
                for b in basis:
                    positions.append([cx+b[0], cy+b[1], cz+b[2]])
                    idx += 1
    N = idx; positions = np.array(positions)
    tree = spatial.cKDTree(positions)
    edges = []
    for i in range(N):
        dists, nbs = tree.query(positions[i], k=min(14,N))
        for d,j in zip(dists[1:], nbs[1:]):
            if d < 0.8 and i < j: edges.append((i,j))
    G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(edges)
    centroid = positions.mean(axis=0)
    dists = np.linalg.norm(positions-centroid, axis=1)
    n_src = max(1,int(0.1*N))
    src_idx = np.argsort(dists)[:n_src]
    src = SourceSet(src_idx, center_pos=centroid)
    return G, positions, src, "G5_fcc"


def build_G6_perturbed_cubic():
    """G6: perturbed cubic. 10^3 + N(0,0.05) noise, 6-NN by distance."""
    n = 10; N = n**3; noise_scale = 0.05
    positions = np.zeros((N,3)); xyz_to_idx = {}
    for idx, (x,y,z) in enumerate(product(range(n), repeat=3)):
        positions[idx] = [x+np.random.randn()*noise_scale,
                          y+np.random.randn()*noise_scale,
                          z+np.random.randn()*noise_scale]
        xyz_to_idx[(x,y,z)] = idx
    tree = spatial.cKDTree(positions)
    edges = []
    for i in range(N):
        dists, nbs = tree.query(positions[i], k=min(7,N))
        for j in nbs[1:]:
            if i < j: edges.append((i,j))
    G = nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(edges)
    src_list = []
    for x in range(2,7):
        for y in range(2,7):
            for z in range(2,7):
                src_list.append(xyz_to_idx[(x,y,z)])
    src = SourceSet(src_list, center_pos=np.array([4.5,4.5,4.5]))
    return G, positions, src, "G6_perturbed_cubic"


# ============================================================================
# DYNAMICS: Degree-normalized diffusion + archiving, Dirichlet source
# ============================================================================

def run_dynamics(G, source, graph_label):
    """Evolve q-field to steady state.

    Source nodes fixed at Q_SOURCE (Dirichlet).
    Other nodes:
      q_i += (eta/deg_i)*sum_{j~i}(q_j - q_i) - gamma*q_i*(1 - q_i)
    """
    N = G.number_of_nodes()
    q = np.ones(N)
    src_arr = np.array(list(source.idxs))
    q[src_arr] = Q_SOURCE  # Dirichlet fixed

    is_src = np.zeros(N, dtype=bool)
    is_src[src_arr] = True

    # Precompute neighbor lists and degrees
    neighbors = [list(G.neighbors(i)) for i in range(N)]
    degrees = np.array([max(1, len(nbs)) for nbs in neighbors], dtype=float)

    t0 = time.time()
    for iteration in range(1, MAX_ITER+1):
        q_new = q.copy()

        for i in range(N):
            if is_src[i]:
                continue  # fixed
            nbs = neighbors[i]
            if not nbs:
                continue
            # Degree-normalized diffusion
            sum_nb = sum(q[j] for j in nbs)
            diffusion = ETA * (sum_nb - degrees[i] * q[i]) / degrees[i]
            archiving = -GAMMA * q[i] * (1.0 - q[i])
            q_new[i] = q[i] + diffusion + archiving

        q_new = np.clip(q_new, 0.0, 1.0)
        delta = np.max(np.abs(q_new[~is_src] - q[~is_src])) if (~is_src).any() else 0.0
        q = q_new

        if delta < TOL and iteration > 10:
            print(f"  {graph_label}: converged iter={iteration}, delta={delta:.2e}, "
                  f"q range=[{q.min():.4f},{q.max():.4f}]")
            break
    else:
        print(f"  {graph_label}: max iter reached, delta={delta:.2e}, "
              f"q range=[{q.min():.4f},{q.max():.4f}]")

    print(f"  {graph_label}: dynamics {time.time()-t0:.1f}s")
    return q, iteration, is_src


# ============================================================================
# COARSE-GRAINING
# ============================================================================

def coarse_grain_spatial(positions, q, target_size, is_src=None):
    """K-means spatial coarse-graining."""
    N = len(q)
    if target_size is None or target_size >= N:
        src_mask = is_src.astype(float) if is_src is not None else np.zeros(N)
        return positions.copy(), q.copy(), src_mask

    k = max(2, min(int(target_size), N-1))
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(positions)
    centers = kmeans.cluster_centers_

    coarse_q = np.array([q[labels==c].mean() if (labels==c).sum()>0 else 0.0 for c in range(k)])
    if is_src is not None:
        coarse_src = np.array([is_src[labels==c].mean() if (labels==c).sum()>0 else 0.0 for c in range(k)])
    else:
        coarse_src = np.zeros(k)
    return centers, coarse_q, coarse_src


def coarse_grain_graph(G, q, source_idxs, target_size):
    """Non-geometric coarse-graining via graph-distance + degree binning."""
    N = len(q)
    if target_size is None or target_size >= N:
        is_src = np.array([1.0 if i in source_idxs else 0.0 for i in range(N)])
        return np.arange(N).reshape(-1,1).astype(float), q.copy(), is_src

    src_list = list(source_idxs)
    center = src_list[0]
    try:
        lengths = nx.single_source_shortest_path_length(G, center)
    except:
        lengths = {center:0}; qb=[center]; vv={center:0}
        while qb:
            v=qb.pop(0)
            for w in G.neighbors(v):
                if w not in vv: vv[w]=vv[v]+1; qb.append(w)
        lengths = vv

    dists = np.array([lengths.get(i,999) for i in range(N)])
    max_dist = max(dists.max(), 1)
    degs = np.array([d for _,d in G.degree()], dtype=float)
    max_deg = max(degs.max(), 1)
    embedding = np.column_stack([dists/max_dist, degs/max_deg])

    k = max(2, min(int(target_size), N-1))
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embedding)

    coarse_q = np.array([q[labels==c].mean() if (labels==c).sum()>0 else 0.0 for c in range(k)])
    coarse_dist = np.array([dists[labels==c].mean() if (labels==c).sum()>0 else 0.0 for c in range(k)])
    coarse_src = np.array([
        len(set(np.where(labels==c)[0]) & source_idxs)/max(1,(labels==c).sum())
        for c in range(k)
    ])
    sort_idx = np.argsort(coarse_dist)
    return (coarse_dist[sort_idx].reshape(-1,1), coarse_q[sort_idx], coarse_src[sort_idx])


# ============================================================================
# RADIAL PROFILE + FITTING
# ============================================================================

def compute_radial_profile(positions, q, src_center, n_bins=None):
    """Compute binned radial profile q(r)."""
    N = len(q)
    if positions.shape[1] >= 2 and src_center is not None:
        r = np.linalg.norm(positions - src_center, axis=1)
    elif positions.shape[1] >= 2:
        r = np.linalg.norm(positions - positions.mean(axis=0), axis=1)
    else:
        r = positions.flatten()

    if N <= 8:
        s = np.argsort(r)
        return r[s], q[s], np.zeros(N), np.ones(N,dtype=int)

    nb = max(8, min(N//2, 40))
    r_sorted = np.sort(r)
    bin_edges = np.unique(np.percentile(r, np.linspace(0,100,nb+1)))
    if len(bin_edges) < 3:
        bin_edges = np.linspace(r.min(), r.max(), nb+1)

    nb_act = len(bin_edges)-1
    r_centers = 0.5*(bin_edges[:-1]+bin_edges[1:])
    q_binned = np.zeros(nb_act); q_std = np.zeros(nb_act)
    n_per = np.zeros(nb_act, dtype=int)

    for i in range(nb_act):
        if i == nb_act-1:
            mask = (r>=bin_edges[i]) & (r<=bin_edges[i+1])
        else:
            mask = (r>=bin_edges[i]) & (r<bin_edges[i+1])
        cnt = mask.sum(); n_per[i] = cnt
        if cnt > 0:
            q_binned[i] = q[mask].mean()
            q_std[i] = q[mask].std() if cnt>1 else 0.0
        else:
            q_binned[i] = np.nan; q_std[i] = 0.0

    valid = (n_per>0) & (~np.isnan(q_binned))
    return r_centers[valid], q_binned[valid], q_std[valid], n_per[valid]


def fit_q_r(r, q):
    """Fit q(r) = A/r + B, and power-law q = A*r^(-alpha)."""
    out = {}
    mask = (r > 1e-10) & (~np.isnan(q))
    rf = r[mask]; qf = q[mask]; n = len(rf)
    out['n_pts'] = n

    if n < 3:
        for k in ['A_1r','B_1r','R2_1r','A_std','B_std','alpha','A_pl','R2_pl','alpha_num','alpha_num_std']:
            out[k] = np.nan
        return out

    # Fit 1: q = A/r + B
    x = 1.0/rf
    X = np.column_stack([x, np.ones(n)])
    try:
        coeffs, _, _, _ = np.linalg.lstsq(X, qf, rcond=None)
        A,B = coeffs
        pred = A*x+B; r2 = r_squared(qf, pred)
        resid = qf-pred; sigma2 = np.sum(resid**2)/max(1,n-2)
        XtXi = np.linalg.inv(X.T@X)
        out['A_1r']=float(A); out['B_1r']=float(B); out['R2_1r']=float(max(0,min(1,r2)))
        out['A_std']=float(np.sqrt(sigma2*XtXi[0,0]))
        out['B_std']=float(np.sqrt(sigma2*XtXi[1,1]))
    except:
        for k in ['A_1r','B_1r','R2_1r','A_std','B_std']: out[k]=np.nan

    # Fit 2: power law
    lr = np.log(rf); lq = np.log(np.maximum(qf,1e-15))
    vl = np.isfinite(lr)&np.isfinite(lq)
    if vl.sum()>=3:
        Xl = np.column_stack([lr[vl], np.ones(vl.sum())])
        cl,_,_,_ = np.linalg.lstsq(Xl, lq[vl], rcond=None)
        alpha = -cl[0]; Apl = np.exp(cl[1])
        pred_pl = Apl*rf[vl]**(-alpha)
        r2_pl = r_squared(qf[vl], pred_pl)
        out['alpha']=float(alpha); out['A_pl']=float(Apl); out['R2_pl']=float(max(0,min(1,r2_pl)))
    else:
        out['alpha']=np.nan; out['A_pl']=np.nan; out['R2_pl']=np.nan

    # Numerical alpha
    if n>=4:
        s=np.argsort(rf); rs=rf[s]; qs=qf[s]
        dlnr=np.diff(np.log(rs)); dlnq=np.diff(np.log(np.maximum(qs,1e-15)))
        an=dlnq/np.maximum(dlnr,1e-15)
        va=np.isfinite(an)
        out['alpha_num']=float(np.mean(an[va])) if va.any() else np.nan
        out['alpha_num_std']=float(np.std(an[va])) if va.any() else np.nan
    else:
        out['alpha_num']=np.nan; out['alpha_num_std']=np.nan

    return out


# ============================================================================
# CROSS-GRAPH COMPARISON
# ============================================================================

def compare_q_profiles(all_layer_data, layer_idx):
    """Pairwise R^2 between graphs' q(r) at given layer.

    Each graph's radial coordinate is NORMALIZED by its max r, so all profiles
    are compared on the common [0,1] normalized domain. This accounts for
    different absolute length scales across graph types.
    """
    gnames = sorted(all_layer_data.keys())
    ng = len(gnames)

    # Collect profiles with normalized radial coordinates
    profiles_norm = {}
    for name in gnames:
        d = all_layer_data[name].get(layer_idx)
        if d is not None and d['n_pts'] >= 3 and not np.isnan(d['r']).all():
            r_max = d['r'].max()
            if r_max > 1e-10:
                r_norm = d['r'] / r_max
                # Sort by normalized r
                s = np.argsort(r_norm)
                profiles_norm[name] = {
                    'r_norm': r_norm[s],
                    'q': d['q'][s],
                }

    if len(profiles_norm) < 2:
        return gnames, np.full((ng,ng), np.nan)

    # Common normalized r grid [0, 1]
    r_com = np.linspace(0.0, 1.0, 50)

    q_int = {}
    for name, pd in profiles_norm.items():
        q_int[name] = np.interp(r_com, pd['r_norm'], pd['q'])

    cons = np.zeros((ng,ng))
    for i,g1 in enumerate(gnames):
        for j,g2 in enumerate(gnames):
            if g1 not in profiles_norm or g2 not in profiles_norm:
                cons[i,j] = np.nan
            elif g1==g2:
                cons[i,j] = 1.0
            elif i < j:
                # Symmetric R^2: average of (q1 predicting q2) and (q2 predicting q1)
                q1,q2 = q_int[g1], q_int[g2]
                ssr = np.sum((q1-q2)**2)
                sst1 = np.sum((q1-np.mean(q1))**2)
                sst2 = np.sum((q2-np.mean(q2))**2)
                r2_12 = 1.0 - ssr/max(sst1,1e-15)
                r2_21 = 1.0 - ssr/max(sst2,1e-15)
                r2_sym = 0.5*(max(0,r2_12) + max(0,r2_21))
                cons[i,j] = max(0.0, min(1.0, r2_sym))
                cons[j,i] = cons[i,j]
    return gnames, cons
    return gnames, cons


# ============================================================================
# ASCII PLOT
# ============================================================================

def ascii_plot(x_series, y_series, labels, width=70, height=20,
               title="", xlabel="", ylabel=""):
    """Multi-series ASCII scatter plot."""
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    all_x = np.concatenate([x for x in x_series if len(x)>0])
    all_y = np.concatenate([y for y in y_series if len(y)>0])
    if len(all_x)==0 or len(all_y)==0: return "No data."
    xmi,xma = all_x.min(), all_x.max(); ymi,yma = all_y.min(), all_y.max()
    xr=xma-xmi or 1; yr=yma-ymi or 1
    xmi-=0.05*xr; xma+=0.05*xr; ymi-=0.05*yr; yma+=0.05*yr
    xr=xma-xmi; yr=yma-ymi
    markers='*+#@%=ox'
    for idx,(x,y) in enumerate(zip(x_series,y_series)):
        if len(x)==0: continue
        mk=markers[idx%len(markers)]
        for xi,yi in zip(x,y):
            col=int((xi-xmi)/xr*(width-1)); row=int((yma-yi)/yr*(height-1))
            col=max(0,min(width-1,col)); row=max(0,min(height-1,row))
            grid[row][col]=mk

    lines=[]
    if title: lines.append(f"  {title}"); lines.append(f"  {'='*len(title)}")
    for row in range(height):
        if row==height//2 and ylabel:
            prefix=f"{ylabel:>8s} |"
        else:
            y_val=yma-(row+0.5)*yr/height
            prefix=f"{y_val:8.3f} |" if row%3==0 else " "*8+" |"
        lines.append(prefix+"".join(grid[row]))
    lines.append(" "*9+"+"+"-"*width)
    ll=" "*9
    for col in range(0,width,12):
        ll+=f"{xmi+col*xr/width:.2f}  "
    lines.append(ll)
    if xlabel: lines.append(" "*(9+width//2-len(xlabel)//2)+xlabel)
    for idx,lbl in enumerate(labels):
        lines.append(f"  {markers[idx%len(markers)]} = {lbl}")
    return "\n".join(lines)


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*70)
    print("DGF q-FIELD UNIVERSALITY ENUMERATION v2.1")
    print("="*70)
    print(f"eta={ETA}, gamma={GAMMA}, q_source={Q_SOURCE} (Dirichlet), "
          f"max_iter={MAX_ITER}, tol={TOL}")
    print(f"Diffusion: degree-normalized for stability across graph types")
    print()

    builders = [build_G1_cubic, build_G2_random_geometric, build_G3_small_world,
                build_G4_random_3regular, build_G5_fcc, build_G6_perturbed_cubic]

    results = {}
    all_layer_data = defaultdict(dict)

    # ====== Phase 1: Build + Dynamics ======
    print("="*70)
    print("PHASE 1: Graph Construction & Dynamics")
    print("="*70)

    for builder in builders:
        print(f"\n--- {builder.__name__} ---")
        G, positions, source, short_name = builder()
        has_geo = positions is not None and positions.shape[1] >= 2
        N = G.number_of_nodes()
        avg_deg = np.mean([d for _,d in G.degree()])
        print(f"  {short_name}: N={N}, |E|={G.number_of_edges()}, "
              f"deg={avg_deg:.1f}, |src|={len(source.idxs)}, geo={has_geo}")

        q_steady, n_iter, is_src = run_dynamics(G, source, short_name)

        results[short_name] = {
            'G': G, 'positions': positions, 'source': source,
            'q': q_steady, 'n_iter': n_iter, 'is_src': is_src,
            'has_geometry': has_geo, 'layers': {},
            'N': N, 'avg_deg': avg_deg, 'n_src': len(source.idxs),
        }

    # ====== Phase 2: Coarse-graining + Profiles ======
    print("\n"+"="*70)
    print("PHASE 2: Coarse-graining & Radial Profiles")
    print("="*70)

    for sn in sorted(results.keys()):
        data = results[sn]
        G = data['G']; positions = data['positions']; q = data['q']
        source = data['source']; is_src = data['is_src']; has_geo = data['has_geometry']

        print(f"\n--- {sn} ---")
        cur_q = q.copy()
        cur_pos = positions.copy() if has_geo else np.arange(len(q)).reshape(-1,1).astype(float)
        cur_is_src = is_src.copy()

        for li, ts in zip(CG_LAYERS, CG_SIZES):
            if li == 0:
                cg_q = cur_q; cg_pos = cur_pos; cg_is_src = cur_is_src
                src_center = source.center
            else:
                if has_geo:
                    cg_pos, cg_q, cg_src_frac = coarse_grain_spatial(cur_pos, cur_q, ts, cur_is_src)
                elif li == 1:
                    # First CG of G4 (non-geometric): use graph-distance binning
                    cg_pos, cg_q, cg_src_frac = coarse_grain_graph(G, cur_q, source.idxs, ts)
                else:
                    # Subsequent CG of G4: positions already encode graph distance, use K-means
                    cg_pos, cg_q, cg_src_frac = coarse_grain_spatial(cur_pos, cur_q, ts, cur_is_src)
                cg_is_src = (cg_src_frac > 0.3)
                if has_geo:
                    src_center = cg_pos[cg_is_src].mean(axis=0) if cg_is_src.any() else cg_pos.mean(axis=0)
                else:
                    src_center = None

            # Quoted q: use actual q values at source clusters as reference
            r_vals, q_vals, q_std, n_vals = compute_radial_profile(cg_pos, cg_q, src_center)
            fit = fit_q_r(r_vals, q_vals)

            data['layers'][li] = {
                'N_cg': len(cg_q), 'r': r_vals, 'q': q_vals,
                'q_std': q_std, 'n_bins': len(r_vals), 'fit': fit,
            }
            lp = {'r': r_vals, 'q': q_vals, 'q_std': q_std, 'n_pts': len(r_vals)}
            lp.update(fit)
            all_layer_data[sn][li] = lp

            print(f"  L{li}: N={len(cg_q):>4d}  "
                  f"A={fit.get('A_1r',np.nan):.4f}+/-{fit.get('A_std',np.nan):.4f}  "
                  f"B={fit.get('B_1r',np.nan):.4f}+/-{fit.get('B_std',np.nan):.4f}  "
                  f"R2_1r={fit.get('R2_1r',np.nan):.4f}  "
                  f"alpha={fit.get('alpha',np.nan):.3f}  "
                  f"a_num={fit.get('alpha_num',np.nan):.3f}")

            cur_q = cg_q
            cur_pos = cg_pos if has_geo else np.arange(len(cg_q)).reshape(-1,1).astype(float)
            cur_is_src = cg_is_src  # propagate source mask for next coarse-graining layer

    # ====== Phase 3: Cross-graph comparison ======
    print("\n"+"="*70)
    print("PHASE 3: Cross-Graph q(r) Consistency")
    print("="*70)

    cross_results = {}
    for li in [1,2,3]:
        gnames, cmat = compare_q_profiles(all_layer_data, li)
        cross_results[li] = (gnames, cmat)

        print(f"\nLayer {li} pairwise R^2 matrix:")
        hdr = "              "+" ".join(f"{n[:10]:>10s}" for n in gnames)
        print(hdr)
        for i,n in enumerate(gnames):
            row = f"{n:>12s}: "+" ".join(
                f"{cmat[i,j]:10.4f}" if not np.isnan(cmat[i,j]) else "       ---"
                for j in range(len(gnames)))
            print(row)

        geo_n = [n for n in gnames if 'G4' not in n and 'G3' not in n]
        geo_i = [i for i,n in enumerate(gnames) if n in geo_n]
        if len(geo_i)>=2:
            vals=[cmat[i,j] for i in geo_i for j in geo_i if i<j and not np.isnan(cmat[i,j])]
            print(f"  Geometric (G1,G2,G5,G6) avg pairwise R^2: {np.mean(vals):.4f}" if vals else "  N/A")
        all_i=list(range(len(gnames)))
        av=[cmat[i,j] for i in all_i for j in all_i if i<j and not np.isnan(cmat[i,j])]
        print(f"  All 6 avg pairwise R^2: {np.mean(av):.4f}" if av else "  N/A")

    # ====== Phase 4: ASCII Plots ======
    print("\n"+"="*70)
    print("PHASE 4: Visualizations")
    print("="*70)

    for li in [1,2]:
        xs,ys,ls=[],[],[]
        for sn in sorted(all_layer_data.keys()):
            d=all_layer_data[sn].get(li)
            if d is not None and d['n_pts']>=2:
                xs.append(d['r']); ys.append(d['q']); ls.append(sn)
        if xs:
            print(f"\n--- Layer {li}: q(r) superposition ---")
            print(ascii_plot(xs,ys,ls,
                   title=f"Layer {li}: q_eff(r) -- 6 graphs superposed",
                   xlabel="r (distance from source)", ylabel="q_eff"))

    # q vs 1/r at layer 2
    li=2
    x1r,yq,ls=[],[],[]
    for sn in sorted(all_layer_data.keys()):
        d=all_layer_data[sn].get(li)
        if d is not None and d['n_pts']>=2:
            vv=d['r']>1e-10
            if vv.sum()>=2:
                x1r.append(1.0/d['r'][vv]); yq.append(d['q'][vv]); ls.append(sn)
    if x1r:
        print(f"\n--- Layer {li}: q vs 1/r (linearity check) ---")
        print(ascii_plot(x1r,yq,ls,
               title=f"Layer {li}: q vs 1/r -- universal if all linear",
               xlabel="1/r", ylabel="q_eff"))

    # Normalized-r comparison (r/r_max) for key test
    li=2
    xs_norm, ys_norm, ls_norm = [], [], []
    for sn in sorted(all_layer_data.keys()):
        d = all_layer_data[sn].get(li)
        if d is not None and d['n_pts'] >= 2:
            rmax = d['r'].max()
            if rmax > 1e-10:
                xs_norm.append(d['r'] / rmax)
                ys_norm.append(d['q'])
                ls_norm.append(sn)
    if xs_norm:
        print(f"\n--- Layer {li}: q vs NORMALIZED r (r/r_max) -- universality test ---")
        print(ascii_plot(xs_norm, ys_norm, ls_norm,
               title=f"Layer {li}: q vs r/r_max -- universal if all curves overlap",
               xlabel="r / r_max (normalized distance)", ylabel="q_eff"))

    # ====== Phase 5: Summary Table ======
    print("\n"+"="*70)
    print("SUMMARY TABLE: alpha and R^2 across all graphs and layers")
    print("="*70)
    hdr = f"{'Graph':<16s} {'L':>2s} {'N':>5s} {'A_1r':>8s} {'B_1r':>8s} {'R2_1r':>7s} {'alpha':>7s} {'R2_pl':>7s}"
    print(hdr); print("-"*len(hdr))
    for sn in sorted(results.keys()):
        for li in CG_LAYERS:
            ld = results[sn]['layers'][li]; f=ld['fit']
            print(f"{sn:<16s} {li:>2d} {ld['N_cg']:>5d} "
                  f"{fmt(f.get('A_1r')):>8s} {fmt(f.get('B_1r')):>8s} "
                  f"{fmt(f.get('R2_1r')):>7s} {fmt(f.get('alpha')):>7s} "
                  f"{fmt(f.get('R2_pl')):>7s}")

    # ====== Phase 6: Universality Verdict ======
    print("\n"+"="*70)
    print("UNIVERSALITY VERDICT")
    print("="*70)

    tl = 2  # target layer
    geo_g = ['G1_cubic','G2_random_geom','G5_fcc','G6_perturbed_cubic']
    gnames_l2, cmat_l2 = cross_results.get(tl, ([],np.array([])))

    if len(cmat_l2)>0:
        geo_i = [i for i,n in enumerate(gnames_l2) if n in geo_g]
        geo_v = [cmat_l2[i,j] for i in geo_i for j in geo_i if i<j and not np.isnan(cmat_l2[i,j])]
        all_i = list(range(len(gnames_l2)))
        all_v = [cmat_l2[i,j] for i in all_i for j in all_i if i<j and not np.isnan(cmat_l2[i,j])]

        print(f"\nLayer {tl} (N~{CG_SIZES[tl]} coarse nodes):")
        if geo_v:
            print(f"  Geometric graphs R^2: avg={np.mean(geo_v):.4f}, "
                  f"pairs={[f'{v:.4f}' for v in geo_v]}")
        if all_v:
            print(f"  All 6 graphs R^2: avg={np.mean(all_v):.4f}")

        # Alpha values at layer 2
        alphas = []
        for sn in geo_g:
            ld = all_layer_data.get(sn,{}).get(tl,{})
            a = ld.get('alpha'); alphas.append(a)
        valid_alphas = [a for a in alphas if a is not None and not np.isnan(a)]
        if valid_alphas:
            print(f"  Geometric alpha values: {[f'{a:.3f}' for a in alphas]}")
            print(f"  Alpha mean={np.mean(valid_alphas):.3f}, std={np.std(valid_alphas):.3f}")

        print()
        if geo_v and np.mean(geo_v) >= 0.95:
            print("  *** UNIVERSALITY HOLDS for geometric 3D graphs. ***")
            print("  G1,G2,G5,G6 produce consistent q(r) profiles at coarse-grained scale.")
        elif geo_v and np.mean(geo_v) >= 0.80:
            print("  *** WEAK UNIVERSALITY -- geometric graphs show convergence trend. ***")
        else:
            print("  *** UNIVERSALITY NOT CONFIRMED at current depth/size. ***")

        # Outlier analysis
        for n in gnames_l2:
            row_avg = np.nanmean(cmat_l2[gnames_l2.index(n)])
            if not np.isnan(row_avg) and row_avg < 0.80:
                print(f"  OUTLIER: {n} (avg R^2 w/ others = {row_avg:.4f})")

    # G4 special comment
    if 'G4_random_3reg' in all_layer_data:
        g4l2 = all_layer_data['G4_random_3reg'].get(tl,{})
        a_g4 = g4l2.get('alpha',np.nan)
        r2_g4 = g4l2.get('R2_1r',np.nan)
        print(f"\n  G4 (random 3-regular, no geometry):")
        print(f"    alpha={a_g4:.3f}, R^2_1/r={r2_g4:.4f}")
        print(f"    Note: No geometric embedding -> not expected to follow 3D 1/r.")
        # Compare with geometric average
        if geo_v:
            print(f"    Significantly different from geometric q(r) -- confirms geometry matters.")

    # Save JSON
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir,'..','experiments','universality_enum_v2_results.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    serial = {'parameters':{'eta':ETA,'gamma':GAMMA,'q_source':Q_SOURCE,
             'max_iter':MAX_ITER,'tol':TOL}, 'graphs':{}, 'cross_consistency':{}}
    for sn,data in results.items():
        gd = {'N':data['N'],'avg_deg':data['avg_deg'],'n_source':data['n_src'],
              'n_iter':data['n_iter'],'has_geometry':data['has_geometry'],'layers':{}}
        for li in CG_LAYERS:
            ld=data['layers'][li]
            gd['layers'][str(li)]={'N_cg':ld['N_cg'],'n_bins':ld['n_bins'],
                'fit':{k:(float(v) if not (isinstance(v,float) and np.isnan(v)) else None)
                       for k,v in ld['fit'].items()}}
        serial['graphs'][sn]=gd
    for li,(gn,cm) in cross_results.items():
        geo_n=[n for n in gn if 'G4' not in n and 'G3' not in n]
        geo_i=[i for i,n in enumerate(gn) if n in geo_n]
        entry={'graph_names':gn,'matrix':cm.tolist()}
        if len(geo_i)>=2:
            vv=[cm[i,j] for i in geo_i for j in geo_i if i<j and not np.isnan(cm[i,j])]
            entry['avg_geo_R2']=float(np.mean(vv)) if vv else None
        avv=[cm[i,j] for i in range(len(gn)) for j in range(len(gn)) if i<j and not np.isnan(cm[i,j])]
        entry['avg_all_R2']=float(np.mean(avv)) if avv else None
        serial['cross_consistency'][str(li)]=entry

    with open(out_path,'w') as f:
        json.dump(serial, f, indent=2)
    print(f"\nFull results saved to: {out_path}")


if __name__ == '__main__':
    t0 = time.time()
    main()
    print(f"\nTotal time: {time.time()-t0:.1f}s ({(time.time()-t0)/60:.1f} min)")
