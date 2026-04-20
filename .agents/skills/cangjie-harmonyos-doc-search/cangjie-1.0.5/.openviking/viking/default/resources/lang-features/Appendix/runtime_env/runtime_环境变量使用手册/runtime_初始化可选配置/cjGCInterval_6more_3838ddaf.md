### `cjGCInterval`

指定两次 GC 的间隔时间值，取值必须大于 0，支持单位为 s、ms、us、ns，推荐单位为毫秒（ms）。若本次 GC 距离上次 GC 的间隔小于此值，则本次 GC 将被忽略。该参数可以控制 GC 的频率。默认值为 150 ms。

例如：

```shell
export cjGCInterval=150ms
```

### `cjBackupGCInterval`

指定 backup GC 的间隔值，取值必须大于 0，支持单位为 s、ms、us、ns，推荐单位为秒（s），当仓颉运行时在该参数设定时间内未触发 GC，则触发一次 backup GC。默认值为 240 秒，即 4 分钟。

例如：

```shell
export cjBackupGCInterval=240s
```

### `cjProcessorNum`

指定仓颉线程的最大并发数，支持设置范围为 (0, CPU 核数 * 2]，超出范围的设置无效，仍旧使用默认值。调用系统 API 获取 cpu 核数，若成功默认值为 cpu 核数，否则默认值为 8。

例如：

```shell
export cjProcessorNum=2
```

### `cjStackSize`

指定仓颉线程的栈大小，支持单位为 kb（KB）、mb（MB）、gb（GB），支持设置范围为 Linux 平台下[64KB, 1GB]，Windows 平台下[128KB, 1GB]，超出范围的设置无效，仍旧使用默认值。默认值为 128KB。

例如：

```shell
export cjStackSize=100kb
```

### 运维日志可选配置

#### `MRT_LOG_FILE_SIZE`

指定 runtime 运维日志的文件大小，默认值为 10 MB，支持单位为 kb（KB）、mb（MB）、gb（GB），设置值需大于 0。

日志大小超过该值时，会重新回到日志开头进行打印。

最终生成日志大小略大于 MRT_LOG_FILE_SIZE。

例如：

```shell
export MRT_LOG_FILE_SIZE=100kb
```

#### `MRT_LOG_PATH`

指定 runtime 运维日志的输出路径，若该环境变量未设置或路径设置失败，则运维日志默认打印到 stdout（标准输出）或 stderr（标准错误）中。

例如：

```shell
export MRT_LOG_PATH=/home/cangjie/runtime/runtime_log.txt
```

#### `MRT_LOG_LEVEL`

指定 runtime 运维日志的最小输出级别，大于等于这个级别的日志会被打印，默认值为 e，支持设置值为[v|d|i|w|e|f|s]。v（VERBOSE）、d（DEBUGY）、i（INFO）、w（WARNING）、e（ERROR）、f（FATAL）、s（FATAL_WITHOUT_ABORT）。

例如：

```shell
export MRT_LOG_LEVEL=v
```

#### `MRT_REPORT`

指定 runtime GC 日志的输出路径，若该环境变量未设置或路径设置失败，该日志默认不打印。

例如：

```shell
export MRT_REPORT=/home/cangjie/runtime/gc_log.txt
```

#### `MRT_LOG_CJTHREAD`

指定 cjthread 日志的输出路径，若该环境变量未设置或路径设置失败，该日志默认不打印。

例如：

```shell
export MRT_LOG_CJTHREAD=/home/cangjie/runtime/cjthread_log.txt
```

#### `cjHeapDumpOnOOM`

指定是否要在发生堆溢出后输出堆快照文件，默认不开启。支持设置值为[on|off]，设定为 on 时开启功能，设定 off 或者其他值不开启功能。

例如：

```shell
export cjHeapDumpOnOOM=on
```

#### `cjHeapDumpLog`

指定输出堆快照文件的路径。注意指定的路径必须存在，且应用执行者对其具有读写权限。如果不指定，堆快照文件将输出到当前执行目录。

例如：

```shell
export cjHeapDumpLog=/home/cangjie
```

### 运行环境可选配置

#### `MRT_STACK_CHECK`

开启 native stack overflow 检查，默认不开启，支持设置值为 1、true、TRUE 开启功能。

例如：

```shell
export MRT_STACK_CHECK=true
```

#### `CJ_SOF_SIZE`

当 StackOverflowError 发生时，将自动进行异常栈折叠方便用户阅读，折叠后栈帧层数默认值是 32。可以通过配置此环境变量控制折叠栈长度，支持设置为 int 范围内的整数。
CJ_SOF_SIZE = 0，打印所有调用栈；
CJ_SOF_SIZE < 0，从栈底开始打印环境变量配置层数；
CJ_SOF_SIZE > 0，从栈顶开始打印环境变量配置层数；
CJ_SOF_SIZE 未配置，默认打印栈顶开始 32 层调用栈；

例如：

```shell
export CJ_SOF_SIZE=30
```