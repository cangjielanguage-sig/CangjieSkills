### func off(OnOffType, ?CallbackObject)

```cangjie
public func off(`type`: OnOffType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅WebSocket的指定的[OnOffType](#enum-onofftype)类型消息事件。

> **说明：**
>
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 订阅WebSocket事件时，传入的Callback类型。默认为None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import std.collection.*

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
ws.off(OnOffType.CLOSE, callback:closeCallBack) // 取消订阅 closeCallBack 回调
ws.off(OnOffType.CLOSE) // 取消订阅 OnOffType.CLOSE 类型所有回调
```

### func on(OnOffType, WebSocketAsyncCallback\<HashMap\<UInt32,String>>)

```cangjie
public func on(`type`: OnOffType, callback: WebSocketAsyncCallback<HashMap<UInt32, String>>): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.OPEN。|
|callback|[WebSocketAsyncCallback](#class-websocketasynccallback)\<HashMap\<UInt32,String>>|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import std.collection.*

let ws: WebSocket = createWebSocket()
let openCallBack = WebSocketAsyncCallback<HashMap<UInt32, String>>(
    {
        errorCode: Option<AsyncError>, data: Option<HashMap<UInt32, String>> => match (errorCode) {
            case Some(e) => 0 // error
            case _ => match (data) {
                case Some(value) => ws.send(
                    STRING_DATA("Hello, server!"),
                    {
                        errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
                            case Some(e) => 0 // error
                            case _ => match (data) {
                                case Some(value) => 1 // success
                                case _ => 0 // error
                            }
                        }
                    }
                )
                case _ => errorCode // error
            }
        }
    })
ws.on(OnOffType.OPEN, openCallBack)
ws.off(OnOffType.OPEN , callback:openCallBack) // 取消订阅 openCallBack 回调
ws.off(OnOffType.OPEN) // 取消订阅 OnOffType.OPEN 类型所有回调
```