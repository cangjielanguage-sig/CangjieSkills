## class NotificationFlags

```cangjie
public class NotificationFlags {
    public NotificationFlags(
        public let soundEnabled!: NotificationFlagStatus = TYPE_NONE,
        public let vibrationEnabled!: NotificationFlagStatus = TYPE_NONE
    )
}
```

**功能：** 描述通知标志状态。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### let soundEnabled

```cangjie
public let soundEnabled: NotificationFlagStatus = TYPE_NONE
```

**功能：** 是否启用声音提示。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [NotificationFlagStatus](#enum-notificationflagstatus)

**读写能力：** 只读

**起始版本：** 19

### let vibrationEnabled

```cangjie
public let vibrationEnabled: NotificationFlagStatus = TYPE_NONE
```

**功能：** 是否启用振动提醒功能。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [NotificationFlagStatus](#enum-notificationflagstatus)

**读写能力：** 只读

**起始版本：** 19

### NotificationFlags(NotificationFlagStatus, NotificationFlagStatus)

```cangjie
public NotificationFlags(
    public let soundEnabled!: NotificationFlagStatus = TYPE_NONE,
    public let vibrationEnabled!: NotificationFlagStatus = TYPE_NONE
)
```

**功能：** 构造描述通知标志状态。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|soundEnabled|[NotificationFlagStatus](#enum-notificationflagstatus)|否|TYPE_NONE| **命名参数。** 是否启用声音提示。|
|vibrationEnabled|[NotificationFlagStatus](#enum-notificationflagstatus)|否|TYPE_NONE| **命名参数。** 是否启用振动提醒功能。|