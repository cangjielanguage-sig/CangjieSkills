## class ResourceManager

```cangjie
public class ResourceManager {}
```

**功能：** 提供访问应用资源和系统资源的能力。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### func addResource(String)

```cangjie
public func addResource(path: String): Unit
```

**功能：** 应用运行时加载指定的资源路径，实现资源覆盖。

> **说明**
>
> rawfile和resfile目录不支持资源覆盖。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|资源路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001010 | Invalid overlay path. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let path = "/data/storage/el2/base/haps/entry/files/library-default-unsigned.hsp"
    resourceManager.addResource(path)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func closeRawFd(String)

```cangjie
public func closeRawFd(path: String): Unit
```

**功能：** 关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd）。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

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
    let rawfd = resourceManager.closeRawFd("test.txt")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getBoolean(UInt32)

```cangjie
public func getBoolean(resId: UInt32): Bool
```

**功能：** 获取指定资源ID值对应的布尔值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|资源ID值对应的布尔值。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID. |
  | 9001002 | No matching resource is found based on the resource ID. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.arkui.state_macro_manage.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let res = @r(app.boolean.test)
    let result = resourceManager.getBoolean(res.id)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```