## class CurrentProcess <sup>(deprecated)</sup>

```cangjie
public class CurrentProcess <: Process {}
```

功能：此类为当前进程类，继承 [Process](process_package_classes.md#class-process) 类，提供对当前进程操作相关功能。

提供功能具体如下：

- 提供获取当前进程标准流（`stdIn`、`stdOut`、`stdErr`）机制。
- 提供当前进程退出注册回调函数机制。
- 提供当前进程退出机制，允许设置退出状态码。

> **注意：**
>
> 未来版本即将废弃。

父类型：

- [Process](#class-process)

### prop arguments

```cangjie
public prop arguments: Array<String>
```

功能：返回当前进程参数列表，例如当前进程命令行为 `a.out ab cd ef`，其中 `a.out` 是程序名，则返回的列表包含三个元素 ab cd ef。

> **说明：**
>
> - 使用 C 语言调用仓颉动态库方式时，通过 int SetCJCommandLineArgs(int argc, const char* argv[]) 设置的命令行参数，在使用当前进程的 `arguments` 获取时，将会被舍弃掉第一个参数。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>

### prop homeDirectory

```cangjie
public prop homeDirectory: Path
```

功能：获取 `home` 目录的路径。

类型：[Path](../../fs/fs_package_api/fs_package_structs.md#struct-path)

### prop stdErr

```cangjie
public prop stdErr: OutputStream
```

功能：获取当前进程标准错误流。

类型：[OutputStream](../../io/io_package_api/io_package_interfaces.md#interface-outputstream)

### prop stdIn

```cangjie
public prop stdIn: InputStream
```

功能：获取当前进程标准输入流。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### prop stdOut

```cangjie
public prop stdOut: OutputStream
```

功能：获取当前进程标准输出流。

类型：[OutputStream](../../io/io_package_api/io_package_interfaces.md#interface-outputstream)

### prop tempDirectory

```cangjie
public prop tempDirectory: Path
```

功能：获取临时目录的路径。从环境变量中获取 `TMPDIR`、`TMP`、`TEMP` 和 `TEMPDIR` 环境变量。如果以上值在环境变量中均不存在，则默认返回 `/tmp` 目录。

类型：[Path](../../fs/fs_package_api/fs_package_structs.md#struct-path)

### func atExit(() -> Unit)

```cangjie
public func atExit(callback: () -> Unit): Unit
```

功能：注册回调函数，当前进程退出时执行注册函数。

> **注意：**
>
> 请不要使用 C 语言 atexit 函数，避免出现非预期问题。

参数：

- callback: () ->[Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 需要被注册回调的函数。

### func exit(Int64)

```cangjie
public func exit(code: Int64): Nothing
```

功能：进程退出函数，执行到此函数直接结束当前进程，并且通过入参 `code` 设置返回状态码。

参数：

- code: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 当前进程退出状态码。

### func getEnv(String)

```cangjie
public func getEnv(key: String): Option<String>
```

功能：获取指定名称的环境变量值。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 环境变量名称。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 指定名称对应的环境变量值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数入参包含空字符时，抛出异常。