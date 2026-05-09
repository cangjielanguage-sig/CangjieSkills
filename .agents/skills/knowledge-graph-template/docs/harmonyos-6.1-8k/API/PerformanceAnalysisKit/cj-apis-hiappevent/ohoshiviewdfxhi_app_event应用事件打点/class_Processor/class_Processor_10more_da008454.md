## class Processor

```cangjie
public class Processor {
    public var name: String
    public var debugMode: Bool
    public var routeInfo: String
    public var appId: String
    public var onStartReport: Bool
    public var onBackgroundReport: Bool
    public var periodReport: Int32
    public var batchReport: Int32
    public var userIds: Array<String>
    public var userProperties: Array<String>
    public var eventConfigs: Array<AppEventReportConfig>
    public init(name: String, debugMode!: Bool = false, routeInfo!: String = "", appId!: String = "",
        onStartReport!: Bool = false, onBackgroundReport!: Bool = false, periodReport!: Int32 = 0,
        batchReport!: Int32 = 0, userIds!: Array<String> = [], userProperties!: Array<String> = [],
        eventConfigs!: Array<AppEventReportConfig> = [])
}
```

**功能：** 可以上报事件的数据处理者对象。用于事件的上报和管理，开发者可自定义数据处理配置，满足不同的数据处理需求。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var appId

```cangjie
public var appId: String
```

**功能：** 应用id。传入字符串长度不能超过8KB，超过时会被置为空字符串。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var batchReport

```cangjie
public var batchReport: Int32
```

**功能：** 事件上报阈值，当事件条数达到阈值时上报事件。传入数值必须大于0且小于1000，不在数值范围内会被置为0，不进行上报。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var debugMode

```cangjie
public var debugMode: Bool
```

**功能：** 是否开启debug模式。配置值为true表示开启debug模式，false表示不开启debug模式。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var eventConfigs

```cangjie
public var eventConfigs: Array<AppEventReportConfig>
```

**功能：** 数据处理者配置id。传入数值必须大于或等于0，小于0时会被置为0。传入的值大于0时，与数据处理者的名称name共同唯一标识数据处理者。

**类型：** Array\<[AppEventReportConfig](#class-appeventreportconfig)>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 数据处理者的名称。名称只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var onBackgroundReport

```cangjie
public var onBackgroundReport: Bool
```

**功能：** 当应用程序进入后台时是否上报事件。配置值为true表示上报事件，false表示不上报事件。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var onStartReport

```cangjie
public var onStartReport: Bool
```

**功能：** 数据处理者在启动时是否上报事件。配置值为true表示上报事件，false表示不上报事件。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var periodReport

```cangjie
public var periodReport: Int32
```

**功能：** 事件定时上报时间周期，单位为秒。传入数值必须大于或等于0，小于0时会被置为0，不进行定时上报。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var routeInfo

```cangjie
public var routeInfo: String
```

**功能：** 服务器位置信息。传入字符串长度不能超过8KB，超过时会被置为空字符串。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22