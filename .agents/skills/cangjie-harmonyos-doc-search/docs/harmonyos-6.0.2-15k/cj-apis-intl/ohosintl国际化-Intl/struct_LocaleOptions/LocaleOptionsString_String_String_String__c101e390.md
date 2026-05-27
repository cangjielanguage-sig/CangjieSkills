### LocaleOptions(String, String, String, String, Bool, String)

```cangjie
public LocaleOptions(
    public var calendar!: String = "",
    public var collation!: String = "",
    public var hourCycle!: String = "",
    public var numberingSystem!: String = "",
    public var numeric!: Bool = false,
    public var caseFirst!: String = ""
)
```

**功能：** 构建区域初始化选项的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|calendar|String|否|""| **命名参数。** 日历参数，取值包括："buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。|
|collation|String|否|""| **命名参数。** 排序参数，取值包括："big5han", "compat", "dict", "direct", "ducet", "emoji", "eor", "gb2312", "phonebk", "phonetic", "pinyin", "reformed ", "search", "searchjl", "standard", "stroke", "trad", "unihan", "zhuyin"。|
|hourCycle|String|否|""| **命名参数。** 时制格式，取值包括："h11", "h12", "h23", "h24"。|
|numberingSystem|String|否|""| **命名参数。** 数字系统，取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。|
|numeric|Bool|否|false| **命名参数。** 是否使用12小时制。默认值：false。|
|caseFirst|String|否|""| **命名参数。** 表示大写、小写的排序顺序，取值范围："upper", "lower", "false"。|

> **说明：**
>
>calendar：不同取值表示的含义请参见[设置日历和历法表1](../../../../Dev_Guide/internationalization/cj-i18n-calendar.md)。
>hourCycle：不同取值的显示效果请参见[时间日期国际化表5](../../../../Dev_Guide/internationalization/cj-i18n-time-date.md)。
>collation、caseFirst：不同取值表示的含义请参见[本地习惯排序表1](../../../../Dev_Guide/internationalization/cj-i18n-sorting-local.md)。