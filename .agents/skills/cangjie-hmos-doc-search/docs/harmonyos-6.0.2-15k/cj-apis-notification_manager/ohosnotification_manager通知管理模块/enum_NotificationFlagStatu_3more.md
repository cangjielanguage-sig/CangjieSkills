## enum NotificationFlagStatus

```cangjie
public enum NotificationFlagStatus {
    | TYPE_NONE
    | TYPE_OPEN
    | TYPE_CLOSE
    | ...
}
```

**功能：** 描述通知标志状态。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### TYPE_CLOSE

```cangjie
TYPE_CLOSE
```

**功能：** 通知标志关闭。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### TYPE_NONE

```cangjie
TYPE_NONE
```

**功能：** 默认标志，效果等同于打开。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### TYPE_OPEN

```cangjie
TYPE_OPEN
```

**功能：** 通知标志打开。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

## enum SlotLevel

```cangjie
public enum SlotLevel {
    | LEVEL_NONE
    | LEVEL_MIN
    | LEVEL_LOW
    | LEVEL_DEFAULT
    | LEVEL_HIGH
    | ...
}
```

**功能：** 通知级别。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LEVEL_DEFAULT

```cangjie
LEVEL_DEFAULT
```

**功能：** 表示关闭通知功能。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LEVEL_HIGH

```cangjie
LEVEL_HIGH
```

**功能：** 表示通知功能已启用，状态栏中显示通知图标，有横幅和提示音。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LEVEL_LOW

```cangjie
LEVEL_LOW
```

**功能：** 表示通知功能已启用，且状态栏中显示通知图标，但没有横幅和提示音。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LEVEL_MIN

```cangjie
LEVEL_MIN
```

**功能：** 表示通知功能已启用，但状态栏中不显示通知图标，且没有横幅和提示音。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LEVEL_NONE

```cangjie
LEVEL_NONE
```

**功能：** 表示关闭通知功能。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

## enum SlotType

```cangjie
public enum SlotType {
    | UNKNOWN_TYPE
    | SOCIAL_COMMUNICATION
    | SERVICE_INFORMATION
    | CONTENT_INFORMATION
    | LIVE_VIEW
    | CUSTOMER_SERVICE
    | OTHER_TYPES
    | ...
}
```

**功能：** 通知渠道类型。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### CONTENT_INFORMATION

```cangjie
CONTENT_INFORMATION
```

**功能：** 内容资讯。该类型对应SlotLevel为LEVEL_MIN。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### CUSTOMER_SERVICE

```cangjie
CUSTOMER_SERVICE
```

**功能：** 客服消息。该类型用于用户与商家之间的客服消息，需由用户主动发起。该类型对应SlotLevel为LEVEL_DEFAULT。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### LIVE_VIEW

```cangjie
LIVE_VIEW
```

**功能：** 实况窗。不支持三方应用直接创建该渠道类型通知，可以由系统代理创建后，三方应用发布同ID的通知来更新指定内容。该类型对应SlotLevel为LEVEL_DEFAULT。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### OTHER_TYPES

```cangjie
OTHER_TYPES
```

**功能：** 其他。该类型对应SlotLevel为LEVEL_MIN。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### SERVICE_INFORMATION

```cangjie
SERVICE_INFORMATION
```

**功能：** 服务提醒。该类型对应SlotLevel为LEVEL_HIGH。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### SOCIAL_COMMUNICATION

```cangjie
SOCIAL_COMMUNICATION
```

**功能：** 社交通信。该类型对应SlotLevel为LEVEL_HIGH。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### UNKNOWN_TYPE

```cangjie
UNKNOWN_TYPE
```

**功能：** 未知类型。该类型对应SlotLevel为LEVEL_MIN。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19