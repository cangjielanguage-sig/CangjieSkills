### func getMediaBase64ByName(String, ?ScreenDensity)

```cangjie
public func getMediaBase64ByName(resName: String, density!: ?ScreenDensity = None): String
```

**功能：** 获取指定资源名称对应的默认或指定的屏幕密度图片资源Base64编码。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源ID。|
|density|?[ScreenDensity](#enum-screendensity)|否|None| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源名称对应的图片资源Base64编码。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let code = resourceManager.getMediaBase64ByName("test")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getMediaByName(String, ?ScreenDensity)

```cangjie
public func getMediaByName(resName: String, density!: ?ScreenDensity = None): Array<UInt8>
```

**功能：** 获取指定资源名称对应的默认或指定的屏幕密度媒体文件内容。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|
|density|?[ScreenDensity](#enum-screendensity)|否|None| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|资源名称对应的媒体文件内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    resourceManager.getMediaByName("test", density: ScreenMdpi)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```