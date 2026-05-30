### static func createRandomAccessFile(File, Int64)

```cangjie
public static func createRandomAccessFile(file: File, mode!: Int64 = 0): RandomAccessFile
```

**功能：** 基于文件路径或文件对象创建RandomAccessFile文件对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|[File](#class-file)|是|-|已打开的File对象。|
|mode|Int64|否|0| **命名参数。** 创建文件RandomAccessFile对象的[选项](#enum-openmode)，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建：<br/>-&nbsp;OpenMode.READ_ONLY(0o0)：只读创建。<br/>-&nbsp;OpenMode.WRITE_ONLY(0o1)：只写创建。<br/>-&nbsp;OpenMode.READ_WRITE(0o2)：读写创建。<br/>给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项：<br/>-&nbsp;OpenMode.CREATE(0o100)：若文件不存在，则创建文件。<br/>-&nbsp;OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且文件具有写权限，则将其长度裁剪为零。<br/>-&nbsp;OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。<br/>-&nbsp;OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续&nbsp;IO&nbsp;进行非阻塞操作。<br/>-&nbsp;OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。<br/>-&nbsp;OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。<br/>-&nbsp;OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[RandomAccessFile](#class-randomaccessfile)|返回RandomAccessFile文件对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

### static func createStream(String, String)

```cangjie
public static func createStream(path: String, mode: String): Stream
```

**功能：** 基于文件路径创建文件流。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

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

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let stream = FileFs.createStream(filePath, "r+")
Applog.info("createStream succeed")
stream.close()
```