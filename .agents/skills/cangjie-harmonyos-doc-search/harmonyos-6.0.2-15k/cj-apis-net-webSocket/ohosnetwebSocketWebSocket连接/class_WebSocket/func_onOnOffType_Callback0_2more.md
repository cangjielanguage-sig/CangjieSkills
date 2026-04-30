### func on(OnOffType, Callback0Argument)

```cangjie
public func on(`type`: OnOffType, callback: Callback0Argument): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.DATAEND。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

// 所需要的依赖项
class DataEndCallback <: Callback0Argument {
    let f: () -> Unit
    public init(f: () -> Unit) {
        this.f = f
    }

    public func invoke() {
        f()
    }
}

let ws: WebSocket = createWebSocket()
// on dataEnd
ws.on(
    OnOffType.DATAEND,
    DataEndCallback({
        => // success
    })
)
```

### func on(OnOffType, Callback1Argument\<ResponseHeaders>)

```cangjie
public func on(`type`: OnOffType, callback: Callback1Argument<ResponseHeaders>): Unit
```

**功能：** 订阅HTTP Response Header事件，使用callback方式作为同步方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[OnOffType](#enum-onofftype)|是|-|WebSocket的订阅事件类型，此时应传入OnOffType.DATAEND。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ResponseHeaders](#enum-responseheaders)>|是|-|回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

// 所需要的依赖项
class ReceiveCallback <: Callback1Argument<ResponseHeaders> {
    let f: (ResponseHeaders) -> Unit
    public init(f: (ResponseHeaders) -> Unit) {
        this.f = f
    }

    public func invoke(arg: ResponseHeaders) {
        f(arg)
    }
}

let ws: WebSocket = createWebSocket()
// on headerReceive
ws.on(
    OnOffType.HEADERRECEIVE,
    ReceiveCallback({
        data: ResponseHeaders => AppLog.info("Hello World!") // success
    })
)
```