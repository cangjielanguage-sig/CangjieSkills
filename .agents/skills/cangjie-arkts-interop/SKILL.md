---
name: cangjie-arkts-interop
description: "Use this skill for Cangjie and ArkTS interoperation in HarmonyOS projects: creating Cangjie-ArkTS hybrid app templates, ArkTS importing Cangjie .so functions, JSModule.registerModule exports, @Interop macro exports, Cangjie calling ArkTS APIs through JSRuntime, CJHybridComponent UI embedding, mixed build/config diagnosis, .d.ts synchronization, and runtime validation of cross-language UI behavior."
---

# Cangjie ArkTS Interop

## Route by Scenario

| Scenario | Read or Run |
| --- | --- |
| Create a mixed Cangjie-ArkTS app from an empty directory | `tools/create_hybrid_project.py` |
| Add a Cangjie UI component with an ArkTS wrapper page | `tools/add_hybrid_component.py` |
| Validate mixed project wiring | `tools/hybrid_project_check.py` |
| ArkTS imports Cangjie functions from `lib*.so` | `references/arkts-call-cangjie.md` |
| Type mapping and declaration synchronization | `references/type-mapping.md` |
| Cangjie calls ArkTS/system APIs | `references/cangjie-call-arkts.md` |
| Mixed app structure, build files, `.d.ts`, and runtime validation | `references/hybrid-projects.md` |
| Cangjie component embedded in ArkTS page | `references/cjhybridcomponent-ui.md` |

## Create a Hybrid Project

From a project directory where this solution's skills have already been copied:

```powershell
python -B <cangjie-arkts-interop-skill>/tools/create_hybrid_project.py --target-dir . --app-name "Hybrid App" --bundle-name "com.example.hybrid"
python -B <cangjie-arkts-interop-skill>/tools/hybrid_project_check.py
python -B <harmonyos-build-run-diagnose-skill>/tools/build_recovery.py --retry
```

Use `--repair` only when overwriting template-owned files in a partially generated hybrid project is intended.

For repeatable generation, `[scaffold]` may provide only `app_name`, `bundle_name`, and `module_name`. Keep the hybrid Cangjie library/package name and SDK/model compatibility overrides as explicit advanced CLI arguments.

Treat the packaged creation/check/component scripts and templates as executable resources. Use their `--help` and generated diagnostics; do not read or enumerate their implementation/template trees during ordinary app development. Inspect internals only when a tool fails or the task explicitly maintains this skill.

## Add a Cangjie UI Component

Use this only inside a Cangjie-ArkTS hybrid project, not a pure Cangjie HarmonyOS project:

```powershell
python -B <cangjie-arkts-interop-skill>/tools/add_hybrid_component.py --component MetricsPanel --page metrics --title "Cangjie Metrics"
python -B <cangjie-arkts-interop-skill>/tools/hybrid_project_check.py
python -B <harmonyos-build-run-diagnose-skill>/tools/build_recovery.py --retry
```

The tool creates:

- `entry/src/main/cangjie/<component>.cj`
- `entry/src/main/ets/pages/<page>.ets`
- `@cangjie/cjhybridcomponent` dependency when missing
- `pages/<page>` registration in `main_pages.json`

## Development Procedure

1. Identify the boundary direction: ArkTS to Cangjie, Cangjie to ArkTS, or UI embedding.
2. Keep the package/library chain aligned: `cjpm.toml [package].name` -> `lib<package>.so` -> `entry/oh-package.json5` dependency -> ArkTS import.
3. When exporting Cangjie APIs to ArkTS, update Cangjie export code and `src/main/cangjie/types/lib<package>/Index.d.ts` together.
4. Keep ArkTS Ability and page routing in ArkTS for the hybrid app template; Cangjie provides a dynamic library and exported functions/components.
   In ArkUI component callbacks, use `this.getUIContext().getRouter()` for navigation. Do not generate or copy the global `router.pushUrl/back` APIs deprecated since API 18.
5. Build after every boundary change, then run `hybrid_project_check.py`.
6. For user-visible behavior, install/launch/capture with `harmonyos-build-run-diagnose` and assert the UI text/key produced after the cross-language call.
7. For UI component mixing, assert both that the Cangjie component appears under the ArkTS page and that Cangjie-side click/state behavior works.

## Guardrails

- Prefer simple value boundaries (`string`, `number`, `boolean`) or DTO/JSON for complex data.
- Keep generated/type declaration files single-source and synchronized with the actual Cangjie exports.
- Do not treat a successful Cangjie compile as sufficient; ArkTS import/type errors may appear later in `CompileArkTS`.
- Use `JSRuntime` only with explicit lifetime and thread decisions.
- Treat the unsigned signing warning as non-blocking for local validation unless a signed release is requested.
- Do not apply hybrid scripts to pure Cangjie projects created by `harmonyos-project-bootstrap`; use this skill only when ArkTS files, `module.json5` pages, and Cangjie dynamic-library wiring are present or intentionally being created.
