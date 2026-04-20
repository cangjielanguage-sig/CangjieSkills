## class Processor

```cangjie
public class Processor {
    public let name: String
    public let debugMode: Bool
    public let routeInfo: String
    public let appId: String
    public let onStartReport: Bool
    public let onBackgroundReport: Bool
    public let periodReport: Int64
    public let batchReport: Int64
    public let userIds: Array<String>
    public let userProperties: Array<String>
    public let eventConfigs: Array<AppEventReportConfig>
    public init(name: String, debugMode!: Bool = false, routeInfo!: String = "", appId!: String = "",
            onStartReport!: Bool = false, onBackgroundReport!: Bool = false, periodReport!: Int64 = 0, batchReport!: Int64 = 0,
            userIds!: Array<String> = [], userProperties!: Array<String> = [], eventConfigs!: Array<AppEventReportConfig> = [])
}
```

**功能：** 可以上报事件的数据处理者对象。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let appId

```cangjie
public let appId: String
```

**功能：** 应用id，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let batchReport

```cangjie
public let batchReport: Int64
```

**功能：** 事件上报阈值，当事件条数达到阈值时上报事件。传入数值必须大于0且小于1000，不在数值范围内会被置为默认值0，不进行上报。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let debugMode

```cangjie
public let debugMode: Bool
```

**功能：** 是否开启debug模式，默认值为false。配置值为true表示开启debug模式，false表示不开启debug模式。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let eventConfigs

```cangjie
public let eventConfigs: Array<AppEventReportConfig>
```

**功能：** 数据处理者可以上报的事件数组。

**类型：** Array\<[AppEventReportConfig](#struct-appeventreportconfig)>

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 数据处理者的名称。名称只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let onBackgroundReport

```cangjie
public let onBackgroundReport: Bool
```

**功能：** 当应用程序进入后台时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let onStartReport

```cangjie
public let onStartReport: Bool
```

**功能：** 数据处理者在启动时是否上报事件，默认值为false。配置值为true表示上报事件，false表示不上报事件。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let periodReport

```cangjie
public let periodReport: Int64
```

**功能：** 事件定时上报时间周期，单位为秒。传入数值必须大于或等于0，小于0时会被置为默认值0，不进行定时上报。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### let routeInfo

```cangjie
public let routeInfo: String
```

**功能：** 服务器位置信息，默认为空字符串。传入字符串长度不能超过8KB，超过时会被置为默认值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let userIds

```cangjie
public let userIds: Array<String>
```

**功能：** 数据处理者可以上报的用户ID的name数组。name对应[setUserId](#static-func-setuseridstring-string)接口的name参数。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let userProperties

```cangjie
public let userProperties: Array<String>
```

**功能：** 数据处理者可以上报的用户属性的name数组。name对应[setUserProperty](#static-func-setuserpropertystring-string)接口的name参数。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12