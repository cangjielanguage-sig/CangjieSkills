### func formatRange(DateTime, DateTime)

```cangjie
public func formatRange(startDate: DateTime, endDate: DateTime): String
```

**功能：** 对时间段、日期段进行格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startDate|DateTime|是|-|时间、日期的开始。|
|endDate|DateTime|是|-|时间、日期的结束。|

**返回值：**

|类型|说明|
|:----|:----|
|String|格式化后的时间段、日期段字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.time.DateTime as d

let startDate = d.of(year: 2021, month: 11, dayOfMonth: 17, hour: 3, minute: 24)
let endDate = d.of(year: 2021, month: 11, dayOfMonth: 18, hour: 3, minute: 24)
// 使用en-GB locale创建DateTimeFormat对象
let datefmt = DateTimeFormat("en-GB")
let formattedDateRange = datefmt.formatRange(startDate, endDate) // formattedDateRange = "17/11/2021 – 18/11/2021"
```

### func resolvedOptions()

```cangjie
public func resolvedOptions(): DateTimeOptions
```

**功能：** 获取创建时间、日期格式化对象时设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DateTimeOptions](#struct-datetimeoptions)|时间、日期格式化对象设置的配置项。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.time.DateTime as d

let d = DateTimeOptions(dateStyle: "full", timeStyle: "medium")
let datefmt = DateTimeFormat("en-GB", options: d)
// 返回DateTimeFormat对象的配置项
let options = datefmt.resolvedOptions()
let dateStyle = options.dateStyle // dateStyle = "full"
let timeStyle = options.timeStyle // timeStyle = "medium"
```