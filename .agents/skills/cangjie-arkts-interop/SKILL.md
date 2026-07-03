---
name: cangjie-arkts-interop
description: "HarmonyOS ArkTS interop guidance for Cangjie projects. Use when the task involves @Interop macros, generated .d.ts files, ohos.ark_interop manual registration, Cangjie/ArkTS type mapping, cross-language calls, or symbol conflicts. For routine .cj language/API code without ArkTS interop, use cangjie-lang-features and cangjie-std."
---

# 仓颉 ↔ ArkTS 互操作 Skill

## 路径选择（必读）：**互操作宏优先于互操作库**

在 **ArkTS 调用仓颉** 的场景下，官方与工程实践均明确：

- **首选**：**仓颉-ArkTS 声明式互操作宏**（`ohos.ark_interop_macro`，`@Interop`）。它解析被注解的仓颉代码，**自动生成 ArkTS 声明（`.d.ts`）与互操作胶水层**，开发体验接近「在 ArkTS 里调普通 TS 函数」。
- **备选**：**仓颉-ArkTS 互操作库**（`ohos.ark_interop`，手工 `JSContext` / `JSCallInfo` / `JSModule.registerModule` 等）。能力更底层、更灵活，但样板代码多、易踩线程/类型/生命周期坑；**仅当宏无法满足需求时再使用**。

> **说明（方向不同，工具不同）**：`@Interop` 主要解决「**把仓颉 API 以声明式方式导出给 ArkTS**」。而「**仓颉应用里调用 ArkTS 系统模块/API**」通常仍以 `ohos.ark_interop` 中的 `JSRuntime` / `JSContext` / `requireSystemNativeModule` 等为主（可与宏导出的回调、注册函数配合使用）。

互操作核心类型（概念层面）：`JSValue`、`JSContext`、`JSCallInfo`、`JSRuntime`。

---

## 0. 动手前要确认的 5 件事

1. **调用方向**：ArkTS → 仓颉？仓颉 → ArkTS？还是双向？
2. **导出形态**：普通函数、异步 Promise、传 ArkTS 对象（interface）、返回仓颉对象（class）、枚举？
3. **类型边界**：是否涉及 `JSStringEx` / `JSArrayEx<T>` / `JSHashMapEx<K,V>`、回调、多线程？
4. **线程约束**：`JSRuntime` 创建、以及与 ArkTS 运行时绑定的互操作逻辑，常见要求 **主线程或运行时绑定线程**（以官方文档与报错为准）。
5. **工程集成**：包名是否与 `cjpm.toml`、`lib*.so`、ArkTS `import` 一致；生成 `.d.ts` 后 `oh-package.json5` 依赖是否已加入。

---

## 1. 声明式互操作宏 `@Interop`（ArkTS 调用仓颉 —— **首选**）

### 1.1 必备 import

```cangjie
import ohos.ark_interop.*
import ohos.ark_interop_macro.*
```

宏生成与运行时仍依赖 `ark_interop`；**不要**以为「用了宏就完全不用互操作库」——宏生成的是胶水层，底层仍走互操作运行时。

### 1.2 最小示例：导出普通函数给 ArkTS

```cangjie
// 包名须与 cjpm.toml 的 package name 一致
package ohos_app_cangjie_entry

import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public func addF64(a: Float64, b!: Float64): Float64 {
    a + b
}
```

在 DevEco Studio 中对仓颉源文件右键 **Generate... → Cangjie-ArkTS Interop API**，会在 `cangjie/types/libohos_app_cangjie_entry` 下生成 `Index.d.ts` 等，ArkTS 侧即可按生成签名导入 `libohos_app_cangjie_entry.so` 调用。

### 1.3 异步函数：`@Interop[ArkTS, Async]`

适用于 **ArkTS 侧希望得到 `Promise`** 的耗时仓颉逻辑：

```cangjie
@Interop[ArkTS, Async]
public func doAsync(a: Float64, b: Float64): Float64 {
    a + b
}
```

生成的 ArkTS 声明形态类似：`Promise<number>`。

**异步函数额外限制（编译期约束）**：

