### static func after(Duration, ()->Option\<Duration>)

```cangjie
public static func after(delay: Duration, task: () -> Option<Duration>): Timer
```

功能：初始化一个 [Timer](sync_package_classes.md#class-timer)，关联的 Task 被调度执行的次数取决于它的返回值。如果定时器第一次触发的时间点小于当前时间，关联的 Task 会立刻被调度执行。如果关联 Task 的返回值为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont).None，该 [Timer](sync_package_classes.md#class-timer) 将会失效，并停止调度关联 Task。如果关联 Task 的返回值为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont).Some(v) 且 `v` 大于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero)，下次运行前的最小时间间隔将被设置为 v。否则，关联 Task 会立刻再次被调度执行。

参数：

- delay: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 从现在开始到关联 Task 首次被调度执行的时间间隔
- task: () ->[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)> - 该 [Timer](sync_package_classes.md#class-timer) 调度执行的 Task

返回值：

- [Timer](sync_package_classes.md#class-timer) - 一个 [Timer](sync_package_classes.md#class-timer) 实例

### static func once(Duration, ()->Unit)

```cangjie
public static func once(delay: Duration, task: ()->Unit): Timer
```

功能：设置并启动一次性定时任务，返回控制这个任务的 [Timer](sync_package_classes.md#class-timer) 对象实例。

参数：

- delay: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 从现在开始到 Task 被执行的时间间隔。取值范围 [[Duration.Min](../../core/core_package_api/core_package_structs.md#static-const-min), [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)]，小于或等于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero) 时 Task 将立即被执行。
- task: ()->Unit - 待定时执行的任务。

返回值：

- [Timer](sync_package_classes.md#class-timer) - 生成的对象实例。

示例：

<!-- run -->

```cangjie
import std.time.MonoTime
import std.sync.Timer

main() {
    let start = MonoTime.now()
    Timer.once(Duration.second, {=>
        println("Tick at: ${MonoTime.now() - start}")
    })

    sleep(Duration.second * 2)
    0
}
```

可能的运行结果：

```text
Tick at: 1s2ms74us551ns
```