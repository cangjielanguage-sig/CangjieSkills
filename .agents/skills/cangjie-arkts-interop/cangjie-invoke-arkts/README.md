---
name: cangjie-arkts-bridge
description: 根据 .d.ts、.d.ets 或 .ets 等 ArkTS 声明/接口文件生成调用 ArkTS API 的仓颉互操作封装代码。当用户要读取 ArkTS 声明、识别接口/类/函数/枚举、把 ArkTS 或 TypeScript 风格 API 转成仓颉互操作封装、生成封装代码、创建 ark_wrapper 目录、或产出仓颉与 ArkTS 的互操作胶水代码时使用本 skill，即使用户未明确说「skill」或「bridge」。
---

# 仓颉 ArkTS Bridge 生成器

使用本 skill 生成从仓颉侧调用 ArkTS API 的仓颉代码。输入为一个或多个 ArkTS 声明/源文件（如 `.d.ts`、`.d.ets`、`.ets`）；输出为 `ark_wrapper/` 目录下的仓颉互操作代码。

## 工作流程

1. 定位 ArkTS 输入文件。
   - 优先采用用户给出的明确文件路径。
   - 若用户给出目录，则扫描其中的 `.d.ts`、`.d.ets`、`.ets`。
   - 若文件很多，优先处理声明文件；大范围生成前应先询问用户。
2. 解析对外 API 表面。
   - 提取导出的 interface、class、constructor、method、function、property、enum、type alias、callback 形态、异步 callback API、返回 Promise 的 API、数组、record、可选字段、可空字段以及联合类型等。
   - 保留能说明 API 行为、废弃说明、系统 API 状态或参数含义的源码注释。
   - 在生成的仓颉声明上方保留足够的原始 ArkTS 签名片段（注释中），便于用户核对映射关系。
3. 若不存在则创建 `ark_wrapper/` 目录。
4. 将固定 helper 写入 `ark_wrapper/`。
   - `ark_api_call_async.cj`
   - `callback_manager.cj`
   - `business_exception.cj`
   - 上述文件为共享运行时支撑代码，内容视为固定模板；生成 API 封装时不要重新设计其实现。
   - 权威来源与冲突处理见 `references/fixed_helpers.md`。
   - **包名：** 本 skill 随附的 helper（例如 `ark_wrapper/ark_api_call_async.cj`）可能使用占位符 `package my_module`。向用户项目生成或拷贝 helper 时，须将 **`my_module` 替换为该互操作层的实际仓颉包名**（`ark_wrapper/` 下所有文件，含三个 helper 与每个生成的封装文件，均使用同一包标识）。除非用户明确要求保留该名，否则交付代码中不要残留 `package my_module`。
   - `ark_api_call_async.cj` 直接使用当前 skill 内的本地文件 `ark_wrapper/ark_api_call_async.cj` 作为来源，不要从远程读取该文件。
   - 需要批量就位 helper 时，可在 skill 目录执行 `python3 scripts/fetch_fixed_helpers.py --bridge-dir ark_wrapper --package <package_name> --force`；脚本只使用当前 skill 内本地模板（`ark_wrapper/ark_api_call_async.cj`、`ark_wrapper/callback_manager.cj`、`ark_wrapper/business_exception.cj`）。
5. 在 `ark_wrapper/` 下生成一个或多个 API 封装 `.cj` 文件。
   - 为便于评审，可优先按「每个源声明文件对应一个生成文件」组织。
   - 文件名应稳定、可读，并与输入文件名有清晰对应关系。
   - 生成代码仅围绕输入文件中的 API 表面，不要增加无关封装。
6. 若某类型或 import 无法有把握地映射，为保持互操作层可用，将该值表示为 `JSValue`，并添加能标明未解析 ArkTS 类型的精确 `FIXME` 注释。
7. 结束时总结生成了什么、列出未解决的 `FIXME`，并说明跳过了哪些文件。

## 输出目录结构

生成的代码始终放在：

```text
ark_wrapper/
  ark_api_call_async.cj
  callback_manager.cj
  business_exception.cj
  <generated-api-file>.cj
```

包名以用户指定为准。若用户未指定，则从模块名、工程目录或声明文件名推断。若推断仍模糊，选用保守的小写蛇形包标识，并在总结中说明。

包名须一致：`ark_wrapper/` 下每个 `.cj` 的第一行 `package` 必须相同——不要交付占位符 `package my_module`，除非它本身就是目标包标识。

## 生成规则

遵循华为 DTS 转仓颉规则及 HLE 示例中的常见写法。生成非平凡封装前请先阅读 `references/translation_notes.md`。

核心模式：

