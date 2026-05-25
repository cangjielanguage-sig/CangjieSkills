## struct Parameters

```cangjie
public struct Parameters {
    public Parameters(
        public let key: String,
        public let value: ValueType
    )
}
```

**功能：** [AppEventInfo](#struct-appeventinfo)的事件参数对象。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let key

```cangjie
public let key: String
```

**功能：** 事件参数名，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let value

```cangjie
public let value: ValueType
```

**功能：** 事件参数值，String类型参数长度需在8*1024个字符以内，Array中元素个数需在100以内，超出会做丢弃处理。

**类型：** [ValueType](#enum-valuetype)

**读写能力：** 只读

**起始版本：** 12

### Parameters(String, ValueType)

```cangjie
public Parameters(
    public let key: String,
    public let value: ValueType
)
```

**功能：** 创建[Parameters](#struct-parameters)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|事件参数名，首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。|
|value|[ValueType](#enum-valuetype)|是|-|事件参数值，String类型参数长度需在8*1024个字符以内，Array中元素个数需在100以内，超出会做丢弃处理。|

## struct TriggerCondition

```cangjie
public struct TriggerCondition {
    public let row: Int32
    public let size: Int32
    public let timeOut: Int32
    public init(row!: Int32 = 0, size!: Int32 = 0, timeOut!: Int32 = 0)
}
```

**功能：** 提供了回调触发条件的参数选项，只要满足任一条件就会触发订阅回调。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let row

```cangjie
public let row: Int32
```

**功能：** 满足触发回调的事件总数量，正整数。默认值0，不触发回调。传入负值时，会被置为默认值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let size

```cangjie
public let size: Int32
```

**功能：** 满足触发回调的事件总大小，正整数，单位为byte。默认值0，不触发回调。传入负值时，会被置为默认值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let timeOut

```cangjie
public let timeOut: Int32
```

**功能：** 满足触发回调的超时时长，正整数，单位为30s。默认值0，不触发回调。传入负值时，会被置为默认值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### init(Int32, Int32, Int32)

```cangjie
public init(row!: Int32 = 0, size!: Int32 = 0, timeOut!: Int32 = 0)
```

**功能：** 创建[TriggerCondition](#struct-triggercondition)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|row|Int32|否|0| **命名参数。** 满足触发回调的事件总数量，正整数。默认值0，不触发回调。传入负值时，会被置为默认值。|
|size|Int32|否|0| **命名参数。** 满足触发回调的事件总大小，正整数，单位为byte。默认值0，不触发回调。传入负值时，会被置为默认值。|
|timeOut|Int32|否|0| **命名参数。** 满足触发回调的超时时长，正整数，单位为30s。默认值0，不触发回调。传入负值时，会被置为默认值。|