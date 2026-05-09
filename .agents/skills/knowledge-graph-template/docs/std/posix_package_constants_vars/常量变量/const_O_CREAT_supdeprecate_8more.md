## const O_CREAT <sup>(deprecated)</sup>

```cangjie
public const O_CREAT: Int32
```

功能：如果要打开的文件不存在，则自动创建该文件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000200
- Windows: 0x100
- 其他情况：0x40

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_DIRECTORY <sup>(deprecated)</sup>

```cangjie
public const O_DIRECTORY: Int32
```

功能：如果 `pathname` 指定的文件不是目录，则打开文件失败，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00100000
- 其他情况：0x80000

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_DSYNC <sup>(deprecated)</sup>

```cangjie
public const O_DSYNC: Int32
```

功能：每次写入都会等待物理 `I/O` 完成，但如果写操作不影响读取刚写入的数据，则不等待文件属性更新，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x400000
- 其他情况：0x1000

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_EXCL <sup>(deprecated)</sup>

```cangjie
public const O_EXCL: Int32
```

功能：如同时设置 [O_CREAT](posix_package_constants_vars.md#const-o_creat-deprecated)，则此指令检查文件是否存在。如果文件不存在，则创建文件。否则，打开文件出错。此外，如果同时设置了 [O_CREAT](posix_package_constants_vars.md#const-o_creat-deprecated) 和 [O_EXCL](posix_package_constants_vars.md#const-o_excl-deprecated)，并且要打开的文件是符号链接，则打开文件失败，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000800
- Windows: 0x400
- 其他情况：0x80

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_NOCTTY <sup>(deprecated)</sup>

```cangjie
public const O_NOCTTY: Int32
```

功能：如要打开的文件是终端设备，则该文件不会成为这个进程的控制终端，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00020000
- 其他情况：0x100

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_NOFOLLOW <sup>(deprecated)</sup>

```cangjie
public const O_NOFOLLOW: Int32
```

功能：如 `pathname` 指定的文件是单符号连接，则打开文件失败，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000100
- 其他情况：0x20000

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_NONBLOCK <sup>(deprecated)</sup>

```cangjie
public const O_NONBLOCK: Int32
```

功能：以非阻塞的方式打开文件，即 `I/O` 操作不会导致调用进程等待，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000004
- 其他情况：0x800

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_RDONLY <sup>(deprecated)</sup>

```cangjie
public const O_RDONLY: Int32 = 0x0
```

功能：以只读方式打开文件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)