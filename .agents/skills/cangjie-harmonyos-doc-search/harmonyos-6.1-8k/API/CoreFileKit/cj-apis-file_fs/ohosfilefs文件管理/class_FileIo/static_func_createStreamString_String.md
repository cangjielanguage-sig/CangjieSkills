### static func createStream(String, String)

```cangjie
public static func createStream(path: String, mode: String): Stream
```

**功能：** 基于文件路径创建文件流。需要配合[Stream](#class-stream)中的close()函数关闭文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的应用沙箱路径。|
|mode|String|是|-|-&nbsp;r：打开只读文件，该文件必须存在。<br/>-&nbsp;r+：打开可读写的文件，该文件必须存在。<br/>-&nbsp;w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。<br/>-&nbsp;w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。<br/>-&nbsp;a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。<br/>-&nbsp;a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stream](#class-stream)|返回文件流的结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900006 | No such device or address. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900014 | Device or resource busy. |
  | 13900015 | File exists. |
  | 13900017 | No such device. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900022 | Too many open files. |
  | 13900023 | Text file busy. |
  | 13900024 | File too large. |
  | 13900025 | No space left on device. |
  | 13900027 | Read-only file system. |
  | 13900029 | Resource deadlock would occur. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900034 | Operation would block. |
  | 13900038 | Value too large for defined data type. |
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
    let stream = FileIo.createStream(filePath, "r+")
    Hilog.info(0, "test", "createStream succeed", "")
    stream.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```