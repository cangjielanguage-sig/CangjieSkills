### func getBooleanByName(String)

```cangjie
public func getBooleanByName(resName: String): Bool
```

**功能：** 获取资源名对应的布尔结果。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|资源名对应的布尔结果。|

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
resourceManager.getBooleanByName("test")
```

### func getColor(AppResource)

```cangjie
public func getColor(resource: AppResource): UInt32
```

**功能：** 获取资源对象对应颜色资源的值。此接口用于多工程应用内跨包访问。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|资源对象对应颜色资源的值（十进制）。|

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
let res = @r(app.color.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getColor(resource)
```

### func getColor(Int32)

```cangjie
public func getColor(resId: Int32): UInt32
```

**功能：** 获取资源ID对应颜色资源的值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|Int32|是|-|资源ID。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|资源对象对应颜色资源的值（十进制）。|

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
let res = @r(app.color.test)
resourceManager.getColor(Int32(res.id))
```