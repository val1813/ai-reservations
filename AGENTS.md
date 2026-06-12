# AI Reservations Project Instructions

Scope: this file governs all work under `D:\Claude\ai-reservations`.

Required entry points:

- For research advancement / 科研推进 / 继续科研 / 按科研流程 / 收官: read `D:\Claude\ai-reservations\ai\CLAUDE.md` first, then follow the role/protocol files it points to only when needed.
- 🆕 For context restoration across sessions, say "继续科研" → triggers research-continue Skill (auto-loads Phase清单+研究快照+全部状态)
- 🆕 找到墙破墙 / 破墙 / 打破瓶颈 → triggers WALL_BREAKER agent (`ai/WALL_BREAKER.md`)
- 🆕 复燃 / 灰烬复燃 / 这个课题还有救吗 → triggers EMBER_REKINDLER agent (`ai/EMBER_REKINDLER.md`)
- For candidate selection / 选题 / 北极星候选池 updates: read `D:\Claude\ai-reservations\ai2\SELECTOR.md` first.
- For dean review / 院长复盘: read `D:\Claude\ai-reservations\ai3\DEAN.md` first.

Research advancement hard rules:

- `project\Phase清单.md` is the active checklist. If it does not exist, copy `D:\Claude\ai-reservations\ai\Phase清单模板.md` into the project before doing research work.
- Start from the first unchecked `[ ]` item in `project\Phase清单.md`. Mark an item `[✅]` only after it is actually completed.
- Before all checklist items for the active stage are complete, do not invent or execute steps outside the checklist.
- Maintain `project\北极星队列.md` as the project-local dynamic priority queue. `shared\北极星候选池.md` is a read-only SELECTOR catalog for research windows and is used only to choose an initial topic when a project queue is empty.
- Minimum exploration is 3 AB rounds unless a hard stop is triggered by the SOP.
- INSPECTOR, REVIEWER, AUDITOR, WALL_BREAKER, EMBER_REKINDLER, and A/B roles must be launched as independent agent instances when the SOP requires them. The PI/main context must not hand-write those reports.
- A and B must remain independent and must not read each other's outputs before their round is complete.
- 🆕 卡点重复≥2轮 → 触发WALL_BREAKER（不等≥3轮）。REVIEWER Reject后 → 先复燃再降级。
- 🆕 每轮AB后更新研究快照.md（防跨对话遗忘）。课题最多复燃2次。

Selector hard rules:

- Follow `ai2\SELECTOR.md` rather than memory when generating or refreshing candidates.
- Use `paper-search-mcp` first for academic literature search and WebSearch only as the documented fallback or for non-academic facts such as awards and institutional pages.
- The current SELECTOR structure is long-proposition-first: L-1 hidden-assumption search has highest priority, then L0 recent experiment-theory tensions, then L1-L6 as needed.
- Write selector outputs to `shared\北极星候选池.md` in the format required by `ai2\SELECTOR.md`.

Context hygiene:

- When the user explicitly asks to re-initialize a project and avoid a previous project directory, do not read that previous directory. Use only the shared candidate entry and SOP files needed to initialize the new workspace.
- If a required state file is missing, report the missing file and create the highest-fidelity fallback allowed by the SOP.
