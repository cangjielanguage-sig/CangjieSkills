## class NotificationContent

```cangjie
public class NotificationContent {
    public var notificationContentType: ContentType
    public var normal: Option<NotificationBasicContent> = None
    public var longText: Option<NotificationLongTextContent> = None
    public var multiLine: Option<NotificationMultiLineContent> = None
    public var picture: Option<NotificationPictureContent> = None
    public var systemLiveView: Option<NotificationSystemLiveViewContent> = None

    public init(
        notificationContentType: ContentType,
        normal!: Option<NotificationBasicContent> = None,
        longText!: Option<NotificationLongTextContent> = None,
        multiLine!: Option<NotificationMultiLineContent> = None
    )
}
```

**功能：** 描述通知类型。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### var longText

```cangjie
public var longText: Option<NotificationLongTextContent> = None
```

**功能：** 长文本类型通知内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationLongTextContent](#class-notificationlongtextcontent)>

**读写能力：** 可读写

**起始版本：** 12

### var multiLine

```cangjie
public var multiLine: Option<NotificationMultiLineContent> = None
```

**功能：** 多行类型通知内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationMultiLineContent](#class-notificationmultilinecontent)>

**读写能力：** 可读写

**起始版本：** 12

### var normal

```cangjie
public var normal: Option<NotificationBasicContent> = None
```

**功能：** 基本类型通知内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationBasicContent](#class-notificationbasiccontent)>

**读写能力：** 可读写

**起始版本：** 12

### var notificationContentType

```cangjie
public var notificationContentType: ContentType
```

**功能：** 通知内容类型。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [ContentType](#enum-contenttype)

**读写能力：** 可读写

**起始版本：** 12

### var picture

```cangjie
public var picture: Option<NotificationPictureContent> = None
```

**功能：** 图片类型通知内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationPictureContent](#class-notificationpicturecontent)>

**读写能力：** 可读写

**起始版本：** 19

### var systemLiveView

```cangjie
public var systemLiveView: Option<NotificationSystemLiveViewContent> = None
```

**功能：** 系统实况窗类型通知内容。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationSystemLiveViewContent](#class-notificationsystemliveviewcontent)>

**读写能力：** 可读写

**起始版本：** 19