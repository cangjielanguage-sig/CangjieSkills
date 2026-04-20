### func getDisplayName(String)

```cangjie
public func getDisplayName(locale: String): String
```

**功能：** 获取日历对象名称在指定语言下的翻译。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域ID的字符串，由语言、脚本、国家地区组成。|

**返回值：**

|类型|说明|
|:----|:----|
|String|日历对象名称在指定语言下的翻译。如buddhist在en-US上显示的名称为“Buddhist&nbsp;Calendar”。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.i18n.CalendarType
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US", calendarType: CalendarType.Buddhist)
    let res = calendar.getDisplayName("zh") // res = "佛历"
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getFirstDayOfWeek()

```cangjie
public func getFirstDayOfWeek(): Int32
```

**功能：** 获取系统设置的周起始日。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|周起始日。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US")
    let res = calendar.getFirstDayOfWeek() // res = 1
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getMinimalDaysInFirstWeek()

```cangjie
public func getMinimalDaysInFirstWeek(): Int32
```

**功能：** 获取日历对象一年中第一周的最小天数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|一年中第一周的最小天数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("zh-Hans")
    let res = calendar.getMinimalDaysInFirstWeek() // res = 1
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getTimeInMillis()

```cangjie
public func getTimeInMillis(): Float64
```

**功能：** 获取当前日历对象的时间戳。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|Unix时间戳，表示从1970.1.1&nbsp;00:00:00&nbsp;GMT逝去的毫秒数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US")
    calendar.setTime(5000.0)
    let millis = calendar.getTimeInMillis() // millis = 5000
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getTimeZone()

```cangjie
public func getTimeZone(): String
```

**功能：** 创建对应时区城市的时区对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|时区城市ID，要求是系统支持的时区城市ID。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.i18n.CalendarType
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("zh-Hans", calendarType: CalendarType.Chinese)
    calendar.setTimeZone("Asia/Shanghai")
    let timeZone = calendar.getTimeZone() // timeZone = "Asia/Shanghai"
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```