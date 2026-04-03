### func connect(String, AsyncCallback\<Bool>, ?WebSocketRequestOptions)

```cangjie
public func connect(url: String, callback: AsyncCallback<Bool>,
options!: ?WebSocketRequestOptions = None): Unit
```

**功能：** 根据URL地址和header，建立一个WebSocket连接，使用AsyncCallback方式作为异步方法。

> **说明：**
>
> - 可通过监听error事件获得该接口的执行结果，错误发生时会得到错误码：200。
> - URL地址长度不能超过1024个字符，否则会连接失败。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|建立WebSocket连接的URL地址。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Bool>|是|-|以AsyncCallback形式返回建立连接的结果。|
|options|?[WebSocketRequestOptions](#class-websocketrequestoptions)|否|None|参考[WebSocketRequestOptions](#class-websocketrequestoptions)。默认为None。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webSocket错误码](../../errorcodes/cj-errorcode-net-websocket.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |201|Permission denied.|
  |2302001|Websocket url error.|
  |2302002|Websocket certificate file does not exist.|
  |2302003|Websocket connection already exists.|
  |2302998|It is not allowed to access this domain.|
  |2302999|Websocket other unknown error.|

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
```