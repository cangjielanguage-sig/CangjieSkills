## class HttpRequest

```cangjie
public class HttpRequest {}
```

**功能：** HTTP请求任务。在调用HttpRequest的方法前，需要先通过[createHttp()](#func-createhttp)创建一个任务。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** 中断请求任务。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let httpRequest = createHttp()
    httpRequest.destroy()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(HttpRequestEvent, ?CallbackObject)

```cangjie
public func off(event: HttpRequestEvent, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅HTTP请求事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[HttpRequestEvent](#enum-httprequestevent)|是|-|要取消订阅的HTTP请求事件类型。|
|callback|?[CallbackObject](../arkinterop/cj-api-callback_invoke.md#class-callbackobject)|否|None|**命名参数。** 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。|

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
class HeadersReceiveCb <: Callback1Argument<HashMap<String, String>> {
    let callback_: (HashMap<String, String>)->Unit
    public init(callback: (HashMap<String, String>)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: HashMap<String, String>): Unit {
        callback_(val)
    }
}

try {
    let client = createHttp()

    let headersReceiveCallBack = HeadersReceiveCb({ map => Hilog.info(0, "test", "header info: ${map}") })
    client.on(HttpRequestEvent.HeadersReceive, headersReceiveCallBack)

    client.off(HttpRequestEvent.HeadersReceive)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```