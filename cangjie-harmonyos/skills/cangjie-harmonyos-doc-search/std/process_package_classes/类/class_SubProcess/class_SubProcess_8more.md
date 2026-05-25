## class SubProcess

```cangjie
public class SubProcess <: Process {}
```

功能：此类为子进程类，继承 [Process](process_package_classes.md#class-process) 类，提供对子进程操作相关功能。

> **说明：**
>
> 提供功能具体如下：
>
> - 提供获取子进程标准流（`stdIn`、`stdOut`、`stdErr`）机制。
> - 提供等待子进程执行返回退出状态码机制，允许设置等待超时时长。
> - 提供等待子进程执行返回输出结果（包含运行正常、异常结果）机制，允许设置等待超时时长。

父类型：

- [Process](#class-process)

### prop stdErr <sup>(deprecated)</sup>

```cangjie
public prop stdErr: InputStream
```

功能：获取输入流，连接到子进程标准错误流。

> **注意：**
>
> 未来版本即将废弃，使用 [stdErrPipe](./process_package_classes.md#prop-stderrpipe) 替代。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### prop stdErrPipe

```cangjie
public prop stdErrPipe: InputStream
```

功能：获取输入流，连接到子进程标准错误流。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### prop stdIn <sup>(deprecated)</sup>

```cangjie
public prop stdIn: OutputStream
```

功能：获取输出流，连接到子进程标准输入流。

> **注意：**
>
> 未来版本即将废弃，使用 [stdInPipe](./process_package_classes.md#prop-stdinpipe) 替代。

类型：[OutputStream](../../io/io_package_api/io_package_interfaces.md#interface-outputstream)

### prop stdInPipe

```cangjie
public prop stdInPipe: OutputStream
```

功能：获取输出流，连接到子进程标准输入流。

类型：[OutputStream](../../io/io_package_api/io_package_interfaces.md#interface-outputstream)

### prop stdOut <sup>(deprecated)</sup>

```cangjie
public prop stdOut: InputStream
```

功能：获取输入流，连接到子进程标准输出流。

> **注意：**
>
> 未来版本即将废弃，使用 [stdOutPipe](./process_package_classes.md#prop-stdoutpipe) 替代。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### prop stdOutPipe

```cangjie
public prop stdOutPipe: InputStream
```

功能：获取输入流，连接到子进程标准输出流。

类型：[InputStream](../../io/io_package_api/io_package_interfaces.md#interface-inputstream)

### func wait(?Duration)

```cangjie
public func wait(timeout!: ?Duration = None): Int64
```

功能：阻塞当前进程等待子进程任务执行完成并返回子进程退出状态码，允许指定等待超时时间。对于需要操作标准流的场景（Pipe 模式），使用者需要优先处理标准流，避免子进程标准流缓冲区满后调用本函数产生死锁。

> **说明：**
>
> 超时时间处理机制：
>
> - 未传参、 `timeout` 值为 `None` 或值小于等于 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).Zero 时，阻塞等待直至子进程执行返回。
> - `timeout` 值大于 [Duration](../../core/core_package_api/core_package_structs.md#struct-duration).Zero 时，阻塞等待子进程执行返回或等待超时后抛出超时异常。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 命名可选参数，设置等待子进程超时时间，默认为 `None`。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回子进程退出状态。若子进程正常退出，返回子进程退出码，若子进程被信号杀死，返回导致子进程终止的信号编号。

异常：

- [TimeoutException](../../core/core_package_api/core_package_exceptions.md#class-timeoutexception) - 当等待超时，子进程未退出时，抛出异常。