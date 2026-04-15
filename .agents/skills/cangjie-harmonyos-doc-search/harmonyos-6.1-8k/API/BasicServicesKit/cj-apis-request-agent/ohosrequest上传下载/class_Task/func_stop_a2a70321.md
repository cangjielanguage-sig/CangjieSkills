### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止任务，可以停止正在运行/正在等待/正在重试的任务，已停止的任务可被[start](#func-start)恢复。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13400003 | Task service ability error. |
  | 21900007 | Operation with wrong task state. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let config = Config(
        Action.Download,
        "https://example.com/largefile.zip"
    )
    let task = create(context, config)

    task.start()
    task.stop()
    Hilog.info(0, "test", "成功停止任务")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```