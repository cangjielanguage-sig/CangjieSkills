### func on(OnOffType, WebSocketAsyncCallback\<MessageData>)

```cangjie
public func on(`type`: OnOffType, callback: WebSocketAsyncCallback<MessageData>): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.MESSAGE。|
|callback|[WebSocketAsyncCallback](#class-websocketasynccallback)\<[MessageData](#enum-messagedata)>|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import std.collection.*

let ws: WebSocket = createWebSocket()
// on message
let messageCallBack = WebSocketAsyncCallback<MessageData>(
    {
        errorCode: Option<AsyncError>, data: Option<MessageData> => match (errorCode) {
            case Some(e) => 0 // error
            case _ => match (data) {
                case Some(value) => 1 // success
                case _ => 0 // error
            }
        }
    })
ws.on(OnOffType.MESSAGE, messageCallBack)
ws.off(OnOffType.MESSAGE, callback: messageCallBack) // 取消订阅 messageCallBack 回调
ws.off(OnOffType.MESSAGE) // 取消订阅 OnOffType.MESSAGE 类型所有回调
```

### func on(OnOffType, WebSocketAsyncCallback\<CloseResult>)

```cangjie
public func on(`type`: OnOffType, callback: WebSocketAsyncCallback<CloseResult>): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.MESSAGE。|
|callback|[WebSocketAsyncCallback](#class-websocketasynccallback)\<[CloseResult](#class-closeresult)>|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let ws: WebSocket = createWebSocket()
// on close
let closeCallBack = WebSocketAsyncCallback<CloseResult>(
    {
        errorCode: Option<AsyncError>, data: Option<CloseResult> => match (errorCode) {
            case Some(e) => 0 // error
            case _ => match (data) {
                case Some(value) => 1 // success
                case _ => 0 // error
            }
        }
    })
ws.on(OnOffType.CLOSE, closeCallBack)
ws.off(OnOffType.CLOSE, callback: closeCallBack) // 取消订阅 closeCallBack 回调
ws.off(OnOffType.CLOSE) // 取消订阅 OnOffType.CLOSE 类型所有回调
```

### func on(OnOffType, WebSocketErrorCallback)

```cangjie
public func on(`type`: OnOffType, callback: WebSocketErrorCallback): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.ERROR。|
|callback|[WebSocketErrorCallback](#class-websocketerrorcallback)|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let ws: WebSocket = createWebSocket()
// on error
let errorCallBack = WebSocketErrorCallback({
    err: BusinessException => // ErrorCallback
})
ws.on(OnOffType.ERROR, errorCallBack)
ws.off(OnOffType.ERROR, callback:errorCallBack) // 取消订阅 errorCallBack 回调
ws.off(OnOffType.ERROR) // 取消订阅 OnOffType.ERROR 类型所有回调
```