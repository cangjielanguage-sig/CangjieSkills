## 仓颉与 ArkTS 互操作逻辑要求在与 ArkTS 运行时绑定的系统线程上执行

**【规则】** 在仓颉调用 ArkTS 时，所有涉及 ArkTS 数据访问或接口调用的操作，需要运行在 ArkTS 运行时绑定的系统线程上。否则将触发 JSThreadMisMatch 异常。

仓颉线程是用户态线程，运行时会将仓颉线程调度到系统线程上执行，因此仓颉程序默认不会绑定在特定系统线程执行；而仓颉与 ArkTS 互操作逻辑要求运行在与 ArkTS 运行时绑定的系统线程上，因此开发者进行互操作时，需要关注互操作发生的线程，如果在非 ArkTS 线程，开发者需要使用互操作库提供的接口切换到 ArkTS 线程执行。开发者可以使用以下接口来保证互操作逻辑的正确执行：

- 使用 JSContext.isInBindThread() 判断当前线程是否可以执行互操作接口；
- 如需切换线程执行，可使用：
    - JSContext.postJSTask { ... } 创建在 ArkTS 线程执行的任务；
    - 如果 ArkTS 被部署在主线程上，开发者可以使用 spawn(UIThread) 语法使互操作逻辑所在线程被调度到主线程执行、

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
        // 实际仓颉函数行为
        let value = a + b
        // 创建result
        let result = context.number(value).toJSValue() // 错误：没有运行在ArkTS运行时绑定的系统线程上
        // 调用js回调
        callback.call(result)
    }

    // 返回 void
    return context.undefined().toJSValue()
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports => exports["addNumberAsync"] = runtime.function(addNumberAsync).toJSValue()
}
```

**正确示例（isInBindThread & postJSTask 使用示例）：**

仓颉代码：

<!--compile-->
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
        // 实际仓颉函数行为
        let value = a + b
        if (context.isInBindThread()) { // 正确：如果当前线程为 ArkTS 运行时绑定的系统线程，可以直接同步调用
            // 创建result
            let result = context.number(value).toJSValue()
            // 调用js回调
            callback.call(result)
        } else {                        // 正确：否则使用 postJSTask 发起异步回调至 ArkTS 线程上执行
            context.postJSTask {
                // 创建result
                let result = context.number(value).toJSValue()
                // 调用js回调
                callback.call(result)
            }
        }
    }

    // 返回 void
    return context.undefined().toJSValue()
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports => exports["addNumberAsync"] = runtime.function(addNumberAsync).toJSValue()
}
```

**正确示例（spawn(UIThread) 使用示例）：**

仓颉代码：

<!--compile-->
```cangjie
import ohos.ark_interop.*
import ohos.base.UIThread

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
        // 实际仓颉函数行为
        let value = a + b
        spawn(UIThread) { // 正确：调度到 ArkTS 主线程上执行
            // 创建result
            let result = context.number(value).toJSValue()
            // 调用js回调
            callback.call(result)
        }
    }

    // 返回 void
    return context.undefined().toJSValue()
}