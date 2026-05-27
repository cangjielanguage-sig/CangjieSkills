## class NotificationRequest

```cangjie
public class NotificationRequest {
    public var content: NotificationContent
    public var id: Int32 = 0
    public var notificationSlotType: SlotType = OTHER_TYPES
    public var isOngoing: Bool = false
    public var isUnremovable: Bool = false
    public var deliveryTime: Int64 = 0
    public var tapDismissed: Bool = true
    public var autoDeletedTime: Int64 = -1
    public var color: UInt32 = 0
    public var colorEnabled: Bool = false
    public var isAlertOnce: Bool = false
    public var isStopwatch: Bool = false
    public var isCountDown: Bool = false
    public var isFloatingIcon: Bool = false
    public var label: String = ""
    public var badgeIconStyle: Int32 = 0
    public var showDeliveryTime: Bool = false
    public var smallIcon: Option<PixelMap> = None
    public var largeIcon: Option<PixelMap> = None
    public let creatorBundleName: String
    public let creatorUid: Int32
    public let creatorPid: Int32
    public let creatorUserId: Int32
    public let hashCode: String
    public var groupName: String = ""
    public var distributedOption: Option<DistributedOptions> = None
    public let notificationFlags: Option<NotificationFlags>
    public var badgeNumber: UInt32 = 0
    public var appMessageId: String = ""

    public init(
        content: NotificationContent,
        id!: Int32 = 0,
        label!: String = ""
    )

    public init(
        content: NotificationContent,
        creatorBundleName: String,
        creatorUid: Int32,
        creatorPid: Int32,
        creatorUserId: Int32,
        hashCode: String,
        notificationFlags: ?NotificationFlags
    )
}
```

**功能：** 描述通知的请求。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### var appMessageId

```cangjie
public var appMessageId: String = ""
```

**功能：** 应用发送通知携带的唯一标识字段, 用于通知去重。如果同一应用通过本地和云端等不同途径发布携带相同appMessageId的通知，设备只展示一条消息，之后收到的重复通知会被静默去重，不展示、不提醒。去重标识仅在通知发布的24小时内有效，超过24小时或者设备重启失效。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var autoDeletedTime

```cangjie
public var autoDeletedTime: Int64 = -1
```

**功能：** 自动清除的时间。数据格式：时间戳。单位：ms。例如，希望某通知存留3秒（3000ms）后对其进行清除，则对应的清除时间为：new Date().getTime() + 3000。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var badgeIconStyle

```cangjie
public var badgeIconStyle: Int32 = 0
```

**功能：** 通知角标类型。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var badgeNumber

```cangjie
public var badgeNumber: UInt32 = 0
```

**功能：** 应用程序图标上显示的通知数。当角标设定个数取值0时，表示清除角标。取值大于99时，通知角标将显示99+。

**系统能力：** SystemCapability.Notification.Notification

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var color

```cangjie
public var color: UInt32 = 0
```

**功能：** 通知背景颜色。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var colorEnabled

```cangjie
public var colorEnabled: Bool = false
```

**功能：** 通知背景颜色是否使能。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var content

```cangjie
public var content: NotificationContent
```

**功能：** 通知内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [NotificationContent](#class-notificationcontent)

**读写能力：** 可读写

**起始版本：** 12