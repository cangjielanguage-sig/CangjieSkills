### func unlock()

```cangjie
public func unlock(): Unit
```

**功能：** 解锁文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900004 | Interrupted system call. |
  | 13900008 | Bad file descriptor. |
  | 13900020 | Invalid argument. |
  | 13900034 | Operation would block. |
  | 13900042 | Unknown error. |
  | 13900043 | No record locks available. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"
    let file = FileIo.open(filePath, mode: (OpenMode.READ_WRITE | OpenMode.CREATE))
    file.tryLock(exclusive: true)
    file.unlock()
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```