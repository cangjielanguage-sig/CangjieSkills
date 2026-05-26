### func closeRawFd(String)

```cangjie
public func closeRawFd(path: String): Unit
```

**功能：** 关闭resources/rawfile目录下rawfile文件。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|rawfile文件路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001005|The resource not found by path.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let rawfd = resourceManager.closeRawFd("test.txt")
```

### func getBoolean(Int32)

```cangjie
public func getBoolean(resId: Int32): Bool
```

**功能：** 获取资源ID对应的布尔结果。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|Int32|是|-|资源ID。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|资源对象对应的布尔结果。|

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
let res = @r(app.boolean.test)
resourceManager.getBoolean(Int32(res.id))
```

### func getBoolean(AppResource)

```cangjie
public func getBoolean(resource: AppResource): Bool
```

**功能：** 获取资源对象对应的布尔结果。此接口用于多工程应用内跨包访问。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resource|[AppResource](#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|资源对象对应的布尔结果。|

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
let res = @r(app.boolean.test)
let resource = AppResource("com.example.myapplication", "entry", Int32(res.id))
resourceManager.getBoolean(resource)
```