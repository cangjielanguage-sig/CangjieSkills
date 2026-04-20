## 使用说明

通过 `cjprof --help` 即可查看命令使用方法。支持 `record`，`report` 和 `heap` 子命令，分别用于采集 CPU 热点函数信息、生成 CPU 热点函数报告（包含火焰图）和导出与分析堆内存。

```text
cjprof --help
 Usage: cjprof [--help] COMMAND [ARGS]

The supported commands are:
  -v        Print version of cjprof
  heap      Dump heap into a dump file or analyze the heap dump file
  record    Run a command and record its profile data into data file
  report    Read profile data file (created by cjprof record) and display the profile
```

> **注意：**
>
> 由于 `cjprof record` 依赖系统的 `perf` 权限，因此使用需要满足以下两个条件之一：
>
> - 使用 `root` 用户或 `sudo` 权限执行。
> - 系统的 `perf_event_paranoid` 参数（通过 `/proc/sys/kernel/perf_event_paranoid` 文件）配置为 -1 。
>
> 否则可能会出现权限不足的问题。

### 采集 CPU 热点函数信息

#### 命令

```text
cjprof record
```

#### 格式

```text
cjprof record [<options>] [<command>]
cjprof record [<options>] -- <command> [<options>]
```

#### 选项

`-f, --freq <freq>` 指定采样频率，单位为赫兹（Hz），即每秒采样次数，默认为 5000 Hz，当指定为 max 或超过系统支持的最大频率时，取系统支持的最大频率。

`-o, --output <file>` 指定采样结束后生成的采样数据文件名，默认为 `cjprof.data` 。

`-p, --pid <pid>` 指定被采样应用程序的进程 ID，当指定 `<command>` 新启动应用程序进行采样时，该选项会被忽略。

#### 示例

- 采样正在运行的应用程序。

    ```text
    # 以 10000 Hz 的采样频率对正在运行的应用程序（进程号为 12345）进行采样，采样结束后将采样数据生成在当前路径下名为 sample.data 的文件中。
    cjprof record -f 10000 -p 12345 -o sample.data
    ```

- 新启动应用程序并对其进行采样。

    ```text
    # 执行当前路径下的 `test` 应用程序，参数为 `arg1 arg2` ，并以系统支持的最大采样频率对其进行采样，采样结束后将采样数据生成在当前路径下名为 `cjprof.data` （默认文件名）的文件中。
    cjprof record -f max -- ./test arg1 arg2
    ```

#### 注意事项

开始采样后，只有被采样程序退出后才会结束采样。如果需要提前结束采样，可以在采样过程中通过按 `Ctrl+C` 主动停止采样。

### 生成 CPU 热点函数报告

#### 命令

```text
cjprof report
```

#### 格式

```text
cjprof report [<options>]
```

#### 选项

`-F, --flame-graph` 生成 CPU 热点函数火焰图，而非默认的文本报告。

`-i, --input <file>` 采样数据文件名，默认为 `cjprof.data` 。

`-o, --output <file>` 生成的 CPU 热点函数火焰图文件名，默认为 `FlameGraph.svg`，仅当生成火焰图时才有效。

#### 示例

- 生成默认的 CPU 热点函数文本报告。

    ```text
    # 分析 sample.data 中的采样数据，生成 CPU 热点函数文本报告。
    cjprof report -i sample.data
    ```

- 生成 CPU 热点函数火焰图。

    ```text
    # 分析 cjprof.data（默认文件）中的采样数据，生成名为 test.svg 的 CPU 热点函数火焰图。
    cjprof report -F -o test.svg
    ```

#### 报告形式说明

文本形式的报告包含函数采样总占比（包含子函数）、函数采样占比（自身）以及函数名（如果没有对应的符号信息则显示为地址）三部分，报告结果以函数采样总占比降序排列。

火焰图中的横轴代表采样占比大小，越宽表示采样占比越大，即运行时间越长，纵轴表示调用栈，父函数在下，子函数在上。