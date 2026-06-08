# Nature Physics May 2026 — Writing Pattern Analysis

## Papers analyzed
1. Calugaru et al. "Observation of an obstructed atomic band in a TMD" (pp 686-691)
2. Zhao et al. "Wetting by active fluids" (pp 805-811)  
3. Tu et al. "Symmetry-broken Kondo screening in kagome superconductor" (pp 698-705)
4. Radovskaia et al. "Photoengineering magnon spectrum in AFM" (pp 728-735)

---

## 1. STRUCTURE PATTERN (universal across all 4)

```
ABSTRACT (~200 words)
  - Sentence 1-2: Broad context / why it matters
  - Sentence 3-4: The gap / what hasn't been done  
  - "Here we [verb]..." — the contribution
  - 2-3 sentences: how we did it + key result
  - Closing: broader implication

INTRODUCTION (~800-1000 words, no section header)
  - ¶1: Wide context — field significance
  - ¶2: Narrow to specific problem / gap
  - ¶3: What's been tried, why it's insufficient
  - ¶4: "In this work, we..." — clear statement of contribution
  - NO "This paper is organized as follows"

RESULTS AND DISCUSSION (merged, no separate Discussion header in some)
  - Flowing narrative with sub-headings
  - Each subsection: one key finding
  - Figures integrated inline (not at end)
  - "We find/observe/show/demonstrate" — active voice

CONCLUSIONS / DISCUSSION (2-5 paragraphs)
  - Summary of contributions (past tense: "We have shown...")
  - Broader implications ("Our results suggest/indicate...")
  - Future directions ("calls for further investigation")
  - NEVER: "More work is needed" (too weak)
  - INSTEAD: specific next steps ("Our observation calls for systematic investigation of X using Y")

METHODS (at end, before references)
  - Subheadings for each technique
  - Past tense, passive or "we" voice
  - Error analysis, statistics, code/data availability
```

## 2. SENTENCE-LEVEL PATTERNS

### Opening sentences of Introduction (real examples):

| Paper | Opening |
|-------|---------|
| 1 | "The topology of electron wavefunctions has become a central theme in modern condensed matter physics." |
| 2 | "The Young–Dupre equation describes the equilibrium wetting of a macroscopic liquid droplet on a solid surface as illustrated in Fig. 1a." |
| 3 | "Quantum states of matter reorganize themselves in response to defects, giving rise to emergent local excitations that reflect the intrinsic properties of the underlying phases." |
| 4 | "Femtosecond light pulses lead the exploration of spin dynamics in antiferromagnets (AFMs), materials with antiparallel spin ordering." |

**Pattern:** Direct, declarative. States what IS known. No "It is well known that..." or "Recently, there has been growing interest in..."

### Gap sentences (how they identify what's missing):

- "Despite extensive theoretical predictions, the unambiguous quantitative experimental identification of [X] has not yet been achieved." (Paper 1)
- "So far, however, a comprehensive theory of [X] is lacking for [Y], which raises the question as to whether..." (Paper 2)
- "Yet, it remains unclear whether such impurities can trigger unconventional phenomena in [X]." (Paper 3)
- "Achieving this crucially requires direct control of [X]." (Paper 4)

**Pattern:** "Despite/Yet/However" + specific gap. NOT "There is a need for more research."

### The "Here we..." sentence (MOST IMPORTANT — every paper has it):

- "Here we present direct evidence of such a phase in 1H-NbSe2." (Paper 1)
- "Here we develop an analogue to the Young–Dupre equation for systems made of self-propelled particles." (Paper 2)
- "Here we demonstrate the emergence of Kondo resonance states near magnetic dopants in CsV3Sb5." (Paper 3)
- "Here we demonstrate an optically driven renormalization of the terahertz magnon spectrum in the insulating antiferromagnet DyFeO3." (Paper 4)

**Pattern:** "Here we [action verb] [what we did/found] in [specific system]."
**Short. One sentence. No subordinate clauses. 15-25 words.**

### Hedging language (when making claims):

REAL examples from these papers:
- "These results suggest that..." (Paper 4) ← NOT "prove"
- "Our results strongly indicate that..." (Paper 3) ← NOT "demonstrate"
- "We propose that..." (Paper 3) ← NOT "We conclude"
- "This phenomenon arises precisely due to..." (Paper 1) ← Strong claim WITH mechanism
- "our observation calls for further systematic investigation" (Paper 3) ← Honest

