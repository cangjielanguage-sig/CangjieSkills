### static func readText(String, ReadTextOptions)

```cangjie
public static func readText(filePath: String, options!: ReadTextOptions = ReadTextOptions()): String
```

**功能：** 基于文本方式读取文件（即直接读取文件的文本内容）。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filePath|String|是|-|文件的应用沙箱路径。|
|options|[ReadTextOptions](#class-readtextoptions)|否|ReadTextOptions()|**命名参数。** 支持如下选项：<br/>-&nbsp;offset，Int64类型，表示期望读取文件的位置。可选，默认从初始位置开始读取。<br/>-&nbsp;length，Int64类型，表示期望读取数据的长度。可选，默认文件长度。<br/>-&nbsp;encoding，String类型，当数据是&nbsp;String&nbsp;类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"，仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回读取文件的内容。|

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
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900024 | File too large. |
  | 13900025 | No space left on device. |
  | 13900034 | Operation would block. |
  | 13900041 | Quota exceeded. |
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
    let filePath = pathDir + "/test.txt"
    let str = FileIo.readText(filePath)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func rename(String, String)

```cangjie
public static func rename(oldPath: String, newPath: String): Unit
```

**功能：** 重命名文件或目录。

> **说明：**
>
> 该接口不支持在分布式文件路径下操作。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|oldPath|String|是|-|文件的应用沙箱原路径。|
|newPath|String|是|-|文件的应用沙箱新路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900014 | Device or resource busy. |
  | 13900015 | File exists. |
  | 13900016 | Cross-device link. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900025 | No space left on device. |
  | 13900027 | Read-only file system. |
  | 13900028 | Too many links. |
  | 13900032 | Directory not empty. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900041 | Quota exceeded. |
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
    let srcFile = pathDir + "/test.txt"
    let dstFile = pathDir + "/new.txt"
    FileIo.rename(srcFile, dstFile)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```