### func getDisplayName(String)

```cangjie
public func getDisplayName(locale: String): String
```

**功能：** 获取日历对象在该区域的名字。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

**返回值：**

|类型|说明|
|:----|:----|
|String|日历在locale所指示区域的名字。如buddhist在en-US上显示的名称为“Buddhist Calendar”。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US", calendarType: "buddhist")
let res = calendar.getDisplayName("zh") // res = "佛历"
```

### func getFirstDayOfWeek()

```cangjie
public func getFirstDayOfWeek(): Int32
```

**功能：** 获取日历对象的一周起始日。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|获取一周的起始日，1代表周日，7代表周六。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US")
let res = calendar.getFirstDayOfWeek() // res = 1
```

### func getMinimalDaysInFirstWeek()

```cangjie
public func getMinimalDaysInFirstWeek(): Int32
```

**功能：** 获取一年中第一周的最小天数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|一年中第一周的最小天数。这表示为了确定一年中的第一周至少需要包含的天数。例如，如果这个值设置为4，那么一年的第一周必须至少包含4天，否则这些天将被算作上一年的最后一周。这一设定帮助确保周数的计算符合不同地区的习惯。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
let res = calendar.getMinimalDaysInFirstWeek() // res = 1
```

### func getTimeInMillis()

```cangjie
public func getTimeInMillis(): Float64
```

**功能：** 获取当前日历的UTC毫秒数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|当前日历的UTC毫秒数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US")
calendar.setTime(5000.0)
let millis = calendar.getTimeInMillis() // millis = 5000
```

### func getTimeZone()

```cangjie
public func getTimeZone(): String
```

**功能：** 获取日历对象的时区。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|合法的时区ID，如“Asia/Shanghai”。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans", calendarType: "chinese")
calendar.setTimeZone("Asia/Shanghai")
let timeZone = calendar.getTimeZone() // timeZone = "Asia/Shanghai"
```