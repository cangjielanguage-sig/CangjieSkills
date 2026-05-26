### var deliveryTime

```cangjie
public var deliveryTime: Int64 = 0
```

**功能：** 通知发送时间。系统自动生成，无需开发者配置。数据格式：时间戳。单位：ms。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var distributedOption

```cangjie
public var distributedOption: Option<DistributedOptions> = None
```

**功能：** 分布式通知的选项。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[DistributedOptions](#struct-distributedoptions)>

**读写能力：** 可读写

**起始版本：** 19

### var groupName

```cangjie
public var groupName: String = ""
```

**功能：** 组通知名称。默认为空。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var id

```cangjie
public var id: Int32 = 0
```

**功能：** 通知ID，默认为0。当相同通知ID存在时，将更新该通知的内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var isAlertOnce

```cangjie
public var isAlertOnce: Bool = false
```

**功能：** 发布或更新该通知时，是否只进行一次通知提醒，默认为false。

- true：仅首次发布通知时进行提醒，后续更新该通知时，提醒方式变更为LEVEL_MIN。
- false：每次均按照配置的通知提醒方式进行提醒。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isCountDown

```cangjie
public var isCountDown: Bool = false
```

**功能：** 是否显示倒计时时间。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isFloatingIcon

```cangjie
public var isFloatingIcon: Bool = false
```

**功能：** 是否显示状态栏图标。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isOngoing

```cangjie
public var isOngoing: Bool = false
```

**功能：** 预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isStopwatch

```cangjie
public var isStopwatch: Bool = false
```

**功能：** 是否显示已用时间。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var isUnremovable

```cangjie
public var isUnremovable: Bool = false
```

**功能：** 预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var label

```cangjie
public var label: String = ""
```

**功能：** 通知标签。label字段的功能类似于id，可以单独使用，也可与id结合共同作为通知的标识。优先推荐使用id。如果发布通知时label不为空，那么在更新或删除该通知时，也需要指定相应的label。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var largeIcon

```cangjie
public var largeIcon: Option<PixelMap> = None
```

**功能：** 通知大图标。可选字段，图标像素的总字节数不超过192KB（图标像素的总字节数通过getPixelBytesNumber获取），建议图标像素长宽为128*128。实际显示效果依赖于设备能力和通知中心UI样式。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 19