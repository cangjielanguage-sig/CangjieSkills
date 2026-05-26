### static func copy(String, String, CopyOptions)

```cangjie
public static func copy(srcUri: String, destUri: String, option: CopyOptions): Unit
```

**功能：** 拷贝文件或者目录。支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。 跨端拷贝时，限制同时最多存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcUri|String|是|-|待复制文件或目录的uri。|
|destUri|String|是|-|目标文件或目录的uri。|
|option|[CopyOptions](#class-copyoptions)|是|-|拷贝进度回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let srcDirPathLocal = pathDir + "/src";
let dstDirPathLocal = pathDir + "/dest";
let sig = TaskSignal()
let myProgress = ProgressListener({progress => AppLog.info("progress ${progress.processedSize} total ${progress.totalSize}")
if (progress.totalSize < progress.processedSize * 2) {
    AppLog.info("try cancel")
    sig.cancel()
}})
let myOpt = CopyOptions(myProgress, sig)
FileFs.copy(srcDirPathLocal, dstDirPathLocal, myOpt)
```

### static func copy(String, String)

```cangjie
public static func copy(srcUri: String, destUri: String): Unit
```

**功能：** 拷贝文件或者目录。支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。 跨端拷贝时，限制同时最多存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcUri|String|是|-|待复制文件或目录的uri。|
|destUri|String|是|-|目标文件或目录的uri。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let srcDirPathLocal = pathDir + "/src";
let dstDirPathLocal = pathDir + "/dest";
let sig = TaskSignal()
let myProgress = ProgressListener({progress => AppLog.info("progress ${progress.processedSize} total ${progress.totalSize}")
if (progress.totalSize < progress.processedSize * 2) {
    AppLog.info("try cancel")
    sig.cancel()
    }})
FileFs.copy(srcDirPathLocal, dstDirPathLocal)
```