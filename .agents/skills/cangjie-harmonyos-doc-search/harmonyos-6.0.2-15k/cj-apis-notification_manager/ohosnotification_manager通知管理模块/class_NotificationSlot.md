## class NotificationSlot

```cangjie
public class NotificationSlot {
    public var notificationType: SlotType
    public var level: SlotLevel
    public var desc: String
    public var badgeFlag: Bool
    public var bypassDnd: Bool
    public var lockscreenVisibility: Int32
    public var vibrationEnabled: Bool
    public var sound: String
    public var lightEnabled: Bool
    public var lightColor: Int32
    public let enabled: Bool
    public var vibrationValues: Array<Int64> = []
}
```

**功能：** 描述通知槽。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### var badgeFlag

```cangjie
public var badgeFlag: Bool
```

**功能：** 是否显示角标。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var bypassDnd

```cangjie
public var bypassDnd: Bool
```

**功能：** 是否在系统中绕过免打扰模式。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var desc

```cangjie
public var desc: String
```

**功能：** 通知渠道描述信息。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var level

```cangjie
public var level: SlotLevel
```

**功能：** 通知级别。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [SlotLevel](#enum-slotlevel)

**读写能力：** 可读写

**起始版本：** 19

### var lightColor

```cangjie
public var lightColor: Int32
```

**功能：** 通知灯颜色。预留能力，暂不支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var lightEnabled

```cangjie
public var lightEnabled: Bool
```

**功能：** 是否闪灯。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var lockscreenVisibility

```cangjie
public var lockscreenVisibility: Int32
```

**功能：** 在锁定屏幕上显示通知的模式。预留能力，暂不支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var notificationType

```cangjie
public var notificationType: SlotType
```

**功能：** 通道类型。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [SlotType](#enum-slottype)

**读写能力：** 可读写

**起始版本：** 19

### var sound

```cangjie
public var sound: String
```

**功能：** 通知提示音。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var vibrationEnabled

```cangjie
public var vibrationEnabled: Bool
```

**功能：** 是否可振动。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var vibrationValues

```cangjie
public var vibrationValues: Array<Int64> = []
```

**功能：** 通知振动样式。预留能力，暂不支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Array\<Int64>

**读写能力：** 可读写

**起始版本：** 19

### let enabled

```cangjie
public let enabled: Bool
```

**功能：** 此通知插槽中的启停状态。true表示使能；false表示禁止。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19