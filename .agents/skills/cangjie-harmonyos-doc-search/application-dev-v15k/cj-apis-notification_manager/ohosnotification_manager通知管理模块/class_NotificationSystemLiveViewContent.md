## class NotificationSystemLiveViewContent

```cangjie
public class NotificationSystemLiveViewContent <: NotificationBasicContent {
    public var typeCode: Int32
    public var capsule: Option<NotificationCapsule>
    public var button: Option<NotificationButton>
    public var time: Option<NotificationTime>
    public var progress: Option<NotificationProgress>
    public init(title: String, text: String, typeCode: Int32)
}
```

**功能：** 描述系统实况窗通知内容。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**父类型：**

- [NotificationBasicContent](#class-notificationbasiccontent)

### var button

```cangjie
public var button: Option<NotificationButton>
```

**功能：** 实况通知的按钮。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationButton](#class-notificationbutton)>

**读写能力：** 可读写

**起始版本：** 19

### var capsule

```cangjie
public var capsule: Option<NotificationCapsule>
```

**功能：** 实况通知的胶囊。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationCapsule](#class-notificationcapsule)>

**读写能力：** 可读写

**起始版本：** 19

### var progress

```cangjie
public var progress: Option<NotificationProgress>
```

**功能：** 实况内容的进度。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationProgress](#class-notificationprogress)>

**读写能力：** 可读写

**起始版本：** 19

### var time

```cangjie
public var time: Option<NotificationTime>
```

**功能：** 实况通知的时间。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationTime](#class-notificationtime)>

**读写能力：** 可读写

**起始版本：** 19

### var typeCode

```cangjie
public var typeCode: Int32
```

**功能：** 类型标识符，标记调用方业务类型。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(String, String, Int32)

```cangjie
public init(title: String, text: String, typeCode: Int32)
```

**功能：** 构造描述系统实况窗通知内容实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|通知标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|text|String|是|-|通知内容（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|typeCode|Int32|是|-|类型标识符，标记调用方业务类型。|