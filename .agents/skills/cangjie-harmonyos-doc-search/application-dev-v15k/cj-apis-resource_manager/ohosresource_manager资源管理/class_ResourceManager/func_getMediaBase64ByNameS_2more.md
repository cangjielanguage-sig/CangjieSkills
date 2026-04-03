### func getMediaBase64ByName(String, UInt32)

```cangjie
public func getMediaBase64ByName(resName: String, density!: UInt32 = 0): String
```

**功能：** 获取资源名对应指定屏幕密度的图片资源，返回图片资源的Base64编码。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|
|density|UInt32|否|0| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源名对应图片资源的Base64编码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|If the density invalid.|
  |9001003|If the resName invalid.|
  |9001004|If the resource not found by resName.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getMediaBase64ByName("test")
```

### func getMediaByName(String, UInt32)

```cangjie
public func getMediaByName(resName: String, density: UInt32): Array<UInt8>
```

**功能：** 获取资源名对应指定屏幕密度的媒体文件内容。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|
|density|UInt32|是|-|资源获取需要的屏幕密度，0表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|资源名对应的媒体资源。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|If the density invalid.|
  |9001003|If the resName invalid.|
  |9001004|If the resource not found by resName.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getMediaByName("test", 120)
```