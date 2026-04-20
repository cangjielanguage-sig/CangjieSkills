## func getTask(UIAbilityContext, String, ?String)

```cangjie
public func getTask(context: UIAbilityContext, id: String, token!: ?String = None): Task
```

**功能：** 根据任务id查询任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名  | 类型 | 必填 | 默认值 | 说明                           |
| :------ | :----- | :--- | :----- | :----------------------------- |
| context | [UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext) | 是   | -      | 基于应用程序的上下文。         |
| id      | String  | 是   | -      | 任务id。                       |
| token   | ?String  | 否   | None   | **命名参数。** 任务查询token。 |

**返回值：**

| 类型                | 说明                                               |
| :------------------ | :------------------------------------------------- |
| [Task](#class-task) | 返回一个Task对象，里面包括任务id和任务的配置信息。 |

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13400003 | Task service ability error. |
  | 13499999 | Other error. |
  | 21900006 | Task removed or not found. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let taskId = "example_task_id"
    let task = getTask(context, taskId)
    Hilog.info(0, "test", "成功获取任务，任务ID: ${task.tid}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func remove(String)

```cangjie
public func remove(id: String): Unit
```

**功能：** 移除属于调用方的指定任务，如果正在处理中，该任务将被迫停止。在调用后任务对象和其回调函数会被释放。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型   | 必填 | 默认值 | 说明     |
| :----- | :----- | :--- | :----- | :------- |
| id     | String | 是   | -      | 任务id。 |

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
    remove(taskId)
    Hilog.info(0, "test", "成功移除任务，任务ID: ${taskId}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func search(Filter)

```cangjie
public func search(filter!: Filter = Filter()): Array<String>
```

**功能：** 根据[Filter](#class-filter)过滤条件查找任务id。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型                    | 必填 | 默认值   | 说明       |
| :----- | :---------------------- | :--- | :------- | :--------- |
| filter | [Filter](#class-filter) | 否   | Filter() | **命名参数。** 过滤条件。 |

**返回值：**

| 类型           | 说明                 |
| :------------- | :------------------- |
| Array\<String> | 返回满足条件任务id。 |

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13400003 | Task service ability error. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let filter = Filter()
    let taskIds = search(filter: filter)
    Hilog.info(0, "test", "搜索到任务数量: ${taskIds.size}")
    for (id in taskIds) {
        Hilog.info(0, "test", "任务ID: ${id}")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```