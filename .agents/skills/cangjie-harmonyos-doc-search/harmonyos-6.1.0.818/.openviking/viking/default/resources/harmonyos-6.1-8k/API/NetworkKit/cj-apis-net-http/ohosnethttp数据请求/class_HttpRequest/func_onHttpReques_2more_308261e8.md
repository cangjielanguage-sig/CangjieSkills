### func on(HttpRequestEvent, Callback0Argument)

```cangjie
public func on(event: HttpRequestEvent, callback: Callback0Argument): Unit
```

**功能：** 订阅HTTP流式响应数据接收完毕事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[HttpRequestEvent](#enum-httprequestevent)|是|-|HTTP请求事件类型，仅支持DataEnd事件。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数。|

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

// 定义DataEndCb类
class DataEndCb <: Callback0Argument {
    let callback_: ()->Unit
    public init(callback: ()->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException): Unit {
        callback_()
    }
}

try {
    let client = createHttp()

    let dataEndCallBack = DataEndCb({ => Hilog.info(0, "test", "data end") })
    client.on(HttpRequestEvent.DataEnd, dataEndCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func on(HttpRequestEvent, Callback1Argument\<DataReceiveProgressInfo>)

```cangjie
public func on(event: HttpRequestEvent, callback: Callback1Argument<DataReceiveProgressInfo>): Unit
```

**功能：** 订阅HTTP流式响应数据接收进度事件。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[HttpRequestEvent](#enum-httprequestevent)|是|-|HTTP请求事件类型，仅支持DataReceiveProgress事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[DataReceiveProgressInfo](#class-datareceiveprogressinfo)>|是|-|回调函数，用于接收数据接收进度信息，参数为DataReceiveProgressInfo对象。|

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

// 定义DataReceiveProgressCb类
class DataReceiveProgressCb <: Callback1Argument<DataReceiveProgressInfo> {
    let callback_: (DataReceiveProgressInfo)->Unit
    public init(callback: (DataReceiveProgressInfo)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: DataReceiveProgressInfo): Unit {
        callback_(val)
    }
}

try {
    let client = createHttp()

    let dataReceiveProgressCallBack = DataReceiveProgressCb({ info => Hilog.info(0, "test", "receive progress ${info.receiveSize} ${info.totalSize} ") })
    client.on(HttpRequestEvent.DataReceiveProgress, dataReceiveProgressCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```