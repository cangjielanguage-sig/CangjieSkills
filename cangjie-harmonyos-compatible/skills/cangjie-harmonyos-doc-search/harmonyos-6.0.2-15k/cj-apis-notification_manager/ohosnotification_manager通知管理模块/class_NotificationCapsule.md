## class NotificationCapsule

```cangjie
public class NotificationCapsule {
    public NotificationCapsule(
        public var title!: String = "",
        public var icon!: Option<PixelMap> = None,
        public var backgroundColor!: String = ""
    )
}
```

**功能：** 描述通知胶囊。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

### var backgroundColor

```cangjie
public var backgroundColor: String = ""
```

**功能：** 背景颜色。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var icon

```cangjie
public var icon: Option<PixelMap> = None
```

**功能：** 胶囊图片。

**系统能力：** SystemCapability.Notification.Notification

**类型：** [Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String = ""
```

**功能：** 胶囊标题。

**系统能力：** SystemCapability.Notification.Notification

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### NotificationCapsule(String, Option\<PixelMap>, String)

```cangjie
public NotificationCapsule(
    public var title!: String = "",
    public var icon!: Option<PixelMap> = None,
    public var backgroundColor!: String = ""
)
```

**功能：** 构造描述通知胶囊实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 胶囊标题。|
|icon|[Option](#notificationcapsulestring-optionpixelmap-string)\<[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)>|否|None| **命名参数。** 胶囊图片。|
|backgroundColor|String|否|""| **命名参数。** 背景颜色。|