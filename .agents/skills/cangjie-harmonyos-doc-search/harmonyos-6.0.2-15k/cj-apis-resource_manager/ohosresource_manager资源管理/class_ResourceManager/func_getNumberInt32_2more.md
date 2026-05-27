### func getNumber(Int32)

```cangjie
public func getNumber(resId: Int32): Number
```

**功能：** 获取资源ID对应的数字资源。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|Int32|是|-|资源ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[Number](#enum-number)|资源对象对应的数字资源。|

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
let res = @r(app.integer.test)
let number = resourceManager.getNumber(Int32(res.id))
match (number) {
    case INT(v) => AppLog.info(v.toString())
    case FLOAT(v) => AppLog.info(v.toString())
    case _ => throw IllegalArgumentException("The type is not supported.")
}
```

### func getNumber(AppResource)

```cangjie
public func getNumber(resource: AppResource): Number
```

**功能：** 获取资源对象的数字资源。此接口用于多工程应用内跨包访问。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[Number](#enum-number)|资源对象对应的数字资源。|

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
let res = @r(app.integer.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
let number = resourceManager.getNumber(resource)
match (number) {
    case INT(v) => AppLog.info(v.toString())
    case FLOAT(v) => AppLog.info(v.toString())
    case _ => throw IllegalArgumentException("The type is not supported.")
}
```