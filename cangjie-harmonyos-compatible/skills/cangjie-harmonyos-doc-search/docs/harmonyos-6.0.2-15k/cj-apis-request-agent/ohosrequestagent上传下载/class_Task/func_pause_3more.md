### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停任务，可以暂停正在等待/正在运行/正在重试的后台任务。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 13400003 | Task service ability error. |
  | 21900005 | Operation with wrong task mode. |
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
    overwrite: true
)
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.pause()
} catch (e: BusinessException) {
    Hilog.error(0, "TaskPause", "${e}")
}
```

### func resume()

```cangjie
public func resume(): Unit
```

**功能：** 重新启动任务，可以恢复暂停的后台任务。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[上传下载错误码](../../errorcodes/cj-errorcode-request.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 13400003 | Task service ability error. |
  | 21900005 | Operation with wrong task mode. |
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
    overwrite: true
)
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.resume()
} catch (e: BusinessException) {
    Hilog.error(0, "TaskResume", "${e}")
}
```

### func start()

```cangjie
public func start(): Unit
```

**功能：** 启动任务，无法启动已初始化的任务。可以启动一个已失败或已停止的下载任务，从上次的进度开始续传。

**需要权限：** ohos.permission.INTERNET

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
    overwrite: true
)
try {
    let task = create(Global.getStageContext(), config) // 需获取Context应用上下文，详见本文使用说明
    task.start()
} catch (e: BusinessException) {
    Hilog.error(0, "TaskStart", e.toString())
}
```