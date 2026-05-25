## func setuid(UInt32) <sup>(deprecated)</sup>

```cangjie
public func setuid(id: UInt32): Int32
```

功能：设置调用进程的有效用户 `ID`，需要适当的权限。

> **注意：**
>
> 未来版本即将废弃。

参数：

- id: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 调用进程的有效用户 `ID` 号。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 设置成功，返回 `0`，设置失败, 返回 `-1`。

## func symlink(String, String) <sup>(deprecated)</sup>

```cangjie
public func symlink(path: String, symPath: String): Int32
```

功能：创建一个名为 `symPath` 链接到 `path` 所指定的文件。

- 符号链接在运行时被解释为链接的内容已被替换到要查找文件或目录的路径中。
- 符号链接可能包含..路径组件，这些组件（如果在链接的开头使用）引用链接所在目录的父目录。
- 符号链接（也称为软链接）可以指向现有文件或不存在的文件，后者被称为悬空链接。
- 符号链接的权限是不相关的，在跟踪链接时，所有权将被忽略，但当请求删除或重命名链接并且链接位于设置了粘滞位的目录中时，所有权将被检查。
- 如果 symPath 已存在，则不会被覆盖。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- symPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 链接文件路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 或 `symPath` 包含空字符时，抛出异常。

## func symlinkat(String, Int32, String) <sup>(deprecated)</sup>

```cangjie
public func symlinkat(path: String, fd: Int32, symPath: String): Int32
```

功能：创建一个名为 `symPath` 链接到 `path` 与 `fd` 所指定的文件。

- `symPath` 为相对路径且 `fd` 为特殊值 `AT_FDCWD` 时，则路径将相对于调用进程的当前工作目录。
- `symPath` 为相对路径且 `fd` 非 `AT_FDCWD` 时，则路径将相对于 `fd` 引用的文件所属目录。
- `symPath` 为绝对路径时 `fd` 参数将被忽略。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- symPath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 链接文件路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 成功返回 `0`，错误返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 或 `symPath` 包含空字符时，抛出异常。

## func ttyname(Int32) <sup>(deprecated)</sup>

```cangjie
public func ttyname(fd: Int32): String
```

功能：返回终端名称。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 操作成功时返回路径名，失败时，返回 `NULL`。

## func umask(UInt32) <sup>(deprecated)</sup>

```cangjie
public func umask(cmask: UInt32): UInt32
```

功能：设置权限掩码。

> **注意：**
>
> 未来版本即将废弃。

参数：

- cmask: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 文件权限参数。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 返回文件上一个掩码的值。