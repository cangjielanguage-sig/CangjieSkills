# ohos.background_task_mgr（后台任务管理）

本模块提供申请后台任务的接口。当应用退至后台时，开发者可以通过本模块接口为应用申请短时、长时任务，避免应用进程被终止或挂起。

## 导入模块

```cangjie
import kit.BackgroundTasksKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func cancelSuspendDelay(Int32)

```cangjie
public func cancelSuspendDelay(requestId: Int32): Unit
```

**功能：** 取消短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|requestId|Int32|是|-|短时任务的请求ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[backgroundTaskManager错误码](../../errorcodes/cj-errorcode-background_task_mgr.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9800001|Memory operation failed.|
  |9800002|Parcel operation failed.|
  |9800003|Inner transact failed.|
  |9800004|System service operation failed.|
  |9900001|Caller information verification failed.|
  |9900002|Background task verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

let id: Int32 = 1
try {
    cancelSuspendDelay(id)
} catch (e: BusinessException) {
    AppLog.info("cancelSuspendDelay failed. code is ${e.code} message is ${e.message}")
}
```

## func getRemainingDelayTime(Int32)

```cangjie
public func getRemainingDelayTime(requestId: Int32): Int32
```

**功能：** 获取本次短时任务的剩余时间。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|requestId|Int32|是|-|短时任务的请求ID。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回本次短时任务的剩余时间，单位为毫秒。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[backgroundTaskManager错误码](../../errorcodes/cj-errorcode-background_task_mgr.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9800001|Memory operation failed.|
  |9800002|Parcel operation failed.|
  |9800003|Inner transact failed.|
  |9800004|System service operation failed.|
  |9900001|Caller information verification failed.|
  |9900002|Background task verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BackgroundTasksKit.*

let id: Int32 = 1
let time = getRemainingDelayTime(id)
```