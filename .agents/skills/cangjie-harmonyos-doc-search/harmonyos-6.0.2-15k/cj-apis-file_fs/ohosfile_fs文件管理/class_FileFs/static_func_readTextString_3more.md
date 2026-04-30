### static func readText(String, ReadTextOptions)

```cangjie
public static func readText(filePath: String, option!: ReadTextOptions = ReadTextOptions()): String
```

**功能：** 以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filePath|String|是|-|文件的应用沙箱路径。|
|option|[ReadTextOptions](#struct-readtextoptions)|否|ReadTextOptions()| **命名参数。** 支持如下选项：<br/>-&nbsp;offset，Int64类型，表示期望读取文件的位置。可选，默认从初始位置开始读取。<br/>-&nbsp;length，Int64类型，表示期望读取数据的长度。可选，默认文件长度。<br/>-&nbsp;encoding，String类型，当数据是&nbsp;String&nbsp;类型时有效，表示数据的编码方式，默认&nbsp;"utf-8"，仅支持&nbsp;"utf-8"。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回读取文件的内容。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let str = FileFs.readText(filePath)
```

### static func rename(String, String)

```cangjie
public static func rename(oldPath: String, newPath: String): Unit
```

**功能：** 重命名文件或文件夹。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|oldPath|String|是|-|文件的应用沙箱原路径。|
|newPath|String|是|-|文件的应用沙箱新路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let srcFile = pathDir + "/test.txt"
let dstFile = pathDir + "/new.txt"
FileFs.rename(srcFile, dstFile)
```

### static func rmdir(String)

```cangjie
public static func rmdir(path: String): Unit
```

**功能：** 删除目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|目录的应用沙箱路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let dirPath = pathDir + "/testDir"
FileFs.rmdir(dirPath)
```