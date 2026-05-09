### func getRawFd(String)

```cangjie
public func getRawFd(path: String): RawFileDescriptor
```

**功能：** 获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。

> **说明**
>
> 文件描述符（fd）使用完毕后需调用[closeRawFd](#func-closerawfdstring)关闭fd，避免资源泄露。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|[RawFileDescriptor](./cj-apis-raw_file_descriptor.md#class-rawfiledescriptor)|rawfile文件所在HAP的文件描述符（fd）。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001005 | Invalid relative path. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let rawfd = resourceManager.getRawFd("test.txt")
    Hilog.info(0, "test", "${rawfd.fd} ${rawfd.offset} ${rawfd.length}", "")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getRawFileContent(String)

```cangjie
public func getRawFileContent(path: String): Array<UInt8>
```

**功能：** 获取resources/rawfile目录下对应的rawfile文件内容。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回获取的rawfile文件内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001005 | Invalid relative path. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    resourceManager.getRawFileContent("test.txt")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getRawFileList(String)

```cangjie
public func getRawFileList(path: String): Array<String>
```

**功能：** 获取resources/rawfile目录下文件夹及文件列表。

>**说明**
>
> 若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件夹路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|rawfile文件目录下的文件夹及文件列表。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001005 | Invalid relative path. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    resourceManager.getRawFileList("")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```