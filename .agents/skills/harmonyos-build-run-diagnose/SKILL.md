---
name: harmonyos-build-run-diagnose
description: "Use this skill to build, repair, install, launch, capture UI, interact with, and diagnose Cangjie HarmonyOS apps. Use it for .hap generation, build failures, cjpm/Hvigor cache recovery, hdc discovery, emulator or device validation, screenshots, component-tree assertions, screenshot/mockup alignment, hilog runtime triage, white screens, crashes, and interaction bugs."
---

# Build, Run, and Diagnose

## Tools

Use the project-local packaged tools:

```text
<harmonyos-build-run-diagnose-skill>/tools/build.py
<harmonyos-build-run-diagnose-skill>/tools/build_analyzer.py
<harmonyos-build-run-diagnose-skill>/tools/build_recovery.py
<harmonyos-build-run-diagnose-skill>/tools/ui_capture.py
<harmonyos-build-run-diagnose-skill>/tools/hilog_capture.py
```

Auto-detect the latest installed `~/.cangjie-sdk/*/cangjie` SDK. Use an explicit older SDK only when the project or user requires it.

Treat these scripts as packaged executable tools: use `--help` and their reports rather than reading their implementation. Inspect tool source only when a tool fails or the task explicitly changes the tool.

The tools read `<project>/cangjie.skills.toml` and `~/.cangjie/cangjie.skills.toml` when present. Use the user file for DevEco, Cangjie SDK, `hdc`, registry, and device defaults; use the project file only for repeatable project settings. CLI arguments override config. `<cangjie-harmonyos-dev-skill>/references/configuration.md` defines the complete contract.

## Build

If the HarmonyOS module imports `stdx.*`, install both emulator and device binaries before building:

```powershell
python -B <harmonyos-project-bootstrap-skill>/tools/setup_harmonyos_stdx.py --project <project>/<module>
```

The bootstrap tool supports only `ohos-x64` and `ohos-aarch64`, installs both by default, and configures their respective `cjpm.toml` target tables. Read `<harmonyos-project-bootstrap-skill>/references/harmonyos-stdx.md` for compatibility, offline, and recovery rules.

Prefer the recovery wrapper:

```powershell
python -B <harmonyos-build-run-diagnose-skill>/tools/build_recovery.py --retry
```

Use the raw build tool only when cache recovery is not needed:

```powershell
python -B <harmonyos-build-run-diagnose-skill>/tools/build.py --project-root <project>
```

When running from outside the project root, pass `--project-root <project>`.

The build tool selects the only declared module, otherwise `entry`, otherwise the first declared module with a warning. Pass `--module <name>` when that fallback is not the intended target.

If DevEco Studio or the Cangjie SDK is not at the default path, pass `--deveco-home` / `--cangjie-sdk` or configure `[toolchain]` in user config.

Success requires:

- `ohpm install` succeeded.
- `SyncCangjieResource` succeeded.
- `assembleHap` logs contain `BUILD SUCCESSFUL`.
- `<module>/build/default/outputs/default/*-unsigned.hap` exists.

## Build Failure Workflow

1. Read `<project>/build.log`.
2. From the project root, run `python -B <harmonyos-build-run-diagnose-skill>/tools/build_analyzer.py`; from elsewhere, pass `--project-root <project>`.
3. Extract the first stable error block, not the last noisy warning.
4. Check project `Evolution.md`, user memory `~/.cangjie/harmonyos-evolution.md`, then the packaged read-only baseline `<harmonyos-evolution-skill>/references/memory.md`.
5. Match known patterns in `references/build-failures.md`.
6. Use `cangjie-harmonyos-knowledge` for HarmonyOS/ArkUI signatures and platform errors; use `cangjie-coding` for language, collection, conversion, or cjpm errors.
7. Make the smallest code/config fix and rebuild.
8. After two repeated failures with the same signature, widen cleanup scope or report the exact blocker.

## Runtime and UI Validation

Locate `hdc` first:

```powershell
& "C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains\hdc.exe" list targets
```

Install/launch/capture after a successful build:

```powershell
python -B <harmonyos-build-run-diagnose-skill>/tools/ui_capture.py `
  --project <project> `
  --hap "<project>/<module>/build/default/outputs/default/<module>-default-unsigned.hap" `
  --wait 8 `
  --foreground-retries 2 `
  --out <out>
```

Pure Cangjie apps can need several seconds for the runtime and Ability to cold-start on an emulator. Use `--wait 8 --foreground-retries 2` for the first capture; a launcher capture is not application evidence.

Capture bounded hilog when launch, crash, white-screen, or assertions fail:

```powershell
python -B <harmonyos-build-run-diagnose-skill>/tools/hilog_capture.py --project-root <project> --out <out> --seconds 8
```

`hilog_capture.py` detects bundle, module, and ability from the project. Use `--bundle`, `--ability`, `--module`, or `[runtime]` only when detection is ambiguous.

For an interaction state that will later scroll off-screen or disappear after navigation, put partial `assertions` directly on a `snapshot` scenario step. Those assertions are evaluated immediately and are included in `interaction_report.md`; top-level assertions remain final-state checks. The complete contract is `references/ui-scenario-schema.json`.

Read `references/runtime-ui-diagnosis.md` before judging foreground state, UI diffs, interaction assertions, or hilog severity.

When the task starts from a screenshot or visual mockup, also read `references/visual-template-validation.md`. Visual approval requires an image-capable agent to inspect both reference and final capture; component-tree assertions and text-only reasoning are supporting evidence, not a visual comparison.

## Validation Rules

- A build success is not enough for UI work; verify foreground state and business key/text.
- A screenshot or layout capture is not enough if it shows launcher, status bar, or unrelated windows.
- Prefer stable `key` assertions such as `countDisplay == "1"` over visual diffs.
- Read generated `ui_summary.md`, `interaction_report.md`, and bounded hilog output. Do not print, grep, or read a raw one-line `layout.json`; use the reports or a small structured JSON query when a field is missing.
- Use `hilog_summary.md` attribution fields. PID-attributed target-app errors take priority; bundle-text fallback is used only when the tool cannot resolve an app process. Treat other full-system hilog `ERROR` lines as noise unless they explain the symptom.
- Never accept an hdc command from exit code alone. The packaged tools also reject textual failures such as `[Fail]`, missing/offline devices, invalid commands, and failed connections.

## Experience Recording

Record only verified lessons. Write task-specific notes to project `Evolution.md`; write verified cross-project lessons to `~/.cangjie/harmonyos-evolution.md`. Do not modify packaged memory during application work.
