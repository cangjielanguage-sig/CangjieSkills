## struct AppEventInfo

```cangjie
public struct AppEventInfo {
    public AppEventInfo(
        public let domain: String,
        public let name: String,
        public let event: EventType,
        public let params: Array<Parameters>
    )
}
```

**功能：** 提供了应用事件信息的参数选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let domain

```cangjie
public let domain: String
```

**功能：** 事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let event

```cangjie
public let event: EventType
```

**功能：** 事件类型。

**类型：** [EventType](#enum-eventtype)

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let params

```cangjie
public let params: Array<Parameters>
```

**功能：** 事件参数对象，每个事件参数包括参数名和参数值，其规格定义如下：

参数名为String类型，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。

参数值支持String、Int32、Float64、Bool、数组类型，String类型参数长度需在8*1024个字符以内；数组类型参数中的元素类型只能全为String、Int32、Float64、Bool中的一种，且元素个数需在100以内。

参数个数需在32个以内。

**类型：** Array\<[Parameters](#struct-parameters)>

**读写能力：** 只读

**起始版本：** 12

### AppEventInfo(String, String, EventType, Array\<Parameters>)

```cangjie
public AppEventInfo(
    public let domain: String,
    public let name: String,
    public let event: EventType,
    public let params: Array<Parameters>
)
```

**功能：** 创建[AppEventInfo](#struct-appeventinfo)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|是|-|事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。|
|name|String|是|-|事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。|
|event|[EventType](#enum-eventtype)|是|-|事件类型。|
|params|Array\<[Parameters](#struct-parameters)>|是|-|事件参数对象，每个事件参数包括参数名和参数值，其规格定义如下：<br>- 参数名为String类型，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。<br>- 参数值支持String、Int32、Float64、Bool、数组类型，String类型参数长度需在8*1024个字符以内；数组类型参数中的元素类型只能全为String、Int32、Float64、Bool中的一种，且元素个数需在100以内。<br>- 参数个数需在32个以内。|