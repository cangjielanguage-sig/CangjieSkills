## const S_IWUSR <sup>(deprecated)</sup>

```cangjie
public const S_IWUSR: UInt32 = 0x80
```

功能：表示文件所有者具有写权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IXGRP <sup>(deprecated)</sup>

```cangjie
public const S_IXGRP: UInt32 = 0x8
```

功能：表示文件用户组具有执行权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IXOTH <sup>(deprecated)</sup>

```cangjie
public const S_IXOTH: UInt32 = 0x1
```

功能：表示其他用户对文件具有执行权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const S_IXUSR <sup>(deprecated)</sup>

```cangjie
public const S_IXUSR: UInt32 = 0x40
```

功能：表示文件所有者具有执行权限，适用函数 open，open64，openat，openat64，[chmod](posix_package_funcs.md#func-chmodstring-uint32-deprecated)(mode)，[fchmod](posix_package_funcs.md#func-fchmodint32-uint32-deprecated)(mode)，[fchmodat](posix_package_funcs.md#func-fchmodatint32-string-uint32-int32-deprecated)(mode)，[creat](posix_package_funcs.md#func-creatstring-uint32-deprecated)， 所属函数参数 `flag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

## const SEEK_CUR <sup>(deprecated)</sup>

```cangjie
public const SEEK_CUR: Int32 = 0x1
```

功能：向当前读或写位置添加偏移量，适用函数 [lseek](posix_package_funcs.md#func-lseekint32-int64-int32-deprecated)，所属函数参数 `whence`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SEEK_END <sup>(deprecated)</sup>

```cangjie
public const SEEK_END: Int32 = 0x2
```

功能：将读写位置设置为文件末尾，并添加偏移量，适用函数 [lseek](posix_package_funcs.md#func-lseekint32-int64-int32-deprecated)，所属函数参数 `whence`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)