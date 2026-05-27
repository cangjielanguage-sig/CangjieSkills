## struct LocaleOptions

```cangjie
public struct LocaleOptions {
    public LocaleOptions(
        public var calendar!: String = "",
        public var collation!: String = "",
        public var hourCycle!: String = "",
        public var numberingSystem!: String = "",
        public var numeric!: Bool = false,
        public var caseFirst!: String = ""
    )
}
```

**功能：** 区域初始化选项。LocaleOptions属性为可选。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var calendar

```cangjie
public var calendar: String = ""
```

**功能：** 日历参数，取值包括："buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var caseFirst

```cangjie
public var caseFirst: String = ""
```

**功能：** 表示大写、小写的排序顺序，取值范围："upper", "lower", "false"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var collation

```cangjie
public var collation: String = ""
```

**功能：** 排序参数，取值包括："big5han", "compat", "dict", "direct", "ducet", "emoji", "eor", "gb2312", "phonebk", "phonetic", "pinyin", "reformed ", "search", "searchjl", "standard", "stroke", "trad", "unihan", "zhuyin"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var hourCycle

```cangjie
public var hourCycle: String = ""
```

**功能：** 时制格式，取值包括："h11", "h12", "h23", "h24"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numberingSystem

```cangjie
public var numberingSystem: String = ""
```

**功能：** 数字系统，取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numeric

```cangjie
public var numeric: Bool = false
```

**功能：** 是否使用12小时制。默认值：false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19