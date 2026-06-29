# 仓颉桥接规则

`@Interop[ArkTS]` 宏的约束、场景速查和回调桥接模式。

## 修饰符约束

`@Interop[ArkTS]` 宏作用域内，类和方法只支持 `public` 修饰符，不支持 `open`、`protected`、`mut` 等其他修饰符。编译器会报错 `Modifier only supports public within the Interop macro scope`。

## 导入约束

生成 `bridge/` 下的仓颉互操作文件前，先读取模块 `cjpm.toml` 的 `[package].name`，不要猜包名。所有 `src/main/cangjie/bridge/` 下生成的 `.cj` 文件必须使用：

```cj
package <package.name>.bridge

import <package.name>.*
```

例如 `cjpm.toml` 中是：

```toml
[package]
name = "ohos_app_cangjie_library"
```

则 bridge 文件开头必须是：

```cj
package ohos_app_cangjie_library.bridge

import ohos_app_cangjie_library.*
```

使用 `@Interop[ArkTS]` 时，还必须同时导入两个互操作包：

```cj
import ohos.ark_interop.*
import ohos.ark_interop_macro.*
```

### 跨包调用命名规则（默认用短名）

bridge 文件已经固定要求 `import <package.name>.*`。如果需要调用业务实现，再额外导入 `import <package.name>.bussiness.*`。在 bridge 内调用业务包符号时：

- **默认使用短名**：例如 `ContextTestExample()`、`RecordDownloadInfo(...)`。
- **仅当出现同名冲突/歧义时**才使用全限定名：例如 bridge 包内也存在同名类型时，业务类型写成 `<package.name>.bussiness.<TypeName>` 以消除歧义。

**目标**：在不引入歧义的前提下，让 bridge 代码更简洁、可读。

## 文件位置约束

生成的仓颉互操作 wrapper 代码必须放在对应模块的 `src/main/cangjie/bridge/` 目录下，包括：

- `@Interop[ArkTS]` 标注的 class、interface、func 所在文件
- `GlobalContext.cj`
- 手写 `SharedObject & JSInteropType<T>` 互操作类型
- 只服务互操作边界的参数转换、集合转换、句柄存储等 helper

业务实现代码保留在原业务目录，不要为了互操作把业务类整体搬进 `bridge/`；在 `bridge/` 中生成边界层来调用业务实现。

反向扫描也要遵守这个边界：搜索业务代码、扫描待翻译 public API、生成函数级翻译覆盖表时，必须排除 `src/main/cangjie/bridge/` 和 `src/main/cangjie/mock/`。`bridge/` 目录只用来放生成的互操作 wrapper，`mock/` 目录只用来放测试、兼容或替身实现，不要把其中的 `.cj` 文件再次当作业务代码输入。

## 宏场景速查

| 目标 | 形态 | 宏写法 |
|------|------|--------|
| ArkTS 调用仓颉函数 | 函数 | `@Interop[ArkTS]` |
| ArkTS 调用耗时仓颉逻辑 | 异步函数 | `@Interop[ArkTS, Async]` |
| 把 ArkTS 创建的对象传给仓颉 | `interface` | `@Interop[ArkTS]` |
| 把仓颉创建的对象返回给 ArkTS | `class` | `@Interop[ArkTS]` |
| 双向传递枚举 | `enum` | `@Interop[ArkTS]` |
| 隐藏 class 成员 | class 成员 | `@Interop[ArkTS, Invisible]` 或非 public |

### 异步函数

```cj
@Interop[ArkTS, Async]
public func doAsync(a: Float64, b: Float64): Float64 {
    a + b
}
```

异步函数额外限制：`JSStringEx`、`JSArrayEx<T>`、`JSHashMapEx<K, V>` 不能在异步互操作函数中使用。

## 通用约束

- `@Interop` 导出的函数、interface、class、enum 必须是 `public`。
- 不支持类型参数（泛型）和参数默认值。
- 在 `Interop` 应用的函数签名、成员类型标注中，不支持 `Option<T>` 的 `?T` 语法糖；须写完整 `Option<T>`。
- interface 不支持泛型和继承其他接口。
- class 不支持泛型；构造函数需 `public`，不支持成员变量形参和参数默认值。
- bridge 文件命名规则：`<业务文件名去掉.cj>Bridge.cj`，例如 `FileDownloaderManager.cj` → `FileDownloaderManagerBridge.cj`。
- class / interface / 顶层 func 命名规则：由于 `bridge/` 使用独立包名 `<cjpm.toml [package].name>.bridge` 与业务包隔离，默认优先同名；仅在产生冲突时在 class / interface / 顶层 func 名称后加 `Bridge` 后缀，例如 `FileDownloaderManager` → `FileDownloaderManagerBridge`；冲突时在覆盖表记录 `原名 -> 新名`。
- **成员函数名不受以上规则影响，永远与业务代码保持一致，不加任何后缀**。

