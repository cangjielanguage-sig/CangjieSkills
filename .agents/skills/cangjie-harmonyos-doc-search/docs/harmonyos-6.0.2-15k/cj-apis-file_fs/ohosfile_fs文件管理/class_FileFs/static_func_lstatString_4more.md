### static func lstat(String)

```cangjie
public static func lstat(path: String): Stat
```

**功能：** 以同步方法获取链接文件信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的应用沙箱路径。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stat](#class-stat)|表示文件的具体信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/linkToFile"
let fileStat = FileFs.lstat(filePath)
```

### static func mkdir(String)

```cangjie
public static func mkdir(path: String): Unit
```

**功能：** 创建目录。

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
let dirPath = pathDir + "/testDir1/testDir2/testDir3"
FileFs.mkdir(dirPath)
```

### static func mkdir(String, Bool)

```cangjie
public static func mkdir(path: String, recursion: Bool): Unit
```

**功能：** 创建目录。当recursion指定为true，可多层级创建目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|目录的应用沙箱路径。|
|recursion|Bool|是|-|是否多层级创建目录。`recursion`指定为`true`时，可多层级创建目录。`recursion`指定为`false`时，仅可创建单层目录。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let dirPath = pathDir + "/testDir1/testDir2/testDir3"
FileFs.mkdir(dirPath, true)
```

### static func mkdtemp(String)

```cangjie
public static func mkdtemp(prefix: String): String
```

**功能：** 以同步的方法创建临时目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|prefix|String|是|-|指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。|

**返回值：**

|类型|说明|
|:----|:----|
|String|产生的唯一目录路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let res = FileFs.mkdtemp(pathDir + "/XXXXXX")
```