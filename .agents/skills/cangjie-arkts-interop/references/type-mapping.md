# Cangjie ArkTS Type Mapping

Use this reference when writing `Index.d.ts`, `@Interop[ArkTS]` exports, or manual `JSModule.registerModule` wrappers.

## Common Mappings

| Cangjie / interop value | ArkTS / TypeScript |
| --- | --- |
| `Bool` | `boolean` |
| `Int8`, `Int16`, `Int32`, `Int64` | `number` |
| `UInt8`, `UInt16`, `UInt32`, `UInt64` | `number` |
| `Float32`, `Float64` | `number` |
| `String`, `JSStringEx` | `string` |
| `Unit` | `void` or `undefined` |
| `Option<T>` | `T \| undefined` |
| `Array<Byte>` | `ArrayBuffer` |
| Cangjie `enum` exported with `@Interop` | `const enum` |
| `@Interop interface` | TypeScript `interface` |
| `@Interop class` | TypeScript `class` |

## Manual `JSModule.registerModule`

Manual wrappers convert through `JSCallInfo` and `JSContext`:

```cangjie
let s = callInfo[0].toString()
let n = callInfo[1].toNumber()
let out = runtime.string("${s}: ${n}").toJSValue()
```

Then declare the ArkTS side:

```typescript
export declare function formatScore(name: string, score: number): string
```

## `@Interop[ArkTS]` Rules

- Exported functions/classes/enums must be `public`.
- Avoid generics and default parameter values at the boundary.
- For interfaces, use `prop` or `mut prop`, not normal Cangjie fields.
- Use `@Interop[ArkTS, Invisible]` for class members ArkTS cannot understand.
- Keep enum types end-to-end; do not silently replace exported enums with `Int64` in signatures.
- For async exports, prefer simple value parameters or JSON strings. Avoid passing JS runtime-bound objects across worker threads.

## Declaration Integrity

Treat `.d.ts` as a contract:

- If Cangjie export name changes, update `.d.ts` and ArkTS imports.
- If return conversion changes from `string` to `number`, update `.d.ts`.
- If `.d.ts` declares a function not registered/exported by Cangjie, ArkTS can compile but fail at runtime.
- If Cangjie exports a symbol but `.d.ts` omits it, `CompileArkTS` can fail at import or type checking.
