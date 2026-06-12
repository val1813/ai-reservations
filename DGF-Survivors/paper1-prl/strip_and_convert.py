"""Strip blueprint annotations and convert markdown to LaTeX."""
import re, os

def strip_blueprint(text):
    # Remove blueprint annotation lines: **[#N — ...]**
    text = re.sub(r'\*\*\[#\d+.*?\]\*\*\s*\n', '', text)
    # Remove inline blueprint annotations
    text = re.sub(r'\[#\d+.*?\]', '', text)
    return text

def md_to_latex(text, is_sm=False, is_cover=False):
    """Minimal markdown-to-LaTeX for PRL manuscript."""
    text = strip_blueprint(text)

    # Title (only in main manuscript)
    if not is_sm and not is_cover:
        text = re.sub(r'^# (.+)$', r'\\title{\1}', text, flags=re.M)

    # Author
    text = re.sub(r'^Zhongchang Huang$', r'\\author{Zhongchang Huang}', text, flags=re.M)
    text = re.sub(r'^Independent Researcher, Nanjing, China$',
                  r'\\affiliation{Independent Researcher, Nanjing, China}', text, flags=re.M)

    # Section headers
    text = re.sub(r'^## (.+)$', r'\\section{\1}', text, flags=re.M)

    # Remove horizontal rules
    text = re.sub(r'^---\s*$', '', text, flags=re.M)

    # Theorem environment
    text = re.sub(r'\*\*Theorem \((.+?)\)\.\*\*', r'\\begin{theorem}[\1]', text)
    text = re.sub(r'\*Proof sketch\.\*', r'\\begin{proof}[Proof sketch]', text)
    text = re.sub(r'∎', r'\\end{proof}', text)
    if '\\end{proof}' not in text and '\\begin{proof}' in text:
        text += '\n\\end{proof}'

    # Bold text (before italics)
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)

    # Italic text
    text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', text)
    text = re.sub(r'_(.+?)_', r'\\textit{\1}', text)

    # Inline math: $...$ stays as is

    # Display math: $$...$$ stays as is (amsmath compatible)

    # Subscripts and superscripts in text mode that aren't in math
    # (leave math mode alone)

    # References: [1] → handled by LaTeX bibliography
    # Keep reference section as-is, will use thebibliography

    # Greek letters in text mode → math mode
    # θ → $\theta$, π → $\pi$, etc.
    # But only outside math mode
    def replace_greek(match):
        char = match.group(0)
        greek_map = {'θ': r'$\theta$', 'π': r'$\pi$', 'η': r'$\eta$',
                     'σ': r'$\sigma$', 'ρ': r'$\rho$', 'ℤ': r'$\mathbb{Z}$',
                     'Δ': r'$\Delta$', 'ε': r'$\varepsilon$'}
        return greek_map.get(char, char)

    # Don't replace inside math mode or existing $...$
    # Simple approach: only replace standalone greek letters

    # Tables
    text = re.sub(r'^\|(.+)\|$', lambda m: '\\begin{tabular}{' + 'c' * (m.group(1).count('|')-1) + '}\n' +
                  m.group(0).replace('|', ' & ').replace(' &  ', ' \\\\\n') + '\n\\end{tabular}', text, flags=re.M)

    # References
    if '## REFERENCES' in text:
        text = text.replace('## REFERENCES', '\\begin{thebibliography}{99}')
        # Convert [N] Author... to \bibitem{N} Author...
        text = re.sub(r'\[(\d+)\]\s+', r'\\bibitem{\1} ', text)
        # Close thebibliography at end of file
        text = text.rstrip() + '\n\\end{thebibliography}\n'

    return text

