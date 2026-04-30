## class CalendarAccount

```cangjie
public class CalendarAccount {
    public CalendarAccount(
        public let name: String,
        public var `type`: CalendarType,
        public var displayName!: String = ""
    )
}
```

**功能：** 日历账户信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var \`type\`

```cangjie
public var `type`: CalendarType
```

**功能：** 账户类型。

**类型：** [CalendarType](#enum-calendartype)

**读写能力：** 可读写

**起始版本：** 20

### var displayName

```cangjie
public var displayName: String = ""
```

**功能：** 账户显示在日历应用上的名称（面向用户）。不填时，默认为空字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### let name

```cangjie
public let name: String
```

**功能：** 账户名称（面向开发者）。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### CalendarAccount(String, CalendarType, String)

```cangjie
public CalendarAccount(
    public let name: String,
    public var `type`: CalendarType,
    public var displayName!: String = ""
)
```

**功能：** 构造CalendarAccount对象。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|账户名称（面向开发者）。|
|\`type\`|[CalendarType](#enum-calendartype)|是|-|账户类型。|
|displayName|String|否|""|账户显示在日历应用上的名称（面向用户）。不填时，默认为空字符串。|

## class CalendarConfig

```cangjie
public class CalendarConfig {
    public CalendarConfig(
        public var enableReminder!: Bool = false,
        public var color!: Color = Color(0x0a59f7)
    )
}
```

**功能：** 日历配置信息。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var color

```cangjie
public var color!: Color = Color(0x0a59f7)
```

**功能：** 设置Calendar颜色。不填时，默认值为0x0a59f7。

**类型：** ?Color

**读写能力：** 可读写

**起始版本：** 20

### var enableReminder

```cangjie
public var enableReminder!: Bool = false
```

**功能：** 是否打开Calendar下所有Event提醒能力。当取值为true时，该Calendar下所有Event具备提醒能力；当取值为false时，不具备提醒能力，默认具备提醒能力。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 20

### CalendarConfig(?Bool, ?Color)

```cangjie
public CalendarConfig(
    public var enableReminder!: Bool = false,
    public var color!: Color = Color(0x0a59f7)
)
```

**功能：** 构造CalendarConfig对象。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enableReminder|Bool|否|false|是否打开Calendar下所有Event提醒能力。当取值为true时，该Calendar下所有Event具备提醒能力；当取值为false时，不具备提醒能力，默认具备提醒能力。|
|color|Color|否|Color(0x0a59f7)|设置Calendar颜色。不填时，默认值为0x0a59f7。|