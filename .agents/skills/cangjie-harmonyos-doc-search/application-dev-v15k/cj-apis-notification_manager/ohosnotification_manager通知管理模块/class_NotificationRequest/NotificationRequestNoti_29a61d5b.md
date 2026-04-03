### NotificationRequest(NotificationContent, String, Int32, Int32, Int32, String, Option\<NotificationFlags>)

```cangjie
public init(
    content: NotificationContent,
    creatorBundleName: String,
    creatorUid: Int32,
    creatorPid: Int32,
    creatorUserId: Int32,
    hashCode: String,
    notificationFlags: ?NotificationFlags
)
```

**功能：** 构造描述通知的请求实例。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[NotificationContent](#class-notificationcontent)|是|-|通知内容。|
|creatorBundleName|String|否|""| **命名参数。** 创建通知的包名。|
|creatorUid|Int32|否|0| **命名参数。** 创建通知的UID。|
|creatorPid|Int32|否|0| **命名参数。** 创建通知的PID。|
|creatorUserId|Int32|否|0| **命名参数。** 创建通知的UserId。|
|hashCode|String|否|""| **命名参数。** 通知唯一标识。|
|notificationFlags|[Option](#notificationcapsulestring-optionpixelmap-string)\<[NotificationFlags](#class-notificationflags)>|否|None| **命名参数。** 获取NotificationFlags。|