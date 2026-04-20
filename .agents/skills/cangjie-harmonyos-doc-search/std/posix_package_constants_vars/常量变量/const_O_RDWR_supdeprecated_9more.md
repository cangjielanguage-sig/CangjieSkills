## const O_RDWR <sup>(deprecated)</sup>

```cangjie
public const O_RDWR: Int32 = 0x2
```

功能：以读写模式打开文件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_RSYNC <sup>(deprecated)</sup>

```cangjie
public const O_RSYNC: Int32 = 0x101000
```

功能：此标志仅影响读取操作，必须与 [O_SYNC](posix_package_constants_vars.md#const-o_sync-deprecated) 或 [O_DSYNC](posix_package_constants_vars.md#const-o_dsync-deprecated) 结合使用。如果有必要，它将导致读取调用阻塞，直到正在读取的数据（可能还有元数据）刷新到磁盘，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_SYNC <sup>(deprecated)</sup>

```cangjie
public const O_SYNC: Int32
```

功能：同步打开文件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x0080
- 其他情况：0x101000

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_TRUNC <sup>(deprecated)</sup>

```cangjie
public const O_TRUNC: Int32
```

功能：如果文件存在且打开可写，则此标志将文件长度清除为 0，文件中以前存储的数据消失，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000400
- 其他情况：0x200

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_WRONLY <sup>(deprecated)</sup>

```cangjie
public const O_WRONLY: Int32 = 0x1
```

功能：以只写方式打开文件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const R_OK <sup>(deprecated)</sup>

```cangjie
public const R_OK: Int32 = 0x4
```

功能：测试文件读权限，适用函数 [access](posix_package_funcs.md#func-accessstring-int32-deprecated)，[faccessat](posix_package_funcs.md#func-faccessatint32-string-int32-int32-deprecated)，所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const S_IFBLK <sup>(deprecated)</sup>

```cangjie
public const S_IFBLK: UInt32 = 0x6000
```

功能：文件类型为块设备，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IFCHR <sup>(deprecated)</sup>

```cangjie
public const S_IFCHR: UInt32 = 0x2000
```

功能：文件类型为字符设备，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IFDIR <sup>(deprecated)</sup>

```cangjie
public const S_IFDIR: UInt32 = 0x4000
```

功能：文件类型为目录，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)