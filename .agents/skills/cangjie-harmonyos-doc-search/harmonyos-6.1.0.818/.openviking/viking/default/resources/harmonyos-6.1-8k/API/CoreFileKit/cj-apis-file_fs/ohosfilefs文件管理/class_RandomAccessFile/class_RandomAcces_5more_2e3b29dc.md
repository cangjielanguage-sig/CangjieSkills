## class RandomAccessFile

```cangjie
public class RandomAccessFile {}
```

**功能：** 随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile方法来构建一个RandomAccessFile实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### prop fd

```cangjie
public prop fd: Int32
```

**功能：** 打开的文件描述符。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### prop filePointer

```cangjie
public prop filePointer: Int64
```

**功能：** RandomAccessFile对象的偏置指针。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭RandomAccessFile对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let randomAccessFile = FileIo.createRandomAccessFile(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    randomAccessFile.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func read(Array\<Byte>, ReadOptions)

```cangjie
public func read(buffer: Array<Byte>, options!: ReadOptions = ReadOptions()): Int64
```

**功能：** 从文件读取数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buffer|Array\<Byte>|是|-|用于读取文件的缓冲区。|
|options|[ReadOptions](#class-readoptions)|否|ReadOptions()|**命名参数。** 支持如下选项：<br>- length，?UIntNative类型，表示期望读取数据的长度。可选，默认缓冲区长度。<br>- offset，?Int64类型，表示期望读取文件的位置。可选，默认从当前位置开始读。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|实际读取的长度。|

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

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let file = FileIo.open(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    let randomAccessFile = FileIo.createRandomAccessFile(file)
    let length: Int64 = 4096
    let arrayBuffer = Array<Byte>(length, repeat: 0)
    let readLength = randomAccessFile.read(arrayBuffer)
    randomAccessFile.close()
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```