### func on(EventCallbackType, Callback1Argument\<HttpResponse>)

```cangjie
public func on(event: EventCallbackType, callback: Callback1Argument<HttpResponse>): Unit
```

**功能：** 订阅任务响应头。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名   | 类型  | 必填 | 默认值 | 说明  |
| :------- | :----  | :--- | :----- | :----  |
| event    | [EventCallbackType](#enum-eventcallbacktype)  | 是   | -      | 订阅的事件类型。<br>- 取值为Response，表示任务响应。     |
| callback | [Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<HttpResponse> | 是   | -      | 发生相关的事件时触发该回调方法，返回任务响应头的数据结构。 |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.callback_invoke.*
import ohos.business_exception.BusinessException

public class ProgressCallback1 <: Callback1Argument<HttpResponse> {
    public ProgressCallback1(let f: (HttpResponse) -> Unit) {}

    public func invoke(err: ?BusinessException, arg: HttpResponse): Unit {
        f(arg)
    }
}

try {
    let config = Config(
        Action.Download,
        "zipURL"
    )
    let task = create(Global.abilityContext, config)
    let callback = ProgressCallback1({response => Hilog.info(0, "test", "invoke success")})
    task.on(EventCallbackType.Response, callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.toString()}")
}
```

### func on(EventCallbackType, Callback1Argument\<Progress>)

```cangjie
public func on(event: EventCallbackType, callback: Callback1Argument<Progress>): Unit
```

**功能：** 订阅任务进度的事件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名   | 类型 | 必填 | 默认值 | 说明 |
| :------- | :---  | :--- | :----- | :----  |
| event    | [EventCallbackType](#enum-eventcallbacktype) | 是   | -      | 订阅的事件类型。<br>- 取值为Progress，表示任务进度，任务进度有进展时触发该事件。 |
| callback | [Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[Progress](#class-progress)> | 是   | -      | 发生相关的事件时触发该回调方法，返回任务信息的数据结构。 |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

public class ProgressCallback2 <: Callback1Argument<Progress> {
    public ProgressCallback2(let f: (Progress) -> Unit) {}

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
    let callback = ProgressCallback2({progress => Hilog.info(0, "test", "invoke success")})
    task.on(EventCallbackType.Pause, callback)
    task.off(EventCallbackType.Pause, callback: callback)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.toString()}")
}
```