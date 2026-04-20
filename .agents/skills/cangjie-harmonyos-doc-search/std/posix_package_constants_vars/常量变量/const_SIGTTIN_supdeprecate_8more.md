## const SIGTTIN <sup>(deprecated)</sup>

```cangjie
public const SIGTTIN: Int32 = 0x15
```

功能：后台读取控件 `tty`，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGTTOU <sup>(deprecated)</sup>

```cangjie
public const SIGTTOU: Int32 = 0x16
```

功能：后台写控制 `tty`，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGURG <sup>(deprecated)</sup>

```cangjie
public const SIGURG: Int32
```

功能：紧急情况（套接字），忽略默认操作，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x10
- 其他情况：0x17

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGUSR1 <sup>(deprecated)</sup>

```cangjie
public const SIGUSR1: Int32
```

功能：用户定义的信号，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x1E
- 其他情况：0xA

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGUSR2 <sup>(deprecated)</sup>

```cangjie
public const SIGUSR2: Int32
```

功能：用户定义的信号，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。不同系统下的值分别为：

- macOS: 0x1F
- 其他情况：0xC

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGVTALRM <sup>(deprecated)</sup>

```cangjie
public const SIGVTALRM: Int32 = 0x1A
```

功能：虚拟时间警报，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGWINCH <sup>(deprecated)</sup>

```cangjie
public const SIGWINCH: Int32 = 0x1C
```

功能：终端窗口大小更改，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const SIGXCPU <sup>(deprecated)</sup>

```cangjie
public const SIGXCPU: Int32 = 0x18
```

功能：`CPU` 占用率超过上限，默认操作终止，适用函数 [kill](posix_package_funcs.md#func-killint32-int32-deprecated)，[killpg](posix_package_funcs.md#func-killpgint32-int32-deprecated)，所属函数参数 `sig`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)