## interface 翻译规则

翻译仓颉 `interface` 时，互操作侧代码也必须位于 `src/main/cangjie/bridge/`。如果原 interface 已在 `bridge/` 内，优先在原 interface 上直接添加 `@Interop[ArkTS]`；如果原 interface 在业务目录中，则在 `bridge/` 中生成同名互操作 interface，不要再额外生成一个继承它的 bridge interface 或 wrapper interface。互操作导出的命名、生成声明中的命名、ArkTS wrapper 中引用的命名都与原仓颉 interface 名称保持一致，除非工程已有同名冲突或用户明确要求改名。

添加 `@Interop[ArkTS]` 前，必须扫描 interface 的所有 `public` 方法签名和属性类型，并把普通仓颉集合类型替换成互操作集合类型：

| 原仓颉类型 | 互操作签名类型 | ArkTS 声明类型 |
|------------|----------------|----------------|
| `HashMap<K, V>` | `JSHashMapEx<K, V>` | `Map<K, V>` |
| `Array<T>` | `JSArrayEx<T>` | `Array<T>` |

示例：

```cj
package <package.name>.bridge

import <package.name>.*
import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public interface UserRepo {
    public func findAll(): JSArrayEx<String>
    public func findMeta(): JSHashMapEx<String, String>
}
```

如果原业务 interface 中已经使用 `HashMap` 或 `Array`，不要直接把原签名暴露给 ArkTS；先把边界签名改成 `JSHashMapEx` / `JSArrayEx`，必要时在实现层做一次转换。`JSArrayEx<T>` 和 `JSHashMapEx<K, V>` 只用于互操作边界，业务内部仍可继续使用普通 `Array` / `HashMap`。

### JSHashMapEx / JSArrayEx 与 JSCurrentJSContext

在互操作桥接层中，当需要**主动构造** `JSHashMapEx<K, V>` 或 `JSArrayEx<T>` 等依赖当前 JS 运行时的互操作集合时，必须在构造与使用期间**显式设置当前 JSContext**，并在使用结束后及时恢复：

```cj
// mainThreadContext 为主线程 JSContext（例如在初始化阶段保存的主线程上下文）
JSCurrentJSContext.set(mainThreadContext)

let jsMap = JSHashMapEx<String, String>()
for ((key, value) in downData) {
    jsMap[key] = value
}

arktsListener.onSetUbtData(ubtType, jsMap)

JSCurrentJSContext.unset()
```

推荐模式：

- **进入互操作集合构造前**：调用 `JSCurrentJSContext.set(mainThreadContext)`，其中 `mainThreadContext` 必须是当前线程可用、与 ArkTS 交互的主 JSContext。
- **完成所有对 `JSHashMapEx` / `JSArrayEx` 的写入和回调调用后**：调用 `JSCurrentJSContext.unset()`，避免在后续业务逻辑中意外复用过期的 JSContext。
- 不要在多个并发线程上同时共享同一个 `JSCurrentJSContext`，也不要在未设置 context 的情况下创建或操作 `JSHashMapEx` / `JSArrayEx`。

同一仓颉模块及其子包内避免：

- 多个 `@Interop` 导出同名函数、interface、class 或 enum。
- `@Interop` 导出物与 `JSModule.registerModule`、`registerClass`、`registerFunc` 的注册名同名。
- 复制或派生工程后旧声明覆盖新声明。
- **`@Interop` 类之间相互引用**（见下文「`@Interop` 类之间禁止相互引用」）。

## `@Interop` 类之间禁止相互引用

`@Interop[ArkTS]` 标注的类只是 ArkTS 与仓颉之间的边界桥接，不是普通仓颉类。**不能让一个 `@Interop` 类在方法签名、返回值、成员变量、参数类型中引用另一个 `@Interop` 类**；否则生成的声明和运行时转换会出现不一致，典型表现为：ArkTS 侧拿到的对象类型错乱、构造签名丢失、`undefined` 调用、或编译期报 `type not exported`。

