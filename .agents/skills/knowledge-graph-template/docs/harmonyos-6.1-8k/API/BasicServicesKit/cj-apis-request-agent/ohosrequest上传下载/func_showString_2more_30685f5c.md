## func show(String)

```cangjie
public func show(id: String): TaskInfo
```

**功能：** 根据任务id查询任务的详细信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型   | 必填 | 默认值 | 说明     |
| :----- | :----- | :--- | :----- | :------- |
| id     | String | 是   | -      | 任务id。 |

**返回值：**

| 类型                        | 说明                             |
| :-------------------------- | :------------------------------- |
| [TaskInfo](#class-taskinfo) | 返回任务详细信息的TaskInfo对象。 |

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13400003 | Task service ability error. |
  | 21900006 | Task removed or not found. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let taskId = "example_task_id"
    let taskInfo = show(taskId)
    Hilog.info(0, "test", "任务信息: ${taskInfo.description}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func touch(String, String)

```cangjie
public func touch(id: String, token: String): TaskInfo
```

**功能：** 根据任务id和token查询任务的详细信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型   | 必填 | 默认值 | 说明            |
| :----- | :----- | :--- | :----- | :-------------- |
| id     | String | 是   | -      | 任务id。        |
| token  | String | 是   | -      | 任务查询token。 |

**返回值：**

| 类型                        | 说明                             |
| :-------------------------- | :------------------------------- |
| [TaskInfo](#class-taskinfo) | 返回任务详细信息的TaskInfo对象。 |

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13400003 | Task service ability error. |
  | 21900006 | Task removed or not found. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let taskId = "example_task_id"
    let token = "example_token"
    let taskInfo = touch(taskId, token)
    Hilog.info(0, "test", "任务信息: ${taskInfo.description}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```