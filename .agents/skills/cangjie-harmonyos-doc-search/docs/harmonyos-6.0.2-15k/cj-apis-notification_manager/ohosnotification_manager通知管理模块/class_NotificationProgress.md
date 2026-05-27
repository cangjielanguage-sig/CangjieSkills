## class NotificationProgress

```cangjie
public class NotificationProgress {
    public NotificationProgress(
        public var maxValue!: Int32 = 0,
        public var currentValue!: Int32 = 0,
        public var isPercentage!: Bool = false
    )
}
```

**功能：** 描述通知进度。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### var currentValue

```cangjie
public var currentValue: Int32 = 0
```

**功能：** 进度当前值。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var isPercentage

```cangjie
public var isPercentage: Bool = false
```

**功能：** 是否按百分比展示。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var maxValue

```cangjie
public var maxValue: Int32 = 0
```

**功能：** 进度最大值。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### NotificationProgress(Int32, Int32, Bool)

```cangjie
public NotificationProgress(
    public var maxValue!: Int32 = 0,
    public var currentValue!: Int32 = 0,
    public var isPercentage!: Bool = false
)
```

**功能：** 构造描述通知进度实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxValue|Int32|否|0| **命名参数。** 进度最大值。|
|currentValue|Int32|否|0| **命名参数。** 进度当前值。|
|isPercentage|Bool|否|false| **命名参数。** 是否按百分比展示。|