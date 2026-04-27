# 互操作库与 JSRuntime

## 适用场景

宏覆盖不了时的底层方案，以及仓颉主动调用 ArkTS 系统模块：
- 完全动态的 JSValue 处理、反射式对象操作
- 宏类型系统覆盖不到的边界
- 精细控制 exports 表
- **仓颉调用 ArkTS** 系统模块

## 手工导出（优先用 @Interop 宏替代）

```cangjie
import ohos.ark_interop.*

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

**thisArg**：从对象取出方法再调用时必须补 thisArg，否则 `this` 丢失：

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let object = callInfo[0].asObject()
    // ✅ 直接 callMethod 自动绑 this
    object.callMethod("doSth")
    // ✅ 取出后手动补 thisArg
    let f = object["doSth"].asFunction()
    f.call(thisArg: object.toJSValue())
}
```

**JSExternal**：需要手搓对象表面时使用，参考文档 `JSExternal.md`。

## JSRuntime 单例（关键）

> ⚠️ 每次 `JSRuntime()` 新建会导致旧 JSContext/JSValue/回调被 GC 后崩溃。**必须**单例持有。
>
> ⚠️ **禁止在 `spawn` 线程中创建 `JSRuntime()`**——只能在主线程上创建。仓颉线程与系统线程不是 1:1 绑定，spawn 线程中创建会触发未定义行为或崩溃。

```cangjie
import ohos.ark_interop.*

public class ArkTSBridge {
    private static var instance: Option<ArkTSBridge> = Option<ArkTSBridge>.None
    private let jsRuntime: JSRuntime
    public let jsContext: JSContext
    private var cachedModule: Option<JSValue> = Option<JSValue>.None

    private init() {
        jsRuntime = JSRuntime()
        jsContext = jsRuntime.mainContext
    }

    public static func getInstance(): ArkTSBridge {
        match (instance) {
            case Some(v) => v
            case None =>
                let mgr = ArkTSBridge()
                instance = Some(mgr)
                mgr
        }
    }

    // 缓存系统模块，避免重复加载
    public func getModule(name: String): JSValue {
        match (cachedModule) {
            case Some(m) => m
            case None =>
                let module = jsContext.requireSystemNativeModule(name)
                cachedModule = Some(module)
                module
        }
    }
}
```

## 模块加载与名称映射

### requireSystemNativeModule（加载 NAPI 系统模块）

`@ohos.X.Y` → `ctx.requireSystemNativeModule("X.Y")`，去掉 `@ohos.` 前缀。

`@hms.X.Y` → `ctx.requireSystemNativeModule("X.Y", prefix: "hms")`，去掉 `@hms.` 前缀并加 `prefix` 参数。

已验证：`"net.http"`、`"file.fs"`、`"file.photoAccessHelper"`。

### requireArkModule（更通用的模块加载 API）

`requireArkModule` 支持更多场景，推荐在新代码中使用：

```cangjie
func loadModule(context: JSContext): Unit {
    // 系统模块：@ohos.*, @hms.*, @system.*, @kit.*
    let hilog = context.requireArkModule("@ohos.hilog").asObject()
    hilog.callMethod("info", [
        context.number(0).toJSValue(),
        context.string("test").toJSValue(),
        context.string("load success").toJSValue()
    ])

    // hap 模块里的文件（需 build-profile.json5 配置 runtimeOnly.sources）
    let test = context.requireArkModule("entry/src/main/ets/Test").asObject()
    test.callMethod("test")

    // native 模块
    let native = context.requireArkModule("libentry.so").asObject()
}
```

| 场景 | src 格式 | 说明 |
|------|---------|------|
| 系统模块 | `@ohos.*`、`@hms.*`、`@system.*`、`@kit.*` | 直接传完整名称 |
| hap 文件 | `"模块名/模块下路径"` | 需 `runtimeOnly.sources` 配置；不带后缀 |
| har 文件 | `"模块名/模块下路径"` | 需 `runtimeOnly.packages` 配置 |
| hsp 文件 | `"模块名/模块下路径"` | 支持远程/ohpm hsp |
| native 模块 | `"lib模块名.so"` | 支持 hap/har/本地 hsp 中的 napi/仓颉模块 |

> **限制**：只能在 ArkTS 绑定线程使用；禁止在全局变量初始化和模块导出流程中使用；部分系统模块（如 `ohos.router`）只在主运行时提供。

## JSObject 属性提取（必须类型检查）

```cangjie
// ✅ 先 hasProperty + 类型检查，再转换
let parsed = jsonUtil.callMethod("parse", args.toArray())
if (!parsed.isObject()) {
    return  // 解析失败，安全退出
}
let rootObj = parsed.asObject()

if (rootObj.hasProperty("id") && rootObj["id"].isNumber()) {
    record.id = Int64(rootObj["id"].toNumber())
}
if (rootObj.hasProperty("name") && rootObj["name"].isString()) {
    record.name = rootObj["name"].toString()
}
if (rootObj.hasProperty("items") && rootObj["items"].isArray()) {
    let arr = rootObj["items"].asArray()
    // 遍历数组...
}

// ❌ 不检查直接转换 — 字段不存在或类型不符时崩溃
let name = rootObj["name"].toString()
let count = rootObj["count"].toNumber()
```

