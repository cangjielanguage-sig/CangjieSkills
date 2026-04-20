## record命令

采样指定目标程序，并且将采样数据保存到指定的文件中(默认为/data/local/tmp/perf.data)。

**record命令参数说明：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help  | 帮助命令。 |
| -a  | 采集整机信息，用于评估所有进程、线程。 |
| --exclude-hiperf | 不采集hiperf本身数据。 |
| -c | 设置采集的cpuid,只采集这些cpu数据。 |
| --cpu-limit | 设置采集时cpu最大占比，取值范围：1 - 100，默认25。 |
| -d | 采集时长。 |
| -f | 采集频率，默认4000次每秒，不能和--period一起使用。 |
| --period | 设置采集事件周期，多少事件采集一次，不能和-f一起使用。 |
| -e | 采集事件，以逗号隔开。 |
| -g | 采集事件群组，以逗号隔开。 |
| --no-inherit | 不采集子进程数据。 |
| -p | 采集进程ID，以逗号隔开，不能和-a一起使用。 |
| -t | 采集线程ID，以逗号隔开，不能和-a一起使用。 |
| --exclude-tid | 不采集线程ID，以逗号隔开，不能和-a一起使用。 |
| --exclude-thread | 不采集线程名，以逗号隔开，不能和-a一起使用。 |
| --offcpu | 跟踪线程何时脱离cpu调度。 |
| -j | 分支堆栈采样，过滤器支持any、any_call、any_ret、ind_call、ind_jmp、cond、call。 |
| -s/--callstack | 设置回栈模式。 |
| --kernel-callchain | 采集内核态堆栈，必须和-s fp/dwarf一起使用。 |
| --callchain-useronly | 只收集用户态堆栈。 |
| --delay-unwind | -s dwarf被设置时栈会在录制时展开，设置此选项栈会在录制后展开。 |
| --disable-unwind | -s dwarf被设置时，默认情况下，录制时堆栈将不会展开。 |
| --disable-callstack-expand | -s dwarf被设置时，破除64K栈限制，默认情况下合并callstack构建更完整的调用堆栈，可能有时候会不准确。 |
| --enable-debuginfo-symbolic | -s fp/dwarf被设置时，elf在.gnu_debugdata段的符号会被解析，默认不解析。 |
| --clockid | 设置采集时钟类型，支持monotonic 和 monotonic_raw。 |
| --symbol-dir | 在线符号化符号表文件路径。 |
| -m | mmap页数量，取值范围：2 - 1024，默认1024。 |
| --app | 采集的应用程序名，以逗号隔开，应用程序必须是debuggable模式，应用程序未启动时会等待20s。 |
| --chkms | 设置查询的间隔时间，取值范围：1 - 200，默认10。 |
| --data-limit | 输出数据达到指定大小停止采集，默认无限制。 |
| -o | 设置输出文件路径。 |
| -z | 以压缩文件形式输出。 |
| --restart | 收集应用启动的性能指标信息，如果进程在30秒内未启动，记录将退出。 |
| --verbose | 输出更详细的报告。 |
| --control [command]| 采集命令控制参数。命令包括prepare/start/pause/resume/stop。 |
| --dedup_stack | 删除记录中的重复堆栈，不能和-a一起使用。 |
| --cmdline-size | 设置/sys/kernel/tracing/saved_cmdlines_size节点的值，取值范围：512 - 4096。 |
| --report | 采集后回栈报告，不能和-a一起使用。 |
| --dumpoptions | dump命令选项。 |

```shell
Usage: hiperf record [options] [command [command-args]]
```

对指定的PID为267的进程采样10秒，并且使用dwarf回栈。

```shell
hiperf record -p 267 -d 10 -s dwarf
```

**使用样例：**

```bash
$ hiperf record -p 1273 -d 10 -s dwarf
Profiling duration is 10.000 seconds.
Start Profiling...
Timeout exit (total 10000 ms)
Process and Saving data...
/proc/sys/kernel/kptr_restrict is NOT 0, will try set it to 0.
[ hiperf record: Captured 0.297 MB perf data. ]
[ Sample records: 97, Non sample records: 2426 ]
[ Sample lost: 0, Non sample lost: 0 ]
```