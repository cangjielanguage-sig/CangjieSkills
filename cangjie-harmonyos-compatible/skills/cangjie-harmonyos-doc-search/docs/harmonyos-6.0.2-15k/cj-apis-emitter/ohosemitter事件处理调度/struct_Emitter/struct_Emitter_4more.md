## struct Emitter

```cangjie
public struct Emitter {}
```

**功能：** Emitter提供了持续订阅事件、单次订阅事件、取消订阅事件，以及发送事件到事件队列的能力。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### static func emit(InnerEvent, EventData)

```cangjie
public static func emit(event: InnerEvent, data!: EventData = EventData.Empty): Unit
```

**功能：** 发送指定优先级事件。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[InnerEvent](#class-innerevent)|是|-|发送的事件，其中[EventPriority](#enum-eventpriority)用于指定事件被发送的优先级。 |
|data|[EventData](#struct-eventdata)|否|EventData.Empty| **命名参数。** 事件携带的数据。|

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
import std.collection.HashMap

let p = HashMap<String, EventDataType>()
p.add("1", INT64(1))
p.add("2", BOOL(false))
p.add("3", STRING("3"))
let eventData = EventData(p)
let innerEvent = InnerEvent(1, priority: EventPriorityHIGH)
Emitter.emit(innerEvent, data: eventData)
```

### static func emit(String, Options, EventData)

```cangjie
public static func emit(
    eventId: String,
    options!: Options = Options(LOW),
    data!: EventData = EventData.Empty
): Unit
```

**功能：** 发送指定优先级事件。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|发送的事件ID，不支持空字符串。|
|options|[Options](#struct-options)|否|Options(LOW)| **命名参数。** 事件优先级。|
|data|[EventData](#struct-eventdata)|否|EventData.Empty| **命名参数。** 事件携带的数据。|

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
import std.collection.HashMap

let p = HashMap<String, EventDataType>()
p.add("1", INT64(1))
p.add("2", BOOL(false))
p.add("3", STRING("3"))
let priority = Options(EventPriority.HIGH)
let eventData = EventData(p)
Emitter.emit("eventId", options: priority, data: eventData)
```

### static func getListenerCount(UInt32)

```cangjie
public static func getListenerCount(eventId: UInt32): UInt32
```

**功能：** 获取指定事件的订阅数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|UInt32|是|-|事件ID，不支持空字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|事件ID。|

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
import ohos.base.*

// 此处代码可添加在依赖项定义中
func callback(eventData: EventData) {
    Hilog.info(0, "EmitterTest", "callback")
}

let f = EventCallback("callback", callback)
Emitter.on("eventId", f)
let count = Emitter.getListenerCount(1)
AppLog.info("count = ${count}")
```