## 基本调用

```cangjie
let b = Bridge.get()
let fs = b.ctx.requireSystemNativeModule("file.fs").asObject()
let content = fs.callMethod("readTextSync", [pathValue])

// JS 回调创建
let cb = b.ctx.function({ ctx, info =>
    let data = info[0]
    // 处理 data...
    ctx.undefined().toJSValue()
})
```

## 多线程与线程切换

ArkTS 是单线程执行的，互操作逻辑必须在 **ArkTS 运行时绑定的系统线程** 上执行，否则触发 `JSThreadMisMatch` 异常。

### 判断与切换 API

```cangjie
// 判断当前线程是否可执行互操作
if (context.isInBindThread()) {
    // 直接同步调用
    let result = context.number(value).toJSValue()
    callback.call(result)
} else {
    // 切换到 ArkTS 线程执行
    context.postJSTask {
        let result = context.number(value).toJSValue()
        callback.call(result)
    }
}
```

如果 ArkTS 部署在主线程，也可用 `spawn(UIThread) { ... }` 切换。

### 死锁警告

> ⚠️ 主线程中调用的仓颉接口里，**禁止** `future.get()` 等待 `spawn(UIThread)` 的结果，否则死锁（App Freeze / APP_INPUT_BLOCK）。同理禁止用 Mutex lock 等待会在 `spawn(UIThread)` 中释放的锁。

### 手工 Promise（promiseCapability）

宏的 `@Interop[ArkTS, Async]` 无法满足时，可用底层 Promise 模式：

```cangjie
func addNumberAsync(context: JSContext, callInfo: JSCallInfo): JSValue {
    let a = callInfo[0].toNumber()
    let b = callInfo[1].toNumber()
    let promise = context.promiseCapability()
    spawn {
        let result = a + b
        context.postJSTask {
            promise.resolve(context.number(result).toJSValue())
        }
    }
    promise.toJSValue()
}
```

## 跨语言异常处理

互操作中被调用侧抛出的异常会自动转换为调用侧可捕获的异常，必须 try-catch 处理：

```cangjie
// 仓颉侧捕获 ArkTS 异常 —— 必须用 JSCodeError，不要用 BusinessException/Exception
func callArktsWithExp(context: JSContext, callInfo: JSCallInfo): JSValue {
    try {
        callInfo[0].asFunction().call()
    } catch (err: JSCodeError) {
        // ArkTS 侧 throw 的 Error 对象会被自动转换为 JSCodeError
    }
    context.undefined().toJSValue()
}
```

ArkTS 侧同理用 `try { ... } catch (err) { ... }` 捕获仓颉侧抛出的异常。

### 异常类型选择速查

| 场景 | 仓颉侧 catch 的类型 |
|------|-------------------|
| ArkTS 函数 throw 的 Error | `JSCodeError`（**首选**） |
| 调用 NAPI 系统模块（如 `file.fs`、`net.http`）失败 | 仍是 `JSCodeError`，其 message 中携带业务码 |
| 仓颉自身（非互操作）异常 | 普通 `Exception` 子类 |

> ❌ `BusinessException` 是 ArkTS 侧 `@ohos.base` 的类型，仓颉侧无对应 catch 类。在仓颉里用它捕获 ArkTS 系统模块异常是无效的——这些异常进入仓颉时已转为 `JSCodeError`。
>
> ✅ 推荐写法：`catch (err: JSCodeError) { /* 互操作异常 */ } catch (err: Exception) { /* 仓颉自身异常兜底 */ }`

## 跨语言对象引用与内存泄漏

避免跨语言对象形成环形引用（ArkTS 对象 → 仓颉对象 → ArkTS 回调 → 同一 ArkTS 对象），各自的 GC 无法识别跨运行时的环形依赖，会导致内存泄漏。使用完毕后及时将回调引用置空断环。

## 排障清单

1. **JSRuntime 必须单例 + 主线程创建** → 禁 spawn 中 JSRuntime()
2. **JSObject 先检查再转换** → hasProperty + isNumber/isString
3. **thisArg** 补全：方法从对象取出后 call 要带 thisArg
4. **多线程** → isInBindThread() 判断 + postJSTask 切换；主线程禁 future.get() spawn(UIThread)
5. **异常处理** → 仓颉侧捕获 ArkTS 异常**只用 `JSCodeError`**，不要用 BusinessException
6. **Async 宏自动切线程** → @Interop[ArkTS, Async] 函数体不要手写 spawn/postJSTask；isInBindThread+postJSTask 仅用于手写 registerFunc 的回调场景
7. **JSValue 生命周期** → 引用类型注意持有；避免跨语言环形引用
8. **属性写入静默失败**：密封/只读属性不报错

## 参考资料

- 互操作库：`cj-arkts_interoperability_lib/cj-arkts_interoperability_lib.md`
- 互操作概述：`cangjie_arkts_overview/cangjie_arkts_overview.md`
