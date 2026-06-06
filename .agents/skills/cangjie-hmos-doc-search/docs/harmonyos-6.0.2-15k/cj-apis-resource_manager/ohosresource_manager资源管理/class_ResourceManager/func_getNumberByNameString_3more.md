### func getNumberByName(String)

```cangjie
public func getNumberByName(resName: String): Number
```

**功能：** 获取资源名的数字资源。若integer资源和float资源中有相同的`resName`，优先返回integer资源的数值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|

**返回值：**

|类型|说明|
|:----|:----|
|[Number](#enum-number)|资源名对应的数字资源。|

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
let number = resourceManager.getNumberByName("test")
match (number) {
    case INT(v) => AppLog.info(v.toString())
    case FLOAT(v) => AppLog.info(v.toString())
    case _ => throw IllegalArgumentException("The type is not supported.")
}
```

### func getOverrideConfiguration()

```cangjie
public func getOverrideConfiguration(): Configuration
```

**功能：** 获取差异化资源的配置。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[Configuration](#class-configuration)|差异化资源的配置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
resourceManager.getOverrideConfiguration()
```

### func getOverrideResourceManager(Configuration)

```cangjie
public func getOverrideResourceManager(configuration!: ?Configuration = None): ResourceManager
```

**功能：** 获取可以加载差异化资源的资源管理对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|configuration|[Configuration](#class-configuration)|否|None|指定想要获取的资源配置。<br>通过[getOverrideConfiguration](#func-getoverrideconfiguration)获取差异化配置后，根据需求修改配置项，再作为参数传入该函数。<br>若缺省则表示使用当前系统的configuration。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResourceManager](#class-resourcemanager)|可以加载差异化资源的资源管理对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let config = resourceManager.getOverrideConfiguration()
resourceManager.getOverrideResourceManager(configuration: config)
```