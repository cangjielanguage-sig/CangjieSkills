## func search(Filter)

```cangjie
public func search(filter: Filter): Array<String>
```

**功能：** 根据[Filter](#class-filter)过滤条件查找任务id。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filter|[Filter](#class-filter)|是|-|过滤条件。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回满足条件任务id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)

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
import ohos.base.*

try {
    let tids: Array<String> = search(Filter(state: State.INITIALIZED))
} catch (e: BusinessException) {
    Hilog.error(0, "SearchTask", "Failed to search task, ${e}")
}
```

## func show(String)

```cangjie
public func show(id: String): TaskInfo
```

**功能：** 根据任务id查询任务的详细信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|任务id。|

**返回值：**

| 类型                | 说明                      |
| :------------------- | :------------------------- |
| [TaskInfo](#class-taskinfo) | 返回任务详细信息的TaskInfo对象。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | parameter error. Possible causes: 1. Missing mandatory parameters 2. Incorrect parameter type. |
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
    let taskInfo = show("123456")
} catch (e: BusinessException) {
    Hilog.error(0, "ShowTask", "Failed to show task, ${e}")
}
```

## func touch(String, String)

```cangjie
public func touch(id: String, token: String): TaskInfo
```

**功能：** 根据任务id和token查询任务的详细信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|任务id。|
|token|String|是|-|任务查询token。|

**返回值：**

| 类型                | 说明                      |
| :------------------- | :------------------------- |
| [TaskInfo](#class-taskinfo) | 返回任务详细信息的TaskInfo对象。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | parameter error. Possible causes: 1. Missing mandatory parameters 2. Incorrect parameter type 3. Parameter verification failed. |
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
    let taskInfo = touch("123456", "token123456")
} catch (e: BusinessException) {
    Hilog.error(0, "TouchTask", "Failed to touch task, ${e}")
}
```