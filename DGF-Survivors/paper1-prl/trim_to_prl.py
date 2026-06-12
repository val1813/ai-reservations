"""Trim paper to PRL 4-page limit: delete 7 refs, Fig3, merge sections, compress."""
import re

with open(r'D:\Claude\ai-reservations\DGF-Survivors\paper1-prl\main.tex', encoding='utf-8') as f:
    text = f.read()

# ============================================================
# STEP 1: Delete Fig3 (evidence summary) — figure + caption
# ============================================================
text = re.sub(
    r'\\begin\{figure\}\[p\].*?\\includegraphics.*?fig3_evidence_summary.*?\\end\{figure\}',
    '', text, flags=re.DOTALL
)

# ============================================================
# STEP 2: Merge Physical Interpretation into Introduction
# Delete the section header and merge key sentences
# ============================================================
# Physical Interpretation section has: section header + 3 paragraphs
# Keep only the core idea: interferometer + gate algebra connection
text = text.replace(
    r'\section{Physical Interpretation}',
    ''
)

# ============================================================
# STEP 3: Compress Discussion
# ============================================================
# Giarmatzi-Costa paragraph -> one sentence
old_gc = r"Giarmatzi and Costa [15] established a general framework for witnessing quantum memory in non-Markovian processes via the process matrix formalism. Their parameter-mapping demonstration showed that gate structures control quantum memory. CFOL is a special case -- applied to $\exp(i\theta\,\sigma\otimes\sigma)$ with a causal ring topology -- yielding an exact iff condition on the Cartan angle. The quantum causal model literature [10,12--14] has established that cyclic structures produce correlations impossible in acyclic quantum circuits. Those works ask what correlations are compatible with a given cyclic structure. We ask what non-Markovianity is forced by that structure. The CFOL theorem provides an exact, quantitative condition on gate parameters that compatibility criteria alone do not capture."
new_gc = r"Giarmatzi and Costa [15] showed that entanglement witnesses in the process state map to quantum memory detection; CFOL is a special case yielding an exact iff condition on the Cartan angle. The quantum causal model literature [10,12--14] established that cyclic structures produce correlations impossible in acyclic circuits; our contribution is the exact quantitative condition on gate parameters that compatibility criteria alone do not provide."
text = text.replace(old_gc, new_gc)

# Qudit paragraph -> one sentence
old_qd = r"Generalization to qudits is not obvious. For $d>2$, the Cartan subalgebra has dimension $d-1$; the Cartan decomposition of arbitrary two-qudit unitaries follows the KAK parametrization [18]. The condition $c_j\in(\pi/2)\mathbb{Z}$ generalizes to a discrete subgroup of the higher-dimensional torus whose relationship to the qudit Pauli group has not been characterized."
new_qd = r"Whether the theorem extends to qudits ($d>2$) is open: the Cartan subalgebra has dimension $d-1$, and the discrete subgroup of the higher-dimensional torus corresponding to zero QCMI has not been characterized."
text = text.replace(old_qd, new_qd)

# ============================================================
# STEP 4: Delete 7 references and their citations
# Delete: [8] Zurek, [11] Huang, [18] Khaneja, [25] Elben, [29] Wilde, [30] Modi, [31] Li
# ============================================================
# Remove specific citations in text
# [8] — appears in "[8]" and ", yet does not address... [8]"
# Let me just remove the entire clause containing [8]
text = re.sub(
    r'\. The broader theory of decoherence and einselection \[8\] provides the conceptual foundation for understanding how environments monitor systems, yet does not address how the topology of the system-environment interaction graph constrains the resulting dynamics\.',
    '.',
    text
)

# [11] — appears as "[11]" in bootstrap sentence. Remove the cite but keep text.
text = text.replace('the mutual information estimator [11]', 'the mutual information estimator')

# [25] — appears as "[25]" in readout sentence
text = text.replace('was applied [25]', 'was applied')

# Remove [18] citation
text = re.sub(r'\[18\]\s*', '', text)  # KAK citation

# Remove [29] Wilde — not cited in body, just delete bibitem
# Remove [30] Modi — cited as "[30,31]"
text = text.replace('[30,31]', '')
# Remove [31] Li
# Remove [25] Elben from bib

# ============================================================
# STEP 5: Delete the 7 bibitems
# ============================================================
refs_to_delete = [8, 11, 18, 25, 29, 30, 31]
# Build bibitem patterns
for refnum in sorted(refs_to_delete, reverse=True):  # delete from highest to lowest to preserve line positions
    pattern = r'\\bibitem\{' + str(refnum) + r'\}.*?\n'  # delete the bibitem line
    text = re.sub(pattern, '', text, count=1)

# ============================================================
# STEP 6: Renumber remaining references
# ============================================================
# After deletion, we need to renumber bibitems and their citations
# Build shift map
remaining = sorted(set(range(1, 33)) - set(refs_to_delete))
shift = {}
new_num = 1
for old in remaining:
    shift[old] = new_num
    new_num += 1

# Fix bibitems
def fix_bibitem(m):
    n = int(m.group(1))
    return '\\bibitem{' + str(shift.get(n, n)) + '}'
text = re.sub(r'\\bibitem\{(\d+)\}', fix_bibitem, text)

# Fix bracket citations like [8], [1--3], [4,5], [19--22,26]
# These are manual brackets, not \cite{}. Find patterns like [digits] or [digits--digits] or [digits,digits]
def fix_bracket_cite(m):
    """Fix manual citation like [19--22,28] → renumbered"""
    content = m.group(1)
    parts = re.split(r'([\d]+)', content)
    res = []
    for p in parts:
        if p.isdigit():
            n = int(p)
            res.append(str(shift.get(n, n)))
        else:
            res.append(p)
    return '[' + ''.join(res) + ']'
text = re.sub(r'\[([\d,\-]+)\]', fix_bracket_cite, text)

# Clean up double spaces and empty brackets
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'\[\]', '', text)
text = re.sub(r'\.\s+\.', '.', text)
text = re.sub(r',\s*,', ',', text)

with open(r'D:\Claude\ai-reservations\DGF-Survivors\paper1-prl\main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

# Report
bibitems = re.findall(r'\\bibitem\{(\d+)\}', text)
cites_in_body = set()
for m in re.finditer(r'\[([\d,\-]+)\]', text):
    for p in re.split(r'\D+', m.group(1)):
        if p.isdigit():
            cites_in_body.add(int(p))
print(f"Remaining refs: {len(bibitems)} (last: {bibitems[-1]})")
print(f"Cited in body: {sorted(cites_in_body)}")
# Check for orphan refs
orphans = set(range(1, len(bibitems)+1)) - cites_in_body
if orphans:
    print(f"ORPHAN refs (not cited): {sorted(orphans)}")
else:
    print("All refs cited in body ✓")
