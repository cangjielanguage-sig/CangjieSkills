## func link(String, String) <sup>(deprecated)</sup>

```cangjie
public func link(path: String, newpath: String): Int32
```

功能：为存在的文件创建链接，一个文件可以有多个指向其 `i-node` 的目录条目。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- newpath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 其他文件路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 或 `newPath` 包含空字符时，抛出异常。

## func linkat(Int32, String, Int32, String, Int32) <sup>(deprecated)</sup>

```cangjie
public func linkat(fd: Int32, path: String, nfd: Int32, newPath: String, lflag: Int32): Int32
```

功能：创建相对于目录文件描述符的文件链接。

- `path` 为相对路径且 `fd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `path` 为相对路径且 `fd` 非 `AT_FDCWD` 时，则路径将相对于 `fd` 引用的文件所属目录。
- `path` 为绝对路径时 `fd` 参数将被忽略。
- `newPath` 的场景与 `path` 相同，只是当 `newPath` 为相对路径时是相对于 `nfd` 引用的文件所属目录。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- nfd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 其他文件描述符。
- newPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 其他文件路径，如果 `newpath` 存在，则不会覆盖。
- lflag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - [AT_EMPTY_PATH](posix_package_constants_vars.md#const-at_empty_path-deprecated) 或 `AT_SYMLINK_FOLLOW` 或 `0`。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 或 `newPath` 包含空字符时，抛出异常。

## func lseek(Int32, Int64, Int32) <sup>(deprecated)</sup>

```cangjie
public func lseek(fd: Int32, offset: Int64, whence: Int32): Int64
```

功能：当文件进行读或写时，读或写位置相应增加。本函数用于控制文件的读或写位置。调用成功时，返回当前读写位置，即从文件开头开始的字节数。如果发生错误，返回 -1。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 打开文件的文件描述符。
- offset: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 偏移量。
- whence: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 表示控制模式。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 调用成功时，返回当前读写位置，即从文件开头开始的字节数。