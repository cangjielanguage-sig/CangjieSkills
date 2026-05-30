## class FileFs

```cangjie
public class FileFs {}
```

**功能：** 文件管理工具类，提供基础文件操作能力。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### static func access(String)

```cangjie
public static func access(path: String): Bool
```

**功能：** 检查文件是否存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件应用沙箱路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true，表示文件存在；返回false，表示文件不存在。|

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
let res = FileFs.access(filePath)
if (res) {
    Applog.info("file exists")
} else {
    Applog.info("file not exists")
}
```

### static func access(String, AccessModeType)

```cangjie
public static func access(path: String, mode: AccessModeType): Bool
```

**功能：** 检查文件是否存在，或校验操作权限。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件或目录应用沙箱路径。|
|mode|[AccessModeType](#enum-accessmodetype)|是|-|文件或目录校验的权限。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true，表示文件存在；返回false，表示文件不存在。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  |错误码ID|错误信息|
  |:----|:----|
  |13900002|No such file or directory|
  |13900005|I/O error|
  |13900008|Bad file descriptor|
  |13900011|Out of memory|
  |13900012|Permission denied|
  |13900013|Bad address|
  |13900018|Not a directory|
  |13900020|Invalid argument|
  |13900023|Text file busy|
  |13900030|Filename too Long|
  |13900033|Too many symbolic links encountered|
  |13900042|Unknown error|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*
import kit.UIKit.BusinessException

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
try {
    let res = FileFs.access(filePath, AccessModeType.WRITE)
    if (res) {
        Applog.info("file exists")
    } else {
        Applog.info("file not exists")
    }
} catch (e: BusinessException) {
    AppLog.error("access failed with error message: ${e.message}, error code: ${e.code}")
}
```