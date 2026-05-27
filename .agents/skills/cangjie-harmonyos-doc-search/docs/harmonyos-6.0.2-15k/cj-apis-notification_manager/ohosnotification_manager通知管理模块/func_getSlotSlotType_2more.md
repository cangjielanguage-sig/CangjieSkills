## func getSlot(SlotType)

```cangjie
public func getSlot(slotType: SlotType): NotificationSlot
```

**功能：** 获取一个指定类型的通知渠道。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotType|[SlotType](#enum-slottype)|是|-|通知渠道类型，例如社交通信、服务提醒、内容咨询等类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[NotificationSlot](#class-notificationslot)|获取一个通知渠道。|

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
    let slot = getSlot(slottype)
    AppLog.info(
        "test getSlot: .notificationType: ${match_slotType(slot.notificationType)}, .desc: ${slot.desc}, .level: ${match_slotLevel(slot.level)}"
    )
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```

## func getSlots()

```cangjie
public func getSlots(): Array<NotificationSlot>
```

**功能：** 获取此应用程序的所有通知渠道。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NotificationSlot](#class-notificationslot)>|获取此应用程序的所有通知渠道。|

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

try {
    let slots = getSlots()
    AppLog.info("test getSlots: slots.size: ${slots.size}")
    for (slot in slots) {
        AppLog.info("slot.desc: ${slot.desc}, slot.badgeFlag: ${slot.badgeFlag}, slot.lockscreenVisibility: ${slot.lockscreenVisibility}, slot.lightEnabled: ${slot.lightEnabled}, slot.vibrationValues.size: ${slot.vibrationValues.size}")
    }
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```