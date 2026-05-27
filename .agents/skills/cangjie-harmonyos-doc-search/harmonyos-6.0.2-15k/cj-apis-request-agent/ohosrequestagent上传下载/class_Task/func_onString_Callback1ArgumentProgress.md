### func on(String, Callback1Argument\<Progress>)

```cangjie
public func on(event: String, callback: Callback1Argument<Progress>): Unit
```

**功能：** 订阅任务的事件。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|订阅的事件类型。<br>- 取值为'progress'，表示任务进度。<br>- 取值为'completed'，表示任务完成。<br>- 取值为'failed'，表示任务失败。<br>- 取值为'pause'，表示任务暂停。<br>- 取值为'resume'，表示任务恢复。<br>- 取值为'remove'，表示任务删除。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Progress](#class-progress)>|是|-|发生相关的事件时触发该回调方法，返回任务信息的数据结构。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 21900005 | Operation with wrong task mode. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.BasicServicesKit.Action as RAction
import kit.PerformanceAnalysisKit.*
import ohos.base.BusinessException

// 此处代码可添加在依赖项定义中
class ProgressCallback <: Callback1Argument<Progress> {
    public init() {}
    public open func invoke(arg: Progress): Unit {
        Hilog.info(0, "request", "progress callback.")
    }
}

let fileSpec = FileSpec(
    path: "./taskOnTest.avi",
    filename: "taskOnTest.avi",
    mimeType: "application/octet-stream"
)
let attachments = ConfigDataType.FORMITEMS(
    [
        FormItem(
            name: "taskOnTest",
            value: FormItemValueType.FILE(fileSpec)
        )
    ]
)
let config = Config(
    action: RAction.UPLOAD,
    url: "http://127.0.0.1",
    title: "taskOnTest",
    mode: Mode.FOREGROUND,
    description: "Sample code for event listening",
    overwrite: false,
    method: "PUT",
    data: attachments,
    saveas: "./",
    network: Network.CELLULAR,
    metered: false,
    roaming: true,
    retry: true,
    redirect: true,
    index: 0,
    begins: 0,
    ends: -1,
    gauge: false,
    precise: false,
    token: "it is a secret"
)
let createOnCallback =ProgressCallback()
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.on("progress", createOnCallback)
} catch (e: BusinessException) {
    Hilog.error(0, "TaskCreate", e.toString())
}
```