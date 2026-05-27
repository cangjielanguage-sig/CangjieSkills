### static func unsubscribe(CommonEventSubscriber)

```cangjie
public static func unsubscribe(subscriber: CommonEventSubscriber): Unit
```

**功能：** 取消订阅公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscriber|[CommonEventSubscriber](#class-commoneventsubscriber)|是|-|表示订阅者对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[事件错误码](../../errorcodes/cj-errorcode-common_event_service.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  | 错误码ID | 错误信息                            |
  | :------- | :----------------------------------- |
  | 801     | capability not supported.               |
  | 1500007 | error sending message to Common Event Service. |
  | 1500008 | Common Event Service does not complete initialization. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

// 订阅事件：亮屏
let events = [Support.COMMON_EVENT_SCREEN_ON]
// 订阅者信息
let info = CommonEventSubscribeInfo(events)
// 订阅者
let sub = CommonEventManager.createSubscriber(info)
// 取消订阅
try {
    CommonEventManager.unsubscribe(sub)
} catch (e: BusinessException) {
    AppLog.info("errorCode = ${e.code}, errorMsg = ${e.message}")
}
```