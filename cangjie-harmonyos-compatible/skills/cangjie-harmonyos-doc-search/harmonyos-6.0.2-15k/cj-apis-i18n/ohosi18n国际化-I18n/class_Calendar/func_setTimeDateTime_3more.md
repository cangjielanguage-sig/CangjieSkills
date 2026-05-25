### func setTime(DateTime)

```cangjie
public func setTime(date: DateTime): Unit
```

**功能：** 设置日历对象内部的时间日期。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|DateTime|是|-|将要设置的日历对象的内部时间日期。说明：月份从0开始计数，如0表示一月。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.time.DateTime

let calendar = getCalendar("en-US")
let date: DateTime = DateTime.nowUTC()
calendar.setTime(date) // set time to nowUTC
```

### func setTime(Float64)

```cangjie
public func setTime(time: Float64): Unit
```

**功能：** 设置日历对象内部的时间日期，time为从1970.1.1 00:00:00 GMT逝去的毫秒数。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|time|Float64|是|-|time为从1970.1.1 00:00:00 GMT逝去的毫秒数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US")
calendar.setTime(10540800000.0)
```

### func setTimeZone(String)

```cangjie
public func setTimeZone(timeZone: String): Unit
```

**功能：** 设置日历对象的时区。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeZone|String|是|-|合法的时区ID，如“Asia/Shanghai”。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US")
calendar.setTimeZone("Asia/Shanghai")
```