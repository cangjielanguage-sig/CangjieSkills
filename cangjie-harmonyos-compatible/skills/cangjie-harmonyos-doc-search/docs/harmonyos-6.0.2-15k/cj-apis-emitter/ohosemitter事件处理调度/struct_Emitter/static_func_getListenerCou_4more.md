### static func getListenerCount(String)

```cangjie
public static func getListenerCount(eventId: String): UInt32
```

**功能：** 获取指定事件的订阅数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|事件ID，不支持空字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|事件ID，不支持空字符串。|

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
let count = Emitter.getListenerCount("eventId")
AppLog.info("count = ${count}")
```

### static func off(UInt32)

```cangjie
public static func off(eventId: UInt32): Unit
```

**功能：** 取消针对该事件ID的订阅。若该事件已经通过on或者once接口订阅，则取消该订阅；否则，不做任何处理。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|UInt32|是|-|事件ID，不支持空字符串。|

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

// 取消eventID为1的所有事件回调处理函数
Emitter.off(1)
```

### static func off(String)

```cangjie
public static func off(eventId: String): Unit
```

**功能：** 取消针对该事件ID的订阅。若该事件已经通过on或者once接口订阅，则取消该订阅；否则，不做任何处理。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|String|是|-|事件ID，不支持空字符串。|

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

let eventId: String = "id1"
Emitter.off(eventId)
```

### static func off(UInt32, EventCallback)

```cangjie
public static func off(eventId: UInt32, callback: EventCallback): Unit
```

**功能：** 取消针对该事件ID的订阅。若该事件已经通过on或者once接口订阅，则取消该订阅；否则，不做任何处理。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|UInt32|是|-|事件ID，不支持空字符串。|
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
Emitter.off(1, f)
```