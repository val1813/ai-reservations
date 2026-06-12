import re

with open(r'D:\Claude\ai-reservations\DGF-Survivors\paper1-prl\main.tex', encoding='utf-8') as f:
    text = f.read()

shift = {25:23, 26:24, 27:25, 28:26, 29:27, 30:28, 31:29}

# Fix \bibitem{N}
def fb(m):
    n = int(m.group(1))
    ns = shift.get(n, n)
    return '\\bibitem{' + str(ns) + '}'
text = re.sub(r'\\bibitem\{(\d+)\}', fb, text)

# Fix \cite{...}
def fc(m):
    content = m.group(1)
    parts = re.split(r'(\d+)', content)
    res = []
    for p in parts:
        if p.isdigit():
            n = int(p)
            res.append(str(shift.get(n, n)))
        else:
            res.append(p)
    return '\\cite{' + ''.join(res) + '}'
text = re.sub(r'\\cite\{([^}]+)\}', fc, text)

with open(r'D:\Claude\ai-reservations\DGF-Survivors\paper1-prl\main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

refs = re.findall(r'\\bibitem\{(\d+)\}', text)
print(f'Total refs: {len(refs)}, Last: {refs[-1]}')
cites = set()
for m in re.finditer(r'\\cite\{([^}]+)\}', text):
    for p in re.split(r'\D+', m.group(1)):
        if p.isdigit():
            cites.add(int(p))
print(f'Cited refs: {sorted(cites)}')
