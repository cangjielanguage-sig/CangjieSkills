## class Timer

```cangjie
public class Timer <: Equatable<Timer> & Hashable {}
```

功能：提供定时器功能。

用于在指定时间点或指定时间间隔后，执行指定任务一次或多次。

> **注意：**
>
> - [Timer](sync_package_classes.md#class-timer) 隐式包含了 `spawn` 操作，即，每个 [Timer](sync_package_classes.md#class-timer) 会创建一个线程用于执行该 [Timer](sync_package_classes.md#class-timer) 关联的 Task。
> - 每个 [Timer](sync_package_classes.md#class-timer) 只能在初始化时绑定一个 Task，初始化完成后，无法重置关联的 Task。
> - 只有关联 Task 执行完毕，或 使用 `cancel` 接口主动取消 [Timer](sync_package_classes.md#class-timer)，[Timer](sync_package_classes.md#class-timer) 的生命周期才会结束，之后才能被 [GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 回收。换句话说，在 [Timer](sync_package_classes.md#class-timer) 关联的 Task 执行完毕或 [Timer](sync_package_classes.md#class-timer) 被主动取消前，[Timer](sync_package_classes.md#class-timer) 实例均不会被 [GC](../../runtime/runtime_package_api/runtime_package_funcs.md#func-gcbool) 回收，从而确保关联 Task 可以被正常执行。
> - 系统繁忙时，Task 的触发时间可能会被影响。[Timer](sync_package_classes.md#class-timer) 不保证 Task 的触发时间一定准时。[Timer](sync_package_classes.md#class-timer) 保证 Task 的触发时间小于等于当前时间。
> - [Timer](sync_package_classes.md#class-timer) 不会主动捕获关联 Task 抛出的异常。只要 Task 有未被捕获的异常，[Timer](sync_package_classes.md#class-timer) 就会失效。
> - [Timer](sync_package_classes.md#class-timer) 通常按使用方式分为 一次性任务定时器 和 重复性任务定时器两种，一次性任务定时器 Task 只会执行一次，重复性任务定时器 Task 会按指定周期执行, 直到使用 `cancel` 接口主动取消 或者 达到 [Timer](sync_package_classes.md#class-timer) 创建时指定的结束条件。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[Timer](#class-timer)>
- [Hashable](../../core/core_package_api/core_package_interfaces.md#interface-hashable)