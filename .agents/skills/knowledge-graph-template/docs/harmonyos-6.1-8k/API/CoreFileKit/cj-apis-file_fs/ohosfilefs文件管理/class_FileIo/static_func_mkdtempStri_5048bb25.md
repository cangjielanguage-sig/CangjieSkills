### static func mkdtemp(String)

```cangjie
public static func mkdtemp(prefix: String): String
```

**功能：** 创建临时目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|prefix|String|是|-|指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回生成的唯一目录路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900001 | Operation not permitted. |
  | 13900002 | No such file or directory. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900015 | File exists. |
  | 13900018 | Not a directory. |
  | 13900020 | Invalid argument. |
  | 13900025 | No space left on device. |
  | 13900028 | Too many links. |
  | 13900030 | File name too long. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900041 | Quota exceeded. |
  | 13900042 | Unknown error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let res = FileIo.mkdtemp(pathDir + "/XXXXXX")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```