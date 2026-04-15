### func set(Int32, Int32, Int32, ?Int32, ?Int32, ?Int32)

```cangjie
public func set(year: Int32, month: Int32, date: Int32, hour!: ?Int32 = None, minute!: ?Int32 = None, second!: ?Int32 = None): Unit
```

**功能：** 设置日历对象的年、月、日、时、分、秒。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|year|Int32|是|-|设置的年。|
|month|Int32|是|-|设置的月。说明：月份从0开始计数，如0表示一月。|
|date|Int32|是|-|设置的日。|
|hour|?Int32|否|None|**命名参数。** 设置的小时。默认值：系统当前时间。|
|minute|?Int32|否|None|**命名参数。** 设置的分钟。默认值：系统当前时间。|
|second|?Int32|否|None|**命名参数。** 设置的秒。默认值：系统当前时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("zh-Hans")
    calendar.set(2021,11,11)  // set time to 2021.12.11
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setFirstDayOfWeek(Int32)

```cangjie
public func setFirstDayOfWeek(value: Int32): Unit
```

**功能：** 设置日历对象的周起始日。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|一周的起始日，1代表周日，7代表周六。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("zh-Hans")
    calendar.setFirstDayOfWeek(3)
    let firstDayOfWeek = calendar.getFirstDayOfWeek() // firstDayOfWeek = 3
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setMinimalDaysInFirstWeek(Int32)

```cangjie
public func setMinimalDaysInFirstWeek(value: Int32): Unit
```

**功能：** 设置日历对象一年中第一周的最小天数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|一年中第一周的最小天数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("zh-Hans")
    calendar.setMinimalDaysInFirstWeek(3)
    let minimalDaysInFirstWeek = calendar.getMinimalDaysInFirstWeek() // minimalDaysInFirstWeek = 3
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setTime(Float64)

```cangjie
public func setTime(time: Float64): Unit
```

**功能：** 基于传入的时间戳，设置日历对象内部的时间、日期。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|time|Float64|是|-|Unix时间戳，表示从1970.1.1&nbsp;00:00:00&nbsp;GMT逝去的毫秒数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let calendar = getCalendar("en-US")
    calendar.setTime(10540800000.0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```