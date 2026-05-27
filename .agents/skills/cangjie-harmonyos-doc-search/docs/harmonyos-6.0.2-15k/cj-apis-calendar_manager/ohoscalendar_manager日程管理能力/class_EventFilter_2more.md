## class EventFilter

```cangjie
public class EventFilter {}
```

**功能：** 日程过滤器，查询日程时进行筛选过滤，获取符合条件的日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### static func filterById(Array\<Int64>)

```cangjie
public static func filterById(ids: Array<Int64>): EventFilter
```

**功能：** 根据日程id过滤日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ids|Array\<Int64>|是|-|日程id数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[EventFilter](#class-eventfilter)|返回日程过滤器对象。|

### static func filterByTime(Int64, Int64)

```cangjie
public static func filterByTime(start: Int64, end: Int64): EventFilter
```

**功能：** 根据日程时间过滤日程。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int64|是|-|开始时间。|
|end|Int64|是|-|结束时间。|

**返回值：**

|类型|说明|
|:----|:----|
|[EventFilter](#class-eventfilter)|返回日程过滤器对象。|

### static func filterByTitle(String)

```cangjie
public static func filterByTitle(title: String): EventFilter
```

**功能：** 根据日程标题过滤日程，该条件为模糊匹配。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|日程标题。|

**返回值：**

|类型|说明|
|:----|:----|
|[EventFilter](#class-eventfilter)|返回日程过滤器对象。|

## class EventService

```cangjie
public class EventService {
    public EventService(
        public var `type`: ServiceType,
        public var uri: String,
        public var description!: ?String = ""
    )
}
```

**功能：** 日程服务。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var \`type\`

```cangjie
public var `type`: ServiceType
```

**功能：** 服务类型。

**类型：** [ServiceType](#enum-servicetype)

**读写能力：** 可读写

**起始版本：** 20

### var description

```cangjie
public var description: ?String = ""
```

**功能：** 服务辅助描述。不填时，默认为空字符串。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 20

### var uri

```cangjie
public var uri: String
```

**功能：** 服务的uri，格式为Deeplink类型。可以跳转到三方应用相应界面。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### EventService(ServiceType, String, ?String)

```cangjie
public EventService(
    public var `type`: ServiceType,
    public var uri: String,
    public var description!: ?String = ""
)
```

**功能：** 构造EventService对象。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ServiceType](#enum-servicetype)|是|-|服务类型。|
|uri|String|是|-|服务的uri，格式为Deeplink类型。可以跳转到三方应用相应界面。|
|description|?String|否|""|服务辅助描述。不填时，默认为空字符串。|