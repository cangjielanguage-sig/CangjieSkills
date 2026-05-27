|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|否|""| **命名参数。** 区域参数， 如："zh-Hans-CN"。locale属性默认值为系统当前Locale。|
|currency|String|否|""| **命名参数。** 货币单位， 取值符合ISO-4217标准，如："EUR", "CNY", "USD"等。支持三位数字代码，如："978"，"156"，"840"等。|
|currencySign|String|否|"standard"| **命名参数。** 货币单位的符号显示，取值包括： "standard", "accounting"。|
|currencyDisplay|String|否|"symbol"| **命名参数。** 货币的显示方式，取值包括："symbol", "narrowSymbol", "code", "name"。|
|unit|String|否|""| **命名参数。** 单位名称，如："meter", "inch", "hectare"等。|
|unitDispaly|String|否|"short"| **命名参数。** 单位的显示格式，取值包括："long", "short", "narrow"。|
|unitUsage|String|否|"default"| **命名参数。** 单位的使用场景，取值包括："default", "area-land-agricult", "area-land-commercl", "area-land-residntl", "length-person", "length-person-small", "length-rainfall", "length-road", "length-road-small", "length-snowfall", "length-vehicle", "length-visiblty", "length-visiblty-small", "length-person-informal", "length-person-small-informal", "length-road-informal", "speed-road-travel", "speed-wind", "temperature-person", "temperature-weather", "volume-vehicle-fuel", "elapsed-time-second", "size-file-byte", "size-shortfile-byte"。|
|signDisplay|String|否|"auto"| **命名参数。** 数字符号的显示格式，取值包括："auto", "never", "always", "expectZero"。|
|compactDisplay|String|否|"short"| **命名参数。** 紧凑型的显示格式，取值包括："long", "short"。|
|notation|String|否|"standard"| **命名参数。** 数字的格式化规格，取值包括："standard", "scientific", "engineering", "compact"。|
|localeMather|String|否|"best fit"| **命名参数。** 要使用的区域匹配算法，取值包括："lookup", "best fit"。|
|style|String|否|"decimal"| **命名参数。** 数字的显示格式，取值包括："decimal", "currency", "percent", "unit"。|
|numberingSystem|String|否|""| **命名参数。** 数字系统，取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。numberingSystem属性默认值为locale的默认数字系统。|
|useGrouping|Bool|否|false| **命名参数。** 是否分组显示。|
|minimumIntegerDigits|Int64|否|1| **命名参数。** 表示要使用的最小整数位数，取值范围：1~21。|
|minimumFractionDigits|Int64|否|0| **命名参数。** 表示要使用的最小分数位数，取值范围：0~20。|
|maximumFractionDigits|Int64|否|3| **命名参数。** 表示要使用的最大分数位数，取值范围：1~21。|
|minimumSignificantDigits|Int64|否|1| **命名参数。** 表示要使用的最低有效位数，取值范围：1~21。|
|maximumSignificantDigits|Int64|否|21| **命名参数。** 表示要使用的最大有效位数，取值范围：1~21。|

> **说明：**
>
> 各属性不同取值代表的含义或呈现效果，请参见[数字与度量衡国际化](../../../../Dev_Guide/internationalization/cj-i18n-numbers-weights-measures.md#数字与度量衡国际化)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*