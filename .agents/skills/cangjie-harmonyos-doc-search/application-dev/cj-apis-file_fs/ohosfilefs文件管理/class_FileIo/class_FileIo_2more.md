## class FileIo

```cangjie
public class FileIo {}
```

**功能：** 提供文件基础操作的能力。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static func access(String, AccessModeType, AccessFlagType)

```cangjie
public static func access(path: String, mode!: AccessModeType = AccessModeType.Exist,
    flag!: AccessFlagType = AccessFlagType.Local): Bool
```

**功能：**  检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件或目录应用沙箱路径。|
|mode|[AccessModeType](#enum-accessmodetype)|否|AccessModeType.Exist|**命名参数。** 文件或目录校验的权限。|
|flag|[AccessFlagType](#enum-accessflagtype)|否|AccessFlagType.Local|**命名参数。** 文件或目录校验的位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回布尔值。返回true，表示文件或目录在本地且校验权限存在；返回false，表示文件或目录不存在或者文件或目录在云端或其他分布式设备上。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900018 | Not a directory. |
  | 13900020 | Invalid argument. |
  | 13900023 | Text file busy. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
try {
    let res = FileIo.access(filePath, mode: AccessModeType.Write, flag: AccessFlagType.Local)
    if (res) {
        Hilog.info(0, "test", "file exists", "")
    } else {
        Hilog.info(0, "test", "file not exists", "")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "test", "access failed with error message: ${e.message}, error code: ${e.code}", "")
}
```