- `JSStringEx`、`JSArrayEx<T>`、`JSHashMapEx<K, V>` **不能**在异步互操作函数中使用。

### 1.4 场景选择速查（官方分类）

| 目标 | 形态 | 宏写法 |
|------|------|--------|
| ArkTS 调用仓颉函数 | 函数 | `@Interop[ArkTS]` |
| ArkTS 调用耗时仓颉逻辑 | 异步函数 | `@Interop[ArkTS, Async]` |
| 把 ArkTS 创建的对象传给仓颉 | `interface` | `@Interop[ArkTS]` |
| 把仓颉创建的对象返回给 ArkTS | `class` | `@Interop[ArkTS]`；不暴露成员用 `@Interop[ArkTS, Invisible]` |
| 双向传递枚举 | `enum` | `@Interop[ArkTS]` |

### 1.5 `@Interop` 通用约束（函数/interface/class/枚举）

**函数（含异步）常见硬约束**：

- 必须由 **`public`** 修饰
- **不支持**类型参数（泛型）
- **不支持**参数默认值
- 可走命名参数，但 ArkTS 调用形态与普通参数一致（不要依赖「只存在于仓颉侧」的默认参数）

**接口 `interface` 约束（节选）**：

- `public`，**不支持**泛型，**不支持**继承其他接口
- 成员函数、属性规则与函数类似；不支持操作符重载

**类 `class` 约束（节选）**：

- `public`；**不支持**泛型；构造函数需 `public`，**不支持**成员变量形参、不支持参数默认值
- 可继承类/接口但「不会展开」——设计导出面时要克制
- 不准备暴露给 ArkTS 的成员：可用 **`@Interop[ArkTS, Invisible]`** 或 **非 public** 等方式隐藏（见官方 class 文档）

**语法糖限制**：

- 在 `Interop` 应用的函数签名、成员类型标注中，**不支持** `Option<T>` 的 `?T` 语法糖（须写完整 `Option<T>`）。

### 1.6 类型映射（宏路径下常用）

宏路径下 ArkTS 与仓颉类型对应关系（节选，完整表见官方「类型映射」文档）：

| 仓颉 | ArkTS | 备注 |
|------|-------|------|
| `Int8`…`Float64` 等数值类型 | `number` | |
| `Bool` | `boolean` | |
| `String`、`JSStringEx` | `string` | |
| `Unit` | `undefined` | |
| `Option<T>` | `T \| undefined` | `T` 不能再是 `Option` 或函数类型；自定义类型须也被 `Interop` 修饰 |
| `func` | `function` | |
| `JSArrayEx<T>` | `Array<T>` | `T` 不能是函数；自定义类型须 `Interop` |
| `JSHashMapEx<K,V>` | `Map<K,V>` | `V` 不能是函数；自定义类型须 `Interop` |
| `Array<Byte>` | `ArrayBuffer` | |
| `enum` | `const enum` | |
| `class` / `interface` | `class` / `interface` | |

> `JSStringEx`、`JSArrayEx<T>`、`JSHashMapEx<K,V>` **只能**出现在被 `Interop` 修饰的函数、class、interface 中。

### 1.7 命名与符号冲突（必踩坑清单）

同一仓颉模块（同包及其子包）内须避免：

1. **多个 `@Interop` 导出同名** 的函数/interface/class（会编译报错或父子包符号覆盖）。
2. **`@Interop` 导出物** 与 **`JSModule.registerModule` / `registerClass` / `registerFunc` 注册名** **同名**（后者可能覆盖前者）。

**结论**：只要能用宏表达导出，就 **不要** 再手写 `registerModule` 去导同名符号。

---

## 2. 互操作库 `ohos.ark_interop`（底层动态接口 —— **宏不够用再用**）

适用场景（示例）：

- 需要 **完全动态** 的 `JSValue` 处理、反射式对象操作、或宏类型系统暂时覆盖不到的边界场景
- 需要在仓颉里 **精细控制** `exports` 表、`runtime.function(...)` 的注册过程
- **仓颉调用 ArkTS**：加载系统模块、`JSObject`/`JSFunction` 调用等

