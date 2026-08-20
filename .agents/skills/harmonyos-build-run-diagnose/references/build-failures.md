# Build Failure Patterns

## cjpm Incremental Cache Deserialization

Signature:

```text
Failed :entry:default@CompileCangjie
DataModelException: This data is not DataModelString.
cjpm.implement.DepModel::loadDepIncrementalCache
```

Treat this as a project-local cache/intermediate compatibility problem before editing application code.

Recovery:

1. Keep the relevant `build.log` excerpt.
2. Remove only paths inside the project root:
   - `.hvigor/cache`
   - `.hvigor/dependencyMap`
   - `<module>/build/default/intermediates/cj`
   - `<module>/build/default/intermediates/loader`
   - `<module>/build/default/intermediates/source_map`
3. Rebuild with `build_recovery.py --retry`.
4. If it repeats, temporarily set `[profile.build] incremental = false` in `<module>/cjpm.toml`, rebuild, and record whether the setting was kept.

## cjpm Cannot Create a Deep Build-Log Path on Windows

Signature:

```text
Failed :<module>:default@CompileCangjie
Failed to open the file ...\.build-logs\<package>\<package>.<target>..Default.outlog
The system cannot find the path specified.
Error: create '...' failed
```

Measure the reported absolute path. Cangjie 1.1.0 `cjpm` can fail when its generated path exceeds the traditional 260-character Windows limit even when `LongPathsEnabled` is enabled. Recreate or move the project to a shorter root and rebuild before changing source or configuration. A successful build from the shorter root confirms a path-length failure; cache cleanup alone does not fix it.

## hdc Missing From PATH

Signature:

```text
hdc : The term 'hdc' is not recognized
```

Use the DevEco toolchains path directly or add it to the current shell PATH:

```powershell
$env:PATH = "C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains;$env:PATH"
```

## stdx Package or Link Failure

Signatures include `stdx`, `cannot find library`, `package not found`, or `undefined symbol`.

Check:

1. Target platform matches the emulator/device ABI.
2. `<module>/cjpm.toml` target config has the correct `bin-dependencies.path-option`.
3. x86_64 is used for emulator, aarch64 for most physical devices.
4. Run `python -B <harmonyos-project-bootstrap-skill>/tools/setup_harmonyos_stdx.py --project <project>/<module>` to repair both HarmonyOS targets.
5. Run `cjpm clean`, then rebuild after dependency path changes.

## ArkTS Habit Copied Into Cangjie

| Log or source clue | Likely cause | Fix |
| --- | --- | --- |
| `expected type name after ':'` with `{left: 20}` | ArkTS object literal used in Cangjie | Use named parameters, for example `.margin(left: 20.vp)` |
| `'trim' is not a member of struct 'String'` | JS/ArkTS String API assumed | Check Cangjie String docs; use `trimAscii()` when suitable |
| `'length' is not a member of class 'ObservedArrayList'` | JS array length used on observed list | Use `.size` |
| `'add' is not a member of class 'ObservedArrayList'` | Generic collection method assumed | Use `.append(value)` for appending items |
| Length/spacing overload mismatch | Missing unit or wrong numeric type | Use `.vp`, `.percent`, or documented option types |

Always inspect the source line before applying a pattern.

## JSModule Export Lambda Has an Extra Block

Signature:

```text
expected '=>' in lambda expression, found 'exports'
exports["name"] = runtime.function(...)
```

For `JSModule.registerModule`, keep the Cangjie trailing-lambda form without an ArkTS-style block after `=>`:

```cangjie
let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports =>
    exports["name"] = runtime.function(exportedFunc).toJSValue()
}
```

## ArkTS Builder Contains a Local Statement

Signature:

```text
Only UI component syntax can be written here
```

An ArkTS `@Builder` body accepts UI component syntax, not an arbitrary local declaration such as `const status = ...`. Move the calculation into a method or the caller, pass the value as a builder parameter, or call a side-effect-free helper inline.

## Cross-Package Cangjie Component Calls the Generated Constructor

Signatures include missing arguments for `Option<CustomView>` / `Option<LocalStorage>`, or an unexpected hidden generated parameter when calling `ChildPage()`.

For a Cangjie ArkUI component in a subpackage:

1. Put its source in the matching subdirectory and declare the component `public`.
2. Give it at least one `var` construction property, even when it is a private defaulted token.
3. Instantiate it declaratively with that named property, for example `ChildPage(pageToken: 0)`.

Rebuild from source after changing the package/component boundary; do not call generated `__gen_*` constructor parameters directly.
