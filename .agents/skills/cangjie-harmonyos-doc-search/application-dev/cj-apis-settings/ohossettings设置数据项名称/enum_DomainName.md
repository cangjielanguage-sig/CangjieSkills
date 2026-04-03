## enum DomainName

```cangjie
public enum DomainName <: ToString {
    | DeviceShared
    | UserProperty
    | ...
}
```

**功能：** 提供查询的域名。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**父类型：**

- ToString

### DeviceShared

```cangjie
DeviceShared
```

**功能：** 设备属性共享域，所有设置项不区分多用户。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let value = getValue(context, Display.ScreenBrightnessStatus, "100", DomainName.DeviceShared)
    Hilog.info(0, "cangjie_ohos_test", "Device shared screen brightness: ${value}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### UserProperty

```cangjie
UserProperty
```

**功能：** 为用户属性域，该域下所有配置区分多用户。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let value = getValue(context, Display.ScreenBrightnessStatus, "100", DomainName.UserProperty)
    Hilog.info(0, "cangjie_ohos_test", "User property screen brightness: ${value}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回查询的域名对应字符串。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|查询的域名对应字符串。|