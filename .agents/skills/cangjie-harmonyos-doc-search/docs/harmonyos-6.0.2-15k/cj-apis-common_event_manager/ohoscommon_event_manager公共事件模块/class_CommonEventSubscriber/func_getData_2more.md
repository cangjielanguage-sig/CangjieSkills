### func getData()

```cangjie
public func getData(): String
```

**功能：** 获取有序公共事件传递的数据（String类型）。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|表示有序公共事件传递的数据（String类型）|

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
let subscribeInfo = CommonEventSubscribeInfo(["event"])
// 订阅者
let subscriber = CommonEventManager.createSubscriber(subscribeInfo)
// 订阅事件回调函数
func callback(c: CommonEventData): Unit {
    try {
        //获取有序公共事件传递的数据
        let data = subscriber.getData()
        AppLog.info("data = ${data}")
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

### func setData(String)

```cangjie
public func setData(data: String): Unit
```

**功能：** 设置有序公共事件传递的数据（String类型）。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|String|是|-|有序公共事件传递的数据（String类型）。|

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
let subscribeInfo = CommonEventSubscribeInfo(["event"])
// 订阅者
let subscriber = CommonEventManager.createSubscriber(subscribeInfo)
// 订阅事件回调函数
func callback(c: CommonEventData): Unit {
    try {
        //设置有序公共事件传递的数据
        subscriber.setData("DATA")
        //获取有序公共事件传递的数据
        let data = subscriber.getData()
        AppLog.info("data = ${data}")
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