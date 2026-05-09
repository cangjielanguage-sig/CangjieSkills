### static func copyFile(Int32, String, Int32)

```cangjie
public static func copyFile(src: Int32, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 复制文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|Int32|是|-|待复制文件的文件描述符。|
|dest|String|是|-|目标文件路径。|
|mode|Int32|否|0| **命名参数。** mode提供覆盖文件的选项，当前仅支持0，且默认为0。<br/>0：完全覆盖目标文件，未覆盖部分将被裁切掉。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900010 | Try again. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900030 | File name too long. |
  | 13900031 | Function not implemented. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900034 | Operation would block. |
  | 13900038 | Value too large for defined data type. |
  | 13900042 | Unknown error. |
  | 13900044 | Network is unreachable. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let srcPath = pathDir + "/srcDir/test.txt"
    let dstPath = pathDir + "/dstDir/test.txt"
    let srcFile = FileIo.open(srcPath)
    FileIo.copyFile(srcFile.fd, dstPath, mode: 0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func copyFile(Int32, Int32, Int32)

```cangjie
public static func copyFile(src: Int32, dest: Int32, mode!: Int32 = 0): Unit
```

**功能：** 复制文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|Int32|是|-|待复制文件的文件描述符。|
|dest|Int32|是|-|目标文件的文件描述符。|
|mode|Int32|否|0| **命名参数。** mode提供覆盖文件的选项，当前仅支持0，且默认为0。<br/>0：完全覆盖目标文件，未覆盖部分将被裁切掉。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900010 | Try again. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900030 | File name too long. |
  | 13900031 | Function not implemented. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900034 | Operation would block. |
  | 13900038 | Value too large for defined data type. |
  | 13900042 | Unknown error. |
  | 13900044 | Network is unreachable. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let srcPath = pathDir + "/srcDir/test.txt"
    let dstPath = pathDir + "/dstDir/test.txt"
    let srcFile = FileIo.open(srcPath)
    let dstFile = FileIo.open(dstPath)
    FileIo.copyFile(srcFile.fd, dstFile.fd, mode: 0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```