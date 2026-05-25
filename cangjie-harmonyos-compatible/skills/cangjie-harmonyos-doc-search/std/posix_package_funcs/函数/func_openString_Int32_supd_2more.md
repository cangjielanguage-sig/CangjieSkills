## func \`open`(String, Int32) <sup>(deprecated)</sup>

```cangjie
public func `open`(path: String, oflag: Int32): Int32
```

功能：打开文件并为其返回新的文件描述符，或在失败时返回 `-1`。

当文件打开方式参数 `oflag` 设置为 [O_CREAT](posix_package_constants_vars.md#const-o_creat-deprecated) 时，可以通过参数设置文件权限。

[O_RDONLY](posix_package_constants_vars.md#const-o_rdonly-deprecated)、[O_RDWR](posix_package_constants_vars.md#const-o_rdwr-deprecated)、[O_WRONLY](posix_package_constants_vars.md#const-o_wronly-deprecated) 作为 `oflag` 取值为互斥关系，但可以与其他操作标识一起使用，如 [O_APPEND](posix_package_constants_vars.md#const-o_append-deprecated) 。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- oflag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件打开的方式。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回新的文件描述符，执行失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。

## func \`open`(String, Int32, UInt32) <sup>(deprecated)</sup>

```cangjie
public func `open`(path: String, oflag: Int32, flag: UInt32): Int32
```

功能：打开文件并为其返回新的文件描述符，或在失败时返回 `-1`。path 代表文件路径，oflag 代表文件打开的方式，其中 [O_RDONLY](posix_package_constants_vars.md#const-o_rdonly-deprecated)、[O_RDWR](posix_package_constants_vars.md#const-o_rdwr-deprecated)、[O_WRONLY](posix_package_constants_vars.md#const-o_wronly-deprecated) 作为 oflag 取值为互斥关系，但可以与其他操作标识一起使用，如 [O_APPEND](posix_package_constants_vars.md#const-o_append-deprecated) 操作。

当文件打开方式参数 `oflag` 设置为 [O_CREAT](posix_package_constants_vars.md#const-o_creat-deprecated) 时，可以通过参数设置文件权限。

[O_RDONLY](posix_package_constants_vars.md#const-o_rdonly-deprecated)、[O_RDWR](posix_package_constants_vars.md#const-o_rdwr-deprecated)、[O_WRONLY](posix_package_constants_vars.md#const-o_wronly-deprecated) 作为 `oflag` 取值为互斥关系，但可以与其他操作标识一起使用，如 [O_APPEND](posix_package_constants_vars.md#const-o_append-deprecated) 。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。
- oflag: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件打开的方式。
- flag: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 如果 `oflag` 设置了 [O_CREAT](posix_package_constants_vars.md#const-o_creat-deprecated) 并且需要创建新文件，则 `flag` 参数标识对新文件的权限，否则 `flag` 不改变文件权限。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回新的文件描述符，执行失败时返回 `-1`。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `path` 包含空字符时，抛出异常。