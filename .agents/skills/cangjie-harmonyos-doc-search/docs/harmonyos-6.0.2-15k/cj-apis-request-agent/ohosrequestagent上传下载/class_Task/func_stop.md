### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止任务，可以停止正在运行/正在等待/正在重试的任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 13400003 | Task service ability error. |
  | 21900007 | Operation with wrong task state. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*
import ohos.base.BusinessException

let config = Config(
    action: Action.DOWNLOAD,
    url: "http://127.0.0.1",
)
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.stop()
} catch (e: BusinessException) {
    Hilog.error(0, "TaskStop", "${e}")
}
```