### 先问自己：是否允许改变业务 public API 形态？

**默认不允许（preserve_public_api_shape = true）。**

如果业务 API 本身就是“跨类对象传递”（例如 `configure(): Father`、`paramTest(a: Father)`），并且希望 ArkTS 侧仍然以“对象”形式拿到/传入 `Father`，那么这类 API **不能**用 `@Interop[ArkTS]` 宏来实现；应直接使用 **手写互操作库**（`SharedObject & JSInteropType<T>` + `JSModule.registerClass` + `toJSValue/fromJSValue`），以保持签名不变。

只有在**用户明确同意改变 API 形态**时，才允许退而求其次用 **句柄模式**（把 `Father` 改为 `Int64`/`String` id 等扁平类型）。一旦选择句柄模式，必须在最终“翻译覆盖表”里标记 `API Shape Changed = yes` 并写清 `Before → After`。

### 反例（不要这样写）

```cj
@Interop[ArkTS]
public class B {
    public init() {}
    public func foo(): Unit {}
}

@Interop[ArkTS]
public class A {
    public init() {}
    public func foo(): B {   // ❌ 返回另一个 @Interop 类
        return B()
    }
}
```

### 正确做法：拆成互操作库模式

把被引用方（`B`）从 `@Interop` 桥接降级为**仓颉内部的普通 `public` 业务类**，只让真正作为 ArkTS 入口的那一个类保留 `@Interop[ArkTS]`；跨类协作留在仓颉侧完成，对 ArkTS 只暴露扁平、可序列化的参数与返回值（`String`、数值、`JSValue`、回调函数等）。

如果 ArkTS 侧确实需要持有 `B` 的实例，改用以下任一方式：

1. **句柄模式**：`A` 返回 `B` 的句柄（`String` id 或 `Int64`），仓颉侧用 `HashMap` 维护真实对象，ArkTS 后续通过句柄调用 `A` 上的方法来操作 `B`。
2. **拆成两个桥接类 + 扁平参数**：`A` 和 `B` 都保留 `@Interop[ArkTS]`，但彼此方法签名中**只传扁平参数**，不出现对方的类型；跨类状态通过仓颉内部的业务层（非 `@Interop` 的普通类）关联。
3. **手写互操作库（`SharedObject & JSInteropType<T>`）**：完全不使用 `@Interop[ArkTS]` 宏，自己实现 `JSModule.registerClass`、`jsConstructor`、每个方法的 `_ArkTS_Interop_Identifier` 跳板，以及 `toJSValue` / `fromJSValue` / `toArkTsType`。这样 `A` 和 `B` 都是手写互操作类型，返回值之间允许通过 `toJSValue` / `fromJSValue` 自由互转。适合跨类返回对象的场景。

### 选型速查（只看这一段也能做对）

| 需求 | 推荐方案 | 是否改变业务 public API 形态 |
|------|----------|-----------------------------|
| ArkTS 侧要拿到/传入真实对象（跨类对象传递），签名必须不变 | 手写互操作库（`SharedObject & JSInteropType<T>`） | 否 |
| ArkTS 侧允许只拿到句柄（id），不要求对象语义 | 句柄模式（`Int64`/`String` id） | 是（必须记录 `Before → After`） |
| 回调/listener（ArkTS 不实现仓颉 interface） | 回调桥接模式（函数参数/注册式）+ adapter | 通常否 |

改写上例（句柄模式）：

```cj
// 仓颉内部业务类，不加 @Interop
public class BImpl {
    public init() {}
    public func foo(): Unit {}
}

@Interop[ArkTS]
public class A {
    private let store: HashMap<String, BImpl> = HashMap<String, BImpl>()

    public init() {}

    public func createB(): String {
        let id = "b_${store.size}"
        store.put(id, BImpl())
        return id
    }

    public func callBFoo(id: String): Unit {
        store[id]?.foo()
    }
}
```

改写上例（方式 3：手写互操作库）：

`A` 和 `B` 都不再用 `@Interop[ArkTS]`，而是实现 `SharedObject & JSInteropType<T>`，手工注册类、方法跳板和类型互转函数。每个业务方法需要一个配套的 `xxx_ArkTS_Interop_Identifier` 静态跳板，用来从 `JSCallInfo` 取出 `this`、还原仓颉对象、调用真实方法、再把返回值 `toJSValue` 回去。

