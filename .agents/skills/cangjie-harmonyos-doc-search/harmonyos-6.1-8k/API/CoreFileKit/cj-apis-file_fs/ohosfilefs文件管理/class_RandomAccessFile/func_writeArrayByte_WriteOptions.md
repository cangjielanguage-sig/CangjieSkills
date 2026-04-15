### func write(Array\<Byte>, WriteOptions)

```cangjie
public func write(buffer: Array<Byte>, options!: WriteOptions = WriteOptions()): Int64
```

**功能：** 将数据写入文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buffer|Array\<Byte>|是|-|待写入文件的数据，可来自缓冲区。|
|options|[WriteOptions](#class-writeoptions)|否|WriteOptions()|**命名参数。** 支持如下选项：<br>- length，?UIntNative类型，表示期望写入数据的长度。默认缓冲区长度。<br>- offset，?Int64类型，表示期望写入文件的位置。可选，默认从当前位置开始写。<br>- encoding，String类型，当数据是String类型时有效，表示数据的编码方式，默认"utf-8"。仅支持"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|实际写入的长度。|

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
  | 13900020 | Invalid argument. |
  | 13900024 | File too large. |
  | 13900025 | No space left on device. |
  | 13900034 | Operation would block. |
  | 13900041 | Quota exceeded. |
  | 13900042 | Unknown error. |

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
    let option = WriteOptions(length: 5, offset: 5)
    let arr: Array<UInt8> = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
    let bytesWritten = randomAccessFile.write(arr, options: option)
    randomAccessFile.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```