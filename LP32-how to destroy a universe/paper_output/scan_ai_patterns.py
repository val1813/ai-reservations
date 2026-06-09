import re, sys

with open(sys.argv[1], 'r') as f:
    text = f.read()

# Crude LaTeX stripping
text = re.sub(r'%.*', '', text)
text = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', text)
text = re.sub(r'\$[^$]*\$', 'MATH', text)
text = re.sub(r'\\begin\{[^}]*\}', '', text)
text = re.sub(r'\\end\{[^}]*\}', '', text)
text = re.sub(r'\{[^}]*\}', '', text)
text = re.sub(r'\[[^]]*\]', '', text)

# Split into paragraphs
paras = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 80]

print(f"Total prose paragraphs: {len(paras)}\n")

# 1. Sentence counts
print("=== 1. SENTENCES PER PARAGRAPH ===")
sc_list = []
for i, p in enumerate(paras):
    sc = len(re.findall(r'(?<=[a-zA-Z])[.?!]\s+(?=[A-Z])', p)) + 1
    sc_list.append(sc)
    preview = p[:70].replace('\n', ' ')
    print(f"  P{i:02d}: {sc}s | {preview}...")

import statistics
print(f"\nMean: {statistics.mean(sc_list):.1f}, Std: {statistics.stdev(sc_list):.1f}")
print(f"Min: {min(sc_list)}, Max: {max(sc_list)}")
if statistics.stdev(sc_list) < 2.0:
    print("WARNING: Paragraphs too uniform!")

# 2. Connectors
print("\n=== 2. CONNECTOR DENSITY ===")
connectors = ['However', 'Moreover', 'Furthermore', 'Therefore', 'Thus',
              'Nevertheless', 'Consequently', 'Hence', 'Indeed', 'Nonetheless']
for c in connectors:
    count = text.count(c)
    if count > 0:
        print(f"  {c}: {count}")

# 3. Enumeration structures
print("\n=== 3. ENUMERATION PATTERNS ===")
for pattern in ['First', 'Second', 'Third', 'Finally', 'spanning']:
    count = text.count(pattern)
    if count > 0:
        print(f"  '{pattern}': {count}")

# 4. Hedging
print("\n=== 4. HEDGING / FORBIDDEN PHRASES ===")
for phrase in ['We hope', 'We are confident', 'in principle', 'awaits future',
               'should be candid', 'remains an open', 'leave.*future work',
               'Further investigation is warranted']:
    matches = re.findall(phrase, text)
    if matches:
        print(f"  '{phrase}': {len(matches)}")
    else:
        print(f"  '{phrase}': 0")

# 5. Sentence-frame repetition
print("\n=== 5. REPEATED SENTENCE FRAMES ===")
frames = ['which is', 'this is', 'it is', 'there are', 'we note', 'we emphasize']
for frm in frames:
    count = len(re.findall(frm, text, re.IGNORECASE))
    if count > 2:
        print(f"  '{frm}': {count} (WARNING if >3)")

print("\nDone.")
