## struct AppEventFilter

```cangjie
public struct AppEventFilter {
    public let domain: String
    public let eventTypes: Array<EventType>
    public let names: Array<String>

    public init(domain: String, eventTypes!: Array<EventType> = [], names!: Array<String> = [])
}
```

**功能：** 提供了过滤应用事件的参数选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let domain

```cangjie
public let domain: String
```

**功能：** 需要订阅的事件领域。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let eventTypes

```cangjie
public let eventTypes: Array<EventType>
```

**功能：** 需要订阅的事件类型集合。

**类型：** Array\<[EventType](#enum-eventtype)>

**读写能力：** 只读

**起始版本：** 12

### let names

```cangjie
public let names: Array<String>
```

**功能：** 需要订阅的事件名称集合。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### init(String, Array\<EventType>, Array\<String>)

```cangjie
public init(domain: String, eventTypes!: Array<EventType> = [], names!: Array<String> = [])
```

**功能：** 创建[AppEventFilter](#struct-appeventfilter)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|是|-|需要订阅的事件领域。|
|eventTypes|Array\<[EventType](#enum-eventtype)>|否|[]| **命名参数。** 需要订阅的事件类型集合。|
|names|Array\<String>|否|[]| **命名参数。** 需要订阅的事件名称集合。|

## struct AppEventGroup

```cangjie
public struct AppEventGroup {
    public let name: String
    public let appEventInfos: Array<AppEventInfo>
    public init(name: String, appEventInfos: Array<AppEventInfo>)
}
```

**功能：** 提供了订阅返回的事件组的参数定义。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let appEventInfos

```cangjie
public let appEventInfos: Array<AppEventInfo>
```

**功能：** 事件对象集合。

**类型：** Array\<[AppEventInfo](#struct-appeventinfo)>

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 事件名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String, Array\<AppEventInfo>)

```cangjie
public init(name: String, appEventInfos: Array<AppEventInfo>)
```

**功能：** 创建[AppEventGroup](#struct-appeventgroup)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|事件名称。|
|appEventInfos|Array\<[AppEventInfo](#struct-appeventinfo)>|是|-|事件对象集合。|