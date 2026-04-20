## class AppEventFilter

```cangjie
public class AppEventFilter {
    public var domain: String
    public var eventTypes: Array<EventType>
    public var names: Array<String>
    public init(domain: String, eventTypes!: Array<EventType> = [], names!: Array<String> = [])
}
```

**功能：** 提供设置[Watcher](#class-watcher)的订阅过滤条件的参数选项。用于在事件观察者中设置事件过滤条件，确保只有满足过滤条件的事件才会被监听处理。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var domain

```cangjie
public var domain: String
```

**功能：** 需要订阅的事件领域。可以是系统事件领域（hiAppEvent.domain.OS）或开发者在使用[Write](#static-func-writeappeventinfo)接口时传入的自定义事件信息（[AppEventInfo](#class-appeventinfo)）中的事件领域。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var eventTypes

```cangjie
public var eventTypes: Array<EventType>
```

**功能：** 需要订阅的事件类型集合。

**类型：** Array\<[EventType](#enum-eventtype)>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var names

```cangjie
public var names: Array<String>
```

**功能：** 需要订阅的事件名称集合。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### init(String, Array\<EventType>, Array\<String>)

```cangjie
public init(domain: String, eventTypes!: Array<EventType> = [], names!: Array<String> = [])
```

**功能：** 创建[AppEventFilter](#class-appeventfilter)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|是|-|需要订阅的事件领域。可以是系统事件领域（hiAppEvent.domain.OS）或开发者在使用[Write](#static-func-writeappeventinfo)接口时传入的自定义事件信息（[AppEventInfo](#class-appeventinfo)）中的事件领域。|
|eventTypes|Array\<[EventType](#enum-eventtype)>|否|[]|**命名参数。** 需要订阅的事件类型集合。默认不进行过滤。|
|names|Array\<String>|否|[]|**命名参数。** 需要订阅的事件名称集合。默认不进行过滤。|