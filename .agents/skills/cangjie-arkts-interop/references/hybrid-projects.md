# Hybrid Project Structure

Use this reference for HarmonyOS apps where ArkTS owns the Ability/page shell and Cangjie provides a dynamic library, exported functions, or embedded components.

Shared `[scaffold]` defaults cover only app name, Bundle name, and Module name. Use `create_hybrid_project.py --package-name` only when intentionally changing the complete Cangjie library/type/import chain; keep SDK/model overrides explicit on the generator CLI.

## Minimal Layout

```text
entry/
  build-profile.json5
  cjpm.toml
  oh-package.json5
  src/main/module.json5
  src/main/cangjie/index.cj
  src/main/cangjie/types/lib<package>/Index.d.ts
  src/main/cangjie/types/lib<package>/oh-package.json5
  src/main/ets/entryability/EntryAbility.ets
  src/main/ets/pages/Index.ets
  src/main/resources/base/profile/main_pages.json
```

## Required Wiring

- `entry/cjpm.toml` `[package].name` is the Cangjie package and dynamic library stem.
- `entry/oh-package.json5` depends on `"lib<package>.so": "file:src/main/cangjie/types/lib<package>"`.
- `types/lib<package>/oh-package.json5` declares `"name": "lib<package>.so"` and `"types": "./Index.d.ts"`.
- ArkTS imports exported Cangjie APIs from `lib<package>.so`.
- ArkTS page navigation uses the page-bound UI context, for example `this.getUIContext().getRouter().pushUrl({ url: 'pages/metrics' })`. The global `router.pushUrl/back` APIs are deprecated since API 18.
- `module.json5` uses ArkTS Ability `srcEntry`, usually `./ets/entryability/EntryAbility.ets`.
- `module.json5` should include `"pages": "$profile:main_pages"`.
- `main_pages.json` registers ArkTS pages such as `"pages/Index"`.
- `entry/build-profile.json5` should set `cangjieOptions.path` to `./cjpm.toml` and include both `x86_64` and `arm64-v8a` ABI filters for emulator/device coverage.
- `entry/cjpm.toml` `compile-option` must use the module-specific condition variable, for example `COMPILE_CONDITION_ENTRY` for module `entry` and `COMPILE_CONDITION_MAIN` for module `main`.

## Validation

Run from the project root:

```powershell
python -B <cangjie-arkts-interop-skill>/tools/hybrid_project_check.py
python -B <harmonyos-build-run-diagnose-skill>/tools/build_recovery.py --retry
```

For UI behavior, install and assert the cross-language result:

```powershell
python -B <harmonyos-build-run-diagnose-skill>/tools/ui_capture.py --project . --hap entry/build/default/outputs/default/entry-default-unsigned.hap --out ui_hybrid --foreground-retries 2 --scenario scenario.json
```

## Common Failures

| Symptom | Check |
| --- | --- |
| ArkTS import cannot find `lib*.so` | `entry/oh-package.json5` dependency and `types/lib<package>/oh-package.json5` name |
| ArkTS symbol missing | `Index.d.ts` does not declare the exported Cangjie symbol |
| Cangjie builds but ArkTS fails | ArkTS import/types are stale or mismatched |
| App launches but value does not change | UI event did not call the imported function, or Cangjie export name differs from `.d.ts` |
| Emulator install/launch crash | Missing `x86_64` ABI filter or wrong bundle/ability/module launch parameters |
| Cangjie compile shows broken `--cfg -B` options | `COMPILE_CONDITION_<MODULE>` in `cjpm.toml` does not match the HarmonyOS module name |
| `CJHybridComponent` blank or missing | Check `@cangjie/cjhybridcomponent` dependency, `library` package name, Cangjie `@HybridComponentEntry`, and wrapper page route |
| ArkTS warns that `router.pushUrl` or `router.back` is deprecated | Remove the global router import and call `this.getUIContext().getRouter().pushUrl(...)` or `.back()` from the component callback |
