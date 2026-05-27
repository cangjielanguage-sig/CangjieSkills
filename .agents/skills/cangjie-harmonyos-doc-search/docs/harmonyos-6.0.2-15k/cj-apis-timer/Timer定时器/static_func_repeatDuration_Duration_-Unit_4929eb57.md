## static func repeat(Duration, Duration, ()->Unit, CatchupStyle)

```cangjie
public static func repeat(delay: Duration, interval: Duration, task: ()->Unit, style!: CatchupStyle = Burst): Timer
```

**功能：** 设置并启动重复性定时任务，返回控制这个任务的[Timer](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_classes#class-timer)对象实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|delay|[Duration](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#struct-duration)|是|-|从现在开始到Task被执行的时间间隔。取值范围[[Duration.Min](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-min)，[Duration.Max](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-max)]，小于或等于[Duration.Zero](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-zero)时Task将立即被执行。|
|interval|[Duration](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#struct-duration)|是|-|两次Task之间的时间间隔。取值范围([Duration.Zero](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-zero)，[Duration.Max](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-max)]。|
|task|()->Unit|是|-|待定时执行的任务。|
|style|CatchupStyle|否|Burst|追平策略。<br> 当Task执行时间过长时，后续任务执行时间点可能发生延迟，不同的追平策略适用于不同的场景，详见[CatchupStyle](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_enums#enum-catchupstyle)说明。|

**返回值：**

|类型|说明|
|:---|:---|
|Timer|[Timer](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_classes#class-timer)对象实例。|