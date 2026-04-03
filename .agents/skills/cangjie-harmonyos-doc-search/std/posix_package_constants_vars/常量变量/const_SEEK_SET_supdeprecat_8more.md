## const SEEK_SET <sup>(deprecated)</sup>

```cangjie
public const SEEK_SET: Int32 = 0x0
```

功能：偏移参数表示新的读写位置，适用函数 [lseek](posix_package_funcs.md#func-lseekint32-int64-int32-deprecated)，所属函数参数 `whence`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGABRT <sup>(deprecated)</sup>

```cangjie
public const SIGABRT: Int32 = 0x6
```

功能：异常终止，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGALRM <sup>(deprecated)</sup>

```cangjie
public const SIGALRM: Int32 = 0xE
```

功能：计时器到期，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGBUS <sup>(deprecated)</sup>

```cangjie
public const SIGBUS: Int32
```

功能：硬件故障，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0xA
- 其他情况：0x7

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGCHLD <sup>(deprecated)</sup>

```cangjie
public const SIGCHLD: Int32
```

功能：子进程状态更改，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x14
- 其他情况：0x11

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGCONT <sup>(deprecated)</sup>

```cangjie
public const SIGCONT: Int32
```

功能：暂停过程的继续，默认操作继续或忽略，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x13
- 其他情况：0x12

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGFPE <sup>(deprecated)</sup>

```cangjie
public const SIGFPE: Int32 = 0x8
```

功能：算术错误，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGHUP <sup>(deprecated)</sup>

```cangjie
public const SIGHUP: Int32 = 0x1
```

功能：连接已断开，默认操作已终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)