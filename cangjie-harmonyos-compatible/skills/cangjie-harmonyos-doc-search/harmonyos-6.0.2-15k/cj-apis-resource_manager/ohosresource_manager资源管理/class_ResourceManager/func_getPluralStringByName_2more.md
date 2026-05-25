### func getPluralStringByName(String, Int64)

```cangjie
public func getPluralStringByName(resName: String, num: Int64): String
```

**功能：** 获取资源名的单复数字符串资源，并根据指定数量格式化字符串。

> **说明：**
>
> 中文环境下，字符串不区分单复数；英文环境下，字符串区分单复数。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|
|num|Int64|是|-|数量值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|指定资源名的单复数字符串资源。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001003|If the resName invalid.|
  |9001004|If the resource not found by resName.|
  |9001006|If the resource re-ref too much.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getPluralStringByName("test", 1)
```

### func getPluralStringValue(Int32, Int64)

```cangjie
public func getPluralStringValue(resId: Int32, num: Int64): String
```

**功能：** 获取资源ID的单复数字符串资源，并根据指定数量格式化字符串。

> **说明：**
>
> 中文环境下，字符串不区分单复数；英文环境下，字符串区分单复数。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|Int32|是|-|资源ID。|
|num|Int64|是|-|数量值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|指定资源对象的单复数字符串资源。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|
  |9001006|If the resource re-ref too much.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.plural.test)
resourceManager.getPluralStringValue(Int32(res.id), 1)
```