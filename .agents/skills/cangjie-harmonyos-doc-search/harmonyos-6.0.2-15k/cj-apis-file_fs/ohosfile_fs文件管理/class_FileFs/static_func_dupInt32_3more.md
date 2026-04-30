### static func dup(Int32)

```cangjie
public static func dup(fd: Int32): File
```

**功能：** 将文件描述符转化为File。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|文件描述符。|

**返回值：**

|类型|说明|
|:----|:----|
|[File](#class-file)|打开的File对象。|

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
let file1 = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
let fd = file1.fd
let file2 = FileFs.dup(fd)
Applog.info("The name of the file2 is " + file2.name)
FileFs.close(file1)
FileFs.close(file2)
```

### static func fdatasync(Int32)

```cangjie
public static func fdatasync(fd: Int32): Unit
```

**功能：** 以同步方法实现文件内容数据同步。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath)
FileFs.fdatasync(file.fd)
FileFs.close(file)
```

### static func fdopenStream(Int32, String)

```cangjie
public static func fdopenStream(fd: Int32, mode: String): Stream
```

**功能：** 以同步方法基于文件描述符打开文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|
|mode|String|是|-|-&nbsp;r：打开只读文件，该文件必须存在。<br/>-&nbsp;r+：打开可读写的文件，该文件必须存在。<br/>-&nbsp;w：打开只写文件，若文件存在原文件内容将被覆盖。<br/>-&nbsp;w+：打开可读写文件，若文件存在原文件内容将被覆盖。<br/>-&nbsp;a：以附加的方式打开只写文件，写入的数据会被加到文件尾，即文件原先的内容会被保留。<br/>-&nbsp;a+：以附加方式打开可读写的文件，写入的数据会被加到文件尾后，即文件原先的内容会被保留。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stream](#class-stream)|返回文件流的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode: (READ_ONLY.mode | CREATE.mode))
let stream = FileFs.fdopenStream(file.fd, "r+")
FileFs.close(file)
stream.close()
```