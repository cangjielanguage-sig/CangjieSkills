## const SIGXFSZ <sup>(deprecated)</sup>

```cangjie
public const SIGXFSZ: Int32 = 0x19
```

功能：文件长度超过上限，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const W_OK <sup>(deprecated)</sup>

```cangjie
public const W_OK: Int32 = 0x2
```

功能：测试文件写权限，适用函数 [access](posix_package_funcs.md#func-accessstring-int32-deprecated)，[faccessat](posix_package_funcs.md#func-faccessatint32-string-int32-int32-deprecated)，所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const X_OK <sup>(deprecated)</sup>

```cangjie
public const X_OK: Int32 = 0x1
```

功能：测试文件执行权限，适用函数 [access](posix_package_funcs.md#func-accessstring-int32-deprecated)，[faccessat](posix_package_funcs.md#func-faccessatint32-string-int32-int32-deprecated)，所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)