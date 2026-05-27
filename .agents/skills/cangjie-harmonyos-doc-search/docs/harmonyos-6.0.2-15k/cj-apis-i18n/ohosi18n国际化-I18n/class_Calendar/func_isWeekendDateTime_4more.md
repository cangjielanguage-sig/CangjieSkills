### func isWeekend(?DateTime)

```cangjie
public func isWeekend(date!: ?DateTime = None): Bool
```

**功能：** 判断指定的日期在日历中是否为周末。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|?DateTime|否|None| **命名参数。** 指定的日期。若不填，则判断当前日期是否为周末。默认值为None时是系统日期。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若判断指定日期为周末时，返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.time.DateTime

let calendar = getCalendar("zh-Hans")
calendar.set(2021,11,11)  // set time to 2021.12.11
calendar.isWeekend() // true
let date = DateTime.ofUTC(year: 2024, month: 11, dayOfMonth: 4, hour: 0, minute: 0, second: 0, nanosecond: 0)
calendar.isWeekend(date: date) // false
```

### func set(Int32, Int32, Int32, Int32, Int32, Int32)

```cangjie
public func set(year: Int32, month: Int32, day: Int32,
    hour!: Int32 = -1, minute!: Int32 = -1, second!: Int32 = -1): Unit
```

**功能：** 设置日历对象的年、月、日、时、分、秒。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|year|Int32|是|-|设置的年。|
|month|Int32|是|-|设置的月。说明：月份从0开始计数，如0表示一月。|
|day|Int32|是|-|设置的日。|
|hour|Int32|否|- 1| **命名参数。** 设置的小时。-1代表系统小时。|
|minute|Int32|否|- 1| **命名参数。** 设置的分钟。-1代表系统分钟。|
|second|Int32|否|- 1| **命名参数。** 设置的秒。-1代表系统秒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
calendar.set(2021,11,11)  // set time to 2021.12.11
```

### func setFirstDayOfWeek(Int32)

```cangjie
public func setFirstDayOfWeek(value: Int32): Unit
```

**功能：** 设置每一周的起始日。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|设置一周的起始日，1代表周日，7代表周六。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
calendar.setFirstDayOfWeek(3)
let firstDayOfWeek = calendar.getFirstDayOfWeek() // firstDayOfWeek = 3
```

### func setMinimalDaysInFirstWeek(Int32)

```cangjie
public func setMinimalDaysInFirstWeek(value: Int32): Unit
```

**功能：** 设置一年中第一周的最小天数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|一年中第一周的最小天数。这表示为了确定一年中的第一周至少需要包含的天数。例如，如果这个值为4，那么一年的第一周必须至少包含4天，否则这些天将被算作上一年的最后一周。这一设定帮助确保周数的计算符合不同地区的习惯。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
calendar.setMinimalDaysInFirstWeek(3)
let minimalDaysInFirstWeek = calendar.getMinimalDaysInFirstWeek() // minimalDaysInFirstWeek = 3
```