```cj
public class A <: SharedObject & JSInteropType<A> {
    static init() {
        JSModule.registerClass("A") { context =>
            let clazz = context.clazz(jsConstructor)
            clazz.addMethod("foo", context.function(foo_ArkTS_Interop_Identifier))
            return clazz
        }
    }

    public init() {}

    public static func jsConstructor(context: JSContext, callInfo: JSCallInfo): JSValue {
        let clazz = A()
        let thisArg = callInfo.thisArg
        let thisObject = thisArg.asObject(context)
        let jsExternal = context.external(clazz)
        thisObject.attachCJObject(jsExternal)
        return thisObject.toJSValue()
    }

    public func foo(): B {
        return B()
    }

    public static func foo_ArkTS_Interop_Identifier(context: JSContext, callInfo: JSCallInfo): JSValue {
        let thisArg = callInfo.thisArg
        let thisObject = thisArg.asObject(context)
        let jsExternal = thisObject.getAttachInfo() ?? throw Exception("class: get external failed.")
        let clazz = jsExternal.cast<A>() ?? throw Exception("class: get clazz failed.")
        let RET = clazz.foo()
        RET.toJSValue(context)
    }

    public func toJSValue(context: JSContext): JSValue {
        let ext = context.external(this)
        let obj = context.object()
        obj["foo"] = context.function(foo_ArkTS_Interop_Identifier).toJSValue()
        obj.attachCJObject(ext)
        obj.toJSValue()
    }

    public static func fromJSValue(context: JSContext, input: JSValue) {
        let jsObj = input.asObject(context)
        let jsExt = jsObj.getAttachInfo() ?? throw Exception("class: get external failed.")
        let obj = jsExt.cast<A>() ?? throw Exception("class: get clazz failed.")
        return obj
    }

    public static func toArkTsType(): String {
        "class"
    }
}
```

`B` 用同样的骨架实现（`JSModule.registerClass("B")` + `jsConstructor` + `toJSValue` / `fromJSValue` / `toArkTsType`），这样 `A.foo(): B` 的返回值可以通过 `RET.toJSValue(context)` 正常过桥。

**骨架对应关系（照着每一处改名即可）：**

| 位置 | 按类名替换的内容 |
|------|------------------|
| `class <Name> <: SharedObject & JSInteropType<<Name>>` | 类名 |
| `JSModule.registerClass("<Name>")` | JS 侧暴露的类名，与 ArkTS 调用名一致 |
| 每个 `public func <method>(...)` | 另加一个 `<method>_ArkTS_Interop_Identifier` 静态跳板，并在 `registerClass` 里 `addMethod("<method>", context.function(...))` 注册 |
| `toJSValue` 里 `obj["<method>"] = context.function(...)` | 逐个方法登记 |
| `fromJSValue` / `jsConstructor` | 结构固定，只改 `cast<<Name>>()` 里的类型名 |

**何时选手写互操作库**：当多个仓颉类之间存在对象级返回或参数传递，并且业务希望保留类之间的真实引用关系、不想拆成句柄或扁平参数时，使用此方式。代价是模板代码较多、需严格按结构填写，增删方法要同时改四处（业务方法本体、`_ArkTS_Interop_Identifier` 跳板、`registerClass` 的 `addMethod`、`toJSValue` 里的 `obj[...]`）。

**判断清单**：动笔写 `@Interop[ArkTS]` 前，检查该类的 `public` 成员签名里（参数、返回值、字段类型）是否出现其他 `@Interop[ArkTS]` 标注的类型，如有，按上述三种方式之一重构后再加注解；若选择方式 3，则整类都不再用 `@Interop[ArkTS]` 宏，改为手写 `SharedObject & JSInteropType<T>` 实现。

## 回调桥接模式

由于 `open` 不可用，不能让 ArkTS 继承仓颉类再 override 方法。需要用以下替代模式：

### 模式 A：函数参数回调（推荐）

把回调函数作为 `@Interop[ArkTS]` 方法的参数传入。仓颉侧在内部持有这些函数引用，业务事件触发时调用对应函数。

