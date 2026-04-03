### func getBooleanByName(String)

```cangjie
public func getBooleanByName(resName: String): Bool
```

**功能：** 获取指定资源名称对应的布尔值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|资源名称对应的布尔值。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let result = resourceManager.getBooleanByName("test")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getColor(UInt32)

```cangjie
public func getColor(resId: UInt32): UInt32
```

**功能：** 获取指定资源ID对应的颜色值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回资源ID值对应的颜色值（十进制）。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID.|
  | 9001002 | No matching resource is found based on the resource ID.|
  | 9001006 | The resource is referenced cyclically.|

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
    let res = @r(app.color.test)
    let result = resourceManager.getColor(res.id)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getColorByName(String)

```cangjie
public func getColorByName(resName: String): UInt32
```

**功能：** 获取指定资源名称对应的颜色值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回资源名称对应的颜色值（十进制）。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let result = resourceManager.getColorByName("test")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```