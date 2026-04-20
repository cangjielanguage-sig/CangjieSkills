## const SIGQUIT <sup>(deprecated)</sup>

```cangjie
public const SIGQUIT: Int32 = 0x3
```

功能：终端退出字符，默认动作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGSEGV <sup>(deprecated)</sup>

```cangjie
public const SIGSEGV: Int32 = 0xB
```

功能：内存引用无效，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGSTKFLT <sup>(deprecated)</sup>

```cangjie
public const SIGSTKFLT: Int32 = 0x10
```

功能：协处理器堆栈故障，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGSTOP <sup>(deprecated)</sup>

```cangjie
public const SIGSTOP: Int32
```

功能：停止，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x11
- 其他情况：0x13

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGSYS <sup>(deprecated)</sup>

```cangjie
public const SIGSYS: Int32
```

功能：终止，默认操作终止进程并生成核心转储文件（core dump），用于调试分析，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0xC
- 其他情况：0x1F

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGTERM <sup>(deprecated)</sup>

```cangjie
public const SIGTERM: Int32 = 0xF
```

功能：终止，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGTRAP <sup>(deprecated)</sup>

```cangjie
public const SIGTRAP: Int32 = 0x5
```

功能：硬件故障，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGTSTP <sup>(deprecated)</sup>

```cangjie
public const SIGTSTP: Int32
```

功能：终端停止符号，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x12
- 其他情况：0x14

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)