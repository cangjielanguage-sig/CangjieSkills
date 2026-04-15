## class NetConnection

```cangjie
public class NetConnection {}
```

**功能：** 网络连接的句柄。

> **说明：**
>
>（1）设备从无网络状态转变为有网络状态时，将触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件；
>
>（2）接收到netAvailable事件后，若设备从有网络状态转变为无网络状态，将触发netLost事件；
>
>（3）若未接收到netAvailable事件，则将直接接收到netUnavailable事件；
>
>（4）设备从WiFi网络切换至蜂窝网络时，将先触发netLost事件（WiFi丢失），随后触发netAvailable事件（蜂窝可用）。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### func on(NetConnectionEvent, Callback1Argument\<NetHandle>)

```cangjie
public func on(event: NetConnectionEvent, callback: Callback1Argument<NetHandle>): Unit
```

**功能：** 订阅网络可用事件。此接口需在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[NetConnectionEvent](#enum-netconnectionevent)|是|-|网络连接事件类型，仅支持NetAvailable和NetLost事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[NetHandle](#class-nethandle)>|是|-|回调函数，返回数据网络句柄。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)。

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

// 定义NetAvailableCb类
class NetAvailableCb <: Callback1Argument<NetHandle> {
    let callback_: (NetHandle)->Unit
    public init(callback: (NetHandle)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: NetHandle): Unit {
        callback_(val)
    }
}

try {
    let netConn = createNetConnection()
    netConn.register()

    let netAvailableCallBack = NetAvailableCb({handle => Hilog.info(0, "net_connection test", "onNetAvailable handle is ${handle.netId}")})
    netConn.on(NetConnectionEvent.NetAvailable, netAvailableCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```