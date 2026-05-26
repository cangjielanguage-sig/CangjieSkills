### static func read(Int32, Array\<Byte>, ReadOptions)

```cangjie
public static func read(fd: Int32, buffer: Array<Byte>, options!: ReadOptions = ReadOptions()): Int64
```

**功能：** 以同步方法从文件读取数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|
|buffer|Array\<Byte>|是|-|用于保存读取到的文件数据的缓冲区。|
|options|[ReadOptions](#struct-readoptions)|否|ReadOptions()| **命名参数。** 支持如下选项：<br/>-&nbsp;offset，Int64类型，表示期望读取文件的位置。默认从当前位置开始读。<br/>-&nbsp;length，UIntNative类型，表示期望读取数据的长度。默认缓冲区长度。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回实际读取的长度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
let buf = Array<Byte>(4096, repeat: 0)
FileFs.read(file.fd, buf)
FileFs.close(file)
```

### static func readLines(String, Options)

```cangjie
public static func readLines(filePath: String, options!: Options = Options()): ReaderIterator
```

**功能：** 以同步方式逐行读取文件文本内容。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filePath|String|是|-|文件的应用沙箱路径。|
|options|[Options](#struct-options)|否|Options()| **命名参数。** 可选项。支持以下选项：<br/>-&nbsp;encoding，String类型，当数据是&nbsp;String&nbsp;类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"，仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|[ReaderIterator](#class-readeriterator)|返回文件读取迭代器。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let options: Options = Options(encoding: "utf-8")
let readerIterator = FileFs.readLines(filePath, options: options)
var result = readerIterator.next()
while (!result.done) {
  Applog.info("content: " + result.value)
  result = readerIterator.next()
}
```