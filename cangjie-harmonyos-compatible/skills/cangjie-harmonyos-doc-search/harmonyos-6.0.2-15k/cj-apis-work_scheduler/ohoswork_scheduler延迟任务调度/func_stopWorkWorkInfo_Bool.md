## func stopWork(WorkInfo, Bool)

```cangjie
public func stopWork(work: WorkInfo, needCancel!: Bool = false): Unit
```

**功能：** 取消延迟任务。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|work|[WorkInfo](#class-workinfo)|是|-|要停止或移除的延迟任务。|
|needCancel|Bool|否|false| **命名参数。** 是否需要移除的任务。<br>- true表示停止并移除。<br>- false表示只停止不移除。<br>默认为false。|

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

let workInfo = WorkInfo(
  1,
  "com.example.myapplication",
  "MyExtension",
  batteryStatus: BatteryStatus.BATTERY_STATUS_LOW,
  isRepeat: false,
  isPersisted: true
)

try{
  stopWork(workInfo, needCancel: false)
  AppLog.info("workschedulerLog stopWork success")
} catch (e: Exception) {
  AppLog.error("workschedulerLog stopWork failed. message: ${e.toString()}")
}
```