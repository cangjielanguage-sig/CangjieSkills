## class CommonEventManager

```cangjie
public class CommonEventManager {}
```

**功能：** 本结构体提供了公共事件的管理能力。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static func createSubscriber(CommonEventSubscribeInfo)

```cangjie
public static func createSubscriber(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber
```

**功能：** 创建订阅者。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscribeInfo|[CommonEventSubscribeInfo](./cj-apis-common_event_subscribe_info.md#class-commoneventsubscribeinfo)|是|-|表示订阅信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[CommonEventSubscriber](./cj-apis-common_event_subscriber.md#class-commoneventsubscriber)|订阅者对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[事件错误码](./cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1500008 | Common Event Service does not complete initialization. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*

let subscriber: CommonEventSubscriber //用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let support = Support.COMMON_EVENT_ABILITY_ADDED
//订阅者信息
let subscribeInfo: CommonEventSubscribeInfo = CommonEventSubscribeInfo([support])
//创建订阅者
try {
    subscriber = CommonEventManager.createSubscriber(subscribeInfo)
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", "errorCode = ${e.code}, errorMsg = ${e.message}")
}
```

### static func publish(String, CommonEventPublishData)

```cangjie
public static func publish(event: String, options!: CommonEventPublishData =  CommonEventPublishData()): Unit
```

**功能：** 发布公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|表示要发送的公共事件。|
|options|[CommonEventPublishData](./cj-apis-common_event_publish_data.md#class-commoneventpublishdata)|否|CommonEventPublishData()|**命名参数。** 表示发布公共事件的属性。|

**异常：**

- BusinessException：对应错误码如下表，详见[事件错误码](./cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1500003 | The common event sending frequency too high. |
  | 1500007 | Failed to send the message to the common event service. |
  | 1500008 | Failed to initialize the common event service. |
  | 1500009 | Failed to obtain system parameters. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.base.*
import ohos.business_exception.*

try {
    // 公共事件属性
    let pData = CommonEventPublishData(bundleName: "com.example.myapplication", data: "123321", code: 123321)
    //发布公共事件
    CommonEventManager.publish(Support.COMMON_EVENT_SCREEN_ON, options: pData)
} catch (e: BusinessException) {
    let code = e.code
    let message = e.message
    Hilog.error(0, "AppLogCj", "publish failed, error code: ${code}, message: ${message}.")
}
```