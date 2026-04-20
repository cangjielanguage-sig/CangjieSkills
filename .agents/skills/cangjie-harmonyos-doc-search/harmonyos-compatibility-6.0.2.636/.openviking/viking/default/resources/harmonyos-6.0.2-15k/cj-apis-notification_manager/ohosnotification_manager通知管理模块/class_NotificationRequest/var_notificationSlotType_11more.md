### var notificationSlotType

```cangjie
public var notificationSlotType: SlotType = OTHER_TYPES
```

**功能：** 通知渠道类型，默认为OTHER_TYPES。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [SlotType](#enum-slottype)

**读写能力：** 可读写

**起始版本：** 19

### var showDeliveryTime

```cangjie
public var showDeliveryTime: Bool = false
```

**功能：** 是否显示分发时间。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var smallIcon

```cangjie
public var smallIcon: Option<PixelMap> = None
```

**功能：** 通知小图标。可选字段，图标像素的总字节数不超过192KB（图标像素的总字节数通过getPixelBytesNumber获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 19

### var tapDismissed

```cangjie
public var tapDismissed: Bool = true
```

**功能：** 通知是否自动清除。当通知携带wantAgent或actionButtons时该字段生效。默认值为true。

- true：点击通知或按钮后，自动删除当前通知。
- false：点击通知或按钮后，保留当前通知。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### let creatorBundleName

```cangjie
public let creatorBundleName: String = ""
```

**功能：** 创建通知的包名。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let creatorPid

```cangjie
public let creatorPid: Int32 = 0
```

**功能：** 创建通知的PID。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let creatorUid

```cangjie
public let creatorUid: Int32 = 0
```

**功能：** 创建通知的UID。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let creatorUserId

```cangjie
public let creatorUserId: Int32 = 0
```

**功能：** 创建通知的UserId。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let hashCode

```cangjie
public let hashCode: String = ""
```

**功能：** 通知唯一标识。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let notificationFlags

```cangjie
public let notificationFlags: Option<NotificationFlags> = None
```

**功能：** 获取NotificationFlags。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationFlags](#class-notificationflags)>

**读写能力：** 只读

**起始版本：** 19

### init(NotificationContent, Int32, String)

```cangjie
public init(
    content: NotificationContent,
    id!: Int32 = 0,
    label!: String = ""
)
```

**功能：** 构造描述通知的请求实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[NotificationContent](#class-notificationcontent)|是|-|通知内容。|
|id|Int32|否|0| **命名参数。** 通知ID，默认为0。|
|label|String|否|""| **命名参数。** 通知标签。|