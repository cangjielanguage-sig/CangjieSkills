## func requestSuspendDelay(String, () -> Unit)

```cangjie
public func requestSuspendDelay(reason: String, callback: () -> Unit): DelaySuspendInfo
```

**功能：** 申请短时任务。

> **说明：**
>
> 短时任务的申请时间最长为3分钟，低电量时最长为1分钟。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|String|是|-|申请短时任务的原因。|
|callback|() -> Unit|是|-|短时任务即将超时的回调函数，一般在超时前6秒，通过此回调通知应用。|

**返回值：**

|类型|说明|
|:----|:----|
|[DelaySuspendInfo](#class-delaysuspendinfo)|返回短时任务信息。|

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

let myReason = "test requestSuspendDelay"
try {
    let delayInfo = requestSuspendDelay(myReason, { =>
        AppLog.info("Request suspension delay will time out.")
    })
    let id = delayInfo.requestId
    let time = delayInfo.actualDelayTime
    AppLog.info("The requestId is: ${id}")
    AppLog.info("The actualDelayTime is: ${time}")
} catch (e: BusinessException) {
    AppLog.info("requestSuspendDelay failed. code is ${e.code} message is ${e.message}")
}
```

## func stopBackgroundRunning(StageContext)

```cangjie
public func stopBackgroundRunning(context: StageContext): Unit
```

**功能：** 向系统申请取消长时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用运行的上下文。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.BackgroundTasksKit.*

let stageContext = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
stopBackgroundRunning(stageContext)
```

## class DelaySuspendInfo

```cangjie
public class DelaySuspendInfo {
    public DelaySuspendInfo(
        public let requestId: Int32,
        public let actualDelayTime: Int32
    )
}
```

**功能：** 短时任务信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 12

### let actualDelayTime

```cangjie
public let actualDelayTime: Int32
```

**功能：** 应用实际申请的短时任务时间，单位为毫秒。短时任务申请时间最长为3分钟，低电量时最长为1分钟。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let requestId

```cangjie
public let requestId: Int32
```

**功能：** 短时任务的请求ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### DelaySuspendInfo(Int32, Int32)

```cangjie
public DelaySuspendInfo(
    public let requestId: Int32,
    public let actualDelayTime: Int32
)
```

**功能：** 构造DelaySuspendInfo对象。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|requestId|Int32|是|-|短时任务的请求ID。|
|actualDelayTime|Int32|是|-|应用实际申请的短时任务时间，单位为毫秒。短时任务申请时间最长为3分钟，低电量时最长为1分钟。|