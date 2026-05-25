## class WebSocket

```cangjie
public class WebSocket {}
```

**功能：** 在调用WebSocket的方法前，需要先通过[webSocket.createWebSocket](#func-createwebsocket)创建一个WebSocket。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### func close(AsyncCallback\<Bool>, ?WebSocketCloseOptions)

```cangjie
public func close(callback: AsyncCallback<Bool>,
options!: ?WebSocketCloseOptions = None): Unit
```

**功能：** 关闭WebSocket连接，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Bool>|是|-|回调函数。|
|options|?[WebSocketCloseOptions](#class-websocketcloseoptions)|否|None|参考[WebSocketCloseOptions](#class-websocketcloseoptions)。默认为None。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |201|Permission denied.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import std.collection.HashMap

let ws: WebSocket = createWebSocket()
let options: WebSocketRequestOptions = WebSocketRequestOptions(
    header: HashMap<String, String>([("content-type", "application/json")]))
let availableWebSocketAddress: String = 'wss://ws.welive.huawei.com/'
ws.connect(
    availableWebSocketAddress,
    {
        errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
            case Some(e) => 0 // error
            case _ => match (data) {
                case Some(value) => 1 // success
                case _ => 0 // error
            }
        }
    },
    options: options
)
ws.close(
    {
        errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
            case Some(e) => 0 // error
            case _ => match (data) {
                case Some(value) => 1 // success
                case _ => 0 // error
            }
        }
    })
```