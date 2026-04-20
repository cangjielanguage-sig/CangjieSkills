## class Stream

```cangjie
public class Stream {}
```

**功能：** 文件流。在调用Stream的方法前，需要先通过[FileIo.createStream](#static-func-createstreamstring-string)方法或者[FileIo.fdopenStream](#static-func-fdopenstreamint32-string)来构建一个Stream实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900025 | No space left on device. |
  | 13900041 | Quota exceeded. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let stream = FileIo.createStream(filePath, "r+")
    stream.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func flush()

```cangjie
public func flush(): Unit
```

**功能：** 刷新文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900010 | Try again. |
  | 13900013 | Bad address. |
  | 13900020 | Invalid argument. |
  | 13900024 | File too large. |
  | 13900025 | No space left on device. |
  | 13900034 | Operation would block. |
  | 13900041 | Quota exceeded. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let stream = FileIo.createStream(filePath, "r+")
    stream.flush()
    stream.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```