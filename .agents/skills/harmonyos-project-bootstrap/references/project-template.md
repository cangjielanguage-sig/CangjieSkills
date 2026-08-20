# Pure Cangjie Project Template

Create or repair projects through `tools/create_project.py`; do not copy template files manually.

The tool renders `templates/cangjie-harmonyos-app/`, validates inputs, remaps the module directory, replaces template tokens, preserves binary media, and rejects unresolved tokens. Use `--repair` only to overwrite template-owned files.

Use `[scaffold]` only when `app_name`, `bundle_name`, and `module_name` must be reused across generation runs. Prefer CLI arguments for a one-off project. Keep `vendor`, SDK, and model overrides on the generator CLI.

For the supported SDK 6.1 / Cangjie 1.1.0 pure Stage template, the internal Cangjie package and cjpm library name is `ohos_app_cangjie_entry`. A custom internal name can compile but fails cold start with `cj functions for CJAbilityStage.LoadAbilityStage are not registered`; use `--bundle-name` and `--module-name` for application identity.

```powershell
python -B <harmonyos-project-bootstrap-skill>/tools/create_project.py `
  --target-dir . `
  --app-name "Todo" `
  --bundle-name "com.example.todo"
```
