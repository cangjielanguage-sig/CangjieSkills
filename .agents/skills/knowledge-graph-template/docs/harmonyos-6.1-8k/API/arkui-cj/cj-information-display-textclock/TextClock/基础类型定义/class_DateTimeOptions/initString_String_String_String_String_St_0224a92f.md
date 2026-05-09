#### init(?String, ?String, ?String, ?String, ?String, ?String, ?Bool, ?String, ?String, ?String, ?String, ?String, ?String, ?String, ?String, ?String, ?String, ?String, ?String)

```cangjie
public init(locale!: ?String = None, dateStyle!: ?String = None, timeStyle!: ?String = None,
    hourCycle!: ?String = None, timeZone!: ?String = None, numberingSystem!: ?String = None, hour12!: ?Bool = None,
    weekday!: ?String = None, era!: ?String = None, year!: ?String = None, month!: ?String = None,
    day!: ?String = None, hour!: ?String = None, minute!: ?String = None, second!: ?String = None,
    timeZoneName!: ?String = None, dayPeriod!: ?String = None, localeMatcher!: ?String = None,
    formatMatcher!: ?String = None)
```

**功能：** DateTimeOptions的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|?String|否|None| **命名参数。** 区域设置ID。初始值："zh-Hans-CN"。|
|dateStyle|?String|否|None| **命名参数。** 日期显示格式。初始值："long"。|
|timeStyle|?String|否|None| **命名参数。** 时间显示格式。初始值："long"。|
|hourCycle|?String|否|None| **命名参数。** 小时周期。初始值："h11"。|
|timeZone|?String|否|None| **命名参数。** 时区。初始值：""。|
|numberingSystem|?String|否|None| **命名参数。** 数字系统。初始值："adlm"。|
|hour12|?Bool|否|None| **命名参数。** 是否使用12小时制。初始值：false。|
|weekday|?String|否|None| **命名参数。** 星期显示格式。初始值："long"。|
|era|?String|否|None| **命名参数。** 纪元显示格式。初始值："long"。|
|year|?String|否|None| **命名参数。** 年份显示格式。初始值："numeric"。|
|month|?String|否|None| **命名参数。** 月份显示格式。初始值："numeric"。|
|day|?String|否|None| **命名参数。** 天显示格式。初始值："numeric"。|
|hour|?String|否|None| **命名参数。** 小时显示格式。初始值："numeric"。|
|minute|?String|否|None| **命名参数。** 分钟显示格式。初始值："numeric"。|
|second|?String|否|None| **命名参数。** 秒显示格式。初始值："numeric"。|
|timeZoneName|?String|否|None| **命名参数。** 时区名称显示格式。初始值："long"。|
|dayPeriod|?String|否|None| **命名参数。** 时间段显示格式初始值："long"。|
|localeMatcher|?String|否|None| **命名参数。** 区域设置匹配算法。初始值："lookup"。|
|formatMatcher|?String|否|None| **命名参数。** 格式匹配算法。初始值："basic"。|