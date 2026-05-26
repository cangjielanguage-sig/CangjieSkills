### func get(String)

```cangjie
public func get(field: String): Int32
```

**功能：** 获取日历对象中与field相关联的值。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|通过field来获取日历对象相应的值。目前支持的field值请参考下表。 |

|field名称|说明|
|----- | ----------------------------------------|
|era|纪元，例如公历中的公元前或者公元后。|
|year|年。|
|month|月。说明：月份从0开始计数，如0表示一月。|
|date|日。|
|hour|挂钟小时数。|
|hour_of_day|一天中的第几小时。|
|minute|分。|
|second|秒。|
|millisecond|毫秒。|
|week_of_year|一年中的第几周，按照星期计算周，注意：第一周的归属算法各地有区别。|
|year_woy|一年中的第几周，按照数值计算周，例如一年中前1~7日属于第一周。|
|week_of_month|一个月中的第几周，按照星期计算周。|
|day_of_week_in_month|一月中的第几周，按照数值计算周，例如1-7日属于第一周。|
|day_of_year|一年中的第几天。|
|day_of_week|一周中的第几天（星期）。|
|milliseconds_in_day|一天中的第几毫秒。|
|zone_offset|以毫秒计时的时区固定偏移量（不含夏令时）。|
|dst_offset|以毫秒计时的夏令时偏移量。|
|dow_local|本地星期。|
|extended_year|扩展的年份数值，支持负数。|
|julian_day|儒略日，与当前时区相关。|
|is_leap_month|是否为闰月。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|与field相关联的值，如当前Calendar对象的内部日期的年份为1990，get(“year”)返回1990。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("en-US")
calendar.set(2024, 1, 1, hour: 12, minute: 30, second: 30)
let year = calendar.get("year") // 2024
let month = calendar.get("month") // 1
let date = calendar.get("date") // 1
let hour = calendar.get("hour_of_day") // 12
let minute = calendar.get("minute") // 30
let second = calendar.get("second") // 30
```