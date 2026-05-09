## 仓颉应用中只能在主线程上使用 JSRuntime() 创建 ArkTS 运行时

**【规则】** 仓颉应用中只能在主线程上使用 JSRuntime() 创建 ArkTS 运行时。

线程环境要求 JSRuntime 绑定一个系统线程，所有互操作接口只能在这个系统线程上调用，否则会出现未定义的行为。然而仓颉的线程与系统线程不是 1：1 绑定的关系，导致在仓颉 spawn 出来的仓颉线程里创建的 JSRuntime，在仓颉视角里为同步调用，而在 ArkTS 的视角里会出现线程切换，进而触发未定义行为或崩溃。因此限制只能在系统线程上创建 JSRuntime 而不能在仓颉线程里创建 JSRuntime。

**错误示例：**

仓颉代码：

<!--compile.error-->
```cangjie
import ohos.ark_interop.*

func addNumberAsync(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 从JSCallInfo获取参数列表
    let arg0: JSValue = callInfo[0]
    let arg1: JSValue = callInfo[1]
    let arg2: JSValue = callInfo[2]

    // 把JSValue转换为仓颉类型
    let a: Float64 = arg0.toNumber()
    let b: Float64 = arg1.toNumber()
    let callback = arg2.asFunction()

    // 新建仓颉线程
    spawn {
        let runtime = JSRuntime() // 错误：只能在主线程上使用 JSRuntime() 创建 ArkTS 运行时
        // ...
    }

    // 返回 void
    return context.undefined().toJSValue()
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports => exports["addNumberAsync"] = runtime.function(addNumberAsync).toJSValue()
}
```