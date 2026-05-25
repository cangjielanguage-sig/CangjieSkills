### func getMediaContent(UInt32, ?ScreenDensity)

```cangjie
public func getMediaContent(resId: UInt32, density!: ?ScreenDensity = None): Array<UInt8>
```

**功能：** 获取指定资源ID对应的默认或指定的屏幕密度媒体文件内容。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|
|density|?[ScreenDensity](#enum-screendensity)|否|None| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|资源ID对应的媒体文件内容。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID. |
  | 9001002 | No matching resource is found based on the resource ID. |

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
    let res = @r(app.media.test)
    resourceManager.getMediaContent(res.id, density: ScreenSdpi)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getMediaContentBase64(UInt32, ?ScreenDensity)

```cangjie
public func getMediaContentBase64(resId: UInt32, density!: ?ScreenDensity = None): String
```

**功能：** 获取指定资源ID对应的默认或指定的屏幕密度图片资源Base64编码。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID值。|
|density|?[ScreenDensity](#enum-screendensity)|否|None| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源ID对应的图片资源Base64编码。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID. |
  | 9001002 | No matching resource is found based on the resource ID. |

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
    let res = @r(app.media.test)
    let code = resourceManager.getMediaContentBase64(res.id)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```