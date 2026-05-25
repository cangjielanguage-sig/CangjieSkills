### static func fsync(Int32)

```cangjie
public static func fsync(fd: Int32): Unit
```

**功能：** 以同步方法同步文件数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath)
FileFs.fsync(file.fd)
FileFs.close(file)
```

### static func getxattr(String, String)

```cangjie
public static func getxattr(path: String, key: String): String
```

**功能：** 获取文件或目录的扩展属性。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件或目录的应用沙箱路径。|
|key|String|是|-|扩展属性的key。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回扩展属性的value。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  |错误码ID|错误信息|
  |:----|:----|
  |13900002|No such file or directory|
  |13900007|Arg list too long|
  |13900012|Permission denied|
  |13900031|Function not implemented|
  |13900037|No data available|
  |13900038|Value too large for defined data type|
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

let attrValue = FileFs.getxattr(filePath, attrKey)
Applog.info("Get extended attribute succeed, the value is: " + attrValue)
```