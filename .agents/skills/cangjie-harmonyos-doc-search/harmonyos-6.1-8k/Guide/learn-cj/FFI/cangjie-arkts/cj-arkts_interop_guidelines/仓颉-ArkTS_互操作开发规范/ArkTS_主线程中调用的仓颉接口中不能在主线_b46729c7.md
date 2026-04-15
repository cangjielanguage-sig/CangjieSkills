## ArkTS 主线程中调用的仓颉接口中，不能在主线程中阻塞等待 spawn(UIThread) 的执行结果

**【规则】** ArkTS 主线程中调用的仓颉接口中，不能在主线程中阻塞等待 spawn(UIThread) 的执行结果，否则会造成死锁，触发 App Freeze 故障。

ArkTS 主线程中调用的仓颉接口时，仓颉代码中可能会通过 spawn(UIThread) 表达式向主线程抛一个异步任务，该操作通常用于将仓颉接口的执行结果返回给 ArkTS 侧。开发者需要注意，不能在主线程中阻塞等待 spawn(UIThread) 的执行结果，否则会造成死锁，触发 App Freeze 故障（APP_INPUT_BLOCK）。常见的阻塞行为包括但不限于：

- 使用 future.get() 等待 spawn(UIThread) 表达式返回值；
- 使用 Mutex 的 lock() 接口获取会在 spawn(UIThread) 的任务中释放的锁。

**错误示例：**

仓颉侧代码：

<!--compile.error-->
```cangjie
import ohos.ark_interop.*
import ohos.ark_interop_macro.*
import ohos.base.UIThread

@Interop[ArkTS]
public func testCJ(): Unit {
    // ...
    let future = spawn(UIThread) {
        // ...
    }
    future.get() // 错误：spawn(UIThread) 是创建一个仓颉任务到主线程，future.get() 又在主线程等待，会造成死锁
    // ...
}
```

ArkTS 侧代码：

```javascript
import { testCJ } from "libohos_app_cangjie_entry.so"

@Entry
@Component
struct Index {
   // ...
   testCJ() // ArkTS 主线程中调用仓颉接口
   // ...
}
```