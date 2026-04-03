## func obtainAllWorks()

```cangjie
public func obtainAllWorks(): Array<WorkInfo>
```

**功能：** 获取当前应用所有的延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WorkInfo](#class-workinfo)>|返回当前应用所有的延迟任务。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[workScheduler错误码](../../errorcodes/cj-errorcode-work_scheduler.md).

  |错误码ID|错误信息|
  |:---|:---|
  |9700001|Memory operation failed.|
  |9700002|Parcel operation failed.|
  |9700003|System service operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

try{
    let works = obtainAllWorks()
    AppLog.info('workschedulerLog obtainAllWorks success. work size = ${works.size}')
} catch (e: BusinessException) {
    AppLog.error('workschedulerLog obtainAllWorks failed. code is ${e.code} message is ${e.message}')
}
```

## func startWork(WorkInfo)

```cangjie
public func startWork(work: WorkInfo): Unit
```

**功能：** 申请延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|work|[WorkInfo](#class-workinfo)|是|-|要添加到执行队列的延迟任务。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[workScheduler错误码](../../errorcodes/cj-errorcode-work_scheduler.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9700001|Memory operation failed.|
  |9700002|Parcel operation failed.|
  |9700003|System service operation failed.|
  |9700004|Check workInfo failed.|
  |9700005|StartWork failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*
import kit.AbilityKit.*

let workInfo = WorkInfo(
    1,
    "com.example.myapplication",
    "MyExtension",
    batteryStatus: BatteryStatus.BATTERY_STATUS_LOW,
    isRepeat: false,
    isPersisted: true)

startWork(workInfo)
```

## func stopAndClearWorks()

```cangjie
public func stopAndClearWorks(): Unit
```

**功能：** 停止和取消当前应用所有的延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[workScheduler错误码](../../errorcodes/cj-errorcode-work_scheduler.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.|
  |9700001|Memory operation failed.|
  |9700002|Parcel operation failed.|
  |9700003|System service operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

let workInfo = WorkInfo(
  1,
  "com.example.myapplication",
  "MyExtension",
  batteryStatus: BatteryStatus.BATTERY_STATUS_LOW,
  isRepeat: false,
  isPersisted: true
)

try{
  startWork(workInfo)
  stopAndClearWorks()
  AppLog.info('stopAndClearWorks success')
} catch (e: BusinessException) {
  AppLog.error('stopAndClearWorks failed. code is ${e.code} message is ${e.message}')
}
```