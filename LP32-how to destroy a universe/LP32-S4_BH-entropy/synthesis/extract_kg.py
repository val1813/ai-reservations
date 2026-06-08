"""Extract knowledge_graph JSON from R3_closeout.md and validate."""
import json, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('D:/Claude/ai-reservations/LP32-how to destroy a universe/LP32-S4_BH-entropy/synthesis/R3_closeout.md', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '```json'
end_marker = '```'
start = content.find(start_marker) + len(start_marker)
end = content.find(end_marker, start)
json_str = content[start:end].strip()

kg = json.loads(json_str)
print(f'Valid JSON: {len(kg["nodes"])} nodes, {len(kg["edges"])} edges, {len(kg["ahas"])} ahas')
print(f'Status: {kg["meta"]["status"]}')
print(f'Open problems: {len(kg["open_problems"])}')
print(f'Cross references: {len(kg["cross_references"])} categories')

out_path = 'D:/Claude/ai-reservations/knowledge_graph/LP32-S4_v4_20260608.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(kg, f, ensure_ascii=False, indent=2)
print(f'Standalone JSON written: {out_path}')
print(f'File size: {os.path.getsize(out_path)} bytes')
