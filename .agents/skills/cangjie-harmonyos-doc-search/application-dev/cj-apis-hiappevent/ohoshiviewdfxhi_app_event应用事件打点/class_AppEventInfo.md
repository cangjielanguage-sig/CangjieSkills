## class AppEventInfo

```cangjie
public class AppEventInfo {
    public var domain: String
    public var name: String
    public var eventType: EventType
    public var params: HashMap<String, EventValueType>
    public init(domain: String, name: String, event: EventType, params: HashMap<String, EventValueType>)
}
```

**功能：** 提供事件信息的参数选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var domain

```cangjie
public var domain: String
```

**功能：** 事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var eventType

```cangjie
public var eventType: EventType
```

**功能：** 事件类型。

**类型：** [EventType](#enum-eventtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var params

```cangjie
public var params: HashMap<String, EventValueType>
```

**功能：** 事件参数对象，包含每个事件参数的参数名和参数值。针对应用事件，[Write](#static-func-writeappeventinfo)打点写入的参数由开发者定义，其规格如下：

- 参数名为StringValue类型，首字符必须为字母字符或`$`字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName、\$123_name等。

- 参数值支持StringValue、IntValue、FloatValue、BoolValue、数组类型。StringValue类型参数长度需在8*1024个字符以内，超出后会和对应的参数名一同被丢弃；IntValue、FloatValue类型参数取值需在-(2^53 - 1)~2^53 - 1范围内，超出可能会产生不确定值；数组类型参数中的元素类型只能全为StringValue、IntValue、FloatValue、BoolValue中的一种，且元素个数需在100以内，超出部分即从第101个元素开始会被丢弃。

- 参数个数需在32个以内，超出的参数会做丢弃处理。

**类型：** HashMap\<String,[EventValueType](#enum-eventvaluetype)>

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### init(String, String, EventType, HashMap\<String,EventValueType>)

```cangjie
public init(domain: String, name: String, event: EventType, params: HashMap<String, EventValueType>)
```

**功能：** 创建[AppEventInfo](#class-appeventinfo)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|是|-|事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。|
|name|String|是|-|事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。|
|event|[EventType](#enum-eventtype)|是|-|事件类型。|
|params|HashMap\<String,[EventValueType](#enum-eventvaluetype)>|是|-|事件参数对象，包含每个事件参数的参数名和参数值。|