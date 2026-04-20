## func getcwd() <sup>(deprecated)</sup>

```cangjie
public func getcwd(): String
```

功能：获取当前执行进程工作目录的绝对路径。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 操作成功，返回包含路径信息的字符串，操作失败则返回空字符串。

## func getgid() <sup>(deprecated)</sup>

```cangjie
public func getgid(): UInt32
```

功能：获取用户组 `ID`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 当前用户组 `ID`。

## func getgroups(Int32, CPointer\<UInt32>) <sup>(deprecated)</sup>

```cangjie
public unsafe func getgroups(size: Int32, gidArray: CPointer<UInt32>): Int32
```

功能：获取当前用户所属组的代码。

如果 `gidArray` 参数大小的值为零，则函数仅返回表示用户所属的组数，不会向 `gidArray` 中放入 `gid`。

> **注意：**
>
> 未来版本即将废弃。

参数：

- size: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - `gidArray` 可以容纳的 `gid` 的数量。
- gidArray: [CPointer](../../core/core_package_api/core_package_intrinsics.md#cpointert)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)> - 存放 `gid` 信息。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行成功，返回组代码，执行失败, 返回 `-1`。

## func gethostname() <sup>(deprecated)</sup>

```cangjie
public func gethostname(): String
```

功能：获取主机名称，此名称通常是 `TCP`/`IP` 网络上主机的名称。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 获取到的主机的名称字符串, 获取失败则返回空字符串。

## func getlogin() <sup>(deprecated)</sup>

```cangjie
public func getlogin(): String
```

功能：获取当前登录名。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 操作成功时返回登录名，失败时返回空字串。

## func getos() <sup>(deprecated)</sup>

```cangjie
public func getos(): String
```

功能：从 `/proc/version` 文件中获取 `Linux` 系统的信息。例如: `Linux version 4.15.0-142-generic (buildd@lgw01-amd64-036) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #146-Ubuntu SMP Tue Apr 13 01:11:19 UTC 2021`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 获取到的 Linux 系统的信息字符串。

## func getpgid(Int32) <sup>(deprecated)</sup>

```cangjie
public func getpgid(pid: Int32): Int32
```

功能：获取 `pid` 指定的进程的 `PGID`，如果 `pid` 为零，返回调用进程的进程 `ID`。

> **注意：**
>
> 未来版本即将废弃。

参数：

- pid: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 目标进程 `ID`。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行成功，返回进程组 `ID`，执行失败, 返回 `-1`。

## func getpgrp() <sup>(deprecated)</sup>

```cangjie
public func getpgrp(): Int32
```

功能：获取调用进程的父进程 `ID`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回调用进程的父进程 `ID`。

## func getpid() <sup>(deprecated)</sup>

```cangjie
public func getpid(): Int32
```

功能：获取调用进程的进程 `ID(PID)`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回调用进程的进程 `ID(PID)`。