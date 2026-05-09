## enum Display

```cangjie
public enum Display <: ToString {
    | FontScale
    | ScreenBrightnessStatus
    | AutoScreenBrightness
    | ScreenOffTimeout
    | AutoScreenBrightnessMode
    | ManualScreenBrightnessMode
    | ...
}
```

**功能：** 提供设置显示效果的数据项（暂不支持）。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**父类型：**

- ToString

### AutoScreenBrightness

```cangjie
AutoScreenBrightness
```

**功能：** 是否启用屏幕亮度自动调整。

值为AutoScreenBrightnessMode，表示启用自动调整。

值为ManualScreenBrightnessMode，表示不启用自动调整。

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
    let autoBrightness = getValue(context, Display.AutoScreenBrightness, "0")
    Hilog.info(0, "cangjie_ohos_test", "Auto screen brightness setting: ${autoBrightness}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### FontScale

```cangjie
FontScale
```

**功能：** （domainName为USER_PROPERTY）字体的比例因子，值为固定浮点数。标准档位取值为1，其他档位包括0.85、1.15、1.3、1.45。关怀模式下，额外提供1.75、2、3.2档位。

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
    let fontScale = getValue(context, Display.FontScale, "1.0")
    Hilog.info(0, "cangjie_ohos_test", "Font scale setting: ${fontScale}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### ScreenBrightnessStatus

```cangjie
ScreenBrightnessStatus
```

**功能：** 屏幕亮度。取值范围:0到255。

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
    let brightness = getValue(context, Display.ScreenBrightnessStatus, "128")
    Hilog.info(0, "cangjie_ohos_test", "Screen brightness setting: ${brightness}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### ScreenOffTimeout

```cangjie
ScreenOffTimeout
```

**功能：** 设备在一段时间不活动后进入睡眠状态的等待时间（单位: ms）。

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
    let timeout = getValue(context, Display.ScreenOffTimeout, "30000")
    Hilog.info(0, "cangjie_ohos_test", "Screen off timeout setting: ${timeout} ms")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### AutoScreenBrightnessMode

```cangjie
AutoScreenBrightnessMode
```

**功能：** 使用屏幕亮度自动调整时AutoScreenBrightness的值。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

### ManualScreenBrightnessMode

```cangjie
ManualScreenBrightnessMode
```

**功能：** 使用屏幕亮度手动调整时的AutoScreenBrightness值。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22