```cj
@Interop[ArkTS]
public class <Feature>Client {
    private var onSuccessFn: ?((String) -> Unit) = None
    private var onFailFn: ?((String) -> Unit) = None

    public func setOnSuccess(fn: (String) -> Unit): Unit {
        onSuccessFn = Some(fn)
    }

    public func setOnFail(fn: (String) -> Unit): Unit {
        onFailFn = Some(fn)
    }

    public func doAction(input: String): Unit {
        // 业务逻辑...
        if (input.isNotEmpty) {
            onSuccessFn?.let({ it("ok") })
        } else {
            onFailFn?.let({ it("empty") })
        }
    }
}
```

ArkTS 侧用法：

```ts
import { requireCJLib } from 'libark_interop_loader.so'
import { <Feature>Client as CJClient, CustomLib } from 'lib<module>.so'

const lib = requireCJLib('lib<module>.so') as CustomLib
const client = new lib.<Feature>Client()
client.setOnSuccess((msg: string) => { console.info(msg) })
client.setOnFail((msg: string) => { console.error(msg) })
client.doAction('hello')
```

### 模式 B：注册式回调

提供单独的 `@Interop[ArkTS]` 函数来注册/注销回调，内部用仓颉 `HashMap` 或列表持有回调引用。适用于多实例或多监听器场景。

```cj
@Interop[ArkTS]
public class <Feature>Client {
    private let handlers: HashMap<String, (String) -> Unit> = HashMap<String, (String) -> Unit>()

    public func registerHandler(name: String, fn: (String) -> Unit): Unit {
        handlers.put(name, fn)
    }

    public func unregisterHandler(name: String): Unit {
        handlers.remove(name)
    }

    public func emit(name: String, payload: String): Unit {
        handlers[name]?.let({ it(payload) })
    }
}
```

选择原则：单监听器用模式 A，多监听器或需要动态增删用模式 B。

### spawn / 后台线程调用 ArkTS 回调（强制规则：business 不改，桥接层补 postJSTask）

如果业务代码中存在在 `spawn { ... }` 内触发“仓颉 → ArkTS”的互操作调用，例如：

```cj
spawn {
    downloadProgressListener.onSetUbtData("c_download_restore_start", map)
}
```

并且满足以下任一条件：

1. `onSetUbtData` 属于被 `@Interop[ArkTS]` 标注的 `class` / `interface` 的方法，或
2. `onSetUbtData` 的实现内部存在“仓颉调用 ArkTS”的互操作（例如回调 ArkTS listener、构造 `JSHashMapEx` / `JSArrayEx` 并传给 ArkTS 等）

则必须遵守：

- **business 代码不能改**（尤其是 `spawn { ... }` 逻辑不动）。
- 只能在生成/桥接的互操作代码里补线程切换：把实际的 ArkTS 互操作调用通过主线程 JSContext 的 `postJSTask { ... }` 投递回主 JS 线程执行。

示例（在生成的互操作桥接层方法实现中改）：

```cj
public func onSetUbtData(ubtType: String, downData: HashMap<String, String>): Unit {
    mainThreadContext.getOrThrow().postJSTask {
        JSCurrentJSContext.set(mainThreadContext)
        let jsMap = JSHashMapEx<String, String>()
        for ((key, value) in downData) {
            jsMap[key] = value
        }
        arktsListener.onSetUbtData(ubtType, jsMap)
        JSCurrentJSContext.unset()
    }
}
```

注意：

- `mainThreadContext` 必须是主线程 `JSContext`（通常在初始化阶段保存）；不要在后台线程里直接构造/操作 `JSHashMapEx` / `JSArrayEx`。
- `JSCurrentJSContext.set(...)` / `unset()` 必须包裹构造与调用（见上文「JSHashMapEx / JSArrayEx 与 JSCurrentJSContext」）。

## ArkTS 构造签名限制

ArkTS 有两条严格规则限制构造签名的写法：

- `arkts-no-type-query`：禁止在类型位置使用 `typeof`，不能用 `typeof CJXxx` 描述构造签名。
- `arkts-no-ctor-signatures-iface`：禁止在 `.ets` 源文件的 `interface` 中写构造签名 `new (...)`。

**正确做法**：`CustomLib` 必须定义在 `.d.ts` 声明文件中（如 `types/lib<module>/Index.d.ts`），使用 `{ new (...): Xxx }` 内联构造签名。`.ets` 源文件只导入使用，不定义构造签名。

## Context 处理

如果仓颉侧参数或业务依赖涉及 `kit.AbilityKit.Context` 或 `ohos.ability.Context`，不要直接把它当普通互操作类型暴露给 ArkTS。改用单独的上下文桥接文件保存从 ArkTS 侧注入的 `UIAbilityContext`，再让业务代码通过该全局入口读取。

