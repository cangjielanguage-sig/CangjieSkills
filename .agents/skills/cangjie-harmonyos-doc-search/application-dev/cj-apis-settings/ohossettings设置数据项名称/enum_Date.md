## enum Date

```cangjie
public enum Date <: ToString {
    | DateFormat
    | TimeFormat
    | AutoGainTime
    | AutoGainTimeZone
    | ...
}
```

**功能：** 提供设置时间和日期格式的数据项（暂不支持）。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**父类型：**

- ToString

### AutoGainTime

```cangjie
AutoGainTime
```

**功能：** 是否自动从网络获取日期、时间和时区。

值为true，表示自动从网络获取信息。

值为false，表示不自动获取信息。

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
    let autoGainTime = getValue(context, Date.AutoGainTime, "false")
    Hilog.info(0, "cangjie_ohos_test", "Auto gain time setting: ${autoGainTime}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### AutoGainTimeZone

```cangjie
AutoGainTimeZone
```

**功能：** 是否自动从NITZ获取时区。

值为true，表示自动获取。

值为false，表示不自动获取。

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
    let autoGainTimeZone = getValue(context, Date.AutoGainTimeZone, "false")
    Hilog.info(0, "cangjie_ohos_test", "Auto gain time zone setting: ${autoGainTimeZone}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### DateFormat

```cangjie
DateFormat
```

**功能：** 日期格式。

日期格式包括mm/dd/yyyy、dd/mm/yyyy和yyyy/mm/dd，其中mm、dd和yyyy分别代表月份、日期和年份。

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
    let dateFormat = getValue(context, Date.DateFormat, "MM/dd/yyyy")
    Hilog.info(0, "cangjie_ohos_test", "Date format setting: ${dateFormat}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### TimeFormat

```cangjie
TimeFormat
```

**功能：** 时间以12小时格式或24小时格式显示。

值为 "12"表示12小时格式。

值为"24"表示24小时格式。

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
    let timeFormat = getValue(context, Date.TimeFormat, "24")
    Hilog.info(0, "cangjie_ohos_test", "Time format setting: ${timeFormat}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置时间和日期格式的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|设置时间和日期格式的数据项。|