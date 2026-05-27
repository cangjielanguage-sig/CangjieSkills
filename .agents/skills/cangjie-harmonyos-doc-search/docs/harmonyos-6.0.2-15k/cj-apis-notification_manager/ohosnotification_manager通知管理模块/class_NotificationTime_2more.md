## class NotificationTime

```cangjie
public class NotificationTime {
    public NotificationTime(
        public var initialTime!: Int32 = 0,
        public var isCountDown!: Bool = false,
        public var isPaused!: Bool = false,
        public var isInTitle!: Bool = false
    )
}
```

**功能：** 描述通知时间。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### var initialTime

```cangjie
public var initialTime: Int32 = 0
```

**功能：** 起始时间。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var isCountDown

```cangjie
public var isCountDown: Bool = false
```

**功能：** 是否倒计时。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isInTitle

```cangjie
public var isInTitle: Bool = false
```

**功能：** 时间是否展示在title中。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isPaused

```cangjie
public var isPaused: Bool = false
```

**功能：** 是否暂停。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### NotificationTime(Int32, Bool, Bool, Bool)

```cangjie
public NotificationTime(
    public var initialTime!: Int32 = 0,
    public var isCountDown!: Bool = false,
    public var isPaused!: Bool = false,
    public var isInTitle!: Bool = false
)
```

**功能：** 构造描述通知时间实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|initialTime|Int32|否|0| **命名参数。** 起始时间。|
|isCountDown|Bool|否|false| **命名参数。** 是否倒计时。|
|isPaused|Bool|否|false| **命名参数。** 是否暂停。|
|isInTitle|Bool|否|false| **命名参数。** 时间是否展示在title中。|

## struct DistributedOptions

```cangjie
public struct DistributedOptions {
    public DistributedOptions(
        let isDistributed!: Bool = true,
        let supportDisplayDevices!: Array<String> = Array<String>(),
        let supportOperateDevices!: Array<String> = Array<String>()
    )
}
```

**功能：** 描述分布式选项。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### DistributedOptions(Bool, Array\<String>, Array\<String>)

```cangjie
public DistributedOptions(
    let isDistributed!: Bool = true,
    let supportDisplayDevices!: Array<String> = Array<String>(),
    let supportOperateDevices!: Array<String> = Array<String>()
)
```

**功能：** 构造描述分布式选项实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isDistributed|Bool|否|true| **命名参数。** 是否为分布式通知。|
|supportDisplayDevices|Array\<String>|否|Array\<String>()| **命名参数。** 可以同步通知到的设备列表。|
|supportOperateDevices|Array\<String>|否|Array\<String>()| **命名参数。** 可以打开通知的设备列表。|