## class CommonEventSubscribeInfo

```cangjie
public class CommonEventSubscribeInfo {
    public init(
        events: Array<String>,
        publisherPermission!: ?String = None,
        publisherDeviceId!: ?String = None,
        userId!: ?Int32 = None,
        priority!: ?Int32 = None,
        publisherBundleName!: ?String = None
    )
}
```

**功能：** 用于表示订阅者的信息。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

### prop events

```cangjie
public prop events: Array<String>
```

**功能：** 表示要订阅的公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** Array\<string>

**读写能力：** 只读

**起始版本：** 12

### prop priority

```cangjie
public prop priority: ?Int32
```

**功能：** 表示订阅者的优先级。值的范围是-100到1000，超过上下限的优先级将被设置为上下限值。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** ?Int32

**读写能力：** 只读

**起始版本：** 12

### prop publisherBundleName

```cangjie
public prop publisherBundleName: ?String
```

**功能：** 表示要订阅的发布者的bundleName。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### prop publisherDeviceId

```cangjie
public prop publisherDeviceId: ?String
```

**功能：** 表示设备ID。通过[@ohos.deviceInfo](./cj-apis-device_info.md)获取udid，作为订阅者的设备ID。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### prop publisherPermission

```cangjie
public prop publisherPermission: ?String
```

**功能：** 表示发布者的权限，订阅方将只能接收到具有该权限的发送方发布的事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### prop userId

```cangjie
public prop userId: ?Int32
```

**功能：** 表示用户ID。此参数是可选的，默认值当前用户的ID。如果指定了此参数，则该值必须是系统中现有的用户ID。通过[getOsAccountLocalId](./cj-apis-account-osAccount.md#func-getosaccountlocalid)获取系统账号ID，作为订阅者的用户ID。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** ?Int32

**读写能力：** 只读

**起始版本：** 12

### init(Array\<String>, ?String, ?String, ?Int32, ?Int32, ?String)

```cangjie
public init(
    events: Array<String>,
    publisherPermission!: ?String = None,
    publisherDeviceId!: ?String = None,
    userId!: ?Int32 = None,
    priority!: ?Int32 = None,
    publisherBundleName!: ?String = None
)
```

**功能：** 构造CommonEventSubscribeInfo对象。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|events|Array\<String>|是|-|表示要订阅的公共事件。|
|publisherPermission|?String|否|None| **命名参数。** 表示发布者的权限，订阅方将只能接收到具有该权限的发送方发布的事件。|
|publisherDeviceId|?String|否|None| **命名参数。** 表示设备ID。通过[@ohos.deviceInfo](./cj-apis-device_info.md)获取udid，作为订阅者的设备ID。|
|userId|?Int32|否|None| **命名参数。** 表示用户ID。此参数是可选的，默认值当前用户的ID。如果指定了此参数，则该值必须是系统中现有的用户ID。通过[getOsAccountLocalId](./cj-apis-account-osAccount.md#func-getosaccountlocalid)获取系统账号ID，作为订阅者的用户ID。|
|priority|?Int32|否|None| **命名参数。**  表示订阅者的优先级。值的范围是-100到1000，超过上下限的优先级将被设置为上下限值。|
|publisherBundleName|?String|否|None| **命名参数。** 表示要订阅的发布者的bundleName。|