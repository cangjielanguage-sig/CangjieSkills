### func write(String, WriteOptions)

```cangjie
public func write(buffer: String, options!: WriteOptions = WriteOptions()): Int64
```

**功能：** 将数据写入流文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buffer|String|是|-|待写入文件的数据。|
|options|[WriteOptions](#struct-writeoptions)|否|WriteOptions()| **命名参数。** 支持如下选项：<br/>-&nbsp;length，UIntNative类型，表示期望写入数据的长度。默认缓冲区长度。<br/>-&nbsp;offset，Int64类型，表示期望写入文件的位置。可选，默认从当前位置开始写。<br/>-&nbsp;encoding，String类型，当数据是String类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"。仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|实际写入的长度。|

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
let num = stream.write("hello, world")
stream.close()
```

### func write(Array\<Byte>, WriteOptions)

```cangjie
public func write(buffer: Array<Byte>, options!: WriteOptions = WriteOptions()): Int64
```

**功能：** 将数据写入流文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buffer|Array\<Byte>|是|-|待写入文件的数据。|
|options|[WriteOptions](#struct-writeoptions)|否|WriteOptions()| **命名参数。** 支持如下选项：<br/>-&nbsp;length，?UIntNative类型，表示期望写入数据的长度。默认缓冲区长度。<br/>-&nbsp;offset，?Int64类型，表示期望写入文件的位置。可选，默认从当前位置开始写。<br/>-&nbsp;encoding，String类型，当数据是String类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"。仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|实际写入的长度。|

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
let arr: Array<UInt8> = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
let num = stream.write(arr)
stream.close()
```