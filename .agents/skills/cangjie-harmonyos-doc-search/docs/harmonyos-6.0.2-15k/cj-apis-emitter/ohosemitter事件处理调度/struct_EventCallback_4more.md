## struct EventCallback

```cangjie
public struct EventCallback {
    public EventCallback(
        public let name: String,
        public let callback: (EventData) -> Unit
    )
}
```

**功能：** 订阅的回调函数。拥有相同name的回调函数会被认为是同一个回调函数，用户在使用时需要保证name的唯一性。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### let callback

```cangjie
public let callback: (EventData) -> Unit
```

**功能：** 回调函数。

**类型：** ([EventData](#struct-eventdata))->Unit

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 函数名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### EventCallback(String, (EventData) -> Unit)

```cangjie
public EventCallback(
        public let name: String,
        public let callback: (EventData) -> Unit
)
```

**功能：** EventCallback的构造函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|函数名称。|
|callback|([EventData](#struct-eventdata))->Unit|是|-|回调函数。|

## struct EventData

```cangjie
public struct EventData {
    public EventData(
        public var data: HashMap<String, EventDataType>
    )
}
```

**功能：** 发送事件时传递的数据。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### var data

```cangjie
public var data: HashMap<String, EventDataType>
```

**功能：** 传递的数据。

**类型：** HashMap\<String, [EventDataType](#enum-eventdatatype)>

**读写能力：** 可读写

**起始版本：** 12

### EventData(HashMap\<String, EventDataType>)

```cangjie
public EventData(
    public var data: HashMap<String, EventDataType>
)
```

**功能：** EventData的构造函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|HashMap\<String, [EventDataType](#enum-eventdatatype)>|是|-|发送事件时传递的数据。|

## struct Options

```cangjie
public struct Options {
    public Options(
        public var priority: EventPriority
    )
}
```

**功能：** 发送事件的优先级。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### var priority

```cangjie
public var priority: EventPriority
```

**功能：** 事件的优先级。

**类型：** [EventPriority](#enum-eventpriority)

**读写能力：** 可读写

**起始版本：** 12

### Options(EventPriority)

```cangjie
public Options(
    public var priority: EventPriority
)
```

**功能：** Options的构造函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|priority|[EventPriority](#enum-eventpriority)|是|-|事件的优先级。|

## enum EventDataType

```cangjie
public enum EventDataType {
    | INT64(Int64)
    | BOOL(Bool)
    | STRING(String)
    | ...
}
```

**功能：** 发送事件时传递的数据类型。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** Bool类型的数据。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### INT64(Int64)

```cangjie
INT64(Int64)
```

**功能：** Int64类型的数据。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### STRING(String)

```cangjie
STRING(String)
```

**功能：** String类型的数据。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12