#### init(String, String, String, String, String, String, Bool, String, String, String, String, String, String, String, String, String, String, String, String)

```cangjie
public init(locale!: String = "zh-Hans-CN", dateStyle!: String = "long", timeStyle!: String = "long",
    hourCycle!: String = "h11", timeZone!: String = "", numberingSystem!: String = "adlm", hour12!: Bool = false,
    weekday!: String = "long", era!: String = "long", year!: String = "numeric", month!: String = "numeric",
    day!: String = "numeric", hour!: String = "numeric", minute!: String = "numeric", second!: String = "numeric",
    timeZoneName!: String = "long", dayPeriod!: String = "long", localeMatcher!: String = "lookup",
    formatMatcher!: String = "basic")
```

**功能：** 构造一个DateTimeOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|否|"zh-Hans-CN"| **命名参数。** 区域参数， 如：zh-Hans-CN。|
|dateStyle|String|否|"long"| **命名参数。** 日期显示格式，取值包括："long", "short", "medium", "full", "auto"。|
|timeStyle|String|否|"long"| **命名参数。** 时间显示格式，取值包括："long", "short", "medium", "full", "auto"。|
|hourCycle|String|否|"h11"| **命名参数。** 时制格式，取值包括："h11", "h12", "h23", "h24"。|
|timeZone|String|否|""| **命名参数。** 使用的时区（合法的IANA时区ID）。|
|numberingSystem|String|否|"adlm"| **命名参数。** 数字系统，取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。|
|hour12|Bool|否|false| **命名参数。** 是否使用12小时制，若hour12和hourCycle未设置且系统24小时开关打开时，hour12属性的默认值为false。|
|weekday|String|否|"long"| **命名参数。** 工作日的显示格式，取值包括："long", "short", "narrow", "auto"。|
|era|String|否|"long"| **命名参数。** 时代的显示格式，取值包括："long", "short", "narrow", "auto"。|
|year|String|否|"numeric"| **命名参数。** 年份的显示格式，取值包括："numeric", "2-digit"。|
|month|String|否|"numeric"| **命名参数。** 月份的显示格式，取值包括："numeric", "2-digit", "long", "short", "narrow", "auto"。|
|day|String|否|"numeric"| **命名参数。** 日期的显示格式，取值包括："numeric", "2-digit"。|
|hour|String|否|"numeric"| **命名参数。** 小时的显示格式，取值包括："numeric", "2-digit"。|
|minute|String|否|"numeric"| **命名参数。** 分钟的显示格式，取值包括："numeric", "2-digit"。|
|second|String|否|"numeric"| **命名参数。** 秒钟的显示格式，取值包括："numeric", "2-digit"。|
|timeZoneName|String|否|"long"| **命名参数。** 时区名称的本地化表示, 取值包括："long", "short", "auto"。|
|dayPeriod|String|否|"long"| **命名参数。** 时段的显示格式，取值包括："long", "short", "narrow", "auto"。|
|localeMatcher|String|否|"lookup"| **命名参数。** 要使用的区域匹配算法，取值包括：<br/>"lookup"：精确匹配；<br/>"best fit"：最佳匹配。|
|formatMatcher|String|否|"basic"| **命名参数。** 要使用的格式匹配算法，取值包括：<br/>"basic"：精确匹配；<br/>"best fit"：最佳匹配。|