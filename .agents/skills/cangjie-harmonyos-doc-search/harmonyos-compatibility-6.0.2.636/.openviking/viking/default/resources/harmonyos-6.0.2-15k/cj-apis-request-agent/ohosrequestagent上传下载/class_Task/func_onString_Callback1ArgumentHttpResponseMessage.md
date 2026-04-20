### func on(String, Callback1Argument\<HttpResponseMessage>)

```cangjie
public func on(event: String, callback: Callback1Argument<HttpResponseMessage>): Unit
```

**功能：** 订阅任务响应头。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|订阅的事件类型。<br>- 取值为'response'，表示任务响应。 |
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[HttpResponseMessage](#class-httpresponsemessage)>|是|-|发生相关的事件时触发该回调方法，返回任务响应头的数据结构。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Missing mandatory parameters 2. Incorrect parameter type 3. Parameter verification failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import kit.BasicServicesKit.Action as RAction
import ohos.base.BusinessException

// 此处代码可添加在依赖项定义中
class ResponseCallback <: Callback1Argument<HttpResponseMessage> {
    public init() {}
    public open func invoke(arg: HttpResponseMessage): Unit {
        Hilog.info(0, "request", "response callback.")
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
let responseOnCallback = ResponseCallback()
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.on("response", responseOnCallback)
} catch (e: BusinessException) {
    Hilog.error(0, "TaskCreate", e.toString())
}
```