### func getSubscribeInfo()

```cangjie
public func getSubscribeInfo(): CommonEventSubscribeInfo
```

**功能：** 获取订阅者的订阅信息。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[CommonEventSubscribeInfo](#class-commoneventsubscribeinfo)|表示订阅者的订阅信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[事件错误码](../../errorcodes/cj-errorcode-common_event_service.md)。

  | 错误码ID | 错误信息                            |
  | :------- | :----------------------------------- |
  | 1500008 | Common Event Service does not complete initialization. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.BusinessException

// 订阅者信息
let subscribeInfo = CommonEventSubscribeInfo(["event"],
    priority: 10,
    publisherPermission: "publisherPermission",
    publisherDeviceId: "publisherDeviceId",
    publisherBundleName: "com.example.myapplication")
// 订阅者
let subscriber = CommonEventManager.createSubscriber(subscribeInfo)
// 订阅事件回调函数
func callback(c: CommonEventData): Unit {
    try {
        //获取订阅者的订阅信息
        let info = subscriber.getSubscribeInfo()
        AppLog.info("info.events = ${info.events}")
        AppLog.info("info.userId = ${info.userId}")
        AppLog.info("info.priority = ${info.priority}")
        AppLog.info("info.publisherDeviceId = ${info.publisherDeviceId}")
        AppLog.info("info.publisherBundleName = ${info.publisherBundleName}")
        AppLog.info("info.publisherPermission = ${info.publisherPermission}")
        subscriber.finishCommonEvent()
    } catch (e: BusinessException) {
        AppLog.error("errorCode = ${e.code}, errorMsg = ${e.message}")
    }
}
// 订阅
CommonEventManager.subscribe(subscriber, callback)
// 发布数据
let pData = CommonEventPublishData("com.example.myapplication", "data", 1, isOrdered: true)
// 发布
CommonEventManager.publish("event", pData)
```