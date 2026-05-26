### static func once(InnerEvent, EventCallback)

```cangjie
public static func once(event: InnerEvent, callback: EventCallback): Unit
```

**功能：** 单次订阅指定事件，并在接收到该事件并执行完相应的回调函数后，自动取消订阅。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[InnerEvent](#class-innerevent)|是|-|单次订阅的事件，其中[EventPriority](#enum-eventpriority)，在订阅事件时无需指定，也不生效。|
|callback|[EventCallback](#struct-eventcallback)|是|-|接收到该事件时需要执行的回调处理函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid eventId.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*

// 此处代码可添加在依赖项定义中
func callback(eventData: EventData) {
    Hilog.info(0, "EmitterTest", "callback")
}

let event1: InnerEvent = InnerEvent(1)
let f = EventCallback("callback", callback)
Emitter.once(event1, f)
```

### static func once(String, EventCallback)

```cangjie
public static func once(eventId: String, callback: EventCallback): Unit
```

**功能：** 单次订阅指定事件，并在接收到该事件并执行完相应的回调函数后，自动取消订阅。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|单次订阅的事件，不支持空字符串。|
|callback|[EventCallback](#struct-eventcallback)|是|-|接收到该事件时需要执行的回调处理函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid eventId.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.*

// 此处代码可添加在依赖项定义中
func callback(eventData: EventData) {
    Hilog.info(0, "EmitterTest", "callback")
}

let f = EventCallback("callback", callback)
// 收到eventId为1的事件后执行回调函数
Emitter.once("eventId", f)
```