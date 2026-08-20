# ArkTS Calling Cangjie

Use this reference when ArkTS imports and calls functions exported by a Cangjie dynamic library.

## JSModule.registerModule Pattern

Cangjie export:

```cangjie
package ohos_app_cangjie_entry

import ohos.ark_interop.JSModule
import ohos.ark_interop.JSContext
import ohos.ark_interop.JSCallInfo
import ohos.ark_interop.JSValue

func greet(runtime: JSContext, callInfo: JSCallInfo): JSValue {
    let name = callInfo[0].toString()
    runtime.string("Hello ${name}").toJSValue()
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports =>
        exports["greet"] = runtime.function(greet).toJSValue()
}
```

The trailing lambda already owns the following indented statements. Do not write `runtime, exports => { ... }`; that ArkTS-style extra block produces Cangjie `expected '=>' in lambda expression` errors at the first `exports[...]` line.

Type declaration:

```typescript
export declare function greet(name: string): string
```

ArkTS call:

```typescript
import { greet } from 'libohos_app_cangjie_entry.so';

this.message = greet('Cangjie');
```

## Synchronization Rule

Every new or renamed export must update three places in the same change:

1. Cangjie `exports["name"] = runtime.function(funcName).toJSValue()`
2. `src/main/cangjie/types/lib<package>/Index.d.ts`
3. ArkTS import/call site

Then rebuild. `CompileCangjie` can pass while `CompileArkTS` fails if the declaration/import is stale.

## Basic Mapping

| Cangjie JSValue operation | ArkTS declaration |
| --- | --- |
| `runtime.string(...).toJSValue()` | `string` |
| `runtime.number(...).toJSValue()` | `number` |
| `runtime.boolean(...).toJSValue()` | `boolean` |
| `runtime.undefined().toJSValue()` | `void` / `undefined` |

For parameters, read from `JSCallInfo` by index and convert explicitly:

```cangjie
let s = callInfo[0].toString()
let n = callInfo[1].toNumber()
let b = callInfo[2].toBoolean()
```

## When to Prefer `@Interop`

Use `@Interop[ArkTS]` for typed public functions/classes/enums when the macro flow is available and generated declarations can be refreshed in DevEco. Use `JSModule.registerModule` for small manual exports, dynamic JSValue handling, or cases where the macro does not cover the boundary.
