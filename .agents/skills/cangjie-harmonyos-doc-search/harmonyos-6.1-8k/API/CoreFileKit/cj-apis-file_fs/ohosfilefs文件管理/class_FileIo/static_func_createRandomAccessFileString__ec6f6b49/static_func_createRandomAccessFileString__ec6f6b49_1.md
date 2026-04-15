### static func createRandomAccessFile(String, Int64, RandomAccessFileOptions)

```cangjie
public static func createRandomAccessFile(file: String, mode!: Int64 = OpenMode.READ_ONLY,
    options!: RandomAccessFileOptions = RandomAccessFileOptions()): RandomAccessFile
```

**功能：** 基于文件路径创建RandomAccessFile文件对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|String|是|-|文件的应用沙箱路径。|
|mode|Int64|否|OpenMode.READ_ONLY|**命名参数。** 创建文件RandomAccessFile对象的[选项](#class-openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：<br/>-&nbsp;OpenMode.READ_ONLY(0o0)：只读创建。<br/>-&nbsp;OpenMode.WRITE_ONLY(0o1)：只写创建。<br/>-&nbsp;OpenMode.READ_WRITE(0o2)：读写创建。<br/>给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：<br/>-&nbsp;OpenMode.CREATE(0o100)：若文件不存在，则创建文件。<br/>-&nbsp;OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且文件具有写权限，则将其长度裁剪为零。<br/>-&nbsp;OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。<br/>-&nbsp;OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续&nbsp;IO&nbsp;进行非阻塞操作。<br/>-&nbsp;OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。<br/>-&nbsp;OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。<br/>-&nbsp;OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。|
|options|[RandomAccessFileOptions](#class-randomaccessfileoptions)|否|RandomAccessFileOptions()|**命名参数。** 支持如下选项：<br/>- start，Option\<Int64>类型，表示期望读取文件的位置。可选，默认从当前位置开始读。<br/>- end，Option\<Int64>类型，表示期望读取结束的位置。可选，默认文件末尾。|

**返回值：**

|类型|说明|
|:----|:----|
|[RandomAccessFile](#class-randomaccessfile)|返回RandomAccessFile文件对象。|

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
    let file = FileIo.open(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    FileIo.write(file.fd, "hello world")
    FileIo.fdatasync(file.fd)
    let randomAccessFile = FileIo.createRandomAccessFile(filePath)
    randomAccessFile.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```