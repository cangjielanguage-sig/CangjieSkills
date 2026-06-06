## class ResourceManager

```cangjie
public class ResourceManager {}
```

**功能：** 提供访问应用资源的能力。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

> **说明：**
>
> - 资源文件在工程的resources目录中定义，资源ID可通过@r(资源地址).id的方式获取，例如@r(app.string.test).id。
>
> - 对于本应用包资源，通过指定资源ID或资源名进行访问。对于应用内跨包资源，通过指定[AppResource](#class-appresource)对象进行访问。

### static func getResourceManager(StageContext)

```cangjie
public static func getResourceManager(context: StageContext): ResourceManager
```

**功能：** 根据上下文，获取资源管理对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResourceManager](#class-resourcemanager)|资源管理对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resMgr = ResourceManager.getResourceManager(stageContext)
```

### static func getSystemResourceManager()

```cangjie
public static func getSystemResourceManager(): ResourceManager
```

**功能：** 获取系统资源管理对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ResourceManager](#class-resourcemanager)|系统资源管理对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001009|If application can’t access system resource.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

ResourceManager.getSystemResourceManager()
```

### func addResource(String)

```cangjie
public func addResource(path: String): Unit
```

**功能：** 应用运行时，加载指定的资源路径，实现资源覆盖。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|资源路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[资源管理错误码](../../errorcodes/cj-errorcode-resource-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |9001010|If the overlay path is invalid.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let path = "/data/storage/el2/base/haps/entry/files/library-default-unsigned.hsp"
resourceManager.addResource(path)
```