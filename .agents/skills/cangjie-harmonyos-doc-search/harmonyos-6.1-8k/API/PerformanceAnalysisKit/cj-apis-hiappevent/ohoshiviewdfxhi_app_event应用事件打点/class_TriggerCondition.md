## class TriggerCondition

```cangjie
public class TriggerCondition {
    public var row: Int32
    public var size: Int32
    public var timeOut: Int32
    public init(row!: Int32 = 0, size!: Int32 = 0, timeOut!: Int32 = 0)
}
```

**功能：** 提供设置[Watcher](#class-watcher)的onTrigger回调触发条件的参数选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var row

```cangjie
public var row: Int32
```

**功能：** 满足触发回调的事件总数量，正整数。设置为0，不触发回调。传入负值时，会被置为0。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var size

```cangjie
public var size: Int32
```

**功能：** 满足触发回调的事件总大小，正整数，单位为byte。设置为0，不触发回调。传入负值时，会被置为0。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var timeOut

```cangjie
public var timeOut: Int32
```

**功能：** 满足触发回调的超时时长，正整数，单位为30s。设置为0，不触发回调。传入负值时，会被置为0。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### init(Int32, Int32, Int32)

```cangjie
public init(row!: Int32 = 0, size!: Int32 = 0, timeOut!: Int32 = 0)
```

**功能：** 创建[TriggerCondition](#class-triggercondition)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|row|Int32|否|0|**命名参数。** 满足触发回调的事件总数量，正整数。默认值0，不触发回调。传入负值时，会被置为默认值。|
|size|Int32|否|0|**命名参数。** 满足触发回调的事件总大小，正整数，单位为byte。默认值0，不触发回调。传入负值时，会被置为默认值。|
|timeOut|Int32|否|0|**命名参数。** 满足触发回调的超时时长，正整数，单位为30s。默认值0，不触发回调。传入负值时，会被置为默认值。|