---
name: harmonyos-evolution
description: "Use this skill to read, match, and write verified Cangjie HarmonyOS development lessons in project Evolution.md or user memory after build, runtime, UI, interop, or retrieval issues are proven and fixed."
---

# Evolution Memory

## Read Order

1. Project root `Evolution.md`
2. User memory `~/.cangjie/harmonyos-evolution.md`
3. Packaged read-only baseline `<harmonyos-evolution-skill>/references/memory.md`
4. Current `build.log`, hilog summary, UI capture report, or interaction report

## Write Rules

- Require build, runtime, interaction, or retrieval evidence.
- Keep project-local facts in project `Evolution.md`.
- Keep verified cross-project lessons in `~/.cangjie/harmonyos-evolution.md`; create it when needed.
- Treat packaged `references/memory.md` as read-only release content so Skill updates cannot overwrite user lessons.
- Update the owning reference instead of duplicating build, UI, interop, bootstrap, configuration, or retrieval rules here.
- Merge repeated lessons; do not append status history or hypotheses.

Use this format:

```markdown
## <issue title>

- Scenario: build / runtime / UI / interop / retrieval
- Symptom:
- Cause:
- Fix:
- Verification:
- Keywords:
```
