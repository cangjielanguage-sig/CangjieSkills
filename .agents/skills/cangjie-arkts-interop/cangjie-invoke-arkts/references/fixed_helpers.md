# Fixed Helper Files

Generated bridge output must include these shared helper files in `ark_wrapper/`:

- `ark_api_call_async.cj`
- `callback_manager.cj`
- `business_exception.cj`

Treat these helper files as fixed runtime support code. Do not refactor, rename public symbols, change error handling, or inline their logic into generated API wrappers.

## Authoritative Sources

本 skill 已内置三个 helper 文件，处理时仅使用本地副本，不需要从远程读取：

| File | Source |
| --- | --- |
| `ark_api_call_async.cj` | `ark_wrapper/ark_api_call_async.cj` |
| `callback_manager.cj` | `ark_wrapper/callback_manager.cj` |
| `business_exception.cj` | `ark_wrapper/business_exception.cj` |

## Package Name

The helper files in the reference repository use:

```cj
package my_module
```

When generating a real bridge, update only the `package` declaration to match the generated bridge package if needed. Keep the rest of each helper file unchanged.

This skill may ship `ark_wrapper/ark_api_call_async.cj` with `package my_module` as a placeholder; when producing output for a project, replace `my_module` with the actual bridge package name on **all** helpers and generated wrappers so every file under `ark_wrapper/` agrees.

## Conflict Handling

If `ark_wrapper/` already contains one of these helper files:

1. If the file matches the fixed helper content except for package name, leave it in place.
2. If the file differs and the user did not ask to regenerate helpers, warn before overwriting.
3. If the user explicitly asked to regenerate bridge code, replace the helper with the fixed version and preserve the selected package declaration.

The bundled `scripts/fetch_fixed_helpers.py` script reads local templates only and rewrites only the package declaration:

```sh
python3 scripts/fetch_fixed_helpers.py --bridge-dir ark_wrapper --package <package_name> --force
```

## Required Symbols

Generated wrappers may rely on these helper symbols:

- `EMPTY_ARG`
- `getMainContext`
- `checkThreadAndCall`
- `getJSModule`
- `getClassConstructorObj`
- `jsObjApiCall`
- `hmsGlobalApiCall`
- `ohosGlobalApiCall`
- `jsObjApiCallPromise`
- `hmsGlobalApiCallPromise`
- `ohosGlobalApiCallPromise`
- `asyncCallbackWrapper`
- `toJSArray`
- `fromJSArray`
- `fromJSArrayOption`
- `hashmap2Record`
- `record2Hashmap`
- `BusinessException`
- `AsyncCallback`
- `CallbackManager`
- `CallbackObject` wrapper classes from `callback_manager.cj`

If a generated wrapper needs behavior outside these helpers, prefer adding a small local conversion function in the generated API file rather than modifying the helper files.
