#### 案例二：因未处理仓颉标准库抛出的异常导致的 Crash 问题

本节以 `NoneValueException` 异常为例，通过一个简单的案例展示分析仓颉 `Crash` 问题的过程。

案例源代码如下：

```cangjie
import std.collection.*

func foo() {
    let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
    println(map["d"])
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
    Reason:std.core:NoneValueException
    Uncaught exception was found.
    Exception info: Value does not exist!

    Stacktrace:
        at _CNac10ArrayDequeIG_E4growHl.exception_outlined_func.10(std/collection/array_deque.cj:160)
        at std.collection.HashMap<...>::[](T0)(std/collection/hash_map.cj:835)
        at ohos_app_cangjie_entry.foo()(entry\src\main\cangjie/index.cj:22)
        at ohos_app_cangjie_entry.EntryView::build::lambda.0::lambda.0::lambda.0::lambda.0::lambda.0::lambda.0()(entry\src\main\cangjie/index.cj:35)
        at _CCN22ohos_app_cangjie_entry9EntryView5buildHvEL_L_L_L_L_L_E_29$i(:0)
        at _CCN14ohos.component13ComponentBaseIG_E7onClickHF0uRNY_10ClickEventEEEL_E_6$i(:0)
        at _CCN14ohos.component16InteractableView7onClickHF0uRNY_10ClickEventEEEL_E_6$i(:0)
        at ohos.component.CallbackCJClickEvent::invoke(Int32, CPointer<...>, CPointer<...>)(cj_lambda_invoker_impl.cj:50)
        at ohos.ffi.ohosFFICJCallbackInvoker(Int64, Int32, CPointer<...>, CPointer<...>)(ffi_callback.cj:172)
    ```

    根据 `Crash` 原因和异常信息可知，程序崩溃的直接原因是存在未捕获的 `NoneValueException` 异常。

2. 根据 `Crash` 日志中的堆栈定位到具体源代码。

    从上至下查看异常代码调用栈，前两帧为 `std` 模块即标准库抛出异常的现场，`std` 模块的上一帧为具体源代码的位置。

    分析堆栈可以定位到异常抛出位置在源代码的第 22 行 `foo` 函数中，且错误的发生与 `HashMap` 下标语法访问有关。

    具体异常代码如下：

    ```cangjie
    func foo() {
        let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
        println(map["d"])
    }
    ```

3. 分析异常代码，确定问题根因。

    分析异常代码上下文可知，由于 `map` 中不存在 `key` 为 `d` 的键值对导致异常。

    该案例，较为简单，如果代码逻辑复杂，可以借助 `DevEco Studio` 提供的调试工具对程序进行调试。

4. 修改方案。

    根据分析结果，对源代码进行相应修改。可以在查找 `HashMap` 中的键值对前，增加对 `key` 值是否存在的保护性判断。

    修改后 `foo` 函数源代码如下：

    ```cangjie
    func foo() {
        let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
        if (map.contains("d")) {
            println(map["d"])
        }
    }
    ```