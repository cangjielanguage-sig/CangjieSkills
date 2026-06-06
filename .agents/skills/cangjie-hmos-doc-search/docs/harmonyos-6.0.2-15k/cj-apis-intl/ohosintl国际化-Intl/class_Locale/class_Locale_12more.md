## class Locale

```cangjie
public class Locale {
    public init()
    public init(locale: String, options!: ?LocaleOptions = None)
}
```

**功能：** 区域对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### prop baseName

```cangjie
public prop baseName: String
```

**功能：** Locale的基本信息，由语言、脚本、国家或地区组成，如：zh-Hans-CN。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop calendar

```cangjie
public prop calendar: String
```

**功能：** 区域的日历信息，取值包括："buddhist", "chinese", "coptic","dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop caseFirst

```cangjie
public prop caseFirst: String
```

**功能：** 区域的排序规则是否考虑大小写，取值包括："upper", "lower", "false"。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop collation

```cangjie
public prop collation: String
```

**功能：** 区域的排序规则，取值包括："big5han", "compat", "dict", "direct", "ducet", "eor", "gb2312", "phonebk", "phonetic", "pinyin", "reformed", "searchjl", "stroke", "trad", "unihan", "zhuyin"。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop hourCycle

```cangjie
public prop hourCycle: String
```

**功能：** 区域的时制信息，取值包括："h12", "h23", "h11", "h24"。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop language

```cangjie
public prop language: String
```

**功能：** 与区域设置相关的语言，如：zh。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop numberingSystem

```cangjie
public prop numberingSystem: String
```

**功能：** 区域使用的数字系统，
取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop numeric

```cangjie
public prop numeric: Bool
```

**功能：** 是否对数字字符进行特殊的排序规则处理。默认值：false。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### prop region

```cangjie
public prop region: String
```

**功能：** 与区域设置相关的国家或地区，如：CN。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop script

```cangjie
public prop script: String
```

**功能：** 区域语言的书写方式（脚本），如：Hans。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建区域对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 默认构造函数使用系统当前locale创建
let locale = Locale()
// 返回系统当前locale
let localeID = locale.toString()
```