### prop startTime

```cangjie
public prop startTime: DateTime
```

功能：获取进程启动时间，获取失败时返回 [DateTime.UnixEpoch](../../time/time_package_api/time_package_structs.md#static-prop-unixepoch)。

类型：[DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime)

### prop systemTime

```cangjie
public prop systemTime: Duration
```

功能：获取进程启动时间，获取失败时返回 -1ms。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### prop userTime

```cangjie
public prop userTime: Duration
```

功能：获取进程启动时间，获取失败时返回 -1ms。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### prop workingDirectory <sup>(deprecated)</sup>

```cangjie
public prop workingDirectory: Path
```

功能：获取进程工作路径。对于 `Windows` 平台，仅对当前进程生效，其他场景下无法在非特权 `API` 下获取到本属性。

> **注意：**
>
> 未来版本即将废弃，使用 [getHomeDirectory()](../../env/env_package_api/env_package_funcs.md#func-gethomedirectory) 替代。

类型：[Path](../../fs/fs_package_api/fs_package_structs.md#struct-path)

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在或对应进程为僵尸进程，或在 `Windows` 平台的不支持的场景下无法获取进程工作路径时，抛出异常。

### static func of(Int64) <sup>(deprecated)</sup>

```cangjie
public static func of(pid: Int64): Process
```

功能：根据输入进程 `id` 绑定一个进程实例。

> **注意：**
>
> 未来版本即将废弃，使用 [findProcess](./process_package_funcs.md#func-findprocessint64) 替代。

参数：

- pid: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 进程 `id`。

返回值：

- [Process](process_package_classes.md#class-process) - 返回进程 `id` 对应的进程实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当输入进程 `id` 大于 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 最大值或小于 `0`时，抛出异常。
- [ProcessException](process_package_exceptions.md#class-processexception) - 当内存分配失败或 `pid` 对应的进程不存在时，抛出异常。