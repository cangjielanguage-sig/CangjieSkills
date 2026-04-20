### func getConfiguration()

```cangjie
public func getConfiguration(): Configuration
```

**功能：** 获取设备的Configuration。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Configuration](#class-configuration)|设备的Configuration。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let configuration = resourceManager.getConfiguration()
    Hilog.info(0, "test", configuration.locale, "")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getDeviceCapability()

```cangjie
public func getDeviceCapability(): DeviceCapability
```

**功能：** 获取设备的DeviceCapability。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[DeviceCapability](#class-devicecapability)|设备的DeviceCapability。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let deviceCapability = resourceManager.getDeviceCapability()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getLocales(Bool)

```cangjie
public func getLocales(includeSystem!: Bool = false): Array<String>
```

**功能：** 获取应用的语言列表。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|includeSystem|Bool|否|false| **命名参数。** 是否包含系统资源，默认值为false。 <br> - false：表示仅获取应用资源的语言列表。 <br> - true：表示获取系统资源和应用资源的语言列表。 <br>当使用系统资源管理对象获取语言列表时，includeSystem值无效，始终返回系统资源语言列表。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回获取的语言列表，列表中的字符串由语言、脚本（可选）、地区（可选），按照顺序使用中划线“-”连接组成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    resourceManager.getLocales()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```