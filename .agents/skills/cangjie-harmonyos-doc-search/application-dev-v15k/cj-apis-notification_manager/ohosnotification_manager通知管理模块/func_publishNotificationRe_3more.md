## func publish(NotificationRequest)

```cangjie
public func publish(request: NotificationRequest): Unit
```

**功能：** 发布通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[NotificationRequest](#class-notificationrequest)|是|-|用于设置要发布通知的内容和相关配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|
  |1600004|Notification is not enabled.|
  |1600005|Notification slot is not enabled.|
  |1600009|Over max number notifications per second.|
  |1600012|No memory space.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

// 创建通知Request对象
var normal = NotificationBasicContent("test_title", "test_text")
normal.additionalText = "test_additionalText"
let content = NotificationContent(NOTIFICATION_CONTENT_BASIC_TEXT, normal: normal)
let request = NotificationRequest(content, id: 1)
try {
    publish(request)
} catch (e: Exception) {
    AppLog.info("notification request fail because: ${e}")
}
```

## func removeAllSlots()

```cangjie
public func removeAllSlots(): Unit
```

**功能：** 删除此应用程序所有通知渠道。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

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
    removeAllSlots()
    AppLog.info("test removeAllSlots success")
} catch (e: Exception) {
    AppLog.info("call removeAllSlots fail because ${e}")
}
```

## func removeSlot(SlotType)

```cangjie
public func removeSlot(slotType: SlotType): Unit
```

**功能：** 删除此应用程序指定类型的通知渠道。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotType|[SlotType](#enum-slottype)|是|-|通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types.<br>3.Parameter verification failed.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

let slottype = SlotType.SOCIAL_COMMUNICATION

try {
    removeSlot(slottype)
    AppLog.info("test removeSlot success")
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```