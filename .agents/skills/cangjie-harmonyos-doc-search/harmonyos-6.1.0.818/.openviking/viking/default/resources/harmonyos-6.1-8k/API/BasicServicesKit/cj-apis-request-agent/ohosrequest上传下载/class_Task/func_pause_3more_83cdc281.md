### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停任务，可以暂停正在等待/正在运行/正在重试的任务，已暂停的任务可被[resume](#resume)恢复。

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
    let config = Config(
        Action.Download,
        "zipURL"
    )
    let task = create(Global.abilityContext, config)
    task.pause()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.toString()}")
}
```

### func resume()

```cangjie
public func resume(): Unit
```

**功能：** 重新启动任务，可以恢复被暂停的任务。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
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
    let config = Config(
        Action.Download,
        "zipURL"
    )
    let task = create(Global.abilityContext, config)
    task.resume()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.toString()}")
}
```

### func start()

```cangjie
public func start(): Unit
```

**功能：** 启动一个任务。

以下状态的任务可以被启动：

1. 刚被request.agent.create接口创建的任务。
2. 使用request.agent.create接口创建的已经失败或者停止的下载任务。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)与[通用错误码说明文档](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
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
        "https://example.com/file.txt"
    )
    let task = create(context, config)

    task.start()
    Hilog.info(0, "test", "成功启动任务")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```