def process_manuscript(text):
    """Process main manuscript."""
    latex = []
    latex.append(r'\documentclass[twocolumn,aps,prl,showpacs]{revtex4-2}')
    latex.append(r'\usepackage{amsmath,amssymb,graphicx}')
    latex.append(r'\begin{document}')
    latex.append(r'\preprint{APS/123-QED}')
    latex.append('')

    # Extract title, author, abstract, body
    stripped = strip_blueprint(text)

    lines = stripped.split('\n')
    title_done = False
    author_done = False
    in_abstract = False
    in_refs = False
    body_lines = []
    abstract_lines = []
    ref_lines = []

    for line in lines:
        if line.startswith('# ') and not title_done:
            title = line[2:].strip()
            latex.append(r'\title{' + title + '}')
            title_done = True
            continue
        if line.strip() == 'Zhongchang Huang':
            latex.append(r'\author{Zhongchang Huang}')
            continue
        if line.strip() == 'Independent Researcher, Nanjing, China':
            latex.append(r'\affiliation{Independent Researcher, Nanjing, China}')
            continue
        if line.strip() == '## ABSTRACT':
            in_abstract = True
            continue
        if line.strip() == '## INTRODUCTION':
            in_abstract = False
            latex.append(r'\begin{abstract}')
            latex.append(' '.join(abstract_lines).strip())
            latex.append(r'\end{abstract}')
            latex.append('')
            latex.append(r'\maketitle')
            latex.append('')
            latex.append(r'\section{Introduction}')
            continue
        if line.strip() == '## REFERENCES':
            in_refs = True
            continue
        if in_abstract:
            if line.strip():
                abstract_lines.append(line.strip())
            continue
        if in_refs:
            ref_lines.append(line)
            continue

        # Section handling
        if line.startswith('## ') and not in_refs:
            sec_name = line[3:].strip()
            # Map to proper LaTeX sections
            if sec_name.upper() in ['INTRODUCTION', 'CAUSAL RING MODEL', 'CFOL THEOREM',
                                      'PHYSICAL INTERPRETATION', 'SCALING LAW',
                                      'EXPERIMENTAL TESTS', 'DISCUSSION', 'CONCLUSION']:
                if sec_name.upper() == 'CAUSAL RING MODEL':
                    latex.append(r'\section{Causal Ring Model}')
                elif sec_name.upper() == 'CFOL THEOREM':
                    latex.append(r'\section{CFOL Theorem}')
                elif sec_name.upper() == 'PHYSICAL INTERPRETATION':
                    latex.append(r'\section{Physical Interpretation}')
                elif sec_name.upper() == 'SCALING LAW':
                    latex.append(r'\section{Scaling Law}')
                elif sec_name.upper() == 'EXPERIMENTAL TESTS':
                    latex.append(r'\section{Experimental Tests}')
                elif sec_name.upper() == 'DISCUSSION':
                    latex.append(r'\section{Discussion}')
                elif sec_name.upper() == 'CONCLUSION':
                    latex.append(r'\section{Conclusion}')
            continue

        if line.startswith('**Theorem'):
            latex.append(r'\begin{theorem}[CFOL]')
            # Extract theorem content
            theorem_text = line.replace('**Theorem (Causal Faithfulness of Orthogonal Lie-algebra — CFOL).**', '').strip()
            latex.append(theorem_text)
            continue

        if line.startswith('*Proof sketch.*'):
            latex.append(r'\begin{proof}[Proof sketch]')
            proof_text = line.replace('*Proof sketch.*', '').strip()
            if proof_text:
                latex.append(proof_text)
            continue

        if '∎' in line:
            line = line.replace('∎', '')
            latex.append(line)
            latex.append(r'\end{proof}')
            continue

        if line.startswith('$$'):
            latex.append(line)
            continue

        # Regular text
        if line.strip():
            latex.append(line)
        else:
            latex.append('')

    # Add references
    if ref_lines:
        latex.append(r'\begin{thebibliography}{99}')
        for line in ref_lines:
            line = line.strip()
            if not line:
                continue
            m = re.match(r'\[(\d+)\]\s+(.+)', line)
            if m:
                num, ref = m.groups()
                latex.append(r'\bibitem{' + num + '} ' + ref)
        latex.append(r'\end{thebibliography}')

    latex.append(r'\end{document}')
    return '\n'.join(latex)

def process_sm(text):
    """Process Supplemental Material."""
    latex = []
    latex.append(r'\documentclass[aps,prl,showpacs]{revtex4-2}')
    latex.append(r'\usepackage{amsmath,amssymb,graphicx}')
    latex.append(r'\begin{document}')
    latex.append(r'\title{Supplemental Material: Causal Topology Enforces Quantum Non-Markovianity}')
    latex.append(r'\author{Zhongchang Huang}')
    latex.append(r'\affiliation{Independent Researcher, Nanjing, China}')
    latex.append(r'\date{\today}')
    latex.append(r'\maketitle')
    latex.append('')

    stripped = strip_blueprint(text)
    lines = stripped.split('\n')
    skip_until_body = True

    for line in lines:
        if line.startswith('# '):
            skip_until_body = False
            continue
        if skip_until_body:
            continue
        if line.startswith('## S1.'):
            latex.append(r'\section{Full CFOL Proof}')
            continue
        if line.startswith('## S2.'):
            latex.append(r'\section{Gram Matrix Factorization}')
            continue
        if line.startswith('## S3.'):
            latex.append(r'\section{Numerical Verification}')
            continue
        if line.startswith('## S4.'):
            latex.append(r'\section{Scaling Law Derivation}')
            continue
        if line.startswith('## S5.'):
            latex.append(r'\section{Experimental Protocols}')
            continue
        if line.startswith('## S6.'):
            latex.append(r'\section{Error Budget Analysis}')
            continue
        if line.startswith('**Table'):
            latex.append(r'\begin{table}[h]')
            latex.append(r'\caption{' + line.replace('**', '').replace('.**', '') + '}')
            continue
        if line.startswith('---'):
            continue

        # Bold text
        line = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)

        if line.strip():
            latex.append(line)
        else:
            latex.append('')

    latex.append(r'\end{document}')
    return '\n'.join(latex)

def process_cover(text):
    """Process Cover Letter — keep as plain text with minimal formatting."""
    stripped = strip_blueprint(text)
    # Also strip [S1 — W=...] style annotations
    stripped = re.sub(r'\[S\d+\s*[—–-]\s*W=\d+.*?\]\s*', '', stripped)
    return stripped

# Read files
base = r'D:\Claude\ai-reservations\DGF-Survivors'
outdir = os.path.join(base, 'paper1-prl')

for fname, proc_func, out_name in [
    ('S1_PRL_manuscript.md', process_manuscript, 'main.tex'),
    ('S1_PRL_SM.md', process_sm, 'supplemental.tex'),
    ('S1_PRL_cover_letter.md', process_cover, 'cover_letter.txt'),
]:
    with open(os.path.join(base, fname), encoding='utf-8') as f:
        text = f.read()
    result = proc_func(text)
    outpath = os.path.join(outdir, out_name)
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'{out_name}: {len(result)} chars → {outpath}')

print('Done.')
