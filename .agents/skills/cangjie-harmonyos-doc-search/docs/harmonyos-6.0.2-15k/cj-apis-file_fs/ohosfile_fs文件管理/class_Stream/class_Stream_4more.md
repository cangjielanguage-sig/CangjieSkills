## class Stream

```cangjie
public class Stream {}
```

**功能：** 文件流。在调用Stream的方法前，需要先通过[FileFs.createStream](#static-func-createstreamstring-string)方法或者[FileFs.fdopenStream](#static-func-fdopenstreamint32-string)来构建一个Stream实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### func close()

```cangjie
public func close(): Unit
```

**功能：** 同步关闭文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let stream = FileFs.createStream(filePath, "r+")
stream.close()
```

### func flush()

```cangjie
public func flush(): Unit
```

**功能：** 同步刷新文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let stream = FileFs.createStream(filePath, "r+")
stream.flush()
stream.close()
```

### func read(Array\<Byte>, ReadOptions)

```cangjie
public func read(arrayBuffer: Array<Byte>, options!: ReadOptions = ReadOptions()): Int64
```

**功能：** 以同步方法从流文件读取数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arrayBuffer|Array\<Byte>|是|-|用于读取文件的缓冲区。|
|options|[ReadOptions](#struct-readoptions)|否|ReadOptions()| **命名参数。** 支持如下选项：<br/>-&nbsp;length，UIntNative类型，表示期望读取数据的长度。可选，默认缓冲区长度。<br/>-&nbsp;offset，Int64类型，表示期望读取文件的位置。可选，默认从当前位置开始读。<br/>|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|实际读取的长度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let stream = FileFs.createStream(filePath, "r+")
let buf = Array<Byte>(4096, repeat: 0)
let num = stream.read(buf)
stream.close()
```