### static func lseek(Int32, Int64, WhenceType)

```cangjie
public static func lseek(fd: Int32, offset: Int64, whence!: WhenceType = SeekSet): Int64
```

**功能：** 调整文件偏置指针位置。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|文件描述符。|
|offset|Int64|是|-|相对偏移位置，单位为字节。|
|whence|[WhenceType](#enum-whencetype)|否|SeekSet|**命名参数。** 偏移指针相对位置类型。不指定则默认为文件起始位置处。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|当前文件偏移指针位置（相对于文件头的偏移量，单位为字节）。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900008 | Bad file descriptor. |
  | 13900020 | Invalid argument. |
  | 13900026 | Illegal seek. |
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
    let filePath = pathDir + "/test.txt"
    let file = FileIo.open(filePath, mode: OpenMode.CREATE)
    let offset = FileIo.lseek(file.fd, 5, whence: WhenceType.SeekSet)
    Hilog.info(0, "test", "The current offset is at ${offset.toString()}", "")
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func lstat(String)

```cangjie
public static func lstat(path: String): Stat
```

**功能：** 获取链接文件信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的应用沙箱路径path或URI。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stat](#class-stat)|返回Stat对象，表示文件的具体信息，详情见Stat。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900030 | File name too long. |
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
    let filePath = pathDir + "/linkToFile"
    let fileStat = FileIo.lstat(filePath)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```