---
name: harmonyos-build
description: >-
  HarmonyOS / DevEco app build flow: run build.py, read build.log, triage failures in order. Use when building an exported DevEco project after x2cj export.
---

# HarmonyOS / DevEco build

## Purpose

Run the scripted build and, on failure, triage in the fixed order below. Base every conclusion on logs—no guessed fixes or skipped steps.

## Build flow

### Step 1: Run the build

From the **x2cj-skills** repo root (or pass an absolute path to the script):

```bash
python skills/x2cj/build/build.py --project-root <DevEco project root>
```

If the skill is installed elsewhere (e.g. `.agents/skills/...`), use that copy of `build.py`.

- **`--project-root`**: root of the **exported** DevEco project (same layout as `export_deveco_app.py` output); optional, defaults to the current working directory.
- The script runs `ohpm install` → `SyncCangjieResource` → `assembleHap` in sequence.
- Set **`DEVECO_HOME`** (DevEco Studio install root) and **`CANGJIE_SDK_HOME`** (Cangjie SDK root, must contain `compiler/`). The script has **no** hard-coded path fallbacks.

### Step 2: Outcome

- Treat the run as success if logs contain `BUILD SUCCESSFUL` (unsigned artifacts are fine).
- Full log: **`build.log`** in the project directory—read it for any investigation.
- If startup fails on missing env or paths, fix **`DEVECO_HOME`** / **`CANGJIE_SDK_HOME`** and confirm directories exist.

### Step 3: Failure triage (strict order)

1. **Cangjie-oriented debugging** — if no hit, analyze the log, fix, rebuild.
2. **Doc search** — if still stuck, use cangjie-harmonyos-doc-search.
3. **User assist** — if the log is insufficient, ask the user to reproduce in DevEco Studio and share errors.
