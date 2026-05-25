## func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消该[Timer](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_classes#class-timer)，关联Task将不再被调度执行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

> **说明：**
>
> 如果调用该函数时关联Task正在执行，不会打断当前运行。该函数不会阻塞当前线程。调用该函数多次等同于只调用一次。

## 示例

### 设置一次性定时器任务

> **说明：**
>
> - 设置一个定时器，该定时器在定时器到期后执行一个函数。
> - 该定时器在回调被执行后自动取消，或使用[cancel()](#func-cancel)方法手动取消。

```cangjie
Timer.once(1000*Duration.millisecond, {=>
                        Hilog.info(0, "timer_once", "timer_once")})
```

### 设置重复性定时器任务

> **说明：**
>
> - 重复调用一个函数，在每次调用之间具有固定的时间延迟。
> - 取消该定时器需手动调用[cancel()](#func-cancel)方法。

```cangjie
Timer.repeat(Duration.Zero, 1000 * Duration.millisecond,{=>
                        Hilog.info(0, "timer_repeat", "timer_repeat")})
```

### 取消定时器任务

```cangjie
var timer_1 : Timer = Timer.once(1000 * Duration.millisecond, { => Hilog.info(0, "timer_once", "timer_once")})
var timer_2 : Timer = Timer.repeat(Duration.Zero, 1000 * Duration.millisecond, { => Hilog.info(0, "timer_repeat", "timer_repeat") })
timer_1.cancel()
timer_2.cancel()
```

### 设置定时器任务对组件进行修改

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog
import std.sync.Timer

@Entry
@Component
class EntryView {
    @State
    var time: Int64 = 0
    @State
    var timeSring: String = "Nothing happen"
    var timer_1: Timer = Timer.once(Duration.Zero, {=> Hilog.info(0, "timer_1", "timer_1")})
    var timer_2: Timer = Timer.once(Duration.Zero, {=> Hilog.info(0, "timer_2", "timer_2")})
    func build() {
        Column() {
            Text(this.timeSring)
            Button("Timer setTimeout").onClick(
                {
                etv => this.timer_1 = Timer.once(
                    1000 * Duration.millisecond,
                    {
                        => this.timeSring = "do after 1s delay"
                    }
                )
            })
            Text("Timer value：${this.time} s")
            Button("Timer setInterval").onClick(
                {
                etv => this.timer_2 = Timer.repeat(Duration.Zero, 1000 * Duration.millisecond, {
                    => this.time++
                })
            })
            Button("cancelTimer").onClick(
                {
                    etv =>
                    this.timeSring = "Nothing happen"
                    this.time = 0
                    this.timer_1.cancel()
                    this.timer_2.cancel()
                }
            )
        }
    }
}
```

## 其他说明

### 超时延迟

如果页面正忙于其他任务，超时可能比预期晚。Timer定时器的函数或代码片段在下一个时间周期执行。例如：

```cangjie
func foo(){
    Hilog.info(0, "test", "OH test foo is called")
}
Timer.once(Duration.Zero, {=> foo()})
Hilog.info(0, "test", "After OH test setTimeout")

//output
After OH test setTimeout
OH test foo is called
```

这是因为，虽然Timer设置了0纳秒的延迟，但任务不会立即执行，而是被放入队列中，等待下一次事件循环。当前代码执行完毕后，队列中的函数才会被执行，因此最终的执行顺序可能与预期不一致。

### 最大延时值

定时器的最大延时值为[Duration.Max](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-max)，定时器的最小延时值为[Duration.Min](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-min)，当延时超过[Duration.Max](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-max)或小于[Duration.Min](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-min)时程序将报错：Exception info: Out of range of representation of 'Duration'!