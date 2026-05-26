## func getTask(StageContext, String, ?String)

```cangjie
public func getTask(context: StageContext, id: String, token!: ?String = None): Task
```

**功能：** 根据任务id查询任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|基于应用程序的上下文。|
|id|String|是|-|任务id。|
|token|?String|否|None| **命名参数。** 任务查询token。|

**返回值：**

|类型|说明|
|:----|:----|
|[Task](#class-task)|返回一个Task对象，里面包括任务id和任务的配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | parameter error. Possible causes: 1. Missing mandatory parameters 2. Incorrect parameter type 3. Parameter verification failed.|
  | 13400003 | Task service ability error. |
  | 21900006 | Task removed or not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import ohos.base.*

try {
    let task = getTask(Global.getStageContext(), "123456")  // 需获取Context应用上下文，详见本文使用说明
} catch (e: BusinessException) {
    Hilog.error(0, "GetTask", "Failed to get task, ${e}")
}
```

## func remove(String)

```cangjie
public func remove(id: String): Unit
```

**功能：** 移除属于调用方的指定任务。如果正在处理中，该任务将被迫停止。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|任务id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 13400003 | Task service ability error. |
  | 21900006 | Task removed or not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import ohos.base.BusinessException

try {
    remove("12345")
} catch (e: BusinessException) {
    Hilog.error(0, "TaskRemove", "${e}")
}
```

## func search()

```cangjie
public func search(): Array<String>
```

**功能：** 根据默认[Filter](#class-filter)过滤条件查找任务id。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回满足条件任务id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | parameter error. Possible causes: 1. Incorrect parameter type 2. Parameter verification failed. |
  | 13400003 | Task service ability error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import ohos.base.BusinessException

try {
    let tids = search()
} catch (e: BusinessException) {
    Hilog.error(0, "TaskRemove", "${e}")
}
```