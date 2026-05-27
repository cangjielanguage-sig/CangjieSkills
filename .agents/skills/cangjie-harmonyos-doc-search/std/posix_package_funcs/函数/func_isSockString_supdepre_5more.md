## func isSock(String) <sup>(deprecated)</sup>

```cangjie
public func isSock(path: String): Bool
```

功能：检查传入对象是否为套接字文件，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isType(String, UInt32) <sup>(deprecated)</sup>

```cangjie
public func isType(path: String, mode: UInt32): Bool
```

功能：检查文件是否为指定模式的文件。如果是，返回 `ture`，否则返回 `false`。根据模式的不同值确定不同的类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- mode: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 判断参数。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是指定模式的文件，返回 `true`，否则返回 `false`。

## func kill(Int32, Int32) <sup>(deprecated)</sup>

```cangjie
public func kill(pid: Int32, sig: Int32): Int32
```

功能：系统调用可用于向任何进程组或进程发送任何信号。

- 如果 `pid` 大于 `0`，则信号 `sig` 将发送到 `pid` 对应的进程。
- 如果 `pid` 等于 `0`，然后 `sig` 被发送到调用进程的进程组中的每个进程。
- 如果 `pid` 等于 `-1`，则 `sig` 被发送到调用进程有权发送信号的每个进程。
- 如果 `pid` 小于 `-1`，则将 `sig` 发送到 `ID` 为 `-pid` 的进程组中的每个进程。

> **注意：**
>
> 未来版本即将废弃。

参数：

- pid: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 进程 `ID`。
- sig: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 信号 `ID`。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，否则返回 `-1`。

## func killpg(Int32, Int32) <sup>(deprecated)</sup>

```cangjie
public func killpg(pgid: Int32, sig: Int32): Int32
```

功能：将信号 `sig` 发送到进程组 `pgrp`，如果 `pgrp` 为 `0`，则 [killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)() 将信号发送到调用进程的进程组。

> **注意：**
>
> 未来版本即将废弃。

参数：

- pgid: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 组 `ID`。
- sig: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 信号 `ID`。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，否则返回 `-1`。

## func lchown(String, UInt32, UInt32) <sup>(deprecated)</sup>

```cangjie
public func lchown(path: String, owner: UInt32, group: UInt32): Int32
```

功能：修改文件链接本身所有者和所有者所属组。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 字符串类型的文件路径。
- owner: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 所有者 `uid`。
- group: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 指定 `gid` 参数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。