---
name: harmonyos-project-bootstrap
description: "Use this skill to create or repair a Cangjie HarmonyOS project, including template-based creation, bundleName/package/module wiring, resources, Cangjie Ability entry files, and HarmonyOS-only stdx provisioning for x64 emulators and ARM64 devices."
---

# Project Bootstrap

## Primary Workflow

1. Determine the app name, bundle name, target directory, and module name. For the supported SDK 6.1 / Cangjie 1.1.0 pure Stage template, keep the internal Cangjie package and cjpm dynamic library name as `ohos_app_cangjie_entry`; express application identity through `bundleName` and `module_name`.
2. Create or repair the project with:

   ```bash
   python -B <harmonyos-project-bootstrap-skill>/tools/create_project.py --target-dir . --app-name "<app name>" --bundle-name "<bundle name>"
   ```

   Use `--repair` when the directory already contains a partially generated HarmonyOS project and template-owned files should be overwritten.
   For repeatable generation, `[scaffold]` may provide only `app_name`, `bundle_name`, and `module_name`; see `<cangjie-harmonyos-dev-skill>/references/configuration.md`. Keep one-off and advanced values on the CLI.
3. If the module imports `stdx.*`, read `references/harmonyos-stdx.md`, then install and configure both HarmonyOS ABIs with `tools/setup_harmonyos_stdx.py`.
4. Implement requested features in `entry/src/main/cangjie/index.cj` and related Cangjie files.
5. Build with `harmonyos-build-run-diagnose`.
6. If a device or emulator is available, install, launch, capture UI, and verify interactions with `harmonyos-build-run-diagnose`.

## Template Resources

- Project template: `templates/cangjie-harmonyos-app/`
- Project creation tool: `tools/create_project.py`
- HarmonyOS stdx tool: `tools/setup_harmonyos_stdx.py`
- Template contract: `references/project-template.md`
- stdx setup contract: `references/harmonyos-stdx.md`

The script owns parameter validation, file copying, and placeholder replacement. Keep reusable project structure in the template directory, not inside script string literals.

Treat the creation script and template as packaged executable resources. Run `create_project.py --help`, then invoke it; do not read the script or enumerate/read the full template during normal project creation. Inspect their internals only when the tool fails or the task is to modify the bootstrap skill itself.

## Checks

- Use reverse-domain `bundleName`, for example `com.example.todo`.
- Treat a target containing only `.agents/` or `.claude/` skill containers as empty; preserve those containers during creation or repair.
- Keep `entry/cjpm.toml` `src-dir` as `./src/main/cangjie`.
- Keep `module.json5.mainElement` aligned with `EntryAbility` and `srcEntry` aligned with the Cangjie package.
- Keep the pure-template internal Cangjie package/cjpm library name as `ohos_app_cangjie_entry`. A custom name can compile but fails cold start with `cj functions for CJAbilityStage.LoadAbilityStage are not registered`; the creation tool therefore does not expose a package-name override. This constraint does not make `bundleName` or `module_name` fixed.
- Include `x86_64` and `arm64-v8a` ABI filters for emulator and device coverage.
- Add `stdx` dependencies only when the app uses stdx APIs. Only `ohos-x64` and `ohos-aarch64` are in scope.
