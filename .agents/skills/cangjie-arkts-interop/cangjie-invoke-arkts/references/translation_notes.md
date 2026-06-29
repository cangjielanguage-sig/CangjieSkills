# ArkTS to Cangjie Bridge Translation Notes

These notes summarize the rules to apply when generating Cangjie wrappers for ArkTS `.d.ts`, `.d.ets`, or `.ets` APIs.

Primary references:

- Huawei Cangjie guide: `https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-dts2cj-translation-rules`
- HLE development guide: `https://raw.githubusercontent.com/causerp/cangjie_tools/dev/hyperlangExtension/doc/developer_guide_zh.md`
- HLE examples: `https://github.com/causerp/cangjie_tools/tree/dev/hyperlangExtension/tests/expected/my_module`

## High-Level Shape

The HLE generator reads ArkTS declaration files, extracts interface metadata, builds an intermediate model, then produces Cangjie wrapper code. This skill should follow the same idea manually:

1. Parse the API declarations.
2. Classify each declaration as data object, wrapped object/class, global function, enum, callback, alias, or unsupported external type.
3. Generate Cangjie declarations that marshal arguments to `JSValue`, call ArkTS through helper functions, and unmarshal return values back to Cangjie types.

## File Structure

Generated wrapper files usually start with:

```cj
package <module_name>

import ohos.ark_interop.*
import ohos.ark_interop_helper.*
import ohos.base.*
```

Add `std.collection.{ HashMap }` when generating records, and add other imports only when the generated code needs them.

Per this skill’s layout, place fixed helpers and generated wrapper `.cj` files under `ark_wrapper/`.

## Interfaces

For a data-only interface:

- Generate `public open class <Name>`.
- Store fields as constructor parameters.
- Generate `toJSValue(context: JSContext): JSValue`.
- Generate `static func fromJSValue(context: JSContext, input: JSValue): <Name>`.
- Read/write object fields through `context.object()` and `input.asObject()`.

For an object interface with methods:

- Generate a wrapper with `protected <Name>(var arkts_object: JSObject)`.
- Generate instance methods that call `jsObjApiCall`.
- Generate `toJSValue` by returning `arkts_object.toJSValue()`.
- Generate `fromJSValue` by wrapping `input.asObject()`.

## Classes

For ArkTS classes:

- Generate a Cangjie class with `var arkts_object: JSObject`.
- Constructors call `getClassConstructorObj(<module>, <className>).toJSValue().asClass().new(...)`.
- Static methods call `jsObjApiCall` on `getClassConstructorObj(...)`.
- Instance methods call `jsObjApiCall` on `arkts_object`.
- Properties become Cangjie `prop` / `mut prop` with getter/setter bodies that read/write `arkts_object["name"]`.

## Functions

For global functions:

- Use `hmsGlobalApiCall` when the module is known to use the `hms` prefix.
- Use `ohosGlobalApiCall` when the module is a normal OHOS global module.
- If the prefix is unknown, prefer the user's module instruction; otherwise add a note in the summary.

For object methods:

- Use `jsObjApiCall<T>(arkts_object, "methodName", { ctx => [...] })`.
- Use `EMPTY_ARG` for zero-argument calls.

## Async APIs

For callbacks:

- Use `AsyncCallback<T>` from `business_exception.cj`.
- Convert Cangjie callbacks to ArkTS callbacks with `asyncCallbackWrapper`.

For Promise-returning APIs:

- Expose a callback-style Cangjie function.
- Use `jsObjApiCallPromise` or `jsGlobalApiCallPromise`.
- Convert Promise resolution values with the same return-value parsing logic as sync APIs.

## Enums

Generate Cangjie enums with:

- variants for each ArkTS enum member
- `get()` returning the wire value
- `parse(...)`
- `tryParse(...)`
- `toString()`
- equality and inequality operators

String enums parse from `String`; numeric enums parse from `Int32`. Heterogeneous enums are safer as string-backed unless the official rule or examples show a better mapping.

## Type Mapping

| ArkTS / TypeScript | Cangjie bridge representation |
| --- | --- |
| `string`, `String` | `String` |
| `number` | `Float64` |
| `boolean` | `Bool` |
| `void` | `Unit` |
| `bigint`, `BigInt` | `BigInt` if supported locally; otherwise `JSValue/* FIXME: `BigInt` */` |
| `Uint8Array` | `Array<UInt8>` when marshaling is clear |
| `T[]`, `Array<T>` | `Array<T>` |
| `Record<K, V>` | `HashMap<K, V>` if both types are known |
| `Promise<T>` | callback-style API with `AsyncCallback<T>` |
| function type | Cangjie function type plus `toJSFunction` / `fromJSFunction` when needed |
| `null`, `undefined`, optional property | `Option<T>` / `?T` |
| unknown imported type | `JSValue/* FIXME: OriginalType */` |

## Optional and Nullable Values

Use `Option<T>` or `?T` for nullable/optional values. When passing values to ArkTS:

```cj
match(value) {
case None => ctx.undefined().toJSValue()
case _ => value.getOrThrow().toJSValue(ctx)
}
```

When reading from ArkTS:

```cj
if (obj["field"].isNull()) {
 None < T >
} else {
 T.fromJSValue(context, obj["field"])
}
```

If the source explicitly distinguishes `null` from `undefined`, keep a `FIXME` because many wrappers collapse both to `None`.

## Unsupported or Ambiguous Types

Do not invent a mapping for project-specific ArkTS imports, framework classes, nested generic edge cases, or opaque runtime objects. Use `JSValue` with a precise `FIXME`, for example:

```cj
listener: JSValue/* FIXME: `WbASListener` */
```

This keeps the generated bridge reviewable and avoids silently incorrect conversions.
