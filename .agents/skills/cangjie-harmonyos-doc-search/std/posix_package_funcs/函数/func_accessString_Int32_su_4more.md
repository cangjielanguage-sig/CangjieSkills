## func access(String, Int32) <sup>(deprecated)</sup>

```cangjie
public func access(path: String, mode: Int32): Int32
```

功能：判断某个文件是否具有某种权限，具有返回 `0`，否则返回 `-1`。

`mode` 为指定权限，传入类型 [R_OK](posix_package_constants_vars.md#const-r_ok-deprecated)、`W_OK`、[X_OK](posix_package_constants_vars.md#const-x_ok-deprecated)、[F_OK](posix_package_constants_vars.md#const-f_ok-deprecated)。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- mode: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 待检查的权限。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件具有待检查的权限返回 `0`，否则返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func chdir(String) <sup>(deprecated)</sup>

```cangjie
public func chdir(path: String): Int32
```

功能：通过指定路径的方式，更改调用进程的当前工作目录。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 改变后的路径。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 设置成功，返回 `0`，设置失败, 返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func chmod(String, UInt32) <sup>(deprecated)</sup>

```cangjie
public func chmod(path: String, mode: UInt32): Int32
```

功能：修改文件访问权限。

在 `Windows` 环境下：

- 所有文件和目录都是可读的，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)() 不能更改文件的可读权限；
- 在 `Windows` 环境下，文件的可执行权限通过文件扩展名设置，所有目录都是可执行的，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)() 不能更改文件和目录的可执行权限。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- mode: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 要修改的权限。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。当 `mode` 为非法参数时，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated) 会忽略该参数，返回 `0`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func chown(String, UInt32, UInt32) <sup>(deprecated)</sup>

```cangjie
public func chown(path: String, owner: UInt32, group: UInt32): Int32
```

功能：修改文件所有者和文件所有者所属组。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- owner: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 所有者 `uid`。
- group: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 指定 `gid` 参数。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 操作成功时返回 `0`，失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。