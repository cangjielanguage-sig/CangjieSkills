### func send(MessageData, AsyncCallback\<Bool>)

```cangjie
public func send(data: MessageData, callback: AsyncCallback<Bool>): Unit
```

**功能：** 通过WebSocket连接发送数据，使用callback方式作为异步方法。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[MessageData](#enum-messagedata)|是|-|发送的数据。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Bool>|是|-|回调函数。|

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

let options: WebSocketRequestOptions = WebSocketRequestOptions(
    header: HashMap<String, String>([("content-type", "application/json")]))
let availableWebSocketAddress: String = 'wss://ws.welive.huawei.com/'
let ws: WebSocket = createWebSocket()
// on open
let openCallBack = WebSocketAsyncCallback<HashMap<UInt32, String>>(
    {
        errorCode: Option<AsyncError>, data: Option<HashMap<UInt32, String>> => match (errorCode) {
            case Some(e) => () // error
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
                case _ => () // error
            }
        }
    })
ws.on(OnOffType.OPEN, openCallBack)

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