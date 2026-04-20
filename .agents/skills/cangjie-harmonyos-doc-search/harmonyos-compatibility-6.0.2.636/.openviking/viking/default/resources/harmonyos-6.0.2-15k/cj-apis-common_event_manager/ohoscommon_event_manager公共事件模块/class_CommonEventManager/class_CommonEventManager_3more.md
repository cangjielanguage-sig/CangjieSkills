## class CommonEventManager

```cangjie
public class CommonEventManager {}
```

**功能：** 本结构体提供了公共事件的管理能力。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

### static func createSubscriber(CommonEventSubscribeInfo)

```cangjie
public static func createSubscriber(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber
```

**功能：** 创建订阅者。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscribeInfo|[CommonEventSubscribeInfo](#class-commoneventsubscribeinfo)|是|-|表示订阅信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[CommonEventSubscriber](#class-commoneventsubscriber)|订阅者对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let subscriber: CommonEventSubscriber //用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let support = Support.COMMON_EVENT_ABILITY_ADDED
//订阅者信息
let subscribeInfo: CommonEventSubscribeInfo = CommonEventSubscribeInfo([support])
//创建订阅者
try {
    subscriber = CommonEventManager.createSubscriber(subscribeInfo)
} catch (e: BusinessException) {
    AppLog.info("errorCode = ${e.code}, errorMsg = ${e.message}")
}
```

### static func publish(String)

```cangjie
public static func publish(event: String): Unit
```

**功能：** 发布公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|表示要发送的公共事件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[事件错误码](../../errorcodes/cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息                            |
  | :------- | :----------------------------------- |
  | 1500003 | The common event sending frequency too high. |
  | 1500007 | error sending message to Common Event Service. |
  | 1500008 | Common Event Service does not complete initialization. |
  | 1500009 | error obtaining system parameters.  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    //发布公共事件
    CommonEventManager.publish(Support.COMMON_EVENT_SCREEN_ON)
} catch (e: BusinessException) {
    let code = e.code
    let message = e.message
    AppLog.info("publish failed, error code: ${code}, message: ${message}.")
}
```