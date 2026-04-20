### func getDrawableDescriptorByName(String, UInt32)

```cangjie
public func getDrawableDescriptorByName(resName: String, density!: UInt32 = 0): DrawableDescriptor
```

**功能：** 获取资源对象对应的图片资源，返回图片资源的[DrawableDescriptor](#class-drawabledescriptor)用于图标的显示。此接口用于多工程应用内跨包访问。

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
|[DrawableDescriptor](#class-drawabledescriptor)|资源ID对应图片资源的[DrawableDescriptor](#class-drawabledescriptor)对象。|

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
resourceManager.getDrawableDescriptorByName("test")
```

### func getLocales(Bool)

```cangjie
public func getLocales(includeSystem!: Bool = false): Array<String>
```

**功能：** 获取应用的语言列表。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|includeSystem|Bool|否|false| **命名参数。** 是否包含系统资源，默认值为false。 <br> false：表示仅获取应用资源的语言列表。 <br>true：表示获取系统资源和应用资源的语言列表。 <br>当系统资源管理对象获取语言列表时，includeSystem值无效，返回获取系统资源语言列表。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回获取的语言列表，列表中的字符串由语言、脚本（可选）、地区（可选），按照顺序使用中划线"-"连接组成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getLocales()
```