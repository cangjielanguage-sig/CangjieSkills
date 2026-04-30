### static func publish(String, CommonEventPublishData)

```cangjie
public static func publish(event: String, options: CommonEventPublishData): Unit
```

**功能：** 发布公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|String|是|-|表示要发送的公共事件。|
|options|[CommonEventPublishData](#struct-commoneventpublishdata)|是|-|表示发布公共事件的属性。|

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
    // 公共事件属性
    let pData = CommonEventPublishData("com.example.myapplication", "123321", 123321)
    //发布公共事件
    CommonEventManager.publish(Support.COMMON_EVENT_SCREEN_ON, pData)
} catch (e: BusinessException) {
    let code = e.code
    let message = e.message
    AppLog.info("publish failed, error code: ${code}, message: ${message}.")
}
```

### static func subscribe(CommonEventSubscriber, (CommonEventData) -> Unit)

```cangjie
public static func subscribe(subscriber: CommonEventSubscriber, callback: (CommonEventData) -> Unit): Unit
```

**功能：** 以回调形式订阅公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subscriber|[CommonEventSubscriber](#class-commoneventsubscriber)|是|-|表示订阅者对象。|
|callback|([CommonEventData](#struct-commoneventdata))->Unit|是|-|表示接收公共事件数据的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[事件错误码](../../errorcodes/cj-errorcode-common_event_service.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  | 错误码ID | 错误信息                            |
  | :-------- | :----------------------------------- |
  | 801     | capability not supported.               |
  | 1500007 | error sending message to Common Event Service. |
  | 1500008 | Common Event Service does not complete initialization. |
  | 1500010 | The count of subscriber exceed system specification. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.ValueType as CMEValueType
import kit.BasicServicesKit.*
import ohos.base.*
import std.collection.*

// 订阅事件：亮屏
let events = [Support.COMMON_EVENT_SCREEN_ON]
// 订阅者信息
let info = CommonEventSubscribeInfo(events)
// 订阅者
let sub = CommonEventManager.createSubscriber(info)
let strV = CMEValueType.STRING("Hello")
let intV = CMEValueType.INT(11)
let parameter = HashMap<String, CMEValueType>()
parameter.add("1", strV)
parameter.add("2", intV)
// 订阅事件回调函数
func callback(c: CommonEventData): Unit {
    AppLog.info("Callback")
}
// 发布数据
let pData = CommonEventPublishData("com.example.myapplication", "123321", 123321, parameters: parameter)
try {
    // 订阅
    CommonEventManager.subscribe(sub, callback)
    // 发布
    CommonEventManager.publish(Support.COMMON_EVENT_SCREEN_ON, pData)
} catch (e: BusinessException) {
    AppLog.info("errorCode = ${e.code}, errorMsg = ${e.message}")
}
```