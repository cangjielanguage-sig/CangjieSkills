### func isStickyCommonEvent()

```cangjie
public func isStickyCommonEvent(): Bool
```

**功能：** 检查当前公共事件是否为一个粘性事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示是粘性公共事件；返回false表示不是粘性公共事件。|

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
        //查询当前公共事件是否为粘性公共事件
        let isSticky = subscriber.isStickyCommonEvent()
        AppLog.info("isSticky = ${isSticky}")
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

### func abortCommonEvent()

```cangjie
public func abortCommonEvent(): Unit
```

**功能：** 添加有序公共事件的中止状态。当该接口与[finishCommonEvent()](#func-finishcommonevent)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 20

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
        //添加有序公共事件的中止状态
        subscriber.abortCommonEvent()
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