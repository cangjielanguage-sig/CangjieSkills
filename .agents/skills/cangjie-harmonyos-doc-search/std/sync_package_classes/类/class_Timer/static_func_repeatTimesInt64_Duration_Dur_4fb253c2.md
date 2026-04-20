### static func repeatTimes(Int64, Duration, Duration, ()->Unit, CatchupStyle)

```cangjie
public static func repeatTimes(count: Int64, delay: Duration, interval: Duration, task: () -> Unit, style!: CatchupStyle = Burst): Timer
```

功能：设置并启动重复性定时任务，指定 Task 最大执行次数，返回控制这个任务的 [Timer](sync_package_classes.md#class-timer) 对象实例。

参数：

- count: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - Task 最大执行次数。取值范围 (0, [Int64](../../core/core_package_api/core_package_intrinsics.md#int64).Max]。
- delay: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 从现在开始到 Task 被执行的时间间隔。取值范围 [Duration.Min, [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)]，小于或等于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero) 时 Task 将立即被执行。
- interval: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 两次 Task 之间的时间间隔。取值范围 ([Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero), [Duration.Max](../../core/core_package_api/core_package_structs.md#static-const-max)]。
- task: ()->Unit - 待定时执行的任务。
- style!: [CatchupStyle](./sync_package_enums.md#enum-catchupstyle) - 追平策略，默认 Burst。当 Task 执行时间过长时，后续任务执行时间点可能发生延迟，不同的追平策略适用于不同的场景，详见 [CatchupStyle](sync_package_enums.md#enum-catchupstyle) 说明。

返回值：

- [Timer](sync_package_classes.md#class-timer) - 生成的对象实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) <= 0 或 interval 小于等于 [Duration.Zero](../../core/core_package_api/core_package_structs.md#static-const-zero) 时，抛出异常。

示例：

<!-- run -->

```cangjie
import std.sync.Timer
import std.time.MonoTime

main() {
    let start = MonoTime.now()
    Timer.repeatTimes(3, Duration.second, Duration.second, {=>
        println("Tick at: ${MonoTime.now() - start}")
    })

    sleep(Duration.second * 4)
    0
}
```

可能的运行结果：

```text
Tick at: 1s2ms855us251ns
Tick at: 2s5ms390us18ns
Tick at: 3s7ms935us552ns
```