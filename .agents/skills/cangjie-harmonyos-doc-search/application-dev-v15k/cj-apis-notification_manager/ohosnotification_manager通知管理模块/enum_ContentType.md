## enum ContentType

```cangjie
public enum ContentType {
    | NOTIFICATION_CONTENT_BASIC_TEXT
    | NOTIFICATION_CONTENT_LONG_TEXT
    | NOTIFICATION_CONTENT_PICTURE
    | NOTIFICATION_CONTENT_CONVERSATION
    | NOTIFICATION_CONTENT_MULTILINE
    | NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW
    | NOTIFICATION_CONTENT_LIVE_VIEW
    | ...
}
```

**功能：** 通知内容类型。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_BASIC_TEXT

```cangjie
NOTIFICATION_CONTENT_BASIC_TEXT
```

**功能：** 普通类型通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_CONVERSATION

```cangjie
NOTIFICATION_CONTENT_CONVERSATION
```

**功能：** 社交类型通知。预留能力，暂未支持。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_LIVE_VIEW

```cangjie
NOTIFICATION_CONTENT_LIVE_VIEW
```

**功能：** 普通实况窗类型通知。只支持系统应用。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_LONG_TEXT

```cangjie
NOTIFICATION_CONTENT_LONG_TEXT
```

**功能：** 长文本类型通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_MULTILINE

```cangjie
NOTIFICATION_CONTENT_MULTILINE
```

**功能：** 多行文本类型通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_PICTURE

```cangjie
NOTIFICATION_CONTENT_PICTURE
```

**功能：** 图片类型通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW

```cangjie
NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW
```

**功能：** 实况窗类型通知。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12