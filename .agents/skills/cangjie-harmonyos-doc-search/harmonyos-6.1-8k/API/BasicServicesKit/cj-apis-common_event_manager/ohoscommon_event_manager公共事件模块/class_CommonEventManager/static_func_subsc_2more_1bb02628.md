### static func subscribe(CommonEventSubscriber, AsyncCallback\<CommonEventData>)

```cangjie
public static func subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): Unit
```

**功能：** 订阅公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscriber|[CommonEventSubscriber](cj-apis-common_event_subscriber.md#class-commoneventsubscriber)|是|-|表示订阅者对象。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<[CommonEventData](cj-apis-common_event_data.md#class-commoneventdata)>|是|-|表示接收公共事件数据的回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[事件错误码](./cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 1500007 | Failed to send the message to the common event service. |
  | 1500008 | Failed to initialize the common event service. |
  | 1500010 | The count of subscriber exceed system specification. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*
import ohos.business_exception.*
import kit.PerformanceAnalysisKit.Hilog

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
    Hilog.error(0, "AppLogCj", "errorCode = ${e.code}, errorMsg = ${e.message}")
}
```

### static func unsubscribe(CommonEventSubscriber)

```cangjie
public static func unsubscribe(subscriber: CommonEventSubscriber): Unit
```

**功能：** 取消订阅公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscriber|[CommonEventSubscriber](cj-apis-common_event_subscriber.md#class-commoneventsubscriber)|是|-|表示订阅者对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[事件错误码](./cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 1500007 | Failed to send the message to the common event service. |
  | 1500008 | Failed to initialize the common event service. |

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*
import ohos.business_exception.*
import kit.PerformanceAnalysisKit.Hilog

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
    Hilog.error(0, "AppLogCj", "errorCode = ${e.code}, errorMsg = ${e.message}")
}
```