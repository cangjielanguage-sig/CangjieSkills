# ohos.request.agent（上传下载）

request部件主要给应用提供上传下载文件、后台传输代理的基础能力。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func create(StageContext, Config)

```cangjie
public func create(context: StageContext, config: Config): Task
```

**功能：** 创建要上传或下载的任务，并将其排入队列。每个应用最多支持创建10个未完成的任务。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|基于应用程序的上下文。 |
|config|[Config](#class-config)|是|-|上传/下载任务的配置信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[Task](#class-task)|返回一个Task对象，里面包括任务id和任务的配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)与[通用错误码说明文档](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 201 | The permissions check fails.|
  | 401 | The parameters check fails.Possible causes: 1. Missing mandatory parameters 2. Incorrect parameter type 3. Parameter verification failed.|
  | 13400001 | Invalid file or file system error.|
  | 13400003 | Task service ability error. |
  | 21900004 | The application task queue is full. |
  | 21900005 | Operation with wrong task mode. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import kit.BasicServicesKit.Action as RAction
import ohos.base.*

let fileSpec = FileSpec(
    path: "./createTest.avi",
    filename: "createTest.avi",
    mimeType: "application/octet-stream"
)
let attachments = ConfigDataTypeFORMITEMS(
    [
        FormItem(
            name: "createTest",
            value: FormItemValueType.FILE(fileSpec)
        )
    ]
)
let config = Config(
    action: RAction.UPLOAD,
    url: "http://127.0.0.1",
    title: "createTest",
    mode: Mode.FOREGROUND,
    description: "Sample code for creating task",
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
try {
    let task = create(Global.getStageContext(), config)  // 需获取Context应用上下文，详见本文使用说明
} catch (e: BusinessException) {
    Hilog.error(0, "TaskCreate", e.toString())
}
```