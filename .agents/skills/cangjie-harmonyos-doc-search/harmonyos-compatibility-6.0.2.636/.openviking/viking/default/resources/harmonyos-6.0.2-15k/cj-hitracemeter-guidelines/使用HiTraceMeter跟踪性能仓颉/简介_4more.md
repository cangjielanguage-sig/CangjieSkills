## 简介

HiTraceMeter提供系统性能打点接口。开发者通过在关键代码位置调用HiTraceMeter接口提供的API接口，能够有效跟踪进程轨迹、查看系统性能。

## 基本概念

**HiTraceMeter Tag：** 跟踪数据使用类别分类，称作HiTraceMeter Tag或HiTraceMeter Category。一般每个软件子系统对应一个Tag，该Tag在打点API中以类别Tag参数传入。HiTraceMeter命令行工具采集跟踪数据时，只采集给定的Tag类别选项指定的跟踪数据。

## 实现原理

1. 应用程序通过HiTraceMeter函数接口进行打点，HiTraceMeter函数将跟踪数据通过内核sysfs文件接口输出到内核的ftrace数据缓冲区。

2. HiTraceMeter命令行工具读取内核ftrace缓冲区中的跟踪数据，将文本格式的跟踪数据保存到设备侧的文件中。

## 接口说明

性能打点跟踪接口由HiTraceMeter模块提供，详细API请参见[性能打点跟踪API参考](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-hi_tracemeter.md)。

| 接口名 | 描述 |
| -------- | -------- |
| HiTraceMeter.startTrace(name: String, taskId: Int32): Unit | 异步时间片跟踪接口，标记一个预跟踪耗时任务的开始。taskId是trace中用来表示关联的ID，如果有多个name相同的任务并行执行，则每次调用startTrace的taskId不同；如果具有相同name的任务是串行执行的，则taskId可以相同。 |
| HiTraceMeter.finishTrace(name: String, taskId: Int32): Unit | 异步时间片跟踪接口，name和taskId必须与流程开始的hiTraceMeter.startTrace对应参数值保持一致。 |
| HiTraceMeter.traceByValue(name: String, count: Int32): Unit | 整数跟踪接口，用来标记一个预跟踪的数值变量，该变量的数值会不断变化。 |

HiTraceMeter打点接口按功能/行为分类，主要分三类：同步时间片跟踪接口、异步时间片跟踪接口和整数跟踪接口。无论同步时间片跟踪接口还是异步时间片跟踪接口，接口本身都是同步接口，不是异步接口，都用在同一线程中，不支持跨线程打点和分析。

- 同步时间片跟踪接口用于顺序执行的打点场景，目前Cangjie暂未提供相关接口。
- 异步时间片跟踪接口用于在操作调用前开始打点，在操作完成后进行结束打点。异步跟踪的开始和结束由于不是顺序发生的，解析trace时需要通过唯一的taskId进行识别，taskId作为异步跟踪trace接口的参数传入。
- 整数跟踪接口用于跟踪数值变量。