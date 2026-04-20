### func cancel()

```cangjie
public func cancel(): Unit
```

功能：取消该 [Timer](sync_package_classes.md#class-timer)，关联 Task 将不再被调度执行。

如果调用该函数时关联 Task 正在执行，不会打断当前运行。该函数不会阻塞当前线程。调用该函数多次等同于只调用一次。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取 [Timer](sync_package_classes.md#class-timer) 对象的哈希值。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 对象的哈希值。

### operator func !=(Timer)

```cangjie
public operator func !=(rhs: Timer): Bool
```

功能：判断当前 [Timer](sync_package_classes.md#class-timer) 与入参 `rhs` 指定的 [Timer](sync_package_classes.md#class-timer) 是否不是同一个实例。

参数：

- rhs: [Timer](#class-timer) - 待比较的另一个 [Timer](#class-timer) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若两个 [Timer](sync_package_classes.md#class-timer) 不是同一个实例，则返回 `true`，否则返回 `false`。

### operator func ==(Timer)

```cangjie
public operator func ==(rhs: Timer): Bool
```

功能：判断当前 [Timer](sync_package_classes.md#class-timer) 与入参 `rhs` 指定的 [Timer](sync_package_classes.md#class-timer) 是否是同一个实例。

参数：

- rhs: [Timer](#class-timer) - 待比较的另一个 [Timer](#class-timer) 对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若两个 [Timer](sync_package_classes.md#class-timer) 是同一个实例，则返回 `true`，否则返回 `false`。