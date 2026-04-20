### static func read(Int32, Array\<Byte>, ReadOptions)

```cangjie
public static func read(fd: Int32, buffer: Array<Byte>, options!: ReadOptions = ReadOptions()): Int64
```

**功能：** 从文件读取数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|
|buffer|Array\<Byte>|是|-|用于保存读取到的文件数据的缓冲区。|
|options|[ReadOptions](#class-readoptions)|否|ReadOptions()|**命名参数。** 支持如下选项：<br/>-&nbsp;offset，?Int64类型，表示期望读取文件的位置。默认从当前位置开始读。<br/>-&nbsp;length，?UIntNative类型，表示期望读取数据的长度。默认缓冲区长度。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回实际读取的数据长度（单位：字节）。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900010 | Try again. |
  | 13900013 | Bad address. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900034 | Operation would block. |
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
    let file = FileIo.open(filePath, mode: (OpenMode.READ_WRITE | OpenMode.CREATE))
    let buf = Array<Byte>(4096, repeat: 0)
    FileIo.read(file.fd, buf)
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func readLines(String, Options)

```cangjie
public static func readLines(filePath: String, options!: Options = Options()): ReaderIterator
```

**功能：** 逐行读取文件的文本内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filePath|String|是|-|文件的应用沙箱路径。|
|options|[Options](#class-options)|否|Options()|**命名参数。** 可选项。支持以下选项：<br/>-&nbsp;encoding，String类型，当数据是&nbsp;String&nbsp;类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"，仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|[ReaderIterator](#class-readeriterator)|返回文件读取迭代器。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900012 | Permission denied. |
  | 13900015 | File exists. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900022 | Too many open files. |
  | 13900025 | No space left on device. |
  | 13900027 | Read-only file system. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
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
    let options: Options = Options(encoding: "utf-8")
    let readerIterator = FileIo.readLines(filePath, options: options)
    var result = readerIterator.next()
    while (!result.done) {
        Hilog.info(0, "test", "content: ${result.value}", "")
        result = readerIterator.next()
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```