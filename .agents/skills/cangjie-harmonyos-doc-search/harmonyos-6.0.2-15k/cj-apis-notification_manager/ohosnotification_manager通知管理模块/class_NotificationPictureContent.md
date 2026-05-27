## class NotificationPictureContent

```cangjie
public class NotificationPictureContent <: NotificationBasicContent {
    public var briefText: String
    public var expandedTitle: String
    public var picture: PixelMap
    public init(title: String, text: String, lockscreenPicture: Option<PixelMap>, briefText: String, expandedTitle: String,
                picture: PixelMap, additionalText!: String = "")
}
```

**功能：** 描述附有图片的通知。

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

### var expandedTitle

```cangjie
public var expandedTitle: String
```

**功能：** 通知展开时的标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var picture

```cangjie
public var picture: PixelMap
```

**功能：** 通知的图片内容(图像像素的总字节数不能超过2MB)。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 可读写

**起始版本：** 12

### init(String, String, Option\<PixelMap>, String, String, PixelMap, String)

```cangjie
public init(title: String, text: String, lockscreenPicture: Option<PixelMap>, briefText: String, expandedTitle: String,
            picture: PixelMap, additionalText!: String = "")
```

**功能：** 构造描述附有图片的通知实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|通知标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|text|String|是|-|通知内容（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|lockscreenPicture|[Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>|是|-|通知在锁屏界面显示的图片。|
|briefText|String|是|-|通知概要内容，是对通知内容的总结（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|expandedTitle|String|是|-|通知展开时的标题（不可为空字符串，大小不超过200字节，超出部分会被截断）。|
|picture|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|通知的图片内容(图像像素的总字节数不能超过2MB)。|
|additionalText|String|否|""| **命名参数。** 通知附加内容，是对通知内容的补充（大小不超过200字节，超出部分会被截断）。|