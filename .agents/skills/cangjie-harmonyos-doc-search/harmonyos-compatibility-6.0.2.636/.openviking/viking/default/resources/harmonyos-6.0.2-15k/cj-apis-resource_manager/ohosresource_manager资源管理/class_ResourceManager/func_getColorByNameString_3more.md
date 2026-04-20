### func getColorByName(String)

```cangjie
public func getColorByName(resName: String): UInt32
```

**功能：** 获取资源名对应颜色资源的值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|资源名对应颜色资源的值（十进制）。|

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
resourceManager.getColorByName("test")
```

### func getConfiguration()

```cangjie
public func getConfiguration(): Configuration
```

**功能：** 获取设备的配置信息，返回[Configuration](#class-configuration)对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Configuration](#class-configuration)|设备的配置信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let configuration = resourceManager.getConfiguration()
AppLog.info(configuration.locale)
AppLog.info(configuration.direction.getValue().toString())
```

### func getDeviceCapability()

```cangjie
public func getDeviceCapability(): DeviceCapability
```

**功能：** 获取设备的设备能力，返回[DeviceCapability](#class-devicecapability)对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[DeviceCapability](#class-devicecapability)|设备能力。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.AbilityKit.*

let stageContext = getStageContext(MainAbility.abilityContext.getOrThrow())
let resourceManager = ResourceManager.getResourceManager(stageContext)
let deviceCapability = resourceManager.getDeviceCapability()
AppLog.info(deviceCapability.screenDensity.getValue().toString())
AppLog.info(deviceCapability.deviceType.getValue().toString())
```