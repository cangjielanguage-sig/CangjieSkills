### func getMediaContentBase64(Int32, UInt32)

```cangjie
public func getMediaContentBase64(resId: Int32, density!: UInt32 = 0): String
```

**功能：** 获取资源ID对应指定屏幕密度的图片资源，返回图片资源的Base64编码。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|Int32|是|-|资源ID。|
|density|UInt32|否|0| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源对象对应图片资源的Base64编码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|If the density invalid.|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.media.test)
resourceManager.getMediaContentBase64(Int32(res.id), density: 120)
```

### func getMediaContentBase64(AppResource, UInt32)

```cangjie
public func getMediaContentBase64(resource: AppResource, density!: UInt32 = 0): String
```

**功能：** 获取资源对象对应指定屏幕密度的图片资源，返回图片资源的Base64编码。此接口用于多工程应用内跨包访问。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|
|density|UInt32|否|0| **命名参数。** 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源对象对应图片资源的Base64编码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|If the density invalid.|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.media.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getMediaContentBase64(resource, density: 120)
```