import numpy as np

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho); eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals); return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    n=len(dims); d_total=int(np.prod(dims))
    trace_out=[i for i in range(n) if i not in keep]
    dk=int(np.prod([dims[i] for i in keep]))
    result=np.zeros((dk,dk),dtype=complex)
    for bra in range(d_total):
        bra_bits=[(bra>>i)&1 for i in range(n)]
        bt=tuple(bra_bits[i] for i in trace_out)
        bk=tuple(bra_bits[i] for i in keep)
        bki=sum(bk[i]*(2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits=[(ket>>i)&1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out)==bt:
                kk=tuple(ket_bits[i] for i in keep)
                kki=sum(kk[i]*(2**i) for i in range(len(keep)))
                result[bki,kki]+=rho[bra,ket]
    return result

def embed_lsb(U2q, a, b, nq=4):
    D=2**nq; P=np.zeros((D,D),dtype=complex)
    rem=[i for i in range(nq) if i not in(a,b)]
    for i in range(D):
        bi=[(i>>k)&1 for k in range(nq)]
        pb=[bi[a],bi[b]]+[bi[r] for r in rem]
        j=sum(pb[k]*(1<<k) for k in range(nq))
        P[j,i]=1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2),dtype=complex),U2q) @ P

def h2(x):
    if x<=0 or x>=1: return 0
    return -x*np.log2(x) - (1-x)*np.log2(1-x)

CNOT_LSB=np.zeros((4,4),dtype=complex)
CNOT_LSB[0,0]=1;CNOT_LSB[3,1]=1;CNOT_LSB[2,2]=1;CNOT_LSB[1,3]=1
UQE_CNOT = embed_lsb(CNOT_LSB,0,3)@embed_lsb(CNOT_LSB,1,3)@embed_lsb(CNOT_LSB,1,2)@embed_lsb(CNOT_LSB,0,2)
dims=[2]*6; IR4=np.eye(4,dtype=complex)

print("CNOT cycle: numerical vs analytic formula")
print("  Formula: QCMI = h2((1+4p(1-p))/2)")
print(f"  {'p':>8s}  {'numeric':>10s}  {'analytic':>10s}  {'delta':>10s}")
for p in np.linspace(0.01, 0.99, 15):
    q=1-p; sqrt_p=np.sqrt(p); sqrt_q=np.sqrt(q)
    psi0=np.zeros(64,dtype=complex)
    for a in[0,1]:
        for b in[0,1]:
            for e1 in[0,1]:
                for e2 in[0,1]:
                    amp=0.5*(sqrt_p if e1==0 else sqrt_q)*(sqrt_p if e2==0 else sqrt_q)
                    psi0[(a<<0)|(b<<1)|(a<<2)|(b<<3)|(e1<<4)|(e2<<5)]=amp
    rho0=np.outer(psi0,psi0.conj())
    rf=np.kron(UQE_CNOT,IR4)@rho0@np.kron(UQE_CNOT,IR4).conj().T
    SE=vn_entropy(ptrace(rf,[4,5],dims))
    rQ=ptrace(rf,[2,3],dims); rRQ=ptrace(rf,[0,1,2,3],dims)
    rR=ptrace(rf,[0,1],dims); rQE=ptrace(rf,[2,3,4,5],dims)
    SR=vn_entropy(rR); SQ=vn_entropy(rQ); SRQ=vn_entropy(rRQ); SQE=vn_entropy(rQE)
    QCMI = (SR+SQE-vn_entropy(rf)) - (SR+SQ-SRQ)
    x = 4*p*q; analytic = h2((1+x)/2)
    print(f"  {p:8.3f}  {QCMI:10.6f}  {analytic:10.6f}  {abs(QCMI-analytic):10.2e}")
