# ohos.hiviewdfx.hi_app_event（应用事件打点）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

hi_app_event模块提供应用打点和事件订阅能力，包括事件存储、事件订阅、事件清理、打点配置等功能。[HiAppEvent](#class-hiappevent)将应用运行过程中触发的事件信息统一归纳到[AppEventInfo](#class-appeventinfo)中，并将事件分为系统事件和应用事件两类。

系统事件来源于系统服务，是系统预先定义的事件，这类事件信息中的事件参数对象params包含的字段已由各系统事件定义，具体字段含义在各系统事件指南的介绍中。

应用事件来源于应用，是应用开发者自己定义的事件，这类事件信息支持自定义后通过[Write](#static-func-writeappeventinfo)打点接口进行配置设定，具体字段含义可结合开发者需求展开。

## 导入模块

```cangjie
import kit.PerformanceAnalysisKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。