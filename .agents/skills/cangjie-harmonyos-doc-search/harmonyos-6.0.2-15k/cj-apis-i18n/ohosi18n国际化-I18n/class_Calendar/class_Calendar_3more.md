## class Calendar

```cangjie
public class Calendar {}
```

**功能：** 实体日历对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### func add(String, Int32)

```cangjie
public func add(field: String, amount: Int32): Unit
```

**功能：** 在日历的给定字段进行加减操作。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|field|String|是|-|指定进行操作的日历字段，目前支持的field值有year, month, week_of_year, week_of_month, date, day_of_year, day_of_week, day_of_week_in_month, hour, hour_of_day, minute, second, millisecond。|
|amount|Int32|是|-|进行加减操作的具体数值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[I18n错误码](../../errorcodes/cj-errorcode-i18n.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |890001|Invalid parameter. Possible causes: Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
calendar.set(2021,11,11) // set time to 2021.12.11
calendar.add("year", 3)
let res = calendar.get("year") // res = 2024
```

### func compareDays(DateTime)

```cangjie
public func compareDays(date: DateTime): Int32
```

**功能：** 比较日历和指定日期相差的天数（按毫秒级的精度，不足一天将按一天进行计算）。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|DateTime|是|-|时间、日期。说明：月份从0开始计数，如0表示一月。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|相差的天数，正数代表日历时间更早，负数代表日历时间更晚。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let calendar = getCalendar("zh-Hans")
calendar.set(2021,11,11) // set time to 2021.12.11
let date = DateTime.ofUTC(year: 2024, month: 12, dayOfMonth: 4, hour: 0, minute: 0, second: 0, nanosecond: 0)
let result = calendar.compareDays(date) // result = -8
```