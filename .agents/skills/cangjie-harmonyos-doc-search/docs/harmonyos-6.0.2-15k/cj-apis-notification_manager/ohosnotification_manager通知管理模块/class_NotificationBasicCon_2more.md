## class NotificationBasicContent

```cangjie
public open class NotificationBasicContent {
    public var title: String
    public var text: String
    public var additionalText: String = ""
    public var lockscreenPicture: Option<PixelMap> = None

    public init(
        title: String,
        text: String
    )
}
```

**功能：** 描述普通文本通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

### var additionalText

```cangjie
public var additionalText: String = ""
```

**功能：** 通知附加内容，是对通知内容的补充，默认为空。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var lockscreenPicture

```cangjie
public var lockscreenPicture: Option<PixelMap> = None
```

**功能：** 通知在锁屏界面显示的图片。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 19

### var text

```cangjie
public var text: String
```

**功能：** 通知标题（不可为空字符串）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var title

```cangjie
public var title: String
```

**功能：** 通知内容（不可为空字符串）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### init(String, String)

```cangjie
public init(
    title: String,
    text: String
)
```

**功能：** 构造描述普通文本通知实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|通知标题（不可为空字符串）。|
|text|String|是|-|通知内容（不可为空字符串）。|

## class NotificationButton

```cangjie
public class NotificationButton {
    public NotificationButton(
        public var names!: Array<String> = [],
        public var icons!: Array<PixelMap> = []
    )
}
```

**功能：** 描述通知按钮。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### var icons

```cangjie
public var icons: Array<PixelMap> = []
```

**功能：** 按钮图片（最多支持3个）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Array\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 19

### var names

```cangjie
public var names: Array<String> = []
```

**功能：** 按钮名称（最多支持3个）。

**系统能力：** SystemCapability.Notification.Notification

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### NotificationButton(Array\<String>, Array\<PixelMap>)

```cangjie
public NotificationButton(
    public var names!: Array<String> = [],
    public var icons!: Array<PixelMap> = []
)
```

**功能：** 构造描述通知按钮实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|names|Array\<String>|否|[]| **命名参数。** 按钮名称（最多支持3个）。|
|icons|Array\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>|否|[]| **命名参数。** 按钮图片（最多支持3个）。|