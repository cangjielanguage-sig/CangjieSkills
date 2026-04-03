### class DateTimeOptions

```cangjie
public class DateTimeOptions {
    public var locale: ?String
    public var dateStyle: ?String
    public var timeStyle: ?String
    public var hourCycle: ?String
    public var timeZone: ?String
    public var numberingSystem: ?String
    public var hour12: ?Bool
    public var weekday: ?String
    public var era: ?String
    public var year: ?String
    public var month: ?String
    public var day: ?String
    public var hour: ?String
    public var minute: ?String
    public var second: ?String
    public var timeZoneName: ?String
    public var dayPeriod: ?String
    public var localeMatcher: ?String
    public var formatMatcher: ?String
    public init(locale!: ?String = None, dateStyle!: ?String = None, timeStyle!: ?String = None,
    hourCycle!: ?String = None, timeZone!: ?String = None, numberingSystem!: ?String = None, hour12!: ?Bool = None,
    weekday!: ?String = None, era!: ?String = None, year!: ?String = None, month!: ?String = None,
    day!: ?String = None, hour!: ?String = None, minute!: ?String = None, second!: ?String = None,
    timeZoneName!: ?String = None, dayPeriod!: ?String = None, localeMatcher!: ?String = None,
    formatMatcher!: ?String = None)
}
```

**功能：** 定义DateTimeOptions对象的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var dateStyle

```cangjie
public var dateStyle: ?String
```

**功能：** 日期显示格式。值可以是："long"、"short"、"medium"、"full"或"auto"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var day

```cangjie
public var day: ?String
```

**功能：** 天显示格式。值可以是："numeric"或"2-digit"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var dayPeriod

```cangjie
public var dayPeriod: ?String
```

**功能：** 时间段显示格式。值可以是："long"、"short"、"narrow"或"auto"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var era

```cangjie
public var era: ?String
```

**功能：** 纪元显示格式。值可以是："long"、"short"、"narrow"或"auto"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var formatMatcher

```cangjie
public var formatMatcher: ?String
```

**功能：** 格式匹配算法。值可以是："basic"（精确匹配）或"best fit"（最佳匹配）。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var hour

```cangjie
public var hour: ?String
```

**功能：** 小时显示格式。值可以是："numeric"或"2-digit"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var hour12

```cangjie
public var hour12: ?Bool
```

**功能：** 是否使用12小时制。值true表示使用12小时制，false表示相反。如果同时设置了hour12和hourCycle，则hourCycle不生效。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var hourCycle

```cangjie
public var hourCycle: ?String
```

**功能：** 小时周期。值可以是："h11"、"h12"、"h23"或"h24"。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var locale

```cangjie
public var locale: ?String
```

**功能：** 有效的区域设置ID，例如"zh-Hans-CN"。默认值为当前系统区域设置。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var localeMatcher

```cangjie
public var localeMatcher: ?String
```

**功能：** 区域设置匹配算法。值可以是："lookup"（精确匹配）或"best fit"（最佳匹配）。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22