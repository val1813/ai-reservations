import re, numpy as np, sys

with open('D:/Claude/ai-reservations/LP32-how to destroy a universe/prl/prl_s1_final.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Strip LaTeX commands
for cmd in ['begin{equation}', 'end{equation}', 'begin{quote}', 'end{quote}',
            'begin{enumerate}', 'end{enumerate}', 'begin{itemize}', 'end{itemize}',
            'begin{abstract}', 'end{abstract}', 'section{', 'subsection{',
            'textbf{', 'emph{', 'end{thebibliography}']:
    text = text.replace('\\' + cmd, ' ')

text = re.sub(r'\\[a-zA-Z]+\{', ' ', text)
text = text.replace('{', ' ').replace('}', ' ')
text = re.sub(r'\$[^$]*\$', ' ', text)
text = re.sub(r'\\[a-zA-Z]+', ' ', text)
text = re.sub(r'\s+', ' ', text)

sentences = re.split(r'(?<=[.!?])\s+', text)
sentences = [s.strip() for s in sentences if len(s.split()) > 4 and any(c.isalpha() for c in s)]

sent_lens = [len(s.split()) for s in sentences]
print(f'Total sentences: {len(sentences)}')
print(f'Mean sent len: {np.mean(sent_lens):.1f} (PRL benchmark: 22.5)')
print(f'Std sent len: {np.std(sent_lens):.1f} (PRL: 9.8)')
simple = sum(1 for s in sentences if ',' not in s)
print(f'Simple (no commas): {simple}/{len(sentences)} = {simple/len(sentences)*100:.0f}% (PRL: 29%)')

txt = text.lower()
for pat in ['neither supplies', 'the answer is', 'surprisingly simple',
            'does not stand alone', 'we do not claim nature', 'without einselection',
            'what makes the bound', 'without both the bound']:
    if pat in txt:
        print(f'AI-ism: "{pat}"')

for t in ['furthermore', 'moreover', 'crucially', 'notably']:
    c = txt.count(t)
    if c > 0:
        print(f'Dense transition "{t}": {c}x (PRL avg: 0.3-0.4/paper)')

print('\nSample:')
for s in sentences[:6]:
    print(f'  [{len(s.split())}w] {s[:130]}')
