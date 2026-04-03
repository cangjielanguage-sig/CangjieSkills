## func close(Int32) <sup>(deprecated)</sup>

```cangjie
public func close(fd: Int32): Int32
```

功能：关闭文件，[close](posix_package_funcs.md#func-closeint32-deprecated) 将会触发数据写回磁盘，并释放文件占用的资源。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功时返回 `0`，失败时返回 `-1`。

## func creat(String, UInt32) <sup>(deprecated)</sup>

```cangjie
public func creat(path: String, flag: UInt32): Int32
```

功能：创建文件并为其返回文件描述符，或在失败时返回 `-1`。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- flag: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 创建文件的权限。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回文件描述符，执行失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func dup(Int32) <sup>(deprecated)</sup>

```cangjie
public func dup(fd: Int32): Int32
```

功能：用于复制旧 `fd` 参数指定的文件描述符并返回。此新文件描述符和旧的参数 `fd` 引用同一文件，共享文件各种状态。共享所有的锁定、读写位置和各项权限或标志等。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回最小且未使用的文件描述符，执行失败时返回 `-1`。

## func dup2(Int32, Int32) <sup>(deprecated)</sup>

```cangjie
public func dup2(fd: Int32, fd2: Int32): Int32
```

功能：用于复制 `oldfd` 参数指定的文件描述符，并将其返回到 `newfd` 参数。如果参数 `newfd` 是打开的文件描述符，则 `newfd` 指定的文件将首先关闭。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - `oldfd` 参数指定的文件描述符。
- fd2: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - `newfd` 参数指定的文件描述符。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - `fd2` 文件描述符。