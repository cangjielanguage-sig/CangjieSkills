### func on(HttpRequestEvent, Callback1Argument\<HashMap\<String,String>>)

```cangjie
public func on(event: HttpRequestEvent, callback: Callback1Argument<HashMap<String, String>>): Unit
```

**功能：** 订阅HTTP Response Header 事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[HttpRequestEvent](#enum-httprequestevent)|是|-|HTTP请求事件类型，仅支持HeadersReceive事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<HashMap\<String,String>>|是|-|回调函数，返回HTTP响应头对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[HTTP错误码](./cj-errorcode-net-http.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 2100001 | Invalid parameter value. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*
import std.collection.HashMap

// 定义HeadersReceiveCb类
class HeadersReceiveCb1 <: Callback1Argument<HashMap<String, String>> {
    let callback_: (HashMap<String, String>)->Unit
    public init(callback: (HashMap<String, String>)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: HashMap<String, String>): Unit {
        callback_(val)
    }
}

try {
    let client = createHttp()

    let headersReceiveCallBack = HeadersReceiveCb1({ map => Hilog.info(0, "test", "header info: ${map}") })
    client.on(HttpRequestEvent.HeadersReceive, headersReceiveCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func on(HttpRequestEvent, Callback1Argument\<Array\<Byte>>)

```cangjie
public func on(event: HttpRequestEvent, callback: Callback1Argument<Array<Byte>>): Unit
```

**功能：** 订阅HTTP流式响应数据接收事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[HttpRequestEvent](#enum-httprequestevent)|是|-|HTTP请求事件类型，仅支持DataReceive事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<Array\<Byte>>|是|-|回调函数，用于接收HTTP流式响应数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[HTTP错误码](./cj-errorcode-net-http.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 2100001 | Invalid parameter value. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

// 定义DataReceiveCb类
class DataReceiveCb <: Callback1Argument<Array<Byte>> {
    let callback_: (Array<Byte>)->Unit
    public init(callback: (Array<Byte>)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: Array<Byte>): Unit {
        callback_(val)
    }
}

try {
    let client = createHttp()

    let dataReceiveCallBack = DataReceiveCb({ bytes => Hilog.info(0, "test", "data info : ${bytes}") })
    client.on(HttpRequestEvent.DataReceive, dataReceiveCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```