### static func off(String, EventCallback)

```cangjie
public static func off(eventId: String, callback: EventCallback): Unit
```

**功能：** 取消针对该事件ID的订阅。若该事件已经通过on或者once接口订阅，则取消该订阅；否则，不做任何处理。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|事件ID，不支持空字符串。|
|callback|[EventCallback](#struct-eventcallback)|是|-|取消该事件的回调处理函数。|

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
let eventId: String = "id1"
Emitter.off(eventId, f)
```

### static func on(InnerEvent, EventCallback)

```cangjie
public static func on(event: InnerEvent, callback: EventCallback): Unit
```

**功能：** 持续订阅指定事件，并在接收到该事件时，执行对应的回调处理函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[InnerEvent](#class-innerevent)|是|-|持续订阅的事件，其中[EventPriority](#enum-eventpriority)，在订阅事件时无需指定，也不生效。|
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
Emitter.on(event1, f)
```

### static func on(String, EventCallback)

```cangjie
public static func on(eventId: String, callback: EventCallback): Unit
```

**功能：** 持续订阅指定事件，并在接收到该事件时，执行对应的回调处理函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|持续订阅的事件，不支持空字符串。|
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
Emitter.on("eventId", f)
```