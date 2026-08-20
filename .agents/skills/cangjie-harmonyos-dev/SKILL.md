---
name: cangjie-harmonyos-dev
description: "Use this skill as the main coordinator for Cangjie HarmonyOS application work, including creating or changing apps, implementing ArkUI features, reproducing a screenshot or UI mockup, fixing builds, running on an emulator or device, validating UI interactions and visual alignment, using HarmonyOS APIs, using Cangjie std/stdx, handling ArkTS interop, and recording verified lessons."
---

# Cangjie HarmonyOS Development

## Workflow

1. From the project root, run the bounded discovery gate first:

   ```powershell
   python -B <cangjie-harmonyos-dev-skill>/tools/doctor.py --project-root . --json
   ```

   Treat its final config sources, toolchain paths, runtime metadata, HAP, and device state as authoritative for the current run. When those fields are present, stop filesystem discovery and inspect only the request-relevant `cjpm.toml`, `src/main`, `module.json5`, and existing `Evolution.md` before editing.
2. For machine paths, advanced runtime overrides, or optional RAG embedding settings, read `references/configuration.md` and use layered config before asking the user.
3. Select the narrowest supporting skill:
   - New or broken project structure, or HarmonyOS stdx provisioning: `harmonyos-project-bootstrap`
   - HarmonyOS API, ArkUI, toolchain, or permission knowledge: `cangjie-harmonyos-knowledge`
   - Cangjie syntax, language semantics, std/stdx API knowledge, or `cjpm`: `cangjie-coding`
   - ArkTS/Cangjie interop: `cangjie-arkts-interop`
   - Build, launch, UI capture, hilog, or interaction validation: `harmonyos-build-run-diagnose`
   - Reusable verified lessons: `harmonyos-evolution`
4. Implement the smallest coherent change.
5. Keep user-visible controls addressable with stable keys when interaction verification is required.
6. Build after each meaningful change.
7. For UI or runtime behavior, install, launch, capture, and assert business keys or text.
8. Record verified reusable lessons only after evidence passes.

Packaged scripts and indexes are black-box task resources. Run their `--help` or documented commands and consume bounded reports; do not read long tool implementations, templates, raw indexes, or raw one-line UI trees unless the task is maintaining that resource or a tool failure requires inspection.

The doctor report contains an explicit `inspection.stop` rule. Do not enumerate `.agents/`, packaged knowledge bodies, templates, indexes, `oh_modules`, or build trees after the report is complete unless a reported field is missing or a later build/runtime command fails. This is a verifiable stopping condition, not a suggestion to collect the same facts again.

Batch the initial knowledge lookup and start from the template's verified patterns. Do not pause implementation to query each ordinary style modifier; expand retrieval only when a contract is missing or build/runtime evidence requires it. Project inspection must exclude `.agents/`, `.claude/`, raw knowledge bodies, indexes, and generated dependency/build directories.

## Model Routing

- When the request includes a screenshot, design image, or visual template, an image-capable agent must inspect the reference and compare the final emulator screenshot. A text-only model may implement APIs or run builds, but must not approve visual alignment.
- For screenshot-driven work, read `harmonyos-build-run-diagnose/references/visual-template-validation.md` before implementation and preserve the reference plus every compared capture as evidence.

## Configuration

Layered config is optional. Use the single `cangjie.skills.toml` contract at `<project>/cangjie.skills.toml` or `~/.cangjie/cangjie.skills.toml`; `CANGJIE_SKILLS_CONFIG` may name a final override file. CLI and direct environment values take precedence. Read `references/configuration.md` for every supported key, default, validation rule, and degradation path.

## Implementation Checks

- Query unfamiliar APIs before coding.
- Prefer Cangjie ArkUI signatures over ArkTS assumptions.
- Use named parameters and explicit length units when porting ArkUI code.
- Keep state keys stable for testing, for example `countDisplay`, `submitButton`, `emptyState`.
- Avoid unrelated refactors while fixing build/runtime issues.
- Treat the compiler, current packaged references, and runtime evidence as stronger than model memory.
- Do not copy a Cangjie API from a search snippet without confirming its package, signature, callback shape, permissions, and minimum version when those affect the task.

## Completion Evidence

Report:

- Changed files.
- Knowledge refs used for non-obvious APIs.
- Build result and HAP path when applicable.
- Runtime/UI/hilog evidence when applicable.
- Remaining blocker only when it is backed by logs or tool output.
