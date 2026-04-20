## func faccessat(Int32, String, Int32, Int32) <sup>(deprecated)</sup>

```cangjie
public func faccessat(fd: Int32, path: String, mode: Int32, flag: Int32): Int32
```

功能：判断 `fd` 对应的文件是否具有某种权限，具有返回 `0`，否则返回 `-1`。

`mode` 为指定权限，传入类型 [R_OK](posix_package_constants_vars.md#const-r_ok-deprecated)、`W_OK`、[X_OK](posix_package_constants_vars.md#const-x_ok-deprecated)、[F_OK](posix_package_constants_vars.md#const-f_ok-deprecated)。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- mode: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待检查的权限。
- flag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 将以下一个或多个值按位或运算获取。`(512)`使用有效的用户和组 `ID` 执行访问检查，默认情况下使用有效 `ID`；`(256)` 如果路径名是符号链接，不会取消引用而是返回有关链接本身信息。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件具有待检查的权限返回 `0`，否则返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func fchdir(Int32) <sup>(deprecated)</sup>

```cangjie
public func fchdir(fd: Int32): Int32
```

功能：通过指定文件路径的描述符，更改调用进程的当前工作目录。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 改变后的文件路径的描述符。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 设置成功，返回 `0`，设置失败, 返回 `-1`。

## func fchmod(Int32, UInt32) <sup>(deprecated)</sup>

```cangjie
public func fchmod(fd: Int32, mode: UInt32): Int32
```

功能：修改文件描述符对应的文件访问权限。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。
- mode: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 要修改的权限。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。