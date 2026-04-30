# ohos.work_scheduler（延迟任务调度）

本模块提供延迟任务注册、取消、查询的能力。在开发过程中，对于实时性要求不高的任务，可以调用本模块接口注册延迟任务，在系统空闲时根据性能、功耗、热等情况进行调度执行。

## 导入模块

```cangjie
import kit.BackgroundTasksKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getWorkStatus(Int32)

```cangjie
public func getWorkStatus(workId: Int32): WorkInfo
```

**功能：** 通过workId获取延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|workId|Int32|是|-|延迟任务Id。|

**返回值：**

|类型|说明|
|:----|:----|
|[WorkInfo](#class-workinfo)|如果workId有效，则返回从WorkSchedulerService获取的任务，否则抛出异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[workScheduler错误码](../../errorcodes/cj-errorcode-work_scheduler.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9700001|Memory operation failed.|
  |9700002|Parcel operation failed.|
  |9700003|System service operation failed.|
  |9700004|Check workInfo failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

try{
    let workInfo = getWorkStatus(50)
    AppLog.info('workschedulerLog getWorkStatus success')
} catch (e: BusinessException) {
    AppLog.error('workschedulerLog getWorkStatus failed. code is ${e.code} message is ${e.message}')
}
```

## func isLastWorkTimeOut(Int32)

```cangjie
public func isLastWorkTimeOut(workId: Int32): Bool
```

**功能：** 检查延迟任务的最后一次执行是否超时。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|workId|Int32|是|-|指定延迟任务的Id。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示指定任务的最后一次执行超时，false表示未超时。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[workScheduler错误码](../../errorcodes/cj-errorcode-work_scheduler.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9700001|Memory operation failed.|
  |9700002|Parcel operation failed.|
  |9700003|System service operation failed.|
  |9700004|Check workInfo failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

try{
    let timeout = isLastWorkTimeOut(500)
    AppLog.info('workschedulerLog isLastWorkTimeOut success. timeout = ${timeout}')
  } catch (e: BusinessException) {
    AppLog.error('workschedulerLog isLastWorkTimeOut failed. code is ${e.code} message is ${e.message}')
}
```