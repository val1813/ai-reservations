import random
import math

seed = random.randint(1, 99999)
random.seed(seed)
print(f"SEED: {seed}")

sections = {
    "Introduction": 4,
    "Causal Ring Model": 2,
    "CFOL — Physical Interpretation": 2,
    "Scaling Law": 3,
    "Experimental Tests": 3,
    "Discussion": 3,
    "Conclusion": 1,
}

all_paras = []
for sec_name, n in sections.items():
    for i in range(n):
        all_paras.append({
            "section": sec_name, "idx": i,
            "is_conclusion": sec_name == "Conclusion",
            "is_discussion": sec_name == "Discussion",
            "is_intro": sec_name == "Introduction",
            "is_results": sec_name in ["Scaling Law", "Experimental Tests"],
        })

def generate_blueprint(all_paras):
    paras = []
    for p in all_paras:
        para = {}
        if p["is_conclusion"]:
            para["S"] = random.randint(3, 5)
        elif p["is_discussion"]:
            para["S"] = random.choice([2, 3, 4, 5, 7, 8])
        elif p["is_intro"]:
            para["S"] = random.randint(4, 10)
        else:
            para["S"] = random.randint(2, 8)

        if p["is_conclusion"]:
            para["T"] = random.choice([1, 6])
        elif p["is_discussion"]:
            para["T"] = random.choice([1, 2, 4, 5, 6])
        else:
            para["T"] = random.randint(1, 6)

        para["P"] = random.choices([1, 2, 3, 4, 5], weights=[37, 22, 18, 12, 11])[0]
        para["K"] = random.choices([0, 1, 2, 3], weights=[30, 35, 25, 10])[0]
        para["W"] = random.randint(10, 24)
        if p["is_conclusion"]:
            para["E"] = random.choice([1, 4])
        else:
            para["E"] = random.choices([1, 2, 3, 4], weights=[40, 25, 20, 15])[0]
        if p["is_intro"] and p["idx"] <= 1:
            para["D"] = random.choice([2, 3])
        else:
            para["D"] = random.choices([1, 2, 3], weights=[35, 45, 20])[0]
        para["C"] = random.choices([0, 1, 2], weights=[40, 40, 20])[0]
        if p["is_intro"] and p["idx"] <= 2:
            para["R"] = random.randint(2, 4)
        elif p["is_results"]:
            para["R"] = random.randint(0, 1)
        else:
            para["R"] = random.choices([0, 1, 2, 3, 4], weights=[30, 35, 20, 10, 5])[0]
        if p["is_conclusion"]:
            para["V"] = random.choice([1, 2])
        elif p["is_discussion"] and p["idx"] == 2:
            para["V"] = 4
        else:
            para["V"] = random.choices([1, 2, 3, 4], weights=[50, 20, 20, 10])[0]
        para["F"] = random.choices([0, 1, 2], weights=[50, 35, 15])[0]
        para["B"] = 1 if random.random() < 0.15 else 0
        para["L"] = random.choices([0, 1, 2, 3], weights=[30, 25, 25, 20])[0]
        para["H"] = random.choices(["S", "L", "H_var"], weights=[25, 45, 30])[0]
        paras.append(para)
    return paras

def validate(paras, all_paras):
    errors = []
    S_vals = [p["S"] for p in paras]
    W_vals = [p["W"] for p in paras]
    T_vals = [p["T"] for p in paras]
    D_vals = [p["D"] for p in paras]
    V_vals = [p["V"] for p in paras]
    E_vals = [p["E"] for p in paras]

    s_mean = sum(S_vals) / len(S_vals)
    w_mean = sum(W_vals) / len(W_vals)
    s_std = math.sqrt(sum((s - s_mean)**2 for s in S_vals) / len(S_vals))
    w_std = math.sqrt(sum((w - w_mean)**2 for w in W_vals) / len(W_vals))

    if s_std < 2.5:
        errors.append("S std < 2.5")
    if w_std < 4.0:
        errors.append("W std < 4.0")
    if max(S_vals) - min(S_vals) < 6:
        errors.append("S range < 6")
    if max(W_vals) - min(W_vals) < 10:
        errors.append("W range < 10")

    for i in range(len(T_vals)-1):
        if T_vals[i] == T_vals[i+1]:
            errors.append(f"Adjacent T repeat at {i}")
    for i in range(len(D_vals)-2):
        if D_vals[i] == 1 and D_vals[i+1] == 1 and D_vals[i+2] == 1:
            errors.append(f"3x H density at {i}")
    for i in range(len(S_vals)-2):
        if max(S_vals[i:i+3]) - min(S_vals[i:i+3]) < 3:
            errors.append(f"S tight at {i}")
    for i in range(len(W_vals)-2):
        if max(W_vals[i:i+3]) - min(W_vals[i:i+3]) < 4:
            errors.append(f"W tight at {i}")

    for t in range(1, 7):
        if T_vals.count(t) / len(T_vals) > 0.35:
            errors.append(f"T={t} too frequent")
    if E_vals.count(3) > 3:
        errors.append("E=3 > 3")
    if V_vals.count(1) / len(V_vals) > 0.70:
        errors.append("V=1 > 70%")
    if V_vals.count(3) < 2:
        errors.append("V=3 < 2")
    if V_vals.count(4) < 1 or V_vals.count(4) > 2:
        errors.append("V=4 not 1-2")
    if sum(1 for p in paras if p["F"] == 0) / len(paras) > 0.60:
        errors.append("F=0 > 60%")
    b_count = sum(1 for p in paras if p["B"] == 1)
    if b_count < 2 or b_count > 4:
        errors.append(f"B=1 count {b_count} not 2-4")
    if sum(1 for p in paras if p["L"] == 0) / len(paras) < 0.30:
        errors.append("L=0 < 30%")
    if sum(1 for p in paras if p["H"] == "S") / len(paras) > 0.30:
        errors.append("H=S > 30%")
    if sum(1 for p in paras if p["H"] == "H_var") / len(paras) < 0.20:
        errors.append("H=H_var < 20%")

    for arr_name, arr in [("S", S_vals), ("T", T_vals), ("W", W_vals), ("D", D_vals)]:
        for period in [2, 3, 4]:
            matches = sum(1 for i in range(len(arr)-period) if arr[i] == arr[i+period])
            if matches / (len(arr)-period) > 0.6:
                errors.append(f"{arr_name} period {period}")

    for i, p in enumerate(paras):
        if p["T"] == 3 and p["E"] == 3:
            errors.append(f"T=3,E=3 at {i}")

    for i in range(len(T_vals)-2):
        if T_vals[i] == T_vals[i+1] == T_vals[i+2]:
            errors.append(f"T repeat 3x at {i}")

    intro_last = max(i for i, ap in enumerate(all_paras) if ap["section"] == "Introduction")
    if paras[intro_last]["T"] == 3:
        errors.append("Intro last T=3")

    c_total = sum(p["C"] for p in paras)
    if c_total > len(paras) * 0.8:
        errors.append("C total high")

    return errors

