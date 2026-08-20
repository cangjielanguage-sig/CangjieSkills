# Runtime, UI, and hilog Diagnosis

## Foreground Validation

After launch or capture, verify the app reached the foreground:

```powershell
& "C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains\hdc.exe" -t 127.0.0.1:5555 shell aa dump -a
```

Accept foreground evidence such as `state #FOREGROUND` or `app state #FOREGROUND` for the target bundle.

If capture shows launcher or desktop:

```powershell
& "C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains\hdc.exe" -t 127.0.0.1:5555 shell aa start -a <abilityName> -b <bundleName>
Start-Sleep 2
python -B <harmonyos-build-run-diagnose-skill>/tools/ui_capture.py --project <project> --bundle <bundleName> --ability <abilityName> --no-launch --out <out>
```

## Pure Cangjie Entry Registration Failure

For an SDK 6.1 / Cangjie 1.1.0 pure Stage app that builds successfully but remains on the start window, search the bounded app hilog for:

```text
cj functions for CJAbilityStage.LoadAbilityStage are not registered
```

Check the internal Cangjie package, `[package].name`, `[profile.build.combined]` library name, source `package` declarations, and `module.json5.srcEntry` values together. The verified pure bootstrap keeps these on `ohos_app_cangjie_entry`; `bundleName` and the HarmonyOS module name remain independently configurable. Repair or regenerate with `harmonyos-project-bootstrap` rather than treating a start-window screenshot as application UI. Hybrid ArkTS-entry projects use a different entry model and are outside this pure-template rule.

## UI Assertion Rules

For a keyed click and exact post-action text assertion, write a bounded scenario such as:

```json
{
  "name": "increment-once",
  "steps": [
    {"action": "click", "target": {"key": "incrementButton"}}
  ],
  "assertions": [
    {
      "type": "text_equals",
      "target": {"key": "countDisplay"},
      "expected": "1",
      "message": "count changes after click"
    }
  ]
}
```

Supported common actions are `click`, `input` (with `text` and optional `hide_keyboard`), `back`, `wait` (with `seconds`), and `snapshot`. Common assertions are `exists`, `not_exists`, `text_equals`, and `text_changed`. This schema is sufficient for normal UI validation; do not inspect `ui_capture.py` to discover it.

The machine-readable contract is `references/ui-scenario-schema.json`. Top-level `assertions` keep their original meaning: they run against the final post-interaction capture. A `snapshot` step may also carry its own partial `assertions`; those run immediately against that snapshot and make the step fail when any assertion fails:

```json
{
  "name": "verify-transient-state-before-scroll",
  "steps": [
    {"action": "click", "target": {"key": "calculateButton"}},
    {
      "action": "snapshot",
      "label": "calculated",
      "assertions": [
        {
          "type": "text_equals",
          "target": {"key": "scoreDisplay"},
          "expected": "94",
          "message": "score is exact before it scrolls off-screen"
        }
      ]
    },
    {"action": "swipe", "direction": "up"}
  ],
  "assertions": [
    {"type": "exists", "target": {"key": "detailsPanel"}}
  ]
}
```

Snapshot assertions are additive; they do not replace final assertions. `exists`, `not_exists`, `text_equals`, and `clickable` inspect the snapshot layout. Change-based assertions compare the snapshot to the scenario baseline. This is the preferred way to verify a precise intermediate state when a later keyboard, navigation, or scroll legitimately removes the control from the accessibility tree. The generated report lists each snapshot assertion separately, and a missing layout, wrong foreground bundle, or assertion mismatch is reported as a failed interaction step rather than a successful capture.

- Assert business keys/text, not status bar or window-manager nodes.
- Prefer `key` targets for interactions and state checks.
- Use page diffs only as supporting evidence; time, battery, and system overlays can change.
- Conditional controls must be asserted only after the action that should create them. For example, empty-state text may not exist before clearing a list.
- If a business assertion fails, mark validation failed even if screenshot and layout capture succeeded.
- For text input through `uitest`, use `uiInput inputText <x> <y> <text>`. If the command prints usage or parameter errors, treat the interaction step as failed.
- After text input, the soft keyboard can resize the app window and remove lower controls from the accessibility tree. Add a `back` step, use `hide_keyboard: true` on the input step, or scroll before asserting controls below the keyboard.

## Short Secondary Pages

- A `Scroll` whose content is shorter than its viewport can appear vertically centered on this toolchain. Use a top-anchored `Column` when the page does not need scrolling.
- When a parent also owns fixed bottom navigation, give the child page `layoutWeight(1)` for the remaining region. A child `height(100.percent)` can push navigation beneath the system area.
- Recapture every extracted page after layout refactoring; a successful Overview capture does not prove secondary-page geometry.

## Keyed List Row Stays Stale

If a parent KPI updates after replacing an item but keyed row text does not, the list renderer may be reusing the unchanged `ForEach` identity. Use an observed item/object-link model, or include the relevant item version in the renderer identity (for example `sku + ":" + available`) so the row is rebuilt. Keep accessibility/business keys such as `status_<sku>` stable; only the renderer identity needs a version.

## hilog Triage

Read `hilog_summary.md` first.

Priority:

1. Target bundle/process FATAL or ERROR.
2. Crash stack.
3. Ability not found or launch failure.
4. Permission, resource, or SysCap errors.
5. System service noise.

Do not treat every full-system ERROR line as an app bug. If business UI assertions pass and hilog contains only unrelated system noise, report that no fatal target-app runtime error was found.

`hilog_capture.py` discovers the target application's PID with `pidof`, falls back to an exact process-name match from `ps -A`, and attributes standard hilog lines by their PID field. Only when no application PID can be resolved does it retain the legacy bundle-text filter. Read the `attribution`, `process_discovery`, and `app_pids` fields in `hilog_summary.md`; a bundle-text fallback is weaker evidence and must be described as such.

## hdc Textual Failures

Some hdc versions can return process exit code 0 while printing `[Fail]`, `Device not found`, an offline target, or another command failure. The packaged runtime tools validate both the exit code and output semantics for discovery, connection, install, launch, interaction, file transfer, and hilog control commands. Treat the reported failure reason as authoritative; do not override it because the shell exit code was zero.
