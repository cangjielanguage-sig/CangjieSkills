# ohos.notification_manager（通知管理模块）

本模块提供通知管理的能力，包括发布、取消发布通知，创建、获取、移除通知通道，获取通知的使能状态、角标使能状态，获取通知的相关信息等。

## 导入模块

```cangjie
import kit.NotificationKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func addSlot(SlotType)

```cangjie
public func addSlot(slotType: SlotType): Unit
```

**功能：** 创建指定类型的通知渠道。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotType|[SlotType](#enum-slottype)|是|-|要创建的通知渠道的类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types.<br>3.Parameter verification failed.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|
  |1600012|No memory space.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

let slottype = SlotType.SOCIAL_COMMUNICATION
try {
    addSlot(slottype)
    addSlot(SlotType.CUSTOMER_SERVICE)
    AppLog.info("test addSlot success")
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```

## func cancel(Int32, String)

```cangjie
public func cancel(id: Int32, label!: String = ""): Unit
```

**功能：** 取消本应用指定组下的通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|通知ID。|
|label|String|否|""| **命名参数。** 通知标签，默认为空。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|
  |1600007|The notification is not exist.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    cancel(1, label: "abc")
    AppLog.info("cancel success")
} catch (e: Exception) {
    AppLog.info("call cancel fail because ${e}")
}
```

## func cancelAll()

```cangjie
public func cancelAll(): Unit
```

**功能：** 取消所有已发布的通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
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
    cancelAll()
    AppLog.info("cancelAll success")
} catch (e: Exception) {
    AppLog.info("call cancelAll fail because ${e}")
}
```