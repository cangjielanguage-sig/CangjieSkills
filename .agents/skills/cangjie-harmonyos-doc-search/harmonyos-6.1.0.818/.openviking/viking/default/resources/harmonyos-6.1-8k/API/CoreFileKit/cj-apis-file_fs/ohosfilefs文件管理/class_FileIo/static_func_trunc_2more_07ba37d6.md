### static func truncate(Int32, Int64)

```cangjie
public static func truncate(file: Int32, len!: Int64 = 0): Unit
```

**功能：** 截断文件内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|Int32|是|-|已打开的文件描述符fd。|
|len|Int64|否|0|**命名参数。** 文件截断后的长度（单位：字节）。默认为0。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900023 | Text file busy. |
  | 13900024 | File too large. |
  | 13900027 | Read-only file system. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900042 | Unknown error. |

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
    let len: Int64 = 5
    let file  = FileIo.open(filePath, mode: OpenMode.READ_WRITE)
    FileIo.truncate(file.fd, len: len)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func unlink(String)

```cangjie
public static func unlink(path: String): Unit
```

**功能：** 删除文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的应用沙箱路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900014 | Device or resource busy. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900027 | Read-only file system. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900042 | Unknown error. |

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
    FileIo.unlink(filePath)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```