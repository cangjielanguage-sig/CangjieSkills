## const S_IFIFO <sup>(deprecated)</sup>

```cangjie
public const S_IFIFO: UInt32 = 0x1000
```

功能：文件类型为 `FIFO` 文件，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IFLNK <sup>(deprecated)</sup>

```cangjie
public const S_IFLNK: UInt32 = 0xA000
```

功能：文件类型为软连接，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IFREG <sup>(deprecated)</sup>

```cangjie
public const S_IFREG: UInt32 = 0x8000
```

功能：文件类型为一般文件，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IFSOCK <sup>(deprecated)</sup>

```cangjie
public const S_IFSOCK: UInt32 = 0xC000
```

功能：文件类型为套接字文件，适用函数 [isType](posix_package_funcs.md#func-istypestring-uint32-deprecated)， 所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IRGRP <sup>(deprecated)</sup>

```cangjie
public const S_IRGRP: UInt32 = 0x20
```

功能：表示文件用户组具有读权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IROTH <sup>(deprecated)</sup>

```cangjie
public const S_IROTH: UInt32 = 0x4
```

功能：表示其他用户对文件具有读权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IRUSR <sup>(deprecated)</sup>

```cangjie
public const S_IRUSR: UInt32 = 0x100
```

功能：表示文件所有者具有读权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)