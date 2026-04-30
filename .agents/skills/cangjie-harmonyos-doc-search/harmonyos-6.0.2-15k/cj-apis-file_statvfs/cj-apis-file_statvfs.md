# ohos.file_statvfs（文件系统空间统计）

该模块提供文件系统相关存储信息的功能，向应用程序提供获取文件系统总字节数、空闲字节数的仓颉接口。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class Statfs

```cangjie
public class Statfs {}
```

**功能：** 该类提供文件系统相关存储信息的功能。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### static func getFreeSize(String)

```cangjie
public static func getFreeSize(path: String): Int64
```

**功能：** 获取指定文件系统空闲字节数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|需要查询的文件系统的文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回空闲字节数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let path = "/data/storage/el2/base/haps/entry/files"
let number = Statfs.getFreeSize(path)
```

### static func getTotalSize(String)

```cangjie
public static func getTotalSize(path: String): Int64
```

**功能：** 获取指定文件系统总字节数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|需要查询的文件系统的文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回总字节数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let path = "/data/storage/el2/base/haps/entry/files"
let number = Statfs.getTotalSize(path)
```
