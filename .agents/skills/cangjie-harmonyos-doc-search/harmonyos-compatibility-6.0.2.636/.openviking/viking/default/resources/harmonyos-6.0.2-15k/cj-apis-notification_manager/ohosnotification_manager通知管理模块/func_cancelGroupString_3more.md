## func cancelGroup(String)

```cangjie
public func cancelGroup(groupName: String): Unit
```

**功能：** 取消本应用指定组下的通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|groupName|String|是|-|通知组名称，此名称需要在发布通知时通过[NotificationRequest](#class-notificationrequest)对象指定。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let value = cancelGroup("test3")
    AppLog.info("test cancelGroup success.")
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```

## func getActiveNotificationCount()

```cangjie
public func getActiveNotificationCount(): UInt32
```

**功能：** 获取当前应用未删除的通知数。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取当前应用未删除通知数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let value = getActiveNotificationCount()
    AppLog.info("test getActiveNotificationCount success. NotificationCount: ${value}")
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```

## func getActiveNotifications()

```cangjie
public func getActiveNotifications(): Array<NotificationRequest>
```

**功能：** 获取当前应用未删除的通知列表。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NotificationRequest](#class-notificationrequest)>|获取当前应用通知列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let notifications = getActiveNotifications()
    AppLog.info("test getActiveNotifications success. Notifications.size: ${notifications.size}")
    for(v in notifications) {
        AppLog.info("notification.id: ${v.id}, notification.label: ${v.label}, notifications.creatorUid: ${v.creatorUid}, notifications.creatorPid: ${v.creatorPid}, notifications.creatorUserId: ${v.creatorUserId}")
    }
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```