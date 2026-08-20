# Cangjie Calling ArkTS

Use this reference when Cangjie actively calls ArkTS or system APIs through `ohos.ark_interop`.

## JSRuntime Guardrails

- Create and hold `JSRuntime` deliberately; do not create a fresh runtime for every call.
- Keep JS runtime work on the bound ArkTS thread.
- If a callback must run from another Cangjie thread, use `context.postJSTask { ... }`.
- Catch ArkTS-thrown errors as `JSCodeError`.

## Module Loading

Use `requireArkModule` for modern module loading:

```cangjie
let ctx = runtime.mainContext
let hilog = ctx.requireArkModule("@ohos.hilog").asObject()
```

System modules normally use their full ArkTS module names, such as `@ohos.hilog` or `@kit.PerformanceAnalysisKit`.

## Object Safety

Check object shape before conversion:

```cangjie
let obj = value.asObject()
if (obj.hasProperty("name") && obj["name"].isString()) {
    let name = obj["name"].toString()
}
```

Avoid holding circular cross-language references. If ArkTS passes callbacks into Cangjie, release them when the owner page disappears.
