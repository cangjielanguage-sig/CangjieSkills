# ohos.hi_trace_meter（性能打点）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

hi_trace_meter模块提供了跟踪进程轨迹，度量程序执行性能的打点能力。本模块打点的数据供hiTraceMeter工具分析使用。

> **说明**
>
> - 性能打点接口startTrace、finishTrace、traceByValue无法指定跟踪输出级别，默认均为COMMERCIAL级别性能打点。
>
> - 用户态trace格式使用竖线 | 作为分隔符，所以通过性能打点接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。
>
> - 用户态trace总长度限制512字符，超过的部分将会被截断。

## 导入模块

```cangjie
import kit.PerformanceAnalysisKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。