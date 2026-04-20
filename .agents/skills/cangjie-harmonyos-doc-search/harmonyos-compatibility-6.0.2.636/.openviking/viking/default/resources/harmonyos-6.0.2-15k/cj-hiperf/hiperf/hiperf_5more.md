# hiperf

hiperf为开发人员提供用于调试的命令行工具，用于抓取特定程序或者系统的性能数据，类似内核的perf工具，该工具支持在 Windows/Linux/Mac 等操作系统上运行。

## 环境要求

- 根据hdc命令行工具指导，完成[环境准备](./cj-hdc.md#环境准备)。
- 确保设备已正常连接，并执行hdc shell。

## hiperf命令行说明

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| --debug | 输出debug级别日志。 |
| --hilog | 日志写入hilog。 |
| --logpath | 日志路径。 |
| --logtag | 日志等级。 |
| --mixlog | 混合日志输出。|
| --much | 输出尽可能多的日志。 |
| --nodebug | 无日志输出。 |
| --verbose | 输出verbose级别日志。 |

## 帮助命令

可用 --help 查看帮助。

```shell
hiperf --help
```

**使用样例：**

```bash
$ hiperf --help
Usage: hiperf [options] command [args for command]
options:
        --debug                 show debug log, usage format: --debug [command] [args]
        --help                  show help
        --hilog                 use hilog not file to record log
        --logpath               log file name full path, usage format: --logpath [filepath] [command] [args]
        --logtag                enable log level for HILOG_TAG, usage format: --logtag <tag>[:level][,<tag>[:level]] [command] [args]
                                tag: Dump, Report, Record, Stat... level: D, V, M...
                                example: hiperf --verbose --logtag Record:D [command] [args]
        --mixlog                mix the log in output, usage format: --much [command] [args]
        --much                  show extremely much debug log, usage format: --much [command] [args]
        --nodebug               disable debug log, usage format: --nodebug [command] [args]
        --verbose               show debug log, usage format: --verbose [command] [args]
        -h                      show help
command:
        dump:   Dump content of a perf data file, like perf.data
        help:   Show more help information for hiperf
        list:   List the supported event types.
        record: Collect performance sample information
        report: report sampling information from perf.data format file
        stat:   Collect performance counter information


See 'hiperf help [command]' for more information on a specific command.
```

使用如下命令查看子功能的帮助信息。

```shell
hiperf [command] --help
```

## list命令

可列出设备上支持的所有事件名称，事件名称用于 stat 和 record 的 -e 和 -g 参数。

**list命令参数说明：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| hw | 硬件事件。 |
| sw | 软件事件。 |
| tp | tracepoint事件。 |
| cache | 硬件缓存事件。 |
| raw | 原始pmu事件。 |

```shell
Usage: hiperf list [event type name]
```

使用help命令查询支持的事件类型。

```shell
hiperf list --help
```

**使用样例：**

```bash
$ hiperf list --help
Usage: hiperf list [event type name]
       List all supported event types on this devices.
   To list the events of a specific type, specify the type name
       hw          hardware events
       sw          software events
       tp          tracepoint events
       cache       hardware cache events
       raw         raw pmu events
```

下面列出了设备支持的HW事件，并且会提示哪些事件此设备不支持。

```shell
hiperf list hw
```

**使用样例：**

```bash
$ hiperf list hw
event not support hw-ref-cpu-cycles


Supported events for hardware:
        hw-cpu-cycles
        hw-instructions
        hw-cache-references
        hw-cache-misses
        hw-branch-instructions
        hw-branch-misses
        hw-bus-cycles
        hw-stalled-cycles-frontend
        hw-stalled-cycles-backend
```