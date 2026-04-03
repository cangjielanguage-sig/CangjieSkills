## func fchmodat(Int32, String, UInt32, Int32) <sup>(deprecated)</sup>

```cangjie
public func fchmodat(fd: Int32, path: String, mode: UInt32, flag: Int32): Int32
```

功能：修改文件描述符对应的文件访问权限。

- `path` 为相对路径且 `fd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `path` 为相对路径且 `fd` 非 `AT_FDCWD` 时，则路径将相对于 `fd` 引用的文件所属目录。
- `path` 为绝对路径时 `fd` 参数将被忽略。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- mode: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 要修改的权限。
- flag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 取值可为 `0`，或 `(256)` 如果路径名是符号链接，不会取消引用它，而是返回有关链接本身的信息。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func fchown(Int32, UInt32, UInt32) <sup>(deprecated)</sup>

```cangjie
public func fchown(fd: Int32, owner: UInt32, group: UInt32): Int32
```

功能：修改 `fd` 对应的文件所有者和文件所有者所属组。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- owner: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 所有者 `uid`。
- group: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 指定 `gid` 参数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

## func fchownat(Int32, String, UInt32, UInt32, Int32) <sup>(deprecated)</sup>

```cangjie
public func fchownat(fd: Int32, path: String, owner: UInt32, group: UInt32, flag: Int32): Int32
```

功能：修改文件描述符对应的文件所有者和文件所有者所属组。

- `path` 为相对路径且 `fd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `path` 为相对路径且 `fd` 非 `AT_FDCWD` 时，则路径将相对于 `fd` 引用的文件所属目录。
- `path` 为绝对路径时 `fd` 参数将被忽略。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- owner: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 所有者 `uid`。
- group: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 指定 `gid` 参数。
- flag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 取值可为 `0`，或 `(256)` 如果路径名是符号链接，不会取消引用它，而是返回有关链接本身的信息。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。