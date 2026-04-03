## class File

```cangjie
public class File {}
```

**功能：** 由open接口打开的File对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### prop fd

```cangjie
public prop fd: Int32
```

**功能：** 打开的文件描述符。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### prop name

```cangjie
public prop name: String
```

**功能：** 文件名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### prop path

```cangjie
public prop path: String
```

**功能：** 文件路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### func getParent()

```cangjie
public func getParent(): String
```

**功能：** 获取File对象对应文件父目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回父目录路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900005 | I/O error. |
  | 13900042 | Unknown error. |
  | 14300002 | Invalid URI. |

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
    let file = FileIo.open(filePath, mode: (OpenMode.READ_WRITE | OpenMode.CREATE))
    Hilog.info(0, "", "The parent path is: " + file.getParent())
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func tryLock(Bool)

```cangjie
public func tryLock(exclusive!: Bool = false): Unit
```

**功能：** 文件非阻塞式施加共享锁或独占锁。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|exclusive|Bool|否|false|**命名参数。** 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。|

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
    let file = FileIo.open(filePath, mode:(OpenMode.READ_WRITE | OpenMode.CREATE))
    file.tryLock(exclusive: true)
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```