`GlobalContext.cj` 固定内容：

```cj
package <package.name>.bridge

import <package.name>.*
import ohos.ability.*
import ohos.ability.interop.*
import ohos.ark_interop.*

var ctx:?UIAbilityContext = None
func setContext(runtime: JSContext, callInfo: JSCallInfo): JSValue {
    ctx = createAbilityContextFromJSValue(runtime, callInfo[0])
    runtime.string("hello").toJSValue()
}

let EXPORT_MODULE_CONTEXT = JSModule.registerModule {
    runtime, exports =>
        exports["setContext"] = runtime.function(setContext).toJSValue()
}
```

使用规则：

- **位置与复用**：把 `GlobalContext.cj` 放在对应模块的 `src/main/cangjie/bridge/` 下，与其他桥接文件同目录；已有同用途文件则复用，不重复创建。
- **仓颉侧取值**：直接使用 `ctx` 变量，通过 `ctx.getOrThrow()` 获取 `UIAbilityContext`，不要在多个文件重复定义上下文桥。
- **全局导出收口**：若需要导出全局变量或 `public static` 成员，也统一收口到 `GlobalVar.cj` 中（不存在则新建，存在则复用），不要分散到其他 bridge 文件。
- **声明侧变更**：`.d.ts` 中增加 `import { common } from "@kit.AbilityKit"`，`CustomLib` 中增加 `setContext(ctx: common.UIAbilityContext): void;`；已有声明则增量补，不重写。
- **ArkTS 侧约束**：先调用 `setContext` 注入上下文，再执行业务逻辑；业务方法签名中不暴露 Context 参数。

### 全局变量 / `public static` 变量导出

如果业务代码中存在需要给 ArkTS 读取的全局变量，或 `public class` 下的 `public static let/var` 成员，统一放到 `GlobalVar.cj` 中用 `JSModule.registerModule` 导出（文件不存在则新建）。

#### 简单类型：直接导出值

适用简单类型：`String`、整数、浮点、布尔等。

例如业务代码：

```cj
public class FileDownloader {
    public static let DOWNLOADING: String = "DOWNLOADING"
    public static let STOP: String = "STOP"
    public static let CANCEL: String = "CANCEL"
}
```

生成方式：

```cj
let EXPORT_MODULE_CONTEXT = JSModule.registerModule {
    runtime, exports =>
        exports["STATE_DOWNLOADING"] = runtime.string("DOWNLOADING").toJSValue()
        exports["STATE_STOP"] = runtime.string("STOP").toJSValue()
        exports["STATE_CANCEL"] = runtime.string("CANCEL").toJSValue()
}
```

规则：

- 简单类型直接转 `JSValue` 后挂到 `exports[...]`
- 统一放在 `GlobalVar.cj`（不存在则新建）
- 导出名允许按语义调整，但必须在声明和 ArkTS 使用处保持一致

#### 复杂类型：用 accessor 暴露 getter

适用于自定义类型或必须调用 `toJSValue(...)` 才能转换的对象。

例如业务代码：

```cj
public class C {
    func toJSValue(context: JSContext) {
        context.string("a").toJSValue()
    }
}

public var globalVar: C = C()
```

生成方式：

```cj
let EXPORT_GLOBAL_VAR = JSModule.registerModule {
    runtime, exports =>
        let getterGlobalVar = runtime.function {
            context, callInfo =>
                globalVar.toJSValue(runtime)
        }
        exports.defineOwnAccessor("globalVar", getter: getterGlobalVar)
}
```

规则：

- 复杂对象不要直接写入 `exports[...]`
- 为对象生成 getter，并用 `defineOwnAccessor(...)` 暴露
- getter 内调用真实对象的 `toJSValue(runtime)` 或等价转换逻辑
- 仍统一放在 `GlobalVar.cj`（不存在则新建）

ArkTS 侧调用示例：

```typescript
import { requireCJLib } from 'libark_interop_loader.so'
import { <Feature>Bridge, CustomLib } from 'lib<module>.so'

const cjLib = requireCJLib('lib<module>.so') as CustomLib

// 先注入上下文
cjLib.setContext(this.context)

// 后续业务调用无需再传 context，仓颉侧内部通过 ctx.getOrThrow() 取值
const bridge = new cjLib.<Feature>Bridge()
bridge.doSomething("param")
```
