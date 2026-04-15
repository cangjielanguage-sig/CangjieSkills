## class Task

```cangjie
public class Task {
    public let tid: String
    public var config: Config

    public init(tid: String, config: Config)
}
```

**功能：** 上传或下载任务。使用该方法前需要先获取Task对象，通过create获取。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var config

```cangjie
public var config: Config
```

**功能：** 任务的配置信息。

**类型：** [Config](#class-config)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let tid

```cangjie
public let tid: String
```

**功能：** 任务id，由系统自动生成且唯一。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### init(String, Config)

```cangjie
public init(tid: String, config: Config)
```

**功能：** 创建Task对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明  |
| :----- | :----- | :--- | :----- | :------- |
| tid    | String | 是   | -      | 任务id，由系统自动生成且唯一。。 |
| config | [Config](#class-config) | 是   | -      | 任务的配置信息 |

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
    let config = Config(
        Action.Download,
        "https://example.com/file.txt"
    )
    let task = Task(taskId, config)
    Hilog.info(0, "test", "成功初始化任务，任务ID: ${task.tid}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(EventCallbackType, ?CallbackObject)

```cangjie
public func off(event: EventCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅任务事件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名   | 类型  | 必填 | 默认值 | 说明 |
| :------- | :-----  | :--- | :----- | :----- |
| event    | [EventCallbackType](#enum-eventcallbacktype)| 是   | -      | 订阅的事件类型。<br>- 取值为Progress，表示任务进度。<br>- 取值为Completed，表示任务完成。<br>- 取值为Failed，表示任务失败。<br>- 取值为Pause，表示任务暂停。<br>- 取值为Resume，表示任务恢复。<br>- 取值为Remove，表示任务删除。<br>- 取值为Response，表示任务响应。 |
| callback | ?[CallbackObject](../arkinterop/cj-api-callback_invoke.md#class-callbackobject) | 否   | None   | **命名参数。** 需要取消订阅的回调函数。若无此参数，则取消订阅当前类型的所有回调函数。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

public class ProgressCallback <: Callback1Argument<Progress> {
    public ProgressCallback(let f: (Progress) -> Unit) {}

    public func invoke(err: ?BusinessException, arg: Progress): Unit {
        f(arg)
    }
}

try {
    let config = Config(
        Action.Download,
        "zipURL"
    )
    let task = create(Global.abilityContext, config)
    let callback = ProgressCallback({progress => Hilog.info(0, "test", "invoke success")})
    task.on(EventCallbackType.Pause, callback)
    task.off(EventCallbackType.Pause, callback: callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.toString()}")
}
```