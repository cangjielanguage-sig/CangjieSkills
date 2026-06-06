# hitrace

HiTrace为开发者提供业务流程调用链跟踪的维测接口。通过使用该接口所提供的功能，帮助开发者迅速获取指定业务流程调用链的运行日志，定位跨设备、跨进程、跨线程的故障问题。

## 环境要求

- 根据hdc命令行工具指导，完成[环境准备](./cj-hdc.md#环境准备)。
- 正常连接设备。

## 命令行说明

| 命令 | 含义说明 |
| -------- | -------- |
| -h  | 帮助命令。 |
| -l | 查看tag列表。 |
| --trace_begin | 开始捕获trace。 |
| --trace_finish | 结束捕获trace。 |
| --trace_dump | 导出trace信息。 |
| -b N | 设置用于存储和读取trace的缓冲区大小(buffer size KB)。默认的缓冲区大小为2048 KB。 |
| -t N | 设置hitrace运行时长，单位为秒（默认为5秒），取决于分析所需的时间。 |
| -o | 文件名指定目标文件的名称（默认为stdout）。 |
| -z | 压缩捕获的跟踪。 |
| --trace_clock | 设置向trace添加时间戳的时钟类型，可以是引导（默认）、全局、单声道、正常运行时间或性能。 |
| --trace_finish_nodump | 停止捕获trace时不打印trace信息。 |
| --start_bgsrv | 开启快照模式trace采集服务。 |
| --dump_bgsrv | 触发快照模式trace输出到文件。 |
| --stop_bgsrv | 关闭快照模式trace采集服务。 |

> **说明：**
>
> 快照模式定义为固定trace标签的trace采集服务，默认情况不落盘，开发者可通过 `--dump_bgsrv` 命令触发当前时刻的trace转储，trace为二进制格式，文件默认生成在 `/data/log/hitrace` 目录下，文件命名格式为`trace-YYMMDDHHmmSS@[BOOT_TIME].sys`。可以使用[HiSmartPerf](https://gitee.com/openharmony/developtools_smartperf_host)工具进行可视化trace分析。工具下载链接：[developtools_smartperf_host](https://gitee.com/openharmony/developtools_smartperf_host/releases)官方发行版。