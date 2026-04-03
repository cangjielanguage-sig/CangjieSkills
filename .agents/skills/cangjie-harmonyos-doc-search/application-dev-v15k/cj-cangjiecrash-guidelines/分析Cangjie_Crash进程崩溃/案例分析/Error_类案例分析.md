### Error 类案例分析

`Error` 类问题一般是仓颉语言运行时感知到系统内部错误或资源耗尽错误时抛出的异常。

开发者常见的此类异常有两种：

1. `OutOfMemoryError`：内存不足时由运行时抛出。

2. `StackOverflowError`：仓颉线程栈溢出时由运行时抛出。

#### 案例一：内存不足异常

案例源代码如下：

```cangjie
var bigArray = Array<Rune>(1024 * 1024 * 60, repeat: r'a')

func foo(): Unit {
    var smallArray = Array<Rune>(1024 * 1024 * 5, repeat: r'a')
}

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello Cangjie"
    func build() {
        Row {
            Column {
                Button(message).onClick {
                    evt =>
                    AppLog.info("Hello Cangjie")
                    foo()
                }.fontSize(40).height(80)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

1. 获取 `Crash` 日志，根据日志信息中的 `Crash` 原因和异常信息确认程序崩溃的直接原因。

    `Crash` 日志核心内容如下：

    ```text
    Reason:std.core:OutOfMemoryError
    Uncaught exception was found.
    Exception info: [none]
    Stacktrace:
        at ohos_app_cangjie_entry.foo()(entry\src\main\cangjie/index.cj:24)
        at ohos_app_cangjie_entry.EntryView::build::lambda.0::lambda.0::lambda.0::lambda.0::lambda.0::lambda.0()(entry\src\main\cangjie/index.cj:38)
        at _CCN22ohos_app_cangjie_entry9EntryView5buildHvEL_L_L_L_L_L_E_29$i(:0)
        at _CCN14ohos.component13ComponentBaseIG_E7onClickHF0uRNY_10ClickEventEEEL_E_6$i(:0)
        at _CCN14ohos.component16InteractableView7onClickHF0uRNY_10ClickEventEEEL_E_6$i(:0)
        at ohos.component.CallbackCJClickEvent::invoke(Int32, CPointer<...>, CPointer<...>)(cj_lambda_invoker_impl.cj:50)
        at ohos.ffi.ohosFFICJCallbackInvoker(Int64, Int32, CPointer<...>, CPointer<...>)(ffi_callback.cj:172)
    ```

    根据 `Crash` 原因和异常信息可知，程序崩溃的直接原因是内存不足异常。

2. 分析问题根因。

    对于 `OutOfMemoryError` 异常，调用栈参考意义有限，因为内存不足时，任何地方都可能导致 `OutOfMemoryError`，异常抛出点可能只是恰好用完了所剩无几的可用内存。

    要分析 `OutOfMemoryError` 异常发生的根本原因，可以从以下几个方面综合分析：

    - 内存开销。可以借助 `DevEco Studio` 提供的 `Profiler` 工具对内存开销进行分析。

    - 代码逻辑。可以结合调用栈、堆栈开销等，检视业务代码，确认代码逻辑的正确性。如果代码逻辑无错误，再结合堆栈开销考虑是否可以优化代码。

    - 参数配置。确认 `cjHeapSize` 大小配置是否符合当前业务场景。