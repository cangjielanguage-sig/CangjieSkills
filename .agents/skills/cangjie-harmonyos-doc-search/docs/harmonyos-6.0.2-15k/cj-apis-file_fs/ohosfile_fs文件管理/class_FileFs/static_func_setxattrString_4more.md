### static func setxattr(String, String, String)

```cangjie
public static func setxattr(path: String, key: String, value: String): Unit
```

**功能：** 设置文件或目录的扩展属性。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件或目录的应用沙箱路径。|
|key|String|是|-|扩展属性的key。仅支持前缀为"user."的字符串，且长度需小于256字节。|
|value|String|是|-|扩展属性的value。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  |错误码ID|错误信息|
  |:----|:----|
  |13900002|No such file or directory|
  |13900011|Out of memory|
  |13900012|Permission denied|
  |13900020|Invalid argument|
  |13900025|No space left on device|
  |13900031|Function not implemented|
  |13900038|Value too large for defined data type|
  |13900041|Quota exceeded|
  |13900042|Unknown error|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let attrKey = "user.comment"
let attrValue = "Test file."

FileFs.setxattr(filePath, attrKey, attrValue)
```

### static func stat(Int32)

```cangjie
public static func stat(file: Int32): Stat
```

**功能：** 获取文件详细属性信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|Int32|是|-|已打开的文件描述符fd。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stat](#class-stat)|表示文件的具体信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

### static func stat(String)

```cangjie
public static func stat(file: String): Stat
```

**功能：** 获取文件详细属性信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|String|是|-|文件应用沙箱路径path。|

**返回值：**

|类型|说明|
|:----|:----|
|[Stat](#class-stat)|表示文件的具体信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

### static func truncate(String, Int64)

```cangjie
public static func truncate(file: String, len!: Int64 = 0): Unit
```

**功能：** 以同步方法截断文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|String|是|-|文件的应用沙箱路径。|
|len|Int64|否|0| **命名参数。** 文件截断后的长度，以字节为单位。默认为0。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let len: Int64 = 5
FileFs.truncate(filePath, len: len)
```