best_paras = None
best_errors = None
best_score = 999
for attempt in range(200):
    paras = generate_blueprint(all_paras)
    errors = validate(paras, all_paras)
    if len(errors) == 0:
        best_paras = paras
        best_errors = []
        break
    if len(errors) < best_score:
        best_score = len(errors)
        best_paras = paras
        best_errors = errors

if best_errors:
    print(f"WARNING: Best attempt has {len(best_errors)} errors after 200 attempts")
    for e in best_errors[:10]:
        print(f"  - {e}")
    print()

paras = best_paras

print("=" * 80)
print("STRUCTURE BLUEPRINT")
print(f"SEED: {seed} | Paragraphs: {len(paras)}")
print("=" * 80)

sec_names = list(sections.keys())
para_idx = 0
for sec_name in sec_names:
    n = sections[sec_name]
    print(f"\n### {sec_name} ({n} paras)")
    print(f"| # | S | T | P | K | W | E | D | C | R | V | F | B | L | H |")
    print(f"|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i in range(n):
        p = paras[para_idx]
        print(f"| {para_idx+1} | {p['S']} | {p['T']} | {p['P']} | {p['K']} | {p['W']} | {p['E']} | {p['D']} | {p['C']} | {p['R']} | {p['V']} | {p['F']} | {p['B']} | {p['L']} | {p['H']} |")
        para_idx += 1

print(f"\n## Global Validation")
S_vals = [p["S"] for p in paras]
W_vals = [p["W"] for p in paras]
T_vals = [p["T"] for p in paras]
D_vals = [p["D"] for p in paras]
V_vals = [p["V"] for p in paras]
E_vals = [p["E"] for p in paras]

s_mean = sum(S_vals)/len(S_vals)
w_mean = sum(W_vals)/len(W_vals)
s_std = math.sqrt(sum((s-s_mean)**2 for s in S_vals)/len(S_vals))
w_std = math.sqrt(sum((w-w_mean)**2 for w in W_vals)/len(W_vals))

print(f"S: mean={s_mean:.1f}, std={s_std:.1f}, range=[{min(S_vals)},{max(S_vals)}] diff={max(S_vals)-min(S_vals)}")
print(f"W: mean={w_mean:.1f}, std={w_std:.1f}, range=[{min(W_vals)},{max(W_vals)}] diff={max(W_vals)-min(W_vals)}")
print(f"T: { {t:T_vals.count(t) for t in range(1,7)} }")
print(f"D: H={D_vals.count(1)} M={D_vals.count(2)} L={D_vals.count(3)}")
print(f"V: { {v:V_vals.count(v) for v in range(1,5)} }")
print(f"E: { {e:E_vals.count(e) for e in range(1,5)} }")
adj_t = sum(1 for i in range(len(T_vals)-1) if T_vals[i]==T_vals[i+1])
print(f"Adjacent T repeats: {adj_t}")
print(f"B=1: {sum(1 for p in paras if p['B']==1)}")
print(f"F=0: {sum(1 for p in paras if p['F']==0)/len(paras):.0%}")
print(f"L=0: {sum(1 for p in paras if p['L']==0)/len(paras):.0%}")
print(f"H=S: {sum(1 for p in paras if p['H']=='S')/len(paras):.0%}")
print(f"H=H_var: {sum(1 for p in paras if p['H']=='H_var')/len(paras):.0%}")
print(f"C total: {sum(p['C'] for p in paras)}")
est_words = sum(p["S"] * p["W"] for p in paras)
print(f"Estimated words: {est_words}")
print(f"STATUS: {'PASS' if not best_errors else 'MINOR VIOLATIONS'}")
