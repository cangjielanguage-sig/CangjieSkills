## func renameat(Int32, String, Int32, String) <sup>(deprecated)</sup>

```cangjie
public func renameat(oldfd: Int32, oldName: String, newfd: Int32, newName: String): Int32
```

功能：重命名文件，如果需要将会移动文件所在目录。

[renameat](posix_package_funcs.md#func-renameatint32-string-int32-string-deprecated)() 与 [rename](posix_package_funcs.md#func-renamestring-string-deprecated)() 处理相同，此处仅描述两者差异点：

- `oldName` 为相对路径且 `oldfd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `oldName` 为相对路径且 `oldfd` 非 `AT_FDCWD` 时，则路径将相对于 `oldfd` 引用的文件所属目录。
- `oldName` 为绝对路径时 `oldfd` 参数将被忽略。
- `newName` 的场景与 `oldName` 相同，只是当 `newName` 为相对路径时是相对于 `newfd` 引用的文件所属目录。

> **注意：**
>
> 未来版本即将废弃。

参数：

- oldfd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- oldName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件名。
- newfd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- newName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件名。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `oldName` 或 `newName` 包含空字符时，抛出异常。

## func setgid(UInt32) <sup>(deprecated)</sup>

```cangjie
public func setgid(id: UInt32): Int32
```

功能：设置调用进程的有效组 `ID`，需要适当的权限。

> **注意：**
>
> 未来版本即将废弃。

参数：

- id: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 调用进程的有效组 `ID` 号。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 设置成功，返回 `0`，设置失败, 返回 `-1`。

## func sethostname(String) <sup>(deprecated)</sup>

```cangjie
public func sethostname(buf: String): Int32
```

功能：设置主机名，仅超级用户可以调用。

> **注意：**
>
> 未来版本即将废弃。

参数：

- buf: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 需要设置的主机名。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 设置成功，返回 `0`，设置失败, 返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果参数 `buf` 包含空字符则抛出异常。

## func setpgid(Int32, Int32) <sup>(deprecated)</sup>

```cangjie
public func setpgid(pid: Int32, pgrp: Int32): Int32
```

功能：此函数将参数 `pid` 指定的组 `ID` 设置为参数 `pgrp` 指定的组 `ID`。 如果 `pid` 为 `0`，则使用当前进程的组 `ID`。

> **注意：**
>
> 未来版本即将废弃。

参数：

- pid: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 进程 `ID`。
- pgrp: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 进程组 `ID`。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行成功，返回组 `ID`，执行失败, 返回 `-1`。

## func setpgrp() <sup>(deprecated)</sup>

```cangjie
public func setpgrp(): Int32
```

功能：将当前进程所属的组 `ID` 设置为当前进程的进程 `ID`，此函数等同于调用 [setpgid](posix_package_funcs.md#func-setpgidint32-int32-deprecated)(0, 0)。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 执行成功，返回当前进程的组 `ID`，执行失败, 返回 `-1`。