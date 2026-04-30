### 应用恢复状态管理示意

应用恢复的场景不仅局限于异常时自动重启。所以需要理解应用何时会加载恢复的状态。

一句话概括就是如果应用任务的上次退出不是由用户发起的，且应用存在用于恢复的状态，应用下一次由用户拉起时的启动原因会被设为APP_RECOVERY，并清理该任务的恢复状态。

应用恢复状态标识会在状态保存接口主动或者被动调用时设置。在该应用正常退出或者应用异常退出重启后使用了该状态时清理。正常退出目前包括用户按后退键退出以及用户清理最近任务。

![应用恢复状态管理示意](./figures/20230315112155.png)

### 应用appfreeze的状态保存及恢复

支持应用appfreeze时的状态保存。CjError故障时，onSaveState接口在主线程进行回调。对于AppFreeze故障，主线程可能处于appfreeze的状态，onSaveState会在非主线程进行回调。其主要流程如下图：

![应用appfreeze状态保存恢复示意](./figures/20230315112235.png)

由于appfreeze时的回调不在CJ线程上执行，onSaveState回调中的代码建议不要使用import进来的Native动态库，禁止访问主线程创建的thread_local对象。

### 框架故障管理流程示意

故障管理是应用提升用户体验的重要手段。应用程序框架为开发者提供了故障监听、故障恢复、以及故障查询三种方式来管理应用的故障。

- 故障监听指的是通过[errorManager](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-errormanager)注册[ErrorObserver](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#struct-errorobserver)，监听故障的发生，并通知到监听方。

- 故障恢复指的是[appRecovery](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md)，及故障发生后，将应用重启恢复到故障之前的状态。

- 故障查询指的是[faultLogger](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-faultlogger.md)通过其查询接口获取当前的故障信息。

下图中并没有标记[faultLogger](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-faultlogger.md)的调用时机，开发者可以根据应用启动时传入的[LastExitReason](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#enum-lastexitreason)来决定是否调用[faultLogger](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-faultlogger.md)查询上次的故障信息。

![故障处理流程示意](./figures/20221106203527.png)

这里建议应用开发者使用[errorManager](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-errormanager)对应用的异常进行处理，处理完成后开发者可以选择调用状态保存接口并主动重启应用。

如果开发者没有注册[ErrorObserver](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#struct-errorobserver)也没有使能应用恢复，则按照系统的默认逻辑执行进程退出。用户可以选择从启动器再次打开应用。

如果开发者使能应用恢复，框架会首先检查当前故障是否支持状态保存以及开发者是否配置了状态保存，如果支持则会回调[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)的[onSaveState](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onsavestatestatetype-string)的接口。最后重启应用。