### 2.1 手工导出函数（示意：回调 ArkTS）

仅作对照学习；若只是「导出函数给 ArkTS」，请优先改用 **§1 宏**。

```cangjie
internal func addByCallback(context: JSContext, callInfo: JSCallInfo): JSValue {
    let a = callInfo[0].toNumber()
    let b = callInfo[1].toNumber()
    let callback = callInfo[2].asFunction()
    let ret = context.number(a + b).toJSValue()
    callback.call(ret)
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports =>
        exports["addByCallback"] = runtime.function(addByCallback).toJSValue()
}
```

### 2.2 `thisArg`：方法从对象上取出再调用

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let object = callInfo[0].asObject()
    object.callMethod("doSth")
    let f = object["doSth"].asFunction()
    f.call(thisArg: object.toJSValue())
}
```

### 2.3 `JSExternal`：把仓颉对象挂到 `JSObject` 上（库路径的典型模式）

宏路径若可用 `class` 直接导出，通常更简单；此模式多在需要 **手搓对象表面** 时使用。

（示例可参考本仓库文档快照：`skills/cangjie-hmos-doc-search/application-dev/operating_cangjie_objects/ArkTS_访问仓颉数据/JSExternal.md`）

---

## 3. 仓颉调用 ArkTS（复用 ArkTS API）

宏主要解决 **导出给 ArkTS**；从仓颉侧 **调用 ArkTS 模块** 仍常用：

```cangjie
import ohos.ark_interop.*

func tryLoadArkTSModule() {
    let runtime = JSRuntime()
    let context = runtime.mainContext
    let module = context.requireSystemNativeModule("file.photoAccessHelper")
    let obj = module.asObject()
    // obj.callMethod(...)
}
```

`JSValue` **拷贝 vs 引用**、属性写入静默失败、`thisArg` 等问题仍按互操作库文档处理。

---

## 4. 并发 / 异步 / 多引擎（遇到再深入）

- 异步互操作：优先 **`@Interop[ArkTS, Async]`**，避免手写 Promise 胶水（除非宏不满足）。
- 多线程：互操作逻辑须在**与 ArkTS 运行时绑定的系统线程**上执行；不要想当然跨线程触摸同一 `JSContext`。
- 需要跨语言锁/sentinel 时，再查阅「AsyncLock、Sendable」等专题文档。

---

## 5. 排障清单（10 分钟定位大部分问题）

1. **该不该用宏**：能 `@Interop` 就用；避免 `registerModule` 与 `@Interop` 同名覆盖。
2. **包名 / `.so` 名 / ArkTS import** 是否一致。
3. **`public`/无泛型/无默认值** 是否违反宏约束。
4. **异步函数** 是否误用 `JSStringEx` / `JSArrayEx` / `JSHashMapEx`。
5. **`this` 丢失**：`JSFunction.call` 是否补 `thisArg`。
6. **JSValue 生命周期**：该拷贝还是该保留引用类型。
7. **对象属性写入无报错**：密封/只读属性可能“静默失败”。

---

## 6. 参考资料

- OpenHarmony 仓颉文档目录（互操作总入口）：https://gitcode.com/openharmony/docs_cangjie/tree/master/zh-cn/application-dev/learn-cj/FFI/cangjie-arkts
- 本仓库随附文档快照（可用 `cangjie-hmos-doc-search` 检索）：
  - **声明式互操作宏**：`skills/cangjie-hmos-doc-search/application-dev/cj-arkts_interoperability_macro/仓颉-ArkTS_声明式互操作宏/`
  - **互操作库（手工方式，宏的备选）**：`skills/cangjie-hmos-doc-search/application-dev/cj-arkts_interoperability_lib/cj-arkts_interoperability_lib.md`
  - **宏使用方法（含 Generate 流程）**：`.../使用方法/使用方法_2more.md`
  - **场景：异步/接口/类/枚举**：`.../场景详细说明/场景详细说明_4more.md`
  - **类型映射表**：`.../类型映射.md`
  - **互操作概述**：`skills/cangjie-hmos-doc-search/application-dev/cangjie_arkts_overview/cangjie_arkts_overview.md`
