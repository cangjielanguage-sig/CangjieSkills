## const AT_EMPTY_PATH <sup>(deprecated)</sup>

```cangjie
public const AT_EMPTY_PATH: Int32 = 0x1000
```

功能：表示在文件系统中空路径（即没有指定任何文件或目录）时返回的文件描述符，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const AT_FDCWD <sup>(deprecated)</sup>

```cangjie
public const AT_FDCWD: Int32
```

功能：表示在文件系统中相对路径操作的特殊文件描述符常量，用于在使用 `*at()` 系列系统调用时指定相对路径的解析起点。主要用于 `fchmodat`、 `fchownat`、`linkat`、`renameat`、`symlinkat`、`unlinkat` 等函数，所属函数参数 `fd`。不同系统下的值分别为：

- macOS: -0x2
- 其他情况：-0x64

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const AT_REMOVEDIR <sup>(deprecated)</sup>

```cangjie
public const AT_REMOVEDIR: Int32 = 0x200
```

功能：如果指定了 [AT_REMOVEDIR](posix_package_constants_vars.md#const-at_removedir-deprecated) 标志，则对 `pathname` 执行等效于 `rmdir(2)` 的操作，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const AT_SYMLINK_FOLLOW <sup>(deprecated)</sup>

```cangjie
public const AT_SYMLINK_FOLLOW: Int32
```

功能：表示一个用于控制符号链接解析行为的标志，指定在操作符号链接时是否跟随链接指向的目标文件。通常与 `AT_FDCWD` 结合使用。若无该标志，大多数系统调用会直接操作符号链接本身（如读取链接路径）。使用该标志后，系统调用会先解析符号链接，然后操作其指向的目标文件。主要用于 `linkat`、`unlinkat` 等函数，所属函数参数 `fd`。不同系统下的值分别为：

- macOS: 0x040
- 其他情况：0x400

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const F_OK <sup>(deprecated)</sup>

```cangjie
public const F_OK: Int32 = 0x0
```

功能：测试文件是否存在，适用函数 [access](posix_package_funcs.md#func-accessstring-int32-deprecated)，[faccessat](posix_package_funcs.md#func-faccessatint32-string-int32-int32-deprecated)，所属函数参数 `mode`。

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_APPEND <sup>(deprecated)</sup>

```cangjie
public const O_APPEND: Int32
```

功能：读取或写入文件时，数据将从文件末尾移动。即写入的数据将附加到文件的末尾，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x00000008
- Windows: 0x8
- 其他情况：0x400

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

## const O_CLOEXEC <sup>(deprecated)</sup>

```cangjie
public const O_CLOEXEC: Int32
```

功能：在某些多线程程序中，使用此标志是必不可少的。因为在一个线程同时打开文件描述符，而另一个线程执行 `fork(2)` 加 `execve(2)` 场景下使用单独的 `fcntl(2)` `F_SETFD` 操作设置 `FD_CLOEXEC` 标志并不足以避免竞争条件，适用函数 `open`、`open64`、`openat`、`openat64`，所属函数参数 `oflag`。不同系统下的值分别为：

- macOS: 0x01000000
- 其他情况：0x80000

> **注意：**
>
> 未来版本即将废弃。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)