### static func access(String, AccessModeType, AccessFlagType)

```cangjie
public static func access(path: String, mode: AccessModeType, flag: AccessFlagType): Bool
```

**功能：** 检查文件是否存在，或校验操作权限。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件或目录应用沙箱路径。|
|mode|[AccessModeType](#enum-accessmodetype)|是|-|文件或目录校验的权限。|
|flag|[AccessFlagType](#enum-accessflagtype)|是|-|文件或目录校验的位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true，表示文件在本地且校验权限存在；返回false，表示文件不存在或者文件在云端或其他分布式设备上。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

  |错误码ID|错误信息|
  |:----|:----|
  |13900005|I/O error|
  |13900011|Out of memory|
  |13900012|Permission denied|
  |13900013|Bad address|
  |13900018|Not a directory|
  |13900020|Invalid argument|
  |13900023|Text file busy|
  |13900030|Filename too Long|
  |13900033|Too many symbolic links encountered|

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
    let res = FileFs.access(filePath, AccessModeType.READ, AccessFlagType.LOCAL)
    if (res) {
        Applog.info("file exists")
    } else {
        Applog.info("file not exists")
    }
} catch (e: BusinessException) {
    AppLog.error("access failed with error message: ${e.message}, error code: ${e.code}")
}
```

### static func close(Int32)

```cangjie
public static func close(file: Int32): Unit
```

**功能：** 以同步方法关闭文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|Int32|是|-|已打开的File对象，关闭后file对象不再具备实际意义，不可再用于进行读写等操作。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath)
FileFs.close(file.fd)
```

### static func close(File)

```cangjie
public static func close(file: File): Unit
```

**功能：** 以同步方法关闭文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|file|[File](#class-file)|是|-|已打开的File对象，关闭后file对象不再具备实际意义，不可再用于进行读写等操作。|

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
FileFs.close(file)
```