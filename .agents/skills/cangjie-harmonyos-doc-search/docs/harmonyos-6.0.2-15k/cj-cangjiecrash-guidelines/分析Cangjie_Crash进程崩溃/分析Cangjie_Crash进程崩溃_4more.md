# 分析Cangjie Crash（进程崩溃）

当未捕获的仓颉异常导致应用意外退出时，应用会在抛出未捕获异常时崩溃并且生成对应的仓颉 `Crash` 崩溃日志文件。开发者可通过错误日志确认引起崩溃的代码位置并分析应用崩溃的原因。

## 仓颉 Crash 日志规格

以下是 `Crash` 日志中各字段含义。

```text
Device info:XXXXXX                        // 设备信息
Build info:XXX-XXXX X.X.X.XX(XXXXXXXX)    // 版本信息
Module name:com.example.myapplication     // 模块名
Version:1.0.0                             // 版本号
Pid:45570                                 // 进程号
Uid:0                                     // 用户ID
Reason:std.core:Exception                 // Crash 原因
Uncaught exception was found.
Exception info: throwing foo exception    // 异常信息
Stacktrace:                               // 异常代码调用栈
    at ohos_app_cangjie_entry.foo()(entry\src\main\cangjie/index.cj:20)
```

## 仓颉 Crash 异常捕获场景

在仓颉中，异常类有 `Error` 和 `Exception`：

- `Error` 类描述仓颉语言运行时，系统内部错误和资源耗尽错误，应用程序不应该抛出这种类型错误。如果出现内部错误，只能通知给用户，尽量安全终止程序。

- `Exception` 类描述的是程序运行时的逻辑错误或者 IO 错误导致的异常，例如数组越界或者试图打开一个不存在的文件等，这类异常需要在程序中捕获处理。常见的异常信息详见[常见运行时异常](https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-common_runtime_exceptions)。

## 问题定位思路

### 获取日志

进程崩溃日志是一种故障日志，与应用无响应日志、应用崩溃等都由 `FaultLogger` 模块管理，可通过以下方式获取：

1. 通过 `DevEco Studio` 获取日志

    `DevEco Studio` 会收集设备 `/data/log/faultlog/faultlogger/` 路径下的进程崩溃故障日志并归档在 `FaultLog` 下，仓颉进程崩溃日志归档在 `FaultLog` 下的 `cjerror` 类型中，获取日志的方法请参见 [FaultLog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log)。

2. 通过 `hiAppEvent` 接口订阅

    `hiAppEvent` 提供了故障订阅接口，可以订阅各类故障打点，详见 [`HiAppEvent` 介绍](./cj-hiappevent-intro.md)。

### 根因分析

仓颉 `Crash` 问题分析可以通过故障日志中的异常信息、异常代码调用栈来定位到源代码，得出基本的分析结论。

对于 `Error` 类异常，调用栈参考意义有限，根因定位较为复杂，需要结合代码逻辑、内存开销、参数配置等方面，借助 `DevEco Studio` 中提供的分析工具进行分析。

对于 `Exception` 类异常，大多数情况为代码逻辑异常导致，可以根据调用栈直接定位到异常代码，检视代码逻辑即可。