**Rule:** Claims about WHAT WAS OBSERVED are stated strongly. Claims about INTERPRETATION are hedged. This is the key difference from our current draft.

### Paragraph construction:

Typical paragraph structure in Nature Physics:
1. Topic sentence (what this paragraph shows)
2. Evidence / data description (2-3 sentences)
3. Interpretation / mechanism (1-2 sentences)
4. Transition or implication (1 sentence)

Example (Paper 3):
> "The Kondo screening of a single magnetic impurity... depends on the spatial distribution of the magnetic moment and its exchange coupling to the itinerant electrons within a specific crystal lattice. [TOPIC] Consequently, the real-space pattern of the Kondo resonance should be determined by both the magnetic moment and the crystal lattice symmetries. [EVIDENCE] In our case, the extension of the Kondo resonance with its maximum intensity away from the impurity suggests that the local orbital of a Cr atom is unlikely to be the simple reason for the spatial asymmetry. [INTERPRETATION] It is thus necessary to check the underlying electronic orders presented here. [TRANSITION]"

## 3. WORD-LEVEL PATTERNS

### Human vs AI markers:

| AI tendency | Nature Physics human usage |
|-------------|---------------------------|
| "demonstrate" (overused) | "show" (Paper 1: "Our results show..."), "reveal" (Paper 4), "indicate" |
| "crucial/critical" (overused) | "important" (Paper 3: "it is of fundamental importance"), or omit entirely |
| "Furthermore/Moreover/Additionally" | "We also observe..." / "Notably,..." / "Importantly,..." |
| "robust" (overused) | "pronounced" (Paper 3), "substantial" (Paper 4), or specific numbers |
| "shed light on" | "provide insight into" (Paper 3), "reveal" (Paper 4) |
| "paradigm shift" | Never used in any paper. Just state the finding. |
| "unprecedented" | Never used. |
| Long abstract (250+ words) | Tight (~180-200 words) |
| "In this paper/Article we..." | "Here we..." (Paper 1,2,3,4 all use this) |

### Transition words actually used:

- Between paragraphs: "To better understand..." / "Next, we..." / "We further..." 
- Contrasting: "By contrast," / "However," / "Surprisingly,"
- Emphasizing: "Indeed," / "Notably," / "Importantly,"
- Summarizing: NEVER "In conclusion," at start of last paragraph — just states the finding

### Figure references:

Pattern: "Figure 2a shows..." / "as shown in Fig. 1c" / "(Fig. 3b)"
NOT: "As can be seen in Figure..." or "Figure X illustrates..."

## 4. KEY DIFFERENCES vs OUR CURRENT DRAFT

| Element | Our main.tex | Nature Physics standard | Fix needed |
|---------|-------------|------------------------|------------|
| Abstract | 225 words, contains equations | ~180 words, no equations, no citations | Trim, remove eqns |
| "Here we" sentence | Hidden in middle of abstract | Second-to-last sentence of first paragraph of intro | Restructure |
| Hedging | Mixed | Strong on observations, hedged on interpretation | Review all claims |
| Section headers | Introduction, Results, Discussion, Methods | Results AND Discussion merged with sub-headings | Merge |
| Figure description | Takes a whole paragraph | 1-2 sentences referencing the figure, then moves on | Tighten |
| "Smoking gun" language | Used | Never used. "Falsifiable prediction" is fine | Remove |
| Claims of novelty | "Unlike all competing models" | Just state what's different without "unlike" | Soften |
| Limitations | Bullet list with 4 items | Integrated into discussion narrative | Rewrite as narrative |

## 5. THE GOLDEN RULES

1. **Observations are stated boldly.** "We find X." "Our measurements show Y."
2. **Interpretations are hedged.** "This suggests Z." "It is consistent with W."
3. **"Here we..." is the spine of the introduction.** It's the sentence everything builds toward.
4. **One idea per paragraph.** Nature Physics paragraphs are SHORT (3-5 sentences).
5. **Figures carry the argument.** Text references them briefly and moves on.
6. **No superlatives.** Let the results speak. The reader decides if it's "unprecedented."
7. **Discussion is NOT a rehash of results.** It's implications + limitations + next steps — all woven together.
8. **Methods are terse and specific.** "We used X to measure Y with precision Z. Error bars represent..."
