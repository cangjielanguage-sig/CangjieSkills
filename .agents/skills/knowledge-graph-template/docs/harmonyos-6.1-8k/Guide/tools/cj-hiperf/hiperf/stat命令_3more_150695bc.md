## stat命令

监听指定目标程序，周期性打印性能计数器的值。

**stat命令参数说明：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| -a  | 采集整机信息，用于评估所有进程、线程。 |
| -c | 设置采集的cpuid,限制采集哪些cpu数据。 |
| -d | 采集时长。 |
| -i | 设置每隔多少ms打印stat信息。 |
| -e | 采集事件，以逗号隔开。 |
| -g | 采集事件群组，以逗号隔开。 |
| --no-inherit | 不采集子进程数据。 |
| -p | 采集进程ID，以逗号隔开，不能和-a一起使用。 |
| -t | 采集线程ID，以逗号隔开，不能和-a一起使用。 |
| --app | 采集的应用程序名，以逗号隔开，应用程序必须是debuggable模式，应用程序未启动时会等待10秒。 |
| --chkms | 设置查询的间隔时间，取值范围：1 - 200，默认10。 |
| --per-core | 每个cpu核的打印计数。 |
| --pre-thread | 每个线程的打印计数。 |
| --restart | 收集应用启动的性能指标信息，如果进程在30秒内未启动，记录将退出。 |
| --verbose | 输出更详细的报告。 |
| --dumpoptions | dump命令选项。 |

```shell
Usage: hiperf stat [options] [command [command-args]]
```

下面展示了一个 stats 监听1273进程在CPU0上3秒的性能计数器命令。

```shell
hiperf stat -p 1273 -d 3 -c 0
```

**使用样例：**

```bash
$ hiperf stat -p 1273 -d 3 -c 0
Profiling duration is 3.000 seconds.
Start Profiling...
Timeout exit (total 3000 ms)
                    count  name                           | comment                          | coverage
                      521  hw-branch-instructions         |                                  | (9%)
                      217  hw-branch-misses               |                                  | (9%)
                   32,491  hw-cpu-cycles                  |                                  | (9%)
                    4,472  hw-instructions                |                                  | (9%)
                        1  sw-context-switches            |                                  | (9%)
                        0  sw-page-faults                 |                                  | (9%)
                   39,083  sw-task-clock                  | 0.000143 cpus used               | (9%)
```

## dump命令

此命令主要以不加以处理的方式直接读取perf.data的数据，开发和测试人员可核对其中原始采样数据的正确性。

**dump命令参数说明：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| --head | 只输出数据头和属性。 |
| -d | 只输出数据段。 |
| -f | 只输出附加功能。 |
| --syspath | 符号表文件路径。 |
| -i | 资源文件路径。 |
| -o | 输出文件路径，未设置则输出到屏幕。 |
| --elf | 输出elf文件。 |
| --proto | 输出protobuf格式数据。 |
| --export | 将用户堆栈数据导出到某个分割文件，使用此命令生成ut数据。 |

```shell
Usage: hiperf dump [option] <filename>
```

使用dump命令将/data/local/tmp/perf.data文件读取出来，输出到/data/local/tmp/perf.dump文件中。

```shell
hiperf dump -i /data/local/tmp/perf.data -o /data/local/tmp/perf.dump
```

**使用样例：**

```bash
$ hiperf dump -i /data/local/tmp/perf.data -o /data/local/tmp/perf.dump
dump result will save at '/data/local/tmp/perf.dump'
```

## report命令

此命令主要用于展示相关采样数据（从perf.data中读取）并且转换为用户需要的格式（比如Json或者ProtoBuf）。

**report命令参数说明：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| --symbol-dir | 符号表文件路径。 |
| --limit-percent | 只显示前面多少百分比的内容。 |
| -s | 显示回栈模式。 |
| --call-stack-limit-percent | 只显示前面多少百分比的堆栈内容。 |
| -i | 资源文件路径，默认perf.data。 |
| -o | 输出文件路径，未设置则输出到屏幕。 |
| --proto | 输出protobuf格式数据。 |
| --json | 输出json格式数据。 |
| --diff | 显示-i --diff两个文件的不同。 |
| --branch | 从地址而不是ip地址显示分支。 |
| --\<keys> \<keyname1>\[,keyname2]\[,...] | 可选关键字：comms、pids、tids、dsos、funcs、from_dsos、from_funcs，例如： --comms hiperf。 |
| --sort [key1],[key2],[...] | 按关键字排序。 |
| --hide_count | 报告中不显示数值。 |
| --dumpoptions | dump命令选项。 |

```shell
Usage: hiperf report [option] <filename>
```

范例输出普通报告的命令，限制为占比不超过1%。

```shell
hiperf report --limit-percent 1
```