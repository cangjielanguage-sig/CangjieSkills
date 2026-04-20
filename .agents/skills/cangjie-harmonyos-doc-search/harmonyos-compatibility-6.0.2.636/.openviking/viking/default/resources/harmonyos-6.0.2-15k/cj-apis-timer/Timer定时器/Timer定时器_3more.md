# Timer（定时器）

本模块提供基础的定时器能力，支持按照指定的时间执行对应函数。基于仓颉编程语言标准库，具体请参见[仓颉语言编程语言库API](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-std_module_overview)。

## 导入

```cangjie
import std.sync.Timer
```

## static func once(Duration, ()->Unit)

```cangjie
public static func once(delay: Duration, task: ()->Unit): Timer
```

**功能：** 设置并启动一次性定时任务，返回控制这个任务的[Timer](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_classes#class-timer)对象实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|delay|[Duration](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#struct-duration)|是|-|从现在开始到Task被执行的时间间隔。取值范围[[Duration.Min](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-min)，[Duration.Max](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-max)]，小于或等于[Duration.Zero](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-core_package_structs#static-const-zero)时Task将立即被执行。|
|task|()->Unit|是|-|待定时执行的任务。|

**返回值：**

|类型|说明|
|:---|:---|
|Timer|[Timer](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-sync_package_classes#class-timer)对象实例。|