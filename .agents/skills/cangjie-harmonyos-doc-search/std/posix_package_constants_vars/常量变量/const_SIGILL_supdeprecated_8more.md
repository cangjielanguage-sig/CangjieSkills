## const SIGILL <sup>(deprecated)</sup>

```cangjie
public const SIGILL: Int32 = 0x4
```

功能：硬件指令无效，默认动作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGINT <sup>(deprecated)</sup>

```cangjie
public const SIGINT: Int32 =  0x2
```

功能：终端中断字符，默认动作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGIO <sup>(deprecated)</sup>

```cangjie
public const SIGIO: Int32
```

功能：异步 `IO`，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x17
- 其他情况：0x1D

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGIOT <sup>(deprecated)</sup>

```cangjie
public const SIGIOT: Int32 = 0x6
```

功能：硬件故障，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGKILL <sup>(deprecated)</sup>

```cangjie
public const SIGKILL: Int32 = 0x9
```

功能：终止，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGPIPE <sup>(deprecated)</sup>

```cangjie
public const SIGPIPE: Int32 = 0xD
```

功能：写入未读进程的管道，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGPROF <sup>(deprecated)</sup>

```cangjie
public const SIGPROF: Int32 = 0x1B
```

功能：摘要超时，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGPWR <sup>(deprecated)</sup>

```cangjie
public const SIGPWR: Int32 = 0x1E
```

功能：电源故障或重启，系统调用无效，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)