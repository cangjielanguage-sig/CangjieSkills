### func getString(AppResource)

```cangjie
public func getString(resource: AppResource): String
```

**功能：** 获取资源对象对应的字符串资源。此接口用于多工程应用内跨包访问。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源对象对应的字符串资源。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|
  |9001006|If the resource re-ref too much.|
  |9001007|If the resource obtained by resId formatting error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.string.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getString(resource)
```

### func getString(AppResource, Array\<FormatArgs>)

```cangjie
public func getString(resource: AppResource, args: Array<FormatArgs>): String
```

**功能：** 获取资源对象对应的字符串资源，根据args参数进行格式化。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|
|args|Array\<[FormatArgs](#enum-formatargs)>|是|-|格式化字符串资源参数。 <br>支持参数类型：<br /> %d、%f、%s、%%。 <br>说明：%%转译符，转译%。<br>举例：%%d格式化后为%d字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|String|资源名对应的格式化字符串。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001001|If the resId invalid.|
  |9001002|If the resource not found by resId.|
  |9001006|If the resource re-ref too much.|
  |9001007|If the resource obtained by resId formatting error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let res = @r(app.string.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getString(resource, FormatArgs.STRING("format string"), FormatArgs.INT(10), FormatArgs.FLOAT(98.78))
```