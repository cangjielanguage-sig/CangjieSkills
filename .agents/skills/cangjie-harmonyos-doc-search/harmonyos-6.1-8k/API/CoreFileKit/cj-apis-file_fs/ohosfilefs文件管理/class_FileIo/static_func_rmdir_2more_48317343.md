### static func rmdir(String)

```cangjie
public static func rmdir(path: String): Unit
```

**功能：** 删除目录及其所有子目录和文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|目录的应用沙箱路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900014 | Device or resource busy. |
  | 13900018 | Not a directory. |
  | 13900020 | Invalid argument. |
  | 13900027 | Read-only file system. |
  | 13900030 | File name too long. |
  | 13900032 | Directory not empty. |
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
    let dirPath = pathDir + "/testDir"
    FileIo.rmdir(dirPath)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func stat(Int32)

```cangjie
public static func stat(file: Int32): Stat
```

**功能：** 获取文件或目录详细属性信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|Int32|是|-|已打开的文件描述符fd。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stat](#class-stat)|表示文件或目录的具体信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900030 | File name too long. |
  | 13900031 | Function not implemented. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900038 | Value too large for defined data type. |
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
    let dirPath = pathDir + "/testDir"
    let file = FileIo.open(dirPath)
    FileIo.stat(file.fd)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```