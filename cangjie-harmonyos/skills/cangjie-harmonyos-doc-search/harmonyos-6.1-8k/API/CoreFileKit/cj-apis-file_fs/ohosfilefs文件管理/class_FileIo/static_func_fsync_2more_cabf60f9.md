### static func fsync(Int32)

```cangjie
public static func fsync(fd: Int32): Unit
```

**功能：** 将文件系统缓存数据写入磁盘。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|已打开的文件描述符。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900020 | Invalid argument. |
  | 13900025 | No space left on device. |
  | 13900027 | Read-only file system. |
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
    let filePath = pathDir + "/test.txt"
    let file = FileIo.open(filePath)
    FileIo.fsync(file.fd)
    FileIo.close(file)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func listFile(String, ListFileOptions)

```cangjie
public static func listFile(path: String, options!: ListFileOptions = ListFileOptions()): Array<String>
```

**功能：** 列出当前目录下所有文件名和目录名。支持过滤。

可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|目录的应用沙箱路径。|
|options|[ListFileOptions](#class-listfileoptions)|否|ListFileOptions()|**命名参数。** 文件过滤选项。默认不进行过滤。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回文件名数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900008 | Bad file descriptor. |
  | 13900011 | Out of memory. |
  | 13900018 | Not a directory. |
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
    let filter = Filter(suffix: [".png", ".jpg", ".jpeg"], displayName: ["*abc", "efg*"])
    let listFileOptions = ListFileOptions(recursion: false, listNum: 0, filter: filter)
    let filenames = FileIo.listFile(pathDir, options: listFileOptions)
    for (name in filenames) {
        Hilog.info(0, "test", name, "")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```