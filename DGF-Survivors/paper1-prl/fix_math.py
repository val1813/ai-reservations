"""Fix LaTeX inline math mode in main.tex."""
import re

with open('main.tex', encoding='utf-8') as f:
    text = f.read()

# Fix Greek letters not already in math mode
greek_map = {
    'θ': r'\theta', 'π': r'\pi', 'σ': r'\sigma',
    'η': r'\eta', 'ρ': r'\rho', 'Δ': r'\Delta',
    'ε': r'\varepsilon', 'φ': r'\phi', 'κ': r'\kappa',
    'α': r'\alpha', 'γ': r'\gamma', 'λ': r'\lambda',
    'Σ': r'\Sigma', 'Π': r'\Pi', 'χ': r'\chi',
}

for greek, latex_cmd in greek_map.items():
    # Only replace if not inside $...$ (not between $ signs)
    text = text.replace(greek, '$' + latex_cmd + '$')

# Fix double-wrapping: $$$\theta$$$ -> $\theta$
text = re.sub(r'\$\$\$([^$]+)\$\$\$', r'$\1$', text)
text = re.sub(r'\$\$([^$]+)\$\$', r'$\1$', text)

# Fix common special characters
text = text.replace('ℤ', r'$\mathbb{Z}$')
text = text.replace('⊗', r'$\otimes$')
text = text.replace('→', r'$\rightarrow$')
text = text.replace('∈', r'$\in$')
text = text.replace('∉', r'$\notin$')
text = text.replace('√', r'$\sqrt{}$')
text = text.replace('⟂', r'$\perp$')
text = text.replace('⟺', r'$\iff$')
text = text.replace('⋅', r'$\cdot$')
text = text.replace('×', r'$\times$')
text = text.replace('≈', r'$\approx$')
text = text.replace('±', r'$\pm$')
text = text.replace('∞', r'$\infty$')
text = text.replace('⟨', r'$\langle$')
text = text.replace('⟩', r'$\rangle$')

# Fix superscript numbers
text = re.sub(r'²', r'$^2$', text)
text = re.sub(r'⁴', r'$^4$', text)
text = re.sub(r'⁺', r'$^+$', text)
text = re.sub(r'⁻', r'$^-$', text)
text = re.sub(r'⁰', r'$^0$', text)
text = re.sub(r'³', r'$^3$', text)
text = re.sub(r'⁶', r'$^6$', text)
text = re.sub(r'ⁱ', r'$^i$', text)

# Fix subscript numbers
text = re.sub(r'₁', r'$_1$', text)
text = re.sub(r'₂', r'$_2$', text)
text = re.sub(r'₃', r'$_3$', text)
text = re.sub(r'₄', r'$_4$', text)
text = re.sub(r'₀', r'$_0$', text)
text = re.sub(r'ₐ', r'$_a$', text)
text = re.sub(r'ᵦ', r'$_b$', text)

# Fix n̂ -> \hat{n}
text = text.replace('n̂', r'$\hat{n}$')
text = text.replace('m̂', r'$\hat{m}$')

# Fix common pattern: $U_{uv}$ should work now with subscripts
# But need to handle _ in text mode
text = re.sub(r'(?<!\$)([A-Z])_(\{[^}]*\}|[a-zA-Z0-9]+)(?!\$)', r'$\1_\2$', text)

# Fix bare ^ in text
text = re.sub(r'(?<!\$)e\^\{i([^}]*)\}(?!\$)', r'$e^{i\1}$', text)

# Undo some over-wrapping: remove empty $ pairs
text = re.sub(r'\$\$', '', text)

# Fix specific known patterns that need manual attention
# Dirac notation
text = text.replace('|γ⟩', r'$|\gamma\rangle$')
text = text.replace('|+', r'$|+')
text = text.replace('|-', r'$|-')
text = text.replace('|Ψ⟩', r'$|\Psi\rangle$')
text = text.replace('|Φ⁺⟩', r'$|\Phi^+\rangle$')
text = text.replace('$|Φ$⁺$', r'$|\Phi^+\rangle$')

# Remove duplicate $ caused by multiple replacements
text = re.sub(r'\$([^$]{1,50}?)\$\$', r'$\1', text)
text = re.sub(r'\$\$([^$]{1,50}?)\$', r'\1$', text)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed math mode. Lines:', len(text.split('\n')))
