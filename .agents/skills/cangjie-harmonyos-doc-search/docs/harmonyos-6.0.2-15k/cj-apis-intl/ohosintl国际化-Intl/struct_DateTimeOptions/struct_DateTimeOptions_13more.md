## struct DateTimeOptions

```cangjie
public struct DateTimeOptions {
    public DateTimeOptions(
        public var locale!: String = "",
        public var dateStyle!: String = "",
        public var timeStyle!: String = "",
        public var hourCycle!: String = "",
        public var timeZone!: String = "",
        public var numberingSystem!: String = "",
        public var hour12!: Bool = false,
        public var weekday!: String = "",
        public var era!: String = "",
        public var year!: String = "",
        public var month!: String = "",
        public var day!: String = "",
        public var hour!: String = "",
        public var minute!: String = "",
        public var second!: String = "",
        public var timeZoneName!: String = "",
        public var dayPeriod!: String = "",
        public var localeMatcher!: String = "",
        public var formatMatcher!: String = ""
    )
}
```

**功能：** 时间、日期格式化时可设置的配置项。DateTimeOptions的属性为可选。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var dateStyle

```cangjie
public var dateStyle: String = ""
```

**功能：** 日期显示格式，取值包括："long", "short", "medium", "full", "auto"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var day

```cangjie
public var day: String = ""
```

**功能：** 日期的显示格式，取值包括："numeric", "2-digit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var dayPeriod

```cangjie
public var dayPeriod: String = ""
```

**功能：** 时段的显示格式，取值包括："long", "short", "narrow", "auto"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var era

```cangjie
public var era: String = ""
```

**功能：** 时代的显示格式，取值包括："long", "short", "narrow", "auto"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var formatMatcher

```cangjie
public var formatMatcher: String = ""
```

**功能：** 要使用的格式匹配算法，取值包括："basic", "best fit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var hour

```cangjie
public var hour: String = ""
```

**功能：** 小时的显示格式，取值包括："numeric", "2-digit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var hour12

```cangjie
public var hour12: Bool = false
```

**功能：** 是否使用12小时制，若hour12和hourCycle未设置且系统24小时开关打开时，hour12属性的默认值为false。

**类型：** Bool

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

### var locale

```cangjie
public var locale: String = ""
```

**功能：** 区域参数， 如：zh-Hans-CN.

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var localeMatcher

```cangjie
public var localeMatcher: String = ""
```

**功能：** 要使用的区域匹配算法，取值包括："lookup", "best fit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var minute

```cangjie
public var minute: String = ""
```

**功能：** 分钟的显示格式，取值包括："numeric", "2-digit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var month

```cangjie
public var month: String = ""
```

**功能：** 月份的显示格式，取值包括："numeric", "2-digit", "long", "short", "narrow", "auto"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19