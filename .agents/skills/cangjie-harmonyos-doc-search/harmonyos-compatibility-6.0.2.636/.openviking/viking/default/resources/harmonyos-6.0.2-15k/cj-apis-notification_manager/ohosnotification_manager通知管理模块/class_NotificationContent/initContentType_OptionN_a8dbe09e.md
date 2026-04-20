### init(ContentType, Option\<NotificationBasicContent>, Option\<NotificationLongTextContent>, Option\<NotificationMultiLineContent>)

```cangjie
public init(
    notificationContentType: ContentType,
    normal!: Option<NotificationBasicContent> = None,
    longText!: Option<NotificationLongTextContent> = None,
    multiLine!: Option<NotificationMultiLineContent> = None
)
```

**功能：** 构造描述通知类型实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|notificationContentType|[ContentType](#enum-contenttype)|是|-|通知内容类型。|
|normal|[Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationBasicContent](#class-notificationbasiccontent)>|否|None| **命名参数。** 基本类型通知内容。|
|longText|[Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationLongTextContent](#class-notificationlongtextcontent)>|否|None| **命名参数。** 长文本类型通知内容。|
|multiLine|[Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationMultiLineContent](#class-notificationmultilinecontent)>|否|None| **命名参数。** 多行类型通知内容。|