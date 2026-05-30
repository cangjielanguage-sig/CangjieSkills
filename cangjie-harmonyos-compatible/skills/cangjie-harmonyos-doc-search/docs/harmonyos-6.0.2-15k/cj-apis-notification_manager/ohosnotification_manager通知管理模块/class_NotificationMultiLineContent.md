## class NotificationMultiLineContent

```cangjie
public class NotificationMultiLineContent <: NotificationBasicContent {
    public var briefText: String
    public var longTitle: String
    public var lines: Array<String>
    public init(
        title: String,
        text: String,
        briefText: String,
        longTitle: String,
        lines: Array<String>
    )
}
```

**功能：** 描述多行文本通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**父类型：**

- [NotificationBasicContent](#class-notificationbasiccontent)

### var briefText

```cangjie
public var briefText: String
```

**功能：** 通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过200字节，超出部分会被截断）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var lines

```cangjie
public var lines: Array<String>
```

**功能：** 通知的多行文本（大小不超过200字节，超出部分会被截断）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var longTitle

```cangjie
public var longTitle: String
```

**功能：** 通知展开时的标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### init(String, String, String, String, Array\<String>)

```cangjie
public init(
    title: String,
    text: String,
    briefText: String,
    longTitle: String,
    lines: Array<String>
)
```

**功能：** 构造描述多行文本通知实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|通知标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|text|String|是|-|通知内容（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|briefText|String|是|-|通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|longTitle|String|是|-|通知展开时的标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|lines|Array\<String>|是|-|通知的多行文本（大小不超过200字节，超出部分会被截断）。|