- 仓颉封装文件通常 `import ohos.ark_interop.*`、`ohos.ark_interop_helper.*`、`ohos.base.*`。
- **命名一致性（强约束）**：仓颉侧生成的类名必须与对应 ArkTS 的类名保持一致，不要重命名、不加前后缀、不做风格转换（例如不要把 `AbilityInfo` 改成 `AbilityInfoWrapper` 或其他名字）。
- **命名一致性（强约束）**：仓颉侧生成的函数名也必须与 ArkTS 原函数名保持一致。仓颉支持重载时，针对同一 ArkTS 函数的不同参数形态生成“同名重载”，不要通过改函数名区分（例如必须都叫 `getMd5Sync`，不要改成 `getMd5SyncFromString` 等）。
- 偏「对象形态」的 ArkTS interface 可映射为 `public open class` 封装。
- 纯数据 interface 可映射为带字段的仓颉类，并实现 `toJSValue` 与 `fromJSValue`。
- ArkTS class 映射为包装 `JSObject` 的仓颉类，构造中调用 `getClassConstructorObj(...).toJSValue().asClass().new(...)`。
- 实例方法通过 `jsObjApiCall` 调用。
- **新增规则（全局函数优先级）**：
  - **同步函数**优先使用 `jsGlobalApiCall`。
  - **异步/Promise 函数**优先使用 `jsGlobalApiCallPromise`。
- 对 `export class StringUtil { ... }` 这类 ArkTS `class` 中的 `static` 方法，按全局静态调用处理时也优先使用 `jsGlobalApiCall` / `jsGlobalApiCallPromise`，并保持类名字符串与 ArkTS 一致（例如 `"StringUtil"`）。
- `hmsGlobalApiCall` / `ohosGlobalApiCall` 以及对应的 `*Promise` 版本属于便捷封装（用于固定前缀 `hms` 或普通 `ohos` 场景）；若无明确要求，按上述新增规则优先使用 `jsGlobalApiCall` / `jsGlobalApiCallPromise`。
- 返回 Promise 的 API 映射为 callback 风格仓颉函数，优先使用 `jsGlobalApiCallPromise`（全局函数）或 `jsObjApiCallPromise`（对象方法）。
- callback 风格的 ArkTS API 使用 `AsyncCallback` 与 `asyncCallbackWrapper`。
- enum 映射为带 `get`、`parse`、`tryParse`、`toString`、`==`、`!=` 的仓颉 enum。
- 可选与可空值映射为 `Option<T>` / `?T` 等；除非源码明确要求 `null`，否则将 `None` 转为 `ctx.undefined().toJSValue()`。
- 数组使用 `toJSArray` 与 `fromJSArray`。
- record 使用 `hashmap2Record` 与 `record2Hashmap`。
- 未知的外部 ArkTS 类型应写为 `JSValue/* FIXME: OriginalType */`，不要随意猜仓颉类型。
- 当同名符号在同一仓颉包内产生命名冲突时，优先按文件拆分与作用域消歧；若仍无法避免冲突，保留 ArkTS 原类名并在冲突位置添加明确 `FIXME` 说明后再与用户确认处理策略。
- 对 `string | Uint8Array` 这类可拆分联合参数，优先生成同名重载：
  - `string` 分支映射为 `String` 参数重载。
  - `Uint8Array` 分支映射为 `Array<UInt8>` 参数重载，并通过 `toJSArray` 传入。
  - 调用的 JS 方法名保持 ArkTS 原名（如 `"getMd5Sync"`）。
- 对 `string | undefined | null`（或 `String | string | null | undefined`）参数，优先映射为仓颉 `?String`；调用时显式转换为 `JSValue`（`Some(s)` 映射字符串，`None` 映射 `null` 或 `undefined`，按现有工程约定统一）。

## 类型映射默认表

除非本地工程或官方文档另有规定，否则默认按下表处理：

| ArkTS / TypeScript | 仓颉封装类型 |
| --- | --- |
| `string`, `String` | `String` |
| `number` | `Float64` |
| `boolean` | `Bool` |
| `void` | `Unit` |
| `bigint`, `BigInt` | `BigInt`；若 helper 支持不明则配合 `FIXME` 使用 `JSValue` |
| `T[]`, `Array<T>` | `Array<T>`，配合 `toJSArray` / `fromJSArray` |
| `Record<K, V>` | 在键值类型已知时为 `HashMap<K, V>` |
| `T \| null`, `T \| undefined`, `T?` | `Option<T>` / `?T` |
| 无法解析的 import 类型 | `JSValue/* FIXME: TypeName */` |
| 对象字面量类型 | 生成的 `AutoGenType...` 类 |

若联合类型包含多种具体值类型，在仓颉可合法重载时必须优先生成同名重载（函数名与 ArkTS 保持一致）；仅当重载在仓颉中会产生二义性或非法时，才退化为 `JSValue` 并留 `FIXME`。

## 收尾检查清单

结束前请确认：

- 所有输出文件均在 `ark_wrapper/` 下。
- `ark_wrapper/*.cj` 使用同一、明确的 `package` 声明（除非有意保留，否则不应残留 `my_module` 占位）。
- 三个固定 helper 已就位，或在说明中明确写出其为必需文件。
- 每个生成的 API 封装在需要处包含 `toJSValue` / `fromJSValue`。
- 未解析类型均有明确的 `FIXME` 注释。
- 异步 callback 与 Promise API 经 helper 函数路由，不要手写一套 Promise 处理。
- 最终回复中列出已生成文件与未解决项。

## 参考资料

- `references/translation_notes.md`：DTS 转仓颉模式与示例观察的本地摘要。
- `references/fixed_helpers.md`：固定 helper 的来源与使用要求。
- `scripts/fetch_fixed_helpers.py`：将固定运行时 helper 拉取/写入 `ark_wrapper/` 的脚本。
