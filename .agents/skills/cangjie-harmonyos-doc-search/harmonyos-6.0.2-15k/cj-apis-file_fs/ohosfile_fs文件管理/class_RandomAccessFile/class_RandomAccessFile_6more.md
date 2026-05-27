## class RandomAccessFile

```cangjie
public class RandomAccessFile {}
```

**功能：** 随机读写文件流。在调用RandomAccessFile的方法前，需要先通过[createRandomAccessFile](#static-func-createrandomaccessfilefile-int64)方法来构建一个RandomAccessFile实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### prop fd

```cangjie
public prop fd: Int32
```

**功能：** 打开的文件描述符。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop filePointer

```cangjie
public prop filePointer: Int64
```

**功能：** RandomAccessFile对象的偏置指针。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### func close()

```cangjie
public func close(): Unit
```

**功能：** 同步关闭RandomAccessFile对象。

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
let randomAccessFile = FileFs.createRandomAccessFile(filePath, mode: (CREATE.mode | READ_WRITE.mode))
randomAccessFile.close()
```

### func read(Array\<Byte>, ReadOptions)

```cangjie
public func read(buffer: Array<Byte>, readOptions!: ReadOptions = ReadOptions()): Int64
```

**功能：** 以同步方法从文件读取数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buffer|Array\<Byte>|是|-|用于读取文件的缓冲区。|
|readOptions|[ReadOptions](#struct-readoptions)|否|ReadOptions()| **命名参数。** 支持如下选项：<br>- length，?UIntNative类型，表示期望读取数据的长度。可选，默认缓冲区长度。<br>- offset，?Int64类型，表示期望读取文件的位置。可选，默认从当前位置开始读。|

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
let file = FileFs.open(filePath, mode: (CREATE.mode | READ_WRITE.mode))
let randomAccessFile = FileFs.createRandomAccessFile(file)
let length: Int64 = 4096
let arrayBuffer = Array<Byte>(length, repeat: 0)
let readLength = randomAccessFile.read(arrayBuffer)
randomAccessFile.close()
FileFs.close(file)
```

### func setFilePointer(Int64)

```cangjie
public func setFilePointer(fp: Int64): Unit
```

**功能：** 设置文件偏置指针。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fp|Int64|是|-|RandomAccessFile对象的偏置指针。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let randomAccessFile = FileFs.createRandomAccessFile(filePath, mode: (CREATE.mode | READ_WRITE.mode))
randomAccessFile.setFilePointer(1)
randomAccessFile.close()
```